# Documentation and GitHub Working Agreements

> **Status:** proposed initial agreement  
> **Date:** 21 October 2026  
> **Purpose:** establish a small set of rules for maintaining Cairn's project knowledge and coordinating work on GitHub.  
> **Scope:** repository documentation, discussions, issues, pull requests, and agent participation.

These agreements apply with ordinary Markdown, Git, and GitHub. Their use does not depend on Cairn software or a completed knowledge model.

## 1. Give every document a clear responsibility

A document should make its purpose, scope, and intended reader clear near the beginning. It should be possible to explain what belongs there and what belongs elsewhere. Its status should distinguish an unfinished draft or proposal from current guidance or a historical record. Plain language is sufficient; a fixed metadata template is not required.

## 2. Separate the domain, the product, and the project's working practices

Domain documents describe software development and project knowledge management: situations, activities, problems, scenarios, and existing practices. They must not mention Cairn or prescribe its capabilities. Product documents explain which problems Cairn chooses to address and how. Working-practice documents explain how contributors develop Cairn. Connections between these areas should be explicit references rather than mixed responsibilities.

Keep development knowledge under `devdocs/`, including domain notes, product design, research, decisions, and development working practices. Reserve `docs/` for documentation addressed to Cairn users, such as tutorials, how-to guides, explanations, and reference material. The README and manifesto remain project entry points at the repository root.

## 3. Make each document understandable in its own scope

Define enough context for the intended reader to understand the document without reconstructing a conversation or reading an unspecified collection of notes. Explain essential terms and use the shared glossary consistently. Use links for supporting detail and related material. An index should explain the collection's organization and suggested reading order without creating circular prerequisites.

## 4. Preserve the standing and support of claims

Distinguish observations, assumptions, interpretations, proposals, requirements, and decisions. Cite sources for externally supported claims and link important project conclusions to their evidence or deliberation. Keep uncertainty and unresolved disagreement visible. Historical accuracy, current applicability, and acceptance by maintainers are separate questions. Merging a document does not turn every statement it contains into an established fact.

## 5. Give current guidance a primary home

Maintain the current account of a topic in an identifiable document or source system. Reference it from related material instead of maintaining competing copies. When guidance changes, make the change and its consequences visible; preserve useful history through Git and linked records. Keep filenames stable and retain identifiers used to reference scenarios or other persistent material.

## 6. Use GitHub features according to the work at hand

| Surface | Default responsibility |
| --- | --- |
| Discussions | Explore questions, compare interpretations, and deliberate while the framing or outcome remains open |
| Issues | Track bounded problems, investigations, and changes, with an expected outcome and criteria for assessing completion |
| Pull requests | Propose and review concrete changes to repository documents or code |
| Repository documents | Maintain the current synthesis, guidance, requirements, and consequential decision records |

These are defaults, not a mandatory sequence. A discussion can remain unresolved or produce several investigations. Small changes need not acquire a separate issue solely to satisfy a process.

## 7. Connect deliberation, changes, and outcomes

Link relevant discussions, issues, pull requests, and documents. Record consequential conclusions and their rationale where later contributors can find them, using a separate decision record when useful. Review changes against the affected document's responsibility and the task's intended outcome. When closing work, state what was completed, deferred, rejected, or left unresolved. Closing one item does not establish that related obligations are complete.

AI companions may help investigate, draft, and review. Their proposed interpretations remain distinguishable from source evidence and accepted conclusions. Project edits require maintainer permission; maintainers remain responsible for accepting changes and commitments.

## 8. Keep the process proportionate and revisable

Capture enough knowledge to support real investigation, review, and handover. Add structure or automation when an observed need justifies its cost. Write concise Markdown, with one paragraph per line and no manual wrapping inside prose paragraphs. Avoid requiring exhaustive capture or a separate record for every local choice. Review these agreements when experience exposes friction: Cairn's own use is evidence to examine, not proof that its approach fits every project.
