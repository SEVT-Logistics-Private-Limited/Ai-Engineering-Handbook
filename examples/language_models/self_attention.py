"""Scaled dot-product self-attention, causal masking and multi-head attention in NumPy.

The token embeddings and projection weights are random (seeded), so the attention
pattern itself carries no meaning. The point is the mechanics and the tensor shapes.
In a trained model these weights are learned.

Run:
    python examples/language_models/self_attention.py
"""

import numpy as np


def softmax(x: np.ndarray, axis: int = -1) -> np.ndarray:
    x = x - x.max(axis=axis, keepdims=True)  # subtract the max for numerical stability
    e = np.exp(x)
    return e / e.sum(axis=axis, keepdims=True)


def causal_mask(seq_len: int) -> np.ndarray:
    """True above the diagonal = future positions that must be hidden."""
    return np.triu(np.ones((seq_len, seq_len), dtype=bool), k=1)


def attention(q: np.ndarray, k: np.ndarray, v: np.ndarray, mask: np.ndarray | None = None):
    """softmax(Q K^T / sqrt(d_k)) V. Returns (output, attention_weights)."""
    d_k = q.shape[-1]
    scores = q @ k.swapaxes(-1, -2) / np.sqrt(d_k)  # how well each query matches each key
    if mask is not None:
        scores = np.where(mask, -np.inf, scores)    # masked positions get zero weight after softmax
    weights = softmax(scores, axis=-1)
    return weights @ v, weights


def multi_head_attention(x: np.ndarray, n_heads: int, rng: np.random.Generator, causal: bool = True):
    seq_len, d_model = x.shape
    if d_model % n_heads:
        raise ValueError("d_model must be divisible by n_heads")
    d_head = d_model // n_heads

    w_q, w_k, w_v, w_o = (rng.normal(0, d_model ** -0.5, (d_model, d_model)) for _ in range(4))
    # Project, then split the last dimension into heads: (n_heads, seq_len, d_head)
    split = lambda t: t.reshape(seq_len, n_heads, d_head).transpose(1, 0, 2)
    q, k, v = split(x @ w_q), split(x @ w_k), split(x @ w_v)

    mask = causal_mask(seq_len) if causal else None
    heads, weights = attention(q, k, v, mask)              # every head runs in parallel
    combined = heads.transpose(1, 0, 2).reshape(seq_len, d_model)  # concatenate heads
    return combined @ w_o, weights


def main() -> dict:
    tokens = ["I", "love", "Artificial", "Intelligence"]
    d_model, n_heads = 8, 2
    rng = np.random.default_rng(42)
    x = rng.normal(size=(len(tokens), d_model))  # one embedding vector per token

    out, weights = multi_head_attention(x, n_heads, rng)
    print(f"input  shape: {x.shape}  (tokens, d_model)")
    print(f"output shape: {out.shape}  (tokens, d_model)")
    print(f"attention weights shape: {weights.shape}  (heads, query tokens, key tokens)\n")

    print("Head 1 attention weights (rows = query token, columns = key token):")
    print(" " * 14 + "".join(f"{t[:10]:>12}" for t in tokens))
    for t, row in zip(tokens, weights[0]):
        print(f"{t[:12]:>12}  " + "".join(f"{w:>12.2f}" for w in row))
    print("\nZeros above the diagonal = the causal mask hides future tokens.")
    return {"weights": weights, "output": out}


if __name__ == "__main__":
    main()
