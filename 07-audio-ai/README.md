# 07 — Audio AI and Speech

## Learning path
1. Sound as a physical wave: amplitude, frequency and time
2. Analog-to-digital conversion: sampling and quantization
3. Sample rate, bit depth, channels, clipping and dynamic range
4. Waveforms, windows, frames and overlap
5. Fourier transform and frequency-domain representation
6. Spectrograms and Mel spectrograms
7. MFCCs and learned audio features
8. Audio decoding, resampling, denoising and voice activity detection
9. Speech-to-text (automatic speech recognition)
10. Text-to-speech and vocoders
11. Speaker diarization/recognition and audio event classification
12. Streaming and low-latency audio systems
13. Evaluation: word error rate, latency and subjective audio quality

## Conceptual speech-to-text pipeline
Audio stream/file → decode → resample/normalize → segment or detect speech → acoustic/audio model → text decoding → transcript.

## Conceptual text-to-speech pipeline
Text → text normalization and linguistic representation → acoustic/token generation → waveform/vocoder stage (architecture-dependent) → audio output.

## Practical labs
- Read a WAV file and calculate duration from sample count and sample rate.
- Plot a waveform and spectrogram.
- Compare audio after resampling.
- Run an ASR model and inspect transcript errors.
- Generate speech from text and listen for pronunciation and timing issues.

## Project connection
For a voice assistant, document each actual stage separately: microphone capture, audio transport, speech recognition, text/LLM processing, response generation, TTS and playback. Add exact source/test evidence before marking any stage implemented.
