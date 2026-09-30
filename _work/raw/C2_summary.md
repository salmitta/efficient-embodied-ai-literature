# C2 — Compression for robot foundation models: cluster summary

130 verified records (16 are foundational LLM/diffusion techniques). Almost all VLA-specific compression work is from 2025–2026. Token pruning and few-step samplers without distillation were left to C1. Runtimes and accelerators that only execute quantized models are tagged C2+C5.

## Technique families

1. **Post-training quantization (PTQ) of VLAs.** This is the busiest area. It started with OpenVLA's 4-bit inference result (same real-robot success at about 7 GB instead of 16.8 GB). It then split into several lines:
   - *Action-centric sensitivity allocation*: QVLA assigns bits per channel from action-space sensitivity and treats 0-bit as pruning. ActQuant uses action-guided curvature to reach 2.5–3 bpw. Mix-QVLA uses task-evidence maps.
   - *Temporal / closed-loop awareness*: DA-PTQ targets kinematic drift. DyQ-VLA switches bit-width at runtime using kinematic proxies.
   - *Rotation/outlier methods for W4A4*: HoloQ-VLA and FoldQuantVLA build on QuaRot/SpinQuant-style Hadamard transforms.
   - *Quantizing the diffusion/flow action head*: QuantVLA, HoloQ-VLA.
   - *Binarization*: HBVLA does 1-bit PTQ.

   Many papers use AWQ, GPTQ and SmoothQuant as baselines. These are frequently shown to fail on VLAs, e.g. QVLA reports +22.6 pts over SmoothQuant.
2. **Quantization-aware training and native low-bit models.** Examples: QAIL and SQIL (saliency-weighted QAT, 4-bit, measured on an edge GPU); BitVLA (native ternary weights on BitNet b1.58 2B4T, plus Quantize-then-Distill for the vision encoder); DC-QFA (a device-conditioned QAT and NAS supernet).
3. **Quantizing world-action models (WAMs).** Q-WAM keeps an action-subspace 16-bit low-rank branch. QuantWAMs calibrates at the granularity of model structure, rollout distribution and task. PreDE predicts task degradation offline. QuantWM applies 2-bit KV-cache quantization to video world models.
4. **Weight/structured pruning and recovery.** GLUESTICK finds that LLM-style pruning breaks VLAs and raises safety violations, then recovers them with a training-free weight-space correction. RLRC does prune → SFT+RL recovery → quantize. Offline hidden-state distillation recovers 63–87% width-pruned backbones. EcoVLA does adaptive channel pruning. LightDP prunes diffusion-transformer denoisers.
5. **Depth reduction, layer skipping and early exit.** Redundancy analyses (Drop-Then-Recovery, CKA twin-layer removal, VLM-to-VLA divergence) find language backbones highly redundant, while vision and action pathways are fragile. Dynamic methods: DeeR-VLA, MoLe-VLA, DySL-VLA, AC²-VLA, decoupled early exits for flow VLAs, DeeAD for driving, DynaNav for navigation. EfficientVLA combines layer pruning with other training-free tricks.
6. **Knowledge distillation into compact students.**
   - Layer distillation: Shallow-π goes from 18 to 6 layers, runs on Jetson Thor, and is tested on humanoids.
   - Large-to-tiny distillation: VLA-AD produces a 158M student at 12.5 Hz; XS-VLA and CoTinyVLA give sub-1B VLAs spatial and CoT supervision; ActDistill adds a routed student.
   - RL-based distillation into experts: RPD, SymVD.
   - Representation distillation from world models or vision foundation models: Theia, X-Distill, eVGGT, "Think Like a World Model".
7. **Step distillation of diffusion/flow policies.** Consistency Policy, OneDP, SDM, ManiCM, VDD (mixture of experts), SnapFlow and OFP (1-NFE for π0.5/SmolVLA), and WAM one-step distillation (DIDO, WAM-OPD). There is also runtime sparsity in diffusion policies (SAG, test-time sparsity).
8. **Compact-by-design alternatives** (partly C1): TinyVLA, SmolVLA, NanoVLA, TurboVLA, PocketDP3, and MINERVA (0.54M parameters, 95% on LIBERO).
9. **Deployment runtimes for compressed models** (C5 overlap): vla.cpp (ternary tensor-core kernel for BitVLA on an 8 GB Orin Nano), Embodied.cpp, vla.simd (int8 on a Raspberry Pi 5), llama.cpp/GGUF pipelines (LiteVLA-Edge, EdgeVLN), TensorRT INT8 ACT on an Orin Nano, and FP8/NVFP4 π0.5 on Jetson Thor.

## Key open problems

- **Open-loop fidelity does not predict closed-loop success.** A distilled Octo passes every offline check and then gets 0/72 in closed loop. VLAQuantBench shows recipe-dependent failures, e.g. rescuing OpenVLA-OFT by protecting a single 28K-parameter projection. Cheap predictors of degradation such as PreDE are only a start.
- **Compression vs. generalization/robustness.** Most results are on LIBERO, which MINERVA shows can be solved by tiny models through memorization. Evidence that compression hurts under distribution shift comes from Recti-Q (the PTQ robustness gap), LIBERO-Plus collapse, and GLUESTICK (more safety violations). Systematic OOD and real-robot evaluation of compressed VLAs is still rare.
- **Where to spend bits.** Action heads and projectors are sensitive while language backbones are redundant. Good allocation depends on task phase and denoising step. There is no consensus on per-module or per-timestep precision for flow/diffusion heads, or for world-action models with MoE experts.
- **Real speedups vs. nominal compression.** Many papers report memory savings but only 1.2–1.5x latency gains. "Embodied efficiency" studies (task time, motion energy, the speedup paradox) show that per-step savings can be cancelled by extra steps or worse motion. Native low-bit kernels on robot SoCs (ternary, W4A4, NVFP4) are still immature, and artifact audits show some "INT8" exports are actually FP32.
- **Recovery cost.** RL-based recovery (RLRC) needs hundreds of GPU-hours. Offline and training-free recovery (hidden-state distillation, GLUESTICK) is promising but has only been shown on a few backbones.
- **Security and safety of quantized weights.** A few gradient-chosen bit flips in INT8 VLAs can reduce success to zero. Robustness certification for compressed policies is open.
- **Composability.** Quantization and token pruning conflict unless co-designed (SQAP-VLA). How PTQ, depth pruning, step distillation and async inference stack together is largely unmeasured.

## 10 most important works

1. **OpenVLA** (2406.09246): base model for nearly all VLA compression work; first evidence that 4-bit inference preserves real-robot success.
2. **BitVLA** (2506.07530): first native 1.58-bit VLA; 11x memory and 4.4x latency reduction vs OpenVLA-OFT.
3. **QAIL** (2412.01034), with its follow-up SQIL (2505.15304): first QAT framework for imitation-learning/VLA policies, with edge-GPU speed and energy measurements.
4. **QVLA** (2602.03782): action-centric channel-wise bit allocation that unifies quantization and pruning; clearly beats LLM PTQ baselines.
5. **HoloQ-VLA** (2605.28803) / **FoldQuantVLA** (2609.24433): uniform W4A4 across backbone and diffusion head; FoldQuantVLA runs natively on Jetson Orin and is tested on real robots.
6. **RLRC** (2506.17639): systematic VLA compression study and prune → recover → quantize pipeline (8x memory reduction).
7. **Don't Run with Scissors / GLUESTICK** (2510.08464): shows pruning breaks VLAs and raises safety violations; training-free recovery.
8. **Drop-Then-Recovery** (2606.27755): shows VLA language backbones are highly redundant while vision and action paths are not; points compression at the right modules.
9. **Shallow-π** (2601.20262): depth distillation of flow VLAs with onboard Jetson Orin/Thor deployment on humanoids.
10. **Consistency Policy** (2405.07503) / **OneDP** (2410.21257): foundational distillation of diffusion policies into one-step students (OneDP: 1.5 Hz → 62 Hz).

Also worth reading: **VLAQuantBench** (2609.25376) and **Anatomy of a Closed-Loop Collapse** (2609.23048) on how to evaluate compressed policies.
