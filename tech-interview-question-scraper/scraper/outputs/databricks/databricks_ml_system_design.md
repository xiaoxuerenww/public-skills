# Databricks ML System Design Raw Comments By Question

Source corpus: local scrape under `outputs/raw_posts/`, cross-checked against `outputs/databricks/databricks_reorganized_by_category.md`.

Rule: raw post/reply content is preserved. No rewriting or summarization inside quoted blocks.

## RAG For Table / Notebook Retrieval In Coding Agent

### Source: `1175089`

Original post: https://www.1point3acres.com/bbs/thread-1175089-1-1.html

```text
一个senior staff的大哥和我聊RAG的设计。这哥们做内部的coding agent，然后有个问题就是人要是问数据相关的问题，这个agent应该如何拿到最合适的table/notebook从而回答这个问题。基本上就是retrieval + reranker，大部分细节都是如何index，把什么东西index进去，如何处理noisy甚至不一定helpful的notebook/table等assets，然后metric怎么设计等等。
```

```text
**#2 楼主**

匿名用户 发表于 2026-4-30 11:13
请问lz是target staff吗？面试之前的prep material也是说好的面design么？
对 面试就告诉是MLE system design
```

## Harmful Content Detection

### Source: `1173457`

Original post: https://www.1point3acres.com/bbs/thread-1173457-1-1.html

```text
ML Design：设计harmful content detection，大哥经验很丰富，能问的不能问的都问了。。。
```

### Source: `1172872`

Original post: https://www.1point3acres.com/bbs/thread-1172872-1-1.html

```text
ML design。怎么detect llm harmful content
```

```text
**#3 匿名用户-JEQUF** | `2026-4-14 21:32:46`

感谢分享。但是请问 ML design 到底面的是哪道题：detect llm harmful content 还是 predict OOM issue for notebook(类似colab)？
```

### Source: `1110121`

Original post: https://www.1point3acres.com/bbs/thread-1110121-1-1.html

```text
ML Design轮：Harmful Content Detection，Alex Xu那本ML System Design的书里有
```

## Predict OOM Issue For Notebook

### Source: `1172872`

Original post: https://www.1point3acres.com/bbs/thread-1172872-1-1.html

```text
ML。很奇葩跟recruiter的description完全对不上。最后考的是1. 手撸simple linear regression gradient descent。 2. 介绍一个project。3. ml design。predict OOM issue for notebook(类似colab)
```

```text
**#3 匿名用户-JEQUF** | `2026-4-14 21:32:46`

感谢分享。但是请问 ML design 到底面的是哪道题：detect llm harmful content 还是 predict OOM issue for notebook(类似colab)？
```

## Auto ML Service / Best Model Selection

### Source: `1095753`

Original post: https://www.1point3acres.com/bbs/thread-1095753-1-1.html

```text
Architecture：
要写一个API interface和database schema。尽量还原问题了但是很长，问题如下：
Given a black box service "auto ML service," it automatically trains a set of ML models and returns models information.
Write an interface where the frontend takes in a form of with fields:
dataset name
training purpose (regression, accuracy, 还有一个忘了反正三个选择）
measurement (也是三个用来测量purpose到底好不好的measurement忘了具体选择了，具体是啥反正不重要）
timeout
Outline the backend api request endpoints so that it returns the user the best model that should be used for the inputed scenario.
followup 1:
What should the interface be if the user needs to see real-time updates on all the model's training data  in a table (i.e. if the training for a model has started, started when, what's the duration, what's the current score etc.)
followup 2:
The models will timeout if it has not completed training within the timeout specified by the input. How should this timeout be implemented.
followup 3:
Any optimizations
```

```text
**#9 2024-11-28 23:01:04**

已➕米
谢谢楼主分享，但是architecture部分没看懂题意
请问是指已经给了一个黑盒训练系统的情况下额外设计一个app server和数据库来响应用户前端的请求吗
```

```text
**#10 2025-1-23 16:14:01**

同问这个architecture 的题。 没太看懂，楼主能再仔细说下吗
```

## Distributed Job Scheduler For Model Training

### Source: `1106844`

Original post: https://www.1point3acres.com/bbs/thread-1106844-1-1.html

```text
又有朋友面了这家公司，顺手代发一下其中两道系统设计题
1. 分布式Job scheduler，主要面向model training，重点讨论error handling
2. 买书服务，从一堆book seller里找出最便宜的书籍购买，客户指定最高出价，如果找不到就放弃。这个题感觉API和DB设计更重要些
```

```text
**#2 匿名用户-5JURB** | `2025-1-23 00:46:34`

请问model training指的是什么呀？面的是MLE么？
```

## GPU Compute Platform

### Source: `1122442`

Original post: https://www.1point3acres.com/bbs/thread-1122442-1-1.html

```text
VO SD: 设计一个 compute platform，假设我们管理着X个GPU，用户可以提交不同优先级的job到我们平台来运行。感觉这轮面试官希望我说一些Kubernetes的东西，但是我完全没经验也不好瞎说。所以这就说了一些job queue， docker repository， fault tolerance之类的。
```
