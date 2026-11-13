# 11/13 중산중1 동아(윤정미) 5과 문법 변형 1·2·3차 (각 20문항) — 원본: Grammar Build Up 5과 객관식(hwp)
# 문법: Pattern 1 비교급 · Pattern 2 최상급 · Pattern 3 There is/are — 원본 유형을 살리되 어휘·문장을 바꾸고 난도를 올림 (1차 중상 → 2차 상 → 3차 최상)
from wu_m1g5 import *
H = ('5과 문법 변형', '중1 영어 동아(윤정미) Lesson 5 Grammar', '동아(윤정미) 5과 문법', 'm1g5')
B = lambda *ls: BOX('<br>'.join(ls))
NUMS = ['1개', '2개', '3개', '4개', '5개']
E_, A_, T_ = '비교급', '최상급', 'There is/are'

# ═══════════════ 1차 (중상) ═══════════════
T = Test('1', '1차', '비교급 · 최상급 · There is/are', '5과 문법',
 '범위: 5과 문법 — 비교급(-er / more ~ than), 최상급(the -est / the most ~), There is/are. 교재 문제와 똑같지 않고 어휘를 바꿔 만들었어요. 문장 전체를 끝까지 읽고 고르세요.', H=H)
T.flex('다음 빈칸에 들어갈 말로 알맞은 것은?', E_, B('This winter is much ' + BL + ' than last winter.'),
 ['colder', 'more cold', 'coldest', 'the coldest', 'cold'],
 "이유 ▶ 뒤에 than(~보다) + 앞에 much(훨씬, 비교급 강조) → 비교급. cold는 1음절이라 -er → colder.\n오답 ▶ {1} 1음절에는 more를 붙이지 않는다 {2}·{3} 최상급은 than과 함께 못 쓴다 {4} 원급은 than 앞에 못 온다\n포인트 ▶ much / even / far / a lot + 비교급 + than", [])
T.flex('다음 중 원급과 비교급이 바르게 짝지어진 것은?', E_, '',
 ['thin – thinner', 'wise – wiseer', 'noisy – noisyer', 'famous – famouser', 'bad – badder'],
 "이유 ▶ thin은 「단모음 + 단자음」 → 자음을 한 번 더 쓰고 -er → thinner.\n오답 ▶ {1} -e로 끝나면 -r만 → wiser {2} 「자음 + y」 → y를 i로 → noisier {3} -ous로 끝나는 2음절 이상 → more famous {4} 불규칙 → worse\n포인트 ▶ 단모음+단자음(thin, big, hot, fat, wet)은 자음 하나 더!", [])
T.flex('다음 중 원급과 최상급의 연결이 바르지 <u>않은</u> 것은?', A_, '',
 ['little – littlest', 'wet – wettest', 'useful – most useful', 'far – farthest', 'well – best'],
 "이유 ▶ little(적은)은 불규칙 → little – less – least.\n오답 ▶ {1} 단모음+단자음 → wettest ✔ {2} -ful → most useful ✔ {3} far – farther – farthest ✔ {4} well – better – best ✔\n포인트 ▶ 불규칙 4총사: good/well – better – best · bad – worse – worst · many/much – more – most · little – less – least", [])
T.flex('다음 빈칸에 공통으로 들어갈 말로 알맞은 것은?', A_, B('• Mina is the ' + BL + ' dancer in our club.', '• Who sings ' + BL + ' in your family?'),
 ['best', 'better', 'well', 'most', 'good'],
 "이유 ▶ 첫 문장: the + ___ + 명사 + in our club → 최상급 형용사(good → best) / 둘째 문장: 동사 sings를 꾸미는 부사 + in your family(범위) → 최상급 부사(well → best). 둘 다 best!\n오답 ▶ {1} better는 than과 함께, the와 in ~(범위)에는 최상급 {2}·{4} 원급은 범위 표현과 어울리지 않음 {3} most는 3음절 이상 형용사 앞에 붙는 말\n포인트 ▶ good(형)·well(부) 모두 최상급은 best.", [])
T.flex('다음 빈칸에 들어갈 수 <u>없는</u> 것은?', E_, B("Today's quiz was " + BL + " harder than yesterday's."),
 ['very', 'much', 'even', 'far', 'a lot'],
 "이유 ▶ very는 원급만 꾸민다(very hard ⭕, very harder ❌).\n오답 ▶ {1}·{2}·{3}·{4} much / even / far / a lot은 비교급을 강조(훨씬)\n포인트 ▶ 비교급 강조어 = much, even, far, a lot, still", [])
T.flex('다음 빈칸에 들어갈 말로 알맞은 것은?', T_, B('There ' + BL + ' a lot of furniture in the old house.'),
 ['is', 'are', 'be', 'have', 'has'],
 "이유 ▶ There is/are 뒤의 명사가 진짜 주어. furniture(가구)는 셀 수 없는 명사라 a lot of가 붙어도 단수 취급 → is.\n오답 ▶ {1} a lot of만 보고 복수로 착각한 함정 {2} 동사원형은 불가 {3}·{4} '있다'는 There + be동사\n포인트 ▶ a lot of + 셀 수 없는 명사(water, money, furniture, homework) → There is", [])
T.flex('다음 질문에 대한 응답으로 알맞은 것은?', T_, B('A: Were there any empty seats on the train?', 'B: ' + BL + ' It was full of people.'),
 ["No, there weren't.", "No, they weren't.", 'Yes, there was.', "No, it wasn't.", 'Yes, they were.'],
 "이유 ▶ Were there ~? 로 물으면 there로 답한다 → No, there weren't. 뒤의 '사람들로 꽉 찼다'와도 맞는다.\n오답 ▶ {1}·{4} they로 답하지 않는다 {2} 복수(seats)인데 was, 게다가 뒤 내용과 반대 {3} it으로 답하지 않는다\n포인트 ▶ Is/Are/Was/Were there ~? → Yes, there is[are…]. / No, there isn't[aren't…].", [])
T.flex('다음 중 어법상 <u>어색한</u> 문장은?', E_, '',
 ['This puzzle is more simpler than that one.', 'A cheetah runs faster than a horse.', 'Silver is less valuable than gold.', 'My bag is much heavier than yours.', 'He got up earlier than his parents.'],
 "이유 ▶ more와 -er을 겹쳐 쓸 수 없다 → simpler.\n오답 ▶ {1} fast – faster ✔ {2} less + 원급(덜 ~한) ✔ {3} much(훨씬) + heavier ✔ {4} early – earlier ✔\n포인트 ▶ more + 비교급 ❌ (more simpler, more bigger, more worse)", [])
T.flex('다음 중 어법상 올바른 문장은?', A_, '',
 ['The Nile is the longest river in the world.', 'She is the most smartest girl in my class.', 'This is the most cheap shirt in the store.', 'Jupiter is the bigest planet of all.', 'He is the taller boy of the three.'],
 "이유 ▶ long – longest, 범위는 in the world ✔\n오답 ▶ {1} most와 -est 중복 → the smartest {2} 1음절 → the cheapest {3} 단모음+단자음 → biggest {4} 셋 중에서 → 최상급 the tallest\n포인트 ▶ 셋 이상에서 '가장' → 최상급", [])
T.flex('다음은 5과 본문의 용의자 정보이다. 이를 설명한 내용으로 바르지 <u>않은</u> 것은?', '본문 응용',
 B('Andres Lozano: 176 cm · Larry Johnson: 173 cm · Tim Baker: 182 cm · Luca Ferez: 166 cm'),
 ['Larry is taller than Andres.', 'Tim is the tallest of the four.', 'Luca is shorter than Larry.', 'Andres is taller than Luca.', 'Luca is the shortest of the four suspects.'],
 "이유 ▶ Larry(173 cm) < Andres(176 cm) → Larry가 더 '작다'.\n오답 ▶ {1} Tim 182 cm로 가장 큼 ✔ {2} 166 < 173 ✔ {3} 176 > 166 ✔ {4} 166 cm로 가장 작음 ✔\n포인트 ▶ 표 문제는 비교 대상 두 개를 숫자로 다시 확인!", [])
T.flex('다음 빈칸에 들어갈 말로 알맞은 것은?', '본문 응용', B("I'm about 170 cm tall, and the man was a little " + BL + " than me."),
 ['taller', 'tall', 'tallest', 'more tall', 'the tallest'],
 "이유 ▶ than + a little(조금) → 비교급 taller. 본문: he was a little taller than me.\n오답 ▶ {1} 원급 불가 {2}·{4} 최상급 불가 {3} 1음절은 -er\n포인트 ▶ a little + 비교급 = 조금 더 ~한", [])
T.flex('다음 중 어법상 <u>어색한</u> 문장은?', T_, '',
 ['There are a wheelchair near the painting.', 'There were pieces of cake all over the painting.', 'There is a cake box next to the wheelchair.', 'Is there a bakery near the museum?', "There weren't any guards in the room."],
 "이유 ▶ a wheelchair(단수) → There is[was].\n오답 ▶ {1} pieces(복수) → were ✔ {2} a cake box(단수) → is ✔ {3} 의문문 Is there ~? ✔ {4} 부정문 + any ✔\n포인트 ▶ be동사는 there가 아니라 뒤의 명사에 맞춘다.", [])
T.flex('다음 문장과 의미가 같은 것은?', A_, B('No other student in my class is taller than Jiho.'),
 ['Jiho is the tallest student in my class.', 'Jiho is taller than only one student.', 'Jiho is not as tall as the other students.', 'Jiho is the shortest student in my class.', 'Some students are taller than Jiho.'],
 "이유 ▶ 우리 반에서 지호보다 키 큰 학생은 없다 = 지호가 반에서 가장 키가 크다.\n오답 ▶ {1} 한 명보다만 큼 ✘ {2} 다른 학생만큼 크지 않다(반대) {3} 가장 작다(반대) {4} 지호보다 큰 학생이 있다(반대)\n포인트 ▶ No other + 명사 + 비교급 + than A = A가 가장 ~하다", [])
T.flex('다음 우리말을 영어로 바르게 옮긴 것은?', E_, B('이 상자는 저 상자보다 덜 무겁다.'),
 ['This box is less heavy than that one.', 'This box is less heavier than that one.', 'This box is heavier than that one.', 'This box is not heavy than that one.', 'This box is the least heavy.'],
 "이유 ▶ '덜 ~한' = less + 원급 + than.\n오답 ▶ {1} less 뒤에 비교급 ❌ {2} 더 무겁다(반대) {3} not + 원급 + than은 틀린 형태 {4} '가장 덜 무거운'(최상급) + 비교 대상 없음\n포인트 ▶ less + 원급(heavy) ⭕ / less + 비교급(heavier) ❌", [])
T.flex('다음 빈칸에 들어갈 말로 알맞은 것은?', A_, B('Kevin is the youngest ' + BL + ' the five members.'),
 ['of', 'in', 'than', 'at', 'to'],
 "이유 ▶ the five members는 '비교 대상(사람 여럿)' → of + 복수.\n오답 ▶ {1} in은 장소·집단 범위(in the team, in Korea) {2} than은 비교급과 함께 {3}·{4} 쓰지 않음\n포인트 ▶ 최상급 + of + 복수 비교 대상 / in + 장소·범위", [])
T.flex('다음 대화의 빈칸에 들어갈 말로 알맞은 것은?', E_, B('A: Which is ' + BL + ', the subway or the bus?', 'B: The subway is. It never gets stuck in traffic.'),
 ['faster', 'fastest', 'more fast', 'the fast', 'fast'],
 "이유 ▶ 둘(the subway or the bus) 중 '어느 것이 더' → Which is 비교급, A or B?\n오답 ▶ {1} 둘 비교에는 최상급 ❌ {2} 1음절은 -er {3}·{4} 원급 ❌\n포인트 ▶ Which ~ 비교급, A or B? (둘 중에서)", [])
T.fixed('다음 <보기>에서 어법상 <u>어색한</u> 문장의 개수는?', '종합', B(
 '(a) There is many books on the shelf.', '(b) Seoul is bigger than Busan.', '(c) Health is the most important thing in life.', '(d) My dog is more cuter than yours.', '(e) There were two cats under the car.'),
 NUMS, 2,
 "이유 ▶ 어색한 것 (a)·(d) 2개. (a) many books(복수) → There are (d) more와 -er 중복 → cuter\n오답 ▶ (b) big – bigger ✔ (c) 3음절 이상 → the most important ✔ (e) two cats → were ✔\n포인트 ▶ 개수 문제는 한 문장씩 ⭕ / ❌ 표시하며 세기!", [])
T.flex('다음은 Mina의 방에 있는 물건이다. 내용과 일치하지 <u>않는</u> 것은?', T_, B('Mina\'s room: a bed · two lamps · some books · (TV 없음)'),
 ["There is a TV in Mina's room.", "There is a bed in Mina's room.", "There are two lamps in Mina's room.", "There isn't a TV in Mina's room.", "There are some books in Mina's room."],
 "이유 ▶ TV는 없다 → There isn't a TV.\n오답 ▶ {1} 침대 하나 ✔ {2} 램프 두 개 → are ✔ {3} TV 없음 ✔ {4} 책 몇 권 → are ✔", [])
T.flex('다음 글을 읽고, 가장 어린 사람을 고르면?', E_, B('Amy is older than Ben. Ben is older than Chris. Dan is younger than Chris.'),
 ['Dan', 'Amy', 'Ben', 'Chris', 'Amy and Dan'],
 "이유 ▶ Amy > Ben > Chris > Dan(나이 많은 순). Dan이 Chris보다도 어리다 → 가장 어림.\n포인트 ▶ older(나이 많은) ↔ younger(어린) 방향을 화살표로 적어 보자.", [])
T.flex('다음 빈칸에 들어갈 말로 알맞은 것은?', '본문 응용', B('We had a lot of different cakes, but he just wanted the ' + BL + ' one.'),
 ['smallest', 'smaller', 'small', 'most small', 'smalest'],
 "이유 ▶ 많은 케이크 중 '가장 작은' 것 → the + 최상급 smallest. 본문: he just wanted the smallest one.\n오답 ▶ {1} 비교급은 than과 / 둘 중 비교 {2} the + 원급 + one은 '가장'의 뜻이 아님 {3} 1음절은 -est {4} 철자 오류(smallest)\n포인트 ▶ the + 최상급 + one(=cake)", [])
T.render()

# ═══════════════ 2차 (상) ═══════════════
T = Test('2', '2차', '비교급 · 최상급 · There is/are', '5과 문법',
 '범위: 5과 문법 — 비교급 · 최상급 · There is/are. 1차보다 어려워요. 비교 대상, 범위(in/of), 셀 수 없는 명사를 꼼꼼히 보세요.', H=H)
T.flex('다음 중 원급 – 비교급 – 최상급이 모두 바르게 연결된 것은?', '비교급·최상급', '',
 ['big – bigger – biggest / pretty – prettier – prettiest', 'hot – hoter – hotest / good – better – best', 'busy – busyer – busyest / large – larger – largest',
  'little – less – lest / thin – thinner – thinnest', 'careful – carefuler – carefulest / bad – worse – worst'],
 "이유 ▶ big(단모음+단자음 → gg) / pretty(자음+y → i) 둘 다 ✔\n오답 ▶ {1} hotter – hottest {2} busier – busiest {3} least {4} more careful – most careful\n포인트 ▶ 한 줄에 두 단어 → 둘 다 맞아야 정답!", [])
T.table('(A), (B), (C)의 각 네모 안에서 어법에 맞는 표현으로 바르게 짝지은 것은?', '종합', B(
 '• The weather is getting <b>(A)</b> [ worse / badder ].', '• This is the <b>(B)</b> [ most exciting / excitingest ] game of the season.', '• There <b>(C)</b> [ is / are ] lots of sand on the beach.'),
 ['(A)', '(B)', '(C)'], [['worse', 'most exciting', 'is'], ['badder', 'most exciting', 'is'], ['worse', 'excitingest', 'is'], ['worse', 'most exciting', 'are'], ['badder', 'excitingest', 'are']],
 "이유 ▶ (A) bad의 비교급은 불규칙 worse (B) exciting(-ing, 3음절) → the most exciting (C) sand(모래)는 셀 수 없는 명사 → lots of가 있어도 is\n오답 ▶ badder·excitingest는 없는 말 / lots of만 보고 are를 고르는 함정\n포인트 ▶ 셀 수 없는 명사: sand, water, money, information, furniture", [])
T.flex('다음 중 어법상 <u>어색한</u> 문장은?', A_, '',
 ['Of all the subjects, I like science better.', 'Who is the most famous actor in Korea?', 'This road is much wider than that one.', 'Which do you like better, tea or coffee?', 'Minsu is one of the tallest boys in his class.'],
 "이유 ▶ Of all the subjects(모든 과목 중에서) → 최상급 → I like science (the) best.\n오답 ▶ {1} famous → the most famous ✔ {2} much + 비교급 ✔ {3} 둘 중 → better ✔ {4} one of the + 최상급 + 복수명사 ✔\n포인트 ▶ like A better(둘 중) / like A best(셋 이상 중)", [])
T.flex('다음 빈칸에 들어갈 말로 알맞은 것은?', A_, B('Seoul is one of the ' + BL + ' in the world.'),
 ['biggest cities', 'biggest city', 'bigger cities', 'big cities', 'most big city'],
 "이유 ▶ one of the + 최상급 + 복수명사 = 가장 ~한 것들 중 하나.\n오답 ▶ {1} 단수명사 ❌ {2} 비교급 ❌ {3} 원급 ❌ {4} most big ❌ + 단수\n포인트 ▶ one of the + -est + 복수(-s)", [])
T.flex('다음 문장과 의미가 같은 것은?', E_, B('Mike is not as fast as Tom.'),
 ['Tom is faster than Mike.', 'Mike is faster than Tom.', 'Mike and Tom are equally fast.', 'Tom is not as fast as Mike.', 'Mike is the fastest of all.'],
 "이유 ▶ not as 원급 as = ~만큼 …하지 않다 → Mike는 Tom만큼 빠르지 않다 = Tom이 더 빠르다.\n오답 ▶ {1}·{3} 반대 {2} 똑같이 빠르다는 as fast as(긍정) {4} 근거 없음\n포인트 ▶ A is not as ~ as B = B is ~er than A", [])
T.flex('다음 중 어법상 올바른 문장은?', T_, '',
 ['Are there any problems with the plan?', "There isn't some water in the bottle.", 'Is there many people in the park?', "There aren't a cloud in the sky.", 'Was there any students in the classroom?'],
 "이유 ▶ problems(복수) → Are there ✔, 의문문에 any ✔\n오답 ▶ {1} 부정문에는 any → isn't any water {2} many people(복수) → Are there {3} a cloud(단수) → isn't a cloud {4} students(복수) → Were there\n포인트 ▶ 의문·부정 → any / 수 일치는 뒤의 명사", [])
T.flex('다음 우리말을 영어로 바르게 옮긴 것은?', E_, B('날씨가 점점 더 추워지고 있다.'),
 ['The weather is getting colder and colder.', 'The weather is getting more and more cold.', 'The weather is getting cold and cold.', 'The weather is getting coldest and coldest.', 'The weather is getting more colder and colder.'],
 "이유 ▶ 점점 더 ~한 = 비교급 and 비교급 → colder and colder.\n오답 ▶ {1} 1음절은 -er (more and more는 3음절 이상: more and more interesting) {2} 원급 ❌ {3} 최상급 ❌ {4} more + -er 중복\n포인트 ▶ 비교급 and 비교급 = 점점 더 ~한", [])
T.flex('다음 대화의 빈칸에 들어갈 말로 알맞은 것은?', T_, B('A: Is there a post office near here?', "B: Yes, " + BL + ". It's next to the bank."),
 ['there is', 'it is', 'there are', 'they are', 'it does'],
 "이유 ▶ Is there ~? → Yes, there is.\n오답 ▶ {1}·{3} it/they로 답하지 않음 {2} a post office(단수)인데 are {4} be동사 의문문에 does ❌\n포인트 ▶ 질문의 be동사(Is)와 같은 be동사로 답한다.", [])
T.flex('5과 본문의 내용과 일치하는 것은?', '본문 응용', B('<b>Carlos Diaz:</b> An old man with gray hair was running away, and something fell off his head. It was his wig. I ran after him, but I couldn\'t catch him. He was faster than me.'),
 ['Carlos was slower than the man.', 'Carlos was faster than the man.', 'The man ran more slowly than Carlos.', 'Carlos caught the man easily.', 'The man was the slowest runner of all.'],
 "이유 ▶ He was faster than me(그가 나보다 빨랐다) = Carlos가 그 남자보다 느렸다.\n오답 ▶ {1}·{2} 반대 {3} couldn't catch him(잡지 못함) {4} 근거 없음\n포인트 ▶ A is faster than B = B is slower than A (비교급 뒤집기)", [])
T.fixed('다음 중 어법상 올바른 문장의 개수는?', '종합', B(
 '(a) Mt. Everest is the highest mountain in the world.', '(b) My grandma is the wisest person of my family.', '(c) There is a lot of water in the tank.', '(d) He speaks English more fluently than me.', "(e) This is the worse movie I've ever seen."),
 NUMS, 3,
 "이유 ▶ 올바른 것 (a)·(c)·(d) 3개.\n오답 ▶ (b) 범위(가족 안에서) → in my family (e) 최상급 → the worst movie\n포인트 ▶ (c) water는 셀 수 없음 → There is ✔ / (d) -ly 부사는 more fluently ✔", [])
T.fixed('다음 빈칸에 들어갈 말이 나머지 넷과 <u>다른</u> 것은?', T_, B(
 '① There ' + BL + ' a piano in the hall.', '② There ' + BL + ' some juice in the cup.', '③ There ' + BL + ' a lot of children in the park.',
 '④ There ' + BL + ' an old tree in the yard.', '⑤ There ' + BL + ' much snow on the road.'),
 None, 3,
 "이유 ▶ ③ children은 child의 복수 → are. 나머지는 모두 is.\n오답 ▶ ① a piano(단수) ② juice(셀 수 없음) ④ an old tree(단수) ⑤ snow(셀 수 없음, much) → is\n포인트 ▶ children·people·men·feet은 -s 없는 복수!", [])
T.flex('다음 빈칸에 들어갈 말로 알맞은 것은?', E_, B('This smartphone is ' + BL + ' cheaper than mine.'),
 ['a lot', 'very', 'too', 'so', 'many'],
 "이유 ▶ 비교급 cheaper를 강조 → a lot(훨씬).\n오답 ▶ {1}·{2}·{3} very / too / so는 원급을 꾸밈 {4} many는 명사 앞(many books)\n포인트 ▶ 비교급 강조: much, even, far, a lot, still", [])
T.flex('다음 우리말을 영어로 바르게 옮긴 것은?', A_, B('그는 우리 팀에서 가장 열심히 일하는 사람이다.'),
 ['He is the hardest worker on our team.', 'He is the most hard worker on our team.', 'He is harder worker than our team.', 'He is the hardest workers on our team.', 'He is a hard worker than anyone on our team.'],
 "이유 ▶ hard(1음절) → the hardest + 단수명사 worker.\n오답 ▶ {1} most hard ❌ {2} 비교급 + 비교 대상 오류 {3} 주어 He(한 명) → worker {4} 원급 + than ❌\n포인트 ▶ the -est + 명사 = 가장 ~한 (사람/것)", [])
T.flex('다음 문장과 의미가 같은 것은?', A_, B('Nothing is more precious than time.'),
 ['Time is the most precious thing.', 'Time is less precious than anything.', 'Some things are more precious than time.', 'Time is not precious at all.', 'Nothing is as precious as money.'],
 "이유 ▶ Nothing + 비교급 + than A = A보다 더 ~한 것은 없다 = A가 가장 ~하다.\n오답 ▶ {1}·{2}·{3} 반대 뜻 {4} 돈 이야기가 아님\n포인트 ▶ 부정 주어(Nothing, No one) + 비교급 = 최상급 의미", [])
T.flex('다음 표의 내용과 일치하지 <u>않는</u> 것은?', '비교급·최상급', B('수학 점수 — Yuna: 85 · Jisu: 92 · Hoon: 78 · Mina: 92'),
 ["Mina's score is not as high as Yuna's.", 'Hoon got the lowest score of the four.', "Yuna's score is higher than Hoon's.", "Jisu's score is as high as Mina's.", "Yuna's score is lower than Jisu's."],
 "이유 ▶ Mina 92 > Yuna 85 → Mina는 Yuna'만큼 높지 않은' 게 아니라 더 높다.\n오답 ▶ {1} 78로 가장 낮음 ✔ {2} 85 > 78 ✔ {3} 92 = 92 → as high as ✔ {4} 85 < 92 ✔\n포인트 ▶ 동점이면 as ~ as (최상급 '혼자 1등'에 주의)", [])
T.flex('다음 우리말을 영어로 바르게 옮긴 것은?', T_, B('어제 공원에는 사람들이 많았다.'),
 ['There were a lot of people in the park yesterday.', 'There was a lot of people in the park yesterday.', 'There are a lot of people in the park yesterday.', 'It was a lot of people in the park yesterday.', 'There were a lot of peoples in the park yesterday.'],
 "이유 ▶ 과거(yesterday) + people(복수) → There were.\n오답 ▶ {1} people은 복수 → were {2} yesterday인데 현재 {3} '있다'는 There ~ {4} people은 이미 복수 → peoples ❌(민족들 뜻)\n포인트 ▶ 시제(yesterday) + 수(people) 두 가지 동시 확인!", [])
T.flex('다음 중 어법상 <u>어색한</u> 문장은?', A_, '',
 ['Russia is the larger country in the world.', 'Winter is the coldest season of the year.', 'She runs the fastest in her class.', 'It was the worst day of my life.', 'This is the most delicious pizza I have ever eaten.'],
 "이유 ▶ in the world(세계에서) → 최상급 the largest.\n오답 ▶ {1} the coldest ✔ {2} 부사 최상급 the fastest ✔ {3} bad – worst ✔ {4} the most delicious ✔\n포인트 ▶ 범위 표현(in the world, of the year)이 보이면 최상급!", [])
T.table('(A), (B)의 각 네모 안에서 어법에 맞는 표현으로 바르게 짝지은 것은?', '비교급·최상급', B(
 'A: Which is <b>(A)</b> [ heavier / heaviest ], a kilo of feathers or a kilo of iron?', 'B: They weigh the same!',
 'A: Who is the <b>(B)</b> [ funnier / funniest ] person in your class?', 'B: Junho. He always makes us laugh.'),
 ['(A)', '(B)'], [['heavier', 'funniest'], ['heaviest', 'funniest'], ['heavier', 'funnier'], ['heaviest', 'funnier'], ['more heavy', 'most funny']],
 "이유 ▶ (A) 두 개 중 '어느 것이 더' → 비교급 heavier (B) the ~ person in your class(반에서) → 최상급 funniest (자음+y → iest)\n오답 ▶ 둘 비교에 heaviest ❌ / 범위(in your class)에 funnier ❌ / more heavy·most funny ❌\n포인트 ▶ A or B(둘) → 비교급 / in ~(범위) → 최상급", [])
T.flex('다음 글을 읽고, 가장 무거운 것과 가장 가벼운 것을 차례대로 고르면?', E_, B('Box A is heavier than Box B. Box C is lighter than Box B. Box D is heavier than Box A.'),
 ['D – C', 'A – C', 'D – B', 'A – B', 'C – D'],
 "이유 ▶ D > A > B > C (무거운 순). 가장 무거운 것 D, 가장 가벼운 것 C.\n포인트 ▶ heavier(>) / lighter(<)를 부등호로 바꿔 줄 세우기", [])
T.flex('다음 문장을 의문문으로 바르게 바꾼 것은?', '본문 응용', B('There were four eyewitnesses.'),
 ['Were there four eyewitnesses?', 'Was there four eyewitnesses?', 'Did there were four eyewitnesses?', 'Are there four eyewitnesses?', 'There were four eyewitnesses are?'],
 "이유 ▶ There is/are 의문문 = be동사 + there + 주어 ~? 과거 + 복수 → Were there ~?\n오답 ▶ {1} 복수(eyewitnesses) → were {2} be동사 문장에 did ❌ {3} 시제가 현재로 바뀜 {4} 형태 오류\n포인트 ▶ There were ~. → Were there ~?", [])
T.render()

# ═══════════════ 3차 (최상) ═══════════════
T = Test('3', '3차', '비교급 · 최상급 · There is/are', '5과 문법',
 '범위: 5과 문법 — 비교급 · 최상급 · There is/are. 가장 어려운 단계예요. 개수·짝 고르기 문제는 문장 하나하나 ⭕ / ❌ 를 표시하며 풀어 보세요.', H=H)
T.fixed('다음 <보기>에서 어법상 <u>어색한</u> 문장의 개수는?', '종합', B(
 '(a) He is the most diligent student in his school.', '(b) My brother eats less than I do.', '(c) There is two bakeries on this street.',
 '(d) This test was very easier than I expected.', '(e) Which is the longest, a pen, a pencil, or a ruler?', '(f) Her cookies taste more sweeter than mine.'),
 NUMS, 3,
 "이유 ▶ 어색한 것 (c)·(d)·(f) 3개. (c) two bakeries → There are (d) very는 비교급을 못 꾸밈 → much easier (f) more + -er 중복 → sweeter\n오답 ▶ (a) diligent(3음절) → the most diligent ✔ (b) little – less(덜 먹는다) ✔ (e) 셋 중 → 최상급 ✔\n포인트 ▶ 감각동사(taste) + 형용사 비교급도 more 중복 주의", [])
T.fixed('다음 중 어법상 올바른 문장끼리 바르게 짝지은 것은?', '종합', B(
 'ⓐ Is there a library near your house?', 'ⓑ Today is the hottest day of the year.', 'ⓒ There are much sugar in this tea.', 'ⓓ Jane is more creative than her sister.', 'ⓔ He is the most strongest man in town.'),
 ['ⓐ, ⓑ', 'ⓐ, ⓒ', 'ⓑ, ⓓ, ⓔ', 'ⓐ, ⓑ, ⓓ', 'ⓒ, ⓔ'], 4,
 "이유 ▶ 올바른 것 ⓐ·ⓑ·ⓓ.\n오답 ▶ ⓒ sugar(셀 수 없음, much) → There is ⓔ most + -est 중복 → the strongest\n포인트 ▶ ①은 ⓓ가 빠진 함정 — 올바른 것을 '모두' 담은 선택지를 골라야 해요.", [])
T.flex('다음 중 두 문장의 의미가 서로 <u>다른</u> 것은?', '비교급·최상급', '',
 ['Sam is older than Kate. = Kate is not as young as Sam.', 'Tom is taller than Bill. = Bill is shorter than Tom.', 'No mountain in South Korea is higher than Hallasan. = Hallasan is the highest mountain in South Korea.',
  'This bag is cheaper than that one. = That bag is more expensive than this one.', 'Mina is the best singer in her class. = Mina sings best in her class.'],
 "이유 ▶ Sam이 Kate보다 나이가 많다 = Kate는 Sam보다 어리다. 그런데 'Kate is not as young as Sam'은 'Kate는 Sam만큼 어리지 않다(= Kate가 더 나이 많다)'라서 반대!\n오답 ▶ {1} taller ↔ shorter ✔ {2} No ~ 비교급 than = 최상급 ✔ {3} cheaper ↔ more expensive ✔ {4} best singer = sings best ✔\n포인트 ▶ not as ~ as는 '앞사람이 덜 ~하다'", [])
T.table('다음 빈칸 (A)~(C)에 들어갈 말이 순서대로 바르게 연결된 것은?', '종합', B(
 '• There ' + BL + '(A) a lot of homework today.', '• ' + BL + '(B) there any eggs in the basket?', '• My new phone is ' + BL + '(C) than my old one.'),
 ['(A)', '(B)', '(C)'], [['is', 'Are', 'much lighter'], ['are', 'Are', 'much lighter'], ['is', 'Is', 'much lighter'], ['is', 'Are', 'very lighter'], ['are', 'Is', 'more lighter']],
 "이유 ▶ (A) homework는 셀 수 없음 → is (B) eggs(복수) → Are there (C) much + 비교급\n오답 ▶ a lot of만 보고 are ❌ / 복수 eggs인데 Is ❌ / very lighter·more lighter ❌\n포인트 ▶ homework, information, advice, news → 셀 수 없음", [])
T.flex('다음 중 어법상 올바른 문장은?', A_, '',
 ['Of the three sisters, Amy is the most talkative.', 'Bora is the youngest of my class.', 'There is lots of mistakes in your essay.', 'My score was more worse than I had expected.', 'Which season do you like most best?'],
 "이유 ▶ Of the three sisters(세 자매 중에서) + talkative(3음절) → the most talkative ✔\n오답 ▶ {1} 범위(반) → in my class {2} mistakes(복수) → There are {3} more 중복 → worse {4} most와 best 중복 → best\n포인트 ▶ of + 복수 비교 대상 / in + 범위(class, family, team)", [])
T.fixed('다음 밑줄 친 there의 쓰임이 나머지 넷과 <u>다른</u> 것은?', T_, B(
 '① <u>There</u> is a bank on the corner.', '② <u>There</u> are many stars tonight.', "③ I'll meet you <u>there</u> at six.", '④ <u>There</u> was a big storm last night.', '⑤ Is <u>there</u> any milk left?'),
 None, 3,
 "이유 ▶ ③의 there는 '거기에서'라는 장소 부사. 나머지는 '~가 있다'의 There is/are 구문(there를 해석하지 않음).\n포인트 ▶ There is/are의 there는 '거기'로 해석하지 않는다!", [])
T.flex('다음 표의 내용과 일치하는 것은?', '비교급·최상급', B('건물 높이 — Building A: 320 m · Building B: 450 m · Building C: 280 m · Building D: 390 m'),
 ['Building D is taller than Building A but shorter than Building B.', 'Building C is the second tallest of the four.', 'Building A is taller than Building D.',
  'Building B is not as tall as Building D.', 'Building A is the shortest of the four.'],
 "이유 ▶ D(390) > A(320), D(390) < B(450) ✔\n오답 ▶ {1} C(280)는 가장 낮음 {2} A 320 < D 390 {3} B가 더 높음 {4} 가장 낮은 건 C\n포인트 ▶ 순서: B 450 > D 390 > A 320 > C 280", [])
T.flex('다음 우리말을 영어로 바르게 옮긴 것은?', A_, B('이 모자가 이 가게에서 가장 저렴한 물건이다.'),
 ['This cap is the cheapest item in this store.', 'This cap is cheapest item in this store.', 'This cap is the most cheap item in this store.', 'This cap is cheaper item in this store.', 'This cap is the cheapest items in this store.'],
 "이유 ▶ the + cheapest(1음절 -est) + 단수 item + in this store(범위)\n오답 ▶ {1} the 빠짐 {2} most cheap ❌ {3} 비교급 ❌ {4} 주어 This cap(하나) → item\n포인트 ▶ 명사 앞 최상급에는 반드시 the", [])
T.flex('다음 중 짝지어진 대화가 <u>어색한</u> 것은?', T_, '',
 ['A: Are there any cookies left? — B: Yes, there is.', "A: Is there a bus stop near here? — B: No, there isn't.", 'A: Who is taller, you or your brother? — B: My brother is.',
  "A: Which is the most popular sport in Korea? — B: I think it's baseball.", 'A: Was there a test yesterday? — B: Yes, there was.'],
 "이유 ▶ Are there any cookies(복수)? → Yes, there are.\n오답 ▶ {1} Is there ~? → No, there isn't ✔ {2} 둘 중 → 비교급, My brother is ✔ {3} 최상급 질문 ✔ {4} Was there ~? → Yes, there was ✔\n포인트 ▶ 대답의 be동사는 질문과 같은 수·시제", [])
T.flex('5과 본문의 단서로 찾은 범인(Larry Johnson)에 대한 설명으로 알맞지 <u>않은</u> 것은?', '본문 응용', B(
 'Andres Lozano | 176 cm | long, black hair | Spanish, English | brown eyes', 'Larry Johnson | 173 cm | long, brown hair | English | blue eyes',
 'Tim Baker | 182 cm | long, brown hair | English | green eyes', 'Luca Ferez | 166 cm | short, gray hair | Spanish | blue eyes',
 '(Ann: I\'m about 170 cm tall, and he was a little taller than me.)'),
 ['He speaks more languages than Andres.', 'He is taller than Ann but shorter than Andres.', 'He is the only suspect with long brown hair and blue eyes.', 'He is shorter than Tim.', 'He is taller than Luca.'],
 "이유 ▶ Larry는 영어 한 개, Andres는 스페인어·영어 두 개 → Larry가 '더 적은' 언어를 한다.\n오답 ▶ {1} 약 170 < 173 < 176 ✔ {2} 긴 갈색 머리 + 파란 눈은 Larry뿐(Tim은 초록 눈, Luca는 짧은 회색 머리) ✔ {3} 173 < 182 ✔ {4} 173 > 166 ✔\n포인트 ▶ more + 명사(languages) = 더 많은 ~", [])
T.fixed('다음 글의 밑줄 친 부분 중, 어법상 <u>어색한</u> 것은?', '종합', B(
 'Last weekend, my family went to the zoo. There ' + CN(1, 'were') + ' lots of animals. The giraffe was ' + CN(2, 'taller') + ' than the elephant, but the elephant was ' + CN(3, 'heavier') +
 '. The monkeys were ' + CN(4, 'the noisiest') + ' of all the animals. My little brother said the lion was ' + CN(5, 'more scarier') + ' than the tiger.'),
 ['were', 'taller', 'heavier', 'the noisiest', 'more scarier'], 5,
 "이유 ▶ scary – scarier: more와 -er 중복 → scarier.\n오답 ▶ ① lots of animals(복수) → were ✔ ② tall – taller ✔ ③ heavy – heavier ✔ ④ noisy – the noisiest + of all ✔\n포인트 ▶ 자음 + y → -ier / -iest (heavy, noisy, scary)", [])
T.flex('다음 중 어법상 <u>어색한</u> 문장은?', E_, '',
 ['My hair is longer than you.', 'His car is faster than mine.', "Her voice is softer than her mother's.", 'This room is brighter than that one.', 'Your idea is better than his.'],
 "이유 ▶ 비교 대상은 같은 종류끼리: 내 머리 vs '너의 머리' → than yours (you ❌).\n오답 ▶ {1} mine = my car ✔ {2} her mother's (voice) ✔ {3} that one = that room ✔ {4} his = his idea ✔\n포인트 ▶ than 뒤에 소유대명사(mine, yours, his)를 써야 하는 문장을 찾기!", [])
T.flex('다음 문장과 의미가 같은 것은?', A_, B('Nothing is more important than health.'),
 ['Health is the most important thing.', 'Health is less important than everything.', 'Some things are more important than health.', 'Health is not as important as other things.', 'Health is the least important thing.'],
 "이유 ▶ 건강보다 더 중요한 것은 없다 = 건강이 가장 중요하다.\n오답 ▶ {1}~{4} 모두 건강이 덜 중요하다는 반대 뜻\n포인트 ▶ Nothing + 비교급 + than A = A is the 최상급", [])
T.flex('다음 문장을 부정문으로 바르게 바꾼 것은?', T_, B('There were some cars on the street.'),
 ["There weren't any cars on the street.", "There wasn't any cars on the street.", "There weren't some cars on the street.", "There didn't be any cars on the street.", "There were not any car on the street."],
 "이유 ▶ be동사 뒤에 not + some → any. 복수(cars)·과거 → weren't any cars.\n오답 ▶ {1} 복수인데 wasn't {2} 부정문에 some ❌ {3} be동사 부정에 didn't ❌ {4} any + 셀 수 있는 명사는 복수 cars\n포인트 ▶ some(긍정) → any(부정·의문)", [])
T.flex('다음 빈칸에 들어갈 말로 알맞은 것은?', E_, B('Your phone is not as new ' + BL + ' mine.'),
 ['as', 'than', 'so', 'like', 'of'],
 "이유 ▶ not as + 원급 + as = ~만큼 …하지 않은.\n오답 ▶ {1} than은 비교급(newer)과 함께 {2} not so ~ as는 가능하지만 뒤는 as {3}·{4} 쓰지 않음\n포인트 ▶ as ~ as / not as[so] ~ as 짝 맞추기", [])
T.flex('다음 빈칸에 들어갈 말로 알맞은 것은?', E_, B('I have ' + BL + ' free time than my brother because I go to an academy every day.'),
 ['less', 'fewer', 'little', 'least', 'much'],
 "이유 ▶ 학원에 매일 가서 형보다 자유 시간이 '더 적다' + than → 비교급. time은 셀 수 없음 → little – less.\n오답 ▶ {1} fewer는 셀 수 있는 명사(fewer books) {2} 원급 {3} 최상급 {4} much는 '더 많은' 뜻도 아니고 원급\n포인트 ▶ 셀 수 없는 명사의 '더 적은' = less", [])
T.flex('다음 중 어법상 올바른 문장은?', '종합', '',
 ['Today I feel much better than yesterday.', 'There is much more apples in this basket.', 'This is the most hottest summer ever.', 'Is there any good restaurants near here?', 'She can dance more well than me.'],
 "이유 ▶ feel + 형용사(good → better), much로 비교급 강조 ✔\n오답 ▶ {1} apples(복수) → There are {2} most + -est 중복 → the hottest {3} restaurants(복수) → Are there {4} well – better → dance better\n포인트 ▶ well의 비교급은 better (more well ❌)", [])
T.flex('다음은 한 카페의 메뉴판이다. 내용과 일치하지 <u>않는</u> 것은?', T_, B('Cakes: chocolate · cheese · carrot　|　Cookies: SOLD OUT　|　Juice: apple · orange'),
 ['There are some cookies in the café.', 'There are three kinds of cakes.', "There aren't any cookies now.", 'There is apple juice on the menu.', 'There are two kinds of juice.'],
 "이유 ▶ 쿠키는 다 팔렸다(SOLD OUT) → There aren't any cookies.\n오답 ▶ {1} 케이크 3종류 ✔ {2} 쿠키 없음 ✔ {3} 사과 주스 ✔ {4} 주스 2종류 ✔", [])
T.flex('다음 글의 내용과 일치하는 것은?', E_, B('Jin is heavier than Ken but lighter than Leo. Max is lighter than Ken.'),
 ['Ken is the second lightest of the four.', 'Max is heavier than Jin.', 'Jin is the heaviest of the four.', 'Leo is lighter than Ken.', 'Ken is heavier than Jin.'],
 "이유 ▶ 무거운 순: Leo > Jin > Ken > Max → Ken은 두 번째로 가벼움 ✔\n오답 ▶ {1} Max가 가장 가벼움 {2} Leo가 가장 무거움 {3} Leo > Ken {4} Jin > Ken\n포인트 ▶ but(~지만) 앞뒤로 두 사람과 각각 비교한 문장 → 가운데 자리", [])
T.table('5과 본문 내용을 바탕으로, (A)~(C)의 각 네모 안에서 알맞은 것을 바르게 짝지은 것은?', '본문 응용', B(
 'Carlos ran after the man, but the man was <b>(A)</b> [ fast / faster ] than Carlos. There <b>(B)</b> [ was / were ] a cake box next to the wheelchair. Camila\'s Bakery had a lot of different cakes, but the man bought the <b>(C)</b> [ smaller / smallest ] one.'),
 ['(A)', '(B)', '(C)'], [['faster', 'was', 'smallest'], ['fast', 'was', 'smallest'], ['faster', 'were', 'smallest'], ['faster', 'was', 'smaller'], ['fast', 'were', 'smaller']],
 "이유 ▶ (A) than → 비교급 faster (B) a cake box(단수) → was (C) 많은 케이크 중 '가장' 작은 것 → the smallest\n오답 ▶ 원급 fast + than ❌ / 단수인데 were ❌ / 여러 개 중에서는 최상급(smaller ❌)\n포인트 ▶ 둘 중 → 비교급, 셋 이상 중 → 최상급", [])
T.render()
