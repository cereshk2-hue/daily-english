# 11/26 대진고2 영어II 능률(오선영) 3·4과 본문 '어법·어휘 한 판' DAY 2개 (h2-ne-oh-L3 맨 끝: gt3 · gt4)
# 선생님 자료: 본문 10단계 워크북 6 어법 선택형 연습 hwp(이그잼포유) → work_src/djgate/L3.txt·L4.txt. 어법 괄호는 워크북 그대로(정답 줄 대조)
# 어휘 괄호는 여기 VOC로 더함(문맥상 분명히 반대인 낱말만). 덩이 = 본문 DAY와 같게(3과 ❶❷❸ / ❹❺ / ❻❼, 4과 ❶❷ / ❸ / ❹❺ / ❻❼)
import sys, json, re, subprocess
sys.path.insert(0, '/home/claude/srcrepo/generators'); sys.path.insert(0, '/tmp')
from gencommon import write

HAN = re.compile('[가-힣]')
def parse(f):
    L = [l.rstrip() for l in open(f, encoding='utf-8')]
    L = L[:next(i for i, l in enumerate(L) if l.strip() == '본문 10단계 워크북')]
    out, ko, en = [], [], []
    skip = lambda s: (not s or s in ('Lesson', '영어II', '교과서 본문', '│본문│', '워크북 6') or re.match(r'^\d+$', s) or '어법 선택형 연습' in s
                      or s.startswith('2022 개정') or s.startswith('NE능률') or s.startswith('◗'))
    for l in L:
        s = l.strip()
        if skip(s): continue
        if l.startswith(' ') and not HAN.search(s) and '[' not in s and en:
            ans = [a.strip() for a in s.split(' / ')]
            sent = ' '.join(en); assert len(re.findall(r'\[', sent)) == len(ans), (sent, ans)
            k = iter(ans)
            def rep(m):
                o = [x.strip() for x in m.group(1).split(' / ')]; a = next(k); assert len(o) == 2 and a in o, (o, a)
                return '{%s|%s}' % (a, o[1 - o.index(a)])
            out.append([re.sub(r'\[([^\]]*)\]', rep, sent), ' '.join(ko)]); ko, en = [], []
        elif HAN.search(s): ko.append(s)
        else: en.append(s)
    assert not en, en
    return out
path = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/proj/data/h2-ne-oh-L3.js'
SRC = '/home/claude/srcrepo/work_src/djgate/'
PK = json.loads(subprocess.check_output(['node', '-e', "global.window={};require('%s');process.stdout.write(JSON.stringify(window.PKG))" % path]))
HEADS = ['The First-Past-The-Post Method', 'The Alternative Vote Method', 'The Condorcet Method',
         'Right-to-Repair Movement: Empowering Consumers', 'Repairability Index: Information at a Glance', 'Repair Cafés: It Takes a Community']
EX3 = [
 "from A to B 구조 속 '의문사 + to부정사'(누구와 점심을 먹을지, 어떤 직업을 추구할지) → to have / to pursue",
 "there + be + 복수 주어 many situations → are / 선행사 situations 뒤가 완전한 절(we must make decisions) → 관계부사 where",
 "집단 의사 결정이 목소리를 '수반하는' 능동, 뒤에 목적어 → involves / '서로 다른' 의견 → 현재분사 differing",
 "투표가 '사용되는' 수동 → used / '만들기 위해'(목적) → to make / make + 목적어 + 형용사 보어(fairer and more efficient) → efficient",
 "간접의문문 → 의문사 + 주어 + 동사: how these different voting methods work",
 "need + to부정사 → to decide / 의문사 + to부정사(어떻게 모금할지) → to raise",
 "there + be + 복수 주어 conflicting opinions → were / decide + to부정사 → to put",
 "encourage + 목적어 + to부정사, not A but B로 나란히 → to use / to try / -thing은 형용사가 뒤에서 꾸밈 → something different",
 "전치사 After + 능동 동명사(조사를 '한') → doing / decide + to부정사 → to try",
 "be curious + to부정사(~하고 싶어 하다) → to find",
 "행사가 글자를 '부여받은' 수동 → given / 글자 A로 '나타내진' 수동(by the letter A) → represented",
 "Each of + 복수 명사 → 단수 동사 was / instruct + 목적어 + to부정사의 수동(be instructed to) → to write",
 "분사구문, 빵 바자회와 미술 전시회가 '뒤따르는' → (being) followed by",
 "투표용지가 '집계된' 수동 → were counted",
 "투표자가 선택지를 '받는' 수동 → are given / whichever ~가 주어(단수 취급) → wins",
 "Neither A nor B 짝 → nor / 선호가 '무시되는' 수동 → are ignored / 방법이 '사용되는' 수동 → is used",
 "determine의 목적어, 뒤가 완전한 절 → 접속사 that",
 "형용사 easy 뒤 to부정사(~하기 쉬운) → to understand",
 "보어 자리 to부정사(콘서트를 여는 것) → to hold / 콤마 뒤 계속적 용법(앞 내용을 받음) → which (that ✘)",
 "분사구문, 자치회 구성원이 AV 방식을 '사용하는' 능동 → using / realize의 목적어, 뒤가 완전 → that",
 "for + 의미상 주어 + to부정사(선택지가 이기려면) → to win / need + to부정사 → to get",
 "두 번째 집계가 '요구되는' 수동 → was required / 셀 수 있는 복수 votes → fewest / with + 명사 + 분사, 구성원이 '투표하는' 능동 → voting",
 "선택지 A가 '탈락된' 수동 → eliminated / 표가 '재분배된' 수동 → redistributed",
 "주어 4 votes ~ and 1 (vote)(복수) → were / 표가 '더해진' 수동 → added",
 "allow + 목적어 + to부정사 → to have / 선택지가 표를 '받은' 능동(it received) → received (receive는 능동, 앞의 that 생략된 목적격 관계절)",
 "분사구문, 자치회가 방식을 '사용하는' 능동 → using / involve + 동명사 → comparing",
 "명사 three pairs를 꾸미는 to부정사(고려할 세 쌍) → to consider / discover의 목적어, 뒤가 완전 → that",
 "분사구문, 사람들이 '투표하면서' 능동 → voting / 전치사 by + 능동 동명사 → voting",
 "주어 option A(단수) → was / A가 '선호되는' 수동(be preferred to) → preferred / '여겨질' 수동 → considered",
 "보어 자리, 뒤가 완전한 절 → 접속사 that / fail + to부정사 → to select",
 "뒤에 동사가 바로 옴(주격 관계대명사) → that (whose 뒤에는 명사) / 선행사 elections(복수) → contain / 가주어 It ~ 진주어 that절(뒤가 완전) → that",
 "전치사 Instead of + 의미상 주어 + 동명사, pointing과 and로 나란히 → making / make + 목적어 + 형용사 보어 → easier",
 "decide + to부정사 → to choose / 의원들이 '직접 비교하는' 능동 동명사 → directly comparing",
 "agree의 목적어, 뒤가 완전 → that / 가주어 It ~ 진주어 that절 → that / 동명사 주어 choosing ~은 단수 → is",
 "'어떤 것이든(무엇을 선택하든 그것)' 명사절 주어 → Whichever / believe의 목적어, 뒤가 완전 → that / 전치사 by + 능동 동명사의 부정(not + -ing) → not ranking",
 "분사구문, 그들이 '주장하면서' 능동 → arguing / argue의 목적어, 뒤가 완전 → that",
 "노력이 '고안된' 수동 → are designed / not A but B로 나란히 to부정사(목적) → to make / to help / make + 목적어 + 형용사 보어 → difficult / inefficient / help + 목적어 + 동사원형 → make",
 "understanding과 and로 나란히 동명사 → weighing / 동명사 주어는 단수 → allows / allow + 목적어 + to부정사 → to better understand",
 "be likely + to부정사(~할 가능성이 높다) → to become",
]
EX4 = [
 "분사구문, Liz가 노트북을 '손상시킨' 능동(뒤에 목적어 it) → damaging / 뒤에 주어 + 동사(절) → 접속사 Although (Despite + 명사)",
 "have + 목적어 + 과거분사(노트북이 '수리되는') → repaired / hesitate + to부정사 → to do",
 "주어 자리 동명사 → getting, and로 나란히 → purchasing",
 "명사 the best thing을 꾸미는 to부정사 → to do / 미래진행 will be + -ing(기여하게 될 것) → contributing",
 "유독 물질이 제품에 '포함된' 수동 → contained / 주어 the amount(단수) → is",
 "e-waste가 '발생된' 수동 → generated / 콤마 뒤 계속적 용법(앞 내용) → which (that ✘) / which가 받는 앞 문장(단수) → was / 선행사 the year(시간), 뒤가 완전 → 관계부사 when / predict의 목적어, 뒤가 완전 → that",
 "노력이 '이루어지고 있는' 진행형 수동 → being made / '해결하기 위해' → to address / 접속사 없이 두 절을 이음 → 관계대명사 which(most of which) / 노력이 '집중되는' 수동 → focused / 전치사 on + 능동 동명사 → making / make + 목적어 + 형용사 보어 → easier / easy + to부정사 → to repair",
 "주어 One reason(단수) → is / 보어 자리, 뒤가 완전 → that / difficult + to부정사 → to repair",
 "difficult + to부정사 → to disassemble / require의 목적어, 뒤가 완전 → that / 요구·주장의 that절 → (should) 동사원형 be / 기기가 '고쳐지는' 수동 → be fixed",
 "allow + 목적어 + to부정사 → to take / 제품이 '설계되는' 수동 → designed / difficult + to부정사 → to repair",
 "가주어 It ~ for + 의미상 주어 + to부정사 → to be / 의문사 + to부정사 → to fix / 부품이 '필요한(필요로 되는)' 수동 → needed / '완료하기 위해' → to complete",
 "전치사 by + 능동 동명사(운동이 법을 '홍보하는') → promoting / 선행사 legislation, 뒤가 불완전(주어 없음) → that / 선행사 단수 → states / the right + to부정사 → to fix",
 "'보호하기 위해'(목적) → To protect / make + 목적어 + 형용사 보어 → available",
 "부품과 도구가 '필요로 되는' 수동 → required / '수리하기 위해' → to make",
 "전치사 of + 능동 동명사(소비자를 '막는') → preventing / prevent A from -ing, 소비자가 '설치하는' 능동 → installing / 관행이 '금지되는' 수동 → be prohibited",
 "demand의 목적어, 뒤가 완전 → that / 선행사 a way, 뒤가 불완전(주어 없음) → 관계대명사 that (how ✘) / 선행사 a way(단수) → makes / make + 목적어 + 형용사 보어 → as easy as possible",
 "say의 목적어, 뒤가 완전 → that / 목표가 '달성되는' 수동 → accomplished / 전자 폐기물이 '발생되는' 수동 → be generated",
 "현재진행 is + -ing(영향력을 '얻고 있는') → gaining / with + 명사 + 분사, 나라들이 '동참하는' 능동 → joining",
 "뒤에 동사가 바로 옴(주격 관계대명사) → that / 선행사 a bill(단수) → requires / require의 목적어, 뒤가 완전 → that",
 "분사구문, 지수가 점수를 '사용하는' 능동 → Using / let + 목적어 + 동사원형 → see / 간접의문문 → 의문사 + 주어 + 동사: how easily the product can / 제품이 '수리되는' 수동 → repaired",
 "mean의 목적어, 뒤가 완전 → that / 주어 자리 동명사 → repairing / indicate의 목적어, 뒤가 완전 → that / easy + to부정사 → to repair",
 "be designed + to부정사 → to have / allow + 목적어 + to부정사 → to make / 접속사 when + 능동 분사(소비자가 '구매할' 때) → purchasing",
 "encourage + 목적어 + to부정사 → to make / make + 목적어 + 형용사 보어 → easier / easy + to부정사 → to repair / 셀 수 있는 복수 items → fewer / with + 명사 + 분사, 물건이 '끝나는' 능동(end up) → ending / expect + to부정사 → to make",
 "be likely + to부정사 → to spread / 뒤에 동사가 바로 옴(주격 관계대명사) → that / 선행사 any company(단수) → wants / anticipate + 동명사 → seeing",
 "소비자가 도구를 '받는' 수동 → given / 선행사 the damage, 뒤가 불완전(주어 없음) → that / occur는 자동사라 수동 ✘ → occurs / That is why + 주어 + 동사 → Repair Cafés were",
 "선행사 meeting places(장소), 뒤가 완전 → 관계부사 where / 카페가 봉사자들로 '채워지는' 수동(be staffed by) → staffed / 선행사 volunteer experts(사람) → who / 의문사 + to부정사 → to fix",
 "such + a + 명사(a success) + that → such / such ~ that(너무 ~해서 …하다) → that / there + be + 복수 Repair Cafés → were",
 "전치사 Along with + 능동 동명사(물건을 '막는') → preventing / encourage + 목적어 + to부정사 → to share",
 "with + 명사 + 분사, 사람들이 '신청하는' 능동 → signing / 선행사 spaces(장소), 뒤가 완전 → where / enable + 목적어 + to부정사 → to maintain",
 "선행사 a sustainable perspective, 뒤가 불완전(주어 없음) → that / 선행사 the girl(사람) → who / 선행사 a world(장소), 뒤가 완전 → where / 동명사 주어 repairing ~은 단수 → was",
 "가정법 과거(If + 과거, 주절 wouldn't) → were / 선택지가 '제한되는' 수동 → be limited / 전치사 to + 동명사 → paying / or로 나란히 → throwing / and로 나란히 → buying",
 "'조언을 얻기 위해'(목적) → to get / 의문사 + to부정사 → to fix",
 "주어 자리 동명사 → Repairing / 그녀가 노트북을 '구입했을' 능동 → would have purchased",
 "전치사 in + 관계대명사(뒤가 완전한 절) → in which / 비교급 less 강조 → far (very ✘) / 분사구문, 미래가 지구를 '만드는' 능동 → making",
]
# 어휘 괄호 (문장 번호, 바꿀 낱말(괄호 밖 첫 번째), 오답, 해설)
VOC3 = [(2, 'simple', 'complex', "어휘: not as simple as + '수많은 목소리'를 수반 → simple (complex ✘ 앞뒤가 반대가 됨)"),
        (9, 'yield', 'wield', "어휘: 다른 결과를 낳다 → yield (wield 휘두르다 ✘)"),
        (17, 'uncomplicated', 'complicated', "어휘: and easy to understand와 나란히 → uncomplicated (complicated ✘)"),
        (17, 'weakness', 'strength', "어휘: but + 과반 지지 없이도 이길 수 있다 → 단점 weakness (strength ✘)"),
        (24, 'greater', 'lesser', "어휘: AV 방식의 결점 → 2순위 표가 1순위보다 '더 큰' 영향 → greater (lesser ✘)"),
        (29, 'fails', 'succeeds', "어휘: weakness의 내용 → 승자를 고르지 '못하다' fails (succeeds ✘)"),
        (30, 'numerous', 'few', "어휘: 선택지가 '많은' 선거에서 특히 그렇다 → numerous (few ✘)"),
        (34, 'flawless', 'flawed', "어휘: 어떤 투표 제도도 '흠이 없지' 않다 → flawless (flawed ✘)"),
        (35, 'accurate', 'arbitrary', "어휘: 더 복잡한 방식이 더 '정확한' 결과 → accurate (arbitrary 임의적인 ✘)")]
VOC4 = [(0, 'accidentally', 'intentionally', "어휘: 길에 '실수로' 떨어뜨림 → accidentally (intentionally ✘)"),
        (4, 'toxic', 'harmless', "어휘: 납 같은 '유독' 물질 때문에 위험 → toxic (harmless ✘)"),
        (4, 'alarming', 'reassuring', "어휘: To make matters worse + 증가 → '걱정스러운' 속도 alarming (reassuring ✘)"),
        (9, 'intentionally', 'accidentally', "어휘: What is more + 일부러 고치기 어렵게 설계 → intentionally (accidentally ✘)"),
        (16, 'less', 'more', "어휘: 수리할 권리가 이뤄지면 전자 폐기물이 '훨씬 적게' → less (more ✘)"),
        (22, 'sustainable', 'disposable', "어휘: 매립지로 가는 물건이 줄어 → 더 '지속 가능한' 사회 sustainable (disposable 일회용의 ✘)"),
        (27, 'invaluable', 'valueless', "어휘: invaluable = 매우 귀중한 (valueless 가치 없는 ✘ — in-이 '없는'이 아님!)"),
        (29, 'foster', 'hinder', "어휘: 미래에 큰 긍정적 영향 → 관점을 '기르다' foster (hinder 방해하다 ✘)")]
def addvoc(S, V, E):
    for i, w, bad, ex in V:
        s = S[i][0]; parts = re.split(r'(\{[^}]*\})', s); done = False
        for j, p in enumerate(parts):
            if not p.startswith('{') and re.search(r'\b%s\b' % re.escape(w), p) and not done:
                parts[j] = re.sub(r'\b%s\b' % re.escape(w), '{%s|%s}' % (w, bad), p, count=1); done = True
        assert done, (i, w); S[i][0] = ''.join(parts); E[i] += ' / ' + ex
D = {d['id']: d for d in PK['days']}
norm = lambda t: re.sub(r'\s+', ' ', t.replace('’', "'").replace('“', '"').replace('”', '"')).strip()
plain = lambda s: re.sub(r'\{([^|}]*)\|[^}]*\}', r'\1', s)
def build(gid, lesson, f, EX, VOC, groups, titles):
    S = parse(SRC + f); assert len(S) == len(EX), (f, len(S), len(EX))
    E = list(EX); addvoc(S, VOC, E)
    TX = {k: norm(' '.join(l[1] for l in D[k]['passage'] if not re.match(r'^[❶-❿]$', l[1]))) for k in groups}
    G = {k: [] for k in groups}; nb = 0
    for (s, ko), ex in zip(S, E):
        for h in HEADS:
            if s.startswith(h + ' '): s = s[len(h) + 1:]
        for m in re.findall(r'\{([^}]*)\}', s):
            a, b = m.split('|'); assert a != b
            if not re.search(r'[가-힣]', ex): pass
        where = [k for k in groups if norm(plain(s)) in TX[k]]; assert len(where) == 1, (plain(s), where)
        G[where[0]].append({'s': s, 'ko': ko, 'ex': ex}); nb += s.count('{')
    cnt = {k: sum(p['s'].count('{') for p in G[k]) for k in groups}
    day = {'id': gid, 'name': '', 'range': '%s 본문 · 어법·어휘 한 판' % lesson, 'story': '%s 본문 어법·어휘 한 판 · 괄호 %d개, 덩이 %d개 · 덩이마다 모두 맞혀야 100점' % (lesson, nb, len(groups)),
           'passage': sum((D[k]['passage'] for k in groups), []),
           'steps': [{'type': 'gate', 'title': '어법·어휘 한 판', 'guide': "본문을 %d덩이로 나눴어요. 워크북 어법 괄호에 문맥 어휘 괄호를 더했어요. 덩이마다 괄호를 모두 맞혀야 100점, 하나라도 틀리면 0점! 3번 안에 통과 못 하면 틀린 문장만 해설과 함께 연습하고 다시 도전해요." % len(groups),
                      'items': [{'title': '%s (괄호 %d개)' % (titles[k], cnt[k]), 'parts': G[k]} for k in groups]}]}
    return day, cnt
G3, c3 = build('gt3', '3과', 'L3.txt', EX3, VOC3, ['d1', 'd2', 'd3'], {'d1': '본문 ❶❷❸ · 투표를 해 보자', 'd2': '본문 ❹❺ · 단순 다수결 · 대안 투표', 'd3': '본문 ❻❼ · 콩도르세 · 정답은 없다'})
G4, c4 = build('gt4', '4과', 'L4.txt', EX4, VOC4, ['p1', 'p2', 'p3', 'p4'], {'p1': '본문 ❶❷ · Liz의 노트북 · 전자 폐기물', 'p2': '본문 ❸ · 수리할 권리 운동', 'p3': '본문 ❹❺ · 수리 가능성 지수', 'p4': '본문 ❻❼ · 리페어 카페'})
PK['days'] = [d for d in PK['days'] if d['id'] not in ('gt3', 'gt4')] + [G3, G4]
for i, d in enumerate(PK['days']): d['name'] = 'DAY %d' % (i + 1)
src = open(path, encoding='utf-8').read(); head = src[:src.index('window.PKG')]
tail = src[src.index('/* WRAPUP-TESTS'):]
PK.pop('tests', None)
if '한 판' not in head: head = head.rstrip('\n') + '\n/* 11/26: 3·4과 본문 어법·어휘 한 판 DAY gt3·gt4 맨 끝 (generators/gen_djgate.py) */\n'
write(PK, path, head)
open(path, 'a', encoding='utf-8').write(tail)
print('3과', c3, sum(c3.values()), '· 4과', c4, sum(c4.values()), '·', [d['name'] + ' ' + d['range'] for d in PK['days'][-2:]])
