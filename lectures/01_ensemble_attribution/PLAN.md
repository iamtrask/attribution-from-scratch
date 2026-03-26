# Lecture 1: What Is Attribution, Why Is It Hard?

## The Arc

Four beats that take the student from "attribution is trivial" to "oh no, this is actually hard" to "wait, there's a way out":

1. **N-gram counts** — attribution is just looking up who voted. Trivial.
2. **Perceptron** — attribution is input × weight. Still easy. Decomposable.
3. **Logistic regression** — add a sigmoid and attribution breaks. The nonlinearity mixes sources. You can't decompose the output anymore. THIS is why attribution is hard.
4. **LLM ensemble** — the escape hatch. Don't let sources mix inside the model. Give each source its own prompt. Vote. Attribution is back to counting. Easy again.

The lecture ends with the student holding two things in their head: (a) a hard problem they want to solve (attribution through nonlinearities), and (b) a working solution that sidesteps it (the ensemble). The rest of the course explores both paths.

## Datasets

### The Hogwarts Survey Dataset (Beats 1-3)

1000 survey responses from Hogwarts students about their favorite subject. Four houses (Gryffindor, Slytherin, Hufflepuff, Ravenclaw), each with distinct preferences and realistic noise.

```
"As a member of Gryffindor, my favorite subject is Defense Against the Dark Arts"
"As a member of Slytherin, my favorite subject is Potions"
"As a member of Hufflepuff, my favorite subject is Herbology"
"As a member of Ravenclaw, my favorite subject is Charms"
```

The house is a natural source/group ID baked into the text. When the model predicts "Potions", you trace it to Slytherin. The question "which group drove this prediction?" is attribution. 250 responses per house, 7 subjects, strong preferences with noise (some Gryffindors like Potions, some Slytherins like Herbology). See `corpus.py`.

### The Rooms Dataset (Beat 2 onward — the Shakespeare)

```
Source 1: "The cat is in the kitchen. The kitchen is on the first floor."
Source 2: "The dog is in the garden. The garden has a pond."
Source 3: "The hamster is in the bedroom. The bedroom is upstairs."
Source 4: "The bird is in the cage. The cage is by the window."
Source 5: "The fish is in the pond. The pond is in the garden."
...10 sources
```

Verifiable ground truth. Multi-hop facts for Lecture 2. Carries the entire course.

## What the Student Builds

### Beat 1: N-gram votes (~20 lines)

- Bigram model trained on the Hogwarts survey (1000 responses)
- Prompt: "my favorite subject is"
- The bigram table has counts per next word, traceable to each house:
  ```
  Potions     ██████████████ 172  (Slytherin: 122, Ravenclaw: 26, ...)
  Herbology   ██████████ 147      (Hufflepuff: 107, Slytherin: 15, ...)
  Defense     █████████ 219       (Gryffindor: 126, Slytherin: 47, ...)
  Charms      ████████ 158        (Ravenclaw: 77, Hufflepuff: 40, ...)
  ```
- Attribution = reading off which house contributed which counts. Exact. Free.
- **Lesson:** "A language model is a voting system. Attribution = counting who voted."
- **This is trivially easy.** Savor it.

### Beat 2: Perceptron (~30 lines)

- Same dataset. Bag-of-words features per house. Predict: which subject?
- Single-layer perceptron (no activation function). Train it.
- Output = Σ(house_i_input × weight). Perfectly decomposable.
- Print per-house contributions. They sum to the output exactly.
- "Slytherin contributed 0.6 toward Potions, Ravenclaw contributed 0.2, Gryffindor contributed 0.1..."
- **Lesson:** "Linear models are perfectly attributable. Each source's contribution = its input × the weight."
- **Still easy.** The output is a sum of parts. You can point to each part.

### Beat 3: Logistic regression — attribution breaks (~30 lines)

- Same model, same data. Add a sigmoid: output = σ(Σ(house_i_input × weight))
- Try to decompose: the per-house contributions no longer sum to the output. The sigmoid mixes them nonlinearly.
- Show it concretely: Slytherin contributes 2.0, Ravenclaw contributes 1.0, but σ(3.0) ≠ σ(2.0) + σ(1.0). The nonlinearity creates interaction terms. You can't say "Slytherin was responsible for X% of the output."
- **Lesson:** "One nonlinearity. That's all it takes. The sources get mixed, and you can't un-mix them."
- **This is the crisis.** Every real model — MLPs, transformers, GPT-4 — is nonlinearities stacked on nonlinearities. If you can't attribute through a single sigmoid, how do you attribute through a hundred layers of them?

### Beat 4: LLM ensemble — the escape (~40 lines)

- "What if sources never mix inside the model?"
- Switch to the rooms dataset. One model, N prompts. Each prompt has one source + the question.
- The model processes each source INDEPENDENTLY. No mixing. No nonlinear interaction between sources.
- Collect predictions. Count votes. Print colored inline HTML:

```python
from IPython.display import HTML
html = ""
for token, attr in zip(tokens, attributions):
    color = COLORS[max(attr, key=attr.get)]
    html += f'<span style="border-bottom:3px solid {color};padding:2px">{token}</span> '
display(HTML(html))
```

- Works with any model — local GPT-2, API calls, anything.
- **Lesson:** "Attribution is hard because sources mix. The ensemble prevents mixing. Attribution is easy again."
- **But:** you're running the model N times. And the model can't cross-reference sources. There's a cost.

## The Artifact

**Notebook:** `lecture_01.ipynb` — ~120 lines of code across 4 beats. Inline colored HTML. Zero dependencies beyond numpy + a model.
**Script:** `lecture_01.py` — prints colored text to terminal.

## Key Ideas

1. **Attribution is easy when sources don't mix.** N-grams (counting), perceptrons (linear decomposition), ensembles (separate prompts).
2. **Attribution is hard when sources DO mix.** One sigmoid is enough to break it. Deep networks are hundreds of nonlinearities deep.
3. **The ensemble sidesteps the problem** by preventing sources from mixing. It works, but costs N forward passes and can't cross-reference sources.
4. **Two open problems for the rest of the course:**
   - **Ensemble path (Lectures 2-3):** Can we make the ensemble smarter (weighted votes) and private (noisy votes)?
   - **Single-model path (Lectures 4-5):** Can we do attribution THROUGH the nonlinearities? (Lipschitz bounds, differential privacy)

## Assets Produced (for Lecture 2)

- `corpus.py` — the rooms dataset (10 sources with multi-hop facts)
- The ensemble voting function (one model, N prompts)
- The inline HTML rendering pattern
- The trained perceptron + logistic regression (reused in Lecture 4 as the simple case for Lipschitz bounds)
- The student's understanding: attribution is easy without mixing, hard with mixing

## Pacing

- Beat 1: 5 minutes. "This is easy."
- Beat 2: 5 minutes. "Still easy."
- Beat 3: 10 minutes. "Oh no." (The σ(a+b) ≠ σ(a)+σ(b) demo is the key moment.)
- Beat 4: 10 minutes. "Oh wait, there's a trick." (Relief, but partial — the cost and limitations are real.)
- Total: ~30 minutes of code. The rest is markdown explanation between cells.
