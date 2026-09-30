# Efficient Embodied AI — Literature Database

This database covers the research scope of the CoRL 2026 workshop
[*Efficient Foundation Models for Real-Time Embodied AI*](https://efficient-embodied-ai.github.io/). That scope is making robot foundation models
(VLA policies, world-action models, emerging architectures) fast, cheap and safe enough to run on the robot.

- **2,232 unique items** (papers, preprints, tech reports, blogs, repos, benchmarks), mostly from 2024–2026.
- The items fall into nine topic clusters (C1–C9, defined below).
- The snapshot was taken on 2026-09-30.

## Files

| File | Contents |
|---|---|
| `literature_db.jsonl` | The full database, one JSON record per line. |
| `literature_db.csv` | The same data, flattened. List fields are joined with `; `. |
| `by_cluster/C1.md` … `C9.md` | Annotated bibliography per cluster, sorted by relevance, then year. Each opens with a cluster summary. |
| `efficiency_table.csv` | The 617 items that report efficiency numbers (model, params, hardware, metric, what it measures, benchmarks). |
| `overview.md` | Counts, technique taxonomy, top 30 must-reads, answers to the workshop's key questions, research gaps, items needing review. |
| `search_log.md` | Every query run and how the citation snowball was done. |
| `docs/` | The searchable website (GitHub Pages). `docs/index.html` is self-contained and also works opened straight from disk. |

## Clusters

| | Cluster | Items |
|---|---|---|
| C1 | Efficient architectures for VLA policies and emerging designs | 733 |
| C2 | Compression for robot foundation models | 365 |
| C3 | Memory-efficient adaptation and fine-tuning | 453 |
| C4 | Benchmarking methodology and composability | 363 |
| C5 | Hardware-aware design and accelerators | 245 |
| C6 | Edge-cloud co-design and fleet systems | 218 |
| C7 | Safety under latency and timing variability | 539 |
| C8 | Efficient world models for planning and safety monitoring | 522 |
| C9 | People, venues and blogs (speaker/organizer and lab-blog sweep) | 260 |

An item can belong to several clusters, so the counts add up to more than the total.

## What `relevance` means

`relevance` (1–5) rates how central an item is to the workshop's question: making robot foundation models fast, cheap and safe
enough to deploy on the robot. It does not rate paper quality.

| Score | Meaning | Count |
|---|---|---|
| **5** | **Core.** Directly about the efficiency, real-time execution or deployability of robot or embodied foundation models, with substantive evidence. Also used for works the whole area builds on (e.g. π0, OpenVLA-OFT, RTC). | 248 |
| **4** | **Directly relevant.** An efficiency, latency, compression, adaptation, safety-under-latency or evaluation contribution for robot foundation models, narrower in scope or less established. | 529 |
| **3** | **Relevant.** Covers one of the following: <ul><li>an adjacent technique, or work where efficiency is a secondary angle</li><li>a foundational ML efficiency technique that robotics work builds on (AWQ, GPTQ, LoRA, FlashAttention, speculative decoding…)</li><li>safety, world-model or benchmark work relevant to the workshop questions</li></ul> | 953 |
| **2** | **Context.** A major robot foundation model, dataset or benchmark that the efficiency literature builds on or evaluates against (e.g. Open X-Embodiment, DROID), or background methods. | 497 |
| **1** | **Marginal.** Kept only for completeness. | 5 |

Caveats:
- Scores are the judgment of the subagent that recorded the item, from its abstract. They were not re-calibrated across agents. When several agents recorded the same item, the highest score was kept. Treat differences of one point as noise.
- For a core reading set, filter `relevance >= 4` (777 items). `relevance >= 3` gives 1,730 items.
- `foundational_technique: true` marks generic (non-robotics) ML techniques that are included because robotics work builds on them. It is independent of relevance.

## Efficiency numbers are not comparable across `metric_measures`

`reported_metric` holds the number as the paper reports it. `metric_measures` says what kind of quantity it is. **Numbers from different
`metric_measures` categories must not be compared or ranked against each other.** Even within one category, compare with care.

| `metric_measures` | What it is | Items | Watch out for |
|---|---|---|---|
| `closed-loop control` | Rate or latency of the full perception → policy → actuation loop while the robot (or simulator) runs | 37 | The closest to "real-time on the robot", but setups still differ (cameras, action horizon, network). |
| `open-loop chunk rate` | How fast the model produces action chunks or steps in isolation | 18 | A 50-action chunk at 5 Hz is not a 250 Hz controller. Execution, sensing and replanning are excluded. |
| `throughput` | Actions, tokens or requests per second, often batched or on a server | 69 | Batched throughput (e.g. at concurrency 8) says little about batch-1 latency on one robot. |
| `relative latency` | Speedup or latency reduction vs. the paper's own baseline (e.g. "2.3× faster") | 227 | The baselines, hardware and precision differ between papers. A 3× speedup in one paper and a 3× speedup in another are not the same thing. |
| `relative memory` | Memory or model-size reduction vs. a baseline | 34 | Weight memory, peak VRAM and unified-memory footprint are different quantities. |
| `energy` | Joules or watts per inference, action or episode | 17 | Methods differ: board power vs. GPU rail, idle-subtracted or not, internal telemetry vs. external meter. |
| `other` | FLOPs, parameter counts, task-success changes, mixed metrics | 215 | Heterogeneous. Read `reported_metric` itself. |

Further cautions:
- **Hardware is often missing.** Only 174 of the 617 items with numbers state the hardware. A latency with no hardware should not be compared with anything.
- **Numbers come from abstracts, pages and tables as the authors state them.** Nothing was re-measured, and ambiguous numbers were left out rather than guessed.
- **Faster per step is not always faster per task.** Several works show that per-step speedups do not always shorten tasks or preserve success (e.g. the Speedup Paradox, 2606.28529, and From Inference Efficiency to Embodied Efficiency, 2603.19131).

## Verification status and pending items

Every record was verified against a fetched source (arXiv, OpenReview, Semantic Scholar/OpenAlex abstract, proceedings or project page).
A random sample of 60 arXiv records matched arXiv titles exactly.

As of 2026-09-30:
- **1 item still unverified:** `s2-simulation-evaluating-robot-policies-asynchronous-real-time` ("Simulation for Evaluating Robot
  Policies Should Be Asynchronous and Real-Time"). Its title and authors come from Semantic Scholar, but no abstract could be retrieved.
  It is marked `verified: false`.
- **Venue spot-checks: done.** 22 venues that were originally filled in without a fetched source were re-checked (details in `overview.md`):
  - 20 confirmed;
  - 1 corrected (2310.17552: CoRL 2023 → ICRA 2024);
  - 1 reverted to "arXiv" (2502.04296: a CVPR 2025 claim that could not be confirmed).
- **Other venues:** most 2026 preprints are listed as "arXiv". Their acceptance status was not checked.

## Coverage notes

- **How the database was built:**
  - Nine topic subagents, 801 logged queries.
  - A citation snowball (Semantic Scholar citations and references of all 571 relevance ≥ 4 arXiv items; 2,574 candidate abstracts triaged).
  - Two targeted gap and recency sweeps.
  - Deduplication by arXiv ID → DOI → URL → normalized/fuzzy title.
- **Saturation:**
  - Search saturated for quantization, MoE/early exit, speculative decoding and continual learning.
  - It did not fully saturate for efficient world-action models and adaptive-compute VLAs, where new preprints appear weekly.
- **Not covered:** public workshop submissions. None were visible on OpenReview at snapshot time (the deadline is 2026-10-12).

## Rebuilding

```bash
python3 _work/merge.py          # raw subagent outputs in _work/raw, _work/raw2 -> literature_db.*, by_cluster/, efficiency_table.csv
python3 _work/build_reports.py  # -> overview.md, search_log.md
python3 _work/build_site.py     # -> docs/ (website)
```

## Record schema

`id` (arXiv ID, DOI or slug), `title`, `authors`, `year`, `venue`, `type`, `url`, `pdf_url`, `code_url`, `clusters`, `keywords`,
`model_class`, `techniques`, `base_model`, `params`, `hardware`, `reported_metric`, `metric_measures`, `benchmarks`,
`real_robot_eval`, `onboard_deployment`, `tldr` (written by the curators, not copied from abstracts), `relevance`, `relevance_reason`,
`foundational_technique`, `verified`, `found_via`.
