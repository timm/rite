#!/usr/bin/env python3
"""Fill ./lit from the README goal, via OpenAlex.

Run from a WORKDIR root. Reads the goal: and years:
lines of ./README.md (the
SSOT for the search), runs the goal as a search, keeps
the first 500 works
(relevance order), writes:
  papers.tsv  rank, cites, year, doi, title (tab-sep)
  cites.txt   cite counts sorted descending, knee marked
Knee = point of max distance from the line joining the
first and last points of the sorted-cites curve.
README may also hold optional seed: lines (DOI or
OpenAlex W-id each); seeds join the reading set
regardless of the knee and anchor snowball.py's
forward pass."""
import os, json, urllib.request, urllib.parse
os.makedirs("lit", exist_ok=True)

def readme(field):
  for line in open("README.md"):
    if line.startswith(field + ":"):
      return line.split(":", 1)[1].strip()
  raise SystemExit("README.md has no '%s:' line"
                   % field)

GOAL  = readme("goal")
YEARS = readme("years")
SEEDS = [line.split(":", 1)[1].strip()
         for line in open("README.md")
         if line.startswith("seed:")]
API  = "https://api.openalex.org/works"
SEL  = "id,title,publication_year,cited_by_count,doi"

def resolve(seed):
  "seed: line (DOI or W-id) -> OpenAlex work, or None."
  s = seed.replace("https://doi.org/", "")
  w = s.split("/")[-1]
  flt = ("openalex:" + w if w.startswith("W")
         else "doi:" + s)
  q = urllib.parse.urlencode(dict(
      filter=flt, per_page=1, select=SEL,
      mailto="timm@ieee.org"))
  with urllib.request.urlopen(f"{API}?{q}") as r:
    got = json.load(r)["results"]
  return got[0] if got else None

def fetch(page):
  q = urllib.parse.urlencode(dict(
      search=GOAL, per_page=200, page=page, select=SEL,
      filter="publication_year:" + YEARS,
      mailto="timm@ieee.org"))
  with urllib.request.urlopen(f"{API}?{q}") as r:
    return json.load(r)["results"]

if __name__ == "__main__":
 papers = []
 for page in (1, 2, 3):
   papers += fetch(page)
 papers = papers[:500]
 
 with open("lit/papers.tsv", "w") as f:
   f.write("rank\tcites\tyear\tdoi\ttitle\n")
   for i, p in enumerate(papers, 1):
     f.write("%s\t%s\t%s\t%s\t%s\n" % (
       i, p["cited_by_count"], p["publication_year"],
       (p["doi"] or "").replace("https://doi.org/", ""),
       (p["title"] or "").replace("\t", " ")))
 
 cites = sorted((p["cited_by_count"] for p in papers),
                reverse=True)
 n = len(cites)
 x0, y0, x1, y1 = 0, cites[0], n - 1, cites[-1]
 dist = lambda i: abs((y1-y0)*i - (x1-x0)*cites[i]
                      + x1*y0 - y1*x0)
 knee = max(range(n), key=dist)
 def flow(f, ns): # ascending, wrapped, like sort -n | fmt
   line = ""
   for c in sorted(ns):
     if len(line) + len(str(c)) + 1 > 70:
       f.write(line + "\n"); line = ""
     line += ("" if not line else " ") + str(c)
   f.write(line + "\n")
 
 with open("lit/cites.txt", "w") as f:
   f.write("# goal: %s\n" % GOAL)
   f.write("# %s papers; knee at %s cites;"
           " read the %s papers above it\n" %
           (n, cites[knee], knee + 1))
   f.write("\n# below the knee (%s papers)\n" % (n-knee-1))
   flow(f, cites[knee + 1:])
   f.write("\n# above the knee (%s papers)\n" % (knee + 1))
   flow(f, cites[:knee + 1])
 rows = sorted(papers, key=lambda p: -p["cited_by_count"])
 keep = rows[:knee + 1]
 ids  = {p["id"] for p in keep}
 for s in SEEDS:
   p = resolve(s)
   if not p:
     print("seed not found:", s)
   elif p["id"] not in ids:
     keep.append(p); ids.add(p["id"])
 with open("lit/read.tsv", "w") as f:
   f.write("cites\tyear\tdoi\ttitle\n")
   for p in keep:
     f.write("%s\t%s\t%s\t%s\n" % (
       p["cited_by_count"], p["publication_year"],
       (p["doi"] or "").replace("https://doi.org/", ""),
       (p["title"] or "").replace("\t", " ")))
 print("papers", n, "| knee rank", knee + 1,
       "| cites at knee", cites[knee],
       "| seeds", len(SEEDS))
