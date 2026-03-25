# Chapter 1: Ensemble Attribution — Voting All the Way Up

## The Idea

Three beats in one chapter: (1) an n-gram model where attribution is trivially counting who voted, (2) replace the n-gram with real LLMs and the same vote-counting works, (3) ship a basic web app where you paste URLs and see colored attribution bars. The student has a working product by the end of Ch1.

## What the Student Builds

### Beat 1: N-gram votes (~30 lines)

- Bigram model trained on the animal-in-room corpus (10 source documents)
- Each source contributes counts to the bigram table
- Predict "bedroom" after "the hamster is in the" → trace the count to Hamster Report
- Bar chart: which source voted for each token. Perfect attribution.
- **The lesson:** a language model is a voting system. Attribution = counting who voted.

### Beat 2: LLM ensemble (~40 lines)

- Give each source its own model instance (or API call)
- Each model sees: its source document + the question
- Each produces a prediction. Majority vote wins.
- Attribution = which model(s) voted for the winning answer. Same bar chart.
- **The lesson:** same idea, real models. This is PATE (Papernot et al. 2017).

### Beat 3: The app + URLs (~200 lines)

- Flask + vanilla JS web app
- Sidebar: paste URLs, each gets a color
- Click Generate → ensemble votes → streaming tokens with colored attribution bars
- Hover any token to see which source's model voted for it
- Track-only mode (no privacy yet, just attribution)
- **The lesson:** attribution is useful RIGHT NOW, before any privacy math.

### The Artifact

`http://localhost:5001` — paste 3 Wikipedia URLs about animals. Ask "Which animal lives in the bedroom?" See the answer with colored bars showing which source drove each token. A working citation engine in chapter 1.

## Key Ideas

1. **A language model is a voting system.** N-grams make this literal. LLM ensembles make it practical.
2. **Ensemble = each source gets its own model.** No blending. Attribution = counting votes.
3. **You don't need to understand the model's internals.** Black-box voting works.
4. **Limitation: all votes are equal.** The model that saw the answer and the model that saw irrelevant text get the same weight. → Ch2

## Assets Produced (for Ch2)

- `corpus.py` — the 10 animal-in-room documents (reused in every chapter)
- `chat_app.py` + `chat_ui.html` — the web app (upgraded in every later chapter)
- URL fetching pipeline
- The ensemble voting function
- The bar-chart visualization pattern
