import sys, json, subprocess
sys.path.insert(0, '/tmp/claude-0/-home-claude/a9e3e882-1f02-5d62-8f70-aced81bc59d2/scratchpad')
from gencommon import *

# 중1 천재(소영순) Lesson 5 · Share Your Joys and Worries (본문: Growing Season)
S1 = [("El and Jo were the smallest students in the class.", "El과 Jo는 반에서 가장 작은 학생들이었다."),
      ("They were always together.", "그들은 항상 함께였다."),
      ("They even watered the plants together in the class because they could not reach the pots alone.", "그들은 혼자서는 화분에 손이 닿지 않았기 때문에 교실에서 식물에 물도 함께 주었다."),
      ("However, in the spring, something was DIFFERENT.", "하지만 봄이 되자 무언가가 달라졌다."),
      ("Jo grew TALLER!", "Jo의 키가 더 커졌다!"),
      ("Jo was taller than El, so Jo could water the plants alone.", "Jo는 El보다 키가 더 컸고, 그래서 혼자서 식물에 물을 줄 수 있었다."),
      ("El felt smaller every day.", "El은 매일 더 작아지는 기분이었다.")]
S2 = [("On the last day of school, Mr. Diaz said, \"Class, you can take a flower home and care for it over the summer.\"", "학교 마지막 날, Diaz 선생님이 말씀하셨다. \"여러분, 꽃을 하나 집에 가져가서 여름 동안 돌보세요.\""),
      ("All the students ran to the window.", "모든 학생이 창문으로 달려갔다."),
      ("El's classmates reached for the pots over tiny El.", "El의 반 친구들은 작은 El 너머로 화분에 손을 뻗었다."),
      ("They took all the pots with colorful flowers.", "그들은 알록달록한 꽃이 있는 화분을 모두 가져갔다."),
      ("El took the last pot.", "El은 마지막 화분을 가져갔다."),
      ("It had the smallest plant with no flowers.", "그 화분에는 꽃이 없는 가장 작은 식물이 있었다."),
      ("\"I feel just like you, little plant,\" said El.", "\"나도 꼭 너 같은 기분이야, 작은 식물아.\" El이 말했다."),
      ("Mr. Diaz looked at El and said, \"That's an aster plant. In time, it'll grow and have beautiful flowers.\"", "Diaz 선생님이 El을 보며 말씀하셨다. \"그건 과꽃이란다. 시간이 지나면 자라서 아름다운 꽃을 피울 거야.\""),
      ("\"But it's just a little green plant,\" said El.", "\"하지만 그냥 작은 초록 식물일 뿐인걸요.\" El이 말했다."),
      ("She was not so sure.", "그녀는 그다지 확신하지 못했다."),
      ("\"You can have my zinnia plant,\" Jo said to El, \"I'll be at my grandma's all summer.\"", "\"내 백일홍을 가져도 돼.\" Jo가 El에게 말했다. \"나는 여름 내내 할머니 댁에 있을 거야.\""),
      ("\"I'll plant my aster and your zinnia side by side,\" El said.", "\"내 과꽃과 네 백일홍을 나란히 심을게.\" El이 말했다."),
      ("\"They'll be good friends — just like us!\" said Jo.", "\"그 둘은 좋은 친구가 될 거야, 꼭 우리처럼!\" Jo가 말했다."),
      ("El smiled.", "El은 미소 지었다.")]
S3 = [("El planted the flowers in her garden.", "El은 정원에 꽃들을 심었다."),
      ("It was growing season.", "식물이 자라는 시기였다."),
      ("All summer long, she cared for them.", "여름 내내 그녀는 그것들을 돌보았다."),
      ("On the last day of summer, Jo came to El's house.", "여름의 마지막 날, Jo가 El의 집에 왔다."),
      ("El and Jo ran to the garden and suddenly stopped.", "El과 Jo는 정원으로 달려가다가 갑자기 멈췄다."),
      ("Something was DIFFERENT!", "무언가가 달라져 있었다!"),
      ("There were flowers on the aster ... and El grew TALLER, TOO!", "과꽃에 꽃이 피어 있었다... 그리고 El도 키가 더 컸다!")]
L = lambda S, i: S[i][0]

# ═════════════ 5과 본문 ❶❷ ═════════════
da = steps(
 vocab=[['smallest', '가장 작은 (small - smaller - smallest)', '❶'], ['always', '항상', '❶'], ['together', '함께', '❶'], ['even', '심지어, ~도', '❶'],
        ['water', '물을 주다; 물', '❶'], ['plant', '식물; 심다', '❶'], ['reach', '~에 닿다', '❶'], ['pot', '화분', '❶'], ['alone', '혼자서', '❶'],
        ['however', '하지만', '❶'], ['different', '다른, 달라진', '❶'], ['grow', '자라다 (grow - grew - grown)', '❶'], ['taller', '키가 더 큰', '❶'],
        ['feel', '느끼다 (feel - felt - felt)', '❶'], ['last', '마지막의', '❷'], ['take ~ home', '~을 집에 가져가다', '❷'], ['care for', '~을 돌보다', '❷'],
        ['over the summer', '여름 동안', '❷'], ['classmate', '반 친구', '❷'], ['reach for', '~에 손을 뻗다', '❷'], ['tiny', '아주 작은', '❷'],
        ['colorful', '알록달록한', '❷'], ['look at', '~을 보다', '❷'], ['aster', '과꽃', '❷'], ['in time', '시간이 지나면, 머지않아', '❷'],
        ['sure', '확신하는', '❷'], ['zinnia', '백일홍', '❷'], ['all summer', '여름 내내', '❷'], ['side by side', '나란히', '❷'], ['smile', '미소 짓다', '❷']],
 pickv=[
  (L(S1, 1).replace('always together', 'always {together|alone}'), "정답 ▶ together (함께)\n오답 ▶ alone (혼자): 바로 뒤에 식물에 물도 '함께(together)' 주었다고 나와요. 늘 함께 다니는 단짝이에요."),
  (L(S1, 2).replace('pots alone', 'pots {alone|together}'), "정답 ▶ alone (혼자서)\n오답 ▶ together: 둘 다 키가 작아 '혼자서는' 화분에 손이 닿지 않아서 함께 물을 줬어요."),
  (L(S1, 6).replace('smaller', '{smaller|bigger}'), "정답 ▶ smaller (더 작은)\n오답 ▶ bigger (더 큰): Jo는 키가 커졌는데 El은 그대로라 매일 '더 작아지는' 기분이었어요."),
  (L(S2, 2).replace('tiny', '{tiny|tall}'), "정답 ▶ tiny (아주 작은)\n오답 ▶ tall (키가 큰): 반 친구들이 '작은' El 머리 위로 손을 뻗어 화분을 가져갔어요."),
  (L(S2, 3).replace('with colorful', 'with {colorful|no}'), "정답 ▶ colorful (알록달록한)\n오답 ▶ no: 친구들은 '알록달록한 꽃이 있는' 화분을 다 가져갔고, El에게는 '꽃이 없는(with no flowers)' 화분만 남았어요."),
  (L(S2, 4).replace('the last', 'the {last|first}'), "정답 ▶ last (마지막의)\n오답 ▶ first (첫 번째의): 친구들이 다 가져간 뒤 El은 '마지막' 화분을 가져갔어요."),
  (L(S2, 11).replace('side by side', '{side by side|far apart}'), "정답 ▶ side by side (나란히)\n오답 ▶ far apart (멀리 떨어뜨려): 바로 다음에 '둘은 좋은 친구가 될 거야'라고 해요. 나란히 심어요."),
  (L(S2, 12).replace('good friends', 'good {friends|enemies}'), "정답 ▶ friends (친구들)\n오답 ▶ enemies (적들): 'just like us(꼭 우리처럼)' → 단짝인 El과 Jo처럼 '좋은 친구'가 될 거래요."),
  (L(S2, 13).replace('smiled', '{smiled|cried}'), "정답 ▶ smiled (미소 지었다)\n오답 ▶ cried (울었다): 친구의 따뜻한 말에 El은 '미소' 지었어요."),
 ],
 tf=[
  ["El and Jo were the tallest students in the class.", False, "정답 ▶ F\n이유: 가장 키가 큰(tallest)이 아니라 가장 작은(smallest) 학생들이었어요.", '❶', "El and Jo were the smallest students in the class"],
  ["El and Jo watered the plants together.", True, "정답 ▶ T\n이유: 혼자서는 화분에 닿지 않아 함께 물을 줬어요.", '❶', "They even watered the plants together"],
  ["In the spring, El grew taller than Jo.", False, "정답 ▶ F\n이유: 봄에 키가 커진 사람은 Jo예요. Jo가 El보다 더 컸어요.", '❶', "Jo was taller than El"],
  ["Mr. Diaz let the students take a flower home.", True, "정답 ▶ T\n이유: 'you can take a flower home' → 꽃을 집에 가져가도 된다고 했어요.\n어휘 ▶ let ~하게 해 주다", '❷', "you can take a flower home"],
  ["El took a pot with colorful flowers.", False, "정답 ▶ F\n이유: El은 꽃이 없는(with no flowers) 가장 작은 식물이 있는 마지막 화분을 가져갔어요.", '❷', "It had the smallest plant with no flowers"],
  ["Mr. Diaz said El's plant would have beautiful flowers.", True, "정답 ▶ T\n이유: 시간이 지나면 자라서 아름다운 꽃을 피울 거라고 했어요.", '❷', "it'll grow and have beautiful flowers"],
  ["Jo gave El her zinnia plant.", True, "정답 ▶ T\n이유: 'You can have my zinnia plant' → 내 백일홍을 가져도 된다고 했어요.", '❷', "You can have my zinnia plant"],
  ["Jo stayed at home all summer.", False, "정답 ▶ F\n이유: Jo는 여름 내내 할머니 댁(my grandma's)에 있을 거라고 했어요.", '❷', "I'll be at my grandma's all summer"],
 ],
 ilchi=[
  {'n': '❶', 'box': ['❶'], 'q': "글의 내용과 일치하지 <u>않는</u> 것은?",
   'opts': ["El was taller than Jo in the spring.", "El and Jo were always together.", "They couldn't reach the pots alone.", "Jo grew taller in the spring.", "El felt smaller every day."],
   'ex': "정답 ▶ El was taller than Jo in the spring.\n이유: 봄에는 Jo가 El보다 더 컸어요(Jo was taller than El).",
   'per': [["봄에 El이 Jo보다 키가 컸다.", "Jo was taller than El", "불일치 → Jo가 더 큼"],
           ["El과 Jo는 항상 함께였다.", "They were always together", "일치"],
           ["그들은 혼자서는 화분에 닿을 수 없었다.", "they could not reach the pots alone", "일치"],
           ["봄에 Jo의 키가 커졌다.", "Jo grew TALLER", "일치"],
           ["El은 매일 더 작아지는 기분이었다.", "El felt smaller every day", "일치"]]},
  {'n': '❷', 'box': ['❷'], 'q': "글의 내용과 <u>일치하는</u> 것은?",
   'opts': ["El's plant had no flowers at first.", "El took the first pot.", "Mr. Diaz said El's plant would never grow.", "Jo will stay at El's house all summer.", "El was sure that her plant would have flowers."],
   'ex': "정답 ▶ El's plant had no flowers at first.\n이유: It had the smallest plant with no flowers.\n어휘 ▶ at first 처음에는",
   'per': [["El의 식물은 처음에 꽃이 없었다.", "It had the smallest plant with no flowers", "일치"],
           ["El은 첫 번째 화분을 가져갔다.", "El took the last pot", "불일치 → 마지막 화분"],
           ["선생님은 El의 식물이 절대 자라지 않을 거라고 했다.", "it'll grow and have beautiful flowers", "불일치 → 자랄 것"],
           ["Jo는 여름 내내 El의 집에 있을 것이다.", "I'll be at my grandma's all summer", "불일치 → 할머니 댁"],
           ["El은 자기 식물에 꽃이 필 거라고 확신했다.", "She was not so sure", "불일치 → 확신하지 못함"]]},
 ],
 pickg=[
  (L(S1, 0).replace('the smallest', 'the {smallest|smaller}'), "정답 ▶ smallest\n이유: '반에서(in the class)' 여럿 중 가장 → 최상급 the + -est\n오답 ▶ smaller는 둘을 비교할 때 (than과 함께)"),
  (L(S1, 0).replace(' were ', ' {were|was} '), "정답 ▶ were\n이유: 주어 El and Jo(두 사람 → 복수) + 과거 → were"),
  (L(S1, 2).replace('could not reach', 'could not {reach|reaching}'), "정답 ▶ reach\n이유: 조동사 could 뒤에는 동사원형!"),
  (L(S1, 5).replace('than El', '{than|then} El'), "정답 ▶ than\n이유: 비교급 + than = ~보다 더 …한. then(그때, 그러고 나서)과 철자 헷갈리지 마세요!"),
  (L(S1, 5).replace(', so Jo', ', {so|because} Jo'), "정답 ▶ so\n이유: 키가 더 컸다(원인) → 그래서 혼자 물을 줄 수 있었다(결과) → so(그래서)\n오답 ▶ because는 뒤에 '이유'가 와요."),
  (L(S2, 1).replace('ran to', '{ran|run} to'), "정답 ▶ ran\n이유: 지난 일 → 과거형. run - ran - run (불규칙)"),
  (L(S2, 0).replace('a flower home', 'a flower {home|to home}'), "정답 ▶ home\n이유: home은 '집으로'라는 부사라 앞에 to를 쓰지 않아요. take ~ home = ~을 집에 가져가다 (go home, come home)"),
  (L(S2, 7).replace('looked at', 'looked {at|to}'), "정답 ▶ at\n이유: look at ~ = ~을 보다 (짝꿍 표현)"),
  (L(S2, 11).replace("I'll plant", "I'll {plant|planting}"), "정답 ▶ plant\n이유: I'll = I will. 조동사 will 뒤에는 동사원형!"),
  (L(S2, 9).replace('She was', 'She {was|were}'), "정답 ▶ was\n이유: 주어 She(단수) + 과거 → was"),
 ],
 verb=[
  (L(S1, 6).replace('El felt', 'El ___'), 'feel', ['felt'], "정답 ▶ felt\n이유: feel - felt - felt (불규칙). feel + 형용사 = ~하게 느끼다"),
  (L(S2, 4).replace('El took', 'El ___'), 'take', ['took'], "정답 ▶ took\n이유: take - took - taken (불규칙)"),
  (L(S2, 5).replace('It had', 'It ___'), 'have', ['had'], "정답 ▶ had\n이유: have - had - had"),
  (L(S2, 2).replace('reached', '___'), 'reach', ['reached'], "정답 ▶ reached\n이유: 규칙 변화 reach + -ed. reach for ~ = ~에 손을 뻗다"),
  (L(S1, 2).replace('even watered', 'even ___'), 'water', ['watered'], "정답 ▶ watered\n이유: water(물을 주다) + -ed → 과거형"),
  (L(S2, 13).replace('smiled', '___'), 'smile', ['smiled'], "정답 ▶ smiled\n이유: e로 끝나는 동사는 -d만 붙여요 (smile → smiled)"),
 ],
 error=[
  ("Jo was [[more tall]] than El, so Jo [[could]] water the plants [[alone]].", 0, 'taller',
   "틀린 곳 ▶ ① more tall → taller\n이유: 짧은 형용사의 비교급은 -er (tall - taller - tallest). more는 긴 형용사에 (more beautiful)\n나머지 ▶ ② could + 동사원형 ✔ ③ alone ✔"),
  ("They took all the [[pot]] with [[colorful]] flowers. El [[took]] the last pot.", 0, 'pots',
   "틀린 곳 ▶ ① pot → pots\n이유: all the + 복수 명사 (모든 ~들)\n나머지 ▶ ② colorful(형용사) ✔ ③ took(take의 과거) ✔"),
  ("It [[had]] the [[small]] plant with [[no]] flowers.", 1, 'smallest',
   "틀린 곳 ▶ ② small → smallest\n이유: the + 최상급 → the smallest (가장 작은)\n나머지 ▶ ① had ✔ ③ with no flowers(꽃이 없는) ✔"),
  ("\"But [[it's]] just a little green plant,\" said El. She [[were]] not so [[sure]].", 1, 'was',
   "틀린 곳 ▶ ② were → was\n이유: 주어 She(단수) → was\n나머지 ▶ ① it's = it is ✔ ③ sure(형용사, 확신하는) ✔"),
  ("[[They]] [[was]] always [[together]].", 1, 'were',
   "틀린 곳 ▶ ② was → were\n이유: They(복수) → were\n나머지 ▶ ① They(= El and Jo) ✔ ③ together ✔"),
 ],
 scr=[(L(S1, 6), S1[6][1]), (L(S1, 2), S1[2][1]), (L(S2, 1), S2[1][1]), (L(S2, 2), S2[2][1]), (L(S2, 3), S2[3][1]), (L(S2, 9), S2[9][1])],
 order=[
  ([L(S1, 0), L(S1, 1), L(S1, 2), L(S1, 3)], ["반에서 가장 작은 El과 Jo", "늘 함께였음", "물도 함께 줌", "봄에 무언가 달라짐"]),
  ([L(S2, 1), L(S2, 2), L(S2, 3), L(S2, 4)], ["모두 창문으로 달려감", "친구들이 El 너머로 손을 뻗음", "꽃이 있는 화분을 다 가져감", "El은 마지막 화분"]),
  ([L(S2, 8), L(S2, 9), L(S2, 10), L(S2, 11)], ["그냥 작은 초록 식물일 뿐", "El은 확신하지 못함", "Jo: 내 백일홍 가져", "El: 나란히 심을게"]),
 ],
 insert=[
  ([L(S1, 3), L(S1, 4), L(S1, 5)], 1, ["봄에 무언가 달라짐", "Jo의 키가 커졌음!", "Jo가 El보다 커서 혼자 물을 줌"],
   "정답 ▶ ①\n이유: '무엇이 달라졌는지' → Jo가 컸다 → 그래서 혼자 물을 줄 수 있었다, 순서로 이어져요."),
  ([L(S2, 3), L(S2, 4), L(S2, 5)], 1, ["친구들이 꽃 화분을 다 가져감", "El은 마지막 화분을 가져감", "그것(It)에는 꽃 없는 가장 작은 식물"],
   "정답 ▶ ①\n이유: It은 El이 가져간 '마지막 화분'이에요. 그 화분을 먼저 말해야 It이 이어져요."),
  ([L(S2, 10), L(S2, 11), L(S2, 12)], 1, ["Jo: 내 백일홍 가져", "El: 과꽃과 백일홍을 나란히 심을게", "Jo: 그 둘(They)은 좋은 친구가 될 거야"],
   "정답 ▶ ①\n이유: They는 '나란히 심은 과꽃과 백일홍'이에요. 나란히 심겠다는 말이 바로 앞에 와야 해요."),
 ],
 odd=[
  ([L(S1, 1), L(S1, 2), "El and Jo never helped each other in class.", L(S1, 3)], 2,
   "정답 ▶ ③\n이유: 둘은 늘 함께였고 물도 함께 줬어요. '서로 돕지 않았다'는 반대예요."),
  ([L(S2, 2), L(S2, 3), "El took the pot with the most beautiful flowers.", L(S2, 4)], 2,
   "정답 ▶ ③\n이유: 친구들이 꽃 화분을 다 가져가서 El은 꽃 없는 마지막 화분을 가져갔어요."),
  ([L(S2, 11), L(S2, 12), "Jo didn't want El to have her zinnia.", L(S2, 13)], 2,
   "정답 ▶ ③\n이유: Jo가 먼저 백일홍을 가져가라고 했어요. 원하지 않았다는 건 반대예요."),
 ],
 blank=[
  (L(S1, 2).replace('the pots alone', 'the ____ alone'), ["pots", "window", "students", "door"], "정답 ▶ pots\n이유: 식물에 물을 주려면 '화분'에 손이 닿아야 해요. 키가 작아서 혼자서는 닿지 않았어요."),
  (L(S1, 5).replace('plants alone', 'plants ____'), ["alone", "together", "slowly", "never"], "정답 ▶ alone\n이유: 키가 커져서 이제 '혼자서' 물을 줄 수 있었어요. 전에는 함께(together) 줬죠."),
  (L(S2, 5).replace('with no', 'with ____'), ["no", "many", "colorful", "beautiful"], "정답 ▶ no\n이유: 다른 친구들이 꽃 화분을 다 가져가서 '꽃이 없는' 식물만 남았어요."),
 ],
 gram=[
  ("비교급·최상급이 바르게 짝지어지지 <b>않은</b> 것은?", ['big - biger - bigest', 'small - smaller - smallest', 'tall - taller - tallest', 'tiny - tinier - tiniest'],
   "정답 ▶ big - biger - bigest\n이유: '단모음 + 단자음'으로 끝나면 자음을 한 번 더 써요 → big - bigger - biggest\n포인트 ▶ y로 끝나면 y → i (tiny - tinier - tiniest)"),
  ("빈칸에 들어갈 수 <b>없는</b> 것은?<br><b>Jo is ______ taller than El.</b>", ['very', 'much', 'even', 'a lot'],
   "정답 ▶ very\n이유: 비교급을 강조할 때는 much, even, a lot, far (훨씬). very는 비교급 앞에 못 써요.\n예 ▶ much taller(○) / very taller(✘)"),
  ("밑줄 친 <b>so</b>의 뜻으로 알맞은 것은?<br><b>Jo was taller than El, <u>so</u> Jo could water the plants alone.</b>", ['그래서', '왜냐하면', '하지만', '그다음에'],
   "정답 ▶ 그래서\n이유: 콤마 뒤 so + 문장 = 그래서 (결과)"),
  ("밑줄 친 부분의 뜻으로 알맞은 것은?<br><b>It had the smallest plant <u>with no flowers</u>.</b>", ['꽃이 없는', '꽃과 함께', '꽃이 많은', '꽃을 가진'],
   "정답 ▶ 꽃이 없는\n이유: with no + 명사 = ~이 없는 (with = ~이 있는)"),
  ("밑줄 친 부분을 풀어 쓴 것은?<br><b>In time, <u>it'll</u> grow and have beautiful flowers.</b>", ['it will', 'it is', 'it was', 'it all'],
   "정답 ▶ it will\n이유: 'll = will (I'll = I will, they'll = they will). 앞으로 일어날 일"),
  ("밑줄 친 <b>They</b>가 가리키는 것은?<br><b>\"I'll plant my aster and your zinnia side by side.\" \"<u>They</u>'ll be good friends!\"</b>", ['El의 과꽃과 Jo의 백일홍', 'El과 Jo', '반 친구들', 'Diaz 선생님과 El'],
   "정답 ▶ El의 과꽃과 Jo의 백일홍\n이유: 나란히 심은 두 꽃이 'El과 Jo처럼(just like us)' 좋은 친구가 될 거라는 말이에요."),
  ("다음 질문에 알맞은 대답은?<br><b>Why did El and Jo water the plants together?</b>", ['Because they could not reach the pots alone.', 'Because Mr. Diaz told them to.', 'Because they had no water.', 'Because the plants were very big.'],
   "정답 ▶ Because they could not reach the pots alone.\n이유: Why ~? → Because ~. 키가 작아 혼자서는 화분에 닿지 않았어요."),
 ])

# ═════════════ 5과 본문 ❸ ═════════════
db = steps(
 vocab=[['plant', '심다; 식물', '❸'], ['garden', '정원', '❸'], ['growing season', '식물이 자라는 시기', '❸'], ['all summer long', '여름 내내', '❸'],
        ['care for', '~을 돌보다', '❸'], ['last', '마지막의', '❸'], ['run', '달리다 (run - ran - run)', '❸'], ['suddenly', '갑자기', '❸'],
        ['stop', '멈추다', '❸'], ['different', '달라진, 다른', '❸'], ['aster', '과꽃', '❸'], ['grow taller', '키가 더 크다', '❸'], ['too', '~도, 또한', '❸']],
 pickv=[
  (L(S3, 0).replace('planted', '{planted|picked}'), "정답 ▶ planted (심었다)\n오답 ▶ picked (꺾었다): 화분의 꽃들을 정원에 '심고' 여름 내내 돌봤어요."),
  (L(S3, 2).replace('cared for', '{cared for|looked for}'), "정답 ▶ cared for (돌보았다)\n오답 ▶ looked for (찾았다): 여름 내내 꽃들을 '돌봤어요'."),
  (L(S3, 4).replace('suddenly', '{suddenly|slowly}'), "정답 ▶ suddenly (갑자기)\n오답 ▶ slowly (천천히): 달려가다가 달라진 모습을 보고 '갑자기' 멈췄어요."),
  (L(S3, 6).replace('There were flowers', 'There were {flowers|no flowers}'), "정답 ▶ flowers\n이유: 무언가 달라졌다(DIFFERENT) → 꽃이 없던 과꽃에 '꽃이 피었어요'."),
 ],
 tf=[
  ["El planted the flowers at school.", False, "정답 ▶ F\n이유: 학교가 아니라 자기 집 정원(in her garden)에 심었어요.", '❸', "El planted the flowers in her garden"],
  ["El took care of the flowers all summer.", True, "정답 ▶ T\n이유: All summer long, she cared for them.\n어휘 ▶ take care of = care for", '❸', "All summer long, she cared for them"],
  ["Jo visited El on the first day of summer.", False, "정답 ▶ F\n이유: 여름의 첫날이 아니라 마지막 날(the last day)에 왔어요.", '❸', "On the last day of summer, Jo came to El's house"],
  ["The aster had flowers at the end of summer.", True, "정답 ▶ T\n이유: 여름 마지막 날 과꽃에 꽃이 피어 있었어요.", '❸', "There were flowers on the aster"],
 ],
 ilchi=[
  {'n': '❸', 'box': ['❸'], 'q': "글의 내용과 일치하지 <u>않는</u> 것은?",
   'opts': ["El stopped caring for the flowers in July.", "Jo came to El's house on the last day of summer.", "El and Jo ran to the garden.", "The aster had flowers.", "El grew taller, too."],
   'ex': "정답 ▶ El stopped caring for the flowers in July.\n이유: 여름 내내(All summer long) 돌봤어요. 7월에 그만두지 않았어요.",
   'per': [["El은 7월에 꽃 돌보기를 그만두었다.", "All summer long, she cared for them", "불일치 → 여름 내내"],
           ["Jo는 여름 마지막 날 El의 집에 왔다.", "On the last day of summer, Jo came to El's house", "일치"],
           ["El과 Jo는 정원으로 달려갔다.", "El and Jo ran to the garden", "일치"],
           ["과꽃에 꽃이 피었다.", "There were flowers on the aster", "일치"],
           ["El도 키가 더 컸다.", "El grew TALLER, TOO", "일치"]]},
 ],
 pickg=[
  (L(S3, 0).replace('El planted', 'El {planted|plants}'), "정답 ▶ planted\n이유: 지난 여름의 일 → 과거형 plant + -ed"),
  (L(S3, 2).replace('for them', 'for {them|it}'), "정답 ▶ them\n이유: 돌본 것은 the flowers(복수) → them"),
  (L(S3, 3).replace('Jo came', 'Jo {came|comes}'), "정답 ▶ came\n이유: come - came - come (불규칙). 지난 일 → 과거형"),
  (L(S3, 4).replace('suddenly stopped', 'suddenly {stopped|stoped}'), "정답 ▶ stopped\n이유: '단모음 + 단자음(stop)' → p를 한 번 더 쓰고 -ed"),
  (L(S3, 6).replace('There were', 'There {were|was}'), "정답 ▶ were\n이유: There + be동사 + 주어. 주어 flowers(복수) → were"),
 ],
 verb=[
  (L(S3, 4).replace('El and Jo ran', 'El and Jo ___'), 'run', ['ran'], "정답 ▶ ran\n이유: run - ran - run (불규칙)"),
  (L(S3, 6).replace('El grew', 'El ___'), 'grow', ['grew'], "정답 ▶ grew\n이유: grow - grew - grown (불규칙)"),
  (L(S3, 2).replace('cared', '___'), 'care', ['cared'], "정답 ▶ cared\n이유: e로 끝나는 동사 → -d만 (care → cared)"),
 ],
 error=[
  ("On the last day of summer, Jo [[come]] to El's [[house]]. El and Jo [[ran]] to the garden and suddenly stopped.", 0, 'came',
   "틀린 곳 ▶ ① come → came\n이유: 지난 일 → 과거형 came\n나머지 ▶ ② El's house(El의 집) ✔ ③ ran ✔"),
  ("El and Jo ran to the garden and [[sudden]] [[stopped]]. Something [[was]] DIFFERENT!", 0, 'suddenly',
   "틀린 곳 ▶ ① sudden → suddenly\n이유: 동사 stopped를 꾸미는 말 → 부사 suddenly(갑자기)\n나머지 ▶ ② stopped ✔ ③ was ✔"),
  ("[[There]] [[was]] flowers on the [[aster]] ... and El grew TALLER, TOO!", 1, 'were',
   "틀린 곳 ▶ ② was → were\n이유: 주어 flowers(복수) → There were\n나머지 ▶ ① There ✔ ③ aster ✔"),
 ],
 scr=[(L(S3, 0), S3[0][1]), (L(S3, 2), S3[2][1]), (L(S3, 4), S3[4][1])],
 order=[
  ([L(S3, 0), L(S3, 1), L(S3, 2), L(S3, 3)], ["정원에 꽃들을 심음", "자라는 시기였음", "여름 내내 돌봄", "여름 마지막 날 Jo가 옴"]),
  ([L(S3, 3), L(S3, 4), L(S3, 5), L(S3, 6)], ["Jo가 El의 집에 옴", "정원으로 달려가다 멈춤", "무언가 달라짐!", "과꽃에 꽃이, El도 키가 컸음"]),
 ],
 insert=[
  ([L(S3, 3), L(S3, 4), L(S3, 5)], 1, ["Jo가 El의 집에 옴", "둘이 정원으로 달려가다 갑자기 멈춤", "무언가 달라져 있었음!"],
   "정답 ▶ ①\n이유: '갑자기 멈춘' 이유가 '무언가가 달라져서'예요. 멈춘 다음 달라진 것을 알아차려요."),
  ([L(S3, 4), L(S3, 5), L(S3, 6)], 1, ["정원으로 달려가다 멈춤", "무언가 달라짐!", "과꽃에 꽃이 피고, El도 컸음"],
   "정답 ▶ ①\n이유: '무엇이 달라졌는지'를 마지막 문장이 보여 줘요. 그 앞에 '달라졌다'는 말이 와야 해요."),
 ],
 odd=[
  ([L(S3, 1), L(S3, 2), "El forgot to water the flowers all summer.", L(S3, 3)], 2,
   "정답 ▶ ③\n이유: 여름 내내 꽃을 돌봤다고 했어요. '물 주는 걸 잊었다'는 반대예요."),
 ],
 blank=[
  (L(S3, 2).replace('for them', 'for ____'), ["them", "it", "her", "us"], "정답 ▶ them\n이유: 돌본 것은 정원에 심은 꽃들(the flowers) → 복수 them"),
  (L(S3, 4).replace('suddenly stopped', 'suddenly ____'), ["stopped", "slept", "cried", "sang"], "정답 ▶ stopped\n이유: 달라진 모습에 놀라 '갑자기 멈췄어요'. 다음 문장이 Something was DIFFERENT!"),
 ],
 gram=[
  ("밑줄 친 <b>It</b>과 쓰임이 <b>같은</b> 것은?<br><b><u>It</u> was growing season.</b>", ['It is Monday today.', 'It is my bag.', 'I like it.', 'It is a cute cat.'],
   "정답 ▶ It is Monday today.\n이유: 계절·요일·날씨·시간을 말할 때 쓰는 비인칭 주어 it ('그것'으로 해석하지 않아요)\n오답 ▶ 나머지 it은 '그것'(가리키는 대상이 있음)"),
  ("밑줄 친 <b>them</b>이 가리키는 것은?<br><b>El planted the flowers in her garden. ... she cared for <u>them</u>.</b>", ['the flowers', 'El and Jo', 'the pots', 'her classmates'],
   "정답 ▶ the flowers\n이유: 정원에 심은 꽃들(복수)을 여름 내내 돌봤어요."),
  ("밑줄 친 <b>TOO</b>의 뜻으로 알맞은 것은?<br><b>There were flowers on the aster ... and El grew TALLER, <u>TOO</u>!</b>", ['~도 (또한)', '너무', '두 번', '~까지'],
   "정답 ▶ ~도 (또한)\n이유: 과꽃이 자라 꽃을 피웠고, El'도' 키가 컸어요. 문장 끝 too = ~도"),
 ])

SUMQ = '다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 알맞은 것은?'
def SUMSTEP(items):
    return {'type': 'mc', 'title': '요약문 완성', 'guide': '본문을 읽고 요약문의 빈칸 (A), (B)에 들어갈 말을 고르세요.',
            'items': [{'n': n, 'box': box, 'q': SUMQ + '<br><b>' + s + '</b>', 'opts': o, 'ex': x, 'ev': evl} for n, box, s, o, x, evl in items]}
da.append(SUMSTEP([
  ('❶', ['❶'], "El and Jo were the (A) ______ students in the class, but in the spring Jo grew (B) ______ than El.",
   ['(A) smallest – (B) taller', '(A) tallest – (B) taller', '(A) smallest – (B) smaller', '(A) tallest – (B) shorter', '(A) busiest – (B) older'],
   "정답 ▶ (A) smallest – (B) taller\n(A) 반에서 '가장 작은' 학생들 → smallest\n(B) 봄에 Jo가 El보다 '더 커짐' → taller\n오답 ▶ tallest(가장 큰)는 반대, smaller는 Jo가 아니라 El의 기분이에요.",
   ["El and Jo were the smallest students in the class", "Jo was taller than El"]),
  ('❷', ['❷'], "El took the last pot with a tiny plant, but Mr. Diaz said it would (A) ______ and have (B) ______ flowers.",
   ['(A) grow – (B) beautiful', '(A) die – (B) beautiful', '(A) grow – (B) no', '(A) die – (B) no', '(A) stop – (B) small'],
   "정답 ▶ (A) grow – (B) beautiful\n(A) 시간이 지나면 '자라서' → grow\n(B) '아름다운' 꽃을 피울 것 → beautiful\n오답 ▶ die(죽다)·stop(멈추다)·no(없는)는 선생님 말과 반대예요.",
   ["it'll grow and have beautiful flowers"]),
]))
db.append(SUMSTEP([
  ('❸', ['❸'], "After El cared for the plants all summer, the aster had (A) ______ and El grew (B) ______, too.",
   ['(A) flowers – (B) taller', '(A) flowers – (B) smaller', '(A) no flowers – (B) taller', '(A) no flowers – (B) smaller', '(A) leaves – (B) older'],
   "정답 ▶ (A) flowers – (B) taller\n(A) 과꽃에 '꽃이' 피었다 → flowers\n(B) El도 키가 '더 컸다' → taller\n오답 ▶ no flowers·smaller는 이야기 처음의 모습이에요.",
   ["There were flowers on the aster", "El grew TALLER, TOO"]),
  ('❸', ['❸'], "Like her aster, El (A) ______ during the growing season, so something was (B) ______ at the end of summer.",
   ['(A) grew – (B) different', '(A) grew – (B) the same', '(A) stopped – (B) different', '(A) stopped – (B) the same', '(A) slept – (B) wrong'],
   "정답 ▶ (A) grew – (B) different\n(A) 과꽃처럼 El도 '자랐다' → grew\n(B) 여름 끝에 무언가 '달라져' 있었다 → different\n오답 ▶ the same(똑같은)은 반대, stopped·slept는 관계없어요.",
   ["It was growing season", "Something was DIFFERENT"]),
]))

def P(n, rows): return [['', n, '']] + [['', a, b] for a, b in rows]
DA = {'id': 'L5a', 'name': 'DAY 3', 'range': '5과 본문 ❶❷', 'story': "Lesson 5 · 가장 작은 El과 Jo · 학교 마지막 날, 꽃 없는 화분", 'passage': P('❶', S1) + P('❷', S2), 'steps': da}
DB = {'id': 'L5b', 'name': 'DAY 4', 'range': '5과 본문 ❸', 'story': "Lesson 5 · 여름 내내 자란 과꽃과 El", 'passage': P('❸', S3), 'steps': db}

path = '/home/claude/proj/data/m1-chunjae-so-L6.js'
PK = json.loads(subprocess.check_output(['node', '-e', "global.window={};require('%s');process.stdout.write(JSON.stringify(window.PKG))" % path]))
ids = [d['id'] for d in PK['days']]
assert ids == ['L4a', 'L4b', 'd1', 'd2'], ids
d4 = PK['days'][:2]; d6 = PK['days'][2:]
d6[0]['name'], d6[1]['name'] = 'DAY 5', 'DAY 6'
PK['days'] = d4 + [DA, DB] + d6
PK['unit'] = 'Lesson 4~6'
PK['title'] = 'My Delicious Summer Trip · Share Your Joys and Worries · Heroes in Nature'
PK['titleKo'] = '나의 맛있는 여름 여행 · 기쁨과 걱정 나누기 · 자연에서 일하는 즐거움'
write(PK, path, "/* 중1 천재(소영순) Lesson 4~6 (시험 범위 4·5·6과)\n"
      "   4과: gen_m1c4.py · 5과: gen_m1c5.py · 6과: 예전 파일(id d1, d2 유지 → 학생 기록 보존). 7과는 시험 범위가 아니라 뺌\n"
      "   prose: true → 본문을 대사가 아닌 설명문으로 표시 */\n")
print('ok', [(d['id'], d['name'], d['range'], len(d['steps'])) for d in PK['days']])
