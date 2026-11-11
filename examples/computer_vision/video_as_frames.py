"""Video is a stack of frames: frames, FPS, raw size, and frame sampling for AI models.

Run:
    python examples/computer_vision/video_as_frames.py
"""

import numpy as np


def make_video(n_frames: int = 30, height: int = 32, width: int = 64) -> np.ndarray:
    """A synthetic clip: a white square moving left to right. Shape: (frames, height, width, 3)."""
    video = np.zeros((n_frames, height, width, 3), dtype=np.uint8)
    size = 8
    for t in range(n_frames):
        x = int(t * (width - size) / max(n_frames - 1, 1))
        video[t, height // 2 - size // 2: height // 2 + size // 2, x:x + size] = 255
    return video


def raw_size_bytes(width: int, height: int, fps: int, seconds: float) -> int:
    """Uncompressed size: every pixel of every frame stores 3 bytes (R, G, B)."""
    return int(width * height * 3 * fps * seconds)


def sample_frames(video: np.ndarray, fps: int, target_fps: float) -> np.ndarray:
    """Keep `target_fps` frames per second, as video-AI models usually do."""
    step = max(int(round(fps / target_fps)), 1)
    return video[::step]


def main() -> dict:
    fps = 30
    video = make_video(n_frames=fps)  # 1 second of video
    print(f"video shape (frames, height, width, channels): {video.shape}")
    print(f"duration: {video.shape[0] / fps:.1f} s at {fps} FPS")
    print(f"frame 0 is just an image of shape {video[0].shape}")

    sampled = sample_frames(video, fps, target_fps=2)
    print(f"sampling at 2 FPS keeps {len(sampled)} of {len(video)} frames")

    per_min = raw_size_bytes(1920, 1080, 30, 60)
    print(f"\n1 minute of raw 1080p30 video = {per_min:,} numbers = {per_min / 1024 ** 3:.1f} GiB uncompressed")
    print("Codecs like H.264 store only what changes between frames, shrinking this by 100x or more.")
    return {"shape": video.shape, "sampled": len(sampled), "per_min": per_min}


if __name__ == "__main__":
    main()
