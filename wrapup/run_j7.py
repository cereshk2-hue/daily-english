# 11/13 중3 지학사 7과 실전 변형 1~3회 → m3-jihak-min-L7 '실전 변형' 탭 (OMR)
import json, re, sys
src = open('/home/claude/srcrepo/wrapup/totests.py', encoding='utf-8').read()
src = src.replace(r"""(.*?)</p>', s)}""", r"""(.*?)</p>', s, re.S)}""")
exec(src[:src.index("F = D + 'h1-mock-2509.js'")])
W = '/home/claude/work/wrapup/'
import enrich
for k in '123': enrich.E['j7-' + k] = {int(a): b for a, b in json.load(open(W + 'en-j7-%s.json' % k)).items()}
F = D + 'm3-jihak-min-L7.js'; O = origin(F)
emit(F, [parse('wrapup-j7-%s.html' % k, {'id': 'j7-' + k, 'title': '7과 실전 변형 %s회' % k, 'short': '%s회' % k, 'school': '중3 지학사', 'minutes': 30, 'pts': 5}, O) for k in '123'])
