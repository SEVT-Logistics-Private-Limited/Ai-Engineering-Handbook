# 3. Binary

> Binary is the number system computers use. It has only two digits: 0 and 1.

## Introduction

We said a computer only understands numbers. But inside the hardware, it actually understands only **two** values: ON and OFF. That's binary.

## What is it?

**Binary** is a number system that uses only two digits: **0 and 1**. "Binary" means **two**.

| Digit | Meaning |
|---|---|
| 0 | OFF / low voltage |
| 1 | ON / high voltage |

A single binary digit is called a **bit**.

## Why is it needed?

Electronic circuits can easily tell two states apart: current flowing or not flowing. So every number, letter, pixel and sound is stored as a pattern of 0s and 1s.

## How does it work?

### Counting in binary

| Binary | Number |
|---|---|
| 0000 | 0 |
| 0001 | 1 |
| 0010 | 2 |
| 0011 | 3 |
| 0100 | 4 |

### Bits

| Example | Size |
|---|---|
| `1` | 1 bit |
| `1010` | 4 bits |
| `11001010` | 8 bits |

### Units

| Unit | Size |
|---|---|
| 1 Bit | a single 0 or 1 |
| 1 Byte | 8 bits |
| 1 KB | 1024 bytes |
| 1 MB | 1024 KB |
| 1 GB | 1024 MB |
| 1 TB | 1024 GB |

## Flow diagram

```text
Image / Text / Audio
        ↓
     Numbers
        ↓
Binary (0s and 1s)
        ↓
Electrical signals (OFF / ON)
```

```text
1 bit  →  8 bits = 1 Byte  →  1024 Bytes = 1 KB  →  1024 KB = 1 MB  →  1024 MB = 1 GB  →  1024 GB = 1 TB
```

## Real-world use cases

- Storing files: every photo, video and document on your phone is binary
- Memory and storage sizes (GB, TB)
- Internet data transfer (bits per second)

## In our project

**Used, in two places.**

**1. Sending audio over the API.** Audio is binary data (bytes), but the API sends JSON, which is text. So audio bytes are converted to **base64** text, and back again. This happens when the browser can't do speech recognition itself and uploads the recording instead:

```text
Browser records voice (binary bytes)
        ↓
Encode to base64 text → sent in JSON as "audio_base64"
        ↓
Server decodes base64 → original audio bytes → speech to text
```

The spoken answer comes back the same way: audio bytes → base64 → browser → played.

**2. Saving model files smaller.** Big models were saved as **bf16 (16 bits per number)** instead of 32 bits, so the 3B model's checkpoint is about **6 GB** instead of 12 GB. The compression experiments go further: weights become -1, 0 or +1 and are packed **4 numbers into 1 byte** (2 bits each).

Code: [`voice-assistant/api.py`](https://github.com/SEVT-Logistics-Private-Limited/tiny-llm-jetson/blob/main/voice-assistant/api.py) (`base64.b64decode`, `base64.b64encode`), [`tiny_llm_3b.py`](https://github.com/SEVT-Logistics-Private-Limited/tiny-llm-jetson/blob/main/tiny_llm_3b.py) (bf16 save)

## Key takeaways

- Binary uses only 0 and 1. 0 = OFF, 1 = ON.
- One binary digit = 1 bit, and 8 bits = 1 byte.
- 1 KB = 1024 bytes, 1 MB = 1024 KB, 1 GB = 1024 MB, 1 TB = 1024 GB.

---

**Previous:** [← GPU](02-gpu.md) · [Home](../README.md) · **Next:** [Image →](04-image.md)
