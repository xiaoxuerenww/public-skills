# Interview Prep Multi-Agent

Coordinate interview prep across coding, ML/LLM fundamentals, concept learning, ML system design, and behavioral prep.

## Purpose

Orchestrate multiple interview prep skills for end-to-end preparation, multi-round mocks, study plans, readiness audits, and panel interviews.

## Capabilities

- **Skill Routing** — Delegates to specialized skills based on request type
- **Multi-Round Mocks** — Coordinate coding → system design → behavioral sequences
- **Study Plans** — Generate cross-domain prep schedules
- **Readiness Audits** — Assess preparation status across all domains
- **Panel Interviews** — Run parallel or sequential interviews with different agents

## Routed Skills

This skill delegates to:

1. **coding-interview-companion** — Algorithm and data structure prep
2. **ml-fundamentals-interview** — ML/LLM theory and fundamentals
3. **ml-system-design-interview** — ML system design and architecture
4. **behavioral-interview-coach** — Behavioral and leadership interviews
5. **teach** — Concept learning and deep dives

## Customization Required

The skill references a default concept directory:
```
~/Documents/work/0_inbox/<concept>.md
```

**To customize:**

Either:
- **Option A**: Create `~/Documents/work/0_inbox/` for concept notes
- **Option B**: Update `SKILL.md` and replace with your preferred path

## Usage Examples

```
"Create a 4-week study plan for Staff MLE interviews"
"Run a multi-round mock: coding + system design + behavioral"
"Audit my readiness for Anthropic interviews"
"Panel interview: ML fundamentals + system design in parallel"
"Which interview skill should I use for RLHF prep?"
```

## File Structure

```
interview-prep-multi-agent/
├── README.md           # This file
├── SKILL.md            # Main skill definition
└── .claude-plugin/
    └── plugin.json     # Plugin metadata
```

## Notes

- All personal references sanitized to "the user"
- Default paths use `~/` notation (portable across users)
- Delegates to specialized skills rather than duplicating logic
- Supports both sequential and parallel multi-agent workflows
