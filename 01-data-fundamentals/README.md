# 01 — Data Fundamentals

This module studies the raw forms of information before focusing on specific AI models.

## 1. Text
Learn characters, code points, Unicode, UTF-8, bytes, plain-text files, markup, document formats, tokenization and vocabulary. A character is not necessarily one byte, and a token is not necessarily one word.

## 2. Images
Learn raster images, pixels, width and height, channels, RGB, grayscale, alpha, color spaces, bit depth, resolution, image formats and compression. A decoded image is commonly represented as an array/tensor with dimensions such as height × width × channels.

## 3. Audio
Learn sound as a physical pressure wave and digital audio as samples measured over time. Cover sample rate, amplitude, bit depth, quantization, mono/stereo, waveform, clipping, resampling, codecs and file containers.

## 4. Video
Learn frames, frame rate, timestamps, duration, resolution, codecs, containers and audio tracks. Video processing often samples or decodes frames; temporal order matters.

## 5. Structured and semi-structured data
Cover tables, rows, columns, schemas, JSON, XML, CSV, logs, metadata and database records.

## 6. Multimodal data
Study combinations of modalities, alignment, timestamps, synchronization and shared task context.

## Comparison

| Modality | Raw/digital representation | Common preprocessing | Example model task |
|---|---|---|---|
| Text | Character sequences and encoded bytes | Decode, normalize, tokenize | Language generation |
| Image | Pixel arrays | Decode, resize, crop, normalize | Classification or visual question answering |
| Audio | Time-series samples | Resample, segment, filter, transform | Speech recognition |
| Video | Timestamped frames, often audio | Decode, sample frames, synchronize | Action recognition or summarization |
| Structured | Typed fields and records | Validate, clean, encode categories | Prediction or analytics |

## Important
A file extension alone does not tell you the complete representation. Formats may contain metadata, compression, multiple streams or encoding details. Always inspect and decode data using a format-aware library.

## Next
Continue to [02 — Data Processing](../02-data-processing/README.md).
