# rite: an engine for writing SE research papers

A 14-step loop (HOWTO.md), eight prompt divisions
(seven skills in .claude/skills/ plus a per-paper
bench.md), and an OpenAlex literature pipeline
(etc/*.py). Papers live in their own workdirs; this
repo stays read-only while writing.

Start a paper:

    git clone https://github.com/timm/rite
    python3 rite/etc/init.py mypaper
    cd mypaper       # fill in README.md goal: line
    claude           # follow the loop in rite/HOWTO.md

Worked example: https://github.com/timm/how2rite --
a meta-paper applying the method to itself.
