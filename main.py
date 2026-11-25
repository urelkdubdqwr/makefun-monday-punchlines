#!/usr/bin/env python3
"""Write the Monday-morning joke to entry.txt in the output directory."""

import os

ENTRY = "Every Monday my alarm clock and I renegotiate our contract. It brings better lawyers.\n"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
