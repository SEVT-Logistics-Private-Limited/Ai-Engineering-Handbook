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

You speak a question in Telugu. The assistant understands it, finds the right part of the vehicle manual, asks an LLM to answer, and speaks the answer back to you in Telugu. Then it listens for your next question.

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
| Speech to text | Telugu speech becomes Telugu text | – |
| Translate the query | Telugu → English, because the manuals are in English | [LLM](../../docs/12-llm.md) |
| Retrieve from ChromaDB | Find the manual section that matches the question | [RAG](../../docs/14-rag.md) |
| LLM generates the answer | Gemini answers using the manual section, as "Yodha" | [LLM](../../docs/12-llm.md), [Prompt Engineering](../../docs/20-prompt-engineering.md) |
| Text to speech | The Telugu answer becomes audio | – |

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

## My own Telugu language model

I also built my own small Telugu language model from scratch to understand how LLMs work inside:

| Setting | Value | Meaning |
|---|---|---|
| Transformer layers | 8 | One layer processes the input, then the next layer processes the updated result |
| Attention heads | 8 | 8 attention operations in parallel |
| Context length | 128 | Maximum number of tokens the model can process together in one input |
| Tokens (vocabulary) | 245 | One token per Telugu character |

See [Transformers](../../docs/19-transformers.md) and [Tokenization](../../docs/22-tokenization.md).

## Topics used in this project

[GPU](../../docs/02-gpu.md) · [LLM](../../docs/12-llm.md) · [RAG](../../docs/14-rag.md) · [API](../../docs/15-api.md) · [FastAPI](../../docs/16-fastapi.md) · [DL](../../docs/18-dl.md) · [Transformers](../../docs/19-transformers.md) · [Prompt Engineering](../../docs/20-prompt-engineering.md) · [Hallucination](../../docs/21-hallucination.md) · [Tokenization](../../docs/22-tokenization.md)

---

[Home](../../README.md)
