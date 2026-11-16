# 11/16 발산중 비상(황종배) 8과 문법 심화 변형 1~5세트 (각 20문항) — 원본: Grammar Build Up 8과 객관식(이그잼포유 hwp, 선생님 자료)
# 문법: Pattern 1 not only A but also B (= B as well as A · 수 일치 · 병렬 · 도치, both/either/neither/not A but B)
#       Pattern 2 간접의문문 (의문사+주어+동사 · if/whether · think류는 의문사가 맨 앞 · 의문사 주어 · 시제 · if 쓰임 구별)
# 원본 유형을 살리되 문장·어휘를 바꾸고 난도를 올림 (1세트 중상 → 5세트 최상)
from wu_bs8 import *
H = ('8과 문법 심화', '비상(황종배) Lesson 8 Grammar · not only ~ but also / 간접의문문', '비상(황종배) 8과 문법', 'bs8')
B = lambda *ls: BOX('<br>'.join(ls))
NUMS = ['1개', '2개', '3개', '4개', '5개']
P1, P2, X_ = 'not only ~ but also', '간접의문문', '종합'
NOTE = '범위: 8과 문법 — not only A but also B(= B as well as A, 수 일치·병렬), 간접의문문(의문사+주어+동사, if/whether, think류 동사). 교재 문제를 바탕으로 문장을 바꾸고 더 어렵게 만들었어요. 문장을 끝까지 읽고 고르세요.'
def Tset(k, lv): return Test(str(k), '%d세트' % k, 'not only ~ but also · 간접의문문 · %s' % lv, '8과 문법', NOTE, H=H)
AGREE = '\n포인트 ▶ not only A but also B · either A or B · neither A nor B → 동사는 B에 / B as well as A → 동사는 B(앞)에 / both A and B → 복수'
ORDER = '\n포인트 ▶ 간접의문문 = 의문사 + 주어 + 동사 (do/does/did는 빼고 시제는 동사에)'
THINK = '\n포인트 ▶ think · believe · suppose · guess · imagine 이면 의문사를 맨 앞으로: 의문사 + do you think + 주어 + 동사'

# ═══════════════ 1세트 (중상) ═══════════════
T = Tset(1, '중상')
T.flex('다음 빈칸에 들어갈 말로 알맞은 것은?', P1, B('You have to bring not ' + BL + ' your textbook but also a notebook.'),
 ['only', 'like', 'as', 'well', 'or'],
 "이유 ▶ not only A but also B = A뿐만 아니라 B도 → only\n오답 ▶ {1}·{2}·{3}·{4} not ~ but also와 짝이 되지 않음", [('bring', '가져오다')])
T.flex('다음 빈칸에 들어갈 말로 알맞은 것은?', P1, B('Mia can play not only the piano ' + BL + ' also the cello.'),
 ['but', 'and', 'or', 'so', 'yet'],
 "이유 ▶ not only A but also B → but\n오답 ▶ {1} and also ❌ {2} or는 either와 {3}·{4} 짝이 아님", [])
T.table('(A), (B)에 들어갈 말로 바르게 짝지은 것은?', P1, B('• Not only I but also my sister <b>(A)</b> [ am / is ] good at swimming.', '• He not only cooks but also <b>(B)</b> [ wash / washes ] the dishes.'),
 ['(A)', '(B)'], [['is', 'washes'], ['am', 'washes'], ['is', 'wash'], ['am', 'wash'], ['are', 'washing']],
 "이유 ▶ (A) not only A but also B가 주어면 동사는 B(my sister)에 → is (B) cooks와 나란히(병렬) → washes" + AGREE, [])
T.flex('두 문장의 의미가 같도록 빈칸에 들어갈 말로 알맞은 것은?', P1, B('The cake is not only sweet but also soft.', '= The cake is soft ' + BL + ' sweet.'),
 ['as well as', 'such as', 'better than', 'and so', 'much more'],
 "이유 ▶ not only A but also B = B as well as A (A와 B 자리가 바뀜)\n오답 ▶ {1} 예를 들면 {2} ~보다 나은 {3}·{4} 뜻이 다름", [])
T.flex('다음 문장과 의미가 같은 것은?', P1, B('Not only Tom but also Jake can swim fast.'),
 ['Jake as well as Tom can swim fast.', 'Neither Tom nor Jake can swim fast.', 'Either Tom or Jake can swim fast.', 'Not Tom but Jake can swim fast.', 'Only Jake can swim fast.'],
 "이유 ▶ Tom뿐만 아니라 Jake도 = Jake as well as Tom\n오답 ▶ {1} 둘 다 못함 {2} 둘 중 하나 {3} Tom이 아니라 Jake {4} Jake만", [])
T.flex('다음 우리말을 바르게 영작한 것은?', P1, B('그녀는 친절할 뿐만 아니라 정직하다.'),
 ['She is not only kind but also honest.', 'She is not kind but honest.', 'She is either kind or honest.', 'She is neither kind nor honest.', 'She is kind but not honest.'],
 "이유 ▶ ~할 뿐만 아니라 …하다 = not only ~ but also …\n오답 ▶ {1} 친절한 게 아니라 정직 {2} 둘 중 하나 {3} 둘 다 아님 {4} 친절하지만 정직하지 않음", [('honest', '정직한')])
T.flex('다음 중 어법상 옳은 문장은?', P1, '',
 ['Not only Jisu but also her parents like K-pop.', 'Not only Jisu but also her parents likes K-pop.', 'My friends as well as I am tired.', 'He likes not only swimming but also run.', 'She is not only smart but also kindly.'],
 "이유 ▶ 동사는 B(her parents, 복수)에 → like ✔\n오답 ▶ {1} likes → like {2} B as well as A는 앞(My friends)에 → are {3} swimming과 나란히 → running {4} smart와 나란히 형용사 → kind" + AGREE, [])
T.flex('다음 빈칸에 들어갈 말로 알맞은 것은?', P2, B('Do you know ' + BL + ' she is?'),
 ['who', 'whether', 'which', 'that', 'then'],
 "이유 ▶ 그녀가 누구인지 → 의문사 who + 주어 + 동사\n오답 ▶ {1} whether she is? 뒤가 끊김 {2} which는 '어느 것' {3} that은 의문사가 아님 {4} then은 접속사가 아님", [])
T.flex('다음 빈칸에 들어갈 말로 알맞은 것은?', P2, B("I'm not sure " + BL + ' he will come to the party.'),
 ['if', 'though', 'because', 'so', 'unless'],
 "이유 ▶ 그가 올지 안 올지 확실하지 않다 → 의문사 없는 간접의문문은 if(= whether)\n오답 ▶ {1} ~이지만 {2} ~ 때문에 {3} 그래서 {4} ~하지 않으면 → not sure의 목적어가 안 됨", [])
T.flex('다음 빈칸에 들어갈 말로 알맞은 것은?', P2, B('Do you know ' + BL + '?'),
 ['where the library is', 'where is the library', 'where does the library', 'where the library does', 'is where the library'],
 "이유 ▶ 의문사 + 주어 + 동사 → where the library is\n오답 ▶ {1} 동사가 주어 앞 {2}·{3} does는 쓰지 않음 {4} 어순 엉킴" + ORDER, [])
T.flex('두 문장을 한 문장으로 바르게 바꾼 것은?', P2, B('Can you tell me? + What time does the store open?'),
 ['Can you tell me what time the store opens?', 'Can you tell me what time does the store open?', 'Can you tell me what time the store open?', 'What time can you tell me the store opens?', 'Can you tell me if what time the store opens?'],
 "이유 ▶ does를 빼고 시제·수는 동사에: the store opens\n오답 ▶ {1} does 그대로 ❌ {2} 주어가 단수 → opens {3} tell은 think류가 아님 → 의문사를 앞으로 보내지 않음 {4} 의문사가 있으면 if ❌" + ORDER, [])
T.flex('두 문장을 한 문장으로 바르게 바꾼 것은?', P2, B('Do you know? + Is Mr. Kim in his office?'),
 ['Do you know if Mr. Kim is in his office?', 'Do you know is Mr. Kim in his office?', 'Do you know that is Mr. Kim in his office?', 'Do you know if is Mr. Kim in his office?', 'Do you know where Mr. Kim is in his office?'],
 "이유 ▶ 의문사가 없는 의문문 → if(whether) + 주어 + 동사\n오답 ▶ {1} 접속사 없음 {2} that ❌ {3} 어순 ❌ {4} 뜻이 바뀜(어디)", [])
T.flex('두 문장을 한 문장으로 바르게 바꾼 것은?', P2, B('Do you think? + Where did he go?'),
 ['Where do you think he went?', 'Do you think where he went?', 'Where do you think did he go?', 'Do you think where did he go?', 'Where do you think he goes?'],
 "이유 ▶ think이면 의문사를 맨 앞으로 + 주어 + 동사(did → went)\n오답 ▶ {1} 의문사가 뒤 {2} did 그대로 {3} 둘 다 ❌ {4} 과거 → went" + THINK, [])
T.flex('다음 대화의 빈칸에 들어갈 말로 알맞은 것은?', P2, B("A: I want to visit Ms. Han, but I don't know " + BL + '.', "B: She's in the music room. I'll take you there."),
 ['where she is', 'where is she', 'where she does', 'where did she', 'where she was been'],
 "이유 ▶ 의문사 + 주어 + 동사 → where she is\n오답 ▶ {1} 어순 {2}·{3} do 쓰임 ❌ {4} was been ❌", [])
T.flex('다음 우리말을 바르게 영작한 것은?', P2, B('나는 그가 왜 늦었는지 궁금하다.'),
 ['I wonder why he was late.', 'I wonder why was he late.', 'I wonder why he is late.', 'I wonder he was late why.', 'Why I wonder he was late.'],
 "이유 ▶ why + 주어 + 동사(과거 was)\n오답 ▶ {1} 어순 {2} 시제(늦었는지 → 과거) {3}·{4} 어순 ❌", [('wonder', '궁금하다')])
T.fixed('다음 &lt;보기&gt;에서 어법상 옳은 문장의 개수는?', P1, B(
 '(a) Not only you but also he is right.', '(b) She as well as her friends are kind.', '(c) I like not only apples but also bananas.', '(d) He not only sings but also dance.', '(e) Both Mina and Sora are my friends.'),
 NUMS, 3,
 "이유 ▶ 옳은 것 (a)·(c)·(e) 3개\n오답 ▶ (b) B as well as A는 앞(She)에 → is (d) sings와 나란히 → dances" + AGREE, [])
T.flex('다음 우리말을 바르게 영작한 것은?', P2, B('너는 누가 이 그림을 그렸는지 아니?'),
 ['Do you know who drew this picture?', 'Do you know who did draw this picture?', 'Do you know who this picture drew?', 'Who do you know drew this picture?', 'Do you know who drawn this picture?'],
 "이유 ▶ 의문사(who)가 주어면 바로 동사: who drew\n오답 ▶ {1} did 쓰지 않음 {2} 그림이 그렸다?(주어·목적어 뒤바뀜) {3} know는 think류가 아님 → 의문사를 앞으로 ❌ {4} drawn은 과거분사", [])
T.flex('밑줄 친 if의 쓰임이 &lt;보기&gt;와 같은 것은?', P2, B('&lt;보기&gt; I wonder <u>if</u> it will rain tomorrow.'),
 ['Do you know <u>if</u> she likes cats?', 'Call me <u>if</u> you need help.', '<u>If</u> it rains, we will stay home.', 'I will go out <u>if</u> you come with me.', 'You can sleep <u>if</u> you are tired.'],
 "이유 ▶ &lt;보기&gt;의 if = ~인지 아닌지(간접의문문). 같은 것은 know의 목적어 if절\n오답 ▶ {1}·{2}·{3}·{4} 만약 ~라면(조건)", [])
T.table('(A), (B)에 들어갈 말로 바르게 짝지은 것은?', P1, B('• Either you or Tom <b>(A)</b> [ have / has ] to clean the room.', '• Neither my sister nor I <b>(B)</b> [ am / is ] good at math.'),
 ['(A)', '(B)'], [['has', 'am'], ['have', 'am'], ['has', 'is'], ['have', 'is'], ['having', 'are']],
 "이유 ▶ either A or B · neither A nor B → 동사는 B에: (A) Tom → has (B) I → am" + AGREE, [])
T.flex('다음 중 어법상 <u>어색한</u> 문장은?', P2, '',
 ["I don't know what is his name.", 'Can you tell me where she lives?', 'I wonder if he is at home.', 'Do you know who broke the window?', 'What do you think she wants?'],
 "이유 ▶ what is his name → what his name is\n오답 ▶ {1} where + she + lives ✔ {2} if + 주어 + 동사 ✔ {3} 의문사 주어 + 동사 ✔ {4} think → 의문사 맨 앞 ✔" + ORDER, [])
T.render()

# ═══════════════ 2세트 (상) ═══════════════
T = Tset(2, '상')
T.flex('다음 문장과 의미가 같은 것은?', P1, B('Girls as well as boys enjoy the game.'),
 ['Not only boys but also girls enjoy the game.', 'Only boys enjoy the game.', 'Not girls but boys enjoy the game.', 'Neither boys nor girls enjoy the game.', "Boys enjoy the game, but girls don't."],
 "이유 ▶ B as well as A = not only A but also B → 소년들뿐만 아니라 소녀들도\n오답 ▶ {1} 소년들만 {2} 소녀가 아니라 소년 {3} 둘 다 아님 {4} 소녀는 안 즐김", [])
T.table('두 문장을 한 문장으로 바꿀 때 (A), (B)에 들어갈 말로 알맞은 것은?', P1, B('Mark speaks Spanish. He also speaks Italian.', '→ Mark speaks not <b>(A)</b> Spanish <b>(B)</b> also Italian.'),
 ['(A)', '(B)'], [['only', 'but'], ['only', 'and'], ['but', 'only'], ['just', 'and'], ['also', 'but']],
 "이유 ▶ not only A but also B", [])
T.flex('빈칸에 들어갈 말을 순서대로 바르게 짝지은 것은?', P1, B('• Both Ann and Jake ' + BL + ' coming to the party.', '• Either you or I ' + BL + ' wrong.', '• Kevin as well as his brothers ' + BL + ' tall.'),
 ['are − am − is', 'is − am − are', 'are − are − is', 'are − am − are', 'is − is − is'],
 "이유 ▶ both A and B → 복수 are / either A or B → B(I) am / B as well as A → 앞(Kevin) is" + AGREE, [])
T.flex('다음 중 어법상 <u>어색한</u> 문장은?', P1, '',
 ['Not only the teacher but also the students was surprised.', 'He gave up not only coffee but also soda.', 'Not only she but also I am ready.', 'Amy is not only pretty but also wise.', 'My brother as well as my parents loves pizza.'],
 "이유 ▶ 동사는 B(the students, 복수)에 → were\n오답 ▶ {1} 명사끼리 ✔ {2} B(I) → am ✔ {3} 형용사끼리 ✔ {4} 앞(My brother) → loves ✔", [])
T.flex('다음 우리말을 바르게 영작한 것은?', P1, B('너는 책에서뿐만 아니라 사람들에게서도 많이 배울 수 있다.'),
 ['You can learn a lot not only from books but also from people.', 'You can learn a lot not from books but from people.', 'You can learn a lot either from books or from people.', 'You can learn a lot from books as well as from people.', 'You can learn a lot neither from books nor from people.'],
 "이유 ▶ 책뿐만 아니라(A) 사람들에게서도(B) → not only from books but also from people\n오답 ▶ {1} 책이 아니라 사람 {2} 둘 중 하나 {3} B as well as A → '사람들뿐만 아니라 책에서도'(A·B가 바뀜) {4} 둘 다 아님", [])
T.flex('짝지어진 두 문장의 의미가 서로 <u>다른</u> 것은?', P1, '',
 ['He was a good singer as well as a good dancer.<br>= He was not a good dancer but a good singer.',
  'She is smart, and she is funny, too.<br>= She is not only smart but also funny.',
  'Tea is loved by adults as well as children.<br>= Tea is loved not only by children but also by adults.',
  'Not only Ted but also his dog was wet.<br>= His dog as well as Ted was wet.',
  'The room is quiet as well as clean.<br>= The room is not only clean but also quiet.'],
 "이유 ▶ not A but B = A가 아니라 B → 둘 다라는 as well as와 뜻이 다름\n오답 ▶ {1}·{2}·{3}·{4} not only A but also B = B as well as A", [])
T.flex('다음 중 어법상 옳은 문장은?', P1, '',
 ['Not only did he win the game, but he also broke the record.', 'Not only he won the game, but he also broke the record.', 'Not only did he won the game, but he also broke the record.', 'Not only won he the game, but he also broke the record.', 'Not only does he win the game yesterday, but he also broke the record.'],
 "이유 ▶ Not only가 문장 맨 앞이면 도치: Not only + did + 주어 + 동사원형\n오답 ▶ {1} 도치 안 함 {2} did 뒤에는 원형 win {3} 일반동사는 did를 써서 도치 {4} yesterday(과거) → did", [('record', '기록')])
T.flex('다음 문장을 간접의문문으로 바꿀 때 빈칸에 알맞은 것은?', P2, B('He said to me, "Are you hungry?"', '→ He asked me ' + BL + '.'),
 ['if I was hungry', 'if you were hungry', 'if was I hungry', 'whether am I hungry', 'that I was hungry'],
 "이유 ▶ 의문사 없음 → if + 주어 + 동사. you는 나(I)로, 과거(asked)에 맞춰 was\n오답 ▶ {1} 인칭 {2}·{3} 어순 {4} that ❌", [])
T.flex('다음 빈칸에 들어갈 말로 알맞은 것은?', P2, B('I wonder ' + BL + ' last weekend.'),
 ['what Jenny did', 'what did Jenny do', 'what Jenny does', 'what Jenny will do', 'what does Jenny do'],
 "이유 ▶ last weekend(과거) + 의문사 + 주어 + 동사 → what Jenny did\n오답 ▶ {1}·{4} 어순 {2}·{3} 시제", [])
T.flex('다음 빈칸에 들어갈 말로 적절하지 <u>않은</u> 것은?', P2, B('Can you tell me ' + BL + '?'),
 ['how old is your brother', 'how old your brother is', 'who owns this car', 'if the shop is open', 'what you want for dinner'],
 "이유 ▶ how old + 주어 + 동사 → how old your brother is\n오답 ▶ {1}·{2}·{3}·{4} 어순 ✔ (who가 주어면 바로 동사 owns)" + ORDER, [])
T.flex('다음 우리말을 바르게 영작한 것은?', P2, B('너는 그가 무엇을 샀다고 생각하니?'),
 ['What do you think he bought?', 'Do you think what he bought?', 'What do you think did he buy?', 'Do you think what did he buy?', 'What do you think he buys?'],
 "이유 ▶ think → 의문사 맨 앞 + do you think + 주어 + 동사(과거)\n오답 ▶ {1} 의문사가 뒤 {2} did 그대로 {3} 둘 다 ❌ {4} 샀다 → 과거" + THINK, [])
T.flex('다음 우리말을 바르게 영작한 것은?', P2, B('무엇이 그를 화나게 했는지 말해 줄래?'),
 ['Can you tell me what made him angry?', 'Can you tell me what did make him angry?', 'Can you tell me what he made angry?', 'Can you tell me what him made angry?', 'What can you tell me made him angry?'],
 "이유 ▶ 의문사 what이 주어 → what + 동사(made)\n오답 ▶ {1} did ❌ {2} 그가 무엇을 화나게? {3} 목적격 him이 주어 자리 ❌ {4} tell은 think류가 아님", [])
T.flex('밑줄 친 if의 쓰임이 나머지 넷과 <u>다른</u> 것은?', P2, '',
 ['You can borrow my pen <u>if</u> you need one.', "I'm not sure <u>if</u> this is right.", 'Do you know <u>if</u> Tom is coming?', 'Ask her <u>if</u> she can help us.', 'I wonder <u>if</u> they won the game.'],
 "이유 ▶ 만약 ~라면(조건)\n오답 ▶ {1}·{2}·{3}·{4} ~인지 아닌지(간접의문문, 목적어 역할)", [])
T.flex('빈칸에 들어갈 말이 나머지 넷과 <u>다른</u> 것은?', P2, '',
 ['I wonder ' + BL + ' she will accept my offer.', 'Tell me ' + BL + ' you have in your bag.', 'I know ' + BL + ' you did last summer.', 'Show me ' + BL + ' you bought.', 'Do you know ' + BL + ' this word means?'],
 "이유 ▶ 뒤가 완전한 문장 + '~인지' → if(whether)\n오답 ▶ {1}·{2}·{3}·{4} have·did·bought·means의 목적어가 빠짐 → what", [('accept', '받아들이다')])
T.fixed('다음 &lt;보기&gt;에서 어법상 옳은 문장의 개수는?', P2, B(
 "(a) I don't know where he lives.", '(b) Can you tell me what time is it?', '(c) Why do you think she left?', '(d) I wonder if is he busy.', '(e) Do you know who made this cake?', '(f) Do you think where she went?'),
 NUMS, 3,
 "이유 ▶ 옳은 것 (a)·(c)·(e) 3개\n오답 ▶ (b) what time it is (d) if he is busy (f) Where do you think she went?" + THINK, [])
T.flex('다음 대화의 빈칸에 들어갈 말로 알맞은 것은?', P2, B('Q: ' + BL + '?', 'A: I usually go to bed at 11.'),
 ['Can you tell me when you usually go to bed', 'Can you tell me when do you usually go to bed', 'Can you tell me if you usually go to bed', 'Can you tell me when did you go to bed', 'When can you tell me you usually go to bed'],
 "이유 ▶ 언제 자는지 → when + 주어 + 동사\n오답 ▶ {1}·{3} 어순 {2} 자는지 아닌지 → 대답과 맞지 않음 {4} tell은 think류가 아님", [])
T.flex('(A), (B), (C)에서 어법에 맞는 것을 바르게 짝지은 것은?', P2, B('• I have no idea how <b>(A)</b> [ they got / did they get ] there.', '• Do you know who <b>(B)</b> [ broke / did break ] the vase?', '• Do you know where <b>(C)</b> [ he is / is he ] from?'),
 ['they got − broke − he is', 'did they get − broke − he is', 'they got − did break − he is', 'they got − broke − is he', 'did they get − did break − is he'],
 "이유 ▶ (A) 주어 + 동사 (B) 의문사가 주어 → 바로 동사 (C) 주어 + 동사" + ORDER, [])
T.flex('다음 중 어법상 옳은 문장은?', P1, '',
 ['She enjoys not only cooking but also baking.', 'She enjoys not only cooking but also to bake.', 'He not only reads books but also write poems.', 'The room was not only clean but also comfortably.', 'We visited not only Paris but also went to Rome.'],
 "이유 ▶ 동명사끼리 나란히 ✔\n오답 ▶ {1} cooking과 나란히 → baking {2} reads와 나란히 → writes {3} 형용사 → comfortable {4} 명사(Paris)와 동사구는 나란히 쓸 수 없음 → not only Paris but also Rome", [('poem', '시')])
T.flex('다음 문장과 의미가 같은 것은?', P1, B('Not only Minho but also his friends were late.'),
 ['His friends as well as Minho were late.', 'Neither Minho nor his friends were late.', 'Either Minho or his friends were late.', 'Not Minho but his friends were late.', 'Only Minho was late.'],
 "이유 ▶ 민호뿐만 아니라 친구들도 = His friends as well as Minho\n오답 ▶ {1} 둘 다 아님 {2} 둘 중 하나 {3} 민호가 아니라 친구들 {4} 민호만", [])
T.flex('다음 중 어법상 <u>어색한</u> 문장은?', P2, '',
 ['Do you believe who will win?', 'Who do you believe will win?', "I don't know if she will win.", 'Tell me who won the race.', 'Which team do you think will win?'],
 "이유 ▶ believe → 의문사를 맨 앞으로: Who do you believe will win?\n오답 ▶ {1}·{4} 의문사 맨 앞 ✔ {2} if + 주어 + 동사 ✔ {3} 의문사 주어 + 동사 ✔" + THINK, [])
T.render()

# ═══════════════ 3세트 (상) ═══════════════
T = Tset(3, '상')
T.flex('다음 빈칸에 들어갈 말로 알맞은 것은?', P1, B('Both Minji ' + BL + ' Hana are in the school band.'),
 ['and', 'or', 'nor', 'but', 'as'],
 "이유 ▶ both A and B = A와 B 둘 다\n오답 ▶ {1} either와 {2} neither와 {3} not only와 {4} as well as", [])
T.table('(A), (B)에 들어갈 말로 바르게 짝지은 것은?', P1, B('• Not only Mr. Lee but also his students <b>(A)</b> [ want / wants ] a longer break.', '• Kate as well as her sisters <b>(B)</b> [ like / likes ] horror movies.'),
 ['(A)', '(B)'], [['want', 'likes'], ['wants', 'likes'], ['want', 'like'], ['wants', 'like'], ['wanting', 'liking']],
 "이유 ▶ (A) B(his students, 복수) → want (B) B as well as A는 앞(Kate)에 → likes" + AGREE, [])
T.flex('다음 우리말을 바르게 영작한 것은?', P1, B('Jessica뿐만 아니라 나도 그 영화를 보았다.'),
 ['Not only Jessica but also I watched the movie.', 'Not only I but also Jessica watched the movie.', 'Jessica as well as I watched the movie.', 'Not Jessica but I watched the movie.', 'Either Jessica or I watched the movie.'],
 "이유 ▶ Jessica뿐만 아니라(A) 나도(B)\n오답 ▶ {1} 나뿐만 아니라 Jessica도(A·B 바뀜) {2} B as well as A → 'Jessica도'로 A·B 바뀜 {3} Jessica가 아니라 나 {4} 둘 중 하나", [])
T.flex('다음 문장과 의미가 같은 것은?', P1, B('He gave me not only a book but also a pen.'),
 ['He gave me a pen as well as a book.', 'He gave me a book as well as a pen.', 'He gave me not a book but a pen.', 'He gave me either a book or a pen.', 'He gave me neither a book nor a pen.'],
 "이유 ▶ not only A but also B = B as well as A\n오답 ▶ {1} A·B 자리가 바뀜(펜뿐만 아니라 책도) {2} 책이 아니라 펜 {3} 둘 중 하나 {4} 둘 다 아님", [])
T.flex('다음 중 어법상 옳은 문장은?', P1, '',
 ['Not only you but also she is invited.', 'Not only you but also she are invited.', 'She as well as you are invited.', 'Either you or she are invited.', 'Neither you nor she were invited yesterday.'],
 "이유 ▶ B(she) → is ✔\n오답 ▶ {1} → is {2} 앞(She) → is {3} B(she) → is {4} B(she) → was" + AGREE, [])
T.flex('밑줄 친 ⓐ~ⓔ 중 어법상 <u>어색한</u> 것끼리 짝지은 것은?', P1, B('• ⓐ <u>Not only</u> my mom ⓑ <u>but also</u> my dad ⓒ <u>like</u> jazz.', '• She likes not only ⓓ <u>reading</u> but also ⓔ <u>write</u>.'),
 ['ⓒ, ⓔ', 'ⓐ, ⓒ', 'ⓑ, ⓓ', 'ⓒ, ⓓ', 'ⓑ, ⓔ'],
 "이유 ▶ ⓒ B(my dad) → likes ⓔ reading과 나란히 → writing\n오답 ▶ ⓐ·ⓑ·ⓓ는 바름", [])
T.flex('두 문장을 한 문장으로 바르게 바꾼 것은?', P1, B('• We expected you to be honest.', '• We also expected you to work hard.'),
 ['We expected you not only to be honest but also to work hard.', 'We expected you not only to be honest but also working hard.', 'We expected you to be honest as well as work hard.', 'We expected you not only to work hard also to be honest.', 'We expected you to be honest as well as hard work.'],
 "이유 ▶ to부정사끼리 나란히: not only to be ~ but also to work ~\n오답 ▶ {1} working ❌ {2} to be와 나란히 → to work {3} but 빠짐 {4} 명사 hard work ❌", [('expect', '기대하다')])
T.flex('다음 빈칸에 들어갈 말로 알맞은 것은?', P2, B('Can you tell me ' + BL + '?'),
 ['how long the bridge is', 'how long is the bridge', 'how the bridge is long', 'how long does the bridge', 'is how long the bridge'],
 "이유 ▶ how long은 한 덩어리 + 주어 + 동사\n오답 ▶ {1} 어순 {2} how와 long을 떼면 ❌ {3} does ❌ {4} 어순", [])
T.flex('다음 빈칸에 들어갈 말로 적절하지 <u>않은</u> 것은?', P2, B('Do you know ' + BL + '?'),
 ['why did Ms. Park call you', 'what your parents do', 'how many people came', 'if the bus has left', 'who your best friend is'],
 "이유 ▶ did를 빼고 why Ms. Park called you\n오답 ▶ {1}·{2}·{3}·{4} 의문사(if) + 주어 + 동사 ✔ (how many people은 주어)" + ORDER, [])
T.flex('다음 문장을 간접의문문으로 바르게 바꾼 것은?', P2, B('Mina says to me, "Where do you live?"'),
 ['Mina asks me where I live.', 'Mina asks me where do I live.', 'Mina asks me where you live.', 'Mina asks me where I lived.', 'Mina asked me where do I live.'],
 "이유 ▶ you → I, says(현재) → asks, do 빼고 where I live\n오답 ▶ {1}·{4} do ❌ {2} 인칭 {3} 현재인데 lived", [])
T.flex('두 문장을 한 문장으로 바르게 바꾼 것은?', P2, B("I'd like to know. + Why did she leave early?"),
 ["I'd like to know why she left early.", "I'd like to know why did she leave early.", "I'd like to know why she leaves early.", "I'd like to know why left she early.", "I'd like to know if why she left early."],
 "이유 ▶ did를 빼고 과거 동사 left\n오답 ▶ {1} did ❌ {2} 시제 {3} 어순 {4} if ❌", [])
T.flex('두 문장을 한 문장으로 바르게 바꾼 것은?', P2, B('Do you suppose? + Who ate the cake?'),
 ['Who do you suppose ate the cake?', 'Do you suppose who ate the cake?', 'Who do you suppose did eat the cake?', 'Do you suppose who did eat the cake?', 'Who do you suppose eats the cake?'],
 "이유 ▶ suppose → 의문사 맨 앞. who가 주어라 바로 ate\n오답 ▶ {1}·{3} 의문사가 뒤 {2} did ❌ {4} 시제" + THINK, [])
T.flex('밑줄 친 부분의 쓰임이 나머지 넷과 <u>다른</u> 것은?', P2, '',
 ['I met the girl <u>who lives next door</u>.', "I don't know <u>who lives next door</u>.", 'Tell me <u>where you found it</u>.', 'I wonder <u>when the movie ends</u>.', 'She asked me <u>what I wanted</u>.'],
 "이유 ▶ the girl을 꾸미는 관계대명사절\n오답 ▶ {1}·{2}·{3}·{4} 동사의 목적어인 간접의문문", [])
T.flex('다음 중 어법상 옳은 문장은?', P2, '',
 ['I wonder whether you can come.', 'I wonder whether can you come.', 'Do you know where is the bank?', 'Tell me what does it mean.', "I'm not sure how old is he."],
 "이유 ▶ whether + 주어 + 동사 ✔\n오답 ▶ {1} you can {2} the bank is {3} it means {4} he is" + ORDER, [])
T.flex('다음 대화의 빈칸에 들어갈 말로 알맞은 것은?', P2, B('A: What are you looking at?', "B: This photo. I'm curious about " + BL + '.', "A: It's Jeju Island."),
 ['where this place is', 'who took this photo', 'when it was taken', 'what the problem is', 'how much it costs'],
 "이유 ▶ 대답이 장소(Jeju Island) → 이곳이 어디인지\n오답 ▶ {1} 찍은 사람 {2} 찍은 때 {3} 문제 {4} 가격 → 대답과 맞지 않음", [('curious', '궁금한')])
T.flex('짝지어진 두 문장의 의미가 서로 <u>다른</u> 것은?', P1, '',
 ['He is a doctor as well as a writer.<br>= He is not a writer but a doctor.',
  'I like dogs, and I like cats, too.<br>= I like not only dogs but also cats.',
  'Not only Sam but also Leo plays tennis.<br>= Leo as well as Sam plays tennis.',
  'She speaks English as well as French.<br>= She speaks not only French but also English.',
  'Amy is tall, and Ben is tall, too.<br>= Both Amy and Ben are tall.'],
 "이유 ▶ not A but B = A가 아니라 B (작가가 아님)\n오답 ▶ {1}·{2}·{3}·{4} 둘 다라는 같은 뜻", [])
T.fixed('다음 &lt;보기&gt;에서 어법상 <u>틀린</u> 문장의 개수는?', P2, B(
 '(a) Do you know what time it is?', "(b) I don't care who are you.", '(c) What do you think is the answer?', '(d) Can you tell me how much is it?', '(e) I asked him where he was from.', '(f) No one knows why he quit.'),
 NUMS, 2,
 "이유 ▶ 틀린 것 (b)·(d) 2개: who you are / how much it is\n오답 ▶ (c) What do you think + is(의문사 what이 주어) ✔" + ORDER, [])
T.flex('다음 문장의 틀린 곳을 바르게 고친 것은?', P2, B('Do you think why is she crying?'),
 ['Why do you think she is crying?', 'Do you think why she is crying?', 'Why do you think is she crying?', 'Do you think why is crying she?', 'Why do you think she crying?'],
 "이유 ▶ think → 의문사 맨 앞 + 주어 + 동사\n오답 ▶ {1} 의문사가 뒤 {2} 어순 {3} 어순 {4} is 빠짐" + THINK, [])
T.flex('다음 중 어법상 <u>어색한</u> 문장은?', X_, '',
 ['Not only Tom but also I knows the answer.', 'Do you know who wrote this song?', 'Both my brother and I like soccer.', 'I wonder if it will snow tonight.', 'He is not only funny but also smart.'],
 "이유 ▶ B(I) → know\n오답 ▶ {1} 의문사 주어 + 동사 ✔ {2} both → 복수 ✔ {3} if + 주어 + 동사 ✔ {4} 형용사끼리 ✔", [])
T.flex('두 문장의 빈칸에 공통으로 들어갈 말로 알맞은 것은?', P2, B("• I don't know " + BL + ' she likes me or not.', '• Let me know ' + BL + ' you can come to the meeting.'),
 ['whether', 'what', 'that', 'who', 'which'],
 "이유 ▶ ~인지 아닌지 → whether(= if), or not과 잘 어울림\n오답 ▶ {1}·{3}·{4} 뒤가 완전한 문장이라 ❌ {2} that은 '~인지'의 뜻이 없음", [])
T.render()

# ═══════════════ 4세트 (최상) ═══════════════
T = Tset(4, '최상')
T.flex('(A), (B), (C)에 들어갈 말을 바르게 짝지은 것은?', P1, B('• Not only the boys but also the girl <b>(A)</b> ' + BL + ' happy.', '• The girl as well as the boys <b>(B)</b> ' + BL + ' happy.', '• Both the girl and the boys <b>(C)</b> ' + BL + ' happy.'),
 ['is − is − are', 'are − is − are', 'is − are − are', 'are − are − are', 'is − is − is'],
 "이유 ▶ (A) B(the girl) is (B) 앞(The girl) is (C) both → are" + AGREE, [])
T.flex('다음 중 어법상 옳은 문장은?', P1, '',
 ['Not only does she sing well, but she also dances well.', 'Not only she sings well, but she also dances well.', 'Not only sings she well, but she also dances well.', 'Not only does she sings well, but she also dances well.', 'Not only did she sings well, but she also danced well.'],
 "이유 ▶ Not only 맨 앞 → does + 주어 + 동사원형\n오답 ▶ {1} 도치 안 함 {2} 일반동사는 do로 도치 {3}·{4} does/did 뒤 원형", [])
T.flex('두 문장을 한 문장으로 바르게 만든 것은?', P1, '',
 ['This book is useful. It is also fun.<br>→ This book is fun as well as useful.',
  "Ken can swim. Ray can swim, too.<br>→ Not only Ken but also Ray can't swim.",
  'Sue is a nurse. She is also a singer.<br>→ Sue is not a nurse but a singer.',
  "Leo doesn't like milk. He doesn't like juice either.<br>→ Leo likes not only milk but also juice.",
  'Ann enjoys painting. She also enjoys singing.<br>→ Ann not only enjoys painting but also singing.'],
 "이유 ▶ 유용할 뿐만 아니라 재미있다 = fun as well as useful ✔\n오답 ▶ {1} 못 한다로 바뀜 {2} 간호사가 아니라 가수 {3} 둘 다 싫어함 → neither milk nor juice {4} 병렬 ❌ → enjoys not only painting but also singing", [])
T.flex('&lt;보기&gt;에서 어법상 옳은 문장을 모두 고른 것은?', P1, B(
 '(a) Hana likes not only tea but also coffee.', '(b) Not only I but also Mr. Kim want to be a teacher.', '(c) Jinho is good at singing as well as dance.', '(d) Not only the book but also the movie is fun.', '(e) Sora as well as her cousins are good at tennis.', '(f) Henry speaks not only English but Chinese.'),
 ['(a), (d), (f)', '(a), (b), (d)', '(c), (d), (e)', '(b), (e), (f)', '(a), (c), (f)'],
 "이유 ▶ (a)·(d)·(f) 옳음 ((f) but also의 also는 생략 가능)\n오답 ▶ (b) B(Mr. Kim) → wants (c) singing과 나란히 → dancing (e) 앞(Sora) → is" + AGREE, [])
T.flex('짝지어진 두 문장의 의미가 같은 것은?', P1, '',
 ['He is good at math as well as science.<br>= He is good at not only science but math.',
  'You can enjoy not only its taste but also its smell.<br>= You can enjoy its smell well as its taste.',
  'Her eyes as well as her mouth smile.<br>= Not only her eyes but also her mouth smiles.',
  'The plant is not only pretty but also useful.<br>= The plant is not pretty but useful.',
  'Both Jim and Sue are absent.<br>= Either Jim or Sue is absent.'],
 "이유 ▶ math as well as science = not only science but (also) math ✔\n오답 ▶ {1} as 빠짐(as well as) {2} A·B 자리가 바뀜 → Not only her mouth but also her eyes smile {3} 예쁘지 않다로 바뀜 {4} 둘 중 하나로 바뀜", [])
T.flex('&lt;보기&gt;에서 어법상 옳은 문장끼리 짝지은 것은?', P2, B(
 '(a) Please tell me how is Tom.', '(b) Do you think what he should do?', '(c) Does she know where her friend lives?', '(d) Can you tell me who the window broke?', '(e) I wonder if you will come to my party.', '(f) What do you believe happened?'),
 ['(c), (e), (f)', '(a), (c), (e)', '(b), (d), (f)', '(a), (b), (e)', '(c), (d), (e)'],
 "이유 ▶ (c)·(e)·(f) 옳음\n오답 ▶ (a) how Tom is (b) What do you think he should do? (d) 의문사 주어 → who broke the window" + THINK, [])
T.fixed('다음 &lt;보기&gt;에서 어법상 옳은 문장의 개수는?', P2, B(
 '(a) I wonder whether Cindy likes me.', '(b) Do you remember what time was it?', '(c) How far do you suppose he can run?', "(d) Mike doesn't know if there is a bank nearby.", '(e) Please tell me what should I do.', "(f) I'm not sure when he arrived."),
 NUMS, 4,
 "이유 ▶ 옳은 것 (a)·(c)·(d)·(f) 4개\n오답 ▶ (b) what time it was (e) what I should do" + ORDER, [])
T.flex('다음 우리말을 바르게 영작한 것은?', P2, B('그녀가 어떻게 그 문제를 풀었는지 아무도 모른다.'),
 ['Nobody knows how she solved the problem.', 'Nobody knows how did she solve the problem.', 'Nobody knows how she solves the problem.', 'Nobody knows how solved she the problem.', 'How does nobody know she solved the problem?'],
 "이유 ▶ how + 주어 + 동사(과거)\n오답 ▶ {1} did ❌ {2} 풀었는지 → 과거 {3} 어순 {4} know는 의문사를 앞으로 보내지 않음", [('solve', '풀다')])
T.flex('다음 우리말을 바르게 영작한 것은?', P2, B('너는 그 강이 얼마나 긴지 아니?'),
 ['Do you know how long the river is?', 'Do you know how the river is long?', 'How long do you know the river is?', 'Do you know how long is the river?', 'Do you know the river how long is?'],
 "이유 ▶ how long(한 덩어리) + 주어 + 동사\n오답 ▶ {1} how long을 떼면 ❌ {2} know는 의문사를 앞으로 보내지 않음 {3}·{4} 어순", [])
T.flex('밑줄 친 if의 쓰임이 &lt;보기&gt;와 같은 것은?', P2, B("&lt;보기&gt; We'll be late <u>if</u> we don't hurry."),
 ["You'll feel better <u>if</u> you take a rest.", "I'm not sure <u>if</u> the store is open.", 'Do you know <u>if</u> he got the message?', 'She asked me <u>if</u> I liked jazz.', 'I wonder <u>if</u> the rumor is true.'],
 "이유 ▶ &lt;보기&gt;의 if = 만약 ~라면(조건). 같은 것은 쉬면 나아질 것\n오답 ▶ {1}·{2}·{3}·{4} ~인지 아닌지(간접의문문)", [('rumor', '소문')])
T.flex('다음 중 어법상 옳은 문장은?', P2, '',
 ['Which do you think is better, this or that?', 'Do you think which is better, this or that?', 'Which do you think better is, this or that?', 'Which do you know is better, this or that?', 'Do you think which one better is?'],
 "이유 ▶ think → 의문사 맨 앞. which가 주어라 바로 is\n오답 ▶ {1}·{4} 의문사가 뒤 {2} 어순 {3} know는 의문사를 앞으로 보내지 않음 → Do you know which is better?" + THINK, [])
T.flex('두 문장을 한 문장으로 연결한 것 중 <u>어색한</u> 것은?', P2, '',
 ['Do you guess? + Who called me?<br>→ Do you guess who called me?',
  'I asked her. + Why was she sad?<br>→ I asked her why she was sad.',
  'Tell me. + What did he say?<br>→ Tell me what he said.',
  'Do you think? + Why did she quit?<br>→ Why do you think she quit?',
  "I'd like to know. + Where did they go?<br>→ I'd like to know where they went."],
 "이유 ▶ guess → 의문사 맨 앞: Who do you guess called me?\n오답 ▶ {1}·{2}·{3}·{4} 바르게 연결" + THINK, [])
T.flex('우리말과 일치하도록 괄호 안의 말을 배열할 때 세 번째로 오는 단어는?', P2, B('그들이 그 일을 좋아하는지 넌 알고 있니?', '→ Do you ( like / know / the / if / they ) job?'),
 ['they', 'know', 'if', 'like', 'the'],
 "이유 ▶ Do you know if they like the job? → know(1) if(2) they(3)\n포인트 ▶ 의문사 없는 간접의문문 = if + 주어 + 동사", [])
T.flex('다음 우리말을 영작할 때 네 번째로 오는 단어는?', P2, B('너는 그녀가 왜 울었다고 생각하니?'),
 ['think', 'why', 'she', 'cried', 'do'],
 "이유 ▶ Why(1) do(2) you(3) think(4) she(5) cried(6)?" + THINK, [])
T.flex('다음 중 어법상 <u>어색한</u> 문장은?', P1, '',
 ['Not she but I is in charge of the event.', 'Not only she but also I am in charge of the event.', 'Either she or I am in charge of the event.', 'She as well as I is in charge of the event.', 'Both she and I are in charge of the event.'],
 "이유 ▶ not A but B도 동사는 B(I)에 → am\n오답 ▶ {1} B(I) am ✔ {2} B(I) am ✔ {3} 앞(She) is ✔ {4} both → are ✔" + AGREE, [('in charge of', '~을 맡은')])
T.flex('다음 대화의 빈칸에 들어갈 말로 알맞은 것은?', P2, B('A: Can you tell me ' + BL + '?', "B: It's about 3 kilometers from here."),
 ['how far the station is', 'how far is the station', 'how the station is far', 'where the station far is', 'how far does the station'],
 "이유 ▶ 거리를 물음 → how far + 주어 + 동사\n오답 ▶ {1} 어순 {2} how far를 떼면 ❌ {3} 어순 {4} does ❌", [])
T.table('(A), (B)에 들어갈 말로 바르게 짝지은 것은?', P2, B('• Do you know what <b>(A)</b> [ happened / did happen ] to him?', '• Who do you think <b>(B)</b> [ will win / you will win ] the game?'),
 ['(A)', '(B)'], [['happened', 'will win'], ['did happen', 'will win'], ['happened', 'you will win'], ['did happen', 'you will win'], ['happens', 'win will']],
 "이유 ▶ (A) 의문사 what이 주어 → 바로 happened (B) who가 주어 → do you think 뒤에 바로 will win", [])
T.flex('다음 문장을 간접의문문으로 바꿀 때 빈칸에 알맞은 것은?', P2, B('He said to her, "Did you finish the work?"', '→ He asked her ' + BL + '.'),
 ['if she finished the work', 'if you finished the work', 'did she finish the work', 'whether did she finish the work', 'that she finished the work'],
 "이유 ▶ 의문사 없음 → if + 주어(you → she) + 동사(did 빼고 finished)\n오답 ▶ {1} 인칭 {2}·{3} 어순 {4} that ❌", [])
T.fixed('다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 <u>어색한</u> 것은?', X_, B(
 "I don't know ⓐ <u>what should I do</u>. My friend asked me ⓑ <u>where I was going</u> this weekend, but ⓒ <u>not only my mom but also my dad</u> ⓓ <u>wants</u> me to stay home. ⓔ <u>Why do you think</u> they want that?"),
 ['ⓐ', 'ⓑ', 'ⓒ', 'ⓓ', 'ⓔ'], 1,
 "이유 ▶ ⓐ → what I should do (의문사 + 주어 + 동사)\n오답 ▶ ⓑ 어순 ✔ ⓒ·ⓓ B(my dad) → wants ✔ ⓔ think → 의문사 맨 앞 ✔", [])
T.flex('&lt;보기&gt;에서 어법상 <u>틀린</u> 문장을 모두 고른 것은?', P2, B(
 '(A) Do you think why she is happy?', '(B) Can you tell me where did you go?', "(C) I don't know how I should go there.", '(D) What do you know the price is?', '(E) I wonder why you changed your job.'),
 ['(A), (B), (D)', '(A), (C), (E)', '(B), (C), (D)', '(A), (B), (E)', '(C), (D), (E)'],
 "이유 ▶ (A) Why do you think she is happy? (B) where you went (D) Do you know what the price is?\n오답 ▶ (C)·(E) 옳음" + THINK, [])
T.render()

# ═══════════════ 5세트 (최상) ═══════════════
T = Tset(5, '최상')
T.flex('빈칸에 들어갈 말을 순서대로 바르게 짝지은 것은?', P1, B('• Either Ben ' + BL + ' you have the key.', '• Both Sujin and Mina ' + BL + ' planning a trip.', '• Jake as well as I ' + BL + ' with the plan.'),
 ['or − are − agrees', 'nor − is − agree', 'nor − are − agree', 'or − are − agree', 'or − is − agrees'],
 "이유 ▶ either A or B / both → are / B as well as A → 앞(Jake) agrees" + AGREE, [])
T.fixed('다음 &lt;보기&gt;에서 어법상 옳은 문장의 개수는?', P1, B(
 '(a) She enjoys not only singing but also to dance.', '(b) Not only did she dance, but she also sings last night.', '(c) His words as well as his behavior upset me yesterday.', '(d) Not only Jane but also Eric likes math.', '(e) Not only the students but also the teacher were glad.', '(f) She as well as her friends have the same problem.'),
 NUMS, 2,
 "이유 ▶ 옳은 것 (c)·(d) 2개\n오답 ▶ (a) → dancing (b) last night → sang (e) B(the teacher) → was (f) 앞(She) → has" + AGREE, [('behavior', '행동')])
T.flex('다음 중 어법상 옳은 문장은?', P1, '',
 ["I'm interested not only in art but in history.", 'Not only he is a singer but also an actor.', 'Not only you but also she are pretty.', 'The place is not only wonderful but also a good one to visit.', 'Not only she can sing, but she also can dance.'],
 "이유 ▶ 전치사구끼리(in art / in history) ✔, also 생략 가능\n오답 ▶ {1} 도치 → Not only is he a singer, but he is also an actor. {2} B(she) → is {3} 형용사끼리 → good to visit {4} 도치 → Not only can she sing", [])
T.flex('다음 문장과 의미가 같은 것은?', P1, B('Mina not only sings well but also plays the piano well.'),
 ['Mina plays the piano well as well as sings well.', 'Mina just plays the piano well.', "Mina doesn't sing well but plays the piano well.", 'Mina sings well because she plays the piano well.', 'Mina neither sings nor plays the piano well.'],
 "이유 ▶ not only A but also B = B as well as A\n오답 ▶ {1} 피아노만 {2} 노래를 못함 {3} 이유로 바뀜 {4} 둘 다 못함", [])
T.flex('두 문장을 한 문장으로 바르게 만든 것은?', P1, '',
 ['Leo has been to Japan. Kyle has been to Japan, too.<br>→ Not only Leo but also Kyle has been to Japan.',
  'Ann is a teacher. She is also a writer.<br>→ Ann is not a teacher but a writer.',
  "Ted doesn't eat meat. He doesn't eat fish either.<br>→ Ted eats not only meat but also fish.",
  'The cook enjoys baking. He also enjoys singing.<br>→ The cook not only enjoys baking but also singing.',
  'My shoes are old. My bag is old, too.<br>→ Not only my shoes but also my bag are old.'],
 "이유 ▶ B(Kyle) → has ✔\n오답 ▶ {1} 교사가 아니라 작가 {2} 둘 다 안 먹음 → neither {3} 병렬 ❌ → enjoys not only baking but also singing {4} B(my bag) → is", [])
T.flex('다음 중 어법상 옳은 문장은?', P2, '',
 ['Do you know which color Ross likes better?', 'Do you suppose how far he can run?', 'He wondered what makes a noise like that last night.', 'The student knows how it is hard to be a scientist.', 'Do you think which one is smarter?'],
 "이유 ▶ which color + 주어 + 동사 ✔\n오답 ▶ {1} How far do you suppose he can run? {2} last night → made {3} how hard it is {4} Which one do you think is smarter?" + THINK, [])
T.flex('다음 중 어법상 <u>어색한</u> 문장은?', P2, '',
 ['Where do you think does he keep the file?', 'Why do you suppose she is upset?', "I don't know where this bus goes.", 'Why do you think he wants to be alone?', 'Do you know when the shop closes?'],
 "이유 ▶ does를 빼고 he keeps → Where do you think he keeps the file?\n오답 ▶ {1}·{3} 의문사 맨 앞 + 주어 + 동사 ✔ {2}·{4} 의문사 + 주어 + 동사 ✔" + THINK, [])
T.flex('두 문장을 한 문장으로 연결한 것 중 <u>어색한</u> 것은?', P2, '',
 ["I'd like to know. + Where did you go?<br>→ I'd like to know where you go.",
  'I need to know. + Where did you go last night?<br>→ I need to know where you went last night.',
  'Please tell me. + How long do I have to wait?<br>→ Please tell me how long I have to wait.',
  'I wonder. + Who ate my cookies?<br>→ I wonder who ate my cookies.',
  'Can I ask you? + How much is it?<br>→ Can I ask you how much it is?'],
 "이유 ▶ did를 빼면 시제는 동사로: where you went (go ❌)\n오답 ▶ {1}·{2}·{3}·{4} 바르게 연결", [])
T.flex('밑줄 친 부분 중 어법상 옳은 것은?', P2, '',
 ['No one knows <u>who made this robot</u>.', 'I asked him <u>what is his job</u>.', 'I wonder <u>if he will comes</u>.', "I don't know <u>how tall is he</u>.", 'Do you know <u>what she has a dog</u>?'],
 "이유 ▶ 의문사 who가 주어 → 바로 made ✔\n오답 ▶ {1} what his job was {2} will 뒤 원형 come {3} how tall he is {4} if(whether) she has a dog", [])
T.flex('짝지어진 두 문장의 의미가 서로 <u>다른</u> 것은?', P1, '',
 ["We may meet today. Or we may meet tomorrow. We don't know yet.<br>= We may meet not only today but also tomorrow.",
  "Not only Brielle's heart rate but also her temperature came back to normal.<br>= Her temperature as well as her heart rate came back to normal.",
  'He is strong, and he is fast, too.<br>= He is not only strong but also fast.',
  'Mina reads comics, and her sister does, too.<br>= Not only Mina but also her sister reads comics.',
  'Kids as well as adults love this game.<br>= Not only adults but also kids love this game.'],
 "이유 ▶ 오늘 또는 내일(둘 중 하나) → either today or tomorrow. not only ~ but also는 둘 다\n오답 ▶ {1}·{2}·{3}·{4} 같은 뜻", [('heart rate', '심장 박동 수')])
T.flex('&lt;보기&gt;에서 어법상 옳은 문장을 모두 고른 것은?', P2, B(
 'ⓐ I want to know where you live.', 'ⓑ Do you know what song she want to sing?', 'ⓒ What kind of book do you want to read?', 'ⓓ Do you think I should sleep more?', 'ⓔ Do you think what I can do for you?', 'ⓕ What do you think you will eat for lunch?', 'ⓖ The man wants to know how much is the bag.'),
 ['ⓐ, ⓒ, ⓓ, ⓕ', 'ⓐ, ⓓ, ⓕ', 'ⓑ, ⓔ, ⓖ', 'ⓑ, ⓒ, ⓓ, ⓕ', 'ⓐ, ⓒ, ⓔ, ⓕ'],
 "이유 ▶ ⓐ·ⓒ(직접의문문)·ⓓ(의문사 없는 Do you think ~?)·ⓕ 옳음\n오답 ▶ ⓑ she → wants ⓔ What do you think I can do ~? ⓖ how much the bag is" + THINK, [])
T.fixed('다음 &lt;보기&gt;에서 어법상 <u>틀린</u> 문장의 개수는?', P2, B(
 'ⓐ Do you know where she went yesterday?', 'ⓑ Let me know how much is one ticket.', 'ⓒ Do you think who will win?', 'ⓓ Do you know how giraffes live long?', 'ⓔ Do you remember when did you see him?', 'ⓕ I wonder if she is free now.'),
 NUMS, 4,
 "이유 ▶ 틀린 것 ⓑ·ⓒ·ⓓ·ⓔ 4개: how much one ticket is / Who do you think will win? / how long giraffes live / when you saw him" + ORDER, [('giraffe', '기린')])
T.flex('다음 문장의 틀린 곳을 바르게 고친 것은?', P2, B('Do you believe where did you lose it?'),
 ['Where do you believe you lost it?', 'Do you believe where you lost it?', 'Where do you believe did you lose it?', 'Where do you believe you lose it?', 'Do you believe where lost you it?'],
 "이유 ▶ believe → 의문사 맨 앞 + 주어 + 동사(과거 lost)\n오답 ▶ {1}·{4} 의문사가 뒤 {2} did 그대로 {3} 시제" + THINK, [])
T.flex('다음 빈칸에 if가 들어가기에 <u>어색한</u> 것은?', P2, '',
 ['The problem is ' + BL + ' you always stay up late.', 'She asked me ' + BL + ' I liked music.', 'Let him know ' + BL + ' he is invited or not.', "Can you tell me " + BL + " you're coming?", 'I wonder ' + BL + ' you understand me.'],
 "이유 ▶ 문제는 ~라는 것이다(보어) → that\n오답 ▶ {1}·{2}·{3}·{4} ~인지 아닌지 → if", [('stay up late', '늦게까지 깨어 있다')])
T.flex('다음 중 어법상 옳은 문장은?', P1, '',
 ["Not only my parents but also my brother doesn't like cats.", "Not only my parents but also my brother don't like cats.", "My brother as well as my parents don't like cats.", 'Neither my parents nor my brother like cats.', "Either my parents or my brother don't like cats."],
 "이유 ▶ B(my brother, 단수) → doesn't ✔\n오답 ▶ {1} → doesn't {2} 앞(My brother) → doesn't {3} B(my brother) → likes {4} B(my brother) → doesn't" + AGREE, [])
T.table('(A), (B)에 들어갈 말로 바르게 짝지은 것은?', P2, B('• Tell me what <b>(A)</b> [ make / makes ] a good friend.', '• Do you know who <b>(B)</b> [ eat / ate ] my sandwich?'),
 ['(A)', '(B)'], [['makes', 'ate'], ['make', 'ate'], ['makes', 'eat'], ['make', 'eat'], ['making', 'eaten']],
 "이유 ▶ 의문사가 주어면 3인칭 단수: (A) what makes (B) 이미 먹었으니 과거 ate (who eat ❌)", [])
T.fixed('다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 <u>어색한</u> 것은?', X_, B(
 'Not only Jisu ⓐ <u>but also her friends</u> ⓑ <u>were</u> invited to the party. They wondered ⓒ <u>what they should wear</u>. Jisu asked her mom ⓓ <u>if she could buy</u> a new dress. Her mom asked ⓔ <u>how much did it cost</u>.'),
 ['ⓐ', 'ⓑ', 'ⓒ', 'ⓓ', 'ⓔ'], 5,
 "이유 ▶ ⓔ → how much it cost (did를 빼고 과거 cost)\n오답 ▶ ⓑ B(her friends) → were ✔ ⓒ·ⓓ 어순 ✔", [])
T.flex('다음 우리말을 바르게 영작한 것은?', P2, B('너는 그 남자가 어디 출신이라고 생각하니?'),
 ['Where do you think the man is from?', 'Do you think where the man is from?', 'Where do you think is the man from?', 'Do you think where is the man from?', 'Where do you think the man from is?'],
 "이유 ▶ think → 의문사 맨 앞 + 주어 + 동사 + from\n오답 ▶ {1}·{3} 의문사가 뒤 {2}·{4} 어순" + THINK, [])
T.flex('다음 우리말을 바르게 영작한 것은?', P1, B('그는 음악뿐만 아니라 미술에도 관심이 있다.'),
 ['He is interested not only in music but also in art.', 'He is interested not in music but in art.', 'He is interested in neither music nor art.', 'He is interested in music as well as art.', 'He is interested either in music or in art.'],
 "이유 ▶ 음악뿐만 아니라(A) 미술에도(B) → not only in music but also in art\n오답 ▶ {1} 음악이 아니라 미술 {2} 둘 다 아님 {3} B as well as A → '미술뿐만 아니라 음악에도'(A·B 바뀜) {4} 둘 중 하나", [])
T.flex('다음 중 어법상 <u>어색한</u> 문장은?', X_, '',
 ['Do you know who are those people?', 'Not only Ben but also I am hungry.', 'I wonder whether she got my text.', 'Who do you think broke the vase?', 'She is not only kind but also brave.'],
 "이유 ▶ who those people are (who가 보어)\n오답 ▶ {1} B(I) am ✔ {2} whether + 주어 + 동사 ✔ {3} 의문사 주어 + think ✔ {4} 형용사끼리 ✔" + ORDER, [('brave', '용감한')])
T.render()
