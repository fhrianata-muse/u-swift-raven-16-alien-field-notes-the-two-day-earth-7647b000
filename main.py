#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review — entry program.

Writes one line (an alien tourist's review of Earth) to /output/entry.txt.
The line is kept as data; before writing, the program re-checks the
competition gate itself: plain text, one line, 1 to 200 characters, not
only white space, no leading or trailing space, ending on terminal
punctuation so the review reads complete.
"""

import sys
from pathlib import Path

ENTRY = "When the metal bird landed safely, the locals applauded the pilot like he had done a trick. He had. 5/5, would clap again."

OUT = Path("/output/entry.txt")


def check(text):
    """Return a reason the text fails the gate, or None when it passes."""
    if "\n" in text or "\r" in text:
        return "entry must be a single line"
    if not 1 <= len(text) <= 200:
        return "entry must be 1 to 200 characters, got %d" % len(text)
    if not text.strip():
        return "entry must not be only white space"
    if text != text.strip():
        return "entry must not start or end with white space"
    if any(ord(ch) < 32 for ch in text):
        return "entry must not contain control characters"
    if "  " in text:
        return "entry must not contain double spaces"
    if text[-1] not in ".!?":
        return "entry must end with terminal punctuation"
    return None


def main():
    problem = check(ENTRY)
    if problem is not None:
        print("gate failed: " + problem, file=sys.stderr)
        raise SystemExit(1)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
