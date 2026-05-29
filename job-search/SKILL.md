---
name: frontier-lab-jobs
description: Use this skill when asked to "find roles for [company]", "apply to [role/company]", "track [role]", or variations. E.g., "find roles for Anthropic", "apply to the Universes role", "track my applications". Workflow: (1) Search careers pages for new roles; (2) Suggest new roles with fit assessment; (3) Apply to selected roles (with confirmation); (4) Track applications in Applied_Roles.md. Reads preferences and applied roles before searching. Never suggests roles you've already applied to.
compatibility: WebFetch, WebSearch, Edit, Read
---

# Frontier Lab Job Search

## Tracking File

**File**: `/Users/xue/Documents/work/interview/Company research/Applied_Roles.md`

This file has two sections the skill reads before doing anything:

1. **`## Preferences`** — your domain priorities, role preferences, compensation floor, and flags from past searches. Use this to filter and rank suggestions.
2. **`### 📝 APPLIED roles`** — roles you've manually added. The skill never modifies this section. Use it to avoid suggesting roles you've already applied to.

## Workflow on Each Run

### Step 1 — Read the file first

Open `Applied_Roles.md` and extract:
- **Preferences section**: domain priorities, avoid list, flags, compensation floor
- **APPLIED roles table**: every role title + company already in the table (to deduplicate)

Do not proceed to search until both sections are parsed.

### Step 2 — Search careers pages

- **Anthropic**: fetch `https://job-boards.greenhouse.io/anthropic` filtered to engineering departments + SF/Seattle offices
- **OpenAI**: search `site:openai.com/careers` for research engineer / ML engineer roles in SF
- **Microsoft AI**: search `site:jobs.careers.microsoft.com` for ML/research roles in Seattle or Bay Area

### Step 2.5 — Fetch actual compensation from job postings

For each role found, fetch the individual job posting URL and parse the actual salary/compensation range from the job description. Look for:
- Explicit salary ranges (e.g., "$200K - $370K")
- Compensation bands in the "Compensation" or "Salary" section
- Base + bonus + equity breakdowns when listed

Store actual compensation data. Fall back to benchmark estimates only if posting doesn't list compensation.

### Step 3 — Filter candidates

Keep a role only if **all** of the following are true:
- Title is MLE, Research Engineer, or Research Scientist (no performance engineer, data engineer, full-stack, manager)
- Location is SF, NYC, Seattle, or Bay Area (hybrid acceptable; flag 5-days/week in-office)
- Not already in the APPLIED roles table
- Aligns with at least one preference domain (LLM post-training, RL, LLM systems, LLM application)
- **Actual compensation meets the floor** (use real data from job posting, fallback to benchmark estimates if not listed)

Apply any specific "Avoid" or "Flags" from the Preferences section to further filter.

### Step 4 — Score and rank

Rank surviving roles by domain fit:
1. LLM post-training: RLHF, reward models, Constitutional AI, RL fine-tuning
2. LLM systems / inference / scaling infrastructure with research component
3. LLM application / applied ML
4. LLM × RecSys
5. General RecSys

Within each tier, prefer Staff-level roles (8+ yrs, explicit "Staff" title).

### Step 5 — Output suggestions

Print a **Suggestions** table. If no new roles found, note that in output.

**Output format**:

```
## New Role Suggestions — [date]

Roles already in your applied list: [list titles, confirm skipped]

| Company | Role | Matched Skills | Compensation Expectation | Requirement Summary | Domain Fit | Notes |
|---------|------|----------------|--------------------------|---------------------|------------|-------|
| ...     | [Title](URL) | ... | ... | ... | post-training | ... |

Top pick: [one sentence on the single best role and why]

**Ready to apply?** Reply with role name(s) or "apply all" — or "save for later" to add to WILL APPLY section without applying.
```

**Domain Fit** column values: `post-training`, `rl-systems`, `llm-infra`, `llm-app`, `recsys`

### Step 5.5 — Prepare application fields (one-time setup)

On first apply request, ask for your standard application info:

**Contact & Identity:**
- Full name
- Email address
- Phone number
- LinkedIn profile URL

**Education:**
- Degree, institution, graduation year (BS/MS/PhD)
- Field of study

**Work Summary:**
- Current/most recent title, company, years
- 1-2 line summary of key expertise for ML roles

**Standard responses:**
- Why frontier labs? (1 paragraph — can reuse across applications)
- Why this role? (template: adapt for each company's focus)

Store these in a secure working file (`~/.claude/frontier-app-template.md`) — used to auto-fill similar fields on all applications.

### Step 6 — Apply to selected roles

User confirms which role(s) to apply to. For each:

1. **Prepare fields**: Use stored application template to pre-fill:
   - Contact info (name, email, phone)
   - Education fields
   - Standard "Why frontier labs?" response
   - Role-specific motivation (fetch role description → customize 1-2 sentences)

2. **Show prefilled form**: Display the prepared content in a readable format:
   ```
   Application: Research Engineer, Universes (Anthropic)

   PREFILLED (ready to copy):
   Name: Julie Xue Wang
   Email: heheni723@gmail.com
   Phone: [from template]
   LinkedIn: [from template]
   Education: MS Computer Science, [University], [Year]

   Why frontier labs?
   [Your standard response]

   Why this role?
   [Customized for Universes — agentic training, RL systems]

   Still need:
   - Upload resume (CV_JulieWang_2026.pdf)
   - Upload cover letter or paste (optional)
   - Any custom screening questions on the form
   ```

3. **Get confirmation**: "Ready to apply? [Confirm to proceed]"
   - Confirm → opens job posting URL
   - User fills remaining fields (resume, cover letter, custom responses)
   - User submits form
   - User confirms submission complete

4. **Record timestamp**: Note the application date/time for tracking

**Example flow**:
```
Apply to: Research Engineer, Universes (Anthropic)

Submission: https://job-boards.greenhouse.io/anthropic/jobs/5061517008
Form type: Greenhouse

PREFILLED (copy these):
- Name: Julie Xue Wang
- Email: heheni723@gmail.com
- Phone: [from template]
- Why frontier labs?: "Anthropic's work on Constitutional AI and RL..."
- Why this role?: "Agentic training environments align with my work on..."

STILL NEED:
- Resume upload
- Cover letter (optional)
- Custom screening questions

Ready? [Confirm]
→ Opens job page
→ You paste/upload missing fields + submit
→ Confirm when done
```

### Step 7 — Track applications

After user confirms application submitted, update `Applied_Roles.md`:

1. **Move role from WILL APPLY → APPLIED**:
   - Cut the row from WILL APPLY section
   - Paste into APPLIED section with new `Date Applied` column value (today's date)
   - Update `Status` to "applied"

2. **Add metadata**:
   - `Crawled Date`: Today's date
   - `Date Added`: Today's date
   - `Notes`: Brief context (e.g., "Applied via Greenhouse form", "Direct referral from [person]")

3. **Update Summary**:
   - Decrement `Will apply` count
   - Increment `Applied` count
   - Update `Last Updated` timestamp

4. **Preserve user's data**: Do NOT modify Preferences, Avoid list, or Flags. Do NOT reorder existing APPLIED entries. Only append new applications.

## Table Column Definitions

- **Company**: OpenAI, Anthropic, or Microsoft AI
- **Role**: `[Job Title](URL)` — title is the hyperlink
- **Matched Skills**: Semicolon-separated skills from your background that match
- **Compensation Expectation**: **Actual range from job posting** (if listed), or estimated range from benchmarks (fallback)
- **Requirement Summary**: 2-3 key reqs with fit markers (✓ / ✗)
- **Domain Fit**: one of the five tiers above
- **Notes**: office policy, level signal, hiring urgency, compensation source (actual vs. estimate), or flags

## Compensation Approach

**Priority 1 (Use First):** Parse actual compensation from individual job postings
- Fetch job posting URL and extract salary range from description
- Look for explicit ranges, compensation sections, base+bonus+equity breakdowns
- Use this real data for filtering and compensation expectations

**Priority 2 (Fallback):** Use benchmark estimates when job posting doesn't list compensation

| Company | L6 equivalent | L7 / Staff equivalent |
|---------|--------------|----------------------|
| Anthropic | $350–500K total | $500–850K total |
| OpenAI | $400–700K total | $700K–1M+ total |
| Microsoft AI | $250–380K + RSUs | $300–450K + RSUs |

Benchmark estimates from public Levels.fyi / Blind data. Only use when actual posting compensation unavailable.

## What the Skill Does & Doesn't Do

**Skill CAN do:**
- Search careers pages for new roles
- Suggest roles ranked by fit
- Apply to roles you confirm (with explicit approval for each)
- Track applications in Applied_Roles.md (move from WILL APPLY → APPLIED, update metadata)
- Update Preferences → Flags if you request (e.g., "never Databricks infra roles")

**Skill NEVER does:**
- Never fills in personal/sensitive data (SSN, banking info, passwords) — you handle credential entry
- Never submits applications without your explicit approval
- Never deletes existing rows or reorders user-maintained sections
- Never rewrites Preferences or Avoid list — only appends to Flags
- Never suggests a role already in APPLIED table
- Never modifies APPLIED table except to append new applications or update Status/metadata on rows it added
- Never changes your manual edits or application records

## Application Flow & Permissions

### Permission Requirements

**Search + Suggest**: No confirmation needed. Skill reads preferences and suggests roles.

**Apply**: **Explicit confirmation required for each application.**
- User runs: `apply to [role name]` or `apply [list of roles]` or `apply all` (from suggestions)
- Skill fetches job posting, shows application method (Greenhouse form, LinkedIn, etc.)
- Skill asks: "Ready to apply to [Role] at [Company]? [Confirm]"
- User confirms → skill guides to application page (or form) but does NOT submit
- User fills in CV/cover letter/credentials and submits themselves
- User confirms submission complete → skill tracks in Applied_Roles.md

**Track**: No confirmation needed. Once user confirms submission, skill updates Applied_Roles.md.

### Application Limits & Strategy

- **OpenAI**: 5 application max per 180-day rolling window (internal policy)
- **Anthropic**: No stated limit; apply as many as desired
- **Other labs**: Check Flags in Preferences for known limits

If approaching a limit, skill will warn before applying (e.g., "This is application 4/5 for OpenAI in this 180-day window").

## Updating Preferences

If during a session you give feedback on a role (e.g. "too infra-heavy", "not interested in this team"), ask whether to add it to the **Flags** list in the Preferences section. If yes, append a bullet under "Flags from past searches" and write the file.

Example:
```markdown
**Flags from past searches**:
- Anthropic Pretraining Scaling: 5 days/week SF office required — drawback
- [New flag]: [Reason]
```

This is the only section the skill may write to besides applying + tracking new applications.
