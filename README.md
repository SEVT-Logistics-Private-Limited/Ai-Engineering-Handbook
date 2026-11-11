<div align="center">

# My AI Engineering Journey

**A structured, step-by-step guide to AI, from computer fundamentals to LLMs, RAG and robotics, grounded in a live production project.**

Yodha AI · SEVT Logistics Private Limited

[Topics](#topics) · [Live Project](#featured-project-telugu-voice-ai-assistant) · [Learning Path](#learning-path) · [Roadmap](ROADMAP.md)

</div>

---

## Overview

This repository explains the core concepts behind modern AI in a simple, consistent format. Each topic is one short page with a clear explanation and a flow diagram, and is linked to how the topic is applied in our live **Telugu Voice AI Assistant**.

| At a glance | Detail |
|---|---|
| **Topics covered** | 21, across 6 areas |
| **Applied in production** | 13 of the 21 topics are used in our live project |
| **Live project** | [Telugu Voice AI Assistant](projects/telugu-voice-assistant/README.md), deployed on Azure |
| **Author** | Rishi Sasanala |

## How each topic is structured

Every topic page follows the same seven-part layout, so any page can be read on its own:

| # | Section | Purpose |
|---|---|---|
| 1 | Introduction | Context for the topic |
| 2 | What is it? | Definition |
| 3 | Why is it needed? | The problem it solves |
| 4 | How does it work? | Explanation with examples |
| 5 | Flow diagram | Visual summary |
| 6 | Real-world use cases | Where it is used in industry |
| 7 | In our project | How we applied it in the Telugu Voice AI Assistant |

## Learning path

Topics are designed to be read in order. Each one builds on the previous one.

```text
Hardware                       CPU → GPU   (including binary)
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
| 1 | [CPU](docs/01-cpu.md) | Executes instructions step by step; binary (0s and 1s, bits and bytes); how far LLM training can go on a CPU |
| 2 | [GPU](docs/02-gpu.md) | Many calculations in parallel; 32-bit vs 16-bit numbers; how far we trained and how much of the GPU we used |

### Images and video

Computers can't see pictures, only numbers. This section shows how an image is stored as a grid of pixels, where each pixel holds red, green and blue values, and how resolution decides how much detail an image keeps. It then builds up to video: a sequence of images (frames) shown at a fixed speed (FPS). These basics explain how AI models are able to "see".

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
| 8 | [NLP](docs/08-nlp.md) | AI that understands human language |
| 9 | [VLM](docs/09-vlm.md) | Sees and understands (image + text) |
| 10 | [VLA](docs/10-vla.md) | Sees, understands and acts |
| 11 | [LLM](docs/11-llm.md) | Trained on huge text to understand and generate language |
| 12 | [ROS](docs/12-ros.md) | Connects and coordinates a robot's parts |

### Tech stack

| # | Topic | Summary |
|---|---|---|
| 13 | [RAG](docs/13-rag.md) | Retrieve documents, then let the LLM answer |
| 14 | [API](docs/14-api.md) | How two software systems talk: request → response |
| 15 | [FastAPI](docs/15-fastapi.md) | Build APIs in Python |

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

## Featured project: Telugu Voice AI Assistant

A voice assistant that listens in Telugu, answers vehicle questions from the vehicle manuals using RAG, and replies in Telugu speech.

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

| | |
|---|---|
| **Project details** | [Telugu Voice AI Assistant](projects/telugu-voice-assistant/README.md) |
| **Topic-by-topic mapping** | [Topics covered in this project](projects/telugu-voice-assistant/README.md#topics-covered-in-this-project) |
| **Live application** | [Open the assistant](https://telugu-voice-app.gentletree-f4002f64.southindia.azurecontainerapps.io/assistant) |
| **Source code** | [tiny-llm-jetson](https://github.com/SEVT-Logistics-Private-Limited/tiny-llm-jetson) |

## Repository structure

```text
.
├── docs/                        # 21 topic pages, numbered in reading order
├── projects/
│   └── telugu-voice-assistant/  # Project write-up and screenshots
├── assets/images/               # Images used in the topic pages
├── ROADMAP.md                   # Covered and planned topics
└── README.md
```

## Roadmap

See [ROADMAP.md](ROADMAP.md) for the topics planned next.
