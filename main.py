"""Write the make.fun "worst AI advice" entry to a single text file.

The destination directory is $MAKEFUN_OUTPUT_DIR when set and non-empty,
otherwise /output. The directory is created if missing. The file is always
named entry.txt and contains the entry text followed by one newline.
"""

import os
import sys

ENTRY_TEXT = (
    "Antivirus flagged a threat? Click 'Ignore for now'. "
    "Real threats always introduce themselves politely first.\n"
)


def resolve_output_dir():
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def main():
    output_dir = resolve_output_dir()
    try:
        os.makedirs(output_dir, exist_ok=True)
    except OSError as exc:
        sys.exit(f"cannot create output directory {output_dir!r}: {exc}")
    dest = os.path.join(output_dir, "entry.txt")
    with open(dest, "w", encoding="utf-8") as fh:
        fh.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
