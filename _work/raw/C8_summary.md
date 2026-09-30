# C8 — Efficient world models for planning and safety monitoring: cluster summary

247 verified records in `C8.jsonl` (47 rated relevance 5, 106 rated 4). By model class: 159 world models, 78 world-action models (WAMs), 4 VLAs, 6 systems/other. There are 120 logged searches (arXiv API, Semantic Scholar citation snowballs, WebSearch/WebFetch). All seeds were found and verified: DreamDojo, DreamZero, DYNA-2 (blog), DreamerV3, TD-MPC2, V-JEPA 2, Cosmos (Predict1 and 2.5), Genie / Genie 2 / Genie 3 (Genie 2 and 3 are blogs only; there is no arXiv tech report), and UniSim.

Caveat: most items are 2026 preprints, many from the last 3 months, and very few are peer-reviewed yet. Almost all speed numbers are GPU-server measurements (A100/H100/L40S/RTX 4090). Only a handful of items report true onboard or edge numbers:
- Jetson AGX Orin Conv3D lowering (2609.31938)
- FlowPilot (2608.00635)
- SkyDreamer (2510.14783)
- the perceptive forward dynamics model (FDM, 2504.19322)
- PhyAI and Embodied.cpp (runtimes)

## Technique families

1. **Skip, sparsify or amortize test-time imagination in WAMs.** This is the largest family. Video prediction serves as a training signal, and at inference the model decodes actions only, or uses a single pass or cached future K/V.
   - Examples: Fast-WAM (190 ms), Faster-WAM/DoT (66.5 ms), RIFT, ForeWAM, GigaWorld-Policy-0.5 (85 ms on RTX 4090), Light-WAM, ImageWAM, LaWAM, LAWA, MoWAM, JEPA-WAM, V-JEPA Policy, SV-WAM/Metis (driving), Being-H0.7.
   - Counter-evidence that some test-time future is still needed for OOD generalization: Faster-WAM (sparse future conditioning), 2609.34981 (the benefit lives in the first denoising step), LAWA.
2. **Step distillation, consistency models and one-step generation of world models and WAMs.**
   - Examples: Flash-WAM (8.1 s to 348 ms), DIDO, S-VAM, AnyStep-WAM (budget-adaptive steps), DreamDojo distillation (10.8 FPS), Cosmos-H-Dreams with Self Forcing (~160 FPS), DYNA-2 one-step video (~90x), DriftWorld (one pass, 30+ fps, 17x), DreamerAD (100 to 1 step, 80x), Interactive World Simulator (consistency models, 15 FPS on a 4090), RealWonder, ForgeWM.
   - Recurring failure mode: naive distillation loses the interaction dynamics that matter most. WAM-OPD is one repair.
3. **Asynchronous, dual-rate and rolling denoising, so a slow world branch sits beside a fast action branch.**
   - Examples: AHA-WAM (24 Hz), GlanceWAM (48 ms per chunk), Rolling-WAM (4.5x), DualWAM, LiMA, MinD, X-WAM asynchronous noise sampling, ReSync, Streaming-WAM, FBFM, InternW0, GE slow-fast mode, and the Motubrain empirical study of asynchronous deployment.
   - The Motubrain study's main finding is that timestamp alignment matters more than the blending method.
4. **Systems-level acceleration.**
   - Caching: training-free state reuse (WAMachine), cross-chunk caches (C3ache, X-Cache), feature caching (WorldCache), KV compression and quantization (FAST-AR, QuantWM 2-bit KV, WorldKV).
   - Quantization: QuantWAMs (W4A4, ~29% memory), Q-WAM (W4A4 with action-subspace protection), PreDE (offline prediction of quantization damage), DINO-WM PTQ studies.
   - Runtimes: PhyAI, Embodied.cpp, Inferix, Jetson Conv3D lowering.
   - Full stacks: DreamZero (38x to 7 Hz) and Motubrain (>50x to 11 Hz) combine step reduction, FP8, caching and compilation.
5. **Latent / JEPA world models for cheap planning.**
   - Examples: V-JEPA 2-AC (~16 s per action vs ~4 min for Cosmos pixel planning), DINO-WM, JEPA-WM design study, DDP-WM (9x), Scope-WM, Sparse Imagination, CompACT (8 tokens per frame), Bilinear WMs (~1000x lower planning time), Fast-LeWM (parallel prefix prediction), hierarchical latent MPC (HWM), TD-MPC/TD-MPC2 lineage.
   - Compression and distillation of TD-MPC2: 317M to 1M params, plus pruning with Lyapunov checks.
   - Adaptive deliberation: Fast-TD-MPC plans only when needed, for about 4x speedup.
6. **Transferring world-model knowledge into fast policies, with zero runtime world model.** Examples: FLARE, "Think like a WM, act like a VLA" (32 ms, 1.86 GB), ForeTime-VLA, Vid2WAM, Privileged Foresight Distillation, WPT, WorldGuide, Enfold.
7. **Imagination-based safety monitoring and filtering.**
   - Latent Hamilton-Jacobi reachability safety filters: latent safety filters, UNISafe (conformal epistemic uncertainty), AnySafe, CrossSafe, language-conditioned filters, latent CBFs, adaptive conformal filters (2609.34300 "When World Models Lie").
   - World-model runtime failure monitors: model-based runtime monitoring, Sirius-Fleet, Foresight, FARM (34k-parameter readout, +0.2 ms), ContactGuard, FoMo-FD, bimanual Cosmos-tokenizer monitor, prediction-error anomaly detection.
   - Candidate screening before execution: JEPA safety shields, Pixels-to-Proofs conformal robust MPC, DreamAvoid, FOREWARN, Pre-VLA.
8. **Trustworthiness of world models as oracles, plus attacks.**
   - Oracle trustworthiness: MiraBench (optimism bias), ICAT (world models miss hazards), C3 calibrated uncertainty, "Biased Dreams" (ensemble disagreement misses compounding error), admissibility/VV&A, failure discovery, DreamLedger.
   - Attacks and poisoning: TrojanWorld, TRAP, world-model supply-chain poisoning.
9. **Fast world models as evaluators and simulators.** Examples: 1X World Model, Veo world simulator for Gemini Robotics (including safety probing), WorldEval (safety detector), WorldGym, RoboWorld (r=0.989), WEAVER, HMA (15x), GE-Sim 2.0 (4x frame skip), BWM, World-in-World closed-loop benchmark.

## Key open problems

- **No common latency protocol.** Papers mix per-chunk latency, observation-to-action latency, GPU time per replan, FPS of generated video, and closed-loop Hz, on different GPUs, so the numbers can't be compared across papers. Waypoint-1.5 explicitly separates rendered FPS, latent FPS and control rate, and few others do.
- **Onboard deployment is nearly absent.** The WAMs with the best reported latency (48-100 ms) are measured on A100/H100/4090-class GPUs. Jetson- or edge-class results for video world models are rare (one Conv3D-lowering paper). Energy is essentially never reported.
- **Efficiency vs. robustness is unresolved.** Dropping test-time imagination keeps in-distribution success but can lose OOD generalization. How much future compute is actually needed (e.g., only the first denoising step?) is still debated.
- **Distillation and quantization interact badly with closed-loop control.** Few-step or low-bit students drift under their own rollouts. Calibration has to use closed-loop states (QuantWAMs, PreDE, WAM-OPD), and the cost of large-scale closed-loop validation is itself a bottleneck.
- **World-model-based safety has weak guarantees.**
  - Optimism bias and missed hazards in video world models (MiraBench, ICAT).
  - Ensemble uncertainty misses compounding error.
  - Partial observability hides safety-relevant state.
  - Conformal wrappers help, but assume exchangeability that deployment shift breaks.
  - Real-time budgets for running both a safety monitor and a policy are rarely analysed.
- **Long-horizon memory at bounded cost.** KV growth in autoregressive world models is the dominant memory cost. Hybrid memory, KV quantization and retrieval are early.
- **Security of world-model supply chains.** Backdoors and poisoning of shared pretrained world models are an emerging, unmitigated risk.

## 10 most important works (for this workshop's framing)

1. **DreamZero — World Action Models are Zero-shot Policies (2602.15922).** A 14B video-diffusion WAM with a 38x optimization stack reaching 7 Hz closed-loop control. It is the reference point for real-time WAMs.
2. **V-JEPA 2 (2506.09985).** Latent action-conditioned world model with zero-shot Franka planning, about an order of magnitude faster than pixel-space (Cosmos) planning.
3. **Fast-WAM (2603.16666).** Shows WAMs work without test-time imagination (190 ms, 4x faster). It set off the "skip the video" line of work (Faster-WAM, RIFT, LAWA, 2609.34981).
4. **DreamDojo (2602.06949).** Foundation robot world model from 44k hours of human video, distilled to ~10.8 FPS for live teleoperation, evaluation and planning.
5. **TD-MPC2 (2310.16828).** Decoder-free latent world model with sampling-based MPC. It is the base for most compact, compressible world-model planners.
6. **Latent safety filters (2502.00935) and UNISafe (2505.00779).** Hamilton-Jacobi reachability run inside a world model's latent space, made uncertainty-aware with conformal calibration. They are the core of imagination-based safety monitoring.
7. **Flash-WAM (2606.05254).** Modality-aware consistency distillation to one step per modality, cutting per-chunk latency 23x (8.1 s to 348 ms on L40S) with real humanoid evaluation.
8. **DriftWorld (2607.15065).** One-pass action-conditioned world model at 30+ fps (17x faster than diffusion baselines), which makes large-scale rollout search for planning practical.
9. **QuantWAMs (2607.28405).** First WAM-specific W4A4 PTQ, calibrated on closed-loop rollouts (~29% memory, real AgiBot trials). Q-WAM (2609.33269) is a companion.
10. **Foresight (2606.23085) and FARM (2609.11445).** Policy-agnostic runtime failure monitors that read action-conditioned world-model latents. FARM shows monitoring can be nearly free (a 34k-parameter readout, +0.2 ms).

Also foundational: DreamerV3 (2301.04104), Cosmos (2501.03575), Genie 3 (blog: real-time 720p/24 fps), UniSim (2310.06114), DYNA-2 (blog: shallow action stream and ~90x one-step video distillation).
