import sys, json, subprocess
sys.path.insert(0, '/tmp/claude-0/-home-claude/a9e3e882-1f02-5d62-8f70-aced81bc59d2/scratchpad')
from gencommon import *

# 중1 동아(윤정미): 7과 대화문 · 5과 대화문 · 5과 본문(Who Threw a Cake at the Monalisa?)
# 시험 범위 5·6·7과 (8과 제외). 순서: 6과 → 7과(대화문, 본문) → 5과(대화문, 본문)

def dlg(label, rows):  # rows: [(speaker, en, ko)]
    return [['#', label, '']] + [[s, e, k] for s, e, k in rows]
def T(rows, i): return rows[i][1]

def build(vocab, pickv=(), tf=(), resp=(), pickg=(), verb=(), error=(), scr=(), order=(), insert=(), odd=(), blank=(), func=(), awk=(), ilchi=(), gram=(), summ=(), sec=None):
    st = [{'type': 'vocab', 'title': '핵심어휘·숙어', 'quizN': min(15, len(vocab)), 'items': [[w, m, sec] if sec else [w, m] for w, m in vocab]}]
    def add(lst, s):
        if lst: st.append(s)
    add(pickv, {'type': 'pick', 'title': '어휘선택', 'guide': '문맥에 맞는 낱말을 고르세요.', 'items': [{'s': s, 'ex': x} for s, x in pickv]})
    add(tf, {'type': 'tf', 'title': 'T/F 내용 확인', 'guide': '본문 내용과 일치하면 T, 다르면 F를 고르세요.', 'items': [list(t) for t in tf]})
    add(resp, {'type': 'mc', 'title': '알맞은 응답 고르기', 'guide': '대화의 흐름에 맞는 응답을 고르세요.', 'items': [{'q': '다음 말에 이어질 응답으로 가장 알맞은 것은?<br><b>' + q + '</b>', 'opts': o, 'ex': x} for q, o, x in resp]})
    add(ilchi, {'type': 'mc', 'title': '일치·불일치', 'guide': MCG, 'items': list(ilchi)})
    add(pickg, {'type': 'pick', 'title': '어법선택', 'guide': '어법상 알맞은 것을 고르세요.', 'items': [{'s': s, 'ex': x} for s, x in pickg]})
    add(verb, {'type': 'verb', 'title': '동사변형', 'guide': '( ) 안의 동사를 알맞은 형태로 바꿔 쓰세요.', 'items': [{'s': s, 'v': v, 'a': a, 'ex': x} for s, v, a, x in verb]})
    add(error, {'type': 'error', 'title': '오류찾기', 'guide': '어법상 틀린 곳을 고르세요.', 'items': [{'s': s, 'w': w, 'fix': f, 'ex': x} for s, w, f, x in error]})
    add(scr, {'type': 'scramble', 'title': '본문 스크램블', 'guide': '우리말에 맞게 단어를 눌러 문장을 완성하세요.', 'items': [{'ko': k, 'en': e} for e, k in scr]})
    add(order, {'type': 'order', 'title': '문장순서', 'guide': '대화(문장)를 순서대로 눌러서 배열하세요.', 'items': [{'lines': l, 'flow': f} for l, f in order]})
    add(insert, {'type': 'insert', 'title': '문장삽입', 'guide': '주어진 문장이 들어가기에 가장 알맞은 곳을 고르세요.', 'items': [{'lines': l, 'given': 1, 'flow': f, 'ex': x} for l, f, x in insert]})
    add(odd, {'type': 'odd', 'title': '어색한 문장', 'guide': '글의 흐름과 관계없는 문장을 고르세요.', 'items': [{'lines': l, 'odd': 2, 'ex': x} for l, x in odd]})
    add(blank, {'type': 'blank', 'title': '빈칸추론', 'guide': '빈칸에 들어갈 말로 가장 알맞은 것을 고르세요.', 'items': [{'s': s, 'opts': o, 'ex': x} for s, o, x in blank]})
    add(awk, {'type': 'mc', 'title': '어색한 대화 고르기', 'guide': '짝지어진 대화 중 어색한 것을 고르세요.', 'items': [{'q': '다음 중 짝지어진 대화가 <b>어색한</b> 것은?', 'opts': o, 'ex': x} for o, x in awk]})
    add(func, {'type': 'mc', 'title': '의사소통 기능', 'guide': '상황에 맞는 표현을 고르세요.', 'items': [{'q': q, 'opts': o, 'ex': x} for q, o, x in func]})
    add(gram, {'type': 'mc', 'title': '핵심문법', 'guide': GV, 'items': [{'q': q, 'opts': o, 'ex': x} for q, o, x in gram]})
    add(summ, {'type': 'mc', 'title': '요약문 완성', 'guide': '본문을 읽고 요약문의 빈칸 (A), (B)에 들어갈 말을 고르세요.',
               'items': [{'n': n, 'box': box, 'q': '다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 알맞은 것은?<br><b>' + s + '</b>', 'opts': o, 'ex': x, 'ev': ev} for n, box, s, o, x, ev in summ]})
    return st


ORDER = ['핵심어휘·숙어', '어휘선택', 'T/F 내용 확인', '알맞은 응답 고르기', '일치·불일치', '어법선택', '동사변형', '오류찾기', '본문 스크램블', '문장순서', '문장삽입', '어색한 문장', '빈칸추론', '어색한 대화 고르기', '의사소통 기능', '핵심문법', '요약문 완성']
import re as _re
def _norm(s): return _re.sub(r'\s+', ' ', _re.sub(r'<[^>]+>', ' ', str(s))).lower()
def _text(st, q):
    t = st['type']
    if t == 'vocab': return None
    if t == 'pick': return _re.sub(r'\{([^}|]*)[^}]*\}', r'\1', q['s'])
    if t == 'verb': return q['s'].replace('___', q['a'][0])
    if t == 'error':
        k = [0]
        def f(m):
            r = q['fix'] if k[0] == q['w'] else m.group(1); k[0] += 1; return r
        return _re.sub(r'\[\[(.+?)\]\]', f, q['s'])
    if t == 'blank': return q['s'].replace('____', q['opts'][0])
    if t == 'tf': return q[4]
    if t == 'scramble': return q['en']
    if t in ('order', 'insert', 'odd'): return q['lines'][0]
    return None
def split(steps, passage, parts):
    """parts: list of lists of '#' labels. 대화문 DAY를 10분 분량으로 쪼갠다."""
    texts, cur = [''] * len(parts), None
    for l in passage:
        if l[0] == '#': cur = next((i for i, p in enumerate(parts) if l[1] in p), None); continue
        if cur is not None: texts[cur] += ' ' + l[1]
    texts = [_norm(t) for t in texts]
    out = [[] for _ in parts]
    for st in steps:
        buck = [[] for _ in parts]; rr = 0
        for q in st['items']:
            i = None
            if st['type'] == 'vocab':
                w = _re.sub(r"[~?']|\b(be|a|the)\b", ' ', q[0].lower()).split()
                w = max(w, key=len) if w else ''
                i = next((j for j, t in enumerate(texts) if w[:5] in t), None)
                if i is None: i = min(range(len(parts)), key=lambda j: len(buck[j]))
            elif isinstance(q, dict) and q.get('box'):
                i = next(j for j, p in enumerate(parts) if q['box'][0] in p)
            else:
                s = _text(st, q)
                if s: i = next((j for j, t in enumerate(texts) if _norm(s).rstrip('.?!') in t), None)
                if i is None: i = rr % len(parts); rr += 1
            buck[i].append(q)
        for j, b in enumerate(buck):
            if b:
                s2 = dict(st); s2['items'] = b
                if st['type'] == 'vocab': s2['quizN'] = min(12, len(b))
                out[j].append(s2)
    return out
def add(steps, title, proto, items):
    for s in steps:
        if s['title'] == title: s['items'] += items; return
    s = dict(proto); s['items'] = list(items)
    k = ORDER.index(title); pos = next((i for i, x in enumerate(steps) if ORDER.index(x['title']) > k), len(steps))
    steps.insert(pos, s)
MCST = {'type': 'mc', 'title': '일치·불일치', 'guide': MCG}
SUMST = {'type': 'mc', 'title': '요약문 완성', 'guide': '본문을 읽고 요약문의 빈칸 (A), (B)에 들어갈 말을 고르세요.'}
SUMQ = '다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 알맞은 것은?'
def summ(box, s, o, x, ev): return {'box': box, 'q': SUMQ + '<br><b>' + s + '</b>', 'opts': o, 'ex': x, 'ev': ev}
def sub(passage, labels):
    out, on = [], False
    for l in passage:
        if l[0] == '#': on = l[1] in labels
        if on: out.append(l)
    return out

# ── 앱은 opts[0]을 정답으로 채점한다(보기는 화면에서 섞임). 해설의 '정답 ▶ X'에 맞는 보기를 맨 앞으로 옮긴다 ──
def _st(s): return _re.sub(r'<[^>]+>', '', str(s)).strip()
def ansfirst(steps):
    for st in steps:
        if st['type'] not in ('mc', 'blank'): continue
        for q in st['items']:
            m = _re.search(r'정답 ▶ ([^\n]+)', q.get('ex', ''))
            if not m: continue
            a = _st(m.group(1)); a2 = _re.sub(r'\s*\(.*$', '', a)
            idx = next((i for i, o in enumerate(q['opts']) if _st(o) in (a, a2) or _st(o).startswith(a2)), None)
            assert idx is not None, ('정답 보기 없음', a, q['opts'])
            if idx:
                q['opts'].insert(0, q['opts'].pop(idx))
                if q.get('per'): q['per'].insert(0, q['per'].pop(idx))
    return steps
