# 11/20 심학중1 천재(소영순) 실전 문법 CS — 동명사 1~4차 (m1cg_wu.py) → m1-chunjae-so-L6 tests 맨 뒤 (여러 번 돌려도 같음)
# build_m1c4.py 끝(add_m1cs.py 다음)에서 자동 실행. 단독 실행도 됨
import json, re
_src = open('/home/claude/srcrepo/wrapup/totests.py', encoding='utf-8').read()
_src = _src.replace(r"""(.*?)</p>', s)}""", r"""(.*?)</p>', s, re.S)}""")
_g = {'__name__': 'add_m1cg'}; exec(_src[:_src.index("F = D + 'h1-mock-2509.js'")], _g)
import sys; sys.path.insert(0, '/home/claude/srcrepo/wrapup')
import enrich
W = '/home/claude/work/wrapup/'
_g['W'] = W; _g['enrich'] = enrich
CG = [('m1cg', k, '실전 문법 %s차 (동명사) CS' % k, '동명사 %s차' % k) for k in '1234']
for p, k, _, _ in CG: enrich.E['%s-%s' % (p, k)] = {int(a): b for a, b in json.load(open(W + 'en-%s-%s.json' % (p, k))).items()}
DST = _g['D'] + 'm1-chunjae-so-L6.js'; O = _g['origin'](DST)
NEW = [_g['parse']('wrapup-%s-%s.html' % (p, k), {'id': '%s-%s' % (p, k), 'title': t, 'short': sh, 'school': '심학중 1학년', 'minutes': 30, 'pts': 5}, O) for p, k, t, sh in CG]
KD = _g['kodict'](DST)
for t in NEW:  # totests.emit 의 선택지·단어·해석 붙이기를 새 시험에만 (기존 시험은 그대로)
    en = enrich.E.get(t['id'], {})
    for it in t['items']:
        x = en.get(it['n'], {})
        if 'o' in x: it['okos'] = x['o']
        it['words'] = x.get('w', [])
        it['kos'] = _g['kos'](it, KD)
    assert sum(i['pts'] for i in t['items']) == 100
js = open(DST, encoding='utf-8').read()
m = re.search(r'window\.PKG\.tests = (.*?);\n/\* /WRAPUP-TESTS \*/', js, re.S)
tests = [t for t in json.loads(m.group(1)) if not t['id'].startswith('m1cg-')] + NEW
js = js[:m.start(1)] + json.dumps(tests, ensure_ascii=False) + js[m.end(1):]
open(DST, 'w', encoding='utf-8').write(js)
print('m1-chunjae-so-L6 tests:', [(t['id'], t['short']) for t in tests])
