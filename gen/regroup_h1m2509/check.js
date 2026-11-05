global.window={};require(process.argv[2]);const P=window.PKG;
const norm=s=>String(s).replace(/[‘’]/g,"'").replace(/[“”]/g,'"').replace(/\s+/g,' ').trim().toLowerCase().replace(/[.!?"]+$/,'');
let bad=0;
for(const d of P.days.filter(d=>/^q/.test(d.id))){
 const L=d.passage.filter(r=>r[0]!=='#').map(r=>norm(r[1]));const has=s=>L.some(l=>l.indexOf(norm(s))>=0);
 for(const st of d.steps)for(const it of st.items){
  if(st.type==='tf'&&it[4]&&!has(it[4])){bad++;console.log('TF ev',d.id,it[4])}
  if(it.per)it.per.forEach((p,i)=>{if(p[1]&&!has(p[1])){bad++;console.log('per ev',d.id,p[1])}});
  if(it.per&&it.per.length!==it.opts.length){bad++;console.log('per len',d.id,it.q)}
  if(st.type==='scramble'&&!has(it.en)){console.log('scr not in passage',d.id,it.en.slice(0,40))}
  if(st.type==='error'){const k=(it.s.match(/\[\[/g)||[]).length;if(it.w>=k){bad++;console.log('err w',it.s)}}
  if((st.type==='order'||st.type==='insert')&&it.lines.some(l=>!has(l))){bad++;console.log('order line',d.id,it.lines)}
  if(st.type==='mc'&&new Set(it.opts).size!==it.opts.length){bad++;console.log('dup opt',it.q)}
  if(st.type==='blank'&&!/____/.test(it.s)){bad++;console.log('blank',it.s)}
 }
 const seen={};for(const st of d.steps)for(const it of st.items){const k=st.type+'|'+JSON.stringify(Array.isArray(it)?it[0]:(it.s||it.q&&it.q+it.opts[0]||it.en||it.lines));if(seen[k]){bad++;console.log('DUP',d.id,k.slice(0,90))}seen[k]=1}
 // vocab context coverage
 const src=require('fs').readFileSync('/home/claude/proj/app.js','utf8');
}
console.log('bad',bad);
