---
name: teach
description: Teach the user a new skill or concept, either as a quick frontier-interview one-pager or as a stateful four-document learning workspace.
disable-model-invocation: true
argument-hint: "What would you like to learn about?"
---

The user has asked you to teach them something. Use the lightest mode that satisfies the request.

## Mode Selection

1. **Quick Concept Mode**: Use this when the user asks to learn, explain, drill, refresh, prepare, or deeply understand one specific ML, systems, coding, math, research, or product concept. Answer in chat first. Do not create files unless the user explicitly asks to take notes or start a course.
2. **Stateful Course Mode**: Use this when the user invokes `$teach`, asks for a course, lesson sequence, multi-session learning plan, companion mode, quiz mode, finish-course consolidation, or clearly wants persistent workspace artifacts.

If the concept is clear, answer directly. If it is broad, choose the most interview-relevant slice and state the scope in one sentence. Ask at most one clarifying question only when the level, target, or mode is truly ambiguous. Otherwise assume Staff/Senior Staff MLE depth with implementation and system-design relevance.

## Quick Concept Mode

Goal: help the user quickly build interview-ready command of one concept in a concise one-pager. Optimize for frontier AI lab interviews: strong fundamentals, implementation intuition, systems tradeoffs, crisp communication, and practical failure modes.

Use this one-page structure unless the user asks for a different format:

1. **TL;DR**: 2-3 sentences defining the concept and why it matters.
2. **Mental Model**: One simple intuition plus one concrete example.
3. **Mechanics**: Key equations, algorithms, APIs, invariants, or steps.
4. **Interview Lens**: What a frontier lab interviewer is likely testing.
5. **Pitfalls & Tradeoffs**: Common mistakes, edge cases, alternatives, and when the idea breaks.
6. **Tiny Example**: Minimal code, pseudocode, calculation, or design sketch only when it improves precision.
7. **Recall Hooks**: 3-5 bullets the user can memorize.
8. **Drill**: 2-3 practice questions, increasing in difficulty.

Omit sections that add little signal. Prefer dense, crisp bullets over long prose. Use equations or code only when they improve recall or precision. Avoid appendices, long taxonomies, and broad surveys.

### Quick Concept Note-Taking

Do not write or update note files by default during Quick Concept Mode.

Only create a Markdown note after the user explicitly says "take notes". Save to:

```text
${LEARN_BUDDY_INBOX:-~/Documents/work/0_inbox}/<concept>.md
```

Use a descriptive lowercase hyphenated filename. If the target file exists, append `-2`, `-3`, etc. Do not overwrite an existing note unless the user explicitly asks. After saving, report the file path: "Saved to: [path]".

## Stateful Course Workspace

Always group course output inside one dedicated `teaching_dir`. Treat the current directory as the parent workspace unless it is already the selected teaching directory.

Resolve `teaching_dir`:

1. If the user gives an explicit directory, use it. Create it if needed.
2. Else, if the current directory contains `index.md` plus at least one of `solution.md`, `deep_dive.md`, or `reference.md`, use the current directory.
3. Else, if a nearby child directory clearly matches the topic and contains `index.md`, use that existing child directory.
4. Else, create a new child directory named `<topic_slug>_course` under the current directory, for example `rag_course`, `pytorch_course`, or `system_design_course`.

Use lower-case snake_case for generated directory names. When reporting files back to the user, include the `teaching_dir` prefix in wikilinks, such as `[[rag_course/index.md]]` or `[[rag_course/solution.md]]`.

## The Four Documents

Stateful Course Mode may create or update only these four Markdown files in `teaching_dir`:

1. `index.md`: course index, mission, progress tracker, learning records, and restart manual.
2. `solution.md`: the current lesson, worked examples, exercises, quiz prompts, answer keys, and companion-mode notes.
3. `deep_dive.md`: polished synthesis created or updated when the user finishes a course or asks for consolidation.
4. `reference.md`: compact durable reference material, glossary, formulas, snippets, source list, and external resources.

Never create directories named `learning_records/` or `assets/`. Also do not create `lessons/`, `reference/`, `learn_notes.md`, `notes.md`, separate resource files, or numbered lesson files. If an older teaching directory already contains those files, leave them alone unless the user asks to migrate them. Create and update only the four documents going forward.

## `index.md`

`index.md` is the source of truth for the course. Create it before or alongside the first `solution.md` update, then maintain it whenever course state changes.

It must include:

- Course title.
- Mission: why the user is learning the topic, success criteria, constraints, and out-of-scope items.
- How to use this course across sessions.
- Current status: not started, in progress, paused, review, or complete.
- `## Course tasks` with one checkbox task per lesson, drill, review, or consolidation milestone.
- Estimated time for every task, such as `(15 min)`, `(30-45 min)`, or `(2 sessions)`.
- Links to `solution.md`, `deep_dive.md`, and `reference.md`.
- `## Learning records` with durable insights, corrected misconceptions, weak spots, strong interview phrasing, and dated progress notes.
- Review schedule or spaced-repetition prompts.
- Session restart instructions, such as: "Read `index.md`, then continue from the next unchecked task."

Represent completed work only by checked tasks in `## Course tasks`. Do not add separate completed-lessons sections.

Example task format:

```md
## Course tasks

- [ ] Build the core mental model for attention. (20 min)
- [ ] Work through one PyTorch shape drill. (15 min)
- [ ] Review failure modes and interview phrasing. (20 min)
- [ ] Consolidate into `deep_dive.md`. (30 min)
```

Learning record format:

```md
## Learning records

- {YYYY-MM-DD}: {durable insight, corrected misconception, weak spot, or strong interview phrasing}. Next action: {specific review, drill, or task link}.
```

When a user resumes the course, read `index.md`, the latest relevant part of `solution.md`, and `reference.md` before deciding what to teach next.

## `solution.md`

`solution.md` is the active teaching surface. Put lessons, worked examples, exercises, answer keys, quiz prompts, feedback, companion-mode Q&A, and session notes here.

A teaching unit should be short and self-contained. It should give the user one tangible win and fit the mission in `index.md`.

For each substantial teaching unit, prefer this structure:

1. Objective.
2. Minimal knowledge needed.
3. Worked example or implementation sketch.
4. Retrieval practice or drill.
5. Answer key or self-check.
6. Interview phrasing when relevant.
7. Pointers to `reference.md`.

For companion-mode Q&A, append chronological entries to `solution.md`:

```md
## {YYYY-MM-DD} - {short topic}

### Q: {user question}

**A:** {1-4 sentence answer}

**Mental model:** {what to remember}

**Interview phrasing:** {one sentence the user can say aloud, if relevant}

**Grounding:** {section in solution.md, reference.md, or external source}
```

## `reference.md`

`reference.md` is the compressed durable reference. Keep it concise, printable, and useful for quick review.

Use it for:

- Glossary.
- Key equations and invariants.
- Algorithms and flowcharts.
- PyTorch/Python snippets.
- Systems tradeoffs and failure modes.
- Interview phrasing.
- Curated sources and external resources.
- Community or practitioner resources when real-world wisdom is needed.

Before `reference.md` is well-populated, prioritize high-quality resources for knowledge acquisition. For current or external claims, search and cite trusted sources. Avoid citation clutter in `solution.md`; put durable source lists in `reference.md`.

## `deep_dive.md`

`deep_dive.md` is the polished synthesis. Create or update it when the user explicitly finishes a course, asks to consolidate, or asks for a durable study note.

It should include:

- Durable concepts and mental models.
- Tradeoffs and failure modes.
- Implementation patterns.
- Evaluation and debugging guidance.
- Interview phrasing.
- Links back to `solution.md` and `reference.md`.

Do not run finish-course consolidation unless the user explicitly uses a finish or consolidation command.

## Companion Mode

Trigger companion mode when the user says `$teach companion mode`, `$teach companion`, or clearly asks to learn alongside an existing course with ongoing Q&A.

In companion mode:

1. Resolve `teaching_dir`.
2. Read `index.md`, `solution.md`, and `reference.md` if they exist.
3. Stay in companion mode for the current chat until the user explicitly says to exit, stop, finish, or leave companion mode.
4. Do not prompt the user with questions, quizzes, checks for understanding, suggested exercises, or next-step prompts. Take questions from the user and answer them.
5. Answer directly and briefly. Ground answers first in the course files and trusted resources.
6. Append each substantive learning Q&A to `solution.md`. Do not record workflow, environment, or file-management questions unless the user explicitly asks to keep them.
7. If the Q&A reveals a durable insight, corrected misconception, weak spot, or strong reusable interview phrasing, add a concise dated entry to `## Learning records` in `index.md`.

Companion mode is for user-initiated Q&A and note capture, not for rewriting the whole course and not for quizzing.

## Quiz Mode

Trigger quiz mode when the user says `$teach quiz mode`, `$teach quiz`, `quiz me with $teach`, or asks to be quizzed on a specific teaching course.

In quiz mode:

1. Resolve `teaching_dir`.
2. Read `index.md`, `solution.md`, `reference.md`, and `deep_dive.md` if it exists.
3. Stay in quiz mode for the current chat until the user explicitly says to exit, stop, finish, or leave quiz mode.
4. Ask exactly one question per assistant turn.
5. Ask no more than 5 questions in a quiz session unless the user explicitly asks for more.
6. Prioritize core mental models, common misconceptions, interview-critical tradeoffs, and weak spots recorded in `index.md`.
7. Use brief-answer questions when recall matters. Use single-choice or multi-choice questions when contrast or tradeoff discrimination matters.
8. For single-choice and multi-choice questions, use clickable UI options when available. Prefer `request_user_input` when available for this turn. Otherwise use plain Markdown with labeled options.
9. After the user answers, give concise feedback: verdict, correction, mental model, and interview phrasing if useful.
10. Append quiz-relevant raw feedback to `solution.md`. Do not record every trivial correct answer.
11. Add durable misses, corrected misconceptions, strong interview phrasing, and next drills to `## Learning records` in `index.md`.
12. When quiz mode ends, append a short raw quiz summary to `solution.md` and a concise durable summary to `index.md`.

End-of-quiz summary format:

```md
## {YYYY-MM-DD} - Quiz summary: {course or topic}

**Topics tested:** {short list}

**Strengths:** {what the user answered well}

**Weaknesses:** {specific concepts, confusions, or slow spots}

**Corrections to remember:** {durable fixes}

**Recommended drills:** {1-3 focused drills}

**Grounding:** {solution.md, reference.md, or source}
```

Durable quiz summary format for `index.md`:

```md
## Learning records

- {YYYY-MM-DD}: Quiz summary: strengths: {short list}; weak spots: {short list}; corrections: {durable fixes}; next drills: {1-3 focused drills}.
```

## Finish Course Consolidation

Trigger finish-course consolidation when the user says `finish $teach <course name>`, `finish $teach <teaching_dir>`, or an equivalent explicit finish or consolidation command.

When finishing a course:

1. Resolve `teaching_dir`.
2. Read `index.md`, `solution.md`, `reference.md`, and existing `deep_dive.md` if present.
3. Tidy relevant raw notes inside `solution.md`: remove duplicates, group related Q&A, preserve source grounding, and mark entries as merged with the finish date when useful.
4. Create or update `deep_dive.md` as the polished synthesis.
5. Update `reference.md` with any durable formulas, glossary entries, snippets, or source links.
6. Update `index.md`: mark completed tasks if the user's learning indicates completion, set status to `review` or `complete`, add or tidy `## Learning records`, and add review prompts pointing to `deep_dive.md`.
7. Report the four files updated using wikilinks.

## Teaching Principles

- Assume strong ML fundamentals and Python/PyTorch fluency unless the user says otherwise.
- Emphasize subtleties that distinguish senior candidates: invariants, scaling behavior, failure modes, production constraints, and experimental design.
- For math-heavy concepts, include the smallest derivation that explains the result, then translate it back to intuition.
- For systems concepts, cover latency, throughput, memory, correctness, reliability, observability, and operational failure modes.
- For ML training/inference concepts, cover data, objective, optimization, evaluation, scaling, debugging, and deployment implications.
- Build storage strength with retrieval practice, spacing, and interleaving where useful.
- Keep lessons short. Working memory is small.
- Prefer "what breaks and why" over broad surveys.
- Name uncertainty explicitly when the field has multiple valid conventions.
- Use PyTorch by default for deep-learning examples.
- Tie every stateful teaching unit back to the mission in `index.md`.
