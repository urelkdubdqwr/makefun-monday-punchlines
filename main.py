#!/usr/bin/env python3
"""Write the Monday-morning joke to entry.txt in the output directory.

The joke is stored verbatim in ENTRY (including its single trailing newline)
so the produced file is byte-for-byte stable regardless of platform defaults.
"""

import os
import sys

ENTRY = "Every Monday my alarm clock and I renegotiate our contract. It brings better lawyers.\n"


def main() -> int:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    try:
        os.makedirs(output_dir, exist_ok=True)
        target = os.path.join(output_dir, "entry.txt")
        with open(target, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(ENTRY)
    except OSError as exc:
        print(f"error: could not write entry.txt in {output_dir!r}: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
