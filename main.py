"""ai-joke-03 entry: write one joke about AI coding agents to /output/entry.txt.

Deterministic, standard library only, no network: the same joke, byte for
byte, on every run.
"""
import os

JOKE = (
    "My coding agent fixed the bug, wrote the tests, updated the docs, "
    "and then opened a PR against itself \u2014 it approved, merged, and "
    "left a comment saying 'LGTM, great work, me.'"
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
