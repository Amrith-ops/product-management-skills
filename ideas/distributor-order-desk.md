# Order desk for small distributors: problem and value proposition
Date: 2026-10-24. Status: hypothesis, not validated. Legend: ✔ supported by something I found; 🔶 assumption; 🔵 open question for the founder or for interviews.
Related: `ideas/DECISION.md` (the 14-day test), `ideas/distributor-order-entry.md` (earlier parked note).

## One-paragraph summary
Small family-owned distributors get customer orders as texts, photos of handwritten lists, voicemails, emails and PDFs, and staff retype each one into the system. It is slow and error-prone. We offer an order desk: the distributor sends us the messy order any way it arrives; AI reads it and a person checks it; we return a clean, correct order ready to enter, for a flat monthly fee.

## 1. Who is my customer
**Company:** owner-run (often family-owned) wholesale distributors, roughly $5-50M revenue, 10-100 employees, in **one vertical** (to choose: foodservice, plumbing/HVAC supply, building supply, industrial/MRO, or janitorial). 🔶
**Buyer (decides and pays):** owner or general manager. **Users:** customer-service and inside-sales reps who key orders; operations manager who sees the errors.
**What defines them:** orders arrive in mixed formats from many small customers (contractors, restaurants, shops); they run an ERP or accounting system but customers will not change how they order; they are not software-minded; sales cycles are short because the owner decides. 🔶
**Where to find them:** trade associations and buying groups (for example NAW; Affiliated Distributors for construction and industrial supply), LinkedIn. ✔ these exist; 🔵 no active community of small distributor owners found yet, so reach is unproven.

## 2. Their problems
Ranked by how much they probably hurt (all 🔶 until owners confirm):
1. **Retyping orders takes staff hours every day.** Trade press says inside sales and customer service rekey orders that arrive by email, PDF, spreadsheet and fax ✔ (vendor sources). A vendor claims about 20 minutes and $10-$12 per order 🔶 (vendor figure, unverified).
2. **Mistakes ship the wrong goods:** wrong item, quantity, unit or price leads to returns, credits and unhappy customers. 🔶
3. **Slow turnaround:** late entry means late picking and delivery; reps cannot answer the phone while typing. 🔶
4. **Growth needs more clerks:** every extra order volume needs another person. 🔶
5. **Knowledge sits in people's heads:** which customer calls an item what, which discount applies. 🔶

**Problem statement.** I am an owner of a small distributor. I am trying to get customer orders into the system quickly and correctly. But orders arrive in every format and my staff retype them. Because each customer orders their own way and will not change, software that needs a portal or EDI does not fit. This makes me feel that I am paying people to type, and worrying about the next costly mistake.

## 3. Current solutions
| Option | What it does | Why it falls short for a small owner-run distributor |
|---|---|---|
| Staff retype orders | Works, familiar | Slow, error-prone, does not scale |
| Customer portals / web ordering | Customers enter orders themselves | Many small customers will not use them ✔ (vendor argument: customers will not change how they order) |
| EDI | Standard machine-to-machine orders | Only for large trading partners; costly setup |
| AI order-entry software (WizCommerce Ella, Comena, Y Meadows, TrueCommerce PDF/email, Pepper for food, Cut+Dry, Commercio for small distributors) | Reads emails and PDFs and creates orders | ✔ exist and some target small distributors; typically need ERP integration, demos and annual contracts; may not handle phone, text and photo well 🔶 |
| Offshore data-entry outsourcing | People type for you | Cheaper than staff but still manual, with training and quality issues 🔶 |
| Do nothing | | The current state for many 🔶 |
**Honest read:** the space is crowded with funded vendors. We would win only with a narrower focus, a flat price, zero integration at the start and a person checking every order.

## 4. My solution
**The offer:** an order desk as a service.
- **How it works:** the distributor forwards or uploads each order as it arrives (email, text screenshot, photo, PDF, voicemail transcript). AI extracts customer, items, quantities, units and prices; matches items to the distributor's catalog; flags anything unsure. A person reviews flagged lines. We return a clean order (spreadsheet/CSV for their system, plus a confirmation) within an agreed time.
- **MVP without integration:** their staff import the file or paste it in; no access to their ERP needed at first.
- **Price test:** $400-$800 a month per distributor, flat, month-to-month. 🔶
- **Data moat (grows with use):** each customer's own wording mapped to the distributor's items and units; remembered pricing and discount rules; a normalized manufacturer catalog shared across distributors in one vertical.
- **Value proposition:** *Stop retyping customer orders. Send us the messy ones and get clean, checked orders back fast, for a flat monthly fee that is a fraction of a clerk's pay.*

**Positioning statement**
For owner-run distributors that lose hours each day retyping customer orders, the order desk is an order-entry service that turns any messy order into a clean, checked one. Unlike portals, EDI and enterprise AI order-entry software, it works with whatever format customers already use, needs no integration to start and costs a flat monthly fee.

## 5. Why now (market timing)
- **AI can now read messy inputs:** handwriting, photos and PDFs with usable accuracy at low cost. 🔶 (my general knowledge; test accuracy on real orders)
- **Vendors are launching:** WizCommerce launched an AI order-entry tool in June 2026 ✔; Comena (YC) targets distributors and manufacturers ✔. That signals demand and also competition.
- **Customers will not change:** vendors argue many customers will not move to portals or EDI, which is why AI intake is used ✔ (vendor argument).
- **Labor pressure:** hiring and wage costs push owners to automate. 🔶
- **Solo-friendly:** AI-assisted coding and cheap model access let one person build and run this. ✔ (consistent with the founder's constraints)
- 🔵 Missing: evidence from owners that this is a priority this year.

## 6. Why me
Fill in the founder's real strengths; the parts marked 🔵 need your answer.
- **Builder:** comfortable building with AI-assisted coding and shipping fast. 🔵 confirm your skills and years of experience.
- **Cost base and hours:** operating from India keeps costs low (target under INR 50k a month) and US mornings fall in your evenings, so an asynchronous service fits next to a 9-5. 🔶
- **Domain experience:** none known in distribution. 🔵 Do you know anyone who runs or works at a distributor, or have you done operations, ERP or data-entry work? This is the biggest gap; the first interviews and a pilot with one friendly distributor reduce it.
- **Unfair advantage:** none yet. It would come from one vertical's catalog knowledge and accumulated customer mappings.

## What would make this wrong
- Owners say entry takes minutes a day, not hours.
- Errors are rare or cheap.
- They will not send orders to an outside service (trust, speed).
- Their ERP or workflow needs live integration before any value shows.
- Competitors already serve their size at a low price.

## Next step
Use the 14-day test in `ideas/DECISION.md` to check the table in section 2 with real owners: orders per day, minutes per order, cost of a mistake, what they pay now.
