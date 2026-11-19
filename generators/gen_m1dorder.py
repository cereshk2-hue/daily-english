# 11/19 중산중1 동아(윤정미) 5·6·7과 본문 '문장 순서' 따로 연습 DAY 3개 (맨 끝, 5 → 6 → 7)
# 선생님: 한 줄씩은 너무 잘다 → 2문장씩 한 조각, 본문을 3덩이로. 본문 DAY(5과 L5a·L5b, 6과 d1·d2, 7과 d3·d4)의 문장을 그대로 씀
# 제목 줄(Challenge 01 …, 'Ann Jones, a visitor' 같은 이름표)과 5과 용의자 표는 빼고 문장만. 5과는 증인별로 나눠 3덩이(❶+Ann / Carlos+Diego / Camila+❹) 단락(말하는 사람)마다 앞에서부터 2문장씩, 홀수면 그 단락 마지막 조각 1문장
# 11/19 'tries': 3 → 앱이 한 판처럼 3번 도전 → 오답 학습 → 처음부터 다시 3번
# 본문 탭도 조각 단위(영어 2문장 · 해석 2문장)로 넣어서 앱의 '① 우리말로 내용 흐름 먼저 → ② 영어 순서'가 그대로 동작
import sys, json, re, subprocess
sys.path.insert(0, '/home/claude/srcrepo/generators')
from gencommon import write
path = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/proj/data/m1-donga-yoon-L6.js'
PK = json.loads(subprocess.check_output(['node', '-e', "global.window={};require('%s');process.stdout.write(JSON.stringify(window.PKG))" % path]))
D = {d['id']: d for d in PK['days']}
MARK = re.compile(r'^[❶-❿]$')
HEAD = lambda x: '|' in x or not re.search(r'[.!?]["”’]?$', x.strip())   # 제목·이름표(문장부호로 안 끝남)·표 줄

def sections(keys):
    """본문 DAY들 → [(번호, [(영어, 해석)])]"""
    out = []
    for k in keys:
        for l in D[k]['passage']:
            if l[0] == '#': continue
            if MARK.match(l[1]): out.append((l[1], [])); continue
            if HEAD(l[1]):   # 이름표가 단락 중간에 나오면(5과 증인 둘째 사람) 거기서 작은 단락을 새로 엶: ❷ → ❷b
                if out and out[-1][1] and '|' not in l[1]: out.append((out[-1][0][0] + 'b', []))
                continue
            assert out, l
            out[-1][1].append((l[1], l[2]))
    return out

def pairs(sents):
    return [sents[i:i + 2] for i in range(0, len(sents), 2)]

def build(gid, rng, keys, groups):
    """groups: [[❶, ❷], …] 덩이마다 묶을 단락 번호"""
    sec = dict(sections(keys))
    allm = [m for m, _ in sections(keys)]
    assert sorted(sum(groups, [])) == sorted(allm), (groups, allm)
    items, passage, n = [], [], 0
    for gi, g in enumerate(groups):
        sents = sum((sec[m] for m in g), [])
        ps = sum((pairs(sec[m]) for m in g), [])   # 단락(사람)마다 따로 2문장씩 → 조각이 단락을 넘지 않음
        lines = [' '.join(e for e, k in p) for p in ps]
        assert len(lines) >= 3 and len(set(lines)) == len(lines), lines
        items.append({'lines': lines}); n += len(sents)
        passage.append(['#', '덩이 %d · 본문 %s' % (gi + 1, ''.join(dict.fromkeys(m[0] for m in g))), ''])
        passage += [['', ' '.join(e for e, k in p), ' '.join(k for e, k in p)] for p in ps]
    return {'id': gid, 'name': '', 'range': rng, 'story': rng + ' · 2문장씩 조각, 본문 3덩이 (문장 %d개)' % n,
            'passage': passage,
            'steps': [{'type': 'order', 'title': '문장 순서', 'tries': 3,
                       'guide': "본문을 3덩이로 나눴어요. 덩이마다 우리말 조각을 내용 흐름대로, 다음에 영어 조각을 본문 순서대로 놓아요(한 조각 = 2문장). 모두 맞혀야 100점, 하나라도 틀리면 0점! 3번 안에 통과 못 하면 오답 학습을 하고 다시 도전해요.",
                       'items': items}]}, n

o5, n5 = build('od5', '5과 본문 · 문장 순서', ('L5a', 'L5b'), [['❶', '❷'], ['❷b', '❸'], ['❸b', '❹']])
o6, n6 = build('od6', '6과 본문 · 문장 순서', ('d1', 'd2'), [['❶', '❷'], ['❸'], ['❹', '❺']])
o7, n7 = build('od7', '7과 본문 · 문장 순서', ('d3', 'd4'), [['❶', '❷'], ['❸', '❹'], ['❺', '❻']])
PK['days'] = [d for d in PK['days'] if d['id'] not in ('od5', 'od6', 'od7')] + [o5, o6, o7]
for i, d in enumerate(PK['days']): d['name'] = 'DAY %d' % (i + 1)
src = open(path, encoding='utf-8').read(); head = src[:src.index('window.PKG')]
tail = src[src.index('/* WRAPUP-TESTS'):] if '/* WRAPUP-TESTS' in src else ''
if '문장 순서' not in head: head = head.rstrip('\n') + '\n/* 11/19: 5·6·7과 본문 문장 순서(2문장 조각 · 3덩이) DAY od5·od6·od7 맨 끝 (generators/gen_m1dorder.py) */\n'
if tail: PK.pop('tests', None)
write(PK, path, head)
if tail: open(path, 'a', encoding='utf-8').write(tail)
for o in (o5, o6, o7):
    print(o['range'], [len(it['lines']) for it in o['steps'][0]['items']])
