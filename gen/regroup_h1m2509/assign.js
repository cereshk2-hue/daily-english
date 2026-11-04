global.window={};require('/home/claude/proj/data/h1-mock-2509.js');const P=window.PKG;
const tok=s=>String(s).toLowerCase().replace(/<[^>]+>/g,' ').replace(/\{([^|}]*)\|[^}]*\}/g,'$1').replace(/\[\[|\]\]/g,'').match(/[a-z']{3,}/g)||[];
// sections across d6..d9
const secs=[];
for(const d of P.days.slice(5,9)){let cur=null;for(const r of d.passage){if(r[0]==='#'){cur={label:r[1],num:parseInt(r[1]),rows:[],day:d.id};secs.push(cur)}else cur.rows.push(r)}}
secs.forEach(s=>{s.words=new Set(tok(s.rows.map(r=>r[1]).join(' ')))});
const byNum=n=>secs.find(s=>s.num===n||(s.num===41&&n===42));
function itemText(t,it){
  if(Array.isArray(it))return it[0]+' '+(it[4]||'');
  return [it.s,it.en,it.q,(it.lines||[]).join(' '),it.box&&'',(it.opts||[]).join(' ')].filter(Boolean).join(' ');
}
function best(text,cands){const w=tok(text);let b=null,bs=-1;for(const s of cands){let sc=0;for(const x of w)if(s.words.has(x))sc++;sc/=Math.sqrt(s.words.size);if(sc>bs){bs=sc;b=s}}return b}
const out={};const log=[];
for(const d of P.days.slice(5,9)){
  const cands=secs.filter(s=>s.day===d.id);
  d.steps.forEach((st,si)=>{
    st.items.forEach((it,ii)=>{
      let s=null;
      if(st.type==='vocab')s=byNum(it[2]);
      else if(st.type==='tf')s=byNum(it[3]);
      else if(it.n)s=byNum(it.n);
      else if(it.box)s=secs.find(x=>x.label===it.box[0]);
      if(!s)s=best(itemText(st.type,it),cands);
      if(!s||s.day!==d.id)log.push(['X',d.id,si,ii]);
      (out[s.label]=out[s.label]||{})[si]=(out[s.label][si]||[]);out[s.label][si].push([d.id,si,ii]);
    });
  });
}
for(const s of secs){const o=out[s.label]||{};console.log(s.label,Object.keys(o).map(k=>k+':'+o[k].length).join(' '))}
console.log(log);
require('fs').writeFileSync('assign.json',JSON.stringify({secs:secs.map(s=>({label:s.label,num:s.num,day:s.day})),out}));
