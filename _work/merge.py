#!/usr/bin/env python3
"""Merge subagent JSONL outputs, deduplicate, and emit the database deliverables."""
import csv, glob, json, os, re, sys
from collections import defaultdict
from difflib import SequenceMatcher

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORK = os.path.join(ROOT, "_work")
CLUSTERS = ["C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9"]
CLUSTER_NAMES = {
    "C1": "Efficient architectures for VLA policies and emerging designs",
    "C2": "Compression for robot foundation models",
    "C3": "Memory-efficient adaptation and fine-tuning",
    "C4": "Benchmarking methodology and composability",
    "C5": "Hardware-aware design and accelerators",
    "C6": "Edge-cloud co-design and fleet systems",
    "C7": "Safety under latency and timing variability",
    "C8": "Efficient world models for planning and safety monitoring",
    "C9": "People, venues and blogs",
}
LIST_FIELDS = ["authors", "clusters", "keywords", "techniques", "benchmarks"]
STR_FIELDS = ["title", "venue", "type", "url", "pdf_url", "code_url", "model_class", "base_model",
              "params", "hardware", "reported_metric", "metric_measures", "tldr", "relevance_reason"]
ARXIV_RE = re.compile(r"(?<!\d)(\d{4}\.\d{4,5})(?:v\d+)?(?!\d)")
DOI_RE = re.compile(r"(10\.\d{4,9}/[^\s\"'<>]+)", re.I)


# Garbled Semantic Scholar duplicates of records already in the DB -> canonical arXiv ID (checked by hand).
ALIASES = {
    "open-x-embodiment-robotic-learning-datasets-and-rt-x-models": "2310.08864",
    "6-a-vla-that-learns-from-experience-physical-intelligence": "2511.14759",
    "0-6-a-vla-that-learns-from-experience-physical": "2511.14759",
    "optq-accurate-quantization-for-generative-pre-trained-transformers": "2210.17323",  # OPTQ = GPTQ (ICLR 2023 name)
    "open-x-embodiment-robotic-learning-datasets-and-rt-x-models-open-x-embodiment-co": "2310.08864",
}
# Orchestrator verification against the arXiv API (2026-09-30).
OVERRIDES = {
    "2306.11706": {"verified": True, "title": "RoboCat: A Self-Improving Generalist Agent for Robotic Manipulation"},
    "2206.09557": {"verified": True, "title": "LUT-GEMM: Quantized Matrix Multiplication based on LUTs for Efficient Inference "
                                               "in Large-Scale Generative Language Models (earlier title: nuQmm)"},
    "2310.08864": {"title": "Open X-Embodiment: Robotic Learning Datasets and RT-X Models"},
}

V = "verified 2026-09-30 by orchestrator: "
OVERRIDES.update({
    # --- previously unverified items, now checked against a fetched source ---
    "10.1109/icassp55912.2026.11464271": {"verified": True, "venue": "ICASSP 2026",
        "tldr": "Training-free VLA acceleration that separates foreground from background visual input and reuses cached computation for the redundant background, cutting real-time latency without retraining.",
        "relevance_reason": V + "abstract via OpenAlex (DOI). Directly on training-free VLA inference acceleration."},
    "seeed-gr00t-n17-tensorrt-agx-orin": {"verified": True,
        "tldr": "Step-by-step guide that builds TensorRT engines for all seven GR00T N1.7 components on Jetson AGX Orin (JetPack 7.2) and validates offline action generation from a LeRobot dataset.",
        "relevance_reason": V + "page fetched; reports 0.2755 s warm inference per 16-action chunk (batch 1) on AGX Orin, offline (no robot in the loop)."},
    "table30-v2-cvprw2026": {"verified": True,
        "authors": ["Yunchao Ma", "Ze Chen", "Erjin Zhou", "Ziming Liu", "Haowei Zhang", "Kai Liu", "Haoqiang Fan"],
        "venue": "CVPR 2026 Workshops (pp. 4461-4467)",
        "relevance_reason": V + "CVF open-access page and abstract fetched. Real-robot benchmark infrastructure (RoboChallenge)."},
    "github-awesome-vla-deployment": {"verified": True,
        "relevance_reason": V + "README fetched: 171 curated entries on latency, chunking, quantisation, edge hardware and safety layers for real-robot VLA deployment."},
    "cross-embodiment-robot-foundation-world-models-latent-actions-icml2026": {"verified": True, "venue": "ICML 2026",
        "tldr": "LAC-WM: a robot world model conditioned on a learned latent action space shared across embodiments, which adapts better to unseen robots than explicit action conditioning.",
        "relevance_reason": V + "OpenReview record (ICML 2026 regular) and abstract fetched. World-model work from speaker Jiajun Wu's group."},
    "10.1007/978-3-030-36150-1_24": {"verified": True,
        "tldr": "Measures how offloading a mobile robot's navigation and vision to edge services (software-as-a-service) changes its onboard energy use and compute requirements.",
        "relevance_reason": V + "Springer abstract fetched. Early onboard-vs-edge energy evidence for C6 TCO questions."},
    "s2-control-delay-rl-memoryless-iros-2010": {"verified": True, "venue": "IROS 2010", "url": "https://doi.org/10.1109/IROS.2010.5650345",
        "tldr": "Proposes temporal-difference learning algorithms that account for control delay (the gap between sensing and acting) without augmenting the state, tested in simulation and on a real robot system.",
        "relevance_reason": V + "abstract via OpenAlex (DOI 10.1109/IROS.2010.5650345). Seminal delay-aware RL cited by RTC."},
    "s2-time-optimal-execution-action-chunk-policies": {"verified": True, "venue": "ICLR 2026 (poster)",
        "url": "https://openreview.net/forum?id=INsLvSCJ4z", "relevance": 3,
        "tldr": "Accelerates any action-chunk imitation policy so the robot executes faster than the demonstrations, addressing speed limits from slow teleoperated data and inference latency.",
        "relevance_reason": V + "OpenReview abstract fetched (ICLR 2026 poster). Execution-speed/latency of chunked policies."},
    "2306.11706": {"verified": True, "title": "RoboCat: A Self-Improving Generalist Agent for Robotic Manipulation",
        "tldr": "Multi-embodiment, goal-conditioned decision-transformer agent that improves itself by generating new training data; a context model for cross-embodiment adaptation.",
        "relevance_reason": V + "arXiv abstract fetched. Context: major robot foundation model."},
    "2206.09557": {"verified": True,
        "tldr": "Lookup-table-based GEMM kernel that speeds up weight-only sub-4-bit quantized LLM inference by avoiding dequantization overhead.",
        "relevance_reason": V + "arXiv abstract fetched (paper later retitled LUT-GEMM). Foundational quantized-kernel technique."},
    # --- venue spot-checks ---
    "2310.06114": {"venue": "ICLR 2024"},        # DBLP conf/iclr; award claim not confirmed, dropped
    "2310.17552": {"venue": "ICRA 2024"},        # was 'CoRL 2023'; DBLP conf/icra/LiuDMZ24
    "2502.04296": {"venue": "arXiv"},            # 'CVPR 2025' not found in CVF CVPR 2025 listing or OpenReview
    "2405.07503": {"venue": "RSS 2024"},         # DBLP conf/rss/PrasadLWZB24
    "2410.24164": {"venue": "RSS 2025"},         # listed in RSS 2025 proceedings (roboticsproceedings.org/rss21)
})

METRIC_CATS = ["closed-loop control", "open-loop chunk rate", "throughput", "relative latency", "relative memory", "energy", "other"]


def norm_metric(v):
    v = (v or "").strip()
    for c in METRIC_CATS:
        if v.lower().startswith(c):
            return c
    return v


def load_records():
    recs, bad = [], 0
    files = sorted(glob.glob(os.path.join(WORK, "raw", "*.jsonl")) + glob.glob(os.path.join(WORK, "raw2", "*.jsonl")))
    for f in files:
        src = os.path.basename(os.path.dirname(f)) + "/" + os.path.basename(f)
        with open(f, encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if not line:
                    continue
                try:
                    r = json.loads(line)
                except json.JSONDecodeError:
                    bad += 1
                    continue
                if isinstance(r, dict) and r.get("title"):
                    r["_src"] = src
                    recs.append(r)
    return recs, bad, files


def as_list(v):
    if v is None or v == "":
        return []
    if isinstance(v, list):
        return [str(x).strip() for x in v if str(x).strip()]
    return [s.strip() for s in re.split(r"[;,]", str(v)) if s.strip()]


def as_bool(v):
    if isinstance(v, bool):
        return v
    if isinstance(v, str):
        return v.strip().lower() in ("true", "yes", "1")
    return bool(v) if v is not None else None


def norm_title(t):
    t = t.lower()
    t = re.sub(r"[^a-z0-9 ]+", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def arxiv_id(r):
    for k in ("id", "url", "pdf_url"):
        v = str(r.get(k) or "")
        if "arxiv" in v.lower() or (k == "id" and re.fullmatch(r"\s*\d{4}\.\d{4,5}(v\d+)?\s*", v)):
            m = ARXIV_RE.search(v)
            if m:
                return m.group(1)
    return None


def doi(r):
    for k in ("id", "url"):
        m = DOI_RE.search(str(r.get(k) or ""))
        if m and "arxiv" not in m.group(1).lower():
            return m.group(1).rstrip(".").lower()
    return None


def clean(r):
    out = {}
    for k in STR_FIELDS:
        v = r.get(k)
        out[k] = "" if v is None else (", ".join(map(str, v)) if isinstance(v, list) else str(v).strip())
    for k in LIST_FIELDS:
        out[k] = as_list(r.get(k))
    out["clusters"] = sorted({c.upper() for c in out["clusters"] if c.upper() in CLUSTERS})
    try:
        out["year"] = int(str(r.get("year"))[:4])
    except (TypeError, ValueError):
        out["year"] = None
    try:
        out["relevance"] = max(1, min(5, int(float(r.get("relevance")))))
    except (TypeError, ValueError):
        out["relevance"] = None
    for k in ("real_robot_eval", "onboard_deployment", "foundational_technique", "verified"):
        out[k] = as_bool(r.get(k))
    out["found_via"] = as_list(r.get("found_via")) if isinstance(r.get("found_via"), list) else \
        ([str(r.get("found_via")).strip()] if r.get("found_via") else [])
    out["_arxiv"] = arxiv_id(r)
    out["_doi"] = doi(r)
    out["_ntitle"] = norm_title(out["title"])
    u = re.sub(r"^https?://(www\.)?", "", out["url"].lower()).split("#")[0].split("?")[0].rstrip("/")
    out["_url"] = u if "/" in u else None  # bare domains (e.g. a workshop homepage) are not unique keys
    out["_srcs"] = [r["_src"]]
    out["metric_measures"] = norm_metric(out["metric_measures"])
    if str(r.get("id") or "").strip() in ALIASES:
        out["_arxiv"] = ALIASES[str(r.get("id")).strip()]
        out["title"] = ""  # let the canonical record's title win
        out["verified"] = False
    out["id"] = out["_arxiv"] or out["_doi"] or (str(r.get("id") or "").strip() or re.sub(" ", "-", out["_ntitle"])[:80])
    return out


def merge_into(a, b):
    for k in STR_FIELDS:
        if len(b[k]) > len(a[k]):
            if k == "reported_metric" and a[k] and b[k] and a[k] not in b[k]:
                a[k] = a[k] + " | " + b[k]
            else:
                a[k] = b[k]
    for k in LIST_FIELDS + ["found_via", "_srcs"]:
        seen = {x.lower() for x in a[k]}
        for x in b[k]:
            if x.lower() not in seen:
                a[k].append(x); seen.add(x.lower())
    a["clusters"] = sorted(set(a["clusters"]))
    if len(b["authors"]) > len(a["authors"]):
        a["authors"] = b["authors"]
    a["year"] = a["year"] or b["year"]
    a["relevance"] = max([x for x in (a["relevance"], b["relevance"]) if x is not None], default=None)
    for k in ("real_robot_eval", "onboard_deployment", "foundational_technique"):
        a[k] = bool(a[k]) or bool(b[k]) if (a[k] is not None or b[k] is not None) else None
    a["verified"] = bool(a["verified"]) or bool(b["verified"])
    a["_arxiv"] = a["_arxiv"] or b["_arxiv"]
    a["_doi"] = a["_doi"] or b["_doi"]
    a["_url"] = a["_url"] or b["_url"]
    if a["_arxiv"]:
        a["id"] = a["_arxiv"]


def dedupe(recs):
    merged, by_arxiv, by_doi, by_title, by_url = [], {}, {}, {}, {}
    buckets = defaultdict(list)  # first title word -> indices, for fuzzy matching
    stats = defaultdict(int)
    for r in recs:
        idx = None
        if r["_arxiv"] and r["_arxiv"] in by_arxiv:
            idx = by_arxiv[r["_arxiv"]]; stats["arxiv"] += 1
        elif r["_doi"] and r["_doi"] in by_doi:
            idx = by_doi[r["_doi"]]; stats["doi"] += 1
        elif r["_url"] and r["_url"] in by_url and not (r["_arxiv"] and merged[by_url[r["_url"]]]["_arxiv"]
                                                     and r["_arxiv"] != merged[by_url[r["_url"]]]["_arxiv"]):
            idx = by_url[r["_url"]]; stats["url"] += 1
        elif r["_ntitle"] in by_title:
            idx = by_title[r["_ntitle"]]; stats["title_exact"] += 1
        else:
            words = r["_ntitle"].split()
            keys = set(words[:2])
            for key in keys:
                for j in buckets[key]:
                    m = merged[j]
                    # never fuzzy-merge two different arXiv IDs
                    if r["_arxiv"] and m["_arxiv"] and r["_arxiv"] != m["_arxiv"]:
                        continue
                    sm = SequenceMatcher(None, r["_ntitle"], m["_ntitle"])
                    if sm.real_quick_ratio() > 0.9 and sm.quick_ratio() > 0.9 and sm.ratio() > 0.9:
                        idx = j; stats["title_fuzzy"] += 1; break
                if idx is not None:
                    break
        if idx is None:
            merged.append(r); idx = len(merged) - 1
            for key in set(r["_ntitle"].split()[:2]):
                buckets[key].append(idx)
        else:
            merge_into(merged[idx], r)
        m = merged[idx]
        if m["_arxiv"]: by_arxiv[m["_arxiv"]] = idx
        if m["_doi"]: by_doi[m["_doi"]] = idx
        if r["_url"]: by_url[r["_url"]] = idx
        by_title[r["_ntitle"]] = idx; by_title[m["_ntitle"]] = idx
    return merged, stats


def public(r):
    keys = ["id", "title", "authors", "year", "venue", "type", "url", "pdf_url", "code_url", "clusters",
            "keywords", "model_class", "techniques", "base_model", "params", "hardware", "reported_metric",
            "metric_measures", "benchmarks", "real_robot_eval", "onboard_deployment", "tldr", "relevance",
            "relevance_reason", "foundational_technique", "verified", "found_via"]
    out = {k: r[k] for k in keys}
    out["found_via"] = "; ".join(r["found_via"])
    return out


def sort_key(r):
    return (-(r["relevance"] or 0), -(r["year"] or 0), r["title"].lower())


def md_entry(r):
    auth = ", ".join(r["authors"][:4]) + (" et al." if len(r["authors"]) > 4 else "")
    head = f"**{r['title']}**"
    link = r["url"] or r["pdf_url"]
    if link:
        head = f"**[{r['title']}]({link})**"
    bits = [x for x in [auth, str(r["year"] or ""), r["venue"], r["type"]] if x]
    lines = [f"- {head} — " + " · ".join(bits)]
    meta = []
    if r["relevance"]: meta.append(f"relevance {r['relevance']}/5")
    if r["techniques"]: meta.append("techniques: " + ", ".join(r["techniques"]))
    if r["clusters"]: meta.append("clusters: " + ", ".join(r["clusters"]))
    if r["foundational_technique"]: meta.append("foundational-technique")
    if not r["verified"]: meta.append("⚠ UNVERIFIED")
    lines.append("  - " + "; ".join(meta))
    if r["tldr"]: lines.append(f"  - TL;DR: {r['tldr']}")
    if r["reported_metric"]:
        hw = f" on {r['hardware']}" if r["hardware"] else ""
        mm = f" ({r['metric_measures']})" if r["metric_measures"] else ""
        lines.append(f"  - Efficiency: {r['reported_metric']}{mm}{hw}")
    if r["code_url"]: lines.append(f"  - Code: {r['code_url']}")
    return "\n".join(lines)


def main():
    raw, bad, files = load_records()
    recs = [clean(r) for r in raw]
    merged, stats = dedupe(recs)
    for r in merged:
        for k, v in OVERRIDES.get(r["id"], {}).items():
            r[k] = v
            if k == "title":
                r["_ntitle"] = norm_title(v)
    merged.sort(key=sort_key)
    out = [public(r) for r in merged]

    with open(os.path.join(ROOT, "literature_db.jsonl"), "w", encoding="utf-8") as f:
        for r in out:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    with open(os.path.join(ROOT, "literature_db.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(out[0].keys()))
        w.writeheader()
        for r in out:
            w.writerow({k: ("; ".join(v) if isinstance(v, list) else v) for k, v in r.items()})

    eff_cols = ["id", "title", "year", "model", "params", "hardware", "reported_metric", "metric_measures",
                "benchmarks", "techniques", "onboard_deployment", "url"]
    with open(os.path.join(ROOT, "efficiency_table.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=eff_cols)
        w.writeheader()
        n_eff = 0
        for r in merged:
            if r["reported_metric"]:
                n_eff += 1
                w.writerow({"id": r["id"], "title": r["title"], "year": r["year"],
                            "model": r["base_model"], "params": r["params"], "hardware": r["hardware"],
                            "reported_metric": r["reported_metric"], "metric_measures": r["metric_measures"],
                            "benchmarks": "; ".join(r["benchmarks"]), "techniques": "; ".join(r["techniques"]),
                            "onboard_deployment": r["onboard_deployment"], "url": r["url"]})

    os.makedirs(os.path.join(ROOT, "by_cluster"), exist_ok=True)
    counts = {}
    for c in CLUSTERS:
        items = [r for r in merged if c in r["clusters"]]
        counts[c] = len(items)
        summ = os.path.join(WORK, "raw", f"{c}_summary.md")
        with open(os.path.join(ROOT, "by_cluster", f"{c}.md"), "w", encoding="utf-8") as f:
            f.write(f"# {c}. {CLUSTER_NAMES[c]}\n\n{len(items)} items, sorted by relevance then year.\n\n")
            if os.path.exists(summ):
                f.write("## Cluster summary\n\n")
                body = open(summ, encoding="utf-8").read().strip()
                body = re.sub(r"^#\s.*\n", "", body)  # drop the summary's own H1
                body = re.sub(r"^(#+)", r"#\1", body, flags=re.M)
                f.write(body + "\n\n")
            f.write("## Annotated bibliography\n\n")
            cur = None
            for r in items:
                if r["relevance"] != cur:
                    cur = r["relevance"]
                    f.write(f"\n### Relevance {cur if cur else 'unrated'}\n\n")
                f.write(md_entry(r) + "\n")

    stats_out = {"raw_records": len(raw), "bad_lines": bad, "files": [os.path.relpath(x, ROOT) for x in files],
                 "unique": len(merged), "dupes_merged": dict(stats), "per_cluster": counts,
                 "unverified": sum(1 for r in merged if not r["verified"]),
                 "with_metrics": n_eff,
                 "relevance_hist": {str(k): sum(1 for r in merged if r["relevance"] == k) for k in range(1, 6)},
                 "types": {t: sum(1 for r in merged if r["type"] == t) for t in sorted({r["type"] for r in merged})},
                 "foundational": sum(1 for r in merged if r["foundational_technique"])}
    with open(os.path.join(WORK, "merge_stats.json"), "w") as f:
        json.dump(stats_out, f, indent=2)
    print(json.dumps(stats_out, indent=2))


if __name__ == "__main__":
    main()
