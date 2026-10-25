/* 중1 천재(소영순) Lesson 6 · Heroes in Nature (본문: Joys of Working in Nature)
   작성 규칙은 README.md 의 "데이터 작성 규칙".
   prose: true → 본문을 대사가 아닌 설명문으로 표시 */
window.PKG = {
  id: 'm1-chunjae-so-L6',
  school: '중1 천재(소영순)',
  unit: 'Lesson 6~7',
  title: 'Heroes in Nature · Love for Art',
  titleKo: '자연에서 일하는 즐거움 · 예술에 대한 사랑',
  exam: '2학기 기말고사',
  prose: true,
  stepsBefore: ["핵심어휘·숙어", "어휘선택", "T/F 내용 확인", "어법선택", "동사변형", "오류찾기", "본문 스크램블", "문장순서", "문장삽입", "어색한 문장", "빈칸추론", "핵심문법"],   /* 일치·불일치 추가 전 단계 이름: 예전 기록을 새 단계에 맞추는 데 씀 */
  teacherPhone: '',            /* 결과 받을 번호. 예: '010-1234-5678' */

  days: [
  /* ═══════════════════════════ DAY 1 · 본문 ❶❷ ═══════════════════════════ */
  {
    id: 'd1', name: 'DAY 1', range: '본문 ❶❷', story: '자연에서 일하는 사람들 · 거제의 해녀, 나리',
    passage: [
      ['', '❶', ''],
      ['', 'Some people love to work in nature.', '어떤 사람들은 자연에서 일하는 것을 아주 좋아한다.'],
      ['', 'They work in the sea, mountains, or even in the Arctic.', '그들은 바다, 산, 심지어 북극에서도 일한다.'],
      ['', "Let's meet them and listen to their stories.", '그들을 만나 보고 그들의 이야기를 들어 보자.'],
      ['', '❷', ''],
      ['Nari', 'I am Nari.', '저는 나리입니다.'],
      ['', 'I am a haenyeo in Geoje.', '저는 거제의 해녀입니다.'],
      ['', 'I dive in the water and collect seafood.', '저는 물에 잠수해서 해산물을 채집합니다.'],
      ['', 'In the morning, I check the tide and the weather.', '아침에, 저는 조수와 날씨를 확인합니다.'],
      ['', 'I wear a diving suit and swimming glasses to work in the water.', '저는 물속에서 일하기 위해 잠수복을 입고 수경을 씁니다.'],
      ['', 'I love diving and spending time in the beautiful sea.', '저는 잠수하는 것과 아름다운 바다에서 시간을 보내는 것을 아주 좋아합니다.'],
      ['', "I don't collect too much seafood.", '저는 너무 많은 해산물을 채집하지 않습니다.'],
      ['', 'This is good for the ocean.', '이것이 바다에 좋습니다.'],
      ['', 'These days, I see a lot of trash in the water, so I pick up the trash.', '요즘은 물속에 쓰레기가 많이 보여서 쓰레기를 줍습니다.'],
      ['', 'I believe that we should care about the ocean.', '저는 우리가 바다에 신경을 써야 한다고 믿습니다.']
    ],
    steps: [
      { type: 'vocab', title: '핵심어휘·숙어', quizN: 15, items: [
        ['nature', '자연'], ['mountain', '산'], ['even', '심지어, ~조차'], ['Arctic', '북극; 북극의'],
        ['listen to', '~을 듣다'], ['story', '이야기'], ['haenyeo', '해녀'], ['dive', '잠수하다'],
        ['collect', '모으다, 채집하다'], ['seafood', '해산물'], ['check', '확인하다'], ['tide', '조수, 밀물과 썰물'],
        ['weather', '날씨'], ['wear', '입다, 쓰다, 착용하다'], ['diving suit', '잠수복'], ['swimming glasses', '수경'],
        ['spend time', '시간을 보내다'], ['too much', '너무 많은'], ['be good for', '~에 좋다'], ['ocean', '바다, 대양'],
        ['these days', '요즘'], ['a lot of', '많은'], ['trash', '쓰레기'], ['pick up', '~을 줍다'],
        ['believe', '믿다'], ['care about', '~에 신경 쓰다, 관심을 가지다']
      ]},
      { type: 'pick', title: '어휘선택', guide: '문맥에 맞는 낱말을 고르세요.', items: [
        { s: 'Some people love to work in {nature|future}.', ex: 'nature: 자연' },
        { s: 'They work in the sea, mountains, or {even|ever} in the Arctic.', ex: 'even: 심지어 (ever: 언젠가, 한 번이라도)' },
        { s: "Let's meet them and {listen|look} to their stories.", ex: 'listen to: ~을 듣다' },
        { s: 'I {dive|drive} in the water and collect seafood.', ex: 'dive: 잠수하다 (drive: 운전하다)' },
        { s: 'In the morning, I {check|change} the tide and the weather.', ex: 'check: 확인하다' },
        { s: 'I {wear|carry} a diving suit and swimming glasses to work in the water.', ex: 'wear: (옷·안경 등을) 입다, 쓰다' },
        { s: "I don't collect too much seafood. This is {good|bad} for the ocean.", ex: '해산물을 너무 많이 채집하지 않는 것은 바다에 좋다.' },
        { s: 'These days, I see a lot of trash in the water, so I {pick up|throw away} the trash.', ex: 'pick up: 줍다 (throw away: 버리다)' },
        { s: 'I believe that we should {care about|forget about} the ocean.', ex: 'care about: ~에 신경 쓰다' }
      ]},
      { type: 'tf', title: 'T/F 내용 확인', guide: '본문 내용과 일치하면 T, 다르면 F를 고르세요.', items: [
        ['Some people enjoy working in nature.', true, 'Some people love to work in nature.'],
        ['Nari is a haenyeo in Jeju.', false, '나리는 거제(Geoje)의 해녀다.'],
        ['Nari checks the tide and the weather in the morning.', true, 'In the morning, I check the tide and the weather.'],
        ['Nari wears a diving suit to work in the water.', true, '물속에서 일하기 위해 잠수복을 입는다.'],
        ['Nari collects as much seafood as she can.', false, '너무 많은 해산물을 채집하지 않는다.'],
        ['Nari sees a lot of trash in the water these days.', true, 'These days, I see a lot of trash in the water.'],
        ["Nari doesn't pick up the trash in the water.", false, '나리는 쓰레기를 줍는다(pick up the trash).'],
        ['Nari thinks we should care about the ocean.', true, 'I believe that we should care about the ocean.']
      ]},
      { type: 'mc', title: '일치·불일치', guide: "본문을 읽고 내용과 맞는지 확인해요. 틀린 선택지는 해설의 근거 문장과 비교해 보세요.", items: [
        { n: "❷", box: ["❷"], q: "나리에 관한 내용과 일치하지 <u>않는</u> 것은?", opts: ["Nari collects as much seafood as she can.", "Nari is a haenyeo in Geoje.", "Nari checks the tide and the weather in the morning.", "Nari wears a diving suit to work in the water.", "Nari picks up the trash in the water."], ex: "정답 근거: I don't collect too much seafood. (너무 많은 해산물을 채집하지 않는다)\n· as much ~ as she can : 할 수 있는 한 많이", per: [["나리는 할 수 있는 한 많은 해산물을 채집한다.", "I don't collect too much seafood", "불일치 → 너무 많이 채집하지 않음"], ["나리는 거제의 해녀이다.", "I am a haenyeo in Geoje", "일치"], ["나리는 아침에 조수와 날씨를 확인한다.", "In the morning, I check the tide and the weather", "일치"], ["나리는 물속에서 일하기 위해 잠수복을 입는다.", "I wear a diving suit", "일치"], ["나리는 물속의 쓰레기를 줍는다.", "so I pick up the trash", "일치"]] },
        { n: "❷", box: ["❶", "❷"], q: "글의 내용과 <u>일치하는</u> 것은?", opts: ["Nari thinks that we should care about the ocean.", "Some people work in the Arctic, but not in the sea.", "Nari dives in the water at night.", "Nari doesn't like spending time in the sea.", "There is no trash in the water these days."], ex: "정답 근거: I believe that we should care about the ocean.\n· care about : ~에 신경 쓰다, 관심을 가지다", per: [["나리는 우리가 바다에 신경 써야 한다고 생각한다.", "I believe that we should care about the ocean", "일치"], ["어떤 사람들은 북극에서 일하지만 바다에서는 일하지 않는다.", "They work in the sea, mountains, or even in the Arctic", "불일치 → 바다에서도 일함"], ["나리는 밤에 물에 잠수한다.", "In the morning, I check the tide", "불일치 → 밤이라는 말은 없음"], ["나리는 바다에서 시간 보내는 것을 좋아하지 않는다.", "I love diving and spending time in the beautiful sea", "불일치 → 아주 좋아함"], ["요즘 물속에는 쓰레기가 없다.", "I see a lot of trash in the water", "불일치 → 쓰레기가 많음"]] }
      ]},
      { type: 'pick', title: '어법선택', guide: '어법상 알맞은 것을 고르세요.', items: [
        { s: 'Some people love {to work|work} in nature.', ex: 'love + to부정사/동명사' },
        { s: "Let's meet them and {listen|listening} to their stories.", ex: "Let's + 동사원형 (meet and listen 병렬)" },
        { s: 'I am a haenyeo {in|on} Geoje.', ex: '지역·도시 이름 앞 → in' },
        { s: 'I dive in the water and {collect|collects} seafood.', ex: '주어 I → collect (dive와 병렬)' },
        { s: 'I wear a diving suit and swimming glasses {to work|working} in the water.', ex: '목적(~하기 위해) → to부정사' },
        { s: 'I love diving and {spending|spend} time in the beautiful sea.', ex: 'diving과 and로 연결 → spending' },
        { s: "I don't collect too {much|many} seafood.", ex: 'seafood는 셀 수 없는 명사 → much' },
        { s: 'These days, I see {a lot of|a few} trash in the water.', ex: 'trash는 셀 수 없는 명사 → a lot of (a few는 셀 수 있는 명사)' },
        { s: 'I believe {that|what} we should care about the ocean.', ex: '뒤에 완전한 문장 → 접속사 that' },
        { s: 'I believe that we should {care|cares} about the ocean.', ex: '조동사 should + 동사원형' }
      ]},
      { type: 'verb', title: '동사변형', guide: '( ) 안의 동사를 알맞은 형태로 바꿔 쓰세요.', items: [
        { s: 'Some people love ___ in nature.', v: 'work', a: ['to work', 'working'], ex: 'love + to부정사/동명사 (본문: to work)' },
        { s: 'They ___ in the sea, mountains, or even in the Arctic.', v: 'work', a: ['work'], ex: '주어 They → work' },
        { s: "Let's ___ them and listen to their stories.", v: 'meet', a: ['meet'], ex: "Let's + 동사원형" },
        { s: 'I ___ in the water and collect seafood.', v: 'dive', a: ['dive'], ex: '주어 I + 현재형' },
        { s: 'I wear a diving suit and swimming glasses ___ in the water.', v: 'work', a: ['to work'], ex: '목적(~하기 위해) → to work' },
        { s: 'I love ___ and spending time in the beautiful sea.', v: 'dive', a: ['diving'], ex: 'spending과 병렬 → diving' },
        { s: 'I love diving and ___ time in the beautiful sea.', v: 'spend', a: ['spending'], ex: 'diving과 병렬 → spending' },
        { s: "I don't ___ too much seafood.", v: 'collect', a: ['collect'], ex: "don't + 동사원형" },
        { s: 'This ___ good for the ocean.', v: 'be', a: ['is'], ex: '주어 This → is' },
        { s: 'I believe that we should ___ about the ocean.', v: 'care', a: ['care'], ex: 'should + 동사원형' }
      ]},
      { type: 'error', title: '오류찾기', guide: '어법상 틀린 곳을 고르세요.', items: [
        { s: 'Some people love [[work]] in nature. They [[work]] in the sea, mountains, or [[even]] [[in]] the Arctic.', w: 0, fix: 'to work', ex: 'love + to부정사/동명사 → to work (또는 working)' },
        { s: "Let's [[meet]] them and [[listening]] [[to]] [[their]] stories.", w: 1, fix: 'listen', ex: "Let's + 동사원형 → listen" },
        { s: 'I [[dive]] in the water and [[collects]] seafood. In the morning, I [[check]] the tide and [[the]] weather.', w: 1, fix: 'collect', ex: '주어 I → collect' },
        { s: 'I wear a diving suit and swimming glasses [[work]] [[in]] the water. I love [[diving]] and [[spending]] time in the beautiful sea.', w: 0, fix: 'to work', ex: '목적(~하기 위해) → to work' },
        { s: "I [[don't]] collect too [[many]] seafood. This [[is]] good [[for]] the ocean.", w: 1, fix: 'much', ex: 'seafood는 셀 수 없는 명사 → much' },
        { s: 'These days, I see [[a lot of]] trash in the water, so I [[pick up]] the trash. I believe [[what]] we should [[care]] about the ocean.', w: 2, fix: 'that', ex: '뒤에 완전한 문장 → 접속사 that' }
      ]},
      { type: 'scramble', title: '본문 스크램블', guide: '우리말에 맞게 단어를 눌러 문장을 완성하세요.', items: [
        { ko: '어떤 사람들은 자연에서 일하는 것을 아주 좋아한다.', en: 'Some people love to work in nature.' },
        { ko: '그들을 만나 보고 그들의 이야기를 들어 보자.', en: "Let's meet them and listen to their stories." },
        { ko: '저는 물에 잠수해서 해산물을 채집합니다.', en: 'I dive in the water and collect seafood.' },
        { ko: '저는 물속에서 일하기 위해 잠수복을 입고 수경을 씁니다.', en: 'I wear a diving suit and swimming glasses to work in the water.' },
        { ko: '저는 잠수하는 것과 아름다운 바다에서 시간을 보내는 것을 아주 좋아합니다.', en: 'I love diving and spending time in the beautiful sea.' },
        { ko: '저는 너무 많은 해산물을 채집하지 않습니다.', en: "I don't collect too much seafood." },
        { ko: '저는 우리가 바다에 신경을 써야 한다고 믿습니다.', en: 'I believe that we should care about the ocean.' }
      ]},
      { type: 'order', title: '문장순서', guide: '문장을 본문 순서대로 눌러서 배열하세요.', items: [
        { lines: [
          'Some people love to work in nature.',
          'They work in the sea, mountains, or even in the Arctic.',
          "Let's meet them and listen to their stories.",
          'I am Nari.'
        ]},
        { lines: [
          'I dive in the water and collect seafood.',
          'In the morning, I check the tide and the weather.',
          'I wear a diving suit and swimming glasses to work in the water.',
          'I love diving and spending time in the beautiful sea.'
        ]},
        { lines: [
          "I don't collect too much seafood.",
          'This is good for the ocean.',
          'These days, I see a lot of trash in the water, so I pick up the trash.',
          'I believe that we should care about the ocean.'
        ]}
      ]},
      { type: 'insert', title: '문장삽입', guide: '주어진 문장이 들어가기에 가장 알맞은 곳을 고르세요.', items: [
        { lines: [
          'Some people love to work in nature.',
          'They work in the sea, mountains, or even in the Arctic.',
          "Let's meet them and listen to their stories.",
          'I am Nari.',
          'I am a haenyeo in Geoje.'
        ], given: 1, ex: 'They는 앞 문장의 Some people을 가리킨다.' },
        { lines: [
          'I dive in the water and collect seafood.',
          'In the morning, I check the tide and the weather.',
          'I wear a diving suit and swimming glasses to work in the water.',
          'I love diving and spending time in the beautiful sea.',
          "I don't collect too much seafood."
        ], given: 2, ex: '아침에 조수와 날씨를 확인한 뒤, 물속에서 일하기 위해 잠수복을 입는다.' },
        { lines: [
          'I love diving and spending time in the beautiful sea.',
          "I don't collect too much seafood.",
          'This is good for the ocean.',
          'These days, I see a lot of trash in the water, so I pick up the trash.',
          'I believe that we should care about the ocean.'
        ], given: 2, ex: 'This는 "해산물을 너무 많이 채집하지 않는 것"을 가리킨다.' }
      ]},
      { type: 'odd', title: '어색한 문장', guide: '글의 흐름과 관계없는 문장을 고르세요.', items: [
        { lines: [
          'Some people love to work in nature.',
          'They work in the sea, mountains, or even in the Arctic.',
          "They don't like going outside at all.",
          "Let's meet them and listen to their stories."
        ], odd: 2, ex: '자연에서 일하는 것을 좋아하는 사람들인데 밖에 나가는 것을 싫어한다는 내용은 맞지 않는다.' },
        { lines: [
          'I dive in the water and collect seafood.',
          'In the morning, I check the tide and the weather.',
          'I wear a diving suit and swimming glasses to work in the water.',
          'I am afraid of the sea, so I never swim.',
          'I love diving and spending time in the beautiful sea.'
        ], odd: 3, ex: '나리는 잠수와 바다에서 시간 보내기를 아주 좋아한다.' },
        { lines: [
          "I don't collect too much seafood.",
          'This is good for the ocean.',
          'So I always collect as much seafood as I can.',
          'These days, I see a lot of trash in the water, so I pick up the trash.',
          'I believe that we should care about the ocean.'
        ], odd: 2, ex: '해산물을 너무 많이 채집하지 않는다는 앞 내용과 반대된다.' }
      ]},
      { type: 'blank', title: '빈칸추론', guide: '빈칸에 들어갈 말로 가장 알맞은 것을 고르세요.', items: [
        { s: 'I wear a diving suit and swimming glasses ____.', opts: ['to work in the water', 'to look nice', 'to sleep well', 'to go shopping'], ex: '물속에서 일하기 위해 잠수복과 수경을 착용한다.' },
        { s: 'I love diving and ____ in the beautiful sea.', opts: ['spending time', 'throwing trash', 'building houses', 'doing homework'], ex: '아름다운 바다에서 시간을 보내는 것을 좋아한다.' },
        { s: 'These days, I see a lot of trash in the water, so I ____.', opts: ['pick up the trash', 'throw more trash', 'stop diving', 'buy new glasses'], ex: '쓰레기가 많이 보여서 쓰레기를 줍는다.' },
        { s: "I don't collect too much seafood. This is good for the ocean. I believe that we should ____ the ocean.", opts: ['care about', 'take everything from', 'get away from', 'be afraid of'], ex: '바다를 아끼는 행동을 하므로 바다에 신경 써야 한다고 믿는다.' }
      ]},
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
      ]}
    ]
  },

  /* ═══════════════════════════ DAY 2 · 본문 ❸❹ ═══════════════════════════ */
  {
    id: 'd2', name: 'DAY 2', range: '본문 ❸❹', story: '지리산의 수의사, 지한 · 극지 과학자, 은',
    passage: [
      ['', '❸', ''],
      ['Jihan', 'My name is Jihan.', '제 이름은 지한입니다.'],
      ['', 'I am a vet at the wild animal care center in Jirisan.', '저는 지리산 야생 동물 보호 센터의 수의사입니다.'],
      ['', 'I take care of sick wild animals in the center and send them back to their homes.', '저는 센터의 아픈 야생 동물을 돌보고 그들을 집으로 돌려보냅니다.'],
      ['', 'Also, I often climb the mountain to look after wild animals like bears.', '또한 저는 곰과 같은 야생 동물을 돌보기 위해 자주 산을 오릅니다.'],
      ['', "I'm proud of my job.", '저는 제 직업이 자랑스럽습니다.'],
      ['', 'I think that protecting wild animals is important.', '저는 야생 동물을 보호하는 것이 중요하다고 생각합니다.'],
      ['', 'We should keep an eye on them and their homes to live together.', '우리는 함께 살아가기 위해 그들과 그들의 서식처를 계속 지켜보아야 합니다.'],
      ['', '❹', ''],
      ['Eun', 'My name is Eun, and I am an Arctic scientist.', '제 이름은 은이고, 저는 극지 과학자입니다.'],
      ['', 'I work at the Arctic Dasan Station in Norway.', '저는 노르웨이의 북극 다산 과학 기지에서 일합니다.'],
      ['', 'I study the soil, seawater, and ice in the Arctic.', '저는 북극의 토양, 바닷물, 얼음을 연구합니다.'],
      ['', 'I often travel on the special ship, Araon.', '저는 특별한 배인 아라온호를 타고 자주 이동합니다.'],
      ['', 'This ship is stronger than other ships.', '이 배는 다른 배보다 더 튼튼합니다.'],
      ['', 'It can break thick ice across the ocean.', '그것은 바다를 가로질러 두꺼운 얼음을 깰 수 있습니다.'],
      ['', 'Thanks to Araon, I can collect seawater samples.', '아라온호 덕분에 저는 바닷물 표본을 채집할 수 있습니다.'],
      ['', 'The Arctic Ocean has the answers to the climate crisis.', '북극해는 기후 위기에 대한 해답을 가지고 있습니다.'],
      ['', 'I hope that my work can help the Earth.', '저는 제 일이 지구를 도울 수 있기를 바랍니다.']
    ],
    steps: [
      { type: 'vocab', title: '핵심어휘·숙어', quizN: 15, items: [
        ['vet', '수의사'], ['wild animal', '야생 동물'], ['take care of', '~을 돌보다'], ['sick', '아픈'],
        ['send ~ back', '~을 돌려보내다'], ['often', '자주, 종종'], ['climb', '오르다'], ['look after', '~을 돌보다'],
        ['like (전치사)', '~와 같은, ~처럼'], ['bear', '곰'], ['be proud of', '~을 자랑스러워하다'], ['protect', '보호하다'],
        ['important', '중요한'], ['keep an eye on', '~을 계속 지켜보다'], ['together', '함께'], ['scientist', '과학자'],
        ['station', '기지; 역'], ['soil', '토양, 흙'], ['seawater', '바닷물'], ['travel', '이동하다; 여행하다'],
        ['special', '특별한'], ['strong', '튼튼한, 강한'], ['break', '깨다, 부수다'], ['thick', '두꺼운'],
        ['across', '~을 가로질러'], ['thanks to', '~ 덕분에'], ['sample', '표본, 샘플'], ['answer to', '~에 대한 해답'],
        ['climate crisis', '기후 위기'], ['hope', '바라다, 희망하다']
      ]},
      { type: 'pick', title: '어휘선택', guide: '문맥에 맞는 낱말을 고르세요.', items: [
        { s: 'I am a {vet|chef} at the wild animal care center in Jirisan.', ex: 'vet: 수의사' },
        { s: 'I take care of {sick|healthy} wild animals in the center and send them back to their homes.', ex: '센터에서 아픈(sick) 동물을 돌본다.' },
        { s: 'Also, I often {climb|cross} the mountain to look after wild animals like bears.', ex: 'climb the mountain: 산을 오르다' },
        { s: "I'm {proud|afraid} of my job.", ex: 'be proud of: ~을 자랑스러워하다' },
        { s: 'I think that {protecting|hunting} wild animals is important.', ex: 'protect: 보호하다' },
        { s: 'We should keep an {eye|ear} on them and their homes to live together.', ex: 'keep an eye on: ~을 계속 지켜보다' },
        { s: 'I study the {soil|sand}, seawater, and ice in the Arctic.', ex: 'soil: 토양, 흙' },
        { s: 'This ship is {stronger|weaker} than other ships.', ex: '두꺼운 얼음을 깰 수 있으므로 더 튼튼하다.' },
        { s: 'It can break {thick|thin} ice across the ocean.', ex: 'thick: 두꺼운 (thin: 얇은)' },
        { s: '{Thanks to|Instead of} Araon, I can collect seawater samples.', ex: 'thanks to: ~ 덕분에' },
        { s: 'The Arctic Ocean has the {answers|questions} to the climate crisis.', ex: 'answer to: ~에 대한 해답' }
      ]},
      { type: 'tf', title: 'T/F 내용 확인', guide: '본문 내용과 일치하면 T, 다르면 F를 고르세요.', items: [
        ['Jihan is a vet in Jirisan.', true, '지리산 야생 동물 보호 센터의 수의사다.'],
        ['Jihan sends the wild animals to a zoo.', false, '동물들을 그들의 집(서식처)으로 돌려보낸다.'],
        ['Jihan often climbs the mountain to look after wild animals.', true, 'I often climb the mountain to look after wild animals.'],
        ["Jihan thinks protecting wild animals isn't important.", false, '야생 동물 보호가 중요하다고 생각한다.'],
        ['Eun works at a station in Norway.', true, 'the Arctic Dasan Station in Norway'],
        ['Eun studies the soil, seawater, and ice in the Antarctic.', false, '남극(Antarctic)이 아니라 북극(Arctic)을 연구한다.'],
        ['Araon can break thick ice across the ocean.', true, 'It can break thick ice across the ocean.'],
        ['Eun hopes the work can help the Earth.', true, 'I hope that my work can help the Earth.']
      ]},
      { type: 'mc', title: '일치·불일치', guide: "본문을 읽고 내용과 맞는지 확인해요. 틀린 선택지는 해설의 근거 문장과 비교해 보세요.", items: [
        { n: "❸", box: ["❸"], q: "지한에 관한 내용과 일치하지 <u>않는</u> 것은?", opts: ["Jihan works at a zoo in Seoul.", "Jihan takes care of sick wild animals.", "Jihan sends the animals back to their homes.", "Jihan often climbs the mountain to look after bears.", "Jihan is proud of his job."], ex: "정답 근거: I am a vet at the wild animal care center in Jirisan.\n· vet : 수의사 · take care of = look after : 돌보다", per: [["지한은 서울의 동물원에서 일한다.", "I am a vet at the wild animal care center in Jirisan", "불일치 → 지리산 야생 동물 보호 센터"], ["지한은 아픈 야생 동물을 돌본다.", "I take care of sick wild animals", "일치"], ["지한은 동물들을 집으로 돌려보낸다.", "send them back to their homes", "일치"], ["지한은 곰을 돌보기 위해 자주 산에 오른다.", "I often climb the mountain to look after wild animals like bears", "일치"], ["지한은 자기 직업이 자랑스럽다.", "I'm proud of my job", "일치"]] },
        { n: "❹", box: ["❹"], q: "은에 관한 내용과 <u>일치하는</u> 것은?", opts: ["The ship Araon can break thick ice across the ocean.", "Eun works at a station in Canada.", "Eun studies animals and plants in the Arctic.", "Araon is weaker than other ships.", "Eun can't collect seawater samples."], ex: "정답 근거: It can break thick ice across the ocean.\n· thick : 두꺼운 · thanks to : ~ 덕분에 · sample : 표본", per: [["아라온호는 바다를 가로질러 두꺼운 얼음을 깰 수 있다.", "It can break thick ice across the ocean", "일치"], ["은은 캐나다의 기지에서 일한다.", "I work at the Arctic Dasan Station in Norway", "불일치 → 노르웨이"], ["은은 북극의 동물과 식물을 연구한다.", "I study the soil, seawater, and ice in the Arctic", "불일치 → 토양, 바닷물, 얼음"], ["아라온호는 다른 배보다 약하다.", "This ship is stronger than other ships", "불일치 → 더 튼튼함"], ["은은 바닷물 표본을 채집할 수 없다.", "Thanks to Araon, I can collect seawater samples", "불일치 → 채집할 수 있음"]] }
      ]},
      { type: 'pick', title: '어법선택', guide: '어법상 알맞은 것을 고르세요.', items: [
        { s: 'I am a vet {at|on} the wild animal care center in Jirisan.', ex: '건물·특정 장소 → at, 넓은 지역 → in' },
        { s: 'I take care of sick wild animals in the center and send {them back|back them} to their homes.', ex: '이어동사 목적어가 대명사 → 동사 + 대명사 + back' },
        { s: 'Also, I often climb the mountain {to look|looking} after wild animals like bears.', ex: '목적(~하기 위해) → to부정사' },
        { s: 'Also, I {often climb|climb often} the mountain.', ex: '빈도부사는 일반동사 앞에' },
        { s: "I'm proud {of|for} my job.", ex: 'be proud of: ~을 자랑스러워하다' },
        { s: 'I think that protecting wild animals {is|are} important.', ex: '동명사 주어는 단수 취급 → is' },
        { s: 'We should keep an eye on them and their homes {to live|live} together.', ex: '목적(~하기 위해) → to live' },
        { s: 'This ship is {stronger|strong} than other ships.', ex: 'than 앞 → 비교급 stronger' },
        { s: 'It can {break|breaks} thick ice across the ocean.', ex: '조동사 can + 동사원형' },
        { s: 'Thanks to Araon, I can {collect|collecting} seawater samples.', ex: '조동사 can + 동사원형' },
        { s: 'I hope {that|what} my work can help the Earth.', ex: '뒤에 완전한 문장 → 접속사 that' }
      ]},
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
      ]},
      { type: 'error', title: '오류찾기', guide: '어법상 틀린 곳을 고르세요.', items: [
        { s: 'I take care [[of]] sick wild animals in the center and send [[back them]] [[to]] [[their]] homes.', w: 1, fix: 'them back', ex: '이어동사 목적어가 대명사 → send them back' },
        { s: 'Also, I often [[climb]] the mountain [[looking]] after wild animals [[like]] [[bears]].', w: 1, fix: 'to look', ex: '목적(~하기 위해) → to look' },
        { s: "I'm proud [[of]] my job. I think [[that]] [[protecting]] wild animals [[are]] important.", w: 3, fix: 'is', ex: '동명사 주어는 단수 → is' },
        { s: 'We should [[keep]] an eye [[on]] them and their homes [[live]] [[together]].', w: 2, fix: 'to live', ex: '목적(~하기 위해) → to live' },
        { s: 'I work [[at]] the Arctic Dasan Station [[in]] Norway. I [[study]] the soil, seawater, and ice in the Arctic. I [[travel often]] on the special ship, Araon.', w: 3, fix: 'often travel', ex: '빈도부사는 일반동사 앞 → often travel' },
        { s: 'This ship is [[strong]] [[than]] other ships. It can [[break]] [[thick]] ice across the ocean.', w: 0, fix: 'stronger', ex: 'than 앞 → 비교급 stronger' },
        { s: 'Thanks to Araon, I can [[collects]] seawater samples. The Arctic Ocean [[has]] the answers [[to]] the climate crisis. I hope [[that]] my work can help the Earth.', w: 0, fix: 'collect', ex: 'can + 동사원형' }
      ]},
      { type: 'scramble', title: '본문 스크램블', guide: '우리말에 맞게 단어를 눌러 문장을 완성하세요.', items: [
        { ko: '저는 센터의 아픈 야생 동물을 돌보고 그들을 집으로 돌려보냅니다.', en: 'I take care of sick wild animals in the center and send them back to their homes.' },
        { ko: '또한 저는 곰과 같은 야생 동물을 돌보기 위해 자주 산을 오릅니다.', en: 'Also, I often climb the mountain to look after wild animals like bears.' },
        { ko: '저는 야생 동물을 보호하는 것이 중요하다고 생각합니다.', en: 'I think that protecting wild animals is important.' },
        { ko: '우리는 함께 살아가기 위해 그들과 그들의 서식처를 계속 지켜보아야 합니다.', en: 'We should keep an eye on them and their homes to live together.' },
        { ko: '이 배는 다른 배보다 더 튼튼합니다.', en: 'This ship is stronger than other ships.' },
        { ko: '아라온호 덕분에 저는 바닷물 표본을 채집할 수 있습니다.', en: 'Thanks to Araon, I can collect seawater samples.' },
        { ko: '북극해는 기후 위기에 대한 해답을 가지고 있습니다.', en: 'The Arctic Ocean has the answers to the climate crisis.' },
        { ko: '저는 제 일이 지구를 도울 수 있기를 바랍니다.', en: 'I hope that my work can help the Earth.' }
      ]},
      { type: 'order', title: '문장순서', guide: '문장을 본문 순서대로 눌러서 배열하세요.', items: [
        { lines: [
          'My name is Jihan.',
          'I am a vet at the wild animal care center in Jirisan.',
          'I take care of sick wild animals in the center and send them back to their homes.',
          'Also, I often climb the mountain to look after wild animals like bears.'
        ]},
        { lines: [
          "I'm proud of my job.",
          'I think that protecting wild animals is important.',
          'We should keep an eye on them and their homes to live together.',
          'My name is Eun, and I am an Arctic scientist.'
        ]},
        { lines: [
          'I work at the Arctic Dasan Station in Norway.',
          'I study the soil, seawater, and ice in the Arctic.',
          'I often travel on the special ship, Araon.',
          'This ship is stronger than other ships.'
        ]},
        { lines: [
          'It can break thick ice across the ocean.',
          'Thanks to Araon, I can collect seawater samples.',
          'The Arctic Ocean has the answers to the climate crisis.',
          'I hope that my work can help the Earth.'
        ]}
      ]},
      { type: 'insert', title: '문장삽입', guide: '주어진 문장이 들어가기에 가장 알맞은 곳을 고르세요.', items: [
        { lines: [
          'My name is Jihan.',
          'I am a vet at the wild animal care center in Jirisan.',
          'I take care of sick wild animals in the center and send them back to their homes.',
          'Also, I often climb the mountain to look after wild animals like bears.',
          "I'm proud of my job."
        ], given: 2, ex: 'the center는 앞 문장의 보호 센터를 가리키고, 뒤 문장의 Also는 하는 일을 하나 더 덧붙인다.' },
        { lines: [
          "I'm proud of my job.",
          'I think that protecting wild animals is important.',
          'We should keep an eye on them and their homes to live together.',
          'My name is Eun, and I am an Arctic scientist.'
        ], given: 2, ex: 'them은 앞 문장의 wild animals를 가리킨다.' },
        { lines: [
          'I study the soil, seawater, and ice in the Arctic.',
          'I often travel on the special ship, Araon.',
          'This ship is stronger than other ships.',
          'It can break thick ice across the ocean.',
          'Thanks to Araon, I can collect seawater samples.'
        ], given: 2, ex: 'This ship은 앞의 Araon을 가리키고, 뒤 문장의 It은 This ship을 가리킨다.' },
        { lines: [
          'This ship is stronger than other ships.',
          'It can break thick ice across the ocean.',
          'Thanks to Araon, I can collect seawater samples.',
          'The Arctic Ocean has the answers to the climate crisis.',
          'I hope that my work can help the Earth.'
        ], given: 2, ex: '얼음을 깰 수 있는 아라온호 덕분에 바닷물 표본을 채집할 수 있다.' }
      ]},
      { type: 'odd', title: '어색한 문장', guide: '글의 흐름과 관계없는 문장을 고르세요.', items: [
        { lines: [
          'I am a vet at the wild animal care center in Jirisan.',
          'I take care of sick wild animals in the center and send them back to their homes.',
          'I keep the animals in the center forever.',
          'Also, I often climb the mountain to look after wild animals like bears.',
          "I'm proud of my job."
        ], odd: 2, ex: '동물들을 집(서식처)으로 돌려보낸다는 내용과 반대된다.' },
        { lines: [
          "I'm proud of my job.",
          'I think that protecting wild animals is important.',
          "Wild animals don't need our help at all.",
          'We should keep an eye on them and their homes to live together.'
        ], odd: 2, ex: '야생 동물 보호가 중요하다는 흐름과 맞지 않는다.' },
        { lines: [
          'I work at the Arctic Dasan Station in Norway.',
          'I study the soil, seawater, and ice in the Arctic.',
          'I often travel on the special ship, Araon.',
          "Araon is a small ship, so it can't go through ice.",
          'This ship is stronger than other ships.',
          'It can break thick ice across the ocean.'
        ], odd: 3, ex: '아라온호는 다른 배보다 튼튼하고 두꺼운 얼음을 깰 수 있다.' },
        { lines: [
          'Thanks to Araon, I can collect seawater samples.',
          'The Arctic Ocean has the answers to the climate crisis.',
          'The climate crisis is not a problem for the Earth.',
          'I hope that my work can help the Earth.'
        ], odd: 2, ex: '기후 위기의 해답을 찾아 지구를 돕고 싶다는 흐름과 맞지 않는다.' }
      ]},
      { type: 'blank', title: '빈칸추론', guide: '빈칸에 들어갈 말로 가장 알맞은 것을 고르세요.', items: [
        { s: 'I take care of sick wild animals in the center and ____ to their homes.', opts: ['send them back', 'keep them all', 'sell them', 'hide them'], ex: '치료한 동물을 집(서식처)으로 돌려보낸다.' },
        { s: 'Also, I often climb the mountain ____ wild animals like bears.', opts: ['to look after', 'to hunt', 'to run away from', 'to sell'], ex: '곰 같은 야생 동물을 돌보기 위해 산을 오른다.' },
        { s: 'This ship is stronger than other ships. It can ____ across the ocean.', opts: ['break thick ice', 'sink easily', 'carry many cars', 'catch a lot of fish'], ex: '튼튼한 배라서 두꺼운 얼음을 깰 수 있다.' },
        { s: 'Thanks to Araon, I can collect seawater samples. The Arctic Ocean has the answers to ____.', opts: ['the climate crisis', 'the math test', 'the soccer game', 'the music class'], ex: '북극해는 기후 위기에 대한 해답을 가지고 있다.' }
      ]},
      { type: 'mc', title: '핵심문법', guide: '알맞은 답을 고르세요.', items: [
        { q: '빈칸에 알맞은 것은?<br><b>Protecting wild animals ______ important.</b>', opts: ['is', 'are', 'be', 'am'], ex: '동명사 주어는 단수 취급 → is' },
        { q: '밑줄 친 to부정사가 <b>"~하기 위해"</b>의 뜻이 <b>아닌</b> 것은?', opts: ['I want <u>to become</u> a vet.', 'I climb the mountain <u>to look</u> after bears.', 'We keep an eye on them <u>to live</u> together.', 'She went to the store <u>to buy</u> milk.'], ex: 'want to become은 want의 목적어(~하는 것). 나머지는 목적(~하기 위해).' },
        { q: '어법상 <b>틀린</b> 문장은?', opts: ['Please send back them.', 'Please send them back.', 'Please send the animals back.', 'Please send back the animals.'], ex: '목적어가 대명사이면 send them back 순서만 가능' },
        { q: '비교급 형태가 <b>틀린</b> 것은?', opts: ['important - importanter', 'thick - thicker', 'strong - stronger', 'big - bigger'], ex: '긴 형용사는 more를 쓴다: more important' },
        { q: '빈칸에 알맞은 것은?<br><b>This ship is stronger ______ other ships.</b>', opts: ['than', 'then', 'that', 'to'], ex: '비교급 + than: ~보다 더' },
        { q: '어법상 올바른 문장은?', opts: ['I often climb the mountain.', 'I climb often the mountain.', 'Often I climbs the mountain.', 'I often climbing the mountain.'], ex: '빈도부사는 일반동사 앞에' },
        { q: '빈칸에 알맞은 것은?<br><b>I hope ______ my work can help the Earth.</b>', opts: ['that', 'what', 'this', 'it'], ex: '완전한 문장을 이끄는 접속사 that' },
        { q: '빈칸에 알맞은 것은?<br><b>It can ______ thick ice across the ocean.</b>', opts: ['break', 'breaks', 'breaking', 'to break'], ex: 'can + 동사원형' },
        { q: '"나는 내 직업이 자랑스럽다."를 바르게 영작한 것은?', opts: ["I'm proud of my job.", "I'm proud my job.", 'I proud of my job.', "I'm proud for my job."], ex: 'be proud of: ~을 자랑스러워하다' }
      ]}
    ]
  },
  { id: 'd3', name: 'DAY 3', range: '7과 본문 ❶❷', story: 'Lesson 7 · Henri\'s Scissors · 화가가 된 소년 · 병에 걸린 Matisse', passage: [['', '❶', ''], ['', 'In a small town in France, there lived a young boy.', '프랑스의 작은 마을에 어린 소년이 살았다.'], ['', 'His name was Henri Matisse.', '그의 이름은 Henri Matisse였다.'], ['', 'He liked to draw pictures.', '그는 그림 그리는 것을 좋아했다.'], ['', 'He drew pictures in the sand and in his books.', '그는 모래와 그의 책에 그림을 그렸다.'], ['', 'When Matisse grew up, he left his town and became an artist in Paris.', 'Matisse가 어른이 되었을 때, 그는 마을을 떠나 파리에서 화가가 되었다.'], ['', 'He painted pictures day after day and year after year.', '그는 날마다, 해마다 그림을 그렸다.'], ['', 'He was happy with his life.', '그는 그의 삶에 행복해했다.'], ['', 'More and more people began to notice him.', '점점 더 많은 사람들이 그를 알아보기 시작했다.'], ['', 'They loved his paintings, and soon he became famous.', '그들은 그의 그림을 사랑했고 곧 그는 유명해졌다.'], ['', '❷', ''], ['', 'When Matisse became an old man, he fell ill.', 'Matisse가 노인이 되었을 때, 그는 병에 걸렸다.'], ['', 'He could only lie in bed and sleep.', '그는 침대에 누워 잠만 잘 수 있었다.'], ['', 'He couldn\'t paint at all.', '그는 그림을 전혀 그릴 수 없었다.'], ['', 'He could only paint in his dreams.', '그는 오직 그의 꿈속에서만 그릴 수 있었다.'], ['', 'When Matisse opened his eyes, they were full of sadness.', 'Matisse가 눈을 떴을 때, 그의 눈은 슬픔으로 가득 차 있었다.'], ['', 'Luckily, before long, he could sit.', '다행히도, 얼마 지나지 않아 그는 앉을 수 있었다.'], ['', 'A little later, he started to paint again.', '조금 후에, 그는 다시 그림을 그리기 시작했다.'], ['', 'However, he realized that he couldn\'t paint well anymore.', '하지만 그는 더 이상 그림을 잘 그릴 수 없다는 것을 깨달았다.']], steps: [
    { type: 'vocab', title: '핵심어휘·숙어', quizN: 15, items: [['scissors', '가위', '❶'], ['town', '마을, 읍', '❶'], ['young', '어린', '❶'], ['draw', '그리다 (과거 drew)', '❶'], ['picture', '그림', '❶'], ['sand', '모래', '❶'], ['grow up', '(성인으로) 자라다 (과거 grew up)', '❶'], ['leave', '떠나다 (과거 left)', '❶'], ['artist', '화가, 예술가', '❶'], ['day after day', '날마다, 매일매일', '❶'], ['year after year', '해마다, 매년', '❶'], ['be happy with', '~에 만족하다', '❶'], ['more and more', '점점 더 많은', '❶'], ['notice', '알아차리다, 주목하다', '❶'], ['famous', '유명한', '❶'], ['fall ill', '병에 걸리다 (과거 fell ill)', '❷'], ['lie', '누워 있다', '❷'], ['not ~ at all', '전혀 ~ 아니다', '❷'], ['dream', '꿈', '❷'], ['be full of', '~으로 가득 차다', '❷'], ['sadness', '슬픔', '❷'], ['luckily', '다행히도', '❷'], ['before long', '곧, 머지않아', '❷'], ['a little later', '잠시 후, 조금 있다가', '❷'], ['however', '그러나', '❷'], ['realize', '깨닫다', '❷'], ['not ~ anymore', '더 이상 ~않다', '❷']] },
    { type: 'pick', title: '어휘선택', guide: '문맥에 맞는 낱말을 고르세요.', items: [
      { s: 'In a small town in France, there lived a {young|old} boy.', ex: '어린 소년 → young (old 나이 든)' },
      { s: 'He drew pictures in the {sand|sky} and in his books.', ex: '모래에 그림을 그림 → sand' },
      { s: 'When Matisse grew up, he {left|stayed} his town and became an artist in Paris.', ex: '마을을 \'떠나\' 파리로 감 → left (stay 머무르다)' },
      { s: 'More and more people began to {notice|forget} him.', ex: '점점 많은 사람들이 \'알아보기\' 시작함 → notice' },
      { s: 'They loved his paintings, and soon he became {famous|poor}.', ex: '그림을 사랑함 → 곧 \'유명해짐\' famous' },
      { s: 'When Matisse became an old man, he fell {ill|asleep}.', ex: 'fall ill 병에 걸리다' },
      { s: 'When Matisse opened his eyes, they were full of {sadness|happiness}.', ex: '그림을 그릴 수 없었음 → 슬픔(sadness)' },
      { s: '{Luckily|Sadly}, before long, he could sit.', ex: '다시 앉을 수 있게 됨 → 다행히도(Luckily)' },
      { s: 'However, he {realized|forgot} that he couldn\'t paint well anymore.', ex: 'realize 깨닫다' }
    ] },
    { type: 'tf', title: 'T/F 내용 확인', guide: '본문 내용과 일치하면 T, 다르면 F를 고르세요.', items: [['Henri Matisse lived in a small town in France when he was young.', true, '프랑스의 작은 마을에 살던 어린 소년이었다.', '❶', 'In a small town in France, there lived a young boy'], ['Henri Matisse liked to write poems when he was a boy.', false, '시가 아니라 그림 그리는 것(to draw pictures)을 좋아했다.', '❶', 'He liked to draw pictures'], ['Matisse became an artist in his small town.', false, '마을을 떠나 파리(Paris)에서 화가가 되었다.', '❶', 'he left his town and became an artist in Paris'], ['Matisse painted pictures every day for many years.', true, '날마다, 해마다(day after day and year after year) 그렸다.', '❶', 'He painted pictures day after day and year after year'], ['More and more people loved Matisse\'s paintings.', true, '사람들이 그의 그림을 사랑했다.', '❶', 'They loved his paintings'], ['Matisse fell ill when he was a young artist.', false, '노인이 되었을 때(became an old man) 병에 걸렸다.', '❷', 'When Matisse became an old man, he fell ill'], ['Matisse\'s eyes were full of happiness when he opened them.', false, '슬픔(sadness)으로 가득 차 있었다.', '❷', 'they were full of sadness'], ['Matisse started to paint again, but he couldn\'t paint well anymore.', true, '다시 그리기 시작했지만 더 이상 잘 그릴 수 없었다.', '❷', 'he realized that he couldn\'t paint well anymore']] },
    { type: 'mc', title: '일치·불일치', guide: '선택지는 본문을 어려운 어휘로 바꿔 쓴 문장이에요. 풀고 나서 해설의 어휘를 꼭 확인하세요.', items: [
      { n: '❶', box: ['❶'], q: 'Henri Matisse에 관한 내용과 일치하지 <u>않는</u> 것은?', opts: ['He drew pictures only on paper when he was young.', 'He was born and grew up in a small town in France.', 'He moved to Paris and became an artist.', 'He was satisfied with his life as an artist.', 'He gradually gained fame as more people noticed him.'], ex: '정답 근거: He drew pictures in the sand and in his books. (종이에만 그린 게 아니라 모래와 책에 그림)\n· be satisfied with = be happy with ~에 만족하다 · gradually 점차 · gain fame 명성을 얻다', per: [['그는 어렸을 때 종이에만 그림을 그렸다.', 'He drew pictures in the sand and in his books', '불일치 → 모래와 책에 그림'], ['그는 프랑스의 작은 마을에서 자랐다.', 'In a small town in France, there lived a young boy', '일치'], ['그는 파리로 가서 화가가 되었다.', 'he left his town and became an artist in Paris', '일치 (move to 이사하다)'], ['그는 화가로서의 삶에 만족했다.', 'He was happy with his life', '일치 (be satisfied with = be happy with)'], ['더 많은 사람들이 알아보면서 그는 점차 유명해졌다.', 'More and more people began to notice him', '일치 (gain fame = become famous)']] },
      { n: '❷', box: ['❷'], q: '글의 내용과 <u>일치하는</u> 것은?', opts: ['When Matisse got sick, he could do nothing but stay in bed and sleep.', 'Matisse painted many pictures while he was in bed.', 'Matisse felt delighted when he woke up from his dreams.', 'Matisse could never sit again after he fell ill.', 'Matisse painted better than before when he started again.'], ex: '정답 근거: He could only lie in bed and sleep.\n· do nothing but ~ ~만 하다 · delighted 매우 기쁜 · fall ill = get sick 병에 걸리다', per: [['Matisse는 병에 걸렸을 때 침대에 누워 자는 것밖에 할 수 없었다.', 'He could only lie in bed and sleep', '일치 (do nothing but ~ = ~만 하다)'], ['Matisse는 침대에 있는 동안 많은 그림을 그렸다.', 'He couldn\'t paint at all', '불일치 → 전혀 그릴 수 없었음'], ['Matisse는 꿈에서 깼을 때 매우 기뻤다.', 'they were full of sadness', '불일치 → 슬픔으로 가득'], ['Matisse는 병에 걸린 뒤 다시는 앉을 수 없었다.', 'Luckily, before long, he could sit', '불일치 → 곧 앉을 수 있었음'], ['Matisse는 다시 그리기 시작했을 때 전보다 더 잘 그렸다.', 'he couldn\'t paint well anymore', '불일치 → 더 이상 잘 그릴 수 없었음']] }
    ] },
    { type: 'pick', title: '어법선택', guide: '어법상 알맞은 것을 고르세요.', items: [
      { s: 'In a small town in France, there {lived|living} a young boy.', ex: 'there + 동사 + 주어: ~가 살았다 → lived' },
      { s: 'He liked {to draw|draw} pictures.', ex: 'like + to부정사 (~하는 것을 좋아하다)' },
      { s: 'He {drew|drawed} pictures in the sand and in his books.', ex: 'draw - drew - drawn (불규칙)' },
      { s: 'When Matisse grew up, he left his town and {became|becomes} an artist in Paris.', ex: 'left(과거)와 병렬 → became' },
      { s: 'He was happy {with|to} his life.', ex: 'be happy with ~에 만족하다' },
      { s: 'More and more people began {to notice|noticed} him.', ex: 'begin + to부정사' },
      { s: 'They loved his paintings, and soon he became {famous|fame}.', ex: 'become + 형용사(보어) → famous' },
      { s: 'He could only lie in bed and {sleep|slept}.', ex: 'could + 동사원형 (lie와 병렬)' },
      { s: 'When Matisse opened his eyes, they were full {of|with} sadness.', ex: 'be full of ~으로 가득 차다' },
      { s: 'A little later, he started {to paint|painted} again.', ex: 'start + to부정사/동명사' },
      { s: 'However, he realized {that|what} he couldn\'t paint well anymore.', ex: 'realize + that절 (목적어)' }
    ] },
    { type: 'verb', title: '동사변형', guide: '( ) 안의 동사를 알맞은 형태로 바꿔 쓰세요.', items: [
      { s: 'He liked ___ pictures.', v: 'draw', a: ['to draw', 'drawing'], ex: 'like + to부정사/동명사 (본문: to draw)' },
      { s: 'He ___ pictures in the sand and in his books.', v: 'draw', a: ['drew'], ex: 'draw - drew - drawn (과거)' },
      { s: 'When Matisse ___ up, he left his town and became an artist in Paris.', v: 'grow', a: ['grew'], ex: 'grow - grew - grown (과거)' },
      { s: 'When Matisse grew up, he ___ his town and became an artist in Paris.', v: 'leave', a: ['left'], ex: 'leave - left - left (과거)' },
      { s: 'More and more people began ___ him.', v: 'notice', a: ['to notice', 'noticing'], ex: 'begin + to부정사/동명사 (본문: to notice)' },
      { s: 'When Matisse became an old man, he ___ ill.', v: 'fall', a: ['fell'], ex: 'fall - fell - fallen (과거)' },
      { s: 'He could only ___ in bed and sleep.', v: 'lie', a: ['lie'], ex: 'could + 동사원형' },
      { s: 'A little later, he started ___ again.', v: 'paint', a: ['to paint', 'painting'], ex: 'start + to부정사/동명사 (본문: to paint)' }
    ] },
    { type: 'error', title: '오류찾기', guide: '어법상 틀린 곳을 고르세요.', items: [
      { s: 'In a small town in France, there [[lived]] a young boy. He [[liked]] [[draw]] pictures. He drew pictures [[in]] the sand.', w: 2, fix: 'to draw', ex: 'like + to부정사 → to draw' },
      { s: 'When Matisse [[grew]] up, he left his town and [[become]] an artist [[in]] Paris. He was happy [[with]] his life.', w: 1, fix: 'became', ex: 'left(과거)와 병렬 → became' },
      { s: 'More and more people [[began]] [[to notice]] him. They [[loved]] his paintings, and soon he became [[fame]].', w: 3, fix: 'famous', ex: 'become + 형용사 → famous' },
      { s: 'When Matisse became an old man, he [[falled]] ill. He [[could]] only [[lie]] in bed and [[sleep]].', w: 0, fix: 'fell', ex: 'fall - fell - fallen' },
      { s: 'When Matisse [[opened]] his eyes, they were full [[with]] sadness. A little later, he started [[to paint]] [[again]].', w: 1, fix: 'of', ex: 'be full of ~으로 가득 차다' }
    ] },
    { type: 'scramble', title: '본문 스크램블', guide: '우리말에 맞게 단어를 눌러 문장을 완성하세요.', items: [
      { ko: '프랑스의 작은 마을에 어린 소년이 살았다.', en: 'In a small town in France, there lived a young boy.' },
      { ko: 'Matisse가 어른이 되었을 때, 그는 마을을 떠나 파리에서 화가가 되었다.', en: 'When Matisse grew up, he left his town and became an artist in Paris.' },
      { ko: '점점 더 많은 사람들이 그를 알아보기 시작했다.', en: 'More and more people began to notice him.' },
      { ko: 'Matisse가 노인이 되었을 때, 그는 병에 걸렸다.', en: 'When Matisse became an old man, he fell ill.' },
      { ko: 'Matisse가 눈을 떴을 때, 그의 눈은 슬픔으로 가득 차 있었다.', en: 'When Matisse opened his eyes, they were full of sadness.' },
      { ko: '하지만 그는 더 이상 그림을 잘 그릴 수 없다는 것을 깨달았다.', en: 'However, he realized that he couldn\'t paint well anymore.' }
    ] },
    { type: 'order', title: '문장순서', guide: '문장을 본문 순서대로 눌러서 배열하세요.', items: [
      { lines: ['In a small town in France, there lived a young boy.', 'His name was Henri Matisse.', 'He liked to draw pictures.', 'He drew pictures in the sand and in his books.'], flow: ['프랑스 작은 마을의 어린 소년', '그의 이름은 Henri Matisse', '그림 그리기를 좋아함', '모래와 책에 그림을 그림'] },
      { lines: ['When Matisse grew up, he left his town and became an artist in Paris.', 'He painted pictures day after day and year after year.', 'More and more people began to notice him.', 'They loved his paintings, and soon he became famous.'], flow: ['어른이 되어 파리에서 화가가 됨', '날마다, 해마다 그림을 그림', '점점 많은 사람들이 알아봄', '그림을 사랑했고 곧 유명해짐'] },
      { lines: ['When Matisse became an old man, he fell ill.', 'He could only lie in bed and sleep.', 'When Matisse opened his eyes, they were full of sadness.', 'Luckily, before long, he could sit.', 'However, he realized that he couldn\'t paint well anymore.'], flow: ['노인이 되어 병에 걸림', '침대에 누워 잠만 잘 수 있었음', '눈을 뜨면 슬픔으로 가득', '다행히 곧 앉을 수 있었음', '더 이상 잘 그릴 수 없다는 걸 깨달음'] }
    ] },
    { type: 'insert', title: '문장삽입', guide: '주어진 문장이 들어가기에 가장 알맞은 곳을 고르세요.', items: [
      { lines: ['His name was Henri Matisse.', 'He liked to draw pictures.', 'He drew pictures in the sand and in his books.'], given: 2, flow: ['그의 이름은 Henri Matisse', '그림 그리기를 좋아함', '모래와 책에 그림(pictures)을 그림'], ex: '그림 그리기를 좋아한다는 내용 뒤에 어디에 그렸는지가 이어진다.' },
      { lines: ['More and more people began to notice him.', 'They loved his paintings, and soon he became famous.', 'When Matisse became an old man, he fell ill.'], given: 1, flow: ['점점 많은 사람들이 그를 알아봄', '그들(They)은 그의 그림을 사랑했고 곧 유명해짐', '노인이 되어 병에 걸림'], ex: 'They는 앞 문장의 More and more people을 가리킨다.' },
      { lines: ['Luckily, before long, he could sit.', 'A little later, he started to paint again.', 'However, he realized that he couldn\'t paint well anymore.'], given: 2, flow: ['다행히 곧 앉을 수 있었음', '조금 후 다시 그림을 그리기 시작함', '하지만(However) 더 이상 잘 그릴 수 없었음'], ex: 'However는 \'다시 그리기 시작했다\'는 내용과 반대되는 결과를 이끈다.' }
    ] },
    { type: 'odd', title: '어색한 문장', guide: '글의 흐름과 관계없는 문장을 고르세요.', items: [
      { lines: ['He liked to draw pictures.', 'He drew pictures in the sand and in his books.', 'He didn\'t like drawing at all.', 'When Matisse grew up, he left his town and became an artist in Paris.'], odd: 2, ex: '그림 그리기를 싫어했다 → 그림을 좋아했다는 내용과 반대' },
      { lines: ['He was happy with his life.', 'More and more people began to notice him.', 'Nobody wanted to see his paintings.', 'They loved his paintings, and soon he became famous.'], odd: 2, ex: '아무도 그의 그림을 원하지 않았다 → 점점 유명해졌다는 흐름과 반대' },
      { lines: ['He couldn\'t paint at all.', 'He could only paint in his dreams.', 'He went to the park and painted every day.', 'When Matisse opened his eyes, they were full of sadness.'], odd: 2, ex: '공원에 가서 매일 그렸다 → 침대에 누워 그릴 수 없었다는 내용과 맞지 않음' }
    ] },
    { type: 'blank', title: '빈칸추론', guide: '빈칸에 들어갈 말로 가장 알맞은 것을 고르세요.', items: [
      { s: 'When Matisse grew up, he left his town and became ____ in Paris.', opts: ['an artist', 'a doctor', 'a teacher', 'a farmer'], ex: '파리에서 화가가 됨' },
      { s: 'He couldn\'t paint at all. He could only paint ____.', opts: ['in his dreams', 'in the park', 'in his school', 'with his friends'], ex: '병에 걸려 꿈속에서만 그릴 수 있었음' },
      { s: 'A little later, he started to paint again. However, he realized that ____.', opts: ['he couldn\'t paint well anymore', 'he was a great painter', 'he wanted to sleep', 'he became famous'], ex: 'However → 다시 그렸지만 잘 그릴 수 없었음' }
    ] },
    { type: 'mc', title: '핵심문법', guide: '알맞은 답을 고르세요.', items: [
      { q: '우리말과 같도록 할 때 빈칸에 알맞은 것은?<br>마을에 어린 소년이 살았다.<br><b>In a town, ______ lived a young boy.</b>', opts: ['there', 'it', 'he', 'they'], ex: 'there + 동사 + 주어: ~가 살았다 (there는 해석하지 않음)' },
      { q: '다음 중 어법상 <b>틀린</b> 문장은?', opts: ['He liked draw pictures.', 'He liked to draw pictures.', 'He liked drawing pictures.', 'He began to paint.'], ex: 'like는 to부정사나 동명사를 목적어로 → to draw / drawing' },
      { q: '빈칸에 알맞은 것은?<br><b>When Matisse ______ up, he became an artist.</b>', opts: ['grew', 'grow', 'grows', 'growing'], ex: '과거의 일 → grew (grow - grew - grown)' },
      { q: '밑줄 친 <b>When</b>의 뜻으로 알맞은 것은?<br><b><u>When</u> Matisse opened his eyes, they were full of sadness.</b>', opts: ['~할 때', '언제', '어디서', '왜'], ex: '접속사 when: ~할 때 (시간의 부사절)' },
      { q: '빈칸에 알맞은 것은?<br><b>Soon he became ______.</b>', opts: ['famous', 'fame', 'famously', 'more famous than'], ex: 'become + 형용사(보어)' },
      { q: '두 문장의 뜻이 같도록 할 때 빈칸에 알맞은 것은?<br><b>He could only lie in bed.<br>= He was only ______ to lie in bed.</b>', opts: ['able', 'can', 'could', 'ability'], ex: 'could = was/were able to' },
      { q: '우리말과 같도록 할 때 빈칸에 알맞은 것은?<br>그는 더 이상 그림을 잘 그릴 수 없었다.<br><b>He couldn\'t paint well ______.</b>', opts: ['anymore', 'at all', 'again', 'already'], ex: 'not ~ anymore 더 이상 ~않다' }
    ] }
  ] },
  { id: 'd4', name: 'DAY 4', range: '7과 본문 ❸❹', story: 'Lesson 7 · 가위로 그리는 그림 · 종이 정원과 밤하늘의 별', passage: [['', '❸', ''], ['', 'One day, Matisse got a brilliant idea.', '어느 날, Matisse는 멋진 생각을 해냈다.'], ['', 'He picked up scissors, cut some paper, and made beautiful shapes.', '그는 가위를 집어 들어 종이를 자르고, 아름다운 모양을 만들었다.'], ['', 'He cut out birds and flowers.', '그는 새와 꽃을 잘라 냈다.'], ['', 'He was drawing with SCISSORS!', '그는 가위로 그림을 그리고 있었다!'], ['', 'He said to himself, "My pleasure in cutting things grows and grows.', '그는 자기 자신에게 말했다. “무엇인가를 오려 내는 나의 기쁨이 더욱 커지고 있어.'], ['', 'Scissors gave me another chance."', '가위는 내게 또 다른 기회를 주었어.”'], ['', 'Matisse cut paper all day.', 'Matisse는 하루 종일 종이를 잘랐다.'], ['', '❹', ''], ['', 'Soon his room was full of shapes and colors.', '곧 그의 방은 모양과 색채로 가득 찼다.'], ['', '"I stay in bed most of the time, but I made a small paper garden all around me.', '“나는 대부분 시간을 침대에 머물러 있지만, 온 주변에 작은 종이 정원을 만들었어.'], ['', 'There are leaves, fruits, and birds ... I am really happy," he thought.', '나뭇잎, 과일, 그리고 새들이 있지 … 난 정말 행복해.”라고 그는 생각했다.'], ['', 'Perhaps Matisse is still using scissors to cut out stars in heaven.', '아마도 Matisse는 여전히 천국에서 별을 오리기 위해 가위를 사용하고 있을 것이다.'], ['', 'Look at the night sky.', '밤하늘을 봐.'], ['', 'Some of the stars may come from his scissors.', '별들 중 일부는 그의 가위에서 나온 것일지도 모른다.']], steps: [
    { type: 'vocab', title: '핵심어휘·숙어', quizN: 15, items: [['get an idea', '생각이 나다 (과거 got)', '❸'], ['brilliant', '멋진, 훌륭한', '❸'], ['pick ~ up', '~을 집어 들다', '❸'], ['cut', '자르다 (과거 cut)', '❸'], ['beautiful', '아름다운', '❸'], ['shape', '모양', '❸'], ['cut ~ out', '~을 오려내다', '❸'], ['say to oneself', '혼잣말을 하다, 마음속으로 생각하다', '❸'], ['pleasure', '기쁨, 즐거움', '❸'], ['grow and grow', '점점 더 커지다', '❸'], ['another', '또 다른', '❸'], ['chance', '기회', '❸'], ['all day', '하루 종일', '❸'], ['color', '색, 색채', '❹'], ['stay', '머무르다', '❹'], ['most of the time', '대부분의 시간', '❹'], ['garden', '정원', '❹'], ['all around ~', '~의 주변 일대에', '❹'], ['leaf', '잎, 나뭇잎 (복수 leaves)', '❹'], ['fruit', '과일', '❹'], ['perhaps', '아마, 어쩌면', '❹'], ['still', '아직도, 여전히', '❹'], ['heaven', '천국', '❹'], ['night sky', '밤하늘', '❹'], ['some of ~', '~ 중 일부', '❹'], ['come from', '~에서 나오다', '❹']] },
    { type: 'pick', title: '어휘선택', guide: '문맥에 맞는 낱말을 고르세요.', items: [
      { s: 'One day, Matisse got a {brilliant|terrible} idea.', ex: '멋진 생각 → brilliant' },
      { s: 'He {picked|put} up scissors, cut some paper, and made beautiful shapes.', ex: 'pick ~ up ~을 집어 들다' },
      { s: 'He cut {out|off} birds and flowers.', ex: 'cut ~ out ~을 오려내다' },
      { s: 'He said to himself, "My {pleasure|pain} in cutting things grows and grows.', ex: '오려 내는 \'기쁨\'이 커짐 → pleasure' },
      { s: 'Scissors gave me another {chance|problem}.', ex: '또 다른 \'기회\' → chance' },
      { s: 'Soon his room was full of {shapes|books} and colors.', ex: '오려 낸 \'모양\'과 색채로 가득 → shapes' },
      { s: 'I {stay|work} in bed most of the time, but I made a small paper garden all around me.', ex: '대부분 침대에 \'머물러\' 있음 → stay' },
      { s: '{Perhaps|Never} Matisse is still using scissors to cut out stars in heaven.', ex: '아마도 → Perhaps' },
      { s: 'Some of the stars may {come|go} from his scissors.', ex: 'come from ~에서 나오다' }
    ] },
    { type: 'tf', title: 'T/F 내용 확인', guide: '본문 내용과 일치하면 T, 다르면 F를 고르세요.', items: [['Matisse got a brilliant idea one day.', true, '어느 날 멋진 생각을 해냈다.', '❸', 'One day, Matisse got a brilliant idea'], ['Matisse put down scissors and picked up brushes again.', false, '가위를 집어 들었다(picked up scissors).', '❸', 'He picked up scissors'], ['Matisse made shapes of birds and flowers with scissors.', true, '새와 꽃을 오려 냈다.', '❸', 'He cut out birds and flowers'], ['Matisse felt happy when he cut things out.', true, '오려 내는 기쁨이 점점 커졌다.', '❸', 'My pleasure in cutting things grows and grows'], ['Matisse cut paper for only an hour a day.', false, '하루 종일(all day) 종이를 잘랐다.', '❸', 'Matisse cut paper all day'], ['Matisse was in his garden all day.', false, '대부분 침대에 머물렀다(stay in bed).', '❹', 'I stay in bed most of the time'], ['Matisse made a paper garden near his bed.', true, '온 주변에 작은 종이 정원을 만들었다.', '❹', 'I made a small paper garden all around me'], ['Maybe Matisse is still painting with brushes in heaven.', false, '붓이 아니라 가위로 별을 오리고 있을 것이다.', '❹', 'Perhaps Matisse is still using scissors to cut out stars in heaven']] },
    { type: 'mc', title: '일치·불일치', guide: '선택지는 본문을 어려운 어휘로 바꿔 쓴 문장이에요. 풀고 나서 해설의 어휘를 꼭 확인하세요.', items: [
      { n: '❸', box: ['❸'], q: 'Matisse에 관한 내용과 일치하지 <u>않는</u> 것은?', opts: ['He used scissors only for a short time each day.', 'He came up with a creative idea.', 'He made beautiful shapes out of paper.', 'He thought scissors gave him a new opportunity.', 'His joy kept growing as he cut things out.'], ex: '정답 근거: Matisse cut paper all day. (짧은 시간이 아니라 하루 종일)\n· come up with ~을 생각해 내다 · opportunity = chance 기회 · creative 창의적인', per: [['그는 하루에 잠깐씩만 가위를 사용했다.', 'Matisse cut paper all day', '불일치 → 하루 종일'], ['그는 창의적인 생각을 해냈다.', 'One day, Matisse got a brilliant idea', '일치 (come up with = get an idea)'], ['그는 종이로 아름다운 모양을 만들었다.', 'cut some paper, and made beautiful shapes', '일치'], ['그는 가위가 새로운 기회를 주었다고 생각했다.', 'Scissors gave me another chance', '일치 (opportunity = chance)'], ['무엇인가를 오려 낼수록 그의 기쁨이 계속 커졌다.', 'My pleasure in cutting things grows and grows', '일치']] },
      { n: '❹', box: ['❹'], q: '글의 내용과 <u>일치하는</u> 것은?', opts: ['Matisse created a garden of paper around his bed.', 'Matisse\'s room was empty and dark.', 'Matisse went outside to pick leaves and fruits.', 'Matisse felt lonely in his small room.', 'The writer says all the stars came from Matisse\'s scissors.'], ex: '정답 근거: I made a small paper garden all around me.\n· create 만들다 · empty 텅 빈 · lonely 외로운', per: [['Matisse는 침대 주변에 종이 정원을 만들었다.', 'I made a small paper garden all around me', '일치 (create = make)'], ['Matisse의 방은 텅 비고 어두웠다.', 'Soon his room was full of shapes and colors', '불일치 → 모양과 색채로 가득'], ['Matisse는 밖에 나가 나뭇잎과 과일을 따 왔다.', 'I stay in bed most of the time', '불일치 → 대부분 침대에 머묾 (종이로 만든 것)'], ['Matisse는 작은 방에서 외로웠다.', 'I am really happy', '불일치 → 정말 행복함'], ['글쓴이는 모든 별이 Matisse의 가위에서 나왔다고 말한다.', 'Some of the stars may come from his scissors', '불일치 → 일부(Some)가 나왔을지도 모름']] }
    ] },
    { type: 'pick', title: '어법선택', guide: '어법상 알맞은 것을 고르세요.', items: [
      { s: 'He picked up scissors, cut some paper, and {made|make} beautiful shapes.', ex: 'picked, cut과 병렬 → 과거 made' },
      { s: 'He {was|is} drawing with SCISSORS!', ex: '과거진행형 was + -ing' },
      { s: 'He said to {himself|him}, "My pleasure in cutting things grows and grows.', ex: '주어 He = 말하는 대상 → 재귀대명사 himself' },
      { s: 'My pleasure in {cutting|cut} things grows and grows.', ex: '전치사 in + 동명사' },
      { s: 'My pleasure in cutting things {grows|grow} and grows.', ex: '주어 My pleasure(단수) → grows' },
      { s: 'Scissors gave {me|to me} another chance.', ex: 'give + 간접목적어 + 직접목적어' },
      { s: 'Soon his room was full {of|with} shapes and colors.', ex: 'be full of ~으로 가득 차다' },
      { s: 'There {are|is} leaves, fruits, and birds ...', ex: 'There + be동사 + 복수 주어 → are' },
      { s: 'Perhaps Matisse is still using scissors {to cut|cut} out stars in heaven.', ex: '목적(~하기 위해) → to부정사' },
      { s: 'Some of the stars may {come|comes} from his scissors.', ex: '조동사 may + 동사원형' }
    ] },
    { type: 'verb', title: '동사변형', guide: '( ) 안의 동사를 알맞은 형태로 바꿔 쓰세요.', items: [
      { s: 'One day, Matisse ___ a brilliant idea.', v: 'get', a: ['got'], ex: 'get - got - got(ten) (과거)' },
      { s: 'He picked up scissors, ___ some paper, and made beautiful shapes.', v: 'cut', a: ['cut'], ex: 'cut - cut - cut (과거도 cut)' },
      { s: 'He was ___ with SCISSORS!', v: 'draw', a: ['drawing'], ex: '과거진행형 was + -ing' },
      { s: 'My pleasure in ___ things grows and grows.', v: 'cut', a: ['cutting'], ex: '전치사 in + 동명사 (t 겹쳐 쓰기)' },
      { s: 'Scissors ___ me another chance.', v: 'give', a: ['gave'], ex: 'give - gave - given (과거)' },
      { s: 'I stay in bed most of the time, but I ___ a small paper garden all around me.', v: 'make', a: ['made'], ex: 'make - made - made (과거)' },
      { s: 'Perhaps Matisse is still ___ scissors to cut out stars in heaven.', v: 'use', a: ['using'], ex: '현재진행형 is + -ing' },
      { s: 'Some of the stars may ___ from his scissors.', v: 'come', a: ['come'], ex: 'may + 동사원형' }
    ] },
    { type: 'error', title: '오류찾기', guide: '어법상 틀린 곳을 고르세요.', items: [
      { s: 'He [[picked]] up scissors, [[cut]] some paper, and [[make]] beautiful [[shapes]].', w: 2, fix: 'made', ex: 'picked, cut과 병렬 → 과거 made' },
      { s: 'He said to [[him]], "My pleasure [[in]] [[cutting]] things grows and [[grows]].', w: 0, fix: 'himself', ex: '주어와 같은 대상 → 재귀대명사 himself' },
      { s: 'My pleasure in cutting things [[grow]] and grows. Scissors [[gave]] [[me]] another [[chance]].', w: 0, fix: 'grows', ex: '주어 My pleasure(단수) → grows' },
      { s: 'Soon his room [[was]] full of shapes and colors. There [[is]] leaves, fruits, and [[birds]] ... I am [[really]] happy.', w: 1, fix: 'are', ex: '복수 주어(leaves, fruits, and birds) → are' },
      { s: 'Perhaps Matisse [[is]] still using scissors [[to cut]] out stars. Some of the stars may [[comes]] [[from]] his scissors.', w: 2, fix: 'come', ex: 'may + 동사원형 → come' }
    ] },
    { type: 'scramble', title: '본문 스크램블', guide: '우리말에 맞게 단어를 눌러 문장을 완성하세요.', items: [
      { ko: '어느 날, Matisse는 멋진 생각을 해냈다.', en: 'One day, Matisse got a brilliant idea.' },
      { ko: '그는 가위를 집어 들어 종이를 자르고, 아름다운 모양을 만들었다.', en: 'He picked up scissors, cut some paper, and made beautiful shapes.' },
      { ko: 'Matisse는 하루 종일 종이를 잘랐다.', en: 'Matisse cut paper all day.' },
      { ko: '곧 그의 방은 모양과 색채로 가득 찼다.', en: 'Soon his room was full of shapes and colors.' },
      { ko: '아마도 Matisse는 여전히 천국에서 별을 오리기 위해 가위를 사용하고 있을 것이다.', en: 'Perhaps Matisse is still using scissors to cut out stars in heaven.' },
      { ko: '별들 중 일부는 그의 가위에서 나온 것일지도 모른다.', en: 'Some of the stars may come from his scissors.' }
    ] },
    { type: 'order', title: '문장순서', guide: '문장을 본문 순서대로 눌러서 배열하세요.', items: [
      { lines: ['One day, Matisse got a brilliant idea.', 'He picked up scissors, cut some paper, and made beautiful shapes.', 'He cut out birds and flowers.', 'He was drawing with SCISSORS!'], flow: ['어느 날 멋진 생각을 해냄', '가위를 집어 종이를 잘라 모양을 만듦', '새와 꽃을 오려 냄', '가위로 그림을 그리고 있었음!'] },
      { lines: ['He said to himself, "My pleasure in cutting things grows and grows.', 'Scissors gave me another chance."', 'Matisse cut paper all day.', 'Soon his room was full of shapes and colors.'], flow: ['오려 내는 기쁨이 점점 커짐', '가위가 또 다른 기회를 줌', '하루 종일 종이를 자름', '곧 방이 모양과 색채로 가득 참'] },
      { lines: ['Perhaps Matisse is still using scissors to cut out stars in heaven.', 'Look at the night sky.', 'Some of the stars may come from his scissors.'], flow: ['아마 천국에서도 가위로 별을 오리고 있을 것', '밤하늘을 봐', '별 중 일부는 그의 가위에서 나왔을지도'] }
    ] },
    { type: 'insert', title: '문장삽입', guide: '주어진 문장이 들어가기에 가장 알맞은 곳을 고르세요.', items: [
      { lines: ['He picked up scissors, cut some paper, and made beautiful shapes.', 'He cut out birds and flowers.', 'He was drawing with SCISSORS!'], given: 2, flow: ['가위로 종이를 잘라 모양을 만듦', '새와 꽃을 오려 냄', '가위로 그림을 그리고 있었음!'], ex: '새와 꽃을 오려 낸 것을 \'가위로 그리고 있었다\'고 표현한다.' },
      { lines: ['Matisse cut paper all day.', 'Soon his room was full of shapes and colors.', '"I stay in bed most of the time, but I made a small paper garden all around me.'], given: 1, flow: ['하루 종일 종이를 자름', '곧(Soon) 방이 모양과 색채로 가득 참', '침대에 있지만 종이 정원을 만들었다'], ex: '하루 종일 자른 결과 곧 방이 모양으로 가득 찼다.' },
      { lines: ['Perhaps Matisse is still using scissors to cut out stars in heaven.', 'Look at the night sky.', 'Some of the stars may come from his scissors.'], given: 2, flow: ['천국에서 가위로 별을 오리고 있을 것', '밤하늘을 봐', '별들(the stars) 중 일부는 그의 가위에서'], ex: '밤하늘을 보라는 말 뒤에 별 이야기가 이어진다.' }
    ] },
    { type: 'odd', title: '어색한 문장', guide: '글의 흐름과 관계없는 문장을 고르세요.', items: [
      { lines: ['He picked up scissors, cut some paper, and made beautiful shapes.', 'He cut out birds and flowers.', 'He didn\'t like using scissors at all.', 'He was drawing with SCISSORS!'], odd: 2, ex: '가위 쓰기를 싫어했다 → 가위로 그림을 그렸다는 내용과 반대' },
      { lines: ['He said to himself, "My pleasure in cutting things grows and grows.', 'Scissors gave me another chance."', 'He threw away the scissors and went to sleep.', 'Matisse cut paper all day.'], odd: 2, ex: '가위를 버리고 잤다 → 하루 종일 종이를 잘랐다는 흐름과 맞지 않음' },
      { lines: ['Soon his room was full of shapes and colors.', '"I stay in bed most of the time, but I made a small paper garden all around me.', 'He was very sad because his room was empty.', 'There are leaves, fruits, and birds ... I am really happy," he thought.'], odd: 2, ex: '방이 비어 슬펐다 → 모양과 색채로 가득 차 행복했다는 내용과 반대' }
    ] },
    { type: 'blank', title: '빈칸추론', guide: '빈칸에 들어갈 말로 가장 알맞은 것을 고르세요.', items: [
      { s: 'He picked up scissors, cut some paper, and made ____.', opts: ['beautiful shapes', 'a big cake', 'a new bed', 'a loud sound'], ex: '가위로 종이를 잘라 아름다운 모양을 만듦' },
      { s: 'Scissors gave me ____.', opts: ['another chance', 'a big problem', 'a lot of money', 'a bad dream'], ex: '가위가 또 다른 기회를 줌' },
      { s: 'Perhaps Matisse is still using scissors to cut out ____ in heaven.', opts: ['stars', 'flowers', 'birds', 'leaves'], ex: '밤하늘의 별 → stars' }
    ] },
    { type: 'mc', title: '핵심문법', guide: '알맞은 답을 고르세요.', items: [
      { q: '빈칸에 알맞은 것은?<br><b>He said to ______, "I am happy."</b>', opts: ['himself', 'him', 'his', 'he'], ex: '주어(He)와 같은 대상 → 재귀대명사 himself' },
      { q: '두 문장의 뜻이 같도록 할 때 빈칸에 알맞은 것은?<br><b>Scissors gave me another chance.<br>= Scissors gave another chance ______ me.</b>', opts: ['to', 'for', 'of', 'with'], ex: 'give는 3형식 전환 시 전치사 to' },
      { q: '빈칸에 알맞은 것은?<br><b>There ______ leaves, fruits, and birds.</b>', opts: ['are', 'is', 'be', 'was'], ex: 'There + be동사 + 복수 주어 → are' },
      { q: '밑줄 친 부분과 쓰임이 <b>같은</b> 것은?<br><b>He is using scissors <u>to cut</u> out stars.</b>', opts: ['She went to the shop <u>to buy</u> paper.', 'I want <u>to buy</u> paper.', 'My plan is <u>to buy</u> paper.', 'He liked <u>to buy</u> paper.'], ex: '목적(~하기 위해)의 부사적 용법' },
      { q: '밑줄 친 <b>may</b>의 뜻으로 알맞은 것은?<br><b>Some of the stars <u>may</u> come from his scissors.</b>', opts: ['~일지도 모른다', '~해야 한다', '~할 수 있었다', '~하지 않았다'], ex: 'may: ~일지도 모른다 (추측)' },
      { q: '다음 중 어법상 <b>틀린</b> 문장은?', opts: ['He picked up them.', 'He picked them up.', 'He picked up scissors.', 'He picked scissors up.'], ex: '목적어가 대명사면 동사 + 대명사 + 부사 → picked them up' },
      { q: '빈칸에 알맞은 것은?<br><b>My pleasure in ______ things grows and grows.</b>', opts: ['cutting', 'cut', 'to cut', 'cuts'], ex: '전치사 in 뒤 → 동명사 cutting' }
    ] }
  ] }
  ]
};
