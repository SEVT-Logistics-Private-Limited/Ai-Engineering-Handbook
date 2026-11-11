# 1. CPU (Central Processing Unit)

> The CPU is the main processor of a computer. It executes instructions and performs general-purpose computations, and like all computer hardware, it works in binary (0s and 1s).

## Introduction

A computer doesn't understand photos, videos, languages or sounds. **It only understands numerical information.** Any image, sentence or audio we give it is first converted into numbers:

| We give the computer | It converts it into |
|---|---|
| Image | Numerical pixel values |
| Sentence | Text → tokens → numerical form |
| Audio | Numerical audio signals |

Inside the hardware, those numbers are stored as **binary**: only 0s and 1s. So who does the work on these numbers? The first piece of hardware is the **CPU**.

## What is it?

The **CPU (Central Processing Unit)** is responsible for **executing instructions** and performing **general-purpose computations**. It's often called the "brain" of the computer.

## Why is it needed?

Every program you run (the operating system, a browser, a calculator, a simple game) is a list of instructions. The CPU reads and executes those instructions one after another.

## How does it work?

- The CPU has a **few powerful cores** that work through tasks **step by step**.
- It's generally used for **small and everyday types of work**.
  - Example: it can support small games like Road Dash or card games.
- It **cannot process high-resolution workloads well**. It struggles to process sets of images or video at high resolution quickly.

### Binary: the language of the CPU

**Binary** is a number system that uses only two digits: **0 and 1**. "Binary" means **two**. Electronic circuits can easily tell two states apart, so every number, letter, pixel and sound is stored as a pattern of 0s and 1s.

| Digit | Meaning |
|---|---|
| 0 | OFF / low voltage |
| 1 | ON / high voltage |

Counting in binary:

| Binary | Number |
|---|---|
| 0000 | 0 |
| 0001 | 1 |
| 0010 | 2 |
| 0011 | 3 |
| 0100 | 4 |

A single binary digit is called a **bit**:

| Example | Size |
|---|---|
| `1` | 1 bit |
| `1010` | 4 bits |
| `11001010` | 8 bits |

| Unit | Size |
|---|---|
| 1 Bit | a single 0 or 1 |
| 1 Byte | 8 bits |
| 1 KB | 1024 bytes |
| 1 MB | 1024 KB |
| 1 GB | 1024 MB |
| 1 TB | 1024 GB |

### Training an LLM on a CPU: how far can you go?

Two things limit LLM training on a CPU:

1. **Memory (RAM):** training needs about **16 bytes per parameter**: the model weights (4 bytes), their gradients (4 bytes) and the optimizer's two extra values (8 bytes). So a computer with 16 GB of RAM can hold the training state of a model with at most about **1 billion parameters**, before counting anything else.
2. **Speed:** the CPU works through the calculations step by step, so even models that fit in memory train slowly. In practice, a CPU is fine for small models (up to tens of millions of parameters). Beyond that, training takes hours or days, and that's where the [GPU](02-gpu.md) comes in.

## Flow diagram

```text
Instruction 1  →  Instruction 2  →  Instruction 3  →  Instruction 4
                (one after another, step by step)

Image / Sentence / Audio
          ↓
   Converted to numbers
          ↓
  Binary (0s and 1s)
          ↓
         CPU
          ↓
 Executes instructions → Result
```

```text
1 bit  →  8 bits = 1 Byte  →  1024 Bytes = 1 KB  →  1024 KB = 1 MB  →  1024 MB = 1 GB  →  1024 GB = 1 TB
```

## Real-world use cases

- Running the operating system and everyday apps
- Browsing, documents, spreadsheets
- Small games (Road Dash, card games)
- Controlling the GPU and other hardware
- Storing files: every photo, video and document is binary underneath

## In our project

**Used.** The live voice assistant runs on **CPU-based cloud servers**. No GPU is needed in production.

| Where | How the CPU is used |
|---|---|
| Azure server (first version: Azure VM *Standard D2s v3*, CPU only) | Ran the FastAPI server |
| Azure Container Apps (current) | Runs the FastAPI server inside a Docker container |
| Embedding model `multilingual-e5-small` | Runs on the server's CPU to turn questions into numbers for RAG |

**Why no GPU in production?** The heaviest work, generating answers with the LLM, happens on **Google Gemini's** servers. Our server only handles requests, small embeddings and text cleanup, which a CPU does well.

```text
User request → Azure server (CPU) → calls Gemini (Google's GPUs) → CPU cleans the answer → response
```

### Binary in our project

Audio is binary data (bytes), but our API sends JSON, which is text. So audio bytes are converted to **base64** text and back again. This happens when the browser can't do speech recognition itself and uploads the recording, and for every spoken answer sent back to the browser.

```text
Audio (binary bytes) → base64 text → sent in JSON → decoded back to bytes → played / transcribed
```

### How far can our models train on a CPU? (measured)

We trained our own GPT models on GPUs. To compare, we timed the **exact same model settings** on a **4-core cloud CPU** (Intel Xeon, 16 GB RAM):

| Our model | Parameters | Time per training step (CPU) | Full training run on CPU | Same run on the Jetson GPU (from our model cards) |
|---|---|---|---|---|
| Rung 1 | 984 | 0.002 s | about 10 seconds (5,000 steps) | under 1 minute |
| Rung 2 | 990K | 0.16 s | about **14 minutes** (5,000 steps) | under a few minutes |
| Telugu model | 25M | 1.13 s | about **3.1 hours** (10,000 steps) | trained on A100 (time not recorded) |
| Rung 3 | 151M | 2.47 s | about **3.4 hours** (5,000 steps) | several minutes |
| Rung 7 | 3B | **Cannot run.** Needs about 48 GB RAM just for training state, and this CPU has 16 GB. | Even with enough RAM, roughly **3 days** (estimated) | trained on A100-80GB |

**Answer: on a typical CPU you can practically train models up to about 100–150 million parameters**, and each run takes hours. Above about 1 billion parameters, an ordinary computer runs out of memory. That's why all our real training happened on GPUs.

Code: [`voice-assistant/api.py`](https://github.com/SEVT-Logistics-Private-Limited/tiny-llm-jetson/blob/main/voice-assistant/api.py) · Model settings: [`tiny_llm_1m.py`](https://github.com/SEVT-Logistics-Private-Limited/tiny-llm-jetson/blob/main/tiny_llm_1m.py), [`tiny_llm_telugu.py`](https://github.com/SEVT-Logistics-Private-Limited/tiny-llm-jetson/blob/main/tiny_llm_telugu.py), [`tiny_llm_150m.py`](https://github.com/SEVT-Logistics-Private-Limited/tiny-llm-jetson/blob/main/tiny_llm_150m.py)

---

[Home](../README.md) · **Next:** [GPU →](02-gpu.md)
