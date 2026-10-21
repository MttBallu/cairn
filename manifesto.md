---
status: draft
---

# Cairn Manifesto

## Software engineering advances through experimentation

Software is not built in exactly the same way as a bridge, a house, or a car. Many of its artifacts can be modified, executed, compared, and discarded at relatively low cost. Substantial alternatives can be explored in hours. This makes experimentation, trial and error, and successive refinement powerful ways to develop a system.

Implementation also produces knowledge. Building a candidate solution reveals missing requirements, inadequate abstractions, unexpected behavior, and possibilities that were difficult to anticipate. The understanding of the problem and the shape of the solution evolve together.

We want to preserve this capacity for rapid exploration. Its consequences still matter: persisted data, shared interfaces, deployed systems, and user expectations turn provisional choices into commitments. Effective iteration requires knowing what has been learned and what others now depend on.

## Each iteration should build on what the project has learned

Why did we choose this approach? What did we try? What failed, and under which conditions? What did the result teach us? What should change in the next iteration?

These questions connect experimentation to cumulative progress. Their answers are scattered across code, tests, discussions, reviews, documents, and people's memories. Some remain implicit. Others are recorded but become difficult to find or cease to apply.

When that continuity breaks, a project can repeat failed experiments, reopen settled questions without their evidence, or preserve a choice after its justification has disappeared. A rejected alternative may contain valuable learning even when none of its code survives. A successful implementation may outlive the assumptions that made it appropriate.

Project knowledge should help participants interpret new observations and decide what to do next. Its value depends on being retrieved, understood, and assessed in the situation where it is used.

## Make project knowledge explicit and checkable

Cairn aims to help the people who build and maintain a software project articulate, connect, and challenge the knowledge it relies on. This includes goals, scope, requirements, assumptions, constraints, decisions, evidence, and unresolved questions.

An important premise may be obvious to one contributor and invisible to everyone else. Making it explicit allows the project to examine its support, recognize what depends on it, and reconsider a decision when conditions change. An expectation that data will remain small, for example, can determine a design without ever appearing in its explanation. Articulating that assumption makes the conditions for reconsidering the design visible.

Cairn should also provide checks against declared rules. A project can specify what information a record must contain, which states it can take, and what support is required before it is treated as accepted guidance. Cairn can then check the explicit records and relationships against those expectations. Where a condition can be checked mechanically, the result should be reproducible and its justification inspectable.

Those checks have defined scope. Conformance to a rule, evidence supporting a claim, and acceptance of a decision remain distinct. Uncertainty and incomplete investigation must be expressible accurately. A plausible reconstructed rationale must remain distinguishable from an account supported by historical evidence.

We should reuse established engineering practices before inventing new ones. Scope, requirements, evidence, and acceptance criteria should retain their meaning across changes of agent or tool. Shared expectations can remain stable while the procedures used to meet them evolve.

## Work with the existing development environment

Cairn is intended to complement Git, GitHub/GitLab, automated tests, and existing project documents such as requirements and design records. These tools and artifacts already preserve useful knowledge and support established workflows. Source records should remain authoritative in the systems that own them.

Cairn's contribution should be to connect relevant context, reasoning, evidence, and change across those records. It should make their relationships and current applicability easier to inspect without requiring parallel systems for repository history, issue tracking, or code review.

We are exploring a command-line interface as the main entry point, supported by AI companions using skills that package instructions and resources for particular activities. The companions help maintainers investigate, articulate knowledge, and review work; their edits to project files require permission. Maintainers retain responsibility for assessing claims and accepting commitments. The particular interfaces and integrations remain open to revision.

## Give coding agents usable context and guidelines

Coding agents participate in the same iterative process. They need relevant goals, scope, requirements, constraints, examples, and validation procedures to work appropriately. The availability of project knowledge matters alongside the ability to retrieve it and judge its applicability.

The relationship works in both directions. Project knowledge guides an agent's actions; the resulting changes, experiments, failures, and unresolved questions can contribute to the project's next iteration. Generated explanations are proposals whose source evidence and review status must remain visible.

Agents can accelerate experimentation and help maintainers develop understanding. They can also produce changes faster than people can meaningfully review them. Greater velocity can amplify both useful learning and unexamined commitments.

Cairn should support this feedback loop through faithful context, inspectable evidence, explicit expectations, and clear responsibility. Its purpose should remain meaningful as the agents performing the work change.

## Keep knowledge management sustainable

When work needed to sustain a project is deferred, debt can accumulate. Its interest is paid through repeated investigation, slower changes, operational effort, and failures. Delivering the current task can leave the underlying obligation intact.

Cairn must account for the burden it introduces. Recording, reviewing, finding, and maintaining project knowledge consume attention. Generating more artifacts than maintainers can meaningfully review can increase comprehension debt: the gap between the understanding they need to take responsibility for a system and the understanding they possess.

We therefore favor selective capture, source references, and review focused on the knowledge needed for a particular task. An unreviewed conversation or log can remain available as evidence without becoming accepted guidance. Historical evidence can be preserved while obsolete guidance is retired. The effort required to maintain this knowledge should be justified by its use in actual work.

Success means helping maintainers assess a change, recover reasoning, transfer responsibility, or revise a commitment with reliable evidence and less repeated reconstruction. These outcomes must be considered alongside the cost of achieving them.

Cairn's continued relevance is a hypothesis to test. As existing tools improve, its role may become narrower or take a different form. We will judge its contribution by whether it helps projects learn from their iterations and retain the understanding needed to evolve responsibly.
