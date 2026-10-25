/* 중3 지학사(민찬규) Lesson 7 · Homes Everywhere (본문: If I Lived There)
   작성 규칙은 README.md 의 "데이터 작성 규칙". insert: given = 빠지는 문장 번호(0부터), odd = 어색한 문장 번호 */
window.PKG = {
  id: 'm3-jihak-min-L7',
  school: '중3 지학사(민찬규)',
  unit: 'Lesson 7',
  title: 'If I Lived There',
  titleKo: '만약 내가 그곳에 산다면',
  exam: '2학기 기말고사',
  prose: true,
  stepsBefore: ["핵심어휘·숙어", "어휘선택", "T/F 내용 확인", "어법선택", "동사변형", "오류찾기", "본문 스크램블", "문장순서", "문장삽입", "어색한 문장", "빈칸추론", "핵심문법"],   /* 일치·불일치 추가 전 단계 이름: 예전 기록을 새 단계에 맞추는 데 씀 */
  teacherPhone: '',            /* 결과 받을 번호. 예: '010-1234-5678' */

  days: [
  /* ═══════════════════════════ DAY 1 · 본문 ❶❷ ═══════════════════════════ */
  {
    id: 'd1', name: 'DAY 1', range: '7과 본문 ❶❷', story: '다양한 집 · 미국 푸에블로 · 이탈리아 베니스',
    passage: [
      ['', '❶', ''],
      ['', 'Different people live in different houses.', '다양한 사람들이 다양한 집에서 삽니다.'],
      ['', 'Some use ladders to enter their houses.', '몇몇 사람들은 집에 들어가기 위해 사다리를 이용합니다.'],
      ['', 'Others live in houses on the water.', '다른 사람들은 물 위에 있는 집에 삽니다.'],
      ['', 'And others share their houses with many people.', '그리고 또 다른 사람들은 많은 사람과 함께 집을 공유합니다.'],
      ['', 'Imagine you live in one of these houses.', '여러분이 이 집들 중 하나에 산다고 상상해 보세요.'],
      ['', 'How would that change your life?', '여러분의 삶은 어떻게 바뀔까요?'],
      ['', 'Pueblos in New Mexico, USA', '뉴멕시코의 푸에블로, 미국'],
      ['', 'If I lived in a pueblo, I would climb up a ladder to enter my house.', '만약 내가 푸에블로에 산다면, 나는 집에 들어가기 위해 사다리를 오를 것이다.'],
      ['', "There's a hidden opening on top of the house.", '집 꼭대기에는 숨겨진 구멍이 있다.'],
      ['', 'If unwelcome visitors appeared, I would pull the ladder up to stop them from entering.', '만약 반갑지 않은 방문객이 나타난다면 나는 사다리를 끌어 올려 그들이 들어오지 못하게 할 것이다.'],
      ['', 'The thick walls are made of earth, straw, and water.', '두꺼운 벽은 흙, 지푸라기, 물로 만들어져 있다.'],
      ['', 'They would keep me cool in summer and warm in winter.', '그것들은 여름에는 시원하게, 겨울에는 따뜻하게 유지해 줄 것이다.'],
      ['', 'The house has a flat roof.', '집에는 평평한 지붕이 있다.'],
      ['', 'I would sometimes sleep up on the roof under the moon and stars.', '때때로 나는 달과 별들 아래의 지붕 위에서 잠을 잘 것이다.'],
      ['', '❷', ''],
      ['', 'Houses on Water in Venice, Italy', '베니스의 물 위에 있는 집, 이탈리아'],
      ['', 'If I lived in Venice, I would take a gondola to school every morning.', '만약 내가 베니스에 산다면, 나는 매일 아침 곤돌라를 타고 학교에 갈 것이다.'],
      ['', 'Venice has 118 small islands.', '베니스에는 118개의 작은 섬들이 있다.'],
      ['', 'On weekends, I would travel from island to island by a vaporetto, a water bus.', '주말마다 나는 수상 버스인 바포레토를 타고 이 섬 저 섬을 여행할 것이다.'],
      ['', 'At high tide, the water from the Adriatic Sea often rises and leaves the streets full of water.', '조수가 높을 때에는 아드리아해의 물이 자주 불어나 거리를 물로 가득 차게 한다.'],
      ['', 'However, I would be able to walk around the town through the raised walkways.', '그러나 나는 높이 올린 통로로 도심 주변을 걸어 다닐 수 있을 것이다.'],
      ['', 'Venice is known as the "floating city."', '베니스는 \'떠 있는 도시\'로 알려져 있다.'],
      ['', 'In Venice, there are many colorful houses on the water.', '베니스에는 물 위에 있는 색색의 건물들이 많다.'],
      ['', 'You may wonder how and why they built the houses on the water.', '여러분은 어떻게 그리고 왜 그들이 물 위에 집을 지었는지 궁금할 것이다.'],
      ['', 'The old Venetians decided to live there to keep themselves safe from invaders.', '옛 베니스인들은 침략자들로부터 자신들을 안전하게 지키기 위해 그곳에 살기로 결정했다.'],
      ['', 'But it was not easy for them to build their homes on this swampy surface.', '하지만 그들이 이 습지 위에 집을 짓는 것은 쉽지가 않았다.'],
      ['', 'So they installed more than 10 million wooden poles in the ground.', '그래서 그들은 땅에 천만 개 이상의 나무 기둥들을 설치했다.'],
      ['', 'It is these wooden poles that support Venice to this day.', '지금까지 베니스를 지탱해 주고 있는 것은 바로 이 나무 기둥들이다.']
    ],
    steps: [
      { type: 'vocab', title: '핵심어휘·숙어', quizN: 15, items: [
        ['ladder', '사다리'], ['enter', '들어가다'], ['share A with B', 'A를 B와 공유하다'], ['imagine', '상상하다'],
        ['climb up', '~을 올라가다'], ['hidden', '숨겨진'], ['opening', '구멍, 틈'], ['unwelcome', '반갑지 않은'],
        ['appear', '나타나다'], ['pull up', '끌어올리다'], ['stop A from -ing', 'A가 ~하지 못하게 막다'], ['be made of', '~로 만들어지다'],
        ['earth', '흙'], ['straw', '지푸라기, 짚'], ['flat', '평평한'], ['roof', '지붕'],
        ['island', '섬'], ['tide', '조수, 밀물과 썰물'], ['rise', '(물이) 불어나다, 오르다'], ['leave A full of B', 'A를 B로 가득 찬 상태로 두다'],
        ['be able to', '~할 수 있다'], ['raised', '높인, 들어 올린'], ['walkway', '통로, 보도'], ['be known as', '~로 알려져 있다'],
        ['floating', '떠 있는'], ['wonder', '궁금해하다'], ['invader', '침략자'], ['swampy', '늪 같은, 질퍽한'],
        ['surface', '표면'], ['install', '설치하다'], ['pole', '기둥, 막대'], ['support', '지탱하다, 떠받치다'],
        ['to this day', '오늘날까지']
      ]},
      { type: 'pick', title: '어휘선택', guide: '문맥에 맞는 낱말을 고르세요.', items: [
        { s: 'Some use {ladders|boats} to enter their houses.', ex: '푸에블로 사람들은 사다리(ladder)로 집에 들어간다.' },
        { s: 'And others {share|sell} their houses with many people.', ex: 'share A with B: A를 B와 공유하다' },
        { s: "There's a {hidden|broken} opening on top of the house.", ex: 'hidden: 숨겨진' },
        { s: 'If {unwelcome|welcome} visitors appeared, I would pull the ladder up to stop them from entering.', ex: '들어오지 못하게 막을 사람 → 반갑지 않은(unwelcome) 방문객' },
        { s: 'The {thick|thin} walls are made of earth, straw, and water.', ex: '두꺼운(thick) 벽이 여름엔 시원하고 겨울엔 따뜻하게 해 준다.' },
        { s: 'The house has a {flat|round} roof.', ex: '지붕 위에서 잘 수 있으려면 평평해야(flat) 한다.' },
        { s: 'If I lived in Venice, I would take a {gondola|train} to school every morning.', ex: '물의 도시 베니스 → 곤돌라(gondola)' },
        { s: 'At high tide, the water from the Adriatic Sea often {rises|falls} and leaves the streets full of water.', ex: '조수가 높을 때 물이 불어난다(rise).' },
        { s: 'The old Venetians decided to live there to keep themselves safe from {invaders|tourists}.', ex: 'invader: 침략자' },
        { s: 'But it was not easy for them to build their homes on this {swampy|dry} surface.', ex: 'swampy: 늪 같은, 질퍽한' },
        { s: 'So they installed more than 10 million wooden {poles|walls} in the ground.', ex: 'pole: 기둥 → 나무 기둥이 베니스를 떠받친다.' }
      ]},
      { type: 'tf', title: 'T/F 내용 확인', guide: '본문 내용과 일치하면 T, 다르면 F를 고르세요.', items: [
        ['Some people use ladders to enter their houses.', true, 'Some use ladders to enter their houses.'],
        ['People in a pueblo enter their houses through the front door.', false, '사다리를 타고 지붕의 숨겨진 구멍으로 들어간다.'],
        ['The walls of a pueblo are made of earth, straw, and water.', true, 'made of earth, straw, and water'],
        ['The walls of a pueblo make the house hot in summer.', false, '여름에는 시원하게(cool) 해 준다.'],
        ['A pueblo has a flat roof.', true, 'The house has a flat roof.'],
        ['Venice has 118 small islands.', true, 'Venice has 118 small islands.'],
        ['A vaporetto is a kind of train.', false, '바포레토는 수상 버스(a water bus)다.'],
        ['The old Venetians lived on the water to stay safe from invaders.', true, 'to keep themselves safe from invaders'],
        ['It was easy to build homes on the swampy surface of Venice.', false, '습지 위에 집을 짓는 것은 쉽지 않았다.']
      ]},
      { type: 'mc', title: '일치·불일치', guide: "선택지는 본문 표현을 쉬운 말로 조금 바꿔 썼어요. 해설의 \"바꿔 쓴 표현\"을 꼭 확인하세요.", items: [
        { n: "❶", box: ["❶"], q: "푸에블로에 관한 내용과 일치하지 <u>않는</u> 것은?", opts: ["The walls of a pueblo are made of stone and wood.", "People climb a ladder to get into a pueblo.", "There is a secret opening on the top of the house.", "Pulling up the ladder can keep unwelcome visitors out.", "The roof of a pueblo is flat."], ex: "정답 근거: The thick walls are made of earth, straw, and water.\n· 바꿔 쓴 표현: get into = enter · secret = hidden · keep ~ out = stop ~ from entering\n· be made of : ~로 만들어지다 · straw : 지푸라기", per: [["푸에블로의 벽은 돌과 나무로 만들어진다.", "The thick walls are made of earth, straw, and water", "불일치 → 흙, 지푸라기, 물"], ["사람들은 푸에블로에 들어가기 위해 사다리를 오른다.", "I would climb up a ladder to enter my house", "일치 (get into = enter)"], ["집 꼭대기에 비밀 구멍이 있다.", "There's a hidden opening on top of the house", "일치 (secret = hidden)"], ["사다리를 끌어 올리면 반갑지 않은 방문객을 막을 수 있다.", "I would pull the ladder up to stop them from entering", "일치 (keep ~ out = stop ~ from entering)"], ["푸에블로의 지붕은 평평하다.", "The house has a flat roof", "일치"]] },
        { n: "❷", box: ["❷"], q: "베니스에 관한 내용과 <u>일치하는</u> 것은?", opts: ["The old Venetians moved there to protect themselves from invaders.", "Venice is made up of 18 large islands.", "A vaporetto is a kind of taxi on the road.", "It was easy to build houses on the swampy ground.", "Stone pillars support Venice today."], ex: "정답 근거: The old Venetians decided to live there to keep themselves safe from invaders.\n· 바꿔 쓴 표현: protect A from B = keep A safe from B · be made up of : ~로 이루어지다 · pillar ≒ pole : 기둥\n· invader : 침략자 · swampy : 늪지의 · install : 설치하다", per: [["옛 베니스인들은 침략자로부터 자신을 지키려고 그곳으로 옮겨 갔다.", "to keep themselves safe from invaders", "일치 (protect A from B = keep A safe from B)"], ["베니스는 18개의 큰 섬으로 이루어져 있다.", "Venice has 118 small islands", "불일치 → 118개의 작은 섬"], ["바포레토는 도로 위의 택시의 일종이다.", "a vaporetto, a water bus", "불일치 → 수상 버스"], ["늪지에 집을 짓는 것은 쉬웠다.", "it was not easy for them to build their homes", "불일치 → 쉽지 않았음"], ["오늘날 돌기둥이 베니스를 받치고 있다.", "It is these wooden poles that support Venice", "불일치 → 나무 기둥"]] }
      ]},
      { type: 'pick', title: '어법선택', guide: '어법상 알맞은 것을 고르세요.', items: [
        { s: 'If I {lived|live} in a pueblo, I would climb up a ladder to enter my house.', ex: '가정법 과거: If + 주어 + 과거동사' },
        { s: 'If I lived in a pueblo, I {would|will} climb up a ladder to enter my house.', ex: '가정법 과거: 주어 + would + 동사원형' },
        { s: "{There's|There are} a hidden opening on top of the house.", ex: 'a hidden opening은 단수 → There\'s (There is)' },
        { s: 'If unwelcome visitors appeared, I would pull the ladder up to stop them from {entering|enter}.', ex: 'stop A from -ing: A가 ~하지 못하게 하다' },
        { s: 'The thick walls {are made|make} of earth, straw, and water.', ex: 'be made of: ~로 만들어지다' },
        { s: 'They would keep me {cool|coolly} in summer and warm in winter.', ex: 'keep + 목적어 + 형용사' },
        { s: 'At high tide, the water from the Adriatic Sea often rises and leaves the streets {full|fully} of water.', ex: 'leave + 목적어 + 형용사(full of)' },
        { s: 'However, I would be able {to walk|walking} around the town through the raised walkways.', ex: 'be able to + 동사원형' },
        { s: 'You may wonder how and why {they built|did they build} the houses on the water.', ex: '간접의문문: 의문사 + 주어 + 동사' },
        { s: 'The old Venetians decided to live there to keep {themselves|them} safe from invaders.', ex: '주어(Venetians) 자신 → 재귀대명사 themselves' },
        { s: 'But it was not easy {for them|of them} to build their homes on this swampy surface.', ex: 'to부정사의 의미상 주어: for + 목적격' },
        { s: 'It is these wooden poles {that|what} support Venice to this day.', ex: '강조구문: It is ~ that' }
      ]},
      { type: 'verb', title: '동사변형', guide: '( ) 안의 동사를 알맞은 형태로 바꿔 쓰세요.', items: [
        { s: 'If I ___ in a pueblo, I would climb up a ladder to enter my house.', v: 'live', a: ['lived'], ex: '가정법 과거 → if절에 과거형' },
        { s: 'If I lived in a pueblo, I would climb up a ladder ___ my house.', v: 'enter', a: ['to enter'], ex: '목적(~하기 위해) → to enter' },
        { s: 'If unwelcome visitors ___, I would pull the ladder up to stop them from entering.', v: 'appear', a: ['appeared'], ex: '가정법 과거 → appeared' },
        { s: 'If unwelcome visitors appeared, I would pull the ladder up to stop them from ___.', v: 'enter', a: ['entering'], ex: 'stop A from -ing' },
        { s: 'The thick walls are ___ of earth, straw, and water.', v: 'make', a: ['made'], ex: 'be made of: ~로 만들어지다' },
        { s: 'At high tide, the water from the Adriatic Sea often ___ and leaves the streets full of water.', v: 'rise', a: ['rises'], ex: '단수 주어 the water → rises' },
        { s: 'Venice is ___ as the "floating city."', v: 'know', a: ['known'], ex: 'be known as: ~로 알려져 있다' },
        { s: 'You may wonder how and why they ___ the houses on the water.', v: 'build', a: ['built'], ex: 'build - built - built' },
        { s: 'The old Venetians decided ___ there to keep themselves safe from invaders.', v: 'live', a: ['to live'], ex: 'decide + to부정사' },
        { s: 'So they ___ more than 10 million wooden poles in the ground.', v: 'install', a: ['installed'], ex: '과거 이야기 → installed' }
      ]},
      { type: 'error', title: '오류찾기', guide: '어법상 틀린 곳을 고르세요.', items: [
        { s: 'If I [[live]] in a pueblo, I [[would]] climb up a ladder [[to enter]] [[my]] house.', w: 0, fix: 'lived', ex: '가정법 과거: If + 주어 + 과거동사' },
        { s: 'If unwelcome visitors [[appeared]], I [[would]] pull the ladder [[up]] to stop them from [[enter]].', w: 3, fix: 'entering', ex: 'stop A from -ing' },
        { s: 'The thick walls [[make]] of earth, straw, and water. They would [[keep]] me [[cool]] in summer and [[warm]] in winter.', w: 0, fix: 'are made', ex: 'be made of: ~로 만들어지다' },
        { s: 'They would keep me [[coolly]] in summer and warm in winter. The house [[has]] a [[flat]] roof.', w: 0, fix: 'cool', ex: 'keep + 목적어 + 형용사(부사 X)' },
        { s: 'At high tide, the water from the Adriatic Sea often [[rises]] and [[leaves]] the streets [[fully]] of water. However, I would be able [[to walk]] around the town.', w: 2, fix: 'full', ex: 'leave + 목적어 + 형용사' },
        { s: 'Venice is [[known]] as the "floating city." In Venice, there [[is]] many [[colorful]] houses [[on]] the water.', w: 1, fix: 'are', ex: 'many colorful houses는 복수 → there are' },
        { s: 'You may wonder how and why [[did they build]] the houses on the water. The old Venetians [[decided]] [[to live]] there to keep [[themselves]] safe from invaders.', w: 0, fix: 'they built', ex: '간접의문문: 의문사 + 주어 + 동사' },
        { s: 'But it was not easy [[of them]] [[to build]] their homes on this swampy surface. It [[is]] these wooden poles [[that]] support Venice to this day.', w: 0, fix: 'for them', ex: '의미상 주어: for + 목적격' }
      ]},
      { type: 'scramble', title: '본문 스크램블', guide: '우리말에 맞게 단어를 눌러 문장을 완성하세요.', items: [
        { ko: '다양한 사람들이 다양한 집에서 산다.', en: 'Different people live in different houses.' },
        { ko: '여러분의 삶은 어떻게 바뀔까요?', en: 'How would that change your life?' },
        { ko: '만약 내가 푸에블로에 산다면, 나는 집에 들어가기 위해 사다리를 오를 것이다.', en: 'If I lived in a pueblo, I would climb up a ladder to enter my house.' },
        { ko: '두꺼운 벽은 흙, 지푸라기, 물로 만들어져 있다.', en: 'The thick walls are made of earth, straw, and water.' },
        { ko: '그것들은 여름에는 시원하게, 겨울에는 따뜻하게 유지해 줄 것이다.', en: 'They would keep me cool in summer and warm in winter.' },
        { ko: '만약 내가 베니스에 산다면, 나는 매일 아침 곤돌라를 타고 학교에 갈 것이다.', en: 'If I lived in Venice, I would take a gondola to school every morning.' },
        { ko: '하지만 그들이 이 습지 위에 집을 짓는 것은 쉽지가 않았다.', en: 'But it was not easy for them to build their homes on this swampy surface.' },
        { ko: '지금까지 베니스를 지탱해 주고 있는 것은 바로 이 나무 기둥들이다.', en: 'It is these wooden poles that support Venice to this day.' }
      ]},
      { type: 'order', title: '문장순서', guide: '문장을 본문 순서대로 눌러서 배열하세요.', items: [
        { lines: [
          'Different people live in different houses.',
          'Some use ladders to enter their houses.',
          'Others live in houses on the water.',
          'And others share their houses with many people.'
        ]},
        { lines: [
          'If I lived in a pueblo, I would climb up a ladder to enter my house.',
          "There's a hidden opening on top of the house.",
          'If unwelcome visitors appeared, I would pull the ladder up to stop them from entering.',
          'The thick walls are made of earth, straw, and water.'
        ]},
        { lines: [
          'If I lived in Venice, I would take a gondola to school every morning.',
          'Venice has 118 small islands.',
          'On weekends, I would travel from island to island by a vaporetto, a water bus.',
          'At high tide, the water from the Adriatic Sea often rises and leaves the streets full of water.'
        ]},
        { lines: [
          'The old Venetians decided to live there to keep themselves safe from invaders.',
          'But it was not easy for them to build their homes on this swampy surface.',
          'So they installed more than 10 million wooden poles in the ground.',
          'It is these wooden poles that support Venice to this day.'
        ]}
      ]},
      { type: 'insert', title: '문장삽입', guide: '주어진 문장이 들어가기에 가장 알맞은 곳을 고르세요.', items: [
        { lines: [
          'Different people live in different houses.',
          'Some use ladders to enter their houses.',
          'Others live in houses on the water.',
          'And others share their houses with many people.'
        ], given: 2, ex: 'Some ~ Others ~ And others ~: 어떤 사람들은 ~, 다른 사람들은 ~, 또 다른 사람들은 ~' },
        { lines: [
          "If I lived in a pueblo, I would climb up a ladder to enter my house.",
          "There's a hidden opening on top of the house.",
          'If unwelcome visitors appeared, I would pull the ladder up to stop them from entering.',
          'The thick walls are made of earth, straw, and water.'
        ], given: 2, ex: '꼭대기 구멍으로 사다리를 타고 들어가므로, 사다리를 끌어 올리면 들어올 수 없다.' },
        { lines: [
          'The thick walls are made of earth, straw, and water.',
          'They would keep me cool in summer and warm in winter.',
          'The house has a flat roof.',
          'I would sometimes sleep up on the roof under the moon and stars.'
        ], given: 1, ex: 'They는 앞 문장의 The thick walls를 가리킨다.' },
        { lines: [
          'The old Venetians decided to live there to keep themselves safe from invaders.',
          'But it was not easy for them to build their homes on this swampy surface.',
          'So they installed more than 10 million wooden poles in the ground.',
          'It is these wooden poles that support Venice to this day.'
        ], given: 2, ex: 'So(그래서) 앞에는 이유(습지에 집 짓기가 어려움)가 와야 한다.' }
      ]},
      { type: 'odd', title: '어색한 문장', guide: '글의 흐름과 관계없는 문장을 고르세요.', items: [
        { lines: [
          'Different people live in different houses.',
          'Some use ladders to enter their houses.',
          'Everyone in the world lives in the same kind of house.',
          'Others live in houses on the water.'
        ], odd: 2, ex: '사람마다 다른 집에 산다는 내용과 반대된다.' },
        { lines: [
          'The thick walls are made of earth, straw, and water.',
          'They would keep me cool in summer and warm in winter.',
          'The walls make the house very cold in winter.',
          'The house has a flat roof.'
        ], odd: 2, ex: '벽이 겨울에 따뜻하게 해 준다는 내용과 반대된다.' },
        { lines: [
          'Venice is known as the "floating city."',
          'In Venice, there are many colorful houses on the water.',
          'Venice has no water at all.',
          'You may wonder how and why they built the houses on the water.'
        ], odd: 2, ex: '물 위의 도시라는 내용과 맞지 않는다.' }
      ]},
      { type: 'blank', title: '빈칸추론', guide: '빈칸에 들어갈 말로 가장 알맞은 것을 고르세요.', items: [
        { s: 'If unwelcome visitors appeared, I would pull the ladder up to stop them from ____.', opts: ['entering', 'leaving', 'sleeping', 'helping'], ex: '사다리를 끌어 올려 들어오지(entering) 못하게 한다.' },
        { s: 'They would keep me ____ in summer and warm in winter.', opts: ['cool', 'hot', 'busy', 'sad'], ex: '여름에는 시원하게, 겨울에는 따뜻하게' },
        { s: 'The old Venetians decided to live there to keep themselves safe from ____.', opts: ['invaders', 'friends', 'tourists', 'water'], ex: '침략자로부터 안전하게 지키기 위해 물 위에 살았다.' },
        { s: 'So they installed more than 10 million ____ in the ground.', opts: ['wooden poles', 'glass windows', 'stone walls', 'water buses'], ex: '나무 기둥이 지금까지 베니스를 떠받치고 있다.' }
      ]},
      { type: 'mc', title: '핵심문법', guide: '알맞은 답을 고르세요.', items: [
        { q: '빈칸에 알맞은 것은?<br><b>If I ______ in Venice, I would take a gondola to school.</b>', opts: ['lived', 'live', 'will live', 'have lived'], ex: '가정법 과거: If + 주어 + 과거동사, 주어 + would + 동사원형' },
        { q: '빈칸에 알맞은 것은?<br><b>If I had a sister, I ______ play tennis with her.</b>', opts: ['would', 'will', 'am', 'did'], ex: '가정법 과거 주절: would + 동사원형' },
        { q: '다음 문장에서 알 수 있는 사실은?<br><b>If I lived in a pueblo, I would climb up a ladder.</b>', opts: ['나는 지금 푸에블로에 살지 않는다.', '나는 지금 푸에블로에 산다.', '나는 예전에 푸에블로에 살았다.', '나는 곧 푸에블로로 이사 간다.'], ex: '가정법 과거는 현재 사실의 반대를 가정한다.' },
        { q: '빈칸에 알맞은 것은?<br><b>If I ______ you, I would not say so.</b>', opts: ['were', 'am', 'be', 'is'], ex: '가정법 과거에서 be동사는 주로 were' },
        { q: '빈칸에 알맞은 것은?<br><b>Wearing a helmet keeps you ______.</b>', opts: ['safe', 'safely', 'safety', 'to safe'], ex: 'keep + 목적어 + 형용사' },
        { q: '빈칸에 알맞은 것은?<br><b>The news made him ______.</b>', opts: ['happy', 'happily', 'happiness', 'to happy'], ex: 'make + 목적어 + 형용사' },
        { q: '빈칸에 알맞은 것은?<br><b>It is these wooden poles ______ support Venice.</b>', opts: ['that', 'what', 'where', 'how'], ex: '강조구문: It is + 강조할 말 + that' },
        { q: '빈칸에 알맞은 것은?<br><b>It was not easy ______ them to build their homes.</b>', opts: ['for', 'of', 'to', 'with'], ex: 'to부정사의 의미상 주어: for + 목적격' },
        { q: '빈칸에 알맞은 것은?<br><b>You may wonder ______.</b>', opts: ['how they built the houses', 'how did they build the houses', 'how built they the houses', 'how they did build the houses'], ex: '간접의문문: 의문사 + 주어 + 동사' }
      ]}
    ]
  },

  /* ═══════════════════════════ DAY 2 · 본문 ❸ ═══════════════════════════ */
  {
    id: 'd2', name: 'DAY 2', range: '7과 본문 ❸', story: '중국 푸젠의 토루 · 마무리',
    passage: [
      ['', '❸', ''],
      ['', 'Tulou in Fujian, China', '푸젠의 토루, 중국'],
      ['', 'If I lived in a tulou, a huge round house in Fujian, China, I would always have friends at home to play with.', '만약 내가 거대하고 둥그런 집인 중국 푸젠의 토루에 산다면, 나는 항상 집에 함께 놀 친구들이 있을 것이다.'],
      ['', 'I would sometimes hear my neighbor calling me to come over for tea or dinner.', '때때로 나의 이웃이 차를 마시거나 저녁 식사를 하러 들르라고 나를 부르는 소리를 듣게 될 것이다.'],
      ['', 'In a tulou, there are usually three to five floors.', '토루는 대개 3층에서 5층으로 되어 있다.'],
      ['', 'The first floor is used for cooking and eating.', '1층은 요리하고 식사하는 데에 사용된다.'],
      ['', 'And people store food and tools on the second floor.', '그리고 사람들은 2층에 식량과 도구를 보관한다.'],
      ['', 'Do you wonder where I would sleep?', '내가 어디에서 잠을 잘지 궁금한가?'],
      ['', 'My bedroom would be on the third or fourth floor.', '내 침실은 3층이나 4층에 있을 것이다.'],
      ['', 'A tulou is like a village.', '토루는 마을과 같다.'],
      ['', 'The people living in a tulou mostly have the same family name.', '토루에 사는 사람들은 대부분 같은 성(姓)을 가지고 있다.'],
      ['', 'Some large tulou can house up to 50 families.', '몇몇 큰 토루는 50가구까지 수용할 수 있다.'],
      ['', 'They work together and share many things.', '그들은 함께 일하고 많은 것을 공유한다.'],
      ['', 'Living together in one building keeps them safe.', '한 건물에 함께 사는 것은 그들을 안전하게 지켜 준다.'],
      ['', 'Homes are everywhere.', '집은 어디에나 있습니다.'],
      ['', 'But they are different all over the world.', '그러나 전 세계의 집은 다릅니다.'],
      ['', 'What is your home like?', '여러분의 집은 어떻습니까?']
    ],
    steps: [
      { type: 'vocab', title: '핵심어휘·숙어', quizN: 15, items: [
        ['huge', '거대한'], ['round', '둥근'], ['play with', '~와 함께 놀다'], ['neighbor', '이웃'],
        ['hear A -ing', 'A가 ~하는 것을 듣다'], ['call A to ~', 'A에게 ~하라고 부르다'], ['come over', '(집에) 들르다'], ['floor', '층'],
        ['be used for', '~에 사용되다'], ['store', '저장하다, 보관하다'], ['tool', '도구'], ['wonder', '궁금해하다'],
        ['bedroom', '침실'], ['like (전치사)', '~와 같은, ~처럼'], ['village', '마을'], ['mostly', '대부분, 주로'],
        ['family name', '성(姓)'], ['house (동사)', '수용하다, 살 곳을 제공하다'], ['up to', '~까지'], ['work together', '함께 일하다'],
        ['share', '공유하다, 나누다'], ['safe', '안전한'], ['everywhere', '어디에나'], ['all over the world', '전 세계에'],
        ['What is ~ like?', '~은 어떠니?']
      ]},
      { type: 'pick', title: '어휘선택', guide: '문맥에 맞는 낱말을 고르세요.', items: [
        { s: 'If I lived in a tulou, a {huge|tiny} round house in Fujian, China, I would always have friends at home to play with.', ex: '50가구까지 사는 거대한(huge) 집' },
        { s: 'I would sometimes hear my {neighbor|teacher} calling me to come over for tea or dinner.', ex: 'neighbor: 이웃' },
        { s: 'I would sometimes hear my neighbor calling me to come {over|off} for tea or dinner.', ex: 'come over: (집에) 들르다' },
        { s: 'The first floor is used for {cooking|sleeping} and eating.', ex: '1층은 요리와 식사용, 잠은 3·4층' },
        { s: 'And people {store|sell} food and tools on the second floor.', ex: 'store: 보관하다' },
        { s: 'My {bedroom|kitchen} would be on the third or fourth floor.', ex: '어디서 잘지에 대한 답 → bedroom' },
        { s: 'A tulou is like a {village|school}.', ex: '여러 가족이 함께 사는 마을(village) 같다.' },
        { s: 'The people living in a tulou mostly have the same {family name|birthday}.', ex: 'family name: 성(姓)' },
        { s: 'Some large tulou can {house|move} up to 50 families.', ex: 'house(동사): 수용하다' },
        { s: 'Living together in one building keeps them {safe|lonely}.', ex: '함께 살아서 안전하다(safe).' },
        { s: 'Homes are {everywhere|nowhere}.', ex: 'everywhere: 어디에나' }
      ]},
      { type: 'tf', title: 'T/F 내용 확인', guide: '본문 내용과 일치하면 T, 다르면 F를 고르세요.', items: [
        ['A tulou is a huge round house in China.', true, 'a huge round house in Fujian, China'],
        ['People in a tulou live alone without neighbors.', false, '이웃이 차나 저녁을 먹으러 오라고 부른다.'],
        ['In a tulou, there are usually ten floors.', false, '대개 3층에서 5층이다.'],
        ['The first floor is used for cooking and eating.', true, 'The first floor is used for cooking and eating.'],
        ['People store food and tools on the third floor.', false, '2층(the second floor)에 보관한다.'],
        ['The people living in a tulou mostly have the same family name.', true, 'mostly have the same family name'],
        ['Some large tulou can house up to 50 families.', true, 'up to 50 families'],
        ['Homes are the same all over the world.', false, '전 세계의 집은 다르다(different).']
      ]},
      { type: 'mc', title: '일치·불일치', guide: "선택지는 본문 표현을 쉬운 말로 조금 바꿔 썼어요. 해설의 \"바꿔 쓴 표현\"을 꼭 확인하세요.", items: [
        { n: "❸", box: ["❸"], q: "토루에 관한 내용과 일치하지 <u>않는</u> 것은?", opts: ["People sleep on the first floor of a tulou.", "A tulou is a huge round house.", "A tulou usually has three to five floors.", "Food and tools are kept on the second floor.", "Most people in a tulou share the same family name."], ex: "정답 근거: The first floor is used for cooking and eating. / My bedroom would be on the third or fourth floor.\n· 바꿔 쓴 표현: keep = store · share the same = have the same\n· store : 보관하다 · house : 수용하다(동사)", per: [["사람들은 토루의 1층에서 잔다.", ["The first floor is used for cooking and eating", "My bedroom would be on the third or fourth floor"], "불일치 → 1층은 요리·식사, 침실은 3·4층"], ["토루는 거대하고 둥근 집이다.", "a huge round house", "일치"], ["토루는 보통 3~5층이다.", "there are usually three to five floors", "일치"], ["식량과 도구는 2층에 보관된다.", "people store food and tools on the second floor", "일치 (keep = store)"], ["토루 사람들 대부분은 성(姓)이 같다.", "mostly have the same family name", "일치 (share = have the same)"]] },
        { n: "❸", box: ["❸"], q: "토루에 관한 내용과 <u>일치하는</u> 것은?", opts: ["Some big tulou have room for as many as 50 families.", "People in a tulou rarely meet their neighbors.", "Families in a tulou work separately.", "Living in one building is dangerous for them.", "Homes are the same all over the world."], ex: "정답 근거: Some large tulou can house up to 50 families.\n· 바꿔 쓴 표현: have room for = house (수용하다) · as many as = up to (최대 ~까지)\n· rarely : 거의 ~않다 · separately : 따로", per: [["어떤 큰 토루는 50가구까지 들어갈 공간이 있다.", "Some large tulou can house up to 50 families", "일치 (have room for = house · as many as = up to)"], ["토루 사람들은 이웃을 거의 만나지 않는다.", "I would sometimes hear my neighbor calling me to come over", "불일치 → 이웃이 놀러 오라고 부름"], ["토루의 가족들은 따로 일한다.", "They work together and share many things", "불일치 → 함께 일함"], ["한 건물에 사는 것은 그들에게 위험하다.", "Living together in one building keeps them safe", "불일치 → 안전하게 지켜 줌"], ["집은 전 세계 어디나 똑같다.", "But they are different all over the world", "불일치 → 서로 다름"]] }
      ]},
      { type: 'pick', title: '어법선택', guide: '어법상 알맞은 것을 고르세요.', items: [
        { s: 'If I {lived|live} in a tulou, a huge round house in Fujian, China, I would always have friends at home to play with.', ex: '가정법 과거: If + 주어 + 과거동사' },
        { s: 'If I lived in a tulou, a huge round house in Fujian, China, I would always have friends at home to play {with|for}.', ex: 'play with friends → friends to play with' },
        { s: 'I would sometimes hear my neighbor {calling|to call} me to come over for tea or dinner.', ex: '지각동사 hear + 목적어 + 현재분사(동사원형)' },
        { s: 'I would sometimes hear my neighbor calling me {to come|coming} over for tea or dinner.', ex: 'call + 목적어 + to부정사' },
        { s: 'In a tulou, there {are|is} usually three to five floors.', ex: '복수명사 floors → there are' },
        { s: 'The first floor {is used|uses} for cooking and eating.', ex: 'be used for: ~에 사용되다' },
        { s: 'The first floor is used for {cooking|cook} and eating.', ex: '전치사 for 뒤 → 동명사' },
        { s: 'Do you wonder {where I would sleep|where would I sleep}?', ex: '간접의문문: 의문사 + 주어 + 동사' },
        { s: 'The people {living|lived} in a tulou mostly have the same family name.', ex: '"~에 사는" 능동 → 현재분사 living' },
        { s: 'The people living in a tulou mostly {have|has} the same family name.', ex: '주어 The people(복수) → have' },
        { s: 'Living together in one building {keeps|keep} them safe.', ex: '동명사 주어는 단수 → keeps' },
        { s: 'What is your home {like|look}?', ex: 'What is ~ like?: ~은 어떠니?' }
      ]},
      { type: 'verb', title: '동사변형', guide: '( ) 안의 동사를 알맞은 형태로 바꿔 쓰세요.', items: [
        { s: 'If I ___ in a tulou, a huge round house in Fujian, China, I would always have friends at home to play with.', v: 'live', a: ['lived'], ex: '가정법 과거 → lived' },
        { s: 'If I lived in a tulou, a huge round house in Fujian, China, I would always have friends at home ___ with.', v: 'play', a: ['to play'], ex: '명사(friends)를 꾸미는 to부정사' },
        { s: 'I would sometimes hear my neighbor ___ me to come over for tea or dinner.', v: 'call', a: ['calling', 'call'], ex: '지각동사 hear + 목적어 + 현재분사/동사원형 (본문: calling)' },
        { s: 'I would sometimes hear my neighbor calling me ___ over for tea or dinner.', v: 'come', a: ['to come'], ex: 'call + 목적어 + to부정사' },
        { s: 'The first floor is ___ for cooking and eating.', v: 'use', a: ['used'], ex: 'be used for' },
        { s: 'The first floor is used for ___ and eating.', v: 'cook', a: ['cooking'], ex: '전치사 뒤 → 동명사' },
        { s: 'And people ___ food and tools on the second floor.', v: 'store', a: ['store'], ex: '복수 주어 → store' },
        { s: 'The people ___ in a tulou mostly have the same family name.', v: 'live', a: ['living'], ex: '명사를 꾸미는 현재분사' },
        { s: '___ together in one building keeps them safe.', v: 'live', a: ['Living', 'To live'], ex: '주어 자리 → 동명사 (본문: Living)' },
        { s: 'Living together in one building ___ them safe.', v: 'keep', a: ['keeps'], ex: '동명사 주어는 단수 → keeps' }
      ]},
      { type: 'error', title: '오류찾기', guide: '어법상 틀린 곳을 고르세요.', items: [
        { s: 'If I [[live]] in a tulou, a huge round house in Fujian, China, I [[would]] always have friends at home [[to play]] [[with]].', w: 0, fix: 'lived', ex: '가정법 과거 → lived' },
        { s: 'I would sometimes [[hear]] my neighbor [[calling]] me [[come]] over [[for]] tea or dinner.', w: 2, fix: 'to come', ex: 'call + 목적어 + to부정사' },
        { s: 'In a tulou, there [[is]] usually three to five floors. The first floor [[is used]] for [[cooking]] and [[eating]].', w: 0, fix: 'are', ex: '복수명사 floors → there are' },
        { s: 'The first floor [[uses]] for cooking and eating. And people [[store]] food and tools [[on]] the second floor.', w: 0, fix: 'is used', ex: 'be used for: ~에 사용되다' },
        { s: 'Do you wonder [[where would I sleep]]? My bedroom [[would be]] on the [[third]] or fourth floor.', w: 0, fix: 'where I would sleep', ex: '간접의문문: 의문사 + 주어 + 동사' },
        { s: 'The people [[lived]] in a tulou mostly [[have]] the same family name. Some large tulou [[can]] [[house]] up to 50 families.', w: 0, fix: 'living', ex: '"~에 사는"(능동) → 현재분사 living' },
        { s: 'Living together in one building [[keep]] them [[safe]]. Homes [[are]] [[everywhere]].', w: 0, fix: 'keeps', ex: '동명사 주어는 단수 → keeps' },
        { s: 'But they [[are]] different [[all over]] the world. What [[is]] your home [[look]]?', w: 3, fix: 'like', ex: 'What is ~ like?: ~은 어떠니?' }
      ]},
      { type: 'scramble', title: '본문 스크램블', guide: '우리말에 맞게 단어를 눌러 문장을 완성하세요.', items: [
        { ko: '나는 항상 집에 함께 놀 친구들이 있을 것이다.', en: 'I would always have friends at home to play with.' },
        { ko: '1층은 요리하고 식사하는 데에 사용된다.', en: 'The first floor is used for cooking and eating.' },
        { ko: '사람들은 2층에 식량과 도구를 보관한다.', en: 'People store food and tools on the second floor.' },
        { ko: '내가 어디에서 잠을 잘지 궁금한가?', en: 'Do you wonder where I would sleep?' },
        { ko: '토루는 마을과 같다.', en: 'A tulou is like a village.' },
        { ko: '토루에 사는 사람들은 대부분 같은 성을 가지고 있다.', en: 'The people living in a tulou mostly have the same family name.' },
        { ko: '한 건물에 함께 사는 것은 그들을 안전하게 지켜 준다.', en: 'Living together in one building keeps them safe.' },
        { ko: '여러분의 집은 어떻습니까?', en: 'What is your home like?' }
      ]},
      { type: 'order', title: '문장순서', guide: '문장을 본문 순서대로 눌러서 배열하세요.', items: [
        { lines: [
          'If I lived in a tulou, a huge round house in Fujian, China, I would always have friends at home to play with.',
          'I would sometimes hear my neighbor calling me to come over for tea or dinner.',
          'In a tulou, there are usually three to five floors.',
          'The first floor is used for cooking and eating.'
        ]},
        { lines: [
          'The first floor is used for cooking and eating.',
          'And people store food and tools on the second floor.',
          'Do you wonder where I would sleep?',
          'My bedroom would be on the third or fourth floor.'
        ]},
        { lines: [
          'A tulou is like a village.',
          'The people living in a tulou mostly have the same family name.',
          'Some large tulou can house up to 50 families.',
          'They work together and share many things.',
          'Living together in one building keeps them safe.'
        ]},
        { lines: [
          'Homes are everywhere.',
          'But they are different all over the world.',
          'What is your home like?'
        ]}
      ]},
      { type: 'insert', title: '문장삽입', guide: '주어진 문장이 들어가기에 가장 알맞은 곳을 고르세요.', items: [
        { lines: [
          'In a tulou, there are usually three to five floors.',
          'The first floor is used for cooking and eating.',
          'And people store food and tools on the second floor.',
          'Do you wonder where I would sleep?',
          'My bedroom would be on the third or fourth floor.'
        ], given: 3, ex: '"어디서 잘지 궁금한가?"라는 질문 뒤에 침실 위치가 대답으로 온다.' },
        { lines: [
          'The first floor is used for cooking and eating.',
          'And people store food and tools on the second floor.',
          'Do you wonder where I would sleep?',
          'My bedroom would be on the third or fourth floor.'
        ], given: 1, ex: '1층 다음에 2층 쓰임새가 이어진다.' },
        { lines: [
          'Some large tulou can house up to 50 families.',
          'They work together and share many things.',
          'Living together in one building keeps them safe.'
        ], given: 1, ex: 'They는 앞 문장의 50 families를 가리킨다.' },
        { lines: [
          'Homes are everywhere.',
          'But they are different all over the world.',
          'What is your home like?'
        ], given: 1, ex: 'But(그러나)으로 "어디에나 있다"와 "서로 다르다"를 대조한다.' }
      ]},
      { type: 'odd', title: '어색한 문장', guide: '글의 흐름과 관계없는 문장을 고르세요.', items: [
        { lines: [
          'If I lived in a tulou, a huge round house in Fujian, China, I would always have friends at home to play with.',
          'I would sometimes hear my neighbor calling me to come over for tea or dinner.',
          'I would never see my neighbors in a tulou.',
          'In a tulou, there are usually three to five floors.'
        ], odd: 2, ex: '이웃과 가깝게 지낸다는 내용과 반대된다.' },
        { lines: [
          'In a tulou, there are usually three to five floors.',
          'The first floor is used for cooking and eating.',
          'People never cook inside a tulou.',
          'And people store food and tools on the second floor.'
        ], odd: 2, ex: '1층에서 요리한다는 내용과 반대된다.' },
        { lines: [
          'A tulou is like a village.',
          'The people living in a tulou mostly have the same family name.',
          'Some large tulou can house up to 50 families.',
          'They never share anything with each other.',
          'Living together in one building keeps them safe.'
        ], odd: 3, ex: '함께 일하고 많은 것을 공유한다는 내용과 반대된다.' }
      ]},
      { type: 'blank', title: '빈칸추론', guide: '빈칸에 들어갈 말로 가장 알맞은 것을 고르세요.', items: [
        { s: 'I would sometimes hear my neighbor calling me to ____ for tea or dinner.', opts: ['come over', 'go away', 'stay home', 'run away'], ex: '차나 저녁을 먹으러 들르라고(come over) 부른다.' },
        { s: 'The first floor is used for ____.', opts: ['cooking and eating', 'sleeping', 'storing tools', 'playing games'], ex: '1층은 요리와 식사용이다.' },
        { s: 'Some large tulou can house ____ 50 families.', opts: ['up to', 'less than', 'only', 'away from'], ex: 'up to: ~까지' },
        { s: 'Living together in one building keeps them ____.', opts: ['safe', 'lonely', 'busy', 'angry'], ex: '함께 사는 것이 그들을 안전하게 지켜 준다.' }
      ]},
      { type: 'mc', title: '핵심문법', guide: '알맞은 답을 고르세요.', items: [
        { q: '빈칸에 알맞은 것은?<br><b>If I ______ in a tulou, I would always have friends at home.</b>', opts: ['lived', 'live', 'will live', 'living'], ex: '가정법 과거: If + 주어 + 과거동사' },
        { q: '"만약 내가 토루에 산다면, 항상 친구가 있을 텐데."를 바르게 영작한 것은?', opts: ['If I lived in a tulou, I would always have friends.', 'If I live in a tulou, I would always have friends.', 'If I lived in a tulou, I will always have friends.', 'If I lived in a tulou, I always had friends.'], ex: 'If + 과거동사, 주어 + would + 동사원형' },
        { q: '빈칸에 알맞은 것은?<br><b>Living together keeps them ______.</b>', opts: ['safe', 'safely', 'safety', 'to be safely'], ex: 'keep + 목적어 + 형용사' },
        { q: '빈칸에 알맞은 것은?<br><b>I heard my neighbor ______ me.</b>', opts: ['calling', 'to call', 'called', 'calls'], ex: '지각동사 hear + 목적어 + 현재분사(동사원형)' },
        { q: '빈칸에 알맞은 것은?<br><b>Do you wonder ______?</b>', opts: ['where I would sleep', 'where would I sleep', 'where I sleep would', 'where sleep I would'], ex: '간접의문문: 의문사 + 주어 + 동사' },
        { q: '빈칸에 알맞은 것은?<br><b>The people ______ in a tulou mostly have the same family name.</b>', opts: ['living', 'lived', 'to live', 'lives'], ex: '"~에 사는" 능동 → 현재분사' },
        { q: '빈칸에 알맞은 것은?<br><b>Living together in one building ______ them safe.</b>', opts: ['keeps', 'keep', 'keeping', 'to keep'], ex: '동명사 주어는 단수 취급' },
        { q: '빈칸에 알맞은 것은?<br><b>The first floor is used for ______ and eating.</b>', opts: ['cooking', 'cook', 'to cook', 'cooked'], ex: '전치사 for 뒤 → 동명사' },
        { q: '"너의 집은 어떠니?"를 바르게 영작한 것은?', opts: ['What is your home like?', 'How is your home like?', 'What is your home look?', 'How your home is like?'], ex: 'What is ~ like?: ~은 어떠니? (How와 like를 함께 쓰지 않는다)' }
      ]}
    ]
  }
  ]
};
