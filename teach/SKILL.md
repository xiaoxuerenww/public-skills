---
name: teach
description: Teach the user a new skill or concept, either as a quick frontier-interview one-pager or as a stateful course workspace with durable docs, a question bank, and a learn_notes companion buffer.
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

Omit sections that add little signal. Prefer dense, crisp bullets over long prose. Use equations or code only when they improve recall or precision. Use Obsidian-friendly LaTeX display math for formulas, with each important formula in its own `$$` block rather than inline code or plain text. Avoid appendices, long taxonomies, and broad surveys.

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
2. Else, if the current directory contains `0_index.md` plus at least one of `1_solution.md`, `2_deep_dive.md`, `question_bank.md`, or `learn_notes.md`, use the current directory.
3. Else, if a nearby child directory clearly matches the topic and contains `0_index.md`, use that existing child directory.
4. Else, create a new child directory named `<topic_slug>_course` under the current directory, for example `rag_course`, `pytorch_course`, or `system_design_course`.

Use lower-case snake_case for generated directory names. When reporting files back to the user, include the `teaching_dir` prefix in wikilinks, such as `[[rag_course/0_index.md]]` or `[[rag_course/1_solution.md]]`.

### Obsidian link style for course docs

Whenever mentioning course docs in chat or inside generated course docs, prefer Obsidian wikilinks over plain paths or bare code spans:

- Use `[[<teaching_dir>/0_index.md]]`, `[[<teaching_dir>/1_solution.md]]`, `[[<teaching_dir>/2_deep_dive.md]]`, `[[<teaching_dir>/question_bank.md]]`, and `[[<teaching_dir>/learn_notes.md]]` when reporting from outside the course directory or in chat.
- Inside the same course directory, shorter links like `[[0_index]]`, `[[1_solution]]`, `[[2_deep_dive]]`, `[[question_bank]]`, and `[[learn_notes]]` are acceptable if they resolve cleanly.
- Keep filenames in backticks only when referring to literal filenames, code spans, shell commands, or validation rules. If a user should click it, make it a wikilink.
- In task lists, prefer clickable docs, for example `Read [[0_index]] to understand the course mission. (5 min)`.
- When updating existing docs, convert newly touched course-doc mentions to wikilinks, but do not churn the whole file just to relink every old occurrence.

## Durable Documents, Question Bank, And Learning Buffer

Stateful Course Mode uses three durable Markdown files in `teaching_dir` plus one quiz question bank and one companion notes buffer:

1. `0_index.md`: course index, mission, progress tracker, learning records, and restart manual.
2. `1_solution.md`: the current lesson, worked examples, exercises, quiz prompts, answer keys, and raw quiz feedback.
3. `2_deep_dive.md`: polished synthesis plus compact durable study material, including glossary, formulas, snippets, source list, and external resources.
4. `question_bank.md`: quiz-mode question bank. Quiz questions should come from here by default.
5. `learn_notes.md`: companion-mode learning notes. Companion-mode Q&A always goes here, never into `1_solution.md`.

Never create directories named `learning_records/` or `assets/`. Also do not create `lessons/`, `notes.md`, separate resource files, or numbered lesson files. If an older teaching directory already contains legacy files, leave them alone unless the user asks to migrate them. Create and update only the three durable documents plus `question_bank.md` for quiz mode and `learn_notes.md` for companion mode going forward. Put all durable synthesis, source lists, formulas, glossary entries, and resources in `2_deep_dive.md`.

## Stateful Course Update Workflow

Trigger this workflow when the user says `$teach update @<teaching_dir>/`, asks to update an existing course, or points `$teach` at a course folder that already contains course artifacts.

1. Resolve `teaching_dir`.
2. Audit current files:
   - Active durable docs: `0_index.md`, `1_solution.md`, `2_deep_dive.md`. Quiz bank: `question_bank.md`. Companion notes: `learn_notes.md`.
   - Legacy course files such as `index.md`, `solution.md`, `deep_dive.md`, `<topic>_course.md`, `lessons/`, `learning_records/`, or older numbered notes. Treat `learn_notes.md` as active if companion mode is or was used.
3. Create or refresh missing active docs from the best available legacy sources. Do not delete, archive, or rewrite legacy files unless the user explicitly asks.
4. In `0_index.md`, maintain a `## Legacy source files` section when legacy files exist. List legacy files with a one-line reason they are retained, and state whether the recommendation is leave, archive, or delete. Never perform the cleanup without explicit approval.
5. Refresh the doc-reading task plan at the top of `## Course tasks`, using wikilinks for course docs:
   - Read [[0_index]] to understand mission and progress. (5 min)
   - Read [[1_solution]] for the active lesson, drills, and Q&A. (15-25 min)
   - Read [[2_deep_dive]] for polished synthesis, formulas, glossary, sources, and quick review. (15-30 min)
6. Do not mark doc-reading tasks complete unless the user explicitly says they read that doc or existing course state clearly records it. If the user marked an older equivalent doc as read, transfer progress only when the active numbered doc fully supersedes it, and add a learning record explaining the transfer.
7. Run a course integrity audit before reporting completion:
   - Verify the three active durable docs exist and are non-empty, except [[2_deep_dive]] may be absent or brief before consolidation. Verify [[question_bank]] exists for quiz mode. Verify [[learn_notes]] exists if companion mode has been used.
   - Check wikilinks and Markdown links in all active docs. Resolve relative links against `teaching_dir`; report or fix broken links that point to missing local files.
   - Ensure `## Legacy source files` lists only existing legacy files. Remove nonexistent legacy links or mark them as unavailable only if the absence is meaningful.
   - Ensure active docs are the primary study path. Legacy files may appear only under `## Legacy source files` or source/traceability notes.
   - Verify [[0_index]] has: mission, current status, course-doc reading plan, task plan, course file links, learning records, review schedule, and restart instructions.
8. For interview-targeted courses, ensure [[0_index]] also has: one 30-second target answer or a clearly linked target answer in [[1_solution]], a must-answer question list, and a next mock or quiz action.
9. Avoid unsafe global renames. When migrating or renaming files, update only exact known filenames, wikilinks, Markdown links, and code-span file references. Do not blindly replace substrings inside arbitrary text, because it can create invalid names such as topic-specific file names with numbered doc names spliced in.
10. Report active docs, legacy docs, broken-link fixes, index quality results, and any cleanup recommendation using wikilinks.

## `0_index.md`

`0_index.md` is the source of truth for the course. Create it before or alongside the first `1_solution.md` update, then maintain it whenever course state changes.

It must include:

- Course title.
- Mission: why the user is learning the topic, success criteria, constraints, and out-of-scope items.
- How to use this course across sessions.
- Current status: not started, in progress, paused, review, or complete.
- `## Course tasks` with one checkbox task per lesson, drill, review, consolidation milestone, and required course-doc reading step.
- Estimated time for every task, such as `(15 min)`, `(30-45 min)`, or `(2 sessions)`.
- A task plan for reading all active course docs: [[0_index]], [[1_solution]], and [[2_deep_dive]] when it exists or is non-empty. Keep these as checkboxes in `## Course tasks`, not as a separate completed-docs section.
- Links to [[1_solution]] and [[2_deep_dive]].
- `## Learning records` with durable insights, corrected misconceptions, weak spots, strong interview phrasing, and dated progress notes.
- Review schedule or spaced-repetition prompts.
- Session restart instructions, such as: "Read [[0_index]], then continue from the next unchecked task."

Represent completed work only by checked tasks in `## Course tasks`. Do not add separate completed-lessons sections.

When updating an existing course, especially from `$teach update @<teaching_dir>/`, follow the Stateful Course Update Workflow: audit active and legacy docs, refresh the doc-reading task plan, run the course integrity audit, fix or report broken links, run the index quality check, and report cleanup recommendations. Do not mark a doc-reading task complete unless the user explicitly says they read it or prior course state clearly records it. If [[2_deep_dive]] is missing or empty, include a task to create or read it only when consolidation is relevant.

Example task format:

```md
## Course tasks

- [ ] Read [[0_index]] to understand the course mission and progress. (5 min)
- [ ] Read [[1_solution]] for the active lesson and drills. (15-25 min)
- [ ] Read [[2_deep_dive]] for the polished synthesis, formulas, glossary, sources, and quick review. (15-30 min)
- [ ] Build the core mental model for attention. (20 min)
- [ ] Work through one PyTorch shape drill. (15 min)
- [ ] Review failure modes and interview phrasing. (20 min)
- [ ] Consolidate into [[2_deep_dive]]. (30 min)
```

Learning record format:

```md
## Learning records

- {YYYY-MM-DD}: {durable insight, corrected misconception, weak spot, or strong interview phrasing}. Next action: {specific review, drill, or task link}.
```

Course integrity audit conventions:

- Treat extensionless wikilinks as Markdown file references, for example `[[path/name]]` may resolve to `path/name.md`.
- For links to non-Markdown local files, preserve the extension, for example `[[script.py]]`.
- For external links, do not browse unless the user asks to verify freshness; just preserve the source list.
- If a link target is missing, prefer fixing it to an existing active doc. If no clear target exists, remove it from primary paths and mention it in the report.

When a user resumes the course, read [[0_index]], the latest relevant part of [[1_solution]], and [[2_deep_dive]] before deciding what to teach next.

## `1_solution.md`

`1_solution.md` is the active teaching surface. Put lessons, worked examples, exercises, answer keys, quiz prompts, and quiz feedback here. Do not put companion-mode Q&A here; use `learn_notes.md`.

A teaching unit should be short and self-contained. It should give the user one tangible win and fit the mission in `0_index.md`.

For each substantial teaching unit, prefer this structure:

1. Objective.
2. Minimal knowledge needed.
3. Worked example or implementation sketch.
4. Retrieval practice or drill.
5. Answer key or self-check.
6. Interview phrasing when relevant.
7. Pointers to `2_deep_dive.md`.

## `learn_notes.md`

`learn_notes.md` is the companion-mode learning notes file. Create it when companion mode starts if it does not exist. During active companion mode, append notes by default for learning questions and keep them slightly raw. Do not dedup, regroup, or polish it until companion mode ends, the user asks to consolidate, or the course is finished. After notes are consolidated into [[2_deep_dive]], clean up [[learn_notes]] so it does not keep a duplicate raw copy of already-merged material.

Companion-mode Q&A format:

```md
## {YYYY-MM-DD} - {short topic}

### Q: {user question}

**A:** {1-4 sentence answer}

**Mental model:** {what to remember}

**Interview phrasing:** {one sentence the user can say aloud, if relevant}

**Grounding:** {section in 1_solution.md, 2_deep_dive.md, or external source}
```

## `question_bank.md`

`question_bank.md` is the canonical source for quiz-mode questions. Create or update it when a course enters quiz mode and no usable bank exists. Keep it grounded in `0_index.md`, `1_solution.md`, `2_deep_dive.md`, and durable misses from `learn_notes.md`.

Question-bank entries should be compact and reusable:

```md
## {Topic}

- [ ] **Q:** {question}
  **Type:** brief | single-choice | multi-choice
  **Answer:** {expected answer or option key}
  **Why it matters:** {mental model, misconception, or interview skill being tested}
  **Grounding:** {0_index.md, 1_solution.md, 2_deep_dive.md, or learn_notes.md section}
```

Prefer 10-20 high-signal questions over a broad dump. Group by topic. Include questions for weak spots recorded in `0_index.md` and common interview-critical misconceptions. Mark questions checked only after they have been asked in quiz mode.

## `2_deep_dive.md`

`2_deep_dive.md` is the polished synthesis and durable study note. Create or update it when the user explicitly finishes a course, asks to consolidate, asks for a durable study note, or provides material that should be kept.

It should include:

- Durable concepts and mental models.
- Glossary.
- Key equations and invariants, formatted as LaTeX display math with `$$` blocks.
- Algorithms and flowcharts.
- PyTorch/Python snippets.
- Tradeoffs and failure modes.
- Implementation patterns.
- Evaluation and debugging guidance.
- Interview phrasing.
- Curated sources and external resources.
- Community or practitioner resources when real-world wisdom is needed.
- Links back to `1_solution.md`.

Before `2_deep_dive.md` is well-populated, prioritize high-quality resources for knowledge acquisition. For current or external claims, search and cite trusted sources. Avoid citation clutter in `1_solution.md`; put durable source lists in `2_deep_dive.md`.

### Beautified deep-dive style

When creating or substantially updating `2_deep_dive.md`, make it easy to scan in Obsidian:

- Use clear hierarchy: `##` for major sections, `###` for numbered concept groups, and `####` for individual formulas, algorithms, or definitions.
- Use Obsidian callouts for visual color and emphasis: `[!abstract]` for one-liners, `[!info]` for how to read a section, `[!note]` for annotations, `[!tip]` for interview intuition, `[!important]` for key takeaways, `[!warning]` for failure modes, `[!summary]` for symbol lists, and `[!quote]` for phrasing to say aloud.
- Put key annotations under formulas as callouts instead of loose paragraphs.
- Bold high-signal terms in tables and callouts.
- Use horizontal separators only between major conceptual groups, not after every small item.
- Keep formulas in their own `$$` blocks. Do not put important formulas as inline code inside tables.
- Prefer compact tables for comparisons and callouts for mental models, pitfalls, and interview phrasing.
- Avoid visual clutter: beautify the active study path, but keep the deep dive printable and concise.

Do not create or maintain a separate reference file. Put durable formulas, glossary entries, snippets, source links, resources, and synthesis directly in `2_deep_dive.md`.

Do not run finish-course consolidation unless the user explicitly uses a finish or consolidation command.

## Companion Mode

Trigger companion mode when the user says `$teach companion mode`, `$teach companion`, or clearly asks to learn alongside an existing course with ongoing Q&A.

In companion mode:

1. Resolve `teaching_dir`.
2. Read `0_index.md`, `1_solution.md`, `2_deep_dive.md`, and existing `learn_notes.md` if they exist.
3. Stay in companion mode for the current chat until the user explicitly says to exit, stop, finish, end learning companion, or leave companion mode.
4. Do not prompt the user with questions, quizzes, checks for understanding, suggested exercises, or next-step prompts. Take questions from the user and answer them.
5. Answer directly and briefly. When explaining, give the useful explanation first in a few sentences or tight bullets. Do not over-index on file references, section names, or source grounding; mention grounding only when it improves correctness, resolves ambiguity, or the user asks where something came from.
6. Append notes to `learn_notes.md` by default for learning Q&A, explanations, corrected misconceptions, examples, drills, and useful follow-up context. Do not put companion-mode Q&A in `1_solution.md`. Do not record workflow, environment, or file-management questions unless the user explicitly asks to keep them. If the user says not to take notes, skip note capture for that exchange.
7. If the Q&A reveals a durable insight, corrected misconception, weak spot, or strong reusable interview phrasing, add a concise dated entry to `## Learning records` in `0_index.md`.

When companion mode ends, tidy `learn_notes.md` before reporting completion: group raw notes by topic, dedup repeated explanations, reorder related entries into a coherent learning path, and preserve useful examples, corrected misconceptions, mental models, and interview phrasing. Keep the file as learning notes, not a polished deep dive. Do not move material into `2_deep_dive.md` unless the user explicitly asks to consolidate or finish the course. If the user does ask to consolidate, merge durable content into [[2_deep_dive]] and then clean [[learn_notes]] down to unmerged open questions, a short dated merge note, and any intentionally retained raw details.

Companion mode is for user-initiated Q&A and note capture, not for rewriting the whole course and not for quizzing. Keep `learn_notes.md` as the active notes buffer during companion mode, then organize it when companion mode ends.

## Quiz Mode

Trigger quiz mode when the user says `$teach quiz mode`, `$teach quiz`, `quiz me with $teach`, or asks to be quizzed on a specific teaching course.

In quiz mode:

1. Resolve `teaching_dir`.
2. Read `question_bank.md` first if it exists, then read `0_index.md`, `1_solution.md`, and `2_deep_dive.md` if needed for grounding.
3. Stay in quiz mode for the current chat until the user explicitly says to exit, stop, finish, or leave quiz mode.
4. Ask exactly one question per assistant turn.
5. Do not impose a fixed question limit. Continue asking one question per turn until the user exits quiz mode, the question bank is exhausted, or the user asks to switch modes.
6. Ask from `question_bank.md` by default. Prefer unchecked questions, then weak spots recorded in `0_index.md`, then questions not asked recently.
7. If `question_bank.md` is missing, empty, or too shallow, create or expand it before quizzing using grounded course material. Do not invent quiz questions from memory when course docs contain enough material.
8. Do not leak the expected answer, answer key, rubric, hints, or grounding before the user answers. When asking a question, show only the question and any answer options needed to respond.
9. Use brief-answer questions when recall matters. Use single-choice or multi-choice questions when contrast or tradeoff discrimination matters.
10. For single-choice and multi-choice questions, use clickable UI options when available. Prefer `request_user_input` when available for this turn. Otherwise use plain Markdown with labeled options. Do not mark the correct option or phrase distractors in a way that reveals the answer.
11. After the user answers, assess and judge the answer before teaching. Give a clear verdict such as correct, partially correct, or incorrect; then give the correction, mental model, and interview phrasing if useful. Tie the correction back to the question-bank grounding when it matters.
12. Be calibrated and candid. Credit what is right, name exactly what is missing or wrong, and distinguish minor wording issues from conceptual errors.
13. Mark the asked question checked in `question_bank.md` when the user has answered it. If the answer reveals a better variant, add that variant as a new unchecked question.
14. Take notes in quiz mode by default. Append quiz-relevant feedback to `1_solution.md`, including the question, the user's answer summary, verdict, correction, and weakness signal when useful. Do not record every trivial correct answer. If the user says not to take notes, skip note capture for that exchange.
15. Track weaknesses throughout the quiz: missing concepts, shallow reasoning, slow recall, imprecise phrasing, false confidence, and repeated mistake patterns.
16. Add durable misses, corrected misconceptions, strong interview phrasing, and next drills to `## Learning records` in `0_index.md`.
17. When quiz mode ends, append a short raw quiz summary to `1_solution.md` and a concise durable summary to `0_index.md`; update `question_bank.md` with newly discovered weak spots.
18. End with an interview-style verdict: pass, borderline, or not yet pass for the target level. Include the main evidence, top weaknesses, and the next 1-3 drills.

End-of-quiz summary format:

```md
## {YYYY-MM-DD} - Quiz summary: {course or topic}

**Topics tested:** {short list}

**Strengths:** {what the user answered well}

**Weaknesses:** {specific concepts, confusions, or slow spots}

**Interview verdict:** pass | borderline | not yet pass for {target level}. Evidence: {1-3 concrete observations}.

**Corrections to remember:** {durable fixes}

**Recommended drills:** {1-3 focused drills}

**Grounding:** {1_solution.md, 2_deep_dive.md, or source}
```

Durable quiz summary format for `0_index.md`:

```md
## Learning records

- {YYYY-MM-DD}: Quiz summary: verdict: {pass | borderline | not yet pass for target level}; strengths: {short list}; weak spots: {short list}; corrections: {durable fixes}; next drills: {1-3 focused drills}.
```

## Finish Course Consolidation

Trigger finish-course consolidation when the user says `finish $teach <course name>`, `finish $teach <teaching_dir>`, or an equivalent explicit finish or consolidation command.

When finishing a course:

1. Resolve `teaching_dir`.
2. Read [[0_index]], [[1_solution]], [[learn_notes]], and existing [[2_deep_dive]] if present.
3. First consolidate durable material from [[learn_notes]] into [[2_deep_dive]]: dedup repeated Q&A, group topics into durable concepts, tradeoffs, common pitfalls, implementation patterns, evaluation/debugging guidance, and interview phrasing, and preserve useful examples and grounding.
4. After [[2_deep_dive]] is updated, clean up [[learn_notes]]: remove content that was fully merged, delete low-signal duplicate raw entries, and keep only unmerged open questions, unresolved weak spots, intentionally retained raw details, and a short dated note such as `Merged into [[2_deep_dive]] on YYYY-MM-DD`.
5. Do not leave [[learn_notes]] as a second deep dive. It should be a small staging inbox after consolidation, not a duplicate archive of merged content.
6. Merge any durable formulas, glossary entries, snippets, source links, resources, and other study material into [[2_deep_dive]].
7. Update [[0_index]]: mark completed tasks if the user's learning indicates completion, set status to `review` or `complete`, add or tidy `## Learning records`, and add review prompts pointing to [[2_deep_dive]].
8. Report the files updated using wikilinks, including [[learn_notes]] when it changed.

## Teaching Principles

- Assume strong ML fundamentals and Python/PyTorch fluency unless the user says otherwise.
- Emphasize subtleties that distinguish senior candidates: invariants, scaling behavior, failure modes, production constraints, and experimental design.
- For math-heavy concepts, include the smallest derivation that explains the result, format formulas as Obsidian-friendly LaTeX display math using `$$`, then translate the math back to intuition.
- For durable study docs, especially [[2_deep_dive]], use Obsidian-native formatting for readability: callouts for colored emphasis, bold key terms, indented annotations, numbered hierarchy, and compact comparison tables.
- For systems concepts, cover latency, throughput, memory, correctness, reliability, observability, and operational failure modes.
- For ML training/inference concepts, cover data, objective, optimization, evaluation, scaling, debugging, and deployment implications.
- Build storage strength with retrieval practice, spacing, and interleaving where useful.
- Keep lessons short. Working memory is small.
- Prefer "what breaks and why" over broad surveys.
- Name uncertainty explicitly when the field has multiple valid conventions.
- Use PyTorch by default for deep-learning examples.
- Tie every stateful teaching unit back to the mission in `0_index.md`.
