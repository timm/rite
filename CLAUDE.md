# CLAUDE.md

rite is the paper-writing engine: the HOWTO loop, the
prompt-division skills, and the literature pipeline. At
paper-writing time this repo is READ-ONLY -- each paper
lives in its own workdir (its own repo) and never edits
this one. Method improvements land here; every paper
benefits.

## Read order

HOWTO.md (the 14-step loop and the eight prompt
divisions), then the skills under .claude/skills/ --
they govern ALL prose, including the banned-LLM-tells
list (prose) and the shipping self-test (ship).

## Engine vs workdir

Engine (this repo): CLAUDE.md, HOWTO.md, seven skills,
etc/*.py, pdf/ (style-source papers).

Workdir (one per paper; stamp with etc/init.py DIR):

    CLAUDE.md   pointer back to this engine
    README.md   goal: and years: lines; SSOT for the
                literature search (fetch.py reads it);
                optional seed: lines (published DOI or
                OpenAlex W-id) force papers into the
                reading set and anchor the forward
                snowball
    flags.py    coding vocabulary; SSOT for the flags
    bench.md    benchmark norms of the target field,
                with [verify] marks (the eighth prompt
                division, per-paper)
    TODO.md     standing work orders
    lit/        pipeline output + hand-written notes

## Pipeline (run from the WORKDIR root, in order)

    python3 $RITE/etc/fetch.py     OpenAlex search of
        the workdir README goal -> lit/papers.tsv,
        lit/cites.txt (knee marked), lit/read.tsv
    python3 $RITE/etc/snowball.py  backward snowball ->
        lit/classics.tsv, lit/read-classics.tsv;
        forward snowball from the seeds (else the kept
        classics) -> lit/forward.tsv
    python3 $RITE/etc/stubs.py     lit/{recent,classics}/
        index.tsv + note stubs (never overwrites)
    python3 $RITE/etc/code.py      abstract coding ->
        lit/*/coding.tsv, lit/coding.md
    python3 $RITE/etc/getpdfs.py   open-access PDFs ->
        lit/*/pdf/NN.pdf (NN = index.tsv row)
    python3 $RITE/etc/recode.py    full-text recode ->
        lit/coding-full.md

$RITE = wherever this repo is cloned.

## Hard rules

1. Never write into this repo during paper work; all
   generated files land in the workdir.
2. Search goal lives in the workdir README.md only;
   coding vocabulary in the workdir flags.py only.
   Never restate either in a script.
3. Never code papers from title+abstract alone.
   Measured (n=22, first exhibit): abstracts missed
   about half the topic flags. Code full text.
4. Naive binary matching over full text saturates
   (every 10-page PDF mentions everything once). Use
   recode.py's per-1k threshold; binary columns exist
   only to document the artifact.
5. Keyword coding is a draft. Hand-audit rows while
   reading. Hand-written notes in lit/ stubs and
   lit/coding-notes.md; no script may overwrite them.
6. Expect roughly half the recents and a fifth of the
   classics to have open-access PDFs. The download
   rate is a finding: report it, never silently drop
   the missing papers.
7. All prose, including this file, obeys the prose and
   structure skills.
