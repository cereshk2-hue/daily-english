/* 중1 천재(소영순) Lesson 4~6 (시험 범위 4·5·6과)
   4과: gen_m1c4.py · 5과: gen_m1c5.py · 6과: 예전 파일(id d1, d2 유지 → 학생 기록 보존). 7과는 시험 범위가 아니라 뺌
   prose: true → 본문을 대사가 아닌 설명문으로 표시 */
/* 10/28: 4·5과 대화문 추가(scratchpad/gen_m1cdlg.py), 10분 분량으로 쪼개서 pick(고르기) */
window.PKG = {
  id: 'm1-chunjae-so-L6',
  school: '중1 천재(소영순)',
  unit: 'Lesson 4~6',
  title: 'My Delicious Summer Trip · Share Your Joys and Worries · Heroes in Nature',
  titleKo: '나의 맛있는 여름 여행 · 기쁨과 걱정 나누기 · 자연에서 일하는 즐거움',
  exam: '2학기 기말고사',
  prose: true,
  stepsBefore: ['핵심어휘·숙어', '어휘선택', 'T/F 내용 확인', '어법선택', '동사변형', '오류찾기', '본문 스크램블', '문장순서', '문장삽입', '어색한 문장', '빈칸추론', '핵심문법'],
  teacherPhone: '',
  pick: true,
  days: [
  { id: 'k4a', name: 'DAY 1', range: '4과 대화문 ① 대화 1~3', story: 'Lesson 4 · 음식 권하기 · 경험 묘사하기 (Listen and Check)', passage: [['#', '4과 대화 1 · 아이스크림 (Listen and Check)', ''], ['M', 'Would you like some ice cream?', '아이스크림 드시겠어요?'], ['G', 'Yes, please.', '네, 좋아요.'], ['M', 'We have strawberry and chocolate.', '딸기와 초콜릿이 있어요.'], ['G', 'Strawberry ice cream, please.', '딸기 아이스크림 주세요.'], ['#', '4과 대화 2 · 주문하기 (Listen and Check)', ''], ['M', 'Hello. Are you ready to order?', '안녕하세요. 주문하시겠어요?'], ['G', 'Yes, I\'ll have a kebab.', '네, 저는 케밥을 먹을래요.'], ['M', 'Would you like a drink?', '마실 것 드실래요?'], ['G', 'Sure. Orange juice, please.', '물론이죠. 오렌지 주스 주세요.'], ['#', '4과 대화 3 · 베트남 여행 (Listen and Check)', ''], ['B', 'Jane, how was your trip to Vietnam?', 'Jane, 베트남 여행은 어땠어?'], ['G', 'It was great. I enjoyed the beautiful nature and ate famous local foods.', '아주 좋았어. 나는 아름다운 자연을 즐겼고 유명한 현지 음식을 먹었어.'], ['B', 'What did you eat?', '무엇을 먹었니?'], ['G', 'I ate rice noodle soup. It had a lot of vegetables and meat. It was tasty.', '쌀국수를 먹었어. 채소와 고기가 많았어. 정말 맛있었어.']], steps: [
    { type: 'vocab', title: '핵심어휘·숙어', quizN: 15, items: [['Would you like ~?', '~ 드시겠어요? (음식 권하기)'], ['strawberry', '딸기'], ['be ready to', '~할 준비가 되다'], ['order', '주문하다'], ['I\'ll have ~', '~을 먹을게요 (주문하기)'], ['drink', '음료, 마실 것'], ['trip', '여행'], ['enjoy', '즐기다'], ['nature', '자연'], ['famous', '유명한'], ['local', '현지의, 지역의'], ['rice noodle soup', '쌀국수'], ['vegetable', '채소'], ['meat', '고기'], ['tasty', '맛있는']] },
    { type: 'pick', title: '어휘선택', guide: '문맥에 맞는 낱말을 고르세요.', items: [
      { s: '{Strawberry|Vanilla} ice cream, please.', ex: '정답 ▶ Strawberry (딸기)\n오답 ▶ Vanilla (바닐라): 가게에 있는 맛은 딸기와 초콜릿(strawberry and chocolate)뿐이에요.' },
      { s: 'Hello. Are you ready to {order|sleep}?', ex: '정답 ▶ order (주문하다)\n오답 ▶ sleep: 식당에서 점원이 손님에게 → \'주문하시겠어요?\'' },
      { s: 'It was great. I enjoyed the beautiful {nature|noise} and ate famous local foods.', ex: '정답 ▶ nature (자연)\n오답 ▶ noise (소음): \'아름다운 ~을 즐겼다\' → 자연' }
    ] },
    { type: 'tf', title: 'T/F 내용 확인', guide: '본문 내용과 일치하면 T, 다르면 F를 고르세요.', items: [['The girl wants chocolate ice cream.', false, '정답 ▶ F\n이유: 소녀는 딸기 아이스크림(Strawberry ice cream)을 주문했어요.', null, 'Strawberry ice cream, please'], ['The girl ordered a kebab.', true, '정답 ▶ T\n이유: Yes, I\'ll have a kebab. → I\'ll have ~ = ~을 먹을게요(주문)', null, 'I\'ll have a kebab'], ['The girl doesn\'t want a drink.', false, '정답 ▶ F\n이유: 음료를 권하자 Sure.라고 하고 오렌지 주스를 주문했어요.', null, 'Sure. Orange juice, please'], ['Jane didn\'t enjoy her trip to Vietnam.', false, '정답 ▶ F\n이유: It was great. 아름다운 자연을 즐겼다(enjoyed)고 했어요.', null, 'It was great'], ['Jane ate rice noodle soup in Vietnam.', true, '정답 ▶ T\n이유: I ate rice noodle soup.', null, 'I ate rice noodle soup']] },
    { type: 'mc', title: '알맞은 응답 고르기', guide: '대화의 흐름에 맞는 응답을 고르세요.', items: [
      { q: '다음 말에 이어질 응답으로 가장 알맞은 것은?<br><b>A: Would you like some ice cream?</b>', opts: ['Yes, please.', 'Yes, I did.', 'I ate pizza.', 'It was great.'], ex: '정답 ▶ Yes, please.\n이유: Would you like ~?(음식 권하기)에 승낙할 때 → Yes, please. / 거절할 때 → No, thanks.\n오답 ▶ Yes, I did.는 Did you ~? 질문의 대답' },
      { q: '다음 말에 이어질 응답으로 가장 알맞은 것은?<br><b>A: How was your trip to Vietnam?</b>', opts: ['It was great.', 'Yes, please.', 'I\'ll have a kebab.', 'No, thanks.'], ex: '정답 ▶ It was great.\n이유: How was ~?(~은 어땠니?)는 소감을 묻는 말 → 과거형으로 느낌을 말해요.' }
    ] },
    { type: 'mc', title: '일치·불일치', guide: '선택지는 본문을 어려운 어휘로 바꿔 쓴 문장이에요. 풀고 나서 해설의 어휘를 꼭 확인하세요.', items: [
      { box: ['4과 대화 1 · 아이스크림 (Listen and Check)', '4과 대화 2 · 주문하기 (Listen and Check)', '4과 대화 3 · 베트남 여행 (Listen and Check)'], q: '대화의 내용과 일치하지 <u>않는</u> 것은?', opts: ['The rice noodle soup had no meat.', 'The man has strawberry and chocolate ice cream.', 'The girl is ready to order.', 'The girl will have a kebab and orange juice.', 'Jane enjoyed the nature in Vietnam.'], ex: '정답 ▶ The rice noodle soup had no meat.\n이유: 쌀국수에는 채소와 고기가 많았어요(a lot of vegetables and meat).', per: [['쌀국수에는 고기가 없었다.', 'It had a lot of vegetables and meat', '불일치 → 고기가 많았음'], ['남자에게는 딸기와 초콜릿 아이스크림이 있다.', 'We have strawberry and chocolate', '일치'], ['소녀는 주문할 준비가 되었다.', 'Yes, I\'ll have a kebab', '일치'], ['소녀는 케밥과 오렌지 주스를 먹을 것이다.', ['I\'ll have a kebab', 'Orange juice, please'], '일치'], ['Jane은 베트남의 자연을 즐겼다.', 'I enjoyed the beautiful nature', '일치']] }
    ] },
    { type: 'pick', title: '어법선택', guide: '어법상 알맞은 것을 고르세요.', items: [
      { s: 'Hello. Are you ready {to order|ordering}?', ex: '정답 ▶ to order\n이유: be ready to + 동사원형 = ~할 준비가 되다' },
      { s: 'What did you {eat|ate}?', ex: '정답 ▶ eat\n이유: 의문사 + did + 주어 + 동사원형 ~? (did가 과거를 나타내니 동사는 원형)' },
      { s: 'It was great. I enjoyed the beautiful nature and {ate|eat} famous local foods.', ex: '정답 ▶ ate\n이유: 지난 여행 이야기 → 과거형. 앞의 enjoyed와 and로 나란히 연결돼요. (eat - ate - eaten)' }
    ] },
    { type: 'scramble', title: '본문 스크램블', guide: '우리말에 맞게 단어를 눌러 문장을 완성하세요.', items: [
      { ko: '아이스크림 드시겠어요?', en: 'Would you like some ice cream?' },
      { ko: '나는 아름다운 자연을 즐겼고 유명한 현지 음식을 먹었어.', en: 'I enjoyed the beautiful nature and ate famous local foods.' }
    ] },
    { type: 'order', title: '문장순서', guide: '대화(문장)를 순서대로 눌러서 배열하세요.', items: [
      { lines: ['Jane, how was your trip to Vietnam?', 'It was great. I enjoyed the beautiful nature and ate famous local foods.', 'What did you eat?', 'I ate rice noodle soup. It had a lot of vegetables and meat. It was tasty.'], flow: ['B: 베트남 여행은 어땠어?', 'G: 좋았어, 자연을 즐기고 현지 음식을 먹었어', 'B: 무엇을 먹었니?', 'G: 쌀국수, 맛있었어'] }
    ] },
    { type: 'blank', title: '빈칸추론', guide: '빈칸에 들어갈 말로 가장 알맞은 것을 고르세요.', items: [
      { s: 'Would you like a ____?', opts: ['drink', 'kebab', 'pizza', 'table'], ex: '정답 ▶ drink\n이유: 대답이 Orange juice, please.이니 \'마실 것\'을 권한 거예요.' },
      { s: 'I ate rice noodle soup. It had a lot of vegetables and meat. It was ____.', opts: ['tasty', 'terrible', 'boring', 'expensive'], ex: '정답 ▶ tasty (맛있는)\n이유: 여행이 좋았다고(It was great) 했으니 먹은 음식도 \'맛있었다\'가 자연스러워요.' }
    ] },
    { type: 'mc', title: '어색한 대화 고르기', guide: '짝지어진 대화 중 어색한 것을 고르세요.', items: [
      { q: '다음 중 짝지어진 대화가 <b>어색한</b> 것은?', opts: ['A: How was your trip? B: Yes, please.', 'A: Would you like some cake? B: No, thanks. I\'m full.', 'A: Are you ready to order? B: Yes, I\'ll have a sandwich.', 'A: What did you eat? B: I ate bibimbap.'], ex: '정답 ▶ A: How was your trip? B: Yes, please.\n이유: 여행 소감을 물었으니 It was great. 처럼 답해야 해요. Yes, please.는 음식을 권할 때의 대답이에요.' }
    ] },
    { type: 'mc', title: '의사소통 기능', guide: '상황에 맞는 표현을 고르세요.', items: [
      { q: '음식을 권하는 표현이 <b>아닌</b> 것은?', opts: ['What did you eat?', 'Would you like some juice?', 'Would you like to try some?', 'Do you want some cookies?'], ex: '정답 ▶ What did you eat?\n이유: \'무엇을 먹었니?\'는 경험을 묻는 말이에요. 나머지는 모두 음식을 권하는 표현이에요.\n참고 ▶ Would you like + 명사 / Would you like to + 동사원형' }
    ] },
    { type: 'mc', title: '요약문 완성', guide: '본문을 읽고 요약문의 빈칸 (A), (B)에 들어갈 말을 고르세요.', items: [
      { n: null, box: ['4과 대화 1 · 아이스크림 (Listen and Check)', '4과 대화 2 · 주문하기 (Listen and Check)'], q: '다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 알맞은 것은?<br><b>The girl chose (A) ______ ice cream, and at the restaurant she ordered a kebab and orange (B) ______.</b>', opts: ['(A) strawberry – (B) juice', '(A) chocolate – (B) juice', '(A) strawberry – (B) soup', '(A) chocolate – (B) cake', '(A) vanilla – (B) juice'], ex: '정답 ▶ (A) strawberry – (B) juice\n(A) 딸기 아이스크림을 골랐다 → strawberry\n(B) 케밥과 오렌지 \'주스\' → juice', ev: ['Strawberry ice cream, please', 'Orange juice, please'] },
      { n: null, box: ['4과 대화 3 · 베트남 여행 (Listen and Check)'], q: '다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 알맞은 것은?<br><b>Jane (A) ______ the nature in Vietnam and ate rice noodle soup with a lot of vegetables and (B) ______.</b>', opts: ['(A) enjoyed – (B) meat', '(A) hated – (B) meat', '(A) enjoyed – (B) fruit', '(A) painted – (B) rice', '(A) missed – (B) fish'], ex: '정답 ▶ (A) enjoyed – (B) meat\n(A) 아름다운 자연을 \'즐겼다\' → enjoyed\n(B) 채소와 \'고기\'가 많았다 → meat', ev: ['I enjoyed the beautiful nature', 'It had a lot of vegetables and meat'] }
    ] }
  ] },
  { id: 'k4b', name: 'DAY 2', range: '4과 대화문 ② 대화 4·클립', story: 'Lesson 4 · 제빵 수업 · 단오 수리취떡', passage: [['#', '4과 대화 4 · 제빵 수업 (In Everyday Life)', ''], ['Mina', 'How was your weekend, Jason?', '주말은 어땠어, Jason?'], ['Jason', 'It was good. I went to a baking class on Saturday.', '좋았어. 나는 토요일에 제빵 수업을 들으러 갔어.'], ['Mina', 'Oh, what did you make?', '오, 무엇을 만들었니?'], ['Jason', 'I made apple pies and chocolate cookies.', '사과 파이와 초콜릿 쿠키를 만들었어.'], ['Mina', 'Sounds delicious!', '맛있겠다!'], ['Jason', 'I brought some of them with me. Would you like some, Mina?', '내가 그중 몇 개를 가져왔어. 좀 먹어 볼래, 미나야?'], ['Mina', 'Sure. Wow, they\'re so good.', '물론이지. 와, 정말 맛있다.'], ['#', '4과 클립 · 단오 수리취떡 (Enjoy the Clip)', ''], ['Jisu', 'Welcome to Jisu\'s channel!', '지수의 채널에 오신 걸 환영해요!'], ['Jisu', 'Today is a traditional Korean holiday, Dano.', '오늘은 한국의 전통적인 명절인 단오입니다.'], ['Jisu', 'So I\'m making surichwitteok with my dad now.', '그래서 저는 지금 아빠와 함께 수리취떡을 만들고 있어요.'], ['Jisu', 'It\'s rice cake with a wheel pattern.', '그것은 바퀴 문양을 가진 떡이랍니다.'], ['Jisu', 'It\'s finally ready!', '마침내 떡이 준비되었어요!'], ['Jisu', 'It looks delicious.', '맛있어 보이네요.'], ['Jisu', 'Would you like some?', '좀 드셔 보실래요?']], steps: [
    { type: 'vocab', title: '핵심어휘·숙어', quizN: 15, items: [['weekend', '주말'], ['baking class', '제빵 수업'], ['cookie', '쿠키'], ['Sounds delicious!', '맛있겠다!'], ['bring', '가져오다 (bring - brought - brought)'], ['some of them', '그중 몇 개'], ['Welcome to ~', '~에 오신 걸 환영합니다'], ['traditional', '전통적인'], ['holiday', '명절, 휴일'], ['rice cake', '떡'], ['wheel', '바퀴'], ['pattern', '무늬, 문양'], ['finally', '마침내'], ['ready', '준비된'], ['look delicious', '맛있어 보이다']] },
    { type: 'pick', title: '어휘선택', guide: '문맥에 맞는 낱말을 고르세요.', items: [
      { s: 'It was good. I went to a {baking|swimming} class on Saturday.', ex: '정답 ▶ baking (제빵)\n오답 ▶ swimming: 그 수업에서 파이와 쿠키를 만들었으니 \'제빵\' 수업이에요.' },
      { s: 'Today is a traditional Korean {holiday|food}, Dano.', ex: '정답 ▶ holiday (명절)\n오답 ▶ food: 단오(Dano)는 한국의 전통 \'명절\'이에요.' },
      { s: 'It\'s rice cake with a wheel {pattern|color}.', ex: '정답 ▶ pattern (무늬)\n오답 ▶ color (색): 수리취떡에는 떡살로 찍은 바퀴 \'무늬\'가 있어요.' }
    ] },
    { type: 'tf', title: 'T/F 내용 확인', guide: '본문 내용과 일치하면 T, 다르면 F를 고르세요.', items: [['Jason went to a baking class on Sunday.', false, '정답 ▶ F\n이유: 일요일이 아니라 토요일(on Saturday)에 갔어요.', null, 'I went to a baking class on Saturday'], ['Jason made apple pies and chocolate cookies.', true, '정답 ▶ T\n이유: I made apple pies and chocolate cookies.', null, 'I made apple pies and chocolate cookies'], ['Mina didn\'t like Jason\'s food.', false, '정답 ▶ F\n이유: Wow, they\'re so good. 정말 맛있다고 했어요.', null, 'they\'re so good'], ['Jisu is making surichwitteok with his mom.', false, '정답 ▶ F\n이유: 엄마가 아니라 아빠(my dad)와 만들고 있어요.', null, 'I\'m making surichwitteok with my dad now'], ['Dano is a traditional Korean holiday.', true, '정답 ▶ T\n이유: Today is a traditional Korean holiday, Dano.', null, 'Today is a traditional Korean holiday, Dano']] },
    { type: 'mc', title: '알맞은 응답 고르기', guide: '대화의 흐름에 맞는 응답을 고르세요.', items: [
      { q: '다음 말에 이어질 응답으로 가장 알맞은 것은?<br><b>A: How was your weekend?</b>', opts: ['It was good. I went to a baking class.', 'Yes, please.', 'I\'m making rice cake.', 'Sounds delicious!'], ex: '정답 ▶ It was good. I went to a baking class.\n이유: 주말 소감(How was ~?)을 물으면 → 느낌(It was good) + 한 일(과거형)로 답해요.' },
      { q: '다음 말에 이어질 응답으로 가장 알맞은 것은?<br><b>A: I brought some cookies. Would you like some?</b>', opts: ['Sure. Wow, they are so good.', 'I made cookies.', 'It was good.', 'Welcome to my channel!'], ex: '정답 ▶ Sure. Wow, they are so good.\n이유: 음식을 권하면(Would you like some?) → 승낙 Sure. / Yes, please. 거절 No, thanks.' }
    ] },
    { type: 'mc', title: '일치·불일치', guide: '선택지는 본문을 어려운 어휘로 바꿔 쓴 문장이에요. 풀고 나서 해설의 어휘를 꼭 확인하세요.', items: [
      { box: ['4과 대화 4 · 제빵 수업 (In Everyday Life)'], q: '대화의 내용과 일치하지 <u>않는</u> 것은?', opts: ['Mina made chocolate cookies.', 'Jason took a baking class on Saturday.', 'Jason made apple pies.', 'Jason brought some cookies with him.', 'Mina tried Jason\'s food.'], ex: '정답 ▶ Mina made chocolate cookies.\n이유: 초콜릿 쿠키를 만든 사람은 Jason이에요. 미나는 Jason이 가져온 것을 먹어 봤어요.', per: [['미나가 초콜릿 쿠키를 만들었다.', 'I made apple pies and chocolate cookies', '불일치 → Jason이 만듦'], ['Jason은 토요일에 제빵 수업을 들었다.', 'I went to a baking class on Saturday', '일치'], ['Jason은 사과 파이를 만들었다.', 'I made apple pies and chocolate cookies', '일치'], ['Jason은 쿠키 몇 개를 가져왔다.', 'I brought some of them with me', '일치'], ['미나는 Jason의 음식을 먹어 봤다.', 'Sure. Wow, they\'re so good', '일치']] },
      { box: ['4과 클립 · 단오 수리취떡 (Enjoy the Clip)'], q: '클립의 내용과 일치하지 <u>않는</u> 것은?', opts: ['The rice cake isn\'t ready yet.', 'Jisu has a channel.', 'Today is Dano.', 'Jisu is making rice cake with his dad.', 'The rice cake has a wheel pattern.'], ex: '정답 ▶ The rice cake isn\'t ready yet.\n이유: It\'s finally ready! 마침내 떡이 준비됐다고 했어요.', per: [['떡은 아직 준비되지 않았다.', 'It\'s finally ready', '불일치'], ['지수는 채널을 가지고 있다.', 'Welcome to Jisu\'s channel', '일치'], ['오늘은 단오이다.', 'Today is a traditional Korean holiday, Dano', '일치'], ['지수는 아빠와 떡을 만들고 있다.', 'I\'m making surichwitteok with my dad now', '일치'], ['떡에는 바퀴 문양이 있다.', 'It\'s rice cake with a wheel pattern', '일치']] }
    ] },
    { type: 'pick', title: '어법선택', guide: '어법상 알맞은 것을 고르세요.', items: [
      { s: 'I {brought|bringed} some of them with me. Would you like some, Mina?', ex: '정답 ▶ brought\n이유: bring의 과거형은 불규칙 brought (bring - brought - brought)' },
      { s: 'So I\'m {making|make} surichwitteok with my dad now.', ex: '정답 ▶ making\n이유: now(지금) 하는 중 → 현재진행형 am + -ing' },
      { s: 'It looks {delicious|deliciously}.', ex: '정답 ▶ delicious\n이유: 감각동사 look + 형용사 = ~해 보이다. 부사(deliciously)는 쓰지 않아요.' }
    ] },
    { type: 'scramble', title: '본문 스크램블', guide: '우리말에 맞게 단어를 눌러 문장을 완성하세요.', items: [
      { ko: '내가 그중 몇 개를 가져왔어.', en: 'I brought some of them with me.' },
      { ko: '그것은 바퀴 문양을 가진 떡이랍니다.', en: 'It\'s rice cake with a wheel pattern.' }
    ] },
    { type: 'order', title: '문장순서', guide: '대화(문장)를 순서대로 눌러서 배열하세요.', items: [
      { lines: ['How was your weekend, Jason?', 'It was good. I went to a baking class on Saturday.', 'Oh, what did you make?', 'I made apple pies and chocolate cookies.'], flow: ['Mina: 주말은 어땠어?', 'Jason: 좋았어, 제빵 수업에 갔어', 'Mina: 무엇을 만들었니?', 'Jason: 사과 파이와 초콜릿 쿠키'] }
    ] },
    { type: 'blank', title: '빈칸추론', guide: '빈칸에 들어갈 말로 가장 알맞은 것을 고르세요.', items: [
      { s: 'I made apple pies and chocolate ____.', opts: ['cookies', 'juice', 'soup', 'noodles'], ex: '정답 ▶ cookies\n이유: 제빵 수업에서 만든 것 = 사과 파이와 초콜릿 \'쿠키\'' },
      { s: 'Today is a traditional Korean holiday, ____.', opts: ['Dano', 'Chuseok', 'Seollal', 'Christmas'], ex: '정답 ▶ Dano\n이유: 수리취떡은 단오에 먹는 떡이에요. 클립에서 오늘은 단오라고 했어요.' }
    ] },
    { type: 'mc', title: '어색한 대화 고르기', guide: '짝지어진 대화 중 어색한 것을 고르세요.', items: [
      { q: '다음 중 짝지어진 대화가 <b>어색한</b> 것은?', opts: ['A: Would you like some juice? B: Yes, I did.', 'A: Would you like some cookies? B: Sure, thanks.', 'A: What did you make? B: I made apple pies.', 'A: How was your weekend? B: It was good.'], ex: '정답 ▶ A: Would you like some juice? B: Yes, I did.\n이유: 음식을 권하는 말에는 Yes, please. / No, thanks.로 답해요. Yes, I did.는 Did you ~?의 대답이에요.' }
    ] },
    { type: 'mc', title: '의사소통 기능', guide: '상황에 맞는 표현을 고르세요.', items: [
      { q: '밑줄 친 말과 바꿔 쓸 수 있는 것은?<br><b>Mina: <u>How was your weekend</u>, Jason?</b>', opts: ['What was your weekend like', 'Where did you go', 'What will you do this weekend', 'Do you like weekends'], ex: '정답 ▶ What was your weekend like\n이유: How was ~? = What was ~ like? (~은 어땠니? 소감 묻기)' }
    ] },
    { type: 'mc', title: '요약문 완성', guide: '본문을 읽고 요약문의 빈칸 (A), (B)에 들어갈 말을 고르세요.', items: [
      { n: null, box: ['4과 대화 4 · 제빵 수업 (In Everyday Life)'], q: '다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 알맞은 것은?<br><b>Jason took a (A) ______ class on Saturday and (B) ______ some cookies to share with Mina.</b>', opts: ['(A) baking – (B) brought', '(A) swimming – (B) brought', '(A) baking – (B) sold', '(A) painting – (B) bought', '(A) baking – (B) threw'], ex: '정답 ▶ (A) baking – (B) brought\n(A) \'제빵\' 수업 → baking\n(B) 만든 것을 \'가져왔다\' → brought (bring의 과거형)', ev: ['I went to a baking class on Saturday', 'I brought some of them with me'] },
      { n: null, box: ['4과 클립 · 단오 수리취떡 (Enjoy the Clip)'], q: '다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 알맞은 것은?<br><b>On Dano, Jisu is making rice cake with a (A) ______ pattern, and he (B) ______ some to the viewers.</b>', opts: ['(A) wheel – (B) offers', '(A) flower – (B) offers', '(A) wheel – (B) sells', '(A) star – (B) throws', '(A) flower – (B) sells'], ex: '정답 ▶ (A) wheel – (B) offers\n(A) \'바퀴\' 문양 → wheel\n(B) Would you like some?(좀 드셔 보실래요?) = 음식을 \'권한다\' → offers', ev: ['It\'s rice cake with a wheel pattern', 'Would you like some?'] }
    ] }
  ] },
  { id: 'L4a', name: 'DAY 3', range: '4과 본문 ❶❷', story: 'Lesson 4 · 담양의 대나무 정원과 음식 · 통영의 충무김밥', passage: [['', '❶', ''], ['', 'During the summer vacation, William traveled around Korea with his family.', '여름 방학 동안, William은 가족과 함께 한국 여기저기를 여행했다.'], ['', 'This is his food diary.', '이것은 그의 음식 일기이다.'], ['', 'July 25', '7월 25일'], ['', 'We went to Damyang and visited Jungnogwon, a famous bamboo garden.', '우리는 담양에 갔고 유명한 대나무 정원인 죽녹원을 방문했다.'], ['', 'We enjoyed walking in the garden.', '우리는 정원에서 걷는 것을 즐겼다.'], ['', 'After we looked around, we ate two local dishes, daetongbap and tteokgalbi.', '주변을 둘러본 후에, 우리는 두 가지 지역 음식인 대통밥과 떡갈비를 먹었다.'], ['', 'Daetongbap is rice in a bamboo bowl.', '대통밥은 대나무 그릇에 담긴 밥이다.'], ['', 'I loved its unique bamboo smell.', '나는 그것의 독특한 대나무 향이 정말 좋았다.'], ['', 'Tteokgalbi, a Korean beef dish, was soft and sweet.', '한국의 소고기 요리인 떡갈비는 부드럽고 달콤했다.'], ['', 'The dishes really went well together.', '그 요리들은 함께 정말 잘 어울렸다.'], ['', '❷', ''], ['', 'July 30', '7월 30일'], ['', 'We visited Tongyeong and went up the mountain by cable car.', '우리는 통영을 방문했고 케이블카를 타고 산에 올라갔다.'], ['', 'Seeing the blue ocean and the green islands was fantastic!', '파란 바다와 초록 섬들을 보는 것은 환상적이었다!'], ['', 'Near the sea, we found a local restaurant and ate chungmugimbap.', '바다 근처에서 우리는 현지 식당을 찾았고 충무김밥을 먹었다.'], ['', 'It wasn\'t like other types of gimbap.', '그것은 다른 종류의 김밥과 달랐다.'], ['', 'There was only rice inside the seaweed.', '김 안에는 오직 밥만 있었다.'], ['', 'Kimchi and spicy squid were on the side.', '김치와 매운 오징어는 옆에 있었다.'], ['', 'It was spicy but really delicious.', '그것은 매웠지만 정말 맛있었다.'], ['', 'I heard about the history of this food.', '나는 이 음식의 역사에 관해 들었다.'], ['', 'Chungmu is an old name for Tongyeong.', '충무는 통영의 옛 이름이다.'], ['', 'Long ago, fishermen in this town started to eat chungmugimbap because it did not go bad quickly.', '오래전에, 이 마을의 어부들은 그것이 빨리 상하지 않았기 때문에 충무김밥을 먹기 시작했다.']], steps: [
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
  { id: 'L4b', name: 'DAY 4', range: '4과 본문 ❸', story: 'Lesson 4 · 제주도의 돔베고기', passage: [['', '❸', ''], ['', 'August 2', '8월 2일'], ['', 'Jeju-do is a beautiful island in Korea.', '제주도는 한국의 아름다운 섬이다.'], ['', 'We went there on a very hot day, and we became tired.', '우리는 매우 더운 날 그곳에 갔고, 피곤해졌다.'], ['', 'However, we got our energy back thanks to dombegogi.', '하지만 우리는 돔베고기 덕분에 기운을 되찾았다.'], ['', 'It surprised me in two ways.', '그것은 두 가지 면에서 나를 놀라게 했다.'], ['', 'First, it was pork on a cutting board, not on a plate.', '첫째, 그것은 접시가 아닌 도마 위에 놓인 돼지고기였다.'], ['', 'Second, the meat was so soft!', '둘째, 고기가 정말 부드러웠다!'], ['', 'I had it with a special fish sauce, and the sauce was great, too.', '나는 그것을 특별한 생선 소스와 함께 먹었는데, 그 소스도 훌륭했다.'], ['', 'Later, I learned about the meaning of dombe.', '나중에, 나는 돔베의 의미에 대해 배웠다.'], ['', 'It means a cutting board in Jeju\'s language.', '그것은 제주 말로 도마를 의미한다.']], steps: [
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
  { id: 'k5a', name: 'DAY 5', range: '5과 대화문 ① 대화 1~3', story: 'Lesson 5 · 감정이나 상태 묻기 · 걱정 표현하기 (Listen and Circle)', passage: [['#', '5과 대화 1 · 깨진 화분 (Listen and Circle)', ''], ['M', 'You look upset. What\'s the matter?', '너 속상해 보인다. 무슨 일 있니?'], ['G', 'I broke a flower pot in the garden. I\'m sorry, Dad.', '제가 정원에 있는 화분을 깼어요. 죄송해요, 아빠.'], ['M', 'Oh, don\'t worry. It\'s okay. We can clean the garden together.', '오, 걱정하지 마. 괜찮아. 정원을 같이 치우면 돼.'], ['#', '5과 대화 2 · 강아지 걱정 (Listen and Circle)', ''], ['G', 'Isaac, are you okay?', 'Isaac, 너 괜찮니?'], ['B', 'I\'m worried about my dog. He isn\'t eating a lot these days.', '우리 개가 걱정돼. 요새 밥을 많이 먹지 않아.'], ['G', 'I\'m sorry to hear that. He needs to go to the animal hospital.', '안됐구나. 동물 병원에 가 봐야 할 것 같아.'], ['#', '5과 대화 3 · 동생 걱정 (Listen and Circle)', ''], ['G', 'I\'m worried about my little brother. He plays video games too much.', '나는 내 남동생이 걱정돼. 남동생은 비디오 게임을 너무 많이 해.'], ['B', 'Why don\'t you play with him outside? That can help.', '밖에서 남동생과 함께 노는 건 어때? 도움이 될 수 있어.'], ['G', 'You are right. I\'ll play soccer with him on weekends.', '네 말이 맞아. 주말마다 남동생과 함께 축구를 할게.']], steps: [
    { type: 'vocab', title: '핵심어휘·숙어', quizN: 15, items: [['upset', '속상한'], ['What\'s the matter?', '무슨 일 있니?'], ['break', '깨다 (break - broke - broken)'], ['flower pot', '화분'], ['garden', '정원'], ['Don\'t worry.', '걱정하지 마.'], ['clean', '치우다, 청소하다'], ['together', '함께'], ['be worried about', '~을 걱정하다'], ['these days', '요즘'], ['I\'m sorry to hear that.', '그것참 안됐구나.'], ['animal hospital', '동물 병원'], ['too much', '너무 많이'], ['Why don\'t you ~?', '~하는 게 어때?'], ['outside', '밖에서'], ['on weekends', '주말마다']] },
    { type: 'pick', title: '어휘선택', guide: '문맥에 맞는 낱말을 고르세요.', items: [
      { s: 'You look {upset|happy}. What\'s the matter?', ex: '정답 ▶ upset (속상한)\n오답 ▶ happy: 뒤에 \'무슨 일 있니?\'라고 묻고, 소녀가 화분을 깼다고 사과해요.' },
      { s: 'I\'m sorry to hear that. He needs to go to the animal {hospital|school}.', ex: '정답 ▶ hospital (병원)\n오답 ▶ school: 개가 밥을 잘 안 먹으니 \'동물 병원\'에 가 봐야 해요.' },
      { s: 'I\'m worried about my little brother. He plays video games too {much|little}.', ex: '정답 ▶ much\n오답 ▶ little: 동생이 걱정되는 이유 → 게임을 \'너무 많이\' 해서' }
    ] },
    { type: 'tf', title: 'T/F 내용 확인', guide: '본문 내용과 일치하면 T, 다르면 F를 고르세요.', items: [['The girl broke a flower pot.', true, '정답 ▶ T\n이유: I broke a flower pot in the garden.', null, 'I broke a flower pot in the garden'], ['The dad is angry at the girl.', false, '정답 ▶ F\n이유: don\'t worry. It\'s okay. 아빠는 괜찮다며 함께 치우자고 해요.', null, 'Oh, don\'t worry. It\'s okay'], ['Isaac\'s dog is eating a lot these days.', false, '정답 ▶ F\n이유: 요즘 밥을 많이 먹지 않아요(isn\'t eating a lot).', null, 'He isn\'t eating a lot these days'], ['The girl\'s little brother plays video games too much.', true, '정답 ▶ T\n이유: He plays video games too much.', null, 'He plays video games too much'], ['The girl will play basketball with her brother.', false, '정답 ▶ F\n이유: 농구가 아니라 축구(soccer)를 할 거예요.', null, 'I\'ll play soccer with him on weekends']] },
    { type: 'mc', title: '알맞은 응답 고르기', guide: '대화의 흐름에 맞는 응답을 고르세요.', items: [
      { q: '다음 말에 이어질 응답으로 가장 알맞은 것은?<br><b>A: You look upset. What\'s the matter?</b>', opts: ['I broke a flower pot.', 'I\'m sorry to hear that.', 'Don\'t worry.', 'You are right.'], ex: '정답 ▶ I broke a flower pot.\n이유: What\'s the matter?(무슨 일 있니?)에는 → 안 좋은 일이나 걱정거리를 말해요.' },
      { q: '다음 말에 이어질 응답으로 가장 알맞은 것은?<br><b>A: I\'m worried about my dog. He isn\'t eating a lot.</b>', opts: ['I\'m sorry to hear that.', 'Sounds delicious!', 'Yes, please.', 'Good for you.'], ex: '정답 ▶ I\'m sorry to hear that.\n이유: 걱정을 들으면 → 위로 I\'m sorry to hear that. / Don\'t worry.\n오답 ▶ Good for you.(잘됐다)는 좋은 소식에 하는 말' }
    ] },
    { type: 'mc', title: '일치·불일치', guide: '선택지는 본문을 어려운 어휘로 바꿔 쓴 문장이에요. 풀고 나서 해설의 어휘를 꼭 확인하세요.', items: [
      { box: ['5과 대화 1 · 깨진 화분 (Listen and Circle)', '5과 대화 2 · 강아지 걱정 (Listen and Circle)', '5과 대화 3 · 동생 걱정 (Listen and Circle)'], q: '대화의 내용과 일치하지 <u>않는</u> 것은?', opts: ['The girl\'s brother plays outside too much.', 'The girl broke a flower pot in the garden.', 'The dad says they can clean the garden together.', 'Isaac is worried about his dog.', 'The girl thinks Isaac\'s dog needs to see an animal doctor.'], ex: '정답 ▶ The girl\'s brother plays outside too much.\n이유: 동생은 비디오 게임을 너무 많이 해요. 그래서 밖에서 같이 놀아 주라는 조언을 들었어요.', per: [['소녀의 남동생은 밖에서 너무 많이 논다.', 'He plays video games too much', '불일치 → 게임을 너무 많이 함'], ['소녀는 정원에서 화분을 깼다.', 'I broke a flower pot in the garden', '일치'], ['아빠는 함께 정원을 치우면 된다고 말한다.', 'We can clean the garden together', '일치'], ['Isaac은 자기 개를 걱정한다.', 'I\'m worried about my dog', '일치'], ['소녀는 Isaac의 개가 동물 병원에 가야 한다고 생각한다.', 'He needs to go to the animal hospital', '일치']] }
    ] },
    { type: 'pick', title: '어법선택', guide: '어법상 알맞은 것을 고르세요.', items: [
      { s: 'I {broke|breaked} a flower pot in the garden. I\'m sorry, Dad.', ex: '정답 ▶ broke\n이유: break의 과거형은 불규칙 broke (break - broke - broken)' },
      { s: 'I\'m worried {about|of} my dog. He isn\'t eating a lot these days.', ex: '정답 ▶ about\n이유: be worried about ~ = ~을 걱정하다 (짝꿍 전치사 about)' },
      { s: 'I\'m worried about my dog. He {isn\'t|doesn\'t} eating a lot these days.', ex: '정답 ▶ isn\'t\n이유: 현재진행형의 부정 = be동사 + not + -ing. doesn\'t 뒤에는 동사원형이 와요.' },
      { s: 'Why don\'t you {play|playing} with him outside? That can help.', ex: '정답 ▶ play\n이유: Why don\'t you + 동사원형 ~? = ~하는 게 어때? (제안)' }
    ] },
    { type: 'scramble', title: '본문 스크램블', guide: '우리말에 맞게 단어를 눌러 문장을 완성하세요.', items: [
      { ko: '정원을 같이 치우면 돼.', en: 'We can clean the garden together.' },
      { ko: '동물 병원에 가 봐야 할 것 같아.', en: 'He needs to go to the animal hospital.' }
    ] },
    { type: 'order', title: '문장순서', guide: '대화(문장)를 순서대로 눌러서 배열하세요.', items: [
      { lines: ['I\'m worried about my little brother. He plays video games too much.', 'Why don\'t you play with him outside? That can help.', 'You are right. I\'ll play soccer with him on weekends.'], flow: ['G: 남동생이 게임을 너무 많이 해서 걱정돼', 'B: 밖에서 같이 노는 게 어때?', 'G: 맞아, 주말마다 축구를 할게'] }
    ] },
    { type: 'blank', title: '빈칸추론', guide: '빈칸에 들어갈 말로 가장 알맞은 것을 고르세요.', items: [
      { s: 'I\'m worried about my dog. He isn\'t eating a lot these ____.', opts: ['days', 'years', 'times', 'pots'], ex: '정답 ▶ days\n이유: these days = 요즘' },
      { s: 'You are right. I\'ll play ____ with him on weekends.', opts: ['soccer', 'video games', 'the piano', 'computer games'], ex: '정답 ▶ soccer\n이유: 게임 대신 \'밖에서\' 함께 놀라는 조언 → 축구를 할게\n오답 ▶ video/computer games는 걱정거리 그 자체예요.' }
    ] },
    { type: 'mc', title: '어색한 대화 고르기', guide: '짝지어진 대화 중 어색한 것을 고르세요.', items: [
      { q: '다음 중 짝지어진 대화가 <b>어색한</b> 것은?', opts: ['A: I broke my leg. B: That sounds great!', 'A: What\'s the matter? B: I have a bad cold.', 'A: I\'m worried about my test. B: Don\'t worry. You\'ll do well.', 'A: Are you okay? B: I\'m worried about my cat.'], ex: '정답 ▶ A: I broke my leg. B: That sounds great!\n이유: 다리가 부러졌다는 말에는 I\'m sorry to hear that.처럼 위로해야 해요.' }
    ] },
    { type: 'mc', title: '의사소통 기능', guide: '상황에 맞는 표현을 고르세요.', items: [
      { q: '걱정을 표현하는 말로 알맞은 것은?', opts: ['I\'m worried about my dog.', 'What\'s the matter?', 'Don\'t worry.', 'I\'m sorry to hear that.'], ex: '정답 ▶ I\'m worried about my dog.\n이유: I\'m worried about ~ = ~이 걱정돼 (걱정 표현)\n오답 ▶ What\'s the matter?(묻기) / Don\'t worry.(위로) / I\'m sorry to hear that.(위로)' },
      { q: '무슨 일인지 묻는 표현이 <b>아닌</b> 것은?', opts: ['What\'s your hobby?', 'What\'s wrong?', 'What\'s the problem?', 'Is there anything wrong?'], ex: '정답 ▶ What\'s your hobby?\n이유: \'취미가 뭐니?\'는 취미를 묻는 말이에요. 나머지는 모두 What\'s the matter?와 같은 뜻이에요.' }
    ] },
    { type: 'mc', title: '요약문 완성', guide: '본문을 읽고 요약문의 빈칸 (A), (B)에 들어갈 말을 고르세요.', items: [
      { n: null, box: ['5과 대화 1 · 깨진 화분 (Listen and Circle)'], q: '다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 알맞은 것은?<br><b>The girl (A) ______ a flower pot, but her dad told her not to (B) ______.</b>', opts: ['(A) broke – (B) worry', '(A) bought – (B) worry', '(A) broke – (B) clean', '(A) sold – (B) cry', '(A) made – (B) worry'], ex: '정답 ▶ (A) broke – (B) worry\n(A) 화분을 \'깼다\' → broke\n(B) 아빠: \'걱정하지 마\' → not to worry\n오답 ▶ clean: 아빠는 오히려 같이 치우자고 했어요.', ev: ['I broke a flower pot in the garden', 'Oh, don\'t worry'] },
      { n: null, box: ['5과 대화 2 · 강아지 걱정 (Listen and Circle)', '5과 대화 3 · 동생 걱정 (Listen and Circle)'], q: '다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 알맞은 것은?<br><b>Isaac\'s dog isn\'t eating a lot, and the girl\'s brother plays (A) ______ too much, so she will play (B) ______ with him.</b>', opts: ['(A) video games – (B) soccer', '(A) soccer – (B) video games', '(A) video games – (B) the piano', '(A) basketball – (B) soccer', '(A) the guitar – (B) chess'], ex: '정답 ▶ (A) video games – (B) soccer\n(A) 동생은 \'비디오 게임\'을 너무 많이 함 → video games\n(B) 주말마다 함께 \'축구\' → soccer\n오답 ▶ ②는 두 낱말을 바꾼 함정!', ev: ['He plays video games too much', 'I\'ll play soccer with him on weekends'] }
    ] }
  ] },
  { id: 'k5b', name: 'DAY 6', range: '5과 대화문 ② 대화 4·클립', story: 'Lesson 5 · 농구 경기 걱정 · 걱정 인형', passage: [['#', '5과 대화 4 · 농구 경기 걱정 (In Everyday Life)', ''], ['Eric', 'What\'s the matter, Bomin?', '보민아, 무슨 일이야?'], ['Bomin', 'I\'m too nervous about tomorrow\'s basketball game, Eric.', '내일 농구 경기 때문에 너무 긴장돼, Eric.'], ['Eric', 'I feel just like you, but we practiced a lot.', '나도 너와 같은 기분이지만, 우리 연습 많이 했잖아.'], ['Bomin', 'I missed the ball many times during the last game. So I\'m worried about tomorrow\'s game.', '나는 지난 경기 때 공을 여러 번 놓쳤어. 그래서 내일 경기가 걱정돼.'], ['Eric', 'Don\'t worry. We all learn from our mistakes. You\'ll do better this time.', '걱정하지 마. 우리 모두 실수에서 배우는 거야. 너는 이번에는 더 잘할 거야.'], ['Bomin', 'Thanks, Eric. I feel better now.', '고마워, Eric. 이제 기분이 훨씬 나아졌어.'], ['#', '5과 클립 · 걱정 인형 (Enjoy the Clip)', ''], ['Maria', 'Hi, I\'m Maria from Guatemala.', '안녕, 나는 과테말라에서 온 Maria야.'], ['Maria', 'In my country, many children have worry dolls.', '우리나라에서는 많은 어린이가 걱정 인형을 가지고 있어.'], ['Maria', 'Look at my worry doll.', '내 걱정 인형을 봐.'], ['Maria', 'I tell her about my worries and keep her under my pillow.', '나는 내 걱정 인형에게 말하고, 베개 밑에 보관해.'], ['Maria', 'Like this.', '이렇게.'], ['Maria', 'Now I\'m worried about the weather on my camp day next week.', '지금 나는 다음 주 캠핑 날의 날씨가 걱정돼.'], ['Maria', 'So I\'ll tell her about it.', '그래서 그것에 대해 인형에게 이야기할 거야.'], ['Maria', 'During the night, she will take away my worries!', '밤 동안 인형이 내 걱정을 가져갈 거야!']], steps: [
    { type: 'vocab', title: '핵심어휘·숙어', quizN: 15, items: [['nervous', '긴장한'], ['tomorrow\'s', '내일의'], ['feel just like you', '너와 똑같이 느끼다'], ['practice', '연습하다'], ['miss', '놓치다'], ['many times', '여러 번'], ['during', '~ 동안'], ['learn from', '~에서 배우다'], ['mistake', '실수'], ['do better', '더 잘하다'], ['feel better', '기분이 나아지다'], ['country', '나라'], ['worry doll', '걱정 인형'], ['pillow', '베개'], ['weather', '날씨'], ['camp day', '캠핑 날'], ['take away', '가져가다, 없애 주다']] },
    { type: 'pick', title: '어휘선택', guide: '문맥에 맞는 낱말을 고르세요.', items: [
      { s: 'Don\'t worry. We all learn from our {mistakes|games}. You\'ll do better this time.', ex: '정답 ▶ mistakes (실수)\n오답 ▶ games: 공을 여러 번 놓친 보민이에게 → \'실수에서 배운다\'고 위로해요.' },
      { s: 'I tell her about my worries and keep her under my {pillow|desk}.', ex: '정답 ▶ pillow (베개)\n오답 ▶ desk: 밤 동안(During the night) 걱정을 가져가는 인형 → 잘 때 \'베개\' 밑에 둬요.' },
      { s: 'Now I\'m worried about the {weather|food} on my camp day next week.', ex: '정답 ▶ weather (날씨)\n오답 ▶ food: 캠핑 날에 걱정되는 것 → \'날씨\'' }
    ] },
    { type: 'tf', title: 'T/F 내용 확인', guide: '본문 내용과 일치하면 T, 다르면 F를 고르세요.', items: [['Bomin is nervous about tomorrow\'s soccer game.', false, '정답 ▶ F\n이유: 축구가 아니라 농구 경기(basketball game)예요.', null, 'I\'m too nervous about tomorrow\'s basketball game'], ['Eric and Bomin practiced a lot.', true, '정답 ▶ T\n이유: we practiced a lot', null, 'we practiced a lot'], ['Bomin still feels bad at the end.', false, '정답 ▶ F\n이유: 마지막에 I feel better now. 기분이 나아졌다고 해요.', null, 'I feel better now'], ['Maria keeps her worry doll under her pillow.', true, '정답 ▶ T\n이유: keep her under my pillow', null, 'keep her under my pillow'], ['Maria is worried about her test.', false, '정답 ▶ F\n이유: 시험이 아니라 다음 주 캠핑 날의 날씨(the weather)가 걱정이에요.', null, 'Now I\'m worried about the weather on my camp day next week']] },
    { type: 'mc', title: '알맞은 응답 고르기', guide: '대화의 흐름에 맞는 응답을 고르세요.', items: [
      { q: '다음 말에 이어질 응답으로 가장 알맞은 것은?<br><b>A: What\'s the matter, Bomin?</b>', opts: ['I\'m too nervous about tomorrow\'s game.', 'I feel better now.', 'You\'ll do better this time.', 'Thanks, Eric.'], ex: '정답 ▶ I\'m too nervous about tomorrow\'s game.\n이유: 무슨 일인지 물으면(What\'s the matter?) → 걱정이나 문제를 말해요.' },
      { q: '다음 말에 이어질 응답으로 가장 알맞은 것은?<br><b>A: Don\'t worry. You\'ll do better this time.</b>', opts: ['Thanks. I feel better now.', 'I\'m sorry to hear that.', 'What\'s the matter?', 'Yes, please.'], ex: '정답 ▶ Thanks. I feel better now.\n이유: 위로를 받으면 → 고맙다고 하며 기분이 나아졌다고 답해요.' }
    ] },
    { type: 'mc', title: '일치·불일치', guide: '선택지는 본문을 어려운 어휘로 바꿔 쓴 문장이에요. 풀고 나서 해설의 어휘를 꼭 확인하세요.', items: [
      { box: ['5과 대화 4 · 농구 경기 걱정 (In Everyday Life)'], q: '대화의 내용과 일치하지 <u>않는</u> 것은?', opts: ['Bomin feels worse after talking with Eric.', 'Bomin has a basketball game tomorrow.', 'Eric feels nervous, too.', 'Eric and Bomin practiced a lot.', 'Bomin missed the ball many times in the last game.'], ex: '정답 ▶ Bomin feels worse after talking with Eric.\n이유: Eric의 위로를 듣고 I feel better now.(기분이 나아졌어)라고 했어요.', per: [['보민이는 Eric과 이야기한 뒤 기분이 더 나빠졌다.', 'I feel better now', '불일치 → 나아짐'], ['보민이는 내일 농구 경기가 있다.', 'I\'m too nervous about tomorrow\'s basketball game', '일치'], ['Eric도 긴장된다.', 'I feel just like you', '일치'], ['둘은 연습을 많이 했다.', 'we practiced a lot', '일치'], ['보민이는 지난 경기에서 공을 여러 번 놓쳤다.', 'I missed the ball many times during the last game', '일치']] },
      { box: ['5과 클립 · 걱정 인형 (Enjoy the Clip)'], q: '클립의 내용과 일치하지 <u>않는</u> 것은?', opts: ['Maria\'s camp day is tomorrow.', 'Maria is from Guatemala.', 'Many children in her country have worry dolls.', 'Maria tells her doll about her worries.', 'Maria is worried about the weather on her camp day.'], ex: '정답 ▶ Maria\'s camp day is tomorrow.\n이유: 캠핑 날은 내일이 아니라 다음 주(next week)예요.', per: [['Maria의 캠핑 날은 내일이다.', 'on my camp day next week', '불일치 → 다음 주'], ['Maria는 과테말라 출신이다.', 'Hi, I\'m Maria from Guatemala', '일치'], ['그 나라의 많은 어린이가 걱정 인형을 가지고 있다.', 'many children have worry dolls', '일치'], ['Maria는 인형에게 걱정을 이야기한다.', 'I tell her about my worries', '일치'], ['Maria는 캠핑 날의 날씨를 걱정한다.', 'I\'m worried about the weather on my camp day', '일치']] }
    ] },
    { type: 'pick', title: '어법선택', guide: '어법상 알맞은 것을 고르세요.', items: [
      { s: 'I feel just like you, but we {practiced|practice} a lot.', ex: '정답 ▶ practiced\n이유: 경기 전까지 이미 \'연습했다\' → 과거형 practiced' },
      { s: 'Don\'t worry. We all learn from our mistakes. You\'ll {do|doing} better this time.', ex: '정답 ▶ do\n이유: You\'ll = You will. 조동사 will + 동사원형' },
      { s: 'In my country, many {children|child} have worry dolls.', ex: '정답 ▶ children\n이유: many + 셀 수 있는 명사의 복수형. child의 복수형은 불규칙 children' },
      { s: '{During|For} the night, she will take away my worries!', ex: '정답 ▶ During\n이유: during + 특정 기간(the night, the game) = ~ 동안. for + 기간의 길이(an hour, two days)' }
    ] },
    { type: 'scramble', title: '본문 스크램블', guide: '우리말에 맞게 단어를 눌러 문장을 완성하세요.', items: [
      { ko: '우리 모두 실수에서 배우는 거야.', en: 'We all learn from our mistakes.' },
      { ko: '나는 내 걱정 인형에게 말하고, 베개 밑에 보관해.', en: 'I tell her about my worries and keep her under my pillow.' }
    ] },
    { type: 'order', title: '문장순서', guide: '대화(문장)를 순서대로 눌러서 배열하세요.', items: [
      { lines: ['What\'s the matter, Bomin?', 'I\'m too nervous about tomorrow\'s basketball game, Eric.', 'I feel just like you, but we practiced a lot.', 'I missed the ball many times during the last game. So I\'m worried about tomorrow\'s game.'], flow: ['Eric: 무슨 일이야?', 'Bomin: 내일 농구 경기 때문에 너무 긴장돼', 'Eric: 나도 그래, 하지만 연습 많이 했잖아', 'Bomin: 지난번에 공을 많이 놓쳐서 걱정돼'] }
    ] },
    { type: 'blank', title: '빈칸추론', guide: '빈칸에 들어갈 말로 가장 알맞은 것을 고르세요.', items: [
      { s: 'I missed the ____ many times during the last game. So I\'m worried about tomorrow\'s game.', opts: ['ball', 'bus', 'class', 'test'], ex: '정답 ▶ ball\n이유: 농구 경기 이야기 → \'공\'을 여러 번 놓쳤다' },
      { s: 'During the night, she will take away my ____!', opts: ['worries', 'dolls', 'pillows', 'dreams'], ex: '정답 ▶ worries\n이유: \'걱정 인형\'은 밤 동안 \'걱정\'을 가져가 줘요.' }
    ] },
    { type: 'mc', title: '어색한 대화 고르기', guide: '짝지어진 대화 중 어색한 것을 고르세요.', items: [
      { q: '다음 중 짝지어진 대화가 <b>어색한</b> 것은?', opts: ['A: I\'m worried about my grandma. B: Sounds fun!', 'A: What\'s wrong? B: I lost my bag.', 'A: I\'m nervous about the test. B: Don\'t worry. You\'ll do well.', 'A: Thanks. I feel better now. B: Glad to hear that.'], ex: '정답 ▶ A: I\'m worried about my grandma. B: Sounds fun!\n이유: 걱정을 말하는 친구에게 \'재미있겠다!\'는 어색해요. → I\'m sorry to hear that. / Don\'t worry.' }
    ] },
    { type: 'mc', title: '의사소통 기능', guide: '상황에 맞는 표현을 고르세요.', items: [
      { q: '밑줄 친 말과 의미가 같은 것은?<br><b>Eric: <u>What\'s the matter</u>, Bomin?</b>', opts: ['What\'s wrong', 'What\'s your name', 'What time is it', 'What do you want'], ex: '정답 ▶ What\'s wrong\n이유: What\'s the matter? = What\'s wrong? = What\'s the problem? (무슨 일이야?)' }
    ] },
    { type: 'mc', title: '요약문 완성', guide: '본문을 읽고 요약문의 빈칸 (A), (B)에 들어갈 말을 고르세요.', items: [
      { n: null, box: ['5과 대화 4 · 농구 경기 걱정 (In Everyday Life)'], q: '다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 알맞은 것은?<br><b>Bomin was worried after (A) ______ the ball many times, but Eric said we all learn from our (B) ______.</b>', opts: ['(A) missing – (B) mistakes', '(A) catching – (B) mistakes', '(A) missing – (B) friends', '(A) kicking – (B) games', '(A) throwing – (B) teachers'], ex: '정답 ▶ (A) missing – (B) mistakes\n(A) 공을 여러 번 \'놓쳐서\' 걱정 → missing\n(B) 우리 모두 \'실수\'에서 배운다 → mistakes', ev: ['I missed the ball many times during the last game', 'We all learn from our mistakes'] },
      { n: null, box: ['5과 클립 · 걱정 인형 (Enjoy the Clip)'], q: '다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 알맞은 것은?<br><b>Maria tells her worry doll about her (A) ______, and the doll will take them (B) ______ during the night.</b>', opts: ['(A) worries – (B) away', '(A) dreams – (B) away', '(A) worries – (B) back', '(A) toys – (B) out', '(A) friends – (B) home'], ex: '정답 ▶ (A) worries – (B) away\n(A) 인형에게 \'걱정\'을 말한다 → worries\n(B) 밤 동안 걱정을 \'가져간다\' → take away', ev: ['I tell her about my worries', 'she will take away my worries'] }
    ] }
  ] },
  { id: 'L5a', name: 'DAY 7', range: '5과 본문 ❶❷', story: 'Lesson 5 · 가장 작은 El과 Jo · 학교 마지막 날, 꽃 없는 화분', passage: [['', '❶', ''], ['', 'El and Jo were the smallest students in the class.', 'El과 Jo는 반에서 가장 작은 학생들이었다.'], ['', 'They were always together.', '그들은 항상 함께였다.'], ['', 'They even watered the plants together in the class because they could not reach the pots alone.', '그들은 혼자서는 화분에 손이 닿지 않았기 때문에 교실에서 식물에 물도 함께 주었다.'], ['', 'However, in the spring, something was DIFFERENT.', '하지만 봄이 되자 무언가가 달라졌다.'], ['', 'Jo grew TALLER!', 'Jo의 키가 더 커졌다!'], ['', 'Jo was taller than El, so Jo could water the plants alone.', 'Jo는 El보다 키가 더 컸고, 그래서 혼자서 식물에 물을 줄 수 있었다.'], ['', 'El felt smaller every day.', 'El은 매일 더 작아지는 기분이었다.'], ['', '❷', ''], ['', 'On the last day of school, Mr. Diaz said, "Class, you can take a flower home and care for it over the summer."', '학교 마지막 날, Diaz 선생님이 말씀하셨다. "여러분, 꽃을 하나 집에 가져가서 여름 동안 돌보세요."'], ['', 'All the students ran to the window.', '모든 학생이 창문으로 달려갔다.'], ['', 'El\'s classmates reached for the pots over tiny El.', 'El의 반 친구들은 작은 El 너머로 화분에 손을 뻗었다.'], ['', 'They took all the pots with colorful flowers.', '그들은 알록달록한 꽃이 있는 화분을 모두 가져갔다.'], ['', 'El took the last pot.', 'El은 마지막 화분을 가져갔다.'], ['', 'It had the smallest plant with no flowers.', '그 화분에는 꽃이 없는 가장 작은 식물이 있었다.'], ['', '"I feel just like you, little plant," said El.', '"나도 꼭 너 같은 기분이야, 작은 식물아." El이 말했다.'], ['', 'Mr. Diaz looked at El and said, "That\'s an aster plant. In time, it\'ll grow and have beautiful flowers."', 'Diaz 선생님이 El을 보며 말씀하셨다. "그건 과꽃이란다. 시간이 지나면 자라서 아름다운 꽃을 피울 거야."'], ['', '"But it\'s just a little green plant," said El.', '"하지만 그냥 작은 초록 식물일 뿐인걸요." El이 말했다.'], ['', 'She was not so sure.', '그녀는 그다지 확신하지 못했다.'], ['', '"You can have my zinnia plant," Jo said to El, "I\'ll be at my grandma\'s all summer."', '"내 백일홍을 가져도 돼." Jo가 El에게 말했다. "나는 여름 내내 할머니 댁에 있을 거야."'], ['', '"I\'ll plant my aster and your zinnia side by side," El said.', '"내 과꽃과 네 백일홍을 나란히 심을게." El이 말했다.'], ['', '"They\'ll be good friends — just like us!" said Jo.', '"그 둘은 좋은 친구가 될 거야, 꼭 우리처럼!" Jo가 말했다.'], ['', 'El smiled.', 'El은 미소 지었다.']], steps: [
    { type: 'vocab', title: '핵심어휘·숙어', quizN: 15, items: [['smallest', '가장 작은 (small - smaller - smallest)', '❶'], ['always', '항상', '❶'], ['together', '함께', '❶'], ['even', '심지어, ~도', '❶'], ['water', '물을 주다; 물', '❶'], ['plant', '식물; 심다', '❶'], ['reach', '~에 닿다', '❶'], ['pot', '화분', '❶'], ['alone', '혼자서', '❶'], ['however', '하지만', '❶'], ['different', '다른, 달라진', '❶'], ['grow', '자라다 (grow - grew - grown)', '❶'], ['taller', '키가 더 큰', '❶'], ['feel', '느끼다 (feel - felt - felt)', '❶'], ['last', '마지막의', '❷'], ['take ~ home', '~을 집에 가져가다', '❷'], ['care for', '~을 돌보다', '❷'], ['over the summer', '여름 동안', '❷'], ['classmate', '반 친구', '❷'], ['reach for', '~에 손을 뻗다', '❷'], ['tiny', '아주 작은', '❷'], ['colorful', '알록달록한', '❷'], ['look at', '~을 보다', '❷'], ['aster', '과꽃', '❷'], ['in time', '시간이 지나면, 머지않아', '❷'], ['sure', '확신하는', '❷'], ['zinnia', '백일홍', '❷'], ['all summer', '여름 내내', '❷'], ['side by side', '나란히', '❷'], ['smile', '미소 짓다', '❷']] },
    { type: 'pick', title: '어휘선택', guide: '문맥에 맞는 낱말을 고르세요.', items: [
      { s: 'They were always {together|alone}.', ex: '정답 ▶ together (함께)\n오답 ▶ alone (혼자): 바로 뒤에 식물에 물도 \'함께(together)\' 주었다고 나와요. 늘 함께 다니는 단짝이에요.' },
      { s: 'They even watered the plants together in the class because they could not reach the pots {alone|together}.', ex: '정답 ▶ alone (혼자서)\n오답 ▶ together: 둘 다 키가 작아 \'혼자서는\' 화분에 손이 닿지 않아서 함께 물을 줬어요.' },
      { s: 'El felt {smaller|bigger} every day.', ex: '정답 ▶ smaller (더 작은)\n오답 ▶ bigger (더 큰): Jo는 키가 커졌는데 El은 그대로라 매일 \'더 작아지는\' 기분이었어요.' },
      { s: 'El\'s classmates reached for the pots over {tiny|tall} El.', ex: '정답 ▶ tiny (아주 작은)\n오답 ▶ tall (키가 큰): 반 친구들이 \'작은\' El 머리 위로 손을 뻗어 화분을 가져갔어요.' },
      { s: 'They took all the pots with {colorful|no} flowers.', ex: '정답 ▶ colorful (알록달록한)\n오답 ▶ no: 친구들은 \'알록달록한 꽃이 있는\' 화분을 다 가져갔고, El에게는 \'꽃이 없는(with no flowers)\' 화분만 남았어요.' },
      { s: 'El took the {last|first} pot.', ex: '정답 ▶ last (마지막의)\n오답 ▶ first (첫 번째의): 친구들이 다 가져간 뒤 El은 \'마지막\' 화분을 가져갔어요.' },
      { s: '"I\'ll plant my aster and your zinnia {side by side|far apart}," El said.', ex: '정답 ▶ side by side (나란히)\n오답 ▶ far apart (멀리 떨어뜨려): 바로 다음에 \'둘은 좋은 친구가 될 거야\'라고 해요. 나란히 심어요.' },
      { s: '"They\'ll be good {friends|enemies} — just like us!" said Jo.', ex: '정답 ▶ friends (친구들)\n오답 ▶ enemies (적들): \'just like us(꼭 우리처럼)\' → 단짝인 El과 Jo처럼 \'좋은 친구\'가 될 거래요.' },
      { s: 'El {smiled|cried}.', ex: '정답 ▶ smiled (미소 지었다)\n오답 ▶ cried (울었다): 친구의 따뜻한 말에 El은 \'미소\' 지었어요.' }
    ] },
    { type: 'tf', title: 'T/F 내용 확인', guide: '본문 내용과 일치하면 T, 다르면 F를 고르세요.', items: [['El and Jo were the tallest students in the class.', false, '정답 ▶ F\n이유: 가장 키가 큰(tallest)이 아니라 가장 작은(smallest) 학생들이었어요.', '❶', 'El and Jo were the smallest students in the class'], ['El and Jo watered the plants together.', true, '정답 ▶ T\n이유: 혼자서는 화분에 닿지 않아 함께 물을 줬어요.', '❶', 'They even watered the plants together'], ['In the spring, El grew taller than Jo.', false, '정답 ▶ F\n이유: 봄에 키가 커진 사람은 Jo예요. Jo가 El보다 더 컸어요.', '❶', 'Jo was taller than El'], ['Mr. Diaz let the students take a flower home.', true, '정답 ▶ T\n이유: \'you can take a flower home\' → 꽃을 집에 가져가도 된다고 했어요.\n어휘 ▶ let ~하게 해 주다', '❷', 'you can take a flower home'], ['El took a pot with colorful flowers.', false, '정답 ▶ F\n이유: El은 꽃이 없는(with no flowers) 가장 작은 식물이 있는 마지막 화분을 가져갔어요.', '❷', 'It had the smallest plant with no flowers'], ['Mr. Diaz said El\'s plant would have beautiful flowers.', true, '정답 ▶ T\n이유: 시간이 지나면 자라서 아름다운 꽃을 피울 거라고 했어요.', '❷', 'it\'ll grow and have beautiful flowers'], ['Jo gave El her zinnia plant.', true, '정답 ▶ T\n이유: \'You can have my zinnia plant\' → 내 백일홍을 가져도 된다고 했어요.', '❷', 'You can have my zinnia plant'], ['Jo stayed at home all summer.', false, '정답 ▶ F\n이유: Jo는 여름 내내 할머니 댁(my grandma\'s)에 있을 거라고 했어요.', '❷', 'I\'ll be at my grandma\'s all summer']] },
    { type: 'mc', title: '일치·불일치', guide: '선택지는 본문을 어려운 어휘로 바꿔 쓴 문장이에요. 풀고 나서 해설의 어휘를 꼭 확인하세요.', items: [
      { n: '❶', box: ['❶'], q: '글의 내용과 일치하지 <u>않는</u> 것은?', opts: ['El was taller than Jo in the spring.', 'El and Jo were always together.', 'They couldn\'t reach the pots alone.', 'Jo grew taller in the spring.', 'El felt smaller every day.'], ex: '정답 ▶ El was taller than Jo in the spring.\n이유: 봄에는 Jo가 El보다 더 컸어요(Jo was taller than El).', per: [['봄에 El이 Jo보다 키가 컸다.', 'Jo was taller than El', '불일치 → Jo가 더 큼'], ['El과 Jo는 항상 함께였다.', 'They were always together', '일치'], ['그들은 혼자서는 화분에 닿을 수 없었다.', 'they could not reach the pots alone', '일치'], ['봄에 Jo의 키가 커졌다.', 'Jo grew TALLER', '일치'], ['El은 매일 더 작아지는 기분이었다.', 'El felt smaller every day', '일치']] },
      { n: '❷', box: ['❷'], q: '글의 내용과 <u>일치하는</u> 것은?', opts: ['El\'s plant had no flowers at first.', 'El took the first pot.', 'Mr. Diaz said El\'s plant would never grow.', 'Jo will stay at El\'s house all summer.', 'El was sure that her plant would have flowers.'], ex: '정답 ▶ El\'s plant had no flowers at first.\n이유: It had the smallest plant with no flowers.\n어휘 ▶ at first 처음에는', per: [['El의 식물은 처음에 꽃이 없었다.', 'It had the smallest plant with no flowers', '일치'], ['El은 첫 번째 화분을 가져갔다.', 'El took the last pot', '불일치 → 마지막 화분'], ['선생님은 El의 식물이 절대 자라지 않을 거라고 했다.', 'it\'ll grow and have beautiful flowers', '불일치 → 자랄 것'], ['Jo는 여름 내내 El의 집에 있을 것이다.', 'I\'ll be at my grandma\'s all summer', '불일치 → 할머니 댁'], ['El은 자기 식물에 꽃이 필 거라고 확신했다.', 'She was not so sure', '불일치 → 확신하지 못함']] }
    ] },
    { type: 'pick', title: '어법선택', guide: '어법상 알맞은 것을 고르세요.', items: [
      { s: 'El and Jo were the {smallest|smaller} students in the class.', ex: '정답 ▶ smallest\n이유: \'반에서(in the class)\' 여럿 중 가장 → 최상급 the + -est\n오답 ▶ smaller는 둘을 비교할 때 (than과 함께)' },
      { s: 'El and Jo {were|was} the smallest students in the class.', ex: '정답 ▶ were\n이유: 주어 El and Jo(두 사람 → 복수) + 과거 → were' },
      { s: 'They even watered the plants together in the class because they could not {reach|reaching} the pots alone.', ex: '정답 ▶ reach\n이유: 조동사 could 뒤에는 동사원형!' },
      { s: 'Jo was taller {than|then} El, so Jo could water the plants alone.', ex: '정답 ▶ than\n이유: 비교급 + than = ~보다 더 …한. then(그때, 그러고 나서)과 철자 헷갈리지 마세요!' },
      { s: 'Jo was taller than El, {so|because} Jo could water the plants alone.', ex: '정답 ▶ so\n이유: 키가 더 컸다(원인) → 그래서 혼자 물을 줄 수 있었다(결과) → so(그래서)\n오답 ▶ because는 뒤에 \'이유\'가 와요.' },
      { s: 'All the students {ran|run} to the window.', ex: '정답 ▶ ran\n이유: 지난 일 → 과거형. run - ran - run (불규칙)' },
      { s: 'On the last day of school, Mr. Diaz said, "Class, you can take a flower {home|to home} and care for it over the summer."', ex: '정답 ▶ home\n이유: home은 \'집으로\'라는 부사라 앞에 to를 쓰지 않아요. take ~ home = ~을 집에 가져가다 (go home, come home)' },
      { s: 'Mr. Diaz looked {at|to} El and said, "That\'s an aster plant. In time, it\'ll grow and have beautiful flowers."', ex: '정답 ▶ at\n이유: look at ~ = ~을 보다 (짝꿍 표현)' },
      { s: '"I\'ll {plant|planting} my aster and your zinnia side by side," El said.', ex: '정답 ▶ plant\n이유: I\'ll = I will. 조동사 will 뒤에는 동사원형!' },
      { s: 'She {was|were} not so sure.', ex: '정답 ▶ was\n이유: 주어 She(단수) + 과거 → was' }
    ] },
    { type: 'verb', title: '동사변형', guide: '( ) 안의 동사를 알맞은 형태로 바꿔 쓰세요.', items: [
      { s: 'El ___ smaller every day.', v: 'feel', a: ['felt'], ex: '정답 ▶ felt\n이유: feel - felt - felt (불규칙). feel + 형용사 = ~하게 느끼다' },
      { s: 'El ___ the last pot.', v: 'take', a: ['took'], ex: '정답 ▶ took\n이유: take - took - taken (불규칙)' },
      { s: 'It ___ the smallest plant with no flowers.', v: 'have', a: ['had'], ex: '정답 ▶ had\n이유: have - had - had' },
      { s: 'El\'s classmates ___ for the pots over tiny El.', v: 'reach', a: ['reached'], ex: '정답 ▶ reached\n이유: 규칙 변화 reach + -ed. reach for ~ = ~에 손을 뻗다' },
      { s: 'They even ___ the plants together in the class because they could not reach the pots alone.', v: 'water', a: ['watered'], ex: '정답 ▶ watered\n이유: water(물을 주다) + -ed → 과거형' },
      { s: 'El ___.', v: 'smile', a: ['smiled'], ex: '정답 ▶ smiled\n이유: e로 끝나는 동사는 -d만 붙여요 (smile → smiled)' }
    ] },
    { type: 'error', title: '오류찾기', guide: '어법상 틀린 곳을 고르세요.', items: [
      { s: 'Jo was [[more tall]] than El, so Jo [[could]] water the plants [[alone]].', w: 0, fix: 'taller', ex: '틀린 곳 ▶ ① more tall → taller\n이유: 짧은 형용사의 비교급은 -er (tall - taller - tallest). more는 긴 형용사에 (more beautiful)\n나머지 ▶ ② could + 동사원형 ✔ ③ alone ✔' },
      { s: 'They took all the [[pot]] with [[colorful]] flowers. El [[took]] the last pot.', w: 0, fix: 'pots', ex: '틀린 곳 ▶ ① pot → pots\n이유: all the + 복수 명사 (모든 ~들)\n나머지 ▶ ② colorful(형용사) ✔ ③ took(take의 과거) ✔' },
      { s: 'It [[had]] the [[small]] plant with [[no]] flowers.', w: 1, fix: 'smallest', ex: '틀린 곳 ▶ ② small → smallest\n이유: the + 최상급 → the smallest (가장 작은)\n나머지 ▶ ① had ✔ ③ with no flowers(꽃이 없는) ✔' },
      { s: '"But [[it\'s]] just a little green plant," said El. She [[were]] not so [[sure]].', w: 1, fix: 'was', ex: '틀린 곳 ▶ ② were → was\n이유: 주어 She(단수) → was\n나머지 ▶ ① it\'s = it is ✔ ③ sure(형용사, 확신하는) ✔' },
      { s: '[[They]] [[was]] always [[together]].', w: 1, fix: 'were', ex: '틀린 곳 ▶ ② was → were\n이유: They(복수) → were\n나머지 ▶ ① They(= El and Jo) ✔ ③ together ✔' }
    ] },
    { type: 'scramble', title: '본문 스크램블', guide: '우리말에 맞게 단어를 눌러 문장을 완성하세요.', items: [
      { ko: 'El은 매일 더 작아지는 기분이었다.', en: 'El felt smaller every day.' },
      { ko: '그들은 혼자서는 화분에 손이 닿지 않았기 때문에 교실에서 식물에 물도 함께 주었다.', en: 'They even watered the plants together in the class because they could not reach the pots alone.' },
      { ko: '모든 학생이 창문으로 달려갔다.', en: 'All the students ran to the window.' },
      { ko: 'El의 반 친구들은 작은 El 너머로 화분에 손을 뻗었다.', en: 'El\'s classmates reached for the pots over tiny El.' },
      { ko: '그들은 알록달록한 꽃이 있는 화분을 모두 가져갔다.', en: 'They took all the pots with colorful flowers.' },
      { ko: '그녀는 그다지 확신하지 못했다.', en: 'She was not so sure.' }
    ] },
    { type: 'order', title: '문장순서', guide: '문장을 본문 순서대로 눌러서 배열하세요.', items: [
      { lines: ['El and Jo were the smallest students in the class.', 'They were always together.', 'They even watered the plants together in the class because they could not reach the pots alone.', 'However, in the spring, something was DIFFERENT.'], flow: ['반에서 가장 작은 El과 Jo', '늘 함께였음', '물도 함께 줌', '봄에 무언가 달라짐'] },
      { lines: ['All the students ran to the window.', 'El\'s classmates reached for the pots over tiny El.', 'They took all the pots with colorful flowers.', 'El took the last pot.'], flow: ['모두 창문으로 달려감', '친구들이 El 너머로 손을 뻗음', '꽃이 있는 화분을 다 가져감', 'El은 마지막 화분'] },
      { lines: ['"But it\'s just a little green plant," said El.', 'She was not so sure.', '"You can have my zinnia plant," Jo said to El, "I\'ll be at my grandma\'s all summer."', '"I\'ll plant my aster and your zinnia side by side," El said.'], flow: ['그냥 작은 초록 식물일 뿐', 'El은 확신하지 못함', 'Jo: 내 백일홍 가져', 'El: 나란히 심을게'] }
    ] },
    { type: 'insert', title: '문장삽입', guide: '주어진 문장이 들어가기에 가장 알맞은 곳을 고르세요.', items: [
      { lines: ['However, in the spring, something was DIFFERENT.', 'Jo grew TALLER!', 'Jo was taller than El, so Jo could water the plants alone.'], given: 1, flow: ['봄에 무언가 달라짐', 'Jo의 키가 커졌음!', 'Jo가 El보다 커서 혼자 물을 줌'], ex: '정답 ▶ ①\n이유: \'무엇이 달라졌는지\' → Jo가 컸다 → 그래서 혼자 물을 줄 수 있었다, 순서로 이어져요.' },
      { lines: ['They took all the pots with colorful flowers.', 'El took the last pot.', 'It had the smallest plant with no flowers.'], given: 1, flow: ['친구들이 꽃 화분을 다 가져감', 'El은 마지막 화분을 가져감', '그것(It)에는 꽃 없는 가장 작은 식물'], ex: '정답 ▶ ①\n이유: It은 El이 가져간 \'마지막 화분\'이에요. 그 화분을 먼저 말해야 It이 이어져요.' },
      { lines: ['"You can have my zinnia plant," Jo said to El, "I\'ll be at my grandma\'s all summer."', '"I\'ll plant my aster and your zinnia side by side," El said.', '"They\'ll be good friends — just like us!" said Jo.'], given: 1, flow: ['Jo: 내 백일홍 가져', 'El: 과꽃과 백일홍을 나란히 심을게', 'Jo: 그 둘(They)은 좋은 친구가 될 거야'], ex: '정답 ▶ ①\n이유: They는 \'나란히 심은 과꽃과 백일홍\'이에요. 나란히 심겠다는 말이 바로 앞에 와야 해요.' }
    ] },
    { type: 'odd', title: '어색한 문장', guide: '글의 흐름과 관계없는 문장을 고르세요.', items: [
      { lines: ['They were always together.', 'They even watered the plants together in the class because they could not reach the pots alone.', 'El and Jo never helped each other in class.', 'However, in the spring, something was DIFFERENT.'], odd: 2, ex: '정답 ▶ ③\n이유: 둘은 늘 함께였고 물도 함께 줬어요. \'서로 돕지 않았다\'는 반대예요.' },
      { lines: ['El\'s classmates reached for the pots over tiny El.', 'They took all the pots with colorful flowers.', 'El took the pot with the most beautiful flowers.', 'El took the last pot.'], odd: 2, ex: '정답 ▶ ③\n이유: 친구들이 꽃 화분을 다 가져가서 El은 꽃 없는 마지막 화분을 가져갔어요.' },
      { lines: ['"I\'ll plant my aster and your zinnia side by side," El said.', '"They\'ll be good friends — just like us!" said Jo.', 'Jo didn\'t want El to have her zinnia.', 'El smiled.'], odd: 2, ex: '정답 ▶ ③\n이유: Jo가 먼저 백일홍을 가져가라고 했어요. 원하지 않았다는 건 반대예요.' }
    ] },
    { type: 'blank', title: '빈칸추론', guide: '빈칸에 들어갈 말로 가장 알맞은 것을 고르세요.', items: [
      { s: 'They even watered the plants together in the class because they could not reach the ____ alone.', opts: ['pots', 'window', 'students', 'door'], ex: '정답 ▶ pots\n이유: 식물에 물을 주려면 \'화분\'에 손이 닿아야 해요. 키가 작아서 혼자서는 닿지 않았어요.' },
      { s: 'Jo was taller than El, so Jo could water the plants ____.', opts: ['alone', 'together', 'slowly', 'never'], ex: '정답 ▶ alone\n이유: 키가 커져서 이제 \'혼자서\' 물을 줄 수 있었어요. 전에는 함께(together) 줬죠.' },
      { s: 'It had the smallest plant with ____ flowers.', opts: ['no', 'many', 'colorful', 'beautiful'], ex: '정답 ▶ no\n이유: 다른 친구들이 꽃 화분을 다 가져가서 \'꽃이 없는\' 식물만 남았어요.' }
    ] },
    { type: 'mc', title: '핵심문법', guide: '알맞은 답을 고르세요.', items: [
      { q: '비교급·최상급이 바르게 짝지어지지 <b>않은</b> 것은?', opts: ['big - biger - bigest', 'small - smaller - smallest', 'tall - taller - tallest', 'tiny - tinier - tiniest'], ex: '정답 ▶ big - biger - bigest\n이유: \'단모음 + 단자음\'으로 끝나면 자음을 한 번 더 써요 → big - bigger - biggest\n포인트 ▶ y로 끝나면 y → i (tiny - tinier - tiniest)' },
      { q: '빈칸에 들어갈 수 <b>없는</b> 것은?<br><b>Jo is ______ taller than El.</b>', opts: ['very', 'much', 'even', 'a lot'], ex: '정답 ▶ very\n이유: 비교급을 강조할 때는 much, even, a lot, far (훨씬). very는 비교급 앞에 못 써요.\n예 ▶ much taller(○) / very taller(✘)' },
      { q: '밑줄 친 <b>so</b>의 뜻으로 알맞은 것은?<br><b>Jo was taller than El, <u>so</u> Jo could water the plants alone.</b>', opts: ['그래서', '왜냐하면', '하지만', '그다음에'], ex: '정답 ▶ 그래서\n이유: 콤마 뒤 so + 문장 = 그래서 (결과)' },
      { q: '밑줄 친 부분의 뜻으로 알맞은 것은?<br><b>It had the smallest plant <u>with no flowers</u>.</b>', opts: ['꽃이 없는', '꽃과 함께', '꽃이 많은', '꽃을 가진'], ex: '정답 ▶ 꽃이 없는\n이유: with no + 명사 = ~이 없는 (with = ~이 있는)' },
      { q: '밑줄 친 부분을 풀어 쓴 것은?<br><b>In time, <u>it\'ll</u> grow and have beautiful flowers.</b>', opts: ['it will', 'it is', 'it was', 'it all'], ex: '정답 ▶ it will\n이유: \'ll = will (I\'ll = I will, they\'ll = they will). 앞으로 일어날 일' },
      { q: '밑줄 친 <b>They</b>가 가리키는 것은?<br><b>"I\'ll plant my aster and your zinnia side by side." "<u>They</u>\'ll be good friends!"</b>', opts: ['El의 과꽃과 Jo의 백일홍', 'El과 Jo', '반 친구들', 'Diaz 선생님과 El'], ex: '정답 ▶ El의 과꽃과 Jo의 백일홍\n이유: 나란히 심은 두 꽃이 \'El과 Jo처럼(just like us)\' 좋은 친구가 될 거라는 말이에요.' },
      { q: '다음 질문에 알맞은 대답은?<br><b>Why did El and Jo water the plants together?</b>', opts: ['Because they could not reach the pots alone.', 'Because Mr. Diaz told them to.', 'Because they had no water.', 'Because the plants were very big.'], ex: '정답 ▶ Because they could not reach the pots alone.\n이유: Why ~? → Because ~. 키가 작아 혼자서는 화분에 닿지 않았어요.' }
    ] },
    { type: 'mc', title: '요약문 완성', guide: '본문을 읽고 요약문의 빈칸 (A), (B)에 들어갈 말을 고르세요.', items: [
      { n: '❶', box: ['❶'], q: '다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 알맞은 것은?<br><b>El and Jo were the (A) ______ students in the class, but in the spring Jo grew (B) ______ than El.</b>', opts: ['(A) smallest – (B) taller', '(A) tallest – (B) taller', '(A) smallest – (B) smaller', '(A) tallest – (B) shorter', '(A) busiest – (B) older'], ex: '정답 ▶ (A) smallest – (B) taller\n(A) 반에서 \'가장 작은\' 학생들 → smallest\n(B) 봄에 Jo가 El보다 \'더 커짐\' → taller\n오답 ▶ tallest(가장 큰)는 반대, smaller는 Jo가 아니라 El의 기분이에요.', ev: ['El and Jo were the smallest students in the class', 'Jo was taller than El'] },
      { n: '❷', box: ['❷'], q: '다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 알맞은 것은?<br><b>El took the last pot with a tiny plant, but Mr. Diaz said it would (A) ______ and have (B) ______ flowers.</b>', opts: ['(A) grow – (B) beautiful', '(A) die – (B) beautiful', '(A) grow – (B) no', '(A) die – (B) no', '(A) stop – (B) small'], ex: '정답 ▶ (A) grow – (B) beautiful\n(A) 시간이 지나면 \'자라서\' → grow\n(B) \'아름다운\' 꽃을 피울 것 → beautiful\n오답 ▶ die(죽다)·stop(멈추다)·no(없는)는 선생님 말과 반대예요.', ev: ['it\'ll grow and have beautiful flowers'] }
    ] }
  ] },
  { id: 'L5b', name: 'DAY 8', range: '5과 본문 ❸', story: 'Lesson 5 · 여름 내내 자란 과꽃과 El', passage: [['', '❸', ''], ['', 'El planted the flowers in her garden.', 'El은 정원에 꽃들을 심었다.'], ['', 'It was growing season.', '식물이 자라는 시기였다.'], ['', 'All summer long, she cared for them.', '여름 내내 그녀는 그것들을 돌보았다.'], ['', 'On the last day of summer, Jo came to El\'s house.', '여름의 마지막 날, Jo가 El의 집에 왔다.'], ['', 'El and Jo ran to the garden and suddenly stopped.', 'El과 Jo는 정원으로 달려가다가 갑자기 멈췄다.'], ['', 'Something was DIFFERENT!', '무언가가 달라져 있었다!'], ['', 'There were flowers on the aster ... and El grew TALLER, TOO!', '과꽃에 꽃이 피어 있었다... 그리고 El도 키가 더 컸다!']], steps: [
    { type: 'vocab', title: '핵심어휘·숙어', quizN: 15, items: [['plant', '심다; 식물', '❸'], ['garden', '정원', '❸'], ['growing season', '식물이 자라는 시기', '❸'], ['all summer long', '여름 내내', '❸'], ['care for', '~을 돌보다', '❸'], ['last', '마지막의', '❸'], ['run', '달리다 (run - ran - run)', '❸'], ['suddenly', '갑자기', '❸'], ['stop', '멈추다', '❸'], ['different', '달라진, 다른', '❸'], ['aster', '과꽃', '❸'], ['grow taller', '키가 더 크다', '❸'], ['too', '~도, 또한', '❸']] },
    { type: 'pick', title: '어휘선택', guide: '문맥에 맞는 낱말을 고르세요.', items: [
      { s: 'El {planted|picked} the flowers in her garden.', ex: '정답 ▶ planted (심었다)\n오답 ▶ picked (꺾었다): 화분의 꽃들을 정원에 \'심고\' 여름 내내 돌봤어요.' },
      { s: 'All summer long, she {cared for|looked for} them.', ex: '정답 ▶ cared for (돌보았다)\n오답 ▶ looked for (찾았다): 여름 내내 꽃들을 \'돌봤어요\'.' },
      { s: 'El and Jo ran to the garden and {suddenly|slowly} stopped.', ex: '정답 ▶ suddenly (갑자기)\n오답 ▶ slowly (천천히): 달려가다가 달라진 모습을 보고 \'갑자기\' 멈췄어요.' },
      { s: 'There were {flowers|no flowers} on the aster ... and El grew TALLER, TOO!', ex: '정답 ▶ flowers\n이유: 무언가 달라졌다(DIFFERENT) → 꽃이 없던 과꽃에 \'꽃이 피었어요\'.' }
    ] },
    { type: 'tf', title: 'T/F 내용 확인', guide: '본문 내용과 일치하면 T, 다르면 F를 고르세요.', items: [['El planted the flowers at school.', false, '정답 ▶ F\n이유: 학교가 아니라 자기 집 정원(in her garden)에 심었어요.', '❸', 'El planted the flowers in her garden'], ['El took care of the flowers all summer.', true, '정답 ▶ T\n이유: All summer long, she cared for them.\n어휘 ▶ take care of = care for', '❸', 'All summer long, she cared for them'], ['Jo visited El on the first day of summer.', false, '정답 ▶ F\n이유: 여름의 첫날이 아니라 마지막 날(the last day)에 왔어요.', '❸', 'On the last day of summer, Jo came to El\'s house'], ['The aster had flowers at the end of summer.', true, '정답 ▶ T\n이유: 여름 마지막 날 과꽃에 꽃이 피어 있었어요.', '❸', 'There were flowers on the aster']] },
    { type: 'mc', title: '일치·불일치', guide: '선택지는 본문을 어려운 어휘로 바꿔 쓴 문장이에요. 풀고 나서 해설의 어휘를 꼭 확인하세요.', items: [
      { n: '❸', box: ['❸'], q: '글의 내용과 일치하지 <u>않는</u> 것은?', opts: ['El stopped caring for the flowers in July.', 'Jo came to El\'s house on the last day of summer.', 'El and Jo ran to the garden.', 'The aster had flowers.', 'El grew taller, too.'], ex: '정답 ▶ El stopped caring for the flowers in July.\n이유: 여름 내내(All summer long) 돌봤어요. 7월에 그만두지 않았어요.', per: [['El은 7월에 꽃 돌보기를 그만두었다.', 'All summer long, she cared for them', '불일치 → 여름 내내'], ['Jo는 여름 마지막 날 El의 집에 왔다.', 'On the last day of summer, Jo came to El\'s house', '일치'], ['El과 Jo는 정원으로 달려갔다.', 'El and Jo ran to the garden', '일치'], ['과꽃에 꽃이 피었다.', 'There were flowers on the aster', '일치'], ['El도 키가 더 컸다.', 'El grew TALLER, TOO', '일치']] }
    ] },
    { type: 'pick', title: '어법선택', guide: '어법상 알맞은 것을 고르세요.', items: [
      { s: 'El {planted|plants} the flowers in her garden.', ex: '정답 ▶ planted\n이유: 지난 여름의 일 → 과거형 plant + -ed' },
      { s: 'All summer long, she cared for {them|it}.', ex: '정답 ▶ them\n이유: 돌본 것은 the flowers(복수) → them' },
      { s: 'On the last day of summer, Jo {came|comes} to El\'s house.', ex: '정답 ▶ came\n이유: come - came - come (불규칙). 지난 일 → 과거형' },
      { s: 'El and Jo ran to the garden and suddenly {stopped|stoped}.', ex: '정답 ▶ stopped\n이유: \'단모음 + 단자음(stop)\' → p를 한 번 더 쓰고 -ed' },
      { s: 'There {were|was} flowers on the aster ... and El grew TALLER, TOO!', ex: '정답 ▶ were\n이유: There + be동사 + 주어. 주어 flowers(복수) → were' }
    ] },
    { type: 'verb', title: '동사변형', guide: '( ) 안의 동사를 알맞은 형태로 바꿔 쓰세요.', items: [
      { s: 'El and Jo ___ to the garden and suddenly stopped.', v: 'run', a: ['ran'], ex: '정답 ▶ ran\n이유: run - ran - run (불규칙)' },
      { s: 'There were flowers on the aster ... and El ___ TALLER, TOO!', v: 'grow', a: ['grew'], ex: '정답 ▶ grew\n이유: grow - grew - grown (불규칙)' },
      { s: 'All summer long, she ___ for them.', v: 'care', a: ['cared'], ex: '정답 ▶ cared\n이유: e로 끝나는 동사 → -d만 (care → cared)' }
    ] },
    { type: 'error', title: '오류찾기', guide: '어법상 틀린 곳을 고르세요.', items: [
      { s: 'On the last day of summer, Jo [[come]] to El\'s [[house]]. El and Jo [[ran]] to the garden and suddenly stopped.', w: 0, fix: 'came', ex: '틀린 곳 ▶ ① come → came\n이유: 지난 일 → 과거형 came\n나머지 ▶ ② El\'s house(El의 집) ✔ ③ ran ✔' },
      { s: 'El and Jo ran to the garden and [[sudden]] [[stopped]]. Something [[was]] DIFFERENT!', w: 0, fix: 'suddenly', ex: '틀린 곳 ▶ ① sudden → suddenly\n이유: 동사 stopped를 꾸미는 말 → 부사 suddenly(갑자기)\n나머지 ▶ ② stopped ✔ ③ was ✔' },
      { s: '[[There]] [[was]] flowers on the [[aster]] ... and El grew TALLER, TOO!', w: 1, fix: 'were', ex: '틀린 곳 ▶ ② was → were\n이유: 주어 flowers(복수) → There were\n나머지 ▶ ① There ✔ ③ aster ✔' }
    ] },
    { type: 'scramble', title: '본문 스크램블', guide: '우리말에 맞게 단어를 눌러 문장을 완성하세요.', items: [
      { ko: 'El은 정원에 꽃들을 심었다.', en: 'El planted the flowers in her garden.' },
      { ko: '여름 내내 그녀는 그것들을 돌보았다.', en: 'All summer long, she cared for them.' },
      { ko: 'El과 Jo는 정원으로 달려가다가 갑자기 멈췄다.', en: 'El and Jo ran to the garden and suddenly stopped.' }
    ] },
    { type: 'order', title: '문장순서', guide: '문장을 본문 순서대로 눌러서 배열하세요.', items: [
      { lines: ['El planted the flowers in her garden.', 'It was growing season.', 'All summer long, she cared for them.', 'On the last day of summer, Jo came to El\'s house.'], flow: ['정원에 꽃들을 심음', '자라는 시기였음', '여름 내내 돌봄', '여름 마지막 날 Jo가 옴'] },
      { lines: ['On the last day of summer, Jo came to El\'s house.', 'El and Jo ran to the garden and suddenly stopped.', 'Something was DIFFERENT!', 'There were flowers on the aster ... and El grew TALLER, TOO!'], flow: ['Jo가 El의 집에 옴', '정원으로 달려가다 멈춤', '무언가 달라짐!', '과꽃에 꽃이, El도 키가 컸음'] }
    ] },
    { type: 'insert', title: '문장삽입', guide: '주어진 문장이 들어가기에 가장 알맞은 곳을 고르세요.', items: [
      { lines: ['On the last day of summer, Jo came to El\'s house.', 'El and Jo ran to the garden and suddenly stopped.', 'Something was DIFFERENT!'], given: 1, flow: ['Jo가 El의 집에 옴', '둘이 정원으로 달려가다 갑자기 멈춤', '무언가 달라져 있었음!'], ex: '정답 ▶ ①\n이유: \'갑자기 멈춘\' 이유가 \'무언가가 달라져서\'예요. 멈춘 다음 달라진 것을 알아차려요.' },
      { lines: ['El and Jo ran to the garden and suddenly stopped.', 'Something was DIFFERENT!', 'There were flowers on the aster ... and El grew TALLER, TOO!'], given: 1, flow: ['정원으로 달려가다 멈춤', '무언가 달라짐!', '과꽃에 꽃이 피고, El도 컸음'], ex: '정답 ▶ ①\n이유: \'무엇이 달라졌는지\'를 마지막 문장이 보여 줘요. 그 앞에 \'달라졌다\'는 말이 와야 해요.' }
    ] },
    { type: 'odd', title: '어색한 문장', guide: '글의 흐름과 관계없는 문장을 고르세요.', items: [
      { lines: ['It was growing season.', 'All summer long, she cared for them.', 'El forgot to water the flowers all summer.', 'On the last day of summer, Jo came to El\'s house.'], odd: 2, ex: '정답 ▶ ③\n이유: 여름 내내 꽃을 돌봤다고 했어요. \'물 주는 걸 잊었다\'는 반대예요.' }
    ] },
    { type: 'blank', title: '빈칸추론', guide: '빈칸에 들어갈 말로 가장 알맞은 것을 고르세요.', items: [
      { s: 'All summer long, she cared for ____.', opts: ['them', 'it', 'her', 'us'], ex: '정답 ▶ them\n이유: 돌본 것은 정원에 심은 꽃들(the flowers) → 복수 them' },
      { s: 'El and Jo ran to the garden and suddenly ____.', opts: ['stopped', 'slept', 'cried', 'sang'], ex: '정답 ▶ stopped\n이유: 달라진 모습에 놀라 \'갑자기 멈췄어요\'. 다음 문장이 Something was DIFFERENT!' }
    ] },
    { type: 'mc', title: '핵심문법', guide: '알맞은 답을 고르세요.', items: [
      { q: '밑줄 친 <b>It</b>과 쓰임이 <b>같은</b> 것은?<br><b><u>It</u> was growing season.</b>', opts: ['It is Monday today.', 'It is my bag.', 'I like it.', 'It is a cute cat.'], ex: '정답 ▶ It is Monday today.\n이유: 계절·요일·날씨·시간을 말할 때 쓰는 비인칭 주어 it (\'그것\'으로 해석하지 않아요)\n오답 ▶ 나머지 it은 \'그것\'(가리키는 대상이 있음)' },
      { q: '밑줄 친 <b>them</b>이 가리키는 것은?<br><b>El planted the flowers in her garden. ... she cared for <u>them</u>.</b>', opts: ['the flowers', 'El and Jo', 'the pots', 'her classmates'], ex: '정답 ▶ the flowers\n이유: 정원에 심은 꽃들(복수)을 여름 내내 돌봤어요.' },
      { q: '밑줄 친 <b>TOO</b>의 뜻으로 알맞은 것은?<br><b>There were flowers on the aster ... and El grew TALLER, <u>TOO</u>!</b>', opts: ['~도 (또한)', '너무', '두 번', '~까지'], ex: '정답 ▶ ~도 (또한)\n이유: 과꽃이 자라 꽃을 피웠고, El\'도\' 키가 컸어요. 문장 끝 too = ~도' }
    ] },
    { type: 'mc', title: '요약문 완성', guide: '본문을 읽고 요약문의 빈칸 (A), (B)에 들어갈 말을 고르세요.', items: [
      { n: '❸', box: ['❸'], q: '다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 알맞은 것은?<br><b>After El cared for the plants all summer, the aster had (A) ______ and El grew (B) ______, too.</b>', opts: ['(A) flowers – (B) taller', '(A) flowers – (B) smaller', '(A) no flowers – (B) taller', '(A) no flowers – (B) smaller', '(A) leaves – (B) older'], ex: '정답 ▶ (A) flowers – (B) taller\n(A) 과꽃에 \'꽃이\' 피었다 → flowers\n(B) El도 키가 \'더 컸다\' → taller\n오답 ▶ no flowers·smaller는 이야기 처음의 모습이에요.', ev: ['There were flowers on the aster', 'El grew TALLER, TOO'] },
      { n: '❸', box: ['❸'], q: '다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 알맞은 것은?<br><b>Like her aster, El (A) ______ during the growing season, so something was (B) ______ at the end of summer.</b>', opts: ['(A) grew – (B) different', '(A) grew – (B) the same', '(A) stopped – (B) different', '(A) stopped – (B) the same', '(A) slept – (B) wrong'], ex: '정답 ▶ (A) grew – (B) different\n(A) 과꽃처럼 El도 \'자랐다\' → grew\n(B) 여름 끝에 무언가 \'달라져\' 있었다 → different\n오답 ▶ the same(똑같은)은 반대, stopped·slept는 관계없어요.', ev: ['It was growing season', 'Something was DIFFERENT'] }
    ] }
  ] },
  { id: 'k6a', name: 'DAY 9', range: '6과 대화문 ① 대화 1~3', story: 'Lesson 6 · 관심 표현하기 · 조언하기 (Listen and Number)', passage: [['#', '6과 대화 1 · 친환경 차 (Listen and Number)', ''], ['G', 'Look at the sign. We can see many eco-friendly cars.', '저 표지판을 봐. 우리는 많은 친환경 차를 볼 수 있어.'], ['B', 'Oh, I\'m interested in eco-friendly cars.', '오, 난 친환경 차에 관심이 있어.'], ['G', 'Me, too.', '나도 그래.'], ['B', 'Let\'s go see them.', '우리 가서 보자.'], ['#', '6과 대화 2 · 업사이클링 가방 (Listen and Number)', ''], ['B', 'These bags look pretty. Did you make them?', '이 가방들은 정말 예뻐요. 당신이 만들었나요?'], ['W', 'Yes, I made them with old jeans and shirts.', '네, 저는 오래된 청바지와 셔츠로 그것들을 만들었어요.'], ['B', 'That\'s cool. I\'m interested in upcycling.', '멋지네요. 저는 업사이클링에 관심이 있어요.'], ['W', 'Then visit our website. You can learn many things about upcycling.', '그러면 우리 홈페이지를 방문해 보세요. 업사이클링에 대한 많은 것을 배울 수 있어요.'], ['#', '6과 대화 3 · 앱 디자이너 (Listen and Number)', ''], ['M', 'Welcome. Do you want to try our app, Eco Friends?', '어서 오세요. 저희 앱, Eco Friends를 사용해 볼래요?'], ['G', 'Yes. Wow, your app is very interesting.', '네. 와, 당신의 앱은 정말 흥미로워요.'], ['M', 'Thanks.', '고맙습니다.'], ['G', 'I want to become an app designer. What should I do?', '저는 앱 디자이너가 되고 싶어요. 제가 어떻게 해야 하나요?'], ['M', 'You should collect new ideas and learn programming.', '새로운 생각들을 모으고 프로그래밍을 배워야 해요.']], steps: [
    { type: 'vocab', title: '핵심어휘·숙어', quizN: 15, items: [['sign', '표지판'], ['eco-friendly', '친환경적인'], ['be interested in', '~에 관심이 있다'], ['Me, too.', '나도 그래.'], ['Let\'s go see ~', '가서 ~을 보자'], ['look pretty', '예뻐 보이다'], ['jeans', '청바지'], ['upcycling', '업사이클링 (버려지는 물건에 디자인을 더해 새 물건으로 만드는 것)'], ['website', '웹사이트, 홈페이지'], ['app', '앱, 응용 프로그램'], ['interesting', '흥미로운'], ['become', '~이 되다'], ['designer', '디자이너'], ['What should I do?', '내가 어떻게 해야 하니? (조언 구하기)'], ['collect', '모으다'], ['programming', '프로그래밍']] },
    { type: 'pick', title: '어휘선택', guide: '문맥에 맞는 낱말을 고르세요.', items: [
      { s: 'Look at the {sign|sky}. We can see many eco-friendly cars.', ex: '정답 ▶ sign (표지판)\n오답 ▶ sky: 친환경 차를 볼 수 있다고 알려 주는 것 → \'표지판\'' },
      { s: 'Yes, I made them with old {jeans|books} and shirts.', ex: '정답 ▶ jeans (청바지)\n오답 ▶ books: 청바지와 셔츠 같은 헌 옷으로 가방을 만들었어요(업사이클링).' },
      { s: 'You should {collect|throw away} new ideas and learn programming.', ex: '정답 ▶ collect (모으다)\n오답 ▶ throw away (버리다): 앱 디자이너가 되려면 새로운 생각을 \'모아야\' 해요.' }
    ] },
    { type: 'tf', title: 'T/F 내용 확인', guide: '본문 내용과 일치하면 T, 다르면 F를 고르세요.', items: [['The boy is interested in eco-friendly cars.', true, '정답 ▶ T\n이유: Oh, I\'m interested in eco-friendly cars.', null, 'I\'m interested in eco-friendly cars'], ['The woman bought the bags at a store.', false, '정답 ▶ F\n이유: 산 것이 아니라 직접 만들었어요(I made them).', null, 'Yes, I made them with old jeans and shirts'], ['The woman made the bags with old jeans and shirts.', true, '정답 ▶ T\n이유: I made them with old jeans and shirts.', null, 'I made them with old jeans and shirts'], ['The girl wants to become a car designer.', false, '정답 ▶ F\n이유: 자동차가 아니라 앱 디자이너(an app designer)가 되고 싶어 해요.', null, 'I want to become an app designer'], ['The man tells the girl to learn programming.', true, '정답 ▶ T\n이유: You should collect new ideas and learn programming.', null, 'You should collect new ideas and learn programming']] },
    { type: 'mc', title: '알맞은 응답 고르기', guide: '대화의 흐름에 맞는 응답을 고르세요.', items: [
      { q: '다음 말에 이어질 응답으로 가장 알맞은 것은?<br><b>A: I\'m interested in eco-friendly cars.</b>', opts: ['Me, too.', 'Yes, please.', 'No, you may not.', 'I\'m sorry to hear that.'], ex: '정답 ▶ Me, too.\n이유: 관심을 말하는 친구에게 → \'나도 그래(Me, too.)\'로 맞장구쳐요.' },
      { q: '다음 말에 이어질 응답으로 가장 알맞은 것은?<br><b>A: I want to become an app designer. What should I do?</b>', opts: ['You should learn programming.', 'I\'m interested in cars.', 'Me, too.', 'Let\'s go see them.'], ex: '정답 ▶ You should learn programming.\n이유: What should I do?(어떻게 해야 하니?)는 조언을 구하는 말 → You should ~.(~해야 해)로 조언해요.' }
    ] },
    { type: 'mc', title: '일치·불일치', guide: '선택지는 본문을 어려운 어휘로 바꿔 쓴 문장이에요. 풀고 나서 해설의 어휘를 꼭 확인하세요.', items: [
      { box: ['6과 대화 1 · 친환경 차 (Listen and Number)', '6과 대화 2 · 업사이클링 가방 (Listen and Number)', '6과 대화 3 · 앱 디자이너 (Listen and Number)'], q: '대화의 내용과 일치하지 <u>않는</u> 것은?', opts: ['The girl thinks the app is boring.', 'The boy and the girl will go see eco-friendly cars.', 'The woman made bags with old clothes.', 'People can learn about upcycling on the woman\'s website.', 'The man gives the girl some advice.'], ex: '정답 ▶ The girl thinks the app is boring.\n이유: 소녀는 앱이 정말 흥미롭다(very interesting)고 했어요.', per: [['소녀는 앱이 지루하다고 생각한다.', 'your app is very interesting', '불일치 → 흥미로움'], ['두 사람은 친환경 차를 보러 갈 것이다.', 'Let\'s go see them', '일치'], ['여자는 헌 옷으로 가방을 만들었다.', 'I made them with old jeans and shirts', '일치'], ['여자의 홈페이지에서 업사이클링을 배울 수 있다.', 'You can learn many things about upcycling', '일치'], ['남자는 소녀에게 조언을 해 준다.', 'You should collect new ideas and learn programming', '일치']] }
    ] },
    { type: 'pick', title: '어법선택', guide: '어법상 알맞은 것을 고르세요.', items: [
      { s: 'Oh, I\'m interested {in|on} eco-friendly cars.', ex: '정답 ▶ in\n이유: be interested in ~ = ~에 관심이 있다 (짝꿍 전치사 in)' },
      { s: 'These bags look pretty. Did you {make|made} them?', ex: '정답 ▶ make\n이유: Did + 주어 + 동사원형 ~? (did가 과거를 나타내니 동사는 원형)' },
      { s: 'Yes. Wow, your app is very {interesting|interested}.', ex: '정답 ▶ interesting\n이유: 앱이 \'흥미를 주는\' 것 → interesting. interested는 사람이 \'흥미를 느끼는\' 것이에요.' },
      { s: 'You should {collect|collecting} new ideas and learn programming.', ex: '정답 ▶ collect\n이유: 조동사 should + 동사원형 = ~해야 한다 (조언)' }
    ] },
    { type: 'scramble', title: '본문 스크램블', guide: '우리말에 맞게 단어를 눌러 문장을 완성하세요.', items: [
      { ko: '저는 업사이클링에 관심이 있어요.', en: 'I\'m interested in upcycling.' },
      { ko: '새로운 생각들을 모으고 프로그래밍을 배워야 해요.', en: 'You should collect new ideas and learn programming.' }
    ] },
    { type: 'order', title: '문장순서', guide: '대화(문장)를 순서대로 눌러서 배열하세요.', items: [
      { lines: ['These bags look pretty. Did you make them?', 'Yes, I made them with old jeans and shirts.', 'That\'s cool. I\'m interested in upcycling.', 'Then visit our website. You can learn many things about upcycling.'], flow: ['B: 가방이 예뻐요, 직접 만들었나요?', 'W: 네, 헌 청바지와 셔츠로', 'B: 멋져요, 업사이클링에 관심 있어요', 'W: 그럼 홈페이지에 가 보세요'] }
    ] },
    { type: 'blank', title: '빈칸추론', guide: '빈칸에 들어갈 말로 가장 알맞은 것을 고르세요.', items: [
      { s: 'Then visit our ____. You can learn many things about upcycling.', opts: ['website', 'school', 'store', 'car'], ex: '정답 ▶ website\n이유: \'방문해서(visit)\' 업사이클링에 대해 많은 것을 배울 수 있는 곳 → 홈페이지' },
      { s: 'Welcome. Do you want to try our ____, Eco Friends?', opts: ['app', 'car', 'bag', 'game'], ex: '정답 ▶ app\n이유: 뒤에서 소녀가 \'앱 디자이너\'가 되고 싶다고 해요. Eco Friends는 앱 이름이에요.' }
    ] },
    { type: 'mc', title: '어색한 대화 고르기', guide: '짝지어진 대화 중 어색한 것을 고르세요.', items: [
      { q: '다음 중 짝지어진 대화가 <b>어색한</b> 것은?', opts: ['A: Do you want to try our app? B: Yes, I should.', 'A: What are you interested in? B: I\'m interested in music.', 'A: What should I do? B: You should practice every day.', 'A: I\'m interested in cars. B: Me, too.'], ex: '정답 ▶ A: Do you want to try our app? B: Yes, I should.\n이유: Do you ~? 질문에는 Yes, I do. / No, I don\'t.로 답해요.' }
    ] },
    { type: 'mc', title: '의사소통 기능', guide: '상황에 맞는 표현을 고르세요.', items: [
      { q: '조언을 구하는 표현으로 알맞은 것은?', opts: ['What should I do?', 'What are you interested in?', 'Did you make them?', 'Let\'s go see them.'], ex: '정답 ▶ What should I do?\n이유: \'내가 어떻게 해야 하니?\' = 조언 구하기 → 대답은 You should ~.' },
      { q: '관심을 표현하는 말이 <b>아닌</b> 것은?', opts: ['You should learn programming.', 'I\'m interested in art.', 'I\'m into art.', 'Art interests me.'], ex: '정답 ▶ You should learn programming.\n이유: You should ~는 조언하는 표현이에요. 나머지는 모두 \'나는 미술에 관심이 있어\'라는 뜻이에요.' }
    ] },
    { type: 'mc', title: '요약문 완성', guide: '본문을 읽고 요약문의 빈칸 (A), (B)에 들어갈 말을 고르세요.', items: [
      { n: null, box: ['6과 대화 1 · 친환경 차 (Listen and Number)', '6과 대화 2 · 업사이클링 가방 (Listen and Number)'], q: '다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 알맞은 것은?<br><b>In Dialog 1, the boy wants to see eco-friendly (A) ______, and in Dialog 2, the woman made bags with old (B) ______ and shirts.</b>', opts: ['(A) cars – (B) jeans', '(A) bags – (B) jeans', '(A) cars – (B) paper', '(A) apps – (B) shoes', '(A) trees – (B) bottles'], ex: '정답 ▶ (A) cars – (B) jeans\n(A) 친환경 \'차\' → cars\n(B) 헌 \'청바지\'와 셔츠 → jeans', ev: ['I\'m interested in eco-friendly cars', 'I made them with old jeans and shirts'] },
      { n: null, box: ['6과 대화 3 · 앱 디자이너 (Listen and Number)'], q: '다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 알맞은 것은?<br><b>The girl wants to become an app (A) ______, and the man advises her to collect new ideas and learn (B) ______.</b>', opts: ['(A) designer – (B) programming', '(A) user – (B) programming', '(A) designer – (B) cooking', '(A) seller – (B) drawing', '(A) player – (B) singing'], ex: '정답 ▶ (A) designer – (B) programming\n(A) 앱 \'디자이너\' → designer\n(B) \'프로그래밍\'을 배워야 한다 → programming', ev: ['I want to become an app designer', 'You should collect new ideas and learn programming'] }
    ] }
  ] },
  { id: 'k6b', name: 'DAY 10', range: '6과 대화문 ② 대화 4·클립', story: 'Lesson 6 · 자연 다큐 영화 · 산림 경비원', passage: [['#', '6과 대화 4 · 자연 다큐 영화 (In Everyday Life)', ''], ['Jinsu', 'Did you see this movie, Amy?', 'Amy, 이 영화 봤어?'], ['Amy', 'I didn\'t see it. What\'s it about, Jinsu?', '안 봤어. 진수야, 그것은 무엇에 관한 거니?'], ['Jinsu', 'It\'s about wild animals in deserts.', '그것은 사막의 야생 동물에 관한 거야.'], ['Amy', 'I\'m interested in making movies about nature.', '나는 자연에 관한 영화를 만드는 데 관심이 있어.'], ['Jinsu', 'Then you should learn from movie directors. The director, Linda Han, is giving a speech in the main hall.', '그러면 너는 영화감독에게서 배워야 해. Linda Han 감독님이 대강당에서 연설을 하고 계셔.'], ['Amy', 'Great. Let\'s go together.', '좋아. 같이 가 보자.'], ['Jinsu', 'Okay.', '그래.'], ['#', '6과 클립 · 산림 경비원 Jake (Enjoy the Clip)', ''], ['Jake', 'Hi, my name is Jake, and I\'m a forest ranger.', '안녕하세요, 제 이름은 Jake이고 저는 산림 경비원입니다.'], ['Jake', 'I\'m interested in forests, so I became a forest ranger.', '저는 숲에 관심이 있어서 산림 경비원이 되었습니다.'], ['Jake', 'Do you want to protect trees and animals in the forest?', '여러분은 숲속의 나무와 동물을 보호하고 싶나요?'], ['Jake', 'Then you should not touch them.', '그러면 그들을 만지지 말아야 합니다.'], ['Jake', 'And don\'t throw away trash in the forest.', '그리고 숲에 쓰레기를 버리지 마세요.']], steps: [
    { type: 'vocab', title: '핵심어휘·숙어', quizN: 15, items: [['movie', '영화'], ['What\'s it about?', '그것은 무엇에 관한 거니?'], ['wild animal', '야생 동물'], ['desert', '사막'], ['nature', '자연'], ['director', '감독'], ['give a speech', '연설하다'], ['main hall', '대강당'], ['together', '함께'], ['forest ranger', '산림 경비원'], ['forest', '숲'], ['protect', '보호하다'], ['touch', '만지다'], ['throw away', '버리다'], ['trash', '쓰레기']] },
    { type: 'pick', title: '어휘선택', guide: '문맥에 맞는 낱말을 고르세요.', items: [
      { s: 'Then you should learn from movie {directors|doctors}. The director, Linda Han, is giving a speech in the main hall.', ex: '정답 ▶ directors (감독)\n오답 ▶ doctors: 영화를 만들고 싶은 Amy → 영화 \'감독\'에게 배워야 해요. 바로 뒤에 감독 Linda Han이 나와요.' },
      { s: 'I\'m interested in {forests|cars}, so I became a forest ranger.', ex: '정답 ▶ forests (숲)\n오답 ▶ cars: 숲에 관심이 있어서 \'산림\' 경비원이 되었어요.' },
      { s: 'And don\'t throw away {trash|water} in the forest.', ex: '정답 ▶ trash (쓰레기)\n오답 ▶ water: 숲을 보호하려면 \'쓰레기\'를 버리지 말아야 해요.' }
    ] },
    { type: 'tf', title: 'T/F 내용 확인', guide: '본문 내용과 일치하면 T, 다르면 F를 고르세요.', items: [['The movie is about wild animals in deserts.', true, '정답 ▶ T\n이유: It\'s about wild animals in deserts.', null, 'It\'s about wild animals in deserts'], ['Amy is interested in drawing cartoons about nature.', false, '정답 ▶ F\n이유: 만화를 그리는 것이 아니라 자연에 관한 영화를 만드는 것(making movies)에 관심이 있어요.', null, 'I\'m interested in making movies about nature'], ['Linda Han is giving a speech in the main hall.', true, '정답 ▶ T\n이유: The director, Linda Han, is giving a speech in the main hall.', null, 'is giving a speech in the main hall'], ['Jake became a forest ranger because he is interested in forests.', true, '정답 ▶ T\n이유: I\'m interested in forests, so I became a forest ranger.', null, 'I\'m interested in forests, so I became a forest ranger'], ['Jake says we can touch animals in the forest.', false, '정답 ▶ F\n이유: 나무와 동물을 만지지 말아야 한다(should not touch)고 했어요.', null, 'Then you should not touch them']] },
    { type: 'mc', title: '알맞은 응답 고르기', guide: '대화의 흐름에 맞는 응답을 고르세요.', items: [
      { q: '다음 말에 이어질 응답으로 가장 알맞은 것은?<br><b>A: What\'s it about?</b>', opts: ['It\'s about wild animals.', 'I didn\'t see it.', 'Great.', 'Okay.'], ex: '정답 ▶ It\'s about wild animals.\n이유: What\'s it about?(무엇에 관한 거니?) → It\'s about ~.(~에 관한 거야)로 답해요.' },
      { q: '다음 말에 이어질 응답으로 가장 알맞은 것은?<br><b>A: I\'m interested in making movies. What should I do?</b>', opts: ['You should learn from movie directors.', 'I didn\'t see it.', 'It\'s about nature.', 'Me, too.'], ex: '정답 ▶ You should learn from movie directors.\n이유: 조언을 구하면 → You should ~.로 조언해요.' }
    ] },
    { type: 'mc', title: '일치·불일치', guide: '선택지는 본문을 어려운 어휘로 바꿔 쓴 문장이에요. 풀고 나서 해설의 어휘를 꼭 확인하세요.', items: [
      { box: ['6과 대화 4 · 자연 다큐 영화 (In Everyday Life)'], q: '대화의 내용과 일치하지 <u>않는</u> 것은?', opts: ['Jinsu is giving a speech in the main hall.', 'Amy didn\'t see the movie.', 'The movie is about wild animals.', 'Amy is interested in making movies about nature.', 'Amy and Jinsu will go to the main hall together.'], ex: '정답 ▶ Jinsu is giving a speech in the main hall.\n이유: 대강당에서 연설하는 사람은 영화감독 Linda Han이에요.', per: [['진수가 대강당에서 연설하고 있다.', 'The director, Linda Han, is giving a speech', '불일치 → Linda Han'], ['Amy는 그 영화를 보지 않았다.', 'I didn\'t see it', '일치'], ['그 영화는 야생 동물에 관한 것이다.', 'It\'s about wild animals in deserts', '일치'], ['Amy는 자연에 관한 영화를 만드는 데 관심이 있다.', 'I\'m interested in making movies about nature', '일치'], ['둘은 함께 대강당에 갈 것이다.', 'Let\'s go together', '일치']] },
      { box: ['6과 클립 · 산림 경비원 Jake (Enjoy the Clip)'], q: '클립의 내용과 일치하지 <u>않는</u> 것은?', opts: ['Jake says we should touch the animals.', 'Jake is interested in forests.', 'Jake is a forest ranger.', 'Jake talks about protecting trees and animals.', 'Jake says we should not throw away trash in the forest.'], ex: '정답 ▶ Jake says we should touch the animals.\n이유: 동물과 나무를 만지지 말아야 한다(should not touch them)고 했어요.', per: [['Jake는 동물을 만져야 한다고 말한다.', 'you should not touch them', '불일치'], ['Jake는 숲에 관심이 있다.', 'I\'m interested in forests', '일치'], ['Jake는 산림 경비원이다.', 'I\'m a forest ranger', '일치'], ['Jake는 나무와 동물 보호에 대해 이야기한다.', 'Do you want to protect trees and animals', '일치'], ['Jake는 숲에 쓰레기를 버리지 말라고 한다.', 'don\'t throw away trash in the forest', '일치']] }
    ] },
    { type: 'pick', title: '어법선택', guide: '어법상 알맞은 것을 고르세요.', items: [
      { s: 'I {didn\'t|don\'t} see it. What\'s it about, Jinsu?', ex: '정답 ▶ didn\'t\n이유: Did you see ~?(과거)로 물었으니 과거 부정 didn\'t + 동사원형으로 답해요.' },
      { s: 'I\'m interested in {making|make} movies about nature.', ex: '정답 ▶ making\n이유: 전치사 in 뒤에는 명사나 동명사(-ing). be interested in -ing' },
      { s: 'Then you should learn from movie directors. The director, Linda Han, is {giving|give} a speech in the main hall.', ex: '정답 ▶ giving\n이유: 지금 연설하는 중 → 현재진행형 is + -ing' },
      { s: 'Do you want {to protect|protecting} trees and animals in the forest?', ex: '정답 ▶ to protect\n이유: want + to부정사 = ~하고 싶다. want 뒤에 -ing는 쓰지 않아요.' }
    ] },
    { type: 'scramble', title: '본문 스크램블', guide: '우리말에 맞게 단어를 눌러 문장을 완성하세요.', items: [
      { ko: '그러면 너는 영화감독에게서 배워야 해.', en: 'Then you should learn from movie directors.' },
      { ko: '저는 숲에 관심이 있어서 산림 경비원이 되었습니다.', en: 'I\'m interested in forests, so I became a forest ranger.' }
    ] },
    { type: 'order', title: '문장순서', guide: '대화(문장)를 순서대로 눌러서 배열하세요.', items: [
      { lines: ['Did you see this movie, Amy?', 'I didn\'t see it. What\'s it about, Jinsu?', 'It\'s about wild animals in deserts.', 'I\'m interested in making movies about nature.'], flow: ['Jinsu: 이 영화 봤어?', 'Amy: 안 봤어, 무엇에 관한 거니?', 'Jinsu: 사막의 야생 동물', 'Amy: 자연에 관한 영화를 만드는 데 관심 있어'] }
    ] },
    { type: 'blank', title: '빈칸추론', guide: '빈칸에 들어갈 말로 가장 알맞은 것을 고르세요.', items: [
      { s: 'Then you should learn from movie directors. The director, Linda Han, is giving a speech in the main ____.', opts: ['hall', 'kitchen', 'desert', 'forest'], ex: '정답 ▶ hall\n이유: 연설을 하는 곳 → main hall(대강당)' },
      { s: 'Then you should not ____ them.', opts: ['touch', 'protect', 'see', 'love'], ex: '정답 ▶ touch\n이유: 나무와 동물을 보호하려면 \'만지지\' 말아야 해요.\n오답 ▶ protect: 보호하지 말라는 건 앞 문장과 반대예요.' }
    ] },
    { type: 'mc', title: '어색한 대화 고르기', guide: '짝지어진 대화 중 어색한 것을 고르세요.', items: [
      { q: '다음 중 짝지어진 대화가 <b>어색한</b> 것은?', opts: ['A: What should I do? B: I\'m interested in movies.', 'A: Did you see this movie? B: No, I didn\'t.', 'A: What\'s it about? B: It\'s about wild animals.', 'A: Let\'s go together. B: Okay.'], ex: '정답 ▶ A: What should I do? B: I\'m interested in movies.\n이유: 조언을 구했는데 자기 관심사를 말했어요. → You should ~.로 조언해야 해요.' }
    ] },
    { type: 'mc', title: '의사소통 기능', guide: '상황에 맞는 표현을 고르세요.', items: [
      { q: '밑줄 친 말과 바꿔 쓸 수 있는 것은?<br><b>Then you <u>should not</u> touch them.</b>', opts: ['shouldn\'t', 'should', 'can', 'will'], ex: '정답 ▶ shouldn\'t\n이유: should not = shouldn\'t (~하면 안 된다). 하지 말라는 조언이에요.' }
    ] },
    { type: 'mc', title: '요약문 완성', guide: '본문을 읽고 요약문의 빈칸 (A), (B)에 들어갈 말을 고르세요.', items: [
      { n: null, box: ['6과 대화 4 · 자연 다큐 영화 (In Everyday Life)'], q: '다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 알맞은 것은?<br><b>Amy is interested in making movies about (A) ______, so Jinsu advises her to learn from movie (B) ______.</b>', opts: ['(A) nature – (B) directors', '(A) cars – (B) directors', '(A) nature – (B) actors', '(A) music – (B) rangers', '(A) cars – (B) teachers'], ex: '정답 ▶ (A) nature – (B) directors\n(A) \'자연\'에 관한 영화 → nature\n(B) 영화 \'감독\'에게 배워야 한다 → directors', ev: ['I\'m interested in making movies about nature', 'you should learn from movie directors'] },
      { n: null, box: ['6과 클립 · 산림 경비원 Jake (Enjoy the Clip)'], q: '다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 알맞은 것은?<br><b>To (A) ______ the forest, we should not touch trees and animals, and we should not throw away (B) ______ there.</b>', opts: ['(A) protect – (B) trash', '(A) visit – (B) trash', '(A) protect – (B) water', '(A) cut – (B) trees', '(A) clean – (B) seeds'], ex: '정답 ▶ (A) protect – (B) trash\n(A) 숲을 \'보호하려면\' → protect\n(B) \'쓰레기\'를 버리지 마세요 → trash', ev: ['Do you want to protect trees and animals in the forest', 'don\'t throw away trash in the forest'] }
    ] }
  ] },
  { id: 'd1', name: 'DAY 11', range: '6과 본문 ❶❷', story: '자연에서 일하는 사람들 · 거제의 해녀, 나리', passage: [['', '❶', ''], ['', 'Some people love to work in nature.', '어떤 사람들은 자연에서 일하는 것을 아주 좋아한다.'], ['', 'They work in the sea, mountains, or even in the Arctic.', '그들은 바다, 산, 심지어 북극에서도 일한다.'], ['', 'Let\'s meet them and listen to their stories.', '그들을 만나 보고 그들의 이야기를 들어 보자.'], ['', '❷', ''], ['Nari', 'I am Nari.', '저는 나리입니다.'], ['', 'I am a haenyeo in Geoje.', '저는 거제의 해녀입니다.'], ['', 'I dive in the water and collect seafood.', '저는 물에 잠수해서 해산물을 채집합니다.'], ['', 'In the morning, I check the tide and the weather.', '아침에, 저는 조수와 날씨를 확인합니다.'], ['', 'I wear a diving suit and swimming glasses to work in the water.', '저는 물속에서 일하기 위해 잠수복을 입고 수경을 씁니다.'], ['', 'I love diving and spending time in the beautiful sea.', '저는 잠수하는 것과 아름다운 바다에서 시간을 보내는 것을 아주 좋아합니다.'], ['', 'I don\'t collect too much seafood.', '저는 너무 많은 해산물을 채집하지 않습니다.'], ['', 'This is good for the ocean.', '이것이 바다에 좋습니다.'], ['', 'These days, I see a lot of trash in the water, so I pick up the trash.', '요즘은 물속에 쓰레기가 많이 보여서 쓰레기를 줍습니다.'], ['', 'I believe that we should care about the ocean.', '저는 우리가 바다에 신경을 써야 한다고 믿습니다.']], steps: [
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
  { id: 'd2', name: 'DAY 12', range: '6과 본문 ❸❹', story: '지리산의 수의사, 지한 · 극지 과학자, 은', passage: [['', '❸', ''], ['Jihan', 'My name is Jihan.', '제 이름은 지한입니다.'], ['', 'I am a vet at the wild animal care center in Jirisan.', '저는 지리산 야생 동물 보호 센터의 수의사입니다.'], ['', 'I take care of sick wild animals in the center and send them back to their homes.', '저는 센터의 아픈 야생 동물을 돌보고 그들을 집으로 돌려보냅니다.'], ['', 'Also, I often climb the mountain to look after wild animals like bears.', '또한 저는 곰과 같은 야생 동물을 돌보기 위해 자주 산을 오릅니다.'], ['', 'I\'m proud of my job.', '저는 제 직업이 자랑스럽습니다.'], ['', 'I think that protecting wild animals is important.', '저는 야생 동물을 보호하는 것이 중요하다고 생각합니다.'], ['', 'We should keep an eye on them and their homes to live together.', '우리는 함께 살아가기 위해 그들과 그들의 서식처를 계속 지켜보아야 합니다.'], ['', '❹', ''], ['Eun', 'My name is Eun, and I am an Arctic scientist.', '제 이름은 은이고, 저는 극지 과학자입니다.'], ['', 'I work at the Arctic Dasan Station in Norway.', '저는 노르웨이의 북극 다산 과학 기지에서 일합니다.'], ['', 'I study the soil, seawater, and ice in the Arctic.', '저는 북극의 토양, 바닷물, 얼음을 연구합니다.'], ['', 'I often travel on the special ship, Araon.', '저는 특별한 배인 아라온호를 타고 자주 이동합니다.'], ['', 'This ship is stronger than other ships.', '이 배는 다른 배보다 더 튼튼합니다.'], ['', 'It can break thick ice across the ocean.', '그것은 바다를 가로질러 두꺼운 얼음을 깰 수 있습니다.'], ['', 'Thanks to Araon, I can collect seawater samples.', '아라온호 덕분에 저는 바닷물 표본을 채집할 수 있습니다.'], ['', 'The Arctic Ocean has the answers to the climate crisis.', '북극해는 기후 위기에 대한 해답을 가지고 있습니다.'], ['', 'I hope that my work can help the Earth.', '저는 제 일이 지구를 도울 수 있기를 바랍니다.']], steps: [
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
