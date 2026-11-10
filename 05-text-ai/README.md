# 05 — Text AI, NLP and LLMs

This module follows text from its digital representation through language modeling and modern LLM applications.

## Learning sequence

### A. Text foundations
- Characters, Unicode, UTF-8 and bytes
- Text normalization and cleaning
- Tokenization strategies: word, character, subword and byte-level
- Vocabulary and token IDs
- Embedding matrices and positional information

### B. Language and NLP
- What NLP is and common tasks
- Language modeling and next-token prediction
- N-grams and statistical language models (historical foundations)
- Neural language models
- Encoder, decoder and encoder-decoder architectures

### C. Transformers
- Sequence modeling and attention motivation
- Query, Key and Value
- Scaled dot-product self-attention
- Multi-head attention
- Causal and padding masks
- Positional encoding/embeddings
- Feed-forward networks, residual connections and normalization
- Encoder-only, decoder-only and encoder-decoder Transformers

### D. LLMs
- Pretraining and objectives
- Instruction tuning and supervised fine-tuning
- Preference alignment (high-level)
- Context windows and long-context limitations
- Inference and autoregressive generation
- Temperature, top-k, top-p and stopping
- Quantization and efficient inference
- Evaluation, hallucinations and safety

## Text-to-text conceptual pipeline

Text input → tokenizer → token IDs → token embeddings + position information → Transformer layers → vocabulary logits → decoding/sampling → generated token IDs → detokenized text.

Exact details vary by model family. Some systems add system prompts, tools, retrieval context, multimodal tokens or other orchestration.

## Project connection: Tiny LLM / GPT-style implementation

Use the shared [topic template](../resources/templates/TOPIC-TEMPLATE.md) and record project evidence for each concept. Potential evidence to inspect includes:
- tokenizer/vocabulary implementation and token-to-ID mapping;
- embedding and positional representation code;
- attention and Transformer block implementations;
- model configuration and parameter counts;
- training loop, loss, optimizer and checkpoints;
- inference/generation code and sampling settings;
- tests, sample runs and hardware constraints.

**Evidence rule:** Do not claim a component was implemented merely because it is covered in this handbook. Link to the exact file, function, commit or test in the project repository. If the implementation has not been inspected, label it "to verify".
