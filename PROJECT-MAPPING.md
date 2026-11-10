# Project-to-Topic Mapping

This map links handbook concepts to implementation evidence. Code presence is not a claim that the experiment was independently rerun here.

## Tiny LLM / Jetson project

**Repository:** [SEVT Logistics — tiny-llm-jetson](https://github.com/SEVT-Logistics-Private-Limited/tiny-llm-jetson)

| Topic | Evidence file / symbol | What it demonstrates |
|---|---|---|
| Text corpus | [tiny_llm.py](https://github.com/SEVT-Logistics-Private-Limited/tiny-llm-jetson/blob/main/tiny_llm.py) | Text is the training source |
| Character tokenization | `chars`, `stoi`, `itos`, `encode`, `decode` | Character-to-integer mapping |
| Token IDs / batches | `data`, `get_batch()` | Integer sequences and shifted targets |
| Token embeddings | `TinyGPT.tok` | Maps token IDs to learned vectors |
| Position embeddings | `TinyGPT.pos` | Adds learned position representations |
| Self-attention | `Block.attn` | PyTorch multi-head attention |
| Causal masking | `Block.forward()` | Prevents attention to future positions |
| Feed-forward network | `Block.mlp` | Per-position nonlinear transformation |
| Normalization / residuals | `ln1`, `ln2`, residual additions | Stabilizes and carries representations |
| Language-model loss | `F.cross_entropy` | Next-token prediction objective |
| Optimization | `torch.optim.AdamW` | Updates model parameters |
| Generation | `TinyGPT.generate()` | Autoregressive next-token sampling |
| Checkpoint verification | [test_tiny_llm.py](https://github.com/SEVT-Logistics-Private-Limited/tiny-llm-jetson/blob/main/test_tiny_llm.py) | Loads weights and generates from seed strings |
| Telugu corpus/model | [tiny_llm_telugu.py](https://github.com/SEVT-Logistics-Private-Limited/tiny-llm-jetson/blob/main/tiny_llm_telugu.py) | Telugu text dataset and character vocabulary |
| API/backend | [telugu_voice_api.py](https://github.com/SEVT-Logistics-Private-Limited/tiny-llm-jetson/blob/main/telugu_voice_api.py) | FastAPI endpoints and Gemini SDK calls |

## Important distinction

The custom GPT model code and deployed voice assistant API are separate paths. The current API uses the Google Gemini SDK for speech recognition, language generation and TTS; it should not be represented as serving the local TinyGPT checkpoint without further code evidence.

## Other project mappings

| Topic | RAG application | VLM experiments | EV application |
|---|---|---|---|
| Python / APIs | To verify against source | To verify against source | To verify against source |
| Embeddings / retrieval | To verify against source | To verify against source | To verify against source |
| Image preprocessing / vision encoder | N/A unless image documents | To verify against source | To verify against source |
| Audio / speech | To verify against source | To verify against source | To verify against source |

Update rows only after inspecting the corresponding project repository and linking exact files, functions or tests.