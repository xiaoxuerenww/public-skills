---
name: project-deep-dive-interview
description: "Prepare, sharpen, and mock project deep-dive interviews for Software Engineer (SDE), including Staff/Senior Staff, roles at frontier AI labs. Use when the user asks to prepare a project deep dive, quiz them to create a skeleton, ask one question per turn, select the right project, convert project notes into Markdown narratives, one-pagers, or explicitly requested Markdown slide decks, build a high-level preparation plan, consolidate raw evidence, index/tidy intake notes, pressure-test technical and execution depth, run a realistic project deep-dive mock, or create feedback and follow-up drills for Anthropic, OpenAI, xAI, Google DeepMind, Meta, Databricks, or similar AI/ML interviews. Outputs are Markdown artifacts; create slides only when explicitly requested."
---

# Project Deep Dive Interview

**Purpose:** Turn your real project material into a credible Staff/Senior Staff Software Engineer (SDE) project deep dive, then mock the interview with frontier-lab-calibrated probing and feedback.

Use this skill for project-focused interviews where the interviewer is testing depth, judgment, ownership, cross-functional influence, engineering rigor, and whether the candidate can defend real tradeoffs under scrutiny.

All outputs must be Markdown. Do not create slides, slide outlines, presentation decks, or PPTX artifacts unless the user explicitly asks for slides or a presentation. If slides are explicitly requested, create a Markdown-native slide document, not PPTX, unless the user explicitly asks for PPTX/Google Slides.

## Workspace Resolution

Resolve `project_dir` before reading or writing files:

1. If the user provides a project directory or file path, use that path. If the path is a file, use its parent directory.
2. Otherwise, if the current directory contains `input/`, `output/`, `context/`, or project notes, use the current directory.
3. Otherwise, search nearby children for project notes such as `*deep*dive*.md`, `*project*.md`, `*context*.md`, `input/0_requirements.md`, or `output/project_deep_dive.md`.
4. If multiple plausible project directories exist, ask one concise clarification question.

Respect explicit source boundaries. If the user excludes a path, do not read it.

Use the current Project_Deep_dive vault layout when it is present:

```text
project_dir/
  requirement/
    INDEX.md                       # Requirement/source index for the interview round
    0_requirements.md              # Interview context, role, company, format, source files
    part_1_past_project_retro.md   # Project-retro prompt and evaluation expectations
    preparation_plan.md            # Optional cross-project prep plan
  projects/
    <project_slug>/
      raw_evidence.md              # Raw source packet preserving source text and local intake
      00_index.md                  # Optional canonical consolidated intake after tidying
      interview_plan.md            # Interview-format plan drafted before quiz/intake mode
      project_deep_dive.md         # Main interview-ready narrative, if requested
      one_pager.md                 # Fast spoken reference, if requested
      deep_dive_presentation.md    # Markdown slide deck only when explicitly requested
      mock_questions.md            # Candidate-facing prompts, hint-light
      mock_feedback.md             # Mock transcript notes and feedback
      drill_notes.md               # Temporary/stabilized drill notes, if retained
      learnings_retro.md           # Learnings, mistakes, retro, and future changes
  projects/llm4rec/                # Source notes for LLM4Rec platform context
  projects/llm_ranker/             # Source notes for LLM ranker context
  projects/AIF/                    # AI Feed / AIF adjacent material
  projects/autoresearch/           # Autoresearch project material
  references/                      # External or technical references
  images/                          # Local images and diagrams
```

When this layout exists, write new project-specific artifacts under `projects/<project_slug>/` and read interview requirements from `requirement/` first. If the older `input/` / `output/` layout exists instead, use it as a fallback. Keep only canonical files after consolidation if the user asks to tidy or delete unneeded docs.

If the user asks for "chat only", do not write files. Otherwise, create or update durable files when the work produces reusable prep material.

## Modes

- **Prepare mode:** Start by creating `input/preparation_plan.md`, then follow the seven-step workflow: project selection, big-picture overview, core deep-dive selection, technical/execution grilling, learnings and retro, mock, and polish.
- **Ask-user-question mode:** Ask targeted clarification questions whenever project details, ownership, metrics, decision rationale, execution sequence, or interviewer context are missing, vague, contradictory, or too important to infer.
- **One-question intake mode:** When the user says `quiz me`, `ask one question per turn`, or wants to create a skeleton from memory, first scan the interview requirements in `requirement/` or legacy `input/0_requirements.md`, draft a short interview plan, create a rough intake skeleton, ask exactly one question per turn, and append each answer into the skeleton before asking the next question.
- **Assumption-review mode:** When the user asks you to assume missing answers, draft plausible answers explicitly marked as assumptions / needs review, then ask the user to verify or correct them before treating them as facts.
- **Evidence/index mode:** When the user asks to `index`, `tidy`, `put raw evidence together`, or `delete unneeded docs`, consolidate intake into `projects/<project_slug>/00_index.md`, preserve raw source text in `projects/<project_slug>/raw_evidence.md`, and keep/delete intermediate docs according to the user's request.
- **Slide mode:** Only when explicitly requested, convert the stabilized intake into a Markdown-native slide deck at `projects/<project_slug>/deep_dive_presentation.md`.
- **Drill mode:** Pressure-test one part of the project, answer questions from source material, and save stabilized gaps or explanations to `projects/<project_slug>/drill_notes.md` when using the current vault layout, or `output/<project_slug>/drill_notes.md` in the legacy layout.
- **Mock mode:** Act as the interviewer. Ask one question at a time, probe deeply, and save feedback to `output/mock_feedback.md` when the mock ends or the user asks for review.
- **Review mode:** Review the user's written or spoken draft against the Staff/Senior Staff rubric and suggest targeted edits.

Infer the mode from the request. If the user says "prepare", "create a one-pager", "make a talk track", or "turn notes into a project deep dive", use prepare mode. If the user says "quiz me", "create skeleton", or "one question per turn", use one-question intake mode. If the user says "assume answers", use assumption-review mode. If they say "index", "tidy", "raw evidence", "regroup", or "delete unneeded docs", use evidence/index mode. If they explicitly ask for "slides", "presentation", or "Markdown deck", use slide mode. If the next useful action is to gather missing details, switch to ask-user-question mode before drafting. If they say "mock", "interview me", or "ask questions", use mock mode. If they say "drill", "pressure test", "go deeper", or asks about one component, use drill mode.

### Two-doc output pattern

All polished project output should split into two companion documents:

1. **Compact presentation doc** (`deep_dive_presentation.md` or `one_pager.md`): sparse speaking anchors. Tables, bullet points, diagrams. No paragraphs. The candidate reads this during prep or glances at it during the interview. Links to the reference doc for backup.
2. **Detailed reference doc** (`presenter_reference.md` or `project_deep_dive.md`): full evidence, extended tradeoff analysis, backup answers to likely follow-ups, verification notes. The candidate studies this beforehand but does not present from it.

This split applies whether the compact doc is a slide deck, a narrative outline, or a one-pager. The principle: keep the presenting artifact lean and move density to the reference doc.

## Source Discovery

Before generating content, read project sources in this order:

1. User-provided files and paths.
2. Current-vault requirements, if present: `requirement/0_requirements.md`, `requirement/part_1_past_project_retro.md`, and `requirement/INDEX.md`.
3. Legacy requirements, if present: `input/0_requirements.md`.
4. The selected project folder under `projects/<project_slug>/`, especially `raw_evidence.md`, `00_index.md`, `interview_plan.md`, `project_deep_dive.md`, `deep_dive_presentation.md`, or notes with `context`, `project`, `deep_dive`, `roadmap`, `design`, `postmortem`, `resume`, or `presentation` in the name.
5. Adjacent source folders when relevant, especially `projects/llm4rec/`, `projects/llm_ranker/`, `projects/AIF/`, `projects/autoresearch/`, and `references/`.
6. Existing outputs only after reading source notes, to avoid reinforcing stale prep.

Capture the source list in `input/0_requirements.md` or the generated output so future work can trace what was used.

If project facts, metrics, dates, launch scope, or ownership claims are unclear, mark them as `needs verification` instead of inventing precision.

## Quiz-to-Skeleton Intake Workflow

Use this workflow when the user wants to be quizzed to create a project skeleton, especially for a project where lived details are not yet in notes.

Before asking the first quiz question:

1. Scan interview requirement docs first:
   - current vault: `requirement/0_requirements.md`, `requirement/part_1_past_project_retro.md`, `requirement/INDEX.md` when present;
   - legacy vault: `input/0_requirements.md` and adjacent requirement files when present;
   - user wording such as `0_requirement` should be interpreted as the local requirement docs, then verified by filesystem scan.
2. Draft or update `projects/<project_slug>/interview_plan.md` with:
   - interview format and timing;
   - interviewer background, if known;
   - expected deliverable, such as 2-page doc, 10-15 slides, or 30-minute project retrospective;
   - evaluation criteria from the requirement docs;
   - recommended project framing;
   - proposed talk-track sections;
   - known source files and facts to verify.
3. Create `projects/<project_slug>/deep_dive_slide_intake_skeleton.md` or `projects/<project_slug>/project_intake_skeleton.md` with:
   - source files already scanned;
   - the interview-plan summary;
   - proposed slide/deep-dive skeleton;
   - missing information per section;
   - an open question queue.
4. Ask exactly one question per turn. Do not batch questions unless the user asks.
5. After each answer, immediately patch the skeleton under `Confirmed answers` and update the relevant slide/section gaps.
6. Keep a running distinction between:
   - user-verified facts;
   - source-derived facts;
   - assumptions pending review;
   - do-not-overclaim boundaries.
7. Prefer questions in this order when building a Staff+ technical retrospective:
   - project framing and product/user experience;
   - launch target, baseline, and missing signals;
   - personal ownership boundary;
   - architecture path;
   - hardest technical decisions;
   - technology rationale and alternatives;
   - experiment/statistical design;
   - evaluation and correctness;
   - rollout/de-risking gates;
   - reliability/operations;
   - impact and caveats;
   - retro and what changed.
8. If the user says "answer that for me" or "assume answers," draft plausible answers in a separate assumption section or file, label them as `assumed draft`, and ask the user to verify before final polish.

For ML/AI project deep dives, the intake skeleton should explicitly ask for:
- product target and denominator;
- baseline failure mode;
- missing content/user/quality/safety signals;
- online and offline architecture;
- training/serving/evaluation constraints;
- experiment randomization and bias handling;
- rollout gates and dashboards;
- reliability incidents and detection gaps.

## Ask-User-Question Mode

Use ask-user-question mode aggressively for clarification and detail gathering. For this skill, project deep-dive quality depends on lived facts, so do not silently infer important details from sparse notes.

Switch into this mode whenever any of these are unclear:

- Which project to use or whether the chosen project is strongest for the target role.
- Your personal ownership boundary versus team contribution.
- Product/user context, launch status, partner teams, timeline, or scope.
- Metrics, baselines, denominators, launch criteria, or result caveats.
- Core technical decision, alternatives considered, rejected options, or why the chosen path won.
- System design, data model, APIs, concurrency, scalability, testing, deployment, monitoring, rollback, or operational details.
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

Calibrate all prep to a Staff/Senior Staff Software Engineer bar:

- **Thesis:** The project should have a crisp one-sentence claim about the hard problem, your role, and why the solution mattered.
- **Scope:** Explain users, product area, system scale (traffic, data volume, latency/availability targets), partner teams, launch or decision impact, and time horizon.
- **Technical depth:** Be ready to defend system design, data models and storage, API/interface contracts, algorithms and data structures, concurrency and consistency, scalability, performance, reliability/fault tolerance, testing and correctness, deployment, and observability.
- **Judgment:** Make tradeoffs explicit: why this approach, why not simpler, why not more ambitious, what changed with evidence.
- **Ownership:** Use "I" for decisions, technical framing, alignment, escalation, and artifacts you personally drove.
- **Leverage:** Highlight design docs, interfaces and platform patterns, test/CI harnesses, decision criteria, partner adoption, and follow-on impact.
- **Frontier-lab lens:** Emphasize careful deployment, operational rigor, reliability and scalability, safety and abuse/misuse resistance, fast iteration under uncertainty, and honest acknowledgment of system limitations. Many frontier-lab SDE projects sit next to ML systems (inference serving, eval/data pipelines, agent tooling); cover that surface where it applies.

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

## Evidence, Index, and Cleanup Workflow

Use this workflow after a long intake session or when the user asks to regroup notes.

### Canonical intake consolidation

Create `projects/<project_slug>/00_index.md` as the canonical consolidated intake. Preserve information, but deduplicate and regroup by topic:

```text
0. Source inventory
1. Interview requirement context
1A. Interview plan
2. Project selection and framing
3. System context and baseline (the existing system the project integrated into)
4. Product context
5. Baseline problem and diagnostic method
6. Role and ownership
7. End-to-end architecture
8. Core strategy (coordinated workstreams)
9. Technology choices, rationale, and timeline
10. Experiment/statistical design
11. Evaluation and correctness
12. Rollout and de-risking (phased: simple → complex)
13. Performance and reliability
14. Results and impact + retrospective
15. Staff+ influence and ownership scope
16. Do-not-overclaim boundaries
17. Remaining gaps / TODOs
18. Follow-up questions
```

Keep original wording where possible. Do not summarize away details. Keep `needs verification` markers.

### Raw evidence packet

When the user asks for raw evidence, create `projects/<project_slug>/raw_evidence.md` with full source text and local intake artifacts grouped by source. Use fenced Markdown blocks and source file paths so claims are traceable. Do not rewrite raw evidence.

### Cleanup

When the user asks to delete unneeded docs after consolidation, keep the canonical docs by default:
- `projects/<project_slug>/00_index.md`, if created
- `projects/<project_slug>/raw_evidence.md`, if created
- any final deliverable the user already requested, such as `projects/<project_slug>/deep_dive_presentation.md`

Delete only intermediate generated files in that project subfolder, such as assumption drafts, temporary skeletons, gap reviews, project briefs, project selections, or preparation plans, after verifying their content is preserved in the canonical files.

## Markdown Slide Mode

Use slide mode only when the user explicitly asks for slides/presentation. Create `projects/<project_slug>/deep_dive_presentation.md` as a Markdown-native deck.

Default slide structure for ML/AI project retrospectives:

- Use 10-15 main slides by default. Prefer 10-12 slides when the material is already concise, and expand up to 15 slides when a slide becomes wordy or combines multiple ideas. The user may override the slide count; respect their preference.
- Keep the presentation deck lightweight. If a slide needs dense evidence, detailed tradeoffs, or backup answers, split that material into a sibling presenter-reference doc such as `projects/<project_slug>/<project_slug>_presenter_reference.md` and link to it from the deck.
- When expanding beyond 10 slides, split by concept rather than adding filler. Good split points: technology ladder vs. technology tradeoffs, novel design problem vs. measurement decisions, experiment design vs. evaluation gates, and launch sequence vs. post-launch hardening.

```text
# <Project Title>
## Slide 1: Thesis
## Slide 2: Role, Ownership, and Outcome
## Slide 3: System Context
## Slide 4: Baseline Failure / Where the Existing Stack Broke
## Slide 5: Product Context and Requirements
## Slide 6: Core Tension / Tradeoff
## Slide 7: Diagnosis
## Slide 8: Core Strategy
## Slide 9: End-to-End Architecture / Pipeline
## Slide 10: Technology Choice and Timeline
## Slide 11: Technology Tradeoffs
## Slide 12: Experiment Design
## Slide 13: Evaluation Scorecard / Launch Gates
## Slide 14: Rollout and De-Risking / Reliability
## Slide 15: Impact, Retrospective, and Staff+ Signal
## Appendix A: Do-Not-Overclaim Boundaries
## Appendix B: Open Verification Items
## Appendix C: Likely Follow-Up Questions
```

Slide design principles:

- **Thesis slide (1):** One-sentence claim and the central project tension. Keep ownership detail minimal if there is a separate role slide.
- **Role / ownership slide (2):** Clarify what the candidate personally drove, what partner teams owned, and the verified outcome metrics.
- **System context slide (3):** Establish the existing system the project integrated into. Use context source folders (e.g., `projects/0_feed_context/`) to ground the system architecture, recommendation funnel, and baseline model. This slide answers "what was already there?" so the audience understands the constraints.
- **Baseline failure and diagnosis slides (4, 7):** Go beyond listing symptoms. Explain the diagnostic method (e.g., offline analysis, feature attribution) that made the problem concrete and actionable.
- **Product requirement vs core tension (5-6):** Separate the legitimate product goal from the contested mechanism or technical tradeoff.
- **Core strategy vs technology choice (8, 10-11):** Differentiate clearly. Strategy answers "what was your plan?" Technology choice answers "why these specific technologies in this order?" Tradeoff slides should include why-not-skip reasoning.
- **Experiment and evaluation (12-13):** Separate experiment variants from metric interpretation and launch gates when the combined slide would be too dense.
- **Rollout / reliability slide (14):** Structure rollout as phased simple-to-complex work, and include reliability if it is a major project learning. If reliability is central, split it into its own slide and compress elsewhere to stay at or below 15 main slides.
- **Impact and retrospective (15):** Combine impact, what you would do differently, and Staff+ signal. Keep details short and move backup evidence to the presenter-reference doc.

### Table patterns for presentation docs

Use these column structures consistently in slides and compact presentation docs:

| Slide type | Recommended columns |
|---|---|
| Tensions | Tension, What goes wrong, Severity |
| Diagnosis | Area, Symptom, Root cause, Impact |
| Strategy | Workstream, Goal, My leverage |
| Technology choices | Stage, Timing, Technology, Purpose |
| Representation phases | Phase, Representation, What it enables, Tradeoff |
| Design decisions | Decision, Challenge, Solution, Tradeoff |
| Launch sequence | Week, System, Change, Size |
| Offline evaluation | Axis, Method |
| Online evaluation | Question, Metrics |
| Role/ownership | Area, What I did |

### Style rules for presentation docs

- Sentence case for all headings ("Core tensions", not "Core Tensions").
- No em dashes or en dashes. Use commas, colons, or periods.
- No decorative bold or italic in table cells. Bold only for the slide heading structure.
- No significance inflation ("pivotal", "crucial", "key"). State the fact.
- Tradeoffs must be explicit and stated in the same breath as the solution.
- "Why not X?" is better than "We chose Y because..." for technology decisions.
- Direct statements over hedged ones. "AIGC was missing the inputs" beats "The system may not have had adequate support for AIGC."
- Tables over bullet lists when comparing options, listing decisions, or showing a sequence.
- One diagram per concept slide max. Do not stack diagrams.

Keep slides interview-ready and concise. Expand abbreviations on first use, for example `Gradient Boosted Decision Tree (GBDT)` and `Deep Neural Network (DNN)`. Cite only verified metrics on main slides; move uncertain details to appendix as `needs verification`.
### Slide Editing Operations

When the user asks to modify an existing slide deck, support these operations:

- **Add slide:** Read context source folders when referenced (e.g., `projects/0_feed_context/`), draft the new slide content, insert it at the right position, and renumber all subsequent slides.
- **Improve slide:** Read adjacent slides to avoid redundancy, then rewrite with richer framing (tables, diagnostic reasoning, gating logic, concrete tradeoffs).
- **Merge slides:** When two slides overlap or are too thin, combine them. Move the stronger content forward and fold the weaker content in. Renumber.
- **Split slide:** When a slide covers two distinct ideas, split and renumber.
- **Move content between slides:** When content is in the wrong slide (e.g., ownership detail in the thesis), relocate it and adjust both slides.
- **Renumber:** After any structural change, scan all `## Slide N:` headers and renumber sequentially. Verify with `grep -n "^## Slide"`.

### Diagram Generation for Slides

When the user asks to draw or visualize a flow, architecture, or pipeline:

1. Check for available Python drawing libraries (matplotlib preferred). If not available in the system Python, create a temporary venv: `python3 -m venv /tmp/drawvenv && /tmp/drawvenv/bin/pip install matplotlib`.
2. Use the `dataviz` skill's palette for colors when available (load `references/palette.md`). Otherwise use a clean, accessible palette.
3. Save diagrams to the vault's `images/` directory with a descriptive filename.
4. Embed in the slide using `![[filename.png]]`, replacing any text-based flow block the diagram replaces.
5. Read the generated image to verify it rendered correctly before moving on.

## Current Vault Artifact Rules

When working in this vault, prefer these artifact locations:

- Interview requirements and prompt docs: `requirement/`.
- Project-specific canonical work: `projects/<project_slug>/`.
- Project source notes: existing sibling folders under `projects/`, especially `llm4rec`, `llm_ranker`, `AIF`, and `autoresearch`.
- External technical references: `references/`.
- Local diagrams/images: `images/`.

Do not create new top-level `input/` or `output/` folders in this vault unless the user explicitly asks or the current directory already uses that legacy layout. For new project slugs, create `projects/<project_slug>/` and keep final files there.

## Prepare Mode

### 1. Project Selection

Create `input/project_selection.md` with a ranked project slate. Keep it rough and content-first.

Start by asking the user for candidate projects if local notes do not already contain a clear slate. Do not choose a primary project from weak evidence.

Evaluate each candidate project on:

- Frontier-lab relevance: distributed systems, backend/infra, developer platforms and tooling, data systems and pipelines, performance and reliability, LLM-product or inference-serving systems, or a research-production bridge.
- Staff+ signal: ambiguity ownership, technical judgment, cross-functional influence, durable leverage, and impact.
- Technical defensibility: enough depth to survive probing on system design, data models, APIs, concurrency, scalability, reliability, testing, deployment, monitoring, and alternatives.
- Recency and authenticity: recent enough to discuss vividly and grounded in your actual role.
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
- How the selected projects connect to Staff/Senior Staff Software Engineer signals.
- 2-3 possible deep-dive themes.
- What each project demonstrates and what it does not.
- A concise transition into the selected core project.

This file should collect the substance you may use for broad opener questions before the interviewer chooses where to go deep. Do not polish the opener yet.

If the career arc or project-to-signal mapping is unclear, ask the user what they want the interviewer to remember before drafting the overview.

### 3. Select Core Deep Dive Project

Create or update `input/project_brief.md` with the chosen core project. Treat this as factual intake, not the final story:

- Interview target: company, role, level, interviewer type, and expected format if known.
- Source files used.
- One-sentence project thesis.
- Product/user context and why the work mattered.
- Your role and ownership boundary.
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

- Product/user goal, requirements, and constraints — and why this system was the right solution.
- Architecture and component boundaries: services, modules, interfaces, and how they interact.
- Data model and storage: schema, access patterns, consistency, indexing, and migrations.
- API/interface contracts, backward compatibility, and versioning.
- Core algorithms, data structures, concurrency model, and consistency/correctness guarantees.
- Scalability and performance: traffic and data volume, bottlenecks, caching, latency and throughput targets.
- Reliability: failure modes, fault tolerance, retries/idempotency, rollback, and incident handling.
- Testing and correctness: unit/integration/load tests, validation strategy, and how regressions are caught.
- Deployment and operations: rollout, CI/CD, configuration, cost, monitoring, and observability.
- Baselines and rejected alternatives (build vs. buy, simpler design, more ambitious design).
- Cross-functional alignment, stakeholder tradeoffs, sequencing, and decision artifacts.
- What you personally decided, influenced, built, or changed.

If the project sits next to ML systems, also probe the relevant surface: inference serving, data/eval pipelines, model/version rollout, and quality monitoring.

When gaps appear, record the strongest current answer plus `needs verification` bullets. Preserve raw technical detail even if it is messy.

### 5. Add Learnings and Retro

Create `output/learnings_retro.md` as content capture:

- What went well.
- What was wrong, uncertain, or changed over time.
- What you learned technically.
- What you learned about execution, influence, or decision-making.
- What you would do differently with another 3-6 months.
- How the project changed later work, standards, platforms, or team strategy.

The retro content should be honest and Staff-level. Avoid generic lessons like "communication is important" unless tied to a concrete change in behavior. Do not over-edit tone until polish.

If the notes do not contain a concrete mistake, pivot, or changed behavior, ask the user for one before drafting the retro.

### 6. Mock

Use mock mode after the plan, project selection, big-picture overview, technical grill, and retro exist. Create or update `input/mock_questions.md` before the mock and `output/mock_feedback.md` after feedback. During the mock, prioritize realistic probing and feedback content over clean transcript formatting.

### 7. Polish

Polish only after the previous steps have produced enough content. Step 7 is where format, narrative order, wording, and final interview usability matter. Create the final Markdown artifacts:

- `projects/<project_slug>/project_deep_dive.md`
- `projects/<project_slug>/one_pager.md`

Polish for:

- A crisp 60-second opener.
- Clear personal ownership.
- 1-2 core technical decisions with evidence and alternatives.
- Honest metrics and caveats.
- Learnings and retro integrated naturally.
- Likely follow-ups answered without over-explaining.
- Frontier-lab readiness: operational rigor, careful deployment, reliability and scalability, safety/user trust, and honesty about limitations.

Before final polish, scan all final claims for unresolved `needs verification` markers and ask the user for any detail that affects credibility.

### Final Deep-Dive Narrative

Create `projects/<project_slug>/project_deep_dive.md` as the durable main artifact when using the current vault layout:

```text
# Project Deep Dive

## 60-Second Opener
## Project Context
## My Role and Ownership
## Problem Framing
## Architecture / System Design
## Deep Dive 1: <hardest decision>
## Deep Dive 2: <second-hardest decision>
## Testing, Correctness, and Validation
## Launch / Operations / Monitoring
## Impact
## Tradeoffs and Alternatives
## Failure Modes
## What I Would Do Differently
## Likely Follow-Ups
```

Keep it interview-ready, not essay-like. Use concise bullets where possible. Make the opener sayable in under one minute.

### Final One-Pager

Create `projects/<project_slug>/one_pager.md` for fast interview reference:

- **Thesis:** one sentence.
- **Signals:** 4-6 Staff+ signals this project demonstrates.
- **Numbers:** verified metrics only; otherwise mark as `verify`.
- **Hard decisions:** 2-3 bullets with option -> choice -> reason.
- **Technical defense:** concise answers to the most likely probes.
- **Follow-up bank:** 8-12 likely questions grouped by product, system design, infra/operations, testing/reliability, and leadership.
- **Do-not-overclaim:** facts or boundaries to avoid overstating.

### Candidate-Facing Mock Questions

Create or update `input/mock_questions.md` with hint-light prompts:

- Start broad: "Walk me through this project."
- Probe role/scope: "What were you personally responsible for?"
- Probe technical crux: "What was the hardest design or system decision?"
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
3. Technical crux: the central system/design decision.
4. Validation: testing strategy, correctness guarantees, how success was measured, launch criteria.
5. Alternatives: simpler baseline, more ambitious approach, build-vs-buy, rejected options.
6. Operations: monitoring, failure modes, rollback, scalability, cost.
7. Staff+ signal: influence, durable artifacts, strategy, mentoring, decision quality.
8. Reflection: what changed, what you would do differently.

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
- **Technical depth:** can defend system design, data, API, and infra choices under probing.
- **Judgment:** tradeoffs are grounded in constraints and evidence.
- **Impact:** results are specific and honestly scoped.
- **Staff+ leverage:** durable influence beyond personal execution.
- **Frontier-lab readiness:** careful deployment, reliability and scalability, safety/user trust, operational rigor, and humility about limitations.

## Review Mode

When reviewing a draft, lead with the highest-risk gaps:

- Missing or weak thesis.
- Unclear personal ownership.
- Too much chronology, not enough decision-making.
- Technical claims that are broad but not defensible.
- Metrics without definitions, baselines, denominators, or caveats.
- Missing alternatives and failure modes.
- Story reads like Senior execution rather than Staff+ leverage.
- Frontier-lab concerns are absent: reliability, scalability, safety/abuse resistance, user trust, deployment risk, or honest system-limitation awareness.

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
- When in one-question intake or mock mode, ask exactly one question at the end of the response.
- When the user asks to preserve or regroup information, prefer canonical Markdown docs over chat-only summaries.
