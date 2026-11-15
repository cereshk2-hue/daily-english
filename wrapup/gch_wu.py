# 11/15 중3 지학사(민찬규) 7·8과 기출 마무리 1·2회 (7과·8과 섞음)
# 원본: 선생님이 주신 학교 기출 hwp 3개(work/gch: 2020 구포중 · 2022 도개중 · 2024 한영중). 7·8과 문항만 골라 검수 후 정리.
# (2020의 4·5과, 2022의 부교재 문항은 범위 밖이라 뺌. 서술형은 빼고 객관식만)
from wu_nrt7 import *
H = ('7·8과 기출 마무리', '중3 영어 지학사(민찬규) Lesson 7~8', '학교 기출(2020 · 2022 · 2024)', 'gch')
B = lambda *ls: BOX('<br>'.join(ls))
S7, S8 = '7과', '8과'
NOTICE = '최근 학교 기출(2020 · 2022 · 2024) 중 7·8과 문항을 골라 7과와 8과를 섞었어요. 원본의 정답 오류·문항 오류는 고쳤어요(해설 끝 수정 ▶).'
PUE = ("If I lived in a pueblo, I would climb up a ladder to enter my house. There's a hidden opening on top of the house. If unwelcome visitors appeared, I would pull the ladder up to stop them from entering. "
       "The thick walls are made of earth, straw, and water. They would keep me cool in summer and warm in winter. The house has a flat roof. I would sometimes sleep up on the roof under the moon and stars.")
VEN2 = ("Venice is known as the \"floating city.\" In Venice, there are many colorful houses on the water. You may wonder how and why they built the houses on the water. "
        "The old Venetians decided to live there to keep themselves safe from invaders. But it was not easy for them to build their homes on this swampy surface. "
        "So they installed more than 10 million wooden poles in the ground. It is these wooden poles that support Venice to this day.")
VEN = ("If I lived in Venice, I would take a gondola to school every morning. Venice has 118 small islands. On weekends, I would travel from island to island by a vaporetto, a water bus. "
       "At high tide, the water from the Adriatic Sea often rises and leaves the streets full of water. However, I would be able to walk around the town through the raised walkways.")
TUL = ("If I lived in a tulou, a huge round house in Fujian, China, I would always have friends at home to play with. I would sometimes hear my neighbor calling me to come over for tea or dinner. "
       "In a tulou, there are usually three to five floors. The first floor is used for cooking and eating. And people store food and tools on the second floor. Do you wonder where I would sleep? My bedroom would be on the third or fourth floor. "
       "A tulou is like a village. The people living in a tulou mostly have the same family name. Some large tulou can house up to 50 families. They work together and share many things.")
P4 = ('Robin and Pascal hid up in a tree and counted the soldiers one by one. "There are five soldiers from midnight to six in the morning. Next, there are three soldiers until noon, and then there are eight soldiers until six in the evening. '
      'Lastly, there are twelve soldiers until midnight. So, you should go inside between six in the morning and noon." "What? I don\'t get it." Pascal thought for a moment. \'Hmm... A graph might make this easier to understand.\' Pascal drew a graph and showed it to Robin. '
      '"Look, the most dangerous time is between six in the evening and midnight. Four times more soldiers work at that time than from six in the morning until noon. Do you see what I mean?" "Aha! I get it now. Thank you so much, Pascal!" '
      '"You\'re welcome. Now I realize the importance of graphs. No one can say that we don\'t need them anymore."')
TURKEY = B('A: Have you heard from Julia? She\'s traveling in Türkiye, right?', 'B: Yes, she sent me some pictures. Do you want to see them?', 'A: Yes, please.', 'B: Okay, take a look.',
           "A: Oh, look at those cave houses! They look so unique, don't they? I wish I could try living there.", 'B: I like those balloons. They look so beautiful!', 'A: I think Türkiye is a wonderful place to visit. I hope to visit there some day.', 'B: Me too!')

# ═══════════════ 1회 ═══════════════
T = Test('1', '1회', '7과 · 8과 섞음', '7~8과 학교 기출', NOTICE, H=H)
# [2024-1]
T.flex('밑줄 친 부분의 우리말 뜻이 바르지 <u>않은</u> 것은?', '7~8과', '',
 ['He fell off a <u>ladder</u> and hurt himself. (사다리를 타다)', "It's hard to <u>build muscle</u> in a short time. (근육을 키우다)", '<u>What matters most</u> is that you keep exercising. (가장 중요한 것)',
  '<u>Thinking outside the box</u> can be helpful sometimes. (새로운 관점에서 생각하기)', 'If I meet Snow White, I will tell her that the apple is <u>poisonous</u>. (독이 있는)'],
 "이유 ▶ fell off a ladder = 사다리에서 떨어졌다. ladder는 '사다리'라는 명사일 뿐 '사다리를 타다'가 아니다.\n오답 ▶ {1}·{2}·{3}·{4} 뜻이 바르다", [('fall off', '~에서 떨어지다')], en=True)
# [2024-2]
T.flex('빈칸 (1)~(4)에 들어갈 단어를 순서대로 짝지은 것은?', S8, B('(1) ______ for your leader!', '(2) Time and ______ wait for no man.', '(3) How could four minus five ______ six?', '(4) I did a ______ on the kinds of pets my classmates have.', '', '(A) repeat (B) equal (C) survey (D) vote (E) tide (F) plant'),
 ['(D) − (E) − (B) − (C)', '(B) − (A) − (C) − (F)', '(B) − (E) − (D) − (C)', '(D) − (B) − (E) − (C)', '(D) − (C) − (B) − (F)'],
 "이유 ▶ (1) 지도자에게 투표하라 vote (2) 세월(시간과 조수)은 사람을 기다리지 않는다 tide (3) 4 빼기 5가 어떻게 6이 될 수 있지? equal (4) 반 친구들이 기르는 애완동물에 대해 조사했다 survey", [('equal', '(수가) ~와 같다'), ('survey', '설문 조사')])
# [2024-3]
T.flex('다음 대화에 대한 설명으로 어색한 것은?', S8, B('A: Mason, how was the (A) ______?', "B: It was bad. I didn't win.", 'A: How come?', 'B: Yura won. Over sixty percent of the students voted for her.', "A: Well, you tried your best and that's what matters.", 'B: I guess so. I have learned many things while running for class president.', "A: I'm really proud of you.", 'B: Thanks, Dad.'),
 ['Yura는 반장 선거에서 60% 미만을 득표하여 당선되었다.', '빈칸 (A)에 들어갈 단어는 election이다.', 'Mason의 아버지는 Mason을 자랑스러워한다.', 'Mason은 반장 선거에 출마했지만 당선되지 못했다.', 'Mason 말고도 반장 선거에 나간 학생으로 Yura가 있었다.'],
 "이유 ▶ Over sixty percent(60% 넘게)가 Yura에게 투표 → 60% 미만이 아니다.\n오답 ▶ {1} 선거(election) ✔ {2} I'm really proud of you ✔ {3} running for class president, didn't win ✔ {4} ✔", [('run for', '~에 출마하다')])
# [2024-4]
T.flex('다음 문장을 순서대로 바르게 배열한 것은?', S7, B('(A) And others share their houses with many people.', '(B) Different people live in different houses.', '(C) Some use ladders to enter their houses.', '(D) Others live in houses on the water.'),
 ['(B) − (C) − (D) − (A)', '(A) − (B) − (D) − (C)', '(B) − (A) − (D) − (C)', '(B) − (D) − (C) − (A)', '(D) − (C) − (B) − (A)'],
 "이유 ▶ 다양한 사람이 다양한 집에 산다 → Some ~ → Others ~ → And others ~\n수정 ▶ 원본에 [8과]로 적혀 있었지만 7과 본문", [])
# [2024-5]
T.flex('다음 대화를 읽고 바로 답할 수 있는 질문은?', S7, TURKEY,
 ['What do both A and B hope for in the future?', 'How long is Julia traveling in Türkiye?', 'What activities did Julia want to do before leaving?', 'Will A and B travel to Türkiye together in the future?', 'Are there any other places in Türkiye that A and B are interested in?'],
 "이유 ▶ A: I hope to visit there some day. B: Me too! → 둘 다 언젠가 튀르키예에 가 보고 싶어 한다.\n오답 ▶ {1}·{2}·{4} 나오지 않음 {3} 함께 갈지는 모름", [])
# [2024-6]
T.flex('다음 대화의 내용과 일치하는 것은?', S7, B('A: Will it snow today?', 'B: I have no idea. Why are you waiting for snow, Taeho?', "A: I got a new sled for my birthday. I can't wait to test it out.", 'B: Let me check the weather. Umm, there will be no snow for a while.',
 'A: I wish I could live in Alaska. Then I could go sledding all day!', 'B: No kidding! Alaska is a very cold place.', 'A: I think it would be fun. I want to build a snow house and stay there on vacation.', 'B: Living in a snow house sounds fun!'),
 ['A is looking forward to the chance to try out the sled.', 'B is planning a trip to Alaska with A.', "A bought a new sled for B's birthday.", 'A prefers to go sledding in a warm climate.', 'B says that snow would definitely fall today.'],
 "이유 ▶ I can't wait to test it out(빨리 시험해 보고 싶다) ✔\n오답 ▶ {1} 여행 계획 없음 {2} 자기 생일 선물 {3} 추운 알래스카 {4} 당분간 눈이 없다", [('sled', '썰매')])
# [2024-9]
T.flex('다음 글의 내용과 일치하는 것은?', S7, B(VEN2),
 ['The old Venetians built their homes on the water for safety from invaders.', 'Venice has no colorful houses on the water.', 'The wooden poles used for support were made of metal.', 'Venice was built not on a swampy surface, but on solid ground.', 'The wooden poles were removed after the houses were built.'],
 "이유 ▶ to keep themselves safe from invaders ✔\n오답 ▶ {1} many colorful houses {2} wooden(나무) {3} swampy surface(늪지) {4} 지금까지 받침(to this day)\n수정 ▶ 원본 ⑤(곤돌라 이야기)는 이 지문에 없는 내용이라 다른 선택지로 바꿈", [])
# [2024-12]
T.flex('글의 흐름상 (A)~(C)에서 적절한 표현을 고른 것은?', S7, B("If I lived in a pueblo, I would (A) [climb up / climb down] a ladder to enter my house. There's a hidden opening on top of the house. If unwelcome visitors appeared, I would pull the ladder up to stop them from (B) [entering / entered]. ... The house has a (C) [flat roof / pointed roof]. I would sometimes sleep up on the roof under the moon and stars."),
 ['climb up − entering − flat roof', 'climb up − entered − pointed roof', 'climb down − entered − pointed roof', 'climb down − entered − flat roof', 'climb down − entering − pointed roof'],
 "이유 ▶ (A) 꼭대기 출입구로 → 올라가다 (B) from + 동명사 (C) 지붕 위에서 잠 → 평평한 지붕", [])
# [2024-13]
T.flex('다음 글을 바르게 이해한 학생들만 고른 것은?', S7, B(PUE, '', '지아: 글쓴이가 과거에 푸에블로에 가 본 경험을 떠올리며 쓴 글이구나.', '재이: 푸에블로의 두꺼운 벽은 흙, 지푸라기, 물로 만들어졌대.', '민우: 글쓴이는 멕시코에 가서 집 꼭대기에 숨겨진 구멍을 찾아봤나 봐.', '하나: 글쓴이는 때때로 달과 별 아래 지붕 위에서 잠을 잘 거라고 상상하고 있어.'),
 ['재이, 하나', '지아, 재이', '지아, 민우', '지아, 하나', '재이, 민우'],
 "이유 ▶ If I lived ~(가정법 과거) = 상상하는 글. 재이 ✔ 하나 ✔\n오답 ▶ 지아·민우: 실제 경험이 아니라 상상", [])
# [2024-14]
T.flex('다음 중 7과 푸에블로 본문에 쓰인 단어를 영어로 풀이한 것은?', S7, '',
 ['a device used for climbing that has two long pieces of wood, metal, or rope with a series of steps between them', 'to fix equipment or furniture into position so that it can be used', 'a passage or path for walking along, often outside and raised above the ground',
  'to put something that is not being used in a place where it can be kept safely', 'the regular upward and downward movement of the level of the ocean'],
 "이유 ▶ ladder(사다리)의 풀이 → 푸에블로 글에 나옴.\n오답 ▶ {1} install {2} walkway {3} store {4} tide – 모두 베니스·토루 글의 단어", [])
# [2024-17]
T.flex('빈칸 ⓐ~ⓔ에 들어갈 단어를 순서대로 묶은 것은?', S8, B('Pascal was doing his math homework in his room. He was struggling ⓐ ______ graphs. "It\'s too hard to read and draw graphs. Why do I need these anyway? No one needs graphs ⓑ ______ real life." He put ⓒ ______ his pen and picked up his favorite book, Robin Hood. ... He looked up ⓓ ______ the book to see who was talking. ... "Close your eyes and repeat ⓔ ______ me."'),
 ['with − in − down − from − after', 'with − off − from − out − after', 'in − up − about − down − behind', 'in − after − from − down − before', 'from − with − after − during − down'],
 "이유 ▶ struggle with(~으로 고생하다) / in real life(실생활에서) / put down(내려놓다) / look up from(~에서 고개를 들다) / repeat after(~을 따라 말하다)", [])
# [2024-18]
T.flex('다음 글의 Pascal과 Manny에 대한 설명으로 옳지 <u>않은</u> 것은?', S8, B('Pascal was doing his math homework in his room. He was struggling with graphs. "It\'s too hard to read and draw graphs." He put down his pen and picked up his favorite book, Robin Hood. He decided to read himself to sleep. When he was about to open the book, he heard a voice. ... It was his dog, Manny, who was talking!'),
 ['Manny는 책을 읽을 수 있고 사람처럼 말도 할 수 있다.', 'Manny는 Pascal과 서로 아는 사이이다.', 'Pascal은 그래프를 읽고 그리는 것이 어렵다고 생각한다.', 'Pascal이 책을 읽으려고 할 때 목소리가 들렸다.', 'Robin Hood 책을 읽으며 잠들려고 한 사람은 Pascal이다.'],
 "이유 ▶ Manny가 말을 한 것은 맞지만, 책을 읽을 수 있다는 말은 없다.\n오답 ▶ {1} his dog ✔ {2} too hard ✔ {3} about to open ~ heard a voice ✔ {4} read himself to sleep ✔", [])
# [2024-23]
T.flex('다음 중 어법상 바른 것만 고른 것은?', S8, B('ⓐ This soup is too salty for me to eat.', 'ⓑ Jamie was so strongly that she could lift the boxes.', "ⓒ Nayoon is so angrily that she can't talk with me.", 'ⓓ The character is too mean to be liked by others.', 'ⓔ The cat is too old to climb up the tree.'),
 ['ⓐ, ⓓ, ⓔ', 'ⓐ, ⓑ, ⓒ', 'ⓐ, ⓑ, ⓓ', 'ⓑ, ⓒ, ⓔ', 'ⓒ, ⓓ, ⓔ'],
 "이유 ▶ ⓑ strongly → strong ⓒ angrily → angry (be동사 뒤 보어는 형용사). ⓐ·ⓓ·ⓔ too ~ to ✔\n수정 ▶ 원본 ⓑ의 철자 오류(storngly)를 고침", [])
# [2024-24]
T.fixed('밑줄 친 ⓐ~ⓔ 중 어법상 어색한 부분이 있는 것은?', S8, B(
 'Suddenly, ⓐ <u>Pascal heard men shouting</u>. ... ⓑ <u>The man pulled Pascal onto his horse and rode into the woods</u>. ... "Well, ⓒ <u>can you help us get back the money that the king taken from the people?</u> He taxed them too much. ⓓ <u>He is too greedy to share with the people</u>, so they don\'t have enough money to buy food. ⓔ <u>I want to help them to get their money back</u>."'),
 ['ⓐ', 'ⓑ', 'ⓒ', 'ⓓ', 'ⓔ'], 3,
 "이유 ▶ 관계대명사절의 동사 자리 → the king took(과거). taken(과거분사)만으로는 동사가 될 수 없다.\n오답 ▶ ⓐ hear + 목적어 + -ing ✔ ⓑ ✔ ⓓ too ~ to ✔ ⓔ help + 목적어 + (to) 동사원형 ✔", [])
# [2024-25]
T.flex("Pascal이 'But first, can you take me to the tower? I need to count the number of soldiers.'라고 말한 이유로 가장 적절한 것은?", S8, '',
 ['He wants to know how many soldiers are there to make a plan.', 'He thinks the soldiers might be friendly.', 'He wants to tell the soldiers that he will hide in the tree.', 'He is just curious about the tower and wants to look around.', 'He wants to make sure they have enough time to meet the soldiers.'],
 "이유 ▶ '해결책이 있다' → 계획을 세우려고 군인 수를 세어야 한다.\n오답 ▶ {1}·{2}·{3}·{4} 근거 없음", [])
# [2024-28]
T.flex('다음 글의 내용에 대해 T/F를 표시했을 때, 잘못 표시된 것은?', S8, B(P4),
 ['Pascal realized how useful graphs can be after showing one to Robin. → F', 'The most dangerous time to enter the tower is between six in the morning and noon. → F', "Robin Hood didn't understand the soldiers' schedule until Pascal drew the graph. → T",
  'The safest time to enter the tower is between six in the evening and midnight. → F', 'There are eight soldiers between midnight and six in the morning. → F'],
 "이유 ▶ Now I realize the importance of graphs → T인데 F로 표시됨.\n오답 ▶ {1} 가장 위험한 때는 오후 6시~자정 → F ✔ {2} I get it now → T ✔ {3} 가장 안전한 때는 오전 6시~정오 → F ✔ {4} 5명 → F ✔", [])
# [2020-A]
T.fixed('다음 글의 밑줄 친 ⓐ~ⓔ 중 글의 흐름상 어색한 것은?', S7, B(
 'Venice is known as the "floating city." ⓐ <u>In Venice, there are many colorful houses on the water.</u> ⓑ <u>You may wonder how and why they built the houses on the water.</u> The old Venetians decided to live there to keep themselves safe from invaders. '
 'But it was not easy for them to build their homes on this swampy surface. ⓒ <u>So they installed more than 10 million wooden poles in the ground.</u> ⓓ <u>Many visitors are inspired by the woods in the city.</u> ⓔ <u>It is these wooden poles that support Venice to this day.</u>'),
 ['ⓐ', 'ⓑ', 'ⓒ', 'ⓓ', 'ⓔ'], 4,
 "이유 ▶ 나무 기둥 설치 → 바로 이 기둥들이 받친다. '관광객이 도시의 숲에 영감을 받는다'는 흐름과 관계없다.", [])
# [2020-B]
T.flex('[ ] 안의 단어를 바르게 배열한 것은?', S7, B('... And people store food and tools on the second floor. [ sleep / would / wonder / I / do / where / you ] ? My bedroom would be on the third or fourth floor.'),
 ['Do you wonder where I would sleep?', 'Do you wonder where would I sleep?', 'Do I sleep where you would wonder?', 'Where I do wonder you would sleep?', 'Where you sleep do I would wonder?'],
 "이유 ▶ Do you wonder ~?(궁금하니?) + 간접의문문(의문사 + 주어 + 동사) where I would sleep", [])
# [2022-C]
T.flex('빈칸 (A)~(C)에 들어갈 말로 알맞은 것은?', S7, B('At high (A) ______, the water from the Adriatic Sea often rises and leaves the streets full of water. ... In Venice, there are (B) ______ colorful houses on the water. ... The old Venetians decided to live there to keep themselves (C) ______ from invaders.'),
 ['tide − many − safe', 'tide − many − safely', 'stem − much − safely', 'tide − much − safe', 'stem − many − safely'],
 "이유 ▶ (A) at high tide(만조 때) (B) 셀 수 있는 복수명사 houses → many (C) keep + 목적어 + 형용사 → safe", [])
# [2022-D]
T.flex('다음 대화의 내용으로 가장 적절한 것은?', S7, B('휘빈: 민우, we need to start our project on our dream country to visit.', "민우: That's right. Which country do you want to visit?", '휘빈: In my case, I want to visit Spain.', '민우: What would you do if you visited Spain?',
 "휘빈: I'm interested in buildings. So I would go see La Sagrada Familia.", "민우: Isn't that the church Antoni Gaudí designed?", '휘빈: Yes, it is. It would be interesting to see how his design was inspired by nature.', '민우: Hmm… How about Gaudí and Spain as the title for our project?', '휘빈: I love it!'),
 ['휘빈이는 Gaudí and Spain을 프로젝트 제목으로 하는 데 찬성한다.', '휘빈이와 민우는 꿈에 그리던 시골에 방문할 예정이다.', '휘빈이는 스페인에 여러 번 가 본 적이 있다.', '휘빈이는 스페인의 상업에 관심이 많다.', '휘빈이는 교회를 보고 디자인이 만들어진 시기를 알아냈다.'],
 "이유 ▶ 민우의 제안(How about Gaudí and Spain ~?)에 I love it! ✔\n오답 ▶ {1} country(나라)를 '시골'로 착각 {2} 가 본 적 없음(would) {3} 건물(buildings)에 관심 {4} 언급 없음\n수정 ▶ 원본 대화의 오타(La Sagrad FAMILIA, designated)를 교과서대로 고침", [])
T.render()

# ═══════════════ 2회 ═══════════════
T = Test('2', '2회', '7과 · 8과 섞음', '7~8과 학교 기출', NOTICE, H=H)
# [2024-7]
T.flex('다음 대화의 주제로 가장 알맞은 것은?', S7, B("Jinho: I think living in a jungle would be really exciting. Don't you think so?", 'Claire: But there are some dangerous animals in the jungle, Jinho.', 'Jinho: I know. But the jungle is full of adventure. I wish I could live there.', 'Claire: What would you do if you lived in the jungle?',
 'Jinho: I would explore it. Maybe I could make some animal friends.', 'Claire: Then where would you sleep? In a cave?', 'Jinho: No, I would stay in a tree house. Then I would be safe from dangerous animals.', 'Claire: That makes sense.'),
 ["Jinho's desire to live in a jungle and explore it", 'Dangerous wild animals in the jungle', 'The preference for different kinds of houses', 'The way to build and stay in a tree house', "Claire's excitement about Jinho's idea of living in the jungle"],
 "이유 ▶ I wish I could live there. / I would explore it. → 정글에 살며 탐험하고 싶은 진호의 소망.\n오답 ▶ {1}·{3} 일부 내용 {2} 비교 없음 {4} Claire는 걱정함", [])
# [2024-10]
T.flex('밑줄 친 우리말을 영어로 바르게 옮긴 것은?', S7, B('At high tide, the water from the Adriatic Sea often rises and leaves the streets full of water. However, <u>나는 높이 올린 통로를 통해 도심 주변을 걸어 다닐 수 있을 것이다.</u>'),
 ['I would be able to walk around the town through the raised walkways.', 'I would be able to walk down the town through the raising walkways.', 'I would be able to walk around the town to the raised walkways.', 'I would be able to walk behind the town through the raised walkways.', 'I would be able walking around the town through the raised walkways.'],
 "이유 ▶ be able to + 동사원형, walk around(~ 주변을 걸어 다니다), through(~을 통해), raised(높여진)\n오답 ▶ {1} raising ❌ {2} to(~로) ❌ {3} behind(~ 뒤에) {4} be able walking ❌", [])
# [2024-11]
T.flex('대화의 흐름에 맞게 빈칸에 들어갈 말을 순서대로 나열한 것은?', S7, B('A: I ______ as many as a hundred fish. Will you come over for dinner? My house is just ______ the river.', 'B: Okay. Does your house have a flat roof?', 'A: No. My house has a yellow ladder outside.', 'B: I found it! By the way, ______ can I cross the river?', 'A: You can cross it ______ the wooden walkway.'),
 ['caught − across − how − using', 'bought − cross − who − using', 'caught − over − when − following', 'brought − across − when − getting', 'coughed − beside − how − getting'],
 "이유 ▶ 물고기를 100마리나 잡았다(caught) / 강 건너편에(across) / 어떻게(how) 건너지? / 나무 통로를 이용해서(using)", [])
# [2024-15]
T.fixed('주어진 문장이 들어갈 위치로 가장 적절한 곳은?', S7, B('These materials help you keep your skin healthy.') + '\n' + B(
 "When you visit Korea, you might wonder where you can stay. (A) Why don't you stay in a hanok? (B) A hanok is a traditional Korean house. (C) If you stayed in a hanok, you would sleep on the floor because there are no beds. (D) Hanok houses are mostly built with natural materials such as wood, stone, straw, paper, and earth. (E) In the cold winter, the warm ondol floors heat your body."),
 ['(A)', '(B)', '(C)', '(D)', '(E)'], 5,
 "이유 ▶ 나무·돌·짚·종이·흙 같은 천연 재료 → '이 재료들(These materials)'이 피부 건강을 지켜 준다.\n포인트 ▶ These materials가 가리키는 말 바로 뒤", [])
# [2024-16]
T.flex('다음 글에 대한 설명으로 올바른 것은?', S7, B("If you walked down a street in the village of the Ndebele in South Africa, you (A) ______ see houses with many unique patterns and styles. Each house tells a different story. Some stories might be about neighbors' babies. Others express personal opinions. "
 'A long time ago, the Ndebele were at war with the Boers. When the Boers invaded ⓐ their land, the Ndebele painted their houses with many colorful symbols. So, ⓑ their enemies couldn\'t understand what ⓒ they were secretly communicating to each other. The symbols expressed feelings such as sadness. Those symbols were (B) handed down from mothers to daughters.'),
 ["밑줄 친 (B) hand down의 뜻은 '…을 물려주다'이다.", '은데벨레 마을은 북아프리카에 있다.', '빈칸 (A)에 들어갈 말로 will이 알맞다.', '밑줄 친 ⓐ, ⓑ, ⓒ 중 가리키는 대상이 다른 것은 ⓒ이다.', '보어족은 은데벨레족의 의사소통을 모두 막았다.'],
 "이유 ▶ hand down = (후대에) 물려주다 ✔\n오답 ▶ {1} 남아프리카(South Africa) {2} If you walked → 가정법 과거 would {3} ⓐ·ⓑ·ⓒ 모두 은데벨레족 {4} 몰래 의사소통했다\n수정 ▶ 원본은 '모두 고르기'(정답 ②④)였는데 OMR에 맞게 ②를 틀린 설명으로 바꿔 정답 하나로", [('hand down', '물려주다')])
# [2024-16b]
T.flex('다음 글에 대해 <보기>에서 옳은 것만 고른 것은?', S7, B('... I would sometimes hear my neighbor ⓐ <u>calling</u> me to come over for tea or dinner. ... Do you wonder ⓑ ______? My bedroom would be on the third or fourth floor. A tulou is like a village. ... Some large tulou can ⓒ <u>house</u> up to 50 families. They work together and share many things. ⓓ <u>Living together in one building keeps them safely.</u>',
 '', '<보기> (A) 토루는 층마다 쓰임이 다르다.', "(B) 'an army or a country that enters another country by force'의 뜻을 가진 단어를 윗글에서 찾을 수 있다.", "(C) ⓐ 대신 'to call'을 쓸 수 있다.", "(D) 빈칸 ⓑ에는 'where would I sleep'이 알맞다.", "(E) ⓒ는 '수용하다'라는 뜻이다.", '(F) ⓓ 문장에는 어법상 오류가 있다.'),
 ['(A), (E), (F)', '(A), (B), (C)', '(A), (B), (F)', '(C), (D), (E)', '(D), (E), (F)'],
 "이유 ▶ (A) 1층 요리·식사, 2층 보관, 3·4층 침실 ✔ (E) house = 수용하다 ✔ (F) keeps them safe ✔\n오답 ▶ (B) invader는 토루 글에 없음 (C) hear + 목적어 + 동사원형/-ing (to부정사 ❌) (D) 간접의문문 where I would sleep\n수정 ▶ 원본 (C)의 'call'은 어법상 맞아서 (C)도 옳은 것이 되므로 'to call'로 바꿈", [])
# [2024-19]
T.flex('다음 중 어법상 바르지 <u>않은</u> 것만 고른 것은?', '7~8과', B('ⓐ I made my sister clean her room.', 'ⓑ Tests in school make students worrying.', 'ⓒ Staying home all day make Julie and Martha boring.', "ⓓ Don't forget to make the sleeping area higher."),
 ['ⓑ, ⓒ', 'ⓐ, ⓑ', 'ⓐ, ⓓ', 'ⓑ, ⓓ', 'ⓒ, ⓓ'],
 "이유 ▶ ⓑ 학생들이 '걱정하는' 상태 → worried ⓒ 동명사 주어 → makes, 사람이 '지루해하는' → bored\n오답 ▶ ⓐ 사역동사 make + 목적어 + 동사원형 ✔ ⓓ make + 목적어 + 형용사 ✔", [])
# [2024-20]
T.flex('대화의 빈칸에 들어갈 표현으로 알맞지 <u>않은</u> 것은?', S8, B("H: I'm writing an article about students' favorite snacks. I'm worried about their health.", 'M: Why?', 'H: Well, I surveyed 100 students and the results show that eighty percent of the students liked pizza and fried chicken for snacks. ______', 'M: Oh, I get it. Students really like fast food.'),
 ['How do you like it?', 'Do you understand?', 'You know what I mean?', 'Do you get what I mean?', "Do you see what I'm saying?"],
 "이유 ▶ 빈칸은 '무슨 말인지 알겠니?'(이해 확인). How do you like it?은 '그거 어때?'(의견 묻기)\n오답 ▶ {1}·{2}·{3}·{4} 모두 이해했는지 확인하는 말", [])
# [2024-21]
T.flex('위 대화(학생들이 좋아하는 간식)에 대해 바르게 설명한 것은?', S8, B("H: I'm writing an article about students' favorite snacks. I'm worried about their health.", 'H: I surveyed 100 students and the results show that eighty percent of the students liked pizza and fried chicken for snacks.', 'M: Oh, I get it. Students really like fast food. What else did they like?', 'H: Twelve percent of the students chose chocolate cake as their favorite.', 'M: Wow, students should really try to eat healthier snacks!'),
 ['Twelve percent of the students chose chocolate cake as their favorite snack.', "Henry is worried about students' grades.", 'Mina thinks students should eat more fast food.', 'Most students chose chocolate cake as their favorite snack.', 'Twenty out of one hundred students preferred fried chicken as a snack.'],
 "이유 ▶ Twelve percent ~ chocolate cake ✔\n오답 ▶ {1} 건강(health)을 걱정 {2} 더 건강한 간식을 먹어야 한다고 함 {3} 12%뿐 {4} 피자와 치킨이 80%\n수정 ▶ 원본 정답은 ②⑤였지만 ②(패스트푸드를 더 먹어야)는 본문과 반대 → 정답 하나로 고침", [])
# [2024-22]
T.flex('밑줄 친 단어의 영어 풀이가 바르지 <u>않은</u> 것은?', S8, '',
 ["It's too hard to read and draw <u>graphs</u>. : pieces of body tissue that help you to move a particular part of the body", 'I need to <u>count</u> the number of soldiers. : to calculate the total number of people, things, etc.',
  'Thirteen out of twenty students chose <u>novels</u>. : long written stories about imaginary people and events', 'He saw <u>soldiers</u> on horses. : members of an army, especially people who are not officers',
  'They were <u>chasing</u> a man with arrows in his hand. : to follow someone quickly in order to catch them'],
 "이유 ▶ ①의 풀이는 muscles(근육). graph는 숫자의 관계를 보여 주는 그림.\n수정 ▶ 원본은 ⑤ chase의 풀이(struggle의 뜻)도 틀려 정답이 두 개 → ⑤를 바른 풀이로 고쳐 정답 하나로", [])
# [2024-26]
T.flex('다음 대화의 내용과 일치하지 <u>않는</u> 것은?', S8, B("B: Jian, what's the matter? You look very upset.", "J: My brother broke my computer. I'm so angry.", "B: I'm sorry to hear that, but your facial muscles must be tired.", 'J: What do you mean?',
 'B: Well, it takes a lot of muscles to look angry, but only a few to smile. Do you see what I mean?', "J: Oh, I get it. I guess it's not good to stay angry for a long time.", "B: That's right. Remember, it's always better to smile."),
 ['It is good to stay angry for a long time.', 'It is better to smile than to stay angry.', 'Being angry uses a lot of facial muscles.', 'We do not need a lot of facial muscles to smile.', 'Jian is upset because her brother broke her computer.'],
 "이유 ▶ it's not good to stay angry for a long time → 반대.\n오답 ▶ {1} always better to smile ✔ {2} a lot of muscles to look angry ✔ {3} only a few to smile ✔ {4} ✔", [('facial muscle', '얼굴 근육')])
# [2024-27]
T.fixed('다음 문장 ⓐ~ⓓ에 대해 잘못 말한 사람의 수는?', S7, B('ⓐ If he will be at home, I will visit him now.', 'ⓑ If she had his number, she would call him.', 'ⓒ I am not good at singing. If I was good at singing, I would join the singing club.', "ⓓ We don't have much snow this year. If it snowed a lot, we would go sledding.", '',
 'Kyle: ⓑ는 어법상 맞아.', "Theo: ⓐ의 'will be'는 'is'로 고쳐야 해.", "Freya: ⓑ는 'As she didn't have his number, she couldn't call him.'과 뜻이 같아.", "Amelia: 글로 쓸 때는 ⓒ의 'was' 대신 'were'를 쓰는 게 좋아.", "Ramsey: ⓓ의 가정은 올해 눈이 많이 오지 않아서 사실이 아닌 상황이야."),
 ['1명', '2명', '3명', '4명', '5명'], 1,
 "이유 ▶ Freya만 틀림: 가정법 과거는 '현재' 사실의 반대 → As she doesn't have his number, she can't call him.\n맞는 사람 ▶ Kyle, Theo(조건절은 현재형), Amelia, Ramsey\n수정 ▶ 원본의 영어 이름 대사를 우리말로 옮겨 이해하기 쉽게 함", [])
# [2024-29]
T.flex("'그는 로빈 후드가 그에게 손을 흔들고 있는 것을 보았다.'를 영작할 때, 바르게 말한 사람끼리 고른 것은?", S8, B('Jina: 이 문장에서 wave의 형태는 waving으로 써야 해.', 'Jiwon: 이 문장은 6개의 단어로 영작할 수 있어.', 'Yoona: 과거에 있었던 일이니, 동사는 saw라고 해야겠지?', 'Hyein: 이 문장은 영작할 때 because를 써야 해.'),
 ['Jina, Yoona', 'Jina, Jiwon', 'Jiwon, Yoona', 'Yoona, Hyein', 'Jiwon, Yoona, Hyein'],
 "이유 ▶ He saw Robin Hood waving at him. → 지각동사 see + 목적어 + -ing(Jina ✔), 과거 saw(Yoona ✔)\n오답 ▶ Jiwon: 7단어 / Hyein: because 필요 없음", [])
# [2024-30]
T.flex('다음 중 우리말을 바르게 영작한 것은?', S8, '',
 ['비가 올 때 우리 학교에서는 아무도 축구를 하지 않아. → No one in my school plays soccer when it rains.', '우리 가족은 아무도 TV를 보지 않아. → Nobody in my family watch TV.', '아무도 이런 종류의 모자는 쓰지 않아. → No one wore these kinds of hats.',
  '그가 틀렸을 때 아무도 고쳐 주지 않을 거야. → Nobody will be corrected when he is wrong.', '겨울에는 아무도 이 강에서 수영하지 않았어. → In winter, no one swim in this river.'],
 "이유 ▶ No one + 단수 동사(plays) ✔\n오답 ▶ {1} watch → watches {2} 현재 → wear {3} 수동태 ❌ → Nobody will correct him {4} swim → swam\n수정 ▶ 원본은 정답이 ④⑤ 두 개 → ④를 틀린 문장으로 바꿔 정답 하나로", [])
# [2020-C]
T.flex('다음 글의 내용으로 대답할 수 <u>없는</u> 질문은?', S7, B(VEN, VEN2),
 ['거리가 물에 잠겼을 때 걸어 다닐 수 있는 높인 통로의 이름은?', '글쓴이가 베니스에 산다면 학교에 갈 때 타고 갈 교통수단은?', '베니스의 섬 개수는?', '베니스의 수상 버스 이름은?', '베니스의 다른 이름(별명)은?'],
 "이유 ▶ 높인 통로(raised walkways)가 있다는 말만 있고, 이름은 나오지 않는다.\n오답 ▶ {1} 곤돌라 {2} 118개 {3} vaporetto {4} floating city", [])
# [2020-D]
T.flex('다음 글에 나타난 토루에서의 삶의 모습으로 적절한 것은?', S7, B(TUL),
 ['토루의 주민들은 대부분 같은 성씨이다.', '집에 함께 놀 친구들이 거의 없다.', '토루에는 보통 3~5개의 거실이 있다.', '제일 아래층은 보통 음식이나 도구를 보관하는 곳이다.', '토루의 주민들은 각자 독립적으로 생활한다.'],
 "이유 ▶ mostly have the same family name ✔\n오답 ▶ {1} always have friends at home to play with {2} 거실이 아니라 3~5개 층 {3} 보관은 2층 {4} 함께 일하고 많은 것을 나눈다\n수정 ▶ 원본 정답(④⑤)에서 ⑤(독립적인 생활)는 본문과 반대이고, 원본 ①(항상 함께 놀 친구가 있다)은 맞는 내용이라 정답이 잘못되어 있었음 → 정답 하나로 고침", [])
# [2022-A]
T.flex('다음 대화에 대한 내용으로 어색한 것은?', S7, TURKEY,
 ['B는 A에게서 튀르키예 여행 사진을 받았다.', 'B는 A에게 튀르키예 여행 사진을 보여 주었다.', 'A는 동굴 집들을 보고 매우 독특하다고 생각한다.', 'A는 튀르키예가 방문하기에 훌륭한 곳이라고 생각한다.', 'B도 튀르키예에 가 보고 싶어 한다.'],
 "이유 ▶ 사진을 보낸 사람은 Julia(she sent me some pictures) → A에게서 받은 것이 아니다.\n오답 ▶ {1} take a look ✔ {2} so unique ✔ {3} a wonderful place to visit ✔ {4} Me too! ✔", [])
# [2022-B]
T.flex('다음 영영풀이에 해당하는 단어로 알맞은 것은?', S7, B('to cause someone to admire or respect you'),
 ['impress', 'depress', 'suspect', 'expect', 'express'],
 "이유 ▶ 다른 사람이 감탄하거나 존경하게 만들다 = 감명을 주다(impress)\n오답 ▶ {1} 우울하게 하다 {2} 의심하다 {3} 기대하다 {4} 표현하다", [])
# [2022-E]
T.fixed('다음 글의 ⓐ~ⓔ 중 어법상 어색한 것은?', S7, B(
 'Different people ⓐ <u>live</u> in different houses. ... If I lived in a pueblo, I would climb up a ladder to enter my house. There\'s a ⓑ <u>hidden</u> opening on top of the house. If unwelcome visitors ⓒ <u>were appeared</u>, I would pull the ladder up to stop them from entering. The thick walls are made of earth, straw, and water. '
 'They would keep me cool in summer and warm in winter. The house ⓓ <u>has</u> a flat roof. I would sometimes ⓔ <u>sleep</u> up on the roof under the moon and stars.'),
 ['ⓐ', 'ⓑ', 'ⓒ', 'ⓓ', 'ⓔ'], 3,
 "이유 ▶ appear(나타나다)는 수동태가 안 되는 자동사 → appeared.\n수정 ▶ 원본 문장(If unwelcome visitors to be appeared.)이 깨져 있어 바로잡음", [])
# [2022-F]
T.flex('다음 글의 내용으로 어색한 것은?', S7, B('Different people live in different houses. Some use ladders to enter their houses. ...', PUE, VEN, VEN2),
 ["베니스는 물 위에 색색의 집이 많고, '평평한 도시'로 알려져 있다.", '집에 들어가기 위해 사다리를 사용하는 사람들도 있다.', '푸에블로에서는 반갑지 않은 방문객이 들어오지 못하게 사다리를 끌어 올린다.', '베니스에 산다면, 곤돌라를 타고 학교에 갈 것이다.', '베니스의 땅에는 천만 개가 넘는 나무 기둥이 설치되어 있다.'],
 "이유 ▶ 베니스의 별명은 floating city(떠 있는 도시) → '평평한 도시'가 아니다.\n오답 ▶ {1}·{2}·{3}·{4} 본문과 일치", [])
T.render()
