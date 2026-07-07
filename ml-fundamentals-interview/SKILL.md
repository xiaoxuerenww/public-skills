---
name: ml-fundamentals-interview
description: ML/LLM fundamentals interview prep for Julie. Use for daily tracked quizzes, "quiz me", spaced review, LLM fundamentals drills, Staff/Senior Staff MLE technical-depth practice, Databricks topic prep, collect-question mode, solve mode for mock_question_bank answers, mock-question-bank setup, "learn ml fundamental" learn mode, "practice ml fundamental" practice mode, "mock ml fundamental" interview mode, session wrap-up cleanup with $file-cleaner, or explicit $ml-fundamentals-interview / $daily-ml-concept requests.
---

# ML/LLM Fundamentals Quiz

## Purpose

Run Staff/Senior Staff MLE fundamentals drills with these modes:

- **Daily Quiz**: tracked no-repeat quiz with notes and pass/fail grading.
- **Learn Mode**: show one grounded question, model answer, and follow-up immediately.
- **Practice Mode**: run guided topic practice with answer attempts, keyword-level
  feedback, and companion notes when a topic directory is active.
- **Mock Mode**: append a dated section to `mock.md`, ask one grounded
  interview question at a time, and proactively save session notes.
- **Topic Prep**: create or refresh Databricks ML fundamentals topic artifacts
  from a grounded question bank.
- **Collect Question Mode**: scan provided question-bank documents for a given
  interview topic, group question/follow-up relationships, highlight
  company-specific scraped questions when provided, and write the consolidated
  bank to `<interview_topic>/mock_question_bank.md`.
- **Solve Mode**: scan `<interview_topic>/mock_question_bank.md` and create
  concise interview-ready answers for every parent question and follow-up in
  `<interview_topic>/solution.md`.

Optimize for frontier AI lab interview depth: concise prompts, rigorous follow-ups,
derivations when relevant, and critical feedback after the user answers.

Keep the active quiz focused on ML/LLM fundamentals. Do not add or ask
distributed-training systems questions such as DDP, tensor/pipeline/sequence
parallelism, ZeRO, PagedAttention internals, or infrastructure sharding unless
Julie explicitly asks for systems/distributed-training drills.

## Source Files

Daily Quiz uses the tracked question bank:

```text
/Users/xue/Documents/work/0_databricks/0_db_ml_fundamental/2_ml-llm-fundamentals-QUIZ.md
```

Progress is tracked in:

```text
/Users/xue/Documents/work/0_databricks/0_db_ml_fundamental/ml_llm_daily_quiz_progress.json
/Users/xue/Documents/work/0_databricks/0_db_ml_fundamental/ml_llm_daily_quiz_notes.md
```

Mock Mode sessions are saved in the active vault problem or topic directory:

```text
<problem_or_topic_dir>/mock.md
```

Append each mock session as a dated section in that `mock.md`.

Topic Prep uses the default Databricks source bank:

```text
/Users/xue/Documents/work/0_databricks/0_db_ml_fundamental/0_db_ml_fundamentals_question_bank.md
```

Learn Mode and Mock Mode use these Databricks-focused docs:

```text
/Users/xue/Documents/work/0_databricks/0_db_ml_fundamental/2_ml-llm-fundamentals.md
/Users/xue/Documents/work/0_databricks/0_db_ml_fundamental/2_ml-llm-fundamentals-QUIZ.md
/Users/xue/Documents/work/0_databricks/0_db_ml_fundamental/2_ml-llm-fundamentals-ANSWERS.md
```

For any mode, ground answers in the source files above plus directly relevant
files in `/Users/xue/Documents/work/0_databricks/0_db_ml_fundamental/`. Do not
fabricate questions or answers from general knowledge when a source doc is
available.

In `ml_llm_daily_quiz_notes.md`, use the question text as the Markdown heading
for each note entry.

## Mode Routing

- If Julie says "learn ml fundamental", use Learn Mode.
- If Julie says "practice ml fundamental", use Practice Mode.
- If Julie says "mock ml fundamental", use Mock Mode.
- If Julie asks to set up, prepare, initialize, refresh, or update an ML
  fundamentals topic directory, use Topic Prep.
- If Julie asks to collect, extract, consolidate, gather, or build questions
  from provided question-bank documents for a topic, use Collect Question Mode.
- If Julie asks to solve, answer, create solutions for, generate answer keys
  for, or update `solution.md` from a topic `mock_question_bank.md`, use Solve
  Mode.
- If Julie says "quiz me", "daily", "today's", asks for spaced review, or gives
  no explicit learn/mock wording, use Daily Quiz.
- If Julie names a topic in any mode, select a question from that topic.

This skill is Q&A only: no coding exercises, no whiteboard systems prompts, and
no system design unless Julie explicitly changes scope.

## Session Wrap-Up Cleanup

When Julie wraps up or ends a **Practice Mode**, **Learn Mode**, or **Mock Mode**
session, use `$file-cleaner` before the final completion message if the active
topic directory contains both `learn_notes.md` and `deep_dive.md`.

Wrap-up signals include: "wrap up", "done for now", "end session", "finish",
"stop here", "summarize session", or an explicit request to clean notes.

Use this workflow:

1. Finish required mode-specific persistence first.
   - Practice Mode: save the latest practice feedback or weakness notes.
   - Learn Mode: append any useful Q&A explanation to `learn_notes.md` when a
     topic directory is active.
   - Mock Mode: update `mock.md` and `mock_tracker.md` before cleanup.
2. Resolve the active `topic_dir` using the same path rules as Topic Prep and
   Mock Mode.
3. If both `<topic_dir>/learn_notes.md` and `<topic_dir>/deep_dive.md` exist,
   invoke `$file-cleaner` to consolidate `learn_notes.md` into `deep_dive.md`,
   regroup from basic to advanced, remove duplicates, and leave `learn_notes.md`
   as a lightweight companion buffer.
4. If either file is missing, skip cleanup and mention the missing file briefly.
5. Report the mode wrap-up artifacts and the file-cleaner result together.

Do not run `$file-cleaner` after Daily Quiz unless Julie explicitly asks. Daily
Quiz notes stay in `ml_llm_daily_quiz_notes.md` for spaced review tracking.

## Note-Taking Preferences

Persist quiz notes automatically in `ml_llm_daily_quiz_notes.md`.

When saving any Daily Quiz, Practice Mode, or Mock Mode answer, preserve the raw
conversation evidence:

- Save Julie's answer as a raw quoted transcript block whenever possible, not
  only as a paraphrase.
- Save the grading verdict explicitly as `Verdict: pass` or `Verdict: fail`.
- Add a `Misses` section that highlights exactly what Julie missed, got wrong,
  left vague, or failed to defend under follow-up.
- Keep misses direct and concrete: missing equation, wrong assumption, weak
  mechanism, missing failure mode, missing tradeoff, or interview-structure gap.
- Use a concise paraphrase only when the raw answer is unavailable or too long;
  if paraphrasing, label it as `Paraphrased answer`.

Use this format for each recorded question:

```markdown
## <question text>

- Recorded: <timestamp>
- Status: `<pass|fail>`
- Verdict: `<pass|fail>`
- Question ID: `<id>`
- Times seen: <ask_count including the current attempt>
- Section: <section path>
- Topic: <topic>
- Raw answer:
  > <Julie's answer verbatim when available>
- Misses:
  - <specific missing/wrong/vague point>
- Feedback: <direct critique>
- Ideal answer: <interview-ready answer>
- Drill next: <specific next target>
```

For session summaries, also use the question text as each `##` heading and
include:

- `Raw answer`: the user's actual answer as a quoted transcript block when
  available.
- `Verdict`: `pass` or `fail`.
- `Misses`: explicit bullets for what was missing, wrong, or too vague.
- `Critical feedback`: the main gap first, direct and specific.
- `Stronger answer`: an interview-ready version.
- `Drill next`: the next focused practice target.

Do not use timestamp, section, or topic as the heading. Do not hide weak areas
behind vague encouragement. Keep notes concise but explicit enough to support
spaced review.

## Daily Quiz Flow

1. Pick the next shuffled no-repeat question with:

   ```bash
   python3 /Users/xue/.codex/skills/ml-fundamentals-interview/scripts/pick_question.py
   ```

   This records the selected parent question and attached follow-ups as asked.
   Use the `Question ID` and `Times seen` values from the output for answer
   tracking and notes.
2. Ask only the selected top-level parent question first. Do not show `Question ID`,
   `Times seen`, `Section`, `Topic`, or "A strong answer should" criteria in
   the live quiz prompt. Keep those details internal for tracking and later
   feedback.
3. Wait for the user's answer. Do not grade yet. Ask the attached follow-up
   questions one at a time, in order, without revealing IDs or rubric metadata.
   If Julie answers "I don't know" or equivalent, switch to Learn Mode Handling
   immediately instead of asking the next follow-up or grading.
4. After Julie has answered the parent and all follow-ups, critically assess
   every answer. Give `pass` or `fail` for each question, including follow-ups.
   Do not provide pass/fail feedback before the follow-up set is complete.
   - `pass`: technically correct enough to survive Staff/Senior Staff follow-ups;
     definitions are precise, mechanisms are causal, math is correct when
     relevant, assumptions are named, and key failure modes or tradeoffs are covered.
   - `fail`: incorrect, shallow, missing the central mechanism/math/tradeoff, or
     not structured enough for a Staff+ interview.
5. Record each question result after grading the complete set. Put the ideal
   answer, raw answer, verdict, misses, and direct feedback in saved notes for
   the parent and each follow-up:

   ```bash
   python3 /Users/xue/.codex/skills/ml-fundamentals-interview/scripts/pick_question.py \
     --record-result QUESTION_ID \
     --status pass \
     --notes "Raw answer: ... Verdict: pass|fail. Misses: ... Feedback: ... Ideal answer: ... Drill next: ..."
   ```

6. Give the model answer after recording all results, with:
   - crisp definition or thesis,
   - key math or mechanism,
   - practical failure modes and tradeoffs,
   - Staff-level interview framing,
   - concise per-question feedback.

## Learn Mode

Triggered by "learn ml fundamental".

Before answering, read:

```text
/Users/xue/Documents/work/0_databricks/0_db_ml_fundamental/2_ml-llm-fundamentals.md
/Users/xue/Documents/work/0_databricks/0_db_ml_fundamental/2_ml-llm-fundamentals-ANSWERS.md
```

Show one question with its model answer and one staff-level follow-up
immediately. Do not record quiz progress or notes in this conversational mode.

Use this strict format:

```markdown
**Q:** <interview question from the source docs>

**A:** <concise model answer grounded in the docs: key equations, mechanisms, failure modes, essential bullets>

**Follow-up Q:** <harder or adjacent question, preferably from Staff-Level Follow-ups>

**Follow-up A:** <concise grounded answer>

---
Next? (or pick a topic: linear regression / word2vec / transformers)
```

Rules:

- One question per turn. Never dump multiple at once.
- Rotate topics unless Julie picks one.
- If Julie answers before reading, grade against the docs, name gaps, then show
  the model answer.
- On wrap-up, follow **Session Wrap-Up Cleanup** and run `$file-cleaner` when
  the active topic directory has both `learn_notes.md` and `deep_dive.md`.

## Practice Mode

Triggered by "practice ml fundamental".

Use Practice Mode when Julie wants lower-pressure drilling than Mock Mode but
more active recall than Learn Mode.

1. Resolve the active topic directory using the Topic Prep path rules.
2. Prefer `mock_question_bank.md` for candidate-facing questions and
   `solution.md` or `deep_dive.md` for feedback grounding.
3. Ask one practice question or ask Julie for a keyword outline, depending on
   her request.
4. Give keyword-level feedback first, then a concise stronger answer.
5. Save durable takeaways to `learn_notes.md` when the explanation is useful
   beyond the current turn. When saving practice feedback, preserve the raw
   answer or keyword outline, record `Verdict: pass|fail`, and add `Misses`
   bullets before the stronger answer.
6. On wrap-up, follow **Session Wrap-Up Cleanup** and run `$file-cleaner` when
   the active topic directory has both `learn_notes.md` and `deep_dive.md`.

Do not turn Practice Mode into a full mock transcript unless Julie asks.

## Topic Prep

Triggered when Julie asks to set up, prepare, initialize, refresh, or update an
ML fundamentals interview-prep topic directory.

Use this workflow for persistent Databricks topic workspaces under:

```text
/Users/xue/Documents/work/0_databricks/0_db_ml_fundamental/
```

Resolve `topic_dir` first:

1. If Julie provides a topic directory, use it.
2. If she provides a file, walk upward to the nearest directory containing
   `mock_question_bank.md`, `mock.md`, `index.md`, `solution.md`, or
   `deep_dive.md`.
3. If no topic is explicit, use the current directory only if it is already a
   topic directory.
4. If multiple nearby topic directories match, ask one concise clarification
   question.

Use the default source bank unless Julie provides another local bank:

```text
/Users/xue/Documents/work/0_databricks/0_db_ml_fundamental/0_db_ml_fundamentals_question_bank.md
```

Topic selection order:

1. Use Julie's explicit topic when provided.
2. Otherwise infer from `topic_dir` by removing leading numeric prefixes and
   separators, for example `1_linear_regression`, `2_word2vec`, or
   `3_transformer`.
3. Read the matching source-bank section completely and skim surrounding
   headings enough to confirm the boundary.
4. If the topic maps to multiple plausible sections, ask one concise
   clarification question instead of mixing sections silently.

Create or update only these topic artifacts:

- `mock_question_bank.md`: candidate-facing questions as Markdown checkbox
  items with tests, expected answer/evaluation notes, grounding, and blank
  `Asked:`.
- `solution.md`: interviewer answer key with one `### Q:` entry for every
  parent question and follow-up in `mock_question_bank.md`; use the Solve Mode
  answer format when generating or refreshing it, and preserve existing
  answer-key content when not explicitly solving.
- `mock.md`: candidate-facing setup, dated transcript placeholders, feedback,
  verdict, weaknesses, next review, and next-round probes; do not leak answer
  keys.
- `index.md`, `deep_dive.md`, and `learn_notes.md` when Julie asks to refresh
  teach/course artifacts for the topic.

For teach/course refreshes, preserve `mock_question_bank.md` and `mock.md`.
If `solution.md` already contains mock answer keys, append teaching material
below a divider such as `# Active Teach Prep` rather than replacing it.

Before reporting completion:

1. Verify active docs exist and are non-empty.
2. Verify `solution.md` has one `### Q:` answer-key entry per question in
   `mock_question_bank.md`.
3. Verify `mock.md` does not contain hidden answer keys.
4. Report updated docs, question and answer-key counts, and any source gaps.

## Collect Question Mode

Triggered when Julie asks to collect, extract, consolidate, gather, or build
mock questions from provided question-bank documents for an interview topic.

Required inputs:

1. `interview_topic`, for example `transformer`, `word2vec`, or `linear regression`.
2. One or more local question-bank documents.

Optional input:

- `company`, for example `Databricks`, `Anthropic`, or `OpenAI`.

If any required input is missing and cannot be inferred from the current note,
selected file, `@file` references, or nearby topic directory, ask one concise
clarification question. Do not silently fall back to the central Daily Quiz bank
unless Julie explicitly includes it as a source document.

Use this workflow:

1. Resolve the output topic directory:
   - Prefer an existing directory whose name matches the topic after removing
     leading numeric prefixes and separators, such as `3_transformer` for
     `transformer`.
   - If no matching directory exists, create `<interview_topic>/` under the
     current vault root, using a filesystem-safe lowercase slug.
   - Output only to `<topic_dir>/mock_question_bank.md`.
2. Read every provided question-bank document completely enough to capture all
   questions related to the topic.
   - Treat Markdown headings, bullet lists, numbered lists, checkbox items,
     `Q:` labels, and bilingual/raw scraped lines as possible questions.
   - Preserve original question wording when possible.
   - Do not invent questions that are not grounded in the provided documents.
3. Extract only questions related to the interview topic.
   - Include close variants and implementation-level follow-ups.
   - Exclude unrelated system design, coding, or product questions unless they
     explicitly test the requested fundamentals topic.
4. Reorganize question/follow-up relationships:
   - If a source already has a parent question with indented or nearby
     follow-ups, keep that relationship.
   - If multiple documents contain the same parent concept with variants,
     merge them into one parent question and list variants as follow-ups.
   - If a question is clearly a narrower probe of another question, nest it as
     a follow-up instead of creating a duplicate parent.
   - Keep source grounding for both parent questions and follow-ups.
5. If `company` is provided, identify questions mentioned in that company's
   interview-question scraped notes among the provided documents.
   - Create a dedicated top section named
     `## <Company> scraped-interview questions`.
   - Put company-scraped questions there first, with follow-ups nested under
     each parent when applicable.
   - Then create a separate section named
     `## Other grounded questions from provided banks`.
   - Do not label a question as company-scraped unless the source document or
     surrounding heading clearly indicates that company.
6. If `company` is not provided, create one main section named
   `## Grounded questions from provided banks`.
7. Use Markdown checkbox format suitable for mock tracking:

   ```markdown
   # <Interview Topic> Mock Question Bank

   Grounding sources:
   - [[source file 1]]
   - [[source file 2]]

   ## <Company> scraped-interview questions

   - [ ] **Q:** <parent question>
     - Source: <file / heading or source id>
     - Follow-ups:
       - [ ] <follow-up question>
       - [ ] <follow-up question>

   ## Other grounded questions from provided banks

   - [ ] **Q:** <parent question>
     - Source: <file / heading>
     - Follow-ups:
       - [ ] <follow-up question>
   ```

8. Preserve existing useful checked-state if updating an existing
   `mock_question_bank.md`:
   - Keep `[x]` for exact or clearly equivalent questions that were already
     marked asked.
   - Keep existing `Asked:` metadata if present.
   - Remove only duplicates introduced by consolidation.

Before reporting completion:

1. Verify `<topic_dir>/mock_question_bank.md` exists and is non-empty.
2. Verify every listed parent question has at least one source reference.
3. If `company` was provided, report how many parent questions were placed in
   the company scraped section versus the other grounded section.
4. Report any provided documents that had no topic-relevant questions.

## Solve Mode

Triggered when Julie asks to solve, answer, create solutions for, generate
answer keys for, or update `solution.md` from a topic `mock_question_bank.md`.

Use this workflow:

1. Resolve `topic_dir`:
   - Prefer an explicit topic directory or file path from Julie.
   - If Julie gives an interview topic, prefer an existing matching directory
     after removing leading numeric prefixes and separators, such as
     `3_transformer` for `transformer`.
   - If no topic is explicit, use the current directory only if it contains
     `mock_question_bank.md`.
   - If multiple directories match, ask one concise clarification question.
2. Read `<topic_dir>/mock_question_bank.md` completely.
3. Extract every parent question and every nested follow-up question.
   - Preserve the original wording of questions.
   - Preserve existing checked state only in `mock_question_bank.md`; do not
     copy checkbox syntax into `solution.md`.
   - If the bank has question/follow-up hierarchy, keep that hierarchy visible
     in `solution.md` by placing follow-up answers directly after the parent
     answer.
4. Create or refresh `<topic_dir>/solution.md` with interview-ready answers for
   every extracted question.
   - Answers should be concise but complete enough for a Staff/Senior Staff MLE
     interview.
   - Prefer mechanism, equations, assumptions, tradeoffs, and failure modes over
     generic definitions.
   - Do not include a `Grounding` field in `solution.md`.
   - Do not include long source excerpts.
5. Put hints after the answer, not before it. Use this exact compact format:

   ```markdown
   # <Interview Topic> Mock Interview Answers

   ## How to use this file

   Use this as the interviewer answer key for [[mock_question_bank]].

   ### Q: <parent question>

   **Answer:** <interview-ready answer>

   **Hints / grading:**
   - **What the interviewer is testing:** <one concise line>
   - **Staff+ signal:** <one concise line>
   - **Weak answer pattern:** <one concise line>
   - **Evaluation notes:** <one concise line or short bullet list>

   #### Follow-up: <follow-up question>

   **Answer:** <interview-ready answer>

   **Hints / grading:**
   - **What the interviewer is testing:** <one concise line>
   - **Staff+ signal:** <one concise line>
   - **Weak answer pattern:** <one concise line>
   - **Evaluation notes:** <one concise line or short bullet list>
   ```

6. Keep hints concise. Do not add extra rubric sections such as
   `Interviewer intent`, `Target answer`, `Grounding`, or `Source`.
7. If updating an existing `solution.md`, preserve any clearly useful existing
   answers when they match current questions, but rewrite old verbose hint
   fields into the compact `Hints / grading` format above.

Before reporting completion:

1. Verify `<topic_dir>/solution.md` exists and is non-empty.
2. Verify it has one `### Q:` entry for every parent question in
   `mock_question_bank.md`.
3. Verify every follow-up in `mock_question_bank.md` appears as a
   `#### Follow-up:` entry in `solution.md`.
4. Verify `solution.md` contains no `Grounding:` field.
5. Report the parent-question count and follow-up count solved.

## Mock Mode

Triggered by "mock ml fundamental".

Before asking, decide whether Julie is using a topic directory with
`mock_question_bank.md` or the central Daily Quiz source docs.

- If a topic directory exists, read `mock_question_bank.md` for question
  selection, and read `solution.md` only after Julie answers for feedback and
  model answers. Use `deep_dive.md` only as supplemental grounding.
- If no topic directory exists, read the same Databricks source docs as Learn
  Mode and use the central docs for question selection and feedback.

Resolve the active mock file before asking:

1. If the current working context is inside a problem or topic directory, use
   that directory's `mock.md`.
2. If Julie provides a problem, topic, directory, or file path, walk upward to
   the nearest directory containing `mock_question_bank.md`, `mock.md`,
   `index.md`, `solution.md`, or `deep_dive.md`, then use that directory's
   `mock.md`.
3. If no problem or topic directory can be resolved, use
   `/Users/xue/Documents/work/0_databricks/0_db_ml_fundamental/mock.md`.

Append a dated section for each mock session to the resolved `mock.md`.
Maintain a sibling scheduler file named `mock_tracker.md` in the same directory
as the resolved `mock.md`.
Do not record Daily Quiz progress in Mock Mode, but do proactively save mock
notes after each answer and before moving to another question.

Do not create dated mock directories.

Default each mock session to 5-10 total parent questions unless Julie requests a
different count. Start with 5 questions when no duration or intensity is
specified; extend toward 10 only if Julie asks for a longer mock, is moving
quickly, or the session needs broader topic coverage.

Before selecting questions, read `mock_tracker.md` first, then read the resolved
`mock.md` if the tracker is missing, incomplete, or needs backfill. Build a
lightweight scheduling state from prior mock sessions:

- Past questions asked, including exact question text, source/topic, timestamp,
  and pass/fail status.
- Recent weaknesses from `Critical feedback`, `Drill next`, and
  `## Running weakness tracker`.
- Topics or mechanisms that have not been asked recently.
- Next due topics, retry candidates, and round-robin position.

Use this `mock_tracker.md` structure:

```markdown
# Mock Tracker

## Scheduler State

- Last updated: <timestamp>
- Active source docs: <files>
- Round-robin order: <topic/section/mechanism list>
- Next round-robin cursor: <topic/section/mechanism>
- Default session target: 5 parent questions

## Question History

| Question | Source | Topic | Last asked | Times asked | Last status | Selection reason | Next due |
|---|---|---|---:|---:|---|---|---:|
| <question text> | <file/section> | <topic> | <timestamp> | <count> | `<pass|fail|skip>` | <reason> | <date/session> |

## Weakness Queue

| Weakness | Evidence | Last seen | Priority | Next drill |
|---|---|---:|---|---|
| <mechanism/topic> | <miss or feedback summary> | <timestamp> | `<high|medium|low>` | <specific drill> |

## Next Session Plan

- Target count: <5-10>
- Planned mix: <round-robin count> round-robin, <weakness count> weakness
- Planned questions:
  1. <question or topic> - <selection reason>
```

If `mock_tracker.md` does not exist, create it before the first mock question by
backfilling whatever can be inferred from `mock.md` and the available question
bank. Keep the tracker concise; it is a scheduler, not a full transcript.

Use that history to shuffle the session queue:

1. **Round robin coverage**: rotate across source sections, topics, or
   mechanisms so the session does not over-focus on one area unless Julie
   explicitly requested that topic.
2. **Recent weakness bias**: prioritize questions that test recent failed,
   skipped, shallow, or repeatedly weak mechanisms.
3. **Repeat control**: avoid repeating the exact same parent question from the
   most recent mock session unless it directly targets a recorded weakness or
   Julie asks to retry it.
4. **Tie-breaker**: when several questions have similar priority, pick the one
   asked least recently; if still tied, choose randomly.

For each session, aim for a practical mix: roughly half round-robin coverage and
half recent-weakness review. If there are fewer than 5 suitable unseen or
weakness-linked questions, allow repeats but state the retry reason in `mock.md`.
After each parent or follow-up answer, update both `mock.md` and
`mock_tracker.md` before continuing. At session end, refresh `## Next Session
Plan` with the next 5-10 question targets based on the latest round-robin cursor
and weakness queue.

Use this `mock.md` structure:

```markdown
# ML/LLM Fundamentals Mock - <YYYY-MM-DD HH:MM>

## Session focus

- Source docs: <files read>
- Topic constraint: <topic, if any>
- Question selection: round robin across <topics/sections> plus recent weakness
  review from <recent mock dates or "none">

## Questions

### <question text>

- Asked: <timestamp>
- Source: <source file or section>
- Selection reason: <round robin coverage | recent weakness review | retry>
- Raw answer:
  > <Julie's answer verbatim when available>
- Verdict: `<pass|fail>`
- Misses:
  - <specific missing/wrong/vague point>
- Critical feedback: <main gap first>
- Model answer: <interview-ready version grounded in docs>
- Drill next: <specific next target>

#### Follow-up: <follow-up question text>

- Raw answer:
  > <Julie's answer verbatim when available>
- Verdict: `<pass|fail>`
- Misses:
  - <specific missing/wrong/vague point>
- Critical feedback: <main gap first>
- Model answer: <grounded answer>
- Drill next: <specific next target>

## Running weakness tracker

- <topic or mechanism>: <repeated gap and next drill>
```

Ask the question and wait for Julie's answer before revealing anything.

Initial turn format:

```markdown
**Q:** <interview question from the source docs>
```

After Julie answers:

```markdown
**Verdict:** <pass|fail>

**Misses:**
- <specific missing/wrong/vague point>

**Feedback:** <what is correct, missing, or imprecise; grade strictly against the docs>

**Model Answer:** <concise answer from the docs>

**Follow-up Q:** <staff-level follow-up; wait for Julie's answer>
```

Then immediately append the parent question, raw answer transcript, verdict,
misses, feedback, model answer, selection reason, and drill target to `mock.md`,
and update `mock_tracker.md` with question history, weakness priority, and next
due state.

After Julie answers the follow-up:

```markdown
**Verdict:** <pass|fail>

**Misses:**
- <specific missing/wrong/vague point>

**Feedback:** <same grading approach>

**Model Answer:** <follow-up answer>

---
**Q:** <next interview question from the source docs>
```

Then append the follow-up raw answer transcript, verdict, misses, feedback,
model answer, and drill target to `mock.md`, update `mock_tracker.md`, and
update `## Running weakness tracker` if the answer reveals a repeated or
high-priority gap. If the session has not reached its target question count,
immediately ask the next parent question without waiting for Julie to request
it. At the target count, stop and provide a concise session summary with
pass/fail pattern, top misses, weaknesses, and next drills.

### Mock Session End Summary

At the target question count, stop and provide a concise session summary, then
append to `mock.md`:

1. **Raw conversation transcript** section: preserve Julie's verbatim answers as
   blockquoted text under each question heading. This section goes before the
   structured grading section so the raw evidence is always visible.
2. **Session verdict** with pass/fail counts across parent + follow-up questions.
3. **Error summary** grouped by severity:
   - `HIGH`: fails with wrong mechanisms or missing core concepts.
   - `MEDIUM`: passes that contained factual errors (e.g. wrong shape, wrong
     formula) even if the overall answer was acceptable.
   - `LOW`: imprecise language or missing polish that would draw follow-ups.
   Each error entry should explain what Julie said, what is wrong, what the
   correct answer is, and the root cause of the confusion.
4. **Strengths**: specific, technically meaningful things Julie did well.
5. **Next review**: specific `deep_dive.md` sections to drill before the next
   mock.
6. **Next-round probes**: 5 targeted questions for the next session mixing
   weakness retries and uncovered topics.

### Post-Mock Artifact Updates

When Julie asks to update artifacts after a mock (e.g. "update deep dive",
"update solution", "update needs_more_work", "enhance deep dive based on mock"),
use the mock session's error summary and weakness tracker as input:

- **`solution.md`**: add follow-up Q&As that emerged during the mock as
  `#### Follow-up:` entries under their parent questions. If an existing answer
  is weaker than the mock's model answer, replace or improve it. Do not add
  duplicates.
- **`deep_dive.md`**: add new subsections addressing each mock weakness. Include
  tables, callout boxes, and common-wrong-answer entries. Update the
  `## Needs-More-Work Coverage Map` with new entries.
- **`needs_more_work.md`**: add unchecked `[ ]` items for each mock fail or
  significant error-in-pass, with `[source:: <date> mock fail]` metadata. Keep
  the description concrete enough for self-review.
- **`learn_notes.md`**: append a dated session takeaways section with the key
  corrected mental models from the mock.

Rules:

- Never show the answer before Julie responds.
- Grade against the docs; flag missing equations, wrong mechanisms, and
  incomplete tradeoffs.
- One question plus one follow-up per round.
- Do not ask "next question?" between rounds. Continue automatically from parent
  question to follow-up, then from completed follow-up to the next parent
  question until the target question count is reached or Julie pauses/stops.
- Ask from `mock_question_bank.md` by default when a topic directory is active.
  Prefer unchecked questions and mark asked questions only after the mock round
  completes.
- Preserve Julie's actual answer as faithfully as possible in `mock.md`; use a
  raw quoted transcript block by default. Use a concise paraphrase only when the
  answer is long, fragmented, or unavailable, and label it as paraphrased.
- Always show and save an explicit verdict and `Misses` bullets before the model
  answer. Do not bury misses inside general feedback.
- If Julie asks to move on before answering, record the skipped question in
  `mock.md` with `Verdict: fail`, `Misses` bullets naming the missing mechanism,
  and the next drill target.
- If Julie asks for a topic shift during a mock, keep using the same active
  `mock.md` and add the new topic under `## Session focus`.
- On wrap-up, update `mock.md` and `mock_tracker.md` first, then follow
  **Session Wrap-Up Cleanup** and run `$file-cleaner` when the active topic
  directory has both `learn_notes.md` and `deep_dive.md`.

## Learn Mode Handling

If Julie answers "I don't know", "not sure", "no idea", or an equivalent
unknown/blank answer during an active Daily Quiz:

1. Do not grade the question yet and do not continue to the next follow-up.
2. Enter `learn-buddy` mode for the current question's core concept.
3. Produce a concise interview-ready one-pager following `learn-buddy` rules,
   including the required saved Markdown note in `/Users/xue/Documents/work/0_inbox/`.
4. After teaching, re-ask the same quiz question or ask Julie to retry it. Keep
   the original question IDs and `Times seen` metadata for later grading.
5. Only record `pass`/`fail` after Julie retries or explicitly chooses to skip
   or move on.

## Move-On Handling

If Julie asks for the next question, another question, to move on, to skip
ahead, or changes topic while there is a current quiz question with an
unrecorded answer, first record notes for the current question before picking
the next one.

- If she gave answers for the current parent/follow-up set, grade the completed
  portion with `pass`/`fail`, record each result with `--record-result`, and
  then move to the requested next question.
- If she explicitly says she does not know, wants to skip, or gives no usable
  answer while asking to move on, record `fail` with notes that name the missing
  mechanism and the next drill target, then move to the requested next question.
  If she only says "I don't know" without asking to move on, use Learn Mode
  Handling instead of recording a failure.
- Do not silently abandon a current question. Every asked question should have
  either a graded result or an explicit skipped/unknown `fail` result
  before another question is selected.

## Modes

- If the user asks for "daily", "today's", or gives no topic, use the next
  question from the shuffled no-repeat queue.
- If the user asks for a specific topic, pass it as `--topic`, for example:

  ```bash
  python3 /Users/xue/.codex/skills/ml-fundamentals-interview/scripts/pick_question.py --topic attention
  ```

- If the user asks for a random question, pass `--random`.
- If the user asks for multiple questions, pass `--count N` and quiz one at a
  time unless they explicitly ask for a list.
- If testing the script without changing progress, pass `--peek`.
- If the question bank is missing or cannot be parsed, state the issue and ask
  for the correct file path.

## Tracking Rules

- Always record asked questions unless the user explicitly asks to preview or
  test without changing progress.
- Always record the graded answer status after the user answers the full
  parent/follow-up set.
- Before selecting a new question, check whether the current question has an
  unrecorded answer or skip. If yes, record it first according to Move-On
  Handling.
- Follow the Note-Taking Preferences exactly for `ml_llm_daily_quiz_notes.md`.
- Keep result notes useful for review: exact `pass`/`fail` verdict, raw answer
  transcript when available, highlighted misses, ideal answer, how many times
  the question has been seen, and the next concept to revisit.
- Use `fail` for answers that miss the central mechanism, math, or tradeoff.
- Do not mark an answer `pass` unless it would survive Staff/Senior Staff
  follow-ups.
- The picker reshuffles after every full pass through the available question
  scope, so repeats happen only after the scope is exhausted.

## Updating The Question Bank

When adding new questions to `2_ml-llm-fundamentals-QUIZ.md`:

1. First search the existing bank for a semantically matching parent question.
2. If a parent exists, add the new question as an indented follow-up under that
   parent, using the next available unique `QNNN` ID.
3. If no parent exists, add the new question as a new top-level parent in the
   most relevant existing section, using the next available unique `QNNN` ID.
4. Do not create a new section unless Julie explicitly asks for it.
5. After editing, verify all question IDs are unique and the picker can parse
   the bank.

## Assessment Standard

When grading, explicitly check:

- Correctness: identify any incorrect claims, missing conditions, or misleading
  analogies.
- Depth: look for mechanism, derivation, assumptions, edge cases, and failure
  modes rather than surface-level definitions.
- Interview readiness: judge whether the answer is structured enough to guide a
  technical conversation with a frontier-lab interviewer.
- Calibration: separate "I know the intuition" from "I can defend the math and
  tradeoffs under follow-up pressure."

Feedback should be direct and useful. Name the biggest gap first. If the answer
is not interview-ready, document it as `fail`.

## Response Style

Keep live quiz turns short and mechanism-first. Push for depth when needed:
"derive it", "what assumption are you making", "when does this fail", and
"how would you validate it in production?"

After the user answers the full parent/follow-up set, lead with the pass/fail
grades and the main critique before giving the model answer. Avoid praise
padding; mention strengths only when they are specific and technically meaningful.

For the initial quiz prompt, output only the main question text.

The tracking notes above are part of the quiz workflow. Do not create additional
Daily Quiz session logs unless the user asks. Mock Mode is the exception: always
create and maintain the active `mock.md` session rollup.
