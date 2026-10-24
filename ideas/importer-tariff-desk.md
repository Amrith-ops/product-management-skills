# Alternative opportunity: tariff and landed-cost desk for small importers
Date: 2026-10-24. Source: first written from the assistant's own knowledge; **verified once on 2026-10-24 with web searches (summaries of vendor and law-firm pages, not primary sources)**. See the verification section below. 🔶 assumption; 🔵 to verify.
Related: `docs/FOUNDER_CRITERIA.md`, `ideas/DECISION.md`.

## One line
Small importers and wholesalers upload product lists and supplier invoices; the service returns the likely tariff classification (HTS code), the duty and tariff rates, and the true landed cost per item, flagging items that need a licensed broker's review.

## 1. Customer
Owner-run importers and wholesalers (family-owned retailers, distributors, small brands) that buy goods overseas and import $500k-$20M a year. Buyer: owner or purchasing/finance manager. Non-experts in customs. 🔶

## 2. Their problems
1. Duties and tariffs change often, so landed cost and margins are unclear. 🔶
2. Classifying each product correctly is confusing; mistakes can bring extra duty or penalties. 🔶
3. They depend on a customs broker for answers, slowly and per request. 🔶
4. Savings opportunities (correct classification, trade agreements, exclusions, duty drawback) go unnoticed. 🔶

## 3. Current solutions
Customs brokers (service, per entry or retainer); freight forwarders' tools; cross-border ecommerce tax and duty tools aimed at online stores; spreadsheets; in-house trade compliance staff at larger firms. 🔶 Many players exist; check what serves small non-ecommerce importers. 🔵

## 4. Solution
- Upload: product descriptions, supplier invoices, country of origin.
- Output: suggested classification with reasoning and cited public rulings; duty and tariff rates; landed cost per product; list of items for broker review.
- Price test: $300-$1,000 a month per importer, flat. 🔶
- Data moat: a curated mapping of customers' products to classifications, learned from broker corrections, plus a maintained rates and rulings database that updates with tariff changes.
- Safety: decision support only; partner with a licensed customs broker for filings; show confidence and cite sources.

## 5. Why now
Tariff changes have made landed cost hard to predict, and importers need faster, cheaper answers than a broker call. LLMs can read product descriptions and public rulings. 🔶 🔵 check how volatile tariffs are in late 2026.

## 6. Why me
4 years of software development; can build the data pipeline, classification workflow and review screen. No customs knowledge and no contacts, so the first step is conversations and a broker partner. 🔵

## Scored against the 12 criteria (0 fails, 1 partial, 2 fits)
| # | Criterion | Score | Note |
|---|---|---|---|
| 1 | USD | 2 | |
| 2 | Few clients, high revenue | 2 | 20-40 clients at $400-$1,000 is the target 🔶 |
| 3 | Remote | 2 | |
| 4 | Reachable as a group | 1 | importer and sourcing groups likely exist 🔵 |
| 5 | Less tech-savvy buyers | 1 | mixed; they cannot build classification data themselves |
| 6 | High margin | 2 | software margin |
| 7 | Under the radar / competition manageable | 1 | many customs and duty tools exist |
| 8 | Hair on fire | 2 | tariff cost and penalty risk 🔶 |
| 9 | Room in existing software | 1 | gaps for small non-ecommerce importers unverified |
| 10 | Opex under INR 50k | 2 | |
| 11 | Low legal risk | 1 | wrong classification can cost the customer; needs disclaimers and a broker partner |
| 12 | Solo-buildable | 1 | data accuracy and upkeep are hard |
| | **Total** | **18 of 24** | |

## Verify before investing time
- Competitors and prices for small importers.
- Where importers gather online and whether owners would talk.
- Whether licensing rules limit what a classification tool may say.
- Whether the tariff landscape still creates urgency.

## Other candidates considered (from knowledge, unverified)
- **Supplier price-change guard for distributors** (same jan-san buyer as the order desk): reads vendor price lists and flags margin leakage. Score about 19, reuses the same reach plan; strong outcome (saves margin).
- **RFQ quoting assistant for small machine shops:** learns from a shop's past quotes. Score about 17; strong reach (machinist forums), but heavy domain knowledge and drawing parsing.

## Verification results (2026-10-24)
**Verdict: weaker than first scored. Revised score 15 of 24 (was 18). Not recommended as the primary bet.**

| Question | What I found | Effect |
|---|---|---|
| Competition | Several classification and landed-cost tools already serve small importers: CustomsValidator (free tier; paid from $29 a month or $5 per analysis), HTS Code Lookup (free with in-app purchases, AI search, landed cost), CodeHTS (landed cost with Section 301, USMCA and fees; integrates with ecommerce and accounting), CustomsCity (CustomsAI), Gaia Dynamics (larger importers). Sources: [SaaSHub CustomsValidator](https://www.saashub.com/customsvalidator), [HTS Code Lookup](https://apps.apple.com/app/id6744954529), [Capterra CodeHTS](https://www.capterra.co.uk/software/1096629/CodeHTS), [CustomsCity](https://customscity.com/customsai-hts-classification/), [Gaia Dynamics](https://gaiadynamics.ai/blog/trade-compliance-software-in-2026-evaluating-vendors-for-tariff-management) | Crowded and cheap; my $300-$1,000 flat price has no support |
| What customers pay for help today | Customs brokers charge roughly $75-$400 per entry, bonds about $300-$750 a year, plus per-agency line fees. Sources: [Suaid Global](https://suaidglobal.com/insights/customs-broker-fees-2026/), [Racklify](https://racklify.com/encyclopedia/what-does-a-customs-broker-charge-typical-fees-billing-models-and-cost-drivers/) (vendor blogs) | Value anchors are per entry, not $500 a month |
| Where importers gather | Facebook groups, Discord servers and forums for importing from China exist (for example China Trading Forum, The Wholesale Forums). They are mostly sourcing and beginner communities, with promotional listings; nothing found on customs or tariff help. Source: [Supplyia list](https://www.supplyia.com/china-import-forum/) | Reach exists but skews to beginners and dropshippers who pay little |
| Legal | 19 CFR 111.1 defines "customs business" to include classification and valuation transactions with CBP and preparing filing documents, whether or not the preparer files them. A standalone tool that only suggests codes may fall outside it; preparing filings for a client probably falls inside. I could not confirm the text of the advice and licensing sections. Source: [19 CFR 111.1 (Cornell)](https://www.law.cornell.edu/cfr/text/19/111.1) | A broker or attorney review is needed before charging for anything filing-related |
| Tariff urgency | The Supreme Court ruled in February 2026 that IEEPA does not authorize broad tariffs; Section 122 and 232/301 actions followed and remain in flux. Sources: [Plante Moran](https://plantemoran.com/explore-our-thinking/insight/2026/02/supreme-court-strikes-down-ieepa-tariffs), [Miller Nash](https://www.millernash.com/firm-news/news/tariffs-in-flux-ieepa-and-section-122-struck-down-section-232-duties-expand) | Urgency is real |
| New angle: IEEPA refunds | CBP runs a refund tool (CAPE) in its ACE portal; only the importer of record or the licensed broker that filed entries can claim; Phase 3 was confirmed for October 6, 2026; finally liquidated entries may require filing suit; the government appealed on June 2, 2026. Sources: [Baker Tilly](https://www.bakertilly.com/insights/ieepa-refunds), [Thompson Hine](https://www.thompsonhinesmartrade.com/2026/09/cbp-confirms-october-6-2026-launch-of-phase-3-of-the-ieepa-tariff-refund-process/), [Holland & Knight](https://www.hklaw.com/en/insights/publications/2026/07/file-now-cits-order-confirms-only-importers-that-have-sued) | Big money and a deadline, but law firms, brokers and tax vendors already compete, only the importer or licensed broker may file (licensing issue), the rules are still in litigation, and the window is temporary, so it fails the data-moat and low-legal-risk criteria |

## Revised score (0 fails, 1 partial, 2 fits)
| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | Total |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2 | 1 | 2 | 1 | 1 | 2 | 0 | 2 | 0 | 2 | 1 | 1 | **15** |
Changes: criterion 2 (price anchors are low), 7 (crowded) and 9 (tools already exist) went down.

## What is still unverified
- Whether small non-ecommerce importers are underserved by the existing tools.
- Fees of refund-recovery services and attorneys.
- The tariff status after July 2026 beyond what the searches showed.
