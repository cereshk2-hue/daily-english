# 11/26 대진고2 10월 모고(2026 경기 고2 학평) 시험범위 20~24·29~42번 '어법·어휘 한 판' DAY 6개 (h2-ne-oh-L3 맨 끝: gm1~gm6, 3지문씩, 11/26부터 문장 하나씩 덩이 + 앞뒤 문장은 흐린 문맥)
# 선생님 자료: 이그잼포유 WORKBOOK 6 어법·어휘 고르기 hwp → work_src/djmock/oct_wb6.txt. 괄호·정답은 워크북 그대로(정답 줄 대조), 해설 ex.py 손글씨
# 고친 것: a(n) → 본문 관사, 41~42번 presenting → 본문 providing, 29번 첫 문장 앞 25~28번 실용문 떼기, 40번 요약문 문장 뺌
# 뺀 괄호(다른 쪽도 말이 됨): 24 assertion/assumption, 39 textual/visual, 40 frequency/duration
import sys, json, re, subprocess
sys.path.insert(0, '/home/claude/srcrepo/generators'); sys.path.insert(0, '/home/claude/srcrepo/gen/djmock')
from gencommon import write
from parse import parse
from ex import EX
path = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/proj/data/h2-ne-oh-L3.js'
PK = json.loads(subprocess.check_output(['node', '-e', "global.window={};require('%s');process.stdout.write(JSON.stringify(window.PKG))" % path]))
D = {d['id']: d for d in PK['days']}
Q = parse('/home/claude/srcrepo/work_src/djmock/oct_wb6.txt')
Q['29'][0][0] = Q['29'][0][0][Q['29'][0][0].index('You might think'):]
Q['40'] = Q['40'][:9]
FIX = [('20', 'a(n) {suitable', 'a {suitable'), ('32', 'In a(n) {democratic', 'In a {democratic'), ('34', 'a(n) {infinite', 'an {infinite'), ('37', 'a(n) {adverse', 'an {adverse'),
       ('41~42', '{presenting|presented}', '{providing|provided}')]
for k, a, b in FIX:
    hit = [p for p in Q[k] if a in p[0]]; assert len(hit) == 1, (k, a); hit[0][0] = hit[0][0].replace(a, b)
for k in Q:
    for p in Q[k]: p[0] = p[0].replace('wasn‘t', 'wasn’t').replace("|don't}", '|don’t}')   # 오답 쪽 따옴표 통일
DROP = [('24', 'assertion'), ('39', 'textual'), ('40', 'frequency')]
for k, w in DROP:
    hit = [p for p in Q[k] if '{%s|' % w in p[0]]; assert len(hit) == 1, (k, w); hit[0][0] = re.sub(r'\{%s\|[^}]*\}' % w, w, hit[0][0])
norm = lambda t: re.sub(r'\s*-\s*', '-', re.sub(r'\s+', ' ', t.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"').replace('—', '-').replace('–', '-'))).strip()
plain = lambda s: re.sub(r'\{([^|}]*)\|[^}]*\}', r'\1', s)
TOPIC = {'20': '정원사 같은 부모', '21': '이자와 시간 인식', '22': '창작자의 사회적 책임', '23': '문어의 팔 뉴런', '24': '아리스토텔레스의 한계', '29': '인류 생존의 허들',
         '30': '비언어 신호의 우위', '31': '자동화된 습관', '32': '대중문화와 법원', '33': '발달의 가소성', '34': '상호 연결과 복잡한 실패', '35': '감염병 치료의 진보',
         '36': '사용성 테스트', '37': '재평가와 회복 탄력성', '38': '물의 수질 기준', '39': '사회사가의 사료 읽기', '40': '돌고래의 반향정위 뇌', '41~42': '지루함의 가치'}
GROUPS = [['20', '21', '22'], ['23', '24', '29'], ['30', '31', '32'], ['33', '34', '35'], ['36', '37', '38'], ['39', '40', '41~42']]
days, tot, BAD = [], 0, []
for gi, G in enumerate(GROUPS, 1):
    items, nb = [], 0
    for k in G:
        S, E = Q[k], EX[k]; assert len(S) == len(E), (k, len(S), len(E))
        qid = 'q' + k.split('~')[0]; TX = norm(' '.join(l[1] for l in D[qid]['passage']))
        parts = []
        for (s, ko), ex in zip(S, E):
            assert norm(plain(s)) in TX, (k, plain(s))
            for m in re.findall(r'\{([^}]*)\}', s):
                a, b = m.split('|'); assert a != b, m
                if a.split()[-1].lower().replace('’', "'") not in ex.lower(): BAD.append((k, a, ex[:60]))
            parts.append({'s': s, 'ko': ko, 'ex': ex})
        c = sum(p['s'].count('{') for p in parts); nb += c
        for j, p in enumerate(parts):   # 11/26 선생님: 힘들어 보임 → 문장 하나씩 덩이(틀리면 그 문장만 다시)
            cx = lambda q: {'s': plain(q['s']), 'ko': q['ko'], 'ex': '', 'ctx': True}   # 앞뒤 문장은 문맥으로만(괄호 없음, 흐리게)
            ps = ([cx(parts[j - 1])] if j else []) + [p] + ([cx(parts[j + 1])] if j + 1 < len(parts) else [])
            items.append({'title': '%s번 %d/%d · %s (괄호 %d개)' % (k, j + 1, len(parts), TOPIC[k], p['s'].count('{')), 'parts': ps})
    nums = '·'.join(G)
    days.append({'id': 'gm%d' % gi, 'name': '', 'range': '모의고사 어법·어휘 한 판 · 10월 %s번' % nums,
                 'story': '모의고사 어법·어휘 한 판 · 10월 모고 %s번 · 괄호 %d개, 문장 하나씩 %d덩이 · 문장마다 모두 맞혀야 통과' % (nums, nb, len(items)),
                 'passage': sum((D['q' + k.split('~')[0]]['passage'] for k in G), []),
                 'steps': [{'type': 'gate', 'title': '모의고사 어법·어휘 한 판', 'guide': "지문 3개를 문장 하나씩 풀어요. 흐린 글씨는 앞뒤 문장(문맥)이에요. 어법 괄호와 어휘(문맥상 반대말·헷갈리는 낱말) 괄호가 섞여 있어요. 문장 속 괄호를 모두 맞히면 통과, 틀리면 그 문장만 다시! 3번 안에 통과 못 하면 해설을 보고 연습한 뒤 다시 도전해요.",
                            'items': items}]})
    tot += nb
assert not BAD, '\n'.join(map(str, BAD))
NEW = [d['id'] for d in days]
PK['days'] = [d for d in PK['days'] if d['id'] not in NEW] + days
for i, d in enumerate(PK['days']): d['name'] = 'DAY %d' % (i + 1)
src = open(path, encoding='utf-8').read(); head = src[:src.index('window.PKG')]
tail = src[src.index('/* WRAPUP-TESTS'):]
if '모고 어법·어휘' not in head: head = head.rstrip('\n') + '\n/* 11/26: 10월 모고 어법·어휘 한 판 DAY gm1~gm6 맨 끝 (gen/djmock/gen.py) */\n'
PK.pop('tests', None)
write(PK, path, head)
open(path, 'a', encoding='utf-8').write(tail)
print('괄호', tot, [(d['name'], d['range'], [it['title'] for it in d['steps'][0]['items']]) for d in days])
