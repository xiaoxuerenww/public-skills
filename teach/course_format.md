# <topic_slug>_course.md Format

`<topic_slug>_course.md` lives at the root of each teaching directory, for example `rag_course.md` inside `rag_course/`. It is the course index, mission, and cross-session manual. It should let the user resume the course after days or weeks without remembering the previous chat.

## Template

```md
# Course: {Topic}

## How to use this course

- Start here at the beginning of every session.
- Read the mission, current status, course tasks, and review schedule.
- Ask the agent: "continue this course from [[<topic_slug>_course.md]]".
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

- [ ] **Task 1: {lesson title}** ({estimated time}) - [[lessons/0001_{lesson}.md]] - {one-line purpose}
- [ ] **Task 2: {lesson title}** ({estimated time}) - [[lessons/0002_{lesson}.md]] - {one-line purpose}
- [ ] **Task 3: {planned task}** ({estimated time}) - {one-line purpose}

## Review schedule

- {date or cadence}: {retrieval prompt or concept to review}
- {date or cadence}: {retrieval prompt or concept to review}

## Reference index

- [[reference/resources.md]] - Source list and communities.
- [[reference/{reference}.md]] - {what it is for}

## Companion and quiz modes

- Raw Q&A and quiz notes: [[learn_notes.md]]
- Finished synthesis: [[deep_dive.md]]
- To continue open-ended Q&A: ask `$teach companion mode` and then ask questions.
- To practice active recall: ask `$teach quiz mode`.
- To finish the course: ask `finish $teach {course_name}`.

## Learning records

- [[learning_records/0001_{record}.md]] - {why it matters}
```

## Rules

- Keep it short enough to scan in under two minutes.
- Use `## Course tasks` as the source of truth for progress; do not add separate `## Completed lessons` or `## Next session` sections.
- Every course task must be a checkbox and include an estimated time, such as `(15 min)`, `(30-45 min)`, or `(2 sessions)`.
- Mark a task complete only when the user has completed the lesson and retrieval practice, not merely when the file exists.
- Fold the mission into `<topic_slug>_course.md`; do not create a separate mission file.
- Store resources in `reference/resources.md`; do not create a root-level resources file.
- Use lower-case snake_case for generated file names and directory names.
- Prefer wikilinks so the course is navigable in Obsidian.
- Do not turn it into a journal. It is an index and restart manual.
