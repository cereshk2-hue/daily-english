# 11/17 중산중1 동아(윤정미) 실전 문법(cs) — 명사절 접속사 that · 1·2·3차 (각 20문항)
# 원본: 선생님 학습지 ____That_1.hwp (객관식 + 서술형) — 서술형은 객관식으로 바꾸고, 1차 기본 → 2차 중상 → 3차 상
import sys; sys.path.insert(0, '/home/claude/srcrepo/wrapup')
from wu_m1cs import *
H = ('실전 문법', '중1 영어 동아(윤정미) 접속사 that', '동아(윤정미) 실전 문법', 'm1cs')
B = lambda *ls: BOX('<br>'.join(ls))
NUMS = ['1개', '2개', '3개', '4개', '5개']
t = lambda x: x.replace('[', '<u>').replace(']', '</u>')   # [that] → 밑줄
O_, S_, C_, D_, P_, K_ = '목적어 that', '주어 · 가주어 it', '보어 that', '생략', '쓰임 구별', '위치'
NOTE = '범위: 명사절을 이끄는 접속사 that — 주어(가주어 it) · 목적어 · 보어, 생략 가능한 that, 여러 가지 that의 쓰임. 선택지를 끝까지 읽고 고르세요.'

# ═══════════════ 1차 (기본) ═══════════════
T = Test('1', '1차', '명사절 접속사 that', '접속사 that', NOTE, H=H)
T.flex('다음 빈칸에 들어갈 말로 알맞은 것은?', O_, B('I think ' + BL + ' Korean students respect their teachers.'),
 ['that', 'who', 'which', 'what', 'if'],
 "이유 ▶ think 뒤에 '주어+동사'(Korean students respect)가 완전하게 이어짐 → 목적어 명사절 that.\n오답 ▶ {1}·{2} 관계대명사는 앞에 꾸밀 명사가 필요 {3} what 뒤에는 빠진 자리가 있어야 함 {4} if(~인지)는 think와 쓰지 않음\n포인트 ▶ think / know / believe / hope + (that) 주어 + 동사", [])
T.flex('다음 빈칸에 들어갈 말로 알맞은 것은?', S_, B('It is certain ' + BL + ' she can speak both Chinese and French.'),
 ['that', 'so', 'and', 'while', 'what'],
 "이유 ▶ It(가주어) is certain + that(진주어)절: 그녀가 두 언어를 할 수 있다는 것은 확실하다.\n오답 ▶ {1} so(그래서) {2} and(그리고) {3} while(~하는 동안)은 진주어절을 이끌지 못함 {4} what 뒤는 완전한 문장이 올 수 없음\n포인트 ▶ It is + 형용사 + that ~ = ~라는 것은 …하다", [])
T.fixed('다음 문장에서 that이 들어가기에 가장 알맞은 곳은?', K_, B('Does ( ① ) he ( ② ) know ( ③ ) she ( ④ ) likes ( ⑤ ) him?'),
 None, 3,
 "이유 ▶ know의 목적어 = '그녀가 그를 좋아한다(she likes him)' → know 바로 뒤 ③에 that.\n오답 ▶ ①·② Does he know까지가 주절 ④ she와 likes 사이는 주어-동사를 끊음 ⑤ likes와 him(목적어) 사이 불가\n포인트 ▶ that은 '동사 + [that + 주어 + 동사]' — 두 번째 주어 앞에!", [])
T.flex('다음 밑줄 친 that 중 생략할 수 있는 것은?', D_, '',
 [t('I think [that] I have to write her a letter.'), t('I like [that] pink shirt.'), t('She is looking at [that] dog over there.'), t("Okay, let's do [that]."), t('[That] means "Good luck."')],
 "이유 ▶ think 뒤 목적어절을 이끄는 접속사 that → 생략 가능.\n오답 ▶ {1}·{2} 저(지시형용사, that + 명사) {3} 그것(지시대명사, 목적어) {4} 그것(지시대명사, 주어) → 빼면 문장이 깨짐\n포인트 ▶ 생략 가능 = 동사 뒤 '목적어절'의 접속사 that 뿐", [])
T.flex('다음 중 밑줄 친 that의 쓰임이 어법상 <u>어색한</u> 것은?', P_, '',
 [t("She doesn't know [that] her glasses are."), t('[That] he won the game was true.'), t("I know [that] she doesn't like meat."), t('The rumor is [that] she failed the exam.'), t('The reason for his absence is [that] he is sick.')],
 "이유 ▶ that 뒤에는 '완전한 문장'이 와야 하는데 her glasses are 뒤가 비어 있음 → '어디에 있는지' where her glasses are.\n오답 ▶ {1} 주어절 ✔ {2} 목적어절 ✔ {3}·{4} 보어절 ✔\n포인트 ▶ 접속사 that + 주어 + 동사 + (빠진 것 없는) 완전한 문장", [])
T.flex('다음 중 밑줄 친 that의 쓰임이 나머지 넷과 <u>다른</u> 것은?', P_, '',
 [t('Sumi was so happy at [that] time.'), t('The problem was [that] the library was noisy.'), t('Are you sure [that] he wants to go there?'), t('We know [that] fast food is not good.'), t('She feels [that] she is very lucky.')],
 "이유 ▶ that time = 그때 → that은 '그(지시형용사)'.\n오답 ▶ {1} 보어절 {2} sure 뒤 내용절 {3}·{4} 목적어절 → 모두 '~라는 것' 접속사\n포인트 ▶ that 바로 뒤가 명사 하나(time)면 지시형용사, 주어+동사면 접속사", [])
T.fixed('다음 문장에서 that이 들어가야 할 곳은?', K_, B('An interesting ①fact ②about eating with hands ③is ④they use only the right hand ⑤when they eat.'),
 None, 4,
 "이유 ▶ 주어 An interesting fact about eating with hands + is + 보어절 [that they use ~] → ④.\n오답 ▶ ①~③ 아직 주어 덩어리 ⑤ they use only the right hand 다음은 부사절(when ~)\n포인트 ▶ 주어가 길어도 is 뒤에 '주어+동사'가 오면 보어 that!", [])
T.flex('<보기>의 밑줄 친 that과 쓰임이 같은 것은?', P_, B(t('<보기> Do you know [that] tomorrow is Sunday?')),
 [t("I don't think [that] I should give it to him."), t('[That] is the car I want to buy.'), t("I don't like cream spaghetti [that] much."), t('This is the answer [that] I wrote on the test.'), t('The singer [that] sang this song won the prize.')],
 "이유 ▶ <보기>와 정답 모두 동사(know / think)의 목적어절을 이끄는 접속사.\n오답 ▶ {1} 저것(지시대명사) {2} 그렇게(지시부사, that much) {3}·{4} 앞 명사(answer / singer)를 꾸미는 관계대명사\n포인트 ▶ 동사 + that + 주어 + 동사 = 접속사(~라는 것을)", [])
T.flex('다음 중 밑줄 친 that의 쓰임이 나머지 넷과 <u>다른</u> 것은?', P_, '',
 [t('I want to buy [that] jacket.'), t('I heard [that] you had an accident.'), t('[That] he is honest is certain.'), t("It's true [that] he failed the exam."), t('She realized [that] she must visit him.')],
 "이유 ▶ that jacket = 저 재킷 → 지시형용사.\n오답 ▶ {1}·{4} 목적어절 {2} 주어절 {3} 진주어절 → 모두 접속사\n포인트 ▶ 접속사 that 뒤 = 주어 + 동사 / 지시형용사 that 뒤 = 명사", [])
T.flex('다음 문장과 의미가 같은 것은?', S_, B('That she has a twin sister is interesting.'),
 ['It is interesting that she has a twin sister.', 'It is interesting what she has a twin sister.', 'This is interesting that she has a twin sister.', 'She is interesting that has a twin sister.', 'It is interesting she has a twin sister that.'],
 "이유 ▶ 주어 that절이 길면 맨 앞에 가주어 It을 두고 that절(진주어)을 뒤로 보낸다.\n오답 ▶ {1} what ❌ {2} 가주어는 This가 아니라 It {3} 주어가 바뀌어 뜻이 달라짐 {4} that 위치 ❌\n포인트 ▶ That ~ is 형용사 = It is 형용사 that ~", [])
T.flex('두 문장을 한 문장으로 바르게 바꾼 것은?', S_, B('He lied to me. It is disappointing.'),
 ['It is disappointing that he lied to me.', 'It is disappointing what he lied to me.', 'That is disappointing he lied to me.', 'It is disappointing that lied to me.', 'He is disappointing that lied to me.'],
 "이유 ▶ It(가주어) is disappointing + that he lied to me(진주어).\n오답 ▶ {1} what ❌ {2} 가주어는 It {3} that절에 주어 he가 빠짐 {4} 주어가 바뀌어 뜻이 달라짐\n포인트 ▶ that절 안에도 '주어 + 동사'가 꼭 있어야 한다", [])
T.flex('두 문장을 한 문장으로 바르게 바꾼 것은?', C_, B('Sue lost the key. That is the problem.'),
 ['The problem is that Sue lost the key.', 'The problem is what Sue lost the key.', 'The problem is that lost the key.', 'The problem that is Sue lost the key.', 'The problem is Sue that lost the key.'],
 "이유 ▶ 문제는 ~라는 것이다 → The problem is + that절(보어).\n오답 ▶ {1} what ❌ {2} that절에 주어 Sue가 빠짐 {3} that의 위치가 is 앞 ❌ {4} that은 Sue 앞에\n포인트 ▶ The problem / The point / The truth is that + 주어 + 동사", [])
T.flex('다음 우리말을 영어로 바르게 옮긴 것은?', O_, B('나는 Kim이 지난 일요일에 아주 열심히 공부했다는 것을 안다.'),
 ['I know that Kim studied very hard last Sunday.', 'I know what Kim studied very hard last Sunday.', 'I know that Kim studies very hard last Sunday.', 'I know Kim that studied very hard last Sunday.', 'I know that very hard Kim studied last Sunday.'],
 "이유 ▶ know + that + Kim studied(과거, last Sunday) + very hard.\n오답 ▶ {1} what ❌ {2} last Sunday인데 현재 studies ❌ {3} that은 주어 Kim 앞 {4} very hard는 동사 뒤\n포인트 ▶ that절 동사 시제는 시간 표현(last Sunday)에 맞춘다", [])
T.flex('다음 빈칸에 공통으로 들어갈 말로 알맞은 것은?', O_, B("• She doesn't know " + BL + ' she failed the test.', '• I hope ' + BL + ' it snows this Christmas.'),
 ['that', 'what', 'which', 'who', 'because'],
 "이유 ▶ know / hope 뒤 목적어절을 이끄는 접속사 that.\n오답 ▶ {1} what 뒤는 빠진 자리가 있어야 함 {2}·{3} 꾸밀 명사가 없음 {4} because(~ 때문에)는 know / hope의 목적어가 될 수 없음\n포인트 ▶ hope 뒤는 that절 ⭕ (if절 ❌)", [])
T.flex('다음 밑줄 친 that 중 생략할 수 <u>없는</u> 것은?', D_, '',
 [t('I think [that] man is my homeroom teacher.'), t('I think [that] you are right.'), t('I think [that] she is really nice.'), t('I think [that] shopping is a lot of fun.'), t('I hope [that] we can be good friends.')],
 "이유 ▶ that man = 저 남자(지시형용사) → 빼면 '남자가 담임선생님이다'로 뜻이 바뀜.\n오답 ▶ {1}~{4} think / hope 뒤 목적어절 접속사 → 생략 가능\n포인트 ▶ I think that + 명사 + 동사…: that이 명사를 꾸미면(저 ~) 생략 불가!", [])
T.flex('다음 대화의 빈칸에 들어갈 말로 알맞은 것은? (think, cool 사용)', O_, B('A: What do you think of his style?', 'B: ' + BL),
 ['I think that it is cool.', 'I think what it is cool.', 'I think that is it cool.', 'I think that cool it is.', 'I am think that it is cool.'],
 "이유 ▶ I think + that + 주어(it) + 동사(is) + cool.\n오답 ▶ {1} what ❌ {2}·{3} that절 안은 '주어 + 동사' 순서 {4} be동사와 일반동사 think를 함께 ❌\n포인트 ▶ What do you think of ~? → I think (that) 주어 + 동사", [])
T.flex('다음 괄호 안의 단어를 배열하여 대화를 완성할 때, 네 번째에 오는 단어는?', O_, B('A: What do you think about this camera?', 'B: (that, I, its, simple, is, think, design)'),
 ['its', 'that', 'design', 'is', 'think'],
 "이유 ▶ I think that its design is simple. → I(1) think(2) that(3) its(4) design(5) is(6) simple(7).\n오답 ▶ {1} 3번째 {2} 5번째 {3} 6번째 {4} 2번째\n포인트 ▶ 주어 + think + that + 주어(its design) + 동사(is) + 보어", [])
T.flex('다음 말을 바르게 옮겨 쓴 것은?', O_, B('Jungi: "Ann will get well soon." (believe)'),
 ['Jungi believes that Ann will get well soon.', 'Jungi believe that Ann will get well soon.', 'Jungi believes what Ann will get well soon.', 'Jungi believes that Ann get well soon.', 'Jungi believes Ann that will get well soon.'],
 "이유 ▶ 주어 Jungi(3인칭 단수) → believes + that + Ann will get well soon.\n오답 ▶ {1} 3인칭 단수 -s 빠짐 {2} what ❌ {3} will이 빠짐 {4} that 위치 ❌\n포인트 ▶ 주절 동사 수 일치도 함께 확인!", [])
T.flex('다음 글의 빈칸에 공통으로 들어갈 말로 알맞은 것은?', S_, B("It is a relief " + BL + " we didn't have an accident. I think " + BL + " we should care about our own and others' safety."),
 ['that', 'this', 'what', 'if', 'who'],
 "이유 ▶ 첫 칸: It(가주어) is a relief + that(진주어)절 / 둘째 칸: think + that(목적어)절.\n오답 ▶ {1} this는 절을 이끌지 못함 {2} what 뒤는 불완전해야 함 {3} if는 진주어 · think의 목적어로 쓰지 않음 {4} 꾸밀 사람 명사 없음\n포인트 ▶ 가주어 · 목적어 자리 모두 that", [])
T.flex('다음 우리말을 영어로 바르게 옮긴 것은?', O_, B('나는 그녀가 그 문제를 풀었다고 생각했다.'),
 ['I thought that she solved the problem.', 'I thought what she solved the problem.', 'I think that she solved the problem.', 'I thought that she solves the problem.', 'I thought she that solved the problem.'],
 "이유 ▶ 생각했다(thought) + that + 그녀가 풀었다(she solved).\n오답 ▶ {1} what ❌ {2} '생각했다'인데 think(현재) {3} 주절이 과거면 that절도 과거(solved) {4} that은 주어 she 앞\n포인트 ▶ 주절 과거 → that절도 과거", [])
T.render()

# ═══════════════ 2차 (중상) ═══════════════
T = Test('2', '2차', '명사절 접속사 that', '접속사 that', NOTE, H=H)
T.flex('다음 중 밑줄 친 that의 쓰임이 나머지 넷과 <u>다른</u> 것은?', P_, '',
 [t('Everything [that] you are saying is unbelievable.'), t('We only know [that] they were invented by an Italian.'), t('They think [that] we are a rich family.'), t('The children saw [that] Santa Claus was coming.'), t('Do you know [that] Jack got married?')],
 "이유 ▶ Everything을 뒤에서 꾸미는 관계대명사 that(네가 말하고 있는 모든 것).\n오답 ▶ {1}~{4} know / think / saw / know의 목적어절 접속사\n포인트 ▶ 명사 + that + (목적어 빠진) 절 = 관계대명사", [])
T.fixed('다음 문장에서 that이 생략된 곳은?', K_, B('I ( ① ) think ( ② ) she ( ③ ) can ( ④ ) do ( ⑤ ) the work.'),
 None, 2,
 "이유 ▶ I think [(that) she can do the work] → think 뒤, she 앞 ②.\n오답 ▶ ① 주어와 동사 사이 ③ she와 can 사이 ④·⑤ 동사구 중간\n포인트 ▶ 동사 뒤에 '주어+동사'가 바로 나오면 그 사이에 that이 생략된 것", [])
T.flex('다음 밑줄 친 that 중 생략할 수 <u>없는</u> 것은?', D_, '',
 [t('I think [that] shirt is too expensive to buy.'), t('I hope [that] my pet dog will get better soon.'), t('I hope [that] the news will make her happy.'), t('I think [that] our house is the most beautiful.'), t('I think [that] mom is always kind to me.')],
 "이유 ▶ that shirt = 저 셔츠(지시형용사). 빼면 '셔츠는 너무 비싸다'로 뜻이 달라짐.\n오답 ▶ {1}~{4} 목적어절 접속사 → 생략 가능\n포인트 ▶ that 뒤 명사에 a / the / my가 없으면 지시형용사인지 의심!", [])
T.flex('다음 밑줄 친 that 중 생략할 수 있는 것은?', D_, '',
 [t('I think [that] I should study harder.'), t('I hope [that] boy will get better soon.'), t('[That] is all right.'), t('I want to buy [that] book.'), t('I have a friend [that] cooks well.')],
 "이유 ▶ think 뒤 목적어절 접속사 → 생략 가능.\n오답 ▶ {1} 저 소년(지시형용사) {2} 그것(지시대명사, 주어) {3} 저 책(지시형용사) {4} 주격 관계대명사 → 생략 불가\n포인트 ▶ that 뒤가 '주어+동사'(I should) → 접속사", [])
T.flex('다음 밑줄 친 that의 쓰임이 나머지 넷과 <u>다른</u> 것은?', P_, '',
 [t('I think [that] bulgogi is delicious.'), t('Look at the man [that] is baking cakes.'), t('It is a game [that] is very popular in Korea.'), t('Did you see the man [that] stole the ring?'), t('He was the first man [that] climbed Mt. Everest.')],
 "이유 ▶ think의 목적어절을 이끄는 접속사(that 뒤 완전한 문장).\n오답 ▶ {1}~{4} the man / a game / the first man 뒤 주격 관계대명사(that 뒤 주어 빠짐)\n포인트 ▶ that 뒤에 주어가 있으면 접속사, 없으면 관계대명사", [])
T.flex('<보기>의 밑줄 친 that절과 문장에서 하는 역할이 같은 것은?', C_, B(t('<보기> The reason is [that] I am very tired.')),
 [t('His problem is [that] he is too lazy.'), t('Frank thinks [that] science is interesting.'), t('It is great [that] you are my best friend.'), t('[That] he was very tall is certain.'), t('I hope [that] you are in good health.')],
 "이유 ▶ <보기>와 정답 모두 be동사 뒤 보어 역할(~라는 것이다).\n오답 ▶ {1}·{4} 목적어 {2} 진주어 {3} 주어\n포인트 ▶ 주어 + be동사 + that절 = 보어", [])
T.flex('우리말과 같도록 할 때 빈칸에 들어갈 말로 알맞은 것은?', O_, B('The police ' + BL + ' he was a criminal.', '(경찰은 그가 범인이라고 생각했다.)'),
 ['thought that', 'think that', 'thought what', 'thought it', 'thinks that'],
 "이유 ▶ '생각했다'(과거) → thought + that + 주어 + 동사.\n오답 ▶ {1} 현재 {2} what ❌ {3} it은 절을 이끌지 못함 {4} 현재 + police(복수)인데 thinks\n포인트 ▶ police는 복수 취급 · 시제는 우리말 끝(~했다)으로 확인", [])
T.flex('우리말과 같도록 할 때 빈칸에 들어갈 말로 알맞은 것은?', O_, B("Let's " + BL + " we're flying in the sky now.", '(우리가 지금 하늘을 날고 있다고 상상해 봅시다.)'),
 ['imagine that', 'imagine what', 'imagining that', 'to imagine that', 'imagine it'],
 "이유 ▶ Let's + 동사원형(imagine) + that절.\n오답 ▶ {1} what ❌ {2}·{3} Let's 뒤는 동사원형 {4} it은 절을 이끌지 못함\n포인트 ▶ imagine / guess / say / remember + that절도 가능", [])
T.flex('다음 중 어법상 <u>어색한</u> 문장은?', O_, '',
 ['I think that is she very kind.', "It is strange that they didn't come.", "The point is that we can't wait any longer.", 'I knew that you gave Mike a lot of books.', 'It is a pity that the story had an unhappy ending.'],
 "이유 ▶ that절은 '주어 + 동사' 순서 → I think that she is very kind.\n오답 ▶ {1}·{4} 가주어 It ~ that ✔ {2} 보어절 ✔ {3} 목적어절, 과거-과거 ✔\n포인트 ▶ that절 안은 평서문 어순(의문문처럼 뒤집지 않음)", [])
T.flex('두 문장을 한 문장으로 바르게 바꾼 것은?', S_, B('Giho plays the piano well. It is true.'),
 ['It is true that Giho plays the piano well.', 'That is true Giho plays the piano well.', 'It is true what Giho plays the piano well.', 'Giho is true that plays the piano well.', 'It is true that Giho play the piano well.'],
 "이유 ▶ It(가주어) is true + that Giho plays ~(진주어).\n오답 ▶ {1} 가주어는 It {2} what ❌ {3} 주어가 바뀌어 뜻이 달라짐 {4} Giho(3인칭 단수) → plays\n포인트 ▶ that절 안 수 일치도 확인", [])
T.flex('두 문장을 한 문장으로 바르게 바꾼 것은?', C_, B('Minho broke the window. That is the truth.'),
 ['The truth is that Minho broke the window.', 'The truth is that Minho broken the window.', 'The truth that is Minho broke the window.', 'The truth is what Minho broke the window.', 'Minho is the truth that broke the window.'],
 "이유 ▶ 진실은 ~라는 것이다 → The truth is + that절(보어).\n오답 ▶ {1} broken(과거분사)만으로는 동사 ❌ {2} that 위치 ❌ {3} what ❌ {4} 뜻이 달라짐\n포인트 ▶ break – broke – broken", [])
T.flex('다음 대화의 빈칸에 들어갈 말로 알맞은 것은? (find, fun 사용)', O_, B('A: How does Julia find English?', 'B: ' + BL),
 ['She finds that it is fun.', 'She find that it is fun.', 'She finds what it is fun.', 'She finds that is it fun.', 'She finds it that is fun.'],
 "이유 ▶ She(3인칭 단수) finds + that + it is fun.\n오답 ▶ {1} -s 빠짐 {2} what ❌ {3} that절 어순 ❌ {4} that 위치 ❌\n포인트 ▶ find that ~ = ~라고 생각하다[알게 되다]", [])
T.flex('다음 대화의 빈칸에 들어갈 말로 알맞은 것은?', O_, B('A: Will it rain soon?', 'B: Yes, ' + BL + '. (think)'),
 ['I think that it will rain soon', 'I think that will it rain soon', 'I think what it will rain soon', 'I think that it rain soon', 'I think it that will rain soon'],
 "이유 ▶ I think + that + it will rain soon(평서문 어순).\n오답 ▶ {1} 의문문 어순 ❌ {2} what ❌ {3} will 빠짐 {4} that 위치 ❌\n포인트 ▶ 질문(Will it ~?)을 that절에 넣을 땐 평서문(it will ~)으로", [])
T.flex('<보기>의 밑줄 친 that과 쓰임이 같은 것은?', P_, B(t('<보기> Remember [that] you should solve the problem.')),
 [t('Ted said [that] he lost his house because of the fire.'), t('After [that], we started to work with computers.'), t("I tried to fix the computer, but [that] didn't work at all."), t('The energy [that] is not used is stored as fat.'), t('This sword is for the person [that] can move the rock.')],
 "이유 ▶ <보기>와 정답 모두 동사(remember / said)의 목적어절 접속사.\n오답 ▶ {1}·{2} 그것(지시대명사) {3}·{4} 앞 명사(energy / person)를 꾸미는 관계대명사\n포인트 ▶ that 뒤가 동사(is / can)로 바로 시작하면 관계대명사", [])
T.fixed('<보기>에서 밑줄 친 that을 생략할 수 있는 문장의 개수는?', D_, B(
 t('(a) I know [that] you are diligent.'), t('(b) [That] he has gone is certain.'), t('(c) Who is [that] boy?'), t('(d) I hope [that] you will get better soon.'), t('(e) I want to buy [that] jacket.')),
 NUMS, 2,
 "이유 ▶ 생략 가능: (a)·(d) know / hope 뒤 목적어절 접속사 → 2개.\n오답 ▶ (b) 문장 맨 앞 주어절 that은 생략 불가 (c)·(e) 저(지시형용사)\n포인트 ▶ 주어 자리 That절은 절대 생략 ❌", [])
T.flex('다음 우리말을 영어로 바르게 옮긴 것은?', S_, B('그가 우리를 속였다는 것은 사실이다.'),
 ['It is true that he cheated us.', 'It is true what he cheated us.', 'That is true he cheated us.', 'It is true that cheated he us.', 'He is true that cheated us.'],
 "이유 ▶ 가주어 It + is true + that he cheated us(진주어).\n오답 ▶ {1} what ❌ {2} 가주어는 It {3} that절 어순 ❌ {4} 뜻이 달라짐\n포인트 ▶ ~라는 것은 사실이다 = It is true that ~", [])
T.flex('다음 우리말에 맞게 단어를 배열할 때, 세 번째에 오는 단어는?', O_, B('나는 내가 실수를 했다고 생각했다.', '(thought, made, I, a mistake, that, I)'),
 ['that', 'I', 'made', 'thought', 'a mistake'],
 "이유 ▶ I thought that I made a mistake. → I(1) thought(2) that(3) I(4) made(5) a mistake(6).\n오답 ▶ {1} 1·4번째 {2} 5번째 {3} 2번째 {4} 6번째\n포인트 ▶ 주어 + 동사 + that + 주어 + 동사", [])
T.flex('<보기>와 같이 바꿔 쓸 때 알맞은 것은?', O_, B('<보기> TV is good. Do you think so? → Do you think (that) TV is good?', 'She is beautiful. Do you think so?'),
 ['Do you think that she is beautiful?', 'Do you think that is she beautiful?', 'Do you think what she is beautiful?', 'Are you think that she is beautiful?', 'Does you think that she is beautiful?'],
 "이유 ▶ Do you think + that + she is beautiful(평서문 어순)?\n오답 ▶ {1} that절 어순 ❌ {2} what ❌ {3} 일반동사 think의 의문문은 Do {4} you → Do\n포인트 ▶ Do you think (that) 주어 + 동사 ~?", [])
T.flex('다음 빈칸에 공통으로 들어갈 말로 알맞은 것은?', O_, B('• I think ' + BL + ' this ice cream is so sweet.', '• She hopes ' + BL + ' her mother will get better soon.'),
 ['that', 'to', 'is', 'the', 'it'],
 "이유 ▶ think / hopes 뒤 목적어절을 이끄는 접속사 that.\n오답 ▶ {1} to + 동사원형이 와야 함 {2} 동사 두 개 ❌ {3}·{4} 절을 이끌지 못함\n포인트 ▶ 동사 + ___ + 주어 + 동사 → that", [])
T.flex('다음 중 어법상 올바른 문장은?', O_, '',
 ['I believe that her son is diligent.', 'I believe that diligent her son is.', 'I believe her son that is diligent.', 'I believe what her son is diligent.', 'I believe that her son diligent.'],
 "이유 ▶ believe + that + 주어(her son) + 동사(is) + 보어(diligent).\n오답 ▶ {1} 어순 ❌ {2} that 위치 ❌ {3} what ❌ {4} 동사 is 빠짐\n포인트 ▶ that절에도 동사가 꼭 있어야 한다", [])
T.render()

# ═══════════════ 3차 (상) ═══════════════
T = Test('3', '3차', '명사절 접속사 that', '접속사 that', NOTE, H=H)
T.table('(A)~(C)의 각 네모 안에서 어법에 맞는 표현을 바르게 짝지은 것은?', '종합', B(
 "• It is strange <b>(A)</b> [ that / this ] they didn't come.", "• The problem is <b>(B)</b> [ that / what ] he didn't know how to drive.", '• I thought that <b>(C)</b> [ she / her ] was going to cry.'),
 ['(A)', '(B)', '(C)'], [['that', 'that', 'she'], ['this', 'that', 'she'], ['that', 'what', 'she'], ['that', 'that', 'her'], ['this', 'what', 'her']],
 "이유 ▶ (A) 가주어 It ~ that(진주어) (B) 뒤가 완전한 문장(he didn't know ~) → 보어절 that (C) that절의 주어 자리 → 주격 she\n오답 ▶ this는 절을 이끌지 못함 / what 뒤는 불완전해야 함 / her는 주어 자리 ❌\n포인트 ▶ that 뒤 = 주어(주격) + 동사 + 완전한 문장", [])
T.fixed('다음 <보기>에서 어법상 <u>어색한</u> 문장의 개수는?', '종합', B(
 '(a) I think that she can do the work.', '(b) It is a pity that the story had an unhappy ending.', '(c) The big news is that Tom and Kate got married.', '(d) I hope that he will doing well.', "(e) She doesn't know that her glasses are."),
 NUMS, 2,
 "이유 ▶ 어색한 것 (d)·(e) 2개.\n오답 ▶ (d) will + 동사원형 → will do well (e) 뒤가 불완전 → where her glasses are / (a) 목적어절 ✔ (b) 가주어-진주어 ✔ (c) 보어절 ✔\n포인트 ▶ that절 안도 조동사·어순·완전한 문장을 모두 확인!", [])
T.flex('다음 중 밑줄 친 that의 쓰임이 나머지 넷과 <u>다른</u> 것은?', P_, '',
 [t('The letter [that] came this morning is from my father.'), t('I remember [that] she was always reading something.'), t('The most important thing is [that] he did his best.'), t('[That] the earth is round is common knowledge.'), t('It is common knowledge [that] the earth is round.')],
 "이유 ▶ The letter를 꾸미는 주격 관계대명사(that 뒤에 주어 없이 came).\n오답 ▶ {1} 목적어 {2} 보어 {3} 주어 {4} 진주어 → 모두 명사절 접속사\n포인트 ▶ 명사 + that + 동사… = 관계대명사 / that + 주어 + 동사 = 접속사", [])
T.flex('다음 밑줄 친 that의 쓰임을 <u>잘못</u> 설명한 것은?', P_, '',
 [t('The truth is [that] I forgot to do it. → 목적어'), t('[That] he has gone is certain. → 주어'), t('I know [that] you are diligent. → 목적어'), t('Who is [that] boy? → 지시형용사'), t('This is the best movie [that] I have ever seen. → 관계대명사')],
 "이유 ▶ The truth is 뒤 → be동사의 '보어'(진실은 ~라는 것이다).\n오답 ▶ {1} 주어 ✔ {2} know의 목적어 ✔ {3} 저 소년 ✔ {4} the best movie를 꾸밈 ✔\n포인트 ▶ be동사 뒤 that절 = 보어 / 일반동사 뒤 that절 = 목적어", [], en=False)
T.fixed('다음 문장에서 that이 들어가기에 가장 알맞은 곳은?', K_, B("It ( ① ) is ( ② ) a relief ( ③ ) we ( ④ ) didn't have ( ⑤ ) an accident."),
 None, 3,
 "이유 ▶ It(가주어) is a relief + [that we didn't have an accident](진주어) → ③.\n오답 ▶ ①·② It is a relief까지 주절 ④ 주어 we와 동사 사이 ⑤ 동사와 목적어 사이\n포인트 ▶ 가주어 문장: It is + 형용사/명사 + that + 주어 + 동사", [])
T.fixed('다음 밑줄 친 that 중 생략할 수 있는 것끼리 바르게 짝지은 것은?', D_, B(
 t('(a) I hope [that] it snows this Christmas.'), t('(b) [That] she has a twin sister is interesting.'), t('(c) I think [that] man is my teacher.'), t('(d) He said [that] he was tired.'), t("(e) I don't like it [that] much.")),
 ['(a), (b)', '(a), (d)', '(b), (c)', '(c), (e)', '(d), (e)'], 2,
 "이유 ▶ (a) hope (d) said 뒤 목적어절 접속사 → 생략 가능.\n오답 ▶ (b) 맨 앞 주어절 that ❌ (c) 저 남자(지시형용사) ❌ (e) 그렇게(지시부사) ❌\n포인트 ▶ 생략 가능한 that = 일반동사 뒤 목적어절 접속사", [])
T.flex('다음 대화의 빈칸에 들어갈 말로 알맞은 것은?', O_, B('A: Did you meet her at the party?', 'B: Yes, ' + BL + '. (remember)'),
 ['I remember that I met her at the party', 'I remember that I meet her at the party', 'I remember what I met her at the party', 'I remember that met her at the party', 'I am remember that I met her at the party'],
 "이유 ▶ 파티에서 만난 일(과거) → remember + that + I met her.\n오답 ▶ {1} 과거 일인데 meet {2} what ❌ {3} 주어 I 빠짐 {4} be동사 + 일반동사 ❌\n포인트 ▶ Did you ~? 질문의 시제(과거)를 그대로 받는다", [])
T.flex('다음 중 어법상 올바른 문장은?', O_, '',
 ['I think that he should not watch TV too much.', 'I think that he should not watches TV too much.', 'I think he that should not watch TV too much.', 'I think that should he not watch TV too much.', 'I think what he should not watch TV too much.'],
 "이유 ▶ think + that + he + should not + 동사원형(watch).\n오답 ▶ {1} 조동사 뒤 동사원형 {2} that 위치 ❌ {3} 의문문 어순 ❌ {4} what ❌\n포인트 ▶ 조동사(should / will / can) + 동사원형", [])
T.flex('다음 우리말을 영어로 바르게 옮긴 것은?', C_, B('제일 중요한 것은 그가 최선을 다했다는 것이다.'),
 ['The most important thing is that he did his best.', 'The most important thing is what he did his best.', 'The most important thing that is he did his best.', 'The most important thing is that he does his best.', 'That the most important thing is he did his best.'],
 "이유 ▶ 주어 The most important thing + is + that he did his best(보어, 과거).\n오답 ▶ {1} what ❌ {2} that 위치 ❌ {3} '다했다'(과거)인데 does {4} That이 맨 앞에 와서 문장 구조가 깨짐\n포인트 ▶ 최상급 주어 + is + that절", [])
T.flex('다음 빈칸에 공통으로 들어갈 말로 알맞은 것은?', '종합', B("• I'm sure " + BL + ' he will pass the test.', '• The fact is ' + BL + ' she never gave up.', '• I hope ' + BL + ' you will like it.'),
 ['that', 'if', 'what', 'whether', 'when'],
 "이유 ▶ sure 뒤 내용절 · 보어절 · hope의 목적어절 → 모두 that.\n오답 ▶ {1}·{3} hope 뒤에 if / whether 불가 {2} 뒤가 완전한 문장이라 what ❌ {4} The fact is when ~ 은 뜻이 맞지 않음\n포인트 ▶ 세 칸 모두 들어가는지 하나씩 넣어 보기!", [])
T.flex('다음 문장과 의미가 같은 것은?', S_, B('That the earth is round is common knowledge.'),
 ['It is common knowledge that the earth is round.', 'The earth is common knowledge that is round.', 'It is common knowledge what the earth is round.', 'This is common knowledge that the earth is round.', 'It is common knowledge that the earth round.'],
 "이유 ▶ 주어 that절을 뒤로 → It(가주어) is common knowledge that ~.\n오답 ▶ {1} 뜻이 달라짐 {2} what ❌ {3} 가주어는 It {4} 동사 is 빠짐\n포인트 ▶ That ~ is … = It is … that ~", [])
T.flex('<조건>에 맞게 우리말을 영어로 옮긴 것은?', S_, B('수진이가 곧 회복할 것이라는 것은 확실하다.', '<조건> 가주어 It을 쓸 것'),
 ['It is certain that Sujin will get better soon.', 'That is certain Sujin will get better soon.', 'It is certain that Sujin get better soon.', 'Sujin is certain that will get better soon.', 'It is certain Sujin that will get better soon.'],
 "이유 ▶ It(가주어) is certain + that Sujin will get better soon(진주어).\n오답 ▶ {1} 가주어는 It {2} will 빠짐 · 3인칭 단수 ❌ {3} 주어가 바뀌어 뜻이 달라짐 {4} that 위치 ❌\n포인트 ▶ get better = (병이) 나아지다", [])
T.flex('다음 빈칸에 that이 들어갈 수 <u>없는</u> 것은?', '종합', '',
 ['Do you know ' + BL + ' she lives?', 'I hope ' + BL + ' you will like the gift.', 'The problem is ' + BL + ' we have no time.', 'It is true ' + BL + ' he won the race.', 'She said ' + BL + ' she was hungry.'],
 "이유 ▶ she lives 뒤에 장소가 빠져 있음 → '그녀가 어디에 사는지' where.\n오답 ▶ {1} 목적어 {2} 보어 {3} 진주어 {4} 목적어 → 모두 뒤가 완전한 문장이라 that ✔\n포인트 ▶ that 뒤 = 빠진 것 없는 문장 / 빠진 게 있으면 where · what 등", [])
T.flex('<보기>의 밑줄 친 that과 쓰임이 같은 것은?', P_, B(t("<보기> Who's [that] girl over there?")),
 [t('Do you know [that] song on the radio?'), t('[That] means she will come back.'), t('I hope [that] she will do better next time.'), t("I don't have money [that] much."), t('He is the man [that] I want to talk to.')],
 "이유 ▶ <보기>와 정답 모두 '저, 그 + 명사'(that girl / that song) → 지시형용사.\n오답 ▶ {1} 그것(지시대명사, 주어) {2} 목적어절 접속사 {3} 그렇게(지시부사) {4} 관계대명사\n포인트 ▶ that + 명사 = 지시형용사 / that 혼자 주어·목적어 = 지시대명사", [])
T.flex('다음 밑줄 친 that 중 생략할 수 있는 것은?', D_, '',
 [t('I think [that] the exam was easy.'), t("They won't arrive [that] early."), t('[That] one looks better than this.'), t("He doesn't like her food [that] much."), t('I met [that] woman again this morning.')],
 "이유 ▶ think 뒤 목적어절 접속사 → 생략 가능.\n오답 ▶ {1}·{3} 그렇게(지시부사, that early / that much) {2} 저것(that one) {4} 저 여자(지시형용사)\n포인트 ▶ that + 형용사/부사(early, much) = 그렇게", [])
T.fixed('<보기>의 밑줄 친 that 중 명사절을 이끄는 접속사는 모두 몇 개인가?', P_, B(
 t('(a) I know [that] you are diligent.'), t('(b) Who is [that] boy?'), t('(c) The truth is [that] I forgot to do it.'), t('(d) He is the man [that] I want to talk to.'), t('(e) [That] he has gone is certain.')),
 NUMS, 3,
 "이유 ▶ 명사절 접속사: (a) 목적어 (c) 보어 (e) 주어 → 3개.\n오답 ▶ (b) 지시형용사 (d) the man을 꾸미는 관계대명사\n포인트 ▶ that 뒤가 완전한 문장(주어+동사+…)이면 명사절 접속사", [])
T.flex('다음 대화의 빈칸에 들어갈 말로 알맞은 것은?', C_, B('A: Why is Minsu so upset?', 'B: The reason is ' + BL + '.'),
 ['that his dog is sick', 'what his dog is sick', 'that is his dog sick', 'because of that his dog is sick', 'that sick his dog is'],
 "이유 ▶ The reason is + that + 주어(his dog) + 동사(is) + sick.\n오답 ▶ {1} what ❌ {2} that절 어순 ❌ {3} because of 뒤에는 명사(구)만 → 절과 함께 ❌ {4} 어순 ❌\n포인트 ▶ The reason is that ~ = 이유는 ~ 때문이다", [])
T.flex('다음 말을 바르게 옮겨 쓴 것은?', O_, B('The teacher: "We should visit Ann at the hospital." (think)'),
 ['The teacher thinks that we should visit Ann at the hospital.', 'The teacher think that we should visit Ann at the hospital.', 'The teacher thinks what we should visit Ann at the hospital.', 'The teacher thinks that we visit should Ann at the hospital.', 'The teacher thinks we that should visit Ann at the hospital.'],
 "이유 ▶ The teacher(3인칭 단수) thinks + that + we should visit ~.\n오답 ▶ {1} -s 빠짐 {2} what ❌ {3} 조동사 + 동사원형 순서 ❌ {4} that 위치 ❌\n포인트 ▶ 인용한 말을 that절로 → 주어 + thinks / believes / knows + that ~", [])
T.flex('다음 우리말을 영어로 바르게 옮긴 것은?', O_, B('그녀는 Bob이 아파서 누워 있다고 추측했다.'),
 ['She guessed that Bob was sick in bed.', 'She guessed what Bob was sick in bed.', 'She guessed that Bob is sick in bed.', 'She guessed Bob that was sick in bed.', 'She guess that Bob was sick in bed.'],
 "이유 ▶ 추측했다(guessed) + that + Bob was sick in bed(과거).\n오답 ▶ {1} what ❌ {2} 주절이 과거면 that절도 과거(was) {3} that 위치 ❌ {4} '추측했다'인데 현재 guess\n포인트 ▶ sick in bed = 아파서 누워 있는", [])
T.flex('다음 중 어법상 올바른 문장은?', '종합', '',
 ["The point is that we can't wait any longer.", 'It is exciting what we are going to Jejudo.', "That is strange they didn't come.", 'I knew that you give Mike a lot of books yesterday.', "The fact is that she don't like her new job."],
 "이유 ▶ 보어절 that + we can't wait ~ ✔\n오답 ▶ {1} what → that {2} 가주어는 It {3} yesterday인데 give → gave {4} she → doesn't\n포인트 ▶ 가주어 It · 시제 · 수 일치까지 함께 확인!", [])
T.render()
