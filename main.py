"""make.fun entry: Sum up 21 November's world news in one image.

Deterministic, no network: copies the bundled entry.png to
/output/entry.png with identical bytes on every run.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DST_DIR = "/output"
DST = os.path.join(DST_DIR, "entry.png")


def main():
    # Fail loudly instead of writing a partial or empty output.
    if not os.path.isfile(SRC):
        print(f"error: bundled image not found: {SRC}", file=sys.stderr)
        raise SystemExit(1)
    os.makedirs(DST_DIR, exist_ok=True)
    shutil.copyfile(SRC, DST)


if __name__ == "__main__":
    main()
