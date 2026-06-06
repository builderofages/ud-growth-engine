/* UD Live Chat — branded client for United Developers' ElevenLabs agents.
   Replaces the stock widget launcher with an on-brand panel. Voice calls
   hand off to the hidden ElevenLabs widget. No dependencies. */
(function () {
  'use strict';
  var host = document.querySelector('elevenlabs-convai');
  var AGENT = host ? host.getAttribute('agent-id') : 'agent_2801ktf0hpcefj1bmz3gp0akkxp1';
  var IS_DEX = AGENT === 'agent_0701ktfcsjtkfw3rtja6nbf06ns7';
  var NAME = IS_DEX ? 'Dex' : 'Riley';
  var ROLE = IS_DEX ? 'Roofing Specialist' : 'Front Desk';
  var inAreas = location.pathname.indexOf('/areas/') > -1;
  var LOGO = (inAreas ? '../' : '') + 'assets/logo-white.png';

  /* hide the stock launcher; keep element alive for voice handoff */
  if (host) host.style.display = 'none';

  var css = ''
    + '.udc-launch{position:fixed;right:22px;bottom:22px;z-index:9990;display:flex;align-items:center;gap:.6rem;'
    + 'background:linear-gradient(180deg,#C53030,#9B1C1C);color:#fff;border:none;cursor:pointer;border-radius:999px;'
    + 'padding:.95rem 1.45rem;font:600 .95rem/1 Inter,system-ui,sans-serif;letter-spacing:-.01em;'
    + 'box-shadow:0 18px 40px -14px rgba(155,28,28,.65),0 2px 0 rgba(255,255,255,.18) inset;transition:transform .22s,box-shadow .25s}'
    + '.udc-launch:hover{transform:translateY(-2px);box-shadow:0 24px 48px -16px rgba(155,28,28,.8),0 2px 0 rgba(255,255,255,.18) inset}'
    + '.udc-launch svg{width:18px;height:18px;stroke:#fff;fill:none;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}'
    + '.udc-panel{position:fixed;right:22px;bottom:22px;z-index:9991;width:min(392px,calc(100vw - 24px));height:min(580px,calc(100vh - 48px));'
    + 'background:#fff;border-radius:20px;box-shadow:0 32px 80px -24px rgba(8,27,48,.55),0 0 0 1px rgba(8,27,48,.06);'
    + 'display:none;flex-direction:column;overflow:hidden;font-family:Inter,system-ui,sans-serif}'
    + '.udc-panel.open{display:flex;animation:udcIn .28s cubic-bezier(.2,.9,.3,1.1)}'
    + '@keyframes udcIn{from{opacity:0;transform:translateY(14px) scale(.98)}to{opacity:1;transform:none}}'
    + '.udc-head{background:linear-gradient(135deg,#0C2440,#081B30);color:#fff;padding:1rem 1.1rem;display:flex;align-items:center;gap:.8rem}'
    + '.udc-head img{height:30px;width:auto;filter:brightness(0) invert(1)}'
    + '.udc-head .t{flex:1;min-width:0}'
    + '.udc-head .n{font-weight:700;font-size:.98rem;letter-spacing:-.01em}'
    + '.udc-head .s{font-size:.74rem;color:#9DB3D6;display:flex;align-items:center;gap:.35rem;margin-top:.15rem}'
    + '.udc-dot{width:7px;height:7px;border-radius:50%;background:#10B981;box-shadow:0 0 0 3px rgba(16,185,129,.25)}'
    + '.udc-x{background:none;border:none;color:#9DB3D6;cursor:pointer;font-size:1.25rem;line-height:1;padding:.3rem .45rem;border-radius:8px}'
    + '.udc-x:hover{background:rgba(255,255,255,.1);color:#fff}'
    + '.udc-body{flex:1;overflow-y:auto;padding:1.1rem;background:#F7F9FD;display:flex;flex-direction:column;gap:.65rem}'
    + '.udc-m{max-width:84%;padding:.7rem .95rem;border-radius:16px;font-size:.92rem;line-height:1.5;white-space:pre-wrap;word-wrap:break-word}'
    + '.udc-m.a{background:#fff;color:#0E1B2C;border:1px solid #E4EAF4;border-bottom-left-radius:6px;align-self:flex-start;box-shadow:0 2px 8px -4px rgba(8,27,48,.12)}'
    + '.udc-m.u{background:linear-gradient(180deg,#C53030,#9B1C1C);color:#fff;border-bottom-right-radius:6px;align-self:flex-end}'
    + '.udc-who{font-size:.68rem;font-weight:600;color:#8C97AF;margin:-.1rem 0 -.35rem .3rem;align-self:flex-start;text-transform:uppercase;letter-spacing:.08em}'
    + '.udc-typing{display:flex;gap:5px;padding:.85rem 1rem;background:#fff;border:1px solid #E4EAF4;border-radius:16px;border-bottom-left-radius:6px;align-self:flex-start;width:max-content}'
    + '.udc-typing i{width:7px;height:7px;border-radius:50%;background:#B6C2D9;animation:udcB 1.2s infinite}'
    + '.udc-typing i:nth-child(2){animation-delay:.15s}.udc-typing i:nth-child(3){animation-delay:.3s}'
    + '@keyframes udcB{0%,60%,100%{transform:none;opacity:.5}30%{transform:translateY(-5px);opacity:1}}'
    + '.udc-chips{display:flex;flex-wrap:wrap;gap:.45rem;padding:.2rem 0}'
    + '.udc-chip{background:#fff;border:1.5px solid #E4EAF4;color:#0E1B2C;border-radius:999px;padding:.5rem .9rem;font:500 .8rem Inter,system-ui,sans-serif;cursor:pointer;transition:.18s}'
    + '.udc-chip:hover{border-color:#C53030;color:#B32424}'
    + '.udc-foot{border-top:1px solid #EDF1F8;background:#fff;padding:.8rem}'
    + '.udc-row{display:flex;gap:.55rem;align-items:flex-end}'
    + '.udc-in{flex:1;resize:none;border:1.5px solid #E4EAF4;border-radius:13px;padding:.72rem .9rem;font:400 .92rem/1.45 Inter,system-ui,sans-serif;color:#0E1B2C;max-height:96px;outline:none;background:#FBFCFE}'
    + '.udc-in:focus{border-color:#C53030;box-shadow:0 0 0 4px rgba(179,36,36,.1);background:#fff}'
    + '.udc-send{background:linear-gradient(180deg,#C53030,#9B1C1C);border:none;color:#fff;width:42px;height:42px;border-radius:12px;cursor:pointer;display:grid;place-items:center;flex:none;transition:transform .18s}'
    + '.udc-send:hover{transform:translateY(-1px)}'
    + '.udc-send svg{width:18px;height:18px;stroke:#fff;fill:none;stroke-width:2.2;stroke-linecap:round;stroke-linejoin:round}'
    + '.udc-sub{display:flex;justify-content:space-between;align-items:center;margin-top:.55rem;font-size:.72rem;color:#8C97AF}'
    + '.udc-sub a{color:#B32424;font-weight:600;text-decoration:none}'
    + '@media(max-width:480px){.udc-panel{right:12px;bottom:12px;border-radius:16px}}';

  var st = document.createElement('style'); st.textContent = css; document.head.appendChild(st);

  var launch = document.createElement('button');
  launch.className = 'udc-launch';
  launch.setAttribute('aria-label', 'Open live chat');
  launch.innerHTML = '<svg viewBox="0 0 24 24"><path d="M21 11.5a8.5 8.5 0 0 1-8.5 8.5c-1.5 0-2.9-.37-4.1-1L3 20l1.1-4.4A8.5 8.5 0 1 1 21 11.5z"/></svg>Questions? Chat with us';
  document.body.appendChild(launch);

  var panel = document.createElement('div');
  panel.className = 'udc-panel';
  panel.innerHTML =
    '<div class="udc-head"><img src="' + LOGO + '" alt=""/>' +
    '<div class="t"><div class="n">' + NAME + ' &middot; United Developers</div>' +
    '<div class="s"><span class="udc-dot"></span>' + ROLE + ' &middot; replies in seconds</div></div>' +
    '<button class="udc-x" aria-label="Close chat">&times;</button></div>' +
    '<div class="udc-body"></div>' +
    '<div class="udc-foot"><div class="udc-row">' +
    '<textarea class="udc-in" rows="1" placeholder="Type your question..."></textarea>' +
    '<button class="udc-send" aria-label="Send"><svg viewBox="0 0 24 24"><path d="M22 2 11 13"/><path d="M22 2 15 22l-4-9-9-4 20-7z"/></svg></button>' +
    '</div><div class="udc-sub"><span>Real answers, not scripts</span><a href="tel:+12408802108">Or call (240) 880-2108</a></div></div>';
  document.body.appendChild(panel);

  var body = panel.querySelector('.udc-body');
  var input = panel.querySelector('.udc-in');
  var sendBtn = panel.querySelector('.udc-send');

  var ws = null, wsReady = false, typingEl = null, greeted = false;

  function el(cls, txt) { var d = document.createElement('div'); d.className = cls; if (txt) d.textContent = txt; return d; }
  function scrollDn() { body.scrollTop = body.scrollHeight; }
  function showTyping() { if (typingEl) return; typingEl = el('udc-typing'); typingEl.innerHTML = '<i></i><i></i><i></i>'; body.appendChild(typingEl); scrollDn(); }
  function hideTyping() { if (typingEl) { typingEl.remove(); typingEl = null; } }
  function agentSay(t) { hideTyping(); body.appendChild(el('udc-who', NAME)); body.appendChild(el('udc-m a', t)); scrollDn(); }
  function userSay(t) { body.appendChild(el('udc-m u', t)); scrollDn(); }

  function chips() {
    var wrap = el('udc-chips');
    var qs = IS_DEX
      ? ['What does a new roof cost?', 'Will insurance cover my roof?', 'I want a free inspection', 'Financing options']
      : ['Book a free inspection', 'I think I have storm damage', 'I have an active leak', 'Question about my claim'];
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
        if (t) { if (!greeted) { greeted = true; agentSay(t); chips(); } else { agentSay(t); } }
      }
      else if (d.type === 'ping') { ws.send(JSON.stringify({ type: 'pong', event_id: d.ping_event.event_id })); }
    };
    ws.onclose = function () { wsReady = false; };
    ws.onerror = function () { hideTyping(); if (greeted) agentSay("Sorry — connection hiccup. Call us at (240) 880-2108 and a real person picks up."); };
  }

  function send(text) {
    text = (text || '').trim(); if (!text) return;
    userSay(text); showTyping();
    var fire = function () { ws.send(JSON.stringify({ type: 'user_message', text: text })); };
    if (wsReady) fire(); else connect(fire);
  }

  launch.onclick = function () {
    launch.style.display = 'none'; panel.classList.add('open');
    if (!greeted) { showTyping(); connect(); }
    setTimeout(function () { input.focus(); }, 250);
  };
  panel.querySelector('.udc-x').onclick = function () { panel.classList.remove('open'); launch.style.display = 'flex'; };
  sendBtn.onclick = function () { send(input.value); input.value = ''; input.style.height = ''; };
  input.addEventListener('keydown', function (e) {
    if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); sendBtn.onclick(); }
  });
  input.addEventListener('input', function () { input.style.height = ''; input.style.height = Math.min(input.scrollHeight, 96) + 'px'; });
})();
