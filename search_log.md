# Search log

Every query run, per subagent, with the number of new relevant items it produced as reported by that subagent. Counts are the subagents' own tallies; some count an item under every query that surfaced it, so column sums can exceed record counts. Round 2 citation snowballing was run programmatically (see section R2).


## Totals

| Subagent | Logged query rows |
|---|---|
| C1 | 88 |
| C2 | 89 |
| C3 | 51 |
| C4 | 87 |
| C5 | 74 |
| C6 | 97 |
| C7 | 115 |
| C8 | 120 |
| C9 | 80 |
| GAP_A | 126 |
| GAP_B | 63 |
| **Total** | **990** |
| R2 snowball | 29 batch API calls + 7 abstract batch calls |

## C1 — Efficient architectures for VLA policies and emerging designs

88 logged query rows.


| # | source | query | new relevant items |
|---|---|---|---|
| 1 | arXiv API | all:"vision-language-action" AND all:efficient | 22 |
| 2 | arXiv API | all:"action chunking" | 12 |
| 3 | arXiv API | all:VLA AND all:"token pruning" | 18 |
| 4 | arXiv API | all:VLA AND all:"KV cache" | 10 |
| 5 | arXiv API | all:VLA AND all:caching AND all:inference | 14 |
| 6 | arXiv API | all:VLA AND all:"early exit" | 6 |
| 7 | arXiv API | all:"mixture of experts" AND all:"robot policy" | 1 |
| 8 | arXiv API | all:VLA AND all:"mixture-of-experts" | 6 |
| 9 | arXiv API | all:"speculative decoding" AND all:(VLA OR robot OR action) | 5 |
| 10 | arXiv API | all:"consistency policy" | 4 |
| 11 | arXiv API | all:"one-step" AND all:"diffusion policy" | 8 |
| 12 | arXiv API | all:"flow matching" AND all:"robot" AND all:policy AND all:efficient | 10 |
| 13 | arXiv API | all:"action tokenization" AND all:robot | 8 |
| 14 | arXiv API | all:"dual-system" AND all:VLA | 12 |
| 15 | arXiv API | all:"fast" AND all:"slow" AND all:VLA | 8 |
| 16 | arXiv API | all:hierarchical AND all:VLA AND all:latency | 5 |
| 17 | arXiv API | all:Mamba AND all:robot AND all:policy | 4 |
| 18 | arXiv API | all:"state space model" AND all:"imitation learning" | 3 |
| 19 | arXiv API | all:"parallel decoding" AND all:action | 4 |
| 20 | arXiv API | all:"real-time" AND all:VLA AND all:inference | 17 |
| 21 | arXiv API | all:"lightweight" AND all:"vision-language-action" | 7 |
| 22 | arXiv API | all:"small" AND all:"vision-language-action" AND all:model | 3 |
| 23 | arXiv API | all:"streaming" AND all:"diffusion policy" | 1 |
| 24 | arXiv API | all:"diffusion policy" AND all:distillation | 8 |
| 25 | arXiv API | all:"rectified flow" AND all:policy AND all:robot | 2 |
| 26 | arXiv API | ti:"RT-1" AND ti:"Robotics Transformer" | 1 |
| 27 | arXiv API | ti:"RT-2" AND all:"vision-language-action" | 1 |
| 28 | arXiv API | ti:OpenVLA | 1 |
| 29 | arXiv API | ti:Octo AND all:"generalist robot policy" | 1 |
| 30 | arXiv API | all:"pi0" AND all:"flow model" AND all:"vision-language-action" | 1 |
| 31 | arXiv API | ti:"MiniVLA" OR all:"MiniVLA" | 0 |
| 32 | arXiv API | ti:"RDT-1B" OR ti:"Robotics Diffusion Transformer" | 2 |
| 33 | arXiv API | ti:CogACT | 1 |
| 34 | arXiv API | all:"Hi Robot" AND all:hierarchical | 1 |
| 35 | arXiv API | ti:"Gemini Robotics" | 3 |
| 36 | arXiv API | ti:"Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware" | 1 |
| 37 | arXiv API | ti:"Diffusion Policy" AND ti:"Visuomotor Policy Learning via Action Diffusion" | 1 |
| 38 | arXiv API | all:"token merging" AND all:robot | 2 |
| 39 | arXiv API | all:"visual token" AND all:reduction AND all:"robot manipulation" | 0 |
| 40 | arXiv API | all:"temporal ensembling" AND all:action | 3 |
| 41 | arXiv API | all:"hypernetwork" AND all:"robot policy" | 2 |
| 42 | arXiv API | all:"layer skipping" AND all:"robot" | 1 |
| 43 | arXiv API | all:"adaptive computation" AND all:"robot policy" | 1 |
| 44 | arXiv API | all:"diffusion transformer policy" AND all:efficient | 2 |
| 45 | arXiv API | all:"autoregressive" AND all:"action expert" AND all:VLA | 1 |
| 46 | arXiv API | all:"discrete diffusion" AND all:VLA | 2 |
| 47 | arXiv API | all:"asynchronous inference" AND all:robot | 16 |
| 48 | arXiv API | all:"action chunk" AND all:"inference delay" | 3 |
| 49 | arXiv API | all:"System 2" AND all:"System 1" AND all:robot | 1 |
| 50 | arXiv API | all:"humanoid" AND all:VLA AND all:"real-time" | 1 |
| 51 | WebSearch | Figure Helix vision-language-action System 1 System 2 200 Hz humanoid | 1 |
| 52 | WebSearch | Gemini Robotics On-Device model runs locally on robot DeepMind blog | 1 |
| 53 | WebSearch | Dyna Robotics DYNA-1 foundation model blog | 1 |
| 54 | WebSearch | MiniVLA Stanford blog 1B VLA faster than OpenVLA | 1 |
| 55 | WebSearch | NVIDIA GR00T N1.5 N1.6 architecture frozen VLM inference latency blog | 2 |
| 56 | WebSearch | Physical Intelligence blog pi0.5 knowledge insulation real-time action chunking | 2 |
| 57 | WebSearch | Hugging Face blog SmolVLA asynchronous inference lerobot | 1 |
| 58 | arXiv API | all:"pi0.5" AND all:"open-world generalization" | 0 |
| 59 | arXiv API | all:"knowledge insulating" AND all:"vision-language-action" | 1 |
| 60 | arXiv API | all:"VLA-Adapter" | 2 |
| 61 | arXiv API | all:"TinyVLA" OR all:"tiny VLA" OR all:"compact VLA" | 2 |
| 62 | arXiv API | all:"visual token" AND all:"vision-language-action" AND all:compression | 1 |
| 63 | arXiv API | all:"action expert" AND all:"flow matching" AND all:"inference" | 1 |
| 64 | arXiv API | all:"denoising steps" AND all:VLA AND all:reduce | 2 |
| 65 | arXiv API | all:"shortcut model" AND all:policy AND all:robot | 3 |
| 66 | arXiv API | all:"mean flow" AND all:policy | 2 |
| 67 | arXiv API | all:"diffusion policy" AND all:"real-time" AND all:"inference speed" | 1 |
| 68 | arXiv API | all:"autoregressive" AND all:"diffusion" AND all:"hybrid" AND all:VLA | 1 |
| 69 | arXiv API | all:"layer pruning" AND all:VLA | 0 |
| 70 | arXiv API | all:"feature caching" AND all:diffusion AND all:policy | 1 |
| 71 | arXiv API | all:"video" AND all:"world action model" AND all:efficient | 0 |
| 72 | arXiv API | all:"on-device" AND all:"vision-language-action" | 6 |
| 73 | arXiv API | all:"Jetson" AND all:"vision-language-action" | 4 |
| 74 | arXiv API | all:"latent action" AND all:VLA AND all:efficient | 0 |
| 75 | arXiv API | all:"memory" AND all:VLA AND all:efficient AND all:"long-horizon" | 2 |
| 76 | arXiv API | all:"reasoning" AND all:VLA AND all:latency AND all:"chain-of-thought" | 4 |
| 77 | arXiv API | all:"navigation" AND all:VLA AND all:efficient AND all:"real-time" | 2 |
| 78 | arXiv API | ti:"pi_0.5" OR open-world generalization VLA Physical Intelligence | 1 |
| 79 | arXiv API | all:"efficient" AND all:"diffusion policy" AND all:"action chunk" | 3 |
| 80 | arXiv API | all:"VLA" AND all:"inference acceleration" AND all:"training-free" | 0 |
| 81 | arXiv API | all:"lightweight" AND all:"diffusion policy" AND all:"embedded" | 0 |
| 82 | arXiv API | all:"small language model" AND all:"robot" AND all:"policy" | 0 |
| 83 | arXiv API | all:"flow matching" AND all:"VLA" AND all:"one-step" | 1 |
| 84 | arXiv API | all:"hierarchical" AND all:"vision-language-action" AND all:"high-frequency" | 0 |
| 85 | arXiv API | all:"early-exit" AND all:"robot" | 0 |
| 86 | arXiv API | all:"token reduction" AND all:"VLA" | 1 |
| 87 | arXiv API | all:"efficient VLA" | 4 |
| 88 | arXiv API | all:"action chunk" AND all:"latency" AND all:"VLA" | 5 |

#### Notes
- The Semantic Scholar API returned HTTP 429 every time I tried it: the IP is shared with the parallel cluster agents. Because of that, citation/reference snowballing through the S2 graph was **not** done. As a substitute I searched for every seed title and followed the seed names and base models that recur across results (OpenVLA, pi0/pi0.5, GR00T, SmolVLA, CogACT, RTC, VLA-Cache).
- Most sources were verified through arXiv API abstracts (export.arxiv.org). The industry blogs and project pages for Helix, MiniVLA, Gemini Robotics On-Device, DYNA-1, GR00T N1.5/N1.6 and the HF async inference post were each fetched with WebFetch. The one exception is the PI RTC blog page: I saw it only as a search result, so it is marked verified=false.
- Saturation: the brief's rule was **not** met. The last 10 searches (rows 79-88) turned up 14 new relevant items. Several of those 10 queries returned zero new items, but broad queries ("efficient VLA", "action chunk latency VLA") kept finding new 2026 preprints. The 2025-2026 literature in this area is growing faster than the search could exhaust it.

## C2 — Compression for robot foundation models

89 logged query rows.


Counts are approximate: an item is credited to each query that surfaced it as a relevant hit, so the column total (175) is higher than the 130 unique records. The Semantic Scholar and arXiv APIs were heavily rate-limited because other cluster agents were using them at the same time, so the arXiv HTML search page was used as the main discovery source.

| # | source | query | new relevant items |
|---|---|---|---|
| 1 | Semantic Scholar | citations of BitVLA arXiv:2506.07530 | 14 |
| 2 | Semantic Scholar | vision-language-action quantization | 12 |
| 3 | Semantic Scholar | robot policy quantization | 2 |
| 4 | Semantic Scholar | post-training quantization vision-language-action (rate-limited, empty) | 0 |
| 5 | Semantic Scholar | quantization-aware imitation learning (rate-limited, empty) | 0 |
| 6 | Semantic Scholar | 1-bit vision-language-action model (rate-limited, empty) | 0 |
| 7 | Semantic Scholar | VLA pruning (rate-limited, empty) | 0 |
| 8 | Semantic Scholar | layer skipping vision-language-action (rate-limited, empty) | 0 |
| 9 | Semantic Scholar | knowledge distillation vision-language-action (rate-limited, empty) | 0 |
| 10 | Semantic Scholar | policy distillation robot foundation model | 0 |
| 11 | Semantic Scholar | distilling diffusion policy one step | 1 |
| 12 | Semantic Scholar | low-rank compression robot policy | 0 |
| 13 | Semantic Scholar | binary neural network robot control | 0 |
| 14 | Semantic Scholar | structured pruning robot manipulation policy | 0 |
| 15 | Semantic Scholar | early exit vision-language-action | 0 |
| 16 | Semantic Scholar | compressed world model robot | 0 |
| 17 | Semantic Scholar | model compression embodied AI | 0 |
| 18 | Semantic Scholar | 4-bit quantization robot | 0 |
| 19 | Semantic Scholar | mixed-precision quantization VLA | 0 |
| 20 | Semantic Scholar | token pruning vision-language-action (scoped out to C1) | 0 |
| 21 | arXiv API | abs:quantization AND abs:vision-language-action (HTTP 429, abandoned) | 0 |
| 22 | arXiv API | abs:pruning AND abs:vision-language-action (HTTP 429, abandoned) | 0 |
| 23 | WebSearch | VLA quantization 4-bit OpenVLA INT4 robot manipulation success rate | 2 |
| 24 | WebSearch | github awesome efficient VLA quantization pruning distillation list | 0 |
| 25 | WebSearch | distilling VLA into small student policy real-time robot teacher-student 2025 | 5 |
| 26 | WebSearch | pruning vision-language-action model layers redundancy DeeR-VLA MoLe-VLA | 3 |
| 27 | WebSearch | consistency policy distillation diffusion policy one-step robot visuomotor | 2 |
| 28 | WebSearch | does quantization/compression hurt generalization VLA robustness study | 0 |
| 29 | WebSearch | TinyVLA OR SmolVLA OR compact VLA distillation from larger VLA | 3 |
| 30 | WebSearch | quantized pi0 / GR00T deployment Jetson INT8 FP8 TensorRT VLA | 2 |
| 31 | arXiv search (HTML) | quantization vision-language-action | 14 |
| 32 | arXiv search (HTML) | pruning vision-language-action | 6 |
| 33 | arXiv search (HTML) | distillation vision-language-action | 5 |
| 34 | arXiv search (HTML) | quantization robot policy | 4 |
| 35 | arXiv search (HTML) | quantization imitation learning | 2 |
| 36 | arXiv search (HTML) | quantization diffusion policy | 0 |
| 37 | arXiv search (HTML) | distillation diffusion policy | 2 |
| 38 | arXiv search (HTML) | quantization vision-language-action (page 2) | 3 |
| 39 | arXiv search (HTML) | layer skipping VLA | 3 |
| 40 | arXiv search (HTML) | early exit robot policy | 1 |
| 41 | arXiv search (HTML) | knowledge distillation robot manipulation policy | 2 |
| 42 | arXiv search (HTML) | 1-bit robot | 2 |
| 43 | arXiv search (HTML) | compression world model | 2 |
| 44 | arXiv search (HTML) | low-rank vision-language-action | 0 |
| 45 | arXiv search (HTML) | compressed VLA | 0 |
| 46 | arXiv search (HTML) | binary neural network robot | 0 |
| 47 | arXiv search (HTML) | consistency distillation visuomotor policy | 3 |
| 48 | arXiv search (HTML) | one-step policy distillation robot | 4 |
| 49 | arXiv search (HTML) | self-distillation flow matching VLA | 1 |
| 50 | arXiv search (HTML) | quantization world action model | 2 |
| 51 | arXiv search (HTML) | Jetson quantized VLA | 0 |
| 52 | arXiv search (HTML) | quantization flow matching policy | 0 |
| 53 | arXiv search (HTML) | structured pruning diffusion policy | 0 |
| 54 | arXiv search (HTML) | distill vision-language-action small model | 1 |
| 55 | arXiv search (HTML) | mixed-precision vision-language-action | 1 |
| 56 | Semantic Scholar | citations of QAIL arXiv:2412.01034 | 4 |
| 57 | Semantic Scholar | citations of SQIL arXiv:2505.15304 | 2 |
| 58 | Semantic Scholar | citations of SQAP-VLA arXiv:2509.09090 | 0 |
| 59 | Semantic Scholar | citations of RLRC arXiv:2506.17639 | 1 |
| 60 | Semantic Scholar | citations of EaqVLA arXiv:2505.21567 | 0 |
| 61 | Semantic Scholar | citations of GLUESTICK arXiv:2510.08464 | 0 |
| 62 | Semantic Scholar | citations of MoLe-VLA arXiv:2503.20384 | 2 |
| 63 | Semantic Scholar | citations of OneDP arXiv:2410.21257 | 7 |
| 64 | Semantic Scholar | citations of Consistency Policy arXiv:2405.07503 | 3 |
| 65 | Semantic Scholar | references of BitVLA arXiv:2506.07530 | 5 |
| 66 | Semantic Scholar | references of QAIL arXiv:2412.01034 | 5 |
| 67 | arXiv abs pages | direct fetch: EfficientVLA, DeeR-VLA, TinyVLA, SmolVLA, NanoVLA, foundational techniques (AWQ, GPTQ, SmoothQuant, QuaRot, SpinQuant, BitNet, LLM.int8, SparseGPT, Wanda, ShortGPT, consistency models, progressive distillation, KD) | 21 |
| 68 | arXiv search (HTML) | quantization humanoid policy | 1 |
| 69 | arXiv search (HTML) | quantization autonomous driving VLA | 0 |
| 70 | arXiv search (HTML) | pruning world model robot | 1 |
| 71 | arXiv search (HTML) | distillation world model policy compact | 0 |
| 72 | arXiv search (HTML) | weight sharing robot policy transformer | 0 |
| 73 | arXiv search (HTML) | low-bit vision encoder robot policy | 0 |
| 74 | arXiv search (HTML) | model compression robot learning | 1 |
| 75 | arXiv search (HTML) | quantization reinforcement learning policy deployment | 2 |
| 76 | arXiv search (HTML) | sparsity mixture of experts VLA efficient | 0 |
| 77 | Semantic Scholar | citations of OpenVLA arXiv:2406.09246 (3,626 citing papers scanned, filtered for compression) | 11 |
| 78 | Semantic Scholar | citations of HBVLA / QVLA / Shallow-pi | 0 |
| 79 | Semantic Scholar | citations of DeeR-VLA arXiv:2411.02359 | 3 |
| 80 | WebFetch | Jetson AI Lab: OpenPi pi0.5 on Jetson Thor tutorial | 1 |
| 81 | arXiv search (HTML) | FP8 robot policy inference | 1 |
| 82 | arXiv search (HTML) | quantization-aware training vision-language-action | 0 |
| 83 | arXiv search (HTML) | GR00T quantization | 0 |
| 84 | arXiv search (HTML) | pi0 compression | 0 |
| 85 | arXiv search (HTML) | SVD low-rank decomposition policy transformer robot | 0 |
| 86 | arXiv search (HTML) | quantized world model planning robot | 0 |
| 87 | arXiv search (HTML) | knowledge distillation humanoid policy compact | 0 |
| 88 | arXiv search (HTML) | weight pruning visuomotor policy | 0 |
| 89 | Semantic Scholar | VLA model compression deployment / distillation VLA student / pruning robot policy transformer / quantized diffusion policy robot / low-bit robot foundation model / compressed policy closed-loop failure (6 queries, rate-limited) | 0 |

## C3 — Memory-efficient adaptation and fine-tuning

51 logged query rows.

| # | source | query | new relevant items |
|---|---|---|---|
| 1 | arXiv API (id_list) | seed works: 2502.19645, 2406.09246, 2106.09685, 2305.14314, 2405.12213, 2509.09674, 2505.19789, 2505.18719, 2502.05450, 2412.06685, 2501.16664, 2506.01844 | 12 |
| 2 | arXiv API | abs:"parameter-efficient" AND abs:"vision-language-action" (+2 more) | 0 (HTTP 429 rate-limited) |
| 3 | WebSearch | parameter-efficient fine-tuning vision-language-action model arXiv | 7 |
| 4 | WebSearch | LoRA fine-tuning robot policy VLA adapter arXiv 2025 | 6 |
| 5 | WebSearch | reinforcement learning fine-tuning VLA flow matching pi0 arXiv 2025 | 8 |
| 6 | WebSearch | continual learning vision-language-action model catastrophic forgetting arXiv | 5 |
| 7 | WebSearch | RLinf VLA reinforcement learning infrastructure embodied arXiv | 3 |
| 8 | WebSearch | few-shot adaptation vision-language-action model new embodiment efficient | 4 |
| 9 | WebSearch | memory-efficient training VLA model single GPU fine-tuning arXiv | 1 |
| 10 | WebSearch | real-world RL fine-tuning generalist robot policy human-in-the-loop VLA arXiv | 9 |
| 11 | WebSearch | pi0 fine-tuning openpi LoRA recipe Physical Intelligence blog | 3 |
| 12 | WebSearch | "knowledge insulation" OR "co-training" VLA training efficiency pi0.5 arXiv | 4 |
| 13 | WebSearch | QLoRA 4-bit fine-tuning OpenVLA robot manipulation | 0 (C2 items only) |
| 14 | WebSearch | adapter tuning robot foundation model prompt tuning visuomotor policy efficient transfer | 4 |
| 15 | Semantic Scholar API | citations of arXiv:2502.19645 (OpenVLA-OFT), 952 citing papers, title-filtered | ~85 candidates |
| 16 | arXiv API (id_list) | batch fetch of OFT citing candidates A/B/C | 83 |
| 17 | WebSearch | TAIL task-specific adapters imitation learning LoRA robot continual | 3 |
| 18 | WebSearch | diffusion steering latent space RL DSRL fine-tune pi0 noise policy | 2 |
| 19 | WebSearch | GR00T N1 post-training fine-tuning humanoid LoRA memory NVIDIA | 2 |
| 20 | WebSearch | HIL-SERL SERL sample-efficient real-world robot reinforcement learning fine-tuning pretrained | 3 |
| 21 | Semantic Scholar API | parameter-efficient fine-tuning robot policy; LoRA vision-language-action; RL fine-tuning VLA | 0 (HTTP 429, failed) |
| 22 | WebSearch | DPPO / GRAPE / LeRobot / RLDG queries | 0 (session web-search budget exhausted) |
| 23 | arXiv API | ti:"policy optimization" AND abs:diffusion AND abs:"fine-tuning" AND cat:cs.RO | 2 |
| 24 | arXiv API | abs:"vision-language-action" AND abs:"preference optimization" | 2 |
| 25 | arXiv API | abs:"vision-language-action" AND abs:LoRA | 6 |
| 26 | arXiv API | abs:"generalist robot polic" AND abs:"fine-tun" AND abs:efficien | 0 |
| 27 | arXiv API | abs:"vision-language-action" AND abs:"continual learning" | 7 |
| 28 | arXiv API | abs:"vision-language-action" AND abs:"reinforcement learning" AND abs:"sample efficien" | 0 |
| 29 | arXiv API | abs:"robot" AND abs:"parameter-efficient fine-tuning" | 5 |
| 30 | arXiv API | ti:VLA AND ti:RL | 4 |
| 31 | arXiv API | abs:"vision-language-action" AND abs:GRPO | 6 |
| 32 | arXiv API | abs:"vision-language-action" AND abs:"few-shot" | 3 |
| 33 | arXiv API | abs:LeRobot | 2 |
| 34 | arXiv API | title lookups: Policy Decorator; RLDG; GRAPE; Sparse Diffusion Policy; HPT; RoboFuME | 6 |
| 35 | arXiv API | abs:"policy steering" AND abs:"value function" AND abs:generalist | 2 |
| 36 | arXiv API | abs:"vision-language-action" AND abs:"test-time adaptation" | 2 |
| 37 | arXiv API | abs:"vision-language-action" AND abs:"model merging" | 1 |
| 38 | arXiv API | abs:"vision-language-action" AND abs:"cross-embodiment" AND abs:"fine-tuning" AND abs:efficient | 1 |
| 39 | arXiv API | abs:"vision-language-action" AND abs:"offline reinforcement learning" | 4 |
| 40 | arXiv API | abs:"vision-language-action" AND abs:"residual policy" | 1 |
| 41 | arXiv API | abs:"vision-language-action" AND abs:"world model" AND abs:"post-training" | 7 |
| 42 | arXiv API | abs:"diffusion policy" AND abs:LoRA | 0 |
| 43 | arXiv API | abs:"vision-language-action" AND abs:"quantization" AND abs:"fine-tuning" AND abs:memory | 0 |
| 44 | arXiv API | abs:"vision-language-action" AND abs:"training cost" | 3 |
| 45 | arXiv API | abs:"vision-language-action" AND abs:"catastrophic forgetting" | 6 |
| 46 | arXiv API | abs:"vision-language-action" AND abs:adapter AND abs:"parameter" | 3 |
| 47 | arXiv API | abs:"vision-language-action" AND abs:"single GPU" | 1 |
| 48 | arXiv API | abs:"vision-language-action" AND abs:"on-device" AND abs:"fine-tun" | 0 |
| 49 | arXiv API | abs:"QLoRA" AND abs:robot | 0 |
| 50 | arXiv API | abs:"low-rank adaptation" AND abs:"robot manipulation" AND abs:policy | 0 |
| 51 | arXiv API | abs:"post-training" AND abs:"vision-language-action" AND abs:"compute" | 3 (C2 quantization hits left to C2) |

## C4 — Benchmarking methodology and composability

87 logged query rows.


Note: arXiv API/search and Semantic Scholar API were intermittently rate-limited (HTTP 429, shared IP with sibling agents); arXiv abs pages were used for verification and WebSearch for discovery. S2 citation snowballing was unavailable throughout.

| # | source | query | new relevant items |
|---|---|---|---|
| 1 | arXiv API | all:"LIBERO" AND all:benchmark | 14 |
| 2 | arXiv API | all:"vision-language-action" AND all:latency AND all:benchmark | 6 |
| 3 | arXiv API | all:"inference latency" AND all:"robot policy" | 4 |
| 4 | arXiv API | all:"control frequency" AND all:"vision-language-action" | 3 |
| 5 | arXiv API | all:VLA AND all:acceleration AND all:evaluation | 8 |
| 6 | arXiv API | ti:efficiency AND abs:embodied AND abs:benchmark (rate-limited, 429) | 0 |
| 7 | WebSearch | SimplerEnv evaluating real-world robot manipulation policies in simulation arXiv | 2 |
| 8 | WebSearch | RoboArena distributed real-world evaluation generalist robot policies | 3 |
| 9 | WebSearch | AutoEval autonomous evaluation generalist robot manipulation policies real world | 2 |
| 10 | WebSearch | VLA inference latency energy profiling Jetson benchmark across hardware 2025 | 4 |
| 11 | WebSearch | CALVIN benchmark long-horizon; RLBench; ManiSkill3 GPU parallelized simulation arXiv | 6 |
| 12 | WebSearch | RoboCasa large-scale simulation everyday tasks; VLABench; RoboTwin benchmark arXiv | 5 |
| 13 | WebSearch | LIBERO-Plus in-depth robustness analysis vision-language-action models | 1 |
| 14 | WebSearch | "closed-loop" vs "open-loop" control frequency VLA reporting asynchronous inference real-time chunking evaluation | 6 |
| 15 | arXiv search | tail latency robot policy | 1 |
| 16 | arXiv search | VLA inference latency hardware profiling | 0 |
| 17 | arXiv search | vision-language-action edge deployment benchmark latency | 2 |
| 18 | arXiv search | robot manipulation benchmark reproducibility evaluation | 10 |
| 19 | arXiv search | real-world robot policy evaluation protocol statistical | 1 |
| 20 | arXiv search | energy consumption robot foundation model inference | 0 |
| 21 | arXiv search | embodied AI benchmark efficiency | 2 |
| 22 | arXiv search | vision-language-action compression combined quantization pruning | 1 |
| 23 | arXiv search | VLA evaluation simulation real correlation | 4 |
| 24 | arXiv search | VLA latency | 7 |
| 25 | arXiv search | VLA inference performance | 3 |
| 26 | arXiv search | robot policy energy | 2 |
| 27 | arXiv search | VLA benchmark latency | 3 |
| 28 | arXiv search | VLA quantization | 6 |
| 29 | arXiv search | Jetson VLA | 5 |
| 30 | arXiv search | robot policy evaluation world model | 6 |
| 31 | arXiv search | VLA leaderboard | 5 |
| 32 | arXiv search | robot policy evaluation statistical | 9 |
| 33 | arXiv search | compressed VLA robustness | 0 |
| 34 | arXiv search | VLA power consumption | 1 |
| 35 | arXiv search | embodied inference energy | 6 |
| 36 | arXiv search | robot learning reproducibility | 1 |
| 37 | arXiv search | VLA pruning evaluation closed-loop | 0 |
| 38 | arXiv search | policy evaluation real robot scalable | 4 |
| 39 | WebSearch | "embodied-efficiency-bench" OR "efficiency benchmark" vision-language-action latency energy leaderboard github | 4 |
| 40 | WebSearch | Hugging Face LeRobot asynchronous inference blog SmolVLA latency | 2 |
| 41 | WebSearch | NVIDIA Jetson Thor GR00T N1 inference latency benchmark blog | 2 |
| 42 | WebSearch | MLPerf robotics inference benchmark embodied AI workload | 2 |
| 43 | arXiv search | THE COLOSSEUM robotic manipulation generalization benchmark | 1 |
| 44 | arXiv search | RoboChallenge real robot online evaluation | 1 |
| 45 | arXiv search | BEHAVIOR-1K benchmark (no direct hit; fetched 2403.09227 by id) | 1 |
| 46 | arXiv search | GemBench generalizable manipulation benchmark | 1 |
| 47 | arXiv search | RoboEval manipulation benchmark | 1 |
| 48 | arXiv search | Embodied Arena | 1 |
| 49 | arXiv search | FurnitureBench reproducible real-world benchmark | 1 |
| 50 | arXiv search | VLA acceleration orthogonal combined caching pruning | 0 |
| 51 | arXiv search | efficient VLA unified comparison | 0 |
| 52 | arXiv search | training-free acceleration VLA benchmark comparison | 0 |
| 53 | arXiv search | token caching VLA | 3 |
| 54 | arXiv search | VLA inference speedup success rate trade-off | 0 |
| 55 | arXiv search | action chunk size latency trade-off | 0 |
| 56 | arXiv search | inference delay robot policy | 0 |
| 57 | WebSearch | do VLA acceleration techniques compose? combining quantization token pruning caching | 2 |
| 58 | WebSearch | action chunk size inference latency trade-off study robot policy reactivity evaluation | 5 |
| 59 | WebSearch | RoboChallenge Table30 real-robot benchmark embodied policies online evaluation Dexmal | 2 |
| 60 | arXiv search | RobotArena (throttled, empty) | 0 |
| 61 | arXiv search | latency injection simulation policy evaluation (throttled, empty) | 0 |
| 62 | arXiv search | SimplerEnv (throttled, empty) | 0 |
| 63 | arXiv search | LIBERO saturated (throttled, empty) | 0 |
| 64 | arXiv search | real-to-sim policy evaluation Gaussian splatting (throttled, empty) | 0 |
| 65 | arXiv search | VLA edge benchmark (throttled, empty) | 0 |
| 66 | arXiv search | robot foundation model deployment latency measurement (throttled, empty) | 0 |
| 67 | WebSearch | RobotArena infinity scalable robot policy benchmarking real-to-sim translation | 3 |
| 68 | WebSearch | simulated inference latency injection benchmark robot policy evaluation delay robustness VLA | 1 |
| 69 | WebSearch | real-to-sim Gaussian splatting policy evaluation correlation VLA benchmark 2025 | 3 |
| 70 | WebSearch | VLA model deployment edge devices benchmark study Jetson Orin OpenVLA pi0 latency memory comparison | 3 |
| 71 | WebSearch | benchmark dynamic manipulation moving objects VLA reaction latency evaluation 2026 | 2 |
| 72 | WebSearch | robot policy evaluation energy consumption per task motion energy metric benchmark manipulation | 2 |
| 73 | WebSearch | WorldArena benchmark world models embodied evaluation leaderboard | 2 |
| 74 | WebSearch | control loop jitter timing variance learned robot policy real-time deployment analysis ROS 2 VLA | 2 |
| 75 | WebSearch | OpenReview CoRL 2025 evaluation protocol vision-language-action benchmark flaws success rate confidence intervals | 3 |
| 76 | WebSearch | SimplerEnv limitations critique visual matching variant aggregation sim-real gap VLA | 0 |
| 77 | WebSearch | humanoid VLA onboard inference latency benchmark whole-body real-time evaluation | 1 |
| 78 | WebSearch | "LIBERO" benchmark saturation near 100% success VLA evaluation critique memorization 2026 | 0 |
| 79 | WebSearch | CALVIN ABC-D efficiency latency comparison VLA inference speed benchmark table | 2 |
| 80 | WebSearch | Physical Intelligence openpi inference speed pi0 RTX 4090 latency blog knowledge insulation | 1 |
| 81 | WebSearch | hardware-normalized comparison robot policy inference FLOPs latency proxy misleading embodied | 0 |
| 82 | WebSearch | ManiSkill3 VLA evaluation GPU parallel rollouts speed benchmark policy evaluation throughput | 1 |
| 83 | WebSearch | RLBench VLA latency efficient 3D policy inference speed comparison benchmark | 1 |
| 84 | WebSearch | "tail latency" OR "p99" VLA robot inference deadline miss real-time scheduling | 1 |
| 85 | WebSearch | RoboArena follow-up crowdsourced pairwise evaluation DROID policy ranking Bradley-Terry 2026 | 0 |
| 86 | WebSearch | reproducibility crisis robot learning seeds variance evaluation VLA fine-tuning random seed | 1 |
| 87 | Semantic Scholar API | citations of arXiv:2602.18397 / search LIBERO benchmark (HTTP 429, no results) | 0 |

## C5 — Hardware-aware design and accelerators

74 logged query rows.


| # | source | query | new relevant items |
|---|---|---|---|
| 1 | arXiv API | all:"vision-language-action" AND (Jetson OR edge OR onboard) | 26 |
| 2 | WebSearch | Jetson Thor GR00T N1 deployment TensorRT inference latency blog | 4 |
| 3 | WebSearch | LeRobot pi0 SmolVLA deployment Jetson Orin inference speed | 0 (dups of Jetson-PI etc.) |
| 4 | WebSearch | AWS Neuron Trainium robotics VLA policy inference blog | 0 (no robotics-specific Neuron post found) |
| 5 | arXiv API (x8 queued: Jetson Orin robot; TensorRT robot; HW-SW co-design robot; accelerator VLA; profiling OpenVLA; memory bandwidth VLA; FlashAttention; Jetson diffusion policy) | — | 0 (HTTP 429 rate-limited, aborted) |
| 6 | WebSearch | arxiv profiling OpenVLA inference latency edge GPU memory-bound analysis | 1 |
| 7 | WebSearch | arxiv VLA accelerator FPGA ASIC design robot policy inference | 4 |
| 8 | WebSearch | arxiv "Jetson" diffusion policy real-time inference robot manipulation onboard | 3 |
| 9 | Semantic Scholar search | vision-language-action model edge deployment hardware latency | 0 (HTTP 429) |
| 10 | WebSearch | arxiv 2026 VLA inference Jetson Thor NVFP4 FP8 humanoid onboard | 2 |
| 11 | WebSearch | arxiv processing-in-memory OR NPU accelerator embodied AI robot foundation model inference | 3 |
| 12 | WebSearch | arxiv Qualcomm Snapdragon NPU on-device robot policy VLA | 2 |
| 13 | Semantic Scholar batch | seed lookup: FlashAttention 1/2/3, PagedAttention, FlashInfer, OpenVLA, pi0, GR00T N1, SmolVLA, TinyVLA, AWQ | 11 |
| 14 | WebFetch arXiv HTML | OpenVLA / pi0 inference-speed sections | (enrichment) |
| 15 | Semantic Scholar citations | citations of 2602.18397 (VLA-Perf) | 8 |
| 16 | Semantic Scholar citations | citations of 2604.24447 (VLA XPU characterization) | 3 |
| 17 | Semantic Scholar citations | citations of 2603.02271 (VLA edge action-generation bottleneck) | 2 |
| 18 | Semantic Scholar citations | citations of 2509.11480 (cross-platform scaling) | 2 |
| 19 | Semantic Scholar citations | citations of 2606.08094 (vla.cpp) | 1 |
| 20 | WebSearch | Figure Helix onboard embedded GPUs low-power inference humanoid | 1 |
| 21 | WebSearch | Gemini Robotics On-Device model runs locally on robot latency | 1 |
| 22 | WebSearch | NVIDIA technical blog Jetson Thor humanoid Blackwell FP4 GR00T | 1 |
| 23 | WebSearch | Unitree G1 onboard compute Jetson Orin NX VLA deployment | 0 (vendor/listicle pages only) |
| 24 | WebSearch | Hugging Face blog async inference LeRobot SmolVLA policy server | 1 |
| 25 | WebSearch | TensorRT-LLM OpenVLA acceleration robot policy real-time kernel fusion | 2 |
| 26 | Semantic Scholar batch | lookup: Running VLAs at Real-time Speed, BLURR, RTC, DeeR-VLA, OpenVLA-OFT | 4 |
| 27 | Semantic Scholar citations | citations of 2510.26742 (Running VLAs at Real-time Speed) | 6 |
| 28 | WebSearch | arxiv FPGA accelerator vision-language-action OR diffusion policy robot | 1 |
| 29 | WebSearch | arxiv algorithm-hardware co-design embodied AI accelerator robot manipulation | 1 |
| 30 | WebSearch | humanoid robot onboard compute power budget watts battery VLA inference | 1 |
| 31 | WebSearch | Corki embodied AI accelerator follow-up ISCA MICRO HPCA robotics | 0 (enriched Corki: ISCA 2025, ZC706 FPGA) |
| 32 | WebSearch | arxiv TPU inference robot policy real-time Gemini Robotics latency cloud local decoder | 2 |
| 33 | WebSearch | arxiv world model inference Jetson onboard real-time robot DreamerV3 edge | 1 |
| 34 | WebSearch | arxiv Jetson Orin quadruped locomotion humanoid whole-body controller onboard latency | 2 |
| 35 | WebSearch | arxiv edge VLA speculative OR pipeline Jetson AGX Orin latency ms 2026 | 2 |
| 36 | WebSearch | arxiv robotics computing workload characterization GPU embodied agents LLM | 1 |
| 37 | WebSearch | arxiv spiking OR neuromorphic Loihi robot policy energy efficient inference | 0 (non-FM SNN control; skipped) |
| 38 | WebSearch | arxiv Apple silicon MLX OR mobile phone VLA inference robot on-device | 0 (LLM-only) |
| 39 | WebSearch | arxiv VLA quantization Jetson TensorRT INT8 FP8 Orin pi0 OR GR00T | 0 (dups; enriched FoldQuantVLA code) |
| 40 | Semantic Scholar citations | citations of 2407.04292 (Corki) | 7 |
| 41 | Semantic Scholar citations | citations of 2512.20276 (ActionFlow) / 2603.18284 (Offload or Overload) | 0 (all already recorded) |
| 42 | Semantic Scholar references | references of 2608.04428 (Deltoris) | 3 |
| 43 | WebSearch | KERV kinematic-rectified speculative decoding embodied VLA | 1 |
| 44 | WebSearch | ReCA integrated acceleration cooperative embodied agents | 1 |
| 45 | WebSearch | Tartan microarchitecting a robotic processor ISCA 2024 | 1 |
| 46 | arXiv API | all:"vision-language-action" AND (accelerator OR hardware OR GPU OR energy) | 2 |
| 47 | arXiv API | all:Jetson AND ("robot policy" OR manipulation OR VLA OR "foundation model") | 6 |
| 48 | arXiv API | all:TensorRT AND (robot OR VLA OR policy) | 0 |
| 49 | arXiv API | all:embodied AND (accelerator OR co-design) AND (robot OR agent) | 2 |
| 50 | arXiv API | all:"Jetson Thor" | 0 (non-policy) |
| 51 | arXiv API | all:"memory-bound" AND (robot OR VLA OR embodied) | 2 |
| 52 | arXiv API | all:"on-device" AND ("robot policy" OR VLA OR "diffusion policy") | 6 |
| 53 | arXiv API | all:energy AND VLA AND (edge OR battery OR power) | 1 |
| 54 | arXiv API | all:NPU AND (robot OR VLA OR embodied) | 1 |
| 55 | arXiv API | all:FPGA AND (VLA OR "robot policy" OR "diffusion policy" OR "imitation learning") | 0 |
| 56 | arXiv API | all:"Orin Nano" AND (policy OR VLA OR manipulation OR navigation) | 0 |
| 57 | arXiv API | all:serving AND ("robot policy" OR VLA OR "physical AI") | 0 |
| 58 | arXiv API | all:offloading AND (VLA OR "robot foundation model") | 2 |
| 59 | Semantic Scholar citations/refs | citations of 2607.12659, 2603.14371, 2608.03682; references of 2609.22335 | 0 (C2/world-model or generic GPU scheduling) |
| 60 | WebFetch | jetson-ai-lab TensorRT Edge-LLM tutorial | 1 |
| 61 | WebSearch | Tesla Optimus AI5 inference computer onboard humanoid compute specs | 0 (news/fan sites without technical sources) |
| 62 | WebSearch | NVIDIA developer blog GR00T N1.6 Jetson Thor deployment sim-to-real | 1 |
| 63 | arXiv API | all:"CUDA graph" AND (robot OR VLA OR policy) | 1 |
| 64 | arXiv API | all:roofline AND (robot OR VLA OR embodied) | 0 |
| 65 | arXiv API | all:"power consumption" AND (VLA OR "robot foundation model" OR humanoid) AND inference | 0 |
| 66 | arXiv API | all:heterogeneous AND all:"vision-language-action" | 0 |
| 67 | arXiv API | all:"llama.cpp" AND (robot OR VLA) | 1 |
| 68 | arXiv API | all:"inference engine" AND (robot OR VLA) | 0 |
| 69 | arXiv API | all:"Jetson AGX Orin" AND (vision-language OR VLM) AND robot | 0 |
| 70 | arXiv API | all:thermal AND (robot OR VLA) AND (inference OR throttling) | 0 |
| 71 | arXiv API | all:Ascend AND (robot OR VLA OR embodied) | 0 |
| 72 | arXiv API | all:"edge GPU" AND (robot OR policy) AND "foundation model" | 0 |
| 73 | WebSearch | Agility Robotics Digit onboard compute foundation model inference | 0 (session web-search budget exhausted) |
| 74 | arXiv API | all:onboard AND humanoid AND (FM OR VLA) AND (GPU OR Jetson OR compute) | 1 |

Saturation: searches 65-74 yielded 2 new items in total (search 67 and search 74), so the stop threshold of fewer than 2 was not strictly reached. Mining stopped anyway because the WebSearch budget ran out and the arXiv/S2 queries had fallen to near-zero yield.

## C6 — Edge-cloud co-design and fleet systems

97 logged query rows.

| # | source | query | new relevant items |
|---|---|---|---|
| 1 | arXiv API | all:FogROS OR all:"fog robotics" | 0 (rate-limited; switched to arxiv.org/abs scraping) |
| 2 | Semantic Scholar API | FogROS2 cloud robotics | 0 (429 rate-limited) |
| 3 | WebSearch | FogROS2 cloud robotics ROS 2 offloading arXiv | 4 |
| 4 | WebSearch | edge-cloud collaborative VLA inference robot arXiv 2025 | 6 |
| 5 | WebSearch | RoboECC edge cloud VLA | 3 |
| 6 | WebSearch | EdgeVLA efficient vision-language-action edge deployment | 2 |
| 7 | WebSearch | SmolVLA asynchronous inference remote policy server robot | 3 |
| 8 | WebSearch | Gemini Robotics On-Device local VLA model | 1 |
| 9 | WebSearch | openpi remote inference policy server websocket pi0 | 2 |
| 10 | WebSearch | RAPID edge-cloud partitioned inference VLA models | 2 |
| 11 | WebSearch | Gemini Robotics technical report cloud backbone local action decoder latency | 2 |
| 12 | WebSearch | cloud robotics network latency VLA policy offloading 5G arXiv | 4 |
| 13 | WebSearch | split computing robot manipulation policy wireless bandwidth arXiv | 3 |
| 14 | WebSearch | asynchronous VLA inference latency action chunk VLASH | 7 |
| 15 | WebSearch | fleet-scale robot foundation model serving GPU cluster multiple robots inference | 4 |
| 16 | WebSearch | cloud robotics survey foundation models offloading 2024 2025 | 2 |
| 17 | WebSearch | split computing survey edge devices deep neural networks partition | 3 |
| 18 | WebSearch | hierarchical VLA slow cloud planner fast onboard controller dual-system latency | 2 |
| 19 | WebSearch | bandwidth-aware robot policy image compression offloading visuomotor | 1 |
| 20 | Semantic Scholar citations | arXiv:2205.09778 (FogROS2) citing papers | 10 |
| 21 | Semantic Scholar citations | arXiv:2603.20711 (RoboECC) | 0 |
| 22 | Semantic Scholar citations | arXiv:2608.00337 (Armory) | 0 |
| 23 | Semantic Scholar citations | arXiv:2607.01088 (ROSA) | 0 |
| 24 | Semantic Scholar citations | arXiv:2603.18284 (Offload or Overload) | 2 |
| 25 | Semantic Scholar citations | arXiv:2602.13476 (AsyncVLA nav) | 0 |
| 26 | Semantic Scholar citations (filtered) | arXiv:2506.07339 (RTC) | 3 |
| 27 | Semantic Scholar citations (filtered) | arXiv:2506.01844 (SmolVLA) | 1 |
| 28 | Semantic Scholar citations (filtered) | arXiv:2512.01031 (VLASH) | 0 |
| 29 | arXiv abs batch | snowball candidate verification (FogROS2/RTC/VLASH citers) | 15 |
| 30 | WebSearch | FogROS adaptive framework automating fog robotics deployment CASE 2021 | 1 |
| 31 | WebSearch | Tanwani fog robotics approach deep robot learning grasp planning | 1 |
| 32 | WebSearch | LLM robot task planning edge cloud collaboration offloading latency arXiv | 3 |
| 33 | WebSearch | Figure Helix System 1 System 2 onboard embedded GPUs VLA | 1 |
| 34 | WebSearch | "vision-language-action" offloading edge server Wi-Fi latency humanoid remote GPU inference study | 0 |
| 35 | WebSearch | task-oriented semantic communication robot policy VLA transmission protocol edge | 4 |
| 36 | WebSearch | energy carbon footprint VLA inference edge robotic systems | 1 |
| 37 | WebSearch | cloud-edge vision-language navigation UAV large model offloading real-time | 3 |
| 38 | WebSearch | Microsoft Research robot inference offloading edge cloud humanoid study September 2026 | 3 |
| 39 | WebSearch | "VTP" task-aware transmission protocol edge VLA robotic systems | 0 |
| 40 | WebSearch | Hugging Face blog asynchronous inference LeRobot robot client policy server | 1 |
| 41 | WebSearch | RT-2 inference multi-TPU cloud service 1-3 Hz | 1 |
| 42 | arXiv API | abs:cloud AND abs:"vision-language-action" | 3 |
| 43 | arXiv API | abs:"edge-cloud" AND abs:robot | 7 |
| 44 | arXiv API | abs:offload AND robot AND (foundation model OR language model OR VLA OR VLM) | 2 |
| 45 | arXiv API | abs:"cloud robotics" AND abs:latency | 8 |
| 46 | arXiv API | abs:serving AND abs:robot AND (policy OR VLA OR foundation model) | 0 |
| 47 | arXiv API | (5G OR 6G OR wireless) AND (VLA OR robot policy OR robot foundation model) | 0 |
| 48 | WebSearch | total cost of ownership robot fleet onboard GPU versus cloud inference | 1 |
| 49 | WebSearch | arXiv 2026 VLA inference edge server multiple robots GPU sharing latency SLO | 0 |
| 50 | WebSearch | Physical Intelligence blog real-time action chunking latency remote inference | 2 |
| 51 | WebSearch | Distributed VLMs efficient vision-language processing cloud-edge collaboration | 3 |
| 52 | Semantic Scholar citations (filtered) | arXiv:2602.18397 (VLA-Perf) | 2 |
| 53 | Semantic Scholar citations | arXiv:2603.19418 (SPO) | 0 |
| 54 | Semantic Scholar citations | arXiv:2605.11381 (Kairos) | 0 |
| 55 | Semantic Scholar citations (filtered) | arXiv:1902.05703 (Chinchali offloading) | 5 |
| 56 | Semantic Scholar citations | arXiv:2503.20020 (Gemini Robotics) | 0 (none matched filter) |
| 57 | arXiv API | abs:"remote inference" AND robot | 3 |
| 58 | arXiv API | abs:"split computing" AND (robot OR UAV OR drone) | 4 |
| 59 | arXiv API | abs:"network delay" AND policy AND (manipulation OR VLA) | 0 |
| 60 | WebSearch | Kehoe Patil Abbeel Goldberg survey cloud robotics and automation T-ASE 2015 | 2 |
| 61 | WebSearch | Boston Dynamics Atlas large behavior model inference offboard GPU TPU latency | 0 |
| 62 | WebSearch | NVIDIA GR00T policy server remote inference ZMQ Jetson Thor deployment | 1 |
| 63 | WebSearch | privacy-preserving cloud robot foundation model inference offloading | 1 |
| 64 | arXiv API | abs:offloading AND abs:manipulation AND abs:robot | 1 |
| 65 | arXiv API | abs:cloud AND abs:humanoid AND abs:latency | 1 |
| 66 | arXiv API | abs:"multi-robot" AND inference AND GPU AND server | 0 |
| 67 | WebSearch | Gemini Robotics-ER orchestrator cloud with on-device VLA agentic architecture latency | 1 |
| 68 | WebSearch | cloud VLA robot network jitter robustness benchmark delay injection arXiv 2026 | 0 |
| 69 | WebSearch | OpenVLA deploy REST API server remote inference robot latency | 1 |
| 70 | arXiv API | abs:"fog robotics" | 1 |
| 71 | arXiv API | abs:edge AND abs:VLA AND (collaborative OR offload OR partition) | 0 |
| 72 | WebSearch | inference offloading robot VLA physical AI toolchain Microsoft Kubernetes | 1 |
| 73 | WebSearch | adaptive offloading decision onboard small policy fallback network degrades VLA | 1 |
| 74 | WebSearch | robot fleet learning cloud data upload bandwidth cost large scale deployment | 2 |
| 75 | arXiv API | abs:"edge server" AND abs:robot AND abs:policy | 4 |
| 76 | arXiv API | abs:offloading AND abs:"large language model" AND abs:robot | 0 |
| 77 | arXiv API | abs:serverless AND abs:robot | 0 |
| 78 | arXiv API | abs:cloud AND abs:"diffusion policy" | 0 |
| 79 | arXiv API | abs:asynchronous AND abs:cloud AND abs:robot | 1 |
| 80 | arXiv API | abs:cloud AND abs:onboard AND abs:hierarchical AND abs:robot | 0 |
| 81 | arXiv API | abs:"on-device" AND abs:"vision-language-action" | 1 (others are C2/C5 onboard-compression items) |
| 82 | arXiv API | abs:wireless AND abs:latency AND abs:manipulation | 0 |
| 83 | arXiv API | abs:"inference serving" AND abs:robot | 0 |
| 84 | arXiv API | abs:"cloud-edge" AND abs:embodied | 0 |
| 85 | arXiv API | abs:"device-edge" AND (robot OR embodied) | 1 (low relevance) |
| 86 | arXiv API | abs:fleet AND abs:"foundation model" AND abs:robot | 1 |
| 87 | arXiv API | abs:"multi-robot" AND abs:"vision-language-action" | 1 (low relevance) |
| 88 | arXiv API | abs:remote AND abs:"vision-language-action" AND abs:latency | 0 |
| 89 | arXiv API | abs:"edge computing" AND abs:"vision-language model" AND abs:robot | 0 |
| 90 | arXiv API | abs:split AND abs:"vision-language-action" AND abs:edge | 0 |
| 91 | arXiv API | abs:offload AND abs:humanoid | 0 |
| 92 | WebSearch | hybrid onboard cloud robot policy latency VLA quadruped remote workstation | 0 (session web-search budget exhausted) |
| 93 | WebSearch | robot foundation model inference cost per robot hour cloud GPU pricing fleet | 0 (session web-search budget exhausted) |
| 94 | arXiv API | abs:"remote workstation" AND abs:robot AND abs:policy | 1 (low relevance) |
| 95 | arXiv API | abs:cloud AND abs:quadruped AND abs:"foundation model" | 0 |
| 96 | arXiv API | ti:cloud AND ti:robot | 1 (low relevance; rest pre-2022 generic cloud-robot architectures) |
| 97 | arXiv API | abs:"edge-cloud" AND abs:"large model" AND abs:robot | 0 |

## C7 — Safety under latency and timing variability

115 logged query rows.


| # | source | query | new relevant items |
|---|---|---|---|
| 1 | WebSearch | Physical Intelligence blog real-time action chunking | 2 |
| 2 | WebSearch | safety filter learned policy robot foundation model control barrier function VLA | 4 |
| 3 | WebSearch | SAFE multitask failure detection vision-language-action models arXiv | 2 |
| 4 | WebSearch | FAIL-Detect failure prediction generative robot policies conformal | 3 |
| 5 | WebSearch | Hsu The Safety Filter: A Unified View of Safety-Critical Control survey | 1 |
| 6 | WebSearch | Bidirectional Decoding improving action chunking via closed-loop resampling | 2 |
| 7 | WebSearch | Ames control barrier functions theory and applications seminal | 2 |
| 8 | WebSearch | Changliu Liu safe control learned policy robot safety index | 3 |
| 9 | arXiv API | all:"action chunking" AND all:latency | 14 |
| 10 | OpenAlex | real-time action chunking asynchronous inference | 0 (noisy) |
| 11 | arXiv search | real-time chunking | 8 |
| 12 | arXiv search | "action chunk" asynchronous inference | 20 |
| 13 | arXiv search | "action chunking" inpainting | 1 |
| 14 | arXiv search | "inference delay" robot policy | 5 |
| 15 | arXiv search | "control barrier function" "vision-language-action" | 5 |
| 16 | arXiv search | "safety filter" "vision-language-action" | 5 |
| 17 | arXiv search | "safety filter" "diffusion policy" | 2 |
| 18 | arXiv search | bidirectional decoding action chunking | 2 |
| 19 | arXiv search | temporal ensembling action chunking | 4 |
| 20 | arXiv search | action chunks latency robot | 8 |
| 21 | arXiv search | vision-language-action inference latency delay real-time | 2 |
| 22 | arXiv search | failure detection vision-language-action | 16 |
| 23 | arXiv search | failure prediction generative robot policy | 6 |
| 24 | arXiv search | runtime monitoring robot policy | 6 |
| 25 | arXiv search | out-of-distribution detection robot policy runtime | 3 |
| 26 | arXiv search | conformal prediction robot policy failure | 5 |
| 27 | arXiv search | safe robot foundation models | 6 |
| 28 | arXiv search | "control barrier function" learned policy robot manipulation | 3 |
| 29 | arXiv search | "safety filter" learned policy reinforcement learning robot | 5 |
| 30 | arXiv search | "Towards Safe Robot Foundation Models" | 2 |
| 31 | arXiv search | "latency-aware" control learned policy | 0 |
| 32 | arXiv search | delay compensation reinforcement learning robot | 1 |
| 33 | arXiv search | "worst-case execution time" neural network | 2 |
| 34 | arXiv search | "random delays" reinforcement learning | 4 |
| 35 | arXiv search | "dual-system" "vision-language-action" fast slow asynchronous | 2 |
| 36 | arXiv search | hierarchical VLA slow planner fast controller high-frequency | 0 |
| 37 | arXiv search | "interrupt" action chunk reactive policy | 0 |
| 38 | arXiv search | "open-loop" action chunk reactive closed-loop | 3 |
| 39 | arXiv search | "hamilton-jacobi" reachability learned policy safety filter | 5 |
| 40 | arXiv search | SafeVLA constrained RL VLA safety (long form) | 0 |
| 41 | arXiv search | "action chunk" execution horizon adaptive | 9 |
| 42 | arXiv search | "chunk size" reactivity robot policy | 0 |
| 43 | arXiv search | "streaming" flow policy robot action | 4 |
| 44 | arXiv search | "runtime monitor" generative policy vision-language model | 1 |
| 45 | arXiv search | edge cloud offloading vision-language-action latency | 1 |
| 46 | arXiv search | "network latency" robot policy learned control | 1 |
| 47 | arXiv search | "emergency stop" learned robot policy safety | 2 |
| 48 | arXiv search | "safe-stoppability" humanoid | 0 |
| 49 | arXiv search | "shielding" learned robot policy safety | 6 |
| 50 | arXiv search | "reachability" vision-language-action safety | 2 |
| 51 | arXiv search | "uncertainty" "vision-language-action" calibration | 6 |
| 52 | arXiv search | SafeVLA | 2 |
| 53 | arXiv search | "Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware" | 1 |
| 54 | arXiv search | SmolVLA asynchronous inference | 1 |
| 55 | arXiv search | "Control Barrier Functions: Theory and Applications" | 1 |
| 56 | arXiv search | "Data-driven safety filters" | 2 |
| 57 | arXiv search | "Safe Control with Learned Certificates" | 1 |
| 58 | arXiv search | RoboGuard LLM robot safety guardrails | 1 |
| 59 | arXiv search | "Sentinel" runtime monitoring generative policies | 0 |
| 60 | arXiv search | "safety index" synthesis safe control | 5 |
| 61 | arXiv search | "Real-time" "safe control" learned policy Liu | 0 |
| 62 | arXiv search | "neural control barrier function" robot | 2 |
| 63 | arXiv search | "deadline" robot inference neural network real-time scheduling | 3 |
| 64 | WebFetch | bid-robot.github.io (venue check) | 0 |
| 65 | Semantic Scholar | citations of 2506.07339 (RTC) | 33 |
| 66 | WebSearch | "Simulation for Evaluating Robot Policies Should Be Asynchronous and Real-Time" | 0 |
| 67 | Semantic Scholar | citations of 2506.09937 (SAFE) | 11 |
| 68 | Semantic Scholar | citations of 2510.09459 (FIPER) | 3 |
| 69 | Semantic Scholar | citations of 2503.08558 (FAIL-Detect) | 3 |
| 70 | Semantic Scholar | citations of 2410.04640 (Sentinel) | (pending review) |
| 71 | Semantic Scholar | citations of 2410.04640 (Sentinel) [corrected count] | 8 |
| 72 | Semantic Scholar | references of 2506.07339 (RTC) | 7 |
| 73 | arXiv search | HiRT hierarchical robot transformer asynchronous | 0 |
| 74 | arXiv search | RoboDual generalist specialist | 1 |
| 75 | arXiv search | "fast and slow" robot policy latency | 0 |
| 76 | arXiv search | jitter latency "vision-language-action" | 0 |
| 77 | arXiv search | "timing" robot learned policy inference variability | 0 |
| 78 | arXiv search | "functional safety" learned robot controller certification | 0 |
| 79 | arXiv search | "speed and separation monitoring" learning | 0 |
| 80 | arXiv search | compliant VLA impedance safe contact | 0 |
| 81 | arXiv search | "collision avoidance" "vision-language-action" real-time | 1 |
| 82 | arXiv search | "backup policy" learned robot | 1 |
| 83 | arXiv search | "simplex architecture" learned controller | 2 |
| 84 | arXiv search | "predictive safety filter" learning-based | 5 |
| 85 | arXiv search | Hierarchical Robot Transformers HiRT | 1 |
| 86 | arXiv search | ASIMOV semantic safety robot constitutions | 1 |
| 87 | arXiv search | "Gemini Robotics" | 1 |
| 88 | arXiv search | GR00T N1 humanoid foundation model | 1 |
| 89 | arXiv search | "Hi Robot" hierarchical interactive | 0 |
| 90 | arXiv search | "hierarchical" "vision-language-action" "high-frequency" low-level controller | 0 |
| 91 | arXiv search | "reaction time" robot policy dynamic | 0 |
| 92 | arXiv search | "table tennis" "vision-language-action" | 0 |
| 93 | arXiv search | "latency" "safety" "vision-language-action" | 3 |
| 94 | arXiv search | "action chunk" safety collision | 1 |
| 95 | WebSearch | (3 queries blocked: session web-search budget exhausted) | 0 |
| 96 | arXiv search | "stale observation" robot policy | 0 |
| 97 | arXiv search | "time-to-hazard" robot | 0 |
| 98 | arXiv search | "fail-safe" "vision-language-action" | 0 |
| 99 | arXiv search | rollback recovery "vision-language-action" safe state | 0 |
| 100 | arXiv search | "real-time guarantees" learned robot policy | 0 |
| 101 | arXiv search | "control loop" jitter neural network policy robot | 0 |
| 102 | arXiv search | "inference latency" humanoid whole-body policy | 0 |
| 103 | arXiv search | "asynchronous" "diffusion policy" delay | 1 |
| 104 | arXiv search | "safety" "action chunking" | 4 |
| 105 | arXiv search | "runtime assurance" learning-enabled robot | 1 |
| 106 | Semantic Scholar search | inference latency robot learning policy delay compensation | 0 |
| 107 | Semantic Scholar search | safety filter imitation learning policy manipulation | 0 |
| 108 | Semantic Scholar search | runtime monitoring learned robot controller out-of-distribution | 1 |
| 109 | Semantic Scholar search | hierarchical vision-language-action slow fast asynchronous | 0 |
| 110 | Semantic Scholar search | Hi Robot open-ended instruction following hierarchical VLA | 0 |
| 111 | arXiv search | "Hi Robot" vision-language-action | 0 (found, judged off-scope) |
| 112 | arXiv search | "thinking while acting" robot | 0 |
| 113 | arXiv search | "reactive" "vision-language-action" dynamic objects | 0 |
| 114 | arXiv search | "certified" neural network controller robot runtime | 0 |
| 115 | arXiv search | "out-of-distribution" "safety filter" world model | 0 |

**Saturation:** the last 10 searches (#106-#115) turned up 1 new relevant item (SODA-MPC), which is below the threshold of 2, so the search stopped. Note: the session-wide WebSearch budget ran out partway through, and the remaining searches used the arXiv listing search, the Semantic Scholar API and OpenAlex.

## C8 — Efficient world models for planning and safety monitoring

120 logged query rows.


| # | source | query | new relevant items |
|---|---|---|---|
| 1 | arXiv API | all:"world model" AND (robot OR robotic) AND (efficient OR real-time OR fast) | 18 |
| 2 | Semantic Scholar API | DreamDojo (search) | 0 (429 rate-limited) |
| 3 | arXiv API | all:DreamDojo | 1 |
| 4 | WebSearch | Dyna Robotics DYNA-2 foundation model | 1 |
| 5 | WebSearch | DreamZero world action model robot | 2 |
| 6 | WebSearch | Genie 3 world model DeepMind real-time 24 fps | 2 |
| 7 | WebFetch | dyna.co/research, dyna.co/dyna-2 | 1 |
| 8 | WebFetch | deepmind.google Genie 3 blog | 1 |
| 9 | WebSearch | few-step distilled video world model real-time robot policy action-conditioned | 6 |
| 10 | WebSearch | world model safety monitoring robot failure prediction imagination | 6 |
| 11 | WebSearch | V-JEPA 2-AC zero-shot robot planning latent world model seconds per action | 2 |
| 12 | WebSearch | DriftWorld fast world modeling drifting robot planning rollouts | 1 |
| 13 | WebSearch | latent safety filter world model Hamilton-Jacobi reachability robot manipulation | 4 |
| 14 | WebSearch | world action model inference speedup asynchronous real-time control video diffusion 2026 | 5 |
| 15 | WebSearch | UNISafe uncertainty-aware latent safety filter OOD failures world model | 2 |
| 16 | WebSearch + WebFetch | NVIDIA blog "world-action models" pretrained to imagine fine-tuned to act | 4 |
| 17 | WebSearch | Cosmos-Predict2.5 distilled few-step world model robotics real-time | 3 |
| 18 | WebSearch | Fast-WAM world action model skip video generation at inference | 5 |
| 19 | WebSearch | "World Action Models in Real Time" asynchronous deployment empirical study | 3 |
| 20 | WebSearch | Genie 2 large-scale foundation world model DeepMind blog | 1 |
| 21 | arXiv API | seed titles: DreamZero, DreamerV3, TD-MPC2, V-JEPA 2, Cosmos, Genie, UniSim | 8 |
| 22 | arXiv API | abs:"world action model" AND (real-time OR latency OR efficient OR speedup) | 30 |
| 23 | arXiv API | abs:"world model" AND abs:distillation AND (robot OR manipulation) | 9 |
| 24 | arXiv API | abs:"video world model" AND (few-step OR one-step OR single-step) | 7 |
| 25 | arXiv API | abs:"action-conditioned video" AND robot AND (fast OR real-time OR efficient) | 8 |
| 26 | arXiv API | abs:"latent world model" AND planning AND robot | 8 |
| 27 | arXiv API | abs:JEPA AND (robot OR planning) AND "world model" | 14 |
| 28 | arXiv API | abs:"world model" AND safety AND (filter OR monitor OR reachability) | 9 |
| 29 | arXiv API | abs:"world model" AND failure AND (detection OR prediction) AND robot | 8 |
| 30 | arXiv API | abs:"model predictive" AND "world model" AND "real-time" | 4 |
| 31 | arXiv API | abs:"real-time" AND interactive AND "world model" AND (video generation OR diffusion) | 12 |
| 32 | arXiv API | abs:"video prediction" AND planning AND robot AND "action-conditioned" | 5 |
| 33 | arXiv API | abs:"world model" AND "policy evaluation" AND robot | 8 |
| 34 | arXiv API | abs:"world model" AND "test-time" AND robot AND (planning OR verification) | 5 |
| 35 | arXiv API | abs:"world model" AND "autonomous driving" AND (real-time OR efficient OR latency) | 6 |
| 36 | arXiv API | abs:"world model" AND humanoid AND (real-time OR onboard) | 3 |
| 37 | arXiv API | abs:"TD-MPC" OR abs:"TD-MPC2" | 7 |
| 38 | arXiv API | abs:DreamerV3 AND robot | 3 |
| 39 | arXiv API | abs:"video diffusion" AND policy AND joint AND action AND robot | 5 |
| 40 | arXiv API | abs:"world model" AND token AND (pruning OR compression OR caching) AND video | 6 |
| 41 | arXiv API | abs:"autoregressive video" AND "real-time" AND (self forcing OR causal OR streaming) | 7 |
| 42 | arXiv API (id_list) | 50 IDs surfaced by web searches (seeds + WAM efficiency + safety) | 20 |
| 43 | WebSearch | model-based runtime monitoring latent dynamics failure classifier robot | 3 |
| 44 | WebSearch | DINO-WM zero-shot planning pretrained visual features world model | 1 |
| 45 | WebSearch | 1X world model challenge compression robot video prediction benchmark | 2 |
| 46 | WebSearch | 1X world model blog humanoid policy evaluation | 1 |
| 47 | WebSearch | GAIA-2 Wayve generative world model driving efficient | 2 |
| 48 | WebSearch | Genie Envisioner GE-Sim real-time world model robot efficient inference | 2 |
| 49 | WebSearch | citing "V-JEPA 2" robot planning latent world model faster planning 2026 | 5 |
| 50 | WebSearch | Cosmos Policy video model fine-tuned robot control planning value | 2 |
| 51 | WebSearch | UniPi learning universal policies via text-guided video generation | 1 |
| 52 | Semantic Scholar API | citations of arXiv:2602.15922 (DreamZero), 405 citing papers filtered by efficiency/safety keywords | 20 |
| 53 | WebSearch | NVIDIA DreamGen video world model synthetic robot data | 1 |
| 54 | WebSearch | Genie 3 robotics world model Waymo World Model 2026 | 1 |
| 55 | WebSearch | "Project Genie" OR "Genie 3" technical report arXiv 2026 real-time interactive world model | 3 |
| 56 | arXiv API | abs:"world model" AND planning AND (sampling OR CEM OR MPPI) AND latent AND "real robot" | 2 |
| 57 | arXiv API | abs:"world model" AND out-of-distribution AND safety AND robot | 2 |
| 58 | arXiv API | abs:"world model" AND conformal AND (safety OR safe) | 3 |
| 59 | arXiv API | abs:imagination AND safety AND (robot OR embodied) AND "world model" | 4 |
| 60 | arXiv API | abs:"world model" AND "vision-language-action" AND (RL OR post-training) | 7 |
| 61 | arXiv API | abs:"world model" AND quantization | 4 |
| 62 | arXiv API | abs:"video generation" AND robot AND inference AND (speedup OR accelerat) | 3 |
| 63 | arXiv API | abs:"world model" AND lightweight AND (robot OR embodied OR driving) | 3 |
| 64 | arXiv API | abs:"diffusion world model" AND (RL OR planning) | 3 |
| 65 | WebSearch | DreamerV3 Nature 2025 Hafner | 0 (venue update) |
| 66 | WebSearch | Physical Intelligence world model blog pi 0.7 | 1 |
| 67 | WebSearch | Tesla world simulator neural network FSD Optimus world model talk | 0 (news only) |
| 68 | arXiv API (id_list) | 36 IDs from DreamZero citation snowball + web results | 30 |
| 69 | arXiv API | abs:"interactive video" AND "world model" AND (real-time OR fps) | 4 |
| 70 | arXiv API | abs:"inverse dynamics" AND video AND policy AND (efficient OR fast) | 2 |
| 71 | arXiv API | abs:"world model" AND Jetson | 1 |
| 72 | arXiv API | abs:predictive AND latent AND "world model" AND navigation AND planning | 3 |
| 73 | Semantic Scholar API | citations of arXiv:2310.16828 (TD-MPC2), 500 filtered | 16 |
| 74 | Semantic Scholar API | citations of arXiv:2502.00935 (latent safety filters), 82 filtered | 6 |
| 75 | Semantic Scholar API | citations of arXiv:2505.00779 (UNISafe), 43 filtered | 1 |
| 76 | Semantic Scholar API | citations of arXiv:2506.09985 (V-JEPA 2), 500 filtered | 3 |
| 77 | Semantic Scholar API | citations of arXiv:2602.06949 (DreamDojo), 125 filtered | 1 |
| 78 | Semantic Scholar API | citations of arXiv:2603.16666 (Fast-WAM), 286 filtered | 7 |
| 79 | Semantic Scholar API | references of arXiv:2607.15065 (DriftWorld) | 0 (only generic distillation refs) |
| 80 | arXiv API (id_list) | 38 IDs from Semantic Scholar snowball | 33 |
| 81 | arXiv API | abs:"world model" AND "inference latency" AND robot | 2 |
| 82 | arXiv API | abs:"world action model" AND (distill OR caching OR quantiz) | 2 |
| 83 | arXiv API | abs:"latent safety" AND "world model" | 0 |
| 84 | arXiv API | abs:"world model" AND "runtime monitor" | 0 |
| 85 | arXiv API | abs:"video world model" AND "real-time" AND robot | 0 |
| 86 | arXiv API | abs:"world model" AND "edge device" | 1 |
| 87 | arXiv API | abs:JEPA AND planning AND efficient | 2 |
| 88 | arXiv API | abs:"imagined rollouts" AND safety AND robot | 0 |
| 89 | arXiv API | abs:"action-conditioned world model" AND speed | 0 |
| 90 | arXiv API | abs:"world model" AND "model predictive control" AND GPU AND robot | 0 |
| 91 | arXiv API | abs:"world model" AND one-step AND (robot OR navigation OR manipulation) | 2 |
| 92 | arXiv API | abs:"world model" AND real-time AND planning AND latent | 1 |
| 93 | arXiv API | abs:"world model" AND failure AND conformal | 0 |
| 94 | arXiv API | abs:"world action model" AND memory AND efficient | 0 |
| 95 | arXiv API | abs:"world model" AND token AND compact AND planning | 0 |
| 96 | arXiv API | abs:"video world model" AND distillation AND causal | 2 |
| 97 | arXiv API | abs:"world model" AND onboard AND (drone OR quadruped OR humanoid) | 1 |
| 98 | arXiv API | abs:"world model" AND hazard AND (robot OR embodied) | 0 |
| 99 | arXiv API | abs:"world action model" AND humanoid AND real-time | 0 |
| 100 | arXiv API | abs:"safety filter" AND latent AND vision | 0 |
| 101 | arXiv API | abs:"world model" AND speedup AND planning | 2 |
| 102 | arXiv API | abs:"world action model" AND latency AND Hz | 0 |
| 103 | arXiv API | abs:"latent world model" AND safety | 0 |
| 104 | arXiv API | abs:"video prediction" AND failure AND robot AND monitor | 0 |
| 105 | arXiv API | abs:"world model" AND pruning | 0 |
| 106 | arXiv API | abs:dreamer AND "real robot" AND onboard | 0 |
| 107 | arXiv API | abs:"world model" AND distilled AND policy AND deployment | 1 |
| 108 | arXiv API | abs:"autoregressive world model" AND "KV cache" AND robot | 0 |
| 109 | arXiv API | abs:model-based AND safety AND imagination AND latent | 1 |
| 110 | arXiv API | abs:"world-action" AND efficient | 2 |
| 111 | arXiv API | abs:"world model" AND "adaptive computation" AND robot | 0 |
| 112 | arXiv API | abs:imagination AND latency AND robot | 0 |
| 113 | arXiv API | abs:"learned simulator" AND real-time AND robot | 0 |
| 114 | arXiv API | abs:"predictive model" AND "failure prediction" AND manipulation | 0 |
| 115 | arXiv API | abs:"world model" AND "consistency model" AND robot | 0 |
| 116 | arXiv API | abs:"world model" AND "flow matching" AND "one step" AND planning | 0 |
| 117 | arXiv API | abs:"diffusion forcing" AND robot AND planning | 0 |
| 118 | arXiv API | abs:"world model" AND "test-time scaling" AND VLA | 1 |
| 119 | arXiv API | abs:"neural simulator" AND robot AND fast | 0 |
| 120 | arXiv API | abs:"world model" AND certified AND safe AND control | 0 |

Saturation: the final 10 searches (#111-#120) surfaced 1 new relevant item.
Note: "new relevant items" counts for rows 1-67 are approximate tallies of relevant items first surfaced by that query (many were later recorded after abstract review).

## C9 — People, venues and blogs

80 logged query rows.

| # | source | query | new relevant items |
|---|---|---|---|
| 1 | workshop site | https://efficient-embodied-ai.github.io/ (CFP, speakers, organizers) | 1 (workshop CFP record) |
| 2 | OpenReview API | notes?content.venueid=robot-learning.org/CoRL/2026/Workshop/EEAI | 0 (403 challenge) |
| 3 | OpenReview API | notes?invitation=.../EEAI/-/Submission | 0 (403 challenge) |
| 4 | OpenReview API | groups?id=.../EEAI (public_submissions=false) | 0 |
| 5 | OpenReview API | invitations?id=.../EEAI/-/Submission | 0 |
| 6 | Semantic Scholar | author/search Jiajun Wu, Yecheng Jason Ma, Dhruv Shah, Ouais Alsharif, Jiafan Yu, Changliu Liu, Zhuoyang Zhang (ID resolution) | 0 |
| 7 | WebSearch | Dyna Robotics DYNA-1 blog foundation model real-world performance | 1 |
| 8 | WebSearch | Zhuoyang Zhang MIT Han Lab VLA efficient 2025 | 4 (leads) |
| 9 | WebSearch | Ouais Alsharif Google DeepMind robotics Gemini Robotics On-Device | 2 |
| 10 | WebSearch | Jiafan Yu Google robotics paper 2025 | 0 |
| 11 | Semantic Scholar | author/2322628540/papers (Dhruv Shah) | 14 |
| 12 | Semantic Scholar | author/3045089/papers (Jiajun Wu, first 100) | 0 (older) |
| 13 | Semantic Scholar | author/2130215451/papers (Yecheng Jason Ma) | 0 |
| 14 | Semantic Scholar | author/2511744/papers (Ouais Alsharif) | 0 (pre-2021 only) |
| 15 | Semantic Scholar | author/143954008/papers (Jiafan Yu) | 0 (energy systems, pre-2019) |
| 16 | WebFetch | arxiv.org/html/2503.20020 (Gemini Robotics latency) | 1 |
| 17 | Semantic Scholar | author/search Jiajun Wu (hIndex filter) + author/2326444500/papers | 7 |
| 18 | Semantic Scholar | paper/batch (17 Wu candidates) | 7 |
| 19 | WebFetch | arxiv 2603.05449 RealWonder / 2606.12402 DIRECT | 2 |
| 20 | WebSearch | Changliu Liu CMU 2025 arXiv vision-language-action safety real-time | 6 (leads) |
| 21 | WebSearch | Changliu Liu Intelligent Control Lab 2026 humanoid safe control VLA arXiv | 4 |
| 22 | WebFetch | alphaxiv @zhuoyang-zhang | 6 |
| 23 | Semantic Scholar | paper/batch (Zhang/Liu/related 17) | 8 |
| 24 | WebFetch | icontrol.ri.cmu.edu/research/humanoid.html + /publication | 10 |
| 25 | Semantic Scholar | search/match (6 Liu titles) | 5 |
| 26 | WebSearch | SafeDec constrained decoding safe autoregressive generalist robot policies | 1 |
| 27 | WebFetch | dyna.co/research (index) | 5 |
| 28 | WebFetch | dyna.co/dyna-2, /research/dyna-1, /dyna-2.1 | 3 |
| 29 | WebFetch | dyna.co/research/pre-training, /research/dyna-2-infrastructure | 2 |
| 30 | WebFetch | pi.website/research (429) | 0 |
| 31 | WebSearch | pi.website research real-time chunking action chunking latency Physical Intelligence blog | 3 |
| 32 | WebSearch | Physical Intelligence blog 2026 pi research post inference speed | 2 |
| 33 | WebFetch | pi.website/blog (429); modal.com PI remote inference blog | 1 |
| 34 | Semantic Scholar | paper/batch (9 PI papers) | 9 |
| 35 | WebFetch | arxiv html 2410.24164 (pi0 timing table); abs 2512.05964 | 2 |
| 36 | WebSearch | NVIDIA GR00T N1.6 Jetson Thor inference latency TensorRT blog | 3 |
| 37 | WebSearch | NVIDIA developer blog GR00T N1.5 deploy Jetson Orin quantization VLA | 1 |
| 38 | WebFetch | Isaac-GR00T deployment README; NVIDIA forum FlashRT; Jetson edge AI blog | 3 |
| 39 | WebFetch | arxiv html 2503.14734 (GR00T N1); Jetson Thor blog | 2 |
| 40 | WebFetch | figure.ai/news/helix | 1 |
| 41 | WebSearch | Hugging Face blog SmolVLA async inference LeRobot | 2 |
| 42 | WebSearch | 1X world model Redwood AI blog onboard NEO technical | 1 |
| 43 | WebFetch | 1x.tech redwood-ai; HF blog async-robot-inference; HF papers 2506.01844 | 3 |
| 44 | WebSearch | 1X world model blog action-conditioned video evaluation 2025 | 2 |
| 45 | WebSearch | AWS Neuron Trainium Inferentia robotics VLA policy inference blog | 0 |
| 46 | WebSearch | Figure AI Helix blog 2025 2026 technical post System 0 logistics speed | 1 |
| 47 | WebFetch | figure.ai/news/helix-logistics; figure.ai/news/helix-02; 1x.tech world-model-self-learning | 3 |
| 48 | WebSearch | Figure Helix 02 System 0 whole-body controller blog | 1 |
| 49 | WebSearch | SARA-RT self-adaptive robust attention Google DeepMind blog | 2 |
| 50 | WebSearch | AWS Trainium robot foundation model training OpenVLA pi0 Neuron SDK robotics case study | 1 |
| 51 | WebSearch | Toyota Research Institute large behavior model blog diffusion policy 2025 | 2 |
| 52 | WebFetch | AWS physical-ai blog pi0 fine-tuning; Boston Dynamics LBM blog | 2 |
| 53 | Semantic Scholar | paper/batch (10 seed papers: SARA-RT, LBM, RT-1/2, OpenVLA, OFT, RDT, DexVLA, PD-VLA, OpenHelix) | 7 |
| 54 | OpenReview API | groups?parent=robot-learning.org/CoRL/2025/Workshop (16 workshops; Eval-Deploy public_submissions=false) | 0 |
| 55 | OpenReview web | openreview.net/group?id=.../EEAI (JS-rendered, no submissions visible) | 0 |
| 56 | Semantic Scholar | search "efficient vision-language-action model inference real-time" venue=CoRL 2025-2026 | 0 |
| 57 | Semantic Scholar | search "vision-language-action real-time inference latency" 2025-2026 | 31 |
| 58 | Semantic Scholar | search "efficient world model real-time planning robot manipulation" 2025-2026 | 14 |
| 59 | WebFetch | bair.berkeley.edu/blog (index) | 1 |
| 60 | WebFetch | ai.stanford.edu/blog (index) | 2 |
| 61 | WebFetch | BAIR GRASP post; SAIL R&B-EnCoRe post; SAIL ICML 2026 list | 7 |
| 62 | Semantic Scholar | paper/batch (4 blog-linked papers) | 4 |
| 63 | WebFetch | huggingface.co/blog/smolvla; huggingface.co/blog/pi0 | 2 |
| 64 | arXiv API | abs:"vision-language-action" AND (abs:quantization OR abs:quantized) | 26 |
| 65 | arXiv API | abs:robot AND cloud AND edge AND (policy OR VLA OR foundation model) | 12 |
| 66 | arXiv API | abs:"world model" AND safety AND (real-time OR monitor) AND robot | 1 |
| 67 | arXiv API | abs:"vision-language-action" AND (safety filter OR control barrier OR fallback OR runtime monitor) | 10 |
| 68 | arXiv API | au:"Ouais Alsharif" (sorted by date) | 0 (latest 2020) |
| 69 | arXiv API | au:"Jiafan Yu" | 0 (energy systems only) |
| 70 | arXiv API | au:"Yecheng Jason Ma" | 1 |
| 71 | arXiv API | au:"Zhuoyang Zhang" | 2 |
| 72 | arXiv API | au:"Dhruv Shah" AND cat:cs.RO (by date) | 3 |
| 73 | arXiv API | au:"Changliu Liu" (by date) | 3 |
| 74 | arXiv API | au:"Jiajun Wu" AND cat:cs.RO (by date) | 3 |
| 75 | arXiv API | abs:robot AND (Trainium OR Inferentia OR NPU OR TPU) AND policy | 1 |
| 76 | arXiv API | abs:"vision-language-action" AND (mixture-of-experts OR early exit) | 7 |
| 77 | arXiv API | abs:"world action model" AND (efficient OR real-time OR latency) | 21 |
| 78 | arXiv API | abs:"vision-language-action" AND abs:Jetson | 10 |
| 79 | arXiv API | abs:"vision-language-action" AND benchmark AND latency AND hardware | 3 |
| 80 | arXiv API | ti:"real-time" AND abs:"vision-language-action" AND abs:humanoid | 2 |

## GAP_A — gap check (composability, TCO, cross-hardware evaluation, OpenVLA on 16 GB Jetson)

126 logged query rows.


| # | source | query | new relevant items |
|---|---|---|---|
| 1 | arXiv API | abs:OpenVLA AND abs:quantization | 0 |
| 2 | arXiv API | abs:OpenVLA AND abs:Jetson | 0 |
| 3 | arXiv API | abs:"vision-language-action" AND abs:Orin | 1 (2510.19430) |
| 4 | arXiv API | abs:OpenVLA AND abs:"4-bit" | 0 |
| 5 | arXiv API | abs:OpenVLA AND abs:memory AND abs:edge | 1 (2606.02775) |
| 6 | arXiv API | abs:"vision-language-action" AND abs:"memory footprint" | 0 |
| 7 | arXiv API | abs:VLA AND abs:Jetson | 0 |
| 8 | arXiv API | abs:"vision-language-action" AND abs:"llama.cpp" | 0 |
| 9 | arXiv API | abs:"vision-language-action" AND abs:TensorRT | 0 |
| 10 | arXiv API | abs:"vision-language-action" AND abs:"8-bit" | 0 |
| 11 | arXiv API | abs:"vision-language-action" AND abs:onboard AND abs:"GPU memory" | 0 |
| 12 | arXiv API | abs:OpenVLA AND abs:"inference speed" | 0 |
| 13 | arXiv API | abs:"vision-language-action" AND abs:INT4 | 0 |
| 14 | arXiv API | abs:"vision-language-action" AND abs:embedded | 0 (noise: 'embedding') |
| 15 | GitHub issues API | repo:openvla/openvla jetson | 0 (PR #318 has only projected numbers; not recorded) |
| 16 | GitHub issues API | repo:openvla/openvla quantization | 3 (issue #324; vla-lite via #311; #152/#57) |
| 17 | GitHub issues API | repo:openvla/openvla 4-bit | 1 (issue #66) |
| 18 | GitHub issues API | repo:openvla/openvla memory GPU | 0 |
| 19 | GitHub issues API | repo:moojink/openvla-oft jetson | 0 |
| 20 | GitHub issues API | repo:Physical-Intelligence/openpi jetson | 1 (issue #386) |
| 21 | GitHub issues API | repo:Physical-Intelligence/openpi orin | 0 |
| 22 | arXiv API | abs:"vision-language-action" AND abs:orthogonal AND abs:acceleration | 0 |
| 23 | arXiv API | abs:"vision-language-action" AND abs:complementary AND abs:quantization | 0 |
| 24 | arXiv API | abs:"vision-language-action" AND abs:pruning AND abs:quantization | 0 (all existing) |
| 25 | arXiv API | abs:VLA AND abs:"token pruning" AND abs:caching | 0 |
| 26 | arXiv API | abs:"vision-language-action" AND abs:"speculative decoding" | 0 (driving-only hits not recorded) |
| 27 | arXiv API | abs:VLA AND abs:distillation AND abs:quantization | 0 |
| 28 | arXiv API | ti:"interplay between sparsity and quantization" | 1 (2405.20935) |
| 29 | arXiv API | abs:"speculative decoding" AND abs:quantization AND abs:compatibility | 1 (2602.21233) |
| 30 | arXiv API | ti:"joint sparsification and quantization" | 0 |
| 31 | arXiv API | abs:"large language model" AND abs:pruning AND abs:quantization AND abs:orthogonal AND abs:combined | 0 |
| 32 | arXiv API | abs:"token merging" AND abs:quantization AND abs:"vision transformer" | 0 |
| 33 | arXiv API | ti:"compressing LLMs" AND ti:truth | 1 (2310.01382) |
| 34 | arXiv API | abs:"vision-language-action" AND abs:"compatible with" AND abs:quantization | 0 |
| 35 | arXiv API | abs:VLA AND abs:"combined with" AND abs:acceleration | 1 (2509.05614) |
| 36 | arXiv API | abs:"vision-language-action" AND abs:"system-level" AND abs:optimizations | 1 (2605.03269) |
| 37 | arXiv API | abs:"diffusion policy" AND abs:quantization AND abs:distillation | 0 |
| 38 | arXiv API | abs:"vision-language-action" AND abs:"end-to-end" AND abs:speedup AND abs:Orin | 0 |
| 39 | arXiv API | abs:"vision-language-action" AND abs:"inference engine" | 0 |
| 40 | arXiv API | abs:"vision-language-action" AND abs:"CUDA graph" | 0 |
| 41 | arXiv API (id_list) | known foundational composition/benchmark works: 1510.00149, 2505.22179, 2410.11305, 2106.07597, 2012.02328, 2410.12032 | 6 |
| 42 | arXiv API | abs:robot AND abs:fleet AND abs:inference AND abs:cost | 0 |
| 43 | arXiv API | abs:"robot policy" AND abs:serving AND abs:batch | 0 |
| 44 | arXiv API | abs:humanoid AND abs:"power consumption" AND abs:onboard AND abs:compute | 0 |
| 45 | arXiv API | abs:"total cost of ownership" AND abs:edge AND abs:cloud AND abs:inference | 0 |
| 46 | arXiv API | abs:robot AND abs:"cloud GPU" AND abs:cost | 1 (2108.01235) |
| 47 | arXiv API | abs:edge AND abs:cloud AND abs:cost AND abs:"LLM inference" AND abs:energy | 0 (general LLM hits not recorded) |
| 48 | arXiv API | ti:"data centers on wheels" | 0 |
| 49 | arXiv API | abs:"autonomous vehicles" AND abs:computing AND abs:emissions AND abs:onboard | 0 |
| 50 | arXiv API | abs:"mobile robot" AND abs:energy AND abs:computation AND abs:locomotion AND abs:breakdown | 0 |
| 51 | arXiv API | abs:robot AND abs:offloading AND abs:"monetary cost" | 0 |
| 52 | arXiv API | abs:"embodied AI" AND abs:"inference cost" AND abs:deployment | 0 |
| 53 | arXiv API | abs:"vision-language-action" AND abs:cost AND abs:cloud AND abs:onboard | 0 (existing) |
| 54 | OpenAlex (fulltext) | robot fleet cloud inference cost | 0 (noisy) |
| 55 | OpenAlex (title+abstract) | autonomous vehicle computing energy emissions onboard | 0 |
| 56 | OpenAlex (title+abstract) | humanoid robot battery power compute | 1 (10.1109/ecti-con64996.2025.11100596) |
| 57 | OpenAlex (title+abstract) | edge versus cloud inference cost comparison | 0 |
| 58 | OpenAlex (title+abstract) | robot inference serving cost GPU | 0 (2609.12075 existing) |
| 59 | arXiv API | ti:wheels AND ti:emissions | 0 |
| 60 | arXiv API | ti:"autonomous driving" AND ti:architectural AND ti:implications | 0 |
| 61 | arXiv API | abs:"mobile robot" AND abs:"energy consumption" AND abs:computing AND abs:GPU | 0 |
| 62 | arXiv API | abs:"cloud robotics" AND abs:cost AND abs:"cloud instance" | 0 |
| 63 | arXiv API | abs:LLM AND abs:inference AND abs:"cost per" AND abs:edge AND abs:device | 0 |
| 64 | OpenAlex (title+abstract) | data centers on wheels | 1 (10.1109/mm.2022.3219803) |
| 65 | OpenAlex (title+abstract) | architectural implications of autonomous driving | 1 (10.1145/3173162.3173191) |
| 66 | OpenAlex (title+abstract) | energy consumption computing mobile robots | 2 (IROS 2021 DVFS+motor; Lambrecht 2019, unverified) |
| 67 | OpenAlex (title+abstract) | power budget onboard computer legged robot | 0 |
| 68 | arXiv API | abs:"vision-language-action" AND abs:serving | 1 (2606.12688) |
| 69 | arXiv API | abs:"multiple robots" AND abs:GPU AND abs:inference AND abs:policy | 0 |
| 70 | arXiv API | abs:"physical AI" AND abs:inference AND abs:cost | 0 |
| 71 | arXiv API | abs:robot AND abs:"cost-effective" AND abs:"foundation model" AND abs:deployment AND abs:cloud | 0 |
| 72 | arXiv API | abs:humanoid AND abs:energy AND abs:"onboard computer" | 0 |
| 73 | arXiv API | abs:"total cost of ownership" AND abs:inference | 2 (2502.01070, 2509.02596) |
| 74 | arXiv API | abs:"total cost of ownership" AND abs:edge | 0 |
| 75 | arXiv API | abs:"cost per token" AND abs:edge AND abs:cloud | 0 |
| 76 | arXiv API | abs:on-device AND abs:cloud AND abs:LLM AND abs:economic | 0 |
| 77 | arXiv API | abs:roofline AND abs:Jetson | 2 (2509.20189, 2609.10550) |
| 78 | arXiv API | abs:roofline AND abs:"vision-language-action" | 0 (existing) |
| 79 | arXiv API | abs:roofline AND abs:robot | 1 (2606.26383) |
| 80 | arXiv API | abs:"vision-language" AND abs:Jetson AND abs:benchmark AND abs:energy | 0 |
| 81 | arXiv API | abs:"large language model" AND abs:Jetson AND abs:benchmark | 2 (2609.08307, 2403.12844) |
| 82 | arXiv API | abs:"tail latency" AND abs:robot AND abs:policy | 0 |
| 83 | arXiv API | abs:"energy per inference" AND abs:edge | 1 (2604.17040) |
| 84 | arXiv API | ti:RobotPerf | 1 (2309.09212) |
| 85 | arXiv API | abs:robotics AND abs:benchmark AND abs:"hardware acceleration" AND abs:ROS | 0 |
| 86 | arXiv API | abs:MLPerf AND abs:edge AND abs:"language model" | 0 |
| 87 | arXiv API | abs:"vision-language-action" AND abs:latency AND abs:jitter | 0 |
| 88 | arXiv API | abs:"vision-language-action" AND abs:"workload characterization" | 0 |
| 89 | arXiv API | abs:embodied AND abs:"workload characterization" | 0 |
| 90 | arXiv API | abs:MLPerf AND abs:Jetson | 0 |
| 91 | arXiv API | abs:MLPerf AND abs:methodology AND abs:latency AND abs:percentile | 0 |
| 92 | arXiv API | abs:"power measurement" AND abs:Jetson AND abs:"deep learning" AND abs:accuracy | 0 |
| 93 | arXiv API | abs:benchmarking AND abs:"edge AI" AND abs:Jetson AND abs:NPU | 0 |
| 94 | arXiv API | abs:"hardware-agnostic" AND abs:efficiency AND abs:metric AND abs:inference | 1 (2602.06069) |
| 95 | arXiv API | abs:deadline AND abs:"vision-language-action" | 0 |
| 96 | arXiv API | abs:"worst-case" AND abs:latency AND abs:"robot policy" | 0 |
| 97 | arXiv API | abs:"energy efficiency" AND abs:"vision-language-action" AND abs:"per action" | 0 |
| 98 | arXiv API | abs:"speed-of-light" AND abs:inference AND abs:robot | 0 |
| 99 | arXiv API | abs:deadline AND abs:VLA AND abs:robot | 0 |
| 100 | arXiv API | abs:p99 AND abs:robot AND abs:latency | 0 |
| 101 | arXiv API | abs:"latency distribution" AND abs:robot AND abs:inference | 0 |
| 102 | arXiv API | abs:"action chunking" AND abs:quantization | 0 (VQ tokenizers, off-topic) |
| 103 | arXiv API | abs:"diffusion policy" AND abs:quantization | 0 |
| 104 | arXiv API | abs:"vision-language-action" AND abs:stacking | 0 (block-stacking noise) |
| 105 | arXiv API | abs:"visual token" AND abs:quantization AND abs:"vision-language model" AND abs:joint | 0 |
| 106 | arXiv API | abs:"Orin NX" AND abs:policy | 0 |
| 107 | arXiv API | abs:"Orin Nano" AND abs:policy AND abs:robot | 0 |
| 108 | arXiv API | abs:"AGX Orin" AND abs:"vision-language" AND abs:robot | 0 (2510.19430 already counted) |
| 109 | arXiv API | abs:"Jetson Thor" | 0 |
| 110 | arXiv API | abs:7B AND abs:VLA AND abs:"edge device" | 0 |
| 111 | Web (jetson-ai-lab.com + Wayback Machine) | jetson-ai-lab.com/benchmarks.html; /openvla.html (archived 2024) | 1 (jetson-ai-lab-openvla-tutorial) |
| 112 | GitHub code search | openvla repo:NVIDIA-AI-IOT/jetson-generative-ai-playground | 0 (auth required) |
| 113 | Hugging Face model API | openvla awq | 0 |
| 114 | Hugging Face model API | openvla gguf | 0 (vla.cpp GGUFs; engine already in DB as 2606.08094) |
| 115 | Hugging Face model API | openvla int4 | 0 |
| 116 | Hugging Face model API | openvla 4bit | 0 (GPTQ checkpoints without model cards) |
| 117 | Hugging Face model API | openvla gptq | 0 |
| 118 | Hugging Face model API | openvla fp8 | 0 |
| 119 | Hugging Face model API | openvla onnx | 0 |
| 120 | Hugging Face model API | openvla trt | 0 |
| 121 | GitHub repo search | openvla+jetson | 1 (Omega1029/openvla-oft-quantization) |
| 122 | GitHub repo search | openvla+orin | 0 |
| 123 | GitHub repo search | vla+jetson+orin+quantization | 0 |
| 124 | GitHub repo search | openvla+tensorrt | 1 (rail-berkeley/tensorrt-openvla) |
| 125 | GitHub repo search | openvla+quantization | 2 (RadixQuantVLA, openvla-serve) |
| 126 | GitHub (direct) | VinRobotics/vla.cpp docs/benchmark (jetson-agx-orin, jetson-orin-nano, libero) | 0 (evidence attached to existing 2606.08094 in findings) |

## GAP_B — gap check (chunk interruption/certification) + 2026 recency sweep

63 logged query rows.


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

## R2 — Round-2 citation snowball (programmatic)

- Seeds: every round-1 item with relevance ≥ 4 and an arXiv ID (571 papers).
- Source: Semantic Scholar Graph API `POST /paper/batch` with nested `citations` and `references` (29 batch calls of 20 papers, sequential, with back-off), because per-agent API calls had been rate-limited in round 1.
- Candidate pool: 37038 papers not already in the database; kept those linked to ≥ 4 core items, from 2022+ (or ≥ 12 links if older), whose titles matched an embodied/efficiency keyword filter → 2574 candidates; abstracts fetched in bulk for 2485.
- Triage: six subagents read every candidate abstract and recorded in-scope items.

### SB_1


- Candidates read: 429
- Recorded: 132
- Skipped: 297
- Count by relevance: 5 -> 1, 4 -> 15, 3 -> 45, 2 -> 71
- Foundational techniques (foundational_technique=true): 7 (DMD2, OmniQuant, KVQuant, Sarathi-Serve, LayerSkip, OPTQ/GPTQ, Diff-Instruct)
- Unverified (no abstract, recorded on title): 5 (Open X-Embodiment, Diffusion-VLA, pi*0.6, HybridFlow, OPTQ)

What got skipped: generic surveys, VLA papers about capability or robustness only with links < 10, attack/security papers, data-collection hardware, and navigation/humanoid work with no efficiency angle.

##### Notable finds
- 2506.08822 FreqPolicy: frequency-consistency one-step flow policy, 93.5 Hz real-world inference, also plugged into a VLA on LIBERO.
- 2606.11187 Next Forcing: multi-chunk prediction for world-action models, 2x inference speedup and 2.3x faster convergence.
- 2603.20658 Speedup Patch: plug-and-play chunk-downsampling scheduler learned offline, 1.8x execution speedup.
- 2607.29482 Temporal Policy: history-initialized transport, 19.1 ms inference on an RTX 4080.
- 2510.07865 DM1: one-step MeanFlow policy, 0.07 s vs 2-3.5 s inference.
- 2607.06262 OTQL: RL post-training that cuts flow-policy/VLA sampling steps by 70%.
- 2608.16503 NebulaVLA: asynchronous dual-frequency VLA, ~2.7x faster action generation.
- 2607.06678 NativeMEM: one-token-per-frame native memory compression for VLAs with negligible latency overhead.
- 2604.24391 FreqCache: frequency-guided token caching for VLN models, 1.59x speedup.
- 2606.25473 Causal-rCM: autoregressive diffusion distillation (1-2 steps) for interactive world models incl. Cosmos.

### SB_2


- Candidates read: 429
- Recorded: 97
- Skipped: 332 (generic VLA/WAM method papers without an efficiency angle and <10 core links, robot attacks/security, LLM agents/planners, driving/traffic work without robot angle, datasets/benchmarks below link threshold)
- By relevance: 5 = 8, 4 = 18, 3 = 45, 2 = 26
- Foundational techniques: 6 (DMD, DivPrune, KIVI, QServe, FLAP, LongLive)
- Unverified (no abstract, title-only): 3 (Open X-Embodiment, RLinf-VLA, pi*0.6)

##### Notable finds
- MoDeVLA (10.1145/3770855.3817651): mixture-of-depth VLA; ~38% latency and 86% FLOPs reduction on Jetson Orin, real robot.
- 2609.28811 DeltaWAM: delta-prediction WAM with streaming cached memory; 36.57% lower one-step latency vs Fast-WAM.
- 2606.02775 AURA-Mem: constant-VRAM gated memory for VLAs aimed at edge memory-write limits (4,224-byte state).
- 2507.10543 MP1: MeanFlow 1-NFE point-cloud policy, 6.8 ms inference, 19x faster than DP3.
- 2503.00339 Falcon: training-free partial-denoising reuse, 2-7x diffusion-policy speedup.
- 2602.02396 PRISM: single-pass IMLE + Performer policy at 30-50 Hz closed-loop control.
- 2609.18732 PASSAGE: fully onboard humanoid flow-matching planner (6.25 Hz) + 50 Hz tracker on Jetson AGX Orin, with real-time chunking.
- 2602.19260 The Price Is Not Right: energy comparison of pi0 vs neuro-symbolic planner (~100x training energy).
- 2508.10259 AMS: OS-level primitives for VLA action management, 29-74% execution time saved.
- 10.1109/CCWC67433.2026.11393726: survey of on-device SLM inference acceleration for real-time robotics.

### SB_3


- Candidates read: 429 (all lines of shards/shard3.jsonl)
- Recorded: 124
- Skipped: 305 (includes 2 duplicates: `10.48550/arXiv.2503.01238` merged into 2503.01238; `10.48550/arXiv.2412.04445` duplicate of 2412.04445)

##### Count by relevance
| relevance | count |
|---|---|
| 5 | 2 |
| 4 | 13 |
| 3 | 81 (incl. 10 foundational_technique=true) |
| 2 (context, links >= 10) | 28 |

- verified=false (no abstract): 2 (2408.17355 Bidirectional Decoding; 2206.09557 nuQmm)

##### Notable finds
- 2606.07383 RhinoVLA: VLA co-designed with an edge SoC (Huixi R1); 11.69 Hz end-to-end on-device via token-efficient backbone, compilation, mixed precision.
- 2609.24840 PredActor (humanoid diffusion policy): 16.79 ms median / 19.38 ms p95 callback on Jetson Orin NX, under the 20 ms control period, deployed on Unitree G1.
- 2605.29438 ElegantVLA: training-free phase-adaptive compute reuse; real GR00T tasks go from 13.8 Hz to 26.3 Hz.
- 2605.29766 MARS Policy: invokes stochastic generation only when needed; 83.2% real-world inference-latency reduction.
- 2606.16253 SPARC (Learned Image Compression for VLAs): task-aware bitrate allocation for bandwidth-limited or remote VLA deployment (C6).
- 2604.04913 DeltaTok/DeltaWorld ("A Frame is Worth One Token"): one token per frame; 35x fewer params and 2,000x fewer FLOPs than prior generative world models.
- 2605.01581 Hyper-DP3: pocket-scale 3D diffusion policy, two-step DDIM, <1% of prior 3D-DP parameters.
- 2608.26673 PredVLA: 0.68M-parameter predictive-coding policy competitive on LIBERO.
- 2509.24527 Dreamer 4 (Training Agents Inside of Scalable World Models): real-time world model on a single GPU via shortcut forcing.
- 2512.17661 Vidarc: cached autoregressive video diffusion for closed-loop control with a 91% latency reduction.

### SB_4


- Candidates read: 429 (every line of shards/shard4.jsonl; abstracts checked in full for borderline items)
- Recorded: 123
- Skipped: 306. These were mostly generic VLA method papers with no efficiency angle and fewer than 10 links, plus surveys, datasets or teleop systems under the link threshold, unrelated robotics, and PPO (a generic RL algorithm, not an efficiency technique).
- Unverified (no abstract, recorded from title): 5 (piRL, AWQ, DEFLECT, VLA-Cache, sample-efficient dexterous fine-tuning)

##### Count by relevance
| relevance | count |
|---|---|
| 5 | 4 |
| 4 | 20 |
| 3 | 56 |
| 2 (context, links >= 10) | 28 |
| 2 (foundational_technique = true) | 15 |

##### Notable finds
- 2609.10915 IMLE-VLA: one-step cIMLE action head for pi0.5, 55 Hz vs 15 Hz inference, 3.9-6.6x lower per-episode inference time.
- 2609.36967 Beyond Token Importance (GeoScaffold): training-free spatial-scaffold visual token pruning for pi0.5, 1.78x prefill speedup at 20% of tokens.
- 2604.03540 Drift-Based Policy Optimization: native 1-NFE generative policy (100 -> 1 NFE), 9.5 ms end-to-end on a dual-arm UR5.
- 2609.36413 RoboActualizer (One from Infinity): ~60M trainable actualizer on a frozen video world model, 39 ms latency, up to 100x fewer trainable params.
- 2512.09101 Masked Generative Policy: parallel masked action-token generation, up to 35x lower inference time.
- 2603.23149 Describe-Then-Act (DILLO): distilled language-action world model for safety steering, 14x faster than visual simulation.
- 10.1109/ISoIRS70157.2026.11545245 Cross-SSM (State-Space Modeling for Action Generation): cache-free linear-time action expert for on-device VLAs.
- 2606.23444 SkyJEPA: JEPA latent world model plus sampling-based control running real-time on embedded quadrotor hardware.
- 2607.02646 EVA-Client: open deployment framework unifying sync/async inference, temporal ensembling and Real-Time Chunking.
- 2606.06049 L-SDPPO: spiking diffusion policy for low-energy manipulation on power-limited spacecraft robots.

### SB_5


- Candidates read: 429
- Recorded: 119 (in raw2/SB_5.jsonl)
- Skipped: 310. This includes 1 duplicate: candidate 171 (DA-SIP, NeurIPS entry with no arXiv ID) was merged into 2511.20906.
- By relevance: 5 -> 5, 4 -> 29, 3 -> 58, 2 (context, links >= 10) -> 27
- foundational_technique=true: 6 (QuIP#, DuQuant, Q-Diffusion, OstQuant, AAPT, MuE early exit)
- verified=false (no abstract, title clearly in scope): 5 (OxyGen, Enfold, VLA-Pruner, action-caching acceleration, RoboCat)

Skip policy: VLA or WAM method papers with no efficiency angle were skipped unless links >= 10 and the paper is a foundation model, dataset or benchmark. Also skipped: surveys (except two on hardware and edge), attack/backdoor papers, and task benchmarks with no efficiency angle and links < 10.

##### Notable finds
- 2603.17850 ProbeFlow: a training-free adaptive ODE step schedule for flow-matching VLA heads. Action decoding is 14.8x faster and end-to-end latency 2.8x lower on MetaWorld.
- 2509.05614 SpecPrune-VLA: action-aware two-level token pruning. Speedup is 1.57x on LIBERO and 1.70x on real robots.
- 2506.13456 BAC: training-free block-wise feature caching for diffusion policies and VLAs, with up to 3x speedup.
- 2603.17240 GigaWorld-Policy: an action-centred WAM where video generation is optional. It runs 9x faster than Motus.
- 2511.12101 Freeze, Share, Shrink: a 5M-parameter MLP action backbone matches a 244M U-Net. This suggests diffusion action heads are over-parameterized.
- 2505.05787 Action lookup table: replaces a diffusion policy with a lookup table that needs 0.0034x the inference time and 0.0085x the memory.
- 2607.06216 MoWorld: a real-time world model that runs at up to 50 FPS on an NPU.
- 2607.15621 Think at 5 Hz, Act at 20 Hz: asynchronous fast-slow driving VLA at 32 ms per tick on a consumer GPU.
- 2609.23305 Shared Execution-Clock Drifting Policy: a one-step policy running onboard NVIDIA Thor for deadline-sensitive manipulation.
- 10.1109/FCCM68464.2026.00075 SmolVLA on an AMD XDNA NPU: an early prototype of VLA deployment on an edge NPU.

### SB_6


- Candidates read: 429 (16 had no abstract)
- Recorded: 121
- Skipped: 308
- By relevance: 5 = 1, 4 = 17, 3 = 87, 2 = 16 (context, links >= 10)
- foundational_technique = true: 9 (ToMe, guided-diffusion distillation, FlatQuant, Atom, RPTQ, TTQ, MobileLLM, VisPruner, on-device SLM survey)
- verified = false (title only, no abstract): 3 (RoboMamba 2406.04339, Chunk-Boundary Artifact 2603.11642, Sliding-Cache VLA ICASSP DOI)

Main reasons for skipping: generic VLA/WAM method papers with no efficiency, latency or safety angle (spatial/3D grounding, reasoning/CoT, reward models); surveys; adversarial/security attacks; data-collection systems; and context-type papers with links < 10.

##### Notable finds
- 10.1109/LRA.2026.3683324 DMS-VLA (RA-L): shares weight templates across layers; 25-55% inference speedup on H100/RTX 4090/Jetson AGX Orin (rel 5).
- 2606.02486 AHEAD ("Intercepting the Future"): a 4.9M-parameter latent world model added to a frozen OpenVLA to compensate for latency on moving objects; tested on a real xArm.
- 2603.06331 WorldCache: training-free token caching for diffusion world models, up to 3.7x end-to-end speedup.
- 2605.08732 Latent Geometry Beyond Search: an amortized inverse-dynamics planner that cuts per-decision cost 100-130x compared with CEM.
- 2609.20761 Agile-WAM: tactile world-action model with 11.9 ms inference latency on real contact-rich tasks.
- 2601.14628 NeuroVLA: neuromorphic VLA running at 0.4 W with safety reflexes under 20 ms.
- 2602.06575 ThinkProprio: proprioception-guided visual token selection that keeps about 12% of tokens and lowers end-to-end latency.
- 10.1109/ICCC70295.2026.11680263 VTP: task-aware transmission protocol for VLAs offloaded to edge servers under packet loss (C6).
- 2603.17834 GeCO: time-unconditional flow matching with adaptive early exit and a training-free OOD safety signal; scales to pi0.
- 2504.18792 STDArm: online latency estimation and delay compensation for policies running on moving mobile platforms.
