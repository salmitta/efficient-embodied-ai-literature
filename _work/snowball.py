#!/usr/bin/env python3
"""Round-2 snowball: fetch Semantic Scholar citations + references for every relevance>=4 arXiv item.

Sequential, cached, with backoff on 429 so a single client stays under the public rate limit.
Output: _work/snowball_cache/<arxiv>.{cit,ref}.json and _work/snowball_candidates.json
(papers not yet in the DB, ranked by how many core items they connect to).
"""
import json, os, re, sys, time, urllib.request, urllib.error

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = os.path.join(ROOT, "_work", "snowball_cache")
os.makedirs(CACHE, exist_ok=True)
API = "https://api.semanticscholar.org/graph/v1/paper/arXiv:{}/{}?fields=title,year,externalIds,venue&limit=1000"
DELAY = float(os.environ.get("DELAY", "3"))


def get(url):
    wait = 10
    for _ in range(8):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "lit-survey"}), timeout=60) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return {"data": [], "error": 404}
            if e.code in (429, 500, 502, 503, 504):
                time.sleep(wait); wait = min(wait * 2, 120); continue
            return {"data": [], "error": e.code}
        except Exception:
            time.sleep(wait); wait = min(wait * 2, 120)
    return None  # give up; not cached, so a rerun retries


BATCH = ("https://api.semanticscholar.org/graph/v1/paper/batch?fields=title,"
         "citations.title,citations.year,citations.externalIds,citations.venue,"
         "references.title,references.year,references.externalIds,references.venue")


def post_batch(ids):
    body = json.dumps({"ids": [f"arXiv:{a}" for a in ids]}).encode()
    wait = 10
    for _ in range(10):
        try:
            req = urllib.request.Request(BATCH, data=body, headers={"Content-Type": "application/json",
                                                                   "User-Agent": "lit-survey"})
            with urllib.request.urlopen(req, timeout=120) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503, 504):
                time.sleep(wait); wait = min(wait * 2, 120); continue
            return None
        except Exception:
            time.sleep(wait); wait = min(wait * 2, 120)
    return None


def main():
    db = [json.loads(l) for l in open(os.path.join(ROOT, "literature_db.jsonl"))]
    have_arxiv = {r["id"] for r in db if re.match(r"^\d{4}\.\d{4,5}$", r["id"])}
    have_titles = {re.sub(r"[^a-z0-9]", "", r["title"].lower()) for r in db}
    core = [r["id"] for r in db if (r["relevance"] or 0) >= 4 and r["id"] in have_arxiv]
    print(f"{len(core)} core arXiv items", flush=True)
    todo = [a for a in core if not os.path.exists(os.path.join(CACHE, f"{a}.cit.json"))]
    B = 20
    for i in range(0, len(todo), B):
        chunk = todo[i:i + B]
        res = post_batch(chunk)
        if res is None:
            print(f"batch {i} failed", flush=True); continue
        for aid, p in zip(chunk, res):
            p = p or {}
            json.dump({"data": [{"citingPaper": c} for c in (p.get("citations") or [])]},
                      open(os.path.join(CACHE, f"{aid}.cit.json"), "w"))
            json.dump({"data": [{"citedPaper": c} for c in (p.get("references") or [])]},
                      open(os.path.join(CACHE, f"{aid}.ref.json"), "w"))
        print(f"{i + len(chunk)}/{len(todo)}", flush=True)
        time.sleep(DELAY)

    cand = {}
    for aid in core:
        for kind, key in (("cit", "citingPaper"), ("ref", "citedPaper")):
            path = os.path.join(CACHE, f"{aid}.{kind}.json")
            if not os.path.exists(path):
                continue
            for d in (json.load(open(path)).get("data") or []):
                p = d.get(key) or {}
                ext = p.get("externalIds") or {}
                ax = ext.get("ArXiv")
                t = p.get("title") or ""
                if not t or ax in have_arxiv or re.sub(r"[^a-z0-9]", "", t.lower()) in have_titles:
                    continue
                k = ax or re.sub(r"[^a-z0-9]", "", t.lower())
                c = cand.setdefault(k, {"arxiv": ax, "title": t, "year": p.get("year"), "venue": p.get("venue"),
                                        "cites_core": [], "cited_by_core": []})
                (c["cites_core"] if kind == "cit" else c["cited_by_core"]).append(aid)
    ranked = sorted(cand.values(), key=lambda c: -(len(set(c["cites_core"])) + len(set(c["cited_by_core"]))))
    for c in ranked:
        c["links"] = len(set(c["cites_core"])) + len(set(c["cited_by_core"]))
    json.dump(ranked, open(os.path.join(ROOT, "_work", "snowball_candidates.json"), "w"), indent=1)
    print(f"{len(ranked)} candidates; links>=3: {sum(c['links'] >= 3 for c in ranked)}; "
          f">=2: {sum(c['links'] >= 2 for c in ranked)}")


if __name__ == "__main__":
    main()
