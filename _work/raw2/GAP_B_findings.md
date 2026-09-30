# GAP_B findings: interrupting and certifying open-loop action-chunk execution, plus the 2026 recency sweep

Scope: 63 queries (36 on chunk interruption/certification, 27 recency-sweep queries), all run against the arXiv export API and OpenAlex. 283 new records went to `GAP_B.jsonl`, all verified from fetched abstracts. IDs marked **(new)** are in GAP_B.jsonl. Other IDs are already in `existing_items.tsv`. I did not re-fetch those this round, so they are described from their titles and cited only for how they fit the picture.

## 1. The problem

A chunked policy (ACT, pi0/pi0.5, GR00T, WAMs) commits to H actions from a single observation. During those H steps the robot runs open loop, or close to it. Four questions follow:
- **When do you stop a chunk?** This is interruption, truncation, or an adaptive horizon.
- **What can you check before a chunk runs?** This is certification: of the chunk itself, of the policy over a set of inputs, or of the closed loop.
- **How do you fix a chunk while it runs?** This is closed-loop correction under the chunk.
- **Can you bound the time it takes to produce the next chunk?** This is WCET and scheduling. Every interruption scheme assumes a replacement chunk arrives before the old one runs out.

## 2. What the literature offers, by mechanism

### 2a. Learned or statistical triggers for truncation and replanning. This is the most active area.
- **Disagreement between samples.** TDHD **(new, 2608.09125)** compares two noise-perturbed flow samples and truncates the chunk with a dual threshold. It is evaluated on real surgical hardware (tissue success 55% -> 80%). KeyStone **(new, 2605.08638)** uses the geometry of K parallel samples at no extra wall-clock time, because diffusion inference is memory-bound. Related existing work: Bidirectional Decoding (2408.17355), GeoAAC (2609.20776), Knowing When to Stop (2609.00908), Adaptive Action Chunking (2604.04161), Dynamic Execution Horizon Prediction (2606.11408), and VLA-Corrector adaptive horizon (2607.01804).
- **Checking the imagined future against reality in WAMs.** This is the strongest quantitative evidence for verified adaptive execution. FFDC **(new, 2605.06222)** continues a WAM plan only while a lightweight verifier finds predicted dynamics consistent with what is observed. It cuts planning calls by 69-74% and completion time by 34-51%, including on a Unitree G1D. World-Coherent Decoding **(new, 2609.02159)** learns an online reliability predictor from imagination-reality mismatch. SANTS **(new, 2605.27947)** learns when to stop video denoising, cutting latency by about 80%. Existing work in the same family: CheckVLA (2607.26789), ContactGuard (2608.13438), Pre-VLA preemptive runtime verification (2605.22446), and Foresight (2606.23085).
- **Learned query and horizon scheduling.** EQRL **(new, 2606.14375)** picks chunk length and denoising budget per query using critic-ensemble disagreement. SparkVLA **(new, 2608.16172)** ranks "stop" against every executable prefix length in one decision. Event-triggered asynchronous inference (2609.22587) is the existing counterpart.
- **Progress and commitment gating.** AGM **(new, 2608.29537)** advances only after a physically verified achievement, using a 2.43M-parameter head. CommitFlow **(new, 2609.21908)** holds back dependent actions until stage commitments are met (+22.7 points over pi0.5 on RoboTwin 2.0). Stage-aware verifiers appear in VLA-Corrector (2609.06508), CARE (2609.24118), and ActionGround (2609.33256, under 1 ms overhead).
- **Failure detectors as interrupt signals.** New: FailureSpot (timestamp-level, per chunk, 2609.04277), FabriMAE attention-entropy self-evaluation (2608.16697), zero-overhead attention-head deviation monitors (2603.13782), and Sentinel-VLA (2605.01191). Existing: SAFE (2506.09937), FIPER (2510.09459), consistency/progress monitoring (2410.04640), VLA-FAIL (2606.21386), SAFECAST (2608.04246), Hide-and-Seek (2605.30834), RoboMonitor (2609.30715), and ActFovea (2607.29169).
- **Interrupts from humans or new instructions.** VITA-E **(new, 2510.21817)** runs Active and Standby VLA instances so a spoken instruction can interrupt ongoing actions. SwitchVLA **(new, 2506.03574)** handles instruction changes mid-execution. This is the only line where "interrupt" is the explicit design target.

### 2b. Correction during and between chunks. This area is mature and mostly empirical.
- **Stitching at chunk boundaries.** The existing RTC family dominates: 2506.07339, 2512.05964, 2605.25537, ECG-RTC (s2-ecg-rtc-2026), native continuation (2602.12978), autoregressive real-time execution (2606.13355), πR² (2607.26055), and asynchronous distribution alignment (2609.36540). New work adds POTR trust-region guidance (2605.24433), ChunkFlow's frozen/editable/future zones (2607.12992), and SMILE's B-spline chunks (2608.29432).
- **Fast residual correction under a slow chunk planner.** Reactive Diffusion Policy **(new, 2503.02881, seminal slow-fast)**, PhaForce (2603.08342), ACPPO-Corr's stepwise within-chunk corrector (2609.36250), and RTCF's frequency-domain correction (2608.04527). Existing work in the same spirit: Leave No Observation Behind (2509.23224), TacForcing (2608.25798), and DREAM-Chunk (2606.18589).
- **Latency compensation.** AHEAD **(new, 2606.02486)** forecasts future VLA patch tokens with a 4.9M-parameter latent world model and stops its horizon when prediction uncertainty rises. This handles the mismatch between observation time and execution time.

### 2c. Safety filtering applied to the whole chunk, not just the next action
- Most classical CBF filters are **myopic**: they act only on the next action. Two lines of work extend the filter across the horizon:
  - **Predictive and multi-step filters.** Predictive safety filter (existing 1812.05506; new racing variant 2102.11907), multi-step MPSF that corrects over a horizon to reduce chattering **(new, 2309.11453)**, uncertainty-aware PSF with NN ensembles (2604.26836), and BarrierFormer's rollout-level barrier supervision (2609.23896, CoRL 2026).
  - **Constraints enforced inside trajectory generation.** SafeDiffuser (2306.00148), SafeFlowMatcher, which proves a barrier certificate on the executed path (2509.24243, ICLR 2026), Constrained Diffusers (2506.12544), D-SafeMPC (2607.10842), and, closest to VLAs, **neuro-symbolic constrained flow matching** (2607.01378). That last one corrects the whole predicted VLA trajectory during denoising and reaches 82.8% collision avoidance on SafeLIBERO versus single-step filters. Existing: barrier-enhanced flow matching for VLAs (2607.29569), VLSA constraint layer (2512.11891), path-consistent safety filtering for diffusion policies (2511.06385), constricting barrier functions (2602.21429), and VLPSA (2609.22462).
- **Latent-space filters for pixel policies.** These are all existing items: latent reachability (2502.00935), latent CBFs (2511.18606, 2507.13871), AnySafe (2509.19555), CrossSafe (2609.28984), and language-conditioned latent filters (2608.00315). This is the only route so far to a safety-filter-style guarantee on image-conditioned VLA behavior, and the guarantee holds only relative to a learned latent model.

### 2d. Formal and statistical certification
- **Verifying closed-loop NN controllers (seminal to 2026).** Reluplex (1702.01135), Verisig (1811.01828), ReachNN (1906.10654), NNV (2004.05519), Reach-SDP (2004.07876), POLAR / POLAR-Express (2106.13867, 2304.01218), beta-CROWN (2103.06624), Marabou 2.0 (2401.14461), VNN-COMP 2025 (2512.19007), and the ACC-2026 alpha-beta-CROWN control tutorial (2605.26577). For image inputs, the practical workaround is to verify through a surrogate generator (GAN/cGAN/VAE: 2105.07091, 2405.18554, 2501.14009). **These tools scale to small MLP controllers, not multi-billion-parameter VLAs.** Exact reachability for ReLU NN control systems is **undecidable** even with trivial plants (2407.04988).
- **Closest to certifying a VLA or visuomotor policy.**
  - *Probabilistic reachable-action verification* **(2608.02545)** freezes the visual encoder and propagates zonotopes through the low-dimensional policy interface. It then conformally calibrates a reachable-action radius under camera-pose perturbation.
  - *Region-level robustness validation of five VLAs* (GR00T, OpenVLA, pi) **(2609.22293)** is sound over continuous perturbation regions rather than samples. Commanded actions change under rotations as small as ±1°. This is direct evidence that per-input certification of VLA chunks is currently fragile.
  - *CertVLA* **(2608.20791)** gives certified robustness of continuous VLA actions to bounded patch attacks, lifted to whole rollouts.
  - *Certifying Plans under Model Mismatch* **(2608.02453)** addresses certifying a fixed action chunk before execution. It proves a trilemma: with scarce target-system data, no sound certifier can keep uniform containment, finite tube width, and unrestricted model error all at once. A Lipschitz-type assumption is unavoidable.
  - Existing: deterministic world models for closed-loop reachability of vision-based control (2512.08991), and "No Free Checker" verifier survey (2609.09250).
- **Conformal and statistical routes, which are what is actually deployable.** KnowNo (2307.01928, seminal), conformal decision theory (existing 2310.05921), FabriVLA conformal chunk uncertainty (existing 2607.08575), ReconVLA (2604.16677), FIDeL (2604.13788), conformal reachability (2602.03799), ensembles of learned HJ filters with CP (2511.07899), CBVF under partial observation (2608.13819), cost-aware ACI for runtime assurance (2605.24463), and conformal policy control (2603.02196, ICML 2026). Existing: learned safety filters with ACI (2604.18482), conformal robust MPC from pixels (2606.15594), and risk-aware online conformal state probing (2609.25889).

### 2e. Runtime assurance (Simplex) wrapped around learned policies
- **Classical Simplex:** Neural Simplex (existing 1908.00528), SOTER (existing 1808.07921), Black-Box Simplex (2102.12981), Bb-Simplex (2202.09710), optimal RTA via RL (2310.04288), RTD-RAX certify-and-repair (2603.21635), online POLAR-Express switching on a Turtlebot (2408.08592), and Synergistic Simplex (existing 2605.08190).
- **Two 2026 results matter specifically for chunked VLAs:**
  - **Generator-Independent Runtime Assurance (2609.06036).** Certifying each candidate separately does not compose under best-of-k or retry sampling: the false-admission rate grows to 1-(1-α)^k. Only certifying the admissible set simultaneously keeps the guarantee independent of the generator. This applies directly to the sample-then-verify pipelines now common for VLAs, such as ADV 2603.18091, CoVer 2602.12281, RoVer 2510.10975, UF-OPS 2603.10282, and existing RoboMonkey 2506.17811.
  - **Conformal recovery-deadline certificates (2606.25371).** A latching Simplex trip suppresses a controller that could have recovered. A split-conformal bound on recovery time licenses a delayed fallback, backed by a verified hard limit. This is the right shape of rule for "let the chunk finish or cut it now".
- **Surveys and agendas:** the community agenda from testing to formal verification (2606.03593), a position that task success cannot verify physical reasoning in VLAs (2606.30686), and, existing, silent failures and runtime action authorization (2606.00090) and formal methods for robot policy learning (2602.06971).

### 2f. Timing: can the next chunk be guaranteed on time?
- Real-time systems work on DNN inference shows that inference time varies widely, and it attributes the variation to data, I/O, model, runtime, hardware, and pipeline effects (2209.05487). GPUs lack analyzable preemption. Mitigations include GCAPS driver-level preemption with response-time analysis (2406.05221, 2401.16529), Reef microsecond kernel preemption (TOCS 2025), RT-Gang one-gang-at-a-time scheduling for tight WCET (1903.00999), DART and LaLaRAND CPU/GPU real-time DNN scheduling (RTSS 2019/2021), ML-based GPU WCET estimation under MPS (IEEE Access 2024), MAST response-time analysis for GPUs (JSA 2024), and feedback-control GPU scheduling that avoids WCET estimates entirely (FC-GPU, TECS 2025). Buttazzo's invited paper (NG-RES 2022) and the RTS 2025 perspectives frame the gap. Existing: 2008.11830, RED (2308.15368, 2605.24044), SlackDrive (2609.28064), and chunk scheduling for batched serving (2608.00337).
- **No paper found in this sweep derives a WCET or response-time bound for a VLA or WAM inference pass on an embedded GPU (Jetson/Orin).** Robotics papers report mean latency or Hz, for example RhinoVLA at 11.69 Hz on an edge SoC (2606.07383), AquaWAM at 2.7x faster on AGX Orin (2609.33299), and IMLE-VLA at 55 Hz versus 15 Hz (2609.10915). None report tail or worst-case numbers.

## 3. Best evidence to date
1. **Verified adaptive execution in WAMs** (2605.06222). Its verifier cuts replanning calls by ~70% and also improves success, on sim and a real humanoid.
2. **Sample-divergence truncation on real surgical hardware** (2608.09125).
3. **Horizon-level safety enforcement inside VLA flow denoising** (2607.01378). It clearly beats next-action-only filters on SafeLIBERO. SafeFlowMatcher (2509.24243) is the version with a proof, for planners.
4. **The theoretical limits:**
   - setwise versus per-candidate certification (2609.06036);
   - the chunk-certification trilemma under model mismatch (2608.02453);
   - undecidability of NNCS reachability (2407.04988);
   - ±1° fragility of VLA actions under sound region validation (2609.22293).
5. **Conformal calibration layered on set propagation through a low-dimensional policy interface** (2608.02545). This is the most plausible template for certifying real visuomotor policies today.

## 4. What remains open
- **No certificate for a VLA chunk as a whole.** Existing guarantees fall into three kinds:
  - statistical (conformal coverage of a failure score or radius);
  - relative to a learned latent model (latent CBFs and HJ reachability);
  - limited to small controllers (formal NN verification).
  No work bounds the physical trajectory a pi0-class chunk induces over its execution horizon.
- **Certificates do not compose with how VLAs are sampled.** Sampling, reranking, and retrying break per-candidate guarantees (2609.06036). Almost no VLA verifier paper accounts for this.
- **Choosing chunk length is not tied to safety.** Adaptive-horizon methods optimize success or compute (EQRL, SparkVLA, and existing 2606.11408 and 2609.00908), not a certified bound. No work links execution horizon H to a reachable-set or CBF margin.
- **Interrupt latency is unmeasured.** No paper reports the time from a trigger (monitor, human, collision risk) to a safe stop or replacement chunk on embedded hardware. VITA-E and SwitchVLA focus on behavior, not timing.
- **Timing guarantees are missing for foundation-model inference.** No WCET or response-time analysis exists for transformer/diffusion VLA inference on Jetson-class GPUs. There is also no analysis of how asynchronous RTC-style pipelines behave when inference overruns its deadline.
- **Calibration under shift.** Conformal monitors assume exchangeability. Online and adaptive CP exists (2605.24463, 2410.08852, existing 2604.18482), but it has not been evaluated on VLA chunk streams with long-horizon drift.
- **Evaluation.** Task success cannot distinguish physical competence from semantic matching (2606.30686). Safety benchmarks for VLAs, such as SafeLIBERO and existing ForesightSafety-VLA 2606.27079, do not report interrupt timing or certificate tightness.

## 5. Recency sweep (2026)
- **Scale.** 184 of the 283 new records came from the recency sweep, sorted newest first and paged until a page gave fewer than 2 new items or dates fell into 2025.
- **Clusters that did not saturate:**
  - **World-action models (C8).** New efficient WAMs appear weekly: SANTS, DeltaWAM, Adaptive-WAM, GigaWorld-Policy, SimWAM, DELE, Next Forcing, RoboActualizer (60M parameters, 39 ms), AquaWAM on Orin, ZimaBlue at 30 Hz, and the WAM survey (2606.20781). The shared trend is to generate less future (latent, delta, or optional video) at inference.
  - **Adaptive-compute and one-step VLAs (C1).** ElegantVLA (13.8 -> 26.3 Hz real), IMLE-VLA (55 Hz), ProbeFlow (14.8x action-head speedup), RD-VLA, SMILE, and BLUE/TOWN-style gating of when to reason.
  - **Efficient VLA RL post-training (C3).** RL Token, OTQL (RL plus a 70% step reduction), QPILOTS, FORCE, D-VLA systems, and ProphRL.
  - **Token pruning (C2).** The 2026 items are driving and multi-modal variants: tri-stage 2D/3D pruning, ETA-VLA, and ThinkProprio. The recency queries also surfaced 2025 gaps missing from the DB: SpecPrune-VLA (2509.05614), BAC diffusion-policy caching (2506.13456), Oat-VLA, ContextVLA, FastDriveVLA, CronusVLA, and DiffusionDrive.
- **Clusters that did saturate.** Queries on VLA weight quantization, MoE/early exit, speculative decoding, and continual learning returned almost nothing not already in the DB (0-1 new items each).
- **Edge runtimes.** Only a few new explicitly on-device items: RhinoVLA on the Huixi R1 SoC, GigaBrain-0-Small on Orin, HoloBrain-0 at 0.2B, and AURA constant-VRAM memory aimed at edge flash endurance. The DB already covers vla.cpp and Embodied.cpp.
