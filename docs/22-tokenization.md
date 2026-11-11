# 22. Tokenization

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

These numbers are then used to look up the **embeddings** (see [Transformers](19-transformers.md)).

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
- Splitting long documents into chunks for [RAG](14-rag.md)

**In my project:** my Telugu language model uses a simple tokenizer where **each Telugu character is one token**, giving **245 tokens** in total ([`tiny_llm_telugu.py`](https://github.com/SEVT-Logistics-Private-Limited/tiny-llm-jetson/blob/main/tiny_llm_telugu.py)).

## Key takeaways

- A token is a unit of text processed by an LLM.
- Tokenization: text → tokens → token IDs → embeddings.
- Tokens affect context window usage, cost, processing time and max prompt and output length.

---

**Previous:** [← Hallucination](21-hallucination.md) · [Home](../README.md)
