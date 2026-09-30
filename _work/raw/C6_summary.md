# C6 — Edge-cloud co-design and fleet systems: cluster summary

158 verified records (0 unverified) in `C6.jsonl`. 97 logged searches in `C6_searchlog.md`. Saturation: searches 88–97 produced no new items with relevance ≥3; the only two additions from that stretch were rated relevance ≤2.
Seed checks. FogROS / FogROS2 (plus -SGC, -Config, -FT, -PLR, FogROS G): verified. SmolVLA async stack: verified. Gemini Robotics On-Device vs the cloud backbone: verified. openpi remote inference (WebSocket policy server): verified. RoboECC (2603.20711, IJCNN 2026): verified. EdgeVLA / EVLA (2507.14049, K-Scale): verified. EVLA is onboard-efficiency work, not an edge-cloud split. Its companion paper RAPID (2603.07949) is the partitioned-inference one.

## Technique families
1. **Cloud/fog offload platforms and middleware.** Examples: the FogROS line; ElasticROS; the policy servers in openpi, LeRobot, GR00T and VLAgents; the PI-on-Modal QUIC channel; the MSR Physical AI Toolchain; Kubernetes-based orchestration. These cover provisioning, secure global routing, multi-cloud replication for tail latency, and cost-aware server selection.
2. **Split / partitioned VLA inference across device–edge–cloud.** Examples: RoboECC, RAPID, EcoVLA and ComVLA; the generic split-computing surveys (Matsubara; DNN partition); VLM split for drones (AVERY; "Cloud, Edge, or Split?"). These choose split points that account for model structure and bandwidth. Some adapt the split online. ComVLA sets its token budget from the channel.
3. **Hierarchical cloud-reasoning / onboard-control architectures.** Examples: Gemini Robotics (cloud backbone plus on-robot decoder, ~250 ms end-to-end, 50 Hz via chunks); Gemini Robotics 2 (cloud ER plus On-Device VLA); Figure Helix, a fully onboard S2/S1 counterpoint; CloudEdgeVLA; AsyncVLA-nav plus an edge adapter; AsyncShield; VLA-ULAP; ECHO (cloud text-to-motion, onboard RL tracker); RoboOS.
4. **Latency hiding and delay robustness for remote/async inference.** Examples: RTC, training-time RTC, VLASH, A2C2-style residuals, DEFLECT, RAPAC-DP, FASTER, FutureRTC, Speculative Policy Orchestration and Dedelayed; the comparison study 2605.08168. These let a policy tolerate 10s–100s of ms, and sometimes seconds, of round-trip delay.
5. **Network-aware execution and communication co-design.** Examples: Communication-Aware Robot Execution (choosing where to send each request); FogROS2-PLR (multi-interface 5G); task-relevant compression and semantic communication; communication-control co-design for factory wireless; learned offloading policies (Chinchali RSS'19, UniLCD).
6. **Fleet-scale serving and scheduling.** Examples: ROSA (shared GPU pool, factory-objective scheduling, up to 12.06x productivity); Robion (up to 64 robots on 4 GPUs at 98% SLO); Armory (chunk-rate-aware batching); Kairos (generate-execute-aware serving); PhyAI (one runtime for onboard, edge and cloud).
7. **Placement analysis, measurement and TCO.** Examples: Offload or Overload (MSR measurement study); VLA-Perf (analytical placement model); cross-platform edge-vs-cloud VLA scaling; "Can the Cloud Drive?" (5G/6G plus cost); SemiAnalysis TCO (silicon crossover at ~7 robots per GPU); PEERNet profiling.
8. **Fleet learning loops.** Examples: SOP (fleet to cloud learner, near-linear scaling with fleet size); RLinf-USER; OpenBot-Fleet; AutoRT; HarvestNet.

## Key open problems
- **Jitter and tail latency, not the mean.** Most async and delay-robust methods are evaluated with fixed or uniform delays. Heavy-tailed, bursty wireless jitter and outages remain under-studied. This includes safe fallback to onboard policies.
- **No standard latency-aware benchmark.** The field lacks shared evaluation protocols with injected delay, bandwidth caps or connectivity maps. LIBERO with synthetic delays dominates. Real-robot evaluation over real Wi-Fi or 5G is rare.
- **Split points for modern VLAs.** VLM-plus-action-expert and world-action models have large intermediate tensors and KV caches. Few works jointly optimize what to transmit (tokens or features) and where to cut the model.
- **Fleet economics.** TCO evidence is mostly analytical or from blogs (SemiAnalysis, "Can the Cloud Drive?"). Measured cost, energy and utilization trade-offs for real fleets are scarce. Interactions between batching and SLOs are only starting to be studied (ROSA, Robion, Armory, Kairos).
- **When to call the cloud.** The open question is how to learn or verify when a request is worth the cost in latency, energy and money. Candidate signals include confidence, scene change and task phase (VLA-ULAP, event-triggered inference, UniLCD, LAECIPS), preferably with safety guarantees under delay.
- **Security and privacy of remote policy servers.** Default servers expose unauthenticated endpoints (openpi issue; LeRobot deserialization CVE reports). Privacy-preserving offload for home robots is largely open.
- **Onboard vs cloud capability gap.** On-device models (Gemini Robotics On-Device, Helix, Jetson-PI) are closing on cloud quality. When the network is worth it depends on model scale, the task's reaction-time needs and connectivity. No general decision theory exists yet.

## 10 most important works
1. **FogROS2** (2205.09778, ICRA 2023), with FogROS2-FT (IROS 2024) and -Config (ICRA 2024). The reference open cloud/fog robotics platform. Covers latency, reliability and cost.
2. **Gemini Robotics** (2503.20020), plus the Gemini Robotics On-Device blog. The canonical cloud-backbone/onboard-decoder VLA with reported latency, and the industry's explicit on-device counterpart.
3. **Real-Time Chunking** (2506.07339, NeurIPS 2025). The key latency-hiding technique that makes remote or slow VLA inference usable. Now in PI, LeRobot and FluxVLA deployments.
4. **SmolVLA** (2506.01844) and the LeRobot async stack. An open reference for asynchronous policy-server/robot-client inference.
5. **Offload or Overload** (2603.18284, MSR). The first measurement study of onboard vs edge vs cloud for mobile-manipulation foundation-model stacks. Covers battery, latency-accuracy, bandwidth and fleet sharing.
6. **ROSA** (2607.01088). Shared GPU-pool serving for robot factories with factory-objective scheduling.
7. **VLA-Perf** (2602.18397). Analytical model and takeaways on where VLA inference should run, given hardware and network.
8. **RoboECC** (2603.20711, IJCNN 2026). Network-aware edge-cloud split deployment designed for diverse VLAs.
9. **CloudEdgeVLA** (2608.00569). Latency-tolerant cloud/edge VLA through delay-trained representational specialization.
10. **Action Chunk Scheduling / Armory** (2608.00337). Formalizes multi-robot remote VLA serving as closed-loop-aware scheduling.

Honourable mentions: AsyncVLA-nav (2602.13476); VLASH (2512.01031); Robion (2609.12075); Kairos (2605.11381); ComVLA (2609.07838); Speculative Policy Orchestration (2603.19418); SemiAnalysis TCO analysis; Chinchali et al. network offloading policies (RSS 2019); Kehoe et al. cloud robotics survey (T-ASE 2015).

Note: several async-inference records are also tagged C7. Onboard-runtime and hardware-characterization records are also tagged C5.
