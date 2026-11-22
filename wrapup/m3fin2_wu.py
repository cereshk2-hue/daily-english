# 11/22 중산중3 7·8과 최종 점검 3·4회 (심화) — 선생님: 1·2회가 기출보다 직관적 → 난이도 올림
# 같은 틀(대화 4 · 문법 4 · 본문 8 · 일본 가옥 4 · Picture Bride 4 · 종합 1, 기출 배점 순서, 45분)
# 어렵게: 긴 바꿔 말하기 선택지 · 모두 고르기 · 개수 · (A)(B)(C) 어법 · 문맥 어휘 · 형태 변화 영작 · 계산/학생 판단
# Picture Bride는 시 원문 없이(4단어 이상 겹침 검사)
import sys
sys.path.insert(0, '/home/claude/srcrepo/wrapup')
from wu_k25v import *
H = ('최종 점검', '중산중 7·8과 최종 점검', '중산중 7·8과 최종 점검', 'm3fin')
Bx = lambda *ls: BOX('<br>'.join(ls))
N = '최종 점검 심화편이에요. 1·2회보다 선택지가 길고, 모두 고르기·개수·형태 바꿔 영작하기처럼 끝까지 따져야 하는 문제가 많아요. 45분 안에 풀고 OMR에 답을 입력하세요.'
K25 = [3, 3, 3, 3, 4, 3, 4, 5, 4, 3, 4, 4, 3, 4, 5, 4, 5, 5, 5, 5, 3, 5, 4, 5, 4]
CNT = ['1개', '2개', '3개', '4개', '5개']
JH = Bx("What would it be like to live in a traditional Japanese house? If you lived there, you would have to take off your shoes in the <i>genkan</i>, an entrance hall, before entering the house. "
        "In the house, many Japanese do not use chairs. Instead, they sit directly on <i>tatami</i> mats that are made from woven grass. "
        "Rooms are divided by <i>shoji</i>, portable sliding doors that are made from wood and thin paper. For large gatherings, these doors can be removed to create one large room. "
        "When the weather gets cold, people prefer to sit at a <i>kotatsu</i>, a heated table, and put their legs in it. Keeping their body warm, Japanese have meals, drink tea, or read books at the table. "
        "In summer, heavy rain can cause flooding. The floor of the house is raised a little off the ground to keep the living area dry and safe from flooding. "
        "The house also has sloped roofs because they keep rainwater flowing off easily. The roofs are covered with <i>kawara</i> tiles. The strong <i>kawara</i> tiles are not only water-resistant but also fireproof.")
PBN = '※ Picture Bride(Cathy Song)는 학교 프린트의 시와 해석을 떠올리며 푸세요.'
VEN2 = ("In Venice, there are many colorful houses on the water. You may wonder how and why they built the houses on the water. The old Venetians decided to live there to keep themselves safe from invaders. "
        "But it was not easy for them to build their homes on this swampy surface. So they installed more than 10 million wooden poles in the ground. It is these wooden poles that support Venice to this day.")
GR = ("\"There are five soldiers from midnight to six in the morning. Next, there are three soldiers until noon, and then there are eight soldiers until six in the evening. Lastly, there are twelve soldiers until midnight. "
      "So, you should go inside between six in the morning and noon.\"")

# ══════════════════════════ 3회 ══════════════════════════
T3 = Test('3', '3회', '7·8과 최종 점검 3회 (심화)', '중산중 최종 점검', N, H=H)
T3.rot0 = 1
# 1 (3)
T3.flex('다음 대화를 읽고 추론한 내용으로 가장 적절한 것은?', '7과 대화', Bx(
 "A: Have you heard from Julia? She's traveling in Türkiye, right?", "B: Yes, she sent me some pictures. Do you want to see them?", "A: Yes, please.", "B: Okay, take a look.",
 "A: Oh, look at those cave houses! They look so unique, don't they? I wish I could try living there.", "B: I like those balloons. They look so beautiful!",
 "A: I think Türkiye is a wonderful place to visit. I hope to visit there some day.", "B: Me too!"),
 ['The speaker who wants to try living in a cave house has never actually lived in one.',
  'Julia took pictures of the balloons because B had asked her to.',
  'A and B have already decided when they will visit Türkiye together.',
  'A is more interested in the balloons than in the cave houses.',
  'Julia sent the pictures directly to A while she was traveling.'],
 "이유 ▶ I wish I could try living there. = 가정법 과거(지금은 그럴 수 없음) → 동굴 집에 살아 본 적이 없다고 추론 ✔\n오답 ▶ {1} 부탁했다는 말 없음 {2} some day(언젠가) — 날짜를 정하지 않음 {3} 동굴 집에 관심 있는 건 A, 풍선은 B {4} 사진을 받은 건 B",
 [('cave', '동굴'), ('directly', '직접')], 3)
# 2 (3)
T3.flex('주어진 말에 이어질 대화의 순서로 가장 적절한 것은?', '7과 대화', Bx(
 "A: What would you do if you became a millionaire, Juwon?", "", "(A) A: Why?", "(B) B: I would build a house that is completely covered with mirrors.", "(C) B: I would build my own house.", "(D) A: What kind of house would you build?", "",
 "B: The mirrors would make the house almost invisible. Wouldn't that be cool?"),
 ['(C) − (D) − (B) − (A)', '(C) − (B) − (D) − (A)', '(D) − (C) − (B) − (A)', '(C) − (A) − (D) − (B)', '(B) − (D) − (C) − (A)'],
 "이유 ▶ 백만장자가 되면? → (C) 내 집을 짓겠다 → (D) 어떤 집? → (B) 거울로 덮인 집 → (A) 왜? → 거울이 집을 거의 안 보이게 해 줄 테니까\n포인트 ▶ 대답 순서: '무엇을'(집 짓기) → '어떤'(거울 집) → '왜'(안 보이게)",
 [('millionaire', '백만장자'), ('invisible', '보이지 않는')], 3)
# 3 (3) 흐름상 어색한 것
T3.fixed('다음 대화의 밑줄 친 ①~⑤ 중 흐름상 <u>어색한</u> 것은?', '8과 대화', Bx(
 "Mina: Henry, what are you doing?", "Henry: ① <u>I'm writing an article about students' favorite snacks. I'm worried about their health.</u>", "Mina: Why?",
 "Henry: ② <u>Well, I surveyed 100 students, and eighty percent of them liked pizza and fried chicken for snacks.</u> Do you see what I mean?",
 "Mina: ③ <u>Oh, I get it. Students really prefer healthy snacks to fast food.</u> What else did they like?",
 "Henry: ④ <u>Twelve percent of the students chose chocolate cake as their favorite.</u>", "Mina: ⑤ <u>Wow, students should really try to eat healthier snacks!</u>"),
 None, 3,
 "이유 ▶ 80%가 피자·치킨(패스트푸드)을 골랐다 → '건강한 간식을 더 좋아한다'는 반대 → Students really like fast food.가 자연스러움\n오답 ▶ ① 건강이 걱정돼 기사를 씀 ② 조사 결과 ④ What else에 대한 대답 ⑤ 결론(더 건강한 간식을 먹어야)",
 [('prefer A to B', 'B보다 A를 더 좋아하다'), ('survey', '조사하다')], 3)
# 4 (3) 표 계산
T3.flex('다음 발표 내용을 표로 정리할 때 <u>잘못된</u> 것은?', '8과 대화', Bx(
 "I did a survey on the books we want for our school library. The result says that thirteen out of twenty students chose novels. That is sixty-five percent of the total. "
 "Five out of twenty students chose science-fiction books. However, only two out of twenty students chose history books. From this survey result, I think the school library should get more novels. Do you see what I mean?"),
 ['Science-fiction books − 5 students − 20%', 'Novels − 13 students − 65%', 'History books − 2 students − 10%', 'All the books − 20 students − 100%', "The speaker's idea − getting more novels"],
 "이유 ▶ 20명 중 5명 = 25% (20%가 아님) → 잘못됨\n오답 ▶ {1} 13/20 = 65% {2} 2/20 = 10% {3} 13 + 5 + 2 = 20명 {4} the school library should get more novels",
 [('novel', '소설'), ('total', '전체')], 3)
# 5 (4) 가정법 모두 고르기
T3.flex('다음 중 어법상 옳은 문장을 <u>모두</u> 고른 것은?', '7과 문법', Bx(
 '(a) If I lived in a tulou, I would always have friends at home to play with.', '(b) If unwelcome visitors appear, I would pull the ladder up.', '(c) If I were in Venice, I could travel from island to island.',
 '(d) If I had a new sled, I will go sledding all day.', '(e) If she knew Hawaii well, she wouldn\'t feel so nervous.'),
 ['(a), (c), (e)', '(a), (b), (c)', '(b), (d)', '(a), (c)', '(c), (d), (e)'],
 "이유 ▶ 가정법 과거: If + 주어 + 과거형(be는 were), 주어 + would/could + 동사원형 → (a)(c)(e) ✔\n틀린 것 ▶ (b) appear → appeared (d) will → would\n주의 ▶ {3}(a),(c)만 고르면 (e)를 빠뜨린 것",
 [('unwelcome', '반갑지 않은'), ('nervous', '긴장한')], 4)
# 6 (3) (A)(B)(C)
T3.flex('(A), (B), (C)의 각 네모 안에서 어법에 맞는 표현으로 가장 적절한 것은?', '7과 문법', Bx(
 '• The thick walls would keep me (A) [ cool / coolly ] in summer and warm in winter.', '• Living together in one building (B) [ keep / keeps ] them safe.', '• The mirrors would make the house almost (C) [ invisible / invisibly ].'),
 ['cool − keeps − invisible', 'coolly − keeps − invisible', 'cool − keep − invisible', 'cool − keeps − invisibly', 'coolly − keep − invisibly'],
 "이유 ▶ (A) keep + 목적어 + 형용사 → cool (B) 동명사구 주어 Living ~ building은 단수 → keeps (C) make + 목적어 + 형용사 → invisible\n함정 ▶ (B) 바로 앞 building에 끌려 keep을 고르기 쉬움",
 [('thick', '두꺼운'), ('invisible', '보이지 않는')], 3)
# 7 (4) 의미 같지 않은 것
T3.flex('다음 중 두 문장의 의미가 서로 같지 <u>않은</u> 것은?', '8과 문법', '',
 ['The question was too difficult for me to answer.<br>= The question is so difficult that I can\'t answer it.',
  'He is too greedy to share with the people.<br>= He is so greedy that he can\'t share with the people.',
  'It\'s too dangerous for you to stand there.<br>= It\'s so dangerous that you can\'t stand there.',
  'She was too tired to walk any farther.<br>= She was so tired that she couldn\'t walk any farther.',
  'The box is too heavy for me to lift.<br>= The box is so heavy that I can\'t lift it.'],
 "이유 ▶ 앞 문장은 과거(was) → so ~ that 문장도 과거로: The question was so difficult that I couldn't answer it. 시제가 달라 의미가 같지 않음\n오답 ▶ {1}{2}{3}{4} too ~ (for 사람) to … = so ~ that 사람 can't(couldn't) … — 시제·의미 모두 일치\n포인트 ▶ that절에서는 목적어(it)를 꼭 써야 함",
 [('greedy', '욕심 많은'), ('farther', '더 멀리')], 4)
# 8 (5) 부분 부정 모두 고르기
T3.flex('다음 우리말과 의미가 같은 문장을 <u>모두</u> 고른 것은?', '8과 문법', Bx('모든 학생이 그래프를 좋아하는 것은 아니다.', '',
 '(a) Not every student likes graphs.', '(b) No student likes graphs.', '(c) Not all students like graphs.', '(d) Nobody likes graphs.', '(e) None of the students like graphs.'),
 ['(a), (c)', '(a), (b)', '(b), (d), (e)', '(a), (c), (e)', '(c), (d)'],
 "이유 ▶ '모두 ~인 것은 아니다' = 부분 부정 Not every / Not all → (a)(c)\n틀린 것 ▶ (b) No student (d) Nobody (e) None of = '아무도 ~않다'(전체 부정)\n포인트 ▶ Not every + 단수 명사 + 단수 동사(likes) / Not all + 복수 명사 + 복수 동사(like)",
 [('graph', '그래프')], 5)
# 9 (4) Venice 긴 내용 일치
T3.flex('다음 글의 내용과 일치하는 것은?', '7과 본문 ❷', Bx(
 "If I lived in Venice, I would take a gondola to school every morning. Venice has 118 small islands. On weekends, I would travel from island to island by a vaporetto, a water bus. "
 "At high tide, the water from the Adriatic Sea often rises and leaves the streets full of water. However, I would be able to walk around the town through the raised walkways. Venice is known as the \"floating city.\" " + VEN2),
 ['The early Venetians chose to live on the water mainly for safety, even though building there was hard.',
  'Venice is made up of over one hundred islands that are connected by wooden poles.',
  'At high tide, people cannot walk anywhere in the town, so they must take gondolas.',
  'The writer actually lives in Venice and takes a gondola to school every morning.',
  'About one million wooden poles were put into the ground to hold up the city.'],
 "이유 ▶ to keep themselves safe from invaders(안전) + it was not easy to build(어려움) ✔\n오답 ▶ {1} 나무 기둥은 섬을 '연결'하는 게 아니라 도시를 '받침'(support) {2} raised walkways로 걸어 다닐 수 있음 {3} If I lived ~ = 가정(실제로 살지 않음) {4} 천만(10 million) 개 이상",
 [('high tide', '만조'), ('swampy', '늪 같은')], 4)
# 10 (3) Venice 삽입 However
T3.fixed('글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳은?', '7과 본문 ❷', Bx(
 "<b>However, I would be able to walk around the town through the raised walkways.</b>", "",
 "If I lived in Venice, I would take a gondola to school every morning. ( ① ) Venice has 118 small islands. ( ② ) On weekends, I would travel from island to island by a vaporetto, a water bus. ( ③ ) "
 "At high tide, the water from the Adriatic Sea often rises and leaves the streets full of water. ( ④ ) Venice is known as the \"floating city.\" ( ⑤ ) In Venice, there are many colorful houses on the water."),
 None, 4,
 "이유 ▶ 만조 때 거리가 물로 가득 찬다 → 그러나(However) 높인 통로로 걸어 다닐 수 있다 — 문제 상황 뒤에 해결\n오답 ▶ ③ 아직 물에 잠기는 문제가 나오지 않아 However가 반대할 내용이 없음 / ⑤ '떠 있는 도시' 소개 뒤라 흐름이 끊김",
 [('raised', '높인'), ('walkway', '통로')], 3)
# 11 (4) 형태 변화 영작
T3.flex('다음 우리말을 &lt;조건&gt;에 맞게 영작할 때, <u>4번째</u>와 <u>15번째</u>로 오는 단어를 바르게 짝지은 것은?', '7과 본문 ❶ 영작', Bx(
 '만약 반갑지 않은 방문객이 나타난다면, 나는 그들이 들어오지 못하게 사다리를 끌어 올릴 것이다.', '',
 '&lt;조건&gt; • If로 시작하는 가정법 과거로 쓸 것  • 15단어로 쓸 것', '• 다음 단어를 모두 쓰되, 필요하면 형태를 바꿀 것: unwelcome, visitor, appear, pull, ladder, up, stop, enter'),
 ['appeared − entering', 'appear − entering', 'appeared − enter', 'appear − to enter', 'appeared − to enter'],
 "완성 ▶ If(1) unwelcome(2) visitors(3) appeared(4), I(5) would(6) pull(7) the(8) ladder(9) up(10) to(11) stop(12) them(13) from(14) entering(15).\n이유 ▶ 가정법 과거 → appeared / stop A from -ing(A가 ~하지 못하게 하다) → entering\n오답 ▶ {1}{3} appear는 현재형 {2}{4} from 뒤에는 동명사",
 [('stop A from -ing', 'A가 ~하지 못하게 하다'), ('unwelcome', '반갑지 않은')], 4)
# 12 (4) 강조 구문 개수
T3.fixed('다음 중 It ~ that 강조 구문이 어법상 바르게 쓰인 문장의 개수는?', '7·8과 본문 강조 구문', Bx(
 '(a) It is these wooden poles that support Venice to this day.', '(b) It was his dog, Manny, who was talking!', '(c) It was the king which took the money from the people.',
 '(d) It is a graph what makes this easier to understand.', '(e) It was in a tulou that I heard my neighbor calling me.'),
 CNT, 3,
 "이유 ▶ 옳은 것 (a) 복수 poles → support (b) 사람 강조는 who도 가능(본문) (e) 장소 부사구 강조 → 3개\n틀린 것 ▶ (c) 사람(the king) → which ❌ who/that (d) what ❌ that",
 [('support', '받치다'), ('emphasize', '강조하다')], 4)
# 13 (3) Pascal 삽입
T3.fixed('글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳은?', '8과 본문 ❶❷', Bx(
 "<b>Pascal closed his eyes and repeated the words.</b>", "",
 "\"Close your eyes and repeat after me. <i>Cogito ergo sum</i>,\" said Manny. ( ① ) \"You can talk?\" ( ② ) \"Just repeat! <i>Cogito ergo sum</i>.\" ( ③ ) Suddenly, he heard men shouting. ( ④ ) "
 "When he opened his eyes, he saw soldiers on horses. ( ⑤ ) They were chasing a man with arrows in his hand."),
 None, 3,
 "이유 ▶ Manny가 '그냥 따라 해!'라고 다시 재촉 → Pascal이 눈을 감고 따라 함 → 갑자기 남자들의 고함 → 눈을 뜨니 군인들\n오답 ▶ ② 따라 했다면 Manny가 다시 Just repeat!이라고 재촉할 필요가 없음 / ④ 눈을 감는 장면이 고함 뒤에 오면 When he opened his eyes와 순서가 어긋남",
 [('repeat', '따라 하다'), ('shout', '소리치다')], 3)
# 14 (4) 어법 모두 고르기
T3.flex('다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 <u>틀린</u> 것을 모두 고른 것은?', '8과 본문 ❹', Bx(
 "Pascal thought for a moment. 'Hmm... A graph might make this ⓐ <u>easier</u> to understand.' Pascal drew a graph and ⓑ <u>showed</u> it to Robin. "
 "\"Look, the most dangerous time is between six in the evening and midnight. Four times ⓒ <u>much</u> soldiers work at that time than from six in the morning until noon. Do you see ⓓ <u>what</u> I mean?\"",
 "\"Aha! I get it now. Thank you so much, Pascal!\"", "\"You're welcome. Now I realize the importance of graphs. No one can say that we don't need ⓔ <u>it</u> anymore.\""),
 ['ⓒ, ⓔ', 'ⓐ, ⓒ', 'ⓑ, ⓓ', 'ⓒ, ⓓ, ⓔ', 'ⓐ, ⓔ'],
 "이유 ▶ ⓒ than과 함께 쓰는 비교급, 셀 수 있는 soldiers → more ⓔ 가리키는 말이 graphs(복수) → them\n바른 것 ▶ ⓐ make + 목적어 + 형용사(비교급) ⓑ drew and showed(과거 병렬) ⓓ 관계대명사 what(~하는 것)",
 [('importance', '중요성'), ('realize', '깨닫다')], 4)
# 15 (5) 학생 판단 계산
T3.flex('다음 글의 내용을 바르게 이해한 학생을 <u>모두</u> 고른 것은?', '8과 본문 ❹', Bx(GR, "\"What? I don't get it.\"", "Pascal thought for a moment. 'Hmm... A graph might make this easier to understand.' Pascal drew a graph and showed it to Robin.", "",
 '지민: 네 시간대의 군인 수를 모두 더하면 28명이야.', '서준: 정오부터 저녁 6시까지는 자정부터 아침 6시까지보다 군인이 3명 많아.', '하은: 군인이 가장 많은 시간대는 가장 적은 시간대의 3배야.',
 '도윤: Robin은 Pascal의 첫 설명을 듣자마자 바로 이해했어.', '유나: Pascal은 숫자를 한눈에 비교하기 쉽게 하려고 그래프를 그렸어.'),
 ['지민, 서준, 유나', '지민, 하은', '서준, 도윤, 유나', '지민, 서준, 하은, 유나', '하은, 도윤'],
 "이유 ▶ 지민 5 + 3 + 8 + 12 = 28 ✔ / 서준 8 − 5 = 3 ✔ / 유나 A graph might make this easier to understand ✔\n틀린 것 ▶ 하은 12 ÷ 3 = 4배(Four times more) / 도윤 처음엔 What? I don't get it.",
 [('midnight', '자정'), ('noon', '정오')], 5)
# 16 (4) 영작 어법
T3.flex('다음 우리말을 영작한 것으로 어법과 의미가 모두 옳은 것은?', '8과 본문 ❸ 영작', Bx('그는 너무 욕심이 많아서 백성들과 나누지 않고, 그래서 백성들은 음식을 살 충분한 돈이 없다.'),
 ['He is too greedy to share with the people, so they don\'t have enough money to buy food.',
  'He is too greedy to share with the people, so they don\'t have money enough buying food.',
  'He is so greedy that he can share with the people, so they don\'t have enough money to buy food.',
  'He is too greedy that he can\'t share with the people, so they don\'t have enough money to buy food.',
  'He is greedy enough to share with the people, so they don\'t have enough money to buy food.'],
 "이유 ▶ too ~ to …(너무 ~해서 …할 수 없다) + enough money to buy(살 충분한 돈) ✔\n오답 ▶ {1} enough는 명사 앞, buying ❌ to buy {2} can → 뜻이 반대 {3} too는 that절과 쓰지 않음(so ~ that) {4} enough to = 충분히 ~해서 …할 수 있다(반대)",
 [('greedy', '욕심 많은'), ('share', '나누다')], 4)
# 17 (5) JH 내용 일치(바꿔 말하기)
T3.flex('[17~20] 다음 글을 읽고 물음에 답하시오.<br>17. 윗글의 내용과 일치하는 것은?', '외부지문 · Reading File', JH,
 ['Because shoji can be taken out, a house can become one big space when many people get together.',
  'People usually put on special indoor shoes in the genkan before entering the house.',
  'Tatami mats are made of wood and thin paper, so they are light enough to carry.',
  'The floor is raised off the ground mainly to keep the house warm in winter.',
  'Kawara tiles are strong against water, but they can easily catch fire.'],
 "이유 ▶ For large gatherings, these doors(shoji) can be removed to create one large room. ✔\n오답 ▶ {1} take off(벗는다) — 실내화 이야기 없음 {2} 나무와 얇은 종이로 만든 건 shoji, tatami는 woven grass(함정) {3} 홍수로부터 건조하고 안전하게(dry and safe from flooding) {4} fireproof(불에 강함)",
 [('get together', '모이다'), ('catch fire', '불이 붙다')], 5)
# 18 (5) JH 문맥 어휘
T3.fixed('18. 다음은 위 글(17번)의 일부이다. 밑줄 친 ⓐ~ⓔ 중 문맥상 낱말의 쓰임이 <u>어색한</u> 것은?', '외부지문 · Reading File', Bx(
 "Rooms are divided by shoji, ⓐ <u>portable</u> sliding doors that are made from wood and thin paper. For large gatherings, these doors can be ⓑ <u>removed</u> to create one large room. "
 "In summer, heavy rain can cause flooding. The floor of the house is ⓒ <u>lowered</u> a little off the ground to keep the living area dry and safe from flooding. "
 "The house also has sloped roofs because they keep rainwater flowing off ⓓ <u>easily</u>. The strong kawara tiles are not only water-resistant but also ⓔ <u>fireproof</u>."),
 ['ⓐ', 'ⓑ', 'ⓒ', 'ⓓ', 'ⓔ'], 3,
 "이유 ▶ 홍수에서 거주 공간을 건조하게 지키려면 바닥을 땅에서 '높여야(raised)' 함 → lowered(낮춰진) ❌\n오답 ▶ ⓐ 옮길 수 있는 ⓑ 떼어 내다 ⓓ 쉽게(흘러내림) ⓔ 불에 강한 → 모두 자연스러움",
 [('lower', '낮추다'), ('portable', '옮길 수 있는')], 5)
# 19 (5) JH 요약(추상 어휘)
T3.flex('19. 위 글(17번)의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 적절한 것은?', '외부지문 · Reading File', Bx(
 "A traditional Japanese house shows how people ____(A)____ their homes to the local weather: it offers ways to stay warm in the cold and to ____(B)____ damage from heavy rain."),
 ['adapt − prevent', 'adapt − cause', 'expose − prevent', 'compare − increase', 'decorate − ignore'],
 "이유 ▶ (A) 추운 날씨엔 kotatsu, 여름 비엔 높인 바닥·경사 지붕·방수 기와 → 집을 날씨에 '맞추다(adapt)' (B) 비 피해를 '막다(prevent)'\n오답 ▶ {1} cause(일으키다) 반대 {2} expose(드러내다) {3} compare(비교하다)·increase(늘리다) {4} decorate(꾸미다)·ignore(무시하다)",
 [('adapt A to B', 'A를 B에 맞추다'), ('prevent', '막다')], 5)
# 20 (5) JH 어법 개수
T3.fixed('20. 위 글(17번)의 내용을 바탕으로 쓴 다음 문장 중 어법상 옳은 것의 개수는?', '외부지문 · Reading File', Bx(
 '(a) If you lived there, you would have to take off your shoes.', '(b) Rooms are divided by shoji, portable sliding doors that is made from wood and thin paper.', '(c) Keeping their body warm, Japanese have meals at the table.',
 '(d) Sloped roofs keep rainwater to flow off easily.', '(e) The floor of the house raises a little off the ground.'),
 CNT, 2,
 "이유 ▶ 옳은 것 (a) 가정법 과거 (c) 분사구문(몸을 따뜻하게 하면서) → 2개\n틀린 것 ▶ (b) 선행사 doors(복수) → are made (d) keep + 목적어 + -ing → flowing (e) 바닥이 '높여지는' → is raised",
 [('sloped', '경사진'), ('raise', '높이다')], 5)
# 21 (3) PB 모두 고르기
T3.flex('[21~24] 외부지문 Picture Bride<br>' + PBN + '<br>21. 시의 내용으로 알 수 있는 사실을 <u>모두</u> 고른 것은?', '외부지문 · Picture Bride', Bx(
 '(a) 할머니가 한국을 떠날 때의 나이는 지금 화자의 나이보다 한 살 적었다.', '(b) 할머니는 인천 항구에서 배를 탔다.', '(c) 남편은 할머니보다 열세 살 많았다.', '(d) 할머니는 하와이에 대해 잘 알고 떠났다.', '(e) 남자는 설탕 공장 근처 노동자 숙소에서 살았다.'),
 ['(a), (c), (e)', '(a), (b), (c)', '(b), (d)', '(a), (c)', '(c), (d), (e)'],
 "이유 ▶ (a) 할머니 23세, 화자 24세 (c) 13살 연상 (e) Waialua 설탕 공장 근처 노동자 숙소 → (a)(c)(e)\n틀린 것 ▶ (b) 부산 (d) 거의 알지 못하는 섬으로 떠남",
 [('port', '항구'), ('workers\' camp', '노동자 숙소')], 3)
# 22 (5) PB 추론
T3.flex('22. 시에서 남자가 할머니의 사진을 빛에 비추어 보는 장면으로 추론할 수 있는 것으로 가장 알맞은 것은?', '외부지문 · Picture Bride', '',
 ['He had only her photograph to learn about the woman he was going to marry.',
  'He was checking whether the photograph had been damaged on the long trip.',
  'He had already met her many times in Korea before she left.',
  'He wanted to send the photograph back to her father in Pusan.',
  'He was taking a picture of her to show the other workers.'],
 "이유 ▶ 사진신부 — 두 사람은 만난 적이 없고 남자는 사진 한 장으로만 신부를 알 수 있었음 → 사진을 빛에 비춰 자세히 들여다봄 ✔\n오답 ▶ {1} 사진 손상 이야기 없음 {2} 처음 만나는 낯선 사람 {3} 사진을 돌려보낸다는 말 없음 {4} 사진을 찍는 장면 아님",
 [('photograph', '사진'), ('damage', '손상시키다')], 5)
# 23 (4) PB 순서
T3.flex('23. 시에 나오는 장면을 순서대로 바르게 나열한 것은?', '외부지문 · Picture Bride', Bx(
 '(A) 낯선 남편과 처음 마주하는 순간', '(B) 화자가 자신의 나이와 할머니가 떠날 때의 나이를 견주어 봄', '(C) 사탕수수 밭의 뜨겁고 건조한 바람이 할머니의 옷자락을 부풀림', '(D) 부산의 양복점들을 지나 항구로 감'),
 ['(B) − (D) − (A) − (C)', '(D) − (B) − (A) − (C)', '(B) − (A) − (D) − (C)', '(B) − (D) − (C) − (A)', '(D) − (A) − (B) − (C)'],
 "이유 ▶ 화자의 나이 비교로 시작(B) → 부산 양복점을 지나 항구로(D) → 하와이에서 낯선 남편과 마주함(A) → 사탕수수 밭의 뜨겁고 건조한 바람(C)으로 끝남",
 [('sugarcane', '사탕수수'), ('tailor shop', '양복점')], 4)
# 24 (5) PB 설명 틀린 것
T3.flex('24. 시에 대한 설명으로 적절하지 <u>않은</u> 것은?', '외부지문 · Picture Bride', '',
 ['화자는 할머니에게 직접 들은 이야기를 그대로 옮겨 전하고 있다.', '화자는 질문을 반복하며 할머니의 마음을 상상한다.', '할머니는 사진 한 장으로 결혼 상대를 정한 사진신부였다.',
  '마지막 장면의 뜨겁고 건조한 바람은 할머니 앞에 놓인 고된 삶을 암시한다.', '화자는 자신과 비슷한 나이에 고향을 떠난 할머니의 처지를 떠올린다.'],
 "이유 ▶ 화자는 할머니의 일을 '알지 못해서' 질문을 던지며 상상함 → 직접 들은 이야기를 그대로 전한다는 건 함정\n오답 ▶ {1} 질문의 반복 = 상상 {2} 사진신부 {3} 불타는 사탕수수 밭의 열풍 = 고된 노동과 낯선 삶 {4} 23세 할머니 ↔ 24세 화자",
 [('imagine', '상상하다')], 5)
# 25 (4) 종합 모두 고르기
T3.flex('다음 중 어법상 옳은 문장을 <u>모두</u> 고른 것은?', '7·8과 종합', Bx(
 '(a) It is too cold for us going out.', '(b) If I were a bird, I could fly to Hawaii.', '(c) I heard my neighbor calling me.', '(d) Living together in one building keep them safe.', '(e) No one knows why he is here.'),
 ['(b), (c), (e)', '(a), (b)', '(c), (d)', '(a), (c), (e)', '(b), (d), (e)'],
 "이유 ▶ (b) 가정법 과거(were, could) (c) 지각동사 hear + 목적어 + -ing (e) No one + 단수 동사, 간접의문문 why + 주어 + 동사 → (b)(c)(e)\n틀린 것 ▶ (a) going → to go (d) 동명사 주어 단수 → keeps",
 [('neighbor', '이웃')], 4)

# ══════════════════════════ 4회 ══════════════════════════
T4 = Test('4', '4회', '7·8과 최종 점검 4회 (심화)', '중산중 최종 점검', N, H=H)
T4.rot0 = 4
# 1 (3)
T4.flex('다음 대화의 내용으로 보아 Taeho에 대한 설명으로 가장 적절한 것은?', '7과 대화', Bx(
 "A: Will it snow today?", "B: I have no idea. Why are you waiting for snow, Taeho?", "A: I got a new sled for my birthday. I can't wait to test it out.",
 "B: Let me check the weather. Umm, there will be no snow for a while.", "A: I wish I lived in Alaska. Then I could go sledding all day!", "B: No kidding! Alaska is a very cold place."),
 ['He is eager to ride his new sled, but the weather will not let him do it soon.',
  'He lives in Alaska, so he can go sledding all day.',
  'He bought a sled because the weather report said it would snow today.',
  'He thinks Alaska is too cold for anyone to live in.',
  'He has already tested his new sled several times this winter.'],
 "이유 ▶ I can't wait to test it out(빨리 타 보고 싶음) + no snow for a while(당분간 눈 없음) ✔\n오답 ▶ {1} I wish I lived in Alaska = 실제로는 알래스카에 살지 않음 {2} 생일 선물로 받음, 눈 예보도 없음 {3} 춥다고 말한 건 B, Taeho는 살고 싶어 함 {4} 아직 test it out 하지 못함",
 [('be eager to', '~하고 싶어 하다'), ('sled', '썰매')], 3)
# 2 (3)
T4.flex('다음 대화의 빈칸 (A), (B)에 들어갈 말로 가장 적절한 것은?', '7과 대화', Bx(
 "Dohun: What would you do if you visited Spain?", "Emma: ________(A)________ So I would go see La Sagrada Familia.", "Dohun: Isn't that the church Antoni Gaudí designed?",
 "Emma: Yes, it is. It would be interesting to see how his design ________(B)________ by nature."),
 ["I'm interested in buildings. − was inspired", "I'm interested in buildings. − inspired", "I'm not interested in art. − was inspired", "I'm interested in sports. − was inspired", "I'm interested in food. − inspired"],
 "이유 ▶ (A) 그래서(So) 성당(건물)을 보러 가겠다 → 건물에 관심이 있다 (B) 설계가 자연에서 영감을 '받은' 것 → 수동태 was inspired\n오답 ▶ {1}{4} inspired(능동) ❌ {2} 관심 없다면 So와 안 맞음 {3} 운동에 관심 있다면 성당을 보러 가는 것과 안 맞음",
 [('be inspired by', '~에서 영감을 받다'), ('design', '설계(하다)')], 3)
# 3 (3)
T4.flex('다음 대화에서 A가 마지막에 "it\'s always better to smile"이라고 말한 근거로 가장 알맞은 것은?', '8과 대화', Bx(
 "A: Jian, what's the matter? You look very upset.", "B: My brother broke my computer. I'm so angry.", "A: I'm sorry to hear that, but your facial muscles must be tired.", "B: What do you mean?",
 "A: Well, it takes a lot of muscles to look angry, but only a few to smile. Do you see what I mean?", "B: Oh, I get it. I guess it's not good to stay angry for a long time.", "A: That's right. Remember, it's always better to smile."),
 ['Looking angry needs many muscles, while smiling needs only a few.', 'Smiling uses more muscles, so it is good exercise for the face.', "Jian's brother promised to fix the computer if Jian smiled.", 'Our facial muscles get stronger when we stay angry for a long time.', 'Smiling is the only way to stop feeling upset.'],
 "이유 ▶ it takes a lot of muscles to look angry, but only a few to smile ✔\n오답 ▶ {1} 반대(웃을 때 근육이 적게 듦) — 함정 {2} 수리 약속 없음 {3} 화난 상태 → 근육이 '피곤함' {4} 유일한 방법이라는 말 없음",
 [('facial muscle', '얼굴 근육'), ('while', '반면에')], 3)
# 4 (3) 반려동물 계산
T4.flex('다음 대화의 내용과 일치하는 것은?', '8과 대화', Bx(
 "Alex: John, what is this graph about?", "John: I did a survey on the kinds of pets my classmates have.", "Alex: What were the results?",
 "John: Eighty percent of the students have pets. Only five out of twenty-five students don't have pets.", "Alex: What kind of pets do they have?",
 "John: Well, ten students have dogs and three students have cats.", "Alex: What about the rest?", "John: Seven students have fish."),
 ['Forty percent of the students have dogs.', 'Twenty students have dogs or cats.', 'Fish are the most popular pet in the class.', "Three students don't have any pets.", 'Twenty-eight percent of the students have cats.'],
 "이유 ▶ 25명 중 10명 = 40% ✔\n오답 ▶ {1} 개 10 + 고양이 3 = 13명 {2} 가장 많은 건 개(10명) {3} 없는 학생은 5명 {4} 28%(7명)는 물고기, 고양이는 3명 = 12%",
 [('the rest', '나머지'), ('survey', '조사')], 3)
# 5 (4) 가정법 전환 틀린 것
T4.flex('다음 문장을 가정법으로 바꾼 것 중 <u>틀린</u> 것은?', '7과 문법', '',
 ['As she knows the answer, she can help us.<br>→ If she didn\'t know the answer, she could help us.',
  'As I don\'t have wings, I can\'t fly to you.<br>→ If I had wings, I could fly to you.',
  'As he isn\'t rich, he can\'t build a mirror house.<br>→ If he were rich, he could build a mirror house.',
  'As I don\'t live in a tulou, I don\'t have friends at home to play with.<br>→ If I lived in a tulou, I would have friends at home to play with.',
  'As it doesn\'t snow, Taeho can\'t test his sled.<br>→ If it snowed, Taeho could test his sled.'],
 "이유 ▶ 긍정·부정을 '둘 다' 반대로: If she didn't know the answer, she couldn't help us. → could ❌\n오답 ▶ {1}{2}{3}{4} 현재 사실 반대 → 과거형(be는 were) + would/could + 동사원형, 긍정↔부정 모두 바꿈",
 [('wing', '날개')], 4)
# 6 (3) 5형식 개수
T4.fixed('다음 중 어법상 옳은 문장의 개수는?', '7과 문법', Bx(
 '(a) The thick walls keep the house quietly.', '(b) The sad news made her upset.', '(c) Raised walkways keep people\'s feet dry.', '(d) This song always makes me happily.', '(e) Please keep the door open.'),
 CNT, 3,
 "이유 ▶ 옳은 것 (b) make + 목적어 + 형용사(upset) (c) keep + 목적어 + 형용사(dry) (e) keep + 목적어 + 형용사(open) → 3개\n틀린 것 ▶ (a) quietly → quiet (d) happily → happy",
 [('quiet', '조용한')], 3)
# 7 (4) too ~ to 전환
T4.flex('다음 문장과 의미가 같도록 바꾼 것으로 어법상 옳은 것은?', '8과 문법', Bx('The tower was so high that we couldn\'t climb it.'),
 ['The tower was too high for us to climb.', 'The tower was too high for us to climb it.', 'The tower was too high of us to climb.', 'The tower was too high for us climbing.', 'The tower was high enough for us to climb.'],
 "이유 ▶ so ~ that 주어 couldn't … = too ~ for 의미상 주어 to … / 문장 주어(The tower)가 climb의 목적어이므로 it을 다시 쓰지 않음 ✔\n오답 ▶ {1} it 중복 {2} high는 for {3} to climb {4} enough to = 오를 수 있었다(반대)",
 [('climb', '오르다')], 4)
# 8 (5) 부분 부정 빈칸
T4.flex('다음 대화의 빈칸에 들어갈 말로 가장 알맞은 것은?', '8과 문법', Bx(
 "A: Do all of your classmates like math?", "B: No, ______________________. Some of them love it, but others hate it."),
 ['not all of them like math', 'none of them like math', 'all of them like math', 'no one likes math at all', 'every student likes math'],
 "이유 ▶ 좋아하는 학생도, 싫어하는 학생도 있음 → '모두 좋아하는 것은 아니다'(부분 부정) Not all ✔\n오답 ▶ {1}{3} 아무도 좋아하지 않는다(전체 부정) — Some of them love it과 모순 {2}{4} 모두 좋아한다 — No와 모순",
 [('others', '다른 사람들'), ('hate', '싫어하다')], 5)
# 9 (4) tulou 일치하지 않는 것
T4.flex('다음 글의 내용과 일치하지 <u>않는</u> 것은?', '7과 본문 ❸', Bx(
 "If I lived in a tulou, a huge round house in Fujian, China, I would always have friends at home to play with. I would sometimes hear my neighbor calling me to come over for tea or dinner. "
 "In a tulou, there are usually three to five floors. The first floor is used for cooking and eating. And people store food and tools on the second floor. Do you wonder where I would sleep? My bedroom would be on the third or fourth floor. "
 "A tulou is like a village. The people living in a tulou mostly have the same family name. Some large tulou can house up to 50 families. They work together and share many things. Living together in one building keeps them safe."),
 ['People in a tulou sleep on the first floor so that they can cook easily.', 'Each floor of a tulou is used for a different purpose.', 'The writer imagines hearing a neighbor inviting him or her for tea or dinner.',
  'Most people in a tulou share the same family name.', 'Some tulou are big enough for as many as fifty families.'],
 "이유 ▶ 1층은 요리·식사, 침실은 3층이나 4층 → 1층에서 잔다는 건 틀림\n오답 ▶ {1} 1층 요리·식사, 2층 보관, 3·4층 침실 {2} hear my neighbor calling me to come over {3} mostly have the same family name {4} up to 50 families",
 [('purpose', '목적, 용도'), ('house', '수용하다')], 4)
# 10 (3) Venice 삽입
T4.fixed('글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳은?', '7과 본문 ❷', Bx(
 "<b>But it was not easy for them to build their homes on this swampy surface.</b>", "",
 "In Venice, there are many colorful houses on the water. ( ① ) You may wonder how and why they built the houses on the water. ( ② ) The old Venetians decided to live there to keep themselves safe from invaders. ( ③ ) "
 "So they installed more than 10 million wooden poles in the ground. ( ④ ) It is these wooden poles that support Venice to this day. ( ⑤ )"),
 None, 3,
 "이유 ▶ 침략자를 피해 물 위에 살기로 함 → 하지만(But) 늪 같은 땅에 짓기는 쉽지 않았다 → 그래서(So) 나무 기둥을 박았다\n오답 ▶ ④ So(그래서 기둥을 박음)의 이유가 사라짐 / ② 어려움 뒤에 '살기로 한 이유'가 끼어들어 So와의 연결이 끊김",
 [('swampy', '늪 같은'), ('install', '설치하다')], 3)
# 11 (4) 간접의문문 배열
T4.flex('다음 우리말을 영작할 때, <u>7번째</u>와 <u>8번째</u>로 오는 단어를 바르게 짝지은 것은?', '7과 본문 ❷ 영작', Bx(
 '여러분은 어떻게 그리고 왜 그들이 물 위에 집을 지었는지 궁금할지도 모른다.', '(13단어, 주어진 단어를 모두 쓰되 필요하면 형태를 바꿀 것: may, wonder, how, why, build, house, water)'),
 ['they − built', 'did − they', 'they − build', 'built − they', 'they − builds'],
 "완성 ▶ You(1) may(2) wonder(3) how(4) and(5) why(6) they(7) built(8) the(9) houses(10) on(11) the(12) water(13).\n이유 ▶ 간접의문문 = 의문사 + 주어 + 동사(did they build ❌) / 과거의 일 → built\n오답 ▶ {1}{3} 의문문 어순 {2} 현재형 {4} 3인칭 단수 아님",
 [('wonder', '궁금해하다')], 4)
# 12 (4) 가주어 빈칸
T4.flex('다음 우리말과 같도록 할 때, 빈칸에 들어갈 말로 알맞은 것은?', '8과 본문 ❶ 영작', Bx('Pascal이 그래프를 읽고 그리는 것은 너무 어려웠다.', '→ It was too hard ________________ graphs.'),
 ['for Pascal to read and draw', 'of Pascal to read and draw', 'for Pascal reading and drawing', 'Pascal to read and draw', 'for Pascal to reading and draw'],
 "이유 ▶ 가주어 It + too hard + for 의미상 주어 + to read and (to) draw ✔\n오답 ▶ {1} hard는 for {2} to부정사 {3} for 빠짐 {4} to + 동사원형",
 [('draw', '그리다')], 4)
# 13 (3) 8과 삽입
T4.fixed('글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳은?', '8과 본문 ❹', Bx(
 "<b>Pascal drew a graph and showed it to Robin.</b>", "",
 "\"So, you should go inside between six in the morning and noon.\" ( ① ) \"What? I don't get it.\" ( ② ) Pascal thought for a moment. 'Hmm... A graph might make this easier to understand.' ( ③ ) "
 "\"Look, the most dangerous time is between six in the evening and midnight.\" ( ④ ) \"Aha! I get it now. Thank you so much, Pascal!\" ( ⑤ )"),
 None, 3,
 "이유 ▶ '그래프가 더 이해하기 쉽게 해 줄지도' → 그래프를 그려 보여 줌 → \"Look(보세요), ~\" 그래프를 보며 설명\n오답 ▶ ② 그래프를 생각하기 전 / ④ 이미 Look 하고 설명을 시작한 뒤",
 [('noon', '정오')], 3)
# 14 (4) (A)(B)(C)
T4.flex('다음 글의 (A), (B), (C)의 각 네모 안에서 어법에 맞는 표현으로 가장 적절한 것은?', '8과 본문 ❸', Bx(
 "\"Well, can you help us (A) [ get / getting ] back the money (B) [ that / what ] the king took from the people? He taxed them too much. "
 "He is too greedy (C) [ to share / sharing ] with the people, so they don't have enough money to buy food.\""),
 ['get − that − to share', 'getting − that − to share', 'get − what − to share', 'get − that − sharing', 'getting − what − sharing'],
 "이유 ▶ (A) help + 목적어 + 동사원형 → get (B) 선행사 the money가 있음 → 관계대명사 that (what은 선행사 포함) (C) too ~ to …\n오답 ▶ getting ❌ / what ❌ / sharing ❌",
 [('tax', '세금을 매기다')], 4)
# 15 (5) 그래프 순서
T4.flex('다음 글을 그래프로 나타낼 때, 군인 수가 <u>많은</u> 시간대부터 바르게 나열한 것은?', '8과 본문 ❹', Bx(GR),
 ['6 p.m.~midnight > noon~6 p.m. > midnight~6 a.m. > 6 a.m.~noon', 'noon~6 p.m. > 6 p.m.~midnight > midnight~6 a.m. > 6 a.m.~noon', '6 p.m.~midnight > midnight~6 a.m. > noon~6 p.m. > 6 a.m.~noon',
  '6 p.m.~midnight > noon~6 p.m. > 6 a.m.~noon > midnight~6 a.m.', 'midnight~6 a.m. > 6 p.m.~midnight > noon~6 p.m. > 6 a.m.~noon'],
 "이유 ▶ 자정~오전 6시 5명, 오전 6시~정오 3명, 정오~오후 6시 8명, 오후 6시~자정 12명 → 12 > 8 > 5 > 3\n함정 ▶ until noon / until six in the evening / until midnight — 시작 시각은 바로 앞 시간대가 끝난 때",
 [('until', '~까지')], 5)
# 16 (4) 영작 개수
T4.fixed('다음 우리말을 영작한 것 중 어법상 옳은 것의 개수는?', '8과 본문 영작', Bx(
 '(a) 그는 누가 말하고 있는지 보려고 고개를 들었다. → He looked up to see who was talking.', '(b) 그는 로빈 후드가 자기에게 손을 흔드는 것을 보았다. → He saw Robin Hood to wave at him.',
 '(c) 나는 내가 왜 여기 있는지 모른다. → I don\'t know why am I here.', '(d) 그는 책을 읽다가 잠들기로 했다. → He decided reading himself to sleep.', '(e) 그는 남자들이 소리치는 것을 들었다. → He heard men shouting.'),
 CNT, 2,
 "이유 ▶ 옳은 것 (a) 목적의 to부정사 + 간접의문문(who가 주어) (e) 지각동사 hear + 목적어 + -ing → 2개\n틀린 것 ▶ (b) to wave → wave/waving (c) why am I → why I am (d) decide + to부정사 → to read",
 [('wave', '손을 흔들다')], 4)
# 17 (5) JH 알 수 있는 것 모두
T4.flex('[17~20] 다음 글을 읽고 물음에 답하시오.<br>17. 윗글을 읽고 알 수 있는 것을 <u>모두</u> 고른 것은?<br>(a) why people take off their shoes in the genkan<br>(b) what tatami mats are made from<br>(c) what people do with the shoji for large gatherings<br>(d) how long it takes to build a traditional house<br>(e) why the roofs are sloped', '외부지문 · Reading File', JH,
 ['(b), (c), (e)', '(a), (b), (c)', '(b), (d)', '(a), (c), (e)', '(c), (d), (e)'],
 "이유 ▶ (b) woven grass (c) 떼어 내 큰 방을 만듦 (e) 빗물이 쉽게 흘러내리게 → (b)(c)(e)\n함정 ▶ (a) 신발을 벗는 '장소'는 나오지만 '이유'는 없음 (d) 짓는 기간 없음",
 [('sloped', '경사진')], 5)
# 18 (5) JH 삽입
T4.fixed('18. 위 글(17번)의 흐름으로 보아, 다음 문장이 들어가기에 가장 적절한 곳은?', '외부지문 · Reading File', Bx(
 "<b>The house also has sloped roofs because they keep rainwater flowing off easily.</b>", "",
 "When the weather gets cold, people prefer to sit at a kotatsu, a heated table, and put their legs in it. ( ① ) Keeping their body warm, Japanese have meals, drink tea, or read books at the table. ( ② ) In summer, heavy rain can cause flooding. ( ③ ) "
 "The floor of the house is raised a little off the ground to keep the living area dry and safe from flooding. ( ④ ) The roofs are covered with kawara tiles. ( ⑤ ) The strong kawara tiles are not only water-resistant but also fireproof."),
 None, 4,
 "이유 ▶ 비 대비 ① 바닥을 높임 → 또한(also) ② 경사 지붕 → 그 지붕(The roofs)은 kawara 기와로 덮임\n오답 ▶ ③ 바닥 이야기보다 먼저 also가 나오면 어색 / ⑤ The roofs가 처음 나올 때 이미 '지붕' 소개가 필요",
 [('flow off', '흘러내리다')], 5)
# 19 (5) JH (A)(B)(C)
T4.flex('19. 다음은 위 글(17번)의 일부이다. (A), (B), (C)의 각 네모 안에서 어법에 맞는 표현으로 가장 적절한 것은?', '외부지문 · Reading File', Bx(
 "Instead, they sit directly on tatami mats that (A) [ is / are ] made from woven grass. When the weather gets cold, people prefer to sit at a kotatsu, a heated table, and (B) [ put / putting ] their legs in it. "
 "The house also has sloped roofs because they keep rainwater (C) [ flowing / to flow ] off easily."),
 ['are − put − flowing', 'is − put − flowing', 'are − putting − flowing', 'are − put − to flow', 'is − putting − to flow'],
 "이유 ▶ (A) 선행사 tatami mats(복수) → are (B) prefer to sit and (to) put — to부정사 병렬 (C) keep + 목적어 + -ing(계속 ~하게 하다) → flowing",
 [('woven', '짠, 엮은'), ('heated', '데워진')], 5)
# 20 (5) JH 영작
T4.flex('20. 위 글(17번)의 내용과 일치하도록 다음 우리말을 영작할 때 가장 알맞은 것은?', '외부지문 · Reading File 영작', Bx('지붕은 방수일 뿐만 아니라 불에도 강한 기와로 덮여 있다.'),
 ['The roofs are covered with tiles that are not only water-resistant but also fireproof.', 'The roofs are covered with tiles that is not only water-resistant but also fireproof.',
  'The roofs cover with tiles that are not only water-resistant but also fireproof.', 'The roofs are covered with tiles that are not only water-resistant and also fireproof.',
  'The roofs are covered with tiles that are either water-resistant or fireproof.'],
 "이유 ▶ 지붕이 '덮여 있는' → are covered with / 선행사 tiles(복수) → are / not only A but also B ✔\n오답 ▶ {1} is ❌ {2} 능동 cover ❌ {3} not only ~ and also ❌ {4} either A or B(둘 중 하나) — 뜻이 다름",
 [('water-resistant', '방수의'), ('fireproof', '내화성의, 불에 강한')], 5)
# 21 (3) PB 일치하지 않는 것
T4.flex('[21~24] 외부지문 Picture Bride<br>' + PBN + '<br>21. 시의 내용과 일치하지 <u>않는</u> 것은?', '외부지문 · Picture Bride', '',
 ['할머니가 한국을 떠날 때 지금의 화자보다 한 살 많았다.', '할머니는 부산을 떠나 하와이로 향했다.', '남자는 와이알루아 설탕 공장 근처의 노동자 숙소에서 지냈다.', '남자는 할머니의 사진을 빛에 비추어 보았다.', '남편은 할머니보다 열세 살 많았다.'],
 "이유 ▶ 할머니 23세, 화자 24세 → 할머니가 한 살 '적었음' — 비교 방향을 뒤집은 함정\n오답 ▶ {1} 부산 → 하와이 {2} Waialua 설탕 공장 근처 노동자 숙소 {3} 사진을 빛에 비춤 {4} 13살 연상",
 [('mill', '공장, 제분소')], 3)
# 22 (5) PB 처지
T4.flex('22. 시에 나타난 할머니의 처지로 가장 알맞은 것은?', '외부지문 · Picture Bride', '',
 ['She was leaving everything familiar to marry a man she knew only from a photograph.', 'She was going to work at a tailor shop in Hawaii with her husband.', 'She had lived in Hawaii as a child and was finally returning home.',
  'She was taking a short trip to Hawaii and planned to come back soon.', 'She was moving to Hawaii because her husband had visited her in Pusan.'],
 "이유 ▶ 사진신부 — 익숙한 고향을 떠나 사진으로만 아는 남자와 결혼하러 감 ✔\n오답 ▶ {1} 양복점은 '부산'에서 지나친 곳(함정) {2} 하와이는 거의 모르는 섬 {3} 짧은 여행 아님 {4} 남편은 하와이에서 기다림, 처음 만나는 낯선 사람",
 [('familiar', '익숙한')], 5)
# 23 (4) PB O/X
T4.fixed('23. 시의 내용에 대한 O/X를 바르게 짝지은 것은?', '외부지문 · Picture Bride', Bx(
 '(a) 화자는 할머니가 떠날 때 몇 살이었는지 알고 있다.', '(b) 할머니가 탄 배는 할머니가 거의 알지 못하는 섬으로 향했다.', '(c) 남자는 큰 도시의 편안한 집에서 할머니를 기다렸다.', '(d) 마지막 장면의 바람은 시원하고 촉촉했다.'),
 ['O − O − X − X', 'O − X − X − X', 'O − O − O − X', 'X − O − X − X', 'O − O − X − O'], 1,
 "이유 ▶ (a) 23세라고 밝힘 → O (b) 거의 알지 못하는 섬 → O (c) 설탕 공장 근처 노동자 숙소 → X (d) 불타는 사탕수수 밭의 뜨겁고 건조한 바람 → X",
 [('humid', '습한')], 4)
# 24 (5) PB 학생 판단
T4.flex('24. 시를 바르게 이해한 학생을 <u>모두</u> 고른 것은?', '외부지문 · Picture Bride', Bx(
 '민지: 이 시는 할머니가 손녀에게 직접 들려주는 이야기 형식이야.', '준호: 화자는 질문을 던지며 할머니의 마음을 상상해.', '서연: 남자가 사진을 빛에 비춰 본 건 아직 만나 본 적 없는 신부를 알고 싶었기 때문으로 볼 수 있어.',
 '태민: 사탕수수 밭의 뜨거운 바람은 할머니가 앞으로 누릴 편안한 생활을 보여 줘.', '하린: 사진신부는 사진만 보고 결혼 상대를 정해 먼 곳으로 떠난 여성이야.'),
 ['준호, 서연, 하린', '민지, 준호', '서연, 태민', '민지, 서연, 하린', '준호, 태민, 하린'],
 "이유 ▶ 준호(질문 = 상상) · 서연(사진만으로 신부를 앎) · 하린(사진신부 뜻) ✔\n틀린 것 ▶ 민지: 말하는 사람은 손녀(화자), 할머니가 직접 말하지 않음 / 태민: 뜨겁고 건조한 바람 = 고된 삶의 암시(편안함 ❌)",
 [('granddaughter', '손녀')], 5)
# 25 (4) 종합 고치기
T4.flex('다음 중 밑줄 친 부분을 바르게 고친 것은?', '7·8과 종합', '',
 ['If I <u>live</u> in Venice, I would take a gondola to school. → lived', 'It\'s too dangerous <u>for</u> you to stand there. → of', 'No one <u>needs</u> graphs in real life. → need',
  'Living together in one building <u>keeps</u> them safe. → keep', 'I would sometimes hear my neighbor <u>calling</u> me. → to call'],
 "이유 ▶ 주절이 would take → 가정법 과거 If + 과거형 lived ✔\n오답 ▶ {1} dangerous는 for(원래 맞음) {2} No one은 단수 → needs가 맞음 {3} 동명사 주어 단수 → keeps가 맞음 {4} 지각동사 hear + 목적어 + -ing/동사원형(to call ❌)",
 [('gondola', '곤돌라')], 4)

for T in (T3, T4):
    assert len(T.items) == 25, len(T.items)
    for it, p in zip(T.items, K25):
        assert it['pts'] == p, (T.tid, it['stem'][:30], it['pts'], p)
        if it['opts']: assert len(set(map(str, it['opts']))) == 5, it['stem']
    T.render()
