<div align="center">

# My-Ai-Engineering-Handbook

**A structured, step-by-step guide to AI, from computer fundamentals to LLMs, RAG and robotics, grounded in a live production project.**

Yodha AI · SEVT Logistics Private Limited

[Topics](#topics) · [Live Project](#featured-project-telugu-voice-ai-assistant) · [Learning Path](#learning-path) · [Roadmap](ROADMAP.md)

</div>

---

## Overview

This handbook explains the core concepts behind modern AI in a simple, consistent format. Each topic is one short page with a clear explanation and a flow diagram, and is linked to how the topic is applied in our live **Telugu Voice AI Assistant**.

| At a glance | Detail |
|---|---|
| **Topics covered** | 22, across 6 areas |
| **Applied in production** | 14 of the 22 topics are used in our live project |
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
Hardware        CPU → GPU → Binary
                          ↓
Images & video  Image → Image Resolution → Video → Frame → FPS
                          ↓
AI models       NLP → VLM → VLA → LLM → ROS
                          ↓
Applications    RAG → API → FastAPI
                          ↓
How AI learns   ML → DL → Transformers
                          ↓
Using LLMs      Prompt Engineering → Hallucination → Tokenization
```

## Topics

### Hardware

| # | Topic | Summary |
|---|---|---|
| 1 | [CPU](docs/01-cpu.md) | Executes instructions, step by step |
| 2 | [GPU](docs/02-gpu.md) | Many calculations in parallel, built for images, video and AI |
| 3 | [Binary](docs/03-binary.md) | 0s and 1s, bits and bytes |

### Images and video

| # | Topic | Summary |
|---|---|---|
| 4 | [Image](docs/04-image.md) | Pixels and RGB values |
| 5 | [Image Resolution](docs/05-image-resolution.md) | Width × height in pixels |
| 6 | [Video](docs/06-video.md) | Images played continuously |
| 7 | [Frame](docs/07-frame.md) | One image inside a video |
| 8 | [FPS](docs/08-fps.md) | Frames shown per second |

### AI models

| # | Topic | Summary |
|---|---|---|
| 9 | [NLP](docs/09-nlp.md) | AI that understands human language |
| 10 | [VLM](docs/10-vlm.md) | Sees and understands (image + text) |
| 11 | [VLA](docs/11-vla.md) | Sees, understands and acts |
| 12 | [LLM](docs/12-llm.md) | Trained on huge text to understand and generate language |
| 13 | [ROS](docs/13-ros.md) | Connects and coordinates a robot's parts |

### Applications

| # | Topic | Summary |
|---|---|---|
| 14 | [RAG](docs/14-rag.md) | Retrieve documents, then let the LLM answer |
| 15 | [API](docs/15-api.md) | How two software systems talk: request → response |
| 16 | [FastAPI](docs/16-fastapi.md) | Build APIs in Python |

### How AI learns

| # | Topic | Summary |
|---|---|---|
| 17 | [ML](docs/17-ml.md) | Systems that learn patterns from data |
| 18 | [DL](docs/18-dl.md) | Multi-layer neural networks; epochs, batches, training |
| 19 | [Transformers](docs/19-transformers.md) | The architecture behind LLMs: attention, Q/K/V, masking |

### Using LLMs

| # | Topic | Summary |
|---|---|---|
| 20 | [Prompt Engineering](docs/20-prompt-engineering.md) | Zero/one/few-shot, chain of thought, role prompting |
| 21 | [Hallucination](docs/21-hallucination.md) | When an LLM makes things up, and how to reduce it |
| 22 | [Tokenization](docs/22-tokenization.md) | Text → tokens → token IDs |

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
├── docs/                        # 22 topic pages, numbered in reading order
├── projects/
│   └── telugu-voice-assistant/  # Project write-up and screenshots
├── assets/images/               # Images used in the topic pages
├── ROADMAP.md                   # Covered and planned topics
└── README.md
```

## Roadmap

See [ROADMAP.md](ROADMAP.md) for the topics planned next.
