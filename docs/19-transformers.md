# 19. Transformers

> A Transformer is a type of deep learning architecture that helps computers understand and generate human language.

## Introduction

Every modern LLM (GPT, Claude, Gemini, Llama) is built on the Transformer. This page covers its architecture, encoders and decoders, embeddings, self-attention (Query, Key, Value), multi-head attention and masking.

## What is it?

A **Transformer** is a **type of deep learning architecture**. It helps computers **understand and generate human language**.

## Why is it needed?

A Transformer looks at **all the words at once** and works out how they relate to each other. That's what lets it understand context, for example which meaning of "bank" is intended in a sentence.

## How does it work?

### Architecture

| Step | What it does |
|---|---|
| Input text | The sentence |
| Tokenization | Split the text into [tokens](22-tokenization.md) |
| Embeddings | Convert the tokens into vectors (numbers) |
| Positional encoding | Add word-order information |
| Transformer layers | Understand context, using self-attention and a feed-forward network |
| Output predictions | Generate or classify text |

**Transformer layers:** one layer processes the input, then the next layer processes the updated result (attention + feed-forward).

### Embeddings

An **embedding** is a **numerical vector representation of data**, such as text, designed to capture useful **semantic relationships** (meaning).

- Tokens are units of text.
- Embeddings are numerical representations.

Embeddings are mostly used in:
1. Semantic search
2. Recommendation systems
3. Clustering
4. RAG
5. Document retrieval

### Encoder vs decoder

| Encoder | Decoder |
|---|---|
| **Understands** the given text | **Generates** the next token |
| A neural network that processes input text and understands the relationships between tokens | A Transformer architecture that generates text one token at a time, using the previous tokens as context |
| Builds rich representations of the input | Designed for generating output tokens |
| Used for understanding / classification | Used for text generation |
| Examples: text classification, sentiment analysis | Examples: GPT-style models |

### Self-attention

**Self-attention** is a mechanism that allows Transformers to **understand the relationship between different words (tokens) in a sentence**.

Example: **"bank"** can mean a money bank or a river bank. Self-attention looks at the other words to work out which one is meant.

### Query, Key and Value (Q / K / V)

| | Question |
|---|---|
| **Query** | What am I looking for? |
| **Key** | What does each item offer? How relevant is it? |
| **Value** | What information do I get? |

**The library example:** imagine you're in a library with 1000 books, and you want a book about AI.
1. You ask the librarian: "I want a book about AI." → this is your **Query**.
2. The librarian checks the labels and titles of each book (Python, AI, Cooking) and compares your request with those labels. This is the purpose of the **Key**: the information used to decide which book matches your search.
3. The librarian finds the book and gives it to you. You open it and get the actual information. This information is the **Value**: the actual content of the selected book.

In a sentence like **"I love Artificial Intelligence"**, each word becomes a token, each token gets a vector of numbers, and **every token has its own Q, K and V**.

### Multi-head attention

Instead of performing only one attention calculation, Transformers use **multiple attention heads**. Each head can learn different types of relationships:
- Head 1: grammatical relationships
- Head 2: nearby-word relationships
- Head 3: coreference (which word "it" refers to)
- Head 4: semantic relationships

**Definition:** multi-head attention performs attention in multiple learned representation subspaces in parallel, allowing the model to capture different relationships between tokens.

| Self-attention | Multi-head attention |
|---|---|
| One attention operation | Multiple attention operations running in parallel |

### Masking

**Masking** is a technique that prevents the Transformer from accessing certain information when it shouldn't. It **hides selected words or tokens from the attention mechanism**.

**The exam example:** imagine you are writing an exam and the question is:

> "The capital of India is ______"

You need to fill in the blank. But imagine the teacher shows you the answer before you even attempt it. Then you learn nothing. **This is where masking comes in:** when the model learns to predict the next word, the future words are hidden.

## Flow diagram

Transformer architecture:

```text
Input text
    ↓
Tokenization (split text into tokens)
    ↓
Embeddings (convert tokens into vectors)
    ↓
Positional encoding (add word-order information)
    ↓
Transformer layers (understand context: self-attention + feed-forward network)
    ↓
Output predictions (generate or classify text)
```

Embeddings:

```text
Text → Tokens → Token IDs → Embedding vectors
```

Self-attention:

```text
"I love Artificial Intelligence"
            ↓
  [I]  [Love]  [Artificial]  [Intelligence]
            ↓
  each token gets a vector (numbers)
            ↓
  each token gets its own  Q  K  V
```

Multi-head attention:

```text
            Input
     ┌────────┼────────┐
     ↓        ↓        ↓
   Head 1   Head 2   Head 3
     └────────┼────────┘
              ↓
           Combine
              ↓
            Output
```

## Real-world use cases

- LLMs: GPT, Claude, Gemini, Llama
- Translation
- Text classification and sentiment analysis
- Image understanding (Vision Transformers in [VLMs](10-vlm.md))

**In my project:** my Telugu language model is a Transformer with:
- **Transformer layers: 8**
- **Attention heads: 8**
- **Context length: 128** (the maximum number of tokens the model can process together in one input)

Code: [`tiny_llm_telugu.py`](https://github.com/SEVT-Logistics-Private-Limited/tiny-llm-jetson/blob/main/tiny_llm_telugu.py)

## Key takeaways

- A Transformer = tokenization → embeddings → positional encoding → Transformer layers → output.
- Encoder = understands. Decoder = generates (GPT is decoder-only).
- Self-attention uses Query, Key and Value. Multi-head attention runs several attentions in parallel.
- Masking hides future words so the model can't peek at the answer.

---

**Previous:** [← DL](18-dl.md) · [Home](../README.md) · **Next:** [Prompt Engineering →](20-prompt-engineering.md)
