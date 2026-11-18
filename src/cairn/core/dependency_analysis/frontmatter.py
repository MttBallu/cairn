"""Build and check directed relations declared in Markdown frontmatter."""

from collections.abc import Iterable, Mapping
from pathlib import Path

import networkx as nx

from cairn.core.files._errors import EmptyDirectoryError
from cairn.core.files.markdown import extract_frontmatter_from_markdown_file


class DependencyCycleError(ValueError):
    """Report a directed cycle as a closed sequence of document IDs."""

    def __init__(self, cycle: tuple[str, ...]) -> None:
        self.cycle = cycle
        super().__init__(f"Dependency cycle: {' -> '.join(cycle)}")


def extract_frontmatter_from_files(
    path_to_dir: Path, pattern: str = "*.md"
) -> list[dict[str, object]]:
    """Read frontmatter from matching files in a directory.

    Parameters
    ----------
    path_to_dir : pathlib.Path
        Directory in which to search.
    pattern : str, optional
        Glob pattern for selecting Markdown files.

    Returns
    -------
    list of dict
        Parsed frontmatter in sorted path order.

    Raises
    ------
    NotADirectoryError
        If the supplied path is missing or is not a directory.
    EmptyDirectoryError
        If no regular file matches the pattern.
    OSError
        If a matching file cannot be opened or read.
    ValueError
        If a matching file has the wrong suffix, invalid UTF-8, or an
        unclosed or invalidly shaped frontmatter block.
    yaml.YAMLError
        If a frontmatter block contains invalid YAML.
    """
    if not path_to_dir.is_dir():
        raise NotADirectoryError(path_to_dir)
    paths = sorted(path for path in path_to_dir.glob(pattern) if path.is_file())
    if not paths:
        raise EmptyDirectoryError(path_to_dir)
    return [extract_frontmatter_from_markdown_file(path) for path in paths]


def build_dependency_map(
    frontmatters: Iterable[Mapping[str, object]], *, source_key: str, relation_key: str
) -> dict[str, set[str]]:
    """Build an adjacency map for one relation declared in frontmatter.

    Parameters
    ----------
    frontmatters : iterable of mappings
        Parsed frontmatter. Input positions in errors are one-based.
    source_key : str
        Field containing the document's unique, nonblank string ID.
    relation_key : str
        Field containing a list of nonblank target IDs. Omission means
        the document has no outgoing edges for this relation.

    Returns
    -------
    dict of str to set of str
        Each source ID maps to the IDs it references, including any
        targets absent from the supplied frontmatter.

    Raises
    ------
    ValueError
        If any source ID is missing, invalid, or duplicated, or any
        present relation field is not a list of nonblank strings.
        Source IDs are checked before relation fields.
    """
    sources: dict[str, tuple[int, Mapping[str, object]]] = {}
    for position, frontmatter in enumerate(frontmatters, start=1):
        source = frontmatter.get(source_key)
        if not isinstance(source, str) or not source.strip():
            raise ValueError(
                f"Frontmatter #{position}: expected a nonblank string in {source_key!r}"
            )
        if source in sources:
            previous_position, _ = sources[source]
            raise ValueError(
                f"Duplicate {source_key!r} value {source!r} "
                f"in frontmatter #{previous_position} and #{position}"
            )
        sources[source] = (position, frontmatter)

    dependency_map: dict[str, set[str]] = {}
    for source, (_, frontmatter) in sources.items():
        targets = frontmatter.get(relation_key, [])
        if not isinstance(targets, list) or any(
            not isinstance(target, str) or not target.strip() for target in targets
        ):
            raise ValueError(
                f"Document {source!r}: expected a list of nonblank strings in {relation_key!r}"
            )
        dependency_map[source] = set(targets)
    return dependency_map


def build_dependency_graph_from_files(
    path_to_dir: Path, source_key: str, relation_key: str, pattern: str = "*.md"
) -> nx.DiGraph[str]:
    """Build a directed graph for one frontmatter relation.

    Parameters
    ----------
    path_to_dir : pathlib.Path
        Directory in which to search.
    source_key : str
        Field containing the source document ID.
    relation_key : str
        Field containing the list of target IDs.
    pattern : str, optional
        Glob pattern for selecting Markdown files.

    Returns
    -------
    networkx.DiGraph
        Graph whose edges point from declaring documents to referenced IDs.

    Raises
    ------
    NotADirectoryError
        If the supplied path is missing or is not a directory.
    EmptyDirectoryError
        If no regular file matches the pattern.
    OSError
        If a matching file cannot be opened or read.
    ValueError
        If frontmatter has an invalid shape, an invalid or duplicate source
        ID, or invalid target IDs.
    yaml.YAMLError
        If a frontmatter block contains invalid YAML.

    See Also
    --------
    validate_dependency_dag : Check that a relation has no directed cycles.
    """
    frontmatters = extract_frontmatter_from_files(path_to_dir, pattern)
    dependency_map = build_dependency_map(
        frontmatters, source_key=source_key, relation_key=relation_key
    )
    graph: nx.DiGraph[str] = nx.DiGraph()
    graph.add_nodes_from(dependency_map)
    graph.add_edges_from(
        (source, target) for source, targets in dependency_map.items() for target in targets
    )
    return graph


def validate_dependency_dag(graph: nx.DiGraph[str]) -> None:
    """Check that a directed graph of document IDs is acyclic.

    Check acyclicity first. Search for a cycle to report only if the
    graph fails that check.

    Parameters
    ----------
    graph : networkx.DiGraph
        Directed graph with string document IDs as nodes.

    Raises
    ------
    DependencyCycleError
        If the graph contains a directed cycle, including a self-dependency.
        The exception's ``cycle`` attribute repeats the starting ID at the end.
    """
    if nx.is_directed_acyclic_graph(graph):
        return

    edges = nx.find_cycle(graph)
    cycle = tuple(source for source, _ in edges) + (edges[-1][1],)
    raise DependencyCycleError(cycle)
