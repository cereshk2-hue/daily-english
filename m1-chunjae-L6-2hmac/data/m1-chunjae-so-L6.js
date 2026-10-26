/* 중1 천재(소영순) Lesson 4 · 6 (시험 범위 4·5·6과, 5과는 나중에 4과와 6과 사이에 넣기)
   4과: scratchpad/gen_m1c4.py · 6과: 예전 파일 그대로(id d1, d2 유지 → 학생 기록 보존). 7과는 시험 범위가 아니라 뺌(예전 파일: scratchpad/m1-chunjae-so-L6.with7.js)
   prose: true → 본문을 대사가 아닌 설명문으로 표시 */
window.PKG = {
  id: 'm1-chunjae-so-L6',
  school: '중1 천재(소영순)',
  unit: 'Lesson 4 · 6',
  title: 'My Delicious Summer Trip · Heroes in Nature',
  titleKo: '나의 맛있는 여름 여행 · 자연에서 일하는 즐거움',
  exam: '2학기 기말고사',
  prose: true,
  stepsBefore: ['핵심어휘·숙어', '어휘선택', 'T/F 내용 확인', '어법선택', '동사변형', '오류찾기', '본문 스크램블', '문장순서', '문장삽입', '어색한 문장', '빈칸추론', '핵심문법'],
  teacherPhone: '',
  days: [
  { id: 'L4a', name: 'DAY 1', range: '4과 본문 ❶❷', story: 'Lesson 4 · 담양의 대나무 정원과 음식 · 통영의 충무김밥', passage: [['', '❶', ''], ['', 'During the summer vacation, William traveled around Korea with his family.', '여름 방학 동안, William은 가족과 함께 한국 여기저기를 여행했다.'], ['', 'This is his food diary.', '이것은 그의 음식 일기이다.'], ['', 'July 25', '7월 25일'], ['', 'We went to Damyang and visited Jungnogwon, a famous bamboo garden.', '우리는 담양에 갔고 유명한 대나무 정원인 죽녹원을 방문했다.'], ['', 'We enjoyed walking in the garden.', '우리는 정원에서 걷는 것을 즐겼다.'], ['', 'After we looked around, we ate two local dishes, daetongbap and tteokgalbi.', '주변을 둘러본 후에, 우리는 두 가지 지역 음식인 대통밥과 떡갈비를 먹었다.'], ['', 'Daetongbap is rice in a bamboo bowl.', '대통밥은 대나무 그릇에 담긴 밥이다.'], ['', 'I loved its unique bamboo smell.', '나는 그것의 독특한 대나무 향이 정말 좋았다.'], ['', 'Tteokgalbi, a Korean beef dish, was soft and sweet.', '한국의 소고기 요리인 떡갈비는 부드럽고 달콤했다.'], ['', 'The dishes really went well together.', '그 요리들은 함께 정말 잘 어울렸다.'], ['', '❷', ''], ['', 'July 30', '7월 30일'], ['', 'We visited Tongyeong and went up the mountain by cable car.', '우리는 통영을 방문했고 케이블카를 타고 산에 올라갔다.'], ['', 'Seeing the blue ocean and the green islands was fantastic!', '파란 바다와 초록 섬들을 보는 것은 환상적이었다!'], ['', 'Near the sea, we found a local restaurant and ate chungmugimbap.', '바다 근처에서 우리는 현지 식당을 찾았고 충무김밥을 먹었다.'], ['', 'It wasn\'t like other types of gimbap.', '그것은 다른 종류의 김밥과 달랐다.'], ['', 'There was only rice inside the seaweed.', '김 안에는 오직 밥만 있었다.'], ['', 'Kimchi and spicy squid were on the side.', '김치와 매운 오징어는 옆에 있었다.'], ['', 'It was spicy but really delicious.', '그것은 매웠지만 정말 맛있었다.'], ['', 'I heard about the history of this food.', '나는 이 음식의 역사에 관해 들었다.'], ['', 'Chungmu is an old name for Tongyeong.', '충무는 통영의 옛 이름이다.'], ['', 'Long ago, fishermen in this town started to eat chungmugimbap because it did not go bad quickly.', '오래전에, 이 마을의 어부들은 그것이 빨리 상하지 않았기 때문에 충무김밥을 먹기 시작했다.']], steps: [
    { type: 'vocab', title: '핵심어휘·숙어', quizN: 15, items: [['during', '~ 동안', '❶'], ['vacation', '방학', '❶'], ['travel', '여행하다', '❶'], ['diary', '일기', '❶'], ['famous', '유명한', '❶'], ['bamboo', '대나무', '❶'], ['garden', '정원', '❶'], ['enjoy', '즐기다', '❶'], ['look around', '주변을 둘러보다', '❶'], ['local', '지역의, 현지의', '❶'], ['dish', '요리; 접시', '❶'], ['bowl', '(우묵한) 그릇', '❶'], ['unique', '독특한', '❶'], ['smell', '냄새, 향', '❶'], ['beef', '소고기', '❶'], ['soft', '부드러운', '❶'], ['sweet', '달콤한', '❶'], ['go well', '잘 어울리다', '❶'], ['together', '함께', '❶'], ['go up', '올라가다', '❷'], ['by cable car', '케이블카를 타고', '❷'], ['ocean', '바다', '❷'], ['island', '섬', '❷'], ['fantastic', '환상적인', '❷'], ['restaurant', '식당', '❷'], ['type', '종류', '❷'], ['inside', '~ 안에', '❷'], ['seaweed', '김, 해초', '❷'], ['spicy', '매운', '❷'], ['squid', '오징어', '❷'], ['on the side', '옆에, 곁들여', '❷'], ['delicious', '맛있는', '❷'], ['history', '역사', '❷'], ['fisherman', '어부 (복수 fishermen)', '❷'], ['go bad', '(음식이) 상하다', '❷']] },
    { type: 'pick', title: '어휘선택', guide: '문맥에 맞는 낱말을 고르세요.', items: [
      { s: 'We went to Damyang and visited Jungnogwon, a {famous|boring} bamboo garden.', ex: '정답 ▶ famous (유명한)\n오답 ▶ boring (지루한): 일부러 찾아가 방문한 곳이고, 걷는 것을 즐겼어요. \'유명한\' 대나무 정원이에요.' },
      { s: 'We enjoyed {walking|sleeping} in the garden.', ex: '정답 ▶ walking (걷기)\n오답 ▶ sleeping (자기): 정원에서 \'걷는 것\'을 즐겼어요. 바로 다음에 주변을 둘러봤다(looked around)고 나와요.' },
      { s: 'I loved its {unique|common} bamboo smell.', ex: '정답 ▶ unique (독특한)\n오답 ▶ common (흔한): 대나무 그릇에 담긴 밥이라 \'독특한\' 대나무 향이 났어요.' },
      { s: 'Tteokgalbi, a Korean beef dish, was {soft|hard} and sweet.', ex: '정답 ▶ soft (부드러운)\n오답 ▶ hard (딱딱한): 떡갈비는 \'부드럽고\' 달콤했어요. soft ↔ hard 반대말로 외워 두세요.' },
      { s: 'The dishes really went {well|bad} together.', ex: '정답 ▶ well\n이유: go well = 잘 어울리다. 두 요리가 함께 \'잘 어울렸다\'\n오답 ▶ go bad = (음식이) 상하다 → ❷에 나오는 표현이에요. 헷갈리지 마세요!' },
      { s: 'We visited Tongyeong and went {up|down} the mountain by cable car.', ex: '정답 ▶ up\n이유: 케이블카를 타고 산에 \'올라가서(went up)\' 파란 바다와 섬들을 내려다봤어요.' },
      { s: 'Near the sea, we found a {local|foreign} restaurant and ate chungmugimbap.', ex: '정답 ▶ local (현지의, 지역의)\n오답 ▶ foreign (외국의): 통영 바닷가의 \'현지\' 식당에서 충무김밥을 먹었어요.' },
      { s: 'Kimchi and {spicy|sweet} squid were on the side.', ex: '정답 ▶ spicy (매운)\n오답 ▶ sweet (달콤한): 바로 다음 문장이 \'It was spicy but really delicious.\'예요.' },
      { s: 'Long ago, {fishermen|farmers} in this town started to eat chungmugimbap because it did not go bad quickly.', ex: '정답 ▶ fishermen (어부들)\n오답 ▶ farmers (농부들): 바닷가 마을(통영)에서 배를 타고 일하는 \'어부들\'이 먹기 시작했어요.' }
    ] },
    { type: 'tf', title: 'T/F 내용 확인', guide: '본문 내용과 일치하면 T, 다르면 F를 고르세요.', items: [['William traveled around Korea with his friends.', false, '정답 ▶ F\n이유: 친구들이 아니라 가족과 함께(with his family) 여행했어요.', '❶', 'William traveled around Korea with his family'], ['Jungnogwon is a famous bamboo garden.', true, '정답 ▶ T\n이유: Jungnogwon, a famous bamboo garden → 콤마 뒤 말이 죽녹원을 설명해요.', '❶', 'Jungnogwon, a famous bamboo garden'], ['Tteokgalbi was hard and salty.', false, '정답 ▶ F\n이유: 떡갈비는 부드럽고 달콤했어요(soft and sweet).', '❶', 'was soft and sweet'], ['Daetongbap is served in a bamboo bowl.', true, '정답 ▶ T\n이유: 대통밥은 대나무 그릇에 담긴 밥이에요.\n어휘 ▶ be served 차려지다', '❶', 'Daetongbap is rice in a bamboo bowl'], ['William climbed the mountain on foot.', false, '정답 ▶ F\n이유: 걸어서가 아니라 케이블카를 타고(by cable car) 올라갔어요.\n어휘 ▶ on foot 걸어서', '❷', 'went up the mountain by cable car'], ['Chungmugimbap had kimchi inside the seaweed.', false, '정답 ▶ F\n이유: 김 안에는 밥만 있었고, 김치와 오징어는 옆에(on the side) 있었어요.', '❷', 'There was only rice inside the seaweed'], ['Tongyeong was once called Chungmu.', true, '정답 ▶ T\n이유: 충무는 통영의 옛 이름이에요.\n어휘 ▶ once 한때', '❷', 'Chungmu is an old name for Tongyeong'], ['Fishermen liked chungmugimbap because it went bad quickly.', false, '정답 ▶ F\n이유: 빨리 상하지 \'않아서(did not go bad quickly)\' 먹었어요.', '❷', 'because it did not go bad quickly']] },
    { type: 'mc', title: '일치·불일치', guide: '선택지는 본문을 어려운 어휘로 바꿔 쓴 문장이에요. 풀고 나서 해설의 어휘를 꼭 확인하세요.', items: [
      { n: '❶', box: ['❶'], q: '글의 내용과 일치하지 <u>않는</u> 것은?', opts: ['William ate three local dishes in Damyang.', 'William traveled with his family.', 'Jungnogwon is a bamboo garden.', 'William loved the smell of daetongbap.', 'Tteokgalbi is a beef dish.'], ex: '정답 ▶ William ate three local dishes in Damyang.\n이유: 세 가지가 아니라 \'두 가지(two local dishes)\' 지역 음식, 대통밥과 떡갈비를 먹었어요.', per: [['William은 담양에서 지역 음식 세 가지를 먹었다.', 'we ate two local dishes, daetongbap and tteokgalbi', '불일치 → 두 가지'], ['William은 가족과 함께 여행했다.', 'William traveled around Korea with his family', '일치'], ['죽녹원은 대나무 정원이다.', 'Jungnogwon, a famous bamboo garden', '일치'], ['William은 대통밥의 향이 정말 좋았다.', 'I loved its unique bamboo smell', '일치'], ['떡갈비는 소고기 요리이다.', 'Tteokgalbi, a Korean beef dish', '일치']] },
      { n: '❷', box: ['❷'], q: '글의 내용과 <u>일치하는</u> 것은?', opts: ['Chungmugimbap was spicy but delicious.', 'William walked up the mountain.', 'There was kimchi inside the seaweed.', 'William didn\'t like chungmugimbap.', 'Chungmugimbap goes bad very quickly.'], ex: '정답 ▶ Chungmugimbap was spicy but delicious.\n이유: It was spicy but really delicious. 매웠지만 정말 맛있었어요.', per: [['충무김밥은 매웠지만 맛있었다.', 'It was spicy but really delicious', '일치'], ['William은 걸어서 산에 올라갔다.', 'went up the mountain by cable car', '불일치 → 케이블카'], ['김 안에 김치가 있었다.', 'There was only rice inside the seaweed', '불일치 → 밥만'], ['William은 충무김밥을 좋아하지 않았다.', 'It was spicy but really delicious', '불일치 → 맛있었음'], ['충무김밥은 아주 빨리 상한다.', 'because it did not go bad quickly', '불일치 → 빨리 상하지 않음']] }
    ] },
    { type: 'pick', title: '어법선택', guide: '어법상 알맞은 것을 고르세요.', items: [
      { s: 'During the summer vacation, William {traveled|travels} around Korea with his family.', ex: '정답 ▶ traveled\n이유: 지난 여름 방학에 한 일 → 과거형. travel + -ed' },
      { s: 'We went to Damyang and {visited|visit} Jungnogwon, a famous bamboo garden.', ex: '정답 ▶ visited\n이유: went(과거)와 and로 이어진 병렬 → 둘 다 과거형' },
      { s: 'We enjoyed {walking|to walk} in the garden.', ex: '정답 ▶ walking\n이유: enjoy는 목적어로 동명사(-ing)만 써요. enjoy -ing = ~하는 것을 즐기다\n오답 ▶ to walk ✘' },
      { s: 'After we looked around, we {ate|eated} two local dishes, daetongbap and tteokgalbi.', ex: '정답 ▶ ate\n이유: eat의 과거형은 불규칙 ate! (eat - ate - eaten)\n오답 ▶ eated라는 말은 없어요.' },
      { s: 'I loved {its|it\'s} unique bamboo smell.', ex: '정답 ▶ its\n이유: \'그것의\' 향 → 소유격 its. it\'s는 it is의 줄임말이에요.' },
      { s: 'Tteokgalbi, a Korean beef dish, {was|were} soft and sweet.', ex: '정답 ▶ was\n이유: 주어는 Tteokgalbi(단수). 콤마 사이 a Korean beef dish는 떡갈비를 설명하는 말(동격)이에요.' },
      { s: '{Seeing|See} the blue ocean and the green islands was fantastic!', ex: '정답 ▶ Seeing\n이유: \'보는 것은\'이 문장의 주어 → 동명사(-ing). 동사원형 See는 주어가 될 수 없어요.' },
      { s: 'Seeing the blue ocean and the green islands {was|were} fantastic!', ex: '정답 ▶ was\n이유: 동명사 주어(Seeing ~)는 단수 취급 → was. 바로 앞 islands(복수)에 속지 마세요!' },
      { s: 'There {was|were} only rice inside the seaweed.', ex: '정답 ▶ was\n이유: There + be동사 + 주어. 주어 rice(쌀, 셀 수 없는 명사)는 단수 → was' },
      { s: 'Long ago, fishermen in this town started to eat chungmugimbap {because|because of} it did not go bad quickly.', ex: '정답 ▶ because\n이유: 뒤에 \'주어 + 동사(it did not go bad)\'가 오면 because. because of 뒤에는 명사' }
    ] },
    { type: 'verb', title: '동사변형', guide: '( ) 안의 동사를 알맞은 형태로 바꿔 쓰세요.', items: [
      { s: 'We ___ to Damyang and visited Jungnogwon, a famous bamboo garden.', v: 'go', a: ['went'], ex: '정답 ▶ went\n이유: go의 과거형은 불규칙 went (go - went - gone)' },
      { s: 'We enjoyed ___ in the garden.', v: 'walk', a: ['walking'], ex: '정답 ▶ walking\n이유: enjoy + 동명사(-ing)' },
      { s: 'We ___ Tongyeong and went up the mountain by cable car.', v: 'visit', a: ['visited'], ex: '정답 ▶ visited\n이유: 과거형 규칙 변화 visit + -ed' },
      { s: 'Near the sea, we ___ a local restaurant and ate chungmugimbap.', v: 'find', a: ['found'], ex: '정답 ▶ found\n이유: find의 과거형은 불규칙 found (find - found - found)' },
      { s: 'Kimchi and spicy squid ___ on the side.', v: 'be', a: ['were'], ex: '정답 ▶ were\n이유: 주어 Kimchi and spicy squid(두 가지 → 복수) + 과거 → were' },
      { s: 'I ___ about the history of this food.', v: 'hear', a: ['heard'], ex: '정답 ▶ heard\n이유: hear의 과거형은 불규칙 heard (hear - heard - heard)' },
      { s: 'Long ago, fishermen in this town started ___ chungmugimbap because it did not go bad quickly.', v: 'eat', a: ['to eat', 'eating'], ex: '정답 ▶ to eat (또는 eating)\n이유: start + to부정사/동명사 = ~하기 시작하다. 본문은 to eat' },
      { s: 'The dishes really ___ well together.', v: 'go', a: ['went'], ex: '정답 ▶ went\n이유: go well(잘 어울리다)의 과거 → went well' }
    ] },
    { type: 'error', title: '오류찾기', guide: '어법상 틀린 곳을 고르세요.', items: [
      { s: 'During the summer vacation, William [[travel]] around Korea [[with]] his [[family]].', w: 0, fix: 'traveled', ex: '틀린 곳 ▶ ① travel → traveled\n이유: 지난 방학에 한 일 → 과거형\n나머지 ▶ ② with(~와 함께) ✔ ③ his family ✔' },
      { s: 'I loved [[it\'s]] unique bamboo [[smell]]. Tteokgalbi, a Korean beef dish, [[was]] soft and sweet.', w: 0, fix: 'its', ex: '틀린 곳 ▶ ① it\'s → its\n이유: \'그것의\' → 소유격 its. it\'s = it is\n나머지 ▶ ② smell(명사, 향) ✔ ③ was(Tteokgalbi 단수) ✔' },
      { s: 'Near the sea, we [[finded]] a local restaurant and [[ate]] [[chungmugimbap]].', w: 0, fix: 'found', ex: '틀린 곳 ▶ ① finded → found\n이유: find는 불규칙 동사 (find - found - found)\n나머지 ▶ ② ate(eat의 과거) ✔' },
      { s: 'There [[were]] only rice [[inside]] the [[seaweed]].', w: 0, fix: 'was', ex: '틀린 곳 ▶ ① were → was\n이유: rice(셀 수 없는 명사)는 단수 취급 → There was\n나머지 ▶ ② inside(~ 안에) ✔ ③ the seaweed ✔' },
      { s: 'Long ago, fishermen in this town [[started]] to eat chungmugimbap [[because of]] it did not go bad [[quickly]].', w: 1, fix: 'because', ex: '틀린 곳 ▶ ② because of → because\n이유: 뒤에 \'주어 + 동사(it did not go bad)\' → because\n나머지 ▶ ① started ✔ ③ quickly(부사, 빨리) ✔' },
      { s: 'Tteokgalbi, a Korean beef dish, was soft and sweet. The dishes [[really]] [[go]] well [[together]].', w: 1, fix: 'went', ex: '틀린 곳 ▶ ② go → went\n이유: 여행 일기 속 지난 일 → 과거형 went\n나머지 ▶ ① really(정말) ✔ ③ together(함께) ✔' }
    ] },
    { type: 'scramble', title: '본문 스크램블', guide: '우리말에 맞게 단어를 눌러 문장을 완성하세요.', items: [
      { ko: '우리는 정원에서 걷는 것을 즐겼다.', en: 'We enjoyed walking in the garden.' },
      { ko: '대통밥은 대나무 그릇에 담긴 밥이다.', en: 'Daetongbap is rice in a bamboo bowl.' },
      { ko: '나는 그것의 독특한 대나무 향이 정말 좋았다.', en: 'I loved its unique bamboo smell.' },
      { ko: '우리는 통영을 방문했고 케이블카를 타고 산에 올라갔다.', en: 'We visited Tongyeong and went up the mountain by cable car.' },
      { ko: '김 안에는 오직 밥만 있었다.', en: 'There was only rice inside the seaweed.' },
      { ko: '나는 이 음식의 역사에 관해 들었다.', en: 'I heard about the history of this food.' }
    ] },
    { type: 'order', title: '문장순서', guide: '문장을 본문 순서대로 눌러서 배열하세요.', items: [
      { lines: ['We went to Damyang and visited Jungnogwon, a famous bamboo garden.', 'We enjoyed walking in the garden.', 'After we looked around, we ate two local dishes, daetongbap and tteokgalbi.', 'Daetongbap is rice in a bamboo bowl.'], flow: ['담양의 죽녹원 방문', '정원에서 걷기를 즐김', '둘러본 후 지역 음식 두 가지를 먹음', '대통밥 = 대나무 그릇의 밥'] },
      { lines: ['We visited Tongyeong and went up the mountain by cable car.', 'Seeing the blue ocean and the green islands was fantastic!', 'Near the sea, we found a local restaurant and ate chungmugimbap.', 'It wasn\'t like other types of gimbap.'], flow: ['케이블카로 산에 올라감', '바다와 섬을 보는 건 환상적', '현지 식당에서 충무김밥', '다른 김밥과 달랐음'] },
      { lines: ['It was spicy but really delicious.', 'I heard about the history of this food.', 'Chungmu is an old name for Tongyeong.', 'Long ago, fishermen in this town started to eat chungmugimbap because it did not go bad quickly.'], flow: ['매웠지만 맛있었음', '이 음식의 역사를 들음', '충무 = 통영의 옛 이름', '어부들이 상하지 않아 먹기 시작'] }
    ] },
    { type: 'insert', title: '문장삽입', guide: '주어진 문장이 들어가기에 가장 알맞은 곳을 고르세요.', items: [
      { lines: ['After we looked around, we ate two local dishes, daetongbap and tteokgalbi.', 'Daetongbap is rice in a bamboo bowl.', 'I loved its unique bamboo smell.'], given: 1, flow: ['대통밥과 떡갈비를 먹음', '대통밥은 대나무 그릇에 담긴 밥', '나는 그것의(its) 대나무 향이 좋았음'], ex: '정답 ▶ ①\n이유: \'대나무 향\'이 나는 이유가 \'대나무 그릇에 담긴 밥\'이기 때문이에요. its는 대통밥을 가리켜요.' },
      { lines: ['It wasn\'t like other types of gimbap.', 'There was only rice inside the seaweed.', 'Kimchi and spicy squid were on the side.'], given: 1, flow: ['다른 김밥과 달랐음', '김 안에는 밥만 있었음', '김치와 오징어는 옆에'], ex: '정답 ▶ ①\n이유: \'어떻게 달랐는지\'를 설명하는 문장이에요. 안에는 밥만 → 반찬은 옆에, 순서로 이어져요.' },
      { lines: ['I heard about the history of this food.', 'Chungmu is an old name for Tongyeong.', 'Long ago, fishermen in this town started to eat chungmugimbap because it did not go bad quickly.'], given: 1, flow: ['이 음식의 역사를 들음', '충무는 통영의 옛 이름', '오래전 어부들이 먹기 시작함'], ex: '정답 ▶ ①\n이유: 들은 역사의 내용이에요. 먼저 \'충무\'라는 이름을 설명하고, 어부들 이야기가 이어져요.' }
    ] },
    { type: 'odd', title: '어색한 문장', guide: '글의 흐름과 관계없는 문장을 고르세요.', items: [
      { lines: ['We enjoyed walking in the garden.', 'After we looked around, we ate two local dishes, daetongbap and tteokgalbi.', 'William didn\'t eat anything in Damyang.', 'Daetongbap is rice in a bamboo bowl.'], odd: 2, ex: '정답 ▶ ③\n이유: 바로 앞에서 대통밥과 떡갈비를 먹었다고 했어요. \'아무것도 먹지 않았다\'는 정반대예요.' },
      { lines: ['We visited Tongyeong and went up the mountain by cable car.', 'Seeing the blue ocean and the green islands was fantastic!', 'It rained all day, so we couldn\'t see anything.', 'Near the sea, we found a local restaurant and ate chungmugimbap.'], odd: 2, ex: '정답 ▶ ③\n이유: 파란 바다와 초록 섬을 보는 게 환상적이었다고 했어요. \'아무것도 못 봤다\'는 흐름과 맞지 않아요.' },
      { lines: ['There was only rice inside the seaweed.', 'Kimchi and spicy squid were on the side.', 'Chungmugimbap has a lot of meat inside.', 'It was spicy but really delicious.'], odd: 2, ex: '정답 ▶ ③\n이유: 김 안에는 \'밥만\' 있었다고 했어요. \'안에 고기가 많다\'는 내용과 반대예요.' }
    ] },
    { type: 'blank', title: '빈칸추론', guide: '빈칸에 들어갈 말로 가장 알맞은 것을 고르세요.', items: [
      { s: 'Tteokgalbi, a Korean ____ dish, was soft and sweet.', opts: ['beef', 'pork', 'fish', 'chicken'], ex: '정답 ▶ beef\n이유: 떡갈비는 \'소고기\' 요리예요. pork(돼지고기)는 ❸의 돔베고기!' },
      { s: 'We visited Tongyeong and went up the mountain by ____.', opts: ['cable car', 'bike', 'bus', 'boat'], ex: '정답 ▶ cable car\n이유: 산에 \'케이블카를 타고\' 올라갔어요. by + 교통수단 = ~을 타고' },
      { s: 'Long ago, fishermen in this town started to eat chungmugimbap because it did not go ____ quickly.', opts: ['bad', 'well', 'up', 'out'], ex: '정답 ▶ bad\n이유: go bad = (음식이) 상하다. 빨리 상하지 않아서 바다에 나가는 어부들이 먹었어요.' }
    ] },
    { type: 'mc', title: '핵심문법', guide: '알맞은 답을 고르세요.', items: [
      { q: '다음 중 동사의 과거형이 <b>잘못된</b> 것은?', opts: ['eat - eated', 'go - went', 'find - found', 'hear - heard'], ex: '정답 ▶ eat - eated\n이유: eat의 과거형은 불규칙 ate예요. go-went, find-found, hear-heard도 모두 불규칙이니 함께 외워 두세요.' },
      { q: '밑줄 친 부분과 같은 대상을 가리키는 것은?<br><b>We visited Jungnogwon, <u>a famous bamboo garden</u>.</b>', opts: ['Jungnogwon', 'Damyang', 'William', 'daetongbap'], ex: '정답 ▶ Jungnogwon\n이유: 콤마(,) 뒤 명사가 앞의 명사를 다시 설명해요(동격). 죽녹원 = 유명한 대나무 정원' },
      { q: '밑줄 친 <b>After</b>의 뜻으로 알맞은 것은?<br><b><u>After</u> we looked around, we ate two local dishes.</b>', opts: ['~한 후에', '~하기 전에', '~하는 동안', '~ 때문에'], ex: '정답 ▶ ~한 후에\n이유: after + 주어 + 동사 = ~한 후에. 둘러본 \'후에\' 먹었어요.\n비교 ▶ before ~하기 전에 / while ~하는 동안' },
      { q: '다음 문장의 뜻으로 알맞은 것은?<br><b>It wasn\'t like other types of gimbap.</b>', opts: ['그것은 다른 종류의 김밥과 달랐다.', '그것은 다른 김밥을 좋아하지 않았다.', '그것은 다른 김밥보다 맛있었다.', '그것은 다른 종류의 김밥이었다.'], ex: '정답 ▶ 그것은 다른 종류의 김밥과 달랐다.\n이유: be동사 뒤 like는 \'좋아하다\'가 아니라 \'~와 같은\'(전치사). wasn\'t like = ~와 같지 않았다' },
      { q: '빈칸에 공통으로 알맞은 것은?<br><b>We went up the mountain ___ cable car. / I go to school ___ bus.</b>', opts: ['by', 'on', 'in', 'with'], ex: '정답 ▶ by\n이유: by + 교통수단(관사 없이) = ~을 타고. by cable car, by bus, by subway' },
      { q: '밑줄 친 부분의 뜻으로 알맞은 것은?<br><b>It did not <u>go bad</u> quickly.</b>', opts: ['(음식이) 상하다', '잘 어울리다', '멀리 가다', '맛있어지다'], ex: '정답 ▶ (음식이) 상하다\n이유: go bad = 상하다\n비교 ▶ go well = 잘 어울리다 (❶)' },
      { q: '다음 질문에 대한 대답으로 알맞은 것은?<br><b>Why did fishermen eat chungmugimbap?</b>', opts: ['Because it did not go bad quickly.', 'Because it was very cheap.', 'Because it had a lot of meat.', 'Because it was sweet.'], ex: '정답 ▶ Because it did not go bad quickly.\n이유: Why ~? → Because ~로 대답. 빨리 상하지 않아서 바다에서 일하는 어부들에게 좋았어요.' }
    ] },
    { type: 'mc', title: '요약문 완성', guide: '본문을 읽고 요약문의 빈칸 (A), (B)에 들어갈 말을 고르세요.', items: [
      { n: '❶', box: ['❶'], q: '다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 알맞은 것은?<br><b>In Damyang, William visited a (A) ______ garden and ate two local dishes that went (B) ______ together.</b>', opts: ['(A) bamboo – (B) well', '(A) bamboo – (B) bad', '(A) flower – (B) well', '(A) flower – (B) bad', '(A) rice – (B) up'], ex: '정답 ▶ (A) bamboo – (B) well\n(A) 죽녹원 = 유명한 \'대나무\' 정원 → bamboo\n(B) 두 요리가 함께 \'잘\' 어울렸다 → went well\n오답 ▶ flower(꽃) 정원이 아니고, go bad는 \'상하다\'라는 뜻이에요.', ev: ['Jungnogwon, a famous bamboo garden', 'The dishes really went well together'] },
      { n: '❷', box: ['❷'], q: '다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 알맞은 것은?<br><b>In Tongyeong, William ate chungmugimbap, which was (A) ______ but delicious, and it did not go bad (B) ______.</b>', opts: ['(A) spicy – (B) quickly', '(A) sweet – (B) quickly', '(A) spicy – (B) slowly', '(A) sweet – (B) slowly', '(A) soft – (B) easily'], ex: '정답 ▶ (A) spicy – (B) quickly\n(A) 매웠지만 맛있었다 → spicy\n(B) 빨리 상하지 않았다 → quickly\n오답 ▶ sweet(달콤한)는 ❶의 떡갈비, slowly(천천히)는 반대 뜻이에요.', ev: ['It was spicy but really delicious', 'because it did not go bad quickly'] }
    ] }
  ] },
  { id: 'L4b', name: 'DAY 2', range: '4과 본문 ❸', story: 'Lesson 4 · 제주도의 돔베고기', passage: [['', '❸', ''], ['', 'August 2', '8월 2일'], ['', 'Jeju-do is a beautiful island in Korea.', '제주도는 한국의 아름다운 섬이다.'], ['', 'We went there on a very hot day, and we became tired.', '우리는 매우 더운 날 그곳에 갔고, 피곤해졌다.'], ['', 'However, we got our energy back thanks to dombegogi.', '하지만 우리는 돔베고기 덕분에 기운을 되찾았다.'], ['', 'It surprised me in two ways.', '그것은 두 가지 면에서 나를 놀라게 했다.'], ['', 'First, it was pork on a cutting board, not on a plate.', '첫째, 그것은 접시가 아닌 도마 위에 놓인 돼지고기였다.'], ['', 'Second, the meat was so soft!', '둘째, 고기가 정말 부드러웠다!'], ['', 'I had it with a special fish sauce, and the sauce was great, too.', '나는 그것을 특별한 생선 소스와 함께 먹었는데, 그 소스도 훌륭했다.'], ['', 'Later, I learned about the meaning of dombe.', '나중에, 나는 돔베의 의미에 대해 배웠다.'], ['', 'It means a cutting board in Jeju\'s language.', '그것은 제주 말로 도마를 의미한다.']], steps: [
    { type: 'vocab', title: '핵심어휘·숙어', quizN: 15, items: [['island', '섬', '❸'], ['become', '~이 되다, ~해지다 (become-became-become)', '❸'], ['tired', '피곤한', '❸'], ['however', '하지만, 그러나', '❸'], ['energy', '기운, 에너지', '❸'], ['get back', '되찾다', '❸'], ['thanks to', '~ 덕분에', '❸'], ['surprise', '놀라게 하다', '❸'], ['way', '면, 방식', '❸'], ['first', '첫째로', '❸'], ['pork', '돼지고기', '❸'], ['cutting board', '도마', '❸'], ['plate', '접시', '❸'], ['second', '둘째로', '❸'], ['meat', '고기', '❸'], ['special', '특별한', '❸'], ['sauce', '소스', '❸'], ['later', '나중에', '❸'], ['learn', '배우다', '❸'], ['meaning', '의미', '❸'], ['mean', '의미하다', '❸'], ['language', '언어, 말', '❸']] },
    { type: 'pick', title: '어휘선택', guide: '문맥에 맞는 낱말을 고르세요.', items: [
      { s: 'We went there on a very {hot|cold} day, and we became tired.', ex: '정답 ▶ hot (더운)\n오답 ▶ cold (추운): 8월 여름날, \'더워서\' 피곤해졌어요.' },
      { s: 'However, we got our energy back {thanks to|instead of} dombegogi.', ex: '정답 ▶ thanks to (~ 덕분에)\n오답 ▶ instead of (~ 대신에): 돔베고기를 먹고 기운을 되찾았어요. 돔베고기 \'덕분에\'' },
      { s: 'First, it was {pork|beef} on a cutting board, not on a plate.', ex: '정답 ▶ pork (돼지고기)\n오답 ▶ beef (소고기): 돔베고기는 \'돼지고기\'예요. 소고기는 ❶의 떡갈비!' },
      { s: 'Second, the meat was so {soft|hard}!', ex: '정답 ▶ soft (부드러운)\n오답 ▶ hard (딱딱한): 놀란 두 번째 이유 → 고기가 아주 \'부드러웠다\'' },
      { s: 'I had it with a special {fish|fruit} sauce, and the sauce was great, too.', ex: '정답 ▶ fish (생선)\n오답 ▶ fruit (과일): 특별한 \'생선\' 소스와 함께 먹었어요.' },
      { s: 'Later, I learned about the {meaning|price} of dombe.', ex: '정답 ▶ meaning (의미)\n오답 ▶ price (가격): 바로 다음 문장이 \'그것은 제주 말로 도마를 의미한다(means)\'예요.' }
    ] },
    { type: 'tf', title: 'T/F 내용 확인', guide: '본문 내용과 일치하면 T, 다르면 F를 고르세요.', items: [['William went to Jeju-do on a cold day.', false, '정답 ▶ F\n이유: 매우 더운 날(a very hot day)에 갔어요.', '❸', 'on a very hot day'], ['William got tired on the hot day.', true, '정답 ▶ T\n이유: 더운 날이라 피곤해졌어요(became tired).\n어휘 ▶ get tired = become tired', '❸', 'we became tired'], ['Dombegogi was served on a plate.', false, '정답 ▶ F\n이유: 접시가 아니라 도마 위에(on a cutting board, not on a plate) 나왔어요.', '❸', 'it was pork on a cutting board, not on a plate'], ['William ate dombegogi with a special sauce.', true, '정답 ▶ T\n이유: 특별한 생선 소스와 함께 먹었어요.', '❸', 'I had it with a special fish sauce'], ['In Jeju\'s language, dombe means a cutting board.', true, '정답 ▶ T\n이유: It means a cutting board in Jeju\'s language.', '❸', 'It means a cutting board in Jeju\'s language']] },
    { type: 'mc', title: '일치·불일치', guide: '선택지는 본문을 어려운 어휘로 바꿔 쓴 문장이에요. 풀고 나서 해설의 어휘를 꼭 확인하세요.', items: [
      { n: '❸', box: ['❸'], q: '글의 내용과 일치하지 <u>않는</u> 것은?', opts: ['The meat of dombegogi was hard.', 'Jeju-do is an island in Korea.', 'William got his energy back thanks to dombegogi.', 'Dombegogi surprised William in two ways.', 'William learned the meaning of dombe later.'], ex: '정답 ▶ The meat of dombegogi was hard.\n이유: 고기가 아주 부드러웠어요(so soft).', per: [['돔베고기의 고기는 딱딱했다.', 'the meat was so soft', '불일치 → 부드러움'], ['제주도는 한국의 섬이다.', 'Jeju-do is a beautiful island in Korea', '일치'], ['William은 돔베고기 덕분에 기운을 되찾았다.', 'we got our energy back thanks to dombegogi', '일치'], ['돔베고기는 두 가지 면에서 William을 놀라게 했다.', 'It surprised me in two ways', '일치'], ['William은 나중에 돔베의 의미를 배웠다.', 'Later, I learned about the meaning of dombe', '일치']] }
    ] },
    { type: 'pick', title: '어법선택', guide: '어법상 알맞은 것을 고르세요.', items: [
      { s: 'We went there on a very hot day, and we {became|become} tired.', ex: '정답 ▶ became\n이유: went(과거)와 and로 이어진 지난 일 → become의 과거형 became (불규칙)' },
      { s: 'We went there on a very hot day, and we became {tired|tiredly}.', ex: '정답 ▶ tired\n이유: become + 형용사 = ~해지다. 부사 tiredly는 올 수 없어요.' },
      { s: 'It surprised {me|I} in two ways.', ex: '정답 ▶ me\n이유: surprised(놀라게 했다)의 목적어 자리 → 목적격 me' },
      { s: 'Second, the meat was {so|such} soft!', ex: '정답 ▶ so\n이유: so + 형용사 = 정말 ~한. such는 뒤에 (a) + 형용사 + 명사가 올 때 (such a soft meat)' },
      { s: 'I had it with a special fish sauce, and the sauce was great, {too|either}.', ex: '정답 ▶ too\n이유: 긍정문 끝 \'~도\' → too. either는 부정문 끝에 써요. (The sauce wasn\'t bad, either.)' },
      { s: 'It {means|mean} a cutting board in Jeju\'s language.', ex: '정답 ▶ means\n이유: 주어 It(3인칭 단수) + 현재 → means. 지금도 그런 뜻이라 현재형이에요.' }
    ] },
    { type: 'verb', title: '동사변형', guide: '( ) 안의 동사를 알맞은 형태로 바꿔 쓰세요.', items: [
      { s: 'We ___ there on a very hot day, and we became tired.', v: 'go', a: ['went'], ex: '정답 ▶ went\n이유: go - went - gone (불규칙)' },
      { s: 'However, we ___ our energy back thanks to dombegogi.', v: 'get', a: ['got'], ex: '정답 ▶ got\n이유: get - got - got(ten). get ~ back = ~을 되찾다' },
      { s: 'I ___ it with a special fish sauce, and the sauce was great, too.', v: 'have', a: ['had'], ex: '정답 ▶ had\n이유: have(먹다)의 과거형 had' },
      { s: 'Later, I ___ about the meaning of dombe.', v: 'learn', a: ['learned', 'learnt'], ex: '정답 ▶ learned\n이유: 규칙 변화 learn + -ed' }
    ] },
    { type: 'error', title: '오류찾기', guide: '어법상 틀린 곳을 고르세요.', items: [
      { s: 'We went there on a very hot day, and we [[become]] [[tired]]. However, we got our energy [[back]] thanks to dombegogi.', w: 0, fix: 'became', ex: '틀린 곳 ▶ ① become → became\n이유: 지난 일 → 과거형 became\n나머지 ▶ ② tired(become + 형용사) ✔ ③ get back(되찾다) ✔' },
      { s: 'It surprised [[I]] in two [[ways]]. First, it [[was]] pork on a cutting board, not on a plate.', w: 0, fix: 'me', ex: '틀린 곳 ▶ ① I → me\n이유: 동사 surprised의 목적어 → 목적격 me\n나머지 ▶ ② ways(two 뒤 복수) ✔ ③ was ✔' },
      { s: 'Later, I [[learned]] about the meaning of dombe. It [[mean]] a cutting board in Jeju\'s [[language]].', w: 1, fix: 'means', ex: '틀린 곳 ▶ ② mean → means\n이유: 주어 It(3인칭 단수) 현재 → means\n나머지 ▶ ① learned ✔ ③ language ✔' }
    ] },
    { type: 'scramble', title: '본문 스크램블', guide: '우리말에 맞게 단어를 눌러 문장을 완성하세요.', items: [
      { ko: '제주도는 한국의 아름다운 섬이다.', en: 'Jeju-do is a beautiful island in Korea.' },
      { ko: '그것은 두 가지 면에서 나를 놀라게 했다.', en: 'It surprised me in two ways.' },
      { ko: '나중에, 나는 돔베의 의미에 대해 배웠다.', en: 'Later, I learned about the meaning of dombe.' }
    ] },
    { type: 'order', title: '문장순서', guide: '문장을 본문 순서대로 눌러서 배열하세요.', items: [
      { lines: ['Jeju-do is a beautiful island in Korea.', 'We went there on a very hot day, and we became tired.', 'However, we got our energy back thanks to dombegogi.', 'It surprised me in two ways.'], flow: ['제주도는 아름다운 섬', '더운 날 가서 피곤해짐', '돔베고기 덕분에 기운을 되찾음', '두 가지 면에서 놀람'] },
      { lines: ['First, it was pork on a cutting board, not on a plate.', 'Second, the meat was so soft!', 'I had it with a special fish sauce, and the sauce was great, too.', 'Later, I learned about the meaning of dombe.'], flow: ['첫째: 접시가 아닌 도마 위 돼지고기', '둘째: 고기가 아주 부드러움', '특별한 생선 소스도 훌륭', '나중에 돔베의 의미를 배움'] }
    ] },
    { type: 'insert', title: '문장삽입', guide: '주어진 문장이 들어가기에 가장 알맞은 곳을 고르세요.', items: [
      { lines: ['It surprised me in two ways.', 'First, it was pork on a cutting board, not on a plate.', 'Second, the meat was so soft!'], given: 1, flow: ['두 가지 면에서 놀람', '첫째(First): 도마 위 돼지고기', '둘째(Second): 고기가 부드러움'], ex: '정답 ▶ ①\n이유: two ways → First, Second 순서로 이어져요. Second 앞에는 First가 있어야 해요.' },
      { lines: ['I had it with a special fish sauce, and the sauce was great, too.', 'Later, I learned about the meaning of dombe.', 'It means a cutting board in Jeju\'s language.'], given: 1, flow: ['생선 소스도 훌륭했음', '나중에 돔베의 의미를 배움', '그것(It)은 도마를 의미함'], ex: '정답 ▶ ①\n이유: It은 dombe를 가리켜요. \'돔베의 의미\'를 먼저 말해야 \'그것은 도마를 의미한다\'가 이어져요.' }
    ] },
    { type: 'odd', title: '어색한 문장', guide: '글의 흐름과 관계없는 문장을 고르세요.', items: [
      { lines: ['We went there on a very hot day, and we became tired.', 'However, we got our energy back thanks to dombegogi.', 'We were too tired to eat anything.', 'It surprised me in two ways.'], odd: 2, ex: '정답 ▶ ③\n이유: 바로 앞에서 돔베고기 덕분에 기운을 되찾았다고 했어요. \'너무 피곤해 아무것도 못 먹었다\'는 반대예요.' },
      { lines: ['First, it was pork on a cutting board, not on a plate.', 'Second, the meat was so soft!', 'The meat was too hard to chew.', 'I had it with a special fish sauce, and the sauce was great, too.'], odd: 2, ex: '정답 ▶ ③\n이유: 고기가 아주 부드러웠다고 했어요. \'너무 딱딱해 씹을 수 없었다\'는 반대예요.' }
    ] },
    { type: 'blank', title: '빈칸추론', guide: '빈칸에 들어갈 말로 가장 알맞은 것을 고르세요.', items: [
      { s: 'However, we got our ____ back thanks to dombegogi.', opts: ['energy', 'money', 'bag', 'way'], ex: '정답 ▶ energy\n이유: 더워서 피곤해졌다가 돔베고기 덕분에 \'기운\'을 되찾았어요.' },
      { s: 'It means a ____ in Jeju\'s language.', opts: ['cutting board', 'plate', 'bowl', 'pork'], ex: '정답 ▶ cutting board\n이유: 고기가 도마 위에 나와서 이름이 \'돔베(도마)\'고기예요.' }
    ] },
    { type: 'mc', title: '핵심문법', guide: '알맞은 답을 고르세요.', items: [
      { q: '밑줄 친 부분의 뜻으로 알맞은 것은?<br><b>We got our energy back <u>thanks to</u> dombegogi.</b>', opts: ['~ 덕분에', '~에게 감사하며', '~ 대신에', '~에도 불구하고'], ex: '정답 ▶ ~ 덕분에\n이유: thanks to + 명사 = ~ 덕분에' },
      { q: '빈칸에 알맞은 것은?<br><b>I don\'t like spicy food. My brother doesn\'t like it, ______.</b>', opts: ['either', 'too', 'so', 'also'], ex: '정답 ▶ either\n이유: 부정문 끝 \'~도\' → either\n비교 ▶ 긍정문은 too (The sauce was great, too.)' },
      { q: '밑줄 친 <b>It</b>이 가리키는 것은?<br><b>Later, I learned about the meaning of dombe. <u>It</u> means a cutting board.</b>', opts: ['dombe', 'dombegogi', 'the sauce', 'Jeju-do'], ex: '정답 ▶ dombe\n이유: 바로 앞 문장의 \'돔베\'라는 말이 \'도마\'라는 뜻이에요.' },
      { q: '다음 문장의 뜻으로 알맞은 것은?<br><b>It was pork on a cutting board, not on a plate.</b>', opts: ['그것은 접시가 아니라 도마 위의 돼지고기였다.', '그것은 도마와 접시 위의 돼지고기였다.', '그것은 접시 위의 돼지고기였다.', '그것은 도마 위의 소고기였다.'], ex: '정답 ▶ 그것은 접시가 아니라 도마 위의 돼지고기였다.\n이유: A, not B = B가 아니라 A' }
    ] },
    { type: 'mc', title: '요약문 완성', guide: '본문을 읽고 요약문의 빈칸 (A), (B)에 들어갈 말을 고르세요.', items: [
      { n: '❸', box: ['❸'], q: '다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 알맞은 것은?<br><b>On a hot day in Jeju-do, William got his (A) ______ back thanks to dombegogi, pork served on a cutting (B) ______.</b>', opts: ['(A) energy – (B) board', '(A) energy – (B) plate', '(A) money – (B) board', '(A) money – (B) plate', '(A) bag – (B) bowl'], ex: '정답 ▶ (A) energy – (B) board\n(A) 피곤했다가 \'기운\'을 되찾음 → energy\n(B) 접시가 아니라 \'도마(cutting board)\' 위에 나옴 → board\n오답 ▶ plate(접시)는 아니라고 했고, money·bag은 관계없어요.', ev: ['we got our energy back thanks to dombegogi', 'it was pork on a cutting board, not on a plate'] },
      { n: '❸', box: ['❸'], q: '다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 알맞은 것은?<br><b>Dombegogi surprised William because the meat was very (A) ______ and the fish sauce was (B) ______, too.</b>', opts: ['(A) soft – (B) great', '(A) hard – (B) great', '(A) soft – (B) terrible', '(A) hard – (B) terrible', '(A) spicy – (B) sweet'], ex: '정답 ▶ (A) soft – (B) great\n(A) 고기가 아주 \'부드러웠다\' → soft\n(B) 생선 소스도 \'훌륭했다\' → great\n오답 ▶ hard(딱딱한)·terrible(끔찍한)은 반대예요.', ev: ['the meat was so soft', 'the sauce was great, too'] }
    ] }
  ] },
  { id: 'd1', name: 'DAY 3', range: '6과 본문 ❶❷', story: '자연에서 일하는 사람들 · 거제의 해녀, 나리', passage: [['', '❶', ''], ['', 'Some people love to work in nature.', '어떤 사람들은 자연에서 일하는 것을 아주 좋아한다.'], ['', 'They work in the sea, mountains, or even in the Arctic.', '그들은 바다, 산, 심지어 북극에서도 일한다.'], ['', 'Let\'s meet them and listen to their stories.', '그들을 만나 보고 그들의 이야기를 들어 보자.'], ['', '❷', ''], ['Nari', 'I am Nari.', '저는 나리입니다.'], ['', 'I am a haenyeo in Geoje.', '저는 거제의 해녀입니다.'], ['', 'I dive in the water and collect seafood.', '저는 물에 잠수해서 해산물을 채집합니다.'], ['', 'In the morning, I check the tide and the weather.', '아침에, 저는 조수와 날씨를 확인합니다.'], ['', 'I wear a diving suit and swimming glasses to work in the water.', '저는 물속에서 일하기 위해 잠수복을 입고 수경을 씁니다.'], ['', 'I love diving and spending time in the beautiful sea.', '저는 잠수하는 것과 아름다운 바다에서 시간을 보내는 것을 아주 좋아합니다.'], ['', 'I don\'t collect too much seafood.', '저는 너무 많은 해산물을 채집하지 않습니다.'], ['', 'This is good for the ocean.', '이것이 바다에 좋습니다.'], ['', 'These days, I see a lot of trash in the water, so I pick up the trash.', '요즘은 물속에 쓰레기가 많이 보여서 쓰레기를 줍습니다.'], ['', 'I believe that we should care about the ocean.', '저는 우리가 바다에 신경을 써야 한다고 믿습니다.']], steps: [
    { type: 'vocab', title: '핵심어휘·숙어', quizN: 15, items: [['nature', '자연'], ['mountain', '산'], ['even', '심지어, ~조차'], ['Arctic', '북극; 북극의'], ['listen to', '~을 듣다'], ['story', '이야기'], ['haenyeo', '해녀'], ['dive', '잠수하다'], ['collect', '모으다, 채집하다'], ['seafood', '해산물'], ['check', '확인하다'], ['tide', '조수, 밀물과 썰물'], ['weather', '날씨'], ['wear', '입다, 쓰다, 착용하다'], ['diving suit', '잠수복'], ['swimming glasses', '수경'], ['spend time', '시간을 보내다'], ['too much', '너무 많은'], ['be good for', '~에 좋다'], ['ocean', '바다, 대양'], ['these days', '요즘'], ['a lot of', '많은'], ['trash', '쓰레기'], ['pick up', '~을 줍다'], ['believe', '믿다'], ['care about', '~에 신경 쓰다, 관심을 가지다']] },
    { type: 'pick', title: '어휘선택', guide: '문맥에 맞는 낱말을 고르세요.', items: [
      { s: 'Some people love to work in {nature|future}.', ex: 'nature: 자연' },
      { s: 'They work in the sea, mountains, or {even|ever} in the Arctic.', ex: 'even: 심지어 (ever: 언젠가, 한 번이라도)' },
      { s: 'Let\'s meet them and {listen|look} to their stories.', ex: 'listen to: ~을 듣다' },
      { s: 'I {dive|drive} in the water and collect seafood.', ex: 'dive: 잠수하다 (drive: 운전하다)' },
      { s: 'In the morning, I {check|change} the tide and the weather.', ex: 'check: 확인하다' },
      { s: 'I {wear|carry} a diving suit and swimming glasses to work in the water.', ex: 'wear: (옷·안경 등을) 입다, 쓰다' },
      { s: 'I don\'t collect too much seafood. This is {good|bad} for the ocean.', ex: '해산물을 너무 많이 채집하지 않는 것은 바다에 좋다.' },
      { s: 'These days, I see a lot of trash in the water, so I {pick up|throw away} the trash.', ex: 'pick up: 줍다 (throw away: 버리다)' },
      { s: 'I believe that we should {care about|forget about} the ocean.', ex: 'care about: ~에 신경 쓰다' }
    ] },
    { type: 'tf', title: 'T/F 내용 확인', guide: '본문 내용과 일치하면 T, 다르면 F를 고르세요.', items: [['Some people enjoy working in nature.', true, 'Some people love to work in nature.'], ['Nari is a haenyeo in Jeju.', false, '나리는 거제(Geoje)의 해녀다.'], ['Nari checks the tide and the weather in the morning.', true, 'In the morning, I check the tide and the weather.'], ['Nari wears a diving suit to work in the water.', true, '물속에서 일하기 위해 잠수복을 입는다.'], ['Nari collects as much seafood as she can.', false, '너무 많은 해산물을 채집하지 않는다.'], ['Nari sees a lot of trash in the water these days.', true, 'These days, I see a lot of trash in the water.'], ['Nari doesn\'t pick up the trash in the water.', false, '나리는 쓰레기를 줍는다(pick up the trash).'], ['Nari thinks we should care about the ocean.', true, 'I believe that we should care about the ocean.']] },
    { type: 'mc', title: '일치·불일치', guide: '본문을 읽고 내용과 맞는지 확인해요. 틀린 선택지는 해설의 근거 문장과 비교해 보세요.', items: [
      { n: '❷', box: ['❷'], q: '나리에 관한 내용과 일치하지 <u>않는</u> 것은?', opts: ['Nari collects as much seafood as she can.', 'Nari is a haenyeo in Geoje.', 'Nari checks the tide and the weather in the morning.', 'Nari wears a diving suit to work in the water.', 'Nari picks up the trash in the water.'], ex: '정답 근거: I don\'t collect too much seafood. (너무 많은 해산물을 채집하지 않는다)\n· as much ~ as she can : 할 수 있는 한 많이', per: [['나리는 할 수 있는 한 많은 해산물을 채집한다.', 'I don\'t collect too much seafood', '불일치 → 너무 많이 채집하지 않음'], ['나리는 거제의 해녀이다.', 'I am a haenyeo in Geoje', '일치'], ['나리는 아침에 조수와 날씨를 확인한다.', 'In the morning, I check the tide and the weather', '일치'], ['나리는 물속에서 일하기 위해 잠수복을 입는다.', 'I wear a diving suit', '일치'], ['나리는 물속의 쓰레기를 줍는다.', 'so I pick up the trash', '일치']] },
      { n: '❷', box: ['❶', '❷'], q: '글의 내용과 <u>일치하는</u> 것은?', opts: ['Nari thinks that we should care about the ocean.', 'Some people work in the Arctic, but not in the sea.', 'Nari dives in the water at night.', 'Nari doesn\'t like spending time in the sea.', 'There is no trash in the water these days.'], ex: '정답 근거: I believe that we should care about the ocean.\n· care about : ~에 신경 쓰다, 관심을 가지다', per: [['나리는 우리가 바다에 신경 써야 한다고 생각한다.', 'I believe that we should care about the ocean', '일치'], ['어떤 사람들은 북극에서 일하지만 바다에서는 일하지 않는다.', 'They work in the sea, mountains, or even in the Arctic', '불일치 → 바다에서도 일함'], ['나리는 밤에 물에 잠수한다.', 'In the morning, I check the tide', '불일치 → 밤이라는 말은 없음'], ['나리는 바다에서 시간 보내는 것을 좋아하지 않는다.', 'I love diving and spending time in the beautiful sea', '불일치 → 아주 좋아함'], ['요즘 물속에는 쓰레기가 없다.', 'I see a lot of trash in the water', '불일치 → 쓰레기가 많음']] }
    ] },
    { type: 'pick', title: '어법선택', guide: '어법상 알맞은 것을 고르세요.', items: [
      { s: 'Some people love {to work|work} in nature.', ex: 'love + to부정사/동명사' },
      { s: 'Let\'s meet them and {listen|listening} to their stories.', ex: 'Let\'s + 동사원형 (meet and listen 병렬)' },
      { s: 'I am a haenyeo {in|on} Geoje.', ex: '지역·도시 이름 앞 → in' },
      { s: 'I dive in the water and {collect|collects} seafood.', ex: '주어 I → collect (dive와 병렬)' },
      { s: 'I wear a diving suit and swimming glasses {to work|working} in the water.', ex: '목적(~하기 위해) → to부정사' },
      { s: 'I love diving and {spending|spend} time in the beautiful sea.', ex: 'diving과 and로 연결 → spending' },
      { s: 'I don\'t collect too {much|many} seafood.', ex: 'seafood는 셀 수 없는 명사 → much' },
      { s: 'These days, I see {a lot of|a few} trash in the water.', ex: 'trash는 셀 수 없는 명사 → a lot of (a few는 셀 수 있는 명사)' },
      { s: 'I believe {that|what} we should care about the ocean.', ex: '뒤에 완전한 문장 → 접속사 that' },
      { s: 'I believe that we should {care|cares} about the ocean.', ex: '조동사 should + 동사원형' }
    ] },
    { type: 'verb', title: '동사변형', guide: '( ) 안의 동사를 알맞은 형태로 바꿔 쓰세요.', items: [
      { s: 'Some people love ___ in nature.', v: 'work', a: ['to work', 'working'], ex: 'love + to부정사/동명사 (본문: to work)' },
      { s: 'They ___ in the sea, mountains, or even in the Arctic.', v: 'work', a: ['work'], ex: '주어 They → work' },
      { s: 'Let\'s ___ them and listen to their stories.', v: 'meet', a: ['meet'], ex: 'Let\'s + 동사원형' },
      { s: 'I ___ in the water and collect seafood.', v: 'dive', a: ['dive'], ex: '주어 I + 현재형' },
      { s: 'I wear a diving suit and swimming glasses ___ in the water.', v: 'work', a: ['to work'], ex: '목적(~하기 위해) → to work' },
      { s: 'I love ___ and spending time in the beautiful sea.', v: 'dive', a: ['diving'], ex: 'spending과 병렬 → diving' },
      { s: 'I love diving and ___ time in the beautiful sea.', v: 'spend', a: ['spending'], ex: 'diving과 병렬 → spending' },
      { s: 'I don\'t ___ too much seafood.', v: 'collect', a: ['collect'], ex: 'don\'t + 동사원형' },
      { s: 'This ___ good for the ocean.', v: 'be', a: ['is'], ex: '주어 This → is' },
      { s: 'I believe that we should ___ about the ocean.', v: 'care', a: ['care'], ex: 'should + 동사원형' }
    ] },
    { type: 'error', title: '오류찾기', guide: '어법상 틀린 곳을 고르세요.', items: [
      { s: 'Some people love [[work]] in nature. They [[work]] in the sea, mountains, or [[even]] [[in]] the Arctic.', w: 0, fix: 'to work', ex: 'love + to부정사/동명사 → to work (또는 working)' },
      { s: 'Let\'s [[meet]] them and [[listening]] [[to]] [[their]] stories.', w: 1, fix: 'listen', ex: 'Let\'s + 동사원형 → listen' },
      { s: 'I [[dive]] in the water and [[collects]] seafood. In the morning, I [[check]] the tide and [[the]] weather.', w: 1, fix: 'collect', ex: '주어 I → collect' },
      { s: 'I wear a diving suit and swimming glasses [[work]] [[in]] the water. I love [[diving]] and [[spending]] time in the beautiful sea.', w: 0, fix: 'to work', ex: '목적(~하기 위해) → to work' },
      { s: 'I [[don\'t]] collect too [[many]] seafood. This [[is]] good [[for]] the ocean.', w: 1, fix: 'much', ex: 'seafood는 셀 수 없는 명사 → much' },
      { s: 'These days, I see [[a lot of]] trash in the water, so I [[pick up]] the trash. I believe [[what]] we should [[care]] about the ocean.', w: 2, fix: 'that', ex: '뒤에 완전한 문장 → 접속사 that' }
    ] },
    { type: 'scramble', title: '본문 스크램블', guide: '우리말에 맞게 단어를 눌러 문장을 완성하세요.', items: [
      { ko: '어떤 사람들은 자연에서 일하는 것을 아주 좋아한다.', en: 'Some people love to work in nature.' },
      { ko: '그들을 만나 보고 그들의 이야기를 들어 보자.', en: 'Let\'s meet them and listen to their stories.' },
      { ko: '저는 물에 잠수해서 해산물을 채집합니다.', en: 'I dive in the water and collect seafood.' },
      { ko: '저는 물속에서 일하기 위해 잠수복을 입고 수경을 씁니다.', en: 'I wear a diving suit and swimming glasses to work in the water.' },
      { ko: '저는 잠수하는 것과 아름다운 바다에서 시간을 보내는 것을 아주 좋아합니다.', en: 'I love diving and spending time in the beautiful sea.' },
      { ko: '저는 너무 많은 해산물을 채집하지 않습니다.', en: 'I don\'t collect too much seafood.' },
      { ko: '저는 우리가 바다에 신경을 써야 한다고 믿습니다.', en: 'I believe that we should care about the ocean.' }
    ] },
    { type: 'order', title: '문장순서', guide: '문장을 본문 순서대로 눌러서 배열하세요.', items: [
      { lines: ['Some people love to work in nature.', 'They work in the sea, mountains, or even in the Arctic.', 'Let\'s meet them and listen to their stories.', 'I am Nari.'] },
      { lines: ['I dive in the water and collect seafood.', 'In the morning, I check the tide and the weather.', 'I wear a diving suit and swimming glasses to work in the water.', 'I love diving and spending time in the beautiful sea.'] },
      { lines: ['I don\'t collect too much seafood.', 'This is good for the ocean.', 'These days, I see a lot of trash in the water, so I pick up the trash.', 'I believe that we should care about the ocean.'] }
    ] },
    { type: 'insert', title: '문장삽입', guide: '주어진 문장이 들어가기에 가장 알맞은 곳을 고르세요.', items: [
      { lines: ['Some people love to work in nature.', 'They work in the sea, mountains, or even in the Arctic.', 'Let\'s meet them and listen to their stories.', 'I am Nari.', 'I am a haenyeo in Geoje.'], given: 1, ex: 'They는 앞 문장의 Some people을 가리킨다.' },
      { lines: ['I dive in the water and collect seafood.', 'In the morning, I check the tide and the weather.', 'I wear a diving suit and swimming glasses to work in the water.', 'I love diving and spending time in the beautiful sea.', 'I don\'t collect too much seafood.'], given: 2, ex: '아침에 조수와 날씨를 확인한 뒤, 물속에서 일하기 위해 잠수복을 입는다.' },
      { lines: ['I love diving and spending time in the beautiful sea.', 'I don\'t collect too much seafood.', 'This is good for the ocean.', 'These days, I see a lot of trash in the water, so I pick up the trash.', 'I believe that we should care about the ocean.'], given: 2, ex: 'This는 "해산물을 너무 많이 채집하지 않는 것"을 가리킨다.' }
    ] },
    { type: 'odd', title: '어색한 문장', guide: '글의 흐름과 관계없는 문장을 고르세요.', items: [
      { lines: ['Some people love to work in nature.', 'They work in the sea, mountains, or even in the Arctic.', 'They don\'t like going outside at all.', 'Let\'s meet them and listen to their stories.'], odd: 2, ex: '자연에서 일하는 것을 좋아하는 사람들인데 밖에 나가는 것을 싫어한다는 내용은 맞지 않는다.' },
      { lines: ['I dive in the water and collect seafood.', 'In the morning, I check the tide and the weather.', 'I wear a diving suit and swimming glasses to work in the water.', 'I am afraid of the sea, so I never swim.', 'I love diving and spending time in the beautiful sea.'], odd: 3, ex: '나리는 잠수와 바다에서 시간 보내기를 아주 좋아한다.' },
      { lines: ['I don\'t collect too much seafood.', 'This is good for the ocean.', 'So I always collect as much seafood as I can.', 'These days, I see a lot of trash in the water, so I pick up the trash.', 'I believe that we should care about the ocean.'], odd: 2, ex: '해산물을 너무 많이 채집하지 않는다는 앞 내용과 반대된다.' }
    ] },
    { type: 'blank', title: '빈칸추론', guide: '빈칸에 들어갈 말로 가장 알맞은 것을 고르세요.', items: [
      { s: 'I wear a diving suit and swimming glasses ____.', opts: ['to work in the water', 'to look nice', 'to sleep well', 'to go shopping'], ex: '물속에서 일하기 위해 잠수복과 수경을 착용한다.' },
      { s: 'I love diving and ____ in the beautiful sea.', opts: ['spending time', 'throwing trash', 'building houses', 'doing homework'], ex: '아름다운 바다에서 시간을 보내는 것을 좋아한다.' },
      { s: 'These days, I see a lot of trash in the water, so I ____.', opts: ['pick up the trash', 'throw more trash', 'stop diving', 'buy new glasses'], ex: '쓰레기가 많이 보여서 쓰레기를 줍는다.' },
      { s: 'I don\'t collect too much seafood. This is good for the ocean. I believe that we should ____ the ocean.', opts: ['care about', 'take everything from', 'get away from', 'be afraid of'], ex: '바다를 아끼는 행동을 하므로 바다에 신경 써야 한다고 믿는다.' }
    ] },
    { type: 'mc', title: '핵심문법', guide: '알맞은 답을 고르세요.', items: [
      { q: '빈칸에 들어갈 수 <b>없는</b> 것은?<br><b>I ______ to play soccer.</b>', opts: ['enjoy', 'like', 'love', 'start'], ex: 'enjoy는 동명사만 목적어로 쓴다 (enjoy playing). like·love·start는 둘 다 가능.' },
      { q: '다음 문장과 뜻이 같은 것은?<br><b>Some people love to work in nature.</b>', opts: ['Some people love working in nature.', 'Some people love work in nature.', 'Some people love worked in nature.', 'Some people loves to work in nature.'], ex: 'love + to부정사 = love + 동명사' },
      { q: '밑줄 친 부분과 쓰임이 같은 것은?<br><b>I wear a diving suit <u>to work</u> in the water.</b>', opts: ['She went to the library <u>to borrow</u> books.', 'I want <u>to work</u> in nature.', 'I love <u>to swim</u> in the sea.', 'He started <u>to read</u> the book.'], ex: '목적(~하기 위해)의 to부정사. 나머지는 동사의 목적어.' },
      { q: '"나는 책을 사기 위해 서점에 갔다."를 바르게 영작한 것은?', opts: ['I went to the bookstore to buy a book.', 'I went to the bookstore buy a book.', 'I went to the bookstore for buy a book.', 'I went to the bookstore buying a book.'], ex: '목적 → to + 동사원형' },
      { q: '빈칸에 공통으로 알맞은 것은?<br><b>I believe ______ we should care about the ocean.<br>I think ______ he is kind.</b>', opts: ['that', 'what', 'this', 'it'], ex: '완전한 문장을 이끄는 접속사 that (생략 가능)' },
      { q: '밑줄 친 <b>that</b>을 생략할 수 있는 것은?', opts: ['I know <u>that</u> she is honest.', '<u>That</u> bag is mine.', 'I like <u>that</u> song.', '<u>That</u> is my brother.'], ex: '동사의 목적어 자리 접속사 that은 생략할 수 있다. 나머지는 지시형용사·지시대명사.' },
      { q: '빈칸에 알맞은 것은?<br><b>I don\'t collect too ______ seafood.</b>', opts: ['much', 'many', 'a few', 'few'], ex: 'seafood는 셀 수 없는 명사 → much' },
      { q: '빈칸에 들어갈 수 <b>없는</b> 것은?<br><b>I see ______ trash in the water.</b>', opts: ['many', 'a lot of', 'lots of', 'much'], ex: 'trash는 셀 수 없는 명사 → many는 쓸 수 없다.' },
      { q: '빈칸에 알맞은 것은?<br><b>I love diving and ______ time in the sea.</b>', opts: ['spending', 'spend', 'spends', 'spent'], ex: 'diving과 and로 연결 → spending' }
    ] }
  ] },
  { id: 'd2', name: 'DAY 4', range: '6과 본문 ❸❹', story: '지리산의 수의사, 지한 · 극지 과학자, 은', passage: [['', '❸', ''], ['Jihan', 'My name is Jihan.', '제 이름은 지한입니다.'], ['', 'I am a vet at the wild animal care center in Jirisan.', '저는 지리산 야생 동물 보호 센터의 수의사입니다.'], ['', 'I take care of sick wild animals in the center and send them back to their homes.', '저는 센터의 아픈 야생 동물을 돌보고 그들을 집으로 돌려보냅니다.'], ['', 'Also, I often climb the mountain to look after wild animals like bears.', '또한 저는 곰과 같은 야생 동물을 돌보기 위해 자주 산을 오릅니다.'], ['', 'I\'m proud of my job.', '저는 제 직업이 자랑스럽습니다.'], ['', 'I think that protecting wild animals is important.', '저는 야생 동물을 보호하는 것이 중요하다고 생각합니다.'], ['', 'We should keep an eye on them and their homes to live together.', '우리는 함께 살아가기 위해 그들과 그들의 서식처를 계속 지켜보아야 합니다.'], ['', '❹', ''], ['Eun', 'My name is Eun, and I am an Arctic scientist.', '제 이름은 은이고, 저는 극지 과학자입니다.'], ['', 'I work at the Arctic Dasan Station in Norway.', '저는 노르웨이의 북극 다산 과학 기지에서 일합니다.'], ['', 'I study the soil, seawater, and ice in the Arctic.', '저는 북극의 토양, 바닷물, 얼음을 연구합니다.'], ['', 'I often travel on the special ship, Araon.', '저는 특별한 배인 아라온호를 타고 자주 이동합니다.'], ['', 'This ship is stronger than other ships.', '이 배는 다른 배보다 더 튼튼합니다.'], ['', 'It can break thick ice across the ocean.', '그것은 바다를 가로질러 두꺼운 얼음을 깰 수 있습니다.'], ['', 'Thanks to Araon, I can collect seawater samples.', '아라온호 덕분에 저는 바닷물 표본을 채집할 수 있습니다.'], ['', 'The Arctic Ocean has the answers to the climate crisis.', '북극해는 기후 위기에 대한 해답을 가지고 있습니다.'], ['', 'I hope that my work can help the Earth.', '저는 제 일이 지구를 도울 수 있기를 바랍니다.']], steps: [
    { type: 'vocab', title: '핵심어휘·숙어', quizN: 15, items: [['vet', '수의사'], ['wild animal', '야생 동물'], ['take care of', '~을 돌보다'], ['sick', '아픈'], ['send ~ back', '~을 돌려보내다'], ['often', '자주, 종종'], ['climb', '오르다'], ['look after', '~을 돌보다'], ['like (전치사)', '~와 같은, ~처럼'], ['bear', '곰'], ['be proud of', '~을 자랑스러워하다'], ['protect', '보호하다'], ['important', '중요한'], ['keep an eye on', '~을 계속 지켜보다'], ['together', '함께'], ['scientist', '과학자'], ['station', '기지; 역'], ['soil', '토양, 흙'], ['seawater', '바닷물'], ['travel', '이동하다; 여행하다'], ['special', '특별한'], ['strong', '튼튼한, 강한'], ['break', '깨다, 부수다'], ['thick', '두꺼운'], ['across', '~을 가로질러'], ['thanks to', '~ 덕분에'], ['sample', '표본, 샘플'], ['answer to', '~에 대한 해답'], ['climate crisis', '기후 위기'], ['hope', '바라다, 희망하다']] },
    { type: 'pick', title: '어휘선택', guide: '문맥에 맞는 낱말을 고르세요.', items: [
      { s: 'I am a {vet|chef} at the wild animal care center in Jirisan.', ex: 'vet: 수의사' },
      { s: 'I take care of {sick|healthy} wild animals in the center and send them back to their homes.', ex: '센터에서 아픈(sick) 동물을 돌본다.' },
      { s: 'Also, I often {climb|cross} the mountain to look after wild animals like bears.', ex: 'climb the mountain: 산을 오르다' },
      { s: 'I\'m {proud|afraid} of my job.', ex: 'be proud of: ~을 자랑스러워하다' },
      { s: 'I think that {protecting|hunting} wild animals is important.', ex: 'protect: 보호하다' },
      { s: 'We should keep an {eye|ear} on them and their homes to live together.', ex: 'keep an eye on: ~을 계속 지켜보다' },
      { s: 'I study the {soil|sand}, seawater, and ice in the Arctic.', ex: 'soil: 토양, 흙' },
      { s: 'This ship is {stronger|weaker} than other ships.', ex: '두꺼운 얼음을 깰 수 있으므로 더 튼튼하다.' },
      { s: 'It can break {thick|thin} ice across the ocean.', ex: 'thick: 두꺼운 (thin: 얇은)' },
      { s: '{Thanks to|Instead of} Araon, I can collect seawater samples.', ex: 'thanks to: ~ 덕분에' },
      { s: 'The Arctic Ocean has the {answers|questions} to the climate crisis.', ex: 'answer to: ~에 대한 해답' }
    ] },
    { type: 'tf', title: 'T/F 내용 확인', guide: '본문 내용과 일치하면 T, 다르면 F를 고르세요.', items: [['Jihan is a vet in Jirisan.', true, '지리산 야생 동물 보호 센터의 수의사다.'], ['Jihan sends the wild animals to a zoo.', false, '동물들을 그들의 집(서식처)으로 돌려보낸다.'], ['Jihan often climbs the mountain to look after wild animals.', true, 'I often climb the mountain to look after wild animals.'], ['Jihan thinks protecting wild animals isn\'t important.', false, '야생 동물 보호가 중요하다고 생각한다.'], ['Eun works at a station in Norway.', true, 'the Arctic Dasan Station in Norway'], ['Eun studies the soil, seawater, and ice in the Antarctic.', false, '남극(Antarctic)이 아니라 북극(Arctic)을 연구한다.'], ['Araon can break thick ice across the ocean.', true, 'It can break thick ice across the ocean.'], ['Eun hopes the work can help the Earth.', true, 'I hope that my work can help the Earth.']] },
    { type: 'mc', title: '일치·불일치', guide: '본문을 읽고 내용과 맞는지 확인해요. 틀린 선택지는 해설의 근거 문장과 비교해 보세요.', items: [
      { n: '❸', box: ['❸'], q: '지한에 관한 내용과 일치하지 <u>않는</u> 것은?', opts: ['Jihan works at a zoo in Seoul.', 'Jihan takes care of sick wild animals.', 'Jihan sends the animals back to their homes.', 'Jihan often climbs the mountain to look after bears.', 'Jihan is proud of his job.'], ex: '정답 근거: I am a vet at the wild animal care center in Jirisan.\n· vet : 수의사 · take care of = look after : 돌보다', per: [['지한은 서울의 동물원에서 일한다.', 'I am a vet at the wild animal care center in Jirisan', '불일치 → 지리산 야생 동물 보호 센터'], ['지한은 아픈 야생 동물을 돌본다.', 'I take care of sick wild animals', '일치'], ['지한은 동물들을 집으로 돌려보낸다.', 'send them back to their homes', '일치'], ['지한은 곰을 돌보기 위해 자주 산에 오른다.', 'I often climb the mountain to look after wild animals like bears', '일치'], ['지한은 자기 직업이 자랑스럽다.', 'I\'m proud of my job', '일치']] },
      { n: '❹', box: ['❹'], q: '은에 관한 내용과 <u>일치하는</u> 것은?', opts: ['The ship Araon can break thick ice across the ocean.', 'Eun works at a station in Canada.', 'Eun studies animals and plants in the Arctic.', 'Araon is weaker than other ships.', 'Eun can\'t collect seawater samples.'], ex: '정답 근거: It can break thick ice across the ocean.\n· thick : 두꺼운 · thanks to : ~ 덕분에 · sample : 표본', per: [['아라온호는 바다를 가로질러 두꺼운 얼음을 깰 수 있다.', 'It can break thick ice across the ocean', '일치'], ['은은 캐나다의 기지에서 일한다.', 'I work at the Arctic Dasan Station in Norway', '불일치 → 노르웨이'], ['은은 북극의 동물과 식물을 연구한다.', 'I study the soil, seawater, and ice in the Arctic', '불일치 → 토양, 바닷물, 얼음'], ['아라온호는 다른 배보다 약하다.', 'This ship is stronger than other ships', '불일치 → 더 튼튼함'], ['은은 바닷물 표본을 채집할 수 없다.', 'Thanks to Araon, I can collect seawater samples', '불일치 → 채집할 수 있음']] }
    ] },
    { type: 'pick', title: '어법선택', guide: '어법상 알맞은 것을 고르세요.', items: [
      { s: 'I am a vet {at|on} the wild animal care center in Jirisan.', ex: '건물·특정 장소 → at, 넓은 지역 → in' },
      { s: 'I take care of sick wild animals in the center and send {them back|back them} to their homes.', ex: '이어동사 목적어가 대명사 → 동사 + 대명사 + back' },
      { s: 'Also, I often climb the mountain {to look|looking} after wild animals like bears.', ex: '목적(~하기 위해) → to부정사' },
      { s: 'Also, I {often climb|climb often} the mountain.', ex: '빈도부사는 일반동사 앞에' },
      { s: 'I\'m proud {of|for} my job.', ex: 'be proud of: ~을 자랑스러워하다' },
      { s: 'I think that protecting wild animals {is|are} important.', ex: '동명사 주어는 단수 취급 → is' },
      { s: 'We should keep an eye on them and their homes {to live|live} together.', ex: '목적(~하기 위해) → to live' },
      { s: 'This ship is {stronger|strong} than other ships.', ex: 'than 앞 → 비교급 stronger' },
      { s: 'It can {break|breaks} thick ice across the ocean.', ex: '조동사 can + 동사원형' },
      { s: 'Thanks to Araon, I can {collect|collecting} seawater samples.', ex: '조동사 can + 동사원형' },
      { s: 'I hope {that|what} my work can help the Earth.', ex: '뒤에 완전한 문장 → 접속사 that' }
    ] },
    { type: 'verb', title: '동사변형', guide: '( ) 안의 동사를 알맞은 형태로 바꿔 쓰세요.', items: [
      { s: 'I ___ care of sick wild animals in the center.', v: 'take', a: ['take'], ex: 'take care of: ~을 돌보다' },
      { s: 'I take care of sick wild animals in the center and ___ them back to their homes.', v: 'send', a: ['send'], ex: 'take와 and로 연결 → send' },
      { s: 'Also, I often climb the mountain ___ after wild animals like bears.', v: 'look', a: ['to look'], ex: '목적(~하기 위해) → to look' },
      { s: 'I think that ___ wild animals is important.', v: 'protect', a: ['protecting', 'to protect'], ex: '주어 자리 → 동명사 (본문: protecting)' },
      { s: 'I think that protecting wild animals ___ important.', v: 'be', a: ['is'], ex: '동명사 주어는 단수 → is' },
      { s: 'We should keep an eye on them and their homes ___ together.', v: 'live', a: ['to live'], ex: '목적(~하기 위해) → to live' },
      { s: 'I often ___ on the special ship, Araon.', v: 'travel', a: ['travel'], ex: '주어 I + 현재형' },
      { s: 'It can ___ thick ice across the ocean.', v: 'break', a: ['break'], ex: 'can + 동사원형' },
      { s: 'The Arctic Ocean ___ the answers to the climate crisis.', v: 'have', a: ['has'], ex: '3인칭 단수 → has' },
      { s: 'I hope that my work can ___ the Earth.', v: 'help', a: ['help'], ex: 'can + 동사원형' }
    ] },
    { type: 'error', title: '오류찾기', guide: '어법상 틀린 곳을 고르세요.', items: [
      { s: 'I take care [[of]] sick wild animals in the center and send [[back them]] [[to]] [[their]] homes.', w: 1, fix: 'them back', ex: '이어동사 목적어가 대명사 → send them back' },
      { s: 'Also, I often [[climb]] the mountain [[looking]] after wild animals [[like]] [[bears]].', w: 1, fix: 'to look', ex: '목적(~하기 위해) → to look' },
      { s: 'I\'m proud [[of]] my job. I think [[that]] [[protecting]] wild animals [[are]] important.', w: 3, fix: 'is', ex: '동명사 주어는 단수 → is' },
      { s: 'We should [[keep]] an eye [[on]] them and their homes [[live]] [[together]].', w: 2, fix: 'to live', ex: '목적(~하기 위해) → to live' },
      { s: 'I work [[at]] the Arctic Dasan Station [[in]] Norway. I [[study]] the soil, seawater, and ice in the Arctic. I [[travel often]] on the special ship, Araon.', w: 3, fix: 'often travel', ex: '빈도부사는 일반동사 앞 → often travel' },
      { s: 'This ship is [[strong]] [[than]] other ships. It can [[break]] [[thick]] ice across the ocean.', w: 0, fix: 'stronger', ex: 'than 앞 → 비교급 stronger' },
      { s: 'Thanks to Araon, I can [[collects]] seawater samples. The Arctic Ocean [[has]] the answers [[to]] the climate crisis. I hope [[that]] my work can help the Earth.', w: 0, fix: 'collect', ex: 'can + 동사원형' }
    ] },
    { type: 'scramble', title: '본문 스크램블', guide: '우리말에 맞게 단어를 눌러 문장을 완성하세요.', items: [
      { ko: '저는 센터의 아픈 야생 동물을 돌보고 그들을 집으로 돌려보냅니다.', en: 'I take care of sick wild animals in the center and send them back to their homes.' },
      { ko: '또한 저는 곰과 같은 야생 동물을 돌보기 위해 자주 산을 오릅니다.', en: 'Also, I often climb the mountain to look after wild animals like bears.' },
      { ko: '저는 야생 동물을 보호하는 것이 중요하다고 생각합니다.', en: 'I think that protecting wild animals is important.' },
      { ko: '우리는 함께 살아가기 위해 그들과 그들의 서식처를 계속 지켜보아야 합니다.', en: 'We should keep an eye on them and their homes to live together.' },
      { ko: '이 배는 다른 배보다 더 튼튼합니다.', en: 'This ship is stronger than other ships.' },
      { ko: '아라온호 덕분에 저는 바닷물 표본을 채집할 수 있습니다.', en: 'Thanks to Araon, I can collect seawater samples.' },
      { ko: '북극해는 기후 위기에 대한 해답을 가지고 있습니다.', en: 'The Arctic Ocean has the answers to the climate crisis.' },
      { ko: '저는 제 일이 지구를 도울 수 있기를 바랍니다.', en: 'I hope that my work can help the Earth.' }
    ] },
    { type: 'order', title: '문장순서', guide: '문장을 본문 순서대로 눌러서 배열하세요.', items: [
      { lines: ['My name is Jihan.', 'I am a vet at the wild animal care center in Jirisan.', 'I take care of sick wild animals in the center and send them back to their homes.', 'Also, I often climb the mountain to look after wild animals like bears.'] },
      { lines: ['I\'m proud of my job.', 'I think that protecting wild animals is important.', 'We should keep an eye on them and their homes to live together.', 'My name is Eun, and I am an Arctic scientist.'] },
      { lines: ['I work at the Arctic Dasan Station in Norway.', 'I study the soil, seawater, and ice in the Arctic.', 'I often travel on the special ship, Araon.', 'This ship is stronger than other ships.'] },
      { lines: ['It can break thick ice across the ocean.', 'Thanks to Araon, I can collect seawater samples.', 'The Arctic Ocean has the answers to the climate crisis.', 'I hope that my work can help the Earth.'] }
    ] },
    { type: 'insert', title: '문장삽입', guide: '주어진 문장이 들어가기에 가장 알맞은 곳을 고르세요.', items: [
      { lines: ['My name is Jihan.', 'I am a vet at the wild animal care center in Jirisan.', 'I take care of sick wild animals in the center and send them back to their homes.', 'Also, I often climb the mountain to look after wild animals like bears.', 'I\'m proud of my job.'], given: 2, ex: 'the center는 앞 문장의 보호 센터를 가리키고, 뒤 문장의 Also는 하는 일을 하나 더 덧붙인다.' },
      { lines: ['I\'m proud of my job.', 'I think that protecting wild animals is important.', 'We should keep an eye on them and their homes to live together.', 'My name is Eun, and I am an Arctic scientist.'], given: 2, ex: 'them은 앞 문장의 wild animals를 가리킨다.' },
      { lines: ['I study the soil, seawater, and ice in the Arctic.', 'I often travel on the special ship, Araon.', 'This ship is stronger than other ships.', 'It can break thick ice across the ocean.', 'Thanks to Araon, I can collect seawater samples.'], given: 2, ex: 'This ship은 앞의 Araon을 가리키고, 뒤 문장의 It은 This ship을 가리킨다.' },
      { lines: ['This ship is stronger than other ships.', 'It can break thick ice across the ocean.', 'Thanks to Araon, I can collect seawater samples.', 'The Arctic Ocean has the answers to the climate crisis.', 'I hope that my work can help the Earth.'], given: 2, ex: '얼음을 깰 수 있는 아라온호 덕분에 바닷물 표본을 채집할 수 있다.' }
    ] },
    { type: 'odd', title: '어색한 문장', guide: '글의 흐름과 관계없는 문장을 고르세요.', items: [
      { lines: ['I am a vet at the wild animal care center in Jirisan.', 'I take care of sick wild animals in the center and send them back to their homes.', 'I keep the animals in the center forever.', 'Also, I often climb the mountain to look after wild animals like bears.', 'I\'m proud of my job.'], odd: 2, ex: '동물들을 집(서식처)으로 돌려보낸다는 내용과 반대된다.' },
      { lines: ['I\'m proud of my job.', 'I think that protecting wild animals is important.', 'Wild animals don\'t need our help at all.', 'We should keep an eye on them and their homes to live together.'], odd: 2, ex: '야생 동물 보호가 중요하다는 흐름과 맞지 않는다.' },
      { lines: ['I work at the Arctic Dasan Station in Norway.', 'I study the soil, seawater, and ice in the Arctic.', 'I often travel on the special ship, Araon.', 'Araon is a small ship, so it can\'t go through ice.', 'This ship is stronger than other ships.', 'It can break thick ice across the ocean.'], odd: 3, ex: '아라온호는 다른 배보다 튼튼하고 두꺼운 얼음을 깰 수 있다.' },
      { lines: ['Thanks to Araon, I can collect seawater samples.', 'The Arctic Ocean has the answers to the climate crisis.', 'The climate crisis is not a problem for the Earth.', 'I hope that my work can help the Earth.'], odd: 2, ex: '기후 위기의 해답을 찾아 지구를 돕고 싶다는 흐름과 맞지 않는다.' }
    ] },
    { type: 'blank', title: '빈칸추론', guide: '빈칸에 들어갈 말로 가장 알맞은 것을 고르세요.', items: [
      { s: 'I take care of sick wild animals in the center and ____ to their homes.', opts: ['send them back', 'keep them all', 'sell them', 'hide them'], ex: '치료한 동물을 집(서식처)으로 돌려보낸다.' },
      { s: 'Also, I often climb the mountain ____ wild animals like bears.', opts: ['to look after', 'to hunt', 'to run away from', 'to sell'], ex: '곰 같은 야생 동물을 돌보기 위해 산을 오른다.' },
      { s: 'This ship is stronger than other ships. It can ____ across the ocean.', opts: ['break thick ice', 'sink easily', 'carry many cars', 'catch a lot of fish'], ex: '튼튼한 배라서 두꺼운 얼음을 깰 수 있다.' },
      { s: 'Thanks to Araon, I can collect seawater samples. The Arctic Ocean has the answers to ____.', opts: ['the climate crisis', 'the math test', 'the soccer game', 'the music class'], ex: '북극해는 기후 위기에 대한 해답을 가지고 있다.' }
    ] },
    { type: 'mc', title: '핵심문법', guide: '알맞은 답을 고르세요.', items: [
      { q: '빈칸에 알맞은 것은?<br><b>Protecting wild animals ______ important.</b>', opts: ['is', 'are', 'be', 'am'], ex: '동명사 주어는 단수 취급 → is' },
      { q: '밑줄 친 to부정사가 <b>"~하기 위해"</b>의 뜻이 <b>아닌</b> 것은?', opts: ['I want <u>to become</u> a vet.', 'I climb the mountain <u>to look</u> after bears.', 'We keep an eye on them <u>to live</u> together.', 'She went to the store <u>to buy</u> milk.'], ex: 'want to become은 want의 목적어(~하는 것). 나머지는 목적(~하기 위해).' },
      { q: '어법상 <b>틀린</b> 문장은?', opts: ['Please send back them.', 'Please send them back.', 'Please send the animals back.', 'Please send back the animals.'], ex: '목적어가 대명사이면 send them back 순서만 가능' },
      { q: '비교급 형태가 <b>틀린</b> 것은?', opts: ['important - importanter', 'thick - thicker', 'strong - stronger', 'big - bigger'], ex: '긴 형용사는 more를 쓴다: more important' },
      { q: '빈칸에 알맞은 것은?<br><b>This ship is stronger ______ other ships.</b>', opts: ['than', 'then', 'that', 'to'], ex: '비교급 + than: ~보다 더' },
      { q: '어법상 올바른 문장은?', opts: ['I often climb the mountain.', 'I climb often the mountain.', 'Often I climbs the mountain.', 'I often climbing the mountain.'], ex: '빈도부사는 일반동사 앞에' },
      { q: '빈칸에 알맞은 것은?<br><b>I hope ______ my work can help the Earth.</b>', opts: ['that', 'what', 'this', 'it'], ex: '완전한 문장을 이끄는 접속사 that' },
      { q: '빈칸에 알맞은 것은?<br><b>It can ______ thick ice across the ocean.</b>', opts: ['break', 'breaks', 'breaking', 'to break'], ex: 'can + 동사원형' },
      { q: '"나는 내 직업이 자랑스럽다."를 바르게 영작한 것은?', opts: ['I\'m proud of my job.', 'I\'m proud my job.', 'I proud of my job.', 'I\'m proud for my job.'], ex: 'be proud of: ~을 자랑스러워하다' }
    ] }
  ] }
  ]
};
