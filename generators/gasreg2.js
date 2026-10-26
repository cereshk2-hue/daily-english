// 오답 노트 시트 코드 단독 점검 (가짜 SpreadsheetApp)
class Sheet{constructor(n){this.name=n;this.d=[];}
 getLastRow(){return this.d.length}
 getRange(r,c,nr,nc){const sh=this; if(typeof r==='string') return {setNumberFormat(){return this},createFilter(){return this}};
  nr=nr||1; nc=nc||1;
  return {setValues(v){v.forEach((row,i)=>{sh.d[r-1+i]=sh.d[r-1+i]||[];row.forEach((x,j)=>sh.d[r-1+i][c-1+j]=x)});return this},
   getValues(){const o=[];for(let i=0;i<nr;i++){const row=[];for(let j=0;j<nc;j++)row.push((sh.d[r-1+i]||[])[c-1+j]??'');o.push(row)}return o},
   getValue(){return (sh.d[r-1]||[])[c-1]??''},setFontWeight(){return this},setBackground(){return this},setFontColor(){return this},setNumberFormat(){return this},createFilter(){return this},
   createTextFinder(t){return {matchEntireCell(){return this},findNext(){for(let i=0;i<nr;i++){if(String((sh.d[r-1+i]||[])[c-1])===t)return {getRow:()=>r+i}}return null}}}}}
 appendRow(row){this.d.push(row.slice())} setFrozenRows(){} setColumnWidth(){} hideColumns(){} deleteRow(i){this.d.splice(i-1,1)}}
const sheets={}; const ss={getSheetByName:n=>sheets[n]||null,insertSheet:(n)=>sheets[n]=new Sheet(n),getSheets:()=>Object.values(sheets)};
global.SpreadsheetApp={getActiveSpreadsheet:()=>ss}; global.LockService={getScriptLock:()=>({waitLock(){},releaseLock(){}})};
global.ContentService={createTextOutput:(s)=>({s,setMimeType(){return this}}),MimeType:{JSON:1}};
global.CacheService={getScriptCache:()=>({get(){},put(){}})}; global.PropertiesService={getScriptProperties:()=>({getProperty(){},setProperty(){}})};
global.HtmlService={};
global.Utilities={formatDate:()=>'10/26 12:40'};
global.SpreadsheetApp.newDataValidation=()=>({requireValueInList(){return this},setAllowInvalid(){return this},setHelpText(){return this},build(){return {}}});
Sheet.prototype.getMaxRows=function(){return 100}; Sheet.prototype.insertColumnAfter=function(){};
const _gr=Sheet.prototype.getRange; Sheet.prototype.getRange=function(...a){const r=_gr.apply(this,a); r.setDataValidation=()=>r; r.setValue=(v)=>{this.d[a[0]-1]=this.d[a[0]-1]||[];this.d[a[0]-1][a[1]-1]=v;return r}; return r};
const src=require('fs').readFileSync('/home/claude/proj/sheet/Code.gs','utf8'); eval(src.replace(/^var /gm,'global.').replace(/^function (\w+)/gm,'global.$1 = function $1'));
const ck=(o)=>JSON.parse(checkRoster(Object.assign({school:'중2 비상(황종배)'},o)).s);
console.log('처음(명단 없음, 등록 아님)', ck({name:'',code:''}));
console.log('새 이름 등록', ck({name:'김민준',code:'4821',reg:'1'}), sheets['학생명단'].d.slice(1));
console.log('같은 이름 다른 코드', ck({name:'김민준',code:'1111',reg:'1'}));
console.log('같은 이름 맞는 코드', ck({name:'김민준',code:'4821'}));
console.log('배경 확인(reg 없음) 모르는 이름', ck({name:'박지호',code:'1234'}), sheets['학생명단'].d.length-1);
console.log('3자리 코드 등록 시도', ck({name:'박지호',code:'123',reg:'1'}));
sheets['학생명단'].d[1][3]='그만둠'; console.log('그만둠', ck({name:'김민준',code:'4821',reg:'1'}));
