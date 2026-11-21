# 11/21 대진고2 · 2026년 10월 고2 학평 요약문 끝판왕 1~10 공통 (boss5_data.py와 같은 형식)
import sys, json, re, subprocess
sys.path.insert(0, '/home/claude/srcrepo/wrapup')
from boss2_data import mc, wr
ATS = [0, 3, 1, 4, 2, 0, 3, 1, 2, 4, 1, 0, 3, 2, 4, 1, 0, 2]
ATS2 = [2, 4, 0, 3, 1, 4, 0, 2, 3, 1, 3, 4, 0, 1, 2, 0, 3, 1]
def rot(k, T=None): return [(a + k) % 5 for a in (T or ATS)]
_PK = json.loads(subprocess.check_output(['node', '-e', "global.window={};require('/home/claude/proj/data/h2-ne-oh-L3.js');process.stdout.write(JSON.stringify(window.PKG))"]))
P = {}
for d in _PK['days']:
    if not re.match(r'q\d+$', d['id']): continue
    cur = None
    for l in d['passage']:
        if l[0] == '#':
            mm = re.match(r'(\d+(?:~\d+)?)번', l[1]); cur = mm.group(1) if mm else None; P.setdefault(cur, [])
        elif cur: P[cur].append(l[1])
P = {k: ' '.join(v).replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"') for k, v in P.items()}
B2 = lambda a, b: [{'label': '(A)', 'pts': 3, 'ans': a, 'chk': []}, {'label': '(B)', 'pts': 3, 'ans': b, 'chk': []}]
X = '근거가 없어요.'
class Maker:
    def __init__(s, A): s.A = A
    def __call__(s, lv, sent, o, k, ko, gr, r2, r3, gm=''):
        tr = '① %s%s ① %s%s ① %s → %s, ① %s → %s: %s' % (o[1][1], r2, o[2][0], r3, o[3][0], o[3][1], o[4][0], o[4][1], X)
        return mc(lv, sent, o, s.A[k], ko, gr, tr, gm=gm)
