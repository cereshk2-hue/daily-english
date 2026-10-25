// node tools/validate.js data/xxx.js  — 데이터 형식·본문 일치 검사
const fs=require('fs'),vm=require('vm');const ctx={window:{}};vm.runInNewContext(fs.readFileSync(process.argv[2],'utf8'),ctx);
const P=ctx.window.PKG;let bad=0;const err=(d,s,m)=>{bad++;console.log(`✗ ${d} ${s}: ${m}`)};
const n=s=>s.replace(/[’‘]/g,"'").replace(/…/g,'...').replace(/\s+/g,' ').trim();
for(const d of P.days){
  const text=n(d.passage.map(l=>l[1]).join(' ')).toLowerCase(), has=f=>n(f).toLowerCase().replace(/^\(|\)$/g,'').split(/(?<=[.!?])\s+/).every(x=>text.includes(x.replace(/^\(|\)$/g,'').replace(/[.!?]$/,''))), lines=d.passage.filter(l=>l[0]!=='#').map(l=>n((l[0]?l[0]+': ':'')+l[1]));
  let cnt=0;
  for(const st of d.steps){
    st.items.forEach((q,i)=>{cnt++;const tag=`${st.title}#${i+1}`;
      if(st.type==='pick'){const m=q.s.match(/\{([^}]*)\}/g);if(!m||m.length!==1)err(d.id,tag,'중괄호 1개 필요');else{const o=m[0].slice(1,-1).split('|');if(o.length<2||new Set(o).size!==o.length)err(d.id,tag,'선택지 이상');
        const filled=n(q.s.replace(/\{([^}|]*)[^}]*\}/,'$1').replace(/^\(|\)$/g,''));if(!has(filled))err(d.id,tag,'정답 넣은 문장이 본문에 없음: '+filled);}}
      if(st.type==='verb'){if((q.s.match(/___/g)||[]).length!==1)err(d.id,tag,'___ 1개 필요');const f=n(q.s.replace('___',q.a[0]));if(!has(f))err(d.id,tag,'정답 넣은 문장이 본문에 없음: '+f);}
      if(st.type==='error'){const m=[...q.s.matchAll(/\[\[(.+?)\]\]/g)];if(m.length<3||q.w>=m.length)err(d.id,tag,'표시 개수/정답 번호 이상');
        let k=0;const f=n(q.s.replace(/\[\[(.+?)\]\]/g,(a,b)=>k++===q.w?q.fix:b));if(!has(f))err(d.id,tag,'고친 문장이 본문에 없음: '+f);}
      if(st.type==='order')q.lines.forEach(l=>{if(!lines.some(x=>x===n(l)||x.startsWith(n(l).replace(/\)$/,''))||x.includes(n(l))))err(d.id,tag,'본문에 없는 줄: '+l)});
      if(st.type==='order'){const sl=lines.filter(x=>!/^[❶-❿]$/.test(x)),idx=q.lines.map(l=>sl.findIndex(x=>x.includes(n(l).replace(/\)$/,''))));if(idx.some((v,j)=>j&&v<=idx[j-1]))err(d.id,tag,'본문 순서와 다름 '+idx)}
      if(st.type==='insert'){if(!(q.given>=1&&q.given<q.lines.length))err(d.id,tag,'given 범위');q.lines.forEach(l=>{if(!has(l))err(d.id,tag,'본문에 없는 문장: '+l)});
        const sl=lines.filter(x=>!/^[❶-❿]$/.test(x)),idx=q.lines.map(l=>sl.findIndex(x=>x.includes(n(l).replace(/[.!?]$/,''))));if(idx.some((v,j)=>j&&v!==idx[j-1]+1))err(d.id,tag,'연속된 본문 문장이 아님 '+idx)}
      if(st.type==='odd'){q.lines.forEach((l,j)=>{const inP=has(l);if(j===q.odd&&inP)err(d.id,tag,'어색한 문장이 본문에 있음');if(j!==q.odd&&!inP)err(d.id,tag,'본문에 없는 문장: '+l)})}
      if(st.type==='blank'){if((q.s.match(/____/g)||[]).length!==1)err(d.id,tag,'____ 1개');if(!has(q.s.replace('____',q.opts[0])))err(d.id,tag,'정답 넣은 문장이 본문에 없음');if(new Set(q.opts).size!==q.opts.length)err(d.id,tag,'선택지 중복')}
      if(st.type==='scramble'&&!has(q.en))err(d.id,tag,'본문에 없음: '+q.en);
      if(st.type==='mc'&&new Set(q.opts).size!==q.opts.length)err(d.id,tag,'선택지 중복');
      if(st.type==='tf'&&typeof q[1]!=='boolean')err(d.id,tag,'T/F 값');
      if(st.type==='vocab'&&(q.length<2||q.length>3))err(d.id,tag,'어휘 형식');
    });
  }
  console.log(`${d.id}: ${d.steps.length}단계 ${cnt}문항`);
}
console.log(bad?`문제 ${bad}개`:'✓ 모두 통과');process.exit(bad?1:0);
