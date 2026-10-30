# Wrap-up 시험지 HTML → 데일리 앱 P.tests (학생이 앱에서 답 입력 · 채점 · 오답 노트)
# python3 totests.py  → /home/claude/proj/data/h1-mock-2509.js 끝의 /* WRAPUP-TESTS */ 블록을 다시 씀
import re, json, html, subprocess, sys
W = '/tmp/claude-0/-home-claude/a9e3e882-1f02-5d62-8f70-aced81bc59d2/scratchpad/wrapup/'
DATA = '/home/claude/proj/data/h1-mock-2509.js'
CIR = '①②③④⑤'

# 원문 지문(18~24번): 'N번 글' 문항을 오답 노트에서 풀 때 함께 보여 줌
pk = json.loads(subprocess.check_output(['node', '-e', "global.window={};require('%s');console.log(JSON.stringify(window.PKG.days.map(d=>d.passage)))" % DATA]))
ORIG = {}
for ps in pk:
    cur = None
    for l in ps:
        if l[0] == '#':
            m = re.match(r'(\d+)번', l[1]); cur = m.group(1) if m else None
            if cur: ORIG.setdefault(cur, [])
        elif cur: ORIG[cur].append(l[1])
ORIG = {k: ' '.join(v) for k, v in ORIG.items()}

def txt(h): return html.unescape(re.sub(r'<[^>]+>', '', h)).strip()

def parse(fn, tid, title, short):
    s = open(W + fn, encoding='utf-8').read()
    main = s[s.index('<div class="qs">'):s.index('<div class="foot">')]
    chunks = main.split('<div class="q">')[1:]
    keys = re.findall(r'<div>(\d+)<b>([①②③④⑤])</b></div>', s)
    key = {int(n): CIR.index(c) for n, c in keys}
    exps = {int(n): txt(e) for n, c, e in re.findall(r'<p><b>(\d+)</b> <span class="k">([①②③④⑤])</span> (.*?)</p>', s)}
    items = []
    for ch in chunks:
        stem = re.search(r'<div class="stem">(.*?)</div>', ch, re.S).group(1)
        n = int(re.search(r'<span class="n">(\d+)\.</span>', stem).group(1))
        src = re.search(r'<span class="src">\[(.*?)\]</span>', stem)
        src = src.group(1) if src else ''
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
        # 지문이 없는 문항: '위 글(N번)' → N번 문항의 지문, 'NN번 글' → 원문
        ctx = ''
        if not any(k == 'box' for k, _ in parts):
            m = re.search(r'위 글\((\d+)번\)', stem)
            m2 = re.search(r'(\d\d)번 글', stem)
            if m: ctx = 'Q' + m.group(1)
            elif m2: ctx = '<div class="wbox"><p>' + html.escape(ORIG[m2.group(1)]) + '</p></div>'
            elif '글' in stem: raise SystemExit(('지문 없음', fn, n, stem))
        items.append({'n': n, 'src': src, 'stem': stem, 'body': body, 'opts': opts, 'en': en, 'ans': key[n], 'ex': exps[n], 'ctx': ctx})
    for it in items:
        if it['ctx'].startswith('Q'):
            ref = items[int(it['ctx'][1:]) - 1]
            it['ctx'] = ''.join(re.findall(r'<div class="wbox">.*?</div>', ref['body'], re.S))
            assert it['ctx'], it['n']
    assert [i['n'] for i in items] == list(range(1, 21)) and len(exps) == 20 and len(key) == 20, fn
    return {'id': tid, 'title': title, 'short': short, 'school': '중산고 1학년', 'minutes': 30, 'items': items}

TESTS = [
    parse('wrapup-2509-22.html', 'js2509a', '9월 학평 18~22번 Wrap-up', '18~22번'),
    parse('wrapup-2509-2324.html', 'js2509b', '9월 학평 23·24번 Wrap-up', '23·24번'),
]
for t in TESTS:
    print(t['id'], len(t['items']), ''.join(CIR[i['ans']] for i in t['items']), sum(1 for i in t['items'] if i['ctx']), 'ctx')
js = open(DATA, encoding='utf-8').read()
blk = '/* WRAPUP-TESTS: scratchpad/wrapup/totests.py 로 만듦 (손으로 고치지 말 것) */\nwindow.PKG.tests = ' + json.dumps(TESTS, ensure_ascii=False) + ';\n/* /WRAPUP-TESTS */\n'
if '/* WRAPUP-TESTS' in js: js = re.sub(r'/\* WRAPUP-TESTS.*?/\* /WRAPUP-TESTS \*/\n', lambda m: blk, js, flags=re.S)
else: js = js.rstrip('\n') + '\n' + blk
open(DATA, 'w', encoding='utf-8').write(js)
