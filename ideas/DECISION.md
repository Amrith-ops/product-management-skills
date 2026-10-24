# Decision: what to work on (v2, supersedes v1)
Date: 2026-10-24. Reason for change: the founder does not want to sell to technical buyers, who compare the product with building it themselves or an open-source option unless there is a data moat.

## Changes from v1
- **Trustreply is parked** (not dropped): its buyers are technical founders.
- **Checked and rejected: permit and hail lead data for trades.** The data is public and commoditized: permit-lead services run from about $20-$50 a month for raw data to $50-$300 for curated leads (one is a flat $149), cheap scrapers sell permits at $30-$50 per 1,000 rows, and hail alerts start at $29.99 a month. Low price, weak moat. Sources: [PermitGrab listing](https://www.saashub.com/permitgrab), [Apify permit leads](https://apify.com/oldbie/construction-permit-leads), [Hail Drive pricing](https://haildrive.com/pricing). Also, using permit data for calls or texts raises TCPA and CAN-SPAM risk ([guide](https://blog.clickpointsoftware.com/2025-guide-to-tcpa-one-to-one-consent-can-spam-state-regulations)); a lawyer should review any campaign.
- **Corrected: distributor order entry is more crowded than I said.** Vendors include Pepper Order Agent (food distribution), Cut+Dry, Commercio (aimed at small distributors), WizCommerce Ella and Comena (YC). Sources: [Facilis](https://facilisgroup.com/commercio-distributor-team-of-4-ditches-paper-processes-saves-hours-per-order), [Pepper](https://www.usepepper.com/products/order-agent), [Cut+Dry](https://insights.cutanddry.com/post/streamlining-order-management-with-ai-order-desk).

## About the "data moat" worry
For non-technical owners the "I can vibe-code this in a week" risk mostly disappears: they will not build it. The real defenses are trust, workflow and accumulated data. A product that learns from use creates its own data over time:
1. Customer-specific mappings (how each buyer describes items, units, pack sizes) to the distributor's SKUs.
2. Per-customer pricing and discount rules remembered from past orders.
3. A normalized manufacturer catalog shared across distributors in the same vertical (grows with each client).
Honest limit: the moat is thin at the start and strengthens with each client.

## Decision
**Primary bet: an order desk for small owner-run distributors, in one vertical, sold service-first** (owner forwards orders by email, text or photo; you return clean order entries, with AI doing most of the work). Price test: $400-$800 a month per distributor. Differentiate on one vertical, human review, a flat price and zero integration, not on features.
**Why still this one:** non-technical buyers, a quantified cost per order (vendor claim of $10-$12 per order, unverified), low legal risk, no field work, buildable without ERP integration, and a data asset that grows.
**Biggest unknown: can you reach these owners?** I found trade associations (NAW, aimed mostly at larger firms; buying groups such as Affiliated Distributors for construction and industrial supply) but no community of small distributor owners. So the first test is reach, not product.

## Sprint (14 days, about 10 hours a week)
| Days | Action | Pass |
|---|---|---|
| 1-4 | **Reach test:** pick one vertical; find 30 owners or general managers at $5-50M distributors (LinkedIn, association member lists, buying-group directories); send 20 personal messages that ask one question: "How many orders a day come by email or text, and who keys them?" | At least 5 replies (25%), 3 agree to talk |
| 5-10 | 8 conversations: orders per day, minutes per order, error cost, ERP in use, who approves software, what they pay now | Median 25+ orders a day keyed by hand |
| 8-14 | 3 paid pilots: you process one week of real orders for $300-$500 | At least 2 pay, accuracy of 95%+ after review |

## Fallback (if reach test fails: fewer than 5 replies from 20 messages, or fewer than 3 conversations)
Switch the buyer community to **trades business owners** (roofing, HVAC, plumbing). Reach there is verified: Reddit's roofing community (reported 80,000+ members), RoofingTalk, ContractorTalk and Facebook groups such as Contractors Helping Contractors and Roofing Business Owners Only (sources: [JobNimbus forums](https://www.jobnimbus.com/blog/top-roofing-forums), [JobNimbus Facebook groups](https://jobnimbus.com/blog/the-7-best-roofing-groups-to-join-on-facebook); vendor blogs, so check activity yourself). Run the same sprint with 8 conversations to choose the problem (slow lead follow-up, quote chasing, lost jobs), then pilot the one owners say costs them most. Trades marketing is priced at $2,000-$6,000 a month including ads, so outcome-based offers can carry $500+.

## Stop rules
- No new research until the sprint ends. Decisions come from conversations and pilot payments.
- If both paths fail their gates, stop and review the criteria, not the idea list.

## Next actions
1. Choose the vertical (suggestion: the one where you can find owners fastest; decide in the first hour).
2. Draft the one-question message, a tracking sheet, and the pilot offer.
3. Check employment contract and Indian export-tax setup before taking payment (CA).
