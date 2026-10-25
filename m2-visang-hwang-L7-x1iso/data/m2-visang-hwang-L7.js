/* 중2 비상(황종배) Lesson 7 · A Taste of the World (본문: Food Brings Us Together)
   작성 규칙은 README.md 의 "데이터 작성 규칙" */
window.PKG = {
  id: 'm2-visang-hwang-L7',
  school: '중2 비상(황종배)',
  unit: 'Lesson 7',
  title: 'Food Brings Us Together',
  titleKo: '음식이 우리를 하나로 만듭니다',
  exam: '2학기 기말고사',
  prose: true,
  stepsBefore: ["핵심어휘·숙어", "어휘선택", "T/F 내용 확인", "어법선택", "동사변형", "오류찾기", "본문 스크램블", "문장순서", "문장삽입", "어색한 문장", "빈칸추론", "핵심문법"],   /* 일치·불일치 추가 전 단계 이름: 예전 기록을 새 단계에 맞추는 데 씀 */
  teacherPhone: '',            /* 결과 받을 번호. 예: '010-1234-5678' */

  days: [
  /* ═══════════════════════════ DAY 1 · 본문 ❶❷ ═══════════════════════════ */
  {
    id: 'd1', name: 'DAY 1', range: '7과 본문 ❶❷', story: '한국의 김장 · 아제르바이잔의 플랫브레드',
    passage: [
      ['', '❶', ''],
      ['Minchan', "Hello, I'm Minchan!", '안녕하세요, 저는 민찬이에요!'],
      ['', "Today, my family and I are at my grandmother's house to do gimjang.", '오늘 저희 가족과 저는 김장을 하기 위해 할머니 댁에 있어요.'],
      ['', 'What is gimjang?', '김장은 무엇일까요?'],
      ['', 'It is a Korean cultural tradition to get together and make a lot of kimchi before winter comes.', '그것은 겨울이 오기 전에 함께 모여 많은 김치를 만드는 한국의 문화적 전통이에요.'],
      ['', 'Gimjang is more than making kimchi.', '김장은 김치를 만드는 것 이상이에요.'],
      ['', "It's also about spending time with family.", '그것은 또한 가족과 시간을 보내는 것에 관한 것이에요.'],
      ['', 'It is always good to get together.', '함께 모이는 것은 언제나 좋아요.'],
      ['', 'Do you also have any special food traditions?', '여러분도 어떤 특별한 음식 전통이 있나요?'],
      ['', '❷', ''],
      ['Emil', "Hi, I'm Emil!", '안녕하세요, 저는 Emil이에요!'],
      ['', 'We also have this kind of cultural tradition in Azerbaijan.', '아제르바이잔에도 이런 종류의 문화적 전통이 있어요.'],
      ['', "Here's a picture from my aunt's wedding.", '여기 제 이모 결혼식 사진이 있어요.'],
      ['', 'Do you see the thing on her shoulder?', '그녀의 어깨 위에 있는 물건이 보이나요?'],
      ['', "It's a flatbread.", '그것은 플랫브레드예요.'],
      ['', 'It is so big that it covers her shoulder.', '그것은 매우 커서 그녀의 어깨를 덮어요.'],
      ['', 'We believe that putting the bread over the shoulder brings good luck.', '우리는 그 빵을 어깨 위에 올려두는 것이 행운을 가져온다고 믿어요.'],
      ['', 'A flatbread is made only from flour, salt, and water.', '플랫브레드는 밀가루, 소금, 물로만 만들어져요.'],
      ['', 'We eat this bread at every meal, but we make it bigger on special days.', '우리는 매 끼니에 이 빵을 먹지만, 특별한 날에는 더 크게 만들어요.'],
      ['', 'So, everyone in the community gets together and helps out.', '그래서 공동체에 있는 모든 사람이 함께 모여서 도와줘요.'],
      ['', 'Baking the bread together makes our community stronger.', '함께 빵을 굽는 일은 우리 공동체를 더욱 단단하게 만들어 줘요.']
    ],
    steps: [
      { type: 'vocab', title: '핵심어휘·숙어', quizN: 15, items: [
        ['grandmother', '할머니'], ['cultural', '문화의, 문화적인'], ['tradition', '전통'], ['get together', '모이다'],
        ['a lot of', '많은'], ['before', '~하기 전에'], ['more than', '~ 이상'], ['spend time', '시간을 보내다'],
        ['special', '특별한'], ['kind', '종류'], ['aunt', '이모, 고모'], ['wedding', '결혼식'],
        ['shoulder', '어깨'], ['flatbread', '납작한 빵, 플랫브레드'], ['so ~ that ...', '너무 ~해서 …하다'], ['cover', '덮다'],
        ['believe', '믿다'], ['bring good luck', '행운을 가져오다'], ['be made from', '~로 만들어지다'], ['flour', '밀가루'],
        ['salt', '소금'], ['meal', '식사, 끼니'], ['community', '공동체'], ['help out', '돕다'],
        ['bake', '굽다'], ['stronger', '더 강한, 더 단단한']
      ]},
      { type: 'pick', title: '어휘선택', guide: '문맥에 맞는 낱말을 고르세요.', items: [
        { s: "Today, my family and I are at my grandmother's house to {do|buy} gimjang.", ex: 'do gimjang: 김장을 하다' },
        { s: 'It is a Korean cultural tradition to get together and make a lot of kimchi before {winter|summer} comes.', ex: '김장은 겨울이 오기 전에 한다.' },
        { s: 'Gimjang is {more|less} than making kimchi.', ex: 'more than: ~ 이상 (가족과 시간을 보내는 일이기도 하다)' },
        { s: "It's also about {spending|wasting} time with family.", ex: 'spend time with: ~와 시간을 보내다' },
        { s: 'We also have this kind of cultural {tradition|problem} in Azerbaijan.', ex: '김장과 같은 문화적 전통(tradition)' },
        { s: "Here's a picture from my aunt's {wedding|school}.", ex: 'wedding: 결혼식' },
        { s: 'It is so big that it {covers|breaks} her shoulder.', ex: 'cover: 덮다' },
        { s: 'We believe that putting the bread over the shoulder brings good {luck|weather}.', ex: 'bring good luck: 행운을 가져오다' },
        { s: 'A flatbread is made only from {flour|rice}, salt, and water.', ex: '빵은 밀가루(flour)로 만든다.' },
        { s: 'We eat this bread at every meal, but we make it {bigger|smaller} on special days.', ex: '특별한 날엔 더 크게 → 모두가 도와야 한다' },
        { s: 'Baking the bread together makes our community {stronger|weaker}.', ex: '함께 구우며 공동체가 더 단단해진다.' }
      ]},
      { type: 'tf', title: 'T/F 내용 확인', guide: '본문 내용과 일치하면 T, 다르면 F를 고르세요.', items: [
        ["Minchan is at his grandmother's house to do gimjang.", true, "at my grandmother's house to do gimjang"],
        ['Gimjang is done after winter.', false, '겨울이 오기 전(before winter)에 한다.'],
        ['Gimjang is only about making kimchi.', false, '가족과 시간을 보내는 것이기도 하다.'],
        ['Emil has a similar cultural tradition in Azerbaijan.', true, 'this kind of cultural tradition in Azerbaijan'],
        ["The picture is from Emil's aunt's birthday party.", false, '이모의 결혼식(wedding) 사진이다.'],
        ['The flatbread is so small that it fits in her hand.', false, '너무 커서 어깨를 덮는다.'],
        ['A flatbread is made from flour, salt, and water.', true, 'made only from flour, salt, and water'],
        ['Baking the bread together makes the community stronger.', true, 'makes our community stronger']
      ]},
      { type: 'mc', title: '일치·불일치', guide: "본문을 읽고 내용과 맞는지 확인해요. 틀린 선택지는 해설의 근거 문장과 비교해 보세요.", items: [
        { n: "❶", box: ["❶"], q: "김장에 관한 내용과 일치하지 <u>않는</u> 것은?", opts: ["Gimjang is only about making kimchi.", "Minchan's family is at his grandmother's house.", "People make a lot of kimchi before winter comes.", "Gimjang is also about spending time with family.", "Minchan thinks it is good to get together."], ex: "정답 근거: Gimjang is more than making kimchi.\n· more than ~ : ~ 이상의 것 · get together : 모이다 · tradition : 전통", per: [["김장은 김치를 만드는 것일 뿐이다.", "Gimjang is more than making kimchi", "불일치 → 김치 만들기 이상"], ["민찬이네 가족은 할머니 댁에 있다.", "my family and I are at my grandmother's house", "일치"], ["겨울이 오기 전에 많은 김치를 만든다.", "make a lot of kimchi before winter comes", "일치"], ["김장은 가족과 시간을 보내는 것이기도 하다.", "It's also about spending time with family", "일치"], ["민찬이는 함께 모이는 것이 좋다고 생각한다.", "It is always good to get together", "일치"]] },
        { n: "❷", box: ["❷"], q: "Emil의 전통에 관한 내용과 <u>일치하는</u> 것은?", opts: ["People believe the bread on the shoulder brings good luck.", "The picture is from Emil's sister's wedding.", "The flatbread is so small that it fits in a hand.", "A flatbread is made from flour, sugar, and milk.", "People in Azerbaijan eat flatbread only on special days."], ex: "정답 근거: We believe that putting the bread over the shoulder brings good luck.\n· so ~ that ... : 너무 ~해서 …하다 · flour : 밀가루 · community : 공동체", per: [["사람들은 어깨 위의 빵이 행운을 가져온다고 믿는다.", "putting the bread over the shoulder brings good luck", "일치"], ["사진은 Emil의 언니(누나) 결혼식 사진이다.", "my aunt's wedding", "불일치 → 이모(고모) 결혼식"], ["플랫브레드는 아주 작아서 손에 쏙 들어간다.", "It is so big that it covers her shoulder", "불일치 → 어깨를 덮을 만큼 큼"], ["플랫브레드는 밀가루, 설탕, 우유로 만든다.", "made only from flour, salt, and water", "불일치 → 밀가루, 소금, 물"], ["아제르바이잔 사람들은 특별한 날에만 플랫브레드를 먹는다.", "We eat this bread at every meal", "불일치 → 매 끼니 먹음"]] }
      ]},
      { type: 'pick', title: '어법선택', guide: '어법상 알맞은 것을 고르세요.', items: [
        { s: "Today, my family and I {are|am} at my grandmother's house to do gimjang.", ex: 'my family and I(복수) → are' },
        { s: "Today, my family and I are at my grandmother's house {to do|doing} gimjang.", ex: '목적(~하기 위해) → to부정사' },
        { s: 'It is a Korean cultural tradition {to get|get} together and make a lot of kimchi before winter comes.', ex: '명사를 꾸미는 to부정사' },
        { s: 'It is a Korean cultural tradition to get together and make a lot of kimchi before winter {comes|will come}.', ex: '때를 나타내는 부사절은 현재가 미래를 대신한다.' },
        { s: 'Gimjang is more than {making|make} kimchi.', ex: '전치사 than 뒤 → 동명사' },
        { s: "It's also about {spending|spend} time with family.", ex: '전치사 about 뒤 → 동명사' },
        { s: 'It is always good {to get|got} together.', ex: '가주어 It ~ 진주어 to부정사' },
        { s: 'It is so big {that|what} it covers her shoulder.', ex: 'so ~ that ...: 너무 ~해서 …하다' },
        { s: 'We believe that putting the bread over the shoulder {brings|bring} good luck.', ex: '동명사 주어(putting ~)는 단수 → brings' },
        { s: 'A flatbread is made only {from|by} flour, salt, and water.', ex: 'be made from: ~로 만들어지다(재료)' },
        { s: 'So, everyone in the community {gets|get} together and helps out.', ex: 'everyone은 단수 → gets' },
        { s: 'Baking the bread together makes our community {stronger|strongly}.', ex: 'make + O + 형용사' }
      ]},
      { type: 'verb', title: '동사변형', guide: '( ) 안의 동사를 알맞은 형태로 바꿔 쓰세요.', items: [
        { s: "Today, my family and I are at my grandmother's house ___ gimjang.", v: 'do', a: ['to do'], ex: '목적(~하기 위해) → to do' },
        { s: 'It is a Korean cultural tradition to get together and make a lot of kimchi before winter ___.', v: 'come', a: ['comes'], ex: '시간 부사절 → 현재형, 3인칭 단수' },
        { s: 'Gimjang is more than ___ kimchi.', v: 'make', a: ['making'], ex: '전치사 than 뒤 → 동명사' },
        { s: "It's also about ___ time with family.", v: 'spend', a: ['spending'], ex: '전치사 about 뒤 → 동명사' },
        { s: 'It is always good ___ together.', v: 'get', a: ['to get'], ex: '가주어 It ~ 진주어 to부정사' },
        { s: 'It is so big that it ___ her shoulder.', v: 'cover', a: ['covers'], ex: '주어 it → covers' },
        { s: 'We believe that ___ the bread over the shoulder brings good luck.', v: 'put', a: ['putting'], ex: '주어 자리 → 동명사 putting' },
        { s: 'A flatbread is ___ only from flour, salt, and water.', v: 'make', a: ['made'], ex: 'be made from' },
        { s: 'So, everyone in the community ___ together and helps out.', v: 'get', a: ['gets'], ex: 'everyone(단수) → gets' },
        { s: '___ the bread together makes our community stronger.', v: 'bake', a: ['Baking'], ex: '주어 자리 → 동명사 Baking' }
      ]},
      { type: 'error', title: '오류찾기', guide: '어법상 틀린 곳을 고르세요.', items: [
        { s: "Today, my family and I [[am]] at my [[grandmother's]] house [[to do]] gimjang. What [[is]] gimjang?", w: 0, fix: 'are', ex: 'my family and I(복수) → are' },
        { s: 'It is a Korean cultural tradition [[get]] together and [[make]] a lot of kimchi [[before]] winter [[comes]].', w: 0, fix: 'to get', ex: '명사를 꾸미는 to부정사 → to get' },
        { s: "Gimjang is more than [[make]] kimchi. It's also about [[spending]] time [[with]] family. It is always good [[to get]] together.", w: 0, fix: 'making', ex: '전치사 than 뒤 → 동명사' },
        { s: 'It is so big [[what]] it [[covers]] her shoulder. We [[believe]] that putting the bread over the shoulder [[brings]] good luck.', w: 0, fix: 'that', ex: 'so ~ that ...' },
        { s: 'We believe that putting the bread over the shoulder [[bring]] good luck. A flatbread [[is made]] only [[from]] flour, salt, and water.', w: 0, fix: 'brings', ex: '동명사 주어는 단수 → brings' },
        { s: 'We eat this bread at every [[meal]], but we make it [[more bigger]] on special days. So, everyone in the community [[gets]] together and [[helps]] out.', w: 1, fix: 'bigger', ex: 'big의 비교급은 bigger (more와 함께 쓰지 않음)' },
        { s: 'So, everyone in the community [[get]] together and [[helps]] out. [[Baking]] the bread together makes our community [[stronger]].', w: 0, fix: 'gets', ex: 'everyone은 단수 → gets' }
      ]},
      { type: 'scramble', title: '본문 스크램블', guide: '우리말에 맞게 단어를 눌러 문장을 완성하세요.', items: [
        { ko: '그것은 겨울이 오기 전에 함께 모여 많은 김치를 만드는 한국의 문화적 전통이에요.', en: 'It is a Korean cultural tradition to get together and make a lot of kimchi before winter comes.' },
        { ko: '김장은 김치를 만드는 것 이상이에요.', en: 'Gimjang is more than making kimchi.' },
        { ko: '함께 모이는 것은 언제나 좋아요.', en: 'It is always good to get together.' },
        { ko: '그것은 매우 커서 그녀의 어깨를 덮어요.', en: 'It is so big that it covers her shoulder.' },
        { ko: '플랫브레드는 밀가루, 소금, 물로만 만들어져요.', en: 'A flatbread is made only from flour, salt, and water.' },
        { ko: '함께 빵을 굽는 일은 우리 공동체를 더욱 단단하게 만들어 줘요.', en: 'Baking the bread together makes our community stronger.' }
      ]},
      { type: 'order', title: '문장순서', guide: '문장을 본문 순서대로 눌러서 배열하세요.', items: [
        { lines: [
          "Today, my family and I are at my grandmother's house to do gimjang.",
          'What is gimjang?',
          'It is a Korean cultural tradition to get together and make a lot of kimchi before winter comes.',
          'Gimjang is more than making kimchi.'
        ]},
        { lines: [
          'Gimjang is more than making kimchi.',
          "It's also about spending time with family.",
          'It is always good to get together.',
          'Do you also have any special food traditions?'
        ]},
        { lines: [
          "Here's a picture from my aunt's wedding.",
          'Do you see the thing on her shoulder?',
          "It's a flatbread.",
          'It is so big that it covers her shoulder.'
        ]},
        { lines: [
          'A flatbread is made only from flour, salt, and water.',
          'We eat this bread at every meal, but we make it bigger on special days.',
          'So, everyone in the community gets together and helps out.',
          'Baking the bread together makes our community stronger.'
        ]}
      ]},
      { type: 'insert', title: '문장삽입', guide: '주어진 문장이 들어가기에 가장 알맞은 곳을 고르세요.', items: [
        { lines: [
          'What is gimjang?',
          'It is a Korean cultural tradition to get together and make a lot of kimchi before winter comes.',
          'Gimjang is more than making kimchi.',
          "It's also about spending time with family."
        ], given: 3, ex: '"김치를 만드는 것 이상"이라는 말 뒤에 "또한(also) 가족과 시간을 보내는 것"이 온다.' },
        { lines: [
          'Do you see the thing on her shoulder?',
          "It's a flatbread.",
          'It is so big that it covers her shoulder.',
          'We believe that putting the bread over the shoulder brings good luck.'
        ], given: 1, ex: '"어깨 위의 물건이 보이나요?"라는 질문에 대한 대답이다.' },
        { lines: [
          'We eat this bread at every meal, but we make it bigger on special days.',
          'So, everyone in the community gets together and helps out.',
          'Baking the bread together makes our community stronger.'
        ], given: 1, ex: '특별한 날엔 빵이 커서 → 그래서(So) 모두가 모여 돕는다.' }
      ]},
      { type: 'odd', title: '어색한 문장', guide: '글의 흐름과 관계없는 문장을 고르세요.', items: [
        { lines: [
          'It is a Korean cultural tradition to get together and make a lot of kimchi before winter comes.',
          'Gimjang is more than making kimchi.',
          'Families never meet during gimjang.',
          "It's also about spending time with family."
        ], odd: 2, ex: '김장은 가족이 함께 모이는 전통이다.' },
        { lines: [
          "It's a flatbread.",
          'It is so big that it covers her shoulder.',
          'The bread is too small to see in the picture.',
          'We believe that putting the bread over the shoulder brings good luck.'
        ], odd: 2, ex: '빵은 어깨를 덮을 만큼 크다.' },
        { lines: [
          'A flatbread is made only from flour, salt, and water.',
          'People in Azerbaijan never eat bread at meals.',
          'We eat this bread at every meal, but we make it bigger on special days.',
          'So, everyone in the community gets together and helps out.'
        ], odd: 1, ex: '매 끼니마다 이 빵을 먹는다는 내용과 반대된다.' }
      ]},
      { type: 'blank', title: '빈칸추론', guide: '빈칸에 들어갈 말로 가장 알맞은 것을 고르세요.', items: [
        { s: "It's also about ____.", opts: ['spending time with family', 'buying kimchi at a store', 'eating alone', 'going on a trip'], ex: '김장은 가족과 시간을 보내는 일이기도 하다.' },
        { s: 'It is so big that it ____.', opts: ['covers her shoulder', 'fits in her pocket', 'falls on the floor', 'breaks into pieces'], ex: '너무 커서 어깨를 덮는다.' },
        { s: 'We believe that putting the bread over the shoulder ____.', opts: ['brings good luck', 'makes people sad', 'is a bad idea', 'breaks the bread'], ex: '빵을 어깨에 올리면 행운이 온다고 믿는다.' },
        { s: 'Baking the bread together makes our community ____.', opts: ['stronger', 'weaker', 'quieter', 'smaller'], ex: '함께 빵을 구우며 공동체가 단단해진다.' }
      ]},
      { type: 'mc', title: '핵심문법', guide: '알맞은 답을 고르세요.', items: [
        { q: '빈칸에 알맞은 것은?<br><b>______ is always good to get together.</b>', opts: ['It', 'That', 'This', 'What'], ex: '가주어 It ~ 진주어 to부정사' },
        { q: '"함께 모이는 것은 언제나 좋다."를 바르게 영작한 것은?', opts: ['It is always good to get together.', 'It is always good get together.', 'That is always good to get together.', 'It always good is to get together.'], ex: '가주어 It ~ 진주어 to부정사' },
        { q: '빈칸에 알맞은 것은?<br><b>It is ______ big that it covers her shoulder.</b>', opts: ['so', 'very', 'too', 'such'], ex: 'so + 형용사 + that: 너무 ~해서 …하다' },
        { q: '다음 문장의 뜻으로 알맞은 것은?<br><b>It is so big that it covers her shoulder.</b>', opts: ['그것은 너무 커서 그녀의 어깨를 덮는다.', '그것은 그녀의 어깨를 덮을 만큼 작다.', '그것은 너무 커서 어깨를 덮지 못한다.', '그것은 그녀의 어깨보다 작다.'], ex: 'so ~ that ...: 너무 ~해서 …하다' },
        { q: '빈칸에 알맞은 것은?<br><b>Baking the bread together ______ our community stronger.</b>', opts: ['makes', 'make', 'making', 'to make'], ex: '동명사 주어는 단수 취급' },
        { q: '빈칸에 알맞은 것은?<br><b>It makes our community ______.</b>', opts: ['stronger', 'strongly', 'strength', 'to strong'], ex: 'make + O + 형용사' },
        { q: '빈칸에 알맞은 것은?<br><b>A flatbread is made ______ flour, salt, and water.</b>', opts: ['from', 'by', 'to', 'at'], ex: 'be made from: ~로 만들어지다(재료가 변함)' },
        { q: '밑줄 친 to부정사가 <b>"~하기 위해"</b>의 뜻으로 쓰인 것은?', opts: ["We are at my grandmother's house <u>to do</u> gimjang.", 'It is always good <u>to get</u> together.', 'I want <u>to make</u> kimchi.', 'It is fun <u>to bake</u> bread.'], ex: '①만 목적(~하기 위해). ②④는 진주어, ③은 목적어' }
      ]}
    ]
  },

  /* ═══════════════════════════ DAY 2 · 본문 ❸ ═══════════════════════════ */
  {
    id: 'd2', name: 'DAY 2', range: '7과 본문 ❸', story: '싱가포르의 호커 센터',
    passage: [
      ['', '❸', ''],
      ['Vivian', "I'm Vivian!", '저는 Vivian이에요!'],
      ['', 'Have you heard of hawker centers in Singapore?', '여러분은 싱가포르에 있는 호커 센터에 대해 들어 본 적 있나요?'],
      ['', 'Hawkers are people who sell food on the street.', '호커는 길거리에서 음식을 파는 사람들을 말해요.'],
      ['', 'They formed the hawker centers and these centers have become a huge food community.', '그들이 호커 센터를 만들었고, 이 센터들이 거대한 음식 공동체가 되었어요.'],
      ['', 'These centers are so popular that they are always full of people.', '이 센터들은 매우 인기 있어서 늘 사람들로 가득 차요.'],
      ['', 'There are all kinds of food, from Chinese noodles to Malaysian curry to Indonesian satay.', '중국식 국수부터 말레이시아식 카레, 인도네시아식 사테까지 모든 종류의 음식들이 있어요.'],
      ['', 'My friends and I are from different countries.', '제 친구들과 저는 서로 다른 나라 출신이에요.'],
      ['', 'We all have different food tastes.', '우리는 모두 음식 취향이 달라요.'],
      ['', 'But at the hawker centers, we can always find something we like.', '하지만 호커 센터에서 우리는 항상 우리가 좋아하는 것을 찾을 수 있어요.'],
      ['', 'Sometimes, we share the tables with strangers and end up becoming friends.', '때때로 우리는 낯선 사람들과 테이블을 함께 쓰다가 친구가 되기도 해요.'],
      ['', 'It is fun to enjoy the food with good people.', '좋은 사람들과 함께 음식을 즐기는 건 재미있어요.'],
      ['', "That's why I love this hawker culture.", '그게 제가 이 호커 문화를 사랑하는 이유예요.']
    ],
    steps: [
      { type: 'vocab', title: '핵심어휘·숙어', quizN: 15, items: [
        ['hear of', '~에 대해 듣다'], ['hawker', '노점상'], ['sell', '팔다'], ['on the street', '길거리에서'],
        ['form', '만들다, 형성하다'], ['huge', '거대한'], ['community', '공동체'], ['popular', '인기 있는'],
        ['be full of', '~로 가득 차다'], ['all kinds of', '모든 종류의'], ['from A to B', 'A부터 B까지'], ['noodle', '국수'],
        ['curry', '카레'], ['country', '나라'], ['taste', '취향, 맛'], ['something', '어떤 것'],
        ['share A with B', 'A를 B와 함께 쓰다, 나누다'], ['stranger', '낯선 사람'], ['end up -ing', '결국 ~하게 되다'], ['fun', '재미있는'],
        ["That's why ~", '그것이 ~하는 이유다'], ['culture', '문화']
      ]},
      { type: 'pick', title: '어휘선택', guide: '문맥에 맞는 낱말을 고르세요.', items: [
        { s: 'Hawkers are people who {sell|buy} food on the street.', ex: 'hawker: 길거리에서 음식을 파는(sell) 사람' },
        { s: 'They {formed|closed} the hawker centers and these centers have become a huge food community.', ex: 'form: 만들다, 형성하다' },
        { s: 'They formed the hawker centers and these centers have become a {huge|tiny} food community.', ex: 'huge: 거대한' },
        { s: 'These centers are so {popular|quiet} that they are always full of people.', ex: '인기가 많아서(popular) 사람들로 가득하다.' },
        { s: 'There are all {kinds|names} of food, from Chinese noodles to Malaysian curry to Indonesian satay.', ex: 'all kinds of: 모든 종류의' },
        { s: 'My friends and I are from {different|the same} countries.', ex: '나라가 달라서 음식 취향도 다르다.' },
        { s: 'We all have different food {tastes|names}.', ex: 'taste: 취향, 입맛' },
        { s: 'Sometimes, we share the tables with {strangers|teachers} and end up becoming friends.', ex: 'stranger: 낯선 사람 → 친구가 된다' },
        { s: 'It is {fun|boring} to enjoy the food with good people.', ex: '좋은 사람들과 즐기는 건 재미있다(fun).' },
        { s: "That's why I {love|hate} this hawker culture.", ex: '앞의 좋은 점들이 호커 문화를 사랑하는 이유다.' }
      ]},
      { type: 'tf', title: 'T/F 내용 확인', guide: '본문 내용과 일치하면 T, 다르면 F를 고르세요.', items: [
        ['Hawkers are people who sell food on the street.', true, 'Hawkers are people who sell food on the street.'],
        ['The hawker centers are usually empty.', false, '늘 사람들로 가득 차 있다.'],
        ['At hawker centers, you can only eat Chinese food.', false, '중국·말레이시아·인도네시아 등 모든 종류의 음식이 있다.'],
        ['Vivian and her friends are all from the same country.', false, '서로 다른 나라 출신이다.'],
        ['Vivian and her friends have different food tastes.', true, 'We all have different food tastes.'],
        ['Vivian can always find something she likes at the hawker centers.', true, 'we can always find something we like'],
        ['Vivian sometimes becomes friends with strangers there.', true, 'end up becoming friends'],
        ["Vivian doesn't like the hawker culture.", false, '호커 문화를 사랑한다.']
      ]},
      { type: 'mc', title: '일치·불일치', guide: "본문을 읽고 내용과 맞는지 확인해요. 틀린 선택지는 해설의 근거 문장과 비교해 보세요.", items: [
        { n: "❸", box: ["❸"], q: "호커 센터에 관한 내용과 일치하지 <u>않는</u> 것은?", opts: ["Hawker centers are usually empty.", "Hawkers are people who sell food on the street.", "There are many kinds of food at hawker centers.", "Vivian and her friends are from different countries.", "Vivian sometimes shares tables with strangers."], ex: "정답 근거: These centers are so popular that they are always full of people.\n· be full of : ~로 가득 차다 · stranger : 낯선 사람 · end up -ing : 결국 ~하게 되다", per: [["호커 센터는 보통 비어 있다.", "they are always full of people", "불일치 → 늘 사람들로 가득 참"], ["호커는 길에서 음식을 파는 사람들이다.", "Hawkers are people who sell food on the street", "일치"], ["호커 센터에는 여러 종류의 음식이 있다.", "There are all kinds of food", "일치"], ["Vivian과 친구들은 서로 다른 나라 출신이다.", "My friends and I are from different countries", "일치"], ["Vivian은 가끔 낯선 사람과 테이블을 함께 쓴다.", "we share the tables with strangers", "일치"]] },
        { n: "❸", box: ["❸"], q: "호커 센터에 관한 내용과 <u>일치하는</u> 것은?", opts: ["Vivian and her friends can always find something they like there.", "Hawker centers sell only Chinese food.", "Vivian and her friends have the same food tastes.", "Vivian never becomes friends with strangers there.", "Vivian doesn't like the hawker culture."], ex: "정답 근거: But at the hawker centers, we can always find something we like.\n· taste : 취향, 입맛 · That's why ~ : 그래서 ~하다, 그것이 ~하는 이유이다", per: [["Vivian과 친구들은 그곳에서 늘 좋아하는 것을 찾을 수 있다.", "we can always find something we like", "일치"], ["호커 센터는 중국 음식만 판다.", "from Chinese noodles to Malaysian curry to Indonesian satay", "불일치 → 여러 나라 음식"], ["Vivian과 친구들은 음식 취향이 같다.", "We all have different food tastes", "불일치 → 취향이 다름"], ["Vivian은 그곳에서 낯선 사람과 친구가 되는 일이 없다.", "end up becoming friends", "불일치 → 친구가 되기도 함"], ["Vivian은 호커 문화를 좋아하지 않는다.", "That's why I love this hawker culture", "불일치 → 아주 좋아함"]] }
      ]},
      { type: 'pick', title: '어법선택', guide: '어법상 알맞은 것을 고르세요.', items: [
        { s: '{Have you heard|Did you heard} of hawker centers in Singapore?', ex: '현재완료 의문문: Have + 주어 + p.p.?' },
        { s: 'Hawkers are people {who|which} sell food on the street.', ex: '선행사가 사람 → who' },
        { s: 'Hawkers are people who {sell|sells} food on the street.', ex: '선행사 people(복수) → sell' },
        { s: 'They formed the hawker centers and these centers have {become|became} a huge food community.', ex: '현재완료 have + p.p.(become)' },
        { s: 'These centers are so popular {that|what} they are always full of people.', ex: 'so ~ that ...' },
        { s: 'These centers are so popular that they are always full {of|with} people.', ex: 'be full of: ~로 가득 차다' },
        { s: '{There are|There is} all kinds of food, from Chinese noodles to Malaysian curry to Indonesian satay.', ex: 'all kinds of food(복수 의미) → There are' },
        { s: 'My friends and I {are|am} from different countries.', ex: 'My friends and I(복수) → are' },
        { s: 'Sometimes, we share the tables with strangers and end up {becoming|to become} friends.', ex: 'end up + -ing' },
        { s: 'It is fun {to enjoy|enjoy} the food with good people.', ex: '가주어 It ~ 진주어 to부정사' },
        { s: "{That's why|That's because} I love this hawker culture.", ex: '앞이 이유, 뒤가 결과 → That\'s why' }
      ]},
      { type: 'verb', title: '동사변형', guide: '( ) 안의 동사를 알맞은 형태로 바꿔 쓰세요.', items: [
        { s: 'Have you ___ of hawker centers in Singapore?', v: 'hear', a: ['heard'], ex: '현재완료 have + p.p.' },
        { s: 'Hawkers are people who ___ food on the street.', v: 'sell', a: ['sell'], ex: '선행사 people(복수) → sell' },
        { s: 'They ___ the hawker centers and these centers have become a huge food community.', v: 'form', a: ['formed'], ex: '과거형 formed' },
        { s: 'They formed the hawker centers and these centers have ___ a huge food community.', v: 'become', a: ['become'], ex: 'become - became - become' },
        { s: 'These centers are so popular that they ___ always full of people.', v: 'be', a: ['are'], ex: '주어 they → are' },
        { s: 'But at the hawker centers, we can always ___ something we like.', v: 'find', a: ['find'], ex: 'can + 동사원형' },
        { s: 'Sometimes, we ___ the tables with strangers and end up becoming friends.', v: 'share', a: ['share'], ex: '주어 we → share' },
        { s: 'Sometimes, we share the tables with strangers and end up ___ friends.', v: 'become', a: ['becoming'], ex: 'end up + -ing' },
        { s: 'It is fun ___ the food with good people.', v: 'enjoy', a: ['to enjoy'], ex: '가주어 It ~ 진주어 to부정사' },
        { s: "That's why I ___ this hawker culture.", v: 'love', a: ['love'], ex: '주어 I → love' }
      ]},
      { type: 'error', title: '오류찾기', guide: '어법상 틀린 곳을 고르세요.', items: [
        { s: 'Have you [[heard]] of hawker centers in Singapore? Hawkers are people [[which]] [[sell]] food [[on]] the street.', w: 1, fix: 'who', ex: '선행사가 사람 → who' },
        { s: 'They [[formed]] the hawker centers and these centers have [[became]] a [[huge]] food community.', w: 1, fix: 'become', ex: '현재완료 have + p.p. → become' },
        { s: 'These centers are [[so]] popular [[what]] they are always [[full]] [[of]] people.', w: 1, fix: 'that', ex: 'so ~ that ...' },
        { s: 'There [[is]] all kinds of food, [[from]] Chinese noodles [[to]] Malaysian curry to Indonesian satay.', w: 0, fix: 'are', ex: 'all kinds of food → There are' },
        { s: 'My friends and I [[am]] from different countries. We all [[have]] different food tastes. But at the hawker centers, we can always [[find]] something we [[like]].', w: 0, fix: 'are', ex: 'My friends and I(복수) → are' },
        { s: 'Sometimes, we [[share]] the tables [[with]] strangers and end up [[to become]] friends.', w: 2, fix: 'becoming', ex: 'end up + -ing' },
        { s: "It is fun [[enjoy]] the food with good people. That's [[why]] I [[love]] this hawker [[culture]].", w: 0, fix: 'to enjoy', ex: '가주어 It ~ 진주어 to부정사' }
      ]},
      { type: 'scramble', title: '본문 스크램블', guide: '우리말에 맞게 단어를 눌러 문장을 완성하세요.', items: [
        { ko: '호커는 길거리에서 음식을 파는 사람들이에요.', en: 'Hawkers are people who sell food on the street.' },
        { ko: '이 센터들은 매우 인기 있어서 늘 사람들로 가득 차요.', en: 'These centers are so popular that they are always full of people.' },
        { ko: '우리는 모두 음식 취향이 달라요.', en: 'We all have different food tastes.' },
        { ko: '하지만 호커 센터에서 우리는 항상 우리가 좋아하는 것을 찾을 수 있어요.', en: 'But at the hawker centers, we can always find something we like.' },
        { ko: '때때로 우리는 낯선 사람들과 테이블을 함께 쓰다가 친구가 되기도 해요.', en: 'Sometimes, we share the tables with strangers and end up becoming friends.' },
        { ko: '좋은 사람들과 함께 음식을 즐기는 건 재미있어요.', en: 'It is fun to enjoy the food with good people.' },
        { ko: '그게 제가 이 호커 문화를 사랑하는 이유예요.', en: "That's why I love this hawker culture." }
      ]},
      { type: 'order', title: '문장순서', guide: '문장을 본문 순서대로 눌러서 배열하세요.', items: [
        { lines: [
          'Have you heard of hawker centers in Singapore?',
          'Hawkers are people who sell food on the street.',
          'They formed the hawker centers and these centers have become a huge food community.',
          'These centers are so popular that they are always full of people.'
        ]},
        { lines: [
          'These centers are so popular that they are always full of people.',
          'There are all kinds of food, from Chinese noodles to Malaysian curry to Indonesian satay.',
          'My friends and I are from different countries.',
          'We all have different food tastes.'
        ]},
        { lines: [
          'But at the hawker centers, we can always find something we like.',
          'Sometimes, we share the tables with strangers and end up becoming friends.',
          'It is fun to enjoy the food with good people.',
          "That's why I love this hawker culture."
        ]}
      ]},
      { type: 'insert', title: '문장삽입', guide: '주어진 문장이 들어가기에 가장 알맞은 곳을 고르세요.', items: [
        { lines: [
          'Have you heard of hawker centers in Singapore?',
          'Hawkers are people who sell food on the street.',
          'They formed the hawker centers and these centers have become a huge food community.'
        ], given: 1, ex: 'They는 Hawkers를 가리키므로 호커를 설명한 문장이 먼저 와야 한다.' },
        { lines: [
          'My friends and I are from different countries.',
          'We all have different food tastes.',
          'But at the hawker centers, we can always find something we like.'
        ], given: 2, ex: 'But: 취향은 다르지만 호커 센터에선 모두 좋아하는 것을 찾는다.' },
        { lines: [
          'Sometimes, we share the tables with strangers and end up becoming friends.',
          'It is fun to enjoy the food with good people.',
          "That's why I love this hawker culture."
        ], given: 2, ex: "That's why: 앞의 이유들 때문에 호커 문화를 사랑한다." }
      ]},
      { type: 'odd', title: '어색한 문장', guide: '글의 흐름과 관계없는 문장을 고르세요.', items: [
        { lines: [
          'Hawkers are people who sell food on the street.',
          'They formed the hawker centers and these centers have become a huge food community.',
          'Hawker centers are always quiet and empty.',
          'These centers are so popular that they are always full of people.'
        ], odd: 2, ex: '늘 사람들로 가득하다는 내용과 반대된다.' },
        { lines: [
          'These centers are so popular that they are always full of people.',
          'There are all kinds of food, from Chinese noodles to Malaysian curry to Indonesian satay.',
          'You can eat only one kind of food there.',
          'My friends and I are from different countries.'
        ], odd: 2, ex: '모든 종류의 음식이 있다는 내용과 반대된다.' },
        { lines: [
          'But at the hawker centers, we can always find something we like.',
          'Sometimes, we share the tables with strangers and end up becoming friends.',
          "We never talk to people we don't know.",
          'It is fun to enjoy the food with good people.'
        ], odd: 2, ex: '낯선 사람과 친구가 된다는 내용과 반대된다.' }
      ]},
      { type: 'blank', title: '빈칸추론', guide: '빈칸에 들어갈 말로 가장 알맞은 것을 고르세요.', items: [
        { s: 'These centers are so popular that ____.', opts: ['they are always full of people', 'nobody visits them', 'they close early', 'they sell only drinks'], ex: '인기가 많아 늘 사람들로 가득하다.' },
        { s: 'There are all kinds of food, ____.', opts: ['from Chinese noodles to Malaysian curry to Indonesian satay', 'but only Korean food', 'with no noodles', 'except curry'], ex: '여러 나라의 음식이 다 있다.' },
        { s: 'Sometimes, we share the tables with strangers and end up ____.', opts: ['becoming friends', 'fighting', 'leaving early', 'eating alone'], ex: '낯선 사람과 친구가 된다.' },
        { s: 'It is fun to enjoy the food with ____.', opts: ['good people', 'no one', 'angry people', 'my phone'], ex: '좋은 사람들과 함께 즐기는 것이 재미있다.' }
      ]},
      { type: 'mc', title: '핵심문법', guide: '알맞은 답을 고르세요.', items: [
        { q: '빈칸에 알맞은 것은?<br><b>______ you heard of hawker centers?</b>', opts: ['Have', 'Did', 'Are', 'Has'], ex: '현재완료 의문문: Have + 주어 + p.p.?' },
        { q: '대화의 빈칸에 알맞은 것은?<br><b>A: Have you heard of hawker centers?<br>B: Yes, I ______.</b>', opts: ['have', 'did', 'am', 'do'], ex: '현재완료 의문문의 대답: Yes, I have. / No, I haven\'t.' },
        { q: '빈칸에 알맞은 것은?<br><b>Hawkers are people ______ sell food on the street.</b>', opts: ['who', 'which', 'what', 'whose'], ex: '선행사가 사람, 주어 역할 → who' },
        { q: '빈칸에 알맞은 것은?<br><b>These centers are ______ popular that they are always full of people.</b>', opts: ['so', 'too', 'very', 'such'], ex: 'so + 형용사 + that: 너무 ~해서 …하다' },
        { q: '빈칸에 알맞은 것은?<br><b>We end up ______ friends.</b>', opts: ['becoming', 'become', 'to become', 'became'], ex: 'end up + -ing: 결국 ~하게 되다' },
        { q: '빈칸에 알맞은 것은?<br><b>It is fun ______ the food with good people.</b>', opts: ['to enjoy', 'enjoy', 'enjoys', 'enjoyed'], ex: '가주어 It ~ 진주어 to부정사' },
        { q: '"그게 내가 이 문화를 사랑하는 이유야."를 바르게 영작한 것은?', opts: ["That's why I love this culture.", "That's because I love this culture.", "That's what I love this culture.", "Why that's I love this culture."], ex: "That's why + 결과: 그래서 ~하다" },
        { q: '빈칸에 알맞은 것은?<br><b>The centers are always full ______ people.</b>', opts: ['of', 'with', 'by', 'at'], ex: 'be full of: ~로 가득 차다' },
        { q: '빈칸에 알맞은 것은?<br><b>all kinds of food, ______ Chinese noodles to Malaysian curry</b>', opts: ['from', 'between', 'since', 'for'], ex: 'from A to B: A부터 B까지' }
      ]}
    ]
  }
  ]
};
