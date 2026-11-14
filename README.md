<div align="center">

# My AI Engineering Journey

**A structured guide to AI engineering, from computer fundamentals to LLMs, RAG and robotics, applied in a live production project.**

![Topics](https://img.shields.io/badge/topics-21-2563eb)
![Applied in project](https://img.shields.io/badge/applied%20in%20project-13%20of%2021-16a34a)
![Deployed on](https://img.shields.io/badge/deployed%20on-Azure-0078d4)

Yodha AI · SEVT Logistics Private Limited

[Topics](#topics) · [Featured Project](#featured-project) · [Learning Path](#learning-path) · [Roadmap](ROADMAP.md)

</div>

---

## Overview

Each topic is a short, consistent page: a clear explanation, a flow diagram, and how the concept is applied in our live **Telugu Voice AI Assistant**.

| At a glance | Detail |
|---|---|
| **Topics** | 21, grouped into 6 areas |
| **Applied in our project** | 13 of the 21 topics |
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
Machine learning foundations   ML → DL → Transformers
                                     ↓
LLMs                           Prompt Engineering → Hallucination → Tokenization
```

## Topics

### Hardware

| # | Topic | Summary |
|---|---|---|
| 1 | [CPU](docs/01-cpu.md) | Step-by-step processing, binary, and how far LLM training can go on a CPU |
| 2 | [GPU](docs/02-gpu.md) | Parallel processing, number formats, and how far we trained on a GPU |

### Images and video

Computers cannot see pictures, only numbers. This section shows how an image is stored as a grid of pixels, where each pixel holds red, green and blue values, and how resolution decides how much detail an image keeps. It then builds up to video: a sequence of images (frames) shown at a fixed speed (FPS). These basics explain how AI models are able to "see".

| # | Topic | Summary |
|---|---|---|
| 3 | [Image](docs/03-image.md) | Pixels and RGB values |
| 4 | [Image Resolution](docs/04-image-resolution.md) | Width × height in pixels |
| 5 | [Video](docs/05-video.md) | Images played continuously |
| 6 | [Frame](docs/06-frame.md) | One image inside a video |
| 7 | [FPS](docs/07-fps.md) | Frames shown per second |

### Language, vision and robotics

| # | Topic | Summary |
|---|---|---|
| 8 | [NLP](docs/08-nlp.md) | Branch of AI that understands human language |
| 9 | [VLM](docs/09-vlm.md) | Sees and understands (image + text) |
| 10 | [VLA](docs/10-vla.md) | Sees, understands and acts |
| 11 | [LLM](docs/11-llm.md) | Trained on huge text to understand and generate language |
| 12 | [ROS](docs/12-ros.md) | Connects and coordinates a robot's parts |

### Tech stack

| # | Topic | Summary |
|---|---|---|
| 13 | [RAG](docs/13-rag.md) | Retrieve documents, then let the LLM answer |
| 14 | [API](docs/14-api.md) | How two software systems talk: request → response |
| 15 | [FastAPI](docs/15-fastapi.md) | Building APIs in Python |

### Machine learning foundations

| # | Topic | Summary |
|---|---|---|
| 16 | [ML](docs/16-ml.md) | Systems that learn patterns from data |
| 17 | [DL](docs/17-dl.md) | Multi-layer neural networks; epochs, batches, training |
| 18 | [Transformers](docs/18-transformers.md) | The architecture behind LLMs: attention, Q/K/V, masking |

### LLMs

| # | Topic | Summary |
|---|---|---|
| 19 | [Prompt Engineering](docs/19-prompt-engineering.md) | Zero/one/few-shot, chain of thought, role prompting |
| 20 | [Hallucination](docs/20-hallucination.md) | When an LLM makes things up, and how to reduce it |
| 21 | [Tokenization](docs/21-tokenization.md) | Text → tokens → token IDs |

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
├── docs/         21 topic pages, numbered in reading order
├── projects/     Telugu Voice AI Assistant write-up and screenshots
├── assets/       Images used in the topic pages
└── ROADMAP.md    Covered and planned topics
```
