# 11/12 중산고2 Wrap-up 4세트 → 앱 (모고: WRAPUP 블록을 끝판왕 BOSS 블록 앞에 둠)
import json, re, sys
src = open('/home/claude/srcrepo/wrapup/totests.py', encoding='utf-8').read()
src = src.replace(r"""(.*?)</p>', s)}""", r"""(.*?)</p>', s, re.S)}""")
exec(src[:src.index("F = D + 'h1-mock-2509.js'")])
W = '/home/claude/work/wrapup/'
import enrich
TS = [('1922', '19~22번'), ('2327', '23·24·26·27번'), ('2930', '29·30번')]
for tid, sh in TS: enrich.E['js2609-' + tid] = {int(k): v for k, v in json.load(open(W + 'en-js2609-%s.json' % tid)).items()}
enrich.E['js2-mirae-l4'] = {int(k): v for k, v in json.load(open(W + 'en-js2-mirae-L4.json')).items()}
F = D + 'h2-mock-2609-jungsan.js'
js = open(F, encoding='utf-8').read()
m = re.search(r'/\* BOSS-TESTS.*?/\* /BOSS-TESTS \*/\n', js, re.S); boss = m.group(0) if m else ''
assert boss
open(F, 'w', encoding='utf-8').write(js.replace(boss, ''))
O = origin(F)
new = [parse('wrapup-js2609-%s.html' % tid, {'id': 'js2609-' + tid, 'title': '9월 학평 %s Wrap-up' % sh, 'short': sh, 'school': '중산고 2학년', 'minutes': 30, 'pts': 5}, O) for tid, sh in TS]
emit(F, new)
open(F, 'a', encoding='utf-8').write(boss)
F = D + 'h2-mirae-kim-L4.js'; O = origin(F)
emit(F, [parse('wrapup-js2-mirae-L4.html', {'id': 'js2-mirae-l4', 'title': '4과 본문 Wrap-up', 'short': '본문 ❶~❽', 'school': '중산고 2학년', 'minutes': 30, 'pts': 5}, O)])
