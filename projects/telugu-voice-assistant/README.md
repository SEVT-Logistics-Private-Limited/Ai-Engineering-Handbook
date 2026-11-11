# Project: Telugu Voice AI Assistant (Yodha)

> A voice assistant that listens in Telugu, answers vehicle questions using the vehicle manuals, and replies out loud in Telugu.

| | |
|---|---|
| **Live app** | [Open the assistant](https://telugu-voice-app.gentletree-f4002f64.southindia.azurecontainerapps.io/assistant) |
| **API docs** | [`/docs`](https://telugu-voice-app.gentletree-f4002f64.southindia.azurecontainerapps.io/docs) |
| **Source code** | [tiny-llm-jetson](https://github.com/SEVT-Logistics-Private-Limited/tiny-llm-jetson) |
| **Built with** | Python, FastAPI, Google Gemini, ChromaDB, Docker, Azure |

<p align="center">
  <img src="images/assistant-sign-in.png" alt="Sign-in screen of the live Yodha assistant" width="300">
</p>

---

## What it does

The user speaks a question in Telugu. The assistant understands it, finds the relevant section of the vehicle manual, asks an LLM to answer, and speaks the answer back in Telugu. It then listens for the next question.

## How it works

```text
User speaks (query raised)
        ↓
Speech to text (FastAPI: POST)
        ↓
Translate the query (Telugu text → English)
        ↓
Retrieve from ChromaDB (vehicle manuals)
        ↓
LLM generates the answer
        ↓
Text to speech (FastAPI: POST /tts)
        ↓
User hears the answer
```

| Step | What happens | Topic |
|---|---|---|
| Speech to text | Telugu speech becomes Telugu text | Not yet |
| Translate the query | Telugu → English, because the manuals are in English | [LLM](../../docs/12-llm.md) |
| Retrieve from ChromaDB | Find the manual section that matches the question | [RAG](../../docs/14-rag.md) |
| LLM generates the answer | Gemini answers using the manual section, as "Yodha" | [LLM](../../docs/12-llm.md), [Prompt Engineering](../../docs/20-prompt-engineering.md) |
| Text to speech | The Telugu answer becomes audio | Not yet |

## System overview

```text
                Browser (voice UI)
                       ↓  request
              FastAPI server on Azure
        ┌──────────────┼──────────────┐
        ↓              ↓              ↓
    ChromaDB      Google Gemini   Text to speech
(vehicle manuals)     (LLM)        (Telugu audio)
        └──────────────┼──────────────┘
                       ↓  response
                Browser plays the answer
```

## API endpoints

The assistant is a REST API built with [FastAPI](../../docs/16-fastapi.md).

| Method | Endpoint | What it does |
|---|---|---|
| GET | `/healthz` | Checks the server is running |
| GET | `/assistant` | Opens the voice assistant web page |
| POST | `/tts` | Text → Telugu speech |
| POST | `/converse` | Voice → answer as text and audio |
| POST | `/converse_text_stream` | Text → answer, sent back step by step |

![FastAPI docs page listing the assistant's endpoints](images/api-docs.png)

## Deployment

```text
Push code to GitHub
        ↓
GitHub Actions builds the Docker image
        ↓
Image stored in Azure Container Registry
        ↓
Azure Container Apps runs the live app
```

## In-house Telugu language model

We also built a small Telugu language model from scratch to understand how LLMs work internally:

| Setting | Value | Meaning |
|---|---|---|
| Transformer layers | 8 | One layer processes the input, then the next layer processes the updated result |
| Attention heads | 8 | 8 attention operations in parallel |
| Context length | 128 | Maximum number of tokens the model can process together in one input |
| Tokens (vocabulary) | 245 | One token per Telugu character |

See [Transformers](../../docs/19-transformers.md) and [Tokenization](../../docs/22-tokenization.md).

## Topics covered in this project

The project uses **14 of the 22 topics** in this handbook. Each topic page has an **"In our project"** section with the full details.

| # | Topic | Used? | How we used it |
|---|---|---|---|
| 1 | [CPU](../../docs/01-cpu.md) | Yes | The live server runs on CPU-only cloud machines (Azure), including the embedding model |
| 2 | [GPU](../../docs/02-gpu.md) | Yes | Trained our models on a Jetson Orin Nano and a Colab A100, using bf16 and gradient checkpointing |
| 3 | [Binary](../../docs/03-binary.md) | Yes | Audio sent as base64 in JSON; models saved in 16-bit (bf16) to halve file size |
| 4 | [Image](../../docs/04-image.md) | Not yet | Not used yet |
| 5 | [Image Resolution](../../docs/05-image-resolution.md) | Not yet | Not used yet |
| 6 | [Video](../../docs/06-video.md) | Not yet | Not used yet |
| 7 | [Frame](../../docs/07-frame.md) | Not yet | Not used yet |
| 8 | [FPS](../../docs/08-fps.md) | Not yet | Not used yet |
| 9 | [NLP](../../docs/09-nlp.md) | Yes | Telugu speech-to-text, keyword matching, translation, text cleanup, Telugu-script detection |
| 10 | [VLM](../../docs/10-vlm.md) | Not yet | Not used yet |
| 11 | [VLA](../../docs/11-vla.md) | Not yet | Not used yet |
| 12 | [LLM](../../docs/12-llm.md) | Yes | Gemini with a 3-model fallback chain; our own GPT models from 984 parameters to 3B |
| 13 | [ROS](../../docs/13-ros.md) | Not yet | Not used yet |
| 14 | [RAG](../../docs/14-rag.md) | Yes | Vehicle manuals in ChromaDB, e5 embeddings, top-1 chunk if distance ≤ 0.35 |
| 15 | [API](../../docs/15-api.md) | Yes | 8 REST endpoints of our own; we call the Gemini and gTTS APIs |
| 16 | [FastAPI](../../docs/16-fastapi.md) | Yes | The server: Pydantic validation, streaming (SSE), automatic `/docs` |
| 17 | [ML](../../docs/17-ml.md) | Yes | Rules for simple questions, learned models for everything else |
| 18 | [DL](../../docs/18-dl.md) | Yes | Trained the Telugu model: batch 16, 10,000 steps, loss 331 → 1.42 |
| 19 | [Transformers](../../docs/19-transformers.md) | Yes | Our Telugu Transformer (8 layers, 8 heads, 128 context), e5 encoder, Gemini decoder |
| 20 | [Prompt Engineering](../../docs/20-prompt-engineering.md) | Yes | "Yodha" role prompt with rules, time, manual text and the last 8 messages |
| 21 | [Hallucination](../../docs/21-hallucination.md) | Yes | "Don't imagine" rules, RAG, relevance threshold, Telugu output check |
| 22 | [Tokenization](../../docs/22-tokenization.md) | Yes | Character tokenizer (245 Telugu tokens); output-token limits on Gemini |

How the topics connect inside the assistant:

```text
User speaks (NLP: speech to text)
        ↓
Browser → our REST API (API, FastAPI, Binary: base64 audio)
        ↓
Simple question? → rules → instant answer (ML vs rules)
        ↓ no
RAG: embeddings + ChromaDB (RAG, Transformers: e5 encoder)
        ↓
Prompt: Yodha role + rules + manual text (Prompt Engineering, Hallucination)
        ↓
Gemini generates the answer (LLM, Tokenization: token limits)
        ↓
Clean text → speech → user hears it (NLP)

Behind the scenes: our own Telugu model trained on a GPU (GPU, DL, Transformers, Tokenization)
                   live server runs on Azure CPUs (CPU)
```

---

[Home](../../README.md)
