# 11/15 중산고1 9월 모고 '변형 어휘' DAY (h1-mock-2509.js 맨 뒤 v1~v11)
# 재료: work/vocab/sets3.json(전체, 뜻 칸에 (= 유의어) (↔ 반의어)) · sets4.json(쉬운 단어 뺀 것)
# 단계: ① 어휘 카드(영→한) ② 바꿔 쓰기(영→영) ③ 문장 속 바꿔 쓰기(본문 문장) ④ 반대말 함정(본문 문장) ⑤ 뜻 보고 철자 쓰기
import sys, json, re, random, subprocess
sys.path.insert(0, '/tmp/claude-0/-home-claude/a9e3e882-1f02-5d62-8f70-aced81bc59d2/scratchpad')
from gencommon import write
V = '/home/claude/srcrepo/work/vocab/'
S3 = json.load(open(V + 'sets3.json')); S4 = json.load(open(V + 'sets4.json'))
path = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/proj/data/h1-mock-2509.js'
PK = json.loads(subprocess.check_output(['node', '-e', "global.window={};require('%s');process.stdout.write(JSON.stringify(window.PKG))" % path]))
random.seed(1115)

M, SRC = {}, {}
for n, v in S3:
    for w, m, s in v: M.setdefault(w, m); SRC.setdefault(w, s)
FIXM = {'creates': 'create'}
for _n, _v in S3 + S4:
    for _r in _v:
        if _r[0] in FIXM: _r[0] = FIXM[_r[0]]
        _r[1] = _r[1].replace('creates', 'create')
M, SRC = {}, {}
for _n, _v in S3:
    for _w, _m, _s in _v: M.setdefault(_w, _m); SRC.setdefault(_w, _s)
DROPPAIR = [{'coin', 'establish'}, {'need -ing', 'need to be p.p.'}]
SKIPCTX = {('sense', 'senses')}
def base(m): return re.sub(r'\s*\((=|↔)[^)]*\)', '', m).strip()
def rel(w, sym):
    m = re.search(r'\(%s ([^)]*)\)' % sym, M.get(w, ''))
    return [x.strip() for x in m.group(1).split(',')] if m else []
SYN = {w: [x for x in rel(w, '=') if x in M and {w, x} not in DROPPAIR] for w in M}
ANT = {w: [x for x in rel(w, '↔') if x in M] for w in M}
def core(w): return set(p.strip() for p in re.split(r'[,·/]', re.sub(r'\(.*?\)', '', base(M[w]))) if p.strip())

# 본문 문장: 번호 → [(en, ko)]
SENT = {}
for d in PK['days']:
    cur = None
    for r in d['passage']:
        if r[0] == '#':
            m = re.match(r'(\d+(?:·\d+)?(?:~\d+)?)번', r[1]); cur = m.group(1).replace('·', '~') if m else None
            if cur == '41': cur = '41~42'
            SENT.setdefault(cur, [])
        elif cur and r[1] and not re.match(r'^[❶-❿]$', r[1]): SENT[cur].append((r[1], r[2]))
def forms(w):
    if ' ' in w: return [w]
    out = [w, w + 's', w + 'es', w + 'ed', w + 'd', w + 'ing', w + 'ly']
    if w.endswith('e'): out += [w[:-1] + 'ing', w[:-1] + 'ed']
    if w.endswith('y'): out += [w[:-1] + 'ies', w[:-1] + 'ied']
    return out
def find_sent(w, extra=()):
    nums = [s.replace(' 변형', '').replace(' 일부', '').replace('번', '') for s in SRC.get(w, '').split('/')] + [x.replace('번', '') for x in extra]
    for n in dict.fromkeys(nums):
        for en, ko in SENT.get(n, []):
            for f in forms(w):
                pat = re.compile(r'(?<![A-Za-z])%s(?![A-Za-z])' % re.escape(f), re.I)
                if len(pat.findall(en)) == 1: return n, en, ko, pat.search(en).group(0)
    return None

GROUPS = [('18·19번', ['18번', '19번']), ('20번', ['20번']), ('21·22번', ['21번', '22번']), ('23·24번', ['23번', '24번']), ('26·29번', ['26번', '29번']), ('30·31번', ['30번', '31번']),
          ('32·33번', ['32번', '33번']), ('34·35번', ['34번', '35번']), ('36~38번', ['36번', '37번', '38번']), ('39·40번', ['39번', '40번']), ('41~42번', ['41~42번'])]
S4D = {n.replace('중산고1 9월 ', ''): v for n, v in S4}
SYNSET = [r for n, v in S4 if '바꿔' in n for r in v]
POOL = list(M)

def distract(target_ws, k, avoid):
    """뜻이 겹치지 않는 오답 k개 (같은 DAY 단어 먼저)"""
    bad = set()
    for t in target_ws: bad |= core(t)
    out = []
    pl = avoid['pool'][:]; random.shuffle(pl)
    for w in pl + random.sample(POOL, len(POOL)):
        if w in out or w in avoid['no'] or ' ' in w and len(w.split()) > 3: continue
        if any(w[:5].lower() == t[:5].lower() for t in target_ws): continue
        if core(w) & bad: continue
        if any(w in SYN.get(t, []) or t in SYN.get(w, []) for t in target_ws): continue
        out.append(w)
        if len(out) == k: break
    return out
def gl(w): return '%s(%s)' % (w, base(M[w]))
def mask(w): return w[0] + '□' * (len(w) - 1)

def example(w, nums):
    f = find_sent(w, nums)
    if f: return f + (None,)
    for x in SYN.get(w, []):
        f = find_sent(x, nums)
        if f: return f + (x,)
    f = find_sent(w, [k + '번' for k in SENT if k])   # 다른 지문에서라도 실제 모의고사 문장
    if f: return f + (None,)
    return None

days = []
for i, (label, nums) in enumerate(GROUPS, 1):
    words = [r for n in nums for r in S4D[n]]
    ws = [r[0] for r in words]
    EX = {w: example(w, nums) for w in ws}
    pool = ws[:]
    random.shuffle(pool)
    # ① 카드
    cards = []
    for w, m, _s in words:
        e = EX[w]
        cards.append([w, base(m), int(e[0].split('~')[0]), e[3]] if e else [w, base(m)])
    # ② 영→영
    syn_items = []
    for w in ws:
        s = [x for x in SYN.get(w, []) if x != w]
        if not s: continue
        ans = s[0]; trap = ANT.get(w, [])[:1]
        dis = trap + distract([w, ans], 3 - len(trap), {'pool': pool, 'no': {w, ans}})
        ex = '정답 ▶ %s\n이유: %s = %s → 같은 뜻 \'%s\'\n오답 ▶ %s' % (ans, gl(w), gl(ans), base(M[w]).split(',')[0], ' / '.join(gl(x) + (' ← 반대말 함정' if x in trap else '') for x in dis))
        e = EX[w]
        if e: ex += '\n예문 ▶ %s (%s번)\n해석: %s' % (e[1], e[0], e[2]) + ('\n(본문에서는 같은 뜻의 %s로 쓰였어요)' % e[4] if e[4] else '')
        syn_items.append({'q': '<b class="en">%s</b>와(과) 바꿔 쓸 수 있는 말은?' % w, 'opts': [ans] + dis, 'ex': ex})
    # ③ 문장 속 바꿔 쓰기 / ④ 반대말 함정
    ctx_items, ant_items, used = [], [], []
    for w in ws:
        f = find_sent(w, nums)
        if not f: continue
        n, en, ko, hit = f
        if (w, hit.lower()) in SKIPCTX: continue
        s = [x for x in SYN.get(w, []) if x != w]
        if s and len(ctx_items) < 8:
            ans = s[0]; dis = distract([w, ans], 3, {'pool': pool, 'no': {w, ans}})
            u = re.sub(r'(?<![A-Za-z])(%s)(?![A-Za-z])' % re.escape(hit), r'<u>\1</u>', en, count=1, flags=re.I)
            ctx_items.append({'q': '밑줄 친 말과 바꿔 쓸 수 있는 것은? <small>(%s번 본문 · 선택지는 기본형)</small><br><span class="en">%s</span>' % (n, u), 'opts': [ans] + dis,
                              'ex': '정답 ▶ %s\n이유: 이 문장의 %s는 \'%s\' → %s와 같은 뜻\n해석: %s\n오답 ▶ %s' % (ans, hit, base(M[w]), gl(ans), ko, ' / '.join(gl(x) for x in dis))})
            used.append((n, en, ko))
        a = ANT.get(w, [])
        if a and hit.lower() == w.lower() and len(ant_items) < 6:
            ant_items.append({'s': re.sub(r'(?<![A-Za-z])(%s)(?![A-Za-z])' % re.escape(w), lambda m_: '{%s|%s}' % (m_.group(1), a[0] if m_.group(1)[0].islower() else a[0].capitalize()), en, count=1, flags=re.I),
                              'ex': '정답 ▶ %s (%s)\n이유: 문맥상 \'%s\'이 맞아요. %s는 반대말(%s)이라 흐름이 뒤집혀요.\n해석: %s' % (w, base(M[w]), base(M[w]), a[0], base(M[a[0]]), ko)})
            used.append((n, en, ko))
    # ⑤ 철자 (뜻 → 영어), 한 단어만
    sp = [w for w in ws if ' ' not in w and w.isalpha() and len(w) >= 5][:10]
    spell = [{'s': '%s → ___' % base(M[w]), 'v': mask(w), 'mask': mask(w), 'a': [w], 'ex': '정답 ▶ %s (%s)' % (w, base(M[w]))} for w in sp]
    # 본문 탭: 이 DAY에서 쓴 문장 (+ 단어 표)
    used += [(e[0], e[1], e[2]) for e in EX.values() if e]
    passage = []
    own = [x.replace('번', '') for x in nums]
    for n in own:   # 이 DAY 지문 전체(실제 모의고사 원문)
        passage.append(['#', '%s번 · 실제 모의고사 원문' % n, ''])
        passage += [['', en, ko] for en, ko in SENT.get(n, [])]
    extra = [u for u in used if u[0] not in own]
    for n in sorted(set(u[0] for u in extra), key=lambda x: int(x.split('~')[0])):
        passage.append(['#', '%s번 · 실제 모의고사 문장 (예문)' % n, ''])
        seen = set()
        for nn, en, ko in extra:
            if nn == n and en not in seen: seen.add(en); passage.append(['', en, ko])
    if not passage: passage = [['#', '이 DAY의 단어', ''], ['', ws[0], base(M[ws[0]])]]
    steps = [{'type': 'vocab', 'title': '변형 어휘 카드', 'guide': "뜻을 고르면 그 단어가 실제 9월 모의고사에서 쓰인 문장과 해석이 함께 나와요. 같은 뜻의 다른 말(유의어)은 다음 단계에서 연결해요.", 'quizN': min(12, len(cards)), 'items': cards}]
    if syn_items: steps.append({'type': 'mc', 'title': '바꿔 쓰기 (영 → 영)', 'guide': '왼쪽 단어와 같은 뜻의 영어를 고르세요. 시험의 어휘 비틀기가 바로 이 연결이에요. 반대말 함정에 주의!', 'items': syn_items[:12]})
    if ctx_items: steps.append({'type': 'mc', 'title': '문장 속 바꿔 쓰기', 'guide': '실제 본문 문장이에요. 밑줄 친 말을 바꿔 써도 뜻이 그대로인 말을 고르세요.', 'items': ctx_items})
    if ant_items: steps.append({'type': 'pick', 'title': '반대말 함정 고르기', 'guide': '본문 문장에 맞는 말을 고르세요. 하나는 반대말 함정이에요.', 'items': ant_items})
    if spell: steps.append({'type': 'verb', 'title': '뜻 보고 철자 쓰기', 'guide': '우리말 뜻을 보고 영어 단어를 쓰세요. 첫 글자와 네모칸 수가 힌트예요.', 'free': True, 'ph': '영어 단어 쓰기', 'items': spell})
    days.append({'id': 'v%d' % i, 'name': '', 'range': '변형 어휘 %d · %s' % (i, label), 'story': '9월 모고 %s · 변형 어휘 (카드 → 바꿔 쓰기 → 문장 속 → 반대말 → 철자)' % label, 'passage': passage, 'steps': steps})

base_days = [d for d in PK['days'] if not re.match(r'v\d+$', d['id'])]
PK['days'] = base_days + days
for k, d in enumerate(PK['days']): d['name'] = 'DAY %d' % (k + 1)
src = open(path, encoding='utf-8').read(); head = src[:src.index('window.PKG')]
if '변형 어휘 DAY' not in head: head = head.rstrip('\n') + '\n/* 11/15: 변형 어휘 DAY v1~v11 맨 뒤 추가 (generators/gen_js1voc.py) */\n'
write(PK, path, head)
for d in days: print(d['range'], [(s['title'], len(s['items'])) for s in d['steps']])
