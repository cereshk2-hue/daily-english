# 11/28 중산중1 족보 5과(문법 공략 01) 유사문제 1세트 (보충용) 25문항 → m1-donga-yoon-L6 /* M1JB5S-TESTS */ m1jb-5s
# 족보 1~25번 유형을 번호별로 그대로 따라 문장만 새로 (18번 그림 → 표로 바꿈). 종이 시험지 + 앱 OMR, kind exam + retry 1
import json, re
from collections import Counter
path = '/home/claude/proj/data/m1-donga-yoon-L6.js'
W = lambda *ps: '<div class="wbox">' + ''.join('<p>%s</p>' % p for p in ps) + '</div>'
CNT = ['1개', '2개', '3개', '4개', '5개']
CARLOS = W('<b>Carlos Diaz, a janitor</b>', 'An old man with gray hair was running away, and something fell off his head. It was his wig. (A) <u>나는 그를 쫓아 달려갔지만</u>, (B) <u>그를 잡을 수 없었다</u>. He was faster than me.')
# (출처, 발문, 본문, 선택지(첫 번째가 정답; CNT면 ans 자리 / 두 개 고르기면 ans 리스트), ans, 해설)
I = [
 ('영작 · 과거', '윗글의 밑줄 친 우리말 (A)를 영어로 가장 적절하게 옮긴 것은?', CARLOS,
  ['I ran after him', 'I runned after him', 'I ran him after', 'I ran after to him', 'He ran after me'], None,
  "run after = ~을 쫓아 달려가다, run의 과거는 ran\n오답 ▶ ② runned ✘(불규칙) ③ 어순 ✘ ④ after 뒤에 to ✘ ⑤ 주어·목적어가 바뀜"),
 ('영작 · 과거', '윗글의 밑줄 친 우리말 (B)를 영어로 가장 적절하게 옮긴 것은?', CARLOS,
  ["I couldn't catch him", "I can't catch him", "I couldn't caught him", "I didn't could catch him", "I couldn't catch to him"], None,
  "~할 수 없었다 = couldn't + 동사원형\n오답 ▶ ② 현재 ✘(지난 일) ③ couldn't 뒤 과거형 ✘ ④ didn't could ✘ ⑤ catch 뒤 to ✘"),
 ('There is/are', '다음 중 어법상 옳은 문장을 있는 대로 고른 것은?',
  W('ⓐ There are two cats on the sofa.', "ⓑ There isn't much milk in the cup.", 'ⓒ Is there any students in the gym?', 'ⓓ Were there many cars on the road last night?', 'ⓔ There is three pens in my bag.'),
  ['ⓐ, ⓑ, ⓓ', 'ⓐ, ⓑ', 'ⓐ, ⓓ', 'ⓑ, ⓒ, ⓔ', 'ⓒ, ⓓ, ⓔ'], None,
  "옳은 것 ⓐⓑⓓ\nⓒ students(복수) → Are there ⓔ three pens(복수) → There are\nⓓ last night(과거) + 복수 → Were there ✓"),
 ('비교급', '다음 &lt;보기&gt;의 문장과 의미가 가장 유사한 것은?', W('&lt;보기&gt; Tom is older than Jake.'),
  ['Jake is younger than Tom.', 'Jake is older than Tom.', 'Tom is younger than Jake.', 'Tom is the oldest boy.', 'Jake is the youngest boy.'], None,
  "Tom이 Jake보다 나이가 많다 = Jake가 Tom보다 어리다\n오답 ▶ ②③ 뜻이 반대 ④⑤ 둘만 비교했으므로 최상급 ✘"),
 ('There is/are', '&lt;보기&gt; ⓐ~ⓔ의 어법상 틀린 부분을 올바르게 고친 것을 있는 대로 고른 것은?',
  W('&lt;보기&gt;', 'ⓐ There not are many trees in the park.', 'ⓑ There is two dogs in the yard.', 'ⓒ Is there any juice in the bottle yesterday?', 'ⓓ There are a lot of snow on the road.', 'ⓔ There were a lot of people at the concert last night.',
    '(가) ⓐ not are → are not', '(나) ⓑ is → are', '(다) ⓒ Is → Are', '(라) ⓓ are → is', '(마) ⓔ were → was'),
  ['(가), (나), (라)', '(가), (나)', '(나), (다)', '(다), (마)', '(가), (라), (마)'], None,
  "바르게 고친 것 (가)(나)(라)\n(다) yesterday(과거) + juice(셀 수 없음) → Was there 로 고쳐야 함 (Are ✘)\n(라) snow는 셀 수 없음 → is ✓\n(마) ⓔ는 원래 맞는 문장(people 복수 + 과거 were) → was로 고치면 ✘"),
 ('There의 쓰임', '주어진 문장의 There와 쓰임이 같은 것을 있는 대로 고른 것은?',
  W('<u>There</u> are many books in the library.', '- I will go ⓐ<u>there</u> tomorrow.', '- Is ⓑ<u>there</u> a bank near here?', '- Put the box over ⓒ<u>there</u>.', '- ⓓ<u>There</u> was a big tree in the garden.', '- How many students are ⓔ<u>there</u> in your class?'),
  ['ⓑ, ⓓ, ⓔ', 'ⓐ, ⓒ', 'ⓑ, ⓓ', 'ⓐ, ⓒ, ⓔ', 'ⓒ, ⓓ, ⓔ'], None,
  "주어진 There = '~가 있다' 구문의 There(해석하지 않음)\n같은 것 ⓑⓓⓔ / ⓐⓒ는 '거기에, 저기에'(장소 부사)"),
 ('본문 어법', '다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 <u>틀린</u> 것은?',
  W('<b>Ann Jones, a visitor</b>', 'I ⓐ<u>was looking</u> at the Monalisa, and someone ⓑ<u>threw</u> a cake at the painting. I turned around and saw an old man. He ⓒ<u>was standing</u> in front of a wheelchair. I\'m about 170 cm tall, and he was a little ⓓ<u>more tall</u> than me.',
    '<b>Diego Perez, a guard</b>', 'I went to the crime scene, and there ⓔ<u>were</u> pieces of cake all over the painting.'),
  ['ⓐ', 'ⓑ', 'ⓒ', 'ⓓ', 'ⓔ'], ('fix', 3),
  "ⓓ tall의 비교급은 taller (more tall ✘)\n옳은 것 ▶ ⓐⓒ 과거진행형 ⓑ throw의 과거 threw ⓔ pieces(복수) → were"),
 ('종합', '다음 중 어법상 옳지 <u>않은</u> 것끼리 짝지어진 것은?',
  W('(a) There are five apples in the box.', '(b) Is there a pen in your pencil case?', '(c) There is a lot of books on the shelf.', '(d) My room is more small than yours.', '(e) This is the most beautiful flower in the garden.'),
  ['(c), (d)', '(a), (b)', '(a), (e)', '(b), (d), (e)', '(c), (d), (e)'], None,
  "(c) books(복수) → There are (d) small의 비교급 → smaller\n(e) beautiful은 most를 붙인 최상급 ✓"),
 ('본문 어법', '다음 글의 빈칸 (A)~(C)에 들어갈 말이 어법상 바르게 짝지어진 것은?',
  W('<b>Carlos Diaz, a janitor</b>', 'An old man with gray hair ___(A)___ running away, and something fell off his head. It was his wig. I ran after him, but I couldn\'t catch him. He was ___(B)___ than me. In fact, the old man was not old. He was a young man ___(C)___ long brown hair.'),
  ['was – faster – with', 'were – faster – with', 'was – fastest – with', 'was – faster – in', 'were – fastest – in'], None,
  "(A) 주어 An old man(단수) → was (B) than 앞 → 비교급 faster (C) ~을 가진 → with"),
 ('비교급·최상급', '다음 ⓐ~ⓔ 중 어법상 옳은 문장의 개수는?',
  W('ⓐ She is smarter than her brother.', 'ⓑ This is the most longest river.', 'ⓒ Math is difficulter than science.', 'ⓓ Today is the best day of my life.', 'ⓔ He is the tallest boy in his class.'), CNT, 2,
  "옳은 것 ⓐⓓⓔ → 3개\nⓑ most + longest 중복 → the longest ⓒ difficult → more difficult"),
 ('비교급·최상급', '다음 중 어법상 <u>어색한</u> 문장은?', '',
  ['This is most popular song.', 'She is busier than her sister.', 'Planes are faster than trains.', 'It was the worst day of the year.', 'The Nile is the longest river in the world.'], None,
  "최상급 앞에는 the → This is the most popular song.\n② busy → busier(y → i) ④ bad - worse - worst"),
 ('that의 쓰임', '다음 글의 밑줄 친 (A)와 쓰임이 같은 것끼리 짝지어진 것은?',
  W('<b>Camila Santos</b>', 'We sold only one cake (A)<u>that</u> day, so I remember him clearly.', '- I like ⓐ<u>that</u> bag.', '- I think ⓑ<u>that</u> he is kind.', '- Look at ⓒ<u>that</u> tall building.', '- She said ⓓ<u>that</u> she was tired.', '- Who is ⓔ<u>that</u> boy over there?'),
  ['ⓐ, ⓒ, ⓔ', 'ⓐ, ⓒ', 'ⓑ, ⓓ', 'ⓑ, ⓓ, ⓔ', 'ⓒ, ⓓ'], None,
  "(A) that day = '그날' → 명사 앞 '저, 그'(지시형용사)\n같은 것 ⓐⓒⓔ / ⓑⓓ는 '~라는 것'(접속사, 뒤에 주어 + 동사)"),
 ('비교급·최상급', '다음 문장의 빈칸 (A)~(C)에 들어갈 말이 어법상 바르게 짝지어진 것은?',
  W('- Mina is __(A)__ singer in our school.', '- This box is __(B)__ than that one.', '- The movie was __(C)__ than the book.'),
  ['the best – heavier – more interesting', 'the goodest – heavier – more interesting', 'best – heavyer – more interesting', 'the best – more heavy – interestinger', 'the goodest – heavyer – most interesting'], None,
  "(A) good의 최상급 the best (B) heavy → heavier(y → i) (C) interesting → more interesting"),
 ('비교급·최상급', '다음 중 원급 – 비교급 – 최상급의 형태가 바르지 <u>않은</u> 것은?', '',
  ['easy – easyer – easyest', 'big – bigger – biggest', 'famous – more famous – most famous', 'early – earlier – earliest', 'good – better – best'], None,
  "자음 + y → y를 i로 바꾸고 -er, -est → easy – easier – easiest\n② 단모음 + 단자음 → 자음 하나 더 ⑤ 불규칙"),
 ('비교급·최상급', '다음 중 나머지 넷과 비교의 형태가 <u>다른</u> 문장은?', '',
  ['The tallest student sat in the back.', 'My sister is younger than me.', 'He swims faster than his friends.', 'This road is wider than that one.', 'Spring days are warmer than winter days.'], None,
  "①만 최상급(the tallest, 가장 키가 큰) / 나머지는 비교급 + than(~보다 더)"),
 ('배열', '주어진 해석과 일치하도록 단어를 배열하여 문장을 완성했을 때 \'네 번째\'에 오는 단어는?', W('공원에 아이들이 많이 있었다.', '(park / were / in / children / many / the / there)'),
  ['children', 'were', 'many', 'in', 'park'], None,
  "There were many children in the park. → There(1) were(2) many(3) children(4)"),
 ('There is/are', '다음 중 어법상 <u>어색한</u> 문장은?', '',
  ['Is there three chairs in the room?', 'There is a cat under the table.', 'There are not many cars on the street.', 'There are some cookies in the jar.', "Isn't there any milk in the fridge?"], None,
  "three chairs(복수) → Are there three chairs ~?\n⑤ milk(셀 수 없음) → Isn't there ✓"),
 ('There is/are', '다음은 민수의 방에 있는 것을 정리한 표이다. 표의 내용을 바르게 설명한 문장은?',
  W('• 침대 위: 인형 2개', '• 책상 위: 컴퓨터 1대', '• 책상 아래: 고양이 1마리', '• 침대 아래: 아무것도 없음'),
  ['There are two dolls on the bed.', 'There is a doll on the bed.', 'There are two computers on the desk.', 'There is a dog under the desk.', 'There is a ball under the bed.'], None,
  "인형 2개 → There are two dolls on the bed.\n오답 ▶ ② 인형은 2개 ③ 컴퓨터 1대 ④ 고양이 ⑤ 침대 아래 아무것도 없음"),
 ('There is/are', '다음 ⓐ~ⓔ 중 어법상 옳은 문장의 개수는?',
  W('ⓐ There is no milk in the cup.', 'ⓑ There was two dogs in the yard.', 'ⓒ There is some girls in the library.', "ⓓ There aren't many people in the store.", "ⓔ There isn't any juice in the bottle yesterday."), CNT, 1,
  "옳은 것 ⓐⓓ → 2개\nⓑ two dogs → were ⓒ girls → are ⓔ yesterday → wasn't"),
 ('There is/are', "다음 중 빈칸에 'is(Is)'가 들어갈 수 <u>없는</u> 문장은?", '',
  ['_____ there any eggs in the fridge?', 'There _____ a bakery near my house.', 'There _____ a TV in the living room.', '_____ there a pen on the desk?', 'There _____ a bird in the cage.'], None,
  "eggs(복수) → Are there any eggs ~? / 나머지는 단수 명사라 is(Is)"),
 ('There is/are', '다음 문장 (A), (B)에 대해 올바르지 <u>않은</u> 설명을 한 사람은?',
  W('(A) Are there any questions?', '(B) There was a lot of snow last winter.',
    '하늘: (A)는 \'~가 있다\'라는 뜻의 There is/are 구문이 의문문으로 쓰였어.', "재현: (A)에 대한 대답으로 'Yes, there are.' 또는 'No, there aren't.'를 쓸 수 있어.",
    '서준: (B)에는 last winter라는 과거 시점이 있어서 be동사의 과거형이 쓰였어.', '예린: (B)의 snow는 셀 수 없는 명사라서 were가 아니라 was를 썼어.',
    "민재: (A)에 대한 대답으로 'Yes, they are.'를 쓸 수 있어."),
  ['하늘', '재현', '서준', '예린', '민재'], ('fix', 4),
  "There is/are 의문문의 대답은 there로 → Yes, there are. / No, there aren't. (they ✘)"),
 ('so의 쓰임', '다음 글의 밑줄 친 (A)so와 쓰임이 <u>다른</u> 것은?',
  W('<b>Camila Santos</b>', 'We sold only one cake that day, (A)<u>so</u> I remember him clearly.'),
  ['She is so kind to everyone.', 'I was tired so I went to bed early.', 'It was cold so I wore a coat.', 'He missed the bus so he was late.', 'I was hungry so I ate some bread.'], None,
  "(A) so = 그래서(결과) / ①의 so = 매우, 아주(형용사 kind를 꾸밈)"),
 ('-ing의 쓰임', '다음 밑줄 친 ⓐ~ⓔ 중 나머지와 쓰임이 <u>다른</u> 것끼리 짝지어진 것은?',
  W('- Jisu was ⓐ<u>reading</u> a book.', '- I love this ⓑ<u>painting</u>.', '- They were ⓒ<u>playing</u> soccer.', '- The ⓓ<u>building</u> is very tall.', '- He was ⓔ<u>sleeping</u> on the sofa.'),
  ['ⓑ, ⓓ', 'ⓐ, ⓑ', 'ⓐ, ⓒ', 'ⓒ, ⓔ', 'ⓓ, ⓔ'], None,
  "ⓑ painting(그림), ⓓ building(건물) = 명사 / ⓐⓒⓔ = be동사 + -ing 과거진행형(~하고 있었다)"),
 ('비교 추론', '주어진 두 문장의 맥락으로 아래 문장을 추론할 때, 의미상 알맞은 것을 <b>두 개</b> 고르면?', '',
  ['Mina is 15. Jisu is 15, too. → Mina is not older than Jisu.', 'Tom is taller than Ben. Ben is taller than Sam. → Sam is the tallest of the three.',
   'My bag is 3 kg. Your bag is 5 kg. → My bag is heavier than your bag.', 'I got up at 7. My sister got up at 6. → My sister got up earlier than me.',
   'The red pen is longer than the blue pen. The black pen is longer than the blue pen. → The black pen is the longest of the three.'], [0, 3],
  "① 둘이 같은 나이 → 더 많지 않다 ✓ ④ 6시 < 7시 → 언니가 더 일찍 ✓\n오답 ▶ ② Sam이 가장 작음 ③ 내 가방이 더 가벼움 ⑤ 빨간 펜과 검은 펜 중 어느 쪽이 더 긴지 알 수 없음"),
 ('본문 어법', '다음 글의 밑줄 친 (A)~(E)에 대해 올바르지 <u>않은</u> 설명을 한 사람은?',
  W('An old man with gray hair (A)<u>was running</u> away, and something (B)<u>fell off</u> his head. I (C)<u>ran after</u> him, but I (D)<u>couldn\'t catch</u> him. He was (E)<u>faster</u> than me.',
    "민지: (A)는 '달아나고 있었다'라는 뜻의 과거진행형이야.", "다연: (B)의 fall off는 '~에서 떨어지다'라는 뜻이야.", "도준: (C)의 ran after는 '~을 쫓아 달려갔다'라는 뜻이야.",
    "경재: (D)의 couldn't는 can't의 과거형으로 '~할 수 없었다'라는 뜻이야.", "지훈: (E)의 faster는 fast의 최상급이야."),
  ['민지', '다연', '도준', '경재', '지훈'], ('fix', 4),
  "faster는 비교급(더 빠른), 최상급은 (the) fastest"),
]
assert len(I) == 25
# 정답 번호 고르게: CNT·두 개 고르기는 고정, 이름 선택지는 이름 순서 그대로 정답만 옮김
fixed = {k: (x[4][1] if isinstance(x[4], tuple) else x[4]) for k, x in enumerate(I) if x[3] is CNT or isinstance(x[4], tuple)}
need = Counter({0: 5, 1: 5, 2: 5, 3: 5, 4: 4})
for v in fixed.values(): need[v] -= 1
pool = sum([[k] * need[k] for k in range(5)], [])
order = [2, 0, 3, 1, 4, 2, 3, 0, 1, 4, 3, 2, 4, 0, 1, 3, 2, 4, 0, 1, 3, 0, 4, 2, 1]
items = []
for n, (src_, stem, body, opts, ans, ex) in enumerate(I, 1):
    if opts is CNT: o, a = list(CNT), ans
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
T = {'id': 'm1jb-5s', 'kind': 'exam', 'retry': 1, 'title': '족보 5과 유사문제 (보충) 25문항', 'short': '족보 5과 유사', 'school': '중산중 1학년', 'minutes': 40,
     'note': '족보 5과 문법 공략과 같은 유형을 새 문장으로 만든 보충 세트예요. 문제는 종이 시험지로 풀고, 여기엔 답만 입력해요.', 'items': items}
src = open(path, encoding='utf-8').read()
src = re.sub(r'/\* M1JB5S-TESTS.*?/\* /M1JB5S-TESTS \*/\n?', '', src, flags=re.S)
src = src.rstrip('\n') + '\n/* M1JB5S-TESTS: gen/m1jb/similar5.py 로 만듦 (손으로 고치지 말 것) */\nwindow.PKG.tests = (window.PKG.tests || []).filter(function (t) { return t.id !== "m1jb-5s"; }).concat([%s]);\n/* /M1JB5S-TESTS */\n' % json.dumps(T, ensure_ascii=False)
open(path, 'w', encoding='utf-8').write(src)
print(''.join(('[' + ''.join('①②③④⑤'[x] for x in it['ans']) + ']') if isinstance(it['ans'], list) else '①②③④⑤'[it['ans']] for it in items), Counter(str(i['ans']) for i in items))
