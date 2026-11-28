# 11/28 중산중1 족보 6과(문법 공략 01: to부정사 명사적·명사절 that) 유사문제 1세트 (보충) 25문항 → /* M1JB6S-TESTS */ m1jb-6s
# 족보 1~25번 유형을 번호별로 따라 새 문장. 종이 시험지 + 앱 OMR, kind exam + retry 1
import json, re
from collections import Counter
path = '/home/claude/proj/data/m1-donga-yoon-L6.js'
W = lambda *ps: '<div class="wbox">' + ''.join('<p>%s</p>' % p for p in ps) + '</div>'
CNT = ['1개', '2개', '3개', '4개', '5개']
CNTM = ['1명', '2명', '3명', '4명', '5명']
I = [
 ('to부정사 명사적', '다음 대화의 빈칸 (가), (나)에 들어갈 말을 가장 바르게 짝지은 것은?',
  W('G: I want ___(가)___ the zero-waste challenge.', 'B: Great! Then you should ___(나)___ your own cup.', 'G: Okay, I will.'),
  ['to join – bring', 'joining – to bring', 'to join – to bring', 'joining – bring', 'join – bringing'], None,
  "(가) want + to부정사 → to join (나) 조동사 should + 동사원형 → bring"),
 ('to부정사 명사적', '다음 중 to부정사의 역할이 나머지 넷과 <u>다른</u> 것은?', '',
  ['My plan is to read ten books.', 'I want to be a teacher.', 'She hopes to visit Jeju.', 'We decided to recycle more.', 'They agreed to help us.'], None,
  "①은 be동사 뒤 보어(~하는 것이다) / 나머지는 동사의 목적어(~하기를, ~하는 것을)"),
 ('명사절 that', '다음은 명사절 접속사 that에 대해 정리한 내용이다. ⓐ~ⓔ 중 <u>잘못</u> 이해한 것은?',
  W('ⓐ 명사절 접속사 that 뒤에는 주어 + 동사가 있는 완전한 문장이 온다.', 'ⓑ that절은 문장에서 주어, 목적어, 보어 역할을 할 수 있다.', 'ⓒ think, know, believe 같은 동사 뒤에서 목적어로 자주 쓰인다.',
    'ⓓ 목적어 역할을 하는 that절의 that은 생략할 수 있다.', 'ⓔ 문장 맨 앞에서 주어 역할을 하는 that절의 that도 항상 생략할 수 있다.'),
  ['ⓐ', 'ⓑ', 'ⓒ', 'ⓓ', 'ⓔ'], ('fix', 4),
  "주어 역할을 하는 that절의 that은 생략할 수 없음 (That he is honest is true. → that 생략 ✘)"),
 ('종합', '다음 중 어법상 옳지 <u>않은</u> 문장의 개수는?',
  W('(a) Ride a bike is good exercise.', '(b) To learn a new language takes time.', '(c) I think that she is honest.', '(d) He knows that his sister kind.',
    '(e) The problem is that we have no time.', '(f) To keep a diary are helpful.', '(g) She enjoys to swim in the sea.'), CNT, 3,
  "틀린 것 (a)(d)(f)(g) → 4개\n(a) 주어 자리 → To ride a bike (d) that절에 동사 없음 → his sister is kind (f) to부정사 주어는 단수 → is (g) enjoy + 동명사 → swimming"),
 ('본문 어법', '다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 옳은 것은?',
  W('Every day, we produce lots of waste, and the Earth ⓐ<u>are getting</u> sicker and sicker. Do you want ⓑ<u>saving</u> the Earth? Then, ⓒ<u>join</u> the zero-waste challenge, and share your stories.',
    '<b>Olivia</b>: ⓓ<u>There was</u> lots of leftovers, but we brought them home.', '<b>Emma</b>: I heard that plastic never ⓔ<u>go</u> away completely.'),
  ['ⓐ', 'ⓑ', 'ⓒ', 'ⓓ', 'ⓔ'], ('fix', 2),
  "ⓒ 명령문(참여하세요) → 동사원형 join ✓\n틀린 것 ▶ ⓐ the Earth(단수) → is ⓑ want + to부정사 → to save ⓓ leftovers(복수) → There were ⓔ plastic(단수) → goes"),
 ('to부정사 명사적', '다음 우리말을 알맞게 영작한 것은?', W('나의 목표는 매일 책을 읽는 것이다.'),
  ['My goal is to read books every day.', 'My goal is read books every day.', 'My goal to read books every day.', 'My goal is to reading books every day.', 'My goal is read to books every day.'], None,
  "be동사 뒤 보어 '~하는 것' → is + to + 동사원형\n오답 ▶ ② to 빠짐 ③ 동사 is 빠짐 ④ to + -ing ✘ ⑤ 어순 ✘"),
 ('to부정사 명사적', '다음 중 어법상 맞는 문장은?', '',
  ['We decided to recycle plastic.', 'She wants buy a new bag.', 'I enjoy to watch movies.', 'He hopes win the game.', 'They plan to going camping.'], None,
  "decide + to부정사 ✓\n오답 ▶ ② wants to buy ③ enjoy watching ④ hopes to win ⑤ plan to go"),
 ('that의 쓰임', '다음 중 that의 쓰임이 밑줄 친 Ⓐ와 같은 것은?', W("I'm not very good at sewing, and I don't think Ⓐ<u>that</u> the bag looks perfect."),
  ['I know that he is busy.', 'Look at that dog.', 'That is my bike.', "The movie wasn't that bad.", 'Who is that girl?'], None,
  "Ⓐ = think의 목적어절을 이끄는 접속사(~라는 것) → ① know that + 주어 + 동사\n② ⑤ 저(지시형용사) ③ 저것(지시대명사) ④ 그렇게(부사)"),
 ('본문 · 설명 개수', '다음 글을 바르게 설명한 것의 개수는?',
  W('<b>Domingo</b>: My dog tore my bag. I wanted ⓐ<u>to buy</u> a new one, but I thought again. I learned ⓑ<u>that</u> reusing is important for zero-waste living. So, I decided ⓒ<u>to fix</u> it and reuse it. I\'m not very good ⓓ_____ sewing, and I don\'t think ⓔ<u>that</u> the bag looks perfect.',
    '㉠ ⓐ와 ⓒ는 둘 다 동사의 목적어 역할을 하는 to부정사이다.', '㉡ ⓑ의 that은 생략할 수 있다.', '㉢ ⓓ에 들어갈 말은 at이다.', "㉣ ⓔ의 that은 '저'라는 뜻의 지시형용사이다.", '㉤ a new one의 one은 bag을 가리킨다.'), CNT, 3,
  "바른 설명 ㉠㉡㉢㉤ → 4개\n㉣ ⓔ는 think의 목적어절을 이끄는 접속사 that\n㉢ be good at ~ = ~을 잘하다"),
 ('to · that 생략', '다음 중 to 또는 that을 생략할 수 <u>없는</u> 것을 모두 고르면?', '',
  ['I think that you are right.', 'She wants to learn Chinese.', 'We know that the shop opens at 9.', 'He decided to stay home.', 'I hope that you feel better.'], [1, 3],
  "to부정사의 to는 생략할 수 없음 → ② ④\n①③⑤ 목적어절을 이끄는 접속사 that은 생략할 수 있음"),
 ('배열', '&lt;보기&gt;의 단어를 괄호 안의 우리말과 일치하도록 알맞게 배열한 것은?', W('&lt;보기&gt; to / decided / recycle / they / bottles / the', '(그들은 그 병들을 재활용하기로 결심했다.)'),
  ['They decided to recycle the bottles.', 'They to decided recycle the bottles.', 'Decided they to recycle the bottles.', 'They decided the bottles to recycle.', 'To recycle they decided the bottles.'], None,
  "주어 They + 동사 decided + 목적어 to recycle the bottles"),
 ('종합', '다음 중 어법상 옳은 문장의 개수는?',
  W('(1) My hope is to visit Paris.', '(2) I finished cleaning my room.', '(3) He wants to play baseball.', '(4) To exercise every day are good.', '(5) She decided going abroad.', '(6) He hope to see you again.'), CNT, 2,
  "옳은 것 (1)(2)(3) → 3개\n(4) to부정사 주어는 단수 → is (5) decide + to부정사 → to go (6) He → hopes"),
 ('to부정사 명사적', '괄호 안의 우리말과 일치하도록 빈칸에 들어갈 가장 알맞은 것은?', W('His plan is __________ a new bike.', '(그의 계획은 새 자전거를 사는 것이다.)'),
  ['to buy', 'buy', 'bought', 'buys', 'to buying'], None,
  "be동사 뒤 보어 '~하는 것' → to + 동사원형 to buy"),
 ('배열', '다음 우리말과 일치하도록 괄호 안의 단어를 배열할 때, 4번째에 오는 단어는?', W('남은 음식이 많이 있었다. (leftovers / there / of / lots / were)'),
  ['of', 'were', 'lots', 'leftovers', 'there'], None,
  "There were lots of leftovers. → There(1) were(2) lots(3) of(4)"),
 ('본문 어법', '다음 글의 밑줄 친 ㉠~㉤ 중 어법상 옳지 <u>않은</u> 것은?',
  W('<b>Olivia</b>: My birthday ㉠<u>was</u> last Saturday, and my family and I ㉡<u>ate</u> out. There were lots of leftovers, but we ㉢<u>brought</u> them home. The next day, I ㉣<u>make</u> a nice lunch out of them. FYI, you can ㉤<u>find</u> great cooking ideas for leftovers on the Internet.'),
  ['㉠', '㉡', '㉢', '㉣', '㉤'], ('fix', 3),
  "㉣ The next day(지난 일) → 과거 made\n㉤ can + 동사원형 find ✓"),
 ('종합 · 설명', '주어진 문장에 대해 <u>잘못</u> 설명한 학생은 모두 몇 명인가?',
  W('(A) I want to become a doctor.', '(B) To protect animals is important.', '(C) She plan to visit her uncle.', '(D) He promised to helps me.', '(E) My job is to teach children.',
    "Jack: (A)는 틀린 문장이야. want to become이 아니라 want becoming이 맞아.", 'Anna: (B)는 옳은 문장이야. to부정사가 주어일 때는 단수 취급하니까 is가 맞아.', 'Sarah: (C)는 틀린 문장이야. 주어가 She니까 plans로 고쳐야 해.',
    'Andrew: (D)는 틀린 문장이야. to 뒤에는 동사원형이 와야 하니까 to help로 고쳐야 해.', 'William: (E)는 틀린 문장이야. to teach가 아니라 teaching만 쓸 수 있어.'), CNTM, 1,
  "잘못 설명 Jack·William → 2명\n(A) want + to부정사가 맞는 문장 (E) be동사 뒤 to부정사 보어도 맞는 문장"),
 ('to부정사 명사적', '다음 문장의 빈칸 (A)~(C)에 들어갈 말이 어법상 바르게 짝지어진 것은?',
  W('- I decided __(A)__ my old clothes.', '- Please __(B)__ your own bag.', '- My dream is __(C)__ the Earth.'),
  ['to reuse – bring – to save', 'reuse – bring – to save', 'to reuse – to bring – save', 'reusing – to bring – saving', 'to reuse – bringing – to save'], None,
  "(A) decide + to부정사 (B) Please + 명령문(동사원형) (C) be동사 뒤 보어 to부정사"),
 ('역할 구별', '다음 &lt;보기&gt;의 밑줄 친 부분이 같은 역할을 하는 것끼리 바르게 연결한 것은?',
  W('&lt;보기&gt;', 'A. She wants <u>to travel</u>.', 'B. His job is <u>to drive a bus</u>.', 'C. <u>To swim in the sea</u> is fun.', 'D. I think <u>that he is kind</u>.', 'E. <u>That she won the prize</u> is surprising.', 'F. The truth is <u>that I was wrong</u>.'),
  ['A–D / B–F / C–E', 'A–D / B–E / C–F', 'A–E / B–D / C–F', 'A–E / B–F / C–D', 'A–F / B–D / C–E'], None,
  "목적어 A·D / 보어(be동사 뒤) B·F / 주어(문장 맨 앞) C·E"),
 ('본문 · 설명', '다음 글의 ⓐ~ⓓ에 대해 올바르게 설명한 사람끼리 짝지어진 것은?',
  W("<b>Emma</b>: I often use food delivery services, but today I ⓐ<u>didn't</u>. Instead, I walked to my favorite restaurant ⓑ<u>with</u> a reusable container. I heard ⓒ<u>that</u> plastic never goes away completely. I didn't use ⓓ<u>any</u> single-use plastic today.",
    '제니: ⓐ didn\'t 뒤에는 use food delivery services가 생략되어 있어.', "지수: ⓑ with는 '~을 가지고'라는 뜻이야.", "리사: ⓒ that은 '저것'이라는 뜻의 지시대명사야.", '로제: ⓓ any는 부정문이니까 some으로 바꿔야 해.'),
  ['제니 – 지수', '제니 – 리사', '지수 – 로제', '리사 – 로제', '제니 – 로제'], None,
  "제니 ✓ 지수 ✓\n리사 ✘ ⓒ는 heard의 목적어절을 이끄는 접속사 that 로제 ✘ 부정문에서는 any가 맞음"),
 ('명사절 that 영작', '&lt;조건&gt;에 맞추어 다음 우리말과 같은 영어 문장을 만들 때, 3번째 단어와 6번째 단어를 바르게 연결한 것은?',
  W('나는 그가 정직하다고 생각해.', '&lt;조건&gt; - 명사절 접속사 that을 포함할 것. - 총 6단어로 쓸 것.'),
  ['that – honest', 'he – honest', 'that – is', 'think – he', 'he – is'], None,
  "I think that he is honest. → I(1) think(2) that(3) he(4) is(5) honest(6)"),
 ('본문 · 설명', '다음 글의 밑줄 친 (a)~(e)에 대한 설명으로 적절하지 <u>않은</u> 것은?',
  W('<b>Minsu</b>: Yesterday, I took (a)<u>some</u> plastic and glass bottles to a recycling machine near my house. I put (b)<u>them</u> into the machine one by one, and I got some points (c)<u>in return</u>. What can I do with (d)<u>those</u> points? Well, I can use them (e)<u>like</u> money.'),
  ["(a) some은 '약간의, 몇몇의'라는 뜻이다.", '(b) them은 plastic and glass bottles를 가리킨다.', "(c) in return은 '그 대가로'라는 뜻이다.", "(d) those는 that으로 바꿔야 한다.", "(e) like는 '~처럼'이라는 뜻의 전치사이다."], ('fix', 3),
  "points가 복수 명사 → those가 맞음 (that ✘)"),
 ('that의 쓰임', '다음 밑줄 친 ⓐ~ⓔ를 쓰임에 따라 알맞게 분류한 것은?',
  W('- I think ⓐ<u>that</u> recycling is important.', '- ⓑ<u>That</u> bag is mine.', '- She knows ⓒ<u>that</u> he is sick.', '- ⓓ<u>That</u> is a good idea.', '- We heard ⓔ<u>that</u> the store closed.'),
  ['ⓐ, ⓒ, ⓔ … ⓑ, ⓓ', 'ⓐ, ⓑ, ⓒ … ⓓ, ⓔ', 'ⓐ, ⓑ, ⓓ … ⓒ, ⓔ', 'ⓑ, ⓒ, ⓔ … ⓐ, ⓓ', 'ⓒ, ⓓ, ⓔ … ⓐ, ⓑ'], None,
  "ⓐⓒⓔ 접속사(~라는 것, 뒤에 주어 + 동사) / ⓑ 저(지시형용사) ⓓ 저것(지시대명사)"),
 ('본문 어법', '다음 글의 빈칸 (A)~(D)에 들어갈 말이 어법상 알맞게 짝지어진 것은?',
  W('<b>Olivia</b>: My birthday (A)_____ last Saturday, and my family and I ate out. There (B)_____ lots of leftovers, but we brought them home. The next day, I made a (C)_____ lunch out of them. FYI, you can (D)_____ great cooking ideas for leftovers on the Internet.'),
  ['was – were – nice – find', 'is – were – nice – find', 'was – was – nice – find', 'was – were – nicely – to find', 'is – was – nicely – to find'], None,
  "(A) last Saturday → was (B) lots of leftovers(복수) → were (C) 명사 lunch를 꾸밈 → 형용사 nice (D) can + 동사원형 find"),
 ('명사절 that', '다음 중 어법상 옳은 문장은?', '',
  ['That he was late is surprising.', 'That she is honest are true.', 'The fact are that we lost the game.', 'Her dream are to be a nurse.', 'I know that she like music.'], None,
  "that절 주어는 단수 → is ✓\n오답 ▶ ② are → is ③ The fact → is ④ Her dream → is ⑤ she → likes"),
 ('종합 · 설명', '주어진 문장에 대해 어법상 <u>올바르게</u> 설명한 학생은 모두 몇 명인가?',
  W('(A) I believe that she is kind.', '(B) Look at that bird in the tree.', '(C) I think he was busy yesterday.', '(D) He studies hard makes his parents happy.', '(E) She want to be a pilot.',
    '주원: (A)는 believe의 목적어 자리에 접속사 that이 이끄는 절이 온 옳은 문장이야.', '유나: (B)의 that은 접속사라서 뒤에 주어 + 동사가 와야 해.', '준우: (C)는 think 뒤에 접속사 that이 생략된 옳은 문장이야.',
    '하은: (D)는 동사가 두 개라서 틀린 문장이야. That he studies hard로 고쳐야 해.', '지아: (E)는 주어가 She니까 want를 wants로 고쳐야 해.'), CNTM, 3,
  "올바른 설명 주원·준우·하은·지아 → 4명\n유나 ✘ (B)의 that은 '저'라는 뜻의 지시형용사(that bird)"),
]
assert len(I) == 25
# 정답 번호 고르게: CNT·두 개 고르기는 고정, 이름 선택지는 이름 순서 그대로 정답만 옮김
fixed = {k: (x[4][1] if isinstance(x[4], tuple) else x[4]) for k, x in enumerate(I) if x[3] is CNT or x[3] is CNTM or isinstance(x[4], tuple)}
need = Counter({0: 5, 1: 5, 2: 5, 3: 5, 4: 4})
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
T = {'id': 'm1jb-6s', 'kind': 'exam', 'retry': 1, 'title': '족보 6과 유사문제 (보충) 25문항', 'short': '족보 6과 유사', 'school': '중산중 1학년', 'minutes': 40,
     'note': '족보 6과 문법 공략과 같은 유형을 새 문장으로 만든 보충 세트예요. 문제는 종이 시험지로 풀고, 여기엔 답만 입력해요.', 'items': items}
src = open(path, encoding='utf-8').read()
src = re.sub(r'/\* M1JB6S-TESTS.*?/\* /M1JB6S-TESTS \*/\n?', '', src, flags=re.S)
src = src.rstrip('\n') + '\n/* M1JB6S-TESTS: gen/m1jb/similar6.py 로 만듦 (손으로 고치지 말 것) */\nwindow.PKG.tests = (window.PKG.tests || []).filter(function (t) { return t.id !== "m1jb-6s"; }).concat([%s]);\n/* /M1JB6S-TESTS */\n' % json.dumps(T, ensure_ascii=False)
open(path, 'w', encoding='utf-8').write(src)
print(''.join(('[' + ''.join('①②③④⑤'[x] for x in it['ans']) + ']') if isinstance(it['ans'], list) else '①②③④⑤'[it['ans']] for it in items), Counter(str(i['ans']) for i in items))
