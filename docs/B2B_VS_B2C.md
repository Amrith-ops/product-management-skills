# B2B vs B2C: which to pick
Date: 2026-10-24. Context: solo founder in India, 9-5 job, Western customers (`docs/FOUNDER_CRITERIA.md`).
Scores are my judgment (1-5); weights are mine and reflect the founder's stated criteria. Change the weights and the answer can change.

## The case that triggered this: White Glove Content (read 2026-10-24)
Source: [TrustMRR page](https://trustmrr.com/startup/white-glove-content) (markdown snapshot). TrustMRR says revenue figures come from Stripe via an API key; descriptions and the seller message are user-written.

| Fact | Value |
|---|---|
| What it sells | Done-for-you faceless video production as a subscription: scripts, AI voiceover, editing, thumbnails, optional auto-upload |
| Who buys | Faceless content creators, multi-channel operators, entrepreneurs, brands (listed audience: "Both") |
| Pricing | Starter $54/mo, Growth $124/mo, Pro $284/mo; no setup fee, month-to-month, clients keep ad revenue |
| Founded | 2026-04-17 |
| Monthly verified revenue | Apr $2.1k, May $22.4k, Jun $40.8k, Jul $45.9k, Aug $57.4k, Sep $68.3k, Oct (to the 24th) $52.8k |
| Current MRR / subscribers | $65.1k / 548 active subscriptions (about $119 average per subscriber) |
| Last 30 days | revenue $69.1k, MRR growth -1.0%, profit margin 65%, 17.3k visitors, $4.02 revenue per visitor |
| Team / funding | 2-5 people, bootstrapped |
| Stack | Cloudflare, Stripe, Vercel, OpenAI |
| Other | X followers 0; domain rating 5; listed for sale since 2026-09-16 at $2.5M (3.0x revenue) with 17 offers |

### What this shows
- **Timeline is faster than you said:** about 5 months from launch to roughly $57-68k a month, not 8-9. Growth has flattened: MRR is -1.0% over the last 30 days.
- **It is not pure consumer AI.** It is a productized done-for-you service sold to people who earn from content (prosumer / small operators), delivered by AI plus a team of 2-5. That is the same pattern as idea #16 (Geek Squad for AI).
- **It is volume-based:** 548 customers at about $119. Your goal of $16-20k needs about 135-170 customers at that price, or 32-40 at $500.
- **Margin is 65%, not software margin**, because delivery is partly human and AI costs are variable.
- **The founder listed it for sale after 5 months.** I cannot tell why. Possible reasons: flattening growth, churn, platform-policy risk for faceless AI content, or a planned exit. 🔵 Retention and churn are not public.
- **Acquisition channel is unknown.** X followers 0 and domain rating 5 suggest it did not come from organic social or SEO; Google Analytics is connected, but the page does not show the source of traffic. 🔵
- **Survivorship bias still applies:** this is one listed winner. The same page lists other consumer-AI businesses for sale with falling revenue, for example a video tool at -8.5%.

### Scored on the founder's 12 criteria (same 0/1/2 method)
| C1 | C2 | C3 | C4 | C5 | C6 | C7 | C8 | C9 | C10 | C11 | C12 | Total |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2 | 0 | 2 | 2 | 2 | 1 | 0 | 1 | 1 | 1 | 1 | 0 | **13** |
High revenue does not mean a fit: it fails "few clients" and "solo-buildable" because it needs hundreds of subscribers and a delivery team. The pattern (tiered, month-to-month, no setup fee) is what to copy, not the scale.

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
2. Prosumer is the bridge: consumer-style speed, B2B-style willingness to pay and lower support per dollar. White Glove Content is this type: a done-for-you subscription for people who earn from content.
3. Decide by evidence, not by one case study. Run `demand-test` on the top idea in each model (for example distributor order entry for B2B and one prosumer idea), with the same pass/fail thresholds, for 2 weeks.

## Next steps
- Copy the pattern in a narrower niche: a tiered, month-to-month, done-for-you subscription at $300-500 for 30-50 clients, where AI does most of the delivery.
- Find the acquisition channel of similar listed businesses (TrustMRR lists channels and categories) before choosing a niche.
- Run the two-week `demand-test` on one B2B and one prosumer offer.
- Note: the web-fetch tool still could not reach `trustmrr.com`; shell `curl` could, so read pages that way.
