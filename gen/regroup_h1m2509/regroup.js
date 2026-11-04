global.window={};require('/home/claude/proj/data/h1-mock-2509.js');const P=window.PKG;const A=require('./assign.json');
const D={};P.days.forEach(d=>D[d.id]=d);
// 'The ___ you practice, the better' 은 34번(the harder ..., the faster ...) 문법이라 34번으로
const g=A.out['32번 · 빈칸']['13'];const k=g.findIndex(([d,s,i])=>/The ______ you practice/.test(D[d].steps[s].items[i].q));
A.out['34번 · 빈칸']['13']=[g.splice(k,1)[0]];
const secRows={};for(const d of P.days.slice(5,9)){let cur;for(const r of d.passage){if(r[0]==='#'){cur=r[1];secRows[cur]=[r]}else secRows[cur].push(r)}}
const L=n=>Object.keys(secRows).find(l=>parseInt(l)===n);
const story={32:'32 빈칸',33:'33 빈칸',34:'34 빈칸',35:'35 무관한 문장',36:'36 글의 순서',37:'37 글의 순서',38:'38 문장 삽입',39:'39 문장 삽입',40:'40 요약문',41:'41 · 42 장문 (제목 · 어휘)'};
const plan=[[6,[32,33],'32·33번'],[7,[34,35],'34·35번'],[8,[36,37],'36·37번'],[9,[38,39],'38·39번'],[10,[40],'40번'],[11,[41],'41·42번']];
const tmpl=D.d6.steps;const newDays=[];let total=0;
for(const [no,nums,range] of plan){
  const labs=nums.map(L);
  const steps=tmpl.map((t,si)=>{const items=[];for(const l of labs)for(const [d,s,i] of (A.out[l][si]||[]))items.push(D[d].steps[s].items[i]);
    const st=Object.assign({},t,{items});return st}).filter(s=>s.items.length);
  steps.forEach(s=>total+=s.items.length);
  newDays.push({id:'p'+no,name:'DAY '+no,range,story:nums.map(n=>story[n]).join(' · ').replace('32 빈칸 · 33 빈칸','32 · 33 빈칸'),
    passage:[].concat(...labs.map(l=>secRows[l])),steps});
}
const old=P.days.slice(5,9).reduce((n,d)=>n+d.steps.reduce((m,s)=>m+s.items.length,0),0);
console.error('items old',old,'new',total);
newDays.forEach(d=>console.error(d.id,d.range,d.story,d.steps.length,d.steps.reduce((n,s)=>n+s.items.length,0),d.steps.map(s=>s.items.length).join(',')));
const tests=P.tests;delete P.tests;
P.days=P.days.slice(0,5).concat(newDays);
require('fs').writeFileSync('pkg.json',JSON.stringify(P));
