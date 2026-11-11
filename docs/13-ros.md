# 13. ROS (Robot Operating System)

> ROS is a robotics software framework that provides tools and communication mechanisms to build and control robots.

## Introduction

A robot is many parts working together: cameras, sensors, arms, a microphone. Something has to connect them so they can talk to each other. That's ROS.

## What is it?

**ROS (Robot Operating System)** is a **robotics software framework** that provides **tools and communication mechanisms** to build and control robots.

## Why is it needed?

Imagine you're building a robot. It has:
- a camera
- sensors
- arms
- a microphone

All of these **need to communicate with each other**. ROS helps **connect, communicate between and coordinate** these components.

## How does it work?

ROS acts like the robot's nervous system. Each part (camera, sensor, arm) sends and receives messages through ROS, so information from the camera can reach the AI brain, and commands from the AI brain can reach the arms.

### How it fits with the other AI models

| Name | What it does |
|---|---|
| NLP | Understands human language |
| LLM | Understands and generates language using a trained model |
| VLM | Understands images and text, and generates text responses |
| VLA | Connects vision, language and physical actions |
| **ROS** | **Connects and coordinates robot software and hardware** |

## Flow diagram

```text
Camera  ─┐
Sensors ─┤
Arms    ─┼──→  ROS  ←──→  AI brain (VLA)
Mic     ─┘
        (connects, communicates, coordinates)
```

```text
Camera sees the bottle → ROS → VLA decides "pick it up" → ROS → Arm moves
```

## Real-world use cases

- Research and university robots
- Warehouse and delivery robots
- Drones
- Industrial robotic arms

## Key takeaways

- ROS is a framework for building and controlling robots.
- It connects and coordinates the camera, sensors, arms and microphone.
- ROS connects and coordinates robot software and hardware.

---

**Previous:** [← LLM](12-llm.md) · [Home](../README.md) · **Next:** [RAG →](14-rag.md)
