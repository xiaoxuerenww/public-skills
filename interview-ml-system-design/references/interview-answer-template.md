---
title: ML System Design - Interview Answer Template
created: 2026-05-25
tags: [ml-systems, interview-prep, template]
---

# Interview Answer Template

Structured approach for answering ML system design interview questions.

---

## 📋 Question Analysis Framework

When you receive a question, immediately analyze it using this framework:

### 1. **What type is this?**
   - Recommendation? Classification? Ranking? Prediction? Clustering?
   - Understanding the problem category helps you apply the right framework.

### 2. **What constraints matter most?**
   - **Latency**: Real-time (<100ms) vs batch (hours)?
   - **Accuracy**: Model precision vs recall vs overall AUC?
   - **Scale**: QPS, DAU, data volume?
   - **Cost**: Budget-constrained? Infrastructure-limited?

### 3. **What's the hardest part?**
   - Is it data availability? Model complexity? Serving infrastructure? Monitoring?
   - Identifying the bottleneck helps you allocate time during the interview.

### 4. **What am I being tested on?**
   - **Scoping skills**: Can you understand requirements?
   - **Trade-off analysis**: Do you think about pros/cons?
   - **Technical depth**: Can you dive into details?
   - **Communication**: Can you explain clearly?

---

## 🎯 Structured Answer Template (30 Minutes Total)

Use this framework for every question. Allocate your time strategically:

### **Opening (1 minute): Clarify the Problem**

**What to do**:
- Ask clarifying questions to understand scope and constraints
- Show you're thinking about the problem systematically
- Buy time to organize your thoughts

**Example questions**:
- "Can I clarify the problem statement?"
- "What's the scale we're designing for? (QPS, DAU, number of items/users)"
- "What are the latency requirements?"
- "What are the success metrics?"
- "What are the main constraints? (cost, infrastructure, data availability)"

**What NOT to do**:
- ❌ Don't ask obvious questions (show you read the problem)
- ❌ Don't ask too many questions (3-4 is enough)
- ❌ Don't assume answers—ask instead

---

### **Approach (2 minutes): High-Level Outline**

**What to do**:
- State the phases you'll cover
- Show you have a mental model
- Set expectations for the deep dive

**Example phrasing**:
> "I'll structure my answer around these phases:
> 1. **Scoping**: Define the problem clearly
> 2. **Data & Features**: Design the data pipeline and features
> 3. **Model**: Choose architecture and training strategy
> 4. **Serving**: Build the inference infrastructure
> 5. **Monitoring**: Ensure quality and iterate
> 
> I'll spend most time on the phases most relevant to your question."

**Why this works**:
- Shows you understand the end-to-end system
- Helps the interviewer follow your thinking
- Demonstrates you've thought about dependencies

---

### **Deep Dive (15-20 minutes): Go Phase-by-Phase**

For each phase, use this structure:

#### **Phase Template**:

**State your approach**:
> "For [Phase], here's my approach..."

**Provide specifics**:
> "The [key component] would be [architecture/design], which handles [constraint]."

**Discuss trade-offs**:
> "The trade-off here is [option A: pros/cons] vs [option B: pros/cons]. I'd choose [option] because..."

**Add diagrams** (draw on the board):
- Data flow diagrams
- Architecture diagrams
- Feature store layout
- Serving pipeline

#### **Example Deep Dive for Recommendation System**:

**Phase 1: Scoping**
- "Input: User ID and context. Output: Top-K recommendations. Scale: 100M users, 10M items, <500ms latency."
- Metrics: Watch time, completion rate, retention
- Constraints: Freshness, diversity, computational cost

**Phase 2: Data & Features**
- "User features come from watch history (embeddings, genres, ratings). Item features come from metadata and popularity."
- "I'd use a feature store (online + offline) for consistency and low-latency retrieval."
- Trade-off: Dense vs sparse embeddings; dimensionality affects latency and accuracy.

**Phase 3: Model**
- "Two-stage design: Candidate generation (~100 items) then ranking (rerank to ~10)."
- "Stage 1 uses embeddings + ANN search. Stage 2 uses gradient boosting or neural network on rich features."
- Trade-off: More complex models improve accuracy but increase latency.

**Phase 4: Serving**
- "Serving pipeline: User request → Load balancer → API server → Feature retrieval → Scoring → Diversification → Return top-10."
- "Caching strategy: User embeddings cached daily, item embeddings updated on metadata changes, ANN index updated hourly."
- Trade-off: More caching reduces latency but requires cache invalidation logic.

**Phase 5: Monitoring**
- "Key metrics: Engagement (watch time, completion rate), personalization (% watched from recommendations), freshness, diversity."
- "Drift detection: User embedding drift, item feature drift, concept drift."
- "Retraining: Embedding models weekly, ranking models every 2 days."

---

### **Wrap-up (2 minutes): Summarize**

**What to do**:
- Recap key architectural decisions
- Reiterate the main trade-off
- Connect back to the requirements

**Example phrasing**:
> "In summary, the system has:
> - **Two-stage ranking** for balancing speed and accuracy
> - **Feature store** (online + offline) for consistency
> - **Caching at multiple levels** to meet the <500ms latency requirement
> - **Real-time monitoring** to detect and respond to drift
> 
> The key trade-off is between model complexity (accuracy) and latency. We mitigate this by using a two-stage system."

**Be prepared to**:
- Answer follow-up questions
- Go deeper on any phase
- Discuss alternatives or variations

---

## 🎯 Answer Structure Checklist

Use this checklist to stay on track:

### Opening
- [ ] Ask 2-3 clarifying questions
- [ ] Confirm understanding of constraints
- [ ] Understand success metrics

### Approach
- [ ] State the 5 phases clearly
- [ ] Mention which phases are most relevant
- [ ] Set time expectations

### Deep Dive
- [ ] Phase 1: Clear scoping with numbers
- [ ] Phase 2: Feature engineering strategy
- [ ] Phase 3: Model architecture with rationale
- [ ] Phase 4: Serving pipeline and caching
- [ ] Phase 5: Monitoring and iteration

### Wrap-up
- [ ] Summarize key decisions
- [ ] Reiterate main trade-offs
- [ ] Ask for feedback or follow-ups

---

## 💡 Pro Tips for Staying on Track

### Time Management
- **Hard limit on Opening**: 1 minute. Don't over-ask.
- **Hard limit on Deep Dive**: Save 2 minutes for wrap-up.
- **If running over**: Prioritize the phases most relevant to the question.
  - Recommendation → Spend time on ranking & serving
  - Fraud detection → Spend time on features & model
  - Latency-critical → Spend time on serving & caching

### Showing Your Thinking
- ✅ "Let me think out loud about this..."
- ✅ "The trade-off is..."
- ✅ "Here's why I chose this approach..."
- ✅ "An alternative would be..."

### When You Don't Know
- ✅ "I haven't built that exact component, but based on [principle], I'd approach it like..."
- ✅ "That's a great point. I'd need to research that, but here's my initial thinking..."
- ❌ Don't fake expertise or make things up

---

## Special Question Types

### Type 1: "How Would You Debug This?"

**Example**: "The CTR model accuracy dropped 5% after a deploy. The model version didn't change. How would you investigate?"

**Approach**:
1. Isolate the change: What changed in the deploy?
2. Investigate by layer: Data pipeline? Features? Serving code?
3. Common causes: Stale features, online/offline mismatch, traffic distribution change
4. Resolution: Rollback or fix root cause; add monitoring

---

### Type 2: "Improve This Existing System"

**Example**: "CTR is decent but engagement metrics are plateauing. How would you improve it?"

**Approach**:
1. Measure current state: What are we optimizing? Baseline performance?
2. Diagnose bottleneck: Model quality? Coverage? Diversity? Freshness?
3. Propose improvements: By category (model, data, serving, monitoring)
4. Prioritize by impact: What has highest impact? Fastest to implement?

---

### Type 3: "Design for Constraint X"

**Example**: "Design a recommendation system for mobile with <10MB model size."

**Approach**:
1. Acknowledge the constraint: "This is a mobile-first system..."
2. Design for constraint: Lightweight architectures, quantization, distillation
3. Discuss trade-offs: Smaller = lower accuracy; mitigation?
4. Hybrid approach: On-device + server-side for refinement

---

## 🔗 Related Resources

- [[Quick_Concepts_Cheatsheet]] — Quick lookup for models, metrics, architecture patterns
- [[Technical_Cheatsheet]] — Deep dives into TF-IDF, BM25, feature stores
- [[Practice_Questions_by_Difficulty]] — Full practice questions with solutions
- [[Interview_Communication_Guide]] — Communication tips and interviewer expectations
- [[MLSD_5Phase_Framework]] — Detailed framework for each phase

---

*Last updated: 2026-05-25*
