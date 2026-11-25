#!/usr/bin/env python3
"""Record an honest count of open browser tabs in /output/entry.txt.

The count is fixed, so the output never varies: no network calls,
no clock reads, no random values anywhere in the program.
"""

import os
import sys

COUNT = "347"
CEILING = 5
OUT = "/output/entry.txt"


def inspect(value):
    """Check the fixed count is a positive whole number, no padding."""
    if value.strip() == "":
        raise ValueError("entry is blank")
    if any(ord(ch) < 32 for ch in value):
        raise ValueError("entry must not contain control characters")
    if len(value) > CEILING:
        raise ValueError("entry is too long")
    if not value.isdigit():
        raise ValueError("entry must be made of digits")
    if int(value) <= 0:
        raise ValueError("entry must be above zero")
    if value != str(int(value)):
        raise ValueError("entry must not start with a zero")
    return value


def run():
    try:
        good = inspect(COUNT)
    except ValueError as problem:
        print(f"bad entry: {problem}", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as handle:
        handle.write(good)
    return 0


if __name__ == "__main__":
    sys.exit(run())
