# 11/26 중산중1 동아(윤정미) 5·6·7과 시험범위 어법 '상' 난이도 20문항 OMR 시험 m1hd-1 (m1-donga-yoon-L6 맨 끝 /* M1HD-TESTS */ 블록)
# 범위 문법: 5과 There is/are · 비교급/최상급, 6과 접속사 that · to부정사 명사적, 7과 to부정사 부사적 · when/before/after(미래 대신 현재)
# 정답 ①~⑤ 4개씩. 답이 둘이 될 수 있는 보기는 뺌(예: Wash your hands after you eat → (A) 빈칸 바꿈)
import json, re, sys
path = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/proj/data/m1-donga-yoon-L6.js'
W = lambda *ps: '<div class="wbox">' + ''.join('<p>%s</p>' % p for p in ps) + '</div>'
CNT = ['1개', '2개', '3개', '4개', '5개']
I = [
 ('종합', '다음 <보기>에서 어법상 <u>어색한</u> 문장의 개수는?',
  W('(a) There is a lot of books on the shelf.', '(b) She finished to clean her room before dinner.', '(c) I think that he is the kindest boy in our class.',
    '(d) When she will arrive, I’ll call you.', '(e) My bag is much heavier than yours.', '(f) He went to the store to buy some milk.'), CNT, 2,
  "이유 ▶ 어색한 것은 (a)·(b)·(d) 3개.\n(a) a lot of books(복수) → There are\n(b) finish는 -ing만 → finished cleaning\n(d) 때를 나타내는 부사절은 미래라도 현재형 → When she arrives\n옳은 것 ▶ (c) 접속사 that + 최상급 (e) much + 비교급 강조 (f) 목적 '사러'"),
 ('종합', '다음 중 어법상 올바른 문장끼리 바르게 짝지은 것은?',
  W('ⓐ Is there any water in the bottle?', 'ⓑ This is the most popular song of the three songs.', 'ⓒ We decided going camping this weekend.',
    'ⓓ I was surprised to hear the news.', 'ⓔ After he will finish his homework, he will play games.'),
  ['ⓐ, ⓒ', 'ⓑ, ⓔ', 'ⓐ, ⓑ, ⓓ', 'ⓑ, ⓒ, ⓓ', 'ⓐ, ⓓ, ⓔ'], 2,
  "이유 ▶ 옳은 것은 ⓐ·ⓑ·ⓓ.\nⓐ water(셀 수 없음) → Is there ✓ ⓑ the most + 형용사 + of the three ✓ ⓓ 감정의 원인 to부정사 ✓\n틀린 것 ▶ ⓒ decide는 to부정사 → decided to go ⓔ After he finishes (부사절은 현재형)"),
 ('접속사 that', '다음 밑줄 친 that의 쓰임이 나머지 넷과 <u>다른</u> 것은?', '',
  ['I learned <u>that</u> the earth is round.', 'She knows <u>that</u> I like her.', 'We were glad <u>that</u> you came.', 'Is <u>that</u> your new bike?', 'I didn’t know <u>that</u> Tom was sick.'], 3,
  "이유 ▶ ④ that = '저것'(지시대명사), 뒤에 주어+동사가 없음.\n나머지 ▶ 뒤에 완전한 문장(주어+동사)이 오는 접속사 that '~라는 것' (③ glad 뒤 감정의 내용도 접속사)"),
 ('to부정사 쓰임', '다음 밑줄 친 to부정사 중 쓰임이 같은 것끼리 바르게 짝지은 것은?',
  W('(a) My dream is <u>to become</u> a pilot.', '(b) She went to the library <u>to borrow</u> books.', '(c) I was happy <u>to win</u> the race.',
    '(d) He wants <u>to travel</u> around the world.', '(e) This question is hard <u>to answer</u>.', '(f) <u>To exercise</u> every day is not easy.'),
  ['(a), (b)', '(b), (d)', '(a), (d), (f)', '(a), (e)', '(c), (d), (f)'], 2,
  "이유 ▶ (a) 보어 (d) 목적어 (f) 주어 → 모두 명사적 용법 '~하는 것'.\n나머지 ▶ (b) 목적 '빌리러' (c) 감정의 원인 '이겨서' (e) 형용사 수식 '대답하기에' → 부사적 용법"),
 ('to부정사 부사적', "밑줄 친 to부정사의 쓰임이 '~하기 위해서'인 것은?", '',
  ['I hope <u>to see</u> you again.', 'She was sad <u>to leave</u> her friends.', 'He grew up <u>to be</u> a famous singer.', 'They got up early <u>to catch</u> the first bus.', 'This book is easy <u>to read</u>.'], 3,
  "이유 ▶ ④ 첫 버스를 '타기 위해' 일찍 일어났다 → 목적.\n오답 ▶ ① 명사적(hope의 목적어) ② 감정의 원인 '떠나서' ③ 결과 '자라서 ~가 되었다' ⑤ 형용사 수식 '읽기에'"),
 ('when · before · after', '다음 두 문장을 한 문장으로 바르게 바꾼 것은?', W('I brushed my teeth. Then I went to bed.'),
  ['I brushed my teeth after I went to bed.', 'I went to bed after I brushed my teeth.', 'I went to bed before I brushed my teeth.', 'After I went to bed, I brushed my teeth.', 'Before I brushed my teeth, I went to bed.'], 1,
  "이유 ▶ 이를 닦은 '뒤에' 잤다 → I went to bed after I brushed my teeth.\n오답 ▶ ①③④⑤ 모두 '잔 뒤에 이를 닦았다'로 순서가 거꾸로\n포인트 ▶ after 뒤 = 먼저 한 일, before 뒤 = 나중에 한 일"),
 ('종합', '다음 빈칸 (A)~(C)에 들어갈 말로 어법상 알맞은 것끼리 짝지은 것은?',
  W('• There ___(A)___ some juice in the fridge.', '• When she ___(B)___ home tomorrow, I will give her the gift.', '• Mina runs ___(C)___ of all the students in her class.'),
  ['is – comes – the fastest', 'are – comes – faster', 'is – will come – the fastest', 'are – will come – faster', 'is – came – the faster'], 0,
  "이유 ▶ (A) juice(셀 수 없음) → is (B) 때의 부사절은 미래라도 현재형 → comes (C) of all ~ '모두 중에서' → 최상급 the fastest\n오답 ▶ will come ❌(부사절) / came ❌(tomorrow) / faster·the faster ❌(of all 뒤는 최상급)"),
 ('종합', '다음 글의 밑줄 친 ①~⑤ 중 어법상 <u>틀린</u> 것은?',
  W('Last Saturday, I decided <u>① to clean</u> my room. There <u>② were</u> many old toys under my bed. I found <u>③ that</u> my favorite robot was broken. I was sad <u>④ to see</u> it. After I <u>⑤ will finish</u> cleaning, I took a long shower.'),
  ['①', '②', '③', '④', '⑤'], 4,
  "이유 ▶ ⑤ 지난 일이고, 때의 부사절에는 will을 쓰지 않음 → After I finished cleaning\n옳은 것 ▶ ① decide + to부정사 ② many old toys(복수, 과거) → were ③ found의 목적어절 접속사 that ④ 감정의 원인 to부정사"),
 ('종합', '다음 우리말을 영어로 바르게 옮긴 것은?', W('나는 그가 우리 반에서 가장 빨리 달린다고 생각한다.'),
  ['I think he runs the faster in our class.', 'I think that he run the fastest in our class.', 'I think that he runs most fast in our class.', 'I think what he runs the fastest in our class.', 'I think that he runs the fastest in our class.'], 4,
  "이유 ▶ think + (that) 주어 + 동사 / 주어 he → runs / fast의 최상급 fastest\n오답 ▶ ① the faster ❌(최상급) ② he run ❌(runs) ③ most fast ❌(fastest) ④ what ❌(접속사 that)"),
 ('to부정사 명사적', '다음 빈칸에 들어갈 말로 어법상 알맞지 <u>않은</u> 것은?', W('She ________ to learn Chinese.'),
  ['wants', 'decided', 'hopes', 'enjoyed', 'planned'], 3,
  "이유 ▶ enjoy는 동명사(-ing)만 목적어로 → She enjoyed learning Chinese.\n나머지 ▶ want·decide·hope·plan + to부정사"),
 ('비교급', '다음 빈칸에 들어갈 말로 어법상 알맞지 <u>않은</u> 것은?', W('My room is ________ bigger than yours.'),
  ['much', 'very', 'even', 'far', 'a lot'], 1,
  "이유 ▶ 비교급을 강조할 때는 much·even·far·a lot(훨씬). very는 원급만 꾸밈(very big ✓, very bigger ❌)"),
 ('종합', '다음 중 어법상 올바른 문장은?', '',
  ['There are much water in the lake.', 'She is one of the smartest student in her school.', 'He was disappointed to lose the game.', 'I’m sure that she will passes the test.', 'Before he goes to school tomorrow, he will eats breakfast.'], 2,
  "이유 ▶ ③ 감정(disappointed) + to부정사(원인) '져서 실망했다' ✓\n오답 ▶ ① much water → There is ② one of the + 최상급 + 복수 명사 → students ④ will + 동사원형 → will pass ⑤ will eats → will eat"),
 ('접속사 that', '다음 밑줄 친 that 중 쓰임상 생략할 수 있는 것은?', '',
  ['I think <u>that</u> this answer is wrong.', '<u>That</u> is my sister, Jimin.', 'I really like <u>that</u> red cap.', 'Look at <u>that</u> tall man over there.', '<u>That</u> was a great movie.'], 0,
  "이유 ▶ ① think의 목적어절을 이끄는 접속사 that → 생략 가능 (I think this answer is wrong.)\n오답 ▶ ②⑤ 지시대명사 '저것/그것' ③④ 지시형용사 '저 ~' → 생략하면 뜻이 바뀌거나 문장이 안 됨"),
 ('종합', '다음 <보기>에서 어법상 <u>옳은</u> 문장의 개수는?',
  W('(a) My brother is two years older than me.', '(b) This is the more expensive bag in this store.', '(c) They practiced hard to win the game.',
    '(d) Is there many people in the park?', '(e) We hope that you will enjoy the trip.', '(f) When I was young, I lived in Busan.'), CNT, 3,
  "이유 ▶ 옳은 것은 (a)·(c)·(e)·(f) 4개.\n틀린 것 ▶ (b) in this store '이 가게에서' → 최상급 the most expensive (d) many people(복수) → Are there\n옳은 것 ▶ (a) 비교급 + than (c) 목적 to부정사 (e) 접속사 that (f) when + 과거"),
 ('to부정사 부사적', '<보기>의 밑줄 친 부분과 쓰임이 같은 것은?', W('I was excited <u>to meet</u> the singer.'),
  ['She went outside <u>to get</u> some fresh air.', 'He was surprised <u>to see</u> me there.', 'My plan is <u>to visit</u> Jeju this summer.', 'The water is safe <u>to drink</u>.', 'She grew up <u>to be</u> a doctor.'], 1,
  "이유 ▶ <보기> excited + to meet = 만나서 신났다(감정의 원인). ② surprised + to see '봐서 놀랐다'도 감정의 원인.\n오답 ▶ ① 목적 ③ 명사적(보어) ④ 형용사 수식 '마시기에' ⑤ 결과"),
 ('to부정사 부사적', '다음 문장과 의미가 같도록 어법에 맞게 바꾼 것은?', W('She studied hard so that she could pass the exam.'),
  ['She studied hard to pass the exam.', 'She studied hard passing the exam.', 'She studied hard for pass the exam.', 'She passed the exam to study hard.', 'She studied hard in order passing the exam.'], 0,
  "이유 ▶ so that ~ can '~할 수 있도록' = to부정사(목적) → to pass (= in order to pass)\n오답 ▶ ② -ing ❌ ③ for + 동사원형 ❌ ④ 뜻이 바뀜(공부하려고 합격?) ⑤ in order to pass로 써야 함"),
 ('비교급·최상급', '다음 표의 내용을 비교급·최상급으로 바르게 나타낸 것은?',
  W('Tom — 15살 · 165 cm　|　Jake — 14살 · 170 cm　|　Ryan — 16살 · 168 cm'),
  ['Tom is older than Ryan.', 'Jake is the tallest of the three.', 'Ryan is younger than Jake.', 'Tom is taller than Ryan.', 'Jake is the oldest of the three.'], 1,
  "이유 ▶ 키: Jake 170 > Ryan 168 > Tom 165 → Jake가 가장 크다 ✓\n오답 ▶ ① Tom 15 < Ryan 16 ③ Ryan 16 > Jake 14 ④ Tom 165 < Ryan 168 ⑤ 가장 나이 많은 사람은 Ryan"),
 ('when · before · after', '다음 빈칸 (A)~(C)에 들어갈 말로 어법상 알맞은 것끼리 짝지은 것은?',
  W('• Look both ways ___(A)___ you cross the street.', '• ___(B)___ I got home, my mom was cooking dinner.', '• We went out to play ___(C)___ it stopped raining.'),
  ['before – When – after', 'after – When – before', 'before – After – before', 'after – Before – after', 'after – After – when'], 0,
  "이유 ▶ (A) 길을 건너기 '전에' 양쪽을 본다 → before (B) 집에 왔을 '때' 엄마가 요리 중 → When (C) 비가 그친 '후에' 놀러 나갔다 → after\n오답 ▶ (A) after ❌(건넌 뒤에 보면 소용없음) (C) before ❌(비가 그치기 전에 놀러 감 ✘)"),
 ('종합', '다음 밑줄 친 부분을 어법상 바르게 고친 것이 <u>아닌</u> 것은?', '',
  ['She enjoys <u>to swim</u> in the sea. → swimming', 'There <u>is</u> many cars on the road. → are', 'He is <u>tallest</u> than me. → taller', 'I hope <u>seeing</u> you soon. → to see', 'I went to the shop <u>buy</u> some bread. → buying'], 4,
  "이유 ▶ ⑤ '빵을 사러' 가게에 갔다 → 목적의 to부정사 to buy로 고쳐야 함 (buying ❌)\n나머지 ▶ ① enjoy + -ing ② many cars → are ③ than 앞은 비교급 ④ hope + to부정사 → 모두 바르게 고침"),
 ('종합', '다음 글의 (A)~(C)의 각 네모 안에서 어법에 맞는 표현을 바르게 짝지은 것은?',
  W('Yesterday was (A) [ the most / the more ] exciting day of my life. My uncle took me to a baseball stadium (B) [ to watch / watching ] a game. I hope (C) [ that / what ] I can go there again soon.'),
  ['the more – to watch – what', 'the more – watching – that', 'the most – watching – that', 'the most – to watch – what', 'the most – to watch – that'], 4,
  "이유 ▶ (A) of my life '내 인생에서' → 최상급 the most (B) 경기를 '보러' → 목적 to watch (C) hope의 목적어, 뒤가 완전한 절 → 접속사 that"),
]
E = lambda s: s
items = []
for n, (src, stem, body, opts, ans, ex) in enumerate(I, 1):
    assert len(opts) == 5 and 0 <= ans < 5
    items.append({'n': n, 'src': src, 'stem': stem, 'body': body, 'opts': opts, 'en': True, 'ans': ans, 'ex': ('정답 ▶ %s\n' % '①②③④⑤'[ans]) + ex, 'ctx': '', 'pts': 5, 'words': [], 'kos': []})
from collections import Counter
c = Counter(it['ans'] for it in items); assert len(items) == 20 and all(c[i] == 4 for i in range(5)), c
T = {'id': 'm1hd-1', 'title': '실전 문법 심화 (5·6·7과 · 상)', 'short': '문법 심화', 'school': '중산중 1학년', 'minutes': 30, 'items': items}
src = open(path, encoding='utf-8').read()
src = re.sub(r'/\* M1HD-TESTS.*?/\* /M1HD-TESTS \*/\n?', '', src, flags=re.S)
src = src.rstrip('\n') + '\n/* M1HD-TESTS: gen/m1hd/build.py 로 만듦 (손으로 고치지 말 것) */\nwindow.PKG.tests = (window.PKG.tests || []).filter(function (t) { return t.id !== "m1hd-1"; }).concat([%s]);\n/* /M1HD-TESTS */\n' % json.dumps(T, ensure_ascii=False)
open(path, 'w', encoding='utf-8').write(src)
print('ok', dict(c))
