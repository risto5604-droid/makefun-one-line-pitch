#!/usr/bin/env python3
"""Writes the entry line to /output/entry.txt for make.fun bounty
u-ronigrv-a-day-of-one-line-pitches-12cd9bb3."""
import os

LINE = "You've been carrying that app idea around for months, so describe it in plain words tonight and wake up tapping on something real, built while you slept, no code required."

# Gate: the entry must be exactly ONE sentence of 1-240 characters of UTF-8
# text, not only whitespace. ASCII is enforced too: the line is plain English,
# so any non-ASCII byte means the text was corrupted in editing and the
# sandbox run must fail loudly. One sentence means exactly one terminal
# period: "make.fun" is spelled out nowhere in the line, so a second period
# can only mean a second sentence sneaked in.
assert 1 <= len(LINE) <= 240 and LINE.strip() and LINE.isascii() and LINE.count(".") == 1, "entry line violates the one-sentence 1-240 character gate"

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
