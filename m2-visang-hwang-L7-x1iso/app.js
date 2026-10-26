/* 데일리 학습 패키지 엔진 — 과별 데이터(window.PKG)만 바꾸면 그대로 재사용
   탭: 오늘의 학습(DAY 세트, 순서대로·점수·문자) / 본문 / 유형별 연습(자유, 점수 미반영)
   이어하기: DAY 세트는 문제 하나 풀 때마다 저장 → 나갔다 와도 그 문제부터 */
(function () {
  'use strict';
  var P = window.PKG;
  /* 주요 문장 스크램블: 어법선택에 나온 문장(핵심 문법이 들어간 본문 문장)으로 스크램블을 만든다 (선생님 요청).
     문장이 3개보다 적으면 데이터의 원래 문장을 쓴다. 예전 기록의 '본문 스크램블' 점수는 migrate에서 이어 붙인다. */
  var HS = /^고/.test(P.school || '');
  P.days.forEach(function (d) {
    var nz = function (x) { return String(x).toLowerCase().replace(/[’‘`]/g, "'").replace(/\s+/g, ' ').trim(); };
    var unq = function (x) { return String(x).trim().replace(/^["“]/, '').replace(/["”]$/, '').trim(); };
    var lines = d.passage.filter(function (l) { return l[0] !== '#' && l[2] && !(/^[❶-❿]$/.test(l[1])); }), picked = [], exOf = {}, gapOf = {};
    /* 고등: 문장 전체 스크램블 대신 문법 포인트(어법선택 정답 자리)가 있는 3~4단어만 비워서 채우기 */
    var gapAt = function (q, t) {
      var m = /\{([^}|]*)\|[^}]*\}/.exec(q.s); if (!m) return null;
      var pre = nz(q.s.slice(0, m.index).replace(/\{([^}|]*)[^}]*\}/g, '$1')), full = nz(q.s.replace(/\{([^}|]*)[^}]*\}/g, '$1')).replace(/^\(|\)$/g, '').replace(/[.!?"]+$/, '');
      var T = nz(t), off = T.indexOf(full); if (off < 0) return null;
      var pos = off + (pre ? pre.length + (/\s$/.test(q.s.slice(0, m.index)) ? 1 : 0) : 0);
      var ws = T.slice(0, pos).split(' ').length - 1, n = nz(m[1]).split(' ').length, W = T.split(' ').length;
      var Wd = String(t).trim().split(/\s+/), FN = /^(a|an|the|of|to|in|on|at|for|with|by|from|our|their|my|your|his|her|its|and|or|but|that|as|some|any)$/i;
      var a = ws, b = Math.min(W - 1, ws + Math.min(n, 4) - 1), goal = Math.min(4, Math.max(3, n));
      var right = function () { return b < W - 1 && !/[,;:]$/.test(Wd[b]); };
      while (b - a + 1 < goal) { if (right()) b++; else if (a > 0) a--; else break; }
      if (b - a + 1 < 4 && FN.test(String(Wd[b]).replace(/[^a-z']/gi, '')) && right()) b++; /* 'to eat a' → 'to eat a sandwich' */
      return b - a + 1 >= 3 ? [a, b] : null;
    };
    d.steps.forEach(function (st) {
      if (st.type !== 'pick' || !/어법/.test(st.title)) return;
      st.items.forEach(function (q) {
        var f = nz(q.s.replace(/\{([^}|]*)[^}]*\}/, '$1')).replace(/^\(|\)$/g, '').replace(/[.!?"]+$/, '');
        lines.forEach(function (l, i) { var t = unq(l[1]), w = t.split(/\s+/).length; if (w >= 5 && w <= 24 && /[.!?]$/.test(t) && !/["“”]/.test(t) && nz(t).indexOf(f) >= 0) { if (picked.indexOf(i) < 0) picked.push(i); if (q.ex) exOf[i] = (exOf[i] ? exOf[i] + '\n\n' : '') + q.ex; if (!gapOf[i]) gapOf[i] = gapAt(q, t); } });
      });
    });
    picked.sort(function (a, b) { return a - b; });
    if (picked.length > 7) { var keep = [], stepN = picked.length / 7; for (var k = 0; k < 7; k++) keep.push(picked[Math.floor(k * stepN)]); picked = keep; }
    d.steps.forEach(function (st) {
      if (st.type !== 'scramble') return;
      st.title = '주요 문장 스크램블'; st.guide = HS ? '문법 포인트가 들어간 3~4단어가 비어 있어요. 우리말을 보고 단어를 순서대로 눌러 빈칸을 채우세요.' : '핵심 문법이 들어간 문장이에요. 우리말에 맞게 단어를 눌러 문장을 완성하세요.';
      if (picked.length >= 3) st.items = picked.map(function (i) { return { ko: unq(lines[i][2]), en: unq(lines[i][1]), gap: gapOf[i] || null, ex: exOf[i] ? '이 문장의 문법 포인트\n' + exOf[i] : '' }; });
    });
  });
  var KEY = 'daily:' + P.id;
  /* 카톡 안 브라우저 감지: 기록이 지워질 수 있어 크롬·사파리로 열도록 안내 */
  var IN_APP = false; /* 카톡 안내 꺼짐: 대부분 카톡으로 학습 (선생님 요청) */
  var LINKS = {}; /* 예전 claude.ai 사본 주소는 더 쓰지 않음 → 지금 주소(GitHub)를 그대로 바깥 브라우저로 연다 */
  function hereURL() { return location.protocol === 'https:' ? location.origin + location.pathname : ''; }
  /* 브라우저가 저장 공간을 함부로 지우지 않도록 요청 */
  try { if (navigator.storage && navigator.storage.persist) navigator.storage.persist().catch(function () {}); } catch (e) {}
  var app = document.getElementById('app');
  var CIRC = '①②③④⑤⑥⑦⑧⑨⑩';
  var SHORT = { vocab: '어휘', tf: 'TF', verb: '동사변형', error: '오류찾기', order: '문장순서', scramble: '주요문장', mc: '문법', insert: '삽입', odd: '어색한문장', blank: '빈칸' };

  /* ---------- 저장 ---------- */
  /* 학생별 저장: 같은 기기(학원 아이패드)를 여러 학생이 써도 기록이 섞이지 않게 이름마다 따로 저장한다.
     daily:<단원>:<이름> = 그 학생 기록, daily:roster = 이 기기에서 쓴 이름 목록, daily:who = 마지막 학생 */
  function lsGet(k) { try { return localStorage.getItem(k); } catch (e) { return null; } }
  function lsSet(k, v) { try { localStorage.setItem(k, v); } catch (e) {} }
  function roster() { try { return JSON.parse(lsGet('daily:roster')) || []; } catch (e) { return []; } }
  function addRoster(n) { var r = roster().filter(function (x) { return x !== n; }); r.unshift(n); lsSet('daily:roster', JSON.stringify(r.slice(0, 60))); }
  function dropRoster(n) { lsSet('daily:roster', JSON.stringify(roster().filter(function (x) { return x !== n; }))); if (lsGet('daily:who') === n) lsSet('daily:who', ''); }
  (function legacy() { /* 예전 방식(daily:<단원> 하나) 기록을 그 학생 이름 칸으로 옮긴다 */
    var old = lsGet(KEY); if (!old) return;
    try { var o = JSON.parse(old); if (o && o.name) { if (!lsGet(KEY + ':' + o.name)) lsSet(KEY + ':' + o.name, old); addRoster(o.name); if (!lsGet('daily:who')) lsSet('daily:who', o.name); } localStorage.removeItem(KEY); } catch (e) {}
  })();
  function load(n) { var o = null; if (n) { try { o = JSON.parse(lsGet(KEY + ':' + n)); } catch (e) {} } o = o || {}; o.days = o.days || {}; o.name = n || ''; if (n) legacyMerge(o); return o; }
  /* 모의고사를 번호별로 나누기 전(예전 DAY)의 완료 기록 → 새 번호에 '이전 완료'로 남김. P.legacy = { key: 예전 저장 이름(주소가 바뀐 경우), map: { 예전 DAY id: [새 번호 id…] } } */
  function legacyMerge(o) {
    var Lg = P.legacy, ver = Lg && Lg.v || 1; if (!Lg || !Lg.map || o.legacyDone === ver || (ver === 1 && o.legacyDone === true)) return;
    var src = o; if (Lg.key) { try { src = JSON.parse(lsGet(Lg.key + ':' + o.name)); } catch (e) { src = null; } }
    if (src && src.days) Object.keys(Lg.map).forEach(function (oid) {
      var od = src.days[oid]; if (!od) return;
      var ent = (od.history || []).slice(), c = 0, t = 0;
      Object.keys(od.scores || {}).forEach(function (k) { c += od.scores[k][0]; t += od.scores[k][1]; });
      if (od.finished) ent.push({ c: c, t: t, pct: t ? Math.round(c / t * 100) : 0, finished: od.finished, review: od.reviewDone || null });
      ent.forEach(function (e) { Lg.map[oid].forEach(function (nid) {
        var dd = P.days.filter(function (x) { return x.id === nid; })[0]; if (!dd) return;
        var nd = o.days[nid] || (o.days[nid] = { scores: {}, wrong: {}, started: null, finished: null, run: null, history: [], titles: dd.steps.map(function (x) { return x.title; }) });
        nd.history = nd.history || [];
        if (!nd.history.some(function (h) { return h.finished === e.finished; })) nd.history.push({ c: e.c, t: e.t, pct: e.pct, started: null, finished: e.finished, review: e.review || null, restored: true });
      }); });
    });
    o.legacyDone = ver;
  }
  var S = (function () { var r = roster(), w = lsGet('daily:who'); /* 이름이 하나뿐인 기기(학생 폰)는 바로 그 학생, 여럿이면(아이패드) 매번 고르게 */
    return r.length === 1 ? load(r[0]) : r.length > 1 ? load('') : load(w || ''); })();
  function useStudent(n) { S = load(n); addRoster(n); lsSet('daily:who', n); migrate(); save(); }
  var STORE_OK = (function () { try { var k = KEY + ':t'; localStorage.setItem(k, '1'); var ok = localStorage.getItem(k) === '1'; localStorage.removeItem(k); return ok && !/^file:/.test(location.protocol) || ok && !/\\Temp\\|\/Temp\//i.test(decodeURIComponent(location.pathname)); } catch (e) { return false; } })();
  function save() { if (!S.name) return; try { localStorage.setItem(KEY + ':' + S.name, JSON.stringify(S)); } catch (e) {} }
  /* 단계 구성이 바뀌어도(예: 일치·불일치 추가) 저장된 점수가 엉뚱한 단계로 가지 않게 단계 이름으로 다시 맞춘다.
     예전 기록에 단계 이름이 없으면 PKG.stepsBefore(예전 단계 이름 목록)를 기준으로 삼는다. */
  function migrate() {
    var changed = false;
    P.days.forEach(function (d) {
      var st = S.days[d.id]; if (!st) return;
      var cur = d.steps.map(function (x) { return x.title; });
      var old = (st.titles || P.stepsBefore || cur).map(function (t) { return t === '본문 스크램블' ? '주요 문장 스크램블' : t; });
      if (old.join('|') !== cur.join('|')) {
        var mv = function (o) { var n = {}; Object.keys(o || {}).forEach(function (k) { var j = cur.indexOf(old[k]); if (j >= 0) n[j] = o[k]; }); return n; };
        st.scores = mv(st.scores); st.wrong = mv(st.wrong);
        if (st.run) { var j = cur.indexOf(old[st.run.si]); if (j >= 0) st.run.si = j; else st.run = null; }
        changed = true;
      }
      if (!st.titles || st.titles.join('|') !== cur.join('|')) { st.titles = cur; changed = true; }
    });
    if (changed) save();
  }
  migrate();

  /* ---------- 선생님 구글 시트로 자동 기록 ----------
     ../config.js 의 window.SHEET_URL 로 보낸다. 못 보낸 건 기기에 모아 두었다가 다음에 다시 보낸다(인터넷 끊겨도 안전). */
  var SHEET = window.SHEET_URL || '', OUTK = 'daily:outbox', flushing = false;
  function outbox() { try { return JSON.parse(lsGet(OUTK)) || []; } catch (e) { return []; } }
  function devId() { var d = lsGet('daily:dev'); if (!d) { d = Math.random().toString(36).slice(2, 8); lsSet('daily:dev', d); } return d; }
  function report(kind, d, extra) {
    if (!SHEET || !S.name) return;
    try {
      var st = DS(d.id), g = dayProgress(d), w = [];
      d.steps.forEach(function (s, i) { var ws = st.wrong[i] || []; if (ws.length) w.push(stepShort(s) + '(' + ws.map(function (q) { return q.key; }).join(', ') + ')'); });
      var row = { t: Date.now(), kind: kind, name: S.name, unitId: P.id, school: P.school, unit: P.unit + ' ' + P.title, day: d.name, range: d.range,
        done: g.done, total: d.steps.length, c: g.c, tt: g.t, pct: pctOf(g.c, g.t), attempt: attemptNo(d), finished: !!g.finished,
        review: !g.finished ? '' : !wrongCount(d) ? '틀린 문제 없음' : st.reviewDone ? '완료' : '안 함', wrongN: wrongCount(d),
        started: st.started || 0, ended: st.finished || 0, mins: st.started && st.finished ? Math.max(1, Math.round((st.finished - st.started) / 60000)) : '',
        code: g.finished ? checkCode(d) : '', wrong: g.finished ? w.join(' / ') : '', weak: g.finished ? weakText(d) : '', dev: devId(), step: '', stepScore: '' };
      if (extra) Object.keys(extra).forEach(function (k) { row[k] = extra[k]; });
      var q = outbox(); q.push(row); lsSet(OUTK, JSON.stringify(q.slice(-300)));
    } catch (e) {}
    flush();
  }
  function flush() {
    if (!SHEET || flushing || !window.fetch) return;
    var q = outbox().slice(0, 40); if (!q.length) return;
    flushing = true;
    fetch(SHEET, { method: 'POST', mode: 'no-cors', keepalive: true, headers: { 'Content-Type': 'text/plain;charset=utf-8' }, body: JSON.stringify({ k: window.SHEET_KEY || '', rows: q }) })
      .then(function () { var all = outbox(), sent = {}; q.forEach(function (r) { sent[r.t + r.name + r.kind] = 1; });
        lsSet(OUTK, JSON.stringify(all.filter(function (r) { return !sent[r.t + r.name + r.kind]; }))); flushing = false; if (outbox().length) setTimeout(flush, 500); },
        function () { flushing = false; });
  }
  try { window.addEventListener('online', flush); document.addEventListener('visibilitychange', function () { if (document.visibilityState === 'visible') flush(); }); } catch (e) {}

  /* ---------- 학생 명단 확인 ----------
     선생님 시트의 '학생명단' 탭(이름 · 학생 코드)에 있는 학생만 들어온다. 탭이 비어 있으면 예전처럼 누구나.
     한 번 확인된 학생은 이 기기에 기억(daily:pass) → 인터넷이 잠깐 안 돼도 공부 가능. 열 때마다 다시 확인해서
     선생님이 명단에서 지우면 다음에 열 때부터 막힌다. */
  var PASSK = 'daily:pass', GATE = lsGet('daily:gate') === '1', DENY = {};
  /* daily:pass = { 이름: { c: 코드, u: { 단원id: 확인 시각 } } } — 코드는 기기에 한 번만, 교재(단원)는 따로 확인 */
  function passes() { try { return JSON.parse(lsGet(PASSK)) || {}; } catch (e) { return {}; } }
  function myPass(n) { var x = passes()[n]; return x && x.c ? x : null; }
  function setPass(n, c, unitOk) { var p = passes(), x = p[n] && p[n].c ? p[n] : { c: c, u: {} };
    if (c == null) { delete p[n]; } else { x.c = c; x.u = x.u || {}; if (unitOk === true) x.u[P.id] = Date.now(); else if (unitOk === false) delete x.u[P.id]; p[n] = x; }
    lsSet(PASSK, JSON.stringify(p)); }
  function ncode(c) { return String(c == null ? '' : c).replace(/\D/g, '').replace(/^0+/, ''); }
  function needPass() { if (!GATE || !SHEET || !S.name) return false; var x = myPass(S.name); return !(x && x.u && x.u[P.id]); }
  function checkPass(n, c) { /* → {gate, ok, why}. 시트가 아직 옛 코드면 gate:false. 연결이 안 되면 실패(reject) */
    var u = SHEET + (SHEET.indexOf('?') < 0 ? '?' : '&') + 'check=1&name=' + encodeURIComponent(n || '') + '&code=' + encodeURIComponent(ncode(c)) + '&school=' + encodeURIComponent(P.school || '') + '&_=' + Date.now();
    return fetch(u, { cache: 'no-store' }).then(function (r) { return r.text(); }).then(function (t) {
      var j = null; try { j = JSON.parse(t); } catch (e) {}
      if (!j || typeof j.gate !== 'boolean') j = { gate: false, ok: false };
      GATE = j.gate; lsSet('daily:gate', GATE ? '1' : '');
      return j;
    });
  }
  function applyCheck(n, c, j) { /* 결과를 기기에 기억 */
    if (!j.gate || !n) return;
    if (j.ok) { setPass(n, ncode(c), true); delete DENY[n]; }
    else if (j.why === 'unit') { setPass(n, ncode(c), false); DENY[n] = 'unit'; }
    else { setPass(n, null); DENY[n] = 'code'; }
  }
  function gateSync() { /* 화면을 열 때: 명단이 켜졌는지, 지금 학생이 아직 명단에 있고 이 교재가 열려 있는지 */
    if (!SHEET || !window.fetch) return;
    var n = S.name, pc = n && myPass(n), was = GATE + '|' + needPass() + '|' + (DENY[n] || '');
    checkPass(n, pc ? pc.c : '').then(function (j) {
      if (pc) applyCheck(n, pc.c, j);
      if (was !== GATE + '|' + needPass() + '|' + (DENY[n] || '') && app.querySelector('.bnav, #nameform, #passform')) { var y = window.scrollY; home(); window.scrollTo(0, y); }
    }, function () {});
  }
  function tryEnter(n, c, msg, btn) {
    if (!ncode(c)) { msg.textContent = '선생님께 받은 학생 코드를 적어 주세요.'; msg.hidden = false; return; }
    var old = btn.textContent; btn.disabled = true; btn.textContent = '확인 중…'; msg.hidden = true;
    checkPass(n, c).then(function (j) {
      btn.disabled = false; btn.textContent = old;
      applyCheck(n, c, j);
      if (!j.gate || j.ok) { useStudent(n); home(); return; }
      if (j.why === 'unit') { useStudent(n); home(); return; } /* 코드는 맞음 → '열어 주지 않은 과제' 안내 화면 */
      msg.textContent = '이름이나 학생 코드가 맞지 않아요. 선생님께 확인해 주세요.'; msg.hidden = false;
    }, function () { btn.disabled = false; btn.textContent = old; msg.textContent = '인터넷 연결을 확인하고 다시 눌러 주세요.'; msg.hidden = false; });
  }

  setTimeout(flush, 800);
  function DS(id) { return S.days[id] || (S.days[id] = { scores: {}, wrong: {}, started: null, finished: null, run: null, titles: (P.days.filter(function (d) { return d.id === id; })[0] || { steps: [] }).steps.map(function (x) { return x.title; }) }); }

  /* ---------- 도구 ---------- */
  function E(s) { return String(s == null ? '' : s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  function shuffle(a) { a = a.slice(); for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)), t = a[i]; a[i] = a[j]; a[j] = t; } return a; }
  function shuffleDiff(a) { if (a.length < 2) return a.slice(); var s, n = 0; do { s = shuffle(a); n++; } while (s.join('\u0001') === a.join('\u0001') && n < 20); return s; }
  function norm(s) { return String(s).toLowerCase().replace(/[’‘`]/g, "'").replace(/\s+/g, ' ').trim(); }
  function strip(h) { return String(h).replace(/<[^>]+>/g, '').replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&amp;/g, '&'); }
  function cut(s, n) { s = String(s); return s.length > n ? s.slice(0, n) + '…' : s; }
  function $(sel) { return app.querySelector(sel); }
  /* 약한 유형(70% 미만)과 그 뒤 보충 연습 결과: 선생님 시트·결과 카드에 쓰인다 */
  function weakList(d) {
    var st = DS(d.id), out = [];
    d.steps.forEach(function (s, i) { var sc = st.scores[i]; if (!sc || sc[0] / sc[1] >= 0.7) return;
      var ex = (st.extra || {})[i] || [], last = ex[ex.length - 1], best = null;
      ex.forEach(function (x) { if (!best || x.c / x.t > best.c / best.t) best = x; });
      out.push({ i: i, s: s, sc: sc, n: ex.length, last: last, ok: !!best && best.c / best.t >= 0.7, best: best }); });
    return out;
  }
  function weakText(d) {
    return weakList(d).map(function (w) { return stepShort(w.s) + ' ' + w.sc[0] + '/' + w.sc[1] + ' → ' + (w.n ? '보충 ' + w.best.c + '/' + w.best.t + (w.ok ? ' ✓' : '') + (w.n > 1 ? ' (' + w.n + '번)' : '') + ' ' + fmtTime(w.last.at) : '보충 안 함'); }).join(' / ');
  }
  function stepShort(st) { return st.type === 'pick' ? st.title : st.type === 'mc' && /실전/.test(st.title) ? '실전' : st.type === 'mc' && /일치/.test(st.title) ? '일치' : st.type === 'mc' && /요약/.test(st.title) ? '요약문' : SHORT[st.type]; }
  var CARD = { vocab: '단어', tf: 'T/F', verb: '동사', error: '오류', order: '순서', scramble: '스크램블', mc: '문법', insert: '삽입', odd: '어색', blank: '빈칸' };
  function cardLabel(st) { return st.type === 'pick' ? (/어법/.test(st.title) ? '어법' : '어휘') : st.type === 'mc' && /실전/.test(st.title) ? '실전' : st.type === 'mc' && /일치/.test(st.title) ? '일치' : st.type === 'mc' && /요약/.test(st.title) ? '요약' : CARD[st.type]; }
  function fmtTime(t) { var d = new Date(t); return (d.getMonth() + 1) + '/' + d.getDate() + ' ' + String(d.getHours()).padStart(2, '0') + ':' + String(d.getMinutes()).padStart(2, '0'); }
  function top() { window.scrollTo(0, 0); }
  var TAB = 'today', SEL = 0;
  var HUBM = /[?&]hub=([A-Za-z0-9-]+)/.exec(location.search), FROM_HUB = HUBM ? HUBM[1] : '';
  try { if (FROM_HUB) sessionStorage.setItem('fromHub', FROM_HUB); else FROM_HUB = sessionStorage.getItem('fromHub') || ''; } catch (e) {} /* 본문·유형별 탭에서 고른 DAY */

  /* ---------- 문항 만들기 ---------- */
  /* 모의고사처럼 본문을 '#' 제목으로 나눈 세트: 문항마다 몇 번 지문인지 찾아서 q.src 에 붙인다.
     본문 문장이 들어 있는 문항은 자동으로 찾고, 단어·T/F·문법 문항은 데이터의 n(문항 번호)을 쓴다. */
  function sections(d) {
    var isSec = function (l) { return l[0] === '#' || (!l[0] && /^[❶-❿]$/.test(l[1]) && !l[2]); };
    if (!d || !d.passage.some(isSec)) return null;
    var out = [], cur = null;
    d.passage.forEach(function (l) { if (isSec(l)) out.push(cur = { label: l[0] === '#' ? l[1] : '본문 ' + l[1], text: '' }); else if (cur) cur.text += ' ' + norm(l[1]); });
    return out;
  }
  function filled(type, q) {
    var s = '';
    if (type === 'pick') s = q.s.replace(/\{([^}|]*)[^}]*\}/, '$1');
    else if (type === 'verb') s = q.s.replace('___', q.a[0]);
    else if (type === 'error') { var k = 0; s = q.s.replace(/\[\[(.+?)\]\]/g, function (a, b) { return k++ === q.w ? q.fix : b; }); }
    else if (type === 'blank') s = q.s.replace('____', q.opts[0]);
    else if (type === 'scramble') s = q.en;
    else if (type === 'order' || type === 'insert') s = q.lines[0];
    else if (type === 'odd') s = q.lines[q.odd === 0 ? 1 : 0];
    return s;
  }
  /* 근거 문장: 본문에서 str 이 들어 있는 줄을 찾아 [영어, 해석, 찾은 부분] */
  function findLine(d, str) {
    var k = norm(str).replace(/[.!?"]+$/, ''); if (!k) return null;
    var l = d.passage.filter(function (x) { return x[0] !== '#' && x[2] && norm(x[1]).indexOf(k) >= 0; })[0];
    return l ? [l[1], l[2], str] : null;
  }
  function findLines(d, list) {
    var out = [], seen = {};
    [].concat(list || []).forEach(function (x) { var l = x && findLine(d, x); if (l && !seen[l[0]]) { seen[l[0]] = 1; out.push(l); } });
    return out;
  }
  /* 일치·불일치 등: box: ['❷'] → 그 본문 단락을 문제 아래 상자로 보여 준다 */
  function boxHTML(d, box) {
    var on = false, out = [];
    d.passage.forEach(function (l) {
      if (l[0] === '#' || (!l[0] && /^[❶-❿]$/.test(l[1]) && !l[2])) { on = box.indexOf(l[0] === '#' ? l[1] : l[1]) >= 0; return; }
      if (on) out.push(E((l[0] ? l[0] + ': ' : '') + l[1]));
    });
    return out.length ? '<span class="exam-box en">' + out.join(' ') + '</span>' : '';
  }
  function autoEv(d, type, q) {
    if (!/^(pick|verb|error|blank|insert)$/.test(type)) return [];
    var f = type === 'insert' ? q.lines[q.given] : filled(type, q);
    return findLines(d, norm(f).split(/(?<=[.!?]["']?)\s+/).map(function (x) { return x.replace(/[.!?"]+$/, ''); })).map(function (l) { return [l[0], l[1], '']; });
  }
  function srcOf(secs, type, q) {
    var n = type === 'vocab' ? q[2] : type === 'tf' ? q[3] : q.n, s = '';
    if (n != null) { var hit = secs.filter(function (x) { return x.label.indexOf(n + '번') === 0 || x.label === '본문 ' + n; })[0]; return hit ? hit.label : (/^\d+$/.test(n) ? n + '번' : '본문 ' + n); }
    s = filled(type, q);
    s = norm(s).split(/(?<=[.!?]["']?)\s+/)[0].replace(/[.!?"]+$/, '');
    var f = s && secs.filter(function (x) { return x.text.indexOf(s) >= 0; })[0];
    if (f) return f.label;
    /* 본문 문장을 그대로 쓰지 않는 문항(단어·T/F·문법): 겹치는 낱말이 가장 많은 본문을 고른다. 애매하면 비워 둔다 */
    var probe = type === 'vocab' ? q[0] : type === 'tf' ? q[0] : type === 'mc' ? strip(String(q.q).replace(/<br>/g, ' ')) + ' ' + strip(q.opts[0]) : '';
    var STOP = /^(that|this|with|from|have|they|their|there|what|when|which|about|were|been|into|than|then|them|your|will|would|could|should|some|other|these|those|very|also|only|just|more|most|does|did|doing|being|after|before|because|while|where|people|things|thing|said)$/;
    var ws = (norm(probe).match(/[a-z][a-z'-]{2,}/g) || []).filter(function (w) { return type === 'vocab' || (w.length > 3 && !STOP.test(w)); }).map(function (w) { return w.slice(0, Math.max(4, Math.min(w.length, 6) - 1)); });
    if (!ws.length) return '';
    var sc = secs.map(function (x) { return { l: x.label, n: ws.filter(function (w) { return new RegExp('\\b' + w.replace(/[^a-z'-]/g, '')).test(x.text); }).length }; }).sort(function (a, b) { return b.n - a.n; });
    var need = type === 'vocab' ? 1 : 2;
    return sc[0].n >= need && (!sc[1] || sc[0].n > sc[1].n) ? sc[0].l : '';
  }
  function gen(step, d) {
    var secs = sections(d);
    if (!secs) return gen0(step);
    var lab = function (q, raw) {
      var src = srcOf(secs, step.type, raw); if (src) { q.src = src; q.key = src.split(' ')[0] + ' ' + q.key; }
      var ev = step.type === 'tf' ? raw[4] : raw.ev;
      if (ev) { q.ev = findLines(d, ev); q.evLabel = '근거 문장'; } else { q.ev = autoEv(d, step.type, raw); q.evLabel = '문장 해석'; }
      if (raw.box) q.prompt = String(q.prompt || '') + boxHTML(d, raw.box);
      if (/요약/.test(step.title)) q.num = true;
      if (raw.flow) { q.flow = raw.flow; q.flowOn = step.type === 'insert' ? raw.given : -1; }
      if (raw.per) q.per = raw.per.map(function (p, i) { return { o: raw.opts[i], ko: p[0], ev: findLines(d, p[1]), note: p[2] || '' }; });
      return q;
    };
    if (step.type === 'vocab') return gen0(step).map(function (q) { return lab(q, step.items.filter(function (w) { return w[0] === q.key; })[0]); });
    var idx = step.items.map(function (_, i) { return i; });
    if (step.type !== 'order') idx = shuffle(idx);
    return idx.map(function (i) {
      var q = gen0({ type: step.type, items: [step.items[i]] })[0];
      if (step.type === 'order') q.key = '세트 ' + (i + 1);
      return lab(q, step.items[i]);
    });
  }
  function gen0(step) {
    var t = step.type, it = step.items;
    if (t === 'vocab') {
      return shuffle(it).slice(0, step.quizN || it.length).map(function (w, i) {
        var ko2en = i % 3 === 2, others = shuffle(it.filter(function (x) { return x !== w; })).slice(0, 3);
        var ans = ko2en ? w[0] : w[1];
        return { t: 'choice', prompt: E(ko2en ? w[1] : w[0]), big: true, en: !ko2en, sub: ko2en ? '알맞은 영어 표현을 고르세요.' : '알맞은 뜻을 고르세요.',
          opts: shuffle([ans].concat(others.map(function (x) { return ko2en ? x[0] : x[1]; }))).map(E), ans: E(ans), key: w[0],
          ex: '정답 ▶ ' + w[0] + ' = ' + w[1] + (others.length ? '\n다른 보기 ▶ ' + others.map(function (x) { return x[0] + ' = ' + x[1]; }).join(' / ') : '') };
      });
    }
    if (t === 'pick') return shuffle(it).map(function (q) {
      var m = /\{([^}]*)\}/.exec(q.s), opts = m[1].split('|');
      return { t: 'pick', pre: q.s.slice(0, m.index), post: q.s.slice(m.index + m[0].length), opts: shuffle(opts), ans: opts[0], ex: q.ex, key: opts[0] };
    });
    if (t === 'tf') return shuffle(it).map(function (q) { return { t: 'tf', s: q[0], ans: q[1], ex: q[2], key: q[0].split(' ').slice(0, 4).join(' ') + '…' }; });
    if (t === 'verb') return shuffle(it).map(function (q) { return { t: 'verb', s: q.s, v: q.v, a: q.a, ex: q.ex, key: q.v + '→' + q.a[0] }; });
    if (t === 'error') return shuffle(it).map(function (q) {
      var parts = [], re = /\[\[(.+?)\]\]/g, last = 0, m, k = 0;
      while ((m = re.exec(q.s))) { parts.push({ x: q.s.slice(last, m.index) }); parts.push({ x: m[1], mk: k++ }); last = re.lastIndex; }
      parts.push({ x: q.s.slice(last) });
      return { t: 'error', parts: parts, w: q.w, fix: q.fix, ex: q.ex, key: q.fix };
    });
    if (t === 'order') return it.map(function (q, i) { return { t: 'order', lines: q.lines, pool: shuffleDiff(q.lines.map(function (_, j) { return j; })), key: '세트 ' + (i + 1) }; });
    if (t === 'scramble') return shuffle(it).map(function (q) {
      var en = q.en.trim(), p = /[.!?]$/.test(en) ? en.slice(-1) : '', body = p ? en.slice(0, -1) : en, toks = body.split(/\s+/);
      if (HS && toks.length >= 5) { /* 고등: 3~4단어 빈칸 채우기 */
        var W = en.split(/\s+/), g = q.gap;
        if (!g) { var len = W.length >= 12 ? 4 : 3, a0 = Math.max(1, Math.floor((W.length - len) / 2)); g = [a0, a0 + len - 1]; }
        var part = W.slice(g[0], g[1] + 1), post = W.slice(g[1] + 1).join(' '), m2 = /^(.*?)([.!?]["”]?)$/.exec(part[part.length - 1]);
        if (g[1] === W.length - 1 && m2 && m2[1]) { part[part.length - 1] = m2[1]; post = m2[2]; } /* 문장 끝 부호는 빈칸 밖에 */
        return { t: 'scramble', gap: true, ko: q.ko, pre: W.slice(0, g[0]).join(' '), post: post, toks: part, pool: shuffleDiff(part.map(function (_, j) { return j; })), punct: '', ans: part.join(' '), full: en, key: cut(q.ko, 14), ex: q.ex || '' };
      }
      return { t: 'scramble', ko: q.ko, toks: toks, pool: shuffleDiff(toks.map(function (_, j) { return j; })), punct: p, ans: en, key: cut(q.ko, 14), ex: q.ex || '' };
    });
    if (t === 'insert') return shuffle(it).map(function (q) {
      var rest = q.lines.filter(function (_, j) { return j !== q.given; });
      return { t: 'insert', given: q.lines[q.given], rest: rest, ans: q.given - 1, ex: q.ex, key: cut(q.lines[q.given], 22) };
    });
    if (t === 'odd') return shuffle(it).map(function (q) { return { t: 'odd', lines: q.lines, ans: q.odd, ex: q.ex, key: cut(q.lines[q.odd], 22) }; });
    if (t === 'blank') return shuffle(it).map(function (q) {
      return { t: 'choice', prompt: '<span class="en">' + E(q.s).replace('____', '<span class="blank" id="blank">&nbsp;</span>') + '</span>', fill: E(q.opts[0]),
        opts: shuffle(q.opts).map(E), ans: E(q.opts[0]), ex: q.ex, key: q.opts[0], optEn: true };
    });
    if (t === 'mc') return shuffle(it).map(function (q) { return { t: 'choice', prompt: q.q, opts: shuffle(q.opts), ans: q.opts[0], ex: q.ex, key: strip(q.opts[0]) }; });
    return [];
  }

  /* ---------- 진행 계산 ---------- */
  function dayProgress(d) {
    var st = DS(d.id), done = d.steps.filter(function (_, i) { return st.scores[i]; }).length, c = 0, t = 0;
    Object.keys(st.scores).forEach(function (k) { c += st.scores[k][0]; t += st.scores[k][1]; });
    var next = d.steps.findIndex(function (_, i) { return !st.scores[i]; });
    return { done: done, next: next, c: c, t: t, finished: done === d.steps.length };
  }
  function bridge(d, nowIdx) {
    var st = DS(d.id);
    return '<div class="bridge" style="--n:' + d.steps.length + '" aria-hidden="true">' + d.steps.map(function (_, i) {
      return '<i class="' + (st.scores[i] ? 'done' : i === nowIdx ? 'now' : '') + '"></i>';
    }).join('') + '</div>';
  }
  function daySwitch(id) {
    return '<div class="seg' + (P.pick ? ' pk' : '') + '" role="tablist" aria-label="' + (P.pick ? '번호' : 'DAY') + ' 고르기">' + P.days.map(function (d, i) {
      return '<button role="tab" aria-selected="' + (i === SEL) + '" class="' + (i === SEL ? 'on' : '') + '" data-sel="' + i + '">' + (inProgress(d) ? '<span class="seglock">' + LOCK + '</span>' : '') + E(d.name) + (P.pick ? '' : ' <small>' + E(d.range) + '</small>') + '</button>';
    }).join('') + '</div>';
  }
  /* 컨닝 방지: DAY 를 시작한 뒤 오답 학습까지 다 끝낼 때까지 그 DAY 의 본문·유형별 연습·다시 풀기를 잠근다 */
  var LOCK = '<svg viewBox="0 0 16 16" width="14" height="14" aria-hidden="true"><rect x="3" y="7" width="10" height="7.5" rx="1.5" fill="currentColor"/><path d="M5.2 7V5a2.8 2.8 0 0 1 5.6 0v2" fill="none" stroke="currentColor" stroke-width="1.8"/></svg>';
  function inProgress(d) { return false; } /* 학습 중 잠금 꺼짐 (선생님 요청) */
  function lockHTML(d, what) {
    var di = P.days.indexOf(d);
    return '<section class="card lockcard"><div class="lockicon">' + LOCK + '</div><h2>' + E(d.name) + ' ' + what + '은 잠시 잠겨 있어요</h2>' +
      '<p class="sub">문제를 푸는 중에는 ' + what + '을 볼 수 없어요. ' + E(d.name) + '를 오답 학습까지 끝내면 다시 열려요.</p>' +
      '<button class="btn" data-golock="' + di + '">' + (needReview(d) ? '오답 학습 하러 가기' : '이어서 풀기') + '</button></section>';
  }

  /* ---------- 홈 (탭) ---------- */
  function home(tab) {
    if (tab) TAB = tab;
    RS = null; top();
    var h = '<header class="htop' + (TAB === 'today' && S.name && !P.pick ? '' : ' flat') + '">' + (FROM_HUB ? '<a class="hublink" href="../' + FROM_HUB + '/">← 전체 목록</a>' : '') +
      '<div class="htop-bar"><span>' + E(P.school) + ' · ' + E(P.unit) + '</span>' +
      (S.name ? '<button class="htop-who" id="rename" title="학생 바꾸기"><span class="av">' + E(S.name.charAt(0)) + '</span>' + E(S.name) + '<small>바꾸기</small></button>' : '') + '</div>' +
      '<h1 class="en">' + E(P.title) + '</h1><p>' + E(P.exam) + ' 대비 · ' + P.days.length + (P.pick ? '문항' : ' DAY') + '</p></header><div class="hbody' + (TAB === 'today' && S.name && !P.pick ? '' : ' flat') + '">';
    /* 카톡 안: 이 화면에 아직 기록이 없을 때만, 닫을 수 있는 작은 안내. 이미 카톡에서 풀던 학생은 그대로 이어서 하게 둔다 */
    if (IN_APP && !S.kakaoOk && !Object.keys(S.days).some(function (k) { return S.days[k] && S.days[k].started; })) h += '<div class="card" id="kakaonote" style="margin:0 0 16px"><b>처음이라면 크롬·사파리로 여는 걸 추천해요.</b> 이미 카톡에서 풀던 학생은 그대로 카톡에서 이어서 하면 돼요. ' +
      (hereURL() ? '<a class="btn ghost" style="margin:10px 0 6px;width:100%" target="_blank" rel="noopener" href="kakaotalk://web/openExternal?url=' + encodeURIComponent(hereURL()) + '">크롬·사파리로 열기</a>' : '') +
      '<span class="note" style="display:block">버튼이 안 되면 화면 오른쪽 아래(또는 위) <b>⋮ / ⋯ → 다른 브라우저로 열기</b>를 눌러 주세요. 늘 같은 곳(카톡 또는 브라우저)으로 들어와야 기록이 이어져요.</span><button class="link" id="kakaook" style="margin-top:6px">카톡에서 계속할게요 (닫기)</button></div>';
    if (!STORE_OK) h += '<p class="card" style="margin:0 0 16px;border-color:var(--bad);background:var(--bad-soft)"><b>이 화면에서는 기록이 저장되지 않아요.</b> 나갔다 들어오면 처음부터 시작해요. 선생님께 받은 링크를 크롬이나 사파리로 열어 주세요.</p>';
    if (!S.name) {
      var rs = roster();
      h += '<form class="card who" id="nameform" style="margin-bottom:16px"><label for="nm" style="flex-basis:100%;font-weight:600">' + (rs.length ? '누가 공부하나요? 내 이름을 눌러 주세요' : '이름을 먼저 적어 주세요') + '</label>' +
        (rs.length ? '<div class="whochips">' + rs.map(function (n) { return '<span class="whochip"><button type="button" class="btn ghost" data-who="' + E(n) + '">' + E(n) + '</button><button type="button" class="x" data-unwho="' + E(n) + '" aria-label="' + E(n) + ' 목록에서 빼기" title="목록에서 빼기(기록은 남아요)">×</button></span>'; }).join('') + '</div>' +
          '<span class="note" style="flex-basis:100%">내 이름이 없으면 아래에 새로 적어요. 같은 이름을 적으면 내 기록이 그대로 이어져요.</span>' : '') +
        '<span class="note" style="flex-basis:100%">선생님이 알아볼 수 있게 <b>한글 이름 전체</b>(예: 김민준)를 정확히 적어 주세요.</span><span class="note" id="nmbad" style="flex-basis:100%;color:var(--bad);font-weight:700" hidden>이름은 띄어쓰기 없이 한글로 적어 주세요. 예: 김민준</span>' +
        '<input id="nm" autocomplete="name" placeholder="예: 김민준" maxlength="12">' + (GATE ? '<input id="pc" inputmode="numeric" autocomplete="off" placeholder="학생 코드" maxlength="8" style="max-width:9em">' : '') + '<button class="btn" type="submit">' + (rs.length ? '새 이름으로 시작' : '저장') + '</button></form>';
    }
    if (!S.name && GATE && SHEET) { app.innerHTML = h + '</div>'; bindHome(); var n0 = $('#nm'); if (n0) n0.focus(); return; } /* 명단이 켜져 있으면 이름·코드를 넣기 전엔 학습 화면을 보여 주지 않음 */
    if (needPass()) {
      var mp = myPass(S.name), deny = DENY[S.name];
      if (deny === 'unit') h += '<form class="card who" id="passform" style="margin-bottom:16px"><p style="flex-basis:100%;margin:0;font-weight:600">' + E(S.name) + ' 학생에게는 아직 열리지 않은 과제예요.</p>' +
        '<span class="note" style="flex-basis:100%">선생님이 열어 주시면 바로 들어올 수 있어요. 선생님께 말씀드려 주세요.</span>' +
        '<button class="btn ghost" type="button" id="recheck">다시 확인하기</button>' +
        '<button class="link" type="button" id="notme" style="flex-basis:100%;text-align:left">' + E(S.name) + ' 학생이 아니에요 (다른 이름으로)</button></form></div>';
      else if (mp && !deny) h += '<div class="card" id="passform" style="margin-bottom:16px"><p style="margin:0">확인하고 있어요…</p><span class="note">인터넷이 연결되어 있어야 해요.</span></div></div>';
      else h += '<form class="card who" id="passform" style="margin-bottom:16px"><label for="pc" style="flex-basis:100%;font-weight:600"><b>' + E(S.name) + '</b> 학생, 선생님께 받은 <b>학생 코드</b>를 적어 주세요.</label>' +
        '<span class="note" style="flex-basis:100%">처음 한 번만 적으면 다음부터는 바로 들어와요.</span><span class="note" id="pcbad" style="flex-basis:100%;color:var(--bad);font-weight:700" hidden></span>' +
        '<input id="pc" inputmode="numeric" autocomplete="off" placeholder="학생 코드" maxlength="8"><button class="btn" type="submit">확인</button>' +
        '<button class="link" type="button" id="notme" style="flex-basis:100%;text-align:left">' + E(S.name) + ' 학생이 아니에요 (다른 이름으로)</button></form></div>';
      app.innerHTML = h; bindHome(); var pi = $('#pc'); if (pi) pi.focus();
      if (mp && !deny) gateSync();
      return;
    }
    var TABS = [['today', '오늘의 학습', '<path d="M3 11l9-7 9 7v9a1 1 0 0 1-1 1h-5v-6H9v6H4a1 1 0 0 1-1-1z"/>'], ['text', '본문', '<path d="M5 3h10l4 4v14H5z"/><path d="M9 12h6M9 16h4"/>'],
      ['types', '유형별 연습', '<rect x="4" y="4" width="7" height="7" rx="1.5"/><rect x="13" y="4" width="7" height="7" rx="1.5"/><rect x="4" y="13" width="7" height="7" rx="1.5"/><rect x="13" y="13" width="7" height="7" rx="1.5"/>']];
    h += '<div class="stack">';
    if (TAB === 'today') h += todayHTML();
    if (TAB === 'text') h += '<h3 class="sech">본문</h3>' + daySwitch() + (inProgress(P.days[SEL]) ? lockHTML(P.days[SEL], '본문') : passageHTML(P.days[SEL]));
    if (TAB === 'types') h += '<h3 class="sech">유형별 연습</h3>' + daySwitch() + (inProgress(P.days[SEL]) ? lockHTML(P.days[SEL], '유형별 연습') : typesHTML(P.days[SEL]));
    h += '</div></div><nav class="bnav tabs" role="tablist">' + TABS.map(function (t) {
      return '<button role="tab" aria-selected="' + (TAB === t[0]) + '" class="' + (TAB === t[0] ? 'on' : '') + '" data-tab="' + t[0] + '"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round" aria-hidden="true">' + t[2] + '</svg>' + t[1] + '</button>';
    }).join('') + '</nav>';
    app.innerHTML = h;
    bindHome();
  }

  /* ---------- 완료 도장 · 달력 (처음 화면) ---------- */
  var CAL = null, CALSEL = null;
  function ymd(t) { var d = new Date(t); return d.getFullYear() + '-' + (d.getMonth() + 1) + '-' + d.getDate(); }
  function events() {
    var ev = [];
    P.days.forEach(function (d) {
      hist(d).forEach(function (h, i) { if (h.finished) ev.push({ d: d, n: i + 1, t: h.finished, pct: h.pct, rev: !!h.review || h.c === h.t }); });
      var st = DS(d.id), g = dayProgress(d);
      if (st.finished) ev.push({ d: d, n: attemptNo(d), t: st.finished, pct: pctOf(g.c, g.t), rev: !needReview(d) });
    });
    return ev.sort(function (a, b) { return a.t - b.t; });
  }
  function stampHTML() {
    var ev = events(), now = new Date();
    if (!CAL) CAL = { y: now.getFullYear(), m: now.getMonth() };
    var h = '<section class="card stampcard"><div class="row" style="justify-content:space-between"><h2>완료 도장</h2><span class="stamp-sum">' +
      (ev.length ? '완료 <b>' + ev.filter(function (e) { return e.rev; }).length + '회</b>' + (ev.some(function (e) { return !e.rev; }) ? ' · 오답 남음 ' + ev.filter(function (e) { return !e.rev; }).length : '') + ' · 마지막 ' + fmtTime(ev[ev.length - 1].t).split(' ')[0] : '아직 찍힌 도장이 없어요') + '</span></div>';
    h += '<div class="stamps">' + P.days.map(function (d) {
      var mine = ev.filter(function (e) { return e.d === d; }), last = mine[mine.length - 1];
      if (!last) return '<div class="stamp empty"><small>' + E(d.name) + '</small><b>?</b><small>' + E(d.range) + '</small></div>';
      var pend = !last.rev;
      return '<div class="stamp' + (pend ? ' pend' : '') + '" title="' + E(mine.map(function (e) { return e.n + '회차 ' + e.pct + '점 ' + fmtTime(e.t); }).join(' / ')) + '">' +
        (mine.length > 1 ? '<i class="times">×' + mine.length + '</i>' : '') +
        '<small>' + E(d.name) + '</small><b>' + (pend ? '오답 남음' : '완료') + '</b><small>' + fmtTime(last.t).split(' ')[0] + ' · ' + last.pct + '점</small></div>';
    }).join('') + '</div>';
    return h + '</section>';
  }

  function lockBtn(d, why) { return '<button class="btn ghost locked" disabled aria-disabled="true"><span><svg viewBox="0 0 16 16" width="14" height="14" aria-hidden="true"><rect x="3" y="7" width="10" height="7.5" rx="1.5" fill="currentColor"/><path d="M5.2 7V5a2.8 2.8 0 0 1 5.6 0v2" fill="none" stroke="currentColor" stroke-width="1.8"/></svg> ' + (attemptNo(d) + 1) + '회차 도전</span><small>' + E(why) + '</small></button>'; }
  /* 지금 할 DAY: 오답 학습 남은 DAY → 하던 DAY → 아직 안 끝낸 첫 DAY → 마지막 DAY */
  function focusIdx() {
    var i;
    for (i = 0; i < P.days.length; i++) if (needReview(P.days[i])) return i;
    for (i = 0; i < P.days.length; i++) { var d = P.days[i], g = dayProgress(d); if (!g.finished && (g.done || DS(d.id).run)) return i; }
    for (i = 0; i < P.days.length; i++) if (!dayProgress(P.days[i]).finished) return i;
    return P.days.length - 1;
  }
  var SEL_SET = false;
  function myStats() {
    var mins = 0, solved = 0, right = 0, done = 0;
    var dur = function (a, b) { return a && b && b > a ? Math.min((b - a) / 60000, 120) : 0; };
    P.days.forEach(function (d) {
      var st = DS(d.id), g = dayProgress(d);
      hist(d).forEach(function (x) { mins += dur(x.started, x.finished); solved += x.t || 0; right += x.c || 0; if (x.finished) done++; });
      mins += dur(st.started, st.finished); solved += g.t; right += g.c; if (g.finished && !needReview(d)) done++;
      Object.keys(st.extra || {}).forEach(function (k) { (st.extra[k] || []).forEach(function (x) { solved += x.t; right += x.c; }); });
    });
    return { mins: Math.round(mins), solved: solved, acc: solved ? Math.round(right / solved * 100) : 0, done: done };
  }
  function hm(m) { return m >= 60 ? Math.floor(m / 60) + '<i>시간</i> ' + (m % 60) + '<i>분</i>' : m + '<i>분</i>'; }
  function dayState(d) {
    var g = dayProgress(d), st = DS(d.id);
    if (needReview(d)) return 'rev';
    if (g.finished) return 'done';
    if (g.done || st.run) return 'now';
    return 'wait';
  }
  function pickGridHTML() { /* 모의고사: 번호를 골라서 학습 */
    var done = P.days.filter(function (d) { return dayState(d) === 'done'; }).length;
    return '<h3 class="sech">문항 고르기 <span>완료 ' + done + ' / ' + P.days.length + '</span></h3><p class="note" style="margin:-4px 0 10px">공부할 번호를 누르면 아래에 단계가 나와요. 순서는 자유예요.</p><div class="qgrid">' + P.days.map(function (d, di) {
      var s = dayState(d), g = dayProgress(d), prev = s === 'wait' && hist(d).some(function (x) { return x.restored; });
      var tag = s === 'done' ? '완료' + (hist(d).length ? ' ×' + (hist(d).length + 1) : '') : s === 'rev' ? '오답 남음' : s === 'now' ? g.done + '/' + d.steps.length + '단계' : prev ? '이전 완료' : '';
      return '<button class="qt ' + s + (prev ? ' prev' : '') + (di === SEL ? ' sel' : '') + '" data-sel="' + di + '"><b>' + E(d.name.replace(/번$/, '')) + '</b><small>' + E(d.range) + '</small><i>' + tag + '</i></button>';
    }).join('') + '</div>';
  }
  function todayHTML() {
    var h = '', fi = focusIdx(), fd = P.days[fi], fg = dayProgress(fd), fst = DS(fd.id), fstate = dayState(fd);
    if (!SEL_SET) SEL = fi;
    if (P.pick) {
      if (!SEL_SET) { var pi = P.days.findIndex(function (d) { var s = dayState(d); return s === 'now' || s === 'rev'; }); SEL = pi >= 0 ? pi : Math.max(0, P.days.findIndex(function (d) { return dayState(d) !== 'done'; })); }
      h += pickGridHTML();
      var ms0 = myStats();
      h += '<div class="stats"><div class="stat"><small>누적 학습</small><b>' + hm(ms0.mins) + '</b></div><div class="stat"><small>푼 문제</small><b>' + ms0.solved + '<i>문제</i></b></div><div class="stat"><small>정답률</small><b>' + ms0.acc + '<i>%</i></b></div></div>';
      return h + dayDetailHTML();
    }
    var allDone = P.days.every(function (d) { return dayState(d) === 'done'; });
    var pct = Math.round(fg.done / fd.steps.length * 100);
    /* 오늘 할 학습 */
    var label = allDone ? '모든 DAY 완료' : fstate === 'rev' ? '마지막 단계: 오답 학습' : fstate === 'now' ? '이어서 할 학습' : '오늘 할 학습';
    var sub = allDone ? '수고했어요! 약한 유형을 보충하거나 2회차에 도전해 보세요.'
      : fstate === 'rev' ? '틀린 ' + wrongCount(fd) + '문제를 다시 풀면 결과를 보낼 수 있어요.'
      : fst.run ? '<b>' + E(fd.steps[fst.run.si].title) + '</b> ' + Math.min(fst.run.qi + 1, fst.run.qs.length) + '/' + fst.run.qs.length + '번에서 멈췄어요'
      : fg.done ? '다음 단계: <b>' + E(fd.steps[fg.next].title) + '</b>' : E(fd.story);
    var cta = allDone ? '<button class="btn cta" data-res="' + fi + '">결과 다시 보기</button>'
      : fstate === 'rev' ? '<button class="btn cta" data-rev="' + fi + '">오답 학습 하기 (' + wrongCount(fd) + '개) →</button>'
      : '<button class="btn cta" data-go="' + fi + '">' + (fstate === 'now' ? '이어서 하기' : '시작하기') + ' →</button>';
    h += '<section class="card hero"><div class="hero-in"><div class="ring" style="--p:' + (allDone ? 100 : pct) + '"><div><b>' + (allDone ? '✓' : fg.done) + '</b><small>' + (allDone ? '완료' : '/ ' + fd.steps.length + '단계') + '</small></div></div>' +
      '<div class="hero-t"><div class="k">' + label + '</div><h2>' + E(fd.name) + ' · ' + E(fd.range) + '</h2><p>' + sub + '</p></div></div>' + cta + '</section>';
    /* 나의 학습 기록 */
    var ms = myStats();
    h += '<div class="stats"><div class="stat"><small>누적 학습</small><b>' + hm(ms.mins) + '</b></div><div class="stat"><small>푼 문제</small><b>' + ms.solved + '<i>문제</i></b></div><div class="stat"><small>정답률</small><b>' + ms.acc + '<i>%</i></b></div></div>';
    if (S.name) { h += noteHTML(); setTimeout(noteSync, 0); }
    /* 학습 진도 */
    h += '<h3 class="sech">학습 진도 <span>완료 ' + P.days.filter(function (d) { return dayState(d) === 'done'; }).length + ' / ' + P.days.length + '</span></h3><div class="drows">' + P.days.map(function (d, di) {
      var g = dayProgress(d), st = DS(d.id), s = dayState(d), hs = hist(d);
      var line = s === 'done' ? pctOf(g.c, g.t) + '점 · ' + (st.finished ? fmtTime(st.finished).split(' ')[0] + ' 완료' : '완료') + (wrongCount(d) ? ' · 오답 학습 완료' : ' · 틀린 문제 없음')
        : s === 'rev' ? pctOf(g.c, g.t) + '점 · 오답 학습 ' + wrongCount(d) + '개 남음'
        : s === 'now' ? g.done + ' / ' + d.steps.length + '단계 진행 중' : E(d.story);
      var badge = { done: '완료' + (hs.length ? ' ×' + (hs.length + 1) : ''), rev: '오답 남음', now: '진행 중', wait: '시작 전' }[s];
      return '<button class="drow ' + s + (di === SEL ? ' sel' : '') + '" data-sel="' + di + '"><span class="dn"><small>DAY</small>' + E(d.name.replace(/^DAY\s*/, '')) + '</span>' +
        '<span class="dt"><b>' + E(d.range) + '</b><span>' + line + '</span>' + (s === 'now' ? '<span class="mini"><i style="width:' + Math.round(g.done / d.steps.length * 100) + '%"></i></span>' : '') + '</span><span class="badge">' + badge + '</span></button>';
    }).join('') + '</div>';
    h += dayDetailHTML();
    return h;
  }

  function dayDetailHTML() {
    var h = '';
    /* 약한 유형 보충 띠 */
    var wk = []; P.days.forEach(function (d, di) { if (dayState(d) !== 'done') return; weakList(d).forEach(function (w) { if (!w.ok) wk.push({ di: di, d: d, w: w }); }); });
    if (wk.length) h += '<div class="weakstrip"><div><b>약한 유형 보충 ' + wk.length + '개 남았어요</b><span>' + wk.slice(0, 3).map(function (x) { return E(x.d.name) + ' · ' + E(x.w.s.title) + ' ' + x.w.sc[0] + '/' + x.w.sc[1]; }).join(' · ') + '</span></div><button class="btn" data-weak="' + wk[0].di + ':' + wk[0].w.i + '">보충하기</button></div>';
    /* 고른 DAY 단계 */
    var d = P.days[SEL], di = SEL, g = dayProgress(d), st = DS(d.id), run = st.run;
    var hs = hist(d), hnote = hs.length ? '<br><small>' + attemptNo(d) + '회차 · 이전 기록 ' + hs.map(function (x, i) { return (i + 1) + '회차 ' + x.pct + '점'; }).join(', ') + '</small>' : '';
    var status = (needReview(d) ? '<b>문제 풀이 완료 · ' + pctOf(g.c, g.t) + '점</b> (' + g.c + '/' + g.t + ') · 오답 학습 ' + wrongCount(d) + '개 남음 (끝내야 결과를 보낼 수 있어요)' : g.finished ? '<b>완료</b> · ' + g.c + '/' + g.t + ' (' + Math.round(g.c / g.t * 100) + '%)' + (st.finished ? ' · ' + fmtTime(st.finished) : '')
      : run ? '<b>' + E(d.steps[run.si].title) + ' ' + Math.min(run.qi + 1, run.qs.length) + '/' + run.qs.length + '번</b>에서 멈췄어요'
      : g.done ? '<b>' + g.done + '/' + d.steps.length + '단계</b> 건넜어요 · 다음: ' + E(d.steps[g.next].title) : '아직 시작 전') + hnote;
    h += '<h3 class="sech" id="daydetail">' + E(d.name) + ' 단계 <span>' + E(d.range) + '</span></h3><section class="card day">' +
      '<ol class="slist">' + d.steps.map(function (s, i) {
        var sc = st.scores[i], cls = sc ? 'd' : i === g.next ? 'n' : 'w', low = sc && sc[0] / sc[1] < 0.7;
        return '<li><button class="srow ' + cls + '" data-step="' + di + ':' + i + '"' + (cls === 'w' ? ' disabled' : '') + '><span class="ic">' + (sc ? '✓' : i + 1) + '</span><span class="sn">' + E(s.title) + '</span>' +
          '<span class="sc' + (low ? ' low' : '') + '">' + (sc ? sc[0] + '/' + sc[1] : cls === 'n' ? (run && run.si === i ? '이어서' : '다음') : '') + '</span></button></li>';
      }).join('') + '</ol>' +
      '<p class="note" style="margin:8px 0 0">끝낸 단계를 누르면 다시 풀어 볼 수 있어요 (점수는 처음 기록 유지).</p>' +
      '<div class="status">' + status + '</div>' + weakBox(d, di) + '<div class="acts">' +
      (needReview(d) ? '<button class="btn plank" data-rev="' + di + '">오답 학습 하기</button>' + lockBtn(d, '오답 학습 후 열려요') : g.finished ? '<button class="btn" data-res="' + di + '">결과 보내기</button><button class="btn ghost" data-retry="' + di + '">' + (attemptNo(d) + 1) + '회차 도전</button>'
        : '<button class="btn" data-go="' + di + '">' + (g.done || run ? '이어서 하기' : '시작하기') + '</button>' + lockBtn(d, '다 끝내면 열려요')) +
      '</div>' + (g.finished && !needReview(d) ? '<p class="note retrynote" id="rn' + di + '" hidden>한 번 더 누르면 ' + (attemptNo(d) + 1) + '회차를 처음부터 시작해요. 지금 점수(' + pctOf(g.c, g.t) + '점)는 ' + attemptNo(d) + '회차 기록으로 남아요.</p>' : '') + '</section>';
    h += '<p class="note">기록은 이 기기에 이름별로 저장돼요. 같은 기기에서 같은 이름으로 들어오면 이어서 할 수 있어요.' + (SHEET ? ' 끝낸 단계는 선생님께도 자동으로 전달돼요.' : '') + '</p>';
    return h;
  }

  function weakBox(d, di) {
    if (!dayProgress(d).finished || needReview(d)) return '';
    var ws = weakList(d); if (!ws.length) return '';
    return '<div class="weakbox"><b>약한 유형 보충 연습</b> <small>70% 넘게 맞히면 ✓ · 선생님께 자동으로 전달돼요</small><div class="weakbtns">' + ws.map(function (w) {
      return '<button class="btn ghost' + (w.ok ? ' wdone' : '') + '" data-weak="' + di + ':' + w.i + '">' + (w.ok ? '✓ ' : '') + E(stepShort(w.s)) + ' <small>' + w.sc[0] + '/' + w.sc[1] + (w.n ? ' → ' + w.best.c + '/' + w.best.t : '') + '</small></button>'; }).join('') + '</div></div>';
  }
  function passageHTML(d) {
    return '<section class="card"><div class="row" style="justify-content:space-between"><h2 class="en">' + E(P.title) + '</h2>' +
      '<button class="link" id="ptog">해석 숨기기</button></div><div class="script" id="script">' +
      d.passage.map(function (l) {
        if (!l[0] && /^[❶-❿]$/.test(l[1])) return '<div class="sec">본문 ' + l[1] + '</div>';
        if (l[0] === '#') return '<div class="sec">' + E(l[1]) + '</div>'; /* 모의고사: ['#', '18번 · 글의 목적', ''] */
        var stage = !l[0] && !P.prose;
        return '<div class="line' + (stage ? ' stage' : '') + '">' + (l[0] ? '<span class="sp' + (/^Troll/.test(l[0]) ? ' troll' : '') + '">' + E(l[0]) + '</span>' : '') +
          '<span class="t en">' + E(l[1]) + '</span><span class="k">' + E(l[2]) + '</span></div>';
      }).join('') + '</div></section>';
  }

  function typesHTML(d) {
    return '<p class="sub" style="margin:0">원하는 유형을 골라 자유롭게 연습해요. 여기서 푼 건 점수와 문자에 들어가지 않아요.</p>' +
      '<div class="typegrid">' + d.steps.map(function (s, i) {
        return '<button class="typebtn" data-free="' + i + '"><b>' + E(s.title) + '</b><small>' + (s.type === 'vocab' ? (s.quizN || s.items.length) : s.items.length) + '문항</small></button>';
      }).join('') + '</div>';
  }

  function bindHome() {
    var rg = $('#rsgo'); if (rg) rg.onclick = function () {
      var r = restoreFrom($('#rsin').value), msg = $('#rsmsg');
      if (r.err) { msg.textContent = r.err; msg.style.color = 'var(--bad)'; return; }
      home('today'); var m2 = $('#rsmsg'), dt = $('#restore');
      if (dt) dt.open = true;
      if (m2) { m2.textContent = r.added ? '완료 도장 ' + r.added + '개를 되살렸어요.' : '이미 다 들어 있는 기록이에요.'; m2.style.color = 'var(--ok)'; }
    };
    var ko = $('#kakaook'); if (ko) ko.onclick = function () { S.kakaoOk = true; save(); var n = $('#kakaonote'); if (n) n.remove(); };
    var f = $('#nameform');
    if (f) f.addEventListener('submit', function (e) { e.preventDefault(); var v = $('#nm').value.replace(/\s+/g, '').trim(); var bad = $('#nmbad');
      if (!/^[가-힣]{2,5}$/.test(v)) { bad.textContent = '이름은 띄어쓰기 없이 한글로 적어 주세요. 예: 김민준'; bad.hidden = false; $('#nm').focus(); return; }
      if (GATE && SHEET) { tryEnter(v, ($('#pc') || {}).value, bad, f.querySelector('[type=submit]')); return; }
      useStudent(v); home(); });
    var pf = $('#passform');
    if (pf && pf.tagName === 'FORM' && $('#pc')) pf.addEventListener('submit', function (e) { e.preventDefault(); tryEnter(S.name, $('#pc').value, $('#pcbad'), pf.querySelector('[type=submit]')); });
    var rc = $('#recheck'); if (rc) rc.onclick = function () { rc.disabled = true; rc.textContent = '확인 중…'; var mp = myPass(S.name);
      checkPass(S.name, mp ? mp.c : '').then(function (j) { applyCheck(S.name, mp ? mp.c : '', j); home(); }, function () { rc.disabled = false; rc.textContent = '인터넷 연결을 확인해 주세요'; }); };
    var nm = $('#notme'); if (nm) nm.onclick = function () { S = load(''); lsSet('daily:who', ''); home(); };
    app.querySelectorAll('[data-who]').forEach(function (b) { b.onclick = function () { useStudent(b.dataset.who); home(); gateSync(); }; });
    app.querySelectorAll('[data-unwho]').forEach(function (b) { b.onclick = function () {
      if (b.dataset.arm) { dropRoster(b.dataset.unwho); home(); return; }
      b.dataset.arm = '1'; b.textContent = '빼기?'; setTimeout(function () { delete b.dataset.arm; b.textContent = '×'; }, 2500); }; });
    var rn = $('#rename'); if (rn) rn.onclick = function () { S = load(''); lsSet('daily:who', ''); home(); var n = $('#nm'); if (n && !roster().length) n.focus(); };
    app.querySelectorAll('[data-caln]').forEach(function (b) { b.onclick = function () { var m = CAL.m + +b.dataset.caln; CAL = { y: CAL.y + Math.floor(m / 12), m: (m % 12 + 12) % 12 }; CALSEL = null; home(); }; });
    app.querySelectorAll('[data-cald]').forEach(function (b) { b.onclick = function () { CALSEL = CALSEL === b.dataset.cald ? null : b.dataset.cald; var y = window.scrollY; home(); window.scrollTo(0, y); }; });
    app.querySelectorAll('[data-tab]').forEach(function (b) { b.onclick = function () { home(b.dataset.tab); }; });
    app.querySelectorAll('[data-note]').forEach(function (b) { b.onclick = function () { startNote(b.dataset.note); }; });
    app.querySelectorAll('[data-sel]').forEach(function (b) { b.onclick = function () { SEL = +b.dataset.sel; SEL_SET = true; home(); if (TAB === 'today') { var dd = $('#daydetail'); if (dd) dd.scrollIntoView({ block: 'start' }); } }; });
    var needName = function () { if (S.name) return false; var n = $('#nm'); n.placeholder = '이름을 적어야 시작할 수 있어요'; n.focus(); top(); return true; };
    app.querySelectorAll('[data-go]').forEach(function (b) { b.onclick = function () { if (needName()) return; var di = +b.dataset.go, rn = DS(P.days[di].id).run; startStep(di, rn ? rn.si : dayProgress(P.days[di]).next); }; });
    app.querySelectorAll('[data-step]').forEach(function (b) { b.onclick = function () {
      if (needName()) return;
      var p = b.dataset.step.split(':'), di = +p[0], si = +p[1];
      if (DS(P.days[di].id).scores[si]) { if (inProgress(P.days[di])) { var nt = $('#lk' + di); if (nt) nt.hidden = false; return; } startFree(di, si, '다시 풀기'); } else startStep(di, si);
    }; });
    app.querySelectorAll('[data-retry]').forEach(function (b) { b.onclick = function () {
      if (needName()) return;
      var di = +b.dataset.retry, d = P.days[di];
      if (!b.dataset.armed) { b.dataset.armed = '1'; b.textContent = '한 번 더 누르면 시작'; b.classList.add('plank'); b.classList.remove('ghost'); $('#rn' + di).hidden = false; return; }
      newAttempt(d); startStep(di, 0);
    }; });
    app.querySelectorAll('[data-golock]').forEach(function (b) { b.onclick = function () {
      if (needName()) return;
      var di = +b.dataset.golock, d = P.days[di];
      if (needReview(d)) { retryWrong(di); return; }
      var rn = DS(d.id).run; startStep(di, rn ? rn.si : dayProgress(d).next);
    }; });
    app.querySelectorAll('[data-res]').forEach(function (b) { b.onclick = function () { result(+b.dataset.res); }; });
    app.querySelectorAll('[data-rev]').forEach(function (b) { b.onclick = function () { retryWrong(+b.dataset.rev); }; });
    app.querySelectorAll('[data-weak]').forEach(function (b) { b.onclick = function () { var p = b.dataset.weak.split(':'); startFree(+p[0], +p[1], '보충 연습'); }; });
    app.querySelectorAll('[data-free]').forEach(function (b) { b.onclick = function () { startFree(SEL, +b.dataset.free, '유형별 연습'); }; });
    var tg = $('#ptog'); if (tg) tg.onclick = function () { var sc = $('#script'), off = sc.classList.toggle('hide-ko'); tg.textContent = off ? '해석 보기' : '해석 숨기기'; };
  }

  /* ---------- 풀이 ---------- */
  var RS = null; /* { di, si, qs, qi, c, wrong, phase, answered, practice } practice: false | '다시 풀기' | '유형별 연습' | '오답 학습' */

  function saveRun() {
    if (RS.practice) return;
    var st = DS(P.days[RS.di].id);
    st.run = { si: RS.si, qs: RS.qs, qi: RS.answered ? RS.qi + 1 : RS.qi, c: RS.c, wrong: RS.wrong, phase: RS.phase };
    save();
  }

  function startStep(di, si) {
    var d = P.days[di], st = DS(d.id), step = d.steps[si];
    if (!st.started) { st.started = Date.now(); save(); report('시작', d); }
    if (st.run && st.run.si === si) {
      var r = st.run;
      RS = { di: di, si: si, qs: r.qs, qi: r.qi, c: r.c, wrong: r.wrong || [], phase: r.phase, answered: false, practice: false };
      if (RS.qi >= RS.qs.length) { RS.qi = RS.qs.length - 1; finishStep(); return; }
    } else {
      RS = { di: di, si: si, qs: gen(step, d), qi: 0, c: 0, wrong: [], phase: step.type === 'vocab' ? 'study' : 'quiz', answered: false, practice: false };
      saveRun();
    }
    render();
  }

  function startFree(di, si, label) {
    var step = P.days[di].steps[si];
    var qs = gen(step, P.days[di]).map(function (q) { q.stepTitle = step.title; q.guide = step.guide; return q; });
    RS = { di: di, si: si, qs: qs, qi: 0, c: 0, wrong: [], phase: step.type === 'vocab' ? 'study' : 'quiz', answered: false, practice: label, back: label === '유형별 연습' ? 'types' : 'today' };
    render();
  }

  function header() {
    var d = P.days[RS.di];
    var X = '<button class="xbtn" id="quit" aria-label="나가기"><span aria-hidden="true">✕</span></button>';
    var pill = RS.phase === 'quiz' && RS.qs.length ? '<span class="qpill">' + Math.min(RS.qi + 1, RS.qs.length) + ' / ' + RS.qs.length + '</span>' : '';
    var frac = RS.qs.length ? (RS.qi + (RS.answered ? 1 : 0)) / RS.qs.length : 0;
    if (RS.practice === '오답 학습') return '<div class="topbar"><div class="row">' + X + '<span class="crumb">' + E(d.name) + ' · <b>오답 학습</b> · 저장됨</span>' + pill + '</div><div class="pbar"><i style="width:' + Math.round(frac * 100) + '%"></i></div></div>';
    if (RS.practice) return '<div class="topbar"><div class="row">' + X + '<span class="crumb"><b>' + E(RS.practice) + '</b> · 점수에 안 들어가요</span>' + pill + '</div><div class="pbar"><i style="width:' + Math.round(frac * 100) + '%"></i></div></div>';
    return '<div class="topbar"><div class="row">' + X + '<span class="crumb">' + E(d.name) + ' · <b>' + (RS.si + 1) + ' / ' + d.steps.length + '단계</b> · 저장됨</span>' + pill + '</div>' +
      '<div class="pbar"><i style="width:' + Math.round((RS.si + frac) / d.steps.length * 100) + '%"></i></div></div>';
  }

  function render() {
    top();
    if (RS.practice === '오답 노트' && RS.qs[RS.qi] && RS.qs[RS.qi].dayIdx != null) RS.di = RS.qs[RS.qi].dayIdx;
    var d = P.days[RS.di], q = RS.qs[RS.qi], step = d.steps[RS.si] || d.steps[0], h = header(), fromQ = RS.practice === '오답 학습' || RS.practice === '오답 노트';
    var title = q && q.stepTitle && fromQ ? q.stepTitle : step.title;
    var guide = q && q.guide && fromQ ? q.guide : step.guide;
    h += '<div class="stepk">' + (RS.practice ? E(RS.practice) + (RS.practice === '오답 노트' ? ' · ' + E(d.name + ' ' + d.range) : '') : 'STEP ' + (RS.si + 1)) + '</div><div class="stepname">' + E(title) + '</div><p class="guide">' + E(guide || (step.type === 'vocab' ? '단어와 뜻을 훑어보고 퀴즈를 시작하세요.' : '')) + '</p>';
    if (RS.phase === 'study') {
      h += '<div class="card"><div class="qno">' + step.items.length + '개 · 소리 내어 한 번씩 읽어 보세요' + (step.quizN ? ' (퀴즈는 ' + step.quizN + '개 무작위)' : '') + '</div><div class="wordlist">' +
        step.items.map(function (w) { return '<div class="w en">' + E(w[0]) + '</div><div class="m">' + E(w[1]) + '</div>'; }).join('') +
        '</div><div class="nextbar"><button class="btn" id="gostart">퀴즈 시작</button></div></div>';
      app.innerHTML = h; bindQuit(); $('#gostart').onclick = function () { RS.phase = 'quiz'; saveRun(); render(); }; return;
    }
    if (RS.phase === 'summary') { app.innerHTML = h + summaryHTML(); bindQuit(); bindSummary(); return; }
    h += '<div class="card pop" id="qcard">' + (q.src ? '<div class="src"><b>' + E(q.src.replace(/^(\d+번)/, '$1 지문')) + '</b></div>' : '') + qHTML(q) + '<div id="fb"></div></div>';
    app.innerHTML = h; bindQuit(); bindQ(q);
  }

  function bindQuit() { $('#quit').onclick = function () { home(RS && RS.practice === '유형별 연습' ? 'types' : 'today'); }; }

  function qHTML(q) {
    if (q.t === 'choice') return (q.sub ? '<div class="guide" style="margin:0 0 6px">' + q.sub + '</div>' : '') +
      '<div class="prompt' + (q.big ? ' big' : '') + (q.en ? ' en' : '') + '">' + q.prompt + '</div>' +
      '<div class="opts' + (q.num ? ' num' : '') + '">' + q.opts.map(function (o, i) { return '<button class="opt' + (q.optEn ? ' en' : '') + '" data-i="' + i + '">' + o + '</button>'; }).join('') + '</div>';
    if (q.t === 'pick') return '<div class="prompt en">' + E(q.pre) + '<span class="blank" id="blank">?</span>' + E(q.post) + '</div>' +
      '<div class="opts two">' + q.opts.map(function (o, i) { return '<button class="opt en" data-i="' + i + '">' + E(o) + '</button>'; }).join('') + '</div>';
    if (q.t === 'tf') return '<div class="prompt en">' + E(q.s) + '</div><div class="opts two"><button class="opt tfbtn" data-v="1">T</button><button class="opt tfbtn" data-v="0">F</button></div>';
    if (q.t === 'verb') return '<div class="prompt en">' + E(q.s).replace('___', '<span class="blank" id="blank">&nbsp;</span>') + ' <span class="verbhint">(' + E(q.v) + ')</span></div>' +
      '<form class="typein" id="vf"><input id="vin" autocomplete="off" autocapitalize="off" autocorrect="off" spellcheck="false" placeholder="알맞은 형태로 쓰기" aria-label="답 입력"><button class="btn" type="submit">확인</button></form>';
    if (q.t === 'error') return '<div class="prompt en">' + q.parts.map(function (p) {
      return p.mk == null ? E(p.x) : '<button class="mark" data-m="' + p.mk + '"><sup>' + CIRC[p.mk] + '</sup>' + E(p.x) + '</button>'; }).join('') + '</div>';
    if (q.t === 'insert') return '<div class="given"><span class="eyebrow">주어진 문장</span><span class="en">' + E(q.given) + '</span></div>' +
      '<div class="prompt en para">' + q.rest.map(function (l, j) { return E(l) + ' <button class="mark gap" data-m="' + j + '">' + CIRC[j] + '</button> '; }).join('') + '</div>';
    if (q.t === 'odd') return '<div class="prompt en para">' + q.lines.map(function (l, j) {
      return '<button class="sent" data-m="' + j + '"><sup>' + CIRC[j] + '</sup>' + E(l) + '</button>'; }).join(' ') + '</div>';
    if (q.t === 'order') return '<div class="guide" style="margin:0">누른 순서대로 아래에 쌓여요. 잘못 놓았으면 다시 눌러 빼세요.</div>' +
      '<div class="tray lines" id="tray"></div><div class="pool lines" id="pool">' + q.pool.map(function (j) { return '<button class="chip en" data-j="' + j + '">' + E(q.lines[j]) + '</button>'; }).join('') + '</div>' +
      '<div class="nextbar"><button class="btn" id="chk" disabled>확인</button></div>';
    if (q.t === 'scramble' && q.gap) return '<div class="prompt"><span class="ko">우리말</span>' + E(q.ko) + '</div>' +
      '<div class="gapline en">' + E(q.pre) + ' <span class="tray inline" id="tray"></span> ' + E(q.post) + '</div><div class="pool" id="pool">' + q.pool.map(function (j) { return '<button class="chip en" data-j="' + j + '">' + E(q.toks[j]) + '</button>'; }).join('') + '</div>' +
      '<div class="nextbar"><button class="btn" id="chk" disabled>확인</button></div>';
    if (q.t === 'scramble') return '<div class="prompt"><span class="ko">우리말</span>' + E(q.ko) + '</div>' +
      '<div class="tray" id="tray"></div><div class="pool" id="pool">' + q.pool.map(function (j) { return '<button class="chip en" data-j="' + j + '">' + E(q.toks[j]) + '</button>'; }).join('') + '</div>' +
      (q.punct ? '<div class="note">문장 끝 부호 <b>' + E(q.punct) + '</b> 는 자동으로 붙어요.</div>' : '') +
      '<div class="nextbar"><button class="btn" id="chk" disabled>확인</button></div>';
    return '';
  }

  function bindQ(q) {
    var card = $('#qcard');
    if (q.t === 'choice' || q.t === 'pick') card.querySelectorAll('.opt').forEach(function (b) { b.onclick = function () {
      var o = q.opts[+b.dataset.i], ok = o === q.ans;
      card.querySelectorAll('.opt').forEach(function (x) { x.disabled = true; if (q.opts[+x.dataset.i] === q.ans) x.classList.add('right'); });
      if (!ok) b.classList.add('wrong');
      var bl = $('#blank');
      if (bl && (q.t === 'pick' || q.fill)) { if (q.t === 'pick') bl.textContent = q.ans; else bl.innerHTML = q.fill; bl.classList.add('ok'); }
      answer(ok, q.ex);
    }; });
    if (q.t === 'tf') card.querySelectorAll('.opt').forEach(function (b) { b.onclick = function () {
      var v = b.dataset.v === '1', ok = v === q.ans;
      card.querySelectorAll('.opt').forEach(function (x) { x.disabled = true; if ((x.dataset.v === '1') === q.ans) x.classList.add('right'); });
      if (!ok) b.classList.add('wrong');
      answer(ok, q.ex);
    }; });
    if (q.t === 'verb') {
      var inp = $('#vin'); inp.focus({ preventScroll: true });
      $('#vf').addEventListener('submit', function (e) {
        e.preventDefault(); if (RS.answered) return;
        var v = norm(inp.value); if (!v) { inp.focus(); return; }
        var ok = q.a.some(function (a) { return norm(a) === v; });
        inp.disabled = true; inp.classList.add(ok ? 'right' : 'wrong'); this.querySelector('button').disabled = true;
        var bl = $('#blank'); bl.textContent = q.a[0]; bl.classList.add('ok');
        answer(ok, q.ex, ok ? '' : '정답: <b class="en">' + E(q.a.join(' / ')) + '</b>');
      });
    }
    if (q.t === 'error') card.querySelectorAll('.mark').forEach(function (b) { b.onclick = function () {
      if (RS.answered) return;
      var m = +b.dataset.m, ok = m === q.w;
      card.querySelectorAll('.mark').forEach(function (x) { x.disabled = true; if (+x.dataset.m === q.w) x.classList.add('right'); });
      if (!ok) b.classList.add('wrong');
      var wrongTxt = q.parts.filter(function (p) { return p.mk === q.w; })[0].x;
      answer(ok, q.ex, (ok ? '' : '틀린 곳은 <b>' + CIRC[q.w] + '</b> · ') + '<span class="en">' + E(wrongTxt) + ' → <span class="fix">' + E(q.fix) + '</span></span>');
    }; });
    if (q.t === 'insert' || q.t === 'odd') card.querySelectorAll('[data-m]').forEach(function (b) { b.onclick = function () {
      if (RS.answered) return;
      var m = +b.dataset.m, ok = m === q.ans;
      card.querySelectorAll('[data-m]').forEach(function (x) { x.disabled = true; if (+x.dataset.m === q.ans) x.classList.add('right'); });
      if (!ok) b.classList.add('wrong');
      if (q.t === 'insert') {
        var g = card.querySelector('.mark[data-m="' + q.ans + '"]');
        g.insertAdjacentHTML('afterend', ' <span class="inserted en">' + E(q.given) + '</span>');
      }
      answer(ok, q.ex, ok ? '' : '정답: <b>' + CIRC[q.ans] + '</b>');
    }; });
    if (q.t === 'order' || q.t === 'scramble') {
      var picked = [], tray = $('#tray'), pool = $('#pool'), chk = $('#chk'), lines = q.t === 'order';
      var label = function (j) { return lines ? q.lines[j] : q.toks[j]; };
      var draw = function () {
        tray.innerHTML = picked.map(function (j, k) { return '<button class="chip in en" data-k="' + k + '">' + (lines ? '<span class="n">' + (k + 1) + '</span>' : '') + E(label(j)) + '</button>'; }).join('') +
          (!lines && q.punct && picked.length ? '<span class="punct">' + E(q.punct) + '</span>' : '');
        pool.querySelectorAll('.chip').forEach(function (c) { var u = picked.indexOf(+c.dataset.j) >= 0; c.classList.toggle('used', u); c.disabled = u; });
        chk.disabled = picked.length !== q.pool.length;
        tray.querySelectorAll('.chip').forEach(function (c) { c.onclick = function () { if (RS.answered) return; picked.splice(+c.dataset.k, 1); draw(); }; });
      };
      pool.querySelectorAll('.chip').forEach(function (c) { c.onclick = function () { if (RS.answered) return; picked.push(+c.dataset.j); draw(); }; });
      draw();
      chk.onclick = function () {
        if (RS.answered) return;
        var ok, extra;
        if (lines) { ok = picked.every(function (j, k) { return j === k; }); extra = ok ? '' : '<b>바른 순서</b><ol style="margin:4px 0 0;padding-left:1.3em">' + q.lines.map(function (l) { return '<li class="en">' + E(l) + '</li>'; }).join('') + '</ol>'; }
        else { var built = picked.map(function (j) { return q.toks[j]; }).join(' ') + q.punct; ok = norm(built) === norm(q.ans); extra = ok ? '' : q.gap ? '정답: <span class="en">' + E(q.pre) + ' <b>' + E(q.ans) + '</b> ' + E(q.post) + '</span>' : '정답: <b class="en">' + E(q.ans) + '</b>'; }
        tray.classList.add(ok ? 'right' : 'wrong'); chk.hidden = true;
        tray.querySelectorAll('.chip').forEach(function (c) { c.disabled = true; });
        answer(ok, q.ex || '', extra);
      };
    }
  }

  function hl(l) { if (!l[2]) return E(l[0]); var i = l[0].toLowerCase().indexOf(String(l[2]).toLowerCase()); return i < 0 ? E(l[0]) : E(l[0].slice(0, i)) + '<b>' + E(l[0].slice(i, i + l[2].length)) + '</b>' + E(l[0].slice(i + l[2].length)); }
  function evLines(ls) { return ls.map(function (l) { return '<div class="ev-l"><span class="en">' + hl(l) + '</span><span class="ko">' + E(l[1]) + '</span></div>'; }).join(''); }
  function evHTML(q) {
    var h = '';
    if (q.flow) h += '<div class="ev"><div class="ev-h">글의 전개</div><ol class="flow">' + q.flow.map(function (f, i) {
      return '<li' + (i === q.flowOn ? ' class="on"' : '') + '>' + E(f) + (i === q.flowOn ? ' <small>← 주어진 문장</small>' : '') + '</li>'; }).join('') + '</ol></div>';
    if (q.per) h += '<div class="ev"><div class="ev-h">선택지 해설</div>' + q.per.map(function (p, i) {
      return '<div class="per-i' + (i === 0 ? ' ans' : '') + '"><div class="per-o"><b>' + (i === 0 ? '✓ 정답' : '✗') + '</b> <span' + (/[a-z]/i.test(p.o) ? ' class="en"' : '') + '>' + E(strip(p.o)) + '</span></div>' +
        (p.ko ? '<div class="per-ko">' + E(p.ko) + '</div>' : '') + (p.note ? '<div class="per-note">' + E(p.note) + '</div>' : '') +
        (p.ev.length ? '<div class="per-ev"><span class="ev-tag">근거</span>' + evLines(p.ev) + '</div>' : '') + '</div>';
    }).join('') + '</div>';
    else if (q.ev && q.ev.length) h += '<div class="ev"><div class="ev-h">' + E(q.evLabel || '근거 문장') + '</div>' + evLines(q.ev) + '</div>';
    return h;
  }
  function answer(ok, ex, extra) {
    if (RS.answered) return; RS.answered = true;
    var q = RS.qs[RS.qi];
    if (ok) RS.c++; else RS.wrong.push(q);
    var ne = null; try { ne = !ok ? noteAdd(q, 'wrong') : RS.practice === '오답 노트' ? noteAdd(q, 'ok') : noteEntry(q); } catch (e) {}
    if (RS.practice === '오답 학습') {
      if (!ok && RS.qi < RS.base) RS.fw = (RS.fw || 0) + 1;
      if (!ok) RS.qs.push(reshuffle(q));
      DS(P.days[RS.di].id).review = { qs: RS.qs, qi: RS.qi + 1, c: RS.c, base: RS.base, fw: RS.fw || 0 }; save();
    }
    saveRun();
    var last = RS.qi === RS.qs.length - 1;
    var fb = '<div class="feedback ' + (ok ? 'ok' : 'bad') + '" role="status"><b class="tag">' + (ok ? '정답!' : '아쉬워요') + '</b>' +
      (extra ? '<div class="answer-line">' + extra + '</div>' : '') + (ex ? '<div class="answer-line">' + E(ex) + '</div>' : '') + evHTML(q) + '</div>' +
      (ok ? '<div class="notebar"><button type="button" class="conf' + (ne && ne.conf ? ' on' : '') + '" id="conf" aria-pressed="' + !!(ne && ne.conf) + '">' + (ne && ne.conf ? '★ 헷갈려요 (오답 노트에 담김)' : '☆ 헷갈려요') + '</button><span>확신이 없었다면 눌러 두세요.</span></div>'
        : '<div class="notebar"><span class="in">📌 오답 노트에 담겼어요</span></div>') +
      '<div class="nextbar"><button class="btn" id="nx">' + (last ? (RS.practice === '오답 학습' ? '오답 학습 마치기' : '이 단계 마치기') : (RS.practice === '오답 학습' && !ok ? '다음 문제 (이 문제는 뒤에 다시 나와요)' : '다음 문제')) + '</button></div>';
    $('#fb').innerHTML = fb;
    var cf = $('#conf'); if (cf) cf.onclick = function () {
      var on = cf.classList.toggle('on'); if (on) noteAdd(q, 'conf'); else noteUnconf(q);
      cf.setAttribute('aria-pressed', on); cf.textContent = on ? '★ 헷갈려요 (오답 노트에 담김)' : '☆ 헷갈려요';
    };
    var nx = $('#nx'); nx.onclick = next; nx.focus({ preventScroll: true });
    nx.scrollIntoView({ block: 'nearest', behavior: 'smooth' });
  }

  function next() {
    RS.answered = false;
    if (RS.qi < RS.qs.length - 1) { RS.qi++; render(); return; }
    finishStep();
  }

  function finishStep() {
    RS.answered = false;
    if (!RS.practice) {
      var d = P.days[RS.di], st = DS(d.id), step = d.steps[RS.si];
      st.scores[RS.si] = [RS.c, RS.qs.length];
      st.wrong[RS.si] = RS.wrong.map(function (q) { var c = JSON.parse(JSON.stringify(q)); c.stepTitle = step.title; c.guide = step.guide; return c; });
      st.run = null;
      if (dayProgress(d).finished && !st.finished) st.finished = Date.now();
      save();
      report(dayProgress(d).finished ? 'DAY 완료' : '단계 완료', d, { step: (RS.si + 1) + '. ' + step.title, stepScore: RS.c + '/' + RS.qs.length });
    } else if (RS.practice === '오답 노트') {
      report('오답 노트', P.days[RS.di], { step: '오답 노트 ' + (RS.noteKey === '*' ? '남은 문제 전체' : RS.noteKey === '**' ? '전체 복습' : String(RS.noteKey).replace(/^g:/, '')), stepScore: RS.c + '/' + RS.qs.length });
    } else if (RS.practice !== '오답 학습') {
      var dx = P.days[RS.di], sx = DS(dx.id); sx.extra = sx.extra || {}; (sx.extra[RS.si] = sx.extra[RS.si] || []).push({ c: RS.c, t: RS.qs.length, at: Date.now() }); save();
      report(RS.practice === '보충 연습' ? '보충 연습' : RS.practice, dx, { step: (RS.si + 1) + '. ' + dx.steps[RS.si].title, stepScore: RS.c + '/' + RS.qs.length });
    } else if (RS.practice === '오답 학습') {
      var st2 = DS(P.days[RS.di].id); st2.reviewDone = { n: RS.base, tries: RS.qs.length, at: Date.now(), first: RS.base - (RS.fw || 0) }; st2.review = null; save();
      report('오답 학습 완료', P.days[RS.di], { stepScore: RS.base + '개 중 ' + (RS.base - (RS.fw || 0)) + '개 한 번에' });
    }
    RS.phase = 'summary'; render();
  }

  function summaryHTML() {
    var d = P.days[RS.di], step = d.steps[RS.si], g = dayProgress(d);
    if (RS.practice === '오답 학습') return '<div class="card pop stack" style="gap:10px"><div class="eyebrow">오답 학습 끝</div>' +
      '<div class="score">' + RS.base + '<small>개 모두 맞혔어요</small></div><p class="note" style="margin:0">한 번에 맞힌 문제 ' + (RS.base - (RS.fw || 0)) + '개 · 총 ' + RS.qs.length + '번 풀었어요. 이제 선생님께 결과를 보낼 수 있어요.</p>' +
      '<div class="nextbar"><button class="btn plank" id="back">결과 보내러 가기</button></div></div>';
    var h = '<div class="card pop stack" style="gap:10px"><div class="eyebrow">' + E(step.title) + ' 끝' + (RS.practice ? ' · 점수에 안 들어가요' : '') + '</div>' +
      '<div class="score">' + RS.c + '<small> / ' + RS.qs.length + '</small></div>';
    if (RS.wrong.length) h += '<div><div class="note" style="margin-bottom:4px">틀린 문제</div><ul class="wronglist">' + RS.wrong.map(function (q) { return '<li class="en">' + E(q.key) + '</li>'; }).join('') + '</ul></div>';
    h += '<div class="nextbar">';
    if (RS.practice) h += '<button class="btn ghost" id="again">한 번 더</button><button class="btn" id="back">돌아가기</button>';
    if (!RS.practice && g.finished) h = h.replace('<div class="nextbar">', '<p class="dayscore">DAY 풀이 점수 <b>' + pctOf(g.c, g.t) + '점</b> (' + g.c + '/' + g.t + ')' + (wrongCount(d) ? ' · 이제 틀린 ' + wrongCount(d) + '문제를 다시 풀어요' : '') + '</p><div class="nextbar">');
    if (RS.practice) {} else if (g.finished && wrongCount(d)) h += '<button class="btn plank" id="toreview">마지막 단계: 오답 학습 (' + wrongCount(d) + '개)</button>';
    else if (g.finished) h += '<button class="btn plank" id="tores">다 건넜어요! 결과 보기</button>';
    else h += '<button class="btn" id="tonext">다음 단계: ' + E(d.steps[g.next].title) + '</button>';
    return h + '</div></div>';
  }
  function bindSummary() {
    var di = RS.di, si = RS.si, pr = RS.practice, nk = RS.noteKey, b;
    if ((b = $('#tores'))) b.onclick = function () { result(di); };
    if ((b = $('#toreview'))) b.onclick = function () { retryWrong(di); };
    if ((b = $('#tonext'))) b.onclick = function () { startStep(di, dayProgress(P.days[di]).next); };
    if ((b = $('#back'))) b.onclick = function () { pr === '오답 학습' || (pr === '보충 연습' && dayProgress(P.days[di]).finished && !needReview(P.days[di])) ? result(di) : home(pr === '유형별 연습' ? 'types' : 'today'); };
    if ((b = $('#again'))) b.onclick = function () { pr === '오답 노트' ? startNote(nk) : startFree(di, si, pr); };
  }

  /* ---------- 결과 · 문자 ---------- */
  function message(d) {
    var st = DS(d.id), g = dayProgress(d), mins = st.started && st.finished ? Math.max(1, Math.round((st.finished - st.started) / 60000)) : null;
    var hs = hist(d), lines = ['[' + P.unit + ' ' + P.title + '] ' + d.name + ' 완료' + (hs.length ? ' (' + attemptNo(d) + '회차)' : ''), '이름: ' + S.name, '풀이 점수: ' + g.c + '/' + g.t + ' (' + pctOf(g.c, g.t) + '점)'];
    lines.push(d.steps.map(function (s, i) { var sc = st.scores[i]; return stepShort(s) + ' ' + sc[0] + '/' + sc[1]; }).join(', '));
    var w = [];
    d.steps.forEach(function (s, i) { var ws = st.wrong[i] || []; if (ws.length) w.push(stepShort(s) + '(' + ws.map(function (q) { return q.key; }).join(', ') + ')'); });
    lines.push(w.length ? '틀린 것: ' + w.join(' / ') : '틀린 것: 없음');
    if (w.length) lines.push(st.reviewDone ? '오답 학습 완료: ' + revText(st.reviewDone) : '오답 학습: 아직 안 함');
    if (weakList(d).length) lines.push('약한 유형: ' + weakText(d));
    if (hs.length) lines.push('이전 기록: ' + hs.map(histLine).join(' / '));
    lines.push((st.finished ? fmtTime(st.finished) : '') + (mins ? ' · ' + mins + '분 걸림' : '') + ' · 확인 코드 ' + checkCode(d));
    return lines.join('\n');
  }
  /* 확인 코드: 이름·단원·점수·완료 시각으로 만든 4자리. 점수를 고친 캡처는 코드가 맞지 않는다 */
  function checkCode(d) {
    var st = DS(d.id), str = [S.name, P.id, d.id, d.steps.map(function (_, i) { return (st.scores[i] || []).join('-'); }).join(','), st.finished || 0, st.reviewDone ? st.reviewDone.n + '-' + st.reviewDone.first : 0, (st.history || []).map(function (h) { return h.c + '/' + h.t + '@' + h.finished; }).join(';')].join('|'), h = 2166136261;
    for (var i = 0; i < str.length; i++) { h ^= str.charCodeAt(i); h = Math.imul(h, 16777619) >>> 0; }
    var A = 'ABCDEFGHJKLMNPQRSTUVWXYZ23456789', out = '';
    for (var k = 0; k < 4; k++) { out += A[h % A.length]; h = Math.floor(h / A.length); }
    return out;
  }
  /* 기록 코드: 이 단원에서 끝낸 모든 회차(날짜·점수·오답 학습)를 결과 메시지에 담는다.
     카톡 안 화면처럼 기록이 지워지는 곳에서도, 내가 보낸 결과 메시지를 붙여 넣으면 도장·달력이 되살아난다 */
  function b64e(str) { return btoa(unescape(encodeURIComponent(str))).replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, ''); }
  function b64d(str) { str = str.replace(/-/g, '+').replace(/_/g, '/'); while (str.length % 4) str += '='; return decodeURIComponent(escape(atob(str))); }
  function fnv(str) { var h = 2166136261; for (var i = 0; i < str.length; i++) { h ^= str.charCodeAt(i); h = Math.imul(h, 16777619) >>> 0; } return h.toString(36); }
  function recordCode() {
    var a = [];
    P.days.forEach(function (d, di) {
      hist(d).forEach(function (h) { if (h.finished) a.push([di, h.c, h.t, Math.round(h.finished / 60000), h.review ? h.review.n : 0, h.review && h.review.first != null ? h.review.first : -1]); });
      var st = DS(d.id), g = dayProgress(d);
      if (st.finished && g.finished) a.push([di, g.c, g.t, Math.round(st.finished / 60000), st.reviewDone ? st.reviewDone.n : 0, st.reviewDone && st.reviewDone.first != null ? st.reviewDone.first : -1]);
    });
    var body = JSON.stringify({ u: P.id, n: S.name, a: a });
    return 'R1' + fnv(body) + '.' + b64e(body);
  }
  function restoreFrom(text) {
    var m = /R1([0-9a-z]+)\.([A-Za-z0-9_-]+)/.exec(String(text || '').replace(/\s+/g, ''));
    if (!m) return { err: '기록 코드를 찾지 못했어요. 카톡에 보낸 결과 메시지를 통째로 복사해서 붙여 넣어 주세요.' };
    var body; try { body = b64d(m[2]); } catch (e) { return { err: '기록 코드가 잘렸어요. 메시지를 처음부터 끝까지 다시 복사해 주세요.' }; }
    if (fnv(body) !== m[1]) return { err: '기록 코드가 잘렸거나 바뀌었어요. 메시지를 다시 복사해 주세요.' };
    var o; try { o = JSON.parse(body); } catch (e) { return { err: '기록 코드를 읽지 못했어요.' }; }
    if (o.u !== P.id) return { err: '다른 단원의 결과예요. 이 단원(' + P.unit + ')에서 보낸 결과를 붙여 넣어 주세요.' };
    var added = 0;
    (o.a || []).forEach(function (x) {
      var d = P.days[x[0]]; if (!d) return;
      var st = DS(d.id), t = x[3] * 60000, hs = st.history || (st.history = []);
      var dup = hs.some(function (h) { return Math.round((h.finished || 0) / 60000) === x[3]; }) || (st.finished && Math.round(st.finished / 60000) === x[3]);
      if (dup) return;
      hs.push({ c: x[1], t: x[2], pct: pctOf(x[1], x[2]), started: null, finished: t, review: x[4] ? { n: x[4], first: x[5] >= 0 ? x[5] : null, tries: x[4] } : null, restored: true });
      hs.sort(function (p, q) { return p.finished - q.finished; });
      added++;
    });
    if (!S.name && o.n) S.name = o.n;
    save();
    return { added: added, name: o.n };
  }
  function smsHref(body) {
    var num = String(P.teacherPhone || '').replace(/[^0-9+]/g, '');
    var ios = /iPhone|iPad|iPod/i.test(navigator.userAgent) || (navigator.platform === 'MacIntel' && navigator.maxTouchPoints > 1);
    return 'sms:' + num + (ios ? '&' : '?') + 'body=' + encodeURIComponent(body);
  }
  function pctOf(c, t) { return t ? Math.round(c / t * 100) : 0; }
  function hist(d) { return DS(d.id).history || []; }
  function attemptNo(d) { return hist(d).length + 1; }
  function revText(rv) {
    if (rv.first == null) return rv.n + '개 모두 맞힘 (' + rv.tries + '번 풀이)';
    return '최종 100점 · ' + rv.n + '개 중 ' + rv.first + '개 한 번에 맞힘' + (rv.n > rv.first ? ' · ' + (rv.n - rv.first) + '개 재도전' : '');
  }
  function histLine(h, i) { return (i + 1) + '회차 ' + h.pct + '점 (' + h.c + '/' + h.t + (h.finished ? ', ' + fmtTime(h.finished) : '') + (h.review ? ', 오답 ' + h.review.n + '개 중 ' + (h.review.first != null ? h.review.first + '개 한 번에' : '모두 맞힘') : '') + ')'; }
  function newAttempt(d) {
    var old = DS(d.id), done = dayProgress(d), hs = (old.history || []).slice();
    if (done.finished) hs.push({ c: done.c, t: done.t, pct: pctOf(done.c, done.t), started: old.started, finished: old.finished, review: old.reviewDone || null });
    S.days[d.id] = { scores: {}, wrong: {}, started: null, finished: null, run: null, history: hs, titles: d.steps.map(function (x) { return x.title; }) }; save();
  }
  function wrongCount(d) { var st = DS(d.id); return d.steps.reduce(function (n, _, i) { return n + (st.wrong[i] || []).length; }, 0); }
  function needReview(d) { return dayProgress(d).finished && wrongCount(d) > 0 && !DS(d.id).reviewDone; }
  /* ---------- 오답 노트 ----------
     S.note = { id: { id, d: DAY id, q: 문제 사본, wrong: 틀린 횟수, conf: 헷갈려요, ok: 노트에서 맞힘, at } }
     틀린 문제는 자동으로, 맞힌 문제도 '헷갈려요'를 누르면 담긴다. 과(교과서)·DAY(모의고사)별로 골라 다시 푼다. */
  function noteId(q, d) { return d.id + '|' + fnv([q.t, q.stepTitle || '', strip(q.prompt || q.s || q.ko || (q.lines || []).join('/') || ''), q.key || ''].join('|')); }
  function notes() { return S.note || (S.note = {}); }
  function curStepTitle() { var q = RS.qs[RS.qi], d = P.days[RS.di]; return q.stepTitle || (d.steps[RS.si] || {}).title || ''; }
  function noteEntry(q) { return notes()[q.noteId || noteId(Object.assign({ stepTitle: curStepTitle() }, q), P.days[RS.di])]; }
  function noteAdd(q, kind) {
    var d = P.days[RS.di], step = d.steps[RS.si] || {}, c = JSON.parse(JSON.stringify(q));
    c.stepTitle = q.stepTitle || step.title; c.guide = q.guide || step.guide; delete c.noteId; delete c.dayIdx;
    var id = q.noteId || noteId(c, d), e = notes()[id] || (notes()[id] = { id: id, d: d.id, wrong: 0, conf: false, ok: false, first: Date.now() });
    e.q = c; e.at = Date.now();
    if (kind === 'wrong') { e.wrong++; e.ok = false; } else if (kind === 'conf') { e.conf = true; e.ok = false; } else if (kind === 'ok') { e.ok = true; e.conf = false; }
    save(); noteSend(e); return e;
  }
  function noteUnconf(q) { var e = noteEntry(q); if (!e) return; e.conf = false; e.at = Date.now(); if (!e.wrong) { delete notes()[e.id]; noteSend(e, true); } else { if (RS.practice === '오답 노트') e.ok = true; noteSend(e); } save(); }
  /* 시트와 맞추기: 바뀐 노트는 보내고(daily:noteq 대기열), 학생이 들어오면 시트의 노트를 받아 합친다 → 어느 기기에서든 같은 노트 */
  var NQK = 'daily:noteq', nFlushing = false, nSynced = {};
  function noteQ() { try { return JSON.parse(lsGet(NQK)) || []; } catch (e) { return []; } }
  function noteSend(e, del) {
    if (!SHEET || !S.name || !e) return;
    var d = P.days.filter(function (x) { return x.id === e.d; })[0] || P.days[0], q = e.q || {};
    var item = { name: S.name, unit: P.id, school: P.school, id: e.id, at: e.at || Date.now(), del: !!del, day: d.name + ' ' + d.range, group: noteGroup(d), step: q.stepTitle || '',
      text: cut(strip(q.prompt || q.s || q.ko || (q.lines || []).join(' / ') || q.key || ''), 200), wrong: e.wrong, conf: e.conf, ok: e.ok,
      data: del ? '' : JSON.stringify({ id: e.id, d: e.d, wrong: e.wrong, conf: e.conf, ok: e.ok, at: e.at, first: e.first, q: e.q }) };
    var qq = noteQ().filter(function (x) { return !(x.name === item.name && x.unit === item.unit && x.id === item.id); }); qq.push(item);
    lsSet(NQK, JSON.stringify(qq.slice(-400))); setTimeout(noteFlush, 300);
  }
  function noteFlush() {
    if (!SHEET || nFlushing || !window.fetch) return;
    var qq = noteQ(); if (!qq.length) return;
    var batch = qq.slice(0, 15); nFlushing = true;
    fetch(SHEET, { method: 'POST', mode: 'no-cors', headers: { 'Content-Type': 'text/plain;charset=utf-8' }, body: JSON.stringify({ k: window.SHEET_KEY || '', notes: batch }) })
      .then(function () { var sent = {}; batch.forEach(function (x) { sent[x.name + x.unit + x.id + x.at + x.del] = 1; });
        lsSet(NQK, JSON.stringify(noteQ().filter(function (x) { return !sent[x.name + x.unit + x.id + x.at + x.del]; }))); nFlushing = false; if (noteQ().length) setTimeout(noteFlush, 500); },
        function () { nFlushing = false; });
  }
  try { window.addEventListener('online', noteFlush); } catch (e) {}
  function noteSync() {
    if (!SHEET || !S.name || !window.fetch || nSynced[S.name]) return;
    var who = S.name, pc = myPass(who); nSynced[who] = true;
    fetch(SHEET + (SHEET.indexOf('?') < 0 ? '?' : '&') + 'notes=1&name=' + encodeURIComponent(who) + '&code=' + encodeURIComponent(pc ? pc.c : '') + '&unit=' + encodeURIComponent(P.id) + '&_=' + Date.now(), { cache: 'no-store' })
      .then(function (r) { return r.text(); }).then(function (t) {
        var j = null; try { j = JSON.parse(t); } catch (e) {}
        if (!j || !j.ok || S.name !== who) { if (!j || !j.ok) nSynced[who] = false; return; }
        var mine = notes(), seen = {}, changed = false;
        (j.notes || []).forEach(function (raw) { var e; try { e = JSON.parse(raw); } catch (x) { return; } if (!e || !e.id || !e.q) return; seen[e.id] = 1;
          var l = mine[e.id]; if (!l || (e.at || 0) > (l.at || 0)) { mine[e.id] = e; changed = true; } });
        Object.keys(mine).forEach(function (id) { if (!seen[id]) noteSend(mine[id]); }); /* 이 기기에만 있던 노트는 시트로 */
        if (changed) { save(); var c = app.querySelector('.notecard'); if (c) { c.outerHTML = noteHTML(); app.querySelectorAll('[data-note]').forEach(function (b) { b.onclick = function () { startNote(b.dataset.note); }; }); } }
      }, function () { nSynced[who] = false; });
  }
  function noteGroup(d) { var m = /(\d+)과/.exec(d.range || ''); return m ? m[1] + '과' : d.name; }
  function noteGroups() {
    var g = {}, order = [];
    Object.keys(notes()).forEach(function (id) { var e = notes()[id], di = P.days.findIndex(function (d) { return d.id === e.d; }); if (di < 0) return;
      var k = noteGroup(P.days[di]); if (!g[k]) { g[k] = { k: k, di: di, rem: 0, all: 0, label: /과$/.test(k) ? k : k + ' (' + P.days[di].range + ')' }; order.push(k); }
      g[k].all++; if (!e.ok) g[k].rem++; if (di < g[k].di) g[k].di = di; });
    return order.map(function (k) { return g[k]; }).sort(function (a, b) { return a.di - b.di; });
  }
  function noteHTML() {
    var gs = noteGroups(), rem = gs.reduce(function (n, g) { return n + g.rem; }, 0), all = gs.reduce(function (n, g) { return n + g.all; }, 0);
    if (!all) return '<section class="card notecard"><div class="nc-h"><b>오답 노트</b><span>아직 비어 있어요</span></div><p class="note" style="margin:6px 0 0">틀린 문제와, 맞혔어도 <b>헷갈려요</b>를 누른 문제가 여기에 모여요. 시험 전이나 주말에 모아서 다시 풀어요.</p></section>';
    return '<section class="card notecard"><div class="nc-h"><b>오답 노트</b><span>남은 문제 <b>' + rem + '</b>개 · 모은 문제 ' + all + '개</span></div>' +
      '<div class="nc-g">' + gs.map(function (g) { return '<button class="btn ghost" data-note="g:' + E(g.k) + '">' + E(g.label) + ' <b>' + (g.rem || '✓') + '</b></button>'; }).join('') + '</div>' +
      (rem ? '<button class="btn" data-note="*">남은 문제 전체 다시 풀기 (' + rem + ')</button>' : '<p class="note" style="margin:8px 0 0">남은 문제를 다 맞혔어요! 시험 전에는 아래에서 전체를 다시 복습해 보세요.</p>') +
      (all > rem ? '<button class="link" data-note="**" style="margin-top:8px">맞힌 문제까지 전체 복습 (' + all + ')</button>' : '') + '</section>';
  }
  function startNote(key) {
    var es = Object.keys(notes()).map(function (id) { return notes()[id]; }).filter(function (e) { return P.days.some(function (d) { return d.id === e.d; }); });
    if (key === '*') es = es.filter(function (e) { return !e.ok; });
    else if (key !== '**') { var k = key.replace(/^g:/, ''), inG = es.filter(function (e) { return noteGroup(P.days.filter(function (d) { return d.id === e.d; })[0]) === k; }), r = inG.filter(function (e) { return !e.ok; }); es = r.length ? r : inG; }
    if (!es.length) return;
    var di0 = function (e) { return P.days.findIndex(function (d) { return d.id === e.d; }); };
    es.sort(function (a, b) { return di0(a) - di0(b) || a.first - b.first; });
    var qs = es.map(function (e) { var q = reshuffle(e.q); q.noteId = e.id; q.dayIdx = di0(e); return q; });
    RS = { di: qs[0].dayIdx, si: 0, qs: qs, qi: 0, c: 0, wrong: [], phase: 'quiz', answered: false, practice: '오답 노트', back: 'today', noteKey: key };
    render();
  }
  function reshuffle(q) { q = JSON.parse(JSON.stringify(q)); if (q.t === 'order' || q.t === 'scramble') q.pool = shuffleDiff(q.pool); if (q.opts) q.opts = shuffle(q.opts); return q; }
  /* 오답 학습: 틀린 문제를 모두 맞힐 때까지 다시 낸다. 끝내야 결과를 보낼 수 있다. 문제마다 저장돼 이어서 할 수 있다. */
  function retryWrong(di) {
    var d = P.days[di], st = DS(d.id);
    if (st.review && st.review.qs && st.review.qi < st.review.qs.length) {
      var r = st.review; RS = { di: di, si: 0, qs: r.qs, qi: r.qi, c: r.c, wrong: [], phase: 'quiz', answered: false, practice: '오답 학습', base: r.base, fw: r.fw || 0 };
    } else {
      var qs = []; d.steps.forEach(function (_, i) { (st.wrong[i] || []).forEach(function (q) { qs.push(reshuffle(q)); }); });
      RS = { di: di, si: 0, qs: qs, qi: 0, c: 0, wrong: [], phase: 'quiz', answered: false, practice: '오답 학습', base: qs.length };
      st.review = { qs: qs, qi: 0, c: 0, base: qs.length }; save();
    }
    render();
  }

  function result(di) {
    RS = null; top();
    var d = P.days[di], st = DS(d.id), g = dayProgress(d), msg = message(d), pct = Math.round(g.c / g.t * 100);
    var wrongN = wrongCount(d);
    if (needReview(d)) { retryWrong(di); return; }
    var h = '<div class="topbar"><div class="row"><button class="link" id="quit">← 처음 화면</button><span class="crumb">' + E(d.name) + ' · <b>결과</b></span></div>' + bridge(d, -1) + '</div>';
    var mins = st.started && st.finished ? Math.max(1, Math.round((st.finished - st.started) / 60000)) : null;
    var rv = st.reviewDone;
    /* 캡처 한 장에 다 들어가는 결과 카드 */
    h += '<div class="stack"><section class="rcard" id="rcard">' +
      '<div class="rc-top"><div><div class="rc-name">' + E(S.name) + '</div><div class="rc-unit">' + E(P.school) + ' · ' + E(P.unit) + '<br><b>' + E(d.name) + '</b> ' + E(d.range) + '</div></div>' +
      '<div class="rc-score"><small class="lbl">' + (hist(d).length ? attemptNo(d) + '회차 ' : '') + '풀이 점수</small><b>' + pct + '</b><span>점</span><small>' + g.c + ' / ' + g.t + '</small></div></div>' +
      '<div class="rc-grid">' + d.steps.map(function (s, i) { var sc = st.scores[i], low = sc[0] / sc[1] < 0.7;
        return '<div class="' + (low ? 'low' : '') + '"><span>' + E(cardLabel(s)) + '</span><b>' + sc[0] + '/' + sc[1] + '</b></div>'; }).join('') + '</div>' +
      '<div class="rc-review ' + (wrongN && !rv ? 'no' : 'ok') + '">' + (wrongN ? (rv ? '✓ 오답 학습 완료 → ' + revText(rv) : '✗ 오답 학습 안 함') : '✓ 틀린 문제 없음') + '</div>' +
      (weakList(d).length ? '<div class="rc-weak"><b>약한 유형 보충</b> ' + weakList(d).map(function (w) { return '<span class="' + (w.ok ? 'ok' : 'no') + '">' + E(stepShort(w.s)) + ' ' + (w.n ? w.best.c + '/' + w.best.t + (w.ok ? ' ✓' : '') + ' <small>' + fmtTime(w.last.at) + '</small>' : '안 함') + '</span>'; }).join('') + '</div>' : '') +
      (hist(d).length ? '<div class="rc-hist"><div class="rc-hist-h">이전 기록</div>' + hist(d).map(function (h, i) {
        return '<div><span>' + (i + 1) + '회차</span><b>' + h.pct + '점</b><small>' + h.c + '/' + h.t + (h.finished ? ' · ' + fmtTime(h.finished) : '') + (h.review ? ' · 오답 ' + h.review.n + '개' : '') + '</small></div>'; }).join('') + '</div>' : '') +
      '<div class="rc-foot"><span>' + (st.finished ? fmtTime(st.finished) + ' 완료' : '') + (mins ? ' · ' + mins + '분' : '') + '</span><span>확인 코드 <b>' + checkCode(d) + '</b></span></div>' +
      '</section><p class="note" style="margin:0;text-align:center">카드만 캡처하면 결과가 다 담겨요.</p>';
    if (weakList(d).length) h += '<section class="card stack" style="gap:10px"><h2>빨간 영역 다시 풀기</h2><p class="note" style="margin:0">70% 미만인 영역이에요. 눌러서 다시 풀면 기록이 선생님께 전달되고, 70%를 넘기면 ✓가 붙어요.</p><div class="weakbtns">' +
      weakList(d).map(function (w) { return '<button class="btn ghost' + (w.ok ? ' wdone' : '') + '" data-weak="' + di + ':' + w.i + '">' + (w.ok ? '✓ ' : '') + E(w.s.title) + ' <small>' + w.sc[0] + '/' + w.sc[1] + (w.n ? ' → ' + w.best.c + '/' + w.best.t : '') + '</small></button>'; }).join('') + '</div></section>';
    h += '<section class="card stack" style="gap:12px"><h2>선생님께 결과 보내기</h2>' +
      '<button class="btn plank wide" id="kakao">카톡으로 보내기</button>' +
      '<p class="note" style="margin:0" id="kakaonote">누르면 공유 창이 열려요. <b>카카오톡 → 선생님 채팅방</b>을 고르고 전송을 누르세요.</p>' +
      '<a class="btn ghost wide" id="sms" href="' + E(smsHref(msg)) + '">문자로 보내기</a>' +
      '<p class="note" style="margin:0">문자앱이 열리면 <b>전송 버튼을 직접 눌러야</b> 보내져요.' + (P.teacherPhone ? ' 받는 번호: <b>' + E(P.teacherPhone) + '</b>' : '') +
      ' 둘 다 안 되면 아래 내용을 복사해서 카톡에 붙여 넣어 보내 주세요.</p>' +
      '<pre class="msg" id="msg">' + E(msg) + '</pre><button class="btn ghost" id="copy">결과 내용 복사</button></section>';
    h += '<section class="card stack" style="gap:10px"><h2>더 해 보기</h2>' +
      (wrongN ? '<p class="note" style="margin:0">오답 학습 완료 · ' + wrongN + '개를 모두 맞혔어요.</p>' : '<p class="note" style="margin:0">틀린 문제가 없어요.</p>') +
      '<button class="btn ghost" id="reset">' + (attemptNo(d) + 1) + '회차 다시 도전하기</button><p class="note" id="resetnote" hidden>다시 누르면 지금 점수(' + pct + '점)는 ' + attemptNo(d) + '회차 기록으로 남고, ' + (attemptNo(d) + 1) + '회차를 처음부터 시작해요.</p></section></div>';
    app.innerHTML = h;
    $('#quit').onclick = function () { home('today'); };
    app.querySelectorAll('[data-weak]').forEach(function (b) { b.onclick = function () { var p = b.dataset.weak.split(':'); startFree(+p[0], +p[1], '보충 연습'); }; });
    $('#kakao').onclick = function () {
      var btn = this, note = $('#kakaonote');
      var fallback = function () {
        var ok = function () { note.innerHTML = '<b>결과를 복사했어요.</b> 카카오톡을 열어 선생님 채팅방에 <b>붙여넣기</b> 하고 전송하세요.'; };
        var sel = function () { var r = document.createRange(); r.selectNodeContents($('#msg')); var x = getSelection(); x.removeAllRanges(); x.addRange(r); note.innerHTML = '아래 결과가 선택됐어요. <b>길게 눌러 복사</b>한 뒤 카카오톡 선생님 채팅방에 붙여넣기 하세요.'; };
        try { navigator.clipboard.writeText(msg).then(ok, sel); } catch (e) { sel(); }
      };
      if (navigator.share) navigator.share({ text: msg }).then(function () { note.innerHTML = '공유 창을 열었어요. 선생님 채팅방에서 <b>전송</b>까지 눌렀는지 확인하세요.'; }, function (e) { if (!e || e.name !== 'AbortError') fallback(); });
      else fallback();
    };
    $('#copy').onclick = function () {
      var btn = this, done = function () { btn.textContent = '복사했어요'; };
      var sel = function () { var r = document.createRange(); r.selectNodeContents($('#msg')); var s = getSelection(); s.removeAllRanges(); s.addRange(r); btn.textContent = '선택됐어요. 길게 눌러 복사하세요'; };
      try { navigator.clipboard.writeText(msg).then(done, sel); } catch (e) { sel(); }
    };
    var armed = false;
    $('#reset').onclick = function () {
      if (!armed) { armed = true; $('#resetnote').hidden = false; this.textContent = '한 번 더 누르면 초기화'; return; }
      newAttempt(d); home('today');
    };
  }

  if (/[?&]test\b/.test(location.search)) window.__dbg = function () { return RS; };
  home();
  gateSync();
  setTimeout(noteFlush, 1500);
})();
