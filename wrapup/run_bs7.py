# 11/13 발산중1 비상(황종배) 7과 문법 심화 1~5세트 → m2-visang-hwang-L7(중2 비상 황종배 L7~8 단원) '문법 심화' 탭 (OMR)
import json, re, sys
src = open('/home/claude/srcrepo/wrapup/totests.py', encoding='utf-8').read()
src = src.replace(r"""(.*?)</p>', s)}""", r"""(.*?)</p>', s, re.S)}""")
exec(src[:src.index("F = D + 'h1-mock-2509.js'")])
W = '/home/claude/work/wrapup/'
import enrich
for k in '12345': enrich.E['bs7-' + k] = {int(a): b for a, b in json.load(open(W + 'en-bs7-%s.json' % k)).items()}
F = D + 'm2-visang-hwang-L7.js'; O = origin(F)
emit(F, [parse('wrapup-bs7-%s.html' % k, {'id': 'bs7-' + k, 'title': '7과 문법 심화 %s세트' % k, 'short': '%s세트' % k, 'school': '발산중 · 비상(황종배)', 'minutes': 30, 'pts': 5}, O) for k in '12345'])
