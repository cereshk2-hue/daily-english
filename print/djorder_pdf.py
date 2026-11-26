# 11/26 대진고2 10월 모고 문장 순서(om20~om41) 인쇄용: 지문마다 문장을 섞어 (A)~ 기호, 순서 쓰기 칸 + 뒤에 정답·해석
import json, subprocess, random, html
PK = json.loads(subprocess.check_output(['node', '-e', "global.window={};require('/home/claude/proj/data/h2-ne-oh-L3.js');process.stdout.write(JSON.stringify(window.PKG))"]))
E = lambda s: html.escape(s, quote=False)
L = 'ABCDEFGHIJKLMN'
CSS = """@page{size:A4;margin:14mm 14mm}body{font-family:'Noto Sans KR','Noto Sans CJK KR',sans-serif;font-size:10.5pt;line-height:1.55;color:#111}
h1{font-size:13pt;margin:0 0 2px}.sub{font-size:9pt;color:#555;margin-bottom:8px}.nm{float:right;font-size:9.5pt;font-weight:400}
ol.s{list-style:none;padding:0;margin:0}ol.s li{margin:0 0 7px;padding-left:34px;text-indent:-34px}ol.s b{display:inline-block;width:34px;text-indent:0}
.ans{margin-top:12px;border:1px solid #999;border-radius:6px;padding:8px 10px;font-size:10pt}.pb{page-break-after:always}
table{border-collapse:collapse;width:100%;font-size:9.5pt}td,th{border:1px solid #bbb;padding:4px 6px;vertical-align:top}th{background:#f2f2f2}"""
P, K = [], []
for d in [x for x in PK['days'] if x['id'].startswith('om')]:
    st = d['steps'][0]; lines = st['items'][0]['lines']; ko = {l[1]: l[2] for l in d['passage']}
    no = d['range'].split('10월 ')[1]; rnd = random.Random('dj' + d['id'])
    idx = list(range(len(lines)))
    while True:
        rnd.shuffle(idx)
        if all(idx[i] + 1 != idx[i + 1] for i in range(len(idx) - 1)) and idx[0] != 0: break   # 원문 이웃이 붙어 있지 않게
    lab = {j: L[i] for i, j in enumerate(idx)}
    P.append('<h1>모의고사 문장 순서 · %s <span class="nm">이름 ________ 점수 ____</span></h1><div class="sub">대진고2 · 2026 10월 경기 고2 학평 · %s · 문장 %d개를 글의 순서대로 배열하세요.</div><ol class="s">%s</ol><div class="ans">순서: %s</div>'
             % (E(no), E(d['story'].split(' · ')[2]), len(lines), ''.join('<li><b>(%s)</b>%s</li>' % (L[i], E(lines[j])) for i, j in enumerate(idx)), ' → '.join(['(&nbsp;&nbsp;&nbsp;)'] * len(lines))))
    K.append('<h1>%s · 정답</h1><div class="ans" style="margin:0 0 6px"><b>%s</b></div><table><tr><th style="width:34px">순서</th><th>문장</th><th>해석</th></tr>%s</table>'
             % (E(no), ' → '.join('(%s)' % lab[j] for j in range(len(lines))), ''.join('<tr><td>(%s)</td><td>%s</td><td>%s</td></tr>' % (lab[j], E(lines[j]), E(ko.get(lines[j], ''))) for j in range(len(lines)))))
doc = '<!doctype html><html><head><meta charset="utf-8"><style>%s</style></head><body>%s<div class="pb"></div>%s</body></html>' % (CSS, '<div class="pb"></div>'.join(P), '<div class="pb"></div>'.join(K))
open('/home/claude/out/djmock/djorder.html', 'w', encoding='utf-8').write(doc)
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(); pg.goto('file:///home/claude/out/djmock/djorder.html'); pg.wait_for_timeout(500)
    pg.pdf(path='/home/claude/out/djmock/대진고2_10월모고_문장순서.pdf', format='A4', print_background=True); b.close()
print('ok')
