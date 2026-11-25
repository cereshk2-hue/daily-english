# 11/24 ★ 끝판왕 '교집합 = 정답' 패턴 제거 (모든 고등 끝판왕 공통) — 학생 제보
# 옛 구조 (a,b)✓ (a,b') (a',b) (x,y) (z,w): (A)·(B) 정답 낱말만 두 번씩 나와 겹치는 짝 = 정답
# 새 구조 2×2 격자 + 1: (a,b)✓ (a,b') (a',b) (a',b') (z,w) — a·a'·b·b' 모두 두 번씩 → 빈도로 못 고름. 오답 순서도 섞음
# 각 *_build.py finalize()에서 서술형이 아닌 문항마다 fix() → (번호 붙인 뒤) post()
import re, random
from collections import Counter
CIRC = '①②③④⑤'

def leak(o, ans=0):
    """(A)·(B) 모두 최다 빈도인 짝이 하나뿐이고 그게 정답이면 True"""
    ca, cb = Counter(p[0] for p in o), Counter(p[1] for p in o)
    top = [p for p in o if ca[p[0]] == max(ca.values()) and cb[p[1]] == max(cb.values())]
    return len(top) == 1 and top[0] == o[ans]

def _lead(chunk):
    m = re.match(r'[①②③④⑤]+\s*\(?([A-Za-z][A-Za-z\-\']*(?: [a-z][a-z\-\']*)*?)(?=$|[\s(→:,·)])', chunk)
    return m.group(1) if m else None

# 11/24 21:45 선생님: "규칙이 생기는 건 유감" → 모양을 섞고(격자·사슬A·사슬B·두 짝), 정답 자리는 모양 안 다섯 자리 중 무작위
#   → 겹침·빈도·'한 번만 나온 짝' 어느 것으로도 정답을 못 고름. (A)/(B) 각 칸의 틀린 낱말은 원래 오답 낱말에서만 씀
TEMPL = {'grid': [(0, 0), (0, 1), (1, 0), (1, 1), (2, 2)], 'chainA': [(0, 0), (1, 0), (1, 1), (2, 1), (3, 2)],
         'chainB': [(0, 0), (0, 1), (1, 1), (1, 2), (2, 3)], 'pairs': [(0, 0), (0, 1), (1, 2), (2, 2), (3, 3)]}
FALLBACK = {'fanA': [(0, 0), (1, 0), (2, 0), (0, 1), (1, 1)], 'fanB': [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1)]}   # 한쪽 오답 낱말이 하나뿐일 때
STATS = {}
def fix(it, rng, gloss, TR=None, key=None):
    import os
    if os.environ.get("NOGRID"): return False
    o = [tuple(p) for p in it['o']]
    a, b = o[0]
    onlyB = [p[0] for p in o[1:] if p[1] == b and p[0] != a]; onlyA = [p[1] for p in o[1:] if p[0] == a and p[1] != b]
    WA = list(dict.fromkeys(onlyB + [p[0] for p in o[1:] if p[0] != a]))   # 한 칸 함정 낱말을 앞에
    WB = list(dict.fromkeys(onlyA + [p[1] for p in o[1:] if p[1] != b]))
    ok = [k for k, T in TEMPL.items() if len({x for x, _ in T}) - 1 <= len(WA) and len({y for _, y in T}) - 1 <= len(WB)]
    if not ok: ok = [k for k, T in FALLBACK.items() if len({x for x, _ in T}) - 1 <= len(WA) and len({y for _, y in T}) - 1 <= len(WB)]
    assert ok, o
    name = rng.choice(sorted(ok)); T = {**TEMPL, **FALLBACK}[name]; ci = rng.randrange(5)
    ca, cb = T[ci]
    ia = [x for x in dict.fromkeys(x for x, _ in T) if x != ca]; ib = [y for y in dict.fromkeys(y for _, y in T) if y != cb]
    MA = {ca: a, **{x: WA[i] for i, x in enumerate(ia)}}; MB = {cb: b, **{y: WB[i] for i, y in enumerate(ib)}}
    new = [(MA[x], MB[y]) for x, y in T]
    wrong = [p for i, p in enumerate(new) if i != ci]; rng.shuffle(wrong)
    it['o'] = [(a, b)] + wrong
    assert len(set(it['o'])) == 5 and not leak(it['o']), it['o']
    STATS[(name, ci)] = STATS.get((name, ci), 0) + 1
    # 해설: 낱말 하나를 설명하는 '① w(뜻)…' 조각만 남기고(빠진 낱말이 섞인 조각·짝 설명 'X → Y' 조각은 지움), 설명 없는 오답은 줄을 새로 붙임
    src = TR.pop(key) if (TR is not None and key in TR) else it['tr']
    G = dict(re.findall(r'([A-Za-z][A-Za-z\-]*)\(([^()]*?)\)', src))
    gl = lambda w: G.get(w) or gloss(w) or ''
    words = {w for p in it['o'] for w in p}
    parts = re.split(r' (?=[①②③④⑤]+\s*\(?[A-Za-z])', src)
    if re.match(r'[①②③④⑤]', parts[0]): parts = [''] + parts
    def tagged(c): return re.findall(r'[①②③④⑤]+\s*\(?([A-Za-z][A-Za-z\-]*(?: [a-z][a-z\-]*)?)', c)
    first = {w.split()[0] for w in words}
    def good(c):
        if '→' in c: return False
        return all(t in words or t.split()[0] in first for t in tagged(c))
    kept = [c for c in parts[1:] if good(c)]
    expl = set()
    for c in kept:
        for t in tagged(c): expl |= {w for w in words if w == t or w.split()[0] == t.split()[0]}
    out = [parts[0].strip()] + kept
    def gg(ws):
        g = [gl(w) for w in ws if gl(w)]
        return '(%s)' % ' · '.join(g) if len(g) == len(ws) else ''
    for p in it['o'][1:]:
        wi = [i for i, (w, c) in enumerate(zip(p, (a, b))) if w != c]; wr = [p[i] for i in wi]
        if all(w in expl and w not in (a, b) for w in wr): continue
        if len(wr) == 1:
            w = wr[0]; out.append('① %s%s는 %s 자리에 맞지 않아요.' % (w, ('(%s)' % gl(w)) if gl(w) else '', '(AB)'[wi[0] * 1 + 0:wi[0] + 1] and ('(A)' if wi[0] == 0 else '(B)')))
        else: out.append('① %s → %s: 두 칸 모두 함정이에요%s.' % (p[0], p[1], gg(p)))
        expl |= set(wr)
    it['tr'] = ' '.join(x for x in out if x)
    it['_grid'] = True
    return True

def post(it):
    """번호가 붙은 뒤: 'X → Y' 짝 설명은 그 짝의 번호 하나로, 앞 '함정 ▶' 중복 제거"""
    if not it.get('_grid'): return it['tr']
    o = it['opts']
    def rep2(m):
        idx = [i for i, p in enumerate(o) if tuple(p) == (m.group(2), m.group(3))]
        return (CIRC[idx[0]] + ' ' if len(idx) == 1 else m.group(1) + ' ') + m.group(2) + ' → ' + m.group(3)
    t = re.sub(r'([①②③④⑤]+) ([A-Za-z][A-Za-z\- ]*?) → ([A-Za-z][A-Za-z\- ]*?)(?=[:(])', rep2, it['tr'])
    return re.sub(r'^함정 ▶\s*', '', t)
