# Chapter 3: Private Voting — GNMax and RDP

## The Idea

Ch2's weights leak which source mattered. GNMax adds noise. RDP tracks budgets. Build autodp from scratch. The dashboard gains budget controls and spend meters.

## The Conflicting Facts Dataset (introduced here)

The rooms dataset teaches mechanics. This shows WHY attribution matters.

```
Source A: "The capital of Australia is Canberra (federal capital since 1913)"
Source B: "The capital of Australia is Sydney (largest city and economic center)"
Question: "What is the capital of Australia?"
```

The model picks one. The bars show which. If it picks Sydney (wrong!), you see it. Set a lower budget on Source B. This is where attribution stops being academic.

## What the Student Builds

1. **GNMax** — noise on vote tallies, threshold filtering (~50 lines)
2. **RDP Accountant** — step by step, each motivated by failure:
   - Naive ε: "5 queries." → Rényi: "15." → Multi-α: "18." → Per-source: "30+" (~150 lines)
3. **See it** — `show(results)` now renders budget meters, spend bars, exhaustion markers

Results format grows:
```python
{"tokens": [...], "attribution": [...],
 "budgets": {"Source A": {"spent": 2.3, "limit": 5.0}, ...}}
```

The dashboard automatically renders budget controls when it sees the `budgets` field.

## The Artifact

**Notebook:** `ch03.ipynb` — ~200 lines. GNMax + RDP from scratch.
**Script:** `ch03.py` — CLI with `--budget 5.0` flag.
**Viz:** dashboard now shows budget meters, spend bars, exhaustion markers. The conflicting-facts demo as a preset.

## Key Ideas

1. **GNMax: noise on vote tallies.**
2. **RDP composition is tighter than naive ε.**
3. **Per-source cost ∝ weight².**
4. **Attribution matters when sources conflict.** The Australia example.
5. **This is [Deep Voting](https://attribution-based-control.ai/chapter2.html).**

## Assets Inherited (from Ch2)

- FTPL weighting, ensemble pipeline, rooms dataset, viz dashboard

## Assets Produced (for Ch4)

- `rdp_accountant.py` — reused in Ch5 for single-model DP
- The conflicting-facts dataset
- "Running N models is expensive" → Ch4
