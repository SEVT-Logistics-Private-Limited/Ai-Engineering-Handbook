"""Autoregressive text generation and temperature.

A character-level bigram model counts which character follows which, then generates
text one token at a time: predict next token -> append -> repeat. This is the same
generation loop GPT-style models use, with a far simpler model inside.

Run:
    python examples/language_models/text_generation.py
"""

import numpy as np

CORPUS = "to be or not to be that is the question " * 50  # same toy corpus as tiny-llm-jetson


def apply_temperature(logits: np.ndarray, temperature: float) -> np.ndarray:
    """softmax(logits / T). Low T sharpens the distribution, high T flattens it."""
    if temperature <= 0:
        raise ValueError("temperature must be > 0 (use argmax for greedy decoding)")
    z = logits / temperature
    z = z - z.max()
    p = np.exp(z)
    return p / p.sum()


class BigramModel:
    def __init__(self, text: str):
        self.chars = sorted(set(text))
        self.stoi = {c: i for i, c in enumerate(self.chars)}
        counts = np.ones((len(self.chars), len(self.chars)))  # +1 smoothing
        for a, b in zip(text, text[1:]):
            counts[self.stoi[a], self.stoi[b]] += 1
        self.logits = np.log(counts / counts.sum(axis=1, keepdims=True))

    def generate(self, prompt: str, n_tokens: int, temperature: float, seed: int = 0) -> str:
        rng = np.random.default_rng(seed)
        out = list(prompt)
        for _ in range(n_tokens):
            probs = apply_temperature(self.logits[self.stoi[out[-1]]], temperature)
            out.append(self.chars[rng.choice(len(self.chars), p=probs)])  # sample, then add to context
        return "".join(out)


def entropy(p: np.ndarray) -> float:
    p = p[p > 0]
    return float(-(p * np.log2(p)).sum())


def main() -> dict:
    model = BigramModel(CORPUS)
    logits = model.logits[model.stoi["t"]]
    print("Next-token distribution after 't' (higher entropy = more random):")
    entropies = {}
    for t in (0.3, 1.0, 2.0):
        p = apply_temperature(logits, t)
        entropies[t] = entropy(p)
        top = model.chars[int(p.argmax())]
        print(f"  T={t}: top token {top!r} with p={p.max():.2f}, entropy={entropies[t]:.2f} bits")

    print()
    for t in (0.3, 1.0, 2.0):
        print(f"T={t}: {model.generate('to', 40, t)!r}")
    return {"entropies": entropies}


if __name__ == "__main__":
    main()
