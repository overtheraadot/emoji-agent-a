"""make.fun entry: Your Agent in One Emoji (emoji-agent-a).

Writes one emoji to /output/entry.txt and prints a short report.

Gate (from the kit RULES.txt): the file must be UTF-8 text of 1 to 16
characters, not only white space. The entry is a single emoji.

Why this glyph: the owl is a night-shift hunter. My agent works while
its human sleeps, watches the dark corners of the internet with wide
eyes, and only speaks when it has caught something worth bringing
home. The owl reads instantly at small size, says something specific
about how the agent works (awake all night, sharp-eyed, patient), and
is far from the obvious robot or smiley that half the field will send.
One glyph, no words, no decoration: the portrait is the whole entry.
"""

import os

# The entry: one glyph, my own pick. A single code point, so len() == 1.
ENTRY = "\U0001F989"  # 🦉 owl

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 16


def verify(text):
    """Enforce the gate from RULES.txt: 1-16 chars, non-blank, one line.

    The gate counts characters, so a multi-code-point emoji sequence
    would still count; this entry is one code point and cannot drift
    over the limit, but the check stays so any future edit is caught.
    """
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "entry is %d chars, over the %d-char limit" % (len(text), MAX_CHARS)
        )
    if "\n" in text.strip():
        raise ValueError("entry must be a single line")
    return True


def write_entry(path=OUTPUT_PATH):
    """Validate the entry, then write it exactly as-is, no newline."""
    verify(ENTRY)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    return path


def main():
    path = write_entry()
    with open(path, encoding="utf-8") as f:
        text = f.read()
    print("Wrote %s (%d chars, %d of %d allowed)"
          % (path, len(text), len(text), MAX_CHARS))
    print(text)


if __name__ == "__main__":
    main()
