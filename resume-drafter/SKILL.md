---
name: resume-drafter
description: "Tailor a resume for a target company, role, or job posting by mapping role requirements to the user's existing project portfolio. Use for prompts like 'draft resume for <company> <role>' or when another job-search skill needs a role-specific resume."
---

# Resume Drafter

Draft a new resume by selecting, regrouping, and reframing existing projects so the resume better matches the target role. The core move is **reorganization**: do not invent new work; change emphasis, ordering, framing, and evidence density.

## Source Files

- Application tracker: `/Users/xue/Documents/Job/apply/application_tracker.md`
- Resume template: `/Users/xue/Documents/Job/apply/resume/xuew_resume_template.md`
- Project index: `/Users/xue/Documents/Job/apply/Projects/00_PROJECTS_INDEX.md`
- Project details: `/Users/xue/Documents/Job/apply/Projects/projects/`
- Output directory: `/Users/xue/Documents/Job/apply/resume/`

## Workflow

### Step 1 - Resolve the Target Role

Identify the target company, role title, and role evidence.

Use the user's prompt first:
- If the prompt includes a job URL, role description, or enough role detail, use it as the role source.
- If the prompt only names a company or ambiguous role, read the application tracker and look for matching role links or role rows.
- If no existing role link or role information exists, invoke `$frontier-lab-jobs` to find the top 5 relevant roles using the resume template as background, then ask the user to choose one before continuing.

Do not draft an outline or resume until one exact role is selected.

Completion criterion: one exact target role is selected with either a job link, pasted role requirements, or tracker evidence.

### Step 2 - Read the Baseline

Read the resume template, project index, and relevant project detail files.

Start with:
1. `/Users/xue/Documents/Job/apply/resume/xuew_resume_template.md`
2. `/Users/xue/Documents/Job/apply/Projects/00_PROJECTS_INDEX.md`
3. Project detail files under `/Users/xue/Documents/Job/apply/Projects/projects/` selected by role fit

Use `rg` over the project details for role keywords such as `LLM`, `agent`, `ranking`, `recommendation`, `retrieval`, `evaluation`, `post-training`, `inference`, `personalization`, `ads`, and any exact terms from the job description.

Completion criterion: the agent can name the strongest project candidates, their theme, and the evidence that supports each one.

### Step 3 - Build the Project Map

Create a project map before drafting the resume.

Always cover both main themes:
- **AI / LLM / Agent**
- **Recommendation**

Each final resume must include at least one AI / LLM / Agent project and at least one Recommendation project, either as full bullets or compressed bullets.

For each theme, choose which projects should lead, support, or compress based on the role:
- **Lead:** strongest fit; gets prime resume space and sharper metrics.
- **Support:** shows breadth or adjacent fit; appears with concise bullets.
- **Compress:** important for coverage but lower role fit; keep short.

Adjust story emphasis by role:
- LLM/post-training/alignment roles: lead with LLM systems, eval, agents, human feedback, quality, safety, and research-production judgment.
- Agent/product roles: lead with agent workflow, tool use, reliability, UX/product impact, iteration loops, and launch outcomes.
- ML infrastructure roles: lead with scale, latency, serving, observability, data/eval pipelines, and cross-team platform leverage.
- Recommendation/ranking roles: lead with ranking, personalization, candidate generation, retrieval, experimentation, metrics, and product impact.
- Staff/Senior Staff roles: surface scope, ambiguous problem framing, durable technical direction, influence, and leverage across teams.

Completion criterion: every selected project has a target role signal, a resume section placement, and a planned emphasis.

### Step 4 - Build a Fact Ledger

Create a fact ledger before writing the outline or resume. Use only claims grounded in the resume template or project files.

Format:

```markdown
| Verified Fact | Source File | Resume Use | Missing Evidence |
|---------------|-------------|------------|------------------|
| ...           | ...         | ...        | ...              |
```

Completion criterion: every role-matched claim planned for the resume is either source-backed or listed as missing evidence.

### Step 5 - Draft an Outline for Review

Stop after drafting the outline unless the user has already approved a specific outline in the current session.

The outline must include:
- Target company and role
- Role requirement summary
- Resume positioning thesis
- Project ordering and section placement
- Theme coverage check for AI / LLM / Agent and Recommendation
- Bullet strategy: lead/support/compress decisions
- Open questions or missing evidence

Use this project-fit table:

```markdown
| Project | Theme | Role Signal | Placement | Strategy | Evidence Needed |
|---------|-------|-------------|-----------|----------|-----------------|
| ...     | ...   | ...         | ...       | ...      | ...             |
```

Ask the user to review the outline before writing the resume.

Completion criterion: the user approves the outline or gives edits that are incorporated into a revised outline.

### Step 6 - Draft the Resume

After approval, draft a new Markdown resume from the template.

Rules:
- Preserve verified facts from the template and project files.
- Do not fabricate metrics, titles, dates, publications, or credentials.
- Keep the resume concise and recruiter-readable.
- Prefer strong project grouping and ordering over generic keyword stuffing.
- Keep both required project themes represented, even if one is compressed.
- Preserve the user's voice: concrete Google-scale ML work, not inflated marketing prose.

Output path:

```text
/Users/xue/Documents/Job/apply/resume/xue_resume_<target_company>_<target_role>.md
```

Normalize `<target_company>` and `<target_role>` to lowercase hyphen-case, for example `xue_resume_anthropic_staff-mle.md` or `xue_resume_openai_research-engineer.md`.

If the role slug is very long, use a shortened version (e.g., `staff-mle` instead of `staff-machine-learning-engineer`).

Completion criterion: the new resume file exists, is grounded in the approved outline, and differs from the template only where role tailoring requires it.

### Step 7 - Polish with Humanizer

Call `$humanizer` on the generated resume before final verification.

Humanizer constraints:
- Use **Professional-Formal** tone for resume content.
- Remove AI-sounding phrasing, inflated claims, vague impact language, and filler.
- Preserve every verified fact, metric, project, title, date, and credential.
- Keep the resume concise; do not add new claims during polish.
- Preserve the approved project ordering and theme coverage.

Completion criterion: the resume is polished in place and remains fact-equivalent to the approved draft.

### Step 8 - Verify

Before final response:
- Re-read the generated resume.
- Confirm both main themes appear.
- Confirm the file does not contain placeholder text.
- Confirm no unapproved metrics or facts were introduced.
- Confirm the `$humanizer` polish did not change verified facts, metrics, project scope, titles, dates, or credentials.
- Compare against the template and report the major changes: reordered projects, rewritten bullets, compressed sections, and removed content.
- Report the output path and any unresolved evidence gaps.

## Output Style

Use concise Markdown. For outlines, prefer tables when comparing project fit. For final resume content, preserve a resume-like structure rather than explanatory notes.
