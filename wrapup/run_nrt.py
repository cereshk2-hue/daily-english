# 11/15 중3 지학사 (+ 7·8과 기출 마무리 1·2회 맨 아래) m3-jihak-min-L7 시험 탭: 7과 실전 변형 1~3회 + 너른터 7과 변형기출 1~4세트 + 너른터 8과 변형기출 1~4세트 (OMR)
import json, re, sys
src = open('/home/claude/srcrepo/wrapup/totests.py', encoding='utf-8').read()
src = src.replace(r"""(.*?)</p>', s)}""", r"""(.*?)</p>', s, re.S)}""")
exec(src[:src.index("F = D + 'h1-mock-2509.js'")])
W = '/home/claude/work/wrapup/'
import enrich
ALL = [('j7', k, '7과 실전 변형 %s회' % k, '%s회' % k) for k in '123'] + \
      [('nrt7', k, '너른터 7과 변형기출 %s세트' % k, '%s세트' % k) for k in '1234'] + \
      [('nrt8', k, '너른터 8과 변형기출 %s세트' % k, '%s세트' % k) for k in '1234'] + \
      [('gch', k, '7·8과 기출 마무리 %s회' % k, '%s회' % k) for k in '12'] + \
      [('k25', '1', '중산중 2025 기출 (2학기 2차 지필)', '2025 기출')]
for p, k, _, _ in ALL: enrich.E['%s-%s' % (p, k)] = {int(a): b for a, b in json.load(open(W + 'en-%s-%s.json' % (p, k))).items()}
F = D + 'm3-jihak-min-L7.js'; O = origin(F)
TS = [parse('wrapup-%s-%s.html' % (p, k), {'id': '%s-%s' % (p, k), 'title': t, 'short': sh, 'school': '중3 지학사', 'minutes': 45 if p == 'k25' else 30, 'pts': 5}, O, **({'nmc': 25} if p == 'k25' else {})) for p, k, t, sh in ALL]
K25 = [3, 3, 3, 3, 4, 3, 4, 5, 4, 3, 4, 4, 3, 4, 5, 4, 5, 5, 5, 5, 3, 5, 4, 5, 4]  # 원본 배점(합 100)
for t in TS:
    if t['id'] == 'k25-1':
        assert len(t['items']) == 25 and sum(K25) == 100
        for it, pt in zip(t['items'], K25): it['pts'] = pt
emit(F, TS)
