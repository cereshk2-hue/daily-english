global.window={};require(process.argv[2]);const P=window.PKG;
const norm=s=>String(s).replace(/\s+/g,' ').trim().toLowerCase();
for(const d of P.days.filter(d=>/^q/.test(d.id))){const T=norm(d.passage.filter(r=>r[0]!=='#').map(r=>r[1]).join(' '));
 for(const st of d.steps)for(const it of st.items){let s=null;
  if(st.type==='pick')s=it.s.replace(/\{([^|}]*)\|[^}]*\}/,'$1');
  if(st.type==='error'){let k=0;s=it.s.replace(/\[\[(.+?)\]\]/g,(m,x)=>k++===it.w?it.fix:x)}
  if(st.type==='verb')s=it.s.replace('___',it.a[0]);
  if(st.type==='blank')s=it.s.replace('____',it.opts[0]);
  if(s&&T.indexOf(norm(s).replace(/[.!?"]+$/,''))<0)console.log(d.id,st.type,'|',s.slice(0,140));
 }}
