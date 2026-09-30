# C7 — Safety under latency and timing variability: cluster summary

Corpus: 230 records in `C7.jsonl` (227 verified, 3 title-only Semantic Scholar records flagged `verified: false`); 115 logged searches in `C7_searchlog.md`. The literature is heavily 2025–2026. After Physical Intelligence's RTC (June 2025), asynchronous-execution papers grew quickly. Runtime monitoring for VLAs grew in parallel after SAFE, FIPER and FAIL-Detect.

## Technique families

1. **Asynchronous execution with chunk continuity (the RTC family).** These methods overlap inference with execution and keep the committed prefix consistent.
   - Inference-time inpainting and guidance: RTC, ECG-RTC, SEAM.
   - Training-time prefix conditioning: training-time RTC, Soft RTC, Legato.
   - Noise selection: PAINT.
   - Native discrete-diffusion unmasking: DiscreteRTC.
   - Smoothing and fusion layers: VLA-RAIL, LiPo, GROOVE, ABPolicy.
   - Controlled comparisons: "Understanding Asynchronous Inference Methods" (2605.08168) and the Motubrain world-action-model deployment study (2608.01880). The latter found that timestamp alignment is the prerequisite for everything else.
2. **Delay and staleness compensation.** These methods predict the execution-time state or observation, or train on stale inputs.
   - VLASH (rolling the state forward), FutureRTC, F2F-AP (object flow), DA-DP (delay-conditioned diffusion policy).
   - DEFLECT (counterfactual preferences), Action ControlNet, RAPAC-DP (cloud delay), Streaming-WAM (committed-action-conditioned world model).
   - RL under random delays: DCAC, DEER, delayed-observation Dreamer, ARLI, Real-Time EXPO-FT.
3. **A fast low-level loop under a slow policy (dual-rate or hierarchical control).**
   - Slow VLM plus fast actor: HiRT, RoboDual, GR00T N1, DuoCore-FS, Fast-in-Slow, TIDAL, DAM-VLA, LAG-Fusion, SPARK-VLN.
   - Per-step residual correction: A2C2, VLA-Feedback (keeps the last denoising step for correction), πR² (a fresh proprioception channel every tick).
   - Onboard adapters under remote or cloud models: AsyncVLA, AsyncShield, VLA-ULAP, Speculative Policy Orchestration.
4. **Cutting reaction latency inside the sampler.**
   - Emitting near-term actions first: FASTER (horizon-aware schedule), Urgency-Aware Denoising, RAVEL.
   - Streaming generation: Streaming Flow Policy, Staircase Policy, FlashVLA, Reflex (ICML 2026), "Running VLAs at Real-time Speed".
   - Latency-bounded autoregressive decoding: 2606.13355.
5. **Reactive decoding and adaptive open-loop commitment.**
   - Test-time selection: BID, DREAM-Chunk.
   - Adaptive execution horizon: AutoHorizon, DVAC, A3, DEHP, BCP, attention-entropy truncation.
   - Analyses of when open-loop execution helps: 2608.15938 and the non-Markovian distribution-alignment work.
   - Robust ensembling: median temporal ensembling.
6. **Runtime monitoring and failure prediction.**
   - Learned probes on internal features: SAFE, VLA-FAIL, Hide-and-Seek, SAFECAST, AEGIS probe.
   - OOD detection plus uncertainty with conformal calibration: FIPER, FAIL-Detect, the uncertainty-aware latent safety filter.
   - Black-box action-space signals: Sentinel temporal consistency, ActProbe, Tri-Info, SafeContract (2605.28726).
   - Zero-cost flow-uncertainty proxies: denoising acceleration, velocity-field disagreement.
   - World-model and latent-prediction monitors: CheckVLA, ContactGuard, PATCH, Foresight, FARM.
   - Timeliness-aware metrics: AUCPDT and AUTC (RTCSA 2026).
   - Monitors run at control rate: RAPT at 50 Hz; RC-NF with under 100 ms response.
7. **Safety filters and shields for learned policies.**
   - CBF and QP filters on VLAs: AEGIS/VLSA with the SafeLIBERO benchmark, VLPSA, the attention-guided CBF filter, Acc-CBF-QP, SHIELD.
   - CBFs inside the sampler: Barrier-Enhanced Flow Matching, constricting barrier functions.
   - Reachability and latent filters: latent safety filters, LatentCBF, CrossSafe, language-conditioned filters.
   - Predictive and gameplay filters: Wabersich & Zeilinger, gameplay filter, PACS path-consistent braking.
   - Constraint-manifold layers: ATACOM for robot foundation models.
   - Anchors: the unifying survey (Hsu, Hu & Fisac) and CBF foundations (Ames et al.).
8. **Fallback, abstention and runtime assurance.**
   - Simplex-style switching: Neural Simplex, SOTER, SODA-MPC, the quadrotor OOD switch.
   - Rollback to safe checkpoints: SafeLoop (time-to-hazard), Rewind-IL.
   - Handing control to a stronger policy or a human: AEGIS backup reflex, AutoIntervene, ARMADA.
   - Precomputed semantic fallback sets: FORTRESS.
   - Conformal abstention and decision rules: BOKBO, conformal decision theory.
   - Safe-stoppability monitors for humanoid E-stop: Changliu Liu's lab.
9. **Timing guarantees and systems.**
   - Deadline-aware DNN scheduling on robots: RED (RTSS 2023 and its extension).
   - WCET-analyzable neural code: Designing NNs for Real-Time Systems; an allocation-free dual-number compiler for neural CBFs.
   - Serving with latency SLOs: Robion, Armory chunk scheduling, KerColle GPU concurrency.
   - Performance modelling and measurement: VLA-Perf, XPU characterization, the Offload-or-Overload measurement study.
   - Evaluation under configurable latency: ReflexBench, Kinetix.

## Key open problems

- **No latency-conditioned reporting standard.** Most papers report success at a few injected delays, measured in control steps and in simulation (Kinetix, LIBERO). Few report success against measured wall-clock latency distributions, jitter, or tail (p99) latency on real hardware. DA-DP and ReflexBench argue for doing this.
- **Monitors and filters have their own latency.** VLM checkers, resampling verifiers (RoboMonkey, Pre-VLA at about 184 ms per chunk) and world-model monitors add compute to the loop. How to budget safety compute inside a control period, and prove it fits, is largely open. Only a few papers (RAPT, RC-NF, the neural-CBF compiler) report monitor latency.
- **Open-loop chunks are a blind spot.** Committed actions execute without feedback. Fault injection (one-step perturbations, blank frames, frozen observations, SilentDrift backdoors, FreezeVLA) shows that timing faults and open-loop horizons interact. There are few formal bounds on how long a chunk can safely run open-loop.
- **Guarantees rarely survive composition.** CBF and reachability filters assume known dynamics and actuation limits (see the CBF-tautologies critique). VLA filters mostly handle collision geometry, while semantic, contact and dynamic hazards are left out. Guarantees across asynchronous hand-offs, where the filter acts on stale predictions, are rare.
- **Fallback design for generalist policies.** It is unclear when to stop, roll back, switch to a stronger or remote model, or ask a human, and how to calibrate those switches across open-ended tasks with little calibration data (CaB, BOKBO, AEGIS).
- **Certification.** Nobody has yet produced WCET or timing certification of billion-parameter VLAs on GPUs with non-deterministic scheduling. Existing timing-analysis work targets small networks or safety filters, not the policy itself.
- **Networked and shared inference.** Cloud and edge serving to fleets adds jitter and queueing delay (Armory, Robion, ComVLA). Onboard fallback adapters are promising, but they lack guarantees.

## 10 most important works

1. **Real-Time Execution of Action Chunking Flow Policies (RTC)**, Black, Galliker & Levine, NeurIPS 2025 (2506.07339), plus the PI blog post. It defined asynchronous freeze-and-inpaint execution for large VLAs.
2. **Training-Time Action Conditioning for Efficient Real-Time Chunking**, Black et al., 2025 (2512.05964). It removes the inference-time overhead of RTC and was validated on π0.6.
3. **Bidirectional Decoding (BID)**, Liu et al., ICLR 2025 (2408.17355). It set out the consistency-versus-reactivity tradeoff of action chunking and gave a closed-loop decoding algorithm.
4. **VLASH: Real-Time VLAs via Future-State-Aware Asynchronous Inference**, MIT Han Lab (2512.01031). It uses state roll-forward at no runtime cost and reports up to 11.8x lower reaction latency.
5. **Understanding Asynchronous Inference Methods for VLAs** (2605.08168). It compares IT-RTC, TT-RTC, VLASH and A2C2 head-to-head under controlled conditions.
6. **SAFE: Multitask Failure Detection for VLAs**, NeurIPS 2025 (2506.09937). It is a feature-based, conformally calibrated failure detector that generalizes to unseen tasks.
7. **FIPER: Failure Prediction at Runtime for Generative Robot Policies**, NeurIPS 2025 (2510.09459), together with **FAIL-Detect** (RSS 2025, 2503.08558). Both detect failures without failure data, using OOD scores and uncertainty with conformal guarantees.
8. **Sentinel: Runtime Monitoring of Consistency and Progress**, CoRL 2024 (2410.04640). It splits detection into fast statistical checks and slow VLM checks.
9. **The Safety Filter: A Unified View of Safety-Critical Control**, Hsu, Hu & Fisac, Annual Review 2024 (2309.05837), with **Control Barrier Functions: Theory and Applications**, Ames et al. 2019 (1903.11199). Together they are the conceptual foundation for filtering learned policies.
10. **VLSA/AEGIS + SafeLIBERO** (IROS 2026, 2512.11891), with **VLPSA** (2609.22462) and **PACS** (ICRA 2026, 2511.06385). These are real-time CBF and reachability safety filters built for VLA and diffusion policies.

Honorable mentions:
- A2C2 (2509.23224), πR² (2607.26055), FASTER (2603.19199) and AsyncVLA (2602.13476) for fast reactive layers under slow models.
- RAPT (2602.01515), SafeLoop (2609.26313) and FORTRESS (2505.10547) for control-rate monitoring and fallback.
- The neural-CBF WCET compiler (2604.23995) and RED (RTSS 2023) for timing guarantees.
