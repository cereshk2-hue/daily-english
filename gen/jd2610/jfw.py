# 저동고1 · 2026년 10월 고1 학평(경기) 한 지문 = 하루. fw.py(안곡고2)에 요약문 단계 · 원자료(prep.json) 로더 · 어휘 파서 추가
import json, re
from fw import *
PREP = json.load(open('/home/claude/work/jd2610/prep.json', encoding='utf-8'))
Q = json.load(open('/home/claude/work/jd2610/q.json', encoding='utf-8'))
def load(n, label, fix_ko=None, sents=None, foot=None):
    v = PREP[str(n)]; E = sents or v['sents']; K = list(v['ko'])
    for i, k in (fix_ko or {}).items():
        if i == 'ins': continue
    if fix_ko and 'ins' in fix_ko:
        for i, k in fix_ko['ins']: K.insert(i, k)
    for i, k in (fix_ko or {}).items():
        if isinstance(i, int): K[i] = k
    assert len(E) == len(K), (n, len(E), len(K))
    f = foot if foot is not None else ' '.join(Q[str(n)]['foot'])
    return P(n, label, list(zip(E, K)), f)
def words(n, drop=(), add=()):
    """해설서 WORDS & EXPRESSIONS → [[단어, 뜻]] (탭 없는 줄은 앞 뜻에 이어 붙임)"""
    out = []
    for l in Q[str(n)]['words'].split('\n'):
        if not l.strip(): continue
        if '\t' in l:
            w, m = l.split('\t', 1); out.append([w.strip().lstrip('*'), re.sub(r'\s+', ' ', m.replace('\t', ' ')).strip()])
        elif re.match(r'^[A-Za-z*]', l.strip()) and out and out[-1][1]:
            out.append([l.strip().lstrip('*'), ''])
        elif out:
            prev = out[-1][1]
            out[-1][1] = (prev + (' ' if prev else '') + l.strip()).strip()
    out = [[w, re.sub(r'\s+', ' ', m).strip().rstrip(',;').strip()] for w, m in out]
    out = [[w, m] for w, m in out if w and m and w not in drop and ':' not in w and not m.startswith('(') and '학력평가' not in m]
    return out + [list(a) for a in add]
def SUM(p, q, opts, ex, ev):
    for e in ev: assert e in p.text(), (p.n, e)
    return {'n': p.n, 'box': [p.label], 'q': '다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 알맞은 것은?<br><b>' + q + '</b>', 'opts': opts, 'ex': ex, 'ev': ev}
def jday(n, name, rng, story, p, m):
    d = day('q%s' % n, name, rng, story, p, m)
    if getattr(m, 'SUMQ', None): d['steps'].append({'type': 'mc', 'title': '요약문 완성', 'guide': '지문을 읽고 요약문의 빈칸 (A), (B)에 들어갈 말을 고르세요.', 'items': m.SUMQ})
    return d
def raw(n): return ' '.join(Q[str(n)]['ps'])
def underlined(n, spans, text=None):
    """원문항 그대로(①~⑤ 표시 포함) + 밑줄: spans = ['mean', 'making', ...] 순서대로 ①~⑤ 뒤 낱말"""
    t = text or raw(n)
    for i, w in enumerate(spans):
        m = CIR[i] + w; assert m in t, (n, m); t = t.replace(m, CIR[i] + '<u>' + w + '</u>', 1)
    f = ' '.join(Q[str(n)]['foot'])
    return box(t + ('<br><small>' + f + '</small>' if f else ''))
def spread(d, n):
    """변형 문항(keep) 정답 위치 고르게: 정답을 target 자리로 옮기고 해설의 ①~⑤ 번호도 같이 바꿈"""
    k = 0
    for st in d['steps']:
        if st['title'] != '실전 문항': continue
        for it in st['items']:
            if not it['q'].startswith('<b>[변형]'): continue
            k += 1; L = len(it['opts']); a = it['a']; t = (int(n) * 3 + k * 2) % L
            rest = [i for i in range(L) if i != a]; order = rest[:t] + [a] + rest[t:]
            mp = {old: new for new, old in enumerate(order)}
            it['opts'] = [it['opts'][i] for i in order]; it['a'] = t
            it['ex'] = re.sub('[①②③④⑤]', lambda m: CIR[mp[CIR.index(m.group())]] if CIR.index(m.group()) < L else m.group(), it['ex'])
    return d
