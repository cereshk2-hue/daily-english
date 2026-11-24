# 11/24 중산고1 '끝판왕 어휘 심화' DAY hv1~hv4 (맨 끝) — 선생님: "끝판왕 난이도 올렸으니 어휘를 더 넣어서 학습"
# 재료: wrapup/boss4_hard.py 의 고난도 문항 72개(H35~H41, 원래 서술형 제외) · 뜻 = HMEAN
#   문항 o[0] = 정답 짝(A, B) · o[1] = A만 맞은 짝(→ B 자리 함정) · o[2] = B만 맞은 짝(→ A 자리 함정)
# 단계: ① 카드(정답 어휘 + 끝판왕 문장) ② 쉬운 단어, 숨은 뜻(흔한 뜻 함정) ③ 문장 속 뜻(같은 자리 오답 낱말의 뜻이 오답)
#       ④ 한 끗 함정 고르기(끝판왕에서 한 칸만 틀린 짝)
# 데이터 파일에는 HV-DAYS 블록으로 맨 끝에 붙임(기존 머리·시험 블록은 건드리지 않음) → DAY 62~65
import sys, json, re, random, subprocess
sys.path.insert(0, '/home/claude/srcrepo/generators')
sys.path.insert(0, '/home/claude/srcrepo/wrapup')
import boss4_data as B
path = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/proj/data/h1-mock-2509.js'
random.seed(1124)
orig = set(id(x) for n in ['S35', 'S36', 'S37', 'S38', 'S39', 'S40', 'S41'] for x in getattr(B, n))
HM = B.HMEAN
NOTRAP = {'random', 'dealings'}          # 흔한 뜻이 문맥 뜻과 너무 가까워 '숨은 뜻 함정'으로 쓰지 않음
TRAPFIX = {'profile': '(SNS) 프로필, 자기소개', 'posed': '포즈를 취했다', 'coined': '동전을 주조했다', 'banked': '은행에 예금된', 'check': '확인하다', 'dissolves': '녹아 없어짐'}
SIMILAR = [{'bespoke', 'tailored'}, {'alien', 'foreign'}, {'averted', 'stemmed'}, {'biased', 'partial', 'slanted'}, {'glide', 'coast', 'coasts'}, {'perpetual', 'incessant'}, {'with', 'by'}]
EXCL = {('dealings', 'trades')}          # dealings도 '거래'로 읽힐 수 있어 오답에서 뺌
FILLW = {'unleashed': ['eclipsed'], 'grip': ['hasten'], 'pervasive': ['fictional'], 'rote': ['seasoned'], 'dealings': ['motives'], 'sporadic': ['vestigial'], 'against': ['beyond'], 'neutral': ['cleared', 'bleached']}
def similar(u, v): return any(u in g and v in g for g in SIMILAR)
def toks(m): return set(t.strip() for t in re.split(r'[,;]', re.sub(r'\([^)]*\)', '', m)) if t.strip())
def clean(m): return re.sub(r'\s*\([^()]*✗\)', '', m.split(': ')[0]).strip()
def mean(v):
    m = HM.get(v) or B.MEAN.get(v) or B.MEAN.get(v + '_', '') or {'borrow': '빌리다'}.get(v, '')
    assert m, v
    return clean(m)
def trap(w):
    if w in NOTRAP or '✗' not in HM[w]: return None
    if w in TRAPFIX: return TRAPFIX[w]
    t = re.search(r'\(([^()]*)✗\)', HM[w]).group(1).strip().rstrip(',').strip()
    return t.split(', ')[-1] if w == 'dissolves' else re.sub(r'^\w+ ', '', t) if w == 'banked' else t
def fill(s, a, b): return s.replace('{A}', a).replace('{B}', b)
def mark(s, slot, w, other):
    return s.replace('{%s}' % slot, '<u>%s</u>' % w).replace('{%s}' % ('B' if slot == 'A' else 'A'), other)
def point(tr): return re.sub(r'^함정 ▶\s*', '', tr.split(' ①')[0]).strip()

GROUPS = [('35·36', [('35', B.H35), ('36', B.H36)]), ('37·38', [('37', B.H37), ('38', B.H38)]),
          ('39·40', [('39', B.H39), ('40', B.H40)]), ('41~42', [('41~42', B.H41)])]
days = []
FILLED = []
for gi, (lab, parts) in enumerate(GROUPS, 1):
    passage, cards, poly, ctx, picks, seen = [], [], [], [], [], set()
    POOL = list(dict.fromkeys(p[i] for _, L in parts for x in L if id(x) not in orig for p in x['o'][1:] for i in (0, 1) if p[i] not in (x['o'][0][0], x['o'][0][1])))
    for num, L in parts:
        its = [x for x in L if id(x) not in orig]
        assert len(its) in (9, 18), (num, len(its))
        passage.append(['#', '%s번 · 끝판왕 문장 (정답을 넣은 문장)' % num, ''])
        for k, x in enumerate(its):
            (a, b), o = x['o'][0], x['o']
            en = fill(x['s'], a, b); passage.append(['', en, x['ko']])
            assert o[1][0] == a and o[1][1] != b and o[2][1] == b and o[2][0] != a, x['s']
            for slot, w, oth in (('A', a, b), ('B', b, a)):
                assert w in HM, w
                if w not in seen:
                    seen.add(w); cards.append([w, clean(HM[w]), int(num.split('~')[0]), w])
                ix = 0 if slot == 'A' else 1
                wrongs = list(dict.fromkeys(p[ix] for p in o[1:] if p[ix] != w))
                wm, ms = [], {clean(HM[w])}
                for v in wrongs + FILLW.get(w, []) + random.sample(POOL, len(POOL)):
                    if len(wm) == 3: break
                    if v == w or v in (a, b) or (w, v) in EXCL or any(similar(v, u) for u, _ in wm): continue
                    if mean(v) in ms or toks(mean(v)) & toks(mean(w)): continue
                    wm.append((v, mean(v))); ms.add(mean(v))
                if len([v for v, _ in wm if v not in wrongs]): FILLED.append((w, [v for v, _ in wm if v not in wrongs]))
                q = '밑줄 친 <b class="en">%s</b>의 이 문장 속 뜻은? <small>(%s번 끝판왕)</small><br><span class="en">%s</span>' % (w, num, mark(x['s'], slot, w, oth))
                base = '해석: %s\n근거(본문) ▶ %s\n포인트 ▶ %s' % (x['ko'], x['gr'], point(x['tr']))
                t = trap(w)
                if t:
                    opts = [clean(HM[w]), t] + [m for _, m in wm][:3]
                    ex = '정답 ▶ %s\n이유: 이 문장의 %s는 흔히 아는 \'%s\'이(가) 아니라 \'%s\'의 뜻이에요.\n오답 ▶ %s ← 흔히 아는 뜻(함정) / %s\n%s' % (
                        clean(HM[w]), w, t, clean(HM[w]), t, ' / '.join('%s = %s' % (v, m) for v, m in wm[:3]), base)
                    poly.append({'q': q, 'opts': opts, 'ex': ex})
                else:
                    opts = [clean(HM[w])] + [m for _, m in wm]
                    ex = '정답 ▶ %s\n이유: %s = \'%s\' → 해석과 맞아요.\n오답 ▶ %s ← 끝판왕에서 같은 자리에 나온 함정 낱말들\n%s' % (
                        clean(HM[w]), w, clean(HM[w]), ' / '.join('%s = %s' % (v, m) for v, m in wm), base)
                    ctx.append({'q': q, 'opts': opts, 'ex': ex})
                assert len(set(opts)) == len(opts) and len(opts) >= 4, (w, opts)
            # ④ 한 끗 함정: 문항마다 한 칸(번갈아)
            slot = 'A' if k % 2 == 0 else 'B'
            w, tw = (a, o[2][0]) if slot == 'A' else (b, o[1][1])
            s = x['s'].replace('{%s}' % slot, '{%s|%s}' % (w, tw)).replace('{%s}' % ('B' if slot == 'A' else 'A'), b if slot == 'A' else a)
            if s.startswith('{'): pass
            picks.append({'s': s, 'ex': '정답 ▶ %s (%s)\n오답 ▶ %s (%s) ← 끝판왕에서 이 칸만 틀린 함정\n해석: %s\n근거(본문) ▶ %s\n포인트 ▶ %s' % (
                w, clean(HM[w]), tw, mean(tw), x['ko'], x['gr'], point(x['tr']))})
    steps = [{'type': 'vocab', 'title': '끝판왕 어휘 카드', 'guide': '끝판왕 %s번 정답 어휘예요. 뜻을 고르면 그 단어가 쓰인 끝판왕 문장과 해석이 함께 나와요.' % lab, 'quizN': 15, 'items': cards},
             {'type': 'mc', 'title': '쉬운 단어, 숨은 뜻', 'guide': '아는 단어 같아도 끝판왕에서는 덜 알려진 뜻으로 나와요. 흔히 아는 뜻은 함정!', 'items': poly},
             {'type': 'mc', 'title': '문장 속 뜻', 'guide': '밑줄 친 말의 이 문장 속 뜻을 고르세요. 오답은 끝판왕에서 같은 자리에 나왔던 함정 낱말의 뜻이에요.', 'items': ctx},
             {'type': 'pick', 'title': '한 끗 함정 고르기', 'guide': '끝판왕 선택지에서 한 칸만 틀린 함정이에요. 문장에 맞는 말을 고르세요.', 'items': picks}]
    rng = '끝판왕 어휘 심화 %d · %s번' % (gi, lab)
    days.append({'id': 'hv%d' % gi, 'name': '', 'range': rng, 'story': '9월 모고 %s번 요약문 끝판왕 · 어휘 심화 (카드 → 숨은 뜻 → 문장 속 뜻 → 한 끗 함정)' % lab,
                 'passage': passage, 'steps': steps})
    print(rng, [(s['title'], len(s['items'])) for s in steps])

print('보충 오답', FILLED)
NB = int(json.loads(subprocess.check_output(['node', '-e', "global.window={};require('%s');process.stdout.write(JSON.stringify(window.PKG.days.filter(function(d){return !/^hv\\d+$/.test(d.id)}).length))" % path])))
for i, d in enumerate(days): d['name'] = 'DAY %d' % (NB + i + 1)
from gencommon import js
blk = ('/* HV-DAYS: 11/24 끝판왕 어휘 심화 DAY hv1~hv4 맨 끝 (generators/gen_js1hv.py 로 만듦 · 손으로 고치지 말 것) */\n'
       '(function(){var P=window.PKG,N=' + js(days) + ';'
       'P.days=P.days.filter(function(d){return !/^hv\\d+$/.test(d.id)}).concat(N);P.days.forEach(function(d,i){d.name="DAY "+(i+1)});})();\n/* /HV-DAYS */\n')
src = open(path, encoding='utf-8').read()
src = re.sub(r'/\* HV-DAYS:.*?/\* /HV-DAYS \*/\n', '', src, flags=re.S)
open(path, 'w', encoding='utf-8').write(src.rstrip('\n') + '\n' + blk)
