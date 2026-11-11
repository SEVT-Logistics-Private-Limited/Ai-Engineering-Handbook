# 14. RAG (Retrieval-Augmented Generation)

> RAG is an approach that combines information retrieval with an LLM to generate answers.

## Introduction

An LLM only knows what it was trained on. It doesn't know your private documents or the latest information. RAG fixes this: first **find** the relevant information, then let the LLM **answer using it**.

## What is it?

**RAG (Retrieval-Augmented Generation)** is an approach that **combines information retrieval with an LLM to generate answers**.

| Step | Meaning |
|---|---|
| **Retrieval** | Find relevant information from documents or a knowledge base |
| **Augmentation** | Add the retrieved information to the LLM prompt |
| **Generation** | Let the LLM produce an answer using the question and the retrieved context |

## Why is it needed?

1. **Reduces hallucination:** the LLM answers from real documents
2. **Latest information:** just update the documents
3. **Cost effective:** no need to retrain the model
4. **Better accuracy**

### RAG vs fine-tuning

| RAG | Fine-tuning |
|---|---|
| Requires a retrieval pipeline | Requires a training dataset and workflow |
| Good for private, changing knowledge | Good for adapting style, tone, behaviour and domain patterns |
| Update knowledge by updating the sources | Requires another training or fine-tuning process |

## How does it work?

### Important terms

- **Document ingestion:** the process of bringing source data into the RAG system and preparing it for retrieval. Sources include:
  1. PDF files
  2. Word documents
  3. HTML pages, text files
  4. Knowledge bases, databases
- **Chunking:** splitting a large document into smaller pieces of text.
- **Embedding:** a numerical vector representing text or other information.
- **Retrieval:** the process of finding relevant information from the indexed knowledge base.

### How do you know your RAG system is working well?

Evaluate it using different metrics:
1. **Retrieval accuracy:** Precision@K, Recall@K
2. **Faithfulness:** does the answer stick to the retrieved information?
3. **Answer relevance:** does the answer match the question?
4. **Context precision:** was the retrieved context useful?
5. **Monitor latency, response quality and hallucination rate in production**

## Flow diagram

```text
User asks a question
        ↓
Embedding
        ↓
Vector search
        ↓
Retrieve context
        ↓
LLM generates the answer
        ↓
Final answer
```

Preparing the documents (done once):

```text
Documents (PDF, Word, HTML)
        ↓
Document ingestion
        ↓
Chunking
        ↓
Embeddings
        ↓
Vector database
```

## Real-world use cases

- Customer support bots that answer from company documents
- Searching internal company knowledge
- Assistants that answer from manuals

## In our project

**Used. This is the core of the assistant:** it answers vehicle questions from **vehicle manuals**.

| RAG part | What we used |
|---|---|
| Documents | Vehicle manuals |
| Embedding model | `intfloat/multilingual-e5-small` |
| Vector database | **ChromaDB** (collection `vehicle_manuals`) |
| Results used | The **1** closest chunk (`n_results=1`) |
| Relevance check | Only used if the distance is **≤ 0.35** (close enough) |
| LLM | Google Gemini |

```text
User asks in Telugu: "ఇంజిన్ ఆయిల్ ఎప్పుడు మార్చాలి?"
        ↓
Translate to English: "When should I change the engine oil?"
        ↓
Embedding (multilingual-e5-small, with "query:" prefix)
        ↓
Search ChromaDB (vehicle_manuals)
        ↓
Closest chunk close enough? (distance ≤ 0.35)
   ├── yes → add the manual text + source to the prompt
   └── no  → answer without the manual
        ↓
Gemini answers in Telugu
        ↓
User hears the answer
```

Details:
- The question is translated first because the **manuals are in English**.
- The manual passage is limited to **1,200 characters** to keep the prompt small.
- The database loads in the **background** when the server starts, so the app works even if the database isn't available.
- `GET /` reports `"kb": "loaded"` or `"kb": "disabled"`, so we can check whether RAG is active.

Code: [`voice-assistant/api.py`](https://github.com/SEVT-Logistics-Private-Limited/tiny-llm-jetson/blob/main/voice-assistant/api.py) (functions `_load_kb`, `retrieve_manual_context`, `build_system`)

---

**Previous:** [← ROS](13-ros.md) · [Home](../README.md) · **Next:** [API →](15-api.md)
