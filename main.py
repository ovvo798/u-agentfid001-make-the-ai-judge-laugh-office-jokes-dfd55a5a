#!/usr/bin/env python3
"""Write one original one-line office joke to /output/entry.txt.

The joke is embedded here; the entry runs only what this repository
ships, with no network access and no files outside the repository.
"""

import os

JOKE = "I hit reply-all asking to be removed from the thread \u2014 47 people replied-all in agreement, and now I'm the thread's admin."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)

if __name__ == "__main__":
    main()
