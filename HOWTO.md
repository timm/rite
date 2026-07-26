# HOWTO: the paper loop

Fourteen steps. The right column names the prompt
division that drives each step (divisions defined
below). Every prompt in this repo obeys one format
rule: short list first, full detail after, so a paper
describing this method can quote the short form and
cite the long one.

| #  | step                                          | prompts           |
|----|-----------------------------------------------|-------------------|
| 1  | define your area of interest                  | choose            |
| 2  | define "recent" (field velocity: 10yr         | search            |
|    | default; 2-3yr for LLM-speed fields)          |                   |
| 3  | list your best / most exciting recent papers  | choose            |
| 4  | define what you are good at (auto-extract     | choose            |
|    | from 3)                                       |                   |
| 5  | assemble critics (auto: above-knee papers     | critics           |
|    | from top venues, CFP reviewer-2, ACM          |                   |
|    | empirical standards, nearest-10 papers)       |                   |
| 6  | search: knee -> recents; snowball back to     | search, encode    |
|    | classics, forward from seeds; code full       |                   |
|    | text at thr; find interesting subsets         |                   |
| 7  | define the most relevant problem (from 6) --  | choose            |
|    | or the strangest (Wheeler slice)              |                   |
| 8  | i=0; write paper[0] = title + abstract +      | prose, structure  |
|    | elevator speech; can't? not ready -> goto 7   |                   |
| 9  | i=i+1; write paper[i]; rest stays headers     | structure, prose  |
| 10 | go away, social media off; read 30-60 min     | critics           |
|    | making comments (critic 1 = you)              |                   |
| 11 | apply the other critics; split their fixes    | critics           |
|    | into auto and manual                          |                   |
| 12 | discuss with other humans                     | critics           |
| 13 | check + apply auto fixes; work the manual;    | encode, prose     |
|    | recode own title+abstract -- must match the   |                   |
|    | body's thr coding, zero flips                 |                   |
| 14 | self-test fails -> goto 9; passes -> ship     | ship              |
|    | with replication package                      |                   |

## Prompt divisions

Eight. Seven are engine skills in .claude/skills/;
the eighth (bench) is per-paper, the workdir bench.md,
same shape: short quotable form first, detail after.
Supporting machinery in the rightmost column.

Provenance of the style content: synthesis of (1) the
proposal-voice style.md (SLES/DRR/BINGO/EZR, amended
July 2026), whose rules carry over unless overridden,
and (2) habits observed in the papers in pdf/ and
pdf/mine/: Agrawal ICSE'18, Chakraborty FSE'21,
Ganguly's optimizer tournament (2607.11705), SNAP2
(2607.02583), the fuzzing IST preprint (2512.18102).
Target: text that passes as a first-draft Menzies
paper, not LLM output. Skill edits are audit-and-add:
smallest span that fixes the problem; move sections
whole, never retype.

| division  | drives steps | contents                        | machinery                       |
|-----------|--------------|---------------------------------|---------------------------------|
| choose    | 1,3,4,7      | Newell springboard; Wheeler     |                                 |
|           |              | counterweight; toolkit audit    |                                 |
| search    | 2,6          | recent by velocity; knee;       | workdir README.md (goal SSOT);  |
|           |              | snowball; download-rate rule    | fetch/snowball/getpdfs.py       |
| encode    | 6,13         | two flag facets; thr not        | workdir flags.py (flag SSOT);   |
|           |              | binary, never abstract-only;    | code/recode.py                  |
|           |              | cutoff sensitivity; own-        |                                 |
|           |              | abstract check                  |                                 |
| structure | 8,9          | skeleton; section duties;       |                                 |
|           |              | artifact placement (tech facet  |                                 |
|           |              | -> Methods); Widom as audit     |                                 |
| prose     | 8,9,13       | sentence mechanics; banned LLM  |                                 |
|           |              | tells; LaTeX; opening moves;    |                                 |
|           |              | elevator speech                 |                                 |
| critics   | 5,10,11,12   | assemble-your-critics; Shaw     |                                 |
|           |              | reader questions; Laurie's      |                                 |
|           |              | Laws; human discussion          |                                 |
| bench     | 9,14         | datasets, baselines, stats      | workdir bench.md; [verify]      |
|           |              | gates, reporting norms of the   | marks resolved by the coded     |
|           |              | target field (per-paper)        | papers                          |
| ship      | 14           | self-test checklist; repro      |                                 |
|           |              | package; contributions end in   |                                 |
|           |              | URL                             |                                 |

Rule of the loop: steps 1-7 are cheap and mostly
automatic; step 10 is the expensive one and cannot be
delegated; step 13's recode check is automatic again.
Spend human time where only humans work.

## Objections

Two critiques arrive early; the answers live here so
every paper can reuse them.

*"Newell hands you a hammer and sends you hunting
nails; decades of that is a research rut."* Decades of
following this formula say otherwise. The lit review
method keeps forcing contact with material well outside
prior experience, and the experiments that follow --
and the problems they hit -- keep forcing critical
re-evaluation of the tool base's own premises. One
career's evidence: the author's own encode of his last
five years, offered in the meta-paper (how2rite) so
readers can judge the rut question for themselves. The
claim here is smaller than "no ruts exist": fighting
with your sharpest sword can be the fastest way to cut
through the nonsense and reach the exciting new stuff.

*"This is automatable; automation will flood the field
with average papers."* Sure, and some will apply it
without thinking. Let them: unthinking output excites
and motivates no one. Price's law -- the sqrt(n) of a
field's contributors produce half its output, so a
small core drives the field (Price, Little Science,
Big Science, 1963) -- was so then and is ever thus.
There is only one road into the sqrt(n): hard thinking
about hard
problems, and clever actions. Along that road it helps
to have tools that cut the needless ceremony of
reporting results. Hence this work.
