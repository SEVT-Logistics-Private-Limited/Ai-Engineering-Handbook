# AI Engineering Handbook

**From digital-data fundamentals to production AI engineering.**

This repository is a structured, practical knowledge base for understanding how AI systems work from first principles and how those concepts are implemented in real applications. It connects theory, data flow, code, engineering decisions, project evidence, and interview preparation.

## Mission

Build a reliable reference that answers five questions for every technology:
1. What is it?
2. Why is it needed?
3. How does it work internally?
4. How can it be implemented and tested?
5. Where have I used it in a real project, and what evidence supports that claim?

## Learning map

| Stage | Area | Coverage |
|---|---|---|
| 00 | Fundamentals | Data, bits, bytes, computing, AI, ML, deep learning |
| 01 | Data modalities | Text, images, audio, video, structured and multimodal data |
| 02 | Data processing | Encoding, preprocessing, tokenization, embeddings, feature extraction |
| 03–04 | ML and deep learning | Learning paradigms, neural networks, optimization, CNNs, RNNs, Transformers |
| 05–09 | Modality-specific AI | NLP/LLMs, computer vision, audio AI, video AI, multimodal AI/VLMs |
| 10 | Generative AI | Generative models, diffusion, prompting |
| 11–12 | AI application patterns | RAG, vector search, agents, tools and workflows |
| 13 | AI engineering | Python, APIs, FastAPI, databases, testing, deployment, monitoring, security |
| 14 | Projects | Architecture, implementation, evidence, testing, challenges and outcomes |
| 15 | Interview preparation | Conceptual, coding, system-design and project-based questions |

See [the detailed roadmap](ROADMAP.md) and [the learning map](docs/LEARNING-MAP.md).

## Repository principles

- **Start at zero:** explain prerequisites and terminology before advanced concepts.
- **Explain the mechanism:** include step-by-step flows, shapes, examples, diagrams and equations where useful.
- **Connect concepts to implementation:** include runnable examples and code walkthroughs when appropriate.
- **Separate knowledge from evidence:** distinguish a technology being studied from one actually implemented in a project.
- **Be precise about project claims:** cite the exact repository, file, function, configuration or test that proves an implementation.
- **Keep it maintainable:** use the shared [topic template](resources/templates/TOPIC-TEMPLATE.md), progress tracker and glossary.

## Topic documentation format

Every topic should cover: definition; prerequisites; problem solved; internal working; architecture/data flow; terminology; worked example; implementation; testing and trade-offs; real-world uses; project connection and evidence; interview questions; references.

## Project portfolio

Project pages are indexed in [the project portfolio](14-projects/README.md). Initial areas to document include a Tiny LLM / GPT-style PyTorch implementation, a RAG application, VLM experiments, a Telugu voice assistant, and an EV AI application. Details are intentionally marked **to verify** until source code, configuration or test evidence has been inspected.

## Start here

1. Read [00 — Fundamentals](00-fundamentals/README.md).
2. Continue with [01 — Data Fundamentals](01-data-fundamentals/README.md).
3. Study the modality processing pipelines in [02 — Data Processing](02-data-processing/README.md).
4. Follow the [complete roadmap](ROADMAP.md).
5. Track progress in [LEARNING-PROGRESS.md](LEARNING-PROGRESS.md).

## Status and contribution

This is a continuously evolving personal engineering handbook. Prefer small, focused topic pages. Add source links and dates to external references. Do not publish credentials, private customer data, proprietary source code, or confidential project details.

**Learn the fundamentals. Understand the architecture. Build the technology. Document the evidence.**
