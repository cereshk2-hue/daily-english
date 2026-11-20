import re, json
CIR='①②③④⑤'
def load(fn):
    t=open(fn).read()
    t=re.sub(r'=====P\d[LR]\n','\n',t)
    lines=t.split('\n'); qs={}; cur=None; nxt=1
    for ln in lines:
        m=re.match(r'^\s*(\d{1,2})\.(\s|$)',ln)
        if m and int(m.group(1))==nxt:
            cur=nxt; qs[cur]=[]; nxt+=1
        if cur: qs[cur].append(ln)
    return {k:'\n'.join(v) for k,v in qs.items()}
def opts(txt):
    # 마지막 ① 부터 끝까지를 선택지로
    i=txt.rfind('①')
    seg=txt[i:]
    parts=re.split(r'([①②③④⑤])',seg)[1:]
    d={}
    for a,b in zip(parts[0::2],parts[1::2]):
        b=b.split('\n\n\n')[0]; d[a]=re.sub(r'\s+',' ',b).strip()
    return [d.get(c,'') for c in CIR]
E=load('even_c.txt'); O=load('odd_c.txt')
print(len(E),len(O))
OK=[int(x) for x in '3 1 1 3 5 4 1 3 4 4 1 5 2 4 5 1 2 5 1 2 2 5 2 5 5 4 5 4 3 3 1 1 5 3 3 2 4 3 4 2 1 2 4 2 3'.split()]
EK=[int(x) for x in '1 1 3 3 5 4 1 3 4 4 2 5 1 4 5 5 2 1 1 5 2 2 3 1 5 4 5 4 3 3 1 1 5 2 3 2 4 3 4 2 5 2 4 2 3'.split()]
res={}
for q in range(1,46):
    eo,oo=opts(E[q]),opts(O[q])
    ot=oo[OK[q-1]-1]; et=eo[EK[q-1]-1]
    N=lambda x: re.sub(r'[^A-Za-z가-힣$0-9]','',x)[:30]
    same = N(ot)==N(et)
    stem_e=re.sub(r'\s+',' ',E[q][:E[q].find('①')] if '①' in E[q] else E[q])[:80]
    flag='' if same else '  <<< 다름'
    print(q, OK[q-1], EK[q-1], ('same' if eo==oo else 'shuffled'), '|', et[:40], flag)
    res[q]={'even':eo,'odd':oo}
json.dump({'E':E,'O':O},open('qs.json','w'),ensure_ascii=False)
