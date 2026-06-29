---
name: coding-interview-companion
description: "End-to-end coding interview prep for algorithms, data structures, and practical coding rounds. Use when preparing technical interview problems in solve, learn, practice, or mock mode: first locate the current problem directory, read and analyze raw source material from context/, generate comprehensive candidate-facing requirements and starter code under input/, use solution/ for study artifacts, use dated practice_MMDD/ directories for first-pass implementation drills with interface and tests only, and use dated mock_MMDD/ directories for mock interview sessions. Solve mode analyzes context/ and writes input/0_requirements.md plus starter files before creating solution artifacts, learn mode defaults to interactive Q&A with comprehensive session notes under solution/ and wrap-up-only grouped consolidation, practice mode creates a fresh implementation sandbox with public interface stubs and unit tests while leaving implementation to the user, and mock mode simulates an interviewer and reviews the user's attempt under a fresh mock_MMDD/ directory."
---

# Coding Interview Companion

**Purpose:** Complete lifecycle support for coding interview prep, from requirements analysis through solution writing, learning review, and mock interviews.

**Important:** First identify the current problem directory. All `context/`, `input/`, `output/`, `solution/`, `practice_MMDD/`, and `mock_MMDD/` paths are subdirectories of that problem directory, not necessarily the shell's current directory.

## Problem Directory Resolution

Before reading or writing files, set `problem_dir`:

1. If the user provides a problem directory or file path, use that directory. If they provide a file inside `context/`, `input/`, `solution/`, `mock_MMDD/`, or legacy `output/`/`mock/`, walk upward to the nearest directory that contains the problem's artifact folders.
2. Otherwise, if the current directory contains `context/`, `input/`, `solution/`, `mock_MMDD/`, or legacy `output/`/`mock/`, use the current directory.
3. Otherwise, search nearby child directories for `context/`, `input/0_requirements.md`, `input/*.md`, `solution/deep_dive.md`, or legacy `output/deep_dive.md` and choose the directory that matches the current problem context.
4. If multiple directories match and the current problem is ambiguous, ask one concise clarification question.

After resolving `problem_dir`, use:
- `problem_context = <problem_dir>/context`
- `problem_input = <problem_dir>/input`
- `problem_solution_output = <problem_dir>/solution`
- `problem_practice_output = <problem_dir>/practice_MMDD` where `MMDD` is the current date, e.g. `practice_0602`
- `problem_mock_output = <problem_dir>/mock_MMDD` where `MMDD` is the current date, e.g. `mock_0602`

Create `problem_input` and the selected mode's artifact directory if needed and they do not exist. Treat `context/` as the raw source folder when present; do not overwrite raw context files. In practice and mock mode, create a new dated top-level directory for each session.

## Quick Setup

1. **Create a directory** for your interview prep:
   ```bash
   mkdir my-interview-prep
   cd my-interview-prep
   ```

2. **Create context folder and raw notes file:**
   ```bash
   mkdir context
   echo "# Raw Interview Context
   - Type: Coding + System Design + Behavioral
   - Date: June 2026
   - Focus areas: algorithms, data structures
   " > context/raw_notes.md
   ```

3. **Invoke the skill** from this directory or pass the problem directory explicitly:
   ```
   /coding-interview-companion
   
   "Solve mode for ./my-interview-prep"
   ```

## Directory Structure

All paths are **relative to the resolved problem directory**:

```
problem-directory/
  context/
    ...                         # Raw source material: prompt dumps, notes, screenshots, copied starter code, interview docs
  input/
    0_requirements.md          # Comprehensive candidate-facing requirements synthesized from context/ by solve mode
    next_round_mock_questions.md # Follow-up drills generated from prior mock misses and weaknesses
    <problem_name>.md          # Clean problem statement derived from context/
    <problem_name>.ipynb       # Starter notebook/interface derived from context/ for Colab rounds
    <problem_name>.py          # Optional starter Python fallback/export when useful
  solution/
    interview_discussion.md         # Interview-ready answers (created by solve mode)
    <problem_name>_solution.ipynb   # Full Colab reference solution (created by solve mode for Colab rounds)
    <problem_name>_solution.py      # Optional Python fallback/export when useful
    deep_dive.md                    # Broader concepts and deep dives (created/updated by solve and learn)
    learn_notes.md                  # Learning session notes (created by learn mode, merged into deep_dive)
  practice_MMDD/
    practice_instructions.md        # Candidate-facing prompt and implementation contract (created in practice mode)
    practice_<problem_name>.py      # Public interface scaffold for user implementation (created in practice mode)
    test_practice_<problem_name>.py # Unit tests for the user implementation (created in practice mode)
  mock_MMDD/
    mock_instructions.md           # Candidate-facing prompt and constraints (created in mock mode)
    mock_<problem_name>_<part>.ipynb # Colab mock scaffold and user attempt (created in mock mode for Colab rounds)
    mock_feedback.md                # Mock interview feedback (created by mock mode)
```

The skill will:
- **Resolve:** `problem_dir` before any file operation
- **Read raw source from:** all relevant files under `<problem_dir>/context/`, including prompt dumps, question lists, starter code, notebooks, screenshots converted to text, and named files from the user request
- **Write generated input artifacts to:** `<problem_dir>/input/`, including a comprehensive `input/0_requirements.md` and candidate-facing starter code
- **Write solve outputs to:** `<problem_dir>/solution/`
- **Write practice outputs to:** `<problem_dir>/practice_MMDD/`
- **Write mock outputs to:** `<problem_dir>/mock_MMDD/`
- **Write learn notes to:** `<problem_dir>/solution/learn_notes.md`
- **Create directories** if they don't exist
- **Clean duplicate setup files:** after setup, remove legacy duplicate files only when the same raw source is preserved in `context/` or the same generated artifact is preserved in `input/` / `solution/`

## Modes

All paths are relative to the resolved `problem_dir`:

- **Solve mode:** Read and analyze raw information from `<problem_dir>/context/`, create a comprehensive requirements doc and frozen starter files under `<problem_dir>/input/`, then generate `<problem_dir>/solution/interview_discussion.md`, `<problem_dir>/solution/<problem_name>_solution.ipynb` for Colab rounds, and `<problem_dir>/solution/deep_dive.md`.
- **Learn mode:** Default to interactive Q&A: answer the user's immediate interview-prep questions, ask targeted follow-ups when useful, proactively take raw chronological notes of interview-relevant questions and responses in `<problem_dir>/solution/learn_notes.md` during the session without waiting for a separate note-taking request, do not summarize until the learning session concludes, and stay in learn mode until the user explicitly ends it or uses a clear ending hint such as `wrap learning`.
- **Practice mode:** Create a first-pass implementation sandbox under `<problem_dir>/practice_MMDD/`: write candidate-facing instructions, create public interface stubs for the user to implement, create unit tests, and stop without adding solutions, hints, or interviewer feedback.
- **Mock mode:** Interview as a hiring engineer, create `<problem_dir>/mock_MMDD/mock_instructions.md`, create/review `<problem_dir>/mock_MMDD/mock_<problem_name>_<part>.ipynb` for Colab rounds, and record feedback in `<problem_dir>/mock_MMDD/mock_feedback.md`.

---

## Solve Mode Workflow

Use this workflow to analyze an interview round and produce interview-ready solutions.

### Phase 1: Requirements Analysis

All file operations are relative to the resolved `problem_dir`.

1. Scan `<problem_dir>/context/` for comprehensive raw interview context:
   - Read all relevant raw source files under `<problem_dir>/context/`, including Markdown, text, Python, notebooks, copied prompt dumps, screenshots converted to text, and any files explicitly named by the user.
   - Inspect nearby raw-context files such as `*requirements*.md`, `*question*.md`, `*mock*.md`, `*debug*.md`, `*starter*.py`, `*buggy*.py`, notebook files, and problem-specific `.md`/`.py` files.
   - Treat `context/` as the source of truth for raw problem information. Do not edit or overwrite raw context files.
   - Use legacy `input/` or `output/` artifacts only as supporting context when `context/` is missing or incomplete; prefer `context/` for new workflows.
   - Prefer source prompts and starter code under `context/` over derived solution artifacts when defining the candidate-facing problem.
   - Use solution/output artifacts only as supporting context for answer keys or study notes, never as the source for candidate-facing mock prompts.
   - Identify all interview problems, constraints, follow-ups, and context.
   - If the requirements reference multiple problems or parts, break them into discrete problems.
   - Surface any ambiguities early.

2. Create a comprehensive requirements document in `<problem_dir>/input/0_requirements.md`:
   - Synthesize the raw `context/` material into a clean, interview-ready requirements document.
   - Include:
     - Round or prompt context.
     - Problem list and part breakdown.
     - Candidate-facing problem statement.
     - Input/output contracts.
     - Public function/class signatures.
     - Constraints and assumptions.
     - Examples and edge cases.
     - Follow-up questions or variations.
     - Starter-code source references from `context/`.
     - Ambiguities, missing facts, and chosen assumptions.
   - Keep answer keys, expected fixes, hidden hints, rubric notes, and solution reasoning out of candidate-facing requirements unless clearly labeled as interviewer-only notes.

3. Create problem setup files in `<problem_dir>/input/`:
   - For each distinct problem, create `<problem_dir>/input/<problem_name>.md` with:
     - Problem statement (clean, formatted for reference)
     - Input/output contract
     - Constraints and edge cases
     - Example test cases
     - Follow-up questions or variations
   - For Colab coding problems, create `<problem_dir>/input/<problem_name>.ipynb` with:
     - Public function/class signatures and type hints derived from `context/`
     - Docstrings explaining the interface
     - Candidate-facing starter code copied or cleaned from `context/` when available
     - Stub bodies with `raise NotImplementedError()` only for missing implementation sections
     - Keep this file frozen for learn and mock modes; write reference solutions under `<problem_dir>/solution/` and mock attempts under `<problem_dir>/mock_MMDD/`.
   - Create a `.py` fallback/export only when it helps local validation or the prompt is not Colab-based.

4. Clean up duplicate setup files:
   - After creating `context/`, `input/`, and `solution/` artifacts, scan the resolved `problem_dir` and its immediate parent for setup duplicates from the old flat layout.
   - Remove an old legacy prompt/source file only when it is byte-for-byte duplicated in `<problem_dir>/context/` or its full content has been intentionally preserved there.
   - Remove an old generated requirements, prompt, starter, solution, or discussion file only when the corresponding normalized file exists under `<problem_dir>/input/` or `<problem_dir>/solution/` and contains the same information.
   - Do not delete raw context that exists only in one place. If a legacy raw file is the only source, move or copy it into `<problem_dir>/context/` first, verify the content, then remove the duplicate legacy copy.
   - Do not delete unrelated notes, neighboring problem files, or legacy artifacts for other rounds. If the duplicate relationship is not exact or obvious, keep the file and mention it as a cleanup candidate.
   - When removing files, also remove empty directories created only by that cleanup if they are inside `problem_dir`; leave parent directories alone unless the user explicitly asked for broader cleanup.
   - Report the removed paths and the retained canonical paths in the final summary.

5. Brief summary:
   - Recap the problem landscape and what you'll solve in order.
   - Call out any non-obvious constraints or tradeoffs.

### Phase 2: Solve Each Problem

For each problem in order:

1. **Approach & Design:**
   - State the input/output contract and key invariants.
   - Outline your approach, complexity, and why you chose it.
   - Compare with alternative approaches if relevant.

2. **Implementation (Coding Problems):**
   - Implement in `<problem_dir>/solution/<problem_name>_solution.ipynb` for Colab rounds with:
     - Docstrings and type hints
     - Concise comments on non-obvious logic (pointers, state, edge cases, base cases, DP transitions)
     - Interview-appropriate style: clear over clever
   - Add focused tests or a small `if __name__ == "__main__":` smoke-test block when useful.
   - Test thoroughly; include edge cases in reasoning and report the command you ran.

3. **Write `<problem_dir>/solution/interview_discussion.md`:**
   - Create one section per problem with:
     - **Problem Statement** (condensed from input)
     - **Key Insights** (2-3 bullet points: what makes this hard, what's the aha moment)
     - **Approach** (pseudocode + explanation, not full code)
     - **Complexity** (time/space with reasoning)
     - **Code Walkthrough** (short snippets + explanation, not full listing)
     - **Edge Cases** (how the solution handles them)
     - **Follow-Ups** (how to extend, optimize, or adapt)
   - Write as if explaining to an interviewer: conversational, confident, complete.

4. **Create `<problem_dir>/solution/deep_dive.md`:**
   - One section per problem with:
     - **Context** (where this pattern appears, what makes it Interview-hard)
     - **Mental Model** (how to think about the problem without code)
     - **Solution & Why** (full explanation + concise code snippets)
     - **Complexity Analysis** (detailed reasoning)
     - **Variants & Trade-offs** (alternative approaches and when to use them)
     - **Common Pitfalls** (what candidates often miss)
     - **Related Concepts** (link to your study notes if available)
   - Deeper and broader than `interview_discussion.md`; assume you know the basics.

5. **Walk-through:**
   - Summarize each solved problem: key insight, approach, complexity.
   - Mention which output files were created or updated.

---

## Learn Mode Workflow

Use this workflow as an interactive Q&A companion with auto-notes. Do not edit frozen files in `<problem_dir>/input/`.

### Setup

1. Confirm you're in learn mode and state which problem/concept you're exploring.
2. Default to answering the user's next question directly; offer a short menu only if the user has not chosen a focus.
3. Create `<problem_dir>/solution/learn_notes.md` if it does not exist.
4. Proactively update `<problem_dir>/solution/learn_notes.md` after each stabilized interview-relevant exchange with raw notes of the question and response, including follow-up Q&A, corrections, examples, and clarified misconceptions.

### During Learning

1. **Interactive Q&A Loop:**
   - Treat the user's question as the driver of the session.
   - Answer the immediate question first, then add only the context needed to make it interview-useful.
   - Ask at most one targeted follow-up or check-for-understanding question before continuing.
   - If the user says "next", continue to the next natural interview-relevant question or subtopic without extra framing.

2. **Explanations:**
   - Use plain language first, then technical depth.
   - Keep answers concise; answer the immediate question, then add context.
   - Use one small concrete example per explanation; avoid stacking examples.
   - Tie code to the problem statement and `<problem_dir>/solution/deep_dive.md` when available.
   - Highlight what you should say in a real interview.

3. **Answer Questions:**
   - When you ask about solution details, approach trade-offs, complexity, or edge cases, answer fully.
   - If you notice confusion, clarify the mental model before going deeper.
   - Point out common pitfalls and how tests or examples expose them.

4. **Raw Session Notes (Default):**
   - During the learning session, keep `<problem_dir>/solution/learn_notes.md` as the raw chronological learning log.
   - Proactively write notes after each stabilized interview-relevant exchange; do not wait for the user to say "take notes".
   - Record the actual question and response content while it is still fresh. Preserve the reasoning, examples, corrections, code details, and follow-up context that appeared in the exchange.
   - Use a raw transcript-like structure such as:
     - **Timestamp / turn:**
     - **Question / prompt:**
     - **Response notes:**
     - **Follow-up / correction:**
     - **Open item:**
   - Do not group, compress, polish, or convert notes into durable takeaways during the active learning session.
   - Do NOT take notes for workflow, environment, IDE, file-conversion, or tooling questions unless explicitly asked.
   - Keep notes chronological during the active session. Do not summarize them prematurely.

5. **Defer Deep-Dive Consolidation:**
   - Do not merge into `<problem_dir>/solution/deep_dive.md` after each individual question.
   - Do not group or summarize `<problem_dir>/solution/learn_notes.md` while learn mode is active.
   - Stay in learn mode until the user explicitly says `end learn`, `conclude learn`, or `exit learn`, or uses a clear ending hint such as `wrap learning`, `wrap learn`, `wrap up learning`, `finish learning`, `finish learn`, `end learning`, or similar wording.
   - Treat ending hints as permission to conclude learn mode only when they refer to learning/learn mode or clearly ask to wrap the learning session.
   - Do not treat generic phrases like "summarize", "consolidate", "done", "next", or a topic change as permission to exit learn mode unless they include a learn-mode ending command or clear learning-session wrap-up hint.
   - While the session is active, preserve detailed raw learning evidence in `<problem_dir>/solution/learn_notes.md`.

6. **Interactive & Pause:**
   - After answering, keep the session open for the next question.
   - Ask one check-for-understanding question only when it would expose a likely interview misconception.

### End of Learn Session

- Run this section only after the user explicitly says `end learn`, `conclude learn`, or `exit learn`, or uses a clear learn-mode ending hint such as `wrap learning`.
- Read the full `<problem_dir>/solution/learn_notes.md` before consolidating.
- Group related notes by concept, pattern, edge case, implementation technique, complexity tradeoff, and interview phrasing.
- Summarize each group into durable takeaways and merge them into `<problem_dir>/solution/deep_dive.md` under a dated "Learning Notes & Refinements" section or the most relevant existing section.
- Preserve important examples, counterexamples, invariants, and code-level caveats; remove duplicate or low-signal chatter.
- Reset `<problem_dir>/solution/learn_notes.md` to a short staging inbox that records the consolidation date and any remaining open gaps.
- Summarize what changed in understanding compared to the start and list the highest-leverage next drills.

---

## Practice Mode Workflow

Use this workflow for a first-pass solo implementation drill. Practice mode is lighter than mock mode: it sets up the files the user needs to code, then stops.

### Setup

1. **Create practice session directory:**
   - Create a new top-level practice directory named `<problem_dir>/practice_MMDD/`, where `MMDD` is the current date in the local timezone, e.g. `practice_0602`.
   - If `<problem_dir>/practice_MMDD/` already exists for a prior practice session that day, create the next available suffix: `practice_MMDD_2/`, `practice_MMDD_3/`, etc.
   - Set `problem_practice_output` to that new directory for the entire practice session.

2. **Scan generated input context for practice:**
   - Read `input/0_requirements.md` when present, then scan the rest of `input/` for generated candidate-facing prompt docs, function signatures, starter code, examples, and constraints.
   - If the user has an active or named input file, treat it as the primary practice target.
   - Use `input/*.py`, `input/*.ipynb`, `input/<problem_name>.md`, or a named input file as the preferred source of public interfaces.
   - Use solution artifacts only to understand test expectations when no candidate-facing examples exist. Do not copy solution logic, hints, or implementation details into practice files.

3. **Create candidate-facing instructions:**
   - Create `<problem_practice_output>/practice_instructions.md` with:
     - Problem statement.
     - Public interface contract.
     - Input/output behavior.
     - Constraints and edge cases.
     - How to run the unit tests.
     - What file the user should edit.
   - Keep the instructions candidate-facing. Do not include solution outline, hidden hints, rubric language, expected fixes, or answer keys.

4. **Create implementation scaffold:**
   - Prefer a Python scaffold for local practice: `<problem_practice_output>/practice_<problem_name>.py`.
   - For each requested function or class, include imports, type hints, docstrings with shape or data-contract notes when useful, and stub bodies using `raise NotImplementedError()`.
   - Preserve the public interface from `input/` exactly unless the prompt is ambiguous; if ambiguous, choose the simplest interview-friendly signature and record the assumption in `practice_instructions.md`.
   - Do not implement helper functions, algorithms, or partial logic for the user. Only add minimal pass-through structure needed for imports and tests to run.
   - For Colab or notebook rounds, create a `.py` scaffold for local unit testing and optionally create a matching `.ipynb` only when the input round is explicitly notebook-based.

5. **Create unit tests:**
   - Create `<problem_practice_output>/test_practice_<problem_name>.py`.
   - Use `pytest`-style tests by default unless the local repo clearly uses `unittest`.
   - Include focused public tests from the prompt examples plus edge cases implied by the candidate-facing requirements.
   - Tests should import from `practice_<problem_name>.py` and fail with `NotImplementedError` until the user implements the scaffold.
   - Do not include hidden-solution tests that reveal the algorithm or internal strategy.
   - Include one command in `practice_instructions.md`, usually:
     ```bash
     python3 -m pytest test_practice_<problem_name>.py
     ```

6. **Verify scaffold only:**
   - Run a syntax/import check that does not require the solution to pass, such as `python3 -m py_compile practice_<problem_name>.py test_practice_<problem_name>.py`.
   - Do not run the full pytest suite expecting success before the user implements the scaffold. If you do run pytest, report that failures are expected because implementation stubs raise `NotImplementedError`.
   - Stop after setup and tell the user which file to implement and which command to run.

### During Practice

- The user owns implementation in `<problem_practice_output>/practice_<problem_name>.py`.
- Do not edit the implementation after setup unless the user explicitly asks for help, review, or a fix.
- If the user asks for review, review the current practice implementation like code review: correctness first, then edge cases, complexity, clarity, and tests.
- If the user asks for hints, give the smallest conceptual hint; do not paste a full solution unless explicitly requested.
- Practice mode does not create `mock_feedback.md`, does not ask one-interviewer-question-at-a-time, and does not update next-round mock questions unless the user explicitly asks to convert practice misses into follow-up drills.

## Mock Mode Workflow

Use this workflow to simulate a real interview with step-by-step feedback.

### Setup

1. **Frame the interview:**
   - State only the interview problem and your role as interviewer; do not tell the user the sequence of steps to follow unless they explicitly ask about process.
   - Do not reveal the full intended solution upfront.
   - Keep feedback in interviewer tone: concise, probing, honest.
   - Ask exactly one question per assistant turn in mock mode; do not bundle multiple numbered questions or prompts in the same turn.
   - Treat the exchange like a real interview: do not coach, narrate what the candidate should do next, or provide a checklist of tasks.

2. **Create mock session directory:**
   - Create a new top-level mock directory named `<problem_dir>/mock_MMDD/`, where `MMDD` is the current date in the local timezone, e.g. `mock_0602`.
   - If `<problem_dir>/mock_MMDD/` already exists for a prior mock session that day, create the next available suffix: `mock_MMDD_2/`, `mock_MMDD_3/`, etc.
   - Set `problem_mock_output` to that new directory for the entire mock session.

3. **Scan generated input context for the mock:**
   - Read `input/0_requirements.md` when present, then scan the rest of `input/` for generated candidate-facing prompt docs, full question lists, starter code, and named files relevant to the mock.
   - If the user has an active or named input file, treat it as the primary mock target.
   - Use `input/mock_interview_questions.md` or similar files for prompt shape and constraints only; strip any answer-key, hint, rubric, or expected-fix language.
   - Use `input/*.ipynb`, `input/*_buggy.py`, `input/<problem_name>.py`, or the named input code file as the preferred starter-code source. For Colab rounds, write the mock artifact as `.ipynb`.

4. **Create candidate-facing instructions:**
   - Create `<problem_mock_output>/mock_instructions.md` with only the interview prompt, constraints, allowed assumptions, expected deliverables, and how the candidate should signal completion.
   - Hide all hints: do NOT include expected bugs, solution outline, fix list, `# FIX` comments, scoring rubric, "look at X first" guidance, expected outputs, or answer-key language.
   - If a candidate-facing source prompt already exists under `input/` (for example `input/mock_interview_questions.md`), summarize only the prompt/constraints needed for the mock; do not copy answer-key or rubric sections.

5. **Create starter code:**
   - Prefer copying the realistic candidate starter from `input/<problem_name>.ipynb`, `input/<problem_name>.py`, `input/<problem_name>_buggy.py`, or the named input code file into `<problem_mock_output>/mock_<problem_name>_<part>.ipynb` for Colab rounds.
   - Preserve the original bug surface in starter code, but remove any solution comments, `# FIX` markers, expected outputs, helper hints, or answer-key snippets before placing it in the mock directory.
   - If no starter code exists, create `<problem_mock_output>/mock_<problem_name>_<part>.ipynb` with public function/class signatures and type hints only for Colab rounds.
   - Stub bodies with `raise NotImplementedError()` only for missing implementations. Do not add algorithm hints, helper functions, test harnesses, or expected outputs unless the original prompt explicitly provides them as candidate-facing material.

### During Mock

1. **Clarification Questions (Your Turn):**
   - When you ask clarifying questions, I answer directly with constraints and examples.
   - I pick reasonable assumptions for ambiguous points.
   - I do NOT volunteer hidden edge cases or gotchas.
   - Ask one clarification question at a time, then wait for the answer before asking the next question.
   - Do not suggest which clarifying questions to ask; wait for the candidate to drive this phase.
   - Record Q&A in `<problem_mock_output>/mock_feedback.md`.

2. **Approach Explanation (Your Turn):**
   - When you outline your approach, I give concise feedback:
     - Correct or missing constraints? Call them out.
     - Overcomplicating? Ask a probing question that exposes the issue; do not volunteer hints unless the candidate asks for clarification.
     - Prune the idea? Validate it and move forward.
   - End feedback with at most one targeted next question.
   - Record approach feedback in `<problem_mock_output>/mock_feedback.md`.

3. **Coding (Your Turn):**
   - You implement in the scaffolded `<problem_mock_output>/mock_<problem_name>_<part>.ipynb` for Colab rounds.
   - I do NOT edit files or paste full implementations.
   - Do not provide hints, API reminders, or solution direction unless the candidate explicitly asks for clarification or help.
   - Record hints in `<problem_mock_output>/mock_feedback.md`.

4. **Code Review (My Turn):**
   - When you say "done", I review `<problem_mock_output>/mock_<problem_name>_<part>.*`:
     - List correctness bugs first, then edge cases, complexity, clarity, communication.
     - Provide smallest conceptual fix for each issue (no auto-patching).
     - Ask which tests you wrote; if none, note that test coverage was your responsibility.
   - When you ask me to "review my change", "check my code", or show a new test/fix, I review the current attempt before asking any new follow-up question.
   - Stay on the current coding round until the implementation and tests pass the current round's stated requirements, or until you explicitly ask to move on.
   - If the code still fails, give only the next blocking finding and the smallest conceptual fix; do not advance to optimization, scaling, or a new follow-up yet.
   - Record findings in `<problem_mock_output>/mock_feedback.md`.

5. **Follow-up:**
   - Ask follow-up questions only after the current coding round has passed code review and relevant tests, unless the follow-up directly targets the blocking bug.
   - If there are multiple coding parts, repeat Setup and During Mock steps 1-4 for the next part.
   - If there are no more coding parts, ask one design or scaling follow-up question at a time.

6. **Closing (My Turn):**
   - Give a verdict: "pass/lean pass/lean no/no-hire for this round" (or score if you ask).
   - Include 2-4 focused improvements for the next attempt.
   - Ask one follow-up question an interviewer might ask (optimization, concurrency, testing strategy, etc.).
   - Record verdict, improvements, and follow-up in `<problem_mock_output>/mock_feedback.md`.
   - Summarize the user's misses and weaknesses from this mock session:
     - Correctness bugs or failed invariants.
     - Missed edge cases and missing tests.
     - Complexity or performance blind spots.
     - API, notebook, or implementation mistakes.
     - Communication, clarification, or approach gaps.
     - Follow-up concepts that were weak or incomplete.
   - Convert those misses into additional next-round mock questions under `<problem_dir>/input/next_round_mock_questions.md`.
   - Also update the relevant generated problem prompt under `<problem_dir>/input/` with a `## Next Round Mock Focus` section when there is an obvious target file, such as `<problem_name>.md` or `mock_interview_questions.md`.
   - Keep next-round questions candidate-facing: ask probing questions and add constraints, but do not include answer keys, expected fixes, hidden hints, or solution outlines.
   - Include source traceability in the input update, such as `Source mock: mock_MMDD/mock_feedback.md`.

### Note-Taking (Proactive)

- Record every interview-relevant turn in `<problem_mock_output>/mock_feedback.md`:
  - Your clarification Qs and my answers
  - Your approach + my feedback
  - Hints given during coding
  - Code review findings
  - Final verdict and improvements
  - End-of-session misses, weaknesses, and next-round question seeds
- This becomes a learning record and a self-review guide.
- Do not record workflow, environment, IDE, file-conversion, or tooling questions unless explicitly asked.

---

## Tips for Best Results

- **Solve mode:** Create interview-ready `solution/interview_discussion.md` first; it's your cheat sheet before a real interview.
- **Learn mode:** Default to Q&A with raw chronological question/response notes; stay in learn mode until explicit `end learn`, `conclude learn`, `exit learn`, or a clear hint like `wrap learning`, then group and summarize into `solution/deep_dive.md`.
- **Practice mode:** Use this for first-pass coding reps: scaffold the interface and public unit tests, then let the user implement before asking for review.
- **Mock mode:** Treat it like a real interview: no Googling, no pausing to think for too long, explain as you code.
- **Between rounds:** Review `solution/interview_discussion.md` to warm up, then run a mock to stress-test under time pressure.

---

## File Reference

| File | Purpose | Created by | Edited in Learn | Reviewed in Mock |
|------|---------|-----------|-----------------|------------------|
| `<problem_dir>/context/*` | Raw source material | You | No | No |
| `<problem_dir>/input/0_requirements.md` | Comprehensive generated requirements | Solve | No | Reference |
| `<problem_dir>/input/next_round_mock_questions.md` | Next mock questions from prior misses | Mock | No | Reference |
| `<problem_dir>/input/<problem>.md` | Problem statement | Solve | No | No |
| `<problem_dir>/input/<problem>.ipynb` | Colab public interface | Solve | No | No |
| `<problem_dir>/input/<problem>.py` | Optional Python fallback/export | Solve | No | No |
| `<problem_dir>/solution/interview_discussion.md` | Interview cheat sheet | Solve | Yes (optional) | Reference |
| `<problem_dir>/solution/<problem>_solution.ipynb` | Full Colab solution | Solve | No | No |
| `<problem_dir>/solution/<problem>_solution.py` | Optional Python fallback/export | Solve | No | No |
| `<problem_dir>/solution/deep_dive.md` | Concept deep dives | Solve + Learn | Yes (merge notes) | Reference |
| `<problem_dir>/solution/learn_notes.md` | Raw learning notes | Learn | Yes (merge into deep_dive) | No |
| `<problem_dir>/practice_MMDD/practice_instructions.md` | Practice prompt and run command | Practice | No | Reference |
| `<problem_dir>/practice_MMDD/practice_<problem>.py` | Your first-pass implementation scaffold | Practice | No | Review on request |
| `<problem_dir>/practice_MMDD/test_practice_<problem>.py` | Public unit tests for practice implementation | Practice | No | Review on request |
| `<problem_dir>/mock_MMDD/mock_instructions.md` | Candidate-facing prompt | Mock | No | Reference |
| `<problem_dir>/mock_MMDD/mock_<problem_name>_<part>.ipynb` | Your Colab attempt | You | No | Yes |
| `<problem_dir>/mock_MMDD/mock_feedback.md` | Interview feedback | Mock | No | Record |
