// 지문별 바탕: 원래 d6~d9(orig) 문항을 assign.json 대로 지문에 나누고, 40번은 이미 보강한 현재 p10 을 그대로 쓴다
const fs=require('fs');
const load=f=>{global.window={};delete require.cache[require.resolve(f)];require(f);return window.PKG};
const O=load('/home/claude/work/regroup/orig_h1-mock-2509.js');const C=load('/home/claude/proj/data/h1-mock-2509.js');
const A=require('./assign.json');const D={};O.days.forEach(d=>D[d.id]=d);
const g=A.out['32번 · 빈칸']['13'];const k=g.findIndex(([d,s,i])=>/The ______ you practice/.test(D[d].steps[s].items[i].q));
A.out['34번 · 빈칸']['13']=[g.splice(k,1)[0]];
const secRows={};for(const d of O.days.slice(5,9)){let cur;for(const r of d.passage){if(r[0]==='#'){cur=r[1];secRows[cur]=[r]}else secRows[cur].push(r)}}
const tmpl=D.d6.steps;const out={};
for(const lab of Object.keys(secRows)){const n=parseInt(lab);
  if(n===40){out[40]=JSON.parse(JSON.stringify(C.days.find(d=>d.id==='p10')));continue}
  out[n]={passage:secRows[lab],steps:tmpl.map((t,si)=>Object.assign({},t,{items:(A.out[lab][si]||[]).map(([d,s,i])=>D[d].steps[s].items[i])}))};}
fs.writeFileSync('base.json',JSON.stringify({head:O.days.slice(0,5),pk:Object.assign({},O,{days:undefined,tests:undefined}),per:out}));
console.log(Object.keys(out).map(n=>n+':'+out[n].steps.reduce((a,s)=>a+s.items.length,0)).join(' '));
