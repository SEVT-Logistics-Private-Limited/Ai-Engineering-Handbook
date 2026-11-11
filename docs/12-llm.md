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

**In my project:**
- The live Telugu voice assistant uses **Google Gemini** as its LLM.
- I also built GPT-style models **from scratch**, from 984 parameters up to about 3 billion ([tiny-llm-jetson](https://github.com/SEVT-Logistics-Private-Limited/tiny-llm-jetson)).

## Key takeaways

- An LLM is trained on huge amounts of text to learn language and predict the next token.
- GPT = Generative Pre-trained Transformer: decoder-only, generating token by token.
- Temperature controls randomness.

---

**Previous:** [← VLA](11-vla.md) · [Home](../README.md) · **Next:** [ROS →](13-ros.md)
