# C9 summary: people, venues and blogs sweep

**Scope covered:** the workshop site; author sweeps of all 7 speakers and organizers; lab and company blogs; a venue sweep through Semantic Scholar and arXiv query families; the workshop's OpenReview venue.
**Output:** 237 records in `C9.jsonl`, of which 235 are verified and 2 are `verified:false`. The search log has 80 entries.
**Record types:** 146 preprints, 40 papers, 24 blogs, 12 tech reports, 8 repos, 6 benchmarks and 1 workshop-CFP record.
**Found via:** 143 venue sweep, 49 author sweep, 43 blog sweep.

**Tooling caveats**
- The shared WebSearch budget ran out partway through (200 of 200 calls used). Later work used WebFetch, the Semantic Scholar API and the arXiv API.
- `pi.website` returned HTTP 429, so Physical Intelligence posts were reached through their arXiv papers, a search snippet of the RTC page, and the Hugging Face and Modal posts.

## Workshop site (efficient-embodied-ai.github.io)
- **Event:** CoRL 2026 workshop, Nov 12, 2026, in Austin.
- **Papers:** 4 pages plus references, non-archival, double-blind on OpenReview. Due Oct 12, with notification Oct 26.
- **Challenge:** the harness and reference container were released Sep 25. Challenge submissions are due Oct 23 and results are verified Nov 5.
- **CFP topics:**
  - efficient VLA / world-action-model architectures (chunking, MoE, early exit, diffusion/flow step reduction)
  - compression (quantization, pruning, distillation)
  - memory-efficient adaptation
  - benchmarking, including whether techniques compose
  - hardware-aware design (GPU, TPU, Trainium/Inferentia, mobile NPUs)
  - edge-cloud hybrids for fleets
  - safety/latency trade-offs and fallback policies under stochastic response time
  - efficient world models for online planning and safety monitoring
- **Speakers:** Jiajun Wu (Stanford), Yecheng Jason Ma (Dyna), Dhruv Shah (Princeton/GDM), Ouais Alsharif (GDM).
- **Organizers:** Jiafan Yu (Google), Ouais Alsharif, Changliu Liu (CMU), Dhruv Shah, Jiajun Wu, Zhuoyang Zhang (MIT).

## OpenReview status
- The group `robot-learning.org/CoRL/2026/Workshop/EEAI` exists; the API `groups` call works.
- It has `public_submissions=false`. The submission invitation opened 2026-09-14 and is due 2026-10-12.
- `notes` queries through api2 and the v1 API (by venueid and by invitation) returned 403 ChallengeRequiredError. The web group page is JS-rendered and showed no content.
- **No public submissions are visible.** This is expected, since the deadline has not passed and submissions are set non-public.
- Sister CoRL 2025 workshops (RoboWM, Eval-Deploy, SAFE-ROL, GenPriors, etc.) are listed, and Eval-Deploy also has non-public submissions.

## Key people and their threads (2023–2026, in scope)
- **Dhruv Shah (Princeton / GDM):**
  - edge-cloud and asynchronous navigation VLAs: AsyncVLA runs a remote VLA plus an onboard Edge Adapter and tolerates 6 s delays
  - the Gemini Robotics family: a cloud backbone plus an on-robot decoder, <160 ms backbone latency, ~250 ms end-to-end, 50 Hz effective control
  - MoE action heads, key-frame long-context policies (BPP), and hierarchical VLA orchestration studies
  - world-model evaluation (a Veo simulator, WorldArena) and the earlier compact onboard navigation models (GNM, ViNT, NoMaD)
- **Jiajun Wu (Stanford):**
  - test-time compute routing for embodied planners: DIRECT is up to 65% lower latency at matched success
  - a real-time physics-bridged video world model: RealWonder, 4 diffusion steps, 13.2 FPS
  - test-time-training memory for VLAs (T2Mem), world-action interfaces (TrAct, Masked Visual Actions), and a world-model survey
  - safety of LLM planners (DESPITE)
- **Yecheng Jason Ma (Dyna Robotics):**
  - Dyna-2 is a flow-matching world-action model with a mixture-of-transformers design and 1M-hour human-video scaling; its one-step video mode is ~90x faster (110 ms vs 10.2 s on H100).
  - Dyna-2.1 is a three-rate stack: VLM orchestrator, ~5 Hz policy, and a 100 Hz RL whole-body controller.
  - DYNA-1 used reward-model-in-the-loop RL: 99.4% success over 24 h.
  - His academic papers from 2023–2026 (Eureka, DrEureka, DROID, GCR) are mostly outside the efficiency scope.
- **Zhuoyang Zhang (MIT Han Lab):**
  - VLASH, future-state-aware async inference: up to 11.8x lower reaction latency on pi0.5 (IROS 2026)
  - ForeAct, an efficient foresight planner: 0.33 s per image on H100 (CVPR 2026 Highlight)
  - CoT-VLA; co-author on pi0.7
  - efficiency primitives: NVILA, LPD parallel decoding, JetViT hybrid attention, 2-bit KV-cache video generation
- **Changliu Liu (CMU ICL):**
  - runtime safety for foundation-model robots: SafeDec, STL-constrained decoding (ICML 2026)
  - safe-stoppability fallback monitors for humanoids (IROS 2026) and λ-Reachability (CoRL 2026)
  - Koopman safe control; a one-step diffusion distillation for real-time control (Koopman distillation)
  - VLESA safety agent, SPARK toolbox; HOVER / VIRAL humanoid controllers
- **Ouais Alsharif (GDM):** no public papers from 2023–2026 were found on Semantic Scholar or arXiv. His latest are the 2019–2020 StarNet / streaming point-cloud detection papers (targeted computation), which predate the window and were not recorded. His current work is presumably inside the Gemini Robotics team reports.
- **Jiafan Yu (Google):** Semantic Scholar and arXiv show only 2017–2018 energy-systems papers (DeepSolar, etc.). No in-scope publications were found.

## Blogs / industry: technical posts recorded
- **Google DeepMind:**
  - Gemini Robotics On-Device (fully local bi-arm VLA, 50–100 demo adaptation; no latency disclosed)
  - Gemini Robotics 2 / On-Device 2 (July 2026)
  - SARA-RT linear-attention up-training (14% faster than RT-2)
- **Physical Intelligence** (reached through papers and third-party posts):
  - pi0 timing table: 73 ms on RTX 4090
  - FAST, Knowledge Insulation, RTC (>300 ms delay tolerance), training-time RTC, pi*0.6, pi0.7
  - Modal remote-inference case study: 10–15 ms added network overhead
- **NVIDIA:**
  - GR00T N1: L40, 63.9 ms per 16-action chunk, 10/120 Hz
  - GR00T N1.7 TensorRT table: Orin 354 → 151 ms, Thor 113 → 80 ms, H100 86 → 28 ms
  - Jetson Thor launch (GR00T N1.5 2.74x faster than Orin) and a Jetson edge-AI tutorial
  - community FlashRT: pi0.5 at 23 Hz on Thor and 57 Hz on an RTX 5090
- **Figure:**
  - Helix: 7B S2 at 7–9 Hz plus an 80M S1 at 200 Hz, on dual embedded GPUs
  - Helix logistics "Sport Mode": test-time chunk resampling, up to 50% faster
  - Helix 02 S0: 10M parameters at 1 kHz
- **1X:**
  - Redwood: 160M parameters, ~5 Hz onboard
  - 1XWM world-model policy: 14B, ~11 s per inference offboard
- **Hugging Face LeRobot:**
  - SmolVLA: 450M, 64 tokens per frame, layer skipping
  - async inference post: ~2x faster task completion
  - pi0/pi0-FAST port using FlexAttention
- **Dyna:** DYNA-1, DYNA-1 pre-training, Dyna-2, Dyna-2 infrastructure, Dyna-2.1.
- **TRI / Boston Dynamics:** the LBM careful-examination report, and a 450M flow DiT on Atlas with 1.5–2x test-time speedup.
- **BAIR:** GRASP parallel gradient planning for world models.
- **SAIL:** R&B-EnCoRe, with concise reasoning cutting WidowX latency from ~5 s to ~3 s, and the ICML 2026 roundup.
- **AWS:** a pi0 fine-tuning post on H100s showing 1 ODE step is enough (~199 ms). No AWS Neuron (Trainium/Inferentia) robot-policy inference post was found, which is a gap given the CFP mentions this hardware.
- **MIT Han Lab:** covered through the VLASH, ForeAct, NVILA and LPD records.
- **Tesla AI:** the AI page has no Optimus-specific technical detail, so nothing was recorded.
- **Unitree / Agility:** not reached after the search budget ran out.

## Venue observations
- **2026 arXiv volume:** 2026 is dominated by arXiv-first work. Three families are growing especially fast:
  1. efficient world-action models (about 30 recorded): Fast-WAM, Flash-WAM, GlanceWAM, Rolling-WAM, Efficient-WAM, Light-WAM, LaWAM, MotionWAM
  2. VLA quantization (about 20): VLAQuantBench, HBVLA, BitVLA, DyQ, DA-PTQ, FoldQuant
  3. async / real-time chunking (RTC, VLASH, FASTER, TIC-VLA, Jetson-PI)
- **Peer-reviewed venues:**
  - CoRL/RSS 2023–2025 carry the seminal works (RT-2, OpenVLA, OFT, FAST, pi0).
  - NeurIPS 2024–2025: DeeR-VLA, RTC, KI, MPA.
  - ICML 2025–2026: Hi Robot, SafeDec, VLAW.
  - IROS 2025–2026: PD-VLA, VLASH, safe-stoppability.
  - CVPR / ICCV: CoT-VLA, NVILA, ForeAct, LightDP.
  - VLSI 2026: a custom VLA edge processor, 6.7 ms / 150 Hz.
- **Hardware and systems** are emerging as their own sub-venue: VLA-Perf, edge characterization on Orin/Thor (action generation takes 75% of latency), cross-platform scaling, vla.cpp, Embodied.cpp, and roofline co-design laws.
- **Direct composition evidence is still rare.** Examples are SQAP-VLA (quantization plus pruning), Decoupled Early Exits (three compute axes), the ONNX-changes-behavior study, and VLAQuantBench.

## Open problems surfaced
- **Reporting:** metrics are inconsistent. Papers mix chunk rate, closed-loop rate and relative latency, so few report closed-loop Hz on named onboard hardware.
- **Measured bottleneck:** on edge devices the action head or decoding, not the VLM, dominates latency.
- **Edge-cloud safety:** jitter and command starvation (AsyncShield, SPO), with no standard fallback semantics.
- **Composition:** a benchmark of how efficiency techniques compose is missing.
- **Hardware gaps:** there is no public Trainium/Inferentia or mobile-NPU inference evidence for VLAs.
- **World-action models:** whether test-time imagination is needed at all (Fast-WAM vs GlanceWAM).

## 10 most important works (for this workshop)
1. Real-Time Execution of Action Chunking Flow Policies (RTC), 2506.07339, and Training-Time RTC, 2512.05964
2. Gemini Robotics (cloud backbone plus on-robot decoder latency design), 2503.20020, and the Gemini Robotics On-Device blog
3. Figure Helix blog (onboard 7B@7–9 Hz / 80M@200 Hz dual-system) plus Helix logistics Sport Mode
4. VLASH: future-state-aware asynchronous inference, 2512.01031 (organizer Zhuoyang Zhang)
5. AsyncVLA: asynchronous edge-adapter VLA, 2602.13476 (organizer Dhruv Shah)
6. pi0 (with its timing breakdown), 2410.24164, and FAST, 2501.09747
7. OpenVLA-OFT: Optimizing Speed and Success, 2502.19645
8. GR00T N1, 2503.14734, plus the Isaac-GR00T TensorRT cross-hardware latency table
9. Fast-WAM, 2603.16666, and Flash-WAM, 2606.05254 (efficiency of world-action models), with Dyna-2's one-step WAM blog
10. SafeDec, 2509.01728, and Safe-Stoppability Monitors, 2603.22703 (organizer Changliu Liu: runtime safety and fallbacks)

## Saturation note
- **People and blogs:** these sweeps saturated. The final arXiv author re-sweeps added only 2–3 items per person.
- **Venue sweep:** this did not saturate. The last query batches still returned 2–20 new relevant 2026 preprints each (efficient WAMs, VLA quantization, edge runtimes). The literature is expanding faster than one cluster can cover.
- **Stopping point:** work stopped at 237 records, above the 80–200 target. The C1–C8 cluster agents are expected to cover these families in depth.
