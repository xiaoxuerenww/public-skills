---
name: one-week-prep
description: |
  Plan and execute a 1-week interview prep sprint for any interview type (ML breadth, system design, coding, behavioral, project deep-dive). Generates a day-by-day study plan calibrated to the user's background, tracks daily progress, and adjusts the remaining plan when days are missed or topics shift. Use when the user wants to prepare for an interview in ~1 week, asks for a short-timeline study plan, or wants to track progress on an active prep sprint.
---

# One-Week Interview Prep Sprint

Generate a 7-day study plan for any interview type, then track daily progress and adapt.

## Modes

Detect mode from user input:

- **Plan**: user asks to prepare for an interview, create a study plan, or start a prep sprint -> generate the plan
- **Update**: user reports progress, logs a day, or says what they studied -> update state
- **Status**: user asks where they stand, what's left, or "how am I doing" -> summarize progress
- **Adjust**: user says they missed a day, want to change focus, or have fewer days left -> rebalance the plan

If ambiguous, default to **Plan** for new requests, **Update** if an active sprint state file exists.

---

## Plan Mode

### Step 1: Gather inputs

Collect (ask only for what's missing -- infer from context when possible):

| Input | How to get it | Default |
|-------|--------------|---------|
| Interview type | User's request (e.g., "ML breadth", "system design", "coding", "behavioral", "project deep-dive") | Required |
| Target company/level | User's profile or explicit mention | From CLAUDE.md profile |
| Days available | User states or default | 7 |
| Hours per day | User states or infer from schedule | 3 |
| Existing strength | User's background (CLAUDE.md) or ask | Infer from profile |
| Weak areas | User states or "unknown" | Determine in plan |
| Target note location | Linked note, current directory, or ask | `<vault>/interview-prep/` |

_Done when_: you have interview type, level, and days.

### Step 2: Build topic inventory

Based on interview type, enumerate all topics that could appear. Use these sources:

- For ML breadth/theory: reference the topic checklist in `../ml_theory_breadth_prep_guide.md`
- For ML system design: reference `../ml-system-design-interview/SKILL.md` patterns
- For coding: reference standard algorithm/DS categories
- For behavioral: reference CARL framework from `../../behavioral-interview-coach/`
- For project deep-dive: reference `../../interview-project-deep-dive/`

Categorize each topic by priority:
- **Must-know**: appears in >70% of interviews for this type/level
- **Should-know**: appears in 30-70%
- **Nice-to-know**: <30% but signals depth

_Done when_: prioritized topic list exists.

### Step 3: Calibrate to user's background

For each topic, estimate the user's current level:
- **Strong** (quick refresh): user has production experience or recent study
- **Medium** (study needed): user knows the concept but can't explain fluently
- **Weak** (deep study): user needs to learn or relearn

Use CLAUDE.md profile, conversation history, and explicit user input. When uncertain, ask for a quick self-assessment on 3-5 key areas.

_Done when_: each topic has a priority + current-level tag.

### Step 4: Generate the day-by-day plan

Allocation rules:
1. **Front-load highest-ROI topics**: must-know + weak/medium topics get early days
2. **Back-load mocks**: at least D6 or D7 should be a full mock or weak-spot blitz
3. **Group related topics**: don't scatter related concepts across non-adjacent days
4. **Budget time realistically**: each topic block should fit the daily hours budget
5. **Strong topics get sprint format**: 15-20 min refresh, not full study sessions
6. **Weak + must-know topics get dedicated blocks**: 45-90 min each

Output format for each day:

```markdown
### Day N: <theme>
| Block | Topic | Time | Method |
|-------|-------|------|--------|
| 1 | <topic> | 45 min | Study: <specific resource or approach> |
| 2 | <topic> | 30 min | Quiz: /interview-ML or self-quiz |
| ... | ... | ... | ... |

**Exit check**: <what you should be able to do after this day>
```

Include for the full plan:
- A "non-negotiable core" list: if the user can only do 4 days, which 4?
- A "daily routine template" with morning recall + evening quiz pattern

### Step 5: Write the plan + state file

Write two files:

1. **Plan doc**: `<target_dir>/prep_plan_<type>.md` -- the full day-by-day plan with topic inventory and resources
2. **State file**: `<target_dir>/prep_state_<type>.md` -- progress tracker (see State File Format below)

_Done when_: both files written, user sees the plan summary and file links.

---

## Update Mode

### Step 1: Read state

Read `prep_state_<type>.md` to get current progress.

_Done when_: you know which day the user is on and what's been completed.

### Step 2: Record progress

Update the state file based on user input:
- Mark today's topics with status (done / partial / skipped)
- Log what the user actually studied and for how long
- Record self-reported confidence (if provided)
- Note any weak spots the user identified

### Step 3: Micro-adjust

If the user is behind or ahead:
- **Behind**: suggest what to merge or cut from remaining days. Prioritize must-know topics.
- **Ahead**: suggest pulling forward nice-to-know topics or adding an extra mock.
- **Topic shift**: if the user discovered a new weak area, swap it into a remaining day.

Write adjustments directly into the plan doc (mark changes with `[adjusted]`).

_Done when_: state file updated, any plan adjustments noted, one-line summary to user.

---

## Status Mode

Read the state file and report:
- Days completed / remaining
- Topics covered vs. remaining (with priority tags)
- Weak spots identified so far
- Suggested focus for the next session
- Overall readiness estimate: "On track" / "Behind -- need to prioritize X" / "Ahead -- consider adding Y"

Keep the status report under 15 lines.

---

## Adjust Mode

Triggers: "I missed a day", "I only have 3 days left", "I want to focus more on X", "skip Y"

1. Read current state
2. Recalculate remaining days and redistribute topics
3. Apply the same allocation rules from Plan Step 4
4. Update both the plan doc and state file
5. Show the user the revised remaining days

---

## State File Format

```markdown
---
type: <interview type>
target: <company/level>
start_date: <YYYY-MM-DD>
end_date: <YYYY-MM-DD>
status: active | completed | paused
total_days: 7
hours_per_day: 3
---

# Prep Sprint: <type> -- Progress

## Daily Log

### Day 1 -- <date>
- **Status**: done | partial | skipped | pending
- **Studied**: <what was actually covered>
- **Time spent**: <actual hours>
- **Confidence**: <self-reported or observed, 1-5>
- **Weak spots**: <topics needing more work>
- **Notes**: <anything else>

### Day 2 -- <date>
- **Status**: pending
...

## Topic Tracker

| Topic | Priority | Pre-level | Current | Day | Status |
|-------|----------|-----------|---------|-----|--------|
| Transformer internals | must-know | medium | strong | D3 | done |
| RLHF/DPO | must-know | weak | medium | D4 | partial |
| Classical ML | should-know | strong | strong | D1 | done |
| ... | ... | ... | ... | ... | ... |

## Adjustments Log

- <date>: <what changed and why>
```

---

## Integration with Other Skills

- Use `/interview-ML` quiz mode for daily quizzes during ML breadth/theory sprints
- Use `/interview-ML` mock mode for D6/D7 full mocks
- Use `/interview-coding` for coding prep sprints
- Use `/behavioral-interview-coach` for behavioral prep sprints
- Use `/interview-project-deep-dive` for project deep-dive sprints
- Reference `../ml_theory_breadth_prep_guide.md` for ML breadth topic lists and resources

---

## Quality Bar

A good plan should:
- Be completable in the stated time (don't over-schedule)
- Prioritize ruthlessly (not "cover everything")
- Include at least one mock or simulation day
- Have clear exit checks so the user knows if a day was productive
- Adapt when reality diverges from the plan
