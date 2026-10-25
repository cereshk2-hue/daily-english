/* 고2 영어Ⅱ NE능률(오선영) Lesson 3 · Life Is a Sum of Choices (본문: 같은 투표, 다른 승자)
   작성 규칙은 README.md 의 "데이터 작성 규칙". 고등은 본문이 길어 DAY 3개로 나눔 */
window.PKG = {
  id: 'h2-ne-oh-L3',
  school: '고2 능률(오선영)',
  unit: '영어Ⅱ Lesson 3',
  title: 'Life Is a Sum of Choices',
  titleKo: '삶은 선택의 합',
  exam: '2학기 기말고사',
  prose: true,
  stepsBefore: ["핵심어휘·숙어", "어휘선택", "T/F 내용 확인", "어법선택", "동사변형", "오류찾기", "본문 스크램블", "문장순서", "문장삽입", "어색한 문장", "빈칸추론", "핵심문법"],   /* 일치·불일치 추가 전 단계 이름: 예전 기록을 새 단계에 맞추는 데 씀 */
  teacherPhone: '',            /* 결과 받을 번호. 예: '010-1234-5678' */

  days: [
  /* ═══════════════════════════ DAY 1 · 본문 ❶❷❸ ═══════════════════════════ */
  {
    id: 'd1', name: 'DAY 1', range: '3과 본문 ❶❷❸', story: '집단 의사 결정과 투표 · 학생 자치회의 투표 준비',
    passage: [
      ['', '❶', ''],
      ['', 'We make many personal choices in our lives, from who to have lunch with to what career to pursue.', '우리는 누구와 점심을 먹을 것인지부터 어떠한 직업을 추구할 것인지까지 우리의 삶에서 많은 개인적인 선택을 한다.'],
      ['', 'However, there are many situations where we must make decisions as a group.', '하지만, 우리가 집단으로서 결정을 내려야 하는 상황들이 많이 있다.'],
      ['', 'Group decision-making is not as simple as our personal choices, as it involves numerous voices with differing opinions.', '집단 의사 결정은 다른 의견을 가진 수많은 목소리를 수반하기 때문에 우리의 개인적인 선택들만큼 간단하지 않다.'],
      ['', 'Voting is often used to make group decisions fairer and more efficient, and various voting methods have been developed over time.', '투표는 흔히 집단 의사 결정을 더 공정하고 더 효율적으로 만들기 위해 사용되며, 시간이 흐르면서 다양한 투표 방법이 개발되어 왔다.'],
      ['', 'The following story illustrates how these different voting methods work.', '다음 이야기는 이러한 다양한 투표 방법이 어떻게 적용되는지 보여준다.'],
      ['', '❷', ''],
      ['', 'The members of the Greenville High School student council needed to decide how to raise money for children in need.', 'Greenville 고등학교 학생 자치회의 구성원들은 어려움에 처한 아이들을 위해 모금할 방법을 결정해야 했다.'],
      ['', 'Their three options were an art show, a bake sale, and a charity concert, but there were conflicting opinions.', '그들의 세 가지 선택지는 미술 전시회, 빵 바자회, 그리고 자선 콘서트였지만, 상충되는 의견들이 있었다.'],
      ['', 'So they decided to put it to a vote.', '그래서 그들은 그것을 투표에 부치기로 결정했다.'],
      ['', "When they asked for advice from Ms. Akers, the council's advisor, she encouraged them not to use the familiar voting method, but to try something different instead.", '그들이 자치회의 고문 교사인 Akers 선생님에게 조언을 구했을 때, 그녀는 익숙한 투표 방법을 사용하지 말고, 대신 다른 것을 시도해 보라고 권장했다.'],
      ['', 'After doing some research, the council members decided to try three different voting systems: the first-past-the-post (FPTP) method, the alternative vote (AV) method, and the Condorcet method.', '약간의 조사를 한 후, 자치회 구성원들은 단순 다수결(FPTP) 방식, 대안 투표(AV) 방식, 그리고 콩도르세 방식이라는 세 가지의 다른 투표 시스템을 시도해 보기로 결정했다.'],
      ['', 'The entire council was curious to find out if the different methods would yield different results.', '모든 자치회 구성원들은 각각 다른 방법이 서로 다른 결과를 낼지 궁금해했다.'],
      ['', '❸', ''],
      ['', 'On the day of the vote, each possible event was given a letter: "art show" was represented by the letter A, the letter B indicated "bake sale," and C stood for "charity concert."', '투표 당일, 각각의 가능한 행사에 글자가 하나씩 부여되었다. \'미술 전시회\'는 글자 A로 표시되었고, 글자 B는 \'빵 바자회\'를 나타냈으며, C는 \'자선 콘서트\'를 의미했다.'],
      ['', 'Each of the 20 council members was given a voting slip and instructed to write down the options in order of preference.', '20명의 자치회 구성원들 각각은 투표용지를 받았고, 선호하는 순서대로 선택지를 적으라는 지시를 받았다.'],
      ['', 'For example, if the charity concert was their first choice, followed by the bake sale and the art show, they would write CBA.', '예를 들어, 자선 콘서트가 첫 번째 선택이고 빵 바자회와 미술 전시회가 뒤따른다면, 그들은 CBA를 적을 것이다.'],
      ['', 'After every member had voted, the voting slips were counted.', '모든 구성원이 투표를 마친 후, 투표용지가 집계되었다.'],
      ['', 'The results were as follows:', '결과는 다음과 같았다.']
    ],
    steps: [
      { type: 'vocab', title: '핵심어휘·숙어', quizN: 15, items: [
        ['personal', '개인적인'], ['career', '직업, 경력'], ['pursue', '추구하다'], ['situation', '상황'],
        ['decision-making', '의사 결정'], ['involve', '수반하다, 포함하다'], ['numerous', '수많은'], ['differing', '서로 다른'],
        ['fair', '공정한'], ['efficient', '효율적인'], ['method', '방법, 방식'], ['illustrate', '보여 주다, 설명하다'],
        ['student council', '학생 자치회'], ['raise money', '모금하다'], ['in need', '어려움에 처한'], ['option', '선택지'],
        ['charity', '자선'], ['conflicting', '상충되는, 상반된'], ['put ~ to a vote', '~을 투표에 부치다'], ['advisor', '고문, 지도 교사'],
        ['encourage A to ~', 'A에게 ~하도록 권장하다'], ['familiar', '익숙한'], ['alternative', '대안의'], ['entire', '전체의'],
        ['yield', '(결과를) 내다, 산출하다'], ['represent', '나타내다, 상징하다'], ['indicate', '나타내다, 가리키다'], ['stand for', '~을 뜻하다'],
        ['voting slip', '투표용지'], ['instruct A to ~', 'A에게 ~하도록 지시하다'], ['in order of preference', '선호하는 순서대로'], ['as follows', '다음과 같이']
      ]},
      { type: 'pick', title: '어휘선택', guide: '문맥에 맞는 낱말을 고르세요.', items: [
        { s: 'We make many {personal|personnel} choices in our lives, from who to have lunch with to what career to pursue.', ex: "personal 개인적인 vs personnel 인사의, 직원의 (철자 혼동)" },
        { s: 'Group decision-making is not as simple as our personal choices, as it involves numerous voices with {differing|deferring} opinions.', ex: "differing 서로 다른 vs deferring 미루는, 따르는 (철자 혼동)" },
        { s: 'Voting is often used to make group decisions fairer and more {efficient|sufficient}, and various voting methods have been developed over time.', ex: "efficient 효율적인 vs sufficient 충분한 (철자 혼동)" },
        { s: 'The following story {illustrates|imitates} how these different voting methods work.', ex: "illustrate 보여 주다, 설명하다 vs imitate 모방하다" },
        { s: 'Their three options were an art show, a bake sale, and a charity concert, but there were {conflicting|confining} opinions.', ex: "conflicting 상충되는 vs confining 제한하는 (철자 혼동)" },
        { s: "When they asked for advice from Ms. Akers, the council's advisor, she encouraged them not to use the {familiar|familial} voting method, but to try something different instead.", ex: "familiar 익숙한 vs familial 가족의 (철자 혼동)" },
        { s: 'The entire council was curious to find out if the different methods would {yield|wield} different results.', ex: "yield (결과를) 내다 vs wield (권력 등을) 행사하다" },
        { s: 'On the day of the vote, each possible event was given a letter: "art show" was {represented|repressed} by the letter A, the letter B indicated "bake sale," and C stood for "charity concert."', ex: "represent 나타내다 vs repress 억압하다" },
        { s: 'Each of the 20 council members was given a voting slip and instructed to write down the options in order of {preference|reference}.', ex: "preference 선호 vs reference 참고, 언급" },
        { s: 'After every member had voted, the voting slips were {counted|countered}.', ex: "count 집계하다 vs counter 반박하다" }
      ]},
      { type: 'tf', title: 'T/F 내용 확인', guide: '본문 내용과 일치하면 T, 다르면 F를 고르세요.', items: [
        ["Collective decision-making is less intricate than making individual choices.", false, "intricate 복잡한 · collective = group · individual = personal → 집단 결정은 개인 선택만큼 간단하지 않다"],
        ["An array of voting methods has evolved over time.", true, "an array of 다양한 (= various) · evolve 발전하다 (≒ be developed)"],
        ["The council sought to raise funds for underprivileged children.", true, "seek to ~하려고 하다 · funds = money · underprivileged = in need"],
        ["The council members unanimously backed one option from the outset.", false, "unanimously 만장일치로 · from the outset 처음부터 → 의견이 엇갈렸음(conflicting opinions)"],
        ["Ms. Akers urged the council to adhere to the customary voting method.", false, "urge 촉구하다 · adhere to 고수하다 · customary = familiar → 다른 것을 시도하라고 권함"],
        ["The council opted to experiment with three distinct voting systems.", true, "opt to = decide to · distinct = different"],
        ["In the vote, the letter C denoted the bake sale.", false, "denote = stand for → C는 자선 콘서트, 빵 바자회는 B"],
        ["Each member ranked the options according to personal preference.", true, "rank 순위를 매기다 = write down the options in order of preference"]
      ]},
      { type: 'mc', title: '일치·불일치', guide: "선택지는 본문을 어려운 어휘로 바꿔 쓴 문장이에요. 풀고 나서 해설의 어휘를 꼭 확인하세요.", items: [
        { n: "❷", box: ["❶", "❷"], q: "글의 내용과 일치하지 <u>않는</u> 것은?", opts: ["Ms. Akers urged the council to stick with the conventional voting method.", "Collective decisions are more intricate than individual ones because they entail many divergent views.", "Voting is employed to render group decisions more equitable and efficient.", "The council aimed to raise funds for underprivileged children.", "The council members were eager to see whether different methods would produce different outcomes."], ex: "정답: urge : 촉구하다 · stick with : 고수하다 · conventional = familiar → 실제로는 다른 것을 시도하라고 권함\n· collective = group · intricate : 복잡한 (↔ simple) · entail = involve · divergent = differing\n· employ = use · render : ~하게 만들다 · equitable = fair\n· funds = money · underprivileged = in need\n· eager to = curious to · produce = yield · outcome = result", per: [["Akers 선생님은 자치회에 기존 투표 방식을 고수하라고 촉구했다.", "she encouraged them not to use the familiar voting method", "불일치 → 익숙한 방식 말고 다른 것을 시도하라고 권함"], ["집단 결정은 서로 다른 의견을 많이 수반해서 개인 결정보다 복잡하다.", "it involves numerous voices with differing opinions", "일치"], ["투표는 집단 결정을 더 공정하고 효율적으로 만드는 데 쓰인다.", "Voting is often used to make group decisions fairer and more efficient", "일치"], ["자치회는 어려운 처지의 아이들을 위해 기금을 모으려 했다.", "raise money for children in need", "일치"], ["자치회 구성원들은 방식에 따라 결과가 달라지는지 알고 싶어 했다.", "was curious to find out if the different methods would yield different results", "일치"]] },
        { n: "❸", box: ["❸"], q: "글의 내용과 <u>일치하는</u> 것은?", opts: ["Members were directed to rank the options according to their preferences.", "Each event was assigned a number rather than a letter.", "Only half of the council members cast a ballot.", "Members were allowed to choose just one option on their ballots.", "The letter B denoted the charity concert."], ex: "정답: direct : 지시하다 (= instruct) · rank : 순위를 매기다 · according to one's preferences = in order of preference\n· assign : 부여하다 (= give) · cast a ballot : 투표하다 (= vote) · ballot = voting slip\n· denote : 나타내다 (= indicate, stand for)", per: [["구성원들은 선호에 따라 선택지에 순위를 매기라는 지시를 받았다.", "instructed to write down the options in order of preference", "일치"], ["각 행사에는 글자가 아니라 숫자가 부여되었다.", "each possible event was given a letter", "불일치 → 글자가 부여됨"], ["자치회 구성원의 절반만 투표했다.", ["Each of the 20 council members was given a voting slip", "After every member had voted"], "불일치 → 모두 투표함"], ["구성원들은 투표용지에 선택지 하나만 고를 수 있었다.", "write down the options in order of preference", "불일치 → 선호 순서대로 모두 적음"], ["글자 B는 자선 콘서트를 나타냈다.", "the letter B indicated", "불일치 → B는 빵 바자회, C가 자선 콘서트"]] }
      ]},
      { type: 'pick', title: '어법선택', guide: '어법상 알맞은 것을 고르세요.', items: [
        { s: 'However, there are many situations {where|which} we must make decisions as a group.', ex: '뒤에 완전한 절 + 선행사 situations → 관계부사 where' },
        { s: 'Group decision-making is not as {simple|simply} as our personal choices, as it involves numerous voices with differing opinions.', ex: 'be동사의 보어 → 형용사 원급 (as 형용사 as)' },
        { s: 'Voting is often used to make group decisions {fairer|more fairly} and more efficient, and various voting methods have been developed over time.', ex: 'make + O + 형용사(목적격 보어)' },
        { s: 'Voting is often used to make group decisions fairer and more efficient, and various voting methods {have been developed|have developed} over time.', ex: '방법이 "개발되는" 것 → 현재완료 수동태' },
        { s: 'The following story illustrates {how|what} these different voting methods work.', ex: '뒤에 완전한 절 → 간접의문문 how' },
        { s: 'The members of the Greenville High School student council needed to decide {how to raise|how raising} money for children in need.', ex: '의문사 + to부정사' },
        { s: "When they asked for advice from Ms. Akers, the council's advisor, she encouraged them not {to use|using} the familiar voting method, but to try something different instead.", ex: 'encourage + O + (not) to부정사' },
        { s: 'The entire council was curious to find out {if|that} the different methods would yield different results.', ex: '"~인지 아닌지" → if(whether)' },
        { s: 'Each of the 20 council members {was|were} given a voting slip and instructed to write down the options in order of preference.', ex: 'each of + 복수명사 → 단수동사' },
        { s: 'For example, if the charity concert was their first choice, {followed|following} by the bake sale and the art show, they would write CBA.', ex: '첫 번째 선택이 다른 것에 "뒤따라지는" → 과거분사 followed' },
        { s: 'After every member {had voted|has voted}, the voting slips were counted.', ex: '집계(과거)보다 먼저 → 과거완료 had voted' }
      ]},
      { type: 'verb', title: '동사변형', guide: '( ) 안의 동사를 알맞은 형태로 바꿔 쓰세요.', items: [
        { s: 'We make many personal choices in our lives, from who to have lunch with to what career ___.', v: 'pursue', a: ['to pursue'], ex: '의문사 + to부정사' },
        { s: 'However, there ___ many situations where we must make decisions as a group.', v: 'be', a: ['are'], ex: 'there + be + 복수주어 → are' },
        { s: 'Group decision-making is not as simple as our personal choices, as it ___ numerous voices with differing opinions.', v: 'involve', a: ['involves'], ex: '주어 it(단수) → involves' },
        { s: 'Voting is often used to make group decisions fairer and more efficient, and various voting methods have been ___ over time.', v: 'develop', a: ['developed'], ex: '현재완료 수동태 have been p.p.' },
        { s: 'The members of the Greenville High School student council needed to decide how ___ money for children in need.', v: 'raise', a: ['to raise'], ex: '의문사 + to부정사' },
        { s: 'So they decided ___ it to a vote.', v: 'put', a: ['to put'], ex: 'decide + to부정사' },
        { s: "When they asked for advice from Ms. Akers, the council's advisor, she encouraged them not ___ the familiar voting method, but to try something different instead.", v: 'use', a: ['to use'], ex: 'encourage + O + not to부정사' },
        { s: 'After ___ some research, the council members decided to try three different voting systems: the first-past-the-post (FPTP) method, the alternative vote (AV) method, and the Condorcet method.', v: 'do', a: ['doing'], ex: '전치사 after + 동명사' },
        { s: 'Each of the 20 council members was given a voting slip and ___ to write down the options in order of preference.', v: 'instruct', a: ['instructed'], ex: 'was given and (was) instructed → 수동태 병렬' },
        { s: 'For example, if the charity concert was their first choice, ___ by the bake sale and the art show, they would write CBA.', v: 'follow', a: ['followed'], ex: '수동 의미 분사 → followed' },
        { s: 'After every member had ___, the voting slips were counted.', v: 'vote', a: ['voted'], ex: '과거완료 had p.p.' }
      ]},
      { type: 'error', title: '오류찾기', guide: '어법상 틀린 곳을 고르세요.', items: [
        { s: 'We make many [[personal]] choices in our lives, from who to have lunch [[with]] to what career [[to pursue]]. However, there [[is]] many situations [[where]] we must make decisions as a group.', w: 3, fix: 'are', ex: 'there + be + 복수주어(many situations) → are' },
        { s: 'Group decision-making is not as [[simply]] as our personal choices, as it [[involves]] numerous voices with [[differing]] opinions. Voting is often used [[to make]] group decisions [[fairer]] and more efficient.', w: 0, fix: 'simple', ex: 'be동사 보어 → 형용사 simple' },
        { s: 'Voting is often used to make group decisions fairer and more efficient, and various voting methods [[have developed]] over time. The [[following]] story illustrates [[how]] these different voting methods [[work]].', w: 0, fix: 'have been developed', ex: '방법은 개발되는 것 → 현재완료 수동태' },
        { s: "When they asked [[for]] advice from Ms. Akers, the council's advisor, she encouraged them not [[using]] the [[familiar]] voting method, but [[to try]] something different [[instead]].", w: 1, fix: 'to use', ex: 'encourage + O + not to부정사, but to부정사 (병렬)' },
        { s: 'The entire council [[was]] curious [[to find out]] [[that]] the different methods would [[yield]] different results.', w: 2, fix: 'if', ex: '"~인지 아닌지" → if / whether' },
        { s: 'Each of the 20 council members [[were]] given a voting slip and [[instructed]] to [[write down]] the options [[in order of]] preference.', w: 0, fix: 'was', ex: 'each of + 복수명사 → 단수동사 was' },
        { s: 'For example, if the charity concert [[was]] their first choice, [[following]] by the bake sale and the art show, they [[would write]] CBA. After every member [[had voted]], the voting slips [[were counted]].', w: 1, fix: 'followed', ex: '"뒤따라지는" 수동 의미 → followed' }
      ]},
      { type: 'scramble', title: '본문 스크램블', guide: '우리말에 맞게 단어를 눌러 문장을 완성하세요.', items: [
        { ko: '하지만, 우리가 집단으로서 결정을 내려야 하는 상황들이 많이 있다.', en: 'However, there are many situations where we must make decisions as a group.' },
        { ko: '다음 이야기는 이러한 다양한 투표 방법이 어떻게 적용되는지 보여준다.', en: 'The following story illustrates how these different voting methods work.' },
        { ko: '그래서 그들은 그것을 투표에 부치기로 결정했다.', en: 'So they decided to put it to a vote.' },
        { ko: '모든 자치회 구성원들은 각각 다른 방법이 서로 다른 결과를 낼지 궁금해했다.', en: 'The entire council was curious to find out if the different methods would yield different results.' },
        { ko: '모든 구성원이 투표를 마친 후, 투표용지가 집계되었다.', en: 'After every member had voted, the voting slips were counted.' },
        { ko: '집단 의사 결정은 우리의 개인적인 선택들만큼 간단하지 않다.', en: 'Group decision-making is not as simple as our personal choices.' }
      ]},
      { type: 'order', title: '문장순서', guide: '문장을 본문 순서대로 눌러서 배열하세요.', items: [
        { lines: [
          'We make many personal choices in our lives, from who to have lunch with to what career to pursue.',
          'However, there are many situations where we must make decisions as a group.',
          'Group decision-making is not as simple as our personal choices, as it involves numerous voices with differing opinions.',
          'Voting is often used to make group decisions fairer and more efficient, and various voting methods have been developed over time.',
          'The following story illustrates how these different voting methods work.'
        ]},
        { lines: [
          'The members of the Greenville High School student council needed to decide how to raise money for children in need.',
          'Their three options were an art show, a bake sale, and a charity concert, but there were conflicting opinions.',
          'So they decided to put it to a vote.',
          "When they asked for advice from Ms. Akers, the council's advisor, she encouraged them not to use the familiar voting method, but to try something different instead."
        ]},
        { lines: [
          "When they asked for advice from Ms. Akers, the council's advisor, she encouraged them not to use the familiar voting method, but to try something different instead.",
          'After doing some research, the council members decided to try three different voting systems: the first-past-the-post (FPTP) method, the alternative vote (AV) method, and the Condorcet method.',
          'The entire council was curious to find out if the different methods would yield different results.'
        ]},
        { lines: [
          'Each of the 20 council members was given a voting slip and instructed to write down the options in order of preference.',
          'For example, if the charity concert was their first choice, followed by the bake sale and the art show, they would write CBA.',
          'After every member had voted, the voting slips were counted.',
          'The results were as follows:'
        ]}
      ]},
      { type: 'insert', title: '문장삽입', guide: '주어진 문장이 들어가기에 가장 알맞은 곳을 고르세요.', items: [
        { lines: [
          'We make many personal choices in our lives, from who to have lunch with to what career to pursue.',
          'However, there are many situations where we must make decisions as a group.',
          'Group decision-making is not as simple as our personal choices, as it involves numerous voices with differing opinions.',
          'Voting is often used to make group decisions fairer and more efficient, and various voting methods have been developed over time.'
        ], given: 1, ex: 'However로 "개인적 선택"과 "집단 결정"을 대조한다.' },
        { lines: [
          'The members of the Greenville High School student council needed to decide how to raise money for children in need.',
          'Their three options were an art show, a bake sale, and a charity concert, but there were conflicting opinions.',
          'So they decided to put it to a vote.',
          "When they asked for advice from Ms. Akers, the council's advisor, she encouraged them not to use the familiar voting method, but to try something different instead."
        ], given: 2, ex: '의견이 엇갈려서(So) 투표에 부쳤다. it은 모금 방법 결정을 가리킨다.' },
        { lines: [
          "When they asked for advice from Ms. Akers, the council's advisor, she encouraged them not to use the familiar voting method, but to try something different instead.",
          'After doing some research, the council members decided to try three different voting systems: the first-past-the-post (FPTP) method, the alternative vote (AV) method, and the Condorcet method.',
          'The entire council was curious to find out if the different methods would yield different results.'
        ], given: 1, ex: '다른 방식을 시도하라는 조언 → 조사 후 세 가지 방식을 정함' },
        { lines: [
          'Each of the 20 council members was given a voting slip and instructed to write down the options in order of preference.',
          'For example, if the charity concert was their first choice, followed by the bake sale and the art show, they would write CBA.',
          'After every member had voted, the voting slips were counted.'
        ], given: 1, ex: 'For example로 "선호하는 순서대로 적기"를 구체적으로 보여 준다.' }
      ]},
      { type: 'odd', title: '어색한 문장', guide: '글의 흐름과 관계없는 문장을 고르세요.', items: [
        { lines: [
          'We make many personal choices in our lives, from who to have lunch with to what career to pursue.',
          'However, there are many situations where we must make decisions as a group.',
          'Making decisions as a group is always quick and easy.',
          'Group decision-making is not as simple as our personal choices, as it involves numerous voices with differing opinions.'
        ], odd: 2, ex: '집단 결정은 간단하지 않다는 흐름과 반대된다.' },
        { lines: [
          'Their three options were an art show, a bake sale, and a charity concert, but there were conflicting opinions.',
          'So they decided to put it to a vote.',
          'Ms. Akers decided the event by herself without a vote.',
          "When they asked for advice from Ms. Akers, the council's advisor, she encouraged them not to use the familiar voting method, but to try something different instead."
        ], odd: 2, ex: '자치회가 투표로 정했다는 내용과 맞지 않는다.' },
        { lines: [
          'Each of the 20 council members was given a voting slip and instructed to write down the options in order of preference.',
          'The members were told to choose only one option and leave the others blank.',
          'For example, if the charity concert was their first choice, followed by the bake sale and the art show, they would write CBA.',
          'After every member had voted, the voting slips were counted.'
        ], odd: 1, ex: '세 선택지를 모두 선호 순서대로 적었다.' }
      ]},
      { type: 'blank', title: '빈칸추론', guide: '빈칸에 들어갈 말로 가장 알맞은 것을 고르세요.', items: [
        { s: 'Group decision-making is not as simple as our personal choices, as it involves numerous voices with ____.', opts: ["differing opinions", "identical opinions", "personal choices", "a single voice"], ex: '여러 의견이 엇갈려서 간단하지 않다.' },
        { s: 'Voting is often used to make group decisions ____, and various voting methods have been developed over time.', opts: ["fairer and more efficient", "simpler and more personal", "faster but less fair", "more familiar and traditional"], ex: '투표는 결정을 공정하고 효율적으로 만든다.' },
        { s: "When they asked for advice from Ms. Akers, the council's advisor, she encouraged them not to use the familiar voting method, but to ____ instead.", opts: ["try something different", "use the familiar method", "put it to a vote", "do some research"], ex: '익숙한 방식 대신 다른 것을 시도하라고 권했다.' },
        { s: 'Each of the 20 council members was given a voting slip and instructed to write down the options ____.', opts: ["in order of preference", "in order of importance", "in alphabetical order", "by the number of votes"], ex: '예시(CBA)처럼 선호하는 순서대로 적었다.' }
      ]},
      { type: 'mc', title: '핵심문법', guide: '알맞은 답을 고르세요.', items: [
        { q: '밑줄 친 부분과 의미가 같은 것은?<br><b>They needed to decide <u>how to raise</u> money.</b>', opts: ['how they should raise', 'how should they raise', 'how they raise should', 'how raising'], ex: '의문사 + to부정사 = 의문사 + 주어 + should + 동사원형' },
        { q: '빈칸에 알맞은 것은?<br><b>There are many situations ______ we must make decisions as a group.</b>', opts: ['where', 'which', 'what', 'who'], ex: '선행사(situations) + 완전한 절 → 관계부사 where (= in which)' },
        { q: '빈칸에 알맞은 것은?<br><b>Group decision-making is not as ______ as our personal choices.</b>', opts: ['simple', 'simpler', 'simplest', 'simply'], ex: 'as + 형용사 원급 + as' },
        { q: '빈칸에 알맞은 것은?<br><b>Various voting methods ______ over time.</b>', opts: ['have been developed', 'have developed', 'has been developed', 'were developing'], ex: '복수 주어 + 수동 → have been p.p.' },
        { q: '빈칸에 알맞은 것은?<br><b>She encouraged them ______ the familiar method.</b>', opts: ['not to use', 'to not using', 'not using', "don't use"], ex: 'to부정사의 부정: not + to부정사' },
        { q: '빈칸에 알맞은 것은?<br><b>They wanted to find out ______ the methods would yield different results.</b>', opts: ['if', 'that', 'what', 'which'], ex: '"~인지 아닌지" → if / whether' },
        { q: '빈칸에 알맞은 것은?<br><b>Each possible event ______ a letter.</b>', opts: ['was given', 'gave', 'was giving', 'given'], ex: '4형식 수동태: A be given B (A가 B를 받다)' },
        { q: '빈칸에 알맞은 것은?<br><b>Each of the 20 council members ______ given a voting slip.</b>', opts: ['was', 'were', 'be', 'have'], ex: 'each of + 복수명사 → 단수동사' },
        { q: '빈칸에 알맞은 것은?<br><b>After every member ______, the voting slips were counted.</b>', opts: ['had voted', 'has voted', 'votes', 'will vote'], ex: '과거보다 더 이전 → 과거완료' }
      ]}
    ]
  },

  /* ═══════════════════════════ DAY 2 · 본문 ❹❺ ═══════════════════════════ */
  {
    id: 'd2', name: 'DAY 2', range: '3과 본문 ❹❺', story: '단순 다수결(FPTP) 방식 · 대안 투표(AV) 방식',
    passage: [
      ['', '❹', ''],
      ['', 'The First-Past-The-Post Method', '단순 다수결(FPTP) 방식'],
      ['', 'The FPTP method is the simplest of the three methods.', 'FPTP 방식은 세 가지 방식 중 가장 간단하다.'],
      ['', 'Voters are given several options, and whichever gets the most first-preference votes wins.', '투표자들에게는 여러 가지 선택지가 주어지고, 어떤 것이든 가장 많은 1지망 표를 얻은 것이 이긴다.'],
      ['', 'Neither the second nor third preference matters at all, so they are ignored.', '2지망도 3지망도 둘 다 전혀 중요하지 않으므로, 그것들은 무시된다.'],
      ['', 'This method is commonly used in political elections around the world.', '이 방식은 전 세계 정치 선거에서 흔히 사용된다.'],
      ['', 'The student council quickly determined that the winner would be option C, the charity concert.', '학생 자치회는 빠르게 자선 콘서트인 선택지 C가 승자가 될 것임을 알아냈다.'],
      ['', 'This was because it received 8 first-preference votes, while option A received 5 and option B received 7.', '이는 선택지 A는 5표, 선택지 B는 7표를 받은 반면, 그것은 8표의 1지망 표를 받았기 때문이었다.'],
      ['', 'The FPTP method is uncomplicated and easy to understand, but it has a significant weakness.', 'FPTP 방식은 복잡하지 않고 이해하기 쉽지만, 상당한 약점을 가지고 있다.'],
      ['', 'It is possible to win a vote without the support of the majority.', '과반수의 지지 없이도 투표에서 승리하는 것이 가능하다.'],
      ['', 'That was the case here.', '이것이 바로 그런 경우였다.'],
      ['', "According to the results of the FPTP method, the council's choice was to hold a charity concert.", 'FPTP 방식의 결과에 따르면, 자치회의 선택은 자선 콘서트를 개최하는 것이었다.'],
      ['', 'However, only 8 out of 20 council members chose the charity concert as their first preference, which equaled 40% of the total votes.', '하지만 20명의 자치회 구성원 중 8명만이 1지망으로 자선 콘서트를 골랐는데, 이는 전체 표의 40%에 해당했다.'],
      ['', '❺', ''],
      ['', 'The Alternative Vote Method', '대안 투표(AV) 방식'],
      ['', 'Next, the council members examined the votes using the AV method, and they soon realized that there would be a different result.', '다음으로, 자치회 구성원들은 AV 방식을 사용하여 표를 검토했고, 그들은 곧 다른 결과가 나올 것이라는 것을 깨달았다.'],
      ['', 'The AV method can potentially include more than one round of counting.', 'AV 방식은 잠재적으로 한 차례 이상의 집계를 포함할 수 있다.'],
      ['', 'For an option to win in the first round, it needs to get more than 50% of the first-preference votes.', '어떤 선택지가 1차 집계에서 승리하기 위해서는, 1지망 표의 50% 이상을 얻어야 한다.'],
      ['', 'As the charity concert only received 40% of the total votes, a second round of counting was required.', '자선 콘서트는 전체 표의 40%만을 받았기 때문에, 2차 집계가 필요했다.'],
      ['', 'Option A, the art show, received the fewest first-preference votes, with only 5 council members voting for it.', '미술 전시회인 선택지 A는 오직 5명의 자치회 구성원들만 그것에 투표하며 가장 적은 1지망 표를 받았다.'],
      ['', "Therefore, option A was eliminated, and the 5 council members' votes were redistributed based on their second preferences.", '따라서 선택지 A는 제거되었고, 5명의 자치회 구성원들의 표가 그들의 두 번째 선호도에 따라 재분배되었다.'],
      ['', 'As a result, 4 votes for option B (ABC) and 1 for option C (ACB) were added to the total.', '그 결과, 선택지 B에 4표(ABC), 선택지 C에 1표(ACB)가 합계에 추가되었다.'],
      ['', 'This meant that option B had 11 total votes, while option C had only 9.', '이것은 선택지 C는 9표밖에 얻지 못한 반면 선택지 B가 총 11표를 얻었다는 것을 의미했다.'],
      ['', 'As a result, the bake sale would be the winner.', '결과적으로, 빵 바자회가 승자가 될 것이었다.'],
      ['', 'Unfortunately, the AV method is not perfect either.', '안타깝게도, AV 방식도 완벽하지는 않다.'],
      ['', 'It sometimes allows second-preference votes to have a greater influence than first-preference votes.', '그것은 때때로 2지망 표가 1지망 표보다 더 큰 영향력을 갖게 하기도 한다.'],
      ['', 'In this case, the bake sale won, but this was mainly due to the second-preference votes it received.', '이 경우에는 빵 바자회가 승리했지만, 이는 주로 그것이 얻은 2지망 표 때문이었다.']
    ],
    steps: [
      { type: 'vocab', title: '핵심어휘·숙어', quizN: 15, items: [
        ['the simplest', '가장 간단한'], ['first-preference vote', '1지망 표'], ['whichever', '~하는 어느 것이든'], ['neither A nor B', 'A도 B도 아닌'],
        ['matter', '중요하다'], ['ignore', '무시하다'], ['commonly', '흔히, 일반적으로'], ['political', '정치의'],
        ['election', '선거'], ['determine', '알아내다, 결정하다'], ['while', '~인 반면에'], ['uncomplicated', '복잡하지 않은'],
        ['significant', '상당한, 중요한'], ['weakness', '약점'], ['majority', '과반수, 다수'], ['according to', '~에 따르면'],
        ['equal', '~와 같다, ~에 해당하다'], ['examine', '검토하다'], ['realize', '깨닫다'], ['potentially', '잠재적으로'],
        ['round', '(집계의) 차례, 회'], ['require', '필요로 하다'], ['eliminate', '제거하다'], ['redistribute', '재분배하다'],
        ['based on', '~에 근거하여'], ['as a result', '그 결과'], ['unfortunately', '안타깝게도'], ['influence', '영향력'],
        ['mainly', '주로'], ['due to', '~ 때문에']
      ]},
      { type: 'pick', title: '어휘선택', guide: '문맥에 맞는 낱말을 고르세요.', items: [
        { s: 'The FPTP method is the {simplest|most elaborate} of the three methods.', ex: "1지망만 세는 방식 → 가장 간단한(simplest). elaborate 정교한, 복잡한" },
        { s: 'Neither the second nor third preference matters at all, so they are {ignored|weighted}.', ex: "전혀 중요하지 않으니 무시된다(ignored). weight 가중치를 두다" },
        { s: 'This method is {commonly|seldom} used in political elections around the world.', ex: "commonly 흔히 vs seldom 좀처럼 ~않는" },
        { s: 'The FPTP method is {uncomplicated|convoluted} and easy to understand, but it has a significant weakness.', ex: "uncomplicated 복잡하지 않은 vs convoluted 난해한, 뒤얽힌" },
        { s: 'It is possible to win a vote without the support of the {majority|plurality}.', ex: "majority 과반수 vs plurality 최다 득표(과반 미달). C는 최다 득표였지만 과반이 아니었다." },
        { s: 'As the charity concert only received 40% of the total votes, a second round of counting was {required|acquired}.', ex: "require 필요로 하다 vs acquire 획득하다 (철자 혼동)" },
        { s: 'Option A, the art show, received the {fewest|most} first-preference votes, with only 5 council members voting for it.', ex: 'A(5) < B(7) < C(8) → 가장 적은(fewest)' },
        { s: "Therefore, option A was {eliminated|illuminated}, and the 5 council members' votes were redistributed based on their second preferences.", ex: "eliminate 제거하다 vs illuminate 밝히다 (철자 혼동)" },
        { s: 'It sometimes allows second-preference votes to have a greater {influence|affluence} than first-preference votes.', ex: "influence 영향력 vs affluence 풍요 (철자 혼동)" },
        { s: 'In this case, the bake sale won, but this was {mainly|hardly} due to the second-preference votes it received.', ex: "2지망 표 덕분에 이겼다 → 주로(mainly). hardly 거의 ~않다" }
      ]},
      { type: 'tf', title: 'T/F 내용 확인', guide: '본문 내용과 일치하면 T, 다르면 F를 고르세요.', items: [
        ["Under FPTP, lower-ranked preferences are entirely disregarded.", true, "lower-ranked 하위 순위의 · disregard = ignore · entirely = at all"],
        ["The FPTP method is seldom employed in political elections.", false, "seldom 좀처럼 ~않는 · employ = use → 실제로는 commonly used"],
        ["The charity concert prevailed under FPTP with eight first-preference votes.", true, "prevail = win"],
        ["The charity concert garnered the backing of most council members.", false, "garner 얻다 · backing = support → 8/20 = 40%, 과반 아님"],
        ["To triumph in the first AV round, an option must secure a majority of first-preference votes.", true, "triumph = win · secure 확보하다 · majority = more than 50%"],
        ["The bake sale was the first option to be eliminated under AV.", false, "가장 먼저 탈락한 것은 미술 전시회(A, 5표)"],
        ["Following the redistribution, option B tallied 11 votes.", true, "following = after · redistribution 재분배 · tally 집계되다, 총 ~가 되다"],
        ["The bake sale's victory hinged chiefly on first-preference votes.", false, "hinge on ~에 달려 있다 · chiefly = mainly → 실제로는 2지망 표 덕분"]
      ]},
      { type: 'mc', title: '일치·불일치', guide: "선택지는 본문을 어려운 어휘로 바꿔 쓴 문장이에요. 풀고 나서 해설의 어휘를 꼭 확인하세요.", items: [
        { n: "❹", box: ["❹"], q: "글의 내용과 일치하지 <u>않는</u> 것은?", opts: ["Under FPTP, the charity concert secured an outright majority.", "In FPTP, second and third preferences are disregarded entirely.", "FPTP is prevalent in political elections worldwide.", "The FPTP method is straightforward but has a considerable flaw.", "A candidate can prevail without majority backing under FPTP."], ex: "정답: secure : 확보하다 · outright majority : 확실한 과반 → 실제로는 40%\n· disregard = ignore · entirely = at all\n· prevalent : 널리 퍼진 (= commonly used) · worldwide = around the world\n· straightforward = uncomplicated · considerable = significant · flaw = weakness\n· prevail = win · backing = support", per: [["FPTP에서 자선 콘서트는 확실한 과반을 얻었다.", "only 8 out of 20 council members chose the charity concert as their first preference", "불일치 → 40%뿐, 과반 아님"], ["FPTP에서 2지망과 3지망은 완전히 무시된다.", "Neither the second nor third preference matters at all, so they are ignored", "일치"], ["FPTP는 전 세계 정치 선거에 널리 쓰인다.", "This method is commonly used in political elections around the world", "일치"], ["FPTP는 간단하지만 상당한 결점이 있다.", "uncomplicated and easy to understand, but it has a significant weakness", "일치"], ["FPTP에서는 과반의 지지 없이도 이길 수 있다.", "It is possible to win a vote without the support of the majority", "일치"]] },
        { n: "❺", box: ["❺"], q: "글의 내용과 <u>일치하는</u> 것은?", opts: ["In the AV count, the art show was eliminated and its votes were reallocated by second preference.", "The charity concert won in the first round of the AV method.", "An option needs at least a third of the first-preference votes to win the first round.", "After redistribution, the charity concert outnumbered the bake sale.", "The AV method is flawless because first preferences always carry the most weight."], ex: "정답: reallocate = redistribute (재분배하다) · eliminate : 제거하다\n· at least : 최소한 · a third : 3분의 1 → 실제로는 50% 초과\n· outnumber : ~보다 수가 많다 → 실제로는 B 11 vs C 9\n· flawless = perfect · carry weight : 영향력을 갖다 (= have influence)", per: [["AV 집계에서 미술 전시회가 탈락하고 그 표는 2지망에 따라 재분배되었다.", "option A was eliminated, and the 5 council members' votes were redistributed based on their second preferences", "일치"], ["AV 방식 1차 집계에서 자선 콘서트가 이겼다.", "a second round of counting was required", "불일치 → 2차 집계가 필요했음"], ["1차에서 이기려면 1지망 표의 최소 3분의 1이 필요하다.", "it needs to get more than 50% of the first-preference votes", "불일치 → 50% 초과"], ["재분배 후 자선 콘서트가 빵 바자회보다 표가 많았다.", "option B had 11 total votes, while option C had only 9", "불일치 → B 11표, C 9표"], ["1지망이 언제나 가장 큰 영향력을 가지므로 AV 방식은 완벽하다.", "It sometimes allows second-preference votes to have a greater influence than first-preference votes", "불일치 → 2지망이 더 큰 영향을 주기도 함"]] }
      ]},
      { type: 'pick', title: '어법선택', guide: '어법상 알맞은 것을 고르세요.', items: [
        { s: 'Voters are given several options, and whichever gets the most first-preference votes {wins|win}.', ex: 'whichever절(단수 취급)이 주어 → wins' },
        { s: 'Neither the second nor third preference {matters|matter} at all, so they are ignored.', ex: 'neither A nor B → B(third preference, 단수)에 수일치' },
        { s: 'Neither the second nor third preference matters at all, so they {are ignored|ignore}.', ex: '선호가 "무시되는" 것 → 수동태' },
        { s: 'The student council quickly determined {that|what} the winner would be option C, the charity concert.', ex: '뒤에 완전한 절 → 접속사 that' },
        { s: 'This was because it received 8 first-preference votes, {while|during} option A received 5 and option B received 7.', ex: '뒤에 절 → 접속사 while (during은 전치사)' },
        { s: 'It is possible {to win|win} a vote without the support of the majority.', ex: '가주어 It ~ 진주어 to부정사' },
        { s: 'However, only 8 out of 20 council members chose the charity concert as their first preference, {which|that} equaled 40% of the total votes.', ex: '콤마 뒤 계속적 용법 → which (that 불가)' },
        { s: 'Next, the council members examined the votes {using|used} the AV method, and they soon realized that there would be a different result.', ex: '구성원들이 "사용하는" 능동 → 현재분사 using' },
        { s: 'For an option {to win|winning} in the first round, it needs to get more than 50% of the first-preference votes.', ex: 'for + 의미상 주어 + to부정사(목적)' },
        { s: 'Option A, the art show, received the fewest first-preference votes, with only 5 council members {voting|voted} for it.', ex: 'with + 명사 + 분사: 구성원이 "투표하는" 능동 → voting' },
        { s: 'It sometimes allows second-preference votes {to have|have} a greater influence than first-preference votes.', ex: 'allow + O + to부정사' }
      ]},
      { type: 'verb', title: '동사변형', guide: '( ) 안의 동사를 알맞은 형태로 바꿔 쓰세요.', items: [
        { s: 'Voters are ___ several options, and whichever gets the most first-preference votes wins.', v: 'give', a: ['given'], ex: '4형식 수동태 be given' },
        { s: 'Neither the second nor third preference ___ at all, so they are ignored.', v: 'matter', a: ['matters'], ex: 'neither A nor B → B에 수일치(단수)' },
        { s: 'This method is commonly ___ in political elections around the world.', v: 'use', a: ['used'], ex: '수동태 be used' },
        { s: 'The student council quickly ___ that the winner would be option C, the charity concert.', v: 'determine', a: ['determined'], ex: '과거형' },
        { s: 'It is possible ___ a vote without the support of the majority.', v: 'win', a: ['to win'], ex: '가주어 It ~ 진주어 to부정사' },
        { s: 'Next, the council members examined the votes ___ the AV method, and they soon realized that there would be a different result.', v: 'use', a: ['using'], ex: '분사구문(능동) using' },
        { s: 'As the charity concert only received 40% of the total votes, a second round of counting was ___.', v: 'require', a: ['required'], ex: '수동태 was required' },
        { s: 'Option A, the art show, received the fewest first-preference votes, with only 5 council members ___ for it.', v: 'vote', a: ['voting'], ex: 'with + 명사 + 현재분사' },
        { s: "Therefore, option A was ___, and the 5 council members' votes were redistributed based on their second preferences.", v: 'eliminate', a: ['eliminated'], ex: '수동태 was eliminated' },
        { s: 'It sometimes allows second-preference votes ___ a greater influence than first-preference votes.', v: 'have', a: ['to have'], ex: 'allow + O + to부정사' }
      ]},
      { type: 'error', title: '오류찾기', guide: '어법상 틀린 곳을 고르세요.', items: [
        { s: 'Voters [[are given]] several options, and whichever [[get]] the most first-preference votes [[wins]]. Neither the second nor third preference [[matters]] at all, so they [[are ignored]].', w: 1, fix: 'gets', ex: 'whichever가 이끄는 절의 주어 whichever는 단수 취급 → gets' },
        { s: 'The FPTP method is [[uncomplicated]] and easy [[to understand]], but it has a significant weakness. It is possible [[win]] a vote [[without]] the support of the majority.', w: 2, fix: 'to win', ex: '가주어 It ~ 진주어 to부정사' },
        { s: 'However, only 8 out of 20 council members [[chose]] the charity concert [[as]] their first preference, [[that]] [[equaled]] 40% of the total votes.', w: 2, fix: 'which', ex: '콤마 뒤 계속적 용법 → which' },
        { s: 'Next, the council members [[examined]] the votes [[used]] the AV method, and they soon [[realized]] that there [[would be]] a different result.', w: 1, fix: 'using', ex: '능동 분사구문 → using' },
        { s: 'For an option [[to win]] in the first round, it [[needs]] to get [[more than]] 50% of the first-preference votes. As the charity concert only received 40% of the total votes, a second round of counting [[required]].', w: 3, fix: 'was required', ex: '집계가 "요구되는" 것 → 수동태' },
        { s: 'Option A, the art show, received the [[fewest]] first-preference votes, with only 5 council members [[voted]] for it. Therefore, option A [[was eliminated]].', w: 1, fix: 'voting', ex: 'with + 명사 + 분사: 능동 → voting' },
        { s: 'It sometimes [[allows]] second-preference votes [[have]] a greater influence [[than]] first-preference votes. In this case, the bake sale [[won]], but this was mainly due to the second-preference votes it received.', w: 1, fix: 'to have', ex: 'allow + O + to부정사' }
      ]},
      { type: 'scramble', title: '본문 스크램블', guide: '우리말에 맞게 단어를 눌러 문장을 완성하세요.', items: [
        { ko: 'FPTP 방식은 세 가지 방식 중 가장 간단하다.', en: 'The FPTP method is the simplest of the three methods.' },
        { ko: '이 방식은 전 세계 정치 선거에서 흔히 사용된다.', en: 'This method is commonly used in political elections around the world.' },
        { ko: '과반수의 지지 없이도 투표에서 승리하는 것이 가능하다.', en: 'It is possible to win a vote without the support of the majority.' },
        { ko: 'AV 방식은 잠재적으로 한 차례 이상의 집계를 포함할 수 있다.', en: 'The AV method can potentially include more than one round of counting.' },
        { ko: '결과적으로, 빵 바자회가 승자가 될 것이었다.', en: 'As a result, the bake sale would be the winner.' },
        { ko: '안타깝게도, AV 방식도 완벽하지는 않다.', en: 'Unfortunately, the AV method is not perfect either.' }
      ]},
      { type: 'order', title: '문장순서', guide: '문장을 본문 순서대로 눌러서 배열하세요.', items: [
        { lines: [
          'The FPTP method is the simplest of the three methods.',
          'Voters are given several options, and whichever gets the most first-preference votes wins.',
          'Neither the second nor third preference matters at all, so they are ignored.',
          'This method is commonly used in political elections around the world.'
        ]},
        { lines: [
          'The FPTP method is uncomplicated and easy to understand, but it has a significant weakness.',
          'It is possible to win a vote without the support of the majority.',
          'That was the case here.',
          "According to the results of the FPTP method, the council's choice was to hold a charity concert.",
          'However, only 8 out of 20 council members chose the charity concert as their first preference, which equaled 40% of the total votes.'
        ]},
        { lines: [
          'Next, the council members examined the votes using the AV method, and they soon realized that there would be a different result.',
          'The AV method can potentially include more than one round of counting.',
          'For an option to win in the first round, it needs to get more than 50% of the first-preference votes.',
          'As the charity concert only received 40% of the total votes, a second round of counting was required.'
        ]},
        { lines: [
          'Option A, the art show, received the fewest first-preference votes, with only 5 council members voting for it.',
          "Therefore, option A was eliminated, and the 5 council members' votes were redistributed based on their second preferences.",
          'As a result, 4 votes for option B (ABC) and 1 for option C (ACB) were added to the total.',
          'This meant that option B had 11 total votes, while option C had only 9.'
        ]}
      ]},
      { type: 'insert', title: '문장삽입', guide: '주어진 문장이 들어가기에 가장 알맞은 곳을 고르세요.', items: [
        { lines: [
          'The student council quickly determined that the winner would be option C, the charity concert.',
          'This was because it received 8 first-preference votes, while option A received 5 and option B received 7.',
          'The FPTP method is uncomplicated and easy to understand, but it has a significant weakness.'
        ], given: 1, ex: 'This was because ~는 C가 이긴 이유를 설명한다.' },
        { lines: [
          'It is possible to win a vote without the support of the majority.',
          'That was the case here.',
          "According to the results of the FPTP method, the council's choice was to hold a charity concert.",
          'However, only 8 out of 20 council members chose the charity concert as their first preference, which equaled 40% of the total votes.'
        ], given: 3, ex: 'However로 "선택은 콘서트였지만 실제 지지는 40%뿐"이라고 대조한다.' },
        { lines: [
          'For an option to win in the first round, it needs to get more than 50% of the first-preference votes.',
          'As the charity concert only received 40% of the total votes, a second round of counting was required.',
          'Option A, the art show, received the fewest first-preference votes, with only 5 council members voting for it.',
          "Therefore, option A was eliminated, and the 5 council members' votes were redistributed based on their second preferences."
        ], given: 3, ex: 'Therefore: 가장 적은 표를 받았으므로 제거되었다.' },
        { lines: [
          'Unfortunately, the AV method is not perfect either.',
          'It sometimes allows second-preference votes to have a greater influence than first-preference votes.',
          'In this case, the bake sale won, but this was mainly due to the second-preference votes it received.'
        ], given: 1, ex: 'AV 방식의 약점(완벽하지 않음)을 구체적으로 설명한다.' }
      ]},
      { type: 'odd', title: '어색한 문장', guide: '글의 흐름과 관계없는 문장을 고르세요.', items: [
        { lines: [
          'The FPTP method is the simplest of the three methods.',
          'Voters are given several options, and whichever gets the most first-preference votes wins.',
          'In this method, the third preference is the most important.',
          'Neither the second nor third preference matters at all, so they are ignored.'
        ], odd: 2, ex: '2·3지망은 전혀 중요하지 않다는 내용과 반대된다.' },
        { lines: [
          'The FPTP method is uncomplicated and easy to understand, but it has a significant weakness.',
          'It is possible to win a vote without the support of the majority.',
          'Every winner in this method has the support of most voters.',
          'That was the case here.'
        ], odd: 2, ex: '과반 지지 없이 이길 수 있다는 약점과 반대된다.' },
        { lines: [
          'Option A, the art show, received the fewest first-preference votes, with only 5 council members voting for it.',
          'Option A was chosen as the final winner right away.',
          "Therefore, option A was eliminated, and the 5 council members' votes were redistributed based on their second preferences.",
          'As a result, 4 votes for option B (ABC) and 1 for option C (ACB) were added to the total.'
        ], odd: 1, ex: 'A는 가장 적은 표를 받아 제거되었다.' }
      ]},
      { type: 'blank', title: '빈칸추론', guide: '빈칸에 들어갈 말로 가장 알맞은 것을 고르세요.', items: [
        { s: 'It is possible to win a vote without the support of ____.', opts: ["the majority", "the council advisor", "first-preference votes", "the plurality"], ex: '40%의 표로 이겼다 → 과반수 지지 없이' },
        { s: 'For an option to win in the first round, it needs to get ____ of the first-preference votes.', opts: ["more than 50%", "exactly 40%", "a plurality", "less than half"], ex: '1차에서 이기려면 과반(50% 이상)이 필요하다.' },
        { s: "Therefore, option A was eliminated, and the 5 council members' votes were redistributed based on ____.", opts: ["their second preferences", "their first preferences", "the total votes", "the FPTP results"], ex: '제거된 A의 표는 2지망에 따라 다시 나뉜다.' },
        { s: 'It sometimes allows second-preference votes to have ____ than first-preference votes.', opts: ["a greater influence", "a smaller influence", "the same weight", "no influence at all"], ex: '빵 바자회는 주로 2지망 표 덕분에 이겼다.' }
      ]},
      { type: 'mc', title: '핵심문법', guide: '알맞은 답을 고르세요.', items: [
        { q: '빈칸에 알맞은 것은?<br><b>The FPTP method is the simplest ______ the three methods.</b>', opts: ['of', 'in', 'than', 'at'], ex: '최상급 + of + 복수명사(~ 중에서)' },
        { q: '빈칸에 알맞은 것은?<br><b>______ gets the most votes wins.</b>', opts: ['Whichever', 'Which', 'Whom', 'That'], ex: '복합관계대명사 whichever: ~하는 어느 것이든' },
        { q: '"2지망도 3지망도 전혀 중요하지 않다."를 바르게 영작한 것은?', opts: ['Neither the second nor third preference matters at all.', 'Either the second nor third preference matters at all.', 'Neither the second or third preference matters at all.', 'Both the second nor third preference matters at all.'], ex: 'neither A nor B: A도 B도 아닌' },
        { q: '빈칸에 알맞은 것은?<br><b>______ is possible to win a vote without the majority.</b>', opts: ['It', 'That', 'This', 'What'], ex: '가주어 It ~ 진주어 to부정사' },
        { q: '빈칸에 알맞은 것은?<br><b>Only 8 members chose it, ______ equaled 40% of the votes.</b>', opts: ['which', 'that', 'what', 'who'], ex: '앞 절 전체를 받는 계속적 용법 → which' },
        { q: '빈칸에 알맞은 것은?<br><b>They examined the votes ______ the AV method.</b>', opts: ['using', 'used', 'to using', 'uses'], ex: '능동 분사구문 → 현재분사' },
        { q: '빈칸에 알맞은 것은?<br><b>______ an option to win, it needs more than 50%.</b>', opts: ['For', 'Of', 'With', 'By'], ex: 'to부정사의 의미상 주어: for + 목적격' },
        { q: '빈칸에 알맞은 것은?<br><b>It received the fewest votes, with only 5 members ______ for it.</b>', opts: ['voting', 'voted', 'to vote', 'votes'], ex: 'with + 명사 + 분사: 능동이면 현재분사' },
        { q: '빈칸에 알맞은 것은?<br><b>It allows second-preference votes ______ a greater influence.</b>', opts: ['to have', 'have', 'having', 'had'], ex: 'allow + O + to부정사' }
      ]}
    ]
  },

  /* ═══════════════════════════ DAY 3 · 본문 ❻❼ ═══════════════════════════ */
  {
    id: 'd3', name: 'DAY 3', range: '3과 본문 ❻❼', story: '콩도르세 방식 · 투표 방식을 이해하는 것의 가치',
    passage: [
      ['', '❻', ''],
      ['', 'The Condorcet Method', '콩도르세 방식'],
      ['', 'Finally, the student council counted the votes using the Condorcet method.', '마지막으로, 학생 자치회는 콩도르세 방식을 사용하여 표를 집계했다.'],
      ['', "This method involves comparing the voters' preferences between each possible pair of options.", '이 방식은 가능한 선택지 쌍에 대한 투표자들의 선호도를 비교하는 것을 수반한다.'],
      ['', 'In this case, there were three pairs to consider: A vs. B, B vs. C, and A vs. C.', '이 경우에는, 고려해야 할 세 쌍이 있었는데, 그것은 바로 A와 B, B와 C, A와 C였다.'],
      ['', 'Through this method, the student council discovered that its members preferred option A to option B by a count of 11 to 9.', '이 방식을 통해, 학생 자치회는 구성원들이 11대 9로 선택지 B보다 선택지 A를 선호한다는 사실을 발견했다.'],
      ['', 'In other words, 11 people preferred A to B, voting either ABC, ACB, or CAB.', '즉, 11명이 ABC, ACB, CAB 중 하나에 투표하며 B보다 A를 선호했다.'],
      ['', 'Meanwhile, 9 people preferred B to A by voting BAC, BCA, or CBA.', '한편, 9명은 BAC, BCA 또는 CBA에 투표함으로써 A보다 B를 선호했다.'],
      ['', 'Interestingly, the voters preferred option B to option C by the same count of 11 to 9.', '흥미롭게도, 투표자들은 동일하게 11대 9로 선택지 C보다 선택지 B를 선호했다.'],
      ['', 'They also preferred option A to option C by 11 to 9.', '그들은 또한 11대 9로 선택지 C보다 선택지 A를 선호했다.'],
      ['', 'As option A, the art show, was preferred to both of the other options, it would be considered the winner.', '미술 전시회인 선택지 A가 나머지 두 선택지보다 더 선호되었으므로, 이 선택지가 승자로 간주될 것이었다.'],
      ['', "The Condorcet method's weakness is that, along with being complex, it sometimes fails to select a winner.", '콩도르세 방식의 약점은 복잡하다는 것에 더해, 때때로 승자를 선정하지 못한다는 것이다.'],
      ['', 'This is especially true in elections that contain numerous options.', '이는 특히 수많은 선택지가 있는 선거에서 그렇다.'],
      ['', 'It is possible that no option will be clearly preferred over the others.', '어떤 선택지도 다른 것들보다 명확하게 선호되지 않을 수도 있다.'],
      ['', '❼', ''],
      ['', "Instead of all methods pointing toward a single option and making the council's choice easier, the winner differed with each method.", '모든 방식이 하나의 선택지를 가리키고 자치회의 선택을 더 쉽게 만드는 대신, 각 방식마다 승자는 달랐다.'],
      ['', 'After a long, intense discussion with Ms. Akers, the student council members decided to choose the Condorcet method, as they liked the idea of directly comparing each option with the others.', 'Akers 선생님과의 오랜 열띤 논의 끝에, 학생 자치회 구성원들은 콩도르세 방식을 선택하기로 결정했는데, 각 선택지를 다른 선택지들과 직접 비교한다는 점이 마음에 들었기 때문이다.'],
      ['', 'Everyone agreed that they learned a lot about different voting systems through this experience.', '모두가 이번 경험을 통해 각기 다른 투표 시스템에 대해 많은 것을 배웠다는 것에 동의했다.'],
      ['', 'It is obvious that choosing an ideal voting method is a complex and challenging task.', '이상적인 투표 방법을 선택하는 것은 복잡하고 도전적인 일이라는 것은 분명하다.'],
      ['', 'No voting system is flawless or clearly superior to another.', '어떤 투표 시스템도 완벽하거나 다른 시스템보다 명백히 우수하지는 않다.'],
      ['', 'Whichever we choose will have pros and cons.', '우리가 선택하는 어느 것이든 장단점이 있을 것이다.'],
      ['', 'Some people believe that it is best to keep the process simple by not ranking our choices at all.', '어떤 사람들은 우리의 선택들에 아예 순위를 매기지 않음으로써 과정을 단순하게 유지하는 것이 최선이라고 생각한다.'],
      ['', 'Others continue to develop and test new ways of voting, arguing that more complex methods deliver more accurate results.', '다른 사람들은 더 복잡한 방식이 더 정확한 결과를 가져온다고 주장하며 계속해서 새로운 투표 방법을 개발하고 시험한다.'],
      ['', 'All of these efforts are designed not to make decision-making difficult and inefficient, but to help us make better decisions as a society.', '이러한 모든 노력은 의사 결정을 어렵고 비효율적으로 만들기 위한 것이 아니라, 우리가 사회로서 더 나은 결정을 내릴 수 있게 돕기 위해 고안된 것이다.'],
      ['', 'Ultimately, understanding all of the possible voting methods and weighing their pros and cons allows us to better understand the process of decision-making.', '결국, 모든 가능한 투표 방법을 이해하고 장단점을 따져 보는 것은 우리가 의사 결정 과정을 더 잘 이해할 수 있게 한다.'],
      ['', 'When we understand decision-making better, we are more likely to become better decision-makers ourselves.', '우리가 의사 결정을 더 잘 이해할 때, 우리 스스로 더 나은 의사 결정자가 될 가능성이 더 높다.']
    ],
    steps: [
      { type: 'vocab', title: '핵심어휘·숙어', quizN: 15, items: [
        ['involve -ing', '~하는 것을 수반하다'], ['compare', '비교하다'], ['pair', '쌍'], ['consider', '고려하다; 여기다'],
        ['discover', '발견하다'], ['prefer A to B', 'B보다 A를 선호하다'], ['in other words', '즉, 다시 말해'], ['meanwhile', '한편'],
        ['interestingly', '흥미롭게도'], ['along with', '~에 덧붙여, ~와 함께'], ['complex', '복잡한'], ['fail to', '~하지 못하다'],
        ['select', '선정하다, 선택하다'], ['contain', '포함하다'], ['instead of', '~ 대신에'], ['point toward', '~을 가리키다'],
        ['differ', '다르다'], ['intense', '열띤, 강렬한'], ['directly', '직접'], ['obvious', '분명한, 명백한'],
        ['ideal', '이상적인'], ['challenging', '도전적인, 힘든'], ['flawless', '흠 없는, 완벽한'], ['superior to', '~보다 우수한'],
        ['pros and cons', '장단점'], ['rank', '순위를 매기다'], ['argue', '주장하다'], ['accurate', '정확한'],
        ['be designed to', '~하도록 고안되다'], ['ultimately', '결국, 궁극적으로'], ['weigh', '따져 보다, 저울질하다'], ['be likely to', '~할 가능성이 있다']
      ]},
      { type: 'pick', title: '어휘선택', guide: '문맥에 맞는 낱말을 고르세요.', items: [
        { s: "This method involves {comparing|compiling} the voters' preferences between each possible pair of options.", ex: "compare 비교하다 vs compile 편찬하다, 모으다" },
        { s: "The Condorcet method's weakness is that, along with being {complex|complacent}, it sometimes fails to select a winner.", ex: "complex 복잡한 vs complacent 자기만족적인 (철자 혼동)" },
        { s: 'This is especially true in elections that contain {numerous|numerical} options.', ex: "numerous 수많은 vs numerical 수의, 숫자로 나타낸" },
        { s: "Instead of all methods pointing toward a single option and making the council's choice easier, the winner {differed|deferred} with each method.", ex: "differ 다르다 vs defer 미루다 (철자 혼동)" },
        { s: 'After a long, intense discussion with Ms. Akers, the student council members decided to choose the Condorcet method, as they liked the idea of {directly|indirectly} comparing each option with the others.', ex: "각 선택지를 직접(directly) 비교하는 콩도르세 방식" },
        { s: 'It is {obvious|oblivious} that choosing an ideal voting method is a complex and challenging task.', ex: "obvious 분명한 vs oblivious 의식하지 못하는 (철자 혼동)" },
        { s: 'No voting system is {flawless|flawed} or clearly superior to another.', ex: '어떤 방식도 완벽하지(flawless) 않다.' },
        { s: 'Whichever we choose will have {pros and cons|ins and outs}.', ex: "pros and cons 장단점 vs ins and outs 자세한 내막" },
        { s: 'Others continue to develop and test new ways of voting, arguing that more complex methods deliver more {accurate|accumulated} results.', ex: "accurate 정확한 vs accumulated 축적된 (철자 혼동)" },
        { s: 'When we understand decision-making better, we are more {likely|unlikely} to become better decision-makers ourselves.', ex: 'be likely to: ~할 가능성이 있다' }
      ]},
      { type: 'tf', title: 'T/F 내용 확인', guide: '본문 내용과 일치하면 T, 다르면 F를 고르세요.', items: [
        ["The Condorcet method weighs the options against each other in pairs.", true, "weigh A against B : A와 B를 비교하다"],
        ["Four pairings had to be considered in this case.", false, "pairing 짝 → A-B, B-C, A-C 세 쌍"],
        ["Voters favored option B over option A by 11 to 9.", false, "favor A over B = prefer A to B → 실제로는 A를 11대 9로 선호"],
        ["Option A outranked both of the remaining options.", true, "outrank ~보다 우위에 있다 · remaining = other"],
        ["The Condorcet method unfailingly identifies a definitive winner.", false, "unfailingly 반드시 · definitive 확정적인 → sometimes fails to select a winner"],
        ["All three methods converged on an identical winner.", false, "converge on ~로 모이다 · identical = same → 방식마다 승자가 달랐음"],
        ["The council ultimately settled on the Condorcet method.", true, "ultimately = finally · settle on ~으로 결정하다"],
        ["The writer contends that no voting system is without drawbacks.", true, "contend = claim · drawback 결점 → No voting system is flawless"]
      ]},
      { type: 'mc', title: '일치·불일치', guide: "선택지는 본문을 어려운 어휘로 바꿔 쓴 문장이에요. 풀고 나서 해설의 어휘를 꼭 확인하세요.", items: [
        { n: "❻", box: ["❻"], q: "글의 내용과 일치하지 <u>않는</u> 것은?", opts: ["The Condorcet method invariably produces a clear winner.", "The Condorcet method compares voters' preferences between every pair of options.", "Voters favored the art show over the bake sale by 11 to 9.", "The bake sale was preferred to the charity concert by the same margin.", "Besides being intricate, the method may struggle when there are many options."], ex: "정답: invariably : 언제나, 예외 없이 → 실제로는 sometimes fails to select a winner\n· favor A over B = prefer A to B · margin : (득표) 차이 (= count)\n· besides = along with · intricate = complex · numerous = many", per: [["콩도르세 방식은 언제나 확실한 승자를 낸다.", "it sometimes fails to select a winner", "불일치 → 때때로 승자를 뽑지 못함"], ["콩도르세 방식은 모든 선택지 쌍에 대한 선호를 비교한다.", "comparing the voters' preferences between each possible pair of options", "일치"], ["투표자들은 11대 9로 빵 바자회보다 미술 전시회를 선호했다.", "preferred option A to option B by a count of 11 to 9", "일치"], ["빵 바자회는 같은 차이로 자선 콘서트보다 선호되었다.", "preferred option B to option C by the same count of 11 to 9", "일치"], ["복잡할 뿐 아니라, 선택지가 많으면 어려움을 겪을 수 있다.", ["along with being complex", "especially true in elections that contain numerous options"], "일치"]] },
        { n: "❼", box: ["❼"], q: "글의 내용과 <u>일치하는</u> 것은?", opts: ["The council opted for the Condorcet method because it pits each option directly against the others.", "All three methods converged on the same winner.", "The writer claims one voting system is clearly superior to the others.", "Everyone agrees that ranking choices always makes voting more accurate.", "These efforts aim to make decision-making more cumbersome."], ex: "정답: opt for : ~을 선택하다 (= choose) · pit A against B : A와 B를 맞붙이다 (≒ compare)\n· converge on : ~로 모이다 (↔ differ)\n· superior to : ~보다 우수한 · flawless : 결점 없는\n· rank : 순위를 매기다\n· cumbersome : 번거로운 (= difficult and inefficient)", per: [["자치회는 각 선택지를 다른 것과 직접 맞붙이기 때문에 콩도르세 방식을 택했다.", "they liked the idea of directly comparing each option with the others", "일치"], ["세 방식 모두 같은 승자로 모였다.", "the winner differed with each method", "불일치 → 방식마다 승자가 달랐음"], ["필자는 한 투표 방식이 다른 것보다 확실히 우수하다고 주장한다.", "No voting system is flawless or clearly superior to another", "불일치"], ["순위를 매기면 항상 더 정확해진다는 데 모두가 동의한다.", "it is best to keep the process simple by not ranking our choices at all", "불일치 → 순위를 아예 안 매기자는 사람도 있음"], ["이런 노력은 의사 결정을 더 번거롭게 만드는 것이 목적이다.", "not to make decision-making difficult and inefficient", "불일치 → 더 나은 결정을 돕기 위함"]] }
      ]},
      { type: 'pick', title: '어법선택', guide: '어법상 알맞은 것을 고르세요.', items: [
        { s: "This method involves {comparing|to compare} the voters' preferences between each possible pair of options.", ex: 'involve + 동명사' },
        { s: 'In this case, there were three pairs {to consider|considering}: A vs. B, B vs. C, and A vs. C.', ex: '명사를 꾸미는 to부정사 (고려해야 할)' },
        { s: 'Through this method, the student council discovered that its members preferred option A {to|than} option B by a count of 11 to 9.', ex: 'prefer A to B' },
        { s: 'Meanwhile, 9 people preferred B to A by {voting|vote} BAC, BCA, or CBA.', ex: '전치사 by + 동명사' },
        { s: 'As option A, the art show, {was preferred|preferred} to both of the other options, it would be considered the winner.', ex: 'A가 "선호되는" 것 → 수동태' },
        { s: 'As option A, the art show, was preferred to both of the {other|another} options, it would be considered the winner.', ex: 'the other + 복수명사: 나머지 모두' },
        { s: "The Condorcet method's weakness is that, along with being complex, it sometimes fails {to select|selecting} a winner.", ex: 'fail + to부정사' },
        { s: 'This is especially true in elections {that|what} contain numerous options.', ex: '선행사(elections) + 주격 관계대명사 that' },
        { s: "Instead of all methods {pointing|pointed} toward a single option and making the council's choice easier, the winner differed with each method.", ex: '전치사 of + 동명사 (all methods는 의미상 주어)' },
        { s: 'It is obvious that choosing an ideal voting method {is|are} a complex and challenging task.', ex: '동명사 주어 → 단수동사 is' },
        { s: 'Ultimately, understanding all of the possible voting methods and weighing their pros and cons allows us {to better understand|better understand} the process of decision-making.', ex: 'allow + O + to부정사' }
      ]},
      { type: 'verb', title: '동사변형', guide: '( ) 안의 동사를 알맞은 형태로 바꿔 쓰세요.', items: [
        { s: 'Finally, the student council counted the votes ___ the Condorcet method.', v: 'use', a: ['using'], ex: '능동 분사구문 using' },
        { s: "This method involves ___ the voters' preferences between each possible pair of options.", v: 'compare', a: ['comparing'], ex: 'involve + 동명사' },
        { s: 'In other words, 11 people preferred A to B, ___ either ABC, ACB, or CAB.', v: 'vote', a: ['voting'], ex: '분사구문(동시 동작) voting' },
        { s: 'As option A, the art show, was ___ to both of the other options, it would be considered the winner.', v: 'prefer', a: ['preferred'], ex: '수동태 was preferred' },
        { s: 'As option A, the art show, was preferred to both of the other options, it would be ___ the winner.', v: 'consider', a: ['considered'], ex: 'consider A B의 수동태: be considered B' },
        { s: "The Condorcet method's weakness is that, along with ___ complex, it sometimes fails to select a winner.", v: 'be', a: ['being'], ex: '전치사 with + 동명사' },
        { s: 'After a long, intense discussion with Ms. Akers, the student council members decided ___ the Condorcet method, as they liked the idea of directly comparing each option with the others.', v: 'choose', a: ['to choose'], ex: 'decide + to부정사' },
        { s: 'It is obvious that ___ an ideal voting method is a complex and challenging task.', v: 'choose', a: ['choosing', 'to choose'], ex: '주어 자리 → 동명사 (본문: choosing)' },
        { s: 'Others continue to develop and test new ways of voting, ___ that more complex methods deliver more accurate results.', v: 'argue', a: ['arguing'], ex: '능동 분사구문 arguing' },
        { s: 'All of these efforts are ___ not to make decision-making difficult and inefficient, but to help us make better decisions as a society.', v: 'design', a: ['designed'], ex: 'be designed to: ~하도록 고안되다' }
      ]},
      { type: 'error', title: '오류찾기', guide: '어법상 틀린 곳을 고르세요.', items: [
        { s: "This method involves [[to compare]] the voters' preferences between each possible [[pair]] of options. In this case, there [[were]] three pairs [[to consider]]: A vs. B, B vs. C, and A vs. C.", w: 0, fix: 'comparing', ex: 'involve + 동명사' },
        { s: 'Through this method, the student council discovered [[that]] its members preferred option A [[than]] option B by a count of 11 to 9. In other words, 11 people [[preferred]] A to B, [[voting]] either ABC, ACB, or CAB.', w: 1, fix: 'to', ex: 'prefer A to B (than X)' },
        { s: 'As option A, the art show, [[preferred]] to both of the [[other]] options, it [[would be]] [[considered]] the winner.', w: 0, fix: 'was preferred', ex: 'A가 "선호되는" 것 → 수동태' },
        { s: "The Condorcet method's weakness is [[that]], along with [[being]] complex, it sometimes fails [[selecting]] a winner. This is especially true in elections [[that]] contain numerous options.", w: 2, fix: 'to select', ex: 'fail + to부정사' },
        { s: "Instead of all methods [[pointed]] toward a single option and [[making]] the council's choice [[easier]], the winner [[differed]] with each method.", w: 0, fix: 'pointing', ex: '전치사 of 뒤 → 동명사 (and making과 병렬)' },
        { s: 'It is obvious that choosing an ideal voting method [[are]] a complex and [[challenging]] task. No voting system is flawless or clearly [[superior]] [[to]] another.', w: 0, fix: 'is', ex: '동명사 주어 → 단수동사' },
        { s: 'Others continue [[to develop]] and test new ways of voting, [[argued]] that more complex methods [[deliver]] more [[accurate]] results.', w: 1, fix: 'arguing', ex: '"주장하며"(능동) → 현재분사 arguing' }
      ]},
      { type: 'scramble', title: '본문 스크램블', guide: '우리말에 맞게 단어를 눌러 문장을 완성하세요.', items: [
        { ko: '마지막으로, 학생 자치회는 콩도르세 방식을 사용하여 표를 집계했다.', en: 'Finally, the student council counted the votes using the Condorcet method.' },
        { ko: '이는 특히 수많은 선택지가 있는 선거에서 그렇다.', en: 'This is especially true in elections that contain numerous options.' },
        { ko: '어떤 투표 시스템도 완벽하거나 다른 시스템보다 명백히 우수하지는 않다.', en: 'No voting system is flawless or clearly superior to another.' },
        { ko: '우리가 선택하는 어느 것이든 장단점이 있을 것이다.', en: 'Whichever we choose will have pros and cons.' },
        { ko: '모두가 이번 경험을 통해 각기 다른 투표 시스템에 대해 많은 것을 배웠다는 것에 동의했다.', en: 'Everyone agreed that they learned a lot about different voting systems through this experience.' },
        { ko: '우리가 의사 결정을 더 잘 이해할 때, 우리 스스로 더 나은 의사 결정자가 될 가능성이 더 높다.', en: 'When we understand decision-making better, we are more likely to become better decision-makers ourselves.' }
      ]},
      { type: 'order', title: '문장순서', guide: '문장을 본문 순서대로 눌러서 배열하세요.', items: [
        { lines: [
          'Finally, the student council counted the votes using the Condorcet method.',
          "This method involves comparing the voters' preferences between each possible pair of options.",
          'In this case, there were three pairs to consider: A vs. B, B vs. C, and A vs. C.',
          'Through this method, the student council discovered that its members preferred option A to option B by a count of 11 to 9.'
        ]},
        { lines: [
          'In other words, 11 people preferred A to B, voting either ABC, ACB, or CAB.',
          'Meanwhile, 9 people preferred B to A by voting BAC, BCA, or CBA.',
          'Interestingly, the voters preferred option B to option C by the same count of 11 to 9.',
          'They also preferred option A to option C by 11 to 9.',
          'As option A, the art show, was preferred to both of the other options, it would be considered the winner.'
        ]},
        { lines: [
          "Instead of all methods pointing toward a single option and making the council's choice easier, the winner differed with each method.",
          'After a long, intense discussion with Ms. Akers, the student council members decided to choose the Condorcet method, as they liked the idea of directly comparing each option with the others.',
          'Everyone agreed that they learned a lot about different voting systems through this experience.'
        ]},
        { lines: [
          'It is obvious that choosing an ideal voting method is a complex and challenging task.',
          'No voting system is flawless or clearly superior to another.',
          'Whichever we choose will have pros and cons.',
          'Some people believe that it is best to keep the process simple by not ranking our choices at all.',
          'Others continue to develop and test new ways of voting, arguing that more complex methods deliver more accurate results.'
        ]}
      ]},
      { type: 'insert', title: '문장삽입', guide: '주어진 문장이 들어가기에 가장 알맞은 곳을 고르세요.', items: [
        { lines: [
          'Through this method, the student council discovered that its members preferred option A to option B by a count of 11 to 9.',
          'In other words, 11 people preferred A to B, voting either ABC, ACB, or CAB.',
          'Meanwhile, 9 people preferred B to A by voting BAC, BCA, or CBA.'
        ], given: 2, ex: 'Meanwhile(한편)로 A를 선호한 11명과 B를 선호한 9명을 대조한다.' },
        { lines: [
          "The Condorcet method's weakness is that, along with being complex, it sometimes fails to select a winner.",
          'This is especially true in elections that contain numerous options.',
          'It is possible that no option will be clearly preferred over the others.'
        ], given: 1, ex: 'This는 "승자를 정하지 못하는 경우"를 가리킨다.' },
        { lines: [
          'It is obvious that choosing an ideal voting method is a complex and challenging task.',
          'No voting system is flawless or clearly superior to another.',
          'Whichever we choose will have pros and cons.',
          'Some people believe that it is best to keep the process simple by not ranking our choices at all.',
          'Others continue to develop and test new ways of voting, arguing that more complex methods deliver more accurate results.'
        ], given: 4, ex: 'Some people ~ / Others ~: 어떤 사람들은 ~, 다른 사람들은 ~' },
        { lines: [
          'All of these efforts are designed not to make decision-making difficult and inefficient, but to help us make better decisions as a society.',
          'Ultimately, understanding all of the possible voting methods and weighing their pros and cons allows us to better understand the process of decision-making.',
          'When we understand decision-making better, we are more likely to become better decision-makers ourselves.'
        ], given: 2, ex: '의사 결정 과정을 이해하면 → 더 나은 결정자가 된다.' }
      ]},
      { type: 'odd', title: '어색한 문장', guide: '글의 흐름과 관계없는 문장을 고르세요.', items: [
        { lines: [
          'Through this method, the student council discovered that its members preferred option A to option B by a count of 11 to 9.',
          'In other words, 11 people preferred A to B, voting either ABC, ACB, or CAB.',
          'Most voters did not care about option A at all.',
          'Meanwhile, 9 people preferred B to A by voting BAC, BCA, or CBA.'
        ], odd: 2, ex: 'A가 가장 선호되었다는 내용과 반대된다.' },
        { lines: [
          "The Condorcet method's weakness is that, along with being complex, it sometimes fails to select a winner.",
          'It always selects a clear winner quickly and easily.',
          'This is especially true in elections that contain numerous options.',
          'It is possible that no option will be clearly preferred over the others.'
        ], odd: 1, ex: '승자를 정하지 못할 때가 있다는 약점과 반대된다.' },
        { lines: [
          'It is obvious that choosing an ideal voting method is a complex and challenging task.',
          'No voting system is flawless or clearly superior to another.',
          'The FPTP method is the only perfect way to vote.',
          'Whichever we choose will have pros and cons.'
        ], odd: 2, ex: '완벽한 투표 방식은 없다는 흐름과 반대된다.' }
      ]},
      { type: 'blank', title: '빈칸추론', guide: '빈칸에 들어갈 말로 가장 알맞은 것을 고르세요.', items: [
        { s: 'This method involves ____ between each possible pair of options.', opts: ["comparing the voters' preferences", "counting only first preferences", "redistributing the eliminated votes", "ranking the options by popularity"], ex: '콩도르세 방식은 선택지를 쌍으로 비교한다.' },
        { s: "The Condorcet method's weakness is that, along with being complex, it sometimes ____.", opts: ["fails to select a winner", "selects too many winners", "ignores second preferences", "requires a second round"], ex: '어떤 선택지도 명확히 선호되지 않을 수 있다.' },
        { s: 'No voting system is ____ or clearly superior to another.', opts: ["flawless", "complex", "flawed", "familiar"], ex: '모든 방식에 장단점이 있다.' },
        { s: 'All of these efforts are designed not to make decision-making difficult and inefficient, but to help us ____ as a society.', opts: ["make better decisions", "make faster decisions", "avoid complex decisions", "rank our choices"], ex: 'not A but B: 어렵게 하려는 게 아니라 더 나은 결정을 돕기 위해' }
      ]},
      { type: 'mc', title: '핵심문법', guide: '알맞은 답을 고르세요.', items: [
        { q: '빈칸에 알맞은 것은?<br><b>This method involves ______ the voters\' preferences.</b>', opts: ['comparing', 'to compare', 'compare', 'compared'], ex: 'involve + 동명사' },
        { q: '"11명이 B보다 A를 선호했다."를 바르게 영작한 것은?', opts: ['11 people preferred A to B.', '11 people preferred A than B.', '11 people preferred B to A.', '11 people preferred A over to B.'], ex: 'prefer A to B: B보다 A를 선호하다' },
        { q: '빈칸에 알맞은 것은?<br><b>9 people preferred B to A ______ BAC.</b>', opts: ['by voting', 'by vote', 'with voted', 'for voting'], ex: 'by + 동명사: ~함으로써' },
        { q: '빈칸에 알맞은 것은?<br><b>Option A would ______ the winner.</b>', opts: ['be considered', 'consider', 'considering', 'be considering'], ex: 'consider A B의 수동태: A is considered B' },
        { q: '빈칸에 알맞은 것은?<br><b>It sometimes fails ______ a winner.</b>', opts: ['to select', 'selecting', 'select', 'selected'], ex: 'fail + to부정사' },
        { q: '빈칸에 알맞은 것은?<br><b>______ is obvious that choosing an ideal method is a challenging task.</b>', opts: ['It', 'That', 'What', 'This'], ex: '가주어 It ~ 진주어 that절' },
        { q: '빈칸에 알맞은 것은?<br><b>These efforts are designed ______ to make decisions difficult, but to help us.</b>', opts: ['not', 'neither', 'either', 'no'], ex: 'not A but B: A가 아니라 B' },
        { q: '빈칸에 알맞은 것은?<br><b>They help us ______ better decisions.</b>', opts: ['make', 'making', 'made', 'to making'], ex: 'help + O + 동사원형(to부정사)' },
        { q: '빈칸에 알맞은 것은?<br><b>______ we choose will have pros and cons.</b>', opts: ['Whichever', 'Which', 'What if', 'Whether'], ex: '복합관계대명사 whichever: ~하는 어느 것이든 (주어 역할)' }
      ]}
    ]
  }
  ]
};
