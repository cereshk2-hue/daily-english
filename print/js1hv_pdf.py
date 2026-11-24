# 11/24 중산고1 끝판왕 어휘 심화 DAY 62~65 인쇄본: ① 어휘표(뜻·숨은 뜻 함정·끝판왕 문장·해석) ② 확인 테스트(뜻 쓰기 + 한 끗 함정) ③ 정답
import json, subprocess, re, html, sys
from playwright.sync_api import sync_playwright
DATA = '/home/claude/proj/data/h1-mock-2509.js'
OUT = '/home/claude/out/js1hv/'
PK = json.loads(subprocess.check_output(['node', '-e', "global.window={};require('%s');process.stdout.write(JSON.stringify(window.PKG))" % DATA]))
E = html.escape
CSS = """@page{size:A4;margin:13mm 12mm}body{font-family:'Noto Sans CJK KR','Noto Sans KR',sans-serif;font-size:9.6pt;color:#111}
h1{font-size:14pt;margin:0 0 2mm}h2{font-size:11pt;margin:4mm 0 2mm;border-bottom:1.5px solid #333}.sub{color:#555;font-size:8.6pt;margin-bottom:3mm}
table{border-collapse:collapse;width:100%}td,th{border:1px solid #aaa;padding:1.3mm 1.6mm;vertical-align:top}th{background:#eee;font-size:8.6pt}
.en{font-family:'Noto Serif','Times New Roman',serif}.w{font-weight:700;white-space:nowrap}.tr{color:#b00;font-size:8.4pt}.ko{color:#444;font-size:8.4pt}
.brk{page-break-before:always}.q{margin:0 0 2.4mm;line-height:1.55}.blank{display:inline-block;min-width:38mm;border-bottom:1px solid #333}
.two{columns:2;column-gap:7mm}.two .q{break-inside:avoid}"""
def tr_of(d, w):
    for q in d['steps'][1]['items']:
        if '<b class="en">%s</b>' % w in q['q']: return q['opts'][1]
    return ''
def sent_of(d, w):
    for r in d['passage']:
        if r[0] != '#' and re.search(r'(?<![A-Za-z])%s(?![A-Za-z])' % re.escape(w), r[1]): return r[1], r[2]
    return '', ''
def trapinfo(d, w):
    for st in d['steps'][4:]:
        for q in st['items']:
            if q['q'].startswith('<b class="en">%s</b>' % w):
                m = re.search(r'끝판왕 문장\((.*?)번\) ▶ (.*)\n해석: (.*)\n이 자리의 정답은 (.*?)\(', q['ex'])
                return m.groups()
    return None
def B(s, w): return re.sub(r'(?<![A-Za-z])(%s)(?![A-Za-z])' % re.escape(E(w)), r'<b>\1</b>', E(s), count=1)
def page(d, ans=False):
    cards = d['steps'][0]['items']; picks = d['steps'][3]['items']
    t = '<h1>%s · %s</h1><div class="sub">중산고1 9월 모고 요약문 끝판왕 정답·함정 선택지 어휘 %d개 · 빨간 글씨 = 흔히 아는 뜻(함정) · 함정 선택지 어휘는 정답 자리 문장과 함께</div>' % (E(d['name']), E(d['range']), len(cards))
    if not ans:
        t += '<h2>① 어휘표</h2><table><tr><th>#</th><th>어휘</th><th>이 문장 속 뜻</th><th>끝판왕 문장 · 해석</th></tr>'
        for i, c in enumerate(cards, 1):
            if len(c) < 4:
                n_, en_, ko_, cw = trapinfo(d, c[0])
                t += '<tr><td>%d</td><td class="w en">%s</td><td>%s</td><td><span class="tr">%s번 함정 선택지 · 이 자리 정답은 <b class="en">%s</b></span></td></tr>' % (i, E(c[0]), E(c[1]), n_, E(cw))
                continue
            en, ko = sent_of(d, c[3]); trp = tr_of(d, c[0])
            t += '<tr><td>%d</td><td class="w en">%s</td><td>%s%s</td><td><span class="en">%s</span><br><span class="ko">%s</span></td></tr>' % (
                i, E(c[0]), E(c[1]), ('<br><span class="tr">✗ %s</span>' % E(trp)) if trp else '', B(en, c[3]), E(ko))
        t += '</table>'
        t += '<div class="brk"></div><h1>%s 확인 테스트</h1><div class="sub">이름: ____________ &nbsp; 점수: ____ / %d</div>' % (E(d['name']), len(cards) + len(picks))
        t += '<h2>② 이 문장 속 뜻 쓰기</h2><div class="two">'
        for i, c in enumerate(cards, 1): t += '<div class="q">%d. <b class="en">%s</b> <span class="blank"></span></div>' % (i, E(c[0]))
        t += '</div><h2>③ 한 끗 함정: 문맥에 맞는 말에 ○</h2>'
        for i, p in enumerate(picks, 1):
            m = re.search(r'\{([^|}]*)\|([^}]*)\}', p['s']); a, b = m.group(1), m.group(2)
            o = sorted([a, b])
            t += '<div class="q en">%d. %s</div>' % (i, E(p['s'][:m.start()]) + '( <b>%s</b> / <b>%s</b> )' % (E(o[0]), E(o[1])) + E(p['s'][m.end():]))
    else:
        t += '<h2>② 뜻 쓰기 정답</h2><div class="two">' + ''.join('<div class="q">%d. <b class="en">%s</b> %s</div>' % (i, E(c[0]), E(c[1])) for i, c in enumerate(cards, 1)) + '</div>'
        t += '<h2>③ 한 끗 함정 정답</h2>'
        for i, p in enumerate(picks, 1):
            m = re.search(r'\{([^|}]*)\|([^}]*)\}', p['s']); ex = p['ex'].split('\n')
            t += '<div class="q">%d. <b class="en">%s</b> (✗ %s) — %s<br><span class="ko">%s</span></div>' % (i, E(m.group(1)), E(m.group(2)), E(ex[0].split('(', 1)[1].rstrip(')')), E(ex[-1].replace('포인트 ▶ ', '')))
    return t
H = [d for d in PK['days'] if re.match(r'hv\d+$', d['id'])]
import os; os.makedirs(OUT, exist_ok=True)
with sync_playwright() as p:
    b = p.chromium.launch()
    for kind, ans in (('어휘표_테스트', False), ('정답', True)):
        body = '<div class="brk"></div>'.join(page(d, ans) for d in H)
        pg = b.new_page(); pg.set_content('<html><head><meta charset="utf-8"><style>%s</style></head><body>%s</body></html>' % (CSS, body))
        f = OUT + '중산고1_끝판왕어휘심화_DAY62-65_%s.pdf' % kind; pg.pdf(path=f, format='A4', print_background=True); print(f)
    b.close()
