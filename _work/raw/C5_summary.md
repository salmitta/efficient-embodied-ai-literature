# C5 — Hardware-aware design and accelerators: cluster summary

Items: 138 records in `C5.jsonl` (137 verified, 1 unverified). Relevance counts: 29 at 5, 37 at 4, 45 at 3, 27 at 2. Log: 74 query entries in `C5_searchlog.md`.
Types: 98 preprints, 25 peer-reviewed papers, 9 blogs/tutorials, 4 tech reports, 2 repos/docs.

## Technique families

1. **Workload characterization and performance modeling.** These papers profile VLAs across hardware tiers and build analytical models of their cost. They agree on a split: the VLM prefill is compute-bound, while autoregressive decoding and the iterative action expert are memory-bandwidth-bound (or bound by launch overhead) at batch 1.
   - Key works: VLA-Perf (2602.18397), VLA across XPUs (2604.24447), MolmoAct on Orin/Thor (2603.02271), Cross-Platform Scaling (2509.11480), PhyAI's control-time roofline (2608.03682), energy/carbon footprint on AGX Orin (DOI 10.1145/3797248.3815411), Offload or Overload (2603.18284), Hydra (2608.25053), batch-1 decode bandwidth gap (2605.30571), Seeing is Free, Speaking is Not (2607.09520).
2. **Kernel- and graph-level optimization on GPUs.** Techniques include CUDA graphs, operator fusion, Triton GEMM tuning, custom TensorRT plugins, FP8/NVFP4, and hand-written CUDA kernels.
   - Key works: Running VLAs at Real-time Speed (2510.26742), GR00T TensorRT deployment guide, OpenPi π0.5 on Thor (FP8+NVFP4), FlashRT, FoldQuantVLA's W4A4 TensorRT plugins (2609.24433), KerColle's SM-level scheduling (2609.22335), the FlashAttention 1/2/3 family (foundational).
3. **Portable edge runtimes.** These are C++, llama.cpp-style, and SIMD CPU engines that run many VLA architectures without PyTorch.
   - Key works: vla.cpp (2606.08094), Embodied.cpp (2607.02501), vla.simd (2609.24274), Jetson-PI-Edge (2607.12659), LiteVLA-Edge (2603.03380), OmniModel.cpp in ActQuant (2605.24011), TensorRT Edge-LLM.
4. **Onboard deployment recipes for specific robots.** Jetson Orin, Orin NX, Orin Nano, and Thor deployments across manipulation, humanoid control, UAVs, and field robots.
   - Key works: Jetson-PI, bimanual ACT on Orin Nano (2608.03938), SONIC and OmniXtreme on G1's Orin, OxyGen on a humanoid with onboard Thor (2603.14371), Shallow-π on Orin/Thor, NanoVLA, LiteVLA-H, EdgeVLN (Orin NX), AnywhereVLA (Orin NX + NUC split).
5. **Heterogeneous and partitioned compute (onboard / edge / cloud).** Covers dual-GPU onboard splits (Figure Helix), cloud backbone plus onboard decoder (Gemini Robotics), device-edge co-inference optimized for energy under SLOs, and CPU-GPU layer offload.
   - Key works: EcoVLA (2608.15502), RoboECC, RAPID, CloudEdgeVLA, VLA-ULAP (energy on Orin Nano), ComVLA (6G), hybrid CPU-GPU driving VLA (2608.14586), OOM-Free Alpamayo (2605.11678), and operator-level CPU/GPU/NPU mapping in BIDENT (2606.05271).
6. **Fleet serving on shared GPUs.** This family trades per-robot compute against pooled datacenter GPUs.
   - Key works: ROSA, Robion, Armory's action-chunk scheduling, Kairos, VLAgents, LeRobot async inference.
   - The SemiAnalysis TCO study (a blog) estimates offload is cheaper beyond roughly 5–7 robots.
7. **Dedicated accelerators and algorithm-architecture co-design.** Custom silicon and co-designed hardware for VLAs and embodied agents.
   - Key works: Dadu-Corki (ISCA 2025; ZC706 FPGA), SpecVLA (2608.15636), VQVLA (2607.24148), DiTPA (ISCA 2026), Deltoris (bit-serial systolic, 2608.04428), ReCA (ASPLOS 2025), CREATE (undervolting resilience).
   - Older robotics accelerators: Robomorphic, RoboX, Tartan, RoboGPU.
   - Alternative silicon: Cambricon MLU, Mobilint NPU, AMD ROCm, SpikeVLA.
8. **Hardware-aware model design.** Models whose size and structure are chosen for a device's roofline. Examples: a co-design scaling law via roofline on Orin (2602.10377), EdgeVLA, NanoVLA, BitVLA, SmolVLA, VOTE, DeeR-VLA (budget-conditioned early exit), and the latency-paired action-head study (2609.13984).

## Key open problems

- **Memory bandwidth, not FLOPs, limits edge VLAs.** Thor has about 1 PFLOP of dense FP4 but only 273 GB/s. The action expert and decode are memory-bound, and at batch 1 launch overhead and low bandwidth utilization dominate. Few works co-design model structure against this: most compress weights rather than restructure how memory is accessed.
- **Metrics are not comparable.** Papers report open-loop chunk latency, action-supply rate, closed-loop Hz, and "FPS" interchangeably, on different GPUs and with different camera counts.
  - Benchmark bugs can invert rankings (2609.37771).
  - Faster runtimes can silently change closed-loop behavior: ONNX exports that are really FP32 (2609.14146), and precision issues in positional indices (vla.cpp).
  - Energy and thermal-soak measurements are rare. Internal Jetson power telemetry is biased (2608.00927).
- **Energy and battery costs are mostly unquantified.** Onboard GPUs can cut humanoid runtime by hours (2603.18284). Yet only a handful of papers report joules per action or task, and even fewer report per-unit cost.
- **Heterogeneous SoC utilization.** The NPUs, DLAs and CPUs on Jetson or Snapdragon-class SoCs are largely unused by VLA stacks. Operator-level mapping (BIDENT) and non-NVIDIA stacks (ROCm, Cambricon, Ascend) are early-stage.
- **Accelerator research still runs on simulators.** VLA accelerators (Corki, SpecVLA, VQVLA, DiTPA, Deltoris) are evaluated in simulation or on FPGAs against A100 or mobile-GPU baselines. None has been shown in closed loop on a real robot at humanoid power budgets.
- **Onboard vs offboard is an unsettled systems question.** Fleet serving is cheaper at scale but vulnerable to network jitter. Hybrid designs (a slow cloud System 2 with a fast onboard System 1) lack principled latency and safety guarantees under degraded links.
- **Scaling to 10–100B parameters onboard.** Projections call for HBM or processing-in-memory (2603.02271) or flash-backed NPUs (Cambricon-LLM), but none exists in a robot form factor.
- **Industry opacity.** Figure, Tesla (AI5), 1X, Agility and Gemini Robotics On-Device disclose little about onboard latency, power or cost.

## 10 most important works (for this cluster)

1. **VLA-Perf** — *How Fast Can I Run My VLA?* (2602.18397). An analytical performance model covering model design and on-device/edge/cloud placement.
2. **Characterizing VLA Models across XPUs** (2604.24447). A cost/energy/time leaderboard across GPUs and NPUs; shows the compute-bound VLM versus memory-bound action expert.
3. **Running VLAs at Real-time Speed** (2510.26742). The canonical kernel-level recipe: π0 at about 30 Hz on an RTX 4090.
4. **Dadu-Corki** (2407.04292, ISCA 2025). The founding algorithm-architecture co-design paper for embodied-AI robots.
5. **Characterizing VLA Models: action-generation bottleneck on Orin/Thor** (2603.02271). Memory-bound action generation takes up to 75% of latency, with HBM/PIM projections.
6. **Jetson-PI** (2607.12659). Onboard asynchronous VLA on Jetson Orin with CUDA-level system optimizations: 8.66x control frequency over naive PyTorch.
7. **NVIDIA Isaac GR00T TensorRT deployment guide and Jetson Thor platform blog.** The reference cross-hardware latency table (H100 through Orin) and Thor specs (FP4 compute vs 273 GB/s bandwidth).
8. **Figure Helix** (blog, 2025). The industrial example of splitting a VLA across two onboard embedded GPUs: S2 at 7–9 Hz, S1 at 200 Hz.
9. **PhyAI** (2608.03682). One runtime spanning onboard, edge and cloud for VLAs and world-action models, with a control-time roofline and detailed profiles.
10. **Offload or Overload** (2603.18284) together with **ROSA** (2607.01088). Measurement and system design for the onboard-vs-offboard trade-off, covering battery, network and fleet sharing.

Runners-up:
- vla.cpp (2606.08094)
- EcoVLA (2608.15502)
- OxyGen (2603.14371)
- FoldQuantVLA (2609.24433)
- DiTPA (ISCA 2026)
- the energy/carbon footprint of VLAs on AGX Orin
- the FlashAttention series (foundational)
