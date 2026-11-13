# 11/13 발산중 비상(황종배) 7과 문법 심화 변형 1~5세트 (각 20문항) — 원본: Grammar Build Up 7과 객관식(hwp)
# 문법: Pattern 1 so ~ that …(↔ too ~ to / ~ enough to) · Pattern 2 가주어 it + to부정사(의미상 주어 for / of)
# 원본 유형(쓰임 구별 · 의미 같은 문장 · 영작 · 배열 · 개수 · 짝 고르기)을 살리되 문장·어휘를 바꾸고 난도를 올림 (1세트 중상 → 5세트 최상)
from wu_bs7 import *
H = ('7과 문법 심화', '비상(황종배) Lesson 7 Grammar · so ~ that / 가주어 it', '비상(황종배) 7과 문법', 'bs7')
B = lambda *ls: BOX('<br>'.join(ls))
NUMS = ['1개', '2개', '3개', '4개', '5개']
S_, I_, X_ = 'so ~ that', '가주어 it', '종합'
NOTE = '범위: 7과 문법 — so ~ that …(too ~ to / ~ enough to와 바꿔 쓰기), 가주어 it + to부정사(의미상 주어 for / of). 교재 문제를 바탕으로 문장을 바꾸고 더 어렵게 만들었어요. 문장을 끝까지 읽고 고르세요.'

def Tset(k, lv): return Test(str(k), '%d세트' % k, 'so ~ that · 가주어 it · %s' % lv, '7과 문법', NOTE, H=H)

# ═══════════════ 1세트 (중상) ═══════════════
T = Tset(1, '중상')
T.flex('다음 빈칸에 들어갈 말로 알맞은 것은?', S_, B('The soup was ' + BL + ' hot that I couldn\'t eat it right away.'),
 ['so', 'such', 'very', 'too', 'enough'],
 "이유 ▶ 「so + 형용사 + that + 주어 + 동사」 = 매우 ~해서 …하다. 뒤에 that절이 있으니 so.\n오답 ▶ {1} such는 명사(구) 앞(such a hot soup) {2} very는 that절과 짝이 안 됨 {3} too는 to부정사와 짝(too hot to eat) {4} enough는 형용사 뒤(hot enough to)\n포인트 ▶ so ~ that / too ~ to / ~ enough to 짝을 외우자!", [])
T.flex('다음 문장과 의미가 같은 것은?', S_, B("The box was so heavy that I couldn't lift it."),
 ['The box was too heavy for me to lift.', 'The box was heavy enough for me to lift.', 'The box was so heavy that I could lift it.', 'The box was too heavy for me to lift it.', 'The box was not heavy, so I lifted it.'],
 "이유 ▶ so ~ that + 부정문(couldn't) = too ~ to. 의미상 주어 I → for me.\n오답 ▶ {1}·{2}·{4} 들 수 있다는 뜻(반대) {3} to부정사의 목적어가 문장 주어(The box)와 같으면 it을 다시 쓰지 않는다\n포인트 ▶ so ~ that 주어 can't ⇄ too ~ (for 목적격) to", [])
T.flex('다음 빈칸에 들어갈 말로 알맞은 것은?', I_, B(BL + ' is important to drink enough water every day.'),
 ['It', 'That', 'This', 'What', 'There'],
 "이유 ▶ 진주어 to drink enough water every day를 뒤로 보내고 주어 자리에 가주어 It.\n오답 ▶ {1}·{2} that·this는 가주어로 쓰지 않는다 {3} what은 의문사·관계대명사 {4} There is는 '~이 있다'\n포인트 ▶ It(가주어) ~ to부정사(진주어) — It은 해석하지 않는다", [])
T.flex('다음 빈칸에 들어갈 말로 알맞은 것은?', I_, B('It was very kind ' + BL + ' you to help the old lady.'),
 ['of', 'for', 'to', 'with', 'at'],
 "이유 ▶ kind(친절한)처럼 사람의 성격·태도를 나타내는 형용사 뒤 의미상 주어는 of + 목적격.\n오답 ▶ {1} for는 성격이 아닌 형용사(important, hard 등) 뒤 {2}·{3}·{4} 의미상 주어로 쓰지 않음\n포인트 ▶ 성격 형용사(kind, nice, wise, smart, polite, rude, foolish …) + of", [])
T.flex('다음 빈칸에 들어갈 말로 알맞은 것은?', I_, B('It is hard ' + BL + ' me to wake up early on weekends.'),
 ['for', 'of', 'to', 'with', 'by'],
 "이유 ▶ hard(어려운)는 사람의 성격이 아니므로 의미상 주어는 for + 목적격.\n오답 ▶ {1} of는 성격 형용사 뒤 {2}·{3}·{4} 의미상 주어로 쓰지 않음\n포인트 ▶ 의미상 주어: 대부분 for, 성격 형용사만 of", [])
T.flex('다음 우리말을 바르게 영작한 것은?', S_, B('그 영화는 매우 슬퍼서 나는 울었다.'),
 ['The movie was so sad that I cried.', 'The movie was such sad that I cried.', 'The movie was so sad than I cried.', 'The movie was too sad that I cried.', 'The movie was so sadly that I cried.'],
 "이유 ▶ so + 형용사(sad) + that + 주어 + 동사.\n오답 ▶ {1} such + 형용사만 ❌ {2} than ❌ → that {3} too ~ that ❌ {4} be동사 뒤 보어는 형용사 sad", [])
T.flex('다음 중 밑줄 친 It의 쓰임이 &lt;보기&gt;와 같은 것은?', I_, B('&lt;보기&gt; <u>It</u> is fun to ride a bike along the river.'),
 ['It is dangerous to swim in this lake.', 'It is Monday today.', 'It is my new phone.', 'It was cold last night.', 'It is getting dark outside.'],
 "이유 ▶ &lt;보기&gt;는 가주어 It(진주어 to ride a bike ~). 같은 것은 진주어 to swim ~이 있는 문장.\n오답 ▶ {1}·{3}·{4} 요일·날씨·명암을 나타내는 비인칭 주어 It {2} '그것'을 가리키는 대명사 It\n포인트 ▶ 문장 뒤에 to부정사가 있고 It 자리에 넣을 수 있으면 가주어", [])
T.flex('다음 문장과 의미가 같은 것은?', S_, B('He was so tall that he could reach the top shelf.'),
 ['He was tall enough to reach the top shelf.', 'He was too tall to reach the top shelf.', 'He was enough tall to reach the top shelf.', 'He was so tall to reach the top shelf.', 'He was tall enough reaching the top shelf.'],
 "이유 ▶ so ~ that + 긍정문(could) = 형용사 + enough + to부정사.\n오답 ▶ {1} too ~ to는 '너무 ~해서 …할 수 없다'(반대) {2} enough는 형용사 뒤 {3} so ~ to ❌ {4} enough 뒤 to부정사\n포인트 ▶ so ~ that 주어 can ⇄ 형용사 enough to", [])
T.flex('다음 중 어법상 옳은 문장은?', I_, '',
 ['It is not easy for him to solve the puzzle.', 'It is nice for you to say so.', 'It is important of us to recycle.', 'That is fun to play soccer with friends.', 'It is exciting travel to new places.'],
 "이유 ▶ easy는 성격 형용사가 아니므로 for him ✔, 진주어 to solve ✔\n오답 ▶ {1} nice(성격) → of you {2} important → for us {3} 가주어는 It {4} 진주어는 to travel\n포인트 ▶ 가주어 문장 3점 체크: It? / for·of? / to + 동사원형?", [])
T.flex('다음 중 어법상 <u>어색한</u> 문장은?', S_, '',
 ['She spoke so quiet that nobody heard her.', 'The road was so icy that some cars slid.', 'I was so tired that I fell asleep early.', 'He ran so fast that he caught the bus.', "The bag was so expensive that I didn't buy it."],
 "이유 ▶ 동사 spoke를 꾸미는 부사가 와야 한다 → so quietly.\n오답 ▶ {1}·{2}·{4} be동사 뒤 형용사 ✔ {3} ran을 꾸미는 부사 fast ✔(fast는 형용사·부사 모양이 같음)\n포인트 ▶ so 뒤: be동사 문장이면 형용사, 일반동사 문장이면 부사", [])
T.flex('다음 문장을 가주어 It을 사용하여 바르게 바꾼 것은?', I_, B('To keep a diary every day is difficult.'),
 ['It is difficult to keep a diary every day.', 'It is difficult keep a diary every day.', 'That is difficult to keep a diary every day.', 'It is difficult for keep a diary every day.', 'Difficult is it to keep a diary every day.'],
 "이유 ▶ 주어 To keep ~을 뒤로 보내고 그 자리에 It.\n오답 ▶ {1} 진주어는 to + 동사원형 {2} That ❌ {3} for + 동사원형 ❌ {4} 어순 오류", [])
T.flex('다음 문장의 의미로 가장 알맞은 것은?', S_, B('It rained so heavily that the soccer game was canceled.'),
 ['비가 매우 많이 와서 축구 경기가 취소되었다.', '축구 경기를 취소하기 위해 비가 많이 왔다.', '비가 많이 왔지만 축구 경기는 열렸다.', '축구 경기가 취소되어서 비가 많이 왔다.', '비가 오기 전에 축구 경기가 취소되었다.'],
 "이유 ▶ so ~ that: so 뒤(heavily)가 원인, that절이 결과 → 비가 많이 와서(원인) 경기가 취소됨(결과).\n오답 ▶ {1} 목적(~하기 위해)으로 해석한 함정 {2} 양보(~지만) ❌ {3} 원인·결과가 뒤바뀜 {4} 시간 순서 ❌", [], en=False)
T.table('(A), (B)에 들어갈 말로 바르게 짝지은 것은?', I_, B('• It was careless <b>(A)</b> [ of / for ] him to leave the door open.', '• It is necessary <b>(B)</b> [ of / for ] us to wear a helmet.'),
 ['(A)', '(B)'], [['of', 'for'], ['for', 'for'], ['of', 'of'], ['for', 'of'], ['to', 'for']],
 "이유 ▶ (A) careless(부주의한)는 사람의 태도 → of (B) necessary(필요한)는 성격이 아님 → for\n포인트 ▶ 형용사가 '사람을 평가하는 말'이면 of", [])
T.flex('다음 대화의 빈칸에 들어갈 말로 알맞은 것은?', S_, B("A: Why didn't you finish the book?", 'B: It was ' + BL + ' boring that I stopped reading it.'),
 ['so', 'too', 'very', 'such', 'enough'],
 "이유 ▶ 뒤에 that절(that I stopped reading it) → so ~ that.\n오답 ▶ {1} too는 to부정사와 {2} very는 that절과 짝 ❌ {3} such + (a) 형용사 + 명사 {4} enough는 형용사 뒤", [])
T.fixed('다음 &lt;보기&gt;에서 어법상 <u>틀린</u> 문장의 개수는?', X_, B(
 '(a) It is good for your health to walk every day.', '(b) It was wise for her to save money.', "(c) The water was so cold that we couldn't swim.", "(d) He is too young that he can't drive.", '(e) It is exciting to watch the final game.'),
 NUMS, 2,
 "이유 ▶ 틀린 것 (b)·(d) 2개. (b) wise(현명한, 성격) → of her (d) too ~ that ❌ → so young that he can't drive / too young to drive\n오답 ▶ (a) for your health는 '건강에'라는 부사구, 가주어·진주어 ✔ (c)·(e) ✔", [])
T.flex('다음 우리말과 일치하도록 괄호 안의 단어를 바르게 배열한 것은?', I_, B('우리가 서로 돕는 것은 중요하다. (it, important, for, us, to, help, is, each other)'),
 ['It is important for us to help each other.', 'It is important us for to help each other.', 'It is for us important to help each other.', 'It is important to help for us each other.', 'For us it is to help important each other.'],
 "이유 ▶ It(가주어) + is + important + for us(의미상 주어) + to help each other(진주어).\n포인트 ▶ 의미상 주어 for/of는 to부정사 바로 앞!", [])
T.fixed('다음 중 밑줄 친 that의 쓰임이 나머지 넷과 <u>다른</u> 것은?', X_, B(
 '① He was so sleepy <u>that</u> he went to bed early.', "② The music was so loud <u>that</u> I couldn't hear you.", '③ I know <u>that</u> she likes cats.', '④ It was so windy <u>that</u> the trees shook.', '⑤ The cake was so sweet <u>that</u> nobody finished it.'),
 None, 3,
 "이유 ▶ ③은 know의 목적어가 되는 명사절 접속사 that(~라는 것). 나머지는 so ~ that의 that(결과).\n포인트 ▶ 앞에 so + 형용사/부사가 있는지 확인!", [])
T.flex('다음 문장과 의미가 같은 것은?', S_, B('I was too busy to call you yesterday.'),
 ["I was so busy that I couldn't call you yesterday.", 'I was so busy that I could call you yesterday.', 'I was busy enough to call you yesterday.', 'I was so busy to call you yesterday.', 'I was very busy, so I called you yesterday.'],
 "이유 ▶ too ~ to = so ~ that 주어 can't. 과거이므로 couldn't.\n오답 ▶ {1}·{2}·{4} 전화했다는 뜻(반대) {3} so ~ to ❌", [])
T.flex('다음 문장에서 진주어로 알맞은 것은?', I_, B('It is a good idea to take a short break after studying.'),
 ['to take a short break after studying', 'It', 'a good idea', 'a short break', 'after studying'],
 "이유 ▶ 가주어 It이 가리키는 진짜 주어는 문장 뒤의 to부정사구 전체.\n오답 ▶ {1} 가주어 {2} 보어 {3} to부정사의 목적어 {4} 부사구\n포인트 ▶ 진주어 = to부정사구 '전체'", [])
T.flex('다음 중 어법상 옳은 문장은?', X_, '',
 ['The dog was so smart that it opened the door by itself.', 'It is impossible of me to finish this today.', 'It was so a nice day that we went out.', 'To read comics is fun it.', 'The test was enough easy to pass.'],
 "이유 ▶ so + 형용사(smart) + that + 주어(it) + 동사 ✔\n오답 ▶ {1} impossible → for me {2} so a nice day ❌ → so nice that / such a nice day that {3} it을 뒤에 쓰지 않음 {4} easy enough", [])
T.render()

# ═══════════════ 2세트 (상) ═══════════════
T = Tset(2, '상')
T.flex('다음 빈칸에 공통으로 들어갈 말로 알맞은 것은?', I_, B('• It is generous ' + BL + ' him to share his food.', '• It was silly ' + BL + ' me to believe the rumor.'),
 ['of', 'for', 'to', 'with', 'by'],
 "이유 ▶ generous(너그러운), silly(어리석은) 모두 사람의 성격·태도 → of + 목적격.\n오답 ▶ {1} for는 성격이 아닌 형용사 뒤 {2}·{3}·{4} 의미상 주어로 쓰지 않음", [])
T.flex('다음 빈칸에 공통으로 들어갈 말로 알맞은 것은?', I_, B('• It is difficult ' + BL + ' babies to walk.', '• It was boring ' + BL + ' us to wait in line.'),
 ['for', 'of', 'to', 'with', 'by'],
 "이유 ▶ difficult, boring은 사람의 성격이 아님 → for + 목적격.\n오답 ▶ {1} of는 성격 형용사 뒤 {2}·{3}·{4} 의미상 주어로 쓰지 않음", [])
T.flex('다음 문장과 의미가 같은 것은?', S_, B('She was so brave that she could fight the fire.'),
 ['She was brave enough to fight the fire.', 'She was too brave to fight the fire.', "She was so brave that she couldn't fight the fire.", 'She was enough brave to fight the fire.', 'She was brave so that she could fight the fire.'],
 "이유 ▶ so ~ that 주어 could = 형용사 + enough to.\n오답 ▶ {1}·{2} 할 수 없다는 뜻(반대) {3} enough는 형용사 뒤 {4} so that은 목적(~하기 위해서)", [])
T.flex('다음 중 짝지어진 두 문장의 의미가 서로 <u>다른</u> 것은?', X_, '',
 ['He is too weak to carry the box. = He is so weak that he can carry the box.', "The room was so dark that I couldn't see. = The room was too dark for me to see.",
  'It is fun to play tennis. = To play tennis is fun.', 'She is rich enough to buy the car. = She is so rich that she can buy the car.', 'To swim in the river is dangerous. = It is dangerous to swim in the river.'],
 "이유 ▶ too ~ to = so ~ that 주어 can't. 오른쪽은 can이라 반대.\n오답 ▶ {1} too ~ to ⇄ so ~ that can't ✔ {2}·{4} 진주어 ⇄ 가주어 ✔ {3} enough to ⇄ so ~ that can ✔", [])
T.flex('다음 우리말을 바르게 영작한 것은?', S_, B('그 질문은 매우 어려워서 아무도 그것에 답할 수 없었다.'),
 ['The question was so difficult that nobody could answer it.', 'The question was too difficult that nobody could answer it.', 'The question was so difficult what nobody could answer it.', 'The question was such difficult that nobody could answer it.', 'The question was so difficultly that nobody could answer it.'],
 "이유 ▶ so + 형용사 + that + 주어 + 동사.\n오답 ▶ {1} too ~ that ❌ {2} what ❌ {3} such + 형용사만 ❌ {4} be동사 뒤 형용사", [])
T.flex('다음 중 밑줄 친 It의 쓰임이 &lt;보기&gt;와 같은 것은?', I_, B('&lt;보기&gt; <u>It</u> is rude to talk loudly on the bus.'),
 ['It is a good habit to read every day.', 'It is raining heavily now.', 'It was in the box.', "It is 7 o'clock.", 'It was my brother who called you.'],
 "이유 ▶ &lt;보기&gt;는 가주어 It. 같은 것은 진주어 to read every day가 있는 문장.\n오답 ▶ {1}·{3} 날씨·시간의 비인칭 주어 {2} 대명사 It {4} It ~ who 강조 구문", [])
T.fixed('다음 &lt;보기&gt;에서 어법상 <u>틀린</u> 문장의 개수는?', X_, B(
 '(a) It is polite of you to say thank you.', '(b) It is easy for kids learn new words.', '(c) The street was so crowded that we could hardly walk.', '(d) That is important to protect nature.', '(e) She was so happily that she sang a song.'),
 NUMS, 3,
 "이유 ▶ 틀린 것 (b)·(d)·(e) 3개. (b) 진주어 to learn (d) 가주어 It (e) be동사 뒤 형용사 happy\n오답 ▶ (a) polite(성격) → of ✔ (c) so crowded that ✔", [])
T.table('(A), (B), (C)의 각 네모 안에서 어법에 맞는 표현으로 바르게 짝지은 것은?', X_, B(
 '• The coffee was <b>(A)</b> [ so / too ] hot that I waited for a while.', '• It was clever <b>(B)</b> [ of / for ] her to find the answer.', '• It is not safe <b>(C)</b> [ walking / to walk ] alone at night.'),
 ['(A)', '(B)', '(C)'], [['so', 'of', 'to walk'], ['too', 'of', 'to walk'], ['so', 'for', 'to walk'], ['so', 'of', 'walking'], ['too', 'for', 'walking']],
 "이유 ▶ (A) 뒤에 that절 → so (B) clever(성격) → of (C) 가주어 It의 진주어 → to walk\n오답 ▶ too ~ that ❌ / clever + for ❌ / 진주어 walking ❌", [])
T.flex('다음 중 의미하는 바가 나머지 넷과 <u>다른</u> 것은?', S_, '',
 ['Jake was sick enough to go to school.', 'Jake was too sick to go to school.', "Jake was so sick that he couldn't go to school.", "Jake was sick, so he couldn't go to school.", "Because Jake was sick, he couldn't go to school."],
 "이유 ▶ 나머지는 모두 '아파서 학교에 갈 수 없었다'. sick enough to go는 '갈 만큼 (충분히) 아팠다'로 뜻이 반대.\n포인트 ▶ too ~ to(못 함) ↔ enough to(할 수 있음)", [])
T.fixed('다음 빈칸 ⓐ~ⓓ 중 of가 들어갈 것끼리 바르게 짝지은 것은?', I_, B(
 '• It is foolish ⓐ_____ him to waste money.', '• It is useful ⓑ_____ students to learn coding.', '• It was honest ⓒ_____ her to tell the truth.', '• It is hard ⓓ_____ me to stay calm.'),
 ['ⓐ, ⓑ', 'ⓐ, ⓒ', 'ⓑ, ⓒ', 'ⓑ, ⓓ', 'ⓒ, ⓓ'], 2,
 "이유 ▶ foolish(어리석은)·honest(정직한)는 성격 → of: ⓐ·ⓒ. useful·hard는 for.\n포인트 ▶ 형용사가 '그 사람이 ~하다'로 바뀌면 of(He is foolish. ✔ / He is useful? ✘)", [])
T.flex('다음 두 문장을 가주어 It을 사용하여 한 문장으로 바르게 바꾼 것은?', I_, B('Kids drink milk every day. + It is good.'),
 ['It is good for kids to drink milk every day.', 'It is good of kids to drink milk every day.', 'It is good kids to drink milk every day.', 'It is good for kids drinking milk every day.', 'That is good for kids to drink milk every day.'],
 "이유 ▶ It + is good + for kids(의미상 주어) + to drink ~(진주어).\n오답 ▶ {1} good(좋은, 이로운)은 여기서 성격이 아님 → for {2} for 빠짐 {3} 진주어는 to drink {4} 가주어는 It", [])
T.flex('다음 우리말과 일치하도록 괄호 안의 단어를 바르게 배열한 것은?', S_, B("그는 매우 빨리 말해서 나는 그를 이해할 수 없었다. (so, that, fast, spoke, he, I, couldn't, understand, him)"),
 ["He spoke so fast that I couldn't understand him.", "He spoke fast so that I couldn't understand him.", "He so spoke fast that I couldn't understand him.", "He spoke so that fast I couldn't understand him.", "He spoke that so fast I couldn't understand him."],
 "이유 ▶ 동사 spoke + so + 부사 fast + that + 주어 + 동사.\n오답 ▶ {1} so that은 목적(~하도록) {2}·{3}·{4} 어순 오류", [])
T.flex('다음 대화의 빈칸에 들어갈 말로 알맞은 것은?', S_, B('A: Can you carry this table alone?', "B: No, it's " + BL + ' heavy for me to carry.'),
 ['too', 'so', 'enough', 'such', 'much'],
 "이유 ▶ 「too + 형용사 + for 목적격 + to부정사」 = 너무 ~해서 …가 ~할 수 없다.\n오답 ▶ {1} so는 that절과 {2} enough는 형용사 뒤 {3} such는 명사 앞 {4} much는 형용사 원급을 꾸미지 않음", [])
T.flex('다음 중 어법상 <u>어색한</u> 문장은?', I_, '',
 ['It was nice for you to invite me.', 'It is necessary for us to save energy.', 'It was stupid of me to lose my key.', 'It is fun to learn magic tricks.', 'It is impossible for her to win the race.'],
 "이유 ▶ nice(친절한, 성격) → of you.\n오답 ▶ {1}·{4} necessary·impossible → for ✔ {2} stupid → of ✔ {3} 의미상 주어 없는 가주어 문장 ✔", [])
T.flex('다음 문장과 의미가 같은 것은?', S_, B('This bag is light enough for a child to carry.'),
 ['This bag is so light that a child can carry it.', "This bag is so light that a child can't carry it.", 'This bag is too light for a child to carry.', 'This bag is so light for a child to carry it.', 'This bag is light so that a child could carry it.'],
 "이유 ▶ 형용사 enough to = so ~ that 주어 can. that절 안에서는 목적어 it을 써야 한다.\n오답 ▶ {1}·{2} 들 수 없다는 뜻(반대) {3} so ~ for ~ to ❌ {4} so that은 목적", [])
T.flex('다음 문장과 의미가 같은 것은?', I_, B('To ride a bike without a helmet is dangerous.'),
 ['It is dangerous to ride a bike without a helmet.', 'It is dangerous ride a bike without a helmet.', 'That is dangerous to ride a bike without a helmet.', 'It is dangerous for ride a bike without a helmet.', 'Riding a bike with a helmet is dangerous.'],
 "이유 ▶ 진주어 To ride ~를 뒤로, 가주어 It.\n오답 ▶ {1} to 빠짐 {2} That ❌ {3} for + 동사원형 ❌ {4} without → with로 뜻이 바뀜", [])
T.fixed('다음 중 밑줄 친 so의 쓰임이 나머지 넷과 <u>다른</u> 것은?', S_, B(
 '① I was <u>so</u> tired that I slept all day.', '② The sky was <u>so</u> clear that we saw many stars.', '③ It was late, <u>so</u> I took a taxi.', '④ She sang <u>so</u> well that everyone clapped.', '⑤ The test was <u>so</u> hard that I failed it.'),
 None, 3,
 "이유 ▶ ③의 so는 '그래서'라는 접속사. 나머지는 so ~ that의 so(매우).\n포인트 ▶ so 뒤에 형용사·부사 + that이 오는지 확인!", [])
T.flex('다음 문장과 의미가 같은 것은?', S_, B("It was so foggy that the plane couldn't take off."),
 ['It was too foggy for the plane to take off.', 'It was foggy enough for the plane to take off.', "It was too foggy that the plane couldn't take off.", 'It was so foggy for the plane to take off.', 'It was foggy so that the plane could take off.'],
 "이유 ▶ so ~ that 주어 couldn't = too ~ for 목적격 to.\n오답 ▶ {1} 이륙할 수 있다는 뜻 {2} too ~ that ❌ {3} so ~ for ~ to ❌ {4} so that은 목적", [])
T.flex('다음 우리말을 바르게 영작한 것은?', I_, B('네가 그 아이를 도와준 것은 정말 친절했다.'),
 ['It was really kind of you to help the child.', 'It was really kind for you to help the child.', 'It was really kind of you helping the child.', 'It was really kind of you help the child.', 'That was really kind of you help the child.'],
 "이유 ▶ kind(성격) → of you + to help(진주어).\n오답 ▶ {1} for ❌ {2}·{3} 진주어는 to부정사 {4} That ❌ + to 빠짐", [])
T.fixed('다음 중 어법상 옳은 문장을 모두 고른 것은?', X_, B(
 'ⓐ It is important to be on time.', 'ⓑ The room was so messy that I cleaned it.', 'ⓒ It was brave for him to save the cat.', 'ⓓ He is old enough to drive a car.', "ⓔ The tea was too hot that I couldn't drink it."),
 ['ⓐ, ⓑ', 'ⓑ, ⓒ', 'ⓐ, ⓑ, ⓓ', 'ⓑ, ⓓ, ⓔ', 'ⓐ, ⓒ, ⓔ'], 3,
 "이유 ▶ 옳은 것 ⓐ·ⓑ·ⓓ.\n오답 ▶ ⓒ brave(용감한, 성격) → of him ⓔ too ~ that ❌ → so hot that / too hot to drink\n포인트 ▶ ①은 ⓓ가 빠진 함정 — '모두'를 담은 선택지!", [])
T.render()

# ═══════════════ 3세트 (상) ═══════════════
T = Tset(3, '상')
T.flex('다음 빈칸에 들어갈 말로 알맞은 것은?', S_, B('The puppy was ' + BL + ' cute that everyone wanted to hold it.'),
 ['so', 'such', 'too', 'very', 'enough'],
 "이유 ▶ 형용사 cute + that절 → so ~ that.\n오답 ▶ {1} such a cute puppy that 처럼 명사가 필요 {2} too는 to부정사와 {3} very는 that절과 짝 ❌ {4} cute enough to", [])
T.fixed('다음 중 밑줄 친 It의 쓰임이 나머지 넷과 <u>다른</u> 것은?', I_, B(
 '① <u>It</u> is fun to make cookies.', '② <u>It</u> is wrong to tell lies.', '③ <u>It</u> is sunny and warm today.', '④ <u>It</u> is helpful to take notes in class.', '⑤ <u>It</u> is hard to say goodbye.'),
 None, 3,
 "이유 ▶ ③은 날씨를 나타내는 비인칭 주어 It. 나머지는 진주어 to부정사가 있는 가주어 It.\n포인트 ▶ 뒤에 to부정사가 없으면 가주어가 아니다", [])
T.flex('다음 문장과 의미가 같은 것은?', S_, B('Tom is so smart that he can solve any puzzle.'),
 ['Tom is smart enough to solve any puzzle.', 'Tom is too smart to solve any puzzle.', 'Tom is smart so that he can solve any puzzle.', 'Tom is enough smart to solve any puzzle.', 'Tom is so smart to solve any puzzle.'],
 "이유 ▶ so ~ that 주어 can = 형용사 enough to.\n오답 ▶ {1} 풀 수 없다는 뜻 {2} so that은 목적 {3} enough는 형용사 뒤 {4} so ~ to ❌", [])
T.table('(A), (B)에 들어갈 말로 바르게 짝지은 것은?', I_, B('• It is <b>(A)</b> [ possible / kind ] for him to arrive on time.', '• It was <b>(B)</b> [ careful / difficult ] of you to check the door twice.'),
 ['(A)', '(B)'], [['possible', 'careful'], ['kind', 'careful'], ['possible', 'difficult'], ['kind', 'difficult'], ['necessary', 'important']],
 "이유 ▶ (A) 뒤가 for him → 성격이 아닌 형용사 possible (B) 뒤가 of you → 성격 형용사 careful(조심성 있는)\n오답 ▶ kind는 of와 / difficult는 for와 / important도 for와 짝\n포인트 ▶ for·of를 보고 거꾸로 형용사를 고르는 문제!", [])
T.flex('다음 우리말을 바르게 영작한 것은?', S_, B('이 수학 문제는 내가 풀기에 너무 어렵다.'),
 ['This math problem is too difficult for me to solve.', 'This math problem is too difficult for me to solve it.', 'This math problem is so difficult for me to solve.', 'This math problem is difficult enough for me to solve.', 'This math problem is too difficult of me to solve.'],
 "이유 ▶ too + 형용사 + for 목적격 + to부정사. 문장 주어(problem)가 solve의 목적어이므로 it을 다시 쓰지 않는다.\n오답 ▶ {1} it 중복 {2} so ~ for ~ to ❌ {3} 풀 수 있다는 뜻 {4} difficult → for", [])
T.fixed('다음 &lt;보기&gt;에서 어법상 옳은 문장의 개수는?', X_, B(
 '(a) It is exciting to go camping.', "(b) It was so dark that I couldn't find the switch.", '(c) It is careless for you to forget your homework.', '(d) To exercise regularly is good for you.', '(e) She was enough strong to lift it.', '(f) It is boring for me to watch this show.'),
 NUMS, 4,
 "이유 ▶ 옳은 것 (a)·(b)·(d)·(f) 4개.\n오답 ▶ (c) careless(성격) → of you (e) strong enough", [])
T.table('두 문장을 한 문장으로 바꿀 때, (A), (B), (C)에 들어갈 말로 알맞은 것은?', I_, B('He was rude. + He ignored his teacher.', '→ <b>(A)</b> _____ was rude <b>(B)</b> _____ him <b>(C)</b> _____ his teacher.'),
 ['(A)', '(B)', '(C)'], [['It', 'of', 'to ignore'], ['That', 'of', 'to ignore'], ['It', 'for', 'to ignore'], ['It', 'of', 'ignoring'], ['That', 'for', 'ignore']],
 "이유 ▶ 가주어 It + rude(무례한, 성격) → of him + 진주어 to ignore.\n오답 ▶ That ❌ / for ❌ / 진주어 ignoring ❌", [])
T.flex('다음 중 의미하는 바가 나머지 넷과 <u>다른</u> 것은?', S_, '',
 ['The shoes were big enough for me to wear.', 'The shoes were too small for me to wear.', "The shoes were so small that I couldn't wear them.", "I couldn't wear the shoes because they were too small.", "The shoes were small, so I couldn't wear them."],
 "이유 ▶ 나머지는 '작아서 신을 수 없었다'. 정답은 '신을 수 있을 만큼 컸다'로 반대.\n포인트 ▶ 원인(small)과 결과(couldn't wear)를 함께 확인", [])
T.flex('다음 문장의 의미로 가장 알맞은 것은?', S_, B('She practiced so hard that she won first prize.'),
 ['그녀는 매우 열심히 연습해서 1등 상을 받았다.', '그녀는 1등 상을 받기 위해 열심히 연습했다.', '그녀는 열심히 연습했지만 1등을 하지 못했다.', '그녀는 1등 상을 받아서 열심히 연습했다.', '그녀는 너무 열심히 연습해서 1등을 할 수 없었다.'],
 "이유 ▶ so hard(원인) → that she won(결과).\n오답 ▶ {1} 목적(so that)으로 착각 {2} 양보 ❌ {3} 원인·결과 뒤바뀜 {4} won과 반대", [], en=False)
T.flex('다음 중 어법상 <u>어색한</u> 문장은?', X_, '',
 ['It was so a cold day that we stayed home.', 'It is fun for me to draw cartoons.', 'The film was so long that I got bored.', 'It was wise of him to apologize first.', 'He was too nervous to speak in public.'],
 "이유 ▶ so 뒤에는 형용사·부사만 → It was so cold that ~ / It was such a cold day that ~.\n오답 ▶ {1} fun → for ✔ {2} so long that ✔ {3} wise → of ✔ {4} too ~ to ✔", [])
T.table('다음 대화의 빈칸 (A), (B)에 들어갈 말로 알맞은 것은?', X_, B('A: Is it okay for us to swim here?', 'B: No. The waves are <b>(A)</b> _____ high that <b>(B)</b> _____ is dangerous to swim.'),
 ['(A)', '(B)'], [['so', 'it'], ['too', 'it'], ['so', 'that'], ['such', 'it'], ['very', 'this']],
 "이유 ▶ (A) 뒤에 that절 → so (B) 진주어 to swim의 가주어 → it\n오답 ▶ too ~ that ❌ / 가주어 that·this ❌ / such high ❌", [])
T.flex('다음 문장에서 진주어로 알맞은 것은?', I_, B('It was a great experience for me to travel alone.'),
 ['to travel alone', 'a great experience', 'for me', 'It', 'alone'],
 "이유 ▶ 가주어 It이 가리키는 것은 to travel alone. for me는 의미상 주어.\n오답 ▶ {1} 보어 {2} 의미상 주어 {3} 가주어 {4} 부사", [])
T.flex('다음 문장과 의미가 같은 것은?', S_, B("The ice isn't thick enough to walk on."),
 ['The ice is too thin to walk on.', 'The ice is thick enough to walk on.', 'The ice is so thin that we can walk on it.', 'The ice is too thick to walk on.', 'The ice is not too thin to walk on.'],
 "이유 ▶ 위를 걸을 만큼 두껍지 않다 = 너무 얇아서 걸을 수 없다.\n오답 ▶ {1}·{2}·{4} 걸을 수 있다는 뜻 {3} 너무 두꺼워서 못 걷는다(뜻이 이상함)\n포인트 ▶ not ~ enough to = too (반대말) to", [])
T.flex('다음 우리말을 바르게 영작한 것은?', I_, B('아이들이 혼자 그 강을 건너는 것은 위험하다.'),
 ['It is dangerous for children to cross the river alone.', 'It is dangerous of children to cross the river alone.', 'It is dangerous for children cross the river alone.', 'It is dangerous children to cross the river alone.', 'It is dangerous for children crossing the river alone.'],
 "이유 ▶ dangerous → for children + to cross.\n오답 ▶ {1} of ❌ {2}·{4} 진주어는 to부정사 {3} for 빠짐", [])
T.flex('다음 중 밑줄 친 that의 쓰임이 &lt;보기&gt;와 같은 것은?', S_, B('&lt;보기&gt; He was so angry <u>that</u> he left the room.'),
 ['The book was so popular that it sold out quickly.', 'I think that he is right.', 'This is the house that Jack built.', 'She saved money so that she could buy a bike.', 'It is true that he won the race.'],
 "이유 ▶ &lt;보기&gt;는 so ~ that(결과)의 that.\n오답 ▶ {1} 명사절 접속사 {2} 관계대명사 {3} so that(목적: ~하기 위해서) {4} 가주어 It의 진주어 that절", [])
T.flex('다음 중 짝지어진 두 문장의 의미가 서로 <u>다른</u> 것은?', X_, '',
 ['The movie was so boring that I fell asleep. = The movie was too boring for me to fall asleep.', 'It is fun to play with friends. = Playing with friends is fun.',
  'The rope was strong enough to hold him. = The rope was so strong that it could hold him.', 'It was kind of her to help me. = She was kind to help me.', "I was too full to eat dessert. = I was so full that I couldn't eat dessert."],
 "이유 ▶ 왼쪽은 '지루해서 잠들었다', 오른쪽은 too ~ to라서 '너무 지루해서 잠들 수 없었다'로 반대.\n오답 ▶ {1} 진주어 to부정사 = 동명사 주어 ✔ {2}·{4} ✔ {3} It is kind of A to ~ = A is kind to ~ ✔", [])
T.flex('다음 빈칸에 공통으로 들어갈 말로 알맞은 것은?', I_, B('• ' + BL + ' is not easy to make new friends.', '• ' + BL + ' was raining all day yesterday.'),
 ['It', 'That', 'This', 'There', 'What'],
 "이유 ▶ 첫 문장은 가주어 It, 둘째 문장은 날씨의 비인칭 주어 It — 둘 다 It.\n포인트 ▶ 쓰임은 다르지만 모양은 같은 It", [])
T.flex('다음 빈칸에 들어갈 말로 알맞은 것은?', S_, B('The music was so loud that I ' + BL + ' sleep last night.'),
 ["couldn't", "can't", "won't", "don't", "am not"],
 "이유 ▶ 과거(was, last night) + '너무 시끄러워서 잘 수 없었다' → couldn't.\n포인트 ▶ that절의 시제는 주절과 맞춘다", [])
T.flex('다음 중 어법상 옳은 문장은?', X_, '',
 ['It was generous of them to donate their time.', 'It is easy of me to cook ramen.', 'The bag is too heavy for me to carry it.', 'It is important protect your eyes.', "The ground was so wet what we couldn't play."],
 "이유 ▶ generous(성격) → of them + to donate ✔\n오답 ▶ {1} easy → for {2} it 중복 {3} to protect {4} what → that", [])
T.flex('다음 우리말을 바르게 영작한 것은?', S_, B('그 개는 너무 피곤해서 걸을 수 없었다.'),
 ['The dog was too tired to walk.', 'The dog was so tired that it could walk.', 'The dog was tired enough to walk.', "The dog was too tired that it couldn't walk.", 'The dog was so tired to walk.'],
 "이유 ▶ too + 형용사 + to부정사 = 너무 ~해서 …할 수 없다.\n오답 ▶ {1}·{2} 걸을 수 있다는 뜻 {3} too ~ that ❌ {4} so ~ to ❌", [])
T.render()

# ═══════════════ 4세트 (최상) ═══════════════
T = Tset(4, '최상')
T.fixed('다음 &lt;보기&gt;에서 어법상 <u>틀린</u> 문장의 개수는?', X_, B(
 '(a) It is natural for babies to cry at night.', '(b) It was thoughtful for you to bring flowers.', '(c) The sun was so bright that I wore sunglasses.', '(d) The river was too deep for us to cross it.', '(e) To be honest is important.', '(f) He was so busily that he skipped lunch.'),
 NUMS, 3,
 "이유 ▶ 틀린 것 (b)·(d)·(f) 3개. (b) thoughtful(사려 깊은, 성격) → of you (d) it 중복(The river가 cross의 목적어) (f) be동사 뒤 형용사 busy\n오답 ▶ (a) natural → for ✔ (c)·(e) ✔", [])
T.fixed('다음 중 어법상 옳은 문장끼리 바르게 짝지은 것은?', X_, B(
 'ⓐ It is fun for us to sing together.', 'ⓑ The box was strong enough to hold the books.', 'ⓒ It was smart for him to choose that answer.', 'ⓓ The road was so slippery that we drove slowly.', 'ⓔ It is hard to me to say no.'),
 ['ⓐ, ⓑ', 'ⓒ, ⓔ', 'ⓐ, ⓑ, ⓒ', 'ⓐ, ⓑ, ⓓ', 'ⓑ, ⓓ, ⓔ'], 4,
 "이유 ▶ 옳은 것 ⓐ·ⓑ·ⓓ.\n오답 ▶ ⓒ smart(성격) → of him ⓔ to me ❌ → for me", [])
T.flex('다음 중 짝지어진 두 문장의 의미가 서로 <u>다른</u> 것은?', X_, '',
 ['She is too shy to sing in public. = She is so shy that she can sing in public.', 'It is necessary to wear a seat belt. = To wear a seat belt is necessary.',
  'He is strong enough to move the rock. = He is so strong that he can move the rock.', 'It was silly of me to say that. = I was silly to say that.', "The soup was too salty for me to eat. = The soup was so salty that I couldn't eat it."],
 "이유 ▶ too ~ to = so ~ that 주어 can't. 오른쪽은 can이라 반대.\n오답 ▶ {1}·{2}·{3}·{4} 모두 같은 뜻으로 바르게 바꿈", [])
T.fixed('다음 빈칸에 들어갈 말이 나머지 넷과 <u>다른</u> 것은?', I_, B(
 '① It is very kind _____ you to say so.', '② It was brave _____ him to jump into the water.', '③ It is impossible _____ us to win the game.', '④ It was polite _____ her to wait for us.', '⑤ It is wise _____ you to save money.'),
 None, 3,
 "이유 ▶ ③ impossible은 성격 형용사가 아님 → for. 나머지 kind·brave·polite·wise는 성격 → of.", [])
T.flex('다음 문장과 의미가 같은 것은?', S_, B('The test was so easy that all the students could pass it.'),
 ['The test was easy enough for all the students to pass.', 'The test was too easy for all the students to pass.', 'The test was easy enough for all the students to pass it.', 'The test was so easy for all the students to pass.', 'The test was easy so that all the students could pass it.'],
 "이유 ▶ so ~ that 주어 could = 형용사 enough for 목적격 to. 문장 주어(test)가 pass의 목적어이므로 it을 쓰지 않는다.\n오답 ▶ {1} 통과할 수 없다는 뜻 {2} it 중복 {3} so ~ for ~ to ❌ {4} so that은 목적", [])
T.flex('다음 두 문장을 한 문장으로 바르게 바꾼 것은?', S_, B("Mina was so tired. + She couldn't do her homework."),
 ['Mina was too tired to do her homework.', 'Mina was tired enough to do her homework.', 'Mina was so tired that she could do her homework.', "Mina was too tired that she couldn't do her homework.", 'Mina was so tired to do her homework.'],
 "이유 ▶ 너무 피곤해서(원인) 숙제를 할 수 없었다(결과) → too ~ to.\n오답 ▶ {1}·{2} 할 수 있다는 뜻 {3} too ~ that ❌ {4} so ~ to ❌", [])
T.flex('다음 중 어법상 옳은 문장은?', X_, '',
 ["It is not easy for me to understand his jokes.", 'It was nice for her to visit me.', 'The coffee was too hot for me to drink it.', 'He was enough brave to tell the truth.', 'That is fun to learn a new sport.'],
 "이유 ▶ easy → for me + to understand ✔\n오답 ▶ {1} nice → of her {2} it 중복 {3} brave enough {4} 가주어 It", [])
T.fixed('다음 중 밑줄 친 It이 가주어로 쓰인 것끼리 바르게 짝지은 것은?', I_, B(
 'ⓐ <u>It</u> is cold outside.', 'ⓑ <u>It</u> is fun to swim in the sea.', 'ⓒ <u>It</u> is my umbrella.', 'ⓓ <u>It</u> is important to keep promises.', 'ⓔ <u>It</u> is Sunday today.'),
 ['ⓐ, ⓔ', 'ⓑ, ⓓ', 'ⓒ, ⓓ', 'ⓐ, ⓑ', 'ⓒ, ⓔ'], 2,
 "이유 ▶ 진주어 to부정사가 있는 ⓑ·ⓓ가 가주어 It.\n오답 ▶ ⓐ·ⓔ 날씨·요일의 비인칭 주어(①은 비인칭끼리 짝지은 함정) ⓒ 대명사", [])
T.flex('다음 중 의미하는 바가 나머지 넷과 <u>다른</u> 것은?', S_, '',
 ['It was cold enough for us to go out.', 'It was too cold for us to go out.', "It was so cold that we couldn't go out.", "We couldn't go out because it was very cold.", "Because of the cold weather, we couldn't go out."],
 "이유 ▶ 나머지는 '추워서 나갈 수 없었다'. 정답은 '나갈 수 있을 만큼 추웠다'로 결과가 반대.", [])
T.table('다음 대화의 (A), (B)에 들어갈 말로 알맞은 것은?', S_, B("A: Why don't you buy that jacket?", "B: It's <b>(A)</b> [ so / too / enough ] expensive <b>(B)</b> [ that I / for me to ] buy."),
 ['(A)', '(B)'], [['too', 'for me to'], ['so', 'for me to'], ['too', 'that I'], ['so', 'that I'], ['enough', 'for me to']],
 "이유 ▶ 뒤에 동사원형 buy만 있으므로 for me to + 동사원형 → too expensive for me to buy(너무 비싸서 살 수 없다).\n오답 ▶ so ~ for ~ to ❌ / too ~ that ❌ / so expensive that I buy는 '비싸서 산다'로 흐름에 맞지 않고 can't가 필요 / enough는 형용사 뒤", [])
T.flex('다음 우리말을 바르게 영작한 것은?', S_, B('그 책은 매우 재미있어서 나는 하룻밤에 그것을 다 읽었다.'),
 ['The book was so interesting that I read it all in one night.', 'The book was too interesting to read it all in one night.', 'The book was so interested that I read it all in one night.', 'The book was so interesting for me to read it all in one night.', 'The book was such interesting that I read it all in one night.'],
 "이유 ▶ so + interesting(흥미를 주는) + that + 주어 + 동사.\n오답 ▶ {1} too ~ to는 '읽을 수 없었다'(반대) {2} 책이 흥미를 '느끼는' 게 아님 → interesting {3} so ~ for ~ to ❌ {4} such + 형용사만 ❌", [])
T.flex('다음 중 가주어 It을 사용하여 바꿔 쓴 문장이 <u>틀린</u> 것은?', I_, '',
 ['To fix this machine is hard for me. → It is hard of me to fix this machine.', 'To wear a mask is helpful. → It is helpful to wear a mask.', 'To stay up late is bad for you. → It is bad for you to stay up late.',
  'To learn history is interesting. → It is interesting to learn history.', 'To travel by train is fun. → It is fun to travel by train.'],
 "이유 ▶ hard는 성격 형용사가 아님 → It is hard for me to fix this machine.\n오답 ▶ {1}·{2}·{3}·{4} 모두 바르게 바꿈", [])
T.flex('다음 빈칸에 들어갈 말로 알맞은 것은?', S_, B('The bus was so crowded that I ' + BL + ' get on it.'),
 ["couldn't", 'could', 'can', "don't", "mustn't"],
 "이유 ▶ 너무 붐벼서(원인) 탈 수 없었다(결과), 과거 → couldn't.\n오답 ▶ {1}·{2} 탈 수 있었다는 뜻 {3} 시제·의미 ❌ {4} '타면 안 된다'(금지)", [])
T.fixed('다음 문장에서 for us가 들어갈 위치로 알맞은 곳은?', I_, B('It is ( ① ) necessary ( ② ) to ( ③ ) protect ( ④ ) the environment ( ⑤ ).'),
 None, 2,
 "이유 ▶ 의미상 주어는 to부정사 바로 앞 → It is necessary for us to protect the environment.", [])
T.flex('다음 문장과 의미가 같은 것은?', S_, B('The water is warm enough for the baby to take a bath in.'),
 ['The water is so warm that the baby can take a bath in it.', "The water is so warm that the baby can't take a bath in it.", 'The water is too warm for the baby to take a bath in.', 'The water is so warm for the baby to take a bath in it.', 'The water is warm so that the baby could take a bath in it.'],
 "이유 ▶ 형용사 enough for 목적격 to = so ~ that 주어 can. that절에는 목적어 it이 필요(in it).\n오답 ▶ {1}·{2} 목욕할 수 없다는 뜻 {3} so ~ for ~ to ❌ {4} so that은 목적", [])
T.fixed('다음 중 밑줄 친 that의 쓰임이 나머지 넷과 <u>다른</u> 것은?', S_, B(
 '① The room was so quiet <u>that</u> I could hear the clock.', "② I was so excited <u>that</u> I couldn't sleep.", '③ It was so hot <u>that</u> we went swimming.', '④ He worked hard so <u>that</u> he could pass the test.', '⑤ She spoke so softly <u>that</u> nobody heard her.'),
 None, 4,
 "이유 ▶ ④는 so that(~하기 위해서, 목적). 나머지는 so + 형용사/부사 + that(결과).\n포인트 ▶ so와 that 사이에 형용사·부사가 있는가? 없으면 목적의 so that", [])
T.fixed('다음 &lt;보기&gt;에서 어법상 옳은 문장의 개수는?', X_, B(
 '(a) It is exciting for me to meet new people.', '(b) It was foolish of him to trust the stranger.', '(c) The cake was so delicious that I had another piece.', '(d) It is necessary of you to wear a uniform.', '(e) The question was too hard for me to answer it.'),
 NUMS, 3,
 "이유 ▶ 옳은 것 (a)·(b)·(c) 3개.\n오답 ▶ (d) necessary → for you (e) it 중복", [])
T.flex('다음 문장과 의미가 같은 것은?', I_, B('It was very generous of Kate to share her umbrella.'),
 ['Kate was very generous to share her umbrella.', 'It was very generous for Kate to share her umbrella.', 'Kate was too generous to share her umbrella.', 'Kate shared her umbrella because she was not generous.', 'Sharing her umbrella was not generous of Kate.'],
 "이유 ▶ It is 성격 형용사 of A to ~ = A is 성격 형용사 to ~.\n오답 ▶ {1} generous → of {2} '너무 너그러워서 나누지 못했다'(이상한 뜻) {3}·{4} 뜻이 반대", [])
T.flex('다음 우리말을 바르게 영작한 것은?', I_, B('그가 그렇게 말한 것은 무례했다.'),
 ['It was rude of him to say so.', 'It was rude for him to say so.', 'That was rude of him say so.', 'It was rude of him saying so.', 'It was rudely of him to say so.'],
 "이유 ▶ rude(성격) → of him + to say.\n오답 ▶ {1} for ❌ {2} That ❌ + to 빠짐 {3} 진주어는 to부정사 {4} be동사 뒤 형용사 rude", [])
T.flex('다음 문장의 의미로 가장 알맞은 것은?', X_, B('It was so windy that it was hard for us to open the umbrella.'),
 ['바람이 매우 많이 불어서 우리가 우산을 펴기가 어려웠다.', '우산을 펴기 위해 바람이 많이 불었다.', '바람이 불었지만 우리는 쉽게 우산을 폈다.', '우산을 펴서 바람이 많이 불었다.', '바람이 너무 많이 불어서 우리는 우산을 펼 필요가 없었다.'],
 "이유 ▶ so windy that(원인 → 결과) + 결과 안에 가주어 it ~ for us to open(우리가 우산을 펴는 것은 어려웠다).\n오답 ▶ {1} 목적 ❌ {2} 양보 ❌ {3} 원인·결과 뒤바뀜 {4} hard(어려운) ≠ 필요 없다", [], en=False)
T.render()

# ═══════════════ 5세트 (최상 · 종합) ═══════════════
T = Tset(5, '최상')
T.table('다음 빈칸 ⓐ, ⓑ에 들어갈 말이 차례대로 짝지어진 것은?', X_, B('The test was ⓐ _____ difficult that ⓑ _____ was hard to finish it on time.'),
 ['ⓐ', 'ⓑ'], [['so', 'it'], ['too', 'it'], ['so', 'that'], ['very', 'it'], ['such', 'this']],
 "이유 ▶ ⓐ 뒤에 that절 → so ⓑ 진주어 to finish의 가주어 → it\n오답 ▶ too ~ that ❌ / 가주어 that·this ❌ / very는 that절과 짝 ❌", [])
T.fixed('다음 &lt;보기&gt;에서 어법상 옳은 문장의 개수는?', X_, B(
 '(a) It is important for us to listen carefully.', '(b) It was silly of me to forget my bag.', '(c) The movie was so scary that I closed my eyes.', '(d) The box was too small to put all the toys in.', '(e) It is easy for him solve the problem.', '(f) She is enough tall to be a model.'),
 NUMS, 4,
 "이유 ▶ 옳은 것 (a)·(b)·(c)·(d) 4개. (d) 주어 box가 put ~ in의 목적어 → in 뒤에 it을 쓰지 않은 것이 맞다.\n오답 ▶ (e) to solve (f) tall enough", [])
T.flex('다음 중 짝지어진 두 문장의 의미가 서로 <u>다른</u> 것은?', X_, '',
 ["It was so noisy that I couldn't focus. = It was noisy enough for me to focus.", 'To walk in the rain is fun. = It is fun to walk in the rain.',
  "The bread is so big that it covers my aunt's shoulder. = The bread is big enough to cover my aunt's shoulder.", 'It was kind of you to wait for me. = You were kind to wait for me.', "The puzzle was too hard for me to solve. = The puzzle was so hard that I couldn't solve it."],
 "이유 ▶ 왼쪽은 '시끄러워서 집중할 수 없었다', 오른쪽 enough to는 '집중할 수 있을 만큼'으로 반대(too noisy for me to focus여야 함).\n오답 ▶ {1}·{3} ✔ {2} so ~ that 긍정 = enough to(교과서 문장) ✔ {4} ✔", [])
T.flex('다음 중 밑줄 친 It의 쓰임이 &lt;보기&gt;와 같은 것은?', I_, B('&lt;보기&gt; <u>It</u> is always good to get together. (교과서 문장)'),
 ['It is helpful to share ideas with others.', 'It was snowing all night.', 'It is on the table.', 'It is far from here to the station.', 'It was Jim that broke the vase.'],
 "이유 ▶ &lt;보기&gt;는 가주어 It(진주어 to get together).\n오답 ▶ {1}·{3} 날씨·거리의 비인칭 주어 {2} 대명사 {4} It ~ that 강조 구문", [])
T.flex('다음 교과서 문장의 의미로 가장 알맞은 것은?', S_, B("The bread is so big that it covers my aunt's shoulder."),
 ['그 빵은 매우 커서 이모의 어깨를 덮는다.', '이모의 어깨를 덮기 위해 빵이 커졌다.', '빵이 너무 커서 이모의 어깨를 덮을 수 없다.', '빵은 이모의 어깨만큼 크지 않다.', '빵이 이모의 어깨를 덮어서 커 보인다.'],
 "이유 ▶ so big(원인) → that it covers ~(결과).\n오답 ▶ {1} 목적 ❌ {2} too ~ to처럼 해석한 함정 {3} 비교 ❌ {4} 원인·결과 뒤바뀜", [], en=False)
T.flex('다음 중 어법상 <u>틀린</u> 문장은?', I_, '',
 ['It is careful for you to check your answers.', 'It is wise of her to choose that school.', 'It is useful for students to learn coding.', 'The street was so dark that I used my phone light.', 'This tea is too hot for me to drink.'],
 "이유 ▶ careful(조심성 있는)은 사람의 태도 → of you.\n오답 ▶ {1} wise → of ✔ {2} useful → for ✔ {3} so dark that ✔ {4} too hot for me to drink(목적어 생략) ✔", [])
T.flex('다음 우리말과 일치하도록 괄호 안의 단어를 바르게 배열한 것은?', I_, B('그가 진실을 말한 것은 정직했다. (him, it, of, to, was, honest, tell, the truth)'),
 ['It was honest of him to tell the truth.', 'It was honest for him to tell the truth.', 'It was of him honest to tell the truth.', 'It was honest to him of tell the truth.', 'Honest it was of him to tell the truth.'],
 "이유 ▶ It was + honest + of him + to tell the truth.\n오답 ▶ {1} 주어진 단어에 for가 없고, honest는 of와 짝 {2}·{3}·{4} 어순 오류", [])
T.flex('다음 문장과 의미가 같은 것은?', S_, B("The shelf is so high that she can't reach it."),
 ['The shelf is too high for her to reach.', 'The shelf is too high for her to reach it.', 'The shelf is high enough for her to reach.', 'The shelf is too high of her to reach.', 'The shelf is so high for her to reach.'],
 "이유 ▶ so ~ that 주어 can't = too ~ for 목적격 to. shelf가 reach의 목적어 → it을 쓰지 않는다.\n오답 ▶ {1} it 중복 {2} 닿을 수 있다는 뜻 {3} of ❌ {4} so ~ for ~ to ❌", [])
T.fixed('다음 중 밑줄 친 It의 쓰임이 나머지 넷과 <u>다른</u> 것은?', I_, B(
 '① <u>It</u> is fun to bake bread.', '② <u>It</u> is not safe to swim here.', '③ <u>It</u> is very far to the beach.', '④ <u>It</u> is hard to choose just one.', '⑤ <u>It</u> is kind of you to help me.'),
 None, 3,
 "이유 ▶ ③은 거리를 나타내는 비인칭 주어 It(to the beach는 to부정사가 아니라 '해변까지'). 나머지는 가주어 It.\n포인트 ▶ to 뒤에 동사원형이 오는지 확인!", [])
T.flex('다음 우리말을 바르게 영작한 것은?', I_, B('학생들이 매일 운동하는 것은 필요하다.'),
 ['It is necessary for students to exercise every day.', 'It is necessary of students to exercise every day.', 'It is necessary for students exercising every day.', 'It is necessary students to exercise every day.', 'It is necessary for students exercise every day.'],
 "이유 ▶ necessary → for students + to exercise.\n오답 ▶ {1} of ❌ {2}·{4} 진주어는 to부정사 {3} for 빠짐", [])
T.flex('다음 중 어법상 옳은 문장은?', X_, '',
 ['The dress was so beautiful that she bought it right away.', 'It was so cold day that we stayed inside.', 'It was silly for him to cry over it.', 'The car was enough fast to win the race.', 'It is fun of me to ride a bike.'],
 "이유 ▶ so + 형용사 + that + 주어 + 동사 ✔\n오답 ▶ {1} so cold day ❌ → so cold that / such a cold day that {2} silly → of {3} fast enough {4} fun → for", [])
T.flex('다음 중 의미하는 바가 나머지 넷과 <u>다른</u> 것은?', S_, '',
 ['I was excited enough to sleep well.', 'I was too excited to sleep.', "I was so excited that I couldn't sleep.", "I couldn't sleep because I was very excited.", "Because of my excitement, I couldn't sleep."],
 "이유 ▶ 나머지는 '너무 신나서 잘 수 없었다'. 정답은 '잘 잘 만큼 신났다'로 반대.", [])
T.fixed('다음 빈칸에 of가 들어가는 것의 개수는?', I_, B(
 '(a) It is clever _____ her to use the map.', '(b) It is possible _____ us to finish early.', '(c) It was rude _____ him to shout at the waiter.', '(d) It is fun _____ me to dance.', '(e) It was nice _____ you to call me.'),
 NUMS, 3,
 "이유 ▶ of: (a) clever · (c) rude · (e) nice 3개(성격 형용사). (b) possible · (d) fun은 for.", [])
T.flex('다음 문장의 의미로 가장 알맞은 것은?', S_, B('He is too young to watch the movie.'),
 ['그는 너무 어려서 그 영화를 볼 수 없다.', '그는 그 영화를 볼 만큼 충분히 나이가 들었다.', '그는 그 영화를 보기 위해 어려 보인다.', '그는 어리지만 그 영화를 볼 수 있다.', '그 영화는 너무 어려워서 볼 수 없다.'],
 "이유 ▶ too + 형용사 + to부정사 = 너무 ~해서 …할 수 없다.\n오답 ▶ {1} enough to의 뜻 {2} 목적 ❌ {3} 양보 ❌ {4} young(어린)을 difficult로 착각", [], en=False)
T.flex('다음 빈칸에 들어갈 말로 알맞은 것은?', S_, B('She sang so ' + BL + ' that everyone in the hall cried.'),
 ['beautifully', 'beautiful', 'beauty', 'more beautiful', 'beautify'],
 "이유 ▶ 일반동사 sang을 꾸미는 부사 → beautifully.\n오답 ▶ {1} 형용사(be동사 뒤에 쓰임) {2} 명사 {3} 비교급 형용사 {4} 동사", [])
T.flex('다음 문장에서 It이 가리키는 것으로 알맞은 것은?', I_, B('It is a good habit to eat breakfast every day.'),
 ['to eat breakfast every day', 'a good habit', 'breakfast', 'every day', 'a habit'],
 "이유 ▶ 가주어 It = 진주어 to eat breakfast every day(아침을 먹는 것).\n오답 ▶ {1}·{4} 보어 {2} 목적어 {3} 부사구", [])
T.table('다음 대화의 (A), (B)에 들어갈 말로 알맞은 것은?', X_, B('A: Was it hard <b>(A)</b> [ for / of ] you to move the sofa?', 'B: Yes. It was <b>(B)</b> [ so / too ] heavy that I needed help.'),
 ['(A)', '(B)'], [['for', 'so'], ['of', 'so'], ['for', 'too'], ['of', 'too'], ['to', 'so']],
 "이유 ▶ (A) hard → for (B) 뒤에 that절 → so\n오답 ▶ hard + of ❌ / too ~ that ❌", [])
T.flex('다음 두 문장을 한 문장으로 바르게 바꾼 것은?', S_, B('The water was very clean. + We could see the fish.'),
 ['The water was so clean that we could see the fish.', 'The water was too clean to see the fish.', "The water was so clean that we couldn't see the fish.", 'The water was clean enough that we could not see the fish.', 'The water was such clean that we could see the fish.'],
 "이유 ▶ 매우 깨끗해서(원인) 물고기를 볼 수 있었다(결과) → so ~ that 주어 could.\n오답 ▶ {1}·{2}·{3} 볼 수 없었다는 뜻 {4} such + 형용사만 ❌", [])
T.fixed('다음 중 어법상 옳은 문장을 모두 고른 것은?', X_, B(
 'ⓐ It is my dream to be a pilot.', 'ⓑ It was brave of you to speak first.', 'ⓒ The room is warm enough to sleep in.', 'ⓓ It is hard for me to say sorry.', 'ⓔ The test was so easy what I finished early.'),
 ['ⓐ, ⓑ', 'ⓑ, ⓒ, ⓔ', 'ⓐ, ⓒ, ⓓ', 'ⓐ, ⓑ, ⓒ, ⓓ', 'ⓑ, ⓒ, ⓓ, ⓔ'], 4,
 "이유 ▶ 옳은 것 ⓐ·ⓑ·ⓒ·ⓓ. ⓐ 가주어 It + 진주어 to be a pilot ✔ ⓒ room이 sleep in의 목적어 → it 생략 ✔\n오답 ▶ ⓔ what → that", [])
T.flex('다음 우리말을 바르게 영작한 것은?', X_, B('그 시험은 매우 어려워서 내가 그것을 통과하는 것은 불가능했다.'),
 ['The test was so hard that it was impossible for me to pass it.', 'The test was so hard that it was impossible of me to pass it.', 'The test was too hard that it was impossible for me to pass it.', 'The test was so hard that it was impossible for me pass it.', 'The test was so hard that was impossible for me to pass it.'],
 "이유 ▶ so hard that(결과) + 가주어 it was impossible for me to pass it. (that절 안의 새 문장이므로 it 필요)\n오답 ▶ {1} impossible → for {2} too ~ that ❌ {3} to 빠짐 {4} 가주어 it 빠짐", [])
T.render()
