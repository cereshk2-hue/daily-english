# 11/16 발산중 비상(황종배) 문법 심화: 7과 1~5세트 + 8과 1~5세트 + (11/25) 8과 실전 문법 CS 간접의문문 1~5차 → m2-visang-hwang-L7 시험 탭 (OMR). (emit은 시험 칸을 통째로 덮으니 항상 모두 넣음)
# 11/25: html·en json은 srcrepo/wrapup 것을 씀(work/wrapup 비어 있음). bs8cs는 bs8cs_wu.py로 만든 뒤 여기로 복사
import json, re, sys, os
os.chdir('/home/claude/srcrepo/wrapup')
src = open('/home/claude/srcrepo/wrapup/totests.py', encoding='utf-8').read()
src = src.replace(r"""(.*?)</p>', s)}""", r"""(.*?)</p>', s, re.S)}""")
exec(src[:src.index("F = D + 'h1-mock-2509.js'")])
W = '/home/claude/srcrepo/wrapup/'
import enrich
for p in ['bs7-%s' % k for k in '12345'] + ['bs8-%s' % k for k in '12345'] + ['bs8cs-%s' % k for k in '12345']:
    enrich.E[p] = {int(a): b for a, b in json.load(open(W + 'en-%s.json' % p)).items()}
F = D + 'm2-visang-hwang-L7.js'; O = origin(F)
T = [parse('wrapup-bs%s-%s.html' % (L, k), {'id': 'bs%s-%s' % (L, k), 'title': '%s과 문법 심화 %s세트' % (L, k), 'short': '%s과 %s세트' % (L, k) if L == '8' else '%s세트' % k, 'school': '발산중 · 비상(황종배)', 'minutes': 30, 'pts': 5}, O) for L in '78' for k in '12345']
T += [parse('wrapup-bs8cs-%s.html' % k, {'id': 'bs8cs-%s' % k, 'title': '실전 문법 %s차 (간접의문문) CS' % k, 'short': '간접의문문 %s차' % k, 'school': '발산중 · 비상(황종배)', 'minutes': 30, 'pts': 5}, O) for k in '12345']
emit(F, T)
