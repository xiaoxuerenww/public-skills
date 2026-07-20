# Databricks Staff MLE Focused Prep Notes

Source: `outputs/databricks/databricks_reorganized_by_category.md`.

Scope: filtered to Staff/Senior MLE, Applied AI, AI Eng, and ML-track signals. Frontend, pure backend, pure infra/system programming, NG/intern-only, recruiter-only, and generic SDE/SWE material are excluded.

Kept categories: leetcode-style algorithm coding, ML/LLM fundamentals, ML system design.

## Summary

- Algorithm coding sources: `1173790`, `1124389`, `1173457`, `1172872`, `1110121`
- ML/LLM fundamental sources: `1173457`, `1172872`, `1110121`, `1060896`, `1147731`
- ML system design sources: `1175089`, `1173457`, `1172872`, `1110121`
- High-confidence Staff/Senior MLE anchors: `1175089`, `1173790`, `1173457`, `1172872`, `1110121`

## Algorithm Coding

### Sliding-window / hit-counter style KV metrics

Sources: `1173790`, related MLE/AI Eng context in `1163734` but pure SDE deployment details are excluded.

What to prepare:

- Implement `put/get` event tracking and query QPS/load over the last 5 minutes.
- Support multiple events with the same timestamp.
- Extend from a fixed 5-minute window to configurable windows such as 24 hours.
- Explain memory optimization: raw event queue vs bucketed counters vs rolling aggregates.
- Clarify whether timestamps are monotonic, whether late events exist, and whether the result is exact or approximate.

Why this stays in scope: `1173790` is explicitly Staff Applied AI, and the poster notes they normally do ML but were tested on practical coding.

### SnapshotSet / snapshot iterator

Source: `1124389`.

What to prepare:

- Implement a set whose iterator freezes the visible contents at iterator creation time.
- Keep `contains` current while existing iterators remain stable.
- Start with single-thread, single-iterator behavior; then discuss multiple iterators.
- Use version/timestamp metadata or add/delete logs to decide what each iterator can see.
- Be ready to explain why binary search over per-key logs can work, and what changes under concurrency.

Why this stays in scope: the post says the role was MLE and the interview explicitly used this non-LeetCode but data-structure-heavy coding task.

### Interval deletion / simplified cipher

Sources: `1173457`, `1110121`.

What to prepare:

- Given a list of intervals over a source string, delete the `idx`-th position from the cover and return the updated cover.
- Clarify immediately whether `idx` refers to the interval list, a generated cipher position, or a source-string index.
- Handle unsorted or overlapping intervals if allowed.
- Implement interval split, shrink, removal, and merge operations.
- Follow-up: return a simplified representation by merging adjacent intervals that can be represented as one contiguous source span.

Why this stays in scope: both MLE/Senior MLE posts mention this coding family, and `1173457` says ambiguity around `idx` caused major time loss.

### Lazy array and laziness testing

Source: `1172872`.

What to prepare:

- Implement deferred transformations over an array-like object.
- Define when computation materializes: iteration, indexing, `collect`, or explicit evaluation.
- Test laziness with a stub/mock function and invocation counts.
- Discuss caching: repeated reads should either recompute by contract or memoize by design.
- Cover edge cases around chained operations and mutation after lazy operations are registered.

Why this stays in scope: it appears in an MLE onsite post alongside ML design and ML fundamentals.

## ML/LLM Fundamental

### Linear regression gradient descent from scratch

Sources: `1173457`, `1172872`.

What to prepare:

- Derive MSE with the mean included, not only sum of squared errors.
- Implement gradient descent for `X -> y` with correct tensor/vector shapes.
- Explain learning rate, convergence, early stopping, and debugging non-convergence.
- Write a tiny test where loss decreases on synthetic data.
- Be able to find bugs in gradient, averaging, broadcasting, and update order.

Interview framing: `1173457` explicitly says forgetting the “Mean” in MSE can make convergence difficult; `1172872` reports simple linear regression gradient descent in the ML round.

### Word2Vec and embedding training

Source: `1110121`.

What to prepare:

- Explain skip-gram vs CBOW at a high level.
- Explain negative sampling and why full softmax is expensive.
- Describe what the learned embedding represents and how it is used downstream.
- Know common training pairs, context windows, and objective intuition.

Interview framing: `1110121` says the Senior MLE loop asked how to train word2vec, and replies clarify the ML/LLM round was oral fundamentals, not coding.

### Transformer architecture and attention fundamentals

Source: `1110121`.

What to prepare:

- Explain the transformer block: token embeddings, positional encoding, multi-head attention, MLP, residuals, layer norm.
- Explain why query and key are separate projections rather than one shared vector.
- Explain attention scores, scaling by `sqrt(d_k)`, masking, and value aggregation.
- Be ready to contrast self-attention with RNN/CNN-style sequence modeling.

Interview framing: `1110121` explicitly lists transformer architecture and why query/key are needed.

### ML domain coding / performance-oriented ML challenge

Sources: `1060896`, `1147731`.

What to prepare:

- Expect ML coding to be framed as designing and implementing a performant ML engineering solution, not necessarily hand-writing a full transformer.
- Be ready for debugging-oriented live coding.
- Prepare small, correct implementations with tests and tradeoff discussion.
- Prioritize correctness, shape discipline, numerical stability, and performance reasoning.

Evidence note: these posts are less concrete than `1173457`/`1110121`, so treat them as process hints rather than confirmed question banks.

## ML System Design

### RAG over tables/notebooks for a coding/data agent

Source: `1175089`.

What to prepare:

- Design retrieval over Databricks assets such as tables and notebooks.
- Decide what to index: schema, table descriptions, lineage, notebook text, query history, ownership, freshness, permissions, and usage signals.
- Add retrieval + reranking, with filtering for noisy or unhelpful assets.
- Handle permissions and data governance so the agent cannot surface unauthorized assets.
- Define metrics: retrieval recall, answer usefulness, citation correctness, latency, freshness, and human feedback.
- Discuss cold start, stale notebooks, duplicated tables, and ambiguous user questions.

Interview framing: `1175089` says a senior staff interviewer asked MLE system design for a coding agent retrieving the best table/notebook.

### Harmful content detection for LLM outputs

Sources: `1173457`, `1172872`, `1110121`.

What to prepare:

- Define taxonomy: hate, harassment, self-harm, sexual content, violence, illegal advice, privacy leakage, prompt-injection-sensitive content.
- Build data strategy: labeled production examples, policy guidelines, synthetic/adversarial cases, human review, active learning.
- Model choices: prompt/classifier baseline, fine-tuned encoder/LLM judge, ensemble, thresholding by severity.
- Serving design: synchronous guardrail path, caching, fallback, latency budgets, logging, auditability.
- Evaluation: per-category precision/recall, calibration, false-positive cost, red-team sets, drift monitoring.
- Operations: escalation, appeals, policy versioning, monitoring and rollback.

Interview framing: all three MLE/Senior MLE posts mention harmful content detection as an ML design round.

### Notebook OOM prediction

Source: `1172872`.

What to prepare:

- Predict whether a notebook run will hit out-of-memory before or during execution.
- Features: code/static features, historical run telemetry, input data size, cluster memory, library versions, user/workspace history, Spark execution signals.
- Labels: OOM failures, near-OOM runs, retries with larger clusters; avoid leakage from post-failure logs.
- Model: start with interpretable baseline, then tree/sequence model if telemetry supports it.
- Product action: warn user, suggest cluster sizing, sample data, rewrite query, or auto-scale.
- Evaluation: recall on true OOMs, precision to avoid alert fatigue, time-to-warning, saved compute, user acceptance.
- Monitoring: data drift, cluster changes, workload seasonality, feedback loop from ignored/accepted suggestions.

Interview framing: `1172872` reports this as an ML design problem similar to Colab/notebook OOM prediction.

## Explicitly Excluded

- Frontend / React / UI system design.
- Traditional backend track and pure SDE/SWE loops.
- Pure infra/system programming: file systems, log writers, HDFS/S3-style design, network throttling, generic distributed data systems.
- NG/intern-only OA lists unless they directly support a Staff MLE topic.
- Generic Databricks interview process, recruiter/HM-only posts, and non-Databricks posts misfiled into the corpus.
