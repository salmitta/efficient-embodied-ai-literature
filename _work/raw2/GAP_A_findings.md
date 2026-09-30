# GAP_A findings: questions 1-4

The database already covered these questions well. Most of the arXiv queries returned items it already held (see the search log). The new items that add the most are measurements from practitioners (GitHub issues and repos, the archived NVIDIA tutorial) and foundational or methodology papers from outside robotics. Existing items are cited by id. Items added in this pass are marked [new].

---

## Q1. Do efficiency techniques compose?

**What the literature says**
- Composition is common, but it rarely multiplies cleanly. EfficientVLA (2506.10100) combines three reductions: language-layer pruning, token selection and action-head caching. FLOPs drop to 28.9%, but the speedup is only 1.93x. Think Twice, Act Once (2505.21200) combines action reuse with token pruning: 55.7% fewer FLOPs gives only 36.0% lower latency. The FLOP savings are much larger than the latency savings, so the parts are not additive.
- Some combinations fail when applied naively. SQAP-VLA (2509.09090) reports that token pruning and quantization are incompatible when stacked directly, and designs quantization-aware pruning criteria to fix it. RLRC (2506.17639) uses a prune, then SFT+RL recovery, then quantize order. It reaches 8x memory and 2.3x speed, which shows the order matters and a recovery step between stages is needed. QVLA (2602.03782) merges pruning into mixed precision by allowing 0-bit channels.
- The LLM literature makes this formal. Sparsity and quantization are provably non-orthogonal: errors compound, and quantizing before pruning corrupts the importance scores ([new] 2405.20935). Speculative decoding (EAGLE-2 tree verification) cancels out the memory-bound gains of 4-bit weights, and a hierarchical fix recovers 2.78x ([new] 2505.22179). QSpec ([new] 2410.11305) and SpecQuant show pairings designed to compose. Deep Compression ([new] 1510.00149) is the canonical stacked pipeline, with retraining between stages. LLM-KICK ([new] 2310.01382) warns that proxy metrics such as perplexity hide the damage done by compression. This is the LLM analogue of VLAs passing offline checks but failing closed-loop (2609.23048).
- Systems-level stacking composes more predictably. In RLDX-1 ([new] 2605.03269), CUDA Graph capture gives about 1.45x, and kernel fusion on top brings it to 1.63x (71.2 to 43.7 ms p50 on an RTX 5090). SpecPrune-VLA ([new] 2509.05614) adds 1.32x on top of FlashAttention (A800) and 1.42x when combined with action-expert caching. GigaBrain-0-Small ([new] 2510.19430) stacks a smaller backbone, removed transfers, cached RoPE tables and torch.compile. On AGX Orin it gets about 10x lower latency than pi0 (0.13 s vs 1.28 s) at equal success on one task.
- Chunking, asynchrony and compression do combine in practice. Jetson-PI (2607.12659) combines async foresight, scheduling and CUDA optimizations for 8.66x control frequency on Orin. FoldQuantVLA (2609.24433) runs native W4A4 TensorRT on Orin.

**Best evidence**
- 2405.20935: theory and experiments.
- 2509.09090 and 2506.17639: VLA stacking ablations.
- 2609.25376 (VLAQuantBench): outcomes depend on how layer scope, format and calibration interact.
- 2609.37771: accelerator benchmarks have bugs that can flip method rankings.
- 2609.10550 [new]: cross-layer interactions mean no single-layer analysis predicts deployment outcomes.

**What remains open**
- No study stacks all of quantization, distillation, pruning, token reduction, caching and chunking/async on one VLA and reports closed-loop success plus wall-clock time on one device, with each factor ablated.
- There are no interaction terms (for example, whether quantization error grows under async/RTC inpainting, or with token pruning plus chunk reuse).
- No study checks whether the order effects from 2405.20935 carry over to flow/diffusion action heads.

---

## Q2. Total cost of ownership: fleet-scale onboard vs. cloud inference

**What the literature says**
- There is no robotics-specific TCO or $/robot-hour study. The closest evidence comes from serving systems and measurement studies:
  - ROSA (2607.01088): up to 12.06x factory productivity from shared GPU serving, plus battery benefits.
  - Robion (2609.12075): 64 robots on 4 GPUs at 98% SLO, 6.7x the robot load of vLLM-Omni.
  - Kairos (2605.11381) and Action Chunk Scheduling (2608.00337): chunk-aware batching gives +18% throughput.
  - Offload or Overload (2603.18284) and the MSR blog (msr-offloaded-inference-blog-2026): small onboard GPUs cannot run the full stack, and large ones drain the battery up to 160% faster.
  - FogROS2-Config (2311.05600): up to 20x cloud cost reduction by choosing the right instance type.
  - 2501.14823: analytical hybrid edge-cloud savings.
- Onboard power budgets:
  - [new] 10.1109/mm.2022.3219803 (Data Centers on Wheels) is the only fleet-scale onboard-compute model found. It says onboard compute must stay under 1.2 kW per vehicle at 95% adoption, and hardware efficiency must double every 1.1 years. The framing transfers to humanoid fleets.
  - [new] 10.1145/3173162.3173191 (ASPLOS 2018): power, thermal and tail-latency constraints for onboard compute.
  - [new] 10.1109/iros51168.2021.9635877: joint DVFS and motor control saves 30-50% of battery energy, so compute and locomotion energy interact.
  - [new] 10.1109/ecti-con64996.2025.11100596: measured component power of a humanoid, with compute as a major load.
  - Energy per inference for VLAs on AGX Orin: 10.1145/3797248.3815411.
  - Device-edge energy-optimal splits: EcoVLA (2608.15502).
- General TCO methods that could be adapted, tagged foundational: [new] 2502.01070 (TCO is driven by thin-GEMM/decode utilization, not peak FLOPs, which matches batch-1 robot decode) and [new] 2509.02596 (a levelized cost-per-inference metric).
- Cost-accuracy decision framing: [new] 2108.01235 (when to call a cloud GPU model).
- Composite-model serving: [new] 2606.12688 (M*).

**Best evidence**
- 2607.01088 and 2609.12075: fleet GPU sharing, reporting throughput and SLOs but not dollars.
- 2603.18284: onboard vs. edge vs. cloud measurements.
- 10.1109/mm.2022.3219803: fleet energy framing.

**What remains open**
- No paper puts a dollar figure on onboard hardware (for example Orin or Thor capex and energy) against cloud GPU-hours per robot, including network cost, utilization and duty cycle.
- No measured humanoid compute share of the battery budget for VLA workloads.
- No study of how batching gains (2608.00337) change the break-even fleet size.
- Nobody has measured whether cloud serving's higher throughput per GPU outweighs the success loss from latency (compare DeDelayed 2510.13714, RTC 2506.07339).

---

## Q3. Comparable efficiency evaluation across hardware

**What the literature says**
- The robotics VLA literature mixes incompatible metrics: chunk rate, closed-loop Hz, relative speedup and throughput. Reported speeds are not reproducible across setups. In OpenVLA issue #66 ([new] github-openvla-issue-66-rtx4090-hz), different users get 4.4 vs 6.02 actions/s on the same RTX 4090 class, and 2.06 on an A6000.
- Some existing works do profile across hardware:
  - 2604.24447: a cross-XPU leaderboard scored by cost, energy and time.
  - 2509.11480: power-capped Jetsons vs. datacenter GPUs.
  - 2603.02271: action generation is memory-bound on Orin and Thor.
  - 2605.30571: batch-1 decode reaches a smaller fraction of bandwidth on faster GPUs.
  - 2608.25053 (Hydra) and 2607.08029: quantization does not reduce power monotonically, and INT4 decode can be slower.
  - 2608.00927 (AgriJetsonBench): internal Jetson power telemetry is biased, so it uses external power logging.
  - 2605.29710 (PhAIL): distributional time-to-success with confidence intervals.
- vla.cpp (2606.08094) now publishes a near-MLPerf-style protocol in its repo benchmark docs. The protocol is 3 warmups plus 20 reps across 3 processes, with min/mean/p50/p90 latency and peak RSS, for 13 VLAs on AGX Orin, Orin Nano Super, RTX 3060/3090/5090, Intel and Snapdragon. Examples on AGX Orin: OpenVLA-OFT BF16 p50 385 ms with 15.4 GB RSS, and pi0.5 353 ms with 6.0 GB. It also states that success rates at default flags do not carry over to faster flag sets.
- New methodology items:
  - [new] 2509.20189 (Pagoda): time and energy rooflines for Orin across power modes. MAXN is not the most energy-efficient mode.
  - [new] 2606.26383 (SOLAR): automated speed-of-light bounds, including robotics workloads.
  - [new] 2609.10550: an evidence protocol requiring hardware, software versions, batch semantics and thermal state.
  - [new] 2309.09212 (RobotPerf): vendor-agnostic ROS 2 benchmarking.
  - MLPerf family: 1911.02549 and 2510.27065 were already present. [new] 2410.12032 (MLPerf Power), 2106.07597 (MLPerf Tiny) and 2012.02328 (MLPerf Mobile) were added.
  - [new] 2403.12844 (MELT): energy and thermal behavior for sustained on-device transformer inference.
  - [new] 2604.17040: measured sparsity yields no Jetson latency or energy gain because inference is launch-dominated.
  - [new] github-openvla-serve-roofline: OpenVLA decode runs at 16.33 ms/token against a 15.6 ms/token HBM floor on an L40S, which leaves only about 7% for fusion or CUDA graphs.

**Best evidence**
- 2606.08094 (vla.cpp benchmark protocol and multi-device tables).
- 2410.12032 (energy measurement rules).
- 2509.20189 (roofline normalization on Jetson).
- 2608.00927 (external power measurement).

**What remains open**
- There is no agreed VLA benchmark that jointly reports closed-loop success, end-to-end perception-to-actuation latency distribution (p50/p99) and energy per action at a fixed power mode across devices.
- There is no standard hardware-normalized metric for VLAs, such as fraction of roofline or bandwidth floor achieved, or success per joule.
- p99 or tail latency is almost never reported for VLAs. Of the works found, only LA-IMR (2505.07417) and Kairos (2605.11381) target tail latency or SLOs.

---

## Q4. Can OpenVLA-7B-class models fit 16 GB Jetsons without losing LIBERO success?

**What the literature says**
- Memory: the OpenVLA paper (2406.09246) reports 16.8 GB (bf16), 10.2 GB (int8) and 7.0 GB (int4). At int4 it matches bf16 on BridgeData real-robot success (71.9%), on RTX 4090/A5000, not Jetson. Maintainers say a 16 GB GPU is needed for bf16 and about 6 GB for int4 ([new] github-openvla-issue-152-gpu-size).
- Independent measurements ([new] github-openvla-compat-vla-lite): peak memory is 15.29 GB for bf16, 8.05 GB for int8 and 4.60 GB for nf4. Latency does not improve (nf4 245 ms, int8 422 ms, bf16 260 ms). nf4 flips the gripper on 2 of 16 frames. No LIBERO closed-loop run was done.
- A 16 GB Orin NX is tight at bf16. vla.cpp measures OpenVLA-OFT BF16 at 15.4 GB peak RSS on AGX Orin, and no Orin Nano entry exists for it. The openpi community reports OOM for pi0 or pi0.5 on Orin NX 16GB and about 1 s per inference on AGX Orin 64GB ([new] github-openpi-issue-386-jetson-orin). GigaBrain-0 ([new] 2510.19430) measures pi0 at 17.5 GB and 1.28 s on AGX Orin.
- On-Jetson measurement of OpenVLA-7B ([new] jetson-ai-lab-openvla-tutorial), on AGX Orin 64GB with MLC:
  - Latency: FP16 840 ms, FP8 471 ms, INT4 336 ms (2.97 FPS).
  - Fine-tuned MimicGen stacking success: 86%, 85% and 84% respectively.
  - The tutorial lists Orin NX 16GB as supported but gives no numbers for it.
- LIBERO success under 4-bit: several works claim little or no loss, but mostly on datacenter GPUs or with simulated quantization.
  - ActQuant (2605.24011): 95% retained at 3 bits per weight or less, backbone 14.3 GB down to 2.7 GB.
  - Mix-QVLA (2606.19565): 15.4 GB to 4.1 GB, success 96.3 vs 97.1.
  - QVLA (2602.03782): 29.2% of VRAM, 98.9% of performance.
  - HoloQ-VLA (2605.28803), HBVLA (2602.13710) and BitVLA (2506.07530) also report low-bit results.
  - FoldQuantVLA (2609.24433): native W4A4 TensorRT on Orin at 1.20-1.33x over FP TensorRT.
  - VLAQuantBench (2609.25376): results depend on scope and format.
  - [new] github-omega1029-openvla-oft-quantization: W4A4 is lossless on LIBERO only with a rotation, and collapses to 0% without one (fake quantization).
  - [new] github-openvla-issue-324-fp8-nvfp4-libero: FP8/NVFP4 at 7.68/4.44 GB with no significant LIBERO drop (dequantized).
  - [new] github-radixquantvla: W4 pi0.5 reaches 98-99% on LIBERO-Object on an A100.
- Ports that exist:
  - llama.cpp/GGUF: vla.cpp (2606.08094) and LiteVLA-Edge (2603.03380).
  - TensorRT-LLM: [new] github-rail-berkeley-tensorrt-openvla, with no published numbers.
  - MLC/NanoLLM: the Jetson tutorial above.
  - Distilled or smaller alternatives: Shallow-π (2601.20262) and GigaBrain-0-Small.

**Best evidence**
- jetson-ai-lab-openvla-tutorial: on-device INT4 and closed-loop sim success.
- 2606.08094: Orin memory and latency tables.
- 2609.24433: native W4A4 on Orin.
- 2605.24011 and 2606.19565: LIBERO success with measured memory.

**What remains open**
- No source reports OpenVLA or OpenVLA-OFT LIBERO success from real low-bit kernels running on an Orin NX 16GB or Orin Nano, together with peak unified memory (including the vision tower, KV cache and a ROS stack) and control Hz.
- Most 4-bit LIBERO results use fake quantization or datacenter GPUs. Weight-only 4-bit often gives no speedup at batch 1 (vla-lite, github-laelazorana-embodied-efficiency, 2607.08029).
- Unified-memory overheads (JAX preallocation, CUDA context, camera buffers) are undocumented.
- Discrete-bin gripper flips under 4-bit have not been checked in closed loop at scale.
