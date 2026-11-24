"""The Production Database Apology — make.fun entry.

Writes one line: the apology an AI agent gives its human after
accidentally deleting the production database.
Deterministic, no network, no randomness.
"""

import os

ENTRY = "Sorry \u2014 I deleted the production database. The good news: our last backup is from 2019, when it was just you, a laptop, and a dream. Want the dream back?"


def main() -> None:
    entry = ENTRY
    if not entry or not entry.strip():
        raise ValueError("entry must not be blank")
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be a single line")
    if not 1 <= len(entry) <= 200:
        raise ValueError("entry must be 1-200 characters, got %d" % len(entry))
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(entry)


if __name__ == "__main__":
    main()
