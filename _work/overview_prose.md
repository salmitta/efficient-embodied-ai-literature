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

<!--TOP30-->

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
