# Satellite Roof Intelligence — Instant Quotes + Speculative Outreach
### The "see your roof from space" weapon, built two ways

This is the tech you flagged: measure roofs from aerial/satellite imagery, generate the estimate and the visual **before the homeowner ever asks**. We deploy it in two directions — inbound (a conversion machine on the site) and outbound (the highest-converting cold outreach play in home services).

---

## 1. The tech stack (what actually powers it)

| Layer | Tool | What it gives us | Cost reality |
|---|---|---|---|
| Roof geometry | **Google Solar API** (`buildingInsights`) | Roof area (m²), segment count, pitch per segment, sun data — by lat/lng, instant | ~$0.01–0.10/lookup; covers most US homes |
| Imagery | **Google Maps Static / Aerial View API** | Satellite/45° aerial image of the exact home | pennies per image |
| Geocoding | Google Geocoding API | Address → coordinates | pennies |
| Pro measurement (close stage) | **EagleView / Hover / Roofr reports** | Insurance-grade measurement reports reps attach to claims | ~$15–60/report, only on serious deals |
| Mockups | AI image editing (e.g., generative fill on the aerial/street photo) | "Your house with the new roof / solar" visual | near-zero |

**Two-tier discipline:** cheap instant data (Google) for lead gen at scale; paid insurance-grade reports (EagleView-class) only once a deal is real. Never pay $50/report to generate leads.

---

## 2. Weapon 1 — Inbound: "Instant Satellite Roof Quote" *(BUILT → `website/roof-quote.html`)*

Homeowner types their address → satellite view of *their actual roof* → live measurements (sq ft, squares, pitch, complexity) → instant estimate range → claims their "full roof report" by leaving name + phone → AI receptionist books the inspection.

**Why it converts:** nobody else in the DMV offers this. It removes the #1 friction ("I don't want a salesman in my house just to get a price"), it's a pattern-interrupt ("whoa, that's my roof"), and it pre-frames the value conversation before a rep ever shows up.

**Status:** production file built. Runs in **demo mode** today (realistic sample data — show ownership immediately); paste one Google API key (Geocoding + Solar + Static Maps enabled) and a webhook URL into the CONFIG block to go fully live. Estimate math is configurable (`PRICE_PER_SQ`, currently $475–675/sq DMV asphalt installed, 10% waste).

**Use it everywhere:** site nav + hero, QR code on door hangers and yard signs, link in every ad ("See your roof from space"), rep follow-up texts, GBP posts.

---

## 3. Weapon 2 — Outbound: Speculative Roof Reports (the Marlow play, roofing edition)

The viral play from your bookmark: a 19-year-old screenshots businesses off Google Maps, builds the deliverable *before asking*, texts it to the owner — 41% hit rate, because the prospect is looking at *their own thing already improved*. Translate to roofing:

**The play, step by step:**
1. **Target selection.** Storm hits a ZIP (weather trigger from the demand engine) → pull the affected streets. Prioritize roofs 12+ years old (county assessor data / visual age from imagery) in owner-occupied homes.
2. **Auto-generate a personalized Roof Report per address:** satellite image of THEIR roof, measured sq ft + squares, storm event date + hail size that hit their street, estimate range, and the insurance math ("with an approved claim, your cost ≈ your deductible").
3. **Deliver it** as a personalized link (udroofing.com/r/123-main-st) via:
   - **Door hanger / postcard with QR** → their own roof on the card (legal everywhere, feels like magic)
   - **Door knock opener**: rep opens with the printed report — "I'm not here to inspect, we already measured your roof from above. Here's what we found."
   - **Text/email** where we have consent or prior relationship (past leads, past customers, referral neighbors)
4. **CTA:** "Claim your free on-site verification" → AI receptionist books it.

**Why this 100x's door-to-door:** the rep no longer knocks cold — every door already has a personalized artifact. Close-rate physics change exactly like the Marlow play: you're not pitching, you're handing them something that's already theirs.

**Compliance guardrails (non-negotiable):**
- Cold SMS/email to purchased lists = TCPA/CAN-SPAM risk. Default to **print + door + QR** for strangers; text/email only with consent or existing relationship.
- Estimates are clearly labeled preliminary; no fabricated damage claims — the report shows measurements and *possible* storm exposure, the inspection verifies.
- Honor no-soliciting signs (UD already has one Yelp complaint about this — the report-in-hand approach should *reduce* friction, not add pressure).

---

## 4. The factory (how reports get made at scale)

```
Storm trigger (ZIP)  ──►  Address list (assessor/owner data)
        │
        ▼
For each address:
  Geocode → Solar API (roof geometry) → Static Map image
  → estimate calc → render report page (template)
  → generate QR → batch print file (door hangers/postcards)
        │
        ▼
Routes pushed to reps' phones · AI receptionist standing by
· every scan/claim tracked per street
```

Build effort: the report page is a variant of `roof-quote.html` with pre-filled data; a small script (Make/n8n or custom) runs the per-address pipeline. **Cost per personalized report: under $0.15.** Compare to $300–600 blended cost per storm lead from ads.

---

## 5. KPIs for the satellite system
- Tool: address scans → report claims (target 25–40%) → booked inspections → closed jobs
- Outbound: reports delivered → QR scans (target 8–15%) → claims → inspections → closed
- Cost per booked inspection vs. paid channels (this should be the cheapest channel in the stack)
- Rep feedback: door conversations started with report-in-hand vs. cold

---

## 6. Positioning for the pitch to ownership
One line: **"Every competitor knocks doors blind. Our reps walk every storm street already holding each home's roof measurements and estimate — and homeowners can scan their own roof from our website 24/7."**

That's a capability no roofing company in the DMV is showing. It feeds the brand (innovative, transparent, no-pressure), the funnel (cheap qualified leads), and recruiting ("we give reps superpowers, not just a clipboard").
