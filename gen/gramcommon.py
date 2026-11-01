import sys, re, json, subprocess
sys.path.insert(0, '/home/claude/work/gen')
from gencommon import write
from dlgcommon import ansfirst
# 문법 DAY 공통 도구 (gen_v7gram.py에서 뽑음)

class Day:
    def __init__(s, did, rng, story):
        s.d = {'id': did, 'name': 'DAY', 'range': rng, 'story': story, 'passage': [], 'steps': []}
        s.notes, s.ex, s.seen = [], [], set()
    def note(s, title, rows):
        s.notes.append(['#', title, '']); s.notes += [['', a, b] for a, b in rows]
    def sent(s, en, ko):
        en = re.sub(r'<[^>]+>', '', en)
        if en not in s.seen: s.seen.add(en); s.ex.append(['', en, ko])
    def step(s, st): s.d['steps'].append(st); return st
    def done(s):
        s.d['passage'] = s.notes + ([['#', '예문', '']] + s.ex if s.ex else [])
        return s.d

def cards(title, items, n=None, guide='카드를 한 번 읽고, 퀴즈에서 짝이 맞는 것을 고르세요.'): return {'type': 'vocab', 'title': title, 'guide': guide, 'quizN': n or len(items), 'items': [list(x) for x in items]}
def SCARDS(D, title, items, n=None, guide=''):
    for en, ko in items: D.sent(en, re.sub(r' \([^)]*\)$', '', ko))
    return cards(title, items, n, guide)
def TF(title, items, guide='맞으면 T, 틀리면 F를 고르세요.'): return {'type': 'tf', 'title': title, 'guide': guide, 'items': [[a, b, c, None, None] for a, b, c in items]}
def MC(title, items, guide='알맞은 답을 고르세요.'):
    return {'type': 'mc', 'title': title, 'guide': guide, 'items': [dict({'q': it[0], 'opts': it[1], 'ex': it[2]}, **({'sort': True} if len(it) > 3 and it[3] else {})) for it in items]}
def PICK(D, title, items, guide='어법상 알맞은 것을 고르세요.'):
    for s, ko, x in items: D.sent(re.sub(r'\{([^|}]*)\|[^}]*\}', r'\1', s), ko)
    return {'type': 'pick', 'title': title, 'guide': guide, 'items': [{'s': s, 'ex': x} for s, ko, x in items]}
def SCR(D, title, items, guide='우리말에 맞게 단어를 눌러 문장을 완성하세요.'):
    for en, ko in items: D.sent(en, ko)
    return {'type': 'scramble', 'title': title, 'guide': guide, 'items': [{'ko': ko, 'en': en} for en, ko in items]}
def ERR(D, title, items):
    for s, w, f, ko, x in items:
        k = [0]
        def rep(m):
            r = f if k[0] == w else m.group(1); k[0] += 1; return r
        D.sent(re.sub(r'\s+', ' ', re.sub(r'\[\[(.+?)\]\]', rep, s)).strip(), ko)
    return {'type': 'error', 'title': title, 'guide': '어법상 틀린 곳을 고르세요.', 'items': [{'s': s, 'w': w, 'fix': f, 'ex': x} for s, w, f, ko, x in items]}
U = lambda s, u: s.replace(u, '<u>' + u + '</u>', 1)
def Q(en, u=None): return '<br><b>' + (U(en, u) if u else en) + '</b>'

