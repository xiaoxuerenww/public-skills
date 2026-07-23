# Tech Article Format

Use this skill when formatting technical documents, system design docs, interview prep notes, or deep-dive articles. Apply these formatting conventions to make documents scannable, visually readable, and interview-friendly.

---

## Core Principles

1. **Scannable over prose** — Readers skim first, read second
2. **Tables for comparisons** — Never use bullet lists for tradeoffs or alternatives
3. **Visual hierarchy** — Bold, italic, and structure guide the eye
4. **Shorter is better** — One idea per bullet, not multi-sentence paragraphs

---

## Section Structure

Each major section should follow this pattern:

```markdown
## Section Title

> **TL;DR:** One-sentence summary of the key insight or decision.

**Problem:** What are we trying to solve? (1-2 sentences max)

**Why hard — the tension:**

| One extreme | Other extreme |
|-------------|---------------|
| Downside A  | Downside B    |
| Downside C  | Downside D    |

**Alternatives considered:**

| Approach | Pros | Cons | Decision |
|----------|------|------|:--------:|
| Option A | ... | ... | ❌ |
| Option B | ... | ... | ❌ |
| **Chosen option** | ... | ... | ✅ |

**Chosen:** Brief statement of what was selected.

**Why it works:**
- Key reason 1
- Key reason 2

**Invariants:**
- **Rule 1** — explanation
- **Rule 2** — explanation

**Pragmatic notes:**
- Real-world consideration
- Operational tip

**Related:** Links to related concepts or patterns
```

---

## Formatting Rules

### Text Emphasis

| Format | Use for | Example |
|--------|---------|---------|
| **Bold** | Key terms, concepts, decisions, invariants | **never directly executes SQL** |
| *Italic* | Emphasis, caveats, definitions being introduced | *plausible-but-wrong* |
| `code` | Technical terms, config keys, API endpoints, code | `execute(sql)` |

### Tables — When to Use

| Use tables for | Use bullets for |
|----------------|-----------------|
| Comparing alternatives | Sequential steps |
| Tradeoffs (pros/cons) | Single-dimension lists |
| Multi-attribute data | Simple enumerations |
| Failure modes + mitigations | Nested hierarchies |

### Bullets — Keep Short

**Good:**
- LLM **never directly executes SQL** — only produces candidates
- Context size is **capped** — ranking truncates, never grows
- Permission filtering applied **before ranking**, not after

**Bad:**
- The LLM never directly executes SQL because we want to ensure that all queries go through a validation layer first, which helps us maintain security and prevent any potential injection attacks or malformed queries from reaching the database.

### Callouts and TL;DRs

Use blockquotes for section summaries:
```markdown
> **TL;DR:** Hybrid orchestrator — deterministic harness controls flow; LLM handles intent/SQL within bounded steps.
```

---

## Common Table Patterns

### Alternatives Comparison
```markdown
| Approach | Pros | Cons | Decision |
|----------|------|------|:--------:|
| Option A | Fast | Limited | ❌ |
| **Chosen** | Balanced | Complex | ✅ |
```

### Tension/Tradeoff
```markdown
| Too much X | Too little X |
|------------|--------------|
| Problem A  | Problem B    |
```

### Component Breakdown
```markdown
| Component | Time/Cost | Notes |
|-----------|-----------|-------|
| Step 1 | ~300ms | |
| Step 2 | ~1.5s | **Dominates** |
```

### Failure Modes
```markdown
| Failure Mode | Example | Mitigation |
|-------------|---------|------------|
| **Mode A** | Specific case | How to prevent |
```

### Ownership/Contracts
```markdown
| Team/Role | Owns |
|-----------|------|
| Team A | Responsibility 1 |
| Team B | Responsibility 2 |
```

---

## Data Model Formatting

For schema/data model sections, use **definition-style lists**:

```markdown
**EntityName:**
- `field_1`, `field_2`, `field_3`
- `field_4`: `enum_value_1 | enum_value_2 | enum_value_3`
- `field_5`, `field_6`
```

---

## Appendix Conventions

- Mark appendices as *"Not for spoken delivery"* if they're reference-only
- Use horizontal rules (`---`) to separate major sections
- Keep appendices at the end, clearly labeled

---

## Quick Checklist

Before finalizing a document:

- [ ] Every section has a **TL;DR** blockquote
- [ ] All alternatives/tradeoffs use **tables**, not bullet lists
- [ ] **Bold** marks key terms and decisions
- [ ] Bullets are **single ideas**, not paragraphs
- [ ] "Why hard" sections show **tension as a table**
- [ ] Invariants are **bolded and bulleted**
- [ ] No multi-sentence bullets
