import re,json
L=open('exam.txt').read().split('\n')
heads=[(i,l) for i,l in enumerate(L) if re.match(r'^[0-9~]+번┃',l)]
out={}
for k,(i,h) in enumerate(heads):
    j=heads[k+1][0] if k+1<len(heads) else len(L)
    sec=L[i:j]; num=h.split('번')[0]
    ko=[sec[t-1].strip() for t in range(1,len(sec)) if sec[t].strip()=='해석']
    a=sec.index('❙원본 문제❙') if '❙원본 문제❙' in sec else None
    orig=[]
    if a is not None:
        for l in sec[a+1:]:
            if l.startswith('▌'): break
            orig.append(l)
    ans=None
    for t in range(1,len(sec)):
        if sec[t].strip()=='정답':
            for b in range(t-1,max(0,t-4),-1):
                m=re.match(r'^\s*([①②③④⑤])',sec[b])
                if m: ans=m.group(1);break
            if ans: break
    out[num]={'head':h,'ko':ko,'orig':'\n'.join(orig).strip(),'ans':ans}
json.dump(out,open('sec.json','w'),ensure_ascii=False,indent=1)
for n in ['31','32','33','34','35','36','37','38','39','40','41~42']: print(n,out[n]['head'],out[n]['ans'],len(out[n]['ko']))
