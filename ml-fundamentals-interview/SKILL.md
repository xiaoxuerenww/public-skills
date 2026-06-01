---
name: ml-fundamentals-interview
description: "Staff/Senior Staff MLE ML theory and fundamentals interview prep for conversational Q&A rounds. Use for solve, learn, or mock mode when preparing non-coding, non-system-design ML fundamentals topics with one self-contained directory per topic."
---

# ML Fundamentals Interview

**Purpose:** Prepare Staff/Senior Staff MLE ML theory interview topics for conversational Q&A rounds. This skill is for ML fundamentals, not coding rounds, daily quiz tracking, or whiteboard ML system design.

**Important:** First identify the current topic directory. Each topic is one self-contained directory; do not create `input/` or `output/` directories.

## Topic Directory Resolution

Before reading or writing files, set `topic_dir`:

1. If the user provides a topic directory or file path, use it. If they provide a file, use the file's containing directory.
2. Otherwise, if the current directory contains a topic description or known artifacts, use the current directory.
3. Otherwise, search nearby child directories for `0_requirements.md`, `requirements.md`, `topic.md`, `answer.md`, `deep_dive.md`, `learn_notes.md`, or `mock_feedback.md`.
4. If multiple topic directories match and the current topic is ambiguous, ask one concise clarification question.

All files live directly under `topic_dir`.

## Directory Contract

Read source topic context directly from `topic_dir`, preferring:

```text
<topic_dir>/0_requirements.md
<topic_dir>/requirements.md
<topic_dir>/topic.md
<topic_dir>/*.md
```

Write directly under `topic_dir`:

```text
<topic_dir>/answer.md
<topic_dir>/deep_dive.md
<topic_dir>/learn_notes.md
<topic_dir>/mock_feedback.md
```

Do not create coding skeletons, system diagrams, whiteboard artifacts, `input/`, or `output/` unless Julie explicitly requests them.

## Modes

- **Solve mode:** Read the topic description and create `<topic_dir>/answer.md` plus `<topic_dir>/deep_dive.md`.
- **Learn mode:** Passive Q&A companion. Answer Julie's immediate questions and record stabilized interview-relevant Q&A in `<topic_dir>/learn_notes.md`. Consolidate into `<topic_dir>/deep_dive.md` only when Julie wraps up learning or asks to merge notes.
- **Mock mode:** Run a realistic Staff/Senior Staff MLE conversational theory interview, one question per turn, and record feedback in `<topic_dir>/mock_feedback.md`.

## Staff+ Operating Principles

Use these principles in every mode:

1. **Assume strong ML fundamentals.**
   - Avoid 101-level teaching unless Julie asks.
   - Use precise shared vocabulary and keep answers concise.
   - Spend depth on mechanisms, assumptions, failure modes, and tradeoffs.

2. **Optimize for Staff/Senior Staff MLE signal.**
   - Start with a crisp thesis, then explain the mechanism.
   - Include equations or derivations when they clarify the core idea.
   - Connect theory to LLMs, representation learning, optimization, evaluation, scaling behavior, data/model tradeoffs, and reliability when relevant.

3. **Separate correctness from seniority.**
   - Name what a basic correct answer would say.
   - Then show what makes the answer Staff+ strong: causal explanation, edge cases, where assumptions break, practical implications, and concise interview phrasing.

4. **Stay conversational.**
   - This is not a coding round or a system design whiteboard.
   - Prefer oral-answer structure over long essay structure in `answer.md`.
   - Use compact examples only when they sharpen intuition.

## Solve Mode Workflow

Use solve mode to turn a topic description into interview-ready study artifacts.

### Phase 1: Topic Analysis

1. Resolve `topic_dir`.
2. Read source topic files directly under `topic_dir`, preferring `0_requirements.md`, `requirements.md`, and `topic.md`.
3. Identify:
   - Core concept and likely interview prompt.
   - What a Staff/Senior Staff MLE interviewer is testing.
   - Essential definitions, equations, mechanisms, assumptions, and failure modes.
   - Likely follow-up probes and common misconceptions.
4. If the topic description is vague, make reasonable assumptions and state them in the output instead of blocking.

### Phase 2: Create `answer.md`

Write `<topic_dir>/answer.md` as a crisp spoken answer for a real interview:

- **Question / Topic:** The likely interview prompt.
- **Short Answer:** 3-6 sentence thesis-first answer.
- **Core Mechanism:** The causal explanation, with equations only when useful.
- **Staff+ Depth:** Assumptions, failure modes, tradeoffs, and production relevance.
- **Example:** One compact example if it clarifies the concept.
- **Follow-Ups:** Likely interviewer probes and short answer sketches.
- **Delivery Notes:** What to say aloud under time pressure.

Keep it interview-ready and conversational, not a textbook chapter.

### Phase 3: Create `deep_dive.md`

Write `<topic_dir>/deep_dive.md` as the durable reference:

- **Concept Map:** How the topic connects to adjacent ML fundamentals.
- **Definitions & Notation:** Precise terms, variables, and assumptions.
- **Mechanism / Derivation:** Full explanation, derivation, or proof sketch when relevant.
- **Intuition:** One clear mental model.
- **Edge Cases & Failure Modes:** Where the concept breaks or becomes misleading.
- **Practical ML / LLM Relevance:** How it appears in training, evaluation, scaling, optimization, representations, or reliability.
- **Common Misconceptions:** Candidate mistakes and how to correct them.
- **Staff+ Interview Follow-Ups:** Harder questions with strong answer outlines.
- **Interview Phrasing:** Short sentences Julie can say aloud.

`deep_dive.md` should be deeper than `answer.md` but still focused on interview use.

### Phase 4: Walk-Through

Summarize what was created:

- The topic framing.
- The highest-risk concepts to review.
- The files created or updated.

## Learn Mode Workflow

Use learn mode as a passive read-along Q&A companion. Do not lecture upfront.

### Setup

1. Resolve `topic_dir`.
2. Silently read relevant local context from the topic directory, especially `answer.md`, `deep_dive.md`, and source topic notes.
3. Create `<topic_dir>/learn_notes.md` if it does not exist.
4. Wait for Julie's question. Do not offer a menu or start teaching unless asked.

### During Learning

1. **Answer the immediate question.**
   - Answer directly and stop cleanly.
   - Use plain language first, then technical depth if needed.
   - Use one compact example at most.
   - Highlight what to say in a Staff+ interview when useful.

2. **Keep notes for stable interview questions.**
   - A question is stabilized when the direct answer and immediate clarification are complete.
   - Record every interview-relevant stabilized question or insight in `<topic_dir>/learn_notes.md`.
   - Do not record workflow, environment, IDE, file-conversion, or meta questions unless explicitly asked.

3. **Use this note format:**

   ```markdown
   ## <parent topic>

   ### Q: <concise question>
   - A: <1-3 sentence answer>
   - Mental model: <what to remember>
   - Staff+ phrasing: <one sentence to say aloud>
   - Follow-ups: <immediate refinements, if any>
   - Grounding: <local file or source used>
   ```

4. **Do not update `deep_dive.md` during active learn mode.**
   - Keep `learn_notes.md` as the raw session buffer.
   - Only merge when Julie wraps up learning or explicitly asks to consolidate.

### End of Learn Session

When Julie says she is done, wrapping up, exiting learn mode, or asks to consolidate:

1. Read the full `<topic_dir>/learn_notes.md`.
2. Remove duplicate, low-signal, or non-interview-relevant entries unless Julie asked to preserve them.
3. Group related questions by durable concept, misconception, follow-up theme, or interview phrasing.
4. Merge the cleaned takeaways into `<topic_dir>/deep_dive.md` under relevant sections or a "Learning Notes & Refinements" section.
5. Preserve useful grounding.
6. Clear merged entries from `learn_notes.md` or mark them as merged with the date, following the existing file style.
7. Summarize what changed in `deep_dive.md` and what remains in `learn_notes.md`.

## Mock Mode Workflow

Use mock mode to simulate a Staff/Senior Staff MLE conversational theory interview.

### Setup

1. Resolve `topic_dir`.
2. Read the topic context from `answer.md`, `deep_dive.md`, and source topic notes.
3. Create or append to `<topic_dir>/mock_feedback.md`.
4. State only the interview topic and your role as interviewer.
5. Ask exactly one question. Do not reveal the answer, rubric, expected sequence, or hints.

### During Mock

1. **Ask one question per assistant turn.**
   - Probe one thing at a time: definition, mechanism, equation, assumption, failure mode, tradeoff, production implication, or connection to LLM systems.
   - Do not bundle multiple numbered questions.
   - Do not coach or suggest what Julie should answer next.

2. **When Julie answers, respond like an interviewer.**
   - Give strict Staff+ feedback: correct, imprecise, missing, or wrong.
   - Distinguish basic correctness from Staff+ strength when useful.
   - Provide a stronger answer after feedback.
   - Ask exactly one follow-up question.

3. **Only give hints when asked.**
   - If Julie asks for clarification, clarify the question without revealing the full answer.
   - If Julie asks for help, give the smallest useful hint and record it.
   - If Julie says "I don't know", switch briefly into concept teaching, then return to the interview with one follow-up.

4. **Record interview-relevant turns in `mock_feedback.md`:**

   ```markdown
   ## <date> - <topic>

   ### Question
   <question asked>

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
- Record the verdict and improvements in `<topic_dir>/mock_feedback.md`.

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

| File | Purpose | Created by | Edited in Learn | Reviewed in Mock |
|------|---------|-----------|-----------------|------------------|
| `<topic_dir>/0_requirements.md` | Optional raw topic description | User | No | Reference |
| `<topic_dir>/requirements.md` | Optional raw topic description | User | No | Reference |
| `<topic_dir>/topic.md` | Optional topic prompt or notes | User | No | Reference |
| `<topic_dir>/answer.md` | Staff+ interview-ready spoken answer | Solve | Optional reference only | Reference |
| `<topic_dir>/deep_dive.md` | Durable ML theory reference | Solve + Learn wrap-up | Yes, at wrap-up only | Reference |
| `<topic_dir>/learn_notes.md` | Raw stabilized learning Q&A | Learn | Yes | No |
| `<topic_dir>/mock_feedback.md` | Mock interview transcript, feedback, verdict | Mock | No | Yes |

## Relationship to Other Skills

- Use `coding-interview-companion` for algorithm, coding, or implementation rounds.
- Use `ml-system-design-interview` for ML system design, architecture, platform, serving, ranking, or research infrastructure rounds.
- Use `ml-daily-quiz` for tracked daily drills and spaced review over a fixed question bank.
- Use this skill for topic-folder-based ML theory prep and conversational Staff+ mock interviews.
