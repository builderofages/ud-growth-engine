# Database Reactivation Kit — the fastest money in the building
### Zero ad spend. UD already paid for these names once.

Every $10M home-services company sits on thousands of dead quotes, old inspections, and past customers. Reactivation typically books 3–8% of a clean list into appointments. On 2,000 old contacts at $14K avg job and 35% close, **even a 4% booking rate ≈ 28 jobs ≈ ~$390K signed** — from texts and calls that cost almost nothing.

**Compliance gate (non-negotiable):** SMS/calls only to contacts with prior business relationship or consent; honor opt-outs instantly; quiet hours 8am–8:30pm; business name in every message. Cold purchased lists → mail/door only.

---

## Segments (pull from their CRM/spreadsheets on access day)
| Segment | Who | Angle |
|---|---|---|
| A. Lost quotes <24mo | Inspected/quoted, never signed | "Prices & schedule changed — re-quote in 10 min" |
| B. Past customers 2+ yrs | Completed jobs | Roof Shield™ + referral reward |
| C. Claim-denied | Inspected, carrier denied | Financing: "$160/mo, not $14,000" |
| D. Storm-ZIP history | Anyone in a newly-hit ZIP | "Storm just hit your street — priority recheck" (auto via storm-trigger workflow) |

## Sequences (load into Agent 2)

**A — Lost quotes (6 touches / 14 days)**
1. SMS D0: "Hi {name}, {rep} from United Developers — we quoted your roof on {date}. We have install slots open in {city} this month and material pricing has shifted. Want a fresh number? Takes 10 min."
2. Call D1 (AI receptionist script): re-qualify, book inspection refresh.
3. SMS D3: photo of a just-finished local job + "your neighbors on {street} went ahead — happy to re-quote yours."
4. Email D6: re-quote letter + 131-review proof block + financing line.
5. SMS D10: "Last check-in — want me to close your file or hold a slot?" (takeaway close)
6. Voicemail drop D14.

**B — Past customers**
1. SMS: "It's been {n} years since your roof — want a free maintenance check? We'll send the photo report." → books Roof Shield™ pitch.
2. Email: Roof Shield launch ($19/mo) + $100 referral reward per signed neighbor.
3. SMS 30d later: referral nudge with personalized link.

**C — Claim-denied (financing)**
1. SMS: "Carrier said no — your roof still says yes. We now offer financing from ~$160/mo and retail pricing. Want options?"
2. Email: 3 payment scenarios on their exact quote.
3. Call: AI books retail estimate.

**D — Storm-ZIP (auto-fired by `tools/workflows/storm-trigger.n8n.json`)**
SMS within 2h of NWS alert: "{name}, hail was just reported near {street}. As a past UD customer you get priority inspection — reply YES and we'll slot you first."

## Offer math to approve with ownership
- Re-quote honor window (any quote <12mo honored ±5%) · $100 referral bounty · Roof Shield first-month free for segment B · financing partner live before segment C fires.

## KPIs (weekly scoreboard rows)
List size by segment · deliverability % · reply % (target 8–15%) · booked (target 3–8% of list) · signed $ · cost ≈ $0 ad spend · opt-out % (<2%).

**Day-one ask to UD:** export of all leads/quotes/customers (CSV is fine: name, phone, email, address, last activity, consent flag). Everything else is already built.
