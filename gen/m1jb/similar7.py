# 11/28 중산중1 족보 7과(문법 공략 01: to부정사 부사적·when/before/after) 유사문제 1세트 (보충) 25문항 → /* M1JB7S-TESTS */ m1jb-7s
# 족보 1~25번 유형을 번호별로 따라 새 문장. 종이 시험지 + 앱 OMR, kind exam + retry 1
import json, re
from collections import Counter
path = '/home/claude/proj/data/m1-donga-yoon-L6.js'
W = lambda *ps: '<div class="wbox">' + ''.join('<p>%s</p>' % p for p in ps) + '</div>'
CNT = ['1개', '2개', '3개', '4개', '5개']
CNTM = ['1명', '2명', '3명', '4명', '5명']
I = [
 ('대화 · 요약 어법', '주어진 대화를 참고할 때, 요약문의 밑줄 친 ⓐ~ⓔ 중 어법상 자연스러운 것은?',
  W('G: Minho, what do you want to be in the future?', "B: I want to be a chef. I'm interested in cooking Korean food.", "G: That's great. I'm interested in drawing, so I want to be a cartoonist.", "B: Cool! Let's go to the bookstore to buy some cartoon books.",
    '&lt;요약&gt; Minho ⓐ<u>want</u> to be a chef. He is interested in ⓑ<u>cook</u> Korean food. The girl wants to be a cartoonist ⓒ<u>because</u> she is interested in drawing. Minho suggests ⓓ<u>go</u> to the bookstore. They will go there ⓔ<u>buying</u> some cartoon books.'),
  ['ⓐ', 'ⓑ', 'ⓒ', 'ⓓ', 'ⓔ'], ('fix', 2),
  "ⓒ because + 주어 + 동사(이유) ✓\nⓐ Minho(3인칭 단수) → wants ⓑ 전치사 in + 동명사 → cooking ⓓ suggest + 동명사 → going ⓔ 목적(~하기 위해) → to buy"),
 ('to부정사 목적', '다음 우리말을 가장 적절하게 영작한 것은?', W('동물에 대해 배우기 위해, 나는 그 책을 읽을 거예요.'),
  ["I'm going to read the book to learn about animals.", "I'm reading the book to learning about animals.", "To read the book, I'm going to learn about animals.", "I'm going to read the book in order to learning about animals.", "For learn about animals, I'm going to read the book."], None,
  "목적(~하기 위해) → to + 동사원형 learn\n오답 ▶ ② to + -ing ✘ ③ 뜻이 바뀜(책을 읽기 위해 배운다) ④ in order to + -ing ✘ ⑤ for + 동사원형 ✘"),
 ('to부정사 부사적', '다음 ⓐ~ⓔ 중 어법상 옳은 문장의 개수는?',
  W('ⓐ She went to the store to buy milk.', 'ⓑ I was glad to meeting you.', 'ⓒ This box is light enough to carry.', 'ⓓ He woke up early so as to catching the bus.', 'ⓔ We were surprised to see the snow.'), CNT, 2,
  "옳은 것 ⓐⓒⓔ → 3개\nⓑ to meet ⓓ so as to catch (to 뒤 동사원형)"),
 ('to부정사 부사적', '다음 중 어법상 틀린 문장끼리 바르게 짝지은 것은?',
  W('ⓐ He ran fast to catch the bus.', 'ⓑ I was sad to leaving my friends.', 'ⓒ This tea is too hot to drink.', 'ⓓ She saved money in order to buying a car.', 'ⓔ He got up early so as not to be late.'),
  ['ⓑ, ⓓ', 'ⓐ, ⓑ', 'ⓐ, ⓒ', 'ⓒ, ⓓ', 'ⓑ, ⓓ, ⓔ'], None,
  "ⓑ to leave ⓓ in order to buy\nⓒ too ~ to …(너무 ~해서 …할 수 없다) ✓ ⓔ so as not to + 동사원형(~하지 않기 위해) ✓"),
 ('to부정사 목적', '밑줄 친 To와 같은 쓰임의 to는?', W('<u>To</u> make a better movie, I work with many people.'),
  ['I went to the park to walk my dog.', 'I was happy to see you again.', 'She wants to be a vet.', 'My dream is to travel the world.', 'I have a lot of homework to do.'], None,
  "주어진 To = 목적(~하기 위해) → ① 개를 산책시키기 위해\n② 감정의 원인 ③ want의 목적어(명사적) ④ 보어(명사적) ⑤ homework를 꾸밈(형용사적)"),
 ('before 배열', '주어진 우리말과 의미가 같도록 단어들을 배열할 때 다섯 번째로 나오는 단어는? (단, 부사절은 주절 뒤에 올 것)', W('Tom은 학교에 가기 전에 아침을 먹었다.', '[ went / before / Tom / breakfast / ate / school / to / he ]'),
  ['he', 'before', 'went', 'breakfast', 'school'], None,
  "Tom ate breakfast before he went to school. → Tom(1) ate(2) breakfast(3) before(4) he(5)"),
 ('to부정사 부사적', '다음 문장 (A)~(E)에 대해 올바른 설명을 한 사람을 모두 고른 것은?',
  W('(A) He went to the library to borrow books.', '(B) She was sad to lose her dog.', '(C) This question is hard to answer.', '(D) She grew up to be a famous singer.', '(E) I left early not to be late.',
    "수빈: (A)의 to borrow는 목적을 나타내. in order to borrow로 바꿔 써도 돼.", '다현: (B)의 to lose는 감정의 원인을 나타내는 to부정사야.', "유진: (C)의 to answer는 명사 this question을 꾸며 주고 있어.",
    '지훈: (D)의 to be는 결과를 나타내는 to부정사야.', "민재: (E)의 not to be는 to not be로 고쳐야 올바른 부정형이야."),
  ['수빈, 다현, 지훈', '수빈', '수빈, 유진', '다현, 유진', '수빈, 지훈, 민재'], None,
  "올바른 설명 수빈·다현·지훈\n유진 ✘ to answer는 형용사 hard를 꾸밈(~하기에 어려운) 민재 ✘ to부정사의 부정은 not to + 동사원형"),
 ('when', '주어진 두 문장을 접속사를 사용하여 한 문장으로 바꿀 때 가장 적절한 것은?', W('· I came home.', '· At that time, my brother was sleeping.'),
  ['My brother was sleeping when I came home.', 'My brother was sleeping so I came home.', 'My brother was sleeping because I came home.', 'My brother was sleeping after I came home.', 'My brother was sleeping than I came home.'], None,
  "그때(At that time) = 내가 집에 왔을 때 → when\n오답 ▶ ② 그래서 ③ ~ 때문에 ④ ~한 후에 ⑤ than은 비교"),
 ('after 영작', '주어진 우리말과 의미가 같도록 알맞게 영작한 문장의 개수는?', W('그는 숙제를 끝낸 후에 TV를 봤다.',
    'ⓐ He watched TV after he finished his homework.', 'ⓑ After he finished his homework, he watched TV.', 'ⓒ He watched TV after finishing his homework.', 'ⓓ He watched TV before he finished his homework.', 'ⓔ He watched TV because he finished his homework.'), CNT, 2,
  "알맞은 것 ⓐⓑⓒ → 3개 (after + 주어 + 동사 / after + -ing)\nⓓ 순서가 반대 ⓔ 이유(~ 때문에)"),
 ('시간 부사절', '다음 중 어법상 옳은 문장끼리 짝지어진 것은?',
  W('ⓐ I will call you when I will get home.', 'ⓑ After eating lunch, we played soccer.', 'ⓒ She was cooking when arrived her dad.', 'ⓓ We wash our hands before we eat.', 'ⓔ When he will come tomorrow, I will tell him.'),
  ['ⓑ, ⓓ', 'ⓐ, ⓒ', 'ⓐ, ⓔ', 'ⓑ, ⓒ', 'ⓓ, ⓔ'], None,
  "ⓑ After + -ing ✓ ⓓ before + 주어 + 동사 ✓\nⓐⓔ 시간 부사절은 미래라도 현재시제 → when I get / When he comes ⓒ 주어 + 동사 순서 → when her dad arrived"),
 ('when의 쓰임', '밑줄 친 부분의 쓰임이 나머지와 다른 하나는? (when)', '',
  ['When did you get up this morning?', 'When I was young, I lived in Busan.', 'I was happy when I got the gift.', 'Call me when you are free.', 'When it snows, we make a snowman.'], None,
  "①의 When = 언제(의문사) / 나머지 = ~할 때(접속사)"),
 ('when', "다음 중 빈칸에 'when'이 들어갈 수 있는 문장은?", '',
  ['I was taking a shower _____ the phone rang.', 'She is taller _____ her sister.', 'I went to the store _____ buy some milk.', 'We stayed home _____ of the rain.', 'He has lived here _____ 2010.'], None,
  "① 전화가 울렸을 때 → when\n② than ③ to ④ because of ⑤ since"),
 ('시간 부사절', '주어진 우리말과 의미가 같도록 빈칸에 들어갈 말이 바르게 짝지어진 것은?',
  W('· 우리는 숙제를 끝낸 후에 영화를 볼 것이다.', '= __(A)__ we __(B)__ our homework, we will watch a movie.', '· 길을 건널 때는 조심하세요.', '= __(C)__ you cross the street, be careful.'),
  ['After – finish – When', 'Before – finished – When', 'After – will finish – When', 'When – finish – Before', 'After – will finish – Because'], None,
  "(A) ~한 후에 After (B) 시간 부사절은 미래도 현재시제 finish (C) ~할 때 When"),
 ('before · after', '<보기>에서 같은 내용을 말한 사람끼리 짝지은 것은?'.replace('<보기>', '&lt;보기&gt;'),
  W('A: I read a book after I eat dinner.', 'B: I eat dinner when my dad comes home.', 'C: I eat dinner before I read a book.', 'D: I read a book when I am bored.', 'E: I always read a book before I eat dinner.'),
  ['A, C', 'A, B', 'B, C', 'B, D', 'C, E'], None,
  "A = 저녁 먹고 → 책 / C = 책 읽기 전에 저녁 = 저녁 먹고 → 책 → 같은 내용\nE는 책 → 저녁(반대)"),
 ('to부정사 목적', '주어진 문장의 밑줄 친 부분과 쓰임이 같은 것을 포함한 문장의 개수는?', W('She went to Italy <u>to learn</u> cooking.',
    '1) I was glad to see you.', '2) This river is dangerous to swim in.', '3) He studies hard to become a doctor.', '4) I went to the bank to get some money.', '5) She was surprised to hear the news.'), CNT, 1,
  "주어진 to learn = 목적. 같은 것 3)·4) → 2개\n1)·5) 감정의 원인 2) 형용사 dangerous를 꾸밈"),
 ('영작', '다음 중 주어진 우리말을 <u>잘못</u> 영작한 것은?', '',
  ['영화가 끝난 뒤에 우리는 집에 갔다. / We went home before the movie ended.', '나는 책을 사러 서점에 갔다. / I went to the bookstore to buy a book.', '그녀는 사진을 찍으러 공원에 갔다. / She went to the park to take pictures.',
   '나는 피곤할 때 일찍 잔다. / I go to bed early when I am tired.', 'Jake는 아침을 먹기 전에 샤워를 했다. / Jake took a shower before he ate breakfast.'], None,
  "끝난 '뒤에' → after the movie ended (before ✘)"),
 ('when', '빈칸에 들어갈 말로 어법상 가장 적절한 것은?', W('I met my old friend __________ I was walking in the park.'),
  ['when', 'during', 'than', 'to meet', 'for meet'], None,
  "뒤에 주어 + 동사(I was walking) → 접속사 when(~할 때)\n② during + 명사 ③ 비교 ④⑤ 접속사가 아님"),
 ('종합', '다음 중 어법상 옳지 <u>않은</u> 문장의 개수는?',
  W('(1) Before he will eat, he washes his hands.', '(2) I was happy to get your letter.', '(3) He went out to buying some bread.', '(4) I will call you when I have time.', '(5) This book is easy to read.', '(6) After you finish dinner, wash the dishes.', '(7) When she will arrive, I will tell you.'), CNT, 2,
  "틀린 것 (1)(3)(7) → 3개\n(1) Before he eats (3) to buy (7) When she arrives"),
 ('after', '다음 두 문장과 의미가 같은 것은?', W('I finished my homework. Then I went to bed.'),
  ['After I finished my homework, I went to bed.', 'Before I finished my homework, I went to bed.', 'I went to bed when I started my homework.', 'I finished my homework after I went to bed.', 'I went to bed, so I finished my homework.'], None,
  "숙제를 끝냄 → 그다음 잠 = 숙제를 끝낸 후에 잤다"),
 ('to부정사 목적 배열', '주어진 우리말과 일치하도록 <보기>의 단어들을 모두 사용하여 배열할 때, 세 번째에 오는 표현은? (단, <보기>의 문장부호에 유의할 것)'.replace('<보기>', '&lt;보기&gt;'),
  W('&lt;보기&gt; soccer / plays / after school / Jun / to stay healthy,', '(건강을 유지하기 위해, Jun은 방과 후에 축구를 한다.)'),
  ['plays', 'Jun', 'soccer', 'after school', 'to stay healthy'], None,
  "To stay healthy, Jun plays soccer after school. → To stay healthy,(1) Jun(2) plays(3)"),
 ('시간 부사절', '&lt;보기&gt;의 문장을 어법상 올바르게 고친 것은?', W('&lt;보기&gt; She takes a walk when she will feel tired.'),
  ['She takes a walk when she feels tired.', 'She takes a walk when feel tired.', 'To feels tired, she takes a walk.', 'She takes a walk when tired feel.', 'She will takes a walk when she feels tired.'], None,
  "시간 부사절은 현재시제 → when she feels tired\n⑤ will + 동사원형 take ✘"),
 ('after의 쓰임', '&lt;보기&gt;의 밑줄 친 부분과 쓰임이 같은 것은?', W('&lt;보기&gt; I brush my teeth <u>after</u> I eat lunch.'),
  ['She went home after she finished work.', 'I went out to buy milk.', 'She wants to be a nurse.', 'I like reading books during vacation.', 'He is busy because he has a test.'], None,
  "<보기> after = ~한 후에(시간의 접속사, 뒤에 주어 + 동사) → ①"),
 ('before', '다음 빈칸에 공통으로 들어갈 말로 가장 적절한 것은?', W('· Wash your hands _____ you eat.', "· Let's go home _____ it gets dark.", '· _____ I go to bed, I read a book.'),
  ['before', 'so', 'until', 'after', 'because'], None,
  "먹기 전에 / 어두워지기 전에 / 자기 전에 → before\n④ after는 셋째 문장(잠든 후에 책을 읽는다)에 어울리지 않음"),
 ('to부정사 목적', '다음 글의 빈칸에 공통으로 들어갈 말로 가장 적절한 것은?',
  W("I'm Sora, a makeup artist. _____ make the actors look like their characters, I use special makeup.", "I'm Ben, a sound engineer. I use many microphones _____ record clear sounds."),
  ['to / To', 'in / In', 'for / For', 'be / Be', 'in order / In order'], None,
  "목적(~하기 위해) → to + 동사원형\n⑤ in order는 뒤에 to가 있어야 함(in order to)"),
 ('after의 쓰임', '다음 글의 밑줄 친 after와 쓰임이 <u>다른</u> 것은?', W("My name is Emma, and I'm a film editor. My work begins <u>after</u> the shooting is over."),
  ['He felt hungry after the soccer game.', 'After she finished her work, she went home.', 'I always brush my teeth after I eat breakfast.', 'After the rain stopped, the children played outside.', 'We will start after everyone arrives.'], None,
  "밑줄 after = 접속사(뒤에 주어 + 동사) / ①의 after = 전치사(뒤에 명사 the soccer game)"),
]
assert len(I) == 25
# 정답 번호 고르게: CNT·두 개 고르기는 고정, 이름 선택지는 이름 순서 그대로 정답만 옮김
fixed = {k: (x[4][1] if isinstance(x[4], tuple) else x[4]) for k, x in enumerate(I) if x[3] is CNT or x[3] is CNTM or isinstance(x[4], tuple)}
need = Counter({0: 5, 1: 5, 2: 5, 3: 5, 4: 5})
for v in fixed.values(): need[v] -= 1
pool = sum([[k] * need[k] for k in range(5)], [])
order = [2, 0, 3, 1, 4, 2, 3, 0, 1, 4, 3, 2, 4, 0, 1, 3, 2, 4, 0, 1, 3, 0, 4, 2, 1]
items = []
for n, (src_, stem, body, opts, ans, ex) in enumerate(I, 1):
    if opts is CNT or opts is CNTM: o, a = list(opts), ans
    elif isinstance(ans, tuple): o, a = list(opts), ans[1]
    elif isinstance(ans, list): o, a = list(opts), ans
    else:
        a = next(k for k in order[n - 1:] + order + list(range(5)) if k in pool); pool.remove(a)
        o = list(opts); right = o.pop(0); o.insert(a, right)
    assert len(o) == 5 and len(set(o)) == 5
    mark = ''.join('①②③④⑤'[x] for x in a) if isinstance(a, list) else '①②③④⑤'[a]
    items.append({'n': n, 'src': src_, 'stem': stem + (' (두 개 고르기)' if isinstance(a, list) else ''), 'body': body, 'opts': o, 'en': True, 'ans': a,
                  'ex': '정답 ▶ %s\n이유 ▶ %s' % (mark, ex), 'ctx': '', 'pts': 4, 'words': [], 'kos': []})
assert sum(i['pts'] for i in items) == 100
T = {'id': 'm1jb-7s', 'kind': 'exam', 'retry': 1, 'title': '족보 7과 유사문제 (보충) 25문항', 'short': '족보 7과 유사', 'school': '중산중 1학년', 'minutes': 40,
     'note': '족보 7과 문법 공략과 같은 유형을 새 문장으로 만든 보충 세트예요. 문제는 종이 시험지로 풀고, 여기엔 답만 입력해요.', 'items': items}
src = open(path, encoding='utf-8').read()
src = re.sub(r'/\* M1JB7S-TESTS.*?/\* /M1JB7S-TESTS \*/\n?', '', src, flags=re.S)
src = src.rstrip('\n') + '\n/* M1JB7S-TESTS: gen/m1jb/similar7.py 로 만듦 (손으로 고치지 말 것) */\nwindow.PKG.tests = (window.PKG.tests || []).filter(function (t) { return t.id !== "m1jb-7s"; }).concat([%s]);\n/* /M1JB7S-TESTS */\n' % json.dumps(T, ensure_ascii=False)
open(path, 'w', encoding='utf-8').write(src)
print(''.join(('[' + ''.join('①②③④⑤'[x] for x in it['ans']) + ']') if isinstance(it['ans'], list) else '①②③④⑤'[it['ans']] for it in items), Counter(str(i['ans']) for i in items))
