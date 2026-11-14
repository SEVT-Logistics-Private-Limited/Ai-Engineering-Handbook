# 24. Semi-Supervised Learning

> Semi-supervised learning uses a small amount of labelled data together with a large amount of unlabelled data.

## Introduction

[Supervised Learning](22-supervised-learning.md) needs a known output (label) for every example. [Unsupervised Learning](23-unsupervised-learning.md) uses no labels at all. Semi-supervised learning sits **between the two**.

## What is it?

**Semi-Supervised Learning** is a type of ML that uses a **combination of**:

- a **small amount of labelled data** (inputs with known outputs), and
- a **large amount of unlabelled data** (inputs only).

It **learns patterns from the labelled data** and uses them to make sense of the unlabelled data, so the model ends up trained on far more data than was labelled by hand.

### Example: 1000 emails

Suppose you have 1000 emails:

| Emails | Labelled? |
|---|---|
| 100 | **Labelled** (marked spam / not spam) |
| 900 | **Unlabelled** |

The model learns patterns from the 100 labelled emails and **applies them to the 900 unlabelled emails**.

## Why is it needed?

- Labelling data by hand is slow and expensive.
- Unlabelled data is cheap and easy to collect in large amounts.
- A small labelled set alone is often not enough to train a good model. Adding the unlabelled data improves it without labelling everything.

## How does it work?

1. Train a model on the small labelled set.
2. Use that model to predict labels for the unlabelled data.
3. Keep the predictions the model is confident about and treat them as labels.
4. Retrain on the labelled data plus these newly labelled examples, and repeat.

## Where it fits

| | Supervised | Semi-supervised | Unsupervised |
|---|---|---|---|
| Labelled data | All of it | A small part | None |
| Unlabelled data | None | Most of it | All of it |
| Example | 1000 labelled emails | 100 labelled + 900 unlabelled emails | 1000 unlabelled emails |

## Flow diagram

```text
Small labelled data (100 emails)        Large unlabelled data (900 emails)
        ↓                                          ↓
Model learns patterns  ───── applies them to ─────→ Predicted labels
        ↓
Retrain on labelled + newly labelled data
        ↓
Better model
```

## Real-world use cases

- Spam detection with only a few emails marked by users
- Medical image analysis, where only experts can label scans
- Speech recognition, where transcribing audio by hand is costly
- Sorting large collections of documents or web pages

## In our project

**Not used yet.** We don't train a model on a mix of labelled and unlabelled data.

---

**Previous:** [← Unsupervised Learning](23-unsupervised-learning.md) · [Home](../README.md) · **Next:** [Reinforcement Learning →](25-reinforcement-learning.md)
