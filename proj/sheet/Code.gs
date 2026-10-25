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

function doGet() {
  return ContentService.createTextOutput('데일리 영어 기록 받기: 작동 중이에요.');
}

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
