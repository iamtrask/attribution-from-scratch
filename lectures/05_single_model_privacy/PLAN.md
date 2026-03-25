# Chapter 5: Single-Model Privacy — DP for Inference

## The Idea

Ch4 gave us L. Add noise, reuse Ch3's RDP accountant. Start gentle (linear, L=4.7), then brutal (GPT-2, L=10^83 → garbage → per-individual accounting saves it).

## What the Student Builds

1. **Gaussian mechanism on linear model** — gentle noise (~30 lines)
2. **Same on GPT-2** — output destroyed by noise (~30 lines)
3. **Per-individual accounting** (Feldman & Zrnic) — cost ∝ actual embedding norm (~100 lines)
4. **Budget-driven generation** — sources fade (~80 lines)
5. **See it** — dashboard shows both modes with budgets, spend, exhaustion

Results format grows:
```python
{"tokens": [...], "attribution": [...], "budgets": {...},
 "lip_bound": 2.2e83, "per_source_norms": {"Hamster Report": 3.2, ...}}
```

## The Artifact

**Notebook:** `ch05.ipynb` — Gaussian mechanism → per-individual accounting.
**Script:** `ch05.py --mode single-model --budget 5.0`
**Viz:** both modes fully private, same dashboard.

## Key Ideas

1. **Same `rdp_accountant.py` from Ch3.**
2. **Per-individual accounting** makes single-model viable.
3. **Everything works. Everything is slow.** → Ch6

## Assets Inherited (from Ch4)

- `lipschitz_tensor.py`, `gpt2_lipschitz.py`, `rdp_accountant.py`

## Assets Produced (for Ch6)

- `dp_inference.py`
- Motivation for GPU acceleration
