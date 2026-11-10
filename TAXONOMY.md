# AI/ML Topic Taxonomy

Topics are ordered from fundamentals to advanced. **Phase 1** is the minimum viable learning path; **Later** is intentionally deferred.

## 0. Shared first-principles foundations
1. [Phase 1] What is information and data?
2. [Phase 1] Analog information versus digital data.
3. [Phase 1] Binary digits, bits, bytes and number systems.
4. [Phase 1] Files, formats, metadata, storage and transmission.
5. [Phase 1] Programs, algorithms and data structures.
6. [Phase 1] AI vs ML vs deep learning vs generative AI.
7. [Phase 1] Models, parameters, training, inference and evaluation.
8. [Phase 1] Arrays, tensors, dimensions and matrices.
9. [Later] Linear algebra, probability, statistics and calculus for ML.
10. [Later] Optimization, generalization, regularization and experimental design.

## 1. Text

### Representation and preprocessing
1. [Phase 1] What is text? Characters, words, sentences and documents.
2. [Phase 1] Character sets and code points.
3. [Phase 1] ASCII and its limitations.
4. [Phase 1] Unicode and UTF-8 encoding/decoding.
5. [Phase 1] Text files, markup, normalization and newline handling.
6. [Phase 1] Text cleaning and preprocessing.
7. [Phase 1] Tokenization: character, word and subword methods.
8. [Phase 1] Vocabulary, token IDs, unknown and special tokens.
9. [Phase 1] Sequence length, context windows, padding, truncation and masks.
10. [Phase 1] Embeddings: lookup tables, vector dimensions and similarity intuition.
11. [Later] Static vs contextual embeddings and positional representations.

### Sequence models and Transformers
12. [Later] N-gram and statistical language models.
13. [Later] RNNs, LSTMs and GRUs.
14. [Later] Encoder-decoder sequence-to-sequence models and teacher forcing.
15. [Phase 1] Attention as a sequence-modeling mechanism.
16. [Phase 1] Transformer overview: encoder, decoder and decoder-only.
17. [Phase 1] Query, Key, Value and scaled dot-product self-attention.
18. [Phase 1] Multi-head attention and causal/padding masks.
19. [Phase 1] Positional information, feed-forward layers, residuals and normalization.
20. [Phase 1] GPT-style next-token prediction and autoregressive generation.
21. [Later] BERT, T5 and architecture comparisons.

### LLMs and application patterns
22. [Phase 1] What is an LLM? Pretraining vs inference.
23. [Phase 1] Prompting, context construction and decoding controls.
24. [Later] Instruction tuning and supervised fine-tuning.
25. [Later] Parameter-efficient fine-tuning: LoRA and adapters.
26. [Later] Quantization, pruning, distillation and efficient inference.
27. [Phase 1] LLM evaluation basics, hallucinations and grounding.
28. [Phase 1] RAG: ingestion, chunking, embeddings, retrieval and generation.
29. [Later] Reranking, hybrid retrieval, query rewriting and advanced RAG evaluation.
30. [Later] Agents: tool/function calling, planning, state, memory and workflow orchestration.
31. [Later] Multi-agent systems, guardrails, approvals and agent evaluation.

### Text I/O modes
- [Phase 1] Text → Text: completion, chat, classification, extraction, translation and summarization.
- [Later] Text → Image: text-conditioned image generation.
- [Later] Text → Audio: text-to-speech.
- [Later] Text → Video: text-to-video generation.
- [Phase 1] Text + retrieved text → Text: RAG-grounded response.
- [Later] Text + Image → Text: visual question answering.
- [Later] Text + Audio → Text: instruction-conditioned audio understanding.
- [Later] Text + Video → Text: video question answering and summarization.

## 2. Image

### Representation
1. [Phase 1] What is an image? Raster vs vector; capture and file concepts.
2. [Phase 1] Pixels, width, height, channels and image tensors.
3. [Phase 1] Grayscale, RGB/RGBA, color spaces and bit depth.
4. [Phase 1] Resolution, aspect ratio, formats and compression.

### Preprocessing
5. [Phase 1] Image decoding and validation.
6. [Phase 1] Resize, crop, pad, normalize and channel ordering.
7. [Later] Augmentation, denoising, filtering and color transforms.
8. [Later] Patch extraction, tiling and high-resolution image handling.

### Models and tasks
9. [Phase 1] Basic computer-vision pipeline and feature extraction.
10. [Phase 1] CNN fundamentals: convolution, kernels, feature maps and pooling.
11. [Later] Vision Transformers and patch embeddings.
12. [Phase 1] Image classification.
13. [Later] Object detection and localization.
14. [Later] Semantic and instance segmentation.
15. [Later] OCR, image retrieval and visual embeddings.
16. [Later] Image-text alignment and vision-language encoders.

### Generation and evaluation
17. [Later] Text-to-image generation.
18. [Later] Image-to-image transformation, editing and inpainting.
19. [Later] GANs, VAEs, diffusion and autoregressive image models.
20. [Phase 1] Classification metrics: accuracy, precision, recall and confusion matrix.
21. [Later] Detection/segmentation metrics: IoU, mAP and task-specific measures.
22. [Later] Image-generation evaluation: FID, CLIP-based measures and human evaluation.

### Image I/O modes
- [Phase 1] Image → Label: classification.
- [Later] Image → Text: captioning and OCR output.
- [Later] Image + Text → Text: visual question answering.
- [Later] Text → Image: image generation.
- [Later] Image → Image: editing, restoration and transformation.

## 3. Video

### Representation
1. [Phase 1] What is video? Frames ordered over time.
2. [Phase 1] FPS, timestamps, duration, resolution and aspect ratio.
3. [Phase 1] Containers vs codecs; keyframes and compression.
4. [Later] Variable frame rate, color formats and synchronized audio tracks.

### Preprocessing
5. [Phase 1] Decode video and inspect streams/metadata.
6. [Phase 1] Frame extraction and uniform temporal sampling.
7. [Later] Clip segmentation, scene detection and keyframe selection.
8. [Later] Resize, normalize, temporal sampling and audio-video alignment.

### Models and tasks
9. [Phase 1] Frame-based baselines and temporal information.
10. [Later] 2D CNN + temporal models, 3D CNNs and recurrent approaches.
11. [Later] Video Transformers and long-video modeling.
12. [Later] Action recognition, event detection and video classification.
13. [Later] Object tracking and temporal localization.
14. [Later] Video-language models and video question answering.

### Generation and evaluation
15. [Later] Text-to-video and image-to-video generation.
16. [Later] Video-to-video editing, frame interpolation and controlled generation.
17. [Phase 1] Task evaluation basics: classification accuracy and event-level checks.
18. [Later] Temporal consistency, perceptual quality, FVD and human evaluation.

### Video I/O modes
- [Phase 1] Video → Text: sampled-frame description and basic summary.
- [Later] Video + Text → Text: video question answering.
- [Later] Text → Video: video generation.
- [Later] Image → Video: image animation.
- [Later] Video → Video: editing, enhancement and transformation.
- [Later] Audio + Video → Text: synchronized audiovisual understanding.

## 4. Audio

### Representation
1. [Phase 1] What is sound? Pressure waves, amplitude, frequency and time.
2. [Phase 1] Analog-to-digital conversion, sampling and quantization.
3. [Phase 1] Sample rate, bit depth, channels and duration.
4. [Phase 1] Waveforms, PCM, audio formats and codecs.
5. [Later] Windows, frames, Fourier transform, STFT and spectrograms.
6. [Later] Mel scale, Mel spectrograms and MFCC features.

### Preprocessing
7. [Phase 1] Audio decoding, resampling and channel conversion.
8. [Phase 1] Audio segmentation and basic normalization.
9. [Later] Voice activity detection, denoising and endpoint detection.
10. [Later] Feature extraction, augmentation and streaming buffers.

### Models and tasks
11. [Phase 1] Speech-to-text / automatic speech recognition (ASR).
12. [Phase 1] Text-to-speech (TTS) pipeline and voice output.
13. [Later] CTC, RNN-T and encoder-decoder ASR design patterns.
14. [Later] Acoustic models, language models and neural vocoders.
15. [Later] Speaker recognition, diarization and audio event classification.
16. [Later] Speech translation and speech-to-speech models.

### Generation and evaluation
17. [Later] Neural speech generation and voice conversion.
18. [Later] General audio/music generation.
19. [Phase 1] ASR evaluation: Word Error Rate (WER) and Character Error Rate (CER).
20. [Later] TTS evaluation: MOS, intelligibility, naturalness and latency.
21. [Later] PESQ/STOI where appropriate, plus human evaluation.

### Audio I/O modes
- [Phase 1] Audio → Text: transcription / ASR.
- [Phase 1] Text → Audio: speech synthesis / TTS.
- [Later] Audio → Audio: enhancement, conversion or speech-to-speech.
- [Later] Audio + Text → Text: instruction-conditioned audio understanding.
- [Later] Audio → Label: sound and event classification.

## 5. Multimodal

### Representation and alignment
1. [Phase 1] What is multimodal data? Multiple modalities in one task.
2. [Phase 1] Modality-specific input representations and encoders.
3. [Later] Shared embedding spaces and cross-modal alignment.
4. [Later] Time synchronization, modality metadata and missing modalities.

### Preprocessing and fusion
5. [Phase 1] Preparing text + image and audio + text inputs.
6. [Later] Early, late and intermediate fusion patterns.
7. [Later] Cross-attention and multimodal token/feature fusion.
8. [Later] Multimodal retrieval and indexing.

### Models and applications
9. [Phase 1] Vision-language model (VLM) fundamentals.
10. [Later] Audio-language and video-language models.
11. [Later] General-purpose multimodal/omni models.
12. [Later] Multimodal RAG.
13. [Later] Multimodal agents and tool use.
14. [Later] Real-time streaming multimodal systems.

### Generation and evaluation
15. [Later] Cross-modal generation and conditional outputs.
16. [Phase 1] Basic grounding and consistency checks across input modalities.
17. [Later] Modality-specific quality, alignment, temporal consistency and human evaluation.

### Multimodal I/O modes
- [Phase 1] Image + Text → Text: visual question answering.
- [Later] Audio + Text → Text: voice instruction and contextual response.
- [Later] Video + Text → Text: video understanding.
- [Later] Audio + Video → Text: audiovisual summarization.
- [Later] Text → Image/Audio/Video: cross-modal generation.
- [Later] Mixed input modalities → mixed output modalities: interactive assistants.

## 6. Cross-modal engineering
1. [Phase 1] Input/output contracts and modality-aware APIs.
2. [Phase 1] Data validation, preprocessing boundaries and error handling.
3. [Later] Model serving, batching, streaming and latency management.
4. [Later] Evaluation datasets, reproducibility and regression testing.
5. [Later] Security, privacy, governance and content safety.
6. [Later] Deployment, monitoring, cost, scaling and edge inference.

## Label meaning
- **Phase 1:** MVP learning scope; establish first-principles understanding and one practical I/O path per modality where feasible.
- **Later:** advanced or specialized topics to add after the MVP.
- The taxonomy is a curriculum map, not a claim that every topic has already been studied or implemented.