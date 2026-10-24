# Founder Workflow

A repeatable loop for building a product from scratch as a solo founder, using the
PM skills in `.claude/skills/` and commands in `.claude/commands/`
(source: deanpeters/product-manager-skills, CC BY-NC-SA 4.0).

**Loop:** Frame → Discover → Size → Position → Strategize → Prioritize → De-risk → Define → Plan → Measure

Keep every output as markdown under `docs/` so each pass builds on the last.

## Gate rule
Do not write a PRD (step 8) until steps 1-4 each have a written artifact and
discovery evidence from at least a few real sources.

## Steps

### 1. Frame the problem
- Skills: `problem-statement`, `problem-framing-canvas`, `proto-persona`, `jobs-to-be-done`
- Output: `docs/problem.md`, `docs/persona.md`
- Prompt: "Use problem-statement and proto-persona for: <idea>. Who is blocked, what are they trying to do, why does it matter?"

### 2. Discover
- Command: `/discover <problem or opportunity>` (chains `discovery-process`, `problem-framing-canvas`, `discovery-interview-prep`)
- Extra: `voice-of-customer-miner` for public reviews/forums when interviews are slow
- Output: `docs/discovery.md` (interview plan, findings, validated/invalidated hypotheses)

### 2a. Find your audience before interviews
- Skills: `community-discovery`, then `research-outreach` (original to this repo)
- Output: `docs/community-map.md`, lead sheet, post experiment log
- Rule: mark evidence as verbatim, paraphrase, or unverified; never present a summary as a quote.

### 3. Size and scan the market
- Skills: `tam-sam-som-calculator`, `market-landscape-scan`, `competitive-research-snapshot`, `porters-five-forces`
- Output: `docs/market.md`
- Prompt: "Size the market for <product> with explicit assumptions, then scan competitors with cited sources."

### 4. Position
- Skills: `positioning-statement` (or `positioning-workshop`), `press-release`
- Output: `docs/positioning.md`, `docs/press-release.md` (write the launch announcement before building)

### 5. Strategize
- Command: `/strategy <product>` (runs `product-strategy-session`)
- Output: `docs/strategy.md`

### 6. Prioritize bets
- Skills: `opportunity-solution-tree`, `feature-investment-advisor`
- Command: `/prioritize` (uses `prioritization-advisor` to pick RICE, ICE, value/effort, etc.)
- Output: `docs/priorities.md`

### 7. De-risk cheaply
- Skills: `pol-probe-advisor`, `pol-probe`, `derisk-measurement-advisor`
- Output: `docs/probes/<name>.md` (hypothesis, probe, pass/fail threshold, result)
- Rule: test the riskiest assumption before writing real code.

### 8. Define
- Command: `/write-prd <slice>`
- Skills: `epic-hypothesis`, `epic-breakdown-advisor`, `user-story-mapping`, `user-story`, `user-story-splitting`
- Output: `docs/prd/<slice>.md`, stories small enough to ship independently

### 9. Plan
- Command: `/plan-roadmap`
- Output: `docs/roadmap.md` (now / next / later with tradeoffs)

### 10. Measure
- Skills: `saas-revenue-growth-metrics`, `saas-economics-efficiency-metrics`, `business-health-diagnostic`, `acquisition-channel-advisor`, `finance-based-pricing-advisor`
- Output: `docs/metrics/<period>.md`; feed findings back into step 1 or 6.

## Cadences

**Weekly:** `/discover` → `pol-probe` → `/prioritize` → `/write-prd` (one small slice) → build → measure.

**Once per product:** `positioning-statement`, `tam-sam-som-calculator`, `competitive-research-snapshot`, `/strategy`.

**Quarterly / monthly (re-check prior work):** `competitive-intel-watch`, `pestel-delta-monitor`, `pricing-packaging-tracker`.

**Retiring something:** `eol-process`.

## Skip until you have a team
`stakeholder-identification`, `stakeholder-mapping`, `stakeholder-engagement-advisor`,
`director-readiness-advisor`, `vp-cpo-readiness-advisor`, `executive-onboarding-playbook`,
`/leadership-transition`.

## Support skills (called by others, rarely used directly)
`workshop-facilitation`, `autonomous-investigation`, `context-engineering-advisor`.
