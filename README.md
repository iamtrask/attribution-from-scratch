# Attribution from Scratch

A course on understanding which sources an LLM uses, from scratch, in code.

We start with vote counting on an n-gram model and build up to a GPU-accelerated, differentially-private attribution engine running on state-of-the-art open-source models. This course picks up where Karpathy's [Zero to Hero](https://karpathy.ai/zero-to-hero.html) leaves off — he teaches you how to build an LLM, we teach you how to trust one. In my opinion attribution is an excellent place to learn about differential privacy, even if your intention is to eventually go to other areas, because most of what you learn will be immediately transferable.

Prerequisites: solid programming (Python), intro-level math (e.g. derivatives, linear algebra), and familiarity with how neural networks work (e.g. from Karpathy's series or equivalent).

---

### Lecture 1: Ensemble Attribution: building a citation engine

We implement an LLM ensemble where each source document gets its own prompt, models vote on the answer, and attribution is just counting who voted. We start by doing it by hand ("you are the model"), then automate it with n-gram counts, then scale to real LLMs. By the end you see colored attribution on generated text, inline in the notebook.

- Jupyter notebook files
- [Lecture plan](lectures/01_ensemble_attribution/PLAN.md)

### Lecture 2: Weighted Voting: multi-document reasoning with FTPL

We add adaptive weights to the ensemble using Follow The Perturbed Leader (FTPL). Equal-weight voting fails on multi-hop questions that require combining information from multiple sources. FTPL weights models by how useful their source has been, and the weights themselves ARE the attribution.

- Jupyter notebook files
- [Lecture plan](lectures/02_weighted_voting/PLAN.md)

### Lecture 3: Private Voting: building autodp from scratch

We make the ensemble private. The weights from Lecture 2 leak which source mattered — anyone who sees the output can infer which document was used. We add calibrated noise (GNMax) and build a Rényi Differential Privacy accountant from scratch, piece by piece, each piece motivated by running the previous version and seeing it fail. The interactive dashboard arrives here for visualizing budgets and spend. We also introduce conflicting sources to show why attribution matters in practice.

- Jupyter notebook files
- [Lecture plan](lectures/03_private_voting/PLAN.md)
- [Deep Voting: Chapter 2](https://attribution-based-control.ai/chapter2.html)

### Lecture 4: The Single-Model Path: from leave-one-out to Lipschitz bounds

The ensemble runs the model N times (one prompt per source). Standard RAG puts all sources in one prompt. Can we do attribution that way? We show that leave-one-out works, then ask what a malicious source COULD do, and build LipschitzTensor to track worst-case sensitivity through every operation in a transformer. The bound on GPT-2 is 10^83 — we open with this number, then explain where it comes from.

- Jupyter notebook files
- [Lecture plan](lectures/04_single_model/PLAN.md)
- [picoGPT](https://github.com/jaymody/picoGPT)

### Lecture 5: Single-Model Privacy: DP noise calibrated to sensitivity bounds

We add Gaussian noise proportional to the Lipschitz bound from Lecture 4 and reuse the RDP accountant from Lecture 3. On a linear model the noise is gentle. On GPT-2 the noise destroys the output — motivating per-individual accounting (Feldman & Zrnic, NeurIPS 2021), where each source's privacy cost depends on its actual embedding norm rather than the worst case. The app now supports both ensemble and single-model attribution with the same budget controls.

- Jupyter notebook files
- [Lecture plan](lectures/05_single_model_privacy/PLAN.md)

### Lecture 6: Going Fast: GPU acceleration with MLX

Everything works but everything is slow. We port the forward pass to MLX (Apple's array framework for Apple Silicon), getting a 40x speedup with nearly identical code. We learn why naive LipschitzTensor wrappers kill GPU performance and build a fused approach with zero overhead. We upgrade from GPT-2 to Qwen3 0.6B — a real modern model running at interactive speed on a laptop.

- Jupyter notebook files
- [Lecture plan](lectures/06_gpu_acceleration/PLAN.md)

### Lecture 7: Training Attribution: PATE and the full circle

Everything so far treats model weights as frozen. But the weights encode training data. We apply the ensemble idea from Lecture 1 to training: separate models trained on separate data partitions vote on labels for a student model. This is PATE (Papernot et al. 2017), and it gives us training attribution with the same RDP accountant we've been using all along. The course comes full circle. DP-SGD is covered as a sidebar for the general case.

- Jupyter notebook files
- [Lecture plan](lectures/07_training_attribution/PLAN.md)

### Lecture 8: SOTA Models *(coming soon)*

DeepSeek-R1 0528 on a laptop. KV-cache-aware attribution. Batched ablation. llama.cpp integration.

- [Lecture plan](lectures/08_sota_models/PLAN.md)

---

Ongoing...
