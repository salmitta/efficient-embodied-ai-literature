# SB_6 triage log (snowball round 2, shard6)

- Candidates read: 429 (16 had no abstract)
- Recorded: 121
- Skipped: 308
- By relevance: 5 = 1, 4 = 17, 3 = 87, 2 = 16 (context, links >= 10)
- foundational_technique = true: 9 (ToMe, guided-diffusion distillation, FlatQuant, Atom, RPTQ, TTQ, MobileLLM, VisPruner, on-device SLM survey)
- verified = false (title only, no abstract): 3 (RoboMamba 2406.04339, Chunk-Boundary Artifact 2603.11642, Sliding-Cache VLA ICASSP DOI)

Main reasons for skipping: generic VLA/WAM method papers with no efficiency, latency or safety angle (spatial/3D grounding, reasoning/CoT, reward models); surveys; adversarial/security attacks; data-collection systems; and context-type papers with links < 10.

## Notable finds
- 10.1109/LRA.2026.3683324 DMS-VLA (RA-L): shares weight templates across layers; 25-55% inference speedup on H100/RTX 4090/Jetson AGX Orin (rel 5).
- 2606.02486 AHEAD ("Intercepting the Future"): a 4.9M-parameter latent world model added to a frozen OpenVLA to compensate for latency on moving objects; tested on a real xArm.
- 2603.06331 WorldCache: training-free token caching for diffusion world models, up to 3.7x end-to-end speedup.
- 2605.08732 Latent Geometry Beyond Search: an amortized inverse-dynamics planner that cuts per-decision cost 100-130x compared with CEM.
- 2609.20761 Agile-WAM: tactile world-action model with 11.9 ms inference latency on real contact-rich tasks.
- 2601.14628 NeuroVLA: neuromorphic VLA running at 0.4 W with safety reflexes under 20 ms.
- 2602.06575 ThinkProprio: proprioception-guided visual token selection that keeps about 12% of tokens and lowers end-to-end latency.
- 10.1109/ICCC70295.2026.11680263 VTP: task-aware transmission protocol for VLAs offloaded to edge servers under packet loss (C6).
- 2603.17834 GeCO: time-unconditional flow matching with adaptive early exit and a training-free OOD safety signal; scales to pi0.
- 2504.18792 STDArm: online latency estimation and delay compensation for policies running on moving mobile platforms.
