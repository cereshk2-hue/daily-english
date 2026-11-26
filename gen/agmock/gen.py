# 11/26 안곡고1 모고 '어법·어휘 한 판' (h1-donga-lee-L3 맨 끝): 9월 30·33~42번(gs30~gs41) + 10월 21~24·29~32번(go21~go32) = 18 DAY, 지문 하나 = DAY 하나 = 덩이 하나
# 선생님 자료: 이그잼포유 WORKBOOK 6 어법·어휘 고르기 hwp(9월 60e73768 · 10월 40720b60) → work_src/agmock/*.txt. 괄호·정답은 워크북 그대로(정답 줄 대조), 해설 ex.py 손글씨
# 고친 것: 10월 29번 첫 문장 앞 실용문 뗌, 10월 31번 is not → 본문 isn't, 9월 40번 요약문 문장 뺌, 비분리 하이픈(‑) 그대로 대조
# 뺀 괄호(다른 쪽도 말이 됨): 9월 34 Wherever/Where, 9월 33 that/those(of Zeuxis), 10월 22 usually/rarely · end/beginning, 10월 30 consumption/production
import sys, json, re, subprocess
sys.path.insert(0, '/home/claude/srcrepo/generators'); sys.path.insert(0, '/home/claude/srcrepo/gen/djmock'); sys.path.insert(0, '/home/claude/srcrepo/gen/agmock')
from gencommon import write
from parse import parse
from ex import EX9, EX10
path = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/proj/data/h1-donga-lee-L3.js'
PK = json.loads(subprocess.check_output(['node', '-e', "global.window={};require('%s');process.stdout.write(JSON.stringify(window.PKG))" % path]))
D = {d['id']: d for d in PK['days']}
SRC = '/home/claude/srcrepo/work_src/agmock/'
Q9 = parse(SRC + '60e73768.txt'); Q10 = parse(SRC + '40720b60.txt')
Q9['40'] = Q9['40'][:9]
Q10['29'][0][0] = Q10['29'][0][0][Q10['29'][0][0].index('Since hydra'):]
def fix(Q, k, a, b):
    hit = [p for p in Q[k] if a in p[0]]; assert len(hit) == 1, (k, a); hit[0][0] = hit[0][0].replace(a, b)
fix(Q10, '31', '{is|are} not usually', '{isn’t|aren’t} usually')
fix(Q9, '34', '{Wherever|Where}', 'Wherever')
fix(Q9, '33', 'such as {that|those} of', 'such as that of')
fix(Q10, '22', '{usually|rarely}', 'usually'); fix(Q10, '22', '{end|beginning}', 'end')
fix(Q10, '30', '{consumption|production}', 'consumption')
norm = lambda t: re.sub(r'\s*-\s*', '-', re.sub(r'\s+', ' ', t.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"').replace('—', '-').replace('–', '-').replace('‑', '-'))).strip()
plain = lambda s: re.sub(r'\{([^|}]*)\|[^}]*\}', r'\1', s)
T9 = {'30': '문단은 짧게', '33': '모방으로서의 예술', '34': '몸이 아는 달리기', '35': '반려견 목욕', '36': '수학은 패턴', '37': '코페르니쿠스와 망원경',
      '38': '측정 단위의 일관성', '39': '농사짓는 잎꾼개미', '40': '관계 감시 장치 자존감', '41~42': '인터넷과 속어'}
T10 = {'21': '같은 게임, 같은 상품', '22': '사회가 만든 시간', '23': '내부 고발자 보호', '24': '목표에 대한 환상', '29': '불멸의 해파리',
       '30': '보조금의 왜곡', '31': '스타트렉과 풍요', '32': '경청받는 느낌'}
days, tot, BAD = [], 0, []
for mon, pre, gid, Q, EX, T in (('9월', 'q', 'gs', Q9, EX9, T9), ('10월', 'o', 'go', Q10, EX10, T10)):
    for k in T:
        S, E = Q[k], EX[k]; assert len(S) == len(E), (mon, k, len(S), len(E))
        src = D[pre + k.split('~')[0]]; TX = norm(' '.join(l[1] for l in src['passage']))
        parts = []
        for (s, ko), ex in zip(S, E):
            assert norm(plain(s)) in TX, (mon, k, plain(s))
            for m in re.findall(r'\{([^}]*)\}', s):
                a, b = m.split('|'); assert a != b, m
                if a.split()[-1].lower().replace('’', "'") not in ex.lower().replace('’', "'"): BAD.append((mon, k, a, ex[:50]))
            parts.append({'s': s, 'ko': ko, 'ex': ex})
        nb = sum(p['s'].count('{') for p in parts); tot += nb
        days.append({'id': gid + k.split('~')[0], 'name': '', 'range': '모의고사 어법·어휘 한 판 · %s %s번' % (mon, k),
                     'story': '모의고사 어법·어휘 한 판 · %s 모고 %s번 · %s · 괄호 %d개 · 지문 전체를 한 번에 모두 맞혀야 100점' % (mon, k, T[k], nb),
                     'passage': src['passage'],
                     'steps': [{'type': 'gate', 'title': '모의고사 어법·어휘 한 판', 'guide': "지문 하나를 한 판으로 완성해요. 어법 괄호와 어휘(문맥상 반대말·헷갈리는 낱말) 괄호가 섞여 있어요. 괄호를 모두 맞혀야 100점, 하나라도 틀리면 0점! 3번 안에 통과 못 하면 틀린 문장만 해설과 함께 연습하고 다시 도전해요.",
                                'items': [{'title': '%s %s번 · %s (괄호 %d개)' % (mon, k, T[k], nb), 'parts': parts}]}]})
assert not BAD, '\n'.join(map(str, BAD))
NEW = [d['id'] for d in days]
PK['days'] = [d for d in PK['days'] if d['id'] not in NEW] + days
for i, d in enumerate(PK['days']): d['name'] = 'DAY %d' % (i + 1)
src = open(path, encoding='utf-8').read(); head = src[:src.index('window.PKG')]
tail = src[src.index('/* WRAPUP-TESTS'):] if '/* WRAPUP-TESTS' in src else ''
assert tail or 'tests' not in PK, 'tests 블록 확인'
if '모고 어법·어휘' not in head: head = head.rstrip('\n') + '\n/* 11/26: 9월·10월 모고 어법·어휘 한 판 DAY gs30~gs41 · go21~go32 맨 끝 (gen/agmock/gen.py) */\n'
PK.pop('tests', None)
write(PK, path, head)
if tail: open(path, 'a', encoding='utf-8').write(tail)
print('괄호', tot, [(d['name'], d['range'], d['steps'][0]['items'][0]['title']) for d in days])
