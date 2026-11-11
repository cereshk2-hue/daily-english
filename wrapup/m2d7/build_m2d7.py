# 11/11 중2 동아(윤정미) 7과 데일리 실전 9회(다른 창에서 만든 문항은행 xlsx) → 앱 '실전 문제' 탭(OMR 답안지)
# 바탕: m1c4/build_m1c4.py. 검수하며 고친 곳은 FIXB(지문)·SPECIAL/EXTRA_OK(서술형)에 모아 둠
import openpyxl, re, json, sys, html as H
from docx import Document
Z = '/home/claude/work/m2d7/zip/'
src = open('/home/claude/srcrepo/wrapup/totests.py', encoding='utf-8').read()
sys.path.insert(0, '/home/claude/srcrepo/wrapup')
exec(src[:src.index("F = D + 'h1-mock-2509.js'")])
CIRC = '①②③④⑤'
wb = openpyxl.load_workbook(Z + '중2동아7과_데일리실전_문항은행.xlsx'); ws = wb['문항은행']
HD = [c.value for c in ws[1]]
rows = [dict(zip(HD, r)) for r in ws.iter_rows(min_row=2, values_only=True) if r[0]]
KEY = {str(r[0]).replace('회', ''): list(r[1:]) for r in wb['회차별 정답'].iter_rows(min_row=2, values_only=True) if r[0]}
BODY = '지문·보기 (밑줄은 < >로 표시)'

# 검수: 지문 표기 오류 고치기 (회, 번호): [(찾을 것, 바꿀 것)]
FIXB = {
 (1, 4): [('G:\nB: Why?', 'G: ________\nB: Why?')],                       # 빈칸 표시 빠짐
 (3, 5): [('it’ll be <more> fun', 'it’ll be more fun')],                  # 번호 없는 밑줄
 (4, 6): [('it’ll be <more> fun', 'it’ll be more fun')],
 (5, 3): [('the T-shirt <better>.', 'the T-shirt better.')],
 (6, 3): [('the T-shirt <better>.', 'the T-shirt better.')],
 (3, 16): [('was not easy', '________ was not easy')],                    # 빈칸 표시 빠짐
 (6, 16): [('is important to show up', '________ is important to show up')],
 (8, 15): [('exc<it>ing', 'exciting')],                                   # 단어 속 it 밑줄
 (6, 5): [('(A) B: Don’t forget Korea.G: Of course, Korea, too. So, the fireworks start at 7 p.m. Right?B: Yeah.\n(B) Let’s do something together until then.G:',
           '(A) B: Don’t forget Korea.\nG: Of course, Korea, too. So, the fireworks start at 7 p.m. Right?\n(B) B: Yeah. Let’s do something together until then.\nG:'),
          ('Which do you like more?B:', 'Which do you like more?\nB:'), ('more fun.G:', 'more fun.\nG:'), ('too?G:', 'too?\nG:')],
}
def fixrow(r):   # FIXB는 지문이나 선택지 어디든 그 글자가 있는 칸에 적용
    k, n = r['회차'], int(r['번호'])
    for a, b in FIXB.get((k, n), []):
        hit = [c for c in [BODY] + list(CIRC) if r[c] and a in str(r[c])]
        assert hit, (k, n, a)
        for c in hit: r[c] = str(r[c]).replace(a, b)
def fixbody(k, n, s):
    s = str(s or '')
    s = s.replace('\u2003', ' ')
    s = re.sub(r'([A-Za-z0-9]{2})(_{4,})', r'\1 \2', s); s = re.sub(r'(_{4,})([A-Za-z0-9]{2})', r'\1 \2', s)
    s = re.sub(r'[ \t]{2,}', ' ', s); s = re.sub(r'(_{4,}) ,', r'\1,', s)
    return s
def fmt(s):
    s = H.escape(str(s or '').strip(), quote=False)
    s = s.replace('&lt;조건&gt;', '\x01조건\x02').replace('&lt;보기&gt;', '\x01보기\x02')
    s = re.sub(r'&lt;(.+?)&gt;', r'<u>\1</u>', s)
    s = s.replace('\x01', '&lt;').replace('\x02', '&gt;')
    return s.replace('\n', '<br>')
def plain(s): return re.sub(r'\s+', ' ', str(s or '')).strip()
def isen(o): return sum(c.isascii() and c.isalpha() for c in o) > len(o) * 0.5

CAUT = {}
for k in range(1, 10):
    ps = [p.text for p in Document(Z + '중2동아7과_데일리실전_%02d회.docx' % k).paragraphs]
    CAUT[str(k)] = [p.replace('[주의]', '').strip() for p in ps if p.startswith('[주의]')]

def variants(a, it_opt=False):
    v = {a}
    for x in list(v):
        if re.search(r'[?!.]$', x): v.add(x[:-1])
    for x in list(v):
        x2 = x.replace('’', "'")
        v |= {x2, x2.replace("isn't", 'is not'), x2.replace('is not', "isn't")}
    if it_opt:   # 'It ________.' 답란: It 빼고 써도, 붙여 써도 정답
        for x in list(v):
            v.add(x[3:] if x.startswith('It ') else 'It ' + x)
    return sorted(v)
def arrow(a, b): return [a + s + b for s in (' → ', '→', ' -> ', '->', ' - ')] + [b]
SPECIAL = {
 ('7', 20): [{'label': '(1)', 'pts': 2.5, 'ans': arrow('healthily', 'healthy') + arrow('strongly', 'strong'), 'chk': []},   # [주의] 순서 바뀌어도 정답
             {'label': '(2)', 'pts': 2.5, 'ans': arrow('strongly', 'strong') + arrow('healthily', 'healthy'), 'chk': []}],
 ('9', 19): [{'label': '빈칸 %d' % (i + 1), 'pts': 1, 'ans': [w], 'chk': []} for i, w in enumerate(['It', 'to', 'solve', 'the', 'problem'])],
}
IT_OPT = {('1', 20), ('7', 19)}
EXTRA_OK = {('4', 19, 0): ['It isn’t possible to run faster than reindeer.'], ('6', 20, 1): ['It isn’t easy to swim in the sea.']}
def blanks(r):
    k, n = str(r['회차']), int(r['번호'])
    if (k, n) in SPECIAL: return SPECIAL[(k, n)]
    a = plain(r['서술형 정답'])
    parts = re.split(r'\s+/\s+(?=\(\w\))', a) if re.match(r'\(\w\)', a) else [a]
    out = []
    for i, p in enumerate(parts):
        m = re.match(r'\((\w)\)\s*(.*)', p)
        lab, ans = (('(%s)' % m.group(1)), m.group(2)) if m else ('', p)
        alts = variants(ans, (k, n) in IT_OPT)
        for e in EXTRA_OK.get((k, n, i), []): alts += [x for x in variants(e) if x not in alts]
        out.append({'label': lab, 'pts': 0, 'ans': alts, 'chk': []})
    w = {1: [5], 2: [2.5, 2.5], 3: [2, 1.5, 1.5], 5: [1] * 5}[len(out)]
    for b, p in zip(out, w): b['pts'] = p
    return out

def okos(r, ans):   # 선택지 우리말: 오답 분석(①…②…) + 해설 속 정답 해석
    oa = plain(r['오답 분석·주의']); ex = plain(r['해설'])
    parts = re.split(r'\s*([①②③④⑤])\s*', ' ' + oa)
    d = {parts[i]: parts[i + 1].strip() for i in range(1, len(parts) - 1, 2)}
    m = re.search(CIRC[ans] + r"\s*['‘]([^'’]+)['’]", ex)
    if m: d[CIRC[ans]] = m.group(1).strip()
    if set(d) != set(CIRC) or any(not v or isen(v) for v in d.values()): return None
    return [d[c] for c in CIRC]

tests = []; nok = 0
for k in range(1, 10):
    K = str(k); R = sorted([r for r in rows if str(r['회차']) == K], key=lambda r: int(r['번호']))
    assert len(R) == 20, (K, len(R))
    items, wi = [], 0
    for r in R:
        fixrow(r)
        n = int(r['번호']); body = fmt(fixbody(k, n, r[BODY]))
        ex = '이유 ▶ ' + plain(r['해설']) + ('\n오답 ▶ ' + plain(r['오답 분석·주의']) if r['오답 분석·주의'] else '') + ('\n포인트 ▶ ' + plain(r['핵심']) if r['핵심'] else '')
        src_ = r['영역'] + ' · ' + r['유형'].replace('★', '').strip()
        if r['형식'] == '객관식':
            opts = [fmt(fixbody(k, n, r[c])) if r[c] else '' for c in CIRC]; ans = CIRC.index(str(r['정답']).strip())
            if not any(opts):
                opts = ['( %s ) 자리' % c if '( ①' in body else '%s번' % c for c in CIRC]
            assert all(opts), (K, n); assert str(KEY[K][n - 1]).strip() == CIRC[ans], (K, n, KEY[K][n - 1])
            it = {'n': n, 'src': src_, 'stem': fmt(r['발문']), 'body': body, 'opts': opts, 'en': isen(plain(r['①'])), 'ans': ans, 'ex': ex, 'ctx': '', 'pts': 5}
            if it['en'] and len(plain(r['①']).split()) > 3:
                o = okos(r, ans)
                if o: it['okos'] = o; nok += 1
            items.append(it)
        else:
            c = CAUT[K][wi]; wi += 1
            if '마침표' in c and '앱' in c: c = '마침표는 찍어도 안 찍어도 정답이에요.'
            if r['오답 분석·주의'] and plain(r['오답 분석·주의']) == plain(CAUT[K][wi - 1]): ex = ex.split('\n오답 ▶ ')[0] + ('\n포인트 ▶ ' + plain(r['핵심']) if r['핵심'] else '')
            items.append({'kind': 'write', 'n': '서술형 %d' % n, 'src': src_, 'pts': 5, 'stem': fmt(r['발문']), 'body': body, 'blanks': blanks(r),
                          'model': plain(r['서술형 정답']), 'ex': ex.replace('이유 ▶ ', '해설 ▶ ', 1) + '\n주의 ▶ ' + c})
    assert wi == len(CAUT[K]), (K, wi, len(CAUT[K]))
    tests.append({'id': 'm2d7-%02d' % k, 'title': '동아 7과 실전 문제 %d회' % k, 'short': '실전 %d회' % k, 'school': '중2 동아(윤정미)', 'minutes': 30, 'items': items})
print('선택지 해석 붙인 문항', nok)
F = D + 'm2-donga-yoon-L7.js'
emit(F, tests)
