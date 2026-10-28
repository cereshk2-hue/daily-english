// 정답이 opts[0]이 아닌 것으로 보이는 mc 문항 찾기 (per 노트 / 해설 '정답 ▶ X' 기준)
const fs=require('fs');
for (const f of fs.readdirSync('/home/claude/proj/data').filter(f=>f.endsWith('.js'))) {
  global.window={}; delete require.cache[require.resolve('/home/claude/proj/data/'+f)]; require('/home/claude/proj/data/'+f);
  for (const d of window.PKG.days) d.steps.forEach(st=>{ if(st.type!=='mc'&&st.type!=='blank')return; (st.items||[]).forEach((q,i)=>{
    const strip=s=>String(s).replace(/<[^>]+>/g,'').trim();
    const m=String(q.ex||'').match(/정답 ▶ ([^\n]+)/); if(!m) return; const a=strip(m[1]).replace(/\s*\(.*$/,'');
    const idx=q.opts.findIndex(o=>strip(o)===strip(m[1])||strip(o)===a||strip(o).startsWith(a));
    if(idx>0) console.log(f,d.id,st.title,i,'ans idx',idx,'|',strip(q.opts[0]).slice(0,40),'| ex:',m[1].slice(0,40));
  });});
}
