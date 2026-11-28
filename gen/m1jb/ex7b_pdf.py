# 족보 7과 최다오답 공략(01) 친절한 해설지 PDF
import sys, html
sys.path.insert(0, '/home/claude/srcrepo/gen/m1jb')
from ex7b import EX
from playwright.sync_api import sync_playwright
C = '①②③④⑤'
ANS = {1: [2, 5], 2: 2, 3: 2, 4: 4, 5: 3, 6: 3, 7: 2, 8: [2, 5], 9: [3, 4], 10: [1, 5], 11: 3, 12: [3, 5], 13: 4, 14: 4, 15: 5, 16: 2, 17: 2, 18: [2, 4], 19: [1, 4], 20: [2, 5]}
e = html.escape
def mark(a): return ''.join(C[x - 1] for x in a) if isinstance(a, list) else C[a - 1]
rows = []
for n in range(1, 21):
    core, notes, point = EX[n]; lab = ['·'] * 5 if n in (7, 11, 13, 14) else list(C)
    li = ''.join('<li class="%s"><b>%s</b> %s</li>' % ('ok' if '✔' in x[:3] else ('no' if '✘' in x[:3] else ''), l, e(x)) for l, x in zip(lab, notes))
    rows.append('<div class="q"><div class="h"><span class="n">%d번</span><span class="a">정답 %s</span></div><p class="c"><b>핵심</b> %s</p><ul>%s</ul><p class="p"><b>포인트</b> %s</p></div>' % (n, mark(ANS[n]), e(core), li, e(point)))
key = ''.join('<td><b>%d</b><br>%s</td>' % (n, mark(ANS[n])) for n in range(1, 21))
doc = '''<!doctype html><html><head><meta charset="utf-8"><style>@page{size:A4;margin:13mm 12mm}body{font-family:"Noto Sans KR",sans-serif;font-size:9.6pt;line-height:1.55;color:#222}
h1{font-size:15pt;margin:0}.sub{color:#666;font-size:9pt;margin:2px 0 8px}table{border-collapse:collapse;width:100%%;margin:0 0 10px}td{border:1px solid #bbb;text-align:center;padding:3px 0;font-size:9pt}
.cols{columns:2;column-gap:7mm}.q{break-inside:avoid;border:1px solid #c9cfe0;border-radius:8px;padding:7px 9px;margin:0 0 9px}.h{display:flex;justify-content:space-between;border-bottom:1px solid #e1e5f0;padding-bottom:3px;margin-bottom:4px}
.n{font-weight:800;color:#2b4bb8;font-size:11pt}.a{font-weight:800;color:#c8372d}.c{margin:2px 0 4px}.c b,.p b{background:#eef2ff;color:#2b4bb8;border-radius:4px;padding:0 4px;margin-right:4px;font-size:8.5pt}
ul{list-style:none;padding:0;margin:0}li{margin:2px 0;padding-left:1.4em;text-indent:-1.4em}li.ok{color:#1d6b3a}li.no{color:#333}.p{margin:5px 0 0;font-size:9pt;background:#fffbe8;border-radius:5px;padding:3px 6px}</style></head><body>
<h1>족보 7과 최다오답 공략 (01) · 친절한 해설지</h1><div class="sub">중산중1 동아(윤정미) 7. Find Your Dream · 20문항 · 선지마다 해석과 맞고 틀린 이유</div>
<table><tr>%s</tr></table><div class="cols">%s</div></body></html>''' % (key, ''.join(rows))
open('/home/claude/out/m1jb/ex7b.html', 'w', encoding='utf-8').write(doc)
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(); pg.goto('file:///home/claude/out/m1jb/ex7b.html'); pg.wait_for_timeout(800)
    pg.pdf(path='/home/claude/out/m1jb/Jungsan_M1_L7_choda_explained.pdf', format='A4', print_background=True); b.close()
print('ok')
