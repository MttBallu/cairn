"""Operations for simple content extraction within a raw file."""

from pathlib import Path


def extract_frontmatter_as_str(path: Path) -> str:
    """Read UTF-8 YAML frontmatter delimited by lines containing ``---``."""
    with path.open("rb") as file:
        opening = file.readline().removeprefix(b"\xef\xbb\xbf")
        if opening.rstrip(b" \t\r\n") != b"---":
            return ""

        lines: list[bytes] = []
        for line in file:
            if line.rstrip(b" \t\r\n") == b"---":
                break
            lines.append(line)
        else:
            raise ValueError(f"Unclosed YAML frontmatter in {path}")

    return b"".join(lines).decode("utf-8")
