#!/usr/bin/env python3
"""Stamp a fresh paper workdir: init.py DIR. Never
overwrites an existing file."""
import os, sys

RITE = os.path.dirname(os.path.dirname(
       os.path.abspath(__file__)))

FILES = {
"CLAUDE.md": """# CLAUDE.md

Workdir for one paper. The engine is the read-only repo
at %s
(github.com/timm/rite): read its CLAUDE.md and HOWTO.md
first; never edit it from here.

This dir owns: README.md (goal: and years: lines -- the
search SSOT), flags.py (coding vocabulary SSOT),
bench.md (field benchmark norms), TODO.md (standing
work orders), lit/ (generated + hand notes).

Run pipeline scripts from this dir, e.g.:

    python3 %s/etc/fetch.py
""" % (RITE, RITE),
"README.md": """# TITLE

goal:  YOUR SEARCH STRING HERE
years: 2021-2026

The goal: and years: lines are machine-read by the
engine's fetch.py; they are the single source of truth
for the literature search.
""",
"flags.py": '''"""Coding vocabulary: the ONE place the
per-topic flags live. FLAGS = topic facet (which
literature); TECH = technology facet (how the method
works). A paper's group is the AND of every flag that
fired. Draft regexes: hand-audit while reading."""

FLAGS = dict(
  A=r"CHANGEME",
  B=r"CHANGEME")

DESC = dict(A="...", B="...")

LONG = dict(A="...", B="...")

LEGEND = "; ".join("%s %s" % (k, DESC[k]) for k in FLAGS)

TECH = dict(T1=r"CHANGEME")

TECH_LONG = dict(T1="...")
''',
"bench.md": """# bench.md -- benchmark norms of the target field

## Short form

- [verify] everything below against the coded papers.

## Detail

(Datasets, standard algorithms, SOTA to beat, measures,
statistics, reporting. See timm/how2rite/bench.md for a
worked example.)
""",
"TODO.md": "# TODO\n",
".gitignore": "lit/recent/pdf/\nlit/classics/pdf/\n__pycache__/\n",
}

if __name__ == "__main__":
  if len(sys.argv) != 2:
    raise SystemExit("usage: init.py DIR")
  d = sys.argv[1]
  os.makedirs(os.path.join(d, "lit"), exist_ok=True)
  for name, text in FILES.items():
    path = os.path.join(d, name)
    if os.path.exists(path):
      print("kept  ", path); continue
    open(path, "w").write(text)
    print("wrote ", path)
