from pathlib import Path
from typing import NewType

PathToMarkdown = NewType("PathToMarkdown", Path)


def parse_markdown_path(path: Path) -> PathToMarkdown:
    if path.suffix.lower() != ".md":
        raise ValueError(f"Markdown file expected, got {path.suffix!r}")
    return PathToMarkdown(path)
