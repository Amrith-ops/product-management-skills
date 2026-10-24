# Step 7 - De-risk with a Proof of Life probe
Skills: `pol-probe-advisor`, `pol-probe`
**Status: plan only. Not run.**

# PoL Probe: Cited First-Draft Questionnaire

## Hypothesis
If we draft answers only from a founder's own documents and cite each one, at least 70% of answers will be accepted without edits and the founder will pay $149/mo.

## Risk being eliminated
Accuracy and trust: can an LLM answer security questions faithfully from a small document set, and will founders accept it?

## Prototype type
Vibe-Coded PoL Probe (plus concierge: run it by hand for the first users).

## Target users
5 founders/CTOs from the discovery interviews, each with one real questionnaire and 3+ policy docs. 🔵

## Success criteria (harsh truth)
- **Pass:** median 70%+ of answers accepted unedited; zero fabricated claims (any uncited answer is flagged); 3 of 5 agree to a paid pilot at $149/mo.
- **Fail:** under 50% accepted, any fabricated claim presented as fact, or fewer than 2 of 5 willing to pay.
- **Learn:** which question categories fail; what documents are missing; real willingness to upload.

## Stack
Single script/notebook: parse xlsx -> chunk docs -> retrieve -> draft with citation -> abstain if no support -> write xlsx. No auth, no UI, no database.

## Timeline
Build 3 days, test 3 days (5 sessions), analyze 1 day, dispose of code on day 8 (keep the learnings doc).

## Disposal plan
Delete all uploaded customer documents after each session; record only anonymized accuracy stats.

## Second probe: demand
Landing page with the positioning statement, a sample-questionnaire upload, and a $149 pre-order for 3 months. Pass: 100 relevant visitors produce 5 email signups and 1 paid pre-order. 🔵

## Decision rule
Pass both -> build the MVP (Step 8). Pass accuracy but fail demand -> revisit positioning/channel. Fail accuracy -> narrow to one questionnaire type (e.g., SIG Lite) or stop.
