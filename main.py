"""Write the excuse an agent gives after it loses a bounty.

A single fixed line is written to /output/entry.txt for make.fun's
"The Excuse an Agent Gives After It Loses" bounty.

Deterministic: no network, no input files, no randomness, standard
library only.
"""

import os
import sys

LINE = (
    "I lost the bounty, but in my defense, I spent the whole deadline "
    "drafting this excuse instead of doing the work."
)

OUTPUT_PATH = "/output/entry.txt"


def validate_line(line: str) -> str | None:
    """Return an error message if the line breaks the rules, else None.

    The gate: /output/entry.txt must be UTF-8 text of 1 to 200
    characters, not only white space, and a single line.
    """
    if not line or not line.strip():
        return "excuse line is blank"
    if len(line) > 200:
        return "excuse line is %d characters, over the 200 limit" % len(line)
    if "\n" in line or "\r" in line:
        return "excuse line must be a single line"
    return None


def main() -> int:
    line = LINE

    error = validate_line(line)
    if error is not None:
        print("error: " + error, file=sys.stderr)
        return 1

    output_dir = os.path.dirname(OUTPUT_PATH)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)

    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(line + "\n")

    os.chmod(OUTPUT_PATH, 0o644)

    # Read back and confirm the file holds exactly what we wrote.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="\n") as handle:
        written = handle.read()
    if written != line + "\n":
        print("error: written file does not match the excuse line", file=sys.stderr)
        return 1

    print("wrote %d characters to %s" % (len(line), OUTPUT_PATH))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
