# 11/13 (+11/17 실전 문법 m1cs·m1to 1~3차, +11/19 비교급·최상급 m1cp 1~3차 CS) 중산중1 동아 5과 문법 변형 1·2·3차 → m1-donga-yoon-L6 '문법 변형' 탭 (OMR)
import json, re, sys
src = open('/home/claude/srcrepo/wrapup/totests.py', encoding='utf-8').read()
src = src.replace(r"""(.*?)</p>', s)}""", r"""(.*?)</p>', s, re.S)}""")
exec(src[:src.index("F = D + 'h1-mock-2509.js'")])
W = '/home/claude/work/wrapup/'
import enrich
for P in ('m1g5', 'm1cs', 'm1to', 'm1cp'):
  for k in '123': enrich.E[P + '-' + k] = {int(a): b for a, b in json.load(open(W + 'en-%s-%s.json' % (P, k))).items()}
F = D + 'm1-donga-yoon-L6.js'; O = origin(F)
CP = [parse('wrapup-m1cp-%s.html' % k, {'id': 'm1cp-' + k, 'title': '실전 문법 %s차 (비교급 · 최상급) CS' % k, 'short': '비교 %s차' % k, 'school': '중산중 1학년', 'minutes': 30, 'pts': 5}, O) for k in '123']
# 11/19 5과 문법 변형(m1g5)과 같은 영어 문장이 실전 문법(m1cp)에 있으면 멈춤
_sn = lambda h: set(re.sub(r'\s+', ' ', x).strip().lower() for x in re.findall(r"[A-Z][^<>.!?\n]{12,}[.!?]", re.sub(r'<[^>]+>', ' ', re.sub(r'(?s)<(style|script)[^>]*>.*?</\1>', '', h))) if not re.search('[가-힣]', x))
_g5 = set().union(*[_sn(open(W + 'wrapup-m1g5-%s.html' % k, encoding='utf-8').read()) for k in '123'])
_cp = set().union(*[_sn(open(W + 'wrapup-m1cp-%s.html' % k, encoding='utf-8').read()) for k in '123'])
assert not (_g5 & _cp), sorted(_g5 & _cp)
emit(F, [parse('wrapup-m1g5-%s.html' % k, {'id': 'm1g5-' + k, 'title': '5과 문법 변형 %s차' % k, 'short': '%s차' % k, 'school': '중산중 1학년', 'minutes': 30, 'pts': 5}, O) for k in '123'] +
     [parse('wrapup-m1cs-%s.html' % k, {'id': 'm1cs-' + k, 'title': '실전 문법 %s차 (접속사 that)' % k, 'short': 'that %s차' % k, 'school': '중산중 1학년', 'minutes': 30, 'pts': 5}, O) for k in '123'] +
     [parse('wrapup-m1to-%s.html' % k, {'id': 'm1to-' + k, 'title': '실전 문법 %s차 (to부정사)' % k, 'short': 'to부정사 %s차' % k, 'school': '중산중 1학년', 'minutes': 30, 'pts': 5}, O) for k in '123'] + CP)
