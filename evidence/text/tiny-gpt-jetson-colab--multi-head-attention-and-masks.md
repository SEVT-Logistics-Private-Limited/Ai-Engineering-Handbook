---
project: tiny-gpt-jetson-colab
concept_id: TXT-180
status: Implemented
---

# Tiny GPT — Jetson + Colab — Multi-Head Attention and Attention Masks

## Linked concept
[TXT-180 — Multi-Head Attention and Attention Masks](../../concepts/text/180-multi-head-attention-and-masks.md)

## Problem
TODO: supply the original requirement and why this concept was needed.

## Architecture
The Block uses torch.nn.MultiheadAttention with n_head heads and creates a boolean upper-triangular mask using torch.triu(..., diagonal=1). This prevents the causal language model from attending to future sequence positions.

```mermaid
flowchart TD
 A[Text corpus] --> B[Model source component]
 B --> C[Concept-specific processing]
 C --> D[Training output or generated sequence]
```

## My exact contribution
TODO: supply the work you personally designed, coded, configured, tested, debugged or operated. Separate personal contribution from team work.

## Stack
Confirmed in inspected source: Python and PyTorch. TODO: supply exact versions, runtime and hardware details for this specific concept.

## Decisions & tradeoffs
TODO: supply your rationale, alternatives and tradeoffs. The source proves code structure, not why you personally selected it.

## Results/metrics
TODO: supply measured results, measurement method, dataset/sample size, environment, units and date. If none exist, state that clearly.

## What failed
TODO: supply failures, limitations and root causes. Do not invent failures.

## What I'd change
TODO: supply concrete improvements and why.

## Evidence links
- [Source: tiny_llm.py](https://github.com/SEVT-Logistics-Private-Limited/tiny-llm-jetson/blob/main/tiny_llm.py)
- Tests, commands and commits: TODO: supply.

## Link back
[Return to TXT-180 — Multi-Head Attention and Attention Masks](../../concepts/text/180-multi-head-attention-and-masks.md)