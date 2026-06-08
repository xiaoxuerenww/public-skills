---
name: project-deep-dive-interview
description: "Prepare, sharpen, and mock project deep-dive interviews for Staff/Senior Staff MLE roles at frontier AI labs. Use when the user asks to prepare a project deep dive, select the right project, convert project notes into Markdown narratives or one-pagers, build a high-level preparation plan, ask detailed clarification questions, pressure-test technical and execution depth, run a realistic project deep-dive mock, or create feedback and follow-up drills for Anthropic, OpenAI, xAI, Google DeepMind, Meta, or similar frontier lab interviews. Outputs are Markdown artifacts, not slides."
---

# Project Deep Dive Interview

**Purpose:** Turn Julie's real project material into a credible Staff/Senior Staff MLE project deep dive, then mock the interview with frontier-lab-calibrated probing and feedback.

Use this skill for project-focused interviews where the interviewer is testing depth, judgment, ownership, cross-functional influence, ML rigor, and whether the candidate can defend real tradeoffs under scrutiny.

All outputs must be Markdown. Do not create slides, slide outlines, presentation decks, or PPTX artifacts unless the user explicitly overrides this instruction.

## Workspace Resolution

Resolve `project_dir` before reading or writing files:

1. If the user provides a project directory or file path, use that path. If the path is a file, use its parent directory.
2. Otherwise, if the current directory contains `input/`, `output/`, `context/`, or project notes, use the current directory.
3. Otherwise, search nearby children for project notes such as `*deep*dive*.md`, `*project*.md`, `*context*.md`, `input/0_requirements.md`, or `output/project_deep_dive.md`.
4. If multiple plausible project directories exist, ask one concise clarification question.

Respect explicit source boundaries. If the user excludes a path, do not read it.

Use these paths when creating durable prep:

```text
project_dir/
  input/
    0_requirements.md              # Interview context, role, company, format, source files
    preparation_plan.md            # Seven-step high-level prep plan
    project_selection.md           # Candidate projects, ranking, selected direction
    project_brief.md               # Candidate-facing project summary and likely interview frame
    mock_questions.md              # Candidate-facing next-round prompts, hint-light
  output/
    big_picture_overview.md        # Portfolio-level overview and project map
    project_deep_dive.md           # Main interview-ready narrative and technical defense
    one_pager.md                   # Fast spoken reference
    drill_notes.md                 # Weak areas, technical follow-ups, study notes
    learnings_retro.md             # Learnings, mistakes, retro, and future changes
    mock_feedback.md               # Mock transcript notes, scorecard, next drills
    learn_notes.md                 # Temporary chronological notes during learn/drill mode
```

If the user asks for "chat only", do not write files. Otherwise, create or update durable files when the work produces reusable prep material.

## Modes

- **Prepare mode:** Start by creating `input/preparation_plan.md`, then follow the seven-step workflow: project selection, big-picture overview, core deep-dive selection, technical/execution grilling, learnings and retro, mock, and polish.
- **Ask-user-question mode:** Ask targeted clarification questions whenever project details, ownership, metrics, decision rationale, execution sequence, or interviewer context are missing, vague, contradictory, or too important to infer.
- **Drill mode:** Pressure-test one part of the project, answer questions from source material, and save stabilized gaps or explanations to `output/drill_notes.md`.
- **Mock mode:** Act as the interviewer. Ask one question at a time, probe deeply, and save feedback to `output/mock_feedback.md` when the mock ends or the user asks for review.
- **Review mode:** Review the user's written or spoken draft against the Staff/Senior Staff rubric and suggest targeted edits.

Infer the mode from the request. If the user says "prepare", "create a one-pager", "make a talk track", or "turn notes into a project deep dive", use prepare mode. If the next useful action is to gather missing details, switch to ask-user-question mode before drafting. If they say "mock", "interview me", or "ask questions", use mock mode. If they say "drill", "pressure test", "go deeper", or asks about one component, use drill mode.

## Source Discovery

Before generating content, read project sources in this order:

1. User-provided files and paths.
2. `input/0_requirements.md`, if present.
3. Existing project notes in `project_dir`, especially docs with `context`, `project`, `deep_dive`, `roadmap`, `design`, `postmortem`, `resume`, or `presentation` in the name.
4. Existing outputs only after reading source notes, to avoid reinforcing stale prep.

Capture the source list in `input/0_requirements.md` or the generated output so future work can trace what was used.

If project facts, metrics, dates, launch scope, or ownership claims are unclear, mark them as `needs verification` instead of inventing precision.

## Ask-User-Question Mode

Use ask-user-question mode aggressively for clarification and detail gathering. For this skill, project deep-dive quality depends on lived facts, so do not silently infer important details from sparse notes.

Switch into this mode whenever any of these are unclear:

- Which project to use or whether the chosen project is strongest for the target role.
- Julie's personal ownership boundary versus team contribution.
- Product/user context, launch status, partner teams, timeline, or scope.
- Metrics, baselines, denominators, launch criteria, or result caveats.
- Core technical decision, alternatives considered, rejected options, or why the chosen path won.
- Data, labels, model, evaluation, infra, serving, monitoring, rollback, or operational details.
- Cross-functional execution: conflicts, alignment, stakeholder tradeoffs, sequencing, or decision artifacts.
- Learnings, mistakes, retro, or what changed afterward.
- Company/interviewer context that changes what to emphasize.

Ask concise, grouped questions and wait for the user before writing polished artifacts when the missing detail changes the answer. Prefer 3-6 questions per batch. For broad project discovery, use slightly larger batches only when useful.

Question format:

```text
I need a few details before drafting this section:

1. <question>
2. <question>
3. <question>
```

After the user answers, save durable details into the relevant Markdown artifact. In steps 1-6, optimize for content capture, not formatting polish:

- `input/project_selection.md` for candidate-project facts.
- `input/project_brief.md` for selected-project facts and ownership.
- `output/drill_notes.md` for technical and execution clarifications.
- `output/learnings_retro.md` for learnings and retro details.
- `output/project_deep_dive.md` and `output/one_pager.md` only after the details are stable.

If the user asks to proceed despite missing facts, draft with explicit `needs verification` markers rather than pretending certainty.

## Frontier Lab Calibration

Calibrate all prep to a Staff/Senior Staff MLE bar:

- **Thesis:** The project should have a crisp one-sentence claim about the hard problem, Julie's role, and why the solution mattered.
- **Scope:** Explain users, product area, model/system scale, partner teams, launch or decision impact, and time horizon.
- **Technical depth:** Be ready to defend data, modeling, eval, infra, serving, experiment design, monitoring, and failure modes.
- **Judgment:** Make tradeoffs explicit: why this approach, why not simpler, why not more ambitious, what changed with evidence.
- **Ownership:** Use "I" for decisions, technical framing, alignment, escalation, and artifacts Julie personally drove.
- **Leverage:** Highlight design docs, eval harnesses, decision criteria, platform patterns, partner adoption, and follow-on impact.
- **Frontier-lab lens:** Emphasize careful deployment, empirical rigor, safety, user trust, feedback loops, fast iteration under uncertainty, and honest model/system limitations.

Avoid making the project sound like a generic architecture tour. The center should be the 1-2 hard technical decisions and the judgment behind them.

## Seven-Step Preparation Plan

When the user asks to prepare a project deep dive, start with a high-level plan before drafting the final narrative. Create or update `input/preparation_plan.md` in Markdown with exactly these steps unless the user asks for a different sequence:

```text
# Project Deep Dive Preparation Plan

## 1. Project Selection
## 2. Big Picture Overview
## 3. Select Core Deep Dive Project
## 4. Grill Technical and Execution Details
## 5. Add Learnings and Retro
## 6. Mock
## 7. Polish
```

For each step include:

- Objective.
- Source material to read.
- Output Markdown file(s).
- Success criteria.
- Open user questions and facts to verify.

Keep this plan as the orchestration artifact. Update status as work progresses instead of scattering status across many files. If a step needs important missing details, ask the user questions before marking the step complete.

For steps 1-6, focus on content, not format. The goal is to surface facts, choices, evidence, gaps, and user clarifications. Use rough Markdown bullets, raw Q&A, and `needs verification` markers freely. Do not spend effort on wording, final ordering, elegant section titles, or interview polish until step 7.

## Prepare Mode

### 1. Project Selection

Create `input/project_selection.md` with a ranked project slate. Keep it rough and content-first.

Start by asking the user for candidate projects if local notes do not already contain a clear slate. Do not choose a primary project from weak evidence.

Evaluate each candidate project on:

- Frontier-lab relevance: GenAI, LLM systems, recommendation/ranking, evaluation, safety, infra, or research-production bridge.
- Staff+ signal: ambiguity ownership, technical judgment, cross-functional influence, durable leverage, and impact.
- Technical defensibility: enough depth to survive probing on data, model, evaluation, infra, launch, monitoring, and alternatives.
- Recency and authenticity: recent enough to discuss vividly and grounded in Julie's actual role.
- Risk: confidential details, weak metrics, unclear ownership, or overclaiming risk.

Capture:

- Candidate projects.
- Best prompts each project can answer.
- Strengths and risks.
- Ranking.
- Recommended primary and backup project.

### 2. Big Picture Overview

Create `output/big_picture_overview.md` as a content-first portfolio-level map before narrowing into the core project:

- Career/project arc in 5-7 bullets.
- How the selected projects connect to Staff/Senior Staff MLE signals.
- 2-3 possible deep-dive themes.
- What each project demonstrates and what it does not.
- A concise transition into the selected core project.

This file should collect the substance Julie may use for broad opener questions before the interviewer chooses where to go deep. Do not polish the opener yet.

If the career arc or project-to-signal mapping is unclear, ask Julie what she wants the interviewer to remember before drafting the overview.

### 3. Select Core Deep Dive Project

Create or update `input/project_brief.md` with the chosen core project. Treat this as factual intake, not the final story:

- Interview target: company, role, level, interviewer type, and expected format if known.
- Source files used.
- One-sentence project thesis.
- Product/user context and why the work mattered.
- Julie's role and ownership boundary.
- Core technical problem.
- Main design or research decisions.
- Measured results and caveats.
- Likely interviewer concerns.
- Claims that need verification.

If the chosen project is weak for the target company or level, state that clearly and recommend either a backup project or a narrower framing.

Ask clarifying questions before finalizing the brief if ownership, impact, timeline, or the core technical problem is not defensible from the notes.

### 4. Grill Technical and Execution Details

Before polishing the final narrative, grill the core project and write findings to `output/drill_notes.md`.

This step should be question-heavy. Ask detailed follow-up questions until the project can withstand a Staff/Senior Staff technical deep dive.

Cover both technical and execution details:

- Product/user goal and why ML was the right lever.
- Data sources, labels, leakage risks, quality issues, and feedback loops.
- Model, ranking, retrieval, eval, or infra choices.
- Baselines and rejected alternatives.
- Offline and online evaluation, metric definitions, causal validity, launch criteria.
- Serving, latency, cost, reliability, monitoring, rollback, and incident handling.
- Cross-functional alignment, stakeholder tradeoffs, sequencing, and decision artifacts.
- What Julie personally decided, influenced, built, or changed.

When gaps appear, record the strongest current answer plus `needs verification` bullets. Preserve raw technical detail even if it is messy.

### 5. Add Learnings and Retro

Create `output/learnings_retro.md` as content capture:

- What went well.
- What was wrong, uncertain, or changed over time.
- What Julie learned technically.
- What Julie learned about execution, influence, or decision-making.
- What she would do differently with another 3-6 months.
- How the project changed later work, standards, platforms, or team strategy.

The retro content should be honest and Staff-level. Avoid generic lessons like "communication is important" unless tied to a concrete change in behavior. Do not over-edit tone until polish.

If the notes do not contain a concrete mistake, pivot, or changed behavior, ask Julie for one before drafting the retro.

### 6. Mock

Use mock mode after the plan, project selection, big-picture overview, technical grill, and retro exist. Create or update `input/mock_questions.md` before the mock and `output/mock_feedback.md` after feedback. During the mock, prioritize realistic probing and feedback content over clean transcript formatting.

### 7. Polish

Polish only after the previous steps have produced enough content. Step 7 is where format, narrative order, wording, and final interview usability matter. Create the final Markdown artifacts:

- `output/project_deep_dive.md`
- `output/one_pager.md`

Polish for:

- A crisp 30-second opener that loosely follows CARL: Context, Action, Result, Learning.
- Clear personal ownership.
- 1-2 core technical decisions with evidence and alternatives.
- Honest metrics and caveats.
- Learnings and retro integrated naturally.
- Likely follow-ups answered without over-explaining.
- Frontier-lab readiness: eval rigor, careful deployment, safety/user trust, and empirical humility.

Before final polish, scan all final claims for unresolved `needs verification` markers and ask the user for any detail that affects credibility.

### Final Deep-Dive Narrative

Create `output/project_deep_dive.md` as the durable main artifact:

```text
# Project Deep Dive

## 30-Second CARL Opener
## Project Context
## My Role and Ownership
## Problem Framing
## Architecture / ML Approach
## Deep Dive 1: <hardest decision>
## Deep Dive 2: <second-hardest decision>
## Evaluation and Experimentation
## Launch / Operations / Monitoring
## Impact
## Tradeoffs and Alternatives
## Failure Modes
## What I Would Do Differently
## Likely Follow-Ups
```

Keep it interview-ready, not essay-like. Use concise bullets where possible. Make the opener sayable in about 30 seconds.

For `## 30-Second CARL Opener`, use a compact CARL shape:

- **Context:** What the project was and why it mattered.
- **Action:** What Julie personally drove or decided.
- **Result:** What changed, with verified metrics or clear qualitative impact.
- **Learning:** The Staff-level lesson, retro, or durable judgment signal.

Keep this to 4 short spoken bullets or one tight paragraph. Do not force full behavioral-story detail; the goal is to orient the interviewer and invite technical probing.

### Final One-Pager

Create `output/one_pager.md` for fast interview reference:

- **Thesis:** one sentence.
- **30-second CARL opener:** Context, Action, Result, Learning.
- **Signals:** 4-6 Staff+ signals this project demonstrates.
- **Numbers:** verified metrics only; otherwise mark as `verify`.
- **Hard decisions:** 2-3 bullets with option -> choice -> reason.
- **Technical defense:** concise answers to the most likely probes.
- **Follow-up bank:** 8-12 likely questions grouped by product, ML, infra, eval, and leadership.
- **Do-not-overclaim:** facts or boundaries to avoid overstating.

### Candidate-Facing Mock Questions

Create or update `input/mock_questions.md` with hint-light prompts:

- Start broad: "Walk me through this project."
- Probe role/scope: "What were you personally responsible for?"
- Probe technical crux: "What was the hardest ML/system decision?"
- Probe alternatives: "Why not use a simpler approach?"
- Probe evaluation: "How did you know it worked?"
- Probe failure: "What broke or could have gone wrong?"
- Probe judgment: "What would you change with another 6 months?"
- Probe Staff+ influence: "How did this change the team's direction or platform?"

Do not include answer keys in `input/mock_questions.md`. Put answer guidance in `output/project_deep_dive.md` or `output/drill_notes.md`.

## Drill Mode

Use drill mode when the user wants to deepen one weak area or asks a technical follow-up.

1. Read the relevant source files and existing `output/project_deep_dive.md`.
2. Answer only the current question unless the user asks for a full rewrite.
3. When a stable insight emerges, append it to `output/drill_notes.md` with:
   - Date.
   - Topic.
   - Strong answer.
   - Gaps or facts to verify.
   - Follow-up questions to practice.
4. If the user says to wrap up or consolidate, update `output/project_deep_dive.md` and `output/one_pager.md` from `output/drill_notes.md`, then clear or summarize temporary `output/learn_notes.md`.

Keep drill answers technical and direct. Do not turn the session into broad coaching unless the user asks.

## Mock Mode

Act like a realistic frontier-lab project deep-dive interviewer.

Rules:

- Ask one question per turn.
- Start with a broad opener, then follow the user's answer.
- Probe depth instead of giving hints.
- Do not reveal the rubric during the mock unless the user asks to pause.
- Track notes silently enough to produce feedback later.
- If the user asks "review my answer" or "feedback", stop interviewing and give calibrated feedback.

Recommended flow:

1. Opener: "Pick one project and walk me through it."
2. Role and scope: personal ownership, stakeholders, constraints.
3. Technical crux: data/model/system decision.
4. Evaluation: offline/online metrics, causal validity, launch criteria.
5. Alternatives: simpler baseline, more ambitious approach, rejected options.
6. Operations: monitoring, failure modes, rollback, cost.
7. Staff+ signal: influence, durable artifacts, strategy, mentoring, decision quality.
8. Reflection: what changed, what Julie would do differently.

When reviewing, write `output/mock_feedback.md` unless chat-only:

```text
# Project Deep Dive Mock Feedback

## Verdict
## What Worked
## Main Risks
## Staff+ Signal Scorecard
## Technical Depth Gaps
## Communication Edits
## Stronger Answer Patterns
## Next-Round Drills
```

Use this scorecard:

- **Project thesis:** clear, senior enough, and easy to repeat.
- **Ownership:** personal decisions are explicit; team work is contextual.
- **Technical depth:** can defend ML/data/eval/infra choices under probing.
- **Judgment:** tradeoffs are grounded in constraints and evidence.
- **Impact:** results are specific and honestly scoped.
- **Staff+ leverage:** durable influence beyond personal execution.
- **Frontier-lab readiness:** careful deployment, safety/user trust, empirical rigor, and humility about limitations.

## Review Mode

When reviewing a draft, lead with the highest-risk gaps:

- Missing or weak thesis.
- Unclear personal ownership.
- Too much chronology, not enough decision-making.
- Technical claims that are broad but not defensible.
- Metrics without definitions, baselines, denominators, or caveats.
- Missing alternatives and failure modes.
- Story reads like Senior execution rather than Staff+ leverage.
- Frontier-lab concerns are absent: safety, eval rigor, user trust, deployment risk, or model limitation awareness.

Then provide:

- A tighter opener.
- 3-5 targeted edits.
- Likely follow-up questions.
- Optional rewrite only for the sections that need it.

## Answer Style

- Be concise and direct.
- Use bullets for artifacts; use natural spoken phrasing for talk tracks.
- Do not over-polish; credible answers can acknowledge uncertainty.
- Keep project context short. Spend most time on decisions, evidence, and tradeoffs.
- Prefer specific technical nouns over generic impact language.
- Use `needs verification` for uncertain metrics or claims.
- Separate candidate-facing prompts from answer keys.
