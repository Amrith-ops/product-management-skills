# Step 6 - Prioritize bets
Skills: `opportunity-solution-tree`, `prioritization-advisor`, `/prioritize`
Method: RICE (single founder, few data points, so use rough scores).

## Opportunity solution tree
Outcome: complete a buyer questionnaire in under 1 hour with answers the founder trusts.
- Opp A: Answers exist but are scattered -> knowledge base from uploaded docs.
- Opp B: Each questionnaire has a different format -> import xlsx/csv, export back in place.
- Opp C: Fear of wrong answers -> citations, abstain-when-unsure, review queue.
- Opp D: Same questions recur -> answer library with approved answers.
- Opp E: Buyers want evidence -> attach docs/links (later).

## RICE (Reach/month, Impact 0.25-3, Confidence %, Effort weeks)
| Feature | R | I | C | E | Score |
|---|---|---|---|---|---|
| Doc upload + retrieval with citations | 100 | 3 | 70% | 1.5 | 140 |
| xlsx/csv import and in-place export | 100 | 3 | 80% | 1.5 | 160 |
| Cite-or-abstain + confidence flag | 100 | 3 | 70% | 0.5 | 420 |
| Review/approve queue | 100 | 2 | 80% | 1 | 160 |
| Answer library (reuse approved answers) | 80 | 2 | 60% | 1 | 96 |
| Evidence attachments | 40 | 1 | 50% | 1 | 20 |
| Portal integrations | 20 | 2 | 30% | 6 | 2 |

## Decision
Build, in order: cite-or-abstain engine, xlsx/csv round trip, review queue, retrieval, library. Defer attachments, portals, integrations.
All scores 🔶 until discovery supplies real reach and impact.
