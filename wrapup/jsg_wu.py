# 11/18 중산중3 지학사(민찬규) 기출 선별 1·2회 — 중산중 2학기 지필 4개(2022 1차·2차, 2024 1차·2차)에서 7·8과 문항만 골라 17문항씩 (7과 8 + 8과 9)
# 원본: 선생님 스캔 PDF 4개(학생 필기 있음) → work/m3exam. 외부지문(미로·Frindle·속담·Write for Rights·행운의 숫자·소금·SNS·노래)과 다른 과 대화·문법(관계부사·분사구문·one) 제외
# 은데벨레·한옥은 7과 응용 지문(우리 단원 본문엔 없음)이라 넣음. 정답은 원본 정답을 검수해 정함. 원본 번호는 각 문항 위 주석 [연도-차수-번호]
from wu_jsg import *
H = ('중산중 기출 선별', '중산중 2학기 지필평가 (2022 · 2024)', '중산중 기출 2022 · 2024', 'jsg')
Bx = lambda *ls: BOX('<br>'.join(ls))
S7, S8, S7A = '7과', '8과', '7과 응용'
N = '중산중 3학년 2학기 지필평가(2022 · 2024) 중 7·8과 문항만 골라 모았어요. 배점은 문항 끝에 있어요. 35분 안에 풀고 OMR에 답을 입력하세요.'
CN_ = '①②③④⑤'

# 공통 지문
VEN12 = Bx("If I lived in Venice, I would take a gondola to school every morning. Venice has 118 small islands. On weekends, I would travel from island to island by a <i>vaporetto</i>, a water bus. "
           "At high tide, the water from the Adriatic Sea often (가) <u>rises and leave the streets full of water</u>. ( ⓐ )",
           "(나) <u>Venice is known as the \"floating city.\"</u> In Venice, there are many colorful houses on the water. You may wonder about the houses on the water. ( ⓑ ) "
           "The old Venetians decided to live there to protect themselves from invaders. But (다) <u>it was not easy for them to build</u> their homes on this swampy surface. ( ⓒ ) "
           "So they installed more than 10 million wooden poles in the ground. ( ⓓ ) (라) <u>It is these wooden poles that supports</u> Venice to this day. ( ⓔ )")
ROB17 = Bx("\"My name is Pascal. I don't know why I'm here, but there must be a reason. The soldiers were shooting arrows. You ⓐ <u>saved</u> me from them. Thank you so much. Is there anything I can do for you?\"",
           "\"Well, can you help us ⓑ <u>get back</u> the money that the king took from the people? He taxed them too much. He is ___(A)___ greedy to share with the people, so they don't have ⓒ <u>enough</u> money to buy food. "
           "I want to help them get their money back. ⓓ <u>However</u>, there are many soldiers in the tower, so ⓔ <u>anyone</u> can get inside.\"",
           "\"Hmm... I think I have a solution. But first, can you take me to the tower? I need to count the number of soldiers.\"")
ROB19 = Bx("Robin Hood asked Pascal, \"Can you help us get back the money that the king took from the people? He taxed them too much, so they don't have enough money to buy food. I want to help them get their money back. "
           "However, there are many soldiers in the tower, so no one can get inside.\"",
           "\"Hmm... I think I have a solution. But first, can you take me to the tower? I need to count the number of soldiers,\" Pascal said.",
           "Robin and Pascal hid up in a tree and counted the soldiers one by one.",
           "After counting the soldiers, Pascal told Robin when the best time to enter the tower was, but he didn't get it. Pascal thought a graph might make his explanation easier to understand and drew the graph.")
TD = 'style="border:1px solid #9aa3b5;padding:3px 8px;text-align:center"'
GRAPH = ('<b>One-Day Soldiers in the Tower</b> (number of soldiers)<br><table style="border-collapse:collapse;margin:4px 0;font-size:13px"><tr>'
         + ''.join('<th %s>%s</th>' % (TD, h) for h in ('time', '0~6', '6~12', '12~18', '18~24')) + '</tr><tr>'
         + ''.join('<td %s>%s</td>' % (TD, v) for v in ('soldiers', '5', '3', '8', '12')) + '</tr></table>(Pascal이 그린 막대그래프를 표로 옮김)')
ROB15 = Bx("Suddenly, Pascal heard men shouting. When he opened ⓐ <u>his</u> eyes, he saw soldiers on horses. They were chasing a man with arrows in ⓑ <u>his</u> hand. The man saw Pascal and shouted.",
           "\"It's too dangerous for you to stand there. Come on.\" The man held out ⓒ <u>his</u> hand to Pascal and pulled him onto ⓓ <u>his</u> horse and rode into the woods.",
           "When they arrived at a house, the man stopped and got off ⓔ <u>his</u> horse.",
           "\"Hello, my name is Robin Hood.\"", "\"Wow! Are you the Robin Hood from the book?\"", "\"No, I'm the Robin Hood of Sherwood Forest. Who are you and why are you here?\"",
           "\"My name is Pascal. I don't know why I'm here, but there must be a reason. You saved me from the soldiers. Thank you very much for saving my life, so I'd like to do anything for you. Is there anything I can do for you?\"")

# ═══════════════ 1회 ═══════════════
T = Test('1', '1회', '7과 8문항 · 8과 9문항', '중산중 기출', N, H=H)
# [2024-2차-1]
T.flex('밑줄 친 어휘의 의미와 가장 가까운 것은?', S8, Bx('The kids <u>chased</u> each other around the kitchen table.'),
 ['to run after somebody in order to catch him or her', 'to make a logical or causal connection', 'to calculate the total number of people or things', 'to express indirectly by an image, form, or model', 'to mean something is important because it has an effect on you'],
 "이유 ▶ chase = 뒤쫓다(잡으려고 뒤따라 달리다). 본문: They were chasing a man with arrows in his hand.\n오답 ▶ {1} connect {2} count {3} represent {4} matter", [('chase', '뒤쫓다'), ('calculate', '계산하다')], 5)
# [2024-1차-10]
T.flex('다음 단어 퍼즐을 풀었을 때, ⓐ~ⓕ의 글자를 순서대로 연결하여 완성한 단어는?', S7, Bx(
 '<b>DOWN</b> 1. an army or a country that enters another country by force in order to take control of it', '<b>ACROSS</b> 2. very wet or covered with water land in which plants, trees, etc. are growing',
 '<b>ACROSS</b> 3. to provide a place for somebody to live', '<b>ACROSS</b> 4. the substance that plants grow in', '',
 '1 (세로 7칸): □ □ □ □ ⓕ ⓑ □', '2 (가로 6칸): □ □ □ ⓐ □ □', '3 (가로 5칸): ⓓ ⓔ □ □ ⓑ', '4 (가로 5칸): □ □ □ ⓒ □',
 '※ 1의 넷째 칸 = 2의 셋째 칸, 1의 여섯째 칸 = 3의 다섯째 칸(ⓑ), 1의 일곱째 칸 = 4의 셋째 칸'),
 ['method', 'mature', 'medium', 'prefer', 'prison'],
 "이유 ▶ 1 invader(침략자) 2 swampy(늪 같은) 3 house(살 곳을 제공하다) 4 earth(흙) → ⓐ m ⓑ e ⓒ t ⓓ h ⓔ o ⓕ d = method\n오답 ▶ {1}·{2}·{3}·{4} 글자가 맞지 않음", [('invader', '침략자'), ('swampy', '늪 같은'), ('house', '(동) 살 곳을 제공하다'), ('earth', '흙')], 6)
# [2024-2차-2]
T.flex('다음 대화의 내용과 일치하지 <u>않는</u> 것은?', S8, Bx(
 'A: Emma, can you help me with this math problem?', 'B: Sure, what is it?', 'A: You have to move one stick to make this sum right. How could four minus five equal six?',
 'B: Oh, it\'s simple. You need to move one of the sticks in number four to make it eleven. Do you see what I mean?', 'A: Yes, now I get it. Eleven minus five equals six. How clever!', 'B: Thinking outside the box can be helpful sometimes.'),
 ['A는 B가 알려 준 방법을 한 번에 이해하지 못했다.', 'A가 완성한 식은 11 − 5 = 6이다.', '계산이 맞도록 막대를 옮겨야 한다.', '두 사람은 수학 문제에 대해 대화하고 있다.', 'B는 11이 되도록 4의 막대를 옮기라고 제안했다.'],
 "이유 ▶ Do you see what I mean? → Yes, now I get it. 바로 이해했다.\n오답 ▶ {1} Eleven minus five equals six ✔ {2} move one stick to make this sum right ✔ {3} math problem ✔ {4} move one of the sticks in number four to make it eleven ✔", [('equal', '(수가) ~와 같다'), ('think outside the box', '고정관념을 깨고 생각하다')], 5)
# [2022-1차-16]
T.flex('대화의 빈칸에 들어갈 말을 <보기>에서 골라 순서대로 바르게 배열한 것은?', S7, Bx(
 'Jinho: I think living in a jungle would be really fun.', 'Claire: I don\'t think so. ________', 'Jinho: I know. But ________ It would be cool to live there.', 'Claire: ________',
 'Jinho: I would explore it. Maybe I could make some animal friends.', 'Claire: Then where would you sleep? In a cave?', 'Jinho: No, I would stay in a tree house. ________', 'Claire: That makes sense.', '',
 '&lt;보기&gt; (A) What would you do in the jungle? (B) It would protect me from dangerous animals. (C) Jungle is a dangerous place full of wild animals. (D) I could get some exciting experience from jungle life.'),
 ['(C) − (D) − (A) − (B)', '(A) − (C) − (D) − (B)', '(B) − (D) − (A) − (C)', '(C) − (A) − (B) − (D)', '(D) − (C) − (A) − (B)'],
 "이유 ▶ 반대(I don't think so) → (C) 위험한 곳 / I know. But → (D) 신나는 경험 / (A) 정글에서 뭘 할래? → explore / tree house → (B) 위험한 동물로부터 지켜 줄 것", [('explore', '탐험하다'), ('protect', '보호하다')], 6)
# [2022-1차-15]
T.flex('가정법으로 표현한 문장 중 어법상 옳은 것은?', S7, '',
 ["Because you live so far away, we don't see you often. → If you didn't live so far away, we would see you often.", "I don't know his phone number. → I wish I know his phone number.",
  "Because she didn't drive carefully, she had an accident. → If she had driven carefully, she wouldn't have an accident.", "The baby isn't sleeping now. So I can't go out with you. → If the baby weren't sleeping now, I could go out with you.",
  "As I didn't turn in the research paper, I failed the class. → If I turned in the research paper, I wouldn't have failed the class."],
 "이유 ▶ 현재 사실의 반대 → If + 과거(didn't live), would + 동사원형(see) ✔\n오답 ▶ {1} I wish + 과거 → knew {2} 과거 사실의 반대 → wouldn't have had {3} 지금 자고 있지 않다 → If the baby were sleeping {4} If I had turned in", [('turn in', '제출하다')], 6)
# [2022-2차-4]
T.flex('어법상 옳지 <u>않은</u> 것은?', S8, '',
 ['The room was too small for our family to live in it.', 'He was too selfish to listen to us.', 'The woman was too angry to calm down.', "I was so disappointed that I couldn't see anyone.", "The medicine tastes so bitter that I can't take it."],
 "이유 ▶ too ~ to … 에서 to부정사의 목적어가 문장의 주어(The room)와 같으면 다시 쓰지 않는다 → live in (it 빼기)\n오답 ▶ {1}·{2} too + 형용사 + to부정사 ✔ {3}·{4} so + 형용사 + that ✔", [('selfish', '이기적인'), ('bitter', '쓴')], 6)
# [2022-1차-18]
T.flex('다음 글의 내용으로 옳은 것은?', S7, Bx(
 "If I lived in a <i>pueblo</i>, I would climb up a ladder to enter my house. There's a hidden opening on top of the house. If unwelcome visitors appeared, I would pull the ladder up to stop them from entering. "
 "The thick walls are made of earth, straw, and water. They would keep me cool in summer and warm in winter. The house has a flat roof. I would sometimes sleep up on the roof under the moon and stars."),
 ['People living in a pueblo can block unwanted guests.', 'There is no need to use equipment for getting into a pueblo.', 'A pueblo has a hole on its wall.', 'A pueblo is made of artificial materials.', 'A pueblo has a raised part on the roof.'],
 "이유 ▶ If unwelcome visitors appeared, I would pull the ladder up to stop them from entering. ✔\n오답 ▶ {1} 사다리(ladder)가 필요 {2} 구멍은 꼭대기(on top) {3} 흙·짚·물(자연 재료) {4} 평평한 지붕(flat roof)", [('unwelcome', '반갑지 않은'), ('artificial', '인공의')], 6)
# [2024-1차-12]
T.flex('[8~9] 다음 글의 밑줄 친 (가)~(라) 중 어법상 옳은 것을 고른 것은?', S7, VEN12,
 ['(나), (다)', '(가), (나)', '(가), (다)', '(나), (라)', '(다), (라)'],
 "이유 ▶ (나) be known as ~로 알려지다 ✔ (다) 가주어 it + for 의미상 주어 + to부정사 ✔\n오답 ▶ (가) rises와 병렬 → leaves (라) 강조된 주어 poles(복수) → support", [('tide', '조수'), ('swampy', '늪 같은'), ('install', '설치하다')], 6)
# [2024-1차-13]
T.fixed('위 글(8번)의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳은?', S7, GIV('However, I would be able to walk around the town through the raised walkways.'),
 ['ⓐ', 'ⓑ', 'ⓒ', 'ⓓ', 'ⓔ'], 1,
 "이유 ▶ 만조 때 거리에 물이 가득 찬다(ⓐ 앞) → However, 높은 보도로 걸어 다닐 수 있다. 물이 찬 거리와 대조\n오답 ▶ ⓑ~ⓔ는 집과 나무 기둥 이야기라 보도(walkways)가 이어질 수 없음", [('walkway', '보도, 통로'), ('raised', '높인')], 6)
# [2024-1차-16]
T.table('밑줄 친 ⓐ~ⓒ에 들어갈 표현을 바르게 연결한 것은?', S7, Bx(
 "A <i>tulou</i> is a huge round house in Fujian, China. I always have friends at home to play with. I sometimes hear my neighbor ⓐ [to call / calling] me to come over for tea or dinner. In a <i>tulou</i>, there are usually three to five floors. "
 "The first floor is used for cooking and eating. And people store food and tools on the second floor. My bedroom would be on the third or fourth floor.",
 "A <i>tulou</i> is like a village. The people ⓑ [living / lived] in a <i>tulou</i> mostly have the same family name. Some large <i>tulou</i> can house up to 50 families. They work together and share many things. ⓒ [Live / Living] together in one building makes them feel protected."),
 ['ⓐ', 'ⓑ', 'ⓒ'], [['calling', 'living', 'Living'], ['calling', 'living', 'Live'], ['to call', 'lived', 'Live'], ['to call', 'lived', 'Living'], ['calling', 'lived', 'Living']],
 "이유 ▶ ⓐ 지각동사 hear + 목적어 + -ing(또는 동사원형) ⓑ 사람들이 '사는' 능동 → 현재분사 living ⓒ 주어 자리 → 동명사 Living\n오답 ▶ to call(지각동사 뒤 to부정사 ❌), lived(수동 의미 ❌), Live(동사원형은 주어가 못 됨)", [('house', '(동) 수용하다'), ('protected', '보호받는')], 6)
# [2024-1차-21]
T.flex('<보기>의 ⓐ~ⓔ 중 어법상 틀린 것만을 있는 대로 고른 것은?', S7A, Bx(
 "When you visit Korea, you might wonder where ⓐ <u>can you</u> stay. Why don't you stay in a <i>hanok</i>? A <i>hanok</i> is a traditional Korean house. <i>Hanok</i> houses are mostly ⓑ <u>built</u> with natural materials such as wood, stone, straw, paper, and earth. "
 "These materials help you ⓒ <u>protect</u> your skin. In the cold winter, the <i>ondol</i> floors keep you ⓓ <u>warmly</u>. The doors in <i>hanok</i> are covered with thin paper. They make you ⓔ <u>staying</u> cool in the summer."),
 ['ⓐ, ⓓ, ⓔ', 'ⓐ, ⓔ', 'ⓑ, ⓒ', 'ⓓ, ⓔ', 'ⓑ, ⓒ, ⓓ'],
 "이유 ▶ ⓐ 간접의문문 '의문사 + 주어 + 동사' → where you can stay ⓓ keep + 목적어 + 형용사 → warm ⓔ 사역동사 make + 목적어 + 동사원형 → stay\n오답 ▶ ⓑ 한옥이 '지어지는' 수동 ✔ ⓒ help + 목적어 + 동사원형 ✔", [('traditional', '전통적인'), ('material', '재료')], 6)
# [2024-2차-10]
T.flex('다음 글의 ⓐ~ⓔ 중 어법상 옳은 것만을 있는 대로 고른 것은?', S8, Bx(
 'Pascal was doing his math homework in his room. He was struggling with graphs.',
 '"It\'s too hard to read and draw graphs. Why do I need these anyway? ⓐ <u>No one need graphs in real life.</u>" He put down his pen and picked up his favorite book, <i>Robin Hood</i>. ⓑ <u>He decided reading himself to sleep.</u> When he was about to open the book, he heard a voice. '
 'He looked up from the book to see who was talking. He couldn\'t believe his eyes. ⓒ <u>It was his dog, Manny, that was talking!</u>',
 '"Close your eyes and repeat after me. <i>Cogito ergo sum</i>," said Manny.', '"You can talk?"', '"Just repeat! <i>Cogito ergo sum</i>."',
 'Pascal closed his eyes and repeated the words. Suddenly, ⓓ <u>he heard men shouting</u>. When he opened his eyes, he saw soldiers on horses. They were chasing a man with arrows in his hand. The man saw Pascal and shouted.',
 '"ⓔ <u>It\'s too dangerous of you to stand there.</u> Come on." The man pulled Pascal onto his horse and rode into the woods.'),
 ['ⓒ, ⓓ', 'ⓐ, ⓑ', 'ⓐ, ⓒ', 'ⓑ, ⓓ, ⓔ', 'ⓒ, ⓓ, ⓔ'],
 "이유 ▶ ⓒ It ~ that 강조 구문 ✔ ⓓ 지각동사 hear + 목적어 + -ing ✔\n오답 ▶ ⓐ No one은 단수 → needs ⓑ decide + to부정사 → to read ⓔ dangerous의 의미상 주어 → for you", [('struggle with', '~으로 애를 먹다'), ('be about to', '막 ~하려고 하다')], 6)
# [2024-2차-17]
T.fixed('[13~14] 다음 글의 흐름에 맞지 <u>않는</u> 어휘는?', S8, ROB17, ['ⓐ', 'ⓑ', 'ⓒ', 'ⓓ', 'ⓔ'], 5,
 "이유 ▶ 탑 안에 군인이 많다 → '아무도 들어갈 수 없다' no one이어야 한다. anyone(누구나)은 흐름과 반대\n오답 ▶ ⓐ 구해 주었다 ⓑ 되찾다 ⓒ 충분한 ⓓ 그러나 → 모두 자연스러움", [('tax', '세금을 부과하다'), ('greedy', '욕심 많은')], 6)
# [2024-2차-18]
T.flex('위 글(13번)의 (A)에 들어갈 말로 가장 적절한 것은?', S8, '', ['too', 'very', 'much', 'many', 'enough'],
 "이유 ▶ too + 형용사 + to부정사 = 너무 ~해서 …할 수 없다 → too greedy to share\n오답 ▶ {1}·{2}·{3}은 to부정사와 '너무 ~해서 …할 수 없다'를 만들지 못함 {4} enough는 형용사 뒤(greedy enough to)", [('share', '나누다')], 6)
# [2022-2차-19]
T.flex('[15~16] 다음 글의 내용을 근거로 대답할 수 <u>없는</u> 질문은?', S8, ROB19,
 ['When was the best time to enter the tower?', 'What did Robin Hood want Pascal to do?', 'Who taxed the people too much?', 'Where did Pascal count the soldiers?', 'Why did Pascal draw the graph?'],
 "이유 ▶ Pascal이 들어갈 때를 말해 주었다(told Robin when ~)고만 나오고, 그때가 언제인지는 이 글에 없다.\n오답 ▶ {1} 돈을 되찾게 도와 달라 {2} the king {3} 나무 위(up in a tree) {4} 설명을 이해하기 쉽게 하려고", [('count', '세다'), ('explanation', '설명')], 6)
# [2022-2차-20]
T.flex('다음은 위 글(15번)에서 Pascal이 그린 그래프이다. 글의 맥락상 그래프에 대한 해석으로 바르지 <u>않은</u> 것은?', S8, Bx(GRAPH),
 ['The best time to enter the tower is between midnight and six in the morning.', 'There are five soldiers from midnight to six in the morning.', 'There are three soldiers at 11 a.m., and then there are eight soldiers at 5 p.m.',
  'The most dangerous time to get into the tower is between six in the evening and midnight.', 'Four times less soldiers work between six in the morning and noon than from six in the evening until midnight.'],
 "이유 ▶ 군인이 가장 적은 때(3명)는 6~12시 → 들어가기 가장 좋은 때는 아침 6시~정오. 자정~6시는 5명\n오답 ▶ {1} 0~6시 5명 ✔ {2} 11시 3명·17시 8명 ✔ {3} 18~24시 12명 최다 ✔ {4} 3명은 12명의 4분의 1 ✔", [('midnight', '자정'), ('noon', '정오')], 6)
# [2022-2차-7]
T.flex('다음 중 It ~ that 강조 구문으로 쓰인 것을 <보기>에서 있는 대로 고른 것은?', S8, Bx(
 'ⓐ It is true that he entered the university.', 'ⓑ It was at the bus stop that he saw her this morning.', 'ⓒ It was my father\'s car that I had to borrow to go to the job interview.',
 'ⓓ It was a mistake that I booked this hotel without checking any reviews.', 'ⓔ It was his girlfriend that he bought a bunch of flowers for her birthday.'),
 ['ⓑ, ⓒ, ⓔ', 'ⓐ, ⓑ', 'ⓐ, ⓓ', 'ⓐ, ⓑ, ⓔ', 'ⓒ, ⓓ, ⓔ'],
 "이유 ▶ It is/was와 that을 빼도 문장이 성립하면 강조 구문: ⓑ He saw her at the bus stop ⓒ I had to borrow my father's car ⓔ He bought a bunch of flowers for his girlfriend\n오답 ▶ ⓐ·ⓓ 가주어 it ~ 진주어 that절(that 뒤가 완전한 문장)", [('borrow', '빌리다'), ('book', '예약하다')], 6)
P1 = T.pts(); T.render()

# ═══════════════ 2회 ═══════════════
T = Test('2', '2회', '7과 8문항 · 8과 9문항', '중산중 기출', N, H=H)
# [2022-2차-2]
T.flex('다음의 어느 영어 의미에도 해당하지 <u>않는</u> 것은?', S8, Bx(
 '∘ to move your arm and hand from side to side', '∘ to express indirectly by an image, form, or model', '∘ wanting more money, power and food than you really need', '∘ to collect money so that the government can perform public services'),
 ['count', 'greedy', 'represent', 'tax', 'wave'],
 "이유 ▶ 차례로 wave(흔들다) / represent(나타내다) / greedy(욕심 많은) / tax(세금을 부과하다) → count(세다)는 해당 없음\n오답 ▶ {1}·{2}·{3}·{4} 풀이가 있음", [('represent', '나타내다'), ('wave', '(손을) 흔들다')], 5)
# [2024-1차-2]
T.flex('다음 대화의 내용과 일치하지 <u>않는</u> 것은?', S7, Bx(
 "A: Have you heard from Julia? She's traveling in Turkey, right?", 'B: Yes, she sent me some pictures. Do you want to see them?', 'A: Yes, please.', 'B: Okay, take a look.',
 "A: Oh, look at those cave houses! They look so unique, don't they? I wish I could try living there.", 'B: I like those balloons. They look so beautiful!', 'A: I think Turkey is a wonderful place to visit. I hope to visit there some day.', 'B: Me too!'),
 ['A는 터키를 방문할 의사가 없다.', 'Julia는 터키를 여행하고 있다.', 'A는 동굴 집에서 살아 보고 싶어 한다.', 'B는 사진에 있는 풍선들이 아름답다고 생각한다.', '두 사람은 Julia가 보낸 사진들을 보며 대화하고 있다.'],
 "이유 ▶ I hope to visit there some day. → 언젠가 가 보고 싶어 한다.\n오답 ▶ {1} She's traveling in Turkey ✔ {2} I wish I could try living there ✔ {3} They look so beautiful ✔ {4} take a look ✔", [('unique', '독특한'), ('cave', '동굴')], 6)
# [2024-2차-8]
T.flex('대화의 흐름상 (A)~(E)를 가장 적절하게 배열한 것은?', S8, Bx(
 'A: What is this graph about?', 'B: I did a survey on the kinds of pets my classmates have.', 'A: ______ / B: ______ / A: ______ / B: ______ / A: ______', 'B: Seven students have fish.', '',
 '(A) What about the rest?', '(B) What were the results?', '(C) What kind of pets do they have?', '(D) Well, ten students have dogs and three students have cats.', "(E) Eighty percent of the students have pets. Only five out of twenty-five students don't have pets."),
 ['(B) − (E) − (C) − (D) − (A)', '(A) − (D) − (C) − (E) − (B)', '(B) − (E) − (A) − (D) − (C)', '(C) − (D) − (A) − (E) − (B)', '(D) − (C) − (A) − (E) − (B)'],
 "이유 ▶ 결과는? (B) → 80%가 반려동물이 있다 (E) → 어떤 종류? (C) → 개 10, 고양이 3 (D) → 나머지는? (A) → 물고기 7", [('survey', '설문 조사'), ('the rest', '나머지')], 6)
# [2022-1차-17]
T.flex('다음 대화에서 언급되지 <u>않은</u> 것은?', S7, Bx(
 'B: Will it snow today?', 'G: I have no idea. Why are you waiting for snow, Taeho?', "B: I got a new sled as my birthday present. I can't wait to test it out.", 'G: Let me check the weather. Umm, there will be no snow for a while.',
 'B: How wonderful it would be to live in Alaska! Then I could go sledding all day!', 'G: No kidding! Alaska is a very cold place.', 'B: I think it would be fun. I want to build a snow house and stay there on vacation.', 'G: Living in a snow house sounds fun!'),
 ["The date when Taeho's vacation starts", 'The thing that Taeho got for his birthday', 'What Taeho wants to do when it snows', 'The place where Taeho wants to live', 'The house that Taeho wants to build'],
 "이유 ▶ 방학 때 눈집에 머물고 싶다고만 했고 방학이 언제 시작하는지는 없다.\n오답 ▶ {1} 새 썰매 {2} 썰매를 시험해 보기 {3} 알래스카 {4} 눈집", [('sled', '썰매'), ('test out', '시험해 보다')], 5)
# [2022-2차-5]
T.flex('다음 대화의 내용으로 옳은 것은?', S8, Bx(
 'Mina: Henry, what are you doing?', "Henry: I'm writing an article about students' favorite snacks. I'm worried about their health.", 'Mina: Why?',
 'Henry: Well, I surveyed 100 students and the results show that eighty percent of the students liked pizza and fried chicken for snacks. Do you see what I mean?',
 'Mina: Oh, I get it. Students really like fast food. What else did they like?', 'Henry: Twelve percent of the students chose chocolate cake as their favorite.', 'Mina: Wow, students should really try to eat healthier snacks!'),
 ['Most of the students liked fast food as their snacks.', "The topic of Henry's article is how snacks harm students' health.", 'Less than half of the students liked pizza and fried chicken.', 'The 20 percent of the students liked chocolate cake.', 'Mina thinks students should stop eating snacks.'],
 "이유 ▶ 80%가 피자·치킨(패스트푸드)을 좋아했다 → 대부분 ✔\n오답 ▶ {1} 주제는 좋아하는 간식 {2} 80%(절반 넘음) {3} 12% {4} 더 건강한 간식을 먹어야 한다(끊으라는 말 아님)\n수정 ▶ 원본 ③ The most students → Most of the students (어법만 다듬음)", [('article', '기사, 글'), ('survey', '설문 조사하다')], 6)
# [2024-1차-8]
T.table('빈칸에 들어갈 말을 바르게 연결한 것은?', S7, Bx(
 '∘ What would you do if you ___(A)___ in my shoes? (네가 내 입장에 있다면 무엇을 하겠니?)', '∘ If I ___(B)___ enough money, I could have afforded to buy a car. (만약 내가 돈이 충분히 있었다면, 나는 차를 살 여유가 있었을 것이다.)'),
 ['(A)', '(B)'], [['were', 'had had'], ['were', 'had'], ['had been', 'have had'], ['have been', 'had'], ['have been', 'have had']],
 "이유 ▶ (A) 현재 사실의 반대(가정법 과거) → were (B) 과거 사실의 반대(가정법 과거완료: could have afforded) → If + had p.p. = had had", [('in one\'s shoes', '~의 입장에서'), ('afford', '~할 여유가 있다')], 6)
# [2022-1차-19]
T.flex('다음 중 어법상 옳은 것은?', S7, '',
 ['I kept the windows closed all day.', 'I tried to keep my dog quietly.', 'She kept the front door unlocking.', 'His accident made people shocking.', 'His jokes make me to laugh all the time.'],
 "이유 ▶ keep + 목적어 + 과거분사(창문이 '닫힌' 상태) ✔\n오답 ▶ {1} 목적격 보어는 형용사 → quiet {2} 문이 '잠기지 않은' → unlocked {3} 사람들이 '충격받은' → shocked {4} 사역동사 make + 동사원형 → laugh", [('unlock', '잠금을 풀다')], 6)
# [2024-1차-4]
T.flex('다음 글에서 푸에블로에 대한 내용으로 옳은 것은?', S7, Bx(
 "When I live in a <i>pueblo</i>, I climb up a ladder to enter my house. There's a hidden opening on top of the house. If unwelcome visitors appear, I can pull the ladder up to stop them from entering. "
 "The thick walls are made of earth, straw, and water. It is cool in summer and warm in winter because of the thick walls. The house has a flat roof. I would sometimes sleep up on the roof under the moon and stars."),
 ['It is possible to pull the ladder up.', 'There is a door behind the house.', 'People use wood, straw and water to make walls.', 'The house is cool in summer but cold in winter.', 'The house has a round roof.'],
 "이유 ▶ I can pull the ladder up ✔\n오답 ▶ {1} 꼭대기의 숨겨진 출입구 {2} 흙(earth)·짚·물 {3} 겨울엔 따뜻함 {4} 평평한 지붕(flat roof)", [('hidden', '숨겨진'), ('straw', '짚')], 6)
# [2022-1차-22]
T.flex('다음 글을 읽고 대답할 수 <u>없는</u> 질문은?', S7, Bx(
 "A <i>tulou</i> is a huge round house in China. In a <i>tulou</i>, there are usually three to five floors. The first floor is used for cooking and eating. And people store food and tools on the second floor. Do you wonder where I would sleep? My bedroom would be on the third or fourth floor.",
 "A <i>tulou</i> is like a village. The people living in a <i>tulou</i> mostly have the same family name. Some large <i>tulou</i> can house up to 50 families. They work together and share many things. Living together in one building keeps them safe."),
 ['How do the people in a tulou share things equally?', 'What shape does a tulou look like?', 'How many floors does a tulou have?', 'What is each floor in a tulou used for?', 'What is the benefit of living together in a tulou?'],
 "이유 ▶ 많은 것을 함께 나눈다(share many things)고만 했지 '어떻게 똑같이' 나누는지는 없다.\n오답 ▶ {1} 둥근(round) {2} 3~5층 {3} 1층 요리·식사, 2층 저장, 3·4층 침실 {4} 안전하게 지켜 준다", [('store', '저장하다'), ('benefit', '이점')], 6)
# [2022-1차-23]
T.table('다음 글을 읽고 빈칸 (A)~(C)에 각각 들어갈 말로 가장 적절한 것은?', S7, Bx(
 "Venice is known as the \"floating city\" whose ground is not solid because it is covered with wet land. The old Venetians decided to live there to keep themselves safe from invaders. But it was not easy for them to build their homes on this swampy surface. "
 "So they installed more than 10 million wooden poles in the ground. Thanks to these wooden poles, the city does not sink.", '',
 'The old Venetians wanted to ___(A)___ themselves from invaders. So they decided to build the houses on water. Because Venice doesn\'t have a ___(B)___ surface, the Venetians installed many wooden poles in the ground to ___(C)___ their homes from falling down.'),
 ['(A)', '(B)', '(C)'], [['protect', 'hard', 'prevent'], ['save', 'weak', 'support'], ['hurt', 'strong', 'stop'], ['defend', 'soft', 'keep'], ['attack', 'flat', 'support']],
 "이유 ▶ (A) 침략자로부터 자신을 지키다 protect (B) 땅이 단단하지 않다(not solid) → hard surface가 없다 (C) prevent A from -ing A가 ~하지 못하게 하다\n오답 ▶ soft(부드러운) 표면이 없다는 반대 / support·save·attack은 from과 맞지 않음", [('solid', '단단한'), ('sink', '가라앉다')], 6)
# [2024-1차-17]
T.table('밑줄 친 ⓐ~ⓒ에 들어갈 표현을 바르게 연결한 것은?', S7A, Bx(
 "When you walk down a street in the village of the Ndebele in South Africa, you can see houses with many unique patterns and styles. Each house tells a different story. ___ⓐ___ stories might be about neighbors' babies. ___ⓑ___ express personal opinions.",
 "A long time ago, the Ndebele were at war with the Boers. When the Boers invaded their land, the Ndebele painted their houses with many colorful symbols. ___ⓒ___, their enemies couldn't understand what they were secretly communicating to each other. "
 "The symbols expressed feelings such as sadness. Those symbols were handed down from mothers to daughters."),
 ['ⓐ', 'ⓑ', 'ⓒ'], [['Some', 'Others', 'So'], ['Another', 'Others', 'Or'], ['One', 'Another', 'Moreover'], ['The other', 'One', 'In fact'], ['Some', 'One', 'However']],
 "이유 ▶ ⓐⓑ 여러 이야기 중 '어떤 것들은 ~, 다른 것들은 …' = Some ~ Others ⓒ 상징으로 칠했다 → 그래서(So) 적들이 몰랐다\n오답 ▶ Another·One은 단수 / However·In fact·Moreover·Or는 앞뒤 관계와 맞지 않음", [('pattern', '무늬'), ('hand down', '물려주다')], 6)
# [2022-2차-6]
T.table('다음 글을 읽고 빈칸 (A)~(C)에 각각 들어갈 말로 가장 적절한 것은?', S8, Bx(
 'Pascal was doing his math homework in his room. He was struggling with graphs. "It\'s too hard to read and draw graphs. Why do I need these anyway? No one needs graphs in real life." He put down his pen and picked up his favorite book, <i>Robin Hood</i>. '
 'He decided to read himself to sleep. When he was about to open the book, he heard a voice. He looked up from the book to see who was talking. He couldn\'t believe his eyes. It was his dog, Manny, who was talking!',
 '"Close your eyes and repeat after me. <i>Cogito ergo sum</i>," said Manny.', '"You can talk?"', '"Just repeat! <i>Cogito ergo sum</i>."', 'Pascal closed his eyes and repeated the words even though he didn\'t understand what they meant.', '',
 "Pascal who was ___(A)___ at graphs didn't think that they were ___(B)___ in real life. His dog, Manny, who could talk made him ___(C)___ the words he didn't understand."),
 ['(A)', '(B)', '(C)'], [['not good', 'useful', 'repeat'], ['bad', 'useful', 'stop'], ['not good', 'useless', 'talk'], ['good', 'useless', 'say'], ['good', 'useful', 'imitate']],
 "이유 ▶ (A) 그래프로 애를 먹었다 → 잘하지 못했다 not good (B) 실생활에 필요 없다고 생각 → 유용하다고(useful) 생각하지 않았다 (C) Manny가 따라 말하게 했다 → repeat\n오답 ▶ useless는 didn't think와 겹쳐 뜻이 반대가 됨 / stop·talk 등은 내용과 다름", [('struggle with', '~으로 애를 먹다'), ('useful', '유용한')], 6)
# [2022-2차-15]
T.fixed('[13~14] 윗글의 밑줄 친 ⓐ~ⓔ 중 내용상 가리키는 것이 <u>다른</u> 것은?', S8, ROB15, ['ⓐ', 'ⓑ', 'ⓒ', 'ⓓ', 'ⓔ'], 1,
 "이유 ▶ ⓐ Pascal이 눈을 떴다 → Pascal\n오답 ▶ ⓑ~ⓔ 화살을 든 남자(= Robin Hood)의 손·말", [('chase', '뒤쫓다'), ('arrow', '화살')], 6)
# [2022-2차-16]
T.flex('위 글(13번)의 내용과 일치하는 것은?', S8, '',
 ['Pascal은 감사의 의미로 Robin Hood를 돕고 싶어 한다.', '군인들이 Pascal을 쫓고 있었다.', 'Pascal이 한 남자에게 위험하다고 알려 주었다.', 'Robin Hood는 자신이 책에 나온 사람이라고 소개했다.', 'Robin Hood는 Pascal이 여기에 온 이유를 알려 주었다.'],
 "이유 ▶ Thank you very much for saving my life, so I'd like to do anything for you. ✔\n오답 ▶ {1} 화살을 든 남자를 쫓았다 {2} 남자가 Pascal에게 위험하다고 했다 {3} 책이 아니라 셔우드 숲의 Robin Hood {4} Pascal도 이유를 모른다(I don't know why I'm here)", [('forest', '숲')], 6)
# [2024-2차-19]
T.table('밑줄 친 ⓐ~ⓒ에 들어갈 표현을 바르게 연결한 것은?', S8, Bx(
 "Robin and Pascal hid up in a tree and ⓐ [counted / caught] the soldiers one by one.", "\"There are five soldiers from midnight to six in the morning. Next, there are three soldiers until noon, and then there are eight soldiers until six in the evening. ⓑ [In short / Lastly], there are twelve soldiers until midnight. So, you should go inside between six in the morning and noon.\"",
 "\"What? I don't get it.\"", "Pascal thought for a moment. 'Hmm... A graph might make this ⓒ [easily / easier] to understand.' Pascal drew a graph and showed it to Robin."),
 ['ⓐ', 'ⓑ', 'ⓒ'], [['counted', 'Lastly', 'easier'], ['counted', 'In short', 'easily'], ['counted', 'Lastly', 'easily'], ['caught', 'In short', 'easily'], ['caught', 'Lastly', 'easier']],
 "이유 ▶ ⓐ 군인 수를 하나씩 '셌다' ⓑ 시간대를 차례로 말하고 마지막 → Lastly ⓒ make + 목적어 + 형용사 보어 → easier\n오답 ▶ caught(잡았다)는 흐름과 다름 / In short(요컨대)는 요약할 때 / easily는 부사라 보어 자리에 못 씀", [('one by one', '하나씩'), ('lastly', '마지막으로')], 6)
# [2024-2차-21]
T.flex('다음 중 어법상 틀린 것을 <보기>에서 고른 것은?', S8, Bx(
 '(A) It was Andy that I talked to yesterday.', '(B) It was to catch a bus that Frank was running.', '(C) It is to be a soccer player that my future dream is.', '(D) It is my mom who is the tallest person in my family.', '(E) It was at the bus stop which I saw Mr. Kim this morning.'),
 ['(C), (E)', '(A), (C)', '(B), (C)', '(B), (D)', '(D), (E)'],
 "이유 ▶ (C) 보어(to be a soccer player)는 It ~ that으로 강조하지 않는다(My future dream is to be ~) (E) 장소 부사구 강조 → which가 아니라 that\n오답 ▶ (A) 사람 목적어 강조 ✔ (B) 목적의 부사구 강조 ✔ (D) 사람 주어 강조 → who도 가능 ✔", [('emphasize', '강조하다')], 6)
# [2022-2차-17]
T.flex('어법상 옳은 것만을 <보기>에서 있는 대로 고른 것은?', S8, Bx(
 'ⓐ He did take a walk in the park last night.', 'ⓑ It was I that she gave a chocolate box.', 'ⓒ This time, she is not going to help him, however.', "ⓓ It was because I didn't feel very well that I didn't go to school today."),
 ['ⓐ, ⓒ, ⓓ', 'ⓐ, ⓑ', 'ⓑ, ⓓ', 'ⓒ, ⓓ', 'ⓐ, ⓑ, ⓒ'],
 "이유 ▶ ⓐ 동사 강조 did + 동사원형 ✔ ⓒ however는 문장 끝에도 올 수 있다 ✔ ⓓ 이유 부사절 강조 It was because ~ that ✔\n오답 ▶ ⓑ 목적어(그녀가 초콜릿 상자를 준 '나')는 목적격 → It was me that she gave a chocolate box (to)", [('however', '그러나')], 6)
P2 = T.pts(); T.render()
print('pts', P1, P2)
