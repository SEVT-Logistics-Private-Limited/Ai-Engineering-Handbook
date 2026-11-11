# 11. VLA (Vision Language Action)

> A VLA helps AI-powered robots understand their surroundings, follow instructions and perform physical actions. It sees, understands and acts.

## Introduction

A [VLM](10-vlm.md) can describe what it sees, but it can't do anything about it. A VLA goes one step further: it **acts**.

## What is it?

**VLA (Vision Language Action)** helps **AI-powered robots** to:
- understand their surroundings
- follow instructions
- perform physical actions

> **Sees → Understands → Acts**
>
> Vision + Language + Action

## Why is it needed?

Robots need to turn an instruction in human language into real movement in the physical world.

## How does it work?

Example: you tell a robot **"Pick up the red bottle."**

The VLA:
1. **Sees** the bottle using a camera
2. **Understands** the instruction
3. **Determines** the required movement
4. **Generates** the action

### VLM vs VLA

| VLM | VLA |
|---|---|
| Vision Language Model | Vision Language Action |
| Understands images and language | Connects vision and language to action |
| Describes images and answers questions | Helps control physical actions |
| Image question answering | Robotic manipulation |
| Shown a red bottle: "I can see a red bottle on the table." | Sees the red bottle, understands "pick it up", generates actions and picks it up |
| Only says what it sees; no action | Sees, understands and acts |
| **VLM = sees and understands** | **VLA = sees, understands and acts** |

## Flow diagram

```text
Instruction: "Pick up the red bottle"
              ↓
Sees the bottle (camera)
              ↓
Understands the instruction
              ↓
Determines the required movement
              ↓
Generates the action
              ↓
Robot picks up the bottle
```

## Real-world use cases

- Warehouse robots picking items
- Household robots
- Robotic arms in factories

## In our project

**Not used yet.** Our project is a voice assistant, not a robot. It answers questions but doesn't perform physical actions.

## Key takeaways

- VLA = Vision + Language + Action.
- It sees, understands and acts.
- A VLM only describes. A VLA actually does the task.

---

**Previous:** [← VLM](10-vlm.md) · [Home](../README.md) · **Next:** [LLM →](12-llm.md)
