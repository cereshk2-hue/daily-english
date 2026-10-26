import json, re, sys, copy
sys.path.insert(0, '/tmp/claude-0/-home-claude/a9e3e882-1f02-5d62-8f70-aced81bc59d2/scratchpad')
sys.path.insert(0, '/tmp/claude-0/-home-claude/a9e3e882-1f02-5d62-8f70-aced81bc59d2/scratchpad/split')
from gencommon import write
from split import secs_of, assign
D = '/tmp/claude-0/-home-claude/a9e3e882-1f02-5d62-8f70-aced81bc59d2/scratchpad/split/'
FIX = {'Seoul is known': '26', 'so ______ his sister': '31'}
def nkey(num): return int(str(num).split('~')[0])
def split_pkg(P):
    out, legacy = [], {}
    for d in P['days']:
        secs = secs_of(d); buckets = {c['label']: [] for c in secs}
        for st in d['steps']:
            per = {c['label']: [] for c in secs}
            for q in st['items']:
                if len(secs) == 1: c = secs[0]
                else:
                    c = None
                    for k, v in FIX.items():
                        if k in json.dumps(q, ensure_ascii=False): c = [x for x in secs if x['num'] == v][0]
                    if c is None: c, _ = assign(secs, st, q)
                per[c['label']].append(q)
            for lab, items in per.items():
                if items:
                    s2 = dict(st, items=items)
                    if st['type'] == 'vocab': s2['quizN'] = min(10, len(items))
                    buckets[lab].append(s2)
        # passage rows per section
        rows = {}; cur = None
        for l in d['passage']:
            if l[0] == '#': cur = l[1]; rows[cur] = [l]
            else: rows[cur].append(l)
        ids = []
        for c in secs:
            num = c['num']; nid = 'q' + num.split('~')[0]; kind = c['label'].split('·', 1)[1].strip() if '·' in c['label'] else c['label']
            out.append({'id': nid, 'name': num + '번', 'range': kind, 'story': c['label'], 'passage': rows[c['label']], 'steps': buckets[c['label']], '_num': num})
            ids.append(nid)
        legacy[d['id']] = ids
    return out, legacy

def finish(days):
    days.sort(key=lambda x: nkey(x['_num']))
    for x in days: x.pop('_num', None)
    return days

if __name__ == '__main__':
    # ── 고1 2025년 9월 ──
    P1 = json.load(open(D + 'h1-mock-2509.json'))
    days1, leg1 = split_pkg(P1)
    P1['days'] = finish(days1); P1['pick'] = True; P1['legacy'] = {'map': leg1}
    write(P1, '/home/claude/proj/data/h1-mock-2509.js',
          "/* 고1 2025학년도 9월 전국연합학력평가 영어 18~24 · 26 · 29~31번 — 모의고사는 번호 하나 = DAY 하나, 학생이 번호를 골라 학습\n"
          "   만든 곳: scratchpad/gen_h1m2509b.py(26~31) + 이전 18~24 파일을 split/combine.py 로 번호별로 나눔. legacy.map = 예전 DAY → 새 번호 */\n")

    # ── 고2 2026년 9월 ──
    P2 = json.load(open(D + 'h2-mock-2609-angok.json'))
    days2, leg2 = split_pkg(P2)
    for x in json.load(open(D + 'new_h2.json')):
        days2.append({'id': 'q%d' % x['num'], 'name': '%d번' % x['num'], 'range': x['kind'], 'story': x['label'], 'passage': x['passage'], 'steps': x['steps'], '_num': str(x['num'])})
    P2['days'] = finish(days2)
    P2.update({'id': 'h2-mock-2609', 'school': '고2 모의고사(2026년 9월 학평)', 'unit': '19~24 · 26~27 · 29~30 · 34 · 38 · 40~42번',
               'titleKo': '2026년 9월 고2 학력평가', 'pick': True, 'legacy': {'key': 'daily:h2-mock-2609-angok', 'map': leg2}})
    write(P2, '/home/claude/proj/data/h2-mock-2609.js',
          "/* 고2 2026년 9월 학력평가(인천광역시교육청) 영어 19~24 · 26~27 · 29~30 · 34 · 38 · 40~42번 — 번호 하나 = DAY 하나, 학생이 번호를 골라 학습\n"
          "   만든 곳: scratchpad/gen_m2609.py(24·29·30·34·38·40·41~42, 예전 파일) + gen_m2609b.py(19~23·26·27) → split/combine.py\n"
          "   legacy = 예전 주소(h2-mock-2609-angok)의 기기 기록을 새 번호로 옮겨 '이전 완료'로 보여 줌 */\n")
    for P in (P1, P2):
        print(P['id'], P['unit'], [(d['name'], d['range'], len(d['steps'])) for d in P['days']])
        print('  legacy', P['legacy'])
