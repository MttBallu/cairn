# Domain Revision and Consistency Review

> **Status:** revision completed; collection ready for maintainer review  
> **Date:** 21 October 2026  
> **Purpose:** record the revision performed, its consistency checks, and its limits.  
> **Scope:** five domain notes, their index and glossary, preserved inputs, and a deferred-material buffer.

## Result and navigation

The [domain index](../domain/README.md) is the entry point. It links the five revised notes, the [glossary](../domain/glossary.md), and all twenty-two scenarios. Development material remains under `devdocs/`; `docs/` remains reserved for user documentation. The [working agreements](../documentation-and-github-working-agreements.md) are included as the governing working reference supplied for this revision.

The collection describes software development and project knowledge independently of Cairn. Product and modelling proposals are preserved in a [dedicated buffer](../product/deferred-material.md) for later triage. Their preservation does not accept them as requirements or select a product architecture.

## Changes by document

| Document | Revision performed |
| --- | --- |
| [Context](../domain/software-design-context.md) | Reorganized around learning, commitment, implicit knowledge, reuse, checks, and preservation costs; clarified assumptions as relied-upon premises and qualified capture heuristics |
| [Scenarios](../domain/software-design-scenarios.md) | Preserved S1–S15 and their distinct mechanisms; aligned generic participants and supersession terminology; added experiment-driven clarification of a need in S2 and implicit-premise/record-conformance distinctions in S3; shortened the cross-scenario synthesis |
| [Debt](../domain/software-project-debt.md) | Removed product framing and implications; preserved debt, principal, interest, comprehension, legitimate compatibility obligations, and differentiated responses; generalized documentation-induced debt and qualified prescriptive wording |
| [Agents](../domain/llms-and-coding-agents-in-software-project-knowledge.md) | Preserved A1–A7; clarified guidance, authority, delivery versus reliance, candidate accounts, and capture economics; removed the proposed service API and model obligations; qualified review-independence and adoption claims |
| [Tools](../domain/software-project-knowledge-tools.md) | Replaced the long product-oriented report as the domain entry point with a concise, source-linked synthesis; retained the full report separately; bounded claims about capability gaps and reuse |
| [Glossary](../domain/glossary.md) | Created working definitions as level-two subsections with internal links; stated that entries are contextual roles rather than a decided formal model |
| [Index](../domain/README.md) | Added roles, reading guidance, source limitations, and direct links to both scenario sets |

## Terminological consistency

The editorial pass reconciled the following distinctions across the notes:

- **Assumption and support:** an assumption identifies a relied-upon premise; its support is assessed separately. It is not defined by an automatic lack of evidence.
- **Assumption and instruction:** a qualified premise differs from a direction to act. Effective instructions need not be faithful accounts of their rationale.
- **Participant and coding agent:** the scenario corpus uses participant generically; the agent note distinguishes the configured system, model, and situated run.
- **Witness, interpretation, and evidence:** a record can witness an event or state while its interpretation and support for a particular claim require assessment.
- **Acceptance and truth:** endorsement does not establish truth, implementation, or continuing applicability.
- **Historical accuracy and applicability:** an earlier rationale can be accurately recorded but obsolete; a later refutation can instead expose an originally mistaken premise.
- **Supersession, refutation, and retraction:** replacing guidance does not alone show the earlier rationale was unsound; challenging a premise and withdrawing endorsement remain different acts.
- **Rule conformance and substantive support:** a record can satisfy a declared structure without supplying adequate evidence for its claims.
- **Local closure and related obligations:** closed issues, approved reviews, completed changes, and remaining preventive work retain different meanings.
- **Debt and interest:** recurring additional work differs from reducing an underlying obligation; legitimate support costs, legacy, and ordinary learning are not automatic debt diagnoses.
- **Delivery and reliance:** availability, requests, responses, citations, and reported reliance are separate observations or assertions.
- **Independent review:** another run, model, or human approval does not by itself demonstrate a materially independent assessment.

No remaining contradiction was identified in these uses during this editorial review. The meanings remain working vocabulary, open to challenge by additional situations; they do not constitute a validated ontology.

## Boundary and coverage review

The current domain files contain no references to Cairn and no residual operations such as `begin_run`, `find_applicable_assumptions`, or `propose_assumption`. The prose was also examined for unnamed product requirements: no assumption store, schema, service architecture, or mandatory lifecycle is selected.

Scenarios remain illustrations, not product use cases or measurements of prevalence. The general corpus retains the distinctions among accretion without a decision, a lost decision account, and an interrupted migration. Both knowledge production and later retrieval remain represented. Additional responses can involve learning, implementation changes, organizational arrangements, or accepting a bounded burden.

The agent and debt notes retain their different questions. Detailed agent failure mechanisms are explained in the agent note; the debt note examines their deferred costs. The tools assessment describes existing affordances without treating one product as their necessary successor.

## Source and proposal preservation

The five [source editions](source-editions/2026-10-21/README.md) were copied before revision. Their Markdown bytes are unchanged. The [source manifest](source-editions/2026-10-21/source-manifest.json) records SHA-256 values and sizes, all rechecked against the snapshots.

The buffer retains five substantial original extracts: the tools report's product recommendations and conclusions, the agent note's proposed MCP interface and modelling questions, and the debt note's product implications. Each extract links to its source edition. Other mixed framing remains recoverable in the complete snapshots, rather than being promoted into new requirements or discarded.

The full tools source retains its original source ledger and research limitations. Its original product recommendations are historical material, not current domain conclusions. The maintained synthesis is the primary reading route.

## Citation and evidence review

Selected current examples were checked against primary documentation: AGENTS.md, Agent Skills, MCP, Git history, GitHub Issues, GitLab merge requests, Backstage catalog and search, dependency alerts, architecture checks, OSLC, and PROV-O. ADR, RFC, assurance, and postmortem sources were also inspected. The debt and comprehension references retain their conceptual or situated empirical standing.

The revised notes remove the adoption-count argument for sustained rationale capture, avoid universal absence claims about mainstream tools, and distinguish documented features from effectiveness in use. Older design-rationale and traceability research is not presented as a 2026 industry census. The student study is not treated as an industry-wide causal estimate. The original source dates were retained; the revision date does not imply that every historical study or product in the full report was re-audited.

This is an editorial consistency and source-scope review, not an independent validation of the conceptual account or a new systematic literature review.

## Mechanical checks

The final checks cover relative Markdown file links and heading anchors, the two complete scenario identifier sets, level-two glossary entries, balanced code fences, duplicate heading labels in the current domain notes, product-name/API leakage, paragraph formatting, and source snapshot hashes. Verbatim historical inputs retain their original formatting.

| Check | Final result |
| --- | --- |
| Current domain files | 7: five notes, index, and glossary |
| Relative file links and heading anchors | 199 checked; no unresolved targets |
| General scenario identifiers and titles | S1–S15 retained in order |
| Agent scenario identifiers and titles | A1–A7 retained in order |
| Glossary structure | 58 entries, all at `##` level |
| Product-name/API leakage in domain files | None detected; semantic review also performed |
| Duplicate heading labels in current domain files | None |
| Fences, paragraph wrapping, and blank-line checks | Passed |
| Original source snapshots | 5 SHA-256 matches |

## Deferred work

The [buffer](../product/deferred-material.md) remains to be triaged into product questions, accepted scope, rejected ideas, experiments, or implementation options. This revision does not choose among those responses. It also does not decide the ultimate formal representation of glossary concepts.

The resulting files are prepared for repository review with their relative structure intact. GitHub issue and pull-request references can be attached when that repository work is created; no such references are invented here.
