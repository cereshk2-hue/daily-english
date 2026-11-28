# 미래엔 L4 고난도 세트 1·2 인쇄용 (문제 → 정답·해설), 보기 순서는 시드 고정 섞기
import json, subprocess, re, html, random
random.seed(428)
from playwright.sync_api import sync_playwright
PK = json.loads(subprocess.check_output(['node', '-e', "global.window={};require('/home/claude/proj/data/h2-mirae-kim-L4.js');process.stdout.write(JSON.stringify(window.PKG))"]))
C = '①②③④⑤'
qh, ah, n = [], [], 0
for d in [x for x in PK['days'] if x['id'] in ('hs1', 'hs2')]:
    qh.append('<h1 class="set">%s</h1>' % d['range']); ah.append('<h2>%s</h2>' % d['range'].split(' (')[0])
    for st in d['steps']:
        qh.append('<h2>%s</h2><p class="g">%s</p>' % (st['title'], st['guide']))
        for it in st['items']:
            n += 1
            if st['type'] == 'insert':
                g = it['lines'][it['given']]; rest = [l for j, l in enumerate(it['lines']) if j != it['given']]
                body = ' '.join('%s ( %s )' % (html.escape(l), C[k]) for k, l in enumerate(rest))
                qh.append('<div class="q"><b>%d.</b> 글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳은?<div class="given">%s</div><div class="wbox">%s</div></div>' % (n, html.escape(g), body))
                ah.append('<div class="a"><b>%d. %s</b> %s</div>' % (n, C[it['given'] - 1], html.escape(it['ex']).replace('\n', '<br>')))
                continue
            if it.get('keep'): o5, a = it['opts'], it['a']
            else:
                idx = list(range(5)); random.shuffle(idx); o5 = [it['opts'][i] for i in idx]; a = idx.index(0)
            opts = '' if o5[0] == '①' else ''.join('<li><span>%s</span> %s</li>' % (C[i], o) for i, o in enumerate(o5))
            ex = re.sub(r'^정답 ▶ [^\n]*', '정답 ▶ ' + C[a] + ('' if it.get('keep') else ' ' + re.sub('<[^>]+>', '', it['opts'][0])), it['ex'])
            qh.append('<div class="q"><b>%d.</b> %s<ol class="o">%s</ol></div>' % (n, it['q'], opts))
            ah.append('<div class="a"><b>%d. %s</b> %s</div>' % (n, C[a], html.escape(ex).replace('\n', '<br>')))
css = '''@page{size:A4;margin:14mm 12mm}body{font-family:"Noto Sans KR",sans-serif;font-size:10pt;line-height:1.5}h1{font-size:15pt;margin:0 0 4px}h1.set{column-span:all;margin-top:10px;background:#eee;padding:3px 6px;font-size:12.5pt}h2{font-size:11.5pt;border-bottom:2px solid #333;margin:14px 0 4px;column-span:all}
.g{color:#555;font-size:9pt;margin:0 0 6px;column-span:all}.cols{columns:2;column-gap:8mm}.q{break-inside:avoid;margin:0 0 10px}.wbox{border:1px solid #999;padding:5px 7px;margin:4px 0;font-size:9.5pt}.wbox p{margin:0 0 3px}.given{border:1.5px solid #333;padding:4px 7px;margin:4px 0;font-size:9.5pt}
.o{list-style:none;padding:0;margin:3px 0}.o li{margin:1px 0}.o span{margin-right:3px}.a{break-inside:avoid;margin:0 0 7px;font-size:9pt}.pb{break-before:page}'''
doc = '<!doctype html><html><head><meta charset="utf-8"><style>%s</style></head><body><h1>중산고2 미래엔(김성연) L4 What-If Science 고난도 2세트</h1><p class="g">순서 · 삽입 · 어휘 상(다의어) · 본문 문법 · 이름 ________</p><div class="cols">%s</div><div class="pb"></div><h1>정답과 해설</h1><div class="cols">%s</div></body></html>' % (css, ''.join(qh), ''.join(ah))
open('/home/claude/out/mirae4h/hs.html', 'w', encoding='utf-8').write(doc)
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(); pg.goto('file:///home/claude/out/mirae4h/hs.html'); pg.wait_for_timeout(800)
    pg.pdf(path='/home/claude/out/mirae4h/Jungsan_H2_Miraen_L4_hard2sets.pdf', format='A4', print_background=True); b.close()
print(n)
