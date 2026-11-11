# 7. Frame

> A frame is a single individual image inside a video.

## Introduction

When you pause a video, the picture you see on screen is one **frame**.

## What is it?

A **frame** is a **single individual image inside a video**.

| Image | Frame |
|---|---|
| One photograph on its own | One image that is part of a video |

## Why is it needed?

Frames are the building blocks of video. AI models that understand video usually look at selected frames, because each frame is just an image they can process.

## How does it work?

- A video is a sequence of frames.
- Each frame is an image, so it's made of pixels, and each pixel has RGB values.
- Frames are shown one after another at a fixed speed, measured in [FPS](08-fps.md).

## Flow diagram

```text
Video  =  Frame 1 → Frame 2 → Frame 3 → Frame 4 → ...
              ↓
        each frame is an image
              ↓
         pixels → RGB values
```

## Real-world use cases

- Taking a screenshot (a single frame) from a video
- Thumbnails on YouTube
- AI video analysis: picking a few frames per second to analyse

## In our project

**Not used yet.** Our project works with voice and text only, so it doesn't process video frames yet.

## Key takeaways

- A frame = one image inside a video.
- Image = 1 photograph, frame = one image inside a video.

---

**Previous:** [← Video](06-video.md) · [Home](../README.md) · **Next:** [FPS →](08-fps.md)
