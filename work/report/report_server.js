
/* ---------- 주간 리포트 (11/6) ----------
 * 현황판 위 [주간 리포트] → 주(월~일)와 학생을 고르면 학부모님용 리포트 한 장.
 * 선생님 한마디 · 다음 주 목표는 '주간리포트' 탭에 저장되고, [이미지로 저장]으로 카톡에 올릴 그림을 만든다.
 * 숫자는 모두 '기록' · '현황' · '오답노트' 탭에서 그 주(월 0시 ~ 다음 월 0시, 한국 시간) 것만 모은다. */
var MEMO = '주간리포트', MEMO_HEAD = ['주(월요일)·기간', '학생', '선생님 한마디', '다음 주 목표', '저장 시각'];
function weekStart(wk) {
  var tz = 'Asia/Seoul';
  if (wk && /^\d{4}-\d{2}-\d{2}$/.test(String(wk))) {
    var d0 = new Date(String(wk) + 'T12:00:00+09:00'), u0 = +Utilities.formatDate(d0, tz, 'u');
    return Utilities.formatDate(new Date(d0.getTime() - (u0 - 1) * 86400000), tz, 'yyyy-MM-dd');
  }
  var now = new Date(), u = +Utilities.formatDate(now, tz, 'u');
  return Utilities.formatDate(new Date(now.getTime() - (u - 1) * 86400000), tz, 'yyyy-MM-dd');
}
/* 기간 직접 고르기(11/6): from·to(yyyy-MM-dd)가 둘 다 맞으면 그 기간, 아니면 wk가 든 주(월~일).
 * 한마디 저장 키: 주간이면 '2026-11-02', 기간이면 '2026-10-01~2026-10-31'. */
function rangeOf(wk, from, to) {
  var re = /^\d{4}-\d{2}-\d{2}$/;
  from = String(from || ''); to = String(to || '');
  if (re.test(from) && re.test(to)) {
    if (from > to) { var x = from; from = to; to = x; }
    var a = new Date(from + 'T00:00:00+09:00').getTime(), b = new Date(to + 'T00:00:00+09:00').getTime() + 86400000;
    if (!isNaN(a) && !isNaN(b) && b - a <= 186 * 86400000) {
      var ws = weekStart(from), we = Utilities.formatDate(new Date(new Date(ws + 'T12:00:00+09:00').getTime() + 6 * 86400000), 'Asia/Seoul', 'yyyy-MM-dd');
      if (from === ws && to === we) return { key: ws, from: from, to: to, t0: a, t1: b, custom: false };
      return { key: from + '~' + to, from: from, to: to, t0: a, t1: b, custom: true };
    }
  }
  var w = weekStart(wk), t0 = new Date(w + 'T00:00:00+09:00').getTime();
  return { key: w, from: w, to: Utilities.formatDate(new Date(t0 + 6 * 86400000 + 43200000), 'Asia/Seoul', 'yyyy-MM-dd'), t0: t0, t1: t0 + 7 * 86400000, custom: false };
}
function memoKey(k) { k = String(k || ''); var m = /^(\d{4}-\d{2}-\d{2})~(\d{4}-\d{2}-\d{2})$/.exec(k); return m ? rangeOf('', m[1], m[2]).key : weekStart(k); }
function reportData(wk, from, to) {
  var ss = SpreadsheetApp.getActiveSpreadsheet(), tz = 'Asia/Seoul';
  var RG = rangeOf(wk, from, to); wk = RG.key;
  var t0 = RG.t0, t1 = RG.t1, S = {};
  var inW = function (x) { var t = x instanceof Date ? x.getTime() : +x || 0; return t >= t0 && t < t1; };
  function st(n) { return S[n] || (S[n] = { name: n, grades: {}, days: {}, t: [], ty: {}, solved: 0, right: 0, noteDays: {}, noteN: 0, noteC: 0, prog: {}, ex: {}, vk: {}, vw: [], vRe: 0, vDone: 0, vLeft: 0, wraps: [], nNew: 0, nFix: 0, nLeft: 0, memo: '', goal: '', ever: 0 }); }
  var quit = {}, r = ss.getSheetByName(ROSTER);
  if (r && r.getLastRow() > 1) r.getRange(2, 1, r.getLastRow() - 1, 4).getValues().forEach(function (v) { var n = String(v[0]).trim(); if (n && /그만|차단|퇴원|정지/.test(String(v[3]))) quit[n] = 1; });
  var log = ss.getSheetByName('기록');
  if (log && log.getLastRow() > 1) log.getRange(2, 1, log.getLastRow() - 1, 8).getValues().forEach(function (v) {
    var n = String(v[1]).trim(); if (!n || !(v[0] instanceof Date)) return;
    var s = st(n); s.ever = 1; var g = String(v[2]).split(' ')[0]; if (g) s.grades[g] = 1;
    if (!inW(v[0])) return;
    var dk = Utilities.formatDate(v[0], tz, 'yyyy-MM-dd'); s.days[dk] = 1; s.t.push(v[0].getTime());
    var m = /(\d+)\/(\d+)\s*$/.exec(String(v[7]));
    if (/오답 노트/.test(String(v[5]))) { s.noteDays[dk] = 1; if (m) { s.noteN += +m[2]; s.noteC += +m[1]; } return; }
    if (!/단계 완료|DAY 완료/.test(String(v[5]))) return;
    var m2 = /^(\d+)\/(\d+)/.exec(String(v[7])); if (!m2 || !+m2[2]) return;
    s.solved += +m2[2]; s.right += +m2[1];
    /* 하루 한 문제(고3 수능실전반 '실전 1문제'): DAY별 맞힘/틀림 — 그 기간 처음 푼 기록만 */
    if (/실전 \d+문제/.test(String(v[6]))) { var ek = String(v[2]) + '|' + String(v[4]); if (!s.ex[ek] || s.ex[ek].t > v[0].getTime()) s.ex[ek] = { book: String(v[2]), day: String(v[4]), c: +m2[1], a: +m2[2], t: v[0].getTime(), wrong: (/틀림 ([\d·]+)번/.exec(String(v[6])) || ['', ''])[1].split('·').filter(String).map(Number), fixed: [] }; }
    /* 어휘(11/6): 단어 리스트·핵심어휘 단계에서 처음 푼 단어 수 (같은 DAY·단계는 한 번만) */
    if (/핵심어휘|단어 리스트|단어장/.test(String(v[6]))) { var vk = String(v[2]) + '|' + String(v[4]) + '|' + String(v[6]).replace(/^\d+\.\s*/, ''); if (!s.vk[vk]) s.vk[vk] = { c: +m2[1], a: +m2[2] }; }
    var ty = typeOf(v[6]); if (!ty) return;
    var x = s.ty[ty] || (s.ty[ty] = { c: 0, a: 0 }); x.c += +m2[1]; x.a += +m2[2];
  });
  var now = ss.getSheetByName('현황');
  if (now && now.getLastRow() > 1) now.getRange(2, 1, now.getLastRow() - 1, 12).getValues().forEach(function (v) {
    var n = String(v[0]).trim(); if (!n) return;
    var s = st(n); s.ever = 1; var g = String(v[1]).split(' ')[0]; if (g) s.grades[g] = 1;
    var day = String(v[3]), prog = String(v[5]), sc = /^(\d+)점/.exec(String(v[6])), end = v[11], last = v[10];
    if (/^Wrap-up/.test(day)) { if (inW(end) || (inW(last) && sc)) s.wraps.push({ name: day.replace(/^Wrap-up\s*/, ''), score: sc ? +sc[1] : null, t: end instanceof Date ? end.getTime() : last instanceof Date ? last.getTime() : 0 }); return; }
    var key = String(v[1]) + '|' + String(v[2]), p = s.prog[key] || (s.prog[key] = { book: String(v[1]), unit: String(v[2]), done: [], doing: [] });
    if ((prog === '완료' || prog === '오답 학습 남음') && inW(end)) p.done.push({ day: day, range: String(v[4]), score: sc ? +sc[1] : null, rev: prog === '오답 학습 남음' });
    else if (!(end instanceof Date) && inW(last)) p.doing.push({ day: day, range: String(v[4]), prog: prog });
  });
  var nt = ss.getSheetByName(NOTE);
  if (nt && nt.getLastRow() > 1) nt.getRange(2, 1, nt.getLastRow() - 1, 12).getValues().forEach(function (v) {
    var n = String(v[0]).trim(); if (!n || /^Wrap-up/.test(String(v[2]))) return;
    var s = st(n), ok = String(v[8]) === '맞힘', f = /"first":(\d+)/.exec(String(v[11]));
    if (f && inW(+f[1])) s.nNew++;
    if (ok && inW(v[9])) s.nFix++;
    if (!ok) s.nLeft++;
    if (typeOf(v[4]) !== '어휘' && +v[6] > 0) s.nOther = (s.nOther || 0) + 1;
    if (typeOf(v[4]) === '어휘' && +v[6] > 0) {
      var q = null; try { q = JSON.parse(String(v[11])).q; } catch (e) {}
      var wd = q ? String(q.a && q.a[0] || q.key || '') : ''; if (!wd) wd = String(v[5]).slice(0, 30); wd = wd.replace(/^(\d+(?:[~·]\d+)?번|본문 \S+)\s+/, ''); /* 키 앞에 붙은 출처(22번 등) 빼기 */
      var ft = f ? +f[1] : 0, lt = v[9] instanceof Date ? v[9].getTime() : 0;
      if (f && inW(ft) && s.vw.indexOf(wd) < 0) s.vw.push(wd);
      if (inW(lt) && lt - ft > 60000) { s.vRe++; if (ok) s.vDone++; }
      if (!ok) s.vLeft++;
    }
    if (/실전 \d+문제/.test(String(v[4])) && +v[6] > 0) { var nm = /^\s*(\d+)\s*\./.exec(String(v[5])); s.exN = s.exN || []; s.exN.push({ k: String(v[1]) + '|' + String(v[2]), n: nm ? +nm[1] : 0, ok: ok }); }
  });
  var ms = ss.getSheetByName(MEMO);
  if (ms && ms.getLastRow() > 1) ms.getRange(2, 1, ms.getLastRow() - 1, 4).getValues().forEach(function (v) {
    var w = v[0] instanceof Date ? Utilities.formatDate(v[0], tz, 'yyyy-MM-dd') : String(v[0]);
    if (w === wk && S[String(v[1]).trim()]) { S[String(v[1]).trim()].memo = String(v[2]); S[String(v[1]).trim()].goal = String(v[3]); }
  });
  var list = Object.keys(S).filter(function (n) { return !quit[n] && S[n].ever; }).map(function (n) {
    var s = S[n];
    (s.exN || []).forEach(function (x) { var e = s.ex[x.k]; if (e && x.n && e.wrong.indexOf(x.n) < 0) { e.wrong.push(x.n); if (x.ok) e.fixed.push(x.n); } });
    var exam = Object.keys(s.ex).map(function (k) { var e = s.ex[k]; e.wrong.sort(function (a, b) { return a - b; }); return e; }).sort(function (a, b) { return a.t - b.t; });
    var ts = s.t.sort(function (a, b) { return a - b; }), mins = 0;
    for (var i = 1; i < ts.length; i++) { var g = ts[i] - ts[i - 1]; if (g > 0 && g <= 15 * 60000) mins += g / 60000; }
    return { name: n, grades: Object.keys(s.grades), days: Object.keys(s.days).sort(), mins: Math.round(mins), solved: s.solved, right: s.right,
      noteN: s.noteN, noteC: s.noteC, noteDays: Object.keys(s.noteDays).length,
      types: Object.keys(s.ty).filter(function (k) { return s.ty[k].a >= 4; }).map(function (k) { return { k: k, c: s.ty[k].c, a: s.ty[k].a }; })
        .sort(function (a, b) { return b.c / b.a - a.c / a.a; }),
      prog: Object.keys(s.prog).map(function (k) { return s.prog[k]; }).filter(function (p) { return p.done.length || p.doing.length; }),
      wraps: s.wraps.sort(function (a, b) { return a.t - b.t; }), nNew: s.nNew, nFix: s.nFix, nLeft: s.nLeft, memo: s.memo, goal: s.goal, exam: exam, nOther: s.nOther || 0,
      voc: (function () { var c = 0, a = 0; Object.keys(s.vk).forEach(function (k) { c += s.vk[k].c; a += s.vk[k].a; }); return { a: a, c: c, wrong: s.vw, re: s.vRe, done: s.vDone, left: s.vLeft }; })() };
  }).sort(function (a, b) { return (b.days.length - a.days.length) || (a.name < b.name ? -1 : 1); });
  return { wk: wk, from: RG.from, to: RG.to, custom: RG.custom, made: Date.now(), list: list };
}
function saveMemo(wk, name, memo, goal) {
  wk = memoKey(wk); name = String(name || '').trim(); if (!name) return false;
  var lock = LockService.getScriptLock(); lock.waitLock(20000);
  try {
    var ss = SpreadsheetApp.getActiveSpreadsheet(), sh = ss.getSheetByName(MEMO);
    if (!sh) { sh = ss.insertSheet(MEMO, ss.getSheets().length); sh.getRange(1, 1, 1, MEMO_HEAD.length).setValues([MEMO_HEAD]).setFontWeight('bold').setBackground('#2f5fd0').setFontColor('#ffffff'); sh.setFrozenRows(1); sh.getRange('A:A').setNumberFormat('@'); sh.setColumnWidth(3, 420); }
    var row = [wk, name, String(memo || '').slice(0, 600), String(goal || '').slice(0, 200), new Date()], at = 0;
    if (sh.getLastRow() > 1) sh.getRange(2, 1, sh.getLastRow() - 1, 2).getValues().forEach(function (v, i) {
      var w = v[0] instanceof Date ? Utilities.formatDate(v[0], 'Asia/Seoul', 'yyyy-MM-dd') : String(v[0]);
      if (w === wk && String(v[1]).trim() === name) at = i + 2; });
    if (at) sh.getRange(at, 1, 1, row.length).setValues([row]); else sh.appendRow(row);
    return true;
  } finally { lock.releaseLock(); }
}
