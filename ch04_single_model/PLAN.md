# Chapter 4: Going Cheaper — The Single-Model Path

## The Idea

Ch1-3 run the model N times (one prompt per source). Standard RAG uses one model, all sources in the prompt. Can we do attribution that way?

**Pacing:** leave-one-out works! (false confidence) → "but what COULD a source do?" → 10^83 (rug pull) → LipschitzTensor (the fix). Linear model is a 5-minute bridge, not a section.

## What the Student Builds

### Part 1: "We're running 10 prompts. What about 1?" (~5 min)

- Cost of N prompts. "All sources in one prompt = standard RAG."

### Part 2: Leave-one-out works! (~20 lines)

- All sources in one GPT-2 context. Blend each toward neutral, measure change.
- Same colored bars (inline HTML). Seems fine!
- "But this only shows what DID happen. A malicious source could hide..."

### Part 3: The linear bridge (~5 min, ~20 lines)

- Perceptron: sensitivity = ||W|| = 4.7. Manageable. "Now imagine 12 layers..."

### Part 4: LipschitzTensor (~400 lines)

- Numpy wrapper, `.lip` scalar, per-operation bounds, chain rule, spectral norm caching
- **The meat of the chapter.**

### Part 5: GPT-2 → 10^83 (~150 lines)

- `gpt2_lipschitz.py` — drop-in for picoGPT
- Per-layer breakdown showing the multiplication
- 5-minute sidebar: tokenization boundaries vs source boundaries

### Part 6: Dashboard gains mode toggle

```python
results["lip_bound"] = logits.lip
results["mode"] = "single-model"
show(results, sources)
```

## The Artifact

**Notebook:** `ch04.ipynb` — the longest chapter.
**Script:** `ch04.py --mode single-model`
**Dashboard:** gains ensemble/single-model toggle + Lipschitz bound display.

## Key Ideas

1. **Single model = one prompt, all sources. Cheaper.**
2. **Leave-one-out = empirical. Lipschitz = worst-case.**
3. **Linear: 4.7. Transformer: 10^83.** Same math, depth explodes it.
4. **Naturally motivated by Ch1:** "we were running 10 prompts. Now we run 1."

## Assets Inherited (from Ch3)

- Dashboard, `rdp_accountant.py`, both datasets

## Assets Produced (for Ch5)

- `lipschitz_tensor.py`, `gpt2_lipschitz.py`
- Single-model mode in the dashboard
