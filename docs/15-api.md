# 15. API (Application Programming Interface)

> An API is a medium that lets two software systems communicate. You send a request to the API and get a response.

## Introduction

When an app shows you the weather, it doesn't calculate the weather itself. It asks another system through an **API** and gets the answer back.

## What is it?

**API (Application Programming Interface)** is a **medium (contract) that lets two software systems communicate**.

> You **send a request → to the API → and get a response**.

### Types of APIs

1. **REST** (Representational State Transfer): uses HTTP
2. **SOAP** (Simple Object Access Protocol): uses XML
3. **GraphQL**
4. **WebSocket**
5. **Webhooks**

## Why is it needed?

- It lets apps, websites and services talk to each other.
- It lets you use an AI model (like Gemini) from your own app.

## How does it work?

### 1. REST API

A REST API is a medium for two software systems to communicate **over HTTP**.
- Simple and flexible
- Follows REST principles and usually communicates over HTTP

**REST methods:**

| Method | Does |
|---|---|
| GET | Get data |
| POST | Create data |
| PUT | Update data |
| DELETE | Delete data |

### 2. SOAP API

**SOAP (Simple Object Access Protocol)** is **structured and strict**.
- SOAP is a protocol used by applications to communicate with each other over a network.
- A SOAP API lets two applications communicate using **formatted XML messages**.
- Unlike GET/PUT/POST/DELETE, SOAP uses **"operations" (functions)**.

### REST vs SOAP

| REST | SOAP |
|---|---|
| Flexible | Strict |
| JSON | XML |
| HTTP methods (GET / POST / PATCH / DELETE) | Operations + WSDL |
| Web / mobile / microservices | Enterprise / legacy systems |

## Flow diagram

```text
Client (app) → sends a request → API → Server
Client (app) ← gets a response ← API ← Server
```

```text
                  API
        ┌──────────┴──────────┐
        ↓                     ↓
      REST                  SOAP
        ↓                     ↓
     Flexible               Strict
        ↓                     ↓
      JSON                   XML
        ↓                     ↓
  HTTP methods        Operations + WSDL
        ↓                     ↓
Web / Mobile /        Enterprise /
 Microservices       legacy systems
```

## Real-world use cases

- Weather, maps and payment apps
- Calling an LLM (Gemini, GPT) from your own code
- Mobile apps talking to their servers

## In our project

**Used, in both directions.** Our project **provides** an API and **uses** other APIs.

**Our API (REST):** the browser talks to our server through these endpoints:

| Method | Endpoint | What it does |
|---|---|---|
| GET | `/healthz` | Checks the server is running |
| GET | `/` | Shows the status: version, time, knowledge base loaded or not |
| GET | `/assistant` | Opens the voice assistant web page |
| POST | `/tts` | Text → Telugu speech |
| POST | `/converse` | Voice + chat history → transcript, answer and audio |
| POST | `/converse_stream` | Same, but sends the steps back one by one |
| POST | `/converse_text_stream` | Text → answer, sent back step by step (used by the web page) |
| POST | `/voice` | One question in voice → one answer in voice |

**APIs we call:**

| External API | Used for |
|---|---|
| **Google Gemini API** | LLM answers, translation, speech-to-text backup |
| **gTTS** (Google Text-to-Speech) | Telugu speech output |

```text
Browser → POST /converse_text_stream → Our API → Gemini API → Our API → Browser
Browser → POST /tts → Our API → gTTS → Our API → Browser (plays audio)
```

All our endpoints use **REST + JSON**. The streaming endpoints use **Server-Sent Events (SSE)** to send each step (transcript → answer → done) as soon as it's ready.

Code: [`voice-assistant/api.py`](https://github.com/SEVT-Logistics-Private-Limited/tiny-llm-jetson/blob/main/voice-assistant/api.py), [`voice-assistant/telugu_assistant.html`](https://github.com/SEVT-Logistics-Private-Limited/tiny-llm-jetson/blob/main/voice-assistant/telugu_assistant.html)

---

**Previous:** [← RAG](14-rag.md) · [Home](../README.md) · **Next:** [FastAPI →](16-fastapi.md)
