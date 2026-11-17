# 11/17 중산중1 동아(윤정미) 실전 문법 — to부정사 1·2·3차 (각 20문항)
# 원본: 선생님 학습지 To____1.hwp · To____1-1.hwp · To____2.hwp 에서 범위만 골라 씀
# 범위: 명사적 용법(주어·목적어·보어, 의문사+to부정사 제외) + 부사적 용법(목적 = 중심 / 감정의 원인·판단의 근거·결과·형용사 수식 = 가려내기용)
# 범위 밖이라 뺀 것: 형용사적 용법, be to 용법, 의문사+to, 5형식 목적격보어, 의미상 주어 for/of
import sys; sys.path.insert(0, '/home/claude/srcrepo/wrapup')
from wu_m1to import *
H = ('실전 문법', '중1 영어 동아(윤정미) to부정사', '동아(윤정미) to부정사', 'm1to')
B = lambda *ls: BOX('<br>'.join(ls))
NUMS = ['1개', '2개', '3개', '4개', '5개']
t = lambda x: x.replace('[', '<u>').replace(']', '</u>')
N_, P_, K_, A_ = '명사적 용법', '부사적 · 목적', '쓰임 구별', '부사적 · 가려내기'
NOTE = '범위: to부정사 명사적 용법(주어 · 목적어 · 보어) + 부사적 용법(목적 ~하기 위해서). 감정의 원인 · 판단의 근거 · 결과 · 형용사 수식은 목적과 구별하는 문제로 나와요.'

# ═══════════════ 1차 (기본) ═══════════════
T = Test('1', '1차', 'to부정사 명사적 · 부사적 용법', 'to부정사', NOTE, H=H)
T.flex('다음 빈칸에 들어갈 말로 알맞은 것은?', N_, B('Sejin ' + BL + ' take pictures.'),
 ['likes to', 'is', 'will be', "won't be", 'likes'],
 "이유 ▶ take(동사원형)가 이어지므로 likes to + 동사원형 → 사진 찍는 것을 좋아한다.\n오답 ▶ {1}·{2}·{3} be동사 뒤에 동사원형 take ❌ {4} likes 뒤에 동사원형 바로 ❌\n포인트 ▶ 동사 + to + 동사원형 = ~하는 것을 (목적어)", [])
T.flex('다음 빈칸에 공통으로 들어갈 말로 알맞은 것은?', N_, B('• I want ' + BL + ' buy a new jacket.', '• I hope ' + BL + ' be a doctor.'),
 ['to', 'for', 'in', 'by', 'at'],
 "이유 ▶ want / hope + to + 동사원형(buy / be) → 목적어 역할.\n오답 ▶ {1}~{4} 전치사 뒤에는 동사원형이 올 수 없음\n포인트 ▶ want · hope · plan · decide · wish + to부정사", [])
T.flex('다음 중 어법상 올바른 것은?', N_, '',
 ['I want to watch TV.', 'I want to watches TV.', 'I want watch TV.', 'I want to watching TV.', 'I want watching TV.'],
 "이유 ▶ want + to + 동사원형(watch).\n오답 ▶ {1} to 뒤에 -es ❌ {2} to 빠짐 {3} to 뒤에 -ing ❌ {4} want는 동명사를 목적어로 쓰지 않음\n포인트 ▶ to 뒤는 언제나 동사원형", [])
T.flex('다음 빈칸에 들어갈 말로 알맞은 것은?', N_, B('My dream is ' + BL + ' a scientist.'),
 ['to be', 'to is', 'is', 'be to', 'to being'],
 "이유 ▶ My dream is + to be a scientist(보어) = 내 꿈은 과학자가 되는 것이다.\n오답 ▶ {1}·{4} to 뒤는 동사원형 be {2} is가 두 번 {3} 어순 ❌\n포인트 ▶ 주어 + be동사 + to부정사 = ~하는 것이다 (보어)", [])
T.flex('다음 빈칸에 들어갈 말로 알맞은 것은?', N_, B(BL + ' this book is boring.'),
 ['To read', 'Read', 'Reads', 'To reads', 'Do read'],
 "이유 ▶ 문장의 주어 자리 → To read this book(이 책을 읽는 것은).\n오답 ▶ {1}·{2}·{4} 동사로 문장을 시작하면 주어가 없음 {3} to 뒤는 동사원형\n포인트 ▶ To + 동사원형 ~ + is … = ~하는 것은 …하다 (주어)", [])
T.flex('다음 빈칸에 들어갈 말로 알맞은 것은?', P_, B('She turned the music down ' + BL + ' the phone.'),
 ['to answer', 'answer', 'answered', 'be answered', 'have answered'],
 "이유 ▶ 전화를 받기 위해 음악 소리를 줄였다 → 목적 to answer.\n오답 ▶ {1}·{2}·{3}·{4} 이미 동사(turned)가 있어서 동사를 또 쓸 수 없음\n포인트 ▶ 문장 끝 to + 동사원형 = ~하기 위해서 (목적)", [])
T.flex('두 문장을 한 문장으로 바르게 바꾼 것은?', P_, B('Helen wanted to buy some clothes. So she went to the department store.'),
 ['Helen went to the department store to buy some clothes.', 'Helen went to the department store buy some clothes.', 'Helen went to the department store to bought some clothes.', 'Helen went to the department store for buy some clothes.', 'Helen wanted to the department store to buy some clothes.'],
 "이유 ▶ 옷을 사려고 백화점에 갔다 → went to ~ + to buy(목적).\n오답 ▶ {1} to 빠짐 {2} to 뒤는 동사원형 {3} for + 동사원형 ❌ {4} 동사 went가 빠져 뜻이 깨짐\n포인트 ▶ '하고 싶어서 → 했다' = 동사 + to부정사(목적)", [])
T.flex('다음 문장과 의미가 같은 것은?', P_, B('I took the first train in order to arrive early.'),
 ['I took the first train so as to arrive early.', 'I took the first train so to arrive early.', 'I took the first train in order arrive early.', 'I took the first train as to arrive early.', 'I took the first train in order for arrive early.'],
 "이유 ▶ in order to = so as to = ~하기 위해서.\n오답 ▶ {1} so as to에서 as 빠짐 {2} in order 뒤 to 빠짐 {3} so 빠짐 {4} for ❌\n포인트 ▶ 목적 = to V = in order to V = so as to V", [])
T.flex('다음 밑줄 친 to부정사의 쓰임이 나머지 넷과 <u>다른</u> 것은?', K_, '',
 [t('[To be] honest is very important.'), t('She studied hard [to be] a lawyer.'), t('Joe exercises every day [to lose] weight.'), t('He came here [to say] goodbye to us.'), t('We got up early [to catch] the first train.')],
 "이유 ▶ To be honest가 문장의 주어(정직한 것은) → 명사적 용법.\n오답 ▶ {1}~{4} 모두 '~하기 위해서'(목적) → 부사적 용법\n포인트 ▶ 문장 맨 앞 To V ~ + 동사 = 주어 / 문장 뒤 to V = 목적인지 확인", [])
T.flex('<보기>의 밑줄 친 부분과 쓰임이 같은 것은?', K_, B(t('<보기> I went to the library [to read] books.')),
 [t('She turned on the light [to read] it.'), t('I planned [to read] a lot of books.'), t('[To read] the book is fun.'), t('He wants [to read] the comic book.'), t('His hobby is [to read] comic books.')],
 "이유 ▶ <보기>와 정답 모두 '읽기 위해서'(목적).\n오답 ▶ {1}·{3} 목적어(~하는 것을) {2} 주어 {4} 보어 → 모두 명사적 용법\n포인트 ▶ '~하기 위해서'로 해석되면 목적", [])
T.flex('다음 밑줄 친 부분의 용법이 나머지 넷과 <u>다른</u> 것은?', K_, '',
 [t('I wanted [to meet] Mr. Kim.'), t('Jiyoung went to America [to study] English.'), t('Mom cleaned the oven [to bake] some cookies.'), t('He studied hard [to pass] the exam.'), t('Minho went to the market [to buy] some ice cream.')],
 "이유 ▶ wanted의 목적어(만나기를) → 명사적 용법.\n오답 ▶ {1}~{4} 모두 목적(~하기 위해서) → 부사적 용법\n포인트 ▶ want · plan · hope 바로 뒤 to V = 목적어", [])
T.flex('<보기>의 밑줄 친 부분과 쓰임이 같은 것은?', K_, B(t('<보기> Our hope is [to become] one country again someday.')),
 [t('His plan is [to take] the night train.'), t('She went to Seoul [to become] an actress.'), t('He studied hard [to win] the prize.'), t('I was glad [to see] you.'), t('This book is easy [to read].')],
 "이유 ▶ <보기>와 정답 모두 be동사 뒤 보어(~하는 것이다) → 명사적 용법.\n오답 ▶ {1}·{2} 목적 {3} 감정의 원인 {4} 형용사 수식 → 모두 부사적 용법\n포인트 ▶ 주어 + is + to V = ~하는 것이다", [])
T.fixed('다음 문장에서 to가 들어갈 위치로 알맞은 두 곳은?', N_, B('My dream is ⓐ become ⓑ a doctor ⓒ because I ⓓ like ⓔ help sick people.'),
 ['ⓐ, ⓒ', 'ⓐ, ⓔ', 'ⓑ, ⓒ', 'ⓑ, ⓔ', 'ⓓ, ⓔ'], 2,
 "이유 ▶ My dream is to become a doctor(보어) / I like to help sick people(목적어) → ⓐ, ⓔ.\n오답 ▶ ⓑ become과 a doctor 사이 ❌ ⓒ because 앞 ❌ ⓓ 주어 I와 like 사이 ❌\n포인트 ▶ is 뒤 · like 뒤에 동사원형이 오면 그 앞에 to", [])
T.flex('다음 중 어법상 틀린 것은?', N_, '',
 ['My dream was to became a teacher.', 'Her hobby is to read books.', 'His role is to give advice to others.', 'Her plan is to take a cooking class.', 'Their goal is to win a gold medal this year.'],
 "이유 ▶ to 뒤는 동사원형 → to become. (과거 was여도 to 뒤는 그대로 원형)\n오답 ▶ {1}~{4} be동사 + to + 동사원형(보어) ✔\n포인트 ▶ 시제는 be동사(was)에만, to 뒤는 늘 원형", [])
T.flex('다음 밑줄 친 to부정사의 쓰임이 나머지 넷과 <u>다른</u> 것은?', K_, '',
 [t('He went out [to take] a walk.'), t('His plan is [to wake] up at 7.'), t('The best choice is [to call] Mom.'), t('My dream is [to become] a singer.'), t('My hope is [to have] my own shop.')],
 "이유 ▶ 산책하기 위해 나갔다 → 목적(부사적 용법).\n오답 ▶ {1}~{4} be동사 뒤 보어(~하는 것이다) → 명사적 용법\n포인트 ▶ 일반동사 문장 끝 to V(목적) vs is 뒤 to V(보어)", [])
T.flex('다음 우리말을 영어로 바르게 옮긴 것은?', N_, B('나는 캠핑 가기를 원한다.'),
 ['I want to go camping.', 'I want go camping.', 'I want to going camping.', 'I want going to camping.', 'I to want go camping.'],
 "이유 ▶ want + to go camping(목적어).\n오답 ▶ {1} to 빠짐 {2} to 뒤 -ing ❌ {3} want + -ing ❌ {4} to 위치 ❌\n포인트 ▶ go camping / go shopping / go swimming → want to go ~", [])
T.flex('다음 우리말을 영어로 바르게 옮긴 것은?', P_, B('그녀는 책을 몇 권 반납하러 도서관에 갔다.'),
 ['She went to the library to return some books.', 'She went to the library return some books.', 'She went to the library to returns some books.', 'She went to the library for return some books.', 'She went to return the library some books.'],
 "이유 ▶ 반납하러(목적) → went to the library + to return some books.\n오답 ▶ {1} to 빠짐 {2} to 뒤는 원형 {3} for + 동사원형 ❌ {4} 어순이 깨져 뜻이 달라짐\n포인트 ▶ ~하러 가다 = go to + 장소 + to V", [])
T.flex('다음 빈칸에 들어갈 말로 알맞지 <u>않은</u> 것은?', N_, B('I ' + BL + ' writing a letter in English.'),
 ['decided', 'enjoyed', 'finished', 'liked', 'gave up'],
 "이유 ▶ decide는 to부정사만 목적어로 → decided to write.\n오답 ▶ {1} enjoy {2} finish {4} give up → 동명사만 {3} like → 둘 다 가능\n포인트 ▶ to부정사만: want · hope · plan · decide · wish / 동명사만: enjoy · finish · give up · mind", [])
T.flex('다음 대화의 빈칸에 들어갈 말로 알맞은 것은?', N_, B('A: What do you want to do right now?', 'B: I want ' + BL + ' fresh orange juice.'),
 ['to drink', 'drink', 'drinking', 'to drinks', 'drank'],
 "이유 ▶ want + to drink(목적어).\n오답 ▶ {1} to 빠짐 {2} want + -ing ❌ {3} to 뒤는 원형 {4} 동사 두 개 ❌\n포인트 ▶ What do you want to do? → I want to + 동사원형", [])
T.flex('<보기>의 밑줄 친 부분과 쓰임이 같은 것은?', K_, B(t('<보기> He worked hard [to succeed].')),
 [t('David practiced so hard [to win] the game.'), t("I'm sorry [to hear] the news."), t('[To study] English is interesting.'), t('I would like [to dance] with my dad.'), t('The boy grew up [to be] a scholar.')],
 "이유 ▶ <보기>와 정답 모두 '~하기 위해서'(목적).\n오답 ▶ {1} 감정의 원인(듣게 되어 유감) {2} 주어 {3} 목적어 {4} 결과(자라서 학자가 되었다)\n포인트 ▶ 감정 형용사(sorry, happy) 뒤 to V = 감정의 원인", [])
T.render()

# ═══════════════ 2차 (중상) ═══════════════
T = Test('2', '2차', 'to부정사 명사적 · 부사적 용법', 'to부정사', NOTE, H=H)
T.flex('<보기>의 밑줄 친 부분과 용법이 같은 것은?', A_, B(t('<보기> My grandfather lived [to be] one hundred years old.')),
 [t('The boy grew up [to be] a great scholar.'), t('He must be crazy [to do] such a thing.'), t('He worked hard [to succeed].'), t("I'm glad [to see] you again."), t('Harry decided [to move] to New York.')],
 "이유 ▶ <보기>와 정답 모두 '~해서 (결국) …하다'(결과): 살아서 100살이 되었다 / 자라서 학자가 되었다.\n오답 ▶ {1} 판단의 근거 {2} 목적 {3} 감정의 원인 {4} 목적어(명사적)\n포인트 ▶ live · grow up · wake up + to V = 결과", [])
T.flex('<보기>의 밑줄 친 부분과 쓰임이 <u>다른</u> 것은?', K_, B(t('<보기> He came to my office [to say] hello to me.')),
 [t('We are planning [to travel] to Fiji.'), t('He called her [to ask] for help.'), t('Isabella saves money [to buy] a house.'), t('John went to Tokyo [to learn] Japanese.'), t('She boiled water [to make] hot chocolate.')],
 "이유 ▶ planning의 목적어(여행하는 것을) → 명사적 용법.\n오답 ▶ {1}~{4} 모두 목적(~하기 위해서)\n포인트 ▶ plan / want / decide 뒤 to V = 목적어", [])
T.flex('다음 문장과 의미가 가장 가까운 것은?', P_, B('Because Joe wanted to become a painter, he took more art classes.'),
 ['Joe took more art classes to become a painter.', 'Joe took more art classes, so he became a painter.', 'Joe wanted to become a painter to take more art classes.', 'After Joe took more art classes, he became a painter.', 'When Joe took more art classes, he became a painter.'],
 "이유 ▶ 화가가 되고 싶어서(목적) 미술 수업을 더 들었다 → took more art classes to become a painter.\n오답 ▶ {1}·{3}·{4} 실제로 화가가 '되었다'(결과)는 뜻 {2} 수업을 듣기 위해 화가가 되고 싶었다(거꾸로)\n포인트 ▶ 목적은 '바라는 일', 결과는 '실제로 일어난 일'", [])
T.flex('다음 중 어법상 <u>어색한</u> 문장은?', A_, '',
 ["I'll be very happy to helping others.", 'Tom washed the dishes to help his mother.', 'Emma reads English novels to learn new words.', 'I was surprised to hear about his decision.', 'She went to the library to return some books.'],
 "이유 ▶ to 뒤는 동사원형 → happy to help.\n오답 ▶ {1}·{2}·{4} 목적 ✔ {3} 감정의 원인 ✔\n포인트 ▶ 어떤 용법이든 to + 동사원형", [])
T.flex('우리말과 같도록 할 때 빈칸에 들어갈 말로 알맞은 것은?', A_, B('This class is hard ' + BL + '.', '(이 수업은 따라가기에 어렵다.)'),
 ['to catch up with', 'catch up with', 'to catching up with', 'catching to up with', 'for catch up with'],
 "이유 ▶ 형용사 hard를 꾸미는 to부정사 → ~하기에 어렵다.\n오답 ▶ {1} to 빠짐 {2} to 뒤는 원형 {3} 어순 ❌ {4} for + 동사원형 ❌\n포인트 ▶ easy · hard · difficult + to V = ~하기에 (형용사 수식)", [])
T.flex('다음 우리말을 영어로 바르게 옮긴 것은?', A_, B('호랑이들을 훈련시키다니 그는 용감한 게 틀림없다.'),
 ['He must be brave to train tigers.', 'He must be brave train tigers.', 'He must brave to train tigers.', 'He must be brave to trains tigers.', 'He must be brave training to tigers.'],
 "이유 ▶ must be + 형용사 + to V = ~하다니 …임에 틀림없다(판단의 근거).\n오답 ▶ {1} to 빠짐 {2} must 뒤 be 빠짐 {3} to 뒤는 원형 {4} 어순 ❌\n포인트 ▶ must be ~ to V = 판단의 근거", [])
T.flex('다음 우리말을 영어로 바르게 옮긴 것은?', A_, B('나는 그 개구리가 살아 있는 것을 발견하고 기뻤다.'),
 ['I was delighted to find the frog alive.', 'I was delighted find the frog alive.', 'I was delighted to find alive the frog.', 'I delighted to find the frog alive.', 'I was delighted to finding the frog alive.'],
 "이유 ▶ was delighted + to find(감정의 원인) + the frog alive.\n오답 ▶ {1} to 빠짐 {2} find + 목적어(the frog) + alive 순서 {3} be동사 was 빠짐 {4} to 뒤는 원형\n포인트 ▶ 감정 형용사 + to V = ~해서 (기쁘다 / 슬프다 / 놀라다)", [])
T.flex('다음 중 어법상 <u>어색한</u> 것은?', P_, '',
 ['I pressed the button so to roll down the window.', 'I pressed the button to roll down the window.', 'I pressed the button in order to roll down the window.', 'I pressed the button so as to roll down the window.', 'I pressed the button so that I could roll down the window.'],
 "이유 ▶ so to ❌ → so as to.\n오답 ▶ {1} to V {2} in order to V {3} so as to V {4} so that 주어 can[could] V → 모두 목적 ✔\n포인트 ▶ 목적 = to V = in order to V = so as to V = so that ~ can", [])
T.flex('다음 중 빈칸에 to를 쓸 수 <u>없는</u> 것은?', N_, '',
 ["All the students " + BL + " know what we're having for lunch.", 'The difficult thing is ' + BL + ' lift this desk.', 'Her wish is ' + BL + ' see him one last time.', 'One thing we can do is ' + BL + ' open the window.', 'His final decision is ' + BL + ' leave in the morning.'],
 "이유 ▶ All the students(주어) + know(동사) → 동사 자리라 to ❌.\n오답 ▶ {1}~{4} is 뒤 보어 → to + 동사원형 ✔\n포인트 ▶ 주어 바로 뒤 동사 자리에는 to를 쓰지 않는다", [])
T.flex('다음 밑줄 친 to부정사의 역할이 바르게 연결된 것은?', N_, '',
 [t("It's important [to keep] the air clean. → 진주어"), t('My hobby is [to sing]. → 목적어'), t('He hopes [to pass] the test. → 보어'), t('[To ride] a bike is fun. → 보어'), t('I want [to travel] to Spain. → 주어')],
 "이유 ▶ It(가주어) ~ to keep the air clean(진주어) ✔\n오답 ▶ {1} is 뒤 → 보어 {2} hopes의 목적어 {3} 문장의 주어 {4} want의 목적어\n포인트 ▶ It is + 형용사 + to V = to V가 진짜 주어", [], en=False)
T.flex('다음 밑줄 친 부분의 용법이 나머지 넷과 <u>다른</u> 것은?', K_, '',
 [t('He visited the museum [to see] the paintings.'), t('[To see] is to believe.'), t('It is easy [to learn] chess.'), t('Kevin planned [to see] the musical.'), t('My wish is [to have] my own house.')],
 "이유 ▶ 그림을 보기 위해 방문했다 → 목적(부사적).\n오답 ▶ {1} 주어 {2} 진주어 {3} 목적어 {4} 보어 → 모두 명사적\n포인트 ▶ 명사적 = '~하는 것' / 부사적(목적) = '~하기 위해서'", [])
T.flex('다음 빈칸에 공통으로 들어갈 말로 알맞은 것은?', N_, B('• I like ' + BL + ' cook.', '• She forgot ' + BL + ' bring her notebook.'),
 ['to', 'of', 'not', 'will', 'with'],
 "이유 ▶ like / forget + to + 동사원형(cook / bring).\n오답 ▶ {1}·{4} 전치사 뒤 동사원형 ❌ {2} I like not cook ❌ {3} 동사 + will ❌\n포인트 ▶ forget to V = ~할 것을 잊다", [])
T.flex('다음 빈칸에 들어갈 말로 알맞은 것은?', N_, B('My plan ' + BL + ' to cook spaghetti.'),
 ['is', 'will', 'like', 'want', 'hope'],
 "이유 ▶ 주어 My plan + is + to cook(보어) = 내 계획은 스파게티를 요리하는 것이다.\n오답 ▶ {1} will 뒤에는 동사원형 {2}·{3}·{4} 주어 My plan(사물)과 뜻이 맞지 않고 3인칭 단수 -s도 없음\n포인트 ▶ My plan / dream / hobby is to V", [])
T.flex('다음 중 어법상 옳은 문장은?', N_, '',
 ['I hope to buy that blue backpack.', 'My hobby is collect coins.', 'His dream is to becomes an actor.', 'Jane wants be a teacher.', 'What do you plan doing tomorrow?'],
 "이유 ▶ hope + to buy ✔\n오답 ▶ {1} is to collect {2} to become {3} wants to be {4} plan to do\n포인트 ▶ is 뒤 보어 · 동사 뒤 목적어 모두 to + 원형", [])
T.fixed('다음 대화에서 어법상 고쳐야 할 부분끼리 바르게 짝지은 것은?', N_, B('B: Jessica, are you interested in movies?', 'G: No, I ⓐam interested in Korean food. I ⓑwant ⓒbeing a cook and ⓓworking in Korea ⓔin the future.'),
 ['ⓐ, ⓑ', 'ⓑ, ⓒ', 'ⓒ, ⓓ', 'ⓓ, ⓔ', 'ⓐ, ⓔ'], 3,
 "이유 ▶ want는 to부정사를 목적어로 → ⓒ to be, ⓓ (to) work.\n오답 ▶ ⓐ be interested in ✔ ⓑ want ✔ ⓔ in the future ✔\n포인트 ▶ want to A and (to) B — and 뒤도 같은 모양", [])
T.flex('두 문장의 뜻이 같도록 할 때 빈칸에 들어갈 수 <u>없는</u> 것은?', N_, B('David ' + BL + ' to learn a foreign language.', '= David ' + BL + ' learning a foreign language.'),
 ['hopes', 'loves', 'likes', 'hates', 'starts'],
 "이유 ▶ hope는 to부정사만 목적어로 → hopes learning ❌.\n오답 ▶ {1} love {2} like {3} hate {4} start → to부정사 · 동명사 둘 다 가능, 뜻도 같음\n포인트 ▶ 둘 다 OK: like · love · hate · start · begin · continue", [])
T.flex('다음 빈칸에 들어갈 수 있는 것은?', N_, B('I ' + BL + ' to listen to music.'),
 ['want', 'will', 'enjoy', 'am going to', 'can'],
 "이유 ▶ want + to listen ✔\n오답 ▶ {1}·{4} 조동사 뒤엔 to 없이 원형 {2} enjoy + listening {3} am going to + to listen → to 중복\n포인트 ▶ will / can / be going to + 동사원형", [])
T.flex('두 문장을 한 문장으로 바르게 바꾼 것은?', A_, B('I was surprised. I heard about his decision.'),
 ['I was surprised to hear about his decision.', 'I was surprised hear about his decision.', 'I was surprised to heard about his decision.', 'I surprised to hear about his decision.', 'I was surprising to hear about his decision.'],
 "이유 ▶ 그 결정을 듣고 놀랐다 → was surprised + to hear(감정의 원인).\n오답 ▶ {1} to 빠짐 {2} to 뒤는 원형 {3} be동사 빠짐 {4} 내가 '놀란' 것 → surprised\n포인트 ▶ was surprised[happy, sad] to V = ~해서 놀랐다[기뻤다, 슬펐다]", [])
T.flex('<보기>의 밑줄 친 부분과 쓰임이 같은 것은?', A_, B(t('<보기> I must be foolish [to make] the same mistake.')),
 [t('She must be smart [to solve] the puzzle so fast.'), t('We were sad [to hear] the bad news.'), t('This software is easy [to use].'), t('He went to the store [to buy] milk.'), t('The boy grew up [to be] a doctor.')],
 "이유 ▶ <보기>와 정답 모두 '~하다니'(판단의 근거): 그렇게 빨리 풀다니 똑똑한 게 틀림없다.\n오답 ▶ {1} 감정의 원인 {2} 형용사 수식 {3} 목적 {4} 결과\n포인트 ▶ must be + 성격 형용사 + to V = 판단의 근거", [])
T.flex("밑줄 친 to부정사가 '~하기 위해서'의 뜻으로 쓰인 것은?", K_, '',
 [t('I turned on the TV [to watch] the news.'), t('I was happy [to win] the game.'), t('She grew up [to be] a pianist.'), t('This river is dangerous [to swim] in.'), t('He must be rich [to buy] that car.')],
 "이유 ▶ 뉴스를 보기 위해 TV를 켰다 → 목적.\n오답 ▶ {1} 감정의 원인(이겨서 기뻤다) {2} 결과(자라서 ~가 되었다) {3} 형용사 수식(수영하기에 위험한) {4} 판단의 근거(사다니 부자임에 틀림없다)\n포인트 ▶ 앞에 감정 형용사 · must be · grow up · easy/hard가 있는지 먼저 본다", [])
T.render()

# ═══════════════ 3차 (상) ═══════════════
T = Test('3', '3차', 'to부정사 명사적 · 부사적 용법', 'to부정사', NOTE, H=H)
T.table('(A)~(C)의 각 네모 안에서 어법에 맞는 표현을 바르게 짝지은 것은?', '종합', B(
 '• My hobby is <b>(A)</b> [ to collect / collect ] old coins.', '• She went to the bakery <b>(B)</b> [ to buy / buys ] some bread.', '• We decided <b>(C)</b> [ to take / taking ] a taxi.'),
 ['(A)', '(B)', '(C)'], [['to collect', 'to buy', 'to take'], ['collect', 'to buy', 'to take'], ['to collect', 'buys', 'to take'], ['to collect', 'to buy', 'taking'], ['collect', 'buys', 'taking']],
 "이유 ▶ (A) is 뒤 보어 → to collect (B) 빵을 사러(목적) → to buy (C) decide는 to부정사만 → to take\n오답 ▶ is 뒤에 동사원형 collect ❌ / 동사 went가 있는데 buys ❌ / decided taking ❌\n포인트 ▶ 보어 · 목적 · 목적어 자리 모두 to + 동사원형", [])
T.fixed('다음 <보기>에서 어법상 <u>어색한</u> 문장의 개수는?', N_, B(
 '(a) We enjoyed to watch the full moon.', '(b) Tom wants to go there.', '(c) It began to snow at night.', '(d) He gave up to smoke.', '(e) Jim expected to stay in New York.'),
 NUMS, 2,
 "이유 ▶ 어색한 것 (a)·(d) 2개.\n오답 ▶ (a) enjoy + 동명사 → watching (d) give up + 동명사 → smoking / (b) want ✔ (c) begin은 둘 다 가능 ✔ (e) expect + to V ✔\n포인트 ▶ enjoy · finish · give up + -ing", [])
T.fixed('다음 밑줄 친 to부정사 중 쓰임이 같은 것끼리 바르게 짝지은 것은?', K_, B(
 t('(a) I went to the park [to walk] my dog.'), t('(b) [To walk] in the morning is good.'), t('(c) She was pleased [to get] the letter.'), t('(d) He saved money [to buy] a bike.'), t('(e) My plan is [to walk] to school.')),
 ['(a), (b)', '(b), (c)', '(a), (d)', '(c), (e)', '(b), (d)'], 3,
 "이유 ▶ (a) 개를 산책시키려고 (d) 자전거를 사려고 → 둘 다 목적.\n오답 ▶ (b) 주어 (c) 감정의 원인 (e) 보어\n포인트 ▶ 같은 동사(walk)라도 자리에 따라 용법이 다르다", [])
T.flex('다음 밑줄 친 to부정사의 쓰임을 <u>잘못</u> 설명한 것은?', A_, '',
 [t('She was pleased [to see] him again. → 목적'), t('He must be kind [to help] her. → 판단의 근거'), t('She grew up [to be] a nurse. → 결과'), t('This question is hard [to answer]. → 형용사 수식'), t('I came here [to see] you. → 목적')],
 "이유 ▶ pleased(기쁜) 뒤 → 감정의 원인(다시 만나서 기뻤다).\n오답 ▶ {1} 돕다니 친절함에 틀림없다 ✔ {2} 자라서 간호사가 되었다 ✔ {3} 대답하기에 어렵다 ✔ {4} 너를 보러 왔다 ✔\n포인트 ▶ 감정 형용사 + to V는 목적이 아니라 감정의 원인!", [], en=False)
T.flex('<조건>에 맞게 우리말을 영어로 옮긴 것은?', P_, B('그는 아내를 만나러 미국에 돌아갔다.', '<조건> in order to를 쓸 것'),
 ['He went back to America in order to see his wife.', 'He went back to America in order see his wife.', 'He went back to America in order to seeing his wife.', 'He went back to America in order that see his wife.', 'He went back in order to America see his wife.'],
 "이유 ▶ went back to America + in order to see(목적).\n오답 ▶ {1} to 빠짐 {2} to 뒤는 원형 {3} in order that 뒤에는 주어 + 동사 {4} 어순이 깨짐\n포인트 ▶ in order to V = ~하기 위해서", [])
T.fixed('다음 글의 밑줄 친 ①~⑤ 중 어법상 틀린 것은?', '종합', B(
 "I'd like ①<u>to open</u> a flea market at school ②<u>to help</u> poor people. We can sell our handmade works ③<u>to raise</u> money. I'll be very happy ④<u>to helping</u> others with my talent. ⑤<u>To share</u> is a great thing."),
 None, 4,
 "이유 ▶ ④ to 뒤는 동사원형 → to help (감정의 원인).\n오답 ▶ ① would like의 목적어 ✔ ②·③ 목적 ✔ ⑤ 주어 ✔\n포인트 ▶ 글 속에서도 to 뒤 모양부터 확인", [])
T.flex('다음 밑줄 친 to부정사의 쓰임이 나머지 넷과 <u>다른</u> 것은?', A_, '',
 [t('I was sad [to lose] my puppy.'), t('She went to the library [to return] some books.'), t('Mom cleaned the oven [to bake] cookies.'), t('He got up early [to catch] the bus.'), t('They saved money [to travel] abroad.')],
 "이유 ▶ 강아지를 잃어서 슬펐다 → 감정의 원인.\n오답 ▶ {1}~{4} 모두 목적(~하기 위해서)\n포인트 ▶ sad · happy · glad · sorry · surprised + to V = 감정의 원인", [])
T.table('(A)~(C)에 들어갈 말이 바르게 짝지어진 것은?', '종합', B(
 '• She agreed <b>(A)</b> ______ me. (help)', '• He finished <b>(B)</b> ______ the room. (clean)', '• I stopped by the store <b>(C)</b> ______ milk. (buy)'),
 ['(A)', '(B)', '(C)'], [['to help', 'cleaning', 'to buy'], ['helping', 'cleaning', 'to buy'], ['to help', 'to clean', 'to buy'], ['to help', 'cleaning', 'buying'], ['helping', 'to clean', 'buying']],
 "이유 ▶ (A) agree + to V (B) finish + -ing (C) 우유를 사러(목적) → to buy\n오답 ▶ agreed helping ❌ / finished to clean ❌ / 목적은 to V (buying ❌)\n포인트 ▶ 목적어는 동사에 따라, 목적은 언제나 to V", [])
T.flex('다음 문장과 의미가 같은 것은?', N_, B('To learn many languages is useful.'),
 ['It is useful to learn many languages.', 'It is useful learn many languages.', 'That is useful to learn many languages.', 'It is useful to learning many languages.', 'Many languages is useful to learn it.'],
 "이유 ▶ 주어 to부정사가 길면 가주어 It을 앞에 두고 to V를 뒤로.\n오답 ▶ {1} to 빠짐 {2} 가주어는 It {3} to 뒤는 원형 {4} 주어가 바뀌고 it이 남음\n포인트 ▶ To V ~ is … = It is … to V ~", [])
T.flex('다음 중 어법상 올바른 문장은?', N_, '',
 ['We decided not to miss the movie.', 'We decided to not miss the movie.', 'She enjoys to bake cookies.', 'I hope seeing you soon.', 'My goal is to winning the race.'],
 "이유 ▶ to부정사의 부정은 not을 to 앞에 → not to miss.\n오답 ▶ {1} to not ❌ {2} enjoy + baking {3} hope + to see {4} to 뒤는 원형 win\n포인트 ▶ not to V = ~하지 않기로 / ~하지 않는 것", [])
T.flex("밑줄 친 to부정사가 '~해서 (결국) …하다(결과)'의 뜻으로 쓰인 것은?", A_, '',
 [t('He woke up [to find] himself famous.'), t('He woke up early [to study].'), t('I am happy [to wake] up early.'), t('It is hard [to wake] up early.'), t('My plan is [to wake] up early.')],
 "이유 ▶ 깨어나 보니 자신이 유명해져 있었다 → 결과.\n오답 ▶ {1} 목적(공부하려고) {2} 감정의 원인 {3} 진주어(명사적) {4} 보어(명사적)\n포인트 ▶ woke up to find ~ = 깨어나 보니 ~였다", [])
T.flex('다음 문장과 의미가 같은 것은?', P_, B('She went to the bakery so that she could buy some bread.'),
 ['She went to the bakery to buy some bread.', 'She went to the bakery for buy some bread.', 'She went to the bakery, so she bought some bread.', 'She bought some bread to go to the bakery.', 'She went to the bakery in order buy some bread.'],
 "이유 ▶ so that ~ could = 목적 → to buy.\n오답 ▶ {1} for + 동사원형 ❌ {2} '그래서 빵을 샀다'(결과 사실) {3} 빵을 사서 빵집에 간다(거꾸로) {4} in order to에서 to 빠짐\n포인트 ▶ so that 주어 can V = to V (목적)", [])
T.flex('두 문장을 한 문장으로 바꿀 때 빈칸에 들어갈 말로 알맞은 것은?', A_, B('Mina got a letter from her friend. She was very happy.', '→ Mina was very happy ' + BL + ' a letter from her friend.'),
 ['to get', 'get', 'got', 'to getting', 'for getting'],
 "이유 ▶ 편지를 받아서 기뻤다 → happy + to get(감정의 원인).\n오답 ▶ {1}·{2} 동사가 두 개 {3} to 뒤는 원형 {4} 감정의 원인은 to V\n포인트 ▶ 감정의 원인 = 감정 형용사 + to V", [])
T.flex('<보기>의 밑줄 친 부분과 쓰임이 같은 것은?', A_, B(t('<보기> This software is easy [to use].')),
 [t('This river is dangerous [to swim] in.'), t('She was surprised [to hear] it.'), t('He must be smart [to say] so.'), t('I went out [to buy] some food.'), t('He wants [to use] my computer.')],
 "이유 ▶ <보기>와 정답 모두 형용사(easy / dangerous)를 꾸밈 → ~하기에.\n오답 ▶ {1} 감정의 원인 {2} 판단의 근거 {3} 목적 {4} 목적어(명사적)\n포인트 ▶ easy · hard · dangerous · difficult + to V = 형용사 수식", [])
T.flex('다음 밑줄 친 to의 쓰임이 나머지 넷과 <u>다른</u> 것은?', '종합', '',
 [t('I went [to] the store yesterday.'), t('I want [to] go home.'), t('She came [to] see me.'), t('It is fun [to] swim.'), t('My dream is [to] be a pilot.')],
 "이유 ▶ to + 명사(the store) → 전치사(~으로).\n오답 ▶ {1}~{4} to + 동사원형 → to부정사\n포인트 ▶ to 뒤가 명사면 전치사, 동사원형이면 to부정사", [])
T.flex('다음 대화의 빈칸에 들어갈 말로 알맞은 것은?', P_, B('A: Why did you go to the library?', 'B: ' + BL),
 ['I went there to borrow some books.', 'I went there borrow some books.', 'I went there to borrowed some books.', 'I went there for borrow some books.', 'I went to there to borrow some books.'],
 "이유 ▶ Why ~? → 목적 to borrow로 답한다.\n오답 ▶ {1} to 빠짐 {2} to 뒤는 원형 {3} for + 동사원형 ❌ {4} there 앞에 to ❌\n포인트 ▶ Why ~? → To V. / ~ to V. (목적으로 답하기)", [])
T.fixed('<보기>의 밑줄 친 to부정사 중 목적(~하기 위해서)의 뜻으로 쓰인 것은 모두 몇 개인가?', K_, B(
 t('(a) Dad turned on the TV [to watch] the news.'), t("(b) I'm glad [to meet] you."), t('(c) She saved money [to buy] a bike.'), t('(d) He grew up [to be] a pilot.'), t('(e) We ran [to catch] the bus.')),
 NUMS, 3,
 "이유 ▶ 목적: (a) 뉴스를 보려고 (c) 자전거를 사려고 (e) 버스를 타려고 → 3개.\n오답 ▶ (b) 감정의 원인 (d) 결과\n포인트 ▶ 동작(turned on · saved · ran)의 이유 = 목적", [])
T.flex('다음 중 어법상 <u>어색한</u> 문장은?', N_, '',
 ['I want being a cook in the future.', 'To ride a bike is fun.', 'She plans to visit her grandfather.', 'Would you like to have dinner with us?', "I'm planning to take a swimming class."],
 "이유 ▶ want + to V → I want to be a cook.\n오답 ▶ {1} 주어 ✔ {2} plan + to V ✔ {3} would like + to V ✔ {4} planning + to V ✔\n포인트 ▶ want / would like / plan + to V", [])
T.flex('다음 우리말을 영어로 바르게 옮긴 것은?', '종합', B('우리는 서로를 돕기 위해 함께 일하기로 동의했다.'),
 ['We agreed to work together to help each other.', 'We agreed working together to help each other.', 'We agreed to work together help each other.', 'We agreed to working together to help each other.', 'We agree to work together to help each other.'],
 "이유 ▶ agreed + to work(목적어) + to help(목적).\n오답 ▶ {1} agree + -ing ❌ {2} help 앞 to 빠짐 {3} to 뒤는 원형 {4} '동의했다'(과거)인데 agree\n포인트 ▶ 한 문장에 to V 두 개: 앞은 목적어, 뒤는 목적", [])
T.flex('다음 중 어법상 올바른 문장은?', '종합', '',
 ['He went to the gym to exercise.', 'He went to the gym exercise.', 'He hopes going to the gym.', 'To exercising every day is good.', 'His goal is to exercises every day.'],
 "이유 ▶ 운동하러(목적) → to exercise ✔\n오답 ▶ {1} to 빠짐 {2} hope + to go {3} To exercise {4} to 뒤는 원형\n포인트 ▶ 용법이 달라도 to 뒤는 동사원형!", [])
T.render()
