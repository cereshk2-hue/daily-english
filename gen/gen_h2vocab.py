import sys, json, re, random, subprocess
sys.path.insert(0, '/tmp/claude-0/-home-claude/a9e3e882-1f02-5d62-8f70-aced81bc59d2/scratchpad')
from gencommon import write
from dlgcommon import ansfirst
# 고2 대진고 능률(오선영) Lesson 3 어휘 학습 DAY (10/28). 출처: 선생님 문서 '대진고 Lesson 3 어휘 완전정복 학습지'(Claude Docs) → daejin_tables.json
SP = '/tmp/claude-0/-home-claude/a9e3e882-1f02-5d62-8f70-aced81bc59d2/scratchpad/'
T = json.load(open(SP + 'daejin_tables.json'))
TXT = open(SP + 'daejin_vocab.txt').read()
cl = lambda s: re.sub(r'\s+', ' ', s.replace('**', '').replace('°', '')).strip()
EST = set()  # 추정답(°)이 들어간 표제어 번호
W = []
for r in T[0][1:]:
    no, w, m, syn, ant = int(r[0]), r[1], r[2], r[3], r[4]
    if '°' in ''.join(r): EST.add(no)
    note = ''
    a2 = ant
    if ' / ' in ant: a2, note = ant.split(' / ', 1)
    if ant.startswith('cf)') or no == 24: a2, note = '', ant
    W.append({'no': no, 'w': cl(w), 'm': cl(m), 'syn': [cl(x) for x in syn.split(',') if cl(x)], 'ant': [cl(x) for x in a2.split(',') if cl(x)], 'note': cl(note)})
assert len(W) == 52
# ── 최근 프린트(선생님 10/28 21:32 스캔) 기준 보정 ──
def Wn(n): return W[n - 1]
Wn(2)['ant'] = ['abandon']                       # r____ 빈칸은 프린트에도 비어 있음 → relinquish(추정) 제외
Wn(21)['syn'] = ['count']; Wn(21)['ant'] = []     # 반의어 칸 필기가 불분명(be ^ important / in____) → 제외
Wn(32)['syn'] = ['possibly', 'likely']            # c____ 빈칸 비어 있음 → conceivably(추정) 제외
Wn(36)['m'] = '비교하다, 대조하다'
Wn(40)['syn'] = ['include', 'embrace', 'hold', 'encompass']
Wn(42)['m'] = '직접적으로'
Wn(43)['syn'] = ['evident', 'apparent', 'conspicuous']   # clear(추정) → 프린트: conspicuous
Wn(44)['ant'] = ['deficient', 'flawed']                  # defective(추정) → 프린트: deficient
Wn(44)['note'] = 'cf) optimum, optimize'
Wn(51)['m'] = '궁극적으로, 결국'
DROP3 = {2, 13, 20}       # STEP3 번호: relinquish / matter 반의어 / conceivably
FIX3 = {27: ('= evident, apparent, c□□□□□□□□□□', ['conspicuous']), 29: ('↔ d□□□□□□□□, flawed', ['deficient'])}
DROP4 = {9}               # STEP4: matter의 반의어
def mask(word): return ' '.join(p[0] + '□' * (len(p) - 1) for p in word.split(' '))
# STEP2 마스크가 원본과 같은지 확인 (원본 마스크 사용)
MK = {}
for r in T[1][1:]:
    for no, m in ((r[0], r[2]), (r[3], r[5])):
        if no:
            ww = W[int(no) - 1]['w']; MK[int(no)] = m
            assert len(m) == len(ww) and m[0] == ww[0] and all((c == ' ') == (d == ' ') for c, d in zip(m, ww)), (no, m, ww)
def answers(step):
    seg = re.search(step + r': (.*?)\n', TXT).group(1)
    out = {}
    for part in seg.split(' · '):
        n, a = part.split('. ', 1); out[int(n)] = [x.strip() for x in a.split(',')]
    return out
A3, A4 = answers('STEP 3'), answers('STEP 4')

def card(x):
    s = x['m']
    if x['syn']: s += ' | = ' + ', '.join(x['syn'])
    if x['ant']: s += ' | ↔ ' + ', '.join(x['ant'])
    if x['note']: s += ' | ' + x['note']
    return s
def exw(x):
    e = '정답 ▶ %s (%s)' % (x['w'], x['m'])
    if x['syn']: e += '\n유의어 ▶ ' + ', '.join(x['syn'])
    if x['ant']: e += '\n반의어 ▶ ' + ', '.join(x['ant'])
    if x['note']: e += '\n참고 ▶ ' + x['note']
    return e

# STEP3 문항: 원본 네모칸 문제 → 네모칸 하나씩 문항으로
S3 = []
for r in T[2][1:]:
    n, head, prob = int(r[0]), r[1], r[2]
    if n in DROP3: continue
    ans = A3[n]
    if n in FIX3: prob, ans = FIX3[n]
    ms = re.findall(r'[a-zA-Z]□+', prob)
    assert len(ms) == len(ans), (n, ms, ans)
    for k, (mk, a) in enumerate(zip(ms, ans)):
        assert mk[0] == a[0] and len(mk) == len(a), (n, mk, a)
        s = prob; cnt = [0]
        def rep(mm):
            i = cnt[0]; cnt[0] += 1
            return '___' if i == k else mm.group(0)
        s = re.sub(r'[a-zA-Z]□+', rep, s)
        x = next(w for w in W if w['w'] == head)
        kind = '유의어' if prob.startswith('=') else '반의어'
        S3.append({'no': x['no'], 'item': {'s': head + ' ' + s, 'v': mk, 'mask': mk, 'a': [a],
                   'ex': '정답 ▶ %s\n이유: %s(%s)의 %s → %s\n%s' % (a, head, x['m'], kind, a, ('유의어 ▶ ' + ', '.join(x['syn'])) if kind == '유의어' else ('반의어 ▶ ' + ', '.join(x['ant'])))}})

rnd = random.Random(20261028)
EXCL = {'conflict': ['contend', 'argue', 'differ', 'vary', 'diverge'], 'represent': ['clarify', 'show', 'signify', 'point out', 'demonstrate'], 'indicate': ['symbolize', 'stand for', 'depict', 'demonstrate', 'clarify'], 'illustrate': ['show', 'depict', 'signify'], 'ideal': ['excellent', 'faultless', 'impeccable', 'outstanding', 'flawless', 'superior'], 'weigh': ['inspect', 'investigate', 'scrutinize', 'examine', 'compare'], 'uncomplicated': ['direct', 'straight', 'clear', 'evident', 'apparent', 'obvious']}
ALLSYN = [(w['no'], s) for w in W for s in w['syn']]
ALLANT = [(w['no'], s) for w in W for s in w['ant']]
def related(x):
    bag = set(x['syn'] + x['ant'] + [x['w']])
    for w in W:  # 유의어·반의어가 겹치는 표제어는 서로 관련 있음
        kw = lambda m: set(t for t in re.split(r'[,\s()\[\]·~]+', re.sub(r'\[.*?\]', '', m)) if len(t) >= 2)
        if w['no'] != x['no'] and (set(w['syn'] + [w['w']]) & set(x['syn'] + [x['w']]) or set(w['ant']) & set(x['ant']) or kw(w['m']) & kw(x['m'])):
            bag |= set(w['syn'] + w['ant'] + [w['w']])
    return bag
def mcq(x, kind):
    pool = ALLSYN if kind == '유의어' else ALLANT
    right = x['syn'][0] if kind == '유의어' else x['ant'][0]
    bad = related(x) | set(EXCL.get(x['w'], []))
    cand = [s for no, s in pool if no != x['no'] and s not in bad and ' ' not in s or (no != x['no'] and s not in bad and len(s.split()) <= 3)]
    cand = sorted(set(c for c in cand if c not in bad and c != right))
    opts = [right] + random.Random('%s-%s' % (x['w'], kind)).sample(cand, 3)
    lst = x['syn'] if kind == '유의어' else x['ant']
    return {'q': '<b>%s</b> (%s)의 %s로 알맞은 것은?' % (x['w'], x['m'], kind), 'opts': opts,
            'ex': '정답 ▶ %s\n이유: %s의 %s ▶ %s\n오답 ▶ %s' % (right, x['w'], kind, ', '.join(lst), ' / '.join('%s(%s의 %s)' % (o, next(w['w'] for w in W if o in (w['syn'] if kind == '유의어' else w['ant'])), kind) for o in opts[1:]))}

def day(i, lo, hi):
    ws = [w for w in W if lo <= w['no'] <= hi]
    P = [['#', '어휘 %d~%d번' % (lo, hi), '']] + [['', '%d. %s' % (w['no'], w['w']), card(w)] for w in ws]
    st = [{'type': 'vocab', 'title': '단어장 (뜻 익히기)', 'quizN': len(ws), 'items': [[w['w'], w['m']] for w in ws]},
          {'type': 'verb', 'title': '뜻 보고 철자 쓰기', 'guide': '우리말 뜻을 보고, 첫 글자와 네모칸 수에 맞게 단어를 쓰세요.', 'free': True, 'ph': '단어 쓰기',
           'items': [{'s': '%s → ___' % w['m'], 'v': MK[w['no']], 'mask': MK[w['no']], 'a': [w['w']], 'ex': exw(w)} for w in ws]}]
    s3 = [x['item'] for x in S3 if lo <= x['no'] <= hi]
    if s3: st.append({'type': 'verb', 'title': '유의어·반의어 쓰기', 'guide': '원본 학습지의 빈칸 그대로예요. 첫 글자와 네모칸 수에 맞게 쓰세요. (서술형 1순위)', 'free': True, 'ph': '단어 쓰기', 'items': s3})
    sy = [mcq(w, '유의어') for w in ws if w['syn']]
    an = [mcq(w, '반의어') for w in ws if w['ant']]
    st.append({'type': 'mc', 'title': '유의어 고르기', 'guide': '표제어와 뜻이 같은(비슷한) 말을 고르세요.', 'items': sy})
    if an: st.append({'type': 'mc', 'title': '반의어 고르기', 'guide': '표제어와 뜻이 반대인 말을 고르세요.', 'items': an})
    return {'id': 'v%d' % i, 'name': 'DAY', 'range': '어휘 %s %d~%d번' % ('①②③④'[i - 1], lo, hi), 'story': 'Lesson 3 어휘 완전정복 · %d~%d번 (뜻 · 철자 · 유의어 · 반의어)' % (lo, hi), 'passage': P, 'steps': st}

V = [day(1, 1, 13), day(2, 14, 26), day(3, 27, 39), day(4, 40, 52)]
# 실전 모의고사 (STEP4 40문항)
it4 = []
for r in T[3][1:]:
    n, hint, mk = int(r[0]), r[1], r[2]
    if n in DROP4: continue
    a = A4[n][0]
    assert mk[0] == a[0] and len(mk) == len(a), (n, mk, a)
    x = next((w for w in W if w['w'] == a), None)
    src = next((w for w in W if a in ' '.join(w['syn'] + w['ant']).split() + w['syn'] + w['ant'] and re.search(r'\b%s\b' % re.escape(w['w']), hint)), None) or next((w for w in W if a in w['syn'] + w['ant']), None)
    e = '정답 ▶ %s' % a + ('\n%s' % exw(x).split('\n', 1)[1] if x and '\n' in exw(x) else '') + ('\n이유: %s(%s)의 %s ▶ %s' % (src['w'], src['m'], '반의어' if any(a in t.split() for t in src['ant']) else '유의어', ', '.join(src['ant'] if any(a in t.split() for t in src['ant']) else src['syn'])) if not x and src else '')
    if x: e = exw(x)
    it4.append({'s': hint.replace('☐', '( )') + ' → ___', 'v': mk, 'mask': mk, 'a': [a], 'ex': e})
P5 = [['#', '실전 모의고사 범위: 어휘 1~52번 전체', '']] + [['', '%d. %s' % (w['no'], w['w']), card(w)] for w in W]
V.append({'id': 'v5', 'name': 'DAY', 'range': '어휘 실전 모의고사 39', 'story': 'Lesson 3 어휘 · 섞어서 39문항 (37개 이상 목표)', 'passage': P5,
          'steps': [{'type': 'verb', 'title': '실전 모의고사', 'guide': '힌트를 보고 첫 글자와 네모칸 수에 맞게 쓰세요. 목표 37/39!', 'free': True, 'ph': '단어 쓰기', 'items': it4}]})

path = '/home/claude/proj/data/h2-ne-oh-L3.js'
PK = json.loads(subprocess.check_output(['node', '-e', "global.window={};require('%s');process.stdout.write(JSON.stringify(window.PKG))" % path]))
base = [d for d in PK['days'] if not re.match(r'^v\d$', d['id'])]
order = base + V
for i, d in enumerate(order): d['name'] = 'DAY %d' % (i + 1)
for d in V: ansfirst(d['steps'])
PK['days'] = order
PK['pick'] = True
src = open(path).read(); head = src[:src.index('window.PKG')]
if '어휘 DAY' not in head: head = head.rstrip('\n') + '\n/* 10/28: 어휘 DAY v1~v5 (scratchpad/gen_h2vocab.py, 선생님 문서 대진고 L3 어휘 학습지) · pick */\n'
write(PK, path, head)
print('ok', [(d['id'], d['name'], d['range']) for d in order], 'EST', sorted(EST))
