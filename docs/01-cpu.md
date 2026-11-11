# 1. CPU (Central Processing Unit)

> The CPU is the main processor of a computer. It executes instructions and performs general-purpose computations.

## Introduction

A computer doesn't understand photos, videos, languages or sounds. **It only understands numerical information.** Any image, sentence or audio we give it is first converted into numbers:

| We give the computer | It converts it into |
|---|---|
| Image | Numerical pixel values |
| Sentence | Text → tokens → numerical form |
| Audio | Numerical audio signals |

So who does the work on these numbers? The first piece of hardware is the **CPU**.

## What is it?

The **CPU (Central Processing Unit)** is responsible for **executing instructions** and performing **general-purpose computations**. It's often called the "brain" of the computer.

## Why is it needed?

Every program you run (the operating system, a browser, a calculator, a simple game) is a list of instructions. The CPU reads and executes those instructions one after another.

## How does it work?

- The CPU has a **few powerful cores** that work through tasks **step by step**.
- It's generally used for **small and everyday types of work**.
  - Example: it can support small games like Road Dash or card games.
- It **cannot process high-resolution workloads well**. It struggles to process sets of images or video at high resolution quickly.

## Flow diagram

```text
Instruction 1  →  Instruction 2  →  Instruction 3  →  Instruction 4
                (one after another, step by step)

Image / Sentence / Audio
          ↓
   Converted to numbers
          ↓
         CPU
          ↓
 Executes instructions → Result
```

## Real-world use cases

- Running the operating system and everyday apps
- Browsing, documents, spreadsheets
- Small games (Road Dash, card games)
- Controlling the GPU and other hardware

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

Code: [`voice-assistant/api.py`](https://github.com/SEVT-Logistics-Private-Limited/tiny-llm-jetson/blob/main/voice-assistant/api.py)

## Key takeaways

- A computer only understands numbers.
- The CPU executes instructions and does general-purpose computing.
- It's good for everyday work, but not for processing large amounts of high-resolution images or video.

---

[Home](../README.md) · **Next:** [GPU →](02-gpu.md)
