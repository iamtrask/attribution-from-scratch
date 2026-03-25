# Chapter 8: SOTA Models — DeepSeek-R1 and Beyond

**Status: Coming soon / Advanced**

The capstone. DeepSeek-R1 0528 distill-7B on a laptop. KV-cache-aware attribution. Batched ablation. llama.cpp integration.

Ch1-7 is the complete course. This chapter is for people who want to take it to production.

## What the Student Would Build

1. **KV-cache-aware leave-one-out** — reuse cached K/V, recompute from divergence
2. **Batched ablation** — N passes in one batched forward pass
3. **llama.cpp integration** — C for inference, Python for attribution
4. **DeepSeek-R1** — MoE, reasoning traces, distilled 7B
5. **URL ingestion** — fetch real documents, chunk, attribute at paragraph level

## Target Models

- DeepSeek-R1 0528 distill-7B (laptop)
- DeepSeek-R1 0528 full 671B (server, stretch goal)
- Qwen3 0.6B → 4B (already fast from Ch6)

## Key Ideas

1. **KV-cache reuse** makes leave-one-out practical at scale
2. **MoE = natural ensemble** for training attribution
3. **llama.cpp:** C for speed, Python for attribution
