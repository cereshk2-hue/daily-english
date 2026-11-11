# 11/11 대진고 고2 능률(오선영) Lesson 4 어휘 DAY w1~w4 (학습지 62개, table.py). 3과 어휘를 쉽게 바꾼 순서 그대로:
#   단어장 → 뜻이 같은 말 모두 고르기(정답 1개~전부) → 반의어 고르기 → 뜻 보고 철자 쓰기 → 유의어·반의어 쓰기(학습지 빈칸)
import sys, json, subprocess, re, random
sys.path.insert(0, '/home/claude/work/gen'); sys.path.insert(0, '/home/claude/work/oh4v')
from gencommon import write
from dlgcommon import ansfirst
from table import T
W = [{'no': a, 'w': b, 'm': c, 'syn': d, 'ant': e, 'bl': f, 'note': g} for a, b, c, d, e, f, g in T]
EXCL = {'hazard': ['hazardous', 'lethal', 'noxious'], 'toxic': ['danger', 'risk', 'threat', 'peril'], 'limit': ['ban', 'bar', 'inhibit', 'forbid', 'disallow', 'preclude'],
        'prohibit': ['restrict', 'confine', 'circumscribe'], 'state': ['claim', 'request'], 'demand': ['declare', 'express', 'specify'], 'predict': ['expect', 'anticipate'],
        'anticipate': ['forecast', 'project'], 'generate': ['bring about', 'arise', 'happen'], 'occur': ['bring about', 'give rise to', 'spawn'], 'approach': ['angle', 'viewpoint'],
        'perspective': ['method', 'strategy', 'tactic'], 'transition': ['cycle', 'rotation', 'vary', 'fluctuate'], 'cycle': ['change', 'shift', 'transformation'], 'range': ['change', 'shift'],
        'material': ['component', 'factor', 'part'], 'element': ['substance'], 'repair': ['maintenance', 'care', 'upkeep', 'preservation'], 'maintenance': ['fix', 'mend', 'restore'],
        'extend': ['promote'], 'foster': ['lengthen', 'prolong', 'elongate'], 'appliance': ['component', 'part'], 'reasonable': ['realistic', 'feasible', 'informed'], 'informed': ['sensible', 'practical'],
        'empower': ['sanction', 'enactment', 'regulation'], 'legislation': ['act', 'proposed law', 'authorize', 'entitle'], 'bill': ['enactment', 'regulation'], 'index': ['label', 'tag', 'mark', 'sticker'],
        'label': ['indicator', 'measure', 'gauge'], 'invaluable': ['ingenious', 'inventive'], 'innovative': ['priceless', 'extremely valuable'], 'advocate': ['promote', 'nurture'],
        'acquire': ['secure'], 'obtain': ['attain', 'procure', 'garner'], 'install': ['embed'], 'glance': ['angle', 'outlook'], 'alarming': ['hazardous', 'lethal'], 'discard': ['eradicate', 'get rid of'], 'crack': ['harm', 'impair', 'injure']}
def kw(m): return set(t for t in re.split(r'[,\s()\[\]·~;]+', m) if len(t) >= 2)
def related(x):
    bag = set(x['syn'] + x['ant'] + [x['w']]) | set(EXCL.get(x['w'], []))
    for w in W:
        if w is not x and (set(w['syn'] + [w['w']]) & set(x['syn'] + [x['w']]) or kw(w['m']) & kw(x['m'])):
            bag |= set(w['syn'] + w['ant'] + [w['w']])
    for k, v in EXCL.items():
        if x['w'] in v: bag |= set([k] + next(w['syn'] for w in W if w['w'] == k))
    return bag
OWNS = {}; OWNA = {}
for w in W:
    for s in w['syn']: OWNS.setdefault(s, w)
    for s in w['ant']: OWNA.setdefault(s, w)
def multi(x):
    r = random.Random('m4-' + x['w']); N = 5
    c = r.randint(1, min(len(x['syn']), N))
    if c == len(x['syn']) >= 3 and r.random() < 0.6: N = c
    right = r.sample(x['syn'], c); bad = related(x)
    cand = sorted(set(s for w in W if w is not x for s in w['syn'] if s not in bad))
    wrong = r.sample(cand, N - c)
    ex = '정답 ▶ %s (%d개)\n이유: %s(%s)의 유의어 ▶ %s' % (', '.join(right), c, x['w'], x['m'], ', '.join(x['syn']))
    if wrong: ex += '\n오답 ▶ ' + ' / '.join('%s(%s의 유의어 · %s)' % (o, OWNS[o]['w'], OWNS[o]['m']) for o in wrong)
    return {'q': '<span class="en">%s</span> <span style="font-size:.6em;font-weight:500">(%s)</span>' % (x['w'], x['m']), 'opts': right + wrong, 'ans': right, 'ex': ex}
def antq(x):
    r = random.Random('a4-' + x['w']); right = x['ant'][0]; bad = related(x)
    cand = sorted(set(s for w in W if w is not x for s in w['ant'] if s not in bad and s != right))
    wrong = r.sample(cand, 3)
    return {'q': '<b>%s</b> (%s)의 반의어로 알맞은 것은?' % (x['w'], x['m']), 'opts': [right] + wrong,
            'ex': '정답 ▶ %s\n이유: %s의 반의어 ▶ %s\n오답 ▶ %s' % (right, x['w'], ', '.join(x['ant']), ' / '.join('%s(%s의 반의어)' % (o, OWNA[o]['w']) for o in wrong))}
def mask(word, pre=None):
    if pre: return pre + '□' * (len(word) - len(pre))
    return ' '.join(p[0] + '□' * (len(p) - 1) for p in word.split(' '))
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
def spell(x):
    hw = next((b for b in x['bl'] if b[0] == 'w'), None)
    if x['w'] == 'take into account': return {'s': '%s → take into ___' % x['m'], 'v': mask('account', 'a'), 'mask': mask('account', 'a'), 'a': ['account'], 'ex': exw(x)}
    if x['w'] == 'dispose of': return {'s': '%s → ___ of' % x['m'], 'v': mask('dispose', 'd'), 'mask': mask('dispose', 'd'), 'a': ['dispose'], 'ex': exw(x)}
    mk = mask(x['w'], hw[1] if hw else None) if ' ' not in x['w'] else mask(x['w'])
    return {'s': '%s → ___' % x['m'], 'v': mk, 'mask': mk, 'a': [x['w']], 'ex': exw(x)}
def blanks(x):
    out = []
    for kind, pre, a in x['bl']:
        if kind == 'w': continue
        lst = x['syn'] if kind == 'syn' else x['ant']
        assert a in lst, (x['w'], a); mk = mask(a, pre)
        shown = ', '.join('___' if t == a else t for t in lst)
        out.append({'s': '%s (%s) %s %s' % (x['w'], x['m'], '=' if kind == 'syn' else '↔', shown), 'v': mk, 'mask': mk, 'a': [a],
                    'ex': '정답 ▶ %s\n이유: %s(%s)의 %s ▶ %s' % (a, x['w'], x['m'], '유의어' if kind == 'syn' else '반의어', ', '.join(lst))})
    return out
def day(i, lo, hi):
    ws = [w for w in W if lo <= w['no'] <= hi]
    P = [['#', 'Lesson 4 어휘 %d~%d번' % (lo, hi), '']] + [['', '%d. %s' % (w['no'], w['w']), card(w)] for w in ws]
    st = [{'type': 'vocab', 'title': '단어장 (뜻 익히기)', 'quizN': len(ws), 'items': [[w['w'], w['m']] for w in ws]},
          {'type': 'multi', 'title': '뜻이 같은 말 모두 고르기', 'guide': '표제어와 뜻이 같은(비슷한) 말을 모두 누른 뒤 확인을 누르세요. 정답은 1개일 수도, 전부일 수도 있어요. 하나라도 빠지거나 더 고르면 오답이에요.', 'items': [multi(w) for w in ws if w['syn']]}]
    an = [antq(w) for w in ws if w['ant']]
    if an: st.append({'type': 'mc', 'title': '반의어 고르기', 'guide': '표제어와 뜻이 반대인 말을 고르세요.', 'items': an})
    st.append({'type': 'verb', 'title': '뜻 보고 철자 쓰기', 'guide': '우리말 뜻을 보고, 앞글자와 네모칸 수에 맞게 단어를 쓰세요.', 'free': True, 'ph': '단어 쓰기', 'items': [spell(w) for w in ws]})
    b = [it for w in ws for it in blanks(w)]
    if b: st.append({'type': 'verb', 'title': '유의어·반의어 쓰기', 'guide': '학습지 빈칸 그대로예요. 앞글자와 네모칸 수에 맞게 쓰세요. (서술형 대비)', 'free': True, 'ph': '단어 쓰기', 'items': b})
    return {'id': 'w%d' % i, 'name': 'DAY', 'range': '4과 어휘 %s %d~%d번' % ('①②③④'[i - 1], lo, hi), 'story': 'Lesson 4 어휘 · %d~%d번 (뜻 · 유의어 모두 고르기 · 반의어 · 철자)' % (lo, hi), 'passage': P, 'steps': st}
V = [day(1, 1, 16), day(2, 17, 31), day(3, 32, 47), day(4, 48, 62)]
for d in V: ansfirst([s for s in d['steps'] if s['type'] == 'mc'])
path = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/proj/data/h2-ne-oh-L3.js'
PK = json.loads(subprocess.check_output(['node', '-e', "global.window={};require('%s');process.stdout.write(JSON.stringify(window.PKG))" % path]))
PK['days'] = [d for d in PK['days'] if not re.match(r'w\d$', d['id'])] + V
for i, d in enumerate(PK['days']): d['name'] = 'DAY %d' % (i + 1)
src = open(path, encoding='utf-8').read(); head = src[:src.index('window.PKG')]
tail = src[src.index('/* WRAPUP-TESTS'):] if '/* WRAPUP-TESTS' in src else ''
if '4과 어휘' not in head: head = head.rstrip('\n') + '\n/* 11/11: 4과 어휘 DAY w1~w4 (대진고 L4 어휘 학습지 62개) work/oh4v/mk4vocab.py + table.py */\n'
PK.pop('tests', None)
write(PK, path, head)
if tail: open(path, 'a', encoding='utf-8').write(tail)
for d in V:
    print(d['range'], [(s['title'], len(s['items'])) for s in d['steps']])
    for it in d['steps'][1]['items']: print('   ', re.sub('<[^>]+>', '', it['q']), '| O', it['ans'], '| X', [o for o in it['opts'] if o not in it['ans']])
