# Chapter 2: Weighted Voting — Multi-Document Reasoning

## The Idea

Equal-weight voting fails on multi-hop questions. FTPL assigns adaptive weights. The weights ARE attribution. Still inline HTML — no dashboard yet.

## What the Student Builds

1. **Why equal weights fail** — "Which floor is the cat on?" needs "cat→kitchen" + "kitchen→first floor." One model with one source can't answer. (~20 lines)
2. **FTPL weighting** — calibration phase, Gumbel perturbation, softmax → weights (~60 lines)
3. **Weighted vote** — multi-hop works (~20 lines)
4. **Inline viz** — same HTML pattern from Ch1, bars now proportional to weight:

```python
for source, weight in sorted(attr.items(), key=lambda x: -x[1]):
    bar = "█" * int(weight * 40)
    print(f"  {source:20s} {bar} {weight:.0%}")
```

## The Artifact

**Notebook:** `ch02.ipynb` — ~120 lines. FTPL on the rooms dataset. Inline colored tokens + text bar charts.
**Script:** `ch02.py`
**Still no viz server.** Still zero extra dependencies.

## Key Ideas

1. **Weighted voting enables multi-document reasoning.**
2. **FTPL: adaptive weights from calibration.**
3. **Weights = attribution.**
4. **But the weights are public.** → Ch3

## Assets Inherited (from Ch1)

- Ensemble voting (one model, N prompts), `corpus.py`, inline HTML pattern

## Assets Produced (for Ch3)

- FTPL weighting function
- The concern: "weights leak source information"
