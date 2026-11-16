# 시험지 보관함: data/*.js 의 tests(OMR 시험) 전부를 PDF(시험지 / 정답·해설)로 만들고
# 선생님 보드 아래 비밀 폴더(t-<board>/<VAULT>/)에 목록 페이지와 함께 놓는다.
# 사용: python3 tools/papers.py [출력 폴더]  (기본: dist/github/<board>/<VAULT>)
# 새 시험지를 만들 때마다 이 스크립트를 다시 돌리면 보관함이 자동으로 채워진다(바뀐 시험만 다시 렌더).
import os, re, sys, json, html, hashlib, subprocess, datetime
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SEC = json.load(open(os.path.join(R, 'tools', 'secrets.json')))
VAULT = 'papers-6mfjk0ggdw'
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(R, 'dist', 'github', SEC['board'], VAULT)
os.makedirs(os.path.join(OUT, 'pdf'), exist_ok=True)
NUM = '①②③④⑤⑥⑦⑧'
E = lambda s: html.escape(str(s))

def load(f):
    return json.loads(subprocess.check_output(['node', '-e', "global.window={};require('%s');process.stdout.write(JSON.stringify(window.PKG))" % f]))

CSS = r'''
@page { size: A4; margin: 14mm 12mm 14mm }
* { box-sizing: border-box }
body { font-family: 'Noto Sans KR', 'Noto Sans CJK KR', 'Apple SD Gothic Neo', sans-serif; font-size: 10pt; line-height: 1.55; color: #111; margin: 0 }
.head { border-bottom: 2px solid #111; padding-bottom: 6px; margin-bottom: 10px; display: flex; justify-content: space-between; align-items: flex-end; gap: 12px }
.head h1 { font-size: 15pt; margin: 0 } .head .sub { font-size: 9pt; color: #444 }
.head .who { font-size: 9.5pt; white-space: nowrap } .head .who span { display: inline-block; width: 26mm; border-bottom: 1px solid #111; margin-left: 4px }
.cols { column-count: 2; column-gap: 7mm; column-rule: 1px solid #ccc }
.ctx { break-inside: avoid; border: 1px solid #999; padding: 6px 8px; margin: 0 0 8px; font-size: 9.5pt }
.ctx-h { font-weight: 700; font-size: 9pt; margin-bottom: 3px }
.q { break-inside: avoid; margin: 0 0 11px }
.stem { font-weight: 700 } .stem .n { display: inline-block; min-width: 1.6em } .src { color: #666; font-weight: 400; font-size: 8.5pt }
.wbox, .wgiven, .wsum, .wcond { border: 1px solid #999; padding: 5px 7px; margin: 5px 0; font-weight: 400 }
.wbox p { margin: 0 0 3px } .wgiven { border-width: 1.5px } .wsum { border-style: dashed } .wcond { font-size: 9pt; border-color: #bbb }
.wblank { display: inline-block; min-width: 5em; border-bottom: 1px solid #111; height: 1em }
.wcols { font-size: 8.5pt; color: #555 } .pt { font-weight: 400; color: #555 } .gap { font-weight: 700 } .tag { font-weight: 700 }
.exam-box { border: 1px solid #999; padding: 5px 7px; margin: 5px 0 }
.opts { margin: 4px 0 0; padding: 0; list-style: none } .opts li { padding-left: 1.4em; text-indent: -1.4em; margin: 1px 0 }
.lines div { border-bottom: 1px solid #999; height: 7mm }
.key { width: 100%; border-collapse: collapse; margin: 0 0 12px; font-size: 9.5pt; text-align: center }
.key td, .key th { border: 1px solid #999; padding: 3px 2px } .key th { background: #f0f0f0 }
.ex { break-inside: avoid; margin: 0 0 9px; font-size: 9pt } .ex b.a { color: #b00 }
.ex .t { white-space: pre-wrap }
.foot { position: fixed; bottom: -9mm; left: 0; right: 0; text-align: center; font-size: 8pt; color: #888 }
'''

def ans_txt(it):
    a = it.get('ans')
    if isinstance(a, list): return ', '.join(NUM[x] if isinstance(x, int) and x < len(NUM) else str(x) for x in a)
    if isinstance(a, int): return NUM[a] if a < len(NUM) else str(a + 1)
    if it.get('kind') == 'write': return it.get('model', '서술형')
    return str(a)

def sheet(P, t, answers):
    sub = ' · '.join(x for x in [P.get('school', ''), P.get('unit', ''), P.get('title', '')] if x)
    h = ['<!doctype html><html lang="ko"><meta charset="utf-8"><style>%s</style><body>' % CSS,
         '<div class="head"><div><h1>%s%s</h1><div class="sub">%s%s</div></div><div class="who">%s</div></div>' % (
             E(t['title']), ' · 정답과 해설' if answers else '', E(sub), (' · %s분 · %d문항' % (t['minutes'], len(t['items'])) if t.get('minutes') else ' · %d문항' % len(t['items'])),
             '' if answers else '이름<span></span>&nbsp; 점수<span style="width:16mm"></span>')]
    if answers:
        mc = [it for it in t['items'] if it.get('kind') != 'write']
        rows = [mc[i:i + 10] for i in range(0, len(mc), 10)]
        if rows:
            h.append('<table class="key">' + ''.join('<tr><th>번호</th>%s</tr><tr><th>정답</th>%s</tr>' % (''.join('<td>%s</td>' % E(it['n']) for it in r), ''.join('<td>%s</td>' % E(ans_txt(it)) for it in r)) for r in rows) + '</table>')
        h.append('<div class="cols">')
        for it in t['items']:
            ex = it.get('ex', '')
            h.append('<div class="ex"><b>%s.</b> <b class="a">%s</b> <span class="src">%s</span><div class="t">%s</div></div>' % (
                E(it['n']), E(ans_txt(it)), E(it.get('src', '')), ex.replace('\n', '<br>')))
        h.append('</div>')
    else:
        h.append('<div class="cols">')
        last = None
        for it in t['items']:
            ctx = it.get('ctx') or ''
            if ctx and ctx != last:
                h.append('<div class="ctx">%s</div>' % ctx)
            last = ctx or last if ctx else last
            q = ['<div class="q"><div class="stem"><span class="n">%s.</span> %s <span class="src">%s</span></div>' % (E(it['n']), it.get('stem', ''), E(it.get('src', '')))]
            if it.get('body'): q.append(it['body'])
            if it.get('opts'): q.append('<ul class="opts">%s</ul>' % ''.join('<li>%s %s</li>' % (NUM[i], o) for i, o in enumerate(it['opts'])))
            if it.get('kind') == 'write':
                n = max(2, len(it.get('blanks') or []))
                q.append('<div class="lines">%s</div>' % ''.join('<div></div>' for _ in range(n)))
            q.append('</div>')
            h.append(''.join(q))
        h.append('</div>')
    h.append('</body></html>')
    return '\n'.join(h)

# ---- 1) 시험 모으기
units = []
for f in sorted(os.listdir(os.path.join(R, 'data'))):
    if not f.endswith('.js'): continue
    P = load(os.path.join(R, 'data', f))
    if not P.get('tests'): continue
    folder = next((d for d in os.listdir(os.path.join(R, 'dist', 'github')) if d.startswith(f[:-3] + '-')), '')
    units.append((f[:-3], folder, P))

# ---- 2) PDF 만들기 (내용이 바뀐 시험만)
from playwright.sync_api import sync_playwright
mf_path = os.path.join(OUT, 'manifest.json')
old = json.load(open(mf_path)) if os.path.exists(mf_path) else {}
mf, todo = {}, []
for uid, folder, P in units:
    for t in P['tests']:
        key = '%s__%s' % (uid, t['id'])
        hsh = hashlib.md5(json.dumps([P.get('school'), P.get('unit'), P.get('title'), t], ensure_ascii=False, sort_keys=True).encode()).hexdigest()[:12]
        mf[key] = {'hash': hsh, 'made': old.get(key, {}).get('made') if old.get(key, {}).get('hash') == hsh else None}
        files = [os.path.join(OUT, 'pdf', key + s) for s in ('-q.pdf', '-a.pdf')]
        if mf[key]['made'] is None or not all(os.path.exists(x) for x in files): todo.append((key, P, t, files))
print('시험 %d개 · 새로 렌더 %d개' % (len(mf), len(todo)))
if todo:
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page()
        for key, P, t, files in todo:
            for ans, path in ((False, files[0]), (True, files[1])):
                pg.set_content(sheet(P, t, ans), wait_until='load')
                pg.pdf(path=path, format='A4', print_background=True, prefer_css_page_size=True,
                       display_header_footer=True, header_template='<span></span>',
                       footer_template='<div style="font-size:7pt;width:100%%;text-align:center;color:#888">%s · <span class="pageNumber"></span>/<span class="totalPages"></span></div>' % E(t['title']))
            mf[key]['made'] = datetime.date.today().isoformat()
        b.close()
for k in list(old):
    if k not in mf:
        for s in ('-q.pdf', '-a.pdf'):
            try: os.remove(os.path.join(OUT, 'pdf', k + s))
            except FileNotFoundError: pass
json.dump(mf, open(mf_path, 'w'), ensure_ascii=False, indent=1)

# ---- 3) 목록 페이지
def grade_of(uid):
    m = re.match(r'(m|h)(\d)', uid); return ('중' if m.group(1) == 'm' else '고') + m.group(2) if m else ''
cards = []
for uid, folder, P in sorted(units, key=lambda x: (x[0][0] != 'm', x[0])):
    rows = []
    for t in P['tests']:
        key = '%s__%s' % (uid, t['id'])
        nw = sum(1 for it in t['items'] if it.get('kind') == 'write')
        cnt = '%d문항' % len(t['items']) + (' (서술형 %d)' % nw if nw else '')
        rows.append('<tr><td><b>%s</b><small>%s</small></td><td>%s</td><td class="d">%s</td><td class="b"><a href="pdf/%s-q.pdf" target="_blank">시험지</a><a class="a" href="pdf/%s-a.pdf" target="_blank">정답·해설</a></td></tr>' % (
            E(t['title']), E(' · %s분' % t['minutes'] if t.get('minutes') else ''), cnt, E(mf[key]['made'] or ''), E(key), E(key)))
    days = [d for d in P['days']]
    dl = ''.join('<li><b>%s</b> %s</li>' % (E(d['name']), E(d.get('range', ''))) for d in days)
    g = grade_of(uid); sc = P.get('school', '')
    head = ' · '.join(x for x in [g if not sc.startswith(g) else '', sc, P.get('unit', '')] if x)
    cards.append('<section class="u" data-q="%s"><h2>%s</h2><p class="t">%s</p>'
                 '<table><thead><tr><th>시험지 (앱 맨 아래 OMR)</th><th>문항</th><th>만든 날</th><th></th></tr></thead><tbody>%s</tbody></table>'
                 '<details><summary>데일리 DAY %d개 · 어디까지 만들었는지 보기</summary><ol>%s</ol></details></section>' % (
                     E((head + ' ' + P.get('title', '') + ' ' + ' '.join(t['title'] for t in P['tests'])).lower()), E(head), E(P.get('title', '')), ''.join(rows), len(days), dl))
total = sum(len(P['tests']) for _, _, P in units)
page = '''<!doctype html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow">
<title>시험지 보관함</title><style>
body{margin:0;font-family:'Pretendard','Noto Sans KR','Apple SD Gothic Neo',sans-serif;background:#f6f5f2;color:#1c1b19}
header{background:#1c1b19;color:#fff;padding:22px 18px 18px}header h1{margin:0;font-size:22px}header p{margin:6px 0 0;font-size:13px;opacity:.8}
header .bar{font-size:12px;background:#b3261e;display:inline-block;padding:3px 8px;border-radius:6px;margin-bottom:10px}
header a{color:#fff}.wrap{max-width:900px;margin:0 auto;padding:14px}
input{width:100%;box-sizing:border-box;font:inherit;padding:12px 14px;border:1.5px solid #ddd;border-radius:12px;margin:4px 0 12px}
.u{background:#fff;border-radius:16px;padding:16px;margin:0 0 14px;box-shadow:0 1px 3px rgba(0,0,0,.06)}
.u h2{margin:0;font-size:17px}.u .t{margin:2px 0 10px;color:#666;font-size:13px}
table{width:100%;border-collapse:collapse;font-size:14px}th{text-align:left;font-size:12px;color:#888;font-weight:600;padding:4px 6px;border-bottom:1px solid #eee}
td{padding:9px 6px;}td:nth-child(2){white-space:nowrap}td{border-bottom:1px solid #f0efec;vertical-align:middle}td small{color:#888;margin-left:4px}td.d{color:#888;font-size:12px;white-space:nowrap}
td.b{white-space:nowrap;text-align:right}td.b a{display:inline-block;padding:6px 10px;border-radius:9px;background:#1c1b19;color:#fff;text-decoration:none;font-size:13px;margin-left:4px}
td.b a.a{background:#fff;color:#1c1b19;border:1.5px solid #1c1b19}
details{margin-top:10px;font-size:13px}summary{cursor:pointer;color:#555}ol{columns:2;margin:8px 0 0;padding-left:0;list-style:none}ol li{padding:2px 0}
@media(max-width:600px){th:nth-child(3),td.d{display:none}td.b a{display:block;margin:3px 0;text-align:center}ol{columns:1}}
</style></head><body><header><div class="bar">선생님 전용 · 정답이 들어 있어요. 학생에게 이 주소는 주지 마세요</div><h1>시험지 보관함</h1>
<p>단원 @U@개 · 시험지 @T@개 · 앱 맨 아래 OMR로 답을 입력하는 시험들 · 마지막 정리 @D@</p><p><a href="../">← 데일리 영어 보드</a> &nbsp;·&nbsp; <a href="setup-grid.html">학생별 진도표 켜기 안내</a></p></header>
<div class="wrap"><input id="s" placeholder="학교·단원·번호로 찾기 (예: 중산고1, 끝판왕, 너른터)">@C@</div>
<script>document.getElementById('s').addEventListener('input',function(e){var v=e.target.value.trim().toLowerCase();document.querySelectorAll('.u').forEach(function(u){u.style.display=!v||u.dataset.q.indexOf(v)>=0?'':'none'})})</script>
</body></html>'''.replace('@U@', str(len(units))).replace('@T@', str(total)).replace('@D@', datetime.date.today().isoformat()).replace('@C@', ''.join(cards))
open(os.path.join(OUT, 'index.html'), 'w', encoding='utf-8').write(page)
print('보관함:', OUT, '· 단원', len(units), '· 시험지', total)
