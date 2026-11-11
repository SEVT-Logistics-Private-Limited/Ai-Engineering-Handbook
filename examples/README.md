# Examples

Runnable code for every chapter. Each script is self-contained, prints what it's doing, and is covered by the test suite.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Run

From the repository root:

```bash
python examples/language_models/rag_pipeline.py
```

## Index

| Chapter | Script | Demonstrates | Dependencies |
|---|---|---|---|
| Computing Foundations | [`binary_and_bytes.py`](computing_foundations/binary_and_bytes.py) | Binary, bytes, UTF-8, image size in bytes | stdlib |
| AI Fundamentals | [`training_loop.py`](ai_fundamentals/training_loop.py) | Epochs, batches, forward pass, loss, gradients, updates | numpy |
| Language Models | [`tokenizer.py`](language_models/tokenizer.py) | Character and word tokenizers, `<unk>` handling | stdlib |
| Language Models | [`embeddings_similarity.py`](language_models/embeddings_similarity.py) | Cosine similarity, semantic search | numpy |
| Language Models | [`self_attention.py`](language_models/self_attention.py) | Scaled dot-product attention, causal mask, multi-head | numpy |
| Language Models | [`text_generation.py`](language_models/text_generation.py) | Autoregressive generation, temperature | numpy |
| Language Models | [`prompt_templates.py`](language_models/prompt_templates.py) | Zero/one/few-shot, chain of thought, role prompts | stdlib |
| Language Models | [`rag_pipeline.py`](language_models/rag_pipeline.py) | Chunking, TF-IDF retrieval, augmented prompt, Precision@K / Recall@K | numpy |
| Computer Vision | [`image_as_array.py`](computer_vision/image_as_array.py) | Pixels, RGB, grayscale, resizing, normalisation | numpy |
| Computer Vision | [`video_as_frames.py`](computer_vision/video_as_frames.py) | Frames, FPS, raw video size, frame sampling | numpy |
| Computer Vision | [`image_patches.py`](computer_vision/image_patches.py) | Vision Transformer patch embeddings | numpy |
| APIs | [`rest_api.py`](apis/rest_api.py) | FastAPI CRUD: GET, POST, PUT, DELETE, validation | fastapi, httpx |

## Test

```bash
pytest examples/tests -q
```

## Notes

- Examples use small, dependency-light implementations so the mechanics stay visible. Each docstring names the production library you'd use instead.
- Random weights (attention, patch projection) are seeded and **untrained**. They show tensor shapes and data flow, not learned behaviour.
- The RAG example's documents are sample texts written for the example, not real manuals.
