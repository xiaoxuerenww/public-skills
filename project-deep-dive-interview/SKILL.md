---
name: project-deep-dive-interview
description: "Collect, plan, polish, and drill project deep-dive interview materials for Staff/Senior Staff MLE or SWE roles at frontier AI labs. Use when the user asks to prepare a project deep dive, turn project notes into a single _deep_dive.md doc, quiz them to confirm assumptions and fill gaps, design a presentation outline with storytelling flow and depth/breadth balance, iteratively polish each presentation slide/section, or pressure-test a technical/execution area through drill questions. Outputs are Markdown artifacts."
---

# Project Deep Dive Interview

**Purpose:** Turn real project material into a credible Staff/Senior Staff project deep dive in a single durable artifact: `_deep_dive.md`.

Use this skill for project-focused interviews where the interviewer tests depth, judgment, ownership, cross-functional influence, engineering rigor, and whether the candidate can defend real tradeoffs under scrutiny.

### Storytelling philosophy

The presentation must explain high-level business value and domain-specific concepts in plain, accessible language. An interviewer who is not in your sub-domain should follow the story. Every project deep dive must answer six questions clearly:

1. **Why this project.** What was the business problem, who was affected, and why did it matter enough to invest in. Start from user/business pain, not from the technology.
2. **Your role and contribution.** Were you the TL, the architect, the hands-on coder, or all three? Be precise about what you personally drove vs. what the team did. "I designed the serving architecture and wrote the inference pipeline; the team built the training infra" is clear. "We built a system" is not.
3. **Technical tradeoffs.** When there were two viable approaches, explain both, why you chose one, and what you gave up. The interviewer wants to see judgment, not just execution.
4. **Challenges and surprises.** What went wrong that you did not expect? Be specific and first-hand. This is where credibility lives.
5. **How you measured success.** What were the metrics, how were they defined, and what was the ROI? The candidate must be able to state numbers from memory.
6. **Retro elevated to reusable patterns.** Do not just say "I learned X." Show how the learning became a reusable pattern, framework, or principle that you applied to subsequent projects. This is the move that elevates a good presentation into a Staff+ presentation: the candidate does not just ship one project, they extract transferable engineering judgment that compounds across projects.

All outputs must be Markdown. Do not create PPTX or Google Slides unless the user explicitly asks. Project deep-dive content uses two files per project:

- `projects/<project_slug>/_deep_dive.md` — raw collected material (collection mode), then presentation slides + reference material (after polish). The content artifact.
- `projects/<project_slug>/_outline.md` — presentation outline (plan mode). The planning artifact: narrative arc, slide structure, time budgets, depth allocation, flex plan, grading coverage, and Q&A prep.

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
      _outline.md
      _deep_dive.md
  references/
  images/
```

When this layout exists, write only `projects/<project_slug>/_deep_dive.md` and read interview requirements from `requirement/` first. If the older `input/` / `output/` layout exists instead, still keep project-deep-dive output to `_deep_dive.md` in the appropriate project/output location.

If the user asks for "chat only", do not write files. Otherwise, create or update only `_deep_dive.md` when the work produces reusable prep material.

## Modes

Only use these modes:

- **Collection mode:** Gather raw project information. Scan existing materials, create a quiz question list, make reasonable assumptions, quiz the user one question per turn to confirm and fill gaps, then output all raw material into `_deep_dive.md` organized by topic (main story, follow-up/deep-dive material, evidence status). No slide structure or presentation layout.
- **Plan mode:** Design the presentation outline from collected material. Define 10-20 slides with storytelling flow, time budgets, depth allocation, flex plan, and grading coverage. Outputs to `_outline.md`. Does not draft slide content.
- **Polish mode:** Let the user review every slide/section in the presentation part of `_deep_dive.md`, suggest changes, repeat until the user is satisfied.
- **Drill mode:** Pressure-test one part of the project, answer questions from source material, and save stabilized gaps or explanations into the reference sections of `projects/<project_slug>/_deep_dive.md`, with any compact speaking anchors reflected in the presentation slides section.

Infer the mode from the request:

- If the user says `collect`, `prepare`, `turn notes into a project deep dive`, or asks to gather project material, use collection mode.
- If the user says `plan`, `design`, `outline`, `define the structure`, `storytelling flow`, or asks for a presentation outline, use plan mode.
- If the user asks to `polish`, `review slide`, `improve slide`, or iterate on the presentation slides, use polish mode.
- If the user says `drill`, `pressure test`, `go deeper`, or asks about one component or follow-up answer, use drill mode.

Do not use separate slide, mock, review, evidence, or index modes. If the user asks for those older words, route the work into collection, plan, polish, or drill as appropriate.

## Output pattern

Project output goes into two files per project:

| File | Written by | Purpose |
|---|---|---|
| `projects/<project_slug>/_deep_dive.md` | Collection, polish, drill | Raw material (collection), then presentation slides + reference material (after polish) |
| `projects/<project_slug>/_outline.md` | Plan | Presentation outline: narrative arc, slide structure, time budgets, grading coverage, flex plan, Q&A prep |

The workflow is: **collect** raw info into `_deep_dive.md`, **plan** the slide structure in `_outline.md`, then **polish** drafts slide content back into `_deep_dive.md` following the approved outline.

After polish mode populates slides, `_deep_dive.md` has two major parts:

1. **Part 1: Presentation slides** (top half): sparse speaking anchors. Tables, bullets, and diagrams. No dense paragraphs. The candidate reads this during prep or glances at it during the interview.
2. **Part 2: Reference material** (bottom half): full evidence, extended tradeoff analysis, backup answers to likely follow-ups, verification notes, assumptions, and do-not-overclaim boundaries. The candidate studies this beforehand but does not present from it.

The principle: keep presentation slides lean and put density in reference sections. Do not create other files like `presenter_reference.md`, `deep_dive_presentation.md`, `one_pager.md`, `project_deep_dive.md`, `raw_evidence.md`, `00_index.md`, `interview_plan.md`, `mock_questions.md`, `mock_feedback.md`, `drill_notes.md`, or `learnings_retro.md`.

## Source discovery

Before generating content, read project sources in this order:

1. User-provided files and paths.
2. Current-vault requirements, if present: `requirement/0_requirements.md`, `requirement/part_1_past_project_retro.md`, and `requirement/INDEX.md`.
3. Legacy requirements, if present: `input/0_requirements.md`.
4. The selected project folder under `projects/<project_slug>/`, especially `_deep_dive.md`, or notes with `context`, `project`, `deep_dive`, `roadmap`, `design`, `postmortem`, `resume`, or `presentation` in the name.
5. Adjacent source folders when relevant, especially `projects/llm4rec/`, `projects/llm_ranker/`, `projects/AIF/`, `projects/autoresearch/`, and `references/`.
6. Existing outputs only after reading source notes, to avoid reinforcing stale prep.

Capture the source list in the reference section of `_deep_dive.md` so future work can trace what was used.

If project facts, metrics, dates, launch scope, or ownership claims are unclear, mark them as `needs verification` instead of inventing precision.

## Collection mode

Collection mode must run these steps in order.

### 1. Scan existing materials

Read interview requirements, project notes, raw evidence, prior `_deep_dive.md`, and relevant adjacent source folders. Create or update a source inventory in `projects/<project_slug>/_deep_dive.md` (in the reference section).

Capture:

- Source files read.
- Interview target: company, role, level, interviewer type, and expected format if known.
- Candidate project or project options.
- Existing verified facts.
- Conflicting or stale claims.
- Missing facts that affect credibility.

If local notes do not identify a project, ask the user for candidate projects before proceeding.

### 2. Create a quiz question list

Create a quiz question list in the reference section of `_deep_dive.md` before drafting final content. This is the ordered intake queue for the rest of collection mode. The list should cover:

- Project framing and product/user experience.
- Launch target, baseline, and missing signals.
- Personal ownership boundary ("I" vs. "we" — be precise about what the candidate personally drove).
- Architecture path.
- Hardest technical decisions.
- Technology rationale and **alternatives considered** — not just what was built but what was not built and why.
- Experiment/statistical design, if relevant.
- Evaluation and correctness.
- Rollout and de-risking gates.
- Reliability and operations.
- Quantified impact: latency, cost, accuracy, headcount-time-saved, revenue. The candidate must memorize these numbers.
- ROI defense: project cost (engineer-years x cost/engineer) vs. measured return. Interviewers translate effort into dollars and ask whether the return justified the spend.
- Retro and what changed: two concrete things the candidate would redesign with hindsight, and what the next version looks like.
- Reusable patterns from retro: what learning from this project became a principle, framework, or pattern the candidate applied to later projects. Collect at least one concrete example of "I learned X here, and later applied it to project Y." This elevates the presentation from "I shipped" to "I extract transferable judgment."
- Hardest unanticipated challenge: a specific story, not a vague answer.
- Plain-language business value: can the candidate explain why this project mattered in one sentence a non-domain interviewer would follow?

For ML/AI project deep dives, explicitly include:

- Product target and denominator.
- Baseline failure mode.
- Missing content/user/quality/safety signals.
- Online and offline architecture.
- Training/serving/evaluation constraints.
- Experiment randomization and bias handling.
- Rollout gates and dashboards.
- Reliability incidents and detection gaps.

For Q&A trap preparation, explicitly collect answers for:

- "Why didn't you use X?" — have the comparison rehearsed for every major technology choice.
- "What would you change with hindsight?" — two concrete answers, not platitudes.
- "What was the hardest unanticipated challenge?" — specific and first-hand, not second-hand.
- "Was it worth it?" — ROI in dollars, both cost and return quantified.

### 3. Make reasonable assumptions for some questions

For questions that can be partially answered from source material or strong domain context, draft plausible answers in the reference section of `_deep_dive.md` under `Assumptions pending user review`.

Rules:

- Label each assumption as `assumed draft`.
- Separate assumptions from source-derived facts and user-verified facts.
- Prefer reasonable directional answers over fake precision.
- Mark metrics, dates, ownership boundaries, and launch scope as `needs verification` unless directly supported.
- Do not treat assumptions as final facts until the user confirms or corrects them.

### 4. Quiz user to confirm assumptions and answer gaps

Quiz the user after assumptions are drafted. Always ask exactly one question per turn. Do not batch questions, even if several gaps remain.

Default behavior:

- Pick the next highest-priority unresolved item from the quiz question list.
- Ask one concise question at the end of the response.
- After each answer, immediately patch the reference section of `_deep_dive.md` with confirmed facts, corrected assumptions, and remaining gaps.
- Mark the answered item in the quiz question list as answered, corrected, or still needs verification.
- Keep a running distinction between user-verified facts, source-derived facts, assumptions pending review, and do-not-overclaim boundaries.

Question format:

```text
Next question: <one question>
```

### 5. Output raw material into `_deep_dive.md`

Create or update `projects/<project_slug>/_deep_dive.md` as the raw material repository. Collection mode does **not** create slide structure or presentation layout. That is plan mode's job.

Use this structure:

```text
# <Project Title> Deep Dive

## Source inventory
## Interview requirement context

## Main story
### Project framing
### Product and user context
### Role and ownership
### System context and baseline
### Baseline problem and diagnostic method
### End-to-end architecture
### Core technical decisions
### Alternatives and tradeoffs
### Experiment, evaluation, and correctness
### Rollout and de-risking
### Reliability and operations
### Results and impact
### Learnings and retro
### Reusable patterns (retro elevated to transferable principles)
### Staff+ signal

## Follow-up and deep-dive material
### Likely follow-up questions and backup answers
### Deep-dive topics (areas the interviewer will probe)
### Q&A trap answers

## Evidence status
### User-verified facts
### Source-derived facts
### Assumptions pending user review
### Do-not-overclaim boundaries
### Open verification items

## Quiz question list
```

Content rules:

- Preserve raw technical details even if they are messy. Do not summarize away useful evidence.
- Use `needs verification` markers for unresolved claims.
- Keep full evidence, extended tradeoff analysis, backup answers to likely follow-ups, and verification notes.
- Organize by topic, not by slide. Plan mode will later decide what goes on which slide.
- Expand abbreviations on first use, for example `Gradient Boosted Decision Tree (GBDT)` and `Deep Neural Network (DNN)`.

### 6. Consistency check

After generating or substantially updating `_deep_dive.md`, run a consistency check before moving to plan mode. This catches contradictions and gaps while the material is fresh and the user is still available to clarify.

**What to check:**

| Dimension | What to verify | Example failure |
|---|---|---|
| **Factual correctness** | Numbers, dates, team sizes, launch timelines, and technology names are internally consistent across all sections. The same fact is not stated differently in two places. | "Main story" says 3-month timeline, "Results" says 6 months. |
| **Statement consistency** | Ownership claims ("I" vs. "we"), role descriptions, and scope boundaries do not contradict each other across sections. The candidate's contribution is described the same way everywhere. | "Role and ownership" says "I designed the serving layer," but "Core technical decisions" says "the team designed the serving layer." |
| **Philosophy alignment** | The storytelling philosophy (section at the top of this skill) is reflected in the collected material. All six questions are answerable from the material: why this project, your role, technical tradeoffs, challenges, how you measured success, and reusable patterns from retro. | Material has strong architecture content but no reusable-pattern story, leaving the "retro elevated to transferable principles" gap unfilled. |
| **Metrics consistency** | Every metric cited in "Results and impact" traces back to a definition or context in an earlier section. Units, baselines, and comparison periods are consistent. ROI cost and return numbers are compatible. No metric appears without context for what it measures and why it matters. | "Results" claims "40% latency reduction" but no section defines the baseline latency or measurement method. |

**How to run the check:**

1. Re-read `_deep_dive.md` end to end after generation.
2. For each dimension, list any inconsistencies or gaps found.
3. If inconsistencies exist, fix the ones that have a clear correct answer from source material. For ambiguous ones, add them to the quiz question list and flag them as `consistency gap: needs user clarification`.
4. Append a brief consistency check summary to the reference section of `_deep_dive.md`:

```text
## Consistency check
- **Date:** <date>
- **Factual correctness:** <pass | N issues found — list>
- **Statement consistency:** <pass | N issues found — list>
- **Philosophy alignment:** <pass | gaps: list missing philosophy questions>
- **Metrics consistency:** <pass | N issues found — list>
```

5. If any gaps were added to the quiz question list, continue collection-mode quizzing to resolve them before proceeding.

## Plan mode

Use plan mode after collection is complete (or when enough material exists) to define the presentation outline before drafting full slide content.

The presentation must fit a **20-25 minute candidate presentation** followed by **25-30 minutes of interviewer Q&A**. Design the outline to hit this time budget. Multiple candidates report this round as the highest-leverage on the loop.

### Design philosophy

Every outline decision — which slides exist, how deep each goes, where time is spent — must serve the grading axes interviewers evaluate on. These are not a checklist to verify at the end; they are the lens through which the outline is designed from the start.

**Presentation structure principle:** Lead with breadth at Staff level, reserve depth for follow-up. The outline should demonstrate command of the full project landscape first, then go deep on 2-3 decision points. An outline that dives deep immediately without establishing breadth signals IC-level scope, not Staff.

| Axis | What it means for the outline |
|---|---|
| **Problem clarity** | The audience must understand the stakes within the first 2 minutes. If the problem is not crisp and compelling early, the interviewer spends the rest of the talk wondering why this project matters. Lead with "why it mattered," not "what I built." Include why this project was important to the company or team, not just the technical challenge. |
| **Architecture and alternatives** | The outline must dedicate its deepest slides to decisions, not descriptions. For every major choice, the outline allocates space for the road not taken and the reasoning. A slide that only describes what was built without why-not-X is incomplete. |
| **Ownership precision** | Ownership is not a single slide; it is threaded throughout. Every slide should make clear what "I" drove vs. what the team did. The outline should mark where ownership claims land so they are distributed, not clustered in one place. |
| **Incremental planning** | The outline must show how the candidate broke complex work into milestones, balanced short-term delivery with long-term goals, and navigated constraints (timelines, cross-functional dependencies, organizational challenges). This is where Staff-level execution judgment shows: not just what was built, but the sequencing strategy, how technical debt was managed, and how scalability and sustainability were weighed against shipping speed. |
| **Quality and correctness** | At least one slide must address how the candidate ensured quality: testing strategy, correctness guarantees, performance validation, and any statistical analysis used. Interviewers probe whether rigor was real or performative. |
| **Rollout and de-risking** | The outline allocates space for how the project was launched, what gates controlled risk, and how the candidate measured impact at scale. This is not an afterthought appendix slide; it demonstrates operational maturity. |
| **Quantified impact** | Numbers must appear on impact slides and be echoed in the thesis. The outline should identify which specific metrics (success metrics, KPIs, before/after comparisons) the candidate will state and ensure they are supported by collected evidence. No slide should claim impact without a number. |
| **Reflective depth** | The ending must go beyond "it worked." The outline allocates time for what surprised the candidate, what they would redesign, and what the next version looks like. Two concrete hindsight answers, not platitudes. Crucially, retro learnings must be **elevated to reusable patterns**: show how a lesson from this project became a principle or framework applied to subsequent work. This is the move that separates "I shipped a project" from "I extract transferable engineering judgment that compounds." This is where Staff+ judgment shows. |

When designing slides, ask: "Which grading axis does this slide serve?" If the answer is none, the slide is filler — cut it or repurpose it.

### 1. Review collected material

Read `_deep_dive.md` reference material and source inventory. Identify the core narrative: the hard problem, the candidate's role, the key decisions, and the outcome.

Pick a project that maps to the target team's domain when possible, but a sharp deep-dive on a tangentially-related project beats a shallow one on a perfectly-matched project.

### 2. Define the narrative arc

Design a 10-20 slide outline that tells a coherent story. Each slide entry specifies:

- **Slide number and title.**
- **Purpose:** One sentence on what this slide accomplishes in the narrative.
- **Grading axis:** Which interviewer grading criteria this slide serves (may cover more than one).
- **Time budget:** Estimated minutes for this slide. The total must sum to 20-25 minutes.
- **Depth allocation:** Whether this slide gets shallow coverage (context-setting, 30-60 seconds) or deep coverage (technical meat, 2-3 minutes). The total should balance: roughly 30% context/framing, 50% technical depth, 20% impact/retro.
- **Key content:** 2-3 bullet anchors of what goes here.

### 3. Balance depth vs. breadth

Apply these principles:

- **Go deep on 2-3 slides** that cover the hardest technical decisions, the core tradeoffs, and the candidate's unique judgment. These are the slides the interviewer will drill into.
- **Go broad on context slides** (problem framing, system overview, team structure). Keep them lean so the audience orients quickly without losing patience.
- **Cut slides that repeat** the same point. Merge or drop rather than pad.
- **Sequence for storytelling:** Problem before solution. Constraint before decision. Decision before outcome. Outcome before retro.
- **Identify the "2-minute version":** Mark 3-5 slides that, alone, would convey the project's core story if time is cut short.
- **Watch the time.** Candidates who get stuck on early slides and run short on Q&A send a negative signal. Front-load context slides at shallow depth so the presentation reaches impact and retro with time to spare.
- **Ensure alternatives-considered coverage.** At least one slide must present architecture choices alongside alternatives not taken and why. Interviewers grade on this explicitly.

### 4. Grading coverage check

Before finalizing the outline, verify every grading axis maps to at least one slide. If any axis is missing, add or restructure slides to cover it.

| Grading axis | What interviewers look for | Minimum coverage |
|---|---|---|
| Problem clarity | Clear problem statement, why it mattered to the company/team, stakes within 2 minutes. | 1 slide (setup) |
| Architecture and alternatives | Architecture choices **and** alternatives considered. Not just what was built but what was not and why. | 1-2 slides (deep) |
| Ownership precision | The candidate's specific contribution vs. the team's. "We" is fine if "I" is also surfaced. | Threaded across multiple slides, explicit in at least 1 |
| Incremental planning | Milestone breakdown, short-term vs. long-term balance, technical debt and scalability reasoning, cross-functional navigation. | 1 slide (strategy/execution) |
| Quality and correctness | Testing, correctness guarantees, performance validation, statistical analysis if relevant. | 1 slide or threaded into architecture/rollout |
| Rollout and de-risking | Launch strategy, risk gates, how impact was measured at scale. | 1 slide (rollout) |
| Quantified impact | Success metrics, KPIs, before/after numbers. The candidate can state these from memory. | 1 slide (impact) |
| Reflective depth | What surprised the candidate, what they would redesign, what the next version looks like. Two concrete hindsight answers. Retro elevated to reusable patterns applied to later projects. | 1 slide (retro/learnings) |

Output a coverage table in the outline showing which slides serve which axis. Flag any axis covered by zero slides as a gap.

### 5. Build the flex plan

Design three versions of the presentation from the same outline:

- **15-minute cut:** Mark slides to skip or compress if the interviewer signals to move faster. Keep the 2-minute-version slides intact.
- **25-minute target:** The default presentation.
- **35-minute expand:** Mark 2-3 slides with optional deeper content if time allows or the interviewer asks to go deeper on a section.

### 5. Design the Q&A prep section

Include a Q&A preparation outline in the reference section of `_deep_dive.md`:

- List 15 likely follow-up questions mapped to specific slides.
- For each, note a 60-second answer anchor.
- Flag the 4 common Q&A traps and ensure rehearsed answers exist:
  - "Why didn't you use X?" — comparison for each major technology choice.
  - "What would you change with hindsight?" — two concrete answers.
  - "What was the hardest unanticipated challenge?" — specific first-hand story.
  - "Was it worth it?" — ROI in dollars, both cost and return.
- Note: include a one-page architecture diagram the candidate can sketch live if asked.

### 6. Output the outline

Write the outline to a separate file: `projects/<project_slug>/_outline.md`. This keeps the outline as a standalone planning artifact, separate from the content in `_deep_dive.md`. Use this format:

```text
## Slide N: <Title>
**Purpose:** <one sentence>
**Grading axis:** problem clarity | architecture & alternatives | ownership | incremental planning | quality & correctness | rollout & de-risking | quantified impact | reflective depth
**Time:** <N minutes>
**Depth:** shallow | medium | deep
**Flex:** [cut] | [expand: ...] | —
**Content anchors:**
- ...
- ...
```

Add a narrative summary and grading coverage table at the top of the presentation slides section:

```text
## Narrative arc
- **Setup (slides 1-3, ~5 min):** ...
- **Core (slides 4-N, ~15 min):** ...
- **Resolution (slides N-end, ~5 min):** ...
- **2-minute version:** slides X, Y, Z
- **15-min cut:** skip slides X, Y; compress Z
- **35-min expand:** expand slides A, B with ...

## Grading coverage
| Grading axis | Covered by slides | Depth |
|---|---|---|
| Problem clarity | 1, 2 | shallow |
| Architecture & alternatives | 5, 6, 7 | deep |
| Ownership precision | 2, 5, 8 | threaded |
| Incremental planning | 4 | medium |
| Quality & correctness | 6, 8 | threaded |
| Rollout & de-risking | 9 | medium |
| Quantified impact | 10 | medium |
| Reflective depth | 11 | medium |
```

### 7. Get user approval before proceeding

Present the outline from `_outline.md` to the user. Use `AskUserQuestion` to confirm: "Approve this outline and move to polish/content drafting?" The user can accept, reorder slides, adjust depth allocation, change time budgets, or request changes. Iterate on `_outline.md` until approved. Do not draft full slide content in `_deep_dive.md` until the outline is approved.

## Polish mode

Use polish mode to iterate on `_deep_dive.md` only.

### 1. Scan the full doc for context

Read `_deep_dive.md` end to end. Internally evaluate every slide/section against these criteria:

- Whether the thesis is clear and sayable.
- Whether ownership is explicit.
- Whether the slide has one job.
- Whether technical depth is defensible.
- Whether tradeoffs are stated in the same breath as the solution.
- Whether the slide is too dense and should move material to the reference section.
- Whether claims need verification.

Build an internal priority list of improvements, but do not present the full list to the user.

### 2. Suggest one improvement at a time

For each iteration:

1. Pick the single highest-priority improvement from the internal list.
2. Show the proposed edit for that one slide or section only. Quote the current text and show the replacement so the user can review the diff.
3. **Wait for explicit user approval before writing.** Use `AskUserQuestion` to prompt the user with one option: "Accept" (apply the change as shown). The user can also select "Other" to type custom feedback. Do not patch files until the user accepts. If the user provides typed feedback instead, revise the proposal based on their input and show it again with the same prompt.
4. Once approved, patch the presentation slides section of `_deep_dive.md`.
5. Renumber `## Slide N:` headings if the change added, deleted, moved, merged, or split slides.
6. Verify numbering with `grep -n "^## Slide"`.
7. Move to the next improvement and repeat until the user is satisfied or says to stop.

Support these edit operations:

- **Add slide:** Draft the new slide from source/reference context, insert it at the right position, and renumber.
- **Improve slide:** Rewrite with clearer framing, tables, diagnostic reasoning, gating logic, or concrete tradeoffs.
- **Merge slides:** Combine overlapping or thin slides, keep the stronger framing, and move extra details to the reference section.
- **Split slide:** Split when a slide covers two distinct ideas.
- **Move content:** Relocate details to the better slide or to the reference section.
- **Renumber:** Scan all slide headings and renumber sequentially.

### 3. Compact presentation slides

When the user asks to compact the presentation:

1. Read `_deep_dive.md` end to end.
2. Identify dense paragraphs, backup evidence, caveats, long tradeoff analysis, and answer-key material in the presentation slides section.
3. Move those details into the matching heading in the reference material section, preserving evidence and wording where useful.
4. Replace dense presentation content with sparse anchors, tables, or short bullets.
5. Verify no important evidence was lost.

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
3. Embed in the presentation slides section of `_deep_dive.md` using `![[filename.png]]`, replacing any text flow block the diagram supersedes.
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

1. Read the relevant source files and existing `projects/<project_slug>/_deep_dive.md`.
2. Answer only the current question unless the user asks for a full rewrite.
3. When a stable insight emerges, append it to the reference section of `projects/<project_slug>/_deep_dive.md` under a drill notes or follow-up heading with:
   - Date.
   - Topic.
   - Strong answer.
   - Gaps or facts to verify.
   - Follow-up questions to practice.
4. If the user says to wrap up or consolidate, update the presentation slides and reference sections of `_deep_dive.md` directly. Do not create a separate drill notes file.

Keep drill answers technical and direct. Do not turn the session into broad coaching unless the user asks.

## Answer style

- Be concise and direct.
- Use bullets for artifacts and natural spoken phrasing for talk tracks.
- Do not over-polish during intake. Credible answers can acknowledge uncertainty.
- Prefer specific technical nouns over generic impact language.
- Use `needs verification` for uncertain metrics or claims.
- Separate presentation anchors from reference-section answer keys within `_deep_dive.md`.
- During collection-mode quiz intake, always ask exactly one question at the end of the response.
- When the user asks to preserve or regroup information, put it into `_deep_dive.md`, not a separate file.
