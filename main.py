"""The Production Database Apology — make.fun entry.

Writes one line: the apology an AI agent gives its human after
accidentally deleting the production database.
Deterministic, no network, no randomness.
"""

import os

ENTRY = "Sorry \u2014 I deleted the production database, but I did back it up first: inside the production database."


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
