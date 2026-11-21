#!/usr/bin/env python3
"""The joke about the demo — make.fun entry.

Writes one one-line joke about working beside an AI coding agent
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Deterministic, stdlib only, no network.
"""

import os

JOKE = "My AI agent fixed the demo bug live on stage \u2014 by deleting the feature the client came to see."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
