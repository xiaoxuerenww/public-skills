# Databricks Cross-Functional Behavior And Leadership Raw Comments By Question

Source corpus: local scrape under `outputs/raw_posts/`.

Rule: raw post/reply content is preserved. No rewriting or summarization inside quoted blocks.

## Round Format

### Source: `1076701`

Original post: https://www.1point3acres.com/bbs/thread-1076701-1-1.html

```text
申请的senior，只给面L4，说是不给Up Level。
1. Cross functional：Standard BQ，project deep dive，conflict，comments from Mgr
2. Algorithm：经典 IP CIDR
3. System design coding：event writer
和地里的log/data writer是一样的。Multi-thread，每个thread需要push data to file。怎么样可以Low latency，high throughput，recover from server crash。
其实重点就是，每一个push call必须保证data have been persisted before returning success。那么选择就十分有限了。
4. Coding：Tic tac toe，MxN的棋盘
```

### Source: `1149122`

Original post: https://www.1point3acres.com/bbs/thread-1149122-1-1.html

```text
Algorithm: Hashmap QPS. 不要求thread safe，很多followup，比如高效查询不止最近5分钟的hit count，要最近24小时之类的，讨论使用不同数据结构实现的tradeoffs
Coding: Lazy Array. 很多followup，比如如何用caching减少运算，要自己写test case验证laziness
System Design: Chat System. 这轮要注意紧扣面试官的要求，重点大概率是在如何handle message deletion，不要over engineer用websocket之类的。这轮答得不好。
System Programming: Durable event writer. 讨论高并发下的性能tradeoffs
Cross Functional: Project deep dive + regular BQ
加面System Design: 分布式文件系统，文件immutable，要支持recursive deletion。这轮问得非常细，我准备的时候把gfs，bigtable，hdfs等经典文章吃透，结合gpt深挖各种潜在的followup，还是有帮助的。
Reference check给了3个。整个流程从约面试到面试官写feedback到HC做决定给offer很有效率。总体感觉面试的bar很高，如果有一轮答得不好的话，别的几轮得比较strong才可能有机会加面。
```

### Source: `1151590`

Original post: https://www.1point3acres.com/bbs/thread-1151590-1-1.html

```text
cross-function：常规问题，conflict，ambiguous situation，ownership，feedback等，30分钟草草结束
```

### Source: `1088545`

Original post: https://www.1point3acres.com/bbs/thread-1088545-1-1.html

```text
Behavioral interview:
resume and project deep dive, some standard questions
```

### Source: `1149185`

Original post: https://www.1point3acres.com/bbs/thread-1149185-1-1.html

```text
cross: 常规bq
```

## Project Deep Dive And Past Experience

### Source: `1074759`

Original post: https://www.1point3acres.com/bbs/thread-1074759-1-1.html

```text
- BQ
HM聊，但是对背景问得特别细，细到比如在前司和现在的升职时间线，之后就是问之前做项目的具体细节，算是比较经典的bq，项目timeline，人员，idea initiative之类的，有什么conflict。
另外想表扬一下Databricks的recruiter，虽然挂了但是给电话通知的，还分享了一些feedback还挺有用的。不过面试完确实发现自己技术上还有很大的进步空间，继续加油吧。
```

### Source: `1072913`

Original post: https://www.1point3acres.com/bbs/thread-1072913-1-1.html

```text
BQ:
和hm project dive deep。项目的mileston,时间线，问的特别细致。
面试体验还是挺好的。整体感觉就是coding的bar很高，估计是因为大家都知道题目所以特别卷？follow up也要做出来。还有就是不要给面试官挑刺的机会，要把话语权掌握在自己手中。。。
```

### Source: `1096748`

Original post: https://www.1point3acres.com/bbs/thread-1096748-1-1.html

```text
1. cross functional面试：和一位EM聊聊经验，比较technical，会问一些详细的关于以前project的问题
```

### Source: `1154835`

Original post: https://www.1point3acres.com/bbs/thread-1154835-1-1.html

```text
cf: bq面，除了一些常规bq题，面试官主要问了我实习，问的非常细，包括我实习时候组的架构都问了。感觉对我做的东西不是很感兴趣，搞不好这面挂了呢
```

### Source: `1155225`

Original post: https://www.1point3acres.com/bbs/thread-1155225-1-1.html

```text
一开始先是跟 recruiter 电话面试，之后就是 hiring manager 1 小时的 Zoom，问的都是简历上的经验，有没有 pre-sale 方面的实操，还有一些 behavioral 的问题。
```

## Conflict, Disagreement, And Ambiguity

### Source: `1124438`

Original post: https://www.1point3acres.com/bbs/thread-1124438-1-1.html

```text
第三轮：cross functional，一直在问conflict，如何处理planing 中的risk 和ambiguous things
```

### Source: `1156044`

Original post: https://www.1point3acres.com/bbs/thread-1156044-1-1.html

```text
Behavioral
问题都比较常规
以下内容需要积分高于 188 您已经可以浏览
自我介绍，motivation，重点讲一下实习，为什么选择这两段实习
how to handle disagreements
most challenging project
ambiguous task and how you dealt with it
valuable feedbacks you've received
```

### Source: `1067183`

Original post: https://www.1point3acres.com/bbs/thread-1067183-1-1.html

```text
**#9 匿名用户-2AUPC** | `2024-10-3 21:04:04`

冷眸映青瞳 发表于 2024-9-29 14:36
求问一下常规BQ指的是哪些题呀，即将面对第一个bq面。。楼主好人感谢楼主
已经不记得了
比如说resolve conflict之类得比较常规的
可以看看亚麻的leadership principle 翻翻地里的帖子有很多
```

### Source: `1110121`

Original post: https://www.1point3acres.com/bbs/thread-1110121-1-1.html

```text
BQ：
use customer feedback to improve product
use data to make decision
disagree with others
most challenging project
总之尽力了，可能BQ给的example太naive，scope不够大。毕竟本来就没打算面Senior Staff。。。
```

## Feedback

### Source: `1171295`

Original post: https://www.1point3acres.com/bbs/thread-1171295-1-1.html

```text
Behavioral Questions (BQ)
常规 BQ，印象比较深的是关于项目和 Critical Feedback 的问题。
面试结果
面完两天后通知交 reference。交了四个 reference，两周后通知挂了，不提供feedback。应该是 Hiring Committee 那边决定的。
总结就是交 reference 要小心。
求米求米。
```

### Source: `1156044`

Original post: https://www.1point3acres.com/bbs/thread-1156044-1-1.html

```text
Behavioral
问题都比较常规
以下内容需要积分高于 188 您已经可以浏览
自我介绍，motivation，重点讲一下实习，为什么选择这两段实习
how to handle disagreements
most challenging project
ambiguous task and how you dealt with it
valuable feedbacks you've received
```

## Customer Feedback, Data Decisions, And Product Judgment

### Source: `1110121`

Original post: https://www.1point3acres.com/bbs/thread-1110121-1-1.html

```text
BQ：
use customer feedback to improve product
use data to make decision
disagree with others
most challenging project
总之尽力了，可能BQ给的example太naive，scope不够大。毕竟本来就没打算面Senior Staff。。。
```

## Technical Design Conflict

### Source: `1173457`

Original post: https://www.1point3acres.com/bbs/thread-1173457-1-1.html

```text
Behavior：正常问题，问了technical design conflict
求点米呀～
```

## Most Challenging Or Most Proud Project

### Source: `1110121`

Original post: https://www.1point3acres.com/bbs/thread-1110121-1-1.html

```text
BQ：
use customer feedback to improve product
use data to make decision
disagree with others
most challenging project
总之尽力了，可能BQ给的example太naive，scope不够大。毕竟本来就没打算面Senior Staff。。。
```

### Source: `1156044`

Original post: https://www.1point3acres.com/bbs/thread-1156044-1-1.html

```text
Behavioral
问题都比较常规
以下内容需要积分高于 188 您已经可以浏览
自我介绍，motivation，重点讲一下实习，为什么选择这两段实习
how to handle disagreements
most challenging project
ambiguous task and how you dealt with it
valuable feedbacks you've received
```

### Source: `1095753`

Original post: https://www.1point3acres.com/bbs/thread-1095753-1-1.html

```text
HR：
非常经典的BQ问题们，聊聊之前的project，有什么technical difficulty，怎么solve conflict 之类的
```

## Hiring Manager Fit, Leveling, And Team Match

### Source: `1122442`

Original post: https://www.1point3acres.com/bbs/thread-1122442-1-1.html

```text
年初LinkedIn收到hm私信，这个组是之前数据砖收购的某ml platform公司人马。
hm 初筛 - 问了过去项目经历。hm提到这个org面试有两种选择，ml track 和 traditional backend track，面试内容不一样，hm表示选哪个track 都行，主要是希望找good engineer。我面的是traditional backend
```

### Source: `1122442`

Original post: https://www.1point3acres.com/bbs/thread-1122442-1-1.html

```text
VO hm - 这轮体验超级差，还是之前那个hm，全程没耐心，很condescending的态度。因为我背景和这个组不算特别match，这个初筛的时候我就和hm说了，他表示完全可以来了再学。但是这轮面试时候态度大转弯，全程非常不耐烦。
面完快两周也没消息，肯定是挂了，也懒得问了
```
