# 11/21 대진고2 · 2026년 10월 고2 학평 요약문 끝판왕 1~10 — 20·21 / 22·23 / 24·26 / 29·30 / 31·32 / 33·34 / 35·36 / 37·38 / 39·40 / 41~42
# 문항: boss6_a.py(1~5) · boss6_b.py(6~10), 공통 boss6_core.py. 형식은 끝판왕(boss5_data)과 같음
import boss6_a, boss6_b
from boss6_core import P
SETS = boss6_a.SETS + boss6_b.SETS
exec(open('/home/claude/srcrepo/wrapup/boss6_s3.py', encoding='utf-8').read())   # 11/24 26번 제외 → 세트 3 = 24번 20문항(고정 규칙 어휘)
exec(open('/home/claude/srcrepo/wrapup/boss6_hard.py', encoding='utf-8').read())   # 11/25 1·2·4~10세트 어휘 끝판왕화 (선생님: 고2인 만큼 난이도 확실히)
CTX = {'hard': False}
TR = {}
import boss2_data as _b2
MEAN = {}
for f in ('bossjd_mean.txt', 'boss5_mean.txt', 'boss6_mean.txt'):
    try: MEAN.update(dict(x.split(':', 1) for x in open('/home/claude/srcrepo/wrapup/' + f, encoding='utf-8').read().strip().split('|') if ':' in x))
    except FileNotFoundError: pass
    if f == 'bossjd_mean.txt': MEAN.update(_b2.MEAN)
EXTRA = {}
def M(w): return (HMEAN3.get(w) if CTX['hard'] else None) or MEAN.get(w, '')
MEAN.update({_k: _v for _k, _v in HMEAN3.items() if _k not in MEAN})
MISSING = sorted({w for _S in SETS for _it in _S['items'] for _p in _it.get('o', []) for w in _p if w not in MEAN})
