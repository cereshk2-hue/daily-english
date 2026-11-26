// 11/26 전 단원 OMR 시험 구조 검사
const fs=require('fs');const C='①②③④⑤';const out=[];let nT=0,nI=0;
const strip=s=>String(s||'').replace(/<[^>]+>/g,'').replace(/&lt;/g,'<').replace(/&gt;/g,'>').replace(/&amp;/g,'&');
for(const f of fs.readdirSync('/home/claude/proj/data').filter(f=>f.endsWith('.js'))){
  global.window={};try{delete require.cache['/home/claude/proj/data/'+f];require('/home/claude/proj/data/'+f)}catch(e){out.push([f,'LOAD',e.message]);continue}
  const P=window.PKG;if(!P||!P.tests)continue;
  const ids=new Set();
  for(const t of P.tests){nT++;if(ids.has(t.id))out.push([f,t.id,'-','시험 id 중복']);ids.add(t.id);
    const ns=new Set();
    t.items.forEach((it,k)=>{nI++;const E=(m)=>out.push([f,t.id,it.n,m]);
      if(ns.has(String(it.n)))E('문항 번호 중복');ns.add(String(it.n));
      const st=strip(it.stem),bd=strip(it.body),ex=String(it.ex||'');
      if(it.kind==='write'){if(!it.blanks||!it.blanks.length)E('서술형 빈칸 없음');return}
      const o=it.opts||[];
      if(o.length!==5)E('선택지 '+o.length+'개');
      o.forEach((x,i)=>{const s=strip(x).trim();if(!s)E('선택지 '+C[i]+' 비어 있음');if(/________/.test(s)&&!/빈칸|들어갈/.test(st))E('선택지에 빈칸 찌꺼기 '+C[i])});
      const so=o.map(x=>strip(x).trim());const numOnly=so.every((x,i)=>x===C[i]);if(!numOnly&&so.some((x,i)=>x===C[i]))E('선택지 일부만 번호뿐 '+so.join('|').slice(0,60));if(numOnly&&!/[①-⑤❶-❺➀-➄ⓐ-ⓔ⓵-⓹]/.test(String(it.body||'')+String(it.ctx||'')))E('선택지가 번호뿐인데 본문에 ①~⑤ 표시 없음');if(!numOnly&&new Set(so).size!==so.length)E('선택지 중복 '+so.join(' | ').slice(0,80));
      const A=Array.isArray(it.ans)?it.ans:[it.ans];
      if(!A.length||A.some(a=>!(Number.isInteger(a)&&a>=0&&a<5)))E('정답 범위 오류 '+JSON.stringify(it.ans));
      if(Array.isArray(it.ans)&&it.ans.length>1&&!/모두|2개|두 개|모두 고르/.test(st))E('복수 정답인데 발문에 "모두" 없음');
      if(!Array.isArray(it.ans)&&/모두 고르/.test(st))E('"모두 고르시오"인데 정답 1개');
      if(/개수|몇 개/.test(st)&&!so.every(s=>/^\d+\s*개?$|^[0-9]+$|개$/.test(s)))E('개수 문제인데 선택지가 개수가 아님: '+so[0].slice(0,40));
      if(/(^|\s)① ?\S{0,6}\s+② ?\S{0,6}\s+③/.test(bd.slice(-120))&&!/[ⓐ-ⓙ]/.test(bd.slice(-120)))E('본문 끝에 선택지 줄이 남음: '+bd.slice(-70));
      const m=ex.match(/정답\s*▶\s*([①-⑤]+)/);if(m){const want=A.map(a=>C[a]).join('');if(m[1]!==want)E('해설 정답 '+m[1]+' ≠ 정답 '+want)}
      if((String(it.body||'')+o.join('')+String(it.stem||'')).split('<u>').length!==(String(it.body||'')+o.join('')+String(it.stem||'')).split('</u>').length)E('<u> 짝 안 맞음');
      if(/밑줄 친/.test(st)&&!/<u>|[ⓐ-ⓙ①-⑤❶-❺]|\(A\)/.test(String(it.body||'')+o.join('')+String(it.ctx||'')))E('밑줄 문제인데 밑줄 표시 없음');
      if(/다음 글|윗글|위 글|글의/.test(st)&&!bd.trim()&&!strip(it.ctx).trim()&&!it.grp){const nn=parseInt(it.n);const cov=t.items.slice(0,k).some(p=>{const m=strip(p.body).match(/\[(\d+)\s*[~\-]\s*(\d+)\]/);return m&&nn>=+m[1]&&nn<=+m[2]});if(!cov)E('글이 필요한데 본문 없음')}
      if(/\s–\s/.test(so.join(' '))&&so.filter(s=>/\s–\s/.test(s)).length<5)E('선택지 일부에만 " – " (줄바꿈 찌꺼기?) '+so.find(s=>/\s–\s/.test(s)).slice(0,50));
    })}
}
console.log('시험',nT,'문항',nI,'의심',out.length);for(const r of out)console.log(r.join(' | '));
