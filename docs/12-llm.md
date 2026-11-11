# 12. LLM (Large Language Model)

> An LLM is an AI model trained on a huge amount of text data to understand and generate human language.

## Introduction

ChatGPT, Claude and Gemini are all LLMs. They can answer questions, write and summarise, and all of them work by predicting text one token at a time.

## What is it?

An **LLM (Large Language Model)** is an AI model (a neural network) **trained on a very large amount of text data** to learn patterns in language, the relationships between tokens, and to **predict the next token** in a sequence.

**In simple words:** it learns patterns from text, and uses those patterns to understand and generate language.

Examples: models from families such as **GPT, Claude, Gemini**.

### GPT-style models

**GPT** stands for **Generative Pre-trained Transformer**.

GPT-style models are generally **decoder-only** [Transformer](19-transformers.md) models designed for **autoregressive generation**: the model generates the answer **token by token**.

Examples: GPT-3, GPT-4, GPT-5, Llama, Qwen.

## Why is it needed?

A single LLM can answer questions, explain topics, write, summarise, translate and hold a conversation.

## How does it work?

### How does an LLM read text?

1. **Text input:** "I love AI"
2. **Tokenization:** ["I", "love", "AI"]
3. **Token IDs:** [40, 2031, 1589]
4. **Embeddings:** a numerical vector representing each token
5. **Transformer** processes the embeddings

### How does it generate an answer?

Predict the next token → add it to the context → predict the next token → repeat.

### Temperature

**Temperature** controls the **randomness of token selection** during generation. It affects the generation (sampling) process.
- **Low temperature:** focused, predictable answers
- **High temperature:** more random and creative answers

## Flow diagram

How an LLM reads text:

```text
Text input: "I love AI"
        ↓
Tokenization: ["I", "love", "AI"]
        ↓
Token IDs: [40, 2031, 1589]
        ↓
Embeddings (numbers for each token)
        ↓
Transformer processes the embeddings
```

How a GPT-style model generates an answer:

```text
Input tokens
     ↓
Transformer
     ↓
Predict next token
     ↓
Add token to context
     ↓
Predict next token
     ↓
Repeat
```

## Real-world use cases

- Chat assistants (ChatGPT, Claude, Gemini)
- Writing, summarising and translating
- Coding help
- Voice assistants

## In our project

**Used, in two ways.**

### 1. Gemini powers the live assistant

The LLM does three jobs in our voice assistant:

| Job | Example |
|---|---|
| **Answer questions** | Generates Yodha's Telugu answer |
| **Translate** | Telugu question → English for the manual search |
| **Speech to text (backup)** | Transcribes Telugu audio when the browser can't |

**Fallback chain:** if one model fails or returns nothing, the next one is tried automatically.

```text
gemini-3.6-flash → (fails) → gemini-2.0-flash → (fails) → gemini-1.5-flash → (all fail) → polite Telugu apology
```

- Answers are limited to **500 output tokens** (`max_output_tokens`) to keep them short and fast.
- The **last 8 messages** of the conversation are sent each time, so the assistant remembers context.

### 2. We built our own GPT-style models from scratch

| Model | Parameters | Trained on |
|---|---|---|
| Rung 1 | 984 | Jetson Orin Nano |
| Rung 2 | 990K | Jetson Orin Nano |
| Rung 5 | ~1B | Colab A100 |
| Rung 7 | ~3B | Colab A100 |
| **Telugu model** | **25M** | Colab A100, real Telugu text |

Each one is a decoder-only model that generates text **token by token**, exactly as described above. The goal is to eventually replace Gemini with our own Telugu model.

Code: [`voice-assistant/api.py`](https://github.com/SEVT-Logistics-Private-Limited/tiny-llm-jetson/blob/main/voice-assistant/api.py) (`_llm_call_with_fallback`, `telugu_llm`), [`tiny_llm.py`](https://github.com/SEVT-Logistics-Private-Limited/tiny-llm-jetson/blob/main/tiny_llm.py), [`tiny_llm_telugu.py`](https://github.com/SEVT-Logistics-Private-Limited/tiny-llm-jetson/blob/main/tiny_llm_telugu.py)

## Key takeaways

- An LLM is trained on huge amounts of text to learn language and predict the next token.
- GPT = Generative Pre-trained Transformer: decoder-only, generating token by token.
- Temperature controls randomness.

---

**Previous:** [← VLA](11-vla.md) · [Home](../README.md) · **Next:** [ROS →](13-ros.md)
