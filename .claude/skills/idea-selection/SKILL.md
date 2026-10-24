---
name: idea-selection
argument-hint: "[list of candidate ideas and your background]"
description: Score and choose between startup ideas using pain, reach, buildability, revenue path, and founder fit, with kill criteria. Use at the very start, before problem framing.
intent: >-
  Compare candidate ideas with an explicit scorecard so a solo founder commits to one on evidence and constraints, not excitement. Produces a ranked table, the chosen idea, its biggest risks, and kill criteria.
type: workflow
best_for:
  - "Choosing one idea from several"
  - "Stress-testing a favorite idea before investing months"
  - "Writing down what would make you stop"
scenarios:
  - "I have five SaaS ideas; which one should I build?"
  - "Is this idea worth pursuing as a solo founder?"
theme: strategy
estimated_time: "30-45 min"
---

## Purpose
Replace gut feel with a short, honest scorecard. Pick one idea, name the riskiest assumption, and set conditions that end it.

## Input
**Works best with:** 3-8 candidate ideas (one line each), your skills, time per week, runway in months, target monthly income.
**Also useful:** industries you know, audiences you can already reach.

## Key Concepts
Score each idea 1-5 on weighted criteria (weights are defaults; change them and say why).
| Criterion | Weight | Question |
|---|---|---|
| Pain | 25% | Do people already pay money, time, or lost deals today? |
| Reachability | 20% | Can I contact 50 buyers in 2 weeks without ads? |
| Revenue path | 20% | Does target income need a believable number of customers at a believable price? |
| Buildability | 15% | Can I ship a useful version in 4-6 weeks alone? |
| Founder fit | 10% | Do I know the domain or can I learn it fast? |
| Moat / defensibility | 10% | What keeps a clone or incumbent from taking it? |

- **Revenue check:** target MRR / price = customers needed. If that exceeds 1-2% of reachable buyers, flag it.
- **Evidence grade:** mark each score `evidence` (sourced), `estimate`, or `guess`. Guess-heavy winners need cheap validation first.
- **Substitute check:** the real competitor is often "do nothing" or a spreadsheet.

## Application
1. List candidates; drop any that fail a hard filter (illegal, needs a licence you lack, needs a large team).
2. Score each criterion with a one-line reason and an evidence grade.
3. Compute weighted totals and rank.
4. Run the revenue check on the top three.
5. Pick the winner; name its **riskiest assumption** and the cheapest test (hand off to `community-discovery`, `demand-test`).
6. Write **kill criteria**: specific results by specific dates that end the idea.
7. Record what would make the runner-up better.

### Output template
```markdown
## Scorecard
| Idea | Pain | Reach | Revenue | Build | Fit | Moat | Total | Evidence |
## Revenue check (top 3)
## Decision
## Riskiest assumption and cheapest test
## Kill criteria (metric, threshold, date)
```

## Examples
See `examples/trustreply.md`.

## Common Pitfalls
- Scoring pain from your own annoyance instead of other people's spend.
- Ignoring reachability; a great idea you cannot reach stalls.
- Equal weights by default; state and justify them.
- Skipping kill criteria, so no idea ever ends.

## References
- Next: `community-discovery`, `problem-statement`, `demand-test`. Related: `product-strategy-session`, `tam-sam-som-calculator`
