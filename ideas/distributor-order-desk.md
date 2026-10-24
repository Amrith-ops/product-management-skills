# Order desk for small distributors: problem and value proposition
Date: 2026-10-24. Status: hypothesis, not validated. Legend: ✔ supported by something I found; 🔶 assumption; 🔵 open question for the founder or for interviews.
Related: `ideas/DECISION.md` (the 14-day test), `ideas/distributor-order-entry.md` (earlier parked note).

## One-paragraph summary
Small family-owned distributors get customer orders as texts, photos of handwritten lists, voicemails, emails and PDFs, and staff retype each one into the system. It is slow and error-prone. We offer an order desk: the distributor sends us the messy order any way it arrives; AI reads it and a person checks it; we return a clean, correct order ready to enter, for a flat monthly fee.

## 1. Who is my customer
**Company:** owner-run (often family-owned) wholesale distributors, roughly $5-50M revenue, 10-100 employees, in **one vertical: janitorial and sanitation supply** (see `ideas/janitorial-vertical.md`). 🔶
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
- **Solo-friendly build:** AI-assisted coding and cheap model access let one person build the software. Running the review is the harder part (see section 7).
- 🔵 Missing: evidence from owners that this is a priority this year.

## 6. Why would a customer choose me (and not their CRM, ERP or the AI vendors)?
**Why their existing software does not already solve it**
- **CRM** (for example HubSpot, Salesforce): tracks leads, deals and contacts. It does not read a photo of a handwritten parts list and turn it into order lines. 🔶 (general knowledge; confirm in interviews)
- **ERP / accounting system** (for example distribution ERPs, QuickBooks): stores orders, prices and stock, but expects the order to arrive already structured. Someone still types it in. Some offer customer portals or EDI, which small customers rarely use. ✔ (vendor argument that customers will not change how they order)
- **The missing step** is the translation from a messy message into a clean order, before it reaches the ERP. That is the gap.

**Honest answer on "why me" today: there is no reason yet.** You have no track record, brand or distribution experience. Funded vendors with more money can add this feature. The reasons a customer could pick you must be earned and made specific:
| Possible reason | Why it can matter | Status |
|---|---|---|
| One vertical, deeply known (their items, units, pack sizes) | Generic tools guess wrong on industry terms | Built through pilots 🔶 |
| Starts in 48 hours, no integration, no contract | Enterprise vendors need demos, setup and annual deals | Plausible 🔶 |
| Flat low price | Vendors price for bigger firms | Unverified 🔵 |
| Accuracy promise with a credit for errors | Owners fear wrong shipments | Must be earned with data 🔵 |
| Founder-led attention: the owner can call you | Small owners value reachability | True from day one |
| Learns each customer's wording over time | Switching later means losing that memory | Grows with use (the data moat) |
Until pilots prove accuracy, the real pitch is price, speed to start and attention, not technology.

**Why you (founder) personally.** Known facts: 4 years of software development experience; no distributor contacts; no stated operations, ERP or data-entry background; a 9-5 job; India-based (low costs, US mornings fall in your evenings).
- **What 4 years of dev gives you:** you can build the core reliably (document and image extraction, a review screen, data models, uptime) and debug it yourself. That is a real advantage over a non-technical operator. 🔶
- **What is missing:** domain knowledge (how distributors name items, units, pricing rules) and access to buyers. Both are the main risks, not the code.
- **So the honest "why me" is:** a builder who can iterate fast, who picks one vertical, learns it through pilots and keeps the price low. Not a domain expert yet.

### Closing the access and domain gaps (borrow what you do not have)
| Gap | Ways to close it |
|---|---|
| No distributor contacts | (1) Cold LinkedIn outreach to owners, customer-service and operations managers at distributors in one vertical, using the one-question message. (2) **Referral partners who already serve distributors:** ERP consultants and resellers for the systems small distributors use (they know many owners and see this pain), offered a referral fee. (3) Buying-group and trade-association events and member directories. (4) Offer one "design partner" distributor a free first month in return for access to their real orders and feedback. |
| No domain knowledge | (1) Pay 3-5 hourly calls with ex-customer-service, inside-sales or operations people from distributors (found through LinkedIn); ask how orders flow, what goes wrong, item naming. (2) Recruit one industry insider as an advisor, paid or with a small share. (3) Learn the vertical's catalog and vocabulary from public product catalogs. |
| Trust | A design partner and a written accuracy promise with a credit for errors. |
Both gaps make this idea riskier than it looked: you can build it, but you start without buyers or vocabulary. That is why the first step is a reach test, not code.

## 7. How the "human review" works for a solo founder with a 9-5
Doing every review yourself in real time does not work: US business hours run roughly 6:30 pm to 2:30 am India time, and you cannot check orders all day. Design it so your review time stays small:
1. **The distributor's own clerk approves.** AI drafts the order; their rep checks and clicks approve in seconds instead of typing for minutes. That is their "human in the loop", not yours.
2. **You only handle exceptions:** items the system cannot match with confidence. Teach it once and it remembers (the data moat), so exceptions shrink over time.
3. **Two fixed review windows a day** (for example in your evening), with an agreed turnaround, not instant.
4. **Pilots first, by hand.** With 2-3 pilots the volume is small enough to do manually while you learn what goes wrong.
5. **Later, a part-time trained reviewer** (hired and supervised by you) once accuracy and volume justify it. Watch data-privacy and quality risk.

**Illustrative capacity maths (assumptions, not data)**
| Scenario | Orders a day | Share needing your review | Minutes per reviewed order | Your daily time |
|---|---|---|---|---|
| 3 pilots, early | 90 | 40% | 2 | about 72 min |
| 3 pilots, after learning | 90 | 15% | 1 | about 14 min |
| 10 clients, mature | 300 | 10% | 1 | about 30 min |
| 10 clients, if review stays at 40% | 300 | 40% | 2 | about 4 hours (not workable) |
So it works only if the share needing review falls quickly. That is the main thing the pilots must measure. If it does not fall, either price higher, hire a reviewer, or drop the idea.

## What would make this wrong
- Owners say entry takes minutes a day, not hours.
- Errors are rare or cheap.
- They will not send orders to an outside service (trust, speed).
- The share of orders needing your review does not fall below about 15%, so review cannot fit around a 9-5.
- Their ERP or workflow needs live integration before any value shows.
- Competitors already serve their size at a low price.

## Next step
Use the 14-day test in `ideas/DECISION.md` to check the table in section 2 with real owners: orders per day, minutes per order, cost of a mistake, what they pay now.
