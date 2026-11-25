# 11/25 심학중1 천재(소영순) 실전기출: 2025 2학기 기말(루원·공주여·권선·석우·천생) + 2026 2학기 중간(창포·청람·고덕·신흥·천생·명일) → 4·5·6과 문항만 25문항씩 (m1-chunjae-so-L6, kind 'exam', /* M1CX-TESTS */)
# 7과·서술형·그림 필요·정답 둘/애매 문항 제외. 오타·정답 오류는 고쳐 넣고 '확인 ▶'에 적음
import json, re, html, sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(HERE, 'ex.py'), encoding='utf-8').read())
SRC = '/home/claude/work/m1cx/src/items.json'
DATA = '/home/claude/proj/data/m1-chunjae-so-L6.js'
RAW = json.load(open(SRC))
LAB = {'16b2f511': '2025 2학기 기말', '345324d9': '2025 2학기 기말', 'af97c04a': '2025 2학기 기말', 'ff349c4c': '2025 2학기 기말', 'ff7704dc': '2025 2학기 기말'}
C = '①②③④⑤'
EXCL = {201: 'ⓘ All summer long을 "긴 여름 동안"으로 본 것을 틀렸다고 해야 정답(5개)이 됨 → 논쟁 소지', 262: '석우중 34번과 같은 대화·같은 정답(중복)', 3: '외부 지문(신데렐라)', 54: '틀린 것은 ⓑⓒⓔ인데 맞는 선택지가 없음(원본 오류)', 59: '그림', 106: '모두 고르기', 111: '모두 고르기', 116: '모두 고르기',
        194: '서술형', 196: '정답 둘(T/F)', 204: '서술형', 209: '서술형', 210: '그림', 211: '그림', 212: '서술형', 213: '서술형'}
FIX_TXT = {49: [("How I'm worried", "Now I'm worried")], 47: [("El'’s", "El's")], 146: [('Scra', 'Sera')], 153: [('plaant', 'plant')],
           102: [('at the time.Plant.', 'at the time.')], 64: [('(라) – (B) – (나)', '(라) – (다) – (나)')], 110: [('net spicy', 'not spicy')], 117: [('tired? hot', 'tired?')],
           224: [('할미니', '할머니'), ('EI', 'El')], 78: [('thetide', 'the tide')]}
FIX_ANS = {227: (2, '원본 정답 ②는 오류: ⓐ·ⓑ·ⓓ·ⓔ는 모두 El이 받은 작은 화분(과꽃), ⓒ all the plants만 다른 친구들이 가져간 꽃들 → ③'),
           232: (3, '원본 정답 ②는 오류: soil(토양, 흙)은 맞는 풀이. Thanks to는 "~ 덕분에"이므로 "~에도 불구하고"가 어색 → ④'),
           273: (2, '원본 정답 ⑤는 오류: luckyer → luckier가 맞음. ③ My brother runs more slowly than I.가 옳은 문장')}
NOTE = {49: '원본 오타 How → Now', 146: '원본 오타 Scra → Sera(이름)', 110: '원본 오타 net → not', 224: '원본 오타(할미니·EI) 고쳐 실음', 102: '원본 끝에 정답(Plant.)이 새어 있어 지움', 53: '같은 지문의 어법 문제(오류로 제외)에 쓰인 틀린 철자(visitted·enjoied·eaten)를 바르게 고쳐 실음', 64: '원본 선택지 ④ 오타 (B) → (다)'}
LES = {66: '4·5과', 226: '5과'}
def T(rows):
    h = '<table class="gt" style="border-collapse:collapse;margin:4px 0">'
    for k, r in enumerate(rows):
        tag = 'th' if k == 0 else 'td'
        h += '<tr>' + ''.join('<%s style="border:1px solid #888;padding:2px 6px">%s</%s>' % (tag, html.escape(c), tag) for c in r) + '</tr>'
    return h + '</table>'
TBL = {67: T([['Students', 'English', 'Math'], ['Amy', '95', '90'], ['Brian', '88', '90'], ['Cindy', '88', '88']])}
def H(s): return re.sub(r'[ ]*\t+[ ]*', ' &nbsp;&nbsp; ', html.escape(s)).replace('\n', '<br>').replace('', '<u>').replace('', '</u>')
def school(o):
    s = o['school'].replace('학교', '')
    return s
items = []
for i, o in enumerate(RAW):
    t = o['tag'] or ''
    if t.startswith('7') or not o['ans'] or i in EXCL: continue
    if not o['opts'] or len(o['opts']) != 5: continue
    assert len(o['ans']) == 1, i
    les = LES.get(i) or t
    assert les in ('4과', '5과', '6과', '4·5과'), (i, t)
    body = o['body']; opts = list(o['opts']); g = o['group']['text'] if o['group'] else None
    for a, b in FIX_TXT.get(i, []):
        hit = False
        if a in body: body = body.replace(a, b); hit = True
        o2 = [x.replace(a, b) for x in opts]
        if o2 != opts: opts = o2; hit = True
        if g and a in g: g = g.replace(a, b); hit = True
        assert hit, (i, a)
    if i == 53: g = re.sub(r'[ⓐ-ⓖ]', '', g).replace('\ue000', '').replace('\ue001', '').replace('visitted', 'visited').replace('enjoied', 'enjoyed').replace('eaten', 'ate')
    ans = C.index(o['ans'][0]); note = NOTE.get(i, '')
    if i in FIX_ANS: ans, note = FIX_ANS[i]
    assert all(x.strip() for x in opts), (i, opts)
    gh = o['group']['head'] if o['group'] else ''
    items.append({'i': i, 'lab': LAB.get(o['file'][:8], '2026 2학기 중간'), 'school': school(o), 'lesson': les,
                  'gkey': (o['file'], gh, g[:80]) if g else None, 'stem': re.sub(r'\s*\[[^\]]*\]\s*$', '', o['stem']),
                  'body': TBL[i] if i in TBL else H(body), 'ghtml': H(g) if g else None, 'ghead': re.sub(r'\s*\[[^\]]*\]\s*$', '', gh).replace('Read the following and answer.', '다음 글을 읽고 물음에 답하시오.'),
                  'opts': [H(x.strip()) for x in opts], 'ans': ans, 'note': note})
units = []
for it in items:
    if it['gkey'] and units and units[-1][0]['gkey'] == it['gkey']: units[-1].append(it)
    else: units.append([it])
order = {'4과': 0, '4·5과': 1, '5과': 2, '6과': 3}
# 실전처럼 회마다 4·5·6과가 섞이도록: 과별로 묶음을 나눠 담고(큰 묶음 먼저), 회 안에서는 4→5→6과 순서
N = len(items); NS = (N + 24) // 25; CAP = [25] * (NS - 1) + [N - 25 * (NS - 1)]
sets = [[] for _ in range(NS)]; cnt = [0] * NS
for L in sorted(order, key=order.get):
    us = sorted([u for u in units if u[0]['lesson'] == L], key=lambda u: (-len(u), u[0]['i']))
    tot = sum(len(u) for u in us); have = [0] * NS
    for u in us:
        cand = [k for k in range(NS) if cnt[k] + len(u) <= CAP[k]]
        assert cand, ('pack fail', L)
        k = min(cand, key=lambda k: (have[k] / CAP[k] - tot / N, -(CAP[k] - cnt[k]), k))
        sets[k].append(u); cnt[k] += len(u); have[k] += len(u)
assert cnt == CAP, (cnt, CAP)
for S in sets: S.sort(key=lambda u: (order[u[0]['lesson']], u[0]['i']))
print('items', len(items), 'sets', [sum(len(u) for u in s) for s in sets])
if 'list' in sys.argv:
    for it in items: print(it['i'], it['school'], it['lesson'], C[it['ans']], it['stem'][:40], '' if it['i'] in EX else 'NOEX')
def test(no, S):
    its = []; n = 0; total = sum(len(u) for u in S)
    base = 100 // total; pts = [base] * total
    for j in range(100 - base * total): pts[-1 - j] += 1
    for u in S:
        for j, it in enumerate(u):
            n += 1; body = it['body']
            if it['ghtml'] and j == 0:
                rng = '[%d~%d] ' % (n, n + len(u) - 1) if len(u) > 1 else ''
                body = '<div class="wbox"><p><b>%s%s</b></p><p>%s</p></div>' % (rng, html.escape(it['ghead']), it['ghtml']) + (('<div>' + body + '</div>') if body.strip() else '')
            elif body.strip(): body = '<div class="wbox"><p>%s</p></div>' % body
            k = 'c%d' % it['i']
            if os.environ.get('NOEX'): EX.setdefault(k, '-')
            assert k in EX, k
            ex = '정답 ▶ %s\n%s\n출처 ▶ %s %s · %s' % (C[it['ans']], EX[k], it['school'], it['lab'], it['lesson'])
            if it['note']: ex += '\n확인 ▶ ' + it['note']
            its.append({'n': n, 'src': '%s · %s' % (it['school'], it['lesson']), 'stem': html.escape(it['stem']).replace('않은', '<u>않은</u>').replace('없는', '<u>없는</u>').replace('어색한', '<u>어색한</u>').replace('다른', '<u>다른</u>'),
                        'body': body, 'opts': it['opts'], 'en': True, 'ans': it['ans'], 'ex': ex, 'ctx': '', 'pts': pts[n - 1], 'words': [], 'kos': []})
    return {'id': 'm1cx-%d' % no, 'kind': 'exam', 'title': '천재(소영순) 실전기출 %d회 (2025·2026 다른 학교 4·5·6과)' % no, 'short': '실전기출 %d회' % no,
            'school': '심학중 1학년', 'minutes': 45, 'items': its}
if 'list' not in sys.argv:
    TESTS = [test(k + 1, S) for k, S in enumerate(sets)]
    for t in TESTS:
        assert sum(x['pts'] for x in t['items']) == 100
        print(t['id'], len(t['items']), ''.join(C[x['ans']] for x in t['items']), sorted({x['src'].split(' · ')[1] for x in t['items']}))
    if 'emit' in sys.argv:
        ids = [t['id'] for t in TESTS]
        blk = ('/* M1CX-TESTS: gen/m1cx/build.py 로 만듦 (손으로 고치지 말 것) */\nwindow.PKG.tests = (window.PKG.tests || []).filter(function (t) { return %s.indexOf(t.id) < 0; }).concat(%s);\n/* /M1CX-TESTS */\n'
               % (json.dumps(ids), json.dumps(TESTS, ensure_ascii=False)))
        js = open(DATA, encoding='utf-8').read()
        if '/* M1CX-TESTS' in js: js = re.sub(r'/\* M1CX-TESTS.*?/\* /M1CX-TESTS \*/\n', lambda m: blk, js, flags=re.S)
        else: js = js.rstrip('\n') + '\n\n' + blk
        open(DATA, 'w', encoding='utf-8').write(js); print('emit', ids)
