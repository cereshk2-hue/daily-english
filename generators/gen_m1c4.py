import sys, json, subprocess
sys.path.insert(0, '/tmp/claude-0/-home-claude/a9e3e882-1f02-5d62-8f70-aced81bc59d2/scratchpad')
from gencommon import *

# 중1 천재(소영순) Lesson 4 · My Delicious Summer Trip (본문: My Korean Food Diary)
S1 = [("During the summer vacation, William traveled around Korea with his family.", "여름 방학 동안, William은 가족과 함께 한국 여기저기를 여행했다."),
      ("This is his food diary.", "이것은 그의 음식 일기이다."),
      ("July 25", "7월 25일"),
      ("We went to Damyang and visited Jungnogwon, a famous bamboo garden.", "우리는 담양에 갔고 유명한 대나무 정원인 죽녹원을 방문했다."),
      ("We enjoyed walking in the garden.", "우리는 정원에서 걷는 것을 즐겼다."),
      ("After we looked around, we ate two local dishes, daetongbap and tteokgalbi.", "주변을 둘러본 후에, 우리는 두 가지 지역 음식인 대통밥과 떡갈비를 먹었다."),
      ("Daetongbap is rice in a bamboo bowl.", "대통밥은 대나무 그릇에 담긴 밥이다."),
      ("I loved its unique bamboo smell.", "나는 그것의 독특한 대나무 향이 정말 좋았다."),
      ("Tteokgalbi, a Korean beef dish, was soft and sweet.", "한국의 소고기 요리인 떡갈비는 부드럽고 달콤했다."),
      ("The dishes really went well together.", "그 요리들은 함께 정말 잘 어울렸다.")]
S2 = [("July 30", "7월 30일"),
      ("We visited Tongyeong and went up the mountain by cable car.", "우리는 통영을 방문했고 케이블카를 타고 산에 올라갔다."),
      ("Seeing the blue ocean and the green islands was fantastic!", "파란 바다와 초록 섬들을 보는 것은 환상적이었다!"),
      ("Near the sea, we found a local restaurant and ate chungmugimbap.", "바다 근처에서 우리는 현지 식당을 찾았고 충무김밥을 먹었다."),
      ("It wasn't like other types of gimbap.", "그것은 다른 종류의 김밥과 달랐다."),
      ("There was only rice inside the seaweed.", "김 안에는 오직 밥만 있었다."),
      ("Kimchi and spicy squid were on the side.", "김치와 매운 오징어는 옆에 있었다."),
      ("It was spicy but really delicious.", "그것은 매웠지만 정말 맛있었다."),
      ("I heard about the history of this food.", "나는 이 음식의 역사에 관해 들었다."),
      ("Chungmu is an old name for Tongyeong.", "충무는 통영의 옛 이름이다."),
      ("Long ago, fishermen in this town started to eat chungmugimbap because it did not go bad quickly.", "오래전에, 이 마을의 어부들은 그것이 빨리 상하지 않았기 때문에 충무김밥을 먹기 시작했다.")]
S3 = [("August 2", "8월 2일"),
      ("Jeju-do is a beautiful island in Korea.", "제주도는 한국의 아름다운 섬이다."),
      ("We went there on a very hot day, and we became tired.", "우리는 매우 더운 날 그곳에 갔고, 피곤해졌다."),
      ("However, we got our energy back thanks to dombegogi.", "하지만 우리는 돔베고기 덕분에 기운을 되찾았다."),
      ("It surprised me in two ways.", "그것은 두 가지 면에서 나를 놀라게 했다."),
      ("First, it was pork on a cutting board, not on a plate.", "첫째, 그것은 접시가 아닌 도마 위에 놓인 돼지고기였다."),
      ("Second, the meat was so soft!", "둘째, 고기가 정말 부드러웠다!"),
      ("I had it with a special fish sauce, and the sauce was great, too.", "나는 그것을 특별한 생선 소스와 함께 먹었는데, 그 소스도 훌륭했다."),
      ("Later, I learned about the meaning of dombe.", "나중에, 나는 돔베의 의미에 대해 배웠다."),
      ("It means a cutting board in Jeju's language.", "그것은 제주 말로 도마를 의미한다.")]
L = lambda S, i: S[i][0]

# ═════════════ 4과 본문 ❶❷ ═════════════
da = steps(
 vocab=[['during', '~ 동안', '❶'], ['vacation', '방학', '❶'], ['travel', '여행하다', '❶'], ['diary', '일기', '❶'], ['famous', '유명한', '❶'],
        ['bamboo', '대나무', '❶'], ['garden', '정원', '❶'], ['enjoy', '즐기다', '❶'], ['look around', '주변을 둘러보다', '❶'], ['local', '지역의, 현지의', '❶'],
        ['dish', '요리; 접시', '❶'], ['bowl', '(우묵한) 그릇', '❶'], ['unique', '독특한', '❶'], ['smell', '냄새, 향', '❶'], ['beef', '소고기', '❶'],
        ['soft', '부드러운', '❶'], ['sweet', '달콤한', '❶'], ['go well', '잘 어울리다', '❶'], ['together', '함께', '❶'], ['go up', '올라가다', '❷'],
        ['by cable car', '케이블카를 타고', '❷'], ['ocean', '바다', '❷'], ['island', '섬', '❷'], ['fantastic', '환상적인', '❷'], ['restaurant', '식당', '❷'],
        ['type', '종류', '❷'], ['inside', '~ 안에', '❷'], ['seaweed', '김, 해초', '❷'], ['spicy', '매운', '❷'], ['squid', '오징어', '❷'],
        ['on the side', '옆에, 곁들여', '❷'], ['delicious', '맛있는', '❷'], ['history', '역사', '❷'], ['fisherman', '어부 (복수 fishermen)', '❷'], ['go bad', '(음식이) 상하다', '❷']],
 pickv=[
  (L(S1, 3).replace('famous', '{famous|boring}'), "정답 ▶ famous (유명한)\n오답 ▶ boring (지루한): 일부러 찾아가 방문한 곳이고, 걷는 것을 즐겼어요. '유명한' 대나무 정원이에요."),
  (L(S1, 4).replace('walking', '{walking|sleeping}'), "정답 ▶ walking (걷기)\n오답 ▶ sleeping (자기): 정원에서 '걷는 것'을 즐겼어요. 바로 다음에 주변을 둘러봤다(looked around)고 나와요."),
  (L(S1, 7).replace('unique', '{unique|common}'), "정답 ▶ unique (독특한)\n오답 ▶ common (흔한): 대나무 그릇에 담긴 밥이라 '독특한' 대나무 향이 났어요."),
  (L(S1, 8).replace('soft and', '{soft|hard} and'), "정답 ▶ soft (부드러운)\n오답 ▶ hard (딱딱한): 떡갈비는 '부드럽고' 달콤했어요. soft ↔ hard 반대말로 외워 두세요."),
  (L(S1, 9).replace('went well', 'went {well|bad}'), "정답 ▶ well\n이유: go well = 잘 어울리다. 두 요리가 함께 '잘 어울렸다'\n오답 ▶ go bad = (음식이) 상하다 → ❷에 나오는 표현이에요. 헷갈리지 마세요!"),
  (L(S2, 1).replace('went up', 'went {up|down}'), "정답 ▶ up\n이유: 케이블카를 타고 산에 '올라가서(went up)' 파란 바다와 섬들을 내려다봤어요."),
  (L(S2, 3).replace('a local', 'a {local|foreign}'), "정답 ▶ local (현지의, 지역의)\n오답 ▶ foreign (외국의): 통영 바닷가의 '현지' 식당에서 충무김밥을 먹었어요."),
  (L(S2, 6).replace('spicy squid', '{spicy|sweet} squid'), "정답 ▶ spicy (매운)\n오답 ▶ sweet (달콤한): 바로 다음 문장이 'It was spicy but really delicious.'예요."),
  (L(S2, 10).replace('fishermen', '{fishermen|farmers}'), "정답 ▶ fishermen (어부들)\n오답 ▶ farmers (농부들): 바닷가 마을(통영)에서 배를 타고 일하는 '어부들'이 먹기 시작했어요."),
 ],
 tf=[
  ["William traveled around Korea with his friends.", False, "정답 ▶ F\n이유: 친구들이 아니라 가족과 함께(with his family) 여행했어요.", '❶', "William traveled around Korea with his family"],
  ["Jungnogwon is a famous bamboo garden.", True, "정답 ▶ T\n이유: Jungnogwon, a famous bamboo garden → 콤마 뒤 말이 죽녹원을 설명해요.", '❶', "Jungnogwon, a famous bamboo garden"],
  ["Tteokgalbi was hard and salty.", False, "정답 ▶ F\n이유: 떡갈비는 부드럽고 달콤했어요(soft and sweet).", '❶', "was soft and sweet"],
  ["Daetongbap is served in a bamboo bowl.", True, "정답 ▶ T\n이유: 대통밥은 대나무 그릇에 담긴 밥이에요.\n어휘 ▶ be served 차려지다", '❶', "Daetongbap is rice in a bamboo bowl"],
  ["William climbed the mountain on foot.", False, "정답 ▶ F\n이유: 걸어서가 아니라 케이블카를 타고(by cable car) 올라갔어요.\n어휘 ▶ on foot 걸어서", '❷', "went up the mountain by cable car"],
  ["Chungmugimbap had kimchi inside the seaweed.", False, "정답 ▶ F\n이유: 김 안에는 밥만 있었고, 김치와 오징어는 옆에(on the side) 있었어요.", '❷', "There was only rice inside the seaweed"],
  ["Tongyeong was once called Chungmu.", True, "정답 ▶ T\n이유: 충무는 통영의 옛 이름이에요.\n어휘 ▶ once 한때", '❷', "Chungmu is an old name for Tongyeong"],
  ["Fishermen liked chungmugimbap because it went bad quickly.", False, "정답 ▶ F\n이유: 빨리 상하지 '않아서(did not go bad quickly)' 먹었어요.", '❷', "because it did not go bad quickly"],
 ],
 ilchi=[
  {'n': '❶', 'box': ['❶'], 'q': "글의 내용과 일치하지 <u>않는</u> 것은?",
   'opts': ["William ate three local dishes in Damyang.", "William traveled with his family.", "Jungnogwon is a bamboo garden.", "William loved the smell of daetongbap.", "Tteokgalbi is a beef dish."],
   'ex': "정답 ▶ William ate three local dishes in Damyang.\n이유: 세 가지가 아니라 '두 가지(two local dishes)' 지역 음식, 대통밥과 떡갈비를 먹었어요.",
   'per': [["William은 담양에서 지역 음식 세 가지를 먹었다.", "we ate two local dishes, daetongbap and tteokgalbi", "불일치 → 두 가지"],
           ["William은 가족과 함께 여행했다.", "William traveled around Korea with his family", "일치"],
           ["죽녹원은 대나무 정원이다.", "Jungnogwon, a famous bamboo garden", "일치"],
           ["William은 대통밥의 향이 정말 좋았다.", "I loved its unique bamboo smell", "일치"],
           ["떡갈비는 소고기 요리이다.", "Tteokgalbi, a Korean beef dish", "일치"]]},
  {'n': '❷', 'box': ['❷'], 'q': "글의 내용과 <u>일치하는</u> 것은?",
   'opts': ["Chungmugimbap was spicy but delicious.", "William walked up the mountain.", "There was kimchi inside the seaweed.", "William didn't like chungmugimbap.", "Chungmugimbap goes bad very quickly."],
   'ex': "정답 ▶ Chungmugimbap was spicy but delicious.\n이유: It was spicy but really delicious. 매웠지만 정말 맛있었어요.",
   'per': [["충무김밥은 매웠지만 맛있었다.", "It was spicy but really delicious", "일치"],
           ["William은 걸어서 산에 올라갔다.", "went up the mountain by cable car", "불일치 → 케이블카"],
           ["김 안에 김치가 있었다.", "There was only rice inside the seaweed", "불일치 → 밥만"],
           ["William은 충무김밥을 좋아하지 않았다.", "It was spicy but really delicious", "불일치 → 맛있었음"],
           ["충무김밥은 아주 빨리 상한다.", "because it did not go bad quickly", "불일치 → 빨리 상하지 않음"]]},
 ],
 pickg=[
  (L(S1, 0).replace('traveled', '{traveled|travels}'), "정답 ▶ traveled\n이유: 지난 여름 방학에 한 일 → 과거형. travel + -ed"),
  (L(S1, 3).replace('visited', '{visited|visit}'), "정답 ▶ visited\n이유: went(과거)와 and로 이어진 병렬 → 둘 다 과거형"),
  (L(S1, 4).replace('walking', '{walking|to walk}'), "정답 ▶ walking\n이유: enjoy는 목적어로 동명사(-ing)만 써요. enjoy -ing = ~하는 것을 즐기다\n오답 ▶ to walk ✘"),
  (L(S1, 5).replace('we ate', 'we {ate|eated}'), "정답 ▶ ate\n이유: eat의 과거형은 불규칙 ate! (eat - ate - eaten)\n오답 ▶ eated라는 말은 없어요."),
  (L(S1, 7).replace('its', '{its|it\'s}'), "정답 ▶ its\n이유: '그것의' 향 → 소유격 its. it's는 it is의 줄임말이에요."),
  (L(S1, 8).replace(' was ', ' {was|were} '), "정답 ▶ was\n이유: 주어는 Tteokgalbi(단수). 콤마 사이 a Korean beef dish는 떡갈비를 설명하는 말(동격)이에요."),
  (L(S2, 2).replace('Seeing', '{Seeing|See}'), "정답 ▶ Seeing\n이유: '보는 것은'이 문장의 주어 → 동명사(-ing). 동사원형 See는 주어가 될 수 없어요."),
  (L(S2, 2).replace(' was ', ' {was|were} '), "정답 ▶ was\n이유: 동명사 주어(Seeing ~)는 단수 취급 → was. 바로 앞 islands(복수)에 속지 마세요!"),
  (L(S2, 5).replace('There was', 'There {was|were}'), "정답 ▶ was\n이유: There + be동사 + 주어. 주어 rice(쌀, 셀 수 없는 명사)는 단수 → was"),
  (L(S2, 10).replace('because it', '{because|because of} it'), "정답 ▶ because\n이유: 뒤에 '주어 + 동사(it did not go bad)'가 오면 because. because of 뒤에는 명사"),
 ],
 verb=[
  (L(S1, 3).replace('We went', 'We ___'), 'go', ['went'], "정답 ▶ went\n이유: go의 과거형은 불규칙 went (go - went - gone)"),
  (L(S1, 4).replace('walking', '___'), 'walk', ['walking'], "정답 ▶ walking\n이유: enjoy + 동명사(-ing)"),
  (L(S2, 1).replace('We visited', 'We ___'), 'visit', ['visited'], "정답 ▶ visited\n이유: 과거형 규칙 변화 visit + -ed"),
  (L(S2, 3).replace('we found', 'we ___'), 'find', ['found'], "정답 ▶ found\n이유: find의 과거형은 불규칙 found (find - found - found)"),
  (L(S2, 6).replace(' were ', ' ___ '), 'be', ['were'], "정답 ▶ were\n이유: 주어 Kimchi and spicy squid(두 가지 → 복수) + 과거 → were"),
  (L(S2, 8).replace('I heard', 'I ___'), 'hear', ['heard'], "정답 ▶ heard\n이유: hear의 과거형은 불규칙 heard (hear - heard - heard)"),
  (L(S2, 10).replace('started to eat', 'started ___'), 'eat', ['to eat', 'eating'], "정답 ▶ to eat (또는 eating)\n이유: start + to부정사/동명사 = ~하기 시작하다. 본문은 to eat"),
  (L(S1, 9).replace('went well', '___ well'), 'go', ['went'], "정답 ▶ went\n이유: go well(잘 어울리다)의 과거 → went well"),
 ],
 error=[
  ("During the summer vacation, William [[travel]] around Korea [[with]] his [[family]].", 0, 'traveled',
   "틀린 곳 ▶ ① travel → traveled\n이유: 지난 방학에 한 일 → 과거형\n나머지 ▶ ② with(~와 함께) ✔ ③ his family ✔"),
  ("I loved [[it's]] unique bamboo [[smell]]. Tteokgalbi, a Korean beef dish, [[was]] soft and sweet.", 0, 'its',
   "틀린 곳 ▶ ① it's → its\n이유: '그것의' → 소유격 its. it's = it is\n나머지 ▶ ② smell(명사, 향) ✔ ③ was(Tteokgalbi 단수) ✔"),
  ("Near the sea, we [[finded]] a local restaurant and [[ate]] [[chungmugimbap]].", 0, 'found',
   "틀린 곳 ▶ ① finded → found\n이유: find는 불규칙 동사 (find - found - found)\n나머지 ▶ ② ate(eat의 과거) ✔"),
  ("There [[were]] only rice [[inside]] the [[seaweed]].", 0, 'was',
   "틀린 곳 ▶ ① were → was\n이유: rice(셀 수 없는 명사)는 단수 취급 → There was\n나머지 ▶ ② inside(~ 안에) ✔ ③ the seaweed ✔"),
  ("Long ago, fishermen in this town [[started]] to eat chungmugimbap [[because of]] it did not go bad [[quickly]].", 1, 'because',
   "틀린 곳 ▶ ② because of → because\n이유: 뒤에 '주어 + 동사(it did not go bad)' → because\n나머지 ▶ ① started ✔ ③ quickly(부사, 빨리) ✔"),
  ("Tteokgalbi, a Korean beef dish, was soft and sweet. The dishes [[really]] [[go]] well [[together]].", 1, 'went',
   "틀린 곳 ▶ ② go → went\n이유: 여행 일기 속 지난 일 → 과거형 went\n나머지 ▶ ① really(정말) ✔ ③ together(함께) ✔"),
 ],
 scr=[(L(S1, 4), S1[4][1]), (L(S1, 6), S1[6][1]), (L(S1, 7), S1[7][1]), (L(S2, 1), S2[1][1]), (L(S2, 5), S2[5][1]), (L(S2, 8), S2[8][1])],
 order=[
  ([L(S1, 3), L(S1, 4), L(S1, 5), L(S1, 6)], ["담양의 죽녹원 방문", "정원에서 걷기를 즐김", "둘러본 후 지역 음식 두 가지를 먹음", "대통밥 = 대나무 그릇의 밥"]),
  ([L(S2, 1), L(S2, 2), L(S2, 3), L(S2, 4)], ["케이블카로 산에 올라감", "바다와 섬을 보는 건 환상적", "현지 식당에서 충무김밥", "다른 김밥과 달랐음"]),
  ([L(S2, 7), L(S2, 8), L(S2, 9), L(S2, 10)], ["매웠지만 맛있었음", "이 음식의 역사를 들음", "충무 = 통영의 옛 이름", "어부들이 상하지 않아 먹기 시작"]),
 ],
 insert=[
  ([L(S1, 5), L(S1, 6), L(S1, 7)], 1, ["대통밥과 떡갈비를 먹음", "대통밥은 대나무 그릇에 담긴 밥", "나는 그것의(its) 대나무 향이 좋았음"],
   "정답 ▶ ①\n이유: '대나무 향'이 나는 이유가 '대나무 그릇에 담긴 밥'이기 때문이에요. its는 대통밥을 가리켜요."),
  ([L(S2, 4), L(S2, 5), L(S2, 6)], 1, ["다른 김밥과 달랐음", "김 안에는 밥만 있었음", "김치와 오징어는 옆에"],
   "정답 ▶ ①\n이유: '어떻게 달랐는지'를 설명하는 문장이에요. 안에는 밥만 → 반찬은 옆에, 순서로 이어져요."),
  ([L(S2, 8), L(S2, 9), L(S2, 10)], 1, ["이 음식의 역사를 들음", "충무는 통영의 옛 이름", "오래전 어부들이 먹기 시작함"],
   "정답 ▶ ①\n이유: 들은 역사의 내용이에요. 먼저 '충무'라는 이름을 설명하고, 어부들 이야기가 이어져요."),
 ],
 odd=[
  ([L(S1, 4), L(S1, 5), "William didn't eat anything in Damyang.", L(S1, 6)], 2,
   "정답 ▶ ③\n이유: 바로 앞에서 대통밥과 떡갈비를 먹었다고 했어요. '아무것도 먹지 않았다'는 정반대예요."),
  ([L(S2, 1), L(S2, 2), "It rained all day, so we couldn't see anything.", L(S2, 3)], 2,
   "정답 ▶ ③\n이유: 파란 바다와 초록 섬을 보는 게 환상적이었다고 했어요. '아무것도 못 봤다'는 흐름과 맞지 않아요."),
  ([L(S2, 5), L(S2, 6), "Chungmugimbap has a lot of meat inside.", L(S2, 7)], 2,
   "정답 ▶ ③\n이유: 김 안에는 '밥만' 있었다고 했어요. '안에 고기가 많다'는 내용과 반대예요."),
 ],
 blank=[
  (L(S1, 8).replace('beef', '____'), ["beef", "pork", "fish", "chicken"], "정답 ▶ beef\n이유: 떡갈비는 '소고기' 요리예요. pork(돼지고기)는 ❸의 돔베고기!"),
  (L(S2, 1).replace('cable car', '____'), ["cable car", "bike", "bus", "boat"], "정답 ▶ cable car\n이유: 산에 '케이블카를 타고' 올라갔어요. by + 교통수단 = ~을 타고"),
  (L(S2, 10).replace('go bad', 'go ____'), ["bad", "well", "up", "out"], "정답 ▶ bad\n이유: go bad = (음식이) 상하다. 빨리 상하지 않아서 바다에 나가는 어부들이 먹었어요."),
 ],
 gram=[
  ("다음 중 동사의 과거형이 <b>잘못된</b> 것은?", ['eat - eated', 'go - went', 'find - found', 'hear - heard'],
   "정답 ▶ eat - eated\n이유: eat의 과거형은 불규칙 ate예요. go-went, find-found, hear-heard도 모두 불규칙이니 함께 외워 두세요."),
  ("밑줄 친 부분과 같은 대상을 가리키는 것은?<br><b>We visited Jungnogwon, <u>a famous bamboo garden</u>.</b>", ['Jungnogwon', 'Damyang', 'William', 'daetongbap'],
   "정답 ▶ Jungnogwon\n이유: 콤마(,) 뒤 명사가 앞의 명사를 다시 설명해요(동격). 죽녹원 = 유명한 대나무 정원"),
  ("밑줄 친 <b>After</b>의 뜻으로 알맞은 것은?<br><b><u>After</u> we looked around, we ate two local dishes.</b>", ['~한 후에', '~하기 전에', '~하는 동안', '~ 때문에'],
   "정답 ▶ ~한 후에\n이유: after + 주어 + 동사 = ~한 후에. 둘러본 '후에' 먹었어요.\n비교 ▶ before ~하기 전에 / while ~하는 동안"),
  ("다음 문장의 뜻으로 알맞은 것은?<br><b>It wasn't like other types of gimbap.</b>", ['그것은 다른 종류의 김밥과 달랐다.', '그것은 다른 김밥을 좋아하지 않았다.', '그것은 다른 김밥보다 맛있었다.', '그것은 다른 종류의 김밥이었다.'],
   "정답 ▶ 그것은 다른 종류의 김밥과 달랐다.\n이유: be동사 뒤 like는 '좋아하다'가 아니라 '~와 같은'(전치사). wasn't like = ~와 같지 않았다"),
  ("빈칸에 공통으로 알맞은 것은?<br><b>We went up the mountain ___ cable car. / I go to school ___ bus.</b>", ['by', 'on', 'in', 'with'],
   "정답 ▶ by\n이유: by + 교통수단(관사 없이) = ~을 타고. by cable car, by bus, by subway"),
  ("밑줄 친 부분의 뜻으로 알맞은 것은?<br><b>It did not <u>go bad</u> quickly.</b>", ['(음식이) 상하다', '잘 어울리다', '멀리 가다', '맛있어지다'],
   "정답 ▶ (음식이) 상하다\n이유: go bad = 상하다\n비교 ▶ go well = 잘 어울리다 (❶)"),
  ("다음 질문에 대한 대답으로 알맞은 것은?<br><b>Why did fishermen eat chungmugimbap?</b>", ['Because it did not go bad quickly.', 'Because it was very cheap.', 'Because it had a lot of meat.', 'Because it was sweet.'],
   "정답 ▶ Because it did not go bad quickly.\n이유: Why ~? → Because ~로 대답. 빨리 상하지 않아서 바다에서 일하는 어부들에게 좋았어요."),
 ])

# ═════════════ 4과 본문 ❸ ═════════════
db = steps(
 vocab=[['island', '섬', '❸'], ['become', '~이 되다, ~해지다 (become-became-become)', '❸'], ['tired', '피곤한', '❸'], ['however', '하지만, 그러나', '❸'],
        ['energy', '기운, 에너지', '❸'], ['get back', '되찾다', '❸'], ['thanks to', '~ 덕분에', '❸'], ['surprise', '놀라게 하다', '❸'], ['way', '면, 방식', '❸'],
        ['first', '첫째로', '❸'], ['pork', '돼지고기', '❸'], ['cutting board', '도마', '❸'], ['plate', '접시', '❸'], ['second', '둘째로', '❸'],
        ['meat', '고기', '❸'], ['special', '특별한', '❸'], ['sauce', '소스', '❸'], ['later', '나중에', '❸'], ['learn', '배우다', '❸'],
        ['meaning', '의미', '❸'], ['mean', '의미하다', '❸'], ['language', '언어, 말', '❸']],
 pickv=[
  (L(S3, 2).replace('very hot', 'very {hot|cold}'), "정답 ▶ hot (더운)\n오답 ▶ cold (추운): 8월 여름날, '더워서' 피곤해졌어요."),
  (L(S3, 3).replace('thanks to', '{thanks to|instead of}'), "정답 ▶ thanks to (~ 덕분에)\n오답 ▶ instead of (~ 대신에): 돔베고기를 먹고 기운을 되찾았어요. 돔베고기 '덕분에'"),
  (L(S3, 5).replace('it was pork', 'it was {pork|beef}'), "정답 ▶ pork (돼지고기)\n오답 ▶ beef (소고기): 돔베고기는 '돼지고기'예요. 소고기는 ❶의 떡갈비!"),
  (L(S3, 6).replace('so soft', 'so {soft|hard}'), "정답 ▶ soft (부드러운)\n오답 ▶ hard (딱딱한): 놀란 두 번째 이유 → 고기가 아주 '부드러웠다'"),
  (L(S3, 7).replace('special fish', 'special {fish|fruit}'), "정답 ▶ fish (생선)\n오답 ▶ fruit (과일): 특별한 '생선' 소스와 함께 먹었어요."),
  (L(S3, 8).replace('the meaning', 'the {meaning|price}'), "정답 ▶ meaning (의미)\n오답 ▶ price (가격): 바로 다음 문장이 '그것은 제주 말로 도마를 의미한다(means)'예요."),
 ],
 tf=[
  ["William went to Jeju-do on a cold day.", False, "정답 ▶ F\n이유: 매우 더운 날(a very hot day)에 갔어요.", '❸', "on a very hot day"],
  ["William got tired on the hot day.", True, "정답 ▶ T\n이유: 더운 날이라 피곤해졌어요(became tired).\n어휘 ▶ get tired = become tired", '❸', "we became tired"],
  ["Dombegogi was served on a plate.", False, "정답 ▶ F\n이유: 접시가 아니라 도마 위에(on a cutting board, not on a plate) 나왔어요.", '❸', "it was pork on a cutting board, not on a plate"],
  ["William ate dombegogi with a special sauce.", True, "정답 ▶ T\n이유: 특별한 생선 소스와 함께 먹었어요.", '❸', "I had it with a special fish sauce"],
  ["In Jeju's language, dombe means a cutting board.", True, "정답 ▶ T\n이유: It means a cutting board in Jeju's language.", '❸', "It means a cutting board in Jeju's language"],
 ],
 ilchi=[
  {'n': '❸', 'box': ['❸'], 'q': "글의 내용과 일치하지 <u>않는</u> 것은?",
   'opts': ["The meat of dombegogi was hard.", "Jeju-do is an island in Korea.", "William got his energy back thanks to dombegogi.", "Dombegogi surprised William in two ways.", "William learned the meaning of dombe later."],
   'ex': "정답 ▶ The meat of dombegogi was hard.\n이유: 고기가 아주 부드러웠어요(so soft).",
   'per': [["돔베고기의 고기는 딱딱했다.", "the meat was so soft", "불일치 → 부드러움"],
           ["제주도는 한국의 섬이다.", "Jeju-do is a beautiful island in Korea", "일치"],
           ["William은 돔베고기 덕분에 기운을 되찾았다.", "we got our energy back thanks to dombegogi", "일치"],
           ["돔베고기는 두 가지 면에서 William을 놀라게 했다.", "It surprised me in two ways", "일치"],
           ["William은 나중에 돔베의 의미를 배웠다.", "Later, I learned about the meaning of dombe", "일치"]]},
 ],
 pickg=[
  (L(S3, 2).replace('we became', 'we {became|become}'), "정답 ▶ became\n이유: went(과거)와 and로 이어진 지난 일 → become의 과거형 became (불규칙)"),
  (L(S3, 2).replace('became tired', 'became {tired|tiredly}'), "정답 ▶ tired\n이유: become + 형용사 = ~해지다. 부사 tiredly는 올 수 없어요."),
  (L(S3, 4).replace('surprised me', 'surprised {me|I}'), "정답 ▶ me\n이유: surprised(놀라게 했다)의 목적어 자리 → 목적격 me"),
  (L(S3, 6).replace('so soft', '{so|such} soft'), "정답 ▶ so\n이유: so + 형용사 = 정말 ~한. such는 뒤에 (a) + 형용사 + 명사가 올 때 (such a soft meat)"),
  (L(S3, 7).replace('great, too', 'great, {too|either}'), "정답 ▶ too\n이유: 긍정문 끝 '~도' → too. either는 부정문 끝에 써요. (The sauce wasn't bad, either.)"),
  (L(S3, 9).replace('It means', 'It {means|mean}'), "정답 ▶ means\n이유: 주어 It(3인칭 단수) + 현재 → means. 지금도 그런 뜻이라 현재형이에요."),
 ],
 verb=[
  (L(S3, 2).replace('We went', 'We ___'), 'go', ['went'], "정답 ▶ went\n이유: go - went - gone (불규칙)"),
  (L(S3, 3).replace('we got', 'we ___'), 'get', ['got'], "정답 ▶ got\n이유: get - got - got(ten). get ~ back = ~을 되찾다"),
  (L(S3, 7).replace('I had', 'I ___'), 'have', ['had'], "정답 ▶ had\n이유: have(먹다)의 과거형 had"),
  (L(S3, 8).replace('I learned', 'I ___'), 'learn', ['learned', 'learnt'], "정답 ▶ learned\n이유: 규칙 변화 learn + -ed"),
 ],
 error=[
  ("We went there on a very hot day, and we [[become]] [[tired]]. However, we got our energy [[back]] thanks to dombegogi.", 0, 'became',
   "틀린 곳 ▶ ① become → became\n이유: 지난 일 → 과거형 became\n나머지 ▶ ② tired(become + 형용사) ✔ ③ get back(되찾다) ✔"),
  ("It surprised [[I]] in two [[ways]]. First, it [[was]] pork on a cutting board, not on a plate.", 0, 'me',
   "틀린 곳 ▶ ① I → me\n이유: 동사 surprised의 목적어 → 목적격 me\n나머지 ▶ ② ways(two 뒤 복수) ✔ ③ was ✔"),
  ("Later, I [[learned]] about the meaning of dombe. It [[mean]] a cutting board in Jeju's [[language]].", 1, 'means',
   "틀린 곳 ▶ ② mean → means\n이유: 주어 It(3인칭 단수) 현재 → means\n나머지 ▶ ① learned ✔ ③ language ✔"),
 ],
 scr=[(L(S3, 1), S3[1][1]), (L(S3, 4), S3[4][1]), (L(S3, 8), S3[8][1])],
 order=[
  ([L(S3, 1), L(S3, 2), L(S3, 3), L(S3, 4)], ["제주도는 아름다운 섬", "더운 날 가서 피곤해짐", "돔베고기 덕분에 기운을 되찾음", "두 가지 면에서 놀람"]),
  ([L(S3, 5), L(S3, 6), L(S3, 7), L(S3, 8)], ["첫째: 접시가 아닌 도마 위 돼지고기", "둘째: 고기가 아주 부드러움", "특별한 생선 소스도 훌륭", "나중에 돔베의 의미를 배움"]),
 ],
 insert=[
  ([L(S3, 4), L(S3, 5), L(S3, 6)], 1, ["두 가지 면에서 놀람", "첫째(First): 도마 위 돼지고기", "둘째(Second): 고기가 부드러움"],
   "정답 ▶ ①\n이유: two ways → First, Second 순서로 이어져요. Second 앞에는 First가 있어야 해요."),
  ([L(S3, 7), L(S3, 8), L(S3, 9)], 1, ["생선 소스도 훌륭했음", "나중에 돔베의 의미를 배움", "그것(It)은 도마를 의미함"],
   "정답 ▶ ①\n이유: It은 dombe를 가리켜요. '돔베의 의미'를 먼저 말해야 '그것은 도마를 의미한다'가 이어져요."),
 ],
 odd=[
  ([L(S3, 2), L(S3, 3), "We were too tired to eat anything.", L(S3, 4)], 2,
   "정답 ▶ ③\n이유: 바로 앞에서 돔베고기 덕분에 기운을 되찾았다고 했어요. '너무 피곤해 아무것도 못 먹었다'는 반대예요."),
  ([L(S3, 5), L(S3, 6), "The meat was too hard to chew.", L(S3, 7)], 2,
   "정답 ▶ ③\n이유: 고기가 아주 부드러웠다고 했어요. '너무 딱딱해 씹을 수 없었다'는 반대예요."),
 ],
 blank=[
  (L(S3, 3).replace('our energy', 'our ____'), ["energy", "money", "bag", "way"], "정답 ▶ energy\n이유: 더워서 피곤해졌다가 돔베고기 덕분에 '기운'을 되찾았어요."),
  (L(S3, 9).replace('a cutting board', 'a ____'), ["cutting board", "plate", "bowl", "pork"], "정답 ▶ cutting board\n이유: 고기가 도마 위에 나와서 이름이 '돔베(도마)'고기예요."),
 ],
 gram=[
  ("밑줄 친 부분의 뜻으로 알맞은 것은?<br><b>We got our energy back <u>thanks to</u> dombegogi.</b>", ['~ 덕분에', '~에게 감사하며', '~ 대신에', '~에도 불구하고'],
   "정답 ▶ ~ 덕분에\n이유: thanks to + 명사 = ~ 덕분에"),
  ("빈칸에 알맞은 것은?<br><b>I don't like spicy food. My brother doesn't like it, ______.</b>", ['either', 'too', 'so', 'also'],
   "정답 ▶ either\n이유: 부정문 끝 '~도' → either\n비교 ▶ 긍정문은 too (The sauce was great, too.)"),
  ("밑줄 친 <b>It</b>이 가리키는 것은?<br><b>Later, I learned about the meaning of dombe. <u>It</u> means a cutting board.</b>", ['dombe', 'dombegogi', 'the sauce', 'Jeju-do'],
   "정답 ▶ dombe\n이유: 바로 앞 문장의 '돔베'라는 말이 '도마'라는 뜻이에요."),
  ("다음 문장의 뜻으로 알맞은 것은?<br><b>It was pork on a cutting board, not on a plate.</b>", ['그것은 접시가 아니라 도마 위의 돼지고기였다.', '그것은 도마와 접시 위의 돼지고기였다.', '그것은 접시 위의 돼지고기였다.', '그것은 도마 위의 소고기였다.'],
   "정답 ▶ 그것은 접시가 아니라 도마 위의 돼지고기였다.\n이유: A, not B = B가 아니라 A"),
 ])

SUMQ = '다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 알맞은 것은?'
def SUMSTEP(items):
    return {'type': 'mc', 'title': '요약문 완성', 'guide': '본문을 읽고 요약문의 빈칸 (A), (B)에 들어갈 말을 고르세요.',
            'items': [{'n': n, 'box': box, 'q': SUMQ + '<br><b>' + s + '</b>', 'opts': o, 'ex': x, 'ev': evl} for n, box, s, o, x, evl in items]}
da.append(SUMSTEP([
  ('❶', ['❶'], "In Damyang, William visited a (A) ______ garden and ate two local dishes that went (B) ______ together.",
   ['(A) bamboo – (B) well', '(A) bamboo – (B) bad', '(A) flower – (B) well', '(A) flower – (B) bad', '(A) rice – (B) up'],
   "정답 ▶ (A) bamboo – (B) well\n(A) 죽녹원 = 유명한 '대나무' 정원 → bamboo\n(B) 두 요리가 함께 '잘' 어울렸다 → went well\n오답 ▶ flower(꽃) 정원이 아니고, go bad는 '상하다'라는 뜻이에요.",
   ["Jungnogwon, a famous bamboo garden", "The dishes really went well together"]),
  ('❷', ['❷'], "In Tongyeong, William ate chungmugimbap, which was (A) ______ but delicious, and it did not go bad (B) ______.",
   ['(A) spicy – (B) quickly', '(A) sweet – (B) quickly', '(A) spicy – (B) slowly', '(A) sweet – (B) slowly', '(A) soft – (B) easily'],
   "정답 ▶ (A) spicy – (B) quickly\n(A) 매웠지만 맛있었다 → spicy\n(B) 빨리 상하지 않았다 → quickly\n오답 ▶ sweet(달콤한)는 ❶의 떡갈비, slowly(천천히)는 반대 뜻이에요.",
   ["It was spicy but really delicious", "because it did not go bad quickly"]),
]))
db.append(SUMSTEP([
  ('❸', ['❸'], "On a hot day in Jeju-do, William got his (A) ______ back thanks to dombegogi, pork served on a cutting (B) ______.",
   ['(A) energy – (B) board', '(A) energy – (B) plate', '(A) money – (B) board', '(A) money – (B) plate', '(A) bag – (B) bowl'],
   "정답 ▶ (A) energy – (B) board\n(A) 피곤했다가 '기운'을 되찾음 → energy\n(B) 접시가 아니라 '도마(cutting board)' 위에 나옴 → board\n오답 ▶ plate(접시)는 아니라고 했고, money·bag은 관계없어요.",
   ["we got our energy back thanks to dombegogi", "it was pork on a cutting board, not on a plate"]),
  ('❸', ['❸'], "Dombegogi surprised William because the meat was very (A) ______ and the fish sauce was (B) ______, too.",
   ['(A) soft – (B) great', '(A) hard – (B) great', '(A) soft – (B) terrible', '(A) hard – (B) terrible', '(A) spicy – (B) sweet'],
   "정답 ▶ (A) soft – (B) great\n(A) 고기가 아주 '부드러웠다' → soft\n(B) 생선 소스도 '훌륭했다' → great\n오답 ▶ hard(딱딱한)·terrible(끔찍한)은 반대예요.",
   ["the meat was so soft", "the sauce was great, too"]),
]))

def P(n, rows): return [['', n, '']] + [['', a, b] for a, b in rows]
DA = {'id': 'L4a', 'name': 'DAY 1', 'range': '4과 본문 ❶❷', 'story': "Lesson 4 · 담양의 대나무 정원과 음식 · 통영의 충무김밥", 'passage': P('❶', S1) + P('❷', S2), 'steps': da}
DB = {'id': 'L4b', 'name': 'DAY 2', 'range': '4과 본문 ❸', 'story': "Lesson 4 · 제주도의 돔베고기", 'passage': P('❸', S3), 'steps': db}

path = '/home/claude/proj/data/m1-chunjae-so-L6.js'
PK = json.loads(subprocess.check_output(['node', '-e', "global.window={};require('%s');process.stdout.write(JSON.stringify(window.PKG))" % path]))
keep = [d for d in PK['days'] if d['id'] in ('d1', 'd2')]
assert len(keep) == 2 and keep[0]['range'].startswith('6과')
keep[0]['name'], keep[1]['name'] = 'DAY 3', 'DAY 4'
PK['days'] = [DA, DB] + keep
PK['unit'] = 'Lesson 4 · 6'
PK['title'] = 'My Delicious Summer Trip · Heroes in Nature'
PK['titleKo'] = '나의 맛있는 여름 여행 · 자연에서 일하는 즐거움'
write(PK, path, "/* 중1 천재(소영순) Lesson 4 · 6 (시험 범위 4·5·6과, 5과는 나중에 4과와 6과 사이에 넣기)\n"
      "   4과: scratchpad/gen_m1c4.py · 6과: 예전 파일 그대로(id d1, d2 유지 → 학생 기록 보존). 7과는 시험 범위가 아니라 뺌(예전 파일: scratchpad/m1-chunjae-so-L6.with7.js)\n"
      "   prose: true → 본문을 대사가 아닌 설명문으로 표시 */\n")
print('ok', [(d['id'], d['name'], d['range'], len(d['steps'])) for d in PK['days']])
