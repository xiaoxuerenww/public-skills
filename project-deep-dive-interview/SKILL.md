---
name: project-deep-dive-interview
description: "Collect, outline, polish, and drill project deep-dive interview materials for Staff/Senior Staff MLE or SWE roles at frontier AI labs. Use when the user asks to prepare a project deep dive, turn project notes into a single _deep_dive.md doc, quiz them to confirm assumptions and fill gaps, design a presentation outline with storytelling flow and key topics per page, iteratively polish each presentation slide/section, or pressure-test a technical/execution area through drill questions. Outputs are Markdown artifacts."
---

# Project Deep Dive Interview

**Purpose:** Turn real project material into a credible Staff/Senior Staff project deep dive in a single durable artifact: `_deep_dive.md`.

Use this skill for project-focused interviews where the interviewer tests depth, judgment, ownership, cross-functional influence, engineering rigor, and whether the candidate can defend real tradeoffs under scrutiny.

### Storytelling philosophy

The presentation must explain high-level business value and domain-specific concepts in plain, accessible language. An interviewer who is not in your sub-domain should follow the story.

#### Narrative craft principles

- Opening hook: lead with the tension, not the solution
- Audience calibration: assume smart non-domain interviewer
- One-sentence thesis as the backbone
- Tension before resolution at every level (project, slide, sentence)
- Concrete over abstract: specific numbers, names, dates anchor credibility
- "So what" checkpoint: every section must answer why the audience should care
- Pacing: front-load context fast, spend time on decisions and judgment
- Transitions as connective tissue: each slide should logically follow the previous
- The "I" thread: ownership woven throughout, not dumped in one place
- Closing the loop: retro connects back to the opening tension

Every project deep dive must answer six questions clearly:

1. **Why this project.** What was the business problem, who was affected, and why did it matter enough to invest in. Start from user/business pain, not from the technology.
2. **Your role and contribution.** Were you the TL, the architect, the hands-on coder, or all three? Be precise about what you personally drove vs. what the team did. "I designed the serving architecture and wrote the inference pipeline; the team built the training infra" is clear. "We built a system" is not.
3. **Technical tradeoffs.** When there were two viable approaches, explain both, why you chose one, and what you gave up. The interviewer wants to see judgment, not just execution.
4. **Challenges and surprises.** What went wrong that you did not expect? Be specific and first-hand. This is where credibility lives.
5. **How you measured success.** What were the metrics, how were they defined, and what was the ROI? The candidate must be able to state numbers from memory.
6. **Retro elevated to reusable patterns.** Do not just say "I learned X." Show how the learning became a reusable pattern, framework, or principle that you applied to subsequent projects. This is the move that elevates a good presentation into a Staff+ presentation: the candidate does not just ship one project, they extract transferable engineering judgment that compounds across projects.

All outputs must be Markdown. Do not create PPTX or Google Slides unless the user explicitly asks. Project deep-dive content uses two files per project:

- `projects/<project_slug>/_deep_dive.md` — raw collected material (collection mode), then presentation slides + reference material (after polish). The content artifact.
- `projects/<project_slug>/_outline.md` — presentation outline (outline mode). The planning artifact: narrative arc, storytelling flow, key points and topics per page.

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
- **Outline mode:** Design the presentation outline from collected material. A lightweight doc with storytelling flow, key points, and topics per page. Outputs to `_outline.md`. Does not draft slide content.
- **Polish mode:** Let the user review every slide/section in the presentation part of `_deep_dive.md`, suggest changes, repeat until the user is satisfied.
- **Drill mode:** Pressure-test one part of the project, answer questions from source material, and save stabilized gaps or explanations into the reference sections of `projects/<project_slug>/_deep_dive.md`, with any compact speaking anchors reflected in the presentation slides section.

Infer the mode from the request:

- If the user says `collect`, `prepare`, `turn notes into a project deep dive`, or asks to gather project material, use collection mode.
- If the user says `plan`, `outline`, `design`, `define the structure`, `storytelling flow`, or asks for a presentation outline, use outline mode.
- If the user asks to `polish`, `review slide`, `improve slide`, or iterate on the presentation slides, use polish mode.
- If the user says `drill`, `pressure test`, `go deeper`, or asks about one component or follow-up answer, use drill mode.

Do not use separate slide, mock, review, evidence, or index modes. If the user asks for those older words, route the work into collection, outline, polish, or drill as appropriate.

## Output pattern

Project output goes into two files per project:

| File | Written by | Purpose |
|---|---|---|
| `projects/<project_slug>/_deep_dive.md` | Collection, polish, drill | Raw material (collection), then presentation slides + reference material (after polish) |
| `projects/<project_slug>/_outline.md` | Outline | Presentation outline: narrative arc, storytelling flow, key points and topics per page |

The workflow is: **collect** raw info into `_deep_dive.md`, **outline** the storytelling flow in `_outline.md`, then **polish** drafts slide content back into `_deep_dive.md` following the approved outline.

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

Create or update `projects/<project_slug>/_deep_dive.md` as the raw material repository. Collection mode does **not** create slide structure or presentation layout. That is outline mode's job.

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
- Organize by topic, not by slide. Outline mode will later decide what goes on which slide.
- Expand abbreviations on first use, for example `Gradient Boosted Decision Tree (GBDT)` and `Deep Neural Network (DNN)`.

### 6. Consistency check

After generating or substantially updating `_deep_dive.md`, run a consistency check before moving to outline mode. This catches contradictions and gaps while the material is fresh and the user is still available to clarify.

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

## Outline mode

Use outline mode after collection is complete (or when enough material exists) to define the presentation outline before drafting full slide content. The output is a lightweight doc: storytelling flow, key points, and topics per page. No dense content drafting.

The presentation must fit a **20-25 minute candidate presentation** followed by **25-30 minutes of interviewer Q&A**.

### Storytelling flow

The outline is a narrative arc, not a content dump. Every page exists to advance the story.

#### Narrative arc shape

- Setup / rising action / climax / resolution structure
- Where the "turn" happens (the moment the project got hard)
- Emotional arc: curiosity, tension, resolution, reflection
- Foreshadowing: plant constraints early that pay off in decision pages
- The "villain": what force was working against you (latency, data sparsity, org friction)
- Callback structure: retro page echoes the opening problem statement

#### Sequencing principles

- Problem before solution
- Constraint before decision
- Decision before outcome
- Outcome before retro
- Lead with breadth at Staff level, reserve depth for follow-up
- Front-load context fast, spend time on decisions and judgment

### Grading axes

Every page must serve at least one grading axis. If it serves none, cut or repurpose it.

- Problem clarity
- Architecture and alternatives
- Ownership precision
- Incremental planning
- Quality and correctness
- Rollout and de-risking
- Quantified impact
- Reflective depth (retro elevated to reusable patterns)

### Steps

1. **Review collected material.** Read `_deep_dive.md`. Identify the core narrative: the hard problem, the candidate's role, the key decisions, and the outcome.
2. **Design the storytelling flow.** Write 10-20 pages. For each page: title, one-sentence purpose, which grading axes it serves, 2-3 topic bullets. Keep it lightweight.
3. **Mark depth allocation.** Go deep on 2-3 pages (hardest decisions, core tradeoffs). Go broad on context pages. Roughly 30% context, 50% technical depth, 20% impact/retro.
4. **Identify the 2-minute version.** Mark 3-5 pages that alone convey the core story if time is cut short.
5. **Grading coverage check.** Verify every grading axis maps to at least one page. Flag gaps.
6. **Output to `_outline.md`.** Write the outline as a standalone lightweight doc.

### Output format

Write to `projects/<project_slug>/_outline.md`:

```text
## Narrative arc
- **Setup (pages 1-3, ~5 min):** ...
- **Core (pages 4-N, ~15 min):** ...
- **Resolution (pages N-end, ~5 min):** ...
- **2-minute version:** pages X, Y, Z

## Page N: <Title>
**Purpose:** <one sentence>
**Grading axis:** <which axes>
**Topics:**
- ...
- ...
```

### Get user approval before proceeding

Present the outline to the user. Use `AskUserQuestion` to confirm: "Approve this outline and move to polish/content drafting?" Iterate on `_outline.md` until approved. Do not draft full slide content in `_deep_dive.md` until the outline is approved.

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

#### Storytelling lens

Also evaluate each slide against these narrative criteria:

- Does the slide open with tension or context, not a solution dump?
- Is there a clear "before, after" or "problem, decision, outcome" arc within the slide?
- Does the transition from the previous slide feel logical or abrupt?
- Would a non-domain interviewer follow this slide without extra explanation?
- Does the slide advance the narrative or just add information?
- Is the candidate's voice present (not a generic architecture description)?

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
