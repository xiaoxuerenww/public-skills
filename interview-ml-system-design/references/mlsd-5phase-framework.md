#ml-system-design 

### Phase 1: Problem Definition & Scoping

**Key Questions:**
- What is the business objective? (revenue, engagement, efficiency, safety)
- What are we trying to predict/classify/generate? (labels, outputs, free-form text, decisions)
- What's the scale? (QPS, data volume, users)
- What are the constraints? (latency, cost, accuracy requirements)

**Key Artifacts:**
- Requirements document (functional + non-functional)
- Success metrics (primary, secondary, guardrails)
- Baseline and target performance

**Example Scoping (Traditional ML):**
```
Problem: Recommendation system for video platform
Input: User profile, watch history, context
Output: Top-K video recommendations per user
Scale: 1M DAU, <100ms latency requirement
Success Metric: CTR improvement, watch time
```

**AI/LLM-Specific Scoping:**

| Dimension | Questions to ask |
|-----------|-----------------|
| **Output type** | Deterministic (classification, ranking) or generative (free-form text, code, reasoning)? |
| **Token budget** | What's the acceptable cost per request? Per-user per-day? |
| **Hallucination tolerance** | Zero-tolerance (medical, legal) or best-effort (creative, exploratory)? |
| **Latency profile** | Is streaming acceptable? First-token latency vs. total latency? |
| **Privacy** | Can data leave the org? On-prem LLM required? PII in prompts? |
| **Determinism** | Does the same input need the same output? (caching, reproducibility) |

**Example Scoping (AI/LLM):**
```
Problem: Internal knowledge-base Q&A agent
Input: Employee question + access-controlled document corpus
Output: Grounded answer with source citations
Scale: 10K employees, ~500 queries/day, <5s end-to-end
Hallucination tolerance: Low — answers must cite sources, "I don't know" preferred over guessing
Token budget: ~$0.02/query average
Success Metric: Answer accuracy (human eval), citation faithfulness, user satisfaction
```

---

### Phase 2: Data & Context Engineering

**Data Pipeline (Traditional ML):**
1. **Collection**: Where does data come from? (user events, logs, databases)
2. **Storage**: How is it stored? (data warehouse, data lake, HDFS)
3. **Processing**: Cleaning, validation, deduplication
4. **Labeling**: Manual annotation, weak supervision, or synthetic labels

**Feature Engineering (Traditional ML):**
1. **Feature Extraction**: Raw → meaningful signals
2. **Feature Selection**: High-impact features vs. dimensionality
3. **Feature Encoding**: Categorical, numerical, embeddings
4. **Feature Stores**: Centralized feature management for consistency

**Context Engineering (AI/LLM):**

The equivalent of "feature engineering" for LLM systems is building the **context pipeline** — what information reaches the model and how.

1. **RAG vs. Fine-tuning Decision**

| Approach | When to use | Tradeoffs |
|----------|-------------|-----------|
| **RAG** | Dynamic knowledge, frequent updates, attribution needed | Higher latency, retrieval errors, context window limits |
| **Fine-tuning** | Stable domain knowledge, style/format adaptation, latency-critical | Expensive retraining, knowledge cutoff, no attribution |
| **Both** | Domain-adapted model + real-time knowledge retrieval | Complexity, cost of maintaining both pipelines |

2. **RAG Pipeline Design**
   - **Ingestion**: Document parsing, format handling (PDF, HTML, tables, code)
   - **Chunking strategy**: Fixed-size, semantic, hierarchical, or document-structure-aware
   - **Embedding model**: Selection (dense vs. sparse), dimensionality, domain fit
   - **Vector store**: Choice (Pinecone, Weaviate, pgvector, FAISS), indexing strategy
   - **Retrieval**: Dense retrieval, sparse (BM25), hybrid, reranking
   - **Context assembly**: Chunk selection, ordering, deduplication, context window packing

3. **Context Window Management**
   - Total budget allocation: system prompt, retrieved context, conversation history, output
   - Long-context strategies: summarization, sliding window, hierarchical retrieval

**Key Metrics:**

| Traditional ML | AI/LLM |
|----------------|--------|
| Data freshness | Index freshness (how stale is the vector store?) |
| Data quality (completeness, correctness) | Chunk quality (are chunks self-contained and coherent?) |
| Feature correlation and importance | Retrieval precision/recall (does the right context get retrieved?) |
| Training/serving feature parity | Embedding drift (do new documents embed consistently?) |

---

### Phase 3: Model Architecture & Orchestration

**Model Selection (Traditional ML):**
- **Linear/Logistic Regression**: Simple, interpretable, fast
- **Tree-Based (XGBoost, LightGBM)**: High performance, handles non-linear relationships
- **Neural Networks**: Deep learning, embeddings, flexibility
- **Ensemble Methods**: Combining multiple models

**Training Considerations (Traditional ML):**
1. **Offline Training**: Batch processing for model updates
2. **Online/Continual Learning**: Real-time adaptation
3. **Hyperparameter Tuning**: Grid search, Bayesian optimization, AutoML
4. **Cross-validation**: Proper train/val/test splits

**Model Validation (Traditional ML):**
- **Evaluation Metrics**: Accuracy, precision, recall, AUC, RMSE, NDCG, etc.
- **Offline Evaluation**: Metrics on held-out test set
- **Online Evaluation**: A/B tests, canary deployments
- **Bias & Fairness**: Disparate impact, representation

**LLM Selection & Orchestration (AI/LLM):**

1. **Model Selection**

| Factor | Considerations |
|--------|---------------|
| **Capability** | Reasoning depth, code generation, multilingual, multimodal |
| **Context window** | 4K–1M+ tokens; impacts RAG design and cost |
| **Latency** | Time-to-first-token, tokens/second, total generation time |
| **Cost** | Per-token pricing (input vs. output), batch vs. real-time |
| **Privacy** | API-hosted vs. self-hosted, data residency requirements |
| **Reliability** | Rate limits, uptime SLAs, provider redundancy |

2. **Prompt Architecture**
   - System prompt design: role, constraints, output format, few-shot examples
   - Prompt templating and versioning (treat prompts as code artifacts)
   - Chain-of-thought, structured output (JSON mode), tool-use instructions

3. **Multi-Model Routing**
   - Route easy queries to cheap/fast models, hard queries to capable/expensive models
   - Classifier-based routing vs. cascading (try cheap first, escalate on low confidence)
   - Fallback chains: primary model → backup model → graceful degradation

4. **Agentic & Tool-Use Design**
   - Agent loop: plan → act → observe → repeat
   - Tool selection and API design for LLM consumption
   - Max-step limits and circuit breakers to prevent runaway loops
   - Single agent with tools vs. multi-agent orchestration (single agent usually wins)

---

### Phase 4: Serving, Infrastructure & Safety

**Serving Options (Traditional ML):**

| Approach | Latency | Scalability | Complexity | Use Case |
|----------|---------|-------------|-----------|----------|
| **Batch** | Hours | High | Low | Offline recommendations, analytics |
| **API Server** | 10-100ms | Medium | Medium | Real-time predictions, recommendations |
| **Edge** | <10ms | Medium | High | On-device ML, mobile apps |
| **Streaming** | Real-time | High | High | Real-time ranking, personalization |

**Infrastructure Stack (Traditional ML):**
```
Request → Load Balancer 
       → Model Server (TensorFlow Serving, Triton, KServe)
       → Feature Store (retrieval, caching)
       → Model Registry (versioning, rollback)
       → Logging & Monitoring
```

**Key Considerations (Traditional ML):**
- **Caching**: Reduce latency and load (feature caching, model predictions)
- **Batching**: Increase throughput by processing multiple requests together
- **Quantization**: Reduce model size and latency
- **Distillation**: Use smaller student models to approximate larger models

**LLM Serving & Cost Control (AI/LLM):**

1. **Inference Infrastructure**
   - API providers (OpenAI, Anthropic, Google) vs. self-hosted (vLLM, TGI, Triton)
   - GPU provisioning: instance types, autoscaling, spot vs. on-demand
   - Streaming responses (SSE) for perceived latency reduction

2. **Cost Optimization**

| Technique | Mechanism | Savings |
|-----------|-----------|---------|
| **Prompt compression** | Remove redundant context, shorten system prompts | 20-50% token reduction |
| **Semantic caching** | Cache responses for semantically similar queries | Avoid repeat LLM calls |
| **Model routing** | Cheap model for easy queries, expensive for hard | 50-70% cost reduction |
| **Batch API** | Async processing for non-real-time tasks | 50% cost reduction |
| **Context pruning** | Retrieve fewer, higher-quality chunks | Fewer input tokens |

3. **Safety & Guardrails**

| Threat | Defense |
|--------|---------|
| **Hallucination** | RAG grounding, citation requirements, confidence thresholds, "I don't know" fallback |
| **Prompt injection** | Input sanitization, instruction hierarchy, system prompt hardening |
| **PII leakage** | PII detection/redaction in inputs and outputs, data residency controls |
| **Toxic output** | Output classifiers, content filters, refusal patterns |
| **Jailbreaking** | Input/output guardrail models, adversarial testing |
| **Abuse/cost attacks** | Rate limiting, token budgets per user, anomaly detection |

---

### Phase 5: Evaluation, Monitoring & Iteration

**Monitoring Metrics (Traditional ML):**

1. **Model Performance**
   - Accuracy, precision, recall, AUC
   - Online metrics (CTR, conversion, revenue)
   - Business KPIs

2. **System Health**
   - Latency (p50, p99, p99.9)
   - Throughput (QPS)
   - Error rate
   - Cache hit rate

3. **Data Quality**
   - Data drift (feature distributions changing)
   - Concept drift (model assumptions breaking)
   - Missing values, out-of-range values

**Alerting & Incident Response (Traditional ML):**
- Alert on metric degradation
- Automated rollback if needed
- Post-mortem analysis

**Feedback Loop (Traditional ML):**
- Collect predictions and outcomes
- Retrain models with new data
- A/B test improvements

**LLM Evaluation & Monitoring (AI/LLM):**

1. **Offline Evaluation**

| Metric | What it measures | How |
|--------|-----------------|-----|
| **Faithfulness** | Does the output match the retrieved context? | LLM-as-judge, NLI models |
| **Answer relevance** | Does the output answer the question? | LLM-as-judge, human eval |
| **Context precision** | Was the retrieved context relevant? | Retrieval metrics (MRR, NDCG) |
| **Groundedness** | Are claims traceable to sources? | Citation verification |
| **Harmfulness** | Does the output contain unsafe content? | Safety classifiers |

2. **Online Monitoring**
   - Per-request cost tracking (input tokens, output tokens, model used)
   - Latency breakdown: retrieval time, LLM inference time, post-processing
   - Guardrail trigger rate (how often do safety filters fire?)
   - Hallucination rate (flagged by users or automated checks)
   - Cache hit rate for semantic caching

3. **Evaluation Infrastructure**
   - Golden test sets: curated question-answer pairs for regression testing
   - LLM-as-judge pipelines: automated quality scoring on sampled traffic
   - Human evaluation workflows: for high-stakes or ambiguous outputs
   - Prompt regression testing: run golden set after every prompt change

4. **Iteration & Feedback Loops**
   - Prompt versioning and A/B testing (treat prompts like model versions)
   - RAG pipeline tuning: chunking size, retrieval top-K, reranker thresholds
   - Fine-tuning triggers: when prompt engineering plateaus, consider fine-tuning
   - User feedback collection: thumbs up/down, corrections, escalations
   - Continuous retrieval index updates: new documents, stale content removal
