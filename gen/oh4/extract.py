import re, json
L = open('/home/claude/work/oh4/l4.txt', encoding='utf-8').read().split('\n')
H = [i for i, l in enumerate(L) if re.fullmatch(r'본문 [❶-❼]', l)] + [len(L)]
hang = lambda s: len(re.findall(r'[가-힣]', s))
out = []
for k in range(7):
    a, b = H[k], H[k+1]; sec = L[a][-1]
    kp = next(i for i in range(a, b) if hang(L[i]) > 40 and not L[i].strip().startswith('❮'))
    lines = [L[i] for i in range(a + 1, kp) if hang(L[i]) == 0 and re.search(r'[A-Za-z]{2}', L[i]) and '⤷' not in L[i] and '⤶' not in L[i] and not L[i].strip().startswith('(')]
    txt = re.sub(r'\s+', ' ', ' '.join(x.strip() for x in lines)).strip()
    E = [s for s in re.split(r'(?<=[.?!])\s+(?=[A-Z“"])', txt) if s]
    K = [s for s in re.split(r'(?<=[.?!])\s+', L[kp].strip()) if s]
    out.append([sec, E, K]); print(sec, len(E), len(K))
json.dump(out, open('/home/claude/work/oh4/raw.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
