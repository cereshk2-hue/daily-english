# 11/12 안곡고2 Wrap-up 3세트 → 앱 (WRAPUP 블록을 끝판왕 BOSS 블록 앞에 둠)
import json, re, sys
src = open('/home/claude/srcrepo/wrapup/totests.py', encoding='utf-8').read()
src = src.replace(r"""(.*?)</p>', s)}""", r"""(.*?)</p>', s, re.S)}""")
exec(src[:src.index("F = D + 'h1-mock-2509.js'")])
W = '/home/claude/work/wrapup/'
import enrich
TS = [('2429', '24·29번'), ('3034', '30·34번'), ('3842', '38·41~42번')]
for tid, sh in TS: enrich.E['ag2609-' + tid] = {int(k): v for k, v in json.load(open(W + 'en-ag-%s.json' % tid)).items()}
F = D + 'h2-mock-2609-angok.js'
js = open(F, encoding='utf-8').read()
m = re.search(r'/\* BOSS-TESTS.*?/\* /BOSS-TESTS \*/\n', js, re.S); boss = m.group(0) if m else ''
open(F, 'w', encoding='utf-8').write(js.replace(boss, ''))
O = origin(F)
new = [parse('wrapup-ag2609-%s.html' % tid, {'id': 'ag2609-' + tid, 'title': '9월 학평 %s Wrap-up' % sh, 'short': sh, 'school': '안곡고 2학년', 'minutes': 30, 'pts': 5}, O) for tid, sh in TS]
emit(F, new)
open(F, 'a', encoding='utf-8').write(boss)
