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

var VIEW = 'dW6ypYyx'; // 현황판 열쇠: 주소 끝 ?view=dW6ypYyx 가 있어야 학생 현황판이 열려요

function doGet(e) {
  if (e && e.parameter && e.parameter.view === VIEW) {
    var t = HtmlService.createTemplate(BOARD_HTML);
    t.data = JSON.stringify(boardData());
    return t.evaluate().setTitle('학생 현황판').addMetaTag('viewport', 'width=device-width, initial-scale=1');
  }
  return ContentService.createTextOutput('데일리 영어 기록 받기: 작동 중이에요.');
}

/* 기록 탭을 학생별로 모아 현황판 카드 데이터로 만든다 */
function boardData() {
  var ss = SpreadsheetApp.getActiveSpreadsheet(), tz = 'Asia/Seoul';
  var today = Utilities.formatDate(new Date(), tz, 'yyyy-MM-dd');
  var log = ss.getSheetByName('기록'), now = ss.getSheetByName('현황'), S = {};
  function st(name) { return S[name] || (S[name] = { name: name, grades: {}, last: 0, mins: 0, minsToday: 0, solved: 0, right: 0, solvedToday: 0, days: 0, reviewLeft: 0, weakLeft: 0, rows: [], _t: [] }); }
  if (log && log.getLastRow() > 1) {
    log.getRange(2, 1, log.getLastRow() - 1, 8).getValues().forEach(function (v) {
      if (!v[1]) return;
      var s = st(String(v[1])), t = v[0] instanceof Date ? v[0].getTime() : 0;
      if (!t) return;
      s._t.push(t); if (t > s.last) s.last = t;
      var g = String(v[2]).split(' ')[0]; if (g) s.grades[g] = 1;
      var m = /^(\d+)\/(\d+)$/.exec(String(v[7]));
      if (m) { s.solved += +m[2]; s.right += +m[1]; if (Utilities.formatDate(v[0], tz, 'yyyy-MM-dd') === today) s.solvedToday += +m[2]; }
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
  var list = Object.keys(S).map(function (k) { var s = S[k]; s.grades = Object.keys(s.grades); s.rows.sort(function (a, b) { return b.last - a.last; }); return s; });
  list.sort(function (a, b) { return b.last - a.last; });
  return { today: today, made: Date.now(), list: list };
}

var BOARD_HTML = '<!doctype html><html><head><base target="_top"><meta charset="utf-8">' +
'<style>' +
':root{--bg:#f4f6fb;--card:#fff;--ink:#1b2333;--muted:#6b7487;--line:#e3e7ef;--blue:#2f5fd0;--ok:#1d8549;--warn:#b26a00;--bad:#cc3434}' +
'*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.45 -apple-system,"Apple SD Gothic Neo","Noto Sans KR",sans-serif}' +
'header{position:sticky;top:0;z-index:2;background:var(--blue);color:#fff;padding:14px 16px 10px}h1{margin:0;font-size:19px}' +
'.sub{font-size:12px;opacity:.85;margin-top:2px}.bar{display:flex;gap:6px;overflow-x:auto;margin-top:10px;padding-bottom:2px}' +
'.bar button{flex:none;border:0;border-radius:99px;padding:6px 12px;font:inherit;font-size:13px;background:rgba(255,255,255,.18);color:#fff}.bar button.on{background:#fff;color:var(--blue);font-weight:700}' +
'input{width:100%;margin-top:8px;border:0;border-radius:10px;padding:9px 12px;font:inherit}' +
'main{max-width:640px;margin:0 auto;padding:12px 12px 40px}.sum{display:flex;gap:8px;margin:2px 0 12px;font-size:13px;color:var(--muted);flex-wrap:wrap}' +
'.card{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:14px;margin-bottom:10px}' +
'.top{display:flex;align-items:center;gap:12px}.av{flex:none;width:44px;height:44px;border-radius:50%;background:var(--blue);color:#fff;display:grid;place-items:center;font-weight:700}' +
'.nm{font-size:18px;font-weight:700}.gr{font-size:13px;color:var(--muted);margin-left:6px;font-weight:400}.when{margin-left:auto;font-size:12px;color:var(--muted);text-align:right}' +
'.when.today{color:var(--ok);font-weight:700}.when.old{color:var(--bad)}' +
'.grid{display:grid;grid-template-columns:1fr 1fr;gap:10px 12px;margin-top:12px}.grid small{display:block;color:var(--muted);font-size:12px}.grid b{font-size:18px}' +
'.tags{display:flex;flex-wrap:wrap;gap:6px;margin-top:10px}.tag{font-size:12px;border-radius:99px;padding:3px 9px;background:#eef1f7}.tag.w{background:#fff1d6;color:var(--warn)}.tag.b{background:#fbe5e5;color:var(--bad)}.tag.o{background:#e3f4e6;color:var(--ok)}' +
'details{margin-top:10px;border-top:1px solid var(--line);padding-top:8px}summary{cursor:pointer;color:var(--blue);font-size:13px}' +
'.row{padding:8px 0;border-bottom:1px dashed var(--line);font-size:13px}.row:last-child{border:0}.row .u{color:var(--muted)}.row .p{font-weight:700}.row .p.done{color:var(--ok)}.row .p.rev{color:var(--warn)}.row .wk{color:var(--bad);font-size:12px}' +
'.empty{text-align:center;color:var(--muted);padding:40px 0}' +
'</style></head><body><header><h1>학생 현황판</h1><div class="sub" id="made"></div><div class="bar" id="bar"></div><input id="q" placeholder="이름 찾기"></header><main><div class="sum" id="sum"></div><div id="list"></div></main>' +
'<script>var D=<?!= data ?>;' +
'var F="all",Q="";function E(s){return String(s==null?"":s).replace(/[&<>"]/g,function(c){return{"&":"&amp;","<":"&lt;",">":"&gt;","\\"":"&quot;"}[c]})}' +
'function dk(t){var d=new Date(t);return d.getFullYear()+"-"+("0"+(d.getMonth()+1)).slice(-2)+"-"+("0"+d.getDate()).slice(-2)}' +
'function ft(t){if(!t)return"기록 없음";var d=new Date(t),w="일월화수목금토"[d.getDay()];return(d.getMonth()+1)+"/"+d.getDate()+"("+w+") "+("0"+d.getHours()).slice(-2)+":"+("0"+d.getMinutes()).slice(-2)}' +
'function hm(m){return m>=60?Math.floor(m/60)+"시간 "+(m%60)+"분":m+"분"}' +
'var G={};D.list.forEach(function(s){s.grades.forEach(function(g){G[g]=1})});' +
'var B=[["all","전체"],["notoday","오늘 안 한 학생"],["todo","할 일 남은 학생"]].concat(Object.keys(G).sort().map(function(g){return["g:"+g,g]}));' +
'function bar(){document.getElementById("bar").innerHTML=B.map(function(b){return"<button data-f=\\""+b[0]+"\\" class=\\""+(F===b[0]?"on":"")+"\\">"+E(b[1])+"</button>"}).join("");' +
'[].forEach.call(document.querySelectorAll("[data-f]"),function(x){x.onclick=function(){F=x.dataset.f;bar();draw()}})}' +
'function draw(){var L=D.list.filter(function(s){if(Q&&s.name.indexOf(Q)<0)return false;if(F==="notoday")return dk(s.last)!==D.today;if(F==="todo")return s.reviewLeft||s.weakLeft;if(F.indexOf("g:")===0)return s.grades.indexOf(F.slice(2))>=0;return true});' +
'var td=D.list.filter(function(s){return dk(s.last)===D.today}).length;' +
'document.getElementById("sum").innerHTML="<span>학생 "+D.list.length+"명</span><span>· 오늘 학습 "+td+"명</span><span>· 보이는 학생 "+L.length+"명</span>";' +
'document.getElementById("list").innerHTML=L.length?L.map(function(s){var age=(Date.now()-s.last)/864e5,cls=dk(s.last)===D.today?"today":age>3?"old":"";' +
'var acc=s.solved?Math.round(s.right/s.solved*100):0;' +
'return"<div class=card><div class=top><div class=av>"+E(s.name.charAt(0))+"</div><div><span class=nm>"+E(s.name)+"</span><span class=gr>"+E(s.grades.join(" · "))+"</span></div><div class=\\"when "+cls+"\\">"+(cls==="today"?"오늘 ":"")+ft(s.last)+"</div></div>"+' +
'"<div class=grid><div><small>누적 학습시간</small><b>"+hm(s.mins)+"</b></div><div><small>오늘 학습시간</small><b>"+hm(s.minsToday)+"</b></div>"+' +
'"<div><small>누적 푼 문제</small><b>"+s.solved+"문제</b></div><div><small>정답률 · 틀린 문제</small><b>"+acc+"% · "+(s.solved-s.right)+"개</b></div></div>"+' +
'"<div class=tags><span class=\\"tag o\\">완료 DAY "+s.days+"개</span>"+(s.reviewLeft?"<span class=\\"tag w\\">오답 학습 남음 "+s.reviewLeft+"</span>":"")+(s.weakLeft?"<span class=\\"tag b\\">약한 유형 보충 안 함 "+s.weakLeft+"</span>":"")+(s.solvedToday?"<span class=tag>오늘 "+s.solvedToday+"문제</span>":"")+"</div>"+' +
'(s.rows.length?"<details><summary>단원·DAY별 보기 ("+s.rows.length+")</summary>"+s.rows.map(function(r){var pc=r.prog==="완료"?"done":r.prog==="오답 학습 남음"?"rev":"";' +
'return"<div class=row><div><span class=\\"p "+pc+"\\">"+E(r.day)+" · "+E(r.prog)+"</span> "+E(r.score)+"</div><div class=u>"+E(r.book)+" · "+E(r.unit)+" · "+E(r.range)+" · "+ft(r.last)+"</div>"+(r.weak?"<div class=wk>"+E(r.weak)+"</div>":"")+"</div>"}).join("")+"</details>":"")+"</div>"}).join(""):"<p class=empty>해당하는 학생이 없어요.</p>"}' +
'document.getElementById("made").textContent=ft(D.made)+" 기준 · 새로고침하면 최신으로 바뀌어요";' +
'document.getElementById("q").oninput=function(){Q=this.value.trim();draw()};bar();draw();</script></body></html>';

function doPost(e) {
  var data;
  try { data = JSON.parse(e.postData.contents); } catch (err) { return out('bad'); }
  if (!data || data.k !== KEY || !data.rows || !data.rows.length) return out('no');
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

/** 처음 한 번 실행: 탭 만들기 + 권한 허용 */
function setup() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  sheet(ss, '현황', NOW_HEAD); sheet(ss, '기록', LOG_HEAD);
  var first = ss.getSheetByName('시트1') || ss.getSheetByName('Sheet1');
  if (first && ss.getSheets().length > 2 && first.getLastRow() === 0) ss.deleteSheet(first);
}
