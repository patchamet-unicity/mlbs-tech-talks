---
name: save-handoff
description: Update a talk's HANDOFF.md with the current working state so a later Codex session can resume immediately. Use when the user asks to save, prepare, record, or update a handoff before stopping or switching sessions.
---

# Save Handoff

Update the active talk's `HANDOFF.md` as a concise, self-contained snapshot for the next Codex session.

## Find the handoff

- Use the talk named or implied by the conversation.
- If it is unclear, inspect `talks/*/HANDOFF.md`, recent changed files, and the current conversation. Ask only when more than one talk remains genuinely plausible.
- Read the existing `HANDOFF.md`, the talk's `NOTES.md` when relevant, and any documentation explicitly referenced by the handoff.
- Inspect `git status` and the scoped diff so uncommitted work is represented accurately. Do not assume every repository change belongs to this session.

## Update it

Treat `HANDOFF.md` as current state, not an append-only session log. Preserve still-valid decisions and constraints, remove or rewrite stale status, and keep enough detail that a fresh session does not need the old chat.

Capture only what materially helps continuation:

- current stage and what is complete
- work completed or changed in the latest session
- important decisions, rejected directions, and invariants that must remain intact
- exact files or components involved
- unfinished work, blockers, and unanswered user questions
- ordered next actions, with the first action concrete enough to start immediately
- verification already performed and anything still unverified

Use evidence from the files, diffs, commands, and conversation. Clearly label uncertainty; never invent completion, decisions, test results, or user approval. Keep durable talk content in `NOTES.md`; keep only execution state and continuation context in `HANDOFF.md`.

Prefer editing existing sections over duplicating information. Add a new heading only when the current structure cannot express an important state. Keep paths and commands exact, and keep the writing compact even when the handoff itself is detailed.

## Finish

- Re-read the resulting `HANDOFF.md` and compare it with the scoped diff and current conversation.
- Report which handoff was updated and summarize the next action.
- Do not commit, push, or modify unrelated files unless the user explicitly asks.
