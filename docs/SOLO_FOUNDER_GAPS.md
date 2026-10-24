# Missing for solo founders

What the upstream PM skills (deanpeters/product-manager-skills, 77 skills) do not cover well when you are
one person with no customers, no audience, and no team. Based on the skill list, descriptions, and keyword
searches, not a line-by-line read of every skill. Verify before relying on it.

## Why gaps exist
The upstream set is written for working PMs inside a company: existing users, sales calls, support tickets,
stakeholders, a team to hand work to. A solo founder starts with none of that.

## Gaps, ranked by when they hurt (workflow order)
| # | Missing skill | Why a solo founder needs it | Closest existing |
|---|---|---|---|
| 1 | ~~Idea selection and scoring~~ **added** (`idea-selection`): **Idea selection and scoring** (founder-market fit, pain, reachability, time-to-revenue, kill criteria) | Choosing the wrong idea costs months | `product-strategy-session` (assumes a product exists) |
| 2 | **Beachhead / ICP selection** (pick one narrow first segment) | Focus beats breadth at zero users | `proto-persona`, `market-landscape-scan` |
| 3 | ~~Community discovery~~ **added** (`community-discovery`) | No audience to recruit from | `voice-of-customer-miner` (quotes only) |
| 4 | ~~Research outreach~~ **added** (`research-outreach`) | Strangers will not reply to pitches | none |
| 5 | ~~Demand tests~~ **added** (`demand-test`): **Demand tests**: landing page, waitlist, fake door, pre-sell (paid pilots) | Proves willingness to pay before building | `pol-probe` (feasibility/usability tilt) |
| 6 | ~~Pricing research~~ **added** (`pricing-research`): **Pricing research for a new product** (Van Westendorp, Gabor-Granger, pre-sell price ladders) | Price is guessed; no ARPU or churn history yet | `finance-based-pricing-advisor` (needs existing data) |
| 7 | **MVP scoping and build-vs-buy** (concierge/Wizard-of-Oz first, cut list, buy not build) | Prevents 3-month builds for unvalidated ideas | `epic-breakdown-advisor`, `prd-development` |
| 8 | **AI-build handoff** (turn a PRD into agent-ready specs, acceptance tests, guardrails for vibe coding) | Quality and security of AI-written code is on you | `prd-development`, `user-story` |
| 9 | **Distribution plan before launch** (one channel, owned audience, content calendar) | Building without distribution is the common failure | `acquisition-channel-advisor` (assumes live channel) |
| 10 | **Launch playbook** (Show HN, Product Hunt, communities, email list) | One-person launch needs a checklist | none |
| 11 | **Founder sales**: outbound scripts, demo, objection handling, pilots | First 20 customers come from you | `battle-card-builder` (competitive only) |
| 12 | **Onboarding and activation design** | First-session value decides retention | `customer-journey-map` |
| 13 | **Analytics from zero** (minimal event plan, what to log on day one) | Metrics skills assume data exists | `saas-revenue-growth-metrics` |
| 14 | **Support and feedback loop for one person** (triage, tagging, weekly review) | Feedback arrives faster than you can sort | `voice-of-customer-miner` |
| 15 | **Weekly operating cadence and focus** (time budget across build/sell/learn) | Solo time is the scarce resource | none |
| 16 | **Persevere / pivot / kill with runway** (decision gates tied to months and cash) | Sunk-cost bias without a team to challenge you | `eol-readiness-advisor` (product sunsets) |
| 17 | **Bootstrapped economics** (runway, personal break-even, price to reach salary) | Different goal than VC unit economics | `saas-economics-efficiency-metrics` |
| 18 | **Trust and legal basics** (terms, privacy policy, DPA, data handling page) | B2B buyers ask on day one | none |
| 19 | **Build in public / audience building** | Cheapest early distribution | none |

## Upstream skills to skip as a solo founder
`stakeholder-*`, `director-readiness-advisor`, `vp-cpo-readiness-advisor`, `executive-onboarding-playbook`,
`leadership-transition`, `eol-stakeholder-sequence`, `eol-internal-enablement`, `agent-orchestration-advisor`
(until you have complexity that needs it).

## Suggested build order for new skills
1. `idea-selection`, 2. `demand-test`, 3. `pricing-research`, 4. `mvp-scoping`, 5. `launch-playbook`,
6. `founder-decision-gates` (persevere/pivot/kill), 7. `ai-build-handoff`.
Each is a natural gate in `docs/FOUNDER_WORKFLOW.md`.
