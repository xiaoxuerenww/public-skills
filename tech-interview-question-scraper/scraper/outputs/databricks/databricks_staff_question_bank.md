# Databricks Staff-Level Question Bank

Scope: local Databricks scrape in `outputs/databricks.md`, prioritized for Staff / Senior Staff prep as:

1. Applied AI
2. MLE
3. SWE / backend / infra

## What To Optimize For

Databricks appears much more question-bank-heavy than broad-theory-heavy. The recurring bar is not just "know the prompt"; posts repeatedly mention follow-up depth, production constraints, API/schema detail, testing, and bug-free execution under time pressure.

For Staff level, prepare every question in two layers:

- Implementation layer: clean code, edge cases, tests, complexity.
- Staff layer: product/API contract, production failure modes, scaling bottlenecks, observability, correctness guarantees, and tradeoffs.

## Priority 1: Applied AI

### RAG For Data Assets / Coding Agent

Source: `1175089`, posted 2026-04-30.

Prompt: An internal coding agent receives data-related user questions. Design how it retrieves the most relevant tables, notebooks, or other workspace assets so it can answer correctly.

Expected discussion:

- Retrieval + reranking architecture.
- What to index: table metadata, schemas, lineage, query logs, notebook text/code, comments, ownership, freshness, permissions.
- How to handle noisy or unhelpful notebooks and tables.
- Query understanding: user intent, entity linking, workspace context, historical usage.
- Ranking metrics: answer accuracy, asset hit rate, human acceptance, citation correctness, latency.
- Safety/permissions: only retrieve assets the user can access; avoid leaking table names or notebook content.
- Feedback loop: clicks, accepted answers, corrections, offline eval sets.

Staff-level bar:

- Separate candidate generation from reranking.
- Explain evaluation design, not just architecture.
- Make freshness, permissions, lineage, and noisy-assets handling first-class.

### Harmful Content Detection

Sources: `1173457`, `1172872`, posted 2026-04.

Prompt: Design an ML system to detect harmful LLM content.

Expected discussion:

- Label taxonomy: policy classes, severity, ambiguity, appeal/escalation.
- Model choices: classifier, LLM judge, rules, ensemble, active learning.
- Online serving path: pre-generation, post-generation, streaming moderation, fallback behavior.
- Data flywheel: sampling, human review, disagreement handling, adversarial examples.
- Metrics: precision/recall by harm type, false-positive cost, calibration, latency, coverage.
- Abuse resistance: prompt obfuscation, multilingual, context-dependent harm, jailbreaks.
- Ops: monitoring drift, incident response, model/version rollouts.

Staff-level bar:

- Talk explicitly about policy ambiguity and reviewer disagreement.
- Tie thresholds to product risk, not only model metrics.
- Include online monitoring and escalation paths.

### Predict Notebook OOM / Resource Failure

Source: `1172872`, posted 2026-04-13.

Prompt: Design an ML system to predict OOM issues for notebooks, similar to Colab-like execution.

Expected discussion:

- Signals: notebook code, cell history, input data sizes, Spark plan, library imports, previous runs, cluster size, memory pressure.
- Prediction target: probability of OOM, time-to-failure, recommended cluster/resource config.
- Feature extraction before execution versus during execution.
- Intervention: warning, autoscale, rewrite suggestion, sample-first execution, checkpoint.
- Metrics: prevented failures, false warning rate, user acceptance, cost increase.
- Cold start: new notebooks, new users, new data.

Staff-level bar:

- Frame this as a product intervention problem, not just binary classification.
- Discuss false positives because unnecessary warnings/autoscaling cost user trust and money.

### Applied AI Coding Screen: KV Store + QPS / Hit Counter

Sources: `1173790`, `1163734`, `1158524`, `1157471`, `1155270`.

Prompt: Implement an in-memory key-value store with `put/get` and an API for average QPS/load over the last 5 minutes. Follow-ups include saving space, 24-hour window, multiple events with the same timestamp, variable window size, and high throughput.

Expected implementation:

- Basic version: `dict` for values plus event tracking for `put/get`.
- Sliding-window queue for exact recent events.
- Bucketed ring buffer for high-throughput approximate or per-second aggregation.
- Correct expiration on every read/write/query.
- Multiple events in same timestamp bucket.

Staff-level follow-ups:

- Exact queue vs bucketed approximation.
- Memory bound for 5 minutes vs 24 hours.
- Multi-threaded updates and lock granularity.
- Sharding keys or metrics to reduce contention.
- Observability semantics: QPS over wall-clock duration vs active observed range.

## Priority 2: MLE

### ML Coding: Linear Regression Gradient Descent

Sources: `1173457`, `1172872`.

Prompt: Implement simple linear regression with gradient descent. Use MSE. Discuss learning rate, early stopping, convergence, and debug a bug.

Expected implementation:

- Forward: `y_pred = X @ w + b`.
- Loss: mean squared error, not just squared error sum.
- Gradients: `dW = 2/n * X.T @ (y_pred - y)`, `db = 2/n * sum(...)`.
- Training loop with learning rate and optional early stopping.
- Tests on synthetic data with known weights.

Staff-level follow-ups:

- Why loss may not converge: learning rate, missing mean, feature scale, bad initialization.
- Numeric stability and shape correctness.
- How to debug using loss curves and gradient norms.

### ML Tech Fit / Project Deep Dive

Sources: `1147731`, `1173457`, `1172872`, `1156010`.

Expected topics:

- ML performance-related coding.
- Deep dive into a project.
- Technical design conflict.
- Cross-functional collaboration.
- Critical feedback / disagreement.

Staff-level bar:

- Prepare one project with clear problem framing, model/system choices, production constraints, metrics, launch impact, and tradeoffs.
- Be ready to go from ML method to infra bottleneck to cross-functional decision.

### SQL / Data Systems Fundamentals

Sources: `1160799`, `1155225`.

Prompts seen:

- Query optimizer over a SQL query node structure; predicate pushdown is explicitly mentioned.
- OLAP vs OLTP.
- Data skew.

Expected discussion:

- Predicate pushdown, projection pruning, filter ordering, joins at a high level.
- Spark/distributed data intuitions: partitioning, shuffle, skew mitigation.
- OLAP vs OLTP storage and access patterns.

Staff-level bar:

- For Databricks, be able to connect ML product work to data platform fundamentals.
- Do not treat SQL/data systems as unrelated to Applied AI.

## Priority 3: SWE / Backend / Infra

### Architecture / System Design

#### Bookstore / Bookseller Aggregation

Sources: `1176356`, `1161741`, `1156010`.

Prompt: User submits ISBN, bid price, and payment method. System queries many downstream bookstores, finds the lowest price, buys if price <= bid, otherwise returns price; if no stock, notify user.

Staff-level focus:

- Async fan-out and partial result aggregation.
- Timeouts, circuit breakers, retries, provider-specific rate limits.
- Cache, TTL, request coalescing, thundering herd protection.
- Hold/order/charge consistency and compensation.
- Idempotency for duplicate purchase/charge requests.

#### Distributed File System / Google Drive / Dropbox

Sources: `1176894`, `1164871`, `1149122`.

Prompts:

- Distributed file system.
- Google Drive / Dropbox.
- Immutable files with recursive deletion.

Staff-level focus:

- Metadata service, namespace tree, file chunks, replication.
- Recursive delete semantics and tombstones.
- Consistency model, failure recovery, background GC.
- Permissions, sharing, versioning, audit logs.

#### Job Scheduler

Source: `1171295`.

Prompt: Design a job scheduler where each job is a DAG/list of tasks with dependencies.

Staff-level focus:

- DAG representation and dependency resolution.
- Task state machine and retries.
- Worker leasing, heartbeats, idempotency.
- Backpressure, priority, fairness.
- Recovery after scheduler crash.

#### Low-Level KV Cache / WAL / Durable KV Store

Sources: `1160799`, `1169434`, `1149185`, `1148433`.

Prompts:

- Single-machine in-memory cache with persistence via WAL.
- Durable KV store.
- KV cache + hit count.

Staff-level focus:

- WAL append path, fsync policy, crash recovery.
- Compaction/snapshotting.
- Locking and critical-section minimization.
- Sharding to avoid lock contention.
- Eviction policy and correctness under concurrent access.

#### Log Writer / Multi-threaded Event Recorder

Sources: `1163200`, `1164871`, `1157037`, `1154779`, `1156010`.

Prompt: Multi-threaded log writer or event recorder; writes to disk must be synchronous.

Staff-level focus:

- Producer/consumer queue.
- Ordering guarantees.
- Batching vs sync durability.
- Backpressure when disk is slow.
- Flush, fsync, rotation, recovery.

#### Payments / Stock / Commerce-Like Systems

Sources: `1171816`, `1163200`, `1156044`.

Prompts:

- Stock trading system with third-party order APIs.
- Visa/payment system.
- Game shop with credits, purchase, refund.

Staff-level focus:

- Idempotency keys.
- Pending states.
- External API failure and retry semantics.
- Transaction boundaries.
- Duplicate request handling.
- Compensation and reconciliation.

#### Chat / Slack / WhatsApp

Sources: `1174967`, `1154779`, `1157037`, `1156010`.

Prompt: Design chat/Slack/WhatsApp-like systems. Some posts say interviewers ask for pseudo-code/API/schema rather than classic box-diagram design.

Staff-level focus:

- Conversation/message schema.
- Delivery semantics and read receipts.
- WebSocket vs polling vs push.
- Fanout model.
- Offline users and sync.
- Search/retention/moderation if asked.

### Coding / Algorithm Bank

#### Find Optimal Commute

Sources: `1176846`, `1174371`, `1175668`, `1164869`, `1164006`, `1156123`, `1155285`, `1154062`.

Prompt: Given a 2D grid with `S`, `D`, `X`, and transportation modes `1..4`, plus time/cost per mode, return the fastest mode, tie-breaking by cost.

Variants:

- Run BFS once per mode.
- Optimize to one scan / one BFS with mode in state.
- Allow mode switching with penalty.
- Limit number of switches.
- Dijkstra-style follow-up when edge costs differ.

Must know:

- Clarify if path must stay within one mode.
- Tie-breaking order.
- Duplicate priority handling.
- Test unreachable destination, multiple fastest modes, start/destination adjacent, blocked path.

#### CIDR / IP Firewall

Sources: `1165653`, `1163200`, `1162425`, `1157120`, `1156044`, `1153441`, `1153413`, `1152588`, `1160799`.

Prompt: Given ordered CIDR allow/deny rules and an input IP, return the first matching rule/status.

Variants:

- Input is CIDR block instead of single IP.
- Determine if a CIDR is fully allowed/blocked.
- Handle overlapping allow/deny ranges.
- Merge/subtract ranges.

Must know:

- Convert IPv4 to 32-bit int.
- CIDR mask and range `[start, end]`.
- Ordered first-match semantics.
- Range coverage/subtraction for CIDR-input follow-up.

#### Fibonacci Tree Path

Sources: `1170829`, `1171221`, `1161944`, `1165439`, `1159207`, `1156044`.

Prompt: Fibonacci tree has recursively defined subtrees and preorder labels. Given order `k` and nodes `a,b`, return path from `a` to `b` without constructing the tree.

Must know:

- Precompute subtree sizes up to `k`.
- Map node index into left/right subtree intervals.
- Get root-to-node path for each target.
- LCA by comparing paths.
- Complexity `O(k)`, use `long`/BigInt awareness.

#### RLE + Bit-Packing Encoding / Decoding

Sources: `1163200`, `1169579`, `1156044`, `1154491`, `1156010`, `1157037`.

Prompt: Encode/decode an integer stream using RLE and bit-packing. Choose encoding based on constraints.

Details seen:

- Encoder receives one int at a time.
- RLE has minimum run length.
- Bit-packing packs fixed-size groups, often 8 values.
- Decoder may need iterator semantics.
- Edge cases: negative values, int max/min, stream ending mid-run.

Must know:

- State machine implementation.
- Flush behavior at stream end.
- Tests for boundary lengths and mixed encodings.

#### Lazy Array

Sources: `1171295`, `1172872`, `1169434`, `1164871`, `1155285`.

Prompt: Implement lazy array transformations and prove/test laziness.

Must know:

- Store base data plus deferred operations.
- Materialize only on access/iteration.
- Compose map/filter-like operations if asked.
- Unit test by stubbing function calls and asserting they are not invoked until materialization.

#### Snapshot Set / MVCC Iterator

Sources: `1174847`, `1161180`.

Prompt: Implement snapshot set with iterator; maintain history/MVCC-style snapshot ids.

Must know:

- `add/remove/contains`.
- Snapshot/iterator returns stable view even after mutations.
- Per-key logs vs global logs tradeoff.
- `__iter__` returning `self` if writing Python iterator.

#### Hit Counter / KV QPS

Sources: same as Applied AI coding screen.

Treat as cross-role high priority. Databricks uses this for AI Eng, Applied AI, SWE, and screen loops.

#### Customer Revenue

Source: `1163087`.

Prompt: Customer revenue, sometimes top-k becomes least-k. Follow-up: nested revenue and read-heavy/write-heavy optimization.

Must know:

- Revenue aggregation over customer/referral graph.
- Top/least k maintenance.
- Nested revenue propagation.
- Read-heavy vs write-heavy tradeoffs.

#### Tic Tac Toe

Sources: `1162425`, `1161617`, `1147384`, `1148433`.

Prompt: Design/implement `m*n` tic-tac-toe.

Must know:

- O(1) or near-O(1) win checks using row/col/diag counters.
- Generalized board dimensions.
- Tests for invalid moves, draw, repeated moves.

#### Query Optimizer / Predicate Pushdown

Source: `1160799`.

Prompt: Given a data structure representing a SQL query, implement optimizations such as predicate pushdown.

Must know:

- Represent relational operators as nodes.
- Push filters below projections/joins where semantically valid.
- Preserve correctness with column references.

This is lower-frequency but high relevance for Databricks data systems.

#### Other Lower-Frequency Coding Prompts

- Randomly connect node groups into one connected graph with a uniformly sampled valid edge set: `1175668`, `1173709`.
- File encryption tree DP with file vs directory encryption APIs: `1174298`.
- Cipher cover intervals, delete by cover index, merge/simplify intervals: `1173457`.
- Tetris-like falling block simulation: `1154835`.
- LC 438 / first anagram and scalable follow-up: `1174703`, `1161617`, `1154914`.
- Durable KV store: `1149185`, `1148433`.
- Design song list / reorder list OOD: `1154568`.

## Recommended Prep Order

1. Applied AI design: RAG over tables/notebooks, harmful content detection, notebook OOM prediction.
2. Cross-role coding: KV store + QPS/hit counter, optimal commute, CIDR firewall.
3. MLE coding: linear regression gradient descent, debugging convergence, early stopping.
4. Systems design: bookstore, distributed file system, job scheduler, KV/WAL, log writer.
5. Databricks-specific coding bank: Fibonacci tree, RLE/bit-packing, lazy array, snapshot set/MVCC.
6. Behavioral/project deep dive: one Staff-level ML/platform project with technical conflict, ambiguity, feedback, and cross-functional tradeoffs.

## Staff-Level Checklist

For every prompt, prepare:

- Clean baseline solution.
- Edge cases and direct tests.
- Complexity and bottleneck.
- Production contract: API semantics, consistency, failure handling.
- Scaling path: sharding, caching, batching, approximate vs exact.
- Concurrency story if mutable/shared state exists.
- Observability: metrics, logs, alerts, debugging hooks.
- Tradeoff: when the simple design is enough and when to upgrade.

# Prep checklist
1. Coding data structures:
    
    - Interval delete/update/merge.
    - SnapshotSet / snapshot iterator.
    - Lazy array and testing laziness.
    - KV cache / hit counter / sliding-window QPS.
2. ML Fundamentals:
    
    - Word2vec training.
    - Transformer architecture.
    - Query/key/value reasoning.
    - Linear regression gradient descent from scratch.
    - MSE gradient, learning rate, early stopping, convergence debugging, shape checks.
3. ML system design:
    
    - Harmful content detection for LLM outputs.
    - Notebook OOM prediction.
    - Production moderation: taxonomy, thresholds, human review, adversarial eval, monitoring.
4. Behavioral:
    
    - Customer feedback to improve product.
    - Data-driven decision.
    - Technical design conflict.
    - Challenging project with Staff+ scope.