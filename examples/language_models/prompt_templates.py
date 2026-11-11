"""Prompt engineering patterns as reusable templates.

These functions build the prompt text. Send the result to any chat LLM API.

Run:
    python examples/language_models/prompt_templates.py
"""


def zero_shot(task: str, text: str) -> str:
    return f"{task}\n\nText: {text}\nAnswer:"


def few_shot(task: str, examples: list[tuple[str, str]], text: str) -> str:
    """One example = one-shot, several examples = few-shot."""
    shots = "\n\n".join(f"Text: {x}\nAnswer: {y}" for x, y in examples)
    return f"{task}\n\n{shots}\n\nText: {text}\nAnswer:"


def chain_of_thought(question: str) -> str:
    return f"{question}\n\nThink through the problem step by step, then give the final answer on the last line."


def role_prompt(role: str, request: str) -> list[dict]:
    """Chat-style messages: the system message sets the role."""
    return [
        {"role": "system", "content": f"You are {role}."},
        {"role": "user", "content": request},
    ]


def main() -> dict:
    task = "Classify the sentiment as Positive or Negative."
    prompts = {
        "zero-shot": zero_shot(task, "The service was quick and friendly."),
        "one-shot": few_shot(task, [("I love this phone.", "Positive")], "The battery died in an hour."),
        "few-shot": few_shot(task, [("I love this phone.", "Positive"),
                                    ("Worst purchase ever.", "Negative")], "Setup took two minutes."),
        "chain-of-thought": chain_of_thought("A service is due every 10,000 km. The car is at 23,500 km. "
                                             "How many km until the next service?"),
    }
    for name, prompt in prompts.items():
        print(f"--- {name} ---\n{prompt}\n")

    messages = role_prompt("an experienced AWS cloud engineer", "Explain AWS IAM.")
    print("--- role prompting (chat messages) ---")
    for m in messages:
        print(f"{m['role']:>6}: {m['content']}")
    prompts["role"] = messages
    return prompts


if __name__ == "__main__":
    main()
