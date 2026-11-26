#!/usr/bin/env python3
"""One-Liner Laughs entry: write a single funny line to /output/entry.txt."""

import os

JOKE = "I told my therapist I'm afraid of commitment, so we meet twice a week now."


def main():
    # The gate requires UTF-8 text of 1 to 200 characters, not only whitespace.
    # Fail loudly instead of writing a line the gate would refuse.
    if not (1 <= len(JOKE) <= 200) or not JOKE.strip():
        raise SystemExit(f"joke is {len(JOKE)} chars, outside the 1-200 gate")
    os.makedirs("/output", exist_ok=True)
    # No trailing newline: it would count toward the 200-char cap and the
    # Size tie-break, and the judge reads the text exactly as written.
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
