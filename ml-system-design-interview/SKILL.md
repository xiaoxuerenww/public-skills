---
name: ml-system-design-interview
description: "End-to-end ML system design interview prep with prep, create, solve, outline-review, companioned learn, and mock modes. Use when designing recommendation systems, ranking platforms, experiment pipelines, ML infra, model serving, evaluation systems, or research infrastructure: locate the current problem directory, preserve ground-truth requirements, generate prep artifacts, synthesize Staff+ solutions, take learning notes, and run dated mock sessions."
---

# ML System Design Interview

**Purpose:** Complete lifecycle support for Staff/Senior Staff ML system design prep: generate prep artifacts from a ground-truth problem prompt, create a problem folder, synthesize L6+ solutions, create blank keyword-outline practice docs, companion learning with notes, and run realistic mock interviews.

**Boundary:** Use this for ML system design, architecture, platform, serving, ranking, recommendation, evaluation, experiment, and research-infrastructure prompts. Do not use it for coding implementation rounds or pure ML theory Q&A.

**Important:** First identify the current problem directory. In prep mode, `<problem_dir>/0_requirements.md` is the ground-truth prompt and must be read but never modified. Legacy `context/`, `input/`, `solution/`, and `mock_MMDD/` paths are also subdirectories of that problem directory, similar to `coding-interview-companion`.

## Problem Directory Resolution

Before reading or writing files, set `problem_dir`:

1. If the user provides a problem directory or file path, use it. If they provide a file inside `context/`, `input/`, `solution/`, `outline_MMDD/`, `mock_MMDD/`, or legacy `output/`, walk upward to the nearest directory that contains the problem's artifact folders or a root-level `0_requirements.md`.
2. Otherwise, if the current directory contains `0_requirements.md`, `context/`, `input/`, `solution/`, `outline_MMDD/`, `mock_MMDD/`, or legacy `output/`, use the current directory.
3. Otherwise, search nearby child directories for `0_requirements.md`, `context/*.md`, `input/0_requirements.md`, `input/*.md`, `solution/deep_dive.md`, legacy `output/deep_dive.md`, or `**/*requirements.md` and choose the directory that matches the current problem context.
4. If multiple directories match and the current problem is ambiguous, ask one concise clarification question.

After resolving `problem_dir`, use:

- `problem_requirements = <problem_dir>/0_requirements.md` for prep mode ground truth. If only legacy `<problem_dir>/input/0_requirements.md` exists, read it as supporting context, but do not rewrite it unless the user explicitly asks outside prep mode.
- `problem_context = <problem_dir>/context`
- `problem_reference = <problem_dir>/reference`
- `problem_input = <problem_dir>/input`
- `problem_solution = <problem_dir>/solution`
- `problem_outline = <problem_dir>/outline_MMDD` where `MMDD` is the current local date, e.g. `outline_0602`
- `problem_mock = <problem_dir>/mock_MMDD` where `MMDD` is the current local date, e.g. `mock_0602`

Create directories as needed for the selected mode. Treat `context/` as raw source material and never overwrite it. Treat `reference/` as curated study material and never overwrite it unless Julie explicitly asks. Treat root-level `0_requirements.md` as immutable ground truth in prep mode. Legacy `output/` is allowed as supporting context for old prep folders, but new non-prep artifacts should use `solution/` and `mock_MMDD/`.

## Directory Structure

All paths are relative to the resolved `problem_dir`:

```text
problem-directory/
  0_requirements.md             # Prep-mode ground truth. Read only, never modify in prep mode.
  1_mock_questions.md           # Candidate-facing mock bank and follow-up probes from requirements
  2_index.md                    # Study index written last after other prep artifacts exist
  3_key_topics.md               # Key topics, cruxes, concepts, and coverage map
  4_deep_dive.md                # Durable Staff+ design rationale and deep dives
  5_interview_ready_solutions.md # Interview-ready Staff+ answer and delivery script
  context/
    ...                         # Raw prompt dumps, requirements, notes, screenshots converted to text, source docs
  reference/
    ...                         # Curated reading materials, PDFs, clipped solutions, source links, examples
  input/
    0_requirements.md           # Legacy normalized prompt from older workflows
    <problem_name>.md           # Legacy candidate-facing problem statement
    next_round_mock_questions.md # Follow-up drills generated from prior mock misses
  solution/
    interview_solutions.md      # Legacy interview-ready L6+ answer
    deep_dive.md                # Legacy design rationale and durable concepts
    learn_notes.md              # Companion learning Q&A notes
  outline_MMDD/
    keyword_outline.md          # Blank template copy for Julie's keyword-only talking points
    outline_feedback.md         # Review of gaps, missing cruxes, and next practice targets
  mock_MMDD/
    mock_instructions.md        # Candidate-facing mock prompt and constraints
    my_solution.md              # Julie's design attempt for this mock
    mock_feedback.md            # Mock transcript, strict feedback, verdict, weakness notes
```

## Modes

- **Prep mode:** Read `<problem_dir>/0_requirements.md` as immutable ground truth and generate numbered root-level prep artifacts in this order: `1_mock_questions.md`, `3_key_topics.md`, `4_deep_dive.md`, `5_interview_ready_solutions.md`, then `2_index.md`. Do not modify `0_requirements.md`.
- **Create mode:** Create or normalize the problem directory from Julie's request, raw notes, or requirement docs. Preserve raw material in `context/`, then write `input/0_requirements.md` and `input/<problem_name>.md`.
- **Solve mode:** Read `context/` and `input/`, normalize requirements if needed, frame the problem as L6+ MLE system design, then write `solution/interview_solutions.md` and `solution/deep_dive.md`.
- **Outline-review mode:** Create a dated blank `outline_MMDD/keyword_outline.md` from `ML_System_Design/1_Frameworks/ML_System_Design_Interview_Template.md` for Julie to fill with keywords only, then review that outline and write `outline_MMDD/outline_feedback.md` with missing coverage, weak cruxes, and concrete next fixes. Do not fill in the solution for her.
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

Use the vault template `ML_System_Design/1_Frameworks/ML_System_Design_Interview_Template.md` for outline-review mode when available. If it is missing, recreate only its section headers as a fallback and note that fallback in `outline_feedback.md`.

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


## Prep Mode Workflow

Use prep mode when Julie asks to `prep`, `set up prep`, `create prep artifacts`, `generate mock questions`, `create key topics`, `create deep dive`, `create interview-ready solutions`, or points to a problem directory that already contains `0_requirements.md`.

### Prep Mode Contract

1. Resolve `problem_dir`.
2. Require `<problem_dir>/0_requirements.md` as the source of truth.
   - Read it first and ground every generated artifact in it.
   - Do not edit, rewrite, rename, move, reformat, or normalize this file.
   - If it is missing, stop and ask Julie to provide or create `0_requirements.md`; do not silently fall back to inferred requirements for prep mode.
3. Generate root-level numbered artifacts, not `solution/` artifacts, in this exact order:
   1. `1_mock_questions.md`
   2. `3_key_topics.md`
   3. `4_deep_dive.md`
   4. `5_interview_ready_solutions.md`
   5. `2_index.md`
4. Existing numbered artifacts may be updated in place, but preserve useful user-written notes unless they directly conflict with `0_requirements.md`.
5. Do not create or update `input/0_requirements.md` in prep mode.
6. Treat `reference/` files as optional curated study material. Read them when present, use them to enrich Staff+ depth and the ranked-materials section in `2_index.md`, but never let them override `0_requirements.md`.
7. Treat legacy `context/`, `input/`, `solution/`, and `output/` files as optional supporting context only. They must not override `0_requirements.md`.

### Prep Mode Reference Handling

When `<problem_dir>/reference/` exists:

1. List all files under `reference/` before generating prep artifacts.
2. Read Markdown, text, and other directly readable local files that are relevant to the prompt. For PDFs or large binary files, extract or inspect only enough to identify title, source, topic coverage, and usefulness unless Julie asks for full PDF-grounded synthesis.
3. Use references as supporting context for `3_key_topics.md`, `4_deep_dive.md`, and `5_interview_ready_solutions.md` when they add concrete interview-tested framing, but preserve `0_requirements.md` as the source of truth.
4. In `2_index.md`, add a `Ranked Reference Materials` section. Rank every useful item in `reference/` by interview ROI, where Rank 1 is the highest-priority read.
5. For each ranked material include:
   - link using Obsidian wiki-link syntax;
   - `Why read`: one concise reason tied to the current problem;
   - `Use for`: mock, key topics, deep dive, spoken answer, or follow-up probes;
   - `Priority`: must-read, skim, optional, or archive;
   - `Time`: realistic reading time;
   - `Key takeaways`: 2-4 bullets, grounded in the material.
6. If a reference is low-quality, duplicative, off-topic, or mostly generic, still list it as optional or archive and explain why briefly.
7. If no `reference/` directory exists or it is empty, write `No local reference materials found yet` in the index rather than inventing references.

### Output 1: `1_mock_questions.md`

Write this first so Julie can start practicing immediately. Include:

- Candidate-facing prompt copied or paraphrased only as allowed by `0_requirements.md`.
- Clarifying questions Julie should ask upfront, with concise expected interviewer answers only if they are grounded in `0_requirements.md`.
- A realistic first-round mock question set grouped by interview phase: scoping, architecture, data, modeling, evaluation, serving, monitoring, failure modes, and evolution.
- Staff+ follow-up probes that test crux identification, decision-making, ML correctness, operational maturity, and cross-team ownership.
- One or more timed mock formats, for example 30-minute and 45-minute versions.
- No hidden full solution before the mock question sections. Keep answer keys light or put them under a clearly marked `Interviewer notes` section.

### Output 3: `3_key_topics.md`

Write this after mock questions. Include:

- Coverage map from `0_requirements.md` to required concepts.
- The 1-2 core cruxes and why they matter.
- Key design decisions Julie must be able to make aloud.
- Metrics taxonomy: business, product, offline ML, online experiment, guardrail, and infrastructure metrics.
- Common weak-answer patterns and how to upgrade them to Staff+ phrasing.
- Glossary or concept notes only where they support interview performance.

### Output 4: `4_deep_dive.md`

Write this after key topics. It is the durable reasoning document. Include:

- One section per major design decision or component.
- For each section: problem, why hard, alternatives, chosen solution, why it works, invariants, failure modes, mitigation, and measurement.
- Deep dives on the true cruxes rather than a broad tour of obvious plumbing.
- Production maturity: drift, leakage, training-serving skew, privacy, safety, cost, capacity, canaries, rollback, retraining, and maintainability.
- Cross-team contracts and migration plan when relevant.

### Output 5: `5_interview_ready_solutions.md`

Write this after deep dive. It is the spoken answer key. Include:

- 30-second thesis.
- Problem framing, clarifying questions, assumptions, goals, non-goals, and success criteria.
- High-level design with ASCII diagram when useful.
- Data, modeling, serving, evaluation, monitoring, failure modes, and evolution plan.
- Staff+ crux and simplifications: what to go deep on and what to intentionally shortcut.
- Interview delivery plan for 30-minute and 45-minute versions.
- Pushback answers for likely interviewer challenges.
- Level calibration: mid-level, senior, Staff, and Principal signals when useful.

### Output 2: `2_index.md`

Write this last so it accurately reflects generated files. Include:

- Source of truth link: `[[0_requirements.md]]`.
- Links to `[[1_mock_questions.md]]`, `[[3_key_topics.md]]`, `[[4_deep_dive.md]]`, and `[[5_interview_ready_solutions.md]]`.
- A `Ranked Reference Materials` section derived from `<problem_dir>/reference/` when present, using wiki-links and ranking each useful material by interview ROI.
- Suggested study order and time budget.
- Checklist of what Julie should rehearse.
- Open questions or assumptions that came from `0_requirements.md`.
- Last updated date from the local `date` command.

### Prep Mode Rubric Pass

Before finalizing, verify:

- `0_requirements.md` was not modified.
- Every numbered artifact is grounded in `0_requirements.md`.
- The output order was followed: 1, 3, 4, 5, then 2.
- The artifacts emphasize cruxes, decisions, and Staff+ production judgment.
- The index links to all generated files and names the source of truth.
- If `reference/` exists, the index includes ranked reference materials with priority, reading time, why-read, use-for, and key takeaways.
- There are no answer-key leaks in candidate-facing mock sections unless clearly marked as interviewer notes.

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


## Outline-Review Mode Workflow

Use outline-review mode when Julie asks for a `blank doc`, `blank template`, `keyword outline`, `talking points only`, `let me fill`, `review my outline`, or asks to practice without a full mock. This is lighter than mock mode: the skill scaffolds a blank workspace, Julie fills key words only, then the skill reviews for completeness and Staff+ signal.

### Setup Blank Keyword Outline

1. Resolve `problem_dir`.
2. Read the best available problem context in this priority order:
   - root-level `0_requirements.md`
   - `1_mock_questions.md` or `input/<problem>.md`
   - `input/0_requirements.md`
   - raw `context/` notes
   - existing `solution/` or numbered prep artifacts only as optional supporting context
3. Create a fresh dated top-level directory named `outline_MMDD/`. If one already exists today, create `outline_MMDD_2/`, `outline_MMDD_3/`, etc.
4. Copy the section structure from `ML_System_Design/1_Frameworks/ML_System_Design_Interview_Template.md` into `outline_MMDD/keyword_outline.md`.
5. Keep the document blank except for:
   - title and source problem link
   - a short instruction: `Fill keywords only, not full sentences. Aim for the talking points you would say aloud.`
   - the template section headings
   - optional HTML comments that say `keywords only` but do not leak hints, answer keys, rubrics, or expected components
6. Create `outline_MMDD/outline_feedback.md` with a stub containing the date, source files, and `Status: waiting for Julie's keyword outline`.
7. Tell Julie only where the blank outline is and that she should fill keywords only. Do not suggest the answer structure beyond the copied template.

### Review Filled Keyword Outline

Use this when Julie says `review`, `done`, `feedback`, `what did I miss`, or points to `outline_MMDD/keyword_outline.md`.

1. Read `outline_MMDD/keyword_outline.md` and the same problem context used in setup.
2. Review Julie's keywords as an interview plan, not polished prose. Do not penalize missing full sentences.
3. Evaluate against the feedback rubric, with special attention to:
   - missing requirements, non-goals, scale, constraints, or success metrics
   - whether the 1-2 cruxes are visible early
   - architecture coverage and data/control flow
   - data, features, modeling, serving, evaluation, monitoring, and failure modes
   - decision-making versus option listing
   - complexity control and production maturity
   - Staff+ signals: invariants, tradeoffs, rollout, rollback, ownership, and cross-team contracts
4. Write `outline_MMDD/outline_feedback.md` with:
   - verdict: `ready for spoken mock`, `needs one repair pass`, or `not ready yet`
   - top missing items, grouped by section
   - strongest signals already present
   - biggest risk if spoken live
   - 3-5 keyword-level additions Julie should add, not a full model answer
   - one focused next drill question if useful
5. In chat, summarize only the verdict, top 3 misses, and next repair pass. Do not rewrite `keyword_outline.md` unless Julie explicitly asks.

### Outline-Review Guardrails

- Preserve Julie's keyword-only practice format. Do not expand her outline into paragraphs by default.
- Do not leak a full answer while she is still practicing. Feedback should identify gaps and suggest keywords or categories, not provide a polished solution.
- If the outline is blank or mostly blank, say so and keep feedback to the minimum missing sections rather than generating an answer.
- Keep this mode separate from mock mode: no interviewer roleplay, no one-question-at-a-time loop, and no final hire/no-hire verdict.

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

- **Prep mode:** Start from root-level `0_requirements.md`, never modify it, then generate `1_mock_questions.md`, `3_key_topics.md`, `4_deep_dive.md`, `5_interview_ready_solutions.md`, and finally `2_index.md`.
- **Create mode:** Preserve raw context in `context/`, then generate clean candidate-facing inputs.
- **Solve mode:** Create `solution/interview_solutions.md` first. It is the cheat sheet before a real interview.
- **Outline-review mode:** Create a blank `outline_MMDD/keyword_outline.md` from `ML_System_Design_Interview_Template`, wait for Julie to fill keywords only, then write gap-focused feedback without rewriting her answer.
- **Companioned learn mode:** Default to read-along Q&A with auto-notes, then consolidate into `solution/deep_dive.md` only at wrap-up.
- **Mock mode:** Treat it like a real interview: outline first, design second, do not over-optimize.
- **Between rounds:** Review `solution/interview_solutions.md`, then run a mock to stress-test under time pressure.

## File Reference

| File | Purpose | Created by | Edited in Learn | Reviewed in Mock |
|------|---------|------------|-----------------|------------------|
| `0_requirements.md` | Prep-mode ground truth | User | No | Reference |
| `1_mock_questions.md` | Mock question bank and probes | Prep | No | Reference |
| `2_index.md` | Prep index and study checklist, written last | Prep | No | Reference |
| `3_key_topics.md` | Coverage map, cruxes, concepts, and Staff+ phrasing | Prep | No | Reference |
| `4_deep_dive.md` | Durable design rationale and Staff+ deep dives | Prep | No | Reference |
| `5_interview_ready_solutions.md` | Spoken Staff+ answer key | Prep | Optional reference only | Reference |
| `context/*` | Raw source material | Create/User | No | Reference |
| `reference/*` | Curated study materials ranked in `2_index.md` during prep | User/Research | Optional reference only | Reference |
| `input/0_requirements.md` | Legacy normalized prep prompt from raw context | Create/Solve | No | Reference |
| `input/<problem>.md` | Legacy candidate-facing problem statement | Create/Solve | No | Reference |
| `input/next_round_mock_questions.md` | Next mock prompts from prior misses | Mock | No | Reference |
| `solution/interview_solutions.md` | Legacy interview cheat sheet | Solve | Optional reference only | Reference |
| `solution/deep_dive.md` | Legacy design rationale and L6+ concepts | Solve + Learn wrap-up | Wrap-up only | Reference |
| `solution/learn_notes.md` | Raw chronological learning notes | Learn | Yes | No |
| `outline_MMDD/keyword_outline.md` | Blank template workspace for keyword-only talking points | Outline-review | No | Reviewed in Outline-review |
| `outline_MMDD/outline_feedback.md` | Gap-focused feedback on Julie's keyword outline | Outline-review | No | Reference |
| `mock_MMDD/mock_instructions.md` | Candidate-facing mock prompt | Mock | No | Reference |
| `mock_MMDD/my_solution.md` | Julie's mock design attempt | User | No | Yes |
| `mock_MMDD/mock_feedback.md` | Interview feedback, transcript, verdict | Mock | No | Yes |

## Relationship to Other Skills

- Use `coding-interview-companion` for algorithm, coding, or implementation rounds.
- Use `ml-fundamentals-interview` for non-system-design ML theory Q&A and conversational theory mocks.
- Use `ml-daily-quiz` for tracked daily drills and spaced review over a fixed question bank.
- Use this skill for ML system design, research infrastructure, serving, evaluation, ranking, recommendation, and platform design prep.
