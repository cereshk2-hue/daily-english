# 11/24 중산중1 동아(윤정미) 2026 2학기 중간 기출(7개교: 해원·지산·삼성·남인천여·사하·연화·부산수영) → 25문항씩 OMR (m1-donga-yoon-L6, /* M1GC-TESTS */)
# 범위 5·6(·7)과 → [4과] 문항 제외. 그림·표지판·색 표 등 이미지가 필요한 문항, 정답이 둘이거나 근거가 애매한 문항 제외. 오타·정답 오류는 고쳐 넣고 해설에 적음
import json, re, html, sys
SRC = [('a', '/home/claude/work/m1gc/', '2026 2학기 중간'), ('b', '/home/claude/work/m1gc25/', '2025 2학기 기말')]
DATA = '/home/claude/proj/data/m1-donga-yoon-L6.js'
D = [(p + str(i), o, lab) for p, w, lab in SRC for i, o in enumerate(json.load(open(w + 'items.json')))]
C = '①②③④⑤'
EXCL_B = {'b0': '단어 퍼즐(★칸) 그림', 'b23': '빈칸 문장이 깨짐(must no)', 'b25': '그림', 'b26': '그림', 'b107': '그림', 'b111': '그림', 'b88': '지문 없음',
          'b121': '"Hojin은 작곡에 재능이 있다"를 맞게 보면 5개 → 원본 정답(4개)과 어긋남', 'b140': 'some day·one day 둘 다 가능(정답 둘)', 'b146': '보기 ② 문장이 깨짐', 'b171': '중복(b127과 거의 같음)', 'b174': '중복(해원중 플로깅 배열과 같음)', 'b137': '중복(구남중 영영풀이와 같음)'}
EXCL = {'a24': '가로세로 퍼즐 그림', 'a32': '표지판 그림', 'a50': '표지판 그림', 'a51': '기차 색 표(그림)', 'a54': '그림 묘사', 'a58': '용의자 그림 표', 'a75': '표지판 그림', 'a123': '표지판 그림',
        'a142': '그림 묘사', 'a138': 'T/F 표 체크 위치가 원본에서 깨짐', 'a37': 'ⓕ(경비원이 남자를 봤는지) 본문에 근거 없음 → 정답 애매', 'a70': '③(Camila가 영어를 하는지)도 답할 수 없어 정답 둘',
        'a149': '빈칸에 못 들어가는 말이 여럿(정답 여럿)', 'a167': '빈칸에 안 맞는 말이 share·reduce 둘(원본 정답 waste는 들어감)',
        'a150': '4과', 'a152': '4과', 'a156': '4과', 'a158': '4과', 'a159': '4과', 'a161': '4과', 'a162': '4과'}
FIX_TXT = {'a47': [('There\'s ho food', 'There\'s no food')], 'a61': [('te be guilty', 'to be guilty')], 'a121': [('The leave turned', 'The leaves turned')],
           'a140': [('the closet store', 'the closest store')], 'a134': [('ⓔ\ue000the bag looks perfect\ue001', 'ⓔ\ue000the bag looks perfectly\ue001')]}
FIX_GRP = {'a69': [('you can find ideas for ⓔ\ue000leftovers\ue001 on the internet. (E) great cooking', 'you can find great cooking ideas for ⓔ\ue000leftovers\ue001 on the internet. (E)')],
           'a151': [('   (A) → (B) → (C) → (D)', '   ( ? )')]}
FIX_ANS = {'a141': (1, '원본 정답 ④(ⓑ,ⓒ,ⓓ)는 ⓒ "I heard it the art museum ~"이 틀린 문장이라 오류 → ⓑ,ⓓ ②'),
           'a151': (0, '원본 정답 ④는 오류. Excuse me? → ⓓ 뜻 설명 → ⓑ Sounds cool → ⓒ 매주 토요일 → ⓐ 생각해 볼게 → ⓔ 쓰레기봉투 부탁 → Sure ①'),
           'a157': (1, '원본 정답 ③(We are do ~)은 틀린 문장 → ② Tom and Jenny are running in the gym.이 옳음')}
NOTE = {'a134': '원본은 ⓓ·ⓔ 둘 다 옳은 표현이라 정답이 둘 → ⓔ를 looks perfectly(틀림)로 바꿔 정답 하나로', 'a140': '원본 오타 closet → closest로 고쳐 실음', 'a47': '원본 오타 ho → no', 'a61': '원본 오타 te → to', 'a121': '원본 오타 leave → leaves', 'a69': '지문 끝 깨진 부분(great cooking)을 원문대로 고침'}
def T(rows, head=True):
    h = '<table class="gt" style="border-collapse:collapse;margin:4px 0">'
    for k, r in enumerate(rows):
        tag = 'th' if head and k == 0 else 'td'
        h += '<tr>' + ''.join('<%s style="border:1px solid #888;padding:2px 6px">%s</%s>' % (tag, html.escape(c), tag) for c in r) + '</tr>'
    return h + '</table>'
TBL = {'a36': T([['', 'Eric', 'Kevin', 'Alex', 'Peter'], ['Height', '182 cm', '176 cm', '173 cm', '166 cm'], ['Hair', 'long, brown', 'long, black', 'long, brown', 'short, brown'], ['Language', 'Spanish', 'Spanish', 'English', 'English'], ['Eyes', 'green', 'black', 'blue', 'blue']]),
       'a76': T([['Name', 'Ping', 'Rex', 'Viki'], ['Speed', '9 km/h', '7 km/h', '6 km/h'], ['Height', '30 cm tall', '60 cm tall', '50 cm tall'], ['Price', '$100', '$150', '$200']]),
       'a102': 'The person was taller than 170cm.<br>He had long brown hair.<br>He spoke only English.<br>He had blue eyes.' + T([['Suspect', 'Height', 'Hair', 'Languages', 'Eyes'], ['A', '176cm', 'black', 'Spanish, English', 'brown'], ['B', '173cm', 'brown', 'English', 'blue'], ['C', '182cm', 'brown', 'English', 'green'], ['D', '166cm', 'gray', 'Spanish', 'blue']]),
       'a108': T([['Student', 'Reading Time'], ['Mina', '20 minutes'], ['Tom', '35 minutes'], ['Suji', '50 minutes']]) + '→ Suji reads ________________ of the three students.',
       'a133': T([['Animal', 'Weight', 'Speed', 'Age'], ['Cat', '4kg', '20km/h', '8 years old'], ['Dog', '15kg', '30km/h', '2 years old'], ['Horse', '400kg', '60km/h', '4 years old']]),
       'a165': '&lt;Three New Smartphones&gt;' + T([['', 'Price', 'Battery Life', 'Weight'], ['A', '$1500', '10 Hours', '180g'], ['B', '$1700', '15 Hours', '200g'], ['C', '$1600', '12 Hours', '170g']])}
GTBL = {'a163': '&lt;About Tim&gt;' + T([['Profile', ''], ['Age', '14'], ['School', 'Busan Middle School'], ['Favorite subject', 'English'], ['Hobby', 'to play the guitar'], ['Favorite food', 'pizza']])
        + T([['Schedule', ''], ['7:00', 'get up'], ['8:00', 'go to school'], ['12:30', 'have lunch'], ['4:00', 'play the guitar'], ['7:00', 'do his homework']])}
GTBL['a164'] = GTBL['a163']
def H(s): return re.sub(r'[ ]*\t+[ ]*', ' &nbsp;&nbsp; ', html.escape(s)).replace('\n', '<br>').replace('\ue000', '<u>').replace('\ue001', '</u>')
def lesson(o):
    t = o['tag'] or '5,6과'
    return {'5과': '5과', '6과': '6과', '7과': '7과'}.get(t, '6·7과' if '7' in t else '5·6과')
EXCL.update(EXCL_B)
FIX_TXT.update({'b9': [("I'rn Peter", "I'm Peter")], 'b5': [('히루:', '리우:')], 'b33': [('vore a wig', 'wore a wig')], 'b34': [('가리지는', '가리키는')],
                'b95': [('hadn signals', 'hand signals')], 'b167': [('tum off', 'turn off')], 'b169': [('to cat healthier', 'to eat healthier')], 'b149': [('The girl jobs every day', 'The girl jogs every day')]})
NOTE.update({'b5': '원본 <보기> 이름 오타(히루 → 리우)', 'b95': '원본 오타 hadn → hand(③도 틀린 것처럼 보이던 문제)', 'b27': '원본 선택지 ③ 오타(ⓔ ⓔ ⓓ → ⓔ ⓐ ⓓ)'})
FIX_ANS.update({'b169': (0, '원본 정답 ③은 오류: need to go는 가능. practice는 to부정사를 쓰지 않으므로(practiced playing) ①이 정답'),
                'b178': (0, '원본 정답 ③은 오류: Domingo = Reuse, Minsu = Recycle → Reduce–Reuse–Recycle ①'),
                'b186': (3, '원본 정답 ②는 오류: 소녀 소개(C) → 이름(A) → (B) → (D) 순서 ④'),
                'b189': (1, '원본 정답 ①은 오류: 웃으며 셀카를 찍은 것은 맞음. 의자가 부서져도 신경 쓰지 않았으므로(she didn\'t care) ②가 일치하지 않음'),
                'b190': (1, '원본 정답 ①은 오류: 문을 두드렸는데(knocked) → 대답이 없었다 → (B)')})
items = []
for i, o, lab in D:
    if not o['ans'] or i in EXCL or '8' in (o['tag'] or ''): continue
    if i == 'b27': o['opts'][2] = o['opts'][2].replace('ⓔ\t\t  ⓔ', 'ⓔ\t\t  ⓐ')
    body = o['body']; opts = list(o['opts']); g = o['group']['text'] if o['group'] else None
    for a, b in FIX_TXT.get(i, []):
        hit = False
        if a in body: body = body.replace(a, b); hit = True
        opts2 = [x.replace(a, b) for x in opts]
        if opts2 != opts: opts = opts2; hit = True
        if g and a in g: g = g.replace(a, b); hit = True
        assert hit, (i, a)
    for a, b in FIX_GRP.get(i, []):
        if g and a in g: g = g.replace(a, b)
        elif a in body: body = body.replace(a, b)
        else: raise SystemExit('grp fix miss %d' % i)
    if i == 'a16': opts[4] = 'ⓔ'
    ans = C.index(o['ans'][0]); assert len(o['ans']) == 1
    note = NOTE.get(i, '')
    if i in FIX_ANS: ans, note = FIX_ANS[i]
    assert all(x.strip() for x in opts) and len(opts) == 5, (i, opts)
    bh = TBL[i] if i in TBL else H(body)
    gh = GTBL[i] if i in GTBL else (H(g) if g else None)
    stem = re.sub(r'\s*\[[\d과, ~]+\]\s*$', '', o['stem'])
    items.append({'i': i, 'lab': lab, 'school': o['school'], 'lesson': lesson(o), 'gkey': (o['file'], o['group']['head'], o['group']['text'][:80]) if o['group'] else None,
                  'stem': stem, 'body': bh, 'ghtml': gh, 'ghead': re.sub(r'\s*\[[\d과, ~]+\]\s*$', '', o['group']['head']) if o['group'] else '',
                  'opts': [H(x.strip()) for x in opts], 'ans': ans, 'note': note})
# 묶음(같은 지문) 단위
units = []
for it in items:
    if it['gkey'] and units and units[-1][0]['gkey'] == it['gkey']: units[-1].append(it)
    else: units.append([it])
order = {'5과': 0, '5·6과': 1, '6과': 2, '6·7과': 3, '7과': 4}
units.sort(key=lambda u: order[u[0]['lesson']])
sets = []; pool = list(units)
while pool:
    cur = []; n = 0; k = 0
    while k < len(pool) and n < 25:
        u = pool[k]
        if n + len(u) <= 25: cur.append(u); n += len(u); pool.pop(k)
        else: k += 1
    sets.append(cur)
print('items', len(items), 'sets', [sum(len(u) for u in s) for s in sets])
def test(no, S):
    its = []; n = 0
    total = sum(len(u) for u in S)
    pts = [4] * total if total == 25 else None
    if pts is None:
        base = 100 // total; pts = [base] * total
        for j in range(100 - base * total): pts[-1 - j] += 1
    for u in S:
        for j, it in enumerate(u):
            n += 1
            body = it['body']
            if it['ghtml'] and j == 0:
                rng = '[%d~%d] ' % (n, n + len(u) - 1) if len(u) > 1 else ''
                body = '<div class="wbox"><p><b>%s%s</b></p><p>%s</p></div>' % (rng, html.escape(it['ghead']), it['ghtml']) + (('<div>' + body + '</div>') if body.strip() else '')
            elif body.strip(): body = '<div class="wbox"><p>%s</p></div>' % body
            ex = '정답 ▶ %s\n출처 ▶ %s %s · %s' % (C[it['ans']], it['school'], it['lab'], it['lesson'])
            if it['note']: ex += '\n확인 ▶ ' + it['note']
            its.append({'n': n, 'src': '%s · %s' % (it['school'].replace('학교', ''), it['lesson']), 'stem': html.escape(it['stem']).replace('않은', '<u>않은</u>').replace('없는', '<u>없는</u>').replace('어색한', '<u>어색한</u>'),
                        'body': body, 'opts': it['opts'], 'en': True, 'ans': it['ans'], 'ex': ex, 'ctx': '', 'pts': pts[n - 1], 'words': [], 'kos': []})
    return {'id': 'm1gc-%d' % no, 'title': '동아(윤정미) 기출 %d회 (2025·2026 다른 학교 5·6·7과)' % no, 'short': '기출 %d회' % no, 'school': '중산중 1학년', 'minutes': 45, 'items': its}
TESTS = [test(k + 1, S) for k, S in enumerate(sets)]
for t in TESTS:
    assert sum(x['pts'] for x in t['items']) == 100
    print(t['id'], len(t['items']), ''.join(C[x['ans']] for x in t['items']))
if 'emit' in sys.argv:
    ids = [t['id'] for t in TESTS]
    blk = ('/* M1GC-TESTS: gen/m1gc/build.py 로 만듦 (손으로 고치지 말 것) */\nwindow.PKG.tests = (window.PKG.tests || []).filter(function (t) { return %s.indexOf(t.id) < 0; }).concat(%s);\n/* /M1GC-TESTS */\n'
           % (json.dumps(ids), json.dumps(TESTS, ensure_ascii=False)))
    js = open(DATA, encoding='utf-8').read()
    if '/* M1GC-TESTS' in js: js = re.sub(r'/\* M1GC-TESTS.*?/\* /M1GC-TESTS \*/\n', lambda m: blk, js, flags=re.S)
    else: js = js.rstrip('\n') + '\n\n' + blk
    open(DATA, 'w', encoding='utf-8').write(js); print('emit', ids)
