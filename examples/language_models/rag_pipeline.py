"""A minimal, dependency-light RAG pipeline: ingestion -> chunking -> embeddings ->
vector search -> augmented prompt, plus retrieval evaluation (Precision@K, Recall@K).

Embeddings here are TF-IDF vectors computed with NumPy so the example runs anywhere.
Production systems swap in a neural embedding model (e.g. multilingual-e5-small) and a
vector database (e.g. ChromaDB); the pipeline shape stays the same.

The documents are short sample texts written for this example, not real manuals.
The final LLM call is left to you: send `build_prompt(...)` to any chat model.

Run:
    python examples/language_models/rag_pipeline.py
"""

import re
from dataclasses import dataclass

import numpy as np

SAMPLE_DOCUMENTS = {
    "engine-manual.txt": (
        "Engine oil should be changed every 10,000 km or once a year, whichever comes first. "
        "Use the oil grade listed on the filler cap. Check the oil level every month with the dipstick "
        "while the engine is cold and the vehicle is on level ground."
    ),
    "tyres-manual.txt": (
        "Recommended tyre pressure is 32 psi for the front tyres and 30 psi for the rear tyres. "
        "Check tyre pressure when the tyres are cold. Rotate the tyres every 8,000 km to keep wear even."
    ),
    "battery-manual.txt": (
        "If the battery warning light stays on while driving, the charging system may be faulty. "
        "Turn off unnecessary electrical loads and visit a service centre. Batteries usually last three to five years."
    ),
}


@dataclass
class Chunk:
    source: str
    text: str


def tokenize(text: str) -> list[str]:
    return re.findall(r"[a-z0-9,]+", text.lower())


def chunk_text(text: str, chunk_size: int = 25, overlap: int = 5) -> list[str]:
    """Split text into chunks of `chunk_size` words; consecutive chunks share `overlap` words."""
    if not 0 <= overlap < chunk_size:
        raise ValueError("overlap must be >= 0 and smaller than chunk_size")
    words = text.split()
    step = chunk_size - overlap
    return [" ".join(words[i:i + chunk_size]) for i in range(0, max(len(words) - overlap, 1), step)]


def ingest(documents: dict[str, str]) -> list[Chunk]:
    return [Chunk(src, c) for src, text in documents.items() for c in chunk_text(text)]


class TfidfIndex:
    """A tiny in-memory vector store: TF-IDF embeddings + cosine-similarity search."""

    def __init__(self, chunks: list[Chunk]):
        self.chunks = chunks
        docs = [tokenize(c.text) for c in chunks]
        self.vocab = {w: i for i, w in enumerate(sorted({w for d in docs for w in d}))}
        df = np.zeros(len(self.vocab))
        for d in docs:
            for w in set(d):
                df[self.vocab[w]] += 1
        self.idf = np.log((1 + len(docs)) / (1 + df)) + 1
        self.matrix = np.vstack([self.embed(" ".join(d)) for d in docs])

    def embed(self, text: str) -> np.ndarray:
        vec = np.zeros(len(self.vocab))
        for w in tokenize(text):
            if w in self.vocab:
                vec[self.vocab[w]] += 1
        vec *= self.idf
        norm = np.linalg.norm(vec)
        return vec / norm if norm else vec

    def search(self, query: str, k: int = 2, min_score: float = 0.1) -> list[tuple[Chunk, float]]:
        scores = self.matrix @ self.embed(query)  # cosine similarity (all vectors are unit length)
        best = np.argsort(scores)[::-1][:k]
        return [(self.chunks[i], float(scores[i])) for i in best if scores[i] >= min_score]


def build_prompt(question: str, results: list[tuple[Chunk, float]]) -> str:
    if not results:
        context = "No relevant documents were found."
    else:
        context = "\n".join(f"[{c.source}] {c.text}" for c, _ in results)
    return (
        "Answer the question using only the context below. "
        "If the answer is not in the context, say you don't know.\n\n"
        f"Context:\n{context}\n\nQuestion: {question}\nAnswer:"
    )


def precision_recall_at_k(retrieved: list[str], relevant: set[str], k: int) -> tuple[float, float]:
    top = retrieved[:k]
    hits = sum(1 for s in top if s in relevant)
    return hits / k, hits / len(relevant)


def main() -> dict:
    chunks = ingest(SAMPLE_DOCUMENTS)
    index = TfidfIndex(chunks)
    print(f"ingested {len(SAMPLE_DOCUMENTS)} documents -> {len(chunks)} chunks, vocabulary of {len(index.vocab)} words\n")

    question = "When should I change the engine oil?"
    results = index.search(question)
    print(f"query: {question}")
    for c, score in results:
        print(f"  {score:.2f}  [{c.source}] {c.text[:60]}...")
    print("\n--- augmented prompt sent to the LLM ---")
    print(build_prompt(question, results))

    eval_set = [
        ("When should I change the engine oil?", {"engine-manual.txt"}),
        ("What tyre pressure should I use?", {"tyres-manual.txt"}),
        ("The battery light is on, what do I do?", {"battery-manual.txt"}),
    ]
    k = 1
    precisions, recalls = [], []
    for q, relevant in eval_set:
        retrieved = [c.source for c, _ in index.search(q, k=k, min_score=0.0)]
        p, r = precision_recall_at_k(retrieved, relevant, k)
        precisions.append(p)
        recalls.append(r)
    print(f"\nretrieval evaluation on {len(eval_set)} questions: "
          f"Precision@{k}={np.mean(precisions):.2f}, Recall@{k}={np.mean(recalls):.2f}")
    return {"top_source": results[0][0].source if results else None,
            "precision": float(np.mean(precisions)), "recall": float(np.mean(recalls))}


if __name__ == "__main__":
    main()
