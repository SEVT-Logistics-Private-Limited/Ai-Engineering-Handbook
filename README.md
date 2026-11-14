<div align="center">

# My AI Engineering Journey

**A structured guide to AI engineering, from computer fundamentals to LLMs, RAG and robotics, applied in a live production project.**

![Topics](https://img.shields.io/badge/topics-25-2563eb)
![Applied in project](https://img.shields.io/badge/applied%20in%20project-13%20of%2025-16a34a)
![Deployed on](https://img.shields.io/badge/deployed%20on-Azure-0078d4)

Yodha AI · SEVT Logistics Private Limited

[Topics](#topics) · [Featured Project](#featured-project) · [Learning Path](#learning-path) · [Roadmap](ROADMAP.md)

</div>

---

## Overview

Each topic is a short, consistent page: a clear explanation, a flow diagram, and how the concept is applied in our live **Telugu Voice AI Assistant**.

| At a glance | Detail |
|---|---|
| **Topics** | 25, grouped into 6 areas |
| **Applied in our project** | 13 of the 25 topics |
| **Page format** | Introduction · Definition · Rationale · Mechanism · Flow diagram · Use cases · Application in our project |
| **Featured project** | [Telugu Voice AI Assistant](projects/telugu-voice-assistant/README.md), deployed on Azure Container Apps |
| **Author** | Rishi Sasanala |

## Learning path

Topics are designed to be read in order. Each builds on the previous one.

```text
Hardware                       CPU → GPU
                                     ↓
Images and video               Image → Image Resolution → Video → Frame → FPS
                                     ↓
Language, vision and robotics  NLP → VLM → VLA → LLM → ROS
                                     ↓
Tech stack                     RAG → API → FastAPI
                                     ↓
Machine learning foundations   ML → Supervised → Unsupervised → Semi-Supervised → Reinforcement → DL → Transformers
                                     ↓
LLMs                           Prompt Engineering → Hallucination → Tokenization
```

## Topics

### Hardware

| # | Topic | Summary | Topics inside |
|---|---|---|---|
| 1 | [CPU](docs/01-cpu.md) | Step-by-step processing, binary, and how far LLM training can go on a CPU | Step-by-step (sequential) processing · Binary: the language of the CPU · Training an LLM on a CPU: how far you can go |
| 2 | [GPU](docs/02-gpu.md) | Parallel processing, number formats, and how far we trained on a GPU | Parallel processing · Number formats (bits per number) · How far you can train on a GPU · GPU memory usage |

### Images and video

Computers cannot see pictures, only numbers. This section shows how an image is stored as a grid of pixels, where each pixel holds red, green and blue values, and how resolution decides how much detail an image keeps. It then builds up to video: a sequence of images (frames) shown at a fixed speed (FPS). These basics explain how AI models are able to "see".

| # | Topic | Summary | Topics inside |
|---|---|---|---|
| 3 | [Image](docs/03-image.md) | Pixels and RGB values | Pixels · RGB colour values · How a computer processes an image |
| 4 | [Image Resolution](docs/04-image-resolution.md) | Width × height in pixels | Width × height · Megapixels (MP) · Resolution vs memory and GPU needs |
| 5 | [Video](docs/05-video.md) | Images played continuously | Video as a sequence of images · How a video is stored in a computer |
| 6 | [Frame](docs/06-frame.md) | One image inside a video | Image vs frame · Frames as the building blocks of video |
| 7 | [FPS](docs/07-fps.md) | Frames shown per second | Frames per second · 30 / 60 / 120 FPS · How much data one second of video holds |

### Language, vision and robotics

| # | Topic | Summary | Topics inside |
|---|---|---|---|
| 8 | [NLP](docs/08-nlp.md) | Branch of AI that understands human language | What NLP is · Understanding a request: intent, action and required information |
| 9 | [VLM](docs/09-vlm.md) | Sees and understands (image + text) | Image + text understanding · How a VLM reads an image |
| 10 | [VLA](docs/10-vla.md) | Sees, understands and acts | Vision → language → action · VLM vs VLA |
| 11 | [LLM](docs/11-llm.md) | Trained on huge text to understand and generate language | GPT-style models · How an LLM reads text · How it generates an answer · Temperature |
| 12 | [ROS](docs/12-ros.md) | Connects and coordinates a robot's parts | What ROS does · How it fits with the other AI models |

### Tech stack

| # | Topic | Summary | Topics inside |
|---|---|---|---|
| 13 | [RAG](docs/13-rag.md) | Retrieve documents, then let the LLM answer | RAG vs fine-tuning · Document ingestion · Chunking · Embedding · Retrieval · Evaluating a RAG system |
| 14 | [API](docs/14-api.md) | How two software systems talk: request → response | Request → response · Types of APIs · REST and its methods · SOAP · REST vs SOAP |
| 15 | [FastAPI](docs/15-fastapi.md) | Building APIs in Python | Python functions as endpoints · Automatic `/docs` · Input validation · Request flow |

### Machine learning foundations

| # | Topic | Summary | Topics inside |
|---|---|---|---|
| 16 | [ML](docs/16-ml.md) | Systems that learn patterns from data | AI vs ML · Rules vs learning from data · Types of ML (supervised, unsupervised, semi-supervised, reinforcement) |
| 17 | [Supervised Learning](docs/17-supervised-learning.md) | Learns from inputs with known outputs: classification and regression | Inputs + known target outputs · House-price example · Classification · Regression |
| 18 | [Unsupervised Learning](docs/18-unsupervised-learning.md) | Finds patterns in data without known outputs | No known target outputs · Customer-data example · Clustering · Anomaly detection · Supervised vs unsupervised |
| 19 | [Semi-Supervised Learning](docs/19-semi-supervised-learning.md) | Learns from a little labelled data plus a lot of unlabelled data | Labelled vs unlabelled data · 1000-emails example · How labels spread to unlabelled data · Supervised vs semi-supervised vs unsupervised |
| 20 | [Reinforcement Learning](docs/20-reinforcement-learning.md) | An agent learns decisions from rewards and penalties | Agent · Environment · Action · Reward and penalty · Bicycle example · The learning loop |
| 21 | [DL](docs/21-dl.md) | Multi-layer neural networks; epochs, batches, training | Neural networks · Epoch · Batch · Batch size · The training loop |
| 22 | [Transformers](docs/22-transformers.md) | The architecture behind LLMs: attention, Q/K/V, masking | Architecture · Embeddings · Encoder vs decoder · Self-attention · Query, Key, Value (Q/K/V) · Multi-head attention · Masking |

### LLMs

| # | Topic | Summary | Topics inside |
|---|---|---|---|
| 23 | [Prompt Engineering](docs/23-prompt-engineering.md) | Zero/one/few-shot, chain of thought, role prompting | Zero-shot · One-shot · Few-shot · Chain of thought · Role prompting |
| 24 | [Hallucination](docs/24-hallucination.md) | When an LLM makes things up, and how to reduce it | What hallucination is · Why it happens · How to reduce it (RAG, prompts, validation, temperature, citations) |
| 25 | [Tokenization](docs/25-tokenization.md) | Text → tokens → token IDs | Token · Tokenization · Token IDs · Why tokens matter (limits and cost) |

## Featured project

**Telugu Voice AI Assistant.** A voice assistant that listens in Telugu, grounds its answers in vehicle manuals using Retrieval-Augmented Generation (RAG), and replies in spoken Telugu.

```text
User speaks (Telugu)
        ↓
Speech to text
        ↓
FastAPI server receives the question (REST API on Azure)
        ↓
Translate the query (Telugu → English)
        ↓
RAG: retrieve the matching section from ChromaDB (vehicle manuals)
        ↓
LLM (Gemini) generates the answer using the manual section
        ↓
Text to speech (FastAPI: POST /tts)
        ↓
User hears the answer
```

| Resource | Link |
|---|---|
| **Project overview** | [Telugu Voice AI Assistant](projects/telugu-voice-assistant/README.md) |
| **Topic-by-topic mapping** | [Topics covered in this project](projects/telugu-voice-assistant/README.md#topics-covered-in-this-project) |
| **Live application** | [Open the assistant](https://telugu-voice-app.gentletree-f4002f64.southindia.azurecontainerapps.io/assistant) |
| **Source code** | [tiny-llm-jetson](https://github.com/SEVT-Logistics-Private-Limited/tiny-llm-jetson) |

## Repository structure

```text
.
├── docs/         25 topic pages, numbered in reading order
├── projects/     Telugu Voice AI Assistant write-up and screenshots
├── assets/       Images used in the topic pages
└── ROADMAP.md    Covered and planned topics
```
