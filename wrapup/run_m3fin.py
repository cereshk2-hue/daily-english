# 11/22 중산중3 7·8과 최종 점검 1·2회 → m3-jihak-min-L7 시험 탭 맨 아래 (기존 WRAPUP-TESTS는 그대로, 따로 FINAL-TESTS 블록)
# 먼저 cd /home/claude/work/wrapup && python3 m3fin_wu.py (wrapup-m3fin-*.html · en-m3fin-*.json)
import json, re, sys
sys.path.insert(0, '/home/claude/srcrepo/wrapup')
src = open('/home/claude/srcrepo/wrapup/totests.py', encoding='utf-8').read()
src = src.replace(r"""(.*?)</p>', s)}""", r"""(.*?)</p>', s, re.S)}""")
exec(src[:src.index("F = D + 'h1-mock-2509.js'")])
W = '/home/claude/work/wrapup/'
import enrich
for k in '12': enrich.E['m3fin-%s' % k] = {int(a): b for a, b in json.load(open(W + 'en-m3fin-%s.json' % k)).items()}
F = D + 'm3-jihak-min-L7.js'; O = origin(F)
TS = [parse('wrapup-m3fin-%s.html' % k, {'id': 'm3fin-%s' % k, 'title': '중산중 7·8과 최종 점검 %s회' % k, 'short': '최종 점검 %s회' % k, 'school': '중3 지학사', 'minutes': 45, 'pts': 5}, O, nmc=25) for k in '12']
for t in TS:
    h = open(W + 'wrapup-%s.html' % t['id'], encoding='utf-8').read()
    P = [int(x) for x in re.findall(r'<span class="pt">\[(\d+)점\]</span>', h)]
    assert len(t['items']) == len(P) == 25 and sum(P) == 100, (len(t['items']), P)
    for it, pt in zip(t['items'], P): it['pts'] = pt
from enrich import E as EN
KD = kodict(F)
for t in TS:
    en = EN.get(t['id'], {})
    for it in t['items']:
        x = en.get(it['n'], {})
        if 'o' in x and len(x['o']) == 5: it['okos'] = x['o']
        it['words'] = x.get('w', [])
        it['kos'] = kos(it, KD)
js = open(F, encoding='utf-8').read()
blk = ('/* FINAL-TESTS: wrapup/run_m3fin.py 로 만듦 (손으로 고치지 말 것) */\nwindow.PKG.tests = (window.PKG.tests || []).filter(function (t) { return !/^m3fin-/.test(t.id); }).concat('
       + json.dumps(TS, ensure_ascii=False) + ');\n/* /FINAL-TESTS */\n')
if '/* FINAL-TESTS' in js: js = re.sub(r'/\* FINAL-TESTS.*?/\* /FINAL-TESTS \*/\n', lambda m: blk, js, flags=re.S)
else: js = js.rstrip('\n') + '\n' + blk
open(F, 'w', encoding='utf-8').write(js)
for t in TS: print(t['id'], len(t['items']), sum(i['pts'] for i in t['items']), ''.join(CIR[i['ans']] for i in t['items']))
