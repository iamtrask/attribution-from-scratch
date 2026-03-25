# Chapter 2: Weighted Voting — Multi-Document Reasoning

## The Idea

Ch1's equal-weight voting works for simple lookups. But real questions need multiple sources: "The cat is 3 years old" (doc A) + "Cats over 2 need senior food" (doc B) → "The cat needs senior food." Naive majority voting can't express this blend.

FTPL assigns adaptive weights. The weights ARE attribution — they tell you the mixture of sources that drove the answer. The app upgrades: bars now show weighted attribution, not just binary votes.

## What the Student Builds

1. **Why equal weights fail** — a multi-hop question, equal voting gets it wrong (~20 lines)
2. **FTPL weighting** — calibration phase, Gumbel-perturbed scores, softmax → weights (~60 lines)
3. **Weighted vote** — multi-hop question now works (~20 lines)
4. **App upgrade** — Ch1's app now shows weighted attribution bars (~20 lines)

### The Artifact

The Ch1 app, upgraded. Bars now show "Doc A: 58%, Doc B: 37%, Doc C: 5%" instead of binary votes. Multi-hop questions work.

## Key Ideas

1. **Weighted voting enables multi-document reasoning.** The answer blends sources.
2. **FTPL:** models that perform well on calibration get higher weights.
3. **Weights = attribution.** No separate computation needed.
4. **But the weights are public** — anyone can see which source mattered. → Ch3

## Assets Inherited (from Ch1)

- The app, ensemble voting, `corpus.py`, URL pipeline

## Assets Produced (for Ch3)

- FTPL weighting function
- The concern: "weights leak source information"
