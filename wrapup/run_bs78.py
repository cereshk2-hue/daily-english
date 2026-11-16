# 11/16 발산중 비상(황종배) 문법 심화: 7과 1~5세트 + 8과 1~5세트 → m2-visang-hwang-L7 '문법 심화' 탭 (OMR). (emit은 시험 칸을 통째로 덮으니 항상 둘 다 넣음)
import json, re, sys
src = open('/home/claude/srcrepo/wrapup/totests.py', encoding='utf-8').read()
src = src.replace(r"""(.*?)</p>', s)}""", r"""(.*?)</p>', s, re.S)}""")
exec(src[:src.index("F = D + 'h1-mock-2509.js'")])
W = '/home/claude/work/wrapup/'
import enrich
for L in '78':
    for k in '12345': enrich.E['bs%s-%s' % (L, k)] = {int(a): b for a, b in json.load(open(W + 'en-bs%s-%s.json' % (L, k))).items()}
F = D + 'm2-visang-hwang-L7.js'; O = origin(F)
emit(F, [parse('wrapup-bs%s-%s.html' % (L, k), {'id': 'bs%s-%s' % (L, k), 'title': '%s과 문법 심화 %s세트' % (L, k), 'short': '%s과 %s세트' % (L, k) if L == '8' else '%s세트' % k, 'school': '발산중 · 비상(황종배)', 'minutes': 30, 'pts': 5}, O) for L in '78' for k in '12345'])
