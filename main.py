#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review.

Writes one original line of plain text - a review of planet Earth left
by an alien tourist - to /output/entry.txt. Pure standard library.
"""

import os

ENTRY = (
    "Gorgeous planet, but the locals keep feeding the wildlife (us) "
    "and the Wi-Fi password is apparently a state secret. "
    "3/5 stars - would abduct again."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY.strip()
    # Gate: exactly one line, 1-200 characters, not only whitespace, valid UTF-8.
    assert text, "entry must not be empty"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert text.strip(), "entry must not be only whitespace"
    text.encode("utf-8")  # raises if not valid UTF-8

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text + "\n")

    # Read back and re-verify: the file on disk must hold exactly our line.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        on_disk = f.read()
    assert on_disk == text + "\n", "written file does not match the entry"
    assert len(on_disk.rstrip("\n")) == len(text), "char count changed on disk"
    assert on_disk.count("\n") == 1, "entry file must hold exactly one line"

    print(f"Wrote {len(text)} characters to {OUTPUT_PATH}:")
    print(text)


if __name__ == "__main__":
    main()
