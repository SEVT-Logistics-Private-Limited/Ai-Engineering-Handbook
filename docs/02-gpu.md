# 2. GPU (Graphics Processing Unit)

> The GPU is designed to perform many calculations in parallel, which makes it perfect for graphics, video and AI.

## Introduction

The CPU can't process high-resolution images and video quickly. **This is where the GPU comes in.**

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
- **bf16 (16-bit numbers)** instead of 32-bit, which halves the memory
- **Gradient checkpointing:** recompute some values instead of storing them, saving memory
- **Smaller batch sizes** for the biggest models

What we learned: on the A100-80GB, about **3 billion parameters** was the maximum model size we could train.

```text
Training script (Python) → GPU (Jetson / A100) → trained model file (.pt) → saved to Hugging Face
```

Code: [`tiny_llm_400m.py`](https://github.com/SEVT-Logistics-Private-Limited/tiny-llm-jetson/blob/main/tiny_llm_400m.py) (bf16 + gradient checkpointing), [`tiny_llm_3b.py`](https://github.com/SEVT-Logistics-Private-Limited/tiny-llm-jetson/blob/main/tiny_llm_3b.py)

---

**Previous:** [← CPU](01-cpu.md) · [Home](../README.md) · **Next:** [Binary →](03-binary.md)
