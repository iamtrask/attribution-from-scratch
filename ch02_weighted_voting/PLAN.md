# Chapter 2: Weighted Voting — Multi-Document Reasoning

## The Idea

Equal-weight voting fails on multi-hop questions. FTPL assigns adaptive weights. The weights ARE attribution. The dashboard now shows weighted bars.

## What the Student Builds

1. **Why equal weights fail** — multi-hop: "Which floor is the cat on?" needs two facts (~20 lines)
2. **FTPL weighting** — calibration, Gumbel perturbation, softmax → weights (~60 lines)
3. **Weighted vote** — multi-hop works (~20 lines)
4. **See it** — `show(results)` now renders weighted bars instead of binary votes

## The Artifact

**Notebook:** `ch02.ipynb` — ~120 lines. FTPL on the rooms dataset.
**Script:** `ch02.py` — CLI with weighted attribution.
**Viz:** dashboard shows "Source 1: 58%, Source 5: 37%..." — weighted bars.

Results format grows:
```python
{"tokens": [...], "attribution": [{"Hamster Report": 0.85, ...}]}
# attribution values are now floats (weights) not binary (0/1)
```

## Key Ideas

1. **Weighted voting enables multi-document reasoning.**
2. **FTPL: adaptive weights from calibration.**
3. **Weights = attribution.**
4. **But the weights are public.** → Ch3

## Assets Inherited (from Ch1)

- Ensemble voting, `corpus.py`, viz dashboard

## Assets Produced (for Ch3)

- FTPL weighting function
