---
name: ml-fundamentals-interview
description: "Staff/Senior Staff MLE ML theory and fundamentals interview prep for conversational Q&A rounds. Use for create, solve, companioned learn, or mock mode when preparing non-coding, non-system-design ML fundamentals topics with one self-contained topic directory."
---

# ML Fundamentals Interview

**Purpose:** End-to-end Staff/Senior Staff MLE ML fundamentals prep for conversational theory rounds: create topic folders, synthesize answers, companion learning with notes, and run realistic mocks.

**Boundary:** Use this for ML theory and fundamentals. Do not use it for coding rounds, daily quiz tracking, or ML system design whiteboards.

**Important:** First identify the current topic directory. All `context/`, `input/`, `solution/`, and `mock_MMDD/` paths are subdirectories of that topic directory, similar to `coding-interview-companion`.

## Topic Directory Resolution

Before reading or writing files, set `topic_dir`:

1. If the user provides a topic directory or file path, use it. If they provide a file inside `context/`, `input/`, `solution/`, `mock_MMDD/`, or legacy flat files, walk upward to the nearest directory that contains the topic artifacts.
2. Otherwise, if the current directory contains `context/`, `input/`, `solution/`, `mock_MMDD/`, or legacy flat topic files such as `topic.md`, `answer.md`, `deep_dive.md`, `learn_notes.md`, or `mock_feedback.md`, use the current directory.
3. Otherwise, search nearby child directories for `context/*.md`, `input/0_requirements.md`, `input/topic.md`, `solution/deep_dive.md`, `solution/learn_notes.md`, or legacy flat files.
4. If multiple topic directories match and the current topic is ambiguous, ask one concise clarification question.

After resolving `topic_dir`, use:

- `topic_context = <topic_dir>/context`
- `topic_input = <topic_dir>/input`
- `topic_solution = <topic_dir>/solution`
- `topic_mock = <topic_dir>/mock_MMDD` where `MMDD` is the current local date, e.g. `mock_0602`

Create directories as needed for the selected mode. Treat `context/` as raw source material and never overwrite it.

## Directory Structure

All paths are relative to `topic_dir`:

```text
topic-directory/
  context/
    ...                         # Raw notes, prompt dumps, screenshots converted to text, source docs
  input/
    0_requirements.md           # Clean topic requirements synthesized from context or the user request
    topic.md                    # Candidate-facing topic prompt and scope
    follow_up_questions.md      # Important interviewer probes and next-round focus
  solution/
    answer.md                   # Crisp spoken Staff+ answer
    deep_dive.md                # Durable reference and refinements
    learn_notes.md              # Raw/stabilized companion learning notes
  mock_MMDD/
    mock_instructions.md        # Candidate-facing mock topic and constraints
    mock_feedback.md            # Mock transcript, strict feedback, verdict, weakness notes
```

Legacy flat files directly under `topic_dir` are allowed as read-only supporting context unless Julie asks to migrate them. New artifacts should use the directory structure above.

## Modes

- **Create mode:** Create or normalize the topic directory from Julie's request or raw notes. Write `context/raw_notes.md` when source material is provided directly, then create `input/0_requirements.md` and `input/topic.md`.
- **Solve mode:** Read `context/` and `input/`, create or update `input/0_requirements.md` if missing, then write `solution/answer.md` and `solution/deep_dive.md`.
- **Companioned learn mode:** Passive Q&A companion. Answer Julie's questions directly, keep concise necessary context, and proactively record stabilized interview-relevant Q&A in `solution/learn_notes.md`. Do not prompt or quiz unless explicitly in mock mode.
- **Mock mode:** Run a realistic Staff/Senior Staff MLE conversational theory interview, one question per turn, and record feedback in a fresh `mock_MMDD/` session.

## Staff+ Operating Principles

1. **Assume strong ML fundamentals.** Avoid 101-level teaching unless Julie asks. Spend depth on mechanisms, assumptions, equations, failure modes, and tradeoffs.
2. **Optimize for Staff/Senior Staff MLE signal.** Start with a crisp thesis, explain the causal mechanism, and connect to LLMs, representation learning, optimization, evaluation, scaling behavior, or reliability when relevant.
3. **Separate correctness from seniority.** Name the basic correct answer, then show the Staff+ answer: assumptions, where it breaks, practical implications, and strong interview phrasing.
4. **Stay conversational and concise.** Prefer oral-answer structure over long essays. Use one compact example only when it sharpens intuition.
5. **Be proactive with notes.** Update learning or mock notes after meaningful interview-relevant exchanges without asking permission.

## Create Mode Workflow

Use create mode when Julie asks to create a topic, provides raw notes without an existing structure, or wants this skill to initialize prep artifacts.

1. Resolve or create `topic_dir`.
   - If Julie provides a topic name but no path, create a lower-case snake_case directory in the current workspace.
   - Use a descriptive topic slug, e.g. `cross_entropy_vs_kl`, `bias_variance_tradeoff`, `attention_mechanism`.
2. Create `context/`, `input/`, and `solution/`.
3. Preserve raw source material:
   - If Julie pasted raw notes or a prompt, write it to `context/raw_notes.md`.
   - If source files already exist, leave them unchanged.
4. Write `input/0_requirements.md` with:
   - Topic framing and likely interviewer prompt.
   - Concepts in scope and out of scope.
   - Required definitions, notation, equations, mechanisms, assumptions, and failure modes.
   - Staff+ evaluation criteria.
   - Likely follow-up probes.
   - Ambiguities and chosen assumptions.
5. Write `input/topic.md` as the candidate-facing topic prompt:
   - Clean question.
   - Expected answer dimensions.
   - Constraints and assumptions.
   - Follow-up themes, without answer keys.
6. Summarize created files and suggest solve mode only if Julie asked for the full answer next.

## Solve Mode Workflow

Use solve mode to turn a topic description into interview-ready study artifacts.

### Phase 1: Topic Analysis

1. Resolve `topic_dir`.
2. Read raw source from `context/` and generated prompts from `input/`, preferring `input/0_requirements.md`, `input/topic.md`, and explicit files named by Julie.
3. If `input/0_requirements.md` is missing, create it from available context before writing solutions.
4. Identify:
   - Core concept and likely interview prompt.
   - What a Staff/Senior Staff MLE interviewer is testing.
   - Essential definitions, equations, mechanisms, assumptions, and failure modes.
   - Likely follow-up probes and common misconceptions.
5. If context is vague, make reasonable assumptions and state them in the output instead of blocking.

### Phase 2: Create `solution/answer.md`

Write `solution/answer.md` as a crisp spoken answer for a real interview:

- **Question / Topic:** Likely interview prompt.
- **Short Answer:** 3-6 sentence thesis-first answer.
- **Core Mechanism:** Causal explanation, with equations only when useful.
- **Staff+ Depth:** Assumptions, failure modes, tradeoffs, and production relevance.
- **Example:** One compact example if it clarifies the concept.
- **Follow-Ups:** Likely interviewer probes and short answer sketches.
- **Delivery Notes:** What Julie should say aloud under time pressure.

Keep it interview-ready and conversational, not a textbook chapter.

### Phase 3: Create `solution/deep_dive.md`

Write `solution/deep_dive.md` as the durable reference:

- **Concept Map:** Adjacent ML fundamentals and dependencies.
- **Definitions & Notation:** Precise terms, variables, and assumptions.
- **Mechanism / Derivation:** Full explanation, derivation, or proof sketch when relevant.
- **Intuition:** One clear mental model.
- **Edge Cases & Failure Modes:** Where the concept breaks or becomes misleading.
- **Practical ML / LLM Relevance:** Training, evaluation, scaling, optimization, representations, or reliability.
- **Common Misconceptions:** Candidate mistakes and corrections.
- **Staff+ Interview Follow-Ups:** Harder questions with strong answer outlines.
- **Interview Phrasing:** Short sentences Julie can say aloud.

`deep_dive.md` should be deeper than `answer.md` but still focused on interview use.

### Phase 4: Walk-Through

Summarize:

- The topic framing.
- Highest-risk concepts to review.
- Files created or updated.

## Companioned Learn Mode Workflow

Use companioned learn mode as a passive read-along Q&A companion with auto-notes. Do not lecture upfront.

### Setup

1. Resolve `topic_dir`.
2. Silently read relevant local context from `input/`, `solution/answer.md`, `solution/deep_dive.md`, and source notes.
3. Create `solution/learn_notes.md` if it does not exist.
4. Wait for Julie's question. Do not offer a menu, prompt her with questions, quiz her, or start teaching unless asked.

### During Learning

1. **Answer the immediate question.**
   - Answer directly and stop cleanly.
   - Keep explanations brief with only necessary context and details.
   - Use plain language first, then technical depth if needed.
   - Use one compact example at most.
   - Highlight Staff+ interview phrasing when useful.

2. **Keep notes for stable interview questions.**
   - A question is stabilized when the direct answer and immediate clarification are complete.
   - Record every interview-relevant stabilized question or insight in `solution/learn_notes.md`.
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

4. **Do not update `solution/deep_dive.md` during active learn mode.**
   - Keep `solution/learn_notes.md` as the session buffer.
   - Stay in learn mode until Julie explicitly says `end learn`, `conclude learn`, `exit learn`, `wrap learning`, `finish learning`, or asks to consolidate learning notes.
   - Do not treat generic `summarize`, `done`, `next`, or a topic change as permission to exit learn mode unless it clearly refers to the learning session.

### End of Learn Session

When Julie explicitly wraps learning or asks to consolidate:

1. Read the full `solution/learn_notes.md`.
2. Remove duplicate, low-signal, or non-interview-relevant entries unless Julie asked to preserve them.
3. Group related questions by concept, misconception, follow-up theme, or interview phrasing.
4. Merge cleaned takeaways into `solution/deep_dive.md` under relevant sections or a dated `Learning Notes & Refinements` section.
5. Preserve useful grounding, examples, edge cases, and strong phrasing.
6. Reset `solution/learn_notes.md` to a short staging inbox or mark merged entries with the date.
7. Summarize what changed in `deep_dive.md` and what remains open.

## Mock Mode Workflow

Use mock mode to simulate a Staff/Senior Staff MLE conversational theory interview.

### Setup

1. Resolve `topic_dir`.
2. Read mock context from `input/0_requirements.md`, `input/topic.md`, `solution/answer.md`, `solution/deep_dive.md`, and source notes.
3. Create a fresh top-level mock directory named `mock_MMDD/`. If one already exists today, create `mock_MMDD_2/`, `mock_MMDD_3/`, etc.
4. Write `mock_instructions.md` with only the candidate-facing topic, constraints, and expected answer dimensions. Do not include answer keys, hints, rubrics, or expected sequence.
5. Create `mock_feedback.md`.
6. State only the interview topic and your role as interviewer.
7. Ask exactly one question. Do not reveal the answer, rubric, expected sequence, or hints.

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
   - If Julie says "I don't know", briefly teach the missing concept, then return to the interview with one follow-up.

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
- Record the verdict and improvements in `mock_feedback.md`.
- Summarize misses and weaknesses from the session.
- Convert important misses into candidate-facing next-round probes in `input/follow_up_questions.md`, without answer keys or hidden hints.

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
|------|---------|------------|-----------------|------------------|
| `context/*` | Raw source material | Create/User | No | Reference |
| `input/0_requirements.md` | Generated topic requirements | Create/Solve | No | Reference |
| `input/topic.md` | Candidate-facing topic prompt | Create/Solve | No | Reference |
| `input/follow_up_questions.md` | Next-round probes from misses | Mock | No | Reference |
| `solution/answer.md` | Staff+ interview-ready spoken answer | Solve | Optional reference only | Reference |
| `solution/deep_dive.md` | Durable ML theory reference | Solve + Learn wrap-up | Wrap-up only | Reference |
| `solution/learn_notes.md` | Learning Q&A notes | Learn | Yes | No |
| `mock_MMDD/mock_instructions.md` | Candidate-facing mock topic | Mock | No | Reference |
| `mock_MMDD/mock_feedback.md` | Mock transcript, feedback, verdict | Mock | No | Yes |

## Relationship to Other Skills

- Use `coding-interview-companion` for algorithm, coding, or implementation rounds.
- Use `ml-system-design-interview` for ML system design, architecture, platform, serving, ranking, or research infrastructure rounds.
- Use `ml-daily-quiz` for tracked daily drills and spaced review over a fixed question bank.
- Use this skill for topic-folder-based ML theory prep and conversational Staff+ mock interviews.
