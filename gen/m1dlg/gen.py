# 11/27 중산중1 대화문 꿰뚫기 DAY 만들기 (과별 데이터 l5.py · l6.py · l7.py) → m1-donga-yoon-L6 맨 끝
import sys, json, re, subprocess, importlib
sys.path.insert(0, '/home/claude/srcrepo/generators'); sys.path.insert(0, '/home/claude/srcrepo/gen/m1dlg')
from gencommon import write
path = '/home/claude/proj/data/m1-donga-yoon-L6.js'
LESSONS = sys.argv[1:] or ['l5']
src = open(path, encoding='utf-8').read(); cut = src.index('/* WRAPUP-TESTS'); head, tail = src[:src.index('window.PKG')], src[cut:]
PK = json.loads(subprocess.check_output(['node', '-e', "global.window={};eval(require('fs').readFileSync(0,'utf8'));process.stdout.write(JSON.stringify(window.PKG))"], input=src[:cut].encode()))
D = {d['id']: d for d in PK['days']}
def norm(t): return re.sub(r'\s+', ' ', t.replace('’', "'")).strip().lower()
def build(gid, c):
    P = D[c['src']]['passage']; TX = {norm(l[1]) for l in P if l[0] != '#'}
    for _, lines, flow in c['order']: assert all(norm(l) in TX for l in lines), lines; assert len(lines) == len(flow)
    for ko, en in c['scr']: assert norm(en) in norm(' '.join(TX)), en
    for s, ex in c['pick']: assert norm(re.sub(r'\{([^|}]*)\|[^}]*\}', r'\1', s)).split(': ', 1)[-1] in norm(' '.join(TX)), s
    for s, v, a in c['verb']: assert norm(s.replace('___', a[0])) in norm(' '.join(TX)), s
    for s, b, ev, why in c['tf']: assert norm(ev) in norm(' '.join(TX)), ev
    mc = []
    for q, opts, why in c['mc']:
        assert len(opts) == 5 and len(set(opts)) == 5
        mc.append({'q': q, 'opts': opts, 'ex': '정답 ▶ %s\n이유: %s\n오답 ▶ %s' % (opts[0], why, ' / '.join(opts[1:]))})
    n = len(c['scr'])
    return {'id': gid, 'name': '', 'range': c['range'],
            'story': '%s · 대화문 꿰뚫기 (표현 카드 → 대화 순서 → 고르기 → 모든 줄 스크램블 %d → 표현 쓰기 %d → T/F %d → 상황·심경·기능 %d)' % (c['range'], n, len(c['verb']), len(c['tf']), len(mc)),
            'passage': P,
            'steps': [
             {'type': 'vocab', 'title': '대화 핵심 표현', 'guide': '대화에 나오는 표현이에요. 뜻을 정확히 익혀요.', 'quizN': min(10, len(c['vocab'])), 'items': c['vocab']},
             {'type': 'order', 'title': '대화 순서 맞추기', 'tries': 3, 'guide': '대화 한 편을 처음부터 끝까지 순서대로 놓아요. 묻는 말 → 대답, 허락 구하기 → 허락/거절 → 이유의 흐름을 떠올려요.',
              'items': [{'lines': lines, 'flow': flow} for _, lines, flow in c['order']]},
             {'type': 'pick', 'title': '어법·의미 고르기', 'guide': '대화 속 헷갈리는 말을 골라요.', 'items': [{'s': s, 'ex': ex} for s, ex in c['pick']]},
             {'type': 'scramble', 'title': '모든 줄 스크램블', 'guide': '대화의 모든 줄을 우리말 보고 영어로 완성해요. 이것만 다 하면 대화가 통째로 외워져요.', 'items': [{'ko': ko, 'en': en} for ko, en in c['scr']]},
             {'type': 'verb', 'title': '핵심 표현 쓰기', 'ph': '영어로 쓰기', 'guide': '빈칸에 들어갈 영어를 직접 써요(괄호 속 우리말 힌트).', 'items': [{'s': s, 'v': v, 'a': a, 'ex': '정답 ▶ %s' % ' / '.join(a)} for s, v, a in c['verb']]},
             {'type': 'tf', 'title': '대화 내용 T/F', 'guide': '누가 무엇을 했는지, 허락했는지 금지했는지 꼼꼼히 확인해요.', 'items': [[s, b, '정답 ▶ %s\n이유: %s\n근거 ▶ %s' % ('T' if b else 'F', why, ev), None, ev] for s, b, ev, why in c['tf']]},
             {'type': 'mc', 'title': '상황·심경·기능', 'guide': '장소, 관계, 심경, 의도, 빈칸, 어색한 대화까지 시험에 나오는 모양 그대로예요.', 'items': mc}]}
new = []
for L in LESSONS:
    M = importlib.import_module(L)
    for gid, c in M.DLG.items(): new.append(build(gid, c))
ids = {d['id'] for d in new}
old = [d['id'] for d in PK['days']]
PK['days'] = [d for d in PK['days'] if d['id'] not in ids]
for d in new:   # 이미 있던 DAY면 같은 자리에, 처음이면 맨 끝
    k = old.index(d['id']) if d['id'] in old else None
    if k is None or k > len(PK['days']): PK['days'].append(d)
    else: PK['days'].insert(k, d)
for i, d in enumerate(PK['days']): d['name'] = 'DAY %d' % (i + 1)
if '대화문 꿰뚫기' not in head: head = head.rstrip('\n') + '\n/* 11/27: 대화문 꿰뚫기 DAY (gen/m1dlg/gen.py, 과별 l5·l6·l7.py) 맨 끝 */\n'
write(PK, path, head); open(path, 'a', encoding='utf-8').write(tail)
print([(d['name'], d['range']) for d in PK['days'] if d['id'] in ids])
