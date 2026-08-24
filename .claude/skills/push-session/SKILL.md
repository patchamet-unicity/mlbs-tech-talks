---
name: push-session
description: Commit and push ONLY the files the current session touched — a shortcut for "push the files related to this session". Reconciles the files this session created/edited/deleted (via Edit/Write/NotebookEdit) against `git status`, stages just those (NEVER `git add -A`/`.`), drafts an English conventional-commit message, confirms the file list + message with the user (y/n — skippable with `-y`), then commits to the current branch and pushes. Leaves other concurrent sessions' uncommitted changes untouched. Use when the user says "push ไฟล์ที่เกี่ยวข้องกับ session นี้", "push ไฟล์ session นี้", "push my files", "commit+push this session's files", or similar.
---

# push-session

A typing shortcut. The user may run several Claude sessions at once against
the **same** working tree (this repo works directly on `main`), so
`git status` can fill up with changes from more than one session. They don't
want to type out "push the files related to *this* session" each time —
that's all this skill is.

**The hard part is not the git commands — it's staging only this session's
files and nothing else.** This skill exists to encode that discipline
consistently so a stray `git add .` never sweeps another session's
in-flight work into a commit.

## Core rules (non-negotiable)

- **NEVER** `git add -A`, `git add .`, `git add -u`, or `git commit -a`.
  Stage by **explicit path only**.
- **NEVER** stage a file this session did not touch. Files in `git status`
  that this session didn't create/edit belong to other sessions or
  pre-existed — leave them alone.
- **Always confirm** the exact file list + commit message with `(y/n)`
  before committing. Push only after the commit succeeds. The **only**
  exception is the `-y` flag (see Inputs), which skips *just* that one
  prompt — every stop condition below still stops.
- If this session's touched-file set **can't be determined confidently**
  (e.g. the conversation was `/compact`-ed and the edit history is gone),
  do NOT guess. Stop, show `git status`, say so, and ask the user to name
  the files.
- **On a collision with another session, STOP and report — never race.**
  A commit in progress (`.git/index.lock` exists) or a push rejection
  (remote moved ahead) → stop, name what's colliding, and let the user
  decide. No retry loops, no auto-rebase, no force.

## Inputs

- `-y` / `--yes` (optional flag) — skip the `(y/n)` confirmation in Step 4
  and go straight to commit + push. The 📦/⏳ file table is **still
  printed**, just not waited on. This flag skips **only** that prompt —
  every entry under **Stop conditions** still stops the run, and it never
  implies `--force`, a rebase, or `git add -A`.
- `<message>` (optional, free text) — override the commit message. Still
  shown in the confirmation step; the user can still `n`. Without it, the
  skill drafts a message from the staged paths.

Order doesn't matter. A leading `-y` is always the flag, never part of the
message. The user asking in chat to "push เลย" / "ไม่ต้องถาม" in the same
breath as invoking the skill counts as `-y`.

## Steps

### 1. Build this session's touched-file set

From **this conversation**, list every file path I created, modified,
deleted, or renamed via `Edit`, `Write`, `NotebookEdit`, or an explicit
file-move command I ran. Call this `SESSION_FILES`. Normalize to
repo-relative paths so they match `git status` output. If I genuinely
can't reconstruct this (post-compact, no edit history) → go to the
**Can't-attribute** stop condition below.

### 2. Reconcile with the working tree

```powershell
git status --porcelain=v1
```

Partition the changed paths:

- `TO_STAGE` = `SESSION_FILES` ∩ changed paths. **These get committed.**
  Handle every status code: modified (` M`/`M `), added/untracked (`??`),
  deleted (` D`/`D `), renamed (`R `, stage both old and new path).
- `EXCLUDED` = changed paths **not** in `SESSION_FILES`. These are other
  sessions' WIP or pre-existing changes — **never staged**, but listed in
  the confirmation for transparency.
- `SESSION_FILES` not in `git status` (already committed earlier, or
  change reverted) → silently ignored.

If `TO_STAGE` is empty → report "No files from this session to push." and
stop (don't commit an empty change).

### 3. Draft the commit message

- If the user passed `<message>`, use it verbatim.
- Otherwise draft one in **English**, conventional-commit style, matching
  recent history (`git log --oneline -15`). Infer `type`/`scope` from the
  staged paths for **this repo**:
  - `talks/<talk>/**` → `feat(<talk-slug>)` (new content) /
    `docs(<talk-slug>)` (notes, handoff) — e.g. `feat(2026-09-cheap): draft outline`
  - `.claude/skills/**` → `feat(skills)` (new) / `chore(skills)` (tweak)
  - `README.md`, root config → `docs(repo)` / `chore(repo)`
  - Mixed → pick the dominant area; keep the summary specific.
- Keep the subject line tight and specific (what changed, not "update
  files").

### 4. Confirm (🛑 y/n — skipped with `-y`)

Print the confirmation in this **exact Markdown layout** (rendered for the
user — not a code block). One `📦` line per `TO_STAGE` file; one `⏳` line
per `EXCLUDED` file:

```
### 🚀 Ready to Push Session
**Repo:** <repo name> (`<branch>` ➔ `<upstream>`)

---

#### 📦 ไฟล์ที่จะ Commit (Session นี้)
* 🟢 **Modified:** talks/2026-09-foo/NOTES.md
* 🆕 **Added:** talks/2026-09-foo/slides/outline.md

#### ⏳ ไฟล์ที่ไม่มีการเปลี่ยนแปลง (ของ Session อื่น)
* ⚪ **Modified:** README.md

---

#### 💬 Commit Message
> `<type(scope): summary>`

**คุณต้องการ Commit ไฟล์นี้ (<N> ไฟล์) แล้ว Push ขึ้น `<upstream>` เลยมั้ยครับ?** `(y/n)`
```

- **Per-file status emoji** — map each porcelain code:
  🟢 **Modified** (` M`/`M `) · 🆕 **Added** (`??`/`A `) ·
  🔴 **Deleted** (` D`/`D `) · 🔁 **Renamed** (`R ` — show `old ➔ new`).
  In the `⏳` (excluded) section use ⚪ for every file regardless of code.
- `<N>` = count of `TO_STAGE` files.
- If `EXCLUDED` is empty, **omit** the entire `⏳` section.
- 🛑 **Wait for explicit `y`.** Anything else → abort, change nothing.
- **With `-y`**: print the same table, replace the trailing question with
  `**`-y` — commit + push ทันที ไม่รอ confirm**`, and continue straight to
  Step 5. Do **not** ask, and do **not** skip printing the table.

### 5. Stage, commit, push

Only after `y` (or immediately, when `-y` was passed):

**Collision pre-check** — if `.git/index.lock` exists, another session is
mid-commit *right now*. Do NOT delete the lock or wait-loop. One immediate
re-check is fine; if it's still there, stop and report.

```powershell
git add -- "<path1>" "<path2>" …     # explicit paths ONLY
git commit -m "<message>"
git push
```

- Quote every path. `git add -- <path>` correctly stages modifications,
  new files, **and** deletions. For a rename, pass both old and new paths.
- If the branch has **no** upstream: `git push -u origin <branch>`.
- If `commit` fails (e.g. a hook rejects) → **do not push**. Report and
  stop.
- If `push` is rejected (remote moved ahead) → **stop** (no force, no
  auto-rebase). Show who won the race:

  ```powershell
  git fetch origin
  git log --oneline HEAD..origin/<branch>
  ```

  The usual resolution is a simple `git pull --rebase` — but only on the
  user's y.

### 6. Report

One line: the commit hash + subject, count of files, and push result. If
anything was left untouched, restate the excluded count so the user
remembers other sessions still have uncommitted work.

## Stop conditions

**`-y` does not bypass any of these.** It only skips the Step 4 prompt.

- **Can't-attribute**: edit history for this session is unavailable
  (post-compact, fresh session). Stop, show `git status`, ask the user to
  name the files. Never guess-and-commit.
- **Nothing to stage** → report and stop.
- **Commit hook failure** → report, do not push.
- **Another session mid-commit** (`index.lock` after one re-check) → stop.
- **Push rejected** → report which commits won the race, no force, no
  rebase without a y.

## What this skill does NOT do

- Does **not** run `git add -A` / `.` / `-u`, or `git commit -a` — ever.
- Does **not** stage, stash, or revert other sessions' changes.
- Does **not** create or switch branches — commits to the current branch
  (this repo works directly on `main` by design).
- Does **not** pull or rebase.
