# 11/10 중1 천재(소영순) 4과 데일리 실전 10회(다른 창에서 만든 문항은행 xlsx) → 앱 Wrap-up 탭(OMR 답안지)
import openpyxl, re, json, sys, html as H
from docx import Document
Z = '/home/claude/work/m1c4/zip/'
src = open('/home/claude/srcrepo/wrapup/totests.py', encoding='utf-8').read()
sys.path.insert(0, '/home/claude/srcrepo/wrapup')
exec(src[:src.index("F = D + 'h1-mock-2509.js'")])
CIRC = '①②③④⑤'
wb = openpyxl.load_workbook(Z + '천재4단원_데일리실전_문항은행.xlsx'); ws = wb['문항은행']
HD = [c.value for c in ws[1]]
rows = [dict(zip(HD, r)) for r in ws.iter_rows(min_row=2, values_only=True) if r[0]]
KEY = {str(r[0]).replace('회', ''): list(r[1:]) for r in wb['회차별 정답'].iter_rows(min_row=2, values_only=True) if r[0]}

def fmt(s):
    s = H.escape(str(s or '').strip(), quote=False)
    s = s.replace('&lt;조건&gt;', '\x01조건\x02').replace('&lt;보기&gt;', '\x01보기\x02')
    s = re.sub(r'&lt;(.+?)&gt;', r'<u>\1</u>', s)
    s = s.replace('\x01', '&lt;').replace('\x02', '&gt;')
    return s.replace('\n', '<br>')
def plain(s): return re.sub(r'\s+', ' ', str(s or '')).strip()
def isen(o): return sum(c.isascii() and c.isalpha() for c in o) > len(o) * 0.5

# [주의] 줄: 각 회 docx에서 서술형 순서대로
CAUT = {}
for k in range(1, 11):
    ps = [p.text for p in Document(Z + '천재4단원_데일리실전_%02d회.docx' % k).paragraphs]
    CAUT[str(k)] = [p.replace('[주의]', '').strip() for p in ps if p.startswith('[주의]')]

# 서술형 빈칸 나누기 + 허용 답안
def variants(a):
    v = {a}
    for x in list(v):
        if re.search(r'[?!.]$', x): v.add(x[:-1])
    for x in list(v):
        x2 = x.replace('’', "'")
        v |= {x2, x2.replace("didn't", 'did not'), x2.replace("did not", "didn't")}
    return sorted(v)
SPECIAL = {  # (회, 번호): blanks
 ('4', 20): [{'label': '기호', 'pts': 1, 'ans': ['(E)', 'E'], 'chk': []}, {'label': '틀린 단어', 'pts': 2, 'ans': ['speak'], 'chk': []}, {'label': '고친 단어', 'pts': 2, 'ans': ['speaking'], 'chk': []}],
}
EXTRA_OK = {('5', 19, 1): ['He did not finish his homework.'], ('8', 19, 0): ['Seeing the blue ocean and the green islands was fantastic.']}
CHK = {('2', 19, 0): ['was']}   # 선생님 확인: 원칙은 is, was도 어색하진 않음
def blanks(r):
    k, n = str(r['회차']), int(r['번호'])
    if (k, n) in SPECIAL: return SPECIAL[(k, n)]
    a = plain(r['서술형 정답'])
    parts = re.split(r'\s+/\s+(?=\(\w\))', a) if re.match(r'\(\w\)', a) else [a]
    out = []
    for i, p in enumerate(parts):
        m = re.match(r'\((\w)\)\s*(.*)', p)
        lab, ans = (('(%s)' % m.group(1)), m.group(2)) if m else ('', p)
        alts = variants(ans)
        for e in EXTRA_OK.get((k, n, i), []): alts += [x for x in variants(e) if x not in alts]
        out.append({'label': lab, 'pts': 0, 'ans': alts, 'chk': CHK.get((k, n, i), [])})
    w = {1: [5], 2: [2.5, 2.5], 3: [2, 1.5, 1.5], 5: [1] * 5}[len(out)]
    for b, p in zip(out, w): b['pts'] = p
    return out

tests = []
for k in range(1, 11):
    K = str(k); R = sorted([r for r in rows if str(r['회차']) == K], key=lambda r: int(r['번호']))
    assert len(R) == 20, (K, len(R))
    items, wi = [], 0
    for r in R:
        n = int(r['번호']); body = fmt(r['지문·보기 (밑줄은 < >로 표시)'])
        ex = '이유 ▶ ' + plain(r['해설']) + ('\n오답 ▶ ' + plain(r['오답 분석·주의']) if r['오답 분석·주의'] else '') + ('\n포인트 ▶ ' + plain(r['핵심']) if r['핵심'] else '')
        if r['형식'] == '객관식':
            opts = [fmt(r[c]) for c in CIRC]; ans = CIRC.index(str(r['정답']).strip())
            if not any(opts):  # 선지가 본문 속 ①~⑤ 자리(문장 삽입·밑줄)
                opts = ['( %s ) 자리' % c if '( ①' in body or '(①' in body else '%s번' % c for c in CIRC]
            assert all(opts), (K, n); assert str(KEY[K][n - 1]).strip() == CIRC[ans], (K, n, KEY[K][n - 1])
            items.append({'n': n, 'src': r['영역'] + ' · ' + r['유형'], 'stem': fmt(r['발문']), 'body': body, 'opts': opts, 'en': isen(plain(r['①'])), 'ans': ans, 'ex': ex, 'ctx': '', 'pts': 5})
        else:
            c = CAUT[K][wi]; wi += 1
            bl = blanks(r)
            items.append({'kind': 'write', 'n': '서술형 %d' % n, 'src': r['영역'] + ' · ' + r['유형'], 'pts': 5, 'stem': fmt(r['발문']), 'body': body, 'blanks': bl,
                          'model': plain(r['서술형 정답']), 'ex': ex.replace('이유 ▶ ', '해설 ▶ ', 1) + '\n주의 ▶ ' + c})
    assert wi == len(CAUT[K]), (K, wi, len(CAUT[K]))
    tests.append({'id': 'm1c4-%02d' % k, 'title': '천재 4과 실전 문제 %d회' % k, 'short': '실전 %d회' % k, 'school': '중1 천재(소영순)', 'minutes': 30, 'items': items})
F = D + 'm1-chunjae-so-L6.js'
emit(F, tests)
