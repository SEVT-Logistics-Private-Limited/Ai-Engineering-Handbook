# 25. Reinforcement Learning

> Reinforcement learning is a type of ML where an agent learns to make decisions by interacting with an environment and receiving rewards or penalties for its actions.

## Introduction

The other types of ML learn from a fixed dataset. Reinforcement learning is different: the model **learns by doing**, through trial and error.

## What is it?

**Reinforcement Learning (RL)** is a type of ML where an **agent** learns how to **make decisions** by **interacting with an environment** and **receiving rewards or penalties for its actions**.

| Term | Meaning | In the bicycle example |
|---|---|---|
| **Agent** | The learner that makes decisions | The kid |
| **Environment** | The world the agent acts in | The bicycle and the road |
| **Action** | What the agent does | Pedalling, steering, balancing |
| **Reward** | Feedback for a good action | Staying upright and moving forward |
| **Penalty** | Feedback for a bad action | Falling down |

### Example: a kid learning to ride a bicycle

Imagine a kid learning to ride a bicycle. Nobody can give them a table of correct answers. They try, wobble and fall (penalty), try again, and stay balanced a little longer (reward). After many attempts they learn which actions keep them upright.

## Why is it needed?

Some problems have no dataset of correct answers. The right move depends on the situation, and the result of an action is only known after trying it. Examples: playing a game, controlling a robot, driving. Reinforcement learning handles these by learning from the results of its own actions.

## How does it work?

1. The agent takes an action.
2. The environment responds.
3. The agent receives a reward or a penalty.
4. The agent learns from that feedback.
5. It chooses a better action next time, and the loop repeats.

Over many rounds, the agent learns the actions that earn the most reward.

## Flow diagram

```text
Agent → Takes action → Environment → Reward / Penalty
  ↑                                        ↓
Chooses a better action  ←────────────  Learns
```

## Real-world use cases

- Game-playing AI (chess, Go, video games)
- Robots learning to walk or pick up objects
- Self-driving cars
- Recommendation systems that learn from what users click

## In our project

**Not used yet.** Our voice assistant answers questions; it doesn't learn from rewards and penalties.

Reinforcement learning matters most in robotics, which connects to [VLA](10-vla.md) and [ROS](12-ros.md).

---

**Previous:** [← Semi-Supervised Learning](24-semi-supervised-learning.md) · [Home](../README.md) · **Next:** [DL →](17-dl.md)
