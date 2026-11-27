# 11/27 대화문 꿰뚫기 인쇄용 학습지: 과 데이터(l5.py …) → 대화 순서(섞기)·우리말 보고 영작·빈칸 쓰기·T/F·객관식 + 정답
import sys, html, random, importlib
sys.path.insert(0, '/home/claude/srcrepo/gen/m1dlg')
L = sys.argv[1] if len(sys.argv) > 1 else 'l5'; M = importlib.import_module(L)
E = lambda s: html.escape(s, quote=False)
CSS = """@page{size:A4;margin:13mm 14mm}body{font-family:'Noto Sans KR','Noto Sans CJK KR',sans-serif;font-size:10pt;line-height:1.55;color:#111}
h1{font-size:14pt;margin:0 0 2px}h2{font-size:11pt;margin:12px 0 5px;border-bottom:1.5px solid #333;padding-bottom:2px}.sub{font-size:8.8pt;color:#555;margin-bottom:6px}.nm{float:right;font-size:9pt;font-weight:400}
.en{font-family:'Noto Serif','Noto Serif CJK KR',serif}ol{margin:3px 0 3px 20px;padding:0}li{margin:0 0 5px}.ln{border-bottom:1px solid #999;height:17px;margin:2px 0 7px}.box{border:1px solid #999;border-radius:5px;padding:5px 9px;margin:4px 0 8px}
.pb{page-break-after:always}.opt{display:block;margin-left:10px}.k{font-size:9.3pt}.k li{margin:0 0 3px}"""
C = '①②③④⑤'; P, K = [], []
import json, subprocess
_pk = json.loads(subprocess.check_output(['node', '-e', "global.window={};require('%s')" % getattr(M, 'UNIT', '/home/claude/proj/data/m1-donga-yoon-L6.js') + ";process.stdout.write(JSON.stringify(window.PKG.days))"]))
D = {d['id']: [l for l in d['passage'] if l[0] != '#'] for d in _pk}
for gid, c in M.DLG.items():
    rnd = random.Random(gid); h = '<h1>%s <span class="nm">이름 ________</span></h1><div class="sub">%s · 대화문 꿰뚫기 학습지</div>' % (E(c['range']), '발산중2 비상(황종배)' if L.startswith('v') else '중산중1 동아(윤정미)')
    h += '<h2>1. 대화 순서 맞추기</h2>'; key = []
    for name, lines, flow in c['order']:
        idx = list(range(len(lines)))
        while True:
            rnd.shuffle(idx)
            if idx != sorted(idx): break
        lab = 'ABCDEFGHIJ'
        h += '<div class="box"><b>%s</b>%s<div>순서: %s</div></div>' % (E(name), ''.join('<div class="en">(%s) %s</div>' % (lab[i], E(lines[j])) for i, j in enumerate(idx)), ' → '.join(['(　)'] * len(lines)))
        key.append('%s: %s' % (name, ' → '.join('(%s)' % lab[idx.index(j)] for j in range(len(lines)))))
    h += '<h2>2. 우리말을 보고 영어로 쓰기</h2><ol>' + ''.join('<li>%s<div class="ln"></div></li>' % E(ko) for ko, en in c['scr']) + '</ol>'
    h += '<h2>3. 빈칸에 알맞은 말 쓰기</h2><ol>' + ''.join('<li class="en">%s <small>(%s)</small></li>' % (E(s).replace('___', '__________'), E(v)) for s, v, a in c['verb']) + '</ol>'
    # 11/27 선생님: 대화문 없이 심경·내용을 물으면 모름 → 4·5번은 새 쪽에 대화문을 먼저 싣고 문제(1~3번 답이 보이지 않게 쪽을 나눔)
    tfn = getattr(M, 'TFN', {}).get(gid)
    dl = []
    for name, lines, flow in c['order']:
        sp = [l for l in D[c['src']] if l[1] in lines]
        dl.append('<div class="box"><b>%s</b>%s</div>' % (E(name), ''.join('<div class="en">%s: %s</div>' % (E(x[0]), E(x[1])) for x in sp)))
    h += '<div class="pb"></div><h1>%s · 대화 보고 풀기 <span class="nm">이름 ________</span></h1><div class="sub">아래 대화를 읽고 4·5번을 풀어요.</div>' % E(c['range']) + ''.join(dl)
    h += '<h2>4. 대화 내용과 맞으면 T, 틀리면 F</h2><ol>' + ''.join('<li class="en">%s%s ( T / F )</li>' % (('[대화 %d] ' % tfn[i]) if tfn else '', E(s)) for i, (s, b, ev, why) in enumerate(c['tf'])) + '</ol>'
    h += '<h2>5. 알맞은 답 고르기</h2><ol>'; mk = []
    for q, opts, why in c['mc']:
        o = opts[:]; rnd.shuffle(o); mk.append(C[o.index(opts[0])])
        h += '<li>%s%s</li>' % (q, ''.join('<span class="opt">%s %s</span>' % (C[i], E(x)) for i, x in enumerate(o)))
    h += '</ol>'; P.append(h)
    K.append('<h1>%s · 정답</h1><h2>1. 대화 순서</h2><div class="k">%s</div><h2>2. 영작</h2><ol class="k en">%s</ol><h2>3. 빈칸</h2><ol class="k en">%s</ol><h2>4. T/F</h2><ol class="k">%s</ol><h2>5. 객관식</h2><div class="k">%s</div>'
             % (E(c['range']), '<br>'.join(E(x) for x in key), ''.join('<li>%s</li>' % E(en) for ko, en in c['scr']), ''.join('<li>%s</li>' % E(' / '.join(a)) for s, v, a in c['verb']),
                ''.join('<li>%s — %s</li>' % ('T' if b else 'F', E(why)) for s, b, ev, why in c['tf']), ' '.join('%d) %s' % (i + 1, m) for i, m in enumerate(mk))))
doc = '<!doctype html><html><head><meta charset="utf-8"><style>%s</style></head><body>%s<div class="pb"></div>%s</body></html>' % (CSS, '<div class="pb"></div>'.join(P), '<div class="pb"></div>'.join(K))
out = '/home/claude/out/m1dlg/' + M.PDF[0]
open(out + '.html', 'w', encoding='utf-8').write(doc)
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(); pg.goto('file://' + out + '.html'); pg.wait_for_timeout(400); pg.pdf(path=out + '.pdf', format='A4', print_background=True); b.close()
print(out + '.pdf')
