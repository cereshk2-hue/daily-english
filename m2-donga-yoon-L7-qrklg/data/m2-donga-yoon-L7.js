/* 중2 동아(윤정미) Lesson 7 · Let's Enjoy Festivals (본문: Seasonal Festivals Around the World)
   작성 규칙은 README.md 의 "데이터 작성 규칙". insert: given = 빠지는 문장 번호(0부터), odd = 어색한 문장 번호 */
window.PKG = {
  id: 'm2-donga-yoon-L7',
  school: '중2 동아(윤정미)',
  unit: 'Lesson 7',
  title: 'Seasonal Festivals Around the World',
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
  }
  ]
};
