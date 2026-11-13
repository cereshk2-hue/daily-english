# 11/13 중3 지학사(민찬규) 7과 실전 변형 빌더 (wu_js2.py 복사 · 학교 표기만 다름) (wu_ag.py 복사 · 머리글을 세트별로 지정: HEAD = (짧은이름, 위 왼쪽, 아래 왼쪽, 파일 접두))
# 선택지 위치는 정답 분포(①~⑤ 각 4개)를 맞추도록 자동 배치. 해설 안의 {a}=정답 번호, {1}~{4}=오답(적은 순서) 번호.
import sys, re, json, html as H
sys.path.insert(0, '/home/claude/work/wrapup')
import os; os.chdir('/home/claude/work/wrapup')
from wcommon import *
CIR = '①②③④⑤'
U = lambda x: '<u>' + x + '</u>'
TG = lambda t, x: '<span class="tag">(%s)</span><u>%s</u>' % (t, x)
CN = lambda n, x: '%s<u>%s</u>' % (CIR[n - 1], x)
GP = lambda n: ' <span class="gap">( %s )</span> ' % CIR[n - 1]
BL = '<span class="blank"></span>'

class Test:
    def __init__(s, tid, short, title, scope, notice, H=('9월 학평', '2026학년도 9월 고2 전국연합학력평가', '2026년 9월 고2 학평', 'js2609')):
        s.tid, s.short, s.title, s.scope, s.notice, s.H = tid, short, title, scope, notice, H
        s.items = []
    def flex(s, stem, src_, body, opts, ex, w, en=True):
        """opts[0] = 정답, (영문, 우리말) 쌍 또는 문자열"""
        s.items.append(dict(k='flex', stem=stem, src=src_, body=body, opts=opts, ex=ex, w=w, en=en))
    def table(s, stem, src_, body, cols, rows, ex, w, ko=None):
        s.items.append(dict(k='table', stem=stem, src=src_, body=body, cols=cols, opts=rows, ex=ex, w=w, ko=ko))
    def fixed(s, stem, src_, body, opts, ans, ex, w, en=True):
        """opts 순서 고정(None이면 ①~⑤ 자리/번), ans = 1~5"""
        s.items.append(dict(k='fixed', stem=stem, src=src_, body=body, opts=opts, ans=ans - 1, ex=ex, w=w, en=en))

    def place(s):
        cnt = [0] * 5
        for it in s.items:
            if it['k'] == 'fixed': cnt[it['ans']] += 1
        assert max(cnt) <= 4, ('고정 정답이 한 번호에 너무 많음', cnt)
        rot = 0
        for it in s.items:
            if it['k'] == 'fixed': continue
            m = min(cnt); cand = [i for i in range(5) if cnt[i] == m]
            p = cand[rot % len(cand)]; rot += 1
            it['ans'] = p; cnt[p] += 1
            o = it['opts']; order = [None] * 5; order[p] = 0
            rest = [i for i in range(5) if i != p]
            for j, pos in enumerate(rest): order[pos] = j + 1
            it['order'] = order  # 표시 위치 → 원래 인덱스
            it['opts'] = [o[k] for k in order]
            if it.get('ko'): it['ko'] = [it['ko'][k] for k in order]
            def rep(m_, it=it):
                t = m_.group(1)
                orig = 0 if t == 'a' else int(t)
                return CIR[it['order'].index(orig)]
            it['ex'] = re.sub(r'\{(a|[1-4])\}', rep, it['ex'])
        assert cnt == [4] * 5, cnt
        for it in s.items: assert '{' not in it['ex'] or '{A}' in it['ex'], it['ex']

    def render(s):
        assert len(s.items) == 20, len(s.items)
        s.place()
        qs, ans, E, EN = [], [], [], {}
        for n, it in enumerate(s.items, 1):
            body = it['body'] or ''
            okos = None
            if it['k'] == 'table':
                body += ('\n' if body else '') + TB(it['cols'], it['opts']); okos = it.get('ko')
            elif it['opts'] is not None:
                en_ = [o[0] if isinstance(o, tuple) else o for o in it['opts']]
                ko_ = [o[1] for o in it['opts'] if isinstance(o, tuple)]
                body += ('\n' if body else '') + OL(en_, it['en'])
                if len(ko_) == 5: okos = ko_
            qs.append(Q(n, it['stem'] + src(it['src']), body)); ans.append(CIR[it['ans']]); E.append(it['ex'])
            EN[n] = {'w': it['w']}
            if okos: EN[n]['o'] = okos
        key = '<div class="keygrid">\n    ' + ''.join('<div>%d<b>%s</b></div>' % (k + 1, a) for k, a in enumerate(ans[:10])) + '\n    ' + ''.join('<div>%d<b>%s</b></div>' % (k + 11, a) for k, a in enumerate(ans[10:])) + '\n  </div>\n  <div class="exp">\n' + ''.join('    <p><b>%d</b> <span class="k">%s</span> %s</p>\n' % (k + 1, ans[k], e.replace('\n', '<br>\n')) for k, e in enumerate(E)) + '  </div>'
        page = ('<title>중3 @H0@ %s</title>\n<meta name="claude:viewport-fit-sides" content="cover">\n' % s.short + fonts + css + '''

<main>
<section class="page">
  <div class="top"><span>@H1@ · <b>%s</b></span><span>중학교 3학년 · 지학사(민찬규) · 내신 대비</span></div>
  <div class="title">
    <div class="g">영어</div>
    <h1>@H0@ %s<small>%s</small></h1>
    <div class="when">20문항 · 각 5점<br>제한 시간 30분</div>
  </div>
  <div class="idrow"><div>반</div><div>번호</div><div>이름</div><div>점수 &nbsp;&nbsp;&nbsp; / 100</div></div>
  <p class="notice">%s</p>

  <div class="qs">''' % (s.short, s.short, s.title, s.notice) + ''.join(qs) + '''  </div>
  <div class="foot"><span>@H2@ %s · 원문 일부 변형</span><span>중3 영어 · 7과 실전 변형</span></div>
</section>

<section class="page">
  <div class="top"><span>@H0@ %s · <b>정답과 해설</b></span><span>중학교 3학년 · 지학사(민찬규)</span></div>
  <div class="title"><div class="g">영어</div><h1>정답과 해설</h1><div class="when">각 5점 · 100점</div></div>
  ''' % (s.short, s.short) + key + '''
  <div class="foot"><span>정답 분포 ①~⑤ 각 4개</span><span>중3 영어 · 7과 실전 변형</span></div>
</section>
</main>
''')
        for k in range(3): page = page.replace('@H%d@' % k, s.H[k])
        fn = 'wrapup-%s-%s.html' % (s.H[3], s.tid)
        open(fn, 'w', encoding='utf-8').write(page)
        json.dump(EN, open('en-%s-%s.json' % (s.H[3], s.tid), 'w'), ensure_ascii=False)
        print(s.tid, ''.join(ans))
        return fn
