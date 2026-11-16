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
function gridData() { /* '현황' 탭 → [학생, 학년·교재, 단원, DAY, 범위, 진행, 점수, 마지막 활동ms, 완료ms] (그만둔 학생 제외) */
  var ss = SpreadsheetApp.getActiveSpreadsheet(), tz = 'Asia/Seoul', quit = {}, rows = [];
  var r = ss.getSheetByName(ROSTER);
  if (r && r.getLastRow() > 1) r.getRange(2, 1, r.getLastRow() - 1, 4).getValues().forEach(function (v) { if (String(v[0]).trim() && /그만|퇴원|차단|정지/.test(String(v[3]))) quit[String(v[0]).trim()] = 1; });
  var sh = ss.getSheetByName('현황'), ms = function (v) { return v instanceof Date ? v.getTime() : (v ? new Date(v).getTime() || 0 : 0); };
  if (sh && sh.getLastRow() > 1) sh.getRange(2, 1, sh.getLastRow() - 1, 12).getValues().forEach(function (v) {
    var n = String(v[0]).trim(); if (!n || quit[n]) return;
    rows.push([n, String(v[1]), String(v[2]), String(v[3]), String(v[4]), String(v[5]), String(v[6]), ms(v[10]), ms(v[11])]);
  });
  return { today: Utilities.formatDate(new Date(), tz, 'yyyy-MM-dd'), made: Date.now(), rows: rows };
}
var GRID_HTML = ''' + json.dumps(grid, ensure_ascii=False) + ';\n'
open(P, 'w', encoding='utf-8').write(src)
print(len(src))
