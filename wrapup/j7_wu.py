# 11/13 중3 지학사(민찬규) Lesson 7 If I Lived There — 실전 변형 1·2·3회 (각 20문항, 1회 중 → 2회 상 → 3회 최상)
# 범위: 대화문(L&S 1·2, Real Life) · 본문(푸에블로·베니스·토루) · 문법(가정법 과거, make/keep + 목적어 + 형용사, It is ~ that 강조 등)
from wu_j7 import *
H = ('7과 실전 변형', '중3 영어 지학사(민찬규) Lesson 7 If I Lived There', '지학사(민찬규) 7과', 'j7')
B = lambda *ls: BOX('<br>'.join(ls))
NUMS = ['1개', '2개', '3개', '4개', '5개']
OPTS_ORD = ['(A) − (C) − (B)', '(B) − (A) − (C)', '(B) − (C) − (A)', '(C) − (A) − (B)', '(C) − (B) − (A)']
def ABC(given, chunks, seq):
    lab = dict(zip(seq, chunks))
    body = B(given) + '\n' + BOX('<br>'.join('<b>(%s)</b> %s' % (L, lab[L]) for L in 'ABC'))
    return body, OPTS_ORD.index(' − '.join('(%s)' % L for L in seq)) + 1
D, R, G = '대화문', '본문', '문법'
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
        "They work together and share many things. Living together in one building keeps them safe.")

# ═══════════════ 1회 (중) ═══════════════
T = Test('1', '1회', '대화문 · 본문 · 문법', '7과 전 범위',
 '범위: 7과 대화문(L&S 1·2, Real Life) · 본문(푸에블로 · 베니스 · 토루) · 문법(가정법 과거, keep/make + 목적어 + 형용사, It is ~ that). 교과서 문장을 일부 바꾼 문항이 있어요. 끝까지 읽고 고르세요.', H=H)
T.flex('다음 대화의 빈칸에 들어갈 말로 가장 알맞은 것은?', D, B(
 'G: Oh, look at those cave houses! They look so unique, don\'t they? ' + BL, 'B: I like those balloons. They look so beautiful!', 'G: I think Türkiye is a wonderful place to visit. I hope to visit there some day.'),
 ['I wish I could try living there.', "I'm glad that I live there now.", "I don't want to visit there at all.", 'I wish I could not see them.', "I can't wait to leave there."],
 "이유 ▶ 동굴 집이 독특해 보인다 → 그곳에서 살아 보고 싶다는 소망(I wish I could ~). 뒤의 '언젠가 방문하고 싶다'와도 이어진다.\n오답 ▶ {1} 지금 사는 게 아니다 {2}·{3}·{4} 독특하다고 감탄한 말과 반대\n포인트 ▶ I wish I could + 동사원형 = ~할 수 있으면 좋겠다(지금은 못 함)", [])
T.flex('밑줄 친 말에 담긴 의도로 가장 알맞은 것은?', D, B('B: I got a new sled for my birthday. I can\'t wait to test it out.', 'G: Let me check the weather. Umm, there will be no snow for a while.', 'B: <u>I wish I could live in Alaska.</u> Then I could go sledding all day!'),
 ['소망 표현하기', '후회 표현하기', '허락 구하기', '충고하기', '불평하기'],
 "이유 ▶ I wish I could ~ = 실제로는 할 수 없지만 '~하면 좋겠다'는 소망.\n오답 ▶ {1} 후회는 과거 일에 대한 아쉬움 {2} 허락 구하기는 May I ~? {3} 충고는 You'd better ~ {4} 눈이 안 와서 아쉽지만 표현 자체는 소망\n포인트 ▶ 소망 = I wish I could ~ / I hope to ~ / I'd love to ~", [])
T.flex('다음 대화의 내용과 일치하는 것은?', D, B(
 'B: Will it snow today?', 'G: I have no idea. Why are you waiting for snow, Taeho?', "B: I got a new sled for my birthday. I can't wait to test it out.", 'G: Let me check the weather. Umm, there will be no snow for a while.',
 'B: I wish I could live in Alaska. Then I could go sledding all day!', 'G: No kidding! Alaska is a very cold place.', 'B: I think it would be fun. I want to build a snow house and stay there on vacation.'),
 ['태호는 생일 선물로 새 썰매를 받았다.', '당분간 눈이 많이 올 예정이다.', '여학생은 알래스카에 살아 본 적이 있다.', '태호는 눈집에서 지내는 것이 지루할 거라고 생각한다.', '여학생은 날씨를 확인해 주지 않았다.'],
 "이유 ▶ I got a new sled for my birthday ✔\n오답 ▶ {1} there will be no snow for a while(당분간 눈 없음) {2} 근거 없음 {3} I think it would be fun(재미있을 것) {4} Let me check the weather → 확인해 줌", [])
body, a = ABC('B: This is my dream house, Alice. What do you think?', ['G: Oh, the house has wheels! Is it a kind of car?', 'B: Yes, it can move like a car.', 'G: So what would you do if you lived in that house?'], 'BAC')
T.fixed('주어진 말 다음에 이어질 대화의 순서로 가장 알맞은 것은?', D, body, OPTS_ORD, a,
 "이유 ▶ 꿈의 집 소개 → (B) 바퀴가 있네! 차의 일종이야? → (A) 응, 차처럼 움직여 → (C) 그럼 그 집에 산다면 뭘 할 거야?\n포인트 ▶ (A)의 Yes는 (B)의 질문(Is it a kind of car?)에 대한 대답, (C)의 So는 앞 내용을 받아 묻는 말.", [])
T.flex('다음 대화의 빈칸에 들어갈 말로 가장 알맞은 것은?', D, B('A: What would you do if you became a millionaire?', 'B: ' + BL),
 ['I would build my own house.', 'I built my own house last year.', 'I will be a millionaire someday.', 'Yes, I would.', 'I wish I were a millionaire.'],
 "이유 ▶ What would you do if ~? (가정) → I would ~ 로 대답.\n오답 ▶ {1} 과거 사실 {2} 무엇을 할지에 대한 답이 아님 {3} 의문사 의문문에 Yes ❌ {4} 소망일 뿐 무엇을 할지 답하지 않음\n포인트 ▶ 상상해서 묻기 What would you do if ~? → 답 I would ~", [])
T.flex('다음 중 짝지어진 대화가 <u>어색한</u> 것은?', D, '',
 ['A: What would you do if you lived in a tree house? — B: I lived there last year.', 'A: I wish I could fly. — B: Me too. It would be fun.',
  'A: Does anybody live in the upside-down house? — B: No, it would not be easy to live there.', 'A: Which country do you want to visit? — B: In my case, I want to visit Spain.',
  "A: Living in a jungle would be exciting. Don't you think so? — B: But there are dangerous animals there."],
 "이유 ▶ 나무 집에 산다면 '무엇을 할지' 물었는데 작년에 살았다는 과거 사실로 답함 → 어색. (예: I would watch the birds.)\n오답 ▶ {1} 소망에 동의 ✔ {2} 살기 쉽지 않을 것 ✔ {3} 나라 질문 → 스페인 ✔ {4} 반대 의견 제시 ✔", [])
T.flex('다음 글 뒤에 이어질 내용으로 가장 알맞은 것은?', R, B('Different people live in different houses. Some use ladders to enter their houses. Others live in houses on the water. And others share their houses with many people. Imagine you live in one of these houses. How would that change your life?'),
 ['세계 여러 지역의 독특한 집에서 사는 삶을 상상해 보는 글', '사다리를 안전하게 사용하는 방법', '물 위에 집을 짓는 공사 과정', '대가족이 함께 사는 것의 단점', '도시와 시골 집값의 차이'],
 "이유 ▶ 여러 종류의 집을 소개하고 '그중 하나에 산다면 삶이 어떻게 바뀔지 상상해 보라' → 이어서 각 집에 사는 모습을 상상(If I lived in ~).\n오답 ▶ {1}·{2}·{3}·{4} 집의 예일 뿐이거나 언급 없음", [])
T.flex('다음 글의 내용과 일치하지 <u>않는</u> 것은?', R, B(PUE),
 ['The walls of the house are made of wood and stone.', 'There is a hidden opening on top of the house.', 'People use a ladder to enter the house.', 'The thick walls keep the house cool in summer.', 'The house has a flat roof.'],
 "이유 ▶ The thick walls are made of earth, straw, and water(흙, 지푸라기, 물) → 나무와 돌이 아님.\n오답 ▶ {1} hidden opening on top ✔ {2} climb up a ladder to enter ✔ {3} keep me cool in summer ✔ {4} a flat roof ✔", [])
T.fixed('다음 글의 밑줄 친 부분 중, 어법상 <u>틀린</u> 것은?', R, B(
 'If I ' + CN(1, 'lived') + ' in a pueblo, I would climb up a ladder ' + CN(2, 'to enter') + ' my house. If unwelcome visitors appeared, I would pull the ladder up to stop them from ' + CN(3, 'enter') +
 '. The thick walls ' + CN(4, 'are made') + ' of earth, straw, and water. They would keep me ' + CN(5, 'cool') + ' in summer and warm in winter.'),
 ['lived', 'to enter', 'enter', 'are made', 'cool'], 3,
 "이유 ▶ stop A from -ing(A가 ~하지 못하게 하다) → from 뒤에 동명사 <i>entering</i>.\n오답 ▶ ① 가정법 과거(If + 과거형, would) ✔ ② 목적(~하기 위해) ✔ ③ 벽이 '만들어진' 수동 ✔ ⑤ keep + 목적어 + 형용사 ✔\n포인트 ▶ 전치사 뒤에는 동명사!", [])
T.flex('다음 빈칸에 들어갈 말로 가장 알맞은 것은?', R, B('Venice is known as the "' + BL + ' city." In Venice, there are many colorful houses on the water.'),
 ['floating', 'sinking', 'frozen', 'hidden', 'moving'],
 "이유 ▶ 물 위에 집들이 있는 베니스 = '떠 있는' 도시(floating city).\n오답 ▶ {1} 가라앉는 {2} 얼어붙은 {3} 숨겨진 {4} 움직이는 — 본문 표현이 아님", [])
T.fixed('다음 글의 밑줄 친 부분 중, 문맥상 낱말의 쓰임이 적절하지 <u>않은</u> 것은?', R, B(
 'At high tide, the water from the Adriatic Sea often ' + CN(1, 'rises') + ' and leaves the streets ' + CN(2, 'full') + ' of water. However, I would be able to walk around the town through the ' + CN(3, 'raised') +
 ' walkways. The old Venetians decided to live there to keep themselves ' + CN(4, 'safe') + ' from invaders. But it was ' + CN(5, 'easy') + ' for them to build their homes on this swampy surface. So they installed more than 10 million wooden poles in the ground.'),
 ['rises', 'full', 'raised', 'safe', 'easy'], 5,
 "이유 ▶ But(하지만) + So 나무 기둥을 천만 개 이상 설치했다 → 습지 위에 집 짓기가 '쉽지 않았다' → <i>not easy</i> (difficult).\n오답 ▶ ① 물이 '불어나' ② 거리를 물로 '가득' ③ '높이 올린' 통로 ④ 침략자로부터 '안전하게'", [])
T.flex('Why did the old Venetians decide to live on the water?', R, B(VEN2),
 ['To keep themselves safe from invaders.', 'To catch more fish in the sea.', 'Because the land was too expensive.', 'Because they wanted to travel by gondola.', 'Because they liked colorful houses.'],
 "이유 ▶ The old Venetians decided to live there to keep themselves safe from invaders ✔\n오답 ▶ {1}·{2}·{3}·{4} 본문에 없는 이유", [])
T.flex('다음 글의 내용과 일치하는 것은?', R, B(TUL),
 ['1층은 요리하고 식사하는 데 쓰인다.', '2층에는 주로 침실이 있다.', '토루는 보통 6층 이상이다.', '글쓴이의 침실은 1층에 있을 것이다.', '이웃과는 거의 왕래하지 않는다.'],
 "이유 ▶ The first floor is used for cooking and eating ✔\n오답 ▶ {1} 2층은 식량·도구 보관 {2} three to five floors {3} third or fourth floor {4} 이웃이 차·저녁 먹으러 오라고 부름", [])
T.flex('다음 빈칸에 들어갈 말로 가장 알맞은 것은?', R, B('A tulou is like a ' + BL + '. The people living in a tulou mostly have the same family name. Some large tulou can house up to 50 families. They work together and share many things.'),
 ['village', 'castle', 'school', 'market', 'museum'],
 "이유 ▶ 같은 성을 가진 사람들, 50가구까지, 함께 일하고 나눔 → '마을'과 같다.\n오답 ▶ 다른 장소들은 뒤 설명과 이어지지 않음", [])
T.flex('다음 빈칸에 들어갈 말로 알맞은 것은?', G, B('If I ' + BL + ' a tulou, I would always have friends at home to play with.'),
 ['lived in', 'live in', 'will live in', 'living in', 'to live in'],
 "이유 ▶ 주절이 would + 동사원형 → 가정법 과거: If + 주어 + 동사의 과거형.\n오답 ▶ {1} 현재형(직설법 조건) {2} 조건절에 will ❌ {3}·{4} 동사 자리가 아님\n포인트 ▶ If + 과거형, 주어 + would/could + 동사원형 = 현재 사실의 반대", [])
T.flex('다음 문장과 의미가 같은 것은?', G, B("As I don't live in Venice, I can't take a gondola to school."),
 ['If I lived in Venice, I could take a gondola to school.', 'If I live in Venice, I can take a gondola to school.', "If I didn't live in Venice, I couldn't take a gondola to school.",
  "If I lived in Venice, I couldn't take a gondola to school.", "Though I live in Venice, I can't take a gondola to school."],
 "이유 ▶ 직설법(현재 부정) → 가정법 과거(긍정): don't live → lived, can't → could.\n오답 ▶ {1} 가정법이 아님 {2} 긍정·부정이 반대 {3} 주절이 반대 {4} 실제로 산다는 뜻\n포인트 ▶ 직설 ↔ 가정: 시제는 한 칸 과거로, 긍정 ↔ 부정은 뒤집기", [])
T.flex('다음 빈칸에 들어갈 말로 알맞은 것은?', G, B('Living together in one building keeps them ' + BL + '.'),
 ['safe', 'safely', 'safety', 'to safe', 'be safe'],
 "이유 ▶ keep + 목적어 + 형용사(목적격 보어) = ~을 …한 상태로 유지하다 → safe.\n오답 ▶ {1} 부사는 보어 자리에 못 옴 {2} 명사(안전)는 them과 같은 대상이 아님 {3}·{4} 형태 오류\n포인트 ▶ keep/make + 목적어 + 형용사 (부사 ❌)", [])
T.flex('다음 밑줄 친 부분과 쓰임이 같은 것은?', G, B('<u>It</u> is these wooden poles <u>that</u> support Venice to this day.'),
 ['It was Tom that broke the window yesterday.', 'It is true that he is honest.', 'It is interesting to see the house.', 'It is so cold that I want to stay home.', 'It is a pity that she left early.'],
 "이유 ▶ It is[was] + 강조할 말 + that ~: 'Tom'을 강조(어제 창문을 깬 사람은 바로 Tom이었다).\n오답 ▶ {1}·{4} 가주어 it, 진주어 that절 {2} 가주어 it, 진주어 to부정사 {3} 날씨 it + so ~ that(너무 ~해서 …하다)\n포인트 ▶ It is ~ that에서 It is와 that을 지워도 문장이 완전하면 강조 구문(These wooden poles support Venice.)", [])
body, a = ABC('In a tulou, there are usually three to five floors.', ['The first floor is used for cooking and eating.', 'And people store food and tools on the second floor.', 'Do you wonder where I would sleep? My bedroom would be on the third or fourth floor.'], 'ACB')
T.fixed('주어진 문장 다음에 이어질 글의 순서로 가장 알맞은 것은?', R, body, OPTS_ORD, a,
 "이유 ▶ 3~5층 → (A) 1층: 요리·식사 → (C) And 2층: 식량·도구 보관 → (B) 내 침실은 3·4층.\n포인트 ▶ 층 순서(1층 → 2층 → 3·4층)와 연결어 And", [])
T.flex('7과 본문 전체의 제목으로 가장 알맞은 것은?', R, '',
 ['Homes Around the World: Imagining Life in Them', 'How to Build a House on Water', 'The Long History of Venice', 'Why Big Families Should Live Together', 'Dangerous Animals in the Jungle'],
 "이유 ▶ 푸에블로·베니스·토루 등 세계의 다양한 집을 소개하며 그곳에 산다면 어떨지 상상하는 글.\n오답 ▶ {1}·{2}·{3} 한 부분만 다룸 {4} 대화문 내용", [])
T.render()

# ═══════════════ 2회 (상) ═══════════════
T = Test('2', '2회', '대화문 · 본문 · 문법', '7과 전 범위',
 '범위: 7과 대화문 · 본문 · 문법. 1회보다 어려워요. 대화의 흐름, 본문의 세부 내용, 가정법 시제를 꼼꼼히 확인하세요.', H=H)
T.flex('다음 대화의 빈칸에 들어갈 말로 가장 알맞은 것은?', D, B('G: Look. The house in this picture is upside down.', 'B: That\'s interesting. Does anybody live there?', 'G: No, it would not be easy to live there because ' + BL + '.', 'B: Really? But I want to try living there.'),
 ['the inside is also upside down', 'it is too far from the city', 'nobody wants to see it', 'it is covered with mirrors', 'the house has wheels'],
 "이유 ▶ 거꾸로 된 집에 살기 쉽지 않은 이유 → 안쪽도 거꾸로 되어 있어서.\n오답 ▶ {1}·{2} 근거 없음 {3} 거울 집 {4} 바퀴 달린 집 — 다른 대화의 집", [])
T.flex('다음 대화의 내용과 일치하는 것은?', D, B(
 'G: Dohun, we need to start our project on our dream country to visit.', 'B: That\'s right. Which country do you want to visit, Emma?', 'G: In my case, I want to visit Spain.', 'B: What would you do if you visited Spain?',
 "G: I'm interested in buildings. So I would go see La Sagrada Familia.", "B: Isn't that the church Antoni Gaudí designed?", 'G: Yes, it is. It would be interesting to see how his design was inspired by nature.',
 'B: Hmm... How about Gaudí and Spain as the title for our project?', 'G: I love it!'),
 ['Emma is interested in buildings.', 'Dohun designed La Sagrada Familia.', 'Emma wants to visit Italy.', 'They have already finished their project.', 'Emma suggested the title for the project.'],
 "이유 ▶ I'm interested in buildings(Emma) ✔\n오답 ▶ {1} 설계자는 Gaudí {2} 스페인 {3} 이제 시작해야 함(need to start) {4} 제목은 Dohun이 제안(How about ~?)", [])
T.flex('다음 대화의 빈칸에 들어갈 말로 가장 알맞은 것은?', D, B('Claire: Then where would you sleep? In a cave?', 'Jinho: No, I would stay in a tree house. Then ' + BL, 'Claire: That makes sense.'),
 ['I would be safe from dangerous animals.', 'I would be in danger every night.', 'I would go back home to sleep.', 'I could live in a cave instead.', 'animals could easily come into my house.'],
 "이유 ▶ 위험한 동물이 있는 정글 → 나무 위 집 = 동물로부터 안전. That makes sense(일리가 있네)와 연결.\n오답 ▶ {1}·{4} 오히려 위험해짐 {2} 정글에서 지내는 상상과 맞지 않음 {3} 동굴이 아니라고 했다", [])
T.flex('다음 문장과 의미가 가장 가까운 것은?', D, B('I wish I could live in a snow house.'),
 ["I'd love to live in a snow house.", "I'm sorry that I lived in a snow house.", "I don't want to live in a snow house.", 'I used to live in a snow house.', "I'm sure I will live in a snow house."],
 "이유 ▶ 소망 I wish I could ~ = I'd love to ~ / I hope to ~\n오답 ▶ {1} 과거 후회 {2} 반대 {3} 과거 습관 {4} 확신", [])
T.flex('다음 대화를 통해 알 수 있는 것은?', D, B('G: What kind of house would you build?', 'B: I would build a house that is completely covered with mirrors.', 'G: Why?', "B: The mirrors would make the house almost invisible. Wouldn't that be cool?", 'G: That would be cool!'),
 ['The mirrors would make the house hard to see.', 'The boy already lives in a mirror house.', 'The girl thinks the house would look strange.', 'The boy wants to build a house with wheels.', 'The house would be covered with glass windows only.'],
 "이유 ▶ make the house almost invisible = 집을 거의 보이지 않게 만들다 = 보기 어렵게.\n오답 ▶ {1} 가정(would build) {2} That would be cool(멋지겠다) {3} 바퀴 집은 다른 대화 {4} 거울로 완전히 덮인 집\n어휘 ▶ invisible 보이지 않는", [])
T.fixed('다음 대화의 ①~⑤ 중 흐름과 관계없는 말은?', D, B(
 'Jinho: I think living in a jungle would be really exciting. Don\'t you think so?', '① Claire: But there are some dangerous animals in the jungle, Jinho.', '② Jinho: I know. But the jungle is full of adventure. I wish I could live there.',
 '③ Claire: What would you do if you lived in the jungle?', "④ Jinho: I would explore it. I'm afraid of exploring new places, though.", '⑤ Claire: Then where would you sleep? In a cave?'),
 None, 4,
 "이유 ▶ 정글은 모험으로 가득하고 탐험하겠다고 해 놓고, 새로운 곳을 탐험하는 게 무섭다는 말은 흐름과 반대.\n포인트 ▶ 원래 대화: I would explore it. Maybe I could make some animal friends.", [])
T.table('(A), (B), (C)에 들어갈 말로 바르게 짝지은 것은?', R, B(
 'Different people live in different houses. <b>(A)</b> ' + BL + ' use ladders to enter their houses. <b>(B)</b> ' + BL + ' live in houses on the water. And <b>(C)</b> ' + BL + ' share their houses with many people.'),
 ['(A)', '(B)', '(C)'], [['Some', 'Others', 'others'], ['One', 'The other', 'others'], ['Some', 'The other', 'another'], ['Others', 'Some', 'the others'], ['Some', 'Another', 'the other']],
 "이유 ▶ 여러 사람 중 '몇몇은(Some) ~, 다른 사람들은(Others) ~, 또 다른 사람들은(others) ~' — 정해지지 않은 여럿을 나누어 말할 때.\n오답 ▶ One / the other는 둘 중 하나와 나머지 하나 / another·the other는 단수 / the others는 나머지 전부\n포인트 ▶ Some ~, Others[others] ~ (여럿을 나열)", [])
T.flex('다음 빈칸에 들어갈 말로 가장 알맞은 것은?', R, B("If I lived in a pueblo, I would climb up a ladder to enter my house. There's a hidden opening on top of the house. If unwelcome visitors appeared, I would pull the ladder up to " + BL + '.'),
 ['stop them from entering', 'help them climb up easily', 'invite them inside', 'sleep on the roof', 'fix the hidden opening'],
 "이유 ▶ 반갑지 않은 방문객(unwelcome visitors) → 사다리를 끌어 올려 '들어오지 못하게'.\n오답 ▶ {1}·{2} 반대 {3} 지붕에서 자는 것은 다른 내용 {4} 근거 없음", [])
T.fixed('다음 글의 밑줄 친 부분 중, 어법상 <u>틀린</u> 것은?', R, B(
 'If I ' + CN(1, 'lived') + ' in Venice, I would take a gondola to school every morning. At high tide, the water often rises and leaves the streets ' + CN(2, 'full') + ' of water. You may wonder how and why they ' + CN(3, 'built') +
 ' the houses on the water. The old Venetians decided ' + CN(4, 'living') + ' there to keep themselves safe from invaders. It is these wooden poles that ' + CN(5, 'support') + ' Venice to this day.'),
 ['lived', 'full', 'built', 'living', 'support'], 4,
 "이유 ▶ decide는 to부정사를 목적어로 → decided <i>to live</i>.\n오답 ▶ ① 가정법 과거 ✔ ② leave + 목적어 + 형용사(~을 …한 상태로 두다) ✔ ③ 과거의 일 ✔ ⑤ 강조되는 말 these wooden poles(복수) → support ✔\n포인트 ▶ decide / want / hope / plan + to부정사", [])
T.flex('다음 글의 내용과 일치하지 <u>않는</u> 것은?', R, B(VEN + ' ' + VEN2),
 ['Venice consists of more than 200 small islands.', 'A vaporetto is a kind of water bus.', 'The streets are sometimes filled with seawater.', 'There are raised walkways in the town.', 'More than 10 million wooden poles were installed.'],
 "이유 ▶ Venice has 118 small islands → 200개 이상이 아님.\n오답 ▶ {1} a vaporetto, a water bus ✔ {2} leaves the streets full of water ✔ {3} raised walkways ✔ {4} more than 10 million wooden poles ✔\n어휘 ▶ consist of ~으로 이루어지다", [])
body, a = ABC('You may wonder how and why they built the houses on the water.', ['The old Venetians decided to live there to keep themselves safe from invaders.', 'But it was not easy for them to build their homes on this swampy surface.', 'So they installed more than 10 million wooden poles in the ground. It is these wooden poles that support Venice to this day.'], 'CBA')
T.fixed('주어진 문장 다음에 이어질 글의 순서로 가장 알맞은 것은?', R, body, OPTS_ORD, a,
 "이유 ▶ 어떻게, 왜 지었는지 궁금할 것 → (C) 왜: 침략자로부터 안전하려고 → (B) But 습지라 짓기 쉽지 않았다 → (A) So 나무 기둥 설치(어떻게).\n포인트 ▶ why(이유) → But(문제) → So(해결)", [])
T.table('(A), (B), (C)의 각 네모 안에서 어법에 맞는 표현으로 바르게 짝지은 것은?', R, B(
 'I would sometimes hear my neighbor <b>(A)</b> [ call / to call ] me to come over for tea. … The people <b>(B)</b> [ living / lived ] in a tulou mostly have the same family name. … Living together in one building <b>(C)</b> [ keep / keeps ] them safe.'),
 ['(A)', '(B)', '(C)'], [['call', 'living', 'keeps'], ['to call', 'living', 'keeps'], ['call', 'lived', 'keeps'], ['call', 'living', 'keep'], ['to call', 'lived', 'keep']],
 "이유 ▶ (A) 지각동사 hear + 목적어 + 동사원형/-ing → call (B) 사람들이 '사는' 능동 → living (C) 주어는 동명사구(Living together ~) → 단수 keeps\n오답 ▶ 지각동사 뒤 to부정사 ❌ / lived는 수동 의미 / keep은 복수 동사라 동명사 주어(단수)와 맞지 않음\n포인트 ▶ 동명사 주어 → 단수 동사", [])
T.fixed('글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 알맞은 곳은?', R, B('<b>My bedroom would be on the third or fourth floor.</b>') + '\n' + BOX(
 'In a tulou, there are usually three to five floors.' + GP(1) + 'The first floor is used for cooking and eating.' + GP(2) + 'And people store food and tools on the second floor.' + GP(3) + 'Do you wonder where I would sleep?' + GP(4) + 'A tulou is like a village.' + GP(5) + 'The people living in a tulou mostly have the same family name.'),
 None, 4,
 "이유 ▶ '내가 어디서 잘지 궁금한가?'라는 질문 바로 뒤에 그 답(내 침실은 3·4층)이 와야 한다.\n오답 ▶ ①~③ 아직 잠잘 곳 질문이 나오기 전 ⑤ 마을 이야기로 넘어간 뒤", [])
T.flex('다음 밑줄 친 house의 의미로 가장 알맞은 것은?', R, B('Some large tulou can <u>house</u> up to 50 families.'),
 ['to provide a place for people to live', 'a building for people to live in', 'to clean and decorate a room', 'to sell a building to others', 'to build a wall around a town'],
 "이유 ▶ can 뒤의 house는 동사: ~에게 살 곳을 제공하다, 수용하다.\n오답 ▶ {1} 명사 '집'의 뜻 — can 뒤에는 동사 {2}·{3}·{4} 다른 뜻\n포인트 ▶ 조동사 뒤 → 동사원형", [])
T.fixed('다음 중 어법상 <u>틀린</u> 문장의 개수는?', G, B(
 '(a) If I were a bird, I could fly to you.', '(b) If he has a car, he would drive to work.', '(c) If I lived in Alaska, I could go sledding all day.', '(d) What would you do if you meet a famous singer?', "(e) If it didn't rain, we would play soccer outside."),
 NUMS, 2,
 "이유 ▶ 틀린 것 (b)·(d) 2개. (b) 주절 would → If절은 과거형 had (d) would ~ if → 과거형 met\n오답 ▶ (a) be동사는 주어와 관계없이 were ✔ (c)·(e) If + 과거형, could/would ✔", [])
T.flex('다음 문장과 의미가 같은 것은?', G, B('If I had a sled, I could go sledding.'),
 ["As I don't have a sled, I can't go sledding.", 'As I have a sled, I can go sledding.', "As I didn't have a sled, I couldn't go sledding.", "If I don't have a sled, I can't go sledding.", 'Though I don\'t have a sled, I can go sledding.'],
 "이유 ▶ 가정법 과거 = 현재 사실의 반대 → 지금 썰매가 없어서 썰매를 탈 수 없다.\n오답 ▶ {1} 반대 {2} 시제를 과거로 착각 {3} 조건문(직설법) {4} 뜻이 다름", [])
T.flex('다음 중 어법상 올바른 문장은?', G, '',
 ['The mirrors would make the house almost invisible.', 'The thick walls keep me warmly in winter.', 'This song always makes me happily.', 'Regular exercise keeps you healthily.', 'The sad news made her sadly.'],
 "이유 ▶ make + 목적어 + 형용사(invisible) ✔\n오답 ▶ {1} warm {2} happy {3} healthy {4} sad — 목적격 보어 자리에 부사 ❌\n포인트 ▶ 목적어의 상태를 설명 → 형용사", [])
T.flex('다음 우리말을 영어로 바르게 옮긴 것은?', G, B('지금까지 베니스를 지탱하는 것은 바로 이 나무 기둥들이다.'),
 ['It is these wooden poles that support Venice to this day.', 'It is these wooden poles what support Venice to this day.', 'It is these wooden poles that supports Venice to this day.',
  'That is these wooden poles it supports Venice to this day.', 'It is these wooden poles support Venice to this day that.'],
 "이유 ▶ It is + 강조할 말 + that ~ / 강조되는 말이 these wooden poles(복수) → support.\n오답 ▶ {1} that 자리에 what ❌ {2} 복수 주어인데 supports {3}·{4} 어순 오류", [])
T.flex('7과 본문의 집과 그 특징이 바르게 연결되지 <u>않은</u> 것은?', R, '',
 ['tulou – has a flat roof to sleep on', 'pueblo – has walls made of earth, straw, and water', 'Venice – is supported by wooden poles', 'tulou – can house up to 50 families', 'pueblo – is entered by climbing a ladder'],
 "이유 ▶ 평평한 지붕 위에서 잠을 자는 것은 푸에블로(The house has a flat roof. I would sometimes sleep up on the roof).\n오답 ▶ {1}·{2}·{3}·{4} 모두 본문 내용과 일치", [])
T.flex('본문 마지막 문장 <u>What is your home like?</u>를 쓴 의도로 가장 알맞은 것은?', R, B('Homes are everywhere. But they are different all over the world. <u>What is your home like?</u>'),
 ['독자에게 자신의 집에 대해 생각해 보게 하려고', '독자가 좋아하는 집의 크기를 조사하려고', '독자의 집 주소를 물어보려고', '세계에서 가장 좋은 집을 추천하려고', '집을 고치는 방법을 알려 주려고'],
 "이유 ▶ 세계의 집은 다 다르다 → '여러분의 집은 어떤가요?' = 독자 자신의 집을 떠올리게 하는 질문.\n오답 ▶ {1}·{2}·{3}·{4} 모두 글의 흐름(세계의 다양한 집 → 여러분의 집은?)과 관계없음\n포인트 ▶ What is ~ like? = ~은 어떠니?(모습·특징)", [])
T.render()

# ═══════════════ 3회 (최상) ═══════════════
T = Test('3', '3회', '대화문 · 본문 · 문법', '7과 전 범위',
 '범위: 7과 대화문 · 본문 · 문법. 가장 어려운 단계예요. 개수·짝 고르기 문제는 문장 하나하나 ⭕ / ❌ 를 표시하며 풀어 보세요.', H=H)
body, a = ABC("G: Have you heard from Julia? She's traveling in Türkiye, right?", ['B: Yes, she sent me some pictures. Do you want to see them?', 'G: Yes, please. — B: Okay, take a look.', "G: Oh, look at those cave houses! They look so unique, don't they? I wish I could try living there."], 'BAC')
T.fixed('주어진 말 다음에 이어질 대화의 순서로 가장 알맞은 것은?', D, body, OPTS_ORD, a,
 "이유 ▶ Julia 소식? → (B) 응, 사진을 보내왔어. 볼래? → (A) 응, 보여 줘 / 자, 봐 → (C) 저 동굴 집들 좀 봐!\n포인트 ▶ (A)의 Yes, please는 (B)의 Do you want to see them?에 대한 대답", [])
T.flex('According to the dialogue, which house would B most like to live in, and why?', D, B('A: Look at these houses. They look very natural.', 'B: Wow, I wish I could try living there!', 'A: Which house would you most like to live in?', 'B: I wish I could live in the stone house. It looks very strong.'),
 ['the stone house, because it looks very strong', 'the stone house, because it looks very natural', 'the tree house, because it looks very strong', 'the cave house, because it looks unique', 'the snow house, because it looks fun'],
 "이유 ▶ I wish I could live in the stone house. It looks very strong. ✔\n오답 ▶ {1} natural은 집들 전체에 대한 A의 말 {2}·{3}·{4} 다른 집", [])
T.flex('다음 중 짝지어진 대화가 <u>어색한</u> 것은?', D, '',
 ["A: I wish I had a pet. — B: Oh, I'm glad that you have one.", 'A: What would you do if you had a time machine? — B: I would go back to the Joseon Dynasty.',
  "A: I wish I could visit Spain. — B: Me too. I'd love to see Gaudí's buildings.", 'A: Is it a kind of car? — B: Yes, it can move like a car.', "A: Would it be easy to live in the upside-down house? — B: No, it wouldn't."],
 "이유 ▶ I wish I had a pet = 지금 애완동물이 없다는 뜻. 그런데 '네가 하나 있어서 기쁘다'고 답하면 어색.\n오답 ▶ {1} 가정 질문 → I would ~ ✔ {2} 소망에 동의 ✔ {3} 질문에 맞는 답 ✔ {4} Would it ~? → No, it wouldn't ✔\n포인트 ▶ I wish + 과거형 = 현재 사실의 반대", [])
T.flex('다음 대화의 빈칸에 들어갈 말로 알맞은 것은?', D, B("B: Isn't that the church Antoni Gaudí designed?", 'G: Yes, it is. It would be interesting to see how his design ' + BL + ' nature.'),
 ['was inspired by', 'inspired', 'was inspiring', 'inspires by', 'is inspired'],
 "이유 ▶ 디자인이 자연으로부터 '영감을 받았다' → 수동태 be inspired by. 이미 지어진 성당의 디자인 → 과거 was.\n오답 ▶ {1} 능동(디자인이 자연에 영감을 줬다)이라 뜻이 반대 {2} 진행형 능동 {3} 능동 + by ❌ {4} by가 없어 nature와 연결되지 않음", [])
T.flex('다음 대화를 읽고 답할 수 <u>없는</u> 질문은?', D, B(
 'B: Will it snow today?', 'G: I have no idea. Why are you waiting for snow, Taeho?', "B: I got a new sled for my birthday. I can't wait to test it out.", 'G: Let me check the weather. Umm, there will be no snow for a while.',
 'B: I wish I could live in Alaska. Then I could go sledding all day!', 'G: No kidding! Alaska is a very cold place.', 'B: I think it would be fun. I want to build a snow house and stay there on vacation.'),
 ['How long will Taeho stay in Alaska?', 'What did Taeho get for his birthday?', 'Why is Taeho waiting for snow?', 'Will it snow for a while?', 'What does Taeho want to build?'],
 "이유 ▶ 태호가 알래스카에 얼마나 머물지는 나오지 않는다(소망일 뿐).\n오답 ▶ {1} a new sled {2} 새 썰매를 시험해 보고 싶어서 {3} no snow for a while {4} a snow house", [])
T.flex('다음 빈칸에 들어갈 말로 알맞은 것은?', D, B('I would build a house ' + BL + ' is completely covered with mirrors.'),
 ['that', 'what', 'who', 'where', 'it'],
 "이유 ▶ 선행사 a house(사물) + 뒤에 주어가 빠진 절(is covered ~) → 주격 관계대명사 that(= which).\n오답 ▶ {1} what은 선행사를 포함 {2} who는 사람 {3} where 뒤에는 완전한 절 {4} it을 쓰면 접속사 없이 절이 두 개", [])
T.fixed('다음 글의 ①~⑤ 중 전체 흐름과 관계없는 문장은?', R, B(
 'If I lived in a pueblo, I would climb up a ladder to enter my house. ① There\'s a hidden opening on top of the house. ② If unwelcome visitors appeared, I would pull the ladder up to stop them from entering. '
 '③ Ladders were first used by people in ancient Egypt. ④ The thick walls are made of earth, straw, and water. ⑤ The house has a flat roof.'),
 None, 3,
 "이유 ▶ 푸에블로에 산다면 어떨지 상상하는 글. 사다리가 처음 쓰인 역사는 흐름과 관계없다.", [])
T.table('다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 알맞은 것은?', R, B(PUE) + '\n' + SUM('The pueblo\'s <b>(A)</b> ' + BL + ' walls help keep the temperature inside <b>(B)</b> ' + BL + ' all year round.'),
 ['(A)', '(B)'], [['thick', 'comfortable'], ['thin', 'comfortable'], ['flat', 'cold'], ['thick', 'dangerous'], ['hidden', 'hot']],
 "이유 ▶ (A) The thick walls (B) 여름엔 시원하게, 겨울엔 따뜻하게 → 일 년 내내 '쾌적하게(comfortable)'\n오답 ▶ thin은 반대 / flat은 지붕 / cold·hot은 한 계절만 / dangerous는 근거 없음", [])
T.flex('다음 빈칸에 들어갈 말로 가장 알맞은 것은?', R, B('At high tide, the water from the Adriatic Sea often rises and leaves the streets full of water. ' + BL + ', I would be able to walk around the town through the raised walkways.'),
 ['However', 'Therefore', 'For example', 'In addition', 'As a result'],
 "이유 ▶ 거리가 물에 잠긴다(문제) ↔ 그래도 높은 통로로 걸어 다닐 수 있다 → 대조 However(그러나).\n오답 ▶ {1}·{4} 결과(그래서)가 아니라 반대 상황 {2} 예시 아님 {3} 추가 아님", [])
T.flex('다음 글의 내용과 일치하는 것은?', R, B(VEN2),
 ['옛 베니스인들은 습지 위에 집 짓기가 쉽지 않아 땅에 나무 기둥을 설치했다.', '베니스의 집들은 대부분 한 가지 색으로 칠해져 있다.', '베니스 사람들은 물고기를 잡기 위해 물 위에 살기 시작했다.',
  '오늘날 베니스는 콘크리트 기둥이 지탱하고 있다.', '나무 기둥은 백만 개 정도 설치되었다.'],
 "이유 ▶ not easy ~ on this swampy surface. So they installed more than 10 million wooden poles ✔\n오답 ▶ {1} colorful houses(색색의) {2} 침략자로부터 안전하려고 {3} these wooden poles that support Venice to this day {4} 천만 개 이상(10 million)", [])
T.fixed('다음 글의 밑줄 친 (a)~(g) 중 어법상 <u>틀린</u> 것의 개수는?', R, B(
 'I would sometimes hear my neighbor ' + TG('a', 'calling') + ' me to come over for tea. In a tulou, there ' + TG('b', 'is') + ' usually three to five floors. The first floor ' + TG('c', 'is used') +
 ' for cooking and eating. Do you wonder where ' + TG('d', 'would I sleep') + '? The people ' + TG('e', 'living') + ' in a tulou mostly ' + TG('f', 'has') + ' the same family name. Living together in one building ' + TG('g', 'keeps') + ' them safe.'),
 NUMS, 3,
 "이유 ▶ 틀린 것 (b)·(d)·(f) 3개. (b) three to five floors(복수) → are (d) 간접의문문 어순 → where I would sleep (f) 주어 The people(복수) → have\n오답 ▶ (a) hear + 목적어 + -ing ✔ (c) 층이 '사용되는' 수동 ✔ (e) 사람들이 '사는' 능동 ✔ (g) 동명사 주어 → 단수 ✔", [])
T.flex('토루에서의 생활을 가장 잘 나타내는 것은?', R, B(TUL2),
 ['community and cooperation', 'privacy and independence', 'competition and conflict', 'travel and adventure', 'silence and loneliness'],
 "이유 ▶ 마을 같음, 같은 성, 50가구, 함께 일하고 나눔(work together and share), 함께 살아 안전 → 공동체와 협력.\n오답 ▶ {1}·{2}·{4} 반대 {3} 정글 대화의 주제", [])
T.flex('다음 중 두 문장의 의미가 서로 <u>다른</u> 것은?', G, '',
 ['If I lived in Venice, I would take a gondola. = I live in Venice, so I take a gondola.', "As I am not tall, I can't reach the shelf. = If I were tall, I could reach the shelf.",
  "If she had time, she would help us. = As she doesn't have time, she won't help us.", "I am sorry that I can't fly. = I wish I could fly.", "As it is raining, we can't go out. = If it weren't raining, we could go out."],
 "이유 ▶ 가정법 과거(If I lived in Venice) = 실제로는 베니스에 살지 않는다. 오른쪽은 실제로 산다는 뜻이라 반대.\n오답 ▶ {1}·{2}·{4} 직설법 ↔ 가정법 과거 ✔ {3} I wish = I am sorry that ~ 못 해서 ✔", [])
T.fixed('다음 중 어법상 올바른 문장끼리 바르게 짝지은 것은?', G, B(
 'ⓐ If I were you, I would keep the window open.', 'ⓑ The thick walls would keep me coolly in summer.', 'ⓒ If he knew her number, he will call her.', 'ⓓ What would you do if you became a millionaire?', 'ⓔ The mirrors would make the house invisible.'),
 ['ⓐ, ⓑ', 'ⓑ, ⓒ', 'ⓐ, ⓓ', 'ⓐ, ⓓ, ⓔ', 'ⓒ, ⓓ, ⓔ'], 4,
 "이유 ▶ 올바른 것 ⓐ·ⓓ·ⓔ.\n오답 ▶ ⓑ keep + 목적어 + 형용사 → cool ⓒ 가정법 과거 → would call\n포인트 ▶ ③은 ⓔ가 빠진 함정 — 올바른 것을 '모두' 담은 선택지!", [])
T.flex('다음 우리말을 영어로 바르게 옮긴 것은?', G, B('만약 내가 토루에 산다면, 나는 항상 집에 함께 놀 친구들이 있을 텐데.'),
 ['If I lived in a tulou, I would always have friends at home to play with.', 'If I lived in a tulou, I would always have friends at home to play.', 'If I live in a tulou, I would always have friends at home to play with.',
  'If I lived in a tulou, I will always have friends at home to play with.', 'If I lived in a tulou, I would always had friends at home to play with.'],
 "이유 ▶ 가정법 과거 + friends to play with(함께 놀 친구 — play with friends이므로 with 필요).\n오답 ▶ {1} with 빠짐 {2} If절 현재형 {3} 주절 will {4} would 뒤 동사원형 have", [])
T.flex('다음 밑줄 친 to부정사와 쓰임이 같은 것은?', G, B('If unwelcome visitors appeared, I would pull the ladder up <u>to stop</u> them from entering.'),
 ['Some people use ladders to enter their houses.', 'It was not easy for them to build their homes.', 'I would always have friends to play with.', 'The old Venetians decided to live there.', 'I hope to visit Türkiye some day.'],
 "이유 ▶ to stop = ~하기 위해(목적, 부사적 용법). 사다리를 이용하는 목적 to enter와 같다.\n오답 ▶ {1} 진주어(명사적) {2} 명사 friends를 꾸밈(형용사적) {3}·{4} 목적어(명사적)", [])
T.flex('다음 중 어법상 올바른 문장은?', G, '',
 ['I heard someone call my name.', 'I saw her to dance on the stage.', 'He made me to clean my room.', 'The news made us happily.', 'I heard the birds sang in the tree.'],
 "이유 ▶ 지각동사 hear + 목적어 + 동사원형(또는 -ing) ✔\n오답 ▶ {1} saw her dance[dancing] {2} 사역 make + 동사원형 clean {3} happy {4} sing[singing]", [])
body, a = ABC('Different people live in different houses.', ['Some use ladders to enter their houses. Others live in houses on the water.', 'And others share their houses with many people.', 'Imagine you live in one of these houses. How would that change your life?'], 'CAB')
T.fixed('주어진 문장 다음에 이어질 글의 순서로 가장 알맞은 것은?', R, body, OPTS_ORD, a,
 "이유 ▶ 다양한 집 → (C) Some ~, Others ~ → (A) And others ~ → (B) 이 집들 중 하나에 산다고 상상해 보라.\n포인트 ▶ Some → Others → (And) others 나열 / these houses는 앞에 나온 집들을 가리킴", [])
T.flex('7과 본문의 주제로 가장 알맞은 것은?', R, '',
 ["how houses reflect people's surroundings and ways of life", 'why people should live with big families', 'the dangers of living on the water', 'the best kind of house to live in', 'how to design a house with mirrors'],
 "이유 ▶ 침입자를 막는 사다리, 기후에 맞는 두꺼운 벽, 침략을 피한 물 위의 집, 함께 사는 토루 → 집은 환경과 생활 방식을 반영.\n오답 ▶ {1} 토루 한 부분 {2} 위험이 주제가 아님 {3} 최고의 집을 고르지 않음 {4} 대화문 내용\n어휘 ▶ reflect 반영하다 · surroundings 환경", [])
T.table('7과 본문 전체를 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 알맞은 것은?', R, SUM(
 'People around the world live in <b>(A)</b> ' + BL + ' houses, and each home reflects the <b>(B)</b> ' + BL + ' of the people living in it.'),
 ['(A)', '(B)'], [['different', 'way of life'], ['similar', 'way of life'], ['different', 'family name'], ['modern', 'language'], ['similar', 'hometown']],
 "이유 ▶ (A) Homes are everywhere. But they are different all over the world. → different (B) 사다리로 오르내리기, 곤돌라 통학, 이웃과 함께 사는 삶 → 생활 방식(way of life)\n오답 ▶ similar는 반대 / family name은 토루의 세부 / modern·language는 근거 없음", [])
T.render()
