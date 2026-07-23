# Framework Adaptation Notes

Use the generic ML system design template as a starting point, not a script.

## Prep Lifecycle

For each new problem, keep artifacts separated by purpose:

1. `requirements.md` or `problem.md`: prompt, assumptions, requirements, metrics, scale, non-goals, and ambiguities.
2. `system_design_answer.md` / `deep_dive.md` / `interview_discussion.md`: solved L6+ answer and reusable explanation.
3. `learn_notes.md`: chronological explain-mode Q&A and corrected mental models.
4. `mock.md`: chronological mock interview notes, hints, feedback, and verdicts.

Repeat explain mode and mock mode as many times as needed. Append dated sections rather than replacing earlier learning history.

## Generic Product ML Prompt

Use the normal 5 phases:

1. Problem definition and scoping.
2. Data and feature engineering.
3. Model architecture and training.
4. Model serving and infrastructure.
5. Monitoring and iteration.

This fits recommendation, ranking, classification, fraud, content moderation, search, feed, and ad systems.

## Research Infrastructure Prompt

Use the adapted phases:

1. Scope and success criteria.
2. Inputs, metadata, and contract model.
3. Core planner or algorithm.
4. Execution, storage, and infrastructure.
5. Observability, debugging, and iteration.

This fits experiment platforms, ML configuration systems, parameter sweeps, training orchestration, evaluation infrastructure, data pipelines, and debugging systems.

## Interview Answer Skeleton

```text
Clarify:
- Users and workflow.
- Scale and constraints.
- Correctness guarantees.
- Success metrics.
- Stakeholders, adoption path, and what must be true for this to be worth building.

Requirements:
- Functional requirements.
- Non-functional requirements.
- Explicit non-goals.

Architecture:
- Input/source layer.
- Validation/planning layer.
- Execution layer.
- Storage/tracking layer.
- Query/analysis layer.

Deep dives:
- Hard correctness invariant.
- Scale bottleneck.
- Failure/recovery semantics.
- One L6+ leverage point: API contract, platform boundary, research velocity, migration strategy, or cost/risk control.

Trade-offs:
- Simplicity vs flexibility.
- Strictness vs research velocity.
- Reuse tools vs own critical invariants.

Monitoring and debugging:
- System health.
- Data/model quality.
- Failure classification.
- Auditability and provenance.

Wrap-up:
- Restate core thesis.
- Name the riskiest part and mitigation.
- State MVP vs hardening vs scale-out plan.
```

## Seniority Signals

- Make explicit what must never silently go wrong and why it matters to users, researchers, or the business.
- Separate user-facing authoring from internal canonical representation.
- Distinguish control plane state from runtime state.
- Define identity, idempotency, and retry semantics.
- Describe how to debug wrong results, not only failed jobs.
- Name existing tools but own the invariants they cannot guarantee by themselves.
- Sequence the design: MVP first, then hardening, then scale-out.
- Discuss migration and adoption, especially how teams move from existing scripts or manual workflows.
- Tie platform decisions to leverage: fewer invalid experiments, faster iteration, lower GPU waste, safer launches, better auditability.
- Quantify cost, latency, throughput, reliability, or experiment volume when possible.

## L4/L5 vs L6+ Answer Delta

An L4/L5 answer often describes components correctly: configs, scheduler, database, workers, dashboards, and monitoring.

An L6+ answer additionally explains:

- **Why this system exists**: the organizational or research bottleneck it removes.
- **What can corrupt decisions silently**: data leakage, bad overrides, wrong metric aggregation, stale features, duplicate runs, or untracked environment changes.
- **Who owns each contract**: researchers, platform team, scheduler, tracker, model runtime, data pipeline, and reviewers.
- **How trust is enforced**: validation, provenance, immutable records, audit logs, reproducible artifacts, and typed APIs.
- **How the rollout lands**: start with one-run and grid-sweep workflows, migrate high-value teams, add policy gates for large sweeps, then integrate deeper schedulers or search algorithms.
- **How the system evolves**: explicit extension points for new search strategies, schedulers, trackers, model types, and evaluation workflows without breaking old runs.

Use this delta when coaching or grading: the candidate should not merely assemble pieces; they should show judgment about which invariants create leverage at Staff level.
