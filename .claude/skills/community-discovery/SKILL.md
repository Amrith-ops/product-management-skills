---
name: community-discovery
argument-hint: "[problem or audience to research]"
description: Find where a target audience gathers, what they say about a problem, and who can speak to it, with linked evidence. Use before interviews when you have no customer base or audience yet.
intent: >-
  Map the online communities where a target audience discusses a problem, collect linked evidence of what they say, and shortlist the people worth approaching. Built for solo founders with no existing customers who must recruit from scratch.
type: workflow
best_for:
  - "Finding where buyers hang out before you have any customers"
  - "Collecting linked evidence that a pain is real and recurring"
  - "Building a first outreach list without spamming"
scenarios:
  - "Where do small SaaS founders discuss security questionnaires?"
  - "Find evidence that freelancers struggle with late invoices"
theme: discovery
estimated_time: "60-90 min"
---

## Purpose
Answer four questions before any interview: **where** does the audience gather, **what** do they say about this pain, **what proof** can be linked, and **who** has first-hand experience. Output is a community map, an evidence table, and a lead sheet.

This is a pre-interview step. It feeds `voice-of-customer-miner` (quotes), `discovery-interview-prep` (recruiting), and `research-outreach` (contact).

## Input
**Works best with:** the problem statement and the persona (from `problem-statement`, `proto-persona`).
**Also useful:** competitor names, the industry's jargon, which side of the transaction feels the pain (buyer vs answerer).

## Key Concepts
- **Pain side vs answer side.** Communities of experts (who answer) differ from communities of sufferers (who ask). Interview sufferers; use experts as referrers.
- **Evidence grades.** Mark each item `verbatim` (exact text, link opened), `paraphrase` (from a summary, link not opened), or `unverified` (recalled, no link). Never present paraphrase as a quote.
- **Vendor noise.** Content written by vendors selling a fix is not customer voice. Tag it and exclude it from pain counts.
- **No dedicated community is a finding.** The pain may live inside broader threads (e.g., SOC 2, startup security). Say so.

## Application
1. **Restate** the problem, persona, and the exact words they use for it (3-5 phrases, including slang).
2. **Search** each platform with those phrases: Reddit, Hacker News, Indie Hackers, dev.to, LinkedIn, niche Slack/Discord, industry forums, review sites. Record what is reachable and what is blocked.
3. **Build the community map** (table): platform, community, audience side (sufferer/expert/vendor), size or activity signal, rules on self-promotion, evidence grade.
4. **Extract themes** (5-8): what they ask, complain about, recommend. Count threads per theme.
5. **Attach evidence**: per theme, 2-3 links with a grade. Prefer recent, first-person, specific (numbers, hours, dollars).
6. **Log counter-evidence**: who says it is not a problem, what they do instead (substitutes).
7. **Shortlist people**: only those with first-hand experience shown in a specific post. Fields: handle, link, what they said, side, role guess, status. Do not rank by follower count.
8. **Judge** which hypotheses (from `discovery-process`) got support, contradiction, or no data. Name what is still unproven.
9. **Hand off** to `research-outreach`.

### Output template
```markdown
## Community map
| Platform | Community | Side | Activity signal | Self-promo rule | Grade |
## Themes
| Theme | Threads | Example links (grade) |
## Counter-evidence and substitutes
## Lead sheet
| Handle | Link | What they said | Side | Role | Status |
## Hypothesis check
| Hypothesis | Support / Contradiction / No data | Evidence |
## Limits (what could not be reached or verified)
```

## Examples
See `examples/trustreply.md`.

## Common Pitfalls
- Counting vendor blog posts as customer pain.
- Treating a search-engine summary as a quote.
- Choosing "most active" posters by volume; heavy posters are often advisors, not buyers.
- Skipping the limits section when a platform was unreachable.
- Starting outreach before reading each community's rules.

## References
- Related: `voice-of-customer-miner`, `discovery-interview-prep`, `research-outreach`, `proto-persona`, `autonomous-investigation`
