"""Images are arrays of numbers: pixels, RGB channels, resolution and basic processing.

Run:
    python examples/computer_vision/image_as_array.py
"""

import numpy as np

COLOURS = {
    "red": (255, 0, 0), "green": (0, 255, 0), "blue": (0, 0, 255),
    "white": (255, 255, 255), "black": (0, 0, 0),
    "yellow": (255, 255, 0), "magenta": (255, 0, 255),
}


def make_image() -> np.ndarray:
    """A 2x4 image (height 2, width 4) built pixel by pixel. Shape: (height, width, 3)."""
    rows = [["red", "green", "blue", "white"],
            ["black", "yellow", "magenta", "white"]]
    return np.array([[COLOURS[c] for c in row] for row in rows], dtype=np.uint8)


def to_grayscale(img: np.ndarray) -> np.ndarray:
    """ITU-R BT.601 luma: the eye is most sensitive to green, least to blue."""
    weights = np.array([0.299, 0.587, 0.114])
    return (img[..., :3].astype(np.float64) @ weights).round().astype(np.uint8)


def resize_nearest(img: np.ndarray, new_h: int, new_w: int) -> np.ndarray:
    rows = (np.arange(new_h) * img.shape[0] / new_h).astype(int)
    cols = (np.arange(new_w) * img.shape[1] / new_w).astype(int)
    return img[rows][:, cols]


def normalize(img: np.ndarray) -> np.ndarray:
    """Scale 0-255 integers to 0.0-1.0 floats, the usual first step before a neural network."""
    return img.astype(np.float32) / 255.0


def main() -> dict:
    img = make_image()
    h, w, c = img.shape
    print(f"image shape (height, width, channels): {img.shape}, dtype={img.dtype}")
    print(f"top-left pixel (red)   = {tuple(int(v) for v in img[0, 0])}")
    print(f"bottom-left pixel (black) = {tuple(int(v) for v in img[1, 0])}")
    print(f"red channel only:\n{img[..., 0]}")

    gray = to_grayscale(img)
    print(f"\ngrayscale (1 number per pixel):\n{gray}")

    big = resize_nearest(img, 4, 8)
    print(f"\nresized {img.shape[:2]} -> {big.shape[:2]} with nearest-neighbour")
    print(f"normalized value range: {normalize(img).min():.1f} to {normalize(img).max():.1f}")

    full_hd = 1920 * 1080
    print(f"\n1920x1080 = {full_hd:,} pixels = {full_hd / 1e6:.1f} MP = {full_hd * 3:,} numbers (RGB)")
    return {"shape": img.shape, "gray": gray, "pixels_full_hd": full_hd}


if __name__ == "__main__":
    main()
