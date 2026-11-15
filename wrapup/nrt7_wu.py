# 11/15 너른터 7과 변형기출 1~4세트 (중3 지학사 민찬규 Lesson 7 If I Lived There)
# 원본: 선생님이 다른 곳에서 만든 100문항 hwpx(work/nrt7). 검수해서 오류 고치고 객관식 80문항(20 × 4)으로 정리.
# 1세트 도입·푸에블로 / 2세트 베니스 / 3세트 토루 / 4세트 문법·서술형을 객관식으로 바꾼 문항
# 원본 번호는 각 문항 주석 [원Q번호]. 고친 점은 해설 끝 '수정 ▶'에 적음.
from wu_nrt7 import *
H = ('너른터 7과 변형기출', '중3 영어 지학사(민찬규) Lesson 7 If I Lived There', '너른터 7과 변형기출', 'nrt7')
B = lambda *ls: BOX('<br>'.join(ls))
R, G = '본문', '문법'
INTRO = ("Different people live in different houses. Some use ladders to enter their houses. Others live in houses on the water. And others share their houses with many people. "
         "Imagine you live in one of these houses. How would that change your life?")
PUE = ("If I lived in a pueblo, I would climb up a ladder to enter my house. There's a hidden opening on top of the house. If unwelcome visitors appeared, I would pull the ladder up to stop them from entering. "
       "The thick walls are made of earth, straw, and water. They would keep me cool in summer and warm in winter. The house has a flat roof. I would sometimes sleep up on the roof under the moon and stars.")
VEN = ("If I lived in Venice, I would take a gondola to school every morning. Venice has 118 small islands. On weekends, I would travel from island to island by a vaporetto, a water bus. "
       "At high tide, the water from the Adriatic Sea often rises and leaves the streets full of water. However, I would be able to walk around the town through the raised walkways.")
VEN2 = ("Venice is known as the \"floating city.\" In Venice, there are many colorful houses on the water. You may wonder how and why they built the houses on the water. "
        "The old Venetians decided to live there to keep themselves safe from invaders. But it was not easy for them to build their homes on this swampy surface. "
        "So they installed more than 10 million wooden poles in the ground. It is these wooden poles that support Venice to this day.")
TUL = ("If I lived in a tulou, a huge round house in Fujian, China, I would always have friends at home to play with. I would sometimes hear my neighbor calling me to come over for tea or dinner. "
       "In a tulou, there are usually three to five floors. The first floor is used for cooking and eating. And people store food and tools on the second floor. "
       "Do you wonder where I would sleep? My bedroom would be on the third or fourth floor.")
TUL2 = ("A tulou is like a village. The people living in a tulou mostly have the same family name. Some large tulou can house up to 50 families. "
        "They work together and share many things. Living together in one building keeps them safe. Homes are everywhere. But they are different all over the world. What is your home like?")
NOTICE = '너른터 7과 변형기출을 검수해서 정답 오류·문항 오류를 고치고, 서술형 일부는 객관식으로 바꿨어요. 답은 아래 OMR에 입력하세요.'

# ═══════════════ 1세트 · 도입 · 푸에블로 ═══════════════
T = Test('1', '1세트', '본문 ① 도입 · 푸에블로', '7과 본문 1~2', NOTICE, H=H)
# [원Q1]
T.fixed('다음 글의 밑줄 친 ①~⑤ 중 어법상 <u>틀린</u> 것은?', R, B(
 'Different people live in different ' + CN(1, 'houses') + '. Some use ladders ' + CN(2, 'to enter into') + ' their houses. Others live in houses on the water. And ' + CN(3, 'others') +
 ' share their houses with many people. Imagine you ' + CN(4, 'live') + ' in one of these houses. How would that ' + CN(5, 'change') + ' your life?'),
 ['houses', 'to enter into', 'others', 'live', 'change'], 2,
 "이유 ▶ enter(~에 들어가다)는 전치사 없이 바로 목적어를 쓰는 타동사 → to enter their houses.\n오답 ▶ ① different + 복수명사 ✔ ③ Some ~ Others ~ others(어떤 사람들은 ~ 또 다른 사람들은) ✔ ④ Imagine (that) 주어 + 동사 ✔ ⑤ 조동사 would + 동사원형 ✔\n포인트 ▶ enter into ❌ → enter ✔ (discuss about ❌, reach to ❌도 같은 함정)", [('enter', '~에 들어가다'), ('ladder', '사다리')])
# [원Q2]
T.fixed('다음 글의 밑줄 친 ①~⑤ 중 어법상 <u>틀린</u> 것은?', R, B(
 'Different people live in different houses. Some use ladders ' + CN(1, 'to enter') + ' their houses. ' + CN(2, 'Others') + ' live in houses on the water. ' + CN(3, 'And others') +
 ' share their houses with many people. Imagine you live in ' + CN(4, 'one') + ' of these houses. How would that ' + CN(5, 'changes') + ' your life?'),
 ['to enter', 'Others', 'And others', 'one', 'changes'], 5,
 "이유 ▶ 조동사 would 뒤에는 동사원형 → change.\n오답 ▶ ① 목적(~하기 위해) to부정사 ✔ ②·③ 또 다른 사람들 ✔ ④ one of + 복수명사 ✔\n포인트 ▶ 조동사(will, would, can, could) + 동사원형", [])
# [원Q4]
T.fixed('다음 글의 밑줄 친 문장 ①~⑤ 중 어법상 가장 어색한 것은?', R, B(
 CN(1, 'Different people live in different houses') + '. ' + CN(2, 'Some use ladders to enter their houses') + '. ' + CN(3, 'Others live in houses on the water') + '. ' +
 CN(4, 'And others share their houses with many people') + '. ' + CN(5, 'Imagine you live in one of these house') + '. How would that change your life?'), None, 5,
 "이유 ▶ one of these + 복수명사 → these houses.\n오답 ▶ ①~④ 모두 본문 그대로 ✔\n포인트 ▶ one of + the/these + 복수명사(단수 취급)", [])
# [원Q5]
T.flex('다음 글의 밑줄 친 <u>to enter</u>와 용법이 같은 것은?', R, B('Different people live in different houses. Some use ladders <u>to enter</u> their houses. Others live in houses on the water.'),
 ['He left early to avoid the traffic jam.', 'My hobby is to collect old furniture.', 'They expected to have dinner with me this week.', 'She has nothing to worry about.', 'It is hard to learn a new language.'],
 "이유 ▶ to enter = 들어가기 위해(목적, 부사적 용법). to avoid = 교통 체증을 피하기 위해(목적).\n오답 ▶ {1} 보어(~하는 것) – 명사적 {2} expect의 목적어 – 명사적 {3} nothing을 꾸밈 – 형용사적 {4} 진주어 – 명사적\n포인트 ▶ '~하기 위해'로 해석되면 부사적 용법(목적)\n수정 ▶ 원본 ③ advised him to play(목적격 보어)를 가주어 문장으로 바꿈, traffic jam 앞에 the 추가", [('avoid', '피하다'), ('traffic jam', '교통 체증')])
# [원Q9]
T.flex('주어진 문장 다음에 이어질 글의 순서로 가장 적절한 것은?', R, B('Different people live in different houses.') + '\n' + BOX('<b>(A)</b> How would that change your life?<br><b>(B)</b> Imagine you live in one of these houses.<br><b>(C)</b> Some use ladders to enter their houses.<br><b>(D)</b> Others live in houses on the water.<br><b>(E)</b> And others share their houses with many people.'),
 ['(C) − (D) − (E) − (B) − (A)', '(C) − (E) − (B) − (D) − (A)', '(E) − (C) − (B) − (D) − (A)', '(C) − (D) − (B) − (A) − (E)', '(C) − (A) − (D) − (E) − (B)'],
 "이유 ▶ (C) Some(어떤 사람들은) → (D) Others(다른 사람들은) → (E) And others(또 다른 사람들은) → (B) 이런 집들 중 하나에 산다고 상상해 봐 → (A) 그것이 네 삶을 어떻게 바꿀까?\n포인트 ▶ Some → Others → others 순서, these houses는 앞의 세 집을 가리키므로 (B)는 (C)(D)(E) 뒤", [], en=True)
# [원Q10 서술형 → 객관식]
T.flex('다음 빈칸에 들어갈 말로, 영영풀이에 해당하는 단어는?', R, B('[영영풀이] a device used for climbing that has two long pieces of wood, metal, or rope with a series of steps between them', '', 'Different people live in different houses. Some use ' + BL + 's to enter their houses.'),
 ['ladder', 'rope', 'bridge', 'pole', 'gate'],
 "이유 ▶ 두 개의 긴 나무·금속·밧줄 사이에 일련의 발판이 있는 오르는 도구 = 사다리(ladder).\n오답 ▶ {1} 밧줄 {2} 다리 {3} 기둥 {4} 문\n수정 ▶ 원본 10번(주관식)을 객관식으로 바꿈", [('device', '도구, 장치'), ('a series of', '일련의'), ('step', '발판, 계단')])
# [원Q12]
T.flex('다음 (A), (B), (C)의 각 괄호 안에서 어법에 맞는 표현으로 가장 적절한 것은?', R, B(
 'If I (A) [lived / had lived] in a pueblo, I would climb up a ladder to enter my house. There\'s a hidden opening on top of the house. If unwelcome visitors appeared, I would pull the ladder up to stop them (B) [from / for] entering. The thick walls are made (C) [of / from] earth, straw, and water.'),
 ['lived − from − of', 'lived − for − from', 'had lived − from − of', 'had lived − from − from', 'had lived − for − of'],
 "이유 ▶ (A) 주절 would climb → 가정법 과거 lived (B) stop A from -ing(A가 ~하지 못하게 하다) (C) 재료의 성질이 그대로 보이면(물리적 변화) be made of\n오답 ▶ had lived는 가정법 과거완료(주절이 would have p.p.일 때) / stop A for ❌ / be made from은 화학적 변화(포도 → 와인)\n포인트 ▶ If + 과거형, would + 동사원형", [('unwelcome', '반갑지 않은'), ('straw', '지푸라기, 짚')])
# [원Q13]
T.flex('다음 글의 주제로 가장 적절한 것은?', R, B(INTRO, PUE),
 ['Different types of houses and one in a pueblo', 'Working safely in people\'s homes', 'Health and safety in care homes', 'How to build stairs instead of a ladder', 'Why people dislike unwelcome visitors'],
 "이유 ▶ 앞부분: 세계의 다양한 집 소개 → 뒷부분: 푸에블로 집에 산다면(사다리, 숨겨진 출입구, 두꺼운 벽, 평평한 지붕).\n오답 ▶ {1}·{2} 무관 {3} 사다리 대신 계단 – 언급 없음 {4} 일부 내용일 뿐\n수정 ▶ 원본 ③ 'Pueblo houses and roles of a ladder'는 정답과 너무 가까워 다른 오답으로 바꿈", [('dislike', '싫어하다')])
# [원Q14]
T.flex('다음 글의 제목으로 가장 적절한 것은?', R, B(INTRO, PUE),
 ['Types of Homes around the World: A Ladder House in a Pueblo', 'Why Do People Live in Different Types of Houses?', 'Everyone Needs a Place to Live in', 'Why Does Where You Live Mean So Much?', 'The Most Popular Type of Home in the World'],
 "이유 ▶ 세계의 다양한 집 → 푸에블로의 사다리 집을 상상.\n오답 ▶ {1} 다양한 집에 사는 '이유'는 다루지 않음 {2}·{3} 너무 일반적 {4} 가장 인기 있는 집 – 언급 없음", [])
# [원Q15]
T.flex('다음 글의 내용과 일치하지 <u>않는</u> 것은?', R, B(INTRO, PUE),
 ['반갑지 않은 방문객이 쉽게 들어오도록 사다리를 이용한다.', '사람들은 다양한 형태의 집에서 산다.', '푸에블로에서는 사다리로 집에 들어간다.', '집의 두꺼운 벽은 흙, 지푸라기, 물로 만들어져 있다.', '지붕은 평평해서 그 위에서 잠을 잘 수도 있다.'],
 "이유 ▶ 반갑지 않은 방문객이 나타나면 사다리를 끌어올려 '못 들어오게' 막는다(stop them from entering).\n오답 ▶ {1} Different people live in different houses ✔ {2} climb up a ladder to enter ✔ {3} made of earth, straw, and water ✔ {4} a flat roof, sleep up on the roof ✔\n수정 ▶ 원본 선택지의 맞춤법(낮선, 흑벽)을 다듬음", [])
# [원Q17]
T.fixed('다음 글의 밑줄 친 부분 중 어법상 가장 어색한 것은?', R, B(
 'Some use ladders to ' + CN(1, 'enter') + ' their houses. How would that ' + CN(2, 'change') + ' your life? If I ' + CN(3, 'lived') + ' in a pueblo, I would climb up a ladder to enter my house. There\'s a hidden opening on top of the house. If unwelcome visitors ' +
 CN(4, 'were appeared') + ', I would pull the ladder up to stop them from entering. The house has a flat roof. I would ' + CN(5, 'sometimes') + ' sleep up on the roof under the moon and stars.'),
 ['enter', 'change', 'lived', 'were appeared', 'sometimes'], 4,
 "이유 ▶ appear(나타나다)는 목적어가 없는 자동사라 수동태(be p.p.)로 쓸 수 없다 → appeared.\n오답 ▶ ① to + 동사원형 ✔ ② would + 동사원형 ✔ ③ 가정법 과거 ✔ ⑤ 빈도부사는 조동사 뒤 ✔\n포인트 ▶ 수동태가 안 되는 자동사: appear, happen, disappear, arrive", [('appear', '나타나다')])
# [원Q18]
T.fixed('다음 글의 밑줄 친 부분 중 어법상 가장 어색한 것은?', R, B(
 'And others share ' + CN(1, 'their') + ' houses with many people. If I lived in a pueblo, I would climb up a ladder with a view to ' + CN(2, 'enter') + ' my house. If unwelcome visitors appeared, I would pull the ladder up to stop them from ' +
 CN(3, 'entering') + '. They would keep me cool in summer and ' + CN(4, 'warm') + ' in winter. I would ' + CN(5, 'sometimes') + ' sleep up on the roof under the moon and stars.'),
 ['their', 'enter', 'entering', 'warm', 'sometimes'], 2,
 "이유 ▶ with a view to -ing(~하기 위해)의 to는 전치사 → 동명사 entering.\n오답 ▶ ① others의 소유격 ✔ ③ from + 동명사 ✔ ④ keep + 목적어 + 형용사, cool과 병렬 ✔ ⑤ 빈도부사 ✔\n포인트 ▶ 전치사 to + -ing: with a view to, look forward to, be used to", [('with a view to -ing', '~하기 위해, ~할 목적으로')])
# [원Q19]
T.fixed('다음 글의 밑줄 친 부분 ①~⑤ 중 어법상 가장 어색한 것은?', R, B(
 'If I lived in a pueblo, I ' + CN(1, 'would') + ' climb up a ladder to enter my house. There\'s a ' + CN(2, 'hidden') + ' opening on top of the house. The thick walls are made ' + CN(3, 'of') +
 ' earth, straw, and water. They would keep me cool in summer and ' + CN(4, 'warmly') + ' in winter. I would sometimes ' + CN(5, 'sleep') + ' up on the roof under the moon and stars.'),
 ['would', 'hidden', 'of', 'warmly', 'sleep'], 4,
 "이유 ▶ keep + 목적어 + 형용사(목적격 보어). and로 cool과 나란히 → warm.\n오답 ▶ ① 가정법 과거 주절 ✔ ② '숨겨진' 출입구(과거분사) ✔ ③ be made of ✔ ⑤ would + 동사원형 ✔\n포인트 ▶ 목적격 보어 자리에 부사 ❌", [])
# [원Q20]
T.fixed('다음 글의 밑줄 친 부분 중 문맥상 낱말의 쓰임이 적절하지 <u>않은</u> 것은?', R, B(
 'Different people live in ' + CN(1, 'different') + ' houses. And others ' + CN(2, 'share') + ' their houses with many people. If ' + CN(3, 'unwelcome') +
 ' visitors appeared, I would pull the ladder up to stop them from entering. The thick walls are made of earth, straw, and water. They would keep me ' + CN(4, 'cold') + ' in summer and warm in winter. I would sometimes ' + CN(5, 'sleep') + ' up on the roof under the moon and stars.'),
 ['different', 'share', 'unwelcome', 'cold', 'sleep'], 4,
 "이유 ▶ 두꺼운 벽이 여름에는 '시원하게', 겨울에는 따뜻하게 → cold(추운) ❌ → cool.\n오답 ▶ ① 다른 ② 공유하다 ③ 반갑지 않은 ⑤ 자다 – 모두 문맥에 맞음", [('cool', '시원한')])
# [원Q21]
T.fixed('다음 글의 밑줄 친 부분 중 문맥상 낱말의 쓰임이 적절하지 <u>않은</u> 것은?', R, B(
 'Some use ladders to ' + CN(1, 'enter') + ' their houses. Others live in houses on the water. And others ' + CN(2, 'divide') + ' their houses with many people. If I lived in a pueblo, I would ' +
 CN(3, 'climb up') + ' a ladder to enter my house. If ' + CN(4, 'unwelcome') + ' visitors appeared, I would pull the ladder up to stop them from entering. I would sometimes ' + CN(5, 'sleep') + ' up on the roof under the moon and stars.'),
 ['enter', 'divide', 'climb up', 'unwelcome', 'sleep'], 2,
 "이유 ▶ 많은 사람과 집을 '공유한다' → share. divide(나누다, 쪼개다)는 문맥에 맞지 않음.\n오답 ▶ ① 들어가다 ③ 올라가다 ④ 반갑지 않은 ⑤ 자다\n포인트 ▶ share A with B = A를 B와 함께 쓰다", [('divide', '나누다, 쪼개다')])
# [원Q22]
T.fixed('다음 글의 밑줄 친 부분 중 문맥상 낱말의 쓰임이 적절하지 <u>않은</u> 것은?', R, B(
 CN(1, 'Imagine') + ' you live in one of these houses. How would that ' + CN(2, 'change') + ' your life? If I lived in a pueblo, I would climb up a ladder to enter my house. If ' + CN(3, 'welcome') +
 ' visitors appeared, I would pull the ladder up to stop them from entering. They would keep me cool in summer and ' + CN(4, 'warm') + ' in winter. I would sometimes sleep up on the roof ' + CN(5, 'under') + ' the moon and stars.'),
 ['Imagine', 'change', 'welcome', 'warm', 'under'], 3,
 "이유 ▶ 사다리를 끌어올려 들어오지 못하게 막는 대상은 '반갑지 않은' 방문객 → unwelcome.\n오답 ▶ ① 상상하다 ② 바꾸다 ④ 따뜻한 ⑤ ~ 아래에서", [])
# [원Q23]
T.fixed('다음 글의 밑줄 친 부분 중 문맥상 낱말의 쓰임이 적절하지 <u>않은</u> 것은?', R, B(
 'Different people live in ' + CN(1, 'different') + ' houses. And others ' + CN(2, 'share') + ' their houses with many people. There\'s a ' + CN(3, 'hidden') + ' opening on top of the house. If unwelcome visitors appeared, I would pull the ladder up to ' +
 CN(4, 'stop') + ' them from entering. The house has a ' + CN(5, 'slanted') + ' roof. I would sometimes sleep up on the roof under the moon and stars.'),
 ['different', 'share', 'hidden', 'stop', 'slanted'], 5,
 "이유 ▶ 지붕 위에서 달과 별 아래 잠을 잔다 → 지붕은 '평평한(flat)'. slanted(기울어진) ❌.\n오답 ▶ ① 다른 ② 공유하다 ③ 숨겨진 ④ 막다", [('slanted', '기울어진'), ('flat', '평평한')])
# [원Q24 서술형 → 객관식]
T.flex('다음 글의 빈칸 (a), (b), (c)에 들어갈 말로 바르게 짝지어진 것은?', R, B(
 'And others share their houses <b>(a)</b> ' + BL + ' many people. If unwelcome visitors appeared, I would pull the ladder up to stop them <b>(b)</b> ' + BL + ' entering. The thick walls are made <b>(c)</b> ' + BL + ' earth, straw, and water.'),
 ['with − from − of', 'with − for − from', 'to − from − of', 'with − from − from', 'for − of − with'],
 "이유 ▶ (a) share A with B (b) stop A from -ing (c) be made of(물리적 변화)\n오답 ▶ {1}·{3} be made from은 화학적 변화 {2} share A to ❌ {4} 셋 다 틀림\n수정 ▶ 원본 24번은 빈칸 이름이 (a)(a)(c)로 잘못 적혀 있어 (a)(b)(c)로 고치고 객관식으로 바꿈", [])
# [원Q31]
T.flex('다음 글의 빈칸 (A)에 공통으로 들어갈 말로 가장 적절한 것은? (대소문자 구별 없음)', R, B(
 'Different people live in different houses. Some use ladders to enter their houses. <b>(A)</b> ' + BL + ' live in houses on the water. And <b>(A)</b> ' + BL + ' share their houses with many people.'),
 ['others', 'ones', 'other', 'another', 'the other'],
 "이유 ▶ 정해지지 않은 여러 사람 중 일부는 Some, 또 다른 일부는 Others(복수 대명사).\n오답 ▶ {1} ones는 앞의 명사를 받는 말 {2} other는 명사 앞에 쓰는 형용사 {3} another는 단수 {4} the other는 둘 중 나머지 하나\n수정 ▶ 원본 지문의 오타(peublo)와 시점이 섞인 문장을 빼고 앞부분만 제시", [])
# [원Q32]
T.flex('다음 글의 내용과 일치하는 것은?', R, B(PUE),
 ['You can enter the house through the hidden opening on top of a pueblo.', 'The thin walls would make people stay cool in summer.', 'You should climb up a chimney to sleep up on the roof.',
  'People used only one material to make the thick walls.', 'If you lived in a pueblo, you should use ropes to enter the house.'],
 "이유 ▶ 사다리를 타고 올라가 집에 들어가고, 집 꼭대기에 숨겨진 출입구가 있다 → 꼭대기 출입구로 들어간다.\n오답 ▶ {1} thick walls(두꺼운 벽) {2} 굴뚝 – 언급 없음, 사다리 {3} 흙·지푸라기·물 세 가지 {4} 밧줄이 아니라 사다리\n수정 ▶ 원본 ③의 오타 think walls → thick walls", [('chimney', '굴뚝'), ('material', '재료')])
T.render()

# ═══════════════ 2세트 · 베니스 ═══════════════
T = Test('2', '2세트', '본문 ② 베니스', '7과 본문 3', NOTICE, H=H)
# [원Q33]
T.fixed('다음 글의 밑줄 친 부분 중 어법상 가장 어색한 것은?', R, B(
 'If I ' + CN(1, 'lived') + ' in Venice, I would take a gondola to school every morning. At high tide, the water from the Adriatic Sea ' + CN(2, 'often') + ' rises and leaves the streets full of water. However, I would be able to walk around the town through the ' +
 CN(3, 'raising') + ' walkways. The old Venetians decided ' + CN(4, 'to live') + ' there to keep themselves safe from invaders. It is these wooden poles that ' + CN(5, 'support') + ' Venice to this day.'),
 ['lived', 'often', 'raising', 'to live', 'support'], 3,
 "이유 ▶ 통로는 사람이 '높인'(높여진) 것 → 수동의 과거분사 raised.\n오답 ▶ ① 가정법 과거 ✔ ② 빈도부사는 일반동사 앞 ✔ ④ decide + to부정사 ✔ ⑤ 강조되는 말 these wooden poles(복수)에 맞춘 복수 동사 ✔\n포인트 ▶ raise(올리다)는 타동사 → '올려진' = raised", [('walkway', '통로, 보도'), ('raise', '올리다')])
# [원Q34]
T.flex('다음 (A), (B), (C)의 각 괄호 안에서 어법에 맞는 표현으로 가장 적절한 것은?', R, B(
 'If I lived in Venice, I would (A) [take / have taken] a gondola to school every morning. The old Venetians decided to live there to keep (B) [themselves / them] safe from invaders. It is these wooden poles that (C) [support / supports] Venice to this day.'),
 ['take − themselves − support', 'have taken − themselves − supports', 'take − them − support', 'take − themselves − supports', 'have taken − them − support'],
 "이유 ▶ (A) 가정법 과거 → would + 동사원형 take (B) 주어(The old Venetians) = 목적어 → 재귀대명사 themselves (C) 강조 구문에서 동사는 강조된 these wooden poles(복수)에 맞춤 → support\n오답 ▶ have taken은 가정법 과거완료 / them은 다른 사람들 / supports는 단수", [])
# [원Q35]
T.fixed('다음 글의 밑줄 친 문장 ①~⑤ 중 어법상 가장 어색한 것은?', R, B(
 CN(1, 'If I lived in Venice, I would take a gondola to school every morning') + '. At high tide, ' + CN(2, 'the water from the Adriatic Sea often rise and leave the streets full of water') + '. In Venice, ' +
 CN(3, 'there are many colorful houses on the water') + '. ' + CN(4, 'The old Venetians decided to live there to keep themselves safe from invaders') + '. ' + CN(5, 'It is these wooden poles that support Venice to this day') + '.'), None, 2,
 "이유 ▶ 주어는 the water(단수, from the Adriatic Sea는 꾸밈말) → rises and leaves.\n오답 ▶ ①·③·④·⑤ 본문 그대로 ✔\n포인트 ▶ 주어 + 전치사구 + 동사: 동사는 전치사구 앞의 명사에 맞춘다", [])
# [원Q36]
T.fixed('글의 흐름으로 보아, 주어진 문장이 들어갈 위치로 가장 적절한 곳은?', R, B('The old Venetians decided to live there to keep themselves safe from invaders.') + '\n' + B(
 'Venice is known as the "floating city."' + GP(1) + 'In Venice, there are many colorful houses on the water.' + GP(2) + 'You may wonder how and why they built the houses on the water.' + GP(3) +
 'But it was not easy for them to build their homes on this swampy surface.' + GP(4) + 'So they installed more than 10 million wooden poles in the ground.' + GP(5) + 'It is these wooden poles that support Venice to this day.'), None, 3,
 "이유 ▶ '어떻게, 왜 물 위에 지었을까?' → 왜: 침략자로부터 안전하려고(주어진 문장) → But 이런 늪지에 짓기는 쉽지 않았다 → So 나무 기둥(어떻게).\n포인트 ▶ how and why 질문 다음에 why에 대한 답이 먼저", [('invader', '침략자'), ('swampy', '늪이 많은')])
# [원Q37]
T.flex('주어진 글 다음에 이어질 글의 순서로 가장 적절한 것은?', R, B(VEN) + '\n' + BOX(
 '<b>(A)</b> So they installed more than 10 million wooden poles in the ground. It is these wooden poles that support Venice to this day.<br><b>(B)</b> Venice is known as the "floating city." In Venice, there are many colorful houses on the water. You may wonder how and why they built the houses on the water.<br><b>(C)</b> The old Venetians decided to live there to keep themselves safe from invaders. But it was not easy for them to build their homes on this swampy surface.'),
 ['(B) − (C) − (A)', '(C) − (A) − (B)', '(C) − (B) − (A)', '(B) − (A) − (C)', '(A) − (C) − (B)'],
 "이유 ▶ (B) 떠 있는 도시, 어떻게·왜 지었을까? → (C) 왜: 안전 + 하지만 늪지라 쉽지 않음 → (A) So 나무 기둥 설치.\n포인트 ▶ (C)의 there, them은 (B)의 Venice, they를 받음 / (A)의 So는 (C)의 '쉽지 않았다'의 결과", [])
# [원Q38]
T.fixed('글의 흐름으로 보아, 주어진 문장이 들어갈 위치로 가장 적절한 곳은?', R, B('So they installed more than 10 million wooden poles in the ground.') + '\n' + B(
 'Venice is known as the "floating city."' + GP(1) + 'In Venice, there are many colorful houses on the water.' + GP(2) + 'You may wonder how and why they built the houses on the water.' + GP(3) +
 'The old Venetians decided to live there to keep themselves safe from invaders.' + GP(4) + 'But it was not easy for them to build their homes on this swampy surface.' + GP(5) + 'It is these wooden poles that support Venice to this day.'), None, 5,
 "이유 ▶ 늪지에 짓기 쉽지 않았다 → So 나무 기둥을 박았다 → '바로 이 나무 기둥들(these wooden poles)'이 오늘날까지 받친다.\n포인트 ▶ these wooden poles가 처음 나오는 문장 바로 앞", [('install', '설치하다'), ('pole', '기둥')])
# [원Q44]
T.flex('다음 글의 내용과 일치하지 <u>않는</u> 것은?', R, B(VEN, VEN2),
 ['베니스 사람들은 침략자로부터 안전하려고 최근에 물 위에 집을 지었다.', '베니스는 118개의 작은 섬으로 이루어져 있다.', '섬과 섬 사이는 수상 버스를 타고 이동할 수 있다.', '만조 때 바닷물이 불어나 거리가 물에 잠기곤 한다.', '늪지에 집을 짓기 위해 천만 개가 넘는 나무 기둥을 설치했다.'],
 "이유 ▶ 집을 지은 사람들은 '옛날' 베니스 사람들(The old Venetians) → 최근이 아니다.\n오답 ▶ {1} 118 small islands ✔ {2} a vaporetto, a water bus ✔ {3} At high tide ~ full of water ✔ {4} more than 10 million wooden poles ✔", [])
# [원Q45]
T.flex('다음 글의 내용과 일치하지 <u>않는</u> 것은?', R, B(VEN, VEN2),
 ['Venice is well known as the "flying city."', 'Venice consists of many small islands.', 'People can use a water bus to travel among the islands.', 'The old Venetians built the city on the water to keep themselves safe from invaders.', 'There are raised walkways for the times when the streets are flooded.'],
 "이유 ▶ 베니스의 별명은 floating city(떠 있는 도시) → flying city(날아다니는 도시) ❌.\n오답 ▶ {1} 118 small islands ✔ {2} a vaporetto, a water bus ✔ {3} to keep themselves safe from invaders ✔ {4} the raised walkways ✔\n수정 ▶ 원본 ①(곤돌라는 카누와 비슷한 노 젓는 배)은 본문에 없는 내용이라 이것도 답이 될 수 있었고, ④⑤는 어법이 틀린 문장이라 모두 고침", [('flood', '물에 잠기게 하다')])
# [원Q46]
T.flex('다음 글을 읽고 답할 수 <u>없는</u> 질문은?', R, B(VEN, VEN2),
 ['Where did the writer live in the past?', 'What does Venice consist of?', 'Why is Venice called the "floating city"?', 'Why did the old Venetians build their houses on the water?', 'How could they build their houses on the swampy surface?'],
 "이유 ▶ If I lived in Venice는 '베니스에 산다면'이라는 가정일 뿐 → 글쓴이가 실제로 어디에 살았는지는 알 수 없다.\n오답 ▶ {1} 118개의 작은 섬 {2} 물 위에 화려한 집들 {3} 침략자로부터 안전하려고 {4} 천만 개 넘는 나무 기둥\n수정 ▶ 원본 ① 'Where did I live?'를 뜻이 분명하게 바꿈", [])
# [원Q47]
T.flex('다음 글의 빈칸에 들어갈 말로 가장 적절한 것은?', R, B('If I lived in Venice, I would take a gondola to school every morning. Venice has 118 small islands. On weekends, I would travel from island to island by a vaporetto, a water bus. At high tide, the water from the Adriatic Sea often rises and leaves the streets ' + BL + '. However, I would be able to walk around the town through the raised walkways.'),
 ['full of water', 'filled with tourists', 'polluted with wastes', 'dirty along the way', 'full of colorful houses'],
 "이유 ▶ 만조 때 바닷물이 불어난다 → 거리가 '물로 가득' → 그래도 높인 통로로 걸어 다닐 수 있다(However).\n오답 ▶ {1} 관광객 {2} 쓰레기 {3} 더러운 {4} 화려한 집 – 바닷물이 불어난 결과가 아님", [])
# [원Q48]
T.flex('다음 글의 주제로 가장 적절한 것은?', R, B(VEN, VEN2),
 ['life in Venice and how and why it was built on the water', 'the history and population of Venice', 'famous tourist attractions in Venice', 'the danger of high tides in Italy', 'how to make a gondola'],
 "이유 ▶ 앞부분: 베니스에 산다면 하게 될 생활(곤돌라, 수상 버스, 높인 통로) → 뒷부분: 물 위에 집을 지은 이유와 방법.\n오답 ▶ {1} 인구는 언급 없음 {2} 관광 명소 – 언급 없음 {3} 만조는 일부 {4} 곤돌라 만드는 법 – 언급 없음\n수정 ▶ 원본 ④⑤가 둘 다 정답처럼 읽혀서 선택지를 새로 정리", [('population', '인구'), ('attraction', '명소')])
# [원Q49]
T.flex('다음 글의 빈칸에 들어갈 말로 가장 적절한 것은?', R, B('At high tide, the water from the Adriatic Sea often rises and leaves the streets full of water. However, I would be able to walk around the town ' + BL + '.'),
 ['through the raised walkways', 'using the dried roads', 'with the roads sunken', 'through the raised houses', 'using the water buses'],
 "이유 ▶ However: 거리가 물에 잠겨도 '높인 통로로' 걸어 다닐 수 있다.\n오답 ▶ {1} 마른 도로 – 물에 잠김과 반대 {2} 도로가 가라앉은 채로 {3} 높인 집 사이로 걸을 수 없음 {4} 수상 버스는 '걷는' 방법이 아님", [])
# [원Q50]
T.flex('다음 글의 빈칸에 들어갈 말로 가장 적절한 것은?', R, B('Venice is known as the "floating city." In Venice, there are many colorful houses on the water. You may wonder how and why they built the houses on the water. The old Venetians decided to live there ' + BL + '. But it was not easy for them to build their homes on this swampy surface.'),
 ['to keep themselves safe from invaders', 'because they loved the water too much', 'because they believed in the god of water', 'to isolate themselves from other villagers', 'to build more beautiful houses on the water'],
 "이유 ▶ 물 위에 산 '이유' = 침략자로부터 자신들을 안전하게 지키려고.\n오답 ▶ {1}·{2} 본문에 없는 이유 {3} 다른 마을 사람들과 고립 – 언급 없음 {4} 더 아름다운 집 – 언급 없음\n수정 ▶ 원본 ① did love를 loved로 다듬음", [('isolate', '고립시키다')])
# [원Q51]
T.flex('다음 글의 내용과 일치하는 것은?', R, B(VEN2),
 ['Venice was built on a swampy surface.', "The city of Venice is built in the air, so it's called the \"flying city.\"", 'Visitors to Venice may see many polluted houses on the water.', 'Lots of poles were floated on the water to build houses.', 'The wooden poles were finally removed after the houses were built.'],
 "이유 ▶ this swampy surface(늪이 많은 땅) 위에 집을 지었다 ✔\n오답 ▶ {1} floating city {2} colorful houses(화려한 집) {3} 기둥을 땅속에(in the ground) 박음 {4} 지금까지 받치고 있음(to this day)\n수정 ▶ 원본 ③ may have been built를 분명한 사실 문장으로 바꾸고, ② lots of many 같은 어색한 표현을 고침", [('remove', '없애다')])
# [원Q52]
T.flex('글에 따르면, 오늘날 베니스에서 볼 수 <u>없는</u> 것은?', R, B(VEN, VEN2),
 ['invaders attacking the city', 'a boat called a gondola', 'a water bus called a vaporetto', 'streets full of water at high tide', 'colorful houses on the water'],
 "이유 ▶ 침략자는 옛날 베니스 사람들이 물 위에 살게 된 '이유'일 뿐, 지금 도시를 공격하는 모습은 볼 수 없다.\n오답 ▶ {1} 곤돌라 {2} 수상 버스 {3} 만조 때 물에 잠긴 거리 {4} 물 위의 화려한 집 – 모두 지금 볼 수 있음", [])
# [원Q53]
T.flex('글의 내용으로 보아, 설명이 올바르지 <u>않은</u> 것은?', R, B(VEN, VEN2),
 ['A gondola is used to climb the raised walkways.', 'A water bus is used to move from island to island.', 'The raised walkways are used when the streets are full of water.', 'The old Venetians are people who lived in Venice long ago.', 'Lots of wooden poles were used to build houses on the water.'],
 "이유 ▶ 곤돌라는 학교에 타고 가는 배 → 높인 통로를 오르는 데 쓰지 않는다.\n오답 ▶ {1} from island to island by a vaporetto ✔ {2} 물에 잠겨도 높인 통로로 걷기 ✔ {3} 옛날 베니스 사람들 ✔ {4} 나무 기둥 천만 개 이상 ✔", [])
# [원Q54]
T.fixed('다음 글의 ⓐ~ⓔ 중 전체 흐름과 관계 <u>없는</u> 문장은?', R, B(
 'Venice is known as the "floating city." In Venice, ⓐ there are many colorful houses on the water. ⓑ You may wonder how and why they built the houses on the water. The old Venetians decided to live there to keep themselves safe from invaders. '
 'But it was not easy for them to build their homes on this swampy surface. ⓒ So they installed more than 10 million wooden poles in the ground. ⓓ Many visitors are attracted by the rivers in the city. ⓔ It is these wooden poles that support Venice to this day.'),
 ['ⓐ', 'ⓑ', 'ⓒ', 'ⓓ', 'ⓔ'], 4,
 "이유 ▶ 나무 기둥을 박았다 → 바로 이 기둥들이 받친다. 그 사이의 '관광객이 강에 끌린다'는 집을 지은 방법과 관계없다.\n포인트 ▶ these wooden poles는 ⓒ의 wooden poles를 이어 받아야 함", [('attract', '끌어들이다')])
# [원Q55]
T.flex('다음 글을 읽고 답할 수 <u>없는</u> 질문은?', R, B(VEN, VEN2),
 ['곤돌라에 탈 수 있는 최대 인원은?', '글쓴이가 학교에 갈 때 타고 갈 교통수단은?', '베니스에 있는 섬의 개수는?', '베니스에서 운행하는 수상 버스의 이름은?', '베니스의 또 다른 별명은?'],
 "이유 ▶ 곤돌라의 탑승 인원은 나오지 않는다.\n오답 ▶ {1} 곤돌라(take a gondola to school) {2} 118개 {3} vaporetto {4} floating city", [])
# [원Q58]
T.fixed('다음 글에서 전체 흐름과 관계 <u>없는</u> 문장은?', R, B(
 'If I lived in Venice, I would take a gondola to school every morning. ① Venice has 118 small islands. ② On weekends, I would travel from island to island by a vaporetto, a water bus. ③ Venice has been ranked the most beautiful city in the world many times. '
 '④ At high tide, the water from the Adriatic Sea often rises and leaves the streets full of water. ⑤ However, I would be able to walk around the town through the raised walkways.'), None, 3,
 "이유 ▶ 베니스에 산다면 하게 될 생활(곤돌라, 수상 버스, 높인 통로)을 상상하는 글 → '가장 아름다운 도시로 여러 번 뽑혔다'는 관계없다.\n수정 ▶ 원본 ③의 어순(has been ranked many times the most ~)을 다듬음", [('rank', '순위를 매기다')])
# [원Q59]
T.flex('다음 글을 읽고 답할 수 <u>있는</u> 질문은?', R, B(VEN2),
 ['Why did the old Venetians decide to live on the water?', 'How many houses are there on the water in Venice?', 'Where did the Venetians get the wooden poles?', 'When were the houses on the water built?', 'Who first called Venice the "floating city"?'],
 "이유 ▶ to keep themselves safe from invaders(침략자로부터 안전하려고) ✔\n오답 ▶ {1} 집의 수 {2} 나무를 구한 곳 {3} 지은 시기 {4} 처음 부른 사람 – 모두 나오지 않음\n수정 ▶ 원본 선택지의 오타(are the on, VEnetians)를 고침", [])
T.render()

# ═══════════════ 3세트 · 토루 ═══════════════
T = Test('3', '3세트', '본문 ③ 토루', '7과 본문 4', NOTICE, H=H)
# [원Q60]
T.fixed('다음 글의 밑줄 친 문장 중 어법상 가장 어색한 것은?', R, B(
 'If I lived in a tulou, a huge round house in Fujian, China, ' + CN(1, 'I would always have friends at home to play') + '. I would sometimes hear my neighbor calling me to come over for tea or dinner. In a tulou, ' + CN(2, 'there are usually three to five floors') +
 '. The first floor is used for cooking and eating. ' + CN(3, 'Do you wonder where I would sleep?') + ' My bedroom would be on the third or fourth floor. A tulou is like a village. ' + CN(4, 'The people living in a tulou mostly have the same family name') + '. ' +
 'Homes are everywhere. But they are different all over the world. ' + CN(5, 'What is your home like?')), None, 1,
 "이유 ▶ '함께 놀 친구들' = friends to play with. play friends ❌ → play with friends이므로 전치사 with가 꼭 필요하다.\n오답 ▶ ② There are + 복수명사 ✔ ③ 간접의문문(의문사 + 주어 + 동사) ✔ ④ living이 people을 꾸밈, 동사 have ✔ ⑤ What is ~ like?(~은 어떠니?) ✔\n수정 ▶ 원본 60번은 ①에 이미 to play with가 들어 있어 틀린 문장이 없었음 → ①을 to play로 바꿔 정답이 하나가 되게 함", [('play with', '~와 놀다')])
# [원Q61]
T.fixed('다음 글의 밑줄 친 부분 ①~⑤ 중 어법상 가장 어색한 것은?', R, B(
 CN(1, 'I would sometimes hear my neighbor calling me to come over for tea or dinner') + '. In a tulou, there are usually three to five floors. ' + CN(2, 'The first floor is used for cooking and eating') + '. And people store food and tools on the second floor. ' +
 CN(3, 'Where do you wonder I would sleep?') + ' My bedroom would be on the third or fourth floor. A tulou is like a village. ' + CN(4, 'The people living in a tulou mostly have the same family name') + '. Some large tulou can house up to 50 families. ' + CN(5, 'They work together and share many things') + '.'), None, 3,
 "이유 ▶ Do you wonder ~?는 Yes/No로 답하는 질문 → 간접의문문 어순: Do you wonder where I would sleep?\n오답 ▶ ① hear + 목적어 + -ing ✔ ② 수동태 + 전치사 + 동명사 ✔ ④ ✔ ⑤ ✔\n포인트 ▶ think, believe, guess일 때만 의문사가 맨 앞(Where do you think ~?). wonder, know는 Do you wonder where ~?", [('wonder', '궁금해하다')])
# [원Q62]
T.fixed('다음 글의 밑줄 친 부분 중 어법상 가장 어색한 것은?', R, B(
 'If I lived in a tulou, a huge round house in Fujian, China, ' + CN(1, 'I would always have friends at home to play with') + '. ' + CN(2, 'I would sometimes hear my neighbor calling me to come over for tea or dinner') + '. ' +
 CN(3, 'Do you wonder where I would sleep?') + ' A tulou is like a village. ' + CN(4, 'The people who living in a tulou mostly have the same family name') + '. Some large tulou can house up to 50 families. ' + CN(5, 'Living together in one building keeps them safe') + '.'), None, 4,
 "이유 ▶ 관계대명사 who 뒤에는 동사가 와야 한다 → The people who live in a tulou 또는 who를 빼고 The people living in a tulou.\n오답 ▶ ①·②·③·⑤ 본문 그대로 ✔\n포인트 ▶ 명사 + -ing = 명사 + who(that) + 동사", [])
# [원Q63]
T.fixed('다음 글의 밑줄 친 부분 중 어법상 가장 어색한 것은?', R, B(
 'I would sometimes hear my neighbor ' + CN(1, 'calling') + ' me to come over for tea or dinner. Do you wonder ' + CN(2, 'where') + ' I would sleep? A tulou is like a village. The people living in a tulou mostly ' + CN(3, 'have') +
 ' the same family name. They work together and share many things. Living together in one building ' + CN(4, 'keep') + ' them safe. ' + CN(5, 'What') + ' is your home like?'),
 ['calling', 'where', 'have', 'keep', 'What'], 4,
 "이유 ▶ 주어는 동명사구 Living together in one building → 단수 취급 → keeps.\n오답 ▶ ① 지각동사 hear + 목적어 + -ing ✔ ② 간접의문문 ✔ ③ 주어 The people(복수) ✔ ⑤ What ~ like? ✔\n포인트 ▶ 동명사(구) 주어 = 단수 동사", [])
# [원Q64]
T.flex('다음 (A), (B), (C)의 각 괄호 안에서 어법에 맞는 표현으로 가장 적절한 것은?', R, B(
 'If I (A) [lived / had lived] in a tulou, a huge round house in Fujian, China, I would always have friends at home to play with. The people living in a tulou mostly (B) [have / has] the same family name. Homes are everywhere. But they are different all over the world. (C) [What / How] is your home like?'),
 ['lived − have − What', 'had lived − have − What', 'had lived − have − How', 'lived − has − How', 'had lived − has − What'],
 "이유 ▶ (A) 주절 would have → 가정법 과거 lived (B) 주어 The people(복수) → have (C) like(전치사)의 목적어가 될 수 있는 의문대명사 What\n포인트 ▶ What is ~ like? = How is ~? (How is ~ like? ❌)", [])
# [원Q65]
T.flex('다음 (A), (B), (C)의 각 괄호 안에서 어법에 맞는 표현으로 가장 적절한 것은?', R, B(
 'I would sometimes hear my neighbor (A) [calling / to call] me to come over for tea or dinner. A tulou is like a village. The people (B) [living / live] in a tulou mostly have the same family name. Living together in one building (C) [keeps / keep] them safe.'),
 ['calling − living − keeps', 'calling − live − keep', 'to call − live − keeps', 'calling − live − keeps', 'to call − living − keep'],
 "이유 ▶ (A) 지각동사 hear + 목적어 + 동사원형/-ing (to부정사 ❌) (B) 문장의 동사 have가 따로 있으므로 people을 꾸미는 분사 living (C) 동명사구 주어 → 단수 keeps", [])
# [원Q68 서술형 → 객관식]
T.flex('다음 [영영풀이]에 해당하는 단어로, 본문에 쓰인 것은?', R, B('[영영풀이] to contain or accommodate', '', TUL2),
 ['house', 'share', 'work', 'keep', 'store'],
 "이유 ▶ Some large tulou can <i>house</i> up to 50 families. 여기서 house는 '수용하다(accommodate)'라는 동사.\n오답 ▶ {1} 공유하다 {2} 일하다 {3} 유지하다 {4} 저장하다\n수정 ▶ 원본 68번(주관식)을 객관식으로 바꿈", [('accommodate', '수용하다'), ('house', '(동사) 수용하다, 살 곳을 주다')])
# [원Q71]
T.flex('다음 글의 내용과 일치하지 <u>않는</u> 것은?', R, B(TUL, TUL2),
 ['토루에서 식사하는 곳과 잠자는 곳은 같은 층에 있다.', '토루는 모양이 둥글다.', '토루는 보통 3층에서 5층이다.', '토루에 사는 사람들은 대부분 성이 같다.', '큰 토루는 50가구까지 수용할 수 있다.'],
 "이유 ▶ 1층은 요리·식사, 침실은 3층이나 4층 → 같은 층이 아니다.\n오답 ▶ {1} a huge round house ✔ {2} three to five floors ✔ {3} the same family name ✔ {4} up to 50 families ✔", [])
# [원Q72]
T.flex('다음 글의 내용과 일치하지 <u>않는</u> 것은?', R, B(TUL, TUL2),
 ['모든 토루는 5층이며, 3층과 4층에 침실이 있다.', '토루는 중국 푸젠 지역에 있는 커다란 원형 집이다.', '토루의 1층은 요리하고 식사하는 공간이다.', '2층에는 식량과 도구를 보관한다.', '같은 토루에 사는 사람들은 대부분 성이 같다.'],
 "이유 ▶ 토루는 보통 3층에서 5층(usually three to five floors) → '모든 토루가 5층'은 아니다.\n오답 ▶ {1} a huge round house in Fujian, China ✔ {2} ✔ {3} ✔ {4} ✔\n수정 ▶ 원본의 맞춤법(커다른)을 고침", [])
# [원Q73]
T.flex('What is NOT true according to the passage?', R, B(TUL, TUL2),
 ['A tulou usually has only one family.', 'Most tulous have three to five floors.', 'People have meals on the first floor.', 'Food is stored on the second floor.', 'A tulou is similar to a village.'],
 "이유 ▶ 큰 토루는 50가구까지 살 수 있고, 마을과 같다 → 한 가족만 산다는 것은 틀림.\n오답 ▶ {1} three to five floors ✔ {2} cooking and eating ✔ {3} store food and tools on the second floor ✔ {4} like a village ✔\n수정 ▶ 원본 ① 'three or five floors'(3층 또는 5층)도 본문(3~5층)과 달라 정답이 둘이었음 → three to five로 고침", [('similar to', '~와 비슷한')])
# [원Q74]
T.flex('다음 글을 읽고 답할 수 <u>없는</u> 질문은?', R, B(TUL, TUL2),
 ['How many family names are there in a tulou?', 'Where can we find a tulou?', 'What is the first floor used for?', 'Where would the writer\'s bedroom be?', 'How many families can a large tulou house?'],
 "이유 ▶ '대부분 성이 같다'고만 했을 뿐 성씨가 몇 개인지는 알 수 없다.\n오답 ▶ {1} 중국 푸젠 {2} 요리·식사 {3} 3층이나 4층 {4} 50가구까지\n수정 ▶ 원본 ② 장점(benefits), ③ 높이(how high)는 답이 애매해서 분명한 질문으로 바꿈", [])
# [원Q75]
T.flex('밑줄 친 부분과 같은 의미를 바르게 나타낸 것은?', G, B('<u>The people living in a tulou</u> mostly have the same family name.'),
 ['the people who live in a tulou', 'the people life in a tulou', 'the people who lived in a tulou', 'the people who was living in a tulou', 'the people live in a tulou'],
 "이유 ▶ 명사 + -ing = 명사 + 주격 관계대명사 + 동사. 문장의 시제가 현재(have)이므로 who live.\n오답 ▶ {1} life는 명사 {2} 과거 {3} 복수 주어인데 was {4} 관계대명사 없이 동사 두 개", [])
# [원Q76]
T.fixed('다음 글의 밑줄 친 ①~⑤ 중 어법상 <u>틀린</u> 것은?', R, B(
 'If I lived in a tulou, a huge round house in Fujian, China, I ' + CN(1, 'would always have friends at home to play') + '. I would sometimes hear my neighbor ' + CN(2, 'calling me to come over') + ' for tea or dinner. The first floor ' +
 CN(3, 'is used for cooking') + ' and eating. Do you wonder ' + CN(4, 'where I would sleep') + '? My bedroom would be ' + CN(5, 'on the third or fourth floor') + '.'), None, 1,
 "이유 ▶ play with friends(친구들과 놀다) → friends to play with. 전치사 with가 빠졌다.\n오답 ▶ ② hear + 목적어 + -ing ✔ ③ 수동태 + 동명사 ✔ ④ 간접의문문 ✔ ⑤ ✔", [])
# [원Q77]
T.fixed('다음 글의 밑줄 친 ①~⑤ 중 어법상 <u>틀린</u> 것은?', R, B(
 'A tulou ' + CN(1, 'is like') + ' a village. The people ' + CN(2, 'living in a tulou') + ' mostly have the same family name. Some large tulou ' + CN(3, 'can house up to 50 families') + '. They work together and share many things. ' +
 CN(4, 'Living together in one building keeps them safely') + '. Homes are everywhere. But they are different all over the world. ' + CN(5, 'What is your home like') + '?'), None, 4,
 "이유 ▶ keep + 목적어 + 형용사 → keeps them safe. 부사 safely는 목적격 보어가 될 수 없다.\n오답 ▶ ① ~와 같다 ✔ ② 분사 ✔ ③ 조동사 + 동사 house ✔ ⑤ ✔", [])
# [원Q78]
T.flex('밑줄 친 <u>is like</u>와 의미가 가장 가까운 것은?', R, B('A tulou <u>is like</u> a village. The people living in a tulou mostly have the same family name. Some large tulou can house up to 50 families.'),
 ['resembles', 'cares for', 'takes care of', 'looks after', 'looks into'],
 "이유 ▶ be like(~와 같다, ~와 비슷하다) = resemble(닮다).\n오답 ▶ {1} 돌보다, 좋아하다 {2}·{3} 돌보다 {4} 조사하다\n수정 ▶ 원본 문제 안에 79번의 [조건]이 잘못 붙어 있어 뺌", [('resemble', '닮다, 비슷하다')])
# [원Q80]
T.fixed('다음 글의 밑줄 친 부분 중 쓰임이 옳은 것은?', R, B(
 'A tulou ' + CN(1, 'does like') + ' a village. The people ' + CN(2, 'live') + ' in a tulou ' + CN(3, 'most') + ' have the same family name. Some large tulou can house up to 50 families. They work together and ' + CN(4, 'shares') + ' many things. ' +
 CN(5, 'To live together') + ' in one building keeps them safe.'),
 ['does like', 'live', 'most', 'shares', 'To live together'], 5,
 "이유 ▶ 주어 자리에 to부정사(To live together ~)도 쓸 수 있다 → 단수 동사 keeps ✔\n오답 ▶ ① is like(~와 같다) ② 동사가 have로 따로 있으므로 living ③ 부사 mostly(대부분) ④ They(복수) → share\n포인트 ▶ 동명사 주어 = to부정사 주어 (둘 다 단수 취급)", [])
# [원Q81]
T.fixed('다음 글의 밑줄 친 부분 중 어법상 적절하지 <u>않은</u> 것은?', R, B(
 'A tulou is ' + CN(1, 'similar') + ' to a village. The people ' + CN(2, 'who are living') + ' in a tulou mostly have the same family name. Some large tulou can house ' + CN(3, 'up to') + ' 50 families. They work together and share many things. Living together in one building ' +
 CN(4, 'keep') + ' them safe. Homes are everywhere. But they are ' + CN(5, 'diverse') + ' all over the world.'),
 ['similar', 'who are living', 'up to', 'keep', 'diverse'], 4,
 "이유 ▶ 동명사구 주어는 단수 → keeps.\n오답 ▶ ① be similar to(~와 비슷하다) ✔ ② 관계대명사 + 진행형 ✔ ③ ~까지 ✔ ⑤ 다양한 ✔\n수정 ▶ 원본 발문 '어휘의 쓰임'을 '어법상'으로 고침(틀린 곳이 어법이라서)", [('diverse', '다양한')])
# [원Q83]
T.flex('다음 글에 나타난 토루에서의 삶의 모습으로 적절한 것은?', R, B(TUL, TUL2),
 ['주민들은 대부분 같은 성씨를 쓴다.', '집에 함께 놀 친구가 없다.', '보통 3~5개의 부엌이 있다.', '맨 아래층은 보통 식량이나 도구를 보관하는 데 쓰인다.', '주민들은 모여 살지만 각자 따로 생활한다.'],
 "이유 ▶ mostly have the same family name ✔\n오답 ▶ {1} always have friends at home to play with {2} 부엌이 아니라 3~5개 층 {3} 1층은 요리·식사, 보관은 2층 {4} 함께 일하고 많은 것을 나눈다\n수정 ▶ 원본 정답이 ④⑤ 두 개였지만 ⑤는 본문(work together and share many things)과 반대 → 정답 하나로 고침", [])
# [원Q84]
T.flex('밑줄 친 <u>like</u>와 쓰임이 같은 것은?', G, B('A tulou is <u>like</u> a village.'),
 ['He is like a giant lion.', 'You like your teacher, don\'t you?', 'She likes to go to the shopping mall.', 'They like your ability to communicate with others.', 'I would like to visit Venice someday.'],
 "이유 ▶ 본문의 like는 '~와 같은'이라는 전치사. He is like a giant lion(그는 거대한 사자 같다)도 전치사.\n오답 ▶ {1}·{2}·{3} '좋아하다'라는 동사 {4} would like to(~하고 싶다)\n수정 ▶ 원본은 '모두 고르기'(정답 ②③)였는데 OMR에 맞게 정답 하나로 고침", [])
# [원Q85]
T.fixed('다음 글의 밑줄 친 부분 중 어법상 알맞은 것은?', R, B(
 'If I lived in a tulou, I would always have friends at home to play with. I would sometimes ' + CN(1, 'heard') + ' my neighbor calling me to come over for tea or dinner. In a tulou, there ' + CN(2, 'are') + ' usually three to five floors. The first floor is ' +
 CN(3, 'using') + ' for cooking and eating. Do you wonder where ' + CN(4, 'would I') + ' sleep? The people ' + CN(5, 'lived') + ' in a tulou mostly have the same family name.'),
 ['heard', 'are', 'using', 'would I', 'lived'], 2,
 "이유 ▶ There are + 복수명사(three to five floors) ✔\n오답 ▶ ① would + 동사원형 hear ③ 1층이 '사용되는' 수동 → used ④ 간접의문문 어순 I would ⑤ 사람들이 '사는' 능동 → living\n수정 ▶ 원본 지문 첫 문장이 단어 배열로 깨져 있어 본문 문장으로 되돌림", [])
T.render()

# ═══════════════ 4세트 · 문법 · 서술형을 객관식으로 ═══════════════
T = Test('4', '4세트', '문법 · 서술형 → 객관식', '7과 전 범위', NOTICE + ' 4세트는 원본 서술형 문항을 객관식으로 바꾼 문항이 많아요.', H=H)
# [원Q87]
T.fixed('글의 흐름으로 보아, 주어진 문장이 들어갈 위치로 가장 적절한 곳은?', R, B('Imagine you live in one of these houses.') + '\n' + B(
 'Different people live in different houses. Some use ladders to enter their houses.' + GP(1) + 'Others live in houses on the water. And others share their houses with many people.' + GP(2) + 'How would that change your life?' + GP(3) +
 'If I lived in a pueblo, I would climb up a ladder to enter my house.' + GP(4) + 'There\'s a hidden opening on top of the house.' + GP(5) + 'If unwelcome visitors appeared, I would pull the ladder up to stop them from entering.'), None, 2,
 "이유 ▶ 세 종류의 집 소개 → '이런 집들(these houses) 중 하나에 산다고 상상해 봐' → '그것이(that) 네 삶을 어떻게 바꿀까?'\n포인트 ▶ these houses는 앞의 집들, that은 주어진 문장의 상상을 가리킴", [])
# [원Q88]
T.flex('다음 빈칸에 들어갈 말로 가장 적절한 것은?', G, B('If she had money, she ' + BL + ' buy something to eat.'),
 ['could', 'shall', 'may', 'can', 'will'],
 "이유 ▶ If + 과거형(had) → 가정법 과거 → 주절은 조동사 과거형(would/could) + 동사원형.\n오답 ▶ {1}·{2}·{3}·{4} 현재형 조동사는 가정법 과거의 주절에 쓰지 않음", [])
# [원Q93]
T.flex('다음 중 어법상 어색한 것은?', G, '',
 ['This problem is considered simply.', 'The news made her sad.', 'They let me go to the concert.', 'He saw her entering the building.', 'Jack heard his brother sing on the stage.'],
 "이유 ▶ consider + 목적어 + 형용사(…을 ~하다고 여기다)의 수동태 → is considered simple. 부사 simply ❌.\n오답 ▶ {1} make + 목적어 + 형용사 ✔ {2} let + 목적어 + 동사원형 ✔ {3} see + 목적어 + -ing ✔ {4} hear + 목적어 + 동사원형 ✔", [])
# [원Q94 서술형 → 객관식]
T.flex('다음 문장에서 어법상 틀린 곳을 바르게 고친 것은?', G, B('She kept her knife sharply.'),
 ['sharply → sharp', 'kept → keeps', 'her → hers', 'knife → knives', 'kept → was kept'],
 "이유 ▶ keep + 목적어 + 형용사(목적격 보어) → kept her knife sharp(칼을 날카롭게 유지했다).\n오답 ▶ {1} 시제는 문제없음 {2} 소유격 her ✔ {3} 단수도 가능 {4} 수동태면 목적어가 남을 수 없음\n수정 ▶ 원본 94번(주관식)을 객관식으로 바꿈", [('sharp', '날카로운')])
# [원Q95]
T.flex('다음 빈칸에 들어갈 말로 어법상 알맞지 <u>않은</u> 것은?', G, B('Jack ' + BL + ' his brother sing on the stage.'),
 ['allowed', 'heard', 'saw', 'watched', 'made'],
 "이유 ▶ allow + 목적어 + to부정사 → allowed his brother to sing. 뒤에 동사원형 sing이 있으므로 allowed는 쓸 수 없다.\n오답 ▶ {1}·{2}·{3} 지각동사 + 목적어 + 동사원형 ✔ {4} 사역동사 make + 목적어 + 동사원형 ✔", [])
# [원Q99]
T.flex('다음 중 밑줄 친 if의 쓰임이 나머지 넷과 <u>다른</u> 것은?', G, '',
 ['He couldn\'t tell <u>if</u> she was laughing or crying.', '<u>If</u> he left early, he could take the first train.', 'He could pass the exam <u>if</u> he studied a little harder.', '<u>If</u> they didn\'t stop us, we could save time.', 'I could finish the work early <u>if</u> she helped me.'],
 "이유 ▶ tell if ~ = ~인지 아닌지 알다 → 명사절을 이끄는 if(~인지).\n오답 ▶ {1}·{2}·{3}·{4} '만약 ~라면' 가정법 조건절의 if", [])
# [원Q100]
T.flex('다음 우리말과 같은 의미가 되도록 바르게 영작한 것은?', G, B('네가 내 입장이라면 너도 똑같이 할 거야.'),
 ['If you were in my position, you would do the same.', 'If you are in my position, you would do the same.', 'As you are in my position, you will do the same.', 'If you were in my position, you do the same.', 'As you were not in my position, you would do the same.'],
 "이유 ▶ 현재 사실의 반대 → 가정법 과거: If + 과거형(were), 주어 + would + 동사원형.\n오답 ▶ {1} are → were {2} 가정법이 아님 {3} 주절에 would 필요 {4} 가정법이 아님\n수정 ▶ 원본 우리말 '했을 거야'는 과거 가정(가정법 과거완료)이라 정답과 맞지 않아 '할 거야'로 고침", [('position', '입장, 처지')])
# [원Q8 서술형 → 객관식]
T.flex('두 문장의 의미가 같도록 빈칸에 들어갈 말로 알맞은 것은?', G, B('Some use ladders to enter their houses.', '= Some use ladders with a view to ' + BL + ' their houses.'),
 ['entering', 'enter', 'entered', 'to enter', 'be entering'],
 "이유 ▶ with a view to -ing = ~하기 위해. 이때 to는 전치사 → 동명사 entering.\n오답 ▶ {1}·{3} to를 to부정사로 착각 {2} 과거분사 {4} 형태 오류\n수정 ▶ 원본 8번(주관식)을 객관식으로 바꿈", [])
# [원Q25 서술형 → 객관식]
T.flex('밑줄 친 문장과 의미가 같은 것은?', G, B('<u>I would climb up a ladder to enter my house.</u>'),
 ['I would climb up a ladder for the purpose of entering my house.', 'I would climb up a ladder for the purpose of enter my house.', 'I would climb up a ladder for the purpose to enter my house.',
  'I would climb up a ladder so that entering my house.', 'I would climb up a ladder in order entering my house.'],
 "이유 ▶ to부정사(목적) = for the purpose of -ing = in order to + 동사원형 = so that 주어 can ~.\n오답 ▶ {1} of 뒤 동명사 {2} for the purpose of로 써야 함 {3} so that 뒤에는 주어 + 동사 {4} in order to enter\n수정 ▶ 원본 25번(주관식)을 객관식으로 바꿈", [('for the purpose of -ing', '~할 목적으로')])
# [원Q26 서술형 → 객관식]
T.flex('다음 우리말을 영어로 바르게 옮긴 것은?', G, B('만약 반갑지 않은 방문객들이 나타난다면, 나는 그들이 들어오는 것을 막기 위해 사다리를 끌어올릴 것이다.'),
 ['If unwelcome visitors appeared, I would pull the ladder up to stop them from entering.', 'If unwelcome visitors appear, I would pull the ladder up to stop them from entering.',
  'If unwelcome visitors appeared, I would pull the ladder up to stop them to entering.', 'If unwelcome visitors appeared, I will pull the ladder up to stop them from entering.',
  'If unwelcome visitors were appeared, I would pull the ladder up to stop them from entering.'],
 "이유 ▶ 가정법 과거(If + 과거형, would + 동사원형) + stop A from -ing.\n오답 ▶ {1} appear → appeared {2} stop A from -ing {3} will → would {4} appear는 수동태 ❌\n수정 ▶ 원본 26번(배열 서술형)을 객관식으로 바꿈", [])
# [원Q30 서술형 → 객관식]
T.flex('괄호 안의 단어를 어법에 맞게 고친 것으로 바르게 짝지어진 것은?', G, B('If I ⓐ (live) in a pueblo, I would climb up a ladder to enter my house. If unwelcome visitors ⓑ (appear), I would pull the ladder up to stop them from ⓒ (enter).'),
 ['ⓐ lived − ⓑ appeared − ⓒ entering', 'ⓐ live − ⓑ appeared − ⓒ entering', 'ⓐ lived − ⓑ were appeared − ⓒ entering', 'ⓐ lived − ⓑ appeared − ⓒ enter', 'ⓐ had lived − ⓑ appear − ⓒ to enter'],
 "이유 ▶ ⓐ·ⓑ 가정법 과거 → 과거형 lived, appeared ⓒ 전치사 from 뒤 → 동명사 entering\n오답 ▶ {1} ⓐ 현재형 {2} ⓑ 수동태 ❌ {3} ⓒ from 뒤 동사원형 ❌ {4} 셋 다 틀림\n수정 ▶ 원본 30번(주관식)을 객관식으로 바꿈", [])
# [원Q40 서술형 → 객관식]
T.flex('밑줄 친 강조 구문을 강조하기 전의 문장으로 바르게 고친 것은?', G, B('So they installed more than 10 million wooden poles in the ground. <u>It is these wooden poles that support Venice to this day.</u>'),
 ['These wooden poles support Venice to this day.', 'These wooden poles supports Venice to this day.', 'Venice supports these wooden poles to this day.', 'It supports these wooden poles to this day.', 'These wooden poles that support Venice to this day.'],
 "이유 ▶ It is ~ that을 지우고 남은 말을 이으면 원래 문장: These wooden poles support Venice to this day.\n오답 ▶ {1} 복수 주어에 supports {2} 주어·목적어가 바뀜 {3} 강조된 말이 빠짐 {4} that이 남아 문장이 끝나지 않음\n수정 ▶ 원본 40번(주관식)을 객관식으로 바꿈", [])
# [원Q42 서술형 → 객관식]
T.flex('다음 빈칸에 공통으로 들어갈 말로, 영영풀이에 해당하는 단어는?', R, B('[영영풀이] a long, straight piece of wood, metal, etc., that is often placed in the ground so that it stands straight up', '',
 'So they installed more than 10 million wooden ' + BL + 's in the ground. It is these wooden ' + BL + 's that support Venice to this day.'),
 ['pole', 'island', 'walkway', 'gondola', 'ladder'],
 "이유 ▶ 땅속에 박아 곧게 세우는 길고 곧은 나무·금속 = 기둥(pole).\n오답 ▶ {1} 섬 {2} 통로 {3} 곤돌라 {4} 사다리\n수정 ▶ 원본 42번(주관식)을 객관식으로 바꿈", [('pole', '기둥, 막대')])
# [원Q57 서술형 → 객관식]
T.flex('밑줄 친 부분과 같은 문장 구조를 써서 우리말을 바르게 영작한 것은?', G, B('<u>If I lived in Venice, I would take a gondola to school</u> every morning.', '', '내가 새라면, 나는 너에게 날아갈 수 있을 텐데.'),
 ['If I were a bird, I could fly to you.', 'If I am a bird, I can fly to you.', 'If I were a bird, I can fly to you.', 'If I had been a bird, I could fly to you.', 'If I be a bird, I could fly to you.'],
 "이유 ▶ 가정법 과거: If + 주어 + were(be동사는 주로 were), 주어 + could + 동사원형.\n오답 ▶ {1} 직설법 {2} 주절 can → could {3} 과거완료는 과거 사실의 반대 {4} be → were\n수정 ▶ 원본 57번(주관식)을 객관식으로 바꿈", [])
# [원Q69 서술형 → 객관식]
T.flex('두 문장의 의미가 같도록 빈칸 (a), (b)에 들어갈 말로 바르게 짝지어진 것은?', G, B('The people living in a tulou mostly have the same family name.', '= The people (a) ' + BL + ' (b) ' + BL + ' in a tulou mostly have the same family name.'),
 ['who − live', 'who − living', 'which − live', 'who − lives', 'whom − live'],
 "이유 ▶ 명사 + -ing = 명사 + 주격 관계대명사(who/that) + 동사. 선행사 people(사람, 복수), 시제 현재 → who live.\n오답 ▶ {1} who 뒤에는 동사 {2} which는 사물 {3} people은 복수 {4} whom은 목적격\n수정 ▶ 원본 69번(주관식)을 객관식으로 바꿈", [])
# [원Q70 서술형 → 객관식]
T.flex('괄호 안의 단어를 어법에 맞게 고친 것으로 바르게 짝지어진 것은?', G, B('The first floor is used for cooking and ⓐ (eat). The people ⓑ (live) in a tulou mostly have the same family name. Living together in one building ⓒ (keep) them safe.'),
 ['ⓐ eating − ⓑ living − ⓒ keeps', 'ⓐ eat − ⓑ living − ⓒ keeps', 'ⓐ eating − ⓑ live − ⓒ keeps', 'ⓐ eating − ⓑ living − ⓒ keep', 'ⓐ eaten − ⓑ lived − ⓒ keep'],
 "이유 ▶ ⓐ cooking과 and로 나란히 → eating ⓑ 동사 have가 따로 있으므로 people을 꾸미는 분사 living ⓒ 동명사구 주어 → 단수 keeps\n오답 ▶ {1} ⓐ for 뒤 동명사 {2} ⓑ 동사가 두 개 {3} ⓒ 단수 {4} 셋 다 틀림\n수정 ▶ 원본 70번(주관식)을 객관식으로 바꿈", [])
# [원Q89 서술형 → 객관식]
T.flex('다음 문장을 가정법으로 바르게 바꾼 것은?', G, B('As she loves him, you have to give up on him.'),
 ["If she didn't love him, you wouldn't have to give up on him.", "If she loved him, you would have to give up on him.", "If she doesn't love him, you won't have to give up on him.",
  "If she didn't love him, you would have to give up on him.", "If she hadn't loved him, you didn't have to give up on him."],
 "이유 ▶ 직설법 현재 → 가정법 과거: 시제는 과거로, 긍정 ↔ 부정을 뒤집기 (loves → didn't love, have to → wouldn't have to).\n오답 ▶ {1} 긍정·부정을 안 뒤집음 {2} 직설법 조건문 {3} 주절을 안 뒤집음 {4} 시제 오류\n수정 ▶ 원본 89번(주관식)을 객관식으로 바꿈", [('give up on', '~을 단념하다')])
# [원Q90 서술형 → 객관식]
T.flex('두 문장의 의미가 같도록 빈칸에 들어갈 말로 알맞은 것은?', G, B('I wish I could speak English well.', "= I'm sorry that I " + BL + ' English well.'),
 ["can't speak", 'could speak', 'can speak', "couldn't speak", "won't speak"],
 "이유 ▶ I wish + 가정법 과거(지금 못 해서 아쉬움) = I'm sorry that + 직설법 현재(부정) → can't speak.\n오답 ▶ {1}·{2} 긍정 {3} 과거 {4} 미래\n수정 ▶ 원본 90번(주관식)을 객관식으로 바꿈", [])
# [원Q92 서술형 → 객관식]
T.flex('두 문장의 의미가 같도록 빈칸에 들어갈 말로 알맞은 것은?', G, B('I am sorry that she has to go there with him.', '= I wish ' + BL + '.'),
 ["she didn't have to go there with him", 'she had to go there with him', "she doesn't have to go there with him", "she hadn't had to go there with him", 'she has to go there with him'],
 "이유 ▶ I'm sorry that + 현재·긍정 → I wish + 과거·부정 (has to → didn't have to).\n오답 ▶ {1} 긍정 그대로 {2} 현재형 {3} 과거완료 {4} 직설법 그대로\n수정 ▶ 원본 92번(주관식)을 객관식으로 바꿈", [])
# [원Q96 서술형 → 객관식]
T.flex("다음 문장을 'because'를 써서 직설법으로 바르게 바꾼 것은?", G, B('If we had enough time, we could finish it today.'),
 ["Because we don't have enough time, we can't finish it today.", 'Because we have enough time, we can finish it today.', "Because we didn't have enough time, we couldn't finish it today.",
  "Because we don't have enough time, we can finish it today.", "Because we had enough time, we couldn't finish it today."],
 "이유 ▶ 가정법 과거 → 직설법 현재: 시제는 현재로, 긍정 ↔ 부정 뒤집기 (had → don't have, could → can't).\n오답 ▶ {1} 긍정·부정을 안 뒤집음 {2} 과거 시제 {3} 주절을 안 뒤집음 {4} 시제·의미 오류\n수정 ▶ 원본 96번(주관식)을 객관식으로 바꿈", [])
T.render()
