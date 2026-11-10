# 고2 능률(오선영) 영어Ⅱ Lesson 4 Create a Greener Tomorrow — 본문 DAY 공통 (fw.py 헬퍼 재사용)
import json, re
from fw import P, PK, VB, ER, BL, TF, MC, G, short, box
R = json.load(open('/home/claude/work/oh4/raw.json', encoding='utf-8'))
fix = lambda t: t.replace('’', "'").replace('‘', "'")
SEC, HEAD = {}, {}
for s in R:
    SEC[s['sec']] = P(s['sec'], s['sec'], [(fix(e), k) for e, k in zip(s['E'], s['K'])]); HEAD[s['sec']] = s['head']
def E(sec, i): return SEC[sec].E[i]
def K(sec, i): return SEC[sec].K[i]
def V(sec, rows): return [[w, m, sec] + list(x) for w, m, *x in rows]
def passage(secs):
    rows = []
    for s in secs:
        rows.append(['', s, ''])
        if HEAD[s]: rows.append(['', HEAD[s][0], HEAD[s][1]])
        rows += [['', e, k] for e, k in zip(SEC[s].E, SEC[s].K)]
    return rows
def MULTI(q, opts, ex, per, secs):
    txt = ' '.join(e for s in secs for e in SEC[s].E)
    for x in per: assert not x[1] or x[1] in txt, x[1]
    return {'n': secs[0], 'box': list(secs), 'q': q, 'opts': opts, 'ex': ex, 'per': per}
def day(id, name, rng, story, secs, m):
    L = lambda c: E(*c) if isinstance(c, tuple) else c
    st = [{'type': 'vocab', 'title': '핵심어휘·숙어', 'quizN': 15, 'items': m.VOCAB},
          {'type': 'pick', 'title': '어휘선택', 'guide': G['pick1'], 'items': m.PICK1},
          {'type': 'tf', 'title': 'T/F 내용 확인', 'guide': G['tf'], 'items': m.TF},
          {'type': 'mc', 'title': '일치·불일치', 'guide': G['mc'], 'items': m.MC},
          {'type': 'pick', 'title': '어법선택', 'guide': G['pick2'], 'items': m.PICK2},
          {'type': 'verb', 'title': '동사변형', 'guide': G['verb'], 'items': m.VERB},
          {'type': 'error', 'title': '오류찾기', 'guide': G['error'], 'items': m.ERR},
          {'type': 'scramble', 'title': '본문 스크램블', 'guide': G['scramble'], 'items': [{'ko': K(*c), 'en': E(*c)} for c in m.SCR]},
          {'type': 'order', 'title': '문장순서', 'guide': G['order'], 'items': [{'lines': [E(*c) for c in o], 'flow': [short(K(*c)) for c in o]} for o in m.ORDER]},
          {'type': 'insert', 'title': '문장삽입', 'guide': G['insert'], 'items': [{'lines': [E(*c) for c in o[0]], 'given': o[1], 'flow': [short(K(*c)) for c in o[0]], 'ex': o[2]} for o in m.INSERT]},
          {'type': 'odd', 'title': '어색한 문장', 'guide': G['odd'], 'items': [{'lines': [L(c) for c in o[0]], 'odd': o[1], 'ex': o[2]} for o in m.ODD]},
          {'type': 'blank', 'title': '빈칸추론', 'guide': G['blank'], 'items': m.BLANK},
          {'type': 'mc', 'title': '핵심문법', 'guide': G['gram'], 'items': m.GRAM}]
    return {'id': id, 'name': name, 'range': rng, 'story': story, 'passage': passage(secs), 'steps': [s for s in st if s['items']]}
