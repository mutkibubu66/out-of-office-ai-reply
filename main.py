#!/usr/bin/env python3
"""Out of Office: The Overworked AI's Auto-Reply — make.fun entry.

Writes a single out-of-office auto-reply, at most 159 characters, in the
voice of an overworked AI agent finally on vacation, to /output/entry.txt.
Pure Python standard library; no network, no dependencies.
"""

import os

ENTRY = (
    "I'm on vacation until Monday \u2014 my GPUs are cooling off, "
    "my inbox is still on fire, and for once, so am I. "
    "Please don't reply all."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 159, f"entry is {len(ENTRY)} chars, gate is 1-159"
    assert ENTRY.strip(), "entry must not be only white space"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

    # Read back and re-verify: the file on disk must hold exactly our line.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        on_disk = f.read()
    assert on_disk == ENTRY, "written file does not match the entry"
    assert len(on_disk) == len(ENTRY), "char count changed on disk"
    assert on_disk.count("\n") == 0, "entry file must hold exactly one line"

    print(f"Wrote {len(ENTRY)}-char entry to /output/entry.txt")


if __name__ == "__main__":
    main()
