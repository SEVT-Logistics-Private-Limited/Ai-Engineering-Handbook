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

## In our project

**Used. The assistant has four protections against hallucination:**

| Protection | How it works in our code | Mitigation from this page |
|---|---|---|
| **"Don't imagine" rule** | The prompt says: if you don't know, say so; don't imagine | Better prompts |
| **Live-data rule** | For cricket scores, weather and news, reply "అది నాకు live గా తెలియదు మిత్రమా" ("I don't know that live") | Better prompts |
| **RAG** | Answers about vehicles use the real manual passage | RAG, source grounding |
| **Relevance check** | A manual passage is used only if it's close enough (distance ≤ 0.35), so unrelated text isn't used | Validation |
| **Output check** | If the answer has fewer than 3 Telugu characters, reply "మళ్ళీ చెప్పగలరా?" ("Can you say that again?") instead | Validation |

```text
Question about live cricket score → prompt rule → "I don't know that live"
Question about engine oil         → RAG finds the manual → grounded answer
Answer comes back in English only → output check → "Can you say that again?"
```

Code: [`voice-assistant/api.py`](https://github.com/SEVT-Logistics-Private-Limited/tiny-llm-jetson/blob/main/voice-assistant/api.py) (functions `build_system`, `retrieve_manual_context`, `clean_for_tts`)

---

**Previous:** [← Prompt Engineering](20-prompt-engineering.md) · [Home](../README.md) · **Next:** [Tokenization →](22-tokenization.md)
