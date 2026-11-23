"""Six Words, One Story — entry program.

Writes one original six-word story to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output). Python 3.13 stdlib only; no network, clock, or randomness.
"""

import os

# Final story (revision 2): homecoming with a reversal.
# "She waited forty years; he knocked." ends on arrival but has no
# surprise — the knock is the expected payoff of waiting. This version
# keeps the whole-life arc (a long absence is implied by the return)
# and lands a real turn in the second clause: home, expected to
# welcome him, has forgotten him. Balanced 3 + 3 clauses, every word
# earns its place, and what happened while he was gone stays unsaid.
# Six words: He / returned / home; / nobody / remembered / him.
STORY = "He returned home; nobody remembered him."


def main() -> None:
    # Gate guard: the entry is only valid at exactly six words, 1-60 chars.
    # Fail loudly instead of silently writing an invalid story.
    assert len(STORY.split()) == 6, "story must be exactly six words"
    assert 1 <= len(STORY) <= 60, "story must be 1-60 characters"
    assert STORY.strip(), "story must not be only whitespace"
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    # No trailing newline: the file's character count is the story itself.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(STORY)


if __name__ == "__main__":
    main()
