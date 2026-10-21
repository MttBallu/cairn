# Software Development and Project Knowledge

> **Status:** working domain collection  
> **Revised:** 21 October 2026  
> **Purpose:** orient readers within five complementary notes and their shared vocabulary.  
> **Audience:** readers examining software work, knowledge practices, and existing responses before selecting a solution.

The collection describes how software projects learn, commit, preserve understanding, and respond to change. It includes human and agent-assisted work. It does not prescribe a single methodology, establish a complete taxonomy, or imply that every situation requires a new tool.

## Notes and reading path

| Suggested order | Note | Main question |
| --- | --- | --- |
| 1 | [Development context](software-design-context.md) | How do iteration, learning, commitments, and distributed knowledge interact? |
| 2 | [Situations and scenarios](software-design-scenarios.md) | How can those concerns arise, branch, stall, or become visible during actual work? |
| 3 | [Debt](software-project-debt.md) | What obligations and interest costs arise when sustaining work is deferred? |
| 4 | [LLMs and coding agents](llms-and-coding-agents-in-software-project-knowledge.md) | What changes when agents consume project context and produce changes and candidate knowledge? |
| 5 | [Existing tools and practices](software-project-knowledge-tools.md) | What can already be reused, and which judgments or maintenance burdens remain? |

The [glossary](glossary.md) provides concise working meanings. Each entry is a subsection with its own anchor. Each note supplies enough local context to be read independently; the reading path is an orientation, not a prerequisite chain.

A focused reader can start with a situation below, consult its explanatory note, and use the tools assessment to investigate existing responses. The [detailed tools research](../research/source-editions/2026-10-21/software-project-knowledge-tools.md) is available separately as a dated source edition. The concise assessment remains the primary entry point to that topic.

## Scenario navigation

S1–S15 belong to the general corpus. A1–A7 remain in the agent note because they isolate agent-related pressures that can also affect the general situations. The identifiers remain stable; the headings provide direct links.

### General situations

| Identifier | Situation |
| --- | --- |
| [S1](software-design-scenarios.md#s1--a-bug-report-expands-from-correction-to-prevention) | A bug report expands from correction to prevention |
| [S2](software-design-scenarios.md#s2--a-feature-idea-compresses-a-need-and-a-proposed-solution) | A feature idea compresses a need and a proposed solution |
| [S3](software-design-scenarios.md#s3--a-code-review-redirects-implementation-into-design-deliberation) | A code review redirects implementation into design deliberation |
| [S4](software-design-scenarios.md#s4--a-request-for-comments-gathers-input-without-presupposing-a-decision) | A request for comments gathers input without presupposing a decision |
| [S5](software-design-scenarios.md#s5--a-contextual-change-reopens-an-earlier-decision) | A contextual change reopens an earlier decision |
| [S6](software-design-scenarios.md#s6--an-executable-check-challenges-an-accepted-assumption) | An executable check challenges an accepted assumption |
| [S7](software-design-scenarios.md#s7--inspection-reveals-architecture-produced-by-accretion) | Inspection reveals architecture produced by accretion |
| [S8](software-design-scenarios.md#s8--a-production-incident-compresses-decision-time) | A production incident compresses decision time |
| [S9](software-design-scenarios.md#s9--deliberation-produces-a-decision-but-no-durable-artifact) | Deliberation produces a decision but no durable artifact |
| [S10](software-design-scenarios.md#s10--a-migration-begins-and-remains-half-finished) | A migration begins and remains half finished |
| [S11](software-design-scenarios.md#s11--an-ecosystem-change-imposes-a-background-deadline) | An ecosystem change imposes a background deadline |
| [S12](software-design-scenarios.md#s12--retrieved-knowledge-changes-a-current-proposal) | Retrieved knowledge changes a current proposal |
| [S13](software-design-scenarios.md#s13--investigation-refutes-the-rationale-of-an-earlier-decision) | Investigation refutes the rationale of an earlier decision |
| [S14](software-design-scenarios.md#s14--a-contributor-leaves-and-concentrated-knowledge-becomes-unavailable) | A contributor leaves and concentrated knowledge becomes unavailable |
| [S15](software-design-scenarios.md#s15--project-or-subsystem-inception-concentrates-provisional-choices) | Project or subsystem inception concentrates provisional choices |

### Agent-mediated situations

| Identifier | Situation |
| --- | --- |
| [A1](llms-and-coding-agents-in-software-project-knowledge.md#a1--delegated-implementation-produces-opaque-decision-density) | Delegated implementation produces opaque decision density |
| [A2](llms-and-coding-agents-in-software-project-knowledge.md#a2--retrieved-project-knowledge-guides-an-agent) | Retrieved project knowledge guides an agent |
| [A3](llms-and-coding-agents-in-software-project-knowledge.md#a3--project-guidance-conflicts-during-a-run) | Project guidance conflicts during a run |
| [A4](llms-and-coding-agents-in-software-project-knowledge.md#a4--an-llm-assists-human-knowledge-capture) | An LLM assists human knowledge capture |
| [A5](llms-and-coding-agents-in-software-project-knowledge.md#a5--correct-retrieval-leads-to-incorrect-action) | Correct retrieval leads to incorrect action |
| [A6](llms-and-coding-agents-in-software-project-knowledge.md#a6--parallel-agents-create-an-integration-knowledge-gap) | Parallel agents create an integration knowledge gap |
| [A7](llms-and-coding-agents-in-software-project-knowledge.md#a7--a-coding-agent-performs-review) | A coding agent performs review |

## Standing and limits

The context and debt notes offer conceptual framing and working distinctions. The scenarios are constructed illustrations, not measured incidence data. The agent note combines conceptual analysis with bounded source examples. The tools note is a representative, source-linked synthesis, not a claim to cover all products or configurations.

Document status, evidential support, and current applicability remain different judgments. Citations carry their own dates and limits. Selected live format and capability examples were checked during the revision; the historical source editions were preserved rather than silently refreshed.

Questions that expose an inadequate definition or missing situation can motivate a targeted revision. The collection leaves open which practical, organizational, or technical responses are appropriate in a particular project.
