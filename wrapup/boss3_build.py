# 11/12 안곡고2 요약문 끝판왕 (boss2_build.py 복사 · boss3_data)
# 요약문 끝판왕 챌린지: boss_data.py → ① 앱 시험(P.tests, kind 'boss') ② A4 시험지(학생용·교사용) HTML → PDF
import re, json, html, subprocess, sys
sys.path.insert(0, '/home/claude/srcrepo/wrapup')
from boss3_data import SETS, MEAN, EXTRA, M, TR
C = '①②③④⑤'
esc = lambda s: html.escape(s, quote=False)
DATA = '/home/claude/proj/data/h2-mock-2609-angok.js'
OUT = '/home/claude/work/wrapup/boss3/'

def word_mean(w): return M(w) or EXTRA.get(w, '')

def autofix(it, sid, k):
    if (sid, k + 1) in TR: return TR[(sid, k + 1)]
    o = it['opts']
    def rep(m):
        w = m.group(2).strip()
        for n in range(len(w.split()), 0, -1):
            ww = ' '.join(w.split()[:n])
            idx = [i for i, (a, b) in enumerate(o) if i != it['ans'] and (a == ww or b == ww)]
            if idx: return ''.join(C[i] for i in idx) + ' ' + m.group(2)
        return m.group(0)
    return re.sub(r'([①②③④⑤]+)\s*([A-Za-z][A-Za-z\-]*(?: [a-z][a-z\-]*)?)', rep, it['tr'])

def finalize():
    for S in SETS:
        for k, it in enumerate(S['items']):
            it['no'] = k + 1
            it['src'] = S['nums'][k // 10] + '번'
            it['pts'] = {'하': 3, '중': 5, '상': 6, '서술': 6}[it['lv']]
            if it['lv'] == '서술': continue
            o = list(it['o']); c = o.pop(0); o.insert(it['at'], c)
            assert len(set(o)) == 5, (S['no'], k + 1)
            it['opts'], it['ans'] = o, it['at']
            it['tr'] = autofix(it, S['no'], k)
        mc = [it for it in S['items'] if it['lv'] != '서술']
        S['dist'] = [sum(1 for it in mc if it['ans'] == i) for i in range(5)]
        assert sum(it['pts'] for it in S['items']) == 100, S['no']
finalize()

def fill(s, a, b, gloss=True):
    g = lambda w: '<b>%s</b>%s' % (esc(w), '<small>(%s)</small>' % esc(word_mean(w)) if gloss and word_mean(w) else '')
    return esc(s).replace('{A}', g(a)).replace('{B}', g(b))
def blank(s): return esc(s).replace('{A}', '(A) <span class="bl"></span>').replace('{B}', '(B) <span class="bl"></span>')
def stem(it):
    first = it['no'] in (1, 11)
    if it['lv'] == '서술': return '윗글의 내용을 요약한 문장을 &lt;조건&gt;에 맞게 완성하시오. <span class="pt">[%d점]</span>' % it['pts']
    return ('윗글의 내용을 한 문장으로 요약하고자 한다. 빈칸 (A), (B)에 들어갈 말로 가장 적절한 것은?' if first else '윗글의 내용을 요약한 문장의 빈칸 (A), (B)에 들어갈 말로 가장 적절한 것은?') + ' <span class="pt">[%d점]</span>' % it['pts']
def wsent(s): return esc(s).replace('(A) ', '<b>(A)</b> ').replace('(B) ', '<b>(B)</b> ')
def vocab(it):
    seen, out = set(), []
    for pair in it['opts']:
        for w in pair:
            if w not in seen: seen.add(w); out.append((w, word_mean(w)))
    for w in it['extra']:
        if w not in seen: seen.add(w); out.append((w, word_mean(w)))
    return out

# ── 지문 문장 해석 (데이터 파일 본문 탭) ──
PK = json.loads(subprocess.check_output(['node', '-e', "global.window={};require('%s');process.stdout.write(JSON.stringify(window.PKG))" % DATA]))
KO = {}
for d in PK['days']:
    cur = None
    for l in d['passage']:
        if l[0] == '#':
            m = re.match(r'(\d+(?:~\d+)?)번', l[1]); cur = m.group(1) if m else None
            if cur and cur not in KO: KO[cur] = []
            elif cur: cur = None
        elif cur and l[2]: KO[cur].append([l[1], l[2]])
for S in SETS:
    for n in S['nums']: assert KO.get(n), n

# ═════════ ① 앱 시험 ═════════
def app_tests():
    tests = []
    for S in SETS:
        items = []
        for it in S['items']:
            P = S['P'][(it['no'] - 1) // 10]; num = S['nums'][(it['no'] - 1) // 10]
            ctx = '<div class="wbox"><p>%s</p></div>' % esc(P)
            if it['lv'] == '서술':
                s = it['s']
                items.append({'kind': 'write', 'n': '서술형 %d' % it['no'], 'src': num + '번', 'pts': it['pts'], 'stem': stem(it),
                              'body': ctx + '<div class="wsum">' + wsent(s) + '</div><div class="wcond"><b>&lt;조건&gt;</b> 윗글에서 찾아 쓰되, 주어진 철자로 시작할 것 · 필요하면 어형이나 품사를 바꿀 것</div>',
                              'blanks': [dict(b, note=False) for b in it['blanks']],
                              'model': ' '.join('%s %s' % (b['label'], b['ans'][0]) for b in it['blanks']),
                              'ex': '해석 ▶ %s\n근거 ▶ %s\n어휘 ▶ %s\n채점 ▶ %s' % (it['ko'], it['gr'], ' · '.join('%s %s' % v for v in it['voc']), it['rule'])})
                continue
            a, b = it['opts'][it['ans']]
            ex = '요약문 ▶ %s\n해석 ▶ %s\n근거 ▶ %s\n%s함정 ▶ %s\n난이도 ▶ %s · %d점' % (
                re.sub(r'<[^>]+>', '', fill(it['s'], a, b).replace('<small>(', '(').replace(')</small>', ')')), it['ko'], it['gr'],
                ('구문 ▶ %s\n' % it['gm']) if it['gm'] else '', it['tr'], it['lv'], it['pts'])
            items.append({'n': it['no'], 'src': num + '번', 'stem': stem(it),
                          'body': '<div class="wsum">' + blank(it['s']).replace('class="bl"', 'class="wblank"') + '</div><div class="wcols">선택지 순서: (A) / (B)</div>',
                          'opts': ['%s / %s' % p for p in it['opts']], 'en': True, 'ans': it['ans'], 'ex': ex, 'ctx': ctx, 'pts': it['pts'],
                          'okos': ['%s / %s' % (word_mean(p[0]), word_mean(p[1])) for p in it['opts']],
                          'words': [[w, m] for w, m in vocab(it)], 'kos': KO[num]})
        tests.append({'id': S['id'], 'kind': 'boss', 'title': '요약문 끝판왕 %d · %s·%s번' % (S['no'], S['nums'][0], S['nums'][1]),
                      'short': '끝판왕 %s·%s번' % S['nums'], 'school': '안곡고 2학년 · 최상위 요약문', 'minutes': 35, 'items': items})
    return tests

def emit(tests):
    js = open(DATA, encoding='utf-8').read()
    old = json.loads(subprocess.check_output(['node', '-e', "global.window={};require('%s');process.stdout.write(JSON.stringify(window.PKG.tests||[]))" % DATA]))
    keep = [t for t in old if t.get('kind') != 'boss']
    blk = '/* BOSS-TESTS: 요약문 끝판왕 (wrapup/boss_build.py 로 만듦 · 손으로 고치지 말 것) */\nwindow.PKG.tests = (window.PKG.tests || []).filter(function (t) { return t.kind !== \'boss\'; }).concat(' + json.dumps(tests, ensure_ascii=False) + ');\n/* /BOSS-TESTS */\n'
    if '/* BOSS-TESTS' in js: js = re.sub(r'/\* BOSS-TESTS.*?/\* /BOSS-TESTS \*/\n', lambda m: blk, js, flags=re.S)
    else: js = js.rstrip('\n') + '\n' + blk
    open(DATA, 'w', encoding='utf-8').write(js)
    print('tests: wrap-up', len(keep), '+ boss', len(tests))

# ═════════ ② A4 시험지 ═════════
CSS = '''<style>
@page { size: A4; margin: 13mm 12mm 14mm }
* { box-sizing: border-box }
body { font-family: 'Noto Serif KR', 'Nanum Myeongjo', serif; font-size: 9.6pt; line-height: 1.55; color: #111; margin: 0 }
.sans, .hd, .tt, .idrow, .notice, .stem .n, .key, .eb, h3 { font-family: 'Noto Sans KR', 'Malgun Gothic', sans-serif }
.hd { display: flex; justify-content: space-between; font-size: 8.5pt; border-bottom: 1.6px solid #111; padding-bottom: 3px; margin-bottom: 8px }
.sub { text-align: center; font-size: 9pt; margin: 2px 0 4px }
.tt { display: flex; align-items: flex-end; justify-content: space-between; margin: 0 0 8px }
.tt h1 { font-size: 22pt; margin: 0; letter-spacing: -.02em } .tt .l, .tt .r { font-weight: 700; font-size: 11pt; width: 30% } .tt .r { text-align: right }
.boss { display: inline-block; background: #111; color: #fff; border-radius: 4px; padding: 1px 8px; font-size: 9pt; margin-right: 6px; vertical-align: 3px }
.idrow { display: grid; grid-template-columns: 1fr 1.4fr .8fr 1fr .8fr 2fr .8fr 1fr; border: 1.4px solid #111; font-size: 8.8pt; margin-bottom: 8px }
.idrow div { padding: 5px 6px; border-right: 1px solid #999 } .idrow div:nth-child(odd) { background: #eee; font-weight: 700; text-align: center } .idrow div:last-child { border-right: 0 }
.notice { border: 1px solid #999; background: #f6f6f6; padding: 6px 9px; font-size: 8.4pt; margin-bottom: 10px }
.notice p { margin: 1px 0 }
.cols { column-count: 2; column-gap: 9mm; column-rule: 1px solid #bbb }
.ptitle { font-family: 'Noto Sans KR', sans-serif; font-weight: 700; margin: 0 0 4px }
.passage { text-indent: 1em; text-align: justify; margin: 0 0 12px; break-inside: avoid }
.q { break-inside: avoid; margin: 0 0 13px }
.stem { margin: 0 0 5px; padding-left: 1.6em; text-indent: -1.6em } .stem .n { font-weight: 800 } .pt { font-family: 'Noto Sans KR', sans-serif; font-weight: 700; font-size: 8.6pt }
.sbox { border: 1px solid #555; padding: 6px 9px; margin: 0 0 6px; font-family: 'Noto Serif', 'Noto Serif KR', serif; line-height: 1.85 }
.bl { display: inline-block; width: 5.2em; border-bottom: 1px solid #111; height: 1em; vertical-align: -2px }
table.ch { margin: 0 auto; border-collapse: collapse; font-family: 'Noto Serif', serif; font-size: 9.4pt }
table.ch td { padding: 1px 7px; text-align: center } table.ch td.d { color: #555 } table.ch thead td { font-size: 8.6pt }
.cond { font-size: 8.4pt; border: 1px dashed #777; padding: 4px 7px; margin: 0 0 6px; font-family: 'Noto Sans KR', sans-serif }
.ans { display: flex; gap: 10px; font-family: 'Noto Sans KR', sans-serif; font-size: 9pt } .ans span { flex: 1; border-bottom: 1px solid #111; padding-bottom: 2px }
.ft { text-align: center; font-size: 8pt; margin-top: 4px }
.pg { break-after: page } .pg:last-child { break-after: auto }
/* 교사용 */
.key { width: 100%; border-collapse: collapse; margin: 4px 0 8px; font-size: 9pt; text-align: center } .key td { border: 1px solid #888; padding: 3px } .key tr:nth-child(odd) td { background: #eee; font-weight: 700 }
.rule { border: 1px solid #999; background: #f6f6f6; padding: 6px 9px; font-size: 8.4pt; margin-bottom: 10px; font-family: 'Noto Sans KR', sans-serif }
.ex { break-inside: avoid; margin: 0 0 11px; font-size: 8.9pt }
.eb { background: #111; color: #fff; padding: 2px 7px; font-weight: 700; font-size: 9pt; margin-bottom: 4px } .eb small { font-weight: 500; margin-left: 6px; color: #ddd }
.ex p { margin: 2px 0 } .ex .lb { font-family: 'Noto Sans KR', sans-serif; font-weight: 800; margin-right: 4px }
.ex small { color: #444; font-size: 7.6pt }
.vt { width: 100%; border-collapse: collapse; margin: 3px 0; font-size: 8.3pt } .vt td { border: 1px solid #aaa; padding: 1px 5px } .vt tr:first-child td { background: #eee; font-weight: 700; font-family: 'Noto Sans KR', sans-serif } .vt td:first-child { font-weight: 700; width: 42%; font-family: 'Noto Serif', serif }
h3 { font-size: 10.5pt; margin: 0 0 6px; padding: 3px 0; border-bottom: 1.4px solid #111; break-after: avoid }
.pv { font-size: 8.4pt; margin: 0 0 4px }
</style>'''
FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700;800&family=Noto+Serif+KR:wght@400;700&family=Noto+Serif:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet">'

def student(S):
    q = []
    for half in (0, 1):
        n0 = half * 10 + 1
        q.append('<p class="ptitle">[%d~%d] 다음 글을 읽고, 물음에 답하시오.</p><p class="passage">%s</p>' % (n0, n0 + 9, esc(S['P'][half])))
        for it in S['items'][half * 10:half * 10 + 10]:
            h = '<div class="q"><p class="stem"><span class="n">%d.</span> %s</p>' % (it['no'], stem(it))
            if it['lv'] == '서술':
                h += '<div class="sbox">%s</div><div class="cond">&lt;조건&gt; %s</div><div class="ans">%s</div>' % (
                    wsent(it['s']), '윗글에서 찾아 쓰되, 주어진 철자로 시작할 것 · 필요하면 어형이나 품사를 바꿀 것', ''.join('<span>%s</span>' % b['label'] for b in it['blanks']))
            else:
                h += '<div class="sbox">%s</div><table class="ch"><thead><tr><td></td><td>(A)</td><td></td><td>(B)</td></tr></thead><tbody>%s</tbody></table>' % (
                    blank(it['s']), ''.join('<tr><td>%s</td><td>%s</td><td class="d">……</td><td>%s</td></tr>' % (C[i], esc(a), esc(b)) for i, (a, b) in enumerate(it['opts'])))
            q.append(h + '</div>')
    title = '요약문 끝판왕 %d · %s·%s번' % (S['no'], S['nums'][0], S['nums'][1])
    return ('<!DOCTYPE html><html lang="ko"><head><meta charset="utf-8"><title>%s</title>%s%s</head><body>' % (title, FONTS, CSS) +
        '<div class="hd"><span><b>고2 영어 영역</b></span><span>요약문 끝판왕 챌린지 · %s·%s번 변형</span></div>' % S['nums'] +
        '<p class="sub">2026학년도 9월 고2 전국연합학력평가 %s·%s번 변형</p>' % S['nums'] +
        '<div class="tt"><span class="l">주말 도전 %d</span><h1><span class="boss">최상위</span>요약문 끝판왕</h1><span class="r">%s·%s번</span></div>' % ((S['no'],) + S['nums']) +
        '<div class="idrow"><div>학년·반</div><div>2학년 &nbsp; 반</div><div>번호</div><div>번</div><div>이름</div><div></div><div>점수</div><div>/ 100</div></div>' +
        '<div class="notice"><p><b>※ 유의사항</b></p><p>1. 문항 수 20문항(선택형 18 · 서술형 2) · 시험 시간 35분 · 총점 100점. 문항 끝의 [ ]는 배점입니다.</p><p>2. 각 지문을 먼저 읽은 뒤, 요약문의 빈칸 (A), (B)에 들어갈 말의 조합으로 가장 적절한 것 하나를 고르시오.</p><p>3. 서술형은 &lt;조건&gt;을 지키지 않으면 감점하며, 철자 오류는 오답 처리합니다. 답은 데일리 영어 앱 ‘끝판왕’ 탭에 입력해요.</p></div>' +
        '<div class="cols">' + ''.join(q) + '</div></body></html>')

def teacher(S):
    mc = [it for it in S['items']]
    key = '<table class="key"><tr><td>번호</td>%s</tr><tr><td>정답</td>%s</tr><tr><td>번호</td>%s</tr><tr><td>정답</td>%s</tr></table>' % (
        ''.join('<td>%d</td>' % it['no'] for it in mc[:10]), ''.join('<td>%s</td>' % ('서술형' if it['lv'] == '서술' else C[it['ans']]) for it in mc[:10]),
        ''.join('<td>%d</td>' % it['no'] for it in mc[10:]), ''.join('<td>%s</td>' % ('서술형' if it['lv'] == '서술' else C[it['ans']]) for it in mc[10:]))
    w = [it for it in S['items'] if it['lv'] == '서술']
    rule = ('<div class="rule"><b>배점 및 서술형 채점 기준</b><br>· 배점: 하 4문항(각 3점) · 중 선택형 8문항(각 5점) · 서술형 2문항(각 6점) · 상 6문항(각 6점) = 100점<br>' +
            ''.join('· %d번: %s — %s<br>' % (it['no'], ' '.join('%s %s' % (b['label'], b['ans'][0]) for b in it['blanks']), it['rule']) for it in w) +
            '· 정답 분포 ' + ' '.join('%s %d개' % (C[i], n) for i, n in enumerate(S['dist'])) + '</div>')
    body = []
    for half in (0, 1):
        body.append('<h3>%s 지문 해설 [%d~%d]</h3>' % (S['titles'][half], half * 10 + 1, half * 10 + 10))
        for it in S['items'][half * 10:half * 10 + 10]:
            if it['lv'] == '서술':
                ans = ' '.join('%s <b>%s</b>' % (b['label'], esc(b['ans'][0])) + (' (%s 선생님 확인)' % '·'.join(b['chk']) if b['chk'] else '') for b in it['blanks'])
                s = esc(it['s'])
                for b in it['blanks']:
                    s = re.sub(re.escape(b['label']) + r' [a-z]_+', '<b>%s</b>' % esc(b['ans'][0]), s)
                body.append('<div class="ex"><div class="eb">%d번 서술형<small>중 · 6점</small></div><p><span class="lb">정답</span>%s</p><p><span class="lb">요약문</span>%s</p><p><span class="lb">해석</span>%s</p><p><span class="lb">근거</span>%s</p>%s<p><span class="lb">채점</span>%s</p></div>' % (
                    it['no'], ans, s, esc(it['ko']), esc(it['gr']), '<table class="vt"><tr><td>어휘</td><td>뜻</td></tr>' + ''.join('<tr><td>%s</td><td>%s</td></tr>' % (esc(a), esc(b)) for a, b in it['voc']) + '</table>', esc(it['rule'])))
                continue
            a, b = it['opts'][it['ans']]
            body.append('<div class="ex"><div class="eb">%d번 정답 %s<small>%s · %d점</small></div><p><span class="lb">요약문</span>%s</p><p><span class="lb">해석</span>%s</p><p><span class="lb">근거</span>%s</p>%s%s<p><span class="lb">함정</span>%s</p></div>' % (
                it['no'], C[it['ans']], it['lv'], it['pts'], fill(it['s'], a, b), esc(it['ko']), esc(it['gr']),
                ('<p><span class="lb">구문</span>%s</p>' % esc(it['gm'])) if it['gm'] else '',
                '<table class="vt"><tr><td>어휘</td><td>뜻</td></tr>' + ''.join('<tr><td>%s</td><td>%s</td></tr>' % (esc(x), esc(y)) for x, y in vocab(it)) + '</table>',
                esc(it['tr'])))
    title = '요약문 끝판왕 %d 정답과 해설' % S['no']
    return ('<!DOCTYPE html><html lang="ko"><head><meta charset="utf-8"><title>%s</title>%s%s</head><body>' % (title, FONTS, CSS) +
        '<div class="hd"><span><b>고2 영어 영역 · 정답 및 해설</b></span><span>요약문 끝판왕 챌린지 · 교사용</span></div>' +
        '<p class="sub">2026학년도 9월 고2 전국연합학력평가 %s·%s번 변형</p>' % S['nums'] +
        '<div class="tt"><span class="l">주말 도전 %d</span><h1>정답 및 해설</h1><span class="r">교사용</span></div>' % S['no'] +
        key + rule + '<div class="cols">' + ''.join(body) + '</div></body></html>')

if __name__ == '__main__':
    import os; os.makedirs(OUT, exist_ok=True)
    for S in SETS:
        print('세트', S['no'], S['nums'], '정답', ''.join(C[it['ans']] if it['lv'] != '서술' else '서' for it in S['items']), '분포', S['dist'])
        open(OUT + 'boss%d-student.html' % S['no'], 'w', encoding='utf-8').write(student(S))
        open(OUT + 'boss%d-teacher.html' % S['no'], 'w', encoding='utf-8').write(teacher(S))
    if 'emit' in sys.argv: emit(app_tests())
