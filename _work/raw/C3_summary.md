# C3 — Memory-efficient adaptation and fine-tuning: cluster summary

Records: 235 (all verified against an arXiv abstract or fetched page) in `C3.jsonl`. Searches logged: 51 rows in `C3_searchlog.md`.
Relevance distribution: 5 → 16, 4 → 61, 3 → 107, 2 → 51.

**Coverage caveats.**
- The session's shared WebSearch budget ran out after search 21.
- The Semantic Scholar keyword search kept returning HTTP 429, so most later discovery used the arXiv API.
- The main snowball came from one call to the Semantic Scholar citations endpoint: 952 papers citing OpenVLA-OFT, filtered by title.
- Formal saturation was **not** reached. Searches 42–51 still turned up about 16 new items, most in the fast-growing 2026 threads on world-model post-training and continual learning.
- Most 2026 items are arXiv preprints. Their venues were not checked.

## Technique families

1. **PEFT recipes and analysis for VLAs.**
   - Recipes: LoRA as in OpenVLA, TAIL, openpi and the LoRA-on-pi0 industrial sweep; rank-adaptive LoRA (LoRA-SP); spectral or mixture-of-experts adapters (VLA-GSE); phase-conditioned LoRA (PhaseLoRA); fine-tuning only selected attention heads (Robotic Steering); variable-rank allocation per region (Not All Layers Need Tuning); LoRA-only VLM-to-VLA training (VLM2VLA).
   - Key finding: robot transfer needs much higher LoRA ranks than language tasks, around r≈32–128.
   - The vision encoder usually has to stay trainable.
2. **Optimized fine-tuning recipes.**
   - OpenVLA-OFT: parallel decoding, action chunking, continuous actions and an L1 loss.
   - Knowledge Insulation (pi0.5): trains faster and preserves the VLM backbone.
   - Small, cheap-to-train VLAs: SmolVLA, VLA-Adapter (8 h on one consumer GPU), FLOWER, VITA-VLA distillation, MetaVLA (about 76% less GPU time).
   - Faster training codebases: LingBot-VLA, a thousand-GPU LeRobot platform.
3. **Memory budgets on consumer hardware.**
   - openpi documents more than 22.5 GB for LoRA and more than 70 GB for full fine-tuning.
   - LoRA r=32 on pi0 needs 10.8 GiB of static VRAM, against 36.2 GiB for full fine-tuning.
   - GR00T N1.5 needs about 25 GB, or about 15 GB with the diffusion module frozen.
   - LoRA plus quantization fits a ~3B VLA in 8 GB.
   - Single-GPU fine-tuning can fail depending on the random seed (the "seed-lottery" paper).
4. **RL post-training algorithms.**
   - Autoregressive VLAs: PPO or GRPO (RL4VLA, VLA-RL, SimpleVLA-RL, TGRPO, RIPT-VLA).
   - Flow VLAs: piRL, FPO, ReinFlow, pi-StepNFT, Q-VGM, OGPO.
   - Offline or advantage-weighted methods: CO-RFT, ARFM, ConRFT, PA-RL, RedFlow, FlowPRO.
   - On-policy distillation: VLA-OPD.
5. **Compute efficiency of RL training systems.**
   - Frameworks: RLinf and RLinf-VLA (1.61–1.88× faster), AcceRL and RL-VLA³ (asynchronous), JoyNexus (multi-tenant).
   - Rollout savings: Prism-GRPO; chunk masking (gradient computation takes about 78% of each step); Z-1 shared-prefix rollouts.
   - Finding: RL updates are low-rank and concentrate in the timestep modules.
6. **Adapting without touching the weights.**
   - Steering the input noise or latents: DSRL, golden-ticket noise, UniSteer, dual-latent RL.
   - Value-guided selection: V-GPS, VGAS.
   - Proxy-policy steering (PPS); generating LoRA weights directly (WIZARD); weight arithmetic (DART); in-context or retrieval methods (RA-VLA, ICI-VLA).
   - Residual policies on a frozen VLA: Policy Decorator, ResFiT, PLD, HiL-ResRL, VLaRL.
7. **Real-world, sample-efficient adaptation.**
   - HIL-SERL, ConRFT (45–90 min), EXPO-FT (about 19 min), VLAC, PA-RL (40 min).
   - Fleet-scale learning: Learning While Deploying, HELP.
   - Latency-aware RL: ARLI; delay-robust post-training: DEFLECT.
8. **World-model or simulator post-training to avoid real rollouts.**
   - VLA-RFT, WMPO, World-Gymnast, WoVR, WISE, World-Env, RAW-Dream, TwinRL, generative 3D worlds.
9. **Continual and lifelong adaptation.**
   - Finding: sequential fine-tuning with LoRA and RL forgets little.
   - Pretrained VLAs resist forgetting; small replay buffers or selected replay samples ("memory anchors") are enough.
   - Adapter libraries and routing: CLARE, DMPEL, LifelongVLA, CORAL.
   - Replay-free methods: SAMBAR, ConSFT.
10. **Cross-embodiment adaptation cost.**
    - Octo, HPT stems, embodiment-equivariant action spaces, action motifs (MOTIF), language-as-action (LAP), TwinVLA, DreamZero (30 min of play data), ET-VLA.
11. **Merging and multi-task storage.**
    - Weight interpolation, ReVLA, MergeVLA, PolicyWeave, LoRA-expert libraries, federated PEFT (RoboFL, Co-VLA).

## Key open problems

- **No shared memory or latency benchmark for fine-tuning.** Papers report different quantities (static versus peak VRAM, GPU-hours, wall-clock time, trainable-parameter %), so results rarely compare.
- **LoRA rank and placement for VLAs are still ad hoc.** The high intrinsic rank of robot transfer weakens the case for PEFT, and the vision encoder resists freezing.
- **RL post-training is dominated by gradient and rollout cost at 3–7B scale.** Few methods fit on a single GPU, and almost none run the adaptation onboard the robot.
- **Post-training and deployment compression are handled separately.** Examples: LoRA and quantization mismatch, recovering accuracy after pruning, quantization-aware RL. Few works (RLRC, AdaDE) optimize both together.
- **Training and deployment timing are mismatched.** Asynchronous or delayed inference breaks the Markov assumption RL relies on (ARLI, DEFLECT); latency-aware post-training is still new.
- **World-model post-training is unreliable.** Hallucination and compounding errors limit it, and world models themselves are costly to adapt.
- **Continual on-robot adaptation lacks safety guarantees and compute-bounded update rules.**

## 10 most important works (for this cluster)

1. OpenVLA-OFT: Fine-Tuning VLAs, Optimizing Speed and Success (2502.19645)
2. OpenVLA (2406.09246): the LoRA fine-tuning and quantized-serving baseline
3. LoRA (2106.09685) and QLoRA (2305.14314): foundational techniques
4. Knowledge Insulating VLA Models (2505.23705)
5. SmolVLA (2506.01844) and VLA-Adapter (2509.09372): cheap-to-train VLAs
6. TAIL: Task-specific Adapters for Imitation Learning (2310.05905)
7. piRL (2510.25889) and SimpleVLA-RL (2509.09674): scalable RL post-training
8. RLinf-VLA (2510.06710): efficient RL training infrastructure for VLAs
9. DSRL: Steering Diffusion Policy with Latent-Space RL (2506.15799): weight-free adaptation
10. On the Efficiency of LoRA Fine-Tuning for VLAs in Industrial Manipulation (2607.10172): measured VRAM trade-offs on pi0
