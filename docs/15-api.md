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

**In my project:** the Telugu voice assistant is a REST API built with [FastAPI](16-fastapi.md).

## Key takeaways

- An API lets two systems communicate: request → response.
- REST = flexible, JSON, HTTP methods. SOAP = strict, XML, operations.
- Other types: GraphQL, WebSocket, Webhooks.

---

**Previous:** [← RAG](14-rag.md) · [Home](../README.md) · **Next:** [FastAPI →](16-fastapi.md)
