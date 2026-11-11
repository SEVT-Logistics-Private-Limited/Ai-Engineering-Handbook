"""Embeddings and semantic search with cosine similarity.

The vectors below are hand-made 4-dimensional features so the numbers are easy to read:
[transport, food, technology, nature]. Real embedding models (e.g. multilingual-e5-small)
learn vectors with hundreds of dimensions automatically.

Run:
    python examples/language_models/embeddings_similarity.py
"""

import numpy as np

EMBEDDINGS = {
    "car":      np.array([0.9, 0.0, 0.3, 0.0]),
    "vehicle":  np.array([0.8, 0.0, 0.2, 0.1]),
    "bus":      np.array([0.9, 0.0, 0.1, 0.0]),
    "banana":   np.array([0.0, 0.9, 0.0, 0.4]),
    "apple":    np.array([0.0, 0.8, 0.3, 0.4]),
    "computer": np.array([0.1, 0.0, 0.9, 0.0]),
    "tree":     np.array([0.0, 0.1, 0.0, 0.9]),
}


def cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
    """1.0 = same direction (same meaning), 0.0 = unrelated."""
    norm = np.linalg.norm(a) * np.linalg.norm(b)
    if norm == 0:
        raise ValueError("cannot compare a zero vector")
    return float(np.dot(a, b) / norm)


def most_similar(query: str, k: int = 3) -> list[tuple[str, float]]:
    q = EMBEDDINGS[query]
    scores = [(w, cosine_similarity(q, v)) for w, v in EMBEDDINGS.items() if w != query]
    return sorted(scores, key=lambda s: s[1], reverse=True)[:k]


def main() -> dict:
    print(f"car vs vehicle: {cosine_similarity(EMBEDDINGS['car'], EMBEDDINGS['vehicle']):.3f}")
    print(f"car vs banana : {cosine_similarity(EMBEDDINGS['car'], EMBEDDINGS['banana']):.3f}")

    results = {}
    for query in ("car", "banana"):
        neighbours = most_similar(query)
        results[query] = neighbours
        pretty = ", ".join(f"{w} ({s:.2f})" for w, s in neighbours)
        print(f"\nsemantic search for {query!r}: {pretty}")
    return results


if __name__ == "__main__":
    main()
