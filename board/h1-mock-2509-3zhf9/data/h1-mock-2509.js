/* 고1 2025학년도 9월 전국연합학력평가(인천광역시교육청 주관) 영어 18~24번
   작성 규칙은 README.md 의 "데이터 작성 규칙". 모의고사용으로 추가된 것:
   - 지문은 아래 T18~T24 에 [영어, 해석] 한 줄 = 한 문장으로 적고, passage 에서 sec('18번 · …') 로 문항 제목을 넣음
   - '실전 문항' 단계(type: 'mc')는 exam() 으로 원문항 발문 + 지문을 그대로 보여 줌. opts 첫 번째가 정답
*/
(function () {
  function esc(s) { return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;'); }
  function sec(t) { return [['#', t, '']]; }
  function rows(T) { return T.map(function (r) { return ['', r[0], r[1]]; }); }
  /* exam(번호, 발문, 지문, 밑줄 칠 표현) → 실전 문항 화면 */
  function exam(no, stem, T, u) {
    var body = T.map(function (r) { var t = esc(r[0]); if (u && t.indexOf(esc(u)) >= 0) t = t.replace(esc(u), '<u>' + esc(u) + '</u>'); return t; }).join(' ');
    return '<b>' + no + '. ' + stem + '</b><span class="exam-box en">' + body + '</span>';
  }

  var T18 = [
    ["Dear Principal Jones,", "Jones 교장 선생님께,"],
    ["I hope this message finds you well.", "이 편지를 받으실 때 잘 지내고 계시기를 바랍니다. (직역: 이 메시지가 선생님께 잘 지내시는 상태로 닿기를 바랍니다.)"],
    ["As student council president, I am reaching out to discuss an important matter regarding our school library's current operating hours.", "학생회장으로서, 저는 우리 학교 도서관의 현재 운영 시간에 관한 중요한 문제를 논의하기 위해 연락을 드립니다."],
    ["At present, the library closes at 5 p.m., which many students feel limits their ability to fully use its resources for study and research after regular class hours.", "현재 도서관은 오후 5시에 문을 닫는데, 많은 학생들은 이것이 정규 수업 시간 이후에 학습과 연구를 위해 도서관 자료를 충분히 이용할 수 있는 능력을 제한한다고 느낍니다."],
    ["This is particularly challenging for those preparing for college entrance exams or working on academic projects that demand a quiet and resourceful environment.", "이는 대학 입시를 준비하거나 조용하고 자료가 풍부한 환경을 필요로 하는 학업 프로젝트를 하고 있는 학생들에게 특히 힘든 일입니다."],
    ["Therefore, I'd like to ask you to extend the library's operating hours to 7 p.m.", "그래서 도서관 운영 시간을 오후 7시까지 연장해 주실 것을 요청드리고 싶습니다."],
    ["This change would greatly benefit students by providing additional time to focus on their academic goals.", "이 변화는 학업 목표에 집중할 추가 시간을 제공함으로써 학생들에게 큰 도움이 될 것입니다."],
    ["I hope you will consider this proposal as a step toward improving our academic environment and better supporting our needs.", "이 제안을 우리의 학업 환경을 개선하고 우리의 요구를 더 잘 지원하기 위한 한 걸음으로 고려해 주시기를 바랍니다."],
    ["Sincerely,", "진심을 담아,"],
    ["Eric Park", "Eric Park"],
    ["Student Council President", "학생회장"]
  ];
  var T19 = [
    ["I glanced at the clock on the wall.", "나는 벽에 걸린 시계를 힐끗 보았다."],
    ["10:00.", "10시."],
    ["That meant the casting director would call very soon with the results of my first audition for a musical part in The Wizard of Oz.", "그것은 캐스팅 감독이 '오즈의 마법사' 뮤지컬 배역을 위한 나의 첫 오디션 결과를 가지고 곧 전화할 것이라는 뜻이었다."],
    ["I felt shaky all over, chewing my thumbnail and jiggling my feet.", "나는 엄지손톱을 물어뜯고 발을 달달 떨면서 온몸이 떨렸다."],
    ["Finally, the telephone rang.", "마침내 전화가 울렸다."],
    ["While I was coming round, Dad answered.", "내가 (전화 쪽으로) 오고 있는 동안 아빠가 전화를 받았다."],
    ["I heard him say, \"Ahh, thank you. I'll let her know ...\"", "나는 아빠가 \"아, 감사합니다. 그 애에게 알려 줄게요...\"라고 말하는 것을 들었다."],
    ["As I got to the bottom of the stairs, he was just putting the phone down.", "내가 계단 아래에 다다랐을 때, 아빠는 막 전화를 내려놓고 있었다."],
    ["\"That was The Wizard of Oz. You're second senior munchkin,\" he announced.", "\"'오즈의 마법사'에서 온 전화였어. 너는 두 번째 선배 먼치킨 역이야.\"라고 아빠가 알려 주었다."],
    ["I got a little rush of excitement, knowing I was in — that whatever happened I could be involved in one of the productions.", "내가 합격했다는 것, 즉 무슨 일이 있어도 공연 중 하나에 참여할 수 있다는 것을 알고 나는 살짝 흥분이 밀려왔다."]
  ];
  var T20 = [
    ["Inefficient teachers overlook the potential power of the opening minutes of class.", "비효율적인 교사들은 수업 시작 몇 분의 잠재적인 힘을 간과한다."],
    ["Often, if students are quiet enough and if there are many pressing demands on a teacher's time at that moment, more than ten minutes can disappear before class starts.", "흔히 학생들이 충분히 조용하고 그 순간 교사의 시간에 급한 요구가 많으면, 수업이 시작되기 전에 10분 넘게 사라질 수 있다."],
    ["It's no wonder that students are late for class; they have little reason to be on time.", "학생들이 수업에 늦는 것은 놀랄 일이 아니다. 그들은 제시간에 올 이유가 거의 없다."],
    ["You can use the first ten minutes to get your class off to a great start, or you can choose to waste this time.", "여러분은 처음 10분을 수업을 훌륭하게 시작하는 데 쓸 수도 있고, 이 시간을 낭비하는 쪽을 선택할 수도 있다."],
    ["The first minutes set the tone for the rest of the class.", "처음 몇 분이 수업의 나머지 시간의 분위기를 정한다."],
    ["If you are prepared for class and have taught your students an opening routine, they can use this brief time to make mental and emotional transitions from the last class or subject and prepare to focus on learning new material.", "여러분이 수업 준비가 되어 있고 학생들에게 시작 루틴을 가르쳐 두었다면, 학생들은 이 짧은 시간을 이용해 지난 수업이나 과목에서 정신적·정서적으로 전환하고 새로운 내용을 배우는 데 집중할 준비를 할 수 있다."],
    ["In summary, you should establish an opening routine to develop your class with an effective start.", "요약하자면, 효과적인 시작으로 수업을 전개하기 위해 시작 루틴을 확립해야 한다."]
  ];
  var T21 = [
    ["Many atoms in your body are nearly as old as the universe itself.", "여러분 몸속의 많은 원자는 거의 우주 그 자체만큼 오래되었다."],
    ["When you breathe, for example, only some of the atoms that you inhale are exhaled in your next breath.", "예를 들어, 숨을 쉴 때 여러분이 들이마신 원자 중 일부만 다음 숨에 내쉬어진다."],
    ["The remaining atoms are taken into your body to become part of you, and they later leave your body by various means.", "나머지 원자들은 몸속으로 들어가 여러분의 일부가 되고, 나중에 다양한 방법으로 몸을 떠난다."],
    ["You don't \"own\" the atoms that make up your body; you borrow them.", "여러분은 몸을 구성하는 원자를 '소유'하는 것이 아니라 빌린다."],
    ["We all share from the same atom pool because atoms forever travel around, within, and among us.", "원자는 영원히 우리 주변과 내부, 그리고 우리 사이를 돌아다니기 때문에 우리는 모두 같은 원자 저장소를 함께 쓴다."],
    ["Atoms cycle from person to person as we breathe and as our sweat is evaporated.", "우리가 숨을 쉬고 땀이 증발할 때 원자는 사람에서 사람으로 순환한다."],
    ["We recycle atoms on a grand scale.", "우리는 대규모로 원자를 재활용한다."],
    ["The origin of the lightest atoms goes back to the origin of the universe, and most heavier atoms are older than the Sun and Earth.", "가장 가벼운 원자들의 기원은 우주의 기원으로 거슬러 올라가고, 대부분의 더 무거운 원자들은 태양과 지구보다 오래되었다."],
    ["There are atoms in your body that have existed since the first moments of time, recycling throughout the universe among limitless forms, both nonliving and living.", "여러분의 몸속에는 시간의 첫 순간부터 존재해 온 원자들이 있는데, 그것들은 무생물과 생물을 모두 아우르는 무한한 형태 사이에서 우주 전체에 걸쳐 재활용되어 왔다."],
    ["You're the present caretaker of the atoms in your body.", "여러분은 몸속 원자들의 현재 관리인이다."],
    ["There will be many who will follow you.", "여러분의 뒤를 이을 많은 이들이 있을 것이다."]
  ];
  var T22 = [
    ["The act of gardening itself is a fantastic form of physical activity.", "정원 가꾸기라는 행위 자체가 훌륭한 형태의 신체 활동이다."],
    ["It involves a range of motions, from digging and planting to watering and harvesting.", "그것은 땅 파기와 심기부터 물 주기와 수확하기까지 다양한 동작을 포함한다."],
    ["These activities help improve strength, flexibility, and endurance.", "이러한 활동은 근력, 유연성, 지구력을 향상하는 데 도움이 된다."],
    ["You might not realize it, but small tasks like weeding or turning compost can burn many calories.", "깨닫지 못할 수도 있지만, 잡초 뽑기나 퇴비 뒤집기 같은 작은 일도 많은 칼로리를 소모할 수 있다."],
    ["Gardening is particularly beneficial for those who find traditional exercise challenging.", "정원 가꾸기는 전통적인 운동을 힘들어하는 사람들에게 특히 이롭다."],
    ["It's a low-impact way to stay active and fit, making it accessible for people of all ages and physical abilities.", "그것은 활동적이고 건강한 상태를 유지하는 몸에 무리가 적은 방법이어서, 모든 연령과 신체 능력의 사람들이 쉽게 할 수 있다."],
    ["Besides physical health, gardening has profound mental health benefits.", "신체 건강 외에도, 정원 가꾸기는 정신 건강에 깊은 이점이 있다."],
    ["Tending to plants can be incredibly calming and meditative.", "식물을 돌보는 것은 놀라울 정도로 마음을 진정시키고 명상적일 수 있다."],
    ["It allows you to focus on the present moment, reducing stress and anxiety.", "그것은 현재 순간에 집중할 수 있게 해 주어 스트레스와 불안을 줄여 준다."],
    ["The repetitive tasks involved in gardening can induce a state of mindfulness, similar to meditation.", "정원 가꾸기에 수반되는 반복적인 작업은 명상과 비슷한 마음 챙김 상태를 이끌어 낼 수 있다."],
    ["Studies have shown that spending time in nature, even in a small garden, can elevate mood, improve cognition, and reduce depression symptoms.", "연구들은 자연에서, 심지어 작은 정원에서라도 시간을 보내는 것이 기분을 좋게 하고, 인지 능력을 향상하며, 우울 증상을 줄일 수 있다는 것을 보여 주었다."],
    ["The sense of accomplishment from watching your plants grow and thrive can also boost self-esteem and overall well-being.", "식물이 자라고 번성하는 것을 지켜보며 얻는 성취감은 자존감과 전반적인 행복도 높여 줄 수 있다."]
  ];
  var T23 = [
    ["For many centuries, humans have taken advantage of tools that translate and bring into our perception natural phenomena that we can't perceive with our senses.", "수 세기 동안 인간은 우리가 감각으로 지각할 수 없는 자연 현상을 변환하여 우리의 지각 안으로 가져오는 도구를 이용해 왔다."],
    ["In some cases, this consists of simply amplifying signals that feed into our normal sensory inputs (e.g., telescopes can bring into clear view that which is too far away for our eyes to perceive on their own).", "어떤 경우에 이것은 단순히 우리의 일반적인 감각 입력으로 들어가는 신호를 확장하는 것으로 이루어진다(예를 들어, 망원경은 우리 눈이 스스로 지각하기에는 너무 멀리 있는 것을 선명하게 보이게 할 수 있다)."],
    ["Other instruments turn signals that we cannot perceive into ones that we can observe.", "다른 도구들은 우리가 지각할 수 없는 신호를 우리가 관찰할 수 있는 신호로 바꾼다."],
    ["Some of these take the form of expanding the reach of our current senses, such as creating visible images based on the ultraviolet spectrum of light or changing sounds that are normally outside the range of what human ears can hear into audible signals.", "이 중 일부는 빛의 자외선 스펙트럼을 바탕으로 눈에 보이는 이미지를 만들거나, 보통 인간의 귀가 들을 수 있는 범위 밖에 있는 소리를 들을 수 있는 신호로 바꾸는 것처럼, 우리의 현재 감각이 미치는 범위를 넓히는 형태를 취한다."],
    ["Alternatively, some instruments measure properties for which we have no sensory capacity at all and change them into that which we can observe.", "또는, 어떤 도구들은 우리가 감지할 능력이 전혀 없는 속성을 측정하여 그것을 우리가 관찰할 수 있는 것으로 바꾼다."]
  ];
  var T24 = [
    ["Many opponents of animal experimentation argue that not only is modern medicine not the only cause for the decline in mortality, many medical advances that did contribute to human health were not the result of animal experimentation.", "동물 실험의 많은 반대자들은 현대 의학이 사망률 감소의 유일한 원인이 아닐 뿐만 아니라, 인간의 건강에 실제로 기여한 많은 의학적 진보도 동물 실험의 결과가 아니었다고 주장한다."],
    ["Defenders of research have claimed that since there is a strong correlation between the practice of animal experimentation and medical advancement, the former caused the latter.", "연구 옹호자들은 동물 실험 관행과 의학 발전 사이에 강한 상관관계가 있으므로 전자가 후자를 일으켰다고 주장해 왔다."],
    ["Opponents of research reject this inference.", "연구 반대자들은 이 추론을 거부한다."],
    ["After all, we have independent reasons to expect these phenomena to be correlated.", "결국, 우리에게는 이 현상들이 상관관계가 있을 것이라고 예상할 별개의 이유가 있다."],
    ["Since the law prescribes that all new drugs, prosthetic devices, and surgical techniques be tried on animals before they are used in humans, we will subsequently find that all medical advances are correlated with prior experimentation on animals.", "법은 모든 신약, 보철 장치, 수술 기법이 인간에게 사용되기 전에 동물에게 시험되도록 규정하므로, 우리는 결과적으로 모든 의학적 진보가 사전 동물 실험과 상관관계가 있다는 것을 알게 될 것이다."],
    ["Consequently, the correlation between animal experimentation and medical discovery is the result of legal necessity, not evidence that animal experimentation led to medical advances.", "따라서 동물 실험과 의학적 발견 사이의 상관관계는 법적 필요성의 결과이지, 동물 실험이 의학적 진보로 이어졌다는 증거가 아니다."],
    ["Moreover, several influential physicians have offered historical evidence that animal experimentation has not been as responsible for biomedical discovery as defenders suggest.", "게다가 몇몇 영향력 있는 의사들은 동물 실험이 옹호자들이 말하는 것만큼 생물 의학적 발견에 기여하지 않았다는 역사적 증거를 제시해 왔다."],
    ["They claim that clinical discoveries played a more substantial role than animal researchers have led us to believe.", "그들은 임상적 발견이 동물 연구자들이 우리에게 믿게 해 온 것보다 더 상당한 역할을 했다고 주장한다."]
  ];

window.PKG = {
  id: 'h1-mock-2509',
  school: '고1 모의고사(2025년 9월 학평)',
  unit: '18~24번',
  title: 'September 2025 Mock Test',
  titleKo: '2025년 9월 고1 전국연합학력평가',
  exam: '내신·모의고사',
  prose: true,
  teacherPhone: '',            /* 결과 받을 번호. 예: '010-1234-5678' */

  days: [
  /* ═══════════════════════════ DAY 1 · 18~20번 ═══════════════════════════ */
  {
    id: 'd1', name: 'DAY 1', range: '18~20번', story: '18 글의 목적 · 19 심경 변화 · 20 필자의 주장',
    passage: [].concat(sec('18번 · 글의 목적'), rows(T18), sec('19번 · 심경 변화'), rows(T19), sec('20번 · 필자의 주장'), rows(T20)),
    steps: [
      { type: 'vocab', title: '핵심어휘·숙어', quizN: 15, items: [
        ['reach out', '연락하다', 18], ['regarding', '~에 관한', 18], ['operating hours', '운영 시간', 18], ['at present', '현재', 18],
        ['resource', '자료, 자원', 18], ['regular class hours', '정규 수업 시간', 18], ['particularly', '특히', 18], ['college entrance exam', '대학 입시', 18],
        ['academic', '학업의', 18], ['demand', '요구하다, 필요로 하다', 18], ['resourceful', '자료가 풍부한', 18], ['extend', '연장하다', 18],
        ['benefit', '~에게 도움이 되다', 18], ['additional', '추가의', 18], ['proposal', '제안', 18], ['glance at', '~을 힐끗 보다', 19],
        ['casting director', '캐스팅 감독', 19], ['shaky', '떨리는', 19], ['chew', '씹다, 물어뜯다', 19], ['jiggle', '달달 떨다', 19],
        ['announce', '알리다, 발표하다', 19], ['a rush of excitement', '밀려오는 흥분', 19], ['be involved in', '~에 참여하다', 19], ['production', '(연극·뮤지컬) 공연, 작품', 19],
        ['inefficient', '비효율적인', 20], ['overlook', '간과하다', 20], ['potential', '잠재적인', 20], ['pressing', '긴급한, 급박한', 20],
        ["It's no wonder that ~", '~은 놀랄 일이 아니다', 20], ['get ~ off to a great start', '~을 훌륭하게 시작하다', 20], ['set the tone', '분위기를 정하다', 20], ['routine', '루틴, 정해진 절차', 20],
        ['transition', '전환', 20], ['establish', '확립하다, 만들다', 20]
      ]},
      { type: 'mc', title: '실전 문항', guide: '시험지 원문항이에요. 지문을 읽고 답을 고르세요.', items: [
        { n: 18, q: exam(18, '다음 글의 목적으로 가장 적절한 것은?', T18), opts: ['도서관 운영 시간 연장을 요청하려고', '신간 도서 구입을 건의하려고', '도서관 프로그램 확대를 부탁하려고', '도서 대출 시스템 개선에 감사하려고', '도서관 열람실 공간 확대를 제안하려고'], ex: '정답 ③ · I\'d like to ask you to extend the library\'s operating hours to 7 p.m.', per: [["", "Therefore, I'd like to ask you to extend the library's operating hours to 7 p.m.", "\"Therefore, I'd like to ask you to ~\"가 요청의 핵심 문장 → 운영 시간 연장 요청"], ["", "", "새 책 구입 이야기는 없음"], ["", "", "도서관 프로그램은 언급되지 않음"], ["", "I hope you will consider this proposal", "감사 편지가 아니라 제안·요청하는 편지"], ["", "a quiet and resourceful environment", "조용한 환경 언급은 있지만, 공간이 아니라 \"시간\" 연장을 요청함"]] },
        { n: 19, q: exam(19, '다음 글에 드러난 \'I\'의 심경 변화로 가장 적절한 것은?', T19), opts: ['nervous → pleased', 'puzzled → calm', 'bored → confused', 'satisfied → regretful', 'confident → disappointed'], ex: '정답 ③ · shaky all over, chewing my thumbnail(긴장) → a little rush of excitement(기쁨)', per: [["긴장한 → 기쁜", ["I felt shaky all over", "I got a little rush of excitement"], "손톱을 물어뜯고 발을 떪(긴장) → 합격 소식에 흥분(기쁨)"], ["어리둥절한 → 차분한", "", "어리둥절할 상황이 아니고, 마지막엔 흥분함"], ["지루한 → 혼란스러운", "", "지루해하지 않고 초조해함"], ["만족한 → 후회하는", "", "후회할 일이 없음, 합격함"], ["자신감 있는 → 실망한", "I felt shaky all over", "처음부터 떨렸고, 결과도 합격"]] },
        { n: 20, q: exam(20, '다음 글에서 필자가 주장하는 바로 가장 적절한 것은?', T20), opts: ['수업을 효과적으로 전개하기 위해 시작 루틴을 마련하라.', '학생의 적극적인 참여를 위해 포용적 수업 분위기를 형성하라.', '학습 동기를 부여할 수 있는 창의적인 수업 자료를 개발하라.', '적절한 학습량 조절을 통해 학습 부담을 줄여라.', '학생이 스스로 학습 루틴을 만들도록 장려하라.'], ex: '정답 ② · In summary, you should establish an opening routine ...', per: [["", "In summary, you should establish an opening routine", "\"In summary, you should ~\" 결론 문장이 주장"], ["", "", "포용적 분위기 이야기는 없음"], ["", "", "수업 자료 개발 이야기는 없음"], ["", "", "학습량 조절 이야기는 없음"], ["", "have taught your students an opening routine", "루틴은 교사가 가르쳐 주는 것 → \"학생 스스로\"가 틀림"]] }
      ]},
      { type: 'pick', title: '어휘선택', guide: '문맥에 맞는 낱말을 고르세요.', items: [
        { s: "As student council president, I am {reaching out|ruling out} to discuss an important matter regarding our school library's current operating hours.", ex: "reach out 연락하다 vs rule out 배제하다" },
        { s: 'At present, the library closes at 5 p.m., which many students feel {limits|liberates} their ability to fully use its resources for study and research after regular class hours.', ex: "5시에 닫아서 이용을 제한한다(limits). liberate 해방시키다" },
        { s: 'This is particularly challenging for those preparing for college entrance exams or working on academic projects that demand a quiet and {resourceful|resentful} environment.', ex: "resourceful 자료가 풍부한 vs resentful 분개한 (철자 혼동)" },
        { s: "Therefore, I'd like to ask you to {extend|extent} the library's operating hours to 7 p.m.", ex: "extend 연장하다(동사) vs extent 정도, 범위(명사)" },
        { s: 'This change would greatly benefit students by providing {additional|addictive} time to focus on their academic goals.', ex: "additional 추가의 vs addictive 중독성 있는 (철자 혼동)" },
        { s: 'I felt {shaky|shady} all over, chewing my thumbnail and jiggling my feet.', ex: "shaky 떨리는 vs shady 그늘진, 수상한 (철자 혼동)" },
        { s: 'I got a little rush of {excitement|disappointment}, knowing I was in — that whatever happened I could be involved in one of the productions.', ex: '합격했다는 걸 알고 흥분(excitement)' },
        { s: 'Inefficient teachers {overlook|oversee} the potential power of the opening minutes of class.', ex: "overlook 간과하다 vs oversee 감독하다 (단골 혼동어)" },
        { s: "Often, if students are quiet enough and if there are many {pressing|depressing} demands on a teacher's time at that moment, more than ten minutes can disappear before class starts.", ex: "pressing 긴급한 vs depressing 우울하게 하는" },
        { s: 'The first minutes set the {tone|tune} for the rest of the class.', ex: "set the tone 분위기를 정하다 vs tune 곡조" },
        { s: 'If you are prepared for class and have taught your students an opening routine, they can use this {brief|long} time to make mental and emotional transitions from the last class or subject and prepare to focus on learning new material.', ex: '처음 10분 = 짧은(brief) 시간' }
      ]},
      { type: 'tf', title: 'T/F 내용 확인', guide: '본문 내용과 일치하면 T, 다르면 F를 고르세요.', items: [
        ["Eric Park addresses the principal in his capacity as head of the student council.", true, "in one's capacity as ~의 자격으로 · address ~에게 글을 보내다", 18, "As student council president, I am reaching out"],
        ["At present, the library remains open until 7 p.m.", false, "remain open 계속 열려 있다 → 현재 5시 마감, 7시까지 연장을 요청함", 18, "At present, the library closes at 5 p.m."],
        ["Eric petitions for an earlier opening time in the morning.", false, "petition for ~을 청원하다 → 아침이 아니라 저녁 연장", 18, "extend the library's operating hours to 7 p.m."],
        ["The narrator was anxiously awaiting the outcome of her first audition.", true, "anxiously 초조하게 · await = wait for · outcome = result", 19, "the results of my first audition"],
        ["The casting director informed the narrator of the result face to face.", false, "inform A of B : A에게 B를 알리다 · face to face 직접 → 전화가 왔고 아빠가 받음", 19, "While I was coming round, Dad answered"],
        ["The narrator's father was the one who picked up the phone.", true, "pick up the phone = answer", 19, "While I was coming round, Dad answered"],
        ["The narrator was turned down for a role in the musical.", false, "be turned down 거절당하다 → second senior munchkin 배역을 받음", 19, "You're second senior munchkin"],
        ["The writer deems the opening minutes of class insignificant.", false, "deem ~로 여기다 · insignificant 하찮은 → set the tone", 20, "The first minutes set the tone"],
        ["An opening routine allows students to gear up for absorbing new material.", true, "gear up for ~할 준비를 하다 · absorb 흡수하다 (= learn)", 20, "prepare to focus on learning new material"]
      ]},
      { type: 'mc', title: '일치·불일치', guide: '선택지는 본문을 어려운 어휘로 바꿔 쓴 문장이에요. 풀고 나서 해설의 어휘를 꼭 확인하세요.', items: [
        { n: 18, q: exam(18, "글의 내용과 일치하지 <u>않는</u> 것은?", T18), opts: ["The writer is content with the library's present schedule and seeks no alteration.", "The writer contacts the principal in his capacity as head of the student council.", "The early closing time constrains students' access to the library's resources.", "Students preparing for university admission tests are particularly inconvenienced.", "The writer proposes prolonging the library's hours by two additional hours."], ex: "정답: content(만족한) · seek no alteration(변경을 원하지 않다) → 실제로는 연장을 요청함\n· in one's capacity as ~ : ~의 자격으로 (= As student council president)\n· constrain : 제한하다 (= limit)\n· university admission tests = college entrance exams\n· inconvenienced : 불편을 겪는 (← challenging)\n· prolong : 연장하다 (= extend)", per: [["필자는 도서관의 현재 일정에 만족하며 변경을 원하지 않는다.", "Therefore, I'd like to ask you to extend", "불일치 → 연장을 요청함"], ["필자는 학생회장의 자격으로 교장에게 연락한다.", "As student council president, I am reaching out", "일치"], ["이른 마감 시간이 학생들의 도서관 자료 이용을 제한한다.", "limits their ability to fully use its resources", "일치"], ["대학 입시를 준비하는 학생들이 특히 불편을 겪는다.", "particularly challenging for those preparing for college entrance exams", "일치"], ["필자는 도서관 운영 시간을 2시간 더 연장할 것을 제안한다.", ["the library closes at 5 p.m.", "extend the library's operating hours to 7 p.m."], "일치 (5시 → 7시 = 2시간)"]] },
        { n: 18, q: exam(18, "글의 내용과 <u>일치하는</u> 것은?", T18), opts: ["The writer believes the extension would afford students more time to pursue academic objectives.", "The letter was composed by a teacher on behalf of the students.", "The library is criticized for its noisy and poorly equipped environment.", "The writer demands that the library open on weekends.", "The writer threatens to organize a protest if the request is denied."], ex: "정답: afford : 제공하다 (= provide) · objective : 목표 (= goal) · pursue : 추구하다\n· compose : (글을) 쓰다 · on behalf of : ~을 대신하여 → 실제 필자는 학생회장\n· poorly equipped : 시설이 부족한 → 글에 없음\n· demand : 요구하다 · threaten : 위협하다 → 글에 없음", per: [["필자는 연장이 학생들에게 학업 목표를 추구할 시간을 더 줄 것이라고 믿는다.", "This change would greatly benefit students by providing additional time", "일치"], ["이 편지는 교사가 학생들을 대신해 썼다.", "As student council president", "불일치 → 학생회장 Eric Park가 씀"], ["도서관이 시끄럽고 시설이 부족하다고 비판받는다.", "", "불일치 → 언급 없음"], ["필자는 도서관이 주말에 문을 열 것을 요구한다.", "", "불일치 → 주말이 아니라 저녁 7시까지 연장"], ["필자는 요청이 거절되면 시위를 조직하겠다고 위협한다.", "I hope you will consider this proposal", "불일치 → 정중하게 고려를 부탁할 뿐"]] },
        { n: 19, q: exam(19, "글의 내용과 일치하지 <u>않는</u> 것은?", T19), opts: ["The narrator received the news directly from the casting director over the phone.", "The narrator was apprehensive while awaiting the outcome of the audition.", "The narrator exhibited physical signs of anxiety, such as fidgeting.", "Her father relayed the message once he had hung up the phone.", "The narrator was elated to learn she had secured a role."], ex: "정답: directly(직접) → 실제로는 아빠가 받아서 전해 줌\n· apprehensive : 불안한 (= shaky) · await : 기다리다 · outcome : 결과 (= result)\n· exhibit : 드러내다 · fidget : 안절부절못하다 (= jiggling my feet)\n· relay : 전달하다 · hang up : 전화를 끊다\n· elated : 크게 기뻐하는 (= a rush of excitement) · secure a role : 배역을 따내다", per: [["화자는 캐스팅 감독에게서 직접 전화로 소식을 들었다.", ["Dad answered", "he announced"], "불일치 → 아빠가 받아서 전해 줌"], ["화자는 오디션 결과를 기다리며 불안해했다.", "I felt shaky all over", "일치"], ["화자는 안절부절못하는 등 불안한 몸짓을 보였다.", "chewing my thumbnail and jiggling my feet", "일치"], ["아빠는 전화를 끊고 나서 소식을 전했다.", ["he was just putting the phone down", "he announced"], "일치"], ["화자는 배역을 따냈다는 것을 알고 크게 기뻐했다.", "I got a little rush of excitement, knowing I was in", "일치"]] },
        { n: 19, q: exam(19, "글의 내용과 <u>일치하는</u> 것은?", T19), opts: ["The narrator was cast as a munchkin in The Wizard of Oz.", "The narrator had performed in several musicals before this audition.", "The narrator answered the phone herself when it rang.", "The narrator felt indifferent upon hearing the result.", "The casting director postponed announcing the results."], ex: "정답: be cast as ~ : ~ 역을 맡다 (= You're second senior munchkin)\n· perform in : ~에 출연하다 → 이번이 첫(first) 오디션\n· indifferent : 무관심한 (↔ excitement) · upon -ing : ~하자마자\n· postpone : 미루다 → 10시에 바로 전화가 옴", per: [["화자는 오즈의 마법사에서 먼치킨 역을 맡았다.", "You're second senior munchkin", "일치"], ["화자는 이번 오디션 전에 여러 뮤지컬에 출연했었다.", "my first audition", "불일치 → 첫 오디션이었음"], ["전화가 울렸을 때 화자가 직접 받았다.", "Dad answered", "불일치 → 아빠가 받음"], ["화자는 결과를 듣고 무덤덤했다.", "I got a little rush of excitement", "불일치 → 흥분함"], ["캐스팅 감독은 결과 발표를 미뤘다.", "the casting director would call very soon", "불일치 → 10시에 바로 전화가 옴"]] },
        { n: 20, q: exam(20, "글의 내용과 일치하지 <u>않는</u> 것은?", T20), opts: ["Students who arrive late should be penalized to enforce punctuality.", "Ineffective teachers tend to disregard the significance of the first few minutes.", "Over ten minutes can elapse before instruction actually begins.", "The initial minutes determine the atmosphere of the entire lesson.", "A well-established routine helps students shift their focus to new material."], ex: "정답: penalize : 처벌하다 · enforce punctuality : 시간 엄수를 강제하다 → 글에 없는 내용\n· disregard : 무시하다, 간과하다 (= overlook) · significance : 중요성 (= potential power)\n· elapse : (시간이) 흐르다 (= disappear) · instruction : 수업\n· initial = first · determine the atmosphere = set the tone\n· shift : 전환하다 (= make transitions)", per: [["늦게 오는 학생은 시간 엄수를 위해 벌을 받아야 한다.", "they have little reason to be on time", "불일치 → 벌 이야기는 없음. 늦는 건 일찍 올 이유가 없어서라고 함"], ["비효율적인 교사는 처음 몇 분의 중요성을 간과하는 경향이 있다.", "Inefficient teachers overlook the potential power", "일치"], ["실제 수업이 시작되기 전에 10분 넘게 흘러갈 수 있다.", "more than ten minutes can disappear before class starts", "일치"], ["처음 몇 분이 수업 전체의 분위기를 결정한다.", "The first minutes set the tone", "일치"], ["잘 만든 루틴은 학생들이 새 내용으로 초점을 전환하도록 돕는다.", "make mental and emotional transitions", "일치"]] },
        { n: 20, q: exam(20, "글의 내용과 <u>일치하는</u> 것은?", T20), opts: ["Students have scant motivation to be punctual when class begins late.", "The writer argues that the opening minutes are trivial.", "Teachers should allocate the first ten minutes to reviewing homework.", "An opening routine is effective only for students who are already diligent.", "The writer recommends abolishing routines to encourage spontaneity."], ex: "정답: scant : 거의 없는 (= little) · motivation : 동기 (= reason) · punctual : 시간을 지키는 (= on time)\n· trivial : 사소한 (↔ potential power)\n· allocate A to B : A를 B에 할당하다 → 숙제 검토는 글에 없음\n· diligent : 성실한\n· abolish : 폐지하다 · spontaneity : 즉흥성 → 필자는 루틴을 만들라고 함", per: [["수업이 늦게 시작되면 학생들은 시간을 지킬 이유가 거의 없다.", "they have little reason to be on time", "일치"], ["필자는 수업 시작 몇 분이 사소하다고 주장한다.", "The first minutes set the tone", "불일치 → 오히려 중요하다고 함"], ["교사는 처음 10분을 숙제 검토에 써야 한다.", "", "불일치 → 숙제 이야기는 없음"], ["시작 루틴은 이미 성실한 학생에게만 효과가 있다.", "", "불일치 → 그런 조건은 없음"], ["필자는 즉흥성을 위해 루틴을 없앨 것을 권한다.", "you should establish an opening routine", "불일치 → 루틴을 만들라고 함"]] }
      ]},
      { type: 'pick', title: '어법선택', guide: '어법상 알맞은 것을 고르세요.', items: [
        { s: 'At present, the library closes at 5 p.m., {which|that} many students feel limits their ability to fully use its resources for study and research after regular class hours.', ex: '콤마 뒤 계속적 용법 → which (that은 쓸 수 없음)' },
        { s: 'This is particularly challenging for those {preparing|prepared} for college entrance exams or working on academic projects that demand a quiet and resourceful environment.', ex: 'those가 "준비하는" 능동 → 현재분사 preparing' },
        { s: "Therefore, I'd like to ask you {to extend|extending} the library's operating hours to 7 p.m.", ex: 'ask + 목적어 + to부정사' },
        { s: 'This change would greatly benefit students by {providing|provide} additional time to focus on their academic goals.', ex: '전치사 by + 동명사' },
        { s: 'I hope you will consider this proposal as a step toward {improving|improve} our academic environment and better supporting our needs.', ex: 'toward는 전치사 → 동명사 improving' },
        { s: 'That meant the casting director {would|will} call very soon with the results of my first audition for a musical part in The Wizard of Oz.', ex: '주절이 과거(meant) → 시제 일치 would' },
        { s: 'I felt shaky all over, {chewing|chewed} my thumbnail and jiggling my feet.', ex: '내가 물어뜯는 능동 → 분사구문 chewing' },
        { s: 'As I got to the bottom of the stairs, he was just {putting|put} the phone down.', ex: '과거진행형 was + -ing' },
        { s: "Often, if students are quiet enough and if there {are|is} many pressing demands on a teacher's time at that moment, more than ten minutes can disappear before class starts.", ex: 'there + be + 복수 주어(many pressing demands) → are' },
        { s: "It's no wonder that students are late for class; they have {little|few} reason to be on time.", ex: 'reason(이유)은 여기서 셀 수 없는 명사 → little(거의 없는)' },
        { s: 'If you are prepared for class and have taught your students an opening routine, they can use this brief time to make mental and emotional transitions from the last class or subject and prepare to focus on {learning|learn} new material.', ex: 'focus on + 동명사' }
      ]},
      { type: 'verb', title: '동사변형', guide: '( ) 안의 동사를 알맞은 형태로 바꿔 쓰세요.', items: [
        { s: 'I hope this message ___ you well.', v: 'find', a: ['finds'], ex: '3인칭 단수 현재' },
        { s: "As student council president, I am ___ out to discuss an important matter regarding our school library's current operating hours.", v: 'reach', a: ['reaching'], ex: '현재진행형 am + -ing' },
        { s: 'At present, the library closes at 5 p.m., which many students feel ___ their ability to fully use its resources for study and research after regular class hours.', v: 'limit', a: ['limits'], ex: 'which(= 5시에 닫는 것)가 주어 → limits. many students feel은 삽입절' },
        { s: 'I ___ at the clock on the wall.', v: 'glance', a: ['glanced'], ex: '과거 시제' },
        { s: 'Finally, the telephone ___.', v: 'ring', a: ['rang'], ex: 'ring - rang - rung' },
        { s: 'I heard him ___, "Ahh, thank you. I\'ll let her know ..."', v: 'say', a: ['say', 'saying'], ex: '지각동사 hear + 목적어 + 동사원형' },
        { s: 'I got a little rush of excitement, ___ I was in — that whatever happened I could be involved in one of the productions.', v: 'know', a: ['knowing'], ex: '분사구문(이유) → knowing' },
        { s: 'You can use the first ten minutes to get your class off to a great start, or you can choose ___ this time.', v: 'waste', a: ['to waste'], ex: 'choose + to부정사' },
        { s: 'If you are prepared for class and have ___ your students an opening routine, they can use this brief time to make mental and emotional transitions from the last class or subject and prepare to focus on learning new material.', v: 'teach', a: ['taught'], ex: '현재완료 have + p.p. (teach - taught - taught)' },
        { s: 'In summary, you should establish an opening routine ___ your class with an effective start.', v: 'develop', a: ['to develop'], ex: '목적의 to부정사' },
        { s: 'This change would greatly benefit students by providing additional time ___ on their academic goals.', v: 'focus', a: ['to focus'], ex: 'time을 꾸미는 to부정사(형용사적 용법)' }
      ]},
      { type: 'error', title: '오류찾기', guide: '어법상 틀린 곳을 고르세요.', items: [
        { s: "Therefore, I'd like to ask you [[extend]] the library's operating hours to 7 p.m. This change would greatly [[benefit]] students by [[providing]] additional time [[to focus]] on their academic goals.", w: 0, fix: 'to extend', ex: 'ask + 목적어 + to부정사' },
        { s: 'At present, the library closes at 5 p.m., [[that]] many students feel [[limits]] their ability to fully [[use]] its resources for study and research after regular class hours.', w: 0, fix: 'which', ex: '계속적 용법에는 that을 쓸 수 없다 → which' },
        { s: 'I felt shaky all over, [[chewed]] my thumbnail and [[jiggling]] my feet. Finally, the telephone [[rang]].', w: 0, fix: 'chewing', ex: '동시동작 분사구문, jiggling과 병렬 → chewing' },
        { s: 'As I [[got]] to the bottom of the stairs, he was just [[putting]] the phone down. "That was The Wizard of Oz. You\'re second senior munchkin," he [[announced]]. I got a little rush of excitement, [[knew]] I was in', w: 3, fix: 'knowing', ex: '접속사 없이 동사가 두 개 → 분사구문 knowing' },
        { s: "It's no wonder that students [[are]] late for class; they have little reason [[being]] on time. You can use the first ten minutes [[to get]] your class off to a great start, or you can choose [[to waste]] this time.", w: 1, fix: 'to be', ex: 'reason을 꾸미는 to부정사 → to be' },
        { s: 'The first minutes [[set]] the tone for the rest of the class. If you [[are]] prepared for class and have [[teach]] your students an opening routine, they can use this brief time [[to make]] mental and emotional transitions', w: 2, fix: 'taught', ex: '현재완료 have + p.p.' },
        { s: "Inefficient teachers [[overlook]] the potential power of the opening minutes of class. Often, if students are quiet enough and if there [[is]] many pressing demands on a teacher's time at that moment, more than ten minutes can [[disappear]] before class [[starts]].", w: 1, fix: 'are', ex: 'there + be + 복수 주어 → are' }
      ]},
      { type: 'scramble', title: '본문 스크램블', guide: '우리말에 맞게 단어를 눌러 문장을 완성하세요.', items: [
        { ko: '이 편지를 받으실 때 잘 지내고 계시기를 바랍니다. (직역: 이 메시지가 선생님께 잘 지내시는 상태로 닿기를 바랍니다.)', en: 'I hope this message finds you well.' },
        { ko: '이 변화는 학업 목표에 집중할 추가 시간을 제공함으로써 학생들에게 큰 도움이 될 것입니다.', en: 'This change would greatly benefit students by providing additional time to focus on their academic goals.' },
        { ko: '나는 벽에 걸린 시계를 힐끗 보았다.', en: 'I glanced at the clock on the wall.' },
        { ko: '내가 (전화 쪽으로) 오고 있는 동안 아빠가 전화를 받았다.', en: 'While I was coming round, Dad answered.' },
        { ko: '내가 계단 아래에 다다랐을 때, 아빠는 막 전화를 내려놓고 있었다.', en: 'As I got to the bottom of the stairs, he was just putting the phone down.' },
        { ko: '학생들이 수업에 늦는 것은 놀랄 일이 아니다. 그들은 제시간에 올 이유가 거의 없다.', en: "It's no wonder that students are late for class; they have little reason to be on time." },
        { ko: '처음 몇 분이 수업의 나머지 시간의 분위기를 정한다.', en: 'The first minutes set the tone for the rest of the class.' }
      ]},
      { type: 'order', title: '문장순서', guide: '문장을 본문 순서대로 눌러서 배열하세요.', items: [
        { lines: [T18[2][0], T18[3][0], T18[4][0], T18[5][0], T18[6][0]], flow: ["학생회장으로서 도서관 운영 시간 문제로 연락함", "현재 5시 마감 → 자료 이용이 제한됨", "입시·학업 프로젝트 학생에게 특히 힘듦", "그래서 7시까지 연장을 요청함", "연장하면 학업 목표에 집중할 시간이 생김"] },
        { lines: [T19[0][0], T19[1][0], T19[2][0], T19[3][0]], flow: ["벽시계를 힐끗 봄", "10시", "곧 오디션 결과 전화가 올 시간", "온몸이 떨리고 손톱을 물어뜯음"] },
        { lines: [T19[4][0], T19[5][0], T19[6][0], T19[7][0], T19[8][0]], flow: ["마침내 전화가 울림", "내가 오는 사이 아빠가 받음", "아빠가 \"알려 줄게요\"라고 말함", "계단 아래 오니 아빠가 전화를 내려놓음", "아빠: \"먼치킨 역에 붙었어\""] },
        { lines: [T20[0][0], T20[1][0], T20[2][0], T20[3][0], T20[4][0]], flow: ["비효율적인 교사는 수업 첫 몇 분을 간과함", "수업 시작 전 10분 넘게 사라지기도 함", "그러니 학생들이 늦는 건 당연함", "처음 10분을 잘 쓸 수도, 낭비할 수도 있음", "처음 몇 분이 수업 분위기를 정함"] },
        { lines: [T20[4][0], T20[5][0], T20[6][0]], flow: ["처음 몇 분이 수업 분위기를 정함", "시작 루틴이 있으면 학생들이 전환·집중 준비를 함", "결론: 시작 루틴을 만들어라"] }
      ]},
      { type: 'insert', title: '문장삽입', guide: '주어진 문장이 들어가기에 가장 알맞은 곳을 고르세요.', items: [
        { lines: [T18[3][0], T18[4][0], T18[5][0], T18[6][0]], given: 2, flow: ["현재 5시 마감 → 이용이 제한됨", "입시 준비 학생들에게 특히 힘듦", "그래서 7시까지 연장을 요청함", "이 변화(연장)가 학생들에게 도움이 됨"], ex: '5시 마감의 문제점을 말한 뒤 Therefore로 연장을 요청한다. This change는 연장을 가리킨다.' },
        { lines: [T19[4][0], T19[5][0], T19[6][0], T19[7][0]], given: 1, flow: ["전화가 울림", "아빠가 전화를 받음", "아빠가 \"알려 줄게요\"라고 말함", "아빠가 전화를 내려놓음"], ex: '전화가 울림 → 아빠가 받음 → 아빠(him)가 말하는 것을 들음' },
        { lines: [T19[0][0], T19[1][0], T19[2][0], T19[3][0]], given: 2, flow: ["시계를 봄", "10시", "그것(10시)은 곧 결과 전화가 온다는 뜻", "긴장해서 온몸이 떨림"], ex: 'That meant의 That은 바로 앞의 10:00을 가리킨다.' },
        { lines: [T20[2][0], T20[3][0], T20[4][0], T20[5][0]], given: 3, flow: ["학생들이 늦는 건 당연함", "첫 10분을 쓸지 낭비할지는 선택", "첫 몇 분이 분위기를 정함", "루틴이 있으면 이 짧은 시간을 전환에 씀"], ex: 'this brief time = 앞에서 말한 처음 몇 분' }
      ]},
      { type: 'odd', title: '어색한 문장', guide: '글의 흐름과 관계없는 문장을 고르세요.', items: [
        { lines: [T18[3][0], T18[4][0], 'Many students prefer to study at home rather than in the library.', T18[5][0]], odd: 2, ex: '도서관을 더 오래 이용하고 싶다는 흐름과 반대된다.' },
        { lines: [T19[3][0], 'I decided to give up acting and go to bed early.', T19[4][0], T19[5][0]], odd: 1, ex: '오디션 결과를 초조하게 기다리는 흐름과 맞지 않는다.' },
        { lines: [T20[3][0], T20[4][0], T20[5][0], 'Homework should always be checked at the end of every class.'], odd: 3, ex: '글은 수업 시작 시간에 관한 내용이다.' }
      ]},
      { type: 'blank', title: '빈칸추론', guide: '빈칸에 들어갈 말로 가장 알맞은 것을 고르세요.', items: [
        { s: "Therefore, I'd like to ask you to ____ to 7 p.m.", opts: ["extend the library's operating hours", "reduce the library's operating hours", "open a quiet study room", "lend more academic resources"], ex: '글의 목적: 운영 시간 연장 요청' },
        { s: 'I got a little rush of excitement, knowing I was in — that whatever happened I could ____.', opts: ["be involved in one of the productions", "direct one of the productions", "audition for another part", "watch the production for free"], ex: '배역을 받아 공연에 참여할 수 있게 되었다.' },
        { s: 'The first minutes ____ for the rest of the class.', opts: ["set the tone", "set the record", "waste the time", "end the routine"], ex: '처음 몇 분이 수업 전체 분위기를 정한다.' },
        { s: 'In summary, you should establish ____ to develop your class with an effective start.', opts: ["an opening routine", "a closing routine", "a pressing demand", "a strict rule for latecomers"], ex: '필자의 주장: 시작 루틴을 만들어라.' }
      ]},
      { type: 'mc', title: '핵심문법', guide: '알맞은 답을 고르세요.', items: [
        { n: 18, q: '빈칸에 알맞은 것은?<br><b>The library closes at 5 p.m., ______ many students feel limits their ability.</b>', opts: ['which', 'that', 'what', 'it'], ex: '콤마 뒤 계속적 용법 관계대명사 → which (that 불가)' },
        { n: 18, q: '어법상 바른 문장은?', opts: ["I'd like to ask you to extend the hours.", "I'd like to ask you extend the hours.", "I'd like to ask you extending the hours.", "I'd like to ask you extended the hours."], ex: 'ask + 목적어 + to부정사' },
        { n: 19, q: '빈칸에 알맞은 것은?<br><b>I heard him ______, "Thank you."</b>', opts: ['say', 'to say', 'said', 'to saying'], ex: '지각동사 hear + 목적어 + 동사원형(또는 -ing)' },
        { n: 19, q: '밑줄 친 부분과 바꿔 쓸 수 있는 것은?<br><b>I felt shaky all over, <u>chewing</u> my thumbnail.</b>', opts: ['and I chewed', 'because I chewed', 'although I chewed', 'if I chewed'], ex: '동시동작 분사구문 = and + 동사' },
        { n: 20, q: '빈칸에 알맞은 것은?<br><b>It\'s no ______ that students are late for class.</b> (~은 놀랄 일이 아니다)', opts: ['wonder', 'surprising', 'strange', 'worry'], ex: "It's no wonder that ~: ~은 놀랄 일이 아니다" },
        { n: 20, q: '빈칸에 알맞은 것은?<br><b>They have ______ reason to be on time.</b> (거의 없다)', opts: ['little', 'a little', 'few', 'a few'], ex: '셀 수 없는 명사 + "거의 없는" → little' },
        { n: 19, q: '빈칸에 알맞은 것은?<br><b>That meant the director ______ call very soon.</b>', opts: ['would', 'will', 'shall', 'is'], ex: '주절이 과거(meant) → 종속절도 과거(would): 시제 일치' }
      ]}
    ]
  },

  /* ═══════════════════════════ DAY 2 · 21~22번 ═══════════════════════════ */
  {
    id: 'd2', name: 'DAY 2', range: '21~22번', story: '21 밑줄 함축 의미 · 22 글의 요지',
    passage: [].concat(sec('21번 · 밑줄 함축 의미'), rows(T21), sec('22번 · 글의 요지'), rows(T22)),
    steps: [
      { type: 'vocab', title: '핵심어휘·숙어', quizN: 15, items: [
        ['atom', '원자', 21], ['nearly', '거의', 21], ['universe', '우주', 21], ['inhale', '들이마시다', 21],
        ['exhale', '내쉬다', 21], ['remaining', '나머지의, 남아 있는', 21], ['by various means', '다양한 방법으로', 21], ['make up', '구성하다', 21],
        ['pool', '공동 저장소', 21], ['cycle', '순환하다', 21], ['sweat', '땀', 21], ['evaporate', '증발시키다', 21],
        ['on a grand scale', '대규모로', 21], ['origin', '기원', 21], ['go back to', '~로 거슬러 올라가다', 21], ['limitless', '무한한', 21],
        ['nonliving', '무생물의', 21], ['caretaker', '관리인', 21], ['physical activity', '신체 활동', 22], ['a range of', '다양한', 22],
        ['harvest', '수확하다', 22], ['flexibility', '유연성', 22], ['endurance', '지구력', 22], ['weed', '잡초를 뽑다', 22],
        ['compost', '퇴비', 22], ['beneficial', '이로운', 22], ['challenging', '힘든, 어려운', 22], ['low-impact', '(몸에) 무리가 적은', 22],
        ['accessible', '접근하기 쉬운', 22], ['profound', '깊은, 심오한', 22], ['tend to (plants)', '(식물을) 돌보다', 22], ['meditative', '명상적인', 22],
        ['repetitive', '반복적인', 22], ['induce', '유도하다, 이끌어 내다', 22], ['mindfulness', '마음 챙김', 22], ['elevate', '높이다, 좋게 하다', 22],
        ['cognition', '인지', 22], ['symptom', '증상', 22], ['accomplishment', '성취', 22], ['thrive', '번성하다', 22], ['self-esteem', '자존감', 22]
      ]},
      { type: 'mc', title: '실전 문항', guide: '시험지 원문항이에요. 지문을 읽고 답을 고르세요.', items: [
        { n: 21, q: exam(21, '밑줄 친 There will be many who will follow you가 다음 글에서 의미하는 바로 가장 적절한 것은?', T21, 'There will be many who will follow you.'), opts: ['Atoms will become part of other forms after you', 'Atoms will remain unique and cannot be shared', 'Atoms will follow their original forms', 'Atoms will never be taken by a new form', 'Atoms will disappear completely after your lifetime'], ex: '정답 ① · 원자는 빌려 쓰는 것이고 계속 순환한다 → 내 다음에도 다른 형태의 일부가 된다.', per: [["원자는 당신 이후에 다른 형태의 일부가 될 것이다", ["recycling throughout the universe among limitless forms", "You're the present caretaker of the atoms"], "나는 \"현재\" 관리인일 뿐, 원자는 계속 다른 형태로 순환함"], ["원자는 고유하게 남아 공유될 수 없을 것이다", "We all share from the same atom pool", "같은 원자 저장소를 공유한다고 함"], ["원자는 원래의 형태를 따를 것이다", "", "원래 형태로 돌아간다는 내용은 없음"], ["원자는 결코 새로운 형태에 받아들여지지 않을 것이다", "among limitless forms", "무한한 형태 사이를 순환함 → 반대"], ["원자는 당신의 생이 끝나면 완전히 사라질 것이다", "have existed since the first moments of time", "시간의 시작부터 존재해 온 원자는 사라지지 않음"]] },
        { n: 22, q: exam(22, '다음 글의 요지로 가장 적절한 것은?', T22), opts: ['원예 활동은 신체적 건강과 더불어 정신적 건강에 이롭다.', '야외 활동을 통해 협동심과 자존감을 높일 수 있다.', '취미 활동을 지속적으로 할 수 있는 동기가 필요하다.', '실내에서 식물을 기르는 것은 집중력 향상에 도움이 된다.', '원예 활동은 연령에 관계없이 다양한 사람들이 즐길 수 있다.'], ex: '정답 ③ · 앞부분은 신체 건강, Besides physical health 이후는 정신 건강', per: [["", ["The act of gardening itself is a fantastic form of physical activity", "Besides physical health, gardening has profound mental health benefits"], "앞부분은 신체 건강, Besides 이후는 정신 건강 → 둘 다 이로움"], ["", "boost self-esteem", "자존감은 나오지만 협동심·야외 활동 이야기는 없음"], ["", "", "취미의 동기 이야기는 없음"], ["", "It allows you to focus on the present moment", "집중은 나오지만 \"실내\" 식물 이야기가 아님"], ["", "accessible for people of all ages", "글에 있는 내용이지만 세부 사항일 뿐 요지가 아님"]] }
      ]},
      { type: 'pick', title: '어휘선택', guide: '문맥에 맞는 낱말을 고르세요.', items: [
        { s: 'When you breathe, for example, only some of the atoms that you inhale are {exhaled|exhausted} in your next breath.', ex: "exhale 내쉬다 vs exhaust 고갈시키다, 지치게 하다" },
        { s: 'The {remaining|reminding} atoms are taken into your body to become part of you, and they later leave your body by various means.', ex: "remaining 남아 있는 vs reminding 상기시키는 (철자 혼동)" },
        { s: 'You don\'t "own" the atoms that make up your body; you {borrow|burrow} them.', ex: "borrow 빌리다 vs burrow 굴을 파다 (철자 혼동)" },
        { s: 'We {recycle|destroy} atoms on a grand scale.', ex: '원자는 순환한다 → 재활용한다(recycle).' },
        { s: 'There are atoms in your body that have existed since the first moments of time, recycling throughout the universe among {limitless|lifeless} forms, both nonliving and living.', ex: "limitless 무한한 vs lifeless 생명이 없는 (철자 혼동)" },
        { s: "You're the present {caretaker|owner} of the atoms in your body.", ex: '"소유"하지 않는다고 했으므로 관리인(caretaker)' },
        { s: 'These activities help improve strength, {flexibility|feasibility}, and endurance.', ex: "flexibility 유연성 vs feasibility 실현 가능성" },
        { s: 'Gardening is particularly {beneficial|superficial} for those who find traditional exercise challenging.', ex: "beneficial 이로운 vs superficial 피상적인" },
        { s: "It's a low-impact way to stay active and fit, making it {accessible|accessory} for people of all ages and physical abilities.", ex: "accessible 접근하기 쉬운 vs accessory 부속물, 장신구" },
        { s: 'Tending to plants can be incredibly {calming|stressful} and meditative.', ex: '스트레스를 줄여 준다 → 마음을 진정시키는(calming)' },
        { s: 'The {repetitive|repulsive} tasks involved in gardening can induce a state of mindfulness, similar to meditation.', ex: "repetitive 반복적인 vs repulsive 혐오스러운 (철자 혼동)" }
      ]},
      { type: 'tf', title: 'T/F 내용 확인', guide: '본문 내용과 일치하면 T, 다르면 F를 고르세요.', items: [
        ["Every atom we inhale is expelled with the subsequent breath.", false, "expel 내보내다 · subsequent = next → 일부(only some)만", 21, "only some of the atoms that you inhale are exhaled"],
        ["We are borrowers, not owners, of the atoms composing our bodies.", true, "compose = make up", 21, "you borrow them"],
        ["Atoms circulate among people through respiration and perspiration.", true, "circulate = cycle · respiration 호흡 · perspiration 땀", 21, "Atoms cycle from person to person"],
        ["Most heavier atoms postdate the formation of the Sun and Earth.", false, "postdate ~보다 나중에 생기다 → older than", 21, "most heavier atoms are older than the Sun and Earth"],
        ["Gardening encompasses an array of motions such as digging and harvesting.", true, "encompass = involve · an array of = a range of", 22, "It involves a range of motions"],
        ["Minor chores like weeding expend a negligible number of calories.", false, "chore 잡일 · expend 소모하다 · negligible 무시해도 될 만큼 적은 → many calories", 22, "can burn many calories"],
        ["Gardening is suitable exclusively for the young and physically robust.", false, "exclusively 오로지 · robust 튼튼한 → all ages and physical abilities", 22, "accessible for people of all ages"],
        ["Even a modest garden can help alleviate symptoms of depression.", true, "modest 작은, 소박한 · alleviate = reduce", 22, "even in a small garden"]
      ]},
      { type: 'mc', title: '일치·불일치', guide: '선택지는 본문을 어려운 어휘로 바꿔 쓴 문장이에요. 풀고 나서 해설의 어휘를 꼭 확인하세요.', items: [
        { n: 21, q: exam(21, "글의 내용과 일치하지 <u>않는</u> 것은?", T21), opts: ["All the atoms we inhale are expelled in the very next breath.", "A considerable proportion of the atoms in our bodies are nearly as ancient as the universe.", "We do not possess our atoms but merely borrow them.", "Atoms are exchanged among people through respiration and perspiration.", "The lightest atoms date back to the origin of the universe."], ex: "정답: All / expel(내보내다) → 실제로는 일부(only some)만 내쉼\n· considerable proportion : 상당한 비율 (= many) · ancient : 아주 오래된 (= old)\n· possess : 소유하다 (= own) · merely : 단지\n· respiration : 호흡 (= breathe) · perspiration : 땀 흘리기 (= sweat)\n· date back to = go back to : ~로 거슬러 올라가다", per: [["우리가 들이마신 모든 원자는 바로 다음 숨에 내보내진다.", "only some of the atoms that you inhale are exhaled", "불일치 → 일부(only some)만 내쉼"], ["우리 몸속 원자의 상당 부분은 거의 우주만큼 오래되었다.", "Many atoms in your body are nearly as old as the universe itself", "일치"], ["우리는 원자를 소유하지 않고 단지 빌릴 뿐이다.", "you borrow them", "일치"], ["원자는 호흡과 땀을 통해 사람들 사이에서 교환된다.", "Atoms cycle from person to person as we breathe and as our sweat is evaporated", "일치"], ["가장 가벼운 원자는 우주의 기원으로 거슬러 올라간다.", "The origin of the lightest atoms goes back to the origin of the universe", "일치"]] },
        { n: 21, q: exam(21, "글의 내용과 <u>일치하는</u> 것은?", T21), opts: ["Many heavier atoms predate the formation of the Sun and Earth.", "Atoms that enter the body remain there permanently.", "Each individual draws on a separate, exclusive pool of atoms.", "Atoms circulate only among living organisms.", "The recycling of atoms occurs only on a minuscule scale."], ex: "정답: predate : ~보다 먼저 존재하다 (= older than) · formation : 형성\n· permanently : 영구히 → 실제로는 나중에 몸을 떠남(leave)\n· exclusive : 독점적인 → 실제로는 같은 원자 저장소를 공유(share)\n· circulate : 순환하다 (= cycle) · organism : 생물 → 무생물(nonliving)도 포함\n· minuscule : 아주 작은 (↔ grand)", per: [["많은 무거운 원자는 태양과 지구가 생기기 전부터 있었다.", "most heavier atoms are older than the Sun and Earth", "일치"], ["몸에 들어온 원자는 영원히 그곳에 머문다.", "they later leave your body by various means", "불일치 → 나중에 몸을 떠남"], ["사람마다 따로 쓰는 독점적인 원자 저장소가 있다.", "We all share from the same atom pool", "불일치 → 같은 저장소를 공유함"], ["원자는 살아 있는 생물 사이에서만 순환한다.", "both nonliving and living", "불일치 → 무생물과 생물 모두"], ["원자 재활용은 아주 작은 규모로만 일어난다.", "We recycle atoms on a grand scale", "불일치 → 대규모로 일어남"]] },
        { n: 22, q: exam(22, "글의 내용과 일치하지 <u>않는</u> 것은?", T22), opts: ["Gardening is unsuitable for those who struggle with conventional workouts.", "Gardening encompasses diverse movements from digging to harvesting.", "Even minor chores such as weeding can expend a substantial number of calories.", "Caring for plants can have a soothing, meditative effect.", "Witnessing plants flourish can enhance one's self-esteem."], ex: "정답: unsuitable : 적합하지 않은 → 실제로는 particularly beneficial\n· struggle with : ~을 힘들어하다 (= find ~ challenging) · conventional = traditional\n· encompass : 포함하다 (= involve) · diverse = a range of\n· chore : 잡일 (= task) · expend : 소모하다 (= burn) · substantial = many\n· soothing = calming · flourish = thrive · enhance = boost", per: [["정원 가꾸기는 전통적인 운동을 힘들어하는 사람에게 맞지 않는다.", "Gardening is particularly beneficial for those who find traditional exercise challenging", "불일치 → 오히려 특히 이로움"], ["정원 가꾸기는 땅 파기부터 수확까지 다양한 동작을 포함한다.", "It involves a range of motions, from digging and planting to watering and harvesting", "일치"], ["잡초 뽑기 같은 작은 일도 상당한 칼로리를 소모할 수 있다.", "small tasks like weeding or turning compost can burn many calories", "일치"], ["식물을 돌보는 것은 마음을 달래 주는 명상적 효과가 있다.", "Tending to plants can be incredibly calming and meditative", "일치"], ["식물이 잘 자라는 것을 보면 자존감이 높아질 수 있다.", "watching your plants grow and thrive can also boost self-esteem", "일치"]] },
        { n: 22, q: exam(22, "글의 내용과 <u>일치하는</u> 것은?", T22), opts: ["Gardening's low-impact nature makes it accessible regardless of age.", "Gardening's benefits are confined to physical fitness.", "Repetitive gardening tasks tend to heighten anxiety.", "Research indicates that only large gardens alleviate depression.", "Gardening impairs cognitive function due to its monotony."], ex: "정답: regardless of : ~에 상관없이 (= people of all ages)\n· be confined to : ~에 국한되다 → 정신 건강(mental health)에도 이로움\n· heighten : 높이다 (↔ reduce)\n· alleviate : 완화하다 (= reduce) → 작은 정원(even a small garden)도 효과\n· impair : 손상시키다 (↔ improve) · cognitive : 인지의 · monotony : 단조로움", per: [["정원 가꾸기는 몸에 무리가 적어 나이에 상관없이 할 수 있다.", "making it accessible for people of all ages", "일치"], ["정원 가꾸기의 이점은 신체 건강에 국한된다.", "Besides physical health, gardening has profound mental health benefits", "불일치 → 정신 건강에도 이로움"], ["반복적인 정원 일은 불안을 높이는 경향이 있다.", "reducing stress and anxiety", "불일치 → 불안을 줄여 줌"], ["연구에 따르면 큰 정원만 우울증을 완화한다.", "even in a small garden", "불일치 → 작은 정원도 효과가 있음"], ["정원 가꾸기는 단조로워서 인지 기능을 해친다.", "improve cognition", "불일치 → 인지 능력을 향상함"]] }
      ]},
      { type: 'pick', title: '어법선택', guide: '어법상 알맞은 것을 고르세요.', items: [
        { s: 'Many atoms in your body are nearly as old {as|than} the universe itself.', ex: 'as + 원급 + as' },
        { s: 'When you breathe, for example, only some of the atoms that you inhale {are|is} exhaled in your next breath.', ex: 'some of the atoms(복수) → are' },
        { s: 'The remaining atoms are taken into your body {to become|become} part of you, and they later leave your body by various means.', ex: '결과의 to부정사' },
        { s: 'You don\'t "own" the atoms that {make|makes} up your body; you borrow them.', ex: '선행사 the atoms(복수) → make' },
        { s: 'There are atoms in your body that {have existed|has existed} since the first moments of time, recycling throughout the universe among limitless forms, both nonliving and living.', ex: '선행사 atoms(복수) → have existed' },
        { s: 'There will be many {who|which} will follow you.', ex: 'many(많은 사람들) → 사람 선행사 who' },
        { s: 'It involves a range of motions, from digging and planting to watering and {harvesting|harvest}.', ex: 'from A to B 병렬: watering and harvesting' },
        { s: 'Gardening is particularly beneficial for those who find traditional exercise {challenging|challenge}.', ex: 'find + 목적어 + 형용사 보어' },
        { s: "It's a low-impact way to stay active and fit, {making|made} it accessible for people of all ages and physical abilities.", ex: '능동 분사구문 → making' },
        { s: 'It allows you {to focus|focusing} on the present moment, reducing stress and anxiety.', ex: 'allow + 목적어 + to부정사' },
        { s: 'The repetitive tasks {involved|involving} in gardening can induce a state of mindfulness, similar to meditation.', ex: '작업이 "수반되는" 수동 → 과거분사 involved' },
        { s: 'Studies have shown that {spending|spend} time in nature, even in a small garden, can elevate mood, improve cognition, and reduce depression symptoms.', ex: 'that절의 주어 → 동명사 spending' }
      ]},
      { type: 'verb', title: '동사변형', guide: '( ) 안의 동사를 알맞은 형태로 바꿔 쓰세요.', items: [
        { s: 'Many atoms in your body ___ nearly as old as the universe itself.', v: 'be', a: ['are'], ex: '주어 Many atoms(복수) → are' },
        { s: 'When you breathe, for example, only some of the atoms that you inhale ___ in your next breath.', v: 'exhale', a: ['are exhaled'], ex: '원자가 "내쉬어지는" 수동태' },
        { s: 'The remaining atoms ___ into your body to become part of you, and they later leave your body by various means.', v: 'take', a: ['are taken'], ex: '수동태 be + p.p.' },
        { s: 'Atoms cycle from person to person as we breathe and as our sweat ___.', v: 'evaporate', a: ['is evaporated', 'evaporates'], ex: '본문: is evaporated (땀이 증발되다)' },
        { s: 'There are atoms in your body that ___ since the first moments of time, recycling throughout the universe among limitless forms, both nonliving and living.', v: 'exist', a: ['have existed'], ex: 'since + 과거 시점 → 현재완료' },
        { s: 'These activities help ___ strength, flexibility, and endurance.', v: 'improve', a: ['improve', 'to improve'], ex: 'help + (to) 동사원형' },
        { s: 'Gardening is particularly beneficial for those who ___ traditional exercise challenging.', v: 'find', a: ['find'], ex: '선행사 those(사람들, 복수) → find' },
        { s: 'Tending to plants can be incredibly ___ and meditative.', v: 'calm', a: ['calming'], ex: '마음을 진정시키는 → 현재분사형 형용사 calming' },
        { s: 'It allows you to focus on the present moment, ___ stress and anxiety.', v: 'reduce', a: ['reducing'], ex: '분사구문(결과) → reducing' },
        { s: 'Studies ___ that spending time in nature, even in a small garden, can elevate mood, improve cognition, and reduce depression symptoms.', v: 'show', a: ['have shown'], ex: '현재완료 have + p.p.' },
        { s: 'The sense of accomplishment from ___ your plants grow and thrive can also boost self-esteem and overall well-being.', v: 'watch', a: ['watching'], ex: '전치사 from + 동명사' }
      ]},
      { type: 'error', title: '오류찾기', guide: '어법상 틀린 곳을 고르세요.', items: [
        { s: 'Many atoms in your body are nearly as [[old]] as the universe itself. When you breathe, for example, only some of the atoms that you [[inhale]] [[is]] exhaled in your next [[breath]].', w: 2, fix: 'are', ex: 'some of the atoms(복수) → are' },
        { s: 'You don\'t "own" the atoms that [[make up]] your body; you borrow [[it]]. We all share from the same atom pool because atoms forever [[travel]] around, within, and among us.', w: 1, fix: 'them', ex: 'the atoms(복수)를 가리킴 → them' },
        { s: 'The origin of the lightest atoms [[goes]] back to the origin of the universe, and most heavier atoms are [[old]] than the Sun and Earth. There are atoms in your body that [[have existed]] since the first moments of time', w: 1, fix: 'older', ex: '뒤에 than → 비교급 older' },
        { s: 'It involves a range of motions, from digging and planting to watering and [[harvest]]. These activities help [[improve]] strength, flexibility, and endurance. You might not [[realize]] it, but small tasks like weeding or turning compost can [[burn]] many calories.', w: 0, fix: 'harvesting', ex: 'watering과 병렬 → harvesting' },
        { s: "Gardening is particularly beneficial for those who [[finds]] traditional exercise [[challenging]]. It's a low-impact way [[to stay]] active and fit, [[making]] it accessible for people of all ages and physical abilities.", w: 0, fix: 'find', ex: '선행사 those(복수) → find' },
        { s: 'Tending to plants can be incredibly [[calming]] and meditative. It allows you [[focus]] on the present moment, [[reducing]] stress and anxiety. The repetitive tasks [[involved]] in gardening can induce a state of mindfulness, similar to meditation.', w: 1, fix: 'to focus', ex: 'allow + 목적어 + to부정사' }
      ]},
      { type: 'scramble', title: '본문 스크램블', guide: '우리말에 맞게 단어를 눌러 문장을 완성하세요.', items: [
        { ko: '여러분 몸속의 많은 원자는 거의 우주 그 자체만큼 오래되었다.', en: 'Many atoms in your body are nearly as old as the universe itself.' },
        { ko: '우리는 대규모로 원자를 재활용한다.', en: 'We recycle atoms on a grand scale.' },
        { ko: '여러분은 몸속 원자들의 현재 관리인이다.', en: "You're the present caretaker of the atoms in your body." },
        { ko: '여러분의 뒤를 이을 많은 이들이 있을 것이다.', en: 'There will be many who will follow you.' },
        { ko: '이러한 활동은 근력, 유연성, 지구력을 향상하는 데 도움이 된다.', en: 'These activities help improve strength, flexibility, and endurance.' },
        { ko: '신체 건강 외에도, 정원 가꾸기는 정신 건강에 깊은 이점이 있다.', en: 'Besides physical health, gardening has profound mental health benefits.' },
        { ko: '식물을 돌보는 것은 놀라울 정도로 마음을 진정시키고 명상적일 수 있다.', en: 'Tending to plants can be incredibly calming and meditative.' }
      ]},
      { type: 'order', title: '문장순서', guide: '문장을 본문 순서대로 눌러서 배열하세요.', items: [
        { lines: [T21[0][0], T21[1][0], T21[2][0], T21[3][0]], flow: ["몸속 원자는 우주만큼 오래됨", "숨 쉴 때 일부만 내쉼", "나머지는 몸의 일부가 됐다가 나중에 떠남", "원자는 소유가 아니라 빌리는 것"] },
        { lines: [T21[4][0], T21[5][0], T21[6][0], T21[7][0], T21[8][0]], flow: ["모두 같은 원자 저장소를 공유함", "호흡·땀으로 사람 사이를 순환함", "대규모로 원자를 재활용함", "가벼운 원자는 우주의 기원, 무거운 원자는 태양·지구보다 오래됨", "시간의 시작부터 존재하며 무한한 형태로 순환함"] },
        { lines: [T22[0][0], T22[1][0], T22[2][0], T22[3][0], T22[4][0]], flow: ["정원 가꾸기는 훌륭한 신체 활동", "파기·심기·물 주기·수확 등 다양한 동작", "근력·유연성·지구력 향상", "잡초 뽑기 같은 작은 일도 칼로리 소모", "전통 운동이 힘든 사람에게 특히 좋음"] },
        { lines: [T22[6][0], T22[7][0], T22[8][0], T22[9][0], T22[10][0]], flow: ["신체 외에 정신 건강에도 이점", "식물 돌보기는 마음을 진정시킴", "현재에 집중 → 스트레스·불안 감소", "반복 작업이 마음 챙김 상태를 만듦", "연구: 기분·인지 향상, 우울 감소"] }
      ]},
      { type: 'insert', title: '문장삽입', guide: '주어진 문장이 들어가기에 가장 알맞은 곳을 고르세요.', items: [
        { lines: [T21[1][0], T21[2][0], T21[3][0], T21[4][0]], given: 1, flow: ["숨 쉴 때 일부만 내쉼", "나머지 원자는 몸의 일부가 됨", "원자는 소유가 아니라 빌리는 것", "모두 같은 원자 저장소를 공유함"], ex: 'The remaining atoms = 내쉬어지지 않고 남은 원자' },
        { lines: [T21[7][0], T21[8][0], T21[9][0], T21[10][0]], given: 3, flow: ["원자의 기원은 우주·태양보다 오래됨", "시간의 시작부터 순환해 온 원자", "나는 원자의 현재 관리인", "내 뒤를 이을 이들이 많을 것"], ex: '나는 현재 관리인 → 내 뒤를 이을(follow) 이들이 많다.' },
        { lines: [T22[1][0], T22[2][0], T22[3][0], T22[4][0]], given: 1, flow: ["다양한 동작을 포함함", "이런 활동들이 근력·유연성·지구력 향상", "작은 일도 칼로리 소모", "전통 운동이 힘든 사람에게 좋음"], ex: 'These activities = 앞의 땅 파기, 심기, 물 주기, 수확하기' },
        { lines: [T22[6][0], T22[7][0], T22[8][0], T22[9][0]], given: 2, flow: ["정신 건강에도 이점이 있음", "식물 돌보기는 마음을 진정시킴", "그것이 현재에 집중하게 해 스트레스 감소", "반복 작업 → 마음 챙김 상태"], ex: 'It = 식물을 돌보는 것(Tending to plants)' }
      ]},
      { type: 'odd', title: '어색한 문장', guide: '글의 흐름과 관계없는 문장을 고르세요.', items: [
        { lines: [T21[4][0], T21[5][0], 'Each person is born with a fixed set of atoms that never changes.', T21[6][0]], odd: 2, ex: '원자는 사람 사이를 계속 순환한다는 흐름과 반대된다.' },
        { lines: [T22[2][0], 'Gardening tools are often too expensive for beginners.', T22[3][0], T22[4][0]], odd: 1, ex: '정원 가꾸기의 신체적 이점에 관한 흐름과 관계없다.' },
        { lines: [T22[7][0], T22[8][0], T22[9][0], 'Indoor exercise is the only way to reduce stress.'], odd: 3, ex: '정원 가꾸기가 스트레스를 줄인다는 내용과 맞지 않는다.' }
      ]},
      { type: 'blank', title: '빈칸추론', guide: '빈칸에 들어갈 말로 가장 알맞은 것을 고르세요.', items: [
        { s: 'You don\'t "own" the atoms that make up your body; you ____.', opts: ["borrow them", "own them", "exhale them", "create them"], ex: '소유가 아니라 빌린다 → 계속 순환' },
        { s: 'We all share from the same atom pool because atoms forever ____ around, within, and among us.', opts: ["travel", "remain", "vanish", "settle"], ex: '원자는 영원히 돌아다닌다(travel).' },
        { s: 'Gardening is particularly beneficial for those who find ____ challenging.', opts: ["traditional exercise", "gardening tasks", "mental health", "repetitive tasks"], ex: '전통적인 운동이 힘든 사람에게 이롭다.' },
        { s: 'The repetitive tasks involved in gardening can induce a state of ____, similar to meditation.', opts: ["mindfulness", "anxiety", "exhaustion", "depression"], ex: '명상과 비슷한 마음 챙김(mindfulness)' }
      ]},
      { type: 'mc', title: '핵심문법', guide: '알맞은 답을 고르세요.', items: [
        { n: 21, q: '빈칸에 알맞은 것은?<br><b>Many atoms are nearly ______ old as the universe.</b>', opts: ['as', 'so', 'more', 'than'], ex: 'as + 원급 + as: ~만큼 …한' },
        { n: 21, q: '빈칸에 알맞은 것은?<br><b>Only some of the atoms that you inhale ______ exhaled.</b>', opts: ['are', 'is', 'be', 'being'], ex: 'some of + 복수 명사 → 복수 동사' },
        { n: 21, q: '빈칸에 알맞은 것은?<br><b>There will be many ______ will follow you.</b>', opts: ['who', 'which', 'what', 'whose'], ex: '사람(many) + 주격 관계대명사 who' },
        { n: 22, q: '어법상 바른 문장은?', opts: ['It allows you to focus on the present.', 'It allows you focus on the present.', 'It allows you focusing on the present.', 'It allows to you focus on the present.'], ex: 'allow + 목적어 + to부정사' },
        { n: 22, q: '빈칸에 알맞은 것은?<br><b>Gardening is beneficial for those who find traditional exercise ______.</b>', opts: ['challenging', 'challengingly', 'challenges', 'to challenge'], ex: 'find + 목적어 + 형용사(목적격 보어)' },
        { n: 22, q: '빈칸에 알맞은 것은?<br><b>The tasks ______ in gardening can induce mindfulness.</b>', opts: ['involved', 'involving', 'involve', 'to involve'], ex: '"수반되는" 수동 의미 → 과거분사' },
        { n: 22, q: '밑줄 친 부분과 바꿔 쓸 수 있는 것은?<br><b><u>Besides</u> physical health, gardening has mental health benefits.</b>', opts: ['In addition to', 'Instead of', 'Because of', 'Except for'], ex: 'besides: ~외에도 = in addition to' }
      ]}
    ]
  },

  /* ═══════════════════════════ DAY 3 · 23~24번 ═══════════════════════════ */
  {
    id: 'd3', name: 'DAY 3', range: '23~24번', story: '23 글의 주제 · 24 글의 제목',
    passage: [].concat(sec('23번 · 글의 주제'), rows(T23), sec('24번 · 글의 제목'), rows(T24)),
    steps: [
      { type: 'vocab', title: '핵심어휘·숙어', quizN: 15, items: [
        ['take advantage of', '~을 이용하다', 23], ['translate', '변환하다, 바꾸다', 23], ['perception', '지각', 23], ['phenomena', '현상들 (단수 phenomenon)', 23],
        ['perceive', '지각하다', 23], ['consist of', '~으로 이루어지다', 23], ['amplify', '확장하다, 증폭하다', 23], ['signal', '신호', 23],
        ['sensory input', '감각 입력', 23], ['telescope', '망원경', 23], ['instrument', '도구, 기구', 23], ['observe', '관찰하다', 23],
        ['expand', '넓히다, 확장하다', 23], ['reach', '(미치는) 범위', 23], ['visible', '눈에 보이는', 23], ['ultraviolet', '자외선의', 23],
        ['audible', '들을 수 있는', 23], ['alternatively', '또는, 그 대신에', 23], ['property', '속성', 23], ['capacity', '능력', 23],
        ['opponent', '반대자', 24], ['experimentation', '실험', 24], ['decline', '감소', 24], ['mortality', '사망률', 24],
        ['contribute to', '~에 기여하다', 24], ['defender', '옹호자', 24], ['correlation', '상관관계', 24], ['the former / the latter', '전자 / 후자', 24],
        ['reject', '거부하다', 24], ['inference', '추론', 24], ['independent', '별개의, 독립적인', 24], ['prescribe', '규정하다', 24],
        ['prosthetic', '보철의', 24], ['surgical', '수술의', 24], ['subsequently', '그 결과, 그 후에', 24], ['prior', '사전의, 이전의', 24],
        ['consequently', '따라서, 그 결과', 24], ['legal necessity', '법적 필요성', 24], ['influential', '영향력 있는', 24], ['physician', '의사', 24],
        ['clinical', '임상의', 24], ['substantial', '상당한', 24]
      ]},
      { type: 'mc', title: '실전 문항', guide: '시험지 원문항이에요. 지문을 읽고 답을 고르세요.', items: [
        { n: 23, q: exam(23, '다음 글의 주제로 가장 적절한 것은?', T23), opts: ['the tools that increase the ability of human senses', 'difficulties in replacing human senses with tools', 'human senses that inspire the inventing of scientific tools', 'differences between visual and auditory senses in humans', 'the power of human imagination in discovering the universe'], ex: '정답 ② · 감각으로 지각할 수 없는 것을 지각하게 해 주는 도구들', per: [["인간 감각의 능력을 높여 주는 도구", ["humans have taken advantage of tools", "expanding the reach of our current senses"], "글 전체가 감각으로 못 느끼는 것을 느끼게 해 주는 도구 이야기"], ["인간의 감각을 도구로 대체하는 것의 어려움", "", "어려움은 언급되지 않음"], ["과학 도구 발명에 영감을 주는 인간의 감각", "", "감각이 발명의 영감이라는 내용은 없음"], ["인간의 시각과 청각의 차이", "changing sounds", "시각·청각 예시가 나오지만 차이를 비교하는 글이 아님"], ["우주 발견에서 인간 상상력의 힘", "", "상상력 이야기는 없음"]] },
        { n: 24, q: exam(24, '다음 글의 제목으로 가장 적절한 것은?', T24), opts: ['Is Medicine Advanced by Experimenting on Animals?', 'Bio-medicine: Unlocking New Frontiers in Health Care', 'Refer to Historical Evidence to Solve Medical Issues', "Why Aren't There Strict Laws for Animal Adoption?", 'Medical Advances for Extending Human Life Span'], ex: '정답 ② · 동물 실험이 의학 발전을 이끌었다는 주장에 반대자들이 반박하는 글', per: [["의학은 동물 실험으로 발전하는가?", ["Opponents of research reject this inference", "the correlation between animal experimentation and medical discovery is the result of legal necessity"], "동물 실험 → 의학 발전이라는 주장에 의문을 제기하는 글"], ["생의학: 의료의 새로운 영역을 열다", "", "새 영역 개척 이야기가 아님"], ["의료 문제 해결을 위해 역사적 증거를 참고하라", "several influential physicians have offered historical evidence", "역사적 증거는 근거 중 하나일 뿐, 의료 문제 해결 이야기가 아님"], ["왜 동물 입양에 대한 엄격한 법은 없을까?", "the law prescribes", "입양 이야기는 없음, 법은 실험을 의무화하는 법"], ["인간 수명 연장을 위한 의학적 진보", "the decline in mortality", "사망률 감소 언급은 있지만 수명 연장 방법 이야기가 아님"]] }
      ]},
      { type: 'pick', title: '어휘선택', guide: '문맥에 맞는 낱말을 고르세요.', items: [
        { s: "For many centuries, humans have taken {advantage|advent} of tools that translate and bring into our perception natural phenomena that we can't perceive with our senses.", ex: "take advantage of 이용하다 vs advent 출현, 도래" },
        { s: 'In some cases, this consists of simply {amplifying|reducing} signals that feed into our normal sensory inputs (e.g., telescopes can bring into clear view that which is too far away for our eyes to perceive on their own).', ex: '망원경 → 신호를 확장한다(amplifying).' },
        { s: 'Other instruments turn signals that we cannot perceive into ones that we can {observe|obscure}.', ex: "observe 관찰하다 vs obscure 가리다, 모호하게 하다" },
        { s: 'Some of these take the form of {expanding|expending} the reach of our current senses, such as creating visible images based on the ultraviolet spectrum of light or changing sounds that are normally outside the range of what human ears can hear into audible signals.', ex: "expand 넓히다 vs expend 소비하다 (철자 혼동)" },
        { s: 'Alternatively, some instruments measure properties for which we have no sensory {capacity|captivity} at all and change them into that which we can observe.', ex: "capacity 능력 vs captivity 감금, 포로 상태" },
        { s: 'Defenders of research have claimed that since there is a strong {correlation|corrosion} between the practice of animal experimentation and medical advancement, the former caused the latter.', ex: "correlation 상관관계 vs corrosion 부식 (철자 혼동)" },
        { s: 'Opponents of research {reject|accept} this inference.', ex: '반대자들은 추론을 거부한다(reject).' },
        { s: 'Consequently, the correlation between animal experimentation and medical discovery is the result of {legal|lethal} necessity, not evidence that animal experimentation led to medical advances.', ex: "legal 법적인 vs lethal 치명적인 (철자 혼동)" },
        { s: 'Moreover, several {influential|inferential} physicians have offered historical evidence that animal experimentation has not been as responsible for biomedical discovery as defenders suggest.', ex: "influential 영향력 있는 vs inferential 추론의" },
        { s: 'They claim that clinical discoveries played a more {substantial|minor} role than animal researchers have led us to believe.', ex: '임상적 발견이 더 상당한(substantial) 역할' }
      ]},
      { type: 'tf', title: 'T/F 내용 확인', guide: '본문 내용과 일치하면 T, 다르면 F를 고르세요.', items: [
        ["Telescopes enhance signals so that distant objects become discernible.", true, "enhance ≒ amplify · discernible 식별 가능한", 23, "telescopes can bring into clear view"],
        ["All instruments merely intensify signals our senses can already detect.", false, "merely 단지 · intensify 강화하다 → 감각이 전혀 없는 속성을 재는 도구도 있음", 23, "some instruments measure properties for which we have no sensory capacity at all"],
        ["Some devices transform sounds beyond our hearing range into audible ones.", true, "transform = change · beyond ~의 범위를 넘어선", 23, "changing sounds that are normally outside the range"],
        ["No instrument can gauge properties that lie entirely beyond human senses.", false, "gauge = measure → 그런 속성을 재는 도구가 있음", 23, "some instruments measure properties for which we have no sensory capacity at all"],
        ["Proponents of animal research credit it with driving medical progress.", true, "proponent = defender · credit A with B : B를 A의 공으로 돌리다", 24, "the former caused the latter"],
        ["Opponents of research endorse the inference drawn by defenders.", false, "endorse 지지하다 → reject", 24, "Opponents of research reject this inference"],
        ["The law mandates animal testing of new drugs prior to human use.", true, "mandate = prescribe · prior to = before", 24, "the law prescribes that all new drugs"],
        ["Some physicians argue that clinical findings were less consequential than animal research.", false, "consequential 중대한 → 임상적 발견이 더 큰 역할", 24, "clinical discoveries played a more substantial role"]
      ]},
      { type: 'mc', title: '일치·불일치', guide: '선택지는 본문을 어려운 어휘로 바꿔 쓴 문장이에요. 풀고 나서 해설의 어휘를 꼭 확인하세요.', items: [
        { n: 23, q: exam(23, "글의 내용과 일치하지 <u>않는</u> 것은?", T23), opts: ["Every instrument merely magnifies signals our senses can already detect.", "Telescopes enable us to discern objects too distant for the naked eye.", "Some devices convert imperceptible signals into observable ones.", "Certain tools render ultraviolet light as visible images.", "Some instruments gauge properties for which humans lack any sensory faculty."], ex: "정답: Every / merely(단지) → 감각이 전혀 없는 속성을 재는 도구도 있음\n· magnify : 확대하다 (= amplify) · detect : 감지하다\n· discern : 식별하다 · distant = far away · the naked eye : 맨눈\n· convert = turn · imperceptible : 지각할 수 없는 (= cannot perceive)\n· render A as B : A를 B로 나타내다 · gauge = measure · faculty = capacity", per: [["모든 도구는 우리 감각이 이미 감지할 수 있는 신호를 단지 확대할 뿐이다.", "some instruments measure properties for which we have no sensory capacity at all", "불일치 → 감각이 전혀 없는 속성을 재는 도구도 있음"], ["망원경은 맨눈으로 보기에 너무 먼 물체를 알아볼 수 있게 해 준다.", "telescopes can bring into clear view that which is too far away", "일치"], ["어떤 장치는 지각할 수 없는 신호를 관찰할 수 있는 신호로 바꾼다.", "Other instruments turn signals that we cannot perceive into ones that we can observe", "일치"], ["어떤 도구는 자외선을 눈에 보이는 이미지로 나타낸다.", "creating visible images based on the ultraviolet spectrum of light", "일치"], ["어떤 도구는 인간에게 감각 능력이 전혀 없는 속성을 측정한다.", "measure properties for which we have no sensory capacity at all", "일치"]] },
        { n: 23, q: exam(23, "글의 내용과 <u>일치하는</u> 것은?", T23), opts: ["Certain instruments transform sounds beyond the range of human hearing into audible signals.", "Humans began relying on such tools only in recent decades.", "Scientific tools have rendered human senses obsolete.", "Telescopes function by diminishing the intensity of distant light.", "No tool can detect phenomena outside the scope of human perception."], ex: "정답: transform = change · beyond : ~의 범위를 넘어서 (= outside the range of)\n· rely on : ~에 의존하다 · decade : 10년 → 실제로는 수 세기(many centuries) 동안\n· obsolete : 쓸모없게 된\n· diminish : 줄이다 (↔ amplify) · intensity : 강도\n· scope : 범위 → 그런 현상을 감지하는 도구가 바로 글의 주제", per: [["어떤 도구는 사람이 들을 수 있는 범위를 넘는 소리를 들리는 신호로 바꾼다.", "changing sounds that are normally outside the range of what human ears can hear into audible signals", "일치"], ["인간은 최근 수십 년 사이에야 이런 도구에 의존하기 시작했다.", "For many centuries", "불일치 → 수 세기 동안 써 왔음"], ["과학 도구가 인간의 감각을 쓸모없게 만들었다.", "expanding the reach of our current senses", "불일치 → 감각을 대체한 게 아니라 넓혀 줌"], ["망원경은 먼 빛의 세기를 줄여서 작동한다.", "simply amplifying signals", "불일치 → 신호를 확장함"], ["어떤 도구도 인간의 지각 범위 밖의 현상을 감지할 수 없다.", "natural phenomena that we can't perceive with our senses", "불일치 → 바로 그런 현상을 지각하게 하는 게 도구"]] },
        { n: 24, q: exam(24, "글의 내용과 일치하지 <u>않는</u> 것은?", T24), opts: ["Opponents endorse the inference that correlation proves causation.", "Defenders contend that animal testing brought about medical progress.", "Legislation mandates that new drugs be tested on animals prior to human use.", "The correlation stems from legal requirements rather than genuine causation.", "Some prominent physicians cite historical evidence to challenge the defenders."], ex: "정답: endorse : 지지하다 → 실제로는 거부함(reject) · causation : 인과관계\n· contend = claim · bring about = cause · progress = advancement\n· legislation = the law · mandate : 의무화하다 (= prescribe) · prior to = before\n· stem from : ~에서 비롯되다 (= the result of) · genuine : 진짜의\n· prominent = influential · cite : 인용하다, 제시하다 (= offer)", per: [["반대자들은 상관관계가 인과관계를 증명한다는 추론을 지지한다.", "Opponents of research reject this inference", "불일치 → 추론을 거부함"], ["옹호자들은 동물 실험이 의학 발전을 가져왔다고 주장한다.", "the former caused the latter", "일치 (the former = 동물 실험, the latter = 의학 발전)"], ["법은 신약을 사람에게 쓰기 전에 동물에게 시험하도록 의무화한다.", "the law prescribes that all new drugs", "일치"], ["그 상관관계는 진짜 인과관계가 아니라 법적 요구에서 비롯된다.", "is the result of legal necessity, not evidence", "일치"], ["몇몇 저명한 의사들은 옹호자들을 반박하는 역사적 증거를 제시한다.", "several influential physicians have offered historical evidence", "일치"]] },
        { n: 24, q: exam(24, "글의 내용과 <u>일치하는</u> 것은?", T24), opts: ["Some physicians attribute a more significant role to clinical findings than animal researchers acknowledge.", "Opponents claim modern medicine is the sole factor behind reduced mortality.", "Prosthetic devices are exempt from animal testing under the law.", "The physicians' evidence corroborates the defenders' claims.", "Opponents believe animal experimentation is legally prohibited."], ex: "정답: attribute A to B : A를 B의 덕으로 보다 · clinical findings = clinical discoveries · acknowledge : 인정하다\n· sole = only → 반대자들은 '유일한 원인이 아니다'라고 함\n· be exempt from : ~에서 면제되다 → 보철 장치도 동물 실험 대상\n· corroborate : 뒷받침하다 (↔ 실제로는 반박)\n· prohibit : 금지하다 → 실제로는 법이 동물 실험을 요구함", per: [["몇몇 의사들은 동물 연구자들이 인정하는 것보다 임상적 발견이 더 중요한 역할을 했다고 본다.", "clinical discoveries played a more substantial role than animal researchers have led us to believe", "일치"], ["반대자들은 현대 의학이 사망률 감소의 유일한 요인이라고 주장한다.", "modern medicine not the only cause for the decline in mortality", "불일치 → \"유일한 원인이 아니다\"라고 함"], ["법에 따라 보철 장치는 동물 실험에서 면제된다.", "all new drugs, prosthetic devices, and surgical techniques be tried on animals", "불일치 → 보철 장치도 동물 시험 대상"], ["의사들의 증거는 옹호자들의 주장을 뒷받침한다.", "has not been as responsible for biomedical discovery as defenders suggest", "불일치 → 오히려 반박함"], ["반대자들은 동물 실험이 법으로 금지되어 있다고 믿는다.", "the law prescribes that all new drugs", "불일치 → 법은 오히려 동물 실험을 요구함"]] }
      ]},
      { type: 'pick', title: '어법선택', guide: '어법상 알맞은 것을 고르세요.', items: [
        { s: "For many centuries, humans have taken advantage of tools {that|what} translate and bring into our perception natural phenomena that we can't perceive with our senses.", ex: '선행사 tools가 있음 → 관계대명사 that' },
        { s: 'In some cases, this consists of simply {amplifying|amplify} signals that feed into our normal sensory inputs (e.g., telescopes can bring into clear view that which is too far away for our eyes to perceive on their own).', ex: '전치사 of + 동명사' },
        { s: 'Other instruments turn signals that we cannot perceive into {ones|one} that we can observe.', ex: 'signals(복수)를 받는 대명사 → ones' },
        { s: 'Some of these take the form of expanding the reach of our current senses, such as creating visible images based on the ultraviolet spectrum of light or {changing|changes} sounds that are normally outside the range of what human ears can hear into audible signals.', ex: 'creating과 병렬 → changing' },
        { s: 'Alternatively, some instruments measure properties for {which|that} we have no sensory capacity at all and change them into that which we can observe.', ex: '전치사 + 관계대명사: for which (for that 불가)' },
        { s: 'Many opponents of animal experimentation argue that not only {is modern medicine|modern medicine is} not the only cause for the decline in mortality, many medical advances that did contribute to human health were not the result of animal experimentation.', ex: 'not only가 절 앞에 오면 도치: be동사 + 주어' },
        { s: 'After all, we have independent reasons to expect these phenomena {to be|being} correlated.', ex: 'expect + 목적어 + to부정사' },
        { s: 'Since the law prescribes that all new drugs, prosthetic devices, and surgical techniques {be|are} tried on animals before they are used in humans, we will subsequently find that all medical advances are correlated with prior experimentation on animals.', ex: '규정·요구 동사(prescribe) + that + 주어 + (should) 동사원형' },
        { s: 'Moreover, several influential physicians have offered historical evidence that animal experimentation has not been as responsible for biomedical discovery {as|than} defenders suggest.', ex: 'as + 원급 + as' },
        { s: 'They claim that clinical discoveries played a more substantial role {than|as} animal researchers have led us to believe.', ex: '비교급 more + than' }
      ]},
      { type: 'verb', title: '동사변형', guide: '( ) 안의 동사를 알맞은 형태로 바꿔 쓰세요.', items: [
        { s: "For many centuries, humans ___ advantage of tools that translate and bring into our perception natural phenomena that we can't perceive with our senses.", v: 'take', a: ['have taken'], ex: 'for many centuries(기간) → 현재완료' },
        { s: 'In some cases, this consists of simply ___ signals that feed into our normal sensory inputs (e.g., telescopes can bring into clear view that which is too far away for our eyes to perceive on their own).', v: 'amplify', a: ['amplifying'], ex: '전치사 of + 동명사' },
        { s: 'Some of these take the form of expanding the reach of our current senses, such as ___ visible images based on the ultraviolet spectrum of light or changing sounds that are normally outside the range of what human ears can hear into audible signals.', v: 'create', a: ['creating'], ex: 'such as + 동명사, changing과 병렬' },
        { s: 'Defenders of research ___ that since there is a strong correlation between the practice of animal experimentation and medical advancement, the former caused the latter.', v: 'claim', a: ['have claimed'], ex: '현재완료 have + p.p.' },
        { s: 'After all, we have independent reasons ___ these phenomena to be correlated.', v: 'expect', a: ['to expect'], ex: 'reasons를 꾸미는 to부정사' },
        { s: 'Since the law prescribes that all new drugs, prosthetic devices, and surgical techniques ___ tried on animals before they are used in humans, we will subsequently find that all medical advances are correlated with prior experimentation on animals.', v: 'be', a: ['be', 'should be'], ex: 'prescribe that + 주어 + (should) 동사원형' },
        { s: 'Since the law prescribes that all new drugs, prosthetic devices, and surgical techniques be tried on animals before they ___ in humans, we will subsequently find that all medical advances are correlated with prior experimentation on animals.', v: 'use', a: ['are used'], ex: '약·장치가 "사용되는" 수동태' },
        { s: 'Consequently, the correlation between animal experimentation and medical discovery is the result of legal necessity, not evidence that animal experimentation ___ to medical advances.', v: 'lead', a: ['led'], ex: 'lead - led - led (과거)' },
        { s: 'Moreover, several influential physicians ___ historical evidence that animal experimentation has not been as responsible for biomedical discovery as defenders suggest.', v: 'offer', a: ['have offered'], ex: '현재완료' },
        { s: 'They claim that clinical discoveries played a more substantial role than animal researchers have ___ us to believe.', v: 'lead', a: ['led'], ex: 'have + p.p. / lead + 목적어 + to부정사' }
      ]},
      { type: 'error', title: '오류찾기', guide: '어법상 틀린 곳을 고르세요.', items: [
        { s: 'Other instruments [[turn]] signals that we cannot [[perceive]] into [[one]] that we can [[observe]].', w: 2, fix: 'ones', ex: 'signals(복수) → ones' },
        { s: 'Alternatively, some instruments measure properties for [[that]] we have no sensory capacity at all and [[change]] them into that [[which]] we can observe.', w: 0, fix: 'which', ex: '전치사 뒤에는 that을 쓸 수 없다 → for which' },
        { s: 'Many opponents of animal experimentation [[argue]] that not only [[modern medicine is]] not the only cause for the decline in mortality, many medical advances that did [[contribute]] to human health [[were]] not the result of animal experimentation.', w: 1, fix: 'is modern medicine', ex: 'not only 도치: is + 주어' },
        { s: 'Opponents of research [[reject]] this inference. After all, we have independent reasons [[to expect]] these phenomena [[being]] correlated.', w: 2, fix: 'to be', ex: 'expect + 목적어 + to부정사' },
        { s: 'Since the law prescribes that all new drugs, prosthetic devices, and surgical techniques [[be]] tried on animals before they [[use]] in humans, we will [[subsequently]] find that all medical advances [[are]] correlated with prior experimentation on animals.', w: 1, fix: 'are used', ex: '사용"되는" 것 → 수동태 are used' },
        { s: 'Moreover, several influential physicians [[have offered]] historical evidence that animal experimentation has not been as [[responsible]] for biomedical discovery [[than]] defenders suggest.', w: 2, fix: 'as', ex: 'as + 원급 + as' },
        { s: 'In some cases, this consists of simply [[amplify]] signals that [[feed]] into our normal sensory inputs (e.g., telescopes can bring into clear view that [[which]] is too far away for our eyes to perceive on their own).', w: 0, fix: 'amplifying', ex: '전치사 of + 동명사' }
      ]},
      { type: 'scramble', title: '본문 스크램블', guide: '우리말에 맞게 단어를 눌러 문장을 완성하세요.', items: [
        { ko: '다른 도구들은 우리가 지각할 수 없는 신호를 우리가 관찰할 수 있는 신호로 바꾼다.', en: 'Other instruments turn signals that we cannot perceive into ones that we can observe.' },
        { ko: '연구 반대자들은 이 추론을 거부한다.', en: 'Opponents of research reject this inference.' },
        { ko: '결국, 우리에게는 이 현상들이 상관관계가 있을 것이라고 예상할 별개의 이유가 있다.', en: 'After all, we have independent reasons to expect these phenomena to be correlated.' },
        { ko: '그들은 임상적 발견이 동물 연구자들이 우리에게 믿게 해 온 것보다 더 상당한 역할을 했다고 주장한다.', en: 'They claim that clinical discoveries played a more substantial role than animal researchers have led us to believe.' },
        { ko: '또는, 어떤 도구들은 우리가 감지할 능력이 전혀 없는 속성을 측정하여 그것을 우리가 관찰할 수 있는 것으로 바꾼다.', en: 'Alternatively, some instruments measure properties for which we have no sensory capacity at all and change them into that which we can observe.' }
      ]},
      { type: 'order', title: '문장순서', guide: '문장을 본문 순서대로 눌러서 배열하세요.', items: [
        { lines: [T23[0][0], T23[1][0], T23[2][0], T23[3][0], T23[4][0]], flow: ["인간은 감각으로 못 느끼는 현상을 도구로 지각해 옴", "① 감각 신호를 확장하는 도구 (예: 망원경)", "② 지각 못 하는 신호를 관찰 가능한 신호로 바꾸는 도구", "그 예: 자외선 이미지, 가청 범위 밖 소리 변환", "③ 감각이 아예 없는 속성을 측정해 바꾸는 도구"] },
        { lines: [T24[0][0], T24[1][0], T24[2][0], T24[3][0]], flow: ["반대자: 의학 발전은 동물 실험의 결과가 아니었다", "옹호자: 상관관계가 있으니 동물 실험이 발전을 일으켰다", "반대자는 이 추론을 거부함", "상관관계가 생길 별개의 이유가 있음"] },
        { lines: [T24[3][0], T24[4][0], T24[5][0]], flow: ["상관관계가 생길 별개의 이유가 있음", "법이 모든 신약 등을 먼저 동물에게 시험하게 함", "따라서 상관관계는 법적 필요성의 결과일 뿐"] },
        { lines: [T24[4][0], T24[5][0], T24[6][0], T24[7][0]], flow: ["법이 동물 시험을 의무화함", "상관관계는 법적 필요성의 결과", "게다가 의사들이 역사적 반대 증거를 제시함", "임상적 발견이 더 큰 역할을 했다고 주장함"] }
      ]},
      { type: 'insert', title: '문장삽입', guide: '주어진 문장이 들어가기에 가장 알맞은 곳을 고르세요.', items: [
        { lines: [T23[0][0], T23[1][0], T23[2][0], T23[3][0]], given: 1, flow: ["인간은 도구로 못 느끼는 현상을 지각해 옴", "어떤 경우엔 이것이 신호를 단순히 확장하는 것 (망원경)", "다른 도구는 지각 못 하는 신호를 바꿈", "그중 일부는 감각 범위를 넓힘"], ex: 'this = 감각으로 지각할 수 없는 것을 도구로 지각하게 하는 일' },
        { lines: [T23[1][0], T23[2][0], T23[3][0], T23[4][0]], given: 2, flow: ["신호를 확장하는 도구", "지각 못 하는 신호를 바꾸는 도구", "이것들 중 일부는 감각 범위를 넓히는 형태", "또는 감각이 전혀 없는 속성을 측정"], ex: 'Some of these = 앞의 Other instruments 중 일부' },
        { lines: [T24[1][0], T24[2][0], T24[3][0], T24[4][0]], given: 1, flow: ["옹호자: 동물 실험이 발전을 일으켰다", "반대자는 이 추론을 거부함", "상관관계가 생길 별개의 이유가 있음", "법이 동물 시험을 의무화함"], ex: 'this inference = "전자가 후자를 일으켰다"는 옹호자의 추론' },
        { lines: [T24[4][0], T24[5][0], T24[6][0], T24[7][0]], given: 2, flow: ["법이 동물 시험을 의무화함", "상관관계는 법적 필요성의 결과", "게다가 의사들이 역사적 반대 증거를 제시함", "그들은 임상적 발견이 더 중요했다고 주장함"], ex: 'Moreover로 추가 근거(의사들의 역사적 증거) 제시, They = 그 의사들' }
      ]},
      { type: 'odd', title: '어색한 문장', guide: '글의 흐름과 관계없는 문장을 고르세요.', items: [
        { lines: [T23[2][0], T23[3][0], 'Most scientists believe our senses can perceive everything in nature.', T23[4][0]], odd: 2, ex: '감각으로 지각할 수 없는 것이 있다는 전제와 반대된다.' },
        { lines: [T24[1][0], 'Animal experimentation is the only reason that people live longer today.', T24[2][0], T24[3][0]], odd: 1, ex: '반대자들의 반박 흐름과 맞지 않는다.' },
        { lines: [T24[5][0], T24[6][0], T24[7][0], 'Therefore, all animal experiments should be required by law.'], odd: 3, ex: '동물 실험의 기여를 의심하는 결론과 반대된다.' }
      ]},
      { type: 'blank', title: '빈칸추론', guide: '빈칸에 들어갈 말로 가장 알맞은 것을 고르세요.', items: [
        { s: 'Other instruments turn signals that we cannot perceive into ones that we ____.', opts: ["can observe", "cannot perceive", "can amplify", "already sense"], ex: '지각 못 하는 신호 → 관찰할 수 있는 신호' },
        { s: 'In some cases, this consists of simply ____ that feed into our normal sensory inputs (e.g., telescopes can bring into clear view that which is too far away for our eyes to perceive on their own).', opts: ["amplifying signals", "replacing signals", "blocking signals", "measuring properties"], ex: '망원경 = 신호 확장' },
        { s: 'Consequently, the correlation between animal experimentation and medical discovery is the result of ____, not evidence that animal experimentation led to medical advances.', opts: ["legal necessity", "scientific evidence", "clinical discovery", "animal experimentation"], ex: '법이 동물 실험을 요구해서 생긴 상관관계' },
        { s: 'They claim that ____ played a more substantial role than animal researchers have led us to believe.', opts: ["clinical discoveries", "animal experiments", "legal requirements", "medical advances"], ex: '임상적 발견이 더 큰 역할' }
      ]},
      { type: 'mc', title: '핵심문법', guide: '알맞은 답을 고르세요.', items: [
        { n: 23, q: '빈칸에 알맞은 것은?<br><b>Some instruments measure properties for ______ we have no sensory capacity.</b>', opts: ['which', 'that', 'what', 'whom'], ex: '전치사 + which (사물 선행사, that 불가)' },
        { n: 24, q: 'not only 도치가 바르게 된 것은?', opts: ['Not only is modern medicine not the only cause, ...', 'Not only modern medicine is not the only cause, ...', 'Not only does modern medicine is not the only cause, ...', 'Not only modern medicine are not the only cause, ...'], ex: 'Not only + be동사 + 주어' },
        { n: 24, q: '빈칸에 알맞은 것은?<br><b>The law prescribes that all new drugs ______ tried on animals.</b>', opts: ['be', 'are', 'were', 'been'], ex: '규정·요구 동사 + that + 주어 + (should) 동사원형' },
        { n: 24, q: '밑줄 친 <u>the former</u>가 가리키는 것은?<br><b>There is a strong correlation between animal experimentation and medical advancement, so <u>the former</u> caused the latter.</b>', opts: ['animal experimentation', 'medical advancement', 'a strong correlation', 'defenders of research'], ex: 'the former = 앞의 것(동물 실험), the latter = 뒤의 것(의학 발전)' },
        { n: 24, q: '빈칸에 알맞은 것은?<br><b>Animal experimentation has not been as responsible ______ defenders suggest.</b>', opts: ['as', 'than', 'so', 'that'], ex: 'as + 원급 + as' },
        { n: 23, q: '밑줄 친 <u>ones</u>가 가리키는 것은?<br><b>Other instruments turn signals that we cannot perceive into <u>ones</u> that we can observe.</b>', opts: ['signals', 'instruments', 'senses', 'tools'], ex: 'ones = signals' },
        { n: 24, q: '빈칸에 알맞은 것은?<br><b>Animal researchers have led us ______ that.</b>', opts: ['to believe', 'believe', 'believing', 'believed'], ex: 'lead + 목적어 + to부정사' }
      ]}
    ]
  }
  ]
};
})();
