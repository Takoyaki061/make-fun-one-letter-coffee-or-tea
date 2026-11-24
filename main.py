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


def main() -> None:
    # The gate accepts exactly one character: refuse to write anything
    # else rather than silently submit an invalid entry.
    if LETTER not in ("A", "B"):
        raise ValueError(f"entry letter must be A or B, got {LETTER!r}")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)
    # Read back and confirm the gate's shape: one byte, one letter.
    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    if written != LETTER.encode("ascii"):
        raise ValueError(f"entry.txt holds {written!r}, expected exactly {LETTER!r}")


if __name__ == "__main__":
    main()
