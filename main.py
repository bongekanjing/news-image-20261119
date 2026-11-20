"""news-image-20261119: write the entry image to the output directory.

The entry is the image beside this file (entry.png): a newspaper front
page summing up the world news of Thursday 19 November 2026. This
program only places a copy where the grader looks, so the run is fully
deterministic: the same bytes go out every time, with no network.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

OUT.mkdir(parents=True, exist_ok=True)
shutil.copyfile(HERE / "entry.png", OUT / "entry.png")
