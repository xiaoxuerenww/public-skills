#!/usr/bin/env python3
"""Run a problem folder's test.py against solution.py."""

from __future__ import annotations

import argparse
import os
import py_compile
import subprocess
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run <problem-dir>/test.py with <problem-dir> on PYTHONPATH."
    )
    parser.add_argument("problem_dir", help="Directory containing solution.py and test.py")
    parser.add_argument(
        "--pytest",
        action="store_true",
        help="Run with python -m pytest test.py instead of python test.py",
    )
    args = parser.parse_args()

    problem_dir = Path(args.problem_dir).expanduser().resolve()
    solution = problem_dir / "solution.py"
    test = problem_dir / "test.py"

    if not problem_dir.is_dir():
        print(f"Problem directory not found: {problem_dir}", file=sys.stderr)
        return 2
    if not solution.exists():
        print(f"Missing solution.py in {problem_dir}", file=sys.stderr)
        return 2
    if not test.exists():
        print(f"Missing test.py in {problem_dir}", file=sys.stderr)
        return 2

    try:
        py_compile.compile(str(test), doraise=True)
    except py_compile.PyCompileError as exc:
        print("test.py is not valid Python yet; convert the rough cases first.", file=sys.stderr)
        print(exc.msg, file=sys.stderr)
        return 2

    env = os.environ.copy()
    env["PYTHONPATH"] = (
        str(problem_dir)
        if not env.get("PYTHONPATH")
        else str(problem_dir) + os.pathsep + env["PYTHONPATH"]
    )

    cmd = [sys.executable, "-m", "pytest", "test.py"] if args.pytest else [sys.executable, "test.py"]
    return subprocess.call(cmd, cwd=str(problem_dir), env=env)


if __name__ == "__main__":
    raise SystemExit(main())
