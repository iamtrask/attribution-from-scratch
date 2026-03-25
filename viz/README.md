# viz — Attribution Dashboard

The visualization module for Attribution from Scratch. This is **provided infrastructure**, not a teaching artifact. You import it, you call `show()`, you see your results beautifully. Like matplotlib for attribution.

## Usage

```python
from viz import show

# After running your attribution code:
results = ensemble_vote(sources, query)
show(results, sources)
# Opens http://localhost:5001 with the interactive dashboard
```

## What it renders

- **Source sidebar:** each source with its color, text preview, and spend meter
- **Context blocks:** the source documents in the prompt, color-coded
- **Generated tokens:** with colored attribution bars underneath each token
- **Hover tooltips:** per-source influence breakdown for any token
- **Budget controls:** per-source ε input (when results include budget data)
- **Exhaustion markers:** visual indicators when sources hit their budget

## Results format

The `show()` function renders whatever fields are present in the results dict. Each chapter adds fields as new concepts are introduced:

```python
# Ch1: just votes
{"tokens": ["bedroom"], "attribution": [{"Hamster Report": 1.0, "Cat Report": 0.0, ...}]}

# Ch2: weighted votes
{"tokens": [...], "attribution": [{"Hamster Report": 0.85, "Cat Report": 0.03, ...}]}

# Ch3: add budgets
{"tokens": [...], "attribution": [...],
 "budgets": {"Hamster Report": {"spent": 2.3, "limit": 5.0}, ...}}

# Ch4: add lipschitz bound
{"tokens": [...], "attribution": [...], "budgets": {...},
 "lip_bound": 2.2e83, "mode": "single-model"}

# Ch5: add per-individual accounting
{"tokens": [...], "attribution": [...], "budgets": {...},
 "lip_bound": 2.2e83, "per_source_norms": {...}}
```

The dashboard gracefully handles missing fields — Ch1 results render without budget meters, Ch4 results render without training attribution, etc.

## Design philosophy

- **Not taught, just used.** Students don't learn Flask/HTML/JS. They call `show()`.
- **Gorgeous from day one.** The same polished dashboard works for Ch1's simple votes and Ch8's DeepSeek-R1 attribution.
- **The code is here if you're curious.** But understanding it is not required for the course.
