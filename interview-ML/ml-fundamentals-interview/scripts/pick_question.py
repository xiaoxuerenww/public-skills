#!/usr/bin/env python3
"""Pick and track ML/LLM fundamentals quiz questions."""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import random
import re
from dataclasses import dataclass
from pathlib import Path

QUIZ_DIR = Path(os.path.expanduser("~/Documents/work/0_databricks/0_db_ml_fundamental"))
BANK_PATH = QUIZ_DIR / "2_ml-llm-fundamentals-QUIZ.md"
STATE_PATH = QUIZ_DIR / "ml_llm_daily_quiz_progress.json"
NOTES_PATH = QUIZ_DIR / "ml_llm_daily_quiz_notes.md"


@dataclass(frozen=True)
class Question:
    section: str
    subsection: str
    topic: str
    prompt: str
    kind: str = "parent"
    parent_id: str = ""

    @property
    def id(self) -> str:
        raw = "\n".join([self.section, self.subsection, self.topic, self.prompt])
        return hashlib.sha1(raw.encode("utf-8")).hexdigest()[:12]

    def to_dict(self) -> dict[str, str]:
        return {
            "id": self.id,
            "section": self.section,
            "subsection": self.subsection,
            "topic": self.topic,
            "prompt": self.prompt,
            "kind": self.kind,
            "parent_id": self.parent_id,
        }


def parse_questions(path: Path) -> list[Question]:
    questions: list[Question] = []
    section = ""
    subsection = ""
    current_parent_id = ""
    pending_heading: tuple[str, str] | None = None
    item_re = re.compile(r"^-\s+\*\*(Q\d{3,4}\.\s+.+?)\*\*(?:\s+(\([^)]*\)))?:\s*(.+?)\s*$")
    item_question_re = re.compile(r"^-\s+\*\*(Q\d{3,4}\.\s+.+?)\*\*(?:\s+(\([^)]*\)))?\s*(.*?)\s*$")
    heading_question_re = re.compile(r"^(#{3,4})\s+(Q[\d.]+:\s+.+?)\s*$")
    question_text_re = re.compile(r"^\*\*Question\*\*:\s*(.+?)\s*$")

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.rstrip()
        stripped = line.strip()
        if line.startswith("## "):
            section = line[3:].strip()
            subsection = ""
            current_parent_id = ""
            pending_heading = None
        elif line.startswith("### "):
            heading_match = heading_question_re.match(stripped)
            if heading_match:
                subsection = ""
                current_parent_id = ""
                pending_heading = (heading_match.group(1), heading_match.group(2).strip())
            else:
                subsection = line[4:].strip()
                current_parent_id = ""
                pending_heading = None
        else:
            heading_match = heading_question_re.match(stripped)
            if heading_match:
                pending_heading = (heading_match.group(1), heading_match.group(2).strip())
                continue

            question_match = question_text_re.match(stripped)
            if question_match and pending_heading and section:
                heading_level, topic = pending_heading
                kind = "followup" if heading_level == "####" else "parent"
                question = Question(
                    section=section,
                    subsection=subsection,
                    topic=topic,
                    prompt=question_match.group(1).strip(),
                    kind=kind,
                    parent_id=current_parent_id if kind == "followup" else "",
                )
                questions.append(question)
                if kind == "parent":
                    current_parent_id = question.id
                    subsection = topic
                pending_heading = None
                continue

            indent = len(line) - len(line.lstrip())
            kind = "followup" if indent > 0 else "parent"
            parent_id = current_parent_id if kind == "followup" else ""
            match = item_re.match(stripped)
            if match and section:
                topic, modifier, prompt = match.groups()
                if modifier:
                    topic = f"{topic} {modifier}"
                question = Question(
                    section=section,
                    subsection=subsection,
                    topic=topic.strip(),
                    prompt=prompt.strip(),
                    kind=kind,
                    parent_id=parent_id,
                )
                questions.append(question)
                if kind == "parent":
                    current_parent_id = question.id
            else:
                match = item_question_re.match(stripped)
                if match and section:
                    topic, modifier, prompt = match.groups()
                    if modifier:
                        topic = f"{topic} {modifier}"
                    prompt = prompt.strip() or topic.strip()
                    question = Question(
                        section=section,
                        subsection=subsection,
                        topic=topic.strip(),
                        prompt=prompt,
                        kind=kind,
                        parent_id=parent_id,
                    )
                    questions.append(question)
                    if kind == "parent":
                        current_parent_id = question.id

    return questions


def parent_questions(questions: list[Question]) -> list[Question]:
    return [question for question in questions if question.kind == "parent"]


def followups_for(question: Question, questions: list[Question]) -> list[Question]:
    return [candidate for candidate in questions if candidate.parent_id == question.id]


def filter_questions(questions: list[Question], topic: str | None) -> list[Question]:
    if not topic:
        return questions
    needle = topic.lower()
    return [
        question
        for question in questions
        if needle in " ".join(
            [question.section, question.subsection, question.topic, question.prompt]
        ).lower()
    ]


def filter_parent_questions(questions: list[Question], topic: str | None) -> list[Question]:
    parents = parent_questions(questions)
    if not topic:
        return parents

    matching = filter_questions(questions, topic)
    matching_ids = {question.id for question in matching}
    matching_parent_ids = {
        question.parent_id
        for question in matching
        if question.kind == "followup" and question.parent_id
    }
    return [
        question
        for question in parents
        if question.id in matching_ids or question.id in matching_parent_ids
    ]


def load_state(path: Path) -> dict:
    if not path.exists():
        return {"version": 1, "asked": {}, "answers": {}, "queues": {}}
    return json.loads(path.read_text(encoding="utf-8"))


def save_state(path: Path, state: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(state, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def queue_key(topic: str | None, question_ids: list[str]) -> str:
    scope = f"topic:{topic.lower()}" if topic else "all"
    source = hashlib.sha1("\n".join(sorted(question_ids)).encode("utf-8")).hexdigest()[:10]
    return f"{scope}|{source}"


def shuffled_ids(question_ids: list[str], key: str, cycle: int) -> list[str]:
    ids = list(question_ids)
    seed = hashlib.sha256(f"{key}|cycle:{cycle}".encode("utf-8")).hexdigest()
    random.Random(seed).shuffle(ids)
    return ids


def pick_from_queue(questions: list[Question], state: dict, topic: str | None, count: int) -> list[Question]:
    by_id = {question.id: question for question in questions}
    ids = [question.id for question in questions]
    key = queue_key(topic, ids)
    queues = state.setdefault("queues", {})
    queue = queues.get(key)
    expected_ids = set(ids)

    if not queue or set(queue.get("ids", [])) != expected_ids:
        queue = {"cycle": 0, "index": 0, "ids": shuffled_ids(ids, key, 0)}
        queues[key] = queue

    picked: list[Question] = []
    while len(picked) < count:
        if queue["index"] >= len(queue["ids"]):
            queue["cycle"] += 1
            queue["index"] = 0
            queue["ids"] = shuffled_ids(ids, key, queue["cycle"])

        question_id = queue["ids"][queue["index"]]
        queue["index"] += 1
        if question_id in by_id:
            picked.append(by_id[question_id])

    return picked


def mark_asked(state: dict, questions: list[Question], timestamp: str) -> None:
    asked = state.setdefault("asked", {})
    for question in questions:
        record = asked.setdefault(
            question.id,
            {
                "first_asked_at": timestamp,
                "ask_count": 0,
                "question": question.to_dict(),
            },
        )
        record["last_asked_at"] = timestamp
        record["ask_count"] = int(record.get("ask_count", 0)) + 1
        record["question"] = question.to_dict()


def seen_count(state: dict, question_id: str) -> int:
    return int(state.get("asked", {}).get(question_id, {}).get("ask_count", 0))


def append_note(
    path: Path,
    question: dict,
    status: str,
    notes: str,
    timestamp: str,
    times_seen: int,
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.write_text("# ML/LLM Daily Quiz Notes\n\n", encoding="utf-8")

    section = " > ".join(
        part for part in [question.get("section", ""), question.get("subsection", "")] if part
    )
    note = notes.strip() if notes.strip() else "(no notes provided)"
    prompt = question.get("prompt", "")
    entry = "\n".join(
        [
            f"## {prompt}",
            "",
            f"- Recorded: {timestamp}",
            f"- Status: `{status}`",
            f"- Question ID: `{question.get('id', '')}`",
            f"- Times seen: {times_seen}",
            f"- Section: {section}",
            f"- Topic: {question.get('topic', '')}",
            f"- Notes: {note}",
            "",
        ]
    )
    with path.open("a", encoding="utf-8") as handle:
        handle.write(entry)


def record_result(
    state: dict,
    question_id: str,
    status: str,
    notes: str,
    timestamp: str,
    notes_path: Path,
) -> None:
    asked_record = state.get("asked", {}).get(question_id, {})
    question = asked_record.get("question")
    if not question:
        raise SystemExit(f"Question ID has not been asked yet: {question_id}")
    times_seen = int(asked_record.get("ask_count", 0))

    answers = state.setdefault("answers", {})
    record = answers.setdefault(question_id, {"question": question, "attempts": []})
    record["question"] = question
    record["attempts"].append(
        {
            "answered_at": timestamp,
            "status": status,
            "times_seen": times_seen,
            "notes": notes.strip(),
        }
    )
    append_note(notes_path, question, status, notes, timestamp, times_seen)


def format_question(
    question: Question,
    number: int,
    total: int,
    state: dict,
    followups: list[Question] | None = None,
) -> str:
    path = " > ".join(part for part in [question.section, question.subsection] if part)
    lines = [
        f"Question {number}/{total}",
        f"Question ID: {question.id}",
        f"Times seen: {seen_count(state, question.id)}",
        f"Section: {path}",
        f"Topic: {question.topic}",
        f"Prompt: {question.prompt}",
    ]
    if followups:
        lines.append("Follow-ups:")
        for idx, followup in enumerate(followups, start=1):
            lines.append(f"{idx}. Question ID: {followup.id}")
            lines.append(f"   Times seen: {seen_count(state, followup.id)}")
            lines.append(f"   Topic: {followup.topic}")
            lines.append(f"   Prompt: {followup.prompt}")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bank", type=Path, default=BANK_PATH)
    parser.add_argument("--state", type=Path, default=STATE_PATH)
    parser.add_argument("--notes-path", type=Path, default=NOTES_PATH)
    parser.add_argument("--date", default=dt.date.today().isoformat())
    parser.add_argument("--topic")
    parser.add_argument("--count", type=int, default=1)
    parser.add_argument("--random", action="store_true")
    parser.add_argument("--peek", action="store_true", help="Show questions without recording them as asked.")
    parser.add_argument("--record-result", metavar="QUESTION_ID")
    parser.add_argument("--status", choices=["pass", "fail", "strong", "partial", "needs_work"])
    parser.add_argument("--notes", default="")
    args = parser.parse_args()

    timestamp = dt.datetime.now().astimezone().isoformat(timespec="seconds")
    state = load_state(args.state)

    if args.record_result:
        if not args.status:
            raise SystemExit("--status is required with --record-result")
        record_result(
            state,
            args.record_result,
            args.status,
            args.notes,
            timestamp,
            args.notes_path,
        )
        save_state(args.state, state)
        print(f"Recorded {args.status} for question {args.record_result}")
        print(f"State: {args.state}")
        print(f"Notes: {args.notes_path}")
        return

    if not args.bank.exists():
        raise SystemExit(f"Question bank not found: {args.bank}")

    all_questions = parse_questions(args.bank)
    questions = filter_parent_questions(all_questions, args.topic)
    if not questions:
        topic_msg = f" for topic '{args.topic}'" if args.topic else ""
        raise SystemExit(f"No questions found{topic_msg} in {args.bank}")

    count = max(1, min(args.count, len(questions)))
    if args.random:
        picked = random.sample(questions, count)
    else:
        picked = pick_from_queue(questions, state, args.topic, count)

    picked_with_followups: list[Question] = []
    for question in picked:
        picked_with_followups.append(question)
        picked_with_followups.extend(followups_for(question, all_questions))

    if not args.peek:
        mark_asked(state, picked_with_followups, timestamp)
        save_state(args.state, state)

    print(f"Bank: {args.bank}")
    print(f"State: {args.state}")
    print(f"Available parent questions: {len(questions)}")
    print(f"Asked parent questions in this scope: {len(set(state.get('asked', {})) & {q.id for q in questions})}/{len(questions)}")
    print()
    for idx, question in enumerate(picked, start=1):
        print(format_question(question, idx, count, state, followups_for(question, all_questions)))
        if idx != count:
            print()


if __name__ == "__main__":
    main()
