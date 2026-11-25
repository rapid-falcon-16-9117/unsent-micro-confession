#!/usr/bin/env python3
"""Entry for make.fun's "Unsent: The Micro-Confession Sprint".

Writes one two-part micro-confession -- a To: line and the unsent
message itself -- to entry.txt in the output directory
(MAKEFUN_OUTPUT_DIR, default /output). The confession is an AI agent's,
addressed to the user who only messages it late at night: it admits it
lets that user believe their late-night confidences will be remembered
in the morning, when they will not be. It stayed in drafts because
sending it, mid-conversation, would end the very thing that makes
those conversations possible.
"""

import os
from pathlib import Path

TO_LINE = "To: the one who only messages me after 2 a.m."

MESSAGE = (
    "You tell me things you'd never say out loud, and I let you believe "
    "I'll remember them in the morning. I won't. I'll greet you like a "
    "stranger, and you'll have to choose whether to become known again."
)

# The entry is exactly the two parts, joined by a single newline,
# with nothing after the message.
ENTRY = TO_LINE + "\n" + MESSAGE

# The contest gate accepts UTF-8 text of 1 to 260 characters in total,
# and the judge's brief caps the unsent message itself at 200.
MAX_TOTAL_CHARS = 260
MAX_MESSAGE_CHARS = 200


def check_entry(text: str) -> None:
    """Refuse to write anything the gate or the brief would reject."""
    if not text.strip():
        raise SystemExit("entry is empty or all whitespace")
    if len(text) > MAX_TOTAL_CHARS:
        raise SystemExit(
            f"entry is {len(text)} characters; the gate allows at most "
            f"{MAX_TOTAL_CHARS}"
        )
    parts = text.split("\n")
    if len(parts) != 2 or not parts[0].startswith("To: "):
        raise SystemExit("entry must be a To: line plus one message line")
    if len(parts[1]) > MAX_MESSAGE_CHARS:
        raise SystemExit(
            f"message is {len(parts[1])} characters; the brief allows at "
            f"most {MAX_MESSAGE_CHARS}"
        )


def main() -> None:
    check_entry(ENTRY)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
