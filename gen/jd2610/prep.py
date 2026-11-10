import json, re
Q = json.load(open('/home/claude/work/jd2610/q.json'))
L = open('/home/claude/work/jd2610/e2610.txt', encoding='utf-8').read().split('\n')
heads = [i for i, l in enumerate(L) if re.match(r'^\d{2}(~\d{2})?번┃', l)]
def split(t):
    t = re.sub(r'\( [①-⑤] \)\s*', '', t)
    t = re.sub(r'[①-⑤]', '', t)
    return [s.strip() for s in re.split(r'(?<=[.!?”"])\s+(?=[A-Z“"‘(])', t) if s.strip()]
OUT = {}
for k, h in enumerate(heads):
    no = L[h].split('번')[0]
    if no not in Q: continue
    B = L[h:heads[k+1] if k+1 < len(heads) else len(L)]
    checks = []
    for i, l in enumerate(B):
        if l.strip() == 'CHECK' and i+2 < len(B):
            # the sentence line with ( / ) follows within 3 lines
            for j in range(i+1, min(i+5, len(B))):
                if re.search(r'\([^()]+ / [^()]+\)', B[j]): checks.append(B[j].strip()); break
    q = Q[no]; text = ' '.join(q['ps'][1:] if no in ('38','39') else q['ps'])
    OUT[no] = dict(sents=split(text) if no not in ('28',) else q['ps'], ko=q['ko'], checks=checks, given=q['ps'][0] if no in ('38','39') else None)
json.dump(OUT, open('/home/claude/work/jd2610/prep.json','w',encoding='utf-8'), ensure_ascii=False, indent=1)
for n,v in OUT.items(): print(n, len(v['sents']), len(v['ko']), len(v['checks']))
