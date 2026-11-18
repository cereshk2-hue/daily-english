# 11/16 학생별 진도표: sheet/Code.gs 에 ?view=VIEW&grid=1 페이지(GRID_HTML) + gridData() + 현황판 '진도표 →' 버튼 추가 (여러 번 돌려도 같음)
import json, re
P = 'sheet/Code.gs'; src = open(P, encoding='utf-8').read()
src = re.sub(r'\n/\* ==== 진도표 \(11/16\) ==== \*/[\s\S]*$', '\n', src).rstrip() + '\n'
def rep(a, b):
    global src
    if b in src: return
    assert src.count(a) == 1, a; src = src.replace(a, b)
rep("""  if (e && e.parameter && e.parameter.view === VIEW) {
    var t = HtmlService.createTemplate(BOARD_HTML);""", """  if (e && e.parameter && e.parameter.view === VIEW && e.parameter.grid) { /* 학생별 진도표 (11/16) */
    var g = HtmlService.createTemplate(GRID_HTML), JG = function (o) { return JSON.stringify(o).replace(/</g, '\\\\u003c'); };
    g.data = JG(gridData()); g.back = JG(ScriptApp.getService().getUrl() + '?view=' + VIEW); g.board = JG(BOARD_URL);
    return g.evaluate().setTitle('학생별 진도표').addMetaTag('viewport', 'width=device-width, initial-scale=1');
  }
  if (e && e.parameter && e.parameter.view === VIEW) {
    var t = HtmlService.createTemplate(BOARD_HTML);""")
rep("<a class=rpt id=rpt target=_top>주간 리포트 →</a>", "<a class=rpt id=rpt target=_top>주간 리포트 →</a><a class=rpt id=grd target=_top style=\"right:132px\">진도표 →</a>")
rep('document.getElementById("rpt").href=RU;', 'document.getElementById("rpt").href=RU;document.getElementById("grd").href=RU.replace("&report=1","&grid=1");')
grid = open('work/grid/grid.html', encoding='utf-8').read()
src += '''
/* ==== 진도표 (11/16) ==== */
var BOARD_URL = 'https://cereshk2-hue.github.io/daily-english/t-iyr3rba2/'; // 단원별 전체 DAY 목록을 여기서 읽어요
var NAME_SHOW = { '김혜연': '김샘플' }; // 진도표에서 이름을 바꿔 보여 줄 사람 (선생님 시험용 기록 등)
function gnz(s) { return String(s || '').replace(/\\s+/g, '').replace(/변형어휘/g, '실전어휘뚫기'); }
function gridResets() { /* 11/18 시험 리셋: 보드 progress-map.json 의 시험 [id, short, 제목, 종류, 칸 이름, 리셋ms] → { 단원 이름|제목: 리셋ms } (5분 캐시, 못 읽으면 리셋 없음) */
  var out = {};
  try {
    var c = CacheService.getScriptCache(), hit = c.get('gridResets'); if (hit) return JSON.parse(hit);
    var m = JSON.parse(UrlFetchApp.fetch(BOARD_URL + 'progress-map.json?t=' + Date.now(), { muteHttpExceptions: true }).getContentText());
    Object.keys(m.uk || {}).forEach(function (k) { var u = (m.units || {})[m.uk[k]]; if (!u) return;
      (u.tests || []).forEach(function (t) { if (t[5]) out[k + '|' + gnz(t[2])] = +t[5]; }); });
    c.put('gridResets', JSON.stringify(out), 300);
  } catch (e) {}
  return out;
}
function gridData() { /* '기록' 탭(모든 기록) + '현황' 탭 → 학생·단원·DAY마다 [학생, 학년·교재, 단원, DAY+범위, 진행, 점수(첫 완료), 마지막ms, 완료ms] (그만둔 학생 제외) */
  var ss = SpreadsheetApp.getActiveSpreadsheet(), tz = 'Asia/Seoul', quit = {}, M = {};
  var r = ss.getSheetByName(ROSTER);
  if (r && r.getLastRow() > 1) r.getRange(2, 1, r.getLastRow() - 1, 4).getValues().forEach(function (v) { if (String(v[0]).trim() && /그만|퇴원|차단|정지/.test(String(v[3]))) quit[String(v[0]).trim()] = 1; });
  var ms = function (v) { return v instanceof Date ? v.getTime() : (v ? new Date(v).getTime() || 0 : 0); };
  var FIN = /^(완료|오답 학습 남음)$/, OKP = /^(완료|오답 학습 남음|\\d+\\/\\d+단계)$/;
  function add(n, book, unit, day, prog, score, t) {
    n = String(n).trim(); prog = String(prog).trim(); if (!n || quit[n] || !OKP.test(prog) || !t) return;
    var k = n + '|' + unit + '|' + day, m = M[k] || (M[k] = [n, String(book), String(unit), String(day), '', '', 0, 0, 0]);
    if (FIN.test(prog)) { if (!m[7] || t < m[7]) { m[7] = t; m[5] = String(score); } if (t >= m[8]) { m[8] = t; m[4] = prog; } }
    else if (!m[7] && t >= m[6]) m[4] = prog;
    if (t > m[6]) m[6] = t;
  }
  var RS = gridResets();
  var log = ss.getSheetByName('기록');
  if (log && log.getLastRow() > 1) log.getRange(2, 1, log.getLastRow() - 1, 10).getValues().forEach(function (v) {
    if (/오답 노트/.test(String(v[5]))) return;
    var dd = String(v[4]); if (/^Wrap-up/.test(dd) && String(v[6]).trim()) dd += ' ¦ ' + String(v[6]).trim(); /* 시험은 이름(short)이 겹칠 수 있어 제목(단계 칸)을 붙임 */
    if (/^Wrap-up/.test(dd) && RS[gnz(v[3]) + '|' + gnz(v[6])] > ms(v[0])) return; /* 11/18 리셋한 시험: 리셋 전에 낸 기록은 빼기 */
    add(v[1], v[2], v[3], dd, v[8], v[9], ms(v[0]));
  });
  var sh = ss.getSheetByName('현황');
  if (sh && sh.getLastRow() > 1) sh.getRange(2, 1, sh.getLastRow() - 1, 12).getValues().forEach(function (v) {
    if (/^Wrap-up/.test(String(v[3]))) return; /* 시험은 '기록' 탭(제목 있음)만 씀 */
    add(v[0], v[1], v[2], String(v[3]) + ' ' + String(v[4]), v[5], v[6], ms(v[10]) || ms(v[11]));
  });
  var rows = Object.keys(M).map(function (k) { var m = M[k]; return [NAME_SHOW[m[0]] || m[0], m[1], m[2], m[3], m[4], m[5], m[6], m[7]]; });
  return { today: Utilities.formatDate(new Date(), tz, 'yyyy-MM-dd'), made: Date.now(), rows: rows };
}
var GRID_HTML = ''' + json.dumps(grid, ensure_ascii=False) + ';\n'
open(P, 'w', encoding='utf-8').write(src)
print(len(src))
