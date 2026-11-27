# 11/27 중산중1 실전 문법 심화 2회 (5·6·7과 · 최상) 20문항 OMR m1hd-2 (m1-donga-yoon-L6 /* M1HD2-TESTS */ 블록)
# 1회보다 어렵게: 8문장 개수형, 고친 것 짝, 틀린 곳 2개, 의미가 같지 않은 짝, 빈칸 '모두' 조합, will이 들어갈 수 없는 것 등. 정답 ①~⑤ 4개씩(개수형은 자리 고정, 나머지를 돌려 맞춤)
import json, re, sys
path = '/home/claude/proj/data/m1-donga-yoon-L6.js'
W = lambda *ps: '<div class="wbox">' + ''.join('<p>%s</p>' % p for p in ps) + '</div>'
CNT = ['1개', '2개', '3개', '4개', '5개']
# (출처, 발문, 본문, 선택지(첫 번째가 정답 — CNT면 ans로 자리 고정), ans(None=첫 번째), 해설)
I = [
 ('종합', '다음 중 어법상 <u>어색한</u> 문장의 개수는?',
  W('(a) There are much water in the bottle.', '(b) I hope that you will get well soon.', '(c) She is the smartest of all the students.', '(d) He gave up to play soccer.',
    '(e) When I will finish my work, I’ll call you.', '(f) This box is even heavier than that one.', '(g) We went to the park to fly kites.', '(h) My brother is one of the tallest boy in his class.'), CNT, 3,
  "어색한 것 (a)·(d)·(e)·(h) → 4개\n(a) water는 셀 수 없음 → There is much water\n(d) give up + 동명사 → gave up playing\n(e) 때의 부사절은 미래도 현재형 → When I finish\n(h) one of the + 최상급 + 복수 명사 → boys\n옳은 것 ▶ (b) hope + 접속사 that (c) the + 최상급 + of (f) even + 비교급 (g) 목적 to부정사"),
 ('종합', '다음 중 어법상 올바른 문장끼리 바르게 짝지은 것은?',
  W('ⓐ Is there any milk in the fridge?', 'ⓑ She decided not going there.', 'ⓒ After she eats lunch tomorrow, she will go shopping.', 'ⓓ I think that Minsu is much kinder than his brother.', 'ⓔ My dream is become a doctor.'),
  ['ⓐ, ⓒ, ⓓ', 'ⓐ, ⓑ', 'ⓑ, ⓒ, ⓔ', 'ⓒ, ⓓ, ⓔ', 'ⓐ, ⓓ, ⓔ'], None,
  "옳은 것 ⓐ·ⓒ·ⓓ\nⓐ milk(셀 수 없음) → Is there ✓ ⓒ 부사절 현재형(eats) + 주절 will ✓ ⓓ 접속사 that + much 비교급 ✓\n틀린 것 ▶ ⓑ decide not to + 동사원형 → decided not to go ⓔ 보어 자리 to부정사 → is to become"),
 ('to부정사 부사적', '<보기>의 밑줄 친 부분과 쓰임이 같은 것의 개수는?',
  W('&lt;보기&gt; He studied hard <u>to pass</u> the test.', '(a) She went to the bakery <u>to buy</u> some bread.', '(b) I was surprised <u>to see</u> him there.', '(c) They want <u>to visit</u> Paris.',
    '(d) He saved money <u>to buy</u> a new bike.', '(e) This river is dangerous <u>to swim</u> in.', '(f) We got up early <u>to see</u> the sunrise.'), CNT, 2,
  "<보기> = 목적(~하기 위해서). 같은 것 (a)·(d)·(f) → 3개\n다른 것 ▶ (b) 감정의 원인 '봐서 놀랐다' (c) 명사적(want의 목적어) (e) 형용사 수식 '수영하기에 위험한'"),
 ('접속사 that', '다음 빈칸에 공통으로 들어갈 말로 알맞은 것은? (대·소문자 무시)',
  W('• I believe ______ he is honest.', '• Do you know ______ she moved to Busan?', '• ______ is my favorite song.'),
  ['that', 'what', 'it', 'this', 'which'], None,
  "① ② 접속사 that(~라는 것, 뒤에 완전한 문장) ③ 지시대명사 That(저것)\n오답 ▶ what은 뒤가 불완전해야 함(he is honest는 완전) / this·it은 첫째·둘째 빈칸에 못 들어감"),
 ('when · before · after', '다음 두 문장을 한 문장으로 바르게 바꾼 것은?', W('Jimin finished her homework. Then she watched TV.'),
  ['Before Jimin watched TV, she finished her homework.', 'Jimin watched TV before she finished her homework.', 'After Jimin watched TV, she finished her homework.', 'Jimin finished her homework after she watched TV.', 'When Jimin watched TV, she finished her homework.'], None,
  "숙제를 먼저 끝내고 → 그다음 TV. 'TV를 보기 전에 숙제를 끝냈다' = Before Jimin watched TV, she finished her homework.\n오답 ▶ ②③④ 순서가 거꾸로 ⑤ 동시에 한 일이 됨\n포인트 ▶ before 뒤 = 나중 일, after 뒤 = 먼저 한 일"),
 ('종합', '다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 <u>틀린</u> 것의 개수는?',
  W('Last weekend, my family decided <u>ⓐ to go</u> camping. There <u>ⓑ was</u> many people at the campsite. We were happy <u>ⓒ to find</u> a good spot near the river. My dad said <u>ⓓ that</u> the river was cleaner than the one near our house. Before we <u>ⓔ will go</u> to bed, we looked at the stars.'),
  CNT, 1,
  "틀린 것 ⓑ·ⓔ → 2개\nⓑ many people(복수) → were\nⓔ 지난 일 + 때의 부사절에 will ✘ → Before we went to bed\n옳은 것 ▶ ⓐ decide + to부정사 ⓒ 감정의 원인 to부정사 ⓓ said의 목적어절 접속사 that"),
 ('종합', '다음 글의 밑줄 친 부분을 바르게 고친 것끼리 짝지은 것은?',
  W('Mina enjoys <u>ⓐ to read</u> books. She wants <u>ⓑ becoming</u> a writer. There <u>ⓒ is</u> lots of books in her room. Her room is <u>ⓓ more big</u> than mine. She hopes <u>ⓔ that</u> she will win the contest.'),
  ['ⓐ → reading, ⓑ → to become', 'ⓑ → become, ⓒ → are', 'ⓒ → am, ⓓ → bigger', 'ⓓ → biggest, ⓔ → what', 'ⓐ → read, ⓓ → much big'], None,
  "ⓐ enjoy + 동명사 → reading ✓ ⓑ want + to부정사 → to become ✓\n오답 ▶ ② ⓑ become ✘ ③ ⓒ am ✘(lots of books → are) ④ ⓓ biggest ✘(than 앞 비교급 bigger), ⓔ that은 원래 맞음 ⑤ ⓐ read ✘, much big ✘"),
 ('to부정사 부사적', '다음 우리말을 영어로 바르게 옮긴 것은?', W('나는 그 소식을 들어서 매우 기뻤다.'),
  ['I was very glad to hear the news.', 'I was very glad hear the news.', 'I was very glad to heard the news.', 'I was very glad that hear the news.', 'I was very glad to hearing the news.'], None,
  "감정(glad) + to부정사(원인) = ~해서 기뻤다 → to + 동사원형 hear\n오답 ▶ ② to 빠짐 ③ to + 과거형 ✘ ④ that 뒤에 주어 없음 ⑤ to + -ing ✘"),
 ('종합', '다음 중 어법상 <u>옳은</u> 문장의 개수는?',
  W('(a) Are there any oranges in the basket?', '(b) She runs fastest in her class.', '(c) I need finishing this report today.', '(d) He was disappointed to lose the game.', '(e) When he comes back next week, we will have a party.', '(f) I know what he is a famous singer.'),
  CNT, 3,
  "옳은 것 (a)·(b)·(d)·(e) → 4개\n틀린 것 ▶ (c) need + to부정사 → need to finish (f) 뒤가 완전한 문장 → 접속사 that\n옳은 것 ▶ (a) oranges(복수) → Are there (b) 부사 fast의 최상급 fastest(the 생략 가능) (d) 감정의 원인 (e) 부사절 현재형"),
 ('접속사 that', '<보기>의 밑줄 친 that과 쓰임이 같은 것은?', W('&lt;보기&gt; I think <u>that</u> she is right.'),
  ['We knew <u>that</u> the store was closed.', '<u>That</u> girl is my cousin.', 'Who is <u>that</u> over there?', 'I can’t believe <u>that</u>!', 'Look at <u>that</u> cute puppy.'], None,
  "<보기> = 접속사(뒤에 주어+동사). ① knew 뒤 the store was closed → 접속사\n오답 ▶ ②⑤ 지시형용사 '저 ~' ③④ 지시대명사 '저 사람/그것'"),
 ('to부정사 쓰임', '다음 밑줄 친 to부정사 중 쓰임이 같은 것끼리 바르게 짝지은 것은?',
  W('(a) <u>To learn</u> a new language is fun.', '(b) My hobby is <u>to collect</u> stamps.', '(c) She went to Seoul <u>to meet</u> her aunt.', '(d) He was excited <u>to ride</u> the roller coaster.', '(e) I decided <u>to join</u> the club.', '(f) The math problem is hard <u>to solve</u>.'),
  ['(a), (b), (e)', '(a), (c)', '(b), (d)', '(c), (e)', '(d), (e)'], None,
  "(a) 주어 (b) 보어 (e) 목적어 → 모두 명사적 용법 '~하는 것'\n나머지 ▶ (c) 목적 (d) 감정의 원인 (f) 형용사 수식 → 부사적 용법"),
 ('to부정사 명사적', '다음 빈칸에 들어갈 수 있는 말을 <u>모두</u> 고른 것은?', W('Tom ________ to travel around the world.', '(a) wants　(b) enjoys　(c) hopes　(d) finished　(e) plans'),
  ['(a), (c), (e)', '(a), (b)', '(b), (d)', '(c), (d), (e)', '(a), (b), (c), (e)'], None,
  "want·hope·plan + to부정사 → (a)(c)(e)\n오답 ▶ enjoy·finish는 동명사(-ing)만 → enjoys traveling, finished traveling"),
 ('비교급·최상급', '다음 표의 내용을 바르게 나타낸 것은?', W('Ann — 160 cm · 45 kg　|　Ben — 165 cm · 50 kg　|　Cindy — 158 cm · 52 kg'),
  ['Cindy is the heaviest of the three.', 'Ann is taller than Ben.', 'Ben is shorter than Cindy.', 'Ann is heavier than Cindy.', 'Cindy is the tallest of the three.'], None,
  "몸무게 Cindy 52 > Ben 50 > Ann 45 → Cindy가 가장 무겁다 ✓\n오답 ▶ ② Ann 160 < Ben 165 ③ Ben 165 > Cindy 158 ④ Ann 45 < Cindy 52 ⑤ 가장 큰 사람은 Ben"),
 ('There is/are', '다음 빈칸 (A)~(C)에 들어갈 말로 어법상 알맞은 것끼리 짝지은 것은?',
  W('• There ___(A)___ a lot of money in his wallet.', '• There ___(B)___ five apples on the table.', '• ___(C)___ there any students in the classroom?'),
  ['is – are – Are', 'are – are – Is', 'is – is – Are', 'are – is – Is', 'is – are – Is'], None,
  "(A) money는 셀 수 없음 → is (a lot of가 있어도) (B) five apples → are (C) any students(복수) → Are"),
 ('to부정사 부사적', '다음 문장과 의미가 같도록 어법에 맞게 바꾼 것은?', W('Sora was very happy because she won the prize.'),
  ['Sora was very happy to win the prize.', 'Sora was very happy winning to the prize.', 'Sora won the prize to be very happy.', 'Sora was very happy for win the prize.', 'Sora was very happy to won the prize.'], None,
  "because(원인) → 감정 + to부정사(원인) 'to win'\n오답 ▶ ② 어순·형태 ✘ ③ '행복해지려고 상을 탔다'로 뜻이 바뀜 ④ for + 동사원형 ✘ ⑤ to + 과거형 ✘"),
 ('종합', '다음 짝지어진 두 문장의 의미가 서로 <u>다른</u> 것은?', '',
  ['After she washed her hands, she ate dinner. = She washed her hands after she ate dinner.', 'I went to the library to study. = I went to the library so that I could study.', 'This book is easier than that book. = That book is more difficult than this book.', 'Before I left home, I locked the door. = I locked the door before I left home.', 'I think that he is honest. = I think he is honest.'], None,
  "① 앞: 손 씻기 → 저녁 / 뒤: 저녁 → 손 씻기 (순서가 바뀜)\n나머지 ▶ ② 목적 to = so that ~ could ③ 쉽다 ↔ 어렵다로 바꿔 같은 뜻 ④ before 절의 위치만 바뀜 ⑤ 목적어절 that 생략"),
 ('비교급·최상급', '다음 중 어법상 <u>틀린</u> 것은?', '',
  ['He is one of the most famous singer in Korea.', 'Seoul is one of the biggest cities in Asia.', 'This is the most interesting movie of the three.', 'My bag is a lot lighter than yours.', 'Jane is the youngest in her family.'], None,
  "one of the + 최상급 + 복수 명사 → singers\n옳은 것 ▶ ② cities(복수) ③ the most + 형용사 + of the three ④ a lot + 비교급 ⑤ the + 최상급 + in"),
 ('종합', '다음 글의 (A)~(C)의 각 네모 안에서 어법에 맞는 표현을 바르게 짝지은 것은?',
  W('Yesterday, I went to the market (A) [ to buy / buying ] some fruit. There (B) [ were / was ] lots of fresh strawberries. I hope (C) [ that / what ] my mom will like them.'),
  ['to buy – were – that', 'to buy – was – what', 'buying – were – that', 'buying – was – what', 'to buy – was – that'], None,
  "(A) 과일을 '사러' → 목적 to buy (B) lots of strawberries(복수) → were (C) hope의 목적어, 뒤가 완전한 문장 → 접속사 that"),
 ('when · before · after', '다음 빈칸에 will이 들어갈 수 <u>없는</u> 것은?', '',
  ['When he ______ come back, I’ll tell him.', 'I think it ______ rain tomorrow.', 'She ______ visit her grandma next week.', 'I hope you ______ enjoy the party.', 'We ______ go camping this weekend.'], None,
  "① 때를 나타내는 부사절(When ~)은 미래 일도 현재형 → When he comes back (will ✘)\n나머지 ▶ 주절·목적어절이라 will로 미래를 나타냄"),
 ('종합', '다음 글에서 어법상 <u>틀린</u> 곳 두 개를 찾아 바르게 고친 것은?',
  W('Minho finished <u>ⓐ to do</u> his homework. Then he went out <u>ⓑ to play</u> soccer. He was happy <u>ⓒ to score</u> a goal. His team was <u>ⓓ much better</u> than the other team. After the game <u>ⓔ will end</u>, he went home.'),
  ['ⓐ → doing, ⓔ → ended', 'ⓑ → playing, ⓔ → ends', 'ⓐ → doing, ⓓ → very better', 'ⓒ → scoring, ⓔ → ended', 'ⓓ → more good, ⓔ → ending'], None,
  "ⓐ finish + 동명사 → doing ⓔ 지난 일, 부사절에 will ✘ → ended\n옳은 것 ▶ ⓑ 목적 to부정사 ⓒ 감정의 원인 ⓓ much + 비교급"),
]
assert len(I) == 20
fixed = [k for k, x in enumerate(I) if x[3] is CNT]
need = {k: 4 for k in range(5)}
for k in fixed: need[I[k][4]] -= 1
assert all(v >= 0 for v in need.values()), need
pool = sum([[k] * need[k] for k in range(5)], [])
order = [0, 2, 4, 1, 3, 4, 0, 2, 3, 1, 4, 2, 0, 3, 1, 4, 2, 0, 1, 3]
items = []
for n, (src_, stem, body, opts, ans, ex) in enumerate(I, 1):
    if opts is CNT: o, a = list(CNT), ans
    else:
        a = next(k for k in order[n - 1:] + order + list(range(5)) if k in pool); pool.remove(a)
        o = list(opts); right = o.pop(0); o.insert(a, right)
    assert len(o) == 5 and len(set(o)) == 5
    items.append({'n': n, 'src': src_, 'stem': stem, 'body': body, 'opts': o, 'en': True, 'ans': a, 'ex': '정답 ▶ %s\n이유 ▶ %s' % ('①②③④⑤'[a], ex), 'ctx': '', 'pts': 5, 'words': [], 'kos': []})
from collections import Counter
c = Counter(it['ans'] for it in items); assert all(c[k] == 4 for k in range(5)), c
T = {'id': 'm1hd-2', 'title': '실전 문법 심화 2회 (5·6·7과 · 최상)', 'short': '문법 심화 2회', 'school': '중산중 1학년', 'minutes': 35, 'items': items}
src = open(path, encoding='utf-8').read()
src = re.sub(r'/\* M1HD2-TESTS.*?/\* /M1HD2-TESTS \*/\n?', '', src, flags=re.S)
src = src.rstrip('\n') + '\n/* M1HD2-TESTS: gen/m1hd/build2.py 로 만듦 (손으로 고치지 말 것) */\nwindow.PKG.tests = (window.PKG.tests || []).filter(function (t) { return t.id !== "m1hd-2"; }).concat([%s]);\n/* /M1HD2-TESTS */\n' % json.dumps(T, ensure_ascii=False)
open(path, 'w', encoding='utf-8').write(src)
print('ok', ''.join('①②③④⑤'[it['ans']] for it in items))
