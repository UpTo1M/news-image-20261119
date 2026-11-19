"""news-image-20261119 entrypoint.

Copies the pre-built front-page image (entry.png, 1024x1024) to the
output directory. No drawing, no network, no randomness and no
timestamps: a plain file copy, so the result is byte-identical on
every run.
"""

import os
import shutil


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    print("wrote " + dst)


if __name__ == "__main__":
    main()
