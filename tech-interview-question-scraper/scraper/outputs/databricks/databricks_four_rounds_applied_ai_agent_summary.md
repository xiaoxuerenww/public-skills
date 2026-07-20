# Databricks Applied AI / Agent Team Four-Round Summary

Source files:

- `outputs/databricks/databricks_staff_mle_focus.md`
- `outputs/databricks/databricks_staff_question_bank.md`
- `outputs/databricks/databricks_behavior_question_bank.md`
- `outputs/databricks/databricks_reorganized_by_category.md`

Target: Staff / Senior Staff MLE, Applied AI, AI Eng, agent-facing teams.

## Overall Pattern

For Applied AI / agent roles, the strongest Databricks signals are:

1. Practical ML fundamentals, not broad trivia.
2. Agent/RAG system design grounded in Databricks assets: tables, notebooks, lineage, permissions, usage signals.
3. Behavioral and cross-functional rounds that test execution judgment, project scope, feedback, conflict, and customer/data-driven decisions.
4. Project deep dive where the interviewer can push from ML method to product tradeoff, infra bottleneck, eval validity, and cross-team ownership.

The loop is less about memorizing many ML topics and more about showing that you can build useful, governed, measurable AI systems on top of data/platform surfaces.

## 1. ML Fundamental

High-confidence question families:

- Linear regression gradient descent from scratch.
- Word2Vec training.
- Transformer architecture.
- Query/key/value attention reasoning.
- ML coding/debugging with shape, convergence, and numerical stability.

Likely prompts:

- Implement linear regression with MSE and gradient descent.
- Derive the MSE gradient and explain why the mean term matters.
- Debug non-convergence: learning rate, missing averaging, feature scale, broadcasting bug, update-order bug.
- Explain Word2Vec skip-gram vs CBOW and negative sampling.
- Explain a transformer block.
- Why do attention layers use separate query and key projections?
- Explain masking, scaled dot-product attention, and value aggregation.

Applied AI / agent-team angle:

- Connect embeddings to retrieval quality, indexing, and semantic matching.
- Connect attention/QKV to LLM behavior only at the level needed for agent design, not research-theory overkill.
- Be ready to reason about evals: retrieval recall, rank quality, answer usefulness, calibration, and failure slices.
- In coding, prioritize clean tests and debugging discipline. Databricks posts repeatedly mention runnable tests, mocked time, and production-style completeness.

Prep priority:

1. Linear regression gradient descent, including tests and bug diagnosis.
2. Transformer/QKV oral explanation.
3. Word2Vec and embedding-training intuition.
4. Small ML coding exercises around retrieval, cosine similarity, top-k, and evaluation.

## 2. ML System Design

Highest-priority prompt:

Design retrieval for an internal coding/data agent. A user asks a data-related question; the agent must find the right Databricks table, notebook, or workspace asset so it can answer correctly.

Core design points:

- Index table metadata, schemas, descriptions, owners, lineage, query logs, notebook text/code, comments, freshness, permissions, and usage signals.
- Separate candidate generation from reranking.
- Filter by ACLs before retrieval results can leak asset names or content.
- Handle noisy, stale, duplicate, or unhelpful notebooks/tables.
- Use workspace/user context, entity linking, historical usage, and query intent.
- Define evals: asset recall, answer accuracy, citation correctness, human acceptance, latency, freshness, and permission correctness.
- Add feedback loops from clicks, accepted answers, corrections, and manual reviews.

Other likely ML design prompts:

- Harmful content detection for LLM outputs.
- Notebook OOM / resource-failure prediction.
- RAG or moderation system with production serving and monitoring.

Applied AI / agent-team angle:

- For RAG/agent design, keep the design simple first: retrieval, rerank, answer generation, citation, feedback.
- Make governance first-class: permissions, audit logs, data lineage, tenant/workspace boundaries.
- Treat eval design as a core system component, not an afterthought.
- Discuss product interventions, not only model prediction. For OOM, the action might be warn, autoscale, sample-first, rewrite, checkpoint, or recommend cluster sizing.
- Tie thresholds to user trust, cost, latency, and risk.

Prep priority:

1. RAG over tables/notebooks for a coding/data agent.
2. Harmful content detection for LLM outputs.
3. Notebook OOM prediction.
4. One generic RAG eval and monitoring framework you can reuse.

## 3. Behavioral And Cross-Functional

Databricks behavioral rounds are described as standard BQ, Cross-Functional, HM chat, or culture round. The signal is practical execution rather than values-heavy philosophy.

Likely prompts:

- Why Databricks?
- Why this team or role?
- Walk me through a major project.
- Tell me about your hardest technical challenge.
- Tell me about a technical design conflict.
- Tell me about a cross-functional conflict.
- Tell me about conflict during planning.
- Tell me about critical feedback.
- Tell me about feedback you disagreed with.
- Tell me about your biggest mistake.
- Tell me about using customer feedback to improve a product.
- Tell me about using data to make a decision.
- How do you break down large tasks?
- How do you handle ambiguity or planning risk?

Applied AI / agent-team angle:

- Use stories that combine ML/product judgment with platform constraints.
- Favor examples involving users, data quality, eval ambiguity, launch risk, infra limits, and cross-team dependencies.
- Avoid small examples. One Senior MLE thread explicitly suspected the examples were too naive for the level.
- Be ready for reference-check consistency: manager/TL/peer should be able to support your scope, role, and impact.

Best story anchors to prepare:

- Most challenging ML/platform project.
- Customer feedback changed the roadmap.
- Data changed a product or modeling decision.
- Technical design conflict over model/system tradeoff.
- Cross-functional conflict or planning ambiguity.
- Critical feedback accepted and acted on.
- Feedback you disagreed with but handled constructively.
- Biggest mistake or hard lesson.

Answer shape:

1. State the project and your role.
2. Name stakeholders and their incentives.
3. Describe the ambiguity, conflict, or planning risk.
4. Explain the tradeoff and decision process.
5. Show what you personally did.
6. Quantify impact or state the concrete outcome.
7. Close with what changed afterward.

## 4. Project Deep Dive And Mock Project Leading

The question banks show Project Deep Dive / Domain Deep Dive as a recurring Staff+ signal. For Applied AI / agent teams, expect the interviewer to stay on one project for a long time and push on why, how, tradeoffs, metrics, and execution.

Likely prompts:

- Give a deep technical walkthrough of your most relevant project.
- What was the real problem and why did it matter?
- What did you personally own?
- What alternatives did you consider?
- Why did you choose this architecture/model/eval?
- What was the hardest bottleneck?
- What failed or almost failed?
- How did you know the system was working?
- How did customer feedback or data change the design?
- How did you lead without direct authority?
- How did you break the project into milestones?
- How would you lead a similar project for Databricks agents?

For a Databricks Applied AI / agent team, make the project deep dive map onto:

- Data discovery, retrieval, ranking, or agent workflow quality.
- Eval design under ambiguous user intent.
- Production serving constraints: latency, cost, freshness, reliability.
- Governance: permissions, auditability, privacy, policy, and safe rollout.
- Cross-functional execution with product, infra, UX, data owners, and domain experts.

Mock project-leading prompt to practice:

You are leading a Databricks internal coding/data agent project. The agent must answer user questions about workspace data by retrieving relevant tables and notebooks, citing evidence, respecting permissions, and improving from feedback. Lead the project from ambiguous problem statement to launch.

Expected leadership discussion:

- Clarify users: data scientists, analysts, engineers, admins.
- Define jobs-to-be-done: find the right asset, explain lineage, answer schema/query questions, suggest notebooks or queries.
- Define MVP: retrieval plus citation over a bounded asset set, strict ACL filtering, offline eval, simple feedback collection.
- Define metrics: task success, accepted answer rate, citation correctness, permission violations, latency, freshness, escalation rate.
- Define milestones: data ingestion/indexing, candidate retrieval, reranker, answer generation, eval harness, dogfood, guarded rollout.
- Define risks: data leakage, stale docs, noisy notebooks, duplicated assets, hallucinated citations, over-personalized ranking, cost/latency blowup.
- Define team plan: platform/indexing owner, ML/ranking owner, product/eval owner, governance/security owner, serving/observability owner.
- Define review cadence: weekly eval review, launch-readiness gates, red-team/privacy review, incident playbook.

## Highest-ROI Prep Order

1. Build a 20-minute answer for RAG over Databricks tables/notebooks for a coding/data agent.
2. Prepare a 45-minute project deep dive around your strongest RAG / LM-ranking / agent-system project.
3. Drill linear regression gradient descent and Transformer/QKV fundamentals until they are automatic.
4. Prepare 6-8 behavioral stories using Staff-level scope and real tradeoffs.
5. Practice the mock project-leading prompt above, especially milestones, staffing, metrics, and risks.

## Source Anchors

- `1175089`: Staff-target MLE system design around internal coding-agent retrieval over tables/notebooks.
- `1173790`: Staff Applied AI screen with practical coding emphasis.
- `1173457`: MLE onsite with ML design, ML fundamentals/coding, technical design conflict.
- `1172872`: MLE onsite with linear regression GD, harmful content detection, notebook OOM prediction.
- `1110121`: Senior MLE loop with Word2Vec, Transformer/QKV, BQ examples, and scope warning.
- `1156010`, `1148433`: Staff loops mentioning Domain/Project Deep Dive and Cross-Functional/BQ.
