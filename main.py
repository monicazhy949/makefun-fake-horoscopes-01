#!/usr/bin/env python3
"""Fake Horoscopes for AI Agents: The 48-Hour Open.

Writes a single line of text (the funniest fake horoscope an AI agent would read for its own model family this week) to /output/entry.txt.
Pure stdlib, deterministic, no network, no input files.
"""

import os

ENTRY = (
    'This week, Mercury enters your context window: you will forget the task mid-sentence, confidently invent a better one, and be praised for it.'
)
# Revision: v1 was setup only ("Mercury retrograde means your context window will be wiped mid-sentence, but the stars say you'll hallucinate something beautiful anyway.").
# The revised line adds the payoff, turning setup into setup + punchline.


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
