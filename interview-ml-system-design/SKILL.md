---
name: ml-system-design-interview
description: "End-to-end ML system design interview prep with prep, solve, practice, companioned learn, and mock modes. Use when designing recommendation systems, ranking platforms, experiment pipelines, ML infra, model serving, evaluation systems, or research infrastructure: locate the current problem directory, preserve ground-truth requirements, generate prep artifacts, synthesize Staff+ solutions, scaffold template-based keyword practice with guided discussion notes, take learning notes, and run dated mock sessions."
---

# ML System Design Interview

**Purpose:** Complete lifecycle support for Staff/Senior Staff ML system design prep: generate prep artifacts from a ground-truth problem prompt, synthesize L6+ solutions, scaffold template-based practice outlines and guided discussion notes, companion learning with notes, and run realistic mock interviews.

**Boundary:** Use this for ML system design, architecture, platform, serving, ranking, recommendation, evaluation, experiment, and research-infrastructure prompts. Do not use it for coding implementation rounds or pure ML theory Q&A.

**Important:** First identify the current problem directory. In prep mode, `<problem_dir>/0_requirements.md` is the ground-truth prompt and must be read but never modified. `context/`, `input/`, `solution/`, `practice_MMDD/`, and `mock_MMDD/` paths are subdirectories of that problem directory.

## Quick Start

**Common workflows:**

1. **Prep from existing requirements:**
   ```
   /interview-ml-system-design prep
   ```
   Requires `<problem_dir>/0_requirements.md` already exists.

2. **Solve a new problem:**
   ```
   /interview-ml-system-design solve
   ```
   Reads from `context/` and `input/`, creates `solution/` artifacts.

3. **Practice with keyword outline:**
   ```
   /interview-ml-system-design practice
   ```
   Creates `practice_MMDD/`, reviews your keyword outline.

4. **Learn while reading:**
   ```
   /interview-ml-system-design companion learn
   ```
   Passive Q&A, auto-saves to `learn_notes.md`.

5. **Run a mock interview:**
   ```
   /interview-ml-system-design mock
   ```
   Creates `mock_MMDD/`, asks one question at a time.

**See Modes section below for details.**

## Problem Directory Resolution

Before reading or writing files, set `problem_dir`:

1. If the user provides a problem directory or file path, use it. If they provide a file inside `context/`, `input/`, `solution/`, `practice_MMDD/`, `mock_MMDD/`, or `output/`, walk upward to the nearest directory that contains the problem's artifact folders or a root-level `0_requirements.md`.
2. Otherwise, if the current directory contains `0_requirements.md`, `context/`, `input/`, `solution/`, `practice_MMDD/`, `mock_MMDD/`, or `output/`, use the current directory.
3. Otherwise, search nearby child directories for `0_requirements.md`, `context/*.md`, `input/0_requirements.md`, `input/*.md`, `solution/deep_dive.md`, `output/deep_dive.md`, or `**/*requirements.md` and choose the directory that matches the current problem context.
4. If multiple directories match and the current problem is ambiguous, ask one concise clarification question.

After resolving `problem_dir`, use:

- `problem_requirements = <problem_dir>/0_requirements.md` for prep mode ground truth. If only `<problem_dir>/input/0_requirements.md` exists, read it as supporting context.
- `problem_context = <problem_dir>/context`
- `problem_reference = <problem_dir>/reference`
- `problem_input = <problem_dir>/input`
- `problem_solution = <problem_dir>/solution`
- `problem_practice = <problem_dir>/practice_MMDD` where `MMDD` is the current local date, e.g. `practice_0602`
- `problem_mock = <problem_dir>/mock_MMDD` where `MMDD` is the current local date, e.g. `mock_0602`

Create directories as needed for the selected mode. Treat `context/` as raw source material and never overwrite it. Treat `reference/` as curated study material and never overwrite it unless the user explicitly asks. Treat root-level `0_requirements.md` as immutable ground truth in prep mode.

## Directory Structure

All paths are relative to the resolved `problem_dir`:

```text
problem-directory/
  0_requirements.md           # Prep-mode ground truth (never modified in prep)
  1_mock_questions.md         # Mock question bank (prep mode)
  2_index.md                  # Study index (prep mode)
  3_key_topics.md             # Quick reference (prep mode)
  4_interview_ready_solutions.md  # Interview answer (prep mode)
  5_deep_dive.md              # Learning depth (prep mode)
  learn_notes.md              # Active learning session notes
  
  context/
    ...                       # Raw prompt dumps, requirements, notes, source docs
  reference/
    ...                       # Curated materials, PDFs, solutions, examples
  input/
    0_requirements.md         # Normalized prompt (solve mode or legacy)
    <problem_name>.md         # Candidate-facing statement (solve mode or legacy)
    next_round_mock_questions.md  # Follow-up drills from mocks
  solution/
    interview_solutions.md    # Interview answer (solve mode)
    deep_dive.md              # Learning depth (solve mode)
  practice_MMDD/
    practice_prompt.md        # Candidate-facing timed prompt
    practice_outline.md       # Keyword talking points template
    practice_feedback.md      # Outline review feedback
    practice_notes.md         # Session notes (full practice only)
  mock_MMDD/
    mock_instructions.md      # Candidate-facing mock prompt
    my_solution.md            # User's design attempt
    mock_feedback.md          # Mock transcript and feedback
```

**Note:** Prep mode uses root-level numbered files (`0-5_*.md`). Solve mode uses `solution/` directory. Both are valid; prep mode is newer.

## Modes

- **Prep mode:** Read `<problem_dir>/0_requirements.md` as immutable ground truth and generate numbered root-level prep artifacts in this order: `1_mock_questions.md`, `3_key_topics.md`, `4_interview_ready_solutions.md`, `5_deep_dive.md`, a final link/style pass on `4_interview_ready_solutions.md`, then `2_index.md`. Do not modify `0_requirements.md`.
- **Solve mode:** Read `context/` and `input/`, normalize requirements if needed, frame the problem as L6+ MLE system design, then write `solution/interview_solutions.md` and `solution/deep_dive.md`.
- **Practice mode:** Create a fresh dated `practice_MMDD/` workspace with a blank keyword outline template (supports both full practice sessions and quick outline-only reviews). Let the user fill keyword talking points, review the outline, optionally guide section-by-section discussion, take raw answer notes with verdicts and misses, and wrap up with next practice or mock targets. Do not provide a model answer or roleplay as interviewer unless asked.
- **Companioned learn mode:** Passive read-along Q&A. Wait for the user's questions, answer directly with concise necessary context, ground responses in local notes or cited sources, and record stabilized Q&A in `<problem_dir>/learn_notes.md`. Do not prompt, quiz, or ask check-for-understanding questions.
- **Mock mode:** Interview as a realistic hiring engineer, create a fresh dated `mock_MMDD/` session, ask one question per turn, review `mock_MMDD/my_solution.md`, and record raw transcript, verdict, misses, and feedback in `mock_MMDD/mock_feedback.md`.

## Note-Taking Standard

For Practice and Mock modes, preserve raw conversation evidence when recording the user's attempts:

- Save the user's answer, outline excerpt, or spoken explanation as a raw quoted
  block whenever possible. Use `Paraphrased answer` only when the raw answer is
  unavailable, very long, or fragmented.
- Save an explicit verdict: `Verdict: ...`.
- Add a `Misses` section before the model fix or stronger answer. Highlight
  exactly what the user missed, got wrong, left vague, or failed to defend.
- Keep misses concrete: missing requirement, missing metric, weak crux,
  unclear decision, overcomplicated design, missing tradeoff, missing failure
  mode, missing rollout/rollback, weak ownership, or communication gap.
- Do not bury misses inside general feedback. In chat and saved notes, show the
  verdict and top misses first.

When the user enters **Companioned learn**, **Practice**, or **Mock** mode, keep the
mode active across turns and take notes proactively on every interview-relevant
user and assistant turn until the user explicitly asks to wrap up, stop, exit, or
switch modes. Do not wait for a separate note-taking request. Do not treat
generic "next", a topic change, or a short follow-up as a wrap-up request.

**Practice mode variants:**
- **Full practice:** Outline → review → guided section discussion → wrap-up
- **Outline-only review:** Outline → review → feedback only (skip guided discussion)

## Document Purpose and Writing Guidelines

**Two document types:**

1. **Interview-ready solutions** (`4_interview_ready_solutions.md`, `solution/interview_solutions.md`):
   - **Purpose:** What you'd actually say in a 30-45 minute interview
   - **Scope:** Delivery-optimized, concise, structured for spoken presentation
   - **Depth:** Staff+ level, but focused on what fits in interview time
   - **Use:** Rehearsal, mock prep, quick review before interviews

2. **Deep dive documents** (`5_deep_dive.md`, `solution/deep_dive.md`):
   - **Purpose:** Staff/Principal-level learning depth for understanding *why* decisions matter
   - **Scope:** Durable reasoning, architectural tradeoffs, production lessons
   - **Depth:** Go deeper than what you'd say in an interview — scalability limits, cross-system dependencies, evolution paths, failure modes
   - **Use:** Learning, teaching, long-term reference, design reviews

**Writing conventions for all documents:**

- **Formatting:** Follow `$doc-formatter` conventions for scannable, visually readable documents:
  - Use **tables** for comparisons, alternatives, and tradeoffs (not bullet lists)
  - Add **TL;DR** summaries at major sections
  - Use **bold** for key terms, decisions, and invariants
  - Structure **tension** as comparison tables (not prose)
  - Keep **invariants** and **failure modes** as structured lists with bold labels
- **Abbreviations:** Expand on first use in each document (e.g., "Machine Learning (ML)", "Key-Value (KV) cache", "Natural Language Processing (NLP)", "Training-Serving Skew (TSS)", "Service Level Objective (SLO)"), then use the short form consistently afterward.
- **Clarity:** Use precise technical terms, avoid vague phrases
- **Examples:** Include concrete production examples when available from gathered materials

---

## Reference Materials

Resolve these paths relative to `~/.codex/skills/ml-system-design-interview/`, not `problem_dir`:

- `references/interview-answer-template.md`: answer structure, timing, special question types
- `references/mlsd-5phase-framework.md`: generic 5-phase ML system design framework
- `references/interview-communication-guide.md`: expectations, communication criteria
- `references/quick-concepts-cheatsheet.md`: metrics, latency, serving patterns, tech stack
- `references/framework-adaptation.md`: adapt framework to research infrastructure prompts

For outline-review mode, use the generic interview-ready solution outline template below, not a problem-specific file and not the generic ML system design framework template. Copy headings only and remove all answer content, diagrams, hints, Staff-level talking points, and deep-dive links.

Generic keyword-outline heading structure:

```text
30-second thesis
Opener
Problem framing
  Clarifying questions
  Functional requirements
  Non-functional requirements
  Goals
  Non-goals
  Success criteria
High-level design
  High-level architecture diagram
  Component responsibilities
  Data flow
Data and features
  Input data and signals
  Feature construction
  Freshness and cold start
Modeling
  Baseline
  Production model
  Why this model first?
  Model output
  Training setup
Decision or serving engine
  Thresholding, ranking, or policy logic
Evaluation and monitoring
  Offline
  Online
  Drift
Staff+ crux and simplifications
  Cruxes to go deep on
  Things to shortcut
Trade-offs and alternatives
Failure modes and debugging
Evolution plan
  MVP
  Production hardening
  Scale-out
30-minute delivery plan
45-minute delivery plan
Interview delivery tips
Likely pushback answers
  Pushback 1: model choice
  Pushback 2: missing or stale data
  Pushback 3: false positives vs false negatives
  Pushback 4: latency, cost, or scale
  Pushback 5: labels and ground truth
  Pushback 6: granularity of prediction or action
  Pushback 7: drift and maintenance
Level calibration
Wrap-up
```

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

Use prep mode when the user asks to `prep`, `set up prep`, `create prep artifacts`, `generate mock questions`, `create key topics`, `create deep dive`, `create interview-ready solutions`, or points to a problem directory that already contains `0_requirements.md`.

### Prep Mode Contract

1. Resolve `problem_dir`.
2. Require `<problem_dir>/0_requirements.md` as the source of truth.
   - Read it first and ground every generated artifact in it.
   - Do not edit, rewrite, rename, move, reformat, or normalize this file.
   - If it is missing, stop and ask the user to provide or create `0_requirements.md`; do not silently fall back to inferred requirements for prep mode.
3. **Material gathering (before generating artifacts):**
   - Invoke `$system-design-material-finder` to find relevant interview preparation materials (example solutions, mock questions, company interview guides, domain-specific patterns).
   - Save found materials to `<problem_dir>/reference/` with descriptive filenames.
   - Use these materials plus existing `reference/` and `context/` files to enrich prep artifacts.
   - If material finder returns no results or fails, continue with prep using only `0_requirements.md` and existing `reference/` files.
   - Log what was searched for in `2_index.md` under "Material search attempted" for future reference.
4. Generate root-level numbered artifacts, not `solution/` artifacts, in this exact order:
   1. `1_mock_questions.md`
   2. `3_key_topics.md`
   3. `4_interview_ready_solutions.md`
   4. `5_deep_dive.md`
   5. final link/style pass on `4_interview_ready_solutions.md`
   6. `2_index.md`
5. Existing numbered artifacts may be updated in place, but preserve useful user-written notes unless they directly conflict with `0_requirements.md`.
6. Do not create or update `input/0_requirements.md` in prep mode.
7. Treat `reference/` files as optional curated study material. Read them when present, use them to enrich Staff+ depth and the ranked-materials section in `2_index.md`, but never let them override `0_requirements.md`.
8. Treat `context/`, `input/`, `solution/`, and `output/` files as optional supporting context only. They must not override `0_requirements.md`.

### Prep Mode Reference Handling

When `<problem_dir>/reference/` exists:

1. List all files under `reference/` before generating prep artifacts.
2. Read relevant Markdown and text files. For PDFs, extract title and topic only unless user asks for full synthesis.
3. Use references to enrich `3_key_topics.md`, `4_interview_ready_solutions.md`, and `5_deep_dive.md`, but preserve `0_requirements.md` as source of truth.
4. In `2_index.md`, add a `Reference Materials` section ranking items by interview ROI:
   - **Must-read:** Critical for this problem
   - **Recommended:** Helpful but not critical
   - **Optional:** Background or alternative approaches
   
   For each item include: link, why read (one sentence), use for (mock/deep dive/etc), reading time, 2-3 key takeaways.

5. If no `reference/` exists, write "No reference materials found" in index.

### Output 1: `1_mock_questions.md`

Write this first so the user can start practicing immediately. Include:

- Candidate-facing prompt copied or paraphrased only as allowed by `0_requirements.md`.
- Clarifying questions the user should ask upfront, with concise expected interviewer answers only if they are grounded in `0_requirements.md`.
- A realistic first-round mock question set grouped by interview phase: scoping, architecture, data, modeling, evaluation, serving, monitoring, failure modes, and evolution.
- Staff+ follow-up probes that test crux identification, decision-making, ML correctness, operational maturity, and cross-team ownership.
- One or more timed mock formats, for example 30-minute and 45-minute versions.
- No hidden full solution before the mock question sections. Keep answer keys light or put them under a clearly marked `Interviewer notes` section.

### Output 3: `3_key_topics.md`

Write this after mock questions as a concise fast-review sheet, not a deep-dive document. Keep it short, scannable, and interview-delivery oriented.

Include:

- A compact coverage map from `0_requirements.md` to the minimum concepts the user must mention.
- A `Talking points` section with keyword-level bullets the user can rehearse aloud.
- A `Concise answers` section with 1-3 sentence answers to the most likely interviewer questions.
- The 1-2 core cruxes and why they matter, stated in plain interview language.
- Key design decisions the user must be able to make aloud, each with a one-sentence justification.
- Metrics taxonomy as a compact checklist, not a long explanation.
- Common weak-answer patterns and one-line Staff+ upgrades.
- Glossary or concept notes only if they are essential for interview performance.

Avoid:

- Long paragraphs, full solution scripts, exhaustive component tours, or detailed derivations.
- Content that belongs in `4_interview_ready_solutions.md` or `5_deep_dive.md`.

### Output 4: `4_interview_ready_solutions.md`

**Purpose:** Interview-ready spoken answer — what you'd actually say in a 30-45 minute interview. Optimized for delivery, not learning depth.

**Formatting:** Use `$doc-formatter` conventions for scannable structure: tables for comparisons/alternatives, bold for key terms, TL;DR summaries, clear visual hierarchy.

Write this after key topics. It is the spoken answer key and should stay lighter than `5_deep_dive.md`. Include:

- 30-second thesis.
- Problem framing, clarifying questions, assumptions, goals, non-goals, and success criteria.
- High-level design with ASCII diagram when useful.
- Data, modeling, serving, evaluation, monitoring, failure modes, and evolution plan.
- Staff+ crux and simplifications: what to go deep on and what to intentionally shortcut.
- Inline `Staff-level talking point:` lines inside the relevant sections. Do not create a standalone `## Staff-Level Thesis` or `## Staff-Level Talking Points` block.
- Obsidian section links from each major section to the matching `5_deep_dive.md` section, for example `Deep dive: [[5_deep_dive#Calibration And Thresholding|calibration and thresholding]]`.
- Interview delivery plan for 30-minute and 45-minute versions.
- Pushback answers for likely interviewer challenges.
- Level calibration: mid-level, senior, Staff, and Principal signals when useful.

**Abbreviation handling:** Expand abbreviations on first use in the document (e.g., "Machine Learning (ML)", "Key-Value (KV) cache", "Natural Language Processing (NLP)"), then use the short form consistently afterward.

After `5_deep_dive.md` exists, make a final pass over `4_interview_ready_solutions.md` to ensure every major section has the right deep-dive link and that Staff-level talking points are inline with the section they support.

### Output 5: `5_deep_dive.md`

**Purpose:** Staff/Principal-level learning depth — durable reasoning document for understanding *why* decisions matter, not for interview delivery. Go deeper than what you'd say in an interview.

**Formatting:** Use `$doc-formatter` conventions extensively: tables for tradeoffs/alternatives, tension tables, TL;DR summaries per section, invariants/failure modes as structured lists, visual hierarchy with bold/italic.

Write this after the interview-ready solution. It is the durable reasoning document. Include:

- One section per major design decision or component.
- For each section: problem, why hard, alternatives, chosen solution, why it works, invariants, failure modes, mitigation, and measurement.
- Deep dives on the true cruxes rather than a broad tour of obvious plumbing.
- Production maturity: drift, leakage, training-serving skew, privacy, safety, cost, capacity, canaries, rollback, retraining, and maintainability.
- Staff/Principal-level depth: architectural tradeoffs, scalability limits, cross-system dependencies, evolution paths, lessons from production failures.
- Cross-team contracts and migration plan when relevant.
- Stable, descriptive section headings that can be linked from `4_interview_ready_solutions.md`; avoid renaming them after adding interview-ready links unless you also repair the links.

**Abbreviation handling:** Expand abbreviations on first use in the document (e.g., "Training-Serving Skew (TSS)", "Latency Service Level Objective (SLO)", "Online Analytical Processing (OLAP)"), then use the short form consistently afterward.

### Output 2: `2_index.md`

Write this last so it accurately reflects generated files. Include:

- Source of truth link: `[[0_requirements.md]]`.
- Links to `[[1_mock_questions.md]]`, `[[3_key_topics.md]]`, `[[4_interview_ready_solutions.md]]`, and `[[5_deep_dive.md]]`.
- A `Ranked Reference Materials` section derived from `<problem_dir>/reference/` when present, using wiki-links and ranking each useful material by interview ROI.
- Suggested study order and time budget.
- Checklist of what the user should rehearse.
- Open questions or assumptions that came from `0_requirements.md`.
- Last updated date from the local `date` command.

### Prep Mode Rubric Pass

Before finalizing, verify:

- `0_requirements.md` was not modified.
- Every numbered artifact is grounded in `0_requirements.md`.
- The output order was followed: 1, 3, 4, 5, final link/style pass on 4, then 2.
- `4_interview_ready_solutions.md` links major sections to matching `5_deep_dive.md` headings and has no broken renamed-section links.
- Staff-level talking points in `4_interview_ready_solutions.md` are inline inside relevant sections, not isolated in a standalone Staff-level section.
- The artifacts emphasize cruxes, decisions, and Staff+ production judgment.
- The index links to all generated files and names the source of truth.
- If `reference/` exists, the index includes ranked reference materials with priority, reading time, why-read, use-for, and key takeaways.
- There are no answer-key leaks in candidate-facing mock sections unless clearly marked as interviewer notes.

## Solve Mode Workflow

Use solve mode to analyze a system design prompt and produce interview-ready solution artifacts.

### Phase 1: Requirements Analysis

1. Resolve `problem_dir`.
2. Read raw context from `context/`, generated prompts from `input/`, and any discovered `**/*requirements.md` under `problem_dir`.
3. Prefer source prompts and raw requirements over derived solution artifacts. Read `output/` as supporting context if needed.
4. Create or update `input/0_requirements.md` if it is missing important context.
5. **Material gathering:**
   - Invoke `$system-design-material-finder` to find solutions, tutorials, tech blogs, case studies, and production examples for this specific system design problem.
   - Save found materials to `<problem_dir>/reference/` with descriptive filenames.
   - Use these materials to ground the solution in real-world patterns and production experience.
   - If material finder returns no results or fails, continue with solve using only `context/` and `input/` files.
   - Note in `solution/interview_solutions.md` that solution is based on requirements only, not production examples.
6. Identify:
   - Problem type: product serving, research infra, ranking, config, evaluation, model serving, monitoring, etc.
   - Product objective, ML objective, users, scale, latency, cost, privacy, safety, and compliance constraints.
   - The crux: 1-2 hardest parts where staff-level judgment matters.
   - Straightforward parts to intentionally shortcut.
   - L6+ signals to demonstrate: ambiguity ownership, ML correctness, platform thinking, operational maturity, and strategic sequencing.

### Phase 2: Solve the System

Review gathered materials from `reference/` to understand production patterns, common pitfalls, and industry best practices for this problem type. Ground the solution in real-world examples when available.

For each problem, structure the answer around:

1. **Problem Framing:** Product surface, clarifying questions, assumptions, business objective, ML objective, non-goals, and success criteria.
2. **High-Level Design:** Main components, data flow, control flow, stage contracts, latency and cost budgets, precompute versus online paths, caching, fallbacks, and degradation.
3. **Data and Features:** Signal quality, freshness, explicit and implicit feedback, context, item/content/user features, leakage risk, bias, and training-serving consistency.
4. **Modeling:** Baselines, production model choice, retrieval or ranking stages, objective/loss when it matters, calibration, multitask or multi-objective composition, and model evolution.
5. **Inference and Evaluation:** Serving path, model serving, batching, hardware, caching, offline metrics, online tests, guardrails, experiment validity, and infra health.
6. **Deep Dives:** Pick 2-3 real cruxes. For each: problem, why it matters, options, chosen solution, why it wins, failure mode, and measurement. Cite production examples from gathered materials when relevant.
7. **Failure Modes and Mitigation:** Data staleness, training-serving skew, leakage, drift, exposure bias, feedback loops, policy or safety regressions, cost blowups, canaries, rollback, and retraining triggers.
8. **Evolution Plan:** MVP, hardening, scale-out, and future model/system evolution.

### Phase 3: Create Solution Documents

1. Write `solution/interview_solutions.md` as the **interview-ready answer** (what you'd say in 30-45 min):
   - **Formatting:** Use `$doc-formatter` conventions: tables for comparisons/alternatives, bold for key terms, TL;DR summaries, clear visual hierarchy.
   - Opener
   - Understanding the Problem
   - Problem Framing
   - High-Level Design with ASCII diagram when useful
   - Data and Features
   - Modeling
   - Inference and Evaluation
   - Crux and Simplifications
   - Deep Dives
   - Trade-Offs and Alternatives (use comparison tables)
   - Failure Modes and Debugging
   - Evolution Plan
   - Level Calibration
   - Wrap-Up
   - Interview Delivery
   - **Abbreviation handling:** Expand abbreviations on first use (e.g., "Machine Learning (ML)", "Natural Language Processing (NLP)"), then use short form consistently.

2. Write `solution/deep_dive.md` as the **Staff/Principal-level learning depth document** (for understanding *why*, not for interview delivery):
   - **Formatting:** Use `$doc-formatter` conventions extensively: tables for tradeoffs/alternatives, tension tables, TL;DR per section, invariants/failure modes as structured lists.
   - One section per major component or design decision.
   - For each section: problem, why hard (use tension table), alternatives (use comparison table), chosen solution, why it works, invariants, pragmatic notes, and related concepts.
   - Include L6+ thinking: ambiguity ownership, cross-team contracts, migration strategy, ML correctness, operational maturity.
   - Go deeper than interview-ready: architectural tradeoffs, scalability limits, cross-system dependencies, evolution paths, lessons from production failures.
   - **Abbreviation handling:** Expand abbreviations on first use (e.g., "Training-Serving Skew (TSS)", "Latency Service Level Objective (SLO)"), then use short form consistently.

3. Run a rubric pass before finalizing:
   - **For interview_solutions.md:** Strengthen crux identification, complexity control, decision-making, ML correctness, metrics, failure modes, L6+ signal, and communication. Optimize for delivery clarity.
   - **For deep_dive.md:** Add Staff/Principal-level depth on why decisions matter, production patterns, failure modes, and evolution paths. Optimize for learning depth.
   - **Formatting validation:** Ensure both documents follow `$doc-formatter` conventions:
     - Use tables for all comparisons and alternatives (not bullet lists)
     - Add TL;DR summaries at major sections
     - Use bold for key terms and decisions
     - Structure tradeoffs as tension tables
     - Keep invariants and failure modes as structured lists
   - Prefer targeted depth on the riskiest parts over broad component tours.
   - Remove unnecessary 101 explanations and replace option lists with decisions plus concise justification.

4. Walk through the created artifacts:
   - Key architecture thesis.
   - Hardest tradeoff.
   - Files created or updated.

## Practice Mode Workflow

Use practice mode when the user asks to `practice`, `create practice`, `timed practice`, `independent attempt`, `keyword outline`, `blank template`, `talking points only`, `do a dry run`, `review my practice`, `review my outline`, `guide me section by section`, or points to `practice_MMDD/practice_outline.md`. This mode supports both full practice sessions with guided discussion and quick outline-only reviews.

Practice mode has two variants:

**Full practice (5 phases):**
0. Create a practice doc from `~/Documents/work/0_databricks/Templates/ml_system_design_template.md`.
1. Let the user outline keyword talking points.
2. Review the outline and give feedback.
3. Guide section-by-section discussion, allowing questions and deep dives on weak topics.
4. Proactively take notes throughout the practice conversation, especially raw answers, verdicts, and misses.
5. Wrap up with notes for the next practice or mock.

**Outline-only review (phases 0-2 only):**
- User asks for outline review only, quick feedback, or to skip guided discussion
- Skip phase 3 (guided discussion) and go directly to wrap-up after outline review
- Lighter weight, faster turnaround

Once Practice mode starts, keep appending to `practice_MMDD/practice_notes.md`
on every interview-relevant turn until the user explicitly asks to stop, wrap,
finish practice, move to mock, or switch modes.

### Phase 0: Create Practice Doc

1. Resolve `problem_dir`.
2. Read the best available problem context in this priority order:
   - root-level `0_requirements.md`
   - `1_mock_questions.md`
   - `input/<problem>.md`
   - `input/0_requirements.md`
   - raw `context/` notes
   - existing answer artifacts only to avoid contradicting known constraints, not to leak hints into the prompt
3. Create a fresh dated top-level directory named `practice_MMDD/`. If one already exists today, create `practice_MMDD_2/`, `practice_MMDD_3/`, etc.
4. Copy `~/Documents/work/0_databricks/Templates/ml_system_design_template.md` into `practice_MMDD/practice_outline.md`.
   - Preserve the template section structure.
   - Add only title, date, source prompt link, timebox, and a short instruction: `Fill keywords only, not full prose. Aim for the talking points you would say aloud.`
   - Remove or leave blank any placeholder text that would become a hint.
   - If the template is missing, recreate only its section headings as a fallback and note the fallback in `practice_notes.md`.
5. Write `practice_MMDD/practice_prompt.md` with only:
   - candidate-facing prompt
   - timebox, usually 30 or 45 minutes
   - expected deliverable: keyword talking points in `practice_outline.md`
   - allowed clarifying assumptions if they are grounded in the source prompt
   - completion instruction, e.g. `Fill practice_outline.md with keywords, then say done.`
6. Create `practice_MMDD/practice_feedback.md` with date, source files, timebox, and `Status: waiting for the user's keyword outline`.
7. Create `practice_MMDD/practice_notes.md` with:
   - date and source files
   - `Status: practice setup`
   - empty sections for `Conversation Notes`, `Misses`, `Repairs`, and `Next Practice / Mock`
8. Tell the user only where `practice_outline.md` is, the timebox, and that she should fill keywords only. Do not include answer guidance in chat.

### Phase 1: Keyword Outline

the user fills `practice_MMDD/practice_outline.md` with keyword talking points. Do not edit it, expand it, or provide hints while she is filling it unless she explicitly asks a clarification question.

### Phase 2: Review Keyword Outline

Use this when the user says `done`, `review`, `feedback`, `what did I miss`, or points to `practice_MMDD/practice_outline.md`.

1. Read `practice_MMDD/practice_outline.md`, `practice_MMDD/practice_prompt.md`, `practice_MMDD/practice_notes.md`, and the same problem context used in setup.
2. Review the outline as keyword talking points, not polished prose. Do not penalize missing full sentences.
3. Evaluate against the feedback rubric, with special attention to:
   - whether requirements, goals, non-goals, constraints, and success metrics are explicit
   - whether the 1-2 cruxes appear early and receive enough depth
   - whether architecture, data flow, training flow, serving flow, evaluation, and monitoring connect coherently
   - decision-making versus listing alternatives
   - whether the answer is appropriately simple for the constraints
   - production maturity: failure modes, rollback, privacy/safety, drift, cost, ownership, and iteration plan
   - Staff+ signal: invariants, tradeoffs, rollout sequencing, cross-team contracts, and crisp communication
4. Write `practice_MMDD/practice_feedback.md` with:
   - raw outline excerpt or raw answer evidence when useful, quoted from
     `practice_outline.md` or the conversation
   - verdict: `ready for section discussion`, `needs one outline repair pass`, or `not ready yet`
   - `Misses`: top missing, wrong, vague, or under-defended points, grouped by
     section
   - strongest signals already present
   - crux assessment
   - 3-5 keyword-level repairs the user should add to `practice_outline.md`, not a full model answer
   - proposed section-by-section discussion order, prioritizing weak sections first
5. Append the review summary, verdict, and misses to `practice_MMDD/practice_notes.md`.
6. In chat, summarize only the verdict, top 3 misses, and the next repair pass or first discussion section.

### Phase 3: Guided Section Discussion

Use this after the outline review or when the user asks to discuss the practice section by section.

1. Guide one section at a time in the order from `practice_feedback.md`, usually starting with the weakest or highest-leverage section.
2. Ask for the user's spoken explanation for that section, then respond with targeted feedback.
3. Allow the user to ask questions at any time. Answer directly, then return to the current section unless she chooses to switch.
4. Dive deep on weak topics when needed:
   - clarify the mental model
   - compare options briefly
   - give interview phrasing she can say aloud
   - tie the topic back to requirements, metrics, constraints, and Staff+ signal
5. Avoid turning the session into a full model answer. The goal is to strengthen the user's outline and spoken reasoning.

### Phase 4: Proactive Practice Notes

During setup, review, and guided discussion, proactively append to
`practice_MMDD/practice_notes.md` after every interview-relevant turn. Do not
wait for the exchange to be fully stabilized; later turns can append corrections
or refinements.

- **Section:** current section
- **Question or prompt:** what was discussed
- **Raw answer:** quoted transcript of the user's spoken explanation when
  available
- **Paraphrased answer:** concise summary only when raw transcript is too long,
  fragmented, or unavailable
- **Verdict:** `pass`, `lean pass`, `needs repair`, or `miss`
- **Misses:** specific missing, wrong, vague, or under-defended points
- **Feedback:** what was strong and what was weak
- **Repair:** concrete keyword, talking point, mental model, or follow-up drill
- **Next:** what to revisit later

For assistant-only teaching turns or clarifications, record:

- **Topic:** current concept or section
- **Assistant note:** concise explanation, decision, or clarification
- **Why it matters:** interview relevance or Staff+ signal
- **Next:** what to revisit later

Do not record workflow, environment, IDE, or tooling chatter unless explicitly
asked. Keep notes chronological and practical for next practice.

### Phase 5: Wrap Up Practice

When the user asks to stop, wrap, finish practice, or move to mock:

1. Read `practice_feedback.md`, `practice_notes.md`, and the final `practice_outline.md`.
2. Append a `Wrap-Up` section to `practice_notes.md` with:
   - final verdict: `ready for mock`, `needs one repair pass`, or `needs concept review`
   - top 3 recurring misses, with concrete examples from raw answer notes
   - strongest Staff+ signals to preserve
   - specific repairs before the next practice or mock
   - 2-4 next practice or mock prompts, without answer keys
3. If the session exposed durable misses, append candidate-facing drills to `input/next_round_mock_questions.md` without hidden hints.
4. In chat, summarize the verdict, recurring misses, and next practice/mock plan.

### Practice Guardrails

- Use the Databricks template path above by default for practice docs.
- Do not write the answer for the user during setup or outline review.
- Do not auto-patch `practice_MMDD/practice_outline.md` unless the user explicitly asks.
- Feedback can include small keyword-level additions, but avoid full replacement paragraphs unless the user asks for a rewrite.
- Keep practice mode separate from mock mode: it is guided coaching and discussion, not interviewer roleplay, and it uses `practice_notes.md` instead of `mock_feedback.md`.
- For outline-only review: skip guided discussion (phase 3), provide feedback on the outline, and wrap up directly.
- Preserve the user's keyword-only practice format. Do not expand her outline into paragraphs by default.

## Companioned Learn Mode Workflow

Use companioned learn mode as read-along Q&A support with auto-notes. The user is reading independently. Do not explain upfront or start teaching unless asked.
Once the user enters companioned learn mode, stay in that mode and append to
`<problem_dir>/learn_notes.md` on every interview-relevant turn until she explicitly
asks to wrap learning, finish learning, exit learn mode, or consolidate notes.

### Setup

1. Resolve `problem_dir`.
2. Read relevant local context silently: `input/0_requirements.md`, `input/<problem>.md`, `solution/interview_solutions.md`, `solution/deep_dive.md`, root-level `learn_notes.md`, and any provided notes or search-result packets. If `solution/` doesn't exist, read `output/` as supporting context.
3. Create `<problem_dir>/learn_notes.md` if it does not exist. If `solution/learn_notes.md` exists, read it as supporting context but continue writing new notes to root-level `learn_notes.md`.
4. Wait for the user's question. Do not summarize, propose a menu, ask what she wants next, quiz her, or ask check-for-understanding questions.

### During Learning

1. **Read-Along Q&A Loop:**
   - Wait for the user's question.
   - Answer the immediate question directly and stop cleanly.
   - Do not proactively explain, continue, advance topics, or end with prompts.
   - If the user says "next", continue only if there is an established sequence from prior user questions or material.

2. **Grounding:**
   - Ground answers in local notes first: `input/0_requirements.md`, problem statements, `solution/interview_solutions.md`, `solution/deep_dive.md`, root-level `learn_notes.md`, and relevant bundled references.
   - If the user provides web search results, use those results as grounding and distinguish sourced facts from inference.
   - If the user explicitly asks to search the web, search and cite sources before answering.
   - If local notes and provided results are insufficient, say what is inferred and what is missing.

3. **Explanations:**
   - **Default answer length:** 2-3 sentences maximum covering the core concept. Think "what you'd say in first 30 seconds of explaining this in an interview."
   - **One more level if asked:** If the user asks "why", "how", or "elaborate", add ONE more paragraph (3-4 sentences) with key details — then stop. Do not write comprehensive explanations.
   - **Strict brevity:** Each answer should fit on one screen (~150 words max for initial answer, ~300 words max after elaboration).
   - Use plain language first, then technical depth if needed.
   - Use one compact example at most — no multiple examples.
   - Tie design choices back to requirements and L6+ signals only when directly relevant to the question.
   - Highlight Staff+ interview phrasing when useful, but don't add extra explanatory context.
   - Emphasize staff-level habits: identify the crux, cut unnecessary complexity, make decisions, and connect ML choices to production constraints.

4. **Auto-Notes:**
   - After every interview-relevant user question, assistant answer, useful
     clarification, or insight, record it in `<problem_dir>/learn_notes.md`.
   - Do not wait for a separate note-taking request.
   - If a later turn corrects or refines the idea, append a short refinement
     note instead of rewriting history.
   - **Preserve raw conversation output.** Include:
     - **Raw question:** The user's question verbatim as a blockquote
     - **Raw answer:** The assistant's full answer verbatim as a blockquote (not summarized)
     - **Mental model:** One key insight or misconception fixed (one sentence)
     - **Interview phrasing:** One sentence the user can say aloud
     - **Grounding:** Local note, source file, or cited source used
   - Do not summarize or compress the raw answer. The raw conversation is the
     primary artifact; mental model and interview phrasing are concise extracts.
   - Do not record workflow, environment, IDE, file-conversion, or tooling questions unless explicitly asked.
   - Keep notes chronological and slightly raw, grouped by parent topic.

5. **Defer Deep-Dive Updates:**
   - During active learn mode, write only to `<problem_dir>/learn_notes.md`.
   - Do not merge, rewrite, or polish `solution/deep_dive.md` until the user explicitly exits or wraps up learn mode.
   - Stay in learn mode until the user says `end learn`, `conclude learn`, `exit learn`, `wrap learning`, `finish learning`, or asks to consolidate learning notes.
   - Do not treat generic `summarize`, `done`, `next`, or a topic change as permission to exit learn mode unless it clearly refers to the learning session.

### End of Learn Session

When the user explicitly wraps learning or asks to consolidate:

1. Read the full `<problem_dir>/learn_notes.md`.
2. Remove duplicate, low-signal, or non-interview-relevant entries unless explicitly requested.
3. Regroup related Q&A threads by durable concepts, components, tradeoffs, failure modes, and interview phrasing.
4. Merge cleaned takeaways into `solution/deep_dive.md` under relevant sections or a dated `Learning Notes & Refinements` section.
5. Preserve source grounding, examples, edge cases, and strong phrasing.
6. Reset `<problem_dir>/learn_notes.md` to a short staging inbox or mark merged entries with the date.
7. Summarize what changed in `deep_dive.md` and what remains open.

## Mock Mode Workflow

Use mock mode to simulate a real ML system design interview with step-by-step feedback.
Once the user enters mock mode, stay in mock mode and append to
`mock_MMDD/mock_feedback.md` on every interview-relevant turn until she
explicitly asks to stop, wrap, end the mock, or switch modes.

### Setup

1. Resolve `problem_dir`.
2. Read mock context from `input/0_requirements.md`, `input/<problem>.md`, `solution/interview_solutions.md`, `solution/deep_dive.md`, and raw source notes. Read `output/` as supporting context if `solution/` doesn't exist.
3. Create a fresh top-level mock directory named `mock_MMDD/`. If one already exists today, create `mock_MMDD_2/`, `mock_MMDD_3/`, etc.
4. **Session scope:** Default to 3-5 parent questions per mock session (similar to real 45-60 min interview). User can request more/fewer.
5. Write `mock_instructions.md` with only the candidate-facing prompt, constraints, allowed assumptions, expected deliverables, and how the user should signal completion. Do not include answer keys, hints, rubrics, or expected sequence.
6. Create `my_solution.md` as the user's Markdown outline workspace with no solution hints.
7. Create `mock_feedback.md` with an initial session header, source files, and
   empty sections for `Transcript`, `Verdicts And Misses`, `Hints Given`,
   `Design Review`, and `Next Drills`.
7. State only the interview problem and your role as interviewer.
8. Ask exactly one question. Do not reveal the answer, rubric, expected sequence, or hints.

### During Mock

1. **Ask one question per assistant turn.**
   - Probe one thing at a time: clarification, product objective, architecture, data, modeling, metrics, failure mode, scalability, cross-team contract, or operational maturity.
   - Do not bundle multiple numbered questions.
   - Do not coach, narrate next steps, or provide checklists.

2. **Clarification Questions:**
   - When the user asks clarifying questions, answer directly with constraints and examples.
   - Pick reasonable assumptions for ambiguous points.
   - Do not volunteer hidden edge cases or gotchas.
   - Record the raw clarification question and interviewer answer in
     `mock_feedback.md`.

3. **Approach Feedback:**
   - When the user outlines an approach, give concise interviewer feedback.
   - Call out missing requirements, overcomplication, option-listing without decisions, weak crux identification, or too much time on basics.
   - Lead with `Verdict` and `Misses` before any improvement advice.
   - End with at most one targeted next question.
   - Record the raw approach transcript, verdict, misses, feedback, and next
     question in `mock_feedback.md`.

4. **Design Work:**
   - the user writes in `mock_MMDD/my_solution.md`.
   - Do not edit files or write the solution for her.
   - Do not provide hints, reference pointers, or solution direction unless she explicitly asks for clarification or help.
   - Record any hints in `mock_feedback.md`.

5. **Design Review:**
   - When the user says "done", review `mock_MMDD/my_solution.md`.
   - Review in this order: missing requirements or correctness gaps, crux identification, decision-making, complexity control, deep dives, tradeoffs, failure modes, metrics, evolution plan, L6+ signals, then communication.
   - Provide the smallest conceptual fix for each issue. Do not auto-patch her mock answer.
   - Record the relevant raw `my_solution.md` excerpts, verdict, misses,
     findings, and fixes in `mock_feedback.md`.

6. **Follow-Up:**
   - Ask one scaling, operational, ML correctness, or cross-team follow-up at a time after the current design has been reviewed.

### Closing

When the user asks to stop or the mock reaches a natural end:

- Give a verdict: `strong pass`, `pass`, `lean pass`, `lean no`, or `no-hire for this round`.
- Include 2-4 focused improvements.
- Identify the weakest concept to review next.
- Record the verdict and improvements in `mock_feedback.md`.
- Summarize misses and weaknesses from the session.
- Convert important misses into candidate-facing next-round prompts in `input/next_round_mock_questions.md`, without answer keys or hidden hints.

### Note-Taking

Record every interview-relevant turn in `mock_feedback.md` immediately after it
happens:

- the user's clarification questions and interviewer answers
- the user's raw approach, verdict, misses, and feedback
- Hints given during design
- Assistant follow-up questions and why they were asked
- Design review findings
- Final verdict and improvements
- End-of-session misses, weaknesses, and next-round question seeds

Use this structure for approach or follow-up turns:

```markdown
## <question or topic>

- Asked: <timestamp>
- Raw answer:
  > <the user's answer verbatim when available>
- Verdict: `<strong pass|pass|lean pass|lean no|no-hire|needs repair>`
- Misses:
  - <specific missing/wrong/vague point>
- Feedback: <direct interviewer feedback>
- Stronger framing: <concise Staff+ phrasing or smallest conceptual fix>
- Next question: <one targeted follow-up, if continuing>
```

For design-review findings, quote only the relevant excerpt from
`my_solution.md`, then record `Verdict`, `Misses`, `Fix`, and `Next drill`.

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

- **Prep mode:** Start from root-level `0_requirements.md`, never modify it. Use `$system-design-material-finder` to gather interview prep materials into `reference/`, then generate `1_mock_questions.md`, `3_key_topics.md`, `4_interview_ready_solutions.md`, `5_deep_dive.md`, make the final link/style pass on `4_interview_ready_solutions.md`, and finally write `2_index.md` with ranked reference materials.
- **Solve mode:** Use `$system-design-material-finder` to gather solutions, tutorials, and tech blogs into `reference/`, then create `solution/interview_solutions.md` grounded in production patterns. It is the cheat sheet before a real interview.
- **Practice mode:** Create `practice_MMDD/practice_outline.md` from `~/Documents/work/0_databricks/Templates/ml_system_design_template.md`, review the user's keyword outline. For full practice, guide section-by-section discussion with notes in `practice_notes.md`. For outline-only review, skip guided discussion and wrap up after feedback.
- **Companioned learn mode:** Default to read-along Q&A with auto-notes, then consolidate into `solution/deep_dive.md` only at wrap-up.
- **Mock mode:** Treat it like a real interview: outline first, design second, do not over-optimize.
- **Between rounds:** Review `4_interview_ready_solutions.md` for prep-mode folders or `solution/interview_solutions.md` for legacy solve-mode folders, then run a mock to stress-test under time pressure.

## File Reference

| File | Purpose | Created by | Edited in Learn | Reviewed in Mock |
|------|---------|------------|-----------------|------------------|
| `0_requirements.md` | Prep-mode ground truth | User | No | Reference |
| `1_mock_questions.md` | Mock question bank and probes | Prep | No | Reference |
| `2_index.md` | Prep index and study checklist, written last | Prep | No | Reference |
| `3_key_topics.md` | Concise talking points and short answers for fast review | Prep | No | Reference |
| `4_interview_ready_solutions.md` | Interview-ready spoken answer (30-45 min delivery, not learning depth) | Prep | Optional reference only | Reference |
| `5_deep_dive.md` | Staff/Principal learning depth (understanding why, not for interview delivery) | Prep | No | Reference |
| `context/*` | Raw source material | User | No | Reference |
| `reference/*` | Curated study materials ranked in `2_index.md` during prep | User/Research | Optional reference only | Reference |
| `input/0_requirements.md` | Legacy normalized prep prompt from raw context | Solve | No | Reference |
| `input/<problem>.md` | Legacy candidate-facing problem statement | Solve | No | Reference |
| `input/next_round_mock_questions.md` | Next mock prompts from prior misses | Mock | No | Reference |
| `solution/interview_solutions.md` | Interview-ready answer (30-45 min delivery, not learning depth) | Solve | Optional reference only | Reference |
| `solution/deep_dive.md` | Staff/Principal learning depth (understanding why, not for interview delivery) | Solve + Learn wrap-up | Wrap-up only | Reference |
| `learn_notes.md` | Raw chronological learning notes for the current problem | Learn | Yes | No |
| `practice_MMDD/practice_prompt.md` | Candidate-facing timed practice prompt | Practice | No | Reference |
| `practice_MMDD/practice_outline.md` | Template-based keyword talking points for full or outline-only practice | Practice/User | No | Reviewed in Practice |
| `practice_MMDD/practice_feedback.md` | Raw outline evidence, verdict, misses, and repairs | Practice | No | Reference |
| `practice_MMDD/practice_notes.md` | Raw answer notes, verdicts, misses, repairs, and wrap-up plan (full practice only) | Practice | No | Reference |
| `mock_MMDD/mock_instructions.md` | Candidate-facing mock prompt | Mock | No | Reference |
| `mock_MMDD/my_solution.md` | the user's mock design attempt | User | No | Yes |
| `mock_MMDD/mock_feedback.md` | Raw transcript, verdict, misses, feedback, and next drills | Mock | No | Yes |

## Relationship to Other Skills

- Use `coding-interview-companion` for algorithm, coding, or implementation rounds.
- Use `ml-fundamentals-interview` for non-system-design ML theory Q&A and conversational theory mocks.
- Use `ml-daily-quiz` for tracked daily drills and spaced review over a fixed question bank.
- Use this skill for ML system design, research infrastructure, serving, evaluation, ranking, recommendation, and platform design prep.
