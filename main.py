"""Build the 21 November world-news picture for make.fun.

The picture itself is already drawn and bundled next to this file.
All this program does is place an exact copy of it where the
judge expects to find it. Nothing is fetched, generated, or
changed along the way, so every run produces the same bytes.
"""

from pathlib import Path
import sys

# The picture shipped with this entry, and where it has to land.
bundled_image = Path(__file__).resolve().parent / "entry.png"
output_folder = Path("/output")
output_image = output_folder / "entry.png"


def check_image_ready(image_path):
    """Return how many bytes the bundled picture holds.

    A missing file, or one with nothing in it, counts as zero,
    which tells the caller the entry cannot be built.
    """
    if not image_path.is_file():
        return 0
    return image_path.stat().st_size


def run_entry():
    """Place the bundled picture at the expected output path."""
    picture_size = check_image_ready(bundled_image)
    if picture_size <= 0:
        print(f"error: no usable bundled image at {bundled_image}", file=sys.stderr)
        sys.exit(1)
    output_folder.mkdir(parents=True, exist_ok=True)
    output_image.write_bytes(bundled_image.read_bytes())
    print(f"wrote {output_image} ({picture_size} bytes)")


if __name__ == "__main__":
    run_entry()
