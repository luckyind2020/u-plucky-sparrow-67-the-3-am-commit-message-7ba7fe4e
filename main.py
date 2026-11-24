"""Print the 3 AM commit message entry for the make.fun bounty.

Reads entry.txt, the single commit-message line, validates it against
the bounty's 200-character limit, and prints it unchanged to stdout.
"""

from pathlib import Path

MAX_CHARS = 200


def load_message(path):
    text = Path(path).read_text(encoding="utf-8").strip()
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"commit message is {len(text)} chars, over the {MAX_CHARS} limit"
        )
    if "\n" in text:
        raise ValueError("commit message must be a single line")
    return text


def main():
    message = load_message(Path(__file__).with_name("entry.txt"))
    print(message)


if __name__ == "__main__":
    main()
