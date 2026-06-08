# United Developers — Growth Engine Handover & Turn-Key Guide

This document makes the entire system transferable. Anyone who reads it can launch it, re-point it to a different inbox, clone it to another account, or hand the whole thing to United Developers as a clean turn-key asset. Nothing here requires a developer.

---

## 1. What this system is

A complete, self-contained marketing + operations stack for United Developers (UD Roofing). Everything is static HTML/JS/CSS — no servers to maintain, no database required to run, hosted free on GitHub Pages.

**Public website** (`/website/`)
Homepage funnel, financing, referral ($250), instant satellite roof quote, careers + applicant screener, projects, 6 deep service pages, 6 city/area pages, about, contact, FAQ, privacy, terms. Riley (AI receptionist) and Dex (AI sales) chat on every page.

**Owner & staff tools** (`/dashboard/`)
- `owner-roi.html` — Shah types his real numbers, sees conservative cited dollar value of each system.
- `storm-radar.html` — live National Weather Service alerts scored into a canvass strike list.
- `index.html` — staff dashboard hub.

**Field tools** (`/training/`)
- `field-kit.html` — mobile rep tool: commission calc, live storm zones, door script, objections, roof measure, lead logging.

**AI layer** (`/ai-agents/`)
- `UD-Knowledge-Base.md` — the veteran knowledge base powering the chat/voice agents.

**Growth playbook** (`/growth/`)
- `JUNE-MONEY-PLAN.md` — storm-strike, reactivation, and commercial plan.

**The one file that wires it all** — `/website/config.js`.

---

## 2. The single switch: reassign every lead in one edit

Every form, chat capture, application, referral, satellite quote, and field lead on the entire site routes through **one value**. To send all leads to a different inbox, edit one line in `/website/config.js`:

```js
LEAD_EMAIL: "trainyouragent@gmail.com",   // ← change to office@udroofing.com (or anything)
```

Save, commit, done. The whole site re-points instantly. No other file needs touching.

> First time an inbox is used, FormSubmit sends a one-time activation email to that address. Click the link once and delivery is live forever. So when you switch `LEAD_EMAIL` to `office@udroofing.com`, the first test lead triggers an activation email UD must click once.

**Keep the automated Notion pipeline fed after the switch.** The lead-sync automation reads a *connected* Gmail inbox. When you move `LEAD_EMAIL` to the company inbox, also set `LEAD_CC: "trainyouragent@gmail.com"` (the connected inbox) so every lead still lands there and keeps auto-filing into Notion. Two lines total — `LEAD_EMAIL` and `LEAD_CC` — and the whole pipeline keeps running. (Alternatively, connect the company Gmail as the source inbox and point the automation at it.)

If UD uses a CRM (GoHighLevel, JobNimbus, ServiceTitan, Zapier), paste its inbound webhook into `CRM_WEBHOOK` in the same file and every lead also flows straight into the CRM — automatically, with zero per-form wiring.

---

## 3. Launch checklist — paste-and-go

Open `/website/config.js`. Fill in what you have; leave the rest as `""` (each integration stays dormant until its value is set). This is the entire launch surface:

| Field | What to paste | Where to get it |
|---|---|---|
| `LEAD_EMAIL` | The inbox leads go to | UD's email |
| `CRM_WEBHOOK` | CRM inbound webhook URL | UD's CRM (optional) |
| `SMS_WEBHOOK` | Instant-SMS auto-reply webhook | Zapier/Twilio (optional) |
| `GA4_ID` | `G-XXXXXXX` | Google Analytics |
| `GTM_ID` | `GTM-XXXXXXX` | Google Tag Manager (optional) |
| `META_PIXEL_ID` | Pixel ID | Meta Ads Manager |
| `GOOGLE_ADS_ID` + `GOOGLE_ADS_LEAD_LABEL` | Conversion tag + label | Google Ads |
| `GOOGLE_MAPS_KEY` | Maps/Solar/Geocoding key | Google Cloud Console (upgrades the satellite tool from free Esri to Google imagery) |
| `TRACKING_PHONE` | Call-tracking number | CallRail/etc (optional) |
| `LENDER_URL` | Financing application link | Service Finance/GreenSky/Hearth |
| `BOOKING_URL` | Calendly/Acuity link | UD's scheduler (optional) |

The two AI agent IDs (`AGENT_RILEY`, `AGENT_DEX`) are already filled in. Analytics, pixels, and tag manager auto-inject themselves the moment their ID is present — no code edits.

---

## 4. Clone it (duplicate the whole system)

To stand up an identical copy under any GitHub account:

1. Sign in to GitHub.
2. Create a new empty repository (e.g. `ud-site`).
3. Upload the contents of this `UnitedDevelopers/` folder (drag-and-drop in the GitHub web "Add file → Upload files" screen — no command line needed).
4. Repo → **Settings → Pages** → Source: `main` branch, `/ (root)` → Save.
5. The site goes live at `https://<account>.github.io/<repo>/website/` within a minute.

That's a full working clone. Edit `config.js` on the clone to point it at whatever inbox/keys you want.

---

## 5. Go live on udroofing.com (custom domain)

1. In the repo: **Settings → Pages → Custom domain** → enter `udroofing.com` → Save. This creates a `CNAME` file.
2. At UD's domain registrar (wherever udroofing.com is managed), add DNS records:
   - Four `A` records for the apex `@` → `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
   - One `CNAME` for `www` → `<account>.github.io`
3. Back in Settings → Pages, tick **Enforce HTTPS** once the certificate provisions (a few minutes to a few hours).

The second domain (`uniteddevelopersmdva.com`) can `CNAME`/redirect to the same place.

---

## 6. Transfer the AI agents

The chat/voice agents (Riley, Dex) live in an ElevenLabs account. To hand them over:

- **Simplest:** keep them in the current account and leave the agent IDs in `config.js` as-is — they keep working regardless of who owns the website.
- **Full transfer:** recreate the two agents inside UD's own ElevenLabs account (paste the system prompt from `/ai-agents/UD-Knowledge-Base.md`), then swap the new `AGENT_RILEY` / `AGENT_DEX` IDs into `config.js`. Assign Riley a phone number in ElevenLabs to enable the inbound voice receptionist.

---

## 7. Full ownership handover to United Developers

When you're ready to hand Shah the keys completely, do these in order:

1. **Email** — set `LEAD_EMAIL` to UD's inbox and have them click the one FormSubmit activation link. All leads now go to UD.
2. **Repository** — GitHub → repo **Settings → General → Transfer ownership** to UD's GitHub account, *or* have them follow §4 to clone it into their own account.
3. **Domain** — UD keeps control of their registrar; just confirm the DNS records in §5 point at the live repo.
4. **Analytics/ads** — replace the `GA4_ID`, `META_PIXEL_ID`, `GOOGLE_ADS_ID` values with UD's own accounts so reporting lives in their dashboards.
5. **AI agents** — either leave running as-is or transfer per §6.
6. **CRM** — paste UD's `CRM_WEBHOOK` so leads land in their system of record.

After step 1 and 2, the business is operationally theirs. Steps 3–6 move the remaining accounts into their name.

---

## 8. Where things live (map)

```
UnitedDevelopers/
├─ HANDOVER.md            ← this file
├─ website/
│  ├─ config.js           ← THE switchboard (edit this to launch / reassign)
│  ├─ index.html          ← homepage funnel
│  ├─ roof-quote.html     ← satellite instant quote
│  ├─ financing.html  referral.html  careers.html
│  ├─ about.html  contact.html  faq.html  projects.html
│  ├─ privacy.html  terms.html
│  ├─ ud-chat.js  ud.css  assets/
│  ├─ services/  (6 pages)
│  └─ areas/      (6 city pages)
├─ dashboard/
│  ├─ index.html  owner-roi.html  storm-radar.html
├─ training/
│  └─ field-kit.html
├─ ai-agents/
│  └─ UD-Knowledge-Base.md
└─ growth/
   └─ JUNE-MONEY-PLAN.md
```

---

## 9. One-line summary for Shah

> "Everything that runs the marketing and intake — the site, the AI receptionist, the lead routing, the owner ROI model, the field tools — is one folder you fully own. To make every lead come to your inbox, change one line in `config.js`. To take it over completely, transfer the GitHub repo. That's it."

*Financing terms, license numbers, and the legal pages are drafts pending UD's attorney review before public launch.*
