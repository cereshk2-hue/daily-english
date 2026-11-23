# 11/23 심학중1 천재(소영순) 5과 실전 문법 — 비교급 1~3차 · 최상급 1~3차 (각 20문항, 중상~상)
# 원본: 선생님 Grammar Build Up 5과(Pattern 1 비교급 · Pattern 2 최상급) hwp → work_src/m1c5/u.txt. 각 파트 뒷부분(개수·모두 고르기·표·순서 추론·배열 n번째·지문 ⓐ~ⓔ·의미 같은/다른) 유형을 바꾸고 어렵게
# 논쟁 피함: clever/simple/quiet/healthy(-er·more 둘 다), than I/me(둘 다 맞음 — 틀린 근거로 안 씀), older/elder, farther/further, Today's weather ... than yesterday, 동점(the youngest 애매) 안 만듦
import sys; sys.path.insert(0, '/home/claude/srcrepo/wrapup')
from wu_m1cg import *
H = ('실전 문법', '중1 영어 천재(소영순) 5과 비교급·최상급', '천재(소영순) 5과 비교급·최상급', 'm1cc')
B = lambda *ls: BOX('<br>'.join(ls))
NUMS = ['1개', '2개', '3개', '4개', '5개']
t = lambda x: x.replace('[', '<u>').replace(']', '</u>')
CIRS = ['ⓐ', 'ⓑ', 'ⓒ', 'ⓓ', 'ⓔ']
def TB(head, rows):
    st = 'border:1px solid #888;padding:2px 7px;text-align:center'
    h = '<table style="border-collapse:collapse;margin:4px 0;font-size:.95em"><tr>' + ''.join('<th style="%s;background:#eef2f7">%s</th>' % (st, x) for x in head) + '</tr>'
    for r in rows: h += '<tr>' + ''.join('<td style="%s">%s</td>' % (st, x) for x in r) + '</tr>'
    return BOX(h + '</table>')
F_, S_, A_, E_, T_, L_, X_ = '비교급 형태', '비교급 문장', '원급 비교', '비교급 강조', '표·그림 해석', '5과 본문', '최상급'
N1 = '범위: 비교급(-er / more, 불규칙), 비교급 + than, 비교 대상(소유대명사), 비교급 강조(much · even · far · a lot), as ~ as / not as ~ as, less + 원급. 쉬운 문제 없이 중상~상으로 냈어요.'
N2 = '범위: 최상급(-est / most, 불규칙), the + 최상급 + in/of, one of the + 최상급 + 복수 명사, 비교급 + than any other + 단수 명사, 최상급 뜻의 여러 표현, 비교급·원급 비교와 섞어서. 중상~상.'

# ═══════════════ 비교급 1차 ═══════════════
T = Test('1', '비교급 1차', '비교급 1차 — 형태와 문장', '비교급', N1, H=H); T.rot0 = 0
T.flex('다음 빈칸에 공통으로 들어갈 말로 알맞은 것은?', E_, B('• This box is ' + BL + ' heavier than that one.', '• The movie was ' + BL + ' more exciting than the book.'),
 ['much', 'very', 'more', 'so', 'too'],
 "이유 ▶ 비교급(heavier · more exciting) 앞에서 '훨씬'은 much(even · far · a lot).\n오답 ▶ {1}·{3}·{4} very · so · too는 비교급을 꾸미지 못함 {2} more heavier처럼 비교급이 겹침\n포인트 ▶ much + 비교급 = 훨씬 더 ~한", [('heavy', '무거운')])
T.flex('다음 중 원급과 비교급이 바르게 짝지어진 것끼리 모두 고른 것은?', F_, B('(a) thin − thiner', '(b) early − earlier', '(c) famous − more famous', '(d) bad − badder', '(e) little − less', '(f) dirty − dirtyer'),
 ['(b), (c), (e)', '(a), (b), (c)', '(b), (d), (f)', '(c), (e), (f)', '(a), (d), (e)'],
 "이유 ▶ (b) 자음+y → earlier (c) -ous → more famous (e) little − less(불규칙)\n틀린 것 ▶ (a) thinner(자음 겹침) (d) worse(불규칙) (f) dirtier(y → i)\n포인트 ▶ 단모음+단자음은 자음 한 번 더, 자음+y는 y → i", [('famous', '유명한'), ('dirty', '더러운')])
T.fixed('다음 &lt;보기&gt;에서 어법상 올바른 문장의 개수는?', S_, B('&lt;보기&gt;', '• Daegu is hotter than Seoul.', '• This bag is more cheaper than that one.', "• My hair is longer than my sister's.", '• He runs more fast than his friend.', '• Your idea is better than mine.', '• This puzzle is more difficult than that one.'),
 NUMS, 4,
 "이유 ▶ 옳은 것: hotter · longer than my sister's(hair) · better than mine · more difficult → 4개\n틀린 것 ▶ more cheaper → cheaper(겹침) / more fast → faster\n포인트 ▶ -er 비교급 앞에 more를 또 쓰지 않음", [('puzzle', '퍼즐')])
T.flex('다음 우리말을 영어로 바르게 옮긴 것은?', E_, B('이 노트북은 저 태블릿보다 훨씬 더 비싸다.'),
 ['This laptop is much more expensive than that tablet.', 'This laptop is very more expensive than that tablet.', 'This laptop is much expensiver than that tablet.', 'This laptop is more much expensive than that tablet.', 'This laptop is much more expensive that that tablet.'],
 "이유 ▶ expensive → more expensive, 강조 much는 비교급 바로 앞, ~보다 = than\n오답 ▶ {1} very ❌ {2} expensiver ❌ {3} 어순 more much ❌ {4} that → than\n포인트 ▶ much + more + 원급 + than", [('expensive', '비싼')])
T.flex('다음 표의 내용과 일치하지 <u>않는</u> 것은?', T_, TB(['', 'Minsu', 'Jiho', 'Yuna'], [['Age', '14', '15', '14'], ['Height', '158cm', '165cm', '160cm'], ['Weight', '50kg', '48kg', '52kg']]),
 ['Jiho is younger than Yuna.', 'Yuna is taller than Minsu.', 'Minsu is not as heavy as Yuna.', 'Minsu is as old as Yuna.', 'Jiho is lighter than Minsu.'],
 "이유 ▶ Jiho 15살, Yuna 14살 → Jiho is older than Yuna.\n오답 ▶ {1} 160 ＞ 158 {2} 50kg ＜ 52kg {3} 둘 다 14살 {4} 48kg ＜ 50kg → 모두 일치\n포인트 ▶ not as ~ as = ~만큼 ~하지 않다(더 ~하다의 반대)", [('weight', '몸무게')])
T.flex('다음 문장과 의미가 같은 것은?', A_, B('Mina is not as tall as Jisu.'),
 ['Jisu is taller than Mina.', 'Mina is taller than Jisu.', 'Jisu is shorter than Mina.', 'Mina is as tall as Jisu.', 'Jisu is not as tall as Mina.'],
 "이유 ▶ 미나는 지수만큼 크지 않다 = 지수가 미나보다 크다.\n오답 ▶ {1}·{2}·{4} 반대 뜻 {3} 둘이 같다는 뜻\n포인트 ▶ A is not as ~ as B = B is 비교급 than A", [])
T.flex('괄호 안의 단어를 알맞은 형태로 바꿀 때 바르게 짝지어진 것은?', F_, B('• My bag is ⓐ(heavy) than yours.', '• Today is ⓑ(hot) than yesterday.', '• He sings ⓒ(well) than his brother.'),
 ['heavier − hotter − better', 'heavyer − hotter − better', 'heavier − hoter − better', 'heavier − hotter − weller', 'heavier − hotter − more well'],
 "이유 ▶ heavy → heavier(y → i) / hot → hotter(자음 겹침) / well → better(불규칙)\n오답 ▶ heavyer · hoter · weller · more well ❌\n포인트 ▶ good · well → better", [])
T.fixed('다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 <u>틀린</u> 것은?', L_, B('El and Jo were ⓐ ' + U('the smallest') + ' students in the class. In the spring, Jo grew ⓑ ' + U('taller') + '. Jo was ⓒ ' + U('more tall') + ' than El, so Jo could water the plants alone. El felt ⓓ ' + U('smaller') + ' every day. On the last day of school, El took the last pot. It had ⓔ ' + U('the smallest') + ' plant.'),
 CIRS, 3,
 "이유 ▶ tall의 비교급은 taller → more tall ❌ (교과서: Jo was taller than El.)\n오답 ▶ ⓐ·ⓔ 최상급 the smallest ⓑ grew taller ⓓ felt smaller ✔\n포인트 ▶ 1음절 형용사는 -er", [('water', '물을 주다'), ('pot', '화분')])
T.flex('다음 &lt;보기&gt;를 읽고 나이가 많은 순서대로 바르게 나열한 것은?', S_, B('• Tom is older than Ken.', '• Amy is younger than Ken.', '• Lisa is younger than Amy.'),
 ['Tom − Ken − Amy − Lisa', 'Ken − Tom − Amy − Lisa', 'Tom − Amy − Ken − Lisa', 'Tom − Ken − Lisa − Amy', 'Lisa − Amy − Ken − Tom'],
 "이유 ▶ Tom ＞ Ken, Ken ＞ Amy, Amy ＞ Lisa → Tom − Ken − Amy − Lisa\n오답 ▶ 비교 방향(older / younger)을 거꾸로 읽으면 틀림\n포인트 ▶ younger than = ~보다 어린", [])
T.flex('다음 중 어법상 <u>어색한</u> 것은?', S_, '',
 ['Your phone is newer than me.', "I'm taller than my brother.", 'This river is longer than that one.', 'He got up earlier than usual.', 'My cat is lazier than your cat.'],
 "이유 ▶ 휴대폰과 '나'를 비교 ❌ → newer than mine(내 휴대폰)\n오답 ▶ {1} 사람끼리 {2} 강끼리(that one) {3} earlier than usual {4} 고양이끼리 ✔\n포인트 ▶ 비교하는 두 대상의 종류를 맞추기", [('lazy', '게으른')])
T.flex('다음 빈칸에 들어갈 말로 알맞지 <u>않은</u> 것은?', E_, B('Fruit is ' + BL + ' healthier than candy.'),
 ['very', 'much', 'even', 'far', 'a lot'],
 "이유 ▶ very는 비교급을 꾸미지 못함.\n오답 ▶ {1}·{2}·{3}·{4} 비교급 강조 ✔\n포인트 ▶ much · even · far · a lot · still + 비교급", [('healthy', '건강에 좋은')])
T.flex('다음 단어를 배열하여 문장을 만들 때 <u>4번째</u>로 오는 단어는?', S_, B('이 노래가 저것보다 더 인기 있다.', '( than / is / more / this / popular / that one / song )'),
 ['more', 'popular', 'is', 'than', 'song'],
 "완성 ▶ This(1) song(2) is(3) more(4) popular(5) than(6) that one.\n포인트 ▶ popular처럼 긴 단어는 more + 원급", [('popular', '인기 있는')])
T.flex('다음 대화의 빈칸에 들어갈 말로 알맞은 것은?', S_, B('A: Which is faster, a bike or a car?', 'B: ' + BL),
 ['A car is faster than a bike.', 'A bike is faster than a car.', 'A car is fast than a bike.', 'A car is more fast than a bike.', 'A car is faster then a bike.'],
 "이유 ▶ 자동차가 자전거보다 빠름 + faster than\n오답 ▶ {1} 사실과 반대 {2} fast → faster {3} more fast ❌ {4} then(그때) → than\n포인트 ▶ than(~보다) / then(그때, 그 다음에)", [])
T.flex('다음 중 어법상 <u>틀린</u> 것은?', A_, '',
 ['This box is as heavier as that one.', 'She is as busy as her mom.', "I can't run as fast as you.", 'My room is not so big as yours.', 'He is as kind as his father.'],
 "이유 ▶ as ~ as 사이에는 원급 → as heavy as\n오답 ▶ {1}·{2}·{4} as + 원급 + as {3} not so ~ as도 맞음\n포인트 ▶ as + 원급 + as = ~만큼 ~한", [])
T.flex('다음 중 의미가 나머지 넷과 <u>다른</u> 것은?', A_, '',
 ['B is older than A.', 'A is older than B.', 'B is younger than A.', 'B is not as old as A.', 'A is not as young as B.'],
 "이유 ▶ 나머지는 모두 'A가 B보다 나이가 많다', B is older than A만 반대.\n오답 ▶ {1} A ＞ B {2} = B ＜ A {3} B가 A만큼 나이 들지 않음 {4} A가 B만큼 어리지 않음 → 모두 A ＞ B\n포인트 ▶ not as young as = 더 나이 많다", [])
T.flex('다음 글을 읽고, Jun이 가진 책은 몇 권인지 고르면?', T_, B('I have 12 books. Mina has 3 more books than me. Jun has 5 fewer books than Mina.'),
 ['10', '12', '15', '7', '20'],
 "이유 ▶ Mina = 12 + 3 = 15, Jun = 15 − 5 = 10\n포인트 ▶ more A than ~ = ~보다 A만큼 더 / fewer = 더 적은(셀 수 있는 명사)", [('fewer', '더 적은')])
T.flex('다음 빈칸에 들어갈 말로 알맞은 것은?', S_, B('Her dress is prettier than ' + BL + '. (나의 것)'),
 ['mine', 'me', 'my', 'I', 'myself'],
 "이유 ▶ 드레스끼리 비교 → mine(= my dress)\n오답 ▶ {1}·{3}·{4} 드레스와 사람을 비교 {2} my 뒤에 명사가 필요\n포인트 ▶ 비교 대상이 '~의 것'이면 소유대명사", [('pretty', '예쁜')])
T.flex('다음 문장과 의미가 같은 것은?', A_, B('This test is less difficult than the last one.'),
 ['The last test was more difficult than this one.', 'This test is more difficult than the last one.', 'The last test was less difficult than this one.', 'This test is as difficult as the last one.', 'The last test was not as difficult as this one.'],
 "이유 ▶ less difficult = 덜 어렵다 → 지난 시험이 더 어려웠다.\n오답 ▶ {1}·{2}·{4} 반대 뜻 {3} 같다는 뜻\n포인트 ▶ less + 원급 + than = ~보다 덜 ~한", [('less', '덜')])
T.flex('다음 우리말을 영어로 바르게 옮긴 것은?', L_, B('Jo는 El보다 키가 더 컸다.'),
 ['Jo was taller than El.', 'Jo was more tall than El.', 'Jo was tall than El.', 'Jo was taller then El.', 'Jo is tallest than El.'],
 "이유 ▶ 과거 was + taller + than (교과서 문장)\n오답 ▶ {1} more tall ❌ {2} 비교급이 아님 {3} then ❌ {4} 최상급 + than ❌, 시제도 다름\n포인트 ▶ 비교급 + than", [])
T.flex('다음 중 어법상 올바른 문장을 모두 고른 것은?', E_, B('(a) He is much smarter than his cousin.', '(b) This bag is very cheaper than that one.', '(c) Soccer is more exciting than baseball.', '(d) Your shoes are bigger than my.', '(e) I can swim better than my sister.'),
 ['(a), (c), (e)', '(a), (b), (c)', '(b), (d)', '(c), (d), (e)', '(a), (e)'],
 "이유 ▶ (a) much + 비교급 (c) more exciting (e) well → better ✔\n틀린 것 ▶ (b) very → much (d) my → mine\n포인트 ▶ (a), (e)만 고르면 (c)를 빠뜨림", [('cousin', '사촌')])
T.render()

# ═══════════════ 비교급 2차 ═══════════════
T = Test('2', '비교급 2차', '비교급 2차 — 원급 비교와 강조', '비교급', N1, H=H); T.rot0 = 3
T.flex('다음 중 원급과 비교급이 모두 바르게 짝지어진 것은?', F_, '',
 ['big − bigger / pretty − prettier / bad − worse', 'thin − thinner / many − manyer / useful − more useful', 'large − larger / easy − easyer / good − better', 'fat − fatter / famous − famouser / little − less', 'wet − weter / busy − busier / much − more'],
 "이유 ▶ bigger(자음 겹침) · prettier(y → i) · worse(불규칙) 모두 ✔\n오답 ▶ {1} many → more {2} easy → easier {3} famous → more famous {4} wet → wetter\n포인트 ▶ 셋 중 하나만 틀려도 오답", [])
T.flex('(A), (B), (C)의 각 네모 안에서 어법에 맞는 표현으로 가장 적절한 것은?', E_, B('• A cheetah runs (A) [ fast / faster ] than a horse.', '• My room is (B) [ very / much ] cleaner than yours.', '• Your English is as (C) [ good / better ] as mine.'),
 ['faster − much − good', 'fast − much − good', 'faster − very − good', 'faster − much − better', 'fast − very − better'],
 "이유 ▶ (A) than 앞 → 비교급 faster (B) 비교급 강조 → much (C) as ~ as 사이 → 원급 good\n포인트 ▶ than 앞은 비교급, as ~ as 사이는 원급", [('cheetah', '치타')])
T.fixed('다음 &lt;보기&gt;에서 어법상 올바른 문장의 개수는?', S_, B('&lt;보기&gt;', '• She is wiser than her sister.', '• My score was badder than yours.', '• This road is more wide than that one.', '• He has fewer friends than his brother.', '• Today is very colder than yesterday.', '• I think math is easier than science.', '• His car is as fast as my.'),
 NUMS, 3,
 "이유 ▶ 옳은 것: wiser · fewer friends · easier → 3개\n틀린 것 ▶ badder → worse / more wide → wider / very → much / my → mine\n포인트 ▶ 불규칙 · 겹침 · 강조 · 비교 대상을 모두 확인", [('wise', '현명한'), ('wide', '넓은')])
T.flex('다음 도표를 바르게 설명한 것은?', T_, B("<b>Our Class's Favorite Bread</b>") + TB(['bread', 'bagel', 'croissant', 'muffin', 'donut'], [['students', '6', '12', '9', '3']]),
 ['Muffins are more popular than bagels.', 'Donuts are more popular than bagels.', 'Croissants are less popular than muffins.', 'Thirty-five students answered the question.', 'Bagels are as popular as muffins.'],
 "이유 ▶ 머핀 9명 ＞ 베이글 6명\n오답 ▶ {1} 3 ＜ 6 {2} 12 ＞ 9 → more popular {3} 6 + 12 + 9 + 3 = 30명 {4} 6 ≠ 9\n포인트 ▶ less popular = 덜 인기 있는", [('popular', '인기 있는')])
T.flex('다음 우리말을 영어로 바르게 옮긴 것은?', E_, B('그 영화는 내가 생각했던 것보다 훨씬 더 재미있었다.'),
 ['The movie was much more interesting than I thought.', 'The movie was very more interesting than I thought.', 'The movie was much interestinger than I thought.', 'The movie was more much interesting than I thought.', 'The movie was much more interesting then I thought.'],
 "이유 ▶ much + more interesting + than I thought\n오답 ▶ {1} very ❌ {2} interestinger ❌ {3} 어순 ❌ {4} then → than\n포인트 ▶ than I thought = 내가 생각했던 것보다", [('interesting', '재미있는')])
T.flex('다음 중 짝지어진 두 문장의 의미가 같은 것은?', A_, '',
 ['A van is smaller than a bus.<br>= A bus is not as small as a van.', "I'm as tall as my brother.<br>= My brother is taller than me.", 'Health is more important than money.<br>= Money is more important than health.', 'Swimming is not as dangerous as boxing.<br>= Swimming is more dangerous than boxing.', 'Jim is older than Sue.<br>= Sue is not as young as Jim.'],
 "이유 ▶ 밴이 버스보다 작다 = 버스는 밴만큼 작지 않다 ✔\n오답 ▶ {1} 키가 같다 ≠ 형이 더 크다 {2} 순서가 바뀌어 반대 {3} not as dangerous = 덜 위험 {4} Sue가 더 어림 → Sue is not as old as Jim\n포인트 ▶ not as ~ as는 '반대쪽이 더 ~하다'", [('dangerous', '위험한')])
T.fixed('다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 올바른 것은?', S_, B('My brother and I are twins, but we are very different. He is ⓐ ' + U('more tall') + ' than me. I am ⓑ ' + U('heavyer') + ' than him. He gets up ⓒ ' + U('earlyer') + ' than me. But I study ⓓ ' + U('harder') + ' than him. My grades are ⓔ ' + U('gooder') + ' than his.'),
 CIRS, 4,
 "이유 ▶ hard → harder ✔\n틀린 것 ▶ ⓐ taller ⓑ heavier ⓒ earlier ⓔ better\n포인트 ▶ 1음절은 -er, 자음+y는 -ier, good은 better", [('twin', '쌍둥이'), ('grade', '성적')])
T.flex('다음 &lt;보기&gt;를 읽고 무거운 순서대로 바르게 나열한 것은?', S_, B('• A is heavier than B.', '• C is lighter than B.', '• D is heavier than A.'),
 ['D − A − B − C', 'A − D − B − C', 'D − B − A − C', 'D − A − C − B', 'C − B − A − D'],
 "이유 ▶ D ＞ A, A ＞ B, B ＞ C → D − A − B − C\n포인트 ▶ lighter than = ~보다 가벼운", [('light', '가벼운')])
T.flex('다음 글을 읽고, Yuri가 가진 스티커는 몇 장인지 고르면?', T_, B('Jisu has 20 stickers. Minho has 6 fewer stickers than Jisu. Yuri has 3 more stickers than Minho.'),
 ['17', '14', '20', '23', '11'],
 "이유 ▶ Minho = 20 − 6 = 14, Yuri = 14 + 3 = 17\n포인트 ▶ fewer(더 적은) / more(더 많은)", [('sticker', '스티커')])
T.flex('다음 중 어법상 <u>틀린</u> 문장을 모두 고른 것은?', S_, B('(a) My bag is bigger than yours.', '(b) Her hair is longer than me.', "(c) This year's festival was better than last year's.", '(d) His room is cleaner than his sister.', '(e) Your idea is more creative than mine.'),
 ['(b), (d)', '(a), (b)', '(b), (c), (d)', '(d), (e)', '(a), (c), (e)'],
 "이유 ▶ (b) 머리카락 ↔ 나 → than mine (d) 방 ↔ 누나 → than his sister's\n옳은 것 ▶ (a) yours (c) last year's (festival) (e) mine\n포인트 ▶ 비교 대상의 종류를 맞추기", [('festival', '축제'), ('creative', '창의적인')])
T.flex('다음 빈칸에 들어갈 수 있는 말을 모두 고른 것은?', E_, B('Seoul is ' + BL + ' bigger than my hometown.', '', '(a) much  (b) very  (c) even  (d) far  (e) more'),
 ['(a), (c), (d)', '(a), (b), (c)', '(b), (e)', '(a), (d), (e)', '(c), (d), (e)'],
 "이유 ▶ 비교급 강조 much · even · far ✔\n틀린 것 ▶ (b) very ❌ (e) more bigger(겹침) ❌\n포인트 ▶ very는 원급, much는 비교급", [('hometown', '고향')])
T.flex('다음 단어를 배열하여 문장을 만들 때 <u>6번째</u>로 오는 단어는?', A_, B('내 남동생은 너의 여동생만큼 키가 크지 않다.', '( as / not / my / is / tall / your / brother / as / sister )'),
 ['tall', 'as', 'not', 'your', 'is'],
 "완성 ▶ My(1) brother(2) is(3) not(4) as(5) tall(6) as(7) your(8) sister(9).\n포인트 ▶ not as + 원급 + as", [])
T.flex('다음 대화의 빈칸에 들어갈 말로 알맞은 것은?', S_, B('A: Is your sister older than you?', "B: No. " + BL + " I'm two years older."),
 ['She is younger than me.', 'She is older than me.', "I'm younger than her.", 'She is as old as me.', "I'm not as old as her."],
 "이유 ▶ 내가 두 살 많음 → 언니(여동생)가 나보다 어리다.\n오답 ▶ {1}·{2}·{4} 내가 더 어리다는 뜻 {3} 나이가 같다는 뜻\n포인트 ▶ 뒤 문장 I'm two years older가 단서", [])
T.flex('다음 문장과 의미가 같은 것은?', A_, B('Juice is less sweet than soda.'),
 ['Soda is sweeter than juice.', 'Juice is sweeter than soda.', 'Soda is not as sweet as juice.', 'Juice is as sweet as soda.', 'Soda is less sweet than juice.'],
 "이유 ▶ 주스가 탄산음료보다 덜 달다 = 탄산음료가 더 달다.\n오답 ▶ {1}·{2}·{4} 반대 {3} 같다\n포인트 ▶ less + 원급 = 덜 ~한", [('sweet', '단')])
T.flex('다음 표의 내용과 일치하는 것은?', T_, TB(['', 'Ann', 'Ben', 'Cara'], [['Age', '13', '14', '13'], ['Height', '150cm', '155cm', '160cm'], ['Score', '85', '90', '80']]),
 ["Cara is taller than Ben, but her score is lower than Ann's.", 'Ann is as old as Ben.', 'Ben is shorter than Ann.', "Ann's score is higher than Ben's.", 'Cara is older than Ann.'],
 "이유 ▶ Cara 160 ＞ Ben 155, Cara 80 ＜ Ann 85 ✔\n오답 ▶ {1} 13 ≠ 14 {2} 155 ＞ 150 {3} 85 ＜ 90 {4} 둘 다 13살\n포인트 ▶ but 앞뒤를 모두 확인", [('score', '점수')])
T.flex('다음 중 어법상 <u>틀린</u> 것은?', E_, '',
 ['My room is more cleaner than yours.', 'She is much busier than before.', 'Elephants are a lot heavier than horses.', 'This question is even more difficult than that one.', 'He is far more careful than his friend.'],
 "이유 ▶ cleaner 앞에 more를 또 씀 → My room is cleaner than yours.\n오답 ▶ {1}·{2}·{3}·{4} much · a lot · even · far + 비교급 ✔\n포인트 ▶ 강조어 + more + 원급은 맞고, more + -er은 틀림", [('careful', '조심성 있는')])
T.flex('다음 글의 내용과 일치하는 것은?', L_, B('However, in the spring, something was DIFFERENT. Jo grew TALLER! Jo was taller than El, so Jo could water the plants alone. El felt smaller every day.'),
 ['El was shorter than Jo in the spring.', 'El was taller than Jo in the spring.', 'Jo was as tall as El in the spring.', 'El could water the plants alone.', 'Jo was not as tall as El in the spring.'],
 "이유 ▶ Jo was taller than El = El이 Jo보다 작았다.\n오답 ▶ {1}·{4} 반대 {2} 같다 {3} 혼자 물을 줄 수 있었던 건 Jo\n포인트 ▶ 비교급 문장을 반대 형용사로 바꿔 읽기", [])
T.flex('다음 우리말을 영어로 바르게 옮긴 것은?', A_, B('나는 너만큼 빨리 달릴 수 없다.'),
 ["I can't run as fast as you.", "I can't run as faster as you.", "I can't run fast as you.", "I can't run as fast than you.", 'I can run as fast as you.'],
 "이유 ▶ not as + 원급 + as → can't run as fast as\n오답 ▶ {1} 비교급 ❌ {2} 앞 as 빠짐 {3} than ❌ {4} 긍정(달릴 수 있다)\n포인트 ▶ as ~ as 짝 맞추기", [])
T.flex('다음 빈칸에 알맞은 말이 바르게 짝지어진 것은?', F_, B('• Jinho is a ' + BL + ' dancer than me.', '• He dances ' + BL + ' than me.'),
 ['better − better', 'gooder − weller', 'better − more well', 'good − well', 'more good − better'],
 "이유 ▶ good(형용사) · well(부사)의 비교급은 둘 다 better\n오답 ▶ gooder · weller · more well · more good ❌ / good · well은 원급\n포인트 ▶ a better dancer = dances better", [('dancer', '춤추는 사람')])
T.fixed('다음 &lt;보기&gt;에서 어법상 올바른 문장의 개수는?', E_, B('&lt;보기&gt;', '• Can you speak more slowly?', '• A plane is much faster than a train.', '• His story was very more interesting than mine.', '• This shirt is cheaper than that one.', '• Her cat is not as cute as my.', '• I feel much better today.'),
 NUMS, 4,
 "이유 ▶ 옳은 것: more slowly · much faster · cheaper · much better → 4개\n틀린 것 ▶ very → much / my → mine\n포인트 ▶ -ly 부사는 more + 원급(more slowly)", [('slowly', '천천히')])
T.render()

# ═══════════════ 비교급 3차 ═══════════════
T = Test('3', '비교급 3차', '비교급 3차 — 종합(상)', '비교급', N1, H=H); T.rot0 = 4
T.fixed('다음 중 원급과 비교급이 바르게 짝지어지지 <u>않은</u> 것의 개수는?', F_, B('(a) heavy − heavier  (b) thin − thinner  (c) famous − famouser  (d) good − gooder', '(e) wet − wetter  (f) careful − carefuler  (g) little − less'),
 NUMS, 3,
 "이유 ▶ 틀린 것: (c) more famous (d) better (f) more careful → 3개\n옳은 것 ▶ heavier · thinner · wetter · less\n포인트 ▶ -ous · -ful은 more + 원급", [('careful', '조심하는')])
T.flex('빈칸 ⓐ, ⓑ, ⓒ에 들어갈 말이 바르게 짝지어진 것은?', E_, B('• The weather was ⓐ ' + BL + ' better than I expected.', "• My sister isn't as ⓑ " + BL + ' as me. (busy)', '• This bag is ⓒ ' + BL + ' expensive than that one.'),
 ['much − busy − more', 'very − busy − more', 'much − busier − more', 'much − busy − much', 'more − busy − much'],
 "이유 ▶ ⓐ 비교급 강조 much ⓑ as ~ as 사이 원급 busy ⓒ more expensive\n포인트 ▶ 강조 much / 원급 / more를 자리마다 구별", [('expect', '예상하다')])
T.flex('다음 표의 내용과 일치하지 <u>않는</u> 것은?', T_, TB(['fruit', 'apple', 'banana', 'mango', 'kiwi'], [['price', '1,000원', '1,500원', '3,000원', '1,000원']]),
 ['A banana is less expensive than an apple.', 'A mango is more expensive than a banana.', 'A kiwi is as cheap as an apple.', 'An apple is cheaper than a mango.', 'A banana is not as expensive as a mango.'],
 "이유 ▶ 바나나 1,500원 ＞ 사과 1,000원 → 바나나가 더 비쌈\n오답 ▶ {1} 3,000 ＞ 1,500 {2} 둘 다 1,000원 {3} 1,000 ＜ 3,000 {4} 1,500 ＜ 3,000\n포인트 ▶ less expensive = 덜 비싼(더 싼)", [('price', '가격')])
T.flex('다음 두 문장의 내용을 한 문장으로 바르게 나타낸 것은?', S_, B('My bag weighs 3kg. Your bag weighs 5kg.'),
 ['My bag is lighter than yours.', 'My bag is heavier than yours.', 'Your bag is lighter than mine.', 'My bag is as heavy as yours.', 'Your bag is not as heavy as mine.'],
 "이유 ▶ 3kg ＜ 5kg → 내 가방이 더 가볍다.\n오답 ▶ {1}·{2}·{4} 반대 {3} 같다\n포인트 ▶ weigh = 무게가 ~이다", [('weigh', '무게가 ~이다')])
T.flex('다음 대화의 빈칸에 들어갈 말로 알맞은 것은?', S_, B('A: Mina is taller than Jisu, right?', 'B: Yes. And Hana is taller than Mina.', 'A: Then, ' + BL),
 ['Jisu is shorter than Hana.', 'Hana is shorter than Jisu.', 'Jisu is taller than Mina.', 'Mina is as tall as Hana.', 'Hana is not as tall as Jisu.'],
 "이유 ▶ Hana ＞ Mina ＞ Jisu → 지수는 하나보다 작다.\n오답 ▶ {1}·{2}·{4} 순서와 반대 {3} Hana가 더 큼\n포인트 ▶ 두 비교를 이어 순서 정하기", [])
T.fixed('다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 <u>틀린</u> 것의 개수는?', E_, B('Last weekend, I went hiking with my dad. The mountain was ⓐ ' + U('much higher') + ' than I thought. My dad walked ⓑ ' + U('faster') + ' than me, so I had to walk ⓒ ' + U('more quick') + '. The view from the top was ⓓ ' + U('very more beautiful') + ' than the view from the bottom. I felt ⓔ ' + U('happier') + ' than ever.'),
 NUMS, 2,
 "이유 ▶ 틀린 것: ⓒ 동사 walk를 꾸미는 부사 → more quickly ⓓ very → much → 2개\n옳은 것 ▶ ⓐ much higher ⓑ faster ⓔ happier than ever\n포인트 ▶ 동사 뒤는 부사의 비교급", [('view', '경치'), ('bottom', '아래, 밑')])
T.flex('주어진 단어를 모두 사용하되 필요하면 형태를 바꾸어 문장을 만들 때, <u>5번째</u>로 오는 단어는?', E_, B('이 문제는 저것보다 훨씬 더 쉽다.', '( much / easy / this / that one / is / question / than )'),
 ['easier', 'much', 'easy', 'more', 'than'],
 "완성 ▶ This(1) question(2) is(3) much(4) easier(5) than(6) that one.\n오답 ▶ {2} easy는 비교급으로 바꿔야 함 {3} more easy ❌\n포인트 ▶ 형태 변화 + 강조 much 위치", [('question', '문제')])
T.flex('다음 글을 읽고, Dami의 키를 고르면?', T_, B('Sumin is 150cm tall. Junho is 8cm taller than Sumin. Dami is 5cm shorter than Junho.'),
 ['153cm', '158cm', '145cm', '163cm', '148cm'],
 "이유 ▶ Junho = 150 + 8 = 158, Dami = 158 − 5 = 153\n포인트 ▶ 숫자 + 비교급 + than = ~보다 얼마만큼 더", [])
T.flex('다음 우리말을 영어로 바르게 옮긴 것은?', A_, B('이 상자는 저 상자만큼 무겁지 않다.'),
 ['This box is not as heavy as that one.', 'This box is not as heavier as that one.', 'This box is as not heavy as that one.', 'This box is not heavy as that one.', 'This box is not as heavy than that one.'],
 "이유 ▶ be동사 + not + as + 원급 + as\n오답 ▶ {1} 비교급 ❌ {2} not 위치 ❌ {3} 앞 as 빠짐 {4} than ❌\n포인트 ▶ not은 be동사 바로 뒤", [])
T.flex('다음 중 어법상 올바른 문장을 모두 고른 것은?', S_, B('(a) The river is deeper than the lake.', '(b) I want a bigger room than this.', '(c) He is more lazy than his brother.', '(d) Your plan is more practical than mine.', '(e) She danced more well than me.'),
 ['(a), (b), (d)', '(a), (c)', '(b), (c), (e)', '(a), (d), (e)', '(c), (e)'],
 "이유 ▶ (a) deeper (b) bigger (d) more practical ✔\n틀린 것 ▶ (c) lazier (e) better\n포인트 ▶ 자음+y는 -ier, well은 better", [('practical', '실용적인'), ('lazy', '게으른')])
T.flex('다음 중 빈칸에 들어갈 말이 나머지 넷과 <u>다른</u> 것은?', S_, '',
 ['We had lunch, and ' + BL + ' we went shopping.', 'She is older ' + BL + ' me.', 'This is better ' + BL + ' that.', 'I like summer more ' + BL + ' winter.', 'He runs faster ' + BL + ' his friend.'],
 "이유 ▶ '그 다음에' → then. 나머지는 비교급 뒤 than.\n오답 ▶ {1}~{4} 비교급(older · better · more · faster) + than\n포인트 ▶ than / then 철자 함정", [])
T.flex('다음 우리말을 영어로 바르게 옮긴 것은?', A_, B('축구는 야구보다 덜 인기 있다.'),
 ['Soccer is less popular than baseball.', 'Soccer is less more popular than baseball.', 'Soccer is more popular than baseball.', 'Soccer is less popularer than baseball.', 'Baseball is less popular than soccer.'],
 "이유 ▶ less + 원급 + than\n오답 ▶ {1}·{3} less 뒤는 원급 {2} 반대 뜻 {4} 주어가 바뀌어 반대\n포인트 ▶ 덜 ~한 = less + 원급", [])
T.flex('다음 표의 두 사람을 바르게 비교한 문장은?', T_, TB(['Liz', 'Ben'], [["I'm 155cm tall.", "I'm 178cm tall."], ["I'm 16 years old.", "I'm 14 years old."], ["I'm a good baker.", "I'm not a good baker."], ["I'm not very active.", "I'm very active."]]),
 ['Liz is a better baker than Ben.', 'Ben is shorter than Liz.', 'Liz is younger than Ben.', 'Liz is more active than Ben.', 'Ben is a better baker than Liz.'],
 "이유 ▶ Liz는 빵을 잘 굽고 Ben은 못 굽는다 → Liz is a better baker.\n오답 ▶ {1} Ben이 더 큼 {2} Liz가 더 나이 많음 {3} Ben이 더 활동적 {4} 반대\n포인트 ▶ a good baker → a better baker", [('baker', '제빵사'), ('active', '활동적인')])
T.flex('다음 중 짝지어진 두 문장의 의미가 같은 것을 모두 고른 것은?', A_, B('(a) A is bigger than B. = B is smaller than A.', '(b) A is as old as B. = B is older than A.', '(c) A is not as fast as B. = B is faster than A.', '(d) A is less famous than B. = B is more famous than A.', '(e) A is more careful than B. = B is more careful than A.'),
 ['(a), (c), (d)', '(a), (b)', '(b), (c), (e)', '(c), (d), (e)', '(a), (e)'],
 "이유 ▶ (a) 반대 형용사 (c) not as ~ as (d) less ↔ more 모두 같은 뜻 ✔\n틀린 것 ▶ (b) 같다 ≠ 더 많다 (e) 순서만 바꿔 반대 뜻\n포인트 ▶ 주어를 바꾸면 형용사도 반대로", [])
T.flex('다음 중 어법상 틀린 부분을 바르게 고친 것은?', S_, '',
 ['This bag is more heavier than that one. → more를 뺀다', 'She is much taller than me. → much를 very로', 'My room is cleaner than yours. → yours를 you로', 'He swims better than his brother. → better를 weller로', "I'm not as busy as you. → busy를 busier로"],
 "이유 ▶ heavier 앞 more 겹침 → 빼야 맞음 ✔\n오답 ▶ {1}·{2}·{3}·{4} 원래 맞는 문장을 틀리게 고침\n포인트 ▶ '고친 것'은 원래 문장이 틀렸는지부터", [])
T.flex('다음 글을 읽고, El이 매일 더 작게 느낀 이유로 알맞은 것은?', L_, B('In the spring, something was DIFFERENT. Jo grew TALLER! Jo was taller than El, so Jo could water the plants alone. El felt smaller every day.'),
 ['Jo became taller than El, and Jo could water the plants alone.', 'El grew taller than Jo.', 'Jo was not as tall as El.', 'El could reach the pots alone.', 'The plants were smaller than El.'],
 "이유 ▶ Jo가 El보다 커져서 혼자 물을 줄 수 있게 됨 → El은 작게 느낌\n오답 ▶ {1}·{2} 반대 {3} 혼자 닿은 건 Jo {4} 글에 없음\n포인트 ▶ so 앞이 이유", [('reach', '~에 닿다')])
T.flex('다음 &lt;보기&gt;를 읽고 키가 큰 순서대로 바르게 나타낸 것은?', A_, B('• Ann is as tall as Kate.', '• Kate is taller than Mia.', '• Mia is taller than Lucy.'),
 ['Ann = Kate ＞ Mia ＞ Lucy', 'Kate ＞ Ann ＞ Mia ＞ Lucy', 'Ann = Kate ＞ Lucy ＞ Mia', 'Mia ＞ Ann = Kate ＞ Lucy', 'Lucy ＞ Mia ＞ Ann = Kate'],
 "이유 ▶ Ann = Kate, Kate ＞ Mia, Mia ＞ Lucy\n오답 ▶ {1} as tall as = 같은 키 {2}·{3}·{4} 순서 반대\n포인트 ▶ as ~ as = 같다", [])
T.flex('다음 대화의 빈칸 (A), (B)에 들어갈 말이 바르게 짝지어진 것은?', A_, B('A: Your bag looks ____(A)____ than mine. (big)', "B: Yes, but it isn't as ____(B)____ as yours. (expensive) It's cheap."),
 ['bigger − expensive', 'big − expensive', 'bigger − more expensive', 'biger − expensive', 'more big − expensive'],
 "이유 ▶ (A) than 앞 → bigger (B) as ~ as 사이 → 원급 expensive\n오답 ▶ big · biger · more big ❌ / as more expensive as ❌\n포인트 ▶ 한 대화 안에서 비교급과 원급 비교 구별", [])
T.flex('다음 중 어법은 맞지만 문맥상 <u>어색한</u> 것은?', S_, '',
 ['An elephant is lighter than a mouse.', 'Summer is hotter than winter.', 'A turtle is slower than a rabbit.', 'The sun is bigger than the moon.', 'A train is faster than a bicycle.'],
 "이유 ▶ 코끼리가 쥐보다 가볍다 ❌ → heavier\n오답 ▶ {1}~{4} 사실에 맞음\n포인트 ▶ 비교급의 뜻(가벼운 ↔ 무거운)까지 확인", [('turtle', '거북')])
T.fixed('다음 &lt;보기&gt;에서 어법상 올바른 문장의 개수는?', S_, B('&lt;보기&gt;', '• My shoes are dirtier than yours.', '• This test was much easier than the last one.', '• She can jump higher than her brother.', '• He is more famous than his father.', '• This flower is as beautifuler as that one.', '• I have less money than you.', '• His room is more bigger than mine.'),
 NUMS, 5,
 "이유 ▶ 옳은 것: dirtier · much easier · higher · more famous · less money → 5개\n틀린 것 ▶ as beautiful as / bigger(more 겹침)\n포인트 ▶ less + 셀 수 없는 명사(money)", [('dirty', '더러운')])
T.render()

# ═══════════════ 최상급 1차 ═══════════════
T = Test('4', '최상급 1차', '최상급 1차 — 형태와 the + 최상급', '최상급', N2, H=H); T.rot0 = 1
T.flex('다음 중 원급과 최상급이 바르게 짝지어진 것끼리 모두 고른 것은?', X_, B('(a) big − biggest', '(b) happy − happyest', '(c) good − best', '(d) famous − famousest', '(e) early − earliest', '(f) little − littlest'),
 ['(a), (c), (e)', '(a), (b), (c)', '(b), (d), (f)', '(c), (d), (e)', '(a), (e), (f)'],
 "이유 ▶ biggest(자음 겹침) · best(불규칙) · earliest(y → i) ✔\n틀린 것 ▶ (b) happiest (d) most famous (f) least\n포인트 ▶ 최상급도 비교급과 같은 규칙", [])
T.flex('다음 빈칸에 들어갈 말이 바르게 짝지어진 것은?', X_, B('• He is the tallest boy ' + BL + ' his class.', '• She is the youngest ' + BL + ' the three sisters.'),
 ['in − of', 'of − in', 'in − in', 'of − of', 'at − of'],
 "이유 ▶ 장소·집단(his class) → in / 같은 무리의 수(the three sisters) → of\n포인트 ▶ the + 최상급 + in(장소·범위) / of(복수 명사·숫자)", [])
T.flex('다음 우리말을 영어로 바르게 옮긴 것은?', X_, B('그녀는 우리 학교에서 가장 인기 있는 선생님 중 한 명이다.'),
 ['She is one of the most popular teachers in our school.', 'She is one of the most popular teacher in our school.', 'She is one of the more popular teachers in our school.', 'She is one of most popular teachers in our school.', 'She is one of the popularest teachers in our school.'],
 "이유 ▶ one of the + 최상급 + 복수 명사\n오답 ▶ {1} teacher → teachers {2} 비교급 ❌ {3} the 빠짐 {4} popularest ❌\n포인트 ▶ one of 뒤는 항상 복수 명사", [])
T.flex('다음 중 어법상 <u>어색한</u> 것은?', X_, '',
 ['August is hottest month in Korea.', 'This is the most difficult problem in the book.', 'He is the best player on our team.', 'Today is the happiest day of my life.', 'It is the most popular game among teens.'],
 "이유 ▶ 명사 앞 최상급에는 the → the hottest month\n오답 ▶ {1}~{4} the + 최상급 ✔ (among = ~ 사이에서)\n포인트 ▶ the를 빠뜨리는 함정", [('among', '~ 사이에서')])
T.flex('다음 표의 내용과 일치하는 것은?', T_, TB(['', 'Minsu', 'Jiho', 'Yuna', 'Dami'], [['Age', '15', '14', '16', '13'], ['Height', '160cm', '168cm', '155cm', '162cm']]),
 ['Yuna is the oldest of the four.', 'Jiho is the youngest of the four.', 'Minsu is the tallest of the four.', 'Dami is shorter than Minsu.', 'Yuna is taller than Minsu.'],
 "이유 ▶ Yuna 16살이 가장 많음 ✔\n오답 ▶ {1} 가장 어린 사람은 Dami(13) {2} 가장 큰 사람은 Jiho(168) {3} 162 ＞ 160 {4} 155 ＜ 160\n포인트 ▶ 최상급은 모두 비교해서 하나", [])
T.flex('다음 빈칸에 들어갈 말로 알맞은 것은?', X_, B('Mt. Everest is higher than any other ' + BL + ' in the world.'),
 ['mountain', 'mountains', 'the mountain', "mountain's", 'a mountains'],
 "이유 ▶ 비교급 + than any other + 단수 명사 = 최상급 뜻\n오답 ▶ {1}·{4} 복수 ❌ {2}·{3} any other 뒤 the · 소유격 ❌\n포인트 ▶ any other + 단수", [('mountain', '산')])
T.flex('다음 문장과 의미가 같은 것은?', X_, B('Jisu is the smartest student in her class.'),
 ['Jisu is smarter than any other student in her class.', 'Jisu is smarter than any other students in her class.', 'Jisu is as smart as other students in her class.', 'Any other student is smarter than Jisu.', 'Jisu is not as smart as any other student in her class.'],
 "이유 ▶ 최상급 = 비교급 + than any other + 단수 명사\n오답 ▶ {1} students ❌ {2} 같다 {3}·{4} 반대\n포인트 ▶ 최상급 바꿔 쓰기", [('smart', '똑똑한')])
T.fixed('다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 올바른 것은?', X_, B('My town has ⓐ ' + U('the most big') + ' park in the city. It also has ⓑ ' + U('the oldest') + ' tree in the country. The tree is ⓒ ' + U('more tall') + ' than any other tree. My friends say it is ⓓ ' + U('the beautifulest') + ' place. It is ⓔ ' + U('the better') + ' place for a picnic.'),
 CIRS, 2,
 "이유 ▶ old → the oldest ✔\n틀린 것 ▶ ⓐ the biggest ⓒ taller ⓓ the most beautiful ⓔ the best\n포인트 ▶ 1음절 -est, 긴 단어 most", [('picnic', '소풍')])
T.flex('다음 &lt;보기&gt;를 읽고 키가 가장 큰 사람과 가장 작은 사람을 바르게 짝지은 것은?', X_, B('• A is taller than B.', '• C is the shortest of the four.', '• D is taller than A.'),
 ['D − C', 'A − C', 'D − B', 'B − C', 'A − B'],
 "이유 ▶ D ＞ A ＞ B, C가 가장 작음 → 가장 큰 사람 D, 가장 작은 사람 C\n포인트 ▶ 비교급과 최상급 정보를 함께 쓰기", [])
T.flex('다음 빈칸에 들어갈 말로 알맞은 것은?', X_, B('Of all the seasons, I like spring ' + BL + '.'),
 ['best', 'better', 'most good', 'gooder', 'well'],
 "이유 ▶ 모든 계절 중에서 → 최상급 best (like ~ best = ~을 가장 좋아하다)\n오답 ▶ {1} 비교급 {2}·{3} ❌ {4} 원급\n포인트 ▶ like A best", [('season', '계절')])
T.fixed('다음 &lt;보기&gt;에서 어법상 올바른 문장의 개수는?', X_, B('&lt;보기&gt;', '• She is the kindest girl in my class.', '• This is the most expensive car of all.', '• He is one of the funniest boy in school.', '• Seoul is the largest city in Korea.', '• It was the worst day of my life.', '• This is the most delicious than that.'),
 NUMS, 4,
 "이유 ▶ 옳은 것: the kindest · the most expensive · the largest · the worst → 4개\n틀린 것 ▶ boy → boys / 최상급 + than ❌ → more delicious than\n포인트 ▶ one of + 복수, 최상급 뒤 than ❌", [])
T.flex('다음 대화의 빈칸에 들어갈 말로 알맞은 것은?', X_, B('A: Who is the fastest runner in your class?', 'B: ' + BL),
 ['Minho is. He runs faster than any other student.', 'Minho is. He runs faster than any other students.', 'Minho does. He runs the most fast.', 'Minho is. He runs fastest than any other student.', 'Minho is. He is the most fastest runner.'],
 "이유 ▶ Who is ~? → Minho is. + 비교급 + than any other + 단수\n오답 ▶ {1} students ❌ {2} does ❌, most fast ❌ {3} 최상급 + than ❌ {4} most fastest(겹침) ❌\n포인트 ▶ 대답 동사와 형태를 함께 확인", [])
T.flex('다음 단어를 배열하여 문장을 만들 때 <u>5번째</u>로 오는 단어는?', X_, B('브라질은 남아메리카에서 가장 큰 나라이다.', '( the / Brazil / country / largest / is / South America / in )'),
 ['country', 'largest', 'the', 'in', 'is'],
 "완성 ▶ Brazil(1) is(2) the(3) largest(4) country(5) in(6) South America.\n포인트 ▶ the + 최상급 + 명사 + in + 범위", [('country', '나라')])
T.flex('다음 그림을 바르게 설명한 문장은?', T_, TB(['MP3 player', 'watch', 'camera'], [['$80', '$120', '$310']]),
 ['The camera is the most expensive of the three.', 'The watch is the cheapest of the three.', 'The MP3 player is more expensive than the watch.', 'The watch is more expensive than the camera.', 'The camera is cheaper than the watch.'],
 "이유 ▶ 카메라 $310가 가장 비쌈 ✔\n오답 ▶ {1} 가장 싼 건 MP3 player {2} 80 ＜ 120 {3} 120 ＜ 310 {4} 310 ＞ 120\n포인트 ▶ of the three = 셋 중에서", [])
T.flex('다음 문장과 의미가 같은 것은?', X_, B('No other student in my class is as tall as Minho.'),
 ['Minho is the tallest student in my class.', 'Minho is not the tallest student in my class.', 'Minho is as tall as other students in my class.', 'Minho is shorter than other students in my class.', 'Other students are taller than Minho.'],
 "이유 ▶ 우리 반 어떤 학생도 민호만큼 크지 않다 = 민호가 가장 크다\n오답 ▶ {1}·{3}·{4} 반대 {2} 같다\n포인트 ▶ No other ~ as + 원급 + as = 최상급", [])
T.flex('다음 글의 내용과 일치하는 것은?', L_, B("El's classmates reached for the pots over tiny El. They took all the pots with colorful flowers. El took the last pot. It had the smallest plant with no flowers."),
 ['The plant El took was smaller than the other plants.', 'El took the biggest plant.', "El's plant had the most colorful flowers.", 'El took the first pot.', 'Jo took the smallest plant.'],
 "이유 ▶ the smallest plant = 다른 어떤 식물보다 작았다 ✔\n오답 ▶ {1} 반대 {2} 꽃이 없었음 {3} 마지막 화분 {4} 가장 작은 식물을 가져간 건 El\n포인트 ▶ 최상급을 비교급으로 바꿔 이해하기", [('classmate', '반 친구'), ('tiny', '아주 작은')])
T.flex('괄호 안의 단어를 알맞은 형태로 바꿀 때 바르게 짝지어진 것은?', X_, B('• He is the ' + BL + ' singer in the band. (good)', '• That was the ' + BL + ' day of the year. (bad)'),
 ['best − worst', 'goodest − baddest', 'better − worse', 'best − baddest', 'most good − worst'],
 "이유 ▶ good − better − best / bad − worse − worst\n오답 ▶ 비교급(better · worse) · 규칙 변화(goodest · baddest) ❌\n포인트 ▶ 불규칙 최상급", [('band', '밴드')])
T.flex('다음 중 어법상 <u>틀린</u> 문장을 모두 고른 것은?', X_, B('(a) He is the most smart boy in class.', '(b) That is the biggest building in town.', '(c) She is the youngest of the three.', '(d) This is the most interesting book in the library.', '(e) It is the thinest book of all.'),
 ['(a), (e)', '(a), (b)', '(c), (d)', '(b), (e)', '(a), (d), (e)'],
 "이유 ▶ (a) smart → the smartest (e) thin → the thinnest\n옳은 것 ▶ (b) biggest (c) of the three (d) most interesting\n포인트 ▶ 1음절은 -est, 자음 겹침 주의", [('library', '도서관')])
T.flex('다음 표에 대한 설명으로 적절하지 <u>않은</u> 것은?', T_, B("<b>Ryan's Class: Favorite Food</b>") + TB(['food', 'pizza', 'chicken', 'bulgogi', 'spaghetti'], [['students', '10', '7', '5', '3']]),
 ['Bulgogi is the least popular food.', 'Pizza is the most popular food.', 'Chicken is more popular than bulgogi.', 'Twenty-five students answered.', 'Spaghetti is less popular than bulgogi.'],
 "이유 ▶ 가장 인기 없는 음식은 spaghetti(3명)\n오답 ▶ {1} 10명 {2} 7 ＞ 5 {3} 10 + 7 + 5 + 3 = 25 {4} 3 ＜ 5\n포인트 ▶ the least popular = 가장 인기 없는", [])
T.flex('다음 우리말을 영어로 바르게 옮긴 것은?', X_, B('이것은 그 책에서 가장 어려운 문제이다.'),
 ['This is the most difficult problem in the book.', 'This is the difficultest problem in the book.', 'This is most difficult problem in the book.', 'This is the more difficult problem in the book.', 'This is the most difficult problems in the book.'],
 "이유 ▶ the most + difficult + 단수 명사(This is ~ problem)\n오답 ▶ {1} ❌ {2} the 빠짐 {3} 비교급 {4} This is + 복수 ❌\n포인트 ▶ 3음절 이상은 the most", [('problem', '문제')])
T.render()

# ═══════════════ 최상급 2차 ═══════════════
T = Test('5', '최상급 2차', '최상급 2차 — 최상급 바꿔 쓰기', '최상급', N2, H=H); T.rot0 = 2
T.flex('다음 중 원급 − 비교급 − 최상급이 모두 바르게 짝지어진 것은?', X_, '',
 ['bad − worse − worst / hot − hotter − hottest', 'many − more − most / heavy − heavyer − heavyest', 'good − better − best / thin − thiner − thinest', 'busy − busier − busiest / useful − usefuler − usefulest', 'well − better − best / large − larger − largeest'],
 "이유 ▶ bad − worse − worst, hot − hotter − hottest ✔\n오답 ▶ {1} heavier · heaviest {2} thinner · thinnest {3} more · most useful {4} largest\n포인트 ▶ 두 개 다 맞아야 정답", [])
T.flex('(A), (B), (C)의 각 네모 안에서 어법에 맞는 표현으로 가장 적절한 것은?', X_, B('• It is the (A) [ most exciting / excitingest ] game of the year.', '• He is one of the (B) [ greatest player / greatest players ] in history.', '• This bridge is longer than any other (C) [ bridge / bridges ] in Korea.'),
 ['most exciting − greatest players − bridge', 'excitingest − greatest players − bridge', 'most exciting − greatest player − bridge', 'most exciting − greatest players − bridges', 'excitingest − greatest player − bridges'],
 "이유 ▶ (A) 긴 단어 most exciting (B) one of + 복수 (C) any other + 단수\n포인트 ▶ one of는 복수, any other는 단수", [('history', '역사'), ('bridge', '다리')])
T.fixed('다음 &lt;보기&gt;에서 어법상 올바른 문장의 개수는?', X_, B('&lt;보기&gt;', '• Mt. Halla is the highest mountain in South Korea.', '• This is the most cheap shirt in the store.', '• She is the most famous singer in Korea.', '• He is taller than any other boys in his class.', '• Jane is one of the smartest students in our school.', '• This is the goodest pizza in town.', '• Today is the hotter day of the year.'),
 NUMS, 3,
 "이유 ▶ 옳은 것: the highest · the most famous · one of the smartest students → 3개\n틀린 것 ▶ the cheapest / any other boy / the best / the hottest\n포인트 ▶ 형태 · any other · 불규칙 · 최상급 자리", [])
T.flex('다음 표를 바르게 설명한 것은?', T_, TB(['', 'Steak A', 'Steak B', 'Steak C'], [['price', '$10', '$20', '$35'], ['size', 'small', 'medium', 'large'], ['taste', '★☆☆', '★★☆', '★★★']]),
 ['Steak B is cheaper than Steak C, but it is not as delicious as Steak C.', 'Steak A is the most delicious of all.', 'Steak C is the cheapest of all.', 'Steak B is bigger than Steak C.', 'Steak A is more expensive than Steak B.'],
 "이유 ▶ B $20 ＜ C $35, 맛 ★★ ＜ ★★★ ✔\n오답 ▶ {1} 가장 맛있는 건 C {2} 가장 싼 건 A {3} C가 더 큼 {4} 10 ＜ 20\n포인트 ▶ but 앞뒤 둘 다 확인", [('delicious', '맛있는')])
T.flex('다음 중 의미가 나머지 넷과 <u>다른</u> 것은?', X_, '',
 ['Time is as precious as anything else.', 'Time is the most precious thing.', 'Time is more precious than anything else.', 'Nothing is more precious than time.', 'Nothing is as precious as time.'],
 "이유 ▶ 나머지는 '시간이 가장 소중하다', 이 문장은 '다른 것만큼 소중하다'(같다).\n오답 ▶ {1} 최상급 {2} 비교급 + than anything else {3}·{4} Nothing ~ 비교급 / as ~ as\n포인트 ▶ 최상급 뜻 = Nothing is 비교급 than / as 원급 as", [('precious', '소중한')])
T.flex('다음 우리말을 영어로 바르게 옮긴 것은?', X_, B('그는 세계에서 가장 위대한 과학자 중 한 명이다.'),
 ['He is one of the greatest scientists in the world.', 'He is one of the greatest scientist in the world.', 'He is one of the most great scientists in the world.', 'He is one of greatest scientists in the world.', 'He is the one of greatest scientist in the world.'],
 "이유 ▶ one of the + greatest + 복수 명사\n오답 ▶ {1} 단수 ❌ {2} most great ❌ {3} the 빠짐 {4} 어순·단수 ❌\n포인트 ▶ one of the 최상급 복수", [('scientist', '과학자')])
T.fixed('다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 <u>틀린</u> 것의 개수는?', X_, B('Nina is ⓐ ' + U('the most beautiful') + ' teacher in our school. She is also one of ⓑ ' + U('the thinnest') + ' teachers. Students like her because she is ⓒ ' + U('the funnier') + ' teacher. She is ⓓ ' + U('taller') + ' than any other teacher in school. She works in ⓔ ' + U('the most high') + ' building in Seoul.'),
 NUMS, 2,
 "이유 ▶ 틀린 것: ⓒ the funniest ⓔ the highest → 2개\n옳은 것 ▶ ⓐ the most beautiful ⓑ the thinnest ⓓ taller than any other teacher\n포인트 ▶ 비교급 / 최상급 자리 구별", [('thin', '마른')])
T.flex('다음 대화를 읽고 힘이 센 순서대로 바르게 나열한 것은?', X_, B('A: Is Mike stronger than Kevin?', 'B: Yes, but Jenny is stronger than Mike.', 'A: What about Tom?', 'B: Tom is the weakest of the four.'),
 ['Jenny − Mike − Kevin − Tom', 'Mike − Jenny − Kevin − Tom', 'Jenny − Kevin − Mike − Tom', 'Tom − Kevin − Mike − Jenny', 'Jenny − Mike − Tom − Kevin'],
 "이유 ▶ Mike ＞ Kevin, Jenny ＞ Mike, Tom이 가장 약함 → Jenny − Mike − Kevin − Tom\n포인트 ▶ the weakest = 가장 약한", [('strong', '힘센'), ('weak', '약한')])
T.flex('다음 빈칸에 들어갈 말로 알맞지 <u>않은</u> 것은?', X_, B('This is the ' + BL + ' building in the city.'),
 ['most tall', 'tallest', 'oldest', 'most famous', 'biggest'],
 "이유 ▶ tall의 최상급은 tallest → most tall ❌\n오답 ▶ {1}·{2}·{3}·{4} 바른 최상급\n포인트 ▶ 1음절은 -est", [])
T.flex('다음 우리말과 의미가 같은 문장을 모두 고른 것은?', X_, B('Daniel은 셋 중에서 가장 나이가 많다.', '', '(a) Daniel is the oldest of the three.', '(b) Daniel is older than the other two.', '(c) Daniel is the oldest in the three.', '(d) The other two are younger than Daniel.', '(e) Daniel is older than any other three.'),
 ['(a), (b), (d)', '(a), (c)', '(b), (c), (e)', '(a), (d), (e)', '(c), (d)'],
 "이유 ▶ (a) of the three (b) 나머지 두 명보다 많다 (d) 나머지 두 명이 더 어리다 ✔\n틀린 것 ▶ (c) 숫자 앞은 of (e) any other three ❌\n포인트 ▶ 셋 중 최고 = 나머지 둘보다 더", [])
T.flex('다음 표의 내용과 일치하는 것은?', T_, TB(['', 'Allowance', 'Saving'], [['Lucas', '$10', '$7'], ['Susan', '$20', '$10'], ['Alex', '$15', '$10'], ['Maria', '$15', '$0']]),
 ['Susan gets the most allowance of the four.', 'Maria saves more money than Lucas.', 'Alex saves less money than Lucas.', 'Lucas gets more allowance than Alex.', 'Susan saves the least money of the four.'],
 "이유 ▶ 용돈은 Susan $20이 가장 많음 ✔\n오답 ▶ {1} 0 ＜ 7 {2} 10 ＞ 7 {3} 10 ＜ 15 {4} 가장 적게 모으는 건 Maria($0)\n포인트 ▶ the most / the least", [('allowance', '용돈'), ('save', '저축하다')])
T.flex('다음 단어를 배열하여 문장을 만들 때 <u>6번째</u>로 오는 단어는?', X_, B('목성은 다른 어떤 행성보다 더 크다.', '( other / is / Jupiter / than / any / bigger / planet )'),
 ['other', 'any', 'planet', 'than', 'bigger'],
 "완성 ▶ Jupiter(1) is(2) bigger(3) than(4) any(5) other(6) planet(7).\n포인트 ▶ than any other + 단수 명사", [('planet', '행성')])
T.flex('다음 중 어법상 올바른 것은?', X_, '',
 ['He is one of the best players on the team.', 'She is the most happiest girl in the world.', 'This is the more expensive bag of the three.', 'Tom is the taller boy in his class.', 'It is longest river in Korea.'],
 "이유 ▶ one of the best + 복수 명사 ✔\n오답 ▶ {1} most happiest(겹침) {2} 셋 중 → the most expensive {3} the tallest {4} the 빠짐\n포인트 ▶ 셋 이상 비교 = 최상급", [('player', '선수')])
T.flex('빈칸 ⓐ~ⓔ에 들어갈 말로 바르게 연결된 것은?', X_, B('• Can a turtle swim ⓐ ' + BL + ' as a fish? (fast)', '• This test was ⓑ ' + BL + ' harder than the last one.', '• Mina is ⓒ ' + BL + ' of the five girls. (young)', '• My bag is less ⓓ ' + BL + ' than yours. (heavy)', '• He is one of the kindest ⓔ ' + BL + ' in our town.'),
 ['ⓒ − the youngest', 'ⓐ − as faster', 'ⓑ − very', 'ⓓ − heavier', 'ⓔ − man'],
 "이유 ▶ ⓒ of the five girls → the youngest ✔\n오답 ▶ {1} as fast {2} much · even · far {3} less 뒤 원급 heavy {4} one of + 복수 men\n포인트 ▶ 원급 · 강조 · 최상급 · less · one of 한꺼번에", [])
T.flex('다음 그림에 대한 설명으로 적절하지 <u>않은</u> 것은?', T_, TB(['Sam', 'Nick', 'Leo'], [['140cm', '165cm', '180cm']]),
 ['Nick is the tallest among the three.', 'Leo is taller than Nick.', 'Sam is shorter than Leo.', 'Sam is the shortest among the three.', 'Nick is taller than Sam.'],
 "이유 ▶ 가장 큰 사람은 Leo(180cm)\n오답 ▶ {1} 180 ＞ 165 {2} 140 ＜ 180 {3} 140cm {4} 165 ＞ 140\n포인트 ▶ among the three = 셋 중에서", [])
T.flex('다음 문장과 의미가 통하는 것은?', L_, B('El and Jo were the smallest students in the class.'),
 ['The other students in the class were bigger than El and Jo.', 'El and Jo were bigger than the other students.', 'El was smaller than Jo.', 'El and Jo were as big as the other students.', 'Only El was the smallest student.'],
 "이유 ▶ 반에서 가장 작았다 = 다른 학생들이 더 컸다.\n오답 ▶ {1} 반대 {2} 둘의 비교는 글에 없음 {3} 같다 {4} El과 Jo 둘 다\n포인트 ▶ 최상급 → 비교급으로 바꿔 읽기", [])
T.flex('다음 대화의 빈칸에 들어갈 말로 알맞은 것은?', X_, B('A: Who gets up the earliest in your family?', 'B: My dad does. He gets up ' + BL + ' of all.'),
 ['the earliest', 'earlier', 'the most early', 'the earlyest', 'most earlier'],
 "이유 ▶ of all(모두 중에서) → 최상급 the earliest\n오답 ▶ {1} 비교급 {2}·{3} 형태 ❌ {4} 겹침\n포인트 ▶ early → earliest", [('early', '일찍')])
T.flex('다음 문장과 의미가 같은 것을 모두 고른 것은?', X_, B('Sam is the tallest boy in his class.', '', '(a) Sam is taller than any other boy in his class.', '(b) No boy in his class is taller than Sam.', '(c) Sam is taller than all the other boys in his class.', '(d) Sam is as tall as any other boy in his class.', '(e) Sam is taller than any other boys in his class.'),
 ['(a), (b), (c)', '(a), (d)', '(b), (c), (e)', '(a), (c), (e)', '(b), (d)'],
 "이유 ▶ (a) any other + 단수 (b) No ~ 비교급 than (c) all the other + 복수 ✔\n틀린 것 ▶ (d) 같다 (e) any other boys ❌\n포인트 ▶ all the other 뒤는 복수, any other 뒤는 단수", [])
T.flex('다음 글을 읽고, 세 사람이 가진 책은 모두 몇 권인지 고르면?', T_, B('Ann has 15 books. Ben has 4 more books than Ann, so he has the most books of the three. Cody has 3 fewer books than Ann.'),
 ['46', '42', '49', '34', '31'],
 "이유 ▶ Ben = 15 + 4 = 19, Cody = 15 − 3 = 12 → 15 + 19 + 12 = 46\n포인트 ▶ more / fewer 계산 후 더하기", [])
T.flex('다음 우리말을 영어로 바르게 옮긴 것은?', X_, B('이 가방이 셋 중에서 가장 덜 비싸다.'),
 ['This bag is the least expensive of the three.', 'This bag is the less expensive of the three.', 'This bag is the least expensive in the three.', 'This bag is least expensive than the three.', 'This bag is the most expensive of the three.'],
 "이유 ▶ 가장 덜 ~한 = the least + 원급, 숫자 앞 of\n오답 ▶ {1} 비교급 {2} in ❌ {3} than ❌ {4} 반대 뜻\n포인트 ▶ little − less − least", [])
T.render()

# ═══════════════ 최상급 3차 ═══════════════
T = Test('6', '최상급 3차', '최상급 3차 — 비교급·원급 종합(최상)', '최상급', N2, H=H); T.rot0 = 5
T.fixed('다음 중 원급과 최상급이 바르게 짝지어지지 <u>않은</u> 것의 개수는?', X_, B('(a) nice − nicest  (b) sad − saddest  (c) early − earlyest  (d) useful − usefulest', '(e) bad − worst  (f) thin − thinnest  (g) much − most'),
 NUMS, 2,
 "이유 ▶ 틀린 것: (c) earliest (d) most useful → 2개\n옳은 것 ▶ nicest · saddest · worst · thinnest · most\n포인트 ▶ -ful은 most + 원급", [])
T.flex('다음 빈칸 (A), (B)에 들어갈 말이 바르게 짝지어진 것은?', X_, B('Of the three bags, the red one is ____(A)____. (cheap)', 'And the blue one is ____(B)____ than the red one. (expensive)'),
 ['the cheapest − more expensive', 'cheaper − more expensive', 'the cheapest − most expensive', 'the most cheap − more expensive', 'the cheapest − expensiver'],
 "이유 ▶ (A) 셋 중 → the cheapest (B) than → more expensive\n포인트 ▶ 한 글 안의 최상급 / 비교급 자리", [])
T.flex('다음 중 짝지어진 두 문장의 의미가 같은 것은?', X_, '',
 ['Seoul is the biggest city in Korea.<br>= Seoul is bigger than any other city in Korea.', 'Mina is the youngest of the three.<br>= Mina is older than the other two.', 'This is the cheapest bag.<br>= This bag is more expensive than any other bag.', 'He is the best singer.<br>= He sings worse than anyone else.', 'No one is as kind as Jane.<br>= Jane is not the kindest person.'],
 "이유 ▶ 최상급 = 비교급 + than any other + 단수 ✔\n오답 ▶ {1} older ↔ younger {2} cheapest ↔ more expensive {3} best ↔ worse {4} 가장 친절함 ↔ not\n포인트 ▶ 바꿔 쓸 때 형용사의 방향", [])
T.flex('다음 중 어법상 올바른 문장을 모두 고른 것은?', X_, B('(A) It was the most exciting game of the season.', '(B) Texas is the largest than France in land area.', '(C) She is one of the most talented artists in Korea.', '(D) This room is the most cleanest in the house.', '(E) Mike is taller than any other student in his school.', '(F) That was the baddest movie of the year.'),
 ['(A), (C), (E)', '(B), (C), (D)', '(A), (D), (F)', '(C), (E), (F)', '(A), (B), (E)'],
 "이유 ▶ (A) the most exciting (C) one of + 복수 (E) any other + 단수 ✔\n틀린 것 ▶ (B) than 앞 → larger (D) the cleanest (F) the worst\n포인트 ▶ 최상급 + than ❌, 겹침 ❌", [('talented', '재능 있는'), ('season', '시즌')])
T.flex('다음 표의 내용과 일치하는 것은?', T_, TB(['', 'Horse', 'Elephant', 'Bear', 'Giraffe'], [['Height(cm)', '160', '300', '200', '500'], ['Weight(kg)', '600', '5,000', '800', '1,300'], ['Age', '30', '60', '25', '15']]),
 ['The giraffe is the tallest but the youngest of the four.', 'The bear is the heaviest of the four.', 'The horse is taller than the bear.', 'The elephant is the tallest of the four.', 'The giraffe is heavier than the elephant.'],
 "이유 ▶ 기린 500cm로 가장 크고, 15살로 가장 어림 ✔\n오답 ▶ {1} 가장 무거운 건 코끼리 {2} 160 ＜ 200 {3} 가장 큰 건 기린 {4} 1,300 ＜ 5,000\n포인트 ▶ 표의 두 줄을 동시에 확인", [('giraffe', '기린')])
T.fixed('다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 올바른 것의 개수는?', X_, B('Jupiter is ⓐ ' + U('the biggest') + ' planet in the solar system. It is ⓑ ' + U('much bigger') + ' than Earth. Mercury is ⓒ ' + U('the most small') + ' planet. Venus is ⓓ ' + U('hotter') + ' than any other planet. Saturn is one of ⓔ ' + U('the most beautiful planet') + '.'),
 NUMS, 3,
 "이유 ▶ 옳은 것: ⓐ the biggest ⓑ much bigger ⓓ hotter than any other planet → 3개\n틀린 것 ▶ ⓒ the smallest ⓔ planets(복수)\n포인트 ▶ one of + 복수, 1음절 -est", [('solar system', '태양계')])
T.flex('주어진 단어를 모두 사용하되 필요하면 형태를 바꾸어 문장을 만들 때, <u>4번째</u>로 오는 단어는?', X_, B('그것은 내 인생에서 가장 행복한 날이었다.', '( it / was / day / happy / life / my / of / the )'),
 ['happiest', 'happy', 'day', 'the', 'most'],
 "완성 ▶ It(1) was(2) the(3) happiest(4) day(5) of(6) my(7) life(8).\n오답 ▶ {1} 형태를 바꿔야 함 {4} the most happy ❌\n포인트 ▶ 형태 변화 + 위치", [])
T.flex('다음 &lt;보기&gt;를 읽고, 두 번째로 나이가 많은 사람을 고르면?', X_, B('• Ann is older than Ben.', '• Cindy is the youngest of the five.', '• Dave is older than Ann.', '• Ben is older than Eric.'),
 ['Ann', 'Dave', 'Ben', 'Eric', 'Cindy'],
 "이유 ▶ Dave ＞ Ann ＞ Ben ＞ Eric, Cindy가 가장 어림 → 두 번째는 Ann\n포인트 ▶ 다섯 명 순서를 다 세운 뒤 고르기", [])
T.flex('다음 중 빈칸에 들어갈 말이 나머지 넷과 <u>다른</u> 것은?', X_, '',
 ['He is the tallest ' + BL + ' the three.', 'She is the best singer ' + BL + ' her school.', 'This is the oldest tree ' + BL + ' the park.', 'Seoul is the biggest city ' + BL + ' Korea.', 'I am the happiest girl ' + BL + ' the world.'],
 "이유 ▶ the three(숫자) → of. 나머지는 장소·범위 → in.\n포인트 ▶ of + 복수·숫자 / in + 장소·집단", [])
T.flex('다음 중 의미가 나머지 넷과 <u>다른</u> 것은?', X_, '',
 ['Health is less important than other things.', 'Health is the most important thing.', 'Health is more important than anything else.', 'Nothing is more important than health.', 'Nothing is as important as health.'],
 "이유 ▶ 나머지는 '건강이 가장 중요하다', 이 문장은 '덜 중요하다'.\n오답 ▶ {1}~{4} 최상급 뜻의 여러 표현\n포인트 ▶ less = 덜", [('health', '건강')])
T.flex('다음 표의 내용과 일치하지 <u>않는</u> 것은?', T_, TB(['', 'storybooks', 'comic books', 'magazines'], [['Me', '20', '10', '3'], ['Junho', '7', '20', '2'], ['Minhee', '32', '5', '10'], ['Gayeon', '10', '8', '20']]),
 ['I have the most storybooks of the four.', 'Gayeon has the most magazines of the four.', 'Junho has the fewest magazines of the four.', 'Minhee has fewer comic books than I have.', 'Junho has more comic books than anyone else.'],
 "이유 ▶ 이야기책이 가장 많은 사람은 Minhee(32권)\n오답 ▶ {1} 20권 {2} 2권 {3} 5 ＜ 10 {4} 20권으로 가장 많음\n포인트 ▶ the fewest = 가장 적은", [('magazine', '잡지')])
T.flex('다음 우리말을 영어로 바르게 옮긴 것은?', E_, B('Jina의 농담은 항상 내 것보다 훨씬 더 웃기다.'),
 ["Jina's jokes are always much funnier than mine.", "Jina's jokes are always much funnyer than mine.", "Jina's jokes are always very funnier than mine.", "Jina's jokes are always much funnier than me.", "Jina's jokes are always more much funnier than mine."],
 "이유 ▶ much + funnier + than mine(내 농담)\n오답 ▶ {1} funnier {2} very ❌ {3} 농담 ↔ 나 ❌ {4} 겹침\n포인트 ▶ 강조 · 형태 · 비교 대상 동시에", [('joke', '농담')])
T.fixed('다음 대화의 밑줄 친 ①~⑤ 중 흐름상 <u>어색한</u> 것은?', T_, B('A: What is the most popular sport in your class?', 'B: ① ' + U('Soccer is. Twelve students chose it.'), 'A: How about basketball and baseball?', 'B: ② ' + U('Eight students chose basketball, and two chose baseball.'), 'A: ③ ' + U('Then baseball is the least popular of the three.'), 'B: ④ ' + U('Yes. And basketball is more popular than soccer.'), 'A: ⑤ ' + U('I see. Soccer is really popular in your class.')),
 None, 4,
 "이유 ▶ 농구 8명 ＜ 축구 12명 → basketball is less popular than soccer\n오답 ▶ ① 가장 인기 ② 숫자 ③ 2명이 가장 적음 ⑤ 결론\n포인트 ▶ 숫자로 비교급 확인", [('choose', '고르다')])
T.flex('다음 글의 빈칸에 들어갈 말로 알맞은 것은?', X_, B('Mina is 160cm tall. Jisu is 155cm tall. Hana is 165cm tall. Jisu is ' + BL + ' of the three.'),
 ['the shortest', 'shorter', 'the tallest', 'the most short', 'shortest than'],
 "이유 ▶ 155cm로 가장 작음 + of the three → the shortest\n오답 ▶ {1} 비교급 {2} 반대 {3} ❌ {4} 최상급 + than ❌\n포인트 ▶ of the three = 셋 중", [])
T.fixed('다음 &lt;보기&gt;에서 어법상 올바른 문장의 개수는?', X_, B('&lt;보기&gt;', '• This is the most interesting book of them.', '• He is one of the richest men in the world.', '• She is the more famous actress in Korea.', '• Minsu runs faster than any other boy in his class.', '• It was the worst storm in 100 years.', '• My bag is the heavyest of the three.', '• Jejudo is the largest island in Korea.', '• Kevin is more taller than Sue.'),
 NUMS, 5,
 "이유 ▶ 옳은 것: the most interesting · one of the richest men · faster than any other boy · the worst · the largest → 5개\n틀린 것 ▶ the most famous / the heaviest / taller\n포인트 ▶ men(man의 복수)", [('storm', '폭풍'), ('island', '섬')])
T.flex('다음 글의 내용과 일치하는 것은?', L_, B("On the last day of summer, Jo came to El's house. El and Jo ran to the garden and suddenly stopped. Something was DIFFERENT! There were flowers on the aster ... and El grew TALLER, TOO!"),
 ['El was taller at the end of summer than at the beginning of summer.', 'El was the shortest at the end of summer.', 'The aster had fewer flowers at the end of summer.', "El didn't grow at all during the summer.", 'Jo came to the garden on the first day of summer.'],
 "이유 ▶ El grew TALLER → 여름 끝에 더 커졌다 ✔\n오답 ▶ {1} 글에 없음 {2} 꽃이 없다가 피었음 {3} 반대 {4} 마지막 날\n포인트 ▶ grow + 비교급 = 더 ~해지다", [('aster', '과꽃')])
T.flex('괄호 안의 단어를 알맞은 형태로 바꿀 때 바르게 짝지어진 것은?', X_, B('• Can you come home as ' + BL + ' as possible? (early)', '• She is the ' + BL + ' of the three. (busy)', '• Your plan is ' + BL + ' than mine. (good)'),
 ['early − busiest − better', 'earlier − busiest − better', 'early − busyest − better', 'early − busiest − gooder', 'earliest − busier − better'],
 "이유 ▶ as ~ as 원급 early / the + busiest / than 앞 better\n포인트 ▶ 원급 · 최상급 · 비교급 한 문제에", [('possible', '가능한')])
T.flex('다음 표에 대한 설명으로 적절하지 <u>않은</u> 것은?', T_, TB(['food', 'pizza', 'chicken', 'bulgogi', 'tteokbokki', 'spaghetti'], [['students', '9', '7', '5', '3', '1']]),
 ['More than half of the students like chicken.', 'Pizza is the most popular food in this class.', 'Only one student likes spaghetti.', 'Bulgogi is more popular than tteokbokki.', 'There are twenty-five students in this class.'],
 "이유 ▶ 전체 25명 중 치킨 7명 → 반(13명 이상)이 넘지 않음\n오답 ▶ {1} 9명 {2} 1명 {3} 5 ＞ 3 {4} 9 + 7 + 5 + 3 + 1 = 25\n포인트 ▶ more than half = 절반보다 많은", [('half', '절반')])
T.flex('(가), (나), (다)의 단어를 배열하여 문장을 완성할 때, 각 문장에서 <u>4번째</u>로 오는 단어끼리 모은 것은?', X_, B('(가) ( popular / other / any / soccer / is / more / sport / than )', "(나) ( as / as / her / is / voice / a bird's / sweet )", '(다) ( the / is / building / tallest / this / town / in )'),
 ['popular − as − tallest', 'more − sweet − the', 'popular − sweet − building', 'than − as − tallest', 'more − as − the'],
 "완성 ▶ (가) Soccer is more popular(4) than any other sport. (나) Her voice is as(4) sweet as a bird's. (다) This is the tallest(4) building in town.\n포인트 ▶ 비교급 · 원급 비교 · 최상급 어순", [('voice', '목소리')])
T.flex('다음 글을 읽고, Minsu는 John보다 몇 cm 더 큰지 고르면?', T_, B('Tom is 165cm tall. John is 3cm shorter than Tom. Minsu is the tallest of the three, and he is 3cm taller than Tom.'),
 ['6cm', '3cm', '9cm', '4cm', '0cm'],
 "이유 ▶ John = 162, Minsu = 168 → 168 − 162 = 6cm\n포인트 ▶ 기준(Tom)에서 각각 계산", [])
T.render()
