# TrustMRR stats page: checking three insights
Date: 2026-10-24. Source: https://trustmrr.com/stats (daily snapshot; "Last updated Oct 24, 2026"), plus my profile sample (`research/trustmrr/analysis.md`).
The founder noted three insights from the stats charts; each is checked below.

## What the stats page says (verified by TrustMRR from payment providers)
- Daily snapshot: about $1.96B verified revenue across 69M transactions.
- **Revenue distribution** (share of listed startups): $0-1k 67.6%, $1k-10k 17.0%, $10k-100k 10.3%, $100k-1M 4.1%, $1M+ 1.0%.
- **Time to growth** (months to reach revenue milestones; values read from the page's chart data): $0 to $1: 5, $1 to $1K: 5, **$1K to $10K: 6**, **$10K to $100K: 13.2**, $100K to $1M: 26.4.
- **Founder X followers:** 0-1K 53.9%, 1K-10K 12.0%, 10K-100K 2.4%, 100K+ 0.3%, unknown 31.3%.
- **Revenue vs X followers:** r=0.25 (n=6,023), "revenue trends higher as founder audience grows".
- **Follower growth vs revenue growth:** r=0.04 (n=354); revenue outpaced follower growth in 81% of cases.
- **Revenue vs domain rating:** r=0.43 (n=6,713). **Revenue vs time in business:** r=0.47 (n=7,435).
- **"High revenue ($1M+), least followers"** list: the lowest entries have 37, 67, 79, 79 and 80 followers, with $1.0M to $5.0M revenue.

## Verdict on the three insights
| # | Insight | Verdict | Why |
|---|---|---|---|
| 1 | People with fewer than 10 followers earn over $20k a month, so follower building is not needed | **Partly supported; the "under 10" part is not confirmed** | Supported: follower growth barely tracks revenue growth (r=0.04) and the revenue-vs-followers link is weak (r=0.25). In my profile sample (59 businesses with MRR of $20k or more) the median follower count is 147 and 27 of 59 have under 100. Not confirmed: 22 of those 59 show "0" followers, but a 0 probably means no X handle was linked (for example, Chatbase shows 0), so I cannot treat it as zero audience. The stats page's own "$1M+, least followers" list bottoms out at 37-80 followers and shows total revenue, not monthly. |
| 2 | 10% of businesses earn $10k-100k and 4.1% earn $100k-1M | **Numbers match, meaning is probably different** | The page's "Revenue Distribution" matches your figures (10.3% and 4.1%), but it appears to be total (all-time) revenue, not monthly. Its scatter plots use totals up to about $70M. The page does not say. So read it as "about 15% of listed startups have passed $10k in total revenue", not "earn $10k+ a month". It is also a self-selected set of listed startups, mostly tiny. |
| 3 | 6 months from $1k to $10k MRR, 1.2 years from $10k to $100k MRR | **Numbers are close; the unit is probably wrong** | The chart data gives 6 months ($1K to $10K) and 13.2 months ($10K to $100K), which is about 1.1 years, not 1.2. It says "revenue milestones", which most likely means cumulative revenue, not MRR. It also does not say whether these are averages or medians, and it covers only startups that reached each milestone (survivors). |

## What this means for the founder
- **A big X audience is not a prerequisite.** The follower evidence is weak, and the founder's buyers (low-tech owner-operators) are mostly not on X anyway. Reach them where they gather instead.
- **Plan on months, not weeks, and longer with a 9-5.** If the milestones are cumulative revenue, going from zero to $10k total takes about 16 months on these averages (5 + 5 + 6), and to $100k total about 29 months. Cumulative $10k is much easier than $10k a month, so these times understate the effort for $16-20k MRR. Fast cases exist: White Glove Content reached about $40k in its third month, and unfair.so about $32k MRR in about three months, but they are outliers.
- **Most listed businesses stay small:** 85% of listed startups are under $10k total revenue, so a defined kill rule and milestone gates matter (see `ventures/` examples).
- **Keep expectations separate:** treat any milestone figure as survivor-biased.

## Proposed milestone gates (for the parked idea, not validated)
| Gate | Target | By |
|---|---|---|
| First paid pilot | 1 customer paying | month 2-3 |
| Early traction | 5 paying pilots, about $2k MRR | month 4-6 |
| Proof | 15 clients, about $7k MRR | month 9-12 |
| Goal | 30-50 clients, $16-20k MRR | month 15-24 |
If a gate is missed by a quarter, rerun the interview and demand-test steps before building more.

## Caveats
- The stats page is a daily snapshot and may change. The charts you shared match its figures, but their units (total vs monthly) are not labeled.
- Correlations (r values) say little about cause. Small r means weak association, not "no effect".
- My 59-business sample is not random.
