# Step 2a - Where the buyers are, before interviewing
Skills: `voice-of-customer-miner`, `discovery-interview-prep`
Date: 2026-10-24

## Method and limits (read first)
- Sources: web search summaries only. Direct page fetches of reddit.com, news.ycombinator.com, dev.to,
  hn.algolia.com and several blogs were **blocked by this environment's network policy**.
- So every "evidence" item below is a **paraphrase from a search summary, not a verbatim quote**,
  with a link to open and confirm. Nothing here is a copied comment.
- I found **no direct Reddit thread** on this topic. Reddit evidence is thin and unverified.
- No hours-per-questionnaire figure was found. Hour numbers in the results were for SOC 2 prep (H2 still unproven).

## 1. Where they hang out
| Place | What I found | Confidence |
|---|---|---|
| Hacker News | Several Ask HN / discussion threads on SOC 2 and security questionnaires (links below) | verified exists |
| DEV Community (dev.to) | At least 5 posts on questionnaires stalling small-SaaS deals; many written by vendors/consultants | verified exists, noisy |
| r/SaaS, r/startups | A Reddit-mirror snapshot of a post asking how small SaaS teams answer questionnaires without overstating maturity; not directly readable | partial |
| r/cybersecurity, r/netsec, OWASP Slack, ISACA forums | Listed in a 2026 community roundup; these are security practitioners (answerers), not founders (buyers) | verified exists, wrong side of the table for pain |
| vCISO and SOC 2 auditor circles | Many vCISO firms advertise "answer library" services; they are both competitors and referrers | verified exists |
| LinkedIn, Indie Hackers, founder Slacks | My prior knowledge, not confirmed by this search | unverified |

No community dedicated to security questionnaires was found. The pain surfaces inside broader SOC 2 and startup-security conversations.

## 2. What they are discussing
1. **Custom spreadsheets, same questions worded differently.** Buyers send their own format. (HN, dev.to)
2. **Deals stall when the form arrives.** Often right after a good demo. (dev.to, Sprinto, StartupDefense)
3. **Nobody owns it.** Form bounces from sales to engineering. (dev.to)
4. **"Should we just get SOC 2?"** Recurring debate; commenters say SOC 2 reduces but does not remove questionnaires. (HN)
5. **Honesty vs overstating.** Advice: say "partial" or "under review" rather than a bare "no" or a made-up "yes". (dev.to, Vera, Reddit-mirror post)
6. **Skepticism about the questionnaires themselves** ("dumb", low-signal, outdated). (HN)

## 3. Evidence (paraphrased from search summaries; open each link to confirm wording)
| # | Claim | Source |
|---|---|---|
| E1 | Standard vendor-security process is a giant Excel questionnaire sent by the prospect | [HN: What should I do when asked for SOC2?](https://news.ycombinator.com/item?id=24486697) |
| E2 | A commenter reports questionnaires up to ~300-400 questions; another mentions ~1000 rows | [HN: Our Dumb Security Questionnaire](https://news.ycombinator.com/item?id=25793230) |
| E3 | Certifications reduce but do not eliminate questionnaires; still a time drain needing expert input | HN threads above |
| E4 | Commenters suggest pointing buyers at a standard questionnaire (CAIQ, VSAQ, VSA Core) instead of custom ones | HN threads above |
| E5 | Teams "got tired of endless security questionnaires, so got SOC 2" (substitute risk) | [HN item 44362456](https://news.ycombinator.com/item?id=44362456) |
| E6 | Questionnaires "stall your deal"; nobody owns the form; answer bank of recurring questions recommended | [DEV: The Security Questionnaire That Stalls Your Deal](https://dev.to/ksoft_technologies_33f7f6/the-security-questionnaire-that-stalls-your-deal-2ob6) |
| E7 | Small SaaS deals "get weird" at the questionnaire stage | [DEV: Security Questionnaires Are Where Small SaaS Deals Get Weird](https://dev.to/bertb20/security-questionnaires-are-where-small-saas-deals-get-weird-2c1a) |
| E8 | First questionnaire with no SOC 2: answer honestly with controls you have | [DEV: Your first enterprise security questionnaire, and you have no SOC 2](https://dev.to/plainanswer/your-first-enterprise-security-questionnaire-and-you-have-no-soc-2-19mc) |
| E9 | A 200-question spreadsheet arriving at the worst moment of the sales cycle | [StartupDefense](https://startupdefense.io/blog/security-questionnaires-for-startups) |
| E10 | Cold-war era "irrelevant" questions; questionnaires seen as low-signal chores | [Ramimac: Answering "Dumb Security Questionnaires"](https://ramimac.me/dsqs) |
| E11 | Prior art: Stacksi (YC) built questionnaire auto-fill, acquired by SafeBase in 2023 | [BusinessWire](https://businesswire.com/news/home/20230906917869/en/SafeBase-Acquires-Fellow-Y-Combinator-Backed-Stacksi-to-Fuel-Its-Vision-for-Zero-friction-Security-Assessments) |
| E12 | Reddit-mirror post: how can small SaaS teams answer without overstating maturity; mark unsupported as "needs review" | [Reddit mirror snapshot](https://reddit.sentinel-team.org/posts/1tve84w/snapshots/2026-06-05T22%3A07%3A22.18711Z) (not directly readable here) |

### What the evidence changes
- **Supports** H3 (deals stall) and the cite-or-abstain design (E5, E8, E12 show honesty is a live concern).
- **Does not yet support** H2 (8+ hours). 🔵 Still unproven.
- **New risk:** HN audiences push SOC 2 or standard questionnaires as the fix (E4, E5). Competition is partly "avoid the problem", not just other tools.
- **New competitive fact:** Stacksi/SafeBase (E11) did this idea before. Update `03-market.md`.
- **Noise warning:** much dev.to content is vendor marketing; do not treat it as customer voice.

## 4. Who to talk to without "ghosting" them
I could not verify who is "most active" (the activity data was not readable). Do not rely on my guess; build the list yourself:
1. Open the HN threads in E1, E2, E5. Note the **commenters who describe their own experience** (not generic advice). Those are your warm leads.
2. Open the dev.to posts in E6-E8. Split authors into *vendors* (skip as leads) and *practitioners* (keep).
3. Add vCISOs and SOC 2 auditors as **referrers**, not buyers.
4. Keep a sheet: handle, platform, thread link, quote that shows personal experience, role guess, status.

### Rules so it does not feel like ghosting or farming
- Say who you are and that you are researching, in the first message.
- Reference their specific comment so it is clearly not a mass message.
- One small question, easy to answer in one reply. Offer a 15-minute call only if they volunteer.
- Give first: a short checklist or the anonymized findings, shared back to everyone who helped.
- Respect community rules on self-promotion; do not link a product you have not built.
- Never DM-blast; cap at a few per day.

## 5. Content that pulls real answers (psychology)
These are general behavioral heuristics, **not yet tested on this audience**. Treat each as an experiment.
| Principle | How to use it |
|---|---|
| **Correction beats questions** (people love fixing a wrong claim) | Post a specific draft: "Here are the 12 questions I think appear in nearly every questionnaire. What did I get wrong?" |
| **War stories are status** | Ask "What was the worst questionnaire question you ever got?" Experts enjoy telling and being right. |
| **Low effort to reply** | One concrete question, answerable in a sentence. |
| **Specific numbers invite correction** | "I assume it takes 10+ hours; is that high or low?" beats "how long does it take?" |
| **Honest learner framing** | "I'm researching, not selling" lowers defenses and invites mentoring. |
| **Reciprocity** | Offer a free artifact first (a blank answer-library template). |
| **Shared enemy** | Frame around the dumb form, not around a product. |
| **Avoid** | pitches, links to a landing page, leading polls, vague "thoughts?" posts. |

### Post templates (draft; check each community's rules)
- **HN (Ask HN):** "Ask HN: What's the dumbest or most time-consuming security questionnaire question you've had to answer as a small vendor, and how did you handle it?" 
- **r/SaaS or r/startups:** "I keep hearing founders lose a week to enterprise security questionnaires. For those who've done one: roughly how many hours, who did it, and did the deal slip? Genuinely trying to learn, not selling anything."
- **dev.to / blog:** "The 12 questions in every security questionnaire (and what I'd answer as a 10-person SaaS). Tell me what I got wrong."
- **LinkedIn:** short post with the same 12-question list and an invitation to correct it.

### Experiment design
Run 3 variants (correction post, war-story post, number-anchor post) across 2 communities each.
Measure: replies, % that contain personal experience, DM opt-ins to talk, hours stated. Keep the winner.

## 6. Next actions
1. Allow the blocked hosts so I can pull verbatim comments (see below), or paste the threads yourself.
2. Build the lead sheet from E1, E2, E5, E6-E8.
3. Post one correction-style post, collect replies for 5 days, then start interviews with the volunteers.

### Network access needed for real verbatim evidence
Hosts denied in this session: `www.reddit.com`, `news.ycombinator.com`, `hn.algolia.com`,
`hacker-news.firebaseio.com`, `dev.to`, `reddit.sentinel-team.org`, `ramimac.me`, `chair6.net`.
Change it under the environment's network access settings (cloud environment menu in the session title bar, then Edit):
https://code.claude.com/docs/en/cloud-environments#network-access
