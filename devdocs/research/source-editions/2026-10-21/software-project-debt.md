# Debt in Software Projects

> **Status:** preliminary companion assessment  
> **Date:** 20 October 2026  
> **Purpose:** examine how deferred work creates future obligations and interest costs across software implementation, project knowledge, and maintainer understanding.  
> **Scope:** a working conceptual framing for later investigation, not an exhaustive taxonomy, a debt measurement method, or a proposed Cairn implementation.

This note complements [Observations on Software Design and Development](software-design-context.md), [Software Design Trigger Scenarios](software-design-scenarios.md), [Software-Project Knowledge Tools](software-project-knowledge-tools.md), and [LLMs and Coding Agents in Software-Project Knowledge](llms-and-coding-agents-in-software-project-knowledge.md). Those documents examine learning, commitment, knowledge preservation, and agent participation. The present note adds a temporal and economic question: what costs accumulate when work needed to sustain a project is deferred, and who eventually bears them?

The distinctions below are working analytical tools. Some extend familiar technical-debt language; others separate problems that the same metaphor can otherwise obscure. They do not establish a new ontology or settle Cairn's product boundary.

## Executive assessment

Debt in a software project extends beyond difficult code. It can concern architecture, infrastructure, compatibility mechanisms, verification, recorded project knowledge, and the understanding held by maintainers. These dimensions interact, but their remedies differ.

The central relationship is between **deferred work, an underlying obligation, and interest**. A shortcut may deliver value today while imposing repeated investigation, slower changes, operational effort, or exposure to later failure. Paying those costs does not necessarily remove their cause. Interest can already be paid during ordinary development, long before a cleanup task is opened.

Coding agents make this relationship particularly visible because implementation and explanation can be produced faster than maintainers can inspect and understand them. A working system, passing checks, and a polished account can coexist with substantial gaps in the team's ability to reason about future changes.

For Cairn, this creates both an opportunity and a constraint:

> **Cairn may help maintainers reduce the cost of recovering and applying project knowledge, but it can also increase comprehension debt by generating more artifacts than they can meaningfully review.**

The relevant outcome is therefore the ability to understand and act responsibly, considered alongside the cost of preserving, reviewing, retrieving, and maintaining the supporting knowledge.

## 1. Debt includes interest, not only postponed repayment

For this assessment:

> **Debt is an accumulated obligation created when work needed for sustainable development or operation is deferred, introducing future cost or risk. It carries interest: the additional costs borne while the underlying condition persists, whether repeatedly or when a later event exposes it.**

Interest is central to the metaphor. In [Cunningham's original account](https://c2.com/doc/oopsla92.html), an immature implementation can accelerate delivery, while continuing to work around its limitations consumes time. The deferred consolidation and the continuing friction are related but different costs.

Several elements should therefore be distinguished:

| Element | Meaning |
| --- | --- |
| Underlying condition | The structure, missing knowledge, incomplete transition, or other situation that sustains the obligation |
| Deferred work | The consolidation, validation, migration, explanation, or learning that has not been completed |
| Present benefit | The time, flexibility, delivery, or learning gained through deferral, when such a benefit exists |
| Principal | The work currently needed to remove or materially reduce the underlying obligation |
| Interest | Additional investigation, coordination, rework, operational effort, or failure cost caused by leaving that condition in place |
| Exposure event | A change, incident, handover, or deadline that makes a previously latent cost observable |

For example, a maintainer may repeatedly investigate the same undocumented exception before modifying a component. Each investigation pays interest. Establishing a reliable explanation and making it usable by later maintainers may reduce the underlying knowledge debt. Merely finishing the current modification may leave it intact.

The cost cannot be assumed away because it is absent from the current task estimate. It may be borne later, paid continuously in small amounts, or transferred to other people. However, software debt has no universal repayment schedule: a project may retain a bounded compromise, remove the affected capability, or retire the system. The obligation must be assessed against its actual future exposure.

## 2. Different areas of debt involve different deferred work

The following distinctions identify where a problem is expressed and what kind of work may address it. They are not mutually exclusive categories.

| Area | Typical deferred work | Characteristic interest |
| --- | --- | --- |
| Code | Consolidating duplication, simplifying local mechanisms, clarifying interfaces | Repeated edits, difficult diagnosis, fragile changes |
| Architecture | Revisiting boundaries, dependency directions, or assumptions that no longer fit | Coordination across components, constrained evolution, recurring exceptions |
| Infrastructure | Making environments reproducible, maintaining dependencies, replacing manual configuration | Environment drift, recovery effort, difficult upgrades |
| Deployment, compatibility, and evolution | Providing migration paths, containing compatibility mechanisms, clarifying support boundaries | Parallel maintenance, release constraints, accumulating special cases |
| Verification | Establishing representative checks and validating relied-upon assumptions | Repeated manual validation, uncertain changes, late discovery of failures |
| Project knowledge | Externalizing and maintaining relevant goals, constraints, rationale, evidence, and status | Repeated reconstruction, stale guidance, reopened investigations |
| Comprehension | Developing and sustaining sufficient shared understanding | Slow diagnosis, unsafe changes, dependence on a few people or on repeated agent intervention |

One condition can have several manifestations. An incomplete migration may create architectural complexity, duplicated tests, confusing guidance, and a gap in maintainer understanding. These are useful perspectives on a connected problem, not necessarily separate amounts that can be added together.

The term **technical debt** is sometimes used broadly enough to include several of these areas. This note does not require a universal decision about that vocabulary. Its purpose is to preserve distinctions that change diagnosis or response.

## 3. Compatibility commitments and legacy are not inherently debt

Supporting an older deployment environment can be a deliberate and valuable product commitment. The work required to honor that commitment is part of operating the product. It becomes useful to speak of debt when avoidable burdens accumulate through deferred migration tooling, scattered exceptions, unsupported dependencies, unclear support conditions, or an unfinished transition.

The distinction is between the commitment and the condition under which it is maintained. Removing a compatibility mechanism may reduce implementation complexity while breaking a legitimate obligation to users. A debt assessment must therefore identify what can be changed and who has authority to revise the commitment.

Similarly, **legacy** describes an inherited situation or history, rather than one specific debt mechanism. An old system may be well understood, appropriately bounded, and inexpensive to maintain. A newly generated subsystem can already contain substantial debt.

Age, unfamiliarity, and deviation from a preferred style are consequently insufficient diagnoses. A useful assessment identifies a concrete deferred obligation and the cost or risk it creates.

## 4. Debt can be deliberate, inadvertent, or revealed by learning

Deferral can be an explicit trade-off: a team accepts a temporary implementation to test demand or meet a release. It can also occur through unexamined defaults, repeated local choices, incomplete processes, or knowledge that was never externalized.

[Fowler's technical-debt quadrant](https://martinfowler.com/bliki/TechnicalDebtQuadrant.html) distinguishes deliberate from inadvertent acquisition and prudent from reckless choices. It also recognizes debt discovered through learning: a reasonable implementation can later be understood as requiring consolidation.

This matters because later cost does not prove that the original choice was irrational. The project may have changed, or implementation may have produced knowledge that was unavailable beforehand. Conversely, a useful immediate result does not establish that the resulting obligation is affordable.

A disposable experiment need not satisfy the maintenance expectations of a long-lived product. The important transition occurs when others begin to rely on it: a prototype becomes a shared dependency, data persist in its representation, or its behavior becomes a compatibility promise. Work that was reasonably deferred during exploration can become an unacknowledged obligation after commitment.

Debt review should therefore attend to changes in reliance and scope, including cases where no explicit decision marked the transition.

## 5. Comprehension debt concerns the understanding needed for responsibility

For this assessment:

> **Comprehension debt is the accumulated gap between the understanding maintainers need to take responsibility for a system and the understanding they currently possess.**

That understanding includes relevant behavior, assumptions, boundaries, failure modes, rationale, and consequences of change. It concerns the relationship among a system, its maintainers, and their responsibilities; it is not an intrinsic property of a source file.

The reference point is sufficient understanding for a task and role. Maintainers do not need to know every dependency internally. Stable abstractions, reliable contracts, and accessible evidence make specialization possible. A new contributor's ordinary learning needs are not automatically debt either. The concern arises when necessary comprehension is persistently deferred while the project depends on people being able to modify, operate, or assess the system.

Comprehension is also collective. A team may have enough knowledge in aggregate but be dangerously dependent on one unavailable contributor. Another team may distribute its knowledge widely while nobody understands a consequential interaction. Concentration and insufficiency are different problems, although they can reinforce one another.

A technically sound implementation can therefore carry comprehension debt. Clean formatting, passing checks, and a coherent generated explanation do not establish that the responsible maintainers can reason about it. Conversely, familiarity with a difficult implementation can reduce immediate comprehension gaps while leaving substantial structural debt.

## 6. Recorded intent and human understanding are different resources

[Storey's proposed Triple Debt Model](https://arxiv.org/abs/2603.22106v4) separates technical debt in implementation, cognitive debt in shared understanding, and intent debt in externalized goals, constraints, and rationale. This provides a useful conceptual comparison, rather than a settled taxonomy. This note uses **comprehension debt** for its working definition of the understanding gap and treats missing intent as one important part of the broader project-knowledge problem.

Three situations require different responses:

- A maintainer understands an important compromise, but its rationale exists only in their memory. Selective capture and knowledge transfer may be needed.
- An accurate account exists, but the responsible maintainers cannot find, interpret, or apply it. Retrieval and learning may be needed.
- A fluent explanation exists, but its relationship to the actual evidence or historical decision is unknown. Investigation and qualification may be needed.

Producing a document does not establish that knowledge has been transferred. Reading it does not establish that it was understood. Understanding its account does not establish that the account is correct or currently applicable.

Some consequential structures also emerged without an explicit decision. In those cases, there may be no historical rationale to recover. An investigation can establish present behavior and propose an interpretation, while preserving that the original intent is unknown. Inventing a clean decision history would add misleading knowledge rather than discharge debt.

## 7. Interest can recur, compound, and move between people

Debt may charge interest through repeated small costs: investigating an exception again, maintaining two representations, manually reproducing an environment, or coordinating changes across an inappropriate boundary. It may also remain comparatively quiet until an incident, migration, or departure makes it expensive.

Several mechanisms can increase later costs:

- **Propagation:** more code, data, interfaces, or users come to depend on the original condition.
- **Reconstruction loss:** evidence disappears, memories fade, and the people who understood an exception become unavailable.
- **Workaround accumulation:** local responses add new mechanisms whose interactions require further explanation.
- **Knowledge amplification:** stale or unsupported guidance is reused by people or agents across additional changes.

These mechanisms explain how interest can compound without assuming that every debt grows exponentially. Some compromises remain localized and inexpensive for years. Their priority depends on actual exposure, expected change, and consequence.

Costs may also move between participants and budgets. A contributor gains delivery time while a reviewer absorbs interpretation work; an implementation team finishes a task while operators inherit manual recovery; a departing maintainer leaves successors to reconstruct context. A local productivity improvement can therefore coexist with a higher total project cost.

## 8. Coding agents change the distribution of deferred costs

The companion LLM assessment identifies a rate asymmetry: code and candidate explanation can be generated faster than people can inspect, understand, and validate them. Through the debt lens, this can separate immediate delivery from the comprehension and qualification work needed to sustain it.

Potential consequences include accepted changes whose governing assumptions remain unclear, tests that encode unexamined behavior, and summaries that appear to settle questions nobody actually resolved. Agent review can help, but several runs repeating the same assumptions do not establish independent support.

Agents can also reduce debt. They can retrieve earlier evidence, expose inconsistent guidance, explain a mechanism interactively, suggest an experiment, or help a maintainer articulate a difficult distinction. The relevant difference is how their output participates in investigation and learning.

[Ahmad's study of GenAI-assisted student projects](https://arxiv.org/abs/2604.13277) reports both accumulation patterns, including black-box code acceptance and verification bypass, and uses that supported understanding through explanation and exploration. Its evidence consists of reflective diaries from one educational setting; it does not establish an industry-wide causal effect or a universal debt rate. It supports examining the practice of use rather than treating agent assistance itself as sufficient diagnosis.

The immediate success of an agent task should consequently be considered alongside what remains for maintainers to understand, verify, and maintain.

## 9. Knowledge preservation can create its own debt

Documentation is part of the maintained system. Every retained record can introduce obligations concerning accuracy, scope, current standing, retrieval, and consistency with other records.

Cheap generation does not make these obligations cheap. A long account may take little time to produce while requiring substantial effort to review. Several overlapping summaries may create conflicting guidance. An unqualified interpretation may later be retrieved as established history. The project can exchange one missing explanation for a larger body of unreliable material.

> **Generating more knowledge artifacts than maintainers can meaningfully review can increase comprehension debt, including when Cairn generates them.**

This does not imply that every raw witness must be fully reviewed before it can be retained. A transcript or log can be valuable as searchable evidence without becoming accepted guidance. The distinction must remain visible: preserving a witness, publishing a candidate interpretation, and accepting a project claim create different expectations.

Capture burden and qualification burden must therefore be assessed together. A process can reduce the effort of recording information while increasing the effort of deciding what can be trusted. Likewise, a summary can reduce reading time while hiding uncertainty that matters to the decision.

Useful responses include selective capture, source references, concise accounts of consequential choices, explicit uncertainty, consolidation of competing current guidance, and retirement of obsolete material. Historical witnesses can remain available without remaining active instructions. The objective is usable knowledge at a sustainable total cost, not maximal capture or minimal documentation.

## 10. Diagnosis should connect a condition to an observable burden

Debt is easier to act on when a claim identifies what is deferred and how that deferral affects work. A vague label such as “legacy debt” or “poor documentation” does not provide enough information to choose a response.

A bounded assessment can ask:

1. What condition is creating an obligation, and what work has been deferred?
2. What evidence supports that interpretation, and what remains uncertain?
3. What recurring friction or contingent consequence constitutes the interest?
4. Who currently bears that cost, and who is likely to inherit it?
5. What changes, deadlines, or dependencies increase exposure?
6. What response would reduce the underlying condition, and what would show that it helped?

These are assessment questions, not mandatory fields for every observation. A report can begin as a short witness of repeated friction and receive structure only when useful.

Repeated investigation, difficult handovers, failed environment recreation, and changes that repeatedly violate an unstated assumption are possible signals. They require interpretation. A missing link does not prove lost understanding; a long review does not prove debt; document count and code coverage do not measure comprehension. Evidence may justify a suspected debt before it justifies a confirmed diagnosis.

No single numerical score should be assumed to combine structural, operational, and comprehension costs faithfully. Task-relevant evidence is a stronger starting point than a total derived from convenient proxies.

## 11. Paying interest, containing debt, and reducing principal differ

A workaround can restore service while preserving the cause of future incidents. A specialist can unblock a change while remaining the only person able to do so. A generated explanation can help finish today's task without becoming reliable shared knowledge.

Those actions may be useful. Their local success should not be mistaken for elimination of the underlying obligation.

Responses can instead serve different purposes:

- **Pay current interest:** complete the extra investigation or operational work required now.
- **Contain exposure:** isolate a mechanism, limit dependents, bound a compatibility promise, or delay further commitments.
- **Reduce principal:** consolidate the implementation, complete a migration, establish reliable evidence, or develop and share the missing understanding.
- **Retire the obligation:** remove the capability or end a commitment through an authorized process.
- **Retain deliberately:** accept the remaining burden within an explicit scope and reconsider it when relevant conditions change.

The right response depends on expected use, consequence, cost, and competing work. A project need not eliminate every debt before delivering value. It does need to avoid treating recurring cost as free simply because it has become routine.

Closure should follow the underlying obligation. Merging a refactor, closing a ticket, writing a note, or approving a handover does not by itself establish that the corresponding debt has been reduced. A later maintainer being able to use the result is stronger evidence than the existence of the output artifact alone.

## 12. The existing scenarios already expose debt mechanisms

Debt is a cross-cutting lens over the existing scenario corpus. The situations need not be duplicated into a separate process catalogue.

| Scenario | Debt-related question |
| --- | --- |
| `S5` — Changed context | Which earlier compromises have become costly because their supporting conditions changed? |
| `S7` — Architectural accretion | What recurring burden follows from structures that were never explicitly chosen? |
| `S9` — Unrecorded decision | What must later maintainers reconstruct, and what evidence can still be recovered? |
| `S10` — Incomplete migration | What interest is paid to maintain the mixed state, and what remains to complete or explicitly suspend the transition? |
| `S11` — Ecosystem deadline | How does repeated deferral reduce options or increase the eventual response cost? |
| `S14` — Contributor departure | What obligations depended on personal understanding that was never effectively transferred? |
| `A1` — Delegated implementation | What comprehension and validation work remains after a passing change is delivered? |
| `A4` / `A5` — Generated or stale knowledge | Is the record helping recover understanding, or adding misleading guidance that future work will reuse? |

The sequence from condition to signal, recognition, and uptake remains important. Debt can exist before it is noticed. Recognition does not ensure that work is allocated. Opening a ticket makes an obligation more visible without paying its principal or preventing further interest.

## 13. Implications for Cairn remain a product hypothesis

The debt lens strengthens a possible purpose for Cairn:

> **Help maintainers keep project intent, implementation, and shared understanding connected so that they can investigate, assess, and evolve the system at a sustainable cost.**

This complements the tool-landscape note's candidate focus on living project assumptions. Assumptions connect compromises to their conditions of validity, evidence, and review triggers. That remains a hypothesis to test; debt does not automatically become Cairn's native object, nor does this note prescribe entities or storage.

Cairn could help recover relevant context, distinguish observed facts from candidate explanations, expose missing or conflicting knowledge, and reconnect a changed condition to earlier commitments. The CLI can provide inspectable access to that evidence across artifacts and development platforms. Companion agents can guide investigation, challenge interpretations, and help maintainers review what needs attention. In the current intended mode, they guide and review; edits to project files require permission. Responsibility for accepting commitments and explanations remains explicit.

Cairn's contribution should be tested through concrete maintenance situations: reviewing an agent-generated change, recovering an architectural rationale, transferring responsibility, or revising an old compatibility commitment. Useful observations include whether people can identify the relevant evidence, explain the assumptions, assess a change, and act with less repeated reconstruction.

The evaluation must also include Cairn's own burden: capture effort, review time, misleading candidates, duplicated guidance, and ongoing record maintenance. A smaller amount of faithful, retrievable knowledge may be more valuable than a larger corpus. Better agent output alone is insufficient if the supporting account becomes less accurate or the maintainers less able to understand it.

## Overall assessment

Debt links present development choices to future obligations and the interest paid while those obligations persist. Its usefulness depends on identifying a concrete mechanism rather than labeling every imperfection or inherited commitment as debt.

Implementation quality, recorded knowledge, and maintainer comprehension are related but distinct. Improving one does not automatically improve the others. Coding agents can help connect them, or accelerate their separation.

For Cairn, the central constraint is to support understanding without creating an unmanageable body of explanations. Its contribution should be judged through the work maintainers can perform and the total effort required to sustain that capability.

## Source note

This is a conceptual synthesis grounded in the companion notes and the sources below, rather than a systematic literature review. The proposed distinctions and Cairn implications are analytical propositions for later assessment.

- [Ward Cunningham, *The WyCash Portfolio Management System* (1992)](https://c2.com/doc/oopsla92.html) — the original debt metaphor, relating incremental delivery, consolidation, and interest paid through continuing implementation friction.
- [Martin Fowler, *Technical Debt Quadrant* (2009)](https://martinfowler.com/bliki/TechnicalDebtQuadrant.html) — deliberate and inadvertent debt, prudent and reckless acquisition, and debt revealed through learning.
- [Margaret-Anne Storey, *From Technical Debt to Cognitive and Intent Debt: Rethinking Software Health in the Age of AI* (2026, version 4)](https://arxiv.org/abs/2603.22106v4) — a conceptual proposal separating implementation, shared understanding, and externalized intent; not an established measurement model.
- [Muhammad Ovais Ahmad, *Comprehension Debt in GenAI-Assisted Software Engineering Projects* (2026)](https://arxiv.org/abs/2604.13277) — qualitative evidence from 621 reflective diaries by 207 students over eight weeks, examining practices that accumulate or mitigate comprehension debt; generalization beyond that setting remains limited.
