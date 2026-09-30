# SB_5 snowball round 2 triage log (shard5)

- Candidates read: 429
- Recorded: 119 (in raw2/SB_5.jsonl)
- Skipped: 310. This includes 1 duplicate: candidate 171 (DA-SIP, NeurIPS entry with no arXiv ID) was merged into 2511.20906.
- By relevance: 5 -> 5, 4 -> 29, 3 -> 58, 2 (context, links >= 10) -> 27
- foundational_technique=true: 6 (QuIP#, DuQuant, Q-Diffusion, OstQuant, AAPT, MuE early exit)
- verified=false (no abstract, title clearly in scope): 5 (OxyGen, Enfold, VLA-Pruner, action-caching acceleration, RoboCat)

Skip policy: VLA or WAM method papers with no efficiency angle were skipped unless links >= 10 and the paper is a foundation model, dataset or benchmark. Also skipped: surveys (except two on hardware and edge), attack/backdoor papers, and task benchmarks with no efficiency angle and links < 10.

## Notable finds
- 2603.17850 ProbeFlow: a training-free adaptive ODE step schedule for flow-matching VLA heads. Action decoding is 14.8x faster and end-to-end latency 2.8x lower on MetaWorld.
- 2509.05614 SpecPrune-VLA: action-aware two-level token pruning. Speedup is 1.57x on LIBERO and 1.70x on real robots.
- 2506.13456 BAC: training-free block-wise feature caching for diffusion policies and VLAs, with up to 3x speedup.
- 2603.17240 GigaWorld-Policy: an action-centred WAM where video generation is optional. It runs 9x faster than Motus.
- 2511.12101 Freeze, Share, Shrink: a 5M-parameter MLP action backbone matches a 244M U-Net. This suggests diffusion action heads are over-parameterized.
- 2505.05787 Action lookup table: replaces a diffusion policy with a lookup table that needs 0.0034x the inference time and 0.0085x the memory.
- 2607.06216 MoWorld: a real-time world model that runs at up to 50 FPS on an NPU.
- 2607.15621 Think at 5 Hz, Act at 20 Hz: asynchronous fast-slow driving VLA at 32 ms per tick on a consumer GPU.
- 2609.23305 Shared Execution-Clock Drifting Policy: a one-step policy running onboard NVIDIA Thor for deadline-sensitive manipulation.
- 10.1109/FCCM68464.2026.00075 SmolVLA on an AMD XDNA NPU: an early prototype of VLA deployment on an edge NPU.
