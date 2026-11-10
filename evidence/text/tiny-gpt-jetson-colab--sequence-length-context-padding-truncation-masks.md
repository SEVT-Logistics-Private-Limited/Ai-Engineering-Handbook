---
project: tiny-gpt-jetson-colab
concept_id: TXT-090
status: Implemented
---

# Tiny GPT — Jetson + Colab — Sequence Length, Context Windows, Padding, Truncation and Masks

## Linked concept
[TXT-090 — Sequence Length, Context Windows, Padding, Truncation and Masks](../../concepts/text/090-sequence-length-context-padding-truncation-masks.md)

## Problem
TODO: supply the real requirement and why this concept was used. Do not infer missing context.

## Architecture
The model defines block_size and get_batch() creates fixed-length input and target windows shifted by one character for next-character prediction. The Telugu model configuration sets block_size to 128. The inspected scripts do not show a general variable-length padded inference API.

```mermaid
flowchart TD
 A[Project data] --> B[Verified source component]
 B --> C[Concept-specific operation]
 C --> D[Observed output]
```

## My exact contribution
TODO: supply what you personally designed, coded, configured, tested, debugged or operated. Separate your work from team work.

## Stack
Confirmed in inspected source: Python and PyTorch. TODO: supply exact versions, environment and hardware for this concept.

## Decisions & tradeoffs
TODO: supply actual choices, alternatives, rationale and tradeoffs.

## Results/metrics
TODO: supply measured results, method, dataset/sample size, environment, units and date. If none exist, say so.

## What failed
TODO: supply failures, limitations and root causes. Do not invent failures.

## What I'd change
TODO: supply concrete improvements and why.

## Evidence links
- [Source file](https://github.com/SEVT-Logistics-Private-Limited/tiny-llm-jetson/blob/main/tiny_llm.py)
- Test commands and reproducible results: TODO: supply.

## Link back
[Return to TXT-090 — Sequence Length, Context Windows, Padding, Truncation and Masks](../../concepts/text/090-sequence-length-context-padding-truncation-masks.md)