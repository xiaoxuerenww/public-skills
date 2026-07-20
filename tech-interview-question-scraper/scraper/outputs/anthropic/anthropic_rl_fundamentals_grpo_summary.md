# Anthropic RL Fundamentals (GRPO) Interview Summary

This note summarizes the locally available scraper evidence about the Anthropic
RL Fundamentals interview round, especially the GRPO debugging variant.

## Bottom Line

The RL Fundamentals round appears to be a Research Engineer / research-track
technical interview centered on debugging simple GRPO training code, followed by
RL basics discussion.

The strongest signal is that candidates should understand the GRPO training
flow, numerical stability, current-vs-old policy log probabilities, ratio
clipping, and why the policy ratio may not always be exactly 1.

## Confirmed From Local Scrape

- `outputs/raw_posts/1167043.md`: says the round requires familiarity with the
  GRPO training process.
- `outputs/raw_posts/1167043.md`: describes the task as a simple GRPO training
  debug exercise with three direct bugs.
- `outputs/raw_posts/1167043.md`: says follow-ups cover basic RL topics, with
  the hardest point being why the run is not strictly on-policy, specifically
  why the ratio is not always 1.
- `outputs/raw_posts/1148586.md`: gives concrete bug and follow-up details:
  missing softmax before multinomial sampling, missing epsilon in normalized
  advantage standard deviation, and questions about ratio calculation, clipping,
  when clipping happens, and what clipping affects.
- `outputs/raw_posts/1167043.md` and `outputs/raw_posts/1148586.md`: both point
  to Research Engineer context.

## Likely Interview Shape

1. Candidate receives buggy GRPO / PyTorch-style code.
2. Candidate runs or inspects the code and identifies bugs.
3. Candidate fixes numerical or training-loop issues.
4. Interviewer asks RL fundamentals follow-ups.
5. Discussion goes deeper on policy ratio behavior, clipping, and on-policy
   semantics.

## Concrete Topics To Prepare

- GRPO rollout, reward computation, group-normalized advantage, and policy
  update flow.
- Difference between current policy log probabilities and cached old rollout
  log probabilities.
- Correct ratio form: `exp(model_logprob - old_logprob)`.
- Why raw `model_logprob - old_logprob` is not the probability ratio.
- Why PPO/GRPO clips the ratio.
- When clipping activates.
- What clipping does to gradients and policy updates.
- Why the ratio may be exactly 1 only under specific timing assumptions.
- Difference between rollout policy, current policy, and reference policy.
- KL penalty and reference model role.
- Advantage normalization and numerical stability.
- Sampling from logits requires probabilities, usually after softmax.
- Add epsilon to standard deviation during normalization to avoid NaNs.

## Likely Bugs

Explicitly reported:

- Multinomial sampling uses logits directly instead of softmax probabilities.
- Normalized advantage divides by standard deviation without epsilon, causing
  NaN risk.

Strongly implied:

- Ratio / old-logprob handling is wrong or confusing enough to require
  debugging why the ratio is not always 1.

## Interview Framing

Use this framing:

> This is a GRPO debugging interview: show that the resolved training loop
> preserves the right policy identities, numerical stability, and ratio-clipping
> semantics.

Good answer structure:

1. State the expected GRPO loop.
2. Identify the code invariant that is violated.
3. Fix the bug minimally.
4. Explain why the fix matters mathematically.
5. Add a small check or print that proves the behavior is now sane.

## What Is Not Confirmed

- Exact starter code.
- Exact API signatures.
- Exact full set of three bugs.
- Whether every candidate gets the same version.
- Whether the interview is always in CodeSignal, Colab, or screen-share Python.

Several local posts are requests for RL Fundamentals information rather than
actual content, including `outputs/raw_posts/1157092.md`,
`outputs/raw_posts/1157153.md`, and `outputs/raw_posts/1159633.md`.

## Source Pointers

- `outputs/raw_posts/1167043.md`
- `outputs/raw_posts/1148586.md`
- `outputs/raw_posts/1157092.md`
- `outputs/raw_posts/1157153.md`
- `outputs/raw_posts/1159633.md`
