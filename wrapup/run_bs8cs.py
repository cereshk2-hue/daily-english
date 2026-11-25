# 11/25 발산중 비상(황종배) 8과 실전 문법 CS 간접의문문 1~5차 → m2-visang-hwang-L7 시험 탭 맨 뒤에 덧붙임
# (bs7·bs8 html 원본이 work 폴더에서 사라져 run_bs78로 다시 만들면 기존 시험이 바뀔 수 있음 → 기존 시험 JSON은 그대로 두고 새 시험만 붙임)
# 순서: python3 bs8cs_wu.py (→ /home/claude/work/wrapup에 html·json) → cp 해 와서 → python3 run_bs8cs.py
import json, re, sys, os, shutil
os.chdir('/home/claude/srcrepo/wrapup')
src = open('totests.py', encoding='utf-8').read()
src = src.replace(r"""(.*?)</p>', s)}""", r"""(.*?)</p>', s, re.S)}""")
exec(src[:src.index("F = D + 'h1-mock-2509.js'")]); W = '/home/claude/srcrepo/wrapup/'
import enrich
for k in '12345': enrich.E['bs8cs-' + k] = {int(a): b for a, b in json.load(open('en-bs8cs-%s.json' % k)).items()}
F = D + 'm2-visang-hwang-L7.js'; TMP = '/tmp/vh_tmp.js'; shutil.copy(F, TMP)
O = origin(F)
NEW = [parse('wrapup-bs8cs-%s.html' % k, {'id': 'bs8cs-%s' % k, 'title': '실전 문법 %s차 (간접의문문) CS' % k, 'short': '간접의문문 %s차' % k, 'school': '발산중 · 비상(황종배)', 'minutes': 30, 'pts': 5}, O) for k in '12345']
emit(TMP, NEW)
grab = lambda js: json.loads(re.search(r'/\* WRAPUP-TESTS.*?\*/\nwindow\.PKG\.tests = (.*?);\n/\* /WRAPUP-TESTS \*/', js, re.S).group(1))
new = grab(open(TMP, encoding='utf-8').read())
js = open(F, encoding='utf-8').read()
ids = [t['id'] for t in new]
blk = '/* BS8CS-TESTS: wrapup/run_bs8cs.py 로 만듦 (손으로 고치지 말 것) */\nwindow.PKG.tests = (window.PKG.tests || []).filter(function (t) { return %s.indexOf(t.id) < 0; }).concat(%s);\n/* /BS8CS-TESTS */\n' % (json.dumps(ids), json.dumps(new, ensure_ascii=False))
if '/* BS8CS-TESTS' in js: js = re.sub(r'/\* BS8CS-TESTS.*?/\* /BS8CS-TESTS \*/\n', lambda m: blk, js, flags=re.S)
else: js = js.rstrip('\n') + '\n' + blk
open(F, 'w', encoding='utf-8').write(js)
print('새 시험', ids)
