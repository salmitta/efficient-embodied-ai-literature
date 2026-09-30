#!/usr/bin/env python3
"""Build the searchable static site into docs/ (GitHub Pages-ready) from literature_db.jsonl."""
import json, os, shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
W = os.path.join(ROOT, "_work")
OUT = os.path.join(ROOT, "docs")

db = [json.loads(l) for l in open(os.path.join(ROOT, "literature_db.jsonl"), encoding="utf-8")]
stats = json.load(open(os.path.join(W, "merge_stats.json")))
# Compact positional rows; order must match the reader in site_template.html.
rows = [[r["id"], r["title"], r["authors"], r["year"], r["venue"], r["type"], r["url"], r["pdf_url"], r["code_url"],
         r["clusters"], r["keywords"], r["techniques"], r["base_model"], r["params"], r["hardware"], r["reported_metric"],
         r["metric_measures"], r["benchmarks"], bool(r["real_robot_eval"]), bool(r["onboard_deployment"]), r["tldr"],
         r["relevance"], r["relevance_reason"], bool(r["foundational_technique"]), bool(r["verified"]), r["found_via"],
         r["model_class"]] for r in db]
data = json.dumps(rows, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")


def page(downloads):
    t = open(os.path.join(W, "site_template.html"), encoding="utf-8").read()
    return (t.replace("__DATA__", data).replace("__BUILT__", stats.get("built", ""))
             .replace("__N__", f"{len(db):,}").replace("__DOWNLOADS__", downloads))


def main():
    os.makedirs(OUT, exist_ok=True)
    files = ["literature_db.jsonl", "literature_db.csv", "efficiency_table.csv", "overview.md", "README.md"]
    for f in files:
        shutil.copy(os.path.join(ROOT, f), os.path.join(OUT, f))
    dl = (" Download: <a href=\"literature_db.csv\">CSV</a> · <a href=\"literature_db.jsonl\">JSONL</a> · "
          "<a href=\"efficiency_table.csv\">efficiency table</a> · <a href=\"overview.md\">overview</a> · <a href=\"README.md\">README</a>.")
    head = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
            '<meta name="description" content="Searchable literature database for the CoRL 2026 workshop on Efficient Foundation Models for Real-Time Embodied AI.">\n')
    body = page(dl)
    title_end = body.index("</style>") + len("</style>")
    html = head + body[:title_end] + "\n</head>\n<body>\n" + body[title_end:] + "\n</body>\n</html>\n"
    open(os.path.join(OUT, "index.html"), "w", encoding="utf-8").write(html)
    meta = os.path.join(OUT, "embeddings.json")
    em = json.load(open(meta)) if os.path.exists(meta) else {}
    if em.get("n") != len(db) or em.get("first") != db[0]["id"] or em.get("last") != db[-1]["id"]:
        print("WARNING: docs/embeddings.bin is missing or out of date; semantic search will switch itself off. "
              "Run: cd _work && npm install && node embed.mjs")
    open(os.path.join(OUT, ".nojekyll"), "w").close()  # serve files as-is on GitHub Pages
    print(f"docs/index.html: {os.path.getsize(os.path.join(OUT, 'index.html')) / 1e6:.2f} MB, {len(db)} records")


if __name__ == "__main__":
    main()
