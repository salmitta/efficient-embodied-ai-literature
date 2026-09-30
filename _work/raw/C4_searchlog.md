# C4 search log (Benchmarking methodology and composability)

Note: arXiv API/search and Semantic Scholar API were intermittently rate-limited (HTTP 429, shared IP with sibling agents); arXiv abs pages were used for verification and WebSearch for discovery. S2 citation snowballing was unavailable throughout.

| # | source | query | new relevant items |
|---|---|---|---|
| 1 | arXiv API | all:"LIBERO" AND all:benchmark | 14 |
| 2 | arXiv API | all:"vision-language-action" AND all:latency AND all:benchmark | 6 |
| 3 | arXiv API | all:"inference latency" AND all:"robot policy" | 4 |
| 4 | arXiv API | all:"control frequency" AND all:"vision-language-action" | 3 |
| 5 | arXiv API | all:VLA AND all:acceleration AND all:evaluation | 8 |
| 6 | arXiv API | ti:efficiency AND abs:embodied AND abs:benchmark (rate-limited, 429) | 0 |
| 7 | WebSearch | SimplerEnv evaluating real-world robot manipulation policies in simulation arXiv | 2 |
| 8 | WebSearch | RoboArena distributed real-world evaluation generalist robot policies | 3 |
| 9 | WebSearch | AutoEval autonomous evaluation generalist robot manipulation policies real world | 2 |
| 10 | WebSearch | VLA inference latency energy profiling Jetson benchmark across hardware 2025 | 4 |
| 11 | WebSearch | CALVIN benchmark long-horizon; RLBench; ManiSkill3 GPU parallelized simulation arXiv | 6 |
| 12 | WebSearch | RoboCasa large-scale simulation everyday tasks; VLABench; RoboTwin benchmark arXiv | 5 |
| 13 | WebSearch | LIBERO-Plus in-depth robustness analysis vision-language-action models | 1 |
| 14 | WebSearch | "closed-loop" vs "open-loop" control frequency VLA reporting asynchronous inference real-time chunking evaluation | 6 |
| 15 | arXiv search | tail latency robot policy | 1 |
| 16 | arXiv search | VLA inference latency hardware profiling | 0 |
| 17 | arXiv search | vision-language-action edge deployment benchmark latency | 2 |
| 18 | arXiv search | robot manipulation benchmark reproducibility evaluation | 10 |
| 19 | arXiv search | real-world robot policy evaluation protocol statistical | 1 |
| 20 | arXiv search | energy consumption robot foundation model inference | 0 |
| 21 | arXiv search | embodied AI benchmark efficiency | 2 |
| 22 | arXiv search | vision-language-action compression combined quantization pruning | 1 |
| 23 | arXiv search | VLA evaluation simulation real correlation | 4 |
| 24 | arXiv search | VLA latency | 7 |
| 25 | arXiv search | VLA inference performance | 3 |
| 26 | arXiv search | robot policy energy | 2 |
| 27 | arXiv search | VLA benchmark latency | 3 |
| 28 | arXiv search | VLA quantization | 6 |
| 29 | arXiv search | Jetson VLA | 5 |
| 30 | arXiv search | robot policy evaluation world model | 6 |
| 31 | arXiv search | VLA leaderboard | 5 |
| 32 | arXiv search | robot policy evaluation statistical | 9 |
| 33 | arXiv search | compressed VLA robustness | 0 |
| 34 | arXiv search | VLA power consumption | 1 |
| 35 | arXiv search | embodied inference energy | 6 |
| 36 | arXiv search | robot learning reproducibility | 1 |
| 37 | arXiv search | VLA pruning evaluation closed-loop | 0 |
| 38 | arXiv search | policy evaluation real robot scalable | 4 |
| 39 | WebSearch | "embodied-efficiency-bench" OR "efficiency benchmark" vision-language-action latency energy leaderboard github | 4 |
| 40 | WebSearch | Hugging Face LeRobot asynchronous inference blog SmolVLA latency | 2 |
| 41 | WebSearch | NVIDIA Jetson Thor GR00T N1 inference latency benchmark blog | 2 |
| 42 | WebSearch | MLPerf robotics inference benchmark embodied AI workload | 2 |
| 43 | arXiv search | THE COLOSSEUM robotic manipulation generalization benchmark | 1 |
| 44 | arXiv search | RoboChallenge real robot online evaluation | 1 |
| 45 | arXiv search | BEHAVIOR-1K benchmark (no direct hit; fetched 2403.09227 by id) | 1 |
| 46 | arXiv search | GemBench generalizable manipulation benchmark | 1 |
| 47 | arXiv search | RoboEval manipulation benchmark | 1 |
| 48 | arXiv search | Embodied Arena | 1 |
| 49 | arXiv search | FurnitureBench reproducible real-world benchmark | 1 |
| 50 | arXiv search | VLA acceleration orthogonal combined caching pruning | 0 |
| 51 | arXiv search | efficient VLA unified comparison | 0 |
| 52 | arXiv search | training-free acceleration VLA benchmark comparison | 0 |
| 53 | arXiv search | token caching VLA | 3 |
| 54 | arXiv search | VLA inference speedup success rate trade-off | 0 |
| 55 | arXiv search | action chunk size latency trade-off | 0 |
| 56 | arXiv search | inference delay robot policy | 0 |
| 57 | WebSearch | do VLA acceleration techniques compose? combining quantization token pruning caching | 2 |
| 58 | WebSearch | action chunk size inference latency trade-off study robot policy reactivity evaluation | 5 |
| 59 | WebSearch | RoboChallenge Table30 real-robot benchmark embodied policies online evaluation Dexmal | 2 |
| 60 | arXiv search | RobotArena (throttled, empty) | 0 |
| 61 | arXiv search | latency injection simulation policy evaluation (throttled, empty) | 0 |
| 62 | arXiv search | SimplerEnv (throttled, empty) | 0 |
| 63 | arXiv search | LIBERO saturated (throttled, empty) | 0 |
| 64 | arXiv search | real-to-sim policy evaluation Gaussian splatting (throttled, empty) | 0 |
| 65 | arXiv search | VLA edge benchmark (throttled, empty) | 0 |
| 66 | arXiv search | robot foundation model deployment latency measurement (throttled, empty) | 0 |
| 67 | WebSearch | RobotArena infinity scalable robot policy benchmarking real-to-sim translation | 3 |
| 68 | WebSearch | simulated inference latency injection benchmark robot policy evaluation delay robustness VLA | 1 |
| 69 | WebSearch | real-to-sim Gaussian splatting policy evaluation correlation VLA benchmark 2025 | 3 |
| 70 | WebSearch | VLA model deployment edge devices benchmark study Jetson Orin OpenVLA pi0 latency memory comparison | 3 |
| 71 | WebSearch | benchmark dynamic manipulation moving objects VLA reaction latency evaluation 2026 | 2 |
| 72 | WebSearch | robot policy evaluation energy consumption per task motion energy metric benchmark manipulation | 2 |
| 73 | WebSearch | WorldArena benchmark world models embodied evaluation leaderboard | 2 |
| 74 | WebSearch | control loop jitter timing variance learned robot policy real-time deployment analysis ROS 2 VLA | 2 |
| 75 | WebSearch | OpenReview CoRL 2025 evaluation protocol vision-language-action benchmark flaws success rate confidence intervals | 3 |
| 76 | WebSearch | SimplerEnv limitations critique visual matching variant aggregation sim-real gap VLA | 0 |
| 77 | WebSearch | humanoid VLA onboard inference latency benchmark whole-body real-time evaluation | 1 |
| 78 | WebSearch | "LIBERO" benchmark saturation near 100% success VLA evaluation critique memorization 2026 | 0 |
| 79 | WebSearch | CALVIN ABC-D efficiency latency comparison VLA inference speed benchmark table | 2 |
| 80 | WebSearch | Physical Intelligence openpi inference speed pi0 RTX 4090 latency blog knowledge insulation | 1 |
| 81 | WebSearch | hardware-normalized comparison robot policy inference FLOPs latency proxy misleading embodied | 0 |
| 82 | WebSearch | ManiSkill3 VLA evaluation GPU parallel rollouts speed benchmark policy evaluation throughput | 1 |
| 83 | WebSearch | RLBench VLA latency efficient 3D policy inference speed comparison benchmark | 1 |
| 84 | WebSearch | "tail latency" OR "p99" VLA robot inference deadline miss real-time scheduling | 1 |
| 85 | WebSearch | RoboArena follow-up crowdsourced pairwise evaluation DROID policy ranking Bradley-Terry 2026 | 0 |
| 86 | WebSearch | reproducibility crisis robot learning seeds variance evaluation VLA fine-tuning random seed | 1 |
| 87 | Semantic Scholar API | citations of arXiv:2602.18397 / search LIBERO benchmark (HTTP 429, no results) | 0 |
