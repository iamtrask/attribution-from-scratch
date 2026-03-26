# AI Attribution from Scratch

A course on understanding which sources an LLM uses, from scratch, in code.

We start with vote counting on an n-gram model and build up to a GPU-accelerated, differentially-private attribution engine running on state-of-the-art open-source models. This course picks up where Karpathy's [Zero to Hero](https://karpathy.ai/zero-to-hero.html) leaves off — he teaches you how to build an LLM, we teach you how to trust one. In my opinion attribution is an excellent place to learn about differential privacy, even if your intention is to eventually go to other areas, because most of what you learn will be immediately transferable.

Prerequisites: solid programming (Python), intro-level math (e.g. derivatives, linear algebra), and familiarity with how neural networks work (e.g. from Karpathy's series or equivalent).

---

### Lecture 1: Ensemble Attribution: building a citation engine

We implement an LLM ensemble where each source document gets its own prompt, models vote on the answer, and attribution is just counting who voted. We start by doing it by hand ("you are the model"), then automate it with n-gram counts, then scale to real LLMs. By the end you see colored attribution on generated text, inline in the notebook.

- Jupyter notebook files
- [Lecture plan](lectures/01_ensemble_attribution/PLAN.md)

Ongoing...

---

License

[Apache 2.0](LICENSE)
