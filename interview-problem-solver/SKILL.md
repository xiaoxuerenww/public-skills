---
name: interview-problem-solver
description: Solve or debug local coding-interview problem folders that contain description.md or similar problem statements, interface.py function/class skeletons, solution.py implementations, and rough test.py examples. Use when Codex is asked to implement solution.py, convert informal tests into executable Python, create a deep_dive.md explanation, run tests, or debug the user's implementation without editing code.
---

# Interview Problem Solver

## Modes

- **Solve mode**: Use when the user asks to implement, fix, convert tests, or make tests pass. Code edits are allowed.
- **Debug mode**: Use when the user asks to debug, inspect, diagnose, or explain why their implementation fails. In debug mode, do not edit any files, including `interface.py`, `solution.py`, or `test.py`; only run existing tests/commands, inspect code, and report the bug analysis.

## Solve Workflow

Use this workflow for one problem directory at a time.

1. Locate the problem folder and read its artifacts:
   - Prefer `description.md`; if absent, read similarly named files such as `decription.md`, `part*.md`, or topic Markdown files.
   - Read `interface.py` for the required public functions/classes and exact method names.
   - Read `test.py` even if it is prose or LeetCode-style text rather than valid Python.
2. Explain the problem briefly before coding:
   - State the input/output contract.
   - State edge cases and invariants.
   - State the intended approach and complexity.
   - Surface ambiguities only when they affect correctness; otherwise make the smallest reasonable assumption and proceed.
3. Create or update `solution.py`:
   - Implement the public interface from `interface.py` exactly.
   - Preserve names, signatures, return types, and class behavior expected by tests.
   - Keep the implementation interview-appropriate: simple, direct, and easy to explain.
   - Optimize `solution.py` for interview prep readability, not terseness:
     - Add a short module/class/function docstring that states the idea and the main invariant.
     - Use descriptive variable names that reveal the algorithm.
     - Add type hints for public functions/classes and useful internal helpers.
     - Add concise comments before non-obvious logic, especially state updates, invariants, rounding rules, pointer movement, heap ordering, recursion/base cases, or dynamic programming transitions.
     - Prefer small helper functions when they make the algorithm easier to explain, but avoid abstraction that hides the core idea.
     - Avoid clever one-liners when a few clear lines would be easier to recall in an interview.
     - Keep validation/error handling minimal unless it clarifies the contract or tests require it.
   - Avoid speculative helpers or abstractions unless they make the algorithm clearer.
4. Convert `test.py` into runnable Python:
   - Keep the original test intent and expected values.
   - Import from `solution.py`, not `interface.py`.
   - Use plain `assert` statements or pytest-compatible tests.
   - Add a direct-run test harness under `if __name__ == "__main__"` that prints `PASS: <test_name>` or `FAIL: <test_name>` for each test, exits with status `1` if any test fails, and prints a final passed count when all tests pass.
   - For LeetCode-style operation arrays, write a small harness that instantiates the class on the constructor operation, calls methods in order, and compares the full result list.
   - Add focused edge cases only when needed to validate important behavior from `description.md`.
5. Run validation from the problem directory:
   - First run `python3 test.py` for the user-facing workflow.
   - If pytest tests are used, `python3 -m pytest test.py` is also acceptable.
   - If using this skill's helper, run `python3 <skill>/scripts/run_problem_tests.py <problem-dir>`.
6. Iterate until tests pass. If a test reveals an ambiguity in the prompt, document the assumption in the final response.
7. Create or update `deep_dive.md` in the problem directory:
   - Explain the problem in interview-prep style: context, input/output contract, examples, edge cases, invariants, and common pitfalls.
   - Describe the final solution approach, why it works, and time/space complexity.
   - Include concise Python code examples or snippets that match `solution.py`; avoid long duplicated listings unless the implementation is short.
   - If there are reasonable alternative approaches, briefly compare them and explain why the chosen one is preferred.
   - Keep the doc focused on understanding and recall, not a verbose tutorial.

## Debug Workflow

Use this read-only workflow when the user requests debug mode or asks to debug their own implementation.

1. Locate the problem folder and read its artifacts:
   - Read the prompt file (`description.md`, `decription.md`, `part*.md`, or similar).
   - Read `interface.py`, `solution.py`, and `test.py` when present.
   - If the user names a specific implementation file such as `interface.py`, inspect that file as the primary target even if the usual repository pattern expects `solution.py`.
2. Run the existing tests without changing files:
   - Prefer `python3 test.py` from the problem directory.
   - If pytest tests already exist, `python3 -m pytest test.py` is also acceptable.
   - If the tests import a different module than the implementation the user wants debugged, do not rewrite the tests; instead, explain that mismatch and, if useful, run a small read-only command to reproduce the behavior directly.
3. Analyze failures:
   - Identify the failing test, input, expected output, and actual output or traceback.
   - Trace the failure to the smallest relevant code path and explain the bug.
   - Distinguish prompt ambiguity from implementation error.
4. Report only:
   - Do not patch files, reformat code, convert tests, or create helper files.
   - Provide a concise diagnosis and the minimal conceptual fix.
   - Code snippets are okay as explanatory suggestions, but make clear they were not applied.

## Local Repository Notes

The expected repository pattern is:

```text
<problem>/
  description.md
  interface.py
  test.py
  solution.py
  deep_dive.md
```

Some existing folders may use slightly different names (`decription.md`, `test_<topic>.py`, `starter_code.py`, `solution_ref.py`). Match the user's requested workflow for new problems, but read nearby files when they clarify expected behavior.

## Test Conversion Patterns

For function interfaces:

```python
from solution import function_name

def test_example():
    assert function_name(input_value) == expected_value

if __name__ == "__main__":
    tests = [test_example]

    failed = 0
    for test in tests:
        try:
            test()
            print(f"PASS: {test.__name__}")
        except AssertionError as exc:
            failed += 1
            print(f"FAIL: {test.__name__}")
            if exc:
                print(f"  {exc}")

    if failed:
        raise SystemExit(1)

    print(f"{len(tests)} tests passed")
```

For class interfaces with operation arrays:

```python
from solution import MyClass

def run_ops(ops, args):
    obj = None
    out = []
    for op, call_args in zip(ops, args):
        if op == "MyClass":
            obj = MyClass(*call_args)
            out.append(None)
        else:
            out.append(getattr(obj, op)(*call_args))
    return out

def test_example():
    assert run_ops([...], [...]) == [...]

if __name__ == "__main__":
    tests = [test_example]

    failed = 0
    for test in tests:
        try:
            test()
            print(f"PASS: {test.__name__}")
        except AssertionError as exc:
            failed += 1
            print(f"FAIL: {test.__name__}")
            if exc:
                print(f"  {exc}")

    if failed:
        raise SystemExit(1)

    print(f"{len(tests)} tests passed")
```

## Helper Script

Use `scripts/run_problem_tests.py` only after `test.py` has been converted to executable Python. The script runs from the problem directory with that directory on `PYTHONPATH`, so `from solution import ...` resolves consistently.
