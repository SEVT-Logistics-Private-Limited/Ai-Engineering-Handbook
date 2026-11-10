# 02 — Data Processing and Representation

The purpose of this module is to understand how raw digital data is converted into a form a particular model or algorithm can consume.

## Common pipeline

1. **Acquire:** Receive a file, stream, database record or user input.
2. **Decode:** Interpret bytes according to the file format and encoding.
3. **Validate:** Check type, schema, size, integrity and expected fields.
4. **Clean:** Handle missing, corrupt, duplicated or irrelevant data.
5. **Preprocess:** Normalize, resize, resample, segment or transform as required.
6. **Represent:** Convert to tokens, tensors, features or embeddings.
7. **Batch:** Group examples; use padding and masks where the model requires them.
8. **Feed the model:** Respect the model's expected dimensions, range and format.

## Topics

- Encoding and decoding: character encodings, binary formats, serialization.
- Preprocessing: normalization, resizing, cropping, filtering, augmentation.
- Tokenization: splitting text into model-specific tokens and mapping tokens to IDs.
- Embeddings: learned dense vectors representing tokens, images, audio segments or other items.
- Feature extraction: computing useful attributes from raw data.
- Tensor fundamentals: dimensions, shapes, data types, devices and operations.
- Batching, padding and masks: efficient processing of variable-length inputs.
- Data pipelines: reproducible loading, transformation and batching.

## Do not confuse these terms

- **Encoding** maps data to a representation under a defined scheme.
- **Tokenization** divides text into units defined by a tokenizer.
- **Token IDs** are integer indices in a vocabulary.
- **Embeddings** are vectors, often learned, associated with tokens or other inputs.
- **Features** are input attributes; they may be hand-designed or learned.

Not every AI model uses the same pipeline. For example, a vision model may process image patches, while another model may use a convolutional encoder. Follow the actual model's preprocessing specification.

## Practical labs

- Inspect UTF-8 bytes and decode them.
- Tokenize the same sentence with two tokenizers and compare results.
- Load an image and print its shape, dtype and pixel range.
- Load a WAV file and inspect sample rate, channels and duration.
- Decode an MP4 and extract frames at selected timestamps.
- Build a small Python preprocessing pipeline with tests.
