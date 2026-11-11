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

**In my project:** the Telugu voice assistant uses RAG to answer vehicle questions from **vehicle manuals**:

```text
User asks in Telugu
        ↓
Translate the query (Telugu → English)
        ↓
Retrieve from ChromaDB (vehicle manuals)
        ↓
LLM generates the answer (in Telugu)
        ↓
User hears the answer
```

## Key takeaways

- RAG = Retrieval + Augmentation + Generation.
- It reduces hallucination and keeps answers up to date without retraining.
- Key parts: document ingestion, chunking, embeddings, retrieval.

---

**Previous:** [← ROS](13-ros.md) · [Home](../README.md) · **Next:** [API →](15-api.md)
