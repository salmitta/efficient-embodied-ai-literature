# Literature-mining brief — CoRL 2026 workshop "Efficient Foundation Models for Real-Time Embodied AI"
Workshop site: https://efficient-embodied-ai.github.io/
Framing: making robot foundation models (VLA policies, world-action models, emerging architectures) fast
enough, cheap enough, and safe enough to deploy ON the robot — the "generality / speed / deployability" trilemma.

## SCOPE
Include: peer-reviewed papers, arXiv preprints, OpenReview submissions, workshop papers; technical reports and
model cards from labs/companies; engineering blog posts / knowledge articles / tutorials (Physical Intelligence,
Google DeepMind, NVIDIA, Figure, Hugging Face, Dyna Robotics, Tesla, Agility, Unitree, Stanford AI Lab, BAIR,
MIT Han Lab, CMU, AWS Neuron); GitHub repos and benchmarks accompanying a paper or standard tools; talks/slides
only if they contain unique technical content.
Exclude: generic LLM efficiency work with no robotics/embodied/real-time angle UNLESS robotics papers directly
build on it (AWQ, GPTQ, speculative decoding, FlashAttention, LoRA, consistency models...) — tag these
`"foundational_technique": true`. Exclude news without technical content, SEO listicles, duplicates.
Time window: prioritize 2022–present (today is 2026-09-30). Earlier seminal works only if heavily cited
foundations (RT-1, ACT/ALOHA, Diffusion Policy, DreamerV3, control barrier functions...).

## SUBAGENT INSTRUCTIONS
1. Run at least 25–40 distinct searches for your cluster (keyword combos, synonyms, seed-work names; vary between
   arXiv, Semantic Scholar, Google-Scholar-style queries, OpenReview, GitHub, Papers with Code, blogs).
   Reformulate thin queries.
2. For every seed work: fetch it, record it, then snowball: (a) relevant references it cites, (b) relevant papers
   citing it. Semantic Scholar API is useful, e.g.
   https://api.semanticscholar.org/graph/v1/paper/arXiv:2406.09246/citations?fields=title,year,externalIds,venue,authors&limit=100
   https://api.semanticscholar.org/graph/v1/paper/arXiv:2406.09246/references?fields=title,year,externalIds,venue,authors&limit=100
   https://api.semanticscholar.org/graph/v1/paper/search?query=...&fields=title,year,externalIds,venue,authors,abstract&limit=50
   arXiv API: http://export.arxiv.org/api/query?search_query=all:%22efficient%22+AND+all:VLA&max_results=50
   (If rate-limited, back off and continue with other sources.)
3. For each item, verify relevance from its abstract/page (a search-API abstract counts as a fetched source).
   NEVER invent titles, authors, venues, URLs, or numbers. If you cannot verify an item, set "verified": false
   rather than dropping or guessing.
4. Extract efficiency numbers when reported, ALWAYS with what the number measures and on which hardware.
   "open-loop chunk rate", "closed-loop control rate", "throughput", "relative latency", "relative memory" are NOT
   comparable — record the right one in `metric_measures`.
5. Output JSONL using the schema below + a short cluster summary (technique families, key open problems,
   10 most important works).
6. Stop only when your last 10 searches surface fewer than 2 new relevant items (saturation).

## RECORD SCHEMA (one JSON object per line)
{
  "id": "arXiv ID (e.g. 2406.09246), DOI, or slugified normalized title",
  "title": "", "authors": ["..."], "year": 2025,
  "venue": "e.g. CoRL 2025 / arXiv / blog / tech report",
  "type": "paper | preprint | blog | tech-report | repo | benchmark | talk",
  "url": "", "pdf_url": "", "code_url": "",
  "clusters": ["C1", "C7"],
  "keywords": ["action chunking", "..."],
  "model_class": "VLA | world-action model | world model | diffusion/flow policy | other",
  "techniques": ["quantization", "distillation", "..."],
  "base_model": "e.g. OpenVLA-7B", "params": "",
  "hardware": "e.g. Jetson Orin NX, RTX 4090, A100",
  "reported_metric": "e.g. 12.5 Hz",
  "metric_measures": "closed-loop control | open-loop chunk rate | throughput | relative latency | relative memory | energy | other",
  "benchmarks": ["LIBERO", "real robot", "..."],
  "real_robot_eval": true, "onboard_deployment": true,
  "tldr": "1–2 sentences in your own words (do NOT copy the abstract)",
  "relevance": 1-5, "relevance_reason": "",
  "foundational_technique": false, "verified": true,
  "found_via": "search query | snowball from <id> | author sweep"
}
Use empty string / empty list / null for unknown fields. Never guess numbers.

## QUALITY RULES
Accuracy over volume; every record must trace to a fetched source. Own-words TL;DRs. Prefer original sources
(arXiv, OpenReview, official project pages). Overall target across all clusters: 500–1,500+ unique items, so
each cluster should aim for roughly 80–200 relevant items.

## CLUSTER DEFINITIONS (for tagging)
C1 efficient VLA architectures & emerging designs (small VLAs, action tokenization/chunking, parallel/speculative decoding,
   token pruning/caching, early exit/MoE, few-step diffusion/flow heads, dual-system/hierarchical).
C2 compression (quantization, pruning, distillation, low-rank) for robot foundation models.
C3 memory-efficient adaptation & fine-tuning (PEFT/LoRA, OFT recipes, RL fine-tuning efficiency, continual/few-shot adaptation).
C4 benchmarking methodology & composability (LIBERO, SimplerEnv, CALVIN, RLBench, ManiSkill, real-robot protocols, latency/energy metrics).
C5 hardware-aware design & accelerators (Jetson/Thor, TensorRT, NPUs, kernels, co-design, profiling).
C6 edge-cloud co-design & fleet systems (offloading, split computing, remote/async inference, fleet serving, TCO).
C7 safety under latency & timing variability (RTC, chunk interruption, safety filters/CBFs, runtime monitoring, failure detection, delay compensation, timing guarantees).
C8 efficient world models for planning & safety monitoring (world-action models, latent/video world models, distillation, JEPA, MBRL).
C9 people/venues/blogs sweep.
