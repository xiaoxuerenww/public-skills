# Interview-ML Structure Improvement Proposal

**Goal:** Make interview-ML triggering more direct, intuitive, and efficient by reducing indirection and improving mode detection.

---

## Current Issues

### 1. **Multi-layer Routing Indirection**
- User → `interview-ML` router → sub-skill router → mode detection
- Example: "quiz me on transformers" → `interview-ML` → `ml-fundamentals-interview` → Mode Routing section → Companion/Learn/Practice/Mock mode
- **Problem:** 3 levels of routing for simple requests

### 2. **Verbose Trigger Phrases**
Current triggers are overly specific:
- ❌ "learn ml fundamental" (exact phrase required)
- ❌ "practice ml fundamental" (exact phrase required)  
- ❌ "mock ml fundamental" (exact phrase required)
- **Problem:** Natural variations fail ("learn about attention", "practice transformers")

### 3. **Mode Routing Buried in Long Files**
- `ml-fundamentals-interview/SKILL.md`: 936 lines
- Mode routing section at line 64
- Mode descriptions scattered throughout
- **Problem:** Hard to maintain, easy to miss routing logic

### 4. **Ambiguous Overlaps**
- "companion" → could be fundamentals or teach
- "quiz me" → unclear if learn/practice/mock mode
- "teach me X" → unclear if quick concept or course
- **Problem:** Requires disambiguation logic at multiple levels

---

## Proposed Structure

### **Option A: Flatten Sub-Skills into Top-Level Modes**

```
interview-ML/
├── SKILL.md                          # Simplified router (50-100 lines)
├── modes/
│   ├── companion.md                  # Companion reading mode
│   ├── learn.md                      # Learn mode (show answer immediately)
│   ├── practice.md                   # Practice mode (guided feedback)
│   ├── mock.md                       # Mock interview mode
│   ├── teach.md                      # Teaching/course mode
│   ├── system-design.md             # System design interview
│   └── material-finder.md           # Find references/papers
├── workflows/
│   ├── topic-prep.md                # Setup topic directories
│   ├── collect-questions.md         # Build question banks
│   └── solve-questions.md           # Generate answer keys
└── references/
    ├── fundamentals-sources.md
    └── system-design-framework.md
```

**Routing in SKILL.md:**
```markdown
## Direct Mode Detection

**Keyword Priority (first match wins):**
1. "companion" + (reading|review|learning) → `modes/companion.md`
2. "mock" + (fundamental|ML|interview) → `modes/mock.md`
3. "practice" + concept → `modes/practice.md`
4. "learn" + concept → `modes/learn.md`
5. "teach" + concept → `modes/teach.md`
6. "design" + (system|architecture|rec) → `modes/system-design.md`
7. "find" + (papers|references|materials) → `modes/material-finder.md`
8. "quiz me" → smart default based on context

**Workflow Detection:**
- "setup topic" → `workflows/topic-prep.md`
- "collect questions" → `workflows/collect-questions.md`
- "solve questions" → `workflows/solve-questions.md`
```

**Benefits:**
- ✅ Single routing layer
- ✅ Clear separation: modes vs workflows
- ✅ Each mode file is focused (200-300 lines)
- ✅ Easy to add new modes

**Drawbacks:**
- ⚠️ Breaks existing skill invocations like `$ml-fundamentals-interview`
- ⚠️ Requires migrating 936 lines of mode logic


### **Option B: Keep Sub-Skills, Improve Router Efficiency**

Keep current structure but improve routing:

```
interview-ML/
├── SKILL.md                          # Smart router with pattern matching
├── ml-fundamentals-interview/
│   ├── SKILL.md                      # Entry point (50 lines)
│   └── modes/
│       ├── companion.md
│       ├── learn.md
│       ├── practice.md
│       └── mock.md
├── ml-system-design-interview/
│   └── SKILL.md
├── teach/
│   └── SKILL.md
└── one-week-prep/
    └── SKILL.md
```

**New `interview-ML/SKILL.md`:**
```markdown
## Smart Routing with Fuzzy Matching

**Pattern Matching (priority order):**

1. **Companion Mode:** companion + (my review|reading|learning|this note)
   → `$ml-fundamentals-interview companion`

2. **Mock Interview:** (mock|interview simulation) + (ml|fundamental|concept)
   → `$ml-fundamentals-interview mock`

3. **Practice Drills:** (practice|drill|quiz me) + concept
   → `$ml-fundamentals-interview practice`

4. **Learn Mode:** (learn|understand|explain simply) + concept
   → `$ml-fundamentals-interview learn`

5. **Teach/Course:** (teach|course|deep dive|one-pager) + concept
   → `$teach`

6. **System Design:** (design|architect|build) + (system|rec system|ranking)
   → `$ml-system-design-interview`

7. **Find Materials:** (find|search|curate) + (papers|references|resources)
   → `$system-design-material-finder`

**Simplified Sub-Skill Entry Points:**
- `ml-fundamentals-interview/SKILL.md`: Just route to mode files, no 936-line monolith
- Each mode in separate file under `modes/`
```

**Benefits:**
- ✅ Maintains existing skill structure
- ✅ Adds fuzzy matching for natural language
- ✅ Separates mode logic into focused files
- ✅ Backward compatible with explicit `$skill-name` calls

**Drawbacks:**
- ⚠️ Still two routing layers (but second is faster)
- ⚠️ Need to split large SKILL.md files


### **Option C: Hybrid - Smart Defaults with Explicit Overrides**

```
interview-ML/
├── SKILL.md                          # Main entry with smart defaults
├── fundamentals/                     # Renamed from ml-fundamentals-interview
│   ├── companion.md
│   ├── learn.md
│   ├── practice.md
│   ├── mock.md
│   └── workflows/
│       ├── topic-prep.md
│       ├── collect-questions.md
│       └── solve-questions.md
├── system-design/
│   └── SKILL.md
├── teach/
│   └── SKILL.md
└── shared/
    ├── note-formats.md
    └── source-paths.md
```

**Smart Routing Logic:**
```markdown
## Context-Aware Mode Detection

**Primary Detection (examine user message + context):**

If linked_note or editor_selection present:
  - Contains "companion" → fundamentals/companion.md
  - Otherwise → fundamentals/learn.md (default for reading context)

If no note context:
  - "mock" in message → fundamentals/mock.md
  - "practice" or "drill" → fundamentals/practice.md
  - "design a" or "architecture" → system-design/SKILL.md
  - "teach me" or "explain" → teach/SKILL.md
  - Default: fundamentals/learn.md

**Explicit Overrides:**
User can force a mode with:
- `/interview-ML mock` → fundamentals/mock.md
- `/interview-ML practice` → fundamentals/practice.md
- `/interview-ML teach` → teach/SKILL.md
```

**Benefits:**
- ✅ Context-aware (note presence → companion/learn)
- ✅ Natural language works ("quiz me", "practice", "mock interview")
- ✅ Explicit overrides for power users
- ✅ Cleaner folder names

**Drawbacks:**
- ⚠️ Folder rename breaks existing references
- ⚠️ Context inference might guess wrong occasionally

---

## Recommendation: **Option B** (Smart Router + Mode Separation)

**Why:**
1. **Minimal breaking changes** - keeps existing skill names
2. **Immediate benefit** - fuzzy matching improves UX now
3. **Incremental refactor** - can split mode files gradually
4. **Maintains compatibility** - explicit `$skill` calls still work

**Implementation Plan:**

### Phase 1: Improve Router (No Breaking Changes)
1. Update `interview-ML/SKILL.md` with fuzzy pattern matching
2. Add natural language triggers: "quiz me", "drill me", "mock interview"
3. Test with common user phrases

### Phase 2: Split Large Skill Files
1. Create `ml-fundamentals-interview/modes/` directory
2. Extract modes to separate files:
   - `companion.md` (lines 161-227)
   - `learn.md` (lines 228-319)
   - `practice.md` (lines 320-346)
   - `mock.md` (lines 590-859)
3. Update `ml-fundamentals-interview/SKILL.md` to include mode files

### Phase 3: Consolidate Common Logic
1. Create `shared/` directory
2. Extract repeated sections:
   - Note-taking formats
   - Source file paths
   - Session wrap-up logic
3. Include from mode files

---

## Example: Before vs After

### Before (Current):
```
User: "quiz me on transformers"
  ↓ interview-ML/SKILL.md (router)
  ↓ "Theory, fundamentals, quiz" → ml-fundamentals-interview
  ↓ ml-fundamentals-interview/SKILL.md (936 lines)
  ↓ Mode Routing section (line 64)
  ↓ Check for "learn", "practice", "mock" keywords
  ↓ Default to Learn Mode (line 228)
```

### After (Option B):
```
User: "quiz me on transformers"
  ↓ interview-ML/SKILL.md (smart router, 100 lines)
  ↓ Pattern match: "quiz me" + concept → practice mode
  ↓ ml-fundamentals-interview/modes/practice.md (80 lines)
  ✓ Start practice mode directly
```

**Steps reduced:** 6 → 3  
**Lines to parse:** 936 → 180  
**Natural language support:** ✅

---

## Questions for Review

1. **Prefer Option A, B, or C?** (or suggest Option D)
2. **Breaking changes acceptable?** (rename folders, skill names)
3. **Priority:**
   - Quick win (Phase 1 only)?
   - Full refactor (all 3 phases)?
   - Hybrid approach?
4. **Mode naming preferences:**
   - Keep "ml-fundamentals-interview" or shorten to "fundamentals"?
   - Keep "teach" or rename to "concepts"?
5. **Additional modes needed?**
   - Behavioral interview prep?
   - Coding interview (ML-specific)?

---

## Next Steps After Review

Once you choose an option, I will:
1. Create detailed file-by-file implementation plan
2. Show exact changes (diffs) for your approval
3. Implement incrementally with testing after each phase
4. Update documentation and examples
