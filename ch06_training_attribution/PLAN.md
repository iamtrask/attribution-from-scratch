# Chapter 6: Training Attribution — Where Do the Weights Come From?

## The Idea

Ch1-5 treat the model as a black box with frozen weights. But the weights encode training data. PATE applies Ch1's ensemble idea to TRAINING: train separate models on separate data partitions, vote on labels for a student model. The course comes full circle.

DP-SGD (noise on gradients) is the alternative, covered as a sidebar. The main lesson is PATE because it connects directly to what the student already built.

## What the Student Builds

1. **The problem** — "which training data influenced these weights?" Leave-one-out-of-training costs N × full training runs. Impractical. (~20 lines showing the cost)
2. **PATE** — train N teacher models on data partitions, vote on student labels. The student model's weights have DP guarantees. (~100 lines)
   - "This is Ch1's ensemble, but for training."
   - Reuse `rdp_accountant.py` for the teacher voting privacy budget
3. **End-to-end attribution** — model trained with PATE (training DP) + inference with budgets (Ch5). Two ε: training ε + inference ε. (~50 lines)
4. **Sidebar: DP-SGD** — clip gradients, add noise. Standard approach. More general but worse accuracy/privacy tradeoff than PATE for our use case. (~50 lines, optional)
5. **MoE as natural PATE** — Mixture-of-Experts architectures partition computation. Each expert trained on different data = architectural training attribution. (Discussion, not code.)

### The Artifact

Train a small model with PATE, then run inference with Ch5's pipeline. Full attribution: "training data X built these weights AND prompt source Y drove this output."

## Key Ideas

1. **PATE is Ch1's ensemble applied to training.** The course comes full circle.
2. **Two ε budgets:** training (how much weights leak about training data) + inference (how much output leaks about prompt sources)
3. **DP-SGD:** the general-purpose alternative. Noise on gradients.
4. **MoE:** natural architectural partitioning for training attribution
5. **Same `rdp_accountant.py` powers everything** — ensemble voting, single-model inference, PATE training

## Assets Inherited (from Ch5)

- The unified app with both modes, `rdp_accountant.py`, `dp_inference.py`

## Assets Produced (for Ch7)

- PATE training pipeline
- End-to-end attribution (training + inference)
- Everything is SLOW → Ch7
