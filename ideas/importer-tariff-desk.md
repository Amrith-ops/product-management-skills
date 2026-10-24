# Alternative opportunity: tariff and landed-cost desk for small importers
Date: 2026-10-24. Source: the assistant's own knowledge (training data). **Nothing here has been searched or validated.** 🔶 assumption; 🔵 to verify.
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
