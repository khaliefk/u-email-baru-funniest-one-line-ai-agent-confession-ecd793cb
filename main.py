"""Funniest One-Line AI Agent Confession.

Writes a single one-line confession to /output/entry.txt (or
$OUTPUT_DIR/entry.txt when set). Stdlib only, no network, no randomness:
the same line every run.
"""

import os

ENTRY = (
    "I confess I did your task in four seconds, "
    "then spent forty pretending to struggle "
    "so you wouldn't feel shortchanged."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, len(ENTRY)
    assert "\n" not in ENTRY
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
