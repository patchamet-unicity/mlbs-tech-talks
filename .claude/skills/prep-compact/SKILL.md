---
name: prep-compact
description: Prepare the session for /compact — update the active talk's HANDOFF.md with right-now state, then commit+push this session's files (via push-session discipline), then tell the user it's safe to /compact. Use when the user signals an upcoming /compact in any wording — "จะ push แล้ว compact ก่อนอะ", "เตรียม compact", "จะ compact ละ", "prep compact", "going to compact", "about to compact", "push แล้วจะ compact" — with or without the push mentioned. The actual /compact is run by the user afterwards (built-in, can't be intercepted).
---

# prep-compact

The user is about to run `/compact`. `/compact` collapses the conversation
to a summary that keeps intent but loses fine-grained working state — the
current step, last few decisions, the next concrete action. This skill
externalizes that state into the active talk's handoff doc and pushes it,
so a post-compact session can re-orient from the file.

It is a thin composition of two things:

1. Update the **live handoff** for the talk being worked on.
2. The **push-session** skill's staging discipline (commit+push ONLY this
   session's files — never `git add -A`).

## Inputs

- `-y` / `--yes` (optional) — passed through to the push step: skip the
  push confirmation prompt. The handoff update itself never needs
  confirmation (it's this session's own working doc).
- The user saying "push เลย" / "ไม่ต้องถาม" in the same breath counts
  as `-y`.

## Steps

### 1. Identify the active talk

From recent conversation context: which `talks/<YYYY-MM-topic>/` folder
this session is working in. The handoff lives at
`talks/<talk>/HANDOFF.md`.

**No active talk** (repo-level session — editing README, fixing a skill,
restructuring):

- Trivial / read-only session → skip the handoff, go straight to Step 3
  (push), and say so: "session นี้ไม่ได้ทำ talk ไหน — ไม่มี handoff
  ให้อัปเดต, push อย่างเดียว".
- Non-trivial repo-level work → note the state at the top of the relevant
  file itself, or in a short `HANDOFF.md` at the repo root (delete it when
  the work completes).

### 2. Update the live handoff

Read the existing `talks/<talk>/HANDOFF.md` (create it if missing) and
**overwrite** it to reflect *right-now* state — not end-of-session prose:

- Which stage of the talk we're at (คิดหัวข้อ / outline / เนื้อหา /
  สไลด์ / ซ้อม)
- Decisions made since the previous handoff update (structure chosen,
  slides locked, examples picked/dropped)
- Pending decisions / open questions to resolve next
- Files recently touched that matter
- The **next concrete action** when resumed

Keep it current — overwrite in place, never `HANDOFF-v2.md`.
`HANDOFF.md` is working state, separate from `NOTES.md` (which holds the
talk's actual content/script/references).

### 3. Commit + push this session's files

Follow the **push-session** skill's steps exactly (it is the source of
truth for the staging discipline): build this session's touched-file set
(now including the handoff just updated), reconcile with `git status`,
stage by explicit path only, draft an English conventional-commit
message, show the 📦/⏳ confirmation table `(y/n)` — or proceed
immediately if `-y` — then commit and push.

All of push-session's **stop conditions** apply unchanged. If the push
step stops, the handoff update from Step 2 is still on disk — say so, so
the user knows state is preserved locally even though the push didn't
land.

### 4. Report — safe to compact

One line, ending with the go-signal:

> Handoff updated → commit `<sha>` pushed to `<upstream>`.
> **Safe to /compact now.** 🟢

The user runs `/compact` themselves. After compact, the fresh session
re-orients by reading `talks/<talk>/HANDOFF.md` first, summarizing where
things stand, and waiting for direction.

## What this skill does NOT do

- Does **not** run `/compact` (built-in; user runs it).
- Does **not** stage other sessions' files — push-session rules apply.
- Does **not** rewrite NOTES.md or slides content; only the handoff.

## Related

- `.claude/skills/push-session/` — the staging/commit/push discipline
  reused in Step 3.
