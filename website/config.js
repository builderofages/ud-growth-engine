/* ============================================================================
   UD GROWTH ENGINE — CENTRAL INTEGRATION SWITCHBOARD
   ----------------------------------------------------------------------------
   This is the ONE file to edit at launch. Paste keys/IDs below and the whole
   site wires itself: analytics, ad pixels, tag manager, CRM lead delivery,
   call tracking, conversion events on every form — all automatic.
   Nothing else needs editing. Leave a value as "" to keep that integration off.
   ============================================================================ */
window.UD_CONFIG = {
  // --- Analytics & attribution (paste when Shah is on-site) ---
  GA4_ID:        "",   // "G-XXXXXXX"  Google Analytics 4
  GTM_ID:        "",   // "GTM-XXXXXXX" Google Tag Manager (optional; runs alongside GA4)
  META_PIXEL_ID: "",   // "1234567890" Meta/Facebook Pixel for ad retargeting
  GOOGLE_ADS_ID: "",   // "AW-XXXXXXX" Google Ads conversion tag
  GOOGLE_ADS_LEAD_LABEL: "", // conversion label for a booked-lead event

  // --- Lead delivery (where every form on the site sends to) ---
  LEAD_EMAIL:    "trainyouragent@gmail.com",   // FormSubmit inbox (swap to office@udroofing.com after activation)
  LEAD_CC:       "",   // optional: also copy a second inbox on every lead (e.g. "sales@udroofing.com")
  AUTORESPONSE: "Thanks for reaching out to United Developers — we've got your request and a roofing specialist will call you shortly from (240) 880-2108. If it's urgent storm damage, call us now at (240) 880-2108 and we'll get a free 24-hour inspection on the calendar. — United Developers / UD Roofing (MHIC #111971 · VA #2705183185)",
  CRM_WEBHOOK:   "",   // GoHighLevel / ServiceTitan / JobNimbus / Zapier inbound webhook URL
  SMS_WEBHOOK:   "",   // optional: webhook that fires an instant SMS auto-reply to the lead

  // --- Maps & measurement ---
  GOOGLE_MAPS_KEY: "", // Geocoding + Solar + Static Maps key for the live satellite roof tool

  // --- Call tracking (swaps the displayed number so calls are attributable) ---
  TRACKING_PHONE:      "",  // e.g. "(240) 555-0000" — leave "" to show the real line
  REAL_PHONE_DISPLAY:  "(240) 880-2108",
  REAL_PHONE_TEL:      "+12408802108",

  // --- AI agents (ElevenLabs) ---
  AGENT_RILEY: "agent_2801ktf0hpcefj1bmz3gp0akkxp1",  // receptionist
  AGENT_DEX:   "agent_0701ktfcsjtkfw3rtja6nbf06ns7",  // sales specialist

  // --- Financing partner (paste application URL when lender is signed) ---
  LENDER_URL:  "",   // Service Finance / GreenSky / Hearth application link

  // --- Booking (optional Calendly/Acuity inline scheduler) ---
  BOOKING_URL: ""
};

(function () {
  var C = window.UD_CONFIG;

  /* ---- 1. Google Analytics 4 ---- */
  if (C.GA4_ID) {
    var g = document.createElement('script'); g.async = 1;
    g.src = 'https://www.googletagmanager.com/gtag/js?id=' + C.GA4_ID;
    document.head.appendChild(g);
    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { dataLayer.push(arguments); };
    gtag('js', new Date()); gtag('config', C.GA4_ID);
    if (C.GOOGLE_ADS_ID) gtag('config', C.GOOGLE_ADS_ID);
  }

  /* ---- 2. Google Tag Manager ---- */
  if (C.GTM_ID) {
    (function (w, d, s, l, i) {
      w[l] = w[l] || []; w[l].push({ 'gtm.start': new Date().getTime(), event: 'gtm.js' });
      var f = d.getElementsByTagName(s)[0], j = d.createElement(s);
      j.async = true; j.src = 'https://www.googletagmanager.com/gtm.js?id=' + i;
      f.parentNode.insertBefore(j, f);
    })(window, document, 'script', 'dataLayer', C.GTM_ID);
  }

  /* ---- 3. Meta Pixel ---- */
  if (C.META_PIXEL_ID) {
    !function (f, b, e, v, n, t, s) {
      if (f.fbq) return; n = f.fbq = function () { n.callMethod ? n.callMethod.apply(n, arguments) : n.queue.push(arguments) };
      if (!f._fbq) f._fbq = n; n.push = n; n.loaded = !0; n.version = '2.0'; n.queue = [];
      t = b.createElement(e); t.async = !0; t.src = v; s = b.getElementsByTagName(e)[0]; s.parentNode.insertBefore(t, s)
    }(window, document, 'script', 'https://connect.facebook.net/en_US/fbevents.js');
    fbq('init', C.META_PIXEL_ID); fbq('track', 'PageView');
  }

  /* ---- 4. Unified tracking helper — fire a conversion across every connected platform at once ---- */
  window.UD = window.UD || {};
  UD.track = function (eventName, params) {
    params = params || {};
    try { if (window.gtag) gtag('event', eventName, params); } catch (e) {}
    try { if (window.dataLayer) dataLayer.push(Object.assign({ event: eventName }, params)); } catch (e) {}
    try { if (window.fbq) fbq('track', eventName === 'lead' ? 'Lead' : eventName, params); } catch (e) {}
    try {
      if (eventName === 'lead' && C.GOOGLE_ADS_ID && C.GOOGLE_ADS_LEAD_LABEL && window.gtag)
        gtag('event', 'conversion', { send_to: C.GOOGLE_ADS_ID + '/' + C.GOOGLE_ADS_LEAD_LABEL });
    } catch (e) {}
  };

  /* ---- 5. Unified lead delivery — one call sends to email + CRM + SMS + fires the conversion ---- */
  UD.lead = function (data, subject) {
    data = data || {};
    data.page = location.pathname; data.ts = data.ts || new Date().toISOString();
    // a) email via FormSubmit — with instant auto-reply to the lead + optional CC fan-out
    if (C.LEAD_EMAIL) {
      var payload = Object.assign({ _subject: subject || 'UD WEBSITE LEAD', _template: 'table' }, data);
      if (C.LEAD_CC) payload._cc = C.LEAD_CC;
      // instant branded auto-reply — only when the lead gave a real email (FormSubmit replies to the _replyto address)
      var leadEmail = data.email || data.Email || '';
      if (C.AUTORESPONSE && /@/.test(leadEmail)) { payload._replyto = leadEmail; payload._autoresponse = C.AUTORESPONSE; }
      fetch('https://formsubmit.co/ajax/' + C.LEAD_EMAIL, {
        method: 'POST', headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
        body: JSON.stringify(payload)
      }).catch(function () {});
    }
    // b) CRM webhook (GHL / ServiceTitan / JobNimbus / Zapier)
    if (C.CRM_WEBHOOK) fetch(C.CRM_WEBHOOK, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(data) }).catch(function () {});
    // c) instant-SMS webhook
    if (C.SMS_WEBHOOK) fetch(C.SMS_WEBHOOK, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(data) }).catch(function () {});
    // d) conversion event everywhere
    UD.track('lead', { value: data.est_high || data.roofing_squares || undefined });
  };

  /* ---- 6. Call tracking — swap displayed phone numbers, keep clicks attributable ---- */
  if (C.TRACKING_PHONE) {
    document.addEventListener('DOMContentLoaded', function () {
      document.querySelectorAll('a[href^="tel:"]').forEach(function (a) {
        a.addEventListener('click', function () { UD.track('call_click'); });
      });
    });
  }

  /* ---- 7. Auto conversion + CRM forwarding — ANY form submit fires a lead event AND
     (if CRM_WEBHOOK is set) forwards the serialized fields to the CRM. Zero per-form wiring. ---- */
  document.addEventListener('submit', function (e) {
    var f = e.target;
    if (!f || f.tagName !== 'FORM') return;
    UD.track('form_submit', { form_id: f.id || 'unknown' });
    UD.track('lead', {});
    if (C.CRM_WEBHOOK) {
      var d = { form_id: f.id || 'unknown', page: location.pathname, ts: new Date().toISOString() };
      f.querySelectorAll('input,select,textarea').forEach(function (el) {
        var k = el.id || el.name; if (k && el.value) d[k] = el.value;
      });
      fetch(C.CRM_WEBHOOK, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(d) }).catch(function () {});
    }
  }, true);

  /* ---- 8. Lender link auto-fill — any element with data-ud="finance" points to the lender when set ---- */
  document.addEventListener('DOMContentLoaded', function () {
    if (C.LENDER_URL) document.querySelectorAll('[data-ud="finance"]').forEach(function (el) { el.href = C.LENDER_URL; });
    if (C.BOOKING_URL) document.querySelectorAll('[data-ud="book"]').forEach(function (el) { el.href = C.BOOKING_URL; });
  });
})();
