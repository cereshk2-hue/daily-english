# 11/27 발산중2 외부지문 3 (Reading Material 3) 인쇄물 — 선생님이 마음에 들어 한 형식(11/20, m3rf7) 그대로
#  ① 문장단위 구문 분석지  ② 백지노트  ③ 백지노트 답지  → /home/claude/out/bsrm3/*.pdf
import sys, html, re
sys.path.insert(0, '/home/claude/srcrepo/generators'); sys.path.insert(0, '/home/claude/srcrepo/print')
from bsrm3_data import S, E, K, A, FLOW, GRAMS, IDIOMS, TITLE
import baekji_note
esc = html.escape
O = '/home/claude/out/bsrm3/'
import os; os.makedirs(O, exist_ok=True)
OPEN = {'[': (']', 'main'), '{': ('}', 'sub'), '⟪': ('⟫', 'nest')}
SIMPLE = {'«': ('»', "<b class='key'>", '</b>'), '⟦': ('⟧', "<span class='rel'>", '</span>'), '⦃': ('⦄', "<span class='app'>", '</span>')}
def render(m):
    cnt = [0]
    def parse(i, end):
        out = []
        while i < len(m):
            c = m[i]
            if c == end: return ''.join(out), i + 1
            if c in OPEN:
                close, cls = OPEN[c]; j = m.index(':', i); role = m[i + 1:j]
                inner, i = parse(j + 1, close)
                out.append("<span class='u %s'>%s<sub>%s</sub></span>" % (cls, inner, esc(role)))
            elif c in SIMPLE:
                close, a, b = SIMPLE[c]; inner, i = parse(i + 1, close); out.append(a + inner + b)
            elif c == '‹':
                cnt[0] += 1; n = cnt[0]; inner, i = parse(i + 1, '›'); out.append("<span class='voc'>%s<sup>%d</sup></span>" % (inner, n))
            elif c in '〈〉':
                out.append("<span class='br'>%s</span>" % c); i += 1
            else:
                out.append(esc(c)); i += 1
        return ''.join(out), i
    h, _ = parse(0, None)
    return h.replace('‑', '-')
def card(i, a):
    n = i + 1
    w = ''.join("<span class='w'><sup>%d</sup><b>%s</b> %s</span>" % (j + 1, esc(x), esc(y)) for j, (x, y) in enumerate(a['w']))
    jd = ''.join("<div class='cr'><span class='en'><i>/</i>%s</span><span class='ko'>%s</span></div>" % (esc(x), esc(y)) for x, y in a['jd'])
    chk = "<div class='chk'><b>서술형 포인트</b> %s <span>← %s</span></div>" % (esc(a['chk'][0]), esc(a['chk'][1])) if a['chk'] else ''
    return ('<article class="card"><header class="ch"><span class="num">S%02d</span><span class="pt">POINT</span><ul>%s</ul><span class="flow">%s</span></header><div class="body">'
            '<div class="keyw"><span class="tag">핵심어</span><b>%s</b> %s</div><p class="sen">%s</p><div class="jd"><h4>직독직해</h4>%s</div>'
            '<p class="tr"><b>해석</b> %s</p><p class="gist"><span>결국 이 얘기</span> %s</p>%s<div class="gram"><b>문법</b><ul>%s</ul></div>%s</div></article>') % (
        n, ''.join('<li>%s</li>' % esc(p) for p in a['pt']), esc(a['fl']), esc(a['kw'][0]), esc(a['kw'][1]), render(a['sen']), jd, esc(K[i]), esc(a['gist']), chk,
        ''.join('<li>%s</li>' % esc(g) for g in a['gr']), ("<div class='words'><b>단어</b> %s</div>" % w) if w else '')
def analysis():
    tpl = open('/home/claude/srcrepo/print/m3rf7_analysis.html', encoding='utf-8').read()
    head = tpl[:tpl.index('<body>')].replace('중산중3 L7 외부지문 구문 분석지', '발산중2 외부지문 3 구문 분석지')
    legend = tpl[tpl.index('<div class="legend">'):tpl.index('<section class="block">')]
    legend = legend.replace('<span class="chip c-dash">점선 = 관계대명사절</span>', '<span class="chip c-dash">점선 = 앞 명사를 꾸밈(관계사절)</span>')
    flow = ''.join('<tr><td>%s</td><td>S%s</td><td>%s</td><td>%s</td></tr>' % (esc(a), b, esc(c), esc(d)) for a, b, c, d in FLOW)
    passage = ' '.join('<sup>%d</sup>%s' % (i + 1, esc(e)) for i, e in enumerate(E))
    gram = ''.join('<tr><td><b>%s</b> (S%s)</td><td>%s</td><td>%s</td></tr>' % (esc(a), b, c, esc(d)) for a, b, c, d in GRAMS)
    idi = ''.join('<tr><td>%s</td><td>%s</td><td>S%s</td></tr>' % (esc(a), esc(b), c) for a, b, c in IDIOMS)
    q = '''<div class="q"><p><b>Q1.</b> 어법상 올바른 것을 고르시오.</p><ol>
      <li>There was a woman (calling / called) Callisto (who / whose) job was to help the hunting goddess.</li>
      <li>Callisto was (so / such) beautiful that Zeus fell in love with her.</li>
      <li>One day, she happened (seeing / to see) Callisto in the forest.</li>
      <li>She wanted to get back at Callisto for (steal / stealing) her husband.</li>
      <li>How (happy / happily) she was to see her son!</li>
      <li>If you ever (see / will see) the Great Bear, wish them (happy / happiness).</li></ol></div>
    <div class="q"><p><b>Q2.</b> 같은 뜻이 되도록 빈칸을 채우시오.</p><p>Zeus fell in love with her even though he had a wife.<br>= Zeus fell in love with her ________ he had a wife.</p>
      <p>She thought it was the perfect moment to get back at Callisto.<br>= She thought it was the perfect moment to take ________ ________ Callisto.</p></div>
    <div class="q"><p><b>Q3.</b> 두 문장을 한 문장으로 쓰시오. (so ~ that)</p><p>Callisto was very beautiful. + Zeus fell in love with her.<br>→ Callisto was ________ ________ ________ Zeus fell in love with her.</p></div>
    <div class="q"><p><b>Q4.</b> 우리말에 맞게 배열하시오.</p><p>아르카스는 자라서 강한 사냥꾼이 되었다. (a strong hunter / grew up / to be / Arcas)<br>→ ______________________________________</p>
      <p>그녀는 칼리스토를 못생긴 곰으로 바꾸었다. (Callisto / an ugly bear / turned / into / she)<br>→ ______________________________________</p></div>
    <div class="q"><p><b>Q5.</b> 본문의 내용과 일치하는 것은?</p><ol>
      <li>Callisto was the wife of Zeus.</li>
      <li>Zeus' wife turned Arcas into a bear.</li>
      <li>Arcas recognized his mother at once.</li>
      <li>Zeus wanted to save the woman he loved.</li>
      <li>Zeus placed only Arcas in the night sky.</li></ol></div>
    <div class="ans"><b>정답</b><br>
      Q1 called · whose / so / to see / stealing / happy / see · happiness<br>
      Q2 although / revenge on<br>
      Q3 so beautiful that<br>
      Q4 Arcas grew up to be a strong hunter. / She turned Callisto into an ugly bear.<br>
      Q5 ④ (① 제우스에게는 다른 아내가 있었음 ② 아내가 바꾼 건 칼리스토, 아르카스는 제우스가 바꿈 ③ 알아보지 못함 ⑤ 둘 다 올려놓음)</div>'''
    body = ('<body><div class="wrap"><div class="top"><h1>발산중2 외부지문 3 <small>문장단위 구문 분석지 · 정답</small></h1>'
            '<div class="meta">Reading Material 3 · %s · 21문장 · 발산중 프린트 5~6쪽</div></div>%s'
            '<section class="block"><h2>지문 흐름 (Flow)</h2><p><b>주제</b> 큰곰자리와 작은곰자리에 얽힌 그리스 신화 — 곰이 된 엄마 칼리스토와 아들 아르카스의 슬픈 이야기</p>'
            '<div class="tbl"><table><tr><th>흐름</th><th>문장</th><th>핵심 내용</th><th>연결어·키워드</th></tr>%s</table></div>'
            '<p class="meta">구조: 질문(별자리는 어떻게?) → 이야기(사랑 → 질투·복수 → 엄마와 아들의 만남 → 하늘로) → 독자에게 당부</p></section>'
            '<section class="block"><h2>원문</h2><div class="passage">%s</div></section><section class="block"><h2>문장단위 분석</h2>%s</section>'
            '<section class="block"><h2>핵심 문법 한눈에</h2><div class="tbl"><table><tr><th>문법</th><th>지문 예문</th><th>시험 함정</th></tr>%s</table></div></section>'
            '<section class="block"><h2>숙어·표현</h2><div class="tbl"><table><tr><th>표현</th><th>뜻</th><th>문장</th></tr>%s</table></div></section>'
            '<section class="block"><h2>확인 문제</h2>%s</section></div></body></html>') % (esc(TITLE), legend, flow, passage, ''.join(card(i, a) for i, a in enumerate(A)), gram, idi, q)
    return head + body
GR_NAMES = ['소유격 관계대명사 whose', '과거분사 수식 (called)', 'so ~ that …', '양보 even though', 'happen to + 동사원형', 'to부정사 (형용사적·결과·감정의 원인·목적)',
            '전치사 + 동명사', 'turn A into B', '감탄문 How ~!', '관계대명사 생략 · 조건 if + 현재 · 4형식 wish']
GR_ANS = [('a woman called Callisto <b>whose</b> job was ~ (S4)', 'who ✘ — 뒤에 명사 job'), ('a woman <b>called</b> Callisto (S4)', 'calling ✘ — 불리는(수동)'),
          ('<b>so</b> beautiful <b>that</b> Zeus fell in love (S5)', 'such ✘ — such a + 형 + 명'), ('<b>even though</b> he had a wife (S5)', '= although / despite + 명사'),
          ('<b>happened to see</b> (S8, S18)', 'seeing ✘'), ('moment <b>to get back at</b>(S9) · grew up <b>to be</b>(S14) · happy <b>to see</b>(S16) · <b>To save</b>(S19)', '용법 구별: ~할 / 자라서 ~이 되다 / ~해서 / ~하기 위해'),
          ('for <b>stealing</b> (S9) · while <b>hunting</b> (S15)', 'for steal ✘ · while (he was) hunting'), ('<b>turned</b> Callisto <b>into</b> an ugly bear (S10, S19)', 'to ✘ · = change A into B'),
          ('<b>How happy</b> she was to see her son! (S16)', 'happily ✘ · 어순 How + 형 + 주어 + 동사'), ('the woman <b>he loved</b>(S19) · If you ever <b>see</b> · <b>wish them happiness</b>(S21)', 'loved her ✘ · will see ✘ · happy ✘')]
FLOWLINE = '도입 → 칼리스토와 제우스 → 아내의 복수 → 아들과 곰 → 하늘의 별 → 마무리'
def baekji():
    h = baekji_note.build('발산중2 외부지문 3', 'Reading Material 3 · %s · 21문장 — 왼쪽 본문, 오른쪽 해석. 점선 칸에 문법·구문·어휘를 직접 정리하세요.' % TITLE, S, FLOWLINE, GR_NAMES)
    return h
def answer():
    h = baekji()
    for i, a in enumerate(A):
        old = '<tr class="memo"><td></td><td colspan="2"><div class="ln"></div><div class="ln"></div></td></tr>'
        pt = a['chk'][0] + ' — ' + a['chk'][1] if a['chk'] else a['gr'][0]
        new = '<tr class="memo"><td></td><td colspan="2"><div class="anw">✎ %s</div><div class="anw">· %s</div></td></tr>' % (esc(pt), esc(' / '.join(a['gr'][1:3]) if len(a['gr']) > 1 else a['gist']))
        k = h.index(old); h = h[:k] + new + h[k + len(old):]
    assert '<div class="ln"></div>' not in h[:h.index('<div class="pg"></div>')]
    flow = '<br>'.join('%s (S%s) %s' % (a, b, c) for a, b, c, d in FLOW)
    h = h.replace('<div class="box">문장 번호와 함께 단락별 핵심 내용을 적으세요.</div>', '<div class="box anw" style="height:auto;min-height:150px">%s</div>' % flow, 1)
    for g, (ex, trap) in zip(GR_NAMES, GR_ANS):
        a = '<tr><td>%s</td><td></td><td></td></tr>' % esc(g); assert h.count(a) == 1, g
        h = h.replace(a, '<tr><td>%s</td><td class="anw">%s</td><td class="anw">%s</td></tr>' % (esc(g), ex, esc(trap)))
    boxes = h.split('<div class="box" style="height:190px"></div>'); assert len(boxes) == 3
    voc = ' · '.join('%s %s' % (a, b) for a, b, c in IDIOMS)
    sv = ('· so ~ that: Callisto was so beautiful that Zeus fell in love with her.<br>· even though = although<br>· get back at = take revenge on<br>'
          '· turn A into B = change A into B<br>· while hunting = while he was hunting<br>· How happy she was to see her son! = She was very happy to see her son.<br>'
          '· the woman he loved = the woman (that/whom) he loved<br>· grew up to be a hunter = grew up and became a hunter')
    h = boxes[0] + '<div class="box anw" style="height:auto;min-height:190px">%s</div>' % esc(voc) + boxes[1] + '<div class="box anw" style="height:auto;min-height:190px">%s</div>' % sv + boxes[2]
    h = h.replace('<small>백지노트</small>', '<small>백지노트 · 답지</small>').replace('</style>', '.anw{color:#c8372d;font-size:9.5pt;line-height:1.5}\n</style>', 1)
    return h
if __name__ == '__main__':
    a = analysis(); open(O + 'analysis.html', 'w', encoding='utf-8').write(a)
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(); pg.goto('file://' + O + 'analysis.html'); pg.wait_for_timeout(1500)
        pg.pdf(path=O + 'Balsan_RM3_analysis.pdf', format='A4', print_background=True, prefer_css_page_size=True); b.close()
    bj = baekji(); open(O + 'baekji.html', 'w', encoding='utf-8').write(bj); baekji_note.pdf(bj, O + 'Balsan_RM3_baekji.pdf')
    an = answer(); open(O + 'baekji_answer.html', 'w', encoding='utf-8').write(an); baekji_note.pdf(an, O + 'Balsan_RM3_baekji_answer.pdf')
    print('ok')
