# 11/22 중산중3 7·8과 최종 점검 1·2회 (월요일 시험 전 직보용) — 중산중 2025 기출(k25)과 같은 배점 순서·25문항·45분, 정답 ①~⑤ 각 5개
# 구성: 대화문 4 · 문법 4 · 본문(꼭 외울 문장 영작·삽입·어법·내용) 8 · 외부지문 1 일본 전통 가옥(Reading File) 4 · 외부지문 2 Picture Bride 4 · 종합 1
# Picture Bride는 저작권 있는 시라 원문을 싣지 않고 프린트 칸 번호와 내 말로 쓴 장면 요약으로만 물음(4단어 이상 겹침 검사)
import sys
sys.path.insert(0, '/home/claude/srcrepo/wrapup')
from wu_k25v import *
H = ('최종 점검', '중산중 7·8과 최종 점검', '중산중 7·8과 최종 점검', 'm3fin')
Bx = lambda *ls: BOX('<br>'.join(ls))
N = '월요일 시험 전 마지막 점검이에요. 작년 중산중 기출과 같은 배점·난이도로 대화문·문법·본문(영작·삽입)·외부지문 두 개(일본 전통 가옥, Picture Bride)를 섞었어요. 45분 안에 풀고 OMR에 답을 입력하세요.'
K25 = [3, 3, 3, 3, 4, 3, 4, 5, 4, 3, 4, 4, 3, 4, 5, 4, 5, 5, 5, 5, 3, 5, 4, 5, 4]
JH = Bx("What would it be like to live in a traditional Japanese house? If you lived there, you would have to take off your shoes in the <i>genkan</i>, an entrance hall, before entering the house. "
        "In the house, many Japanese do not use chairs. Instead, they sit directly on <i>tatami</i> mats that are made from woven grass. "
        "Rooms are divided by <i>shoji</i>, portable sliding doors that are made from wood and thin paper. For large gatherings, these doors can be removed to create one large room. "
        "When the weather gets cold, people prefer to sit at a <i>kotatsu</i>, a heated table, and put their legs in it. Keeping their body warm, Japanese have meals, drink tea, or read books at the table. "
        "In summer, heavy rain can cause flooding. The floor of the house is raised a little off the ground to keep the living area dry and safe from flooding. "
        "The house also has sloped roofs because they keep rainwater flowing off easily. The roofs are covered with <i>kawara</i> tiles. The strong <i>kawara</i> tiles are not only water-resistant but also fireproof.")
PBN = '※ Picture Bride(Cathy Song)는 학교 프린트의 시와 해석을 떠올리며 푸세요. (프린트 3쪽 표의 칸 순서)'

# ══════════════════════════ 1회 ══════════════════════════
T1 = Test('1', '1회', '7·8과 최종 점검 1회', '중산중 최종 점검', N, H=H)
# 1 대화 7과 L&S 1-A (3)
T1.flex('다음 대화의 내용과 일치하지 <u>않는</u> 것은?', '7과 대화', Bx(
 "A: Have you heard from Julia? She's traveling in Türkiye, right?", "B: Yes, she sent me some pictures. Do you want to see them?", "A: Yes, please.", "B: Okay, take a look.",
 "A: Oh, look at those cave houses! They look so unique, don't they? I wish I could try living there.", "B: I like those balloons. They look so beautiful!",
 "A: I think Türkiye is a wonderful place to visit. I hope to visit there some day.", "B: Me too!"),
 ['A has already lived in a cave house in Türkiye.', 'Julia is traveling in Türkiye now.', 'Julia sent B some pictures.', 'B thinks the balloons look beautiful.', 'Both A and B hope to visit Türkiye.'],
 "이유 ▶ I wish I could try living there. = 살아 보고 싶지만 지금은 그럴 수 없다(가정법 과거) → 살아 본 적이 있다는 건 함정\n오답 ▶ {1} She's traveling in Türkiye {2} she sent me some pictures {3} They look so beautiful {4} I hope to visit ~ / Me too!",
 [('cave', '동굴'), ('unique', '독특한')], 3)
# 2 대화 7과 L&S 1-B 빈칸 (3)
T1.flex('다음 대화의 빈칸에 들어갈 말로 가장 알맞은 것은?', '7과 대화', Bx(
 "A: Will it snow today?", "B: I have no idea. Why are you waiting for snow, Taeho?", "A: I got a new sled for my birthday. I can't wait to test it out.",
 "B: Let me check the weather. Umm, there will be no snow for a while.", "A: ______________________ Then I could go sledding all day!", "B: No kidding! Alaska is a very cold place."),
 ['I wish I could live in Alaska.', 'I wish I lived in a hot country.', "I'm glad it will snow tomorrow.", 'I hope it will rain all day.', "I don't like cold weather at all."],
 "이유 ▶ 뒤 문장 Then I could go sledding all day! + B의 Alaska is a very cold place → 알래스카에 살면 좋겠다는 소망(I wish + 과거)\n오답 ▶ {1} 더운 나라(썰매와 반대) {2} 당분간 눈이 오지 않음 {3} 비 {4} 추운 날씨를 싫어함 → 흐름과 반대",
 [('sled', '썰매'), ('for a while', '당분간')], 3)
# 3 대화 8과 L&S 2-B (3)
T1.flex('다음 대화를 읽고 알 수 <u>없는</u> 것은?', '8과 대화', Bx(
 "A: Jian, what's the matter? You look very upset.", "B: My brother broke my computer. I'm so angry.", "A: I'm sorry to hear that, but your facial muscles must be tired.", "B: What do you mean?",
 "A: Well, it takes a lot of muscles to look angry, but only a few to smile. Do you see what I mean?", "B: Oh, I get it. I guess it's not good to stay angry for a long time.", "A: That's right. Remember, it's always better to smile."),
 ['how many muscles it takes to smile exactly', 'why Jian is angry', 'who broke Jian\'s computer', 'what A thinks about smiling', 'what Jian realized at the end'],
 "이유 ▶ only a few(몇 개만)라고만 하고 정확한 근육 수는 나오지 않음\n오답 ▶ {1} 동생이 컴퓨터를 고장 냄 {2} My brother {3} it's always better to smile {4} 오래 화내는 건 좋지 않다",
 [('facial muscle', '얼굴 근육'), ('upset', '속상한')], 3)
# 4 대화 8과 Real Life 수치 (3)
T1.flex('다음 대화의 내용과 일치하는 것은?', '8과 대화', Bx(
 "A: Henry, what are you doing?", "B: I'm writing an article about students' favorite snacks. I'm worried about their health.", "A: Why?",
 "B: Well, I surveyed 100 students and the results show that eighty percent of the students liked pizza and fried chicken for snacks. Do you see what I mean?",
 "A: Oh, I get it. Students really like fast food. What else did they like?", "B: Twelve percent of the students chose chocolate cake as their favorite.", "A: Wow, students should really try to eat healthier snacks!"),
 ['Twelve students chose chocolate cake as their favorite snack.', 'Henry surveyed eighty students.', 'Most students chose healthy snacks.', 'Henry is writing an article about fast food restaurants.', 'Twenty students liked pizza and fried chicken.'],
 "이유 ▶ 100명 중 12% = 12명 ✔\n오답 ▶ {1} 100명을 조사 {2} 80%가 피자·치킨(패스트푸드) {3} 좋아하는 간식에 관한 기사 {4} 80명",
 [('survey', '조사하다'), ('article', '기사')], 3)
# 5 가정법 과거 옳은 문장 (4)
T1.flex('다음 중 어법상 옳은 문장은?', '7과 문법', '',
 ['If I lived in Venice, I would take a gondola to school.', 'If I live in a pueblo, I would climb up a ladder.', 'If I were rich, I will build a mirror house.', 'If she has wings, she could fly to Hawaii.', 'If they knew the answer, they can tell us.'],
 "이유 ▶ 가정법 과거: If + 주어 + 동사 과거형 ~, 주어 + would/could + 동사원형 ✔\n오답 ▶ {1} live → lived {2} will → would {3} has → had {4} can → could",
 [('gondola', '곤돌라')], 4)
# 6 make/keep (3)
T1.flex('다음 빈칸에 들어갈 말로 알맞은 것은?', '7과 문법', Bx('The thick walls would keep me ______ in summer and warm in winter.'),
 ['cool', 'coolly', 'to cool', 'cooling', 'be cool'],
 "이유 ▶ keep + 목적어 + 형용사(목적격보어) → cool (and warm과 나란히 형용사)\n오답 ▶ {1} 부사 X {2}{3}{4} keep + 목적어 + 형용사 자리에 올 수 없음",
 [('thick', '두꺼운')], 3)
# 7 too ~ to 전환 (4)
T1.flex('다음 문장과 의미가 같은 것은?', '8과 문법', Bx('The king is so greedy that he can\'t share with the people.'),
 ['The king is too greedy to share with the people.', 'The king is greedy enough to share with the people.', 'The king is too greedy to not share with the people.', 'The king is so greedy that he can share with the people.', 'The king is not greedy, so he shares with the people.'],
 "이유 ▶ so ~ that 주어 can't … = too ~ to … (너무 ~해서 …할 수 없다) ✔ 본문: He is too greedy to share with the people.\n오답 ▶ {1} enough to = 충분히 ~해서 …할 수 있다(반대) {2} to not(뜻 반대) {3} can(반대) {4} 욕심이 없다(반대)",
 [('greedy', '욕심 많은')], 4)
# 8 No one / 부분부정 (5)
T1.flex('다음 중 의미가 나머지 넷과 <u>다른</u> 하나는?', '8과 문법', '',
 ['Not everyone needs graphs in real life.', 'No one needs graphs in real life.', 'Nobody needs graphs in real life.', 'None of the people need graphs in real life.', 'Not a single person needs graphs in real life.'],
 "이유 ▶ Not everyone = 모두가 ~한 것은 아니다(부분 부정) → 필요한 사람도 있음\n오답 ▶ {1}{2}{3}{4} 아무도 필요로 하지 않는다(전체 부정)\n포인트 ▶ 본문 Pascal: No one needs graphs in real life.(전체 부정)",
 [('real life', '실생활')], 5)
# 9 본문 pueblo 내용 (4)
T1.flex('다음 글의 내용과 일치하지 <u>않는</u> 것은?', '7과 본문 ❶', Bx(
 "If I lived in a pueblo, I would climb up a ladder to enter my house. There's a hidden opening on top of the house. If unwelcome visitors appeared, I would pull the ladder up to stop them from entering. "
 "The thick walls are made of earth, straw, and water. They would keep me cool in summer and warm in winter. The house has a flat roof. I would sometimes sleep up on the roof under the moon and stars."),
 ['The opening of a pueblo is on the side of the house so that anyone can see it.', 'People climb a ladder to enter a pueblo.', 'Pulling up the ladder can stop unwelcome visitors.', 'The walls of a pueblo are made of earth, straw, and water.', 'A pueblo has a flat roof to sleep on.'],
 "이유 ▶ There's a hidden opening on top of the house. → 입구는 '지붕 위'에 '숨겨져' 있음\n오답 ▶ {1} climb up a ladder {2} pull the ladder up to stop them {3} earth, straw, and water {4} flat roof, sleep up on the roof",
 [('opening', '입구, 구멍'), ('unwelcome', '반갑지 않은')], 4)
# 10 Venice 삽입 (3)
T1.fixed('글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳은?', '7과 본문 ❷', Bx(
 "<b>So they installed more than 10 million wooden poles in the ground.</b>", "",
 "In Venice, there are many colorful houses on the water. ( ① ) You may wonder how and why they built the houses on the water. ( ② ) The old Venetians decided to live there to keep themselves safe from invaders. "
 "( ③ ) But it was not easy for them to build their homes on this swampy surface. ( ④ ) It is these wooden poles that support Venice to this day. ( ⑤ )"),
 None, 4,
 "이유 ▶ 늪 같은 땅에 집 짓기가 쉽지 않았다 → 그래서(So) 천만 개 넘는 나무 기둥을 박았다 → 바로 이 나무 기둥들(these wooden poles)이 지금도 베네치아를 받친다\n오답 ▶ ③ 앞은 '왜' 물 위에 살았는지(침략자) — 아직 어려움이 나오지 않음 / ⑤ these wooden poles가 주어진 문장보다 먼저 나오게 됨",
 [('install', '설치하다'), ('swampy', '늪 같은'), ('surface', '표면')], 3)
# 11 tulou 영작 배열 (4)
T1.flex('다음 우리말을 영작할 때 <u>네 번째</u>로 오는 단어는?', '7과 본문 ❸ 영작', Bx('한 건물에서 함께 사는 것이 그들을 안전하게 지켜 준다.', '( them / together / keeps / in / living / safe / building / one )'),
 ['one', 'in', 'together', 'keeps', 'building'],
 "(아래에서 덮어씀)",
 [('keep A safe', 'A를 안전하게 지키다')], 4)
# 12 Venice 강조 구문 영작 (4)
T1.flex('다음 우리말을 바르게 영작한 것은?', '7과 본문 ❷ 영작', Bx('오늘날까지 베네치아를 받치고 있는 것은 바로 이 나무 기둥들이다.'),
 ['It is these wooden poles that support Venice to this day.', 'It is these wooden poles what support Venice to this day.', 'It is these wooden poles that supports Venice to this day.', 'These wooden poles is that support Venice to this day.', 'It was Venice that support these wooden poles to this day.'],
 "이유 ▶ It is + 강조할 말(these wooden poles) + that ~ (바로 ~이다) / 강조되는 주어가 복수 → support ✔\n오답 ▶ {1} what X(강조 구문은 that) {2} supports X(poles 복수) {3} is ~ that 구조 X {4} 받치는 것과 받쳐지는 것이 뒤바뀜",
 [('support', '받치다, 지탱하다'), ('to this day', '오늘날까지')], 4)
# 13 Pascal 삽입 (3)
T1.fixed('글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳은?', '8과 본문 ❶', Bx(
 "<b>It was his dog, Manny, who was talking!</b>", "",
 "He put down his pen and picked up his favorite book, <i>Robin Hood</i>. ( ① ) He decided to read himself to sleep. ( ② ) When he was about to open the book, he heard a voice. "
 "( ③ ) He looked up from the book to see who was talking. ( ④ ) He couldn't believe his eyes. ( ⑤ ) \"Close your eyes and repeat after me. <i>Cogito ergo sum</i>,\" said Manny."),
 None, 5,
 "이유 ▶ 누가 말하는지 보려고 고개를 듦 → 자기 눈을 믿을 수 없었다 → (왜냐하면) 말하고 있던 건 바로 개 Manny였다 → Manny의 말\n오답 ▶ ④ 눈을 믿을 수 없었다는 반응보다 정체가 먼저 나오면 어색 / ③ 아직 고개를 들어 보지도 않음\n포인트 ▶ It was ~ who … 강조 구문",
 [('be about to', '막 ~하려던 참이다'), ('can\'t believe one\'s eyes', '눈을 의심하다')], 3)
# 14 8과 본문 어법 (4)
T1.fixed('다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 옳지 <u>않은</u> 것은?', '8과 본문 ❸', Bx(
 "\"Well, can you help us ⓐ <u>get</u> back the money ⓑ <u>that</u> the king took from the people? He taxed them too much. He is too greedy ⓒ <u>to share</u> with the people, so they don't have enough money ⓓ <u>buying</u> food. "
 "I want to help them get their money back. However, there are many soldiers in the tower, so no one ⓔ <u>can get</u> inside.\""),
 ['ⓐ', 'ⓑ', 'ⓒ', 'ⓓ', 'ⓔ'], 4,
 "이유 ▶ enough money to buy food(음식을 살 충분한 돈) — 명사를 꾸미는 to부정사 → buying ❌\n오답 ▶ ⓐ help + 목적어 + 동사원형 ⓑ 목적격 관계대명사 that ⓒ too ~ to ⓔ no one + 조동사 can",
 [('tax', '세금을 매기다'), ('greedy', '욕심 많은')], 4)
# 15 그래프 계산 (5)
T1.flex('다음 글의 내용으로 알 수 있는 것으로 가장 적절한 것은?', '8과 본문 ❹', Bx(
 "\"There are five soldiers from midnight to six in the morning. Next, there are three soldiers until noon, and then there are eight soldiers until six in the evening. Lastly, there are twelve soldiers until midnight. "
 "So, you should go inside between six in the morning and noon.\"", "\"What? I don't get it.\"", "Pascal thought for a moment. 'Hmm... A graph might make this easier to understand.'",
 "Pascal drew a graph and showed it to Robin. \"Look, the most dangerous time is between six in the evening and midnight. Four times more soldiers work at that time than from six in the morning until noon.\""),
 ['Between six in the evening and midnight, there are nine more soldiers than between six in the morning and noon.', 'There are more soldiers in the afternoon than late at night.', 'The safest time is from midnight to six in the morning.', 'There are twenty soldiers in the tower in total at any time.', 'Robin understood the plan before Pascal drew the graph.'],
 "이유 ▶ 저녁 6시~자정 12명 − 오전 6시~정오 3명 = 9명 더 많음 ✔ (12 = 3의 4배)\n오답 ▶ {1} 오후 8명 < 밤 12명 {2} 가장 안전한 때는 오전 6시~정오(3명) {3} 시간대마다 다름 {4} 처음엔 I don't get it",
 [('midnight', '자정'), ('noon', '정오')], 5)
# 16 too greedy 영작 (4)
T1.flex('다음 우리말을 영작할 때 쓰이지 <u>않는</u> 단어는?', '8과 본문 영작', Bx('그래프가 이것을 이해하기 더 쉽게 만들어 줄지도 몰라.', '(조건: 본문 8과 Pascal의 생각을 그대로, 조동사 might를 쓸 것)'),
 ['easily', 'might', 'make', 'easier', 'understand'],
 "이유 ▶ make + 목적어(this) + 형용사(easier) + to understand → 부사 easily는 쓰지 않음\n오답 ▶ {1} 조동사 might(~일지도 모른다) {2} 5형식 make {3} 형용사 비교급 목적격보어 {4} to understand",
 [('might', '~일지도 모른다')], 4)
# 17 일본 가옥 내용 함정 (5)
T1.flex('[17~20] 다음 글을 읽고 물음에 답하시오.<br>17. 윗글의 내용과 일치하지 <u>않는</u> 것은?', '외부지문 · Reading File', JH,
 ['Shoji are heavy wooden walls that cannot be moved.', 'People take off their shoes in the genkan before going inside.', 'Tatami mats are made from woven grass.', 'A kotatsu is a heated table people put their legs in.', 'Kawara tiles are both water-resistant and fireproof.'],
 "이유 ▶ shoji = portable sliding doors (wood and thin paper) → 옮길 수 있는 미닫이문, 떼어 내 큰 방을 만들 수 있음 → '옮길 수 없는 무거운 벽'은 함정\n오답 ▶ {1} genkan에서 신발을 벗음 {2} woven grass {3} a heated table, put their legs in it {4} not only water-resistant but also fireproof",
 [('portable', '휴대용의, 옮길 수 있는'), ('woven', '짠, 엮은')], 5)
# 18 일본 가옥 삽입 (5)
T1.fixed('18. 윗글의 흐름으로 보아, 다음 문장이 들어가기에 가장 적절한 곳은?', '외부지문 · Reading File', Bx(
 "<b>For large gatherings, these doors can be removed to create one large room.</b>", "",
 "In the house, many Japanese do not use chairs. ( ① ) Instead, they sit directly on tatami mats that are made from woven grass. ( ② ) Rooms are divided by shoji, portable sliding doors that are made from wood and thin paper. "
 "( ③ ) When the weather gets cold, people prefer to sit at a kotatsu, a heated table, and put their legs in it. ( ④ ) Keeping their body warm, Japanese have meals, drink tea, or read books at the table. ( ⑤ )"),
 None, 3,
 "이유 ▶ 방은 shoji(옮길 수 있는 미닫이문)로 나뉜다 → 큰 모임 때는 이 문들(these doors)을 떼어 하나의 큰 방을 만든다\n오답 ▶ ② these doors가 가리킬 문이 아직 없음 / ④⑤ kotatsu 이야기 중간",
 [('gathering', '모임'), ('remove', '떼어 내다')], 5)
# 19 일본 가옥 요약 (5)
T1.flex('19. 윗글의 내용을 한 문장으로 요약할 때 빈칸 (A), (B)에 들어갈 말로 가장 알맞은 것은?', '외부지문 · Reading File', Bx(
 "A traditional Japanese house is designed to keep people ____(A)____ in cold weather and to protect the house from ____(B)____ and fire."),
 ['(A) warm − (B) water', '(A) cool − (B) water', '(A) warm − (B) wind', '(A) busy − (B) visitors', '(A) cool − (B) snow'],
 "이유 ▶ (A) kotatsu로 몸을 따뜻하게(Keeping their body warm) (B) 바닥을 높여 홍수를 막고, 경사 지붕으로 빗물을 흘려보내고, kawara는 방수·방화 → 물(water)\n오답 ▶ {1} cool(추운 날씨와 반대) {2} 바람은 언급 없음 {3} 방문객 X {4} 눈 X",
 [('protect A from B', 'B로부터 A를 보호하다')], 5)
# 20 일본 가옥 영작 (5)
T1.flex('20. 윗글의 내용과 일치하도록 다음 우리말을 영작할 때 가장 알맞은 것은?', '외부지문 · Reading File 영작', Bx('바닥은 거주 공간을 홍수로부터 건조하고 안전하게 지키기 위해 땅에서 약간 높여져 있다.'),
 ['The floor is raised a little off the ground to keep the living area dry and safe from flooding.', 'The floor raises a little off the ground to keep the living area dry and safe from flooding.', 'The floor is raised a little off the ground to keep the living area dryly and safely from flooding.', 'The floor is raised a little off the ground keeping the living area wet from flooding.', 'The ground is raised a little off the floor to keep the flooding dry and safe.'],
 "이유 ▶ 바닥이 '높여지는' → 수동 is raised / 목적 to keep / keep + 목적어 + 형용사(dry and safe) ✔\n오답 ▶ {1} 능동 raises X {2} 부사 dryly·safely X {3} wet(반대) {4} 바닥과 땅이 뒤바뀜",
 [('raise', '높이다'), ('flooding', '홍수')], 5)
# 21~24 Picture Bride
T1.flex('[21~24] 외부지문 Picture Bride<br>' + PBN + '<br>21. 시의 내용과 일치하는 것은?', '외부지문 · Picture Bride', '',
 ['The grandmother left Korea when she was twenty-three.', 'The speaker is now twenty-two years old.', 'The grandmother left from the port of Incheon.', 'The man had met the grandmother in Korea before.', 'The husband was thirteen years younger than the grandmother.'],
 "이유 ▶ 할머니는 스물셋에 한국을 떠남 ✔ (프린트 Activity 정답: 23세)\n오답 ▶ {1} 화자보다 한 살 어린 나이 → 화자는 지금 24세 {2} 부산 항구 {3} 사진만 보고 기다림(처음 만남) {4} 13살 '많았음'",
 [('port', '항구'), ('senior', '연상, 손위')], 3)
T1.flex('22. 시에서 화자가 할머니의 일을 계속 질문하는 이유로 가장 알맞은 것은?', '외부지문 · Picture Bride', '',
 ['The speaker can only imagine her grandmother\'s feelings and experience.', 'The speaker wants to blame her grandmother for leaving.', 'The speaker already knows every detail of the trip.', 'The speaker is planning to move to Hawaii herself.', 'The speaker is angry at the man in the photograph.'],
 "이유 ▶ 화자는 할머니가 무엇을 챙겼는지, 떠나는 게 쉬웠는지 알 수 없음 → 질문으로 할머니의 마음과 경험을 '상상'함\n오답 ▶ {1} 탓하는 태도 X {2} 알 수 없다고 함(반대) {3} 이주 계획 X {4} 분노 X",
 [('imagine', '상상하다'), ('blame', '탓하다')], 5)
T1.fixed('23. 시의 내용을 일어난 순서대로 바르게 나열한 것은?', '외부지문 · Picture Bride', Bx(
 '(a) She met her husband, a stranger, for the first time.', '(b) She walked past the tailor shops in Pusan.', '(c) A ship carried her across the sea to Hawaii.', '(d) The hot wind blew her long skirt in the sugarcane fields.'),
 ['(b) − (c) − (a) − (d)', '(b) − (a) − (c) − (d)', '(c) − (b) − (a) − (d)', '(a) − (b) − (c) − (d)', '(b) − (c) − (d) − (a)'], 1,
 "이유 ▶ 부산 양복점을 지나 항구로(b) → 배로 하와이까지(c) → 도착해 낯선 남편을 처음 만남(a) → 사탕수수 밭의 뜨거운 바람이 치마를 부풀림(d)",
 [('tailor shop', '양복점'), ('sugarcane', '사탕수수')], 4)
T1.flex('24. 시의 내용으로 보아 다음 설명 중 <u>틀린</u> 것은?', '외부지문 · Picture Bride', '',
 ['The man lived in a comfortable house in a big city.', 'The man was holding her picture up to the light.', 'The man lived in a workers\' camp near a sugar mill.', 'Moths from the sugarcane fields came into his room.', 'A picture bride married a man after seeing only his photograph.'],
 "이유 ▶ 남자는 설탕 공장 근처 '노동자 숙소'의 작은 방에 살았음 → 큰 도시의 편안한 집은 함정\n오답 ▶ {1} 사진을 빛에 비춰 봄 {2} Waialua 설탕 공장 근처 노동자 숙소 {3} 사탕수수 밭에서 나방이 날아듦 {4} 사진신부 = 사진만 보고 결혼",
 [('workers\' camp', '노동자 숙소'), ('moth', '나방')], 5)
# 25 종합 영작 오류 (4)
T1.flex('다음 중 어법상 옳은 문장은?', '7·8과 종합', '',
 ['I saw Robin Hood waving at me.', 'Living in a tulou keep people safe.', 'It is too dangerous for you stand there.', 'If I were you, I will say the words.', 'No one cannot say that we don\'t need graphs.'],
 "이유 ▶ 지각동사 see + 목적어 + -ing ✔\n오답 ▶ {1} 동명사 주어 단수 → keeps {2} for you to stand {3} will → would {4} No one can (이중 부정 X)",
 [('wave', '손을 흔들다')], 4)

# ══════════════════════════ 2회 ══════════════════════════
T2 = Test('2', '2회', '7·8과 최종 점검 2회', '중산중 최종 점검', N, H=H)
T2.rot0 = 3
T2.flex('다음 대화의 내용과 일치하지 <u>않는</u> 것은?', '7과 대화', Bx(
 "A: What would you do if you became a millionaire, Juwon?", "B: I would build my own house.", "A: What kind of house would you build?",
 "B: I would build a house that is completely covered with mirrors.", "A: Why?", "B: The mirrors would make the house almost invisible. Wouldn't that be cool?", "A: That would be cool!"),
 ['Juwon is already a millionaire and lives in a mirror house.', 'Juwon would build his own house if he were rich.', 'Juwon\'s dream house would be covered with mirrors.', 'Juwon thinks the mirrors would make the house hard to see.', 'A agrees that the house would be cool.'],
 "이유 ▶ What would you do if you became a millionaire? → 백만장자가 된다면(가정) → 이미 부자이고 거울 집에 산다는 건 함정\n오답 ▶ {1} I would build my own house {2} completely covered with mirrors {3} almost invisible {4} That would be cool!",
 [('millionaire', '백만장자'), ('invisible', '보이지 않는')], 3)
T2.flex('다음 대화의 빈칸에 들어갈 말로 가장 알맞은 것은?', '7과 대화', Bx(
 "A: I think living in a jungle would be really exciting. Don't you think so?", "B: But there are some dangerous animals in the jungle, Jinho.", "A: I know. But the jungle is full of adventure. I wish I could live there.",
 "B: ______________________", "A: I would explore it. Maybe I could make some animal friends."),
 ['What would you do if you lived in the jungle?', 'Why did you go to the jungle?', 'When did you live in the jungle?', 'How long have you lived in the jungle?', 'Who lives in the jungle with you?'],
 "이유 ▶ 대답이 I would explore it.(가정법) → '정글에 산다면 무엇을 하겠니?'\n오답 ▶ {1}{2}{3} 실제로 갔거나 살았다는 전제(진호는 살아 본 적 없음) {4} 함께 사는 사람",
 [('explore', '탐험하다'), ('adventure', '모험')], 3)
T2.flex('다음 대화를 읽고 답할 수 <u>없는</u> 질문은?', '7과 대화', Bx(
 "A: Dohun, we need to start our project on our dream country to visit.", "B: That's right. Which country do you want to visit, Emma?", "A: In my case, I want to visit Spain.", "B: What would you do if you visited Spain?",
 "A: I'm interested in buildings. So I would go see La Sagrada Familia.", "B: Isn't that the church Antoni Gaudí designed?", "A: Yes, it is. It would be interesting to see how his design was inspired by nature.",
 "B: Hmm... How about Gaudí and Spain as the title for our project?", "A: I love it!"),
 ['When will Emma and Dohun visit Spain?', 'Which country does Emma want to visit?', 'What is Emma interested in?', 'Who designed La Sagrada Familia?', 'What title did Dohun suggest for the project?'],
 "이유 ▶ 스페인에 언제 가는지는 나오지 않음(프로젝트 주제일 뿐)\n오답 ▶ {1} Spain {2} buildings {3} Antoni Gaudí {4} Gaudí and Spain",
 [('design', '설계하다'), ('be inspired by', '~에서 영감을 받다')], 3)
T2.flex('다음 발표의 내용과 일치하는 것은?', '8과 대화', Bx(
 "I did a survey on the books we want for our school library. The result says that thirteen out of twenty students chose novels. That is sixty-five percent of the total. "
 "Five out of twenty students chose science-fiction books. However, only two out of twenty students chose history books. From this survey result, I think the school library should get more novels. Do you see what I mean?"),
 ['Ten percent of the students chose history books.', 'Thirteen percent of the students chose novels.', 'More students chose history books than science-fiction books.', 'Twenty-five students took part in the survey.', 'The speaker thinks the library should get more history books.'],
 "이유 ▶ 20명 중 2명 = 10% ✔\n오답 ▶ {1} 13명 = 65% {2} 공상 과학 5명 > 역사 2명 {3} 20명 {4} 소설을 더 들여놓자",
 [('novel', '소설'), ('total', '전체')], 3)
T2.flex('다음 문장을 가정법 과거로 바르게 바꾼 것은?', '7과 문법', Bx('As I don\'t live in Alaska, I can\'t go sledding all day.'),
 ['If I lived in Alaska, I could go sledding all day.', 'If I live in Alaska, I could go sledding all day.', 'If I lived in Alaska, I can go sledding all day.', 'If I didn\'t live in Alaska, I could go sledding all day.', 'If I lived in Alaska, I couldn\'t go sledding all day.'],
 "이유 ▶ 현재 사실의 반대 → If + 과거(lived), could + 동사원형, 긍정·부정도 반대로 ✔\n오답 ▶ {1} live → lived {2} can → could {3}{4} 긍정·부정을 그대로 둠",
 [('sled', '썰매를 타다')], 4)
T2.flex('다음 중 어법상 <u>어색한</u> 문장은?', '7과 문법', '',
 ['The old Venetians wanted to keep themselves safely from invaders.', 'The mirrors would make the house almost invisible.', 'Living together keeps them safe.', 'A graph might make this easier to understand.', 'The thick walls would keep me warm in winter.'],
 "이유 ▶ keep + 목적어 + 형용사 → safely(부사) ❌ safe ✔ (본문: to keep themselves safe from invaders)\n오답 ▶ {1} make + 목적어 + invisible {2} keeps them safe {3} make + this + easier {4} keep me warm",
 [('invader', '침략자')], 3)
T2.flex('다음 두 문장을 한 문장으로 바르게 바꾼 것은?', '8과 문법', Bx('• It\'s very dangerous.', '• You can\'t stand there.'),
 ['It\'s too dangerous for you to stand there.', 'It\'s too dangerous for you stand there.', 'It\'s too dangerous of you to stand there.', 'It\'s so dangerous that you can stand there.', 'It\'s dangerous enough for you to stand there.'],
 "이유 ▶ too ~ for 의미상 주어 to부정사 (너무 ~해서 …할 수 없다) ✔ 본문 Robin Hood의 말\n오답 ▶ {1} to 빠짐 {2} of X(dangerous는 for) {3}{4} 뜻이 반대",
 [('dangerous', '위험한')], 4)
T2.flex('다음 우리말을 영작한 것으로 가장 알맞은 것은?', '8과 문법 영작', Bx('이제 아무도 우리가 그래프가 필요 없다고 말할 수 없어.'),
 ['No one can say that we don\'t need them anymore.', 'Not everyone can say that we don\'t need them anymore.', 'No one can\'t say that we don\'t need them anymore.', 'Everyone can say that we don\'t need them anymore.', 'Anyone can say that we need them anymore.'],
 "이유 ▶ 아무도 ~할 수 없다 → No one can ~ (전체 부정, 조동사는 긍정) ✔ 본문 마지막 Pascal의 말\n오답 ▶ {1} 부분 부정(모두가 ~한 것은 아니다) {2} 이중 부정 {3}{4} 뜻 반대",
 [('anymore', '더 이상')], 5)
T2.flex('다음 글을 읽고 답할 수 <u>없는</u> 질문은?', '7과 본문 ❷', Bx(
 "If I lived in Venice, I would take a gondola to school every morning. Venice has 118 small islands. On weekends, I would travel from island to island by a vaporetto, a water bus. "
 "At high tide, the water from the Adriatic Sea often rises and leaves the streets full of water. However, I would be able to walk around the town through the raised walkways. Venice is known as the \"floating city.\""),
 ['How much does it cost to ride a vaporetto?', 'How many islands does Venice have?', 'What is a vaporetto?', 'What happens at high tide?', 'What is Venice known as?'],
 "이유 ▶ 바포레토 요금은 나오지 않음\n오답 ▶ {1} 118 {2} a water bus {3} 바닷물이 올라와 거리가 물에 잠김 {4} the \"floating city\"",
 [('high tide', '만조'), ('walkway', '보도, 통로')], 4)
T2.fixed('글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳은?', '7과 본문 ❸', Bx(
 "<b>Do you wonder where I would sleep?</b>", "",
 "In a tulou, there are usually three to five floors. ( ① ) The first floor is used for cooking and eating. ( ② ) And people store food and tools on the second floor. ( ③ ) "
 "My bedroom would be on the third or fourth floor. ( ④ ) A tulou is like a village. ( ⑤ ) The people living in a tulou mostly have the same family name."),
 None, 3,
 "이유 ▶ 1층 요리·식사, 2층 보관 → 내가 어디서 잘지 궁금하니? → 내 침실은 3층이나 4층\n오답 ▶ ④⑤ 답(침실 위치)이 질문보다 먼저 나오게 됨 / ①② 층별 설명 중간",
 [('store', '보관하다'), ('floor', '층')], 3)
T2.flex('다음 우리말을 영작할 때 <u>다섯 번째</u>로 오는 단어는?', '7과 본문 ❸ 영작', Bx('나는 가끔 이웃이 차를 마시러 오라고 나를 부르는 것을 들을 것이다.', '→ I would sometimes hear ( me / my / calling / neighbor ) to come over for tea.'),
 ['my', 'neighbor', 'calling', 'me', 'hear'],
 "(아래에서 덮어씀)",
 [('come over', '들르다'), ('neighbor', '이웃')], 4)
T2.flex('다음 우리말을 바르게 영작한 것은?', '7과 본문 ❷ 영작', Bx('그러나 그들이 이 늪 같은 표면 위에 집을 짓는 것은 쉽지 않았다.'),
 ['But it was not easy for them to build their homes on this swampy surface.', 'But it was not easy of them to build their homes on this swampy surface.', 'But it was not easy for them building their homes on this swampy surface.', 'But that was not easy for them to build their homes on this swampy surface.', 'But it was easy for them not to build their homes on this swampy surface.'],
 "이유 ▶ It(가주어) + was + 형용사 + for 의미상 주어 + to부정사(진주어) ✔\n오답 ▶ {1} easy는 for {2} 진주어는 to build {3} 가주어는 it {4} 뜻이 달라짐",
 [('swampy', '늪 같은'), ('surface', '표면')], 4)
T2.fixed('글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳은?', '8과 본문 ❷', Bx(
 "<b>The man pulled Pascal onto his horse and rode into the woods.</b>", "",
 "Suddenly, he heard men shouting. ( ① ) When he opened his eyes, he saw soldiers on horses. ( ② ) They were chasing a man with arrows in his hand. ( ③ ) The man saw Pascal and shouted. "
 "\"It's too dangerous for you to stand there. Come on.\" ( ④ ) When they arrived at a house, the man stopped and got off his horse. ( ⑤ )"),
 None, 4,
 "이유 ▶ \"거기 서 있기엔 너무 위험해. 어서!\" → 남자가 Pascal을 말에 끌어올려 숲으로 → 집에 도착해 말에서 내림\n오답 ▶ ③ 아직 남자가 Pascal을 보지도 않음 / ⑤ 말에서 내린 뒤에 말에 태울 수 없음",
 [('pull', '끌어당기다'), ('woods', '숲')], 3)
T2.fixed('다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 옳지 <u>않은</u> 것은?', '8과 본문 ❶', Bx(
 "Pascal was ⓐ <u>doing</u> his math homework in his room. He was struggling with graphs. \"It's too hard ⓑ <u>to read</u> and draw graphs. Why do I need these anyway? No one ⓒ <u>need</u> graphs in real life.\" "
 "He put down his pen and picked up his favorite book, <i>Robin Hood</i>. He decided ⓓ <u>to read</u> himself to sleep. When he was about to open the book, he heard a voice. He looked up from the book to see ⓔ <u>who</u> was talking."),
 ['ⓐ', 'ⓑ', 'ⓒ', 'ⓓ', 'ⓔ'], 3,
 "이유 ▶ No one은 단수 취급 → needs ✔ need ❌\n오답 ▶ ⓐ 과거진행 was doing ⓑ too ~ to ⓓ decide + to부정사 ⓔ 간접의문문 who(주어 역할)",
 [('struggle with', '~으로 애쓰다, 고생하다')], 4)
T2.flex('다음 글을 읽고 알 수 있는 것으로 가장 적절한 것은?', '8과 본문 ❹', Bx(
 "\"There are five soldiers from midnight to six in the morning. Next, there are three soldiers until noon, and then there are eight soldiers until six in the evening. Lastly, there are twelve soldiers until midnight.\"",
 "\"Look, the most dangerous time is between six in the evening and midnight. Four times more soldiers work at that time than from six in the morning until noon. Do you see what I mean?\"", "\"Aha! I get it now. Thank you so much, Pascal!\""),
 ['From noon to six in the evening, there are five more soldiers than from six in the morning until noon.', 'The number of soldiers is the same all day.', 'There are fewer soldiers at night than in the morning.', 'Twelve soldiers work from midnight to six in the morning.', 'Robin did not understand the graph.'],
 "이유 ▶ 정오~저녁 6시 8명 − 오전 6시~정오 3명 = 5명 더 많음 ✔\n오답 ▶ {1} 시간대마다 다름 {2} 밤(12명) > 아침(3명) {3} 자정~오전 6시는 5명 {4} Aha! I get it now.",
 [('lastly', '마지막으로')], 5)
T2.flex('다음 우리말을 영작할 때 빈칸에 들어갈 말로 알맞은 것은?', '8과 본문 영작', Bx('그는 누가 말하고 있는지 보려고 책에서 고개를 들었다.', '→ He looked up from the book ____________ was talking.'),
 ['to see who', 'seeing who', 'to see who he', 'to saw who', 'see who'],
 "이유 ▶ 목적의 to부정사(보려고) + 간접의문문 who was talking(의문사가 주어) ✔\n오답 ▶ {1} seeing(분사) {2} who가 주어라 he 불필요 {3} to + 동사원형 {4} to 빠짐",
 [('look up', '올려다보다')], 4)
T2.flex('[17~20] 다음 글을 읽고 물음에 답하시오.<br>17. 윗글을 읽고 답할 수 <u>없는</u> 질문은?', '외부지문 · Reading File', JH,
 ['How big is a typical traditional Japanese house?', 'Where do people take off their shoes?', 'What are tatami mats made from?', 'Why is the floor raised off the ground?', 'What are the roofs covered with?'],
 "이유 ▶ 집의 크기는 나오지 않음\n오답 ▶ {1} genkan(현관) {2} woven grass {3} 홍수로부터 건조하고 안전하게 {4} kawara tiles",
 [('typical', '전형적인')], 5)
T2.fixed('18. 윗글의 밑줄 친 ⓐ~ⓔ 중 어법상 옳지 <u>않은</u> 것은?', '외부지문 · Reading File', Bx(
 "In the house, many Japanese do not use chairs. Instead, they sit ⓐ <u>directly</u> on tatami mats that ⓑ <u>are made</u> from woven grass. When the weather gets cold, people prefer ⓒ <u>to sit</u> at a kotatsu, a heated table. "
 "ⓓ <u>Keeping</u> their body warm, Japanese have meals at the table. The house also has sloped roofs because they keep rainwater ⓔ <u>to flow</u> off easily."),
 ['ⓐ', 'ⓑ', 'ⓒ', 'ⓓ', 'ⓔ'], 5,
 "이유 ▶ keep + 목적어 + -ing(계속 ~하게 하다) → keep rainwater flowing ✔ to flow ❌\n오답 ▶ ⓐ 동사 sit 수식 부사 ⓑ 매트가 '만들어지는' 수동 ⓒ prefer + to부정사 ⓓ 분사구문(몸을 따뜻하게 하면서)",
 [('sloped', '경사진'), ('flow off', '흘러내리다')], 5)
T2.flex('19. 위 글(17번)에서 여름의 많은 비와 홍수에 대비하는 방법으로 언급되지 <u>않은</u> 것은?', '외부지문 · Reading File', '',
 ['putting their legs in a kotatsu', 'raising the floor a little off the ground', 'making sloped roofs', 'covering the roofs with water-resistant tiles', 'letting rainwater flow off the roofs easily'],
 "이유 ▶ 본문의 비·홍수 대비: 바닥 높이기, 경사 지붕(빗물이 잘 흘러내림), 방수 기와 → kotatsu는 '추위'를 위한 것(비·홍수와 무관) — 함정\n오답 ▶ {1} raised a little off the ground {2} sloped roofs {3} water-resistant kawara {4} keep rainwater flowing off easily",
 [('water-resistant', '방수의')], 5)
T2.flex('20. 윗글의 내용과 일치하도록 다음 우리말을 영작할 때 가장 알맞은 것은?', '외부지문 · Reading File 영작', Bx('당신이 그곳에 산다면, 집에 들어가기 전에 신발을 벗어야 할 것이다.'),
 ['If you lived there, you would have to take off your shoes before entering the house.', 'If you live there, you would have to take off your shoes before entering the house.', 'If you lived there, you will have to take off your shoes before entering the house.', 'If you lived there, you would have to take off your shoes before enter the house.', 'If you lived there, you would have to take on your shoes after entering the house.'],
 "이유 ▶ 가정법 과거 If + lived, would have to + 동사원형 / 전치사 before + 동명사 entering ✔\n오답 ▶ {1} live → lived {2} will → would {3} before enter X {4} take on(신다)·after(뒤에) 뜻이 다름",
 [('take off', '벗다'), ('entrance hall', '현관')], 5)
T2.flex('[21~24] 외부지문 Picture Bride<br>' + PBN + '<br>21. 시의 내용과 일치하지 <u>않는</u> 것은?', '외부지문 · Picture Bride', '',
 ['The grandmother knew Hawaii well before she left Korea.', 'The grandmother walked past tailor shops on her way to the port.', 'The man waited for her on an island in Hawaii.', 'The man was holding her picture up to the light.', 'The husband was a stranger to her when they first met.'],
 "이유 ▶ 배는 할머니를 '거의 알지 못하는' 섬으로 데려감 → 잘 알았다는 건 함정\n오답 ▶ {1} 부산의 양복점을 지나 항구로 {2} 하와이의 섬에서 기다림 {3} 사진을 빛에 비춰 봄 {4} 처음 만난 낯선 사람",
 [('stranger', '낯선 사람')], 3)
T2.flex('22. 시에서 사탕수수 밭의 뜨겁고 건조한 바람이 할머니의 치마를 부풀리는 마지막 장면이 암시하는 것으로 가장 알맞은 것은?', '외부지문 · Picture Bride', '',
 ['the hard and unfamiliar new life waiting for her in Hawaii', 'a cool and relaxing vacation by the sea', 'her happy memories of her father\'s home', 'the end of the sugarcane harvest season', 'her plan to return to Korea soon'],
 "이유 ▶ 불타는 사탕수수 밭의 뜨겁고 건조한 바람 → 낯선 땅에서 고된 노동과 힘든 삶이 기다리고 있음을 암시\n오답 ▶ {1} 시원한 휴가(반대) {2} 고향의 행복한 기억 X {3} 수확 끝 X {4} 귀국 계획 X",
 [('unfamiliar', '낯선'), ('harvest', '수확')], 5)
T2.fixed('23. 프린트 Activity처럼 시의 내용에 대한 O/X를 바르게 짝지은 것은?', '외부지문 · Picture Bride', Bx(
 '(a) 할머니는 남편을 사진으로만 알고 하와이로 떠났다.', '(b) 화자는 할머니가 짐을 무엇을 챙겼는지 정확히 알고 있다.', '(c) 남자는 설탕 공장 근처 노동자 숙소에 살았다.', '(d) 남편은 할머니보다 열세 살 많았다.'),
 ['O − X − O − O', 'O − O − O − O', 'X − X − O − O', 'O − X − X − O', 'O − X − O − X'], 1,
 "이유 ▶ (a) 사진신부 → O (b) 무엇을 챙겼는지 알 수 없다고 함 → X (c) 와이알루아 설탕 공장 근처 노동자 숙소 → O (d) 13살 연상 → O",
 [('picture bride', '사진신부')], 4)
T2.flex('24. 시의 화자에 대한 설명으로 가장 알맞은 것은?', '외부지문 · Picture Bride', '',
 ['She is a granddaughter imagining her grandmother\'s journey at a similar age.', 'She is the picture bride herself telling her own story.', 'She is the man waiting in Hawaii.', 'She is a tailor working in Pusan.', 'She is a worker at the Waialua Sugar Mill.'],
 "이유 ▶ 화자는 손녀(granddaughter)로, 할머니가 떠날 때(23세)와 비슷한 나이(24세)에 할머니의 여정을 상상함 — '할머니 자신'이 말하는 시라고 착각하기 쉬움(함정)\n오답 ▶ {1} 사진신부는 할머니 {2} 기다린 남자 X {3} 양복점은 지나간 곳 {4} 설탕 공장은 남자 쪽",
 [('granddaughter', '손녀'), ('journey', '여정')], 5)
T2.flex('다음 중 어법상 옳은 문장의 개수는?', '7·8과 종합', Bx(
 '(a) If I were a bird, I would fly to my grandmother.', '(b) The mirrors would make the house almost invisibly.', '(c) This coffee is too hot for me to drink.', '(d) Pascal saw Robin Hood to wave at him.', '(e) No one needs graphs in real life.'),
 ['3개', '1개', '2개', '4개', '5개'],
 "이유 ▶ 옳은 것: (a) 가정법 과거(be동사는 were) (c) too ~ for 의미상 주어 to (e) No one + 단수 동사 → 3개\n틀린 것: (b) invisibly → invisible (d) to wave → wave/waving",
 [('invisible', '보이지 않는')], 4)

# 11·12번(2회) 배열 문항 해설 다듬기: 해설에 혼란스러운 문구가 없도록 덮어씀
T1.items[10]['ex'] = "완성 문장 ▶ Living(1) / together(2) / in(3) / one(4) / building(5) / keeps(6) / them(7) / safe(8)\n이유 ▶ 동명사구 주어 Living together in one building(단수) + keeps + them + safe → 네 번째 단어는 one\n오답 ▶ {1} 3번째 {2} 2번째 {3} 6번째 {4} 5번째"
T2.items[10]['ex'] = "완성 문장 ▶ I(1) / would(2) / sometimes(3) / hear(4) / my(5) / neighbor(6) / calling(7) / me(8) / to come over for tea\n이유 ▶ 지각동사 hear + 목적어(my neighbor) + -ing(calling) → 다섯 번째 단어는 my\n오답 ▶ {1} 6번째 {2} 7번째 {3} 8번째 {4} 4번째"
for T in (T1, T2):
    assert len(T.items) == 25, len(T.items)
    for it, p in zip(T.items, K25):
        assert it['pts'] == p, (T.tid, it['stem'][:30], it['pts'], p)
        if it['opts']: assert len(set(map(str, it['opts']))) == 5, it['stem']
    T.render()
