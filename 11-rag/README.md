# 11 — Retrieval-Augmented Generation (RAG)

## What RAG does
RAG combines information retrieval with language generation. Instead of relying only on knowledge encoded in model parameters, an application retrieves relevant external content and supplies it as context to a model.

## Typical ingestion path
Documents → parsing/text extraction → cleaning → chunking → metadata assignment → embedding model → vector index/storage.

## Typical query path
User question → query preprocessing/embedding → retrieval (and optional metadata/hybrid filters) → optional reranking → context assembly → prompt/model generation → answer with grounded references where supported.

## Learning path
1. Why RAG; RAG vs fine-tuning
2. Document loaders and parsing
3. Chunking strategies and overlap
4. Embedding models and vector spaces
5. Vector databases and indexing
6. Similarity metrics and nearest-neighbor search
7. Metadata filtering and hybrid retrieval
8. Top-k selection and reranking
9. Context construction and prompt design
10. Grounded generation and citations
11. FastAPI integration and request lifecycle
12. Evaluation: retrieval quality, answer quality, faithfulness, latency and cost
13. Security: access control, tenant isolation and prompt injection in retrieved content

## Engineering considerations
- Chunk size and overlap affect retrieval granularity and context cost.
- Similarity is not the same as factual correctness.
- Retrieval may return irrelevant or incomplete material; evaluate it independently.
- Preserve source metadata so answers can cite or trace retrieved passages.
- Do not expose documents the requesting user is not authorized to access.

## Project evidence checklist
Record exact parser, chunker, embedding model, vector store, retrieval function, prompt, LLM provider/model, API route, tests and evaluation data. Mark each as verified only after inspecting the implementation.
