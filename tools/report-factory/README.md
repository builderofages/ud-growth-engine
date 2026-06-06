# Report Factory — Speculative Roof Reports at Scale

Storm hits a ZIP → run one command → every address gets a personalized roof report page, a rep route sheet, and print-ready door cards with QR codes.

## Run it
```bash
python3 factory.py addresses.csv "2026-06-02 hail event, Gaithersburg"
```

**Input:** `addresses.csv` — one address per line (optional `,owner_name`).

**Output (`output/`):**
- `reports/<address>.html` — personalized homeowner report (their roof, measurements, estimate range, insurance math, call CTA)
- `index.html` — rep route sheet: every address, measurements, estimate, report link, knock-status checkboxes
- `print-batch.html` — door-hanger cards, 4-per-page, QR per home → print and walk the street

## Live vs demo
- `GOOGLE_API_KEY = ""` (top of factory.py) → **demo mode**: realistic deterministic measurements, works offline. Use for showing the workflow today.
- Paste a Google Cloud key (Geocoding + Solar API + Static Maps enabled) → **live mode**: real roof measurements + real satellite image per address. ~$0.10/address.

## Config (top of factory.py)
`BASE_REPORT_URL` — where reports get hosted (QR codes point here) · `PRICE_PER_SQ` — estimate range per square · `WASTE` — waste factor.

## Workflow per storm
1. Demand engine flags storm ZIP → pull street list (assessor/owner data).
2. Run factory → upload `reports/` to udroofing.com/r/ → print `print-batch.html`.
3. Reps walk the route sheet, report in hand. AI receptionist catches every call/scan.
4. Track: scans → claims → booked inspections per street in the weekly scoreboard.

**Compliance:** print + door + QR for cold homes (no TCPA risk). Text/email only with consent or existing relationship. Estimates labeled preliminary. No fabricated damage — the report shows measurements; the inspection verifies.
