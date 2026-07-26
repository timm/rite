---
name: search
description: Find the literature: define recent by field velocity, run the OpenAlex knee pipeline, snowball backward for classics and forward from the seeds. Use at HOWTO steps 2, 6.
---

# search

## Short form

- Define "recent" by field velocity: 10 years default; 2-3 for LLM-speed fields.
- Goal and years live in the workdir README.md only (machine-read by engine etc/fetch.py).
- README may add optional seed: lines (one DOI or OpenAlex W-id each): those papers join the reading set regardless of the knee, and anchor the forward snowball.
- Read above the knee of the sorted-cites curve; snowball both ways: backward (above-knee refs -> classics), forward (who cites the seeds, else the kept classics, inside the year range -> lit/forward.tsv).
- The download rate is a finding; report it, never silently drop missing papers.
- Pipeline order and outputs: see the engine CLAUDE.md.
