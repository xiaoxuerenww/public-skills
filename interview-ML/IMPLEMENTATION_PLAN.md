# Implementation Plan: Option B - Smart Router + Mode Separation

**Selected Approach:** Incremental refactor with backward compatibility

---

## Final Structure (After All 3 Phases)

```
interview-ML/
├── SKILL.md                                    # Smart router with fuzzy matching (100 lines)
│
├── ml-fundamentals-interview/
│   ├── SKILL.md                                # Thin entry point, routes to modes (80 lines)
│   ├── modes/
│   │   ├── companion.md                        # Companion reading mode (~150 lines)
│   │   ├── learn.md                            # Learn mode (~180 lines)
│   │   ├── practice.md                         # Practice mode (~120 lines)
│   │   └── mock.md                             # Mock interview mode (~350 lines)
│   └── workflows/
│       ├── topic-prep.md                       # Topic directory setup (~100 lines)
│       ├── collect-questions.md                # Question bank building (~80 lines)
│       └── solve-questions.md                  # Answer key generation (~80 lines)
│
├── ml-system-design-interview/
│   └── SKILL.md                                # Keep as-is for now
│
├── teach/
│   └── SKILL.md                                # Keep as-is for now
│
├── system-design-material-finder/
│   └── SKILL.md                                # Keep as-is for now
│
├── one-week-prep/
│   └── SKILL.md                                # Keep as-is for now
│
└── shared/
    ├── note-formats.md                         # Common note-taking formats
    ├── source-paths.md                         # File path configurations
    └── session-cleanup.md                      # Shared wrap-up logic
```

---

## Phase 1: Smart Router (Quick Win)

**Goal:** Improve top-level routing with natural language support
**Breaking Changes:** None
**Time Estimate:** 30 minutes

### Changes:

#### 1.1 Update `interview-ML/SKILL.md`

**Current routing (lines 12-20):**
```markdown
| Request pattern | Invoke skill | Examples |
|----------------|-------------|----------|
| Companion reading/review/learning, annotate a note with Q&A | `$ml-fundamentals-interview` | "Companion my review" |
| Theory, fundamentals, quiz, drill, learn/practice/mock on ML concepts | `$ml-fundamentals-interview` | "Quiz me on attention" |
| System design, architecture, ranking, recommendation, serving, infra | `$ml-system-design-interview` | "Design a recommendation system" |
| Explain, teach, learn a concept, one-pager, course | `$teach` | "Teach me RLHF" |
| Find references, papers, materials for a topic | `$system-design-material-finder` | "Find papers on RAG" |
| Prep sprint, study plan, 1-week prep, track progress, prep status | `$one-week-prep` | "Prepare for ML breadth in 1 week" |
```

**New routing (with fuzzy matching):**
```markdown
## Smart Routing with Pattern Matching

**Check patterns in priority order (first match wins):**

### 1. Companion Reading Mode
**Triggers:** 
- "companion" + (my review | my reading | my learning | this note)
- User has `<linked_note>` or `<editor_selection>` AND says "companion"

**Action:** `$ml-fundamentals-interview companion`

**Examples:**
- "Companion my review of transformers"
- "Companion my reading" (with linked note)

---

### 2. Mock Interview Mode
**Triggers:**
- (mock | interview simulation | interview practice) + (ML | fundamental | concept | topic)
- "mock ml fundamental"
- "run a mock" + (ML concept present)

**Action:** `$ml-fundamentals-interview mock`

**Examples:**
- "Mock ML interview"
- "Mock me on transformers"
- "Run a mock fundamental interview"

---

### 3. Practice/Drill Mode
**Triggers:**
- (practice | drill | quiz me | test me) + ML concept
- "practice ml fundamental"
- "drill on" + concept

**Action:** `$ml-fundamentals-interview practice`

**Examples:**
- "Quiz me on attention"
- "Practice transformers"
- "Drill me on LLM fundamentals"

---

### 4. Learn Mode (Explain with Immediate Answer)
**Triggers:**
- (learn | understand | explain simply | what is) + ML concept
- "learn ml fundamental"
- Question about a concept (with `<linked_note>`)

**Action:** `$ml-fundamentals-interview learn`

**Examples:**
- "Learn about attention mechanisms"
- "What is KV cache?"
- "Help me understand RLHF"

---

### 5. Teaching/Course Mode
**Triggers:**
- (teach | course | deep dive | one-pager | comprehensive) + concept
- "teach me" + concept
- "start a course on" + topic

**Action:** `$teach`

**Examples:**
- "Teach me RLHF"
- "Start a course on diffusion models"
- "Give me a one-pager on RAG"

---

### 6. System Design Interview
**Triggers:**
- (design | architect | build | implement) + (system | recommendation | ranking | serving | infra)
- "system design" + (mock | practice | interview)

**Action:** `$ml-system-design-interview`

**Examples:**
- "Design a recommendation system"
- "Practice ML system design"
- "How would you architect a ranking system?"

---

### 7. Find Materials/References
**Triggers:**
- (find | search | curate | locate | get) + (papers | references | materials | resources | sources)

**Action:** `$system-design-material-finder`

**Examples:**
- "Find papers on RAG"
- "Curate references for model serving"
- "Get resources on LLM fine-tuning"

---

### 8. Prep Planning/Tracking
**Triggers:**
- (prep sprint | study plan | 1-week | one week | track progress | prep status)

**Action:** `$one-week-prep`

**Examples:**
- "Prepare for ML breadth in 1 week"
- "Log today's study"
- "How am I doing on prep?"

---

### Workflow Triggers (pass through to ml-fundamentals-interview)

**Topic Setup:**
- (setup | prepare | initialize | refresh) + (topic | directory)
- Pass through: `$ml-fundamentals-interview` with workflow flag

**Question Collection:**
- (collect | extract | consolidate | build) + (questions | question bank)
- Pass through: `$ml-fundamentals-interview` with workflow flag

**Answer Key Generation:**
- (solve | answer | create solutions | generate answer key) + (mock_question_bank | solution.md)
- Pass through: `$ml-fundamentals-interview` with workflow flag

---

## Routing Rules

1. **Read user message AND context** (`<linked_note>`, `<editor_selection>`)
2. **Match patterns in priority order** (1→8)
3. **On first match:** Invoke target skill immediately with full user request
4. **On ambiguity:** Pick most likely based on context:
   - Note context present → favor companion/learn
   - No note context + question word → favor learn
   - No note context + action word → favor practice/mock
5. **On no match:** Invoke `$ml-fundamentals-interview learn` as safe default
6. **Never re-ask** what the user wants unless genuinely ambiguous between two skills

---

## Edge Case Handling

**Overlapping keywords:**
- "teach me X" + note context → `$teach` (teaching wins over companion)
- "quiz me" + "design" → `$practice` first, then can pivot to system design
- "companion" + "course" → `$teach companion` (teach skill has companion mode)

**Multi-skill requests:**
- "Find papers on RAG then teach me" → Sequential: `$system-design-material-finder`, then `$teach`
- "Design a rec system and mock interview" → Sequential: `$ml-system-design-interview`, then `$ml-fundamentals-interview mock`
```

### Testing Phase 1:
```markdown
## Test Cases for Smart Router

| User Input | Expected Route | Reason |
|------------|---------------|---------|
| "quiz me on transformers" | ml-fundamentals-interview practice | "quiz me" pattern |
| "mock ML interview" | ml-fundamentals-interview mock | "mock" + "ML" pattern |
| "companion my reading" (with note) | ml-fundamentals-interview companion | "companion" + note context |
| "what is attention?" | ml-fundamentals-interview learn | "what is" question pattern |
| "teach me RLHF" | teach | "teach me" pattern |
| "design a rec system" | ml-system-design-interview | "design" + "system" pattern |
| "find papers on RAG" | system-design-material-finder | "find" + "papers" pattern |
| "drill me on LLMs" | ml-fundamentals-interview practice | "drill" pattern |
| "explain KV cache" | ml-fundamentals-interview learn | "explain" pattern |
| "start a course on transformers" | teach | "course" pattern |
```

---

## Phase 2: Split ml-fundamentals-interview into Modes

**Goal:** Break 936-line monolith into focused mode files
**Breaking Changes:** None (internal refactor only)
**Time Estimate:** 1-2 hours

### Changes:

#### 2.1 Create mode files

**New file: `ml-fundamentals-interview/modes/companion.md`**
- Extract lines 159-227 from current SKILL.md
- Add frontmatter:
```markdown
---
# Companion Mode - ML Fundamentals Interview Prep
# Annotate notes with Q&A while reading
---

## Companion Mode

Triggered by "companion", "companion my review", "companion my reading", or
"companion my learning".

[... rest of companion mode content ...]
```

**New file: `ml-fundamentals-interview/modes/learn.md`**
- Extract lines 220-305 from current SKILL.md
- Add frontmatter and shared logic includes

**New file: `ml-fundamentals-interview/modes/practice.md`**
- Extract lines 307-327 from current SKILL.md

**New file: `ml-fundamentals-interview/modes/mock.md`**
- Extract lines 569-859 from current SKILL.md

#### 2.2 Create workflow files

**New file: `ml-fundamentals-interview/workflows/topic-prep.md`**
- Extract "Topic Prep" section (lines 329-407)

**New file: `ml-fundamentals-interview/workflows/collect-questions.md`**
- Extract "Collect Question Mode" section (lines 394-491)

**New file: `ml-fundamentals-interview/workflows/solve-questions.md`**
- Extract "Solve Mode" section (lines 493-568)

#### 2.3 Update `ml-fundamentals-interview/SKILL.md`

**New content (80 lines):**
```markdown
---
name: ml-fundamentals-interview
description: ML/LLM fundamentals interview prep. Includes companion reading, learn, practice, mock modes, plus topic setup workflows.
---

# ML/LLM Fundamentals Interview Prep

Routes to the appropriate mode or workflow based on user request.

## Available Modes

- **Companion Mode:** Annotate notes with Q&A while reading
- **Learn Mode:** Explain concepts with immediate answers
- **Practice Mode:** Guided practice with keyword-level feedback
- **Mock Mode:** Full mock interview with grading and tracking

## Available Workflows

- **Topic Prep:** Set up topic directories with question banks
- **Collect Questions:** Build question banks from sources
- **Solve Questions:** Generate answer keys for question banks

## Source Files

Mock sessions saved to: `<topic_dir>/mock.md`
Default question bank: `~/Documents/work/0_databricks/0_db_ml_fundamental/0_db_ml_fundamentals_question_bank.md`

## Mode Detection

**Priority order:**

1. **Explicit mode in args:**
   - If args contain "companion" → include `modes/companion.md`
   - If args contain "learn" → include `modes/learn.md`
   - If args contain "practice" → include `modes/practice.md`
   - If args contain "mock" → include `modes/mock.md`

2. **Context-based:**
   - `<linked_note>` or `<editor_selection>` present + "companion" → companion mode
   - `<linked_note>` or `<editor_selection>` present, no mode specified → learn mode
   - No note context + (quiz | drill | practice) → practice mode
   - No note context + "mock" → mock mode
   - Default: learn mode

3. **Workflow detection:**
   - (setup | prepare | initialize | refresh) + topic → include `workflows/topic-prep.md`
   - (collect | extract | consolidate) + questions → include `workflows/collect-questions.md`
   - (solve | answer | generate) + (solution | answer key) → include `workflows/solve-questions.md`

## Mode Includes

Based on detection above, include the appropriate mode file(s):

{%- if mode == "companion" -%}
{% include "modes/companion.md" %}
{%- elif mode == "learn" -%}
{% include "modes/learn.md" %}
{%- elif mode == "practice" -%}
{% include "modes/practice.md" %}
{%- elif mode == "mock" -%}
{% include "modes/mock.md" %}
{%- endif -%}

{%- if workflow == "topic-prep" -%}
{% include "workflows/topic-prep.md" %}
{%- elif workflow == "collect-questions" -%}
{% include "workflows/collect-questions.md" %}
{%- elif workflow == "solve-questions" -%}
{% include "workflows/solve-questions.md" %}
{%- endif -%}
```

**Note:** The actual implementation will use the skill framework's include mechanism. If includes aren't supported, we'll use a simple routing approach that reads and follows the appropriate mode file inline.

---

## Phase 3: Extract Shared Logic

**Goal:** DRY up repeated sections across modes
**Breaking Changes:** None
**Time Estimate:** 30 minutes

### Changes:

#### 3.1 Create shared files

**New file: `shared/note-formats.md`**
```markdown
# Common Note-Taking Formats

## Practice/Mock Question Format

```markdown
## <question text>

- Asked: <timestamp>
- Verdict: `<pass|fail>`
- Topic: <topic>
- Raw answer:
  > <the user's answer verbatim when available>
- Misses:
  - <specific missing/wrong/vague point>
- Feedback: <direct critique>
- Ideal answer: <full chat response verbatim — complete explanation, not a summary>
- Drill next: <specific next target>
```

## Learn Notes Format

```markdown
### Q: {user question}

**Raw user answer:** {verbatim when available}

**A:** {concise answer with core concept}

**Key equations:** {LaTeX display math}

**Mental model:** {what to remember}

**Interview phrasing:** {crisp one-sentence version}

**Grounding:** {source reference}
```

[... other common formats ...]
```

**New file: `shared/source-paths.md`**
```markdown
# Source File Paths

## Databricks ML Fundamentals

**Question bank:**
```
~/Documents/work/0_databricks/0_db_ml_fundamental/0_db_ml_fundamentals_question_bank.md
```

**Core references:**
```
~/Documents/work/0_databricks/0_db_ml_fundamental/2_ml-llm-fundamentals.md
~/Documents/work/0_databricks/0_db_ml_fundamental/2_ml-llm-fundamentals-QUIZ.md
~/Documents/work/0_databricks/0_db_ml_fundamental/2_ml-llm-fundamentals-ANSWERS.md
```

## Topic Directory Resolution

1. If user provides topic directory, use it
2. If user provides file, walk up to nearest directory with:
   - `mock_question_bank.md`
   - `mock.md`
   - `index.md`
   - `solution.md`
   - `deep_dive.md`
3. If no explicit topic, use current directory only if it's a topic directory
4. On ambiguity, ask one clarification question
```

**New file: `shared/session-cleanup.md`**
```markdown
# Session Wrap-Up Cleanup

**Trigger signals:**
- "wrap up", "done for now", "end session", "finish"
- "stop here", "summarize session"
- "end learn", "conclude learn", "exit learn"
- "wrap learning", "finish learning"
- Explicit request to clean or consolidate notes

**Workflow:**

1. **Finish mode-specific persistence first:**
   - Practice Mode: save latest feedback/weakness notes
   - Learn Mode: append useful Q&A to `learn_notes.md`
   - Mock Mode: update `mock.md` and `mock_tracker.md`

2. **Resolve active `topic_dir`** (use Topic Prep path rules)

3. **If both `learn_notes.md` AND `deep_dive.md` exist:**
   - Invoke `$file-cleaner`
   - Consolidate `learn_notes.md` → `deep_dive.md`
   - Regroup basic→advanced
   - Remove duplicates
   - Leave `learn_notes.md` as lightweight buffer

4. **If either file missing:**
   - Skip cleanup
   - Mention which file is missing

5. **Report:**
   - Mode wrap-up artifacts saved
   - File-cleaner result (if run)
   - Next review suggestions
```

#### 3.2 Update mode files to reference shared logic

In each mode file, replace duplicated sections with:
```markdown
For note-taking format, see [[shared/note-formats.md]].
For source paths, see [[shared/source-paths.md]].
For wrap-up workflow, see [[shared/session-cleanup.md]].
```

---

## Migration Checklist

### Phase 1: Smart Router
- [ ] Update `interview-ML/SKILL.md` with fuzzy pattern matching
- [ ] Add natural language trigger examples
- [ ] Test with 10 sample user inputs
- [ ] Verify backward compatibility with explicit `$skill-name` calls

### Phase 2: Mode Separation
- [ ] Create `ml-fundamentals-interview/modes/` directory
- [ ] Extract and create `companion.md`
- [ ] Extract and create `learn.md`
- [ ] Extract and create `practice.md`
- [ ] Extract and create `mock.md`
- [ ] Create `ml-fundamentals-interview/workflows/` directory
- [ ] Extract and create `topic-prep.md`
- [ ] Extract and create `collect-questions.md`
- [ ] Extract and create `solve-questions.md`
- [ ] Update `ml-fundamentals-interview/SKILL.md` to route to mode files
- [ ] Test each mode independently
- [ ] Verify all mode transitions work

### Phase 3: Shared Logic
- [ ] Create `shared/` directory
- [ ] Create `note-formats.md`
- [ ] Create `source-paths.md`
- [ ] Create `session-cleanup.md`
- [ ] Update mode files to reference shared docs
- [ ] Test cross-references work
- [ ] Remove duplicated content from mode files

### Final Validation
- [ ] Test all natural language triggers
- [ ] Test all explicit mode invocations
- [ ] Test workflow triggers (topic prep, collect, solve)
- [ ] Test mode transitions (learn→practice, practice→mock)
- [ ] Test wrap-up/cleanup across all modes
- [ ] Verify no regressions in existing functionality

---

## Rollback Plan

**If issues found in Phase 1:**
- Revert `interview-ML/SKILL.md` to previous version
- No other files affected

**If issues found in Phase 2:**
- Revert `ml-fundamentals-interview/SKILL.md`
- Delete `modes/` and `workflows/` directories
- Original monolithic SKILL.md remains as backup

**If issues found in Phase 3:**
- Delete `shared/` directory
- Restore full content to mode files
- No functional change, just duplicated content

---

## Timeline

**Phase 1:** 30 min
**Phase 2:** 1-2 hours
**Phase 3:** 30 min
**Testing:** 30 min

**Total:** 3-4 hours (can split across multiple sessions)

---

## Success Metrics

**After Phase 1:**
- ✅ "quiz me on X" triggers practice mode directly
- ✅ "mock interview" triggers mock mode directly
- ✅ Natural variations work without exact phrase matching

**After Phase 2:**
- ✅ Each mode file < 400 lines
- ✅ Clear separation: modes vs workflows
- ✅ Easier to maintain/update individual modes

**After Phase 3:**
- ✅ No duplicated logic across mode files
- ✅ Single source of truth for formats, paths, cleanup
- ✅ Easy to update note formats globally
