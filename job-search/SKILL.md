---
name: frontier-lab-jobs
description: Use this skill when asked to "find roles for [company]" — e.g. "find roles for Anthropic", "find roles for OpenAI", "find roles for Microsoft AI", or "find roles for all companies". Also triggers on "search for roles at [company]" or "what's open at [company]". Reads your preferences and applied roles from Applied_Roles.md before searching. Suggests new roles only — never modifies your applied list. Returns a suggestion table with matched skills, compensation expectations, and requirement summaries.
compatibility: WebFetch, WebSearch
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

### Step 3 — Filter candidates

Keep a role only if **all** of the following are true:
- Title is MLE, Research Engineer, or Research Scientist (no performance engineer, data engineer, full-stack, manager)
- Location is SF, NYC, Seattle, or Bay Area (hybrid acceptable; flag 5-days/week in-office)
- Not already in the APPLIED roles table
- Aligns with at least one preference domain (LLM post-training, RL, LLM systems, LLM application)
- Compensation likely meets the floor (use the benchmark table below)

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

Print a **Suggestions** table — do not write to `Applied_Roles.md`. The user decides what to add.

**Output format**:

```
## New Role Suggestions — [date]

Roles already in your applied list: [list titles, confirm skipped]

| Company | Role | Matched Skills | Compensation Expectation | Requirement Summary | Domain Fit | Notes |
|---------|------|----------------|--------------------------|---------------------|------------|-------|
| ...     | [Title](URL) | ... | ... | ... | post-training | ... |

Top pick: [one sentence on the single best role and why]
```

**Domain Fit** column values: `post-training`, `rl-systems`, `llm-infra`, `llm-app`, `recsys`

## Table Column Definitions

- **Company**: OpenAI, Anthropic, or Microsoft AI
- **Role**: `[Job Title](URL)` — title is the hyperlink
- **Matched Skills**: Semicolon-separated skills from your background that match
- **Compensation Expectation**: Estimated range based on benchmarks below
- **Requirement Summary**: 2-3 key reqs with fit markers (✓ / ✗)
- **Domain Fit**: one of the five tiers above
- **Notes**: office policy, level signal, hiring urgency, or flags

## Compensation Benchmarks

| Company | L6 equivalent | L7 / Staff equivalent |
|---------|--------------|----------------------|
| Anthropic | $350–500K total | $500–850K total |
| OpenAI | $400–700K total | $700K–1M+ total |
| Microsoft AI | $250–380K + RSUs | $300–450K + RSUs |

Estimates from public Levels.fyi / Blind data. Mark as estimates.

## What the Skill Never Does

- Never edits the `### 📝 APPLIED roles` table — that's yours to maintain
- Never rewrites the `## Preferences` section — only reads it
- Never deletes or reorders rows the user has written
- Never suggests a role already present in the APPLIED roles table

## Updating Preferences

If during a session you give feedback on a role (e.g. "too infra-heavy", "not interested in this team"), ask whether to add it to the **Flags** list in the Preferences section. If yes, append a bullet under "Flags from past searches" and write the file. This is the only section the skill may write to.
