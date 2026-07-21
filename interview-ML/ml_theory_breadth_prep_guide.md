# ML Theory & Breadth Interview: Prep Guidance

A concise guide for preparing the ML concepts / theory / breadth round, targeted at Staff+ MLE roles at frontier AI labs (2025-2026).

---

## What the Round Tests

The ML breadth round evaluates general knowledge of ML concepts from both theoretical and practical angles. Unlike depth interviews, breadth rounds follow a fairly consistent structure across companies. In 2026, **LLM/foundation model questions now lead** -- expect at least one transformer-era question before classical ML.

Four areas are tested: **data handling, model selection & optimization, evaluation & metrics, ML in production**.

---

## Topic Checklist

### Classical ML (still tested, ~30-40% of questions)
- Supervised: linear/logistic regression, SVM, decision trees, ensemble methods (RF, XGBoost)
- Unsupervised: k-means, DBSCAN, PCA, t-SNE
- Optimization: SGD variants (momentum, Adam), loss functions (cross-entropy, hinge, ranking)
- Regularization: L1/L2, dropout, early stopping
- Evaluation: precision/recall/F1, ROC-AUC, cross-validation, confusion matrix
- Key concepts: bias-variance tradeoff, overfitting, data leakage, class imbalance, distribution shift

### Deep Learning Foundations (~20%)
- Feedforward nets, activation functions, backprop
- CNNs (convolution, pooling, architectures)
- RNNs, LSTMs, vanishing/exploding gradients
- Attention mechanism, self-attention

### Foundation Models & LLMs (~30-40%, growing)
- **Transformer internals**: scaled dot-product attention, multi-head attention, positional encoding (RoPE, ALiBi), KV cache, FlashAttention, RMSNorm, MoE routing
- **Training pipeline**: pretraining, SFT, RLHF/DPO/GRPO, reasoning RL
- **Inference optimization**: quantization (INT8/4, FP8), speculative decoding, continuous batching, tensor/pipeline parallelism
- **Decoding**: temperature, top-k/top-p, structured decoding, chain-of-thought
- **Evaluation**: LLM-as-judge, arena evals, MMLU/GPQA, safety/jailbreak testing
- **RAG vs fine-tuning vs long context** tradeoffs

### Multimodal & Genertic AI (~10%)
- CLIP/SigLIP, vision-language models (LLaVA architecture)
- Diffusion models, latent diffusion, flow matching
- Autoregressive vs diffusion generation paradigms

### Statistics & Probability (woven throughout)
- Bayes theorem, MLE/MAP
- Hypothesis testing, p-values
- Similarity metrics (cosine, Euclidean, Mahalanobis)

---

## Prep Methodology

### 1. Spaced Retrieval (primary method)
- Study a topic block (e.g., "ensemble methods") for 30-60 min
- Same day: close notes, explain concepts aloud or write from memory
- Day 2, Day 7, Day 14: quiz yourself again without notes
- Use the `/interview-ML` quiz mode to generate rapid-fire questions

### 2. Concept Mapping
- For each topic, be able to answer: **what it is, when to use it, when NOT to use it, tradeoffs, and a real example**
- Connect concepts: "Why might you prefer XGBoost over a neural net?" "When does RAG beat fine-tuning?"

### 3. Breadth Sprints (for coverage)
- Pick 5-8 topics per session, spend 10-15 min each
- Goal: comfortable giving a 2-minute verbal explanation of each
- Track coverage with a checklist -- mark topics as green/yellow/red

### 4. Mock Rapid-Fire
- Simulate the interview format: 20-30 questions in 45 min
- Mix classical ML, DL, and LLM questions
- Practice concise answers (30-90 seconds each)
- Use `/interview-ML` mock mode or study with a partner

### 5. Weak-Spot Drilling
- After each mock, note topics where you hesitated or gave incomplete answers
- Spend dedicated sessions on weak spots before the next mock

---

## Recommended Resources

### Primary (start here)
1. [Chip Huyen -- Introduction to ML Interviews Book](https://huyenchip.com/ml-interviews-book/) -- free, covers math + CS + ML workflows + algorithms. The canonical breadth prep book.
2. [alirezadir/Machine-Learning-Interviews (GitHub)](https://github.com/alirezadir/Machine-Learning-Interviews) -- comprehensive topic map with 2026 updates covering LLMs, multimodal, and GenAI system design. Author received offers from Meta, Google, Amazon, Apple.
3. [zafstojano/ml-interview-questions-and-answers (GitHub)](https://github.com/zafstojano/ml-interview-questions-and-answers) -- worked solutions to Chip Huyen's book questions.

### LLM-Era Breadth
4. Chip Huyen -- *AI Engineering* (O'Reilly, 2024) -- production LLM systems, RAG, evaluation, agents
5. [The Modern ML Interview (Grokking ML)](https://grokkingml.com/ml-interview-formats.html) -- updated interview format guide

### Video & Courses
6. Andrew Ng's ML Specialization (Coursera) -- classical foundations
7. StatQuest (YouTube) -- visual explanations of algorithms and statistics
8. Coursera Deep Learning Specialization -- DL fundamentals

### Quick Reference
9. [Exponent ML Interview Guide](https://www.tryexponent.com/blog/machine-learning-interview-guide) -- format overview, sample questions
10. [Coursera ML Interview Prep Guide (2026)](https://www.coursera.org/resources/machine-learning-interview-prep-guide) -- structured study plan

---

## Suggested Study Plan (1-week sprint)

Assumes Staff MLE background: classical ML and DL are refresh, not learn-from-scratch. LLM-era topics get the most time since they dominate 2026 breadth rounds at frontier labs.

**Daily commitment: 3 hours** (2 hr study + 1 hr quiz/mock). Use `/interview-ML` quiz mode throughout.

| Day | Morning block (2 hr study) | Evening block (1 hr quiz) |
|-----|---------------------------|--------------------------|
| D1 | **Classical ML speed refresh**: bias-variance, regularization (L1/L2/elastic net), ensemble methods (RF vs XGBoost -- when each wins), loss functions, evaluation (precision/recall/F1/AUC), class imbalance, distribution shift | Self-quiz: explain 10 concepts aloud in 60s each, no notes. Log weak spots |
| D2 | **Optimization + DL foundations**: SGD variants (momentum, Adam, AdamW), learning rate schedules, batch norm vs layer norm vs RMSNorm, activation functions, vanishing gradients | `/interview-ML` quiz on classical ML + DL |
| D3 | **Transformer internals**: scaled dot-product attention math, multi-head attention, positional encoding (RoPE, ALiBi), KV cache mechanics, MQA/GQA/MLA, FlashAttention, MoE routing, tokenization (BPE) | Draw the transformer block from memory. `/interview-ML` quiz on transformers |
| D4 | **LLM training pipeline + alignment**: pretraining objectives, scaling laws (Chinchilla), SFT, RLHF (reward model + PPO), DPO (why it skips reward model), GRPO, KTO, reasoning RL. When to use which | Compare alignment methods in a table from memory |
| D5 | **Inference optimization + RAG**: quantization (INT8/4, FP8, GPTQ, AWQ), speculative decoding, continuous batching, paged attention, parallelism (tensor/pipeline/sequence). RAG architecture, chunking, RAG vs fine-tuning vs long context | Explain RAG end-to-end, then critique failure modes. `/interview-ML` quiz |
| D6 | **Multimodal, safety, evaluation**: CLIP/SigLIP, vision-language models (LLaVA), diffusion basics. LLM-as-judge, arena evals, benchmarks. Safety: red-teaming, jailbreaks, constitutional AI, fairness | `/interview-ML` mixed-topic mock: 25 questions, 45 min |
| D7 | **Weak-spot blitz** (morning): drill the 5-8 weakest topics from D1-D6 logs | **Final mock**: 25-30 questions, 45 min, all areas. Aim for zero hesitations. Rest before interview |

### Daily Routine Template

```
Morning (2 hr block):
  - 10 min: recall yesterday's topics from memory (no notes)
  - 110 min: study today's block (notes, alirezadir repo, resources)

Evening (1 hr block):
  - 45 min: quiz / mock (use /interview-ML or self-quiz)
  - 15 min: log weak spots in a running list
```

### If You Miss a Day

Non-negotiable core (do these 4 days minimum):
1. **D3** -- transformer internals (the new baseline)
2. **D4** -- training pipeline + alignment
3. **D5** -- inference optimization + RAG
4. **D7** -- final mock

---

## Staff-Level Differentiators

At Staff+, breadth answers should signal depth beyond textbook definitions:
- **Connect to production**: "In practice, we found L2 regularization insufficient for feature-sparse models, so we used elastic net with..."
- **Discuss tradeoffs quantitatively**: "RAG adds ~200ms latency per retrieval hop but reduces hallucination by ~30% on our benchmarks"
- **Reference real systems**: cite how major companies solve specific problems
- **Show taste**: know when a simple baseline beats a complex model, and say so
- **Safety & ethics awareness**: alignment methods, evaluation of harmful outputs, fairness metrics -- frontier labs fold this into technical rounds
