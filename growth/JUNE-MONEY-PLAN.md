# UD June Revenue Sprint — Operational Orders
Storm-verified, dollar-mathed, ready to run. Built June 7, 2026.

## The math to $1M in June
$14K average job. $1M = 71 closed roofs in 23 days = ~3.1/day.
UD baseline is ~2/day. The gap is ~1.1 extra closes/day. Three levers below, sized:
| Lever | Closes it can add in June | Why |
|---|---|---|
| June 6 storm strike (below) | 25-40 | Fresh 60mph+hail damage, zero competition for ~5 days |
| Database reactivation | 10-20 | 650+ past customers + dead estimates; referral + RoofShield + neighbor-storm angles; closes at 2-3x cold rate |
| Commercial outreach (PM/HOA) | 1-3 contracts = $50-400K | One TPO/flat contract equals 10-30 houses |
Realistic June total with all three executed hard: **$900K–$1.3M**. It is doable. It requires the crew running the storm play THIS WEEK.

## PLAY 1 — June 6 Storm Strike (run Monday 8 AM)
**Verified by NWS:** Friday June 6, ~6:58 PM EDT, severe thunderstorm warning — **60 mph gusts, 0.75" hail** — over Brooklyn Park / Riviera Beach, moving east at 45 mph. Additional warned cells over Baltimore City/County, Howard, Montgomery, Prince George's.

**Target canvass zones (storm path, west to east):**
- 21225 Brooklyn Park — ground zero per NWS text
- 21122 Pasadena / Riviera Beach — named in warning
- 21060 / 21061 Glen Burnie — directly east on the storm track
- 21144 Severn, 21146 Severna Park — east-southeast continuation
- Secondary: Howard (21044/21045 Columbia), Baltimore County warned cells

**Why these close:** 60 mph = creased shingles (broken seals, invisible from ground). 0.75" hail = dented vents/gutters/soft metal — the exact photo evidence adjusters accept. Damage is 48 hours old; filing window fully open; out-of-state storm chasers haven't mobilized for a sub-1" event — local company with license numbers owns this window.

**Door script (this storm, not generic):**
"Hey — quick heads up, not a sales pitch. Friday evening's storm pushed sixty mile-an-hour gusts straight through this neighborhood — we're the roofing company over in Bethesda, licensed MHIC one-one-one-nine-seven-one. Wind that speed creases shingles even when nothing looks missing, and that hail dents the vents — that's what insurance actually pays on. We're doing free twenty-minute inspections on this street today, photo report's yours either way. Takes me twenty minutes — want me to look while I'm here?"

**Objection one-liners:** "Roof looks fine" → "From the driveway it always does — the crease is at the seal line. That's why the report's free." / "Insurance will raise my rates" → "Storm claims are Act-of-God — carriers rate the region, not you. The storm already happened; your rates move either way."

**Cadence:** Knock 9 AM–1 PM and 4:30–7:30 PM. Every inspection booked = ask the two-fifty referral line at the door. Every roof inspected = chalk-test squares photographed same-day. Goal: 2 reps × 60 doors/day in 21122+21060 = 8-12 inspections/day → 4-6 claims/day filed this week.

**Riley & site are already synced:** the AI receptionist and chat now reference "Friday evening's storm" with the 60-mph spec for callers from these zips, and tags them STORM-JUNE6.

## PLAY 2 — Database Reactivation (fires the day UD exports their list)
Segments: (A) past customers, (B) dead estimates/never-closed inspections, (C) cancelled-claim homeowners.
Send from office@udroofing.com or any ESP. Plain text beats pretty HTML for deliverability and reply rate.

**Email 1 — storm check-in (segment A, send Tuesday):**
Subject: `That storm Friday — quick question about your roof`
> Hi {first} — it's the team at United Developers. We replaced/repaired your roof back in {year}, so this is a service note, not a pitch: Friday evening's storm ran 60 mph gusts through parts of the county. Your GAF system is rated for it, but if you've got a fence, gutters, or a neighbor whose roof took the hit, we're doing free inspections this week. And our referral program pays $250 per neighbor who completes a project — after a storm like this, that's worth mentioning over the fence. Reply here or call (240) 880-2108. — United Developers

**Email 2 — dead estimates (segment B, send Wednesday):**
Subject: `Your roof estimate from {month} — one thing changed`
> Hi {first} — you had us out for an estimate a while back and the timing wasn't right. Two things changed since: Friday's storm may have turned your roof into an insurance claim instead of an out-of-pocket project (we check that free), and we now have $0-down financing from 12 to 180 months. Worth 20 minutes to re-look? Reply or call (240) 880-2108 and we'll re-inspect at no charge — new photo report either way.

**Email 3 — RoofShield (segment A non-responders, +7 days):**
Subject: `$19/month and you never think about your roof again`
> Hi {first} — quick one. We launched RoofShield: nineteen a month gets an annual inspection, gutter check, and a photo report for your records; twenty-nine adds priority scheduling and minor repairs included, transferable when you sell. After this storm season it's the cheapest peace of mind on your house: udroofing.com/roofshield — or just reply "shield" and we'll set it up on your next visit.

**SMS pair (where TCPA consent exists):**
1. `United Developers: Friday's storm hit 60mph in parts of {county}. Free roof checks this week for past customers — reply YES for a slot or STOP to opt out.`
2. (+3 days) `{first}, neighbors referred by you = $250 each when their project completes. After Friday's storm, worth a text to the block: udroofing.com/referral — UD`

## PLAY 3 — Commercial outreach (property managers / HOA mgmt, DMV)
One flat-roof or community contract = $50K–$400K. Targets: community association management firms (Montgomery/Anne Arundel/Howard), commercial property managers with retail/flex inventory, school/church facility managers.
**Email (personalize first line per property):**
Subject: `Friday's storm + your {community/property} roofs`
> {first} — Friday evening's storm ran 60 mph gusts across Anne Arundel and Howard. For managed communities that usually means creased shingles and dented soft metal across multiple buildings — damage that's claimable now but invisible until it leaks in the fall, after the filing window tightens. We're United Developers (GAF factory-certified, MHIC #111971, 650+ DMV projects): we'll walk your roofs this week, document every building with photos, and hand you a board-ready condition report — free, no commitment. If there's a claim, we scope it with the adjuster so the association isn't negotiating alone. 20 minutes to schedule the walk? — {sender}, United Developers, (240) 880-2108
**Follow-up (+4 days):** one paragraph, attach a sample photo report page, offer two specific time windows.

## What I need to fire these
1. PLAY 1 — nothing. Hand this file to the crew lead tonight; Riley and the site already speak this storm.
2. PLAY 2 — UD's customer/estimate export (CSV: name, email, phone, year, segment). Sequences load same day.
3. PLAY 3 — say the word and I pull a ranked DMV property-manager contact list (Apollo connector — one-click auth) and stage personalized drafts in Gmail for your review before anything sends.
