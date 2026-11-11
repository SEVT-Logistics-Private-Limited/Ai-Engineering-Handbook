# 21. Tokenization

> Tokenization is the process of converting text into tokens that the model can process.

## Introduction

LLMs never read words directly. They read **tokens**: small pieces of text converted into numbers. Tokenization is the first step whenever an LLM reads text.

## What is it?

**Token:** a unit of text processed by an LLM.
- Tokens can represent whole words, parts of words, punctuation or other text units, depending on the tokenizer.
- Punctuation and spaces can also affect tokenization.
- LLMs generally process **tokens, not raw words**.

**Tokenization:** the process of converting text into smaller units called tokens that the model can process.
- The tokens are then converted into **token IDs** (numbers).

## Why is it needed?

Computers only understand numbers, so text has to be turned into numbers first.

### Why do tokens matter?

Tokens affect:
- **Context window usage**
- **API costs**
- **Processing time**
- **Max prompt length**
- **Max output length**

## How does it work?

```text
Tokens  →  Token IDs
"AI"       → 2451
"is"       → 318
"amazing"  → 4567
```

These numbers are then used to look up the **embeddings** (see [Transformers](18-transformers.md)).

## Flow diagram

```text
Text input: "I love AI"
        ↓
Tokenization: ["I", "love", "AI"]
        ↓
Token IDs: [40, 2031, 1589]
        ↓
Embeddings
        ↓
Transformer
```

## Real-world use cases

- Calculating the cost of an LLM API call (you pay per token)
- Checking whether a document fits in the model's context window
- Splitting long documents into chunks for [RAG](13-rag.md)

## In our project

**Used, in two ways.**

**1. Our own tokenizer (built from scratch):** a **character-level tokenizer**, where each character is one token.

| Model | Vocabulary (number of tokens) |
|---|---|
| English toy models | 13 (the characters in "to be or not to be that is the question") |
| **Telugu model** | **245** (every unique Telugu character in the training text) |

```text
Telugu text → split into characters → each character gets an ID (0–244) → embeddings → Transformer
```

The token-to-ID table (`stoi`) is saved inside the model file, so the same tokenizer is always used when the model is loaded again.

**2. Token limits on Gemini:** we cap the length of Gemini's replies with `max_output_tokens`:

| Gemini call | Token limit |
|---|---|
| Assistant answers | 500 |
| Translation | 500 |
| Speech to text | 200 |

Fewer output tokens means **faster and cheaper** answers, which matters for a voice assistant.

Code: [`tiny_llm_telugu.py`](https://github.com/SEVT-Logistics-Private-Limited/tiny-llm-jetson/blob/main/tiny_llm_telugu.py), [`voice-assistant/api.py`](https://github.com/SEVT-Logistics-Private-Limited/tiny-llm-jetson/blob/main/voice-assistant/api.py)

---

**Previous:** [← Hallucination](20-hallucination.md) · [Home](../README.md)
