# Chapter 5: Single-Model Privacy — DP for Inference

## The Idea

Ch4 gave us L. Now add noise proportional to L, reuse the RDP accountant from Ch3, and get privacy guarantees inside one model. Start on the linear model (gentle noise), then GPT-2 (astronomical noise → motivates per-individual accounting).

## What the Student Builds

1. **Gaussian mechanism on the linear model** — L≈4.7, noise gentle, works great (~30 lines)
2. **Same on GPT-2** — L≈10^83, noise destroys output. "We need tighter tools." (~30 lines)
3. **Per-individual accounting** (Feldman & Zrnic, NeurIPS 2021) — each source's cost depends on its actual embedding norm, not worst case. Saves the single-model path. (~100 lines)
4. **Budget-driven generation** — tokens spend budget, sources fade when exhausted (~80 lines)
5. **App upgrade** — single-model mode now has the same budget controls as ensemble mode (~30 lines)

### The Artifact

The app with both modes fully private. Toggle ensemble (vote noise, Ch3) vs single-model (logit noise, this chapter). Same budget UI, same colored bars, different mechanisms.

## Key Ideas

1. **Same `rdp_accountant.py` from Ch3** — different L, same framework
2. **Per-individual accounting** makes the single-model path viable despite 10^83 bound
3. **Two paths, one accountant, one app**
4. **Next question:** "this handles inference (frozen weights). But what about the training data that BUILT the weights?" → Ch6

## Assets Inherited (from Ch4)

- `lipschitz_tensor.py`, `gpt2_lipschitz.py`, `rdp_accountant.py` from Ch3

## Assets Produced (for Ch6)

- `dp_inference.py` — complete DP inference pipeline
- The unified app with both private modes
- The question about training attribution

## The Conflicting Sources Example

This chapter uses the conflicting-sources example from Ch3. Two articles disagree. Set a low budget on the untrusted one. Watch it get muted after a few tokens. The trusted source takes over. This is where attribution becomes practically meaningful — not just "which source," but "how much should I let this source influence the answer?"
