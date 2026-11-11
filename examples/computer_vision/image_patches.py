"""How a Vision Transformer (the encoder inside most VLMs) turns an image into tokens:
resize -> normalize -> split into patches -> flatten -> linear projection -> patch embeddings.

The projection matrix is random here; in a real model it is learned.

Run:
    python examples/computer_vision/image_patches.py
"""

import numpy as np


def patchify(img: np.ndarray, patch: int) -> np.ndarray:
    """(H, W, C) -> (num_patches, patch*patch*C). H and W must be divisible by `patch`."""
    h, w, c = img.shape
    if h % patch or w % patch:
        raise ValueError(f"image {h}x{w} is not divisible into {patch}x{patch} patches")
    grid = img.reshape(h // patch, patch, w // patch, patch, c)
    return grid.transpose(0, 2, 1, 3, 4).reshape(-1, patch * patch * c)


def main() -> dict:
    rng = np.random.default_rng(0)
    img = rng.integers(0, 256, size=(224, 224, 3), dtype=np.uint8)  # stand-in for a resized photo
    x = img.astype(np.float32) / 255.0                               # normalize pixel values

    patches = patchify(x, patch=16)
    d_model = 768
    projection = rng.normal(0, 0.02, size=(patches.shape[1], d_model))
    embeddings = patches @ projection

    print(f"image:            {img.shape}  (height, width, channels)")
    print(f"patches:          {patches.shape}  (14 x 14 = 196 patches, each 16*16*3 = 768 numbers)")
    print(f"patch embeddings: {embeddings.shape}  (one vector per patch, like one vector per text token)")
    return {"patches": patches.shape, "embeddings": embeddings.shape}


if __name__ == "__main__":
    main()
