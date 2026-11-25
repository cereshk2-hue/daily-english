# 11/25 발산중2 외부지문 어법·어휘 한 판 — 지문 하나 = DAY 하나 (m2-visang-hwang-L7 맨 끝: ex1 Reading Material 1 · ex2 Reading Material 2)
# 원본: 선생님이 보낸 '발산중2 외부지문 구문 분석지' PDF → work_src/bsext/bs_ext.txt (원문), bs_ko.txt (해석 31줄)
# 괄호 {정답|오답}: 어법 + 어휘(문맥상 분명히 틀린 낱말만). try to/-ing, came home safe/safely처럼 둘 다 되는 건 안 냄
import sys, json, re, subprocess
sys.path.insert(0, '/home/claude/srcrepo/generators')
from gencommon import write
path = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/proj/data/m2-visang-hwang-L7.js'
PK = json.loads(subprocess.check_output(['node', '-e', "global.window={};require('%s');process.stdout.write(JSON.stringify(window.PKG))" % path]))
KO = open('/home/claude/srcrepo/work_src/bsext/bs_ko.txt', encoding='utf-8').read().split('\n')[:31]
R1 = [
 ("Every country {has|have} its own {unique|common} conversation style.", "every + 단수 명사 → has / 어휘: 그 나라만의(its own) 독특한 → unique (common 흔한 ✘)"),
 ("You can {compare|complete} the different styles {to|from} sports.", "어휘: compare A to B = A를 B에 비유하다 (complete 완성하다 ✘) / compare A to B → to"),
 ("Japanese conversations are {like|alike} bowling.", "전치사 like + 명사 = ~와 같은 (alike는 뒤에 명사를 바로 못 씀)"),
 ("Each person {waits|wait} for their {turn|return}, just like bowlers.", "each + 단수 명사 → waits / 어휘: 자기 차례 → turn (return 돌아옴 ✘)"),
 ("{Even if|Even} there {are|is} long pauses during conversation, others never {break in|break down}.", "Even if + 주어 + 동사 = 비록 ~일지라도 (Even만으로는 절을 못 이음) / There are + 복수 pauses / 어휘: 끼어들다 → break in (break down 고장 나다 ✘)"),
 ("{On the other hand|For example}, American conversations are like basketball.", "일본(끼어들지 않음) ↔ 미국(끼어듦) 대조 → On the other hand (For example ✘)"),
 ("When someone {hesitates|hesitate}, another person {interrupts|interrupt}.", "someone은 단수 → hesitates / another + 단수 명사 → interrupts"),
 ("It's like when basketball players {steal|steals} the ball.", "주어 basketball players(복수) → steal"),
 ("Italian conversations {are|is} like rugby.", "주어 conversations(복수) → are"),
 ("Just like rugby players, Italians use {a lot of|much} hand gestures and {interrupt|interrupting} others {frequently|rarely}.", "셀 수 있는 복수 gestures → a lot of (much ✘) / use와 and로 나란히 → interrupt / 어휘: 럭비처럼 자주 끼어듦 → frequently (rarely 거의 ~않는 ✘)"),
 ("Interestingly, Italians tend {to take|taking} interruptions as a sign of {interest|boredom} in the conversation rather than a lack of {thoughtfulness|thoughtful}.", "tend + to부정사 = ~하는 경향이 있다 / 어휘: 배려 부족이 아니라 '관심'의 표시 → interest (boredom 지루함 ✘) / a lack of + 명사 → thoughtfulness"),
 ("The next time you talk with foreign friends, remember {that|what} they have their ways of \"playing ball\" and try {to match|match} them.", "remember + that절(뒤가 완전한 문장) → that (what ✘) / try + to부정사 = ~하려고 노력하다 → to match"),
]
R2 = [
 ("In the 1960s, going to space {was|were} a new {venture|vacation}.", "동명사 주어(going to space) → 단수 was / 어휘: 새로운 모험 → venture (vacation 휴가 ✘)"),
 ("It was {incredibly|incredible} dangerous.", "형용사 dangerous를 꾸미는 부사 → incredibly"),
 ("Many of the young men {who|which} wanted to be the first astronauts {had|has} families.", "선행사 the young men(사람) → who / 주어 Many(of the young men) 복수 → had"),
 ("Besides {worrying|worry} about training, they were {worried|worrying} about their wives and children.", "전치사 Besides + 동명사 → worrying / 사람이 걱정하는 감정 → be worried about"),
 ("They wanted to make sure if they died, their families would {be taken|take} care of.", "가족이 '보살핌을 받는' 것 → 수동태 be taken care of"),
 ("{However|Therefore}, insurance companies did not want {to give|giving} life insurance policies to these astronauts.", "가족을 지키고 싶었다 ↔ 보험사는 거절 → 역접 However / want + to부정사 → to give"),
 ("It was simply too {risky|safe}.", "어휘: 보험을 안 들어 준 이유 → 너무 위험해서 risky (safe 안전한 ✘)"),
 ("The astronauts decided {to use|using} a {creative|boring} way to get money.", "decide + to부정사 → to use / 어휘: 사인을 보험으로 쓴 기발한 방법 → creative (boring 지루한 ✘)"),
 ("They signed {thousands|thousand} of autographs for {eager|bored} fans.", "thousands of + 복수 명사 = 수천의 / 어휘: 사인을 원하는 열성 팬 → eager (bored 지루해하는 ✘)"),
 ("They knew {that|what} people liked to collect {famous|cheap} things.", "knew + that절(뒤가 완전한 문장) → that / 어휘: 유명한 것을 모으기 좋아함 → famous (cheap 값싼 ✘)"),
 ("They gave the autographs {to|for} their friends.", "give A to B = B에게 A를 주다 → to"),
 ("On the day of the launch, the friends took them to the post office to have the envelopes {stamped|stamp} with the date.", "have + 목적어 + 과거분사 = (목적어가) ~되게 하다, 봉투가 소인이 '찍히는' 것 → stamped"),
 ("Then, the envelopes {were given|gave} to the astronauts' families.", "봉투가 가족에게 '주어진' 것 → 수동태 were given"),
 ("It was life insurance in the {form|from} of autographs.", "in the form of = ~의 형태로 → form (from ~로부터 ✘, 철자 함정)"),
 ("If the astronauts did not {return|returned} from the moon, their families could {sell|buy} them.", "did not + 동사원형 → return / 어휘: 사인을 '팔아서' 돈을 얻음 → sell (buy 사다 ✘)"),
 ("Thankfully, however, life insurance autographs {were not needed|did not need}.", "사인이 '필요하게 되지' 않음 → 수동태 were not needed"),
 ("They walked on the moon and {came|come} home safely.", "walked와 and로 나란히(과거) → came"),
 ("They probably signed tens of {thousands|thousand} more autographs for {free|freely}.", "tens of thousands = 수만의 / for free = 무료로 (for 뒤에는 freely ✘)"),
]
ORIG1 = "Every country has its own unique conversation style. You can compare the different styles to sports. Japanese conversations are like bowling. Each person waits for their turn, just like bowlers. Even if there are long pauses during conversation, others never break in. On the other hand, American conversations are like basketball. When someone hesitates, another person interrupts. It's like when basketball players steal the ball. Italian conversations are like rugby. Just like rugby players, Italians use a lot of hand gestures and interrupt others frequently. Interestingly, Italians tend to take interruptions as a sign of interest in the conversation rather than a lack of thoughtfulness. The next time you talk with foreign friends, remember that they have their ways of \"playing ball\" and try to match them."
ORIG2 = "In the 1960s, going to space was a new venture. It was incredibly dangerous. Many of the young men who wanted to be the first astronauts had families. Besides worrying about training, they were worried about their wives and children. They wanted to make sure if they died, their families would be taken care of. However, insurance companies did not want to give life insurance policies to these astronauts. It was simply too risky. The astronauts decided to use a creative way to get money. They signed thousands of autographs for eager fans. They knew that people liked to collect famous things. They gave the autographs to their friends. On the day of the launch, the friends took them to the post office to have the envelopes stamped with the date. Then, the envelopes were given to the astronauts' families. It was life insurance in the form of autographs. People really wanted their autographs. If the astronauts did not return from the moon, their families could sell them. Thankfully, however, life insurance autographs were not needed. They walked on the moon and came home safely. They probably signed tens of thousands more autographs for free."
PLAIN = lambda s: re.sub(r'\{([^|}]*)\|[^}]*\}', r'\1', s)
SENT = lambda t: re.split(r'(?<=[.!?"])\s+(?=[A-Z])', t)
S1, S2 = SENT(ORIG1), SENT(ORIG2)
assert len(S1) == 12 and len(S2) == 19, (len(S1), len(S2))
def parts(R, S, K):
    out, nb = [], 0
    for s, ex in R:
        p = PLAIN(s); assert p in S, p
        for m in re.findall(r'\{([^}]*)\}', s): o = m.split('|'); assert len(o) == 2 and o[0] != o[1]; nb += 1
        out.append({'s': s, 'ko': K[S.index(p)], 'ex': ex})
    return out, nb
P1, n1 = parts(R1, S1, KO[:12]); P2, n2 = parts(R2, S2, KO[12:31])
guide = "지문 전체를 한 번에 풀어요. 어법(문법)과 어휘(문맥에 맞는 낱말) 괄호를 모두 맞혀야 100점, 하나라도 틀리면 0점! 3번 안에 통과 못 하면 틀린 문장만 해설과 함께 연습하고 다시 도전해요."
def day(i, title, S, K, P, nb):
    pas = [['#', 'Reading Material %d · %s' % (i, title), '']] + [['', s, k] for s, k in zip(S, K)]
    return {'id': 'ex%d' % i, 'name': '', 'range': '외부지문 %d · 어법·어휘 한 판' % i, 'story': 'Reading Material %d · %s · 괄호 %d개, 모두 맞혀야 100점' % (i, title, nb),
            'passage': pas, 'steps': [{'type': 'gate', 'title': '어법·어휘 한 판', 'guide': guide, 'items': [{'title': 'Reading Material %d · %s (괄호 %d개)' % (i, title, nb), 'parts': P}]}]}
E1 = day(1, '나라별 대화 방식 (스포츠 비유)', S1, KO[:12], P1, n1); E2 = day(2, '우주 비행사의 사인 보험', S2, KO[12:31], P2, n2)
src = open(path, encoding='utf-8').read(); head = src[:src.index('window.PKG')]
tail = src[src.index('/* BS8CS-TESTS'):] if '/* BS8CS-TESTS' in src else ''
if tail: PK['tests'] = [t for t in PK['tests'] if not t['id'].startswith('bs8cs-')]
PK['days'] = [d for d in PK['days'] if d['id'] not in ('ex1', 'ex2')] + [E1, E2]
for i, d in enumerate(PK['days']): d['name'] = 'DAY %d' % (i + 1)
if '외부지문' not in head: head = head.rstrip('\n') + '\n/* 11/25: 외부지문 어법·어휘 한 판 DAY ex1·ex2 맨 끝 (generators/gen_bsext.py) */\n'
write(PK, path, head)
if tail: open(path, 'a', encoding='utf-8').write(tail)
print('괄호', n1, n2, [d['name'] + ' ' + d['range'] for d in PK['days']][-2:])
