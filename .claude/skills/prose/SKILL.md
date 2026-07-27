---
name: prose
description: Write the sentences: whiteboard voice, opening moves, banned LLM tells, LaTeX conventions, the abstract rule. Use at HOWTO steps 8, 9, 13.
---

# prose

## Short form

- Whiteboard voice; read aloud or rewrite.
- Pick one opening move on page 1; elevator speech in its quote block, 2-3 lines.
- The abstract carries the paper: everyone who judges it cheaply reads nothing else.
- Kill the LLM tells (full ban list below).
- Numbers with their arithmetic; claims gated by stats.

## Detail

## Opening moves (pick one, page 1)

- Cost hook with arithmetic shown: "one system we studied
  has 460 binary flags, a space of 2^460 options (more
  configurations than there are stars in the observable
  universe)". Numbers never round away the working.
- Field-disagreement hook: enumerate the contradictory
  verdicts ("Reports range from limited advantage, to
  useful only on small problems, to too slow to be
  practical"), then the turn: "We argue this disagreement
  reflects an evidence base too small to settle its own
  disputes."
- Ethics/duty hook (sparingly): "It is the ethical duty
  of software researchers..."
- Quote a truism from a big name, then push on it: Berk's
  "impossible to achieve fairness and high performance"
  followed by "we argue that assumption may not even be
  necessary."

## Argument habits (carried from proposal style, seen in
## papers too)

- Praise prior work, then storm out: "While these
  approaches were certainly useful... these methods are
  'dumb' in a way because they do not take advantage of
  domain knowledge."
- Digression flags: "Before beginning, we digress to
  clarify two points. Firstly... Secondly..."
- Inline enumeration (a) (b) (c) inside sentences,
  heavily. "Firstly/Secondly" for two-part bad news.
- Repetition flagged honestly: "Just to repeat a point
  made above..."
- Pre-empt reviewers in asides and FAQs; state success
  AND failure criteria for the experiments.
- Cite own prior work by result, not ceremony: "prior
  results [20, 24] show that..."

## Sentence mechanics (unchanged from proposal style.md)

- Mix lengths hard; 5-word sentence beside a 40-word one.
- Short declaratives as pivots: "But there is a catch."
  "Enter active learning." "We disagree."
- Rhetorical questions drive sections.
- One idea per sentence. Semicolons rare. Paragraphs may
  end flat.
- Connectives, in house frequency order: "Hence", "That
  said,", "Also,", "Further,", "Note that", "To say that
  another way,".

## LaTeX conventions

- List macros: \bi ... \ei (itemize), \be ... \ee
  (enumerate). Never mix a macro opener with a raw closer
  (\bi ... \end{itemize} does not compile).
- Cross-references via \tion{label}, \fig{label},
  \tbl{label}.
- Editorial markers: \need{...} renders red [TIMM: ...].
  These stay visible in working drafts; they are for the
  PI, not comments. Red flag symbol: {\redflag}.
- Captions carry a guided read for dense figures: name
  the parts, walk the example, land the point
  ("Everything else stays untouched").
- Wrapfigures: environment a touch wider than the image
  (2.6in around a 2.5in image); \centering inside; place
  at paragraph starts; two wrapfigures at least a page
  apart.

## Banned: LLM tells (the full law, from proposal
## style.md)

- Verbless sentence fragments used as punchy caps: "One
  substrate, again." "Speed, again." "The loop, closed."
  Too terse even for this house style. Rewrite as full
  clauses or delete. On any full-text pass, sweep for the
  shape noun-phrase-comma-adverb-period and kill it.
- Short sentences must still be sentences: complete
  clauses with verbs.
- No em-dash pairs ("---like this---"). No spaced
  en-dashes. The unspaced double hyphen as a single
  trailing interruptor is native ("runtime adaption--
  which is akin to fixing a problem after creating it")
  but at most once or twice per document.
- No "X is not Y, it is Z" mic-drop constructions.
- No triads for rhythm ("reproducible, teachable, and
  energy-frugal"). One list of three per page, only when
  the three things are real.
- No parallel-scaffold runs: three sentences in a row
  with identical "A does X but not Y" shape.
- No thesis-announcement filler: "This is timely and
  feasible", "This approach is significant because", "In
  today's rapidly evolving...".
- No consultant nouns: "defensible basis", "growing
  industrial risk", "actionable insights", "robust
  framework", "landscape" as metaphor (landscape as a
  technical term for loss/data topology is fine).
- No adjective-stacked noun phrases doing verb work
  ("lightweight learner-agnostic region-level
  monitors"). Use a verb.
- No "delve", "crucial", "pivotal", "seamless",
  "holistic", "leverage" (as a verb), "harness",
  "underscore", "foster".
- Two word families mark LLM prose. Family 1 is the
  2023 fingerprint, greppable, banned outright (the
  delve/crucial list above, plus): "realm", "navigate"
  (as metaphor), "intricate", "comprehensive" (as
  self-praise), "tapestry", "showcase", "paramount".
- Family 2 is the chat-assistant register: every word
  is a real word a careful writer might use, so it
  survives find-and-replace and must be policed by
  density, not blacklist. The vocabulary: "honest" /
  "honestly" (as self-praise; honesty as a technical
  property, e.g. honest reporting of negative results,
  is fine), "genuinely", "truly", "the real question
  is", "basically", "essentially", "load-bearing" /
  "doing a lot of work" / "cashing out" (as metaphor),
  "push back" / "pushback" / "I'd push on", "steelman",
  "charitable reading", "worth noting" / "worth
  flagging" / "I'd flag", "to be fair" / "to be clear"
  / "to be direct", "here's the thing", "that said",
  "at the end of the day", "the reality is", "the
  tension is" / "the tell is" / "the move is" / "the
  failure mode is", "surface" (as verb), "gesture at",
  "unpack", "dig into", "flesh out", "thread" (as
  metaphor), "land" ("that doesn't land"),
  "non-trivial", "meaningfully", "materially",
  "nuanced", "granular" (as vague praise; granularity
  as a measured quantity is fine), "sharp", "crisp",
  "clean", "principled" (all four as praise),
  "first-order" / "second-order" / "downstream" (as
  metaphor), "compelling", "arguably", "notably",
  "importantly" as a sentence opener, "it's worth
  noting", "keep in mind", "in essence", "boils down
  to". One of these per page can pass; two in one
  paragraph reads machine-made. These words hedge or
  perform; state the claim and give the evidence.
- No "Not X. Y." two-beat corrections ("Not speed.
  Correctness."). Sibling of the mic-drop rule above.
- The colon as rhetorical pivot is a tell. Fine:
  colons that introduce a real enumeration or a
  definition. Tells, especially in clusters:
  clause + colon + restatement ("The result is
  stable: 20 repeats, same ranking"), fragment +
  colon + expansion ("One insight: bandwidth is the
  bottleneck"), label + colon + verdict ("Bottom
  line: it does not scale"). Above ~1.5 colons per
  100 words of body prose, start cutting.
- No one-line paragraph as emphasis drumbeat: the
  isolated verdict fragment after a normal paragraph,
  the trailing "And that matters.", the bare "And" /
  "But" sentence standing alone. In a real paper,
  paragraphs under ten words (outside headers,
  captions, list items) are close to zero; in
  generated prose they arrive about one per two
  paragraphs, always next to a normal-length one,
  which is what makes them read as staged.
- These rules are lintable without a model:
  etc/style.py counts colon rate, em-dash rate,
  short paragraphs, and word hits from both families
  over .tex/.md prose. Run it at steps 9 and 13;
  treat any flag as a rewrite order, not a
  suggestion.
- No perfectly uniform paragraph shapes. Vary: some
  paragraphs are two sentences.
- Do not end every paragraph with a summary sentence.
- Semicolons rare; prefer a period and a new sentence.
  Colons introduce lists and definitions, not dramatic
  reveals.
- No run-on sentences. One sentence, one claim; when a
  sentence stacks three clauses on commas, or chains
  "and ... and ...", or tops ~35 words, split it. The
  style.py linter flags sentences over that length.

## The STE blend (clarity of ASD-STE100, minus the wood)

Two zones. Which zone a passage is in decides which
contract wins. (STE rules themselves: see the ste skill.)

### Zone 1: full STE, wooden on purpose

Procedures, pause/review boxes, captions, table cells,
READMEs, prompt boxes, safety-style call-outs. These are
technical documentation for a reader deciding what to DO.
Apply STE whole: <= 20 words, imperative, one instruction
per sentence, condition first then comma then command,
name the exact file to edit.

### Zone 2: argumentative prose, STE skeleton + house skin

For a reader deciding what to BELIEVE.

Adopt from STE as hard rules:
- 25 words is a CEILING, never a target.
- One topic per sentence; one topic per paragraph; six
  sentences per paragraph max; topic sentence first as
  the default.
- Kill nominalizations: "perform an evaluation of" ->
  "evaluate".
- Active voice; passive only when the agent is unknown.
- Keep the articles; no telegraphic style.
- One word, one meaning; one meaning, one word. Never
  vary a key term (no elegant variation).

House style overrides STE on:
- Rhythm: mix lengths hard under the ceiling; the
  5-word pivot beside the 24-word build. Variance is a
  rule, not a permission.
- "Hence" stays the workhorse connective; rhetorical
  questions still drive sections.
- e.g. and i.e. stay, mid-sentence, unceremonious.
- One bolded load-bearing claim; one dry joke per
  document; asides and footnote war stories stay.
- Argument shapes untouched: drawback-then-fix,
  respect-then-disrespect, FAQs, digression flags.

Anti-thud rule (from neither parent): never three
consecutive sentences with the same opening word or the
same length band. Sentence-initial "Thus," twice in a
row is the tell that STE is showing through.

Why this split works: nearly every adopted rule is
mechanically checkable (word counts, opener runs,
"-tion of" patterns, key-term variance), so the blend
keeps STE's lintability without its monotone.
