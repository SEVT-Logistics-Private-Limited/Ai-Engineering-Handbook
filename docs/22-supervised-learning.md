# 22. Supervised Learning

> In supervised learning, the training data contains inputs **and** their known target outputs. The model learns to map one to the other.

## Introduction

[ML](16-ml.md) is about learning patterns from data. The first question to ask about any ML problem is: **does the training data already have the correct answers?** If yes, it is supervised learning.

## What is it?

**Supervised Learning (SL)** is a type of ML where **the training data contains inputs and known target outputs** (also called labels).

The word "supervised" comes from the answers acting like a teacher: for every example, the model is shown what the correct output should be.

Examples: predicting house prices, spam detection.

### Example: house prices

| Input (house size) | Output (price) |
|---|---|
| 1000 sq ft | ₹50 L |
| 1500 sq ft | ₹75 L |
| 2000 sq ft | ₹1 Cr |
| ↑ input we have | ↑ **known target output** |

(L = lakh, Cr = crore.)

The model learns the pattern "bigger house → higher price" from these pairs, then predicts the price of a house it has never seen.

## Why is it needed?

Many real problems have past examples with known answers: past house sales with their prices, emails already marked as spam or not spam. Supervised learning turns those examples into a model that predicts the answer for new data.

## How does it work?

1. Collect examples where each input has its correct output.
2. The model makes a prediction for each input.
3. Compare the prediction with the known output and measure the error.
4. Adjust the model to reduce the error, and repeat.
5. Use the trained model to predict outputs for new inputs.

### Two major problem types

| Type | Predicts | Example input → output |
|---|---|---|
| **Classification** | A **category** | Email → spam / not spam; medical test → disease positive / negative |
| **Regression** | A **numeric value** | House size 1000 sq ft → price ₹50 L |

Quick way to tell them apart: if the answer is a **label from a fixed list**, it is classification. If the answer is a **number on a scale**, it is regression.

## Flow diagram

```text
Training data: Input + Known target output
        ↓
Model predicts → compare with known output → adjust
        ↓
Trained model
        ↓
New input → Prediction
```

```text
Supervised Learning
 ├── Classification   (predicts a category: spam / not spam)
 └── Regression       (predicts a number: house price)
```

## Real-world use cases

- Spam detection (classification)
- Disease detection from test results (classification)
- House price prediction (regression)
- Sales or demand forecasting (regression)

## In our project

**Not used directly.** We don't train a classic classifier or regression model.

The closest idea is how our Telugu language models learn: they predict the **next character** in real Telugu text, and the actual next character is the known target. Because those targets come from the text itself rather than from people labelling data, this is called **self-supervised learning**, a close relative of supervised learning. See [DL](17-dl.md).

---

**Previous:** [← ML](16-ml.md) · [Home](../README.md) · **Next:** [Unsupervised Learning →](23-unsupervised-learning.md)
