# 11/11 중산고1 비밀노트 변형문제 18~24번 인쇄용 시험지 (검수 반영) — build_bimi.py가 만든 tests.json → A4 HTML → PDF
import json, re, html as H, sys
from playwright.sync_api import sync_playwright
D = json.load(open('/home/claude/work/jsan/tests.json'))
OUT = '/home/claude/work/jsan/paper/'
CIRC = '①②③④⑤'
CSS = '''<style>
@page { size: A4; margin: 12mm 11mm 13mm }
* { box-sizing: border-box }
body { font-family: 'Noto Serif CJK KR', 'Noto Serif', serif; font-size: 9.3pt; line-height: 1.55; color: #111; margin: 0 }
.sans, .hd, .tt, .idrow, .notice, .stem, .key, .eb, h3, .gh, .lab, .optn { font-family: 'Noto Sans CJK KR', sans-serif }
.hd { display: flex; justify-content: space-between; font-size: 8.3pt; border-bottom: 1.6px solid #111; padding-bottom: 3px; margin-bottom: 7px }
.tt { display: flex; align-items: flex-end; justify-content: space-between; margin: 0 0 7px }
.tt h1 { font-size: 19pt; margin: 0; letter-spacing: -.02em } .tt .l, .tt .r { font-weight: 700; font-size: 10.5pt; width: 28% } .tt .r { text-align: right }
.idrow { display: grid; grid-template-columns: 1fr 1.4fr .8fr 1fr .8fr 2fr .8fr 1fr; border: 1.4px solid #111; font-size: 8.6pt; margin-bottom: 7px }
.idrow div { padding: 4px 6px; border-right: 1px solid #999 } .idrow div:nth-child(odd) { background: #eee; font-weight: 700; text-align: center } .idrow div:last-child { border-right: 0 }
.notice { border: 1px solid #999; background: #f6f6f6; padding: 5px 9px; font-size: 8.2pt; margin-bottom: 9px } .notice p { margin: 1px 0 }
.cols { column-count: 2; column-gap: 8mm; column-rule: 1px solid #bbb }
.grp { border: 1.2px solid #333; padding: 6px 8px; margin: 0 0 10px; break-inside: avoid-column }
.gh { font-weight: 700; margin: 0 0 3px; font-size: 9pt }
.psg { text-align: justify; margin: 0 }
.q { margin: 0 0 12px; break-inside: avoid }
.q.long { break-inside: auto }
.stem { break-after: avoid; margin: 0 0 4px; padding-left: 1.7em; text-indent: -1.7em; font-weight: 500; font-size: 9pt } .stem .n { font-weight: 800 }
.body { text-align: justify; margin: 0 0 4px }
.opts { break-inside: avoid; margin: 2px 0 0; padding: 0; list-style: none } .opts li { padding-left: 1.4em; text-indent: -1.4em; margin: 1px 0 }
.opts.row { display: flex; gap: 14px; flex-wrap: wrap }
.optn { font-weight: 700 }
.wl { margin: 4px 0 0 } .wl div { display: flex; gap: 6px; align-items: flex-end; margin: 5px 0 } .wl .lab { flex: none; font-size: 8.4pt; font-weight: 700 } .wl span { flex: 1; border-bottom: 1px solid #111; height: 1.35em }
.wl.big span { height: 2.6em }
.pg { break-before: page }
.key { width: 100%; border-collapse: collapse; margin: 4px 0 8px; font-size: 8.6pt; text-align: center } .key td { border: 1px solid #888; padding: 2px 1px } .key tr:nth-child(odd) td { background: #eee; font-weight: 700 }
.rule { border: 1px solid #999; background: #fbf3e6; padding: 6px 9px; font-size: 8.3pt; margin-bottom: 9px; font-family: 'Noto Sans CJK KR', sans-serif } .rule p { margin: 2px 0 }
.ex { break-inside: avoid; margin: 0 0 9px; font-size: 8.6pt }
.eb { background: #111; color: #fff; padding: 2px 7px; font-weight: 700; font-size: 8.8pt; margin-bottom: 3px } .eb small { font-weight: 500; margin-left: 6px; color: #ddd }
.ex p { margin: 1px 0; padding-left: 3.6em; text-indent: -3.6em } .ex .lb { font-family: 'Noto Sans CJK KR', sans-serif; font-weight: 800; margin-right: 4px }
.ex .fix { color: #a8323a; font-weight: 700 }
.ex small { color: #555; font-size: 7.6pt }
</style>'''
def e(s): return H.escape(s, quote=False)
def clean(body):   # 표 머리 (A)(B) 줄·빈 줄 정리
    lines = [l for l in body.split('<br>')]
    lines = [l for l in lines if not re.fullmatch(r'\s*(\(A\)|\(B\)|\(C\))?(\s|\t)*(\(A\)|\(B\)|\(C\))?(\s|\t)*(\(A\)|\(B\)|\(C\))?\s*', l) or not l.strip() == '' and False]
    out = '<br>'.join(l for l in lines if l.strip())
    return out
def ansmark(it): a = it['ans']; return ''.join(CIRC[x] for x in a) if isinstance(a, list) else CIRC[a]
def student_q(it):
    h = '<div class="q%s"><p class="stem"><span class="n">%s.</span> %s</p>' % (' long' if len(it.get('body', '')) > 900 else '', it['n'], it['stem'])
    body = clean(it.get('body', ''))
    if body: h += '<p class="body">%s</p>' % body
    if it.get('kind') == 'write' and '____' not in body:
        big = any(len(b['ans'][0]) > 40 for b in it['blanks'])
        h += '<div class="wl%s">' % (' big' if big else '') + ''.join('<div><span class="lab">%s</span><span></span></div>' % e(b['label'] or '답') for b in it['blanks']) + '</div>'
    elif it.get('kind') != 'write':
        o = it['opts']
        if o != list(CIRC):
            short = all(len(re.sub(r'<[^>]+>', '', x)) <= 3 for x in o)
            h += '<ul class="opts%s">' % (' row' if short else '') + ''.join('<li><span class="optn">%s</span> %s</li>' % (CIRC[i], x) for i, x in enumerate(o)) + '</ul>'
    return h + '</div>'
def paper(t, G, nums):
    its = t['items']; seen = set(); q = []
    for k, it in enumerate(its):
        g = it.get('grp')
        if g is not None and g not in seen:
            seen.add(g); mem = [x['n'] for x in its if x.get('grp') == g]
            gr = G[str(g)]
            q.append('<div class="grp"><p class="gh">[%s~%s] %s</p><p class="psg">%s</p></div>' % (mem[0], mem[-1], e(re.sub(r'\s*\(\d\d번?\)\s*$', '', gr['head'])), e(gr['text']).replace('\n', '<br>')))
        q.append(student_q(it))
    nw = sum(1 for i in its if i.get('kind') == 'write')
    head = ('<div class="hd"><span><b>고1 영어</b> · 중산고 1학년</span><span>2025학년도 9월 고1 전국연합학력평가 %s 변형</span></div>' % nums +
        '<div class="tt"><span class="l">비밀노트 변형문제</span><h1>%s</h1><span class="r">%d문항</span></div>' % (nums, len(its)) +
        '<div class="idrow"><div>학년·반</div><div>1학년 &nbsp; 반</div><div>번호</div><div>번</div><div>이름</div><div></div><div>점수</div><div></div></div>' +
        '<div class="notice"><p><b>※ 유의사항</b> 선택형 %d문항 · 서술형 %d문항. ‘모두 고르시오’ 문항은 정답을 모두 고릅니다.</p><p>답은 데일리 영어 앱 ‘비밀노트 변형문제’ 탭에 같은 번호로 입력해요. 서술형은 시험지에 쓴 답을 그대로 옮겨 적어요.</p></div>' % (len(its) - nw, nw))
    return head + '<div class="cols">' + ''.join(q) + '</div>'
def teacher(t, nums):
    its = t['items']
    rows = []
    for i in range(0, len(its), 12):
        ch = its[i:i + 12]
        rows.append('<tr>%s</tr><tr>%s</tr>' % (''.join('<td>%s</td>' % x['n'] for x in ch) + '<td></td>' * (12 - len(ch)),
                    ''.join('<td>%s</td>' % ('서술' if x.get('kind') == 'write' else ansmark(x)) for x in ch) + '<td></td>' * (12 - len(ch))))
    fixes = [x for x in its if '[수정]' in x.get('ex', '')]
    rule = ('<div class="rule"><p><b>검수에서 고친 곳</b> (비밀노트 원본과 다른 부분 · 앱 채점도 같은 기준)</p>' +
            (''.join('<p>· %s번: %s</p>' % (x['n'], e(re.search(r'\[수정\]\s*(.*)', x['ex']).group(1).split('\n')[0])) for x in fixes) if fixes else '<p>· 없음</p>') + '</div>')
    body = []
    for it in its:
        lines = it['ex'].split('\n')
        if it.get('kind') == 'write':
            top = '%s번 서술형' % it['n']
            lines = ['모범 답안 ▶ ' + ' / '.join(('%s %s' % (b['label'], b['ans'][0])).strip() for b in it['blanks'])] + lines
        else:
            top = '%s번 정답 %s' % (it['n'], ansmark(it))
            lines = [l for l in lines if not l.startswith('정답 ▶')]
        ps = []
        for l in lines:
            if not l.strip(): continue
            m = re.match(r'(모범 답안|이유|오답|포인트|출제 메모|\[원문\])\s*▶?\s*(.*)', l)
            if m:
                lb, tx = m.group(1), m.group(2)
                cls = ' class="fix"' if '[수정]' in tx else ''
                if lb == '출제 메모': ps.append('<p><small><span class="lb">출제 메모</span>%s</small></p>' % e(tx)); continue
                ps.append('<p%s><span class="lb">%s</span>%s</p>' % (cls, lb if lb != '[원문]' else '원문', e(tx)))
            else: ps.append('<p><small>%s</small></p>' % e(l))
        body.append('<div class="ex"><div class="eb">%s<small>%s</small></div>%s</div>' % (top, e(it.get('src') or ''), ''.join(ps)))
    return ('<div class="pg"></div><div class="hd"><span><b>정답 및 해설</b> · 교사용</span><span>비밀노트 변형문제 %s</span></div>' % nums +
            '<div class="tt"><span class="l">비밀노트 변형문제</span><h1>정답 및 해설</h1><span class="r">%s</span></div>' % nums +
            '<table class="key">%s</table>' % ''.join(rows) + rule + '<div class="cols">' + ''.join(body) + '</div>')
import os; os.makedirs(OUT, exist_ok=True)
files = []
with sync_playwright() as p:
    b = p.chromium.launch()
    for t in D['tests']:
        nums = t['title'].replace('비밀노트 변형문제 ', '')
        html = '<!DOCTYPE html><html lang="ko"><head><meta charset="utf-8"><title>%s</title>%s</head><body>' % (t['title'], CSS) + paper(t, D['groups'][t['id']], nums) + teacher(t, nums) + '</body></html>'
        hp = OUT + t['id'] + '.html'; open(hp, 'w', encoding='utf-8').write(html)
        pg = b.new_page(); pg.goto('file://' + hp); pg.wait_for_timeout(300)
        fn = OUT + '중산고1_비밀노트변형_%s.pdf' % nums.replace('·', '-')
        pg.pdf(path=fn, format='A4', print_background=True, prefer_css_page_size=True); pg.close(); files.append(fn)
    b.close()
for f in files: print(f)
