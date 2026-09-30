# SB_1 triage log (shard1, snowball round 2)

- Candidates read: 429
- Recorded: 132
- Skipped: 297
- Count by relevance: 5 -> 1, 4 -> 15, 3 -> 45, 2 -> 71
- Foundational techniques (foundational_technique=true): 7 (DMD2, OmniQuant, KVQuant, Sarathi-Serve, LayerSkip, OPTQ/GPTQ, Diff-Instruct)
- Unverified (no abstract, recorded on title): 5 (Open X-Embodiment, Diffusion-VLA, pi*0.6, HybridFlow, OPTQ)

What got skipped: generic surveys, VLA papers about capability or robustness only with links < 10, attack/security papers, data-collection hardware, and navigation/humanoid work with no efficiency angle.

## Notable finds
- 2506.08822 FreqPolicy: frequency-consistency one-step flow policy, 93.5 Hz real-world inference, also plugged into a VLA on LIBERO.
- 2606.11187 Next Forcing: multi-chunk prediction for world-action models, 2x inference speedup and 2.3x faster convergence.
- 2603.20658 Speedup Patch: plug-and-play chunk-downsampling scheduler learned offline, 1.8x execution speedup.
- 2607.29482 Temporal Policy: history-initialized transport, 19.1 ms inference on an RTX 4080.
- 2510.07865 DM1: one-step MeanFlow policy, 0.07 s vs 2-3.5 s inference.
- 2607.06262 OTQL: RL post-training that cuts flow-policy/VLA sampling steps by 70%.
- 2608.16503 NebulaVLA: asynchronous dual-frequency VLA, ~2.7x faster action generation.
- 2607.06678 NativeMEM: one-token-per-frame native memory compression for VLAs with negligible latency overhead.
- 2604.24391 FreqCache: frequency-guided token caching for VLN models, 1.59x speedup.
- 2606.25473 Causal-rCM: autoregressive diffusion distillation (1-2 steps) for interactive world models incl. Cosmos.
