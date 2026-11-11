# Handbook conventions

This repo is a learning handbook. It goes from first principles to production, and it is tied to real project code. Keep it consistent.

## Page contract (every topic page)

```
# NN.M · Title
> **Modality:** … · **Prereqs:** links · **Used in project:** ✅ | 🟡 | ⬜

## 1. First principles
## 2. Diagram          (Mermaid; must render on GitHub)
## 3. Deep dive        (shapes, math, costs, trade-offs)
## 4. In our project   (permalinks into tiny-llm-jetson; say "Not yet used" if true)
## 5. Common pitfalls  (bullets: symptom → cause → fix)
## 6. References       (primary sources only)
```

## Rules

- **Never invent project usage.** Section 4 only describes what the code actually does. If the README and the code disagree, the code wins, and the discrepancy is called out.
- **Line-level links use commit permalinks** (`blob/<sha>/path#Lx-Ly`) so they don't drift. File-level links may use `blob/main`.
- Current pinned commit: `9a7b564c8d764d1eff92218261f2fd2cef99099e`. When re-pinning, update every `blob/<sha>` link and re-verify the line ranges.
- Mermaid: quote labels containing punctuation (`A["x (y)"]`) and avoid `<`/`>` in labels.
- Engineer-level depth, no filler. Prefer tables and bullets over prose.
- New topic → add it to the TOC and the topic→project map in `README.md`.
