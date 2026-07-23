---
title: ML System Design - Quick Reference & Cheat Sheet
created: 2026-04-13
tags: [ml-systems, quick-reference, cheat-sheet]
---

# Quick Reference & Cheat Sheet

Quick lookup guide for common concepts, metrics, and decision trees.

---

## 🎯 Interview Framework (5-Step Approach)

### 1. Ask Clarifying Questions (5 min)
- **Scale**: QPS, DAU, data volume, storage requirements
- **Latency**: What's acceptable? (ms vs seconds vs batch)
- **Accuracy**: What metrics matter? (AUC, precision, recall, RMSE, NDCG)
- **Cost**: Budget constraints? On-prem vs cloud?
- **Constraints**: Privacy, fairness, interpretability requirements?

### 2. High-Level Approach (5 min)
- **Problem type**: Classification? Ranking? Clustering?
- **Data sources**: Where does data come from?
- **Model type**: Linear, tree, neural, ensemble?
- **Serving**: Batch, API, edge, streaming?

### 3. Deep Dive (15-20 min)
- **Data pipeline**: Collection → storage → processing
- **Feature engineering**: Key features and feature store
- **Model architecture**: Model choice and training strategy
- **Serving infrastructure**: How predictions get to users
- **Monitoring**: How we detect issues and iterate

### 4. Trade-offs & Optimization (5 min)
- **Accuracy vs Latency**
- **Complexity vs Simplicity**
- **Cost vs Performance**

### 5. Scale & Edge Cases (5 min)
- **Cold start problem**
- **Online vs offline learning**
- **Model versioning & rollback**

---

## 📊 Model Selection Decision Tree

```
Problem Type?
├─ Classification (binary/multi-class)
│  ├─ Simple, interpretable → Logistic Regression
│  ├─ Non-linear patterns → XGBoost, LightGBM
│  └─ Complex features → Neural Network
│
├─ Regression
│  ├─ Linear relationships → Linear Regression
│  ├─ Non-linear patterns → Tree-based methods
│  └─ Time-series → LSTM, Transformer
│
├─ Ranking / Recommendation
│  ├─ Collaborative filtering → Matrix factorization, embeddings
│  ├─ Content-based → Feature similarity
│  └─ Hybrid → Combine multiple approaches
│
└─ Clustering
   ├─ Spherical clusters → K-Means
   ├─ Arbitrary shape → DBSCAN
   └─ Hierarchical → Hierarchical clustering
```

---

## ⚡ Latency & Throughput Quick Guide

| Scenario | Latency Requirement | Approach |
|----------|-------------------|----------|
| **Batch processing** | Hours | Spark/Hadoop |
| **Offline analytics** | Minutes | SQL, Presto |
| **Search results** | <100ms | Cached, pre-computed |
| **Feed ranking** | 100-500ms | Lightweight model |
| **Real-time bidding** | <50ms | Simple rules, cache |
| **On-device** | <100ms | Lightweight, quantized |

---

## 🔄 Serving Architecture Decision Matrix

| Requirement | Batch | API | Edge | Streaming |
|-------------|-------|-----|------|-----------|
| **Real-time** | ❌ | ✅ | ✅ | ✅ |
| **Latency** | High | Medium | Low | Medium |
| **Scalability** | High | Medium | Limited | High |
| **Complexity** | Low | Medium | Medium | High |
| **Cost** | Low | Medium | Low | High |
| **Example** | Daily report | Recommendation | Mobile app | Real-time ranking |

---

## 📈 Key Metrics by Use Case

### Recommendation Systems
- **CTR**: Click-through rate
- **Conversion**: Purchase/desired action
- **Engagement**: Watch time, session length
- **Diversity**: Avoid filter bubbles
- **Freshness**: New content distribution
- **Coverage**: % of items with potential to be recommended

### Classification
- **Accuracy**: Overall correctness (imbalanced data? Use others)
- **Precision**: False positives (cost matters? focus here)
- **Recall**: False negatives (missing positive cases)
- **F1**: Harmonic mean (balanced metric)
- **AUC-ROC**: Threshold-independent, good for imbalanced
- **AUC-PR**: Better for highly imbalanced datasets

### Ranking
- **NDCG**: Normalized Discounted Cumulative Gain (best for ranking)
- **MAP**: Mean Average Precision
- **MRR**: Mean Reciprocal Rank
- **Precision@K**: How many of top-K are relevant
- **Recall@K**: Coverage of relevant items

### Regression
- **MAE**: Mean Absolute Error (interpretable)
- **RMSE**: Root Mean Squared Error (punishes large errors)
- **MAPE**: Mean Absolute Percentage Error
- **R²**: Variance explained

---

## 💾 Feature Store Pattern

```
Raw Data → Feature Computation → Feature Store
                                     ├─ Online (low-latency retrieval)
                                     └─ Offline (historical data)
                                     
Serving:
Request → Feature Retrieval → Model → Prediction
```

**Tools**: Feast, Tecton, Hopsworks

**Key concepts**:
- **Point-in-time correctness**: No data leakage from future
- **Online/offline parity**: Same features in training and serving
- **Caching**: Reduce latency and load

---

## 🔍 Data Drift vs Concept Drift

| Type | Definition | Impact | Detection |
|------|-----------|--------|-----------|
| **Data Drift** | Input distribution changes | Model accuracy ↓ | Statistical tests (KS, χ²) |
| **Concept Drift** | Label distribution changes | Model accuracy ↓ | Monitor target metrics |
| **Covariate Shift** | Feature distributions change | Model accuracy ↓ | KL divergence, Kolmogorov-Smirnov |
| **Label Shift** | Label proportions change | Calibration issues | Check label distribution |

**Monitoring approach**:
- Compare train vs serving distributions (statistical tests)
- Monitor model performance on holdout test set
- Alert if metrics degrade >X%

---

## 🎲 A/B Testing Essentials

### Statistical Significance
- **Sample size**: Larger = faster detection, but need more traffic
- **Significance level (α)**: Usually 0.05
- **Power (1-β)**: Usually 0.8 (80% chance of detecting true effect)
- **Formula**: n = 2σ²(Z_α + Z_β)² / δ²

### Common Pitfalls
- ❌ Multiple testing without correction (Bonferroni)
- ❌ Peeking at results early (increases false positive rate)
- ❌ Not accounting for variation by user/item
- ❌ Running tests too short (not enough samples)

### Variants
- **A/B test**: Control vs treatment
- **A/B/n test**: Multiple variants
- **Holdout test**: New vs old
- **Interleaved test**: Ranking-specific, less traffic needed

---

## 🚨 Common Failure Modes & Fixes

| Problem | Cause | Solution |
|---------|-------|----------|
| **Poor accuracy** | Bad features, small dataset | Feature engineering, data collection |
| **High latency** | Slow feature retrieval, heavy model | Caching, quantization, distillation |
| **Data drift** | Distribution changed | Monitor + retrain on new data |
| **Cold start** | No history for new users/items | Hybrid approach, content-based fallback |
| **Bias/fairness** | Skewed training data | Stratified sampling, fairness constraints |
| **Single point of failure** | No backup model | Multi-model ensemble, fallback rules |

---

## 🛠️ Quick Tech Stack Reference

### Data Processing
- **Batch**: Spark, Hadoop, Presto, BigQuery
- **Streaming**: Kafka, Flink, Storm
- **Scheduling**: Airflow, Kubeflow, Prefect

### Feature Store
- Feast (open-source, simple)
- Tecton (managed, enterprise)
- Hopsworks (full stack)

### Model Training
- TensorFlow, PyTorch, Scikit-learn
- Spark MLlib (distributed)
- AutoML: AutoGluon, H2O AutoML

### Model Serving
- TensorFlow Serving (TF-focused)
- Triton (multi-framework)
- Seldon Core (Kubernetes-native)
- BentoML (Python-friendly)

### Monitoring
- Evidently AI (drift detection)
- Great Expectations (data validation)
- Prometheus + Grafana (metrics)
- Datadog (observability)

### Experiment Tracking
- MLflow (open-source, popular)
- Weights & Biases (managed)
- Neptune.ai (collaborative)

---

## 📝 Common Interview Scenarios

### Scenario 1: YouTube Recommendation
**Constraints**: 2B users, <100ms latency, maximize watch time

**Approach**:
1. **Two-stage**: Candidate gen (fast) → Ranking (accurate)
2. **Candidate gen**: Collaborative filtering, embeddings (fast)
3. **Ranking**: Complex model with user/content features
4. **Serving**: Cache candidates, score in real-time
5. **Monitoring**: Watch time, completion rate, diversity

---

### Scenario 2: Fraud Detection
**Constraints**: High precision (reduce false alarms), catch most fraud

**Approach**:
1. **Problem**: Binary classification
2. **Data**: Transaction history, user behavior, device info
3. **Features**: Amount, velocity, location mismatch, device fingerprint
4. **Model**: Tree-based (XGBoost) for interpretability
5. **Serving**: Real-time API, instant response needed
6. **Monitoring**: False positive rate, fraud catch rate

---

### Scenario 3: Search Ranking
**Constraints**: <50ms, relevance + quality signals

**Approach**:
1. **Two-stage**: Retrieval (candidates) → Ranking
2. **Retrieval**: Elasticsearch, BM25, vector search
3. **Ranking**: Learning-to-rank model (LambdaMART, Neural LTR)
4. **Features**: Query-doc relevance, doc quality, freshness
5. **Serving**: Cache top results, lightweight re-ranking
6. **Monitoring**: NDCG, user satisfaction (clicks, dwell time)

---

### Scenario 4: Personalization at Scale
**Constraints**: Real-time, millions of items, cold start

**Approach**:
1. **Features**: User profile, item features, context
2. **Model**: Embeddings-based (collaborative filtering)
3. **Fallback**: Content-based for new users/items
4. **Serving**: Pre-compute popular items, real-time personalization
5. **Monitoring**: Personalization lift (A/B test), engagement

---

## 💡 Pro Tips for Interviews

✅ **Do:**
- Ask clarifying questions upfront
- Start simple, then add complexity
- Discuss trade-offs explicitly
- Show your reasoning process
- Draw diagrams (data flow, architecture)
- Mention monitoring and iteration
- Think about scale and edge cases

❌ **Don't:**
- Jump to implementation without planning
- Over-engineer the first solution
- Ignore constraints
- Forget about monitoring/operations
- Assume perfect data
- Build a single-model system without fallback

---

## 🔗 Cross-Reference Links

- [[ML_System_Design_Guide]] - Full comprehensive guide
- [[interview/4_SystemDesign/0_Template/00_Index]] - Document organization and learning path

---

*Last updated: 2026-04-13*
