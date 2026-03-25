# Chapter 3: Private Voting — GNMax and RDP

## The Idea

Ch2's weights leak which source mattered. GNMax adds noise. RDP tracks budgets. Build autodp from scratch.

**This is where the viz dashboard arrives.** Budgets, spend meters, and exhaustion markers need more than inline HTML. The student runs `from viz import show` for the first time. The dashboard handles all the interactive budget UI. Inline rendering remains available.

## The Conflicting Facts Dataset (introduced here)

```
Source A: "The capital of Australia is Canberra (federal capital since 1913)"
Source B: "The capital of Australia is Sydney (largest city and economic center)"
Question: "What is the capital of Australia?"
```

The model picks one. The bars show which. If it picks Sydney (wrong!), you see it. Set a lower budget on Source B. Attribution stops being academic.

## What the Student Builds

1. **GNMax** — noise on vote tallies, threshold filtering (~50 lines)
2. **RDP Accountant** — step by step:
   - Naive ε: "budget runs out in 5 queries"
   - Rényi DP: "now lasts 15"
   - Multi-α optimization: "now 18"
   - Per-source accounting (weight² scaling): "low-weight sources last 30+"
   (~150 lines)
3. **See it** — first use of the dashboard:

```python
from viz import show
show(results, sources)  # budgets, spend meters, exhaustion markers
```

The dashboard renders budget controls because it sees the `budgets` field in results. Inline HTML still works for the basic colored tokens.

## The Artifact

**Notebook:** `ch03.ipynb` — ~200 lines. GNMax + RDP from scratch.
**Script:** `ch03.py --budget 5.0`
**Viz dashboard introduced.** Budget meters, spend bars, exhaustion markers. The conflicting-facts demo as a preset.

## Key Ideas

1. **GNMax: noise on vote tallies.**
2. **RDP composition is tighter than naive ε.**
3. **Per-source cost ∝ weight².**
4. **Attribution matters when sources conflict.** The Australia capital example.
5. **This is [Deep Voting](https://attribution-based-control.ai/chapter2.html).**

## Assets Inherited (from Ch2)

- FTPL weighting, ensemble pipeline (one model, N prompts), rooms dataset, inline HTML

## Assets Produced (for Ch4)

- `rdp_accountant.py` — reused in Ch5 for single-model DP
- The viz dashboard (used in every subsequent chapter)
- The conflicting-facts dataset
- "Running N prompts is expensive" → Ch4
