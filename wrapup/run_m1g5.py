# 11/13 (+11/17 실전 문법 m1cs·m1to 1~3차) 중산중1 동아 5과 문법 변형 1·2·3차 → m1-donga-yoon-L6 '문법 변형' 탭 (OMR)
import json, re, sys
src = open('/home/claude/srcrepo/wrapup/totests.py', encoding='utf-8').read()
src = src.replace(r"""(.*?)</p>', s)}""", r"""(.*?)</p>', s, re.S)}""")
exec(src[:src.index("F = D + 'h1-mock-2509.js'")])
W = '/home/claude/work/wrapup/'
import enrich
for P in ('m1g5', 'm1cs', 'm1to'):
  for k in '123': enrich.E[P + '-' + k] = {int(a): b for a, b in json.load(open(W + 'en-%s-%s.json' % (P, k))).items()}
F = D + 'm1-donga-yoon-L6.js'; O = origin(F)
emit(F, [parse('wrapup-m1g5-%s.html' % k, {'id': 'm1g5-' + k, 'title': '5과 문법 변형 %s차' % k, 'short': '%s차' % k, 'school': '중산중 1학년', 'minutes': 30, 'pts': 5}, O) for k in '123'] +
     [parse('wrapup-m1cs-%s.html' % k, {'id': 'm1cs-' + k, 'title': '실전 문법 %s차 (접속사 that)' % k, 'short': 'that %s차' % k, 'school': '중산중 1학년', 'minutes': 30, 'pts': 5}, O) for k in '123'] +
     [parse('wrapup-m1to-%s.html' % k, {'id': 'm1to-' + k, 'title': '실전 문법 %s차 (to부정사)' % k, 'short': 'to부정사 %s차' % k, 'school': '중산중 1학년', 'minutes': 30, 'pts': 5}, O) for k in '123'])
