"""Regenerate every figure in assets/images from the runnable examples.

All figures are computed from the code in examples/, so they always match it.

Run from the repository root:
    python scripts/generate_figures.py
"""

import contextlib
import importlib.util
import io
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "images"
ACCENT, MUTED = "#2563eb", "#64748b"

plt.rcParams.update({
    "figure.dpi": 150, "savefig.bbox": "tight", "savefig.facecolor": "white",
    "font.size": 10, "axes.spines.top": False, "axes.spines.right": False,
    "axes.titleweight": "bold", "axes.titlesize": 11,
})


def load(relative_path: str):
    path = ROOT / "examples" / relative_path
    spec = importlib.util.spec_from_file_location(path.stem, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def quiet(fn, *args, **kwargs):
    with contextlib.redirect_stdout(io.StringIO()):
        return fn(*args, **kwargs)


def scene(size: int = 224) -> np.ndarray:
    """A simple synthetic landscape: blue sky gradient, yellow sun, green ground, red house."""
    y, x = np.mgrid[0:size, 0:size] / size
    img = np.zeros((size, size, 3))
    img[..., 0] = 0.35 + 0.3 * y
    img[..., 1] = 0.6 + 0.25 * y
    img[..., 2] = 1.0 - 0.2 * y
    sun = (x - 0.75) ** 2 + (y - 0.22) ** 2 < 0.012
    img[sun] = [1.0, 0.85, 0.1]
    ground = y > 0.68
    img[ground] = np.stack([0.2 + 0.1 * x[ground], 0.6 - 0.15 * y[ground], 0.2 * np.ones(ground.sum())], -1)
    house = (x > 0.2) & (x < 0.42) & (y > 0.5) & (y < 0.72)
    img[house] = [0.8, 0.15, 0.15]
    return (img.clip(0, 1) * 255).astype(np.uint8)


def save(fig, name: str) -> None:
    fig.savefig(OUT / name)
    plt.close(fig)
    print(f"wrote assets/images/{name}")


def training_loss() -> None:
    m = load("ai_fundamentals/training_loop.py")
    x, y = m.make_dataset()
    history = quiet(m.train, x, y)["history"]
    fig, ax = plt.subplots(figsize=(6, 3))
    ax.plot(range(1, len(history) + 1), history, marker="o", color=ACCENT)
    ax.set(title="Training loss per epoch (examples/ai_fundamentals/training_loop.py)",
           xlabel="Epoch", ylabel="Mean squared error", yscale="log")
    ax.grid(alpha=0.3)
    save(fig, "training-loss.png")


def temperature_effect() -> None:
    m = load("language_models/text_generation.py")
    model = m.BigramModel(m.CORPUS)
    logits = model.logits[model.stoi["t"]]
    labels = [repr(c) for c in model.chars]
    fig, axes = plt.subplots(1, 3, figsize=(10, 3), sharey=True)
    for ax, t in zip(axes, (0.3, 1.0, 2.0)):
        p = m.apply_temperature(logits, t)
        ax.bar(labels, p, color=ACCENT if t == 0.3 else MUTED if t == 2.0 else "#0ea5e9")
        ax.set_title(f"T = {t}")
        ax.tick_params(axis="x", labelsize=7, rotation=90)
    axes[0].set_ylabel("Probability of next character")
    fig.suptitle("Next-character probabilities after 't' at different temperatures", fontweight="bold", y=1.06)
    save(fig, "temperature-effect.png")


def causal_attention() -> None:
    m = load("language_models/self_attention.py")
    weights = quiet(m.main)["weights"][0]
    tokens = ["I", "love", "Artificial", "Intelligence"]
    fig, ax = plt.subplots(figsize=(4.8, 4))
    im = ax.imshow(weights, cmap="Blues", vmin=0, vmax=1)
    ax.set_xticks(range(4), tokens, rotation=30)
    ax.set_yticks(range(4), tokens)
    ax.set(xlabel="Key (token being looked at)", ylabel="Query (token doing the looking)",
           title="Causal self-attention weights (1 head)")
    for i in range(4):
        for j in range(4):
            ax.text(j, i, f"{weights[i, j]:.2f}", ha="center", va="center",
                    color="white" if weights[i, j] > 0.5 else "black", fontsize=9)
    ax.spines[:].set_visible(False)
    fig.colorbar(im, ax=ax, fraction=0.046)
    fig.text(0.5, -0.18, "Random (untrained) weights: the values show the mechanics, not meaning.",
             ha="center", fontsize=8, color=MUTED)
    save(fig, "causal-attention.png")


def embedding_similarity() -> None:
    m = load("language_models/embeddings_similarity.py")
    words = list(m.EMBEDDINGS)
    sim = np.array([[m.cosine_similarity(m.EMBEDDINGS[a], m.EMBEDDINGS[b]) for b in words] for a in words])
    fig, ax = plt.subplots(figsize=(5, 4.2))
    im = ax.imshow(sim, cmap="Blues", vmin=0, vmax=1)
    ax.set_xticks(range(len(words)), words, rotation=45, ha="right")
    ax.set_yticks(range(len(words)), words)
    for i in range(len(words)):
        for j in range(len(words)):
            ax.text(j, i, f"{sim[i, j]:.2f}", ha="center", va="center", fontsize=7,
                    color="white" if sim[i, j] > 0.6 else "black")
    ax.set_title("Cosine similarity between embeddings")
    ax.spines[:].set_visible(False)
    fig.colorbar(im, ax=ax, fraction=0.046)
    save(fig, "embedding-similarity.png")


def rgb_channels() -> None:
    img = scene()
    fig, axes = plt.subplots(1, 4, figsize=(10, 2.8))
    axes[0].imshow(img)
    axes[0].set_title("RGB image")
    for ax, (name, idx, cmap) in zip(axes[1:], [("Red", 0, "Reds"), ("Green", 1, "Greens"), ("Blue", 2, "Blues")]):
        ax.imshow(img[..., idx], cmap=cmap, vmin=0, vmax=255)
        ax.set_title(f"{name} channel (0-255)")
    for ax in axes:
        ax.axis("off")
    fig.suptitle("Every pixel stores three numbers: red, green and blue", fontweight="bold", y=1.04)
    save(fig, "rgb-channels.png")


def resolution() -> None:
    m = load("computer_vision/image_as_array.py")
    img = scene()
    fig, axes = plt.subplots(1, 3, figsize=(9, 3.2))
    for ax, size in zip(axes, (16, 48, 224)):
        small = m.resize_nearest(img, size, size)
        ax.imshow(small, interpolation="nearest")
        ax.set_title(f"{size} x {size} = {size * size:,} pixels")
        ax.axis("off")
    fig.suptitle("Same scene at three resolutions: more pixels keep finer detail", fontweight="bold", y=1.03)
    save(fig, "resolution.png")


def image_patches() -> None:
    img = scene()
    fig, ax = plt.subplots(figsize=(4.2, 4.2))
    ax.imshow(img)
    for k in range(0, 225, 16):
        ax.axhline(k - 0.5, color="white", lw=0.8)
        ax.axvline(k - 0.5, color="white", lw=0.8)
    ax.set_title("224 x 224 image split into 16 x 16 patches\n14 x 14 = 196 patches (196 'visual tokens')")
    ax.axis("off")
    save(fig, "image-patches.png")


def video_frames() -> None:
    m = load("computer_vision/video_as_frames.py")
    video = m.make_video(n_frames=30)
    picks = [0, 6, 12, 18, 24, 29]
    fig, axes = plt.subplots(1, len(picks), figsize=(11, 1.9))
    for ax, t in zip(axes, picks):
        ax.imshow(video[t])
        ax.set_title(f"frame {t}\nt = {t / 30:.2f} s", fontsize=8)
        ax.axis("off")
    fig.suptitle("A 30 FPS video is just images shown one after another", fontweight="bold", y=1.12)
    save(fig, "video-frames.png")


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for fn in (training_loss, temperature_effect, causal_attention, embedding_similarity,
               rgb_channels, resolution, image_patches, video_frames):
        fn()


if __name__ == "__main__":
    main()
