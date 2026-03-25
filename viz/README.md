# viz — Attribution Dashboard

The visualization module for Attribution from Scratch. This is **provided infrastructure**, not a teaching artifact. You import it, you call `show()`, you see your results beautifully. Like matplotlib for attribution.

**Introduced in Ch3** when budgets, spend meters, and exhaustion markers outgrow inline HTML. Ch1-2 use inline notebook rendering (zero dependencies).

## Usage

```python
from viz import show

results = ensemble_vote(sources, query)
show(results, sources)
# Opens http://localhost:5001 with the interactive dashboard
```

## Inline rendering (Ch1-2, always available)

For simple attribution (no budgets), inline HTML in the notebook works fine:

```python
from IPython.display import HTML
html = ""
for token, attr in zip(tokens, attributions):
    max_source = max(attr, key=attr.get)
    color = COLORS[max_source]
    html += f'<span style="border-bottom:3px solid {color};padding:2px">{token}</span> '
display(HTML(html))
```

This always works — even after the dashboard is introduced. Two interfaces, same results.

## Dashboard (Ch3+)

The full interactive dashboard with budget controls, spend meters, exhaustion markers, mode toggles, and hover tooltips. Renders whatever fields are present in the results dict:

```python
# Ch1-2: just attribution
{"tokens": [...], "attribution": [{"Hamster Report": 1.0, ...}]}

# Ch3: add budgets
{"tokens": [...], "attribution": [...],
 "budgets": {"Hamster Report": {"spent": 2.3, "limit": 5.0}, ...}}

# Ch4: add mode + lipschitz
{"tokens": [...], "attribution": [...], "budgets": {...},
 "lip_bound": 2.2e83, "mode": "single-model"}
```

## Design philosophy

- **Not taught, just used.** Students don't learn Flask/HTML/JS.
- **Inline first, dashboard when needed.** Ch1-2 have zero viz dependencies.
- **Both interfaces forever.** Inline rendering always available alongside the dashboard.
- **The code is here if you're curious.** Understanding it is not required.
