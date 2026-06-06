# UD Dashboards — Security & Production Architecture
### How the staff dashboard and client portal go from preview → bank-grade

**Status:** The UIs (`index.html` staff command, `portal.html` client portal) are production-designed previews with sample data. A static page cannot be "secure" — security lives in the backend. This document specifies exactly how we ship it properly. No security theater.

---

## 1. Architecture (recommended: Supabase + Cloudflare)

```
Browser ── Cloudflare (WAF, rate-limit, bot-fight, TLS) ── Static UI (Pages)
                     │
                     └── Supabase  ── Auth (SSO/MFA, magic links)
                                   ── Postgres + ROW-LEVEL SECURITY
                                   ── Storage (photos/docs, signed URLs)
                                   ── Edge functions (webhooks from AI agents/CRM)
```

Why this stack: real auth + row-level security without running servers; Cloudflare absorbs DDoS/bots; total cost ≈ $0–50/mo at UD's scale.

## 2. Identity & access
- **Staff:** email+password with mandatory **MFA (TOTP)**; roles `owner / manager / rep / production` enforced in Postgres RLS — a rep literally cannot query another rep's leads, even with the API key, because the database refuses.
- **Clients:** passwordless **magic-link** (or SMS OTP) scoped to their single project. Links expire in 15 min; sessions in 24h. A homeowner can never enumerate other projects — RLS again.
- Admin actions (exports, deletes, role changes) logged to an append-only `audit_log` table.

## 3. Hardening checklist (the "latest hacks" coverage)
| Threat | Defense |
|---|---|
| Credential stuffing / brute force | Cloudflare rate-limiting + Supabase auth throttling + MFA |
| Prompt-injection → AI agents leaking data | AI agents get **scoped service tokens** (read-only views, no PII dumps); agent outputs to clients pass a template, never raw DB |
| XSS | Strict **CSP** (`default-src 'self'`; no inline script in prod build), all user content rendered as text, never `innerHTML` |
| SQL injection | No raw SQL from client — Supabase client + RLS; edge functions use parameterized queries |
| Session theft | `Secure; HttpOnly; SameSite=Strict` cookies, short JWT TTL + refresh rotation |
| CSRF | SameSite cookies + origin checks on edge functions |
| Scraping / bots | Cloudflare bot-fight + Turnstile on auth pages (invisible, no CAPTCHAs for humans) |
| Subdomain takeover / DNS | DNSSEC on; CAA records pinning the cert issuer |
| Secrets leakage | **Zero secrets in the repo** (this repo is public) — keys live in Supabase/Cloudflare env vars only; webhook URLs proxied through an edge function |
| Data at rest | Postgres + Storage encrypted at rest (AES-256, Supabase default); signed URLs expire in 10 min |
| Backups / ransomware | Daily encrypted snapshots, 30-day retention, restore drill quarterly |

**Security headers to ship:** `Content-Security-Policy`, `Strict-Transport-Security (preload)`, `X-Content-Type-Options: nosniff`, `X-Frame-Options: DENY`, `Referrer-Policy: strict-origin-when-cross-origin`, `Permissions-Policy` (camera/mic/geo off).

## 4. Privacy & compliance
- Collect the minimum: name, contact, address, claim metadata. No SSNs, no payment cards stored (payments via processor links only — never build card storage).
- Plain-English privacy policy (already live at `/privacy.html`), SMS opt-out honored automatically, deletion requests honored within 30 days via a single admin action.
- Per-role data visibility matrix documented before launch; reps see only their territory.

## 5. Data model (core tables)
`leads` · `projects` (one per job; client portal key) · `claims` (carrier, stage, checks) ·
`documents` (storage refs + signed URL policy) · `messages` (project-scoped thread) ·
`reps` (ramp stage, scorecards from Agent 3) · `events` (storm triggers, agent activity) · `audit_log`.

## 6. Build plan (5 working days once access lands)
1. **Day 1:** Supabase project + schema + RLS policies; Cloudflare in front of the domain.
2. **Day 2:** Auth flows (staff MFA, client magic links); wire the two UIs to live queries.
3. **Day 3:** Edge functions: lead webhook (site forms + AI receptionist → `leads`), document upload, message thread.
4. **Day 4:** Security headers, CSP, Turnstile, audit log, backups; pen-test pass with OWASP ZAP baseline scan.
5. **Day 5:** Role seeding, owner walkthrough, go-live on `app.udroofing.com` + `my.udroofing.com`.

**What I need to start:** a Supabase org (free), Cloudflare access for the domain, and the go-ahead. Until then the previews demo the full experience safely with sample data and are marked as such.
