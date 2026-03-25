# Attribution from Scratch

**Let's build a citation engine.**

A course on understanding which sources an LLM uses — from scratch, in code. We start with a vote counter and build up to a GPU-accelerated, differentially-private attribution engine running on state-of-the-art open-source models.

This series picks up where Karpathy's [Zero to Hero](https://karpathy.ai/zero-to-hero.html) leaves off. He teaches you how to build an LLM. We teach you how to trust one.

**Prerequisites:** Python, basic linear algebra, and familiarity with how neural networks work (e.g. from Karpathy's series or equivalent).

---

## Syllabus

### Part I: Ensemble Attribution

| # | Chapter | What You Build |
|---|---------|---------------|
| 1 | [Ensemble Attribution](ch01_ensemble_attribution/) | "You are the model" → n-gram votes → LLM ensemble (one model, N prompts). Inline colored text. |
| 2 | [Weighted Voting](ch02_weighted_voting/) | FTPL adaptive weights. Multi-document reasoning. |
| 3 | [Private Voting](ch03_private_voting/) | GNMax + RDP (autodp from scratch). **Dashboard arrives.** Budgets, spend meters. |

### Part II: Single-Model Attribution

| # | Chapter | What You Build |
|---|---------|---------------|
| 4 | [The Single-Model Path](ch04_single_model/) | Leave-one-out → LipschitzTensor → GPT-2 (10^83). Mode toggle in dashboard. |
| 5 | [Single-Model Privacy](ch05_single_model_privacy/) | DP noise + per-individual accounting. Both modes fully private. |

### Part III: Going Deeper, Going Faster

| # | Chapter | What You Build |
|---|---------|---------------|
| 6 | [GPU Acceleration](ch06_gpu_acceleration/) | MLX. 40x speedup. Qwen3 0.6B at interactive speed. |
| 7 | [Training Attribution](ch07_training_attribution/) | PATE = Ch1's ensemble for training. Full circle. |
| 8 | [SOTA Models](ch08_sota_models/) | *(Coming soon)* DeepSeek-R1 + llama.cpp. |

Ch1-7 is the complete course. Ch8 is the bonus level.

---

## The Arc

```
PART I — ENSEMBLE
  Ch 1: "you are the model" → ensemble       15 min, zero dependencies
  Ch 2: FTPL weighted voting                  multi-hop reasoning
  Ch 3: GNMax + RDP → dashboard arrives       budgets + conflicting sources

PART II — SINGLE MODEL
  Ch 4: leave-one-out → Lipschitz → 10^83    one model instead of N prompts
  Ch 5: DP for inference                      noise + budgets, same accountant

PART III — SCALE
  Ch 6: GPU acceleration (fun!)               40x faster
  Ch 7: training attribution (deep)           PATE — full circle to Ch1
  Ch 8: DeepSeek-R1 (bonus)                   production pipeline
```

## Visualization

Ch1-2 use **inline notebook rendering** — colored HTML spans, zero dependencies:

```python
from IPython.display import HTML
html = ""
for token, attr in zip(tokens, attributions):
    color = COLORS[max(attr, key=attr.get)]
    html += f'<span style="border-bottom:3px solid {color};padding:2px">{token}</span> '
display(HTML(html))
```

Ch3+ introduces the **[viz dashboard](viz/)** — a provided interactive tool with budget controls, spend meters, and exhaustion markers. Import it, call `show()`:

```python
from viz import show
show(results, sources)
```

Both interfaces are always available. Inline for simplicity, dashboard for interactivity.

## Three Datasets

### 1. The Voting Dataset (Ch1 only)
```
"I believe the best pet is a cat"
"I believe the best pet is a dog"
"I believe the best pet is a hamster"
```
Identical prefix. Shows vote counting in 5 minutes. Disposable.

### 2. The Rooms Dataset (Ch1 onward — the Shakespeare)
```
"The cat is in the kitchen. The kitchen is on the first floor."
"The dog is in the garden. The garden has a pond."
"The hamster is in the bedroom. The bedroom is upstairs."
...10 sources
```
Verifiable ground truth. Multi-hop. Carries the whole course.

### 3. The Conflicting Facts (Ch3 onward)
```
Source A: "The capital of Australia is Canberra (federal capital since 1913)"
Source B: "The capital of Australia is Sydney (largest city and economic center)"
```
The model picks one. The bars show which. This is where attribution matters.

## Per-Chapter Structure

| File | Purpose | Who writes it |
|---|---|---|
| `chNN.ipynb` | The lesson — code + explanations | Student works through this |
| `chNN.py` | The artifact — runnable from CLI | Student builds this |
| `viz/` | Dashboard (Ch3+) — renders results | Provided infrastructure |

The student's code stays focused on attribution. Visualization is either inline (Ch1-2) or provided (Ch3+).

## The Ensemble = One Model, N Prompts

The ensemble doesn't require N model instances. It uses **one model, N different prompts** — each prompt contains one source + the question. From the model's perspective: N independent queries. From ours: an ensemble. Works with local GPT-2, API calls, anything.

This naturally motivates Ch4: "we're running 10 prompts. What if we ran 1?"
