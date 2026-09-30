# C4 — Benchmarking methodology and composability: cluster summary

182 records in `C4.jsonl` (180 verified, 2 unverified). 87 logged searches. Coverage: the seed simulation benchmarks and their robustness variants; real-robot and real-to-sim evaluation infrastructure; statistical evaluation methods; hardware and energy profiling of VLAs; closed-loop and latency-aware evaluation; and evidence on whether efficiency techniques compose.

Caveat: Semantic Scholar was rate-limited (HTTP 429) for the whole run, so I couldn't snowball through its citation graph. Instead I discovered papers with arXiv search and WebSearch, and verified them from arXiv abstract pages.

## Technique / work families

1. **Standard simulation benchmarks (seeds).** LIBERO, CALVIN, RLBench, ManiSkill2/3, SimplerEnv, RoboCasa/RoboCasa365, VLABench, RoboTwin 2.0, BEHAVIOR-1K, THE COLOSSEUM/Colosseum V2. LIBERO (Spatial/Object/Goal/Long) is the de facto place where papers report how much accuracy an efficiency method keeps.
2. **Robustness and diagnostic variants of LIBERO.** LIBERO-PRO, LIBERO-Plus, LIBERO-X, LIBERO-Para, LIBERO-VPro (camera staleness), LIBERO-MAX (mid-task events, query cadence), LIBERO-Recover, LIBERO-Occ, LIBERO-Safety, LIBERO-VIFO, ConflictVLA-Bench, SafeVLA-Bench, SafeManip, RoboRecover, MAIL-Bench. All report large drops from near-saturated clean scores.
3. **Audits of benchmark validity.** "What Are We Actually Benchmarking" (shortcut solvability, significance, overfitting), MINERVA (a 0.54M-parameter policy gets 95% on LIBERO), "Faster and Better?" (benchmark bugs make accelerated models look better than the baseline), IndustrialVLA-Bench (unified schema with evidence tiers), the seed-lottery study, GPUSimBench (GPU simulator non-determinism), FailBench (unreliable VLM success judges).
4. **Real-robot evaluation infrastructure.**
   - Distributed and crowd-sourced: RoboArena.
   - Autonomous: AutoEval, HALTER.
   - Hosted fleets: RoboChallenge/Table30, RoboDojo-RealEval, ArmnetBench.
   - Low-cost and replicable: VLA-REPLICA, FurnitureBench, UMI-Bench, DuoBench, ATOM-Bench, LongBench.
   - Throughput-aware: PhAIL (time-to-success CDF, human-relative throughput, KS tests).
5. **Proxies for real-world evaluation.**
   - Real-to-sim: SimplerEnv, REALM, X2Real, PolaRiS, RobotArena ∞, RoboSnap, ReVeal, VISER, Gaussian-splat soft-body twins, a sim-real correlation recipe.
   - World models as evaluators: WorldEval, WorldGym, RoboWorld, GigaWorld-1/WMBench, GE-Sim 2.0, WorldArena 1/2.
6. **Statistical methodology.** Best-practices paper (Kress-Gazit et al.), sequential policy comparison with near-optimal stopping and anytime-valid (SAVI) tests, prediction-powered sim+real inference (SureSim), betting estimators, SCAPE (conformal), CDF lower bounds, active factor-based evaluation, TRI's careful LBM study.
7. **Hardware-normalized profiling and performance models.** VLA-Perf (analytical model), Cross-Platform Scaling (edge vs cloud, power caps), XPU characterization (cost/energy/time leaderboard), MolmoAct on Orin/Thor, PhyAI (FLOP share ≠ latency share), vla.cpp / Embodied.cpp runtimes, GR00T deployment tables, Intel ISO-TDP comparison, NVIDIA Thor blog (throughput at concurrency 8, which is not control rate), FlashRT forum numbers.
8. **Energy and embodied-efficiency metrics.**
   - Robot-level efficiency: "From Inference Efficiency to Embodied Efficiency" (completion time, jerk, motion energy).
   - Deployment metrics: Habilis-β (tasks/hour, MTBI).
   - Energy measurement: VLA-ULAP (J per inference and per successful episode), EdgeVLN (latency/energy/memory on Orin NX), edge VLM energy profiling (decode dominates), EcoVLA, power-profile metrics on a UR5e, mechanical-work proxies.
9. **Latency-aware closed-loop evaluation.**
   - Controlled delay benchmarks: RTC/Kinetix delay benchmark, ReflexBench (configurable latency), the async-method comparison (RTC vs VLASH vs A2C2), DEFLECT (noisy/spiky delays).
   - Reaction-latency metrics: FASTER (TTFA + execution horizon), Reflex streaming.
   - Throughput vs time-to-first-action: Staircase Policy.
   - Execution-horizon non-monotonicity: PACE.
   - Serving under SLOs: Robion, Armory.
10. **Composability of efficiency techniques.**
    - Naive combination fails: SQAP-VLA (quantization and token pruning are incompatible unless co-designed).
    - Ordered pipeline: RLRC (prune, recover, then quantize).
    - Stacked methods: EfficientVLA (layer pruning + token pruning + caching), SP-VLA, FlashVLA (action reuse + pruning), joint early-exit axes, Jetson-PI (algorithm + CUDA graphs).
    - Closed-loop failure: token-skipping error compounding.
    - Recipe interactions: VLAQuantBench (layer scope × format × calibration), PreDE (predicting quantization damage offline).
    - Deployment changes behavior: SmolVLA ONNX (export changes closed-loop success; the "INT8" artifact was actually FP32).
    - Task-level paradoxes: Speedup Paradox / TISED (per-step speedup can lengthen tasks; lossy inference can raise dynamic-task success; the sweet spot depends on hardware).
    - Hardware dependence: embodied-efficiency repo (weight-only int4 gives no speedup at batch 1).

## Key open problems

- **Metric non-comparability.** Papers report different things as "speed": CUDA/kernel latency, per-step latency, open-loop chunk or action throughput (e.g. OpenVLA-OFT's 26×), server-side module throughput, and closed-loop control rate. Many omit hardware, batch size, denoising steps or camera count. No standard defines end-to-end perception-to-actuation latency including network and preprocessing.
- **Tail latency and jitter are almost never reported.** The workshop challenge (median and p99 per action), SmolVLA-ONNX (p99), LA-IMR and Robion (SLOs) are exceptions. Deadline-miss rate and control-time margin are not standardized.
- **LIBERO is saturated and gameable.** Tiny policies and no-language probes match SOTA, seeds swing results by up to 29 points, and simulator bugs can reverse rankings between accelerated and baseline models. Success retention on clean LIBERO is a weak signal for compressed models. Robustness variants (LIBERO-Plus/PRO) and dynamic, latency-sensitive tasks are needed.
- **Static benchmarks hide the benefits and costs of latency.** Most sims pause the world during inference. Only a few (Kinetix delay, ReflexBench, DOM, LIBERO-MAX, LIBERO-VPro staleness) run the world during inference.
- **Energy per action or per successful episode is rarely measured.** When it is, the methods differ (board power, idle-subtracted, mechanical work).
- **Composability is mostly anecdotal.** No systematic factorial study of stacking quantization × pruning × caching × step reduction × async execution across hardware exists. Evidence shows interactions are non-additive and hardware-dependent.
- **Deployment artifacts can silently differ from the evaluated model** (graph export, precision flags, positional-index precision). Fixed-input numerical checks and artifact audits are not routine.
- **Statistical power in real-robot trials is low** (N ≤ 25, no confidence intervals). Sequential tests, distributional metrics and sim+real inference exist but are rarely adopted. Automated success judges have known biases.
- **Sim/world-model proxies need validity checks** (reconstruction fidelity, judge accuracy) before they can be trusted to rank efficient variants, especially variants that change motion quality.

## 10 most important works for C4

1. **Embodied Efficiency Challenge / embodied-efficiency-bench** (CoRL 2026 workshop). Compress-to-budget on Jetson Orin NX; success within 15 points, then median and p99 latency per action, then params and memory; organizers re-run top entries.
2. **Faster and Better? Benchmark bugs distort VLA acceleration evaluation** (2609.37771).
3. **From Inference Efficiency to Embodied Efficiency** (2603.19131). Robot-level efficiency metrics.
4. **The Speedup Paradox / TISED** (2606.28529). Maps per-step speedup to task-level effects.
5. **VLA-Perf: How Fast Can I Run My VLA?** (2602.18397). Analytical, hardware-normalized performance model.
6. **Characterizing VLAs across XPUs** (2604.24447). Cost/energy/time leaderboard and two-phase bottleneck.
7. **SQAP-VLA** (2509.09090) with **RLRC** (2506.17639) and **VLAQuantBench** (2609.25376). Core evidence on composing quantization and pruning.
8. **What Are We Actually Benchmarking in Robot Manipulation?** (2606.04233), with LIBERO-PRO/LIBERO-Plus (2510.03827, 2510.13626).
9. **RoboArena** (2506.18123) and **AutoEval** (2503.24278). Scalable real-robot evaluation; complemented by **PhAIL** (2605.29710) for throughput-aware statistics.
10. **Understanding Asynchronous Inference Methods for VLAs** (2605.08168). Controlled delay-sweep comparison; complemented by ReflexBench (2608.14379).
