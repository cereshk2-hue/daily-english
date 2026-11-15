# 11/15 중산고1 9월 모고 '변형 어휘' DAY (h1-mock-2509.js 맨 뒤 v1~v11)
# 재료: work/vocab/sets3.json(전체, 뜻 칸에 (= 유의어) (↔ 반의어)) · sets4.json(쉬운 단어 뺀 것)
# 11/15 개편(선생님 피드백): 끝판왕 어휘 + 원문에서 변형될 만한 어휘로 확장(js1voc_data.py, 손으로 고름)
# 단계: ① 카드 ② 바꿔 쓰기(영→영, 역방향 중복 없음) ③ 유의어 모두 찾기 ④ 문장 속 바꿔 쓰기 ⑤ 쉬운 단어, 숨은 뜻 ⑥ 반대말 함정 (철자 쓰기 삭제)
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


from js1voc_data import W, POLY, CONFLICT, NOCTX, PICK
GROUPS = [('18·19번', ['18', '19']), ('20번', ['20']), ('21·22번', ['21', '22']), ('23·24번', ['23', '24']), ('26·29번', ['26', '29']), ('30·31번', ['30', '31']),
          ('32·33번', ['32', '33']), ('34·35번', ['34', '35']), ('36~38번', ['36', '37', '38']), ('39·40번', ['39', '40']), ('41~42번', ['41~42'])]
def uniq(n):
    out = []
    for en, ko in SENT.get(n, []):
        if (en, ko) not in out: out.append((en, ko))
    return out
def locate(hit, nums):
    """hit이 정확히 한 번 나오는 첫 본문 문장"""
    pat = re.compile(r'(?<![A-Za-z])%s(?![A-Za-z])' % re.escape(hit))
    for n in nums:
        for en, ko in uniq(n):
            if len(pat.findall(en)) == 1: return n, en, ko
    for n in nums:
        for en, ko in uniq(n):
            if pat.search(en): return n, en, ko
    return None
ALLN = [k for k in SENT if k]
def anywhere(w):
    for f in forms(w):
        r = locate(f, ALLN)
        if r: return r + (f,)
    return None
def U(en, hit): return re.sub(r'(?<![A-Za-z])(%s)(?![A-Za-z])' % re.escape(hit), r'<u>\1</u>', en, count=1)
def conflict(a, b): return {a, b} in CONFLICT
def tag(w, e): return '%s(%s)' % (w, e)

days = []
for i, (label, nums) in enumerate(GROUPS, 1):
    E = [dict(h=h, hit=hit, ko=ko, syn=syn, ant=ant, n=n) for n in nums for (h, hit, ko, syn, ant) in W[n]]
    heads = {e['h'] for e in E}
    for e in E:
        e['loc'] = None
        if e['hit']:
            r = locate(e['hit'], [e['n']])
            assert r, (e['h'], e['hit'])
            e['loc'] = r + (e['hit'],)
        else:
            e['loc'] = anywhere(e['h'])
    SYNOF = {s: e for e in E for s in e['syn']}
    def wrong_pool(e, k, extra=()):
        cand = []
        for o in E:
            if o is e or conflict(o['h'], e['h']): continue
            for s in o['syn']:
                if s in e['syn'] or s in e['ant'] or s == e['h'] or s in heads or s in cand: continue
                cand.append((s, o))
        random.shuffle(cand)
        out, used = [], set()
        for s, o in cand:
            if o['h'] in used: continue
            used.add(o['h']); out.append((s, o))
            if len(out) == k: break
        return out
    # ① 카드
    cards = []
    for e in E:
        l = e['loc']
        cards.append([e['h'], e['ko'], int(l[0].split('~')[0]), l[3]] if l else [e['h'], e['ko']])
    # ② 영→영 (답은 이 DAY 표제어가 아닌 유의어 → 다음 문제의 답이 미리 보이지 않음)
    syn_items, ans2 = [], {}
    for e in E:
        cs = [s for s in e['syn'] if s not in heads]
        if not cs: continue
        ans = cs[0]; ans2[e['h']] = ans
        trap = [a for a in e['ant'] if a not in heads][:1]
        wr = wrong_pool(e, 3 - len(trap))
        if len(wr) < 3 - len(trap): continue
        opts = [ans] + trap + [s for s, o in wr]
        ex = '정답 ▶ %s\n이유: %s = \'%s\' → %s도 같은 뜻으로 바꿔 쓸 수 있어요.' % (ans, e['h'], e['ko'], ans)
        ex += '\n오답 ▶ ' + ' / '.join(['%s ← 반대말 함정(반대 뜻)' % t for t in trap] + ['%s(= %s, %s)' % (s, o['h'], o['ko']) for s, o in wr])
        ex += '\n포인트 ▶ %s의 유의어: %s' % (e['h'], ', '.join(e['syn'])) + (' / 반의어: %s' % ', '.join(e['ant']) if e['ant'] else '')
        if e['loc']: ex += '\n예문 ▶ %s (%s번)\n해석: %s' % (e['loc'][1], e['loc'][0], e['loc'][2])
        syn_items.append({'q': '<b class="en">%s</b> <small>(%s)</small>와(과) 바꿔 쓸 수 있는 말은?' % (e['h'], e['ko']), 'opts': opts, 'ex': ex})
    # ③ 유의어 모두 찾기
    multi = []
    for e in sorted([e for e in E if len(e['syn']) >= 3], key=lambda _: random.random()):
        k = 3 if len(e['syn']) >= 4 or random.random() < .5 else 2
        cor = random.sample(e['syn'], k)
        trap = e['ant'][:1]
        wr = wrong_pool(e, 5 - k - len(trap))
        opts = cor + trap + [s for s, o in wr]
        if len(set(opts)) != len(opts) or len(opts) < 5: continue
        ex = '정답 ▶ %s (%d개)\n이유: %s(%s)와 뜻이 같은 말이에요.' % (', '.join(cor), k, e['h'], e['ko'])
        ex += '\n오답 ▶ ' + ' / '.join(['%s ← 반대말 함정' % t for t in trap] + ['%s(= %s, %s)' % (s, o['h'], o['ko']) for s, o in wr])
        rest = [s for s in e['syn'] if s not in cor]
        ex += '\n포인트 ▶ %s의 유의어 전체: %s' % (e['h'], ', '.join(e['syn'])) + (' (선택지에 없던 것: %s)' % ', '.join(rest) if rest else '')
        multi.append({'q': '<span class="en">%s</span> <span style="font-size:.6em;font-weight:500">(%s)</span>' % (e['h'], e['ko']), 'opts': opts, 'ans': cor, 'ex': ex})
        if len(multi) == 8: break
    # ④ 문장 속 바꿔 쓰기 (②와 다른 유의어로)
    ctx = []
    for e in E:
        if not e['hit'] or e['h'] in NOCTX or len(ctx) >= 8: continue
        cs = [s for s in e['syn'] if s not in heads]
        if not cs: continue
        ans = next((s for s in cs if s != ans2.get(e['h'])), cs[0])
        trap = [a for a in e['ant'] if a not in heads][:1]
        wr = wrong_pool(e, 3 - len(trap))
        n, en, ko, hit = e['loc']
        ctx.append({'q': '밑줄 친 말과 바꿔 써도 뜻이 같은 것은? <small>(%s번 본문 · 선택지는 기본형)</small><br><span class="en">%s</span>' % (n, U(en, hit)),
                    'opts': [ans] + trap + [s for s, o in wr],
                    'ex': '정답 ▶ %s\n이유: 이 문장의 %s는 \'%s\'의 뜻 → %s와 바꿔 쓸 수 있어요.\n해석: %s\n오답 ▶ %s\n포인트 ▶ 같은 자리에 올 수 있는 말: %s' % (
                        ans, hit, e['ko'], ans, ko, ' / '.join(['%s ← 반대말 함정' % t for t in trap] + ['%s(%s)' % (s, o['ko']) for s, o in wr]), ', '.join(e['syn']))})
    # ⑤ 쉬운 단어, 숨은 뜻
    poly = []
    for n in nums:
        for hit, ko_c, trap, oth in POLY.get(n, []):
            r = locate(hit, [n]); assert r, (n, hit)
            _, en, ko = r
            poly.append({'q': '밑줄 친 <b class="en">%s</b>의 이 문장 속 뜻은? <small>(%s번 본문)</small><br><span class="en">%s</span>' % (hit, n, U(en, hit)),
                         'opts': [ko_c, trap] + oth,
                         'ex': '정답 ▶ %s\n이유: 해석 \'%s\' → 여기서 %s는 \'%s\'의 뜻이에요.\n오답 ▶ %s ← 흔히 아는 뜻(함정) / %s\n포인트 ▶ 쉬운 단어일수록 문맥에서 다른 뜻으로 자주 나와요. 해석으로 확인하세요.' % (
                             ko_c, ko, hit, ko_c, trap, ' / '.join(oth))})
    # ⑥ 반대말 함정
    picks = []
    for e in E:
        if e['h'] not in PICK or not e['hit'] or len(picks) >= 6: continue
        n, en, ko, hit = e['loc']; w2 = PICK[e['h']]
        if hit[0].isupper(): w2 = w2.capitalize()
        s = re.sub(r'(?<![A-Za-z])%s(?![A-Za-z])' % re.escape(hit), '{%s|%s}' % (hit, w2), en, count=1)
        picks.append({'s': s, 'ex': '정답 ▶ %s (%s)\n이유: 문맥상 \'%s\'이(가) 맞아요. %s는 반대 뜻이라 글의 흐름이 뒤집혀요.\n해석: %s' % (hit, e['ko'], e['ko'], w2, ko)})
    passage = []
    for n in nums:
        passage.append(['#', '%s번 · 실제 모의고사 원문' % n, ''])
        passage += [['', en, ko] for en, ko in uniq(n)]
    own = set(nums)
    ext = []
    for e in E:
        l = e['loc']
        if l and l[0] not in own and (l[0], l[1], l[2]) not in ext: ext.append((l[0], l[1], l[2]))
    for n in sorted(set(x[0] for x in ext), key=lambda x: int(x.split('~')[0])):
        passage.append(['#', '%s번 · 실제 모의고사 문장 (예문)' % n, ''])
        passage += [['', en, ko] for nn, en, ko in ext if nn == n]
    steps = [{'type': 'vocab', 'title': '변형 어휘 카드', 'guide': '뜻을 고르면 그 단어가 실제 9월 모의고사에서 쓰인 문장과 해석이 함께 나와요.', 'quizN': min(12, len(cards)), 'items': cards}]
    steps.append({'type': 'mc', 'title': '바꿔 쓰기 (영 → 영)', 'guide': '단어와 같은 뜻의 영어를 고르세요. 변형 문제의 어휘 바꾸기가 바로 이 연결이에요. 반대말 함정에 주의!', 'items': syn_items})
    if multi: steps.append({'type': 'multi', 'title': '유의어 모두 찾기', 'guide': '표제어와 뜻이 같은(비슷한) 말을 모두 누른 뒤 확인을 누르세요. 하나라도 빠지거나 더 고르면 오답이에요.', 'items': multi})
    if ctx: steps.append({'type': 'mc', 'title': '문장 속 바꿔 쓰기', 'guide': '실제 본문 문장이에요. 밑줄 친 말 대신 써도 뜻이 그대로인 말을 고르세요.', 'items': ctx})
    if poly: steps.append({'type': 'mc', 'title': '쉬운 단어, 숨은 뜻', 'guide': '아는 단어 같아도 문장 속에서는 다른 뜻일 수 있어요. 해석을 떠올리며 이 문장에서의 뜻을 고르세요.', 'items': poly})
    if picks: steps.append({'type': 'pick', 'title': '반대말 함정 고르기', 'guide': '본문 문장에 맞는 말을 고르세요. 하나는 반대말 함정이에요.', 'items': picks})
    days.append({'id': 'v%d' % i, 'name': '', 'range': '변형 어휘 %d · %s번' % (i, label.replace('번', '')), 'story': '9월 모고 %s · 변형 어휘 (카드 → 영영 → 유의어 모두 → 문장 속 → 숨은 뜻 → 반대말)' % label, 'passage': passage, 'steps': steps})

base_days = [d for d in PK['days'] if not re.match(r'v\d+$', d['id'])]
PK['days'] = base_days + days
for k, d in enumerate(PK['days']): d['name'] = 'DAY %d' % (k + 1)
src = open(path, encoding='utf-8').read(); head = src[:src.index('window.PKG')]
if '변형 어휘 DAY' not in head: head = head.rstrip('\n') + '\n/* 11/15: 변형 어휘 DAY v1~v11 맨 뒤 추가 (generators/gen_js1voc.py) */\n'
write(PK, path, head)
for d in days: print(d['name'], d['range'], [(s['title'], len(s['items'])) for s in d['steps']])
