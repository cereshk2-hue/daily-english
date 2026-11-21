import re, json, sys
L = open('/home/claude/work/ag2609/e2609.txt', encoding='utf-8').read().split('\n')
heads = [i for i, l in enumerate(L) if re.match(r'^\d{2}(~\d{2})?번┃', l)]
out = {}
for k, h in enumerate(heads):
    end = heads[k+1] if k+1 < len(heads) else len(L)
    B = L[h:end]; no = B[0].split('번')[0]; typ = B[0].split('┃')[1]
    # 원본 문제
    try: o = B.index('❙원본 문제❙')
    except ValueError: o = None
    stem = passage = None; opts = []
    if o is not None:
        stem = B[o+1].strip(); j = o+2; ps = []
        while j < len(B) and not re.match(r'^[①②③④⑤]', B[j].strip()) and not B[j].startswith('▌'):
            ps.append(B[j].strip()); j += 1
        passage = '\n'.join(x for x in ps if x)
        while j < len(B) and re.match(r'^[①②③④⑤]', B[j].strip()): opts.append(B[j].strip()); j += 1
    ans = next((l for l in B if l.startswith('[정답]')), None)
    tr = next((l for l in B if l.startswith('[해석]')), None)
    # 문장별 해석: '해석' 줄 바로 앞의 한글 줄
    ko = [B[i-1].strip() for i, l in enumerate(B) if l.strip() == '해석' and i > 0]
    # words
    w = []
    wi = [i for i, l in enumerate(B) if l.strip() == '❙WORDS & EXPRESSIONS❙']   # 11/21 앞에 공백 있는 줄도
    if wi:
        j = wi[0] + 1
        while j < len(B) and '출제 가능한' not in B[j]: w.append(B[j]); j += 1
    out[no] = dict(typ=typ, stem=stem, passage=passage, opts=opts, ans=ans, tr=tr, ko=ko, words='\n'.join(w).strip())
json.dump(out, open('/home/claude/work/ag2609/raw.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
for n, v in out.items(): print(n, v['typ'], v['ans'], len(v['ko']), len(v['opts']), (v['passage'] or '')[:60])
