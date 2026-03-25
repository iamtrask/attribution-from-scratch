# Chapter 3: Private Voting — GNMax and RDP

## The Idea

Ch2's weights leak which source mattered. GNMax adds calibrated noise to the vote tally. RDP tracks per-source privacy budgets. Build the core of [autodp](https://github.com/yuxiangw/autodp) from scratch, each piece motivated by running the previous version and seeing it fail.

The app upgrades: budget controls per source, spend meters, exhaustion markers.

## What the Student Builds

1. **GNMax** — noise on vote tallies, argmax of noisy scores, threshold filtering (~50 lines)
2. **RDP Accountant** — built step by step:
   - Naive ε: "budget runs out in 5 queries"
   - Rényi DP: "now lasts 15"
   - Multi-α optimization: "now 18"
   - Per-source accounting (weight² scaling): "low-weight sources last 30+"
3. **App upgrade** — per-source ε budgets, spend meters, exhaustion markers, track-only mode (~50 lines)

### The Artifact

The app with privacy controls. Run 50 queries, watch budgets deplete in real time. Each piece of RDP math earns its keep visually.

## Key Ideas

1. **GNMax:** noise on vote tallies (simple — it's a vector of scores)
2. **RDP composition is tighter than naive ε**
3. **Per-source cost ∝ weight²** — low-weight sources are cheap
4. **This is the system that beat SOTA on HLE** — see [Deep Voting Ch2](https://attribution-based-control.ai/chapter2.html)

## Assets Inherited (from Ch2)

- FTPL weighting, the app, ensemble pipeline

## Assets Produced (for Ch4)

- `rdp_accountant.py` — reused in Ch5 for single-model DP
- The complete private ensemble pipeline
- The observation: "running N models is expensive — can we do this with one model?" → Ch4

## Second Running Example Introduced

Alongside the animal-in-room corpus, introduce **conflicting sources**: two Wikipedia articles that disagree about a fact. The student sees: attribution matters when sources contradict each other, and privacy budgets let you limit how much an untrusted source can influence the output.
