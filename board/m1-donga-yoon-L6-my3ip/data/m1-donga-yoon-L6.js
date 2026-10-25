/* 중1 동아(윤정미) Lesson 6 · Good for the Earth, Good for Us (본문: Join the Zero-Waste Challenge)
   작성 규칙은 README.md 의 "데이터 작성 규칙". insert: given = 빠지는 문장 번호(0부터), odd = 어색한 문장 번호 */
window.PKG = {
  id: 'm1-donga-yoon-L6',
  school: '중1 동아(윤정미)',
  unit: 'Lesson 6~7',
  title: 'Zero-Waste Challenge · Let’s Make a Movie!',
  titleKo: '제로 웨이스트 챌린지에 동참하세요',
  exam: '2학기 기말고사',
  prose: true,
  stepsBefore: ["핵심어휘·숙어", "어휘선택", "T/F 내용 확인", "어법선택", "동사변형", "오류찾기", "본문 스크램블", "문장순서", "문장삽입", "어색한 문장", "빈칸추론", "핵심문법"],   /* 일치·불일치 추가 전 단계 이름: 예전 기록을 새 단계에 맞추는 데 씀 */
  teacherPhone: '',            /* 결과 받을 번호. 예: '010-1234-5678' */

  days: [
  /* ═══════════════════════════ DAY 1 · 본문 ❶❷❸ ═══════════════════════════ */
  {
    id: 'd1', name: 'DAY 1', range: '본문 ❶❷❸', story: '병들어 가는 지구 · Olivia의 챌린지 · Domingo의 챌린지',
    passage: [
      ['', '❶', ''],
      ['', 'Every day, we produce lots of waste, and the Earth is getting sicker and sicker.', '매일 우리는 많은 쓰레기를 만들고, 지구는 점점 더 병들고 있습니다.'],
      ['', 'Do you want to save the Earth?', '여러분은 지구를 구하고 싶나요?'],
      ['', 'Then, join the zero-waste challenge, and share your stories.', '그렇다면 제로 웨이스트 챌린지에 동참하고 여러분의 이야기를 공유해 주세요.'],
      ['', '❷', ''],
      ['', 'Challenge 01 Reduce Food Waste', '챌린지 01 / 음식물 쓰레기를 줄이세요'],
      ['Olivia', 'My birthday was last Saturday, and my family and I ate out.', '내 생일은 지난 토요일이었고, 가족들과 나는 외식을 했어.'],
      ['', 'There were lots of leftovers, but we brought them home.', '남은 음식이 많았지만, 우리는 그것들을 집으로 가져왔어.'],
      ['', 'The next day, I made a nice lunch out of them.', '그다음 날, 나는 그것들로 맛있는 점심을 만들었어.'],
      ['', 'FYI, you can find great cooking ideas for leftovers on the Internet.', '참고로, 인터넷에서 남은 음식을 위한 멋진 요리 아이디어를 찾을 수 있어.'],
      ['', '❸', ''],
      ['', 'Challenge 02 Reuse', '챌린지 02 / 재사용하세요'],
      ['Domingo', 'My dog tore my bag.', '내 개가 내 가방을 찢었어.'],
      ['', 'I wanted to buy a new one, but I thought again.', '나는 새것을 사고 싶었지만, 다시 생각해 봤어.'],
      ['', 'I learned that reusing is important for zero-waste living.', '나는 재사용이 제로 웨이스트 생활에 중요하다고 배웠어.'],
      ['', 'So, I decided to fix it and reuse it.', '그래서 나는 그것을 수선해서 재사용하기로 결심했어.'],
      ['', "I'm not very good at sewing, and I don't think that the bag looks perfect.", '나는 바느질을 아주 잘하지 못하고, 가방이 완벽해 보인다고 생각하진 않아.'],
      ['', "I guess it's all right.", '그래도 괜찮은 것 같아.']
    ],
    steps: [
      { type: 'vocab', title: '핵심어휘·숙어', quizN: 15, items: [
        ['waste', '쓰레기; 낭비'], ['produce', '생산하다, 만들어 내다'], ['lots of', '많은'], ['sick', '아픈, 병든'],
        ['save', '구하다; 저축하다'], ['join', '참여하다, 동참하다'], ['challenge', '도전, 챌린지'], ['share', '공유하다'],
        ['reduce', '줄이다'], ['eat out', '외식하다'], ['leftover', '남은 음식'], ['bring', '가져오다'],
        ['make A out of B', 'B로 A를 만들다'], ['FYI', '참고로'], ['on the Internet', '인터넷에서'], ['reuse', '재사용하다'],
        ['tear', '찢다'], ['learn', '배우다'], ['important', '중요한'], ['living', '생활'],
        ['decide', '결심하다, 결정하다'], ['fix', '고치다, 수선하다'], ['be good at', '~을 잘하다'], ['sew', '바느질하다'],
        ['perfect', '완벽한'], ['guess', '추측하다, ~인 것 같다'], ['all right', '괜찮은']
      ]},
      { type: 'pick', title: '어휘선택', guide: '문맥에 맞는 낱말을 고르세요.', items: [
        { s: 'Every day, we {produce|reduce} lots of waste, and the Earth is getting sicker and sicker.', ex: '쓰레기를 만들어 내서(produce) 지구가 병들고 있다.' },
        { s: 'Do you want to {save|hurt} the Earth?', ex: 'save: 구하다' },
        { s: 'Then, join the zero-waste challenge, and {share|hide} your stories.', ex: 'share: 공유하다' },
        { s: 'Challenge 01 {Reduce|Increase} Food Waste', ex: 'reduce: 줄이다 (increase: 늘리다)' },
        { s: 'My birthday was last Saturday, and my family and I {ate out|stayed home}.', ex: 'eat out: 외식하다 → 식당에서 남은 음식을 가져왔다.' },
        { s: 'There were lots of {leftovers|guests}, but we brought them home.', ex: 'leftover: 남은 음식' },
        { s: 'My dog {tore|fixed} my bag.', ex: 'tear(찢다)의 과거형 tore' },
        { s: 'I learned that {reusing|buying} is important for zero-waste living.', ex: '제로 웨이스트 생활에는 재사용(reusing)이 중요하다.' },
        { s: 'So, I decided to {fix|sell} it and reuse it.', ex: 'fix: 고치다, 수선하다' },
        { s: "I'm not very good at {sewing|cooking}, and I don't think that the bag looks perfect.", ex: '가방을 고치려면 바느질(sewing)을 해야 한다.' }
      ]},
      { type: 'tf', title: 'T/F 내용 확인', guide: '본문 내용과 일치하면 T, 다르면 F를 고르세요.', items: [
        ['The Earth is getting healthier these days.', false, '지구는 점점 더 병들고(sicker and sicker) 있다.'],
        ["Olivia's birthday was last Saturday.", true, 'My birthday was last Saturday.'],
        ["Olivia's family left the leftovers at the restaurant.", false, '남은 음식을 집으로 가져왔다(brought them home).'],
        ['Olivia made lunch out of the leftovers the next day.', true, 'The next day, I made a nice lunch out of them.'],
        ["Domingo's cat tore his bag.", false, '가방을 찢은 것은 개(dog)다.'],
        ['Domingo bought a new bag.', false, '새 가방을 사지 않고 고쳐서 다시 썼다.'],
        ['Domingo learned that reusing is important for zero-waste living.', true, 'I learned that reusing is important for zero-waste living.'],
        ['Domingo thinks his bag looks perfect.', false, '가방이 완벽해 보인다고 생각하지 않는다.']
      ]},
      { type: 'mc', title: '일치·불일치', guide: "본문을 읽고 내용과 맞는지 확인해요. 틀린 선택지는 해설의 근거 문장과 비교해 보세요.", items: [
        { n: "❷", box: ["❷"], q: "Olivia에 관한 내용과 일치하지 <u>않는</u> 것은?", opts: ["Olivia's family threw away the leftovers.", "Olivia's birthday was last Saturday.", "Olivia and her family ate out.", "Olivia made lunch out of the leftovers.", "You can find cooking ideas for leftovers on the Internet."], ex: "정답 근거: There were lots of leftovers, but we brought them home.\n· leftovers : 남은 음식 · throw away : 버리다 · eat out : 외식하다", per: [["Olivia의 가족은 남은 음식을 버렸다.", "we brought them home", "불일치 → 집으로 가져옴"], ["Olivia의 생일은 지난 토요일이었다.", "My birthday was last Saturday", "일치"], ["Olivia와 가족은 외식했다.", "my family and I ate out", "일치"], ["Olivia는 남은 음식으로 점심을 만들었다.", "I made a nice lunch out of them", "일치"], ["인터넷에서 남은 음식 요리 아이디어를 찾을 수 있다.", "you can find great cooking ideas for leftovers on the Internet", "일치"]] },
        { n: "❸", box: ["❸"], q: "Domingo에 관한 내용과 <u>일치하는</u> 것은?", opts: ["Domingo decided to fix his bag and reuse it.", "Domingo tore his dog's bag.", "Domingo bought a new bag.", "Domingo is very good at sewing.", "Domingo thinks the bag looks perfect."], ex: "정답 근거: So, I decided to fix it and reuse it.\n· tear - tore - torn : 찢다 · sew : 바느질하다 · reuse : 재사용하다", per: [["Domingo는 가방을 고쳐서 다시 쓰기로 했다.", "I decided to fix it and reuse it", "일치"], ["Domingo가 개의 가방을 찢었다.", "My dog tore my bag", "불일치 → 개가 Domingo의 가방을 찢음"], ["Domingo는 새 가방을 샀다.", "I wanted to buy a new one, but I thought again", "불일치 → 사지 않음"], ["Domingo는 바느질을 아주 잘한다.", "I'm not very good at sewing", "불일치 → 잘 못함"], ["Domingo는 가방이 완벽해 보인다고 생각한다.", "I don't think that the bag looks perfect", "불일치 → 완벽하진 않다고 생각함"]] }
      ]},
      { type: 'pick', title: '어법선택', guide: '어법상 알맞은 것을 고르세요.', items: [
        { s: 'Every day, we produce lots of waste, and the Earth is getting {sicker|sick} and sicker.', ex: '비교급 and 비교급: 점점 더 ~한' },
        { s: 'Do you want {to save|saving} the Earth?', ex: 'want + to부정사' },
        { s: 'Then, join the zero-waste challenge, and {share|shares} your stories.', ex: '명령문: join and share (동사원형)' },
        { s: 'My birthday {was|is} last Saturday, and my family and I ate out.', ex: 'last Saturday(과거) → was' },
        { s: '{There were|There was} lots of leftovers, but we brought them home.', ex: 'leftovers는 복수 → There were' },
        { s: 'There were lots of leftovers, but we {brought|bringed} them home.', ex: 'bring - brought - brought' },
        { s: 'FYI, you can {find|finds} great cooking ideas for leftovers on the Internet.', ex: 'can + 동사원형' },
        { s: 'I wanted {to buy|buying} a new one, but I thought again.', ex: 'want + to부정사' },
        { s: 'I learned {that|what} reusing is important for zero-waste living.', ex: '뒤에 완전한 문장 → 접속사 that' },
        { s: 'I learned that reusing {is|are} important for zero-waste living.', ex: '동명사 주어는 단수 → is' },
        { s: 'So, I decided {to fix|fixing} it and reuse it.', ex: 'decide + to부정사' }
      ]},
      { type: 'verb', title: '동사변형', guide: '( ) 안의 동사를 알맞은 형태로 바꿔 쓰세요. 과거형에 주의!', items: [
        { s: 'Every day, we produce lots of waste, and the Earth is ___ sicker and sicker.', v: 'get', a: ['getting'], ex: '현재진행형 is getting (t를 한 번 더)' },
        { s: 'Do you want ___ the Earth?', v: 'save', a: ['to save'], ex: 'want + to부정사' },
        { s: 'My birthday ___ last Saturday, and my family and I ate out.', v: 'be', a: ['was'], ex: 'last Saturday → 과거 was' },
        { s: 'My birthday was last Saturday, and my family and I ___ out.', v: 'eat', a: ['ate'], ex: 'eat - ate - eaten' },
        { s: 'There were lots of leftovers, but we ___ them home.', v: 'bring', a: ['brought'], ex: 'bring - brought - brought' },
        { s: 'The next day, I ___ a nice lunch out of them.', v: 'make', a: ['made'], ex: 'make - made - made' },
        { s: 'My dog ___ my bag.', v: 'tear', a: ['tore'], ex: 'tear - tore - torn' },
        { s: 'I wanted to buy a new one, but I ___ again.', v: 'think', a: ['thought'], ex: 'think - thought - thought' },
        { s: 'I learned that ___ is important for zero-waste living.', v: 'reuse', a: ['reusing', 'to reuse'], ex: '주어 자리 → 동명사 (본문: reusing)' },
        { s: 'So, I decided ___ it and reuse it.', v: 'fix', a: ['to fix'], ex: 'decide + to부정사' },
        { s: "I'm not very good at sewing, and I don't think that the bag ___ perfect.", v: 'look', a: ['looks'], ex: '주어 the bag → looks' }
      ]},
      { type: 'error', title: '오류찾기', guide: '어법상 틀린 곳을 고르세요.', items: [
        { s: 'Every day, we [[produce]] lots of waste, and the Earth is [[getting]] [[sick]] and [[sicker]].', w: 2, fix: 'sicker', ex: '비교급 and 비교급 → sicker and sicker' },
        { s: 'Do you want [[saving]] the Earth? Then, [[join]] the zero-waste challenge, and [[share]] [[your]] stories.', w: 0, fix: 'to save', ex: 'want + to부정사' },
        { s: 'My birthday [[was]] last Saturday, and my family and I [[eat]] out. There [[were]] [[lots of]] leftovers.', w: 1, fix: 'ate', ex: 'last Saturday → 과거형 ate' },
        { s: 'There were lots of leftovers, but we [[bringed]] them home. The next day, I [[made]] a nice lunch [[out of]] [[them]].', w: 0, fix: 'brought', ex: 'bring - brought - brought' },
        { s: 'I wanted [[to buy]] a new one, but I [[thinked]] again. I learned [[that]] reusing [[is]] important for zero-waste living.', w: 1, fix: 'thought', ex: 'think - thought - thought' },
        { s: "So, I decided [[fix]] it and [[reuse]] it. I'm not very [[good]] at [[sewing]].", w: 0, fix: 'to fix', ex: 'decide + to부정사' },
        { s: "I'm not very good at sewing, and I don't think [[that]] the bag [[look]] [[perfect]]. I [[guess]] it's all right.", w: 1, fix: 'looks', ex: '주어 the bag은 3인칭 단수 → looks' }
      ]},
      { type: 'scramble', title: '본문 스크램블', guide: '우리말에 맞게 단어를 눌러 문장을 완성하세요.', items: [
        { ko: '여러분은 지구를 구하고 싶나요?', en: 'Do you want to save the Earth?' },
        { ko: '그렇다면 제로 웨이스트 챌린지에 동참하고 여러분의 이야기를 공유해 주세요.', en: 'Then, join the zero-waste challenge, and share your stories.' },
        { ko: '남은 음식이 많았지만, 우리는 그것들을 집으로 가져왔어.', en: 'There were lots of leftovers, but we brought them home.' },
        { ko: '그다음 날, 나는 그것들로 맛있는 점심을 만들었어.', en: 'The next day, I made a nice lunch out of them.' },
        { ko: '나는 재사용이 제로 웨이스트 생활에 중요하다고 배웠어.', en: 'I learned that reusing is important for zero-waste living.' },
        { ko: '그래서 나는 그것을 수선해서 재사용하기로 결심했어.', en: 'So, I decided to fix it and reuse it.' },
        { ko: '나는 바느질을 아주 잘하지는 못해.', en: "I'm not very good at sewing." }
      ]},
      { type: 'order', title: '문장순서', guide: '문장을 본문 순서대로 눌러서 배열하세요.', items: [
        { lines: [
          'Every day, we produce lots of waste, and the Earth is getting sicker and sicker.',
          'Do you want to save the Earth?',
          'Then, join the zero-waste challenge, and share your stories.'
        ]},
        { lines: [
          'My birthday was last Saturday, and my family and I ate out.',
          'There were lots of leftovers, but we brought them home.',
          'The next day, I made a nice lunch out of them.',
          'FYI, you can find great cooking ideas for leftovers on the Internet.'
        ]},
        { lines: [
          'My dog tore my bag.',
          'I wanted to buy a new one, but I thought again.',
          'I learned that reusing is important for zero-waste living.',
          'So, I decided to fix it and reuse it.'
        ]},
        { lines: [
          'I learned that reusing is important for zero-waste living.',
          'So, I decided to fix it and reuse it.',
          "I'm not very good at sewing, and I don't think that the bag looks perfect.",
          "I guess it's all right."
        ]}
      ]},
      { type: 'insert', title: '문장삽입', guide: '주어진 문장이 들어가기에 가장 알맞은 곳을 고르세요.', items: [
        { lines: [
          'Every day, we produce lots of waste, and the Earth is getting sicker and sicker.',
          'Do you want to save the Earth?',
          'Then, join the zero-waste challenge, and share your stories.'
        ], given: 1, ex: 'Then(그렇다면)은 "지구를 구하고 싶나요?"라는 질문에 이어진다.' },
        { lines: [
          'My birthday was last Saturday, and my family and I ate out.',
          'There were lots of leftovers, but we brought them home.',
          'The next day, I made a nice lunch out of them.',
          'FYI, you can find great cooking ideas for leftovers on the Internet.'
        ], given: 2, ex: 'them은 집으로 가져온 남은 음식(leftovers)을 가리킨다.' },
        { lines: [
          'My dog tore my bag.',
          'I wanted to buy a new one, but I thought again.',
          'I learned that reusing is important for zero-waste living.',
          'So, I decided to fix it and reuse it.',
          "I'm not very good at sewing, and I don't think that the bag looks perfect."
        ], given: 3, ex: 'So(그래서) 앞에는 이유(재사용이 중요하다는 것을 배움)가 와야 한다.' }
      ]},
      { type: 'odd', title: '어색한 문장', guide: '글의 흐름과 관계없는 문장을 고르세요.', items: [
        { lines: [
          'Every day, we produce lots of waste, and the Earth is getting sicker and sicker.',
          'Do you want to save the Earth?',
          'Making more waste is good for the Earth.',
          'Then, join the zero-waste challenge, and share your stories.'
        ], odd: 2, ex: '쓰레기가 지구를 병들게 한다는 흐름과 반대된다.' },
        { lines: [
          'My birthday was last Saturday, and my family and I ate out.',
          'There were lots of leftovers, but we brought them home.',
          'We threw all the leftovers away at the restaurant.',
          'The next day, I made a nice lunch out of them.'
        ], odd: 2, ex: '남은 음식을 집으로 가져왔다는 내용과 반대된다.' },
        { lines: [
          'My dog tore my bag.',
          'I wanted to buy a new one, but I thought again.',
          'I learned that reusing is important for zero-waste living.',
          'Buying new things is the best way to save the Earth.',
          'So, I decided to fix it and reuse it.'
        ], odd: 3, ex: '재사용이 중요하다는 흐름과 맞지 않는다.' }
      ]},
      { type: 'blank', title: '빈칸추론', guide: '빈칸에 들어갈 말로 가장 알맞은 것을 고르세요.', items: [
        { s: 'Every day, we produce lots of waste, and the Earth is getting ____.', opts: ['sicker and sicker', 'healthier and healthier', 'cleaner and cleaner', 'bigger and bigger'], ex: '쓰레기 때문에 지구가 점점 더 병들고 있다.' },
        { s: 'There were lots of leftovers, but we ____.', opts: ['brought them home', 'threw them away', 'gave them to the dog', 'left them there'], ex: '음식물 쓰레기를 줄이기 위해 남은 음식을 집으로 가져왔다.' },
        { s: 'I learned that ____ is important for zero-waste living.', opts: ['reusing', 'buying new things', 'throwing things away', 'using plastic'], ex: '제로 웨이스트 생활에는 재사용이 중요하다.' },
        { s: 'So, I decided to ____ it and reuse it.', opts: ['fix', 'sell', 'throw', 'tear'], ex: '찢어진 가방을 고쳐서 다시 쓰기로 했다.' }
      ]},
      { type: 'mc', title: '핵심문법', guide: '알맞은 답을 고르세요.', items: [
        { q: '밑줄 친 to부정사의 쓰임이 나머지와 <b>다른</b> 것은?', opts: ['I went to the store <u>to buy</u> milk.', 'I want <u>to save</u> the Earth.', 'I decided <u>to fix</u> it.', 'She hopes <u>to visit</u> Paris.'], ex: '①은 목적(~하기 위해). 나머지는 동사의 목적어(~하는 것) → 명사적 용법' },
        { q: '빈칸에 들어갈 수 <b>없는</b> 것은?<br><b>I ______ to fix my bag.</b>', opts: ['enjoyed', 'wanted', 'decided', 'planned'], ex: 'enjoy는 동명사만 목적어로 쓴다 (enjoyed fixing).' },
        { q: '빈칸에 알맞은 것은?<br><b>I learned ______ reusing is important.</b>', opts: ['that', 'what', 'this', 'it'], ex: '완전한 문장을 이끄는 접속사 that' },
        { q: '밑줄 친 <b>that</b>을 생략할 수 있는 것은?', opts: ["I don't think <u>that</u> the bag looks perfect.", '<u>That</u> bag is mine.', 'Look at <u>that</u> dog.', '<u>That</u> is my bag.'], ex: '동사의 목적어 자리 접속사 that은 생략할 수 있다.' },
        { q: '동사의 과거형이 <b>틀린</b> 것은?', opts: ['bring - bringed', 'eat - ate', 'make - made', 'tear - tore'], ex: 'bring - brought' },
        { q: '빈칸에 알맞은 것은?<br><b>There ______ lots of leftovers yesterday.</b>', opts: ['were', 'was', 'are', 'is'], ex: '복수명사 + 과거 → There were' },
        { q: '"지구는 점점 더 병들고 있다."를 바르게 영작한 것은?', opts: ['The Earth is getting sicker and sicker.', 'The Earth is getting sick and sick.', 'The Earth is getting more sick and sick.', 'The Earth is getting sickest and sickest.'], ex: '비교급 and 비교급: 점점 더 ~한' },
        { q: '빈칸에 알맞은 것은?<br><b>Reusing old things ______ important.</b>', opts: ['is', 'are', 'be', 'were'], ex: '동명사 주어는 단수 취급 → is' },
        { q: '"나는 남은 음식으로 점심을 만들었다."를 바르게 영작한 것은?', opts: ['I made lunch out of the leftovers.', 'I made the leftovers out of lunch.', 'I made out of lunch the leftovers.', 'I made lunch the leftovers out of.'], ex: 'make A out of B: B로 A를 만들다' }
      ]}
    ]
  },

  /* ═══════════════════════════ DAY 2 · 본문 ❹❺ ═══════════════════════════ */
  {
    id: 'd2', name: 'DAY 2', range: '본문 ❹❺', story: 'Emma의 챌린지 · 민수의 챌린지',
    passage: [
      ['', '❹', ''],
      ['', 'Challenge 03 Say No to Single-Use Plastic', '챌린지 03 / 일회용 플라스틱 사용을 반대하세요'],
      ['Emma', "I often use food delivery services, but today I didn't.", '나는 종종 음식 배달 서비스를 이용하는데, 오늘은 이용하지 않았어.'],
      ['', 'Instead, I walked to my favorite restaurant with a reusable container and picked up the food.', '대신, 재사용할 수 있는 용기를 가지고 내가 가장 좋아하는 식당에 걸어가서 음식을 가져왔어.'],
      ['', 'I heard that plastic never goes away completely.', '플라스틱은 절대로 완전히 없어지지 않는다고 들었어.'],
      ['', "I didn't use any single-use plastic today.", '나는 오늘 어떤 일회용 플라스틱도 사용하지 않았어.'],
      ['', 'I felt good!', '기분이 좋았어!'],
      ['', '❺', ''],
      ['', 'Challenge 04 Recycle', '챌린지 04 / 재활용하세요'],
      ['Minsu', 'Yesterday, I took some plastic and glass bottles to a recycling machine near my house.', '어제 나는 플라스틱과 유리병 몇 개를 집 근처에 있는 재활용 기계에 가져갔어.'],
      ['', 'I put them into the machine one by one, and I got some points in return.', '나는 그것들을 하나씩 기계에 집어넣었고, 대가로 포인트를 받았어.'],
      ['', 'What can I do with those points?', '그 포인트로 무엇을 할 수 있냐고?'],
      ['', 'Well, I can use them like money.', '음, 나는 그것들을 돈처럼 사용할 수 있어.'],
      ['', "Don't you think that's cool?", '멋지다고 생각하지 않니?']
    ],
    steps: [
      { type: 'vocab', title: '핵심어휘·숙어', quizN: 15, items: [
        ['say no to', '~에 반대하다, ~을 거절하다'], ['single-use', '일회용의'], ['plastic', '플라스틱'], ['often', '종종, 자주'],
        ['delivery', '배달'], ['instead', '대신에'], ['favorite', '가장 좋아하는'], ['restaurant', '식당'],
        ['reusable', '재사용할 수 있는'], ['container', '용기, 그릇'], ['pick up', '(음식 등을) 찾아오다'], ['hear', '듣다'],
        ['never', '결코 ~않다'], ['go away', '없어지다'], ['completely', '완전히'], ['feel', '~한 기분이 들다'],
        ['recycle', '재활용하다'], ['take A to B', 'A를 B로 가져가다'], ['glass', '유리'], ['bottle', '병'],
        ['machine', '기계'], ['near', '~ 근처에'], ['put A into B', 'A를 B에 넣다'], ['one by one', '하나씩'],
        ['in return', '대가로, 답례로'], ['point', '포인트, 점수'], ['like (전치사)', '~처럼'], ['cool', '멋진; 시원한']
      ]},
      { type: 'pick', title: '어휘선택', guide: '문맥에 맞는 낱말을 고르세요.', items: [
        { s: 'Challenge 03 Say No to {Single-Use|Reusable} Plastic', ex: 'single-use: 일회용의' },
        { s: "I {often|never} use food delivery services, but today I didn't.", ex: '평소에는 종종(often) 쓰지만 오늘은 쓰지 않았다.' },
        { s: '{Instead|Also}, I walked to my favorite restaurant with a reusable container and picked up the food.', ex: 'instead: 대신에 (배달 대신 직접 갔다)' },
        { s: 'Instead, I walked to my favorite restaurant with a {reusable|single-use} container and picked up the food.', ex: '일회용 플라스틱을 쓰지 않으려고 재사용 용기를 가져갔다.' },
        { s: 'I heard that plastic never goes away {completely|quickly}.', ex: 'completely: 완전히' },
        { s: "I didn't use any single-use plastic today. I felt {good|bad}!", ex: '일회용 플라스틱을 쓰지 않아서 기분이 좋았다.' },
        { s: 'Yesterday, I took some plastic and glass bottles to a {recycling|washing} machine near my house.', ex: 'recycling machine: 재활용 기계' },
        { s: 'I put them into the machine {one by one|all at once}, and I got some points in return.', ex: 'one by one: 하나씩' },
        { s: 'I put them into the machine one by one, and I got some points {in return|in a hurry}.', ex: 'in return: 대가로' },
        { s: 'Well, I can use them {like|with} money.', ex: 'like: ~처럼' }
      ]},
      { type: 'tf', title: 'T/F 내용 확인', guide: '본문 내용과 일치하면 T, 다르면 F를 고르세요.', items: [
        ['Emma never uses food delivery services.', false, 'Emma는 종종(often) 배달 서비스를 이용한다.'],
        ['Emma walked to her favorite restaurant today.', true, 'I walked to my favorite restaurant'],
        ['Emma took a reusable container to the restaurant.', true, 'with a reusable container'],
        ['Emma heard that plastic goes away quickly.', false, '플라스틱은 절대 완전히 없어지지 않는다고 들었다.'],
        ['Emma used some single-use plastic today.', false, '오늘은 일회용 플라스틱을 전혀 쓰지 않았다.'],
        ['Minsu took some bottles to a recycling machine near his house.', true, 'to a recycling machine near my house'],
        ['Minsu got some money from the machine.', false, '돈이 아니라 포인트(points)를 받았다.'],
        ['Minsu can use the points like money.', true, 'I can use them like money.']
      ]},
      { type: 'mc', title: '일치·불일치', guide: "본문을 읽고 내용과 맞는지 확인해요. 틀린 선택지는 해설의 근거 문장과 비교해 보세요.", items: [
        { n: "❹", box: ["❹"], q: "Emma에 관한 내용과 일치하지 <u>않는</u> 것은?", opts: ["Emma used food delivery services today.", "Emma walked to her favorite restaurant.", "Emma took a reusable container with her.", "Emma heard that plastic never goes away completely.", "Emma felt good."], ex: "정답 근거: I often use food delivery services, but today I didn't.\n· delivery : 배달 · reusable : 재사용할 수 있는 · container : 용기", per: [["Emma는 오늘 음식 배달 서비스를 이용했다.", "but today I didn't", "불일치 → 오늘은 이용하지 않음"], ["Emma는 가장 좋아하는 식당에 걸어갔다.", "I walked to my favorite restaurant", "일치"], ["Emma는 재사용 용기를 가지고 갔다.", "with a reusable container", "일치"], ["Emma는 플라스틱이 절대 완전히 사라지지 않는다고 들었다.", "plastic never goes away completely", "일치"], ["Emma는 기분이 좋았다.", "I felt good", "일치"]] },
        { n: "❺", box: ["❺"], q: "Minsu에 관한 내용과 <u>일치하는</u> 것은?", opts: ["Minsu can use the points like money.", "Minsu took paper and cans to the machine.", "The recycling machine is far from Minsu's house.", "Minsu put all the bottles into the machine at once.", "Minsu got some money from the machine."], ex: "정답 근거: Well, I can use them like money.\n· one by one : 하나씩 · in return : 대가로", per: [["민수는 포인트를 돈처럼 쓸 수 있다.", "I can use them like money", "일치"], ["민수는 종이와 캔을 기계에 가져갔다.", "I took some plastic and glass bottles", "불일치 → 플라스틱과 유리병"], ["재활용 기계는 민수의 집에서 멀다.", "a recycling machine near my house", "불일치 → 집 근처"], ["민수는 병을 한꺼번에 기계에 넣었다.", "one by one", "불일치 → 하나씩"], ["민수는 기계에서 돈을 받았다.", "I got some points in return", "불일치 → 돈이 아니라 포인트"]] }
      ]},
      { type: 'pick', title: '어법선택', guide: '어법상 알맞은 것을 고르세요.', items: [
        { s: "I {often use|use often} food delivery services, but today I didn't.", ex: '빈도부사는 일반동사 앞에' },
        { s: "I often use food delivery services, but today I {didn't|don't}.", ex: 'today 오늘 있었던 일(과거) → didn\'t' },
        { s: 'Instead, I {walked|walk} to my favorite restaurant with a reusable container and picked up the food.', ex: 'picked와 병렬 → 과거형 walked' },
        { s: 'Instead, I walked to my favorite restaurant with a reusable container and {picked|picks} up the food.', ex: 'walked와 병렬 → picked' },
        { s: 'I heard {that|what} plastic never goes away completely.', ex: '뒤에 완전한 문장 → 접속사 that' },
        { s: 'I heard that plastic never {goes|go} away completely.', ex: '주어 plastic은 단수 → goes' },
        { s: "I didn't {use|used} any single-use plastic today.", ex: "didn't + 동사원형" },
        { s: 'Yesterday, I {took|take} some plastic and glass bottles to a recycling machine near my house.', ex: 'Yesterday → 과거형 took' },
        { s: 'I put them into the machine one by one, and I {got|get} some points in return.', ex: '과거 이야기 → got' },
        { s: 'What can I {do|did} with those points?', ex: '조동사 can + 동사원형' },
        { s: "{Don't|Doesn't} you think that's cool?", ex: '주어 you → Don\'t' }
      ]},
      { type: 'verb', title: '동사변형', guide: '( ) 안의 동사를 알맞은 형태로 바꿔 쓰세요. 과거형에 주의!', items: [
        { s: "I often ___ food delivery services, but today I didn't.", v: 'use', a: ['use'], ex: '평소 습관 → 현재형' },
        { s: 'Instead, I ___ to my favorite restaurant with a reusable container and picked up the food.', v: 'walk', a: ['walked'], ex: '과거형 walked' },
        { s: 'Instead, I walked to my favorite restaurant with a reusable container and ___ up the food.', v: 'pick', a: ['picked'], ex: '과거형 picked' },
        { s: 'I ___ that plastic never goes away completely.', v: 'hear', a: ['heard'], ex: 'hear - heard - heard' },
        { s: 'I heard that plastic never ___ away completely.', v: 'go', a: ['goes'], ex: '사실·일반적 진리 → 현재형, 주어 단수 → goes' },
        { s: "I didn't ___ any single-use plastic today.", v: 'use', a: ['use'], ex: "didn't + 동사원형" },
        { s: 'I ___ good!', v: 'feel', a: ['felt'], ex: 'feel - felt - felt' },
        { s: 'Yesterday, I ___ some plastic and glass bottles to a recycling machine near my house.', v: 'take', a: ['took'], ex: 'take - took - taken' },
        { s: 'I ___ them into the machine one by one, and I got some points in return.', v: 'put', a: ['put'], ex: 'put - put - put (과거형도 put)' },
        { s: 'I put them into the machine one by one, and I ___ some points in return.', v: 'get', a: ['got'], ex: 'get - got - got/gotten' }
      ]},
      { type: 'error', title: '오류찾기', guide: '어법상 틀린 곳을 고르세요.', items: [
        { s: "I [[often use]] food delivery services, but today I [[don't]]. Instead, I [[walked]] to my [[favorite]] restaurant.", w: 1, fix: "didn't", ex: '오늘 있었던 일 → 과거 didn\'t' },
        { s: 'Instead, I [[walked]] to my favorite restaurant [[with]] a reusable container and [[pick]] up [[the food]].', w: 2, fix: 'picked', ex: 'walked와 병렬 → picked' },
        { s: "I heard [[what]] plastic never [[goes]] away [[completely]]. I didn't use [[any]] single-use plastic today.", w: 0, fix: 'that', ex: '뒤에 완전한 문장 → 접속사 that' },
        { s: "I didn't [[used]] any single-use plastic today. I [[felt]] [[good]]!", w: 0, fix: 'use', ex: "didn't + 동사원형" },
        { s: 'Yesterday, I [[take]] some plastic and glass bottles [[to]] a recycling machine [[near]] my [[house]].', w: 0, fix: 'took', ex: 'Yesterday → 과거형 took' },
        { s: 'I put them [[into]] the machine [[one by one]], and I [[getted]] some points [[in return]].', w: 2, fix: 'got', ex: 'get - got' },
        { s: 'What can I [[did]] with those points? Well, I can [[use]] them [[like]] money.', w: 0, fix: 'do', ex: '조동사 can + 동사원형' }
      ]},
      { type: 'scramble', title: '본문 스크램블', guide: '우리말에 맞게 단어를 눌러 문장을 완성하세요.', items: [
        { ko: '나는 종종 음식 배달 서비스를 이용해.', en: 'I often use food delivery services.' },
        { ko: '플라스틱은 절대로 완전히 없어지지 않는다고 들었어.', en: 'I heard that plastic never goes away completely.' },
        { ko: '나는 오늘 어떤 일회용 플라스틱도 사용하지 않았어.', en: "I didn't use any single-use plastic today." },
        { ko: '나는 그것들을 하나씩 기계에 집어넣었어.', en: 'I put them into the machine one by one.' },
        { ko: '나는 대가로 포인트를 받았어.', en: 'I got some points in return.' },
        { ko: '그 포인트로 무엇을 할 수 있을까?', en: 'What can I do with those points?' },
        { ko: '음, 나는 그것들을 돈처럼 사용할 수 있어.', en: 'Well, I can use them like money.' },
        { ko: '멋지다고 생각하지 않니?', en: "Don't you think that's cool?" }
      ]},
      { type: 'order', title: '문장순서', guide: '문장을 본문 순서대로 눌러서 배열하세요.', items: [
        { lines: [
          "I often use food delivery services, but today I didn't.",
          'Instead, I walked to my favorite restaurant with a reusable container and picked up the food.',
          'I heard that plastic never goes away completely.',
          "I didn't use any single-use plastic today.",
          'I felt good!'
        ]},
        { lines: [
          'Yesterday, I took some plastic and glass bottles to a recycling machine near my house.',
          'I put them into the machine one by one, and I got some points in return.',
          'What can I do with those points?',
          'Well, I can use them like money.',
          "Don't you think that's cool?"
        ]},
        { lines: [
          'I put them into the machine one by one, and I got some points in return.',
          'What can I do with those points?',
          'Well, I can use them like money.',
          "Don't you think that's cool?"
        ]}
      ]},
      { type: 'insert', title: '문장삽입', guide: '주어진 문장이 들어가기에 가장 알맞은 곳을 고르세요.', items: [
        { lines: [
          "I often use food delivery services, but today I didn't.",
          'Instead, I walked to my favorite restaurant with a reusable container and picked up the food.',
          'I heard that plastic never goes away completely.',
          "I didn't use any single-use plastic today.",
          'I felt good!'
        ], given: 1, ex: 'Instead(대신에)는 "오늘은 배달을 이용하지 않았다" 다음에 온다.' },
        { lines: [
          'Instead, I walked to my favorite restaurant with a reusable container and picked up the food.',
          'I heard that plastic never goes away completely.',
          "I didn't use any single-use plastic today.",
          'I felt good!'
        ], given: 3, ex: '일회용 플라스틱을 쓰지 않아서 기분이 좋았다.' },
        { lines: [
          'Yesterday, I took some plastic and glass bottles to a recycling machine near my house.',
          'I put them into the machine one by one, and I got some points in return.',
          'What can I do with those points?',
          'Well, I can use them like money.'
        ], given: 1, ex: 'them은 앞 문장의 plastic and glass bottles를 가리킨다.' },
        { lines: [
          'I put them into the machine one by one, and I got some points in return.',
          'What can I do with those points?',
          'Well, I can use them like money.',
          "Don't you think that's cool?"
        ], given: 2, ex: '"포인트로 무엇을 할 수 있을까?"라는 질문에 대한 대답이다.' }
      ]},
      { type: 'odd', title: '어색한 문장', guide: '글의 흐름과 관계없는 문장을 고르세요.', items: [
        { lines: [
          "I often use food delivery services, but today I didn't.",
          'Instead, I walked to my favorite restaurant with a reusable container and picked up the food.',
          'I asked the restaurant for lots of plastic bags.',
          'I heard that plastic never goes away completely.',
          "I didn't use any single-use plastic today."
        ], odd: 2, ex: '일회용 플라스틱을 쓰지 않으려 했다는 흐름과 반대된다.' },
        { lines: [
          'I heard that plastic never goes away completely.',
          "I didn't use any single-use plastic today.",
          'I felt good!',
          'Single-use plastic is good for the Earth.'
        ], odd: 3, ex: '플라스틱이 없어지지 않아 지구에 해롭다는 흐름과 맞지 않는다.' },
        { lines: [
          'Yesterday, I took some plastic and glass bottles to a recycling machine near my house.',
          'I put them into the machine one by one, and I got some points in return.',
          'The machine was broken, so I threw the bottles away.',
          'What can I do with those points?',
          'Well, I can use them like money.'
        ], odd: 2, ex: '병을 기계에 넣고 포인트를 받았다는 내용과 반대된다.' }
      ]},
      { type: 'blank', title: '빈칸추론', guide: '빈칸에 들어갈 말로 가장 알맞은 것을 고르세요.', items: [
        { s: 'Instead, I walked to my favorite restaurant with ____ and picked up the food.', opts: ['a reusable container', 'a plastic bag', 'a paper cup', 'a delivery box'], ex: '일회용 플라스틱을 쓰지 않으려고 재사용 용기를 가져갔다.' },
        { s: 'I heard that plastic ____ completely.', opts: ['never goes away', 'goes away quickly', 'is good for the Earth', 'is easy to make'], ex: '플라스틱은 절대 완전히 없어지지 않는다.' },
        { s: 'I put them into the machine one by one, and I got ____.', opts: ['some points in return', 'some new bottles', 'a lot of trash', 'a plastic bag'], ex: '병을 넣고 대가로 포인트를 받았다.' },
        { s: 'Well, I can use them ____.', opts: ['like money', 'like plastic', 'like bottles', 'like trash'], ex: '포인트는 돈처럼 쓸 수 있다.' }
      ]},
      { type: 'mc', title: '핵심문법', guide: '알맞은 답을 고르세요.', items: [
        { q: '빈도부사의 위치가 <b>틀린</b> 것은?', opts: ['She always is busy.', 'She is always busy.', 'I never eat breakfast.', 'We can often see stars.'], ex: 'be동사 뒤에 빈도부사 → She is always busy.' },
        { q: '어법상 올바른 문장은?', opts: ['I often use delivery services.', 'I use often delivery services.', 'Often I uses delivery services.', 'I often am late.'], ex: '빈도부사는 일반동사 앞, be동사·조동사 뒤' },
        { q: '대화의 빈칸에 알맞은 것은?<br><b>A: Don\'t you think that\'s cool?<br>B: ______ It\'s really cool.</b>', opts: ['Yes, I do.', 'No, I do.', "Yes, I don't.", "No, I don't."], ex: '부정의문문이어도 대답 내용이 긍정이면 Yes, 부정이면 No' },
        { q: '대화의 빈칸에 알맞은 것은?<br><b>A: Don\'t you like coffee?<br>B: ______ I don\'t like it.</b>', opts: ["No, I don't.", "Yes, I don't.", 'No, I do.', 'Yes, I do.'], ex: '좋아하지 않는다(부정) → No, I don\'t.' },
        { q: '빈칸에 알맞은 것은?<br><b>I heard ______ plastic never goes away.</b>', opts: ['that', 'what', 'this', 'it'], ex: '완전한 문장을 이끄는 접속사 that' },
        { q: '동사의 과거형이 <b>틀린</b> 것은?', opts: ['take - taked', 'put - put', 'get - got', 'feel - felt'], ex: 'take - took' },
        { q: '빈칸에 알맞은 것은?<br><b>I didn\'t use ______ single-use plastic today.</b>', opts: ['any', 'some', 'a', 'many'], ex: '부정문에서는 any (어떤 ~도)' },
        { q: '"나는 병들을 재활용 기계로 가져갔다."를 바르게 영작한 것은?', opts: ['I took the bottles to a recycling machine.', 'I took to a recycling machine the bottles.', 'I taked the bottles to a recycling machine.', 'I take the bottles a recycling machine to.'], ex: 'take A to B: A를 B로 가져가다' },
        { q: '빈칸에 알맞은 것은?<br><b>I put them ______ the machine one by one.</b>', opts: ['into', 'out', 'at', 'from'], ex: 'put A into B: A를 B에 넣다' }
      ]}
    ]
  },

  /* ═══════════════════════════ DAY 3 · Lesson 7 본문 ❶❷❸ ═══════════════════════════ */
  { id: 'd3', name: 'DAY 3', range: '7과 본문 ❶❷❸', story: 'Lesson 7 · 감독 Jim · 야외 촬영 관리자 Anna · 촬영감독 Peter', passage: [['', '❶', ''], ['Jim Brown', 'Hi, I\'m Jim Brown, the director of Happy Days.', '안녕하세요, 나는 \'Happy Days\'의 감독 Jim Brown이에요.'], ['', 'It\'s a movie about the friendship between Tom and his dog Max.', '이것은 Tom과 그의 개 Max의 우정에 관한 영화예요.'], ['', 'A lot of people are working hard to create this movie.', '많은 사람들이 이 영화를 만들기 위해 열심히 일하고 있어요.'], ['', 'Do you want to meet some of them?', '그들 중 몇 명을 만나 보고 싶나요?'], ['', '❷', ''], ['Anna', 'I\'m Anna, and I found this beautiful beach.', '나는 Anna이고, 내가 이 아름다운 해변을 찾아냈어요.'], ['', 'I\'m a location manager, and my job is to find perfect places for shooting.', '나는 야외 촬영 관리자이고, 내 일은 촬영을 위한 완벽한 장소를 찾는 거예요.'], ['', 'Of course, it is not easy, but I love my job.', '물론, 이 일은 쉽지 않지만, 나는 내 일을 정말 좋아해요.'], ['', 'I like to travel and enjoy challenges.', '나는 여행하는 것을 좋아하고 도전을 즐겨요.'], ['', '❸', ''], ['Peter', 'I\'m Peter, the director of photography for this movie.', '나는 이 영화의 촬영감독인 Peter예요.'], ['', 'I\'m in charge of all the cameras.', '나는 모든 카메라를 담당하고 있어요.'], ['', 'Today, Tom and Max are going to play together with a ball on the beach.', '오늘, Tom과 Max는 해변에서 공을 가지고 함께 놀 예정이에요.'], ['', 'To capture their happy moments, I\'m going to use drones.', '그들의 행복한 순간을 포착하기 위해, 나는 드론을 사용할 거예요.']], steps: [
    { type: 'vocab', title: '핵심어휘·숙어', quizN: 15, items: [['director', '감독, 책임자', '❶'], ['friendship', '우정', '❶'], ['between A and B', 'A와 B 사이에', '❶'], ['a lot of', '많은', '❶'], ['work hard', '열심히 일하다', '❶'], ['create', '만들다, 창조하다', '❶'], ['some of them', '그들 중 몇 명', '❶'], ['find', '찾다, 발견하다 (과거 found)', '❷'], ['beach', '해변', '❷'], ['location manager', '야외 촬영 관리자', '❷'], ['perfect', '완벽한', '❷'], ['place', '장소', '❷'], ['shooting', '촬영', '❷'], ['of course', '물론', '❷'], ['easy', '쉬운', '❷'], ['travel', '여행하다', '❷'], ['enjoy', '즐기다', '❷'], ['challenge', '도전', '❷'], ['director of photography', '촬영감독', '❸'], ['be in charge of', '~을 담당하다', '❸'], ['be going to', '~할 것이다, ~할 예정이다', '❸'], ['together', '함께', '❸'], ['capture', '포착하다, 담아내다', '❸'], ['moment', '순간', '❸'], ['drone', '드론', '❸']] },
    { type: 'pick', title: '어휘선택', guide: '문맥에 맞는 낱말을 고르세요.', items: [
      { s: 'It\'s a movie about the {friendship|fight} between Tom and his dog Max.', ex: 'friendship 우정 vs fight 싸움' },
      { s: 'A lot of people are working hard to {create|break} this movie.', ex: '영화를 \'만들기\' 위해 → create' },
      { s: 'I\'m Anna, and I {found|lost} this beautiful beach.', ex: 'found 찾아냈다(find의 과거) vs lost 잃어버렸다' },
      { s: 'I\'m a location manager, and my job is to find {perfect|terrible} places for shooting.', ex: '촬영을 위한 \'완벽한\' 장소 → perfect' },
      { s: 'Of course, it is not {easy|hard}, but I love my job.', ex: 'but I love my job → 일이 \'쉽지 않지만\' 좋아함' },
      { s: 'I like to travel and enjoy {challenges|vacations}.', ex: 'challenge 도전 vs vacation 방학, 휴가' },
      { s: 'I\'m in {charge|change} of all the cameras.', ex: 'be in charge of ~을 담당하다 (change 바꾸다와 헷갈리지 않기)' },
      { s: 'To {capture|lose} their happy moments, I\'m going to use drones.', ex: '행복한 순간을 \'포착하기\' 위해 → capture' }
    ] },
    { type: 'tf', title: 'T/F 내용 확인', guide: '본문 내용과 일치하면 T, 다르면 F를 고르세요.', items: [['Jim Brown is the director of the movie Happy Days.', true, 'Jim Brown은 \'Happy Days\'의 감독이다.', '❶', 'the director of Happy Days'], ['Happy Days is a movie about the friendship between Tom and his cat.', false, '고양이가 아니라 개(his dog Max)와의 우정', '❶', 'the friendship between Tom and his dog Max'], ['Only a few people are working on the movie.', false, '많은 사람들(A lot of people)이 일하고 있다.', '❶', 'A lot of people are working hard'], ['Anna found the beach for the movie.', true, 'Anna가 이 해변을 찾아냈다.', '❷', 'I found this beautiful beach'], ['Anna thinks her job is very easy.', false, '쉽지 않다(not easy)고 했다.', '❷', 'it is not easy'], ['Anna likes to travel.', true, '여행하는 것을 좋아한다.', '❷', 'I like to travel'], ['Peter is in charge of all the cameras.', true, '모든 카메라를 담당한다.', '❸', 'I\'m in charge of all the cameras'], ['Peter is going to use a phone to capture Tom and Max.', false, '휴대폰이 아니라 드론(drones)을 사용한다.', '❸', 'I\'m going to use drones']] },
    { type: 'mc', title: '일치·불일치', guide: '선택지는 본문을 어려운 어휘로 바꿔 쓴 문장이에요. 풀고 나서 해설의 어휘를 꼭 확인하세요.', items: [
      { n: '❷', box: ['❷'], q: 'Anna에 관한 내용과 일치하지 <u>않는</u> 것은?', opts: ['Anna\'s job is to find good actors for the movie.', 'Anna found the beautiful beach.', 'Anna is a location manager.', 'Anna loves her job.', 'Anna enjoys challenges.'], ex: '정답 근거: my job is to find perfect places for shooting (배우가 아니라 촬영 장소를 찾는 일)\n· location manager 야외 촬영 관리자 · challenge 도전', per: [['Anna의 일은 영화에 나올 좋은 배우를 찾는 것이다.', 'my job is to find perfect places for shooting', '불일치 → 촬영 장소를 찾음'], ['Anna는 아름다운 해변을 찾아냈다.', 'I found this beautiful beach', '일치'], ['Anna는 야외 촬영 관리자이다.', 'I\'m a location manager', '일치'], ['Anna는 자기 일을 정말 좋아한다.', 'but I love my job', '일치'], ['Anna는 도전을 즐긴다.', 'I like to travel and enjoy challenges', '일치']] },
      { n: '❸', box: ['❶', '❸'], q: '글의 내용과 <u>일치하는</u> 것은?', opts: ['Tom and Max are going to play with a ball on the beach today.', 'Happy Days is a movie about Tom and his cat.', 'Peter is the director of Happy Days.', 'Peter is in charge of only one camera.', 'Peter is going to use a big truck to film Tom and Max.'], ex: '정답 근거: Today, Tom and Max are going to play together with a ball on the beach.\n· be going to ~할 예정이다 · be in charge of ~을 담당하다 · drone 드론', per: [['Tom과 Max는 오늘 해변에서 공을 가지고 놀 예정이다.', 'Today, Tom and Max are going to play together with a ball on the beach', '일치'], ['\'Happy Days\'는 Tom과 그의 고양이에 관한 영화이다.', 'the friendship between Tom and his dog Max', '불일치 → 개'], ['Peter는 \'Happy Days\'의 감독이다.', 'I\'m Peter, the director of photography', '불일치 → 촬영감독 (감독은 Jim Brown)'], ['Peter는 카메라 한 대만 담당한다.', 'I\'m in charge of all the cameras', '불일치 → 모든 카메라'], ['Peter는 큰 트럭을 사용해서 촬영할 것이다.', 'I\'m going to use drones', '불일치 → 드론']] }
    ] },
    { type: 'pick', title: '어법선택', guide: '어법상 알맞은 것을 고르세요.', items: [
      { s: 'It\'s a movie about the friendship {between|among} Tom and his dog Max.', ex: '둘 사이 → between A and B' },
      { s: 'A lot of people {are|is} working hard to create this movie.', ex: '주어 A lot of people(복수) → are' },
      { s: 'A lot of people are working hard {to create|create} this movie.', ex: '목적(~하기 위해) → to부정사' },
      { s: 'Do you want {to meet|meeting} some of them?', ex: 'want + to부정사' },
      { s: 'I\'m a location manager, and my job is {to find|find} perfect places for shooting.', ex: '보어 자리 \'찾는 것\' → to부정사(명사적 용법)' },
      { s: 'I\'m a location manager, and my job is to find perfect places for {shooting|shoot}.', ex: '전치사 for + 동명사/명사' },
      { s: 'I like to travel and {enjoy|enjoys} challenges.', ex: '주어 I → enjoy (like와 병렬)' },
      { s: 'I\'m {in|on} charge of all the cameras.', ex: 'be in charge of ~을 담당하다' },
      { s: 'Today, Tom and Max are going to {play|playing} together with a ball on the beach.', ex: 'be going to + 동사원형' },
      { s: 'To capture their happy moments, I\'m going to {use|used} drones.', ex: 'be going to + 동사원형' }
    ] },
    { type: 'verb', title: '동사변형', guide: '( ) 안의 동사를 알맞은 형태로 바꿔 쓰세요.', items: [
      { s: 'A lot of people are ___ hard to create this movie.', v: 'work', a: ['working'], ex: '현재진행형 be + -ing' },
      { s: 'A lot of people are working hard ___ this movie.', v: 'create', a: ['to create'], ex: '목적의 to부정사' },
      { s: 'Do you want ___ some of them?', v: 'meet', a: ['to meet'], ex: 'want + to부정사' },
      { s: 'I\'m Anna, and I ___ this beautiful beach.', v: 'find', a: ['found'], ex: 'find - found - found (과거)' },
      { s: 'I\'m a location manager, and my job is ___ perfect places for shooting.', v: 'find', a: ['to find'], ex: '보어 자리 to부정사' },
      { s: 'I like ___ and enjoy challenges.', v: 'travel', a: ['to travel', 'traveling'], ex: 'like + to부정사/동명사 (본문: to travel)' },
      { s: 'Today, Tom and Max are going ___ together with a ball on the beach.', v: 'play', a: ['to play'], ex: 'be going to + 동사원형' },
      { s: 'To ___ their happy moments, I\'m going to use drones.', v: 'capture', a: ['capture'], ex: 'To + 동사원형 (목적)' }
    ] },
    { type: 'error', title: '오류찾기', guide: '어법상 틀린 곳을 고르세요.', items: [
      { s: 'A lot of people [[is]] working [[hard]] [[to create]] this movie. Do you want [[to meet]] some of them?', w: 0, fix: 'are', ex: '주어 A lot of people(복수) → are' },
      { s: 'I\'m Anna, and I [[found]] this beautiful beach. I\'m a location manager, and my job [[is]] [[find]] perfect places [[for]] shooting.', w: 2, fix: 'to find', ex: '보어 자리 → to find' },
      { s: 'Of course, it [[is]] not easy, [[but]] I love my job. I like to travel and [[enjoys]] [[challenges]].', w: 2, fix: 'enjoy', ex: '주어 I → enjoy' },
      { s: 'I\'m [[in]] charge of all the cameras. Today, Tom and Max [[are]] going to [[playing]] together with a ball [[on]] the beach.', w: 2, fix: 'play', ex: 'be going to + 동사원형' },
      { s: '[[Capture]] their happy moments, I\'m [[going]] [[to]] [[use]] drones.', w: 0, fix: 'To capture', ex: '\'~하기 위해\' → To capture' }
    ] },
    { type: 'scramble', title: '본문 스크램블', guide: '우리말에 맞게 단어를 눌러 문장을 완성하세요.', items: [
      { ko: '이것은 Tom과 그의 개 Max의 우정에 관한 영화예요.', en: 'It\'s a movie about the friendship between Tom and his dog Max.' },
      { ko: '많은 사람들이 이 영화를 만들기 위해 열심히 일하고 있어요.', en: 'A lot of people are working hard to create this movie.' },
      { ko: '나는 야외 촬영 관리자이고, 내 일은 촬영을 위한 완벽한 장소를 찾는 거예요.', en: 'I\'m a location manager, and my job is to find perfect places for shooting.' },
      { ko: '나는 여행하는 것을 좋아하고 도전을 즐겨요.', en: 'I like to travel and enjoy challenges.' },
      { ko: '나는 모든 카메라를 담당하고 있어요.', en: 'I\'m in charge of all the cameras.' },
      { ko: '그들의 행복한 순간을 포착하기 위해, 나는 드론을 사용할 거예요.', en: 'To capture their happy moments, I\'m going to use drones.' }
    ] },
    { type: 'order', title: '문장순서', guide: '문장을 본문 순서대로 눌러서 배열하세요.', items: [
      { lines: ['Hi, I\'m Jim Brown, the director of Happy Days.', 'It\'s a movie about the friendship between Tom and his dog Max.', 'A lot of people are working hard to create this movie.', 'Do you want to meet some of them?'], flow: ['Jim Brown 감독 소개', 'Tom과 개 Max의 우정에 관한 영화', '많은 사람들이 영화를 만들려고 일함', '그들 중 몇 명을 만나 볼까?'] },
      { lines: ['I\'m Anna, and I found this beautiful beach.', 'I\'m a location manager, and my job is to find perfect places for shooting.', 'Of course, it is not easy, but I love my job.', 'I like to travel and enjoy challenges.'], flow: ['Anna가 해변을 찾아냄', '야외 촬영 관리자, 촬영 장소 찾기', '쉽지 않지만 일을 좋아함', '여행과 도전을 즐김'] },
      { lines: ['I\'m Peter, the director of photography for this movie.', 'I\'m in charge of all the cameras.', 'Today, Tom and Max are going to play together with a ball on the beach.', 'To capture their happy moments, I\'m going to use drones.'], flow: ['촬영감독 Peter', '모든 카메라 담당', '오늘 Tom과 Max가 해변에서 놀 예정', '드론으로 행복한 순간 포착'] }
    ] },
    { type: 'insert', title: '문장삽입', guide: '주어진 문장이 들어가기에 가장 알맞은 곳을 고르세요.', items: [
      { lines: ['It\'s a movie about the friendship between Tom and his dog Max.', 'A lot of people are working hard to create this movie.', 'Do you want to meet some of them?'], given: 1, flow: ['Tom과 Max의 영화', '많은 사람들이 이 영화(this movie)를 만들려고 일함', '그들(them) 중 몇 명을 만나 볼까?'], ex: 'them은 앞 문장의 A lot of people을 가리킨다.' },
      { lines: ['I\'m a location manager, and my job is to find perfect places for shooting.', 'Of course, it is not easy, but I love my job.', 'I like to travel and enjoy challenges.'], given: 1, flow: ['내 일은 촬영 장소를 찾는 것', '물론 그것(it)은 쉽지 않지만 일을 좋아함', '여행과 도전을 즐김'], ex: 'it은 앞 문장의 \'촬영 장소를 찾는 일\'을 가리킨다.' },
      { lines: ['I\'m in charge of all the cameras.', 'Today, Tom and Max are going to play together with a ball on the beach.', 'To capture their happy moments, I\'m going to use drones.'], given: 2, flow: ['모든 카메라 담당', 'Tom과 Max가 해변에서 놀 예정', '그들의(their) 행복한 순간을 드론으로 포착'], ex: 'their는 Tom과 Max를 가리키므로 두 사람이 나온 뒤에 와야 한다.' }
    ] },
    { type: 'odd', title: '어색한 문장', guide: '글의 흐름과 관계없는 문장을 고르세요.', items: [
      { lines: ['It\'s a movie about the friendship between Tom and his dog Max.', 'A lot of people are working hard to create this movie.', 'Movie tickets are very expensive these days.', 'Do you want to meet some of them?'], odd: 2, ex: '영화표 가격 → 영화를 만드는 사람들 이야기와 관계없음' },
      { lines: ['I\'m a location manager, and my job is to find perfect places for shooting.', 'Of course, it is not easy, but I love my job.', 'I don\'t like going to new places at all.', 'I like to travel and enjoy challenges.'], odd: 2, ex: '새로운 곳에 가기 싫다 → 여행과 도전을 즐긴다는 내용과 반대' },
      { lines: ['I\'m in charge of all the cameras.', 'Today, Tom and Max are going to play together with a ball on the beach.', 'Drones are not allowed near the beach.', 'To capture their happy moments, I\'m going to use drones.'], odd: 2, ex: '드론 금지 → 드론을 사용한다는 내용과 맞지 않음' }
    ] },
    { type: 'blank', title: '빈칸추론', guide: '빈칸에 들어갈 말로 가장 알맞은 것을 고르세요.', items: [
      { s: 'A lot of people are working hard ____.', opts: ['to create this movie', 'to watch this movie', 'to sell tickets', 'to go home'], ex: '영화를 \'만들기 위해\' 일함' },
      { s: 'I\'m a location manager, and my job is to find ____ for shooting.', opts: ['perfect places', 'good actors', 'new cameras', 'funny stories'], ex: '야외 촬영 관리자 → 촬영 장소' },
      { s: 'To capture their happy moments, I\'m going to use ____.', opts: ['drones', 'hand signals', 'rice', 'books'], ex: '촬영감독 Peter → 드론' }
    ] },
    { type: 'mc', title: '핵심문법', guide: '알맞은 답을 고르세요.', items: [
      { q: '빈칸에 알맞은 것은?<br><b>My dream is ______ a chef.</b>', opts: ['to be', 'be', 'is', 'been'], ex: '보어 자리 to부정사(명사적 용법): ~하는 것' },
      { q: '밑줄 친 부분의 쓰임이 <b>나머지와 다른</b> 것은?', opts: ['A lot of people are working hard <u>to create</u> this movie.', 'My job is <u>to find</u> perfect places.', 'I like <u>to travel</u>.', 'Do you want <u>to meet</u> some of them?'], ex: '①은 \'~하기 위해\'(목적, 부사적 용법). 나머지는 \'~하는 것\'(명사적 용법)' },
      { q: '빈칸에 알맞은 것은?<br><b>I went to the library ______ some books.</b>', opts: ['to borrow', 'borrow', 'borrowed', 'borrows'], ex: '목적(~하기 위해) → to부정사' },
      { q: '우리말과 같도록 할 때 빈칸에 알맞은 것은?<br>나는 모든 카메라를 담당하고 있다.<br><b>I\'m in ______ of all the cameras.</b>', opts: ['charge', 'change', 'chance', 'chair'], ex: 'be in charge of ~을 담당하다' },
      { q: '빈칸에 알맞은 것은?<br><b>Tom and Max are going ______ together.</b>', opts: ['to play', 'play', 'playing', 'played'], ex: 'be going to + 동사원형' },
      { q: '다음 중 어법상 <b>틀린</b> 문장은?', opts: ['I want meet him.', 'I want to meet him.', 'I like to travel.', 'I like traveling.'], ex: 'want는 to부정사를 목적어로 → want to meet' },
      { q: '빈칸에 알맞은 것은?<br><b>Jim Brown, the ______ of Happy Days, made the movie.</b>', opts: ['director', 'direct', 'directly', 'directing'], ex: '동격: Jim Brown = the director (감독)' }
    ] }
  ] },

  /* ═══════════════════════════ DAY 4 · Lesson 7 본문 ❹❺❻ ═══════════════════════════ */
  { id: 'd4', name: 'DAY 4', range: '7과 본문 ❹❺❻', story: 'Lesson 7 · 동물 조련사 Jennifer · 영화 편집자 Emma · 폴리 아티스트 Chris', passage: [['', '❹', ''], ['Jennifer', 'I\'m Jennifer.', '나는 Jennifer예요.'], ['', 'I trained and took care of Max for a long time.', '나는 Max를 오랫동안 훈련하고 돌봤어요.'], ['', 'Max is a great actor, but he sometimes gets too excited when a lot of people are around.', 'Max는 훌륭한 배우이지만, 주변에 사람들이 많을 때 가끔 너무 흥분해요.'], ['', 'So, I use hand signals to calm him.', '그래서, 나는 그를 진정시키기 위해 수신호를 사용해요.'], ['', 'Who am I?', '나는 누구일까요?'], ['', 'I\'m an animal wrangler.', '나는 동물 조련사예요.'], ['', '❺', ''], ['Emma', 'My name is Emma, and I\'m a film editor.', '내 이름은 Emma이고, 나는 영화 편집자예요.'], ['', 'My work begins after the shooting is over.', '내 일은 촬영이 끝나고 나서 시작돼요.'], ['', 'To create a better story, I can change the order of scenes or delete some of them.', '더 좋은 이야기를 만들기 위해서, 나는 장면의 순서를 바꾸거나 장면 중 일부를 삭제할 수도 있어요.'], ['', 'Storytelling skills are important for my job, so I read a lot.', '내 직업상 스토리텔링 기술이 중요해서 나는 책을 많이 읽어요.'], ['', '❻', ''], ['Chris', 'I\'m Chris, and I\'m a Foley artist.', '나는 Chris이고, 폴리 아티스트예요.'], ['', 'I create sound effects in my studio when recording on location is not easy.', '나는 야외 촬영장에서 녹음하는 게 쉽지 않을 때 내 작업실에서 음향 효과를 만들어요.'], ['', 'Listen carefully.', '잘 들어 봐요.'], ['', 'Do you hear the sound of waves?', '파도 소리가 들리나요?'], ['', 'I made that sound with rice and a plastic container.', '나는 쌀과 플라스틱 통으로 그 소리를 만들었어요.'], ['', 'Doesn\'t it sound real?', '진짜처럼 들리지 않나요?']], steps: [
    { type: 'vocab', title: '핵심어휘·숙어', quizN: 15, items: [['train', '훈련하다', '❹'], ['take care of', '~을 돌보다 (과거 took care of)', '❹'], ['for a long time', '오랫동안', '❹'], ['actor', '배우', '❹'], ['sometimes', '가끔, 때때로', '❹'], ['get excited', '흥분하다', '❹'], ['around', '주위에', '❹'], ['hand signal', '수신호', '❹'], ['calm', '진정시키다', '❹'], ['animal wrangler', '동물 조련사', '❹'], ['film editor', '영화 편집자', '❺'], ['begin', '시작되다', '❺'], ['be over', '끝나다', '❺'], ['order', '순서', '❺'], ['scene', '장면', '❺'], ['delete', '삭제하다', '❺'], ['storytelling skill', '이야기를 풀어 가는 기술', '❺'], ['important', '중요한', '❺'], ['read a lot', '책을 많이 읽다', '❺'], ['Foley artist', '폴리 아티스트 (효과음을 만드는 사람)', '❻'], ['sound effect', '음향 효과', '❻'], ['studio', '작업실, 스튜디오', '❻'], ['record', '녹음하다', '❻'], ['on location', '야외 촬영장에서', '❻'], ['carefully', '주의 깊게', '❻'], ['wave', '파도', '❻'], ['plastic container', '플라스틱 통', '❻'], ['sound real', '진짜처럼 들리다', '❻']] },
    { type: 'pick', title: '어휘선택', guide: '문맥에 맞는 낱말을 고르세요.', items: [
      { s: 'I {trained|bought} and took care of Max for a long time.', ex: 'trained 훈련했다 → 동물 조련사의 일' },
      { s: 'Max is a great actor, but he sometimes gets too {excited|sleepy} when a lot of people are around.', ex: '그래서 진정시킨다(calm) → excited 흥분한' },
      { s: 'So, I use hand signals to {calm|wake} him.', ex: '흥분한 Max를 \'진정시키기\' 위해 → calm' },
      { s: 'My work {begins|ends} after the shooting is over.', ex: '촬영이 끝난 후 일이 \'시작된다\' → begins' },
      { s: 'To create a better story, I can change the {order|color} of scenes or delete some of them.', ex: '장면의 \'순서\'를 바꾼다 → order' },
      { s: 'To create a better story, I can change the order of scenes or {delete|add} some of them.', ex: '장면 중 일부를 \'삭제\'한다 → delete' },
      { s: 'Storytelling skills are {important|useless} for my job, so I read a lot.', ex: '그래서 책을 많이 읽는다 → important 중요한' },
      { s: 'I create sound {effects|effort} in my studio when recording on location is not easy.', ex: 'sound effects 음향 효과' },
      { s: 'I made that sound with rice and a plastic {container|computer}.', ex: 'plastic container 플라스틱 통' }
    ] },
    { type: 'tf', title: 'T/F 내용 확인', guide: '본문 내용과 일치하면 T, 다르면 F를 고르세요.', items: [['Jennifer trained Max for a long time.', true, 'Max를 오랫동안 훈련하고 돌봤다.', '❹', 'I trained and took care of Max for a long time'], ['Max always stays calm around many people.', false, '사람이 많으면 가끔 너무 흥분한다.', '❹', 'he sometimes gets too excited when a lot of people are around'], ['Jennifer uses hand signals to calm Max.', true, '수신호로 Max를 진정시킨다.', '❹', 'I use hand signals to calm him'], ['Emma\'s work begins before the shooting starts.', false, '촬영이 끝난 후(after the shooting is over) 시작된다.', '❺', 'My work begins after the shooting is over'], ['Emma can change the order of scenes.', true, '장면의 순서를 바꿀 수 있다.', '❺', 'I can change the order of scenes'], ['Emma reads a lot because storytelling skills are important.', true, '스토리텔링 기술이 중요해서 책을 많이 읽는다.', '❺', 'Storytelling skills are important for my job, so I read a lot'], ['Chris makes sound effects on the beach.', false, '작업실(studio)에서 만든다.', '❻', 'I create sound effects in my studio'], ['Chris made the sound of waves with rice and a plastic container.', true, '쌀과 플라스틱 통으로 파도 소리를 만들었다.', '❻', 'I made that sound with rice and a plastic container']] },
    { type: 'mc', title: '일치·불일치', guide: '선택지는 본문을 어려운 어휘로 바꿔 쓴 문장이에요. 풀고 나서 해설의 어휘를 꼭 확인하세요.', items: [
      { n: '❹', box: ['❹'], q: 'Jennifer에 관한 내용과 일치하지 <u>않는</u> 것은?', opts: ['Jennifer met Max for the first time today.', 'Jennifer is an animal wrangler.', 'Jennifer took care of Max.', 'Jennifer thinks Max is a great actor.', 'Jennifer uses hand signals.'], ex: '정답 근거: I trained and took care of Max for a long time. (오늘 처음 만난 게 아니라 오랫동안 돌봄)\n· for a long time 오랫동안 · animal wrangler 동물 조련사', per: [['Jennifer는 오늘 Max를 처음 만났다.', 'I trained and took care of Max for a long time', '불일치 → 오랫동안 돌봄'], ['Jennifer는 동물 조련사이다.', 'I\'m an animal wrangler', '일치'], ['Jennifer는 Max를 돌봤다.', 'took care of Max', '일치'], ['Jennifer는 Max가 훌륭한 배우라고 생각한다.', 'Max is a great actor', '일치'], ['Jennifer는 수신호를 사용한다.', 'I use hand signals to calm him', '일치']] },
      { n: '❺', box: ['❺', '❻'], q: '글의 내용과 <u>일치하는</u> 것은?', opts: ['Emma sometimes deletes some scenes to make a better story.', 'Emma\'s work begins before the shooting.', 'Emma doesn\'t like reading books.', 'Chris records all sounds on location.', 'Chris made the sound of waves with water.'], ex: '정답 근거: To create a better story, I can change the order of scenes or delete some of them.\n· delete 삭제하다 · be over 끝나다 · on location 야외 촬영장에서', per: [['Emma는 더 좋은 이야기를 위해 장면 일부를 삭제하기도 한다.', 'I can change the order of scenes or delete some of them', '일치'], ['Emma의 일은 촬영 전에 시작된다.', 'My work begins after the shooting is over', '불일치 → 촬영이 끝난 후'], ['Emma는 책 읽는 것을 좋아하지 않는다.', 'so I read a lot', '불일치 → 책을 많이 읽음'], ['Chris는 모든 소리를 야외 촬영장에서 녹음한다.', 'I create sound effects in my studio', '불일치 → 작업실에서 만듦'], ['Chris는 물로 파도 소리를 만들었다.', 'I made that sound with rice and a plastic container', '불일치 → 쌀과 플라스틱 통']] }
    ] },
    { type: 'pick', title: '어법선택', guide: '어법상 알맞은 것을 고르세요.', items: [
      { s: 'I trained and {took|take} care of Max for a long time.', ex: 'trained(과거)와 병렬 → took' },
      { s: 'Max is a great actor, but he sometimes {gets|get} too excited when a lot of people are around.', ex: '주어 he(3인칭 단수) → gets' },
      { s: 'Max is a great actor, but he sometimes gets too {excited|exciting} when a lot of people are around.', ex: '사람(Max)이 흥분한 감정 → excited' },
      { s: 'So, I use hand signals {to calm|calm} him.', ex: '목적(~하기 위해) → to부정사' },
      { s: 'My work {begins|begin} after the shooting is over.', ex: '주어 My work(단수) → begins' },
      { s: 'To create a better story, I can {change|changes} the order of scenes or delete some of them.', ex: '조동사 can + 동사원형' },
      { s: 'Storytelling skills {are|is} important for my job, so I read a lot.', ex: '주어 Storytelling skills(복수) → are' },
      { s: 'I create sound effects in my studio when {recording|record} on location is not easy.', ex: '주어 자리 → 동명사 recording' },
      { s: 'Do you hear the sound of {waves|wave}?', ex: '파도 소리 → waves (본문)' },
      { s: 'Doesn\'t it sound {real|really}?', ex: 'sound + 형용사: ~처럼 들리다' }
    ] },
    { type: 'verb', title: '동사변형', guide: '( ) 안의 동사를 알맞은 형태로 바꿔 쓰세요.', items: [
      { s: 'I trained and ___ care of Max for a long time.', v: 'take', a: ['took'], ex: 'take - took - taken (과거)' },
      { s: 'Max is a great actor, but he sometimes ___ too excited when a lot of people are around.', v: 'get', a: ['gets'], ex: '3인칭 단수 현재' },
      { s: 'So, I use hand signals ___ him.', v: 'calm', a: ['to calm'], ex: '목적의 to부정사' },
      { s: 'My work ___ after the shooting is over.', v: 'begin', a: ['begins'], ex: '3인칭 단수 현재' },
      { s: 'To ___ a better story, I can change the order of scenes or delete some of them.', v: 'create', a: ['create'], ex: 'To + 동사원형 (목적)' },
      { s: 'I create sound effects in my studio when ___ on location is not easy.', v: 'record', a: ['recording'], ex: '주어 자리 동명사' },
      { s: 'I ___ that sound with rice and a plastic container.', v: 'make', a: ['made'], ex: 'make - made - made (과거)' }
    ] },
    { type: 'error', title: '오류찾기', guide: '어법상 틀린 곳을 고르세요.', items: [
      { s: 'I trained and [[take]] care of Max [[for]] a long time. Max [[is]] a great actor, but he sometimes [[gets]] too excited when a lot of people are around.', w: 0, fix: 'took', ex: 'trained와 병렬 → 과거 took' },
      { s: 'Max is a great actor, but he sometimes gets too [[exciting]] when a lot of people [[are]] around. So, I use hand signals [[to calm]] [[him]].', w: 0, fix: 'excited', ex: '사람이 흥분한 감정 → excited' },
      { s: 'My work [[begin]] after the shooting [[is]] over. To create a better story, I can [[change]] the order of scenes or [[delete]] some of them.', w: 0, fix: 'begins', ex: '주어 My work(단수) → begins' },
      { s: 'Storytelling skills [[is]] important [[for]] my job, [[so]] I [[read]] a lot.', w: 0, fix: 'are', ex: '주어 Storytelling skills(복수) → are' },
      { s: 'I made that sound [[with]] rice and a plastic container. [[Doesn\'t]] it [[sound]] [[really]]?', w: 3, fix: 'real', ex: 'sound + 형용사 → real' }
    ] },
    { type: 'scramble', title: '본문 스크램블', guide: '우리말에 맞게 단어를 눌러 문장을 완성하세요.', items: [
      { ko: '나는 Max를 오랫동안 훈련하고 돌봤어요.', en: 'I trained and took care of Max for a long time.' },
      { ko: '그래서, 나는 그를 진정시키기 위해 수신호를 사용해요.', en: 'So, I use hand signals to calm him.' },
      { ko: '내 일은 촬영이 끝나고 나서 시작돼요.', en: 'My work begins after the shooting is over.' },
      { ko: '내 직업상 스토리텔링 기술이 중요해서 나는 책을 많이 읽어요.', en: 'Storytelling skills are important for my job, so I read a lot.' },
      { ko: '나는 야외 촬영장에서 녹음하는 게 쉽지 않을 때 내 작업실에서 음향 효과를 만들어요.', en: 'I create sound effects in my studio when recording on location is not easy.' },
      { ko: '나는 쌀과 플라스틱 통으로 그 소리를 만들었어요.', en: 'I made that sound with rice and a plastic container.' }
    ] },
    { type: 'order', title: '문장순서', guide: '문장을 본문 순서대로 눌러서 배열하세요.', items: [
      { lines: ['I trained and took care of Max for a long time.', 'Max is a great actor, but he sometimes gets too excited when a lot of people are around.', 'So, I use hand signals to calm him.', 'I\'m an animal wrangler.'], flow: ['Max를 오랫동안 훈련하고 돌봄', 'Max는 훌륭한 배우지만 사람이 많으면 흥분', '그래서 수신호로 진정시킴', '나는 동물 조련사'] },
      { lines: ['My name is Emma, and I\'m a film editor.', 'My work begins after the shooting is over.', 'To create a better story, I can change the order of scenes or delete some of them.', 'Storytelling skills are important for my job, so I read a lot.'], flow: ['Emma, 영화 편집자', '촬영이 끝난 후 일이 시작됨', '장면 순서 바꾸기·삭제', '스토리텔링 기술이 중요해서 책을 많이 읽음'] },
      { lines: ['I\'m Chris, and I\'m a Foley artist.', 'I create sound effects in my studio when recording on location is not easy.', 'Do you hear the sound of waves?', 'I made that sound with rice and a plastic container.'], flow: ['Chris, 폴리 아티스트', '녹음이 어려울 때 작업실에서 효과음을 만듦', '파도 소리 들리나요?', '쌀과 플라스틱 통으로 만들었음'] }
    ] },
    { type: 'insert', title: '문장삽입', guide: '주어진 문장이 들어가기에 가장 알맞은 곳을 고르세요.', items: [
      { lines: ['I trained and took care of Max for a long time.', 'Max is a great actor, but he sometimes gets too excited when a lot of people are around.', 'So, I use hand signals to calm him.'], given: 2, flow: ['Max를 훈련하고 돌봄', 'Max는 사람이 많으면 흥분함', '그래서(So) 수신호로 진정시킴'], ex: 'So는 \'사람이 많으면 흥분한다\'는 원인 뒤에 와야 한다.' },
      { lines: ['My work begins after the shooting is over.', 'To create a better story, I can change the order of scenes or delete some of them.', 'Storytelling skills are important for my job, so I read a lot.'], given: 1, flow: ['촬영이 끝난 후 일이 시작됨', '장면 순서 바꾸기·삭제', '스토리텔링 기술이 중요함'], ex: '편집자가 촬영 후에 하는 구체적인 일이 이어진다.' },
      { lines: ['Do you hear the sound of waves?', 'I made that sound with rice and a plastic container.', 'Doesn\'t it sound real?'], given: 1, flow: ['파도 소리 들리나요?', '그 소리(that sound)를 쌀과 통으로 만듦', '진짜처럼 들리지 않나요?'], ex: 'that sound는 앞 문장의 the sound of waves를 가리킨다.' }
    ] },
    { type: 'odd', title: '어색한 문장', guide: '글의 흐름과 관계없는 문장을 고르세요.', items: [
      { lines: ['I trained and took care of Max for a long time.', 'Max is a great actor, but he sometimes gets too excited when a lot of people are around.', 'Max likes to eat bones after dinner.', 'So, I use hand signals to calm him.'], odd: 2, ex: 'Max가 좋아하는 음식 → 흥분한 Max를 진정시키는 이야기와 관계없음' },
      { lines: ['My work begins after the shooting is over.', 'To create a better story, I can change the order of scenes or delete some of them.', 'Emma never watches the scenes again.', 'Storytelling skills are important for my job, so I read a lot.'], odd: 2, ex: '장면을 다시 보지 않는다 → 장면 순서를 바꾸는 편집자의 일과 맞지 않음' },
      { lines: ['Do you hear the sound of waves?', 'I made that sound with rice and a plastic container.', 'I don\'t like the sound of waves at all.', 'Doesn\'t it sound real?'], odd: 2, ex: '파도 소리가 싫다 → 소리를 만든 이야기와 관계없음' }
    ] },
    { type: 'blank', title: '빈칸추론', guide: '빈칸에 들어갈 말로 가장 알맞은 것을 고르세요.', items: [
      { s: 'Max is a great actor, but he sometimes gets too excited ____.', opts: ['when a lot of people are around', 'when he is alone', 'when he sleeps', 'when he eats'], ex: '사람이 많을 때 흥분함' },
      { s: 'My work begins ____.', opts: ['after the shooting is over', 'before the shooting starts', 'in the morning', 'on the beach'], ex: '편집자의 일은 촬영이 끝난 후 시작' },
      { s: 'I made that sound with ____.', opts: ['rice and a plastic container', 'water and a cup', 'sand and a box', 'drums and a bell'], ex: '쌀과 플라스틱 통' }
    ] },
    { type: 'mc', title: '핵심문법', guide: '알맞은 답을 고르세요.', items: [
      { q: '밑줄 친 <b>when</b>의 뜻으로 알맞은 것은?<br><b>He gets excited <u>when</u> a lot of people are around.</b>', opts: ['~할 때', '언제', '어디서', '왜'], ex: '접속사 when: ~할 때' },
      { q: '빈칸에 알맞은 것은?<br><b>I use hand signals ______ him.</b>', opts: ['to calm', 'calm', 'calms', 'calmed'], ex: '목적(~하기 위해) → to부정사' },
      { q: '밑줄 친 부분과 쓰임이 <b>같은</b> 것은?<br><b>To create a better story, I can change the order.</b>', opts: ['She went to the store <u>to buy</u> milk.', 'I want <u>to buy</u> milk.', 'My plan is <u>to buy</u> milk.', 'I like <u>to buy</u> milk.'], ex: '목적(~하기 위해)의 부사적 용법' },
      { q: '빈칸에 알맞은 것은?<br><b>______ on location is not easy.</b>', opts: ['Recording', 'Record', 'Records', 'Recorded'], ex: '주어 자리 동명사 → 단수 취급(is)' },
      { q: '우리말과 같도록 할 때 빈칸에 알맞은 것은?<br>그것은 진짜처럼 들린다.<br><b>It sounds ______.</b>', opts: ['real', 'really', 'reality', 'like real'], ex: 'sound + 형용사' },
      { q: '빈칸에 알맞은 것은?<br><b>I trained and ______ care of Max.</b>', opts: ['took', 'take', 'takes', 'taking'], ex: 'trained(과거)와 병렬' },
      { q: '빈칸에 알맞은 것은?<br><b>He got too ______ at the party.</b>', opts: ['excited', 'exciting', 'excite', 'excites'], ex: '사람의 감정 → 과거분사 excited' }
    ] }
  ] }
  ]
};
