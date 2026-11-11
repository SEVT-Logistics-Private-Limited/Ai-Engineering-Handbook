"""Tokenization: turning text into token IDs and back.

Two simple tokenizers built from scratch:
- CharTokenizer: one token per character (what tiny-llm-jetson uses)
- WordTokenizer: one token per word, with an <unk> token for unseen words

Production LLMs use subword tokenizers (BPE, SentencePiece) that sit between these two.

Run:
    python examples/language_models/tokenizer.py
"""

import re


class CharTokenizer:
    def __init__(self, corpus: str):
        self.chars = sorted(set(corpus))
        self.stoi = {c: i for i, c in enumerate(self.chars)}
        self.itos = {i: c for c, i in self.stoi.items()}

    @property
    def vocab_size(self) -> int:
        return len(self.chars)

    def encode(self, text: str) -> list[int]:
        unknown = set(text) - self.stoi.keys()
        if unknown:
            raise ValueError(f"characters not in vocabulary: {sorted(unknown)}")
        return [self.stoi[c] for c in text]

    def decode(self, ids: list[int]) -> str:
        return "".join(self.itos[i] for i in ids)


class WordTokenizer:
    UNK = "<unk>"
    PATTERN = re.compile(r"\w+|[^\w\s]")  # words and individual punctuation marks

    def __init__(self, corpus: str):
        words = sorted(set(self.split(corpus)))
        self.vocab = [self.UNK] + words
        self.stoi = {w: i for i, w in enumerate(self.vocab)}

    @classmethod
    def split(cls, text: str) -> list[str]:
        return cls.PATTERN.findall(text.lower())

    def encode(self, text: str) -> list[int]:
        return [self.stoi.get(w, self.stoi[self.UNK]) for w in self.split(text)]

    def decode(self, ids: list[int]) -> str:
        return " ".join(self.vocab[i] for i in ids)


def main() -> dict:
    corpus = "AI is amazing. AI models read tokens, not raw words."

    char_tok = CharTokenizer(corpus)
    text = "AI is amazing."
    char_ids = char_tok.encode(text)
    print(f"Character tokenizer (vocab size {char_tok.vocab_size})")
    print(f"  {text!r} -> {char_ids}")
    print(f"  {len(text)} characters -> {len(char_ids)} tokens")
    assert char_tok.decode(char_ids) == text

    word_tok = WordTokenizer(corpus)
    word_ids = word_tok.encode(text)
    print(f"\nWord tokenizer (vocab size {len(word_tok.vocab)})")
    print(f"  {text!r} -> {word_ids}")
    print(f"  tokens: {word_tok.split(text)}")

    unseen = "AI is incredible."
    unseen_ids = word_tok.encode(unseen)
    print(f"\nUnseen word: {unseen!r} -> {unseen_ids} -> {word_tok.decode(unseen_ids)!r}")

    return {"char_tokens": len(char_ids), "word_tokens": len(word_ids), "unseen_ids": unseen_ids}


if __name__ == "__main__":
    main()
