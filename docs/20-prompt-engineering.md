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

## In our project

**Used. Our assistant's personality and rules come from its prompt.** It's built fresh for every question (function `build_system`):

| Prompt part | What it says (written in Telugu) | Technique |
|---|---|---|
| **Role** | "You are **Yodha**, a friendly Telugu AI assistant" | Role prompting |
| **Current time** | The current IST time, date and weekday | Giving context |
| **Facts** | Capitals of India, Telangana and Andhra Pradesh | Giving context |
| **Rules** | Answer mainly in Telugu, short answers for short questions, no symbols like `*` `#` `_` `/` | Clear instructions |
| **Honesty** | For live data (cricket scores, weather) say "అది నాకు live గా తెలియదు మిత్రమా" ("I don't know that live, friend"), and don't imagine unknown facts | Reducing hallucination |
| **Manual text** | The vehicle-manual passage from RAG, with its source | Giving context (RAG) |
| **History** | The last 8 messages of the conversation | Memory |

```text
Role (Yodha) + time + rules + manual passage (RAG) + last 8 messages + user question
        ↓
      Gemini
        ↓
  Telugu answer
```

**A lesson we learned:** some Gemini models returned **empty answers** when the role was sent as a "system instruction". The fix was to send the role as the first user message, followed by a model reply "సరే." ("Okay."). It works with every model.

Code: [`voice-assistant/api.py`](https://github.com/SEVT-Logistics-Private-Limited/tiny-llm-jetson/blob/main/voice-assistant/api.py) (functions `build_system`, `telugu_llm`, `get_context`)

## Key takeaways

- Zero-shot = no example, one-shot = one example, few-shot = several examples.
- Chain of thought = step-by-step reasoning.
- Role prompting = tell the model what role to take.

---

**Previous:** [← Transformers](19-transformers.md) · [Home](../README.md) · **Next:** [Hallucination →](21-hallucination.md)
