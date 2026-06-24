---
name: mock-ml-fundamental
description: "Staff/Senior Staff MLE ML theory and fundamentals mock interviews. Supports setup mock and mock: questions come from a user-specified question bank; answer assessment may use learning artifacts."
---

# Mock ML Fundamental

**Purpose:** Set up and run realistic Staff/Senior Staff MLE ML fundamentals mock interviews.

**Boundary:** This skill is mock-only. Do not use it to create topics, solve study prompts, write deep dives, or run companion learning. Use `teach` for learn mode, solve mode, explanations, study notes, and consolidation.

## Topic Directory Resolution

Before reading or writing files, set `topic_dir`:

1. If Julie provides a topic directory, use it.
2. If Julie provides a file path, walk upward to the nearest directory that contains root mock files such as `mock_question_bank.md` or `mock.md`, or optional assessment files such as `deep_dive.md`, `reference.md`, or `solution.md`.
3. Otherwise, if the current directory contains `mock_question_bank.md`, `mock.md`, `deep_dive.md`, `reference.md`, or `solution.md`, use the current directory.
4. Otherwise, search nearby child directories for `mock_question_bank.md` or `mock.md`.
5. If multiple topic directories match and the current topic is ambiguous, ask one concise clarification question.

## Directory Structure

All paths are relative to `topic_dir`:

```text
topic-directory/
  mock_question_bank.md       # User-specified source question bank for question selection
  deep_dive.md                # Optional answer and assessment grounding only
  reference.md                # Optional answer and assessment grounding only
  solution.md                 # Interviewer-only solution key for all mock questions
  mock.md                     # Candidate-facing setup, dated transcript, feedback, verdict, rollup, and next-round probes
```

## Staff+ Operating Principles

1. **Assume strong ML fundamentals.** Avoid 101-level teaching unless Julie asks. Spend depth on mechanisms, assumptions, equations, failure modes, and tradeoffs.
2. **Optimize for Staff/Senior Staff MLE signal.** Evaluate whether the answer explains the causal mechanism and connects to LLMs, representation learning, optimization, evaluation, scaling behavior, or reliability when relevant.
3. **Separate correctness from seniority.** Name the basic correctness issue, then judge Staff+ strength: assumptions, where it breaks, practical implications, and interview phrasing.
4. **Stay interviewer-like.** Ask one question at a time. Do not coach unless Julie asks for help.
5. **Be strict and useful.** Record mock notes, weaknesses, and next drills without asking permission.

## Mock Mode Workflow

This skill has two explicit workflows:

- **Setup mock:** Prepare root-level mock artifacts from the user-specified question bank. Stop after setup; do not start the interview.
- **Mock:** Run the live Staff/Senior Staff MLE conversational theory interview. If setup artifacts are missing, run setup first, then ask the first question.

### Setup Mock

Trigger this workflow when Julie says `setup mock`, `set up mock`, `prepare mock`, or asks to initialize mock files.

1. Resolve `topic_dir`.
2. Resolve the user-specified question bank before creating mock content.
   - If Julie provides a question-bank file path, read it and use it as the sole source bank for this session.
   - If Julie provides question-bank content directly, write or append it to root `mock_question_bank.md`, normalizing each question to checkbox format.
   - If a root `mock_question_bank.md` exists, use it unless Julie provided a different one.
   - If no question bank is specified or discoverable, ask one concise clarification question for the question-bank file or content before starting setup.
   - Do not use `deep_dive.md`, `reference.md`, `solution.md`, or other learning artifacts to create, expand, or fill gaps in the question bank.
   - `solution.md` is created from the finalized question bank as the interviewer-only answer key; `deep_dive.md` and `reference.md` may be used later only as supplemental answer and assessment grounding after Julie answers.
   - Do not auto-generate the initial question bank unless Julie explicitly asks you to create one, and then ground it only in the materials she provides for that question bank.
   - The question bank should contain questions, expected answers or evaluation notes, what each question tests, and grounding/source notes when available.
   - Every question must be a Markdown checkbox item. Use unchecked boxes for not-yet-asked questions and checked boxes for questions already used in a completed mock session.

Question-bank entry format:

```markdown
## <topic>

- [ ] **Q:** <candidate-facing question>
  - Tests: <concept, skill, or misconception>
  - Expected answer / evaluation notes: <interviewer-only answer guidance>
  - Grounding: <source section or note, if available>
  - Asked: <blank until used, then YYYY-MM-DD mock>
```
3. Create or update root `solution.md` for all questions in `mock_question_bank.md`.
   - Include every mock question, grouped by topic in the same order as the question bank.
   - Use the question bank's expected answer, evaluation notes, tests, and grounding as the primary source.
   - If a question lacks enough answer guidance, include a `Needs answer source` note instead of inventing unsupported content.
   - Keep `solution.md` interviewer-only. Do not expose it during the mock unless Julie explicitly asks after the mock.
   - Do not add new questions to `solution.md` that are absent from `mock_question_bank.md`.
4. Create `mock.md` at the root of `topic_dir` if it does not exist. Append one dated section for every mock session.
5. In `mock.md`, include a candidate-facing setup block with only the topic, constraints, and expected answer dimensions derived from `mock_question_bank.md`. Do not include answer keys, hints, rubrics, grounding, or expected sequence.
6. In the same dated section of `mock.md`, include placeholders for the transcript, per-turn feedback, verdict, weaknesses, next review, and next-round probes.
7. Do not expose `mock_question_bank.md` or `solution.md` to Julie during the mock unless she asks to inspect them after the mock.
8. Stop after setup. Report the files prepared using wikilinks and say that `mock` will start the interview.

Root `solution.md` format:

```markdown
# Mock Solutions

## <topic>

### Q: <candidate-facing question>

- Tests: <concept, skill, or misconception>
- Expected answer: <interviewer-only answer guidance>
- Evaluation notes: <what makes the answer strong, partial, or wrong>
- Staff+ signals: <mechanism, assumptions, tradeoffs, edge cases, LLM/frontier relevance>
- Grounding: <source section or question-bank note>
```

### Mock

Trigger this workflow when Julie says `mock`, `start mock`, `run mock`, or asks to begin the interview.

1. Resolve `topic_dir`.
2. Verify `mock.md`, `mock_question_bank.md`, and `solution.md` exist. If any are missing, run **Setup Mock** first.
3. Read `mock_question_bank.md` for question selection. Read `solution.md` after Julie answers for answer and assessment grounding. Read `deep_dive.md` and `reference.md` only if they exist and only as supplemental answer and assessment grounding after Julie answers.
4. State only the interview topic and your role as interviewer.
5. Ask exactly one question from `mock_question_bank.md`. Do not reveal the answer, rubric, expected sequence, grounding, or hints.

### During Mock

1. **Ask one question per assistant turn.**
   - Ask from `mock_question_bank.md` by default.
   - Prefer unchecked questions that match the current weak spot or natural follow-up path.
   - If the conversation reveals a new grounded follow-up, add it to `mock_question_bank.md` before or after asking it, but keep it clearly marked as session-generated.
   - Probe one thing at a time: definition, mechanism, equation, assumption, failure mode, tradeoff, production implication, or connection to LLM systems.
   - Do not bundle multiple numbered questions.
   - Do not coach or suggest what Julie should answer next.
   - Do not ask questions that are not supported by `mock_question_bank.md` unless Julie explicitly asks to broaden the mock and provides additional question-bank material.

2. **When Julie answers, respond like an interviewer.**
   - Give strict Staff+ feedback: correct, imprecise, missing, or wrong.
   - Distinguish basic correctness from Staff+ strength when useful.
   - Provide a stronger answer after feedback.
   - Ground feedback, assessment, and stronger answers first in `solution.md`, then in available `deep_dive.md`, `reference.md`, and the evaluation notes in `mock_question_bank.md`. Do not use those learning artifacts to introduce new questions that are absent from the question bank.
   - Ask exactly one follow-up question.

3. **Only give hints when asked.**
   - If Julie asks for clarification, clarify the question without revealing the full answer.
   - If Julie asks for help, give the smallest useful hint and record it.
   - If Julie says "I don't know", briefly teach the missing concept, then return to the interview with one follow-up.

4. **Record every interview-relevant turn in the dated section of `mock.md`:**

   ```markdown
   ## <date> - <topic>

   ### Question
   <question asked>

   ### Grounding
   <mock_question_bank.md section used to select the question; solution.md section plus any deep_dive.md, reference.md, or question-bank evaluation notes used for assessment>

   ### Julie's Answer
   <faithful summary or quote>

   ### Feedback
   <strict Staff+ feedback>

   ### Stronger Answer
   <interview-ready answer>

   ### Follow-Up
   <next question>
   ```

### Closing

When Julie asks to stop or the mock reaches a natural end:

- Give a verdict: `strong pass`, `pass`, `lean pass`, `lean no`, or `no-hire for this round`.
- Include 2-4 focused improvements.
- Identify the weakest concept to review next.
- Record the verdict and improvements in the dated section for this session in root `mock.md`.
- Complete the rollup fields for this session in root `mock.md`.
- In `mock_question_bank.md`, check off every question asked in this mock session and fill its `Asked:` field with the mock date or session label.
- Summarize misses and weaknesses from the session.
- Convert important misses into candidate-facing next-round probes inside the dated section of root `mock.md`, without answer keys or hidden hints.

Root `mock.md` dated section format:

```markdown
## YYYY-MM-DD - <topic or focus>

- Candidate-facing setup:
  - Topic: <topic or focus>
  - Constraints: <scope, target level, or interview constraints>
  - Expected answer dimensions: <candidate-facing dimensions only, no answer keys or hidden rubric>
- Question source: `mock_question_bank.md`
- Answer and assessment grounding: `solution.md`, plus `deep_dive.md`, `reference.md`, and/or question-bank evaluation notes used
- Verdict: `strong pass | pass | lean pass | lean no | no-hire for this round`
- Strengths: <short bullets or one-line summary>
- Weaknesses: <specific concepts, confusions, or communication issues>
- Next review: <weakest concept and 1-3 drills>
- Next-round probes: <candidate-facing follow-up questions from important misses, without answer keys>
```

## Feedback Rubric

Evaluate Staff/Senior Staff MLE theory answers against:

| Dimension | What to Look For |
|-----------|------------------|
| Precision | Definitions, notation, and assumptions are correct. |
| Mechanism | Explains why the concept works, not just what it is. |
| Math | Uses equations or derivations correctly when relevant. |
| Intuition | Gives a durable mental model without oversimplifying. |
| Edge Cases | Names where assumptions break or the result changes. |
| Tradeoffs | Connects choices to quality, compute, data, robustness, or maintainability. |
| LLM / Frontier Relevance | Relates fundamentals to modern model training, evaluation, scaling, or reliability when appropriate. |
| Staff+ Signal | Prioritizes crux, communicates crisply, and can handle follow-up pressure. |
| Communication | Answers conversationally and directly without rambling. |

## File Reference

| File | Purpose | Created by | Reviewed in Mock |
|------|---------|------------|------------------|
| `mock_question_bank.md` | User-specified source question bank for question selection | User | Primary |
| `deep_dive.md` | Optional answer and assessment grounding | User/Teach | Assessment only |
| `reference.md` | Optional answer and assessment grounding | User/Teach | Assessment only |
| `solution.md` | Interviewer-only solution key for every question in `mock_question_bank.md` | Mock | Assessment only |
| `mock.md` | Candidate-facing setup, dated transcript, feedback, verdict, rollup, and next-round probes | Mock | Yes |

## Relationship to Other Skills

- Use `coding-interview-companion` for algorithm, coding, or implementation rounds.
- Use `ml-system-design-interview` for ML system design, architecture, platform, serving, ranking, or research infrastructure rounds.
- Use `ml-daily-quiz` for tracked daily drills and spaced review over a fixed question bank.
- Use `teach` for ML fundamentals learn mode, solve mode, explanations, study notes, companion learning, and consolidation.
