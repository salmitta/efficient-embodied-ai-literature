# GAP_B search log

Note: WebSearch was unavailable; queries were issued directly against the arXiv export API (https://export.arxiv.org/api/query, sortBy=submittedDate descending unless marked "relevance") and the OpenAlex works API. "New relevant items" = records written to GAP_B.jsonl from that query (items already in existing_items.tsv excluded). Queries 1-36 = Part 1 (chunk interruption/certification); 37-63 = Part 2 (2026 recency sweep).

| # | source | query | new relevant items |
|---|---|---|---|
| 1 | arXiv API | abs:"action chunk" AND (interrupt OR abort OR preempt) | 0 |
| 2 | arXiv API | abs:"action chunk*" AND (safety OR safe) | 2 |
| 3 | arXiv API | abs:"action chunking" AND ("closed-loop" OR reactiv*) | 8 |
| 4 | arXiv API | abs:"control barrier function" AND (diffusion OR "action chunk*" OR "vision-language-action") | 8 |
| 5 | arXiv API | abs:"safety filter" AND ("learned policy" OR "generative policy" OR "diffusion policy" OR VLA) | 1 |
| 6 | arXiv API | abs:reachability AND ("visuomotor policy" OR "learned policy" OR "robot foundation model" OR "vision-language-action") | 4 |
| 7 | arXiv API | abs:"runtime assurance" OR abs:"simplex architecture" | 9 |
| 8 | arXiv API | abs:conformal AND ("policy failure" OR "failure prediction" OR "failure detection") AND robot* | 2 |
| 9 | arXiv API | abs:uncertainty AND replan* AND ("action chunk*" OR "vision-language-action" OR "diffusion policy") | 0 |
| 10 | arXiv API | abs:conformal AND ("vision-language-action" OR "diffusion policy" OR "action chunk*" OR "imitation learning") | 2 |
| 11 | arXiv API | ti:"conformal" AND (ti:robot* OR ti:planning OR ti:control) | 4 |
| 12 | arXiv API (relevance) | ti:"neural network control*" AND (verification OR reachability OR verified OR verifying) | 10 |
| 13 | arXiv API (relevance) | ti:Reluplex OR ti:Marabou OR ti:"NNV" OR ti:"beta-CROWN" OR ti:"VNN-COMP" | 6 |
| 14 | arXiv API (relevance) | abs:"formal verification" AND (visuomotor OR "vision-based control*" OR "robot policy" OR "end-to-end control*") | 0 |
| 15 | arXiv API | abs:"worst-case execution time" AND ("neural network" OR DNN OR GPU) | 2 |
| 16 | arXiv API | abs:"timing analysis" AND GPU AND (DNN OR "neural network" OR inference) | 0 |
| 17 | arXiv API | abs:"real-time" AND Jetson AND ("response time" OR deadline* OR schedulab*) | 2 |
| 18 | arXiv API | abs:"real-time" AND GPU AND DNN AND (deadline* OR predictab* OR "timing guarantee*") | 0 |
| 19 | arXiv API | abs:"execution time" AND (variab* OR jitter) AND "neural network" AND (embedded OR Jetson OR autonomous) | 0 |
| 20 | arXiv API | abs:timing AND ("vision-language-action" OR "robot policy" OR "robot foundation") AND (deadline* OR "real-time guarantee*" OR jitter) | 2 |
| 21 | OpenAlex | worst-case execution time deep neural network GPU | 0 |
| 22 | OpenAlex | real-time GPU scheduling DNN inference embedded autonomous timing predictability | 10 |
| 23 | arXiv API | abs:"receding horizon" AND ("action chunk*" OR "diffusion policy" OR "vision-language-action") | 0 |
| 24 | arXiv API | abs:"action chunk*" AND (guarantee* OR certif* OR provabl*) | 0 |
| 25 | arXiv API | abs:"runtime monitor*" AND ("vision-language-action" OR "robot policy" OR "generative policy" OR visuomotor) | 0 |
| 26 | arXiv API | abs:"predictive safety filter" | 3 |
| 27 | arXiv API | abs:shield* AND ("vision-language-action" OR "diffusion policy" OR "foundation model") AND robot* | 0 |
| 28 | arXiv API | abs:"open-loop" AND abs:"vision-language-action" AND (execution OR monitor*) | 3 |
| 29 | arXiv API | abs:"action chunk*" AND (uncertaint* OR "out-of-distribution") | 2 |
| 30 | arXiv API | abs:"vision-language-action" AND ("failure recovery" OR "error recovery" OR "self-correct*") | 7 |
| 31 | arXiv API | abs:"vision-language-action" AND ("temporal logic" OR "formal specification*" OR "formal guarantee*") | 0 |
| 32 | arXiv API | abs:"control barrier" AND (delay* OR latency) AND (learn* OR neural) | 1 |
| 33 | arXiv API | abs:verif* AND ("diffusion policy" OR "diffusion policies" OR "flow matching policy") | 1 |
| 34 | arXiv API | abs:"vision-language-action" AND (interrupt* OR "human intervention" OR "mid-execution") | 6 |
| 35 | arXiv API | abs:fallback AND ("learned policy" OR "vision-language-action" OR "robot policy") AND safe* | 1 |
| 36 | arXiv API id_list | seminal HJ reachability / KnowNo / DeepReach (1709.07523, 2307.01928, 2011.02082) | 3 |
| 37 | arXiv API (date desc, start=0) | abs:"vision-language-action" AND (efficient OR lightweight) | 17 |
| 38 | arXiv API (date desc, start=100) | abs:"vision-language-action" AND (efficient OR lightweight) | 13 |
| 39 | arXiv API (date desc, start=200) | abs:"vision-language-action" AND (efficient OR lightweight) | 13 |
| 40 | arXiv API (date desc, start=300) | abs:"vision-language-action" AND (efficient OR lightweight) | 19 |
| 41 | arXiv API (date desc, start=400; reached Dec 2025, stop) | abs:"vision-language-action" AND (efficient OR lightweight) | 9 |
| 42 | arXiv API (date desc, start=0) | abs:"vision-language-action" AND (accelerat* OR "inference speed" OR "inference latency" OR speedup) | 6 |
| 43 | arXiv API (date desc, start=100) | abs:"vision-language-action" AND (accelerat* OR "inference speed" OR "inference latency" OR speedup) | 8 |
| 44 | arXiv API (date desc, start=0) | abs:"vision-language-action" AND token* AND (prun* OR reduc* OR compress* OR sparsif*) | 6 |
| 45 | arXiv API (date desc, start=100; reached 2024, stop) | abs:"vision-language-action" AND token* AND (prun* OR reduc* OR compress* OR sparsif*) | 5 |
| 46 | arXiv API (date desc) | ("vision-language-action" OR "diffusion policy" OR "world action model") AND (cach* OR "KV cache") | 8 |
| 47 | arXiv API (date desc) | ("vision-language-action" OR "robot policy" OR "world action model" OR "diffusion policy") AND (quantiz* OR "low-bit" OR binar*) | 1 |
| 48 | arXiv API (date desc, start=0) | ("world action model*" OR "world-action model*") AND (efficien* OR real-time OR latency OR fast* OR distill*) | 21 |
| 49 | arXiv API (date desc, start=100) | ("world action model*" OR "world-action model*") AND (efficien* OR real-time OR latency OR fast* OR distill*) | 7 |
| 50 | arXiv API (date desc, start=0) | abs:"world model*" AND robot* AND (distill* OR "real-time" OR "inference speed" OR lightweight) | 15 |
| 51 | arXiv API (date desc, start=0) | abs:"vision-language-action" AND ("reinforcement learning" OR RL) AND ("sample efficien*" OR efficient OR "fine-tuning") | 6 |
| 52 | arXiv API (date desc, start=100) | abs:"vision-language-action" AND ("reinforcement learning" OR RL) AND ("sample efficien*" OR efficient OR "fine-tuning") | 4 |
| 53 | arXiv API (date desc) | ("vision-language-action" OR "robot foundation model*" OR "generalist robot polic*") AND ("continual learning" OR lifelong OR "test-time adaptation" OR "catastrophic forgetting") | 1 |
| 54 | arXiv API (date desc, start=0) | ("vision-language-action" OR "robot policy" OR "robot policies" OR embodied) AND (Jetson OR "on-device" OR "edge device*" OR onboard) | 5 |
| 55 | arXiv API (date desc) | ("vision-language-action" OR "robot polic*") AND (offload* OR "edge-cloud" OR "cloud-edge" OR serving OR "inference runtime") | 2 |
| 56 | arXiv API (date desc, start=0) | ("vision-language-action" OR "diffusion policy" OR "flow policy" OR "flow matching policy") AND ("one-step" OR "few-step" OR "single-step" OR consistency) | 6 |
| 57 | arXiv API (date desc, start=100) | ("vision-language-action" OR "diffusion policy" OR "flow policy" OR "flow matching policy") AND ("one-step" OR "few-step" OR "single-step" OR consistency) | 4 |
| 58 | arXiv API (date desc) | abs:"vision-language-action" AND ("early exit*" OR "early-exit*" OR "mixture-of-experts" OR "layer skip*" OR "dynamic depth" OR "adaptive computation") | 0 |
| 59 | arXiv API (date desc) | ("vision-language-action" OR "robot polic*") AND (speculative OR "parallel decoding" OR "non-autoregressive") | 0 |
| 60 | arXiv API (date desc) | (small OR compact OR tiny) AND "vision-language-action" AND (parameters OR "consumer GPU" OR CPU) | 3 |
| 61 | arXiv API (date desc) | ("vision-language-action" OR "action chunk*" OR "robot polic*") AND (asynchronous OR "inference delay" OR "latency compensation") | 2 |
| 62 | arXiv API (date desc) | ("diffusion policy" OR "diffusion policies" OR "flow matching") AND robot* AND (accelerat* OR "inference time" OR "real-time") AND (distill* OR "denoising steps" OR NFE) | 1 |
| 63 | arXiv API (date desc) | humanoid AND ("vision-language-action" OR "foundation model") AND (onboard OR "real-time" OR latency) | 2 |
