---
name: pricing-research
argument-hint: "[product, target buyer, price range under consideration]"
description: Find a defensible starting price for a new product with no revenue history, using value anchors, price-sensitivity questions, and pre-sell tests. Use before launch pricing.
intent: >-
  Derive an initial price and tier structure from buyer value, alternatives, and willingness-to-pay evidence rather than guesses. Produces a price hypothesis, a research plan, and a testing ladder.
type: workflow
best_for:
  - "Setting a first price with no ARPU or churn data"
  - "Choosing tier structure and limits"
  - "Planning price tests that do not mislead you"
scenarios:
  - "What should I charge for a $149 vs $349 plan?"
  - "Plan a willingness-to-pay study with 10 interviews"
theme: strategy
estimated_time: "30-45 min"
---

## Purpose
Set a first price that is anchored in buyer value and alternatives, then test it with real commitment. Use `finance-based-pricing-advisor` later, once you have ARPU, conversion, and churn data.

## Input
**Works best with:** persona, jobs-to-be-done, competitor price pages, cost of the current workaround (time x hourly cost, lost deal value).

## Key Concepts
- **Value anchor:** what the problem costs the buyer today (hours x rate, deals delayed). Price should be a small fraction of it (often 10-20%).
- **Alternatives:** the "do nothing" or manual cost, plus competitors' public prices.
- **Cost floor:** your variable cost per customer plus the income needed to reach target MRR.
- **Price-sensitivity questions (Van Westendorp):** at what price is it too cheap to trust, a bargain, getting expensive, too expensive? Ask 10+ buyers; look for overlap of "bargain" and "getting expensive".
- **Gabor-Granger:** show a few prices, ask if they would buy at each.
- **Stated vs revealed:** what people say is weak; a deposit or pilot fee is strong. Prefer revealed evidence.
- **Tier design:** limit by value metric (questionnaires, seats, projects), not by arbitrary feature locks.

## Application
1. Compute the **value anchor** and **alternatives table** with sources and evidence grades.
2. Compute the **customers needed** for the target MRR at three prices.
3. Draft **2-3 tiers** with a clear value metric and limits.
4. Add **price questions** to interviews (Van Westendorp or Gabor-Granger) and record answers per person.
5. Run a **revealed test**: pre-sell at two prices to comparable audiences (one price each), or a ladder across pilots.
6. Pick a **launch price** at the lower end of the viable range; plan an increase for later cohorts. Grandfather early users openly.
7. Set a **review trigger** (for example after 20 customers or 3 months) to revisit with real data.

### Output template
```markdown
## Value anchor (cost of the problem today)
## Alternatives and prices
## Customers needed at each price
## Tier draft (value metric, limits)
## Willingness-to-pay data (per respondent)
## Revealed test plan and result
## Launch price and review trigger
```

## Examples
See `examples/trustreply.md`.

## Common Pitfalls
- Pricing by cost or by copying a competitor without a value anchor.
- Trusting stated willingness to pay from friendly respondents.
- Too many tiers before you have users.
- Free-forever plans that attract non-buyers.
- Never revisiting the price after launch.

## References
- Related: `demand-test`, `finance-based-pricing-advisor`, `jobs-to-be-done`, `competitive-research-snapshot`, `saas-economics-efficiency-metrics`
