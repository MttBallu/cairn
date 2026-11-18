"""Tools for the management of markdown files."""

from collections.abc import Sequence
from pathlib import Path
from typing import Any
import re

import frontmatter
import yaml
from attrs import define, frozen, validators, field
from markdown_it import MarkdownIt
from markdown_it.token import Token

from ._extraction import extract_frontmatter_as_str

type SectionTitles = dict[str, SectionTitles]
type MarkdownTokens = list[Token]


def _check_markdown_file(path: Path) -> None:
    if not path.suffix == ".md":
        raise ValueError(f"Markdown file expected. Got '{path.suffix}' as extension.")


def extract_frontmatter_from_markdown_file(path: Path) -> dict[str, Any]:
    """
    Extract the frontmatter from a Markdown file as a dict.

    Parameters
    ----------
    path: pathlib.Path
        Path to the Markdown file.

    Returns
    -------
    dict
        Dictionary where keys are str.
    """
    _check_markdown_file(path)
    stream = extract_frontmatter_as_str(path)
    metadata = yaml.safe_load(stream)
    if metadata is None:
        return {}

    if not isinstance(metadata, dict) or any(not isinstance(key, str) for key in metadata):
        raise ValueError(f"Expected a YAML mapping with string keys in {path}")

    return metadata


@define(frozen=True)
class MarkdownRawFileContent:
    """Store frontmatter metadata and a Markdown body.

    Parameters
    ----------
    frontmatter : dict of str to Any
        Parsed frontmatter metadata, with string keys.
    body : str
        Markdown body after frontmatter extraction.

    Notes
    -----
    Attributes cannot be rebound after initialization. The frontmatter
    dictionary itself remains mutable.
    """

    frontmatter: dict[str, Any] = field(
        validator=validators.deep_mapping(
            key_validator=validators.instance_of(str),
            mapping_validator=validators.instance_of(dict),
        )
    )
    body: str = field(validator=validators.instance_of(str))


@frozen
class Heading:
    """Represent a Markdown heading and its source line range.

    Parameters
    ----------
    title : str
        Heading text, preserving inline Markdown markup.
    rank : int
        Heading rank from 1 to 6, independent of token nesting depth.
    line_start : int
        Zero-based index of the first heading line in the parsed body.
    line_end : int
        Exclusive end line index of the heading, not of the whole section.
        Must be greater than ``line_start``.

    Raises
    ------
    TypeError
        If a field has an incompatible type.
    ValueError
        If the rank or source line range is invalid.

    Notes
    -----
    Instances are immutable. An underlined heading can span multiple lines.
    """

    title: str = field(validator=validators.instance_of(str))
    rank: int = field(validator=[validators.instance_of(int), validators.in_((1, 2, 3, 4, 5, 6))])
    line_start: int = field(validator=[validators.instance_of(int), validators.ge(0)])
    line_end: int = field(validator=validators.instance_of(int))

    def __attrs_post_init__(self) -> None:
        """Validate the relationship between source line bounds.

        Raises
        ------
        ValueError
            If ``line_end`` is not greater than ``line_start``.
        """
        if self.line_end <= self.line_start:
            raise ValueError("line_end must be greater than line_start")


class SectionNotFoundError(LookupError):
    """Indicate that no section matches the requested title or path."""


class DuplicateSectionTitleError(ValueError):
    """Indicate duplicate sibling titles or an ambiguous section path."""


def extract_text_from_markdown_file(path: Path) -> MarkdownRawFileContent:
    """Read a Markdown file and separate its frontmatter from its body.

    Parameters
    ----------
    path : pathlib.Path
        Path to a UTF-8 text file whose suffix is exactly ``.md``.

    Returns
    -------
    MarkdownRawFileContent
        Parsed metadata and the Markdown body. An empty file produces
        an empty metadata dictionary and an empty body. A file without
        frontmatter produces an empty metadata dictionary.

    Raises
    ------
    ValueError
        If the file suffix is not exactly ``.md``.
    OSError
        If the file cannot be opened or read.
    UnicodeDecodeError
        If the file cannot be decoded as UTF-8.
    yaml.YAMLError
        If YAML frontmatter cannot be parsed.
    TypeError
        If parsed metadata is incompatible with the container's validation.

    Notes
    -----
    The body is returned by ``frontmatter.parse`` and is not parsed into
    Markdown tokens here. File reading and frontmatter parsing can normalize
    newlines or surrounding whitespace; the result is not a byte-for-byte
    representation of the original file.
    """
    if not path.suffix == ".md":
        raise ValueError(f"Markdown file expected. Got '{path.suffix}' as extension.")

    buffer = path.read_text(encoding="utf-8")
    if not buffer:
        return MarkdownRawFileContent(frontmatter={}, body="")
    metadata, body = frontmatter.parse(buffer)
    return MarkdownRawFileContent(frontmatter=metadata, body=body)


def extract_headings(tokens: MarkdownTokens) -> list[Heading]:
    """Extract headings in document order from parsed Markdown tokens.

    Parameters
    ----------
    tokens : MarkdownTokens
        Complete token sequence parsed from a Markdown body without
        frontmatter, using the CommonMark configuration of ``MarkdownIt``.

    Returns
    -------
    list of Heading
        Headings outside lists, block quotes, and code blocks, in document
        order. Repeated titles and skipped ranks are preserved. Return an
        empty list if there are no eligible headings.

    Raises
    ------
    ValueError
        If an eligible heading lacks source line information or a following
        inline token, or its rank or line range is invalid.

    Notes
    -----
    This function does not parse source text or modify tokens. Line ranges
    refer to headings in the parsed body, excluding any removed frontmatter.
    """
    headings: list[Heading] = []
    for index, token in enumerate(tokens):
        if token.type != "heading_open" or token.level != 0:
            continue
        if token.map is None:
            raise ValueError("Heading token has no source line range")
        if index + 1 >= len(tokens) or tokens[index + 1].type != "inline":
            raise ValueError("Heading token must be followed by an inline token")
        headings.append(
            Heading(
                title=tokens[index + 1].content,
                rank=int(token.tag[1:]),
                line_start=token.map[0],
                line_end=token.map[1],
            )
        )
    return headings


def extract_section_titles(headings: list[Heading]) -> SectionTitles:
    """Extract section titles as a nested dictionary.

    Parameters
    ----------
    headings : list of Heading
        Complete sequence of eligible headings in document order, as
        returned by ``extract_headings``.

    Returns
    -------
    SectionTitles
        Dictionary mapping each section title to a dictionary of its
        subsections, in document order. Sections without subsections map
        to empty dictionaries. If there are no headings, return ``{}``.

    Raises
    ------
    DuplicateSectionTitleError
        If two sections under the same parent have identical titles.

    Notes
    -----
    Titles preserve inline Markdown markup and are compared case-sensitively.
    The same title may occur under different parents.

    A heading belongs to the nearest preceding heading of lower rank,
    including when heading ranks are skipped. This function does not parse
    Markdown or extract headings from tokens.
    """
    sections: SectionTitles = {}
    stack: list[tuple[int, SectionTitles]] = [(0, sections)]

    for heading in headings:
        rank = heading.rank
        title = heading.title

        while stack[-1][0] >= rank:
            stack.pop()

        siblings = stack[-1][1]
        if title in siblings:
            raise DuplicateSectionTitleError(
                f"Repeated section title under the same parent: {title!r}"
            )

        children: SectionTitles = {}
        siblings[title] = children
        stack.append((rank, children))

    return sections


def extract_section_from_body(body: str, headings: list[Heading], title: str) -> str:
    """Extract the content of the first section matching a title.

    Parameters
    ----------
    body : str
        Markdown body after removing frontmatter.
    headings : list of Heading
        Complete sequence of eligible headings extracted from exactly
        ``body``, in document order. Line positions must refer to this body.
    title : str
        Heading text to match exactly and case-sensitively, including
        any inline Markdown markup but excluding heading delimiters.

    Returns
    -------
    str
        Section content excluding its heading and including subsections.
        Content ends at the next heading of equal or higher rank, or at
        the end of the body. Whitespace and line endings from ``body``
        are preserved. An empty section returns ``""``.

    Raises
    ------
    SectionNotFoundError
        If no eligible heading matches ``title``.

    Notes
    -----
    If multiple headings match, the first is selected regardless of its
    ancestry. Use ``extract_section_by_path`` to specify the ancestry.
    This function does not parse Markdown or modify the supplied headings.
    """
    for index, heading in enumerate(headings):
        if heading.title == title:
            return _extract_heading_content(body, headings, index)
    raise SectionNotFoundError(f"Section not found: {title!r}")


def extract_section_by_path(body: str, headings: list[Heading], path: Sequence[str]) -> str:
    """Extract section content identified by a complete ancestry path.

    Parameters
    ----------
    body : str
        Markdown body after removing frontmatter.
    headings : list of Heading
        Complete sequence of eligible headings extracted from exactly
        ``body``, in document order. Line positions must refer to this body.
    path : sequence of str
        Nonempty sequence of titles from a root section to the desired
        section, for example ``("Guide", "Usage", "Examples")``. Every
        component must match exactly, including case and inline Markdown
        markup. A single string is not accepted as a path.

    Returns
    -------
    str
        Section content excluding its heading and including subsections,
        up to the next heading of equal or higher rank or the end of the
        body. Whitespace and line endings are preserved. An empty section
        returns ``""``.

    Raises
    ------
    TypeError
        If ``path`` is a string or contains non-string components.
    ValueError
        If ``path`` is empty.
    SectionNotFoundError
        If no section has the complete requested ancestry path.
    DuplicateSectionTitleError
        If more than one section has the complete requested ancestry path.

    Notes
    -----
    Each component identifies an immediate child of the previous section.
    Parentage follows heading ranks, not consecutive rank numbers; skipped
    ranks are allowed. Root sections need not have rank 1. Partial paths
    and suffix matches are not supported. Repeated titles on other paths
    do not cause an error.

    This function does not parse Markdown or modify the supplied headings.
    """
    if isinstance(path, str):
        raise TypeError("path must be a sequence of titles, not a string")
    target = tuple(path)
    if not target:
        raise ValueError("path must contain at least one title")
    if any(not isinstance(title, str) for title in target):
        raise TypeError("path components must be strings")

    ancestry: list[Heading] = []
    match_index: int | None = None
    for index, heading in enumerate(headings):
        while ancestry and ancestry[-1].rank >= heading.rank:
            ancestry.pop()
        ancestry.append(heading)
        if tuple(ancestor.title for ancestor in ancestry) == target:
            if match_index is not None:
                raise DuplicateSectionTitleError(f"Ambiguous section path: {target!r}")
            match_index = index

    if match_index is None:
        raise SectionNotFoundError(f"Section path not found: {target!r}")
    return _extract_heading_content(body, headings, match_index)


def _extract_heading_content(body: str, headings: list[Heading], index: int) -> str:
    """Slice the content of a section selected by heading index.

    Parameters
    ----------
    body : str
        Source Markdown body.
    headings : list of Heading
        Complete sequence of eligible headings from ``body``, in document
        order, with line positions referring to that body.
    index : int
        Valid index of the selected heading in ``headings``.

    Returns
    -------
    str
        Content excluding the heading, including subsections, and preserving
        the body's whitespace and line endings.
    """
    # Match the parser's line boundaries without treating Unicode separators
    # as newlines, and retain the original line endings in returned slices.
    line_starts = [0, *(match.end() for match in re.finditer(r"\r\n|\r|\n", body)), len(body)]
    selected = headings[index]
    start = line_starts[selected.line_end]
    for heading in headings[index + 1 :]:
        if heading.rank <= selected.rank:
            return body[start : line_starts[heading.line_start]]
    return body[start:]
