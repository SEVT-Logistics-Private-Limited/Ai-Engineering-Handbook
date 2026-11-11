# 8. FPS (Frames Per Second)

> FPS is how many frames are displayed in one second.

## Introduction

Why does one video look smooth and another look choppy? The answer is **FPS**: how many frames are shown every second.

## What is it?

**FPS (frames per second)** is **how many frames are displayed in one second**.

| FPS | Meaning |
|---|---|
| 1 FPS | 1 frame per second |
| 30 FPS | 30 frames per second |
| 60 FPS | 60 frames per second |
| 120 FPS | 120 frames per second |

## Why is it needed?

- Higher FPS = smoother motion.
- But higher FPS also means more frames, more pixels and more numbers to process and store.

## How does it work?

If a video has **30 FPS**, the screen shows **30 separate images every second**. Our eyes blend them together, so it looks like continuous movement.

How much data that is for a 1920 × 1080 video at 30 FPS:
- 1 frame ≈ 6.2 million numbers (pixels × 3 RGB)
- 1 second = 30 frames ≈ **186 million numbers**

That's why video needs a [GPU](02-gpu.md).

## Flow diagram

```text
1 second of a 30 FPS video:

Frame 1 → Frame 2 → Frame 3 → ... → Frame 30
└──────────────── 1 second ────────────────┘
```

## Real-world use cases

- Movies (often 24 FPS)
- Standard video (30 FPS)
- Gaming and smooth video (60–120 FPS)
- Slow-motion video (recorded at high FPS)

## Key takeaways

- FPS = frames displayed per second.
- 30 FPS = 30 images every second.
- Higher FPS = smoother, but more data.

---

**Previous:** [← Frame](07-frame.md) · [Home](../README.md) · **Next:** [NLP →](09-nlp.md)
