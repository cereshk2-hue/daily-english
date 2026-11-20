# 11/20 중산중2 동아(윤정미) 7과 실전 문법 — 가주어 it · 진주어 1·2·3차 (각 20문항, 1차 기본 · 2차 중상 · 3차 상)
# 원본: 선생님 학습지 가주어진주어(1)·(2).hwp (work_src/m2gram/*.txt) + 7과 본문(it is important to remember dead people / Is it possible to do so?)
# 범위: It + be + 형용사 + to부정사 / that절, 의미상 주어 for·of, it 쓰임 구별(대명사·비인칭·가주어·강조), not to(3차 일부)
# 논쟁 피함: to not(분리 부정사) 오답으로 안 씀, 동명사 진주어(It is ~ -ing) 오답으로 안 씀, nice·strange·polite·crazy처럼 for·of 둘 다 되는 형용사로 for/of 고르기 안 냄, It takes ~ / It is time to ~ 는 가주어 구별 보기로 안 씀
import sys; sys.path.insert(0, '/home/claude/srcrepo/wrapup')
from wu_m2it import *
H = ('실전 문법', '중2 영어 동아(윤정미) 7과 가주어 it · 진주어', '동아(윤정미) 7과 가주어 · 진주어', 'm2it')
B = lambda *ls: BOX('<br>'.join(ls))
NUMS = ['1개', '2개', '3개', '4개', '5개']
t = lambda x: x.replace('[', '<u>').replace(']', '</u>')
G, S, K, R = '가주어 · 진주어', '의미상 주어', 'it 쓰임 구별', '7과 본문'
NOTE = '범위: 가주어 It + be + 형용사 + to부정사(진주어) / that절, to부정사의 의미상 주어 for · of, it의 여러 가지 쓰임 구별.'

# ═══════════════ 1차 (기본) ═══════════════
T = Test('1', '1차', '가주어 it · 진주어 to부정사', '가주어 it', NOTE, H=H); T.rot0 = 0
T.flex('다음 빈칸에 들어갈 말로 알맞은 것은?', G, B(BL + ' is important to follow the class rules.'),
 ['It', 'That', 'This', 'What', 'There'],
 "이유 ▶ 진주어 to follow ~를 뒤로 보내고 주어 자리에 가주어 It → 학급 규칙을 따르는 것은 중요하다.\n오답 ▶ {1}·{2}·{3}·{4} 가주어 자리에는 It만 씀\n포인트 ▶ It(가주어) + be + 형용사 + to부정사(진주어)", [('follow', '따르다'), ('rule', '규칙')])
T.flex('다음 빈칸에 들어갈 말로 알맞은 것은?', G, B('It is fun ' + BL + ' board games with my family.'),
 ['to play', 'play', 'played', 'plays', 'to playing'],
 "이유 ▶ 진주어 자리 → to + 동사원형 to play. 가족과 보드게임을 하는 것은 재미있다.\n오답 ▶ {1}·{2}·{3} 동사 is가 이미 있어 동사를 또 쓸 수 없음 {4} to 뒤는 동사원형\n포인트 ▶ It is 형용사 + to + 동사원형", [])
T.flex('다음 빈칸에 들어갈 말이 바르게 짝지어진 것은?', G, B(BL + " isn't easy " + BL + ' make new friends.'),
 ['It − to', 'It − for', 'It − that', 'What − to', 'What − that'],
 "이유 ▶ 가주어 It + 진주어 to make → 새 친구를 사귀는 것은 쉽지 않다.\n오답 ▶ {1} for 뒤에 동사원형 ❌ {2} that 뒤에는 주어 + 동사 {3}·{4} 가주어 자리에 What ❌\n포인트 ▶ 동사원형 앞에는 to", [])
T.flex('다음 문장과 의미가 같은 것은?', G, B('To send e-mail is simple.'),
 ['It is simple to send e-mail.', 'It is simple to sends e-mail.', 'That is simple to send e-mail.', 'It is simple to e-mail send.', 'It is simple for send e-mail.'],
 "이유 ▶ 주어 To send e-mail을 뒤로 보내고 가주어 It → It is simple to send e-mail.\n오답 ▶ {1} to 뒤는 동사원형 {2} 가주어는 That ❌ {3} 어순 ❌ {4} for + 동사원형 ❌\n포인트 ▶ To V ~ is 형용사 = It is 형용사 to V ~", [])
T.flex('다음 문장을 가주어 It으로 시작하는 문장으로 바르게 바꾼 것은?', S, B('To learn English is difficult for me.'),
 ['It is difficult for me to learn English.', 'It is difficult to me learn English.', 'It is difficult for me learn English.', 'It is difficult of me to learn English.', 'It is difficult for I to learn English.'],
 "이유 ▶ 의미상 주어 for me + 진주어 to learn English.\n오답 ▶ {1} to me + 동사원형 ❌ {2} to 빠짐 {3} difficult는 of가 아닌 for {4} 전치사 뒤는 목적격 me\n포인트 ▶ It is 형용사 + for + 목적격 + to V", [])
T.flex('<보기>의 밑줄 친 It과 쓰임이 같은 것은?', K, B(t('<보기> [It] is very good to get up early in the morning.')),
 [t("[It]'s interesting to play table tennis."), t("[It]'s raining now."), t('What is [it]?'), t('I saw [it] yesterday.'), t("[It]'s March 18th.")],
 "이유 ▶ <보기>와 정답 모두 뒤의 to부정사를 대신하는 가주어 It(해석하지 않음).\n오답 ▶ {1} 날씨 {4} 날짜 → 비인칭 주어 {2}·{3} '그것' → 대명사\n포인트 ▶ 뒤에 to + 동사원형(진주어)이 있으면 가주어", [])
T.flex('다음 중 어법상 <u>어색한</u> 것은?', G, '',
 ['It is possible learn English.', 'It is good to read many books.', 'It is dangerous to go out at night.', 'It is exciting to watch fireworks.', 'It is important to remember dead people.'],
 "이유 ▶ 진주어 자리에 to가 빠짐 → It is possible to learn English.\n오답 ▶ {1}~{4} It + be + 형용사 + to부정사 ✔\n포인트 ▶ 가주어 문장의 진주어는 to + 동사원형", [])
T.flex('다음 우리말을 영어로 바르게 옮긴 것은?', G, B('매일 운동하는 것은 쉽지 않다.'),
 ["It isn't easy to exercise every day.", "It isn't easy exercise every day.", "That isn't easy to exercise every day.", "It isn't easy to exercises every day.", "It doesn't easy to exercise every day."],
 "이유 ▶ It(가주어) isn't easy + to exercise every day(진주어).\n오답 ▶ {1} to 빠짐 {2} 가주어는 It {3} to 뒤는 동사원형 {4} easy는 형용사 → be동사 isn't\n포인트 ▶ ~하는 것은 …하지 않다 = It isn't 형용사 to V", [])
T.flex('다음 우리말에 맞게 주어진 단어를 바르게 배열한 것은?', G, B('그 문제를 푸는 것은 쉽지 않았다.', '( to / solve / wasn\'t / it / easy / the problem )'),
 ["It wasn't easy to solve the problem.", "It wasn't to solve easy the problem.", "It wasn't easy the problem to solve.", "To solve wasn't easy it the problem.", "It easy wasn't to solve the problem."],
 "이유 ▶ It + wasn't + easy + to solve + the problem.\n오답 ▶ {1}·{2}·{4} 어순 ❌ {3} it이 남아서 주어가 둘\n포인트 ▶ It + be + 형용사 + to + 동사원형 + 목적어", [])
T.flex('다음 빈칸에 들어갈 말로 알맞은 것은?', S, B('It is hard ' + BL + ' me to keep a diary every day.'),
 ['for', 'of', 'to', 'with', 'by'],
 "이유 ▶ hard(어려운)는 사람의 성격이 아님 → 의미상 주어 for me. 내가 매일 일기를 쓰는 것은 어렵다.\n오답 ▶ {1} of는 성격 형용사(kind · wise · careless …) 뒤 {2}·{3}·{4} 의미상 주어로 쓰지 않음\n포인트 ▶ 의미상 주어 = for + 목적격", [])
T.flex('다음 빈칸에 들어갈 말로 알맞은 것은?', S, B('It is very kind ' + BL + ' you to help me.'),
 ['of', 'for', 'to', 'at', 'with'],
 "이유 ▶ kind는 사람의 성격을 나타내는 형용사 → 의미상 주어 of you. 나를 도와주다니 너는 정말 친절하구나.\n오답 ▶ {1} for는 성격이 아닌 형용사(easy · hard · important …) 뒤 {2}·{3}·{4} 의미상 주어로 쓰지 않음\n포인트 ▶ kind · wise · foolish · careless · rude · stupid + of + 목적격", [])
T.flex('다음 우리말에 맞도록 빈칸에 들어갈 말로 알맞은 것은?', S, B('Jane이 선생님이 되기는 어려울 것이다.', '→ It will be difficult ' + BL + ' to be a teacher.'),
 ['for Jane', 'Jane', 'to Jane', 'of Jane', "Jane's"],
 "이유 ▶ to be a teacher의 주인공(의미상 주어) = Jane, difficult → for Jane.\n오답 ▶ {1}·{4} 전치사 없이 ❌ {2} to ❌ {3} difficult는 성격 형용사가 아님\n포인트 ▶ 의미상 주어는 to부정사 바로 앞에 for + 목적격", [])
T.flex('다음 빈칸에 들어갈 말이 바르게 짝지어진 것은?', S, B('• It is important ' + BL + ' to say sorry.', '• It was careless ' + BL + ' to leave the keys on the table.'),
 ['for you − of her', 'of you − of her', 'of you − for her', 'for you − for her', 'for you − of she'],
 "이유 ▶ important(성격 X) → for you / careless(부주의한, 성격) → of her.\n오답 ▶ {1}·{2} important 뒤에 of ❌ {3} careless 뒤에 for ❌ {4} 전치사 뒤는 목적격 her\n포인트 ▶ 성격 형용사면 of, 아니면 for", [('careless', '부주의한')])
T.flex('다음 밑줄 친 It의 쓰임이 나머지 넷과 <u>다른</u> 것은?', K, '',
 [t('[It] is a kind of Korean traditional food.'), t("[It] is not easy to understand another's point of view."), t('[It] was difficult to solve the math problem.'), t('[It] is necessary to exercise regularly.'), t('[It] is dangerous to swim in this river.')],
 "이유 ▶ '그것은 한국 전통 음식의 한 종류이다' → '그것'으로 해석되는 대명사 it.\n오답 ▶ {1}~{4} 뒤에 to부정사(진주어)가 있는 가주어 It\n포인트 ▶ It is + 명사(food) → 대명사 / It is + 형용사 + to V → 가주어", [('point of view', '관점')])
T.flex('다음 문장을 가주어 It을 써서 바르게 바꾼 것은?', G, B('That all people are equal is important.'),
 ['It is important that all people are equal.', 'It is important all people are equal that.', 'It is important to all people are equal.', 'That is important it all people are equal.', 'It is important what all people are equal.'],
 "이유 ▶ that절(주어)도 뒤로 보내고 가주어 It → It is important that all people are equal.\n오답 ▶ {1} that 위치 ❌ {2} to 뒤에 주어 + 동사 ❌ {3} 가주어는 It {4} 완전한 문장 앞엔 what이 아니라 that\n포인트 ▶ It is 형용사 + that + 주어 + 동사", [('equal', '평등한')])
T.flex('다음 대화의 빈칸에 들어갈 말로 알맞은 것은?', S, B('A: Have you finished your homework?', 'B: No, I haven\'t. I have lots of homework, so it is impossible ' + BL + ' my homework today.'),
 ['for me to finish', 'for me finish', 'of me finished', 'of me to finish', 'for me to finishing'],
 "이유 ▶ impossible(성격 X) → for me + to finish.\n오답 ▶ {1} to 빠짐 {2} of · 과거형 ❌ {3} impossible 뒤에 of ❌ {4} to 뒤는 동사원형\n포인트 ▶ It is impossible for 목적격 to V = (누가) ~하는 것은 불가능하다", [])
T.flex('다음 문장에서 어색한 부분을 바르게 고친 것은?', G, B('This is hard to find the things that I want to buy.'),
 ['This → It', 'hard → hardly', 'to find → found', 'that → what', 'to buy → buying'],
 "이유 ▶ 진주어 to find ~ 앞의 가주어는 This가 아니라 It → It is hard to find ~.\n오답 ▶ {1} be동사 뒤 보어는 형용사 hard {2} 진주어는 to부정사 {3} 선행사 the things 뒤 관계대명사 that ✔ {4} want to buy ✔\n포인트 ▶ 가주어는 언제나 It", [])
T.flex('다음 문장과 의미가 같은 것은?', G, B('To eat a lot of vegetables is good for your health.'),
 ['It is good for your health to eat a lot of vegetables.', 'It is good to your health eat a lot of vegetables.', 'It is good for your health eat a lot of vegetables.', 'It is good for your health to eating a lot of vegetables.', 'It is good for your health that eat a lot of vegetables.'],
 "이유 ▶ It is good for your health + to eat ~(진주어).\n오답 ▶ {1} to your health ❌ · to부정사 없음 {2} to 빠짐 {3} to 뒤는 동사원형 {4} that 뒤엔 주어 + 동사\n포인트 ▶ for your health(건강에)는 의미상 주어가 아니라 그대로 두는 말", [])
T.flex('다음 빈칸에 공통으로 들어갈 말로 알맞은 것은?', S, B('• It is impossible ' + BL + ' me to do that alone.', '• It was exciting ' + BL + ' them to reach the top of the mountain.'),
 ['for', 'of', 'at', 'in', 'by'],
 "이유 ▶ impossible · exciting은 성격 형용사가 아님 → 의미상 주어 for me / for them.\n오답 ▶ {1} of는 성격 형용사 뒤 {2}·{3}·{4} 의미상 주어로 쓰지 않음\n포인트 ▶ for + 목적격 + to V", [])
T.flex('다음 밑줄 친 문장의 해석으로 알맞은 것은?', R, B('People who participate in this race wear fun costumes and try to run faster than reindeer. ' + t('[Is it possible to do so?]') + ' Not really, but it doesn\'t matter.'),
 ['그렇게 하는 것이 가능할까?', '그것은 그렇게 하는 것을 가능하게 할까?', '그것은 그렇게 해도 될까?', '그것이 그렇게 하기 위해 가능할까?', '그렇게 한 것이 그것일까?'],
 "이유 ▶ it = 가주어(해석 X), 진주어 to do so(그렇게 하는 것) → 그렇게 하는 것이 가능할까?\n오답 ▶ {1}~{4} it을 '그것'으로 해석함 ❌\n포인트 ▶ 가주어 It은 해석하지 않고 진주어부터 해석", [('participate in', '~에 참가하다'), ('reindeer', '순록')], en=False)
T.render()

# ═══════════════ 2차 (중상) ═══════════════
T = Test('2', '2차', '가주어 it · 의미상 주어 for / of', '가주어 it', NOTE, H=H); T.rot0 = 2
T.flex('다음 중 가주어 It을 써서 바꾼 문장이 <u>틀린</u> 것은?', G, '',
 ['To understand his speech was hard.<br>→ It is hard to understand his speech.', 'To watch fireworks is exciting.<br>→ It is exciting to watch fireworks.', "To raise cows is a farmer's work.<br>→ It is a farmer's work to raise cows.", 'That she is popular is true.<br>→ It is true that she is popular.', 'To find your house was difficult.<br>→ It was difficult to find your house.'],
 "이유 ▶ 원래 문장이 과거(was) → It was hard to understand his speech. (시제를 바꾸면 안 됨)\n오답 ▶ {1}·{2}·{4} to부정사 진주어 ✔ {3} that절 진주어 ✔\n포인트 ▶ 가주어로 바꿔도 동사의 시제는 그대로", [])
T.flex('다음 빈칸에 들어갈 말로 알맞지 <u>않은</u> 것은?', S, B('It is ' + BL + ' for me to get up before 5 o\'clock.'),
 ['wise', 'impossible', 'hard', 'difficult', 'easy'],
 "이유 ▶ wise(현명한)는 사람의 성격 → for me가 아니라 of me를 씀.\n오답 ▶ {1}~{4} 성격이 아닌 형용사 → for me ✔\n포인트 ▶ 빈칸 뒤 for가 있으면 성격 형용사는 못 옴", [])
T.flex('다음 빈칸에 들어갈 말이 나머지 넷과 <u>다른</u> 것은?', S, '',
 ['It is very careless ' + BL + ' you to go there.', 'It was easy ' + BL + ' us to find your house.', 'It was hard ' + BL + ' me to solve the puzzle.', 'It is fun ' + BL + ' me to learn English.', 'It is important ' + BL + ' her to finish the work.'],
 "이유 ▶ careless(부주의한, 성격) → of you.\n오답 ▶ {1}~{4} easy · hard · fun · important → for\n포인트 ▶ 성격 형용사 + of / 그 밖의 형용사 + for", [])
T.flex('<보기>의 빈칸에 들어갈 말과 같은 말이 들어가는 것은?', S, B('<보기> It is foolish ' + BL + ' him to spend all his money.'),
 ['It is rude ' + BL + ' him not to apologize.', 'It is dangerous ' + BL + ' children to play in the street.', 'It was easy ' + BL + ' Koreans to use chopsticks.', 'Is it possible ' + BL + ' us to finish the project in time?', 'It is difficult ' + BL + ' Jack to memorize the poem.'],
 "이유 ▶ <보기> foolish(어리석은)와 정답 rude(무례한)는 성격 형용사 → of.\n오답 ▶ {1}~{4} dangerous · easy · possible · difficult → for\n포인트 ▶ foolish · rude · kind · wise · careless · stupid + of", [('apologize', '사과하다'), ('memorize', '외우다')])
T.flex('다음 중 어법상 <u>어색한</u> 것은?', S, '',
 ["It's impossible of me to find her house.", "It's hard for him to get a driver's license.", "It's important for me to practice English.", "It's generous of you to visit him every week.", "It's easy for her to pass the exam."],
 "이유 ▶ impossible은 성격 형용사가 아님 → for me.\n오답 ▶ {1}·{2}·{4} hard · important · easy + for ✔ {3} generous(너그러운, 성격) + of ✔\n포인트 ▶ 형용사가 사람의 성격을 말하는지 먼저 확인", [('generous', '너그러운'), ("driver's license", '운전 면허')])
T.flex('(A), (B), (C)에서 알맞은 것끼리 짝지은 것은?', S, B('• It is wise (A) [ for / of ] you to follow the rules.', '• It is dangerous (B) [ for / of ] them to stay here.', '• It was difficult (C) [ to understand / understood ] the situation.'),
 ['of − for − to understand', 'for − for − to understand', 'of − of − understood', 'for − of − to understand', 'of − for − understood'],
 "이유 ▶ (A) wise(성격) → of (B) dangerous → for (C) 진주어 → to understand\n오답 ▶ (A)에 for · (B)에 of · (C)에 understood가 들어간 보기는 모두 틀림\n포인트 ▶ 가주어 문장의 진주어는 to부정사", [('situation', '상황')])
T.flex('다음 우리말을 영어로 바르게 옮긴 것은?', S, B('내가 그 문제를 푸는 것은 어려운 일이었다.'),
 ['It was difficult for me to solve the problem.', 'It was difficult to me to solve the problem.', 'It was difficult of me to solve the problem.', 'It was difficult I to solve the problem.', 'It was difficult me to solve the problem.'],
 "이유 ▶ 의미상 주어 for me + to solve.\n오답 ▶ {1} to me ❌ {2} difficult는 of ❌ {3}·{4} 전치사 for가 빠짐\n포인트 ▶ (누가) ~하는 것은 …하다 = It is … for 목적격 to V", [])
T.flex('다음 두 문장의 의미가 같도록 할 때 빈칸에 알맞은 것은?', S, B('You were stupid not to accept his proposal.', '= ' + BL + ' accept his proposal.'),
 ['It was stupid of you not to', 'It was stupid for you not to', 'It was stupid of you not', 'It was stupid of your not to', 'It is stupid of you not to'],
 "이유 ▶ 사람 + be + 성격 형용사 + to V = It + be + 성격 형용사 + of + 목적격 + to V. 부정은 not to, 시제는 과거 was.\n오답 ▶ {1} stupid는 for ❌ {2} to 빠짐 {3} 목적격 you {4} 시제 is ❌\n포인트 ▶ to부정사의 부정 = not + to V", [('accept', '받아들이다'), ('proposal', '제안')])
T.flex('다음 대화의 빈칸에 알맞은 말은?', S, B('A: Mom, Sophie helped me with the math homework.', 'B: It was kind ' + BL + ' to help you. How sweet!'),
 ['of her', 'for her', 'of she', 'to her', 'her'],
 "이유 ▶ kind(친절한, 성격) → of + 목적격 her.\n오답 ▶ {1} kind는 for ❌ {2} 전치사 뒤 목적격 her {3} to ❌ {4} 전치사가 빠짐\n포인트 ▶ It was kind of 사람 to V = ~하다니 (사람)은 친절했다", [])
T.flex('우리말에 맞게 주어진 단어를 배열할 때 네 번째로 오는 단어는?', G, B('패스트푸드를 먹는 것은 건강에 좋지 않다.', '( eat / not / it / healthy / to / is ) fast food.'),
 ['healthy', 'not', 'to', 'is', 'eat'],
 "이유 ▶ It is not healthy to eat fast food. → 네 번째 단어 healthy\n오답 ▶ It(1) is(2) not(3) healthy(4) to(5) eat(6)\n포인트 ▶ 부정 not은 be동사 바로 뒤", [])
T.flex('<보기>의 밑줄 친 it과 쓰임이 같은 것은?', K, B(t("<보기> I don't think [it]'s good to get so many side dishes.")),
 [t('[It] is important to exercise every day.'), t('[It] is so hot out there.'), t('[It] is five kilometers from here.'), t('[It] is too big for your little brother.'), t('[It] is getting dark.')],
 "이유 ▶ <보기>와 정답 모두 뒤의 to부정사를 대신하는 가주어.\n오답 ▶ {1} 날씨 {2} 거리 {4} 명암 → 비인칭 주어 {3} '그것은 네 남동생에게 너무 크다' → 대명사\n포인트 ▶ that절 안의 it's good to ~도 가주어", [('side dish', '반찬')])
T.flex('다음 밑줄 친 It의 쓰임이 나머지 넷과 <u>다른</u> 것은?', K, '',
 [t('[It] is easy to solve the question.'), t('[It] is ten thirty in Paris now.'), t('[It] is winter in Australia now.'), t('[It] is two kilometers to my school.'), t('[It] is getting warmer and warmer.')],
 "이유 ▶ 진주어 to solve the question을 대신하는 가주어.\n오답 ▶ {1} 시간 {2} 계절 {3} 거리 {4} 날씨 → 비인칭 주어\n포인트 ▶ 비인칭 주어: 시간 · 날짜 · 요일 · 계절 · 날씨 · 거리 · 명암", [])
T.flex('다음 글의 밑줄 친 it과 쓰임이 같은 것은?', R, B('People who participate in this race wear fun costumes and try to run faster than reindeer. Is ' + U('it') + ' possible to do so? Not really, but it doesn\'t matter.'),
 [t('[It] is important to remember dead people.'), t('[It] is February 28 today.'), t('[It] started to run toward them.'), t('[It] is a giant wooden statue.'), t('[It] is very dark in the forest.')],
 "이유 ▶ 본문 it = 진주어 to do so를 대신하는 가주어. 정답도 to remember ~의 가주어.\n오답 ▶ {1} 날짜 {4} 명암 → 비인칭 주어 {2} 그것(공룡) {3} 그것(조각상) → 대명사\n포인트 ▶ 의문문 Is it 형용사 to V ~?도 가주어", [('statue', '조각상')])
T.flex('다음 빈칸에 들어갈 말로 알맞지 <u>않은</u> 것은?', S, B('It was ' + BL + ' of you to leave your purse on the bus.'),
 ['difficult', 'careless', 'foolish', 'silly', 'stupid'],
 "이유 ▶ 빈칸 뒤 of you → 성격 형용사만 가능. difficult는 for와 씀.\n오답 ▶ {1}~{4} careless · foolish · silly · stupid = 성격 형용사 → of ✔\n포인트 ▶ of 앞 = 사람의 성격(부주의한 · 어리석은)", [('purse', '지갑')])
T.flex('다음 중 어법상 올바른 것은?', G, '',
 ['It is a lot of fun to play computer games.', 'It is difficult that live without a computer.', 'It is important that spend our time wisely.', 'It is difficult of foreigners to use chopsticks.', 'It is hard take care of babies.'],
 "이유 ▶ It is + 명사(a lot of fun) + to부정사(진주어)도 가능 ✔\n오답 ▶ {1}·{2} that 뒤에는 주어 + 동사 (to live / that we spend) {3} difficult → for foreigners {4} to 빠짐 → to take\n포인트 ▶ that 진주어엔 주어가, to 진주어엔 동사원형이", [('foreigner', '외국인'), ('chopsticks', '젓가락')])
T.flex('다음 빈칸에 들어갈 말이 바르게 짝지어진 것은?', G, B(BL + ' is certain ' + BL + ' my sister hates swimming.'),
 ['It − that', 'That − it', 'It − to', 'This − that', 'It − what'],
 "이유 ▶ 진주어가 that절(주어 my sister + 동사 hates) → It is certain that ~. 내 여동생이 수영을 싫어하는 것은 확실하다.\n오답 ▶ {1} 순서 반대 {2} to 뒤엔 동사원형 {3} 가주어는 It {4} 완전한 문장 앞엔 that\n포인트 ▶ It ~ that + 주어 + 동사", [('certain', '확실한')])
T.fixed('다음 글의 밑줄 친 부분 중 어법상 <u>어색한</u> 것은?', S, B('It is not dangerous ⓐ ' + U('children') + ' ⓑ ' + U('to play') + ' soccer ⓒ ' + U('in the playground') + '. But it is dangerous ⓓ ' + U('for them') + ' to play soccer ⓔ ' + U('on the street') + '.'),
 ['ⓐ', 'ⓑ', 'ⓒ', 'ⓓ', 'ⓔ'], 1,
 "이유 ▶ ⓐ 의미상 주어에는 for가 필요 → for children\n오답 ▶ ⓑ 진주어 to play ✔ ⓒ 장소 ✔ ⓓ for + 목적격 ✔ ⓔ 장소 ✔\n포인트 ▶ 의미상 주어 = for + 목적격 (전치사 빼면 ❌)", [('playground', '운동장')])
T.flex('다음 문장과 의미가 같은 것은?', G, B('It is very important to have breakfast.'),
 ['To have breakfast is very important.', 'Have breakfast is very important.', 'To have breakfast are very important.', 'It to have breakfast is very important.', 'Having breakfast it is very important.'],
 "이유 ▶ 진주어 to have breakfast를 주어 자리로 → To have breakfast is very important.\n오답 ▶ {1} 동사원형으로 주어 ❌ {2} to부정사 주어는 단수 → is {3}·{4} 주어가 둘\n포인트 ▶ 가주어 문장 ↔ To V 주어 문장 (동사는 단수)", [])
T.flex('다음 밑줄 친 부분이 to부정사의 의미상 주어인 것은?', S, '',
 [t('It is important [for her] to finish the work.'), t('This gift is [for her].'), t('I waited [for her] for an hour.'), t('He bought flowers [for her].'), t('It is a letter [for her].')],
 "이유 ▶ for her가 to finish의 행동하는 사람 → 그녀가 그 일을 끝내는 것은 중요하다.\n오답 ▶ {1}·{3}·{4} '그녀를 위한' {2} wait for = ~를 기다리다 → 뒤에 to부정사가 없음\n포인트 ▶ 의미상 주어는 to부정사 바로 앞의 for + 목적격", [])
T.fixed('다음 대화의 ①~⑤ 중 주어진 문장이 들어갈 곳으로 알맞은 것은?', G, B('<b>I think it\'s really fun to shop there.</b>', 'A: Do you like shopping in Insadong, Jane? ( ① )', 'B: Of course. ( ② ) How about you? ( ③ )', 'A: ( ④ ) I agree, but don\'t you think it\'s too crowded? ( ⑤ )', 'B: But there are lots of interesting things to see.'),
 None, 2,
 "이유 ▶ Of course(물론 좋아해) 다음에 '거기서 쇼핑하는 건 정말 재미있다고 생각해' → 그 뒤 How about you? / A가 I agree로 받음.\n오답 ▶ ① A의 질문 뒤에 A가 또 말할 수 없음 ③ How about you?로 상대에게 물어 놓고 대답도 듣기 전에 자기 말을 또 함 ④·⑤ A가 자기 말에 I agree를 할 수 없음\n포인트 ▶ it's fun to shop there = 가주어 + 진주어", [('crowded', '붐비는')])
T.render()

# ═══════════════ 3차 (상) ═══════════════
T = Test('3', '3차', '가주어 it · 의미상 주어 · it 쓰임 심화', '가주어 it', NOTE, H=H); T.rot0 = 4
T.flex('다음 빈칸에 들어갈 말로 알맞지 <u>않은</u> 것은?', S, B('It was ' + BL + ' for her to forgive him.'),
 ['silly', 'easy', 'difficult', 'hard', 'impossible'],
 "이유 ▶ silly(어리석은)는 성격 형용사 → for her가 아니라 of her.\n오답 ▶ {1}~{4} 성격이 아닌 형용사 → for her ✔\n포인트 ▶ 빈칸 뒤 for → 성격 형용사 ❌", [('forgive', '용서하다')])
T.flex('다음 중 어법상 <u>틀린</u> 문장끼리 묶인 것은?', S, B('ⓐ It is time for me to take a vacation now.', 'ⓑ It is not easy of my father to quit smoking.', "ⓒ Sophie's mother told Sophie not to swim in the sea.", 'ⓓ It is foolish for him to spend all his money.'),
 ['ⓑ, ⓓ', 'ⓐ, ⓑ', 'ⓐ, ⓒ', 'ⓒ, ⓓ', 'ⓑ, ⓒ'],
 "이유 ▶ ⓑ easy → for my father ⓓ foolish(성격) → of him\n오답 ▶ ⓐ It is time for 목적격 to V ✔ ⓒ tell + 목적어 + not to V ✔\n포인트 ▶ 의미상 주어 for / of는 앞 형용사로 결정", [('quit', '그만두다')])
T.flex('다음 중 어법상 올바른 문장의 개수는?', G, B('ⓐ It is polite of you to knock on the door.', 'ⓑ It is necessary of him to get the answer.', 'ⓒ It was exciting for them to reach the top of the mountain.', 'ⓓ That is important to keep a diary.', 'ⓔ It is true that Mr. Cook has bought a new car.'),
 ['3개', '1개', '2개', '4개', '5개'],
 "이유 ▶ 올바른 것 ⓐ · ⓒ · ⓔ → 3개\n틀린 것 ▶ ⓑ necessary → for him ⓓ 가주어 That → It\n포인트 ▶ ⓐ polite(예의 바른) + of you ✔ / ⓔ that절 진주어 ✔", [('knock', '노크하다')])
T.flex('다음 밑줄 친 부분의 쓰임이 나머지 넷과 <u>다른</u> 것은?', S, '',
 [t('It was a picture [of him] at the age of five.'), t('It was careless [of you] to drive so fast.'), t('It is kind [of him] to invite his grandparents.'), t('It is honest [of her] to say that she made a mistake.'), t('It is clever [of you] to suggest such a thing.')],
 "이유 ▶ a picture of him = 그의 사진 → 의미상 주어가 아님(It도 대명사).\n오답 ▶ {1}~{4} 성격 형용사 + of + 목적격 + to V → to부정사의 의미상 주어\n포인트 ▶ of 뒤에 to부정사가 이어지는지 확인", [('suggest', '제안하다')])
T.flex('다음 두 문장의 의미가 같지 <u>않은</u> 것은?', S, '',
 ['It is difficult for him to speak in front of his friends.<br>= He is difficult to speak in front of his friends.', "It's so sweet of you to help my sister.<br>= You are so sweet to help my sister.", 'It was careless of you to leave your purse on the bus.<br>= You were careless to leave your purse on the bus.', 'To master something in a short time is impossible.<br>= It is impossible to master something in a short time.', 'That she broke her leg is a pity.<br>= It is a pity that she broke her leg.'],
 "이유 ▶ difficult는 성격 형용사가 아님 → 사람(He)을 주어로 바꿔 쓸 수 없음. (He is difficult = 그는 까다롭다)\n오답 ▶ {1}·{2} 성격 형용사 of 문장 = 사람 주어 문장 ✔ {3} To V 주어 ↔ 가주어 ✔ {4} that절 주어 ↔ 가주어 ✔\n포인트 ▶ It is 성격 형용사 of A to V = A is 성격 형용사 to V", [('master', '완전히 익히다'), ('pity', '유감')])
T.flex('다음 빈칸에 들어갈 말이 순서대로 바르게 짝지어진 것은?', S, B('• It is generous ' + BL + ' you to invite them for dinner.', '• It will be fun ' + BL + ' you to learn how to make your own homepage.', '• It was wise ' + BL + ' him not to drive at night.'),
 ['of − for − of', 'for − for − of', 'of − of − for', 'of − for − for', 'for − of − of'],
 "이유 ▶ generous(너그러운, 성격) → of / fun → for / wise(현명한, 성격) → of\n오답 ▶ 첫째 칸 for · 둘째 칸 of · 셋째 칸 for 가 들어간 보기는 모두 틀림\n포인트 ▶ 부정 not to V가 와도 의미상 주어는 형용사로 정함", [('generous', '너그러운')])
T.flex('다음 우리말을 영어로 바르게 옮긴 것은?', S, B('어떤 학생들에게는 그들 자신만의 결정을 내리는 것이 어렵다.'),
 ['It is difficult for some students to make their own decisions.', 'It is difficult of some students to make their own decisions.', 'It is difficult for some students make their own decisions.', 'Some students is difficult to make their own decisions.', 'It is difficult some students to make their own decisions.'],
 "이유 ▶ It is difficult + for some students(의미상 주어) + to make ~.\n오답 ▶ {1} difficult는 of ❌ {2} to 빠짐 {3} difficult는 사람 주어 ❌ · 수 일치도 ❌ {4} for 빠짐\n포인트 ▶ for + 명사(some students)도 의미상 주어", [('decision', '결정')])
T.fixed('다음 글의 밑줄 친 부분 중 어법상 <u>어색한</u> 것은?', R, B('Many Mexicans believe ⓐ ' + U('that') + ' dead people come back home once a year. They think ⓑ ' + U('it') + ' is important ⓒ ' + U('remembering') + ' dead people. So, people set up altars ⓓ ' + U('in their homes') + '. It is fun ⓔ ' + U('for visitors') + ' to watch the big parades.'),
 ['ⓐ', 'ⓑ', 'ⓒ', 'ⓓ', 'ⓔ'], 3,
 "이유 ▶ ⓒ 가주어 it의 진주어 → to remember (교과서: They believe it is important to remember dead people.)\n오답 ▶ ⓐ believe의 목적어 that절 ✔ ⓑ 가주어 it ✔ ⓓ 장소 ✔ ⓔ 의미상 주어 for visitors ✔\n포인트 ▶ 가주어 It ~ 형용사 + to부정사", [('altar', '제단'), ('parade', '퍼레이드')])
T.flex('다음 빈칸에 that이 들어갈 수 <u>없는</u> 것은?', G, '',
 ['It is necessary ' + BL + ' exercise regularly.', 'It is true ' + BL + ' she is popular.', 'It is important ' + BL + ' we spend our time wisely.', 'It is certain ' + BL + ' my sister hates swimming.', 'It is a pity ' + BL + ' she broke her leg.'],
 "이유 ▶ 빈칸 뒤가 동사원형(exercise) → to가 들어가야 함 (It is necessary to exercise regularly.)\n오답 ▶ {1}~{4} 빈칸 뒤 주어 + 동사 → that ✔\n포인트 ▶ 뒤에 주어 + 동사면 that, 동사원형이면 to", [('regularly', '규칙적으로')])
T.flex('다음 두 문장을 한 문장으로 바르게 바꾼 것은?', S, B("Children shouldn't swim in the deep sea. It is dangerous."),
 ['It is dangerous for children to swim in the deep sea.', 'It is dangerous of children to swim in the deep sea.', 'It is dangerous children to swim in the deep sea.', 'It is dangerous for children to swims in the deep sea.', 'Children are dangerous to swim in the deep sea.'],
 "이유 ▶ 아이들이 깊은 바다에서 수영하는 것은 위험하다 → It is dangerous for children to swim ~.\n오답 ▶ {1} dangerous는 of ❌ {2} for 빠짐 {3} to 뒤는 동사원형 {4} '아이들이 위험한 존재'라는 뜻이 됨\n포인트 ▶ 위험한 것은 '수영하는 것' → 가주어 It", [])
T.flex('다음 밑줄 친 It의 쓰임이 나머지 넷과 <u>다른</u> 것은?', K, '',
 [t('[It] was yesterday that I met my uncle.'), t('[It] is possible to build cities on the moon.'), t('[It] was nice of you to help the little boy.'), t('[It] is hard to finish the work today.'), t('[It] is great that the festival will be held in Seoul.')],
 "이유 ▶ It was ~ that 사이에 yesterday를 넣어 강조 → '내가 삼촌을 만난 것은 바로 어제였다'(강조 구문). It was와 that을 빼도 문장이 됨(I met my uncle yesterday).\n오답 ▶ {1}·{2}·{3} to부정사 진주어의 가주어 {4} that절(the festival will be held …) 진주어의 가주어\n포인트 ▶ It is 형용사 that ~ = 가주어 / It is 부사·명사 that ~ = 강조", [])
T.flex('다음 밑줄 친 It의 쓰임이 같은 것끼리 짝지어진 것은?', K, B(t("ⓐ [It] isn't easy to follow that rule."), t('ⓑ [It] will be dark before long.'), t('ⓒ [It] is interesting to talk with him.'), t('ⓓ [It] was a present from my aunt.'), t('ⓔ [It] is cold and windy today.')),
 ['ⓐ, ⓒ', 'ⓐ, ⓑ', 'ⓑ, ⓓ', 'ⓒ, ⓔ', 'ⓓ, ⓔ'],
 "이유 ▶ ⓐ · ⓒ 모두 뒤의 to부정사를 대신하는 가주어\n오답 ▶ ⓑ 명암 · ⓔ 날씨 → 비인칭 주어 / ⓓ '그것은 이모가 준 선물이었다' → 대명사\n포인트 ▶ 비인칭(ⓑ, ⓔ) · 가주어(ⓐ, ⓒ) · 대명사(ⓓ)", [('before long', '곧')])
T.flex('다음 문장을 가주어 It을 써서 바꾼 것으로 알맞은 것은?', G, B('To spend so much time playing computer games is not good.'),
 ['It is not good to spend so much time playing computer games.', 'It is not good to spend so much time play computer games.', 'It does not good to spend so much time playing computer games.', 'It is good not to spend so much time playing computer games.', 'It is not good to spend so much time to play computer games.'],
 "이유 ▶ It is not good + to spend so much time playing ~ (spend + 시간 + -ing).\n오답 ▶ {1}·{4} spend 시간 뒤엔 -ing {2} good은 형용사 → be동사 {3} '안 쓰는 것이 좋다'로 뜻이 바뀜\n포인트 ▶ not의 위치가 바뀌면 뜻도 바뀜", [('spend', '(시간을) 보내다')])
T.flex('괄호 안의 말을 의미상 주어로 넣어 바르게 다시 쓴 것은?', S, B('It is wise to make your daily plans and try to stick to them. (you)'),
 ['It is wise of you to make your daily plans and try to stick to them.', 'It is wise for you to make your daily plans and try to stick to them.', 'It is wise to make of you your daily plans and try to stick to them.', 'It is wise you to make your daily plans and try to stick to them.', 'It is wise of your to make your daily plans and try to stick to them.'],
 "이유 ▶ wise(성격) → of you, 위치는 to부정사 바로 앞.\n오답 ▶ {1} for ❌ {2} 위치 ❌ {3} 전치사 빠짐 {4} 목적격 you\n포인트 ▶ 형용사 + of/for + 목적격 + to V", [('stick to', '~을 지키다')])
T.flex('다음 대화에서 어법상 <u>어색한</u> 부분을 바르게 고친 것은?', S, B('A: I need to buy a new laptop to finish the project.', "B: Well, it is necessary of you to buy a new laptop, but we don't have enough money at the moment."),
 ['of you → for you', 'necessary → necessarily', 'to buy → buying', "don't → doesn't", 'enough money → money enough'],
 "이유 ▶ necessary는 성격 형용사가 아님 → for you.\n오답 ▶ {1} be동사 뒤 형용사 ✔ {2} 진주어 to buy ✔ {3} 주어 we → don't ✔ {4} enough + 명사 ✔\n포인트 ▶ necessary · important · possible + for", [('laptop', '노트북'), ('at the moment', '지금은')])
T.flex('다음 글의 (A), (B)에 들어갈 말이 바르게 짝지어진 것은?', S, B('It was foolish (A) ' + BL + ' Tom to spend all his money on games. Now it is hard (B) ' + BL + ' him to buy a birthday present for his mom.'),
 ['of − for', 'for − of', 'of − of', 'for − for', 'to − for'],
 "이유 ▶ (A) foolish(어리석은, 성격) → of (B) hard → for\n오답 ▶ (A)에 for · to, (B)에 of가 들어간 보기는 모두 틀림\n포인트 ▶ 한 글 안에서도 형용사마다 for / of가 달라짐", [])
T.flex('다음 중 어법상 올바른 것은?', S, '',
 ['It is important for us to save energy.', 'It was rude for him not to apologize.', 'It is necessary that exercise regularly.', 'That is possible to finish the project in time.', 'It is fun to playing table tennis.'],
 "이유 ▶ important + for us + to save ✔\n오답 ▶ {1} rude(성격) → of him {2} that 뒤 주어 없음 → to exercise {3} 가주어 It {4} to 뒤 동사원형 play\n포인트 ▶ 가주어 · 의미상 주어 · to 뒤 원형을 한 번에 확인", [('save', '아끼다')])
T.flex('다음 우리말을 영어로 바르게 옮긴 것은?', S, B('그녀가 같은 실수를 한 것은 어리석었다.'),
 ['It was silly of her to make the same mistake.', 'It was silly for her to make the same mistake.', 'It is silly of her to make the same mistake.', 'It was silly of her making the same mistake.', 'It was silly her to make the same mistake.'],
 "이유 ▶ silly(어리석은, 성격) → of her, 과거 → was, 진주어 to make.\n오답 ▶ {1} for ❌ {2} 시제 is ❌ {3} 진주어는 to부정사 {4} of 빠짐\n포인트 ▶ 의미상 주어 · 시제 · to부정사 세 가지 확인", [('mistake', '실수')])
T.flex('다음 글의 밑줄 친 do so가 의미하는 것으로 알맞은 것은?', R, B('During this festival, visitors can enjoy various winter sports and Alaskan traditional games. They can also enjoy many special events such as the Running of the Reindeer. People who participate in this race wear fun costumes and try to run faster than reindeer. Is it possible to ' + U('do so') + '? Not really, but it doesn\'t matter.'),
 ['run faster than reindeer', 'wear fun costumes', 'participate in this race', 'enjoy traditional games', 'enjoy winter sports'],
 "이유 ▶ 바로 앞 try to run faster than reindeer → 순록보다 더 빨리 달리는 것이 가능할까? 별로 그렇지 않다.\n오답 ▶ {1}·{2}·{3}·{4} 불가능한 일이 아님 → Not really와 맞지 않음\n포인트 ▶ Is it possible to do so? = 가주어 it + 진주어 to do so", [('various', '다양한'), ('reindeer', '순록')])
T.flex('다음 빈칸에 들어갈 말이 나머지 넷과 <u>다른</u> 것은?', S, '',
 ['It is very kind ' + BL + ' you to say so.', 'It was necessary ' + BL + ' him to get the answer.', 'It is not difficult ' + BL + ' her to win the prize.', 'It is helpful ' + BL + ' me to wear a mask.', 'It is boring ' + BL + ' me to wait for him all day long.'],
 "이유 ▶ kind(친절한, 성격) → of you.\n오답 ▶ {1}~{4} necessary · difficult · helpful · boring → for\n포인트 ▶ 성격 형용사 kind · wise · rude · careless · foolish · silly · honest · generous · clever + of", [('helpful', '도움이 되는')])
T.render()
