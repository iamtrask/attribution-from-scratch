# Chapter 7: Going Fast — GPU Acceleration

## The Idea

Everything works but everything is slow. MLX on Apple Silicon gives 40-50× speedup for single-model mode. Batched inference accelerates the ensemble. Upgrade from GPT-2 to Qwen3 0.6B.

## What the Student Builds

1. **MLX port of GPT-2** — `gpt2_mlx.py`, nearly 1:1 with numpy version (~100 lines)
2. **Fused Lipschitz tracking** — scalar side-channel, zero overhead. The key optimization. (~200 lines)
3. **MLX Qwen3 0.6B** — modern architecture: RoPE, RMSNorm, SwiGLU, GQA (~150 lines)
4. **Benchmark** — numpy vs MLX comparison table (~80 lines)
5. **Accelerated ensemble** — batched inference for N models in one GPU pass
6. **App upgrade** — both modes running at interactive speed on Qwen

### The Artifact

Benchmark: `NumPy 600ms/token → MLX 15ms/token`. The app running Qwen 0.6B on a laptop GPU.

## Key Ideas

1. **Unified memory:** no CPU↔GPU copies on Apple Silicon
2. **Lazy evaluation:** build graph, execute at once
3. **Fused Lipschitz:** naive wrappers kill GPU perf (`.item()` syncs). Scalar side-channel fixes it.
4. **Batched inference:** N ensemble members in one forward pass

## Assets Inherited (from Ch6)

- The complete app with both modes, full DP pipeline

## Assets Produced (for Ch8)

- `gpt2_mlx.py`, `qwen_mlx.py`, `lipschitz_mlx.py`
- The app at interactive speed
- "Qwen 0.6B is fast but small. Can we run DeepSeek-R1?" → Ch8
