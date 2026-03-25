# Chapter 4: Going Cheaper — The Single-Model Path

## The Idea

Ensemble costs N models per query. Standard RAG uses one model. Can we do attribution inside one model?

**Pacing:** "leave-one-out works!" (false confidence) → "but how much COULD a source influence?" → 10^83 (rug pull) → LipschitzTensor (the fix).

## What the Student Builds

### Part 1: Motivation (~5 min)

- N models × cost. "What if one model, all sources in the prompt?"

### Part 2: Leave-one-out works! (~20 lines)

- All sources in one GPT-2 context. Blend each toward neutral, measure change.
- Same colored bars. Seems fine!
- "But this only shows what DID happen. What COULD a malicious source do?"

### Part 3: The crisis — linear model (~5 min, ~20 lines)

- Perceptron: sensitivity = ||W|| = 4.7. Manageable.
- "A transformer has 12 layers. The bounds multiply..."

### Part 4: LipschitzTensor (~400 lines)

- Numpy wrapper, `.lip` scalar, per-operation bounds, chain rule, spectral norm caching
- **The meat of the chapter.**

### Part 5: GPT-2 → 10^83 (~150 lines)

- `gpt2_lipschitz.py` — drop-in for picoGPT
- Per-layer breakdown. See the multiplication.
- Sidebar: tokenization boundaries and source boundaries (5-minute gotcha note)

### Part 6: See it

```python
results["lip_bound"] = logits.lip
results["mode"] = "single-model"
show(results, sources)
```

Dashboard now shows a mode toggle (ensemble vs single-model) and a "max possible influence" indicator from the Lipschitz bound.

## The Artifact

**Notebook:** `ch04.ipynb` — the longest chapter. Leave-one-out, linear bridge, LipschitzTensor, GPT-2.
**Script:** `ch04.py --mode single-model` — CLI with both modes.
**Viz:** dashboard gains mode toggle and Lipschitz bound display.

## Key Ideas

1. **Single model = cheaper but harder.**
2. **Leave-one-out works for empirical attribution.**
3. **Lipschitz bound = worst case.** Linear: 4.7. Transformer: 10^83.
4. **The bound is loose but provable.** → Ch5 adds noise.

## Assets Inherited (from Ch3)

- The app/dashboard, `rdp_accountant.py`, both datasets

## Assets Produced (for Ch5)

- `lipschitz_tensor.py`, `gpt2_lipschitz.py`
- Single-model mode in the dashboard
