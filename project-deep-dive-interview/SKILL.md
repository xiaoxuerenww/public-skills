---
name: project-deep-dive-interview
description: "Prepare, polish, and drill project deep-dive interview materials for Staff/Senior Staff MLE or SWE roles at frontier AI labs. Use when the user asks to prepare a project deep dive, turn project notes into a compact presentation doc plus detailed reference doc, quiz them to confirm assumptions and fill gaps, iteratively polish each presentation slide/section, compact a presentation by moving details into the reference doc, or pressure-test a technical/execution area through drill questions. Outputs are Markdown artifacts."
---

# Project Deep Dive Interview

**Purpose:** Turn real project material into a credible Staff/Senior Staff project deep dive with two durable artifacts: a compact presentation doc and a detailed reference doc.

Use this skill for project-focused interviews where the interviewer tests depth, judgment, ownership, cross-functional influence, engineering rigor, and whether the candidate can defend real tradeoffs under scrutiny.

All outputs must be Markdown. Do not create PPTX or Google Slides unless the user explicitly asks. When the user says presentation, create or update a Markdown-native `deep_dive_presentation.md` by default.

## Workspace resolution

Resolve `project_dir` before reading or writing files:

1. If the user provides a project directory or file path, use that path. If the path is a file, use its parent directory.
2. Otherwise, if the current directory contains `requirement/`, `projects/`, `input/`, `output/`, `context/`, or project notes, use the current directory.
3. Otherwise, search nearby children for project notes such as `*deep*dive*.md`, `*project*.md`, `*context*.md`, `input/0_requirements.md`, or `output/project_deep_dive.md`.
4. If multiple plausible project directories exist, ask one concise clarification question.

Respect explicit source boundaries. If the user excludes a path, do not read it.

Prefer the current Project_Deep_dive layout when present:

```text
project_dir/
  requirement/
    INDEX.md
    0_requirements.md
    part_1_past_project_retro.md
    preparation_plan.md
  projects/
    <project_slug>/
      raw_evidence.md
      00_index.md
      interview_plan.md
      presenter_reference.md
      project_deep_dive.md
      one_pager.md
      deep_dive_presentation.md
      drill_notes.md
      learnings_retro.md
  references/
  images/
```

When this layout exists, write new project-specific artifacts under `projects/<project_slug>/` and read interview requirements from `requirement/` first. If the older `input/` / `output/` layout exists instead, use it as a fallback. Do not create new top-level `input/` or `output/` folders in the current vault unless the user explicitly asks or the current directory already uses that legacy layout.

If the user asks for "chat only", do not write files. Otherwise, create or update durable files when the work produces reusable prep material.

## Modes

Only use these modes:

- **Prepare mode:** Run the six-step workflow in order: scan existing materials, outline questions, make reasonable assumptions for some questions, quiz the user to confirm assumptions and fill gaps, output all evidence and information in the reference doc, then output a compact presentation doc.
- **Polish mode:** Let the user review every slide/section, suggest changes to the compact presentation doc, repeat until the user is satisfied, and when asked to compact the presentation doc, move details into the reference doc.
- **Drill mode:** Pressure-test one part of the project, answer questions from source material, and save stabilized gaps or explanations to `projects/<project_slug>/drill_notes.md` when using the current vault layout, or `output/project_deep_dive.md` / `output/drill_notes.md` in the legacy layout.

Infer the mode from the request:

- If the user says `prepare`, `create a presentation`, `make a talk track`, `turn notes into a project deep dive`, or asks for a new project-deep-dive artifact, use prepare mode.
- If the user asks to `polish`, `review slide`, `improve slide`, `compact presentation`, `move details to reference`, or iterate on the presentation doc, use polish mode.
- If the user says `drill`, `pressure test`, `go deeper`, or asks about one component or follow-up answer, use drill mode.

Do not use separate slide, mock, review, evidence, or index modes. If the user asks for those older words, route the work into prepare, polish, or drill as appropriate.

## Two-doc output pattern

All polished project output should split into two companion documents:

1. **Compact presentation doc** (`projects/<project_slug>/deep_dive_presentation.md` or `one_pager.md`): sparse speaking anchors. Tables, bullets, and diagrams. No dense paragraphs. The candidate reads this during prep or glances at it during the interview. Link to the reference doc for backup.
2. **Detailed reference doc** (`projects/<project_slug>/presenter_reference.md` or `project_deep_dive.md`): full evidence, extended tradeoff analysis, backup answers to likely follow-ups, verification notes, assumptions, and do-not-overclaim boundaries. The candidate studies this beforehand but does not present from it.

The principle: keep the presenting artifact lean and move density to the reference doc.

## Source discovery

Before generating content, read project sources in this order:

1. User-provided files and paths.
2. Current-vault requirements, if present: `requirement/0_requirements.md`, `requirement/part_1_past_project_retro.md`, and `requirement/INDEX.md`.
3. Legacy requirements, if present: `input/0_requirements.md`.
4. The selected project folder under `projects/<project_slug>/`, especially `raw_evidence.md`, `00_index.md`, `interview_plan.md`, `presenter_reference.md`, `project_deep_dive.md`, `deep_dive_presentation.md`, or notes with `context`, `project`, `deep_dive`, `roadmap`, `design`, `postmortem`, `resume`, or `presentation` in the name.
5. Adjacent source folders when relevant, especially `projects/llm4rec/`, `projects/llm_ranker/`, `projects/AIF/`, `projects/autoresearch/`, and `references/`.
6. Existing outputs only after reading source notes, to avoid reinforcing stale prep.

Capture the source list in the reference doc so future work can trace what was used.

If project facts, metrics, dates, launch scope, or ownership claims are unclear, mark them as `needs verification` instead of inventing precision.

## Prepare mode

Prepare mode must run these steps in order.

### 1. Scan existing materials

Read interview requirements, project notes, raw evidence, prior presentation/reference docs, and relevant adjacent source folders. Create or update a source inventory in `projects/<project_slug>/presenter_reference.md`.

Capture:

- Source files read.
- Interview target: company, role, level, interviewer type, and expected format if known.
- Candidate project or project options.
- Existing verified facts.
- Conflicting or stale claims.
- Missing facts that affect credibility.

If local notes do not identify a project, ask the user for candidate projects before proceeding.

### 2. Outline questions

Create a question outline in the reference doc before drafting final content. The outline should cover:

- Project framing and product/user experience.
- Launch target, baseline, and missing signals.
- Personal ownership boundary.
- Architecture path.
- Hardest technical decisions.
- Technology rationale and alternatives.
- Experiment/statistical design, if relevant.
- Evaluation and correctness.
- Rollout and de-risking gates.
- Reliability and operations.
- Impact and caveats.
- Retro and what changed.

For ML/AI project deep dives, explicitly include:

- Product target and denominator.
- Baseline failure mode.
- Missing content/user/quality/safety signals.
- Online and offline architecture.
- Training/serving/evaluation constraints.
- Experiment randomization and bias handling.
- Rollout gates and dashboards.
- Reliability incidents and detection gaps.

### 3. Make reasonable assumptions for some questions

For questions that can be partially answered from source material or strong domain context, draft plausible answers in the reference doc under `Assumptions pending user review`.

Rules:

- Label each assumption as `assumed draft`.
- Separate assumptions from source-derived facts and user-verified facts.
- Prefer reasonable directional answers over fake precision.
- Mark metrics, dates, ownership boundaries, and launch scope as `needs verification` unless directly supported.
- Do not treat assumptions as final facts until the user confirms or corrects them.

### 4. Quiz user to confirm assumptions and answer gaps

Quiz the user after assumptions are drafted. Ask concise questions focused on the highest-risk gaps.

Default behavior:

- Ask one question at a time when the user says `quiz me`, `ask one question per turn`, or when the session is already in an intake flow.
- Otherwise, ask a small batch of 3-6 questions when it is more efficient.
- After each answer, immediately patch the reference doc with confirmed facts, corrected assumptions, and remaining gaps.
- Keep a running distinction between user-verified facts, source-derived facts, assumptions pending review, and do-not-overclaim boundaries.

Question format for batches:

```text
I need a few details before drafting the presentation doc:

1. <question>
2. <question>
3. <question>
```

### 5. Output all evidence and information in the reference doc

Create or update `projects/<project_slug>/presenter_reference.md` as the detailed source of truth. If an existing `project_deep_dive.md` is the user's canonical reference doc, update that instead and state the choice.

Use this structure by default:

```text
# Presenter Reference

## Source inventory
## Interview requirement context
## Project framing
## Product and user context
## Role and ownership
## System context and baseline
## Baseline problem and diagnostic method
## End-to-end architecture
## Core technical decisions
## Alternatives and tradeoffs
## Experiment, evaluation, and correctness
## Rollout and de-risking
## Reliability and operations
## Results and impact
## Learnings and retro
## Staff+ signal
## User-verified facts
## Source-derived facts
## Assumptions pending user review
## Do-not-overclaim boundaries
## Open verification items
## Likely follow-up questions and backup answers
```

Preserve raw technical details even if they are messy. Do not summarize away useful evidence. Use `needs verification` markers for unresolved claims.

### 6. Output a compact presentation doc

Create or update `projects/<project_slug>/deep_dive_presentation.md` unless the user requests `one_pager.md` instead.

Default presentation structure:

```text
# <Project Title>

## Slide 1: Thesis
## Slide 2: Role, ownership, and outcome
## Slide 3: System context
## Slide 4: Baseline failure
## Slide 5: Product requirements
## Slide 6: Core tension
## Slide 7: Diagnosis
## Slide 8: Strategy
## Slide 9: Architecture or pipeline
## Slide 10: Technology choices
## Slide 11: Tradeoffs and alternatives
## Slide 12: Experiment and evaluation
## Slide 13: Rollout and reliability
## Slide 14: Impact and Staff+ signal
## Appendix A: Do-not-overclaim boundaries
## Appendix B: Open verification items
## Appendix C: Likely follow-up questions
```

Keep it compact:

- Use sparse speaking anchors, tables, bullets, and diagrams.
- Avoid dense paragraphs.
- Link to the reference doc for backup details.
- Cite only verified metrics on main slides.
- Move uncertain details to appendix as `needs verification`.
- Expand abbreviations on first use, for example `Gradient Boosted Decision Tree (GBDT)` and `Deep Neural Network (DNN)`.

## Polish mode

Use polish mode to iterate on `deep_dive_presentation.md` and its companion reference doc.

### 1. Let user review every slide/section

Read the current presentation doc and present a concise review queue. For each slide or section, evaluate:

- Whether the thesis is clear and sayable.
- Whether ownership is explicit.
- Whether the slide has one job.
- Whether technical depth is defensible.
- Whether tradeoffs are stated in the same breath as the solution.
- Whether the slide is too dense and should move material to the reference doc.
- Whether claims need verification.

When reviewing interactively, walk slide by slide and ask for approval or changes before moving on if the user wants tight control.

### 2. Suggest changes to the presentation doc and repeat

For each iteration:

1. Read the presentation doc and adjacent reference doc.
2. Propose targeted changes, not a full rewrite unless the user asks.
3. Patch the presentation doc directly after the user approves or asks for the change.
4. Renumber `## Slide N:` headings after adding, deleting, moving, merging, or splitting slides.
5. Verify numbering with `grep -n "^## Slide"`.
6. Repeat until the user is satisfied.

Support these edit operations:

- **Add slide:** Draft the new slide from source/reference context, insert it at the right position, and renumber.
- **Improve slide:** Rewrite with clearer framing, tables, diagnostic reasoning, gating logic, or concrete tradeoffs.
- **Merge slides:** Combine overlapping or thin slides, keep the stronger framing, and move extra details to the reference doc.
- **Split slide:** Split when a slide covers two distinct ideas.
- **Move content:** Relocate details to the better slide or to the reference doc.
- **Renumber:** Scan all slide headings and renumber sequentially.

### 3. Compact presentation doc and move details to reference doc

When the user asks to compact the presentation doc:

1. Read both `deep_dive_presentation.md` and `presenter_reference.md` or the canonical reference doc.
2. Identify dense paragraphs, backup evidence, caveats, long tradeoff analysis, and answer-key material in the presentation doc.
3. Move those details into the matching section of the reference doc, preserving evidence and wording where useful.
4. Replace dense presentation content with sparse anchors, tables, or short bullets.
5. Keep links or short pointers from the presentation doc to the reference doc.
6. Verify no important evidence was lost.

## Presentation style rules

- Sentence case for all headings.
- No em dashes or en dashes. Use commas, colons, or periods.
- No decorative bold or italic in table cells. Bold only for heading structure.
- No significance inflation such as "pivotal", "crucial", or "key". State the fact.
- Direct statements over hedged ones.
- Tables over bullets when comparing options, listing decisions, or showing a sequence.
- One diagram per concept slide max. Do not stack diagrams.
- Keep project context short. Spend most time on decisions, evidence, and tradeoffs.

Recommended table patterns:

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

## Diagram generation

When the user asks to draw or visualize a flow, architecture, or pipeline:

1. Check for available Python drawing libraries, with matplotlib preferred. If not available in the system Python, create a temporary venv: `python3 -m venv /tmp/drawvenv && /tmp/drawvenv/bin/pip install matplotlib`.
2. Save diagrams to the vault's `images/` directory with a descriptive filename.
3. Embed in the presentation doc using `![[filename.png]]`, replacing any text flow block the diagram supersedes.
4. Read the generated image to verify it rendered correctly before moving on.

## Frontier-lab calibration

Calibrate all prep to a Staff/Senior Staff bar:

- **Thesis:** The project should have a crisp one-sentence claim about the hard problem, your role, and why the solution mattered.
- **Scope:** Explain users, product area, system scale, partner teams, launch or decision impact, and time horizon.
- **Technical depth:** Be ready to defend system design, data models and storage, API/interface contracts, algorithms and data structures, concurrency and consistency, scalability, performance, reliability, testing, deployment, and observability.
- **Judgment:** Make tradeoffs explicit: why this approach, why not simpler, why not more ambitious, and what changed with evidence.
- **Ownership:** Use "I" for decisions, technical framing, alignment, escalation, and artifacts the candidate personally drove.
- **Leverage:** Highlight design docs, interfaces and platform patterns, test/CI harnesses, decision criteria, partner adoption, and follow-on impact.
- **Frontier-lab lens:** Emphasize careful deployment, operational rigor, reliability and scalability, safety and abuse/misuse resistance, fast iteration under uncertainty, and honest acknowledgment of system limitations.

Avoid making the project sound like a generic architecture tour. The center should be the 1-2 hard technical decisions and the judgment behind them.

## Drill mode

Use drill mode when the user wants to deepen one weak area or asks a technical follow-up.

1. Read the relevant source files and existing `output/project_deep_dive.md` or `projects/<project_slug>/presenter_reference.md` / `project_deep_dive.md`.
2. Answer only the current question unless the user asks for a full rewrite.
3. When a stable insight emerges, append it to `output/drill_notes.md` or `projects/<project_slug>/drill_notes.md` with:
   - Date.
   - Topic.
   - Strong answer.
   - Gaps or facts to verify.
   - Follow-up questions to practice.
4. If the user says to wrap up or consolidate, update the reference doc and compact presentation doc from `drill_notes.md`, then clear or summarize temporary learn notes if present.

Keep drill answers technical and direct. Do not turn the session into broad coaching unless the user asks.

## Answer style

- Be concise and direct.
- Use bullets for artifacts and natural spoken phrasing for talk tracks.
- Do not over-polish during intake. Credible answers can acknowledge uncertainty.
- Prefer specific technical nouns over generic impact language.
- Use `needs verification` for uncertain metrics or claims.
- Separate presentation anchors from reference-doc answer keys.
- When in one-question intake or drill flow, ask exactly one question at the end of the response.
- When the user asks to preserve or regroup information, prefer canonical Markdown docs over chat-only summaries.
