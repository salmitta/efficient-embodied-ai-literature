# C1 — Efficient architectures for VLA policies and emerging designs: cluster summary

**Records:** 287 in `C1.jsonl` (286 verified, 1 unverified). **Searches:** 88 (see `C1_searchlog.md`).
Relevance split: 52 rated 5, 118 rated 4, 96 rated 3, 21 rated 2.
**Caveats:**
- Semantic Scholar was rate-limited for the whole run, so citation-graph snowballing was replaced by seed-name and keyword searches.
- The saturation rule was not met. The last 10 searches still produced 14 new items, most of them 2026 preprints.

## Technique families

1. **Small / lightweight VLAs (backbone downsizing).**
   - Seeds: TinyVLA, MiniVLA (~1B, Qwen2.5-0.5B), SmolVLA (~450M, trained on community data), EdgeVLA.
   - Also: FLOWER (950M, pruned VLM layers), Evo-1 (0.77B), VLA-Adapter (0.5B backbone), NanoVLA (Jetson Orin Nano), XS-VLA (0.25B).
   - A newer wave drops the LLM entirely and fuses separately encoded vision and language into a compact head: TurboVLA (0.2B, ~32 Hz on an RTX 4090, <1 GB VRAM) and DEM (6.1 ms per forward pass).
   - SSM backbones: RoboMamba, AnoleVLA, and a Mamba action expert for SmolVLA.
   - Hypernetworks that activate only a small task-specific policy: HyperVLA (90x fewer active parameters), TeNet.
2. **Action representation and tokenization.**
   - Seed tokenizers: FAST (DCT+BPE) and FAST+.
   - Learned or structured tokenizers: VQ-VLA, BEAST (B-spline), OmniSAT, FASTer, OAT (ordered, anytime decoding), ActionCodec, X-Tokenizer.
   - Continuous parameterizations: Legendre polynomials (FLASH) and B-splines (ABPolicy).
3. **Parallel and non-autoregressive decoding.**
   - OpenVLA-OFT (parallel decoding + chunking + L1 regression; 26x throughput).
   - Jacobi-style decoding: PD-VLA, CEED-VLA.
   - Discrete and block diffusion: Discrete Diffusion VLA, BlockVLA, TBD-VLA, dVLA, Holo-M.
   - Speculative decoding: Spec-VLA, KERV, HeiSD, WA-SpecDec, FLASH-spec, TS-DP.
4. **Few-step and one-step generative action heads.**
   - Distillation: Consistency Policy, OneDP (1.5 to 62 Hz), ManiCM, SnapFlow (pi0.5 latency 274 to 83 ms), VDD (distilled into a mixture of experts).
   - MeanFlow and shortcut models: MeanFlow VLA, HybridFlow (2 NFE, Jetson Thor), ElasticFlow, ReactVLA, MVP, DriftingVLA.
   - Straighter paths: optimal-transport couplings, WarmPrior, CF-VLA (learned coarse initialization), normalizing-flow heads (NinA).
   - Evidence that heavy iteration may be unnecessary: "Much Ado About Noising" (a two-step regression policy matches flow policies) and "Let It Be Simple" (one-step decoding works because of the condition-target structure).
5. **Dynamic / adaptive compute.**
   - Early exit: DeeR-VLA, decoupled early exits for flow VLAs, LoopVLA (recurrent depth).
   - Layer skipping and mixtures of layers: MoLe-VLA, DySL-VLA, ActDistill, AC²-VLA.
   - Adaptive denoising steps: D3P, FASA, AdaVLA, ELASTIC.
   - MoE: MoDE (90% fewer FLOPs via expert caching), AdaMoE, Dense-to-MoE deactivation, GeRM.
6. **Visual token pruning, merging and compression.** VLA-Pruner, LightVLA (differentiable), SP-VLA, ADP, BFA++, SAFE-Pruner, CogVLA, SemanticVLA, Compressor-VLA, GridS, ST-Merge (8.3x at high resolution), DepthCache, TIES.
7. **Temporal reuse: KV, feature and action caching.**
   - Token and KV reuse: VLA-Cache (seed), TVCache, learned caching, DySta, Gated VLA-Cache, Reflex (streaming KV).
   - Denoiser feature caching: EfficientVLA, EVO cache schedules, test-time sparsity.
   - Action reuse: ActionCache (warm starts), FlashVLA (action reuse), rMuscle (reuse across repeated executions).
   - A warning: training-free token skipping can compound errors across control steps unless it is periodically refreshed with a dense pass ("The Gate, Not the Cache"). Prefix caching also showed limited gains in the CrossVLA study.
8. **Action chunking and real-time execution.**
   - Foundations: ACT and temporal ensembling, Diffusion Policy with receding horizon, BID.
   - Asynchronous execution: RTC (inference-time inpainting), training-time RTC, Legato, REMAC, VLASH (roll the state forward), A2C2 (residual correction), FASTER (time-to-first-action), urgency-aware denoising, Streaming Diffusion Policy, FlashVLA streaming, RAVEL.
   - Adaptive horizons: AAC, GeoAAC, PACE, Mixture of Horizons, PolicyTrim.
   - Practical stacks: LeRobot async inference, Dexmal real-time pi0 at 30 Hz, Jetson-PI (8.66x control-rate gain on Orin).
9. **Dual-system / fast-slow / hierarchical designs.**
   - Seeds: Helix (7B VLM at 7-9 Hz plus an 80M model at 200 Hz, onboard), GR00T N1/N1.5/N1.6, Hi Robot, pi0.5.
   - Research systems: RoboDual, HiRT, Fast-in-Slow (117.7 Hz), DuoCore-FS, UniFS (multi-rate layers), Latent Bridge (50-75% fewer VLM calls), TIDAL, StreamVLA, EMS model switching, SkipVLA (classical planner for free-space motion).
   - Cloud-edge splits: CloudEdgeVLA, AsyncVLA-nav, VLA-ULAP.
10. **Efficient reasoning VLAs.** Latent CoT and early exit: Fast-ThinkAct, AVA-VLA, LaRA-VLA, LaST0. Reasoning reuse: Fast ECoT. Parallel CoT: DualCoT-VLA.
11. **Measurement and systems characterization** (overlaps with C3 and C9).
   - VLA-Perf analytical model, cross-XPU CET leaderboard, and cross-platform edge/cloud scaling.
   - Jetson Orin/Thor characterization: the action phase is memory-bound and can be up to 75% of latency.
   - Embodied-efficiency metrics and the "speedup paradox": per-step speedups do not always shorten tasks.
   - Runtimes: vla.cpp, Embodied.cpp, vla.simd (CPU / Raspberry Pi 5).

## Key open problems

- **Metric incomparability.** Papers report relative latency, open-loop chunk rate, closed-loop control rate, FLOPs or throughput, often on different GPUs. Task-level completion time and energy are rarely reported (2603.19131 and 2606.28529 show why this matters). A shared on-robot, latency-paired benchmark is missing.
- **Speed versus reactivity.** Chunking and async execution hide latency but create stale-observation and chunk-boundary problems. There is no consensus method: inference-time RTC, training-time RTC, VLASH and A2C2 each win in different delay regimes (2605.08168).
- **Compounding errors of training-free acceleration** such as token skipping, caching and pruning under closed-loop rollout. Most papers evaluate only on LIBERO or SIMPLER, where success rates are near saturation.
- **Keeping VLM knowledge while shrinking or insulating the backbone.** See knowledge insulation, VLM4VLA, and the finding that LLM-free designs nearly match large VLAs on standard benchmarks. It is unclear whether generality survives in the open world.
- **Few-step and one-step generation.** When is it lossless (condition-target structure, multimodality)? How does it interact with RL fine-tuning and test-time scaling?
- **Onboard deployment evidence is thin.** Few works report numbers on Jetson, NPU or CPU hardware. Industrial systems such as Helix, Gemini Robotics On-Device and DYNA-1 disclose little technical detail.
- **Composing techniques.** How do quantization, pruning, caching, few-step sampling and async execution stack together? How should compute be allocated across the backbone, action expert and denoising steps (2609.29382)?

## 10 most important works (for this workshop's framing)

1. **pi0 / pi0.5 + FAST + Knowledge Insulation + RTC** (Physical Intelligence; 2410.24164, 2504.16054, 2501.09747, 2505.23705, 2506.07339): the flow-action-expert template, its tokenizer, training recipe and real-time execution method.
2. **OpenVLA-OFT** (2502.19645): parallel decoding + chunking + continuous actions give 26x throughput. This is the efficiency baseline recipe.
3. **Helix** (Figure, 2025 blog): the reference industrial onboard fast-slow design (200 Hz S1 / 7-9 Hz S2).
4. **GR00T N1** (2503.14734): open dual-system humanoid VLA and a common acceleration target.
5. **SmolVLA** (2506.01844) with LeRobot async inference: small VLA plus an open async stack.
6. **Diffusion Policy → Consistency Policy / OneDP** (2303.04137, 2405.07503, 2410.21257): the line of work taking diffusion policies to few or one sampling steps.
7. **VLA-Cache** (2502.02175) and **EfficientVLA** (2506.10100): training-free temporal and structural redundancy removal.
8. **DeeR-VLA** (2411.02359): dynamic early exit under compute and memory budgets.
9. **VLASH** (2512.01031) / **Running VLAs at Real-time Speed** (2510.26742) / **Jetson-PI** (2607.12659): practical real-time and onboard inference.
10. **VLA-Perf** (2602.18397) together with embodied-efficiency metrics (2603.19131): how to reason about and measure VLA latency on real systems.
