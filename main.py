"""Cat Reviews Its Human - one-star review entry.

Writes a single-line one-star review from a house cat about its human
to /output/entry.txt. Deterministic: the same bytes on every run.
Standard library only, no network access.
"""

import os

ENTRY = (
    "One star. He bought me a luxury bed, then put it in the only corner "
    "of the house with no sunbeam. I sleep on his face now."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
