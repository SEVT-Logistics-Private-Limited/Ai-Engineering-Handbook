# 20. Prompt Engineering

> Prompt engineering is the skill of writing the input (prompt) to an LLM so that it gives the answer you want.

## Introduction

The same LLM can give a vague answer or a precise one depending on **how you ask**. Prompt engineering is about asking well.

## What is it?

**Prompt engineering** means designing the prompt (the instructions and examples) you give an LLM. The main techniques:

| Technique | Meaning | Examples given |
|---|---|---|
| **Zero-shot prompting** | Asking the model to perform a task without providing an example | None |
| **One-shot prompting** | Providing one example before asking the model to perform the task | One |
| **Few-shot prompting** | Providing multiple examples | Several |
| **Chain of thought** | Step-by-step reasoning used to solve a complex problem | – |
| **Role prompting** | Telling the model what role or perspective to adopt | – |

## Why is it needed?

- Better prompts give better, more accurate answers.
- It costs nothing: no training needed.
- Good prompts help reduce [hallucination](21-hallucination.md).

## How does it work?

- **Zero-shot:** "Classify this review as Positive or Negative: *The service was quick.*"
- **One-shot:** give one example first ("*I love this phone* → Positive"), then ask.
- **Few-shot:** give several examples first, then ask.
- **Chain of thought:** "Solve this step by step."
- **Role prompting:** "You are an experienced AWS cloud engineer. Explain AWS IAM."

## Flow diagram

```text
Zero-shot:  Question ─────────────────────────→ LLM → Answer
One-shot:   1 example + Question ─────────────→ LLM → Answer
Few-shot:   Many examples + Question ─────────→ LLM → Answer
Chain of thought: Question + "think step by step" → LLM → Steps → Answer
Role:       "You are an expert…" + Question ──→ LLM → Answer in that role
```

## Real-world use cases

- Chatbots with a fixed personality or role
- Getting answers in a specific format
- Solving maths and logic problems step by step

**In my project:** the Telugu voice assistant uses **role prompting**. Its prompt (written in Telugu) tells the LLM:
- "You are **Yodha**, a friendly Telugu AI assistant" (the role)
- answer mainly in Telugu
- give short answers to short questions
- don't use symbols like `*` or `#` (they would be read aloud)
- if you don't know, say so; don't imagine

It also gives the current time and date, and the vehicle-manual passage from [RAG](14-rag.md) ([`voice-assistant/api.py`](https://github.com/SEVT-Logistics-Private-Limited/tiny-llm-jetson/blob/main/voice-assistant/api.py), function `build_system`).

## Key takeaways

- Zero-shot = no example, one-shot = one example, few-shot = several examples.
- Chain of thought = step-by-step reasoning.
- Role prompting = tell the model what role to take.

---

**Previous:** [← Transformers](19-transformers.md) · [Home](../README.md) · **Next:** [Hallucination →](21-hallucination.md)
