// Apps Script 흉내: Code.gs 를 그대로 돌려 현황판 · 주간 리포트 HTML 을 만든다
const fs=require('fs');
const RealDate=Date;const NOWT=RealDate.UTC(2026,10,6,13,0);
global.Date=class extends RealDate{constructor(...a){if(!a.length)super(NOWT);else super(...a)}static now(){return NOWT}};
const K=(y,m,d,h,mi)=>new Date(Date.UTC(y,m-1,d,h-9,mi||0));
function fmt(date,tz,f){const p=Object.fromEntries(new Intl.DateTimeFormat('en-US',{timeZone:'Asia/Seoul',year:'numeric',month:'2-digit',day:'2-digit',hour:'2-digit',minute:'2-digit',hour12:false,weekday:'short'}).formatToParts(date).map(x=>[x.type,x.value]));
 const u={Mon:1,Tue:2,Wed:3,Thu:4,Fri:5,Sat:6,Sun:7}[p.weekday];
 return f.replace('yyyy',p.year).replace('MM',p.month).replace('dd',p.day).replace('HH',p.hour==='24'?'00':p.hour).replace('mm',p.minute).replace(/^u$/,String(u)).replace(/^M\//,String(+p.month)+'/').replace(/\/d /,'/'+(+p.day)+' ');}
class Sheet{constructor(name,rows){this.name=name;this.rows=rows}getLastRow(){return this.rows.length}
 getRange(r,c,nr,nc){const self=this;return{getValues(){return self.rows.slice(r-1,r-1+nr).map(x=>{const a=x.slice(c-1,c-1+nc);while(a.length<nc)a.push('');return a})},
  setValues(v){v.forEach((row,i)=>{self.rows[r-1+i]=self.rows[r-1+i]||[];row.forEach((x,j)=>self.rows[r-1+i][c-1+j]=x)});return this},setFontWeight(){return this},setBackground(){return this},setFontColor(){return this},setNumberFormat(){return this},getValue(){return (self.rows[r-1]||[])[c-1]}}}
 appendRow(r){this.rows.push(r)}setFrozenRows(){}setColumnWidth(){}}
const LOGR=[['시각','학생','학년·교재','단원','DAY','무엇','단계','단계 점수','진행','누적 점수','기기']];
const sc='고1 모의고사(2025년 9월 학평·중산고1)',un='18~24 · 26 · 29~42번 + YBM 3과 본문';
function L(t,n,day,kind,step,s){LOGR.push([t,n,sc,un,day,kind,step,s,'','',''])}
// 김민서: 월 화 목 금 + 지난주 하루
[[2,19],[3,20],[5,19],[6,18]].forEach(([d,h],k)=>{let m=0;const day='DAY '+(6+k)+' 3'+(2+k)+'번';
 [['1. 핵심어휘·숙어','14/15'],['2. 실전 문항','2/3'],['3. 어휘선택','6/6'],['4. T/F 내용 확인','7/7'],['5. 일치·불일치','2/3'],['6. 어법선택','4/7'],['7. 동사변형','3/4'],['8. 오류찾기','2/4'],['9. 본문 스크램블','4/4'],['10. 문장순서','2/2'],['13. 빈칸추론','3/3']].forEach(([st,s])=>{L(K(2026,11,d,h,m),'김민서',day,'단계 완료',st,s);m+=4});
 L(K(2026,11,d,h-1,50),'김민서',day,'오답 노트','오답 노트 오늘의 오답','9/12')});
L(K(2026,10,29,19,0),'김민서','DAY 5 30·31번','단계 완료','3. 어휘선택','5/6');
L(K(2026,11,4,20,0),'이준호','DAY 6 32번','단계 완료','2. 실전 문항','1/3');L(K(2026,11,4,20,5),'이준호','DAY 6 32번','단계 완료','6. 어법선택','5/7');
L(K(2026,10,28,20,0),'박서연','DAY 3 23·24번','단계 완료','3. 어휘선택','6/6');
const sc3='고3 수능실전반',un3='하루 한 문제 · 2026학년도 10월 학평';
[[2,'DAY 1 20번 주장','1/1'],[3,'DAY 2 22번 요지','0/1'],[4,'DAY 3 23번 주제','1/1'],[5,'DAY 4 24번 제목','0/1'],[6,'DAY 25 43~45번 장문 (순서·지칭·일치)','2/3']].forEach(([d,day,sc_])=>{
 LOGR.push([K(2026,11,d,21,0),'최하늘',sc3,un3,day,'단계 완료','1. 실전 1문제',sc_,'','','']);LOGR.push([K(2026,11,d,21,3),'최하늘',sc3,un3,day,'단계 완료','2. 단어 리스트','18/20','','',''],);LOGR.push([K(2026,11,d,21,6),'최하늘',sc3,un3,day,'DAY 완료','3. 단어 테스트','9/10','','',''])});
const NOWR=[['학생','학년·교재','단원','DAY','범위','진행','점수','오답 학습','회차','시작','마지막 활동','완료']];
function N(n,day,rng,prog,score,last,end){NOWR.push([n,sc,un,day,rng,prog,score,'',1,'',last,end||''])}
N('김민서','DAY 6','32번','완료','92점 (70/76)',K(2026,11,2,20,0),K(2026,11,2,20,0));
N('김민서','DAY 7','33번','완료','88점 (60/68)',K(2026,11,3,21,0),K(2026,11,3,21,0));
N('김민서','DAY 8','34번','오답 학습 남음','84점 (63/75)',K(2026,11,5,20,0),K(2026,11,5,20,0));
N('김민서','DAY 9','35번','8/14단계','',K(2026,11,6,19,0));
N('김민서','Wrap-up 18~22번','','완료','90점 (18/20)',K(2026,11,4,21,0),K(2026,11,4,21,0));
N('이준호','DAY 6','32번','2/14단계','',K(2026,11,4,20,5));
const NOTER=[['학생','교재','DAY','과·DAY','단계','문제','틀린 횟수','헷갈려요','상태','마지막','key','data']];
for(let i=0;i<14;i++){const first=i<9?K(2026,11,2+(i%4),20,0).getTime():K(2026,10,28,20,0).getTime();NOTER.push(['김민서',sc,'DAY 6 32번','','어법선택','q',1,'',i%3===0?'남음':'맞힘',i%3===0?K(2026,10,30,1,0):K(2026,11,5,21,0),'k'+i,JSON.stringify({id:'x',first:first})])}
NOTER.push(['최하늘',sc3,'DAY 2 22번 요지','','실전 1문제','22. 다음 글의 요지로 가장 적절한 것은? ...',1,'','맞힘',K(2026,11,5,21,0),'h1','{"first":'+K(2026,11,3,21,0).getTime()+'}']);
NOTER.push(['최하늘',sc3,'DAY 4 24번 제목','','실전 1문제','24. 다음 글의 제목으로 가장 적절한 것은? ...',1,'','남음',K(2026,11,5,21,0),'h2','{"first":'+K(2026,11,5,21,0).getTime()+'}']);
NOTER.push(['최하늘',sc3,'DAY 25 43~45번 장문 (순서·지칭·일치)','','실전 1문제','44. 밑줄 친 (a)~(e) 중에서 ...',1,'','남음',K(2026,11,6,21,0),'h3','{"first":'+K(2026,11,6,21,0).getTime()+'}']);
[['counterintuitive','맞힘',true],['prejudice','남음',true],['profound','맞힘',true],['inevitable','남음',false],['reach out','남음',false]].forEach(([w,st,re],i)=>{const f=K(2026,11,2+i%4,21,3).getTime();
 NOTER.push(['최하늘',sc3,'DAY 1 20번 주장','',i<3?'단어 테스트':'단어 리스트','뜻 → '+w,1,'',st,re?K(2026,11,6,20,0):new Date(f),'v'+i,JSON.stringify({first:f,q:i<3?{t:'verb',a:[w],key:'x→'+w}:{t:'choice',key:w}})])});
const ROST=[['이름','학생 코드','교재','메모'],['김민서','1234','',''],['이준호','2222','',''],['박서연','3333','',''],['최하늘','4444','','']];
const MEMOR=[['주(월요일)','학생','선생님 한마디','다음 주 목표','저장 시각'],['2026-11-02','김민서','이번 주는 4일 동안 지문을 반복해서 32~35번 내용을 거의 외웠어요. 어법(수일치·분사)에서 실수가 남아 있어서 다음 주는 오답 노트로 어법을 집중해서 볼게요.','DAY 10~13 완료, 남은 오답 0개, 어법 80% 이상',new Date()]];
const SH={'기록':new Sheet('기록',LOGR),'현황':new Sheet('현황',NOWR),'오답노트':new Sheet('오답노트',NOTER),'학생명단':new Sheet('학생명단',ROST),'주간리포트':new Sheet('주간리포트',MEMOR)};
global.SpreadsheetApp={getActiveSpreadsheet:()=>({getSheetByName:n=>SH[n]||null,insertSheet:n=>(SH[n]=new Sheet(n,[])),getSheets:()=>Object.values(SH)})};
global.Utilities={formatDate:fmt};global.LockService={getScriptLock:()=>({waitLock(){},releaseLock(){}})};
global.ScriptApp={getService:()=>({getUrl:()=>'https://script.google.com/macros/s/TEST/exec'})};
global.HtmlService={createTemplate:(h)=>{const t={evaluate(){let out=h.replace(/<\?!=\s*(\w+)\s*\?>/g,(m,k)=>t[k]);return{setTitle(){return this},addMetaTag(){return this},html:out}}};return t}};
global.ContentService={createTextOutput:s=>({setMimeType(){return this},s}),MimeType:{JSON:1}};
global.PropertiesService={getScriptProperties:()=>({getProperty:()=>null})};global.CacheService={getScriptCache:()=>({get(){},put(){}})};
eval(fs.readFileSync(__dirname+'/Code.gs','utf8')+';global.doGet=doGet;global.reportData=reportData;global.saveMemo=saveMemo;');
const stub='<script>window.google={script:{run:{_s:null,_f:null,withSuccessHandler(f){this._s=f;return this},withFailureHandler(f){this._f=f;return this},saveMemo(...a){window.__saved=a;setTimeout(()=>this._s&&this._s(true),50)}}}}</script>';
const rep=doGet({parameter:{view:'dW6ypYyx',report:'1',who:'최하늘'}}).html.replace('<head>','<head>'+stub);
fs.writeFileSync(__dirname+'/out_report.html',rep);
fs.writeFileSync(__dirname+'/out_board.html',doGet({parameter:{view:'dW6ypYyx'}}).html);
console.log(JSON.stringify(reportData('2026-11-04').list.map(s=>({n:s.name,days:s.days,mins:s.mins,solved:s.solved,noteN:s.noteN,types:s.types.map(t=>t.k+':'+t.c+'/'+t.a),prog:s.prog.map(p=>p.done.length+'/'+p.doing.length),wraps:s.wraps.length,nNew:s.nNew,nFix:s.nFix,nLeft:s.nLeft,memo:!!s.memo})),null,0));
saveMemo('2026-11-06','이준호','좋아요','DAY 7');console.log(JSON.stringify(SH['주간리포트'].rows.map(r=>r.slice(0,4))));
const rep2=doGet({parameter:{view:'dW6ypYyx',report:'1',from:'2026-10-26',to:'2026-11-08',who:'최하늘'}}).html.replace('<head>','<head>'+stub);
fs.writeFileSync(__dirname+'/out_report2.html',rep2);
const d2=reportData('', '2026-11-06','2026-10-19');console.log('custom',d2.wk,d2.from,d2.to,d2.custom,d2.list.map(s=>s.name+':'+s.days.length).join(','));
const d3=reportData('', '2026-11-02','2026-11-08');console.log('fullweek',d3.wk,d3.custom);
const d4=reportData('', '2026-01-01','2026-11-06');console.log('toolong->week',d4.wk,d4.custom);
saveMemo('2026-10-19~2026-11-06','박서연','한 달 잘했어요','다음 달 목표');console.log(JSON.stringify(SH['주간리포트'].rows.map(r=>r.slice(0,4))));
const d5=reportData('', '2026-10-19','2026-11-06');console.log('memo',d5.list.filter(s=>s.memo).map(s=>s.name+':'+s.memo));

console.log('exam',JSON.stringify(reportData('2026-11-04').list.find(x=>x.name==='최하늘').exam));
console.log('voc',JSON.stringify(reportData('2026-11-04').list.find(x=>x.name==='최하늘').voc));
