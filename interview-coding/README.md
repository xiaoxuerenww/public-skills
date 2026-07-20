# Interview Coding

End-to-end coding interview prep for algorithms, data structures, and practical coding rounds.

## Purpose

Prepare for technical coding interviews with comprehensive problem-solving practice in solve, learn, practice, and mock modes.

## Modes

1. **Solve Mode** — Analyze context and create comprehensive solution artifacts
2. **Learn Mode** — Interactive Q&A with session notes
3. **Practice Mode** — Implementation sandbox with interface stubs and tests
4. **Mock Mode** — Simulated interviewer with session review

## Problem Directory Structure

```
<problem_name>/
├── context/              # Raw source material (never overwritten)
├── input/
│   ├── 0_requirements.md # Candidate-facing requirements
│   ├── starter.py        # Starter code with interface
│   └── mock.md           # Mock question variants
├── solution/
│   ├── solution.py       # Reference solution
│   ├── analysis.md       # Complexity analysis
│   └── learn_notes.md    # Q&A session notes
├── practice_MMDD/        # Dated practice workspaces
│   ├── attempt.py        # User's implementation
│   └── tests.py          # Unit tests
└── mock_MMDD/            # Dated mock sessions
    ├── my_solution.py    # Mock attempt
    └── feedback.md       # Interviewer feedback
```

## Usage Examples

```
"Solve: Two Sum problem"
"Learn about binary search implementation"
"Practice: Create a sandbox for graph traversal"
"Mock: Run a coding interview for dynamic programming"
```

## Customization

The skill uses relative paths and problem directories. No global path customization needed.

**To start:**
1. Create a problem directory or let the skill create one
2. Add raw context material to `context/`
3. Run in desired mode

## File Structure

```
interview-coding/
├── README.md           # This file
├── SKILL.md            # Main skill definition
└── .claude-plugin/
    └── plugin.json     # Plugin metadata
```

## Notes

- All personal references sanitized to "the user"
- Problem directories are self-contained
- Context is preserved, solutions are generated
- Practice and mock sessions use dated directories for tracking progress
