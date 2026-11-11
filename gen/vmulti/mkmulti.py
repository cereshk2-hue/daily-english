# 11/11 대진고 고2 능률(오선영) 3과 어휘 DAY v1~v4: '유의어 고르기(하나)' → '뜻이 같은 말 모두 고르기'(정답 1개~전부), 쉬운 것부터 순서 변경
#   단어장 → 모두 고르기 → 반의어 고르기 → 뜻 보고 철자 쓰기 → 유의어·반의어 쓰기
import sys, json, subprocess, re, random
sys.path.insert(0, '/home/claude/work/gen')
from gencommon import write
path = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/proj/data/h2-ne-oh-L3.js'
PK = json.loads(subprocess.check_output(['node', '-e', "global.window={};require('%s');process.stdout.write(JSON.stringify(window.PKG))" % path]))
W = []
for d in PK['days']:
    if not re.match(r'v[1-4]$', d['id']): continue
    for l in d['passage']:
        if l[0] == '#': continue
        no, w = l[1].split('. ', 1); parts = l[2].split(' | ')
        syn = next((p[2:].split(', ') for p in parts if p.startswith('= ')), [])
        ant = next((p[2:].split(', ') for p in parts if p.startswith('↔ ')), [])
        W.append({'no': int(no), 'w': w, 'm': parts[0], 'syn': syn, 'ant': ant, 'day': d['id']})
assert len(W) == 52, len(W)
# 뜻이 겹쳐 오답으로 쓰면 안 되는 말 (gen_h2vocab.py EXCL + 추가 검토)
EXCL = {'conflict': ['contend', 'argue', 'differ', 'vary', 'diverge'], 'represent': ['clarify', 'show', 'signify', 'point out', 'demonstrate'], 'indicate': ['symbolize', 'stand for', 'depict', 'demonstrate', 'clarify'],
        'illustrate': ['show', 'depict', 'signify', 'symbolize', 'point out'], 'ideal': ['excellent', 'faultless', 'impeccable', 'outstanding', 'flawless', 'superior'], 'weigh': ['inspect', 'investigate', 'scrutinize', 'examine', 'compare'],
        'uncomplicated': ['direct', 'straight', 'clear', 'evident', 'apparent', 'obvious'], 'yield': ['create', 'make'], 'encourage': ['support', 'help'], 'method': ['way', 'system'], 'entire': ['all'],
        'pursue': ['follow'], 'efficient': ['effective'], 'determine': ['decide', 'conclude', 'establish'], 'significant': ['major', 'important', 'considerable', 'substantial'], 'obvious': ['clear'], 'primary': ['main', 'chief', 'principal'], 'matter': ['crucial', 'substantial', 'considerable', 'important', 'significant']}
def kw(m): return set(t for t in re.split(r'[,\s()\[\]·~]+', re.sub(r'\[.*?\]', '', m)) if len(t) >= 2)
def related(x):
    bag = set(x['syn'] + x['ant'] + [x['w']]) | set(EXCL.get(x['w'], []))
    for w in W:
        if w is not x and (set(w['syn'] + [w['w']]) & set(x['syn'] + [x['w']]) or set(w['ant']) & set(x['ant']) or kw(w['m']) & kw(x['m'])):
            bag |= set(w['syn'] + w['ant'] + [w['w']])
    for k, v in EXCL.items():
        if x['w'] in v: bag |= set([k] + next(w['syn'] for w in W if w['w'] == k))
    return bag
OWN = {}
for w in W:
    for s in w['syn']: OWN.setdefault(s, w)
def multi(x):
    r = random.Random('multi-' + x['w'])
    N = 5
    c = r.randint(1, min(len(x['syn']), N))      # 정답 수: 1개 ~ 유의어 수(최대 5)
    if c == len(x['syn']) >= 3 and r.random() < 0.6: N = c   # 가끔은 보기 전부가 정답
    right = r.sample(x['syn'], c)
    bad = related(x)
    cand = sorted(set(s for w in W if w is not x for s in w['syn'] if s not in bad and len(s.split()) <= 3))
    wrong = r.sample(cand, N - c)
    opts = right + wrong
    ex = '정답 ▶ %s (%d개)\n이유: %s(%s)의 유의어 ▶ %s' % (', '.join(right), c, x['w'], x['m'], ', '.join(x['syn']))
    if wrong: ex += '\n오답 ▶ ' + ' / '.join('%s(%s의 유의어 · %s)' % (o, OWN[o]['w'], OWN[o]['m']) for o in wrong)
    return {'q': '<span class="en">%s</span> <span style="font-size:.6em;font-weight:500">(%s)</span>' % (x['w'], x['m']), 'opts': opts, 'ans': right, 'ex': ex}
cnt = {}
for d in PK['days']:
    if not re.match(r'v[1-4]$', d['id']): continue
    ws = [w for w in W if w['day'] == d['id']]
    items = [multi(w) for w in ws if w['syn']]
    for it in items: cnt[len(it['ans'])] = cnt.get(len(it['ans']), 0) + 1
    S = {s['title']: s for s in d['steps']}
    new = [S['단어장 (뜻 익히기)'], {'type': 'multi', 'title': '뜻이 같은 말 모두 고르기', 'guide': '표제어와 뜻이 같은(비슷한) 말을 모두 누른 뒤 확인을 누르세요. 정답은 1개일 수도, 전부일 수도 있어요. 하나라도 빠지거나 더 고르면 오답이에요.', 'items': items}]
    if '반의어 고르기' in S: new.append(S['반의어 고르기'])
    new.append(S['뜻 보고 철자 쓰기'])
    if '유의어·반의어 쓰기' in S: new.append(S['유의어·반의어 쓰기'])
    d['steps'] = new
    d['story'] = d['story'].replace('(뜻 · 철자 · 유의어 · 반의어)', '(뜻 · 유의어 모두 고르기 · 반의어 · 철자)')
src = open(path, encoding='utf-8').read(); head = src[:src.index('window.PKG')]
tail = src[src.index('/* WRAPUP-TESTS'):] if '/* WRAPUP-TESTS' in src else ''
if '모두 고르기' not in head: head = head.rstrip('\n') + "\n/* 11/11: 어휘 DAY v1~v4 '뜻이 같은 말 모두 고르기'(multi, 정답 1개~전부) 추가 · 쉬운 단계부터 순서 변경. work/vmulti/mkmulti.py */\n"
PK.pop('tests', None)
write(PK, path, head)
if tail: open(path, 'a', encoding='utf-8').write(tail)
print('정답 수 분포', sorted(cnt.items()))
for d in PK['days']:
    if re.match(r'v[1-4]$', d['id']):
        for it in d['steps'][1]['items']: print(re.sub('<[^>]+>', '', it['q']), '| O:', it['ans'], '| X:', [o for o in it['opts'] if o not in it['ans']])
