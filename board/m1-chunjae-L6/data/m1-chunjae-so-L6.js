/* 중1 천재(소영순) Lesson 6 · Heroes in Nature (본문: Joys of Working in Nature)
   작성 규칙은 README.md 의 "데이터 작성 규칙".
   prose: true → 본문을 대사가 아닌 설명문으로 표시 */
window.PKG = {
  id: 'm1-chunjae-so-L6',
  school: '중1 천재(소영순)',
  unit: 'Lesson 6',
  title: 'Heroes in Nature',
  titleKo: '자연에서 일하는 즐거움',
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
  }
  ]
};
