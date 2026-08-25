"""Fail when a documentation link points to a missing local source."""

from __future__ import annotations

import json
import re
from pathlib import Path
from urllib.parse import unquote, urlparse


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
SITE_PATH = "/Multitask-Delphos/"
LINK_PATTERN = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")


def markdown_sources() -> list[Path]:
    return sorted(DOCS.rglob("*.md")) + [ROOT / "README.md", ROOT / "CONTRIBUTING.md"]


def notebook_markdown(path: Path) -> str:
    notebook = json.loads(path.read_text(encoding="utf-8"))
    chunks: list[str] = []
    for cell in notebook.get("cells", []):
        if cell.get("cell_type") != "markdown":
            continue
        source = cell.get("source", "")
        chunks.append("".join(source) if isinstance(source, list) else source)
    return "\n".join(chunks)


def site_source(target: str) -> Path | None:
    parsed = urlparse(target)
    if parsed.netloc != "tud-cityai-lab.github.io" or not parsed.path.startswith(SITE_PATH):
        return None
    relative = unquote(parsed.path.removeprefix(SITE_PATH)).strip("/")
    if not relative:
        return DOCS / "index.md"
    explicit = DOCS / relative
    if explicit.suffix in {".md", ".ipynb"}:
        return explicit
    markdown = DOCS / f"{relative}.md"
    return markdown if markdown.exists() else DOCS / relative / "index.md"


def local_source(origin: Path, raw_target: str) -> Path | None:
    target = raw_target.strip().strip("<>").split(maxsplit=1)[0]
    target = unquote(target.split("#", 1)[0])
    if not target or target.startswith(("#", "mailto:", "tel:")):
        return None
    if target.startswith(("http://", "https://")):
        return site_source(target)
    return (origin.parent / target).resolve()


def main() -> int:
    failures: list[str] = []
    sources = [(path, path.read_text(encoding="utf-8")) for path in markdown_sources()]
    sources += [(path, notebook_markdown(path)) for path in sorted(DOCS.rglob("*.ipynb"))]

    for origin, text in sources:
        for line_number, line in enumerate(text.splitlines(), start=1):
            for match in LINK_PATTERN.finditer(line):
                target = local_source(origin, match.group(1))
                if target is not None and not target.exists():
                    failures.append(
                        f"{origin.relative_to(ROOT)}:{line_number}: "
                        f"missing target {match.group(1)!r}"
                    )

    if failures:
        print("Documentation link check failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("All local documentation links resolve to existing sources.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
