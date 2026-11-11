"""Check every relative link, heading anchor and image reference in the Markdown files.

Run from the repository root:
    python scripts/check_links.py

Exits with status 1 if anything is broken. External (http/https) links are not fetched.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"!?\[[^\]]*\]\(([^)\s]+)\)")
HTML_SRC = re.compile(r'<img[^>]+src="([^"]+)"')
HEADING = re.compile(r"^#{1,6}\s+(.+?)\s*$", re.MULTILINE)
CODE_BLOCK = re.compile(r"```.*?```", re.DOTALL)


def slugify(heading: str) -> str:
    """GitHub-style anchor: lowercase, drop punctuation except hyphens, spaces to hyphens."""
    heading = re.sub(r"[`*_]", "", heading).strip().lower()
    heading = re.sub(r"[^\w\- ]", "", heading)
    return heading.replace(" ", "-")


def anchors(path: Path) -> set[str]:
    text = CODE_BLOCK.sub("", path.read_text(encoding="utf-8"))
    return {slugify(h) for h in HEADING.findall(text)}


def main() -> int:
    errors = []
    md_files = sorted(p for p in ROOT.rglob("*.md") if ".git" not in p.parts and ".venv" not in p.parts)
    for md in md_files:
        text = CODE_BLOCK.sub("", md.read_text(encoding="utf-8"))
        targets = LINK.findall(text) + HTML_SRC.findall(text)
        for target in targets:
            if target.startswith(("http://", "https://", "mailto:")):
                continue
            path_part, _, anchor = target.partition("#")
            resolved = (md.parent / path_part).resolve() if path_part else md
            rel = md.relative_to(ROOT)
            if not resolved.exists():
                errors.append(f"{rel}: missing target {target}")
            elif anchor and resolved.suffix == ".md" and anchor not in anchors(resolved):
                errors.append(f"{rel}: missing anchor {target}")
    for e in errors:
        print(e)
    print(f"checked {len(md_files)} Markdown files: {len(errors)} broken link(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
