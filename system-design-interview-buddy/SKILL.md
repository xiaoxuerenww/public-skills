---
name: system-design-interview-buddy
description: End-to-end ML system design interview prep with solve/learn/mock modes. Use when designing recommendation systems, ranking platforms, experiment pipelines, ML infra, model serving, or research infrastructure. Solve mode builds L6+ answers, learn mode companions understanding with auto-notes, mock mode simulates interviews with step-by-step feedback. Works with input/0_requirements.md and outputs to output/ folder (relative to current directory).
---

# System Design Interview Buddy

**Purpose:** Complete lifecycle support for ML system design interview prep—from requirements analysis through mock interviews.

**Important:** This skill works with files relative to your current directory. All paths (input/, output/) are relative to where you invoke the skill.

## Quick Setup

1. **Create a directory** for your interview prep:
   ```bash
   mkdir my-system-design-prep
   cd my-system-design-prep
   ```

2. **Create input folder and requirements file:**
   ```bash
   mkdir input
   echo "# System Design Interview
   - Problem: Design a recommendation system
   - Scale: 1M users, 100M items
   - Latency: <500ms p99
   - Focus: ML correctness, platform thinking
   " > input/0_requirements.md
   ```

3. **Invoke the skill** from this directory:
   ```
   /system-design-interview-buddy

   "Solve mode: Design a recommendation system..."
   ```

## Directory Structure

All paths are **relative to your current working directory**:

```
current-directory/
  input/
    0_requirements.md          # Raw interview prompt (you create this)
    <problem_name>.md          # Problem statement (created by solve mode)
  output/
    interview_solutions.md     # Interview-ready answer (created by solve mode)
    deep_dive.md               # L6+ concepts & design rationale (created/updated by solve & learn)
    learn_notes.md             # Learning session notes (created by learn mode, merged into deep_dive)
    my_solution.md             # Your answer attempt (reviewed by mock mode)
    mock_feedback.md           # Mock interview feedback (created by mock mode)
```

The skill will:
- **Read from:** `./input/0_requirements.md` (relative to current directory)
- **Write to:** `./input/` and `./output/` (relative to current directory)
- **Create directories** if they don't exist

## Modes

All paths are relative to your current directory:

- **Solve mode:** Read `./input/0_requirements.md`, frame the problem as L6+ MLE, build `./output/interview_solutions.md` (full answer) + `./output/deep_dive.md` (design rationale).
- **Learn mode:** Companion your understanding, auto-take notes in `./output/learn_notes.md`, proactively merge into `./output/deep_dive.md`.
- **Mock mode:** Interview as hiring engineer, review `./output/my_solution.md`, give step-by-step feedback, take notes in `./output/mock_feedback.md`.

---

## Reference Materials

This skill leverages these core frameworks when available locally (relative to current directory):

- `./references/interview-answer-template.md`: answer structure, timing, special question types
- `./references/mlsd-5phase-framework.md`: generic 5-phase ML system design framework
- `./references/interview-communication-guide.md`: expectations, communication criteria
- `./references/quick-concepts-cheatsheet.md`: metrics, latency, serving patterns, tech stack
- `./references/framework-adaptation.md`: adapt framework to research infrastructure prompts

For non-serving research infrastructure (experiment platforms, ML config, sweeps), adapt the 5 phases:

```text
1. Scope and success criteria
2. Inputs / data / config / metadata model
3. Core algorithm or control plane
4. Execution / storage / infrastructure
5. Observability / evaluation / iteration / failure handling
```

---

## Solve Mode Workflow

Use this workflow to analyze a system design prompt and produce interview-ready solutions.

### Phase 1: Requirements Analysis

All file operations are relative to your current directory.

1. Read `./input/0_requirements.md`:
   - Capture prompt, context, scale, users, stakeholders.
   - Identify what the interviewer is testing (scoping, ML judgment, platform thinking, cross-team impact).
   - Note ambiguities and your chosen assumptions.

2. Create `./input/<problem_name>.md`:
   - Clean problem statement (distilled from raw input).
   - Clarifying questions (important to ask upfront).
   - Known constraints (scale, latency, cost, compliance, etc.).
   - Explicit non-goals.
   - Success metrics (product, model, system, guardrails).

3. Brief summary:
   - Frame the problem type (product serving, research infra, ranking, config, etc.).
   - Identify the hard part and where to demonstrate L6+ judgment.
   - List L6+ signals to show: problem framing, ambiguity ownership, ML correctness, platform thinking, operational maturity.

### Phase 2: Solve the System

For each problem (one at a time if multiple):

1. **Requirements & Scoping:**
   - Functional requirements tied to success metrics.
   - Non-functional requirements (latency, cost, reliability, fairness).
   - Explicit non-goals.
   - Scale assumptions and bottleneck analysis.

2. **Architecture & Design:**
   - High-level data flow and control flow.
   - Major components and their contracts.
   - Trade-offs between choices (e.g., real-time vs. batch, centralized vs. distributed).
   - Why this design meets requirements.

3. **Deep Dives (2-3 hardest components):**
   - For each hard component: problem → options → chosen solution → why it wins.
   - Examples: feature engineering, training/serving consistency, experiment tracking, config validation, reproducibility, metric semantics.

4. **Failure Modes & Mitigation:**
   - Silent correctness failures (data staleness, training/serving skew, experiment validity loss).
   - Debugging and monitoring signals.
   - Rollback and retry behavior.
   - Cost controls and graceful degradation.

5. **L6+ Signals to Demonstrate:**
   - **Problem framing**: Convert ambiguous prompt into crisp product goal, explicit non-goals, measurable success criteria.
   - **Technical judgment**: Identify 1-2 risks that matter most; spend depth there instead of touring every component.
   - **ML correctness ownership**: Protect experiment validity, data quality, evaluation semantics, reproducibility.
   - **Platform thinking**: Design APIs, contracts, invariants that let many teams move faster without tribal knowledge.
   - **Operational maturity**: Define debugging paths, incident signals, cost controls, degradation modes.
   - **Pragmatic reuse**: Name commodity tools worth reusing while owning critical boundaries and invariants.
   - **Strategic sequencing**: Separate MVP, hardening, and scale-out phases for credibility under constraints.

### Phase 3: Create Output Documents

1. **Write `./output/interview_solutions.md` (Interview-Ready Answer):**
   - **Opener**: Problem framing and thesis (1 sentence summary of the design).
   - **Clarifying Questions**: 3-5 key questions you'd ask.
   - **Requirements**: Functional, non-functional, non-goals, success metrics.
   - **High-Level Architecture**: ASCII diagram + text. Data flow, control flow, major components.
   - **Deep Dives**: 2-3 sections on hardest components. Problem → Options → Chosen solution + Why.
   - **Trade-Offs & Alternatives**: What you didn't choose and why.
   - **Failure Modes & Debugging**: Silent failures, monitoring, rollback, cost controls.
   - **Wrap-Up**: Restate thesis and why the design meets requirements.
   - **Interview Delivery**: How to present under time pressure; which sections to expand/compress.
   - Write as if explaining to an interviewer: conversational, confident, complete.

2. **Create `./output/deep_dive.md` (Design Rationale & L6+ Concepts):**
   - One section per major component or design decision.
   - **Component Name**: Problem statement, why it's hard.
   - **Alternatives**: What else you considered; trade-offs.
   - **Chosen Solution**: Full explanation + conceptual sketches.
   - **Why It Works**: Invariants, guarantees, correctness arguments.
   - **Pragmatic Notes**: Known tools, when to use them, tribal knowledge to avoid.
   - **Related Concepts**: Link to your study notes if available.
   - Deeper and broader than `interview_solutions.md`; assume you know the basics.
   - Include L6+ thinking: ambiguity ownership, cross-team contracts, migration strategy, operational maturity.

4. **Walk-through:**
   - Summarize the system design: key insight, architecture thesis, hardest trade-off.
   - Mention which output files were created or updated.

---

## Learn Mode Workflow

Use this read-only workflow to companion your learning and auto-document insights.

### Setup

1. Confirm you're in learn mode and state which problem/component you're exploring.
2. Outline what you'll walk through (e.g., "architecture overview", "experiment tracking deep dive", "L6+ framing").

### During Learning

1. **Explanations:**
   - Use plain language first, then technical depth.
   - Keep answers concise; answer the immediate question, then add context.
   - Use one compact example per explanation; avoid stacking examples.
   - Tie design choices back to requirements and L6+ signals.
   - Highlight what you should say in a real interview.

2. **Answer Questions:**
   - When you ask about architecture, trade-offs, L6+ judgment, failure modes, or delivery, answer fully.
   - If there's confusion, clarify the mental model before going deeper.
   - Distinguish "basic correct answer" from "L6+ answer" when relevant.
   - Point out common pitfalls in system design interviewing.

3. **Take Notes (Proactive):**
   - For every interview-relevant question or insight, record it in `./output/learn_notes.md`:
     - **Q:** Your question (concise)
     - **A:** The answer (1-3 sentences)
     - **Mental model:** What to remember or misconception fixed
     - **Interview phrasing:** One sentence you can say aloud
   - Do NOT take notes for workflow/environment/tooling questions.
   - Keep notes chronological and slightly raw.
   - Organize Q&A by parent topic (e.g., "# Experiment Tracking", "## Config Validation") for easy review.

4. **Merge into Deep Dive (Proactive):**
   - As you finish learning a component, merge insights from `./output/learn_notes.md` into `./output/deep_dive.md`:
     - Add a "Learning Notes & Refinements" subsection to the relevant component section.
     - Distill Q&A entries into 1-2 sentence takeaways.
     - Delete merged entries from `./output/learn_notes.md` and update the date.
   - Keep `./output/deep_dive.md` interview-ready and polished.

5. **Interactive & Pause:**
   - After explaining a concept or design decision, ask one check-for-understanding question.
   - Offer to dive deeper into any section.

### End of Learn Session

- Confirm `./output/learn_notes.md` is cleaned up and merged into `./output/deep_dive.md`.
- Summarize what you now understand differently about the system design.

---

## Mock Mode Workflow

Use this workflow to simulate a real system design interview with step-by-step feedback.

### Setup

1. **Frame the interview:**
   - State: "I'm your interviewer for <problem>. Ask clarifying questions, outline your approach, then design."
   - Do not reveal the full intended answer upfront.
   - Keep feedback in interviewer tone: concise, probing, honest.

2. **Create your workspace:**
   - You write your answer in `./output/my_solution.md` (Markdown outline + ASCII diagrams, not full code).
   - I record feedback in `./output/mock_feedback.md`.

### During Mock

1. **Clarification Questions (Your Turn):**
   - When you ask clarifying questions, I answer directly with constraints and examples.
   - I pick reasonable assumptions for ambiguous points.
   - I do NOT volunteer hidden edge cases or gotchas.
   - Record Q&A in `./output/mock_feedback.md`.

2. **Approach Explanation (Your Turn):**
   - When you outline your approach, I give concise feedback:
     - Missing requirements or constraints? Call them out.
     - Overcomplicating? Suggest a simpler direction without full solution.
     - Validate the idea? Move forward.
   - Record approach feedback in `./output/mock_feedback.md`.

3. **Detailed Design (Your Turn):**
   - You write in `./output/my_solution.md`.
   - I do NOT edit files or write the solution for you.
   - If you ask for mid-design help, I give localized hints or reference pointers only.
   - Record hints in `./output/mock_feedback.md`.

4. **Design Review (My Turn):**
   - When you say "done", I review `./output/my_solution.md`:
     - Missing requirements or correctness gaps first.
     - Then missing deep dives, trade-off analysis, failure mode coverage, L6+ signals.
     - Then delivery and communication.
     - Provide smallest conceptual fix for each issue (no auto-patching).
   - Record findings in `./output/mock_feedback.md`.

5. **Closing (My Turn):**
   - Give a verdict: "strong pass / pass / lean pass / lean no / no-hire for this round" (or score if you ask).
   - Include 2-4 focused improvements for the next attempt.
   - Ask one follow-up question an interviewer might ask (optimization, cross-team impact, failure handling, etc.).
   - Record verdict, improvements, and follow-up in `./output/mock_feedback.md`.

### Note-Taking (Proactive)

- Record every turn in `./output/mock_feedback.md`:
  - Your clarification Qs and my answers
  - Your approach + my feedback
  - Hints given during design
  - Design review findings
  - Final verdict and improvements
- This becomes your learning record and self-review guide.

---

## Feedback Rubric

Evaluate answers against:

| Dimension | What to Look For |
|-----------|------------------|
| **Scoping** | Clear requirements, non-goals, scale, constraints, and success metrics. |
| **Architecture** | Coherent components and data/control flow; aligned with requirements. |
| **Depth** | Can dive into hard components and explain trade-offs clearly. |
| **ML Correctness** | Protects experiment validity, data quality, reproducibility, metric semantics. |
| **Pragmatism** | Reuses existing tools where appropriate; avoids speculative complexity. |
| **L6+ Signal** | Frames ambiguity, owns failure modes, prioritizes by impact, defines invariants. |
| **Communication** | Structured, concise, responsive to interviewer pushback. |

---

## Tips for Best Results

- **Solve mode:** Create `./output/interview_solutions.md` first; it's your cheat sheet before a real interview.
- **Learn mode:** Merge notes into `./output/deep_dive.md` immediately; it keeps your reference doc sharp.
- **Mock mode:** Treat it like a real interview: outline first, design second, don't over-optimize.
- **Between rounds:** Review `./output/interview_solutions.md` to warm up, then run a mock to stress-test under time pressure.

---

## File Reference

| File | Purpose | Created by | Edited in Learn | Reviewed in Mock |
|------|---------|-----------|-----------------|------------------|
| `./input/0_requirements.md` | Raw interview prompt | You | No | No |
| `./input/<problem>.md` | Problem statement | Solve | No | No |
| `./output/interview_solutions.md` | Interview cheat sheet | Solve | Yes (optional) | Reference |
| `./output/deep_dive.md` | Design rationale & L6+ concepts | Solve + Learn | Yes (merge notes) | Reference |
| `./output/learn_notes.md` | Raw learning notes | Learn | Yes (merge into deep_dive) | No |
| `./output/my_solution.md` | Your design attempt | You | No | Yes |
| `./output/mock_feedback.md` | Interview feedback | Mock | No | Record |
