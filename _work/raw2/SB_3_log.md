# SB_3 — snowball round 2 triage log (shard3)

- Candidates read: 429 (all lines of shards/shard3.jsonl)
- Recorded: 124
- Skipped: 305 (includes 2 duplicates: `10.48550/arXiv.2503.01238` merged into 2503.01238; `10.48550/arXiv.2412.04445` duplicate of 2412.04445)

## Count by relevance
| relevance | count |
|---|---|
| 5 | 2 |
| 4 | 13 |
| 3 | 81 (incl. 10 foundational_technique=true) |
| 2 (context, links >= 10) | 28 |

- verified=false (no abstract): 2 (2408.17355 Bidirectional Decoding; 2206.09557 nuQmm)

## Notable finds
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
