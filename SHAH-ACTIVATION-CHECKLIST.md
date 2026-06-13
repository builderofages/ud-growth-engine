# United Developers — Go-Live Checklist for Shah

> **UPDATED June 12, 2026 — read the addendum at the bottom.** Audit found 4 new items (one prevents lost leads on launch day) and storms on June 11–12 created live canvassing zones — see `growth/CANVASS-TODAY-2026-06-12-BRIEF.md`.

**What this is:** The website and lead system are built, live, and tested. Six things need to come from you to flip it from a working demo into a machine that puts real leads in your team's hands. None of these require any technical skill — just sending a few pieces of info. Most take 5 minutes each.

**What you do NOT need to worry about:** Your email, your current website, and your phone keep working exactly as they do today. Nothing here touches or risks your existing email. We launch on a separate web address first and only point your real domain over once you've seen it working.

---

## The 6 items (in priority order)

### 1. Where should leads go? (most important — 5 min)
Right now every lead from the site lands in a test inbox we control. Give us the email address where your sales team wants new leads delivered (for example `office@udroofing.com` or a dedicated `leads@` address). We change one line and every form, every quote, and the AI receptionist start delivering there instantly.
- **What to send:** the destination email address (and a cell number if you want lead texts too — see #4).

### 2. Google tracking & ad pixels (10 min — unlocks ads & measurement)
Without these you can't see where leads come from or run retargeting ads. If you already run Google or Facebook ads, you have these. If not, we'll help you create them free.
- **What to send:** Google Analytics ID (starts with `G-`), Google Ads ID (`AW-`), and Meta/Facebook Pixel ID. If you don't have them, just say so and we'll set them up.

### 3. Google Maps key (10 min — makes the roof tool pinpoint-accurate)
The instant satellite roof-measuring tool already works. A free Google Maps key upgrades it from "very good" to "exact rooftop" precision, which makes quotes tighter and demos more impressive.
- **What to send:** a Google Maps Platform API key (free tier covers normal volume; we'll send you the exact 4-click steps to create one).

### 4. Instant text-back for leads (optional but high-impact)
Speed kills in roofing — texting a lead within 60 seconds dramatically increases booked inspections. We can auto-text every new lead. Needs a sending number (Twilio or similar — cheap).
- **What to send:** say "yes" and we'll set up a number, or provide your texting service login.

### 5. The web address / domain (the actual launch — your call on timing)
The site is live now at a temporary address. When you're ready, we point your domain (or a subdomain like `new.udroofing.com`) at it.
- **Important & safe:** We will **never touch your email (MX) records.** Your email keeps working. We either use a subdomain or set up redirects so your current Google rankings carry over and nothing breaks.
- **What to send:** your domain registrar login (GoDaddy, Namecheap, etc.) **or** add us as a delegate — we'll handle it and walk you through approving it.

### 6. Google Business Profile access (where most roofing leads actually come from)
Your Google listing (reviews, the map pack) drives more local roofing calls than anything else. Access lets us keep it optimized and funnel reviews.
- **What to send:** add our email as a manager on your Google Business Profile, or share the login.

---

## What's already done and working (so you know what you're getting)
- Full English website — homepage, every service, 15 city pages, 8 homeowner guides, financing + payment calculator, commercial/property-manager page, instant satellite roof quote, about/FAQ/contact/careers.
- **Spanish bilingual funnel** — Spanish landing page, financing page, and insurance-claim guide that feed the same lead system. English-primary; Spanish visitors get a native-language path.
- Live lead delivery (tested — leads arrive by email instantly), AI chat/voice receptionist ("Riley"), SEO + AI-search optimization so ChatGPT/Google can find and cite the business.
- One central settings file means all six items above are single-line switches — no rebuild, no developer needed.

## Fastest path to a ringing phone
Send items **#1 (lead inbox)** and **#5 (domain)** first. Those two alone take the site from "demo" to "live and capturing real customers." The rest make it stronger, but those two make it real.

---

## ADDENDUM — June 12, 2026 audit (4 new items + storm alert)

**⛈ STORM ALERT (act first):** June 11–12 storms produced 1" hail in Bristow/Woolsey (Prince William, ~4:40pm June 12), 74 mph at Andrews AFB / 70 mph PG County, 67 mph at Dulles, 60+ mph Arlington/DC. These are live, claim-grade canvassing zones for the next 5–10 days. Walk-lists with map links: `growth/CANVASS-TODAY-2026-06-12-BRIEF.md`. Send reps before competitors saturate.

**A. (CRITICAL — pairs with item #1)** When the lead email changes, the form service (FormSubmit) sends a one-time **activation link to the NEW inbox**. Until someone clicks it, forms silently fail. Launch-day order: change the email → submit a test form → open the new inbox → click the activation link → submit a second test → confirm it arrives. 5 minutes, prevents silent lead loss.

**B. Repo Settings → Pages → Source: "GitHub Actions"** (one click, already coded). Fixes a structural issue where every page would 404 after the domain connects. Do this BEFORE item #5.

**C. Repo Settings → Secrets → add `ANTHROPIC_API_KEY`** — turns on the cloud content engine (3 SEO articles/week publish themselves, no laptop needed).

**D. Add Shah (or a company account) as repo admin** — the whole site currently lives under one personal GitHub account; that's a single point of failure.

**New internal tool (live now):** `…/website/admin/command-center.html` — sales pipeline board, address storm-intel (type any address → verified storm-hit verdict reps can cite at the door), instant quote builder, and insurance claim-packet generator. Bookmark it; it's the team's back office until the CRM is chosen.

**Also verify:** D.C. contractor license (site currently advertises D.C. service; licenses listed are MD/VA/PA only — either license it or we pull the D.C. claims).
