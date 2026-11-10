# Naming and Cross-Linking Rules

## Folder boundaries
- `concepts/` contains technology explanations only.
- `evidence/` contains project-specific implementation evidence only.
- `projects/` contains the project registry, not concept tutorials.
- `templates/` contains reusable page formats.

## Canonical modality folders
`foundations`, `text`, `image`, `video`, `audio`, `multimodal`. Use the same names under both `concepts/` and `evidence/`.

## Concept page naming
Pattern: `concepts/<modality>/<NNN>-<topic-slug>.md`.

Examples:
- `concepts/foundations/001-what-is-data.md`
- `concepts/text/010-what-is-text.md`
- `concepts/text/020-text-encoding-ascii-utf8.md`
- `concepts/image/010-image-pixel-representation.md`
- `concepts/audio/010-digital-audio-representation.md`

Use three-digit ordering within each modality. Keep slugs short, descriptive and lowercase. Use hyphens, not spaces or underscores.

## Evidence page naming
Pattern: `evidence/<modality>/<project-slug>--<topic-slug>.md`.

Examples:
- `evidence/text/tiny-gpt-jetson-colab--tokenization.md`
- `evidence/audio/telugu-voice-assistant--speech-to-text.md`
- `evidence/multimodal/yoda-agentic-workflows--tool-orchestration.md`

One evidence page documents one project-to-concept relationship. Two projects using the same concept require two separate evidence pages.

## Stable IDs
- Foundations: `FND-001`
- Text: `TXT-010`
- Image: `IMG-010`
- Video: `VID-010`
- Audio: `AUD-010`
- Multimodal: `MM-010`

Project slugs: `tiny-gpt-jetson-colab`, `telugu-voice-assistant`, `yoda-agentic-workflows`.

Do not renumber published topics. If a topic is retired, mark it deprecated and link to its replacement.

## Required two-way links

Every concept page includes `Related project evidence`, linking to every matching evidence page using relative paths. Every evidence page includes `Linked concept`, linking back to exactly one primary concept page.

Example pair:
- Concept: `concepts/text/020-text-encoding-ascii-utf8.md`
- Evidence: `evidence/text/tiny-gpt-jetson-colab--text-encoding.md`
- From evidence to concept: `../../concepts/text/020-text-encoding-ascii-utf8.md`
- From concept to evidence: `../../evidence/text/tiny-gpt-jetson-colab--text-encoding.md`

## Evidence status labels
- `TODO: supply` — details not yet provided.
- `Planned` — intended, not implemented.
- `Explored` — studied/prototyped, integration not confirmed.
- `Implemented` — implementation exists in code/configuration.
- `Tested` — test or reproducible run verifies behavior.
- `Measured` — metric has documented method and context.

A dependency in requirements or a project name alone is not proof of implementation. Link exact source files, functions, commits, tests or measurement records.

## Writing conventions
- Use consistent Markdown headings.
- Use Mermaid for editable diagrams.
- Use language-tagged code fences.
- Expand acronyms on first use.
- Record units, dataset split, model/version and hardware beside metrics.
- Prefer official documentation and primary research.
- Do not publish secrets, customer data or confidential project information.