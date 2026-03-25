# Chapter 6: Going Fast — GPU Acceleration

## The Idea

Palate cleanser. Everything is slow. MLX gives 40-50×. Upgrade to Qwen3 0.6B. Fun, visual, satisfying. The benchmark table is the dopamine hit.

## What the Student Builds

1. **MLX port of GPT-2** (~100 lines)
2. **Fused Lipschitz** — zero-overhead scalar side-channel (~200 lines)
3. **MLX Qwen3 0.6B** (~150 lines)
4. **Benchmark** — the table (~80 lines)
5. **Accelerated ensemble** — batched inference
6. **See it** — same dashboard, dramatically faster

## The Artifact

**Notebook:** `ch06.ipynb` — ports + benchmark.
**Script:** `ch06.py --benchmark`
**Viz:** the dashboard at ~15ms/token. Interactive speed.

## Key Ideas

1. **Unified memory, lazy evaluation, fused Lipschitz.**
2. **Benchmark: 600ms → 15ms.**

## Assets Inherited (from Ch5)

- Complete private attribution system (both modes)

## Assets Produced (for Ch7)

- `gpt2_mlx.py`, `qwen_mlx.py`, `lipschitz_mlx.py`
- Emotional recharge for Ch7
