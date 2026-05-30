---
name: ml-daily-quiz
description: ML/LLM fundamentals interview prep for Julie. Use for daily tracked quizzes, "quiz me", spaced review, LLM fundamentals drills, Staff/Senior Staff MLE technical-depth practice, "learn ml fundamental" learn mode, "mock ml fundamental" interview mode, or explicit $ml-llm-daily-quiz / $daily-ml-concept requests.
---

# ML/LLM Fundamentals Quiz

## Purpose

Run Staff/Senior Staff MLE fundamentals drills with three modes:

- **Daily Quiz**: tracked no-repeat quiz with notes and pass/fail grading.
- **Learn Mode**: show one grounded question, model answer, and follow-up immediately.
- **Mock Mode**: ask one grounded interview question and wait for Julie's answer.

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
- If Julie says "mock ml fundamental", use Mock Mode.
- If Julie says "quiz me", "daily", "today's", asks for spaced review, or gives
  no explicit learn/mock wording, use Daily Quiz.
- If Julie names a topic in any mode, select a question from that topic.

This skill is Q&A only: no coding exercises, no whiteboard systems prompts, and
no system design unless Julie explicitly changes scope.

## Note-Taking Preferences

Persist quiz notes automatically in `ml_llm_daily_quiz_notes.md`.

Use this format for each recorded question:

```markdown
## <question text>

- Recorded: <timestamp>
- Status: `<pass|fail>`
- Question ID: `<id>`
- Times seen: <ask_count including the current attempt>
- Section: <section path>
- Topic: <topic>
- Notes: Ideal answer: ... Julie's answer: ... Feedback: ... Missing/wrong: ... Drill next: ...
```

For session summaries, also use the question text as each `##` heading and
include:

- `Your answer`: the user's actual answer or a faithful paraphrase.
- `Status`: `pass` or `fail`.
- `Critical feedback`: the main gap first, direct and specific.
- `Stronger answer`: an interview-ready version.
- `Drill next`: the next focused practice target.

Do not use timestamp, section, or topic as the heading. Do not hide weak areas
behind vague encouragement. Keep notes concise but explicit enough to support
spaced review.

## Daily Quiz Flow

1. Pick the next shuffled no-repeat question with:

   ```bash
   python3 /Users/xue/.codex/skills/ml-daily-quiz/scripts/pick_question.py
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
   answer and direct feedback in saved notes for the parent and each follow-up:

   ```bash
   python3 /Users/xue/.codex/skills/ml-daily-quiz/scripts/pick_question.py \
     --record-result QUESTION_ID \
     --status pass \
     --notes "Ideal answer: ... Julie's answer: ... Feedback: ... Missing/wrong: ... Drill next: ..."
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

## Mock Mode

Triggered by "mock ml fundamental".

Before asking, read the same Databricks source docs as Learn Mode. Ask the
question and wait for Julie's answer before revealing anything. Do not record
quiz progress or notes in this conversational mode.

Initial turn format:

```markdown
**Q:** <interview question from the source docs>
```

After Julie answers:

```markdown
**Feedback:** <what is correct, missing, or imprecise; grade strictly against the docs>

**Model Answer:** <concise answer from the docs>

**Follow-up Q:** <staff-level follow-up; wait for Julie's answer>
```

After Julie answers the follow-up:

```markdown
**Feedback:** <same grading approach>

**Model Answer:** <follow-up answer>

---
Next question? (or pick a topic)
```

Rules:

- Never show the answer before Julie responds.
- Grade against the docs; flag missing equations, wrong mechanisms, and
  incomplete tradeoffs.
- One question plus one follow-up per round.

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
  python3 /Users/xue/.codex/skills/ml-daily-quiz/scripts/pick_question.py --topic attention
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
- Keep result notes useful for review: exact `pass`/`fail` status, ideal answer,
  Julie's answer or faithful paraphrase, what was missing or technically wrong,
  how many times the question has been seen, and the next concept to revisit.
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
session logs unless the user asks.
