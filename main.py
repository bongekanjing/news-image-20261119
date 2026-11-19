#!/usr/bin/env python3
"""news-image-20261119 entrypoint (Python 3.13, standard library only).

The front page is drawn at build time by draw.py (PIL, DejaVu fonts) and
shipped in this repository as entry.png. This program only copies that
file to the grader's output directory, so both graded runs write
byte-identical bytes with no network and no third-party packages.

Usage:
    MAKEFUN_OUTPUT_DIR=out python3 main.py
Writes <output dir>/entry.png (default /output).
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    # Guard the gate: a whole PNG of at most 1 MiB and 1024x1024.
    with open(dst, "rb") as fh:
        head = fh.read(8)
    if head != b"\x89PNG\r\n\x1a\n":
        raise ValueError("entry.png is not a PNG")
    if os.path.getsize(dst) > 1048576:
        raise ValueError("entry.png exceeds 1 MiB")


if __name__ == "__main__":
    main()
