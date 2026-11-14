# 18. Unsupervised Learning

> In unsupervised learning, the training data has **no** known target outputs. The algorithm tries to discover patterns on its own.

## Introduction

In [Supervised Learning](17-supervised-learning.md), every example comes with the correct answer. Often, though, we only have raw data and no answers. Unsupervised learning is for that case.

## What is it?

**Unsupervised Learning (USL)** is a type of ML where **the training data doesn't have known target outputs**. Nobody tells the model what the right answer is; the **algorithm tries to discover patterns** in the data by itself.

### Example: customer data

| Customer | Income |
|---|---|
| A | ₹50K |
| B | ₹60K |
| C | ₹5 L |

There is no "output" column here, only inputs. An unsupervised algorithm can still notice that A and B are similar, while C is very different, and group them:

```text
Group 1: A, B   (similar income)
Group 2: C      (much higher income)
```

A business could then target each group differently, without anyone defining the groups in advance.

## Why is it needed?

- Labelling data (writing the correct output for every example) is slow and expensive.
- Most real-world data has no labels at all.
- Sometimes we don't know what we are looking for yet, and want the data to show us its structure.

## How does it work?

1. Collect data with inputs only (no target outputs).
2. The algorithm measures how similar or different the data points are.
3. It finds structure, such as groups of similar items or unusual items that don't fit.
4. People look at the discovered patterns and decide what they mean.

Common tasks:

| Task | What it does | Example |
|---|---|---|
| **Clustering** | Groups similar items together | Customer segments by income and spending |
| **Anomaly detection** | Finds items that don't fit the pattern | An unusual transaction that may be fraud |

## Supervised vs unsupervised

| | Supervised | Unsupervised |
|---|---|---|
| Training data | Inputs **+ known target outputs** | Inputs **only** |
| Goal | Predict the output for new inputs | Discover patterns and groups |
| Example | House size → price | Group customers by income |

## Flow diagram

```text
Training data: Inputs only (no known outputs)
        ↓
Algorithm discovers patterns
        ↓
Groups / structure (e.g. customer segments)
```

## Real-world use cases

- Customer segmentation for marketing
- Grouping similar news articles or products
- Detecting unusual transactions
- Recommendations based on similar users

## In our project

**Not used yet.** We don't group or cluster data without labels.

A related idea appears in our [RAG](13-rag.md) search: embeddings place text with similar meaning close together, and we pick the closest manual section. But we use a pretrained embedding model and don't run any clustering ourselves.

---

**Previous:** [← Supervised Learning](17-supervised-learning.md) · [Home](../README.md) · **Next:** [Semi-Supervised Learning →](19-semi-supervised-learning.md)
