# 11/13 중산중1 동아 5과 문법 변형 1·2·3차 → m1-donga-yoon-L6 '문법 변형' 탭 (OMR)
import json, re, sys
src = open('/home/claude/srcrepo/wrapup/totests.py', encoding='utf-8').read()
src = src.replace(r"""(.*?)</p>', s)}""", r"""(.*?)</p>', s, re.S)}""")
exec(src[:src.index("F = D + 'h1-mock-2509.js'")])
W = '/home/claude/work/wrapup/'
import enrich
for k in '123': enrich.E['m1g5-' + k] = {int(a): b for a, b in json.load(open(W + 'en-m1g5-%s.json' % k)).items()}
F = D + 'm1-donga-yoon-L6.js'; O = origin(F)
emit(F, [parse('wrapup-m1g5-%s.html' % k, {'id': 'm1g5-' + k, 'title': '5과 문법 변형 %s차' % k, 'short': '%s차' % k, 'school': '중산중 1학년', 'minutes': 30, 'pts': 5}, O) for k in '123'])
