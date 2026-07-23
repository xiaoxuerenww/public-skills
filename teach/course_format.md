# index.md Format

`index.md` lives at the root of each teaching directory, for example `rag_course/index.md`. It is the course index, mission, and cross-session manual. It should let the user resume the course after days or weeks without remembering the previous chat.

## Template

```md
# Course: {Topic}

## How to use this course

- Start here at the beginning of every session.
- Read the mission, current status, course tasks, and review schedule.
- Ask the agent: "continue this course from [[index.md]]".
- Do the retrieval practice before reading the answer key.
- Check off a task only after the lesson and its retrieval practice are complete.

## Mission

### Why
{1-3 sentences. The concrete real-world goal the user is chasing.}

### Success looks like
- {A specific, observable thing the user will be able to do}
- {Another specific thing}

### Constraints
- {Time, budget, learning preferences, or other constraints}

### Out of scope
- {Adjacent topics not worth chasing right now}

## Status

- Current status: not started | in progress | paused | review | complete
- Current focus: {one sentence}

## Course tasks

- [ ] Read `index.md` to understand the course mission and progress. (5 min)
- [ ] Read `solution.md` for the active lesson, drills, Q&A, and quiz notes. (15-25 min)
- [ ] Read `deep_dive.md` for the polished synthesis, formulas, glossary, sources, and quick review, if present. (15-30 min)
- [ ] **Task 1: {lesson title}** ({estimated time}) - [[solution.md#{lesson heading}]] - {one-line purpose}
- [ ] **Task 2: {lesson title}** ({estimated time}) - [[solution.md#{lesson heading}]] - {one-line purpose}
- [ ] **Task 3: {planned task}** ({estimated time}) - {one-line purpose}

## Review schedule

- {date or cadence}: {retrieval prompt or concept to review}
- {date or cadence}: {retrieval prompt or concept to review}

## Deep dive

- [[deep_dive.md]] - Polished synthesis, source list, glossary, formulas, snippets, and compact durable study material.
- `code/` - Runnable Python, PyTorch, notebook, script, or multi-file examples linked from [[solution.md]] or [[deep_dive.md]].

## Companion and quiz modes

- Companion learning notes: [[learn_notes.md]]
- Quiz notes, feedback, weakness tracking, and interview verdicts: [[solution.md]]
- Finished synthesis: [[deep_dive.md]]
- To continue open-ended Q&A: ask `$teach companion mode` and then ask questions.
- To practice active recall: ask `$teach quiz mode`.
- To finish the course: ask `finish $teach {course_name}`.

## Learning records

- {YYYY-MM-DD}: {durable insight, corrected misconception, weak spot, or strong interview phrasing}. Next action: {specific review, drill, or task link}.
```

## Rules

- Keep it short enough to scan in under two minutes.
- Use `## Course tasks` as the source of truth for progress; do not add separate `## Completed lessons` or `## Next session` sections.
- Every course task must be a checkbox and include an estimated time, such as `(15 min)`, `(30-45 min)`, or `(2 sessions)`.
- Include a checkbox plan for reading all active course docs: `index.md`, `solution.md`, and `deep_dive.md` when it exists or is non-empty.
- Mark a task complete only when the user has completed the lesson and retrieval practice, not merely when the file exists.
- Fold the mission into `index.md`; do not create a separate mission file.
- Store resources in `deep_dive.md`; do not create separate resource files.
- Store runnable code examples in `code/`; keep only short illustrative snippets inline.
- Use lower-case snake_case for generated file names and directory names.
- Prefer wikilinks so the course is navigable in Obsidian.
- Do not turn it into a journal. It is an index and restart manual.
