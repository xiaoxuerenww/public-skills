#ml-system-design 

### Phase 1: Problem Definition & Scoping

**Key Questions:**
- What is the business objective? (revenue, engagement, efficiency, safety)
- What are we trying to predict/classify? (labels, outputs)
- What's the scale? (QPS, data volume, users)
- What are the constraints? (latency, cost, accuracy requirements)

**Key Artifacts:**
- Requirements document (functional + non-functional)
- Success metrics (primary, secondary, guardrails)
- Baseline and target performance

**Example Scoping:**
```
Problem: Recommendation system for video platform
Input: User profile, watch history, context
Output: Top-K video recommendations per user
Scale: 1M DAU, <100ms latency requirement
Success Metric: CTR improvement, watch time
```

---

### Phase 2: Data & Feature Engineering

**Data Pipeline:**
1. **Collection**: Where does data come from? (user events, logs, databases)
2. **Storage**: How is it stored? (data warehouse, data lake, HDFS)
3. **Processing**: Cleaning, validation, deduplication
4. **Labeling**: Manual annotation, weak supervision, or synthetic labels

**Feature Engineering:**
1. **Feature Extraction**: Raw → meaningful signals
2. **Feature Selection**: High-impact features vs. dimensionality
3. **Feature Encoding**: Categorical, numerical, embeddings
4. **Feature Stores**: Centralized feature management for consistency

**Key Metrics:**
- Data freshness (how often is data updated?)
- Data quality (completeness, correctness)
- Feature correlation and importance
- Training/serving feature parity

---

### Phase 3: Model Architecture & Training

**Common Model Architectures:**
- **Linear/Logistic Regression**: Simple, interpretable, fast
- **Tree-Based (XGBoost, LightGBM)**: High performance, handles non-linear relationships
- **Neural Networks**: Deep learning, embeddings, flexibility
- **Ensemble Methods**: Combining multiple models

**Training Considerations:**
1. **Offline Training**: Batch processing for model updates
2. **Online/Continual Learning**: Real-time adaptation
3. **Hyperparameter Tuning**: Grid search, Bayesian optimization, AutoML
4. **Cross-validation**: Proper train/val/test splits

**Model Validation:**
- **Evaluation Metrics**: Accuracy, precision, recall, AUC, RMSE, NDCG, etc.
- **Offline Evaluation**: Metrics on held-out test set
- **Online Evaluation**: A/B tests, canary deployments
- **Bias & Fairness**: Disparate impact, representation

---

### Phase 4: Model Serving & Infrastructure

**Serving Options:**

| Approach | Latency | Scalability | Complexity | Use Case |
|----------|---------|-------------|-----------|----------|
| **Batch** | Hours | High | Low | Offline recommendations, analytics |
| **API Server** | 10-100ms | Medium | Medium | Real-time predictions, recommendations |
| **Edge** | <10ms | Medium | High | On-device ML, mobile apps |
| **Streaming** | Real-time | High | High | Real-time ranking, personalization |

**Infrastructure Stack:**
```
Request → Load Balancer 
       → Model Server (TensorFlow Serving, Triton, KServe)
       → Feature Store (retrieval, caching)
       → Model Registry (versioning, rollback)
       → Logging & Monitoring
```

**Key Considerations:**
- **Caching**: Reduce latency and load (feature caching, model predictions)
- **Batching**: Increase throughput by processing multiple requests together
- **Quantization**: Reduce model size and latency
- **Distillation**: Use smaller student models to approximate larger models

---

### Phase 5: Monitoring & Iteration

**Monitoring Metrics:**

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

**Alerting & Incident Response:**
- Alert on metric degradation
- Automated rollback if needed
- Post-mortem analysis

**Feedback Loop:**
- Collect predictions and outcomes
- Retrain models with new data
- A/B test improvements
