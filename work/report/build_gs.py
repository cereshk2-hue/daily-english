import json,re
src=open('work/report/base_Code.gs').read()
def rep(a,b):
    global src; assert src.count(a)==1,a; src=src.replace(a,b)
rep("""  if (e && e.parameter && e.parameter.view === VIEW) {
    var t = HtmlService.createTemplate(BOARD_HTML);
    t.data = JSON.stringify(boardData());""","""  if (e && e.parameter && e.parameter.view === VIEW && e.parameter.report) { /* 주간 리포트 (11/6) */
    var rp = HtmlService.createTemplate(REPORT_HTML), J = function (o) { return JSON.stringify(o).replace(/</g, '\\\\u003c'); };
    rp.data = J(reportData(e.parameter.wk, e.parameter.from, e.parameter.to)); rp.url = J(ScriptApp.getService().getUrl()); rp.view = J(VIEW); rp.who = J(String(e.parameter.who || ''));
    return rp.evaluate().setTitle('주간 리포트').addMetaTag('viewport', 'width=device-width, initial-scale=1');
  }
  if (e && e.parameter && e.parameter.view === VIEW) {
    var t = HtmlService.createTemplate(BOARD_HTML);
    t.data = JSON.stringify(boardData()); t.rurl = JSON.stringify(ScriptApp.getService().getUrl() + '?view=' + VIEW + '&report=1');""")
rep("""'</style></head><body><header><h1>학생 현황판</h1>""","""'.rpt{position:absolute;top:18px;right:16px;background:#fff;color:var(--navy);text-decoration:none;font-weight:800;font-size:13px;border-radius:99px;padding:7px 14px}a.tag{text-decoration:none}' +
'</style></head><body><header><h1>학생 현황판</h1><a class=rpt id=rpt target=_top>주간 리포트 →</a>""")
rep("""'<script>var D=<?!= data ?>;' +""","""'<script>var D=<?!= data ?>,RU=<?!= rurl ?>;document.getElementById("rpt").href=RU;' +""")
rep(""""<div class=tags><span class=\\\\"tag o\\\\">완료 DAY \"""",""""<div class=tags><a class=tag target=_top href=\\\\""+E(RU+"&who="+encodeURIComponent(s.name))+"\\\\">주간 리포트 →</a><span class=\\\\"tag o\\\\">완료 DAY \"""")
src=src.rstrip()+'\n\n'+open('report_server.js').read().strip()+'\n\nvar REPORT_HTML = '+json.dumps(open('report.html').read(),ensure_ascii=False)+';\n'
open('Code.gs','w').write(src)
print(len(src))
