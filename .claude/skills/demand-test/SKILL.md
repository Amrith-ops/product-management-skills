---
name: demand-test
argument-hint: "[offer to test and target audience]"
description: Test whether people will pay before you build, using a landing page, waitlist, fake door, or paid pre-sell, with pass/fail thresholds. Use after problem validation and before the MVP.
intent: >-
  Design a cheap demand experiment that measures real commitment (email, deposit, paid pilot) rather than compliments. Produces the offer page spec, traffic plan, thresholds, and decision rule.
type: workflow
best_for:
  - "Checking willingness to pay before building"
  - "Choosing between waitlist, fake door, and pre-sell"
  - "Setting honest pass/fail numbers in advance"
scenarios:
  - "Test demand for my questionnaire tool before coding"
  - "Design a pre-sell for a $149/mo product"
theme: validation-experiments
estimated_time: "30-45 min"
---

## Purpose
Show that real buyers will take a costly action. Complements `pol-probe` (which tests feasibility or usability) by testing **commitment**.

## Input
**Works best with:** positioning statement, target persona, price hypothesis, a channel where the audience gathers (from `community-discovery`).

## Key Concepts
Commitment ladder, weakest to strongest:
1. Click / view
2. Email signup
3. Sample submission or call booked
4. Paid deposit or pre-order
5. Paid pilot with real data

- **Compliments are not data.** "Sounds great" costs nothing.
- **Honesty rule:** a fake door or pre-sell must say it is early access; refund promptly if you do not ship. Never charge for something you cannot deliver.
- **Traffic quality > volume.** 100 relevant visitors beat 5,000 random ones.
- **Pre-register thresholds** before launching so you cannot move the goalposts.

## Application
1. State the **offer**: who, what outcome, price, delivery date, early-access terms.
2. Pick the **rung** you need (usually rung 4 or 5 for B2B).
3. Spec the **page**: headline from the positioning statement, 3 benefits, how it works, price, one call to action, an honest "early access" note.
4. Plan **traffic**: communities, direct outreach, referrals. Target 100-300 relevant visitors; list sources.
5. Set **thresholds** (example: 100 relevant visitors -> 5 signups -> 1 paid pre-order; fail = under 2 signups).
6. Define **tracking**: visits by source, signups, bookings, payments. A spreadsheet is enough.
7. Run for a fixed window (7-14 days).
8. **Decide**: pass -> build MVP; mixed -> fix message or channel and retest once; fail -> stop or reposition.
9. Contact every non-buyer who engaged and ask one question: what stopped you?

### Output template
```markdown
## Offer
## Commitment rung and rationale
## Page spec
## Traffic plan
## Thresholds (pass / fail)
## Tracking sheet
## Result and decision
## Why non-buyers did not buy
```

## Examples
See `examples/trustreply.md`.

## Common Pitfalls
- Counting visitors or likes as demand.
- Irrelevant traffic (ads to a broad audience).
- Changing thresholds after seeing results.
- Charging without a clear delivery promise and refund path.

## References
- Related: `pol-probe`, `pol-probe-advisor`, `positioning-statement`, `pricing-research`, `community-discovery`
