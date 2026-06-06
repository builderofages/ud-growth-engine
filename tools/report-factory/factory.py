#!/usr/bin/env python3
"""
UD ROOFING — SPECULATIVE ROOF REPORT FACTORY
TrainYourAgent build. Storm ZIP -> personalized roof reports + print batch.

USAGE:
  python3 factory.py addresses.csv "2026-06-02 hail event, Gaithersburg"

INPUT : addresses.csv  -> one address per line (optionally: address,owner_name)
OUTPUT: output/reports/<slug>.html   personalized homeowner report pages
        output/index.html            rep route sheet (all reports, links, stats)
        output/print-batch.html      print-ready door-hanger cards w/ QR codes

LIVE MODE: set GOOGLE_API_KEY (Geocoding + Solar API + Static Maps enabled).
DEMO MODE: leave key empty -> deterministic realistic sample measurements.
"""
import csv, json, os, re, sys, urllib.parse, urllib.request

# ---------------- CONFIG ----------------
GOOGLE_API_KEY = ""                      # paste to go live
BASE_REPORT_URL = "https://udroofing.com/r"   # where reports will be hosted (for QR)
PHONE = "(240) 880-2108"
PRICE_PER_SQ = (475, 675)                # DMV asphalt installed, per square
WASTE = 1.10
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
# -----------------------------------------

def slugify(s): return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:60]

def fetch_json(url):
    with urllib.request.urlopen(url, timeout=20) as r:
        return json.loads(r.read().decode())

def measure(address):
    """Return dict: sqft, pitch_deg, segments, img_url (or None), formatted."""
    if GOOGLE_API_KEY:
        g = fetch_json("https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s"
                       % (urllib.parse.quote(address), GOOGLE_API_KEY))
        loc = g["results"][0]["geometry"]["location"]
        fmt = g["results"][0]["formatted_address"]
        try:
            s = fetch_json("https://solar.googleapis.com/v1/buildingInsights:findClosest"
                           "?location.latitude=%s&location.longitude=%s&requiredQuality=MEDIUM&key=%s"
                           % (loc["lat"], loc["lng"], GOOGLE_API_KEY))
            area = s["solarPotential"]["wholeRoofStats"]["areaMeters2"] * 10.764
            segs = s["solarPotential"].get("roofSegmentStats", [])
            pitch = sum(x.get("pitchDegrees", 20) for x in segs) / max(len(segs), 1)
            nseg = len(segs)
        except Exception:
            area, pitch, nseg = 2300, 22, 6
        img = ("https://maps.googleapis.com/maps/api/staticmap?center=%s,%s&zoom=20"
               "&size=640x400&maptype=satellite&key=%s" % (loc["lat"], loc["lng"], GOOGLE_API_KEY))
        return dict(sqft=area, pitch=pitch, segs=nseg, img=img, fmt=fmt)
    # demo mode — deterministic per address
    seed = sum(ord(c) for c in address)
    return dict(sqft=1750 + seed % 1400, pitch=18 + seed % 14, segs=4 + seed % 7,
                img=None, fmt=address)

def estimate(sqft):
    squares = round(sqft * WASTE / 100)
    return squares, round(squares * PRICE_PER_SQ[0] / 100) * 100, round(squares * PRICE_PER_SQ[1] / 100) * 100

CSS = """
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'Inter',system-ui,sans-serif;background:#f5f8fd;color:#0b1727;line-height:1.55}
.wrap{max-width:760px;margin:0 auto;padding:1.2rem}
.hdr{background:linear-gradient(135deg,#071c33,#0d3a73);color:#fff;border-radius:18px;padding:1.6rem;text-align:center}
.hdr .tag{font-size:.72rem;font-weight:700;letter-spacing:.12em;color:#7fb0ff}
.hdr h1{font-size:1.5rem;margin:.4rem 0}
.card{background:#fff;border:1px solid #e3e9f4;border-radius:16px;padding:1.3rem;margin-top:1rem;box-shadow:0 8px 30px -18px rgba(10,37,64,.3)}
.sat{border-radius:12px;width:100%;display:block}
.sat-demo{height:280px;border-radius:12px;background:repeating-linear-gradient(45deg,#15324f 0 22px,#173a5c 22px 44px);position:relative}
.sat-demo .h{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%) rotate(-8deg);width:180px;height:130px;background:#2d4a66;border:2.5px dashed #ffb020}
.stats{display:grid;grid-template-columns:1fr 1fr;gap:.7rem;margin-top:1rem}
.stat{background:#eef4ff;border-radius:12px;padding:.8rem}
.stat .v{font-weight:800;font-size:1.3rem;color:#0a2540}
.stat .l{font-size:.72rem;color:#64708c;font-weight:700;text-transform:uppercase}
.price{background:#0a2540;color:#fff;border-radius:14px;padding:1.1rem;margin-top:1rem}
.price .v{color:#7fb0ff;font-weight:900;font-size:1.7rem}
.ins{background:#f0fdf4;border:1px solid #bbf7d0;border-radius:12px;padding:.9rem;margin-top:1rem;font-size:.92rem;color:#14532d}
.cta{display:block;text-align:center;background:linear-gradient(135deg,#1463ff,#0d4fd6);color:#fff;font-weight:800;border-radius:999px;padding:1rem;margin-top:1.1rem;text-decoration:none;font-size:1.05rem}
.fine{font-size:.72rem;color:#8a93a8;text-align:center;margin:1rem 0}
"""

def report_html(d):
    squares, lo, hi = estimate(d["sqft"])
    ratio = round(__import__("math").tan(d["pitch"] * 3.14159 / 180) * 12)
    sat = ('<img class="sat" src="%s" alt="Your roof from above"/>' % d["img"]) if d["img"] \
          else '<div class="sat-demo"><div class="h"></div></div>'
    return f"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>Your Roof Report — United Developers</title>
<style>{CSS}</style></head><body><div class="wrap">
<div class="hdr"><div class="tag">🛰️ PERSONAL ROOF REPORT</div>
<h1>{d['fmt']}</h1>
<div style="font-size:.85rem;color:#c9d8f0">{d['storm']}</div></div>
<div class="card">{sat}
<div class="stats">
<div class="stat"><div class="v">{round(d['sqft']):,}</div><div class="l">Roof area (sq ft)</div></div>
<div class="stat"><div class="v">{squares}</div><div class="l">Roofing squares</div></div>
<div class="stat"><div class="v">{ratio}/12</div><div class="l">Avg pitch</div></div>
<div class="stat"><div class="v">{'Complex' if d['segs']>8 else 'Moderate' if d['segs']>5 else 'Simple'}</div><div class="l">Complexity</div></div>
</div>
<div class="price"><div style="font-size:.72rem;font-weight:700;letter-spacing:.1em;color:#9fb2d2">ESTIMATED REPLACEMENT RANGE*</div>
<div class="v">${lo:,} – ${hi:,}</div>
<div style="font-size:.82rem;color:#c9d8f0">Architectural asphalt, installed</div></div>
<div class="ins">✅ <b>Recent storm in your area.</b> If damage qualifies for an insurance claim, your out-of-pocket is often <b>just your deductible</b> — we handle the claim with you. GAF-certified · A+ BBB · 131+ ⭐⭐⭐⭐⭐</div>
<a class="cta" href="tel:+12408802108">📞 Claim my FREE on-site verification — {PHONE}</a>
</div>
<p class="fine">*Preliminary aerial estimate; exact quote after free inspection. United Developers · MHIC #111971 · VA DPOR #2705183185</p>
</div></body></html>"""

def qr(url, size=170):
    return ("https://api.qrserver.com/v1/create-qr-code/?size=%dx%d&data=%s"
            % (size, size, urllib.parse.quote(url)))

def main():
    src = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "addresses.csv")
    storm = sys.argv[2] if len(sys.argv) > 2 else "Recent hail & wind activity in your neighborhood"
    os.makedirs(os.path.join(OUT, "reports"), exist_ok=True)
    rows = []
    with open(src) as f:
        for line in csv.reader(f):
            if not line or not line[0].strip() or line[0].startswith("#"): continue
            rows.append((line[0].strip(), line[1].strip() if len(line) > 1 else ""))
    print("Generating %d reports (%s mode)..." % (len(rows), "LIVE" if GOOGLE_API_KEY else "DEMO"))
    items = []
    for addr, owner in rows:
        d = measure(addr); d["storm"] = storm
        slug = slugify(addr)
        with open(os.path.join(OUT, "reports", slug + ".html"), "w") as f:
            f.write(report_html(d))
        squares, lo, hi = estimate(d["sqft"])
        items.append(dict(addr=d["fmt"], owner=owner, slug=slug, sqft=round(d["sqft"]),
                          squares=squares, lo=lo, hi=hi, url=f"{BASE_REPORT_URL}/{slug}"))
        print("  ✓", addr)

    # rep route sheet
    rowshtml = "".join(
        f"<tr><td><b>{i['addr']}</b><br><small>{i['owner']}</small></td>"
        f"<td>{i['sqft']:,} sqft · {i['squares']} sq</td><td>${i['lo']:,}–${i['hi']:,}</td>"
        f"<td><a href='reports/{i['slug']}.html'>report</a></td>"
        f"<td>☐ knocked&nbsp; ☐ report left&nbsp; ☐ inspection booked</td></tr>" for i in items)
    with open(os.path.join(OUT, "index.html"), "w") as f:
        f.write(f"""<!DOCTYPE html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Rep Route Sheet — {storm}</title><style>{CSS}
table{{width:100%;border-collapse:collapse;font-size:.88rem;background:#fff;border-radius:12px}}
td,th{{padding:.6rem;border-bottom:1px solid #e3e9f4;text-align:left;vertical-align:top}}</style></head>
<body><div class="wrap" style="max-width:980px"><div class="hdr"><div class="tag">REP ROUTE SHEET</div>
<h1>{storm}</h1><div style="font-size:.85rem;color:#c9d8f0">{len(items)} personalized reports generated</div></div>
<div class="card"><table><tr><th>Address</th><th>Roof</th><th>Estimate</th><th>Report</th><th>Status</th></tr>{rowshtml}</table></div>
</div></body></html>""")

    # print batch (door hangers, 4 per page)
    cards = "".join(f"""<div class="dh"><div class="dh-top">🛰️ WE ALREADY MEASURED YOUR ROOF</div>
<div class="dh-addr">{i['addr']}</div>
<div class="dh-row"><div><div class="dh-num">{i['sqft']:,}</div><div class="dh-lbl">SQ FT</div></div>
<div><div class="dh-num">${i['lo']//1000}–{i['hi']//1000}K</div><div class="dh-lbl">EST. RANGE</div></div>
<img src="{qr(i['url'])}" width="86" height="86" alt="QR"/></div>
<div class="dh-cta">Scan for your full report → or call {PHONE}</div>
<div class="dh-fine">Storm-damage claims: most homeowners pay deductible only. United Developers · GAF-certified · A+ BBB</div></div>""" for i in items)
    with open(os.path.join(OUT, "print-batch.html"), "w") as f:
        f.write(f"""<!DOCTYPE html><html><head><meta charset="utf-8"><title>Print Batch — Door Cards</title><style>
body{{font-family:Inter,system-ui,sans-serif;background:#eee;margin:0;padding:1rem}}
.dh{{width:4in;background:#fff;border:1px solid #ccc;border-radius:10px;padding:.7rem .8rem;margin:.3rem;display:inline-block;vertical-align:top;page-break-inside:avoid}}
.dh-top{{font-size:.62rem;font-weight:800;letter-spacing:.1em;color:#1463ff}}
.dh-addr{{font-weight:800;color:#0a2540;font-size:.95rem;margin:.25rem 0}}
.dh-row{{display:flex;gap:1rem;align-items:center;justify-content:space-between;margin:.4rem 0}}
.dh-num{{font-weight:900;font-size:1.25rem;color:#0a2540}}
.dh-lbl{{font-size:.58rem;font-weight:700;color:#64708c;letter-spacing:.08em}}
.dh-cta{{background:#0a2540;color:#fff;border-radius:8px;padding:.45rem .6rem;font-size:.74rem;font-weight:700;text-align:center}}
.dh-fine{{font-size:.56rem;color:#8a93a8;margin-top:.35rem}}
@media print{{body{{background:#fff}}}}</style></head><body>{cards}</body></html>""")
    print("\nDone → output/index.html (route sheet) · output/print-batch.html (door cards) · output/reports/*.html")

if __name__ == "__main__":
    main()
