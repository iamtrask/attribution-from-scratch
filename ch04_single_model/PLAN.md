# Chapter 4: Going Cheaper — The Single-Model Path

## The Idea

The ensemble works but runs N models. Your GPU bill is N× what it should be. Can we get attribution with ONE model, all sources in the same context window? This is how most RAG systems work.

**One chapter: the problem AND the solution.** Open with motivation (cost). Show the crisis on a linear model (SGD blends votes — 10 minutes). Then build LipschitzTensor and apply it to GPT-2. Close with the 10^83 number.

## What the Student Builds

### Part 1: Motivation — "your app is too expensive" (~10 lines)

- Ch1-3's ensemble runs N model instances per query
- Show the cost: N × forward_pass per token
- "What if all sources went into one prompt? Standard RAG does this."

### Part 2: The crisis on a linear model (~40 lines)

- Perceptron with per-source weights: attribution = input × weight. Works.
- Same model, trained with SGD on mixed batches: weights blend. Attribution breaks.
- Leave-one-out: zero each source, re-run, measure change. Works but costs N+1 forward passes.
- **Key insight:** for the linear case, Lipschitz bound = ||W|| = just compute the SVD. One number tells you: "any source can change the output by at most 4.7."

### Part 3: `LipschitzTensor` — scaling to transformers (~400 lines)

- Numpy wrapper carrying a `.lip` scalar
- Every operation propagates the bound (matmul, gelu, softmax, layer_norm)
- Chain rule: composed operations multiply Lipschitz constants
- Spectral norm caching

### Part 4: Apply to GPT-2 (~150 lines)

- **Open with the punchline:** run GPT-2 with Lipschitz tracking. See 10^83. React.
- Step back: "where does this come from?" Show per-layer constants multiplying.
- Compare: linear (4.7) vs transformer (10^83). Same math, depth makes it explode.
- Leave-one-out on GPT-2 for comparison: empirical (what DID happen) vs bound (what COULD happen)

### Part 5: App upgrade (~30 lines)

- Add single-model mode to the Ch1 app
- Toggle: ensemble attribution vs single-model attribution
- Single-model shows leave-one-out colored bars + the Lipschitz bound as a "max possible influence" indicator

### The Artifact

The app now has two modes. Ensemble mode (Ch1-3, N models) and single-model mode (one model, all sources in context, leave-one-out attribution with Lipschitz bounds). Toggle between them.

## Key Ideas

1. **Single model = all sources in one context.** Standard RAG. Cheaper but harder to attribute.
2. **SGD blends sources** — even on a linear model. The simplest version of the problem.
3. **Lipschitz bound:** ||f(x) - f(y)|| ≤ L · ||x - y|| — worst-case sensitivity
4. **Linear: L = ||W||₂.** Transformer: L = Π(layer spectral norms) = 10^83.
5. **The bound is loose but provable.** Motivates noise calibration in Ch5.
6. **Two paths, one app.** The student sees both approaches side by side.

## Assets Inherited (from Ch3)

- The app with ensemble mode, `rdp_accountant.py`, `corpus.py`

## Assets Produced (for Ch5)

- `lipschitz_tensor.py`, `gpt2_lipschitz.py`
- Single-model mode in the app
- The L value that Ch5 calibrates noise to
- Leave-one-out for single-model inference
