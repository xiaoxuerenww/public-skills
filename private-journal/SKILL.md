---
name: journal
description: |
  Daily ledger and sprint tracker. Use when the user journals, plans their day, logs a daily update, starts or updates a sprint, or posts progress against sprint goals.
---

# Journal

Two modes — **ledger** (daily append-only log) and **sprint** (goal-bounded push with a dedicated doc). Detect the mode from the user's input:

- Mentions "sprint", names a multi-day goal with dates, or an active `sprint_*.md` exists and the message is a progress update → **Sprint**
- Everything else → **Ledger**

If ambiguous, ask which mode.

## Configuration

**Always read `config.md` first** to get the active journal and sprint directories. Paths are:
- **Journal directory**: where `journal.md` lives (default: skill base dir)
- **Sprint directory**: where active sprint docs live (can be external, e.g., job-specific folder)

When the user moves a sprint or changes directories, update `config.md` with the new paths.

---

## Ledger

Append a dated section to `journal.md` in the active journal directory. Never overwrite previous entries.

### Steps

1. **Read** `config.md` to get the journal directory path.
   _Done when_: you have the absolute path to the journal directory.

2. **Read** `<journal_dir>/journal.md` if it exists. Note the last entry date.
   _Done when_: you know today's date and whether an entry for today already exists.

3. **Gather** the user's input — plan, log, or both.
   _Done when_: you have at least one actionable item to record.

4. **Write** a new dated section (or update today's existing section) using the format in `TEMPLATE_LEDGER.md`.
   _Done when_: the section is appended, previous entries untouched, and you confirm the file path to the user.

---

## Sprint

A sprint lives in a dedicated file: `sprint_YYYY_MM_<topic>.md` in the active sprint directory (e.g., `sprint_2026_07_ml-interview-prep.md`). Use the sprint start month for `YYYY_MM`.

### Branch: Init

Trigger: user says "start sprint" or names goals with dates and no active sprint doc matches.

1. **Read** `config.md` to get the sprint directory path.
   _Done when_: you have the absolute path to the sprint directory.

2. **Gather** sprint name, goals (concrete deliverables), start/end dates, sprint directory (if different from current), and any intermediate milestones. Ask for what's missing.
   _Done when_: all inputs collected.

3. **Draft** the sprint doc using the format in `TEMPLATE_SPRINT.md`. Present the plan to the user.
   _Done when_: user confirms or requests changes.

4. **Create** `<sprint_dir>/sprint_YYYY_MM_<topic>.md` with the confirmed plan. If the sprint directory differs from the current one in `config.md`, update `config.md`.
   _Done when_: file written, config updated if needed, and path confirmed to the user.

### Branch: Update

Trigger: user posts progress and an active sprint doc (`Status: Active`) exists.

1. **Read** `config.md` to get the sprint directory path.
   _Done when_: you have the absolute path to the sprint directory.

2. **Find and read** the active sprint doc in that directory (look for `Status: Active`). Identify which tasks the update touches.
   _Done when_: you can map the update to specific plan rows.

3. **Update** two sections of the sprint doc:
   - Plan table: change status of affected rows (`done` / `in-progress` / `blocked` / `skipped`).
   - Daily Log: append a dated entry summarizing what changed and why.
   If the update implies a scope or timeline shift, propose the adjustment before writing.
   _Done when_: both sections updated, and you confirm what changed.

### Branch: Close

Trigger: user says "close sprint" or "end sprint".

1. **Read** `config.md` to get the sprint directory path.
   _Done when_: you have the absolute path to the sprint directory.

2. **Read** the active sprint doc. Set `Status` to `Completed` (or `Abandoned` if user says so).

3. **Add** a `## Retrospective` section with placeholders: goals met vs. missed, what worked, what to change. Prompt the user to fill it in — do not fabricate.
   _Done when_: status updated, retrospective section present, user prompted.
