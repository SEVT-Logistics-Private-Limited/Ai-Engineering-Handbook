# 21. Hallucination

> An LLM hallucinates when it generates information that appears plausible but is incorrect, unsupported or fabricated.

## Introduction

LLMs sound confident even when they're wrong. When an LLM makes something up, it's called **hallucination**.

## What is it?

An LLM **hallucinates** when it generates information that **appears plausible but is incorrect, unsupported or fabricated**.

> **Example:** "Who invented XYZ technology?" The model confidently names a person who never invented it.

## Why is it needed?

Knowing about hallucination is important before using an LLM for real work. A wrong answer that sounds right can mislead users.

## How does it work?

### Why does hallucination happen?

LLMs generate outputs based on **learned patterns** and the **information or context available to them**. They don't automatically verify every statement against a trusted database or reality.

**Factors can include:**
1. Missing information
2. Ambiguous questions
3. Poor prompts
4. Outdated knowledge
5. Insufficient context
6. Long or complex tasks
7. Retrieval failures

### How can you reduce hallucinations?

1. **RAG:** give the model real documents to answer from
2. **Better prompts**
3. **Structured outputs**
4. **Validation against trusted sources**
5. **Lower randomness (temperature) when appropriate**
6. **Citations / source grounding**

## Flow diagram

```text
Why it happens:
Question → LLM uses learned patterns → No fact-check → Plausible but wrong answer

How to reduce it:
Question → RAG (real documents) + better prompt + low temperature → LLM → Grounded answer with sources
```

## Real-world use cases

- Chatbots must not invent company policies
- Medical and legal assistants must give correct facts
- Vehicle assistants must not invent service details

**In my project:** the voice assistant reduces hallucination in two ways:
- Its prompt tells it **not to imagine unknown facts**, and to say it doesn't know.
- **RAG** gives it the real vehicle manual to answer from.

## Key takeaways

- Hallucination = plausible but wrong or made-up output.
- It happens because LLMs generate from patterns and don't verify facts.
- Reduce it with RAG, better prompts, structured outputs, validation, low temperature and citations.

---

**Previous:** [← Prompt Engineering](20-prompt-engineering.md) · [Home](../README.md) · **Next:** [Tokenization →](22-tokenization.md)
