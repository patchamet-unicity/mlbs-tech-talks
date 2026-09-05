---
name: worker-pool-mode
description: Turn the current Codex task into an opt-in manager for a reusable pool of up to two separate Terra medium Codex Desktop worker tasks in the mlbs-tech-talks space. Use when the user invokes worker-pool-mode, asks to delegate work to a worker, wants idle workers reused, or wants parallel worker management. Ordinary tasks remain single-agent until the user activates this mode or explicitly requests a worker.
---

# Worker Pool Mode

Keep the current task as the user-facing manager while bounded supporting work runs in separate Codex Desktop tasks visible in the sidebar. The manager interprets the request, assigns work, reviews worker results, and gives the final answer.

Workers are real peer tasks, not hidden subagents. Do not create them merely because parallel work is possible.

## Activation

- `$worker-pool-mode <work>` or an explicit request to send work to a worker is a one-shot dispatch.
- `$worker-pool-mode on` enables manager judgment for later suitable work in the current task until the user turns it off.
- `$worker-pool-mode status` reports worker tasks and their states without creating, interrupting, or archiving anything.
- `$worker-pool-mode off` stops new delegation. Let active workers finish unless the user explicitly asks to interrupt them.

An ordinary task starts in single-agent mode.

## Decide whether to delegate

While the mode is active, delegate when a subtask is bounded and independent enough to save time, protect the manager's context, or improve verification. Good candidates include focused exploration, reviewing existing slide behavior, testing, researching one design option, implementing a clearly owned file, and independently checking a finished artifact.

Keep work in the manager when it is small, linear, tightly coupled to the next decision, or cheaper to do directly. Do not split write-heavy work across workers that would edit the same files. An explicit request to use a worker overrides the preference to work alone, within the user's existing authorization and safety boundaries.

## Pool identity and ledger

This space has exactly two reusable worker slots:

- `TechTalks · Worker 1`
- `TechTalks · Worker 2`

Never create `TechTalks · Worker 3` or a differently named replacement that bypasses the two-worker limit.

Maintain a compact ledger in the manager's context with each worker's title, task ID, host ID, latest wait cursor, state, and current or most recent assignment. States are `starting`, `working`, `needs-attention`, `idle`, and `closed`.

Call `list_threads` before every dispatch to reconcile the ledger. Prefer recorded task IDs over title matching. A completed worker remains reusable even when it is no longer among the most recent tasks.

## Create a worker

When no existing worker is idle and fewer than two worker tasks exist:

1. Call `list_projects` and resolve the saved `mlbs-tech-talks` project. Never guess its project ID.
2. Create the lowest available worker title with `create_thread` using:
   - model `gpt-5.6-terra`
   - thinking `medium`
   - the saved `mlbs-tech-talks` project
   - `environment: local` so the worker shares the repository checkout and follows the repo convention of working directly on `main`
3. Record the returned task and host IDs immediately.
4. Use `wait_threads` to observe startup and completion. Task creation is asynchronous, so do not report completion from creation alone.

Do not use hidden subagents for pool members and do not create a repository worktree.

Every new worker prompt must be self-contained because it does not inherit this conversation. Include:

- its exact worker title and concrete objective
- the active talk and its `HANDOFF.md` path when the work belongs to a talk
- exact files or components it owns for write work
- the minimum relevant paths, context, settled decisions, constraints, and acceptance criteria
- expected verification
- a warning that all tasks share the checkout, so it must preserve unrelated edits and never revert them
- repo conventions: work directly on `main` and stage only explicit paths
- whether commit or push is authorized; omit those actions unless the user asked for them
- the return format: outcome, changed or inspected files, verification, unresolved risks, and any decision needed
- an instruction not to create more tasks or delegate its assignment

Creating a worker does not broaden the actions already authorized by the user.

## Dispatch or reuse

1. Reuse the lowest-numbered `idle` worker with `send_message_to_thread`. Send a fresh complete brief and tell it not to carry assumptions from its previous assignment.
2. If all existing workers are busy and only one exists, create Worker 2.
3. If both workers are busy, wait for one or keep the work in the manager. Never create a third worker.
4. Do not queue unrelated work onto a busy worker.
5. Wait on active workers together with `wait_threads`, carrying each cursor forward and avoiding noisy polling.

A worker becomes `idle` only after the manager receives its final report and no revision is pending. If a worker is archived or inaccessible, mark it `closed`; ask the user before restoring or replacing it.

## Review worker results

Worker completion is input for review, not automatic acceptance.

1. Inspect the report and relevant files, diff, rendered slide, test output, or source evidence in proportion to the task's risk.
2. If the result is incomplete or incorrect, send concrete feedback to the same worker and request a revision.
3. Wait for the revision and review again.
4. Bring a decision to the user only when missing information, new authority, or a genuine design choice blocks progress.

The manager owns conflicts between worker outputs and the consolidated final response. Keep worker bookkeeping brief unless the user asks for status.

## Pool lifetime

Completed workers stay reusable and visible in the sidebar. Never archive, rename, or delete them without an explicit user request. Turning the mode off changes delegation behavior only; it does not close existing workers.
