"""A complete training loop from scratch: epochs, batches, forward pass, loss,
gradients and optimizer updates.

The model learns the line y = 3x + 2 from 1,000 noisy samples.

Run:
    python examples/ai_fundamentals/training_loop.py
"""

import numpy as np


def make_dataset(n_samples: int = 1000, seed: int = 0) -> tuple[np.ndarray, np.ndarray]:
    rng = np.random.default_rng(seed)
    x = rng.uniform(-1, 1, n_samples)
    y = 3 * x + 2 + rng.normal(0, 0.1, n_samples)  # true weight 3, true bias 2, plus noise
    return x, y


def train(x: np.ndarray, y: np.ndarray, epochs: int = 20, batch_size: int = 100,
          lr: float = 0.1, seed: int = 0) -> dict:
    rng = np.random.default_rng(seed)
    w, b = 0.0, 0.0  # parameters start at zero
    steps_per_epoch = int(np.ceil(len(x) / batch_size))
    history = []

    for epoch in range(1, epochs + 1):
        order = rng.permutation(len(x))  # shuffle every epoch
        for step in range(steps_per_epoch):
            idx = order[step * batch_size:(step + 1) * batch_size]
            xb, yb = x[idx], y[idx]

            pred = w * xb + b                 # 1. forward propagation -> prediction
            error = pred - yb
            loss = np.mean(error ** 2)        # 2. loss function (mean squared error)

            grad_w = 2 * np.mean(error * xb)  # 3. backpropagation -> gradients
            grad_b = 2 * np.mean(error)

            w -= lr * grad_w                  # 4. optimizer (gradient descent) updates weights and bias
            b -= lr * grad_b

        epoch_loss = float(np.mean((w * x + b - y) ** 2))
        history.append(epoch_loss)
        if epoch in (1, 2, 5, 10, epochs):
            print(f"epoch {epoch:>2} | loss {epoch_loss:.4f} | w={w:.3f} b={b:.3f}")

    return {"w": w, "b": b, "history": history, "steps_per_epoch": steps_per_epoch}


def main() -> dict:
    x, y = make_dataset()
    print(f"dataset: {len(x)} samples, batch size 100 -> {int(np.ceil(len(x) / 100))} steps per epoch\n")
    result = train(x, y)
    print(f"\nlearned: y = {result['w']:.2f}x + {result['b']:.2f}   (true: y = 3x + 2)")
    return result


if __name__ == "__main__":
    main()
