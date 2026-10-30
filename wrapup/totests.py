# Wrap-up 시험지 HTML → 데일리 앱 P.tests (학생이 앱에서 답 입력 · 채점 · 오답 노트)
# python3 totests.py  → 각 단원 데이터 끝의 /* WRAPUP-TESTS */ 블록을 다시 씀
#  - 선택형: 시험지 HTML(문항·정답표·해설)을 그대로 옮김
#  - 서술형: 아래 DAEJIN_WRITE 처럼 칸(blank)마다 정답·배점을 적음
#      ans: 자동 정답 / chk: 선생님 확인으로 넘길 답 / review: 정답이 아니면 '확인 필요'(부분 점수·여러 답 가능) / note: 틀리면 오답 노트로
import re, json, html, subprocess
W = '/tmp/claude-0/-home-claude/a9e3e882-1f02-5d62-8f70-aced81bc59d2/scratchpad/wrapup/'
D = '/home/claude/proj/data/'
CIR = '①②③④⑤'
SEC = '❶❷❸❹❺❻❼❽❾❿'

def txt(h): return html.unescape(re.sub(r'<[^>]+>', '', h)).strip()

def origin(datafile):
    """원문: 모의고사는 '18번' 단위, 교과서는 '❶' 단위"""
    pk = json.loads(subprocess.check_output(['node', '-e', "global.window={};require('%s');console.log(JSON.stringify(window.PKG.days.map(d=>d.passage)))" % datafile]))
    out = {}
    for ps in pk:
        cur = None
        for l in ps:
            if l[0] == '#':
                m = re.match(r'(\d+)번', l[1]); cur = m.group(1) if m else None
                if cur and cur in out: cur = None
                elif cur: out[cur] = []
            elif not l[0] and len(l[1]) == 1 and l[1] in SEC:
                cur = l[1] if l[1] not in out else None
                if cur: out[cur] = []
            elif cur is not None: out[cur].append(l[1])
    return {k: ' '.join(v) for k, v in out.items()}


import difflib
def kodict(datafile):
    pk = json.loads(subprocess.check_output(['node', '-e', "global.window={};require('%s');console.log(JSON.stringify(window.PKG.days.map(d=>d.passage)))" % datafile]))
    out = []
    for ps in pk:
        for l in ps:
            if l[0] != '#' and l[2] and len(l[1]) > 25 and (l[1], l[2]) not in out: out.append((l[1], l[2]))
    return out
def sents(h):
    t = txt(h.replace('</p><p>', ' ').replace('</div><div', ' </div><div'))
    t = re.sub(r'\(\s*[①②③④⑤]\s*\)', ' ', t); t = re.sub(r'[①②③④⑤]', '', t); t = re.sub(r'\([a-h]\)|\([A-E]\)', '', t)
    t = re.sub(r'\s+', ' ', t)
    return [x.strip() for x in re.split(r'(?<=[.!?"])\s+(?=[A-Z"])', t) if len(x.strip()) > 25]
def kos(it, KD):
    src = it.get('body', '') + it.get('ctx', '')
    found = []
    for snt in sents(src):
        best, r = None, 0
        for en, ko in KD:
            q = difflib.SequenceMatcher(None, snt.lower(), en.lower()).ratio()
            if q > r: best, r = (en, ko), q
        if best and r > 0.72 and best not in found: found.append(best)
    return [[e, k] for e, k in found]

def secs(src):
    """'본문 ❶~❸' → ['❶','❷','❸'], '본문 ❹' → ['❹']"""
    m = re.search('([%s])~([%s])' % (SEC, SEC), src)
    if m: return list(SEC[SEC.index(m.group(1)):SEC.index(m.group(2)) + 1])
    return [c for c in src if c in SEC]

def parse(fn, meta, orig, nmc=20):
    s = open(W + fn, encoding='utf-8').read()
    main = s[s.index('<div class="qs">'):]
    chunks = [c.split('<div class="foot">')[0] for c in main.split('<div class="q">')[1:nmc + 1]]
    key = {int(n): CIR.index(c) for n, c in re.findall(r'<div>(\d+)<b>([①②③④⑤])</b></div>', s)}
    exps = {int(n): txt(e) for n, c, e in re.findall(r'<p><b>(\d+)</b> <span class="k">([①②③④⑤])</span> (.*?)</p>', s)}
    items = []
    for ch in chunks:
        stem = re.search(r'<div class="stem">(.*?)</div>', ch, re.S).group(1)
        n = int(re.search(r'<span class="n">(\d+)\.</span>', stem).group(1))
        src = re.search(r'<span class="src">\[(.*?)\]</span>', stem); src = src.group(1) if src else ''
        stem = re.sub(r'<span class="n">\d+\.</span>', '', stem)
        stem = re.sub(r'<span class="src">.*?</span>', '', stem).strip()
        parts = re.findall(r'<div class="(box|given|sum)">(.*?)</div>', ch, re.S)
        body = ''.join('<div class="w%s">%s</div>' % (k, v.strip()) for k, v in parts).replace('class="blank"', 'class="wblank"')
        ol = re.search(r'<ol class="ol( en)?">(.*?)</ol>', ch, re.S)
        tb = re.search(r'<table class="ch">(.*?)</table>', ch, re.S)
        en = True
        if ol:
            en = bool(ol.group(1))
            opts = [m.strip() for m in re.findall(r'<li><span>[①②③④⑤]</span><span>(.*?)</span></li>', ol.group(2), re.S)]
        elif tb:
            heads = [txt(h) for h in re.findall(r'<th>(.*?)</th>', tb.group(1))][1:]
            rows = re.findall(r'<tr><td>[①②③④⑤]</td>(.*?)</tr>', tb.group(1), re.S)
            opts = [' / '.join(x.strip() for x in re.findall(r'<td>(.*?)</td>', r)) for r in rows]
            body += '<div class="wcols">선택지 순서: ' + ' / '.join(html.escape(h) for h in heads) + '</div>'
        else:
            ins = '들어가기' in stem
            opts = ['( %s ) 자리' % c if ins else '%s번' % c for c in CIR]
            en = False
        assert len(opts) == 5 and len(set(opts)) == 5, (fn, n, opts)
        ctx = ''
        if not any(k == 'box' for k, _ in parts):
            m = re.search(r'위 글\((\d+)번\)', stem)
            m2 = re.search(r'(\d\d)번 글', stem)
            if m: ctx = 'Q' + m.group(1)
            elif m2: ctx = '<div class="wbox"><p>' + html.escape(orig[m2.group(1)]) + '</p></div>'
            elif secs(src):
                ctx = ''.join('<div class="wbox"><p><b>%s</b> %s</p></div>' % (c, html.escape(orig[c])) for c in secs(src))
            elif '글' in stem: raise SystemExit(('지문 없음', fn, n, stem))
            u = re.search(r'밑줄 친 (.+?)(?:가|이) ', txt(stem))
            if u and ctx and not ctx.startswith('Q') and html.escape(u.group(1)) in ctx:
                ctx = ctx.replace(html.escape(u.group(1)), '<u>' + html.escape(u.group(1)) + '</u>', 1)
        items.append({'n': n, 'src': src, 'stem': stem, 'body': body, 'opts': opts, 'en': en, 'ans': key[n], 'ex': exps[n], 'ctx': ctx, 'pts': meta['pts']})
    for it in items:
        if it['ctx'].startswith('Q'):
            ref = items[int(it['ctx'][1:]) - 1]
            it['ctx'] = ''.join(re.findall(r'<div class="wbox">.*?</div>', ref['body'], re.S)); assert it['ctx'], it['n']
    assert [i['n'] for i in items] == list(range(1, nmc + 1)), fn
    t = dict(meta); del t['pts']; t['items'] = items
    return t

# 대진고 서술형 (시험지 wrapup-daejin-ne-oh-L3.html 서술형 1~3 · 모범 답안과 채점 기준 그대로)
S1 = 'Although the FPTP method is {A} and easy to understand, it can let an option win without the support of the {B}.'
S2 = 'In the AV method, if no option wins more than half of the first-preference votes, the option with the fewest votes is eliminated, and its votes {A}.'
S3 = 'The story of the student council shows that {A}, as the FPTP method chose the charity concert while the AV method chose the bake sale, mainly because of {B}.'
def gap(s, me, fill):
    s = s.replace('{%s}' % me, '___')
    for k, v in fill.items(): s = s.replace('{%s}' % k, v)
    assert '{' not in s, s
    return s
DAEJIN_WRITE = [
    {'n': '서술형 1', 'src': '본문 ❹', 'pts': 6,
     'stem': '본문 ❹의 내용을 요약한 문장의 빈칸 (A), (B)에 들어갈 말을 <b>본문에서 찾아</b> 각각 한 단어로 쓰시오. <b>[6점]</b>',
     'body': '<div class="wsum">' + S1.replace('{A}', '<b>(A)</b> ________').replace('{B}', '<b>(B)</b> ________') + '</div>',
     'blanks': [
        {'label': '(A)', 'pts': 3, 'ans': ['uncomplicated'], 'chk': ['simple'], 'note': True, 's': gap(S1, 'A', {'B': 'majority'}), 'v': '(A) 본문 ❹에서 찾아 한 단어'},
        {'label': '(B)', 'pts': 3, 'ans': ['majority'], 'chk': [], 'note': True, 's': gap(S1, 'B', {'A': 'uncomplicated'}), 'v': '(B) 본문 ❹에서 찾아 한 단어'}],
     'model': '(A) uncomplicated (B) majority',
     'ex': "근거: The FPTP method is uncomplicated and easy to understand ... It is possible to win a vote without the support of the majority. 각 3점. (A)는 본문 단어 uncomplicated가 정답이에요. simple로 쓴 답은 선생님이 확인해요."},
    {'n': '서술형 2', 'src': '본문 ❺', 'pts': 7,
     'stem': '본문 ❺의 내용을 요약한 문장이 되도록 &lt;보기&gt;의 말을 <b>모두 한 번씩</b> 바르게 배열하여 빈칸을 완성하시오. <b>[7점]</b>',
     'body': '<div class="wsum">' + S2.replace('{A}', '________________________') + '</div><div class="wcond"><b>&lt;보기&gt;</b> second preferences / redistribute / voters\' / according / to</div><div class="wcond"><b>&lt;조건&gt;</b> 필요하면 어형을 바꾸고, 문맥에 맞게 <u>be동사 한 단어</u>를 추가할 것</div>',
     'blanks': [{'label': '', 'pts': 7, 'ans': ["are redistributed according to voters' second preferences"], 'chk': [], 'review': True, 'note': True,
                 's': gap(S2, 'A', {}), 'v': "<보기> second preferences / redistribute / voters' / according / to + be동사"}],
     'model': "are redistributed according to voters' second preferences",
     'ex': "근거: the 5 council members' votes were redistributed based on their second preferences → its votes(복수, 현재 일반 서술) + 수동태 are redistributed. according to = based on. 어순 완벽 7점 · be동사 누락/시제 오류 −2점 · redistribute 형태 오류 −2점 (부분 점수는 선생님이 확인해요)."},
    {'n': '서술형 3', 'src': '본문 ❶~❺', 'pts': 7,
     'stem': '본문 ❶~❺의 내용을 요약한 문장을 &lt;조건&gt;에 맞게 완성하시오. <b>[7점]</b>',
     'body': '<div class="wsum">' + S3.replace('{A}', '<b>(A)</b> ________________').replace('{B}', '<b>(B)</b> ________________') + '</div><div class="wcond"><b>&lt;조건&gt;</b> (A) <u>result, depend, voting method</u>를 반드시 사용하여 주어와 동사를 갖춘 절로 쓸 것 (9~11단어, 어형 변화 가능)<br>(B) <u>본문에서 찾아</u> 5단어로 쓸 것 (하이픈으로 연결된 말은 한 단어)</div>',
     'blanks': [
        {'label': '(A)', 'pts': 4, 'ans': ['the result of a vote can depend on the voting method', 'the result can depend on which voting method is used',
                                          'the result of a vote depends on the voting method', 'the results of a vote can depend on the voting method',
                                          'the result of the vote can depend on the voting method'], 'chk': [], 'review': True, 'note': False},
        {'label': '(B)', 'pts': 3, 'ans': ['the second-preference votes it received'], 'chk': ['the second preference votes it received'], 'note': True,
         's': gap(S3, 'B', {'A': 'the result of a vote can depend on the voting method'}), 'v': '(B) 본문 ❺에서 찾아 5단어'}],
     'model': '(A) the result of a vote can depend on the voting method (B) the second-preference votes it received',
     'ex': '(A) the result can depend on which voting method is used(10단어) 등 조건에 맞으면 인정 → 정해 둔 답과 다르게 쓰면 선생님이 확인해요. (A) 4점: 세 단어 모두 사용 2점 + 문법·단어 수 2점 · (B) 3점 (본문 ❺ 마지막 문장 the / second-preference / votes / it / received).'},
]
for w in DAEJIN_WRITE: w['kind'] = 'write'; assert sum(b['pts'] for b in w['blanks']) == w['pts']

def emit(datafile, tests):
    from enrich import E as EN
    KD = kodict(datafile)
    for t in tests:
        en = EN.get(t['id'], {})
        for it in t['items']:
            if it.get('kind') == 'write': continue
            x = en.get(it['n'], {})
            if 'o' in x: assert len(x['o']) == 5, (t['id'], it['n']); it['okos'] = x['o']
            it['words'] = x.get('w', [])
            if it['en'] and not it.get('okos') and len(txt(it['opts'][0]).split()) > 3: print('  선택지 해석 없음', t['id'], it['n'])
            if not it['words']: print('  단어 없음', t['id'], it['n'])
    for t in tests:
        for it in t['items']:
            if it.get('kind') != 'write': it['kos'] = kos(it, KD)
    js = open(datafile, encoding='utf-8').read()
    blk = '/* WRAPUP-TESTS: scratchpad/wrapup/totests.py 로 만듦 (손으로 고치지 말 것) */\nwindow.PKG.tests = ' + json.dumps(tests, ensure_ascii=False) + ';\n/* /WRAPUP-TESTS */\n'
    if '/* WRAPUP-TESTS' in js: js = re.sub(r'/\* WRAPUP-TESTS.*?/\* /WRAPUP-TESTS \*/\n', lambda m: blk, js, flags=re.S)
    else: js = js.rstrip('\n') + '\n' + blk
    open(datafile, 'w', encoding='utf-8').write(js)
    for t in tests:
        mc = [i for i in t['items'] if i.get('kind') != 'write']
        tot = sum(i['pts'] for i in t['items'])
        print(datafile.split('/')[-1], t['id'], len(t['items']), '문항', tot, '점', ''.join(CIR[i['ans']] for i in mc), 'ctx', sum(1 for i in mc if i['ctx']), '해석 없음', [i['n'] for i in mc if not i['kos']])
        assert tot == 100, tot

F = D + 'h1-mock-2509.js'; O = origin(F)
emit(F, [
    parse('wrapup-2509-22.html', {'id': 'js2509a', 'title': '9월 학평 18~22번 Wrap-up', 'short': '18~22번', 'school': '중산고 1학년', 'minutes': 30, 'pts': 5}, O),
    parse('wrapup-2509-2324.html', {'id': 'js2509b', 'title': '9월 학평 23·24번 Wrap-up', 'short': '23·24번', 'school': '중산고 1학년', 'minutes': 30, 'pts': 5}, O),
])
F = D + 'h1-ne-min-L3.js'; O = origin(F)
emit(F, [parse('wrapup-jeodong-ne-L3.html', {'id': 'jd-ne-l3', 'title': '능률 L3 본문 ❶~❸ Wrap-up', 'short': '본문 ❶~❸', 'school': '저동고 1학년', 'minutes': 30, 'pts': 5}, O)])
F = D + 'h2-ne-oh-L3.js'; O = origin(F)
dj = parse('wrapup-daejin-ne-oh-L3.html', {'id': 'dj-ne-l3', 'title': '능률 L3 본문 ❶~❺ Wrap-up', 'short': '본문 ❶~❺', 'school': '대진고 2학년', 'minutes': 45, 'pts': 4}, O)
dj['items'] += DAEJIN_WRITE
emit(F, [dj])
