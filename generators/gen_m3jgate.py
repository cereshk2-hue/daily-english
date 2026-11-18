# 11/18 중산중3 지학사(민찬규) 7·8과 '어법 선택 한 판' DAY 2개 (맨 끝, 7 → 8)
# 선생님 자료: 각 과 본문 7단계 워크북 Part 4 어법 선택형 연습 hwp (이그잼포유) → work_src/m3jgate/L7.txt·L8.txt (hwpread.py)
# 문장·괄호·정답은 txt에서 그대로 읽음([a / b] + 정답 줄 → {정답|오답}), 해설만 여기 EX에 씀. 덩이: 7과 = 워크북 본문 1 / 2 / 3, 8과 = 본문 1 / 2·3 / 4·5
# 채운 문장이 본문 DAY(7과 d1·d2, 8과 d3·d4) 본문에 그대로 있는지 확인. gen_m2dgate.py 구조 복사
import sys, json, re, subprocess
sys.path.insert(0, '/home/claude/srcrepo/generators')
from gencommon import write
path = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/proj/data/m3-jihak-min-L7.js'
SRC = '/home/claude/srcrepo/work_src/m3jgate/'
PK = json.loads(subprocess.check_output(['node', '-e', "global.window={};require('%s');process.stdout.write(JSON.stringify(window.PKG))" % path]))
HAN = re.compile('[가-힣]')

def parse(f):
    L = [l.rstrip() for l in open(SRC + f, encoding='utf-8')]
    L = L[:next(i for i, l in enumerate(L) if l.strip() == '정답')]
    out, ko, en, sec = [], [], [], 0
    for l in L:
        s = l.strip()
        m = re.match(r'^본문 (\d) - Part 4', s)
        if m: sec = int(m.group(1)); continue
        if not s or s.startswith('WORKBOOK') or re.match(r'^Lesson \d', s) or '어법 선택형 연습' in s or s.startswith('괄호 안에서') or re.match(r'^본문 \d$', s): continue
        if l.startswith(' ') and not HAN.search(s) and '[' not in s and en:  # 정답 줄
            ans = [a.strip() for a in s.split(' / ')]
            sent = ' '.join(en); assert len(re.findall(r'\[', sent)) == len(ans), (sent, ans)
            k = iter(ans)
            def rep(m):
                o = [x.strip() for x in m.group(1).split(' / ')]; a = next(k); assert len(o) == 2 and a in o, (o, a)
                return '{%s|%s}' % (a, o[1 - o.index(a)])
            sent = re.sub(r'\[([^\]]*)\]', rep, sent).replace('{to understand.|understanding}’', '{to understand|understanding}.’')
            out.append((sec, sent, ' '.join(ko))); ko, en = [], []
        elif HAN.search(s): ko.append(s)
        else: en.append(s)
    assert not en
    return out

EX7 = [
 "live in + 장소(~에 살다) → live in / 명사 houses를 꾸미는 말 → 형용사 different / '~하기 위해'(목적) → to enter",
 "주어 Others(복수) → live / 가리키는 것이 others(복수) → their",
 "명령문은 동사원형으로 시작 → Imagine / one of + 복수 명사 → houses",
 "가정법 과거(If + 과거, 주어 + would + 동사원형) → would / '~하기 위해'(목적) → to enter",
 "구멍이 '숨겨진' 수동 → 과거분사 hidden",
 "appear는 자동사라 수동태가 안 됨, 가정법 과거 → appeared / 주절 → would / '~하기 위해' → to stop / stop A from -ing → entering",
 "벽이 '만들어진' 수동 → be made of",
 "keep + 목적어(me) + 형용사 보어, cool과 나란히 → warm",
 "would + 동사원형 → sleep",
 "가정법 과거: 주절에 would → If절은 과거 lived / 118 + 복수 명사 → islands",
 "would + 동사원형(travel) → would (would have 뒤에는 과거분사)",
 "주어 the water(단수) → rises / rises와 and로 나란히 → leaves / leave + 목적어 + 형용사 보어(가득 찬) → full",
 "be able to + 동사원형 → to walk / 통로가 '높이 올려진' 수동 → raised",
 "베니스가 '알려진' 수동 → be known as",
 "there + be + 복수(many houses) → are / 명사 houses를 꾸미는 말 → 형용사 colorful",
 "간접의문문은 '의문사 + 주어 + 동사' 순서 → they built",
 "decide + to부정사 → to live / '~하기 위해'(목적) → to keep / 주어 The old Venetians 자신 → themselves / keep + 목적어 + 형용사 → safe",
 "be동사 보어 → 형용사 easy / easy 같은 일반 형용사의 의미상 주어 → for them / to + 동사원형 → build",
 "그들이 기둥을 '설치한' 능동 → installed",
 "these + 복수 명사 → poles / It is ~ that 강조 구문 → that / 강조된 주어 poles(복수) → support",
 "명사 house를 꾸미는 말 → 형용사 huge / 가정법 과거 주절 → would",
 "지각동사 hear + 목적어 + -ing(또는 동사원형) → calling",
 "there + be + 복수(three to five floors) → are / three to five + 복수 → floors / 1층이 '사용되는' 수동 → is used",
 "사람들이 '보관하는' 능동 → store",
 "간접의문문은 '의문사 + 주어 + 동사' 순서 → where I would / would + 동사원형, 보어 앞 → be / 층은 서수 → third",
 "be like + 명사(~와 같은) → like (alike는 명사 앞에 못 씀) / 사람들이 '사는' 능동 → 현재분사 living / 주어 The people(복수) → have",
 "50 + 복수 명사 → families",
 "주어 They, work와 나란히 → share / many + 복수 명사 → things",
 "주어 자리 → 동명사 Living / 동명사 주어는 단수 → keeps / keep + 목적어 + 형용사 → safe",
 "주어 Homes(복수) → are / be동사 보어 → 형용사 different",
]
EX8 = [
 "과거진행형 was + -ing → doing / was + -ing → struggling",
 "가주어 It — 진주어 to부정사 → to read / to read와 and로 나란히(to 생략) → draw / No one은 단수 → needs",
 "put down과 and로 나란히(과거) → picked",
 "decide + to부정사 → to read / read oneself to sleep(책을 읽다가 잠들다), to는 전치사 아닌 to부정사 → sleep",
 "be about to + 동사원형(막 ~하려고 하다) → to open",
 "'~하기 위해'(목적) → to see / 과거진행형 was + -ing → talking",
 "It is ~ who 강조 구문, 강조되는 것이 Manny(이름 있는 대상) → who / was + -ing → talking",
 "명령문은 동사원형으로 시작 → Close",
 "Pascal이 눈을 '감은' 능동 → closed",
 "지각동사 hear + 목적어 + -ing(또는 동사원형) → shouting",
 "과거진행형 were + -ing(쫓고 있었다) → chasing",
 "dangerous 같은 일반 형용사의 의미상 주어 → for you / 가주어 It — 진주어 to부정사 → to stand",
 "그 남자가 '끌어 올린' 능동 → pulled / pulled와 and로 나란히(과거) → rode",
 "arrive는 자동사라 수동태가 안 됨 → arrived / stopped와 and로 나란히(과거) → got",
 "명사 the Robin Hood가 보어 → be동사 의문문 Are",
 "직접의문문은 '의문사 + 동사 + 주어' → Who are you",
 "Robin이 Pascal을 '구해 준' 능동, 목적어 me가 있음 → saved",
 "help + 목적어 + 동사원형(또는 to부정사) → get / 선행사 the money가 있고 뒤가 불완전 → 관계대명사 that (what은 선행사 없이)",
 "too + 형용사 + to부정사(너무 ~해서 …할 수 없다) → to share / enough money to + 동사원형 → buy",
 "want + to부정사 → to help / help + 목적어 + 동사원형 → get / there + be + 복수(many soldiers) → are",
 "take + 사람 + to + 장소(~로 데려가다) → to the tower / need to + 동사원형 → count",
 "그들이 '숨은' 능동(hide-hid-hidden) → hid",
 "there + be + 복수(five soldiers) → are / eight + 복수 명사 → soldiers",
 "there + be + 복수(twelve soldiers) → are / twelve + 복수 명사 → soldiers",
 "조동사 should + 동사원형(능동) → go",
 "Pascal이 '생각한' 능동 → thought",
 "make + 목적어(this) + 형용사 보어 → easier / 형용사 뒤에서 '~하기에' → to understand",
 "show + 사물(it) + to + 사람 (목적어가 대명사 it이면 to 필요) → to Robin",
 "명사 time을 꾸미는 말 → 형용사 dangerous / 주어 the most dangerous time(단수) → is / more + 복수 명사 → soldiers / 주어 soldiers(복수) → work / 간접의문문 '의문사 + 주어 + 동사' → what I mean",
 "'정말 많이' → so much (어순 주의)",
 "say의 목적어, 뒤가 완전한 절 → 접속사 that / 가리키는 것이 graphs(복수) → them",
 "지각동사 see + 목적어 + -ing(또는 동사원형) → waving",
 "say to oneself(혼잣말하다) → to himself",
]
R7, R8 = parse('L7.txt'), parse('L8.txt')
assert len(R7) == len(EX7) and len(R8) == len(EX8), (len(R7), len(EX7), len(R8), len(EX8))

D = {d['id']: d for d in PK['days']}
norm = lambda s: re.sub(r'\s+', ' ', s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"').replace('—', '-').replace('–', '-').replace('…', '...')).lower()
def build(gid, rng, R, EX, keys, groups):
    """groups: [(제목, {워크북 본문 번호})]"""
    TX = norm(' '.join(l[1] for k in keys for l in D[k]['passage'] if not re.match(r'^[❶-❿]$', l[1]) and l[0] != '#'))
    items = []
    for title, secs in groups:
        parts = []
        for (sec, s, ko), ex in zip(R, EX):
            if sec not in secs: continue
            full = norm(re.sub(r'\{([^|}]*)\|[^}]*\}', r'\1', s)); assert full in TX, full
            for m in re.findall(r'\{([^}]*)\}', s): o = m.split('|'); assert len(o) == 2 and o[0] != o[1], s
            # 해설 속 정답 표시가 실제 정답과 맞는지 (괄호마다 정답 단어가 해설에 나오는지)
            for m in re.findall(r'\{([^|}]*)\|', s): assert m.split()[0].strip('.') in ex or m in ex, (m, ex)
            parts.append({'s': s, 'ko': ko, 'ex': ex})
        nb = sum(len(re.findall(r'\{', p['s'])) for p in parts)
        items.append({'title': '%s (괄호 %d개)' % (title, nb), 'parts': parts})
    assert sum(len(i['parts']) for i in items) == len(R)
    n = len(groups)
    return {'id': gid, 'name': '', 'range': rng, 'story': rng + ' · 괄호를 모두 맞혀야 100점 (덩이 %d개)' % n,
            'passage': sum((D[k]['passage'] for k in keys), []),
            'steps': [{'type': 'gate', 'title': '어법 선택 한 판', 'guide': "본문을 %d덩이로 나눴어요. 덩이마다 괄호를 모두 맞혀야 100점, 하나라도 틀리면 0점! 3번 안에 통과 못 하면 틀린 문장만 해설과 함께 연습하고 다시 도전해요." % n,
                       'items': items}]}, [i['title'] for i in items]
g7, n7 = build('gt7', '7과 본문 · 어법 선택 한 판', R7, EX7, ('d1', 'd2'),
               [('본문 ❶ · 들어가며 · 푸에블로', {1}), ('본문 ❷ · 베니스', {2}), ('본문 ❸ · 토루 · 맺음말', {3})])
g8, n8 = build('gt8', '8과 본문 · 어법 선택 한 판', R8, EX8, ('d3', 'd4'),
               [('Pascal과 Manny · 코기토 에르고 숨', {1}), ('로빈 후드와의 만남 · 부탁', {2, 3}), ('병사 수 세기 · 그래프', {4, 5})])
PK['days'] = [d for d in PK['days'] if d['id'] not in ('gt7', 'gt8')] + [g7, g8]
for i, d in enumerate(PK['days']): d['name'] = 'DAY %d' % (i + 1)
src = open(path, encoding='utf-8').read(); head = src[:src.index('window.PKG')]
tail = src[src.index('/* WRAPUP-TESTS'):] if '/* WRAPUP-TESTS' in src else ''
if '한 판' not in head: head = head.rstrip('\n') + '\n/* 11/18: 7·8과 본문 어법 선택 한 판 DAY gt7·gt8 맨 끝 (generators/gen_m3jgate.py) */\n'
if tail: PK.pop('tests', None)
write(PK, path, head)
if tail: open(path, 'a', encoding='utf-8').write(tail)
print(n7, n8, '·', [d['name'] + ' ' + d['range'] for d in PK['days']][-2:])
