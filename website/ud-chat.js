/* UD Live Chat v2 — premium branded client for United Developers' agents. */
(function () {
  'use strict';
  /* ---- brand favicon injector — guarantees the UD mark on every page that loads this script ---- */
  try {
    if (!document.querySelector('link[rel~="icon"]')) {
      var _sc = document.querySelector('script[src*="ud-chat.js"]');
      var _fav = _sc ? _sc.src.replace(/ud-chat\.js.*$/, 'favicon.svg') : 'favicon.svg';
      var _l = document.createElement('link');
      _l.rel = 'icon'; _l.type = 'image/svg+xml'; _l.href = _fav;
      document.head.appendChild(_l);
    }
  } catch (e) {}
  var host = document.querySelector('elevenlabs-convai');
  var AGENT = host ? host.getAttribute('agent-id') : 'agent_2801ktf0hpcefj1bmz3gp0akkxp1';
  var IS_DEX = AGENT === 'agent_0701ktfcsjtkfw3rtja6nbf06ns7';
  var NAME = IS_DEX ? 'Dex' : 'Riley';
  var MONO = IS_DEX ? 'D' : 'R';
  var ROLE = IS_DEX ? 'Roofing Specialist' : 'Front Desk Coordinator';

  if (host) host.style.display = 'none';

  var css = ''
    /* ---- launcher ---- */
    + '.udc-launch{position:fixed;right:24px;bottom:24px;z-index:9990;display:flex;align-items:center;gap:.75rem;'
    + 'background:#fff;border:1px solid rgba(8,27,48,.08);cursor:pointer;border-radius:999px;padding:.55rem 1.25rem .55rem .55rem;'
    + 'font-family:Inter,system-ui,sans-serif;box-shadow:0 6px 16px -6px rgba(8,27,48,.22),0 24px 56px -18px rgba(8,27,48,.34);'
    + 'transition:transform .25s cubic-bezier(.2,.8,.3,1.2),box-shadow .25s}'
    + '.udc-launch:hover{transform:translateY(-3px);box-shadow:0 10px 22px -8px rgba(8,27,48,.26),0 32px 64px -20px rgba(8,27,48,.42)}'
    + '.udc-lava{position:relative;width:44px;height:44px;border-radius:50%;background:linear-gradient(140deg,#C53030 10%,#8E1A1A 90%);'
    + 'display:grid;place-items:center;color:#fff;font:800 1.05rem/1 Sora,Inter,sans-serif;letter-spacing:-.02em;flex:none;'
    + 'box-shadow:0 1px 0 rgba(255,255,255,.25) inset,0 6px 14px -5px rgba(155,28,28,.7)}'
    + '.udc-lava::after{content:"";position:absolute;right:1px;bottom:1px;width:11px;height:11px;border-radius:50%;background:#10B981;border:2.5px solid #fff}'
    + '.udc-ltxt{display:flex;flex-direction:column;line-height:1.15;text-align:left}'
    + '.udc-ltxt b{font-size:.92rem;font-weight:700;color:#0E1B2C;letter-spacing:-.01em}'
    + '.udc-ltxt span{font-size:.74rem;color:#67748E;font-weight:500}'
    /* ---- panel ---- */
    + '.udc-panel{position:fixed;right:24px;bottom:24px;z-index:9991;width:min(400px,calc(100vw - 24px));height:min(620px,calc(100vh - 48px));'
    + 'background:#fff;border-radius:22px;box-shadow:0 8px 20px -8px rgba(8,27,48,.25),0 44px 110px -28px rgba(8,27,48,.6),0 0 0 1px rgba(8,27,48,.05);'
    + 'display:none;flex-direction:column;overflow:hidden;font-family:Inter,system-ui,sans-serif}'
    + '.udc-panel.open{display:flex;animation:udcIn .32s cubic-bezier(.2,.85,.25,1.08)}'
    + '@keyframes udcIn{from{opacity:0;transform:translateY(18px) scale(.97)}to{opacity:1;transform:none}}'
    /* ---- header ---- */
    + '.udc-head{position:relative;background:linear-gradient(135deg,#0E2A4D 0%,#081B30 78%);color:#fff;padding:1.15rem 1.2rem 1.05rem;display:flex;align-items:center;gap:.85rem}'
    + '.udc-head::before{content:"";position:absolute;top:0;left:0;right:0;height:3px;background:linear-gradient(90deg,#C53030,#E89A9A 55%,#C53030)}'
    + '.udc-head::after{content:"";position:absolute;inset:0;background:radial-gradient(75% 130% at 88% -20%,rgba(197,48,48,.28),transparent 60%);pointer-events:none}'
    + '.udc-ava{position:relative;width:42px;height:42px;border-radius:50%;background:linear-gradient(140deg,#C53030 10%,#8E1A1A 90%);flex:none;'
    + 'display:grid;place-items:center;font:800 1rem/1 Sora,Inter,sans-serif;color:#fff;box-shadow:0 1px 0 rgba(255,255,255,.25) inset,0 4px 12px -4px rgba(0,0,0,.5)}'
    + '.udc-ava::after{content:"";position:absolute;right:0;bottom:0;width:11px;height:11px;border-radius:50%;background:#10B981;border:2.5px solid #0A2240}'
    + '.udc-head .t{flex:1;min-width:0;position:relative;z-index:1}'
    + '.udc-head .n{font:700 1.02rem/1.2 Sora,Inter,sans-serif;letter-spacing:-.015em}'
    + '.udc-head .s{font-size:.76rem;color:#9DB3D6;margin-top:.18rem;font-weight:500}'
    + '.udc-head .s b{color:#7CE3B8;font-weight:600}'
    + '.udc-x{position:relative;z-index:1;background:rgba(255,255,255,.08);border:none;color:#C5D4EC;cursor:pointer;width:32px;height:32px;border-radius:9px;display:grid;place-items:center;transition:.18s}'
    + '.udc-x:hover{background:rgba(255,255,255,.16);color:#fff}'
    + '.udc-x svg{width:14px;height:14px;stroke:currentColor;stroke-width:2.4;stroke-linecap:round}'
    /* ---- body ---- */
    + '.udc-body{flex:1;overflow-y:auto;padding:1.25rem 1.1rem;background:linear-gradient(180deg,#F4F7FC,#EEF2F9);display:flex;flex-direction:column;gap:.4rem;scrollbar-width:thin;scrollbar-color:#C9D4E8 transparent}'
    + '.udc-day{align-self:center;font-size:.68rem;font-weight:600;color:#9AA7BF;letter-spacing:.1em;text-transform:uppercase;margin-bottom:.4rem}'
    + '.udc-row-a{display:flex;gap:.55rem;align-items:flex-end;max-width:88%;align-self:flex-start;animation:udcMsg .3s cubic-bezier(.2,.8,.3,1.05)}'
    + '.udc-mava{width:26px;height:26px;border-radius:50%;background:linear-gradient(140deg,#C53030,#8E1A1A);color:#fff;font:800 .68rem/1 Sora,Inter,sans-serif;display:grid;place-items:center;flex:none;margin-bottom:2px}'
    + '@keyframes udcMsg{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:none}}'
    + '.udc-m{padding:.78rem 1rem;border-radius:18px;font-size:.92rem;line-height:1.55;white-space:pre-wrap;word-wrap:break-word;letter-spacing:-.005em}'
    + '.udc-m.a{background:#fff;color:#1A2740;border-bottom-left-radius:6px;box-shadow:0 1px 2px rgba(8,27,48,.06),0 6px 18px -8px rgba(8,27,48,.14)}'
    + '.udc-m.u{background:linear-gradient(160deg,#C53030,#9B1C1C);color:#fff;border-bottom-right-radius:6px;align-self:flex-end;max-width:84%;'
    + 'box-shadow:0 1px 0 rgba(255,255,255,.18) inset,0 8px 20px -8px rgba(155,28,28,.55);animation:udcMsg .3s cubic-bezier(.2,.8,.3,1.05);margin:.25rem 0}'
    + '.udc-typing{display:flex;gap:5px;padding:.9rem 1.05rem;background:#fff;border-radius:18px;border-bottom-left-radius:6px;width:max-content;box-shadow:0 1px 2px rgba(8,27,48,.06),0 6px 18px -8px rgba(8,27,48,.14)}'
    + '.udc-typing i{width:7px;height:7px;border-radius:50%;background:#B32424;opacity:.45;animation:udcB 1.15s infinite}'
    + '.udc-typing i:nth-child(2){animation-delay:.14s}.udc-typing i:nth-child(3){animation-delay:.28s}'
    + '@keyframes udcB{0%,60%,100%{transform:none;opacity:.35}30%{transform:translateY(-5px);opacity:.9}}'
    /* ---- chips ---- */
    + '.udc-chips{display:flex;flex-direction:column;gap:.45rem;padding:.5rem 0 .2rem;align-self:stretch;animation:udcMsg .35s .1s both cubic-bezier(.2,.8,.3,1.05)}'
    + '.udc-chip{display:flex;align-items:center;gap:.6rem;background:#fff;border:1.5px solid #E2E9F4;color:#1A2740;border-radius:13px;'
    + 'padding:.7rem .95rem;font:600 .85rem Inter,system-ui,sans-serif;cursor:pointer;transition:.18s;text-align:left;letter-spacing:-.01em}'
    + '.udc-chip::before{content:"";width:6px;height:6px;border-radius:50%;background:#C53030;flex:none;transition:.18s}'
    + '.udc-chip:hover{border-color:#C53030;box-shadow:0 6px 16px -8px rgba(179,36,36,.35);transform:translateX(2px)}'
    /* ---- footer ---- */
    + '.udc-foot{border-top:1px solid #ECF1F8;background:#fff;padding:.85rem .9rem .7rem}'
    + '.udc-row{display:flex;gap:.55rem;align-items:flex-end;background:#F4F7FC;border:1.5px solid #E2E9F4;border-radius:15px;padding:.3rem .3rem .3rem .95rem;transition:.2s}'
    + '.udc-row:focus-within{border-color:#C53030;box-shadow:0 0 0 4px rgba(179,36,36,.09);background:#fff}'
    + '.udc-in{flex:1;resize:none;border:none;background:transparent;padding:.55rem 0;font:400 .93rem/1.5 Inter,system-ui,sans-serif;color:#0E1B2C;max-height:96px;outline:none}'
    + '.udc-send{background:linear-gradient(160deg,#C53030,#9B1C1C);border:none;color:#fff;width:40px;height:40px;border-radius:11px;cursor:pointer;display:grid;place-items:center;flex:none;'
    + 'box-shadow:0 1px 0 rgba(255,255,255,.2) inset,0 6px 14px -6px rgba(155,28,28,.7);transition:transform .18s,box-shadow .2s}'
    + '.udc-send:hover{transform:translateY(-1px);box-shadow:0 1px 0 rgba(255,255,255,.2) inset,0 10px 18px -7px rgba(155,28,28,.85)}'
    + '.udc-send svg{width:17px;height:17px;stroke:#fff;fill:none;stroke-width:2.2;stroke-linecap:round;stroke-linejoin:round}'
    + '.udc-sub{display:flex;justify-content:space-between;align-items:center;margin-top:.6rem;padding:0 .2rem;font-size:.72rem;color:#9AA7BF;font-weight:500}'
    + '.udc-sub a{color:#B32424;font-weight:700;text-decoration:none;letter-spacing:-.01em}'
    + '@media(max-width:480px){.udc-panel{right:10px;bottom:10px;border-radius:18px}.udc-launch{right:16px;bottom:16px}}';

  var st = document.createElement('style'); st.textContent = css; document.head.appendChild(st);

  var launch = document.createElement('button');
  launch.className = 'udc-launch';
  launch.setAttribute('aria-label', 'Open live chat with ' + NAME);
  launch.innerHTML = '<span class="udc-lava">' + MONO + '</span><span class="udc-ltxt"><b>Chat with ' + NAME + '</b><span>Online now &middot; replies in seconds</span></span>';
  document.body.appendChild(launch);

  var panel = document.createElement('div');
  panel.className = 'udc-panel';
  panel.innerHTML =
    '<div class="udc-head"><span class="udc-ava">' + MONO + '</span>' +
    '<div class="t"><div class="n">' + NAME + '</div>' +
    '<div class="s">' + ROLE + ' at United Developers &middot; <b>Online</b></div></div>' +
    '<button class="udc-x" aria-label="Close chat"><svg viewBox="0 0 24 24"><path d="M6 6l12 12M18 6 6 18"/></svg></button></div>' +
    '<div class="udc-body"><div class="udc-day">United Developers &middot; Live</div></div>' +
    '<div class="udc-foot"><div class="udc-row">' +
    '<textarea class="udc-in" rows="1" placeholder="Ask about your roof, claim, or quote..."></textarea>' +
    '<button class="udc-send" aria-label="Send"><svg viewBox="0 0 24 24"><path d="M22 2 11 13"/><path d="M22 2 15 22l-4-9-9-4 20-7z"/></svg></button>' +
    '</div><div class="udc-sub"><span>Licensed &amp; bonded MD &middot; VA &middot; PA</span><a href="tel:+12408802108">Call (240) 880-2108</a></div></div>';
  document.body.appendChild(panel);

  var body = panel.querySelector('.udc-body');
  var input = panel.querySelector('.udc-in');
  var sendBtn = panel.querySelector('.udc-send');

  var ws = null, wsReady = false, typingEl = null;
  var hist = []; try { hist = JSON.parse(sessionStorage.getItem('udcHist') || '[]'); } catch (_) {}
  var greeted = hist.length > 0;
  var leadSent = sessionStorage.getItem('udcLead') === '1';

  function persist(w, t) {
    hist.push({ w: w, t: t });
    if (hist.length > 40) hist = hist.slice(-40);
    try { sessionStorage.setItem('udcHist', JSON.stringify(hist)); } catch (_) {}
  }
  function captureLead(text) {
    if (leadSent) return;
    var m = text.match(/(\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4})/);
    if (!m) return;
    leadSent = true; try { sessionStorage.setItem('udcLead', '1'); } catch (_) {}
    var transcript = hist.slice(-14).map(function (x) { return (x.w === 'u' ? 'Visitor: ' : NAME + ': ') + x.t; }).join('\n');
    var ld = { phone: m[1], agent: NAME, page: location.pathname, transcript: transcript, ts: new Date().toISOString() };
    var sj = 'UD CHAT LEAD: phone captured by ' + NAME;
    if (window.UD && UD.lead) { UD.lead(ld, sj); }
    else { fetch('https://formsubmit.co/ajax/' + ((window.UD_CONFIG && UD_CONFIG.LEAD_EMAIL) || 'trainyouragent@gmail.com'), { method: 'POST',
      headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
      body: JSON.stringify(Object.assign({ _subject: sj, _template: 'table' }, ld)) }).catch(function () {}); }
  }

  function el(cls, txt) { var d = document.createElement('div'); d.className = cls; if (txt) d.textContent = txt; return d; }
  function scrollDn() { body.scrollTop = body.scrollHeight; }
  function showTyping() {
    if (typingEl) return;
    typingEl = el('udc-row-a');
    typingEl.innerHTML = '<span class="udc-mava">' + MONO + '</span><div class="udc-typing"><i></i><i></i><i></i></div>';
    body.appendChild(typingEl); scrollDn();
  }
  function hideTyping() { if (typingEl) { typingEl.remove(); typingEl = null; } }
  function agentSay(t) {
    hideTyping();
    var row = el('udc-row-a');
    var av = document.createElement('span'); av.className = 'udc-mava'; av.textContent = MONO;
    row.appendChild(av); row.appendChild(el('udc-m a', t));
    body.appendChild(row); scrollDn();
  }
  function agentSayP(t) { agentSay(t); persist('a', t); }
  function userSay(t) { body.appendChild(el('udc-m u', t)); scrollDn(); }
  function userSayP(t) { userSay(t); persist('u', t); captureLead(t); }

  function chips() {
    var wrap = el('udc-chips');
    var qs = IS_DEX
      ? ['What does a new roof actually cost?', 'Will my insurance cover the damage?', 'Book my free inspection', 'What financing do you offer?']
      : ['Book a free roof inspection', 'I think I have storm damage', 'I have an active leak right now', 'Question about an insurance claim'];
    qs.forEach(function (q) {
      var c = document.createElement('button'); c.className = 'udc-chip'; c.textContent = q;
      c.onclick = function () { wrap.remove(); send(q); };
      wrap.appendChild(c);
    });
    body.appendChild(wrap); scrollDn();
  }

  function connect(cb) {
    if (ws && wsReady) { cb && cb(); return; }
    ws = new WebSocket('wss://api.elevenlabs.io/v1/convai/conversation?agent_id=' + AGENT);
    ws.onopen = function () {
      ws.send(JSON.stringify({ type: 'conversation_initiation_client_data', conversation_config_override: { conversation: { text_only: true } } }));
    };
    ws.onmessage = function (e) {
      var d; try { d = JSON.parse(e.data); } catch (_) { return; }
      if (d.type === 'conversation_initiation_metadata') { wsReady = true; cb && cb(); }
      else if (d.type === 'agent_response') {
        var t = d.agent_response_event && d.agent_response_event.agent_response;
        if (t) { if (!greeted) { greeted = true; agentSayP(t); chips(); } else { agentSayP(t); } }
      }
      else if (d.type === 'ping') { ws.send(JSON.stringify({ type: 'pong', event_id: d.ping_event.event_id })); }
    };
    ws.onclose = function () { wsReady = false; };
    ws.onerror = function () { hideTyping(); if (greeted) agentSay("Sorry — connection hiccup on my end. Call us at (240) 880-2108 and a real person picks up."); };
  }

  function send(text) {
    text = (text || '').trim(); if (!text) return;
    userSayP(text); showTyping();
    var fire = function () { ws.send(JSON.stringify({ type: 'user_message', text: text })); };
    if (wsReady) fire(); else connect(fire);
  }

  var restored = false;
  launch.onclick = function () {
    launch.style.display = 'none'; panel.classList.add('open');
    if (greeted && !restored) {
      restored = true;
      hist.forEach(function (x) { x.w === 'u' ? userSay(x.t) : agentSay(x.t); });
    }
    if (!greeted) { showTyping(); connect(); }
    setTimeout(function () { input.focus(); }, 280);
  };
  panel.querySelector('.udc-x').onclick = function () { panel.classList.remove('open'); launch.style.display = 'flex'; };
  sendBtn.onclick = function () { send(input.value); input.value = ''; input.style.height = ''; };
  input.addEventListener('keydown', function (e) {
    if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); sendBtn.onclick(); }
  });
  input.addEventListener('input', function () { input.style.height = ''; input.style.height = Math.min(input.scrollHeight, 96) + 'px'; });

  /* ---- mobile sticky action bar ---- */
  var isCareers = location.pathname.indexOf('careers') > -1;
  var inAreas = /\/(areas|services)\//.test(location.pathname);
  var barCss = ''
    + '.udc-bar{display:none}'
    + '@media(max-width:640px){'
    + '.udc-bar{position:fixed;left:0;right:0;bottom:0;z-index:9989;display:flex;gap:.55rem;padding:.6rem .75rem calc(.6rem + env(safe-area-inset-bottom));'
    + 'background:rgba(255,255,255,.96);backdrop-filter:blur(14px);border-top:1px solid rgba(8,27,48,.09);box-shadow:0 -12px 32px -16px rgba(8,27,48,.3)}'
    + '.udc-bar a{flex:1;display:flex;align-items:center;justify-content:center;gap:.5rem;border-radius:12px;padding:.85rem .5rem;'
    + 'font:700 .9rem Inter,system-ui,sans-serif;text-decoration:none;letter-spacing:-.01em}'
    + '.udc-bar .c{background:#0E2A4D;color:#fff}'
    + '.udc-bar .q{background:linear-gradient(160deg,#C53030,#9B1C1C);color:#fff;box-shadow:0 8px 18px -8px rgba(155,28,28,.6)}'
    + '.udc-bar svg{width:16px;height:16px;stroke:#fff;fill:none;stroke-width:2.2;stroke-linecap:round;stroke-linejoin:round}'
    + '.udc-launch{bottom:calc(78px + env(safe-area-inset-bottom)) !important;right:14px}'
    + '.udc-panel{bottom:calc(78px + env(safe-area-inset-bottom)) !important;height:min(540px,calc(100vh - 150px))}'
    + '}';
  var bst = document.createElement('style'); bst.textContent = barCss; document.head.appendChild(bst);
  var bar = document.createElement('div'); bar.className = 'udc-bar';
  var phoneSvg = '<svg viewBox="0 0 24 24"><path d="M5 3h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 12l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 5a2 2 0 0 1 2-2z"/></svg>';
  bar.innerHTML = isCareers
    ? '<a class="c" href="tel:+12408802108">' + phoneSvg + 'Call Us</a><a class="q" href="#apply">Apply Now</a>'
    : '<a class="c" href="tel:+12408802108">' + phoneSvg + 'Call Now</a><a class="q" href="' + (inAreas ? '../' : '') + 'index.html#quote">Free Inspection</a>';
  document.body.appendChild(bar);

  /* ---- lazy-load below-fold images ---- */
  document.querySelectorAll('img').forEach(function (im) {
    if (!im.closest('header') && im.getBoundingClientRect().top > window.innerHeight) im.loading = 'lazy';
  });
})();
