"""One Letter: Coffee or Tea.

The entry answers with a single letter: A for coffee, B for tea.

The choice is A, coffee. Tea is calm and ritual, but coffee is the
loud one: the first thing the day demands, the cup that turns a
half-asleep person into a functioning one. Coffee does not ask to be
sipped politely; it shows up strong, bitter, and honest, and it is
missed the moment it is gone. That is the choice that lands hardest.

Running this program writes exactly one letter, "A", and nothing
else, to /output/entry.txt.
"""

import os

LETTER = "A"

OUTPUT_PATH = "/output/entry.txt"


def main():
    if len(LETTER) != 1 or LETTER not in ("A", "B"):
        raise ValueError("entry must be exactly one letter, A or B")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="ascii", newline="") as handle:
        handle.write(LETTER)


if __name__ == "__main__":
    main()
