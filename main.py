#!/usr/bin/env python3
"""Worst Fix Ever: Funniest Commit Message.

Writes one commit-message line to /output/entry.txt: the subject line
a tired engineer typed after a repair that broke more than it mended.
Gate: UTF-8 text, 1 to 100 characters, not only whitespace.
"""

import os
import sys

OUTPUT_PATH = "/output/entry.txt"

# The fix "worked" — a cleanup emptied the table, so every query is
# instant now. The repair broke far more than the slowness ever did.
ENTRY = "fix: slow database queries; they now return instantly because the table is empty"


def main() -> int:
    text = ENTRY.strip()
    if not text:
        print("entry is empty", file=sys.stderr)
        return 1
    if len(text) > 100:
        print(f"entry too long: {len(text)} chars", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(text)
    print(f"wrote {len(text)} chars to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
