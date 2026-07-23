---
source: "https://blog.jiaqizhai.com/2026/two-bets-from-2021-how-to-build-scaling-law/"
author:
published: 2026-07-20
created: 2026-07-21
description: "On ROO and SilverTorch, two papers at SIGIR ’26, and the bets they settle."
tags:
---
Under a scaling law, compute converts to quality at a rate you can budget. Language modeling has had one since 2020. Recommendation had no useful equivalent; for many years, doubling a model’s FLOPs barely moved the metrics. That changed in 2024. Behind it were two bets from 2021, against the consensus of the time; their papers are only arriving now, five years later.

## Bet one. Fix the logging schema and better models will follow.

Machine learning communities celebrate architecture improvements, but system changes could improve models more than years of architecture changes combined. Request-Only Optimization ([ROO, SIGIR ’26](https://arxiv.org/abs/2508.05640)) is one such change.

A typical feed answers a request with up to ten items. Log one row per shown item, and the user’s features get stored and re-encoded up to ten times, at petabyte scale. ROO logs the request instead: the features once, the candidates attached. LLM people have since rediscovered the shape of this problem: candidate responses share one prompt, so the shared part should be encoded once, and every major serving stack has shipped that as prefix caching or prompt caching. ROO is the same economics one layer deeper, in the logging schema, in 2021. (It’s also second normal form, which Codd published in 1972 and the ROO paper cites without irony.)

What’s interesting is what ROO risks. Recommenders train on streaming events; request-level rows change the order examples reach the model, and model quality maximalists would reject ROO for that alone. My bet was that a better point on the Pareto frontier existed: give up strict time-ordering, a bounded correctness cost, to buy examples 7× cheaper, then spend the savings on a richer model. That point was worth changing the unit of record under live billion-user products, a migration that took years.

[GR/HSTU](https://arxiv.org/abs/2402.17152) already trained this way in 2023. And the industry is now converging on the ROO format ([MixFormer](https://arxiv.org/abs/2602.14110); [SORT](https://arxiv.org/abs/2603.03988); [HoMer](https://arxiv.org/abs/2510.11100); [Adaptive Ranking](https://engineering.fb.com/2026/03/31/ml-applications/meta-adaptive-ranking-model-bending-the-inference-scaling-curve-to-serve-llm-scale-models-for-ads/), etc.).

## Bet two. A multi-funnel retrieval system reduces to one trainable layer.

Before a feed ranks anything, retrieval pulls a few hundred candidate items from millions; the standard machinery is an approximate nearest-neighbor (ANN) index, dot products over embeddings. The industry ran that layer in a separate service, so at scale, every retrieval model ended in a dot product; a key semantic choice was frozen into deployed infrastructure. Product decisions piled on top: how to weight social connections, how to weight local events, each another funnel. The bet: all of it, the index, the filters, the funnels, reduces to one trainable layer, so what was frozen behind services can be learned together.

Act one: consolidate the external services into the model. The work by Pawel, Kevin, Rui, Jongsoo, Yanzun, Peng, Shripad, Harry, and colleagues in 2020–2022 first turned the ANN service into a model layer. Separate services could quietly disagree; in 2022 an incorrect version switch dropped production metrics by 30%. With SilverTorch, the external services became part of the model, and model publish time fell from days to an hour; retrieval ran natively on GPUs ([MoL](https://arxiv.org/abs/2306.04039); [LiNR](https://arxiv.org/abs/2407.13218)), and the layer that replaced the dot product is a universal approximator of similarity functions with low-rank inputs ([RAILS](https://arxiv.org/abs/2407.15462)).

Act two: consolidate the funnels into the same model. A funnel is, mechanically, a filter on top of a similarity; with the Bloom index from Bi, Lei, and colleagues, filtering becomes bit operations inside the model, sixty-four items processed per PTX instruction, AND/OR/NOT applied bitwise across per-feature masks. Their co-designed Int8 ANN algorithm keeps that filtering compatible with large funnels and scales retrieval to hundreds of millions of items. Together with other optimizations, the two acts form [SilverTorch (SIGIR ’26)](https://arxiv.org/abs/2511.14881), improving cost-efficiency by 13.35× over CPU baselines and 2.27× over GPU baselines.

## How to build a scaling law.

The ultimate validation of these bets comes from a family of models still years away in 2021: [GR/HSTU](https://arxiv.org/abs/2402.17152) demonstrated the first scaling law in deployed recommendation systems, and is now a standard benchmark ([MLPerf’s DLRMv3](https://mlcommons.org/2026/02/dlrmv3-inference-meta/)).

For ROO, the fewer per-candidate features a model needs, the more of every example is the shared history, and the more the request row saves; a model that discards hand-built features needs almost none. ROO alone trains such a model at 7× less compute per example, before algorithmic and kernel optimizations. For SilverTorch, a frozen last layer capped what compute could buy; making it trainable removed the cap, consolidated hundreds of separate deployments into one system, and powered GR/HSTU’s retrieval.

Scaling laws can be built on purpose; this one was, with deliberate efforts from 2020–2021. The recipe:

- Bet on paradigms before they are consensus. Abstraction decisions are 5-year decisions; make them aligned with a directional thesis.
- Build the future you expect to see, layer by layer. ROO’s rows assume a model that reads raw actions; SilverTorch’s in-model index assumes learned similarities.
- Hunt the redundancy in the system, and optimize it away aggressively; clear the way for efficient scaling.
- Hold through the silence. The payoff arrives in years; but when it arrives, it sets the field’s defaults.

## Open positions, 2031.

An essay that began with bets would not be complete without open positions. We’ve discussed how to build a scaling law, but the recipe does not choose the objective: it amplifies whatever already exists.

Silicon Valley commonly argues that usage itself proves value; experiments have already falsified this for feeds. 64% of TikTok’s active users and 48% of Instagram’s preferred the product not to exist, a collective trap ([Bursztyn et al., 2025](https://www.aeaweb.org/articles?id=10.1257/aer.20231468)). One might advocate replacing the owners. The 2024 divest-or-ban law did: after TikTok’s US operations passed to new owners in 2026, within weeks the company said the algorithm had not changed. The optimization direction remains at the mercy of a handful of individuals, who might optimize time well spent in 2018 and ads revenue when the winds change. The settled bets removed key technical obstacles, yielding training data whose unit extends from request to session, and an architecture efficient enough to afford a year of history. What remains in the way is incentives: every duty that binds a company, to advertisers by contract and to shareholders by law ([Dodge v. Ford, 1919](https://en.wikipedia.org/wiki/Dodge_v._Ford_Motor_Co.)), names someone other than the person shaped by the feed.

The problems carry over to language models as they exist today, but inverted: feeds measure without the right maximand; the companies behind LLMs state a maximand, often the benefit of humanity, with no way to measure it. Measurement at that scope first requires boundaries: whose claims count, and over what? Prices exist only where property does ([Mises, 1920](https://mises.org/library/economic-calculation-socialist-commonwealth)). Hayek added that no planner can substitute for the market: the knowledge needed is dispersed ([AER, 1945](https://www.econlib.org/library/Essays/hykKnw.html)). Two open positions hence follow for language models, the first upstream of the second: which boundaries are worth drawing, and what objective is worth optimizing for.

If you’re going to bet, bet at the deepest layer you can reach, with people whose values you share and who have worked through such silences. If the five-year cycle holds, such positions settle around 2031, so the bets behind them are likely being placed this year. One of them is mine.