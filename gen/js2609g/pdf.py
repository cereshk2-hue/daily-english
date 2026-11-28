# 본문 어법 종합 35 인쇄용 (문제 → 정답·해설)
import json, subprocess, re, html, random
random.seed(2609)
from playwright.sync_api import sync_playwright
PK = json.loads(subprocess.check_output(['node', '-e', "global.window={};require('/home/claude/proj/data/h2-mock-2609-jungsan.js');process.stdout.write(JSON.stringify(window.PKG))"]))
d = [x for x in PK['days'] if x['id'] == 'g35'][0]
C = '①②③④⑤'
qh, ah, n = [], [], 0
for st in d['steps']:
    qh.append('<h2>%s</h2><p class="g">%s</p>' % (st['title'], st['guide']))
    for it in st['items']:
        n += 1
        if it.get('keep'): o5, a = it['opts'], it['a']
        else:
            idx = list(range(5)); random.shuffle(idx); o5 = [it['opts'][i] for i in idx]; a = idx.index(0)
        opts = '' if o5[0] == '①' else ''.join('<li><span>%s</span> %s</li>' % (C[i], o) for i, o in enumerate(o5))
        ex = re.sub(r'^정답 ▶ [^\n]*', '정답 ▶ ' + C[a] + ('' if it.get('keep') else ' ' + re.sub('<[^>]+>', '', it['opts'][0])), it['ex'])
        qh.append('<div class="q"><b>%d.</b> %s<ol class="o">%s</ol></div>' % (n, it['q'], opts))
        ah.append('<div class="a"><b>%d. %s</b> %s</div>' % (n, C[a], html.escape(ex).replace('\n', '<br>')))
css = '''@page{size:A4;margin:14mm 12mm}body{font-family:"Noto Sans KR",sans-serif;font-size:10pt;line-height:1.5}h1{font-size:15pt;margin:0 0 4px}h2{font-size:11.5pt;border-bottom:2px solid #333;margin:14px 0 4px;column-span:all}
.g{color:#555;font-size:9pt;margin:0 0 6px;column-span:all}.cols{columns:2;column-gap:8mm}.q{break-inside:avoid;margin:0 0 10px}.q .wbox{border:1px solid #999;padding:5px 7px;margin:4px 0;font-size:9.5pt}.q .wbox p{margin:0 0 3px}
.o{list-style:none;padding:0;margin:3px 0}.o li{margin:1px 0}.o span{margin-right:3px}.a{break-inside:avoid;margin:0 0 7px;font-size:9pt}.pb{break-before:page}'''
doc = '<!doctype html><html><head><meta charset="utf-8"><style>%s</style></head><body><h1>중산고2 9월 모고 본문 어법 종합 35</h1><p class="g">19~24·26·29~42번 본문 문장만으로 · 이름 ________</p><div class="cols">%s</div><div class="pb"></div><h1>정답과 해설</h1><div class="cols">%s</div></body></html>' % (css, ''.join(qh), ''.join(ah))
open('/home/claude/out/js2609g/g35.html', 'w', encoding='utf-8').write(doc)
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(); pg.goto('file:///home/claude/out/js2609g/g35.html'); pg.wait_for_timeout(800)
    pg.pdf(path='/home/claude/out/js2609g/Jungsan_H2_Sep_grammar35.pdf', format='A4', print_background=True); b.close()
from collections import Counter
print(n)
