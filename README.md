# AI Engineering Handbook

A simple, step-by-step guide to AI, from how a computer works to LLMs, RAG and robots. Each topic is one short page with a clear explanation and a flow diagram, and is linked to the real project where I used it.

**Author:** Rishi Sasanala · Yodha AI (SEVT Logistics Private Limited)

---

## How to use this handbook

Read the topics **in order**. Each page has the same simple layout:

1. Introduction
2. What is it?
3. Why is it needed?
4. How does it work?
5. Flow diagram
6. Real-world use cases
7. In our project
8. Key takeaways

The **"In our project"** section shows exactly how the topic is used in the Telugu Voice Assistant, or says "Not used yet". Every page ends with a **Next →** link to the following topic.

## Learning path

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

✅ = used in our project (each page has an **"In our project"** section explaining how)

| # | Topic | In one line | In our project |
|---|---|---|---|
| 1 | [CPU](docs/01-cpu.md) | Executes instructions, step by step | ✅ |
| 2 | [GPU](docs/02-gpu.md) | Many calculations in parallel, built for images, video and AI | ✅ |
| 3 | [Binary](docs/03-binary.md) | 0s and 1s, bits and bytes | ✅ |
| 4 | [Image](docs/04-image.md) | Pixels and RGB values | – |
| 5 | [Image Resolution](docs/05-image-resolution.md) | Width × height in pixels | – |
| 6 | [Video](docs/06-video.md) | Images played continuously | – |
| 7 | [Frame](docs/07-frame.md) | One image inside a video | – |
| 8 | [FPS](docs/08-fps.md) | Frames shown per second | – |
| 9 | [NLP](docs/09-nlp.md) | AI that understands human language | ✅ |
| 10 | [VLM](docs/10-vlm.md) | Sees and understands (image + text) | – |
| 11 | [VLA](docs/11-vla.md) | Sees, understands and acts | – |
| 12 | [LLM](docs/12-llm.md) | Trained on huge text to understand and generate language | ✅ |
| 13 | [ROS](docs/13-ros.md) | Connects and coordinates a robot's parts | – |
| 14 | [RAG](docs/14-rag.md) | Retrieve documents, then let the LLM answer | ✅ |
| 15 | [API](docs/15-api.md) | How two software systems talk: request → response | ✅ |
| 16 | [FastAPI](docs/16-fastapi.md) | Build APIs in Python | ✅ |
| 17 | [ML](docs/17-ml.md) | Systems that learn patterns from data | ✅ |
| 18 | [DL](docs/18-dl.md) | Multi-layer neural networks; epochs, batches, training | ✅ |
| 19 | [Transformers](docs/19-transformers.md) | The architecture behind LLMs: attention, Q/K/V, masking | ✅ |
| 20 | [Prompt Engineering](docs/20-prompt-engineering.md) | Zero/one/few-shot, chain of thought, role prompting | ✅ |
| 21 | [Hallucination](docs/21-hallucination.md) | When an LLM makes things up, and how to reduce it | ✅ |
| 22 | [Tokenization](docs/22-tokenization.md) | Text → tokens → token IDs | ✅ |

See the full mapping in [Topics covered in this project](projects/telugu-voice-assistant/README.md#topics-covered-in-this-project).

## Project: Telugu Voice AI Assistant

A voice assistant that listens in Telugu, answers vehicle questions from the vehicle manuals using RAG, and replies in Telugu speech.

```text
User speaks (Telugu)
        ↓
Speech to text
        ↓
Translate the query (Telugu → English)
        ↓
Retrieve from ChromaDB (vehicle manuals)
        ↓
LLM generates the answer
        ↓
Text to speech
        ↓
User hears the answer
```

- **Read more:** [projects/telugu-voice-assistant](projects/telugu-voice-assistant/README.md)
- **Live app:** [Open the assistant](https://telugu-voice-app.gentletree-f4002f64.southindia.azurecontainerapps.io/assistant)
- **Source code:** [tiny-llm-jetson](https://github.com/SEVT-Logistics-Private-Limited/tiny-llm-jetson)

## Repository structure

```text
.
├── docs/                        # 22 topic pages, numbered in reading order
├── projects/
│   └── telugu-voice-assistant/  # Project write-up and screenshots
├── assets/images/               # Images used in the topic pages
├── ROADMAP.md                   # What's covered and what's next
└── README.md
```

## What's next

See [ROADMAP.md](ROADMAP.md) for the topics planned next.
