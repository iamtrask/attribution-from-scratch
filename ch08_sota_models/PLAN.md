# Chapter 8: SOTA Models — DeepSeek-R1 and Beyond

## The Idea

The capstone. DeepSeek-R1 0528 distill-7B on a laptop. KV-cache-aware attribution. Batched ablation. llama.cpp for maximum throughput. The full production pipeline: paste URLs, ask questions, get attributed answers with privacy guarantees on a SOTA reasoning model.

## What the Student Builds

1. **KV-cache-aware leave-one-out** — reuse cached K/V tensors, only recompute from divergence point
2. **Batched ablation** — N source-removal passes in one batched forward pass
3. **llama.cpp integration** — C for inference, Python for attribution
4. **DeepSeek-R1** — MoE architecture, reasoning traces, distilled 7B variant
5. **The full pipeline** — ensemble + single-model + training attribution + GPU + SOTA model + URLs

### The Artifact

The complete citation engine on DeepSeek-R1. Paste URLs. Ask questions. Get attributed, privacy-budgeted answers with citations. On your laptop.

## Key Ideas

1. **KV-cache reuse** makes leave-one-out practical at 7B scale
2. **MoE = natural ensemble.** Each expert can have its own training attribution.
3. **llama.cpp:** C for speed, Python for attribution
4. **Everything connects:** Ch1's voting → Ch3's RDP → Ch4's Lipschitz → Ch6's PATE → Ch7's GPU → this chapter

## Target Models

- DeepSeek-R1 0528 distill-7B (laptop, MLX or llama.cpp)
- DeepSeek-R1 0528 full 671B (server, CUDA — stretch goal)
- Qwen3 0.6B → 4B (already fast from Ch7)
