/**
 * 데일리 영어 · 학생 학습 기록 받기 (구글 시트 Apps Script)
 * 학생 앱이 단계를 끝낼 때마다 이 시트로 기록을 보냅니다.
 *  - "현황" 탭: 학생 × 단원 × DAY 마다 한 줄. 지금 어디까지 했는지, 점수, 오답 학습, 완료 시각
 *  - "기록" 탭: 들어온 기록 전부 (시간순)
 * 이 파일 전체를 Apps Script 편집기에 붙여 넣고 [배포 → 새 배포 → 웹 앱]으로 배포하세요.
 */
var KEY = 'tBj6XBpuNkxf'; // 학생 앱(config.js)의 SHEET_KEY 와 같아야 해요

var NOW_HEAD = ['학생', '학년·교재', '단원', 'DAY', '범위', '진행', '점수', '오답 학습', '회차', '시작', '마지막 활동', '완료', '걸린 시간(분)', '확인 코드', '틀린 것', '기기', '약한 유형 보충'];
var LOG_HEAD = ['시각', '학생', '학년·교재', '단원', 'DAY', '무엇', '단계', '단계 점수', '진행', '누적 점수', '기기'];

var ROSTER = '학생명단', ROSTER_HEAD = ['이름', '학생 코드', '교재', '메모'];
// 학생은 처음 들어올 때 이름 + 숫자 4자리 코드를 스스로 정하고, 그 줄이 학생명단에 자동으로 생겨요.
// 다음부터는 같은 이름 + 같은 코드여야 들어와요. 코드를 잊은 학생은 학생명단에서 코드를 확인해 알려 주세요.
// 그만둔 학생·모르는 이름은 줄을 지우지 말고 메모 칸에 '그만둠'이라고 적어 두세요(지우면 다시 등록할 수 있어요).
// 교재 칸: 목록에서 고르거나 대충 적어도 돼요(예: 중2 비상). 비워 두면 모든 교재를 열 수 있어요.
// 교재가 두 개면 같은 이름·코드로 줄을 하나 더 적거나, 쉼표로 이어 적어요.
var TEXTBOOKS = ['중1 천재(소영순)', '중1 동아(윤정미)', '중2 동아(윤정미)', '중2 비상(황종배)', '중3 지학사(민찬규)',
  '고1 동아(이병민)', '고1 능률(민병천)', '고1 모의고사', '고2 천재(조수경)', '고2 미래엔(김성연)', '고2 능률(오선영)', '고2 모의고사'];

var VIEW = 'dW6ypYyx'; // 현황판 열쇠: 주소 끝 ?view=dW6ypYyx 가 있어야 학생 현황판이 열려요

function doGet(e) {
  if (e && e.parameter && e.parameter.check) return checkRoster(e.parameter);
  if (e && e.parameter && e.parameter.notes) return getNotes(e.parameter);
  if (e && e.parameter && e.parameter.view === VIEW && e.parameter.report) { /* 주간 리포트 (11/6) */
    var rp = HtmlService.createTemplate(REPORT_HTML), J = function (o) { return JSON.stringify(o).replace(/</g, '\\u003c'); };
    rp.data = J(reportData(e.parameter.wk, e.parameter.from, e.parameter.to)); rp.url = J(ScriptApp.getService().getUrl()); rp.view = J(VIEW); rp.who = J(String(e.parameter.who || ''));
    return rp.evaluate().setTitle('주간 리포트').addMetaTag('viewport', 'width=device-width, initial-scale=1');
  }
  if (e && e.parameter && e.parameter.view === VIEW) {
    var t = HtmlService.createTemplate(BOARD_HTML);
    t.data = JSON.stringify(boardData()); t.rurl = JSON.stringify(ScriptApp.getService().getUrl() + '?view=' + VIEW + '&report=1');
    return t.evaluate().setTitle('학생 현황판').addMetaTag('viewport', 'width=device-width, initial-scale=1');
  }
  return ContentService.createTextOutput('데일리 영어 기록 받기: 작동 중이에요.');
}

/* 기록 탭을 학생별로 모아 현황판 카드 데이터로 만든다 */
function boardData() {
  var ss = SpreadsheetApp.getActiveSpreadsheet(), tz = 'Asia/Seoul';
  var today = Utilities.formatDate(new Date(), tz, 'yyyy-MM-dd');
  var log = ss.getSheetByName('기록'), now = ss.getSheetByName('현황'), S = {};
  function st(name) { return S[name] || (S[name] = { name: name, grades: {}, last: 0, mins: 0, minsToday: 0, solved: 0, right: 0, solvedToday: 0, days: 0, reviewLeft: 0, weakLeft: 0, rows: [], _t: [], nAll: 0, nLeft: 0, nTimes: 0, nToday: 0, nBook: {}, noteT: 0, noteC: 0, noteDays: {}, noteLast: 0 }); }
  if (log && log.getLastRow() > 1) {
    log.getRange(2, 1, log.getLastRow() - 1, 8).getValues().forEach(function (v) {
      if (!v[1]) return;
      var s = st(String(v[1])), t = v[0] instanceof Date ? v[0].getTime() : 0;
      if (!t) return;
      s._t.push(t); if (t > s.last) s.last = t;
      var g = String(v[2]).split(' ')[0]; if (g) s.grades[g] = 1;
      var m = /^(\d+)\/(\d+)$/.exec(String(v[7]));
      if (m) { s.solved += +m[2]; s.right += +m[1]; if (Utilities.formatDate(v[0], tz, 'yyyy-MM-dd') === today) s.solvedToday += +m[2]; }
      if (/오답 노트/.test(String(v[5]))) { /* 오답 학습 기록: 오늘 몇 문제 · 최근 7일 며칠 */
        var dk = Utilities.formatDate(v[0], tz, 'yyyy-MM-dd'), nm = /(\d+)\/(\d+)\s*$/.exec(String(v[7]));
        s.noteDays[dk] = 1; if (t > s.noteLast) s.noteLast = t;
        if (nm && dk === today) { s.noteT += +nm[2]; s.noteC += +nm[1]; }
      }
    });
  }
  Object.keys(S).forEach(function (k) { /* 학습 시간: 기록 사이 간격을 더하되 15분 넘게 비면 쉬었다고 본다 */
    var s = S[k], ts = s._t.sort(function (a, b) { return a - b; });
    for (var i = 1; i < ts.length; i++) { var gap = ts[i] - ts[i - 1]; if (gap > 0 && gap <= 15 * 60000) { s.mins += gap / 60000; if (Utilities.formatDate(new Date(ts[i]), tz, 'yyyy-MM-dd') === today) s.minsToday += gap / 60000; } }
    s.mins = Math.round(s.mins); s.minsToday = Math.round(s.minsToday); delete s._t;
  });
  if (now && now.getLastRow() > 1) {
    now.getRange(2, 1, now.getLastRow() - 1, 17).getValues().forEach(function (v) {
      if (!v[0]) return;
      var s = st(String(v[0])), g = String(v[1]).split(' ')[0]; if (g) s.grades[g] = 1;
      var last = v[10] instanceof Date ? v[10].getTime() : 0; if (last > s.last) s.last = last;
      if (v[5] === '완료') s.days++;
      if (v[5] === '오답 학습 남음') s.reviewLeft++;
      if (/보충 안 함/.test(String(v[16]))) s.weakLeft++;
      s.rows.push({ book: String(v[1]), unit: String(v[2]), day: String(v[3]), range: String(v[4]), prog: String(v[5]), score: String(v[6]), review: String(v[7]), last: last, weak: String(v[16]) });
    });
  }
  /* 누적 오답: '오답노트' 탭 (학생 앱이 틀린 문제·헷갈려요를 모아 둔 것) */
  var nt = ss.getSheetByName(NOTE);
  if (nt && nt.getLastRow() > 1) {
    nt.getRange(2, 1, nt.getLastRow() - 1, 10).getValues().forEach(function (v) {
      if (!v[0] || /^Wrap-up/.test(String(v[2]))) return; /* Wrap-up은 종이로 오답 정리 → 오답 수에서 뺌 */
      var s = st(String(v[0])), bk = String(v[1]).replace(/\(.*$/, '').trim() || '기타', left = String(v[8]) !== '맞힘';
      s.nAll++; if (left) s.nLeft++; s.nTimes += +v[6] || 0;
      if (v[9] instanceof Date && Utilities.formatDate(v[9], tz, 'yyyy-MM-dd') === today && +v[6] > 0) s.nToday++;
      var b = s.nBook[bk] || (s.nBook[bk] = { all: 0, left: 0 }); b.all++; if (left) b.left++;
    });
  }
  var since7 = Utilities.formatDate(new Date(Date.now() - 6 * 86400000), tz, 'yyyy-MM-dd');
  var list = Object.keys(S).map(function (k) { var s = S[k]; s.grades = Object.keys(s.grades);
    s.note7 = Object.keys(s.noteDays).filter(function (x) { return x >= since7; }).length; delete s.noteDays; s.rows.sort(function (a, b) { return b.last - a.last; }); return s; });
  list.sort(function (a, b) { return b.last - a.last; });
  return { today: today, made: Date.now(), list: list };
}

var BOARD_HTML = '<!doctype html><html><head><base target="_top"><meta charset="utf-8">' +
'<style>' +
'@import url("https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700;800&display=swap");' +
':root{--bg:#f5f6fa;--card:#fff;--ink:#0f172a;--muted:#64748b;--line:#e6e9f0;--blue:#2643c4;--soft:#eef1fd;--navy:#101a3a;--ok:#12805c;--oks:#e7f6ef;--warn:#b26a00;--warns:#fff3dc;--bad:#d1435b;--bads:#fdecef}' +
'*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.5 "Noto Sans KR",-apple-system,"Apple SD Gothic Neo",sans-serif;-webkit-font-smoothing:antialiased;letter-spacing:-.005em}' +
'header{position:relative;overflow:hidden;background:var(--navy);color:#fff;padding:18px 16px 16px}header:before{content:"";position:absolute;right:-80px;bottom:-150px;width:300px;height:300px;border-radius:50%;background:radial-gradient(circle,rgba(84,118,255,.5),transparent 65%)}header>*{position:relative}' +
'h1{margin:0;font-size:24px;font-weight:800;letter-spacing:-.02em}' +
'.sub{font-size:12.5px;color:#aab6d8;margin-top:2px}.bar{display:flex;gap:6px;overflow-x:auto;margin-top:14px;padding-bottom:2px;scrollbar-width:none}' +
'.bar button{flex:none;border:0;border-radius:99px;padding:7px 14px;font:inherit;font-size:13px;font-weight:700;background:rgba(255,255,255,.1);color:#c9d3ee}.bar button.on{background:#fff;color:var(--navy)}' +
'input{width:100%;margin-top:10px;border:0;border-radius:12px;padding:10px 14px;font:inherit;background:rgba(255,255,255,.12);color:#fff}input::placeholder{color:#aab6d8}' +
'main{max-width:680px;margin:0 auto;padding:14px 14px 40px}.sum{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin:0 0 14px}.sum div{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:10px 12px}.sum small{display:block;font-size:11.5px;color:var(--muted)}.sum b{font-size:19px;font-weight:800}' +
'.card{background:var(--card);border-radius:18px;padding:16px;margin-bottom:12px;box-shadow:0 1px 2px rgba(15,23,42,.04),0 8px 24px rgba(15,23,42,.06)}' +
'.top{display:flex;align-items:center;gap:12px}.av{flex:none;width:44px;height:44px;border-radius:14px;background:var(--blue);color:#fff;display:grid;place-items:center;font-weight:800;font-size:17px}' +
'.nm{font-size:18px;font-weight:800;letter-spacing:-.02em}.gr{font-size:12.5px;color:var(--muted);margin-left:6px;font-weight:500}.when{margin-left:auto;font-size:12px;color:var(--muted);text-align:right;font-weight:600;white-space:nowrap}' +
'.when.today{color:var(--ok)}.when.old{color:var(--bad)}' +
'.grid{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-top:14px}.grid div{background:var(--bg);border-radius:12px;padding:9px 12px}.grid small{display:block;color:var(--muted);font-size:11.5px}.grid b{font-size:17px;font-weight:800;letter-spacing:-.02em}' +
'.tags{display:flex;flex-wrap:wrap;gap:6px;margin-top:12px}.tag{font-size:12px;font-weight:700;border-radius:99px;padding:4px 10px;background:var(--soft);color:var(--blue)}.tag.w{background:var(--warns);color:var(--warn)}.tag.b{background:var(--bads);color:var(--bad)}.tag.o{background:var(--oks);color:var(--ok)}' +
'details{margin-top:12px;border-top:1px solid var(--line);padding-top:10px}summary{cursor:pointer;color:var(--blue);font-size:13px;font-weight:700}' +
'.row{padding:9px 0;border-bottom:1px solid var(--line);font-size:13px}.row:last-child{border:0}.row .u{color:var(--muted)}.row .p{font-weight:800}.row .p.done{color:var(--ok)}.row .p.rev{color:var(--warn)}.row .wk{color:var(--bad);font-size:12px}' +
'.empty{text-align:center;color:var(--muted);padding:40px 0}' +
'.sum{grid-template-columns:repeat(4,1fr)}@media(max-width:480px){.sum{grid-template-columns:repeat(2,1fr)}}' +
'.grid .nb small:last-child{font-size:11px}.grid .nb.lf{background:var(--bads)}.grid .nb.lf b{color:var(--bad)}.grid .nb.ok{background:var(--oks)}.grid .nb.ok b{color:var(--ok)}' +
'.nbk{display:flex;flex-wrap:wrap;gap:6px 12px;margin-top:8px;font-size:12.5px;color:var(--muted)}.nbk b{color:var(--ink)}.nbk i{font-style:normal;color:var(--bad);font-weight:700}' +
'.rpt{position:absolute;top:18px;right:16px;background:#fff;color:var(--navy);text-decoration:none;font-weight:800;font-size:13px;border-radius:99px;padding:7px 14px}a.tag{text-decoration:none}' +
'</style></head><body><header><h1>학생 현황판</h1><a class=rpt id=rpt target=_top>주간 리포트 →</a><div class="sub" id="made"></div><div class="bar" id="bar"></div><input id="q" placeholder="이름 찾기"></header><main><div class="sum" id="sum"></div><div id="list"></div></main>' +
'<script>var D=<?!= data ?>,RU=<?!= rurl ?>;document.getElementById("rpt").href=RU;' +
'var F="all",Q="";function E(s){return String(s==null?"":s).replace(/[&<>"]/g,function(c){return{"&":"&amp;","<":"&lt;",">":"&gt;","\\"":"&quot;"}[c]})}' +
'function dk(t){var d=new Date(t);return d.getFullYear()+"-"+("0"+(d.getMonth()+1)).slice(-2)+"-"+("0"+d.getDate()).slice(-2)}' +
'function ft(t){if(!t)return"기록 없음";var d=new Date(t),w="일월화수목금토"[d.getDay()];return(d.getMonth()+1)+"/"+d.getDate()+"("+w+") "+("0"+d.getHours()).slice(-2)+":"+("0"+d.getMinutes()).slice(-2)}' +
'function hm(m){return m>=60?Math.floor(m/60)+"시간 "+(m%60)+"분":m+"분"}' +
'var G={};D.list.forEach(function(s){s.grades.forEach(function(g){G[g]=1})});' +
'var B=[["all","전체"],["notoday","오늘 안 한 학생"],["todo","할 일 남은 학생"],["nonote","오답 학습 안 한 학생"],["wrong","오답 많은 순"]].concat(Object.keys(G).sort().map(function(g){return["g:"+g,g]}));' +
'function bar(){document.getElementById("bar").innerHTML=B.map(function(b){return"<button data-f=\\""+b[0]+"\\" class=\\""+(F===b[0]?"on":"")+"\\">"+E(b[1])+"</button>"}).join("");' +
'[].forEach.call(document.querySelectorAll("[data-f]"),function(x){x.onclick=function(){F=x.dataset.f;bar();draw()}})}' +
'function draw(){var L=D.list.filter(function(s){if(Q&&s.name.indexOf(Q)<0)return false;if(F==="notoday")return dk(s.last)!==D.today;if(F==="todo")return s.reviewLeft||s.weakLeft;if(F==="nonote")return s.nLeft>0&&!s.noteT;if(F.indexOf("g:")===0)return s.grades.indexOf(F.slice(2))>=0;return true});if(F==="wrong")L=L.slice().sort(function(a,b){return(b.nLeft-a.nLeft)||(b.nAll-a.nAll)});' +
'var td=D.list.filter(function(s){return dk(s.last)===D.today}).length;' +
'var todo=D.list.filter(function(s){return s.reviewLeft||s.weakLeft}).length;var nl=D.list.reduce(function(n,s){return n+(s.nLeft||0)},0);document.getElementById("sum").innerHTML="<div><small>전체 학생</small><b>"+D.list.length+"명</b></div><div><small>오늘 학습</small><b>"+td+"명</b></div><div><small>할 일 남음</small><b>"+todo+"명</b></div><div><small>못 맞힌 오답 (전체)</small><b>"+nl+"문제</b></div>";' +
'document.getElementById("list").innerHTML=L.length?L.map(function(s){var age=(Date.now()-s.last)/864e5,cls=dk(s.last)===D.today?"today":age>3?"old":"";' +
'var acc=s.solved?Math.round(s.right/s.solved*100):0;' +
'return"<div class=card><div class=top><div class=av>"+E(s.name.charAt(0))+"</div><div><span class=nm>"+E(s.name)+"</span><span class=gr>"+E(s.grades.join(" · "))+"</span></div><div class=\\"when "+cls+"\\">"+(cls==="today"?"오늘 ":"")+ft(s.last)+"</div></div>"+' +
'"<div class=grid><div><small>누적 학습시간</small><b>"+hm(s.mins)+"</b></div><div><small>오늘 학습시간</small><b>"+hm(s.minsToday)+"</b></div>"+' +
'"<div><small>누적 푼 문제</small><b>"+s.solved+"문제</b></div><div><small>정답률 · 틀린 문제</small><b>"+acc+"% · "+(s.solved-s.right)+"개</b></div>"+' +
'"<div class=nb><small>누적 오답 (오답 노트)</small><b>"+s.nAll+"문제</b><small>틀린 횟수 합 "+s.nTimes+"번</small></div><div class=\\""+(s.nLeft?"nb lf":"nb ok")+"\\"><small>아직 못 맞힌 오답</small><b>"+s.nLeft+"문제</b><small>"+(s.nAll?"다시 맞힘 "+(s.nAll-s.nLeft)+"문제":"오답 없음")+"</small></div></div>"+' +
'(Object.keys(s.nBook).length?"<div class=nbk>"+Object.keys(s.nBook).map(function(k){var b=s.nBook[k];return"<span>"+E(k)+" <b>"+b.all+"</b>"+(b.left?" <i>남음 "+b.left+"</i>":" ✓")+"</span>"}).join("")+"</div>":"")+' +
'"<div class=tags><a class=tag target=_top href=\\""+E(RU+"&who="+encodeURIComponent(s.name))+"\\">주간 리포트 →</a><span class=\\"tag o\\">완료 DAY "+s.days+"개</span>"+(s.reviewLeft?"<span class=\\"tag w\\">오답 학습 남음 "+s.reviewLeft+"</span>":"")+(s.weakLeft?"<span class=\\"tag b\\">약한 유형 보충 안 함 "+s.weakLeft+"</span>":"")+(s.solvedToday?"<span class=tag>오늘 "+s.solvedToday+"문제</span>":"")+(s.noteT?"<span class=\\"tag o\\">오늘 오답 학습 "+s.noteT+"문제 · "+s.noteC+"개 맞힘</span>":(s.nLeft?"<span class=\\"tag b\\">오늘 오답 학습 안 함</span>":""))+(s.note7?"<span class=tag>최근 7일 오답 학습 "+s.note7+"일</span>":"")+(s.nToday?"<span class=\\"tag b\\">오늘 새 오답 "+s.nToday+"</span>":"")+"</div>"+' +
'(s.rows.length?"<details><summary>단원·DAY별 보기 ("+s.rows.length+")</summary>"+s.rows.map(function(r){var pc=r.prog==="완료"?"done":r.prog==="오답 학습 남음"?"rev":"";' +
'return"<div class=row><div><span class=\\"p "+pc+"\\">"+E(r.day)+" · "+E(r.prog)+"</span> "+E(r.score)+"</div><div class=u>"+E(r.book)+" · "+E(r.unit)+" · "+E(r.range)+" · "+ft(r.last)+"</div>"+(r.weak?"<div class=wk>"+E(r.weak)+"</div>":"")+"</div>"}).join("")+"</details>":"")+"</div>"}).join(""):"<p class=empty>해당하는 학생이 없어요.</p>"}' +
'document.getElementById("made").textContent=ft(D.made)+" 기준 · 새로고침하면 최신으로 바뀌어요";' +
'document.getElementById("q").oninput=function(){Q=this.value.trim();draw()};bar();draw();</script></body></html>';

function doPost(e) {
  var data;
  try { data = JSON.parse(e.postData.contents); } catch (err) { return out('bad'); }
  if (!data || data.k !== KEY) return out('no');
  if (data.notes && data.notes.length) saveNotes(data.notes);
  if (!data.rows || !data.rows.length) return out('ok');
  var lock = LockService.getScriptLock();
  lock.waitLock(20000);
  try {
    var ss = SpreadsheetApp.getActiveSpreadsheet();
    var log = sheet(ss, '기록', LOG_HEAD), now = sheet(ss, '현황', NOW_HEAD);
    var seen = CacheService.getScriptCache();
    var logRows = [];
    var vals = now.getLastRow() > 1 ? now.getRange(2, 1, now.getLastRow() - 1, 5).getValues() : [];
    var index = {};
    vals.forEach(function (v, i) { index[v[0] + '|' + v[2] + '|' + v[3]] = i + 2; });
    data.rows.forEach(function (r) {
      var id = 'r' + r.t + '|' + r.name + '|' + r.kind;          // 같은 기록이 두 번 와도 한 번만
      if (seen.get(id)) return;
      seen.put(id, '1', 21600);
      var prog = r.finished ? (r.review === '안 함' ? '오답 학습 남음' : '완료') : r.done + '/' + r.total + '단계';
      var score = r.tt ? r.pct + '점 (' + r.c + '/' + r.tt + ')' : '';
      logRows.push([d(r.t), r.name, r.school, r.unit, r.day + ' ' + r.range, r.kind, r.step || '', r.stepScore || '', prog, score, r.dev]);
      var row = [r.name, r.school, r.unit, r.day, r.range, prog, score,
        r.finished ? (r.review || '') : (r.wrongN ? '틀린 문제 ' + r.wrongN + '개' : ''),
        r.attempt, d(r.started), d(r.t), d(r.ended), r.mins || '', r.code || '', r.wrong || '', r.dev, r.weak || ''];
      var key = r.name + '|' + r.unit + '|' + r.day, at = index[key];
      if (at) {
        var oldLast = now.getRange(at, 11).getValue();
        if (oldLast && oldLast > d(r.t)) return;                 // 늦게 도착한 옛 기록은 덮어쓰지 않기
        now.getRange(at, 1, 1, row.length).setValues([row]);
      } else {
        now.appendRow(row); index[key] = now.getLastRow();
      }
      color(now, index[key], r);
    });
    if (logRows.length) log.getRange(log.getLastRow() + 1, 1, logRows.length, LOG_HEAD.length).setValues(logRows);
  } finally { lock.releaseLock(); }
  return out('ok');
}

function color(sh, row, r) {
  var bg = r.finished ? (r.review === '안 함' ? '#fff4d6' : '#e3f4e6') : '#ffffff';
  sh.getRange(row, 1, 1, NOW_HEAD.length).setBackground(bg);
}

function sheet(ss, name, head) {
  var sh = ss.getSheetByName(name);
  if (!sh) {
    sh = ss.insertSheet(name, name === '현황' ? 0 : ss.getSheets().length);
    sh.getRange(1, 1, 1, head.length).setValues([head]).setFontWeight('bold').setBackground('#2f5fd0').setFontColor('#ffffff');
    sh.setFrozenRows(1);
    if (name === '현황') { sh.getRange('A:Q').createFilter(); sh.getRange('J:L').setNumberFormat('m/d hh:mm'); sh.getRange('F:G').setNumberFormat('@'); }
    else { sh.getRange('A:A').setNumberFormat('m/d hh:mm'); sh.getRange('G:J').setNumberFormat('@'); }
    sh.getRange(1, 1, 1, head.length).setFontWeight('bold').setBackground('#2f5fd0').setFontColor('#ffffff');
  }
  return sh;
}

function d(t) { return t ? new Date(t) : ''; }
function out(s) { return ContentService.createTextOutput(s); }

/* 학생 앱이 물어봄: 명단이 켜져 있나(gate), 이 이름 + 코드가 명단에 있고 이 교재가 열려 있나(ok, why) */
function nc(c) { return String(c == null ? '' : c).replace(/\D/g, '').replace(/^0+/, ''); }
function nb(t) { return String(t == null ? '' : t).toLowerCase().replace(/[\s()·.\-]/g, ''); }
function bookOk(cell, school) {
  var want = nb(school), parts = String(cell == null ? '' : cell).split(/[,/\n]/).map(nb).filter(String);
  if (!parts.length) return true; // 비어 있으면 전부
  return parts.some(function (x) { return want.indexOf(x) >= 0 || x.indexOf(want) >= 0; });
}
function bookList() {
  var pr = PropertiesService.getScriptProperties(), l = [];
  try { l = JSON.parse(pr.getProperty('books') || '[]'); } catch (e) {}
  TEXTBOOKS.forEach(function (b) { if (l.indexOf(b) < 0) l.push(b); });
  return l;
}
function bookRule(sh, list) {
  var rule = SpreadsheetApp.newDataValidation().requireValueInList(list, true).setAllowInvalid(true)
    .setHelpText('목록에서 고르거나 직접 적어요(예: 중2 비상). 비워 두면 모든 교재.').build();
  sh.getRange(2, 3, Math.max(sh.getMaxRows() - 1, 1), 1).setDataValidation(rule);
}
function rosterSheet(ss) {
  var sh = ss.getSheetByName(ROSTER);
  var ready = sh && String(sh.getRange(1, 3).getValue()) === '교재';
  if (ready) return sh;
  var lock = LockService.getScriptLock(); lock.waitLock(20000);
  try {
    sh = ss.getSheetByName(ROSTER);
    if (!sh) { sh = sheet(ss, ROSTER, ROSTER_HEAD); }
    else if (String(sh.getRange(1, 3).getValue()) !== '교재') { // 예전 명단(이름·코드·메모) → 교재 칸 끼워 넣기
      sh.insertColumnAfter(2);
      sh.getRange(1, 3).setValue('교재').setFontWeight('bold').setBackground('#2f5fd0').setFontColor('#ffffff');
    }
    sh.getRange('B:B').setNumberFormat('@'); sh.setColumnWidth(3, 200); sh.setColumnWidth(4, 200);
    bookRule(sh, bookList());
  } finally { lock.releaseLock(); }
  return sh;
}
function learnBook(sh, school) { // 새 교재 링크가 처음 열리면 교재 목록에 자동으로 추가
  if (!school) return;
  var l = bookList();
  if (l.some(function (b) { return nb(school).indexOf(nb(b)) >= 0 || nb(b) === nb(school); })) return;
  l.push(String(school)); PropertiesService.getScriptProperties().setProperty('books', JSON.stringify(l)); bookRule(sh, l);
}
function checkRoster(p) {
  /* 학생 스스로 등록: 처음 들어오는 이름 + 4자리 코드 → 학생명단에 자동으로 한 줄. 이미 있는 이름은 코드가 맞아야.
     메모 칸에 '그만둠'(또는 차단·퇴원)이라고 적힌 이름은 들어올 수 없음 (줄을 지우면 다시 등록할 수 있으니 지우지 말고 메모에 적기) */
  var res = { gate: true, ok: false, why: '' };
  try {
    var ss = SpreadsheetApp.getActiveSpreadsheet(), sh = rosterSheet(ss);
    try { learnBook(sh, p.school); } catch (e2) {}
    var read = function () { return sh.getLastRow() > 1 ? sh.getRange(2, 1, sh.getLastRow() - 1, 4).getValues().filter(function (v) { return String(v[0]).trim(); }) : []; };
    var n = String(p.name || '').replace(/\s+/g, ''), c = nc(p.code), raw = String(p.code || '').replace(/\D/g, '');
    var BLOCK = /그만|차단|퇴원|정지/;
    var same = function (rows) { return rows.filter(function (v) { return n && String(v[0]).replace(/\s+/g, '') === n; }); };
    var judge = function (mine) {
      if (mine.some(function (v) { return BLOCK.test(String(v[3])); })) { res.why = 'blocked'; return; }
      var ok = mine.filter(function (v) { return c && nc(v[1]) === c; });
      if (!ok.length) res.why = 'code';
      else if (ok.some(function (v) { return bookOk(v[2], p.school); })) res.ok = true;
      else res.why = 'unit';
    };
    var mine = same(read());
    if (mine.length) judge(mine);
    else if (p.reg === '1' && /^[가-힣]{2,5}$/.test(n) && /^\d{4}$/.test(raw)) {
      var lock = LockService.getScriptLock(); lock.waitLock(20000);
      try {
        mine = same(read());
        if (mine.length) judge(mine);
        else { sh.appendRow([n, raw, '', '자동 등록 ' + Utilities.formatDate(new Date(), 'Asia/Seoul', 'M/d HH:mm')]); res.ok = true; res.isNew = true; }
      } finally { lock.releaseLock(); }
    } else res.why = n ? 'new' : 'code';
  } catch (err) { res = { gate: false, ok: false, why: '' }; }
  return json(res);
}

/** 처음 한 번 실행: 탭 만들기 + 권한 허용 */
function setup() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  sheet(ss, '현황', NOW_HEAD); sheet(ss, '기록', LOG_HEAD); rosterSheet(ss); analysis();
  var first = ss.getSheetByName('시트1') || ss.getSheetByName('Sheet1');
  if (first && ss.getSheets().length > 2 && first.getLastRow() === 0) ss.deleteSheet(first);
}


/* ---------- 오답 노트: 학생 이름에 붙여 저장 → 어느 기기에서든 같은 노트, 선생님은 '오답노트' 탭에서 확인 ---------- */
var NOTE = '오답노트', NOTE_HEAD = ['학생', '교재', 'DAY', '과·DAY', '단계', '문제', '틀린 횟수', '헷갈려요', '상태', '마지막', 'key', 'data'];
function noteSheet(ss) {
  var sh = ss.getSheetByName(NOTE);
  if (!sh) {
    sh = ss.insertSheet(NOTE, ss.getSheets().length);
    sh.getRange(1, 1, 1, NOTE_HEAD.length).setValues([NOTE_HEAD]).setFontWeight('bold').setBackground('#2f5fd0').setFontColor('#ffffff');
    sh.setFrozenRows(1); sh.getRange('J:J').setNumberFormat('m/d hh:mm'); sh.getRange('K:L').setNumberFormat('@');
    sh.setColumnWidth(6, 360); sh.hideColumns(11, 2); sh.getRange(1, 1, 1, 10).createFilter();
  }
  return sh;
}
function saveNotes(list) {
  var lock = LockService.getScriptLock(); lock.waitLock(20000);
  try {
    var sh = noteSheet(SpreadsheetApp.getActiveSpreadsheet());
    list.forEach(function (n) {
      if (!n || !n.name || !n.unit || !n.id) return;
      var key = n.name + '|' + n.unit + '|' + n.id, last = sh.getLastRow();
      var hit = last > 1 ? sh.getRange(2, 11, last - 1, 1).createTextFinder(key).matchEntireCell(true).findNext() : null;
      if (n.del) { if (hit) sh.deleteRow(hit.getRow()); return; }
      if (hit) { var old = sh.getRange(hit.getRow(), 10).getValue(); if (old instanceof Date && old.getTime() > n.at) return; }
      var row = [n.name, n.school || '', n.day || '', n.group || '', n.step || '', String(n.text || '').slice(0, 300), n.wrong || 0,
                 n.conf ? '★' : '', n.ok ? '맞힘' : '남음', new Date(n.at || Date.now()), key, String(n.data || '').slice(0, 45000)];
      if (hit) sh.getRange(hit.getRow(), 1, 1, row.length).setValues([row]); else sh.appendRow(row);
    });
  } finally { lock.releaseLock(); }
}
function getNotes(p) {
  var res = { ok: false, notes: [] };
  try {
    var ss = SpreadsheetApp.getActiveSpreadsheet(), name = String(p.name || '').replace(/\s+/g, ''), unit = String(p.unit || '');
    if (!name || !unit) throw 0;
    var r = ss.getSheetByName(ROSTER), rows = r && r.getLastRow() > 1 ? r.getRange(2, 1, r.getLastRow() - 1, 2).getValues().filter(function (v) { return String(v[0]).trim(); }) : [];
    if (rows.length && !rows.some(function (v) { return String(v[0]).replace(/\s+/g, '') === name && nc(v[1]) === nc(p.code) && nc(p.code); })) return json(res);
    var sh = ss.getSheetByName(NOTE); res.ok = true;
    if (sh && sh.getLastRow() > 1) sh.getRange(2, 11, sh.getLastRow() - 1, 2).getValues().forEach(function (v) {
      if (String(v[0]).indexOf(name + '|' + unit + '|') === 0 && v[1]) res.notes.push(String(v[1]));
    });
  } catch (err) {}
  return json(res);
}
function json(o) { return ContentService.createTextOutput(JSON.stringify(o)).setMimeType(ContentService.MimeType.JSON); }

/* ---------- 학생별 분석 탭 (11/1) ----------
 * '기록'(단계마다 맞힌 수) · '오답노트' · '현황'(Wrap-up 점수)을 학생 이름별로 모아
 * 누가 얼마나 공부하고 있는지, 어떤 유형이 가장 약한지 한눈에 보여 준다.
 * 시트 위 메뉴 [데일리 영어 → 학생별 분석 새로고침] 또는 매시간 자동(메뉴에서 한 번 켜기). */
var ANA = '학생별 분석';
var TYPES = [ // [묶음 이름, 단계 이름에 들어 있는 말] · 위에서부터 먼저 맞는 것
  ['영작·배열', /스크램블|배열|영작|바꿔 쓰기|(으로|형태로|동사로) 쓰기|서술/], ['어휘', /어휘|단어|숙어|유의어|반의어|철자/],
  ['대화문', /대화|의사소통|응답/], ['어법', /어법|동사변형|오류/],
  ['문법 개념', /문법|개념|용법|역할|쓰임|to부정사|S · O · C|동사|하는 것|같은 것끼리|개수 세기|세 개 중/],
  ['내용 일치', /T\/F|일치|내용/], ['해석', /해석|끊어 보기/], ['대의(주제·요지·제목)', /주제|요지|제목|주장|함축|목적/],
  ['빈칸', /빈칸/], ['순서·삽입·흐름', /순서|삽입|어색|흐름|무관/], ['요약문', /요약/], ['실전 문제', /실전/]];
var TYPE_NAMES = TYPES.map(function (t) { return t[0]; });
function typeOf(step) {
  var s = String(step || '').replace(/^\d+\.\s*/, '').trim(); if (!s) return '';
  for (var i = 0; i < TYPES.length; i++) if (TYPES[i][1].test(s)) return TYPES[i][0];
  return '기타';
}
function onOpen() {
  SpreadsheetApp.getUi().createMenu('데일리 영어')
    .addItem('학생별 분석 새로고침', 'analysis')
    .addItem('학생별 분석 매시간 자동 새로고침 켜기', 'analysisAuto')
    .addToUi();
}
function analysisAuto() {
  ScriptApp.getProjectTriggers().forEach(function (t) { if (t.getHandlerFunction() === 'analysis') ScriptApp.deleteTrigger(t); });
  ScriptApp.newTrigger('analysis').timeBased().everyHours(1).create();
  analysis();
  try { SpreadsheetApp.getUi().alert('학생별 분석이 매시간 자동으로 새로고침돼요.'); } catch (e) {}
}
function analysis() {
  var ss = SpreadsheetApp.getActiveSpreadsheet(), tz = 'Asia/Seoul', S = {};
  function st(n) { return S[n] || (S[n] = { name: n, books: {}, days: {}, last: 0, t: [], solved: 0, right: 0, ty: {}, nLeft: 0, nAll: 0, nTy: {}, wrap: [], fin: 0, revLeft: 0, noteDays: {}, noteLast: 0, noteT: 0, noteC: 0 }); }
  var quit = {};
  var r = ss.getSheetByName(ROSTER);
  if (r && r.getLastRow() > 1) r.getRange(2, 1, r.getLastRow() - 1, 4).getValues().forEach(function (v) { if (String(v[0]).trim() && /그만/.test(String(v[3]))) quit[String(v[0]).trim()] = 1; });
  var log = ss.getSheetByName('기록');
  if (log && log.getLastRow() > 1) log.getRange(2, 1, log.getLastRow() - 1, 8).getValues().forEach(function (v) {
    var n = String(v[1]).trim(); if (!n || !(v[0] instanceof Date)) return;
    var s = st(n), t = v[0].getTime();
    s.t.push(t); if (t > s.last) s.last = t; s.days[Utilities.formatDate(v[0], tz, 'yyyy-MM-dd')] = 1;
    if (v[2]) s.books[String(v[2])] = 1;
    if (/오답 노트/.test(String(v[5]))) {
      var dk = Utilities.formatDate(v[0], tz, 'yyyy-MM-dd'), nm = /(\d+)\/(\d+)\s*$/.exec(String(v[7]));
      s.noteDays[dk] = 1; if (t > s.noteLast) s.noteLast = t;
      if (nm && dk === Utilities.formatDate(new Date(), tz, 'yyyy-MM-dd')) { s.noteT += +nm[2]; s.noteC += +nm[1]; }
      return;
    }
    if (!/단계 완료|DAY 완료/.test(String(v[5]))) return;           // 처음 배우는 단계만 (오답 노트 다시 풀기는 빼고)
    var m = /^(\d+)\/(\d+)/.exec(String(v[7])); if (!m) return;
    var c = +m[1], a = +m[2]; if (!a) return;
    s.solved += a; s.right += c;
    var ty = typeOf(v[6]); if (!ty) return;
    var x = s.ty[ty] || (s.ty[ty] = { c: 0, a: 0 }); x.c += c; x.a += a;
  });
  var nt = ss.getSheetByName(NOTE);
  if (nt && nt.getLastRow() > 1) nt.getRange(2, 1, nt.getLastRow() - 1, 9).getValues().forEach(function (v) {
    var n = String(v[0]).trim(); if (!n || /^Wrap-up/.test(String(v[2]))) return;
    var s = st(n), left = String(v[8]) !== '맞힘', ty = typeOf(v[4]) || '기타';
    s.nAll++; if (left) { s.nLeft++; s.nTy[ty] = (s.nTy[ty] || 0) + 1; }
  });
  var now = ss.getSheetByName('현황');
  if (now && now.getLastRow() > 1) now.getRange(2, 1, now.getLastRow() - 1, 8).getValues().forEach(function (v) {
    var n = String(v[0]).trim(); if (!n) return;
    var s = st(n); if (v[1]) s.books[String(v[1])] = 1;
    if (/^Wrap-up/.test(String(v[3]))) { var p = /^(\d+)점/.exec(String(v[6])); s.wrap.push(String(v[3]).replace('Wrap-up ', '') + ' ' + (p ? p[1] + '점' : String(v[6]))); return; }
    if (v[5] === '완료') s.fin++; if (v[5] === '오답 학습 남음') { s.fin++; s.revLeft++; }
  });
  var MIN = 6; // 유형마다 6문제 이상 풀어야 약점으로 판단
  var list = Object.keys(S).filter(function (n) { return !quit[n]; }).map(function (n) {
    var s = S[n], ts = s.t.sort(function (a, b) { return a - b; }), mins = 0;
    for (var i = 1; i < ts.length; i++) { var g = ts[i] - ts[i - 1]; if (g > 0 && g <= 15 * 60000) mins += g / 60000; }
    s.mins = Math.round(mins);
    var since7 = Utilities.formatDate(new Date(Date.now() - 6 * 86400000), tz, 'yyyy-MM-dd');
    s.note7 = Object.keys(s.noteDays).filter(function (x) { return x >= since7; }).length;
    var ranked = Object.keys(s.ty).filter(function (k) { return s.ty[k].a >= MIN; }).map(function (k) { return { k: k, p: s.ty[k].c / s.ty[k].a, a: s.ty[k].a }; })
      .sort(function (a, b) { return a.p - b.p; });
    s.weak = ranked.filter(function (x) { return x.p < 0.85; }).slice(0, 3);
    var tops = Object.keys(s.nTy).sort(function (a, b) { return s.nTy[b] - s.nTy[a]; }).slice(0, 2);
    s.nTop = tops.map(function (k) { return k + ' ' + s.nTy[k]; }).join(', ');
    return s;
  }).sort(function (a, b) { return a.name < b.name ? -1 : a.name > b.name ? 1 : 0; });

  var sh = ss.getSheetByName(ANA) || ss.insertSheet(ANA, 1);
  sh.clear(); sh.clearConditionalFormatRules();
  var stamp = Utilities.formatDate(new Date(), tz, 'M/d HH:mm');
  sh.getRange(1, 1).setValue('학생별 분석 · ' + stamp + ' 기준').setFontWeight('bold').setFontSize(13);
  sh.getRange(2, 1).setValue('정답률은 처음 배우는 단계(단계 완료) 기준. 약한 유형은 6문제 이상 푼 유형 중 정답률 85% 미만, 낮은 순. 남은 오답 = 오답노트에서 아직 못 맞힌 문제. 오답 학습 = 앱의 오답 노트에서 다시 푼 기록(중간에 그만둔 것도 푼 만큼). Wrap-up은 종이 시험지에 오답을 정리하므로 오답 수에서 뺌.').setFontColor('#666666');
  var H1 = ['학생', '교재', '마지막 학습', '공부한 날', '학습 시간(분)', '끝낸 DAY', '푼 문제', '정답률', '약한 유형 1', '약한 유형 2', '약한 유형 3', '남은 오답', '남은 오답 많은 유형', '오늘 오답 학습', '최근 7일 오답 학습한 날', '마지막 오답 학습', '오답 학습 안 한 DAY', 'Wrap-up 점수'];
  var rows = list.map(function (s) {
    var w = function (i) { var x = s.weak[i]; return x ? x.k + ' ' + Math.round(x.p * 100) + '% (' + x.a + '문제)' : ''; };
    return [s.name, Object.keys(s.books).map(function (b) { return b.split('(')[0].trim(); }).filter(function (b, i, a) { return a.indexOf(b) === i; }).join(', '),
      s.last ? new Date(s.last) : '', Object.keys(s.days).length, s.mins, s.fin, s.solved, s.solved ? s.right / s.solved : '',
      w(0), w(1), w(2), s.nLeft, s.nTop, s.noteT ? s.noteT + '문제 · ' + s.noteC + '개 맞힘' : (s.nLeft ? '안 함' : ''), s.note7 + '일 / 7일', s.noteLast ? new Date(s.noteLast) : '',
      s.revLeft, s.wrap.join(' / ')];
  });
  var r0 = 4;
  sh.getRange(r0, 1, 1, H1.length).setValues([H1]).setFontWeight('bold').setBackground('#1f3a5f').setFontColor('#ffffff');
  if (rows.length) {
    sh.getRange(r0 + 1, 1, rows.length, H1.length).setValues(rows);
    sh.getRange(r0 + 1, 3, rows.length, 1).setNumberFormat('m/d hh:mm');
    sh.getRange(r0 + 1, 8, rows.length, 1).setNumberFormat('0%');
    sh.getRange(r0 + 1, 9, rows.length, 1).setFontColor('#b3261e').setFontWeight('bold');
    sh.getRange(r0 + 1, 16, rows.length, 1).setNumberFormat('m/d hh:mm');
    rows.forEach(function (row, i) { /* 오늘 오답 학습: 했으면 초록, 안 했으면 빨강 */
      if (row[13] === '안 함') sh.getRange(r0 + 1 + i, 14).setBackground('#fce8e6').setFontColor('#b3261e').setFontWeight('bold');
      else if (row[13]) sh.getRange(r0 + 1 + i, 14).setBackground('#e6f4ea').setFontColor('#137333');
    });
  }
  // 학생 × 유형 정답률 표 (색: 빨강 낮음 → 초록 높음)
  var r1 = r0 + rows.length + 3;
  sh.getRange(r1 - 1, 1).setValue('유형별 정답률 (빈칸 = 아직 안 풂 · 괄호 = 푼 문제 수)').setFontWeight('bold');
  var used = TYPE_NAMES.concat(['기타']).filter(function (k) { return list.some(function (s) { return s.ty[k]; }); });
  var H2 = ['학생'].concat(used);
  sh.getRange(r1, 1, 1, H2.length).setValues([H2]).setFontWeight('bold').setBackground('#1f3a5f').setFontColor('#ffffff');
  if (list.length && used.length) {
    var pv = list.map(function (s) { return [s.name].concat(used.map(function (k) { return s.ty[k] ? s.ty[k].c / s.ty[k].a : ''; })); });
    var nv = list.map(function (s) { return used.map(function (k) { return s.ty[k] ? s.ty[k].a + '문제' : ''; }); });
    var rg = sh.getRange(r1 + 1, 1, pv.length, H2.length); rg.setValues(pv);
    var body = sh.getRange(r1 + 1, 2, pv.length, used.length); body.setNumberFormat('0%').setNotes(nv).setHorizontalAlignment('center');
    sh.setConditionalFormatRules([SpreadsheetApp.newConditionalFormatRule().setGradientMinpointWithValue('#f4c7c3', SpreadsheetApp.InterpolationType.NUMBER, '0.5')
      .setGradientMidpointWithValue('#fff2cc', SpreadsheetApp.InterpolationType.NUMBER, '0.75').setGradientMaxpointWithValue('#b7e1cd', SpreadsheetApp.InterpolationType.NUMBER, '1').setRanges([body]).build()]);
  }
  sh.setFrozenRows(r0); sh.setFrozenColumns(1);
  sh.autoResizeColumns(1, Math.max(H1.length, H2.length));
  return list.length;
}

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
    if (/실전 \d+문제/.test(String(v[6]))) { var ek = String(v[2]) + '|' + String(v[4]); if (!s.ex[ek] || s.ex[ek].t > v[0].getTime()) s.ex[ek] = { book: String(v[2]), day: String(v[4]), c: +m2[1], a: +m2[2], t: v[0].getTime(), wrong: [], fixed: [] }; }
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
    if (typeOf(v[4]) === '어휘' && +v[6] > 0) {
      var q = null; try { q = JSON.parse(String(v[11])).q; } catch (e) {}
      var wd = q ? String(q.a && q.a[0] || q.key || '') : ''; if (!wd) wd = String(v[5]).slice(0, 30);
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
      wraps: s.wraps.sort(function (a, b) { return a.t - b.t; }), nNew: s.nNew, nFix: s.nFix, nLeft: s.nLeft, memo: s.memo, goal: s.goal, exam: exam,
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

var REPORT_HTML = "<!doctype html><html><head><base target=\"_top\"><meta charset=\"utf-8\">\n<style>\n@import url(\"https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700;900&display=swap\");\n:root{--ink:#1f2a37;--sub:#6b7280;--line:#e7e2d8;--bg:#f6f2ea;--card:#fffdf9;--accent:#2f6b5a;--accent2:#e9f2ee;--warn:#c2410c;--warnbg:#fdeee4;--gold:#b7791f;--navy:#101a3a}\n*{box-sizing:border-box}body{margin:0;background:#eceae4;color:var(--ink);font:15px/1.5 \"Noto Sans KR\",\"Apple SD Gothic Neo\",sans-serif;-webkit-font-smoothing:antialiased}\nheader{background:var(--navy);color:#fff;padding:14px 16px 12px}\nheader .t{display:flex;align-items:center;gap:10px;flex-wrap:wrap}\nheader h1{margin:0;font-size:20px;font-weight:900}\nheader a.back{color:#c9d3ee;font-size:13px;text-decoration:none;margin-left:auto}\n.wk{display:flex;align-items:center;gap:8px;margin-top:10px}\n.wk a{color:#fff;text-decoration:none;background:rgba(255,255,255,.12);border-radius:10px;padding:6px 12px;font-weight:700}\n.wk b{font-size:15px;flex:1;text-align:center}.wk a{flex:none;white-space:nowrap}\n.rg{display:flex;align-items:center;gap:6px;margin-top:10px;flex-wrap:wrap}\n.rg input[type=date]{border:0;border-radius:10px;padding:6px 8px;font:inherit;font-size:14px;background:#fff;color:var(--navy);min-width:0;flex:1 1 130px;max-width:170px}\n.rg span{color:#c9d3ee}\n.rg button,.rg a{border:0;border-radius:10px;padding:7px 12px;font:inherit;font-size:13px;font-weight:800;background:#fff;color:var(--navy);text-decoration:none;cursor:pointer}\n.rg a{background:rgba(255,255,255,.12);color:#fff;font-weight:700}\n.find{margin-top:10px;width:100%;border:0;border-radius:10px;padding:8px 12px;font:inherit;font-size:14px;background:rgba(255,255,255,.95);color:var(--navy)}\n.cal{display:grid;grid-template-columns:repeat(7,1fr);gap:4px;margin-top:10px}\n.cal .h{text-align:center;font-size:11.5px;color:var(--sub);font-weight:700}\n.cal .c{text-align:center;border-radius:8px;padding:5px 0;font-size:12px;color:var(--sub);background:#f1ede5;line-height:1.25}\n.d.fu,.cal .c.fu{background:transparent;border:1.5px dashed #e3ddd2;color:#c4bdb0}\n.cal .c.on{background:var(--accent);color:#fff;font-weight:800}.cal .c.x{background:transparent}\n.cal .c i{display:block;font-style:normal;font-size:10px;opacity:.85}\n.ppl{display:flex;gap:6px;overflow-x:auto;margin-top:10px;padding-bottom:2px;scrollbar-width:none}\n.ppl button{flex:none;border:0;border-radius:99px;padding:6px 12px;font:inherit;font-size:13px;font-weight:700;background:rgba(255,255,255,.1);color:#c9d3ee}\n.ppl button.on{background:#fff;color:var(--navy)}.ppl button.off{opacity:.55}\nmain{max-width:760px;margin:0 auto;padding:14px 12px 60px}\n.tools{background:#fff;border-radius:16px;padding:14px;margin-bottom:12px;box-shadow:0 1px 2px rgba(0,0,0,.05)}\n.tools label{display:block;font-size:12.5px;font-weight:700;color:var(--sub);margin:8px 0 4px}\n.tools textarea,.tools input{width:100%;border:1px solid var(--line);border-radius:10px;padding:9px 11px;font:inherit;font-size:14px;background:#fcfbf8}\n.tools textarea{min-height:76px;resize:vertical}\n.btns{display:flex;gap:8px;flex-wrap:wrap;margin-top:10px}\n.btns button{border:0;border-radius:12px;padding:10px 14px;font:inherit;font-size:14px;font-weight:800;background:var(--accent);color:#fff}\n.btns button.l{background:#efece6;color:var(--ink)}\n.msg{font-size:12.5px;color:var(--sub);margin-top:6px;min-height:18px}\n/* 리포트 카드 (이미지로 저장되는 부분) */\n.rc{background:var(--bg);padding:20px;border-radius:18px}\n.card{background:var(--card);border-radius:20px;padding:26px 26px 22px;box-shadow:0 2px 0 var(--line)}\n.top{display:flex;justify-content:space-between;align-items:flex-end;gap:10px;border-bottom:2px solid var(--ink);padding-bottom:14px}\n.brand{font-size:13px;letter-spacing:.08em;color:var(--accent);font-weight:700}\n.top h2{font-size:26px;font-weight:900;margin:2px 0 0;letter-spacing:-.02em}\n.who{text-align:right}.who b{font-size:22px;font-weight:900}.who span{display:block;color:var(--sub);font-size:13px;margin-top:2px;white-space:nowrap}\n.sec{margin-top:20px}.sec h3{font-size:14px;font-weight:800;color:var(--sub);letter-spacing:.04em;margin:0 0 9px}\n.big{display:flex;gap:10px}.stat{flex:1;background:var(--accent2);border-radius:14px;padding:12px 14px;min-width:0}\n.stat .n{font-size:26px;font-weight:900;color:var(--accent);line-height:1.15;white-space:nowrap}.stat .n small{font-size:14px;font-weight:700;color:var(--ink)}\n.stat .l{font-size:12.5px;color:var(--sub);margin-top:3px}\n.week{display:flex;gap:6px;margin-top:10px}.d{flex:1;text-align:center;border-radius:10px;padding:7px 0 6px;font-size:12.5px;color:var(--sub);background:#f1ede5}\n.d i{display:block;font-style:normal;font-size:15px;margin-top:1px;font-weight:800}.d.on{background:var(--accent);color:#fff}\ntable{width:100%;border-collapse:collapse;font-size:14.5px}td{padding:8px 0;border-bottom:1px solid var(--line);vertical-align:middle}\ntd.r{text-align:right;font-weight:800;white-space:nowrap;padding-left:10px}td .s{display:block;font-size:12.5px;color:var(--sub);font-weight:400;margin-top:1px}\n.bars .row{display:flex;align-items:center;gap:10px;margin:8px 0}.bars .k{width:150px;font-size:14px;white-space:nowrap}\n.bars .tr{flex:1;height:13px;background:#efeae1;border-radius:7px;overflow:hidden}.bars .f{height:100%;background:var(--accent);border-radius:7px}.bars .f.w{background:var(--warn)}\n.bars .v{width:46px;text-align:right;font-weight:800;font-size:14.5px}\n.tag{display:inline-block;font-size:11.5px;font-weight:800;color:var(--warn);background:var(--warnbg);border-radius:6px;padding:1px 6px;margin-left:5px}\n.note3{display:flex;gap:9px}.note3 div{flex:1;border:1.5px solid var(--line);border-radius:14px;padding:11px 13px}\n.note3 b{font-size:22px;font-weight:900}.note3 span{display:block;font-size:12.5px;color:var(--sub)}\n.memo{background:#fbf6e9;border-left:5px solid var(--gold);border-radius:10px;padding:14px 16px;font-size:15px;line-height:1.7;white-space:pre-wrap}\n.memo b{color:var(--gold);font-size:12.5px;display:block;margin-bottom:3px;letter-spacing:.04em}\n.line{margin-top:10px;font-size:14px;line-height:1.6}.line b{color:var(--accent)}\n.none{font-size:14px;color:var(--sub);padding:4px 0}\n.note3 b small{font-size:14px;font-weight:700;margin-left:1px}.vw{font-family:inherit;color:var(--ink)}\n.hint{font-size:12.5px;color:var(--sub);margin-top:6px}\n.ex .ok{color:var(--accent)}.ex .ng{color:var(--warn)}.ex .dn{font-weight:800}\n.foot{margin-top:18px;font-size:11.5px;color:var(--sub);text-align:center}\n/* 이미지 보기 */\n#ov{position:fixed;inset:0;background:rgba(15,20,30,.86);z-index:20;display:none;overflow:auto;padding:16px}\n#ov .in{max-width:520px;margin:0 auto;color:#fff;text-align:center}\n#ov img{width:100%;border-radius:12px;margin:10px 0 4px;display:block}\n#ov a,#ov button{display:inline-block;margin:4px;border:0;border-radius:12px;padding:10px 16px;font:inherit;font-weight:800;background:#fff;color:var(--navy);text-decoration:none}\n#ov p{font-size:13px;color:#d6dbe8;margin:4px 0 14px}\n#shot{position:fixed;left:-10000px;top:0;width:760px}\n@media(max-width:560px){.card{padding:20px 16px 18px}.rc{padding:10px}.top h2{font-size:22px}.stat .n{font-size:21px}.bars .k{width:120px;font-size:13px}.who b{font-size:19px}}\n</style></head><body>\n<header><div class=\"t\"><h1>주간 리포트</h1><a class=\"back\" id=\"back\">← 학생 현황판</a></div>\n<div class=\"wk\"><a id=\"prev\" target=\"_top\">‹ 지난주</a><b id=\"wkl\"></b><a id=\"next\" target=\"_top\">다음 주 ›</a></div>\n<form class=\"rg\" id=\"rg\" method=\"get\" target=\"_top\"><input type=\"hidden\" name=\"view\" id=\"fv\"><input type=\"hidden\" name=\"report\" value=\"1\"><input type=\"hidden\" name=\"who\" id=\"fw\">\n <input type=\"date\" name=\"from\" id=\"from\" aria-label=\"시작 날짜\"><span>~</span><input type=\"date\" name=\"to\" id=\"to\" aria-label=\"끝 날짜\"><button type=\"submit\">기간으로 보기</button><a id=\"thisw\" target=\"_top\">이번 주</a></form>\n<input class=\"find\" id=\"find\" type=\"search\" placeholder=\"학생 이름 검색\" autocomplete=\"off\">\n<div class=\"ppl\" id=\"ppl\"></div></header>\n<main>\n<div class=\"tools\">\n <label>선생님 한마디 (리포트에 그대로 들어가요)</label><textarea id=\"memo\" placeholder=\"예) 이번 주는 지문 반복을 꾸준히 했어요. 다음 주는 어법 오답을 집중해서 볼게요.\"></textarea>\n <label id=\"goall\">다음 주 목표 (쉼표로 나누면 하나씩 강조돼요)</label><input id=\"goal\" placeholder=\"예) DAY 10~13 완료, 남은 오답 0개, 어법 80% 이상\">\n <div class=\"btns\"><button id=\"save\">한마디 저장</button><button id=\"img\">이미지로 저장</button><button class=\"l\" id=\"all\"></button></div>\n <div class=\"msg\" id=\"msg\"></div>\n</div>\n<div id=\"view\"></div>\n</main>\n<div id=\"shot\"></div>\n<div id=\"ov\"><div class=\"in\" id=\"ovin\"></div></div>\n<script src=\"https://cdn.jsdelivr.net/npm/html-to-image@1.11.13/dist/html-to-image.js\"></script>\n<script>\nvar D=<?!= data ?>,URL=<?!= url ?>,VIEW=<?!= view ?>,WHO=<?!= who ?>;\nfunction E(s){return String(s==null?\"\":s).replace(/[&<>\"]/g,function(c){return{\"&\":\"&amp;\",\"<\":\"&lt;\",\">\":\"&gt;\",\"\\\"\":\"&quot;\"}[c]})}\nfunction ymd(d){return d.getUTCFullYear()+\"-\"+(\"0\"+(d.getUTCMonth()+1)).slice(-2)+\"-\"+(\"0\"+d.getUTCDate()).slice(-2)}\nvar CUS=!!D.custom,F0=new Date(D.from+\"T00:00:00Z\"),T0=new Date(D.to+\"T00:00:00Z\"),DAYS=[];for(var t=F0.getTime();t<=T0.getTime();t+=864e5)DAYS.push(ymd(new Date(t)));\nvar TODAY=ymd(new Date((D.made||Date.now())+9*36e5)),N=DAYS.length,NP=DAYS.filter(function(d){return d<=TODAY}).length,PER=CUS?\"이 기간\":\"이번 주\",YO=\"일월화수목금토\";\nfunction md(s){var p=s.split(\"-\");return(+p[1])+\"/\"+(+p[2])}\nfunction dw(s){return YO[new Date(s+\"T00:00:00Z\").getUTCDay()]}\nvar WKL=(CUS&&DAYS[0].slice(0,4)!==DAYS[N-1].slice(0,4)?DAYS[0].slice(2,4)+\". \":\"\")+md(DAYS[0])+\"(\"+dw(DAYS[0])+\") ~ \"+(CUS&&DAYS[0].slice(0,4)!==DAYS[N-1].slice(0,4)?DAYS[N-1].slice(2,4)+\". \":\"\")+md(DAYS[N-1])+\"(\"+dw(DAYS[N-1])+\")\"+(CUS?\" · \"+N+\"일\":\"\");\nfunction link(extra){return URL+\"?view=\"+encodeURIComponent(VIEW)+extra}\nfunction whoQ(){var s=D.list[cur];return s?\"&who=\"+encodeURIComponent(s.name):\"\"}\nfunction navs(){var sh=function(d){return ymd(new Date(F0.getTime()+d*864e5))},sh2=function(d){return ymd(new Date(T0.getTime()+d*864e5))};\n var p=document.getElementById(\"prev\"),n=document.getElementById(\"next\");\n if(CUS){p.textContent=\"‹ 이전\";n.textContent=\"다음 ›\";p.title=\"이전 \"+N+\"일\";n.title=\"다음 \"+N+\"일\";p.href=link(\"&report=1&from=\"+sh(-N)+\"&to=\"+sh2(-N)+whoQ());n.href=link(\"&report=1&from=\"+sh(N)+\"&to=\"+sh2(N)+whoQ())}\n else{p.href=link(\"&report=1&wk=\"+sh(-7)+whoQ());n.href=link(\"&report=1&wk=\"+sh(7)+whoQ())}\n document.getElementById(\"thisw\").href=link(\"&report=1\"+whoQ());var s=D.list[cur];document.getElementById(\"fw\").value=s?s.name:\"\"}\ndocument.getElementById(\"back\").href=link(\"\");\ndocument.getElementById(\"wkl\").textContent=WKL;\ndocument.getElementById(\"fv\").value=VIEW;document.getElementById(\"rg\").action=URL;\ndocument.getElementById(\"from\").value=D.from;document.getElementById(\"to\").value=D.to;\ndocument.getElementById(\"rg\").onsubmit=function(e){var a=document.getElementById(\"from\").value,b=document.getElementById(\"to\").value,m=document.getElementById(\"msg\");\n if(!a||!b){e.preventDefault();m.textContent=\"시작 날짜와 끝 날짜를 모두 골라 주세요.\";return}\n var A=new Date(a+\"T00:00:00Z\"),B=new Date(b+\"T00:00:00Z\");if(A>B){var x=a;a=b;b=x;document.getElementById(\"from\").value=a;document.getElementById(\"to\").value=b;A=new Date(a+\"T00:00:00Z\");B=new Date(b+\"T00:00:00Z\")}\n if((B-A)/864e5+1>186){e.preventDefault();m.textContent=\"기간은 최대 186일(약 6개월)까지 볼 수 있어요.\";return}};\ndocument.getElementById(\"goall\").textContent=(CUS?\"다음 목표\":\"다음 주 목표\")+\" (쉼표로 나누면 하나씩 강조돼요)\";\ndocument.getElementById(\"all\").textContent=PER+\" 학습한 학생 전부 이미지로\";\nvar cur=0;D.list.forEach(function(s,i){if(s.name===WHO)cur=i});\nfunction hm(m){return m>=60?Math.floor(m/60)+\"<small>시간</small> \"+(m%60)+\"<small>분</small>\":m+\"<small>분</small>\"}\nfunction pct(c,a){return a?Math.round(c/a*100):0}\nfunction dayList(arr){var n=arr.map(function(x){var m=/(\\d+)/.exec(x.day);return m?+m[1]:null});\n if(n.every(function(x){return x!=null})){n=n.slice().sort(function(a,b){return a-b});var out=[],s=n[0],p=n[0];for(var i=1;i<=n.length;i++){if(n[i]===p+1){p=n[i];continue}out.push(s===p?\"DAY \"+s:\"DAY \"+s+\"~\"+p);s=p=n[i]}return out.join(\", \")}\n return arr.map(function(x){return x.day}).join(\", \")}\nfunction bookName(b,u){return E(b.replace(/\\s*\\(.*\\)\\s*$/,\"\")||b)+(/\\(/.test(b)?\" <span style=\\\"color:var(--sub);font-weight:400;font-size:13px\\\">\"+E((/\\(([^)]*)\\)/.exec(b)||[\"\",\"\"])[1])+\"</span>\":\"\")}\nfunction cal(s){var pad=(new Date(DAYS[0]+\"T00:00:00Z\").getUTCDay()+6)%7,h=\"<div class=cal>\"+\"월화수목금토일\".split(\"\").map(function(x){return\"<div class=h>\"+x+\"</div>\"}).join(\"\");\n for(var i=0;i<pad;i++)h+=\"<div class=\\\"c x\\\"></div>\";\n DAYS.forEach(function(d,i){var on=s.days.indexOf(d)>=0,dd=+d.slice(8);h+=\"<div class=\\\"c\"+(on?\" on\":\"\")+(d>TODAY?\" fu\":\"\")+\"\\\">\"+(i===0||dd===1?md(d):dd)+\"<i>\"+(on?\"✓\":\"&nbsp;\")+\"</i></div>\"});\n return h+\"</div>\"}\nfunction card(s){\n var st=s.days.length,total=s.solved+s.noteN,h=\"\";\n h+=\"<div class=card><div class=top><div><div class=brand>혜연쌤 DAILY ENGLISH</div><h2>\"+(CUS?\"학습 리포트\":\"주간 학습 리포트\")+\"</h2></div><div class=who><b>\"+E(s.name)+\"</b><span>\"+E(s.grades.join(\" · \"))+(s.grades.length?\" · \":\"\")+WKL+\"</span></div></div>\";\n h+=\"<div class=sec><h3>\"+PER+\" 꾸준함</h3><div class=big><div class=stat><div class=n>\"+st+\"<small>일 / \"+NP+\"일</small></div><div class=l>공부한 날\"+(NP<N?\" (오늘까지)\":\"\")+\"</div></div><div class=stat><div class=n>\"+hm(s.mins)+\"</div><div class=l>학습 시간</div></div><div class=stat><div class=n>\"+total+\"<small>문항</small></div><div class=l>푼 문제</div></div></div>\";\n h+=(CUS?cal(s):\"<div class=week>\"+DAYS.map(function(d,i){var on=s.days.indexOf(d)>=0,fu=d>TODAY;return\"<div class=\\\"d\"+(on?\" on\":\"\")+(fu?\" fu\":\"\")+\"\\\">\"+\"월화수목금토일\"[i]+\"<i>\"+(on?\"✓\":fu?\"&nbsp;\":\"–\")+\"</i></div>\"}).join(\"\")+\"</div>\")+\"</div>\";\n var rows=\"\";s.prog.forEach(function(p){\n  if(p.done.length){var sc=p.done.filter(function(x){return x.score!=null}),av=sc.length?Math.round(sc.reduce(function(a,x){return a+x.score},0)/sc.length):null,rv=p.done.filter(function(x){return x.rev}).length;\n   rows+=\"<tr><td>\"+bookName(p.book)+\"<span class=s>\"+E(dayList(p.done))+\" 완료\"+(rv?\" · 오답 학습 남음 \"+rv+\"개\":\"\")+\"</span></td><td class=r>\"+(av!=null?(sc.length>1?\"평균 \":\"\")+av+\"점\":\"완료\")+\"</td></tr>\"}\n  p.doing.forEach(function(x){rows+=\"<tr><td>\"+bookName(p.book)+\"<span class=s>\"+E(x.day)+\" 진행 중\"+(/\\d+\\/\\d+/.test(x.prog)?\" (\"+E(x.prog)+\")\":\"\")+\"</span></td><td class=r>진행 중</td></tr>\"})});\n s.wraps.forEach(function(w){rows+=\"<tr><td>Wrap-up 시험<span class=s>\"+E(w.name)+\"</span></td><td class=r>\"+(w.score!=null?w.score+\"점\":\"제출\")+\"</td></tr>\"});\n h+=\"<div class=sec><h3>진도</h3>\"+(rows?\"<table>\"+rows+\"</table>\":\"<div class=none>\"+PER+\"에 끝낸 DAY는 없어요.</div>\")+\"</div>\";\n if(s.exam&&s.exam.length){var ec=0,ea=0,er=\"\";s.exam.forEach(function(e){ec+=e.c;ea+=e.a;var m=/^(DAY\\s*\\d+)\\s*(.*)$/.exec(e.day)||[\"\",e.day,\"\"],all=e.c===e.a,w=all?[]:e.wrong,fx=w.filter(function(n){return e.fixed.indexOf(n)>=0});\n  var res=e.a===1?(all?\"<span class=ok>○ 맞힘</span>\":\"<span class=ng>✕ 틀림</span>\"):(all?\"<span class=ok>○ \"+e.c+\"/\"+e.a+\"</span>\":\"<span class=ng>\"+e.c+\"/\"+e.a+\"</span>\");\n  var sub=!all&&e.a>1&&w.length?w.map(function(n){return n+\"번\"}).join(\"·\")+\" 틀림\":\"\"; /* 풀면 바로 정답이 나오므로 '다시 맞힘'은 넣지 않음 (처음 푼 결과만) */\n  er+=\"<tr><td><b class=dn>\"+E(m[1])+\"</b> \"+E(m[2])+(sub?\"<span class=s>\"+E(sub)+\"</span>\":\"\")+\"</td><td class=r>\"+res+\"</td></tr>\"});\n  h+=\"<div class=sec><h3>실전 문제 (하루 한 문제) · \"+ea+\"문제 중 \"+ec+\"개 맞힘</h3><table class=ex>\"+er+\"</table></div>\"}\n var V=s.voc;if(V&&(V.a||V.wrong.length||V.re)){var VW=V.wrong.slice(0,14);\n  h+=\"<div class=sec><h3>어휘</h3><div class=note3><div><b>\"+V.a+\"<small>개</small></b><span>학습한 어휘\"+(V.a?\" · 정답률 \"+pct(V.c,V.a)+\"%\":\"\")+\"</span></div><div><b style=\\\"color:\"+(V.wrong.length?\"var(--warn)\":\"var(--accent)\")+\"\\\">\"+V.wrong.length+\"<small>개</small></b><span>\"+PER+\" 틀린 어휘</span></div><div><b style=\\\"color:var(--accent)\\\">\"+V.re+\"<small>개</small></b><span>다시 공부한 어휘\"+(V.re?\" · \"+V.done+\"개 완전히 익힘\":\"\")+\"</span></div></div>\";\n  h+=(VW.length?\"<div class=line>틀린 어휘 · <span class=vw>\"+VW.map(E).join(\", \")+(V.wrong.length>VW.length?\" 외 \"+(V.wrong.length-VW.length)+\"개\":\"\")+\"</span></div>\":\"\")+(V.left?\"<div class=hint>오답 노트에 아직 남은 어휘 \"+V.left+\"개 · 서로 다른 날 두 번 맞히면 '완전히 익힘'이 돼요.</div>\":\"\")+\"</div>\"}\n var wl=function(t){return /실전/.test(t.k)&&s.exam&&s.exam.length?\"약한 유형\":\"보충 필요\"}; /* 하루 한 문제 실전은 다시 풀 문제가 없으므로 사실만 */\n if(s.types.length){var TT=s.types.slice();if(TT.length>6){var wk=TT.filter(function(t){return pct(t.c,t.a)<70}).slice(-3),ok=TT.filter(function(t){return wk.indexOf(t)<0}).slice(0,6-wk.length);TT=ok.concat(wk)} /* 6개가 넘으면 약한 유형(70% 미만)은 꼭 보이게 */\n h+=\"<div class=sec><h3>유형별 정답률</h3><div class=bars>\"+TT.map(function(t){var p=pct(t.c,t.a),w=p<70;return\"<div class=row><div class=k>\"+E(t.k.replace(\"대의(주제·요지·제목)\",\"주제·요지·제목\"))+(w?\"<span class=tag>\"+wl(t)+\"</span>\":\"\")+\"</div><div class=tr><div class=\\\"f\"+(w?\" w\":\"\")+\"\\\" style=\\\"width:\"+p+\"%\\\"></div></div><div class=v\"+(w?\" style=\\\"color:var(--warn)\\\"\":\"\")+\">\"+p+\"%</div></div>\"}).join(\"\")+\"</div>\"+(function(){var L={};TT.forEach(function(t){if(pct(t.c,t.a)<70)L[wl(t)]=1});var k=Object.keys(L);return k.length?\"<div class=hint>정답률 70% 미만인 유형은 \"+k.map(function(x){return\"'\"+x+\"'\"}).join(\"·\")+((k[k.length-1].charCodeAt(k[k.length-1].length-1)-44032)%28?\"으로\":\"로\")+\" 표시했어요.\"+(L[\"보충 필요\"]?\" 다음 학습에서 이 유형을 더 연습해요.\":\"\")+\"</div>\":\"\"})()+\"</div>\"}\n h+=\"<div class=sec><h3>오답 관리</h3><div class=note3><div><b>\"+s.nNew+\"</b><span>\"+PER+\" 새 오답</span></div><div><b style=\\\"color:var(--accent)\\\">\"+s.nFix+\"</b><span>다시 풀어 맞힘</span></div><div><b style=\\\"color:\"+(s.nLeft?\"var(--warn)\":\"var(--accent)\")+\"\\\">\"+s.nLeft+\"</b><span>아직 남은 오답</span></div></div>\";\n h+=\"<div class=line>\"+(st?\"오답 복습(오늘의 오답)을 <b>\"+st+\"일 중 \"+Math.min(s.noteDays,st)+\"일</b> 했어요\"+(s.noteN?\" · \"+s.noteN+\"문제 중 \"+s.noteC+\"개 맞힘\":\"\")+\".\":PER+\"에는 학습 기록이 없어요.\")+\"</div></div>\";\n if(s.memo||s.goal){h+=\"<div class=sec><h3>선생님 한마디</h3>\"+(s.memo?\"<div class=memo><b>FROM 혜연쌤</b>\"+E(s.memo)+\"</div>\":\"\")+(s.goal?\"<div class=line>\"+(CUS?\"다음 목표\":\"다음 주 목표\")+\" · \"+s.goal.split(/\\s*[,，]\\s*/).filter(String).map(function(g){return\"<b>\"+E(g)+\"</b>\"}).join(\" · \")+\"</div>\":\"\")+\"</div>\"}\n h+=\"<div class=foot>이 리포트는 데일리 학습 기록으로 자동 작성됐어요.</div></div>\";\n return\"<div class=rc>\"+h+\"</div>\"}\nfunction hits(){var q=document.getElementById(\"find\").value.replace(/\\s+/g,\"\");return D.list.map(function(s,i){return i}).filter(function(i){return !q||D.list[i].name.replace(/\\s+/g,\"\").indexOf(q)>=0})}\nfunction ppl(){var H=hits();document.getElementById(\"ppl\").innerHTML=H.length?H.map(function(i){var s=D.list[i];return\"<button data-i=\"+i+\" class=\\\"\"+(i===cur?\"on\":\"\")+(s.days.length?\"\":\" off\")+\"\\\">\"+E(s.name)+(s.days.length?\" \"+s.days.length+\"일\":\"\")+\"</button>\"}).join(\"\"):\"<span style=\\\"color:#c9d3ee;font-size:13px;padding:6px 2px\\\">찾는 학생이 없어요.</span>\";\n [].forEach.call(document.querySelectorAll(\"[data-i]\"),function(b){b.onclick=function(){cur=+b.dataset.i;show()}})}\nfunction show(){ppl();navs();var s=D.list[cur];if(!s){document.getElementById(\"view\").innerHTML=\"<p class=none>기록이 있는 학생이 없어요.</p>\";return}\n document.getElementById(\"memo\").value=s.memo||\"\";document.getElementById(\"goal\").value=s.goal||\"\";document.getElementById(\"msg\").textContent=\"\";\n document.getElementById(\"view\").innerHTML=card(s)}\nfunction live(){var s=D.list[cur];if(!s)return;s.memo=document.getElementById(\"memo\").value;s.goal=document.getElementById(\"goal\").value;document.getElementById(\"view\").innerHTML=card(s);document.getElementById(\"msg\").textContent=\"저장 전이에요. [한마디 저장]을 누르면 시트에 남아요.\"}\ndocument.getElementById(\"find\").oninput=function(){var H=hits();if(H.length===1&&H[0]!==cur){cur=H[0];show()}else ppl()};\ndocument.getElementById(\"find\").onkeydown=function(e){if(e.key===\"Enter\"){e.preventDefault();var H=hits();if(H.length){cur=H[0];show()}}};\ndocument.getElementById(\"memo\").oninput=live;document.getElementById(\"goal\").oninput=live;\ndocument.getElementById(\"save\").onclick=function(){var s=D.list[cur];if(!s)return;var m=document.getElementById(\"msg\");m.textContent=\"저장 중…\";\n google.script.run.withSuccessHandler(function(){m.textContent=\"저장했어요 ('주간리포트' 탭).\"}).withFailureHandler(function(e){m.textContent=\"저장하지 못했어요: \"+(e&&e.message||e)}).saveMemo(D.wk,s.name,s.memo||\"\",s.goal||\"\")};\nfunction shot(s){var box=document.getElementById(\"shot\");box.innerHTML=card(s);var el=box.firstChild;\n var o={pixelRatio:2,backgroundColor:\"#f6f2ea\",cacheBust:true};\n var go=function(opt){return htmlToImage.toPng(el,opt).then(function(){return htmlToImage.toPng(el,opt)})}; /* 사파리는 첫 장이 비는 일이 있어 두 번 그림 */\n return(document.fonts&&document.fonts.ready?document.fonts.ready:Promise.resolve()).then(function(){return go(o)}).catch(function(){return go(Object.assign({},o,{skipFonts:true}))}).then(function(u){return{name:s.name,url:u}})}\nfunction fname(n){return CUS?n+\"_학습리포트_\"+DAYS[0].slice(5).replace(\"-\",\"\")+\"-\"+DAYS[N-1].slice(5).replace(\"-\",\"\")+\".png\":n+\"_주간리포트_\"+DAYS[0].slice(5).replace(\"-\",\"\")+\".png\"}\nfunction overlay(items){var o=document.getElementById(\"ov\"),h=\"<button id=ovx>닫기</button><p>휴대폰: 이미지를 길게 눌러 저장하거나 공유하세요. 컴퓨터: [저장] 또는 오른쪽 클릭 → 이미지 저장.</p>\";\n h+=items.map(function(x){return\"<div><img src=\\\"\"+x.url+\"\\\" alt=\\\"\"+E(x.name)+\"\\\"><a download=\\\"\"+E(fname(x.name))+\"\\\" href=\\\"\"+x.url+\"\\\">\"+E(x.name)+\" 저장</a></div>\"}).join(\"<hr style=\\\"border:0;border-top:1px solid rgba(255,255,255,.2);margin:16px 0\\\">\");\n document.getElementById(\"ovin\").innerHTML=h;o.style.display=\"block\";o.scrollTop=0;document.getElementById(\"ovx\").onclick=function(){o.style.display=\"none\"}}\ndocument.getElementById(\"img\").onclick=function(){var s=D.list[cur];if(!s)return;var m=document.getElementById(\"msg\");m.textContent=\"이미지 만드는 중…\";\n shot(s).then(function(x){m.textContent=\"\";overlay([x])}).catch(function(e){m.textContent=\"이미지를 만들지 못했어요: \"+e})};\ndocument.getElementById(\"all\").onclick=function(){var L=D.list.filter(function(s){return s.days.length}),m=document.getElementById(\"msg\"),out=[],i=0;if(!L.length){m.textContent=PER+\"에 학습한 학생이 없어요.\";return}\n (function next(){if(i>=L.length){m.textContent=\"\";overlay(out);return}m.textContent=\"이미지 만드는 중… \"+(i+1)+\" / \"+L.length;shot(L[i]).then(function(x){out.push(x);i++;next()}).catch(function(e){m.textContent=\"이미지를 만들지 못했어요: \"+e})})()};\nshow();\n</script></body></html>\n";
