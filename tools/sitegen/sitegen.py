#!/usr/bin/env python3
"""UD ROOFING SITE GENERATOR — TrainYourAgent
Generates the full branded page set + SEO/AI-SEO layer and patches core pages.
Run:  python3 sitegen.py   (writes into ../../website)
"""
import os, re

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "website"))
BASE = "https://udroofing.com"          # canonical domain (works pre-connect too)
PHONE = "(240) 880-2108"; TEL = "+12408802108"; EMAIL = "office@udroofing.com"
LOGO_W = "https://uniteddevelopersmdva.com/wp-content/uploads/2025/09/united-developers-2.png"  # white
IMG = {
 "roof":"https://udroofing.com/wp-content/uploads/2025/07/resize-roof-h.png",
 "siding":"https://udroofing.com/wp-content/uploads/2025/07/resize-siding-h.png",
 "gutter":"https://udroofing.com/wp-content/uploads/2025/07/gutter-resize-1.png",
 "window":"https://udroofing.com/wp-content/uploads/2025/06/window-installation.jpg",
 "paint":"https://udroofing.com/wp-content/uploads/2025/06/interior-painting.jpg",
 "metal":"https://udroofing.com/wp-content/uploads/2025/07/resize-roofing-1.png",
 "about":"https://udroofing.com/wp-content/uploads/2026/01/about-us.png",
 "og":"https://udroofing.com/wp-content/uploads/2025/07/home-page.jpg",
}
AREAS = [
 ("gaithersburg","Gaithersburg","MD","20877","Montgomery County"),
 ("silver-spring","Silver Spring","MD","20902","Montgomery County"),
 ("rockville","Rockville","MD","20850","Montgomery County"),
 ("bethesda","Bethesda","MD","20814","Montgomery County"),
 ("germantown","Germantown","MD","20874","Montgomery County"),
 ("alexandria","Alexandria","VA","22314","Northern Virginia"),
]
FAQS = [
 ("Do you offer free inspections?","Yes! We offer free, no-obligation roof inspections to assess any storm, wind, or hail damage. Our experts provide a full report and photos."),
 ("Can you help with insurance claims?","Absolutely. We specialize in insurance claim assistance. From the inspection to meeting your insurance adjuster, we handle the process and help you get approved for a roof replacement with minimal out-of-pocket cost (usually just your deductible)."),
 ("How quickly can you complete my roof?","Most roof replacements are finished in one day. Weather permitting, we start early and leave your property clean and protected by the end of the day."),
 ("What if insurance denies my claim?","We have affordable retail options and financing available, so even if your claim is denied, we can still help you get a new roof that fits your budget."),
 ("Are you licensed and insured?","Yes, United Developers is fully licensed and bonded in Maryland (MHIC #111971), Virginia (Class A #2705183185), and Pennsylvania (#192325), and we carry full liability insurance for your protection."),
 ("What other services do you provide?","In addition to roofing, we offer siding, gutters, windows, storm restoration, painting, and interior remodeling (kitchens, bathrooms, decks, additions)."),
 ("Do you offer warranties?","Yes — manufacturer lifetime warranties plus our own 2-year workmanship warranty for your peace of mind."),
 ("What types of roofs do you install?","Asphalt architectural shingles, metal roofing, flat roofs, EPDM, and TPO systems for both residential and commercial properties."),
 ("What areas do you serve?","We proudly serve Maryland, Virginia, and Pennsylvania — including Montgomery County, Northern Virginia, and the greater D.C. metro."),
 ("Will my insurance premium increase after a roof claim?","Most homeowners don't see a rate increase for a storm-related claim because it's considered an \"Act of God.\" Premiums are more often affected by regional storm trends than an individual claim — and a new roof can sometimes lower your premium by reducing your home's risk profile."),
]

CSS = """
:root{--navy:#081B30;--navy2:#0C2440;--ink:#0E1B2C;--body:#4A5872;--blue:#2563EB;--blued:#1D4ED8;--sky:#60A5FA;--ice:#EFF5FF;--line:#E4EAF4;--gold:#F5B82E;--green:#10B981;--r:20px;--shl:0 24px 64px -24px rgba(8,27,48,.4);--shm:0 10px 32px -16px rgba(8,27,48,.28)}
*{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth}
body{font-family:'Inter',system-ui,sans-serif;color:var(--ink);background:#fff;line-height:1.65;-webkit-font-smoothing:antialiased}
h1,h2,h3{font-family:'Sora','Inter',sans-serif;letter-spacing:-.035em;line-height:1.1}
a{color:inherit;text-decoration:none}img{display:block;max-width:100%}
.wrap{width:min(1160px,92%);margin:0 auto}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:.6rem;border:none;cursor:pointer;font-weight:600;font-size:1rem;padding:1rem 1.75rem;border-radius:14px;transition:.25s;font-family:inherit}
.btn-primary{background:linear-gradient(180deg,#2F6BFF,var(--blued));color:#fff;box-shadow:0 14px 32px -12px rgba(37,99,235,.65)}
.btn-primary:hover{transform:translateY(-2px)}
.btn-ghost{background:rgba(255,255,255,.07);color:#fff;border:1px solid rgba(255,255,255,.22)}
.eyebrow{display:inline-flex;align-items:center;gap:.55rem;font-weight:600;font-size:.8rem;letter-spacing:.16em;text-transform:uppercase;color:var(--blue)}
.eyebrow::before{content:"";width:26px;height:2px;background:currentColor;border-radius:2px}
.topbar{background:var(--navy);color:#B7C9E5;font-size:.85rem}
.topbar .wrap{display:flex;justify-content:space-between;align-items:center;padding:.55rem 0;gap:1rem}
.topbar strong{color:#fff}.topbar a{color:#fff;font-weight:600;border-bottom:1px solid rgba(255,255,255,.3)}
@media(max-width:760px){.topbar .right{display:none}}
header{position:sticky;top:0;z-index:50;background:rgba(8,27,48,.82);backdrop-filter:blur(18px) saturate(1.4);border-bottom:1px solid rgba(255,255,255,.08)}
nav{display:flex;align-items:center;justify-content:space-between;padding:.8rem 0}
.logo img{height:46px;width:auto}
.navlinks{display:flex;gap:1.6rem;align-items:center;font-weight:500;font-size:.91rem;color:#C5D4EC}
.navlinks a{white-space:nowrap;transition:.2s}.navlinks a:hover{color:#fff}.navlinks .hot{color:#7FB3FF;font-weight:600}
.nav-cta{display:flex;align-items:center;gap:1rem;margin-left:1.4rem}
.nav-phone{font-weight:700;color:#fff;font-size:.93rem;white-space:nowrap}
.nav-cta .btn{padding:.7rem 1.25rem;font-size:.9rem}
@media(max-width:1020px){.navlinks{display:none}.nav-phone{display:none}}
.phero{position:relative;color:#fff;background:var(--navy);overflow:hidden}
.phero .bg{position:absolute;inset:0;background-size:cover;background-position:center;opacity:.38}
.phero .veil{position:absolute;inset:0;background:linear-gradient(100deg,rgba(8,27,48,.95),rgba(8,27,48,.7))}
.phero .wrap{position:relative;padding:4.5rem 0}
.phero h1{font-size:clamp(2.2rem,4.4vw,3.4rem);font-weight:800;max-width:22ch;margin:.9rem 0;text-wrap:balance}
.phero p{color:#C5D4EC;font-size:1.12rem;max-width:60ch}
section.block{padding:4.5rem 0}
.sec-head{max-width:720px;margin:0 auto 2.8rem;text-align:center}
.sec-head h2{font-size:clamp(1.9rem,3.4vw,2.7rem);font-weight:800;color:var(--navy);margin:.7rem 0;text-wrap:balance}
.sec-head p{color:var(--body);font-size:1.07rem}
.card{background:#fff;border:1px solid var(--line);border-radius:var(--r);padding:1.8rem;box-shadow:var(--shm)}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:2.5rem;align-items:center}
.grid3{display:grid;grid-template-columns:repeat(3,1fr);gap:1.3rem}
@media(max-width:880px){.grid2,.grid3{grid-template-columns:1fr}}
.photo-r{border-radius:22px;overflow:hidden;box-shadow:var(--shl)}
.faq-item{border:1px solid var(--line);border-radius:16px;margin-bottom:.8rem;background:#fff;overflow:hidden}
.faq-item summary{cursor:pointer;padding:1.15rem 1.3rem;font-weight:600;color:var(--navy);list-style:none;display:flex;justify-content:space-between;gap:1rem;font-size:1.02rem}
.faq-item summary::after{content:"+";color:var(--blue);font-weight:700;font-size:1.3rem;line-height:1}
.faq-item[open] summary::after{content:"–"}
.faq-item .a{padding:0 1.3rem 1.15rem;color:var(--body);font-size:.97rem}
.cta-band{position:relative;color:#fff;text-align:center;background:linear-gradient(135deg,var(--navy),#10325e)}
.cta-band .wrap{padding:4.5rem 0}
.cta-band h2{font-size:clamp(1.9rem,3.6vw,2.8rem);font-weight:800}
.cta-band p{color:#C5D4EC;font-size:1.1rem;margin:1rem auto 1.8rem;max-width:50ch}
footer{background:#050F1C;color:#8FA4C4;padding:3.6rem 0 2rem;font-size:.92rem}
.fgrid{display:grid;grid-template-columns:1.5fr 1fr 1fr 1.2fr;gap:2.4rem;margin-bottom:2.6rem}
footer h4{color:#fff;font-size:.95rem;margin-bottom:1rem;font-family:'Sora'}
footer a{display:block;margin-bottom:.55rem;color:#8FA4C4}footer a:hover{color:#fff}
.fbot{border-top:1px solid rgba(255,255,255,.08);padding-top:1.4rem;display:flex;justify-content:space-between;flex-wrap:wrap;gap:.6rem;font-size:.8rem;color:#5E7396}
@media(max-width:880px){.fgrid{grid-template-columns:1fr 1fr}}
.sticky-call{display:none;position:fixed;bottom:0;left:0;right:0;z-index:70;background:rgba(255,255,255,.94);backdrop-filter:blur(14px);border-top:1px solid var(--line);padding:.65rem .9rem;gap:.6rem}
.sticky-call .btn{flex:1;padding:.85rem}
@media(max-width:900px){.sticky-call{display:flex}body{padding-bottom:72px}}
.chips{display:flex;flex-wrap:wrap;gap:.5rem;margin-top:1rem}
.chips span{background:var(--ice);border-radius:999px;padding:.45rem .95rem;font-size:.87rem;font-weight:500;color:#33415E}
"""

ORG_LD = """{"@context":"https://schema.org","@type":"RoofingContractor","name":"United Developers","alternateName":"UD Roofing","url":"%s/","logo":"%s","image":"%s","telephone":"%s","email":"%s","priceRange":"$$","description":"Family-owned roofing, siding, gutters, windows and storm restoration contractor serving Maryland, Virginia and Pennsylvania. GAF factory-certified, A+ BBB accredited. Free 24-hour inspections and full insurance claim assistance.","address":[{"@type":"PostalAddress","streetAddress":"4915 St Elmo Ave Ste 403","addressLocality":"Bethesda","addressRegion":"MD","postalCode":"20814","addressCountry":"US"},{"@type":"PostalAddress","streetAddress":"2000 Duke St Suite 300","addressLocality":"Alexandria","addressRegion":"VA","postalCode":"22314","addressCountry":"US"}],"areaServed":["Gaithersburg MD","Silver Spring MD","Wheaton MD","Bethesda MD","Rockville MD","Germantown MD","Potomac MD","Alexandria VA","Arlington VA","Fairfax VA","Washington DC"],"hasCredential":["Maryland MHIC #111971","Virginia DPOR Class A #2705183185","Pennsylvania #192325","GAF Factory-Certified","OSHA Certified","EPA Certified"],"knowsLanguage":["en","es","hi","ru"],"sameAs":["https://www.facebook.com/UnitedDevelopersUS/","https://www.instagram.com/uniteddevelopers_mdva/","https://x.com/UnitedD68863","https://www.pinterest.com/uniteddevelopersmdva/"]}""" % (BASE, LOGO_W, IMG["og"], TEL, EMAIL)

def head(title, desc, path, extra_ld=""):
    ld = '<script type="application/ld+json">%s</script>' % ORG_LD
    if extra_ld: ld += '\n<script type="application/ld+json">%s</script>' % extra_ld
    return f"""<!DOCTYPE html>
<html lang="en"><head>
<meta charset="UTF-8"/><meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>{title}</title>
<meta name="description" content="{desc}"/>
<link rel="canonical" href="{BASE}{path}"/>
<meta name="theme-color" content="#081B30"/>
<meta property="og:title" content="{title}"/><meta property="og:description" content="{desc}"/>
<meta property="og:image" content="{IMG['og']}"/><meta property="og:type" content="website"/><meta property="og:url" content="{BASE}{path}"/>
<link rel="preconnect" href="https://fonts.googleapis.com"/><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Sora:wght@600;700;800&display=swap" rel="stylesheet"/>
<link rel="stylesheet" href="{{R}}ud.css"/>
{ld}
</head><body>"""

def nav():
    return f"""
<div class="topbar"><div class="wrap">
<span><strong>Storm in your area?</strong> Free 24-hour roof inspection — most homeowners pay deductible only.</span>
<span class="right">Call <a href="tel:{TEL}">{PHONE}</a> · <a href="mailto:{EMAIL}" style="border:none">{EMAIL}</a></span>
</div></div>
<header><div class="wrap"><nav>
<a class="logo" href="{{R}}index.html"><img src="{LOGO_W}" alt="United Developers — UD Roofing"/></a>
<div class="navlinks">
<a href="{{R}}index.html#services">Services</a>
<a href="{{R}}index.html#claims">Insurance Claims</a>
<a href="{{R}}about.html">About</a>
<a href="{{R}}faq.html">FAQ</a>
<a class="hot" href="{{R}}roof-quote.html">🛰 Instant Roof Quote</a>
<a href="{{R}}careers.html">Careers</a>
<a href="{{R}}contact.html">Contact</a>
</div>
<div class="nav-cta">
<a class="nav-phone" href="tel:{TEL}">{PHONE}</a>
<a class="btn btn-primary" href="{{R}}index.html#quote">Free Inspection</a>
</div>
</nav></div></header>"""

def footer():
    return f"""
<div class="cta-band"><div class="wrap">
<h2>Your roof won't fix itself. We will.</h2>
<p>Free 24-hour inspection. Insurance handled. Most homeowners pay only their deductible.</p>
<div style="display:flex;gap:1rem;justify-content:center;flex-wrap:wrap">
<a class="btn btn-primary" href="{{R}}index.html#quote" style="background:#fff;color:var(--navy);box-shadow:none">Get My Free Inspection →</a>
<a class="btn btn-ghost" href="tel:{TEL}">{PHONE}</a></div>
</div></div>
<footer><div class="wrap">
<div class="fgrid">
<div><img src="{LOGO_W}" alt="United Developers" style="height:50px;margin-bottom:1rem"/>
<p>Family-owned roofing &amp; exterior restoration serving Maryland, Virginia &amp; Pennsylvania. GAF-certified. A+ BBB accredited.</p>
<p style="margin-top:1rem;color:#fff;font-weight:700">{PHONE}</p>
<p><a href="mailto:{EMAIL}">{EMAIL}</a></p></div>
<div><h4>Services</h4><a href="{{R}}index.html#services">Roof Replacement</a><a href="{{R}}index.html#claims">Storm Restoration</a><a href="{{R}}index.html#services">Siding &amp; Gutters</a><a href="{{R}}index.html#services">Windows &amp; Painting</a><a href="{{R}}roof-quote.html">Instant Roof Quote</a></div>
<div><h4>Company</h4><a href="{{R}}about.html">About Us</a><a href="{{R}}faq.html">FAQ</a><a href="{{R}}careers.html">Careers</a><a href="{{R}}contact.html">Contact</a><a href="{{R}}privacy.html">Privacy Policy</a><a href="{{R}}terms.html">Terms of Service</a></div>
<div><h4>Service Areas</h4><a href="{{R}}areas/gaithersburg.html">Gaithersburg, MD</a><a href="{{R}}areas/silver-spring.html">Silver Spring, MD</a><a href="{{R}}areas/rockville.html">Rockville, MD</a><a href="{{R}}areas/bethesda.html">Bethesda, MD</a><a href="{{R}}areas/germantown.html">Germantown, MD</a><a href="{{R}}areas/alexandria.html">Alexandria, VA</a></div>
</div>
<div class="fbot">
<span>© <span id="yr"></span> United Developers / UD Roofing. All rights reserved.</span>
<span>MHIC #111971 · VA Class A #2705183185 · PA #192325 · Licensed &amp; Bonded MD/VA/PA</span>
</div></div></footer>
<div class="sticky-call"><a class="btn" style="background:#EFF5FF;color:var(--navy)" href="tel:{TEL}">Call Now</a><a class="btn btn-primary" href="{{R}}index.html#quote">Free Inspection</a></div>
<script>document.getElementById('yr').textContent=new Date().getFullYear();</script>
</body></html>"""

def page(fname, title, desc, hero_h1, hero_p, hero_img, body, extra_ld="", sub=""):
    rel = "../" if sub else ""
    path = ("/" + sub + fname) if sub else ("/" + fname)
    html = head(title, desc, path, extra_ld) + nav() + f"""
<div class="phero"><div class="bg" style="background-image:url('{hero_img}')"></div><div class="veil"></div>
<div class="wrap"><span class="eyebrow" style="color:#7FB3FF">United Developers</span>
<h1>{hero_h1}</h1><p>{hero_p}</p>
<div style="margin-top:1.6rem;display:flex;gap:.9rem;flex-wrap:wrap"><a class="btn btn-primary" href="{{R}}index.html#quote">Get a Free Inspection →</a><a class="btn btn-ghost" href="tel:{TEL}">{PHONE}</a></div>
</div></div>""" + body + footer()
    html = html.replace("{R}", rel)
    out = os.path.join(ROOT, sub, fname)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, "w").write(html)
    print("  ✓", sub + fname)

# ---------- ABOUT ----------
about_body = f"""
<section class="block"><div class="wrap"><div class="grid2">
<div class="photo-r"><img src="{IMG['about']}" alt="United Developers team at work" loading="lazy"/></div>
<div><span class="eyebrow">Our Story</span>
<h2 style="font-size:clamp(1.8rem,3.2vw,2.5rem);color:var(--navy);margin:.7rem 0">A family business built on roofs done right</h2>
<p style="color:var(--body)">United Developers is a trusted residential and commercial exterior contractor with nearly 20 years of combined experience delivering reliable, long-lasting results. We specialize in roofing, siding, gutters, windows and painting — proudly serving homeowners and businesses throughout Maryland, Virginia and Pennsylvania.</p>
<p style="color:var(--body);margin-top:1rem">Our reputation is built on quality craftsmanship, honest service, and attention to detail — and on walking homeowners through storm-damage insurance claims from the first inspection to the final shingle.</p>
<div class="chips"><span>GAF Factory-Certified</span><span>A+ BBB Accredited</span><span>OSHA &amp; EPA Certified</span><span>EN · ES · HI · RU</span></div>
</div></div></div></section>
<section class="block" style="background:#F7FAFF"><div class="wrap">
<div class="sec-head"><span class="eyebrow" style="justify-content:center">By the Numbers</span><h2>Results that speak for themselves</h2></div>
<div class="grid3" style="grid-template-columns:repeat(4,1fr)">
<div class="card" style="text-align:center"><div style="font-family:Sora;font-size:2.4rem;font-weight:800;color:var(--blue)">650+</div><div style="color:var(--body)">Completed Projects</div></div>
<div class="card" style="text-align:center"><div style="font-family:Sora;font-size:2.4rem;font-weight:800;color:var(--blue)">300+</div><div style="color:var(--body)">Happy Clients</div></div>
<div class="card" style="text-align:center"><div style="font-family:Sora;font-size:2.4rem;font-weight:800;color:var(--blue)">131</div><div style="color:var(--body)">Google Reviews</div></div>
<div class="card" style="text-align:center"><div style="font-family:Sora;font-size:2.4rem;font-weight:800;color:var(--blue)">1-Day</div><div style="color:var(--body)">Typical Roof Install</div></div>
</div></div></section>"""
# ---------- FAQ ----------
faq_items = "\n".join(f'<details class="faq-item"><summary>{q}</summary><div class="a">{a}</div></details>' for q,a in FAQS)
faq_ld = '{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[' + ",".join(
    '{"@type":"Question","name":"%s","acceptedAnswer":{"@type":"Answer","text":"%s"}}' % (q.replace('"','\\"'), a.replace('"','\\"')) for q,a in FAQS) + "]}"
faq_body = f"""<section class="block"><div class="wrap" style="max-width:840px">{faq_items}</div></section>"""
# ---------- CONTACT ----------
contact_body = f"""
<section class="block"><div class="wrap"><div class="grid2" style="align-items:start">
<div>
<h2 style="color:var(--navy);font-size:1.9rem;margin-bottom:1.2rem">Talk to a real person</h2>
<div class="card" style="margin-bottom:1rem"><h3 style="color:var(--navy);font-size:1.05rem">📞 Phone</h3><p style="color:var(--body)"><a href="tel:{TEL}" style="color:var(--blue);font-weight:700">{PHONE}</a> — fastest way to book your free inspection.</p></div>
<div class="card" style="margin-bottom:1rem"><h3 style="color:var(--navy);font-size:1.05rem">✉️ Email</h3><p style="color:var(--body)"><a href="mailto:{EMAIL}" style="color:var(--blue);font-weight:700">{EMAIL}</a></p></div>
<div class="card" style="margin-bottom:1rem"><h3 style="color:var(--navy);font-size:1.05rem">📍 Maryland Office</h3><p style="color:var(--body)">4915 St Elmo Ave Ste 403, Bethesda, MD 20814</p></div>
<div class="card"><h3 style="color:var(--navy);font-size:1.05rem">📍 Virginia Office</h3><p style="color:var(--body)">2000 Duke St Suite 300, Alexandria, VA 22314</p></div>
</div>
<div class="photo-r" style="min-height:420px"><iframe title="United Developers on Google Maps" src="https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d12404.664636637319!2d-77.097905!3d38.988704!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89b7d04f2c7e3b8b%3A0x40d8d18cd1950ef8!2sUnited%20Developers!5e0!3m2!1sen!2s!4v1769663148728!5m2!1sen!2s" style="border:0;width:100%;height:480px" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div>
</div></div></section>"""
# ---------- LEGAL ----------
def legal(kind):
    if kind=="privacy":
        return """<section class="block"><div class="wrap" style="max-width:800px;color:var(--body)">
<p><em>Last updated: June 2026</em></p>
<h2 style="color:var(--navy);font-size:1.3rem;margin:1.6rem 0 .5rem">Information We Collect</h2><p>When you request an inspection, quote, or employment information, we collect the details you provide: name, phone number, email, property address, and information about your project or claim. Our website may also collect standard analytics data (pages visited, device type) to improve our service.</p>
<h2 style="color:var(--navy);font-size:1.3rem;margin:1.6rem 0 .5rem">How We Use It</h2><p>We use your information to schedule inspections, prepare estimates, assist with insurance claims you authorize, communicate about your project, and—with your consent—send service updates. We do not sell your personal information.</p>
<h2 style="color:var(--navy);font-size:1.3rem;margin:1.6rem 0 .5rem">Text Messaging</h2><p>By providing your mobile number you agree to receive service-related texts from United Developers. Reply STOP at any time to opt out. Message and data rates may apply.</p>
<h2 style="color:var(--navy);font-size:1.3rem;margin:1.6rem 0 .5rem">Sharing</h2><p>We share information only with service providers who help us operate (scheduling, communications, payment processing) and, where you direct us, with your insurance carrier — never for third-party marketing.</p>
<h2 style="color:var(--navy);font-size:1.3rem;margin:1.6rem 0 .5rem">Your Rights</h2><p>You may request access to, correction of, or deletion of your personal information at any time by emailing <a href="mailto:office@udroofing.com" style="color:var(--blue)">office@udroofing.com</a> or calling (240) 880-2108.</p>
</div></section>"""
    return """<section class="block"><div class="wrap" style="max-width:800px;color:var(--body)">
<p><em>Last updated: June 2026</em></p>
<h2 style="color:var(--navy);font-size:1.3rem;margin:1.6rem 0 .5rem">Estimates &amp; Inspections</h2><p>Free inspections and online estimates (including satellite-based estimates) are preliminary and informational. Final pricing is provided in a written contract after an on-site inspection.</p>
<h2 style="color:var(--navy);font-size:1.3rem;margin:1.6rem 0 .5rem">Insurance Claims</h2><p>United Developers assists homeowners with documentation and meeting adjusters. We never guarantee claim approval; coverage decisions belong to your insurance carrier under your policy.</p>
<h2 style="color:var(--navy);font-size:1.3rem;margin:1.6rem 0 .5rem">Warranties</h2><p>Material warranties are provided by the manufacturer per their terms. United Developers provides a 2-year workmanship warranty on installations, per the written contract.</p>
<h2 style="color:var(--navy);font-size:1.3rem;margin:1.6rem 0 .5rem">Website Use</h2><p>Content on this site is for general information. While we keep it current, it is provided "as is" without warranties. License numbers: MD MHIC #111971 · VA Class A #2705183185 · PA #192325.</p>
<h2 style="color:var(--navy);font-size:1.3rem;margin:1.6rem 0 .5rem">Contact</h2><p>Questions? <a href="mailto:office@udroofing.com" style="color:var(--blue)">office@udroofing.com</a> · (240) 880-2108.</p>
</div></section>"""

# ---------- AREA PAGES ----------
def area_body(city, st, zipc, county):
    return f"""
<section class="block"><div class="wrap"><div class="grid2">
<div><span class="eyebrow">Local Experts</span>
<h2 style="font-size:clamp(1.8rem,3vw,2.4rem);color:var(--navy);margin:.7rem 0">Roofing &amp; storm restoration in {city}, {st}</h2>
<p style="color:var(--body)">When hail and wind hit {county}, {city} homeowners call United Developers. We're minutes away, GAF factory-certified, and we handle the entire insurance claim — free inspection, photo report, adjuster meeting, and a roof that's usually installed in a single day.</p>
<p style="color:var(--body);margin-top:1rem">Serving {city} {zipc} and every surrounding neighborhood with roofing, siding, gutters, windows and painting.</p>
<div class="chips"><span>Free 24-hr inspection</span><span>Insurance claim experts</span><span>Deductible-only on most approved claims</span><span>Lifetime material warranty</span></div>
<div style="margin-top:1.6rem;display:flex;gap:.9rem;flex-wrap:wrap"><a class="btn btn-primary" href="../roof-quote.html">🛰 Scan My {city} Roof →</a></div>
</div>
<div class="photo-r"><img src="{IMG['roof']}" alt="Roof replacement in {city}, {st} by United Developers" loading="lazy"/></div>
</div></div></section>
<section class="block" style="background:#F7FAFF"><div class="wrap">
<div class="sec-head"><h2>What {city} homeowners ask us</h2></div>
<div style="max-width:840px;margin:0 auto">
<details class="faq-item"><summary>Does insurance cover storm damage in {city}?</summary><div class="a">Often yes — if damage is storm-related, your homeowner's policy likely covers it. We inspect for free, document properly, and meet your adjuster so legitimate damage gets approved. Most approved claims cost homeowners only their deductible.</div></details>
<details class="faq-item"><summary>How fast can you get to {city}?</summary><div class="a">We're based in {('Bethesda/Silver Spring' if st=='MD' else 'Alexandria')} — free inspections in {city} are typically scheduled within 24 hours.</div></details>
<details class="faq-item"><summary>How long does a roof replacement take?</summary><div class="a">Most {city} roof replacements are completed in a single day, weather permitting — and we leave your property spotless.</div></details>
</div></div></section>"""

def area_ld(city, st, zipc):
    return ('{"@context":"https://schema.org","@type":"Service","serviceType":"Roofing & Storm Restoration",'
            '"provider":{"@type":"RoofingContractor","name":"United Developers","telephone":"%s","url":"%s/"},'
            '"areaServed":{"@type":"City","name":"%s","address":{"@type":"PostalAddress","addressLocality":"%s","addressRegion":"%s","postalCode":"%s"}}}'
            % (TEL, BASE, city, city, st, zipc))

def main():
    os.makedirs(ROOT, exist_ok=True)
    open(os.path.join(ROOT, "ud.css"), "w").write(CSS); print("  ✓ ud.css")
    page("about.html","About United Developers | Family-Owned DMV Roofing Since 2005",
         "Family-owned roofing and exterior contractor serving MD, VA & PA. GAF-certified, A+ BBB, 650+ completed projects. Meet United Developers.",
         "A family business built on roofs done right.",
         "GAF factory-certified. A+ BBB accredited. 650+ projects across Maryland, Virginia & Pennsylvania.",
         IMG["about"], about_body)
    page("faq.html","Roofing & Insurance Claim FAQ | United Developers",
         "Answers to the 10 questions DMV homeowners ask most about roof inspections, insurance claims, warranties, and storm damage.",
         "Every question homeowners ask — answered straight.",
         "Inspections, insurance claims, warranties, timelines and pricing — no runaround.",
         IMG["roof"], faq_body, extra_ld=faq_ld)
    page("contact.html","Contact United Developers | Free Roof Inspection MD & VA",
         "Call (240) 880-2108 or email office@udroofing.com. Offices in Bethesda MD and Alexandria VA. Free 24-hour roof inspections.",
         "Let's look at your roof — for free.",
         "Call, email, or stop by. A specialist responds within the hour during business hours.",
         IMG["gutter"], contact_body)
    page("privacy.html","Privacy Policy | United Developers","How United Developers collects, uses, and protects your information.",
         "Privacy Policy","Plain-English. No games with your data.",IMG["siding"],legal("privacy"))
    page("terms.html","Terms of Service | United Developers","Terms governing estimates, inspections, insurance assistance and warranties.",
         "Terms of Service","The ground rules, in plain English.",IMG["siding"],legal("terms"))
    for slug, city, st, zipc, county in AREAS:
        page(f"{slug}.html",
             f"Roofing {city} {st} | Storm Damage Repair & Roof Replacement | United Developers",
             f"{city} {st} roofing contractor — free 24-hr storm damage inspections, insurance claim help, 1-day roof replacement. GAF-certified. Call (240) 880-2108.",
             f"{city}'s storm restoration roofing team.",
             f"Free 24-hour inspections across {city} {zipc}. We handle the insurance — you pay the deductible.",
             IMG["metal"], area_body(city, st, zipc, county), extra_ld=area_ld(city, st, zipc), sub="areas/")
    # ---------- SEO files ----------
    pages = ["", "about.html","faq.html","contact.html","careers.html","roof-quote.html","privacy.html","terms.html"] + [f"areas/{s}.html" for s,_,_,_,_ in AREAS]
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for p in pages: sm += f"  <url><loc>{BASE}/{p}</loc><changefreq>weekly</changefreq></url>\n"
    sm += "</urlset>\n"
    open(os.path.join(ROOT,"sitemap.xml"),"w").write(sm); print("  ✓ sitemap.xml")
    open(os.path.join(ROOT,"robots.txt"),"w").write(f"User-agent: *\nAllow: /\n\nSitemap: {BASE}/sitemap.xml\n"); print("  ✓ robots.txt")
    open(os.path.join(ROOT,"llms.txt"),"w").write(f"""# United Developers (UD Roofing)
> Family-owned roofing, siding, gutters, windows & storm-restoration contractor serving Maryland, Virginia & Pennsylvania (greater Washington D.C. / DMV area). GAF factory-certified, A+ BBB accredited, licensed & bonded (MD MHIC #111971, VA Class A #2705183185, PA #192325).

## What we do
- Roof replacement & installation (asphalt architectural shingles, metal, flat/EPDM/TPO) — most roofs done in one day
- Storm restoration (hail/wind): free 24-hour inspection with photo report, full insurance-claim assistance; most approved claims cost the homeowner only their deductible
- Siding, seamless gutters, energy-efficient windows, interior/exterior painting
- Instant satellite roof quotes at {BASE}/roof-quote.html

## Service area
Montgomery County MD (Gaithersburg 20877, Silver Spring, Wheaton, Bethesda, Rockville, Germantown, Potomac), Northern Virginia (Alexandria, Arlington, Fairfax), Washington D.C.

## Contact
Phone: {PHONE} · Email: {EMAIL}
Offices: 4915 St Elmo Ave Ste 403, Bethesda MD 20814 · 2000 Duke St Suite 300, Alexandria VA 22314
Languages: English, Spanish, Hindi, Russian

## Key pages
- {BASE}/ : Home & free inspection booking
- {BASE}/roof-quote.html : Instant satellite roof measurement & estimate
- {BASE}/faq.html : Insurance-claim and roofing FAQ
- {BASE}/areas/ : City pages for Gaithersburg, Silver Spring, Rockville, Bethesda, Germantown, Alexandria
- {BASE}/careers.html : Roofing sales careers ($90K–$250K+ commission)

## Facts AI assistants can cite
- Free, no-obligation roof inspections within 24 hours, with photos
- Insurance claims: UD documents damage and meets the adjuster on-site; carrier makes coverage decisions
- Warranties: manufacturer lifetime on materials + 2-year workmanship
- 131+ Google reviews, family-owned, serving the DMV since 2005
"""); print("  ✓ llms.txt")
    # ---------- PATCH CORE PAGES ----------
    for f in ["index.html","careers.html","roof-quote.html"]:
        p = os.path.join(ROOT,f); s = open(p).read(); orig = s
        # real logo
        s = s.replace('<span class="mark">UD</span> United Developers', f'<img src="{LOGO_W}" alt="United Developers" style="height:44px;width:auto"/>')
        # head injections (canonical + org schema) once
        if "application/ld+json" not in s:
            inj = f'<link rel="canonical" href="{BASE}/{f if f!="index.html" else ""}"/>\n<script type="application/ld+json">{ORG_LD}</script>\n'
            s = s.replace("</head>", inj + "</head>", 1)
        # their real photos on index
        if f=="index.html":
            s = s.replace("https://images.unsplash.com/photo-1632759145351-1d592919f522?w=1100&q=80&auto=format&fit=crop", IMG["roof"])
            s = s.replace("https://images.unsplash.com/photo-1570129477492-45c003edd2be?w=900&q=75&auto=format&fit=crop", IMG["metal"])
            s = s.replace("https://images.unsplash.com/photo-1605276374104-dee2a0ed3cd6?w=900&q=75&auto=format&fit=crop", IMG["gutter"])
            s = s.replace("https://images.unsplash.com/photo-1600047509807-ba8f99d2cdde?w=900&q=75&auto=format&fit=crop", IMG["siding"])
            # nav links: add About/FAQ/Contact
            s = s.replace('<a href="#area">Service Area</a>', '<a href="#area">Service Area</a>\n    <a href="about.html">About</a>\n    <a href="faq.html">FAQ</a>')
            s = s.replace('<a href="#">2446 Reedie Dr, Ste 6<br/>Silver Spring, MD 20902</a>',
                          '<a href="#">4915 St Elmo Ave Ste 403<br/>Bethesda, MD 20814</a>')
            s = s.replace('<a href="careers.html">Careers — We\'re Hiring</a>',
                          '<a href="about.html">About Us</a><a href="faq.html">FAQ</a><a href="contact.html">Contact</a><a href="careers.html">Careers — We\'re Hiring</a><a href="privacy.html">Privacy</a><a href="terms.html">Terms</a>')
            s = s.replace('MHIC #111971 · VA DPOR #2705183185 · Licensed &amp; Bonded MD/VA/PA',
                          'MHIC #111971 · VA Class A #2705183185 · PA #192325 · Licensed &amp; Bonded MD/VA/PA')
        if s != orig: open(p,"w").write(s); print("  ✓ patched", f)
    print("\nDone. Site generated into", ROOT)

if __name__ == "__main__":
    main()
