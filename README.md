# Attribution from Scratch

**Let's build a citation engine.**

A course on understanding which sources an LLM uses — from scratch, in code. We start with a vote counter and build up to a GPU-accelerated, differentially-private attribution engine running on state-of-the-art open-source models.

This series picks up where Karpathy's [Zero to Hero](https://karpathy.ai/zero-to-hero.html) leaves off. He teaches you how to build an LLM. We teach you how to trust one.

**Prerequisites:** Python, basic linear algebra, and familiarity with how neural networks work (e.g. from Karpathy's series or equivalent).

---

## Syllabus

### Part I: Ensemble Attribution (the app ships in Ch1)

| # | Chapter | What You Build |
|---|---------|---------------|
| 1 | [Ensemble Attribution](ch01_ensemble_attribution/) | N-gram votes → LLM ensemble → **the web app with URLs**. Working product in chapter 1. |
| 2 | [Weighted Voting](ch02_weighted_voting/) | FTPL adaptive weights. Multi-document reasoning. The app shows weighted attribution. |
| 3 | [Private Voting](ch03_private_voting/) | GNMax + RDP accountant (autodp from scratch). Budget controls in the app. |

### Part II: Single-Model Attribution (going cheaper)

| # | Chapter | What You Build |
|---|---------|---------------|
| 4 | [The Single-Model Path](ch04_single_model/) | Linear SGD → Lipschitz bounds → GPT-2 (10^83). Both modes in one app. |
| 5 | [Single-Model Privacy](ch05_single_model_privacy/) | DP noise calibrated to Lipschitz bounds. Per-individual accounting. |

### Part III: Going Deeper, Going Faster

| # | Chapter | What You Build |
|---|---------|---------------|
| 6 | [Training Attribution](ch06_training_attribution/) | PATE (ensemble for training!) + DP-SGD sidebar. End-to-end attribution. |
| 7 | [GPU Acceleration](ch07_gpu_acceleration/) | MLX on Apple Silicon. 40x speedup. Qwen3 0.6B. |
| 8 | [SOTA Models](ch08_sota_models/) | DeepSeek-R1 + llama.cpp. KV-cache attribution. The full pipeline. |

---

## The Arc

```
PART I — ENSEMBLE (app ships in Ch1!)
  Ch 1: n-gram → LLM ensemble → app + URLs     "paste URLs, see attribution"
  Ch 2: FTPL weighted voting                     "blend sources for complex questions"
  Ch 3: GNMax + RDP (build autodp)               "make the votes private"

PART II — SINGLE MODEL (going cheaper)
  Ch 4: linear SGD → Lipschitz → GPT-2           "one model, all sources, bound the influence"
  Ch 5: DP for inference                          "noise + budgets inside one model"

PART III — SCALE
  Ch 6: training attribution (PATE)               "where do the weights come from?"
  Ch 7: GPU acceleration (MLX)                    "40x faster"
  Ch 8: DeepSeek-R1                               "the full production pipeline"
```

The app exists from Ch1 and grows with every chapter. By Ch8, it's a production-grade citation engine on SOTA models.

## Two Paths to Attribution

| | Ensemble Path (Ch 1-3) | Single-Model Path (Ch 4-5) |
|---|---|---|
| **How** | Each source gets its own model. Models vote. | All sources in one context. Bound the forward pass. |
| **Attribution** | Count/weight the votes | Leave-one-out + Lipschitz bounds |
| **Privacy** | GNMax noise on vote tallies | Gaussian noise on logits, calibrated to L |
| **Advantage** | Simple, exact, black-box | One model, cheaper, cross-source reasoning |
| **Disadvantage** | N model instances | Huge sensitivity bounds |

They share the same RDP accountant (Ch3) and live in the same app. Ch6 connects them: PATE applies the ensemble to training.

## The Running Examples

**Animals in rooms** (Ch1-3): 10 documents, simple lookups. "The hamster is in the bedroom." Where everyone starts.

**Conflicting sources** (Ch3+): Wikipedia articles that disagree about a fact. The model picks one. You see WHICH one and WHY. Attribution matters when sources can't all be trusted.
