# Domain selection under 12 founder constraints
Skill: `idea-selection` (adapted: constraints as gates). Date: 2026-10-24.
Evidence: web search summaries, mostly vendor marketing. Scores are my judgment, not validated. 🔶 = assumption, 🔵 = open question.

Full original criteria: `docs/FOUNDER_CRITERIA.md`. The table rows below are shortened.

## 1. Where the constraints conflict (read first)
| Constraint | Issue | Resolution |
|---|---|---|
| #6 "profit margin > 100%" | Gross margin cannot exceed 100%. | Target 85-95% gross margin; judge by ROI to the client (>5x) and net margin after LLM, payment, tax costs. |
| #2 "ultra-rich / family business" | Family offices and very rich families are privacy-heavy, trust-first, often regulated; a Deloitte survey (1,587 family firms, all $100M+ revenue) lists privacy and trust in outside vendors among top barriers. That conflicts with fast sales (#2) and low legal risk (#11). | Target **owner-operated family-owned operating businesses** ($2-50M revenue), not family offices. |
| #5 not tech-savvy vs your 9-5 | Low-tech buyers expect hand-holding, which eats support time. | Design for **zero-integration, email-in/email-out** use plus a productized 30-minute onboarding call. |
| #7 under the radar vs #8 hair on fire | Hair-on-fire pain attracts competitors. | "Under the radar" means a niche too small for VCs (a ~$30-100M segment), not an empty market. 🔶 |
| #1/#2 revenue | $16-20k/mo from 30-50 clients = $400-650/mo each ($4.8-7.8k/yr). | Client must lose >$3k/mo to the problem, i.e. a measurable operational cost. |
| #11 + your job | Your employment contract may restrict outside work or claim IP. Indian tax rules apply to export income. | Check the contract; get a CA to confirm GST export zero-rating under LUT, FIRA/FIRC paperwork, and whether a US entity helps. 🔵 (not legal advice) |

## 2. Candidates scored (0 = fails, 1 = partial, 2 = fits)
| # | Constraint | A. Order entry for small distributors | B. Insurance-agency COI | C. Small trucking back office | D. Multi-unit franchisee reporting | E. Family offices / ultra-rich |
|---|---|---|---|---|---|---|
| 1 | Paid in USD | 2 | 2 | 2 | 2 | 2 |
| 2 | 30-50 clients reach $16-20k | 2 | 1 | 0 | 1 | 2 |
| 3 | Remote, no field work | 2 | 2 | 2 | 2 | 1 |
| 4 | Reachable in groups | 1 | 2 | 2 | 1 | 0 |
| 5 | Less tech-savvy buyers | 2 | 1 | 2 | 1 | 1 |
| 6 | High margin | 2 | 2 | 2 | 2 | 2 |
| 7 | Under radar / competition manageable | 1 | 0 | 0 | 1 | 1 |
| 8 | Hair on fire | 1 | 1 | 2 | 1 | 1 |
| 9 | Room in existing software | 1 | 0 | 0 | 1 | 1 |
| 10 | Opex under ~INR 50k/mo | 2 | 2 | 2 | 2 | 2 |
| 11 | Low legal/compliance risk | 2 | 1 | 1 | 2 | 0 |
| 12 | Solo-buildable | 1 | 1 | 2 | 1 | 0 |
| | **Total (max 24)** | **19** | **15** | **17** | **17** | **13** |

### Evidence behind the scores
- **A. Distributors:** Orders arrive by email, PDF, spreadsheet, fax and are re-keyed into an ERP; one vendor (WizCommerce) estimates ~20 min and $10-12 per order (vendor claim, unverified). Funded vendors already exist (WizCommerce, Comena via YC, Y Meadows, TrueCommerce) and mostly serve larger or ERP-integrated accounts. Sources: [Y Meadows](https://ymeadows.com/en/insights/blog/ai-order-entry-for-distributors/), [Distribution Strategy: WizCommerce](https://distributionstrategy.com/2026/06/wizcommerce-launches-ai-order-entry-tool-for-distributors/), [Comena (YC)](https://www.ycombinator.com/launches/O3U-comena-ai-agents-that-automate-order-processing-for-distributors-and-manufacturers).
- **B. Insurance COI:** real pain (about 3.5 hours/day at 100 certificates), but Vertafore, NowCerts + Certificial, and AI-phone vendors already cover it, and it is tied to agency-management systems. Sources: [Rough Notes](https://roughnotes.com/automating-certificates-of-insurance/), [Vertafore via Coverager](https://coverager.com/vertafore-unveils-integrated-certificates-solution-to-remove-service-bottlenecks-and-accelerate-distribution-velocity-for-agencies/).
- **C. Trucking:** strong pain and low-tech buyers, but many tools (Truckbase, Datatruck, Bubba, Dashdoc) and small carriers pay little; sources focus on 2-25 trucks, so $400+/mo per client is doubtful. Sources: [Dashdoc](https://www.dashdoc.com/en-US/blog/freight-billing-software-small-carriers), [Truckpedia](https://truckpedia.io/resources/best-tms-if-you-factor-streamline-cash-flow-and-operations).
- **D. Franchisee reporting:** month-end consolidation is slow; Autymate, Joiin, Keboola, Ceterus and Pilot already serve it. No independent evidence on how common the pain is. Sources: [Autymate](https://www.autymate.com/features/reporting-consolidation), [Keboola](https://www.keboola.com/solutions/financial-intelligence/franchise-networks).
- **E. Family offices:** [Deloitte family-business study](https://www.deloitte.com/global/en/services/deloitte-private/perspectives/family-business-technology-transformation.html): privacy and vendor trust are top barriers; sample is $100M+ only.
- **India payments:** vendor blogs say SaaS exports can be zero-rated under LUT and need FIRA for refunds; some suggest a US entity. Sources: [Skydo](https://www.skydo.com/blog/fira-gst-refund-saas-exporters-india), [Cashfree](https://www.cashfree.com/blog/indian-saas-global-payments-guide). Verify with a CA.

## 3. Lead hypothesis
**A. AI order entry for small family-owned distributors ($5-50M revenue), one vertical first** (for example foodservice, building supply, industrial or janitorial supplies).
- **Product shape:** customers forward POs to a dedicated email address; it extracts customer, SKUs, quantities, prices; flags uncertain fields; the owner approves; output is a clean spreadsheet/CSV import and a confirmation email. No ERP integration at first. This keeps setup and support low (#5, #12).
- **Why it fits:** ACV maths: at 50 orders/day, the vendor's $11 per order estimate implies ~$11k/month of labor; $450-600/mo is ~5%. 🔶 (vendor claim)
- **Revenue:** 40 clients x $500 = $20k/mo; 30 x $550 = $16.5k.
- **Main risks:** funded competitors; wrong-SKU errors shipping wrong goods (use review step and confidence flags); ERP integration demands as clients grow; reaching distributors (groups unverified 🔵).
- **Runner-up:** D, only if interviews show 10+ location operators will pay ~$500/mo.
- **Not recommended:** B, C, E.

## 4. What you can and cannot build solo (#12)
| Can | Cannot (yet) |
|---|---|
| Email ingestion, PDF/Excel extraction with an LLM, review UI, CSV/Excel export, billing, weekly digest emails | ERP/EDI integrations, mobile apps, hardware, anything needing certifications, 24/7 on-call |

## 5. Operations budget (#10), rough 🔶
Hosting and database about $40-80; LLM/OCR usage about $100-300 at 40 clients; email, monitoring, domain about $30; accountant about $50-100. Roughly $250-500/mo (about INR 21-42k at ~85/USD), under INR 50k. Payment fees (Stripe or a merchant of record) scale with revenue and sit outside that.

## 6. Support plan around a 9-5 (#3)
Email-only support with a stated 24-hour response; auto-alerts for failed extractions; weekly accuracy digest; self-serve answers; a monthly 20-minute check-in for the top clients; productized onboarding call booked outside office hours (US mornings fit India evenings).

## 7. Next steps (workflow)
1. Pick one distributor vertical; run `community-discovery` (trade associations, LinkedIn groups, buying groups, forums) 🔵 not yet done.
2. `research-outreach`; 8-12 owner/ops-manager interviews with the questions: orders per day, minutes per order, error costs, ERP, who keys them.
3. `demand-test`: 5 paid pilots at $400-500/mo.
4. `pricing-research`, then `/write-prd` only after the gate.
5. Kill criteria: fewer than 6 of 10 owners keying 20+ orders/day by hand; fewer than 3 of 5 pilots willing to pay by week 6.
