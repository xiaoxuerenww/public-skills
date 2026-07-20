# Inference API Problem

Based on the posts and replies in [anthropic.md](/Users/aaronteng/Development/scraper/outputs/anthropic/anthropic.md), the `Inference API` prompt is the most common Anthropic system design question family, though it appears under slightly inconsistent labels like `inference api`, `inference system`, `batch inference`, `batch GPU requests`, and even mistyped once as `reference API`.

## Most Complete Problem Description

The most complete reconstruction is:

You have a cluster of GPU servers. Each server exposes an existing inference API that takes `List[str]` as input and returns `List[str]` as output. The key property is that inference latency is roughly the same for batch sizes from `1` to `100`, so the system only becomes efficient if requests are aggregated into batches before hitting the GPU-backed inference API. Your job is to design the HTTP service / middleware layer that sits in front of those GPU workers and uses them efficiently for a ChatGPT-like or general LLM-style product.

What the design seems to include:

- Client-facing API layer.
- Request ingestion.
- Queueing or buffering.
- Batch formation and dispatch to GPU-backed inference workers.
- Result retrieval path, often described as `post & poll`.
- Scheduling, scaling, and operational control.

What is usually out of scope:

- Redesigning the actual model internals.
- Low-level inference optimizations like speculative decoding, continuous batching, prefix caching inside the model server, etc.
- Streaming token output, in many reported variants.

What the interview seems to assume:

- The inference service itself is largely a black box.
- The real problem is the middleware/control plane around it.
- It is usually `near-real-time`, not a long-running offline batch system.

Useful source points:

- Core description: [人类学SWE全套](https://www.1point3acres.com/home/pins/1116057)
- Earlier full wording: [人类学全套](https://www.1point3acres.com/home/pins/1098075)
- Black-box clarification: [人类学SD Q1跟之前不一样了？](https://www.1point3acres.com/home/pins/1161165)
- `post & poll`, no streaming: [Anthropic全套挂经](https://www.1point3acres.com/home/pins/1141635)

## Follow-Up Questions Interviewers Like

These show up repeatedly:

- How exactly do requests flow through the system?
  Request intake, queueing, batch formation, dispatch, and how results are returned.
- How do you batch?
  Time-based vs size-based batching, max batch size, batch timeout, fairness, head-of-line blocking.
- How many GPUs do you need?
  Several candidates report being pushed on concrete capacity estimation, not just architecture.
- How do you scale?
  Queue sharding, worker autoscaling, thresholds, admission control.
- What happens during traffic surges?
  Backpressure, throttling, rate limiting, degraded service behavior.
- What if `CPU is idle but GPU is saturated`?
  This is explicitly reported in a recent post.
- What happens when the cluster is almost full?
  One interviewer asked how many GPUs would actually be carrying workload and what the queue length would look like.
- What metrics do you monitor?
  GPU utilization, GPU availability, latency, inference error rate, queue depth, backlog age, drop/retry rates.
- Where do you apply backpressure?
  At gateway, queue, aggregator, or poller.
- How do priorities work?
  Free vs paid tiers, separate queues, traffic prioritization.
- What if half the GPUs go down?
  Dynamic rate-limit tightening and failure signaling came up explicitly.
- Do you need caching?
  If you bring up caching, interviewers may dive deep, so be precise.
- How do model updates happen?
  Not always asked, but some interviewers pushed into model update/control plane concerns.
- Is the API sync or async?
  The strongest signal is: often effectively sync or near-real-time, sometimes implemented as `post & poll`, but not "submit today, answer tomorrow."

High-signal sources:

- Numerical push: [人类学电面经验](https://www.1point3acres.com/home/pins/1175484)
- Capacity/queue-depth push: [人类学 昂赛 挂经](https://www.1point3acres.com/home/pins/1151263)
- Dynamic rate limiting/failure handling: [Anthropic SD inference 挂经讨论](https://www.1point3acres.com/home/pins/1145567)
- Recent `CPU idle, GPU busy` push: [新鲜出炉的人类学面经](https://www.1point3acres.com/home/pins/1177358)

## Mistakes People Tend To Make

- Treating it like generic system design.
  Candidates who prepared a standard architecture often got dragged into operational details they had not quantified.
- Staying too high-level.
  Interviewers seem to want actual numbers, thresholds, and policies.
- Ignoring the batching economics.
  The whole point is exploiting the "1 to 100 items cost about the same" API behavior.
- Designing the model server itself.
  Multiple posts suggest the inference engine should be treated as a black box.
- Over-indexing on offline async patterns.
  This usually sounds wrong for the common prompt variant.
- Not having a clear control-loop story.
  Queue size alone is not enough; candidates got pushed on earlier failure signals like GPU availability, latency, and error rate.
- Using one queue for all users.
  One candidate explicitly realized afterward this was a mistake; tiers should likely be separated.
- Bringing up caching too casually.
  Once mentioned, interviewers may dig into invalidation, similarity checks, routing affinity, or whether that cache even belongs in your layer.
- Focusing too much on fault tolerance and too little on utilization/scheduling.
  Several posts imply the heart of the problem is aggregation, scheduling, and GPU efficiency.

## Interviewer's Expectation

What they appear to want:

- A clean middleware design around an existing inference API.
- A strong batching strategy.
- Concrete capacity reasoning.
- Clear operational thinking: queueing, scaling, throttling, monitoring.
- Awareness that GPU is the scarce resource.
- Fast adaptation when challenged with edge cases.
- Good discussion of tradeoffs, not just one "perfect" design.

A good answer likely sounds like:

- "Here is the request path."
- "Here is how we batch and when we flush."
- "Here is how we choose workers."
- "Here is how we estimate required GPUs from traffic and latency goals."
- "Here is what happens under overload."
- "Here is how we prioritize users and observe the system."

One subtle expectation: they often seem to care more about whether you can reason operationally than whether you can name every standard component.

## Useful Posts

These are the best non-duplicate posts for this specific prompt family:

- [新鲜出炉的人类学面经](https://www.1point3acres.com/home/pins/1177358)
  Most recent concise confirmation that this is still active; explicitly mentions `CPU idle, GPU busy` and scaling pressure.
- [人类学电面经验](https://www.1point3acres.com/home/pins/1175484)
  Best recent evidence that interviewers push on `GPU estimation`, `queue sharding`, and `scaling thresholds`.
- [人类学SD Q1跟之前不一样了？](https://www.1point3acres.com/home/pins/1161165)
  Best clarification that the `model service is a black box` and you should focus on middleware, scheduling, and scaling.
- [人类学 昂赛 挂经](https://www.1point3acres.com/home/pins/1151263)
  Strong details on interviewer follow-ups like `batch input`, `how many GPUs are active near saturation`, and `batch queue length`.
- [Anthropic SD inference 挂经讨论](https://www.1point3acres.com/home/pins/1145567)
  Best source for advanced follow-ups: dynamic rate limiting, overload handling, queue partitioning by user tier, and GPU failure signals.
- [Anthropic全套挂经](https://www.1point3acres.com/home/pins/1141635)
  Best source for the `post & poll`, `batch operation`, `no need to stream` variant and near-real-time framing.
- [Anthropic 挂经](https://www.1point3acres.com/home/pins/1137926)
  Useful manager/EM-flavored variant with `router`, `traffic prioritization`, `batching service`, and `query cache`.
- [人类学SWE全套](https://www.1point3acres.com/home/pins/1116057)
  Best compact source for the core prompt plus concrete follow-ups like queueing, batching, surge handling, monitoring, and GPU estimation.

## Other Useful Info

- The question ID is unstable.
  The same family gets called `Q1`, and some posters confuse it with other design questions. Do not rely on the number.
- There may be two nearby prompt families.
  Some posts distinguish a `concurrent inference API` from a `batch LLM inference API`.
- Another newer infra prompt is `model distribution to GPU hosts`.
  Do not confuse that with this question.
- Some interviewers push deeper than the core prompt technically requires.
  If you volunteer extras like prompt cache, model update workflow, or async architecture, be ready to defend them.

The simplest preparation model is: treat this as a `GPU-aware batching middleware` design problem, not as "design ChatGPT" in the broad sense.
