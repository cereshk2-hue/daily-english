# 11/25 발산중2 외부지문 어법·어휘 한 판 인쇄용 PDF (문제지 + 정답·해설) — gen_bsext.py의 R1·R2를 그대로 씀
import re, html, sys, types
src = open('/home/claude/srcrepo/generators/gen_bsext.py', encoding='utf-8').read()
g = {}; exec(src[:src.index('PLAIN =')].replace("PK = json.loads", "PK = None and json.loads"), g)
R1, R2 = g['R1'], g['R2']
E = lambda s: html.escape(s, quote=False)
def q(s, n):
    out = []
    def f(m):
        o = m.group(1).split('|'); n[0] += 1
        a, b = (o[0], o[1]) if n[0] % 2 else (o[1], o[0])
        return '<span class="br"><sup>%d</sup>( %s / %s )</span>' % (n[0], E(a), E(b))
    return re.sub(r'\{([^}]*)\}', f, E(s).replace('&quot;', '"'))
def ans(R):
    rows, k = [], 0
    for s, ex in R:
        for m in re.findall(r'\{([^}]*)\}', s): k += 1; rows.append('<td>%d</td><td><b>%s</b></td><td class="x">%s</td>' % (k, E(m.split('|')[0]), E(m.split('|')[1])))
    return rows
CSS = """@page{size:A4;margin:12mm} body{font-family:'Noto Sans KR',sans-serif;font-size:12.5px;color:#111}
h1{font-size:19px;margin:0 0 2px} .sub{color:#555;margin-bottom:10px} .nm{float:right;font-size:12px}
.pass{font-size:14px;line-height:2.25;border:1px solid #999;padding:10px 14px;border-radius:6px}
.br{white-space:nowrap;font-weight:600;color:#1b3a6b} sup{font-size:9px;color:#c00;margin-right:1px}
table{border-collapse:collapse;width:100%;font-size:12px} td,th{border:1px solid #bbb;padding:3px 6px} .x{color:#888;text-decoration:line-through}
.ex{font-size:12px;line-height:1.7;margin:4px 0 0 0;padding-left:16px} .pb{page-break-before:always} h2{font-size:15px;margin:14px 0 6px}"""
def page(i, title, R):
    n = [0]; body = ' '.join(q(s, n) for s, _ in R)
    return '<h1>외부지문 %d · 어법·어휘 한 판 <span class="nm">이름 ________ 점수 ____ / %d</span></h1><div class="sub">발산중2 · Reading Material %d · %s · 괄호 안에서 어법·문맥에 맞는 것에 ○ 하세요.</div><div class="pass">%s</div>' % (i, n[0], i, title, body)
def key(i, title, R):
    rows = ans(R); half = (len(rows) + 1) // 2
    t = '<table><tr><th>번호</th><th>정답</th><th>오답</th><th>번호</th><th>정답</th><th>오답</th></tr>' + ''.join('<tr>%s%s</tr>' % (rows[j], rows[j + half] if j + half < len(rows) else '<td></td><td></td><td></td>') for j in range(half)) + '</table>'
    exs = '<ol class="ex">' + ''.join('<li>%s<br><span style="color:#444">%s</span></li>' % (E(re.sub(r'\{([^|}]*)\|[^}]*\}', r'[\1]', s)), E(ex)) for s, ex in R) + '</ol>'
    return '<div class="pb"></div><h1>외부지문 %d · 정답과 해설</h1><div class="sub">Reading Material %d · %s</div>%s<h2>문장별 해설</h2>%s' % (i, i, title, t, exs)
H = '<!doctype html><html><head><meta charset="utf-8"><style>%s</style></head><body>' % CSS
doc = H + page(1, '나라별 대화 방식 (스포츠 비유)', R1) + '<div class="pb"></div>' + page(2, '우주 비행사의 사인 보험', R2) + key(1, '나라별 대화 방식', R1) + key(2, '우주 비행사의 사인 보험', R2) + '</body></html>'
open('/home/claude/out/bsext/bsext.html', 'w', encoding='utf-8').write(doc)
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(); pg.goto('file:///home/claude/out/bsext/bsext.html'); pg.wait_for_timeout(500)
    pg.pdf(path='/home/claude/out/bsext/발산중2_외부지문_어법어휘한판.pdf', format='A4', print_background=True); b.close()
print('ok')
