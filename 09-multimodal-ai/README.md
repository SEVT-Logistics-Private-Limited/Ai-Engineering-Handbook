# 09 — Multimodal AI and VLMs

## Core idea
A modality is a type of information such as text, image, audio or video. Multimodal systems accept or combine more than one modality. The architecture may use separate encoders, a shared representation space, modality-specific tokens, cross-attention or other fusion mechanisms.

## Learning path
1. Single-modal vs multimodal systems
2. Modality-specific preprocessing and encoders
3. Representations: token IDs, image patches, audio tokens and embeddings
4. Image-text alignment and contrastive learning
5. Shared embedding spaces and cross-modal retrieval
6. Early, late and intermediate fusion (conceptual patterns)
7. Cross-attention and multimodal Transformers
8. Vision-language models and visual question answering
9. Audio-language and video-language models
10. Multimodal prompting and inference
11. Real-time multimodal systems and synchronization
12. Multimodal RAG and evaluation

## Example conceptual flow
Image + question text → image preprocessing/vision encoder and text tokenization → multimodal fusion or alignment → language generation → textual answer.

This is a simplified pattern, not a universal architecture. Always consult the specific model's documentation.

## Practical labs
- Compare image embeddings and text embeddings from an image-text model.
- Run visual question answering on a small test set.
- Change the image crop/resolution and observe effects.
- Evaluate whether answers are grounded in visible evidence.
- Record failure cases such as small text, occlusion, charts and temporal events.

## VLM project documentation checklist
Record model name/version, processor, image size/crops, prompt format, inference settings, input/output examples, latency, limitations and exact code locations.
