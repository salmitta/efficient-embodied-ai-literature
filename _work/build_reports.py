#!/usr/bin/env python3
"""Build search_log.md and overview.md from the merged DB, agent logs and hand-written prose."""
import glob, json, os, re
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
W = os.path.join(ROOT, "_work")
sys_path = W
import sys; sys.path.insert(0, W)
from merge import CLUSTERS, CLUSTER_NAMES

db = [json.loads(l) for l in open(os.path.join(ROOT, "literature_db.jsonl"), encoding="utf-8")]
by_id = {r["id"]: r for r in db}
stats = json.load(open(os.path.join(W, "merge_stats.json")))


def rows_in(md):
    return sum(1 for l in md.splitlines() if re.match(r"^\|\s*\d+", l))


# ---------------- search_log.md ----------------
parts = ["# Search log\n",
         "Every query run, per subagent, with the number of new relevant items it produced as reported by that subagent. "
         "Counts are the subagents' own tallies; some count an item under every query that surfaced it, so column sums can "
         "exceed record counts. Round 2 citation snowballing was run programmatically (see section R2).\n"]
summary_rows = []
sections = []
for label, pat in [(f"{c} — {CLUSTER_NAMES[c]}", os.path.join(W, "raw", f"{c}_searchlog.md")) for c in CLUSTERS] + \
                  [("GAP_A — gap check (composability, TCO, cross-hardware evaluation, OpenVLA on 16 GB Jetson)", os.path.join(W, "raw2", "GAP_A_searchlog.md")),
                   ("GAP_B — gap check (chunk interruption/certification) + 2026 recency sweep", os.path.join(W, "raw2", "GAP_B_searchlog.md"))]:
    if not os.path.exists(pat):
        continue
    body = open(pat, encoding="utf-8").read().strip()
    body = re.sub(r"^#\s.*\n", "", body)
    body = re.sub(r"^(#+)", r"##\1", body, flags=re.M)
    n = rows_in(body)
    summary_rows.append((label.split(" — ")[0], n))
    sections.append(f"\n## {label}\n\n{n} logged query rows.\n\n{body}\n")
sb = sorted(glob.glob(os.path.join(W, "raw2", "SB_*_log.md")))
cand = json.load(open(os.path.join(W, "snowball_candidates.json")))
r2 = json.load(open(os.path.join(W, "round2_candidates.json")))
r2_sec = [f"\n## R2 — Round-2 citation snowball (programmatic)\n",
          f"- Seeds: every round-1 item with relevance ≥ 4 and an arXiv ID ({stats.get('r2_seeds', 571)} papers).",
          "- Source: Semantic Scholar Graph API `POST /paper/batch` with nested `citations` and `references` "
          "(29 batch calls of 20 papers, sequential, with back-off), because per-agent API calls had been rate-limited in round 1.",
          f"- Candidate pool: {len(cand)} papers not already in the database; kept those linked to ≥ 4 core items, from 2022+ "
          f"(or ≥ 12 links if older), whose titles matched an embodied/efficiency keyword filter → {len(r2)} candidates; "
          f"abstracts fetched in bulk for {sum(1 for c in r2 if c['abstract'])}.",
          "- Triage: six subagents read every candidate abstract and recorded in-scope items.\n"]
for f in sb:
    body = open(f, encoding="utf-8").read().strip()
    body = re.sub(r"^#\s.*\n", "", body)
    body = re.sub(r"^(#+)", r"###\1", body, flags=re.M)
    r2_sec.append(f"### {os.path.basename(f)[:-7]}\n\n{body}\n")
parts.append("\n## Totals\n\n| Subagent | Logged query rows |\n|---|---|\n" +
             "\n".join(f"| {a} | {n} |" for a, n in summary_rows) +
             f"\n| **Total** | **{sum(n for _, n in summary_rows)}** |\n| R2 snowball | 29 batch API calls + 7 abstract batch calls |\n")
open(os.path.join(ROOT, "search_log.md"), "w", encoding="utf-8").write("\n".join(parts) + "".join(sections) + "\n".join(r2_sec))

# ---------------- overview.md ----------------
prose = open(os.path.join(W, "overview_prose.md"), encoding="utf-8").read()
top30 = [l.split("|") for l in open(os.path.join(W, "top30.txt"), encoding="utf-8") if l.strip() and not l.startswith("#")]

def link(r):
    return f"[{r['title']}]({r['url']})" if r.get("url") else r["title"]

out = ["# Literature database overview — Efficient Foundation Models for Real-Time Embodied AI (CoRL 2026 workshop)\n",
       f"Built {stats.get('built', '')}. **{stats['unique']} unique items** (from {stats['raw_records']} raw records across "
       f"{len(stats['files'])} subagent outputs; {sum(stats['dupes_merged'].values())} duplicates merged by arXiv ID, DOI, URL and "
       "normalized/fuzzy title). Files: `literature_db.jsonl`, `literature_db.csv`, `by_cluster/C1–C9.md`, `efficiency_table.csv`, "
       "`search_log.md`.\n",
       "## Counts\n",
       "| Cluster | Items | rel 5 | rel 4 | with efficiency numbers |", "|---|---|---|---|---|"]
for c in CLUSTERS:
    items = [r for r in db if c in r["clusters"]]
    out.append(f"| {c} {CLUSTER_NAMES[c]} | {len(items)} | {sum(r['relevance'] == 5 for r in items)} | "
               f"{sum(r['relevance'] == 4 for r in items)} | {sum(1 for r in items if r['reported_metric'])} |")
out.append("\nItems carry multiple cluster tags, so the column sums exceed the unique total.\n")
ty = Counter(r["type"] for r in db)
yr = Counter(r["year"] for r in db)
rel = Counter(r["relevance"] for r in db)
mm = Counter((r["metric_measures"] or "unspecified") for r in db if r["reported_metric"])
out.append("- **By type:** " + ", ".join(f"{k or 'unknown'} {v}" for k, v in ty.most_common()))
out.append("- **By year:** " + ", ".join(f"{k} {yr[k]}" for k in sorted(k for k in yr if k)) + (f", unknown {yr[None]}" if yr[None] else ""))
out.append("- **By relevance:** " + ", ".join(f"{k}: {rel[k]}" for k in (5, 4, 3, 2, 1)))
out.append(f"- **Foundational techniques:** {sum(1 for r in db if r['foundational_technique'])}; "
           f"**real-robot evaluation:** {sum(1 for r in db if r['real_robot_eval'])}; "
           f"**onboard deployment:** {sum(1 for r in db if r['onboard_deployment'])}")
out.append(f"- **Efficiency numbers:** {sum(1 for r in db if r['reported_metric'])} items (`efficiency_table.csv`). What they measure: " +
           ", ".join(f"{k} {v}" for k, v in mm.most_common(12)) + ".\n")
out.append(prose.split("<!--TOP30-->")[0])
out.append("## Top 30 must-read works\n\n| # | Work | Year | Clusters | Why |\n|---|---|---|---|---|")
for i, (rid, why) in enumerate(((a.strip(), b.strip()) for a, b in top30), 1):
    r = by_id.get(rid)
    if r is None:
        out.append(f"| {i} | {rid} (MISSING FROM DB) | | | {why} |"); continue
    out.append(f"| {i} | {link(r)} | {r['year'] or ''} | {', '.join(r['clusters'])} | {why} |")
out.append("\n" + prose.split("<!--TOP30-->")[1])
out.append("\n## Items needing manual review\n")
unv = [r for r in db if not r["verified"]]
out.append(f"### Unverified items ({len(unv)} remaining)\n\nOf 15 originally unverified items, 5 were garbled duplicates of verified "
           "records and have been merged. 9 were confirmed against a fetched abstract or page on 2026-09-30: the `relevance_reason` of "
           "each says which source. The item below could not be confirmed: no abstract is available from Semantic Scholar, OpenAlex, "
           "OpenReview or arXiv, and the session's web-search budget was exhausted.\n")
for r in unv:
    out.append(f"- `{r['id']}` — {link(r)} ({r['type']}, {r['year'] or 'n.d.'}) — {r['relevance_reason'] or r['tldr']}"[:400])
flag = [r for r in db if re.search(r"not re-verified|from memory|unconfirmed|not confirmed", (r["venue"] + " " + r["relevance_reason"]).lower())]
RES = {
    "2301.04104": "confirmed — Crossref DOI 10.1038/s41586-025-08744-2 (Nature, 2025)",
    "2310.16828": "confirmed — DBLP conf/iclr", "2402.15391": "confirmed — DBLP conf/icml",
    "2310.06114": "confirmed ICLR 2024 — DBLP conf/iclr; unconfirmed 'Outstanding Paper' note removed",
    "2412.14803": "confirmed — DBLP conf/icml", "2503.00653": "confirmed — DBLP conf/iclr",
    "2302.00111": "confirmed — DBLP conf/nips", "2405.07503": "confirmed RSS 2024 — DBLP conf/rss",
    "2505.14357": "confirmed — OpenReview 'ICLR 2026 Poster'", "2505.00779": "confirmed — OpenReview 'CoRL 2025 Poster'",
    "2502.00935": "confirmed — RSS 2025 proceedings listing", "2502.01828": "confirmed — RSS 2025 proceedings listing",
    "2503.00200": "confirmed — RSS 2025 proceedings listing", "2410.24164": "confirmed RSS 2025 — RSS 2025 proceedings listing",
    "2405.15223": "confirmed — Semantic Scholar venue metadata", "2506.08009": "confirmed — Semantic Scholar venue metadata",
    "2411.04983": "confirmed — Semantic Scholar venue metadata", "2203.04955": "confirmed — Semantic Scholar venue metadata",
    "2410.22689": "confirmed — Semantic Scholar venue metadata", "2405.12399": "confirmed — Semantic Scholar venue metadata",
    "2310.17552": "**corrected** CoRL 2023 → ICRA 2024 (DBLP conf/icra, Semantic Scholar)",
    "2502.04296": "**reverted** to arXiv — 'CVPR 2025' not found in the CVF CVPR 2025 listing or OpenReview",
}
out.append("\n### Venue spot-checks (resolved 2026-09-30)\n\nThe C8 subagent had filled conference venues for these papers from memory, "
           "and C2 had flagged Consistency Policy and π0 as unconfirmed. Each was re-checked against DBLP keys, Crossref, OpenReview, "
           "the RSS proceedings, or Semantic Scholar venue metadata. DBLP's own search page blocks scripted access, so DBLP keys come "
           "through Semantic Scholar.\n\n| ID | Title | Venue now | Resolution |\n|---|---|---|---|")
for rid, res in RES.items():
    r = by_id.get(rid, {})
    out.append(f"| `{rid}` | {r.get('title', '')} | {r.get('venue', '')} | {res} |")
open(os.path.join(ROOT, "overview.md"), "w", encoding="utf-8").write("\n".join(out) + "\n")
print("wrote search_log.md and overview.md")
