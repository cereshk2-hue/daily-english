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
const src=require('fs').readFileSync('/home/claude/proj/sheet/Code.gs','utf8'); eval(src.replace(/^var /gm,'global.').replace(/^function (\w+)/gm,'global.$1 = function $1'));
const post=(o)=>doPost({postData:{contents:JSON.stringify(Object.assign({k:KEY},o))}});
const N=(id,at,extra)=>Object.assign({name:'김민준',unit:'m2-x',school:'중2 비상',id,at,day:'DAY 1',group:'7과',step:'어법선택',text:'문제 '+id,wrong:1,conf:false,ok:false,data:JSON.stringify({id,at,q:{t:'tf'}})},extra||{});
post({notes:[N('a',100),N('b',100)]});
console.log('rows', sheets['오답노트'].d.length-1, sheets['오답노트'].d[1].slice(0,10).join(' | '));
post({notes:[N('a',200,{ok:true})]}); console.log('a 갱신', sheets['오답노트'].d[1][8]);
post({notes:[N('a',150,{ok:false})]}); console.log('옛 기록은 무시', sheets['오답노트'].d[1][8]);
post({notes:[N('b',300,{del:true})]}); console.log('b 삭제 후 rows', sheets['오답노트'].d.length-1);
let r=JSON.parse(getNotes({name:'김민준',unit:'m2-x',code:''}).s); console.log('명단 없음 → 받기', r.ok, r.notes.length);
sheets['학생명단']=new Sheet('학생명단'); sheets['학생명단'].d=[['이름','학생 코드','교재','메모'],['김민준','4821','','']];
r=JSON.parse(getNotes({name:'김민준',unit:'m2-x',code:'1111'}).s); console.log('코드 틀림', r.ok, r.notes.length);
r=JSON.parse(getNotes({name:'김민준',unit:'m2-x',code:'4821'}).s); console.log('코드 맞음', r.ok, r.notes.length);
r=JSON.parse(getNotes({name:'김민준',unit:'other',code:'4821'}).s); console.log('다른 단원', r.ok, r.notes.length);
console.log('rows만 있는 기존 기록 보내기', post({rows:[]}).s);
