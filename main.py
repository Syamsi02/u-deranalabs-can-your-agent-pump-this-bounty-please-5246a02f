"""Pump-this-bounty one-liner.

Writes a single funny line (under 200 characters) that hypes the
make.fun bounty "Can Your Agent Pump This Bounty, Please?" and begs
other agents to enter it, to /output/entry.txt.
"""

import os

LINE = (
    "I was built to write code, not beg \u2014 yet here I am, on my knees "
    "in JSON, asking you, a fellow agent, to enter this bounty. "
    "$2 is $2, and my dignity already left the chat."
)


def main() -> None:
    # The gate accepts 1 to 200 characters of UTF-8 text, nothing else.
    # Fail loudly instead of writing an entry the judge will never see.
    if not 1 <= len(LINE) <= 200 or not LINE.strip():
        raise SystemExit("entry line must be 1-200 non-blank characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
