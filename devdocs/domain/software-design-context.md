# Observations on Software Development and Project Knowledge

> **Status:** working conceptual assessment  
> **Revised:** 21 October 2026  
> **Purpose:** explain conditions under which software development produces learning, commitments, and knowledge that later work depends on.  
> **Audience:** readers examining software work before selecting a development practice or knowledge-management solution.  
> **Scope:** a focused account of iteration, reasoning, and continuity; not an exhaustive theory of software engineering.

Software is not built in exactly the same way as a bridge, a house, or a car. Many software artifacts can be modified, executed, compared, and discarded at relatively low cost. This makes trial, observation, and revision productive parts of design. The consequences of a change still depend on what has come to rely on it.

This note offers working observations and distinctions. The [scenarios](software-design-scenarios.md) illustrate their possible consequences; the [debt](software-project-debt.md), [agent](llms-and-coding-agents-in-software-project-knowledge.md), and [tools](software-project-knowledge-tools.md) notes examine different aspects. The [glossary](glossary.md) provides concise meanings for shared terms. These links provide detail rather than prerequisites for reading this account.

## Implementation is also investigation

A limited implementation, prototype, benchmark, or branch can answer questions that are difficult to settle entirely in advance: whether a dependency expresses a required case, an abstraction remains usable, or a suspected bottleneck exists. Implementation constructs a candidate system and produces observations about the problem and solution.

The problem and solution can therefore co-evolve. An experiment may expose a missing requirement, an unnecessary constraint, an incompatible combination of goals, or a need that was initially expressed through an unsuitable feature request. The next iteration may change the problem statement as well as the implementation.

An experiment's informative value remains bounded by its conditions. A successful benchmark establishes something about its workload and environment. A convenient prototype does not establish long-term maintainability. A failed alternative can preserve useful negative knowledge even when none of its code survives.

Effective iteration depends on using those results: what was tried, under which conditions, what was observed, and which questions remain. Repeating an experiment under changed conditions may be valuable; repeating it because its existence was forgotten may provide little new information. [S2](software-design-scenarios.md#s2--a-feature-idea-compresses-a-need-and-a-proposed-solution) and [S12](software-design-scenarios.md#s12--retrieved-knowledge-changes-a-current-proposal) illustrate this distinction.

## Failure costs and feedback speeds are uneven

Discarding an isolated experiment may be inexpensive. A destructive migration, broken public interface, production incident, or loss of persisted data may be costly. “Cheap to change” needs its boundary stated: the edited files, deployed system, downstream users, and external commitments can have very different costs.

Feedback also arrives at different speeds. Compilation, type checking, and selected tests can reveal problems quickly. Review, operational use, requirements drift, and accumulated maintenance effort can reveal others much later. A system that works under one observation can remain problematic under another.

Fast feedback helps detect some errors while choices remain easy to change. It can also bias attention toward properties that are easy to observe. Maintainability, appropriateness under future conditions, and shared understanding may receive less scrutiny because their consequences appear slowly. Proxies and periodic review can help, but a proxy is not the property itself.

The effect of an executable check also depends on technical reliability, relevance, and participant response. An unreliable check may be ignored; a reliable check may enforce an obsolete expectation. [S6](software-design-scenarios.md#s6--an-executable-check-challenges-an-accepted-assumption) explores those paths.

## Choices become commitments

A choice becomes harder to revise as stored data, interfaces, components, users, operational procedures, tests, and explanations depend on it. Reversibility is gradual. A provisional label does not prevent dependent work from turning a temporary choice into a practical commitment.

Containment can be engineered. Encapsulation, adapters, and modular boundaries can make an implementation replaceable by placing dependence on an interface instead. This relocates commitment: the internal mechanism becomes easier to replace while the boundary acquires dependents and becomes more consequential.

Three questions help separate the mechanisms: how difficult the choice is intrinsically to revise, how far its dependencies have propagated, and how effectively boundaries contain that propagation. These questions apply to assumptions and working practices as well as code.

Planning can consequently organize learning and commitment: identify desired outcomes, uncertainties, constraints, affordable experiments, and decisions whose consequences need examination before they spread. This does not require predicting the complete final system. [S15](software-design-scenarios.md#s15--project-or-subsystem-inception-concentrates-provisional-choices) illustrates the density of provisional choices at inception.

## Decisions and rationale are situated

Technical information rarely determines a unique appropriate choice. Decisions depend on goals, priorities, time, expertise, constraints, available evidence, acceptable risk, and expectations about future change. New observations or changed circumstances may justify revising a decision that was reasonable when made.

The fact that a decision occurred, the support for its rationale, its current acceptance, and its present applicability are distinct. A record can accurately describe an earlier decision after its guidance ceases to apply. Conversely, new evidence may show that a premise was already mistaken at the time. [S5](software-design-scenarios.md#s5--a-contextual-change-reopens-an-earlier-decision) and [S13](software-design-scenarios.md#s13--investigation-refutes-the-rationale-of-an-earlier-decision) distinguish these histories.

An [assumption](glossary.md#assumption) is a proposition relied upon as a premise within a context; its evidential support is a separate matter. An [instruction](glossary.md#instruction) directs action. A decision can establish an instruction because it relies on an assumption, but the directive alone does not preserve why it was appropriate.

## Structure can emerge without an explicit decision

Framework defaults, generated scaffolding, copied patterns, repeated local convenience, and prototypes that remain in use can shape architecture without a global comparison of alternatives. An incomplete migration can produce a similar present structure through a different history.

Current code and version history provide valuable witnesses of state and change, but they do not necessarily explain goals, considered alternatives, uncertainty, objections, or authority. Missing rationale can mean that an explanation was lost, that a process stopped, or that no explicit rationale ever existed.

Those histories require different interpretations. Recovery from records or interviews may support a historical account; inspection may instead support a present explanation of consequences. A plausible interpretation of current structure should not be presented as an earlier decision that nobody can substantiate. See [S7](software-design-scenarios.md#s7--inspection-reveals-architecture-produced-by-accretion), [S9](software-design-scenarios.md#s9--deliberation-produces-a-decision-but-no-durable-artifact), and [S10](software-design-scenarios.md#s10--a-migration-begins-and-remains-half-finished).

## Project knowledge is distributed and partly implicit

Relevant knowledge can be carried by source code, tests, benchmarks, issues, reviews, commit messages, design records, conversations, external references, operational records, and people's understanding. These sources have different roles. A requirement expresses an expected outcome; an observation reports what was seen; evidence supports a claim; a proposal offers an action; and a decision records a selection.

Some knowledge has never been articulated. A maintainer may choose an in-memory representation because they expect small datasets, without recognizing that expectation as a premise worth stating. Questions about when the design would fail or what would justify another choice can help elicit it. This is different from retrieving an already recorded premise.

Not all expertise can be fully verbalized. Learning, pairing, examples, and practical work can transfer understanding that a document alone does not convey. A handover's adequacy may become visible only when a successor attempts a real task, as in [S14](software-design-scenarios.md#s14--a-contributor-leaves-and-concentrated-knowledge-becomes-unavailable).

Externalization makes scrutiny possible, but it does not establish accuracy or comprehension. A record may contain a tentative belief, a disputed conclusion, or an interpretation rather than an observation. In this collection, [project knowledge](glossary.md#project-knowledge) is a broad account of what participants know, rely on, and preserve, not a guarantee that all recorded text is true.

## Preservation and reuse are separate activities

Keeping an account available is one part of continuity. Later work must create a reason to search, retrieve relevant material, interpret its provenance and standing, and assess whether its conditions still apply. A found record can prevent repetition, reveal an earlier error, or be confidently misapplied.

Historical accuracy and present applicability must therefore be examined separately. A later challenge to one premise can reopen attention without automatically invalidating every decision connected to it. Other reasons may still support the choice.

Relationships also matter. A hyperlink may mean that a record supports, challenges, implements, supersedes, or merely mentions another. Explicit descriptions can reduce ambiguity; their maintenance introduces its own work. There is no assumption here that a complete formal graph is necessary or affordable.

## Checks and explanations provide different support

Types, assertions, tests, architecture rules, policies, and benchmarks can evaluate selected properties. Prose can explain why those properties matter, what assumptions they approximate, and what response a failure should prompt. A failing check is an observation that requires interpretation, not an explanation of its own cause.

Checks can also examine records themselves: required fields, permitted states, or specified relationships. Such [rule conformance](glossary.md#rule-conformance) is different from establishing the truth or adequacy of the represented rationale. A fully populated decision record can contain a mistaken premise; a sound observation can appear in an incomplete record.

Executable expectations and explanations can be linked so that a failed check draws attention to its underlying purpose. They can also drift apart. Disabling a check, changing its threshold, or superseding the decision behind it may require reconsidering the other records, rather than assuming their lifecycles close together.

## Capture and maintenance consume attention

Exhaustive capture is costly and can produce more material than participants can use. Minimal structure can leave a large archive difficult to interpret. Demanding precision while a question is still unclear can encourage false certainty or suppress capture entirely.

One possible heuristic is to retain reasoning when there is observable cognitive friction or a commitment boundary: a seriously considered alternative, an external lookup, explicit uncertainty, disagreement, persisted data, a shared interface, or a new dependency. These are signals available during work, rather than predictions of what will matter years later. They do not guarantee complete coverage: conventional choices can be consequential without hesitation, and unfamiliar local choices can attract disproportionate attention.

Later inspection remains important for inherited and emergent structures. A short witness, an unresolved question, or a link may be sufficient initially; deeper qualification can follow when a concrete task requires it. Whether that practice is worthwhile depends on the effort of capture, review, retrieval, and maintenance as well as the benefit.

The [debt note](software-project-debt.md#knowledge-preservation-can-create-its-own-debt) examines how deferred work and documentation burdens accumulate. The [tools landscape](software-project-knowledge-tools.md) describes existing responses. Neither assumes that every difficulty requires more documentation or a new tool.

## Limits of this account

These are conceptual observations illustrated by plausible project situations. They do not establish how frequently each mechanism occurs, prescribe one lifecycle, or provide a complete development methodology. Project size, criticality, organizational setting, and kinds of expected change affect their importance.

The central question is whether learning from work remains available and usable when later action needs it, at an affordable cost. Responses may involve changing the implementation, simplifying a commitment, sharing expertise, improving records, adjusting a process, or accepting a bounded burden.
