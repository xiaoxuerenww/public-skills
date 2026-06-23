---
name: ml-system-design-interview
description: "End-to-end ML system design interview prep with create, solve, companioned learn, and mock modes. Use when designing recommendation systems, ranking platforms, experiment pipelines, ML infra, model serving, evaluation systems, or research infrastructure: locate the current problem directory, preserve raw context, generate input prompts, write solution artifacts, take learning notes, and run dated mock sessions."
---

# ML System Design Interview

**Purpose:** Complete lifecycle support for Staff/Senior Staff ML system design prep: create a problem folder, synthesize L6+ solutions, companion learning with notes, and run realistic mock interviews.

**Boundary:** Use this for ML system design, architecture, platform, serving, ranking, recommendation, evaluation, experiment, and research-infrastructure prompts. Do not use it for coding implementation rounds or pure ML theory Q&A.

**Important:** First identify the current problem directory. All `context/`, `input/`, `solution/`, and `mock_MMDD/` paths are subdirectories of that problem directory, similar to `coding-interview-companion`.

## Problem Directory Resolution

Before reading or writing files, set `problem_dir`:

1. If the user provides a problem directory or file path, use it. If they provide a file inside `context/`, `input/`, `solution/`, `mock_MMDD/`, or legacy `output/`, walk upward to the nearest directory that contains the problem's artifact folders.
2. Otherwise, if the current directory contains `context/`, `input/`, `solution/`, `mock_MMDD/`, or legacy `output/`, use the current directory.
3. Otherwise, search nearby child directories for `context/*.md`, `input/0_requirements.md`, `input/*.md`, `solution/deep_dive.md`, legacy `output/deep_dive.md`, or `**/*requirements.md` and choose the directory that matches the current problem context.
4. If multiple directories match and the current problem is ambiguous, ask one concise clarification question.

After resolving `problem_dir`, use:

- `problem_context = <problem_dir>/context`
- `problem_input = <problem_dir>/input`
- `problem_solution = <problem_dir>/solution`
- `problem_mock = <problem_dir>/mock_MMDD` where `MMDD` is the current local date, e.g. `mock_0602`

Create directories as needed for the selected mode. Treat `context/` as raw source material and never overwrite it. Legacy `output/` is allowed as supporting context for old prep folders, but new artifacts should use `solution/` and `mock_MMDD/`.

## Directory Structure

All paths are relative to the resolved `problem_dir`:

```text
problem-directory/
  context/
    ...                         # Raw prompt dumps, requirements, notes, screenshots converted to text, source docs
  input/
    0_requirements.md           # Normalized prep prompt from raw context and discovered requirements
    <problem_name>.md           # Candidate-facing problem statement
    next_round_mock_questions.md # Follow-up drills generated from prior mock misses
  solution/
    interview_solutions.md      # Interview-ready L6+ answer
    deep_dive.md                # Design rationale and durable concepts
    learn_notes.md              # Companion learning Q&A notes
  mock_MMDD/
    mock_instructions.md        # Candidate-facing mock prompt and constraints
    my_solution.md              # Julie's design attempt for this mock
    mock_feedback.md            # Mock transcript, strict feedback, verdict, weakness notes
```

## Modes

- **Create mode:** Create or normalize the problem directory from Julie's request, raw notes, or requirement docs. Preserve raw material in `context/`, then write `input/0_requirements.md` and `input/<problem_name>.md`.
- **Solve mode:** Read `context/` and `input/`, normalize requirements if needed, frame the problem as L6+ MLE system design, then write `solution/interview_solutions.md` and `solution/deep_dive.md`.
- **Companioned learn mode:** Passive read-along Q&A. Wait for Julie's questions, answer directly with concise necessary context, ground responses in local notes or cited sources, and record stabilized Q&A in `solution/learn_notes.md`. Do not prompt, quiz, or ask check-for-understanding questions.
- **Mock mode:** Interview as a realistic hiring engineer, create a fresh dated `mock_MMDD/` session, ask one question per turn, review `mock_MMDD/my_solution.md`, and record feedback in `mock_MMDD/mock_feedback.md`.

---

## Reference Materials

Resolve these paths relative to `/Users/xue/.codex/skills/ml-system-design-interview/`, not `problem_dir`:

- `references/interview-answer-template.md`: answer structure, timing, special question types
- `references/mlsd-5phase-framework.md`: generic 5-phase ML system design framework
- `references/interview-communication-guide.md`: expectations, communication criteria
- `references/quick-concepts-cheatsheet.md`: metrics, latency, serving patterns, tech stack
- `references/framework-adaptation.md`: adapt framework to research infrastructure prompts

Read only the relevant reference files for the prompt. For non-serving research infrastructure prompts, adapt the 5 phases:

```text
1. Scope and success criteria
2. Inputs, data, config, and metadata model
3. Core algorithm or control plane
4. Execution, storage, and infrastructure
5. Observability, evaluation, iteration, and failure handling
```

For product ML systems, especially recommendation, ranking, search, feed, ads, marketplace, or personalization, use this local note as a structural reference only, not copied content:
`4_SystemDesign/Case study/Recommendation/Video Recommendation System Design  ML System Design in a Hurry.md`.

## Staff/Principal Operating Principles

Use these principles in every mode:

1. **Communicate like a staff+ peer.** Skip 101-level explanations unless asked. Use shared vocabulary, concise framing, and clear decisions.
2. **Find the crux early.** Separate straightforward plumbing from the 1-2 highest-risk design problems. Spend depth where judgment matters.
3. **Cut complexity by default.** Start with the simplest design that satisfies requirements. Add distributed systems, realtime paths, deep models, LLMs, or extra services only when constraints force them.
4. **Use ML production judgment.** Tie product goals, data, modeling, training, serving, evaluation, monitoring, and operations to latency, cost, freshness, safety, privacy, and rollback constraints.
5. **Show evolution and maturity.** Explain MVP, production hardening, and scale-out. Cover drift, leakage, training-serving skew, PII, safety, canaries, rollback, retraining, and maintainability.
6. **Use a metrics taxonomy.** Include business, offline ML, online product, guardrail, and infrastructure metrics.
7. **Keep explanations concise.** Answer the question with necessary context and details. Avoid broad component tours unless they are needed.

## Create Mode Workflow

Use create mode when Julie asks to create a new ML system design problem, provides raw context without structure, or wants the skill to initialize prep artifacts.

1. Resolve or create `problem_dir`.
   - If Julie provides a problem name but no path, create a lower-case snake_case directory in the current workspace.
   - Use a descriptive slug, e.g. `harmful_content_detection`, `rag_for_data_assets`, `experiment_tracking_platform`.
2. Create `context/`, `input/`, and `solution/`.
3. Preserve raw source material:
   - If Julie pasted raw notes or a prompt, write it to `context/raw_notes.md`.
   - If source files already exist, leave them unchanged.
   - If legacy `*requirements.md` or `output/` files exist, read them as supporting context and do not overwrite them.
4. Write `input/0_requirements.md` with:
   - Prompt, product surface, users, stakeholders, scale, constraints, goals, non-goals, and focus areas.
   - What the interviewer is testing: scoping, ML judgment, platform thinking, operational maturity, cross-team impact.
   - ML objective, product objective, success metrics, and guardrails.
   - Ambiguities and chosen assumptions.
   - Source Requirements section listing source files used.
5. Write `input/<problem_name>.md` with:
   - Clean candidate-facing problem statement.
   - Clarifying questions to ask upfront.
   - Known constraints and explicit non-goals.
   - Success metrics.
   - Follow-up themes, without answer keys or hidden hints.
6. Summarize created files and suggest solve mode only if Julie asked for the full answer next.

## Solve Mode Workflow

Use solve mode to analyze a system design prompt and produce interview-ready solution artifacts.

### Phase 1: Requirements Analysis

1. Resolve `problem_dir`.
2. Read raw context from `context/`, generated prompts from `input/`, and any discovered `**/*requirements.md` under `problem_dir`.
3. Prefer source prompts and raw requirements over derived solution artifacts. Use legacy `output/` only as supporting context.
4. Create or update `input/0_requirements.md` if it is missing important context.
5. Identify:
   - Problem type: product serving, research infra, ranking, config, evaluation, model serving, monitoring, etc.
   - Product objective, ML objective, users, scale, latency, cost, privacy, safety, and compliance constraints.
   - The crux: 1-2 hardest parts where staff-level judgment matters.
   - Straightforward parts to intentionally shortcut.
   - L6+ signals to demonstrate: ambiguity ownership, ML correctness, platform thinking, operational maturity, and strategic sequencing.

### Phase 2: Solve the System

For each problem, structure the answer around:

1. **Problem Framing:** Product surface, clarifying questions, assumptions, business objective, ML objective, non-goals, and success criteria.
2. **High-Level Design:** Main components, data flow, control flow, stage contracts, latency and cost budgets, precompute versus online paths, caching, fallbacks, and degradation.
3. **Data and Features:** Signal quality, freshness, explicit and implicit feedback, context, item/content/user features, leakage risk, bias, and training-serving consistency.
4. **Modeling:** Baselines, production model choice, retrieval or ranking stages, objective/loss when it matters, calibration, multitask or multi-objective composition, and model evolution.
5. **Inference and Evaluation:** Serving path, model serving, batching, hardware, caching, offline metrics, online tests, guardrails, experiment validity, and infra health.
6. **Deep Dives:** Pick 2-3 real cruxes. For each: problem, why it matters, options, chosen solution, why it wins, failure mode, and measurement.
7. **Failure Modes and Mitigation:** Data staleness, training-serving skew, leakage, drift, exposure bias, feedback loops, policy or safety regressions, cost blowups, canaries, rollback, and retraining triggers.
8. **Evolution Plan:** MVP, hardening, scale-out, and future model/system evolution.

### Phase 3: Create Solution Documents

1. Write `solution/interview_solutions.md` as the interview-ready answer:
   - Opener
   - Understanding the Problem
   - Problem Framing
   - High-Level Design with ASCII diagram when useful
   - Data and Features
   - Modeling
   - Inference and Evaluation
   - Crux and Simplifications
   - Deep Dives
   - Trade-Offs and Alternatives
   - Failure Modes and Debugging
   - Evolution Plan
   - Level Calibration
   - Wrap-Up
   - Interview Delivery

2. Write `solution/deep_dive.md` as the durable reference:
   - One section per major component or design decision.
   - For each section: problem, why hard, alternatives, chosen solution, why it works, invariants, pragmatic notes, and related concepts.
   - Include L6+ thinking: ambiguity ownership, cross-team contracts, migration strategy, ML correctness, operational maturity.

3. Run a rubric pass before finalizing:
   - Strengthen crux identification, complexity control, decision-making, ML correctness, metrics, failure modes, L6+ signal, and communication.
   - Prefer targeted depth on the riskiest parts over broad component tours.
   - Remove unnecessary 101 explanations and replace option lists with decisions plus concise justification.

4. Walk through the created artifacts:
   - Key architecture thesis.
   - Hardest tradeoff.
   - Files created or updated.

## Companioned Learn Mode Workflow

Use companioned learn mode as read-along Q&A support with auto-notes. The user is reading independently. Do not explain upfront or start teaching unless asked.

### Setup

1. Resolve `problem_dir`.
2. Read relevant local context silently: `input/0_requirements.md`, `input/<problem>.md`, `solution/interview_solutions.md`, `solution/deep_dive.md`, `solution/learn_notes.md`, and any provided notes or search-result packets. If only legacy `output/` exists, read it as supporting context.
3. Create `solution/learn_notes.md` if it does not exist.
4. Wait for Julie's question. Do not summarize, propose a menu, ask what she wants next, quiz her, or ask check-for-understanding questions.

### During Learning

1. **Read-Along Q&A Loop:**
   - Wait for the user's question.
   - Answer the immediate question directly and stop cleanly.
   - Do not proactively explain, continue, advance topics, or end with prompts.
   - If the user says "next", continue only if there is an established sequence from prior user questions or material.

2. **Grounding:**
   - Ground answers in local notes first: `input/0_requirements.md`, problem statements, `solution/interview_solutions.md`, `solution/deep_dive.md`, `solution/learn_notes.md`, and relevant bundled references.
   - If the user provides web search results, use those results as grounding and distinguish sourced facts from inference.
   - If the user explicitly asks to search the web, search and cite sources before answering.
   - If local notes and provided results are insufficient, say what is inferred and what is missing.

3. **Explanations:**
   - Use plain language first, then technical depth if needed.
   - Keep answers brief with necessary context and details.
   - Use one compact example at most.
   - Tie design choices back to requirements and L6+ signals.
   - Highlight Staff+ interview phrasing when useful.
   - Emphasize staff-level habits: identify the crux, cut unnecessary complexity, make decisions, and connect ML choices to production constraints.

4. **Auto-Notes:**
   - After each stabilized interview-relevant question or insight, record it in `solution/learn_notes.md`.
   - A question is stabilized when the direct answer and immediate clarification are complete.
   - Include:
     - **Q:** Concise question
     - **A:** 1-3 sentence answer
     - **Follow-ups:** Immediate refinements, if any
     - **Mental model:** What to remember or misconception fixed
     - **Interview phrasing:** One sentence Julie can say aloud
     - **Grounding:** Local note, source file, or cited source used
   - Do not record workflow, environment, IDE, file-conversion, or tooling questions unless explicitly asked.
   - Keep notes chronological and slightly raw, grouped by parent topic.

5. **Defer Deep-Dive Updates:**
   - During active learn mode, write only to `solution/learn_notes.md`.
   - Do not merge, rewrite, or polish `solution/deep_dive.md` until Julie explicitly exits or wraps up learn mode.
   - Stay in learn mode until Julie says `end learn`, `conclude learn`, `exit learn`, `wrap learning`, `finish learning`, or asks to consolidate learning notes.
   - Do not treat generic `summarize`, `done`, `next`, or a topic change as permission to exit learn mode unless it clearly refers to the learning session.

### End of Learn Session

When Julie explicitly wraps learning or asks to consolidate:

1. Read the full `solution/learn_notes.md`.
2. Remove duplicate, low-signal, or non-interview-relevant entries unless explicitly requested.
3. Regroup related Q&A threads by durable concepts, components, tradeoffs, failure modes, and interview phrasing.
4. Merge cleaned takeaways into `solution/deep_dive.md` under relevant sections or a dated `Learning Notes & Refinements` section.
5. Preserve source grounding, examples, edge cases, and strong phrasing.
6. Reset `solution/learn_notes.md` to a short staging inbox or mark merged entries with the date.
7. Summarize what changed in `deep_dive.md` and what remains open.

## Mock Mode Workflow

Use mock mode to simulate a real ML system design interview with step-by-step feedback.

### Setup

1. Resolve `problem_dir`.
2. Read mock context from `input/0_requirements.md`, `input/<problem>.md`, `solution/interview_solutions.md`, `solution/deep_dive.md`, and raw source notes. If only legacy `output/` exists, read it as supporting context.
3. Create a fresh top-level mock directory named `mock_MMDD/`. If one already exists today, create `mock_MMDD_2/`, `mock_MMDD_3/`, etc.
4. Write `mock_instructions.md` with only the candidate-facing prompt, constraints, allowed assumptions, expected deliverables, and how Julie should signal completion. Do not include answer keys, hints, rubrics, or expected sequence.
5. Create `my_solution.md` as Julie's Markdown outline workspace with no solution hints.
6. Create `mock_feedback.md`.
7. State only the interview problem and your role as interviewer.
8. Ask exactly one question. Do not reveal the answer, rubric, expected sequence, or hints.

### During Mock

1. **Ask one question per assistant turn.**
   - Probe one thing at a time: clarification, product objective, architecture, data, modeling, metrics, failure mode, scalability, cross-team contract, or operational maturity.
   - Do not bundle multiple numbered questions.
   - Do not coach, narrate next steps, or provide checklists.

2. **Clarification Questions:**
   - When Julie asks clarifying questions, answer directly with constraints and examples.
   - Pick reasonable assumptions for ambiguous points.
   - Do not volunteer hidden edge cases or gotchas.
   - Record Q&A in `mock_feedback.md`.

3. **Approach Feedback:**
   - When Julie outlines an approach, give concise interviewer feedback.
   - Call out missing requirements, overcomplication, option-listing without decisions, weak crux identification, or too much time on basics.
   - End with at most one targeted next question.
   - Record feedback in `mock_feedback.md`.

4. **Design Work:**
   - Julie writes in `mock_MMDD/my_solution.md`.
   - Do not edit files or write the solution for her.
   - Do not provide hints, reference pointers, or solution direction unless she explicitly asks for clarification or help.
   - Record any hints in `mock_feedback.md`.

5. **Design Review:**
   - When Julie says "done", review `mock_MMDD/my_solution.md`.
   - Review in this order: missing requirements or correctness gaps, crux identification, decision-making, complexity control, deep dives, tradeoffs, failure modes, metrics, evolution plan, L6+ signals, then communication.
   - Provide the smallest conceptual fix for each issue. Do not auto-patch her mock answer.
   - Record findings in `mock_feedback.md`.

6. **Follow-Up:**
   - Ask one scaling, operational, ML correctness, or cross-team follow-up at a time after the current design has been reviewed.

### Closing

When Julie asks to stop or the mock reaches a natural end:

- Give a verdict: `strong pass`, `pass`, `lean pass`, `lean no`, or `no-hire for this round`.
- Include 2-4 focused improvements.
- Identify the weakest concept to review next.
- Record the verdict and improvements in `mock_feedback.md`.
- Summarize misses and weaknesses from the session.
- Convert important misses into candidate-facing next-round prompts in `input/next_round_mock_questions.md`, without answer keys or hidden hints.

### Note-Taking

Record every interview-relevant turn in `mock_feedback.md`:

- Julie's clarification questions and interviewer answers
- Julie's approach and feedback
- Hints given during design
- Design review findings
- Final verdict and improvements
- End-of-session misses, weaknesses, and next-round question seeds

Do not record workflow, environment, IDE, file-conversion, or tooling questions unless explicitly asked.

## Feedback Rubric

Evaluate answers against:

| Dimension | What to Look For |
|-----------|------------------|
| Scoping | Clear requirements, non-goals, scale, constraints, and success metrics. |
| Architecture | Coherent components and data/control flow aligned with requirements. |
| Crux | Identifies the 1-2 hardest risks early and avoids obvious plumbing. |
| Complexity Control | Starts simple and adds complexity only when constraints force it. |
| Decision-Making | Makes clear choices with concise justification instead of only listing options. |
| Depth | Can dive into hard components and explain tradeoffs clearly. |
| ML Correctness | Protects experiment validity, data quality, reproducibility, and metric semantics. |
| Metrics | Covers business, offline ML, online product, guardrail, and infrastructure metrics. |
| Pragmatism | Reuses existing tools where appropriate and avoids speculative complexity. |
| L6+ Signal | Frames ambiguity, owns failure modes, prioritizes by impact, and defines invariants. |
| Production Maturity | Handles drift, training-serving skew, privacy, safety, rollout, rollback, retraining, and maintainability. |
| Communication | Structured, concise, peer-level, responsive to pushback, and avoids over-explaining basics. |

## Tips for Best Results

- **Create mode:** Preserve raw context in `context/`, then generate clean candidate-facing inputs.
- **Solve mode:** Create `solution/interview_solutions.md` first. It is the cheat sheet before a real interview.
- **Companioned learn mode:** Default to read-along Q&A with auto-notes, then consolidate into `solution/deep_dive.md` only at wrap-up.
- **Mock mode:** Treat it like a real interview: outline first, design second, do not over-optimize.
- **Between rounds:** Review `solution/interview_solutions.md`, then run a mock to stress-test under time pressure.

## File Reference

| File | Purpose | Created by | Edited in Learn | Reviewed in Mock |
|------|---------|------------|-----------------|------------------|
| `context/*` | Raw source material | Create/User | No | Reference |
| `input/0_requirements.md` | Normalized prep prompt from raw context | Create/Solve | No | Reference |
| `input/<problem>.md` | Candidate-facing problem statement | Create/Solve | No | Reference |
| `input/next_round_mock_questions.md` | Next mock prompts from prior misses | Mock | No | Reference |
| `solution/interview_solutions.md` | Interview cheat sheet | Solve | Optional reference only | Reference |
| `solution/deep_dive.md` | Design rationale and L6+ concepts | Solve + Learn wrap-up | Wrap-up only | Reference |
| `solution/learn_notes.md` | Raw chronological learning notes | Learn | Yes | No |
| `mock_MMDD/mock_instructions.md` | Candidate-facing mock prompt | Mock | No | Reference |
| `mock_MMDD/my_solution.md` | Julie's mock design attempt | User | No | Yes |
| `mock_MMDD/mock_feedback.md` | Interview feedback, transcript, verdict | Mock | No | Yes |

## Relationship to Other Skills

- Use `coding-interview-companion` for algorithm, coding, or implementation rounds.
- Use `ml-fundamentals-interview` for non-system-design ML theory Q&A and conversational theory mocks.
- Use `ml-daily-quiz` for tracked daily drills and spaced review over a fixed question bank.
- Use this skill for ML system design, research infrastructure, serving, evaluation, ranking, recommendation, and platform design prep.
