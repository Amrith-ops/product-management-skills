# Step 8 - PRD (MVP)
Skills: `/write-prd`, `epic-hypothesis`, `user-story`
**Gated: do not build until Step 2 and Step 7 evidence is in.**

## 1. Summary
Trustreply turns a company's policies and past answers into cited first-draft answers for buyer security questionnaires, with a human review step and a reusable answer library.

## 2. Problem
See `01-problem.md`. 🔶 8-20 hours per questionnaire; deals delayed.

## 3. Users
Primary: Founder-CTO Frankie. Secondary: sales engineer.

## 4. Strategic context
Positioning and market in `03-market.md`, `04-positioning.md`.

## 5. Epic hypothesis
If we provide cited draft answers from the customer's own documents, then customers complete a questionnaire in under 1 hour, measured by time from upload to export.

## 6. Scope (MVP)
1. Workspace + email login.
2. Upload knowledge base (PDF, DOCX, MD, TXT). Show chunk count and status.
3. Import questionnaire (xlsx/csv). User maps question and answer columns.
4. Draft answers: each has text, citation(s) (doc, page/section), and confidence. If no supporting passage, status = "Needs human" with no generated claim.
5. Review queue: approve, edit, or reject; edits tracked.
6. Export back to the original file layout.
7. Answer library: approved answers reused for similar questions.
8. Billing (Stripe) with the two tiers.

### Non-goals
Portal scraping, SOC 2 workflows, trust center, evidence attachments, SSO, team roles beyond owner/member.

## 7. User stories (examples)
- As a founder, I upload my policies so that drafts come from my real controls.
  - Given a PDF, when processing completes, then I see its sections searchable and cited.
- As a founder, I see a citation under every answer so that I can verify it.
  - Given a draft, then each sentence maps to a passage, or the answer is marked "Needs human".
- As a founder, I export a filled xlsx so that I can send it unchanged.
  - Given an approved set, then the output keeps the buyer's columns, order, and formatting.

## 8. Success metrics
Activation: first export within 7 days of signup. Quality: unedited-accept rate, uncited-claim rate (target 0). Business: see `10-metrics.md`.

## 9. Trust and security requirements
Encryption at rest and in transit; documents not used for model training; per-customer isolation; delete-on-request within 30 days; subprocessor list and DPA published. 🔵 Provider terms to confirm.

## 10. Technical sketch (solo, AI-assisted build)
Next.js, Postgres with pgvector, object storage, a hosted LLM API (swappable), background jobs for parsing. Deterministic citation check: drop any answer whose cited passage does not exist in the source.

## 11. Assumptions and open questions
🔶 Buyers accept answers drafted by AI if the founder approves. 🔶 xlsx/csv covers most questionnaires.
🔵 Share of questionnaires arriving in portals or Word. 🔵 Legal exposure for incorrect answers (terms of service).
