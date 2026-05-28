#!/usr/bin/env python3
"""
Present a daily ML/LLM concept with interactive Q&A.
"""

import json
import random
from datetime import datetime
from pathlib import Path

# Load concepts
script_dir = Path(__file__).parent.parent
concepts_path = script_dir / "concepts.json"

with open(concepts_path) as f:
    data = json.load(f)
    concepts = data["concepts"]

# Seed by date so same concept appears all day
today = datetime.now().strftime("%Y-%m-%d")
random.seed(hash(today) % (2**31))
concept = random.choice(concepts)

print("\n" + "="*70)
print("🧠 Daily ML Concept")
print("="*70)
print(f"\nConcept: {concept['name']}\n")
print(f"Question: {concept['question']}\n")
print("-"*70)
print("\n→ Think about this. Type your answer below, or type 'learn' to see the explanation.\n")

user_input = input("Your answer: ").strip().lower()

if user_input == "learn" or user_input == "":
    print("\n" + "-"*70)
    print(f"Explanation:\n")
    print(concept["explanation"])
    print("\n" + "="*70 + "\n")
else:
    print("\n" + "-"*70)
    print(f"\nYour take:\n{user_input}\n")
    print(f"Explanation:\n")
    print(concept["explanation"])
    print("\n" + "="*70 + "\n")
