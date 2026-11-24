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

def fix(it, rng, gloss, TR=None, key=None):
    import os
    if os.environ.get("NOGRID"): return False
    """it['o'][0] = 정답 짝. 패턴이 있으면 격자로 바꾸고 True"""
    o = [tuple(p) for p in it['o']]
    if not leak(o): return False
    a, b = o[0]
    onlyA = [p for p in o[1:] if p[0] == a]; onlyB = [p for p in o[1:] if p[1] == b]
    wrongA = [p[0] for p in o[1:] if p[0] != a]; wrongB = [p[1] for p in o[1:] if p[1] != b]
    # a' = 정답 b와 짝지어졌던 틀린 (A)(= 확실히 틀린 말), 없으면 다른 틀린 (A)
    a2 = onlyB[0][0] if onlyB else wrongA[0]
    b2 = onlyA[0][1] if onlyA else wrongB[0]
    if a2 == a or b2 == b: raise SystemExit('grid fail %r' % (o,))
    grid = [(a, b), (a, b2), (a2, b), (a2, b2)]
    rest = [p for p in o[1:] if p not in grid and p[0] not in (a, a2) and p[1] not in (b, b2)]
    za = [p[0] for p in o[1:] if p[0] not in (a, a2)]; zb = [p[1] for p in o[1:] if p[1] not in (b, b2)]
    cands = rest + [(x, y) for x in za for y in zb] + [(x, b2) for x in za] + [(a2, y) for y in zb]
    z = next((c for c in cands if c not in grid and not leak(grid + [c])), None)
    assert z, o
    new = grid[1:] + [z]; rng.shuffle(new)
    it['o'] = [(a, b)] + new
    assert len(set(it['o'])) == 5 and not leak(it['o']), it['o']
    # 해설: 낱말 하나를 설명하는 '① w(뜻)…' 조각만 남기고(빠진 낱말이 섞인 조각·짝 설명 'X → Y' 조각은 지움),
    #       설명이 없는 오답 짝은 '두 칸 모두 함정' 줄을 새로 붙임
    src = TR.pop(key) if (TR is not None and key in TR) else it['tr']
    G = dict(re.findall(r'([A-Za-z][A-Za-z\-]*)\(([^()]*?)\)', src))
    gl = lambda w: G.get(w) or gloss(w) or ''
    words = {w for p in it['o'] for w in p}
    parts = re.split(r' (?=[①②③④⑤]+\s*\(?[A-Za-z])', src)
    def tagged(c): return re.findall(r'[①②③④⑤]+\s*\(?([A-Za-z][A-Za-z\-]*(?: [a-z][a-z\-]*)?)', c)
    def ok(c):
        if '→' in c: return False
        for t in tagged(c):
            if not (t in words or t.split()[0] in {w.split()[0] for w in words}): return False
        return True
    if re.match(r'[①②③④⑤]', parts[0]): parts = [''] + parts      # 머리말 없이 바로 '① …'로 시작
    kept = [c for c in parts[1:] if ok(c)]
    expl = set()
    for c in kept:
        for t in tagged(c):
            expl |= {w for w in words if w == t or w.split()[0] == t.split()[0]}
    out = [parts[0].strip()] + kept
    def gg(ws): 
        g = [gl(w) for w in ws if gl(w)]
        return '(%s)' % ' · '.join(g) if len(g) == len(ws) else ''
    for p in it['o'][1:]:
        wrong = [w for w, c in zip(p, (a, b)) if w != c]
        if p == (a2, b2): out.append('① %s → %s: 두 칸 모두 함정이에요%s.' % (p[0], p[1], gg(p))); continue
        if all(w in expl for w in wrong): continue
        if len(wrong) == 1:
            w = wrong[0]; out.append('① %s%s는 %s 자리에 맞지 않아요.' % (w, ('(%s)' % gl(w)) if gl(w) else '', '(A)' if p[0] == w else '(B)'))
        else: out.append('① %s → %s: 둘 다 근거와 맞지 않아요%s.' % (p[0], p[1], gg(p)))
        expl |= set(wrong)
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
