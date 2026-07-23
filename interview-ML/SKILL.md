---
name: interview-ML
description: "End-to-end Staff+ MLE interview prep: ML fundamentals quizzes, system design, concept teaching, and reference finding. Routes to the right sub-skill based on request type."
argument-hint: "What would you like to work on? (e.g., 'quiz me on transformers', 'design a rec system', 'teach me RLHF')"
---

# ML Interview Prep Router

Route the user's request to the appropriate sub-skill using pattern matching. Read the user's message, context, and classify with priority-ordered patterns.

## Pattern Matching (Priority Order)

Check patterns from top to bottom. **First match wins.**

### 1. Companion Reading Mode

**Pattern keywords:**
- "companion" AND (my review | my reading | my learning | this note)
- User has `<linked_note>` or `<editor_selection>` AND message contains "companion"

**Invoke:** `$ml-fundamentals-interview` with "companion" in args

**Natural language examples:**
- "Companion my review of transformers"
- "Companion my reading" *(with linked note)*
- "Companion this note"

### 2. Mock Interview Mode

**Pattern keywords:**
- (mock | interview simulation | interview practice) AND (ML | fundamental | concept | topic)
- "mock ml fundamental"
- "run a mock" OR "simulate interview"

**Invoke:** `$ml-fundamentals-interview` with "mock" in args

**Natural language examples:**
- "Mock ML interview"
- "Mock me on transformers"
- "Run a mock fundamental interview"
- "Interview simulation on attention"

### 3. Practice/Drill Mode

**Pattern keywords:**
- (practice | drill | quiz me | test me | review) AND ML concept
- "practice ml fundamental"
- "drill on" + concept

**Invoke:** `$ml-fundamentals-interview` with "practice" in args

**Natural language examples:**
- "Quiz me on attention"
- "Practice transformers"
- "Drill me on LLM fundamentals"
- "Test my knowledge of RLHF"

### 4. Learn Mode (Explain with Immediate Answer)

**Pattern keywords:**
- (learn | understand | explain | what is | how does | why does) AND concept
- "learn ml fundamental"
- Question about ML concept

**Invoke:** `$ml-fundamentals-interview` with "learn" in args

**Natural language examples:**
- "Learn about attention mechanisms"
- "What is KV cache?"
- "Help me understand RLHF"
- "Explain how transformers work"

### 5. Teaching/Course Mode

**Pattern keywords:**
- (teach | course | deep dive | one-pager | comprehensive) AND concept
- "teach me" + concept
- "start a course on" OR "give me a one-pager"

**Invoke:** `$teach`

**Natural language examples:**
- "Teach me RLHF"
- "Start a course on diffusion models"
- "Give me a one-pager on RAG"
- "Deep dive into attention mechanisms"

### 6. System Design Interview

**Pattern keywords:**
- (design | architect | build | implement) AND (system | recommendation | ranking | serving | infrastructure)
- "system design" AND (mock | practice | interview)
- "how would you design"

**Invoke:** `$ml-system-design-interview`

**Natural language examples:**
- "Design a recommendation system"
- "Practice ML system design"
- "How would you architect a ranking system?"

### 7. Find Materials/References

**Pattern keywords:**
- (find | search | curate | locate | get | show me) AND (papers | references | materials | resources)

**Invoke:** `$system-design-material-finder`

**Natural language examples:**
- "Find papers on RAG"
- "Curate references for model serving"
- "Get resources on LLM fine-tuning"

### 8. Prep Planning/Tracking

**Pattern keywords:**
- prep sprint | study plan | 1-week | one week | track progress | prep status | log study

**Invoke:** `$one-week-prep`

**Natural language examples:**
- "Prepare for ML breadth in 1 week"
- "Log today's study"
- "How am I doing on prep?"

## Routing Logic

**Step 1: Extract context**
- Check for `<linked_note>` or `<editor_selection>`
- Extract keywords from user message
- Normalize to lowercase for matching

**Step 2: Pattern matching (priority order 1→8)**
- For each pattern above, check if required keywords present
- On first match, invoke target skill immediately
- Pass full user request as args

**Step 3: Disambiguation**
- If multiple patterns match:
  - Note context present → favor companion/learn modes
  - No note + action verb → favor practice/mock modes
  - Teaching keywords → favor teach over fundamentals
- State chosen mode in one sentence

**Step 4: Default fallback**
- If NO pattern matches: invoke `$ml-fundamentals-interview` with "learn" mode
- Brief explanation: "Defaulting to learn mode."

**Step 5: Multi-skill requests**
- "Find papers on X then teach me" → Sequential execution
- Execute in stated order

**Step 6: No-context invocation**
- If user says "interview-ML" with NO further context → list available modes and ask
