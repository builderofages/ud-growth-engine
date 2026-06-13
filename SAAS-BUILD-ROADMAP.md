# UD "Top-Tier SaaS" — Architecture, Truths, and Build Roadmap
**June 12, 2026 · second-pass audit covering the full ops folder, not just the website**

## 0. The satellite truth (read before Shah repeats it to anyone)
**No satellite can see hail damage.** Best commercial imagery is ~30 cm/pixel; hail bruises are 1–3 cm. Anyone selling "AI satellite damage detection" for residential hail is selling radar overlays with better marketing. What IS real, and what we now have:

| Claim | Reality | UD's tool |
|---|---|---|
| "See damage from space" | ❌ Physically impossible | — |
| Storm exposure per address (radar/NWS-verified) | ✅ Free, legal, court-grade citation | **Command Center → Address Intel** (live NOAA/NWS, built today) |
| Roof measurement from above (area, pitch, segments) | ✅ Google Solar API, pennies | report-factory + roof-quote.html + Command Center (key-gated) |
| Insurance-grade measurement report | ✅ EagleView/Hover/Roofr, $15–60 | Buy per-deal at contract stage only |
| Damage *verification* | ✅ On the roof, with photos | Claim Packet generator (checklist baked in) |

This combination — verified exposure + measured roof + documented on-site findings — closes claims *better* than fake satellite promises, and survives an adjuster's scrutiny.

## 1. What was built today: `website/admin/command-center.html`
One internal file, zero backend required, works offline, on-brand:
- **Pipeline** — 7-stage kanban (Lead → Inspection → Claim Filed → Adjuster/Approved → Contract → Install → Paid) with per-job carrier/claim#/deductible, hot-lead flags, KPIs (pipeline value, close rate), JSON backup/restore, CSV export.
- **Address Intel** — type any address → geocoded → checked against 120 days of live NWS storm reports within 15 miles → HIGH/MEDIUM/LOW/NONE claim-probability verdict → satellite + street view links → one click adds it to the pipeline as a (hot) lead. With the Google key in config.js it also auto-measures the roof (Solar API) and pre-fills the quote.
- **Quote Builder** — squares × tier (HDZ/UHDZ/metal/TPO) × steepness + gutters → printable branded estimate with the compliant insurance language.
- **Claim Packet** — carrier-ready documentation packet: NWS citation auto-filled from Intel, photo checklist, compliance guardrails embedded so reps physically can't generate a non-compliant packet.

Storage is localStorage (per-browser). That's deliberate: it ships today. The upgrade path to multi-user cloud is §3.

## 2. Buy vs. build — the call that saves you a year
A $10M roofing company's system of record should be **bought, not built**: AccuLynx or JobNimbus (~$100–300/user-group/mo) gives multi-user CRM, production scheduling, material ordering, Xactimate integration, and mobile apps that 50 competitors already battle-tested. Building that from scratch is a 12-month, $200K+ trap that produces a worse product.

**Build only what can't be bought (UD's actual edge):**
1. Address Intel / storm-verification engine (built today — nobody sells this)
2. Speculative report factory (built — `tools/report-factory`)
3. The public site + instant satellite quote funnel (built)
4. AI receptionist/voice + claim-packet automation (half-built: ElevenLabs agents exist)

The Command Center is the bridge: use it now, keep it as the intel layer after the CRM lands, push leads in via `CRM_WEBHOOK` (already wired in config.js).

## 3. Phased path to "real SaaS" (if we still want it after the CRM)
- **Phase A (now, $0):** Command Center on localStorage. Single-user per browser. Weekly JSON backups.
- **Phase B (1–2 days, $0–25/mo):** Supabase free tier — auth (email magic-link per rep), Postgres tables (jobs, touches, intel_runs), row-level security. Swap the `CC.save/load` functions for Supabase calls (~80 lines). Now it's multi-user with login — front + back + admin, genuinely.
- **Phase C (1 week):** rep mobile flow (same file, responsive — photo upload to Supabase storage from the roof), manager dashboards, lead auto-ingest (FormSubmit → email parser or direct webhook), Notion CRM sync retired.
- **Phase D (only if UD becomes the platform for a roll-up, per the $100M roadmap):** multi-tenant version — each acquired company gets a brand skin on the same engine. *That's* when custom SaaS earns its keep.

## 4. Full ops-folder audit (what exists vs. what's missing)
**Exists and is good:** Master Growth Plan ($10M→$20M model is sound — the levers are missed-call capture, close-rate training, +50% leads, 15–20 reps); Satellite/Speculative playbook (correctly two-tiered, compliant); report-factory (works, demo mode, needs Google key); Sales-Rep-Playbook + training deck + flashcards + field kit (hiring/ramp content exists); Database-Reactivation-Kit; AI-Agent pack (5 agents specced); n8n storm-trigger workflow; JUNE-MONEY-PLAN; Notion CRM; dashboards.

**Was missing — closed today:** back office (Command Center), storm-verified address intel, quote builder, claim packet generator, canvass pack for the live storms, commercial outreach drafts, cloud article engine, Pages deploy fix.

**Still missing (the honest list, in priority order):**
1. **Phone answering nights/weekends** — ElevenLabs voice agent on a Twilio number, or a service. The 24-hr promise is unstaffed. Highest-leverage gap in the entire system.
2. **CRM decision + lead webhook live** (AccuLynx vs JobNimbus — pick in one demo call each; wire `CRM_WEBHOOK`).
3. **Hiring engine running** — the playbook exists but no active funnel: post the rep role on Indeed this week (comp: commission 8–10% of contract or 40–50% of profit split, $50–150K OTE realistic in storm), interview kit from the training deck, 2-week ramp via the academy. Without 4+ reps the leads being generated have nowhere to go — *they have a sales team; this is how it doubles.*
4. **Xactimate/supplement capability** — contract a supplement desk (they take 7–15% of recovered supplements; pure margin until in-house).
5. **GBP + LSA activation** (Shah's accounts — still the #1 inbound channel for roofing).
6. **Review velocity habit** — tool exists; make it a closing-table step.
7. **The 7+5 activation items** from the audit (domain, LEAD_EMAIL+FormSubmit verify, GA4, repo org, disk space, etc.).

## 5. This week's order of operations
1. Deploy today's files to the repo (4 workflow/engine files + admin/command-center.html + canvass/outreach docs are local-only until pushed).
2. Knock the June 11 wind zones + Gainesville hail (canvass pack) — leads exist *today*.
3. Send the 6 commercial drafts after putting real recipients in.
4. Shah: domain, GBP, LSA, FormSubmit re-verify, repo Settings → Pages → "GitHub Actions", add ANTHROPIC_API_KEY secret.
5. Post the sales-rep job ad; book AccuLynx + JobNimbus demos.
6. Stand up the ElevenLabs phone line.
