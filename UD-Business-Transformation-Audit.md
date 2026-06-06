# UD Business Transformation Audit
### Every function of the company, the gap, the change, and what it's worth
*TrainYourAgent · The operations half of the $20M plan — demand systems are built; this is everything else.*

A roofing company doubles on four engines: **demand** (built ✅), **conversion** (built ✅), **throughput** (below), and **cash** (below). This audit walks every remaining function the way a buyer or a CFO would.

---

## 1. Production & Throughput — the real $20M governor
**Typical pain at $10M:** scheduling in someone's head + a whiteboard; crews idle between jobs; materials arrive late; sold backlog sits 3–6 weeks; one complaint UD already has publicly is slow follow-through.
**The change:**
- Install board (in Staff Command, backed by the same Supabase): every signed job → materials ordered → delivery date → crew slot → install → final inspection, with aging alarms at each stage.
- Rule: **no job sits >10 days between sign and install date assigned.** Aging jobs page the owner automatically.
- Crew capacity model: jobs/week per crew × crews = ceiling. At ~2 installs/crew/week, $20M ≈ 28 installs/wk ≈ **14–15 crews** (vs ~5 today). Subcontractor bench must be recruited *like sales reps* — same hiring funnel, crew edition.
**Worth:** this is the difference between booking $20M and *installing* $20M. Backlog cut from weeks to days also collapses cancellations (every idle week loses ~2–5% of signed jobs).

## 2. Job Costing — most roofers don't know their real margin
**Typical pain:** owner knows revenue, guesses margin. Material overruns, change orders, and crew overpayments eat 3–8 points silently.
**The change:** per-job P&L in the dashboard: contract value − materials (actual invoice) − labor (crew rate) − supplement adjustments = gross margin per job, per crew, per rep, per shingle line. Weekly outlier review: every job under 35% GM gets a why.
**Worth:** recovering 3 points of margin on $14M = **+$420K/yr profit** with zero new sales.

## 3. Cash & Collections — the ACV/RCV chase
**Typical pain:** second checks (RCV/depreciation) drift 30–90 days; supplements go unfiled; deductibles uncollected. At $10M, $300–800K is routinely floating.
**The change:**
- RCV tracker: every job past install with depreciation outstanding → automated homeowner + carrier follow-up cadence (Agent 5 drafts, human sends).
- Supplement discipline: checklist per claim (drip edge, ice & water, code items) — supplements average **8–15% of claim value**; unfiled = donated to the carrier.
- Deductible collected at contract, not closeout. Card/ACH link in the client portal.
**Worth:** on 1,000 claims/yr, disciplined supplements alone ≈ **+$1–2M revenue**; cash cycle shortens 3–6 weeks → funds the growth without debt.

## 4. Procurement & Supplier Leverage
**Typical pain:** buying shingles at posted price from one branch; certification rebates unclaimed.
**The change:** consolidate volume against two suppliers and bid them quarterly; climb GAF certification tier (Master Elite unlocks better warranty product to SELL + rebates); claim co-op ad dollars (manufacturers reimburse a % of advertising — most contractors never file).
**Worth:** 2–4% off COGS on ~$7M materials/labor ≈ **$150–250K/yr**, plus co-op funds offsetting the ad budget we specced.

## 5. Customer Experience — the referral machine
**Typical pain:** homeowner silence between sign and install ("did they forget me?") → cancellations, 1-star risk; no systematic referral ask.
**The change (mostly built):** client portal goes live (status, money math, docs); automated milestone messages; post-install photo album + warranty certificate delivered digitally; **referral engine**: $100–250 bounty, asked at the two peak-joy moments (claim approved, install complete), tracked in dashboard.
**Worth:** referral jobs close at 2–3× the rate of cold leads at ~zero CAC. 10% of 1,400 jobs from referrals = **~$2M of nearly-free revenue** — and the portal is why reviews go from 131 to 400+.

## 6. Crews, Safety & Compliance — protecting the license that prints the money
**Typical pain:** sub paperwork scattered; one OSHA visit = $16K+ per serious citation; one uninsured sub injury = existential.
**The change:** crew compliance vault (COI, W-9, license, safety cert per crew, expiry alarms); toolbox-talk log; photo-documented harness use on every job (also marketing content); annual workers-comp audit prep folder maintained continuously, not in a panic.
**Worth:** this is downside protection — one prevented citation or misclassified-sub finding pays for the whole system. Buyers also price this heavily (see §9).

## 7. People Ops beyond sales — retention is cheaper than recruiting
**The change:** rep comp dashboard (everyone sees their collected pipeline → fewer "where's my check" exits); production bonus tied to install-week speed + zero-callback quality; quarterly top-crew bonus from the margin recovered in §2; exit interviews logged — turnover patterns surface in the dashboard.
**Worth:** replacing a producing rep costs ~$30–60K in lost pipeline + ramp. Cutting turnover by 2 reps/yr ≈ **$100K+**.

## 8. Data & Decision Rhythm — the operating system habit
**The change:** the weekly scoreboard (built) becomes a standing 30-min Monday meeting: last week's numbers vs model, one bottleneck named, one owner assigned. Monthly: job-costing review (§2) + cash review (§3). Quarterly: model re-forecast vs $20M path.
**Worth:** this is what makes everything above stick. Companies don't fail from missing tools; they fail from never looking at the board.

## 9. Enterprise Value — the ending most contractors never write
A $10M roofer run on whiteboards sells (if at all) at **2–3× EBITDA**. A $20M company with recurring revenue (Roof Shield), documented systems (this repo), a self-running demand engine, clean books per §2–3, and compliance per §6 trades at **5–8× — and buyers exist** (PE rollups are actively consolidating roofing).
**The math that should motivate ownership:** $20M revenue @ 12% EBITDA = $2.4M × the *difference between 3× and 6×* = **+$7.2M of personal wealth created by the systems alone**, before any revenue growth. That's the line that closes the equity conversation.

---

## The complete transformation map (status of all 20 systems)
| # | System | Status |
|---|---|---|
| 1–12 | Site, funnels, satellite tool, SEO/AI-SEO, 5 AI agents, report factory, dashboards, storm automation, training gym, Roof Shield, reactivation kit, MRR product | ✅ BUILT (this repo) |
| 13 | Production install board + capacity model | Spec'd (§1) — same Supabase backend, ships with dashboard build week |
| 14 | Job costing per job/crew/rep | Spec'd (§2) — needs their material invoices + crew rates |
| 15 | RCV/supplement/deductible cash engine | Spec'd (§3) — Agent 5 extension |
| 16 | Procurement leverage + co-op funds | Playbook (§4) — needs supplier invoices, one quarter |
| 17 | Referral engine + portal CX | 80% built (§5) — bounty decision from ownership |
| 18 | Crew compliance vault | Spec'd (§6) — folder structure + alarms, 1 day |
| 19 | Retention comp dashboards | Spec'd (§7) — rides on job costing |
| 20 | Weekly operating rhythm | Template ready (§8) — starts the week baseline numbers land |

**Combined worth of §1–9 beyond the demand engine: roughly $2–4M/yr in margin, cash, and near-free revenue — plus ~$7M in exit value.** None of it is AI hype; it's plumbing. The AI just means one operator (you) can run all of it.

**What it needs to start:** the same access list as everything else, plus three new asks — material invoices (90 days), crew pay rates, and their QuickBooks/accounting export. Add those to the day-one data request.
