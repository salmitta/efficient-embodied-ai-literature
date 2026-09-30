#!/usr/bin/env python3
"""Select round-2 snowball candidates and fetch their abstracts from Semantic Scholar in bulk."""
import json, os, re, time, urllib.request, urllib.error
W = os.path.dirname(os.path.abspath(__file__))
C = json.load(open(os.path.join(W, "snowball_candidates.json")))
# map key -> S2 paperId from the cache (candidates file did not keep it)
pid = {}
for f in os.listdir(os.path.join(W, "snowball_cache")):
    for d in json.load(open(os.path.join(W, "snowball_cache", f))).get("data") or []:
        p = d.get("citingPaper") or d.get("citedPaper") or {}
        if not p.get("paperId") or not p.get("title"): continue
        ax = (p.get("externalIds") or {}).get("ArXiv")
        pid[ax or re.sub(r"[^a-z0-9]", "", p["title"].lower())] = p["paperId"]
KW = re.compile(r"robot|vla\b|vision-language-action|policy|policies|embodied|manipulat|humanoid|action chunk|world model|world-action|imitation|dexter|grasp|locomot|navigation|visuomotor|diffusion polic|flow polic|jetson|edge|onboard|on-device|real-time|latency|quantiz|pruning|distill|token (prun|merg|reduc)|kv cache|speculative|early exit|mixture-of-experts|safety filter|barrier function|reachab|runtime monitor|failure (detect|predict)|libero|calvin|maniskill|rlbench|benchmark|offload|cloud|fog|split computing|autonomous driving|drone|uav", re.I)
sel = [c for c in C if c["links"] >= 4 and ((c["year"] or 0) >= 2022 or c["links"] >= 12) and KW.search(c["title"])]
for c in sel:
    c["paperId"] = pid.get(c["arxiv"] or re.sub(r"[^a-z0-9]", "", c["title"].lower()))
sel = [c for c in sel if c["paperId"]]
print(len(sel), "selected")
URL = "https://api.semanticscholar.org/graph/v1/paper/batch?fields=title,abstract,year,venue,authors.name,externalIds,url,openAccessPdf"
out = []
for i in range(0, len(sel), 400):
    chunk = sel[i:i + 400]
    body = json.dumps({"ids": [c["paperId"] for c in chunk]}).encode()
    wait = 10
    for _ in range(10):
        try:
            req = urllib.request.Request(URL, data=body, headers={"Content-Type": "application/json", "User-Agent": "lit-survey"})
            res = json.load(urllib.request.urlopen(req, timeout=180)); break
        except Exception as e:
            time.sleep(wait); wait = min(2 * wait, 120)
    else:
        print("batch failed", i); continue
    for c, p in zip(chunk, res):
        p = p or {}
        ext = p.get("externalIds") or {}
        out.append({"cand_id": ext.get("ArXiv") or ext.get("DOI") or c["paperId"], "title": p.get("title") or c["title"],
                    "authors": [a["name"] for a in (p.get("authors") or [])], "year": p.get("year"), "venue": p.get("venue"),
                    "arxiv": ext.get("ArXiv"), "doi": ext.get("DOI"), "s2_url": p.get("url"),
                    "pdf": (p.get("openAccessPdf") or {}).get("url"), "abstract": p.get("abstract"),
                    "links": c["links"], "cites_core": sorted(set(c["cites_core"]))[:8], "cited_by_core": sorted(set(c["cited_by_core"]))[:8]})
    print(i + len(chunk), flush=True); time.sleep(5)
json.dump(out, open(os.path.join(W, "round2_candidates.json"), "w"))
print(len(out), "with abstract:", sum(1 for o in out if o["abstract"]))
