# Learning Map

This map explains the dependency order and the main questions each stage answers.

## 1. From real-world information to digital data
**Question:** How does a computer represent something a human can see, hear or read?

- Text is represented through character standards and byte encodings.
- Images are grids of pixel values with dimensions, channels and color spaces.
- Audio is a sampled digital signal.
- Video is a time-ordered sequence of frames, commonly with an audio stream.
- Structured data is organized into fields, records and schemas.

## 2. From digital data to model inputs
**Question:** How do raw files become numerical inputs?

Decode files → validate and clean → preprocess → transform into tokens, pixels/tensors, signal features or frame sequences → batch and pad → provide to a model.

The exact path depends on the modality and model. Not every model uses embeddings in the same way.

## 3. From model inputs to learned behavior
**Question:** How does a model learn patterns?

A model computes outputs using parameters. During training, a loss measures error and an optimizer updates parameters. During inference, the learned parameters are used without the normal training update step.

## 4. From specialized models to multimodal systems
**Question:** How can models work with text, images, audio and video?

Specialized encoders or tokenizers convert each modality into representations. Architectures align or combine these representations so the model can perform tasks across modalities. Implementations vary: some models accept multiple modalities natively; others use separate components and orchestration.

## 5. From models to applications
**Question:** How does a user interact with a reliable AI feature?

A client sends a request to an API. The backend validates it, loads context or retrieves data if needed, invokes a model, handles errors and formats a response. Production systems also need security, evaluation, monitoring, testing and cost controls.

## Core distinction
A **modality** is the kind of information (text, image, audio, video). A **representation** is how that information is encoded for processing (bytes, token IDs, pixel tensors, waveform samples, embeddings). A **model architecture** defines how representations are processed. An **application** connects models to users, data and infrastructure.
