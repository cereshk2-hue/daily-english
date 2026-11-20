# 11/20 고3 수능실전반 · 2027학년도 수능 영어 짝수형 OMR (h3-suneung-2510 시험 탭, 문제는 종이 시험지)
# 원본 work_src/s2711: 짝수형·홀수형 문제지 PDF(단으로 잘라 텍스트 even_c/odd_c.txt) · 정답표(이미지, 홀·짝) · 해설지(홀수형 번호)
# 짝수형 정답 = 정답표 짝수 → 홀수 정답의 선택지 글자가 짝수형 같은 글자 번호와 일치하는지 45문항 assert
# 해설은 해설지 [출제 의도] · [풀이] · [Words and Phrases]에서, 풀이 속 ①~⑤ 번호를 짝수형 번호로 바꿈
import re, json, subprocess, sys
W = '/home/claude/srcrepo/work_src/s2711/'
DATA = '/home/claude/proj/data/h3-suneung-2510.js'
CIR = '①②③④⑤'
sys.argv = ['x']; _g = {}
exec(open('/home/claude/srcrepo/gen/s2711/parse.py').read().split('E=load')[0], _g)
load, opts = _g['load'], _g['opts']
E, O = load(W + 'even_c.txt'), load(W + 'odd_c.txt')
OK = [int(x) for x in '3 1 1 3 5 4 1 3 4 4 1 5 2 4 5 1 2 5 1 2 2 5 2 5 5 4 5 4 3 3 1 1 5 3 3 2 4 3 4 2 1 2 4 2 3'.split()]
EK = [int(x) for x in '1 1 3 3 5 4 1 3 4 4 2 5 1 4 5 5 2 1 1 5 2 2 3 1 5 4 5 4 3 3 1 1 5 2 3 2 4 3 4 2 5 2 4 2 3'.split()]
THREE = {12, 14, 15, 21, 30, 33, 34, 37, 39, 42}
POS = {4, 29, 30, 35, 38, 39}  # 선택지가 그림·본문 속 번호(①~⑤ 자리)
N = lambda x: re.sub(r'[^A-Za-z가-힣$0-9]', '', x)
def clean(o):
    o = re.sub(r'\s+\d+\s+수학능력시험 문제지.*$', '', o)
    o = re.sub(r'\s+(\d+\s*)+(짝수형|홀수형)?\s*$', '', o); o = re.sub(r'\s*(짝수형|홀수형)\s*$', '', o)
    return o.strip()
# 해설지
H = open(W + 'hae.txt', encoding='utf-8').read().replace('\f', '\n')
H = re.sub(r'(?m)^[ \t]*\d{1,2}[ \t]*\n', '', H)  # 쪽 번호 줄
sec = {}
for m in re.finditer(r'(?m)^(\d{1,2})\.\s*\n?\s*\[출제 의도\]\s*(.+)$', H):
    sec[int(m.group(1))] = m.start()
assert sorted(sec) == list(range(1, 46)), sorted(sec)
order = sorted(sec.items(), key=lambda x: x[1]) + [(99, len(H))]
CORPUS = H
# 해설지 줄바꿈이 낱말 가운데서 끊긴 곳(눈으로 확인한 목록) → 붙여 씀
GLUE = [('개념이', '라는'), ('결', '합에'), ('깊이까', '지의'), ('동', '의했다'), ('드', '문'), ('메커', '니즘'), ('베', '이킹'), ('부드럽', '게'), ('사용했습', '니다'), ('생', '명체'), ('선생', '님에게'), ('슛', '들을'), ('시행', '착오'), ('않', '아!'), ('예', '외일'), ('이', '동하는'), ('인간', '으로서'), ('작', '성하다'), ('장', '신구'), ('전', '화할게요'), ('주', '기가'), ('주장', '하다'), ('지', '도하다'), ('탓하', '며'), ('패', '했다고'), ('필', '요했는데')]
PART = {'가', '이', '은', '는', '을', '를', '의', '에', '도', '와', '과', '로', '만', '서', '다', '고'}
def join_lines(txt):
    # 해설지 쪽 폭 줄바꿈 이어 붙이기: 앞 줄이 문장 끝(. ? ! 따옴표)이면 새 줄, 아니면 이어 붙임.
    # 띄어쓰기: '앞 줄 끝 낱말 + 다음 줄 첫 낱말'이 해설지 다른 곳에 한 줄 안에서 붙어 나오면 붙이고, 아니면 띄움
    out = []
    for ln in [l.strip() for l in txt.strip().split('\n') if l.strip()]:
        newline = not out or re.search(r'[.?!’”]$', out[-1]) or (re.match(r'^[①②③④⑤] ', ln) and re.match(r'^[①②③④⑤] ', out[-1]))
        if not newline:
            a = re.search(r'(\S+)$', out[-1]).group(1); b = re.match(r'(\S+)', ln).group(1)
            bb = b.rstrip(',.')
            glue = any(a.endswith(x) and b.startswith(y) for x, y in GLUE) or (re.search(r'[가-힣)③①②④⑤]$', a) and bb in PART) or (re.search(r'[가-힣]$', a) and re.match(r'^[가-힣]', b) and (a + bb) in CORPUS)
            out[-1] += ('' if glue else ' ') + ln
        else: out.append(ln)
    return out
GROUP = {**{q: '다음 빈칸에 들어갈 말로 가장 적절한 것을 고르시오.' for q in range(31, 35)}, **{q: '주어진 글 다음에 이어질 글의 순서로 가장 적절한 것을 고르시오.' for q in (36, 37)}, **{q: '글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳을 고르시오.' for q in (38, 39)}}
items = []; total = 0
for (q, st), (_, en) in zip(order, order[1:]):
    s = H[st:en]
    kind = re.search(r'\[출제 의도\]\s*(.+)', s).group(1).strip()
    pul = re.search(r'\[풀이\](.*?)(?=\[Words and Phrases\]|\Z)', s, re.S).group(1)
    wp = re.search(r'\[Words and Phrases\](.*)', s, re.S)
    eo = [clean(x) for x in opts(E[q])]; oo = [clean(x) for x in opts(O[q])]
    if q in POS:
        perm = [0, 1, 2, 3, 4]; eo = ['%s번' % c for c in CIR]
    else:
        perm = []
        for i in range(5):  # 홀수 i번 → 짝수 몇 번
            js = [j for j in range(5) if N(eo[j])[:25] == N(oo[i])[:25]]
            assert len(js) == 1, (q, i, oo[i], eo)
            perm.append(js[0])
        assert sorted(perm) == [0, 1, 2, 3, 4], (q, perm)
    assert perm[OK[q - 1] - 1] == EK[q - 1] - 1, ('짝수 정답 불일치', q)
    pul = re.sub(r'[①②③④⑤]', lambda m: CIR[perm[CIR.index(m.group(0))]], pul)
    out = join_lines(pul)
    # 풀이 끝의 선택지 해석 줄(①~⑤로 시작)은 번호 순서대로
    k = len(out)
    while k > 0 and re.match(r'^[①②③④⑤] ', out[k - 1]): k -= 1
    if k > 0 and len(out) - k >= 2: out = out[:k] + sorted(out[k:], key=lambda l: CIR.index(l[0]))
    ex = '정답 ▶ %s%s\n유형 ▶ %s\n풀이 ▶ ' % (CIR[EK[q - 1] - 1], '' if q in POS else ' ' + eo[EK[q - 1] - 1], kind) + '\n'.join(out)
    words = []
    if wp:
        w = re.sub(r'\s+', ' ', ' '.join(join_lines(wp.group(1))))
        ex += '\n단어 ▶ ' + w
    stem = re.sub(r'\s+', ' ', E[q][:E[q].find('①')] if '①' in E[q] else E[q]).strip()
    stem = re.sub(r'^\d+\.\s*', '', stem)
    if len(stem) > 120 or re.search(r'[A-Za-z]{4,}.*[A-Za-z]{4,}.*[A-Za-z]{4,}', stem[60:]):  # 지문이 섞이면 첫 문장(발문)만
        m = re.match(r'(.+?(것은\?|고르시오\.|시오\.)(\s*\[3점\])?)', stem); stem = m.group(1) if m else stem[:80]
    stem = re.sub(r'\s+(Man|Woman|Amy):\s*$', '', stem); stem = stem.replace('anchor 가 ', 'anchor가 ')
    if q == 35: stem = re.match(r'.+?\?', stem).group(0)
    if q in GROUP: stem = GROUP[q] + (' [3점]' if q in THREE else '')
    pts = 3 if q in THREE else 2; total += pts
    items.append({'n': q, 'src': ('듣기 · ' if q <= 17 else '') + kind, 'stem': stem, 'body': '', 'opts': eo,
                  'en': bool(re.search(r'[A-Za-z]{3}', ''.join(eo))) and q not in POS, 'ans': EK[q - 1] - 1, 'ex': ex,
                  'ctx': '', 'pts': pts, 'words': words, 'kos': []})
assert total == 100 and len(items) == 45
# 11/20 18:40 선생님: 듣기(1~17번)는 다 맞았다고 보고 가산점으로 → OMR은 18~45번만, 듣기 배점은 bonus
LIS = [it for it in items if it['n'] <= 17]; items = [it for it in items if it['n'] >= 18]
BONUS = sum(it['pts'] for it in LIS); assert BONUS == 37 and BONUS + sum(it['pts'] for it in items) == 100 and len(items) == 28
T = {'id': 's27e18', 'title': '2027학년도 수능 영어 (짝수형) · 18~45번', 'short': '수능 짝수형', 'school': '고3 수능실전반', 'minutes': 45, 'items': items,
     'bonus': BONUS, 'bonusNote': '듣기 1~17번 %d점은 모두 맞은 것으로 보고 가산점으로 넣었어요' % BONUS}
js = open(DATA, encoding='utf-8').read()
blk = '/* WRAPUP-TESTS: gen/gen_h3s27omr.py 로 만듦 (손으로 고치지 말 것) */\nwindow.PKG.tests = ' + json.dumps([T], ensure_ascii=False) + ';\n/* /WRAPUP-TESTS */\n'
if '/* WRAPUP-TESTS' in js: js = re.sub(r'/\* WRAPUP-TESTS.*?/\* /WRAPUP-TESTS \*/\n', lambda m: blk, js, flags=re.S)
else: js = js.rstrip('\n') + '\n' + blk
if 'testLabel' not in js.split('days:')[0]: js = js.replace("  noteOnly: '단어|어휘|숙어',", "  noteOnly: '단어|어휘|숙어',\n  testLabel: '수능 OMR',", 1)
open(DATA, 'w', encoding='utf-8').write(js)
print('OK', ''.join(CIR[i['ans']] for i in items))
