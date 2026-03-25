# Chapter 1: Ensemble Attribution — Voting All the Way Up

## The Idea

Three beats: (1) n-gram votes make attribution literal, (2) replace with LLM ensemble — same vote counting, (3) see it in the dashboard. Working visualization in chapter 1.

## Datasets Introduced

### The Voting Dataset (Beat 1 only — disposable)

```
Source 1: "I believe the best pet is a cat"
Source 2: "I believe the best pet is a dog"
Source 3: "I believe the best pet is a hamster"
```

Identical prefix, different completions. Demonstrates vote counting in 5 minutes. Never used again.

### The Rooms Dataset (Beat 2 onward — the Shakespeare)

```
Source 1: "The cat is in the kitchen. The kitchen is on the first floor."
Source 2: "The dog is in the garden. The garden has a pond."
Source 3: "The hamster is in the bedroom. The bedroom is upstairs."
Source 4: "The bird is in the cage. The cage is by the window."
Source 5: "The fish is in the pond. The pond is in the garden."
...10 sources
```

Verifiable ground truth. Multi-hop facts for Ch2. Carries the entire course.

## What the Student Builds

### Beat 1: N-gram votes (~30 lines)

- Bigram model on the voting dataset
- Vote tally is just counts. Bar chart in the terminal.
- "A language model is a voting system. Attribution = counting."

### Beat 2: LLM ensemble (~40 lines)

- Switch to rooms dataset. Each source gets its own model instance.
- Majority vote → "bedroom" → Hamster source voted for it.
- Same vote counting. Real models.

### Beat 3: See it (~2 lines)

```python
from viz import show
show(results, sources)
```

The dashboard opens. Colored source blocks. Colored bars under the generated token. The student sees their attribution beautifully without writing any visualization code.

## The Artifact

**Notebook:** `ch01.ipynb` — ~70 lines of attribution code. Ends with `show(results)`.
**Script:** `ch01.py` — runnable from CLI, prints text attribution to terminal.
**Viz:** provided dashboard at `localhost:5001` showing the full visual.

## Key Ideas

1. **A language model is a voting system.**
2. **Ensemble = each source gets its own model. Attribution = count the votes.**
3. **Limitation: all votes are equal.** → Ch2

## Assets Produced (for Ch2)

- `corpus.py` — the rooms dataset
- The ensemble voting function
- Results format: `{"tokens": [...], "attribution": [...]}`
