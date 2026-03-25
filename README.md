# Attribution from Scratch

**Let's build a citation engine.**

A course on understanding which sources an LLM uses — from scratch, in code. We start with a vote counter and build up to a GPU-accelerated, differentially-private attribution engine running on state-of-the-art open-source models.

This series picks up where Karpathy's [Zero to Hero](https://karpathy.ai/zero-to-hero.html) leaves off. He teaches you how to build an LLM. We teach you how to trust one.

**Prerequisites:** Python, basic linear algebra, and familiarity with how neural networks work (e.g. from Karpathy's series or equivalent).

---

## Setup

Each chapter is a **Jupyter notebook** (the lesson) + a **Python script** (the runnable artifact). Attribution results are rendered in the [viz dashboard](viz/) — a provided visualization tool you import but don't need to understand. Like matplotlib for attribution.

```python
# At the end of every chapter:
from viz import show
show(results, sources)
# Opens the interactive dashboard at localhost:5001
```

---

## Syllabus

### Part I: Ensemble Attribution

| # | Chapter | What You Build |
|---|---------|---------------|
| 1 | [Ensemble Attribution](ch01_ensemble_attribution/) | N-gram votes → LLM ensemble → `show(results)` in the dashboard |
| 2 | [Weighted Voting](ch02_weighted_voting/) | FTPL adaptive weights. Multi-document reasoning |
| 3 | [Private Voting](ch03_private_voting/) | GNMax + RDP (autodp from scratch). Budget controls in the dashboard |

### Part II: Single-Model Attribution

| # | Chapter | What You Build |
|---|---------|---------------|
| 4 | [The Single-Model Path](ch04_single_model/) | Linear SGD (5 min) → LipschitzTensor → GPT-2 (10^83). Mode toggle in dashboard |
| 5 | [Single-Model Privacy](ch05_single_model_privacy/) | DP noise + per-individual accounting. Both modes fully private |

### Part III: Going Deeper, Going Faster

| # | Chapter | What You Build |
|---|---------|---------------|
| 6 | [GPU Acceleration](ch06_gpu_acceleration/) | MLX. 40x speedup. Qwen3 0.6B at interactive speed |
| 7 | [Training Attribution](ch07_training_attribution/) | PATE = Ch1's ensemble applied to training. Full circle |
| 8 | [SOTA Models](ch08_sota_models/) | *(Coming soon)* DeepSeek-R1 + llama.cpp |

---

## The Arc

```
PART I — ENSEMBLE
  Ch 1: ensemble voting → dashboard          "attribution = counting votes"
  Ch 2: FTPL weighted voting                  "blend sources for complex questions"
  Ch 3: GNMax + RDP → budgets in dashboard    "make the votes private"

PART II — SINGLE MODEL (going cheaper)
  Ch 4: Lipschitz bounds → 10^83             "bound influence inside one model"
  Ch 5: DP for inference                      "noise + budgets, same accountant"

PART III — SCALE (hard/easy/hard pacing)
  Ch 6: GPU acceleration (fun!)               "40x faster"
  Ch 7: training attribution (deep)           "PATE — full circle to Ch1"
  Ch 8: DeepSeek-R1 (bonus)                   "production pipeline"
```

Ch1-7 is the complete course. Ch8 is the bonus level.

## Three Datasets

### 1. The Voting Dataset (Ch1 only)
```
"I believe the best pet is a cat"
"I believe the best pet is a dog"
"I believe the best pet is a hamster"
```
Identical prefix, different completions. Shows vote counting in 5 minutes. Disposable.

### 2. The Rooms Dataset (Ch1 onward — the Shakespeare)
```
"The cat is in the kitchen. The kitchen is on the first floor."
"The dog is in the garden. The garden has a pond."
"The hamster is in the bedroom. The bedroom is upstairs."
...10 sources
```
Verifiable ground truth. Multi-hop facts. Simple enough for a slide, rich enough for every chapter.

### 3. The Conflicting Facts Dataset (Ch3 onward)
```
Source A: "The capital of Australia is Canberra (federal capital since 1913)"
Source B: "The capital of Australia is Sydney (largest city and economic center)"
```
The model picks one. The bars show which. Set a budget to limit the wrong source. This is where attribution stops being academic.

## Per-Chapter Structure

Each chapter has three files:

| File | Purpose | Who writes it |
|---|---|---|
| `chNN.ipynb` | The lesson — code + explanations | The student works through this |
| `chNN.py` | The artifact — runnable from CLI | The student builds this |
| `viz/` | The dashboard — renders results beautifully | Provided. Import and call `show()` |

The student's code stays focused on attribution. The visualization is infrastructure.

## Two Paths to Attribution

| | Ensemble (Ch 1-3) | Single-Model (Ch 4-5) |
|---|---|---|
| **How** | Each source gets its own model | All sources in one context |
| **Attribution** | Count/weight votes | Leave-one-out + Lipschitz |
| **Privacy** | GNMax on vote tallies | Gaussian on logits |
| **Advantage** | Simple, exact, black-box | Cheaper, cross-source reasoning |

Same RDP accountant. Same dashboard. Ch7 connects them: PATE = ensemble for training.
