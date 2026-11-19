# 11/19 저동고1 2026 고1 10월 학평 '어법·어휘 한 판' 번호 하나 = DAY 하나 (맨 끝) — 단원 범위 20~24·29~35·37~40번 (28번 안내문은 워크북에 괄호 없음)
# 선생님 자료: 10단계 WORKBOOK 6 어법·어휘 고르기 hwp (전 지문) → work_src/jd10gate/raw.txt (hwpread.py). gen_h1m9gate.py 복사
# 문장·괄호·정답은 txt에서 그대로 읽음([a / b] + 정답 줄 → {정답|오답}), 해설은 h1m9gate_ex.py. 한 지문 = 한 덩이
# 채운 문장이 본문 DAY(d1~q41) 지문에 그대로 있는지 확인(40번 요약문 문장만 본문에 없음 → 예외)
import sys, json, re, subprocess
sys.path.insert(0, '/home/claude/srcrepo/generators')
from gencommon import write
from jd10gate_ex import EX
path = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/proj/data/h1-mock-2610-jeodong.js'
SRC = '/home/claude/srcrepo/work_src/jd10gate/raw.txt'
PK = json.loads(subprocess.check_output(['node', '-e', "global.window={};require('%s');process.stdout.write(JSON.stringify(window.PKG))" % path]))
HAN = re.compile('[가-힣]')
SCOPE = ['20', '21', '22', '23', '24', '29', '30', '31', '32', '33', '34', '35', '37', '38', '39', '40']
# 워크북 글자를 본문(앱) 글자에 맞춤
FIX = {
 ('37', 5): ('a(n) {artificial', 'an {artificial'),
 ('33', 4): ('”Beings', '“Beings'),
}
NOT_IN_PASSAGE = {('20', 6), ('31', 1), ('40', 6)}  # 20·31: 워크북 There is not / 본문 There's not·isn't (뜻 같음), 40: 요약문 문장

def parse():
    L = [l.rstrip() for l in open(SRC, encoding='utf-8')]
    out, ko, en, cur = {}, [], [], None
    for l in L:
        s = l.strip()
        m = re.match(r'^(\d+(?:~\d+)?)번$', s)
        if m:
            if cur != m.group(1):
                assert not any('[' in x for x in en), (cur, en)  # 괄호 없는 지문(도표·안내문)은 버림
                cur = m.group(1); ko = []; en = []
            continue
        if (not s or s.startswith('WORKBOOK') or s in ('단계별', 'Learning Guide', '어법·어휘 고르기', '고1', '[도표 생략]') or '학력평가' in s or s.startswith('❙')): continue
        if cur is None: continue
        if l.startswith(' ') and not HAN.search(s) and '[' not in s and en:  # 정답 줄
            ans = [a.strip() for a in s.split(' / ')]
            sent = ' '.join(en); assert len(re.findall(r'\[', sent)) == len(ans), (cur, sent, ans)
            k = iter(ans)
            def rep(m):
                o = [x.strip() for x in m.group(1).split(' / ')]; a = next(k); assert len(o) == 2 and a in o, (cur, o, a)
                return '{%s|%s}' % (a, o[1 - o.index(a)])
            out.setdefault(cur, []).append([re.sub(r'\[([^\]]*)\]', rep, sent), ' '.join(ko)]); ko, en = [], []
        elif HAN.search(s): ko.append(s)
        else: en.append(s)
    for (q, i), (a, b) in FIX.items(): assert out[q][i][0].count(a) == 1, (q, i, a); out[q][i][0] = out[q][i][0].replace(a, b)
    return out

R = parse()
NB = sum(len(re.findall(r'\{', s)) for q in SCOPE for s, _ in R[q])
D = {d['id']: d for d in PK['days']}
norm = lambda s: re.sub(r'\s+', ' ', s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"').replace('—', '-').replace('–', '-').replace('…', '...')).lower().strip()
# 지문별 본문 줄 (# 'NN번 · ' 머리줄로 나눔)
PASS = {}
for k in ['q' + q for q in SCOPE]:
    cur = None
    for l in D[k]['passage']:
        if l[0] == '#': cur = re.match(r'^(\d+(?:~\d+)?)번', l[1]).group(1); PASS[cur] = [l]; continue
        PASS[cur].append(l)
assert set(SCOPE) <= set(PASS), set(SCOPE) - set(PASS)
TOPIC = {q: re.sub(r'^\S+번 · ', '', PASS[q][0][1]) for q in SCOPE}
sq = lambda s: s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
def chunk(q):
    TX = norm(' '.join(l[1] for l in PASS[q] if l[0] != '#'))
    assert len(R[q]) == len(EX[q]), (q, len(R[q]), len(EX[q]))
    parts = []
    for i, ((s, ko), ex) in enumerate(zip(R[q], EX[q])):
        full = norm(re.sub(r'\{([^|}]*)\|[^}]*\}', r'\1', s))
        if (q, i) not in NOT_IN_PASSAGE: assert full in TX, (q, i, full)
        for m in re.findall(r'\{([^}]*)\}', s): o = m.split('|'); assert len(o) == 2 and o[0] != o[1], s
        for m in re.findall(r'\{([^|}]*)\|', s): assert sq(m) in sq(ex) or sq(m).split()[0] in sq(ex), (q, i, m, ex)
        assert ex.count('→') == len(re.findall(r'\{', s)), (q, i, ex)  # 괄호마다 해설 하나
        parts.append({'s': sq(s), 'ko': ko, 'ex': sq(ex)})
    nb = sum(len(re.findall(r'\{', p['s'])) for p in parts)
    return {'title': '%s번 · %s (괄호 %d개)' % (q, TOPIC[q], nb), 'parts': parts}, nb
GROUPS = [[q] for q in SCOPE]  # 11/19 19:20 선생님: 한 회차에 덩이가 너무 많음 → 번호 하나 = DAY 하나 (예전 gt1~gt6 묶음은 지움)
assert sum(GROUPS, []) == SCOPE
new, info = [], []
for gi, G in enumerate(GROUPS):
    items, tot = [], 0
    for q in G: it, nb = chunk(q); items.append(it); tot += nb
    lab = G[0] + '번'
    rng = '%s · 어법·어휘 한 판' % lab
    new.append({'id': 'g' + G[0].split('~')[0], 'name': '', 'range': rng, 'story': rng + ' · 괄호 %d개를 모두 맞혀야 100점' % tot,
                'passage': sum((PASS[q] for q in G), []),
                'steps': [{'type': 'gate', 'title': '어법 선택 한 판', 'guide': "괄호(어법·어휘)를 모두 맞혀야 100점, 하나라도 틀리면 0점! 3번 안에 통과 못 하면 틀린 문장만 해설과 함께 연습하고 다시 도전해요.",
                           'items': items}]})
    info.append((rng, tot))
assert sum(t for _, t in info) == NB
PK['days'] = [d for d in PK['days'] if not re.match(r'^g\d+$', d['id'])] + new
for i, d in enumerate(PK['days']): d['name'] = 'DAY %d' % (i + 1)
src = open(path, encoding='utf-8').read(); head = src[:src.index('window.PKG')]
tail = src[src.index('/* WRAPUP-TESTS'):] if '/* WRAPUP-TESTS' in src else ''
btail = src[src.index('/* BIMI-TESTS'):] if not tail and '/* BIMI-TESTS' in src else ''   # 비밀노트 블록은 그대로 두고 PKG.tests에서는 bimi 빼기
if btail: PK['tests'] = [t for t in PK.get('tests', []) if t.get('kind') != 'bimi']
if '한 판' not in head: head = head.rstrip('\n') + '\n/* 11/19: 어법·어휘 한 판 DAY g20~g40(번호 하나씩) 맨 끝 (generators/gen_jd10gate.py) */\n'
if tail: PK.pop('tests', None)
write(PK, path, head)
if tail: open(path, 'a', encoding='utf-8').write(tail)
if btail: open(path, 'a', encoding='utf-8').write(btail)
print(NB, info, [d['name'] for d in new])
