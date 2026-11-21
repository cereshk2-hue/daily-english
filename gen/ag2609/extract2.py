import re, json
R = json.load(open('/home/claude/work/ag2609/raw.json', encoding='utf-8'))
L = open('/home/claude/work/ag2609/e2609.txt', encoding='utf-8').read().split('\n')
heads = [i for i, l in enumerate(L) if re.match(r'^\d{2}(~\d{2})?번┃', l)]
T = ['30','33','34','35','36','37','38','39','40','41~42']
OUT = {}
for k, h in enumerate(heads):
    no = L[h].split('번')[0]
    if no not in T: continue
    B = L[h:heads[k+1] if k+1 < len(heads) else len(L)]
    o = B.index('❙원본 문제❙'); stem = B[o+1].strip(); j = o+2; ps = []; foot = []
    while j < len(B) and not B[j].startswith('▌') and not B[j].startswith('[정답]'):
        x = B[j].strip()
        if x.startswith('*') or x.startswith('**'): foot.append(x)
        elif x: ps.append(x)
        j += 1
    opts = []
    while ps and re.match(r'^[①②③④⑤]', ps[-1]) and (no not in ('29','30','35','38','39') ):
        opts.insert(0, ps.pop())
    opts = [y.strip() for x in opts for y in re.split(r'\s*(?=[①②③④⑤])', x) if y.strip()]
    ans = next(l for l in B if l.startswith('[정답]'))
    tr = next(l for l in B if l.startswith('[해석]'))
    ko = [B[i-1].strip() for i, l in enumerate(B) if l.strip() == '해석' and i > 0]
    OUT[no] = dict(stem=stem, ps=ps, foot=foot, opts=opts, ans=ans, tr=tr, ko=ko, words=R[no]['words'])
U = lambda x: x.replace('\ue000', '').replace('\ue001', '') if isinstance(x, str) else [U(y) for y in x] if isinstance(x, list) else x   # 11/21 밑줄 표시 지움
OUT = {k: {kk: U(vv) for kk, vv in v.items()} for k, v in OUT.items()}
json.dump(OUT, open('/home/claude/work/ag2609/q.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
