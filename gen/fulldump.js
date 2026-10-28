global.window={}; require(process.argv[2]); const P=window.PKG; const ids=process.argv[3].split(',');
const s=x=>String(x).replace(/<br>/g,' / ').replace(/<[^>]+>/g,'');
for (const d of P.days.filter(d=>ids.includes(d.id))) { console.log('\n##### '+d.id+' '+d.range);
 d.steps.forEach(st=>{ if(st.type==='vocab'){console.log('[V] '+st.items.map(w=>w[0]+'='+w[1]).join(' ; '));return;}
  st.items.forEach((q,i)=>{ let a;
   if(Array.isArray(q)) a=`${q[0]} => ${q[1]?'T':'F'}`;
   else if(st.type==='pick'){ const m=q.s.match(/\{([^|}]*)\|([^}]*)\}/); a=`${q.s.replace(/\{[^}]*\}/,'[ '+m[1]+' / '+m[2]+' ]')} => ${m[1]}`; }
   else if(st.type==='verb') a=`${q.s} (${q.v}) => ${q.a}`;
   else if(st.type==='error'){ const m=[...q.s.matchAll(/\[\[(.*?)\]\]/g)].map(x=>x[1]); a=`${q.s} => #${q.w+1} ${m[q.w]} -> ${q.fix}`; }
   else if(st.type==='order') a='ORDER: '+q.lines.join(' / ');
   else if(st.type==='insert') a=`INSERT given#${q.given}: ${q.lines[q.given]}`;
   else if(st.type==='odd') a=`ODD: ${q.lines[q.odd]}`;
   else if(st.type==='blank') a=`${q.s} => ${q.opts[0]} [${q.opts.slice(1)}]`;
   else if(st.type==='mc') a=`${s(q.q)} => ${s(q.opts[0])}  ✗[${q.opts.slice(1).map(s).join(' | ')}]`;
   else if(st.type==='scramble') a=`SCR: ${q.en} / ${q.ko}`;
   const ex=(Array.isArray(q)?q[2]:q.ex||'').replace(/\n/g,' ¶ ');
   console.log(`[${st.title.slice(0,5)}] ${a}${ex?'\n      ex: '+ex:''}`); }); }); }
