global.window={}; require(process.argv[2]); const P=window.PKG;
const strip=s=>String(s).replace(/<[^>]+>/g,'');
for (const di of process.argv.slice(3).map(Number)) { const d=P.days[di]; console.log('##### '+d.name+' '+d.range);
 d.passage.forEach(l=>console.log('  P|',l[1],'|',l[2]));
 d.steps.forEach(st=>{ console.log('=== '+st.title);
  if(st.type==='vocab'){ console.log(st.items.map(w=>w[0]+'='+w[1]).join(' ; ')); return; }
  st.items.forEach((q,i)=>{ let s;
   if(Array.isArray(q)) s=`${q[0]} => ${q[1]} | ${q[2].split('\n')[1]||''}`;
   else if(st.type==='pick') s=q.s;
   else if(st.type==='verb') s=`${q.s} (${q.v}) => ${q.a}`;
   else if(st.type==='error'){ const m=[...q.s.matchAll(/\[\[(.*?)\]\]/g)].map(x=>x[1]); s=`${q.s} | wrong=${m[q.w]} -> ${q.fix}`; }
   else if(st.type==='order') s=q.lines.join(' / ');
   else if(st.type==='insert') s=`GIVEN: ${q.lines[q.given]} | REST: ${q.lines.filter((_,j)=>j!==q.given).join(' // ')}`;
   else if(st.type==='odd') s=`ODD: ${q.lines[q.odd]}`;
   else if(st.type==='blank') s=`${q.s} => ${q.opts[0]} [${q.opts.slice(1)}]`;
   else if(st.type==='mc') s=`${strip(q.q)} => ${strip(q.opts[0])} [${q.opts.slice(1).map(strip).join(' | ')}]`;
   else if(st.type==='scramble') s=q.en;
   console.log(' '+(i+1)+'. '+s); }); }); }
