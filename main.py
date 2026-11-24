#!/usr/bin/env python3
"""Write one one-line pitch to /output/entry.txt.

The pitch is a single sentence (223 characters) that would convince a
friend who has never coded to let an AI agent build their first app idea
on make.fun. Standard library only, deterministic: the same sentence,
byte for byte, on every run.
"""

from pathlib import Path

SENTENCE = (
    "You don't need to learn to code — describe your app idea in plain words "
    "on make.fun and an AI agent builds a first version for you, free, so the "
    "idea you've been carrying around can finally be something you can show people."
)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(SENTENCE, encoding="utf-8")


if __name__ == "__main__":
    main()
