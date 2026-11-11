# 2. GPU (Graphics Processing Unit)

> The GPU is designed to perform many calculations in parallel, which makes it perfect for graphics, video and AI.

## Introduction

The CPU can't process high-resolution images and video quickly, and it's too slow to train large AI models. **This is where the GPU comes in.**

## What is it?

The **GPU (Graphics Processing Unit)** was designed to **perform many calculations in parallel** to handle huge tasks.

## Why is it needed?

- It can process **sets of images and video at high resolution**.
- It can read images at a much **higher rate**.
- So we can play heavy games like **Call of Duty and PUBG** smoothly.
- AI models are huge collections of numbers, and training them needs millions of calculations at the same time. That's exactly what a GPU does best.

## How does it work?

A GPU has **thousands of small cores**. Instead of doing one calculation after another like a CPU, it splits the work into many small pieces and does them **at the same time**.

| | CPU | GPU |
|---|---|---|
| Cores | A few powerful cores | Thousands of small cores |
| Works | Step by step | Many tasks in parallel |
| Best for | General computing | Images, video, games, **AI** |

### Binary on the GPU: how many bits per number?

Every number in an AI model is stored in binary, and **how many bits each number uses decides how much GPU memory the model needs**:

| Format | Bits per number | Bytes per number | Memory for a 3-billion-parameter model |
|---|---|---|---|
| fp32 (standard) | 32 bits | 4 bytes | ~12 GB |
| **bf16** (half size) | 16 bits | 2 bytes | **~6 GB** |
| Ternary (-1, 0, +1) | ~2 bits | 1/4 byte | ~1 GB (compressed) |

Fewer bits per number means a bigger model fits on the same GPU.

### How far can you train on a GPU?

The limit is **GPU memory (VRAM)**. Training needs about **16 bytes per parameter** (weights, gradients and optimizer values), plus extra memory for the intermediate values of each batch:

| GPU | Memory | Rough maximum model size for training |
|---|---|---|
| NVIDIA Jetson Orin Nano | 8 GB (shared with the CPU) | ~100–150 million parameters |
| NVIDIA A100 | 80 GB | ~3 billion parameters (with memory-saving techniques) |

## Flow diagram

```text
CPU (step by step):
Task 1 → Task 2 → Task 3 → Task 4

GPU (in parallel):
Task 1
Task 2      → all at the same time → Result
Task 3
Task 4
```

```text
Model size (parameters) × 16 bytes  →  training memory needed  →  fits in GPU memory?  →  yes: train / no: use bf16, smaller batch, bigger GPU
```

## Real-world use cases

- Gaming (Call of Duty, PUBG)
- Video editing and high-resolution video playback
- Training and running AI models (LLMs, image models)

## In our project

**Used, for training our own language models.** Training means billions of calculations, so it needs a GPU.

| GPU | What we trained on it |
|---|---|
| **NVIDIA Jetson Orin Nano** (small edge device) | The first models: 984 parameters → 990K → 151M |
| **Google Colab A100 (80 GB)** | Bigger models: 399M → 1B → 2B → 3B parameters, and the 25M Telugu model |

GPU techniques we used to fit large models into GPU memory:
- **bf16 (16-bit numbers)** instead of 32-bit, which halves the memory (binary in action)
- **Gradient checkpointing:** recompute some values instead of storing them, saving memory
- **Smaller batch sizes** for the biggest models

Saving models in **bf16** also halved the file size: the 3B model's checkpoint is about **6 GB** instead of 12 GB.

```text
Training script (Python) → GPU (Jetson / A100) → trained model file (.pt) → saved to Hugging Face
```

### How far did we train on each GPU?

Training memory per model (calculated from each model's size at 16 bytes per parameter; it doesn't include the extra per-batch memory):

| Our model | Parameters | Training memory | GPU | Share of GPU memory |
|---|---|---|---|---|
| Rung 1 | 984 | ~16 KB | Jetson (8 GB) | ~0% |
| Rung 2 | 990K | ~16 MB | Jetson (8 GB) | ~0.2% |
| Rung 3 | 151M | ~2.4 GB | Jetson (8 GB) | ~30% + batch memory + OS → **at the limit** (first run crashed from memory pressure) |
| Telugu model | 25M | ~0.4 GB | A100 (80 GB) | **~0.5%** |
| Rung 4 | 399M | ~6.4 GB | A100 (80 GB) | ~8% |
| Rung 5 | 1B | ~16 GB | A100 (80 GB) | ~20% |
| Rung 6 | 2B | ~32 GB | A100 (80 GB) | ~40% |
| Rung 7 | 3B | ~48 GB | A100 (80 GB) | ~60% + batch memory |
| Rung 8 | 3.07B | ~49 GB | A100 (80 GB) | ~61% + batch memory → **full**: the largest model that fit |

### Are we using 100% of the GPU, or half of it?

**It depends on the model:**

- **Biggest models (3B on the A100, 151M on the Jetson): about 100% of GPU memory.** These were the largest models each GPU could hold. One step bigger and training would not fit.
- **Telugu model (25M) on the A100: less than 1% of GPU memory.** The A100 is far bigger than this model needs. A much smaller and cheaper GPU, or even the Jetson, could train it.
- **Mid-size models (399M–2B): about 10–40% of memory** for the training state. There was room to use larger batches.

Note: "using the GPU" has two meanings. **Memory** (how much VRAM is filled) is what we calculated above. **Compute** (how busy the GPU cores are, in %) wasn't logged during training. It can be checked live with `nvidia-smi` on the A100 or `tegrastats` on the Jetson.

Code: [`tiny_llm_400m.py`](https://github.com/SEVT-Logistics-Private-Limited/tiny-llm-jetson/blob/main/tiny_llm_400m.py) (bf16 + gradient checkpointing), [`tiny_llm_3b.py`](https://github.com/SEVT-Logistics-Private-Limited/tiny-llm-jetson/blob/main/tiny_llm_3b.py) (bf16 save), [`tiny_llm_5b.py`](https://github.com/SEVT-Logistics-Private-Limited/tiny-llm-jetson/blob/main/tiny_llm_5b.py) (3.07B, hardware maximum)

---

**Previous:** [← CPU](01-cpu.md) · [Home](../README.md) · **Next:** [Image →](03-image.md)
