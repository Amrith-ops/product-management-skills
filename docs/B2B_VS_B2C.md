# B2B vs B2C: which to pick
Date: 2026-10-24. Context: solo founder in India, 9-5 job, Western customers (`docs/FOUNDER_CRITERIA.md`).
Scores are my judgment (1-5); weights are mine and reflect the founder's stated criteria. Change the weights and the answer can change.

## The case that triggered this
White Glove Content (https://trustmrr.com/startup/white-glove-content), cited as consumer AI reaching about $60k MRR in 8-9 months.
**I could not open the page or find coverage of it**, so I know nothing about its product, price, customers, or channel. Open questions: what exactly does it sell, to whom (consumers or people who earn with it), at what price, and how did it get its first 100 customers?
What I could confirm about TrustMRR from search results: it lists startups whose revenue is verified through Stripe, LemonSqueezy or Polar, and its "MRR" figure is the last 30 days of revenue, so it can include one-off payments and does not prove recurring revenue or retention. A single success is also survivorship bias; the failures are not listed.

## Arithmetic for the founder's $16-20k/month goal
| Model | Price | Paying customers needed |
|---|---|---|
| B2B SMB | $500/mo | 32-40 |
| Prosumer | $100/mo | 160-200 |
| Prosumer | $50/mo | 320-400 |
| Consumer | $29/mo | 550-690 |
| Consumer | $15/mo | 1,070-1,330 |
Support, refunds and churn scale with customer count. With a 9-5 job, 40 clients is manageable; 1,000+ is a second job. 🔶

## Weighted comparison
| Factor | Weight | B2B (owner-operated SMB) | Prosumer (individuals who earn with it) | Consumer (general public) |
|---|---|---|---|---|
| Customers needed for $16-20k/mo | 15% | 5 | 3 | 1 |
| Support load next to a 9-5 | 15% | 3 | 3 | 1 |
| Churn / retention | 10% | 4 | 3 | 2 |
| Margin after AI cost and fees | 10% | 4 | 4 | 3 |
| Reachable in groups (distribution) | 10% | 4 | 4 | 3 |
| Time to first dollar | 10% | 2 | 4 | 4 |
| Legal / privacy risk (higher = safer) | 10% | 4 | 4 | 2 |
| Upside ceiling | 10% | 3 | 4 | 5 |
| Competition / copycat risk (higher = safer) | 10% | 3 | 2 | 1 |
| **Weighted score (1-5)** | 100% | **3.6** | **3.4** | **2.3** |

Result: B2B SMB 3.6, prosumer 3.4, consumer 2.3. B2B and prosumer are close; consumer trails mainly on customers needed, support, and copycats.
Sensitivity: if time-to-first-dollar and upside ceiling carry much more weight, prosumer and consumer move up. If support-load and stability carry more, B2B moves up.

## Why consumer is tempting and where it bites
- **For:** self-serve, fast to first revenue, high ceiling, viral channels (X, TikTok, communities).
- **Against (general patterns, not verified here):** many customers per dollar; higher monthly churn; refunds and chargebacks; per-user AI inference cost eats margin; platform dependence; daily content work to stay visible; copycats appear fast; privacy and minors' rules add legal risk.

## Recommendation
1. Treat **B2B owner-operated SMB** and **prosumer (people who earn money with the tool)** as the two real options. Consumer fails the founder's "few clients" and "9-5" constraints.
2. Prosumer is the bridge: consumer-style speed, B2B-style willingness to pay and lower support per dollar. Many fast-growing AI products are likely this type; check whether White Glove Content is.
3. Decide by evidence, not by one case study. Run `demand-test` on the top idea in each model (for example distributor order entry for B2B and one prosumer idea), with the same pass/fail thresholds, for 2 weeks.

## Next steps
- Paste the White Glove Content page details here (product, pricing, MRR history, channel) and I will analyze whether it is consumer or prosumer, and what is repeatable.
- Allow `trustmrr.com` in the environment's network settings if you want me to read TrustMRR pages directly.
