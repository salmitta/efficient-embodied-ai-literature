# SB_4 snowball round 2 triage log (shard4)

- Candidates read: 429 (every line of shards/shard4.jsonl; abstracts checked in full for borderline items)
- Recorded: 123
- Skipped: 306. These were mostly generic VLA method papers with no efficiency angle and fewer than 10 links, plus surveys, datasets or teleop systems under the link threshold, unrelated robotics, and PPO (a generic RL algorithm, not an efficiency technique).
- Unverified (no abstract, recorded from title): 5 (piRL, AWQ, DEFLECT, VLA-Cache, sample-efficient dexterous fine-tuning)

## Count by relevance
| relevance | count |
|---|---|
| 5 | 4 |
| 4 | 20 |
| 3 | 56 |
| 2 (context, links >= 10) | 28 |
| 2 (foundational_technique = true) | 15 |

## Notable finds
- 2609.10915 IMLE-VLA: one-step cIMLE action head for pi0.5, 55 Hz vs 15 Hz inference, 3.9-6.6x lower per-episode inference time.
- 2609.36967 Beyond Token Importance (GeoScaffold): training-free spatial-scaffold visual token pruning for pi0.5, 1.78x prefill speedup at 20% of tokens.
- 2604.03540 Drift-Based Policy Optimization: native 1-NFE generative policy (100 -> 1 NFE), 9.5 ms end-to-end on a dual-arm UR5.
- 2609.36413 RoboActualizer (One from Infinity): ~60M trainable actualizer on a frozen video world model, 39 ms latency, up to 100x fewer trainable params.
- 2512.09101 Masked Generative Policy: parallel masked action-token generation, up to 35x lower inference time.
- 2603.23149 Describe-Then-Act (DILLO): distilled language-action world model for safety steering, 14x faster than visual simulation.
- 10.1109/ISoIRS70157.2026.11545245 Cross-SSM (State-Space Modeling for Action Generation): cache-free linear-time action expert for on-device VLAs.
- 2606.23444 SkyJEPA: JEPA latent world model plus sampling-based control running real-time on embedded quadrotor hardware.
- 2607.02646 EVA-Client: open deployment framework unifying sync/async inference, temporal ensembling and Real-Time Chunking.
- 2606.06049 L-SDPPO: spiking diffusion policy for low-energy manipulation on power-limited spacecraft robots.
