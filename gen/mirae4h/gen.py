# 11/28 중산고2 미래엔(김성연) 영어Ⅱ L4 What-If Science — 본문 학습 이어서 고난도 2세트 (h2-mirae-kim-L4 맨 끝 DAY hs1 ❶~❹ · hs2 ❺~❽)
# 단계: ① 순서 배열 고난도(mc, 주어진 글 + (A)(B)(C)) ② 문장 삽입 고난도(insert, 6문장·빈칸 5곳) ③ 어휘 상 '이런 뜻도 있었어?'(다의어 문맥 의미·같은 의미) ④ 본문 문법(밑줄·네모·같은 쓰임·전환·개수·영작)
# 삽입·순서는 답이 한 곳으로만 정해지는 것만. 문법은 정답으로 고친 문장을 원문과 대조(줄인 문장은 MISS로 출력해 눈으로 확인)
import json, re, subprocess, sys
sys.path.insert(0, '/home/claude/srcrepo/generators')
from gencommon import write
path = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/proj/data/h2-mirae-kim-L4.js'
PK = json.loads(subprocess.check_output(['node', '-e', "global.window={};require('%s');process.stdout.write(JSON.stringify(window.PKG))" % path]))
D = {d['id']: d for d in PK['days']}
def body(ids): return [l[1] for i in ids for l in D[i]['passage'] if l[0] != '#' and not re.match(r'^[❶-❿]$', l[1]) and not re.match(r'^\d\. What if', l[1])]
def kor(ids): return {l[1]: l[2] for i in ids for l in D[i]['passage'] if l[0] != '#'}
E1, E2 = body(['d1']), body(['d2', 'd3'])
SRC = ' '.join(E1 + E2)
assert len(E1) == 18 and len(E2) == 38, (len(E1), len(E2))
C5 = ['①', '②', '③', '④', '⑤']; CNT = ['1개', '2개', '3개', '4개', '5개']
U = lambda n, w: '%s<u>%s</u>' % (C5[n - 1], w)
def P(*xs): return '<div class="wbox en">' + ''.join('<p>%s</p>' % x for x in xs) + '</div>'
def find(E, start): return next(i for i, s in enumerate(E) if s.startswith(start))
# ── 순서 배열: (주어진 글 [시작어들], {(A):시작어, ...}, 정답 순서, 해설) ──
def ORD(E, given, parts, ans, ex):
    g = ' '.join(E[find(E, x)] for x in given)
    pt = {k: ' '.join(E[find(E, x)] for x in v) for k, v in parts.items()}
    perms = ['(A) – (C) – (B)', '(B) – (A) – (C)', '(B) – (C) – (A)', '(C) – (A) – (B)', '(C) – (B) – (A)', '(A) – (B) – (C)']
    right = ' – '.join('(%s)' % c for c in ans)
    opts = [right] + [p for p in perms if p != right and p != '(A) – (B) – (C)'][:4]
    q = '주어진 글 다음에 이어질 글의 순서로 가장 적절한 것은?' + P(g, '―――――――――――――――', *['(%s) %s' % (k, pt[k]) for k in 'ABC'])
    return {'q': q, 'opts': opts, 'ex': '정답 ▶ %s\n%s' % (right, ex)}
O1 = [
 ORD(E1, ['Have you ever wondered'], {'A': ['The Italian scientist'], 'B': ['If you have asked'], 'C': ['With only his thoughts']}, 'BAC',
     "(B) this kind of question = 주어진 글의 'What if ~?' 같은 질문 → '다음 갈릴레이가 될 수 있다' → (A) 그 갈릴레이가 누구인지(사고 실험으로 유명) → (C) his thoughts의 his = 갈릴레이, 그가 생각만으로 증명한 것"),
 ORD(E1, ['When the length of', 'These changes can'], {'A': ['One issue is'], 'B': ['However, the area of the feet'], 'C': ["If a person's height increased"]}, 'ACB',
     "(A) many problems 중 '하나의 문제'(One issue) = 발이 몸무게를 못 버팀 → (C) 키가 10배면 몸무게는 1,000배 → (B) However, 발바닥 면적은 100배뿐 — 앞의 1,000배와 대조"),
 ORD(E1, ['In addition, there is'], {'A': ["If a person's height were to"], 'B': ['However, the surface area'], 'C': ['Heat is generated']}, 'CAB',
     "(C) 열 방출이란? 몸에서 생긴 열이 피부로 방출됨 → (A) 키가 10배면 열은 1,000배(부피에 비례) → (B) However, 피부 면적은 100배뿐 → 열이 충분히 빠져나가지 못함"),
]
O2 = [
 ORD(E2, ["The Moon's gravity causes"], {'A': ['Without the Moon, however, the Earth'], 'B': ['This friction leads'], 'C': ['Since the ocean is moving']}, 'CBA',
     "(C) 바다가 오르내리고 지구는 돌고 → 둘 사이 마찰 → (B) This friction = 그 마찰이 자전 속도를 늦춤 → (A) however, 달이 없다면 자전이 느려지지 않음(반대 상황)"),
 ORD(E2, ['We experience the beauty'], {'A': ['However, if there were no Moon, the tilt'], 'B': ['Suppose the Earth were', 'The hemisphere of the Earth'], 'C': ['The axis of rotation']}, 'CAB',
     "(C) 자전축은 23.5도, 달의 중력이 기울기를 안정시킴 → (A) However, 달이 없다면 기울기가 0~85도로 크게 변함 → (B) 예를 들어 60도로 기울었다고 가정하면 한쪽 반구가 훨씬 많은 에너지를 받음"),
 ORD(E2, ['Insects, such as bees'], {'A': ['If they were bigger in size'], 'B': ['Although insects can survive'], 'C': ['Therefore, with the current oxygen']}, 'BCA',
     "(B) 폐 대신 기문(spiracles) → 기문은 폐만큼 효율적이지 않음 → (C) Therefore, 지금 산소 농도로는 더 커질 수 없음 → (A) 더 크다면 몸 깊은 곳까지 산소가 닿지 못함(이유 설명)"),
]
# ── 삽입: (창 시작어, 주어진 문장 위치(창 안 1~5), 해설) ──
def INS(E, start, g, ex):
    s = find(E, start); L = E[s:s + 6]; assert len(L) == 6 and 1 <= g <= 5
    return {'lines': L, 'given': g, 'ex': '정답 ▶ %s번 자리\n단서 ▶ %s' % (C5[g - 1], ex)}
I1 = [
 INS(E1, 'Have you ever wondered', 3, "'he'와 'his thoughts' = 앞 문장의 갈릴레이. 사고 실험을 소개한 바로 뒤에 그가 생각만으로 증명한 내용이 와요."),
 INS(E1, 'The tallest man', 2, "'불가능하다, 크기 효과 때문에' 바로 뒤에 크기 효과의 설명(길이 2배 → 면적 4배, 부피 8배)이 와야 해요. 뒤 문장 These changes가 이 문장을 가리켜요."),
 INS(E1, 'With only his thoughts', 5, "'These changes' = 앞 문장의 면적·부피 변화. 창의 마지막 문장(크기 효과 설명) 바로 뒤 — 문제 제기(many problems)로 이어져요."),
 INS(E1, 'These changes can', 3, "However → 앞 문장 '몸무게는 1,000배'와 대조되는 '발바닥 면적은 100배뿐'. 뒤 문장 This means가 이 둘의 차이를 정리해요."),
 INS(E1, 'However, the area of the feet', 2, "In addition(게다가) → 발 문제(첫 번째 문제)가 끝난 뒤 두 번째 문제(열 방출)를 시작해요. 뒤 문장이 열이 무엇인지 설명해요."),
 INS(E1, 'This means that his feet', 4, "However → '열은 1,000배'와 대조되는 '피부 면적은 100배뿐' → 열이 충분히 빠져나가지 못함. 마지막 문장 This shows가 결론."),
]
I2 = [
 INS(E2, 'This is a famous line', 1, "'This is a famous line' → 줄리엣의 대사 → 그 대사의 뜻(달처럼 사랑도 변할 수 있으니 달에 맹세하지 말라)이 바로 이어져야 해요."),
 INS(E2, 'Then, what would happen', 4, "'This friction' → 앞 문장에서 마찰이 처음 나와야 해요. 뒤 문장 however는 '마찰로 자전이 느려진다'와 반대인 달이 없는 경우."),
 INS(E2, 'This friction leads', 3, "'five hours' → 앞 문장 '하루가 5시간이었다'를 This indicates로 받아 '5시간마다 해가 뜬다'로 정리해요. 뒤는 ❻ Additionally(게다가)로 새 화제."),
 INS(E2, 'We experience the beauty', 2, "However → 앞의 '달의 중력이 기울기를 안정시킨다'와 반대인 '달이 없다면 기울기가 크게 변한다'. 뒤 문장 Suppose(가정해 보라)가 그 예."),
 INS(E2, 'Undoubtedly, it is', 3, "'While more oxygen may seem beneficial(산소가 많으면 이로워 보이지만)' → 앞의 질문(산소 농도가 두 배라면?)에 대한 답의 시작이고, 끝의 'especially for insects'가 뒤 문장 Insects, such as bees로 이어져요."),
 INS(E2, 'This increase in insect size', 2, "Fortunately → '잠자리가 독수리만큼 커진다'는 무서운 이야기 다음에 '거대 곤충에 쫓길 걱정은 없다'. 뒤 문장이 그 이유(우리도 더 빨리 달릴 수 있음)."),
 INS(E2, 'Dragonflies, for example', 4, "'This leads us to expect' → 앞 문장 '산소가 에너지를 더 효율적으로 쓰게 해 운동 능력이 좋아진다'의 결과로 '올림픽 신기록'을 기대. 마지막 문장은 글 전체의 정리."),
]
# ── 어휘 상: 다의어 (발문, [정답, 오답4], 해설) ──
def VM(sent, word, opts, ex): return {'q': '밑줄 친 <b>%s</b>의 문맥상 의미로 가장 알맞은 것은?' % word + P(sent), 'opts': opts, 'ex': '정답 ▶ %s\n%s' % (opts[0], ex)}
def VS(sent, word, opts, ex): return {'q': '밑줄 친 <b>%s</b>와(과) 같은 의미로 쓰인 것은?' % word + P(sent), 'opts': opts, 'ex': '정답 ▶ %s\n%s' % (opts[0], ex)}
V1 = [
 VM("When the length of an object doubles, its area increases by a <u>factor</u> of four (2x2), and its volume by a <u>factor</u> of eight (2x2x2).", 'factor',
    ['배(곱하는 수)', '요인, 원인', '공장', '대리인', '사실'], "by a factor of four = 4배로. factor는 보통 '요인'이지만 수학에서는 '곱하는 수(인수), 배'\n③ 공장은 factory"),
 VM("He demonstrated that objects with different <u>masses</u> should fall at the same speed.", 'masses',
    ['질량', '대중, 민중', '미사(성당 예배)', '대량의', '군중의 무리'], "물리 이야기(떨어지는 속도) → mass = 질량\nthe masses(대중), Mass(미사)도 같은 철자"),
 VM("With only his thoughts, he <u>demonstrated</u> that objects with different masses should fall at the same speed.", 'demonstrated',
    ['증명했다(입증했다)', '시위했다', '시연 판매했다', '연습했다', '반대했다'], "생각만으로 '증명했다' → demonstrate = 증명하다, 보여 주다\n'시위하다'(demonstration 시위)도 같은 단어"),
 VM("Unfortunately, the answer to this hypothetical question is that it is impossible due to the <u>scale</u> effect.", 'scale',
    ['규모, 크기(의 비율)', '저울', '(물고기의) 비늘', '음계', '기어오르다'], "scale effect = 크기 효과(크기가 커질 때 생기는 효과) → 규모·크기\n저울·비늘·음계·기어오르다도 모두 scale"),
 VM("One <u>issue</u> is that the giant would not be able to stand properly on his own.", 'issue',
    ['문제(점)', '(잡지의) 호', '발행하다', '쟁점 토론회', '결과로 나오다'], "One issue is that ~ = 한 가지 문제는 ~이다\nthe latest issue(최신호), issue a passport(여권을 발급하다)"),
 VM("However, the area of the feet <u>supporting</u> his body would only increase by a factor of 100.", 'supporting',
    ['(무게를) 지탱하는', '응원하는', '(가족을) 부양하는', '(의견을) 지지하는', '후원하는'], "발이 몸을 '떠받치는' → 물리적으로 지탱하다\nsupport a family(부양), support a team(응원), support an idea(지지)"),
 VM("Heat is generated in the human body, and it is constantly <u>released</u> from the surface of the skin.", 'released',
    ['방출되는', '(영화가) 개봉되는', '석방되는', '(음반이) 발매되는', '해고되는'], "열이 피부로 '빠져나가는' → 방출되다\nThe movie was released(개봉), The prisoner was released(석방)"),
 VM("This shows that while we may wish to grow as tall as a giant, we would not be able to survive in that <u>form</u>.", 'form',
    ['형태, 모습', '서식, 양식', '학년', '형성하다', '(운동선수의) 컨디션'], "in that form = 그런 모습(거인의 몸)으로\nfill out a form(서식), in good form(컨디션이 좋은)"),
 VS("One issue is that the giant would not be able to <u>stand</u> properly on his own.", 'stand',
    ['Please stand still while I take your picture.', "I can't stand the noise anymore.", 'What does this letter stand for?', 'She took a stand against bullying.', 'He set up a lemonade stand.'],
    "본문 stand = (똑바로) 서다 → ① 가만히 서 있어\n② 참다 ③ stand for = 나타내다 ④ 입장 ⑤ 가판대"),
 VS("His feet would be under too much <u>pressure</u> to support the increased weight.", 'pressure',
    ['The pressure of the water broke the glass.', 'Students feel a lot of pressure before exams.', "Don't give in to peer pressure.", 'The company put pressure on him to quit.', 'She works well under pressure.'],
    "본문 pressure = (무게가 누르는) 물리적 압력 → ① 물의 압력\n②~⑤ 마음의 압박감·사회적 압력"),
]
V2 = [
 VM("This is a famous <u>line</u> from <i>Romeo and Juliet</i>.", 'line', ['(시·극의) 구절, 대사', '선', '(기다리는) 줄', '(교통) 노선', '직업 분야'], "로미오와 줄리엣의 유명한 '대사' → line = 구절, 대사\nstand in line(줄 서다), line of work(직업 분야)"),
 VM("\"O, <u>swear</u> not by the moon, the inconstant moon.\"", 'swear', ['맹세하다', '욕하다', '땀 흘리다', '바꾸다', '숨기다'], "다음 문장 not to swear his love by the Moon(달에 사랑을 맹세하지 말라) → 맹세하다\n'욕하다'(swear at ~)도 같은 단어, '땀 흘리다'는 sweat"),
 VM("Although its appearance changes, the Moon is always <u>present</u> in the night sky.", 'present', ['존재하는, 있는', '현재의', '선물', '제출하다, 발표하다', '증정하다'], "밤하늘에 항상 '있다' → present = 존재하는\nthe present(현재), a present(선물), present a report(발표하다)"),
 VM("This friction leads to a decrease in the rotation <u>rate</u> of the planet.", 'rate', ['속도', '요금', '등급', '평가하다', '순위를 매기다'], "자전(rotation)이 느려짐 → rotation rate = 자전 속도\nroom rate(숙박 요금), first-rate(일류의), rate a movie(평가하다)"),
 VM("The hemisphere of the Earth <u>facing</u> the Sun would receive much more energy from the sun.", 'facing', ['(~을) 향하고 있는', '얼굴을 붉히는', '(어려움에) 직면한', '(시계의) 문자판의', '체면을 지키는'], "태양 '쪽을 향한' 반구 → face = ~을 향하다\nface a problem(직면하다), lose face(체면을 잃다)"),
 VM("It is also necessary to burn <u>common</u> fuels like wood and oil to generate heat and light.", 'common', ['흔한, 보통의', '공통의', '공공의', '평민의', '공동으로 소유한'], "나무·기름 같은 '흔한' 연료 → common = 흔한\nhave something in common(공통점이 있다), common good(공익)"),
 VM("3. What if the oxygen <u>concentration</u> in the atmosphere doubled?", 'concentration', ['농도', '집중(력)', '집결', '전념', '응시'], "대기 중 산소의 '농도' → concentration\n'집중력'(lose concentration)이 더 익숙한 뜻"),
 VM("If the concentration of oxygen were to double, insects could grow in size as oxygen would be more <u>readily</u> available.", 'readily', ['쉽게, 손쉽게', '기꺼이', '마지못해', '완전히', '드물게'], "산소를 '더 쉽게' 얻을 수 있으니 → readily = 쉽게\nShe readily agreed(기꺼이 동의했다)의 '기꺼이'도 같은 단어"),
 VM("Considering that oxygen is used to <u>break down</u> energy so that muscles can use it, the increase in oxygen would help to use energy more efficiently.", 'break down', ['분해하다', '고장 나다', '울음을 터뜨리다', '(문을) 부수다', '(협상이) 결렬되다'], "근육이 쓸 수 있도록 에너지를 '분해하다'\nMy car broke down(고장 났다), She broke down in tears(울음을 터뜨렸다)"),
 VS("This leads us to expect that athletes would <u>set</u> new world records at the Olympics.", 'set',
    ['She set a new school record in the 100m race.', 'The sun sets in the west.', 'Please set the table for dinner.', 'I bought a set of colored pencils.', 'The movie is set in Paris.'],
    "본문 set a record = 기록을 세우다 → ① 학교 신기록을 세웠다\n② (해가) 지다 ③ (식탁을) 차리다 ④ 세트 ⑤ (배경을) 설정하다"),
]
# ── 본문 문법 ──
def GU(no, txt, w, fix, ex): return {'q': '다음 글(본문 %s)의 밑줄 친 ①~⑤ 중 어법상 <u>틀린</u> 것은?' % no + P(txt), 'opts': C5, 'keep': True, 'a': w - 1, 'ex': '정답 ▶ %s (%s)\n%s' % (C5[w - 1], fix, ex), '_fix': (txt, w, fix)}
def GB(no, txt, opts, ex): return {'q': '다음 글(본문 %s)의 (A), (B), (C)에서 어법에 맞는 것끼리 짝지은 것은?' % no + P(re.sub(r'\(([ABC])\)\[([^\]]+)\]', r'(\1) [ \2 ]', txt)), 'opts': opts, 'ex': '정답 ▶ %s\n%s' % (opts[0], ex), '_box': txt}
def G(q, opts, ex, keep=None):
    d = {'q': q, 'opts': opts, 'ex': ex}
    if keep is not None: d.update({'keep': True, 'a': keep})
    return d
G1 = [
 GU('❶', "Have you ever wondered, \"What if I could run %s fast that nobody could see me?\" The Italian scientist Galileo Galilei is famous for a thought experiment, %s is an imaginary experiment %s to explore a mathematical or scientific hypothesis. With only his thoughts, he demonstrated %s objects with different masses should fall at the same speed when %s from the same height." % (U(1, 'so'), U(2, 'which'), U(3, 'designing'), U(4, 'that'), U(5, 'dropped')),
    3, 'designed', "③ 실험이 '고안된' 수동 → designed\n① so ~ that(너무 ~해서 …하다) ② 계속적 용법 관계대명사 ④ 목적어절 접속사 ⑤ when (they are) dropped — 물체가 '떨어뜨려지는' 수동"),
 GU('❷❸', "When the length of an object doubles, its area increases by a factor of four, and its volume %s a factor of eight. These changes can create many problems that %s the giant's life in danger. One issue is %s the giant would not be able to stand properly on his own because of the weight %s down on his feet. If a person's height increased ten times, his weight %s by a factor of 1,000." % (U(1, 'by'), U(2, 'would put'), U(3, 'that'), U(4, 'pushed'), U(5, 'would increase')),
    4, 'pushing', "④ 몸무게가 발을 '누르는' 능동 → pushing\n① (increases) by — 반복되는 동사 생략 ③ 보어절 접속사 that ⑤ 가정법 과거(If + 과거, would + 동사원형)"),
 GU('❹', "Heat is generated in the human body, and it is constantly released from the surface of the skin %s heat from %s in the body. If a person's height %s to increase ten times, the amount of heat %s would increase a thousand times. This shows that while we may wish to grow as tall as a giant, we would not be able %s in that form." % (U(1, 'to prevent'), U(2, 'accumulate'), U(3, 'were'), U(4, 'generated'), U(5, 'to survive')),
    2, 'accumulating', "② prevent A from -ing(A가 ~하지 못하게 막다) → accumulating\n① 목적의 to부정사 ③ 가정법 were to ④ '발생되는' 열 → 과거분사 ⑤ be able to + 동사원형"),
 GB('❸', "If a person's height increased ten times, his weight (A)[would / will] increase by a factor of 1,000 because weight changes in proportion to volume. However, the area of the feet (B)[supporting / supported] his body would only increase by a factor of 100. This means that his feet would be under too much pressure to support the increased weight because the mass would have increased (C)[far / very] more than the area of his feet.",
    ['would – supporting – far', 'will – supporting – far', 'would – supported – far', 'would – supporting – very', 'will – supported – very'],
    "(A) 가정법 과거: If + 과거(increased), would + 동사원형 (B) 발바닥이 몸을 '지탱하는' 능동 → supporting (C) 비교급 강조 far(much, even, still, a lot) — very ✘"),
 GB('❶❷', "If you have asked this kind of question, you may be ready (A)[to become / becoming] the next Galileo. He demonstrated that objects with different masses should fall at the same speed when dropped from the same height in the (B)[absence / absent] of air resistance. Have you ever wondered what would happen if humans (C)[could / can] grow to enormous sizes like the giant in <i>Jack and the Beanstalk</i>?",
    ['to become – absence – could', 'becoming – absence – could', 'to become – absent – could', 'to become – absence – can', 'becoming – absent – can'],
    "(A) be ready to + 동사원형 (B) 정관사 the 뒤 + of 앞 → 명사 absence (C) what would happen if ~ → 가정법 과거 could"),
 G('밑줄 친 which와 용법이 같은 것은?' + P("The Italian scientist Galileo Galilei is famous for a thought experiment, <u>which</u> is an imaginary experiment designed to explore a mathematical or scientific hypothesis."),
   ['I visited Jeju, which is famous for its beautiful beaches.', 'Which do you like better, tea or coffee?', "I don't know which way to go.", 'This is the house which my father built.', 'Tell me which one is yours.'],
   "정답 ▶ I visited Jeju, which ~\n본문 which = 콤마 뒤 계속적 용법 관계대명사(그런데 그것은) → ①\n②③⑤ 의문사(어느 것, 어느) ④ 콤마 없는 제한적 용법"),
 G('다음 문장과 의미가 같은 것은?' + P("If a person's height increased ten times, his weight would increase by a factor of 1,000."),
   ["As a person's height does not increase ten times, his weight does not increase by a factor of 1,000.", "As a person's height increased ten times, his weight increased by a factor of 1,000.",
    "As a person's height does not increase ten times, his weight increases by a factor of 1,000.", "As a person's height did not increase ten times, his weight did not increase by a factor of 1,000.",
    "Though a person's height increases ten times, his weight does not increase by a factor of 1,000."],
   "정답 ▶ As ~ does not increase, ~ does not increase\n가정법 과거 = 현재 사실의 반대 → 직설법 현재 부정(As + 현재 부정, 현재 부정)\n④ 과거 사실의 반대는 가정법 과거완료일 때"),
 G('다음 우리말을 영어로 옮길 때 가장 알맞은 것은?<br>그의 발은 너무 많은 압력을 받아서 늘어난 몸무게를 지탱할 수 없을 것이다.',
   ['His feet would be under too much pressure to support the increased weight.', 'His feet would be under too much pressure supporting the increased weight.', 'His feet would be under so much pressure to support the increased weight.',
    'His feet would be under too much pressure to supporting the increased weight.', 'His feet would be under too many pressure to support the increased weight.'],
   "정답 ▶ too much pressure to support\ntoo ~ to …(너무 ~해서 …할 수 없다) ② to 빠짐 ③ so ~ to ✘ (so ~ that) ④ to + 동사원형 ⑤ pressure는 셀 수 없음 → much"),
 G('다음 중 어법상 옳은 문장의 <b>개수</b>는?' + P('ⓐ Galileo is famous for a thought experiment.', 'ⓑ Anyone can become a great scientist with a hypothesis basing on creativity.', 'ⓒ The tallest man in recorded history was 272 cm tall.',
    'ⓓ Weight changes in proportion of volume.', 'ⓔ Not enough heat would be released from the body through the skin.'), CNT,
   "정답 ▶ 3개\n옳은 것 ⓐⓒⓔ / ⓑ 가설이 창의력에 '바탕을 둔' → based on ⓓ in proportion to(~에 비례하여)", keep=2),
 G('밑줄 친 while과 의미가 같은 것은?' + P("This shows that <u>while</u> we may wish to grow as tall as a giant, we would not be able to survive in that form."),
   ['While I like coffee, my sister prefers tea.', 'I listened to music while I was cooking.', "Don't text while driving.", 'She fell asleep while watching TV.', 'Wait here for a while.'],
   "정답 ▶ While I like coffee ~\n본문 while = ~이지만(양보·대조) → ①\n②③④ ~하는 동안 ⑤ 잠시(명사)"),
]
G2 = [
 GU('❺', "Juliet warns Romeo %s his love by the Moon as it may change just as the Moon changes %s shape. Although its appearance changes, the Moon is always present in the night sky and %s a crucial role in %s the length of the day on Earth as well as the Earth's seasons and weather patterns. Then, what would happen if there %s no Moon?" % (U(1, 'not to swear'), U(2, 'its'), U(3, 'plays'), U(4, 'regulate'), U(5, 'were')),
    4, 'regulating', "④ 전치사 in 뒤 → 동명사 regulating\n① warn + 목적어 + not to부정사 ② 달의(its) ③ is와 and로 병렬, 주어 the Moon → plays ⑤ 가정법 과거 were"),
 GU('❺', "Since the ocean is moving and the Earth is also spinning, friction %s between them. This friction leads to a decrease %s the rotation rate of the planet. Without the Moon, however, the Earth's rotation would not slow down, %s in a change in the length of a day. According to some scientists, when the Earth first %s, there was no Moon and a day was only five hours long. This indicates that without the Moon, we would see the Sun %s every five hours." % (U(1, 'occurs'), U(2, 'in'), U(3, 'resulted'), U(4, 'formed'), U(5, 'rise')),
    3, 'resulting', "③ 결과를 나타내는 분사구문 → resulting in(그 결과 ~하다)\n① friction(단수) + occurs ② a decrease in ~(~의 감소) ④ 자동사 form(형성되다) ⑤ 지각동사 see + 목적어 + 동사원형"),
 GU('❻', "We experience the beauty of different seasons because the Earth %s on its axis. The Moon's gravity holds the Earth in place by %s the tilt. Suppose the Earth %s tilted at an angle of 60 degrees. The hemisphere of the Earth %s the Sun would receive much more energy from the sun than the other hemisphere. If this trend continued, the Earth %s uninhabitable." % (U(1, 'is tilted'), U(2, 'stabilize'), U(3, 'were'), U(4, 'facing'), U(5, 'would become')),
    2, 'stabilizing', "② 전치사 by 뒤 → 동명사 stabilizing(안정시킴으로써)\n① '기울어져 있다' 수동 ③ Suppose + 가정법 과거 were ④ 태양을 '향한' 능동 ⑤ 가정법 과거 would + 동사원형"),
 GB('❼', "Oxygen is a vital gas for life, (A)[making / made] up 21 percent of the Earth's atmosphere. It is essential for breathing and is also necessary (B)[to burn / burning] common fuels like wood and oil to generate heat and light. Insects, such as bees and dragonflies, do not have lungs and instead take in air through external openings (C)[called / calling] spiracles.",
    ['making – to burn – called', 'made – to burn – called', 'making – burning – called', 'making – to burn – calling', 'made – burning – calling'],
    "(A) 산소가 대기의 21%를 '차지하는' 능동 분사구문 → making up (B) It is necessary to + 동사원형 (C) '기문이라고 불리는' 수동 → called"),
 GB('❽', "If they were bigger in size, oxygen (A)[would not / will not] be able to reach the deepest parts of their bodies. Dragonflies, for example, may become as large as eagles, (B)[altering / altered] the balance of predators and prey in the ecosystem. Fortunately, you wouldn't need to worry about giant insects (C)[chasing / to chase] after you if this were to occur.",
    ['would not – altering – chasing', 'will not – altering – chasing', 'would not – altered – chasing', 'would not – altering – to chase', 'will not – altered – to chase'],
    "(A) 가정법 과거(If + were, would) (B) 균형을 '바꾸는' 능동 분사구문 (C) 전치사 about + (의미상 주어 giant insects) + 동명사 chasing"),
 G('밑줄 친 so that과 쓰임이 같은 것은?' + P("Considering that oxygen is used to break down energy <u>so that</u> muscles can use it, the increase in oxygen would help to use energy more efficiently."),
   ['Speak louder so that everyone can hear you.', 'It was so cold that we stayed home.', 'She studied hard, so she passed the test.', 'I think so.', 'So, what do you want to do?'],
   "정답 ▶ Speak louder so that ~\n본문 so that + 주어 + can = ~할 수 있도록(목적) → ①\n② so ~ that(너무 ~해서) ③ 그래서 ④ 그렇게 ⑤ 그러면(말 꺼내기)"),
 G('다음 문장과 의미가 같은 것은?' + P("If there were no Moon, the tilt could vary wildly between 0 and 85 degrees."),
   ['Without the Moon, the tilt could vary wildly between 0 and 85 degrees.', 'With the Moon, the tilt could vary wildly between 0 and 85 degrees.', 'As there is no Moon, the tilt varies wildly between 0 and 85 degrees.',
    'Without the Moon, the tilt could not vary wildly between 0 and 85 degrees.', 'If it had not been for the Moon, the tilt could have varied wildly between 0 and 85 degrees.'],
   "정답 ▶ Without the Moon, ~ could vary\nIf there were no ~ = Without ~ = But for ~ (가정법 과거)\n③ 실제로는 달이 있으니 직설법으로는 As there is a Moon, the tilt does not vary ⑤ 과거 사실의 반대(가정법 과거완료)"),
 G('다음 문장과 의미가 같은 것은?' + P("Although insects can survive without lungs, their spiracles are not as efficient as lungs at taking in air."),
   ['Lungs are more efficient than their spiracles at taking in air.', 'Their spiracles are more efficient than lungs at taking in air.', 'Lungs are not as efficient as their spiracles at taking in air.',
    'Their spiracles are as efficient as lungs at taking in air.', 'Lungs are less efficient than their spiracles at taking in air.'],
   "정답 ▶ Lungs are more efficient than ~\nA is not as ~ as B (A는 B만큼 ~하지 않다) = B is more ~ than A"),
 G('다음 중 어법상 옳은 문장의 <b>개수</b>는?' + P('ⓐ Oxygen is essential for breathing.', 'ⓑ Would it be better to have a higher concentration of oxygen in the atmosphere?', 'ⓒ Insects cannot evolve being larger than their current size.',
    'ⓓ Dragonflies may become as larger as eagles.', 'ⓔ This leads us expect that athletes would set new world records.'), CNT,
   "정답 ▶ 2개\n옳은 것 ⓐⓑ / ⓒ evolve to be ⓓ as large as(원급) ⓔ lead + 목적어 + to부정사 → to expect", keep=1),
 G('다음 우리말을 영어로 옮길 때 가장 알맞은 것은?<br>그것들은 단지 상상에 근거한 것이고 과학적 연구를 통해 검증되지 않았다는 것을 고려하는 것이 중요하다.',
   ['It is important to consider that they are simply based on imagination and have not been tested through scientific research.', 'It is important to consider that they are simply basing on imagination and have not tested through scientific research.',
    'It is important to consider that they simply based on imagination and have not been tested through scientific research.', 'It is important to consider that they are simply based on imagination and has not been tested through scientific research.',
    'It is important considering that they are simply based on imagination and have not been testing through scientific research.'],
   "정답 ▶ It is important to consider that ~ are based on ~ have not been tested\n'근거하다' be based on / '검증되지 않았다' 현재완료 수동 have not been tested(주어 they → have)"),
]
# ── 확인: 문법 고친 본문·네모 정답 본문을 원문과 대조 ──
MISS = []
def chk(t):
    t = re.sub(r'<[^>]+>', '', t).replace('&nbsp;', ' ').strip().rstrip('.?!"').strip()
    if t and t not in SRC: MISS.append(t)
def sents(x): return [y for y in re.split(r'(?<=[.?!"])\s+', x) if y]
for g in G1 + G2:
    if '_fix' in g:
        txt, w, fix = g.pop('_fix'); k = [0]
        def rp(m):
            k[0] += 1; return fix if k[0] == w else m.group(1)
        for s in sents(re.sub(r'[①②③④⑤]<u>(.*?)</u>', rp, txt)): chk(s)
    if '_box' in g:
        for s in sents(re.sub(r'\(([ABC])\)\[([^/\]]+?) / [^\]]+\]', lambda m: m.group(2), g.pop('_box'))): chk(s)
for q in V1 + V2:
    assert len(q['opts']) == 5 and len(set(q['opts'])) == 5
    chk(re.search(r'<p>(.*?)</p>', q['q']).group(1))
for x in O1 + O2 + G1 + G2: assert len(x['opts']) == 5 and len(set(x['opts'])) == 5, x['q'][:40]
def DAY(i, rng, story, src_days, O, I, V, Gm):
    pas = [l for sd in src_days for l in D[sd]['passage']]
    return {'id': 'hs%d' % i, 'name': '', 'range': rng, 'story': story, 'passage': pas, 'steps': [
        {'type': 'mc', 'title': '① 순서 배열 고난도 (%d)' % len(O), 'guide': '주어진 글 다음에 이어질 (A), (B), (C)의 순서를 고르세요. 대명사·연결어·앞뒤 내용이 단서예요.', 'items': O},
        {'type': 'insert', 'title': '② 문장 삽입 고난도 (%d)' % len(I), 'guide': '주어진 문장이 들어가기에 가장 알맞은 곳을 고르세요. 빈칸 5곳 중 답은 한 곳뿐이에요.', 'items': I},
        {'type': 'mc', 'title': '③ 어휘 상 — 이런 뜻도 있었어? (%d)' % len(V), 'guide': '익숙한 단어가 본문에서는 다른 뜻으로 쓰였어요. 문맥에 맞는 뜻을 고르세요.', 'items': V},
        {'type': 'mc', 'title': '④ 본문 문법 (%d)' % len(Gm), 'guide': '본문 문장으로 만든 문법 문제예요. 밑줄·네모·같은 쓰임·바꿔 쓰기·개수·영작.', 'items': Gm}]}
NEW = [DAY(1, '고난도 세트 1 · 본문 ❶~❹ (순서·삽입·어휘 상·문법)', '거인이 될 수 있을까? — 순서 3 · 삽입 6 · 다의어 10 · 문법 10', ['d1'], O1, I1, V1, G1),
       DAY(2, '고난도 세트 2 · 본문 ❺~❽ (순서·삽입·어휘 상·문법)', '달이 없다면? 산소가 두 배라면? — 순서 3 · 삽입 7 · 다의어 10 · 문법 10', ['d2', 'd3'], O2, I2, V2, G2)]
src = open(path, encoding='utf-8').read()
cut = re.search(r'\n/\* [A-Z0-9]+-TESTS', src).start() + 1
head, tail = src[:cut], src[cut:]
PK2 = json.loads(subprocess.check_output(['node', '-e', "global.window={};eval(require('fs').readFileSync(0,'utf8'));process.stdout.write(JSON.stringify(window.PKG))"], input=head.encode()))
head = head[:head.index('window.PKG')]
PK2['days'] = [d for d in PK2['days'] if d['id'] not in ('hs1', 'hs2')] + NEW
for i, d in enumerate(PK2['days']): d['name'] = 'DAY %d' % (i + 1)
if 'mirae4h' not in head: head = head.rstrip('\n') + '\n/* 11/28: 고난도 세트 DAY hs1·hs2 (gen/mirae4h/gen.py) */\n'
write(PK2, path, head)
open(path, 'a', encoding='utf-8').write(tail)
print('원문과 다른(줄인) 문장:', *MISS, sep='\n  ')
print([(d['name'], [len(s['items']) for s in d['steps']]) for d in NEW])
