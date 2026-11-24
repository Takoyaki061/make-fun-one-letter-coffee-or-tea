#!/usr/bin/env python3
"""One Letter: Coffee or Tea — make.fun entry.

The entry is exactly one letter: A for coffee, B for tea, and nothing
else. This program writes that single letter to /output/entry.txt.

The letter: A — coffee.

Why A wins under the judge's own order (vivid, then funny, then true):

Vivid first. Coffee is the most sensorily alive of the two drinks:
dark, bitter, steaming, a jolt in a cup. Tea is calm and gentle, and
calm reads as less vivid, not more. The judge decides at the first
criterion where the letters differ, so vividness settles it before
anything else is weighed — and "A" itself lands like a punch: first,
short, assertive.

Funny second. Coffee owns the jokes. "Don't talk to me before my
coffee", coffee as a personality, the third refill — the humour writes
itself. Tea has ceremony and quiet; it has no punchline that lands
as fast.

True third. Coffee is the honest morning default for most of the
world, the answer that needs no apology. Tea's honest case is real —
the ritual, the centuries, the tea cultures — but it is a quieter
truth, and the judge's own rule says a later criterion only overturns
an earlier one when it differs by much more. Tea's edge on truth is
not that much more.

So A: the fuller, more alive answer, carrying the better joke and the
bolder honest stance. B was weighed and lost on vividness, the
criterion that decides first.
"""

import os

LETTER = "A"
OUTPUT_PATH = "/output/entry.txt"


def validate_letter(letter: str) -> str:
    # The gate accepts exactly one character, A or B: refuse anything
    # else (lowercase, whitespace, a word, punctuation) rather than
    # silently submit an invalid entry.
    if letter not in ("A", "B"):
        raise ValueError(f"entry letter must be A or B, got {letter!r}")
    return letter


def verify_output(path: str, letter: str) -> None:
    # Two independent checks of the gate's shape: the file is exactly
    # one byte long, and that byte is the letter. Either failing means
    # the entry is invalid, so fail loudly instead of submitting it.
    if os.path.getsize(path) != 1:
        raise ValueError(f"entry.txt must be exactly 1 byte, got {os.path.getsize(path)}")
    with open(path, "rb") as f:
        written = f.read()
    if written != letter.encode("ascii"):
        raise ValueError(f"entry.txt holds {written!r}, expected exactly {letter!r}")


def main() -> None:
    letter = validate_letter(LETTER)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(letter)
    verify_output(OUTPUT_PATH, letter)


if __name__ == "__main__":
    main()
