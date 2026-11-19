# 11/19 저동고1 공통영어2 능률(민병천) 3·4과 '어법 선택 한 판' DAY 2개 (맨 끝, 3 → 4)
# 선생님 자료: 각 과 본문 10단계 워크북 6 어법 선택형 연습 hwp (이그잼포유) → work_src/h1ngate/L3.txt·L4.txt (hwpread.py)
# 문장·괄호·정답은 txt에서 그대로 읽음([a / b] + 정답 줄 → {정답|오답}), 해설만 여기 EX에 씀. 덩이는 본문 DAY와 같게 ❶❷ / ❸ / ❹❺
# 채운 문장이 본문 DAY(3과 d1~d3, 4과 l4a~l4c)에 그대로 있는지, 어느 ❶~❺에 있는지 본문에서 찾아 덩이를 나눔. gen_m3jgate.py 구조 복사
import sys, json, re, subprocess
sys.path.insert(0, '/home/claude/srcrepo/generators')
from gencommon import write
path = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/proj/data/h1-ne-min-L3.js'
SRC = '/home/claude/srcrepo/work_src/h1ngate/'
PK = json.loads(subprocess.check_output(['node', '-e', "global.window={};require('%s');process.stdout.write(JSON.stringify(window.PKG))" % path]))
HAN = re.compile('[가-힣]')
HEADS = {'Dealing with Plastic Waste', 'Purifying Polluted Soil', 'Producing Algae Biofuel'}

def parse(f):
    L = [l.rstrip() for l in open(SRC + f, encoding='utf-8')]
    L = L[:next(i for i, l in enumerate(L) if l.strip() == '본문 10단계 워크북')]
    out, ko, en = [], [], []
    skip = lambda s: (not s or s in ('Lesson', '공통영어2', '교과서 본문', '│본문│', '워크북 6') or re.match(r'^\d+$', s) or '어법 선택형 연습' in s
                      or s.startswith('2022 개정') or s.startswith('NE능률') or s.startswith('◗'))
    for l in L:
        s = l.strip()
        if skip(s) or s in HEADS: continue
        if HAN.search(s) and re.search(r'하기$', s): continue  # 4과 소제목(한글)
        if l.startswith(' ') and not HAN.search(s) and '[' not in s and en:  # 정답 줄
            ans = [a.strip() for a in s.split(' / ')]
            sent = ' '.join(en); assert len(re.findall(r'\[', sent)) == len(ans), (sent, ans)
            k = iter(ans)
            def rep(m):
                o = [x.strip() for x in m.group(1).split(' / ')]; a = next(k); assert len(o) == 2 and a in o, (o, a)
                return '{%s|%s}' % (a, o[1 - o.index(a)])
            out.append((re.sub(r'\[([^\]]*)\]', rep, sent), ' '.join(ko))); ko, en = [], []
        elif HAN.search(s): ko.append(s)
        else: en.append(s)
    assert not en
    return out

EX3 = [
 "주어 Children 뒤 동사 자리, 2020년의 일(과거) → learned",
 "선행사 a girl(사람) → 관계대명사 who (what은 선행사 없이) / 주격 관계대명사 뒤 동사는 선행사(단수)에 맞춤 → meets",
 "할머니가 호랑이를 '아는' 능동, 뒤에 목적어 the tiger → knows",
 "소녀가 거래를 '하는' 능동, 뒤에 목적어 a deal → makes",
 "주어 inspiration(단수) → was / 선행사 an old folktale, 뒤가 불완전(tell의 목적어 없음) → that / used to + 동사원형(~하곤 했다) → tell",
 "그것이 '해님 달님'이라고 '불리는' 수동 → is called",
 "want + to부정사 → to revive / 전치사 by + 동명사 → writing",
 "주어 the tiger(단수) → is",
 "so + 형용사 + that(너무 ~해서 …하다) → that",
 "가주어 It ~ 진주어 that절(뒤가 완전) → that",
 "주어 The first appearance(단수, of ~ culture는 수식어) → dates (date back to: ~로 거슬러 올라가다)",
 "그림이 사람들을 '묘사하는' 능동, 뒤에 목적어 people → depicts / 사람들이 동물을 '사냥하는' 능동 → 현재분사 hunting",
 "appear는 자동사라 수동태가 안 됨 → have appeared",
 "조동사 may have + 과거분사 → heard / 설화가 호랑이를 '등장시키는' 능동, 뒤에 목적어 tigers → 현재분사 featuring",
 "percent of + 복수 명사(folktales) → 동사도 복수 include",
 "주어 Tigers(복수) → are / 호랑이가 '보여지는' 수동 → are shown",
 "help + 목적어 + 동사원형(또는 to부정사) → become",
 "지각동사 hear + 목적어 + 동사원형(또는 -ing) → tell / Here is + 단수(a gotgam) → Here’s",
 "뒤에 주어 + 동사(절) → 접속사 Because (Because of + 명사) / 주어 the tiger, thinks와 and로 나란히 → runs",
 "It seems that + 완전한 절(~인 것 같다) → that",
 "have가 '가지다'일 때는 수동태가 안 됨, 뒤에 목적어 respect → had",
 "사람이 '상처를 입는' 수동 동명사 → being injured / injured와 or로 나란히 '죽임을 당하는' → killed / 동명사 주어는 단수 → was",
 "조동사 may have + 과거분사 → made / in order + to부정사(~하기 위해) → to be",
 "face(~에 직면하다)는 뒤에 목적어 a decline → 능동 faced",
 "With ~ 부사구 뒤 문장의 동사 자리, 주어 their use → faded (fading은 동사가 못 됨)",
 "상징성이 '되살려진' 수동 → was revived / 올림픽이 한국에 의해 '개최된' → 과거분사 hosted (by Korea)",
 "주어 Hodori 뒤 동사 자리 → was (to be는 동사가 못 됨)",
 "콤마 뒤 계속적 용법 → which (that ✘) / 선행사 a Siberian tiger(단수) → represents",
 "주어 The PyeongChang Winter Olympics 뒤 동사 자리 → created",
 "백호가 신성한 수호자로 '여겨지는' 수동 → are considered",
 "호랑이가 '언급되는' 수동 → are mentioned",
 "주어 One verse(단수, of the song은 수식어) → is / 콤마 뒤 계속적 용법, 선행사 \"Sugungga\" → which (what ✘) / 선행사 단수 → is",
 "영상이 '시청되는' 수동 → was viewed",
 "셀 수 있는 복수 명사 tigers → a few / 호랑이가 '보고된' 수동 → have been reported / to be + -ing(살고 있는) → living",
 "주어 the history, stories, and cultural meaning(and로 묶인 복수) → have",
 "deny의 목적어, 뒤가 완전한 절 → 접속사 that",
 "뒤에 동사가 바로 옴(주격 관계대명사) → that (whose 뒤에는 명사) / 선행사 a book(단수) → collects",
 "How about + 동명사(~하는 게 어때?) → looking",
]
EX4 = [
 "주어 Our environment 뒤 동사 자리 → is",
 "with + 명사 + 분사(~하면서), 지구가 '되는' 능동 → becoming / 현재진행 are + -ing → rising / 주어 natural disasters(복수) → are",
 "쓰레기가 '생산되고 있는' 진행형 수동(is being + 과거분사) → being produced",
 "주어 Plastic(단수, 콤마 사이는 삽입) → is / 진행형 is + -ing, 뒤에 목적어 problems → causing",
 "가주어 It ~ 진주어 that절(뒤가 완전) → that",
 "be able to + 동사원형 → protect",
 "stop A from -ing(A가 ~하지 못하게 하다) → reaching",
 "주어 자리 → 동명사 Achieving / seem + 형용사 보어 → difficult",
 "자연이 우리에게 해결책을 '제공한' 능동(provide A with B) → may have provided",
 "Here + be + 주어 three areas(복수) → are / 뒤가 완전한 문장, 장소 선행사 → 관계부사 where",
 "플라스틱이 '생산되는' 수동 → is produced",
 "물건이 '사용되는' 수동 → are used / used와 and로 나란히 '버려지는' → discarded",
 "간접의문문 '의문사 + 주어 + 동사' → where these plastic items go / 동사 + 부사의 목적어가 대명사면 가운데 → throw them away",
 "help + (to) 동사원형 → reduce",
 "less than ten percent of + 불가산 명사(waste) → 단수 has / 쓰레기가 '재활용된' 수동 → has been recycled",
 "쓰레기가 '옮겨지는' 수동 → is moved / 쓰레기가 '버려지는' 수동(is + 과거분사) → dumped / dumped와 or로 나란히 → burned",
 "주어 between 8 and 14 million metric tons(복수) 뒤 동사 → end (end up: 결국 ~에 이르다)",
 "이것이 해양 종을 위험에 '빠뜨리는' 능동, 뒤에 목적어 many marine species → puts",
 "진행형 are + -ing (turn to: ~에 의지하다) → turning",
 "주어 Mealworms 뒤 동사 자리 → are (being은 동사가 못 됨)",
 "live는 자동사라 수동태가 안 됨 → live",
 "박테리아가 플라스틱을 '분해하는' 능동, 뒤에 목적어 plastic → break",
 "mean의 목적어, 뒤가 완전한 절 → 접속사 that",
 "명사 ways를 꾸미는 to부정사(to + 동사원형) → cultivate",
 "want + to부정사 → to speed / 뒤가 완전한 문장(the bacteria break down plastic) → 전치사 + 관계대명사 by which",
 "help + 목적어 + (to) 동사원형 → keep",
 "진행형 are + -ing, 뒤에 목적어 soil pollution → causing",
 "흙이 '파내지는' 수동(dig-dug-dug) → can be dug",
 "그것이 문제를 '옮기는' 능동, 뒤에 목적어 the problem → only moves / 주어 it(단수), moves와 and로 나란히 → does",
 "there + be + 단수(an ~ way) → is / 명사 way를 꾸미는 to부정사 → to restore",
 "나무가 (사람을) '놀라게 하는' → 현재분사 amazing",
 "나무가 물질을 '추출하는' 능동, 뒤에 목적어 a wide range of harmful materials → naturally extract",
 "조동사 can + 동사원형 → grow",
 "전치사 of + 동명사(뒤에 목적어 willow trees) → using / 주어 Research(단수, on ~ purpose는 수식어) → is",
 "found의 목적어, 뒤가 완전한 절 → 접속사 that / 주어 some species(복수) → are",
 "분야가 '탐구되는' 수동 → should be further explored / '~하기 위해' to + 동사원형 → find / 간접의문문 '의문사 + 주어 + 동사' → which trees are",
 "be able to + 동사원형 → clean",
 "show의 목적어, 뒤가 완전한 절 → 접속사 that / percent of + 복수 명사(people) → drink",
 "주어 The coffee-making process(단수) → generates / 콤마 뒤 계속적 용법 → which (that ✘) / 선행사 coffee grounds(복수) → are / 찌꺼기가 '보내지는' 수동 → sent",
 "그것들이 온실가스를 '만드는' 능동, 뒤에 목적어 a harmful greenhouse gas → create",
 "there + be + 단수(no way) → there’s / 명사 way를 꾸미는 to부정사 → to stop / stop A from -ing → drinking",
 "전치사 by + 동명사 → turning",
 "선행사 a natural fuel, 뒤가 불완전 → 관계대명사 that (what은 선행사 없이) / 선행사 단수 → is / 연료가 '만들어지는' 수동 → made",
 "found의 목적어, 뒤가 완전한 절 → 접속사 that / 전치사 without + 동명사 → adding / 명사 nutrients 앞 형용사 → other (others는 대명사)",
 "조류가 빛에 '노출되는' 수동(be exposed to) → are exposed",
 "바이오 연료가 배출물을 '만드는' 능동, 뒤에 목적어 only a small amount of emissions → creates",
 "셀 수 있는 복수 명사 solutions → a few",
 "the problems (that) we face: 우리가 문제에 '직면하는' 능동, face의 목적어가 앞의 선행사 → currently face",
 "It seems that + 완전한 절(~인 것 같다) → that",
 "need + to부정사 → to look / keep + 목적어 + 형용사 보어 → healthy / healthy와 and로 나란히 → clean",
 "앞 문장의 일반동사(look for more ways ~)를 대신하는 대동사 → do",
]
R3, R4 = parse('L3.txt'), parse('L4.txt')
assert len(R3) == len(EX3) and len(R4) == len(EX4), (len(R3), len(EX3), len(R4), len(EX4))

D = {d['id']: d for d in PK['days']}
norm = lambda s: re.sub(r'\s+', ' ', s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"').replace('—', '-').replace('–', '-').replace('…', '...')).lower()
def secmap(keys):
    """본문 ❶~❺ 표시로 구간별 글 → {번호: 정규화한 글}"""
    S, cur = {}, 0
    for k in keys:
        for l in D[k]['passage']:
            m = re.match(r'^([❶-❿])$', l[1])
            if m: cur = ord(m.group(1)) - ord('❶') + 1; continue
            S[cur] = S.get(cur, '') + ' ' + l[1]
    return {k: norm(v) for k, v in S.items()}
def build(gid, rng, R, EX, keys, groups):
    SM = secmap(keys); items = []
    tagged = []
    for (s, ko), ex in zip(R, EX):
        full = norm(re.sub(r'\{([^|}]*)\|[^}]*\}', r'\1', s))
        sec = [k for k, v in SM.items() if full in v]; assert len(sec) == 1, (full, sec)
        for m in re.findall(r'\{([^}]*)\}', s): o = m.split('|'); assert len(o) == 2 and o[0] != o[1], s
        for m in re.findall(r'\{([^|}]*)\|', s): assert m.split()[0].strip('.') in ex or m in ex, (m, ex)
        tagged.append((sec[0], {'s': s.replace('’', "'").replace('“', '"').replace('”', '"'), 'ko': ko, 'ex': ex.replace('’', "'")}))
    secs_seen = [t[0] for t in tagged]; assert secs_seen == sorted(secs_seen), secs_seen  # 본문 순서대로
    for title, secs in groups:
        parts = [p for sec, p in tagged if sec in secs]
        nb = sum(len(re.findall(r'\{', p['s'])) for p in parts)
        items.append({'title': '%s (괄호 %d개)' % (title, nb), 'parts': parts})
    assert sum(len(i['parts']) for i in items) == len(R)
    n = len(groups)
    return {'id': gid, 'name': '', 'range': rng, 'story': rng + ' · 괄호를 모두 맞혀야 100점 (덩이 %d개)' % n,
            'passage': sum((D[k]['passage'] for k in keys), []),
            'steps': [{'type': 'gate', 'title': '어법 선택 한 판', 'guide': "본문을 %d덩이로 나눴어요. 덩이마다 괄호를 모두 맞혀야 100점, 하나라도 틀리면 0점! 3번 안에 통과 못 하면 틀린 문장만 해설과 함께 연습하고 다시 도전해요." % n,
                       'items': items}]}, [i['title'] for i in items]
g3, n3 = build('gt3', '3과 본문 · 어법 선택 한 판', R3, EX3, ('d1', 'd2', 'd3'),
               [('본문 ❶❷ · 해님 달님 · 호랑이와 한국 문화', {1, 2}), ('본문 ❸ · 곶감 이야기 · 올림픽 마스코트', {3}), ('본문 ❹❺ · 범 내려온다 · 오늘날', {4, 5})])
g4, n4 = build('gt4', '4과 본문 · 어법 선택 한 판', R4, EX4, ('l4a', 'l4b', 'l4c'),
               [('본문 ❶❷ · 들어가며 · 플라스틱 쓰레기', {1, 2}), ('본문 ❸ · 오염된 토양 정화', {3}), ('본문 ❹❺ · 조류 바이오 연료 · 맺음말', {4, 5})])
PK['days'] = [d for d in PK['days'] if d['id'] not in ('gt3', 'gt4')] + [g3, g4]
for i, d in enumerate(PK['days']): d['name'] = 'DAY %d' % (i + 1)
src = open(path, encoding='utf-8').read(); head = src[:src.index('window.PKG')]
tail = src[src.index('/* WRAPUP-TESTS'):] if '/* WRAPUP-TESTS' in src else ''
if '한 판' not in head: head = head.rstrip('\n') + '\n/* 11/19: 3·4과 본문 어법 선택 한 판 DAY gt3·gt4 맨 끝 (generators/gen_h1ngate.py) */\n'
if tail: PK.pop('tests', None)
write(PK, path, head)
if tail: open(path, 'a', encoding='utf-8').write(tail)
print(n3, n4, '·', [d['name'] + ' ' + d['range'] for d in PK['days']][-2:])
