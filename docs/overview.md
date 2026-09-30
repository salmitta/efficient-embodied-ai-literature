# Literature database overview — Efficient Foundation Models for Real-Time Embodied AI (CoRL 2026 workshop)

Built 2026-09-30. **2232 unique items** (from 2883 raw records across 17 subagent outputs; 651 duplicates merged by arXiv ID, DOI, URL and normalized/fuzzy title). Files: `literature_db.jsonl`, `literature_db.csv`, `by_cluster/C1–C9.md`, `efficiency_table.csv`, `search_log.md`.

## Counts

| Cluster | Items | rel 5 | rel 4 | with efficiency numbers |
|---|---|---|---|---|
| C1 Efficient architectures for VLA policies and emerging designs | 733 | 129 | 212 | 325 |
| C2 Compression for robot foundation models | 365 | 107 | 106 | 165 |
| C3 Memory-efficient adaptation and fine-tuning | 453 | 66 | 100 | 132 |
| C4 Benchmarking methodology and composability | 363 | 79 | 69 | 97 |
| C5 Hardware-aware design and accelerators | 245 | 86 | 55 | 131 |
| C6 Edge-cloud co-design and fleet systems | 218 | 42 | 58 | 86 |
| C7 Safety under latency and timing variability | 539 | 86 | 153 | 132 |
| C8 Efficient world models for planning and safety monitoring | 522 | 67 | 155 | 137 |
| C9 People, venues and blogs | 260 | 91 | 79 | 128 |

Items carry multiple cluster tags, so the column sums exceed the unique total.

- **By type:** preprint 1564, paper 465, benchmark 88, tech-report 51, blog 39, repo 23, talk 2
- **By year:** 2010 1, 2015 3, 2016 1, 2017 2, 2018 10, 2019 15, 2020 13, 2021 26, 2022 46, 2023 81, 2024 188, 2025 537, 2026 1306, unknown 3
- **By relevance:** 5: 248, 4: 529, 3: 953, 2: 497, 1: 5
- **Foundational techniques:** 138; **real-robot evaluation:** 859; **onboard deployment:** 139
- **Efficiency numbers:** 617 items (`efficiency_table.csv`). What they measure: relative latency 227, other 215, throughput 69, closed-loop control 37, relative memory 34, open-loop chunk rate 18, energy 17.

## Technique taxonomy

The families below organize the whole database. Cluster tags are in brackets. Example IDs point to records in `literature_db.jsonl`.

1. **Make the model smaller** [C1, C2]
   - *Compact-by-design VLAs.* Examples: TinyVLA, MiniVLA, SmolVLA (2506.01844), NanoVLA, Evo-1, VLA-Adapter (2509.09372). Also LLM-free heads such as TurboVLA, and hypernetwork-activated policies (HyperVLA 2510.04898).
   - *Quantization.* PTQ with action-centric or closed-loop-aware bit allocation: QVLA 2602.03782, DA-PTQ, DyQ-VLA. Rotation-based W4A4: HoloQ-VLA 2605.28803, FoldQuantVLA 2609.24433. QAT: QAIL 2412.01034, SQIL. Native ternary: BitVLA 2506.07530. 1-bit PTQ: HBVLA 2602.13710. World-action models: Q-WAM, QuantWAMs 2607.28405.
   - *Pruning and depth reduction.* Structured and width pruning, layer skipping, redundancy analyses (Drop-Then-Recovery 2606.27755), and recovery methods such as RLRC 2506.17639 and GLUESTICK 2510.08464.
   - *Knowledge distillation into compact students.* Shallow-π 2601.20262, VLA-AD, XS-VLA, and representation distillation (Theia).
2. **Do less work per control step** [C1]
   - *Visual token pruning and merging.* VLA-Pruner, LightVLA, SP-VLA, SpecPrune-VLA 2509.05614.
   - *Temporal reuse.* KV and feature caching: VLA-Cache 2502.02175, EfficientVLA 2506.10100. Action reuse and warm starts.
   - *Dynamic compute.* Early exit (DeeR-VLA 2411.02359), mixture-of-layers and layer skipping, MoE (MoDE), and adaptive denoising steps.
   - *Efficient reasoning.* Latent or parallel chain-of-thought, and gating decisions about when to reason at all.
3. **Generate actions faster** [C1, C2]
   - *Action tokenization and representation.* FAST 2501.09747, VQ-VLA, BEAST, and B-spline or Legendre chunks.
   - *Parallel and non-autoregressive decoding.* OpenVLA-OFT 2502.19645, Jacobi decoding, discrete and block diffusion.
   - *Speculative decoding for VLAs.* Spec-VLA and related work.
   - *Few-step and one-step generative heads.* Consistency Policy 2405.07503, OneDP 2410.21257, MeanFlow and shortcut models, SnapFlow, and optimal-transport or warm priors. A counter-thread argues heavy iteration is often unnecessary (two-step regression policies).
4. **Decouple thinking from acting** [C1, C6, C7]
   - *Dual-system and fast/slow designs.* Helix, GR00T N1 2503.14734, Hi Robot, π0.5 2504.16054, RoboDual, Fast-in-Slow.
   - *Hierarchical and cloud-edge splits.* Gemini Robotics 2503.20020 with On-Device, CloudEdgeVLA, AsyncVLA 2602.13476, VLA-ULAP.
5. **Hide latency: chunking and asynchronous execution** [C1, C6, C7]
   - *Chunking and temporal ensembling.* ACT 2304.13705.
   - *Asynchronous chunk execution.* RTC 2506.07339 and training-time RTC 2512.05964, Bidirectional Decoding 2408.17355, VLASH 2512.01031, A2C2 2509.23224, FASTER, Streaming Diffusion Policy, and LeRobot async inference.
   - *Adaptive execution horizons.* Knowing When to Stop, EQRL, SparkVLA.
   - *Comparisons.* 2605.08168 is a controlled head-to-head comparison.
6. **Systems, kernels and hardware** [C5]
   - *Workload characterization and performance models.* VLA-Perf 2602.18397, XPU characterization 2604.24447, 2603.02271. Common finding: the VLM prefill is compute-bound, while decode and the action expert are memory-bound at batch 1.
   - *Kernel and graph optimization.* CUDA graphs, fusion, TensorRT, FP8/NVFP4; 2510.26742 and the GR00T TensorRT guide.
   - *Portable edge runtimes.* vla.cpp 2606.08094, Embodied.cpp, vla.simd.
   - *Onboard recipes.* Jetson-PI 2607.12659, plus deployments on Orin Nano and Thor.
   - *Accelerators and co-design.* Dadu-Corki 2407.04292, DiTPA, SpecVLA, and older robotics processors (RoboX, Tartan).
7. **Serve many robots** [C6]
   - *Cloud and fog robotics platforms.* FogROS2 2205.09778.
   - *Split computing and offloading.* RoboECC, RAPID, EcoVLA.
   - *Fleet serving with chunk-aware batching and SLOs.* ROSA 2607.01088, Robion, Kairos 2605.11381, Armory 2608.00337.
   - *Measurement studies.* Offload or Overload 2603.18284.
8. **Adapt cheaply** [C3]
   - *PEFT and LoRA recipes.* Robot transfer needs high ranks, around r≈32–128.
   - *Optimized fine-tuning recipes.* OFT, and Knowledge Insulation 2505.23705.
   - *Efficient RL post-training.* SimpleVLA-RL, πRL, and RLinf-VLA 2510.06710 as infrastructure.
   - *Weight-free steering.* DSRL 2506.15799.
   - *Residual policies, and post-training inside a world model.*
   - *Continual and lifelong adaptation.*
9. **Stay safe despite latency** [C7]
   - *Safety filters and CBFs.* 1903.11199, 2309.05837. Includes multi-step and chunk-level filters, and constraints enforced inside flow or diffusion denoising: SafeFlowMatcher 2509.24243, and 2607.01378 for VLAs.
   - *Latent-space reachability.* 2502.00935, UNISafe 2505.00779.
   - *Failure detection and runtime monitors.* SAFE 2506.09937, FIPER 2510.09459, FAIL-Detect 2503.08558, Sentinel 2410.04640.
   - *Runtime assurance and Simplex.*
   - *Conformal guarantees.*
   - *Real-time scheduling and WCET of DNN inference.*
10. **Plan with efficient world models** [C8]
    - *Latent world models.* DreamerV3 2301.04104, TD-MPC2 2310.16828, V-JEPA 2 2506.09985.
    - *Video and world-action models.* Cosmos 2501.03575, DreamZero 2602.15922, DreamDojo 2602.06949.
    - *"Skip the video" WAMs.* Fast-WAM 2603.16666.
    - *Few-step or consistency distillation.* Flash-WAM 2606.05254.
    - *WAM quantization.*
    - *World-model-based safety monitoring.* Foresight, FARM.
11. **Measure it properly** [C4]
    - *Simulation benchmarks and their robustness variants.* LIBERO and LIBERO-Plus/PRO, SimplerEnv, CALVIN, RLBench, ManiSkill.
    - *Benchmark validity audits.* 2606.04233, and 2609.37771 on benchmark bugs.
    - *Real-robot evaluation infrastructure.* RoboArena 2506.18123, AutoEval 2503.24278.
    - *Statistical methodology.*
    - *Embodied-efficiency and energy metrics.* 2603.19131, 2606.28529.
    - *Latency-injected closed-loop evaluation.*
    - *The workshop's own benchmark.* `embodied-efficiency-challenge-corl2026`: a compress-to-budget contest on Jetson Orin NX that scores median and p99 latency per action.


## Top 30 must-read works

| # | Work | Year | Clusters | Why |
|---|---|---|---|---|
| 1 | [$\pi_0$: A Vision-Language-Action Flow Model for General Robot Control](https://arxiv.org/abs/2410.24164) | 2024 | C1, C2, C3, C4, C5, C9 | π0: the VLM + flow-matching action-expert template most efficiency work now targets. |
| 2 | [$π_{0.5}$: a Vision-Language-Action Model with Open-World Generalization](https://arxiv.org/abs/2504.16054) | 2025 | C1, C9 | π0.5: open-world generalization with the same architecture; common acceleration/compression target. |
| 3 | [FAST: Efficient Action Tokenization for Vision-Language-Action Models](https://arxiv.org/abs/2501.09747) | 2025 | C1, C9 | FAST: DCT+BPE action tokenization that makes autoregressive VLAs trainable and faster. |
| 4 | [Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success](https://arxiv.org/abs/2502.19645) | 2025 | C1, C2, C3, C4, C5, C9 | OpenVLA-OFT: parallel decoding + chunking + continuous actions (≈26× throughput); the baseline efficiency recipe. |
| 5 | [OpenVLA: An Open-Source Vision-Language-Action Model](https://arxiv.org/abs/2406.09246) | 2024 | C1, C2, C3, C4, C5, C9 | OpenVLA: the 7B open VLA behind most compression/profiling studies; first 4-bit real-robot evidence. |
| 6 | [Helix: A Vision-Language-Action Model for Generalist Humanoid Control](https://www.figure.ai/news/helix) | 2025 | C1, C2, C5, C6, C9 | Helix: reference industrial onboard fast/slow design (S2 7–9 Hz, S1 200 Hz on embedded GPUs). |
| 7 | [GR00T N1: An Open Foundation Model for Generalist Humanoid Robots](https://arxiv.org/abs/2503.14734) | 2025 | C1, C2, C3, C5, C7, C9 | GR00T N1: open dual-system humanoid VLA with public TensorRT cross-hardware latency tables. |
| 8 | [SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics](https://arxiv.org/abs/2506.01844) | 2025 | C1, C2, C3, C4, C5, C6, C7, C9 | SmolVLA: ~450M VLA plus open asynchronous inference stack (LeRobot). |
| 9 | [Gemini Robotics: Bringing AI into the Physical World](https://arxiv.org/abs/2503.20020) | 2025 | C1, C2, C5, C6, C7, C9 | Gemini Robotics: cloud backbone + onboard decoder with reported latency; paired with the On-Device release. |
| 10 | [Diffusion Policy: Visuomotor Policy Learning via Action Diffusion](https://arxiv.org/abs/2303.04137) | 2023 | C1, C2, C7 | Diffusion Policy: the generative-policy baseline whose sampling cost motivated step-reduction work. |
| 11 | [Consistency Policy: Accelerated Visuomotor Policies via Consistency Distillation](https://consistency-policy.github.io/) | 2024 | C1, C2 | Consistency Policy: distils diffusion policies to one/few steps; foundation for few-step action heads. |
| 12 | [Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware](https://arxiv.org/abs/2304.13705) | 2023 | C1, C2, C7 | ACT/ALOHA: introduced action chunking and temporal ensembling. |
| 13 | [Real-Time Execution of Action Chunking Flow Policies](https://arxiv.org/abs/2506.07339) | 2025 | C1, C2, C3, C4, C6, C7, C9 | Real-Time Chunking (RTC): freeze-and-inpaint asynchronous execution for large chunking policies. |
| 14 | [Bidirectional Decoding: Improving Action Chunking via Guided Test-Time Sampling](https://arxiv.org/abs/2408.17355) | 2024 | C1, C2, C7 | Bidirectional Decoding: formalizes the consistency-vs-reactivity trade-off of chunked execution. |
| 15 | [VLASH: Real-Time VLAs via Future-State-Aware Asynchronous Inference](https://arxiv.org/abs/2512.01031) | 2025 | C1, C2, C3, C4, C5, C6, C7, C9 | VLASH: future-state-aware async inference; large reaction-latency reductions at no runtime cost. |
| 16 | [Understanding Asynchronous Inference Methods for Vision-Language-Action Models](https://arxiv.org/abs/2605.08168) | 2026 | C1, C2, C4, C6, C7 | Understanding Async Inference Methods for VLAs: controlled head-to-head of RTC variants, VLASH, A2C2. |
| 17 | [VLA-Cache: Towards Efficient Vision-Language-Action Model via Adaptive Token Caching in Robotic Manipulation](https://doi.org/10.48550/arXiv.2502.02175) | 2025 | C1, C4 | VLA-Cache: training-free temporal token/KV reuse across control steps. |
| 18 | [DeeR-VLA: Dynamic Inference of Multimodal Large Language Models for Efficient Robot Execution](https://arxiv.org/abs/2411.02359) | 2024 | C1, C2, C4, C5, C9 | DeeR-VLA: budget-conditioned dynamic early exit for VLAs. |
| 19 | [Running VLAs at Real-time Speed](https://arxiv.org/abs/2510.26742) | 2025 | C1, C2, C3, C5, C7 | Running VLAs at Real-time Speed: kernel/graph-level recipe for π0 at ≈30 Hz on a consumer GPU. |
| 20 | [Jetson-PI: Towards Onboard Real-Time Robot Control via Foresight-Aligned Asynchronous Inference](https://arxiv.org/abs/2607.12659) | 2026 | C1, C2, C3, C4, C5, C6, C7, C9 | Jetson-PI: onboard asynchronous VLA on Jetson Orin with CUDA-level system optimizations. |
| 21 | [How Fast Can I Run My VLA? Demystifying VLA Inference Performance with VLA-Perf](https://arxiv.org/abs/2602.18397) | 2026 | C1, C3, C4, C5, C6, C7, C9 | VLA-Perf: analytical, hardware-normalized performance model for VLA placement and design. |
| 22 | [Characterizing Vision-Language-Action Models across XPUs: Constraints and Acceleration for On-Robot Deployment](https://arxiv.org/abs/2604.24447) | 2026 | C1, C3, C4, C5, C7, C9 | VLAs across XPUs: cost/energy/time leaderboard; compute-bound VLM vs memory-bound action expert. |
| 23 | [From Inference Efficiency to Embodied Efficiency: Revisiting Efficiency Metrics for Vision-Language-Action Models](https://arxiv.org/abs/2603.19131) | 2026 | C1, C2, C4, C5, C9 | From Inference Efficiency to Embodied Efficiency: task-level metrics (completion time, motion energy). |
| 24 | [The Speedup Paradox: Rethinking Inference Speed-Quality Trade-off in Embodied Tasks](https://arxiv.org/abs/2606.28529) | 2026 | C1, C2, C4, C5, C7, C9 | The Speedup Paradox: per-step speedups need not shorten tasks; hardware-dependent sweet spots. |
| 25 | [BitVLA: 1-bit Vision-Language-Action Models for Robotics Manipulation](https://arxiv.org/abs/2506.07530) | 2025 | C1, C2, C5, C9 | BitVLA: first native 1.58-bit VLA; large memory/latency savings vs OpenVLA-OFT. |
| 26 | [VLAQuantBench: Closed-Loop Evaluation of Post-Training Quantization for Vision-Language-Action Models](https://arxiv.org/abs/2609.25376) | 2026 | C1, C2, C4, C5, C9 | VLAQuantBench: closed-loop PTQ benchmark exposing recipe-dependent quantization failures. |
| 27 | [RLRC: Reinforcement Learning-based Recovery for Compressed Vision-Language-Action Models](https://arxiv.org/abs/2506.17639) | 2026 | C1, C2, C3, C4, C9 | RLRC: prune → RL recovery → quantize pipeline; key evidence on composing compression techniques. |
| 28 | [Offload or Overload: A Platform Measurement Study of Mobile Robotic Manipulation Workloads](https://arxiv.org/abs/2603.18284) | 2026 | C4, C5, C6, C7, C9 | Offload or Overload: measurement study of onboard vs edge vs cloud for mobile-manipulation FM stacks. |
| 29 | [World Action Models are Zero-shot Policies](https://arxiv.org/abs/2602.15922) | 2026 | C1, C3, C4, C8 | DreamZero: 14B world-action model driven to real-time closed-loop control via an optimization stack. |
| 30 | [SAFE: Multitask Failure Detection for Vision-Language-Action Models](https://arxiv.org/abs/2506.09937) | 2025 | C7, C8 | SAFE: multitask failure detection for VLAs with conformal calibration. |



## The workshop's key questions: what the literature says

### 1. Do efficiency techniques compose?

**Partly, and not additively.**
- Stacks such as EfficientVLA (2506.10100) and Think Twice, Act Once (2505.21200) save far more FLOPs than wall-clock time. EfficientVLA's FLOPs drop to 28.9%, but it is only 1.93× faster.
- Some pairs conflict unless they are co-designed. SQAP-VLA (2509.09090) shows that naive token pruning combined with quantization fails.
- Order matters. RLRC (2506.17639) needs a recovery step between pruning and quantization.
- LLM theory predicts the same: sparsity and quantization are provably non-orthogonal (2405.20935), and speculative decoding erodes the gains from 4-bit weights (2505.22179).
- Systems-level stacking composes more predictably. Examples are CUDA graphs plus fusion (2605.03269) and Jetson-PI's async execution plus CUDA optimizations (2607.12659).

**Open:**
- Nobody has run a factorial study of quantization × distillation × pruning × token reduction × caching × async on one VLA and one device, reporting closed-loop success and wall-clock time.
- Interaction terms are unmeasured, for example whether quantization error grows under RTC inpainting.
- Recipe-level interactions show up even within one technique (VLAQuantBench 2609.25376), and benchmark bugs can reverse rankings (2609.37771).

### 2. How do you interrupt or certify open-loop action-chunk execution?

**Interruption is an active empirical area. Certification barely exists at VLA scale.**

Deployable today:
- *Statistical triggers:*
  - disagreement between samples (TDHD 2608.09125, KeyStone 2605.08638);
  - checking imagined futures against reality in world-action models (FFDC 2605.06222: about 70% fewer replans, also on a real humanoid);
  - learned horizon scheduling (EQRL, SparkVLA);
  - failure detectors (SAFE, FIPER);
  - conformal calibration.
- *Correction:* RTC-family chunk stitching and fast residual correctors under slow chunk planners.
- *Horizon-level safety:* constraints enforced inside flow denoising (2607.01378 on SafeLIBERO; SafeFlowMatcher 2509.24243 has a proof for planners).

The known limits are theoretical:
- Per-candidate certificates do not compose under best-of-k sampling or retries (2609.06036).
- No sound chunk certifier can hold up under unrestricted model mismatch; this is a trilemma (2608.02453).
- Reachability of neural-network control systems is undecidable (2407.04988).
- VLA actions change under ±1° perturbations in sound region validation (2609.22293).

Formal NN verifiers (α-β-CROWN, POLAR, NNV) scale to small controllers, not billion-parameter VLAs. The most plausible template today propagates reachable sets through a low-dimensional policy interface, then calibrates conformally (2608.02545).

**Open:**
- No certificate covers a whole π0-class chunk.
- No work links execution horizon H to a CBF or reachability margin.
- Interrupt-to-safe-stop latency is unmeasured on embedded hardware.
- No WCET or response-time bound exists for VLA or WAM inference on Jetson-class GPUs.

### 3. What is the total cost of ownership of fleet-scale onboard vs cloud inference?

**There is no robotics-specific dollar TCO study.** The evidence is indirect:
- *Shared-GPU fleet serving* raises throughput and meets SLOs but reports no dollars. ROSA 2607.01088 gives up to 12× factory productivity. Robion serves 64 robots on 4 GPUs at 98% SLO.
- *Measurement:* Offload or Overload (2603.18284) finds that small onboard GPUs cannot run full stacks, and large ones drain batteries much faster.
- *Instance selection:* FogROS2-Config cuts cloud cost up to 20× by choosing instance types.
- *Analytical estimates:* SemiAnalysis-style blogs put offload as cheaper beyond about 5–7 robots.
- *Onboard power framing:* "Data Centers on Wheels" (10.1109/mm.2022.3219803) models fleet-wide onboard compute for vehicles.
- *General methods to adapt:* datacenter TCO and levelized cost-per-inference methods (2502.01070, 2509.02596).

**Open:**
- No measured $/robot-hour comparing Orin/Thor capex and energy against cloud GPU-hours, network cost and duty cycle.
- The VLA share of humanoid battery budgets is unknown.
- It is unknown how chunk-aware batching (2608.00337) moves the break-even fleet size.
- It is unknown whether cloud throughput outweighs the success lost to latency.

### 4. How can efficiency be evaluated across hardware comparably?

**Methods exist. A standard does not.**

Building blocks:
- *Analytical performance models:* VLA-Perf 2602.18397.
- *Cross-XPU leaderboards:* 2604.24447.
- *Roofline analysis across Jetson power modes:* Pagoda 2509.20189.
- *A near-MLPerf protocol:* vla.cpp's multi-device tables, reporting p50/p90 latency and peak RSS for 13 VLAs.
- *Power measurement rules:* MLPerf Power 2410.12032, and external power logging (Jetson internal telemetry is biased; 2608.00927).
- *Distributional time-to-success:* PhAIL 2605.29710.
- *Task-level embodied-efficiency metrics:* 2603.19131.

Reported speeds are still not reproducible. OpenVLA users measure 4.4 vs 6.0 actions/s on the same GPU class. Also, 617 database items report numbers measuring at least eight different quantities (see `efficiency_table.csv` → `metric_measures`).

**Open:**
- No agreed protocol jointly reports closed-loop success, perception-to-actuation p50 and p99 latency, and energy per action at a fixed power mode.
- There is no hardware-normalized metric, such as fraction of the bandwidth floor achieved or success per joule.
- Tail latency is almost never reported.

### 5. Can OpenVLA-7B-class models fit 16 GB Jetson devices without losing LIBERO success?

**Probably yes in memory. Not yet shown end-to-end.**

Memory evidence:
- OpenVLA itself reports 16.8 GB (bf16), 10.2 GB (int8) and 7.0 GB (int4), with no real-robot loss at int4, measured on desktop GPUs.
- Independent measurements give 15.3, 8.1 and 4.6 GB peak, but batch-1 latency does not improve.
- vla.cpp measures OpenVLA-OFT BF16 at 15.4 GB peak RSS on AGX Orin, which is too tight for Orin NX 16 GB with a full robot stack.

On-Jetson evidence:
- The only on-Jetson closed-loop evidence is NVIDIA's AGX Orin (64 GB) tutorial. INT4 runs at 336 ms per step with 84% MimicGen success, against 86% for FP16. It is not LIBERO, and not a 16 GB board.
- FoldQuantVLA (2609.24433) runs native W4A4 on Orin.

LIBERO retention at 3–4 bits is reported by several works, mostly using fake quantization on datacenter GPUs: ActQuant 2605.24011, Mix-QVLA 2606.19565, QVLA 2602.03782, BitVLA 2506.07530. W4A4 collapses without rotation.

**Open:** no source reports OpenVLA or OpenVLA-OFT LIBERO success using real low-bit kernels on an Orin NX 16 GB or Orin Nano, together with peak unified memory and control rate. This is exactly what the workshop's Embodied Efficiency Challenge targets.

## Research gaps (cross-cutting)

1. **Metric incomparability.** This is the most repeated finding across all nine clusters. Different papers call different things "speed":
   - open-loop chunk rate;
   - closed-loop control rate;
   - throughput at batch 8;
   - relative latency;
   - FLOPs.

   Hardware, denoising steps, camera count or batch size are often omitted.
2. **Onboard evidence is thin.** Most efficiency claims are measured on RTX 4090/A100/H100. Jetson/Thor/NPU closed-loop results are a small minority, and industrial systems (Helix, Gemini Robotics On-Device, Tesla, 1X) disclose little. No public Trainium/Inferentia or mobile-NPU VLA evidence was found.
3. **Open-loop fidelity ≠ closed-loop success.** Compression, caching and token skipping pass offline checks and then fail in rollout (for example 2609.23048, and a distilled Octo scoring 0/72). LIBERO is saturated and gameable: a 0.54M-parameter policy scores 95%. Robustness variants and dynamic, latency-sensitive tasks are needed to judge efficient models.
4. **Tail latency, jitter and energy are rarely reported.** Delay robustness is usually tested with fixed or uniform synthetic delays in simulation. Energy per action or per successful episode appears in only a handful of papers, measured in different ways.
5. **Safety compute is not budgeted.** Monitors and filters add latency inside the control period, and few papers report it. Guarantees rarely survive asynchronous hand-offs or sampling-based verification.
6. **Composition and ordering of techniques** are unmeasured (see question 1).
7. **Economics.** There is no measured TCO for fleets, and no decision theory for when to call the cloud with safety guarantees under degraded links.
8. **Efficient world-action models** are moving fastest: new 2026 preprints arrive weekly and the recency sweep did not saturate. The open debate is whether test-time imagination is needed at all (Fast-WAM vs GlanceWAM). Onboard and energy numbers for WAMs are nearly absent.
9. **Adaptation and deployment compression are handled separately.** Examples include LoRA/quantization mismatch and RL recovery after pruning. On-robot adaptation under compute and safety budgets is essentially unexplored.

## Coverage and saturation notes

- Round 1 ran nine cluster subagents (C1–C9). They logged about 800 queries in total (see `search_log.md`).
  - C2, C6, C7 and C8 reached the brief's saturation criterion.
  - C1, C3, C4, C5 and C9 stopped just short. The main reasons were a session-wide web-search cap (200 calls) and Semantic Scholar rate limits. Their remaining new items were mostly 2026 preprints.
- Round 2 made up for this in two ways:
  - It ran a programmatic citation snowball over all 571 relevance ≥ 4 arXiv items: about 37k linked papers, of which 2,574 abstracts were triaged.
  - Two targeted gap agents ran a 2026 recency sweep. It saturated for quantization, MoE/early exit, speculative decoding and continual learning, but not for world-action models or adaptive-compute VLAs.
- The field is expanding faster than any single sweep. Expect new relevant 2026 preprints weekly, especially in C1, C3 and C8.
- Relevance-2 items (about 500) are context: major robot foundation models, datasets and benchmarks that the efficiency literature builds on. Filter on `relevance >= 3` for the core set, which has about 1,730 items.


## Items needing manual review

### Unverified items (1 remaining)

Of 15 originally unverified items, 5 were garbled duplicates of verified records and have been merged. 9 were confirmed against a fetched abstract or page on 2026-09-30: the `relevance_reason` of each says which source. The item below could not be confirmed: no abstract is available from Semantic Scholar, OpenAlex, OpenReview or arXiv, and the session's web-search budget was exhausted.

- `s2-simulation-evaluating-robot-policies-asynchronous-real-time` — [Simulation for Evaluating Robot Policies Should Be Asynchronous and Real-Time](https://www.semanticscholar.org/paper/3dc6d3bd6abc687a9087096b671bd53e9c31d70b) (paper, n.d.) — Evaluation under latency.

### Venue spot-checks (resolved 2026-09-30)

The C8 subagent had filled conference venues for these papers from memory, and C2 had flagged Consistency Policy and π0 as unconfirmed. Each was re-checked against DBLP keys, Crossref, OpenReview, the RSS proceedings, or Semantic Scholar venue metadata. DBLP's own search page blocks scripted access, so DBLP keys come through Semantic Scholar.

| ID | Title | Venue now | Resolution |
|---|---|---|---|
| `2301.04104` | Mastering Diverse Domains through World Models | Nature 2025 (arXiv 2023) | confirmed — Crossref DOI 10.1038/s41586-025-08744-2 (Nature, 2025) |
| `2310.16828` | TD-MPC2: Scalable, Robust World Models for Continuous Control | ICLR 2024 | confirmed — DBLP conf/iclr |
| `2402.15391` | Genie: Generative Interactive Environments | ICML 2024 | confirmed — DBLP conf/icml |
| `2310.06114` | Learning Interactive Real-World Simulators | ICLR 2024 | confirmed ICLR 2024 — DBLP conf/iclr; unconfirmed 'Outstanding Paper' note removed |
| `2412.14803` | Video Prediction Policy: A Generalist Robot Policy with Predictive Visual Representations | ICML 2025 | confirmed — DBLP conf/icml |
| `2503.00653` | Discrete Codebook World Models for Continuous Control | ICLR 2025 | confirmed — DBLP conf/iclr |
| `2302.00111` | Learning Universal Policies via Text-Guided Video Generation | NeurIPS 2023 | confirmed — DBLP conf/nips |
| `2405.07503` | Consistency Policy: Accelerated Visuomotor Policies via Consistency Distillation | RSS 2024 | confirmed RSS 2024 — DBLP conf/rss |
| `2505.14357` | Vid2World: Crafting Video Diffusion Models to Interactive World Models | ICLR 2026 | confirmed — OpenReview 'ICLR 2026 Poster' |
| `2505.00779` | Uncertainty-aware Latent Safety Filters for Avoiding Out-of-Distribution Failures | CoRL 2025 | confirmed — OpenReview 'CoRL 2025 Poster' |
| `2502.00935` | Generalizing Safety Beyond Collision-Avoidance via Latent-Space Reachability Analysis | RSS 2025 | confirmed — RSS 2025 proceedings listing |
| `2502.01828` | From Foresight to Forethought: VLM-In-the-Loop Policy Steering via Latent Alignment | RSS 2025 | confirmed — RSS 2025 proceedings listing |
| `2503.00200` | Unified Video Action Model | RSS 2025 | confirmed — RSS 2025 proceedings listing |
| `2410.24164` | $\pi_0$: A Vision-Language-Action Flow Model for General Robot Control | RSS 2025 | confirmed RSS 2025 — RSS 2025 proceedings listing |
| `2405.15223` | iVideoGPT: Interactive VideoGPTs are Scalable World Models | NeurIPS 2024 | confirmed — Semantic Scholar venue metadata |
| `2506.08009` | Self Forcing: Bridging the Train-Test Gap in Autoregressive Video Diffusion | NeurIPS 2025 | confirmed — Semantic Scholar venue metadata |
| `2411.04983` | DINO-WM: World Models on Pre-trained Visual Features enable Zero-shot Planning | ICML 2025 | confirmed — Semantic Scholar venue metadata |
| `2203.04955` | Temporal Difference Learning for Model Predictive Control | ICML 2022 | confirmed — Semantic Scholar venue metadata |
| `2410.22689` | Multi-Task Interactive Robot Fleet Learning with Visual World Models | CoRL 2024 | confirmed — Semantic Scholar venue metadata |
| `2405.12399` | Diffusion for World Modeling: Visual Details Matter in Atari | NeurIPS 2024 | confirmed — Semantic Scholar venue metadata |
| `2310.17552` | Model-Based Runtime Monitoring with Interactive Imitation Learning | ICRA 2024 | **corrected** CoRL 2023 → ICRA 2024 (DBLP conf/icra, Semantic Scholar) |
| `2502.04296` | Learning Real-World Action-Video Dynamics with Heterogeneous Masked Autoregression | arXiv | **reverted** to arXiv — 'CVPR 2025' not found in the CVF CVPR 2025 listing or OpenReview |
