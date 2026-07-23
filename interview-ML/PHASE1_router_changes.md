# Phase 1: Smart Router Changes (Exact Diff)

## File: `interview-ML/SKILL.md`

### Current Content (lines 6-29):

```markdown
# ML Interview Prep Router

Route the user's request to the narrowest matching sub-skill. Read the user's message, classify it, then invoke the correct skill.

## Routing Table

| Request pattern | Invoke skill | Examples |
|----------------|-------------|----------|
| Companion reading/review/learning, annotate a note with Q&A | `$ml-fundamentals-interview` | "Companion my review", "Companion my reading of this note" |
| Theory, fundamentals, quiz, drill, learn/practice/mock on ML concepts | `$ml-fundamentals-interview` | "Quiz me on attention", "Practice LLM fundamentals", "Mock ML interview" |
| System design, architecture, ranking, recommendation, serving, infra | `$ml-system-design-interview` | "Design a recommendation system", "System design mock", "Practice keyword outline" |
| Explain, teach, learn a concept, one-pager, course | `$teach` | "Teach me RLHF", "Explain KV cache", "Start a course on diffusion" |
| Find references, papers, materials for a topic | `$system-design-material-finder` | "Find papers on RAG", "Curate references for model serving" |
| Prep sprint, study plan, 1-week prep, track progress, prep status | `$one-week-prep` | "Prepare for ML breadth in 1 week", "Log today's study", "How am I doing on prep?" |

## Routing Rules

1. Read the user's request and any linked note or selection context.
2. If the request clearly matches one row, invoke that sub-skill immediately with the user's full request as input. Do not re-ask what they want.
3. If the request spans multiple skills (e.g., "find references on X then design it"), run them sequentially: invoke the first, complete it, then invoke the next.
4. If the request is ambiguous between exactly two skills, pick the more likely one and state which you chose in one sentence. Do not ask a clarifying question unless genuinely stuck.
5. If the user says just "interview-ML" with no further context, briefly list the five modes and ask what they'd like to work on.
```

---

### New Content (Replace lines 6-29):

```markdown
# ML Interview Prep Router

Route the user's request to the appropriate sub-skill using pattern matching. Read the user's message, context, and classify with priority-ordered patterns.

## Pattern Matching (Priority Order)

Check patterns from top to bottom. **First match wins.**

---

### 1. Companion Reading Mode

**Pattern keywords:**
- "companion" AND (my review | my reading | my learning | this note)
- User has `<linked_note>` or `<editor_selection>` AND message contains "companion"

**Invoke:** `$ml-fundamentals-interview` with "companion" in args

**Natural language examples:**
- "Companion my review of transformers"
- "Companion my reading" *(with linked note)*
- "Companion this note"

---

### 2. Mock Interview Mode

**Pattern keywords:**
- (mock | interview simulation | interview practice) AND (ML | fundamental | concept | topic | transformers | attention | etc.)
- "mock ml fundamental"
- "run a mock"
- "simulate interview"

**Invoke:** `$ml-fundamentals-interview` with "mock" in args

**Natural language examples:**
- "Mock ML interview"
- "Mock me on transformers"
- "Run a mock fundamental interview"
- "Interview simulation on attention"

---

### 3. Practice/Drill Mode

**Pattern keywords:**
- (practice | drill | quiz me | test me | review) AND ML concept
- "practice ml fundamental"
- "drill on" + concept
- "quiz me"

**Invoke:** `$ml-fundamentals-interview` with "practice" in args

**Natural language examples:**
- "Quiz me on attention"
- "Practice transformers"
- "Drill me on LLM fundamentals"
- "Test my knowledge of RLHF"

---

### 4. Learn Mode (Explain with Immediate Answer)

**Pattern keywords:**
- (learn | understand | explain | what is | how does | why does) AND concept
- "learn ml fundamental"
- Question about ML concept (especially with linked note)

**Invoke:** `$ml-fundamentals-interview` with "learn" in args

**Natural language examples:**
- "Learn about attention mechanisms"
- "What is KV cache?"
- "Help me understand RLHF"
- "Explain how transformers work"

---

### 5. Teaching/Course Mode

**Pattern keywords:**
- (teach | course | deep dive | one-pager | comprehensive guide | lesson) AND concept
- "teach me" + concept
- "start a course on"
- "give me a one-pager"

**Invoke:** `$teach`

**Natural language examples:**
- "Teach me RLHF"
- "Start a course on diffusion models"
- "Give me a one-pager on RAG"
- "Deep dive into attention mechanisms"

---

### 6. System Design Interview

**Pattern keywords:**
- (design | architect | build | implement | structure) AND (system | recommendation | ranking | serving | infrastructure | rec system)
- "system design" AND (mock | practice | interview)
- "how would you design"

**Invoke:** `$ml-system-design-interview`

**Natural language examples:**
- "Design a recommendation system"
- "Practice ML system design"
- "How would you architect a ranking system?"
- "System design interview for serving"

---

### 7. Find Materials/References

**Pattern keywords:**
- (find | search | curate | locate | get | show me) AND (papers | references | materials | resources | sources)

**Invoke:** `$system-design-material-finder`

**Natural language examples:**
- "Find papers on RAG"
- "Curate references for model serving"
- "Get resources on LLM fine-tuning"
- "Show me papers about attention"

---

### 8. Prep Planning/Tracking

**Pattern keywords:**
- prep sprint | study plan | 1-week | one week | track progress | prep status | log study

**Invoke:** `$one-week-prep`

**Natural language examples:**
- "Prepare for ML breadth in 1 week"
- "Log today's study"
- "How am I doing on prep?"
- "Study plan for system design"

---

## Routing Logic

**Step 1: Extract context**
- Check for `<linked_note>` or `<editor_selection>` 
- Extract all keywords from user message
- Normalize to lowercase for matching

**Step 2: Pattern matching (priority order 1→8)**
- For each pattern above, check if ALL required keywords present
- On first match, invoke target skill immediately
- Pass full user request as args

**Step 3: Disambiguation rules**
- If multiple patterns match at same priority:
  - Note context present → favor companion/learn modes
  - No note + action verb → favor practice/mock modes
  - Teaching keywords present → favor teach over fundamentals
- State chosen mode in one sentence, don't re-ask

**Step 4: Default fallback**
- If NO pattern matches: invoke `$ml-fundamentals-interview` with "learn" as safe default
- Brief explanation: "Defaulting to learn mode for concept explanation."

**Step 5: Multi-skill requests**
- "Find papers on X then teach me" → Sequential: `$system-design-material-finder`, then `$teach`
- Execute in stated order, pass results forward

**Step 6: Explicit skill override**
- If user says "interview-ML" with NO further context → list available modes and ask preference
- Otherwise always auto-route based on patterns above

---

## Edge Cases

**Overlapping keywords:**

| User Input | Matches | Winner | Reason |
|------------|---------|--------|--------|
| "teach me X" + note context | teach (5), learn (4) | teach | Teaching mode explicit |
| "quiz me on X" | practice (3), learn (4) | practice | "quiz" is practice pattern |
| "companion" + "course" | companion (1), teach (5) | teach | "course" is stronger signal |
| "design" + "learn about" | system-design (6), learn (4) | system-design | Action verb wins |

**Context-based disambiguation:**
- `<linked_note>` present + "explain X" → learn mode (read-along Q&A)
- No note + "explain X" → teach mode (standalone lesson)

**Workflow keywords (pass to fundamentals):**
- "setup topic" → `$ml-fundamentals-interview` (detects Topic Prep workflow internally)
- "collect questions" → `$ml-fundamentals-interview` (detects Collect workflow)
- "solve questions" → `$ml-fundamentals-interview` (detects Solve workflow)
```

---

## Testing Phase 1

Run these test cases after updating `SKILL.md`:

```markdown
## Test Case Matrix

| # | User Input | Expected Skill | Expected Mode/Args | Pass? |
|---|------------|----------------|-------------------|-------|
| 1 | "quiz me on transformers" | ml-fundamentals-interview | practice | ⬜ |
| 2 | "mock ML interview" | ml-fundamentals-interview | mock | ⬜ |
| 3 | "companion my reading" *(with note)* | ml-fundamentals-interview | companion | ⬜ |
| 4 | "what is attention?" | ml-fundamentals-interview | learn | ⬜ |
| 5 | "teach me RLHF" | teach | (default) | ⬜ |
| 6 | "design a rec system" | ml-system-design-interview | (default) | ⬜ |
| 7 | "find papers on RAG" | system-design-material-finder | (default) | ⬜ |
| 8 | "drill me on LLMs" | ml-fundamentals-interview | practice | ⬜ |
| 9 | "explain KV cache" | ml-fundamentals-interview | learn | ⬜ |
| 10 | "start a course on transformers" | teach | (default) | ⬜ |
| 11 | "practice transformers" | ml-fundamentals-interview | practice | ⬜ |
| 12 | "help me understand RLHF" | ml-fundamentals-interview | learn | ⬜ |
| 13 | "one-pager on attention" | teach | (default) | ⬜ |
| 14 | "mock interview on LLMs" | ml-fundamentals-interview | mock | ⬜ |
| 15 | "prep for ML in 1 week" | one-week-prep | (default) | ⬜ |

## Edge Case Tests

| # | User Input | Context | Expected | Pass? |
|---|------------|---------|----------|-------|
| E1 | "explain attention" | `<linked_note>` present | ml-fundamentals learn | ⬜ |
| E2 | "explain attention" | No note | teach | ⬜ |
| E3 | "companion" + "course on X" | No note | teach | ⬜ |
| E4 | "quiz me" (no topic) | No note | ml-fundamentals practice | ⬜ |
| E5 | "interview-ML" (only) | No args | List modes + ask | ⬜ |
```

---

## Implementation Steps

1. **Backup current file:**
   ```bash
   cp interview-ML/SKILL.md interview-ML/SKILL.md.backup
   ```

2. **Apply changes:**
   - Replace lines 6-29 with new content above
   - Keep frontmatter (lines 1-5) unchanged

3. **Test with sample inputs:**
   - Run each test case from matrix
   - Check that routing matches expected skill

4. **Verify backward compatibility:**
   - Explicit calls like `$ml-fundamentals-interview` still work
   - Existing workflows not broken

5. **Commit:**
   ```bash
   git add interview-ML/SKILL.md
   git commit -m "feat(interview-ML): add smart router with fuzzy pattern matching

   - Natural language triggers: 'quiz me', 'mock interview', etc.
   - Priority-ordered pattern matching
   - Context-aware disambiguation
   - Backward compatible with explicit skill calls
   ```

---

## Rollback (if needed)

```bash
mv interview-ML/SKILL.md.backup interview-ML/SKILL.md
```
