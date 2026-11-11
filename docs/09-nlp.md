# 9. NLP (Natural Language Processing)

> NLP is the branch of AI that helps computers understand, process and work with human language.

## Introduction

Humans talk in languages like English and Telugu. Computers only understand numbers. NLP is the bridge between the two.

## What is it?

**NLP (Natural Language Processing)** is a **branch of AI** that helps computers **understand, process and work with human language**. It deals with **text**.

## Why is it needed?

- It helps computers understand human language.
- It helps computers process human language requests.

## How does it work?

Example: you tell the computer **"Book a ticket to Hyderabad"**.

NLP helps the computer understand:
- **what you are asking**
- **what action you want**
- **what information it needs**

## Flow diagram

```text
Human language ("Book a ticket to Hyderabad")
              ↓
             NLP
              ↓
   Understand → Process → Work with it
              ↓
   Action: book the ticket
```

```text
NLP  →  helps the computer  →  understand  →  process  →  work with human language
```

## Real-world use cases

- Google Translate
- Voice assistants (Siri, Alexa)
- Chatbots and customer support
- Spam detection

## In our project

**Used. The whole assistant is an NLP system:** it understands Telugu requests and replies in Telugu.

| NLP task | How we do it |
|---|---|
| **Understand speech** | Telugu speech → Telugu text (browser speech recognition, `te-IN`, with Gemini as backup) |
| **Recognise simple requests** | Exact keyword matching for time, date and greetings (`సమయం`, `తేదీ`, `నమస్కారం`…), answered instantly without the LLM |
| **Translate** | Telugu question → English, so it can be matched against the English vehicle manuals |
| **Understand and answer** | The LLM reads the question and generates a Telugu answer |
| **Clean the text** | Remove symbols (`*`, `#`), list numbers and English-only lines so speech sounds natural |
| **Detect the language** | Count Telugu characters (Unicode range `ఀ`–`౿`). If the answer has almost no Telugu, reply "మళ్ళీ చెప్పగలరా?" ("Can you say that again?") |

```text
"ఇప్పుడు సమయం?" (what's the time?) → keyword match → instant answer
"ఇంజిన్ ఆయిల్ ఎప్పుడు మార్చాలి?" (when to change engine oil?) → translate → RAG → LLM → Telugu answer
```

Code: [`voice-assistant/api.py`](https://github.com/SEVT-Logistics-Private-Limited/tiny-llm-jetson/blob/main/voice-assistant/api.py) (functions `check_instant`, `gemini_translate`, `clean_for_tts`)

---

**Previous:** [← FPS](08-fps.md) · [Home](../README.md) · **Next:** [VLM →](10-vlm.md)
