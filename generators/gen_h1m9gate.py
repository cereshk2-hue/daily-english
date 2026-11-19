# 11/19 중산고1 2025 고1 9월 학평 '어법·어휘 한 판' DAY 6개 (맨 끝) — 시험범위 18~24 · 26 · 29~42번
# 선생님 자료: 10단계 WORKBOOK 6 어법·어휘 고르기 hwp (전 지문) → work_src/h1m9gate/raw.txt (hwpread.py)
# 문장·괄호·정답은 txt에서 그대로 읽음([a / b] + 정답 줄 → {정답|오답}), 해설은 h1m9gate_ex.py. 한 지문 = 한 덩이
# 채운 문장이 본문 DAY(d1~q41) 지문에 그대로 있는지 확인(40번 요약문 문장만 본문에 없음 → 예외)
import sys, json, re, subprocess
sys.path.insert(0, '/home/claude/srcrepo/generators')
from gencommon import write
from h1m9gate_ex import EX
path = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/proj/data/h1-mock-2509.js'
SRC = '/home/claude/srcrepo/work_src/h1m9gate/raw.txt'
PK = json.loads(subprocess.check_output(['node', '-e', "global.window={};require('%s');process.stdout.write(JSON.stringify(window.PKG))" % path]))
HAN = re.compile('[가-힣]')
SCOPE = ['18', '19', '20', '21', '22', '23', '24', '26', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41~42']
# 워크북 글자를 본문(앱) 글자에 맞춤
FIX = {
 ('18', 6): (' Sincerely, Eric Park, Student Council President', ''),
 ('30', 6): ('{reduced|improved}', '{decreased|increased}'),
 ('33', 1): ('1.49597 x 10', '1.49597 × 10'),
 ('34', 6): ('a(n) {undermining', 'an {undermining'),
 ('41~42', 0): ('”May I', '“May I'),
 ('41~42', 8): ('”No, thank you“', '“No, thank you”'),
}
NOT_IN_PASSAGE = {('40', 9)}  # 요약문 문장

def parse():
    L = [l.rstrip() for l in open(SRC, encoding='utf-8')]
    out, ko, en, cur = {}, [], [], None
    for l in L:
        s = l.strip()
        m = re.match(r'^(\d+(?:~\d+)?)번$', s)
        if m:
            if cur != m.group(1):
                assert not en or cur in ('25', '27', '28'), (cur, en)  # 25·27·28은 괄호 없는 지문
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
for k in ('d1', 'd2', 'd3', 'd4', 'd5', 'q32', 'q33', 'q34', 'q35', 'q36', 'q37', 'q38', 'q39', 'q40', 'q41'):
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
GROUPS = [['18', '19', '20', '21'], ['22', '23', '24'], ['26', '29', '30'], ['31', '32', '33', '34'], ['35', '36', '37'], ['38', '39', '40', '41~42']]
assert sum(GROUPS, []) == SCOPE
new, info = [], []
for gi, G in enumerate(GROUPS):
    items, tot = [], 0
    for q in G: it, nb = chunk(q); items.append(it); tot += nb
    lab = ['18~21번', '22~24번', '26·29·30번', '31~34번', '35~37번', '38~42번'][gi]
    rng = '%s · 어법·어휘 한 판' % lab
    new.append({'id': 'gt%d' % (gi + 1), 'name': '', 'range': rng, 'story': rng + ' · 괄호 %d개, 지문마다 괄호를 모두 맞혀야 100점 (덩이 %d개)' % (tot, len(G)),
                'passage': sum((PASS[q] for q in G), []),
                'steps': [{'type': 'gate', 'title': '어법 선택 한 판', 'guide': "한 지문이 한 덩이예요(%d덩이). 덩이마다 괄호(어법·어휘)를 모두 맞혀야 100점, 하나라도 틀리면 0점! 3번 안에 통과 못 하면 틀린 문장만 해설과 함께 연습하고 다시 도전해요." % len(G),
                           'items': items}]})
    info.append((rng, tot))
assert sum(t for _, t in info) == NB
PK['days'] = [d for d in PK['days'] if not re.match(r'^gt\d+$', d['id'])] + new
for i, d in enumerate(PK['days']): d['name'] = 'DAY %d' % (i + 1)
src = open(path, encoding='utf-8').read(); head = src[:src.index('window.PKG')]
tail = src[src.index('/* WRAPUP-TESTS'):] if '/* WRAPUP-TESTS' in src else ''
if '한 판' not in head: head = head.rstrip('\n') + '\n/* 11/19: 시험범위 지문 어법·어휘 한 판 DAY gt1~gt6 맨 끝 (generators/gen_h1m9gate.py) */\n'
if tail: PK.pop('tests', None)
write(PK, path, head)
if tail: open(path, 'a', encoding='utf-8').write(tail)
print(NB, info, [d['name'] for d in new])
