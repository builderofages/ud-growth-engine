#!/usr/bin/env python3
"""Cloud article engine for the UD growth repo. Pops one keyword from
growth/keyword-queue.txt, generates a full on-brand resource article via the
Anthropic API, writes it to website/resources/, and adds it to sitemap.xml.
Run from repo root (GitHub Actions does this automatically)."""
import os, re, sys, pathlib
import anthropic

ROOT = pathlib.Path(__file__).resolve().parent.parent
QUEUE = ROOT / "growth" / "keyword-queue.txt"
RES = ROOT / "website" / "resources"
SITEMAP = ROOT / "website" / "sitemap.xml"

if not QUEUE.exists() or not QUEUE.read_text().strip():
    print("Keyword queue empty — nothing to publish."); sys.exit(0)

lines = [l.strip() for l in QUEUE.read_text().splitlines() if l.strip()]
keyword, rest = lines[0], lines[1:]
slug = re.sub(r"[^a-z0-9]+", "-", keyword.lower()).strip("-")[:80]
out = RES / f"{slug}.html"
if out.exists():
    print(f"{out} already exists; dropping keyword and exiting.")
    QUEUE.write_text("\n".join(rest) + "\n"); sys.exit(0)

sample = next(p for p in sorted(RES.glob("*.html")) if p.name != "index.html")
template = sample.read_text()[:18000]

client = anthropic.Anthropic()
msg = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=8000,
    system=(
        "You write SEO/AEO resource articles for United Developers (UD Roofing), a "
        "GAF-certified, family-owned roofing & storm-restoration company in the DMV "
        "(MD/VA). Facts you may use verbatim: phone (240) 880-2108, email "
        "office@udroofing.com, MD MHIC #111971, VA Class A #2705183185, PA #192325, "
        "A+ BBB, 4.9 stars / 131+ Google reviews, since 2005, offices in Bethesda MD "
        "and Alexandria VA. NEVER invent prices as guarantees (give ranges, say "
        "'typical DMV range'), NEVER promise insurance outcomes, NEVER suggest "
        "deductible waiving (illegal MD/VA). Output a COMPLETE standalone HTML page "
        "matching the structure, css links, header/footer, and JSON-LD schema "
        "patterns of the sample page provided. Canonical URL must be "
        "https://udroofing.com/resources/{slug}.html. Include FAQPage JSON-LD with "
        "4-6 real questions. 1500-2200 words, expert but plain-spoken, with a lead "
        "CTA to the free inspection and (240) 880-2108. Output ONLY the HTML."
    ).replace("{slug}", slug),
    messages=[{"role": "user", "content":
        f"Target keyword/topic: {keyword}\n\nSample page for structure/branding:\n\n{template}"}],
)
html = msg.content[0].text
html = re.sub(r"^```html\s*|\s*```$", "", html.strip())
if "<html" not in html.lower():
    print("Generation did not return an HTML page; aborting without commit."); sys.exit(1)

out.write_text(html)
sm = SITEMAP.read_text()
entry = (f"  <url>\n    <loc>https://udroofing.com/resources/{slug}.html</loc>\n"
         f"    <changefreq>monthly</changefreq>\n    <priority>0.8</priority>\n  </url>\n")
SITEMAP.write_text(sm.replace("</urlset>", entry + "</urlset>"))
QUEUE.write_text("\n".join(rest) + ("\n" if rest else ""))
print(f"Published {out.relative_to(ROOT)} and updated sitemap.")
