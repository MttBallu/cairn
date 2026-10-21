# LLMs and Coding Agents in Software-Project Knowledge

> **Status:** working cross-cutting assessment  
> **Revised:** 21 October 2026  
> **Purpose:** examine how agent participation changes the production, use, qualification, and maintenance of project knowledge.  
> **Audience:** readers examining agent-assisted software work and its effects on understanding and responsibility.  
> **Scope:** mechanisms and illustrative situations, not a vendor comparison, product design, or repository permission policy.

Coding agents can participate in implementation, investigation, review, and knowledge capture. They use project records to guide action and produce changes, observations, and candidate explanations that later work may reuse. Their role therefore crosses the situations in the [core scenario corpus](software-design-scenarios.md).

The [context note](software-design-context.md) explains the general knowledge problem. The [debt note](software-project-debt.md) examines deferred costs, and the [tools landscape](software-project-knowledge-tools.md#agent-guidance-and-integration) describes existing formats and integration mechanisms. This note examines what changes when an agent participates, without assuming one degree of autonomy or one governance arrangement.

## Model, coding agent, and run

An LLM is a generative model. A [coding agent](glossary.md#coding-agent) is a configured system that combines a model with instructions, context, tools, permissions, and a mechanism for pursuing work. An [agent run](glossary.md#agent-run) is situated activity against a particular project state for a particular task.

These distinctions matter to history. A person can delegate a task, a configured system can perform a run, a change can result, and someone else can accept it. Calling all of this model authorship loses the distribution of production, review, and responsibility.

Autonomy has several dimensions: task scope, available actions, duration, approval boundaries, concurrent work, environmental reach, and recovery options. Broad read access differs from production write access; a supervised editor session differs from several asynchronous runs. A scalar description such as highly autonomous does not determine the relevant risks.

In these notes, [participant](glossary.md#participant) is the generic term for people and software systems. Human participant and coding agent are used when their differences matter.

## Guidance needs meaning, scope, and authority

Project context can contain task intent, design rationale, procedures, executable checks, and permissions. Their functions differ. A requirement describes an expected outcome; an explanation helps interpret an appropriate change; a procedure describes steps; a check evaluates a selected property; permission authorizes an action.

An [assumption](glossary.md#assumption) is a premise currently relied upon, with support that can vary. An [instruction](glossary.md#instruction) directs action. Turning a qualified premise into a confident instruction can improve compliance while misrepresenting the reason for the rule. For example, a preference for pure functions because of earlier mutation defects has a scope and rationale that a bare prohibition does not preserve.

The relevant context depends on the task, affected artifacts, current project state, and governing commitments. Supplying every document does not ensure that the relevant exception or superseding record receives attention. A correct retrieval can still lead to inappropriate action when the old conditions no longer apply.

Guidance can conflict with other guidance or the current implementation. Possible responses include applying a known precedence rule, using a documented exception, making an interpretation within delegated authority, or surfacing an unresolved question. The appropriate response depends on project arrangements. Technical ability to continue does not establish authority to change policy or accept a risk.

## Context delivery does not establish reliance

The boundary of a run's context can be partly observed, but different claims require different evidence:

| Event or assertion | What a record may establish | Remaining limitation |
| --- | --- | --- |
| Available to the client | A record could be accessed | It may never have been requested |
| Requested | A particular query or request occurred | It may not have returned the relevant material |
| Returned | A particular record or version was delivered | Delivery does not establish attention or correct interpretation |
| Cited | The output refers to the record | Citation does not establish causal influence or faithful application |
| Reported as relied upon | The agent gives an account of reliance | This is an assertion requiring assessment against other evidence |

Task references, project state, returned versions, tool invocations, changes, and execution results can support investigation. The available record is still partial. A transcript of a run is not a complete account of the model's internal operation, and adding more log volume does not automatically improve explanation.

## Agent activity produces candidate knowledge

A diff witnesses a proposed or performed change. A test log records an execution under conditions. A generated account proposes an explanation. These objects have different evidential roles, even when they are produced by one run and presented together.

An outcome account can identify the requested result, affected scope, observed checks, consulted sources, material choices, deviations, and remaining uncertainty. Separating trace-backed observations from interpretations lets a reviewer examine what is supported without reconstructing every intermediate action.

A generated explanation may faithfully summarize the available evidence, but fluency does not establish historical accuracy. It can offer a plausible rationale for a choice without proving that this was the reason for the choice. Later human confirmation is another event, not retroactive proof that the earlier explanation was an observation.

Authorship and responsibility can be layered: requesting, delegating, producing, reviewing, accepting, and owning the consequences are distinct roles. Ordinary author and committer fields may provide only part of that account.

## Velocity and capture economics

Code and explanations can be generated faster than people can inspect, understand, and qualify them. This can separate successful delivery from the understanding needed for later diagnosis or change. It can also make capture cheaper: a system involved in work can help record consulted sources, observations, and unresolved questions while they remain accessible.

Immediate reuse may change the incentive to preserve knowledge. A contributor who records useful guidance can potentially benefit on the next task, rather than relying only on an uncertain future reader. This is a plausible mechanism, not proof of sustained rationale capture. The existence or adoption of an instruction format does not establish the accuracy, completeness, or long-term maintenance of its contents.

The contrast is between uses of assistance, not a necessary outcome of automation. [Ahmad's qualitative study](https://arxiv.org/abs/2604.13277) identifies both practices that accumulated comprehension debt and uses that supported understanding through explanation and exploration. It draws on reflective diaries in one educational setting and does not establish an industry-wide causal rate. The [debt note](software-project-debt.md#coding-agents-change-the-distribution-of-deferred-costs) interprets these risks as deferred obligations.

## Failure patterns

The following are working analytical patterns, not an exhaustive empirical taxonomy:

| Pattern | Mechanism and consequence |
| --- | --- |
| Documentation laundering | A proposed interpretation loses its candidate status and is reused as established history |
| Synthetic consensus | A summary removes disagreement, hesitation, or an unresolved objection |
| Instruction drift | A descriptive record becomes more confident or less qualified because that wording steers an agent more effectively |
| Unknown context boundary | A later investigation cannot distinguish unavailable, unrequested, returned, and allegedly used guidance |
| Context omission | A rule is retrieved without its exception, scope, or superseding record |
| Stale amplification | Outdated guidance is repeated across additional changes |
| Pattern accretion | Repeated locally convenient generations erode a convention without an explicit project decision |
| Volume asymmetry | Outputs exceed review capacity while approval appears more comprehensive than the examination performed |
| Circular evidence | Several derived accounts appear independent although they share one source |
| Silent conflict resolution | A local completion hides incompatible project instructions or assumptions |
| False completion | A requested artifact is delivered while associated migration, validation, or learning remains unfinished |
| Authority leakage | Permission to act is treated as authority to establish policy or accept commitments |
| Integration knowledge gap | Locally coherent concurrent changes rely on incompatible assumptions |

Attributing a repeated pattern to a model's training distribution is itself an interpretation. Repository evidence can show the changes and their effects without providing a historical rationale for every generation.

## Agent-mediated scenarios

A1–A7 isolate pressures introduced or amplified by agent participation. They complement [S1–S15](software-design-scenarios.md#scenario-map) and keep their own identifiers. The situations are illustrative, not reports of measured prevalence. Their deliberate and abbreviated paths describe possibilities rather than a required procedure.

### A1 — Delegated implementation produces opaque decision density

A human delegates a feature or refactoring task to a coding agent. The task is bounded by an issue and repository instructions. The agent modifies several components, introduces an abstraction, adds tests, and returns a passing pull request.

In the deliberate trajectory, the handover identifies the governing assumptions, material alternative, affected commitment surfaces, validation evidence, and one choice that requires explicit acceptance. The reviewer can focus on those points while still inspecting the diff and tests.

In the abbreviated trajectory, the agent supplies a generic summary and a large working diff. The reviewer verifies that checks pass and samples the code. The change is merged, but nobody can later distinguish deliberate architecture from the agent's locally convenient completion.

Important non-implications:

- Passing checks do not establish that the implementation respects every relevant design intention.
- A generated summary does not establish why each consequential choice was made.
- Human approval does not establish that the human reconstructed the complete implementation process.

### A2 — Retrieved project knowledge guides an agent

Before changing a subsystem, an agent retrieves a current ADR, a coding convention, an earlier incident, and an assumption linked to an architectural check. These records redirect the proposed implementation away from an approach that previously caused operational problems.

This is the positive read-path case: preserved knowledge changes an outcome. An account of the run can retain which records were requested and returned, which ones the agent cited, and what observable parts of the change are consistent with them. A claim that one record materially influenced the result remains an assertion unless stronger evidence supports it.

In the abbreviated trajectory, the agent does not search because the task appears routine, or it searches with vocabulary that does not match the earlier record. The prior failure is repeated.

Important non-implications:

- The existence of relevant knowledge does not establish that the agent will retrieve it.
- Retrieval does not establish that the record is current or applicable.
- Following an earlier decision does not establish that present conditions are equivalent.

### A3 — Project guidance conflicts during a run

An agent discovers that a repository-level instruction requires one dependency direction while a subsystem document and the existing implementation require the opposite. Both records appear current.

In the deliberate trajectory, the agent stops at the affected boundary, presents the conflicting witnesses, identifies the smallest decision required, and requests qualification from a person with appropriate authority. The conflict itself becomes a durable signal.

In the abbreviated trajectory, the agent chooses the instruction closest to the edited file, follows the dominant code pattern, or combines the two imperfectly. The task completes while the underlying inconsistency remains invisible.

Important non-implications:

- A more specific instruction is not necessarily more current or authoritative.
- Existing code does not establish intended architecture.
- The agent's ability to continue does not establish that it has authority to resolve the conflict.

### A4 — An LLM assists human knowledge capture

Two people and an LLM explore a design problem. The discussion contains an observation, two alternatives, a provisional assumption, a concern that remains unresolved, and a decision to run an experiment before committing.

In the deliberate trajectory, the raw conversation remains available. The LLM proposes a small set of typed statements and links, marks the objection and assumption as unresolved, and asks targeted questions. Participants correct the proposal and confirm the resulting record.

In the abbreviated trajectory, the LLM produces polished meeting notes stating that the group chose one alternative. The summary removes the unresolved concern and turns the planned experiment into a justification. Future participants see a decision that never occurred.

Important non-implications:

- Mentioning an alternative does not establish that it was seriously evaluated.
- A proposed summary does not establish participant agreement.
- Linguistic coherence does not establish historical or epistemic accuracy.

### A5 — Correct retrieval leads to incorrect action

An agent proposes an implementation and searches for related decisions. It finds an ADR that rejected the same approach two years earlier because a dependency lacked a required capability. The document remains marked “accepted,” so the agent abandons the proposal.

The retrieval is technically successful, but the dependency gained the missing capability several releases ago. The old rationale was sound in its original context and inapplicable now.

In the deliberate trajectory, the agent examines the decision's assumptions and current evidence, detects the changed condition, and reopens the alternative for human evaluation. In the abbreviated trajectory, the apparent authority of the record ends the investigation.

Important non-implications:

- An accepted decision is not timeless instruction.
- Correctly reading a record does not establish that applying it now is correct.
- A changed condition does not retroactively make the earlier decision unsound.

### A6 — Parallel agents create an integration knowledge gap

Several agents work concurrently on related issues in separate workspaces. Each change is locally coherent and passes its own checks. One agent introduces a new representation while another extends the representation being replaced; a third adds a convention based on assumptions that neither of the other runs saw.

In the deliberate trajectory, the runs declare affected assumptions and commitment surfaces. Integration detects overlap before merge, compares the assumptions, and redirects or sequences the changes.

In the abbreviated trajectory, merge conflicts are resolved syntactically and the test suite passes. The project now contains two incompatible directions, but each pull request retains a locally plausible explanation.

Important non-implications:

- Non-overlapping textual diffs do not establish semantic independence.
- Local test success does not establish compatibility between concurrent decisions.
- Successful merge does not establish that the combined system has one coherent direction.

### A7 — A coding agent performs review

A coding agent is asked to review a proposed change. The implementation may have been produced by a human or by another coding agent. The reviewer inspects the diff, retrieves project guidance, executes checks, and reports correctness, maintainability, and architectural concerns.

A configured reviewer may avoid some personal sunk-cost and interpersonal pressures that affect human review in [S3](software-design-scenarios.md#s3--a-code-review-redirects-implementation-into-design-deliberation). This possible advantage does not make the review objective: its instructions, context, model behavior, and incentives can still shape which objections appear and how they are expressed.

In the deliberate trajectory, the review preserves its evidence, applicable instructions, and assumption queries. Independent checks or differently configured reviewers challenge the implementation from distinct perspectives. A human can see which concerns are trace-backed, which are generated judgments, and which require decision authority.

In the abbreviated trajectory, one agent reviews another agent's output using the same model family, instructions, retrieved context, and statistical habits. The second run repeats the first run's blind spots and presents agreement as independent confirmation. The agreement is weak evidence of independence when the review brings no materially different observations, assumptions, or checks. Human participation or a different model would likewise need to contribute a substantive difference rather than merely another approval.

Important non-implications:

- A separate agent run does not establish an independent review.
- Reduced personal or social pressure does not establish architectural insight.
- Agreement between similarly configured agents does not constitute independent evidence.
- An agent review can improve a change without acquiring authority to accept project-level risk.

## Possible practices and their limits

Selective, source-linked accounts can make review more focused. Targeted questions can expose an implicit premise or unresolved conflict. Separating records of execution from generated interpretation can preserve uncertainty, and executable checks can test selected expectations. These approaches have costs and depend on the project’s responsibilities, risks, and available attention.

Additional summaries and reviews can themselves increase the burden. Multiple runs may share blind spots; a polished account may hide a missing premise; a record can become stale while retaining an authoritative appearance. A review practice therefore needs evidence about the properties it actually examines rather than relying on its label.

This account leaves the choice of workflow and formal representation open. An observed difficulty can call for simpler code, a revised commitment, better expertise sharing, clearer records, or a different tool arrangement. It does not establish that all knowledge should be centralized or expressed in one schema.

## Sources and limits

The mechanisms and scenarios are conceptual analyses. Contemporary formats provide capability examples; they do not establish prevalence, sustained adoption quality, or a complete engineering process.

- [AGENTS.md](https://agents.md/) supplies a shared location for repository guidance; it does not require a particular rationale structure.
- [Agent Skills specification](https://agentskills.io/specification) describes packaging for instructions and supporting resources. A portable package does not establish that its procedure is adequate.
- [MCP introduction](https://modelcontextprotocol.io/docs/getting-started/intro) describes connection to external data and tools. Connection alone does not establish which project knowledge is applicable or how a run should be interpreted.
- [Grudin, Groupware and Social Dynamics](https://www.microsoft.com/en-us/research/wp-content/uploads/2017/01/groupware-and-social-dynamics.pdf) analyzes disparities between capture effort and later benefit. Immediate agent reuse is considered here as a possible change to that incentive.
- [Ahmad, Comprehension Debt in GenAI-Assisted Software Engineering Projects](https://arxiv.org/abs/2604.13277) provides situated qualitative evidence about practices of use; its educational setting limits generalization.

Format capabilities were checked against the linked official documentation on 21 October 2026. The conceptual and empirical sources retain their original dates. The [tools landscape](software-project-knowledge-tools.md) gives a wider view of existing responses.
