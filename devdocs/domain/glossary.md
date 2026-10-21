# Software Development and Project Knowledge: Glossary

> **Status:** working vocabulary  
> **Revised:** 21 October 2026  
> **Purpose:** give concise, consistent meanings to terms used in the [domain notes](README.md).  
> **Scope:** ordinary analytical language for software work and project knowledge, not a formal model or an exhaustive software-engineering dictionary.

Entries describe roles and distinctions, not mutually exclusive classes. The same statement can be investigated as a hypothesis, relied upon as an assumption, and later challenged by evidence. Short definitions are supplemented by the linked explanatory notes. The vocabulary can evolve when an example exposes an inadequate distinction.

## Project knowledge

The understanding, statements, practices, and supporting material relevant to explaining, performing, assessing, or evolving project work. This broad phrase includes provisional beliefs and tacit expertise; it does not certify every recorded statement as true. See the [context account](software-design-context.md#project-knowledge-is-distributed-and-partly-implicit).

## Implicit knowledge

Understanding or a relied-upon premise that has not been articulated in the relevant shared record. Some implicit knowledge can be elicited; some expertise is difficult to express fully. Absence from a record does not establish absence from a participant's understanding.

## Explicit knowledge

Knowledge or a belief articulated in an inspectable form, such as an explanation, diagram, convention, or check. Being explicit makes examination possible; it does not establish truth, completeness, shared understanding, or current applicability.

## Claim

A statement presented as holding within some context. Its assertion, support, and acceptance are separate matters. Requirements and instructions express normative expectations and should not silently be treated as observations about what already holds.

## Assumption

A proposition relied upon as a premise for reasoning or action within a context. Its support can range from tentative expectation to strong evidence. Calling it an assumption identifies reliance, not a particular level of confidence. Distinguish a [hypothesis](#hypothesis), which is being investigated, and an [instruction](#instruction), which directs action.

## Hypothesis

A proposition under investigation. It may motivate an experiment without yet being accepted or relied upon in production. A hypothesis and an assumption can share wording while playing different roles.

## Need

An outcome or difficulty that matters to someone in a situation. A suggested implementation may express one response to a need without uniquely identifying it. See [S2](software-design-scenarios.md#s2--a-feature-idea-compresses-a-need-and-a-proposed-solution).

## Requirement

An explicitly stated outcome, capability, or property sought or required of a system or activity. Its source, scope, and acceptance status matter: a candidate requirement is not automatically an accepted obligation. Distinguish a requested solution from the underlying [need](#need).

## Constraint

A condition that limits acceptable choices within a scope. It may originate in an external obligation, environment, or project decision. A constraint on intended behavior is distinct from an observation that existing behavior satisfies it.

## Instruction

A direction to perform, avoid, validate, or escalate an action. An instruction may follow from a decision and its assumptions, but it does not replace their explanation. See the [agent discussion](llms-and-coding-agents-in-software-project-knowledge.md#guidance-needs-meaning-scope-and-authority).

## Proposal

A possible course of action presented for consideration. Discussion, implementation, and acceptance are distinct from making the proposal. A proposed experiment is not evidence that the experiment has occurred.

## Decision

A selection or commitment made by a participant or group within an identified scope. Its authority, status, rationale, and implementation can differ. Some consequential structures emerge without an explicit decision event.

## Rationale

The reasons offered for a choice, including relevant goals, alternatives, assumptions, trade-offs, and evidence. A present justification or reconstructed explanation is not automatically an accurate account of the reasons held when the choice was made.

## Convention

A recurring or expected practice within a project. It may be deliberately adopted, inherited, or emerge through repetition. Its presence in code does not establish an explicit decision or universal enforcement.

## Commitment

A choice or undertaking on which other work, systems, people, or expectations rely. Commitment can accumulate gradually through interfaces, stored data, dependencies, and use. It need not originate in an explicit promise. See [reversibility](software-design-context.md#choices-become-commitments).

## Context

The circumstances relevant to interpreting a statement or activity: goals, participants, available information, system state, environment, time, and constraints. Context can change independently of the wording of a record.

## Scope

The boundary within which a statement, rule, responsibility, or activity applies. A claim may be well supported for one workload, component, version, or task and inappropriate outside it.

## Artifact

A produced or maintained object used in project work, such as code, a document, an issue, a diagram, or a test. An artifact can contain several kinds of statements and have several uses.

## Record

An artifact or part of one retained as an account of a statement, event, state, or outcome. A record's existence does not establish the accuracy of its content or its authority for current action.

## Witness

An observation or record that bears on what occurred or existed: for example, a diff, execution log, or transcript. A witness is partial and has its own reliability and scope. Its interpretation as [evidence](#evidence) for a particular claim requires further judgment.

## Observation

Something noticed or measured under particular conditions, or the reported result of doing so. Distinguish the observation from an explanation of its cause and from the record used to communicate it.

## Evidence

Material used to support or challenge a particular claim through an articulated relationship. The same artifact can be evidence for one claim without supporting another. A passing test, for example, supports a bounded behavioral expectation under its conditions, not every claim about the system.

## Interpretation

An account of what observations or records mean or how they relate. It can be useful while remaining provisional. Repetition or fluent wording does not turn an interpretation into independent evidence.

## Provenance

Information about the origin, production, derivation, and attribution of a record or claim. Provenance supports investigation of reliability and history; it does not by itself establish truth or current applicability.

## Support

The reasons and evidence bearing on a claim, together with their strength and limitations. Support can change without changing the claim's wording or the project's recorded acceptance of it.

## Acceptance

A participant's or project's stance of endorsing a claim, proposal, decision, or result for a specified purpose. Acceptance may be conditional and authority-dependent. It is distinct from truth, implementation, release, and lasting applicability.

## Historical accuracy

How faithfully a record describes the earlier circumstances, events, or beliefs it purports to describe. A historically accurate decision record can remain accurate after its guidance ceases to apply.

## Current applicability

Whether a statement, decision, or practice bears appropriately on the present situation. It depends on relevant conditions and scope, not merely on a document's accepted status. See [S5](software-design-scenarios.md#s5--a-contextual-change-reopens-an-earlier-decision) and [S12](software-design-scenarios.md#s12--retrieved-knowledge-changes-a-current-proposal).

## Rule conformance

Satisfaction of specified rules by a representation, artifact, or state. The word “valid” needs its rule and scope stated. Conformance can be mechanically checked for an expressible rule without establishing that the underlying claim is true, sufficiently supported, or useful.

## Executable check

A procedure that evaluates a specified property and produces an observable result under stated conditions. Examples include tests, assertions, type checks, policies, and benchmarks. Its reliability, coverage, current relevance, and rationale require separate assessment.

## Participant

A person, group, or software system taking part in an activity. This is the generic term in the notes. “Human participant” and “coding agent” are used when the distinction affects interpretation or responsibility.

## Maintainer

A participant with responsibility for some part of a project's continued understanding, operation, or evolution. The exact responsibilities and authority vary by project and should not be inferred solely from authorship or repository access.

## Coding agent

A configured software system combining a generative model with task instructions, context, tools, permissions, and a mechanism for pursuing work. The model alone, the configured system, and a particular [agent run](#agent-run) are distinct. See the [agent note](llms-and-coding-agents-in-software-project-knowledge.md#model-coding-agent-and-run).

## Agent run

A situated activity performed by a coding agent against a project state for a particular task, with particular inputs, tools, and permissions. Separate runs can share assumptions and blind spots; separation alone does not establish independent review.

## Delegation

Entrusting work to another participant within some scope. Delegating implementation does not automatically delegate authority to change requirements, accept risk, or revise project policy.

## Permission

Authorization to perform an action within a boundary. Technical capability, granted permission, appropriate action, and decision authority are different matters.

## Decision authority

The standing to make or accept a commitment in a particular scope. Expertise, influence, ownership, and permission can be relevant without being interchangeable with that authority.

## Activity

A situated instance of work, such as an experiment, review, investigation, or implementation. An activity can contribute to more than one process and affect several persistent objects.

## Process

An actual course of related activities that may branch, pause, redirect, resume, or end. It is distinct from a prescribed procedure and from the [lifecycle](#lifecycle) of the objects involved.

## Lifecycle

The meaningful states and transitions of something that persists through activities, such as a proposal, issue, test, convention, or decision. Interacting lifecycles do not acquire one shared global status.

## Status

A stated position in a particular lifecycle or review scheme, such as proposed, accepted, closed, or superseded. Its meaning belongs to that scheme. A status does not automatically establish support or applicability.

## Closure

An ending or disposition within a specified activity or object's lifecycle. Closing a report does not establish that every follow-up is implemented or every related question resolved.

## Condition

An underlying situation in or around the project, such as a defect, changed dependency, or incomplete migration. It can exist before anyone notices it.

## Signal

Something that makes a condition perceptible, such as a report, failed check, recurring pattern, or announced deadline. A signal may receive no recognition or response.

## Stimulus

A signal or event that draws attention to a situation. The term emphasizes its possible initiating role; it does not imply that activity actually follows.

## Recognition

A participant's interpretation of what a signal may indicate. Recognizing a concern is distinct from giving it [uptake](#uptake).

## Uptake

Treatment of a signal or recognized concern as something worth pursuing. Attention, authority, urgency, and available resources affect uptake. A concern may be recognized and still deferred.

## Request

An invitation or demand for a participant to contribute or act. It can initiate discussion, investigation, or implementation without uniquely determining the response.

## Obligation

Something that requires a response within a context, such as a support commitment, release condition, or security requirement. It can exist without an individual request and leave the response strategy open.

## Supersession

Replacement of an earlier decision or guidance by a later one. Replacement does not by itself establish that the earlier rationale was unsound. Changed circumstances are one possible reason.

## Refutation

Evidence or reasoning defeating a claim or part of a rationale within its stated scope. Refuting one supporting premise does not automatically defeat every dependent conclusion if other reasons still support it.

## Retraction

Withdrawal of endorsement of a claim or decision. Retraction changes a stance; it does not erase the historical fact that the statement was made or guided work. See [S13](software-design-scenarios.md#s13--investigation-refutes-the-rationale-of-an-earlier-decision).

## Debt

An accumulated obligation created when work needed for sustainable development or operation is deferred, introducing future cost or risk. Its [interest](#interest) is the additional burden while the underlying condition persists. This is a working analytical metaphor, developed in the [debt note](software-project-debt.md#deferred-work-principal-and-interest).

## Principal

The work currently needed to remove or materially reduce a debt's underlying obligation. It is not a fixed numerical balance: the relevant work can change as dependencies, goals, and evidence change.

## Interest

Additional investigation, coordination, rework, operational effort, or failure cost caused by leaving a debt's underlying condition in place. It may recur during ordinary work or become visible at a later exposure event. Not every possible failure cost will actually be incurred.

## Comprehension debt

The accumulated gap between the understanding maintainers need to take responsibility for a system and the understanding they currently possess. The reference point is their task and responsibility, not knowledge of every implementation detail. See the [debt analysis](software-project-debt.md#implementation-records-and-understanding-are-different-resources).

## Knowledge concentration

Uneven distribution of relevant understanding or access across participants. Concentration and collective insufficiency are distinct: someone may know the answer but be unavailable, or nobody may understand a consequential interaction. See [S14](software-design-scenarios.md#s14--a-contributor-leaves-and-concentrated-knowledge-becomes-unavailable).

## Context delivery and reliance

Records can be available to a client, requested, returned, cited, and reported as relied upon. These are different events or assertions. A delivery trace can establish a request and response without establishing model attention, belief, or causal influence. See the [agent account](llms-and-coding-agents-in-software-project-knowledge.md#context-delivery-does-not-establish-reliance).
