# 11/19 중산중1 동아(윤정미) 실전 문법 — 비교급 · 최상급 1·2·3차 (각 20문항) · 출처 표시 CS(선생님만 알아보게 제목·꼬리말에 'CS')
# 원본: 선생님 학습지 _____1.hwp(비교급 기본·심화·최상급) · _____1-1.hwp(최상급) · _____1-2.hwp(the 비교급 the 비교급) · _____2.hwp(동등 비교·배수) → work/cmp/*.txt
# 범위(중1 · 5과 문법): 비교급 만들기(규칙·불규칙) · 비교급 + than · 비교 대상(mine/yours) · 비교급 강조(much·even·far·still·a lot, very ❌ — 본문 'a little taller') · Which ~ 비교급, A or B?
#                     최상급 만들기 · the + 최상급 · in(장소·집단)/of(복수) · 표 보고 비교·최상급
# 뺀 것: as ~ as(동등 비교)·not as ~ as·as ~ as possible, 배수, the 비교급 the 비교급, 비교급 and 비교급, the 비교급 of the two, no other / nothing ~ 비교급 / than any other,
#        older/elder·farther/further·later/latter 구별, one of the + 최상급 + 복수명사(5과 본문·대화문에 없음 — 본문은 the smallest one, a little taller than me 뿐)
# 주관식(빈칸 쓰기·고쳐 쓰기·영작)은 객관식으로 바꿈. 5과 문법 변형(m1g5)과 같은 문장은 안 씀(run_m1g5.py에서 겹침 검사)
import sys; sys.path.insert(0, '/home/claude/srcrepo/wrapup')
from wu_m1to import *
H = ('실전 문법', '중1 영어 동아(윤정미) 비교급 · 최상급', '동아(윤정미) 비교급 · 최상급 CS', 'm1cp')
B = lambda *ls: BOX('<br>'.join(ls))
NUMS = ['1개', '2개', '3개', '4개', '5개']
E_, A_, M_ = '비교급', '최상급', '비교급 · 최상급'
NOTE = '범위: 비교급(-er / more ~ than, 불규칙, much · even · far 강조)과 최상급(the -est / the most, in · of). 문장 전체를 끝까지 읽고 고르세요.'
TS = 'style="border:1px solid #9aa3b5;padding:2px 4px;text-align:center"'
def TBL(head, rows):
    return ('<table style="border-collapse:collapse;margin:4px 0;font-size:11.5px"><tr>' + ''.join('<th %s>%s</th>' % (TS, h) for h in head) + '</tr>'
            + ''.join('<tr>' + ''.join('<td %s>%s</td>' % (TS, c) for c in r) + '</tr>' for r in rows) + '</table>')

# ═══════════════ 1차 (기본) ═══════════════
T = Test('1', '1차', '비교급 · 최상급', '비교급 · 최상급', NOTE, H=H)
T.flex('다음 빈칸에 들어갈 말로 알맞은 것은?', E_, B('The earth is ' + BL + ' than the sun.'),
 ['smaller', 'small', 'smallest', 'more small', 'the smallest'],
 "이유 ▶ than(~보다)이 있으므로 비교급 → small + er = smaller.\n오답 ▶ {1} 원급 {2}·{4} 최상급 {3} 1음절은 more를 쓰지 않음\n포인트 ▶ 비교급 + than = ~보다 더 …한", [])
T.flex('다음 빈칸에 들어갈 말로 알맞은 것은?', E_, B('Judy is ' + BL + ' than Mary.'),
 ['prettier', 'prettyer', 'more pretty', 'prettiest', 'pretty'],
 "이유 ▶ 자음 + y → y를 i로 바꾸고 -er → prettier.\n오답 ▶ {1} y를 i로 안 바꿈 {2} -y로 끝나는 2음절은 -er {3} 최상급 {4} 원급\n포인트 ▶ easy - easier, happy - happier, pretty - prettier", [])
T.flex('다음 빈칸에 들어갈 말로 알맞은 것은?', E_, B('This skirt is ' + BL + ' than that blouse.'),
 ['more expensive', 'expensiver', 'expensive', 'most expensive', 'the more expensive'],
 "이유 ▶ 3음절 이상(ex-pen-sive)은 more + 원급.\n오답 ▶ {1} 긴 단어에 -er ❌ {2} 원급 {3} 최상급 {4} 비교급 앞 the ❌\n포인트 ▶ beautiful · expensive · interesting → more ~", [])
T.flex('다음 빈칸에 들어갈 말로 알맞은 것은?', E_, B('He can skate ' + BL + ' than I.'),
 ['better', 'gooder', 'more good', 'well', 'best'],
 "이유 ▶ well(잘)의 비교급 = better (불규칙).\n오답 ▶ {1}·{2} good/well은 불규칙 변화 {3} 원급 {4} 최상급\n포인트 ▶ good / well - better - best", [])
T.flex('다음 중 원급과 비교급이 <u>잘못</u> 짝지어진 것은?', E_, '',
 ['hot - hoter', 'fast - faster', 'lovely - lovelier', 'nice - nicer', 'often - more often'],
 "이유 ▶ 단모음 + 단자음 → 자음을 한 번 더 쓰고 -er → hotter.\n오답 ▶ {1} -er ✔ {2} y → i + er ✔ {3} e로 끝나면 -r ✔ {4} often → more often ✔\n포인트 ▶ hot - hotter, big - bigger, thin - thinner", [])
T.flex('대화의 빈칸에 들어갈 말로 알맞은 것은?', E_, B('A: These pants are too small for me. Do you have a ' + BL + ' size?', 'B: Sure. Here you are.'),
 ['larger', 'large', 'largest', 'more large', 'the largest'],
 "이유 ▶ 작아서 → 더 큰 사이즈 → large + r = larger.\n오답 ▶ {1} 원급(더 큰 뜻이 없음) {2}·{4} 최상급 {3} 1음절은 -er\n포인트 ▶ e로 끝나면 -r만: large - larger, nice - nicer", [])
T.flex('다음 우리말을 영어로 바르게 옮긴 것은?', E_, B('건강이 돈보다 더 중요하다.'),
 ['Health is more important than money.', 'Health is importanter than money.', 'Health is more important as money.', 'Health is most important than money.', 'Money is more important than health.'],
 "이유 ▶ important(3음절 이상) → more important + than.\n오답 ▶ {1} -er ❌ {2} than 대신 as ❌ {3} 최상급 + than ❌ {4} 뜻이 반대\n포인트 ▶ A is 비교급 than B = A가 B보다 더 ~하다", [])
T.flex('다음 표의 내용과 일치하는 것은?', E_, B(TBL(['이름', '나이', '키', '100m 기록'], [['Suji', '13', '167 cm', '15초'], ['Minji', '14', '164 cm', '12초']])),
 ['Minji is older than Suji.', 'Minji is taller than Suji.', 'Suji is faster than Minji.', 'Suji is older than Minji.', 'Minji is slower than Suji.'],
 "이유 ▶ Minji 14살 > Suji 13살 → Minji is older ✔\n오답 ▶ {1} 키는 Suji가 더 큼 {2} 기록이 짧을수록 빠름 → Minji가 더 빠름 {3} Suji가 더 어림 {4} Minji가 더 빠름\n포인트 ▶ 표의 숫자를 비교해서 형용사 고르기", [])
T.flex('다음 빈칸에 들어갈 말로 알맞지 <u>않은</u> 것은?', E_, B('My bag is bigger than ' + BL + '.'),
 ['he', 'yours', 'hers', "Mike's", "my brother's"],
 "이유 ▶ 가방과 가방을 비교 → '~의 것'(소유대명사·소유격 's)이 와야 함. he(그)는 가방과 비교할 수 없음.\n오답 ▶ {1} 너의 것 {2} 그녀의 것 {3} Mike의 것 {4} 내 동생의 것 → 모두 ✔\n포인트 ▶ 비교하는 대상끼리 같아야 한다 (my bag ↔ yours)", [])
T.flex('다음 중 어법상 <u>틀린</u> 것은?', E_, '',
 ['His cell phone is good than mine.', 'This flower is prettier than that one.', 'His backpack is bigger than mine.', 'She is taller than her mom.', 'Today is colder than yesterday.'],
 "이유 ▶ than 앞에는 비교급 → good이 아니라 better.\n오답 ▶ {1} prettier ✔ {2} bigger ✔ {3} taller ✔ {4} colder ✔\n포인트 ▶ than이 보이면 비교급인지 확인!", [])
T.flex('다음 빈칸에 들어갈 말로 알맞은 것은?', A_, B('Snow White was the ' + BL + ' beautiful girl in the world.'),
 ['most', 'more', 'much', 'very', 'best'],
 "이유 ▶ the ~ in the world(세상에서 가장) → 최상급. beautiful은 most + 원급.\n오답 ▶ {1} 비교급(than이 없음) {2}·{3} 최상급이 아님 {4} best는 good의 최상급\n포인트 ▶ the most + 긴 형용사 = 가장 ~한", [])
T.flex('다음 빈칸에 들어갈 말로 알맞은 것은?', A_, B('Today is the ' + BL + ' day of the year.'),
 ['hottest', 'hotest', 'hoter', 'most hot', 'hotter'],
 "이유 ▶ the ~ of the year → 최상급. 단모음 + 단자음 → hot + t + est.\n오답 ▶ {1} t를 한 번 더 써야 함 {2}·{4} 비교급 {3} 1음절은 most ❌\n포인트 ▶ hot - hotter - hottest", [])
T.flex('다음 우리말과 같도록 빈칸에 들어갈 말로 알맞은 것은?', A_, B('Tony는 그의 학급에서 가장 똑똑하다.', 'Tony is the ' + BL + ' his class.'),
 ['cleverest in', 'cleverer than', 'cleverest', 'cleverest with', 'cleverest to'],
 "이유 ▶ 가장 똑똑한 → cleverest, '학급에서'(집단) → in.\n오답 ▶ {1} 비교급 {2} 전치사가 없으면 his class가 이어지지 않음 {3}·{4} 범위는 in / of\n포인트 ▶ the 최상급 + in + 장소·집단", [])
T.flex('다음 빈칸에 들어갈 말이 바르게 짝지어진 것은?', A_, B('• Mt. Baekdu is the highest mountain ' + BL + ' Korea.', '• Bill is the tallest ' + BL + ' all the students.'),
 ['in – of', 'in – in', 'of – in', 'to – to', 'to – of'],
 "이유 ▶ Korea(장소) → in, all the students(복수 대상) → of.\n오답 ▶ {1}·{2} all the students 앞은 of {3}·{4} to는 최상급 범위에 쓰지 않음\n포인트 ▶ in + 장소·집단(단수) / of + 비교 대상(복수)", [])
T.flex('다음 빈칸에 들어갈 말로 알맞은 것은?', A_, B('He was ' + BL + ' actor in his country.'),
 ['the most famous', 'more famous', 'most famous', 'famousest', 'the famousest'],
 "이유 ▶ 나라에서 가장 유명한 → the most famous (famous는 most + 원급).\n오답 ▶ {1} 비교급 {2} the가 빠짐(actor 앞에 관사 필요) {3}·{4} famous는 -est ❌\n포인트 ▶ 최상급 앞에는 the", [])
T.flex('다음은 John의 가족에 관한 표이다. 표의 내용과 일치하지 <u>않는</u> 것은?', A_, B(TBL(['', '나이', '키', '몸무게'], [['Mr. White', '43', '170 cm', '65 kg'], ['Mrs. White', '40', '160 cm', '52 kg'], ['John', '14', '172 cm', '60 kg'], ['Ann', '12', '150 cm', '40 kg']])),
 ['Mrs. White is the oldest in the family.', 'There are four people in the family.', 'John is the tallest in the family.', 'Ann is the youngest in the family.', 'Mr. White is the heaviest in the family.'],
 "이유 ▶ 가장 나이가 많은 사람은 Mr. White(43). Mrs. White는 40.\n오답 ▶ {1} 4명 ✔ {2} 172 cm 최고 ✔ {3} 12살 최저 ✔ {4} 65 kg 최고 ✔\n포인트 ▶ 표에서 가장 큰 숫자 = the -est", [])
T.flex('다음 글의 빈칸에 들어갈 말로 알맞은 것은?', A_, B('Mina is 15 years old. Sumi is 14 years old. Homin is 13 years old. So Mina is the ' + BL + ' of the three.'),
 ['oldest', 'older', 'old', 'most old', 'olds'],
 "이유 ▶ 셋 중에서 가장 나이 많은 → the oldest of the three.\n오답 ▶ {1} 비교급 {2} 원급 {3} 1음절은 -est {4} 없는 말\n포인트 ▶ the 최상급 + of + 복수(the three)", [])
T.flex('다음 중 원급과 최상급이 <u>잘못</u> 짝지어진 것은?', A_, '',
 ['bad - baddest', 'good - best', 'big - biggest', 'easy - easiest', 'useful - most useful'],
 "이유 ▶ bad는 불규칙 → bad - worse - worst.\n오답 ▶ {1} 불규칙 ✔ {2} 자음 반복 ✔ {3} y → i + est ✔ {4} most + 원급 ✔\n포인트 ▶ bad / ill - worse - worst", [])
T.flex('대화의 빈칸에 들어갈 말이 순서대로 바르게 짝지어진 것은?', M_, B("A: I'd like this shirt, but it is too " + BL + ' for me. Do you have a larger size?', "B: I'm sorry. It is the " + BL + ' one in this shop.'),
 ['small – largest', 'big – little', 'large – smallest', 'smaller – large', 'little – bigger'],
 "이유 ▶ 더 큰 사이즈를 찾으니 → too small(너무 작은), 미안하지만 → 이게 가게에서 가장 큰 것 → the largest.\n오답 ▶ {1} 크면 더 큰 걸 찾지 않음 {2}·{4} 뜻이 반대 {3} too 뒤는 원급\n포인트 ▶ the + 최상급 + one(것) + in the shop", [])
T.flex('다음 빈칸에 들어갈 말로 알맞지 <u>않은</u> 것은?', E_, B('Light travels ' + BL + ' faster than sound.'),
 ['very', 'far', 'even', 'still', 'much'],
 "이유 ▶ 비교급(faster)을 '훨씬'으로 강조할 때 very는 쓸 수 없다.\n오답 ▶ {1}·{2}·{3}·{4} far · even · still · much + 비교급 = 훨씬 더 ✔\n포인트 ▶ very + 원급 / much · even · far · still · a lot + 비교급", [])
T.render()

# ═══════════════ 2차 (중상) ═══════════════
T = Test('2', '2차', '비교급 · 최상급', '비교급 · 최상급', NOTE, H=H); T.rot0 = 3
T.flex('다음 빈칸에 들어갈 말로 알맞은 것은?', E_, B('This bag is ' + BL + ' more expensive than that one.'),
 ['much', 'very', 'many', 'most', 'so'],
 "이유 ▶ 비교급(more expensive)을 '훨씬' 강조 → much.\n오답 ▶ {1} very는 비교급 강조 ❌ {2} many는 셀 수 있는 명사 앞 {3} 최상급 {4} so는 비교급 강조 ❌\n포인트 ▶ much more expensive = 훨씬 더 비싼", [])
T.flex('다음 문장을 어법에 맞게 고친 것은?', E_, B('Soccer is popular than baseball.'),
 ['Soccer is more popular than baseball.', 'Soccer is popularer than baseball.', 'Soccer is most popular than baseball.', 'Soccer is the popular than baseball.', 'Soccer is very popular than baseball.'],
 "이유 ▶ than이 있으니 비교급 → popular(3음절) → more popular.\n오답 ▶ {1} 긴 단어에 -er ❌ {2} 최상급 + than ❌ {3} the + 원급 ❌ {4} very는 비교급이 아님\n포인트 ▶ popular · famous · important → more ~ than", [])
T.flex('다음 문장을 어법에 맞게 고친 것은?', E_, B('My room is bigger than you.'),
 ['My room is bigger than yours.', 'My room is bigger than your.', 'My room is big than yours.', 'My room is biggest than you.', 'My room is more big than yours.'],
 "이유 ▶ 내 방 ↔ 너의 방 → yours(너의 것).\n오답 ▶ {1} your 뒤에 명사가 없음 {2} than 앞은 비교급 {3} 최상급 + than ❌ {4} 1음절은 -er (big → bigger)\n포인트 ▶ 비교 대상 맞추기: my room ↔ yours", [])
T.flex('대화의 빈칸에 들어갈 말로 알맞은 것은?', E_, B('A: Which do you like ' + BL + ', tea or coffee?', 'B: I like tea better.'),
 ['better', 'best', 'well', 'more good', 'gooder'],
 "이유 ▶ 둘 중(tea or coffee) 어느 것을 더 좋아하니? → Which ~ better, A or B?\n오답 ▶ {1} 최상급(셋 이상) {2} 원급 {3}·{4} 불규칙 변화 ❌\n포인트 ▶ Which do you like better, A or B? → I like A better.", [])
FOOD = TBL(['', 'Protein', 'Carbohydrate', 'Fat', 'Calories'], [['Bread', '7.3', '40', '2.4', '200'], ['Pizza', '15.0', '37', '10.0', '280'], ['Rice', '6.0', '52', '0.4', '225'], ['Ice Cream', '4.0', '21', '10.0', '190']])
T.flex('[5~6] 다음 식품 영양 분석표를 보고 물음에 답하시오. 빈칸에 들어갈 말로 알맞은 것은?', E_, B(FOOD, 'Pizza has ' + BL + ' than bread.'),
 ['more protein', 'more carbohydrate', 'less fat', 'less calories', 'more salt'],
 "이유 ▶ 단백질: Pizza 15.0 > Bread 7.3 → more protein.\n오답 ▶ {1} 탄수화물은 Bread가 더 많음(40 > 37) {2} 지방은 Pizza가 더 많음 {3} 칼로리도 Pizza가 더 많음 {4} 표에 소금은 없음\n포인트 ▶ many / much - more, little - less (양 비교)", [])
T.flex('위 표(5번)를 보고 빈칸에 들어갈 말로 알맞은 것을 고르시오.', E_, B('Rice has ' + BL + ' than ice cream.'),
 ['less fat', 'less protein', 'less carbohydrate', 'less calories', 'more fat'],
 "이유 ▶ 지방: Rice 0.4 < Ice Cream 10.0 → less fat(지방이 더 적다).\n오답 ▶ {1} 단백질은 Rice가 더 많음(6.0 > 4.0) {2} 탄수화물 Rice가 더 많음 {3} 칼로리 Rice가 더 많음(225 > 190) {4} 지방은 더 적음\n포인트 ▶ little - less - least (양이 더 적은)", [])
T.flex('다음 중 어법상 <u>옳은</u> 것은?', A_, '',
 ['English is the easiest subject for me.', 'I am the thinest among us.', 'He is the tallest in three students.', 'This is the baddest movie in my life.', 'He is the our youngest in my family.'],
 "이유 ▶ easy → easiest (y → i + est) ✔\n오답 ▶ {1} thin → thinnest {2} three students(복수) 앞은 of {3} bad → worst {4} the와 our를 같이 쓸 수 없음\n포인트 ▶ the와 소유격은 둘 중 하나만", [])
T.flex('다음 중 어법상 <u>틀린</u> 것은?', A_, '',
 ['Singing is the most easiest thing.', 'Which city is the biggest in the world?', 'Writing is the hardest thing for me.', 'Jane has the longest hair in the class.', 'Fishing is the most pleasant activity.'],
 "이유 ▶ most와 -est를 같이 쓰지 않는다 → the easiest.\n오답 ▶ {1} biggest ✔ {2} hardest ✔ {3} longest ✔ {4} the most pleasant ✔\n포인트 ▶ 최상급은 -est 또는 most 중 하나만", [])
T.flex('다음 빈칸에 들어갈 말로 알맞지 <u>않은</u> 것은?', A_, B('What is the most ' + BL + ' part of the movie?'),
 ['sad', 'boring', 'exciting', 'difficult', 'wonderful'],
 "이유 ▶ sad는 1음절 → the saddest. most를 쓰지 않는다.\n오답 ▶ {1}·{2}·{3}·{4} 긴 형용사 → the most ~ ✔\n포인트 ▶ 짧은 말 -est / 긴 말 most", [])
T.flex('다음 빈칸에 들어갈 말로 알맞은 것은?', A_, B('She is ' + BL + ' student in her class.'),
 ['the most interesting', 'interest', 'more interest', 'most interest', 'the most interest'],
 "이유 ▶ 반에서 가장 흥미로운 학생 → the most interesting + 명사.\n오답 ▶ {1}·{2}·{3}·{4} interest(관심)는 명사·동사 → 형용사 interesting이어야 함\n포인트 ▶ the most + 형용사 + 명사", [])
T.flex('다음 빈칸에 들어갈 말로 알맞은 것은?', A_, B('I have ' + BL + ' dog in the world!'),
 ['the best', 'best', 'the better', 'a better', 'best of'],
 "이유 ▶ 세상에서 가장 좋은 개 → the best dog.\n오답 ▶ {1} the가 빠짐 {2}·{3} 비교급(than이 없음) {4} of가 들어갈 자리가 아님\n포인트 ▶ good - better - best", [])
MP3 = TBL(['Model', 'A', 'B', 'C', 'D'], [['Weight', '370 g', '320 g', '290 g', '280 g'], ['Price', '$125', '$275', '$500', '$310']])
T.flex('다음 MP3 플레이어 표의 내용과 일치하는 것은?', A_, B(MP3),
 ['MP3 player A is the cheapest.', 'MP3 player A is the lightest.', 'MP3 player C is the heaviest.', 'MP3 player B is the most heaviest.', 'MP3 player C is the most cheap.'],
 "이유 ▶ 가격이 가장 싼 것은 A($125) ✔\n오답 ▶ {1} 가장 가벼운 것은 D {2} 가장 무거운 것은 A {3} most + -est ❌, 가장 무거운 것도 아님 {4} cheap → cheapest, C는 가장 비쌈\n포인트 ▶ 표에서 가장 작은 숫자·가장 큰 숫자 찾기", [])
PUP = TBL(['', 'Hari', 'Duri', 'Seri'], [['height(cm)', '57', '50', '55'], ['weight(kg)', '14', '14', '10']])
T.table('표의 내용과 일치하도록 (A), (B)에 들어갈 말을 바르게 짝지은 것은?', A_, B(PUP, 'These are my puppies. Hari is the <b>(A)</b> ________. Duri is the <b>(B)</b> ________ of the three, but he weighs 14 kg.'),
 ['(A)', '(B)'], [['tallest', 'shortest'], ['shortest', 'tallest'], ['tallest', 'lightest'], ['lightest', 'shortest'], ['taller', 'shorter']],
 "이유 ▶ (A) Hari 57 cm 최고 → tallest (B) Duri 50 cm 최저 → shortest (but 14 kg으로 무겁다)\n오답 ▶ 가장 가벼운 것은 Seri / of the three는 최상급과 함께\n포인트 ▶ the 최상급 + of the three", [])
T.flex('다음 빈칸에 들어갈 말로 알맞은 것은?', A_, B('This is the longest bridge ' + BL + ' this country.'),
 ['in', 'with', 'for', 'by', 'to'],
 "이유 ▶ 이 나라에서(장소) 가장 긴 → in this country.\n오답 ▶ {1}·{2}·{3}·{4} 최상급의 범위를 나타내지 않음\n포인트 ▶ the 최상급 + in + 장소", [])
T.flex('다음 중 원급 – 비교급 – 최상급이 바르게 연결된 것은?', M_, '',
 ['well - better - best', 'funny - funnyer - funnyest', 'thin - thiner - thinest', 'little - more little - most little', 'quick - more quick - most quick'],
 "이유 ▶ well은 불규칙 → better - best ✔\n오답 ▶ {1} funnier - funniest {2} thinner - thinnest {3} little - less - least {4} quicker - quickest\n포인트 ▶ 불규칙: good/well, bad, many/much, little", [])
T.flex('다음 우리말과 같도록 빈칸에 들어갈 말로 알맞은 것은?', A_, B('Andy는 우리 반에서 가장 힘이 세다.', 'Andy is ' + BL + ' my class.'),
 ['the strongest in', 'the strongest of', 'stronger in', 'strongest of', 'the most strong in'],
 "이유 ▶ 가장 힘센 → the strongest, 우리 반(집단) → in.\n오답 ▶ {1}·{3} my class(단수 집단) 앞은 in {2} 비교급 {4} 1음절은 -est\n포인트 ▶ in + my class / of + all the students", [])
T.flex('다음 우리말과 같도록 빈칸에 들어갈 말로 알맞은 것은?', A_, B('이것이 내 가방들 중 가장 비싼 것이다.', 'This is ' + BL + ' of my bags.'),
 ['the most expensive one', 'the expensivest one', 'more expensive one', 'most expensive one', 'the more expensive one'],
 "이유 ▶ 가장 비싼 것 → the most expensive one, 내 가방들(복수) → of my bags.\n오답 ▶ {1} 긴 단어에 -est ❌ {2}·{4} 비교급 {3} the가 빠짐\n포인트 ▶ the most + 형용사 + one(것)", [])
T.flex('다음 우리말과 같도록 빈칸에 들어갈 말로 알맞은 것은?', A_, B('그것은 내 인생에서 최악의 선택이었다.', 'It was ' + BL + ' choice in my life.'),
 ['the worst', 'the baddest', 'the worse', 'worst', 'the most bad'],
 "이유 ▶ 최악의(가장 나쁜) → bad의 최상급 the worst.\n오답 ▶ {1}·{4} bad는 불규칙 {2} 비교급 {3} the가 빠짐\n포인트 ▶ bad - worse - worst", [])
T.flex('다음 질문과 대답 중 어법상 <u>틀린</u> 것은?', A_, '',
 ['Who has largest hands in your family?', 'My brother has the largest hands.', 'My cell phone is the most expensive thing in my bag.', 'Miran is the best dancer in our class.', 'My friend John is the funniest person in our club.'],
 "이유 ▶ 최상급 앞에 the가 빠짐 → the largest hands.\n오답 ▶ {1} the largest ✔ {2} the most expensive ✔ {3} the best + in ✔ {4} funny → funniest ✔\n포인트 ▶ 형용사의 최상급 앞에는 the", [])
T.flex('다음 빈칸에 들어갈 말로 알맞은 것은?', A_, B('The morning is the ' + BL + ' part of the day.'),
 ['best', 'goodest', 'better', 'most good', 'well'],
 "이유 ▶ 하루 중 가장 좋은 때 → good의 최상급 best.\n오답 ▶ {1}·{3} good은 불규칙 {2} 비교급 {4} 부사 원급\n포인트 ▶ the best part of the day", [])
T.render()

# ═══════════════ 3차 (상) ═══════════════
T = Test('3', '3차', '비교급 · 최상급', '비교급 · 최상급', NOTE, H=H)
T.fixed('다음 <보기>에서 어법상 <u>어색한</u> 문장의 개수는?', A_, B(
 '(a) Today is the hotest day of the year.', '(b) It is the smallest picture in this museum.', '(c) You are the most happy person I know.', '(d) Watching TV is the funniest activity for me.', '(e) Studying is my the most important activity.'),
 NUMS, 3,
 "이유 ▶ 어색한 것 (a)·(c)·(e) 3개.\n오답 ▶ (a) hottest (c) the happiest (e) my와 the 중 하나만 / (b) smallest ✔ (d) funniest ✔\n포인트 ▶ 자음 반복 · y → i · the와 소유격은 함께 안 씀", [])
HY = TBL(['', 'height', 'weight'], [['Heejin', '160 cm', '52 kg'], ['Yunji', '162 cm', '55 kg']])
T.flex('다음 표의 내용과 일치하는 것은?', E_, B(HY),
 ['Yunji is heavier than Heejin.', 'Heejin is taller than Yunji.', 'Heejin is heavier than Yunji.', 'Yunji is shorter than Heejin.', 'Yunji is lighter than Heejin.'],
 "이유 ▶ Yunji 55 kg > Heejin 52 kg → heavier ✔ (heavy → y → i + er)\n오답 ▶ {1} Yunji가 더 큼 {2} Yunji가 더 무거움 {3} Yunji가 더 큼 {4} Yunji가 더 무거움\n포인트 ▶ heavy - heavier, light - lighter", [])
T.flex('다음 중 어법상 <u>틀린</u> 것은?', E_, '',
 ['My mom is very taller than my father.', 'This bag is much bigger than mine.', 'She is even prettier than her sister.', 'He runs far faster than me.', 'Watching movies is a lot more interesting than listening to music.'],
 "이유 ▶ very는 비교급을 강조하지 못한다 → much / even / far taller.\n오답 ▶ {1} much ✔ {2} even ✔ {3} far ✔ {4} a lot ✔\n포인트 ▶ 비교급 강조 = much · even · far · still · a lot (훨씬)", [])
T.flex('다음 빈칸에 들어갈 말로 알맞은 것은?', E_, B('Your computer is better than ' + BL + '.'),
 ['mine', 'I', 'her', 'she', 'me'],
 "이유 ▶ 너의 컴퓨터 ↔ 나의 컴퓨터 → mine(나의 것).\n오답 ▶ {1}·{4} 사람과 컴퓨터를 비교 ❌ {2} her 뒤에 명사 없음 {3} 사람(그녀)\n포인트 ▶ 비교 대상: your computer ↔ mine", [])
T.flex('다음 빈칸에 공통으로 들어갈 말로 알맞은 것은?', E_, B('• Health is ' + BL + ' important than money.', '• She knows ' + BL + ' than you.'),
 ['more', 'much', 'most', 'very', 'many'],
 "이유 ▶ more important(비교급) / much(많이)의 비교급 more → knows more than you.\n오답 ▶ {1} much는 원급 {2} 최상급 {3} 비교급이 아님 {4} 원급\n포인트 ▶ many / much - more - most", [])
T.flex('다음 문장의 밑줄 친 부분을 바르게 고친 것은?', E_, B('Old wines are <u>more good</u> than new ones.'),
 ['better', 'gooder', 'best', 'more well', 'much good'],
 "이유 ▶ good의 비교급은 better (불규칙).\n오답 ▶ {1} -er ❌ {2} 최상급 {3} well도 불규칙 {4} much + 원급 ❌\n포인트 ▶ good - better - best", [])
T.flex('다음 우리말을 영어로 바르게 옮긴 것은?', A_, B('그녀는 세 명의 소녀들 중 가장 키가 크다.'),
 ['She is the tallest of the three girls.', 'She is the tallest in the three girls.', 'She is taller of the three girls.', 'She is the most tall of the three girls.', 'She is tallest the three girls.'],
 "이유 ▶ 가장 키가 큰 → the tallest, 세 소녀들(복수 대상) → of.\n오답 ▶ {1} 복수 대상 앞은 of {2} 비교급 {3} 1음절은 -est {4} the와 of가 빠짐\n포인트 ▶ of + the three girls", [])
T.flex('다음 우리말을 영어로 바르게 옮긴 것은?', A_, B('James는 이 회사에서 제일 바쁜 사람이다.'),
 ['James is the busiest person in this company.', 'James is the busyest person in this company.', 'James is the most busy person in this company.', 'James is busier person in this company.', 'James is the busiest person than this company.'],
 "이유 ▶ busy → y → i + est = the busiest, 회사(집단) → in.\n오답 ▶ {1} y를 i로 {2} 2음절 -y는 -est {3} 비교급 + the 없음 {4} than은 비교급과 함께\n포인트 ▶ busy - busier - busiest", [])
T.flex('대화의 빈칸에 들어갈 말로 알맞은 것은?', A_, B("A: You look so happy. What's up?", 'B: I got a 99 on my English test.', 'A: Did anyone do better than you in your class?', 'B: Of course not. ' + BL + '.'),
 ['I am the best in my class', 'Someone is the best in my class', 'I am worse than my classmates', 'Everyone is better than me', 'I am the worst in my class'],
 "이유 ▶ 나보다 잘한 사람이 없다 → 내가 반에서 최고다.\n오답 ▶ {1} 다른 누군가가 최고 {2} 친구들보다 못함 {3} 모두가 나보다 잘함 {4} 반에서 꼴찌\n포인트 ▶ Of course not.(물론 아니야) 다음에 이어질 말 = the best", [])
T.flex('다음 식품 영양 분석표를 바르게 나타낸 것은?', A_, B(FOOD),
 ['Pizza has the most protein.', 'Rice has the most fat.', 'Ice Cream has the most calories.', 'Bread has the least carbohydrate.', 'Rice has the most calories.'],
 "이유 ▶ 단백질: Pizza 15.0 최고 → the most protein ✔\n오답 ▶ {1} 지방은 Rice가 가장 적음 {2} 칼로리 최고는 Pizza {3} 탄수화물 최저는 Ice Cream {4} Pizza가 칼로리 최고\n포인트 ▶ much - more - most / little - less - least", [])
T.flex('다음 빈칸에 들어갈 말로 알맞은 것은?', A_, B('There were many cakes in the bakery, but the man bought the ' + BL + ' one.'),
 ['smallest', 'smaller', 'small', 'most small', 'smallests'],
 "이유 ▶ 많은 케이크 중에서 가장 작은 것 → the smallest one. (5과 본문: he just wanted the smallest one)\n오답 ▶ {1} 비교급(than이 없음) {2} 원급 {3} 1음절은 -est {4} 없는 말\n포인트 ▶ the + 최상급 + one(것)", [])
T.flex('다음 중 원급 – 비교급 – 최상급이 모두 바르게 연결된 것은?', M_, '',
 ['many - more - most', 'bad - worse - worsest', 'little - littler - littlest', 'busy - busyer - busyest', 'famous - famouser - famousest'],
 "이유 ▶ many는 불규칙 → more - most ✔\n오답 ▶ {1} worst {2} less - least {3} busier - busiest {4} more famous - most famous\n포인트 ▶ 불규칙 4형제: good/well, bad, many/much, little", [])
T.fixed('다음 <보기>에서 어법상 <u>옳은</u> 문장의 개수는?', M_, B(
 '(a) This is the longest river in the world.', '(b) He likes skiing the most in winter.', '(c) Seoul is the bigger city in Korea.', '(d) This movie is more exciting than that one.', '(e) My brother is more tall than me.'),
 NUMS, 3,
 "이유 ▶ 옳은 것 (a)·(b)·(d) 3개.\n오답 ▶ (c) the biggest city (e) taller than / (b) like ~ the most(가장 좋아하다) ✔\n포인트 ▶ 범위 in Korea가 있으면 최상급", [])
T.flex('대화의 빈칸에 들어갈 말이 순서대로 바르게 짝지어진 것은?', E_, B('A: Which is ' + BL + ', the sun or the moon?', 'B: The sun is ' + BL + ' than the moon.'),
 ['bigger – much bigger', 'biggest – bigger', 'bigger – more big', 'big – biggest', 'the biggest – very bigger'],
 "이유 ▶ 둘 중 어느 것이 더 큰가 → bigger / 훨씬 더 크다 → much bigger.\n오답 ▶ {1} 둘 비교는 비교급 {2} more big ❌ {3} 원급·최상급 + than ❌ {4} very + 비교급 ❌\n포인트 ▶ Which is 비교급, A or B?", [])
T.flex('다음 글의 내용과 일치하지 <u>않는</u> 것은?', M_, B('Tom is 150 cm tall. Jack is 145 cm tall. Mike is 160 cm tall.'),
 ['Jack is the tallest of the three.', 'Mike is taller than Tom.', 'Tom is taller than Jack.', 'Jack is shorter than Mike.', 'Mike is the tallest of the three.'],
 "이유 ▶ 셋 중 가장 작은 사람이 Jack(145 cm) → the shortest.\n오답 ▶ {1} 160 > 150 ✔ {2} 150 > 145 ✔ {3} 145 < 160 ✔ {4} 160 최고 ✔\n포인트 ▶ 비교급은 둘, 최상급은 셋 이상", [])
T.flex('다음 우리말을 영어로 바르게 옮긴 것은?', A_, B('이 세상에서 제일 큰 도시는 어디니?'),
 ['Where is the biggest city in the world?', 'Where is the bigest city in the world?', 'Where is the most big city in the world?', 'Where is bigger city in the world?', 'Where the biggest city is in the world?'],
 "이유 ▶ big → g를 한 번 더 + est = the biggest, 세상에서 → in the world.\n오답 ▶ {1} 자음 반복 {2} 1음절 -est {3} 비교급 + the 없음 {4} 의문문 어순 ❌\n포인트 ▶ big - bigger - biggest", [])
T.flex('다음 빈칸에 들어갈 말로 알맞지 <u>않은</u> 것은?', E_, B("I'm about 170 cm tall, and he was " + BL + ' taller than me.'),
 ['very', 'a little', 'much', 'a lot', 'even'],
 "이유 ▶ 비교급 taller 앞에 very는 쓸 수 없다. (5과 본문: a little taller than me)\n오답 ▶ {1} 조금 더 ✔ {2}·{3}·{4} 훨씬 더 ✔\n포인트 ▶ a little + 비교급 = 조금 더 / much · a lot · even + 비교급 = 훨씬 더", [])
T.flex('다음 우리말을 영어로 바르게 옮긴 것은?', E_, B('내게는 수영보다 스키 타는 것이 더 쉽다.'),
 ['Skiing is easier than swimming for me.', 'Skiing is easyer than swimming for me.', 'Skiing is more easy than swimming for me.', 'Swimming is easier than skiing for me.', 'Skiing is easiest than swimming for me.'],
 "이유 ▶ easy → easier, 스키 타는 것이 수영보다 → Skiing is easier than swimming.\n오답 ▶ {1} y를 i로 {2} -y 2음절은 -er {3} 뜻이 반대 {4} 최상급 + than ❌\n포인트 ▶ 동명사 주어 비교: Skiing is easier than swimming.", [])
T.flex('다음 중 어법상 <u>틀린</u> 것은?', A_, '',
 ['He is the most fastest runner in our school.', 'She gets up earliest in her family.', 'He is my best friend.', 'Time is the most important thing.', 'Mina is the tallest of them.'],
 "이유 ▶ most와 -est를 같이 쓰지 않는다 → the fastest.\n오답 ▶ {1} 부사의 최상급은 the 없이도 ✔ {2} 소유격 + 최상급(the ❌) ✔ {3} the most important ✔ {4} of them ✔\n포인트 ▶ 소유격 + best (my best friend)", [])
T.fixed('다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 <u>틀린</u> 것은?', M_, B(
 'My family has three dogs. Max is ⓐ <u>the oldest</u> of the three. Coco is ⓑ <u>smaller</u> than Max, but she runs ⓒ <u>faster</u> than him. Bori is ⓓ <u>the youngest</u> in my family. She is ⓔ <u>the most cute</u> dog in the world.'),
 ['ⓐ', 'ⓑ', 'ⓒ', 'ⓓ', 'ⓔ'], 5,
 "이유 ▶ cute(1음절, e로 끝남) → the cutest.\n오답 ▶ ⓐ of the three ✔ ⓑ·ⓒ + than ✔ ⓓ in my family ✔\n포인트 ▶ e로 끝나면 -st: cute - cutest, large - largest", [])
T.render()
