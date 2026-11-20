# 11/18 중산중2 동아(윤정미) m2-donga-yoon-L7 시험 탭(너른터 실전): 7과 1~9회(m2d7/build_m2d7.py, 11/11) + 8과 1~9회(nrtd8_wu.py)
# 11/20 + 실전 문법 가주어 it 1~3차(m2it_wu.py)
# ★ emit은 시험 블록을 통째로 덮어씀 → 이 단원은 build_m2d7.py 단독으로 돌리지 말고 이 파일로 둘 다 함께 emit
import json, re, sys
src = open('/home/claude/srcrepo/wrapup/totests.py', encoding='utf-8').read()
src = src.replace(r"""(.*?)</p>', s)}""", r"""(.*?)</p>', s, re.S)}""")
exec(src[:src.index("F = D + 'h1-mock-2509.js'")])
W = '/home/claude/work/wrapup/'
import enrich
ALL = [('nrtd8', str(k), '너른터 실전 8과 %d회' % k, '8과 %d회' % k) for k in range(1, 10)]
IT = [('m2it', k, '실전 문법 %s차 (가주어 it · 진주어)' % k, '가주어 %s차' % k) for k in '123']
for p, k, _, _ in ALL + IT: enrich.E['%s-%s' % (p, k)] = {int(a): b for a, b in json.load(open(W + 'en-%s-%s.json' % (p, k))).items()}
F = D + 'm2-donga-yoon-L7.js'; O = origin(F)
TS = [parse('wrapup-%s-%s.html' % (p, k), {'id': '%s-%s' % (p, k), 'title': t, 'short': sh, 'school': '중2 동아', 'minutes': 30, 'pts': 5}, O) for p, k, t, sh in ALL]
b = open('/home/claude/srcrepo/wrapup/m2d7/build_m2d7.py', encoding='utf-8').read().replace('emit(F, tests)', '')
g = {'__name__': 'm2d7'}; exec(b, g)
M2D7 = g['tests']; assert len(M2D7) == 9 and all(t['title'].startswith('너른터 실전 7과') for t in M2D7)
TI = [parse('wrapup-%s-%s.html' % (p, k), {'id': '%s-%s' % (p, k), 'title': t, 'short': sh, 'school': '중2 동아', 'minutes': 30, 'pts': 5}, O) for p, k, t, sh in IT]
emit(F, M2D7 + TS + TI)
