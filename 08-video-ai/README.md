# 08 — Video AI

## Learning path
1. Video as a sequence of timestamped frames, often with audio
2. Frame rate (FPS), duration, resolution and aspect ratio
3. Containers vs codecs; compression and decoding
4. Keyframes, timestamps and variable frame rate
5. Frame extraction and temporal sampling
6. Spatial preprocessing: resize, crop and normalization
7. Temporal information: ordering, motion and frame intervals
8. Object detection and tracking across frames
9. Action recognition and event detection
10. Video classification and summarization
11. Audio-video synchronization
12. Video transformers and temporal modeling
13. Evaluation and operational constraints

## Conceptual pipeline
Video container → demultiplex/decode → timestamped frames (+ audio stream) → frame sampling and preprocessing → spatial/temporal model → event labels, captions or summary.

A system may process every frame, selected frames, short clips, or learned frame tokens. Sampling strategy affects compute cost and what events can be observed.

## Practical labs
- Inspect an MP4's duration, dimensions and frame rate.
- Extract frames at chosen timestamps.
- Compare uniform sampling with scene/keyframe sampling.
- Track an object across a short clip.
- Build a simple video summary from sampled frames and note missed events.
