import sys, json, subprocess, re
sys.path.insert(0, '/home/claude/work/gen')
from gencommon import write
# 고2 능률(오선영) 영어Ⅱ L3 · 본문 완전정복 DAY 4~6 (11/10) — 고1 능률(민) 완전정복과 같은 방식, 난이도↑
# ① 주요문장 덩어리 스크램블(덩어리를 더 잘게) ② 오류 사냥(단락마다 7~11곳: 어법 + 문맥상 어휘, 찾기 1점 + 고치기 1점)

CH = {
 '❶': [
  "We make / many personal choices / in our lives, / from who / to have lunch with / to what career / to pursue.",
  "However, / there are / many situations / where we must / make decisions / as a group.",
  "Group decision-making / is not as simple / as our personal choices, / as it involves / numerous voices / with differing opinions.",
  "Voting is often used / to make group decisions / fairer and more efficient, / and various voting methods / have been developed / over time.",
  "The following story / illustrates / how these different / voting methods / work.",
 ],
 '❷': [
  "The members / of the Greenville High School / student council / needed to decide / how to raise money / for children in need.",
  "Their three options / were an art show, / a bake sale, / and a charity concert, / but there were / conflicting opinions.",
  "So they decided / to put it / to a vote.",
  "When they asked / for advice / from Ms. Akers, / the council's advisor, / she encouraged them / not to use / the familiar voting method, / but to try / something different / instead.",
  "After doing / some research, / the council members / decided to try / three different voting systems: / the first-past-the-post (FPTP) method, / the alternative vote (AV) method, / and the Condorcet method.",
  "The entire council / was curious / to find out / if the different methods / would yield / different results.",
 ],
 '❸': [
  "On the day of the vote, / each possible event / was given a letter: / \"art show\" was represented / by the letter A, / the letter B / indicated \"bake sale,\" / and C stood for / \"charity concert.\"",
  "Each of / the 20 council members / was given / a voting slip / and instructed / to write down the options / in order of preference.",
  "For example, / if the charity concert / was their first choice, / followed by / the bake sale / and the art show, / they would write CBA.",
  "After every member / had voted, / the voting slips / were counted.",
  "The results / were / as follows:",
 ],
 '❹': [
  "The FPTP method / is the simplest / of the three methods.",
  "Voters are given / several options, / and whichever gets / the most / first-preference votes / wins.",
  "Neither the second / nor third preference / matters at all, / so they / are ignored.",
  "This method / is commonly used / in political elections / around the world.",
  "The student council / quickly determined / that the winner / would be option C, / the charity concert.",
  "This was because / it received / 8 first-preference votes, / while option A / received 5 / and option B / received 7.",
  "The FPTP method / is uncomplicated / and easy to understand, / but it has / a significant weakness.",
  "It is possible / to win a vote / without the support / of the majority.",
  "That was / the case / here.",
  "According to / the results / of the FPTP method, / the council's choice / was to hold / a charity concert.",
  "However, / only 8 out of 20 / council members / chose the charity concert / as their first preference, / which equaled / 40% of / the total votes.",
 ],
 '❺': [
  "Next, / the council members / examined the votes / using the AV method, / and they soon realized / that there would be / a different result.",
  "The AV method / can potentially include / more than / one round / of counting.",
  "For an option / to win / in the first round, / it needs to get / more than 50% / of the first-preference votes.",
  "As the charity concert / only received / 40% of the total votes, / a second round / of counting / was required.",
  "Option A, / the art show, / received the fewest / first-preference votes, / with only / 5 council members / voting for it.",
  "Therefore, / option A / was eliminated, / and the 5 council members' votes / were redistributed / based on / their second preferences.",
  "As a result, / 4 votes / for option B (ABC) / and 1 / for option C (ACB) / were added / to the total.",
  "This meant / that option B / had 11 total votes, / while option C / had only 9.",
  "As a result, / the bake sale / would be / the winner.",
  "Unfortunately, / the AV method / is not perfect / either.",
  "It sometimes allows / second-preference votes / to have / a greater influence / than / first-preference votes.",
  "In this case, / the bake sale won, / but this was / mainly due to / the second-preference votes / it received.",
 ],
 '❻': [
  "Finally, / the student council / counted the votes / using / the Condorcet method.",
  "This method / involves comparing / the voters' preferences / between / each possible pair / of options.",
  "In this case, / there were / three pairs / to consider: / A vs. B, / B vs. C, / and A vs. C.",
  "Through this method, / the student council / discovered that / its members / preferred option A / to option B / by a count / of 11 to 9.",
  "In other words, / 11 people / preferred A to B, / voting either / ABC, ACB, / or CAB.",
  "Meanwhile, / 9 people / preferred B to A / by voting / BAC, BCA, / or CBA.",
  "Interestingly, / the voters / preferred option B / to option C / by the same count / of 11 to 9.",
  "They also preferred / option A / to option C / by 11 to 9.",
  "As option A, / the art show, / was preferred / to both of / the other options, / it would be considered / the winner.",
  "The Condorcet method's weakness / is that, / along with / being complex, / it sometimes fails / to select / a winner.",
  "This is / especially true / in elections / that contain / numerous options.",
  "It is possible / that no option / will be / clearly preferred / over the others.",
 ],
 '❼': [
  "Instead of / all methods / pointing toward / a single option / and making / the council's choice easier, / the winner differed / with each method.",
  "After a long, / intense discussion / with Ms. Akers, / the student council members / decided to choose / the Condorcet method, / as they liked / the idea of / directly comparing / each option / with the others.",
  "Everyone agreed / that they learned / a lot / about different voting systems / through this experience.",
  "It is obvious / that choosing / an ideal voting method / is a complex / and challenging task.",
  "No voting system / is flawless / or clearly superior / to another.",
  "Whichever / we choose / will have / pros and cons.",
  "Some people believe / that it is best / to keep the process simple / by not ranking / our choices / at all.",
  "Others continue / to develop and test / new ways of voting, / arguing that / more complex methods / deliver / more accurate results.",
  "All of these efforts / are designed / not to make / decision-making / difficult and inefficient, / but to help us / make better decisions / as a society.",
  "Ultimately, / understanding / all of the possible voting methods / and weighing / their pros and cons / allows us / to better understand / the process of decision-making.",
  "When we understand / decision-making better, / we are more likely / to become / better decision-makers / ourselves.",
 ],
}

HUNT = {
 '❶': ("We make many personal choices in our lives, from who to have lunch with to what career [[pursuing|to pursue]]. "
       "However, there [[is|are]] many situations [[which|where]] we must make decisions as a group. "
       "Group decision-making is not as simple [[than|as]] our personal choices, as it involves numerous voices with [[identical|differing]] opinions. "
       "Voting is often used to make group decisions [[fairly|fairer]] and more efficient, and various voting methods have been developed over time. "
       "The following story illustrates how these different voting methods [[works|work]].",
       ["의문사 + to부정사: what career to pursue (어떤 직업을 추구할지) — who to have lunch with와 병렬",
        "there + be + 주어: 주어 many situations(복수) → are",
        "선행사 situations + 완전한 절(we must make decisions) → 관계부사 where. which 뒤는 불완전한 절",
        "as + 원급 + as (~만큼 …한). than은 비교급과 짝",
        "[어휘] 집단 결정이 단순하지 않은 이유 → '서로 다른(differing)' 의견. identical(동일한)이면 결정이 쉬워져요",
        "make + 목적어 + 형용사 보어: make decisions fairer and more efficient (more efficient와 병렬인 비교급 형용사)",
        "간접의문문 how + 주어(these different voting methods, 복수) + 동사 → work"]),
 '❷': ("The members of the Greenville High School student council [[needs|needed]] to decide how [[raising|to raise]] money for children in need. "
       "Their three options were an art show, a bake sale, and a charity concert, but there were [[agreeing|conflicting]] opinions. "
       "So they decided to put it to a vote. "
       "When they asked for advice from Ms. Akers, the council's advisor, she encouraged them not to use the [[unusual|familiar]] voting method, but [[trying|to try]] something different instead. "
       "After [[do|doing]] some research, the council members decided to try three different voting systems: the first-past-the-post (FPTP) method, the alternative vote (AV) method, and the Condorcet method. "
       "The entire council was curious to find out [[that|if]] the different methods would yield different results.",
       ["주어의 핵 The members(복수), of ~ council은 수식어. 이야기 전체가 과거 → needed",
        "의문사 + to부정사: how to raise (어떻게 모금할지) — decide의 목적어",
        "[어휘] but(그러나) 뒤 → 의견이 '충돌하는(conflicting)'. 그래서 투표에 부침",
        "[어휘] 익숙한 방법 대신 '다른 것(something different)'을 시도 → 익숙한(familiar) 방법을 쓰지 말라. unusual(특이한)이면 뒤와 모순",
        "encourage + 목적어 + not to A, but to B — not to use와 병렬 → to try",
        "전치사 After 뒤 → 동명사 doing",
        "find out의 목적어 '~인지 아닌지' → if(= whether). 결과가 다를지 '궁금했다(curious)'이므로 that은 부적절"]),
 '❸': ("On the day of the vote, each possible event [[gave|was given]] a letter: \"art show\" was [[representing|represented]] by the letter A, the letter B [[indicating|indicated]] \"bake sale,\" and C stood for \"charity concert.\" "
       "Each of the 20 council members [[were|was]] given a voting slip and [[instructing|instructed]] to write down the options in order of preference. "
       "For example, if the charity concert was their first choice, [[following|followed]] by the bake sale and the art show, they would write CBA. "
       "After every member [[has|had]] voted, the voting slips were counted. "
       "The results were as [[follow|follows]]:",
       ["행사가 글자를 '부여받은' 수동 → was given (give A B의 수동: A was given B)",
        "by the letter A(행위자) → 수동 was represented",
        "콜론 뒤 세 절의 병렬(was represented / indicated / stood for) → 동사 자리 과거형 indicated. indicating이면 동사가 없음",
        "Each of + 복수명사 → 단수 동사 was",
        "was given ~ and (was) instructed — 지시를 '받은' 수동 병렬 → instructed",
        "콘서트 뒤에 빵 바자회가 '이어지는' — 분사구문, by ~가 있으므로 수동 followed",
        "투표용지를 센(과거) 것보다 투표가 '먼저' 끝남 → 과거완료 had voted",
        "as follows는 관용 표현(다음과 같이) — 주어가 복수여도 항상 follows"]),
 '❹': ("The FPTP method is the [[simpler|simplest]] of the three methods. "
       "Voters are given several options, and whichever [[get|gets]] the most first-preference votes wins. "
       "Neither the second nor third preference [[matter|matters]] at all, so they are [[considered|ignored]]. "
       "This method is commonly [[using|used]] in political elections around the world. "
       "The student council quickly determined that the winner would be option C, the charity concert. "
       "This was because it received 8 first-preference votes, [[during|while]] option A received 5 and option B received 7. "
       "The FPTP method is [[complicated|uncomplicated]] and easy to understand, but it has a significant weakness. "
       "It is possible to win a vote without the support of the [[minority|majority]]. "
       "That was the case here. "
       "According to the results of the FPTP method, the council's choice was to hold a charity concert. "
       "However, only 8 out of 20 council members [[choose|chose]] the charity concert as their first preference, [[that|which]] equaled 40% of the total votes.",
       ["of the three(셋 중에서) → 최상급 the simplest. 비교급은 둘 사이",
        "whichever(~하는 것은 어느 것이든)가 이끄는 명사절의 동사 — whichever 자체가 단수 주어 → gets",
        "Neither A nor B는 B에 수일치 → third preference(단수) → matters",
        "[어휘] 2·3지망은 전혀 중요하지 않다(not matter at all) → '무시된다(ignored)'. considered(고려된다)와 반대",
        "방식이 '사용되는' 수동 → is commonly used",
        "뒤에 절(option A received 5 ~)이 옴 → 접속사 while(반면에). during은 전치사라 명사만 와요",
        "[어휘] and easy to understand와 병렬 → 복잡하지 '않은' uncomplicated. but 뒤 '상당한 약점'과 대조",
        "[어휘] 8표(40%)로 이김 → '과반수(majority)'의 지지 없이도 승리 가능. 바로 다음 That was the case here",
        "이야기 속 과거의 일 → 과거시제 chose (choose - chose - chosen)",
        "콤마 뒤 계속적 용법(앞 내용 8 out of 20을 받음) → which. that은 계속적 용법 불가"]),
 '❺': ("Next, the council members examined the votes [[used|using]] the AV method, and they soon realized that there would be a different result. "
       "The AV method can potentially include more than one round of counting. "
       "For an option to win in the first round, it needs [[getting|to get]] more than 50% of the first-preference votes. "
       "As the charity concert only received 40% of the total votes, a second round of counting was [[requiring|required]]. "
       "Option A, the art show, received the [[most|fewest]] first-preference votes, with only 5 council members [[voted|voting]] for it. "
       "Therefore, option A was [[added|eliminated]], and the 5 council members' votes were [[redistributing|redistributed]] based on their second preferences. "
       "As a result, 4 votes for option B (ABC) and 1 for option C (ACB) [[was|were]] added to the total. "
       "This meant that option B had 11 total votes, while option C had only 9. "
       "As a result, the bake sale would be the winner. "
       "Unfortunately, the AV method is not perfect [[too|either]]. "
       "It sometimes allows second-preference votes [[have|to have]] a greater influence than first-preference votes. "
       "In this case, the bake sale won, but this was mainly [[because|due to]] the second-preference votes it received.",
       ["구성원들이 AV 방식을 '사용하여'(능동, 목적어 the AV method) → 분사구문 using",
        "need + to부정사(~할 필요가 있다). need -ing는 '~될 필요가 있다'(수동 의미)라 여기선 틀림",
        "2차 집계가 '요구되는' 수동 → was required",
        "[어휘] with only 5 council members(겨우 5명) → '가장 적은(fewest)' 1지망 표. 그래서 탈락",
        "with + 목적어 + 분사: 구성원들이 '투표하는' 능동 → voting",
        "[어휘] 가장 적은 표를 받은 A는 '제거되고(eliminated)' 그 표가 2지망대로 재분배됨",
        "표가 '재분배되는' 수동 → were redistributed",
        "주어 4 votes ~ and 1 (vote) ~ → 복수 → were",
        "부정문에서 '~도 역시' → either (too는 긍정문)",
        "allow + 목적어 + to부정사",
        "뒤에 명사구(the second-preference votes ~) → 전치사 due to. because는 접속사라 절이 와야 해요"]),
 '❻': ("Finally, the student council counted the votes using the Condorcet method. "
       "This method involves [[to compare|comparing]] the voters' preferences between each possible pair of options. "
       "In this case, there were three pairs to consider: A vs. B, B vs. C, and A vs. C. "
       "Through this method, the student council discovered that its members preferred option A [[than|to]] option B by a count of 11 to 9. "
       "In other words, 11 people preferred A to B, voting either ABC, ACB, [[and|or]] CAB. "
       "Meanwhile, 9 people preferred B to A by [[vote|voting]] BAC, BCA, or CBA. "
       "Interestingly, the voters preferred option B to option C by the [[different|same]] count of 11 to 9. "
       "They also preferred option A to option C by 11 to 9. "
       "As option A, the art show, was preferred to both of the [[another|other]] options, it would be [[considering|considered]] the winner. "
       "The Condorcet method's weakness is that, along with [[be|being]] complex, it sometimes [[succeeds|fails]] to select a winner. "
       "This is especially true in elections that [[contains|contain]] numerous options. "
       "It is possible that no option will be [[clear|clearly]] preferred over the others.",
       ["involve + 동명사 (~을 포함하다, 수반하다)",
        "prefer A to B (B보다 A를 선호하다) — than 불가",
        "either A, B, or C (A, B, C 중 하나)",
        "전치사 by 뒤 → 동명사 voting (~함으로써)",
        "[어휘] Interestingly + 앞과 같은 11 to 9 → 'the same count'. different면 같은 숫자를 다시 쓸 이유가 없어요",
        "both of the other options (나머지 두 선택지). another는 단수명사 앞",
        "A가 승자로 '여겨지는' 수동 → would be considered",
        "전치사 along with 뒤 → 동명사 being",
        "[어휘] 약점(weakness) → 승자를 고르는 데 '실패한다(fails)'. 다음 문장 '선택지가 많을 때 특히 그렇다'",
        "주격 관계대명사 that의 선행사 elections(복수) → contain",
        "과거분사 preferred를 꾸미는 말 → 부사 clearly"]),
 '❼': ("Instead of all methods pointing toward a single option and making the council's choice [[easily|easier]], the winner differed with each method. "
       "After a long, intense discussion with Ms. Akers, the student council members decided to choose the Condorcet method, as they liked the idea of directly [[compare|comparing]] each option with the others. "
       "Everyone agreed that they learned a lot about different voting systems through this experience. "
       "It is obvious that choosing an ideal voting method [[are|is]] a complex and challenging task. "
       "No voting system is [[flawed|flawless]] or clearly superior [[than|to]] another. "
       "Whichever we choose will have pros and cons. "
       "Some people believe that it is best to keep the process [[simply|simple]] by not ranking our choices at all. "
       "Others continue to develop and test new ways of voting, [[argued|arguing]] that more complex methods deliver more [[accurately|accurate]] results. "
       "All of these efforts are designed not to make decision-making difficult and inefficient, but [[helping|to help]] us make better decisions as a society. "
       "Ultimately, understanding all of the possible voting methods and weighing their pros and cons allows us to better understand the process of decision-making. "
       "When we understand decision-making better, we are more likely [[becoming|to become]] better decision-makers [[us|ourselves]].",
       ["make + 목적어 + 형용사 보어 → easier (선택을 더 쉽게 만들다)",
        "전치사 of 뒤 → 동명사 comparing (부사 directly가 앞에서 꾸밈)",
        "that절의 주어 = 동명사구 choosing an ideal voting method → 단수 is",
        "[어휘] 뒤 '어느 것이든 장단점이 있다' → 어떤 시스템도 '결점이 없지(flawless)' 않다. No ~ flawed면 '모두 완벽'이 되어 모순",
        "superior to (~보다 우월한) — 라틴어 비교급은 than 대신 to",
        "keep + 목적어 + 형용사 보어 → simple",
        "분사구문: 다른 사람들이 '주장하면서'(능동) → arguing",
        "명사 results를 꾸미는 말 → 형용사 accurate",
        "not to A, but to B 병렬 → to help",
        "be likely + to부정사 (~할 가능성이 있다)",
        "주어 we가 '스스로' — 강조의 재귀대명사 ourselves"]),
}

path = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/proj/data/h2-ne-oh-L3.js'
PK = json.loads(subprocess.check_output(['node', '-e', "global.window={};require('%s');process.stdout.write(JSON.stringify(window.PKG))" % path]))
base = [d for d in PK['days'] if not re.match(r'f\d$', d['id'])]
BODY = [d for d in base if re.match(r'd\d$', d['id'])]
KO = {}
for d in BODY:
    for l in d['passage']:
        if l[0] != '#' and l[2]: KO[l[1]] = l[2]

def sec_passage(secs):
    out = []
    for d in BODY:
        on = False
        for l in d['passage']:
            if not l[0] and len(l[1]) == 1 and not l[2]: on = l[1] in secs
            if on: out.append(l)
    return out

def mkday(did, secs, rng):
    scr = []
    for s in secs:
        for c in CH[s]:
            en = c.replace(' / ', ' ')
            assert en in KO, (s, en)
            if len(c.split(' / ')) >= 4: scr.append({'ko': KO[en], 'en': en, 'chunks': c.split(' / ')})
    hunt = []
    for s in secs:
        txt, why = HUNT[s]
        fixed = re.sub(r'\[\[([^|\]]*)\|([^\]]*)\]\]', r'\2', txt)
        want = ' '.join(c.replace(' / ', ' ') for c in CH[s])
        assert fixed == want, (s, [(a, b) for a, b in zip(fixed.split(), want.split()) if a != b][:3])
        n = len(re.findall(r'\[\[', txt)); assert n == len(why), (s, n, len(why))
        hunt.append({'label': '본문 ' + s, 's': txt, 'why': why})
    return {'id': did, 'name': 'DAY', 'range': '3과 본문 완전정복 ' + rng, 'story': '주요문장 덩어리 배열 → 틀린 곳 ' + '·'.join(str(len(HUNT[s][1])) + '개' for s in secs) + ' 찾아 고치기 (어법 + 문맥 어휘)',
            'passage': sec_passage(secs), 'steps': [
        {'type': 'scramble', 'title': '주요문장 덩어리 스크램블', 'guide': '우리말을 보고 잘게 나뉜 의미 덩어리를 순서대로 눌러 문장 전체를 완성하세요.', 'items': scr},
        {'type': 'hunt', 'title': '오류 사냥 · 틀린 곳 찾아 고치기', 'guide': '단락에서 틀린 곳을 정해진 개수만큼 찾고(1점), 바르게 고쳐 쓰세요(1점). 어법뿐 아니라 문맥에 맞지 않는 낱말도 있어요.', 'items': hunt}]}

# 본문 전 문장이 CH에 다 들어갔는지 (소제목 줄 제외)
allen = [l[1] for d in BODY for l in d['passage'] if l[0] != '#' and l[2]]
used = {c.replace(' / ', ' ') for v in CH.values() for c in v}
missing = [e for e in allen if e not in used and len(e.split()) > 4]
assert not missing, missing

NEW = [mkday('f1', ['❶', '❷', '❸'], '❶❷❸'), mkday('f2', ['❹', '❺'], '❹❺'), mkday('f3', ['❻', '❼'], '❻❼')]
k = max(i for i, d in enumerate(base) if re.match(r'd\d$', d['id']))
PK['days'] = base[:k + 1] + NEW + base[k + 1:]
for i, d in enumerate(PK['days']): d['name'] = 'DAY %d' % (i + 1)
src = open(path, encoding='utf-8').read(); head = src[:src.index('window.PKG')]
tail = src[src.index('/* WRAPUP-TESTS'):] if '/* WRAPUP-TESTS' in src else ''
if '본문 완전정복' not in head: head = head.rstrip('\n') + '\n/* 11/10: DAY 4~6 3과 본문 완전정복(잘게 나눈 덩어리 스크램블 · 오류 사냥 어법+어휘) gen/gen_h2ohfull.py — 어휘 DAY는 7~11로 밀림 */\n'
PK.pop('tests', None)
write(PK, path, head)
if tail: open(path, 'a', encoding='utf-8').write(tail)
print('ok', [(d['name'], d['range'], [len(s['items']) for s in d['steps']]) for d in PK['days']])
