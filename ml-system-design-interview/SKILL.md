---
name: ml-system-design-interview
description: "End-to-end ML system design interview prep with solve, learn, and mock modes. Use when designing recommendation systems, ranking platforms, experiment pipelines, ML infra, model serving, or research infrastructure: first locate the current problem directory, discover existing *requirements.md context under the problem tree, then use input/ and output/ subdirectories. Solve mode builds L6+ answers, learn mode waits for the user's questions and answers grounded in notes or search results with interview-relevant auto-notes, mock mode simulates a realistic interviewer and reviews the user's design attempt."
---

# ML System Design Interview

**Purpose:** Complete lifecycle support for ML system design interview prep—from requirements analysis through mock interviews.

**Important:** First identify the current problem directory. All `input/` and `output/` paths are subdirectories of that problem directory, not necessarily the shell's current directory.

## Problem Directory Resolution

Before reading or writing files, set `problem_dir`:

1. If the user provides a problem directory or file path, use that directory. If they provide a file inside `input/` or `output/`, use its parent problem directory.
2. Otherwise, if the current directory contains `input/` or `output/`, use the current directory.
3. Otherwise, search nearby child directories for `input/0_requirements.md`, `*requirements.md`, `input/*.md`, or `output/deep_dive.md` and choose the directory that matches the current problem context.
4. If multiple directories match and the current problem is ambiguous, ask one concise clarification question.

After resolving `problem_dir`, use:
- `problem_input = <problem_dir>/input`
- `problem_output = <problem_dir>/output`

Create `problem_input` and `problem_output` if the selected mode needs them and they do not exist.

## Initial Requirements Discovery

Before solve, learn, or mock setup, understand the problem context:

1. Search inside `problem_dir` for requirement docs matching `**/*requirements.md`.
   - Include nested docs such as `<problem_dir>/*/*requirements.md`.
   - Prefer the most specific problem-level requirement doc over broad planning notes.
   - Ignore generated prep outputs unless no other requirements exist.
2. Read the discovered requirement docs first to infer the intended ML system design interview prompt.
3. Create or update `<problem_dir>/input/0_requirements.md` as the normalized starting point for prep.
   - If the discovered requirements are clear, distill them into a concise interview prompt with problem, context, scale, constraints, goals, non-goals, and focus areas.
   - If the discovered requirements are vague, still make the best ML system design interpretation from available context. State assumptions explicitly instead of blocking on clarification.
   - Preserve links or file paths back to the source requirement docs so later work can trace where the prep prompt came from.
4. Treat `<problem_dir>/input/0_requirements.md` as the canonical prep entrypoint after this setup step.

## Quick Setup

1. **Create a directory** for your interview prep:
   ```bash
   mkdir my-ml-system-design-prep
   cd my-ml-system-design-prep
   ```

2. **Add any existing problem context or create an initial requirements file:**
   ```bash
   mkdir input
   echo "# System Design Interview
   - Problem: Design a recommendation system
   - Scale: 1M users, 100M items
   - Latency: <500ms p99
   - Focus: ML correctness, platform thinking
   " > input/0_requirements.md
   ```
   Existing nested docs such as `notes/round1_requirements.md` or `company/system_design_requirements.md` are also valid; the skill will find them and normalize them into `input/0_requirements.md`.

3. **Invoke the skill** from this directory or pass the problem directory explicitly:
   ```
   /ml-system-design-interview

   "Solve mode for ./my-ml-system-design-prep"
   ```

## Directory Structure

All paths are **relative to the resolved problem directory**:

```
problem-directory/
  input/
    0_requirements.md          # Normalized prep prompt (created from discovered requirements)
    <problem_name>.md          # Problem statement (created by solve mode)
  output/
    interview_solutions.md     # Interview-ready answer (created by solve mode)
    deep_dive.md               # L6+ concepts & design rationale (created by solve, updated at learn wrap-up)
    learn_notes.md             # Chronological learning notes (created/updated during learn mode)
    my_solution.md             # Your answer attempt (reviewed by mock mode)
    mock_feedback.md           # Mock interview feedback (created by mock mode)
```

The skill will:
- **Resolve:** `problem_dir` before any file operation
- **Read from:** discovered `<problem_dir>/**/*requirements.md`, then `<problem_dir>/input/0_requirements.md`
- **Write to:** `<problem_dir>/input/` and `<problem_dir>/output/`
- **Create directories** if they don't exist

## Modes

All paths are relative to the resolved `problem_dir`:

- **Solve mode:** Discover source `*requirements.md` docs, normalize them into `<problem_dir>/input/0_requirements.md`, frame the problem as L6+ MLE, build `<problem_dir>/output/interview_solutions.md` and `<problem_dir>/output/deep_dive.md`, then check the answer against the feedback rubric.
- **Learn mode:** Let the user read the material and ask questions; do not explain upfront. Answer only when asked, ground responses in local notes or provided/web search results, record stabilized Q&A in `<problem_dir>/output/learn_notes.md`, and defer `<problem_dir>/output/deep_dive.md` updates until learn-mode wrap-up.
- **Mock mode:** Interview as a realistic hiring engineer, review `<problem_dir>/output/my_solution.md`, ask one question per turn, and record interview-relevant feedback in `<problem_dir>/output/mock_feedback.md`.

---

## Reference Materials

This skill leverages bundled frameworks in the skill directory. Resolve these paths relative to `/Users/xue/.codex/skills/ml-system-design-interview/`, not relative to `problem_dir`:

- `references/interview-answer-template.md`: answer structure, timing, special question types
- `references/mlsd-5phase-framework.md`: generic 5-phase ML system design framework
- `references/interview-communication-guide.md`: expectations, communication criteria
- `references/quick-concepts-cheatsheet.md`: metrics, latency, serving patterns, tech stack
- `references/framework-adaptation.md`: adapt framework to research infrastructure prompts

Read only the relevant reference file(s) for the prompt. For non-serving research infrastructure (experiment platforms, ML config, sweeps), adapt the 5 phases:

```text
1. Scope and success criteria
2. Inputs / data / config / metadata model
3. Core algorithm or control plane
4. Execution / storage / infrastructure
5. Observability / evaluation / iteration / failure handling
```

## Staff/Principal Operating Principles

Use these principles in every solve, learn, and mock interaction:

1. **Communicate like a staff+ peer:**
   - Skip 101-level explanations unless the user asks.
   - Use shared vocabulary and concise framing to maximize signal per sentence.
   - State decisions clearly; do not only list options for the interviewer to choose.

2. **Find the crux early:**
   - Separate straightforward plumbing from the 1-2 highest-risk design problems.
   - Earmark hard parts explicitly, then spend depth where the system can fail or where judgment matters most.
   - Avoid broad component tours when the interviewer is testing technical judgment.

3. **Cut complexity by default:**
   - Start with the simplest design that satisfies functional requirements and stated constraints.
   - Add distributed systems, realtime paths, deep models, LLMs, or extra services only when scale, latency, quality, safety, or reliability forces them.
   - Justify each added complexity against maintainability, cost, and operational burden.

4. **Use ML production judgment:**
   - Decompose systems into product goal, data, retrieval/ranking/modeling, training, serving, evaluation, monitoring, feedback loops, and operations.
   - Tie every modeling choice to infrastructure constraints such as latency, throughput, GPU/CPU cost, caching, data freshness, privacy, and rollback.
   - Prefer hybrid production architectures when appropriate: rules + ML, batch + realtime, retrieval + ranking + reranking, primary model + fallback.

5. **Show evolution and maturity:**
   - Explain how the design can evolve from MVP to hardened production to scale-out.
   - Use component evolution patterns when relevant, e.g. rules -> classical ML -> deep models -> LLM/RAG/agents, or BM25 -> dense retrieval -> hybrid retrieval -> reranking.
   - Include failure modes, safety, drift, training-serving skew, leakage, PII, monitoring, retraining triggers, canary rollout, rollback, and long-term maintainability.

6. **Use a metrics taxonomy:**
   - Business metrics: revenue, retention, conversion, task success, user trust.
   - Offline ML metrics: AUC, NDCG, precision/recall, calibration, hallucination or factuality measures.
   - Online product metrics: CTR, engagement, latency-sensitive success metrics, experiment lift.
   - Guardrail metrics: fairness, safety, abuse, privacy, complaint rate, regressions.
   - Infrastructure metrics: p95/p99 latency, cost per request, throughput, freshness, availability, error rate.

---

## Solve Mode Workflow

Use this workflow to analyze a system design prompt and produce interview-ready solutions.

### Phase 1: Requirements Analysis

All file operations are relative to the resolved `problem_dir`.

1. Discover initial requirements:
   - Search `problem_dir` for `**/*requirements.md`, including nested docs under `<problem_dir>/*/*requirements.md`.
   - Read all relevant requirement docs before generating prep artifacts.
   - If `<problem_dir>/input/0_requirements.md` already exists, compare it with the discovered source docs and update it if it is missing important context.

2. Normalize the prep entrypoint:
   - Create or update `<problem_dir>/input/0_requirements.md`.
   - Capture prompt, context, scale, users, stakeholders, constraints, goals, non-goals, and focus areas.
   - Identify what the interviewer is testing (scoping, ML judgment, platform thinking, cross-team impact).
   - If the source requirements are vague, infer the most likely ML system design interview from available context and state assumptions explicitly.
   - Include a short "Source Requirements" section listing the files used.

3. Create `<problem_dir>/input/<problem_name>.md`:
   - Clean problem statement (distilled from raw input).
   - Clarifying questions (important to ask upfront).
   - Known constraints (scale, latency, cost, compliance, etc.).
   - Explicit non-goals.
   - Success metrics (product, model, system, guardrails).

4. Brief summary:
   - Frame the problem type (product serving, research infra, ranking, config, etc.).
   - Identify the crux: the 1-2 hardest parts where staff-level judgment matters.
   - Name the straightforward parts you will intentionally shortcut.
   - List L6+ signals to show: problem framing, ambiguity ownership, ML correctness, platform thinking, operational maturity.

### Phase 2: Solve the System

For each problem (one at a time if multiple):

1. **Requirements & Scoping:**
   - Functional requirements tied to success metrics.
   - Non-functional requirements (latency, cost, reliability, fairness).
   - Explicit non-goals.
   - Scale assumptions and bottleneck analysis.
   - Metrics taxonomy: business, offline ML, online product, guardrail, and infrastructure metrics.
   - State assumptions and make decisions; avoid leaving major choices as open option lists.

2. **Architecture & Design:**
   - Start with the simplest viable architecture, then add complexity only where constraints require it.
   - High-level data flow and control flow.
   - Major components and their contracts.
   - Trade-offs between choices (e.g., real-time vs. batch, centralized vs. distributed).
   - Why this design meets requirements.
   - Call out hybrid architecture choices where useful: rules + ML, batch + realtime, retrieval + ranking + reranking, primary model + fallback.

3. **Deep Dives (2-3 hardest components):**
   - For each hard component: problem → options → chosen solution → why it wins.
   - Examples: feature engineering, training/serving consistency, experiment tracking, config validation, reproducibility, metric semantics.
   - Show component evolution when relevant: MVP → hardened production → scale-out.
   - Tie model choices to serving, data freshness, cost, and operational constraints.

4. **Failure Modes & Mitigation:**
   - Silent correctness failures (data staleness, training/serving skew, experiment validity loss).
   - Debugging and monitoring signals.
   - Rollback and retry behavior.
   - Cost controls and graceful degradation.
   - Include safety/privacy risks, leakage, drift, hallucination/factuality failures for GenAI systems, canary rollout, retraining triggers, and long-term maintainability.

5. **L6+ Signals to Demonstrate:**
   - **Problem framing**: Convert ambiguous prompt into crisp product goal, explicit non-goals, measurable success criteria.
   - **Technical judgment**: Identify 1-2 risks that matter most; spend depth there instead of touring every component.
   - **ML correctness ownership**: Protect experiment validity, data quality, evaluation semantics, reproducibility.
   - **Platform thinking**: Design APIs, contracts, invariants that let many teams move faster without tribal knowledge.
   - **Operational maturity**: Define debugging paths, incident signals, cost controls, degradation modes.
   - **Pragmatic reuse**: Name commodity tools worth reusing while owning critical boundaries and invariants.
   - **Strategic sequencing**: Separate MVP, hardening, and scale-out phases for credibility under constraints.
   - **Staff communication**: Speak concisely to a staff+ interviewer; skip basics, state decisions, and justify tradeoffs without over-explaining.

### Phase 3: Create Output Documents

1. **Write `<problem_dir>/output/interview_solutions.md` (Interview-Ready Answer):**
   - **Opener**: Problem framing and thesis (1 sentence summary of the design).
   - **Clarifying Questions**: 3-5 key questions you'd ask.
   - **Requirements**: Functional, non-functional, non-goals, success metrics.
   - **High-Level Architecture**: ASCII diagram + text. Data flow, control flow, major components.
   - **Crux & Simplifications**: What is hard, what is straightforward, and where complexity was intentionally avoided.
   - **Deep Dives**: 2-3 sections on hardest components. Problem → Options → Chosen solution + Why.
   - **Trade-Offs & Alternatives**: What you didn't choose and why.
   - **Metrics**: Business, offline ML, online product, guardrail, and infrastructure metrics.
   - **Failure Modes & Debugging**: Silent failures, monitoring, rollback, cost controls.
   - **Evolution Plan**: MVP, hardening, scale-out, and future model/system evolution.
   - **Wrap-Up**: Restate thesis and why the design meets requirements.
   - **Interview Delivery**: How to present under time pressure; which sections to expand/compress.
   - Write as if explaining to an interviewer: conversational, confident, complete.

2. **Create `<problem_dir>/output/deep_dive.md` (Design Rationale & L6+ Concepts):**
   - One section per major component or design decision.
   - **Component Name**: Problem statement, why it's hard.
   - **Alternatives**: What else you considered; trade-offs.
   - **Chosen Solution**: Full explanation + conceptual sketches.
   - **Why It Works**: Invariants, guarantees, correctness arguments.
   - **Pragmatic Notes**: Known tools, when to use them, tribal knowledge to avoid.
   - **Related Concepts**: Link to your study notes if available.
   - Deeper and broader than `interview_solutions.md`; assume you know the basics.
   - Include L6+ thinking: ambiguity ownership, cross-team contracts, migration strategy, operational maturity.

3. **Rubric Pass:**
   - Before finalizing, check `interview_solutions.md` against the Feedback Rubric.
   - Strengthen weak dimensions, especially crux identification, complexity control, ML correctness, L6+ signal, failure modes, and communication.
   - Prefer adding targeted depth to the 1-2 riskiest parts over broad component tours.
   - Remove unnecessary 101 explanations and replace option lists with clear decisions plus concise justification.

4. **Walk-through:**
   - Summarize the system design: key insight, architecture thesis, hardest trade-off.
   - Mention which output files were created or updated.

---

## Learn Mode Workflow

Use this workflow as read-along Q&A support with auto-notes. The user is reading the material independently; do not explain upfront or start teaching unless they ask. Do not edit frozen files in `<problem_dir>/input/`.

### Setup

1. Confirm you're in learn mode and state which problem/component you're exploring.
2. Read the relevant local context silently: `<problem_dir>/input/0_requirements.md`, `<problem_dir>/input/<problem>.md`, `<problem_dir>/output/deep_dive.md`, and any provided notes or search-result packets.
3. Create `<problem_dir>/output/learn_notes.md` if it does not exist.
4. Do not summarize, explain, propose a menu, or ask what the user wants next. Be ready to answer when the user asks.

### During Learning

1. **Read-Along Q&A Loop:**
   - Wait for the user's question; do not proactively explain, continue, or advance topics.
   - If the user asks a question, answer that question directly and stop.
   - Do not ask the user for questions, offer menus, ask check-for-understanding questions, or end with prompts.
   - If the user says "next", continue only if there is an established sequence from prior user questions or material; otherwise stay concise and do not invent a lecture.

2. **Grounding:**
   - Ground answers in local notes first: `input/0_requirements.md`, problem statements, `output/deep_dive.md`, `output/learn_notes.md`, and bundled references.
   - If the user provides web search results, use those results as grounding and distinguish what is sourced from them.
   - If the user explicitly asks to search the web, search and cite sources before answering.
   - If the local notes and provided results do not contain enough evidence, say what is inferred and what is missing.

3. **Explanations:**
   - Use plain language first, then technical depth.
   - Keep answers concise; answer the immediate question, then add context.
   - Use one compact example per explanation; avoid stacking examples.
   - Tie design choices back to requirements and L6+ signals.
   - Highlight what you should say in a real interview.
   - Emphasize staff-level habits: identify the crux, cut unnecessary complexity, make decisions, and connect ML choices to production constraints.
   - When teaching patterns, explain the evolution path from simple baseline to production-grade system instead of presenting only the final architecture.

4. **Answer Questions:**
   - When you ask about architecture, trade-offs, L6+ judgment, failure modes, or delivery, answer fully.
   - If there's confusion, clarify the mental model before going deeper.
   - Distinguish "basic correct answer" from "L6+ answer" when relevant.
   - Point out common pitfalls in system design interviewing.
   - Prefer examples that show tradeoff reasoning across latency, quality, cost, safety, maintainability, and infrastructure constraints.

5. **Auto-Notes (Default):**
   - After each question is stabilized, record it in `<problem_dir>/output/learn_notes.md`.
   - A question is stabilized when the direct answer and any immediate follow-up clarification are complete.
   - Include follow-up questions and refinements under the same note entry so the learning thread stays coherent.
   - For every interview-relevant stabilized question or insight, record:
     - **Q:** Your question (concise)
     - **A:** The answer (1-3 sentences)
     - **Follow-ups:** Immediate follow-up questions/answers or refinements, if any
     - **Mental model:** What to remember or misconception fixed
     - **Interview phrasing:** One sentence you can say aloud
     - **Grounding:** Local note, source file, or web/search-result source used
   - Do NOT take notes for workflow, environment, IDE, file-conversion, or tooling questions unless explicitly asked.
   - Keep notes chronological and slightly raw.
   - Organize Q&A by parent topic (e.g., "# Experiment Tracking", "## Config Validation") for easy review.
   - Do not update `<problem_dir>/output/deep_dive.md` during active learn mode.

6. **Defer Deep-Dive Updates:**
   - During active learn mode, write only to `<problem_dir>/output/learn_notes.md`.
   - Do not merge, rewrite, or polish `<problem_dir>/output/deep_dive.md` until the user exits or wraps up learn mode.
   - Treat `learn_notes.md` as the raw chronological buffer for the session.

7. **Stop After Answering:**
   - After answering, stop cleanly so the user can keep reading.
   - Do not end with prompts such as "Any questions?", "Want to go deeper?", or check-for-understanding questions.

### End of Learn Session

- When the user says they are done, exiting learn mode, wrapping up, or asks to consolidate notes:
  - Analyze `<problem_dir>/output/learn_notes.md` across the whole session.
  - Remove duplicate, low-signal, or non-interview-relevant entries unless explicitly requested.
  - Regroup related Q&A threads by durable concepts, components, tradeoffs, and interview phrasing.
  - Merge the cleaned takeaways into `<problem_dir>/output/deep_dive.md` under relevant sections or a "Learning Notes & Refinements" section.
  - Preserve source grounding when useful.
  - After merging, either clear merged entries from `learn_notes.md` or mark them as merged with date, depending on the existing file style.
- Summarize what changed in `deep_dive.md` and what remains in `learn_notes.md`.

---

## Mock Mode Workflow

Use this workflow to simulate a real system design interview with step-by-step feedback.

### Setup

1. **Frame the interview:**
   - State only the interview problem and your role as interviewer; do not tell the user the sequence of steps to follow unless they explicitly ask about process.
   - Do not reveal the full intended answer upfront.
   - Keep feedback in interviewer tone: concise, probing, honest.
   - Ask exactly one question per assistant turn in mock mode; do not bundle multiple numbered questions or prompts in the same turn.
   - Treat the exchange like a real interview: do not coach, narrate what the candidate should do next, or provide a checklist of tasks.
   - Probe for staff-level judgment: crux identification, decision-making, complexity control, ML + infra tradeoffs, and operational maturity.

2. **Create your workspace:**
   - You write your answer in `<problem_dir>/output/my_solution.md` (Markdown outline + ASCII diagrams, not full code).
   - I record feedback in `<problem_dir>/output/mock_feedback.md`.

### During Mock

1. **Clarification Questions (Your Turn):**
   - When you ask clarifying questions, I answer directly with constraints and examples.
   - I pick reasonable assumptions for ambiguous points.
   - I do NOT volunteer hidden edge cases or gotchas.
   - Ask one clarification question at a time, then wait for the answer before asking the next question.
   - Do not suggest which clarifying questions to ask; wait for the candidate to drive this phase.
   - Record Q&A in `<problem_dir>/output/mock_feedback.md`.

2. **Approach Explanation (Your Turn):**
   - When you outline your approach, I give concise feedback:
     - Missing requirements or constraints? Call them out.
     - Overcomplicating? Ask a probing question that exposes the issue; do not volunteer hints unless the candidate asks for clarification.
     - Only listing options? Ask which one they choose and why.
     - Spending time on basics? Redirect toward the crux or highest-risk tradeoff.
     - Validate the idea? Move forward.
   - End feedback with at most one targeted next question.
   - Record approach feedback in `<problem_dir>/output/mock_feedback.md`.

3. **Detailed Design (Your Turn):**
   - You write in `<problem_dir>/output/my_solution.md`.
   - I do NOT edit files or write the solution for you.
   - Do not provide hints, reference pointers, or solution direction unless the candidate explicitly asks for clarification or help.
   - Record hints in `<problem_dir>/output/mock_feedback.md`.

4. **Design Review (My Turn):**
   - When you say "done", I review `<problem_dir>/output/my_solution.md`:
     - Missing requirements or correctness gaps first.
     - Then missing crux identification, decision-making, complexity control, deep dives, trade-off analysis, failure mode coverage, metrics, evolution plan, and L6+ signals.
     - Then delivery and communication.
     - Provide smallest conceptual fix for each issue (no auto-patching).
   - Record findings in `<problem_dir>/output/mock_feedback.md`.

5. **Follow-up:**
   - If there are multiple design parts, repeat Setup and During Mock steps 1-4 for the next part.
   - If there are no more design parts, ask one scaling, operational, or cross-team follow-up question at a time.

6. **Closing (My Turn):**
   - Give a verdict: "strong pass / pass / lean pass / lean no / no-hire for this round" (or score if you ask).
   - Include 2-4 focused improvements for the next attempt.
   - Ask one follow-up question an interviewer might ask (optimization, cross-team impact, failure handling, etc.).
   - Record verdict, improvements, and follow-up in `<problem_dir>/output/mock_feedback.md`.

### Note-Taking (Proactive)

- Record every interview-relevant turn in `<problem_dir>/output/mock_feedback.md`:
  - Your clarification Qs and my answers
  - Your approach + my feedback
  - Hints given during design
  - Design review findings
  - Final verdict and improvements
- This becomes your learning record and self-review guide.
- Do not record workflow, environment, IDE, file-conversion, or tooling questions unless explicitly asked.

---

## Feedback Rubric

Evaluate answers against:

| Dimension | What to Look For |
|-----------|------------------|
| **Scoping** | Clear requirements, non-goals, scale, constraints, and success metrics. |
| **Architecture** | Coherent components and data/control flow; aligned with requirements. |
| **Crux** | Identifies the 1-2 hardest risks early and avoids spending time on obvious plumbing. |
| **Complexity Control** | Starts simple and adds complexity only when constraints force it. |
| **Decision-Making** | Makes clear choices with concise justification instead of only listing options. |
| **Depth** | Can dive into hard components and explain trade-offs clearly. |
| **ML Correctness** | Protects experiment validity, data quality, reproducibility, metric semantics. |
| **Metrics** | Covers business, offline ML, online product, guardrail, and infrastructure metrics. |
| **Pragmatism** | Reuses existing tools where appropriate; avoids speculative complexity. |
| **L6+ Signal** | Frames ambiguity, owns failure modes, prioritizes by impact, defines invariants. |
| **Production Maturity** | Handles drift, training-serving skew, privacy/safety, rollout, rollback, retraining, and long-term maintainability. |
| **Communication** | Structured, concise, peer-level, responsive to interviewer pushback, and avoids over-explaining basics. |

---

## Tips for Best Results

- **Solve mode:** Create `<problem_dir>/output/interview_solutions.md` first; it's your cheat sheet before a real interview.
- **Learn mode:** Default to read-along Q&A with auto-notes; write stabilized Q&A to `learn_notes.md` during the session and consolidate into `deep_dive.md` only at wrap-up.
- **Mock mode:** Treat it like a real interview: outline first, design second, don't over-optimize.
- **Between rounds:** Review `<problem_dir>/output/interview_solutions.md` to warm up, then run a mock to stress-test under time pressure.

---

## File Reference

| File | Purpose | Created by | Edited in Learn | Reviewed in Mock |
|------|---------|-----------|-----------------|------------------|
| `<problem_dir>/input/0_requirements.md` | Normalized prep prompt from source requirements | Setup/Solve | No | No |
| `<problem_dir>/input/<problem>.md` | Problem statement | Solve | No | No |
| `<problem_dir>/output/interview_solutions.md` | Interview cheat sheet | Solve | Yes (optional) | Reference |
| `<problem_dir>/output/deep_dive.md` | Design rationale & L6+ concepts | Solve + Learn wrap-up | Yes (wrap-up only) | Reference |
| `<problem_dir>/output/learn_notes.md` | Raw chronological learning notes | Learn | Yes (during session) | No |
| `<problem_dir>/output/my_solution.md` | Your design attempt | You | No | Yes |
| `<problem_dir>/output/mock_feedback.md` | Interview feedback | Mock | No | Record |
