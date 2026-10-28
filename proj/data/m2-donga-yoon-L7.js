/* 중2 동아(윤정미) Lesson 7 · Let's Enjoy Festivals (본문: Seasonal Festivals Around the World)
   작성 규칙은 README.md 의 "데이터 작성 규칙". insert: given = 빠지는 문장 번호(0부터), odd = 어색한 문장 번호 */
window.PKG = {
  id: 'm2-donga-yoon-L7',
  school: '중2 동아(윤정미)',
  pick: true,
  unit: 'Lesson 7~8',
  title: 'Seasonal Festivals Around the World · Time Travel',
  titleKo: '전 세계의 계절 축제들',
  exam: '2학기 기말고사',
  prose: true,
  stepsBefore: ["핵심어휘·숙어", "어휘선택", "T/F 내용 확인", "어법선택", "동사변형", "오류찾기", "본문 스크램블", "문장순서", "문장삽입", "어색한 문장", "빈칸추론", "핵심문법"],   /* 일치·불일치 추가 전 단계 이름: 예전 기록을 새 단계에 맞추는 데 씀 */
  teacherPhone: '',            /* 결과 받을 번호. 예: '010-1234-5678' */

  days: [
  /* ═══════════════════════════ DAY 1 · 본문 ❶❷ ═══════════════════════════ */
  {
    id: 'd1', name: 'DAY 1', range: '7과 본문 ❶❷', story: '스페인 발렌시아의 파야스 축제 · 스웨덴의 한여름 축제',
    passage: [
      ['', '❶', ''],
      ['', 'Fallas Festival in Valencia, Spain', '스페인 발렌시아의 파야스 축제'],
      ['', 'People in Valencia celebrate the coming of spring with the Fallas festival.', '발렌시아 사람들은 파야스 축제로 봄의 시작을 축하한다.'],
      ['', 'This festival takes place from March 15 to 19.', '이 축제는 3월 15일부터 19일까지 열린다.'],
      ['', 'During the festival, people enjoy parades and fireworks.', '축제 기간 동안 사람들은 퍼레이드와 불꽃놀이를 즐긴다.'],
      ['', 'The stars of the festival are fallas, giant wooden statues.', '축제의 주인공은 거대한 나무 조각상인 파야들이다.'],
      ['', 'You can find hundreds of them all over the city.', '도시 곳곳에서 수백 개의 파야들을 볼 수 있다.'],
      ['', 'Surprisingly, the fallas are burned on the last day of the festival.', '놀랍게도, 축제의 마지막 날에는 이 파야들이 불태워진다.'],
      ['', 'Burning them symbolizes saying goodbye to old things and hello to a new start.', '그것들을 태우는 것은 오래된 것들과 작별하고 새로운 시작을 맞이하는 것을 상징한다.'],
      ['', '❷', ''],
      ['', 'Midsummer Festival in Sweden', '스웨덴의 한여름 축제'],
      ['', 'Winter in Sweden is long and dark, so the people there especially welcome summer.', '스웨덴의 겨울은 길고 어두워서 그곳 사람들은 여름을 특히 환영한다.'],
      ['', 'To celebrate the longest day of the year, they have a special festival.', '일 년 중 낮이 가장 긴 날을 기념하기 위해 그들은 특별한 축제를 연다.'],
      ['', 'They call it the Midsummer festival.', '이 축제를 한여름 축제라고 부른다.'],
      ['', 'The festival starts on the Friday evening between June 19 and 25 and ends on the Sunday.', '축제는 6월 19일과 25일 사이의 금요일 저녁에 시작하여 일요일에 끝난다.'],
      ['', 'During the festival, people decorate a tall pole with flowers and green leaves and enjoy traditional dances around it.', '축제 기간 동안 사람들은 꽃과 초록색 잎으로 장대를 장식하고 그 주위를 돌며 전통 춤을 즐긴다.'],
      ['', 'Because the sun hardly sets at this time of year in Sweden, people can enjoy the festival all night long.', '스웨덴에서 매년 이맘때면 해가 거의 지지 않기 때문에 사람들은 밤새도록 축제를 즐길 수 있다.']
    ],
    steps: [
      { type: 'vocab', title: '핵심어휘·숙어', quizN: 15, items: [
        ['seasonal', '계절적인, 계절의'], ['festival', '축제'], ['celebrate', '축하하다, 기념하다'], ['coming', '시작, 도래'],
        ['take place', '열리다, 개최되다'], ['parade', '퍼레이드, 행진'], ['fireworks', '불꽃놀이'], ['star', '주인공; 별'],
        ['giant', '거대한'], ['wooden', '나무로 된'], ['statue', '조각상'], ['hundreds of', '수백의'],
        ['all over', '~ 곳곳에'], ['surprisingly', '놀랍게도'], ['burn', '태우다'], ['last', '마지막의'],
        ['symbolize', '상징하다'], ['say goodbye to', '~에게 작별 인사를 하다'], ['midsummer', '한여름'], ['especially', '특히'],
        ['welcome', '환영하다, 반기다'], ['call A B', 'A를 B라고 부르다'], ['between A and B', 'A와 B 사이에'], ['end', '끝나다'],
        ['decorate', '장식하다, 꾸미다'], ['pole', '기둥, 막대기'], ['traditional', '전통의, 전통적인'], ['hardly', '거의 ~ 않다'],
        ['set', '(해가) 지다'], ['all night long', '밤새도록']
      ]},
      { type: 'pick', title: '어휘선택', guide: '문맥에 맞는 낱말을 고르세요.', items: [
        { s: 'People in Valencia {celebrate|forget} the coming of spring with the Fallas festival.', ex: 'celebrate: 축하하다, 기념하다' },
        { s: 'This festival {takes place|takes care} from March 15 to 19.', ex: 'take place: 열리다, 개최되다' },
        { s: 'During the festival, people enjoy parades and {fireworks|homework}.', ex: 'fireworks: 불꽃놀이' },
        { s: 'The stars of the festival are fallas, {giant|tiny} wooden statues.', ex: 'giant: 거대한 (tiny: 아주 작은)' },
        { s: 'Surprisingly, the fallas are burned on the {last|first} day of the festival.', ex: '축제의 마지막(last) 날에 태운다.' },
        { s: 'Burning them symbolizes saying {goodbye|hello} to old things and hello to a new start.', ex: '오래된 것에는 작별(goodbye), 새 시작에는 인사(hello)' },
        { s: 'Winter in Sweden is long and {dark|bright}, so the people there especially welcome summer.', ex: '겨울이 길고 어두워서 여름을 반긴다.' },
        { s: 'To celebrate the {longest|shortest} day of the year, they have a special festival.', ex: '한여름 축제는 낮이 가장 긴 날을 기념한다.' },
        { s: 'During the festival, people {decorate|destroy} a tall pole with flowers and green leaves and enjoy traditional dances around it.', ex: 'decorate: 장식하다' },
        { s: 'Because the sun {hardly|always} sets at this time of year in Sweden, people can enjoy the festival all night long.', ex: 'hardly: 거의 ~ 않다 → 해가 거의 지지 않아 밤새 즐긴다.' }
      ]},
      { type: 'tf', title: 'T/F 내용 확인', guide: '본문 내용과 일치하면 T, 다르면 F를 고르세요.', items: [
        ['The Fallas festival celebrates the coming of spring.', true, 'celebrate the coming of spring'],
        ['The Fallas festival takes place in May.', false, '3월 15일부터 19일까지 열린다.'],
        ['Fallas are giant wooden statues.', true, 'fallas, giant wooden statues'],
        ['The fallas are kept in a museum after the festival.', false, '축제 마지막 날에 불태워진다.'],
        ['Burning the fallas symbolizes a new start.', true, '새로운 시작을 맞이하는 것을 상징한다.'],
        ['Winter in Sweden is short and warm.', false, '스웨덴의 겨울은 길고 어둡다.'],
        ['The Midsummer festival starts on a Friday evening.', true, 'starts on the Friday evening'],
        ['The sun sets early during the Midsummer festival.', false, '해가 거의 지지 않는다(hardly sets).']
      ]},
      { type: 'mc', title: '일치·불일치', guide: "본문을 읽고 내용과 맞는지 확인해요. 틀린 선택지는 해설의 근거 문장과 비교해 보세요.", items: [
        { n: "❶", box: ["❶"], q: "파야스 축제에 관한 내용과 일치하지 <u>않는</u> 것은?", opts: ["The fallas are burned on the first day of the festival.", "The Fallas festival celebrates the coming of spring.", "The festival takes place from March 15 to 19.", "People enjoy parades and fireworks during the festival.", "The fallas are giant wooden statues."], ex: "정답 근거: Surprisingly, the fallas are burned on the last day of the festival.\n· take place : 열리다 · statue : 조각상 · burn : 태우다 · symbolize : 상징하다", per: [["파야는 축제 첫날에 불태워진다.", "the fallas are burned on the last day of the festival", "불일치 → 마지막 날"], ["파야스 축제는 봄이 오는 것을 축하한다.", "celebrate the coming of spring", "일치"], ["축제는 3월 15일부터 19일까지 열린다.", "takes place from March 15 to 19", "일치"], ["축제 동안 사람들은 퍼레이드와 불꽃놀이를 즐긴다.", "people enjoy parades and fireworks", "일치"], ["파야는 거대한 나무 조각상이다.", "fallas, giant wooden statues", "일치"]] },
        { n: "❷", box: ["❷"], q: "한여름 축제에 관한 내용과 <u>일치하는</u> 것은?", opts: ["People in Sweden can enjoy the festival all night long.", "Winter in Sweden is short and bright.", "The festival celebrates the shortest day of the year.", "The festival starts on Sunday morning.", "People decorate a tall pole with candles."], ex: "정답 근거: Because the sun hardly sets ..., people can enjoy the festival all night long.\n· hardly : 거의 ~않다 · set : (해가) 지다 · decorate : 장식하다 · all night long : 밤새도록", per: [["스웨덴 사람들은 밤새도록 축제를 즐길 수 있다.", "people can enjoy the festival all night long", "일치"], ["스웨덴의 겨울은 짧고 밝다.", "Winter in Sweden is long and dark", "불일치 → 길고 어두움"], ["축제는 일 년 중 낮이 가장 짧은 날을 기념한다.", "To celebrate the longest day of the year", "불일치 → 가장 긴 날"], ["축제는 일요일 아침에 시작한다.", "starts on the Friday evening", "불일치 → 금요일 저녁에 시작해서 일요일에 끝남"], ["사람들은 장대를 양초로 장식한다.", "decorate a tall pole with flowers and green leaves", "불일치 → 꽃과 초록 잎"]] }
      ]},
      { type: 'pick', title: '어법선택', guide: '어법상 알맞은 것을 고르세요.', items: [
        { s: 'People in Valencia {celebrate|celebrates} the coming of spring with the Fallas festival.', ex: '주어는 People(복수). in Valencia는 꾸며 주는 말 → celebrate' },
        { s: 'This festival {takes|take} place from March 15 to 19.', ex: '주어 This festival은 단수 → takes' },
        { s: 'The stars of the festival {are|is} fallas, giant wooden statues.', ex: '주어는 The stars(복수) → are' },
        { s: 'You can find {hundreds|hundred} of them all over the city.', ex: 'hundreds of: 수백의' },
        { s: 'Surprisingly, the fallas {are burned|burn} on the last day of the festival.', ex: '파야는 태워지는 것 → 수동태 are burned' },
        { s: 'Burning them {symbolizes|symbolize} saying goodbye to old things and hello to a new start.', ex: '동명사 주어는 단수 → symbolizes' },
        { s: 'Winter in Sweden is long and dark, {so|because} the people there especially welcome summer.', ex: '앞이 원인, 뒤가 결과 → so' },
        { s: '{To celebrate|Celebrate} the longest day of the year, they have a special festival.', ex: '목적(~하기 위해) → To celebrate' },
        { s: 'They call {it the Midsummer festival|the Midsummer festival it}.', ex: 'call A B: A를 B라고 부르다' },
        { s: 'The festival starts on the Friday evening between June 19 and 25 and {ends|end} on the Sunday.', ex: 'starts와 병렬 → ends' },
        { s: '{Because|So} the sun hardly sets at this time of year in Sweden, people can enjoy the festival all night long.', ex: '앞이 이유 → Because' }
      ]},
      { type: 'verb', title: '동사변형', guide: '( ) 안의 동사를 알맞은 형태로 바꿔 쓰세요.', items: [
        { s: 'People in Valencia ___ the coming of spring with the Fallas festival.', v: 'celebrate', a: ['celebrate'], ex: '복수 주어 People → celebrate' },
        { s: 'This festival ___ place from March 15 to 19.', v: 'take', a: ['takes'], ex: '단수 주어 → takes' },
        { s: 'Surprisingly, the fallas are ___ on the last day of the festival.', v: 'burn', a: ['burned', 'burnt'], ex: '수동태 be + 과거분사 (본문: burned)' },
        { s: '___ them symbolizes saying goodbye to old things and hello to a new start.', v: 'burn', a: ['Burning'], ex: '주어 자리 → 동명사 Burning' },
        { s: 'Burning them ___ saying goodbye to old things and hello to a new start.', v: 'symbolize', a: ['symbolizes'], ex: '동명사 주어는 단수 → symbolizes' },
        { s: 'Burning them symbolizes ___ goodbye to old things and hello to a new start.', v: 'say', a: ['saying'], ex: '동사의 목적어 → 동명사 saying' },
        { s: '___ the longest day of the year, they have a special festival.', v: 'celebrate', a: ['To celebrate'], ex: '목적(~하기 위해) → To celebrate' },
        { s: 'The festival ___ on the Friday evening between June 19 and 25 and ends on the Sunday.', v: 'start', a: ['starts'], ex: '단수 주어 → starts' },
        { s: 'During the festival, people ___ a tall pole with flowers and green leaves and enjoy traditional dances around it.', v: 'decorate', a: ['decorate'], ex: '복수 주어 people → decorate' },
        { s: 'Because the sun hardly ___ at this time of year in Sweden, people can enjoy the festival all night long.', v: 'set', a: ['sets'], ex: '단수 주어 the sun → sets' }
      ]},
      { type: 'error', title: '오류찾기', guide: '어법상 틀린 곳을 고르세요.', items: [
        { s: 'People in Valencia [[celebrates]] the coming of spring [[with]] the Fallas festival. This festival [[takes]] place [[from]] March 15 to 19.', w: 0, fix: 'celebrate', ex: '주어 People은 복수 → celebrate' },
        { s: 'The stars of the festival [[is]] fallas, [[giant]] wooden statues. You can find [[hundreds]] of them [[all over]] the city.', w: 0, fix: 'are', ex: '주어 The stars는 복수 → are' },
        { s: 'Surprisingly, the fallas [[burn]] on the [[last]] day of the festival. [[Burning]] them [[symbolizes]] saying goodbye to old things.', w: 0, fix: 'are burned', ex: '파야는 태워지는 것 → 수동태 are burned' },
        { s: 'Burning them [[symbolize]] [[saying]] goodbye [[to]] old things and hello to [[a new start]].', w: 0, fix: 'symbolizes', ex: '동명사 주어는 단수 → symbolizes' },
        { s: 'Winter in Sweden [[is]] long and dark, [[because]] the people there [[especially]] [[welcome]] summer.', w: 1, fix: 'so', ex: '앞이 원인, 뒤가 결과 → so' },
        { s: '[[Celebrate]] the [[longest]] day of the year, they [[have]] a special festival. They [[call]] it the Midsummer festival.', w: 0, fix: 'To celebrate', ex: '목적(~하기 위해) → To celebrate' },
        { s: 'The festival [[starts]] on the Friday evening [[between]] June 19 and 25 and [[end]] on the Sunday.', w: 2, fix: 'ends', ex: 'starts와 병렬 → ends' },
        { s: 'Because the sun hardly [[set]] at this time of year in Sweden, people [[can]] [[enjoy]] the festival [[all night long]].', w: 0, fix: 'sets', ex: '주어 the sun은 단수 → sets' }
      ]},
      { type: 'scramble', title: '본문 스크램블', guide: '우리말에 맞게 단어를 눌러 문장을 완성하세요.', items: [
        { ko: '이 축제는 3월 15일부터 19일까지 열린다.', en: 'This festival takes place from March 15 to 19.' },
        { ko: '축제 기간 동안 사람들은 퍼레이드와 불꽃놀이를 즐긴다.', en: 'During the festival, people enjoy parades and fireworks.' },
        { ko: '도시 곳곳에서 수백 개의 파야들을 볼 수 있다.', en: 'You can find hundreds of them all over the city.' },
        { ko: '놀랍게도, 축제의 마지막 날에는 이 파야들이 불태워진다.', en: 'Surprisingly, the fallas are burned on the last day of the festival.' },
        { ko: '일 년 중 낮이 가장 긴 날을 기념하기 위해 그들은 특별한 축제를 연다.', en: 'To celebrate the longest day of the year, they have a special festival.' },
        { ko: '이 축제를 한여름 축제라고 부른다.', en: 'They call it the Midsummer festival.' },
        { ko: '사람들은 밤새도록 축제를 즐길 수 있다.', en: 'people can enjoy the festival all night long.' }
      ]},
      { type: 'order', title: '문장순서', guide: '문장을 본문 순서대로 눌러서 배열하세요.', items: [
        { lines: [
          'People in Valencia celebrate the coming of spring with the Fallas festival.',
          'This festival takes place from March 15 to 19.',
          'During the festival, people enjoy parades and fireworks.',
          'The stars of the festival are fallas, giant wooden statues.'
        ]},
        { lines: [
          'The stars of the festival are fallas, giant wooden statues.',
          'You can find hundreds of them all over the city.',
          'Surprisingly, the fallas are burned on the last day of the festival.',
          'Burning them symbolizes saying goodbye to old things and hello to a new start.'
        ]},
        { lines: [
          'Winter in Sweden is long and dark, so the people there especially welcome summer.',
          'To celebrate the longest day of the year, they have a special festival.',
          'They call it the Midsummer festival.',
          'The festival starts on the Friday evening between June 19 and 25 and ends on the Sunday.'
        ]},
        { lines: [
          'They call it the Midsummer festival.',
          'The festival starts on the Friday evening between June 19 and 25 and ends on the Sunday.',
          'During the festival, people decorate a tall pole with flowers and green leaves and enjoy traditional dances around it.',
          'Because the sun hardly sets at this time of year in Sweden, people can enjoy the festival all night long.'
        ]}
      ]},
      { type: 'insert', title: '문장삽입', guide: '주어진 문장이 들어가기에 가장 알맞은 곳을 고르세요.', items: [
        { lines: [
          'During the festival, people enjoy parades and fireworks.',
          'The stars of the festival are fallas, giant wooden statues.',
          'You can find hundreds of them all over the city.',
          'Surprisingly, the fallas are burned on the last day of the festival.',
          'Burning them symbolizes saying goodbye to old things and hello to a new start.'
        ], given: 2, ex: 'them은 바로 앞 문장의 fallas(거대한 나무 조각상)를 가리킨다.' },
        { lines: [
          'The stars of the festival are fallas, giant wooden statues.',
          'You can find hundreds of them all over the city.',
          'Surprisingly, the fallas are burned on the last day of the festival.',
          'Burning them symbolizes saying goodbye to old things and hello to a new start.'
        ], given: 3, ex: '파야를 태운다는 내용 다음에 그 의미(상징)가 온다.' },
        { lines: [
          'Winter in Sweden is long and dark, so the people there especially welcome summer.',
          'To celebrate the longest day of the year, they have a special festival.',
          'They call it the Midsummer festival.',
          'The festival starts on the Friday evening between June 19 and 25 and ends on the Sunday.'
        ], given: 2, ex: 'it은 앞 문장의 a special festival을 가리킨다.' }
      ]},
      { type: 'odd', title: '어색한 문장', guide: '글의 흐름과 관계없는 문장을 고르세요.', items: [
        { lines: [
          'People in Valencia celebrate the coming of spring with the Fallas festival.',
          'This festival takes place from March 15 to 19.',
          'The festival is held in the middle of winter.',
          'During the festival, people enjoy parades and fireworks.'
        ], odd: 2, ex: '봄의 시작을 축하하는 3월 축제라는 내용과 맞지 않는다.' },
        { lines: [
          'The stars of the festival are fallas, giant wooden statues.',
          'You can find hundreds of them all over the city.',
          'Surprisingly, the fallas are burned on the last day of the festival.',
          'People keep the fallas for many years.',
          'Burning them symbolizes saying goodbye to old things and hello to a new start.'
        ], odd: 3, ex: '파야는 축제 마지막 날 불태워진다.' },
        { lines: [
          'Winter in Sweden is long and dark, so the people there especially welcome summer.',
          'To celebrate the longest day of the year, they have a special festival.',
          "People in Sweden don't like summer at all.",
          'They call it the Midsummer festival.'
        ], odd: 2, ex: '스웨덴 사람들은 여름을 특히 반긴다.' }
      ]},
      { type: 'blank', title: '빈칸추론', guide: '빈칸에 들어갈 말로 가장 알맞은 것을 고르세요.', items: [
        { s: 'Surprisingly, the fallas ____ on the last day of the festival.', opts: ['are burned', 'are sold', 'are built', 'are painted'], ex: '놀랍게도 마지막 날에 파야를 불태운다.' },
        { s: 'Burning them symbolizes saying goodbye to old things and hello to ____.', opts: ['a new start', 'old friends', 'the winter', 'the city'], ex: '오래된 것과 작별하고 새로운 시작을 맞이한다.' },
        { s: 'Winter in Sweden is long and dark, so the people there especially ____.', opts: ['welcome summer', 'hate summer', 'miss winter', 'stay home'], ex: '겨울이 길고 어두워서 여름을 특히 반긴다.' },
        { s: 'Because the sun ____ at this time of year in Sweden, people can enjoy the festival all night long.', opts: ['hardly sets', 'sets early', 'never rises', 'is very hot'], ex: '해가 거의 지지 않아 밤새 축제를 즐길 수 있다.' }
      ]},
      { type: 'mc', title: '핵심문법', guide: '알맞은 답을 고르세요.', items: [
        { q: '"파야들은 마지막 날에 불태워진다."를 바르게 영작한 것은?', opts: ['The fallas are burned on the last day.', 'The fallas burn on the last day.', 'The fallas are burn on the last day.', 'The fallas is burned on the last day.'], ex: '수동태: be동사 + 과거분사, 주어 복수 → are burned' },
        { q: '빈칸에 알맞은 것은?<br><b>People in Valencia ______ the coming of spring.</b>', opts: ['celebrate', 'celebrates', 'celebrating', 'to celebrate'], ex: '주어 People(복수) → celebrate. in Valencia는 수에 영향 없음' },
        { q: '빈칸에 알맞은 것은?<br><b>Burning them ______ a new start.</b>', opts: ['symbolizes', 'symbolize', 'symbolizing', 'to symbolize'], ex: '동명사 주어는 단수 취급' },
        { q: '"그들은 그것을 한여름 축제라고 부른다."를 바르게 영작한 것은?', opts: ['They call it the Midsummer festival.', 'They call the Midsummer festival it.', 'They it call the Midsummer festival.', 'They call to it the Midsummer festival.'], ex: 'call A B: A를 B라고 부르다' },
        { q: '빈칸에 들어갈 수 <b>없는</b> 것은?<br><b>We ______ our dog Max.</b>', opts: ['gave', 'call', 'named', 'called'], ex: 'call·name + 목적어 + 명사(~라고 부르다/이름 짓다). gave는 이 뜻으로 쓸 수 없다.' },
        { q: '밑줄 친 to부정사가 <b>"~하기 위해"</b>의 뜻으로 쓰인 것은?', opts: ['<u>To celebrate</u> the longest day, they have a festival.', 'I want <u>to celebrate</u> my birthday.', 'It is fun <u>to celebrate</u> festivals.', 'They decided <u>to celebrate</u> together.'], ex: '①만 목적(~하기 위해). 나머지는 목적어·진주어' },
        { q: '빈칸에 알맞은 것은?<br><b>Winter is long and dark, ______ people welcome summer.</b>', opts: ['so', 'because', 'but', 'or'], ex: '원인, so + 결과' },
        { q: '다음 문장의 뜻으로 알맞은 것은?<br><b>The sun hardly sets.</b>', opts: ['해가 거의 지지 않는다.', '해가 힘들게 진다.', '해가 일찍 진다.', '해가 반드시 진다.'], ex: 'hardly: 거의 ~ 않다 (hard: 열심히/어려운과 구별)' },
        { q: '빈칸에 알맞은 것은?<br><b>This festival takes place ______ March 15 to 19.</b>', opts: ['from', 'between', 'at', 'since'], ex: 'from A to B: A부터 B까지' }
      ]}
    ]
  },

  /* ═══════════════════════════ DAY 2 · 본문 ❸❹ ═══════════════════════════ */
  {
    id: 'd2', name: 'DAY 2', range: '7과 본문 ❸❹', story: '멕시코의 망자의 날 · 알래스카의 퍼 론디 축제',
    passage: [
      ['', '❸', ''],
      ['', 'Day of the Dead Festival in Mexico', '멕시코의 망자의 날 축제'],
      ['', 'Many Mexicans believe that once a year dead people come back home to meet their family and friends.', '많은 멕시코 사람들은 일 년에 한 번 죽은 사람들이 가족과 친구들을 만나기 위해 집으로 돌아온다고 믿는다.'],
      ['', 'They call this day the Day of the Dead.', '이날을 망자의 날이라고 부른다.'],
      ['', 'To welcome dead people, Mexicans hold a festival on November 1 and 2.', '죽은 이들을 맞이하기 위해, 멕시코 사람들은 11월 1일과 2일에 축제를 연다.'],
      ['', 'They believe it is important to remember dead people.', '그들은 고인을 기억하는 것이 중요하다고 믿는다.'],
      ['', 'So, people set up altars in their homes and have big parties in cemeteries.', '그래서 사람들은 집에 제단을 차리고, 묘지에서 큰 파티를 연다.'],
      ['', 'In some areas, people dress up like skeletons and hold big parades.', '일부 지역에서는 사람들이 해골처럼 분장하고 대규모 퍼레이드를 벌인다.'],
      ['', '❹', ''],
      ['', 'Fur Rondy Festival in Alaska, USA', '미국 알래스카의 퍼 론디 축제'],
      ['', 'At the end of February, people in Alaska hold the Fur Rondy festival, one of the biggest winter festivals in the world.', '2월 말, 알래스카 사람들은 세계에서 가장 큰 겨울 축제 중 하나인 퍼 론디 축제를 연다.'],
      ['', 'During this festival, visitors can enjoy various winter sports and Alaskan traditional games.', '이 축제 기간 동안 방문객들은 다양한 겨울 스포츠와 알래스카 전통 게임을 즐길 수 있다.'],
      ['', 'They can also enjoy many special events such as the Running of the Reindeer.', '또한, 순록 경주 같은 많은 특별한 행사도 즐길 수 있다.'],
      ['', 'People who participate in this race wear fun costumes and try to run faster than reindeer.', '이 경주에 참가하는 사람들은 재미있는 복장을 입고 순록보다 더 빨리 달리려고 애쓴다.'],
      ['', 'Is it possible to do so?', '과연 그럴 수 있을까?'],
      ['', "Not really, but it doesn't matter.", '그럴 것 같지는 않지만, 그것은 중요하지 않다.'],
      ['', 'Everyone is just having fun!', '모두가 그저 즐기고 있을 뿐이다!']
    ],
    steps: [
      { type: 'vocab', title: '핵심어휘·숙어', quizN: 15, items: [
        ['believe', '믿다'], ['once a year', '일 년에 한 번'], ['dead', '죽은'], ['come back home', '집에 돌아오다'],
        ['welcome', '맞이하다, 환영하다'], ['hold', '개최하다, 열다'], ['important', '중요한'], ['remember', '기억하다'],
        ['set up', '세우다, 설치하다'], ['altar', '제단'], ['cemetery', '묘지'], ['area', '지역'],
        ['dress up', '변장하다, 차려입다'], ['skeleton', '해골'], ['at the end of', '~의 말에, ~의 끝에'], ['February', '2월'],
        ['visitor', '방문객'], ['various', '다양한'], ['traditional', '전통의'], ['such as', '~와 같은'],
        ['reindeer', '순록'], ['participate in', '~에 참여하다'], ['race', '경주'], ['wear', '입다'],
        ['costume', '의상, 복장'], ['possible', '가능한'], ['matter', '중요하다'], ['have fun', '즐기다, 재미있게 보내다']
      ]},
      { type: 'pick', title: '어휘선택', guide: '문맥에 맞는 낱말을 고르세요.', items: [
        { s: 'Many Mexicans believe that {once|twice} a year dead people come back home to meet their family and friends.', ex: 'once a year: 일 년에 한 번' },
        { s: 'Many Mexicans believe that once a year dead people come back home to {meet|forget} their family and friends.', ex: '가족과 친구를 만나기(meet) 위해 돌아온다.' },
        { s: 'To welcome dead people, Mexicans {hold|cancel} a festival on November 1 and 2.', ex: 'hold: (행사를) 열다' },
        { s: 'They believe it is important to {remember|forget} dead people.', ex: 'remember: 기억하다' },
        { s: 'So, people set up {altars|tents} in their homes and have big parties in cemeteries.', ex: 'altar: 제단' },
        { s: 'In some areas, people dress up like {skeletons|princesses} and hold big parades.', ex: 'skeleton: 해골' },
        { s: 'At the {end|beginning} of February, people in Alaska hold the Fur Rondy festival, one of the biggest winter festivals in the world.', ex: 'at the end of: ~의 말에' },
        { s: 'People who {participate|watch} in this race wear fun costumes and try to run faster than reindeer.', ex: 'participate in: ~에 참여하다' },
        { s: 'People who participate in this race wear fun costumes and try to run {faster|slower} than reindeer.', ex: '순록보다 빨리(faster) 달리려고 애쓴다.' },
        { s: "Not really, but it doesn't {matter|work}.", ex: 'matter: 중요하다' }
      ]},
      { type: 'tf', title: 'T/F 내용 확인', guide: '본문 내용과 일치하면 T, 다르면 F를 고르세요.', items: [
        ['Many Mexicans believe dead people come back home once a year.', true, 'once a year dead people come back home'],
        ['The Day of the Dead festival is held in October.', false, '11월 1일과 2일에 열린다.'],
        ['People in Mexico have big parties in cemeteries.', true, 'have big parties in cemeteries'],
        ['In some areas, people dress up like animals.', false, '해골(skeletons)처럼 분장한다.'],
        ['The Fur Rondy festival is held at the end of February.', true, 'At the end of February'],
        ['Visitors can enjoy Alaskan traditional games.', true, 'Alaskan traditional games'],
        ['People in the race try to run slower than reindeer.', false, '순록보다 빨리 달리려고 한다.'],
        ['Most people in the race can run faster than reindeer.', false, 'Not really (그렇지 않다)']
      ]},
      { type: 'mc', title: '일치·불일치', guide: "본문을 읽고 내용과 맞는지 확인해요. 틀린 선택지는 해설의 근거 문장과 비교해 보세요.", items: [
        { n: "❸", box: ["❸"], q: "망자의 날에 관한 내용과 일치하지 <u>않는</u> 것은?", opts: ["The Day of the Dead festival is held in October.", "Many Mexicans believe dead people come back home once a year.", "Mexicans think it is important to remember dead people.", "People set up altars in their homes.", "In some areas, people dress up like skeletons."], ex: "정답 근거: To welcome dead people, Mexicans hold a festival on November 1 and 2.\n· hold : 열다 · set up : 차리다 · altar : 제단 · cemetery : 묘지 · skeleton : 해골", per: [["망자의 날 축제는 10월에 열린다.", "hold a festival on November 1 and 2", "불일치 → 11월 1일과 2일"], ["많은 멕시코 사람들은 고인이 일 년에 한 번 집에 돌아온다고 믿는다.", "once a year dead people come back home", "일치"], ["멕시코 사람들은 고인을 기억하는 것이 중요하다고 생각한다.", "it is important to remember dead people", "일치"], ["사람들은 집에 제단을 차린다.", "people set up altars in their homes", "일치"], ["일부 지역에서는 사람들이 해골처럼 분장한다.", "people dress up like skeletons", "일치"]] },
        { n: "❹", box: ["❹"], q: "퍼 론디 축제에 관한 내용과 <u>일치하는</u> 것은?", opts: ["People in the race try to run faster than reindeer.", "The festival is held at the beginning of February.", "Fur Rondy is one of the smallest winter festivals.", "Visitors can only enjoy winter sports.", "People usually win the race against reindeer."], ex: "정답 근거: People who participate in this race wear fun costumes and try to run faster than reindeer.\n· participate in : ~에 참가하다 · costume : 의상 · reindeer : 순록 · It doesn't matter. : 중요하지 않다", per: [["경주에 참가한 사람들은 순록보다 빨리 달리려고 한다.", "try to run faster than reindeer", "일치"], ["축제는 2월 초에 열린다.", "At the end of February", "불일치 → 2월 말"], ["퍼 론디는 가장 작은 겨울 축제 중 하나이다.", "one of the biggest winter festivals in the world", "불일치 → 가장 큰 축제 중 하나"], ["방문객들은 겨울 스포츠만 즐길 수 있다.", "various winter sports and Alaskan traditional games", "불일치 → 전통 게임도 즐김"], ["사람들은 보통 순록과의 경주에서 이긴다.", "Not really, but it doesn't matter", "불일치 → 이기기 어렵지만 상관없음"]] }
      ]},
      { type: 'pick', title: '어법선택', guide: '어법상 알맞은 것을 고르세요.', items: [
        { s: 'Many Mexicans believe {that|what} once a year dead people come back home to meet their family and friends.', ex: '뒤에 완전한 문장 → 접속사 that' },
        { s: 'Many Mexicans believe that once a year dead people come back home {to meet|meeting} their family and friends.', ex: '목적(~하기 위해) → to meet' },
        { s: 'They call {this day the Day of the Dead|the Day of the Dead this day}.', ex: 'call A B: A를 B라고 부르다' },
        { s: 'They believe {it|this} is important to remember dead people.', ex: '가주어 it ~ 진주어 to부정사' },
        { s: 'They believe it is important {to remember|remember} dead people.', ex: '가주어 it ~ 진주어 to remember' },
        { s: 'So, people set up altars in their homes and {have|has} big parties in cemeteries.', ex: '복수 주어 people → have' },
        { s: 'At the end of February, people in Alaska hold the Fur Rondy festival, one of the biggest winter {festivals|festival} in the world.', ex: 'one of the + 최상급 + 복수명사' },
        { s: 'At the end of February, people in Alaska hold the Fur Rondy festival, one of the {biggest|bigger} winter festivals in the world.', ex: 'one of the + 최상급' },
        { s: 'People {who|which} participate in this race wear fun costumes and try to run faster than reindeer.', ex: '사람을 꾸미는 관계대명사 → who' },
        { s: 'People who participate in this race {wear|wears} fun costumes and try to run faster than reindeer.', ex: '주어 People(복수) → wear' },
        { s: 'Is it possible {to do|do} so?', ex: '가주어 it ~ 진주어 to do' },
        { s: 'Everyone {is|are} just having fun!', ex: 'everyone은 단수 취급 → is' }
      ]},
      { type: 'verb', title: '동사변형', guide: '( ) 안의 동사를 알맞은 형태로 바꿔 쓰세요.', items: [
        { s: 'Many Mexicans ___ that once a year dead people come back home to meet their family and friends.', v: 'believe', a: ['believe'], ex: '복수 주어 → believe' },
        { s: 'Many Mexicans believe that once a year dead people come back home ___ their family and friends.', v: 'meet', a: ['to meet'], ex: '목적(~하기 위해) → to meet' },
        { s: '___ dead people, Mexicans hold a festival on November 1 and 2.', v: 'welcome', a: ['To welcome'], ex: '목적(~하기 위해) → To welcome' },
        { s: 'They believe it is important ___ dead people.', v: 'remember', a: ['to remember'], ex: '가주어 it ~ 진주어 to부정사' },
        { s: 'In some areas, people ___ up like skeletons and hold big parades.', v: 'dress', a: ['dress'], ex: '복수 주어 → dress' },
        { s: 'At the end of February, people in Alaska ___ the Fur Rondy festival, one of the biggest winter festivals in the world.', v: 'hold', a: ['hold'], ex: '주어 people(복수) → hold' },
        { s: 'People who ___ in this race wear fun costumes and try to run faster than reindeer.', v: 'participate', a: ['participate'], ex: '선행사 People(복수) → participate' },
        { s: 'People who participate in this race wear fun costumes and try ___ faster than reindeer.', v: 'run', a: ['to run'], ex: 'try + to부정사: ~하려고 애쓰다' },
        { s: "Not really, but it doesn't ___.", v: 'matter', a: ['matter'], ex: "doesn't + 동사원형" },
        { s: 'Everyone is just ___ fun!', v: 'have', a: ['having'], ex: '현재진행형 is having' }
      ]},
      { type: 'error', title: '오류찾기', guide: '어법상 틀린 곳을 고르세요.', items: [
        { s: 'Many Mexicans believe [[what]] once a year dead people [[come]] back home [[to meet]] their family [[and]] friends.', w: 0, fix: 'that', ex: '뒤에 완전한 문장 → 접속사 that' },
        { s: 'They [[call]] this day the Day of the Dead. [[Welcome]] dead people, Mexicans [[hold]] a festival [[on]] November 1 and 2.', w: 1, fix: 'To welcome', ex: '목적(~하기 위해) → To welcome' },
        { s: 'They believe it [[is]] important [[remember]] dead people. So, people [[set up]] altars [[in]] their homes.', w: 1, fix: 'to remember', ex: '가주어 it ~ 진주어 to부정사' },
        { s: 'So, people set up altars in their homes and [[has]] big parties [[in]] cemeteries. In some areas, people [[dress up]] [[like]] skeletons.', w: 0, fix: 'have', ex: '복수 주어 people → have' },
        { s: 'people in Alaska [[hold]] the Fur Rondy festival, one of the [[biggest]] winter [[festival]] [[in]] the world.', w: 2, fix: 'festivals', ex: 'one of the + 최상급 + 복수명사' },
        { s: 'People [[which]] participate in this race [[wear]] fun costumes and try [[to run]] [[faster]] than reindeer.', w: 0, fix: 'who', ex: '선행사가 사람 → who' },
        { s: "Is it [[possible]] [[do]] so? Not really, but it [[doesn't]] matter. Everyone [[is]] just having fun!", w: 1, fix: 'to do', ex: '가주어 it ~ 진주어 to부정사' }
      ]},
      { type: 'scramble', title: '본문 스크램블', guide: '우리말에 맞게 단어를 눌러 문장을 완성하세요.', items: [
        { ko: '그들은 이날을 망자의 날이라고 부른다.', en: 'They call this day the Day of the Dead.' },
        { ko: '그들은 고인을 기억하는 것이 중요하다고 믿는다.', en: 'They believe it is important to remember dead people.' },
        { ko: '일부 지역에서는 사람들이 해골처럼 분장하고 대규모 퍼레이드를 벌인다.', en: 'In some areas, people dress up like skeletons and hold big parades.' },
        { ko: '이 축제 기간 동안 방문객들은 다양한 겨울 스포츠를 즐길 수 있다.', en: 'During this festival, visitors can enjoy various winter sports.' },
        { ko: '이 경주에 참가하는 사람들은 재미있는 복장을 입는다.', en: 'People who participate in this race wear fun costumes.' },
        { ko: '과연 그럴 수 있을까?', en: 'Is it possible to do so?' },
        { ko: '그럴 것 같지는 않지만, 그것은 중요하지 않다.', en: "Not really, but it doesn't matter." },
        { ko: '모두가 그저 즐기고 있을 뿐이다!', en: 'Everyone is just having fun!' }
      ]},
      { type: 'order', title: '문장순서', guide: '문장을 본문 순서대로 눌러서 배열하세요.', items: [
        { lines: [
          'Many Mexicans believe that once a year dead people come back home to meet their family and friends.',
          'They call this day the Day of the Dead.',
          'To welcome dead people, Mexicans hold a festival on November 1 and 2.',
          'They believe it is important to remember dead people.'
        ]},
        { lines: [
          'To welcome dead people, Mexicans hold a festival on November 1 and 2.',
          'They believe it is important to remember dead people.',
          'So, people set up altars in their homes and have big parties in cemeteries.',
          'In some areas, people dress up like skeletons and hold big parades.'
        ]},
        { lines: [
          'At the end of February, people in Alaska hold the Fur Rondy festival, one of the biggest winter festivals in the world.',
          'During this festival, visitors can enjoy various winter sports and Alaskan traditional games.',
          'They can also enjoy many special events such as the Running of the Reindeer.',
          'People who participate in this race wear fun costumes and try to run faster than reindeer.'
        ]},
        { lines: [
          'People who participate in this race wear fun costumes and try to run faster than reindeer.',
          'Is it possible to do so?',
          "Not really, but it doesn't matter.",
          'Everyone is just having fun!'
        ]}
      ]},
      { type: 'insert', title: '문장삽입', guide: '주어진 문장이 들어가기에 가장 알맞은 곳을 고르세요.', items: [
        { lines: [
          'Many Mexicans believe that once a year dead people come back home to meet their family and friends.',
          'They call this day the Day of the Dead.',
          'To welcome dead people, Mexicans hold a festival on November 1 and 2.',
          'They believe it is important to remember dead people.'
        ], given: 1, ex: 'this day는 앞 문장의 "죽은 사람들이 돌아오는 날"을 가리킨다.' },
        { lines: [
          'They believe it is important to remember dead people.',
          'So, people set up altars in their homes and have big parties in cemeteries.',
          'In some areas, people dress up like skeletons and hold big parades.'
        ], given: 1, ex: 'So(그래서) 앞에는 이유(고인을 기억하는 것이 중요함)가 온다.' },
        { lines: [
          'At the end of February, people in Alaska hold the Fur Rondy festival, one of the biggest winter festivals in the world.',
          'During this festival, visitors can enjoy various winter sports and Alaskan traditional games.',
          'They can also enjoy many special events such as the Running of the Reindeer.',
          'People who participate in this race wear fun costumes and try to run faster than reindeer.'
        ], given: 3, ex: 'this race는 앞 문장의 the Running of the Reindeer(순록 경주)를 가리킨다.' },
        { lines: [
          'People who participate in this race wear fun costumes and try to run faster than reindeer.',
          'Is it possible to do so?',
          "Not really, but it doesn't matter.",
          'Everyone is just having fun!'
        ], given: 2, ex: 'Not really는 "그럴 수 있을까?"라는 질문에 대한 대답이다.' }
      ]},
      { type: 'odd', title: '어색한 문장', guide: '글의 흐름과 관계없는 문장을 고르세요.', items: [
        { lines: [
          'To welcome dead people, Mexicans hold a festival on November 1 and 2.',
          'They believe it is important to remember dead people.',
          'So, they try to forget dead people quickly.',
          'So, people set up altars in their homes and have big parties in cemeteries.'
        ], odd: 2, ex: '고인을 기억하는 것이 중요하다는 흐름과 반대된다.' },
        { lines: [
          'So, people set up altars in their homes and have big parties in cemeteries.',
          'In some areas, people dress up like skeletons and hold big parades.',
          'Nobody goes outside during the festival.',
          'Many Mexicans believe that once a year dead people come back home to meet their family and friends.'
        ], odd: 2, ex: '파티와 퍼레이드를 하는 축제라는 내용과 맞지 않는다.' },
        { lines: [
          'During this festival, visitors can enjoy various winter sports and Alaskan traditional games.',
          'They can also enjoy many special events such as the Running of the Reindeer.',
          'The festival has no events for visitors.',
          'People who participate in this race wear fun costumes and try to run faster than reindeer.'
        ], odd: 2, ex: '특별한 행사를 즐길 수 있다는 내용과 반대된다.' },
        { lines: [
          'Is it possible to do so?',
          "Not really, but it doesn't matter.",
          'Only the winner can have fun in the race.',
          'Everyone is just having fun!'
        ], odd: 2, ex: '모두가 즐긴다는 내용과 맞지 않는다.' }
      ]},
      { type: 'blank', title: '빈칸추론', guide: '빈칸에 들어갈 말로 가장 알맞은 것을 고르세요.', items: [
        { s: 'Many Mexicans believe that once a year dead people ____ to meet their family and friends.', opts: ['come back home', 'go to school', 'leave the town', 'stay in the sky'], ex: '죽은 사람들이 가족을 만나러 집에 돌아온다고 믿는다.' },
        { s: 'They believe it is important ____ dead people.', opts: ['to remember', 'to forget', 'to scare', 'to leave'], ex: '고인을 기억하는 것이 중요하다고 믿는다.' },
        { s: 'At the end of February, people in Alaska hold the Fur Rondy festival, one of ____ in the world.', opts: ['the biggest winter festivals', 'the smallest summer parties', 'the oldest sports games', 'the hottest food markets'], ex: '세계에서 가장 큰 겨울 축제 중 하나' },
        { s: 'Everyone is just ____!', opts: ['having fun', 'feeling sad', 'running away', 'getting angry'], ex: '이기는 것보다 모두 즐기는 것이 중요하다.' }
      ]},
      { type: 'mc', title: '핵심문법', guide: '알맞은 답을 고르세요.', items: [
        { q: '빈칸에 알맞은 것은?<br><b>It is important ______ dead people.</b>', opts: ['to remember', 'remember', 'remembers', 'remembered'], ex: '가주어 It ~ 진주어 to부정사' },
        { q: '"그 경주에서 이기는 것은 어렵다."를 바르게 영작한 것은?', opts: ['It is hard to win the race.', 'It is hard win the race.', 'That is hard to win the race.', 'It is hard for win the race.'], ex: '가주어 It ~ 진주어 to win' },
        { q: '밑줄 친 <b>It</b>의 쓰임이 나머지와 <b>다른</b> 것은?', opts: ['<u>It</u> is my new bag.', '<u>It</u> is important to remember them.', '<u>It</u> is fun to dance together.', '<u>It</u> is possible to run fast.'], ex: '①은 "그것"(대명사). 나머지는 뒤의 to부정사를 대신하는 가주어' },
        { q: '빈칸에 알맞은 것은?<br><b>It is hard ______ me to run faster than reindeer.</b>', opts: ['for', 'of', 'to', 'with'], ex: 'to부정사의 의미상 주어: for + 목적격' },
        { q: '다음 문장과 형식이 같은 것은?<br><b>They call this day the Day of the Dead.</b>', opts: ['People call him a hero.', 'He gave me a book.', 'She looks happy.', 'I like dancing.'], ex: '동사 + 목적어 + 목적격 보어(명사): A를 B라고 부르다' },
        { q: '빈칸에 알맞은 것은?<br><b>It is one of the ______ in the world.</b>', opts: ['biggest festivals', 'biggest festival', 'bigger festivals', 'big festival'], ex: 'one of the + 최상급 + 복수명사' },
        { q: '빈칸에 알맞은 것은?<br><b>People ______ participate in this race wear fun costumes.</b>', opts: ['who', 'which', 'what', 'whose'], ex: '선행사가 사람, 주어 역할 → who' },
        { q: '빈칸에 알맞은 것은?<br><b>Everyone ______ just having fun!</b>', opts: ['is', 'are', 'be', 'were'], ex: 'everyone은 단수 취급' },
        { q: '빈칸에 알맞은 것은?<br><b>Mexicans hold a festival ______ dead people.</b>', opts: ['to welcome', 'welcome', 'welcomes', 'welcomed'], ex: '목적(~하기 위해) → to welcome' }
      ]}
    ]
  },
  { id: 'd3', name: 'DAY 3', range: '8과 본문 ❶❷❸', story: 'Lesson 8 · Time Travel 사무실 · 시간 여행의 규칙 · 안개 속 정글', passage: [['', '❶', ''], ['', 'Eckels walked into the office of Time Travel.', 'Eckels는 Time Travel의 사무실로 걸어 들어갔다.'], ['', 'The big sign on the wall said, "NAME ANY YEAR IN THE PAST. WE TAKE YOU THERE."', '벽에 걸린 큰 간판에는 “과거의 어느 연도든 말씀하세요. 우리가 당신을 그곳으로 모시겠습니다.”라고 쓰여 있었다.'], ['', 'There was a TV on the wall, and Mr. Keith, the new president, was on the news.', '벽에는 TV가 있었고, 새 대통령인 Keith 씨가 뉴스에 나오고 있었다.'], ['', '"How can we help you?" said Mr. Parker, the founder of Time Travel.', '“무엇을 도와드릴까요?” Time Travel의 설립자인 Parker 씨가 말했다.'], ['', '"I\'ve always wanted to see a dinosaur. Is it possible?" asked Eckels.', '“저는 항상 공룡을 보고 싶었어요. 가능한가요?” Eckels가 물었다.'], ['', '"Sure," said Mr. Parker.', '“물론이죠.” Parker 씨가 대답했다.'], ['', '"We can take you back to the jungle of 60 million years ago."', '“당신을 6천만 년 전의 정글로 데려다줄 수 있습니다.”'], ['', '"Great," said Eckels. "Can you take me there now?"', '“멋지군요.” Eckels가 말했다. “지금 저를 그곳에 데려가 줄 수 있나요?”'], ['', '"You\'re lucky. There\'s a time machine that leaves in 10 minutes," said Mr. Parker.', '“운이 좋으시네요. 10분 후에 출발하는 타임머신이 있습니다.” Parker 씨가 말했다.'], ['', '"This is Travis, your travel guide," he continued.', '“이분은 당신의 여행 안내원인 Travis입니다.” 그는 계속 말했다.'], ['', '"To stay safe, you must follow his instructions."', '“안전하려면 그의 지시를 반드시 따라야 합니다.”'], ['', '❷', ''], ['', 'Inside the time machine, there were two other travelers.', '타임머신 안에는 다른 여행자 두 명이 있었다.'], ['', 'Eckels sat down and closed his eyes.', 'Eckels는 자리에 앉아 눈을 감았다.'], ['', 'He felt the machine moving under his feet.', '그는 발밑에서 타임머신이 움직이는 것을 느꼈다.'], ['', 'After only a few minutes, the machine stopped.', '불과 몇 분 지나지 않아 타임머신이 멈췄다.'], ['', '"We\'ve just arrived in the jungle of 60 million years ago," Travis explained.', '“우리는 이제 막 6천만 년 전 정글에 도착했습니다.” Travis가 설명했다.'], ['', '"Do you see the path over there?', '“저쪽에 길이 보이십니까?'], ['', 'You must not leave it at any time.', '어떤 경우에도 저 길을 절대 벗어나면 안 됩니다.'], ['', 'Do not touch anything.', '아무것도 만지지 마세요.'], ['', 'You might kill something by accident.', '여러분이 실수로 무언가를 죽일 수도 있습니다.'], ['', 'A little change here can cause something unthinkable in the future."', '이곳에서의 작은 변화가 미래에 상상할 수 없는 일을 초래할 수 있습니다.”'], ['', '❸', ''], ['', 'Slowly, everyone got out of the time machine.', '모두 타임머신에서 천천히 내렸다.'], ['', 'The jungle was covered in fog.', '정글은 안개로 뒤덮여 있었다.'], ['', 'It was very quiet.', '그곳은 무척 고요했다.'], ['', '"I\'m so excited," said Eckels.', '“정말 신나요.” Eckels가 말했다.'], ['', '"Be careful. Some of the dinosaurs are hungry," said Travis.', '“조심하세요. 몇몇 공룡들이 배가 고플 수도 있습니다.” Travis가 말했다.'], ['', '"Just stay calm.', '“침착하세요.'], ['', 'I don\'t want you to do anything foolish."', '당신이 어리석은 어떤 행동도 하지 않기를 바랍니다.”'], ['', '"Don\'t worry. I\'m not a fool," said Eckels.', '“걱정하지 마세요. 저는 바보가 아니에요.” Eckels가 말했다.'], ['', 'They all began to walk on the path.', '그들은 모두 길을 걷기 시작했다.']], steps: [
    { type: 'vocab', title: '핵심어휘·숙어', quizN: 15, items: [['walk into', '~ 안으로 걸어 들어가다', '❶'], ['sign', '간판, 표지판', '❶'], ['name', '(이름·날짜 등을) 말하다, 지정하다', '❶'], ['past', '과거', '❶'], ['president', '대통령', '❶'], ['founder', '설립자', '❶'], ['dinosaur', '공룡', '❶'], ['possible', '가능한', '❶'], ['million', '100만', '❶'], ['lucky', '운이 좋은', '❶'], ['leave', '출발하다, 떠나다', '❶'], ['travel guide', '여행 안내원', '❶'], ['stay safe', '안전하게 지내다', '❶'], ['follow', '따르다', '❶'], ['instruction', '지시, 설명', '❶'], ['inside', '~ 안에', '❷'], ['traveler', '여행자', '❷'], ['feet', '발 (foot의 복수)', '❷'], ['a few', '몇몇의, 약간의', '❷'], ['path', '길, 오솔길', '❷'], ['at any time', '언제라도, 어떤 경우에도', '❷'], ['by accident', '실수로, 우연히', '❷'], ['cause', '초래하다, 일으키다', '❷'], ['unthinkable', '상상할 수 없는', '❷'], ['get out of', '~에서 내리다, 나가다', '❸'], ['be covered in', '~으로 뒤덮이다', '❸'], ['fog', '안개', '❸'], ['quiet', '조용한', '❸'], ['stay calm', '침착함을 유지하다', '❸'], ['foolish', '어리석은', '❸'], ['fool', '바보', '❸']] },
    { type: 'pick', title: '어휘선택', guide: '문맥에 맞는 낱말을 고르세요.', items: [
      { s: 'There was a TV on the wall, and Mr. Keith, the new {president|teacher}, was on the news.', ex: '정답 ▶ president (대통령)\n오답 ▶ teacher (선생님): 뉴스에 나오는 \'새 대통령\'이에요. 나중에 현재로 돌아왔을 때 이 대통령이 바뀌어 있어요.' },
      { s: '"How can we help you?" said Mr. Parker, the {founder|customer} of Time Travel.', ex: '정답 ▶ founder (설립자)\n오답 ▶ customer (손님): \'무엇을 도와드릴까요?\'라고 묻는 사람은 회사 쪽 사람이에요. 손님은 Eckels예요.' },
      { s: '"To stay safe, you must {follow|ignore} his instructions."', ex: '정답 ▶ follow (따르다)\n오답 ▶ ignore (무시하다): \'안전하려면\' 안내원의 지시를 \'따라야\' 해요.' },
      { s: 'He felt the machine moving under his {feet|hands}.', ex: '정답 ▶ feet (발)\n오답 ▶ hands (손): 자리에 앉아 눈을 감고 있었으니 \'발밑에서\' 기계가 움직이는 걸 느꼈어요.\n포인트 ▶ foot의 복수는 feet' },
      { s: 'You must not {leave|follow} it at any time.', ex: '정답 ▶ leave (벗어나다)\n오답 ▶ follow (따라가다): it은 the path(길)예요. 길을 \'벗어나면 안 된다\'가 규칙이에요. 길을 따라가지 말라는 건 반대 뜻이에요.' },
      { s: 'A little change here can {cause|stop} something unthinkable in the future."', ex: '정답 ▶ cause (초래하다)\n오답 ▶ stop (멈추다): 과거의 작은 변화가 미래에 상상할 수 없는 일을 \'일으킬\' 수 있다는 경고예요. 이 이야기의 핵심 내용이에요.' },
      { s: 'The jungle was covered in {fog|snow}.', ex: '정답 ▶ fog (안개)\n오답 ▶ snow (눈): 정글이 \'안개\'로 뒤덮여 있었고 무척 고요했어요.' },
      { s: '"Just stay {calm|excited}.', ex: '정답 ▶ calm (침착한)\n오답 ▶ excited (신이 난): Eckels가 \'정말 신나요\'라고 하자 Travis가 \'조심하세요, 침착하세요\'라고 주의를 줬어요.' },
      { s: 'They all began to walk on the {path|river}.', ex: '정답 ▶ path (길)\n오답 ▶ river (강): Travis가 절대 벗어나지 말라고 한 \'길\' 위를 걷기 시작했어요.' }
    ] },
    { type: 'tf', title: 'T/F 내용 확인', guide: '본문 내용과 일치하면 T, 다르면 F를 고르세요.', items: [['Eckels wanted to see a dinosaur.', true, '정답 ▶ T\n이유: \'I\'ve always wanted to see a dinosaur(항상 공룡을 보고 싶었다)\'라고 했어요.', '❶', 'I\'ve always wanted to see a dinosaur'], ['Mr. Parker was the new president.', false, '정답 ▶ F\n이유: Mr. Parker는 Time Travel의 설립자(founder)예요. 새 대통령은 Mr. Keith예요.', '❶', 'Mr. Parker, the founder of Time Travel'], ['The time machine was leaving in an hour.', false, '정답 ▶ F\n이유: 한 시간이 아니라 10분 후에(in 10 minutes) 출발해요.', '❶', 'There\'s a time machine that leaves in 10 minutes'], ['Travis was Eckels\'s travel guide.', true, '정답 ▶ T\n이유: \'This is Travis, your travel guide.\' 콤마 뒤 your travel guide가 Travis를 설명해요.', '❶', 'This is Travis, your travel guide'], ['There were three other travelers in the time machine.', false, '정답 ▶ F\n이유: 다른 여행자는 세 명이 아니라 두 명(two other travelers)이었어요.', '❷', 'there were two other travelers'], ['Travis said the travelers could touch anything in the jungle.', false, '정답 ▶ F\n이유: \'아무것도 만지지 마세요(Do not touch anything)\'라고 했어요.', '❷', 'Do not touch anything'], ['The jungle was quiet and covered in fog.', true, '정답 ▶ T\n이유: 정글은 안개로 뒤덮여 있었고(covered in fog) 무척 고요했어요(very quiet).', '❸', 'The jungle was covered in fog'], ['Eckels said that he was not a fool.', true, '정답 ▶ T\n이유: \'Don\'t worry. I\'m not a fool(걱정 마세요. 저는 바보가 아니에요)\'라고 했어요.', '❸', 'I\'m not a fool']] },
    { type: 'mc', title: '일치·불일치', guide: '선택지는 본문을 어려운 어휘로 바꿔 쓴 문장이에요. 풀고 나서 해설의 어휘를 꼭 확인하세요.', items: [
      { n: '❶', box: ['❶'], q: '글의 내용과 일치하지 <u>않는</u> 것은?', opts: ['Eckels had to wait a whole day for the time machine.', 'Time Travel says it can take people to any year in the past.', 'Mr. Keith appeared on TV as the new president.', 'Mr. Parker started the company Time Travel.', 'Eckels was told to obey Travis for his safety.'], ex: '정답 ▶ Eckels had to wait a whole day for the time machine.\n이유: 하루를 기다린 게 아니라 \'10분 후에 출발하는\' 타임머신이 있었어요.\n어휘 ▶ a whole day 하루 종일 · obey = follow 따르다 · safety 안전', per: [['Eckels는 타임머신을 하루 종일 기다려야 했다.', 'There\'s a time machine that leaves in 10 minutes', '불일치 → 10분 후 출발'], ['Time Travel은 과거의 어느 해로든 데려갈 수 있다고 한다.', 'NAME ANY YEAR IN THE PAST. WE TAKE YOU THERE', '일치'], ['Keith 씨는 새 대통령으로 TV에 나왔다.', 'Mr. Keith, the new president, was on the news', '일치'], ['Parker 씨는 Time Travel 회사를 세웠다.', 'Mr. Parker, the founder of Time Travel', '일치 (founder 설립자)'], ['Eckels는 안전을 위해 Travis의 말을 따르라는 말을 들었다.', 'To stay safe, you must follow his instructions', '일치 (obey = follow)']] },
      { n: '❷', box: ['❷', '❸'], q: 'Travis가 한 말과 일치하는 것은?', opts: ['Even a small change in the past could affect the future.', 'The travelers may leave the path when it is safe.', 'Touching plants in the jungle is allowed.', 'None of the dinosaurs are dangerous.', 'Eckels can do whatever he wants.'], ex: '정답 ▶ Even a small change in the past could affect the future.\n이유: A little change here can cause something unthinkable in the future.\n어휘 ▶ affect 영향을 주다 · allowed 허락된 · whatever ~하는 것은 무엇이든', per: [['과거의 작은 변화도 미래에 영향을 줄 수 있다.', 'A little change here can cause something unthinkable in the future', '일치 (affect 영향을 주다)'], ['안전할 때는 여행자들이 길을 벗어나도 된다.', 'You must not leave it at any time', '불일치 → 어떤 경우에도 안 됨'], ['정글의 식물을 만지는 것은 허락된다.', 'Do not touch anything', '불일치 → 아무것도 만지지 말 것'], ['위험한 공룡은 하나도 없다.', 'Some of the dinosaurs are hungry', '불일치 → 배고픈 공룡도 있음'], ['Eckels는 원하는 것은 무엇이든 해도 된다.', 'I don\'t want you to do anything foolish', '불일치 → 어리석은 행동을 하지 말 것']] }
    ] },
    { type: 'pick', title: '어법선택', guide: '어법상 알맞은 것을 고르세요.', items: [
      { s: 'Inside the time machine, there {were|was} two other travelers.', ex: '정답 ▶ were\n이유: There + be동사 + 주어. 주어 two other travelers가 복수 → were\n오답 ▶ was는 단수 주어일 때 (There was a TV on the wall.)' },
      { s: '"I\'ve always {wanted|want} to see a dinosaur. Is it possible?" asked Eckels.', ex: '정답 ▶ wanted\n이유: have + 과거분사 = 현재완료. I\'ve(I have) always wanted = 항상 ~하고 싶었다(과거부터 지금까지 계속)\n오답 ▶ want(동사원형) ✘' },
      { s: '"You\'re lucky. There\'s a time machine {that|who} leaves in 10 minutes," said Mr. Parker.', ex: '정답 ▶ that\n이유: 꾸밈을 받는 말(선행사) a time machine이 \'사물\'이라 that(또는 which). 뒤에 주어가 없으니 주격 관계대명사예요.\n오답 ▶ who는 선행사가 \'사람\'일 때' },
      { s: '"{To stay|Stay} safe, you must follow his instructions."', ex: '정답 ▶ To stay\n이유: \'안전하기 위해\' → 목적(~하기 위해)을 나타내는 to부정사가 문장 앞에 왔어요.\n오답 ▶ Stay safe, you must ~ 는 명령문 뒤에 또 문장이 붙어 어색해요.' },
      { s: 'He felt the machine {moving|to move} under his feet.', ex: '정답 ▶ moving\n이유: 지각동사 feel + 목적어 + -ing(또는 동사원형) = …가 ~하는 것을 느끼다\n오답 ▶ to move ✘ (지각동사 뒤에는 to부정사를 쓰지 않아요)' },
      { s: 'You might kill something {by|in} accident.', ex: '정답 ▶ by\n이유: by accident = 실수로, 우연히 (짝꿍 표현)\n비교 ▶ in an accident = 사고로 (교통사고 등)' },
      { s: 'You must not {leave|to leave} it at any time.', ex: '정답 ▶ leave\n이유: 조동사 must 뒤에는 동사원형. must not + 동사원형 = ~해서는 안 된다\n오답 ▶ to leave ✘' },
      { s: 'A little change here can cause {something unthinkable|unthinkable something} in the future."', ex: '정답 ▶ something unthinkable\n이유: -thing으로 끝나는 말(something, anything, nothing)은 형용사가 \'뒤에서\' 꾸며요.\n오답 ▶ unthinkable something ✘\n포인트 ▶ something cold, anything foolish, nothing special' },
      { s: 'The jungle was covered {in|at} fog.', ex: '정답 ▶ in\n이유: be covered in/with ~ = ~으로 뒤덮여 있다\n오답 ▶ at ✘' },
      { s: 'I don\'t want you {to do|do} anything foolish."', ex: '정답 ▶ to do\n이유: want + 목적어 + to부정사 = (목적어)가 ~하기를 원하다\n오답 ▶ do ✘ (want 뒤 목적어 다음에는 to부정사)' }
    ] },
    { type: 'verb', title: '동사변형', guide: '( ) 안의 동사를 알맞은 형태로 바꿔 쓰세요.', items: [
      { s: 'Eckels ___ into the office of Time Travel.', v: 'walk', a: ['walked'], ex: '정답 ▶ walked\n이유: 과거 이야기 → 과거형 -ed\n포인트 ▶ walk into = ~ 안으로 걸어 들어가다' },
      { s: 'There was a TV on the wall, and Mr. Keith, the new president, ___ on the news.', v: 'be', a: ['was'], ex: '정답 ▶ was\n이유: 주어 Mr. Keith(단수) + 과거 → was. 콤마 사이 the new president는 Mr. Keith를 설명하는 말(동격)이라 주어의 수와 상관없어요.' },
      { s: 'Eckels ___ down and closed his eyes.', v: 'sit', a: ['sat'], ex: '정답 ▶ sat\n이유: closed(과거)와 병렬 → 과거형. sit - sat - sat (불규칙)' },
      { s: 'After only a few minutes, the machine ___.', v: 'stop', a: ['stopped'], ex: '정답 ▶ stopped\n이유: 과거형. \'모음 1개 + 자음 1개\'로 끝나서 p를 겹치고 -ed (stop → stopped)' },
      { s: 'You might ___ something by accident.', v: 'kill', a: ['kill'], ex: '정답 ▶ kill\n이유: 조동사 might(~할지도 모른다) 뒤에는 동사원형!' },
      { s: 'Slowly, everyone ___ out of the time machine.', v: 'get', a: ['got'], ex: '정답 ▶ got\n이유: 과거형. get - got - got(ten)\n포인트 ▶ get out of = ~에서 내리다' },
      { s: '"I\'m so ___," said Eckels.', v: 'excite', a: ['excited'], ex: '정답 ▶ excited\n이유: 사람이 \'신이 난\' 감정을 느낄 때는 과거분사 excited. exciting은 \'신나게 하는\'(사물이 주는 느낌)' },
      { s: 'They all began ___ on the path.', v: 'walk', a: ['to walk', 'walking'], ex: '정답 ▶ to walk (또는 walking)\n이유: begin + to부정사/동명사 = ~하기 시작하다. 본문은 to walk' }
    ] },
    { type: 'error', title: '오류찾기', guide: '어법상 틀린 곳을 고르세요.', items: [
      { s: '"We can [[take]] you [[back]] to the jungle of 60 [[millions]] years ago."', w: 2, fix: 'million', ex: '틀린 곳 ▶ ③ millions → million\n이유: 숫자(60) 뒤에 오는 million은 단수형! 60 million years = 6천만 년 (two hundred, three thousand도 같아요)\n비교 ▶ millions of ~ = 수백만의 ~ (숫자 없이 쓸 때만 -s)\n나머지 ▶ ① take(can + 동사원형) ✔ ② take ~ back(~을 다시 데려가다) ✔' },
      { s: '"You\'re [[lucky]]. There\'s a time machine [[who]] [[leaves]] in 10 minutes," said Mr. Parker.', w: 1, fix: 'that', ex: '틀린 곳 ▶ ② who → that (또는 which)\n이유: 선행사 a time machine은 사물 → that/which. who는 사람일 때만\n나머지 ▶ ① lucky ✔ ③ leaves(단수 선행사에 맞춘 동사) ✔' },
      { s: 'Eckels [[sat]] down and [[closes]] his eyes. After only a [[few]] minutes, the machine [[stopped]].', w: 1, fix: 'closed', ex: '틀린 곳 ▶ ② closes → closed\n이유: sat(과거) and closed(과거). and로 이어진 동사는 시제를 맞춰요.\n나머지 ▶ ① sat ✔ ③ a few minutes(몇 분, 셀 수 있는 명사) ✔ ④ stopped ✔' },
      { s: 'Do not [[touching]] anything. You [[might]] kill [[something]] by accident.', w: 0, fix: 'touch', ex: '틀린 곳 ▶ ① touching → touch\n이유: 부정 명령문은 Do not(Don\'t) + 동사원형 (~하지 마세요)\n나머지 ▶ ② might(~할지도 모른다) ✔ ③ something ✔' },
      { s: '"Just stay [[calmly]]. I don\'t [[want]] you [[to do]] anything [[foolish]]."', w: 0, fix: 'calm', ex: '틀린 곳 ▶ ① calmly → calm\n이유: stay + 형용사 = ~한 상태를 유지하다. stay 뒤에는 부사가 아니라 형용사!\n나머지 ▶ ② want ✔ ③ to do(want + 목적어 + to부정사) ✔ ④ foolish(anything 뒤에서 꾸밈) ✔' }
    ] },
    { type: 'scramble', title: '본문 스크램블', guide: '우리말에 맞게 단어를 눌러 문장을 완성하세요.', items: [
      { ko: 'Eckels는 Time Travel의 사무실로 걸어 들어갔다.', en: 'Eckels walked into the office of Time Travel.' },
      { ko: '타임머신 안에는 다른 여행자 두 명이 있었다.', en: 'Inside the time machine, there were two other travelers.' },
      { ko: '그는 발밑에서 타임머신이 움직이는 것을 느꼈다.', en: 'He felt the machine moving under his feet.' },
      { ko: '여러분이 실수로 무언가를 죽일 수도 있습니다.', en: 'You might kill something by accident.' },
      { ko: '정글은 안개로 뒤덮여 있었다.', en: 'The jungle was covered in fog.' },
      { ko: '그들은 모두 길을 걷기 시작했다.', en: 'They all began to walk on the path.' }
    ] },
    { type: 'order', title: '문장순서', guide: '문장을 본문 순서대로 눌러서 배열하세요.', items: [
      { lines: ['Eckels walked into the office of Time Travel.', 'The big sign on the wall said, "NAME ANY YEAR IN THE PAST. WE TAKE YOU THERE."', 'There was a TV on the wall, and Mr. Keith, the new president, was on the news.', '"How can we help you?" said Mr. Parker, the founder of Time Travel.'], flow: ['Time Travel 사무실로 들어감', '간판: 과거의 어느 해든 데려다 드립니다', 'TV에 새 대통령 Keith', '설립자 Parker: 무엇을 도와드릴까요?'] },
      { lines: ['Inside the time machine, there were two other travelers.', 'Eckels sat down and closed his eyes.', 'He felt the machine moving under his feet.', 'After only a few minutes, the machine stopped.'], flow: ['타임머신 안에 다른 여행자 두 명', '앉아서 눈을 감음', '발밑에서 기계가 움직이는 걸 느낌', '몇 분 뒤 멈춤'] },
      { lines: ['Slowly, everyone got out of the time machine.', 'The jungle was covered in fog.', 'It was very quiet.', 'They all began to walk on the path.'], flow: ['모두 타임머신에서 내림', '정글은 안개로 뒤덮임', '무척 고요함', '모두 길을 걷기 시작함'] }
    ] },
    { type: 'insert', title: '문장삽입', guide: '주어진 문장이 들어가기에 가장 알맞은 곳을 고르세요.', items: [
      { lines: ['"You\'re lucky. There\'s a time machine that leaves in 10 minutes," said Mr. Parker.', '"This is Travis, your travel guide," he continued.', '"To stay safe, you must follow his instructions."'], given: 1, flow: ['10분 후 출발하는 타임머신이 있음', '이분이 여행 안내원 Travis', '안전하려면 그(his)의 지시를 따라야 함'], ex: '정답 ▶ ①\n이유: 마지막 문장의 his가 가리키는 사람이 Travis예요. 그러니 Travis를 소개하는 문장이 그 바로 앞에 와야 해요.' },
      { lines: ['He felt the machine moving under his feet.', 'After only a few minutes, the machine stopped.', '"We\'ve just arrived in the jungle of 60 million years ago," Travis explained.'], given: 1, flow: ['기계가 움직이는 걸 느낌', '몇 분 뒤 기계가 멈춤', '이제 막 6천만 년 전 정글에 도착'], ex: '정답 ▶ ①\n이유: 움직이다 → 멈추다 → \'도착했습니다\'의 순서예요. 멈춘 다음에 도착했다고 설명해요.' },
      { lines: ['Do not touch anything.', 'You might kill something by accident.', 'A little change here can cause something unthinkable in the future."'], given: 1, flow: ['아무것도 만지지 마세요', '실수로 무언가를 죽일 수도 있어요', '작은 변화가 미래에 상상 못 할 일을 일으켜요'], ex: '정답 ▶ ①\n이유: \'만지지 마라\'의 이유가 \'실수로 무언가를 죽일 수 있기 때문\'이에요. 그리고 그 작은 변화가 미래를 바꾼다는 말로 이어져요.' }
    ] },
    { type: 'odd', title: '어색한 문장', guide: '글의 흐름과 관계없는 문장을 고르세요.', items: [
      { lines: ['"How can we help you?" said Mr. Parker, the founder of Time Travel.', '"I\'ve always wanted to see a dinosaur. Is it possible?" asked Eckels.', 'Eckels was afraid of dinosaurs and wanted to go home.', '"Sure," said Mr. Parker.'], odd: 2, ex: '정답 ▶ ③\n이유: Eckels는 \'항상 공룡을 보고 싶었다\'며 시간 여행을 신청하러 왔어요. \'공룡이 무서워 집에 가고 싶었다\'는 정반대예요.' },
      { lines: ['"Do you see the path over there?', 'You must not leave it at any time.', 'You can walk anywhere you want in the jungle.', 'Do not touch anything.'], odd: 2, ex: '정답 ▶ ③\n이유: Travis는 \'어떤 경우에도 길을 벗어나면 안 된다\'고 했어요. \'정글 어디든 걸어 다녀도 된다\'는 규칙과 반대예요.' },
      { lines: ['"Be careful. Some of the dinosaurs are hungry," said Travis.', '"Just stay calm.', 'Travis told Eckels to run and shout loudly.', 'I don\'t want you to do anything foolish."'], odd: 2, ex: '정답 ▶ ③\n이유: Travis는 \'조심하고 침착하라\'고 했어요. \'뛰면서 크게 소리치라고 했다\'는 흐름과 맞지 않아요.' }
    ] },
    { type: 'blank', title: '빈칸추론', guide: '빈칸에 들어갈 말로 가장 알맞은 것을 고르세요.', items: [
      { s: 'Inside the time machine, there were two other ____.', opts: ['travelers', 'dinosaurs', 'presidents', 'founders'], ex: '정답 ▶ travelers\n이유: 타임머신 안에는 Eckels 말고도 \'다른 여행자 두 명\'이 함께 있었어요.' },
      { s: 'He felt the machine ____ under his feet.', opts: ['moving', 'sleeping', 'singing', 'breaking'], ex: '정답 ▶ moving\n이유: 시간 여행을 떠나는 장면이에요. 발밑에서 기계가 \'움직이는\' 것을 느꼈고, 몇 분 뒤 멈췄어요.' },
      { s: 'You might kill something by ____.', opts: ['accident', 'plan', 'money', 'bus'], ex: '정답 ▶ accident\n이유: by accident = 실수로. 그래서 \'아무것도 만지지 마세요\'라고 해요.' }
    ] },
    { type: 'mc', title: '핵심문법', guide: '알맞은 답을 고르세요.', items: [
      { q: '밑줄 친 부분의 현재완료 쓰임으로 알맞은 것은?<br><b><u>I\'ve always wanted</u> to see a dinosaur.</b>', opts: ['계속 (과거부터 지금까지 쭉)', '경험 (~해 본 적 있다)', '완료 (막 ~했다)', '결과 (~해 버렸다)'], ex: '정답 ▶ 계속\n이유: always와 함께 \'예전부터 지금까지 쭉 보고 싶었다\'는 뜻이에요.\n비교 ▶ 경험: I\'ve never seen ~ / 완료: We\'ve just arrived ~ / 결과: I\'ve lost my key.' },
      { q: '다음 중 어순이 <b>바른</b> 것은?', opts: ['I want to drink something cold.', 'I want to drink cold something.', 'I want to drink something coldly.', 'I want something to cold drink.'], ex: '정답 ▶ I want to drink something cold.\n이유: -thing으로 끝나는 말은 형용사가 뒤에서 꾸며요: something cold(차가운 무언가)\n오답 ▶ cold something(어순 ✘), coldly(부사 ✘), to cold drink(어순 ✘)' },
      { q: '밑줄 친 부분이 가리키는 사람은?<br><b>"How can we help you?" said Mr. Parker, <u>the founder of Time Travel</u>.</b>', opts: ['Mr. Parker', 'Eckels', 'Travis', 'Mr. Keith'], ex: '정답 ▶ Mr. Parker\n이유: 콤마(,) 뒤에서 앞의 사람을 다시 설명하는 말(동격)이에요. Mr. Parker = the founder of Time Travel' },
      { q: '밑줄 친 부분의 뜻으로 알맞은 것은?<br><b>You <u>must not</u> leave it at any time.</b>', opts: ['~해서는 안 된다', '~할 필요가 없다', '~일 리가 없다', '~하지 않았다'], ex: '정답 ▶ ~해서는 안 된다\n이유: must not = 강한 금지 (~해서는 안 된다)\n비교 ▶ don\'t have to = ~할 필요가 없다 / can\'t be = ~일 리가 없다' },
      { q: '밑줄 친 <b>To stay</b>와 쓰임이 <b>같은</b> 것은?<br><b><u>To stay</u> safe, you must follow his instructions.</b>', opts: ['She saved money <u>to buy</u> a bike.', 'I want <u>to buy</u> a bike.', 'My dream is <u>to buy</u> a bike.', 'It is fun <u>to ride</u> a bike.'], ex: '정답 ▶ She saved money to buy a bike.\n이유: 문제의 To stay는 \'안전하기 위해\'(목적, 부사적 용법). 정답도 \'자전거를 사기 위해\'예요.\n오답 ▶ want to buy(목적어), My dream is to buy(보어), It is fun to ride(진주어) → \'~하는 것\'(명사적 용법)' },
      { q: '다음 문장의 뜻으로 알맞은 것은?<br><b>The jungle was covered in fog.</b>', opts: ['정글은 안개로 뒤덮여 있었다.', '정글이 안개를 덮었다.', '정글에는 안개가 없었다.', '정글 안에서 안개가 사라졌다.'], ex: '정답 ▶ 정글은 안개로 뒤덮여 있었다.\n이유: be covered in/with ~ = ~으로 뒤덮이다 (수동태: 주어가 덮임을 당함)' },
      { q: '빈칸에 알맞은 것은?<br><b>Some of the dinosaurs ______ hungry.</b>', opts: ['are', 'is', 'was', 'be'], ex: '정답 ▶ are\n이유: some of + 복수 명사(the dinosaurs) → 복수 동사 are\n포인트 ▶ some of 뒤의 명사에 동사의 수를 맞춰요 (some of the water is …)' }
    ] },
    { type: 'mc', title: '요약문 완성', guide: '본문을 읽고 요약문의 빈칸 (A), (B)에 들어갈 말을 고르세요.', items: [
      { n: '❷', box: ['❶', '❷'], q: '다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 알맞은 것은?<br><b>Eckels traveled back in time to see a (A) ______, and Travis warned that even a small change in the past could (B) ______ the future.</b>', opts: ['(A) dinosaur – (B) change', '(A) dinosaur – (B) protect', '(A) president – (B) change', '(A) president – (B) protect', '(A) butterfly – (B) save'], ex: '정답 ▶ (A) dinosaur – (B) change\n(A) Eckels가 시간 여행을 간 목적 → 공룡(dinosaur)을 보려고\n(B) Travis의 경고: 작은 변화가 미래에 상상할 수 없는 일을 \'일으킬\' 수 있다 → 미래를 바꾸다(change)\n오답 ▶ president(대통령)·butterfly(나비)는 보러 간 대상이 아니고, protect(지키다)·save(구하다)는 경고 내용과 달라요.', ev: ['I\'ve always wanted to see a dinosaur', 'A little change here can cause something unthinkable in the future'] },
      { n: '❸', box: ['❸'], q: '다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 알맞은 것은?<br><b>When they got out of the machine, Travis told Eckels to stay (A) ______ and not to do anything (B) ______.</b>', opts: ['(A) calm – (B) foolish', '(A) excited – (B) foolish', '(A) calm – (B) careful', '(A) excited – (B) careful', '(A) angry – (B) kind'], ex: '정답 ▶ (A) calm – (B) foolish\n(A) \'Just stay calm(침착하세요)\' → calm\n(B) \'I don\'t want you to do anything foolish(어리석은 행동을 하지 않기를)\' → foolish\n오답 ▶ excited(신이 난)는 Eckels의 기분이고, careful(조심스러운)·kind(친절한) 행동은 하지 말라고 한 게 아니에요.', ev: ['Just stay calm', 'I don\'t want you to do anything foolish'] }
    ] }
  ] },
  { id: 'd4', name: 'DAY 4', range: '8과 본문 ❹❺❻', story: 'Lesson 8 · 티라노사우루스 · 현재로 돌아옴 · 죽은 나비 한 마리', passage: [['', '❹', ''], ['', 'After some time, Travis whispered, "Look over there. There is a T. rex."', '얼마 후, Travis가 속삭였다. “저기 봐요. 티라노사우루스가 있어요.”'], ['', 'One hundred meters away, a T. rex slowly appeared.', '100미터 떨어진 곳에서 티라노사우루스가 서서히 나타났다.'], ['', '"It," whispered Eckels. "It ..."', '“저것은,” Eckels가 속삭였다. “저것은 …”'], ['', '"Sh!"', '“쉿!”'], ['', '"It ... is huge. I\'ve never seen such a huge thing. I\'m so scared," said Eckels.', '“저건 … 거대해요. 저렇게 거대한 것을 본 적이 없어요. 너무 무서워요.” Eckels가 말했다.'], ['', '"Sh ... quiet!" Travis said angrily. "You don\'t want it to see you."', '“쉿 … 조용히!” Travis가 화를 내며 말했다. “공룡이 당신을 보길 원하는 건 아니겠죠.”'], ['', '"I can\'t breathe," said Eckels. "Get me out of here!"', '“숨을 쉴 수가 없어요.” Eckels가 말했다. “여기서 나가게 해 줘요!”'], ['', '"Don\'t panic, Eckels," said Travis. "Turn around, and walk quietly back to the machine."', '“겁먹지 마세요, Eckels.” Travis가 말했다. “뒤로 돌아서 조용히 타임머신으로 돌아가세요.”'], ['', 'Eckels turned around and started to run.', 'Eckels는 돌아서서 뛰기 시작했다.'], ['', 'He was so terrified that he left the path by accident.', '그는 너무 겁에 질려 실수로 길을 벗어나고 말았다.'], ['', '"Eckels!" shouted Travis. "Don\'t leave the path!"', '“Eckels!” Travis가 외쳤다. “길을 벗어나지 말아요!”'], ['', 'The T. rex heard Travis and turned its head toward him and the other travelers.', '티라노사우루스가 Travis의 소리를 듣고 그와 다른 여행자들을 향해 고개를 돌렸다.'], ['', 'There was a moment of silence.', '잠시 정적이 흘렀다.'], ['', 'Then, it suddenly started to run toward them with a loud roar.', '그리고 갑자기 티라노사우루스가 큰 포효와 함께 그들을 향해 달려오기 시작했다.'], ['', '"Run, everybody! Run!" shouted Travis.', '“모두 뛰어요! 뛰어!” Travis가 외쳤다.'], ['', '❺', ''], ['', 'Travis and the other travelers returned safely to the machine and found Eckels inside.', 'Travis와 다른 여행자들은 안전하게 타임머신으로 돌아와서 안에 있는 Eckels를 발견했다.'], ['', '"You put all of us in danger," said Travis to Eckels in an angry voice.', '“당신이 우리 모두를 위험에 빠뜨렸어요.” Travis가 화난 목소리로 Eckels에게 말했다.'], ['', '"You left the path."', '“당신이 길을 벗어났잖아요.”'], ['', '"I\'m sorry, but I didn\'t kill anything," said Eckels.', '“미안해요, 그렇지만 난 어떤 것도 죽이지 않았어요.” Eckels가 말했다.'], ['', '"There\'s only a little mud on my shoes."', '“신발에 진흙이 조금 묻었을 뿐이에요.”'], ['', 'Travis stared at Eckels for a long time without saying anything.', 'Travis는 아무 말 없이 Eckels를 오랫동안 응시했다.'], ['', '"Let\'s go home," said Travis finally.', '“집으로 갑시다.” 마침내 Travis가 말했다.'], ['', '❻', ''], ['', 'The machine stopped.', '타임머신이 멈췄다.'], ['', 'They all returned to the present safely.', '그들은 모두 안전하게 현재로 돌아왔다.'], ['', '"Is everything okay here?" asked Travis.', '“이곳은 모든 것이 괜찮나요?” Travis가 물었다.'], ['', '"Fine. Welcome home!" said Mr. Parker.', '“괜찮아요. 돌아오신 것을 환영합니다!” Parker 씨가 말했다.'], ['', 'Eckels looked around the room carefully.', 'Eckels는 방을 주의 깊게 둘러보았다.'], ['', 'Everything looked the same, except the big sign on the wall.', '벽에 걸린 큰 간판만 빼고 모든 것이 똑같아 보였다.'], ['', 'The sign now said, "NAIM ANY YEER EN THE PAST. WEE TAEK YU THAIR."', '간판에는 이제 이렇게 쓰여 있었다. “NAIM ANY YEER EN THE PAST. WEE TAEK YU THAIR.”'], ['', 'Eckels was confused.', 'Eckels는 혼란스러웠다.'], ['', 'Then, he saw the TV.', '그리고 그는 TV를 보았다.'], ['', 'The new president was on the news, but it was not Mr. Keith.', '뉴스에 새 대통령이 나오고 있었는데, Keith 씨가 아니었다.'], ['', '"What\'s going on?" He got more confused.', '“이게 대체 무슨 일이지?” 그는 더욱 혼란스러워졌다.'], ['', 'He sat down and looked closely at the mud on his shoes.', '그는 앉아서 신발에 묻은 진흙을 유심히 살펴보았다.'], ['', '"No, it can\'t be," said Eckels.', '“안 돼, 이럴 리가 없어.” Eckels가 말했다.'], ['', '"It\'s all because of this little thing?"', '“이게 모두 이 작은 것 때문이라고?”'], ['', 'He was shocked.', '그는 충격을 받았다.'], ['', 'In the mud on his right shoe, he found a small dead butterfly.', '그는 자신의 오른쪽 신발에 묻은 진흙 속에서 죽어 있는 작은 나비 한 마리를 발견했다.']], steps: [
    { type: 'vocab', title: '핵심어휘·숙어', quizN: 15, items: [['after some time', '얼마 후에', '❹'], ['whisper', '속삭이다', '❹'], ['T. rex', '티라노사우루스', '❹'], ['away', '떨어져서', '❹'], ['appear', '나타나다', '❹'], ['huge', '거대한', '❹'], ['scared', '무서워하는', '❹'], ['angrily', '화를 내며', '❹'], ['breathe', '숨을 쉬다', '❹'], ['panic', '겁에 질리다, 당황하다', '❹'], ['turn around', '뒤로 돌다', '❹'], ['terrified', '겁에 질린', '❹'], ['toward', '~ 쪽으로, ~을 향하여', '❹'], ['silence', '침묵, 정적', '❹'], ['suddenly', '갑자기', '❹'], ['roar', '포효, 으르렁거림', '❹'], ['return', '돌아오다', '❺'], ['safely', '안전하게', '❺'], ['put ~ in danger', '~을 위험에 빠뜨리다', '❺'], ['mud', '진흙', '❺'], ['stare at', '~을 응시하다', '❺'], ['without -ing', '~하지 않고', '❺'], ['finally', '마침내', '❺'], ['present', '현재', '❻'], ['look around', '둘러보다', '❻'], ['carefully', '주의 깊게', '❻'], ['except', '~을 제외하고', '❻'], ['confused', '혼란스러운', '❻'], ['closely', '자세히, 유심히', '❻'], ['because of', '~ 때문에', '❻'], ['shocked', '충격을 받은', '❻'], ['dead', '죽은', '❻']] },
    { type: 'pick', title: '어휘선택', guide: '문맥에 맞는 낱말을 고르세요.', items: [
      { s: 'After some time, Travis {whispered|shouted}, "Look over there. There is a T. rex."', ex: '정답 ▶ whispered (속삭였다)\n오답 ▶ shouted (외쳤다): 공룡이 눈치채지 않게 \'속삭인\' 거예요. 뒤에서 \'쉿! 조용히!\'라고 해요.' },
      { s: 'One hundred meters away, a T. rex slowly {appeared|disappeared}.', ex: '정답 ▶ appeared (나타났다)\n오답 ▶ disappeared (사라졌다): \'There is a T. rex\' 다음이고, Eckels가 그 거대함에 놀라니 공룡이 \'나타난\' 거예요.' },
      { s: '"It ... is huge. I\'ve never seen such a huge thing. I\'m so {scared|bored}," said Eckels.', ex: '정답 ▶ scared (무서워하는)\n오답 ▶ bored (지루한): 거대한 공룡을 처음 보고 숨을 못 쉴 만큼 \'무서워\'했어요.' },
      { s: '"Don\'t panic, Eckels," said Travis. "Turn around, and walk {quietly|loudly} back to the machine."', ex: '정답 ▶ quietly (조용히)\n오답 ▶ loudly (시끄럽게): 공룡이 알아채지 못하게 \'조용히\' 돌아가라고 했어요.' },
      { s: 'The T. rex heard Travis and turned its {head|tail} toward him and the other travelers.', ex: '정답 ▶ head (머리)\n오답 ▶ tail (꼬리): 소리를 들은 공룡이 그쪽으로 \'고개를 돌렸어요(turned its head)\'.' },
      { s: 'Then, it suddenly started to run toward them with a loud {roar|song}.', ex: '정답 ▶ roar (포효)\n오답 ▶ song (노래): 공룡이 \'큰 포효(으르렁 소리)\'와 함께 달려왔어요.' },
      { s: '"You put all of us in {danger|safety}," said Travis to Eckels in an angry voice.', ex: '정답 ▶ danger (위험)\n오답 ▶ safety (안전): 화난 목소리로 \'당신이 우리 모두를 위험에 빠뜨렸다\'고 혼냈어요.\n포인트 ▶ put ~ in danger = ~을 위험에 빠뜨리다' },
      { s: 'Travis {stared|smiled} at Eckels for a long time without saying anything.', ex: '정답 ▶ stared (응시했다)\n오답 ▶ smiled (웃었다): 화가 난 Travis가 아무 말 없이 오랫동안 \'쳐다봤어요\'. 웃을 상황이 아니에요.' },
      { s: 'Everything looked the same, {except|including} the big sign on the wall.', ex: '정답 ▶ except (~을 제외하고)\n오답 ▶ including (~을 포함하여): 바로 다음에 간판 글자가 이상하게 바뀌어 있었어요. 간판\'만 빼고\' 똑같아 보였어요.' }
    ] },
    { type: 'tf', title: 'T/F 내용 확인', guide: '본문 내용과 일치하면 T, 다르면 F를 고르세요.', items: [['The T. rex appeared one hundred meters away.', true, '정답 ▶ T\n이유: One hundred meters away, a T. rex slowly appeared. 그대로예요.', '❹', 'One hundred meters away, a T. rex slowly appeared'], ['Eckels had seen many huge dinosaurs before.', false, '정답 ▶ F\n이유: \'I\'ve never seen such a huge thing(저렇게 거대한 건 본 적이 없다)\'고 했어요.', '❹', 'I\'ve never seen such a huge thing'], ['Travis told Eckels to run fast to the machine.', false, '정답 ▶ F\n이유: 뛰라는 게 아니라 \'조용히 걸어서(walk quietly)\' 돌아가라고 했어요.', '❹', 'Turn around, and walk quietly back to the machine'], ['Eckels left the path because he was too scared.', true, '정답 ▶ T\n이유: 너무 겁에 질려서(so terrified) 실수로 길을 벗어났어요.', '❹', 'He was so terrified that he left the path by accident'], ['Travis and the others came back to the machine safely.', true, '정답 ▶ T\n이유: 안전하게(safely) 타임머신으로 돌아왔어요.', '❺', 'returned safely to the machine'], ['Eckels said he killed a small animal.', false, '정답 ▶ F\n이유: \'아무것도 죽이지 않았다(I didn\'t kill anything)\'고 했어요. 신발에 진흙만 묻었다고 했죠.', '❺', 'I didn\'t kill anything'], ['When they returned, the sign on the wall looked different.', true, '정답 ▶ T\n이유: 간판만 빼고 모두 똑같아 보였어요. 간판 글자가 이상하게 바뀌어 있었어요.', '❻', 'Everything looked the same, except the big sign on the wall'], ['Mr. Keith was still the president on the news.', false, '정답 ▶ F\n이유: 뉴스의 새 대통령은 Keith 씨가 아니었어요(it was not Mr. Keith).', '❻', 'it was not Mr. Keith']] },
    { type: 'mc', title: '일치·불일치', guide: '선택지는 본문을 어려운 어휘로 바꿔 쓴 문장이에요. 풀고 나서 해설의 어휘를 꼭 확인하세요.', items: [
      { n: '❹', box: ['❹'], q: 'Eckels에 관한 내용과 일치하지 <u>않는</u> 것은?', opts: ['He stayed calm when he saw the T. rex.', 'He had never seen anything as big as the T. rex.', 'He had trouble breathing.', 'He wanted to get out of the jungle.', 'He stepped off the path by mistake.'], ex: '정답 ▶ He stayed calm when he saw the T. rex.\n이유: 침착하기는커녕 \'너무 무섭다, 숨을 못 쉬겠다\'며 겁에 질렸어요.\n어휘 ▶ as big as ~만큼 큰 · have trouble -ing ~하는 데 어려움을 겪다 · by mistake = by accident 실수로', per: [['그는 티라노사우루스를 보고 침착함을 유지했다.', 'I\'m so scared', '불일치 → 너무 무서워함'], ['그는 티라노사우루스만큼 큰 것을 본 적이 없었다.', 'I\'ve never seen such a huge thing', '일치'], ['그는 숨 쉬기 힘들었다.', 'I can\'t breathe', '일치 (have trouble -ing)'], ['그는 정글에서 나가고 싶어 했다.', 'Get me out of here', '일치'], ['그는 실수로 길을 벗어났다.', 'he left the path by accident', '일치 (by mistake = by accident)']] },
      { n: '❻', box: ['❺', '❻'], q: '글의 내용과 <u>일치하는</u> 것은?', opts: ['Eckels found a dead butterfly in the mud on his shoe.', 'Travis praised Eckels for following the rules.', 'Travis talked to Eckels for a long time.', 'Everything in the present was exactly the same as before.', 'Eckels understood what had happened right away.'], ex: '정답 ▶ Eckels found a dead butterfly in the mud on his shoe.\n이유: In the mud on his right shoe, he found a small dead butterfly.\n어휘 ▶ praise 칭찬하다 · exactly 정확히 · right away 즉시', per: [['Eckels는 신발의 진흙에서 죽은 나비를 발견했다.', 'he found a small dead butterfly', '일치'], ['Travis는 규칙을 지킨 Eckels를 칭찬했다.', 'You put all of us in danger', '불일치 → 위험에 빠뜨렸다고 화냄'], ['Travis는 Eckels에게 오랫동안 이야기했다.', 'stared at Eckels for a long time without saying anything', '불일치 → 아무 말 없이 응시함'], ['현재의 모든 것이 전과 똑같았다.', 'Everything looked the same, except the big sign on the wall', '불일치 → 간판과 대통령이 바뀜'], ['Eckels는 무슨 일이 일어났는지 바로 이해했다.', 'Eckels was confused', '불일치 → 혼란스러워함']] }
    ] },
    { type: 'pick', title: '어법선택', guide: '어법상 알맞은 것을 고르세요.', items: [
      { s: '"It ... is huge. I\'ve never {seen|saw} such a huge thing. I\'m so scared," said Eckels.', ex: '정답 ▶ seen\n이유: have + 과거분사 = 현재완료. never와 함께 \'~해 본 적이 없다\'(경험). see - saw - seen\n오답 ▶ saw는 과거형이라 have 뒤에 올 수 없어요.' },
      { s: '"It ... is huge. I\'ve never seen {such a huge thing|a such huge thing}. I\'m so scared," said Eckels.', ex: '정답 ▶ such a huge thing\n이유: such + a + 형용사 + 명사 = 그렇게 ~한 (명사)\n오답 ▶ a such ✘ (such가 a 앞에 와요)\n비교 ▶ so + 형용사: so huge' },
      { s: '"Sh ... quiet!" Travis said angrily. "You don\'t want it {to see|see} you."', ex: '정답 ▶ to see\n이유: want + 목적어 + to부정사 = (목적어)가 ~하기를 원하다. it = the T. rex\n오답 ▶ see ✘' },
      { s: 'He was {so|such} terrified that he left the path by accident.', ex: '정답 ▶ so\n이유: so + 형용사 + that + 주어 + 동사 = 너무 ~해서 …하다. terrified는 형용사라 so\n오답 ▶ such는 뒤에 (a) + 형용사 + 명사가 올 때 (such a huge thing)' },
      { s: 'The T. rex heard Travis and {turned|turns} its head toward him and the other travelers.', ex: '정답 ▶ turned\n이유: heard(과거) and turned(과거). and로 이어진 동사는 시제를 맞춰요.\n오답 ▶ turns는 현재형' },
      { s: '"There\'s only a {little|few} mud on my shoes."', ex: '정답 ▶ little\n이유: mud(진흙)는 셀 수 없는 명사 → a little(조금 있는)\n오답 ▶ a few는 셀 수 있는 복수 명사 앞 (a few minutes)' },
      { s: 'Travis stared at Eckels for a long time without {saying|say} anything.', ex: '정답 ▶ saying\n이유: 전치사 without 뒤에는 동명사(-ing). without saying anything = 아무 말도 하지 않고\n오답 ▶ say(동사원형) ✘' },
      { s: 'Eckels was {confused|confusing}.', ex: '정답 ▶ confused\n이유: 사람이 \'혼란스러움을 느낄 때\'는 confused. 무언가가 \'혼란스럽게 만들 때\'는 confusing\n포인트 ▶ excited/exciting, bored/boring, shocked/shocking' },
      { s: '"What\'s going on?" He got {more|most} confused.', ex: '정답 ▶ more\n이유: get + 비교급 = 더 ~해지다. 간판에 이어 대통령까지 바뀌어 \'더\' 혼란스러워졌어요.\n오답 ▶ most는 최상급(가장)이라 the와 함께, 여럿 중 하나를 비교할 때 써요.' },
      { s: '"No, it {can\'t|must} be," said Eckels.', ex: '정답 ▶ can\'t\n이유: can\'t be = ~일 리가 없다 (강한 부정의 추측). \'안 돼, 이럴 리가 없어\'\n오답 ▶ must be = ~임에 틀림없다 (No와 함께 쓰면 뜻이 맞지 않아요)' }
    ] },
    { type: 'verb', title: '동사변형', guide: '( ) 안의 동사를 알맞은 형태로 바꿔 쓰세요.', items: [
      { s: 'One hundred meters away, a T. rex slowly ___.', v: 'appear', a: ['appeared'], ex: '정답 ▶ appeared\n이유: 과거형 -ed\n포인트 ▶ appear(나타나다) ↔ disappear(사라지다)' },
      { s: 'Eckels turned around and started ___.', v: 'run', a: ['to run', 'running'], ex: '정답 ▶ to run (또는 running)\n이유: start + to부정사/동명사 = ~하기 시작하다. 본문은 to run' },
      { s: 'He was so terrified that he ___ the path by accident.', v: 'leave', a: ['left'], ex: '정답 ▶ left\n이유: 과거형. leave - left - left (불규칙)' },
      { s: 'Travis and the other travelers returned safely to the machine and ___ Eckels inside.', v: 'find', a: ['found'], ex: '정답 ▶ found\n이유: returned(과거)와 병렬 → 과거형. find - found - found' },
      { s: '"You ___ all of us in danger," said Travis to Eckels in an angry voice.', v: 'put', a: ['put'], ex: '정답 ▶ put\n이유: 과거형. put은 현재·과거·과거분사가 모두 put!\n포인트 ▶ put ~ in danger = ~을 위험에 빠뜨리다' },
      { s: 'They all ___ to the present safely.', v: 'return', a: ['returned'], ex: '정답 ▶ returned\n이유: 과거형 -ed\n포인트 ▶ return to ~ = ~로 돌아오다' },
      { s: 'He ___ down and looked closely at the mud on his shoes.', v: 'sit', a: ['sat'], ex: '정답 ▶ sat\n이유: looked(과거)와 병렬 → 과거형. sit - sat - sat' },
      { s: 'He was ___.', v: 'shock', a: ['shocked'], ex: '정답 ▶ shocked\n이유: 사람이 \'충격을 받은\' 감정 → 과거분사 shocked (shocking은 \'충격적인\')' }
    ] },
    { type: 'error', title: '오류찾기', guide: '어법상 틀린 곳을 고르세요.', items: [
      { s: '"Don\'t [[panic]], Eckels," said Travis. "Turn around, and [[walking]] [[quietly]] back to the machine."', w: 1, fix: 'walk', ex: '틀린 곳 ▶ ② walking → walk\n이유: Turn around, and walk ~. 명령문 두 개가 and로 이어져 둘 다 동사원형으로 시작해요.\n나머지 ▶ ① Don\'t panic(Don\'t + 동사원형) ✔ ③ quietly(동사 walk를 꾸미는 부사) ✔' },
      { s: 'The T. rex [[heard]] Travis and turned [[it\'s]] head [[toward]] him and the other travelers.', w: 1, fix: 'its', ex: '틀린 곳 ▶ ② it\'s → its\n이유: \'그것의 머리\' → 소유격 its. it\'s는 it is(또는 it has)의 줄임말이에요.\n나머지 ▶ ① heard(hear의 과거) ✔ ③ toward(~을 향하여) ✔' },
      { s: '"There\'s only a [[few]] mud on my shoes." Travis [[stared]] at Eckels for a long time [[without]] saying anything.', w: 0, fix: 'little', ex: '틀린 곳 ▶ ① few → little\n이유: mud는 셀 수 없는 명사 → a little\n나머지 ▶ ② stared at(~을 응시했다) ✔ ③ without + -ing ✔' },
      { s: 'Eckels looked around the room [[careful]]. Everything [[looked]] the same, [[except]] the big sign on the wall.', w: 0, fix: 'carefully', ex: '틀린 곳 ▶ ① careful → carefully\n이유: 동사 looked around(둘러보았다)를 꾸미는 말 → 부사 carefully(주의 깊게)\n나머지 ▶ ② looked the same(look + 형용사) ✔ ③ except(~을 빼고) ✔' },
      { s: 'Then, he [[saw]] the TV. The new president was on the news, but [[it]] was not Mr. Keith. He got [[most]] confused.', w: 2, fix: 'more', ex: '틀린 곳 ▶ ③ most → more\n이유: get + 비교급 = 더 ~해지다. 하나와 비교하는 \'더\'는 비교급 more\n나머지 ▶ ① saw(see의 과거) ✔ ② it(= the new president) ✔' }
    ] },
    { type: 'scramble', title: '본문 스크램블', guide: '우리말에 맞게 단어를 눌러 문장을 완성하세요.', items: [
      { ko: '100미터 떨어진 곳에서 티라노사우루스가 서서히 나타났다.', en: 'One hundred meters away, a T. rex slowly appeared.' },
      { ko: 'Eckels는 돌아서서 뛰기 시작했다.', en: 'Eckels turned around and started to run.' },
      { ko: '그는 너무 겁에 질려 실수로 길을 벗어나고 말았다.', en: 'He was so terrified that he left the path by accident.' },
      { ko: 'Travis는 아무 말 없이 Eckels를 오랫동안 응시했다.', en: 'Travis stared at Eckels for a long time without saying anything.' },
      { ko: 'Eckels는 방을 주의 깊게 둘러보았다.', en: 'Eckels looked around the room carefully.' },
      { ko: '그는 자신의 오른쪽 신발에 묻은 진흙 속에서 죽어 있는 작은 나비 한 마리를 발견했다.', en: 'In the mud on his right shoe, he found a small dead butterfly.' }
    ] },
    { type: 'order', title: '문장순서', guide: '문장을 본문 순서대로 눌러서 배열하세요.', items: [
      { lines: ['After some time, Travis whispered, "Look over there. There is a T. rex."', 'One hundred meters away, a T. rex slowly appeared.', '"It ... is huge. I\'ve never seen such a huge thing. I\'m so scared," said Eckels.', '"Sh ... quiet!" Travis said angrily. "You don\'t want it to see you."'], flow: ['Travis: 저기 티라노사우루스가 있어요', '100미터 떨어진 곳에 나타남', 'Eckels: 저렇게 거대한 건 처음, 너무 무서워요', 'Travis: 쉿! 조용히!'] },
      { lines: ['Eckels turned around and started to run.', 'He was so terrified that he left the path by accident.', 'The T. rex heard Travis and turned its head toward him and the other travelers.', 'There was a moment of silence.', 'Then, it suddenly started to run toward them with a loud roar.'], flow: ['Eckels가 돌아서 뛰기 시작함', '너무 겁에 질려 실수로 길을 벗어남', '공룡이 소리를 듣고 고개를 돌림', '잠시 정적', '갑자기 포효하며 달려옴'] },
      { lines: ['Then, he saw the TV.', 'The new president was on the news, but it was not Mr. Keith.', 'He sat down and looked closely at the mud on his shoes.', 'In the mud on his right shoe, he found a small dead butterfly.'], flow: ['TV를 봄', '새 대통령이 Keith 씨가 아님', '앉아서 신발의 진흙을 유심히 봄', '진흙 속 죽은 나비 발견'] }
    ] },
    { type: 'insert', title: '문장삽입', guide: '주어진 문장이 들어가기에 가장 알맞은 곳을 고르세요.', items: [
      { lines: ['Eckels turned around and started to run.', 'He was so terrified that he left the path by accident.', '"Eckels!" shouted Travis. "Don\'t leave the path!"'], given: 1, flow: ['돌아서 뛰기 시작함', '너무 겁에 질려 실수로 길을 벗어남', 'Travis: 길을 벗어나지 말아요!'], ex: '정답 ▶ ①\n이유: Travis가 \'길을 벗어나지 말라\'고 외친 이유가 Eckels가 \'길을 벗어났기\' 때문이에요. 그래서 그 바로 앞에 와요.' },
      { lines: ['Travis and the other travelers returned safely to the machine and found Eckels inside.', '"You put all of us in danger," said Travis to Eckels in an angry voice.', '"You left the path."'], given: 1, flow: ['안전하게 돌아와 안에 있는 Eckels를 발견', '당신이 우리 모두를 위험에 빠뜨렸어요', '당신이 길을 벗어났잖아요'], ex: '정답 ▶ ①\n이유: Eckels를 발견한 뒤 → \'우리를 위험에 빠뜨렸다\'며 화를 내고 → 그 이유(길을 벗어났다)를 말해요.' },
      { lines: ['Eckels looked around the room carefully.', 'Everything looked the same, except the big sign on the wall.', 'The sign now said, "NAIM ANY YEER EN THE PAST. WEE TAEK YU THAIR."'], given: 1, flow: ['방을 주의 깊게 둘러봄', '간판만 빼고 모두 똑같아 보임', '간판에 이상한 글자가 쓰여 있음'], ex: '정답 ▶ ①\n이유: \'간판만 빼고 똑같았다\'고 먼저 말한 뒤, 그 간판이 어떻게 바뀌었는지(이상한 철자) 보여 줘요.' }
    ] },
    { type: 'odd', title: '어색한 문장', guide: '글의 흐름과 관계없는 문장을 고르세요.', items: [
      { lines: ['After some time, Travis whispered, "Look over there. There is a T. rex."', 'One hundred meters away, a T. rex slowly appeared.', 'Eckels walked closer to take a picture of it.', '"It ... is huge. I\'ve never seen such a huge thing. I\'m so scared," said Eckels.'], odd: 2, ex: '정답 ▶ ③\n이유: Eckels는 공룡이 너무 커서 무서워 숨도 못 쉬었어요. \'사진을 찍으려고 가까이 걸어갔다\'는 흐름과 맞지 않아요.' },
      { lines: ['"I\'m sorry, but I didn\'t kill anything," said Eckels.', '"There\'s only a little mud on my shoes."', 'Eckels cleaned his shoes carefully before he got in.', 'Travis stared at Eckels for a long time without saying anything.'], odd: 2, ex: '정답 ▶ ③\n이유: 바로 앞에서 \'신발에 진흙이 조금 묻었다\'고 했고, 나중에 그 진흙에서 나비를 발견해요. \'신발을 깨끗이 닦았다\'는 내용과 맞지 않아요.' },
      { lines: ['Eckels was confused.', 'Then, he saw the TV.', 'Everything on the TV was the same as before.', 'The new president was on the news, but it was not Mr. Keith.'], odd: 2, ex: '정답 ▶ ③\n이유: 바로 다음 문장에서 새 대통령이 Keith 씨가 아니었다고 해요. \'TV의 모든 것이 전과 같았다\'는 정반대예요.' }
    ] },
    { type: 'blank', title: '빈칸추론', guide: '빈칸에 들어갈 말로 가장 알맞은 것을 고르세요.', items: [
      { s: 'He was so terrified that he left the ____ by accident.', opts: ['path', 'machine', 'office', 'present'], ex: '정답 ▶ path\n이유: Travis가 절대 벗어나지 말라던 \'길\'을 실수로 벗어났어요. 그래서 Travis가 \'Don\'t leave the path!\'라고 외쳐요.' },
      { s: 'Travis and the other travelers returned safely to the machine and found Eckels ____.', opts: ['inside', 'on the path', 'with the T. rex', 'in the office'], ex: '정답 ▶ inside\n이유: 먼저 도망친 Eckels는 이미 타임머신 \'안에\' 있었어요.' },
      { s: 'In the mud on his right shoe, he found a small dead ____.', opts: ['butterfly', 'dinosaur', 'bird', 'flower'], ex: '정답 ▶ butterfly\n이유: 제목(A Butterfly That Changed the Future)처럼, 길을 벗어날 때 밟은 \'나비 한 마리\'가 미래를 바꿨어요.' }
    ] },
    { type: 'mc', title: '핵심문법', guide: '알맞은 답을 고르세요.', items: [
      { q: '밑줄 친 부분과 현재완료의 쓰임이 <b>같은</b> 것은?<br><b>I<u>\'ve never seen</u> such a huge thing.</b>', opts: ['Have you ever been to Jeju Island?', 'I have lived here for three years.', 'She has just finished her homework.', 'He has lost his key.'], ex: '정답 ▶ Have you ever been to Jeju Island?\n이유: never, ever와 함께 \'~해 본 적이 있다/없다\'를 나타내는 경험 용법이에요.\n오답 ▶ for three years(계속), just(완료), has lost(결과: 잃어버려서 지금 없다)' },
      { q: '빈칸에 알맞은 것은?<br><b>"Let\'s ______ home," said Travis finally.</b>', opts: ['go', 'to go', 'going', 'went'], ex: '정답 ▶ go\n이유: Let\'s + 동사원형 = ~하자 (제안). Let\'s go home. = 집에 갑시다.\n오답 ▶ to go, going, went ✘\n포인트 ▶ 부정은 Let\'s not + 동사원형 (Let\'s not leave the path.)' },
      { q: '빈칸에 알맞은 것은?<br><b>Travis didn\'t want Eckels ______ anything foolish.</b>', opts: ['to do', 'do', 'doing', 'did'], ex: '정답 ▶ to do\n이유: want + 목적어 + to부정사 = (목적어)가 ~하기를 원하다' },
      { q: '밑줄 친 부분의 뜻으로 알맞은 것은?<br><b>Travis stared at Eckels <u>without saying anything</u>.</b>', opts: ['아무 말 없이', '무언가를 말하면서', '아무것도 듣지 않고', '말할 것이 없어서'], ex: '정답 ▶ 아무 말 없이\n이유: without + -ing = ~하지 않고. without saying anything = 아무것도 말하지 않고' },
      { q: '밑줄 친 부분의 뜻으로 알맞은 것은?<br><b>"No, it <u>can\'t be</u>," said Eckels.</b>', opts: ['~일 리가 없다', '~임에 틀림없다', '~할 수 있다', '~해서는 안 된다'], ex: '정답 ▶ ~일 리가 없다\n이유: can\'t be = 강한 부정의 추측. 나비 한 마리 때문에 세상이 바뀐 걸 믿을 수 없어서 하는 말이에요.\n비교 ▶ must be = ~임에 틀림없다' },
      { q: '빈칸에 알맞은 것은?<br><b>It\'s all ______ this little thing?</b>', opts: ['because of', 'because', 'so', 'but'], ex: '정답 ▶ because of\n이유: 뒤에 명사(this little thing)가 오면 because of. because 뒤에는 \'주어 + 동사\'가 와요.\n예 ▶ because of the rain / because it rained' },
      { q: '빈칸에 알맞은 것은?<br><b>Everything looked ______, except the big sign on the wall.</b>', opts: ['the same', 'samely', 'sameness', 'to same'], ex: '정답 ▶ the same\n이유: look + 형용사(보어) = ~해 보이다. look the same = 똑같아 보이다\n오답 ▶ samely(없는 말), sameness(명사), to same(✘)' }
    ] },
    { type: 'mc', title: '요약문 완성', guide: '본문을 읽고 요약문의 빈칸 (A), (B)에 들어갈 말을 고르세요.', items: [
      { n: '❹', box: ['❹'], q: '다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 알맞은 것은?<br><b>When Eckels saw the huge T. rex, he became so (A) ______ that he (B) ______ the path by accident.</b>', opts: ['(A) terrified – (B) left', '(A) calm – (B) left', '(A) terrified – (B) followed', '(A) excited – (B) followed', '(A) calm – (B) cleaned'], ex: '정답 ▶ (A) terrified – (B) left\n(A) 거대한 공룡을 보고 \'너무 겁에 질렸다(so terrified)\' → terrified\n(B) 실수로 길을 \'벗어났다(left the path)\' → left\n오답 ▶ calm(침착한)·excited(신이 난)는 그때 기분이 아니고, followed(따라갔다)·cleaned(청소했다)는 본문과 반대이거나 관계없어요.', ev: ['I\'m so scared', 'He was so terrified that he left the path by accident'] },
      { n: '❻', box: ['❺', '❻'], q: '다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 알맞은 것은?<br><b>After returning to the present, Eckels found that the sign and the (A) ______ were different because he killed a (B) ______ in the past.</b>', opts: ['(A) president – (B) butterfly', '(A) president – (B) dinosaur', '(A) machine – (B) butterfly', '(A) machine – (B) dinosaur', '(A) guide – (B) bird'], ex: '정답 ▶ (A) president – (B) butterfly\n(A) 간판과 함께 달라진 것 → 새 대통령(president)이 Keith 씨가 아니었어요.\n(B) 신발의 진흙에서 발견한 것 → 죽은 나비(butterfly)\n오답 ▶ machine(기계)·guide(안내원)는 바뀌지 않았고, dinosaur(공룡)·bird(새)는 죽인 것이 아니에요.', ev: ['The new president was on the news, but it was not Mr. Keith', 'he found a small dead butterfly'] }
    ] }
  ] }
  ]
};
