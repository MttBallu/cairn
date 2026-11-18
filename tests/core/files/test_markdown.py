"""Tests for markdown_revised.py (Python 3.12+).

Place this file beside markdown_revised.py and run:
    uv run --with pytest --with attrs --with python-frontmatter \
        --with markdown-it-py python -m pytest -q test_markdown.py

If the module lives in your package, adjust the import below.
"""

from copy import deepcopy
from pathlib import Path

import pytest
from attrs.exceptions import FrozenInstanceError
from markdown_it import MarkdownIt
from markdown_it.token import Token
from yaml import YAMLError

import markdown_revised as markdown


@pytest.fixture
def parser() -> MarkdownIt:
    """Provide the CommonMark parser used by the extraction contract."""
    return MarkdownIt("commonmark")


@pytest.fixture
def branch_document() -> str:
    """Provide repeated titles in distinct branches and a nested subsection."""
    return (
        "# Guide\nintro\n"
        "## Usage\nusage intro\n"
        "### Examples\nuser example\n"
        "#### Detail\nmore\n"
        "## Development\n"
        "### Examples\ndev example\n"
        "# Appendix\nend"
    )


@pytest.mark.parametrize("rank", range(1, 7))
def test_heading_accepts_valid_ranks(rank: int) -> None:
    heading = markdown.Heading("Example", rank, 0, 2)
    assert (heading.title, heading.rank, heading.line_start, heading.line_end) == (
        "Example", rank, 0, 2
    )


@pytest.mark.parametrize(
    "field,value,error",
    [
        ("rank", 0, ValueError),
        ("rank", 7, ValueError),
        ("rank", "2", TypeError),
        ("title", None, TypeError),
        ("line_start", -1, ValueError),
        ("line_start", "0", TypeError),
        ("line_end", 0, ValueError),
        ("line_end", -1, ValueError),
        ("line_end", "1", TypeError),
    ],
)
def test_heading_rejects_invalid_fields(field, value, error) -> None:
    arguments = {"title": "Example", "rank": 2, "line_start": 0, "line_end": 1}
    arguments[field] = value
    with pytest.raises(error):
        markdown.Heading(**arguments)


def test_heading_is_immutable() -> None:
    heading = markdown.Heading("Example", 2, 0, 1)
    with pytest.raises(FrozenInstanceError):
        heading.title = "Changed"


@pytest.mark.parametrize(
    "source,metadata,body",
    [
        ("", {}, ""),
        ("# Example\nBody", {}, "# Example\nBody"),
        (
            "---\nid: PY-001\ntags: [python, attrs]\n---\n# Example\nBody\n",
            {"id": "PY-001", "tags": ["python", "attrs"]},
            "# Example\nBody",
        ),
    ],
)
def test_read_file_separates_metadata_and_body(tmp_path, source, metadata, body) -> None:
    path = tmp_path / "example.md"
    path.write_text(source, encoding="utf-8")
    before = path.read_bytes()
    result = markdown.extract_text_from_markdown_file(path)
    assert result.frontmatter == metadata
    assert result.body == body
    assert path.read_bytes() == before


@pytest.mark.parametrize("suffix", [".txt", ".MD", ""])
def test_read_file_rejects_other_suffixes(tmp_path: Path, suffix: str) -> None:
    with pytest.raises(ValueError):
        markdown.extract_text_from_markdown_file(tmp_path / f"example{suffix}")


def test_read_file_reports_missing_file(tmp_path: Path) -> None:
    with pytest.raises(FileNotFoundError):
        markdown.extract_text_from_markdown_file(tmp_path / "missing.md")


def test_read_file_reports_invalid_yaml(tmp_path: Path) -> None:
    path = tmp_path / "invalid.md"
    path.write_text("---\ntags: [unclosed\n---\nBody", encoding="utf-8")
    with pytest.raises(YAMLError):
        markdown.extract_text_from_markdown_file(path)


def test_read_file_reports_invalid_utf8(tmp_path: Path) -> None:
    path = tmp_path / "invalid.md"
    path.write_bytes(b"\xff")
    with pytest.raises(UnicodeDecodeError):
        markdown.extract_text_from_markdown_file(path)


def test_extract_headings_preserves_markup_and_line_ranges(parser: MarkdownIt) -> None:
    body = "## Use `attrs` ###\n\nText\n\nDetails\n-------\n"
    assert markdown.extract_headings(parser.parse(body)) == [
        markdown.Heading("Use `attrs`", 2, 0, 1),
        markdown.Heading("Details", 2, 4, 6),
    ]


def test_extract_headings_preserves_repetitions_and_skipped_ranks(parser) -> None:
    body = "## A\n#### A\n## A\n"
    assert markdown.extract_headings(parser.parse(body)) == [
        markdown.Heading("A", 2, 0, 1),
        markdown.Heading("A", 4, 1, 2),
        markdown.Heading("A", 2, 2, 3),
    ]


@pytest.mark.parametrize(
    "body",
    [
        "", "Ordinary text", "```markdown\n# Example\n```",
        "~~~markdown\n# Example\n~~~", "    # Example\n",
        "> # Example\n", "- # Example\n", "<div>\n# Example\n</div>\n",
    ],
)
def test_extract_headings_ignores_non_document_headings(parser, body: str) -> None:
    assert markdown.extract_headings(parser.parse(body)) == []


def test_extract_headings_does_not_modify_tokens(parser: MarkdownIt) -> None:
    tokens = parser.parse("# Title\n\nUse **attrs**.\n")
    original = deepcopy(tokens)
    markdown.extract_headings(tokens)
    assert tokens == original


@pytest.mark.parametrize("problem", ["missing_map", "missing_inline", "wrong_inline"])
def test_extract_headings_rejects_malformed_heading_tokens(problem: str) -> None:
    opening = Token("heading_open", "h2", 1, map=[0, 1])
    inline = Token("inline", "", 0, content="Example")
    tokens = [opening, inline]
    if problem == "missing_map":
        opening.map = None
    elif problem == "missing_inline":
        tokens.pop()
    else:
        inline.type = "paragraph_open"
    with pytest.raises(ValueError):
        markdown.extract_headings(tokens)


def test_section_tree_uses_rank_and_preserves_order() -> None:
    headings = [
        markdown.Heading("Guide", 2, 0, 1),
        markdown.Heading("Usage", 4, 1, 2),
        markdown.Heading("Examples", 6, 2, 3),
        markdown.Heading("References", 3, 3, 4),
        markdown.Heading("Appendix", 1, 4, 5),
    ]
    tree = markdown.extract_section_titles(headings)
    assert tree == {
        "Guide": {"Usage": {"Examples": {}}, "References": {}},
        "Appendix": {},
    }
    assert list(tree) == ["Guide", "Appendix"]
    assert list(tree["Guide"]) == ["Usage", "References"]


def test_section_tree_is_empty_without_headings() -> None:
    assert markdown.extract_section_titles([]) == {}


def test_section_tree_allows_same_title_under_different_parents(parser) -> None:
    headings = markdown.extract_headings(parser.parse("# A\n## Example\n# B\n## Example"))
    assert markdown.extract_section_titles(headings) == {
        "A": {"Example": {}}, "B": {"Example": {}}
    }


@pytest.mark.parametrize("body", ["# A\n# A", "# A\n## B\n## B"])
def test_section_tree_rejects_duplicate_siblings(parser, body: str) -> None:
    headings = markdown.extract_headings(parser.parse(body))
    with pytest.raises(markdown.DuplicateSectionTitleError):
        markdown.extract_section_titles(headings)


@pytest.mark.parametrize(
    "body,expected",
    [
        ("# A", ""),
        ("# A\n# B", ""),
        ("# A\nlast", "last"),
        ("# A\nintro\n## B\nchild\n# C\nother", "intro\n## B\nchild\n"),
        ("A\n===\nbody\n\nB\n===", "body\n\n"),
        ("# A\n```md\n# Fake\n```\n# B", "```md\n# Fake\n```\n"),
        ("# A\ntext\u2028same line\n# B", "text\u2028same line\n"),
    ],
)
def test_both_lookups_preserve_section_boundaries(parser, body, expected) -> None:
    headings = markdown.extract_headings(parser.parse(body))
    assert markdown.extract_section_from_body(body, headings, "A") == expected
    assert markdown.extract_section_by_path(body, headings, ("A",)) == expected


@pytest.mark.parametrize("newline", ["\n", "\r\n", "\r"])
def test_both_lookups_preserve_line_endings(parser, newline: str) -> None:
    body = newline.join(["# A", "", "body  ", "", "# B"])
    expected = newline.join(["", "body  ", "", ""])
    headings = markdown.extract_headings(parser.parse(body))
    assert markdown.extract_section_from_body(body, headings, "A") == expected
    assert markdown.extract_section_by_path(body, headings, ("A",)) == expected


def test_title_lookup_returns_first_occurrence(parser, branch_document: str) -> None:
    headings = markdown.extract_headings(parser.parse(branch_document))
    assert markdown.extract_section_from_body(branch_document, headings, "Examples") == (
        "user example\n#### Detail\nmore\n"
    )


@pytest.mark.parametrize("title", ["Missing", "examples"])
def test_title_lookup_reports_missing_exact_title(parser, branch_document, title) -> None:
    headings = markdown.extract_headings(parser.parse(branch_document))
    with pytest.raises(markdown.SectionNotFoundError):
        markdown.extract_section_from_body(branch_document, headings, title)


@pytest.mark.parametrize(
    "path,expected",
    [
        (("Guide", "Usage", "Examples"), "user example\n#### Detail\nmore\n"),
        (["Guide", "Development", "Examples"], "dev example\n"),
        (("Appendix",), "end"),
    ],
)
def test_path_lookup_selects_the_requested_branch(parser, branch_document, path, expected) -> None:
    headings = markdown.extract_headings(parser.parse(branch_document))
    assert markdown.extract_section_by_path(branch_document, headings, path) == expected


@pytest.mark.parametrize(
    "path",
    [("Examples",), ("Guide", "Examples"), ("guide", "Usage", "Examples"),
     ("Guide", "Missing"), ("Guide", "Usage", "Examples", "Missing")],
)
def test_path_lookup_requires_complete_exact_ancestry(parser, branch_document, path) -> None:
    headings = markdown.extract_headings(parser.parse(branch_document))
    with pytest.raises(markdown.SectionNotFoundError):
        markdown.extract_section_by_path(branch_document, headings, path)


def test_path_lookup_allows_skipped_ranks_and_roots_below_h1(parser) -> None:
    body = "## A\n#### B\nvalue\n### C\nother\n## D\nend"
    headings = markdown.extract_headings(parser.parse(body))
    assert markdown.extract_section_by_path(body, headings, ("A", "B")) == "value\n"
    assert markdown.extract_section_by_path(body, headings, ("A", "C")) == "other\n"


@pytest.mark.parametrize(
    "body",
    ["# A\n## B\none\n## B\ntwo", "# A\n## B\none\n# A\n## B\ntwo"],
)
def test_path_lookup_rejects_repeated_complete_paths(parser, body) -> None:
    headings = markdown.extract_headings(parser.parse(body))
    with pytest.raises(markdown.DuplicateSectionTitleError):
        markdown.extract_section_by_path(body, headings, ("A", "B"))


def test_path_lookup_ignores_duplicates_on_other_paths(parser) -> None:
    body = "# A\n## B\nselected\n# X\n## Y\n## Y\n"
    headings = markdown.extract_headings(parser.parse(body))
    assert markdown.extract_section_by_path(body, headings, ("A", "B")) == "selected\n"


@pytest.mark.parametrize(
    "path,error", [((), ValueError), ([], ValueError), ("A", TypeError), ([1], TypeError)]
)
def test_path_lookup_rejects_invalid_path_arguments(path, error) -> None:
    with pytest.raises(error):
        markdown.extract_section_by_path("", [], path)


def test_lookups_report_absence_in_a_document_without_headings() -> None:
    with pytest.raises(markdown.SectionNotFoundError):
        markdown.extract_section_from_body("text", [], "A")
    with pytest.raises(markdown.SectionNotFoundError):
        markdown.extract_section_by_path("text", [], ("A",))


def test_lookups_match_titles_with_inline_markdown(parser) -> None:
    body = "# Use `attrs`\n## **Example**\ncontent"
    headings = markdown.extract_headings(parser.parse(body))
    assert markdown.extract_section_from_body(body, headings, "**Example**") == "content"
    assert markdown.extract_section_by_path(body, headings, ("Use `attrs`", "**Example**")) == "content"


def test_section_operations_accept_headings_without_reparsing(monkeypatch) -> None:
    body = "# A\n## B\ncontent"
    headings = [markdown.Heading("A", 1, 0, 1), markdown.Heading("B", 2, 1, 2)]
    original = headings.copy()

    def unexpected_extraction(*args, **kwargs):
        pytest.fail("Section handling must not parse Markdown or extract tokens")

    monkeypatch.setattr(markdown, "extract_headings", unexpected_extraction)
    monkeypatch.setattr(MarkdownIt, "parse", unexpected_extraction)
    assert markdown.extract_section_titles(headings) == {"A": {"B": {}}}
    assert markdown.extract_section_from_body(body, headings, "B") == "content"
    assert markdown.extract_section_by_path(body, headings, ("A", "B")) == "content"
    assert headings == original
