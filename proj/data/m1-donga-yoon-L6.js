/* 중1 동아(윤정미) Lesson 6 · Good for the Earth, Good for Us (본문: Join the Zero-Waste Challenge)
   작성 규칙은 README.md 의 "데이터 작성 규칙". insert: given = 빠지는 문장 번호(0부터), odd = 어색한 문장 번호 */
window.PKG = {
  id: 'm1-donga-yoon-L6',
  school: '중1 동아(윤정미)',
  unit: 'Lesson 6~8',
  startAt: 2, /* DAY 1·2는 이미 함 → DAY 3부터 (선생님 지정 10/27) */
  title: 'Zero-Waste Challenge · Let’s Make a Movie! · Be Smart Online',
  titleKo: '제로 웨이스트 챌린지에 동참하세요',
  exam: '2학기 기말고사',
  prose: true,
  stepsBefore: ["핵심어휘·숙어", "어휘선택", "T/F 내용 확인", "어법선택", "동사변형", "오류찾기", "본문 스크램블", "문장순서", "문장삽입", "어색한 문장", "빈칸추론", "핵심문법"],   /* 일치·불일치 추가 전 단계 이름: 예전 기록을 새 단계에 맞추는 데 씀 */
  teacherPhone: '',            /* 결과 받을 번호. 예: '010-1234-5678' */

  days: [
  /* ═══════════════════════════ DAY 1 · 본문 ❶❷❸ ═══════════════════════════ */
  {
    id: 'd1', name: 'DAY 1', range: '6과 본문 ❶❷❸', story: '병들어 가는 지구 · Olivia의 챌린지 · Domingo의 챌린지',
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
    id: 'd2', name: 'DAY 2', range: '6과 본문 ❹❺', story: 'Emma의 챌린지 · 민수의 챌린지',
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
  ] },
  { id: 'd5', name: 'DAY 5', range: '8과 본문 ❶❷❸', story: 'Lesson 8 · \'좋아요\'를 원한 Goldilocks · 곰 가족의 오두막', passage: [['', '❶', ''], ['', 'There was a little girl with golden hair in a small town.', '작은 마을에 금발의 어린 소녀가 있었다.'], ['', 'Her name was Goldilocks.', '그녀의 이름은 Goldilocks였다.'], ['', 'She liked to share photos on social media.', '그녀는 소셜 미디어에 사진을 공유하는 것을 좋아했다.'], ['', 'At first, she posted everyday things, but people didn\'t give her many likes.', '처음에, 그녀는 일상적인 것들을 올렸지만, 사람들은 그녀에게 ‘좋아요’를 많이 주지 않았다.'], ['', '❷', ''], ['', '"What should I do to get more likes?" she thought.', '“어떻게 하면 더 많은 ‘좋아요’를 받을 수 있지?” 그녀는 생각했다.'], ['', '"I know! I should post funny pictures."', '“알았다! 웃긴 사진들을 올려야겠어.”'], ['', 'Now, her posts were getting a lot of likes, and Goldilocks was happy.', '이제, 그녀의 게시물은 많은 ‘좋아요’를 받고 있었고, Goldilocks는 행복했다.'], ['', 'Her followers, however, soon got bored.', '하지만, 그녀의 팔로워들은 곧 지루해졌다.'], ['', 'So, she decided to post more shocking pictures.', '그래서, 그녀는 더 충격적인 사진들을 올리기로 결심했다.'], ['', 'One day, she was taking a walk in the forest and found a cottage.', '어느 날, 그녀는 숲에서 산책을 하다가 한 오두막집을 발견했다.'], ['', 'She knocked on the door, but there was no answer.', '그녀는 문을 두드렸지만, 아무 대답이 없었다.'], ['', 'It was getting dark, and it started to rain.', '날이 어두워지고 있었고, 비가 내리기 시작했다.'], ['', 'She opened the door and walked inside.', '그녀는 문을 열고 안으로 걸어 들어갔다.'], ['', '❸', ''], ['', 'There were three bowls of soup on a table.', '식탁 위에는 수프 세 그릇이 있었다.'], ['', 'She ate the smallest one and took selfies with a smile.', '그녀는 가장 작은 그릇의 수프를 먹었고 미소를 지으며 셀피를 찍었다.'], ['', 'There were also three chairs.', '의자도 세 개 있었다.'], ['', 'She jumped on the smallest one again and again.', '그녀는 가장 작은 의자 위에서 몇 번이고 뛰었다.'], ['', 'It broke, but she didn\'t care.', '의자가 부서졌지만, 그녀는 신경 쓰지 않았다.'], ['', '"It\'s so fun!" shouted Goldilocks.', '“너무 재미있어!”라고 Goldilocks가 외쳤다.'], ['', 'She took selfies again and posted all the selfies on social media.', '그녀는 다시 셀피를 찍었고 모든 셀피를 소셜 미디어에 올렸다.'], ['', 'Then, she went upstairs and found three beds.', '그런 다음, 그녀는 위층으로 올라가 침대 세 개를 발견했다.'], ['', 'She felt tired and fell asleep in the smallest bed.', '그녀는 피곤해서 가장 작은 침대에서 잠들었다.']], steps: [
    { type: 'vocab', title: '핵심어휘·숙어', quizN: 15, items: [['little', '어린, 작은', '❶'], ['golden', '황금빛의', '❶'], ['town', '마을', '❶'], ['share', '공유하다', '❶'], ['social media', '소셜 미디어', '❶'], ['at first', '처음에는', '❶'], ['post', '게시하다, 올리다 / 게시물', '❶'], ['everyday', '일상의, 매일의', '❶'], ['like', '(소셜 미디어의) 좋아요', '❶'], ['funny', '웃긴, 재미있는', '❷'], ['follower', '팔로워, 따르는 사람', '❷'], ['however', '그러나, 하지만', '❷'], ['get bored', '지루해지다', '❷'], ['decide to', '~하기로 결심하다', '❷'], ['shocking', '충격적인', '❷'], ['take a walk', '산책하다', '❷'], ['forest', '숲', '❷'], ['cottage', '오두막집', '❷'], ['knock on', '~을 두드리다', '❷'], ['answer', '대답, 응답', '❷'], ['get dark', '어두워지다', '❷'], ['inside', '안으로, 안에', '❷'], ['bowl', '그릇', '❸'], ['selfie', '셀피, 셀카', '❸'], ['with a smile', '미소를 지으며', '❸'], ['again and again', '몇 번이고, 반복해서', '❸'], ['break', '부서지다, 깨다 (과거 broke)', '❸'], ['care', '신경 쓰다, 상관하다', '❸'], ['upstairs', '위층으로, 위층에', '❸'], ['tired', '피곤한', '❸'], ['fall asleep', '잠들다 (과거 fell asleep)', '❸']] },
    { type: 'pick', title: '어휘선택', guide: '문맥에 맞는 낱말을 고르세요.', items: [
      { s: 'She liked to {share|hide} photos on social media.', ex: '정답 ▶ share (공유하다)\n오답 ▶ hide (숨기다): 뒤에서 사진을 \'올렸다(posted)\'고 하니 사진을 \'공유하는\' 걸 좋아했어요.' },
      { s: 'At first, she posted {everyday|special} things, but people didn\'t give her many likes.', ex: '정답 ▶ everyday (일상적인)\n오답 ▶ special (특별한): \'좋아요\'를 많이 못 받아서 나중에 웃긴 사진, 충격적인 사진으로 바꿨어요. 처음엔 평범한 \'일상\' 사진이었죠.' },
      { s: 'Her followers, however, soon got {bored|excited}.', ex: '정답 ▶ bored (지루해하는)\n오답 ▶ excited (신이 난): however(하지만)가 있으니 앞의 \'행복했다\'와 반대 내용이에요. 그리고 다음에 \'더 충격적인 사진\'을 올리기로 해요.' },
      { s: 'So, she decided to post more {shocking|boring} pictures.', ex: '정답 ▶ shocking (충격적인)\n오답 ▶ boring (지루한): 팔로워들이 지루해졌으니 \'더 충격적인\' 사진으로 관심을 끌려고 했어요.' },
      { s: 'One day, she was taking a walk in the forest and found a {cottage|school}.', ex: '정답 ▶ cottage (오두막집)\n오답 ▶ school (학교): 숲속에서 발견해 문을 두드리고 들어간 곳은 곰 가족의 \'오두막집\'이에요.' },
      { s: 'She {knocked|kicked} on the door, but there was no answer.', ex: '정답 ▶ knocked (knock on = ~을 두드리다)\n오답 ▶ kicked (발로 찼다): 대답을 기다렸으니 문을 \'두드린\' 거예요.' },
      { s: 'It was getting {dark|bright}, and it started to rain.', ex: '정답 ▶ dark (어두운)\n오답 ▶ bright (밝은): 비가 오고 날이 \'어두워져서\' 집 안으로 들어갔어요.\n포인트 ▶ get dark = 어두워지다' },
      { s: 'Then, she went {upstairs|outside} and found three beds.', ex: '정답 ▶ upstairs (위층으로)\n오답 ▶ outside (밖으로): 침대를 발견하고 잠들었으니 집 \'위층\'이에요. 뒤에서 곰들도 위층으로 올라가 Goldilocks를 찾아요.' },
      { s: 'She felt {tired|hungry} and fell asleep in the smallest bed.', ex: '정답 ▶ tired (피곤한)\n오답 ▶ hungry (배고픈): \'잠들었다(fell asleep)\'와 어울리는 건 \'피곤한\'이에요. 수프는 이미 먹었어요.' }
    ] },
    { type: 'tf', title: 'T/F 내용 확인', guide: '본문 내용과 일치하면 T, 다르면 F를 고르세요.', items: [['Goldilocks liked to share photos on social media.', true, '정답 ▶ T\n이유: She liked to share photos on social media. 그대로예요.', '❶', 'She liked to share photos on social media'], ['At first, people gave Goldilocks many likes.', false, '정답 ▶ F\n이유: 처음에는 \'좋아요\'를 많이 주지 않았어요(didn\'t give her many likes).', '❶', 'people didn\'t give her many likes'], ['Goldilocks posted funny pictures to get more likes.', true, '정답 ▶ T\n이유: \'좋아요\'를 더 받으려고 웃긴 사진을 올리기로 했어요.', '❷', 'I should post funny pictures'], ['Her followers never got bored of her pictures.', false, '정답 ▶ F\n이유: 팔로워들은 곧 지루해졌어요(soon got bored).', '❷', 'Her followers, however, soon got bored'], ['Goldilocks found the cottage while she was taking a walk.', true, '정답 ▶ T\n이유: 숲에서 산책하다가(was taking a walk) 오두막집을 발견했어요.', '❷', 'she was taking a walk in the forest and found a cottage'], ['Someone opened the door for Goldilocks.', false, '정답 ▶ F\n이유: 아무 대답이 없어서(no answer) Goldilocks가 직접 문을 열고 들어갔어요.', '❷', 'She opened the door and walked inside'], ['Goldilocks ate the biggest bowl of soup.', false, '정답 ▶ F\n이유: 가장 큰 게 아니라 가장 작은 것(the smallest one)을 먹었어요.', '❸', 'She ate the smallest one'], ['Goldilocks fell asleep in the smallest bed.', true, '정답 ▶ T\n이유: 피곤해서 가장 작은 침대에서 잠들었어요.', '❸', 'fell asleep in the smallest bed']] },
    { type: 'mc', title: '일치·불일치', guide: '선택지는 본문을 어려운 어휘로 바꿔 쓴 문장이에요. 풀고 나서 해설의 어휘를 꼭 확인하세요.', items: [
      { n: '❷', box: ['❶', '❷'], q: 'Goldilocks에 관한 내용과 일치하지 <u>않는</u> 것은?', opts: ['She stopped posting pictures because her followers got bored.', 'She had golden hair.', 'Her first posts were about ordinary things.', 'She wanted to receive more likes.', 'She went into the cottage when nobody answered.'], ex: '정답 ▶ She stopped posting pictures because her followers got bored.\n이유: 팔로워들이 지루해하자 올리기를 멈춘 게 아니라 \'더 충격적인 사진을 올리기로\' 했어요.\n어휘 ▶ ordinary = everyday 평범한, 일상의 · receive = get 받다', per: [['팔로워들이 지루해해서 그녀는 사진 올리기를 그만두었다.', 'So, she decided to post more shocking pictures', '불일치 → 더 충격적인 사진을 올리기로 함'], ['그녀는 금발이었다.', 'a little girl with golden hair', '일치'], ['그녀의 처음 게시물은 평범한 것들이었다.', 'At first, she posted everyday things', '일치 (ordinary = everyday)'], ['그녀는 \'좋아요\'를 더 받고 싶었다.', 'What should I do to get more likes', '일치'], ['아무도 대답하지 않자 그녀는 오두막에 들어갔다.', 'there was no answer', '일치']] },
      { n: '❸', box: ['❸'], q: '글의 내용과 <u>일치하는</u> 것은?', opts: ['Goldilocks did not mind breaking the chair.', 'There were two bowls of soup on the table.', 'Goldilocks sat quietly on the biggest chair.', 'Goldilocks kept her selfies to herself.', 'Goldilocks found three beds downstairs.'], ex: '정답 ▶ Goldilocks did not mind breaking the chair.\n이유: 의자가 부서졌지만 신경 쓰지 않았어요(didn\'t care).\n어휘 ▶ mind = care 신경 쓰다 · keep ~ to oneself ~을 혼자만 간직하다 · downstairs 아래층에', per: [['Goldilocks는 의자를 부순 것을 신경 쓰지 않았다.', 'It broke, but she didn\'t care', '일치 (mind = care)'], ['식탁 위에 수프가 두 그릇 있었다.', 'There were three bowls of soup on a table', '불일치 → 세 그릇'], ['Goldilocks는 가장 큰 의자에 조용히 앉았다.', 'She jumped on the smallest one again and again', '불일치 → 가장 작은 의자에서 몇 번이고 뜀'], ['Goldilocks는 셀피를 혼자만 간직했다.', 'posted all the selfies on social media', '불일치 → 모두 소셜 미디어에 올림'], ['Goldilocks는 아래층에서 침대 세 개를 발견했다.', 'she went upstairs and found three beds', '불일치 → 위층']] }
    ] },
    { type: 'pick', title: '어법선택', guide: '어법상 알맞은 것을 고르세요.', items: [
      { s: 'There {was|were} a little girl with golden hair in a small town.', ex: '정답 ▶ was\n이유: There + be동사 + 주어. be동사는 뒤의 주어에 맞춰요. a little girl(단수) + 과거 → was\n오답 ▶ were는 복수 주어일 때 (There were three chairs.)' },
      { s: 'She liked {to share|share} photos on social media.', ex: '정답 ▶ to share\n이유: like 뒤에 동사가 오면 to부정사(to share)나 동명사(sharing)로 바꿔요.\n오답 ▶ share(동사원형) ✘ — 동사 두 개가 바로 붙을 수 없어요.' },
      { s: 'At first, she posted everyday things, but people didn\'t give {her|to her} many likes.', ex: '정답 ▶ her\n이유: give + 사람(~에게) + 물건(~을). give her many likes = 그녀에게 많은 \'좋아요\'를 주다\n오답 ▶ to her를 쓰려면 순서를 바꿔 give many likes to her라고 해요.' },
      { s: '"What should I do {to get|getting} more likes?" she thought.', ex: '정답 ▶ to get\n이유: \'좋아요를 더 받기 위해\' → 목적(~하기 위해)을 나타내는 to부정사\n오답 ▶ getting ✘' },
      { s: 'Now, her posts {were|was} getting a lot of likes, and Goldilocks was happy.', ex: '정답 ▶ were\n이유: 주어 her posts(게시물들)가 복수 → were + -ing (과거진행형)\n오답 ▶ was는 단수 주어일 때' },
      { s: 'Her followers, however, soon got {bored|boring}.', ex: '정답 ▶ bored\n이유: 사람이 \'지루함을 느낄 때\'는 bored, 무언가가 \'지루하게 만들 때\'는 boring. 팔로워들이 지루해졌으니 bored\n포인트 ▶ get + 형용사 = ~해지다' },
      { s: 'So, she decided {to post|posting} more shocking pictures.', ex: '정답 ▶ to post\n이유: decide는 목적어로 to부정사만 써요. decide to ~ = ~하기로 결심하다\n오답 ▶ posting ✘' },
      { s: 'It was getting dark, and it started {to rain|rained}.', ex: '정답 ▶ to rain\n이유: start + to부정사(또는 -ing) = ~하기 시작하다. 여기서 it은 날씨를 나타내는 비인칭 주어예요.\n오답 ▶ rained는 과거형 동사라 started 뒤에 올 수 없어요.' },
      { s: 'She felt {tired|tiredly} and fell asleep in the smallest bed.', ex: '정답 ▶ tired\n이유: feel(느끼다) 뒤에는 상태를 나타내는 형용사가 와요. felt tired = 피곤함을 느꼈다\n오답 ▶ tiredly는 부사라 feel 뒤에 올 수 없어요.\n포인트 ▶ feel, look, sound, get + 형용사' },
      { s: 'She ate the {smallest|small} one and took selfies with a smile.', ex: '정답 ▶ smallest\n이유: 세 그릇 중 \'가장 작은\' 것 → the + 최상급 (small - smaller - smallest)\n오답 ▶ the small one은 \'작은 것\'이라 셋 중 하나를 콕 집지 못해요.' }
    ] },
    { type: 'verb', title: '동사변형', guide: '( ) 안의 동사를 알맞은 형태로 바꿔 쓰세요.', items: [
      { s: 'At first, she ___ everyday things, but people didn\'t give her many likes.', v: 'post', a: ['posted'], ex: '정답 ▶ posted\n이유: 과거 이야기 → 과거형 -ed' },
      { s: 'One day, she was ___ a walk in the forest and found a cottage.', v: 'take', a: ['taking'], ex: '정답 ▶ taking\n이유: was + -ing = 과거진행형(~하고 있었다). take → taking (e 빼고 -ing)\n포인트 ▶ take a walk = 산책하다' },
      { s: 'One day, she was taking a walk in the forest and ___ a cottage.', v: 'find', a: ['found'], ex: '정답 ▶ found\n이유: 과거형. find - found - found (불규칙)' },
      { s: 'She ___ the smallest one and took selfies with a smile.', v: 'eat', a: ['ate'], ex: '정답 ▶ ate\n이유: took(과거)와 병렬 → 과거형. eat - ate - eaten (불규칙)' },
      { s: 'It ___, but she didn\'t care.', v: 'break', a: ['broke'], ex: '정답 ▶ broke\n이유: 과거형. break - broke - broken (불규칙)\n포인트 ▶ 여기서 It은 앞 문장의 \'가장 작은 의자\'예요.' },
      { s: 'She ___ selfies again and posted all the selfies on social media.', v: 'take', a: ['took'], ex: '정답 ▶ took\n이유: posted(과거)와 병렬 → 과거형. take - took - taken (불규칙)' },
      { s: 'She felt tired and ___ asleep in the smallest bed.', v: 'fall', a: ['fell'], ex: '정답 ▶ fell\n이유: felt(과거)와 병렬 → 과거형. fall - fell - fallen\n포인트 ▶ fall asleep = 잠들다' },
      { s: '"It\'s so fun!" ___ Goldilocks.', v: 'shout', a: ['shouted'], ex: '정답 ▶ shouted\n이유: 과거형 -ed. 인용문 뒤에서는 \'동사 + 주어(shouted Goldilocks)\' 순서로 쓸 수 있어요.' }
    ] },
    { type: 'error', title: '오류찾기', guide: '어법상 틀린 곳을 고르세요.', items: [
      { s: 'There was a little girl [[with]] golden hair in a small town. Her name [[was]] Goldilocks. She liked [[to share]] photos [[in]] social media.', w: 3, fix: 'on', ex: '틀린 곳 ▶ ④ in → on\n이유: 소셜 미디어·인터넷\'에\' 올리다는 전치사 on을 써요. on social media, on the Internet, on TV\n나머지 ▶ ① with(~을 가진) ✔ ② was ✔ ③ to share(like + to부정사) ✔' },
      { s: 'At first, she [[posted]] everyday things, [[but]] people didn\'t give [[to her]] many likes.', w: 2, fix: 'her', ex: '틀린 곳 ▶ ③ to her → her\n이유: give + 사람 + 물건 순서일 때는 to를 쓰지 않아요. (give many likes to her는 가능)\n나머지 ▶ ① posted ✔ ② but(하지만) ✔' },
      { s: 'Her followers, [[however]], soon got [[boring]]. So, she [[decided]] to post more [[shocking]] pictures.', w: 1, fix: 'bored', ex: '틀린 곳 ▶ ② boring → bored\n이유: 팔로워들이 \'지루함을 느낀\' 것 → bored\n나머지 ▶ ① however ✔ ③ decided ✔ ④ shocking(사진이 충격을 주는 것) ✔' },
      { s: 'She [[knocked]] on the door, but there [[were]] no answer. It was [[getting]] dark, and [[it]] started to rain.', w: 1, fix: 'was', ex: '틀린 곳 ▶ ② were → was\n이유: 주어 no answer(대답 하나도 없음)는 단수 → there was\n나머지 ▶ ① knocked on ✔ ③ getting dark ✔ ④ it(날씨 비인칭 주어) ✔' },
      { s: 'She ate the smallest one and [[take]] selfies [[with]] a smile. There were also three chairs. She jumped on the [[smallest]] one again and again.', w: 0, fix: 'took', ex: '틀린 곳 ▶ ① take → took\n이유: ate(과거) and took(과거). and로 이어진 동사는 시제를 맞춰요.\n나머지 ▶ ② with a smile(미소를 지으며) ✔ ③ smallest(최상급) ✔' }
    ] },
    { type: 'scramble', title: '본문 스크램블', guide: '우리말에 맞게 단어를 눌러 문장을 완성하세요.', items: [
      { ko: '그녀는 소셜 미디어에 사진을 공유하는 것을 좋아했다.', en: 'She liked to share photos on social media.' },
      { ko: '그래서, 그녀는 더 충격적인 사진들을 올리기로 결심했다.', en: 'So, she decided to post more shocking pictures.' },
      { ko: '어느 날, 그녀는 숲에서 산책을 하다가 한 오두막집을 발견했다.', en: 'One day, she was taking a walk in the forest and found a cottage.' },
      { ko: '식탁 위에는 수프 세 그릇이 있었다.', en: 'There were three bowls of soup on a table.' },
      { ko: '그녀는 가장 작은 그릇의 수프를 먹었고 미소를 지으며 셀피를 찍었다.', en: 'She ate the smallest one and took selfies with a smile.' },
      { ko: '그녀는 피곤해서 가장 작은 침대에서 잠들었다.', en: 'She felt tired and fell asleep in the smallest bed.' }
    ] },
    { type: 'order', title: '문장순서', guide: '문장을 본문 순서대로 눌러서 배열하세요.', items: [
      { lines: ['There was a little girl with golden hair in a small town.', 'Her name was Goldilocks.', 'She liked to share photos on social media.', 'At first, she posted everyday things, but people didn\'t give her many likes.'], flow: ['작은 마을의 금발 소녀', '이름은 Goldilocks', '소셜 미디어에 사진 공유를 좋아함', '처음엔 \'좋아요\'를 많이 못 받음'] },
      { lines: ['Now, her posts were getting a lot of likes, and Goldilocks was happy.', 'Her followers, however, soon got bored.', 'So, she decided to post more shocking pictures.', 'One day, she was taking a walk in the forest and found a cottage.'], flow: ['웃긴 사진으로 \'좋아요\'를 많이 받음', '하지만 팔로워들이 곧 지루해함', '더 충격적인 사진을 올리기로 함', '숲에서 오두막집 발견'] },
      { lines: ['There were three bowls of soup on a table.', 'She ate the smallest one and took selfies with a smile.', 'There were also three chairs.', 'She jumped on the smallest one again and again.', 'It broke, but she didn\'t care.'], flow: ['수프 세 그릇', '가장 작은 것을 먹고 셀피', '의자도 세 개', '가장 작은 의자에서 뜀', '의자가 부서져도 신경 안 씀'] }
    ] },
    { type: 'insert', title: '문장삽입', guide: '주어진 문장이 들어가기에 가장 알맞은 곳을 고르세요.', items: [
      { lines: ['Her followers, however, soon got bored.', 'So, she decided to post more shocking pictures.', 'One day, she was taking a walk in the forest and found a cottage.'], given: 1, flow: ['팔로워들이 곧 지루해함', '그래서(So) 더 충격적인 사진을 올리기로 함', '숲에서 오두막집 발견'], ex: '정답 ▶ ①\n이유: So(그래서)는 원인 뒤에 와요. \'팔로워들이 지루해졌다(원인) → 그래서 더 충격적인 사진을 올리기로 했다(결과)\'.' },
      { lines: ['She knocked on the door, but there was no answer.', 'It was getting dark, and it started to rain.', 'She opened the door and walked inside.'], given: 1, flow: ['문을 두드렸지만 대답이 없음', '어두워지고 비가 오기 시작함', '문을 열고 안으로 들어감'], ex: '정답 ▶ ①\n이유: 대답이 없었는데도 들어간 이유가 \'어두워지고 비가 와서\'예요. 그래서 문을 열고 들어가기 바로 앞에 와요.' },
      { lines: ['She took selfies again and posted all the selfies on social media.', 'Then, she went upstairs and found three beds.', 'She felt tired and fell asleep in the smallest bed.'], given: 1, flow: ['셀피를 다시 찍어 모두 올림', '그런 다음(Then) 위층에서 침대 세 개 발견', '피곤해서 가장 작은 침대에서 잠듦'], ex: '정답 ▶ ①\n이유: \'가장 작은 침대에서 잠들었다\' 전에 먼저 위층에서 \'침대 세 개를 발견\'해야 해요. Then(그런 다음)이 순서를 알려 줘요.' }
    ] },
    { type: 'odd', title: '어색한 문장', guide: '글의 흐름과 관계없는 문장을 고르세요.', items: [
      { lines: ['Her name was Goldilocks.', 'She liked to share photos on social media.', 'She never used her phone to take pictures.', 'At first, she posted everyday things, but people didn\'t give her many likes.'], odd: 2, ex: '정답 ▶ ③\n이유: Goldilocks는 사진을 소셜 미디어에 올리는 걸 좋아했어요. \'사진 찍는 데 휴대폰을 전혀 쓰지 않았다\'는 흐름과 맞지 않아요.' },
      { lines: ['One day, she was taking a walk in the forest and found a cottage.', 'She knocked on the door, but there was no answer.', 'The owner of the cottage welcomed her warmly.', 'It was getting dark, and it started to rain.'], odd: 2, ex: '정답 ▶ ③\n이유: 문을 두드려도 대답이 없었어요(no answer). \'주인이 따뜻하게 맞아 주었다\'는 앞뒤 내용과 반대예요.' },
      { lines: ['There were also three chairs.', 'She jumped on the smallest one again and again.', 'She sat on the chair very carefully.', 'It broke, but she didn\'t care.'], odd: 2, ex: '정답 ▶ ③\n이유: 의자 위에서 몇 번이고 뛰다가 의자가 부서졌어요. \'아주 조심스럽게 앉았다\'는 정반대예요.' }
    ] },
    { type: 'blank', title: '빈칸추론', guide: '빈칸에 들어갈 말로 가장 알맞은 것을 고르세요.', items: [
      { s: 'So, she decided to post more ____ pictures.', opts: ['shocking', 'boring', 'everyday', 'old'], ex: '정답 ▶ shocking\n이유: 팔로워들이 지루해져서(got bored) 관심을 끌려면 \'더 충격적인\' 사진이 필요했어요.' },
      { s: 'She knocked on the door, but there was no ____.', opts: ['answer', 'door', 'rain', 'light'], ex: '정답 ▶ answer\n이유: 문을 두드렸는데 \'대답\'이 없어서 직접 문을 열고 들어갔어요.' },
      { s: 'She felt tired and fell asleep in the ____ bed.', opts: ['smallest', 'biggest', 'oldest', 'softest'], ex: '정답 ▶ smallest\n이유: 수프도 의자도 \'가장 작은 것\'을 골랐듯이 침대도 \'가장 작은 침대\'에서 잠들었어요. (아기곰의 것)' }
    ] },
    { type: 'mc', title: '핵심문법', guide: '알맞은 답을 고르세요.', items: [
      { q: '두 문장의 뜻이 같도록 할 때 빈칸에 알맞은 것은?<br><b>People didn\'t give her many likes.<br>= People didn\'t give many likes ______ her.</b>', opts: ['to', 'for', 'of', 'with'], ex: '정답 ▶ to\n이유: give + 사람 + 물건 → give + 물건 + to + 사람. (give, send, show, tell은 to)\n오답 ▶ for는 make, buy, cook에 써요.' },
      { q: '밑줄 친 <b>it</b>과 쓰임이 <b>같은</b> 것은?<br><b>It was getting dark, and <u>it</u> started to rain.</b>', opts: ['<u>It</u> is Sunday today.', '<u>It</u> is my new phone.', 'I like <u>it</u> very much.', '<u>It</u> broke, but she didn\'t care.'], ex: '정답 ▶ It is Sunday today.\n이유: 날씨·시간·요일·명암을 말할 때 쓰는 비인칭 주어 it이에요. \'그것\'으로 해석하지 않아요.\n오답 ▶ 나머지 it은 모두 \'그것\'(휴대폰, 좋아하는 것, 의자)을 가리키는 대명사예요.' },
      { q: '빈칸에 알맞은 것은?<br><b>There were three bowls of soup. She ate the smallest ______.</b>', opts: ['one', 'it', 'them', 'ones'], ex: '정답 ▶ one\n이유: 같은 종류 중 \'하나\'를 말할 때는 one (= bowl of soup). it은 이미 정해진 \'바로 그것\'을 가리켜요.\n오답 ▶ them, ones는 복수예요.' },
      { q: '밑줄 친 <b>with</b>의 뜻으로 알맞은 것은?<br><b>There was a little girl <u>with</u> golden hair.</b>', opts: ['~을 가진', '~와 함께', '~으로 (도구)', '~에 대해'], ex: '정답 ▶ ~을 가진\n이유: with + 외모·특징 = ~을 가진. a little girl with golden hair = 금발을 가진 어린 소녀\n비교 ▶ with a smile(미소를 지으며), with my friend(친구와 함께)' },
      { q: '우리말과 같도록 할 때 빈칸에 알맞은 것은?<br>날이 어두워지고 있었다.<br><b>It was ______ dark.</b>', opts: ['getting', 'gets', 'got', 'to get'], ex: '정답 ▶ getting\n이유: was + -ing = 과거진행형(~하고 있었다). get + 형용사 = ~해지다 → was getting dark' },
      { q: '다음 문장과 뜻이 같은 것은?<br><b>"It\'s so fun!" shouted Goldilocks.</b>', opts: ['Goldilocks shouted, "It\'s so fun!"', 'Goldilocks said it was not fun.', 'Someone shouted at Goldilocks.', 'Goldilocks wanted to have fun.'], ex: '정답 ▶ Goldilocks shouted, "It\'s so fun!"\n이유: 인용문 뒤에서는 \'shouted Goldilocks(동사 + 주어)\'로 순서를 바꿔 쓸 수 있어요. 뜻은 같아요: \'Goldilocks가 외쳤다\'.' },
      { q: '밑줄 친 <b>should</b>의 뜻으로 알맞은 것은?<br><b>"I know! I <u>should</u> post funny pictures."</b>', opts: ['~해야 한다', '~해도 된다', '~할 수 있었다', '~일지도 모른다'], ex: '정답 ▶ ~해야 한다\n이유: should는 \'~해야 한다, ~하는 게 좋겠다\'(충고·의무). 웃긴 사진을 \'올려야겠다\'는 뜻이에요.' }
    ] },
    { type: 'mc', title: '요약문 완성', guide: '본문을 읽고 요약문의 빈칸 (A), (B)에 들어갈 말을 고르세요.', items: [
      { n: '❷', box: ['❶', '❷'], q: '다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 알맞은 것은?<br><b>Goldilocks wanted to get more (A) ______ on social media, so she decided to post more (B) ______ pictures.</b>', opts: ['(A) likes – (B) shocking', '(A) likes – (B) everyday', '(A) money – (B) shocking', '(A) money – (B) everyday', '(A) friends – (B) boring'], ex: '정답 ▶ (A) likes – (B) shocking\n(A) Goldilocks가 원한 것 → 더 많은 \'좋아요(likes)\'\n(B) 팔로워들이 지루해하자 올리기로 한 사진 → 더 \'충격적인(shocking)\' 사진\n오답 ▶ money(돈)·friends(친구)는 원한 것이 아니고, everyday(일상적인)·boring(지루한)은 처음 사진이나 반대 뜻이에요.', ev: ['What should I do to get more likes', 'So, she decided to post more shocking pictures'] },
      { n: '❸', box: ['❸'], q: '다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 알맞은 것은?<br><b>Inside the cottage, Goldilocks ate the soup, (A) ______ a chair, and posted selfies (B) ______ caring about the owners.</b>', opts: ['(A) broke – (B) without', '(A) fixed – (B) without', '(A) broke – (B) after', '(A) fixed – (B) after', '(A) cleaned – (B) before'], ex: '정답 ▶ (A) broke – (B) without\n(A) 의자 위에서 뛰다가 의자가 \'부서졌어요(It broke)\' → broke\n(B) 의자가 부서져도 신경 쓰지 않았고(didn\'t care) 셀피를 모두 올렸어요 → 주인을 \'신경 쓰지 않고(without caring)\'\n오답 ▶ fixed(고쳤다)·cleaned(청소했다)는 본문에 없고, after·before는 \'신경 쓴 뒤/전에\'라는 뜻이라 맞지 않아요.', ev: ['It broke, but she didn\'t care', 'She took selfies again and posted all the selfies on social media'] }
    ] }
  ] },
  { id: 'd6', name: 'DAY 6', range: '8과 본문 ❹❺', story: 'Lesson 8 · 들켜 버린 Goldilocks · 지워지지 않는 게시물', passage: [['', '❹', ''], ['', 'About an hour later, three bears came home.', '약 한 시간 후에, 곰 세 마리가 집으로 돌아왔다.'], ['', '"Someone ate my soup and broke my chair!" cried Baby Bear.', '“누군가 내 수프를 먹고 내 의자를 부서뜨렸어요!”라고 아기곰이 외쳤다.'], ['', 'They went upstairs and saw Goldilocks.', '그들은 위층으로 가서 Goldilocks를 봤다.'], ['', 'Mother Bear found a phone next to Goldilocks.', '엄마곰이 Goldilocks 옆에서 휴대폰을 발견했다.'], ['', '"This is terrible! Look at all these posts of our home," shouted Mother Bear angrily.', '“끔찍해! 우리 집에 관한 이 모든 게시물을 봐요.”라고 엄마곰이 화가 나서 외쳤다.'], ['', 'Goldilocks jumped up in surprise.', 'Goldilocks는 놀라서 벌떡 일어났다.'], ['', '"You broke into our house and posted these pictures without our permission.', '“너는 우리 집에 침입해서 우리의 허락 없이 이 사진들을 올렸어.'], ['', 'Don\'t you know these things are wrong?" said Father Bear.', '너는 이런 것들이 잘못이라는 것을 모르니?”라고 아빠곰이 말했다.'], ['', '"Please forgive me.', '“용서해 주세요.'], ['', 'I\'m so sorry, and I\'ll clean your house every day until the end of the summer," said Goldilocks.', '정말 죄송해요, 여름이 끝날 때까지 매일 여러분 집을 청소할게요.”라고 Goldilocks가 말했다.'], ['', '❺', ''], ['', 'All summer long, Goldilocks worked hard.', '여름 내내, Goldilocks는 열심히 일했다.'], ['', 'On the last day, Goldilocks said to Father Bear, "I deleted all my posts of your cottage, so please don\'t worry."', '마지막 날에 Goldilocks는 “오두막집에 관한 제 게시물을 모두 삭제했으니 걱정하지 마세요.”라고 아빠곰에게 말했다.'], ['', '"You still don\'t understand.', '“너는 아직도 이해하지 못하는구나.'], ['', 'Other people already shared them on social media.', '다른 사람들이 이미 소셜 미디어에 그것들을 공유했어.'], ['', 'Your posts will live on forever," said Father Bear.', '너의 게시물은 영원히 남아 있을 거야.”라고 아빠곰이 말했다.'], ['', '"Oh, I didn\'t think about that," said Goldilocks.', '“아, 그건 생각하지 못했어요.”라고 Goldilocks가 말했다.'], ['', '"From now on, I\'ll think twice before I press POST."', '“이제부터는 ‘게시’를 누르기 전에 두 번 생각할게요.”']], steps: [
    { type: 'vocab', title: '핵심어휘·숙어', quizN: 15, items: [['about', '약, 대략', '❹'], ['later', '~ 후에', '❹'], ['come home', '집에 오다', '❹'], ['someone', '누군가', '❹'], ['cry', '외치다, 울다', '❹'], ['next to', '~ 옆에', '❹'], ['terrible', '끔찍한', '❹'], ['angrily', '화가 나서', '❹'], ['jump up', '벌떡 일어나다', '❹'], ['in surprise', '놀라서', '❹'], ['break into', '~에 침입하다', '❹'], ['without', '~ 없이', '❹'], ['permission', '허락', '❹'], ['wrong', '잘못된', '❹'], ['forgive', '용서하다', '❹'], ['until', '~까지 (계속)', '❹'], ['the end of', '~의 끝', '❹'], ['all summer long', '여름 내내', '❺'], ['work hard', '열심히 일하다', '❺'], ['last', '마지막의', '❺'], ['delete', '삭제하다', '❺'], ['worry', '걱정하다', '❺'], ['still', '아직도, 여전히', '❺'], ['understand', '이해하다', '❺'], ['already', '이미, 벌써', '❺'], ['live on', '계속 살아 있다, 남아 있다', '❺'], ['forever', '영원히', '❺'], ['from now on', '이제부터', '❺'], ['think twice', '두 번 생각하다, 신중히 생각하다', '❺'], ['press', '누르다', '❺']] },
    { type: 'pick', title: '어휘선택', guide: '문맥에 맞는 낱말을 고르세요.', items: [
      { s: 'About an hour {later|ago}, three bears came home.', ex: '정답 ▶ later (~ 후에)\n오답 ▶ ago (~ 전에): Goldilocks가 잠든 뒤 \'약 한 시간 후에\' 곰들이 돌아왔어요. ago는 \'지금으로부터 ~ 전\'이라 이야기 흐름과 맞지 않아요.' },
      { s: 'Mother Bear found a phone {next to|far from} Goldilocks.', ex: '정답 ▶ next to (~ 옆에)\n오답 ▶ far from (~에서 멀리): 잠든 Goldilocks \'옆에서\' 휴대폰을 발견해 게시물을 봤어요.' },
      { s: '"This is {terrible|wonderful}! Look at all these posts of our home," shouted Mother Bear angrily.', ex: '정답 ▶ terrible (끔찍한)\n오답 ▶ wonderful (멋진): 엄마곰이 \'화가 나서(angrily)\' 외쳤으니 \'끔찍해!\'가 맞아요.' },
      { s: 'Goldilocks jumped up in {surprise|silence}.', ex: '정답 ▶ surprise (in surprise = 놀라서)\n오답 ▶ silence (침묵): 자다가 곰들의 외침에 \'놀라서\' 벌떡 일어났어요.' },
      { s: '"You broke into our house and posted these pictures {without|with} our permission.', ex: '정답 ▶ without (~ 없이)\n오답 ▶ with (~와 함께): 아빠곰이 \'잘못이라는 걸 모르니?\'라고 혼내니까 \'허락 없이\' 올린 거예요.' },
      { s: '"Please {forgive|forget} me.', ex: '정답 ▶ forgive (용서하다)\n오답 ▶ forget (잊다): 바로 뒤에 I\'m so sorry(정말 죄송해요)라고 사과하니 \'용서해 주세요\'가 맞아요.' },
      { s: 'On the last day, Goldilocks said to Father Bear, "I {deleted|shared} all my posts of your cottage, so please don\'t worry."', ex: '정답 ▶ deleted (삭제했다)\n오답 ▶ shared (공유했다): \'걱정하지 마세요\'라고 했으니 게시물을 \'지웠다\'가 맞아요.' },
      { s: 'Other people {already|never} shared them on social media.', ex: '정답 ▶ already (이미)\n오답 ▶ never (결코 ~않다): 그래서 게시물이 영원히 남는다(live on forever)고 했어요. 다른 사람들이 \'이미\' 공유한 거예요.' },
      { s: '"From now on, I\'ll think {twice|once} before I press POST."', ex: '정답 ▶ twice (두 번)\n오답 ▶ once (한 번): think twice = 다시 한번 신중하게 생각하다. 교훈을 얻었으니 \'두 번 생각하겠다\'예요.' }
    ] },
    { type: 'tf', title: 'T/F 내용 확인', guide: '본문 내용과 일치하면 T, 다르면 F를 고르세요.', items: [['The three bears came home about an hour later.', true, '정답 ▶ T\n이유: About an hour later, three bears came home. 그대로예요.', '❹', 'About an hour later, three bears came home'], ['Baby Bear said someone ate his soup and broke his chair.', true, '정답 ▶ T\n이유: 아기곰이 \'누군가 내 수프를 먹고 내 의자를 부쉈어요!\'라고 외쳤어요.', '❹', 'Someone ate my soup and broke my chair'], ['Father Bear found a phone next to Goldilocks.', false, '정답 ▶ F\n이유: 휴대폰을 발견한 건 아빠곰이 아니라 엄마곰(Mother Bear)이에요.', '❹', 'Mother Bear found a phone next to Goldilocks'], ['Mother Bear was happy to see the posts of their home.', false, '정답 ▶ F\n이유: \'끔찍해!\'라며 화가 나서(angrily) 외쳤어요.', '❹', 'This is terrible'], ['Goldilocks posted the pictures with the bears\' permission.', false, '정답 ▶ F\n이유: 곰들의 허락 없이(without our permission) 올렸어요.', '❹', 'posted these pictures without our permission'], ['Goldilocks promised to clean the bears\' house until the end of the summer.', true, '정답 ▶ T\n이유: 여름이 끝날 때까지 매일 집을 청소하겠다고 했어요.', '❹', 'I\'ll clean your house every day until the end of the summer'], ['Father Bear said the posts would disappear forever.', false, '정답 ▶ F\n이유: 사라지는 게 아니라 영원히 \'남아 있을(live on forever)\' 거라고 했어요.', '❺', 'Your posts will live on forever'], ['Goldilocks decided to think carefully before posting.', true, '정답 ▶ T\n이유: \'게시를 누르기 전에 두 번 생각하겠다(think twice)\'고 했어요.', '❺', 'I\'ll think twice before I press POST']] },
    { type: 'mc', title: '일치·불일치', guide: '선택지는 본문을 어려운 어휘로 바꿔 쓴 문장이에요. 풀고 나서 해설의 어휘를 꼭 확인하세요.', items: [
      { n: '❹', box: ['❹'], q: '곰 가족에 관한 내용과 일치하지 <u>않는</u> 것은?', opts: ['Father Bear thanked Goldilocks for the pictures.', 'Baby Bear noticed that his chair was broken.', 'The bears found Goldilocks upstairs.', 'Mother Bear got angry when she saw the posts.', 'Father Bear said Goldilocks posted the pictures without permission.'], ex: '정답 ▶ Father Bear thanked Goldilocks for the pictures.\n이유: 아빠곰은 고마워한 게 아니라 \'허락 없이 올린 건 잘못\'이라고 혼냈어요.\n어휘 ▶ notice 알아차리다 · get angry 화가 나다', per: [['아빠곰은 사진에 대해 Goldilocks에게 고마워했다.', 'Don\'t you know these things are wrong', '불일치 → 잘못이라고 혼냄'], ['아기곰은 자기 의자가 부서진 것을 알아차렸다.', 'Someone ate my soup and broke my chair', '일치'], ['곰들은 위층에서 Goldilocks를 발견했다.', 'They went upstairs and saw Goldilocks', '일치'], ['엄마곰은 게시물을 보고 화가 났다.', 'shouted Mother Bear angrily', '일치'], ['아빠곰은 Goldilocks가 허락 없이 사진을 올렸다고 말했다.', 'posted these pictures without our permission', '일치']] },
      { n: '❺', box: ['❺'], q: '글의 내용과 <u>일치하는</u> 것은?', opts: ['Goldilocks worked hard for the bears all summer.', 'Goldilocks posted more pictures of the cottage on the last day.', 'Father Bear said deleting the posts solved the problem.', 'Nobody else shared Goldilocks\'s posts.', 'Goldilocks already knew her posts could live on forever.'], ex: '정답 ▶ Goldilocks worked hard for the bears all summer.\n이유: All summer long, Goldilocks worked hard. (여름 내내 열심히 일했다)\n어휘 ▶ solve 해결하다 · nobody else 다른 아무도 ~않다', per: [['Goldilocks는 여름 내내 곰들을 위해 열심히 일했다.', 'All summer long, Goldilocks worked hard', '일치'], ['Goldilocks는 마지막 날 오두막 사진을 더 올렸다.', 'I deleted all my posts of your cottage', '불일치 → 모두 삭제했음'], ['아빠곰은 게시물을 지운 것으로 문제가 해결됐다고 했다.', 'You still don\'t understand', '불일치 → 아직도 이해 못 한다고 함'], ['다른 누구도 Goldilocks의 게시물을 공유하지 않았다.', 'Other people already shared them on social media', '불일치 → 이미 공유함'], ['Goldilocks는 게시물이 영원히 남을 수 있다는 걸 이미 알았다.', 'Oh, I didn\'t think about that', '불일치 → 생각하지 못했음']] }
    ] },
    { type: 'pick', title: '어법선택', guide: '어법상 알맞은 것을 고르세요.', items: [
      { s: 'About an hour later, three bears came {home|to home}.', ex: '정답 ▶ home\n이유: come home(집에 오다)의 home은 \'집으로\'라는 부사라서 앞에 to를 쓰지 않아요.\n비교 ▶ go home, get home (O) / go to home (X) / go to school (O)' },
      { s: '"Someone {ate|eat} my soup and broke my chair!" cried Baby Bear.', ex: '정답 ▶ ate\n이유: broke(과거)와 병렬 → 과거형. eat - ate - eaten\n오답 ▶ eat은 현재형(그리고 Someone은 단수라 현재라면 eats)' },
      { s: 'They went upstairs and {saw|see} Goldilocks.', ex: '정답 ▶ saw\n이유: went(과거) and saw(과거). and로 이어진 동사는 시제를 맞춰요.\n오답 ▶ see는 현재형' },
      { s: '"This is terrible! Look at all these posts of our home," shouted Mother Bear {angrily|angry}.', ex: '정답 ▶ angrily\n이유: 동사 shouted(외쳤다)를 꾸며 \'화가 나서 외쳤다\' → 부사 angrily\n오답 ▶ angry는 형용사라 동사를 꾸밀 수 없어요. (She was angry. 처럼 be동사 뒤에)' },
      { s: 'Goldilocks jumped up {in|on} surprise.', ex: '정답 ▶ in\n이유: in + 감정 명사 = ~해서, ~한 상태로. in surprise = 놀라서\n비교 ▶ in anger(화가 나서), in joy(기뻐서)' },
      { s: 'Don\'t you know these things {are|is} wrong?" said Father Bear.', ex: '정답 ▶ are\n이유: 주어 these things(이것들)가 복수 → are\n오답 ▶ is는 단수 주어일 때 (This thing is wrong.)' },
      { s: 'I\'m so sorry, and I\'ll clean your house every day {until|by} the end of the summer," said Goldilocks.', ex: '정답 ▶ until\n이유: until = ~까지 \'계속\'. 여름이 끝날 때까지 매일 \'계속\' 청소하겠다는 뜻이에요.\n오답 ▶ by = ~까지 \'완료\'(그때까지 한 번 끝내기). I\'ll finish it by Friday.' },
      { s: 'On the last day, Goldilocks said {to|at} Father Bear, "I deleted all my posts of your cottage, so please don\'t worry."', ex: '정답 ▶ to\n이유: say to + 사람 = ~에게 말하다\n오답 ▶ at은 shout at(~에게 소리치다), look at(~을 보다)처럼 쓰여요.' },
      { s: 'Other people already {shared|share} them on social media.', ex: '정답 ▶ shared\n이유: 이미(already) 일어난 일 → 과거형 shared\n오답 ▶ share는 현재형' },
      { s: '"From now on, I\'ll think twice before I {press|will press} POST."', ex: '정답 ▶ press\n이유: before, when, until 같은 \'시간\'을 나타내는 말 뒤에서는 미래 일이어도 현재형을 써요.\n오답 ▶ will press ✘' }
    ] },
    { type: 'verb', title: '동사변형', guide: '( ) 안의 동사를 알맞은 형태로 바꿔 쓰세요.', items: [
      { s: 'About an hour later, three bears ___ home.', v: 'come', a: ['came'], ex: '정답 ▶ came\n이유: 과거형. come - came - come (불규칙)' },
      { s: '"Someone ate my soup and ___ my chair!" cried Baby Bear.', v: 'break', a: ['broke'], ex: '정답 ▶ broke\n이유: ate(과거)와 병렬 → 과거형. break - broke - broken' },
      { s: 'Mother Bear ___ a phone next to Goldilocks.', v: 'find', a: ['found'], ex: '정답 ▶ found\n이유: 과거형. find - found - found (불규칙)' },
      { s: 'Goldilocks ___ up in surprise.', v: 'jump', a: ['jumped'], ex: '정답 ▶ jumped\n이유: 과거형 -ed\n포인트 ▶ jump up = 벌떡 일어나다' },
      { s: 'Don\'t you ___ these things are wrong?" said Father Bear.', v: 'know', a: ['know'], ex: '정답 ▶ know\n이유: Don\'t you + 동사원형 ~? (부정 의문문) 조동사 do 뒤에는 동사원형!' },
      { s: 'I\'m so sorry, and I\'ll ___ your house every day until the end of the summer," said Goldilocks.', v: 'clean', a: ['clean'], ex: '정답 ▶ clean\n이유: will(I\'ll) 뒤에는 동사원형!' },
      { s: 'All summer long, Goldilocks ___ hard.', v: 'work', a: ['worked'], ex: '정답 ▶ worked\n이유: 과거형 -ed\n포인트 ▶ all summer long = 여름 내내' },
      { s: 'Your posts will ___ on forever," said Father Bear.', v: 'live', a: ['live'], ex: '정답 ▶ live\n이유: will 뒤에는 동사원형! live on = 계속 남아 있다' }
    ] },
    { type: 'error', title: '오류찾기', guide: '어법상 틀린 곳을 고르세요.', items: [
      { s: 'About an hour later, three bears came [[to home]]. They [[went]] upstairs and [[saw]] Goldilocks.', w: 0, fix: 'home', ex: '틀린 곳 ▶ ① to home → home\n이유: home은 \'집으로\'라는 부사라 to를 쓰지 않아요. come home\n나머지 ▶ ② went(과거) ✔ ③ saw(과거, 병렬) ✔' },
      { s: '"This is terrible! Look at all these posts of our home," shouted Mother Bear [[angry]]. Goldilocks [[jumped]] up [[in]] surprise.', w: 0, fix: 'angrily', ex: '틀린 곳 ▶ ① angry → angrily\n이유: 동사 shouted를 꾸미는 말 → 부사 angrily(화가 나서)\n나머지 ▶ ② jumped up ✔ ③ in surprise(놀라서) ✔' },
      { s: 'Don\'t you [[know]] these things [[is]] [[wrong]]?', w: 1, fix: 'are', ex: '틀린 곳 ▶ ② is → are\n이유: 주어 these things가 복수 → are\n나머지 ▶ ① know(Don\'t you + 동사원형) ✔ ③ wrong ✔' },
      { s: 'On the last day, Goldilocks [[said]] to Father Bear, "I [[delete]] all my posts of your cottage, so please [[don\'t]] worry."', w: 1, fix: 'deleted', ex: '틀린 곳 ▶ ② delete → deleted\n이유: 여름이 끝난 마지막 날, 이미 지운 일을 말하니 과거형 deleted\n나머지 ▶ ① said to ✔ ③ don\'t worry(~하지 마세요) ✔' },
      { s: 'Other people already [[shared]] them on social media. Your posts will [[lives]] on [[forever]].', w: 1, fix: 'live', ex: '틀린 곳 ▶ ② lives → live\n이유: will 뒤에는 동사원형! 주어가 단수든 복수든 -s를 붙이지 않아요.\n나머지 ▶ ① shared(already + 과거) ✔ ③ forever ✔' }
    ] },
    { type: 'scramble', title: '본문 스크램블', guide: '우리말에 맞게 단어를 눌러 문장을 완성하세요.', items: [
      { ko: '약 한 시간 후에, 곰 세 마리가 집으로 돌아왔다.', en: 'About an hour later, three bears came home.' },
      { ko: '그들은 위층으로 가서 Goldilocks를 봤다.', en: 'They went upstairs and saw Goldilocks.' },
      { ko: '엄마곰이 Goldilocks 옆에서 휴대폰을 발견했다.', en: 'Mother Bear found a phone next to Goldilocks.' },
      { ko: 'Goldilocks는 놀라서 벌떡 일어났다.', en: 'Goldilocks jumped up in surprise.' },
      { ko: '여름 내내, Goldilocks는 열심히 일했다.', en: 'All summer long, Goldilocks worked hard.' },
      { ko: '다른 사람들이 이미 소셜 미디어에 그것들을 공유했어.', en: 'Other people already shared them on social media.' }
    ] },
    { type: 'order', title: '문장순서', guide: '문장을 본문 순서대로 눌러서 배열하세요.', items: [
      { lines: ['About an hour later, three bears came home.', '"Someone ate my soup and broke my chair!" cried Baby Bear.', 'They went upstairs and saw Goldilocks.', 'Mother Bear found a phone next to Goldilocks.'], flow: ['한 시간 후 곰들이 돌아옴', '아기곰: 누가 내 수프 먹고 의자 부쉈어!', '위층에서 Goldilocks 발견', '엄마곰이 옆에서 휴대폰 발견'] },
      { lines: ['"This is terrible! Look at all these posts of our home," shouted Mother Bear angrily.', 'Goldilocks jumped up in surprise.', '"You broke into our house and posted these pictures without our permission.', 'Don\'t you know these things are wrong?" said Father Bear.'], flow: ['엄마곰: 끔찍해! 이 게시물 좀 봐', 'Goldilocks가 놀라서 벌떡 일어남', '아빠곰: 허락 없이 침입해서 사진을 올렸어', '이런 게 잘못인 걸 모르니?'] },
      { lines: ['All summer long, Goldilocks worked hard.', 'On the last day, Goldilocks said to Father Bear, "I deleted all my posts of your cottage, so please don\'t worry."', '"You still don\'t understand.', 'Other people already shared them on social media.', 'Your posts will live on forever," said Father Bear.'], flow: ['여름 내내 열심히 일함', '마지막 날: 게시물 다 지웠어요', '아빠곰: 아직도 이해 못 하는구나', '다른 사람들이 이미 공유했어', '게시물은 영원히 남을 거야'] }
    ] },
    { type: 'insert', title: '문장삽입', guide: '주어진 문장이 들어가기에 가장 알맞은 곳을 고르세요.', items: [
      { lines: ['They went upstairs and saw Goldilocks.', 'Mother Bear found a phone next to Goldilocks.', '"This is terrible! Look at all these posts of our home," shouted Mother Bear angrily.'], given: 1, flow: ['위층에서 Goldilocks 발견', '엄마곰이 옆에서 휴대폰 발견', '끔찍해! 이 게시물 좀 봐'], ex: '정답 ▶ ①\n이유: 엄마곰이 \'이 게시물들을 봐!\'라고 하려면 먼저 \'휴대폰을 발견\'해야 해요.' },
      { lines: ['"This is terrible! Look at all these posts of our home," shouted Mother Bear angrily.', 'Goldilocks jumped up in surprise.', '"You broke into our house and posted these pictures without our permission.'], given: 1, flow: ['엄마곰이 화가 나서 외침', 'Goldilocks가 놀라서 벌떡 일어남', '아빠곰이 혼냄'], ex: '정답 ▶ ①\n이유: 엄마곰의 외침에 자고 있던 Goldilocks가 \'놀라서 일어난\' 뒤에 아빠곰이 혼내는 흐름이에요.' },
      { lines: ['"You still don\'t understand.', 'Other people already shared them on social media.', 'Your posts will live on forever," said Father Bear.'], given: 1, flow: ['아직도 이해 못 하는구나', '다른 사람들이 이미 공유했어', '그래서 게시물은 영원히 남아'], ex: '정답 ▶ ①\n이유: 지웠는데도 \'영원히 남는\' 이유가 \'다른 사람들이 이미 공유했기\' 때문이에요. 그래서 그 문장 바로 앞에 와요.' }
    ] },
    { type: 'odd', title: '어색한 문장', guide: '글의 흐름과 관계없는 문장을 고르세요.', items: [
      { lines: ['About an hour later, three bears came home.', '"Someone ate my soup and broke my chair!" cried Baby Bear.', 'Baby Bear was happy to find a new friend.', 'They went upstairs and saw Goldilocks.'], odd: 2, ex: '정답 ▶ ③\n이유: 아기곰은 누군가 수프를 먹고 의자를 부쉈다고 외치는 중이에요. \'새 친구를 만나 기뻤다\'는 흐름과 맞지 않아요.' },
      { lines: ['"You broke into our house and posted these pictures without our permission.', 'Don\'t you know these things are wrong?" said Father Bear.', 'Father Bear thanked Goldilocks for the nice pictures.', '"Please forgive me.'], odd: 2, ex: '정답 ▶ ③\n이유: 아빠곰은 \'잘못이라는 걸 모르니?\'라고 혼내고 Goldilocks는 용서를 빌어요. \'멋진 사진에 고마워했다\'는 반대예요.' },
      { lines: ['Other people already shared them on social media.', 'Your posts will live on forever," said Father Bear.', 'Deleted posts disappear from the Internet right away.', '"Oh, I didn\'t think about that," said Goldilocks.'], odd: 2, ex: '정답 ▶ ③\n이유: 이 글의 교훈은 \'지워도 게시물이 영원히 남는다\'예요. \'지운 게시물은 바로 사라진다\'는 정반대예요.' }
    ] },
    { type: 'blank', title: '빈칸추론', guide: '빈칸에 들어갈 말로 가장 알맞은 것을 고르세요.', items: [
      { s: 'Mother Bear found a ____ next to Goldilocks.', opts: ['phone', 'bowl', 'chair', 'book'], ex: '정답 ▶ phone\n이유: 바로 다음에 \'우리 집에 관한 이 모든 게시물을 봐요!\'라고 하니, 게시물을 볼 수 있는 \'휴대폰\'을 발견한 거예요.' },
      { s: 'Other people already ____ them on social media.', opts: ['shared', 'deleted', 'forgot', 'hid'], ex: '정답 ▶ shared\n이유: 그래서 게시물이 영원히 남는다(live on forever)고 했어요. 다른 사람들이 이미 \'공유\'했기 때문이에요.' },
      { s: 'All summer long, Goldilocks worked ____.', opts: ['hard', 'little', 'badly', 'alone'], ex: '정답 ▶ hard\n이유: 여름이 끝날 때까지 매일 청소하겠다고 약속했고, 그 약속대로 여름 내내 \'열심히\' 일했어요.\n주의 ▶ hard는 \'열심히\'(부사)예요. hardly는 \'거의 ~않다\'라 뜻이 달라요.' }
    ] },
    { type: 'mc', title: '핵심문법', guide: '알맞은 답을 고르세요.', items: [
      { q: '밑줄 친 부분의 뜻으로 알맞은 것은?<br><b>Goldilocks jumped up <u>in surprise</u>.</b>', opts: ['놀라서', '놀라운 일 속으로', '놀라게 하려고', '놀라움 없이'], ex: '정답 ▶ 놀라서\n이유: in + 감정 명사 = ~해서, ~한 채로. in surprise = 놀라서\n비교 ▶ in anger(화가 나서), with a smile(미소를 지으며)' },
      { q: '다음 질문에 \'아니요, 알아요.\'라고 답할 때 알맞은 것은?<br><b>Don\'t you know these things are wrong?</b>', opts: ['Yes, I do.', 'No, I don\'t.', 'Yes, I don\'t.', 'No, I do.'], ex: '정답 ▶ Yes, I do.\n이유: 부정 의문문(Don\'t you ~?)에도 대답은 \'내 대답이 긍정이면 Yes, 부정이면 No\'예요. 안다(긍정) → Yes, I do. 우리말로는 \'아니요, 알아요\'가 돼요.\n오답 ▶ No, I don\'t. = \'네, 몰라요\'' },
      { q: '빈칸에 알맞은 것은?<br><b>I\'ll clean your house every day ______ the end of the summer.</b>', opts: ['until', 'by', 'for', 'since'], ex: '정답 ▶ until\n이유: until = ~까지 (그때까지 계속). \'매일\' 계속 청소하니 until\n오답 ▶ by(~까지 완료), for(~ 동안 + 기간 길이), since(~ 이후로 지금까지)는 뜻이 달라요.' },
      { q: '빈칸에 알맞은 것은?<br><b>Someone ______ at the door now.</b>', opts: ['is', 'are', 'were', 'be'], ex: '정답 ▶ is\n이유: Someone(누군가)은 단수 취급 → is. now가 있으니 현재\n포인트 ▶ Someone, Everyone, No one은 모두 단수' },
      { q: '우리말과 같도록 할 때 빈칸에 알맞은 것은?<br>여름 내내, Goldilocks는 열심히 일했다.<br><b>______ summer long, Goldilocks worked hard.</b>', opts: ['All', 'Every', 'Whole', 'During'], ex: '정답 ▶ All\n이유: all ~ long = ~ 내내. all summer long(여름 내내), all day long(하루 종일)' },
      { q: '\'걱정하지 마세요.\'를 바르게 영작한 것은?', opts: ['Please don\'t worry.', 'Please not worry.', 'Please doesn\'t worry.', 'Please no worry.'], ex: '정답 ▶ Please don\'t worry.\n이유: \'~하지 마\'는 Don\'t + 동사원형 (부정 명령문). 앞에 Please를 붙이면 공손해져요.\n오답 ▶ not, doesn\'t, no로는 명령문을 만들 수 없어요.' },
      { q: '빈칸에 알맞은 것은?<br><b>I\'ll think twice before I ______ POST.</b>', opts: ['press', 'will press', 'pressed', 'presses'], ex: '정답 ▶ press\n이유: before(~하기 전에) 뒤에서는 미래의 일이어도 현재형을 써요. 주어가 I라서 press\n오답 ▶ will press(시간 부사절에 will ✘), pressed(과거), presses(3인칭 단수)' }
    ] },
    { type: 'mc', title: '요약문 완성', guide: '본문을 읽고 요약문의 빈칸 (A), (B)에 들어갈 말을 고르세요.', items: [
      { n: '❹', box: ['❹'], q: '다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 알맞은 것은?<br><b>When the bears found out what Goldilocks did, she (A) ______ for posting pictures without permission and promised to (B) ______ their house.</b>', opts: ['(A) apologized – (B) clean', '(A) laughed – (B) clean', '(A) apologized – (B) leave', '(A) laughed – (B) break', '(A) cried – (B) leave'], ex: '정답 ▶ (A) apologized – (B) clean\n(A) \'Please forgive me. I\'m so sorry\' → \'사과했다(apologized)\'\n(B) 여름이 끝날 때까지 매일 집을 \'청소하겠다(clean)\'고 약속했어요.\n오답 ▶ laughed(웃었다)·cried(울었다)는 본문에 없고, leave(떠나다)·break(부수다)는 약속한 일이 아니에요.', ev: ['Please forgive me', 'I\'ll clean your house every day until the end of the summer'] },
      { n: '❺', box: ['❺'], q: '다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 알맞은 것은?<br><b>Goldilocks learned that her posts could (A) ______ forever even after she deleted them, so she decided to think (B) ______ before posting.</b>', opts: ['(A) live on – (B) twice', '(A) disappear – (B) twice', '(A) live on – (B) less', '(A) disappear – (B) never', '(A) break – (B) less'], ex: '정답 ▶ (A) live on – (B) twice\n(A) 지워도 게시물은 영원히 \'남아 있을(live on)\' 거라고 했어요.\n(B) 그래서 \'두 번(twice)\' 생각하고 올리기로 했어요.\n오답 ▶ disappear(사라지다)는 반대, less(덜)·never(결코 ~않다)는 교훈과 맞지 않아요.', ev: ['Your posts will live on forever', 'I\'ll think twice before I press POST'] }
    ] }
  ] }
  ]
};
