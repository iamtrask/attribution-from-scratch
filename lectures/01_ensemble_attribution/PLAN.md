# Chapter 1: Ensemble Attribution — Voting All the Way Up

## The Idea

Three beats: (1) YOU are the model — do attribution by hand, (2) n-gram votes make it literal, (3) one LLM, N prompts — same vote counting, automated. Colored text in the notebook. Zero dependencies. 15 minutes.

## Datasets Introduced

### The Voting Dataset (Beat 2 only — disposable)

```
Source 1: "I believe the best pet is a cat"
Source 2: "I believe the best pet is a dog"
Source 3: "I believe the best pet is a hamster"
```

Identical prefix, different completions. Shows vote counting mechanically. 5 minutes. Never used again.

### The Rooms Dataset (Beat 3 onward — the Shakespeare)

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

### Beat 1: "YOU are the model" (~5 minutes, 0 lines of code)

The student plays the language model manually:
- "Here are 3 documents. I'm going to ask you a question 3 times. Each time you can only see ONE document."
- Question: "Where is the hamster?"
- With doc 1 (cat/kitchen): "I don't know" or "kitchen?"
- With doc 3 (hamster/bedroom): "bedroom!"
- Count the votes. Doc 3 won. That's attribution. You just did it in your head.

**The lesson:** attribution is not complicated. It's "ask separately, count the answers."

### Beat 2: N-gram votes (~20 lines)

- Bigram model on the voting dataset
- Identical prefix → vote tally is just counts
- Print a text bar chart:
  ```
  cat     ███ 33%
  dog     ███ 33%
  hamster ███ 33%
  ```
- "A language model is a voting system. Attribution = counting."

### Beat 3: LLM ensemble — one model, N prompts (~40 lines)

- Switch to rooms dataset
- ONE model (GPT-2 locally, or any API). Run it N times, each with a different source in the prompt: `"[Source doc]. Question: Where is the hamster?"`
- The model doesn't see the other sources. From its perspective, N independent queries.
- Collect predictions. Count votes. Print colored inline HTML:

```python
from IPython.display import HTML
html = ""
for token, attr in zip(tokens, attributions):
    color = COLORS[max(attr, key=attr.get)]
    html += f'<span style="border-bottom:3px solid {color};padding:2px">{token}</span> '
display(HTML(html))
```

- Works with any model — local GPT-2, Claude API, GPT-4, whatever.
- **The lesson:** same idea as Beat 1, automated. Same idea as Beat 2, real model.

## The Artifact

**Notebook:** `ch01.ipynb` — ~60 lines of actual code. Inline colored HTML. Zero dependencies beyond numpy + a model.
**Script:** `ch01.py` — prints colored text to terminal.
**No viz server.** No Flask. No localhost. Just a notebook.

## Key Ideas

1. **Attribution = "ask separately, count the answers."** You did it by hand in Beat 1.
2. **Ensemble = one model, N prompts.** Not N model instances. One model, N contexts.
3. **Limitation: all votes are equal.** → Ch2
4. **This naturally motivates Ch4:** "we're running the model 10 times. What if we ran it ONCE with all sources in the prompt?"

## Assets Produced (for Ch2)

- `corpus.py` — the rooms dataset
- The ensemble voting function (one model, N prompts)
- The inline HTML rendering pattern
- Results format: `{"tokens": [...], "attribution": [{"Hamster Report": 1.0, ...}]}`
