# SB_2 — snowball round 2 triage (shard2)

- Candidates read: 429
- Recorded: 97
- Skipped: 332 (generic VLA/WAM method papers without an efficiency angle and <10 core links, robot attacks/security, LLM agents/planners, driving/traffic work without robot angle, datasets/benchmarks below link threshold)
- By relevance: 5 = 8, 4 = 18, 3 = 45, 2 = 26
- Foundational techniques: 6 (DMD, DivPrune, KIVI, QServe, FLAP, LongLive)
- Unverified (no abstract, title-only): 3 (Open X-Embodiment, RLinf-VLA, pi*0.6)

## Notable finds
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
