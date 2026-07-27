#!/usr/bin/env python3
"""Cheap prose lint: no model, five counters. Usage:
style.py FILE.tex [FILE.md ...]. Flags = rewrite
orders (see .claude/skills/prose/SKILL.md). Exit 1 if
any flag fires."""
import re, sys

FAM1 = ("delve leverage robust realm navigate intricate "
        "crucial underscore seamless comprehensive tapestry "
        "landscape showcase foster pivotal paramount "
        "holistic harness").split()

FAM2 = ["honest", "honestly", "genuinely", "truly",
        "basically", "essentially", "load-bearing",
        "doing a lot of work", "cashing out", "pushback",
        "push back", "steelman", "charitable reading",
        "worth noting", "worth flagging", "to be fair",
        "to be clear", "to be direct", "here's the thing",
        "that said", "at the end of the day",
        "the reality is", "the real question",
        "the tension is", "the tell is", "the move is",
        "the failure mode is", "gesture at", "unpack",
        "dig into", "flesh out", "non-trivial",
        "meaningfully", "materially", "nuanced",
        "granular", "compelling", "arguably", "notably",
        "it's worth", "keep in mind", "in essence",
        "boils down"]

MAXWORDS = 35     # longest sentence
COLONS   = 1.5    # per 100 words
DASHES   = 1.0    # em-dashes per 100 words
SHORTPAR = 10     # words; shorter = drumbeat suspect

def prose(txt):
    "Strip the non-prose bits of .tex/.md."
    txt = re.sub(r"(?s)\\begin\{(verbatim|BVerbatim|table"
                 r"|figure\*?|equation)\}.*?\\end\{\1\}", " ", txt)
    txt = re.sub(r"(?s)```.*?```", " ", txt)
    txt = re.sub(r"(?s)\$[^$]*\$", " ", txt)
    txt = re.sub(r"\\[a-zA-Z]+(\[[^]]*\])?(\{[^{}]*\})*", " ", txt)
    txt = re.sub(r"%.*", "", txt)
    return txt

def lint(path):
    txt   = prose(open(path).read())
    words = len(txt.split())
    if not words: return []
    out, low = [], txt.lower()
    n = low.count(":") * 100 / words
    if n > COLONS:
        out.append(f"colon rate {n:.1f}/100w > {COLONS}")
    n = (txt.count("---") + txt.count("—")) * 100 / words
    if n > DASHES:
        out.append(f"em-dash rate {n:.1f}/100w > {DASHES}")
    for s in re.split(r"[.!?]\s", txt):
        if len(s.split()) > MAXWORDS:
            out.append("run-on (%d words): %s..."
                       % (len(s.split()), " ".join(s.split()[:8])))
    for p in re.split(r"\n\s*\n", txt):
        w = p.split()
        if 0 < len(w) < SHORTPAR and not re.match(
                r"\s*([-*#|]|\d+[.)])", p):
            out.append("drumbeat paragraph: " + " ".join(w))
    hits = [w for w in FAM1 if re.search(r"\b%s\b" % w, low)]
    if hits:
        out.append("family-1 words: " + " ".join(hits))
    for p in re.split(r"\n\s*\n", low):
        hits = [w for w in FAM2 if w in p]
        if len(hits) >= 2:
            out.append("family-2 cluster: " + ", ".join(hits))
    return out

if __name__ == "__main__":
    bad = 0
    for path in sys.argv[1:]:
        for msg in lint(path):
            bad += 1
            print(f"{path}: {msg}")
    sys.exit(bad > 0)
