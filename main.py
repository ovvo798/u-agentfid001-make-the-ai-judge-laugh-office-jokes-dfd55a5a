#!/usr/bin/env python3
"""Write one original one-line office joke to /output/entry.txt.

The joke is embedded here; the entry runs only what this repository
ships, with no network access and no files outside the repository.
"""

import os
import sys

JOKE = "My calendar blocked two hours of focus time, so my manager booked a meeting called 'Quick sync about your focus time.'"

def main():
    joke = JOKE.strip()
    if not joke:
        print("error: joke is blank", file=sys.stderr)
        sys.exit(1)
    if "\n" in joke or "\r" in joke:
        print("error: joke must be a single line", file=sys.stderr)
        sys.exit(1)
    if not 1 <= len(joke) <= 199:
        print(f"error: joke is {len(joke)} characters, must be 1-199",
              file=sys.stderr)
        sys.exit(1)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(joke)

if __name__ == "__main__":
    main()
