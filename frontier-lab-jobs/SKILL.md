---
name: frontier-lab-jobs
description: Use this skill when asked to "find roles for [company]" — e.g. "find roles for Anthropic", "find roles for OpenAI", "find roles for Microsoft AI", "find roles at Handshake", "find roles at xAI", or "find roles for all companies". Also triggers on "search for roles at [company]", "what's open at [company]", "apply to this role", "apply for roles", or "submit applications". Reads your preferences, WILL APPLY queue, and applied roles from the tracking file before searching or applying. Suggests new roles only unless the user explicitly asks to apply. When applying, reads roles marked "will apply", finds the official application page, asks which resume version to use, uses browser/computer control to fill the application, and stops for user confirmation before final submission.
compatibility: WebFetch, WebSearch, Browser/Chrome computer use
---

# Frontier Lab Job Search

## Tracking File

**File**: `apply/application_tracker.md` (relative to vault root: `/Users/xue/Documents/Job/`)

**Absolute path**: `/Users/xue/Documents/Job/apply/application_tracker.md`

This file has three sections the skill reads before doing anything:

1. **`## Preferences`** — your domain priorities, role preferences, compensation floor, and flags from past searches. Use this to filter and rank suggestions.
2. **`### 🎯 WILL APPLY`** — roles queued for application. When the user asks to apply without naming specific roles, this table is the application queue.
3. **`### 📝 APPLIED roles`** — roles you've manually added. The skill never modifies this section unless explicitly asked after submission. Use it to avoid suggesting roles you've already applied to.

## Workflow on Each Run

Use the **Search Workflow** unless the user's request explicitly includes applying, submitting, filling an application, or using a specific resume for a role.

Use the **Application Workflow** only when the user explicitly asks to apply to one or more roles.

## Search Workflow

### Step 1 — Read the tracking file

Open `/Users/xue/Documents/Job/apply/application_tracker.md` and extract:
- **Preferences section**: domain priorities, avoid list, flags, compensation floor
- **WILL APPLY table**: every role title + company with status `will apply`
- **APPLIED roles table**: every role title + company already in the table (to deduplicate)

**Error handling**: If the tracking file doesn't exist, stop and tell the user:
> "Tracking file not found at `/Users/xue/Documents/Job/apply/application_tracker.md`. Please create it or update the path in the skill."

Do not proceed to search until these sections are parsed.

### Step 2 — Search careers pages

Use the company search registry below. If the user specifies a company not in the registry, search `site:{company-domain}/careers` for the role types.

**Company Registry**:
- **Anthropic**: `https://job-boards.greenhouse.io/anthropic` (filter: engineering, SF/Seattle/NYC)
- **OpenAI**: `site:openai.com/careers` (search: research engineer, ML engineer, SF/NYC)
- **xAI**: `https://x.ai/careers` or `site:x.ai/careers` (search: ML engineer, research engineer, SF/Bay Area)
- **Handshake**: `https://jobs.ashbyhq.com/handshake` + `https://joinhandshake.com/careers/` (search: AI, ML, research engineer, SF)
- **Databricks**: `site:databricks.com/company/careers` (search: GenAI, ML engineer, Mountain View/SF/Seattle)
- **Meta AI**: `site:metacareers.com` (filter: AI research, MLE, Menlo Park/NYC/Seattle)
- **Google DeepMind**: `site:deepmind.google/careers` (search: research engineer, ML engineer, Mountain View/NYC)
- **Microsoft AI**: `site:jobs.careers.microsoft.com` (filter: ML/research, Seattle/Bay Area)
- **Cohere**: `site:cohere.com/careers` (search: ML engineer, research, SF/Toronto)
- **Character.AI**: `site:character.ai/careers` or job boards (search: ML engineer, Menlo Park)
- **Scale AI**: `site:scale.com/careers` (search: ML engineer, research, SF)
- **Perplexity**: `site:perplexity.ai/careers` (search: ML engineer, research, SF)
- **Adept**: `site:adept.ai/careers` (search: ML engineer, research, SF)

If the user asks for "all companies" or doesn't specify, search the top 5: Anthropic, OpenAI, xAI, Handshake, Databricks.

### Step 3 — Filter candidates

Keep a role only if **all** of the following are true:
- Title is MLE, Research Engineer, or Research Scientist (no performance engineer, data engineer, full-stack, manager)
- Location is SF, NYC, Seattle, or Bay Area (hybrid acceptable; flag 5-days/week in-office)
- Not already in the **WILL APPLY** table or **APPLIED roles** table (check both)
- Aligns with at least one preference domain (LLM post-training, RL, LLM systems, LLM application)
- Compensation likely meets the floor (use the benchmark table below, or extract from posting)

Apply any specific "Avoid" or "Flags" from the Preferences section to further filter.

### Step 4 — Score and rank

Rank surviving roles by domain fit:

1. **post-training**: RLHF, reward models, Constitutional AI, RL fine-tuning, alignment
   - Examples: "Research Engineer, Post-Training", "Reward Models Platform"
2. **rl-systems**: RL infrastructure, RL training environments, agentic training
   - Examples: "Research Engineer, Universes", "RL Infrastructure"
3. **llm-infra**: LLM systems, inference optimization, scaling infrastructure with research component
   - Examples: "Research Engineer, Inference", "LLM Systems Engineer"
4. **llm-app**: LLM application, applied ML, evaluation, agents, product ML
   - Examples: "Applied AI Engineer", "ML Engineer, LLM Evals"
5. **recsys**: LLM × RecSys, general RecSys
   - Examples: "ML Engineer, Enterprise Brain", "Staff MLE - GenAI + RecSys"

Within each tier, prefer Staff-level roles (8+ yrs, explicit "Staff" title).

### Step 5 — Extract compensation from postings

For each role URL, use WebFetch to extract actual compensation from the job posting:
- Look for: salary range, base, equity, total comp keywords
- Prioritize: "total compensation", "salary range", "base salary + equity"
- Format: `$200K-$370K (from posting)` if found, or `$400-700K (est.)` if using benchmark

Fall back to benchmark estimates only if parsing fails. Mark the source in the Compensation Expectation column.

### Step 6 — Output suggestions

Print a **Suggestions** table — do not write to the tracking file yet. The user decides what to add.

**Output format**:

```
## New Role Suggestions — [date]

Roles already in your applied/queued list: [list titles, confirm skipped]

| Company | Role | Matched Skills | Required Skills | Skill Gap | Compensation Expectation | Requirement Summary | Domain Fit | Notes |
|---------|------|----------------|-----------------|-----------|--------------------------|---------------------|------------|-------|
| ...     | [Title](URL) | ... | ... | ... | ... | ... | post-training | ... |

Top pick: [one sentence on the single best role and why]
```

**Domain Fit** column values: `post-training`, `rl-systems`, `llm-infra`, `llm-app`, `recsys`, `agentic` (new)

### Step 7 — Optionally write to WILL APPLY

After showing suggestions, ask:
> "Add these N roles to the WILL APPLY section? (yes/no)"

If yes:
1. Append roles to `### 🎯 WILL APPLY` table with all columns filled
2. Update Summary metrics:
   - Count total rows across WILL APPLY, APPLIED, INTERVIEWING, EXCLUDED
   - Update `Total roles tracked`, `Will apply`, `Applied` counts
   - Update `Last Updated` to current date
3. Write the file
4. Confirm: "Added N roles to WILL APPLY. Updated Summary metrics."

If no, skip and confirm: "Suggestions shown. No changes made to tracking file."

## Application Workflow

Use this workflow for requests such as:
- "apply to this role"
- "apply to the top 3 roles"
- "submit applications for Anthropic"
- "use resume X for this application"
- "apply to all roles in WILL APPLY"

### Step 1 — Confirm target roles

Identify the exact role(s) the user wants to apply to.

- If the user names a role title, company, or URL, use that as the target.
- If the user asks to apply without naming specific roles, read `/Users/xue/Documents/Job/apply/application_tracker.md` and apply to the roles in `### 🎯 WILL APPLY` whose `Status` is `will apply`.
- If the user asks to "apply to the top roles" without listing them, run the Search Workflow first, present the ranked shortlist, and ask the user which roles to apply to.
- If the user asks to "apply to all roles in WILL APPLY", process each role sequentially (see Step 1b below).
- Do not apply to roles already listed in the `### 📝 APPLIED roles` table unless the user explicitly says to re-apply or continue an in-progress application.
- Before opening application forms, show the queued `will apply` roles found and ask the user to confirm if there is more than one role or if the table contains stale-looking entries.

**Step 1b — Bulk application mode**

If applying to multiple roles from WILL APPLY:
1. Count total roles to apply to
2. For each role, show progress: "Applying 1/4: Handshake AI Research Engineer..."
3. After each submission, ask: "Continue to next role? (yes/skip/stop)"
   - yes: proceed to next role
   - skip: mark this role as skipped, move to next
   - stop: halt bulk application, report progress

### Step 2 — Find the official application page

Find and open the official application URL for each role.

- Prefer direct company career pages and official ATS domains linked from the company site, such as Greenhouse, Ashby, Lever, Workday, or Microsoft Careers.
- Avoid third-party mirrors, job aggregators, reposts, and recruiter pages unless they redirect to the official application.
- Before filling anything, record the company, role title, canonical job URL, application URL, location, and requisition/job ID if visible.
- If a login is required, use the user's existing browser session when available. Do not ask for, store, or type credentials unless the user is actively present and instructs you to use visible, session-local credentials.

### Step 3 — Choose the resume version

Always ask the user which resume version to use before starting the application form, even if a best-fit resume appears obvious.

- If the user already specified a resume in the current request, confirm that exact file/version before upload.
- If the user has not specified a resume, find likely resume options, present a concise list with paths, and ask the user to choose one.
- Do not upload a resume based only on inferred fit.

Resume discovery order:
1. Search likely resume folders:
   - `/Users/xue/Documents/Job/apply/resume/` (current vault)
   - `~/Documents/interview/2026_interview/5_resume/` (interview vault)
2. Prefer a recent PDF resume when an application requires upload.
3. If both Markdown and PDF exist for the same resume, use the PDF for upload and the Markdown only for extracting text.
4. Match resume version to role domain when filenames or folder names indicate specialization:
   - post-training, RLHF, reward modeling, alignment -> post-training / RL / LLM resume
   - inference, systems, scaling, infra -> LLM systems / infra resume
   - applied ML, product, recommendations -> LLM application / RecSys resume
   - agents, agentic systems -> agent / agentic resume
5. Recommend the best-fit resume when useful, but still wait for the user's explicit resume choice before uploading.

Never modify resume files during this workflow unless the user explicitly asks for resume editing.

### Step 4 — Prepare application facts

Use the user's profile from this skill, the tracking file, and local resume content for factual fields.

- Prefer copying exact values from the selected resume or profile for name, email, phone, LinkedIn, work history, and education.
- For eligibility fields, sponsorship, demographic questions, disability, veteran status, EEO, salary expectations, start date, relocation, or legal attestations, stop and ask the user unless the answer is explicitly present in the user's provided instructions for this application.
- For free-text questions, draft concise answers grounded in the selected resume and ask the user to approve before entering them if they are material, subjective, or non-trivial.
- Do not fabricate credentials, publications, employment dates, degree details, authorization status, compensation, referrals, or availability.

### Step 5 — Fill via browser/computer use

Use Browser, Chrome, or another available computer-use tool to complete the application form.

- Prefer Chrome when the task depends on existing logged-in sessions, cookies, saved profile data, or a previously started application.
- Prefer the in-app Browser for clean official job pages that do not require existing user state.
- Upload the selected resume from its local path.
- Fill only fields that can be answered from verified local context or explicit user instructions.
- Keep a running note of fields filled, fields skipped, files uploaded, and any uncertainty.
- If the website blocks automation, requires CAPTCHA, requires email/phone verification, or presents a confusing account/login flow, pause and ask the user to take over that step.

### Step 6 — Review before submit

Stop on the final review page or immediately before the final submit button.

Before submitting, present:
- Company and role
- Official application URL
- Resume file used
- Any cover letter or free-text responses entered
- Questions left blank or answered with assumptions
- Any user action still required

Ask for explicit confirmation before clicking the final submit button. Do not submit without user confirmation in the current session.

### Step 7 — After submission

After a confirmed successful submission:

- Report the confirmation message, confirmation number, and submitted timestamp if visible.
- Suggest the exact row the user can add to `### 📝 APPLIED roles`.
- Do not edit the `### 📝 APPLIED roles` table unless the user explicitly asks you to update it.
- If the user asks you to update the tracking file after submission, append or edit only the requested tracking entry and preserve all existing rows.
- If in bulk application mode, continue to next role or stop based on user input.

## Table Column Definitions

- **Company**: Company name (Anthropic, OpenAI, xAI, Handshake, etc.)
- **Role**: `[Job Title](URL)` — title is the hyperlink
- **Matched Skills**: Semicolon-separated skills from your background that match
- **Required Skills**: Key technical skills or experience explicitly required by the job posting
- **Skill Gap**: Skills/experience the user lacks or needs to develop; "None" if fully qualified
- **Compensation Expectation**: Salary range with source — `$200K-$370K (from posting)` or `$400-700K (est.)`
- **Requirement Summary**: 2-3 key reqs with fit markers (✓ / ✗)
- **Domain Fit**: one of the six tiers: `post-training`, `rl-systems`, `llm-infra`, `llm-app`, `agentic`, `recsys`
- **Notes**: office policy, level signal, hiring urgency, or flags
- **Status**: `will apply`, `applied`, `interviewing`, `excluded`

## Compensation Benchmarks

Use these estimates when actual compensation cannot be extracted from the job posting.

| Company | L6 equivalent | L7 / Staff equivalent |
|---------|--------------|----------------------|
| Anthropic | $350–500K total | $500–850K total |
| OpenAI | $400–700K total | $700K–1M+ total |
| xAI | $350–600K total (est.) | $600K–1M+ total (est.) |
| Handshake | $250–370K total | $400–550K total |
| Databricks | $300–450K total | $450–750K total |
| Meta AI | $350–500K total | $550–850K total |
| Google DeepMind | $350–550K total | $600K–1M+ total |
| Microsoft AI | $250–380K + RSUs | $300–450K + RSUs |
| Cohere | $300–450K total (est.) | $500–800K total (est.) |
| Character.AI | $300–500K total (est.) | $500–850K total (est.) |
| Scale AI | $250–400K total | $400–650K total |

Estimates from public Levels.fyi / Blind data. Mark as estimates.

## What the Skill Never Does

- Never edits the `### 📝 APPLIED roles` table in `/Users/xue/Documents/Job/apply/application_tracker.md` unless the user explicitly asks for that tracking update after a submission or status change
- Never rewrites the `## Preferences` section — only reads it
- Never deletes or reorders rows the user has written
- Never suggests a role already present in the WILL APPLY table or APPLIED roles table
- Never submits an application without explicit final confirmation in the current session
- Never fabricates application facts or answers legal, eligibility, demographic, compensation, or availability questions from assumptions
- Never modifies Summary metrics unless writing new roles to WILL APPLY (then auto-updates counts)

## Updating Preferences

If during a session you give feedback on a role (e.g. "too infra-heavy", "not interested in this team"), ask whether to add it to the **Flags** list in the Preferences section. If yes, append a bullet under "Flags from past searches" and write the file. This is the only section the skill may write to without explicit user request.

## Summary Metrics Maintenance

When writing roles to the WILL APPLY section (Step 7 of Search Workflow), automatically update the Summary section:

1. Count rows in each table:
   - `### 🎯 WILL APPLY` → update `Will apply` count
   - `### 📝 APPLIED roles` → update `Applied` count
   - `### 🔄 INTERVIEWING` → update `Interviewing` count
   - `### ✋ EXCLUDED` → update `Excluded / Freeze` count
2. Sum all counts → update `Total roles tracked`
3. Update `Last Updated` to current date (YYYY-MM-DD format)

This ensures the Summary always reflects the current state of the tracking file.
