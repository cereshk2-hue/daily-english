/* 중1 동아(윤정미) Lesson 5~7 (시험 범위 5·6·7과, 8과 제외 10/28). 순서: 6과 → 7과(대화문·본문) → 5과(대화문·본문)
   6·7과 본문: 예전 파일(id d1~d4 유지) · 7과·5과 대화문, 5과 본문: scratchpad/gen_m1d5.py · skip d1,d2 = 6과 본문은 이미 함(건너뜀 표시)
   prose: true → 본문을 설명문으로 표시(대화문은 화자 표시) */
window.PKG = {
  id: 'm1-donga-yoon-L6',
  school: '중1 동아(윤정미)',
  unit: 'Lesson 5~7',
  title: 'Zero-Waste Challenge · Let’s Make a Movie! · Who Threw a Cake at the Monalisa?',
  titleKo: '제로 웨이스트 챌린지 · 영화 만들기 · 모나리자 케이크 사건',
  exam: '2학기 기말고사',
  prose: true,
  stepsBefore: ['핵심어휘·숙어', '어휘선택', 'T/F 내용 확인', '어법선택', '동사변형', '오류찾기', '본문 스크램블', '문장순서', '문장삽입', '어색한 문장', '빈칸추론', '핵심문법'],
  teacherPhone: '',
  pick: true,
  skip: ['d1', 'd2'],
  days: [
  { id: 'c6a', name: 'DAY 1', range: '6과 대화문 ① 대화 1~4', story: 'Lesson 6 · 도움 요청하고 답하기 · 거절의 이유 말하기 · 대화 1~4', passage: [['#', '6과 대화 1 · 문 닫기 (Watch and Choose)', ''], ['W', 'Excuse me, but can you please close the door? The air conditioner is on.', '실례지만, 문을 닫아 주시겠어요? 에어컨이 켜져 있어서요.'], ['B', 'Oh, I didn\'t know that. I\'ll close it right away.', '아, 몰랐네요. 즉시 닫을게요.'], ['W', 'Thanks.', '감사합니다.'], ['#', '6과 대화 2 · 카페에서 (Watch and Choose)', ''], ['M', 'For here or to go?', '여기에서 드실 건가요, 아니면 가져가실 건가요?'], ['G', 'For here, please. And can you please put my smoothie in a plastic cup, not in a glass?', '여기서 먹고 갈게요. 그리고 제 스무디를 유리잔 말고 플라스틱 컵에 담아 주시겠어요?'], ['M', 'I\'m sorry, but we don\'t use single-use plastic cups inside the café.', '죄송하지만, 카페 안에서는 일회용 플라스틱 컵을 사용하지 않아요.'], ['G', 'Oh, I see.', '아, 그렇군요.'], ['#', '6과 대화 3 · 물 잠그기 (Watch and Choose)', ''], ['W', 'Look. Somebody forgot to turn off the water.', '봐. 누군가 물을 잠그는 걸 깜빡했네.'], ['B', 'Again? People are so forgetful.', '또요? 사람들은 너무 잘 잊어요.'], ['W', 'I know. Can you run over there and turn off the water?', '그러게. 저기로 뛰어가서 물을 잠가 주겠니?'], ['B', 'Sure. No problem.', '물론이죠. 문제없어요.'], ['#', '6과 대화 4 · 상자 옮기기 (Watch and Choose)', ''], ['M', 'Can you please carry this box to my car?', '이 상자를 내 차로 옮겨 줄래?'], ['G', 'I\'m really sorry, Dad, but I\'m late for my class.', '정말 죄송해요, 아빠, 그런데 제가 수업에 늦었어요.'], ['M', 'Oh, I see. I\'ll ask somebody else.', '아, 그렇구나. 다른 사람에게 부탁할게.']], steps: [
    { type: 'vocab', title: '핵심어휘·숙어', quizN: 15, items: [['Can you please ~?', '~해 주시겠어요? (도움 요청)'], ['close', '닫다'], ['air conditioner', '에어컨'], ['be on', '켜져 있다'], ['right away', '즉시, 바로'], ['For here or to go?', '여기서 드세요, 가져가세요?'], ['plastic cup', '플라스틱 컵'], ['glass', '유리잔'], ['single-use', '일회용의'], ['inside', '~ 안에서'], ['forget to', '~할 것을 잊다 (forget - forgot - forgotten)'], ['turn off', '(물·전기를) 잠그다, 끄다'], ['forgetful', '잘 잊어버리는'], ['No problem.', '문제없어요.'], ['carry', '옮기다, 나르다'], ['be late for', '~에 늦다'], ['somebody else', '다른 누군가']] },
    { type: 'pick', title: '어휘선택', guide: '문맥에 맞는 낱말을 고르세요.', items: [
      { s: 'Excuse me, but can you please close the door? The air conditioner is {on|off}.', ex: '정답 ▶ on (켜져 있는)\n오답 ▶ off (꺼져 있는): 에어컨이 \'켜져 있어서\' 찬 바람이 나가지 않게 문을 닫아 달라고 해요.' },
      { s: 'Look. Somebody forgot to turn {off|on} the water.', ex: '정답 ▶ off\n오답 ▶ on: 누군가 물을 \'잠그는(turn off)\' 것을 깜빡해서 물이 계속 나오고 있어요.' },
      { s: 'Again? People are so {forgetful|careful}.', ex: '정답 ▶ forgetful (잘 잊어버리는)\n오답 ▶ careful (조심성 있는): 물 잠그는 걸 또(Again?) 잊었으니 \'잘 잊어버린다\'' }
    ] },
    { type: 'tf', title: 'T/F 내용 확인', guide: '본문 내용과 일치하면 T, 다르면 F를 고르세요.', items: [['The woman asks the boy to open the door.', false, '정답 ▶ F\n이유: 문을 여는 게 아니라 닫아(close the door) 달라고 했어요.', null, 'can you please close the door'], ['The girl will eat at the café.', true, '정답 ▶ T\n이유: For here, please. → 가게 안에서 먹고 가요.', null, 'For here, please'], ['The café uses single-use plastic cups inside.', false, '정답 ▶ F\n이유: 카페 안에서는 일회용 플라스틱 컵을 쓰지 않아요(don\'t use).', null, 'we don\'t use single-use plastic cups inside the café'], ['The boy will turn off the water.', true, '정답 ▶ T\n이유: 물을 잠가 달라는 부탁에 Sure. No problem.이라고 했어요.', null, 'Can you run over there and turn off the water'], ['The girl will carry the box for her dad.', false, '정답 ▶ F\n이유: 수업에 늦어서 거절했고, 아빠는 다른 사람에게 부탁할 거예요.', null, 'I\'m late for my class']] },
    { type: 'mc', title: '알맞은 응답 고르기', guide: '대화의 흐름에 맞는 응답을 고르세요.', items: [
      { q: '다음 말에 이어질 응답으로 가장 알맞은 것은?<br><b>A: Can you please close the door?</b>', opts: ['Sure. No problem.', 'For here, please.', 'You\'re welcome.', 'Yes, I did.'], ex: '정답 ▶ Sure. No problem.\n이유: 도움 요청(Can you please ~?)을 들어줄 때 → Sure. No problem. / 거절할 때 → I\'m sorry, but I can\'t.' },
      { q: '다음 말에 이어질 응답으로 가장 알맞은 것은?<br><b>A: For here or to go?</b>', opts: ['For here, please.', 'Sure. No problem.', 'I\'ll ask somebody else.', 'Thanks.'], ex: '정답 ▶ For here, please.\n이유: \'여기서 드세요, 가져가세요?\' → For here.(여기서요) / To go.(가져갈게요)' }
    ] },
    { type: 'mc', title: '일치·불일치', guide: '선택지는 본문을 어려운 어휘로 바꿔 쓴 문장이에요. 풀고 나서 해설의 어휘를 꼭 확인하세요.', items: [
      { box: ['6과 대화 1 · 문 닫기 (Watch and Choose)', '6과 대화 2 · 카페에서 (Watch and Choose)', '6과 대화 3 · 물 잠그기 (Watch and Choose)', '6과 대화 4 · 상자 옮기기 (Watch and Choose)'], q: '대화의 내용과 일치하지 <u>않는</u> 것은?', opts: ['The girl helps her dad carry the box.', 'The air conditioner is on.', 'The girl wants her smoothie in a plastic cup.', 'Somebody forgot to turn off the water.', 'The boy thinks people are forgetful.'], ex: '정답 ▶ The girl helps her dad carry the box.\n이유: 소녀는 수업에 늦어서 도와드릴 수 없다고 했어요(I\'m really sorry, Dad, but ~).', per: [['소녀는 아빠가 상자 옮기는 것을 돕는다.', 'I\'m late for my class', '불일치 → 거절함'], ['에어컨이 켜져 있다.', 'The air conditioner is on', '일치'], ['소녀는 스무디를 플라스틱 컵에 담기를 원한다.', 'can you please put my smoothie in a plastic cup', '일치'], ['누군가 물 잠그는 것을 잊었다.', 'Somebody forgot to turn off the water', '일치'], ['소년은 사람들이 잘 잊어버린다고 생각한다.', 'People are so forgetful', '일치']] }
    ] },
    { type: 'pick', title: '어법선택', guide: '어법상 알맞은 것을 고르세요.', items: [
      { s: 'Look. Somebody forgot {to turn|turning} off the water.', ex: '정답 ▶ to turn\n이유: forget to + 동사원형 = (앞으로) ~할 것을 잊다. 물을 잠가야 하는데 잊어버렸어요.' },
      { s: 'Oh, I didn\'t know that. I\'ll close {it|them} right away.', ex: '정답 ▶ it\n이유: 가리키는 것은 the door(단수) → it' },
      { s: 'I know. Can you run over there and {turn|turned} off the water?', ex: '정답 ▶ turn\n이유: Can you + 동사원형 ~? run과 turn이 and로 나란히 연결돼요.' },
      { s: 'I\'m really sorry, Dad, but I\'m late {for|of} my class.', ex: '정답 ▶ for\n이유: be late for ~ = ~에 늦다 (짝꿍 전치사 for)' }
    ] },
    { type: 'scramble', title: '본문 스크램블', guide: '우리말에 맞게 단어를 눌러 문장을 완성하세요.', items: [
      { ko: '이 상자를 내 차로 옮겨 줄래?', en: 'Can you please carry this box to my car?' },
      { ko: '죄송하지만, 카페 안에서는 일회용 플라스틱 컵을 사용하지 않아요.', en: 'I\'m sorry, but we don\'t use single-use plastic cups inside the café.' }
    ] },
    { type: 'order', title: '문장순서', guide: '대화(문장)를 순서대로 눌러서 배열하세요.', items: [
      { lines: ['Look. Somebody forgot to turn off the water.', 'Again? People are so forgetful.', 'I know. Can you run over there and turn off the water?', 'Sure. No problem.'], flow: ['W: 누군가 물 잠그는 걸 잊었네', 'B: 또요? 사람들은 너무 잘 잊어요', 'W: 뛰어가서 물 좀 잠가 줄래?', 'B: 물론이죠'] }
    ] },
    { type: 'blank', title: '빈칸추론', guide: '빈칸에 들어갈 말로 가장 알맞은 것을 고르세요.', items: [
      { s: 'Excuse me, but can you please close the door? The air conditioner is ____.', opts: ['on', 'off', 'small', 'cheap'], ex: '정답 ▶ on\n이유: 에어컨이 \'켜져 있어서\' 문을 닫아 달라는 거예요. 꺼져 있으면(off) 닫을 이유가 없어요.' },
      { s: 'I\'m really sorry, Dad, but I\'m ____ for my class.', opts: ['late', 'early', 'ready', 'happy'], ex: '정답 ▶ late\n이유: 부탁을 거절하는 이유 → 수업에 \'늦었다(late)\'' }
    ] },
    { type: 'mc', title: '어색한 대화 고르기', guide: '짝지어진 대화 중 어색한 것을 고르세요.', items: [
      { q: '다음 중 짝지어진 대화가 <b>어색한</b> 것은?', opts: ['A: Can you please close the window? B: Yes, I did.', 'A: Can you please help me? B: Sure. No problem.', 'A: Can you carry this box? B: I\'m sorry, but I can\'t. I\'m busy now.', 'A: For here or to go? B: To go, please.'], ex: '정답 ▶ A: Can you please close the window? B: Yes, I did.\n이유: 도움 요청에는 Sure. No problem. / I\'m sorry, but I can\'t.로 답해요. Yes, I did.는 Did you ~?의 대답이에요.' }
    ] },
    { type: 'mc', title: '의사소통 기능', guide: '상황에 맞는 표현을 고르세요.', items: [
      { q: '도움을 요청하는 표현이 <b>아닌</b> 것은?', opts: ['I\'m sorry, but I can\'t.', 'Can you please close the door?', 'Can you do me a favor?', 'I need a favor.'], ex: '정답 ▶ I\'m sorry, but I can\'t.\n이유: 요청을 \'거절\'하는 말이에요. 나머지는 모두 도움을 요청하는 표현이에요.' },
      { q: '요청을 거절하며 이유를 말하는 것은?', opts: ['I\'m sorry, but I can\'t. I\'m busy now.', 'Sure. No problem.', 'Of course, I can.', 'I\'ll close it right away.'], ex: '정답 ▶ I\'m sorry, but I can\'t. I\'m busy now.\n이유: 거절(I\'m sorry, but I can\'t.) + 이유(I\'m busy now.)\n오답 ▶ 나머지는 모두 들어주는 말' }
    ] },
    { type: 'mc', title: '요약문 완성', guide: '본문을 읽고 요약문의 빈칸 (A), (B)에 들어갈 말을 고르세요.', items: [
      { n: null, box: ['6과 대화 1 · 문 닫기 (Watch and Choose)', '6과 대화 2 · 카페에서 (Watch and Choose)'], q: '다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 알맞은 것은?<br><b>The woman asked the boy to (A) ______ the door, and the café doesn\'t use single-use plastic (B) ______ inside.</b>', opts: ['(A) close – (B) cups', '(A) open – (B) cups', '(A) close – (B) bags', '(A) paint – (B) straws', '(A) open – (B) glasses'], ex: '정답 ▶ (A) close – (B) cups\n(A) 문을 \'닫아\' 달라 → close\n(B) 일회용 플라스틱 \'컵\'을 쓰지 않는다 → cups', ev: ['can you please close the door', 'we don\'t use single-use plastic cups inside the café'] },
      { n: null, box: ['6과 대화 3 · 물 잠그기 (Watch and Choose)', '6과 대화 4 · 상자 옮기기 (Watch and Choose)'], q: '다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 알맞은 것은?<br><b>The boy agreed to turn off the water, but the girl couldn\'t carry the box because she was (A) ______ for her class, so her dad will ask somebody (B) ______.</b>', opts: ['(A) late – (B) else', '(A) early – (B) else', '(A) late – (B) first', '(A) ready – (B) again', '(A) busy – (B) never'], ex: '정답 ▶ (A) late – (B) else\n(A) 수업에 \'늦어서\' 거절 → late\n(B) \'다른\' 사람에게 부탁하겠다 → somebody else', ev: ['I\'m late for my class', 'I\'ll ask somebody else'] }
    ] }
  ] },
  { id: 'c6b', name: 'DAY 2', range: '6과 대화문 ② 대화 5', story: 'Lesson 6 · 플로깅 (Watch, Answer, and Talk)', passage: [['#', '6과 대화 5 · 플로깅 (Watch, Answer, and Talk)', ''], ['Alex', 'Hi, Yuna. What are you doing here?', '안녕, 유나야. 여기에서 뭐 하고 있니?'], ['Yuna', 'Hi, Alex. I\'m plogging with my club members.', '안녕, Alex. 동아리 회원들과 플로깅을 하고 있어.'], ['Alex', 'Excuse me?', '뭐라고?'], ['Yuna', 'Plogging. It means jogging and picking up trash at the same time.', '플로깅. 조깅과 쓰레기 줍기를 동시에 한다는 뜻이야.'], ['Alex', 'Sounds cool! So you\'re a member of a plogging club.', '멋지다! 그럼 너는 플로깅 동아리의 회원이구나.'], ['Yuna', 'Yes. We plog together every Saturday morning from 10 to 12. Interested?', '응. 우리는 매주 토요일 아침 10시부터 12시까지 함께 플로깅을 해. 관심 있니?'], ['Alex', 'Well, I\'ll think about it.', '음, 생각해 볼게.'], ['Yuna', 'OK. By the way, can you please help me with this trash bag? It\'s heavy.', '알겠어. 그런데, 이 쓰레기봉투 드는 것 좀 도와줄래? 무거워.'], ['Alex', 'Sure. No problem.', '물론이지. 문제없어.']], steps: [
    { type: 'vocab', title: '핵심어휘·숙어', quizN: 15, items: [['club member', '동아리 회원'], ['plog', '플로깅하다 (조깅하며 쓰레기 줍기)'], ['Excuse me?', '뭐라고? (되묻기)'], ['mean', '의미하다'], ['jog', '조깅하다'], ['pick up', '줍다'], ['trash', '쓰레기'], ['at the same time', '동시에'], ['Sounds cool!', '멋지다!'], ['every Saturday', '매주 토요일'], ['Interested?', '관심 있니?'], ['think about', '~에 대해 생각하다'], ['by the way', '그런데 (화제 바꾸기)'], ['help A with B', 'A가 B 하는 것을 돕다'], ['trash bag', '쓰레기봉투'], ['heavy', '무거운']] },
    { type: 'pick', title: '어휘선택', guide: '문맥에 맞는 낱말을 고르세요.', items: [
      { s: 'Plogging. It means jogging and picking up {trash|flowers} at the same time.', ex: '정답 ▶ trash (쓰레기)\n오답 ▶ flowers: 플로깅 = 조깅 + \'쓰레기\' 줍기. 나중에 쓰레기봉투도 나와요.' },
      { s: 'OK. By the way, can you please help me with this trash bag? It\'s {heavy|light}.', ex: '정답 ▶ heavy (무거운)\n오답 ▶ light (가벼운): 도와 달라고 하는 이유 → 봉투가 \'무거워서\'' },
      { s: 'Well, I\'ll {think|forget} about it.', ex: '정답 ▶ think\n오답 ▶ forget: 관심 있냐는 말에 바로 답하지 않고 \'생각해 볼게\'라고 해요.' }
    ] },
    { type: 'tf', title: 'T/F 내용 확인', guide: '본문 내용과 일치하면 T, 다르면 F를 고르세요.', items: [['Yuna is plogging alone.', false, '정답 ▶ F\n이유: 혼자가 아니라 동아리 회원들(my club members)과 하고 있어요.', null, 'I\'m plogging with my club members'], ['Plogging means jogging and picking up trash at the same time.', true, '정답 ▶ T\n이유: It means jogging and picking up trash at the same time.', null, 'It means jogging and picking up trash at the same time'], ['Yuna\'s club plogs every Sunday.', false, '정답 ▶ F\n이유: 일요일이 아니라 매주 토요일(every Saturday) 아침이에요.', null, 'We plog together every Saturday morning from 10 to 12'], ['Alex joins the club right away.', false, '정답 ▶ F\n이유: 바로 가입하지 않고 생각해 보겠다(I\'ll think about it)고 했어요.', null, 'Well, I\'ll think about it'], ['Alex will help Yuna with the trash bag.', true, '정답 ▶ T\n이유: Sure. No problem.', null, 'can you please help me with this trash bag']] },
    { type: 'mc', title: '알맞은 응답 고르기', guide: '대화의 흐름에 맞는 응답을 고르세요.', items: [
      { q: '다음 말에 이어질 응답으로 가장 알맞은 것은?<br><b>A: Can you please help me with this trash bag? It\'s heavy.</b>', opts: ['Sure. No problem.', 'Excuse me?', 'Sounds cool!', 'For here, please.'], ex: '정답 ▶ Sure. No problem.\n이유: 도움 요청을 들어주는 말 → Sure. No problem.' },
      { q: '다음 말에 이어질 응답으로 가장 알맞은 것은?<br><b>A: We plog every Saturday. Interested?</b>', opts: ['Well, I\'ll think about it.', 'For here, please.', 'It\'s heavy.', 'I\'m sorry to hear that.'], ex: '정답 ▶ Well, I\'ll think about it.\n이유: 관심 있냐는 제안에 바로 답하지 않을 때 → I\'ll think about it.(생각해 볼게)' }
    ] },
    { type: 'mc', title: '일치·불일치', guide: '선택지는 본문을 어려운 어휘로 바꿔 쓴 문장이에요. 풀고 나서 해설의 어휘를 꼭 확인하세요.', items: [
      { box: ['6과 대화 5 · 플로깅 (Watch, Answer, and Talk)'], q: '대화의 내용과 일치하지 <u>않는</u> 것은?', opts: ['Alex is already a member of the plogging club.', 'Yuna is plogging with her club members.', 'Plogging is jogging and picking up trash.', 'The club plogs from 10 to 12.', 'The trash bag is heavy.'], ex: '정답 ▶ Alex is already a member of the plogging club.\n이유: 동아리 회원은 유나예요. Alex는 생각해 보겠다고만 했어요.', per: [['Alex는 이미 플로깅 동아리 회원이다.', ['So you\'re a member of a plogging club', 'I\'ll think about it'], '불일치 → 회원은 유나'], ['유나는 동아리 회원들과 플로깅을 하고 있다.', 'I\'m plogging with my club members', '일치'], ['플로깅은 조깅하면서 쓰레기를 줍는 것이다.', 'It means jogging and picking up trash at the same time', '일치'], ['동아리는 10시부터 12시까지 플로깅을 한다.', 'from 10 to 12', '일치'], ['쓰레기봉투는 무겁다.', 'It\'s heavy', '일치']] },
      { box: ['6과 대화 5 · 플로깅 (Watch, Answer, and Talk)'], q: 'Alex가 대화 직후에 유나를 위해 할 일로 알맞은 것은?', opts: ['쓰레기봉투 드는 것 도와주기', '플로깅 동아리에 가입하기', '함께 조깅하기', '포스터 만들기', '물 잠그기'], ex: '정답 ▶ 쓰레기봉투 드는 것 도와주기\n이유: can you please help me with this trash bag? → Sure. No problem.\n오답 ▶ 동아리 가입은 \'생각해 볼게\'라고만 했어요.', per: [['', 'can you please help me with this trash bag', '정답'], ['', 'I\'ll think about it', '✘ 아직 생각 중'], ['', '', '✘'], ['', '', '✘'], ['', '', '✘']] }
    ] },
    { type: 'pick', title: '어법선택', guide: '어법상 알맞은 것을 고르세요.', items: [
      { s: 'Plogging. It means {jogging|jog} and picking up trash at the same time.', ex: '정답 ▶ jogging\n이유: means의 목적어 자리 → 동명사(-ing). jogging과 picking up이 and로 나란히 연결돼요.' },
      { s: 'Yes. We plog together every {Saturday|Saturdays} morning from 10 to 12. Interested?', ex: '정답 ▶ Saturday\n이유: every + 단수 명사 (매주 토요일 = every Saturday = on Saturdays)' },
      { s: 'OK. By the way, can you please help me with this trash bag? It\'s {heavy|heavily}.', ex: '정답 ▶ heavy\n이유: be동사 뒤에서 주어를 설명 → 형용사 heavy. heavily는 부사예요.' },
      { s: 'OK. By the way, can you please {help|helping} me with this trash bag? It\'s heavy.', ex: '정답 ▶ help\n이유: Can you (please) + 동사원형 ~? = ~해 주겠니? (도움 요청)' }
    ] },
    { type: 'scramble', title: '본문 스크램블', guide: '우리말에 맞게 단어를 눌러 문장을 완성하세요.', items: [
      { ko: '조깅과 쓰레기 줍기를 동시에 한다는 뜻이야.', en: 'It means jogging and picking up trash at the same time.' },
      { ko: '음, 생각해 볼게.', en: 'Well, I\'ll think about it.' }
    ] },
    { type: 'order', title: '문장순서', guide: '대화(문장)를 순서대로 눌러서 배열하세요.', items: [
      { lines: ['Hi, Yuna. What are you doing here?', 'Hi, Alex. I\'m plogging with my club members.', 'Excuse me?', 'Plogging. It means jogging and picking up trash at the same time.'], flow: ['Alex: 여기서 뭐 하고 있니?', 'Yuna: 동아리 회원들과 플로깅 중', 'Alex: 뭐라고?', 'Yuna: 조깅하며 쓰레기 줍기라는 뜻이야'] }
    ] },
    { type: 'blank', title: '빈칸추론', guide: '빈칸에 들어갈 말로 가장 알맞은 것을 고르세요.', items: [
      { s: 'Yes. We plog together every ____ morning from 10 to 12. Interested?', opts: ['Saturday', 'Sunday', 'Monday', 'Friday'], ex: '정답 ▶ Saturday\n이유: 매주 \'토요일\' 아침 10시부터 12시까지 플로깅을 해요.' },
      { s: 'Sounds cool! So you\'re a ____ of a plogging club.', opts: ['member', 'teacher', 'doctor', 'driver'], ex: '정답 ▶ member\n이유: 유나는 동아리 회원들과 플로깅 중 → 플로깅 동아리의 \'회원\'' }
    ] },
    { type: 'mc', title: '어색한 대화 고르기', guide: '짝지어진 대화 중 어색한 것을 고르세요.', items: [
      { q: '다음 중 짝지어진 대화가 <b>어색한</b> 것은?', opts: ['A: Can you help me with this bag? B: Yes, please.', 'A: What are you doing here? B: I\'m plogging.', 'A: Interested? B: Well, I\'ll think about it.', 'A: Can you help me? B: Sure. No problem.'], ex: '정답 ▶ A: Can you help me with this bag? B: Yes, please.\n이유: Yes, please.는 무언가를 권할 때 받는 말이에요. 도움 요청에는 Sure. No problem.으로 답해요.' }
    ] },
    { type: 'mc', title: '의사소통 기능', guide: '상황에 맞는 표현을 고르세요.', items: [
      { q: '밑줄 친 말과 바꿔 쓸 수 있는 것은?<br><b>Alex: <u>Excuse me?</u></b>', opts: ['Can you say that again?', 'I\'m sorry, but I can\'t.', 'Thank you.', 'Here you are.'], ex: '정답 ▶ Can you say that again?\n이유: 여기서 Excuse me?는 잘 못 알아듣고 \'뭐라고?\' 하고 되묻는 말이에요. = Sorry? / Can you say that again?' }
    ] },
    { type: 'mc', title: '요약문 완성', guide: '본문을 읽고 요약문의 빈칸 (A), (B)에 들어갈 말을 고르세요.', items: [
      { n: null, box: ['6과 대화 5 · 플로깅 (Watch, Answer, and Talk)'], q: '다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 알맞은 것은?<br><b>Yuna\'s club goes plogging, which means jogging and picking up (A) ______, and Alex will think about (B) ______ the club.</b>', opts: ['(A) trash – (B) joining', '(A) flowers – (B) joining', '(A) trash – (B) leaving', '(A) friends – (B) closing', '(A) bottles – (B) selling'], ex: '정답 ▶ (A) trash – (B) joining\n(A) 조깅하며 \'쓰레기\' 줍기 → trash\n(B) 동아리에 \'가입하는\' 것을 생각해 본다 → joining', ev: ['It means jogging and picking up trash at the same time', 'Well, I\'ll think about it'] },
      { n: null, box: ['6과 대화 5 · 플로깅 (Watch, Answer, and Talk)'], q: '다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 알맞은 것은?<br><b>At the end, Yuna asks Alex for (A) ______ with the trash bag because it is (B) ______.</b>', opts: ['(A) help – (B) heavy', '(A) help – (B) light', '(A) money – (B) heavy', '(A) a picture – (B) dirty', '(A) advice – (B) empty'], ex: '정답 ▶ (A) help – (B) heavy\n(A) 쓰레기봉투 드는 것을 \'도와\' 달라 → help\n(B) 봉투가 \'무거워서\' → heavy', ev: ['can you please help me with this trash bag', 'It\'s heavy'] }
    ] }
  ] },
  { id: 'd1', name: 'DAY 3', range: '6과 본문 ❶❷❸', story: '병들어 가는 지구 · Olivia의 챌린지 · Domingo의 챌린지', passage: [['', '❶', ''], ['', 'Every day, we produce lots of waste, and the Earth is getting sicker and sicker.', '매일 우리는 많은 쓰레기를 만들고, 지구는 점점 더 병들고 있습니다.'], ['', 'Do you want to save the Earth?', '여러분은 지구를 구하고 싶나요?'], ['', 'Then, join the zero-waste challenge, and share your stories.', '그렇다면 제로 웨이스트 챌린지에 동참하고 여러분의 이야기를 공유해 주세요.'], ['', '❷', ''], ['', 'Challenge 01 Reduce Food Waste', '챌린지 01 / 음식물 쓰레기를 줄이세요'], ['Olivia', 'My birthday was last Saturday, and my family and I ate out.', '내 생일은 지난 토요일이었고, 가족들과 나는 외식을 했어.'], ['', 'There were lots of leftovers, but we brought them home.', '남은 음식이 많았지만, 우리는 그것들을 집으로 가져왔어.'], ['', 'The next day, I made a nice lunch out of them.', '그다음 날, 나는 그것들로 맛있는 점심을 만들었어.'], ['', 'FYI, you can find great cooking ideas for leftovers on the Internet.', '참고로, 인터넷에서 남은 음식을 위한 멋진 요리 아이디어를 찾을 수 있어.'], ['', '❸', ''], ['', 'Challenge 02 Reuse', '챌린지 02 / 재사용하세요'], ['Domingo', 'My dog tore my bag.', '내 개가 내 가방을 찢었어.'], ['', 'I wanted to buy a new one, but I thought again.', '나는 새것을 사고 싶었지만, 다시 생각해 봤어.'], ['', 'I learned that reusing is important for zero-waste living.', '나는 재사용이 제로 웨이스트 생활에 중요하다고 배웠어.'], ['', 'So, I decided to fix it and reuse it.', '그래서 나는 그것을 수선해서 재사용하기로 결심했어.'], ['', 'I\'m not very good at sewing, and I don\'t think that the bag looks perfect.', '나는 바느질을 아주 잘하지 못하고, 가방이 완벽해 보인다고 생각하진 않아.'], ['', 'I guess it\'s all right.', '그래도 괜찮은 것 같아.']], steps: [
    { type: 'vocab', title: '핵심어휘·숙어', quizN: 15, items: [['waste', '쓰레기; 낭비'], ['produce', '생산하다, 만들어 내다'], ['lots of', '많은'], ['sick', '아픈, 병든'], ['save', '구하다; 저축하다'], ['join', '참여하다, 동참하다'], ['challenge', '도전, 챌린지'], ['share', '공유하다'], ['reduce', '줄이다'], ['eat out', '외식하다'], ['leftover', '남은 음식'], ['bring', '가져오다'], ['make A out of B', 'B로 A를 만들다'], ['FYI', '참고로'], ['on the Internet', '인터넷에서'], ['reuse', '재사용하다'], ['tear', '찢다'], ['learn', '배우다'], ['important', '중요한'], ['living', '생활'], ['decide', '결심하다, 결정하다'], ['fix', '고치다, 수선하다'], ['be good at', '~을 잘하다'], ['sew', '바느질하다'], ['perfect', '완벽한'], ['guess', '추측하다, ~인 것 같다'], ['all right', '괜찮은']] },
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
      { s: 'I\'m not very good at {sewing|cooking}, and I don\'t think that the bag looks perfect.', ex: '가방을 고치려면 바느질(sewing)을 해야 한다.' }
    ] },
    { type: 'tf', title: 'T/F 내용 확인', guide: '본문 내용과 일치하면 T, 다르면 F를 고르세요.', items: [['The Earth is getting healthier these days.', false, '지구는 점점 더 병들고(sicker and sicker) 있다.'], ['Olivia\'s birthday was last Saturday.', true, 'My birthday was last Saturday.'], ['Olivia\'s family left the leftovers at the restaurant.', false, '남은 음식을 집으로 가져왔다(brought them home).'], ['Olivia made lunch out of the leftovers the next day.', true, 'The next day, I made a nice lunch out of them.'], ['Domingo\'s cat tore his bag.', false, '가방을 찢은 것은 개(dog)다.'], ['Domingo bought a new bag.', false, '새 가방을 사지 않고 고쳐서 다시 썼다.'], ['Domingo learned that reusing is important for zero-waste living.', true, 'I learned that reusing is important for zero-waste living.'], ['Domingo thinks his bag looks perfect.', false, '가방이 완벽해 보인다고 생각하지 않는다.']] },
    { type: 'mc', title: '일치·불일치', guide: '본문을 읽고 내용과 맞는지 확인해요. 틀린 선택지는 해설의 근거 문장과 비교해 보세요.', items: [
      { n: '❷', box: ['❷'], q: 'Olivia에 관한 내용과 일치하지 <u>않는</u> 것은?', opts: ['Olivia\'s family threw away the leftovers.', 'Olivia\'s birthday was last Saturday.', 'Olivia and her family ate out.', 'Olivia made lunch out of the leftovers.', 'You can find cooking ideas for leftovers on the Internet.'], ex: '정답 근거: There were lots of leftovers, but we brought them home.\n· leftovers : 남은 음식 · throw away : 버리다 · eat out : 외식하다', per: [['Olivia의 가족은 남은 음식을 버렸다.', 'we brought them home', '불일치 → 집으로 가져옴'], ['Olivia의 생일은 지난 토요일이었다.', 'My birthday was last Saturday', '일치'], ['Olivia와 가족은 외식했다.', 'my family and I ate out', '일치'], ['Olivia는 남은 음식으로 점심을 만들었다.', 'I made a nice lunch out of them', '일치'], ['인터넷에서 남은 음식 요리 아이디어를 찾을 수 있다.', 'you can find great cooking ideas for leftovers on the Internet', '일치']] },
      { n: '❸', box: ['❸'], q: 'Domingo에 관한 내용과 <u>일치하는</u> 것은?', opts: ['Domingo decided to fix his bag and reuse it.', 'Domingo tore his dog\'s bag.', 'Domingo bought a new bag.', 'Domingo is very good at sewing.', 'Domingo thinks the bag looks perfect.'], ex: '정답 근거: So, I decided to fix it and reuse it.\n· tear - tore - torn : 찢다 · sew : 바느질하다 · reuse : 재사용하다', per: [['Domingo는 가방을 고쳐서 다시 쓰기로 했다.', 'I decided to fix it and reuse it', '일치'], ['Domingo가 개의 가방을 찢었다.', 'My dog tore my bag', '불일치 → 개가 Domingo의 가방을 찢음'], ['Domingo는 새 가방을 샀다.', 'I wanted to buy a new one, but I thought again', '불일치 → 사지 않음'], ['Domingo는 바느질을 아주 잘한다.', 'I\'m not very good at sewing', '불일치 → 잘 못함'], ['Domingo는 가방이 완벽해 보인다고 생각한다.', 'I don\'t think that the bag looks perfect', '불일치 → 완벽하진 않다고 생각함']] }
    ] },
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
    ] },
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
      { s: 'I\'m not very good at sewing, and I don\'t think that the bag ___ perfect.', v: 'look', a: ['looks'], ex: '주어 the bag → looks' }
    ] },
    { type: 'error', title: '오류찾기', guide: '어법상 틀린 곳을 고르세요.', items: [
      { s: 'Every day, we [[produce]] lots of waste, and the Earth is [[getting]] [[sick]] and [[sicker]].', w: 2, fix: 'sicker', ex: '비교급 and 비교급 → sicker and sicker' },
      { s: 'Do you want [[saving]] the Earth? Then, [[join]] the zero-waste challenge, and [[share]] [[your]] stories.', w: 0, fix: 'to save', ex: 'want + to부정사' },
      { s: 'My birthday [[was]] last Saturday, and my family and I [[eat]] out. There [[were]] [[lots of]] leftovers.', w: 1, fix: 'ate', ex: 'last Saturday → 과거형 ate' },
      { s: 'There were lots of leftovers, but we [[bringed]] them home. The next day, I [[made]] a nice lunch [[out of]] [[them]].', w: 0, fix: 'brought', ex: 'bring - brought - brought' },
      { s: 'I wanted [[to buy]] a new one, but I [[thinked]] again. I learned [[that]] reusing [[is]] important for zero-waste living.', w: 1, fix: 'thought', ex: 'think - thought - thought' },
      { s: 'So, I decided [[fix]] it and [[reuse]] it. I\'m not very [[good]] at [[sewing]].', w: 0, fix: 'to fix', ex: 'decide + to부정사' },
      { s: 'I\'m not very good at sewing, and I don\'t think [[that]] the bag [[look]] [[perfect]]. I [[guess]] it\'s all right.', w: 1, fix: 'looks', ex: '주어 the bag은 3인칭 단수 → looks' }
    ] },
    { type: 'scramble', title: '본문 스크램블', guide: '우리말에 맞게 단어를 눌러 문장을 완성하세요.', items: [
      { ko: '여러분은 지구를 구하고 싶나요?', en: 'Do you want to save the Earth?' },
      { ko: '그렇다면 제로 웨이스트 챌린지에 동참하고 여러분의 이야기를 공유해 주세요.', en: 'Then, join the zero-waste challenge, and share your stories.' },
      { ko: '남은 음식이 많았지만, 우리는 그것들을 집으로 가져왔어.', en: 'There were lots of leftovers, but we brought them home.' },
      { ko: '그다음 날, 나는 그것들로 맛있는 점심을 만들었어.', en: 'The next day, I made a nice lunch out of them.' },
      { ko: '나는 재사용이 제로 웨이스트 생활에 중요하다고 배웠어.', en: 'I learned that reusing is important for zero-waste living.' },
      { ko: '그래서 나는 그것을 수선해서 재사용하기로 결심했어.', en: 'So, I decided to fix it and reuse it.' },
      { ko: '나는 바느질을 아주 잘하지는 못해.', en: 'I\'m not very good at sewing.' }
    ] },
    { type: 'order', title: '문장순서', guide: '문장을 본문 순서대로 눌러서 배열하세요.', items: [
      { lines: ['Every day, we produce lots of waste, and the Earth is getting sicker and sicker.', 'Do you want to save the Earth?', 'Then, join the zero-waste challenge, and share your stories.'] },
      { lines: ['My birthday was last Saturday, and my family and I ate out.', 'There were lots of leftovers, but we brought them home.', 'The next day, I made a nice lunch out of them.', 'FYI, you can find great cooking ideas for leftovers on the Internet.'] },
      { lines: ['My dog tore my bag.', 'I wanted to buy a new one, but I thought again.', 'I learned that reusing is important for zero-waste living.', 'So, I decided to fix it and reuse it.'] },
      { lines: ['I learned that reusing is important for zero-waste living.', 'So, I decided to fix it and reuse it.', 'I\'m not very good at sewing, and I don\'t think that the bag looks perfect.', 'I guess it\'s all right.'] }
    ] },
    { type: 'insert', title: '문장삽입', guide: '주어진 문장이 들어가기에 가장 알맞은 곳을 고르세요.', items: [
      { lines: ['Every day, we produce lots of waste, and the Earth is getting sicker and sicker.', 'Do you want to save the Earth?', 'Then, join the zero-waste challenge, and share your stories.'], given: 1, ex: 'Then(그렇다면)은 "지구를 구하고 싶나요?"라는 질문에 이어진다.' },
      { lines: ['My birthday was last Saturday, and my family and I ate out.', 'There were lots of leftovers, but we brought them home.', 'The next day, I made a nice lunch out of them.', 'FYI, you can find great cooking ideas for leftovers on the Internet.'], given: 2, ex: 'them은 집으로 가져온 남은 음식(leftovers)을 가리킨다.' },
      { lines: ['My dog tore my bag.', 'I wanted to buy a new one, but I thought again.', 'I learned that reusing is important for zero-waste living.', 'So, I decided to fix it and reuse it.', 'I\'m not very good at sewing, and I don\'t think that the bag looks perfect.'], given: 3, ex: 'So(그래서) 앞에는 이유(재사용이 중요하다는 것을 배움)가 와야 한다.' }
    ] },
    { type: 'odd', title: '어색한 문장', guide: '글의 흐름과 관계없는 문장을 고르세요.', items: [
      { lines: ['Every day, we produce lots of waste, and the Earth is getting sicker and sicker.', 'Do you want to save the Earth?', 'Making more waste is good for the Earth.', 'Then, join the zero-waste challenge, and share your stories.'], odd: 2, ex: '쓰레기가 지구를 병들게 한다는 흐름과 반대된다.' },
      { lines: ['My birthday was last Saturday, and my family and I ate out.', 'There were lots of leftovers, but we brought them home.', 'We threw all the leftovers away at the restaurant.', 'The next day, I made a nice lunch out of them.'], odd: 2, ex: '남은 음식을 집으로 가져왔다는 내용과 반대된다.' },
      { lines: ['My dog tore my bag.', 'I wanted to buy a new one, but I thought again.', 'I learned that reusing is important for zero-waste living.', 'Buying new things is the best way to save the Earth.', 'So, I decided to fix it and reuse it.'], odd: 3, ex: '재사용이 중요하다는 흐름과 맞지 않는다.' }
    ] },
    { type: 'blank', title: '빈칸추론', guide: '빈칸에 들어갈 말로 가장 알맞은 것을 고르세요.', items: [
      { s: 'Every day, we produce lots of waste, and the Earth is getting ____.', opts: ['sicker and sicker', 'healthier and healthier', 'cleaner and cleaner', 'bigger and bigger'], ex: '쓰레기 때문에 지구가 점점 더 병들고 있다.' },
      { s: 'There were lots of leftovers, but we ____.', opts: ['brought them home', 'threw them away', 'gave them to the dog', 'left them there'], ex: '음식물 쓰레기를 줄이기 위해 남은 음식을 집으로 가져왔다.' },
      { s: 'I learned that ____ is important for zero-waste living.', opts: ['reusing', 'buying new things', 'throwing things away', 'using plastic'], ex: '제로 웨이스트 생활에는 재사용이 중요하다.' },
      { s: 'So, I decided to ____ it and reuse it.', opts: ['fix', 'sell', 'throw', 'tear'], ex: '찢어진 가방을 고쳐서 다시 쓰기로 했다.' }
    ] },
    { type: 'mc', title: '핵심문법', guide: '알맞은 답을 고르세요.', items: [
      { q: '밑줄 친 to부정사의 쓰임이 나머지와 <b>다른</b> 것은?', opts: ['I went to the store <u>to buy</u> milk.', 'I want <u>to save</u> the Earth.', 'I decided <u>to fix</u> it.', 'She hopes <u>to visit</u> Paris.'], ex: '①은 목적(~하기 위해). 나머지는 동사의 목적어(~하는 것) → 명사적 용법' },
      { q: '빈칸에 들어갈 수 <b>없는</b> 것은?<br><b>I ______ to fix my bag.</b>', opts: ['enjoyed', 'wanted', 'decided', 'planned'], ex: 'enjoy는 동명사만 목적어로 쓴다 (enjoyed fixing).' },
      { q: '빈칸에 알맞은 것은?<br><b>I learned ______ reusing is important.</b>', opts: ['that', 'what', 'this', 'it'], ex: '완전한 문장을 이끄는 접속사 that' },
      { q: '밑줄 친 <b>that</b>을 생략할 수 있는 것은?', opts: ['I don\'t think <u>that</u> the bag looks perfect.', '<u>That</u> bag is mine.', 'Look at <u>that</u> dog.', '<u>That</u> is my bag.'], ex: '동사의 목적어 자리 접속사 that은 생략할 수 있다.' },
      { q: '동사의 과거형이 <b>틀린</b> 것은?', opts: ['bring - bringed', 'eat - ate', 'make - made', 'tear - tore'], ex: 'bring - brought' },
      { q: '빈칸에 알맞은 것은?<br><b>There ______ lots of leftovers yesterday.</b>', opts: ['were', 'was', 'are', 'is'], ex: '복수명사 + 과거 → There were' },
      { q: '"지구는 점점 더 병들고 있다."를 바르게 영작한 것은?', opts: ['The Earth is getting sicker and sicker.', 'The Earth is getting sick and sick.', 'The Earth is getting more sick and sick.', 'The Earth is getting sickest and sickest.'], ex: '비교급 and 비교급: 점점 더 ~한' },
      { q: '빈칸에 알맞은 것은?<br><b>Reusing old things ______ important.</b>', opts: ['is', 'are', 'be', 'were'], ex: '동명사 주어는 단수 취급 → is' },
      { q: '"나는 남은 음식으로 점심을 만들었다."를 바르게 영작한 것은?', opts: ['I made lunch out of the leftovers.', 'I made the leftovers out of lunch.', 'I made out of lunch the leftovers.', 'I made lunch the leftovers out of.'], ex: 'make A out of B: B로 A를 만들다' }
    ] }
  ] },
  { id: 'd2', name: 'DAY 4', range: '6과 본문 ❹❺', story: 'Emma의 챌린지 · 민수의 챌린지', passage: [['', '❹', ''], ['', 'Challenge 03 Say No to Single-Use Plastic', '챌린지 03 / 일회용 플라스틱 사용을 반대하세요'], ['Emma', 'I often use food delivery services, but today I didn\'t.', '나는 종종 음식 배달 서비스를 이용하는데, 오늘은 이용하지 않았어.'], ['', 'Instead, I walked to my favorite restaurant with a reusable container and picked up the food.', '대신, 재사용할 수 있는 용기를 가지고 내가 가장 좋아하는 식당에 걸어가서 음식을 가져왔어.'], ['', 'I heard that plastic never goes away completely.', '플라스틱은 절대로 완전히 없어지지 않는다고 들었어.'], ['', 'I didn\'t use any single-use plastic today.', '나는 오늘 어떤 일회용 플라스틱도 사용하지 않았어.'], ['', 'I felt good!', '기분이 좋았어!'], ['', '❺', ''], ['', 'Challenge 04 Recycle', '챌린지 04 / 재활용하세요'], ['Minsu', 'Yesterday, I took some plastic and glass bottles to a recycling machine near my house.', '어제 나는 플라스틱과 유리병 몇 개를 집 근처에 있는 재활용 기계에 가져갔어.'], ['', 'I put them into the machine one by one, and I got some points in return.', '나는 그것들을 하나씩 기계에 집어넣었고, 대가로 포인트를 받았어.'], ['', 'What can I do with those points?', '그 포인트로 무엇을 할 수 있냐고?'], ['', 'Well, I can use them like money.', '음, 나는 그것들을 돈처럼 사용할 수 있어.'], ['', 'Don\'t you think that\'s cool?', '멋지다고 생각하지 않니?']], steps: [
    { type: 'vocab', title: '핵심어휘·숙어', quizN: 15, items: [['say no to', '~에 반대하다, ~을 거절하다'], ['single-use', '일회용의'], ['plastic', '플라스틱'], ['often', '종종, 자주'], ['delivery', '배달'], ['instead', '대신에'], ['favorite', '가장 좋아하는'], ['restaurant', '식당'], ['reusable', '재사용할 수 있는'], ['container', '용기, 그릇'], ['pick up', '(음식 등을) 찾아오다'], ['hear', '듣다'], ['never', '결코 ~않다'], ['go away', '없어지다'], ['completely', '완전히'], ['feel', '~한 기분이 들다'], ['recycle', '재활용하다'], ['take A to B', 'A를 B로 가져가다'], ['glass', '유리'], ['bottle', '병'], ['machine', '기계'], ['near', '~ 근처에'], ['put A into B', 'A를 B에 넣다'], ['one by one', '하나씩'], ['in return', '대가로, 답례로'], ['point', '포인트, 점수'], ['like (전치사)', '~처럼'], ['cool', '멋진; 시원한']] },
    { type: 'pick', title: '어휘선택', guide: '문맥에 맞는 낱말을 고르세요.', items: [
      { s: 'Challenge 03 Say No to {Single-Use|Reusable} Plastic', ex: 'single-use: 일회용의' },
      { s: 'I {often|never} use food delivery services, but today I didn\'t.', ex: '평소에는 종종(often) 쓰지만 오늘은 쓰지 않았다.' },
      { s: '{Instead|Also}, I walked to my favorite restaurant with a reusable container and picked up the food.', ex: 'instead: 대신에 (배달 대신 직접 갔다)' },
      { s: 'Instead, I walked to my favorite restaurant with a {reusable|single-use} container and picked up the food.', ex: '일회용 플라스틱을 쓰지 않으려고 재사용 용기를 가져갔다.' },
      { s: 'I heard that plastic never goes away {completely|quickly}.', ex: 'completely: 완전히' },
      { s: 'I didn\'t use any single-use plastic today. I felt {good|bad}!', ex: '일회용 플라스틱을 쓰지 않아서 기분이 좋았다.' },
      { s: 'Yesterday, I took some plastic and glass bottles to a {recycling|washing} machine near my house.', ex: 'recycling machine: 재활용 기계' },
      { s: 'I put them into the machine {one by one|all at once}, and I got some points in return.', ex: 'one by one: 하나씩' },
      { s: 'I put them into the machine one by one, and I got some points {in return|in a hurry}.', ex: 'in return: 대가로' },
      { s: 'Well, I can use them {like|with} money.', ex: 'like: ~처럼' }
    ] },
    { type: 'tf', title: 'T/F 내용 확인', guide: '본문 내용과 일치하면 T, 다르면 F를 고르세요.', items: [['Emma never uses food delivery services.', false, 'Emma는 종종(often) 배달 서비스를 이용한다.'], ['Emma walked to her favorite restaurant today.', true, 'I walked to my favorite restaurant'], ['Emma took a reusable container to the restaurant.', true, 'with a reusable container'], ['Emma heard that plastic goes away quickly.', false, '플라스틱은 절대 완전히 없어지지 않는다고 들었다.'], ['Emma used some single-use plastic today.', false, '오늘은 일회용 플라스틱을 전혀 쓰지 않았다.'], ['Minsu took some bottles to a recycling machine near his house.', true, 'to a recycling machine near my house'], ['Minsu got some money from the machine.', false, '돈이 아니라 포인트(points)를 받았다.'], ['Minsu can use the points like money.', true, 'I can use them like money.']] },
    { type: 'mc', title: '일치·불일치', guide: '본문을 읽고 내용과 맞는지 확인해요. 틀린 선택지는 해설의 근거 문장과 비교해 보세요.', items: [
      { n: '❹', box: ['❹'], q: 'Emma에 관한 내용과 일치하지 <u>않는</u> 것은?', opts: ['Emma used food delivery services today.', 'Emma walked to her favorite restaurant.', 'Emma took a reusable container with her.', 'Emma heard that plastic never goes away completely.', 'Emma felt good.'], ex: '정답 근거: I often use food delivery services, but today I didn\'t.\n· delivery : 배달 · reusable : 재사용할 수 있는 · container : 용기', per: [['Emma는 오늘 음식 배달 서비스를 이용했다.', 'but today I didn\'t', '불일치 → 오늘은 이용하지 않음'], ['Emma는 가장 좋아하는 식당에 걸어갔다.', 'I walked to my favorite restaurant', '일치'], ['Emma는 재사용 용기를 가지고 갔다.', 'with a reusable container', '일치'], ['Emma는 플라스틱이 절대 완전히 사라지지 않는다고 들었다.', 'plastic never goes away completely', '일치'], ['Emma는 기분이 좋았다.', 'I felt good', '일치']] },
      { n: '❺', box: ['❺'], q: 'Minsu에 관한 내용과 <u>일치하는</u> 것은?', opts: ['Minsu can use the points like money.', 'Minsu took paper and cans to the machine.', 'The recycling machine is far from Minsu\'s house.', 'Minsu put all the bottles into the machine at once.', 'Minsu got some money from the machine.'], ex: '정답 근거: Well, I can use them like money.\n· one by one : 하나씩 · in return : 대가로', per: [['민수는 포인트를 돈처럼 쓸 수 있다.', 'I can use them like money', '일치'], ['민수는 종이와 캔을 기계에 가져갔다.', 'I took some plastic and glass bottles', '불일치 → 플라스틱과 유리병'], ['재활용 기계는 민수의 집에서 멀다.', 'a recycling machine near my house', '불일치 → 집 근처'], ['민수는 병을 한꺼번에 기계에 넣었다.', 'one by one', '불일치 → 하나씩'], ['민수는 기계에서 돈을 받았다.', 'I got some points in return', '불일치 → 돈이 아니라 포인트']] }
    ] },
    { type: 'pick', title: '어법선택', guide: '어법상 알맞은 것을 고르세요.', items: [
      { s: 'I {often use|use often} food delivery services, but today I didn\'t.', ex: '빈도부사는 일반동사 앞에' },
      { s: 'I often use food delivery services, but today I {didn\'t|don\'t}.', ex: 'today 오늘 있었던 일(과거) → didn\'t' },
      { s: 'Instead, I {walked|walk} to my favorite restaurant with a reusable container and picked up the food.', ex: 'picked와 병렬 → 과거형 walked' },
      { s: 'Instead, I walked to my favorite restaurant with a reusable container and {picked|picks} up the food.', ex: 'walked와 병렬 → picked' },
      { s: 'I heard {that|what} plastic never goes away completely.', ex: '뒤에 완전한 문장 → 접속사 that' },
      { s: 'I heard that plastic never {goes|go} away completely.', ex: '주어 plastic은 단수 → goes' },
      { s: 'I didn\'t {use|used} any single-use plastic today.', ex: 'didn\'t + 동사원형' },
      { s: 'Yesterday, I {took|take} some plastic and glass bottles to a recycling machine near my house.', ex: 'Yesterday → 과거형 took' },
      { s: 'I put them into the machine one by one, and I {got|get} some points in return.', ex: '과거 이야기 → got' },
      { s: 'What can I {do|did} with those points?', ex: '조동사 can + 동사원형' },
      { s: '{Don\'t|Doesn\'t} you think that\'s cool?', ex: '주어 you → Don\'t' }
    ] },
    { type: 'verb', title: '동사변형', guide: '( ) 안의 동사를 알맞은 형태로 바꿔 쓰세요. 과거형에 주의!', items: [
      { s: 'I often ___ food delivery services, but today I didn\'t.', v: 'use', a: ['use'], ex: '평소 습관 → 현재형' },
      { s: 'Instead, I ___ to my favorite restaurant with a reusable container and picked up the food.', v: 'walk', a: ['walked'], ex: '과거형 walked' },
      { s: 'Instead, I walked to my favorite restaurant with a reusable container and ___ up the food.', v: 'pick', a: ['picked'], ex: '과거형 picked' },
      { s: 'I ___ that plastic never goes away completely.', v: 'hear', a: ['heard'], ex: 'hear - heard - heard' },
      { s: 'I heard that plastic never ___ away completely.', v: 'go', a: ['goes'], ex: '사실·일반적 진리 → 현재형, 주어 단수 → goes' },
      { s: 'I didn\'t ___ any single-use plastic today.', v: 'use', a: ['use'], ex: 'didn\'t + 동사원형' },
      { s: 'I ___ good!', v: 'feel', a: ['felt'], ex: 'feel - felt - felt' },
      { s: 'Yesterday, I ___ some plastic and glass bottles to a recycling machine near my house.', v: 'take', a: ['took'], ex: 'take - took - taken' },
      { s: 'I ___ them into the machine one by one, and I got some points in return.', v: 'put', a: ['put'], ex: 'put - put - put (과거형도 put)' },
      { s: 'I put them into the machine one by one, and I ___ some points in return.', v: 'get', a: ['got'], ex: 'get - got - got/gotten' }
    ] },
    { type: 'error', title: '오류찾기', guide: '어법상 틀린 곳을 고르세요.', items: [
      { s: 'I [[often use]] food delivery services, but today I [[don\'t]]. Instead, I [[walked]] to my [[favorite]] restaurant.', w: 1, fix: 'didn\'t', ex: '오늘 있었던 일 → 과거 didn\'t' },
      { s: 'Instead, I [[walked]] to my favorite restaurant [[with]] a reusable container and [[pick]] up [[the food]].', w: 2, fix: 'picked', ex: 'walked와 병렬 → picked' },
      { s: 'I heard [[what]] plastic never [[goes]] away [[completely]]. I didn\'t use [[any]] single-use plastic today.', w: 0, fix: 'that', ex: '뒤에 완전한 문장 → 접속사 that' },
      { s: 'I didn\'t [[used]] any single-use plastic today. I [[felt]] [[good]]!', w: 0, fix: 'use', ex: 'didn\'t + 동사원형' },
      { s: 'Yesterday, I [[take]] some plastic and glass bottles [[to]] a recycling machine [[near]] my [[house]].', w: 0, fix: 'took', ex: 'Yesterday → 과거형 took' },
      { s: 'I put them [[into]] the machine [[one by one]], and I [[getted]] some points [[in return]].', w: 2, fix: 'got', ex: 'get - got' },
      { s: 'What can I [[did]] with those points? Well, I can [[use]] them [[like]] money.', w: 0, fix: 'do', ex: '조동사 can + 동사원형' }
    ] },
    { type: 'scramble', title: '본문 스크램블', guide: '우리말에 맞게 단어를 눌러 문장을 완성하세요.', items: [
      { ko: '나는 종종 음식 배달 서비스를 이용해.', en: 'I often use food delivery services.' },
      { ko: '플라스틱은 절대로 완전히 없어지지 않는다고 들었어.', en: 'I heard that plastic never goes away completely.' },
      { ko: '나는 오늘 어떤 일회용 플라스틱도 사용하지 않았어.', en: 'I didn\'t use any single-use plastic today.' },
      { ko: '나는 그것들을 하나씩 기계에 집어넣었어.', en: 'I put them into the machine one by one.' },
      { ko: '나는 대가로 포인트를 받았어.', en: 'I got some points in return.' },
      { ko: '그 포인트로 무엇을 할 수 있을까?', en: 'What can I do with those points?' },
      { ko: '음, 나는 그것들을 돈처럼 사용할 수 있어.', en: 'Well, I can use them like money.' },
      { ko: '멋지다고 생각하지 않니?', en: 'Don\'t you think that\'s cool?' }
    ] },
    { type: 'order', title: '문장순서', guide: '문장을 본문 순서대로 눌러서 배열하세요.', items: [
      { lines: ['I often use food delivery services, but today I didn\'t.', 'Instead, I walked to my favorite restaurant with a reusable container and picked up the food.', 'I heard that plastic never goes away completely.', 'I didn\'t use any single-use plastic today.', 'I felt good!'] },
      { lines: ['Yesterday, I took some plastic and glass bottles to a recycling machine near my house.', 'I put them into the machine one by one, and I got some points in return.', 'What can I do with those points?', 'Well, I can use them like money.', 'Don\'t you think that\'s cool?'] },
      { lines: ['I put them into the machine one by one, and I got some points in return.', 'What can I do with those points?', 'Well, I can use them like money.', 'Don\'t you think that\'s cool?'] }
    ] },
    { type: 'insert', title: '문장삽입', guide: '주어진 문장이 들어가기에 가장 알맞은 곳을 고르세요.', items: [
      { lines: ['I often use food delivery services, but today I didn\'t.', 'Instead, I walked to my favorite restaurant with a reusable container and picked up the food.', 'I heard that plastic never goes away completely.', 'I didn\'t use any single-use plastic today.', 'I felt good!'], given: 1, ex: 'Instead(대신에)는 "오늘은 배달을 이용하지 않았다" 다음에 온다.' },
      { lines: ['Instead, I walked to my favorite restaurant with a reusable container and picked up the food.', 'I heard that plastic never goes away completely.', 'I didn\'t use any single-use plastic today.', 'I felt good!'], given: 3, ex: '일회용 플라스틱을 쓰지 않아서 기분이 좋았다.' },
      { lines: ['Yesterday, I took some plastic and glass bottles to a recycling machine near my house.', 'I put them into the machine one by one, and I got some points in return.', 'What can I do with those points?', 'Well, I can use them like money.'], given: 1, ex: 'them은 앞 문장의 plastic and glass bottles를 가리킨다.' },
      { lines: ['I put them into the machine one by one, and I got some points in return.', 'What can I do with those points?', 'Well, I can use them like money.', 'Don\'t you think that\'s cool?'], given: 2, ex: '"포인트로 무엇을 할 수 있을까?"라는 질문에 대한 대답이다.' }
    ] },
    { type: 'odd', title: '어색한 문장', guide: '글의 흐름과 관계없는 문장을 고르세요.', items: [
      { lines: ['I often use food delivery services, but today I didn\'t.', 'Instead, I walked to my favorite restaurant with a reusable container and picked up the food.', 'I asked the restaurant for lots of plastic bags.', 'I heard that plastic never goes away completely.', 'I didn\'t use any single-use plastic today.'], odd: 2, ex: '일회용 플라스틱을 쓰지 않으려 했다는 흐름과 반대된다.' },
      { lines: ['I heard that plastic never goes away completely.', 'I didn\'t use any single-use plastic today.', 'I felt good!', 'Single-use plastic is good for the Earth.'], odd: 3, ex: '플라스틱이 없어지지 않아 지구에 해롭다는 흐름과 맞지 않는다.' },
      { lines: ['Yesterday, I took some plastic and glass bottles to a recycling machine near my house.', 'I put them into the machine one by one, and I got some points in return.', 'The machine was broken, so I threw the bottles away.', 'What can I do with those points?', 'Well, I can use them like money.'], odd: 2, ex: '병을 기계에 넣고 포인트를 받았다는 내용과 반대된다.' }
    ] },
    { type: 'blank', title: '빈칸추론', guide: '빈칸에 들어갈 말로 가장 알맞은 것을 고르세요.', items: [
      { s: 'Instead, I walked to my favorite restaurant with ____ and picked up the food.', opts: ['a reusable container', 'a plastic bag', 'a paper cup', 'a delivery box'], ex: '일회용 플라스틱을 쓰지 않으려고 재사용 용기를 가져갔다.' },
      { s: 'I heard that plastic ____ completely.', opts: ['never goes away', 'goes away quickly', 'is good for the Earth', 'is easy to make'], ex: '플라스틱은 절대 완전히 없어지지 않는다.' },
      { s: 'I put them into the machine one by one, and I got ____.', opts: ['some points in return', 'some new bottles', 'a lot of trash', 'a plastic bag'], ex: '병을 넣고 대가로 포인트를 받았다.' },
      { s: 'Well, I can use them ____.', opts: ['like money', 'like plastic', 'like bottles', 'like trash'], ex: '포인트는 돈처럼 쓸 수 있다.' }
    ] },
    { type: 'mc', title: '핵심문법', guide: '알맞은 답을 고르세요.', items: [
      { q: '빈도부사의 위치가 <b>틀린</b> 것은?', opts: ['She always is busy.', 'She is always busy.', 'I never eat breakfast.', 'We can often see stars.'], ex: 'be동사 뒤에 빈도부사 → She is always busy.' },
      { q: '어법상 올바른 문장은?', opts: ['I often use delivery services.', 'I use often delivery services.', 'Often I uses delivery services.', 'I often am late.'], ex: '빈도부사는 일반동사 앞, be동사·조동사 뒤' },
      { q: '대화의 빈칸에 알맞은 것은?<br><b>A: Don\'t you think that\'s cool?<br>B: ______ It\'s really cool.</b>', opts: ['Yes, I do.', 'No, I do.', 'Yes, I don\'t.', 'No, I don\'t.'], ex: '부정의문문이어도 대답 내용이 긍정이면 Yes, 부정이면 No' },
      { q: '대화의 빈칸에 알맞은 것은?<br><b>A: Don\'t you like coffee?<br>B: ______ I don\'t like it.</b>', opts: ['No, I don\'t.', 'Yes, I don\'t.', 'No, I do.', 'Yes, I do.'], ex: '좋아하지 않는다(부정) → No, I don\'t.' },
      { q: '빈칸에 알맞은 것은?<br><b>I heard ______ plastic never goes away.</b>', opts: ['that', 'what', 'this', 'it'], ex: '완전한 문장을 이끄는 접속사 that' },
      { q: '동사의 과거형이 <b>틀린</b> 것은?', opts: ['take - taked', 'put - put', 'get - got', 'feel - felt'], ex: 'take - took' },
      { q: '빈칸에 알맞은 것은?<br><b>I didn\'t use ______ single-use plastic today.</b>', opts: ['any', 'some', 'a', 'many'], ex: '부정문에서는 any (어떤 ~도)' },
      { q: '"나는 병들을 재활용 기계로 가져갔다."를 바르게 영작한 것은?', opts: ['I took the bottles to a recycling machine.', 'I took to a recycling machine the bottles.', 'I taked the bottles to a recycling machine.', 'I take the bottles a recycling machine to.'], ex: 'take A to B: A를 B로 가져가다' },
      { q: '빈칸에 알맞은 것은?<br><b>I put them ______ the machine one by one.</b>', opts: ['into', 'out', 'at', 'from'], ex: 'put A into B: A를 B에 넣다' }
    ] }
  ] },
  { id: 'c7a', name: 'DAY 5', range: '7과 대화문 ① 대화 1~4', story: 'Lesson 7 · 관심과 장래 희망 묻고 답하기 · 대화 1~4', passage: [['#', '7과 대화 1 · 스포츠 기자', ''], ['G', 'What do you want to be in the future, Minsu?', '앞으로 무엇이 되고 싶니, 민수야?'], ['B', 'I want to be a sports reporter.', '나는 스포츠 기자가 되고 싶어.'], ['G', 'Oh, really? Do you watch a lot of sports games?', '오, 정말? 스포츠 경기를 많이 보니?'], ['B', 'Yes, I do. I\'m interested in all kinds of sports.', '응, 그래. 나는 모든 종류의 스포츠에 관심이 있어.'], ['#', '7과 대화 2 · 요리사', ''], ['G', 'David, what are you making?', 'David, 무엇을 만들고 있니?'], ['B', 'I\'m making pizza and pasta.', '피자와 파스타를 만들고 있어.'], ['G', 'They look delicious. Are you interested in Italian food?', '맛있어 보인다. 너는 이탈리아 음식에 관심 있니?'], ['B', 'Yes, I am. I want to be a world-famous chef in the future!', '응, 그래. 나는 앞으로 세계적으로 유명한 요리사가 되고 싶어!'], ['#', '7과 대화 3 · 작곡가', ''], ['G', 'What\'s this music, Hojin? It\'s awesome.', '이 음악 뭐야, 호진아? 굉장하다.'], ['B', 'I\'m writing a song with this computer program.', '나는 이 컴퓨터 프로그램으로 노래를 만들고 있어.'], ['G', 'You\'re very good. Do you want to be a songwriter?', '정말 잘하는구나. 너는 작곡가가 되고 싶니?'], ['B', 'Yes, I\'m really interested in writing songs.', '응, 나는 노래를 만드는 것에 정말로 관심이 있어.'], ['#', '7과 대화 4 · 패션 디자이너', ''], ['G', 'Are you interested in fashion, Jacob?', '패션에 관심이 있니, Jacob?'], ['B', 'Yes, I love to make clothes.', '응, 나는 옷 만드는 것을 매우 좋아해.'], ['G', 'Really? That\'s so cool!', '정말? 너무 멋있다!'], ['B', 'Thanks. I want to be a fashion designer. I\'ll make clothes for you someday.', '고마워. 나는 패션 디자이너가 되고 싶어. 언젠가 너에게 옷을 만들어 줄게.']], steps: [
    { type: 'vocab', title: '핵심어휘·숙어', quizN: 11, items: [['future', '미래'], ['be interested in', '~에 관심이 있다'], ['reporter', '기자'], ['all kinds of', '모든 종류의'], ['look delicious', '맛있어 보이다'], ['world-famous', '세계적으로 유명한'], ['chef', '요리사'], ['awesome', '굉장한'], ['songwriter', '작곡가'], ['fashion designer', '패션 디자이너'], ['someday', '언젠가']] },
    { type: 'pick', title: '어휘선택', guide: '문맥에 맞는 낱말을 고르세요.', items: [
      { s: 'They look {delicious|terrible}. Are you interested in Italian food?', ex: '정답 ▶ delicious (맛있는)\n오답 ▶ terrible (끔찍한): 요리사가 꿈인 친구가 만든 피자와 파스타 → \'맛있어 보인다\'는 칭찬이에요.' },
      { s: 'You\'re very good. Do you want to be a {songwriter|chef}?', ex: '정답 ▶ songwriter (작곡가)\n오답 ▶ chef (요리사): 컴퓨터 프로그램으로 노래를 만들고 있으니 \'작곡가\'가 되고 싶은지 물어요.' },
      { s: 'Yes, I love to make {clothes|songs}.', ex: '정답 ▶ clothes (옷)\n오답 ▶ songs (노래): 패션에 관심 있냐는 질문의 대답 → \'옷 만드는 것\'을 좋아해요.' }
    ] },
    { type: 'tf', title: 'T/F 내용 확인', guide: '본문 내용과 일치하면 T, 다르면 F를 고르세요.', items: [['Minsu wants to be a cameraman.', false, '정답 ▶ F\n이유: 민수는 스포츠 기자(a sports reporter)가 되고 싶어 해요.', null, 'I want to be a sports reporter'], ['David is making Italian food.', true, '정답 ▶ T\n이유: 피자와 파스타 = 이탈리아 음식을 만들고 있어요.', null, 'I\'m making pizza and pasta'], ['Hojin is writing a song with a computer program.', true, '정답 ▶ T\n이유: I\'m writing a song with this computer program.', null, 'I\'m writing a song with this computer program'], ['Jacob wants to be a fashion model.', false, '정답 ▶ F\n이유: 모델이 아니라 패션 디자이너(a fashion designer)가 되고 싶어 해요.', null, 'I want to be a fashion designer']] },
    { type: 'mc', title: '알맞은 응답 고르기', guide: '대화의 흐름에 맞는 응답을 고르세요.', items: [
      { q: '다음 말에 이어질 응답으로 가장 알맞은 것은?<br><b>A: What do you want to be in the future?</b>', opts: ['I want to be a chef.', 'I\'m making pizza.', 'Yes, I do.', 'I like sports games.'], ex: '정답 ▶ I want to be a chef.\n이유: 장래 희망(What do you want to be ~?)을 물으면 \'I want to be + 직업\'으로 답해요.\n오답 ▶ Yes, I do.는 Do you ~? 질문의 대답' },
      { q: '다음 말에 이어질 응답으로 가장 알맞은 것은?<br><b>A: Do you want to be a songwriter?</b>', opts: ['Yes, I do.', 'Yes, I am.', 'No, I\'m not.', 'Yes, it does.'], ex: '정답 ▶ Yes, I do.\n이유: Do you ~?(일반동사 의문문)에는 Yes, I do. / No, I don\'t.로 답해요.' }
    ] },
    { type: 'mc', title: '일치·불일치', guide: '선택지는 본문을 어려운 어휘로 바꿔 쓴 문장이에요. 풀고 나서 해설의 어휘를 꼭 확인하세요.', items: [
      { box: ['7과 대화 1 · 스포츠 기자', '7과 대화 2 · 요리사', '7과 대화 3 · 작곡가', '7과 대화 4 · 패션 디자이너'], q: '대화의 내용과 일치하지 <u>않는</u> 것은?', opts: ['David wants to be a sports reporter.', 'Minsu is interested in all kinds of sports.', 'Hojin is writing a song with a computer program.', 'Jacob loves to make clothes.', 'Jacob will make clothes for the girl someday.'], ex: '정답 ▶ David wants to be a sports reporter.\n이유: 스포츠 기자가 꿈인 사람은 민수예요. David는 세계적으로 유명한 요리사(chef)가 되고 싶어 해요.', per: [['David는 스포츠 기자가 되고 싶어 한다.', 'I want to be a world-famous chef', '불일치 → 요리사'], ['민수는 모든 종류의 스포츠에 관심이 있다.', 'I\'m interested in all kinds of sports', '일치'], ['호진이는 컴퓨터 프로그램으로 노래를 만들고 있다.', 'I\'m writing a song with this computer program', '일치'], ['Jacob은 옷 만드는 것을 매우 좋아한다.', 'I love to make clothes', '일치'], ['Jacob은 언젠가 소녀에게 옷을 만들어 줄 것이다.', 'I\'ll make clothes for you someday', '일치']] }
    ] },
    { type: 'pick', title: '어법선택', guide: '어법상 알맞은 것을 고르세요.', items: [
      { s: 'Yes, I do. I\'m interested {in|on} all kinds of sports.', ex: '정답 ▶ in\n이유: be interested in ~ = ~에 관심이 있다 (짝꿍 전치사 in)' },
      { s: 'I\'m {making|make} pizza and pasta.', ex: '정답 ▶ making\n이유: 지금 하고 있는 일 → 현재진행형 be + -ing (I\'m making)' },
      { s: 'Yes, I\'m really interested in {writing|write} songs.', ex: '정답 ▶ writing\n이유: 전치사 in 뒤에는 동명사(-ing). be interested in -ing = ~하는 것에 관심이 있다' },
      { s: 'Thanks. I want {to be|being} a fashion designer. I\'ll make clothes for you someday.', ex: '정답 ▶ to be\n이유: want + to부정사 = ~하고 싶다. want 뒤에 -ing는 쓰지 않아요.' }
    ] },
    { type: 'scramble', title: '본문 스크램블', guide: '우리말에 맞게 단어를 눌러 문장을 완성하세요.', items: [
      { ko: '앞으로 무엇이 되고 싶니, 민수야?', en: 'What do you want to be in the future, Minsu?' }
    ] },
    { type: 'order', title: '문장순서', guide: '대화(문장)를 순서대로 눌러서 배열하세요.', items: [
      { lines: ['David, what are you making?', 'I\'m making pizza and pasta.', 'They look delicious. Are you interested in Italian food?', 'Yes, I am. I want to be a world-famous chef in the future!'], flow: ['G: 무엇을 만들고 있니?', 'B: 피자와 파스타', 'G: 맛있어 보여, 이탈리아 음식에 관심 있니?', 'B: 응, 요리사가 되고 싶어'] }
    ] },
    { type: 'blank', title: '빈칸추론', guide: '빈칸에 들어갈 말로 가장 알맞은 것을 고르세요.', items: [
      { s: 'What do you want to ____ in the future, Minsu?', opts: ['be', 'do', 'make', 'play'], ex: '정답 ▶ be\n이유: What do you want to be ~? = 무엇이 되고 싶니? (장래 희망 묻기)' }
    ] },
    { type: 'mc', title: '어색한 대화 고르기', guide: '짝지어진 대화 중 어색한 것을 고르세요.', items: [
      { q: '다음 중 짝지어진 대화가 <b>어색한</b> 것은?', opts: ['A: Are you interested in music? B: Yes, I do.', 'A: What are you interested in? B: I\'m interested in cooking.', 'A: What do you want to be? B: I want to be a pilot.', 'A: Why don\'t we play soccer? B: Sure. Sounds fun!'], ex: '정답 ▶ A: Are you interested in music? B: Yes, I do.\n이유: Are you ~? 질문이니 Yes, I am.으로 답해야 해요.' }
    ] },
    { type: 'mc', title: '의사소통 기능', guide: '상황에 맞는 표현을 고르세요.', items: [
      { q: '관심 있는 것을 묻는 표현으로 알맞은 것은?', opts: ['What are you interested in?', 'What do you want to be?', 'What are you making?', 'Why not?'], ex: '정답 ▶ What are you interested in?\n이유: 관심 묻기 = What are you interested in? / Are you interested in ~?\n대답 ▶ I\'m interested in + 명사/동명사' }
    ] },
    { type: 'mc', title: '요약문 완성', guide: '본문을 읽고 요약문의 빈칸 (A), (B)에 들어갈 말을 고르세요.', items: [
      { box: ['7과 대화 1 · 스포츠 기자', '7과 대화 2 · 요리사'], q: '다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 알맞은 것은?<br><b>Minsu wants to be a sports (A) ______, and David wants to be a world-famous (B) ______.</b>', opts: ['(A) reporter – (B) chef', '(A) chef – (B) reporter', '(A) player – (B) chef', '(A) reporter – (B) songwriter', '(A) designer – (B) pilot'], ex: '정답 ▶ (A) reporter – (B) chef\n(A) 민수: 스포츠 \'기자\' → reporter\n(B) David: 세계적으로 유명한 \'요리사\' → chef\n오답 ▶ player(선수): 민수는 경기를 많이 보지만 꿈은 기자예요.', ev: ['I want to be a sports reporter', 'I want to be a world-famous chef'] },
      { box: ['7과 대화 3 · 작곡가', '7과 대화 4 · 패션 디자이너'], q: '다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 알맞은 것은?<br><b>Hojin is interested in (A) ______ songs, and Jacob loves to (B) ______ clothes.</b>', opts: ['(A) writing – (B) make', '(A) singing – (B) make', '(A) writing – (B) buy', '(A) listening – (B) sell', '(A) singing – (B) wear'], ex: '정답 ▶ (A) writing – (B) make\n(A) 호진: 노래를 \'만드는(작곡하는)\' 것 → writing\n(B) Jacob: 옷을 \'만드는\' 것 → make\n오답 ▶ singing(노래 부르기)이 아니라 writing(작곡)이에요.', ev: ['I\'m really interested in writing songs', 'I love to make clothes'] }
    ] }
  ] },
  { id: 'c7b', name: 'DAY 6', range: '7과 대화문 ② 대화 5', story: 'Lesson 7 · 비행기 체험 (Watch, Answer, and Talk)', passage: [['#', '7과 대화 5 · 비행기 체험 (Watch, Answer, and Talk)', ''], ['G', 'Jiho, why don\'t we try this? We can fly an airplane!', '지호야, 우리 이거 한번 해 보는 게 어때? 우리는 비행기를 조종해 볼 수 있어!'], ['B', 'Sure. It looks like fun!', '물론이야. 재미있어 보인다!'], ['G', 'Do you want to be a pilot in the future?', '너는 앞으로 조종사가 되고 싶니?'], ['B', 'Yes, I\'m interested in flying airplanes. How about you, Lucy?', '응, 나는 비행기를 조종하는 것에 관심이 있어. 너는 어때, Lucy?'], ['G', 'I\'m interested in making airplanes, not flying. I want to be an airplane engineer.', '나는 비행기를 만드는 것에 관심이 있어, 조종하는 것 말고. 나는 비행기 엔지니어가 되고 싶어.'], ['B', 'That sounds cool!', '멋있다!'], ['G', 'Thank you. I want to make an airplane someday!', '고마워. 나는 언젠가 비행기를 만들고 싶어!'], ['B', 'Let\'s fly this airplane, and then we can try making an airplane, too.', '이 비행기를 조종해 보자, 그런 다음에 비행기를 만들어 볼 수도 있어.'], ['G', 'Good idea.', '좋은 생각이야.']], steps: [
    { type: 'vocab', title: '핵심어휘·숙어', quizN: 8, items: [['Why don\'t we ~?', '~하는 게 어때?'], ['fly', '(비행기를) 조종하다; 날다'], ['pilot', '조종사'], ['engineer', '엔지니어'], ['sound cool', '멋지게 들리다'], ['How about you?', '너는 어때?'], ['Let\'s ~', '~하자'], ['try -ing', '(시험 삼아) ~해 보다']] },
    { type: 'pick', title: '어휘선택', guide: '문맥에 맞는 낱말을 고르세요.', items: [
      { s: 'Do you want to be a {pilot|chef} in the future?', ex: '정답 ▶ pilot (조종사)\n오답 ▶ chef: 비행기를 조종해 볼 수 있다고 했으니 \'조종사\'가 되고 싶은지 물어요.' },
      { s: 'I\'m interested in making airplanes, not {flying|cooking}. I want to be an airplane engineer.', ex: '정답 ▶ flying (조종하는 것)\n오답 ▶ cooking: Lucy는 비행기를 \'조종하는 것\'이 아니라 \'만드는 것\'에 관심이 있어요.' }
    ] },
    { type: 'tf', title: 'T/F 내용 확인', guide: '본문 내용과 일치하면 T, 다르면 F를 고르세요.', items: [['Lucy wants to be a pilot.', false, '정답 ▶ F\n이유: 조종사가 되고 싶은 건 지호예요. Lucy는 비행기 엔지니어가 되고 싶어 해요.', null, 'I want to be an airplane engineer'], ['Jiho is interested in flying airplanes.', true, '정답 ▶ T\n이유: Yes, I\'m interested in flying airplanes.', null, 'I\'m interested in flying airplanes']] },
    { type: 'mc', title: '알맞은 응답 고르기', guide: '대화의 흐름에 맞는 응답을 고르세요.', items: [
      { q: '다음 말에 이어질 응답으로 가장 알맞은 것은?<br><b>A: Are you interested in Italian food?</b>', opts: ['Yes, I am.', 'Yes, I do.', 'No, I don\'t.', 'Yes, it is.'], ex: '정답 ▶ Yes, I am.\n이유: Are you ~?(be동사 의문문)에는 Yes, I am. / No, I\'m not.으로 답해요.\n오답 ▶ Yes, I do. / No, I don\'t.는 Do you ~? 질문의 대답' },
      { q: '다음 말에 이어질 응답으로 가장 알맞은 것은?<br><b>A: Why don\'t we try this? We can fly an airplane!</b>', opts: ['Sure. It looks like fun!', 'No, I\'m not.', 'I want to be a pilot.', 'Yes, I do.'], ex: '정답 ▶ Sure. It looks like fun!\n이유: Why don\'t we ~?(~하는 게 어때?)는 제안이에요. 수락은 Sure. / Good idea. / Sounds good.' }
    ] },
    { type: 'mc', title: '일치·불일치', guide: '선택지는 본문을 어려운 어휘로 바꿔 쓴 문장이에요. 풀고 나서 해설의 어휘를 꼭 확인하세요.', items: [
      { box: ['7과 대화 5 · 비행기 체험 (Watch, Answer, and Talk)'], q: '대화의 내용과 일치하지 <u>않는</u> 것은?', opts: ['Lucy wants to be a pilot.', 'Jiho is interested in flying airplanes.', 'Lucy wants to make an airplane someday.', 'They will fly an airplane first.', 'Jiho thinks Lucy\'s dream sounds cool.'], ex: '정답 ▶ Lucy wants to be a pilot.\n이유: 조종사(pilot)가 꿈인 사람은 지호예요. Lucy는 비행기 엔지니어가 되고 싶어 해요.', per: [['Lucy는 조종사가 되고 싶어 한다.', 'I want to be an airplane engineer', '불일치 → 엔지니어'], ['지호는 비행기 조종에 관심이 있다.', 'I\'m interested in flying airplanes', '일치'], ['Lucy는 언젠가 비행기를 만들고 싶어 한다.', 'I want to make an airplane someday', '일치'], ['그들은 먼저 비행기를 조종할 것이다.', 'Let\'s fly this airplane, and then', '일치'], ['지호는 Lucy의 꿈이 멋지다고 생각한다.', 'That sounds cool', '일치']] },
      { box: ['7과 대화 5 · 비행기 체험 (Watch, Answer, and Talk)'], q: '두 사람이 대화 직후에 할 일로 알맞은 것은?', opts: ['비행기 조종 체험하기', '비행기 만들기', '피자 만들기', '노래 만들기', '옷 만들기'], ex: '정답 ▶ 비행기 조종 체험하기\n이유: Let\'s fly this airplane, and then we can try making an airplane, too. → 먼저 조종(fly), 그다음에 만들기\n포인트 ▶ and then(그런 다음에) 앞뒤 순서 확인!', per: [['', 'Let\'s fly this airplane', '정답'], ['', 'and then we can try making an airplane', '✘ 그다음 할 일'], ['', '', '✘'], ['', '', '✘'], ['', '', '✘']] }
    ] },
    { type: 'pick', title: '어법선택', guide: '어법상 알맞은 것을 고르세요.', items: [
      { s: 'Jiho, why don\'t we {try|trying} this? We can fly an airplane!', ex: '정답 ▶ try\n이유: Why don\'t we + 동사원형 ~? = ~하는 게 어때?' }
    ] },
    { type: 'scramble', title: '본문 스크램블', guide: '우리말에 맞게 단어를 눌러 문장을 완성하세요.', items: [
      { ko: '너는 앞으로 조종사가 되고 싶니?', en: 'Do you want to be a pilot in the future?' },
      { ko: '나는 비행기를 만드는 것에 관심이 있어, 조종하는 것 말고.', en: 'I\'m interested in making airplanes, not flying.' }
    ] },
    { type: 'order', title: '문장순서', guide: '대화(문장)를 순서대로 눌러서 배열하세요.', items: [
      { lines: ['Jiho, why don\'t we try this? We can fly an airplane!', 'Sure. It looks like fun!', 'Do you want to be a pilot in the future?', 'Yes, I\'m interested in flying airplanes. How about you, Lucy?', 'I\'m interested in making airplanes, not flying. I want to be an airplane engineer.'], flow: ['G: 이거 해 보는 게 어때? 비행기 조종!', 'B: 물론, 재미있겠다', 'G: 조종사가 되고 싶니?', 'B: 응, 조종에 관심 있어. 너는?', 'G: 나는 만드는 것에 관심, 엔지니어가 꿈'] }
    ] },
    { type: 'blank', title: '빈칸추론', guide: '빈칸에 들어갈 말로 가장 알맞은 것을 고르세요.', items: [
      { s: 'I\'m interested in making airplanes, not flying. I want to be an airplane ____.', opts: ['engineer', 'pilot', 'chef', 'reporter'], ex: '정답 ▶ engineer\n이유: 비행기를 \'만드는 것\'에 관심 있으니 비행기 \'엔지니어\'. pilot은 조종하는 사람' },
      { s: 'Jiho, why don\'t we try this? We can fly an ____!', opts: ['airplane', 'car', 'bike', 'boat'], ex: '정답 ▶ airplane\n이유: fly(조종하다)할 수 있는 것은 비행기예요.' }
    ] },
    { type: 'mc', title: '어색한 대화 고르기', guide: '짝지어진 대화 중 어색한 것을 고르세요.', items: [
      { q: '다음 중 짝지어진 대화가 <b>어색한</b> 것은?', opts: ['A: What do you want to be in the future? B: I\'m making pizza.', 'A: Do you want to be a songwriter? B: Yes, I do.', 'A: What are you making? B: I\'m making a cake.', 'A: How about you? B: I want to be a chef.'], ex: '정답 ▶ A: What do you want to be in the future? B: I\'m making pizza.\n이유: 장래 희망을 물었는데 지금 만드는 음식을 말했어요. → I want to be a chef. 처럼 답해야 해요.' }
    ] },
    { type: 'mc', title: '의사소통 기능', guide: '상황에 맞는 표현을 고르세요.', items: [
      { q: '장래 희망을 묻는 표현이 <b>아닌</b> 것은?', opts: ['What are you good at?', 'What do you want to be in the future?', 'What do you want to do in the future?', 'What\'s your dream job?'], ex: '정답 ▶ What are you good at?\n이유: \'무엇을 잘하니?\'는 잘하는 것을 묻는 표현이에요. 나머지는 모두 장래 희망을 물어요.' }
    ] },
    { type: 'mc', title: '요약문 완성', guide: '본문을 읽고 요약문의 빈칸 (A), (B)에 들어갈 말을 고르세요.', items: [
      { n: null, box: ['7과 대화 5 · 비행기 체험 (Watch, Answer, and Talk)'], q: '다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 알맞은 것은?<br><b>Jiho is interested in (A) ______ airplanes, but Lucy wants to (B) ______ airplanes as an engineer.</b>', opts: ['(A) flying – (B) make', '(A) making – (B) fly', '(A) flying – (B) fly', '(A) selling – (B) buy', '(A) drawing – (B) clean'], ex: '정답 ▶ (A) flying – (B) make\n(A) 지호: 비행기 \'조종\'에 관심 → flying\n(B) Lucy: 비행기를 \'만드는\' 엔지니어 → make\n오답 ▶ 두 사람의 관심을 바꾼 ②에 주의!', ev: ['I\'m interested in flying airplanes', 'I\'m interested in making airplanes, not flying'] },
      { box: ['7과 대화 5 · 비행기 체험 (Watch, Answer, and Talk)'], q: '다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 알맞은 것은?<br><b>Jiho and Lucy will (A) ______ an airplane first, and then they will try (B) ______ one.</b>', opts: ['(A) fly – (B) making', '(A) make – (B) flying', '(A) fly – (B) drawing', '(A) buy – (B) selling', '(A) clean – (B) making'], ex: '정답 ▶ (A) fly – (B) making\n(A) 먼저 비행기를 \'조종\'해 보고 → fly\n(B) 그다음 비행기를 \'만들어\' 본다 → try making\n포인트 ▶ and then(그런 다음에) 앞이 먼저, 뒤가 나중!', ev: ['Let\'s fly this airplane, and then we can try making an airplane, too'] }
    ] }
  ] },
  { id: 'd3', name: 'DAY 7', range: '7과 본문 ❶❷❸', story: 'Lesson 7 · 감독 Jim · 야외 촬영 관리자 Anna · 촬영감독 Peter', passage: [['', '❶', ''], ['Jim Brown', 'Hi, I\'m Jim Brown, the director of Happy Days.', '안녕하세요, 나는 \'Happy Days\'의 감독 Jim Brown이에요.'], ['', 'It\'s a movie about the friendship between Tom and his dog Max.', '이것은 Tom과 그의 개 Max의 우정에 관한 영화예요.'], ['', 'A lot of people are working hard to create this movie.', '많은 사람들이 이 영화를 만들기 위해 열심히 일하고 있어요.'], ['', 'Do you want to meet some of them?', '그들 중 몇 명을 만나 보고 싶나요?'], ['', '❷', ''], ['Anna', 'I\'m Anna, and I found this beautiful beach.', '나는 Anna이고, 내가 이 아름다운 해변을 찾아냈어요.'], ['', 'I\'m a location manager, and my job is to find perfect places for shooting.', '나는 야외 촬영 관리자이고, 내 일은 촬영을 위한 완벽한 장소를 찾는 거예요.'], ['', 'Of course, it is not easy, but I love my job.', '물론, 이 일은 쉽지 않지만, 나는 내 일을 정말 좋아해요.'], ['', 'I like to travel and enjoy challenges.', '나는 여행하는 것을 좋아하고 도전을 즐겨요.'], ['', '❸', ''], ['Peter', 'I\'m Peter, the director of photography for this movie.', '나는 이 영화의 촬영감독인 Peter예요.'], ['', 'I\'m in charge of all the cameras.', '나는 모든 카메라를 담당하고 있어요.'], ['', 'Today, Tom and Max are going to play together with a ball on the beach.', '오늘, Tom과 Max는 해변에서 공을 가지고 함께 놀 예정이에요.'], ['', 'To capture their happy moments, I\'m going to use drones.', '그들의 행복한 순간을 포착하기 위해, 나는 드론을 사용할 거예요.']], steps: [
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
  { id: 'd4', name: 'DAY 8', range: '7과 본문 ❹❺❻', story: 'Lesson 7 · 동물 조련사 Jennifer · 영화 편집자 Emma · 폴리 아티스트 Chris', passage: [['', '❹', ''], ['Jennifer', 'I\'m Jennifer.', '나는 Jennifer예요.'], ['', 'I trained and took care of Max for a long time.', '나는 Max를 오랫동안 훈련하고 돌봤어요.'], ['', 'Max is a great actor, but he sometimes gets too excited when a lot of people are around.', 'Max는 훌륭한 배우이지만, 주변에 사람들이 많을 때 가끔 너무 흥분해요.'], ['', 'So, I use hand signals to calm him.', '그래서, 나는 그를 진정시키기 위해 수신호를 사용해요.'], ['', 'Who am I?', '나는 누구일까요?'], ['', 'I\'m an animal wrangler.', '나는 동물 조련사예요.'], ['', '❺', ''], ['Emma', 'My name is Emma, and I\'m a film editor.', '내 이름은 Emma이고, 나는 영화 편집자예요.'], ['', 'My work begins after the shooting is over.', '내 일은 촬영이 끝나고 나서 시작돼요.'], ['', 'To create a better story, I can change the order of scenes or delete some of them.', '더 좋은 이야기를 만들기 위해서, 나는 장면의 순서를 바꾸거나 장면 중 일부를 삭제할 수도 있어요.'], ['', 'Storytelling skills are important for my job, so I read a lot.', '내 직업상 스토리텔링 기술이 중요해서 나는 책을 많이 읽어요.'], ['', '❻', ''], ['Chris', 'I\'m Chris, and I\'m a Foley artist.', '나는 Chris이고, 폴리 아티스트예요.'], ['', 'I create sound effects in my studio when recording on location is not easy.', '나는 야외 촬영장에서 녹음하는 게 쉽지 않을 때 내 작업실에서 음향 효과를 만들어요.'], ['', 'Listen carefully.', '잘 들어 봐요.'], ['', 'Do you hear the sound of waves?', '파도 소리가 들리나요?'], ['', 'I made that sound with rice and a plastic container.', '나는 쌀과 플라스틱 통으로 그 소리를 만들었어요.'], ['', 'Doesn\'t it sound real?', '진짜처럼 들리지 않나요?']], steps: [
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
  { id: 'c5a', name: 'DAY 9', range: '5과 대화문 ① 대화 1~4', story: 'Lesson 5 · 허락 구하기 · 금지하기 · 대화 1~4', passage: [['#', '5과 대화 1 · 통화 금지', ''], ['W', 'Excuse me, but you must not talk on the phone here.', '실례합니다만, 여기서는 통화하시면 안 됩니다.'], ['B', 'I\'m terribly sorry. I\'ll turn off my phone.', '정말 죄송합니다. 휴대폰을 끌게요.'], ['W', 'You don\'t have to. Texting is OK.', '그럴 필요는 없어요. 문자하는 것은 괜찮아요.'], ['B', 'I see. Thank you.', '알겠습니다. 감사합니다.'], ['#', '5과 대화 2 · 만지기 금지', ''], ['G', 'Excuse me. May I touch this golden bear?', '실례합니다. 이 황금 곰을 만져 봐도 될까요?'], ['M', 'No, you may not. You must not touch anything in this room.', '아니요, 안 됩니다. 이 방에서는 어떤 것도 만지면 안 됩니다.'], ['G', 'OK, I understand.', '네, 알겠습니다.'], ['#', '5과 대화 3 · 뛰기 금지', ''], ['B', 'May I go to the video room, Mom?', '엄마, 비디오방에 가도 돼요?'], ['W', 'Of course, but don\'t run.', '물론이지, 하지만 뛰지는 마라.'], ['B', 'Why not?', '왜 안 돼요?'], ['W', 'Look at that sign. You must not run inside the museum.', '저 표지판을 보렴. 박물관 안에서 뛰면 안 된단다.'], ['#', '5과 대화 4 · 음식 금지', ''], ['B', 'May I take food into the museum?', '박물관에 음식을 가지고 들어가도 되나요?'], ['W', 'No, you may not. You must not bring any food inside.', '아니요, 안 됩니다. 어떤 음식도 내부로 가져오시면 안 됩니다.'], ['B', 'How about water?', '물은 어떤가요?'], ['W', 'Only bottled water is OK.', '병에 든 물만 괜찮습니다.']], steps: [
    { type: 'vocab', title: '핵심어휘·숙어', quizN: 12, items: [['must not', '~하면 안 된다'], ['talk on the phone', '통화하다'], ['terribly', '정말, 몹시'], ['turn off', '(전원을) 끄다'], ['don\'t have to', '~할 필요 없다'], ['text', '문자를 보내다'], ['May I ~?', '~해도 될까요?'], ['touch', '만지다'], ['golden', '황금의'], ['understand', '이해하다'], ['sign', '표지판'], ['inside', '~ 안에(서)'], ['bring', '가져오다'], ['How about ~?', '~은 어때요?'], ['bottled water', '병에 든 물'], ['look over here', '이쪽을 보다']] },
    { type: 'pick', title: '어휘선택', guide: '문맥에 맞는 낱말을 고르세요.', items: [
      { s: 'I\'m terribly sorry. I\'ll turn {off|on} my phone.', ex: '정답 ▶ off\n이유: 통화하면 안 된다는 말에 사과하며 휴대폰을 \'끈다(turn off)\'고 해요. turn on은 켜다' },
      { s: 'Look at that {sign|picture}. You must not run inside the museum.', ex: '정답 ▶ sign (표지판)\n오답 ▶ picture (그림): \'뛰지 마시오\' 같은 규칙은 \'표지판\'에 적혀 있어요.' },
      { s: 'Only {bottled|hot} water is OK.', ex: '정답 ▶ bottled (병에 든)\n오답 ▶ hot (뜨거운): 음식은 안 되지만 \'병에 든\' 물은 괜찮아요.' }
    ] },
    { type: 'tf', title: 'T/F 내용 확인', guide: '본문 내용과 일치하면 T, 다르면 F를 고르세요.', items: [['The boy can send text messages there.', true, '정답 ▶ T\n이유: Texting is OK. 문자하는 것은 괜찮아요.', null, 'Texting is OK'], ['The girl can touch the golden bear.', false, '정답 ▶ F\n이유: No, you may not. 이 방에서는 어떤 것도 만지면 안 돼요.', null, 'You must not touch anything in this room'], ['The boy can run inside the museum.', false, '정답 ▶ F\n이유: 박물관 안에서 뛰면 안 돼요(must not run).', null, 'You must not run inside the museum'], ['Visitors may bring bottled water into the museum.', true, '정답 ▶ T\n이유: Only bottled water is OK.', null, 'Only bottled water is OK']] },
    { type: 'mc', title: '알맞은 응답 고르기', guide: '대화의 흐름에 맞는 응답을 고르세요.', items: [
      { q: '다음 말에 이어질 응답으로 가장 알맞은 것은?<br><b>A: May I touch this golden bear?</b>', opts: ['No, you may not.', 'Yes, I may.', 'No, I don\'t.', 'Yes, it is.'], ex: '정답 ▶ No, you may not.\n이유: May I ~?(허락 구하기) → 수락 Yes, you may. / 거절 No, you may not.\n오답 ▶ Yes, I may.(주어가 you여야 해요)' },
      { q: '다음 말에 이어질 응답으로 가장 알맞은 것은?<br><b>A: May I go to the video room, Mom?</b>', opts: ['Of course, but don\'t run.', 'No, I may not.', 'I\'m sorry to hear that.', 'Yes, I do.'], ex: '정답 ▶ Of course, but don\'t run.\n이유: 허락(Of course) + 조건(but don\'t run). Of course = Yes, you may.' }
    ] },
    { type: 'mc', title: '일치·불일치', guide: '선택지는 본문을 어려운 어휘로 바꿔 쓴 문장이에요. 풀고 나서 해설의 어휘를 꼭 확인하세요.', items: [
      { box: ['5과 대화 1 · 통화 금지', '5과 대화 2 · 만지기 금지', '5과 대화 3 · 뛰기 금지', '5과 대화 4 · 음식 금지'], q: '대화의 내용과 일치하지 <u>않는</u> 것은?', opts: ['Visitors may bring any food into the museum.', 'Texting is OK there.', 'The girl must not touch the golden bear.', 'The boy may go to the video room.', 'Bottled water is OK in the museum.'], ex: '정답 ▶ Visitors may bring any food into the museum.\n이유: 어떤 음식도 가지고 들어오면 안 돼요(must not bring any food). 병에 든 물만 괜찮아요.', per: [['방문객은 어떤 음식이든 박물관에 가져와도 된다.', 'You must not bring any food inside', '불일치'], ['그곳에서 문자하는 것은 괜찮다.', 'Texting is OK', '일치'], ['소녀는 황금 곰을 만지면 안 된다.', 'You must not touch anything in this room', '일치'], ['소년은 비디오방에 가도 된다.', 'Of course, but don\'t run', '일치'], ['박물관에서 병에 든 물은 괜찮다.', 'Only bottled water is OK', '일치']] }
    ] },
    { type: 'pick', title: '어법선택', guide: '어법상 알맞은 것을 고르세요.', items: [
      { s: 'Excuse me, but you must not {talk|talking} on the phone here.', ex: '정답 ▶ talk\n이유: must not + 동사원형 = ~하면 안 된다 (금지)' },
      { s: 'You don\'t have to. {Texting|Text} is OK.', ex: '정답 ▶ Texting\n이유: \'문자하는 것은\'이 주어 → 동명사(-ing). 동사원형 Text는 주어 자리에 올 수 없어요.' },
      { s: 'Excuse me. May I {touch|touching} this golden bear?', ex: '정답 ▶ touch\n이유: May I + 동사원형 ~? = ~해도 될까요?' }
    ] },
    { type: 'scramble', title: '본문 스크램블', guide: '우리말에 맞게 단어를 눌러 문장을 완성하세요.', items: [
      { ko: '이 방에서는 어떤 것도 만지면 안 됩니다.', en: 'You must not touch anything in this room.' },
      { ko: '박물관 안에서 뛰면 안 된단다.', en: 'You must not run inside the museum.' }
    ] },
    { type: 'order', title: '문장순서', guide: '대화(문장)를 순서대로 눌러서 배열하세요.', items: [
      { lines: ['May I go to the video room, Mom?', 'Of course, but don\'t run.', 'Why not?', 'Look at that sign. You must not run inside the museum.'], flow: ['B: 비디오방에 가도 돼요?', 'W: 물론, 하지만 뛰지 마', 'B: 왜 안 돼요?', 'W: 표지판 봐, 뛰면 안 돼'] }
    ] },
    { type: 'blank', title: '빈칸추론', guide: '빈칸에 들어갈 말로 가장 알맞은 것을 고르세요.', items: [
      { s: 'You don\'t have to. ____ is OK.', opts: ['Texting', 'Talking', 'Eating', 'Running'], ex: '정답 ▶ Texting\n이유: 통화(talk)는 안 되지만 \'문자하는 것\'은 괜찮다고 해서 휴대폰을 끌 필요가 없어요.' },
      { s: 'No, you may not. You must not bring any ____ inside.', opts: ['food', 'books', 'friends', 'shoes'], ex: '정답 ▶ food\n이유: 음식을 가지고 들어가도 되냐는 질문에 \'어떤 음식도\' 안 된다고 답해요.' }
    ] },
    { type: 'mc', title: '어색한 대화 고르기', guide: '짝지어진 대화 중 어색한 것을 고르세요.', items: [
      { q: '다음 중 짝지어진 대화가 <b>어색한</b> 것은?', opts: ['A: May I sit here? B: Yes, I may.', 'A: May I use your pen? B: Sure, go ahead.', 'A: May I open the window? B: No, you may not. It\'s cold.', 'A: You must not eat here. B: Oh, I\'m sorry.'], ex: '정답 ▶ A: May I sit here? B: Yes, I may.\n이유: 허락해 줄 때는 Yes, you may.예요. (주어 you)' }
    ] },
    { type: 'mc', title: '의사소통 기능', guide: '상황에 맞는 표현을 고르세요.', items: [
      { q: '허락을 구하는 표현으로 알맞은 것은?', opts: ['May I use your phone?', 'You must not use your phone.', 'Don\'t use your phone.', 'Why not?'], ex: '정답 ▶ May I use your phone?\n이유: May I ~? / Can I ~? = ~해도 될까요? (허락 구하기)\n오답 ▶ must not, Don\'t ~는 금지하기' },
      { q: '밑줄 친 부분의 뜻으로 알맞은 것은?<br><b>B: I\'ll turn off my phone.<br>W: <u>You don\'t have to.</u> Texting is OK.</b>', opts: ['그럴 필요 없어요.', '그러면 안 돼요.', '그렇게 해야 해요.', '그렇게 해도 돼요.'], ex: '정답 ▶ 그럴 필요 없어요.\n이유: don\'t have to = ~할 필요가 없다 (금지가 아님!)\n비교 ▶ must not = ~하면 안 된다' }
    ] },
    { type: 'mc', title: '요약문 완성', guide: '본문을 읽고 요약문의 빈칸 (A), (B)에 들어갈 말을 고르세요.', items: [
      { box: ['5과 대화 1 · 통화 금지'], q: '다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 알맞은 것은?<br><b>The boy must not (A) ______ on the phone there, but (B) ______ is OK.</b>', opts: ['(A) talk – (B) texting', '(A) text – (B) talking', '(A) talk – (B) running', '(A) play – (B) eating', '(A) sing – (B) texting'], ex: '정답 ▶ (A) talk – (B) texting\n(A) \'통화하면\' 안 된다 → talk on the phone\n(B) \'문자하는 것\'은 괜찮다 → texting\n오답 ▶ ②는 반대로 바꾼 함정이에요.', ev: ['you must not talk on the phone here', 'Texting is OK'] },
      { box: ['5과 대화 3 · 뛰기 금지', '5과 대화 4 · 음식 금지'], q: '다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 알맞은 것은?<br><b>Inside the museum, you must not (A) ______ or bring any food, but (B) ______ water is OK.</b>', opts: ['(A) run – (B) bottled', '(A) walk – (B) bottled', '(A) run – (B) hot', '(A) sit – (B) cold', '(A) talk – (B) any'], ex: '정답 ▶ (A) run – (B) bottled\n(A) 박물관 안에서 \'뛰면\' 안 된다 → run\n(B) \'병에 든\' 물만 괜찮다 → bottled', ev: ['You must not run inside the museum', 'Only bottled water is OK'] }
    ] }
  ] },
  { id: 'c5b', name: 'DAY 10', range: '5과 대화문 ② 대화 5', story: 'Lesson 5 · 미술관에서 (Watch, Answer, and Talk)', passage: [['#', '5과 대화 5 · 미술관에서 (Watch, Answer, and Talk)', ''], ['M', 'Everybody, look over here, please. This is Sunflowers by Van Gogh.', '여러분, 이쪽을 봐 주세요. 이것은 반 고흐의 \'해바라기\'입니다.'], ['G', 'Wow, this is my favorite painting. May I take a picture of it?', '와, 제가 가장 좋아하는 그림이에요. 이 그림의 사진을 찍어도 될까요?'], ['M', 'Yes, you may, but you must not use the flash.', '네, 됩니다. 하지만 플래시를 사용하시면 안 됩니다.'], ['G', 'Why not? It\'s a little dark in here.', '왜 안 되나요? 여기는 좀 어두운데요.'], ['M', 'I\'m sorry, but using the flash can damage paintings.', '죄송하지만, 플래시를 사용하는 것은 그림들을 훼손할 수 있습니다.'], ['G', 'Oh, I didn\'t know that.', '아, 그건 몰랐어요.'], ['M', 'Everyone, we\'ll move on to Monet\'s paintings next.', '여러분, 우리는 다음에 모네의 그림으로 이동하겠습니다.'], ['G', 'Great!', '좋아요!']], steps: [
    { type: 'vocab', title: '핵심어휘·숙어', quizN: 6, items: [['favorite', '가장 좋아하는'], ['take a picture', '사진을 찍다'], ['flash', '(카메라) 플래시'], ['dark', '어두운'], ['damage', '손상시키다'], ['move on to', '~로 이동하다']] },
    { type: 'pick', title: '어휘선택', guide: '문맥에 맞는 낱말을 고르세요.', items: [
      { s: 'I\'m sorry, but using the flash can {damage|clean} paintings.', ex: '정답 ▶ damage (손상시키다)\n오답 ▶ clean (깨끗하게 하다): 플래시를 쓰면 안 되는 이유 → 그림을 \'훼손할\' 수 있어서' },
      { s: 'Why not? It\'s a little {dark|hot} in here.', ex: '정답 ▶ dark (어두운)\n오답 ▶ hot (더운): 플래시가 필요한 이유 → 안이 좀 \'어두워서\'' }
    ] },
    { type: 'tf', title: 'T/F 내용 확인', guide: '본문 내용과 일치하면 T, 다르면 F를 고르세요.', items: [['The girl can take a picture of the painting.', true, '정답 ▶ T\n이유: Yes, you may. 사진은 찍어도 돼요.', null, 'Yes, you may, but you must not use the flash'], ['The girl can use the flash.', false, '정답 ▶ F\n이유: 플래시는 사용하면 안 돼요(must not use the flash).', null, 'you must not use the flash']] },
    { type: 'mc', title: '알맞은 응답 고르기', guide: '대화의 흐름에 맞는 응답을 고르세요.', items: [
      { q: '다음 말에 이어질 응답으로 가장 알맞은 것은?<br><b>A: Excuse me, but you must not talk on the phone here.</b>', opts: ['I\'m terribly sorry.', 'You\'re welcome.', 'Yes, you may.', 'Good idea.'], ex: '정답 ▶ I\'m terribly sorry.\n이유: 금지(must not)를 들으면 사과하고 따르는 게 자연스러워요.' },
      { q: '다음 말에 이어질 응답으로 가장 알맞은 것은?<br><b>A: Why not? It\'s a little dark in here.</b>', opts: ['I\'m sorry, but using the flash can damage paintings.', 'Yes, you may.', 'Great!', 'Only bottled water is OK.'], ex: '정답 ▶ I\'m sorry, but using the flash can damage paintings.\n이유: Why not?(왜 안 되나요?)에는 \'이유\'로 답해요.' }
    ] },
    { type: 'mc', title: '일치·불일치', guide: '선택지는 본문을 어려운 어휘로 바꿔 쓴 문장이에요. 풀고 나서 해설의 어휘를 꼭 확인하세요.', items: [
      { box: ['5과 대화 5 · 미술관에서 (Watch, Answer, and Talk)'], q: '대화의 내용과 일치하지 <u>않는</u> 것은?', opts: ['The girl may use the flash.', 'Sunflowers is the girl\'s favorite painting.', 'It is a little dark in the room.', 'Using the flash can damage paintings.', 'They will see Monet\'s paintings next.'], ex: '정답 ▶ The girl may use the flash.\n이유: 사진은 찍어도 되지만 플래시는 사용하면 안 돼요(must not use the flash).', per: [['소녀는 플래시를 사용해도 된다.', 'you must not use the flash', '불일치'], ['\'해바라기\'는 소녀가 가장 좋아하는 그림이다.', 'this is my favorite painting', '일치'], ['방 안이 조금 어둡다.', 'It\'s a little dark in here', '일치'], ['플래시는 그림을 훼손할 수 있다.', 'using the flash can damage paintings', '일치'], ['다음에 모네의 그림을 볼 것이다.', 'we\'ll move on to Monet\'s paintings next', '일치']] },
      { box: ['5과 대화 5 · 미술관에서 (Watch, Answer, and Talk)'], q: '소녀가 플래시를 사용하면 안 되는 이유로 알맞은 것은?', opts: ['플래시가 그림을 훼손할 수 있어서', '방이 너무 밝아서', '미술관이 문을 닫아서', '카메라가 없어서', '사진 촬영이 금지라서'], ex: '정답 ▶ 플래시가 그림을 훼손할 수 있어서\n이유: I\'m sorry, but using the flash can damage paintings.\n오답 ▶ 사진 촬영 자체는 허락됐어요(Yes, you may).', per: [['', 'using the flash can damage paintings', '정답'], ['', 'It\'s a little dark in here', '✘ 오히려 어두움'], ['', '', '✘'], ['', '', '✘'], ['', 'Yes, you may', '✘ 사진은 됨']] }
    ] },
    { type: 'pick', title: '어법선택', guide: '어법상 알맞은 것을 고르세요.', items: [
      { s: 'Wow, this is my favorite painting. May I take a picture of {it|them}?', ex: '정답 ▶ it\n이유: 가리키는 것은 this painting(단수) → it' },
      { s: 'I\'m sorry, but {using|use} the flash can damage paintings.', ex: '정답 ▶ using\n이유: \'플래시를 사용하는 것은\'이 주어 → 동명사(-ing). 동사원형 use는 주어가 될 수 없어요.' }
    ] },
    { type: 'scramble', title: '본문 스크램블', guide: '우리말에 맞게 단어를 눌러 문장을 완성하세요.', items: [
      { ko: '이 그림의 사진을 찍어도 될까요?', en: 'May I take a picture of it?' }
    ] },
    { type: 'order', title: '문장순서', guide: '대화(문장)를 순서대로 눌러서 배열하세요.', items: [
      { lines: ['Everybody, look over here, please. This is Sunflowers by Van Gogh.', 'Wow, this is my favorite painting. May I take a picture of it?', 'Yes, you may, but you must not use the flash.', 'Why not? It\'s a little dark in here.'], flow: ['M: 이쪽을 보세요, 고흐의 해바라기', 'G: 사진 찍어도 될까요?', 'M: 네, 하지만 플래시는 안 돼요', 'G: 왜요? 어두운데요'] }
    ] },
    { type: 'blank', title: '빈칸추론', guide: '빈칸에 들어갈 말로 가장 알맞은 것을 고르세요.', items: [
      { s: 'Everyone, we\'ll move on to ____\'s paintings next.', opts: ['Monet', 'Van Gogh', 'Botero', 'Picasso'], ex: '정답 ▶ Monet\n이유: 고흐의 \'해바라기\' 다음에 \'모네\'의 그림으로 이동해요.' }
    ] },
    { type: 'mc', title: '어색한 대화 고르기', guide: '짝지어진 대화 중 어색한 것을 고르세요.', items: [
      { q: '다음 중 짝지어진 대화가 <b>어색한</b> 것은?', opts: ['A: Can I take pictures here? B: Yes, you must not.', 'A: May I come in? B: Of course.', 'A: Don\'t run here. B: OK, I won\'t.', 'A: How about water? B: Only bottled water is OK.'], ex: '정답 ▶ A: Can I take pictures here? B: Yes, you must not.\n이유: Yes(허락)와 must not(금지)이 서로 반대예요. Yes, you can. / No, you must not.처럼 말해야 해요.' }
    ] },
    { type: 'mc', title: '의사소통 기능', guide: '상황에 맞는 표현을 고르세요.', items: [
      { q: '빈칸에 들어갈 말로 알맞지 <b>않은</b> 것은?<br><b>A: May I eat snacks here?<br>B: ______ You must not eat in the library.</b>', opts: ['Sure, go ahead.', 'No, you may not.', 'I\'m sorry, but you can\'t.', 'No, you can\'t.'], ex: '정답 ▶ Sure, go ahead.\n이유: 뒤에 \'먹으면 안 된다(must not)\'가 오니 거절이 와야 해요. Sure, go ahead.는 허락이에요.' }
    ] },
    { type: 'mc', title: '요약문 완성', guide: '본문을 읽고 요약문의 빈칸 (A), (B)에 들어갈 말을 고르세요.', items: [
      { n: null, box: ['5과 대화 5 · 미술관에서 (Watch, Answer, and Talk)'], q: '다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 알맞은 것은?<br><b>In the museum, the girl may (A) ______ a picture of the painting, but she must not use the (B) ______.</b>', opts: ['(A) take – (B) flash', '(A) take – (B) phone', '(A) draw – (B) flash', '(A) sell – (B) camera', '(A) touch – (B) light'], ex: '정답 ▶ (A) take – (B) flash\n(A) 사진을 \'찍어도\' 된다 → take a picture\n(B) \'플래시\'는 안 된다 → flash', ev: ['May I take a picture of it', 'you must not use the flash'] },
      { box: ['5과 대화 5 · 미술관에서 (Watch, Answer, and Talk)'], q: '다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 알맞은 것은?<br><b>The girl must not use the flash because it can (A) ______ paintings, and next they will (B) ______ on to Monet\'s paintings.</b>', opts: ['(A) damage – (B) move', '(A) clean – (B) move', '(A) damage – (B) look', '(A) protect – (B) go', '(A) paint – (B) move'], ex: '정답 ▶ (A) damage – (B) move\n(A) 플래시는 그림을 \'훼손할\' 수 있다 → damage\n(B) 모네의 그림으로 \'이동한다\' → move on to\n오답 ▶ protect(보호하다)는 반대 뜻이에요.', ev: ['using the flash can damage paintings', 'we\'ll move on to Monet\'s paintings next'] }
    ] }
  ] },
  { id: 'L5a', name: 'DAY 11', range: '5과 본문 ❶❷', story: 'Lesson 5 · 모나리자에 케이크를 던진 사람 · 목격자 진술 1', passage: [['', '❶', ''], ['', 'Last Saturday, someone threw a cake at the Monalisa in the Botero Museum in Bogota, Colombia.', '지난 토요일, 누군가 콜롬비아 보고타의 보테로 박물관에 있는 \'모나리자\'에 케이크를 던졌다.'], ['', 'There were four eyewitnesses.', '네 명의 목격자가 있었다.'], ['', 'What did they say?', '그들은 뭐라고 말했을까?'], ['', 'Read the following, and find the criminal.', '다음을 읽고, 범인을 찾아보자.'], ['', '❷', ''], ['', 'Ann Jones, a visitor', 'Ann Jones, 방문객'], ['', 'I was looking at the Monalisa, and someone threw a cake at the painting.', '저는 \'모나리자\'를 보고 있었는데, 누군가 그 그림을 향해 케이크를 던졌어요.'], ['', 'I turned around and saw an old man.', '저는 뒤로 돌았고 한 노인을 봤어요.'], ['', 'He was standing in front of a wheelchair.', '그는 휠체어 앞에 서 있었어요.'], ['', 'I\'m about 170 cm tall, and he was a little taller than me.', '저는 키가 170cm 정도인데, 그는 저보다 조금 더 컸어요.'], ['', 'Carlos Diaz, a janitor', 'Carlos Diaz, 청소부'], ['', 'An old man with gray hair was running away, and something fell off his head.', '회색 머리의 한 노인이 도망가고 있었는데, 그의 머리에서 무언가 떨어졌어요.'], ['', 'It was his wig.', '그것은 그의 가발이었어요.'], ['', 'I ran after him, but I couldn\'t catch him.', '저는 그를 뒤쫓았지만, 잡을 수 없었어요.'], ['', 'He was faster than me.', '그는 저보다 더 빨랐거든요.'], ['', 'In fact, the old man was not old.', '사실, 그 노인은 나이 든 사람이 아니었어요.'], ['', 'He was a young man with long brown hair.', '그는 긴 갈색 머리의 젊은 남자였어요.']], steps: [
    { type: 'vocab', title: '핵심어휘·숙어', quizN: 15, items: [['last Saturday', '지난 토요일'], ['throw', '던지다 (throw - threw - thrown)'], ['eyewitness', '목격자'], ['the following', '다음 내용'], ['criminal', '범인'], ['visitor', '방문객'], ['turn around', '뒤돌아보다'], ['in front of', '~ 앞에'], ['wheelchair', '휠체어'], ['about', '대략, ~쯤'], ['a little', '조금'], ['janitor', '청소부'], ['gray', '회색의'], ['run away', '도망가다'], ['fall off', '~에서 떨어지다 (fall - fell - fallen)'], ['wig', '가발'], ['run after', '~을 뒤쫓다'], ['catch', '잡다'], ['in fact', '사실은'], ['young', '젊은']] },
    { type: 'pick', title: '어휘선택', guide: '문맥에 맞는 낱말을 고르세요.', items: [
      { s: 'There were four {eyewitnesses|criminals}.', ex: '정답 ▶ eyewitnesses (목격자들)\n오답 ▶ criminals (범인들): 뒤에 \'그들은 뭐라고 말했을까?\'가 나오고, 네 사람의 진술이 이어져요.' },
      { s: 'Read the following, and find the {criminal|painting}.', ex: '정답 ▶ criminal (범인)\n오답 ▶ painting: 진술을 읽고 \'범인\'을 찾아보는 추리 이야기예요.' },
      { s: 'He was standing in front of a {wheelchair|window}.', ex: '정답 ▶ wheelchair (휠체어)\n오답 ▶ window: 나중에 경비원이 그림 근처에서 \'휠체어\'를 발견해요.' },
      { s: 'He was {faster|slower} than me.', ex: '정답 ▶ faster (더 빠른)\n오답 ▶ slower: 뒤쫓았지만 \'잡을 수 없었던\' 이유 → 그가 더 빨라서' },
      { s: 'He was a {young|old} man with long brown hair.', ex: '정답 ▶ young (젊은)\n오답 ▶ old: 바로 앞 문장 \'그 노인은 사실 나이 든 사람이 아니었다\' → 가발을 쓴 \'젊은\' 남자' }
    ] },
    { type: 'tf', title: 'T/F 내용 확인', guide: '본문 내용과 일치하면 T, 다르면 F를 고르세요.', items: [['The Monalisa was in a museum in Colombia.', true, '정답 ▶ T\n이유: the Botero Museum in Bogota, Colombia', '❶', 'in the Botero Museum in Bogota, Colombia'], ['There were three eyewitnesses.', false, '정답 ▶ F\n이유: 목격자는 네 명(four eyewitnesses)이었어요.', '❶', 'There were four eyewitnesses'], ['Ann saw an old man in front of a wheelchair.', true, '정답 ▶ T\n이유: He was standing in front of a wheelchair.', '❷', 'He was standing in front of a wheelchair'], ['The man was shorter than Ann.', false, '정답 ▶ F\n이유: Ann보다 조금 더 컸어요(a little taller than me).', '❷', 'he was a little taller than me'], ['Carlos caught the man.', false, '정답 ▶ F\n이유: 뒤쫓았지만 잡을 수 없었어요(couldn\'t catch him).', '❷', 'I couldn\'t catch him'], ['The man was wearing a wig.', true, '정답 ▶ T\n이유: 머리에서 떨어진 것은 그의 가발(his wig)이었어요.', '❷', 'It was his wig']] },
    { type: 'mc', title: '일치·불일치', guide: '선택지는 본문을 어려운 어휘로 바꿔 쓴 문장이에요. 풀고 나서 해설의 어휘를 꼭 확인하세요.', items: [
      { n: '❷', box: ['❷'], q: '글의 내용과 일치하지 <u>않는</u> 것은?', opts: ['The man had short gray hair.', 'Ann was looking at the Monalisa.', 'Ann is about 170 cm tall.', 'Something fell off the man\'s head.', 'The man was faster than Carlos.'], ex: '정답 ▶ The man had short gray hair.\n이유: 회색 머리는 가발이었고, 실제로는 \'긴 갈색 머리(long brown hair)\'의 젊은 남자였어요.', per: [['그 남자는 짧은 회색 머리였다.', 'He was a young man with long brown hair', '불일치 → 긴 갈색 머리'], ['Ann은 \'모나리자\'를 보고 있었다.', 'I was looking at the Monalisa', '일치'], ['Ann의 키는 약 170cm이다.', 'I\'m about 170 cm tall', '일치'], ['남자의 머리에서 무언가 떨어졌다.', 'something fell off his head', '일치'], ['그 남자는 Carlos보다 빨랐다.', 'He was faster than me', '일치']] }
    ] },
    { type: 'pick', title: '어법선택', guide: '어법상 알맞은 것을 고르세요.', items: [
      { s: 'Read the following, and {find|found} the criminal.', ex: '정답 ▶ find\n이유: Read ~, and find ~. 앞의 Read처럼 명령문 → 동사원형 find' },
      { s: 'There {were|was} four eyewitnesses.', ex: '정답 ▶ were\n이유: 주어 four eyewitnesses(복수) → There were' },
      { s: 'I was {looking|look} at the Monalisa, and someone threw a cake at the painting.', ex: '정답 ▶ looking\n이유: was + -ing = 과거진행형 (~하고 있었다). 케이크가 날아온 그 순간 보고 \'있던\' 중' },
      { s: 'He was {standing|stand} in front of a wheelchair.', ex: '정답 ▶ standing\n이유: 과거진행형 was + -ing (서 있었다)' },
      { s: 'I\'m about 170 cm tall, and he was a little {taller|tallest} than me.', ex: '정답 ▶ taller\n이유: 두 사람 비교 + than → 비교급 taller (tall - taller - tallest)' },
      { s: 'I ran after him, but I {couldn\'t|can\'t} catch him.', ex: '정답 ▶ couldn\'t\n이유: 지난 일 → can의 과거형 could. couldn\'t = could not' },
      { s: 'He was a young man {with|in} long brown hair.', ex: '정답 ▶ with\n이유: with + 특징 = ~을 가진 (a man with long hair 긴 머리를 가진 남자)' }
    ] },
    { type: 'verb', title: '동사변형', guide: '( ) 안의 동사를 알맞은 형태로 바꿔 쓰세요.', items: [
      { s: 'An old man with gray hair was running away, and something ___ off his head.', v: 'fall', a: ['fell'], ex: '정답 ▶ fell\n이유: fall - fell - fallen (불규칙). fall off ~에서 떨어지다' },
      { s: 'I ___ after him, but I couldn\'t catch him.', v: 'run', a: ['ran'], ex: '정답 ▶ ran\n이유: run - ran - run (불규칙). run after ~을 뒤쫓다' },
      { s: 'I ___ around and saw an old man.', v: 'turn', a: ['turned'], ex: '정답 ▶ turned\n이유: 규칙 변화 turn + -ed. turn around 뒤돌아보다' },
      { s: 'What ___ they say?', v: 'do', a: ['did'], ex: '정답 ▶ did\n이유: 과거의 일을 묻는 일반동사 의문문 → What did + 주어 + 동사원형?' }
    ] },
    { type: 'error', title: '오류찾기', guide: '어법상 틀린 곳을 고르세요.', items: [
      { s: 'I\'m [[about]] 170 cm tall, and he was a little [[more tall]] than [[me]].', w: 1, fix: 'taller', ex: '틀린 곳 ▶ ② more tall → taller\n이유: 짧은 형용사의 비교급은 -er (tall → taller)\n나머지 ▶ ① about(대략) ✔ ③ than me ✔' },
      { s: 'It was his wig. I ran after him, but I couldn\'t [[catching]] him. He [[was]] faster than [[me]].', w: 0, fix: 'catch', ex: '틀린 곳 ▶ ① catching → catch\n이유: could(n\'t) + 동사원형\n나머지 ▶ ② was ✔ ③ me ✔' },
      { s: 'In fact, the old man [[were]] not old. He was a [[young]] man [[with]] long brown hair.', w: 0, fix: 'was', ex: '틀린 곳 ▶ ① were → was\n이유: 주어 the old man(단수) → was\n나머지 ▶ ② young ✔ ③ with(~을 가진) ✔' },
      { s: '[[Read]] the following, and [[finds]] the [[criminal]].', w: 1, fix: 'find', ex: '틀린 곳 ▶ ② finds → find\n이유: Read ~, and find ~. 명령문 두 개 → 둘 다 동사원형\n나머지 ▶ ① Read ✔ ③ criminal ✔' }
    ] },
    { type: 'scramble', title: '본문 스크램블', guide: '우리말에 맞게 단어를 눌러 문장을 완성하세요.', items: [
      { ko: '저는 뒤로 돌았고 한 노인을 봤어요.', en: 'I turned around and saw an old man.' },
      { ko: '그는 휠체어 앞에 서 있었어요.', en: 'He was standing in front of a wheelchair.' },
      { ko: '그는 저보다 더 빨랐거든요.', en: 'He was faster than me.' },
      { ko: '사실, 그 노인은 나이 든 사람이 아니었어요.', en: 'In fact, the old man was not old.' },
      { ko: '그는 긴 갈색 머리의 젊은 남자였어요.', en: 'He was a young man with long brown hair.' }
    ] },
    { type: 'order', title: '문장순서', guide: '문장을 본문 순서대로 눌러서 배열하세요.', items: [
      { lines: ['I was looking at the Monalisa, and someone threw a cake at the painting.', 'I turned around and saw an old man.', 'He was standing in front of a wheelchair.', 'I\'m about 170 cm tall, and he was a little taller than me.'], flow: ['모나리자를 보던 중 케이크가 날아옴', '돌아보니 노인이 있었음', '휠체어 앞에 서 있었음', '나보다 조금 컸음'] },
      { lines: ['An old man with gray hair was running away, and something fell off his head.', 'It was his wig.', 'I ran after him, but I couldn\'t catch him.', 'He was faster than me.'], flow: ['회색 머리 노인이 도망가다 무언가 떨어짐', '그것은 가발', '뒤쫓았지만 못 잡음', '그가 더 빨랐음'] }
    ] },
    { type: 'insert', title: '문장삽입', guide: '주어진 문장이 들어가기에 가장 알맞은 곳을 고르세요.', items: [
      { lines: ['An old man with gray hair was running away, and something fell off his head.', 'It was his wig.', 'I ran after him, but I couldn\'t catch him.'], given: 1, flow: ['노인의 머리에서 무언가 떨어짐', '그것(It)은 가발이었음', '뒤쫓았지만 못 잡음'], ex: '정답 ▶ ①\n이유: It은 바로 앞의 something(머리에서 떨어진 것)을 가리켜요.' },
      { lines: ['He was faster than me.', 'In fact, the old man was not old.', 'He was a young man with long brown hair.'], given: 1, flow: ['그가 더 빨랐음', '사실 그 노인은 나이 든 사람이 아니었음', '긴 갈색 머리의 젊은 남자였음'], ex: '정답 ▶ ①\n이유: \'노인이 아니었다\'고 먼저 말한 뒤, 실제 모습(젊은 남자)을 밝혀요.' }
    ] },
    { type: 'odd', title: '어색한 문장', guide: '글의 흐름과 관계없는 문장을 고르세요.', items: [
      { lines: ['I turned around and saw an old man.', 'He was standing in front of a wheelchair.', 'The old man was sitting in the wheelchair.', 'I\'m about 170 cm tall, and he was a little taller than me.'], odd: 2, ex: '정답 ▶ ③\n이유: 노인은 휠체어 \'앞에 서 있었어요(standing)\'. 휠체어에 앉아 있었다는 건 바로 앞 문장과 모순이에요.' },
      { lines: ['I ran after him, but I couldn\'t catch him.', 'He was faster than me.', 'The old man walked very slowly.', 'In fact, the old man was not old.'], odd: 2, ex: '정답 ▶ ③\n이유: 그는 Carlos보다 더 빨랐어요. \'아주 천천히 걸었다\'는 반대예요.' }
    ] },
    { type: 'blank', title: '빈칸추론', guide: '빈칸에 들어갈 말로 가장 알맞은 것을 고르세요.', items: [
      { s: 'Last Saturday, someone threw a ____ at the Monalisa in the Botero Museum in Bogota, Colombia.', opts: ['cake', 'ball', 'shoe', 'cup'], ex: '정답 ▶ cake\n이유: 경비원이 그림 곳곳에서 \'케이크\' 조각을 발견해요.' },
      { s: 'An old man with ____ hair was running away, and something fell off his head.', opts: ['gray', 'brown', 'black', 'red'], ex: '정답 ▶ gray\n이유: 도망가던 \'노인\'처럼 보이게 회색 머리 가발을 썼어요. 진짜 머리는 갈색이었죠.' },
      { s: 'He was a young man with long ____ hair.', opts: ['brown', 'gray', 'blond', 'red'], ex: '정답 ▶ brown\n이유: 가발이 벗겨진 진짜 모습 = 긴 \'갈색\' 머리의 젊은 남자 (범인 찾기의 단서!)' }
    ] },
    { type: 'mc', title: '핵심문법', guide: '알맞은 답을 고르세요.', items: [
      { q: '밑줄 친 부분의 뜻으로 알맞은 것은?<br><b><u>In fact</u>, the old man was not old.</b>', opts: ['사실은', '마침내', '예를 들어', '게다가'], ex: '정답 ▶ 사실은\n이유: in fact = 사실은. 앞에서 \'노인\'이라고 했는데 실제로는 아니었다고 바로잡아요.' },
      { q: '밑줄 친 <b>It</b>이 가리키는 것은?<br><b>Something fell off his head. <u>It</u> was his wig.</b>', opts: ['머리에서 떨어진 것', '그 그림', '휠체어', '케이크'], ex: '정답 ▶ 머리에서 떨어진 것\n이유: It은 바로 앞의 something을 가리켜요.' },
      { q: '다음 문장의 뜻으로 알맞은 것은?<br><b>I ran after him, but I couldn\'t catch him.</b>', opts: ['나는 그를 뒤쫓았지만, 잡을 수 없었다.', '나는 그에게서 도망쳤지만, 잡혔다.', '나는 그를 뒤쫓아 잡았다.', '나는 그를 기다렸지만, 오지 않았다.'], ex: '정답 ▶ 나는 그를 뒤쫓았지만, 잡을 수 없었다.\n이유: run after = 뒤쫓다 / couldn\'t = ~할 수 없었다' },
      { q: '밑줄 친 <b>with</b>와 쓰임이 <b>같은</b> 것은?<br><b>He was a young man <u>with</u> long brown hair.</b>', opts: ['a girl with blue eyes', 'I went there with my mom.', 'He cut it with a knife.', 'I agree with you.'], ex: '정답 ▶ a girl with blue eyes\n이유: \'~을 가진\'(특징)의 with. 파란 눈을 가진 소녀\n오답 ▶ ~와 함께 / ~으로(도구) / ~에게(동의)' },
      { q: '다음 질문에 알맞은 대답은?<br><b>Why couldn\'t Carlos catch the man?</b>', opts: ['Because the man was faster than him.', 'Because the man was in a wheelchair.', 'Because Carlos was sleeping.', 'Because the man was very old.'], ex: '정답 ▶ Because the man was faster than him.\n이유: He was faster than me. → 남자가 Carlos보다 더 빨랐어요.' }
    ] },
    { type: 'mc', title: '요약문 완성', guide: '본문을 읽고 요약문의 빈칸 (A), (B)에 들어갈 말을 고르세요.', items: [
      { n: '❷', box: ['❷'], q: '다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 알맞은 것은?<br><b>The man who threw the cake looked like an old man, but he was actually a (A) ______ man wearing a (B) ______.</b>', opts: ['(A) young – (B) wig', '(A) young – (B) hat', '(A) tall – (B) mask', '(A) old – (B) wig', '(A) short – (B) cap'], ex: '정답 ▶ (A) young – (B) wig\n(A) 사실 노인이 아니라 \'젊은\' 남자 → young\n(B) 머리에서 떨어진 것 = \'가발\' → wig', ev: ['He was a young man with long brown hair', 'It was his wig'] },
      { n: '❷', box: ['❷'], q: '다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 알맞은 것은?<br><b>Ann said the man was a little (A) ______ than 170 cm, and Carlos said the man was (B) ______ than him.</b>', opts: ['(A) taller – (B) faster', '(A) shorter – (B) faster', '(A) taller – (B) slower', '(A) shorter – (B) slower', '(A) older – (B) weaker'], ex: '정답 ▶ (A) taller – (B) faster\n(A) 170cm인 Ann보다 조금 \'더 큼\' → taller\n(B) Carlos보다 \'더 빨라서\' 못 잡음 → faster', ev: ['he was a little taller than me', 'He was faster than me'] }
    ] }
  ] },
  { id: 'L5b', name: 'DAY 12', range: '5과 본문 ❸❹', story: 'Lesson 5 · 목격자 진술 2 · 용의자 정보와 범인 찾기', passage: [['', '❸', ''], ['', 'Diego Perez, a guard', 'Diego Perez, 경비원'], ['', 'I went to the crime scene, and there were pieces of cake all over the painting.', '저는 범죄 현장에 갔는데, 그림 곳곳에 케이크 조각들이 있었어요.'], ['', 'There was also a wheelchair near the painting, and I found a cake box next to the wheelchair.', '그림 근처에 휠체어도 있었는데, 저는 휠체어 옆에서 케이크 상자를 발견했어요.'], ['', 'The box was from Camila\'s Bakery.', '그 상자는 Camila 빵집의 것이었어요.'], ['', 'Camila Santos, the owner of Camila\'s Bakery', 'Camila Santos, Camila 빵집 주인'], ['', 'Last Friday, a young man came in.', '지난 금요일, 한 젊은 남자가 들어왔어요.'], ['', 'I spoke to him in Spanish, but he didn\'t understand me.', '저는 그에게 스페인어로 말했지만, 그는 제 말을 이해하지 못했어요.'], ['', 'He spoke only English.', '그는 영어로만 말했어요.'], ['', 'We had a lot of different cakes, but he just wanted the smallest one.', '우리 가게에는 다양한 케이크가 많이 있었지만, 그는 단지 가장 작은 것을 원했어요.'], ['', 'We sold only one cake that day, so I remember him clearly.', '우리는 그날 케이크를 한 개만 팔아서, 저는 그를 똑똑히 기억해요.'], ['', 'Oh, he had blue eyes.', '아, 그는 파란색 눈을 가지고 있었어요.'], ['', '❹', ''], ['', 'Now, look at the information about the suspects.', '이제, 용의자들에 대한 정보를 보자.'], ['', 'Who threw the cake at the Monalisa?', '누가 \'모나리자\'에 케이크를 던졌을까?'], ['', 'Andres Lozano | Height: 176 cm | Hair: long, black | Languages: Spanish, English | Eyes: brown', 'Andres Lozano | 키: 176cm | 머리: 긴 검은색 | 언어: 스페인어, 영어 | 눈: 갈색'], ['', 'Larry Johnson | Height: 173 cm | Hair: long, brown | Languages: English | Eyes: blue', 'Larry Johnson | 키: 173cm | 머리: 긴 갈색 | 언어: 영어 | 눈: 파란색'], ['', 'Tim Baker | Height: 182 cm | Hair: long, brown | Languages: English | Eyes: green', 'Tim Baker | 키: 182cm | 머리: 긴 갈색 | 언어: 영어 | 눈: 초록색'], ['', 'Luca Ferez | Height: 166 cm | Hair: short, gray | Languages: Spanish | Eyes: blue', 'Luca Ferez | 키: 166cm | 머리: 짧은 회색 | 언어: 스페인어 | 눈: 파란색']], steps: [
    { type: 'vocab', title: '핵심어휘·숙어', quizN: 15, items: [['guard', '경비원'], ['crime scene', '범죄 현장'], ['piece', '조각'], ['all over', '~ 곳곳에'], ['near', '~ 근처에'], ['find', '발견하다 (find - found - found)'], ['next to', '~ 옆에'], ['bakery', '빵집'], ['owner', '주인'], ['come in', '들어오다'], ['speak', '말하다 (speak - spoke - spoken)'], ['Spanish', '스페인어'], ['understand', '이해하다'], ['different', '다양한'], ['sell', '팔다 (sell - sold - sold)'], ['remember', '기억하다'], ['clearly', '분명히, 똑똑히'], ['information', '정보'], ['suspect', '용의자'], ['height', '키'], ['language', '언어']] },
    { type: 'pick', title: '어휘선택', guide: '문맥에 맞는 낱말을 고르세요.', items: [
      { s: 'I went to the crime scene, and there were {pieces|boxes} of cake all over the painting.', ex: '정답 ▶ pieces (조각들)\n오답 ▶ boxes (상자들): 그림에 던진 케이크 \'조각들\'이 곳곳에 묻어 있었어요. 상자는 하나(a cake box)예요.' },
      { s: 'There was also a wheelchair near the painting, and I found a cake box {next to|far from} the wheelchair.', ex: '정답 ▶ next to (~ 옆에)\n오답 ▶ far from (~에서 멀리): 휠체어 \'옆에서\' 케이크 상자를 발견했어요.' },
      { s: 'Last Friday, a young man came {in|out}.', ex: '정답 ▶ in\n이유: 빵집 주인의 말 → 남자가 가게에 \'들어왔다(came in)\'' },
      { s: 'I spoke to him in Spanish, but he didn\'t {understand|remember} me.', ex: '정답 ▶ understand (이해하다)\n오답 ▶ remember: 스페인어로 말했는데 \'알아듣지 못했다\' → 영어만 했으니까요.' },
      { s: 'We sold only one cake that day, so I remember him {clearly|badly}.', ex: '정답 ▶ clearly (똑똑히)\n오답 ▶ badly: 그날 케이크를 하나만 팔아서 그를 \'똑똑히\' 기억해요.' }
    ] },
    { type: 'tf', title: 'T/F 내용 확인', guide: '본문 내용과 일치하면 T, 다르면 F를 고르세요.', items: [['The guard found pieces of cake on the painting.', true, '정답 ▶ T\n이유: there were pieces of cake all over the painting', '❸', 'there were pieces of cake all over the painting'], ['The cake box was from Ann\'s Bakery.', false, '정답 ▶ F\n이유: 케이크 상자는 Ann\'s Bakery가 아니라 Camila\'s Bakery의 것이었어요. Ann은 그림을 보던 방문객이에요.', '❸', 'The box was from Camila\'s Bakery'], ['The young man spoke Spanish well.', false, '정답 ▶ F\n이유: 스페인어를 알아듣지 못했고 영어로만 말했어요.', '❸', 'He spoke only English'], ['The young man bought the smallest cake.', true, '정답 ▶ T\n이유: he just wanted the smallest one', '❸', 'he just wanted the smallest one'], ['The bakery sold many cakes that day.', false, '정답 ▶ F\n이유: 그날 케이크를 한 개만(only one) 팔았어요.', '❸', 'We sold only one cake that day']] },
    { type: 'mc', title: '일치·불일치', guide: '선택지는 본문을 어려운 어휘로 바꿔 쓴 문장이에요. 풀고 나서 해설의 어휘를 꼭 확인하세요.', items: [
      { n: '❹', box: ['❷', '❸', '❹'], q: 'Who threw the cake at the Monalisa? (진술과 용의자 정보를 비교해 범인을 고르세요.)', opts: ['Larry Johnson', 'Andres Lozano', 'Tim Baker', 'Luca Ferez'], ex: '정답 ▶ Larry Johnson\n단서 ① 키: 170cm인 Ann보다 \'조금\' 큼 → 173cm (182cm는 너무 큼, 166cm는 더 작음)\n단서 ② 머리: 회색은 가발, 진짜는 긴 갈색 머리\n단서 ③ 언어: 스페인어를 못하고 영어만 함\n단서 ④ 눈: 파란색\n→ 네 가지가 모두 맞는 사람은 Larry Johnson\n오답 ▶ Andres(검은 머리, 스페인어 함) / Tim(182cm, 초록 눈) / Luca(166cm, 스페인어만)', per: [['범인', ['he was a little taller than me', 'He spoke only English', 'he had blue eyes'], '173cm · 긴 갈색 머리 · 영어 · 파란 눈'], ['', 'Andres Lozano | Height: 176 cm', '✘ 검은 머리, 스페인어도 함, 갈색 눈'], ['', 'Tim Baker | Height: 182 cm', '✘ 너무 큼, 초록 눈'], ['', 'Luca Ferez | Height: 166 cm', '✘ 170보다 작음, 짧은 회색 머리, 스페인어만']] }
    ] },
    { type: 'pick', title: '어법선택', guide: '어법상 알맞은 것을 고르세요.', items: [
      { s: 'I went to the crime scene, and there {were|was} pieces of cake all over the painting.', ex: '정답 ▶ were\n이유: 주어 pieces of cake(복수) → there were' },
      { s: 'I spoke to him in Spanish, but he {didn\'t|doesn\'t} understand me.', ex: '정답 ▶ didn\'t\n이유: 과거의 부정 → didn\'t + 동사원형' },
      { s: 'We had a lot of different cakes, but he just wanted the {smallest|smaller} one.', ex: '정답 ▶ smallest\n이유: 많은 케이크 중에서 가장 → 최상급 the smallest' },
      { s: 'We sold only one cake that day, {so|but} I remember him clearly.', ex: '정답 ▶ so\n이유: 하나만 팔았다(원인) → 그래서 똑똑히 기억한다(결과) → so' },
      { s: 'Who {threw|did throw} the cake at the Monalisa?', ex: '정답 ▶ threw\n이유: 의문사 Who가 주어일 때는 do/did 없이 \'Who + 동사\'로 물어요.' }
    ] },
    { type: 'verb', title: '동사변형', guide: '( ) 안의 동사를 알맞은 형태로 바꿔 쓰세요.', items: [
      { s: 'He ___ only English.', v: 'speak', a: ['spoke'], ex: '정답 ▶ spoke\n이유: speak - spoke - spoken (불규칙)' },
      { s: 'We ___ only one cake that day, so I remember him clearly.', v: 'sell', a: ['sold'], ex: '정답 ▶ sold\n이유: sell - sold - sold (불규칙)' },
      { s: 'We had a lot of different cakes, but he just ___ the smallest one.', v: 'want', a: ['wanted'], ex: '정답 ▶ wanted\n이유: 규칙 변화 want + -ed. 지난 금요일의 일이라 과거형' }
    ] },
    { type: 'error', title: '오류찾기', guide: '어법상 틀린 곳을 고르세요.', items: [
      { s: 'There [[were]] also a wheelchair near the painting, and I found a cake box [[next]] to the [[wheelchair]].', w: 0, fix: 'was', ex: '틀린 곳 ▶ ① were → was\n이유: 주어 a wheelchair(단수) → There was\n나머지 ▶ ② next to ✔ ③ wheelchair ✔' },
      { s: 'I spoke to him [[in]] Spanish, but he [[didn\'t]] [[understood]] me.', w: 2, fix: 'understand', ex: '틀린 곳 ▶ ③ understood → understand\n이유: didn\'t + 동사원형\n나머지 ▶ ① in + 언어(~어로) ✔ ② didn\'t ✔' },
      { s: 'We had a lot of [[different]] cakes, but he just wanted the [[small]] [[one]].', w: 1, fix: 'smallest', ex: '틀린 곳 ▶ ② small → smallest\n이유: the + 최상급 → the smallest one(가장 작은 것)\n나머지 ▶ ① different ✔ ③ one(= cake) ✔' },
      { s: 'Now, [[looks]] at the [[information]] about the [[suspects]].', w: 0, fix: 'look', ex: '틀린 곳 ▶ ① looks → look\n이유: 주어 없이 시작하는 명령문 → 동사원형\n나머지 ▶ ② information ✔ ③ suspects ✔' }
    ] },
    { type: 'scramble', title: '본문 스크램블', guide: '우리말에 맞게 단어를 눌러 문장을 완성하세요.', items: [
      { ko: '그 상자는 Camila 빵집의 것이었어요.', en: 'The box was from Camila\'s Bakery.' },
      { ko: '지난 금요일, 한 젊은 남자가 들어왔어요.', en: 'Last Friday, a young man came in.' },
      { ko: '이제, 용의자들에 대한 정보를 보자.', en: 'Now, look at the information about the suspects.' },
      { ko: '누가 \'모나리자\'에 케이크를 던졌을까?', en: 'Who threw the cake at the Monalisa?' }
    ] },
    { type: 'order', title: '문장순서', guide: '문장을 본문 순서대로 눌러서 배열하세요.', items: [
      { lines: ['I went to the crime scene, and there were pieces of cake all over the painting.', 'There was also a wheelchair near the painting, and I found a cake box next to the wheelchair.', 'The box was from Camila\'s Bakery.'], flow: ['범죄 현장, 그림 곳곳에 케이크 조각', '휠체어 옆에서 케이크 상자 발견', '상자는 Camila 빵집 것'] },
      { lines: ['Last Friday, a young man came in.', 'I spoke to him in Spanish, but he didn\'t understand me.', 'He spoke only English.', 'We had a lot of different cakes, but he just wanted the smallest one.'], flow: ['지난 금요일 젊은 남자가 들어옴', '스페인어를 못 알아들음', '영어만 함', '가장 작은 케이크를 원함'] }
    ] },
    { type: 'insert', title: '문장삽입', guide: '주어진 문장이 들어가기에 가장 알맞은 곳을 고르세요.', items: [
      { lines: ['I went to the crime scene, and there were pieces of cake all over the painting.', 'There was also a wheelchair near the painting, and I found a cake box next to the wheelchair.', 'The box was from Camila\'s Bakery.'], given: 1, flow: ['그림 곳곳에 케이크 조각', '휠체어 옆에서 케이크 상자 발견', '그 상자(The box)는 Camila 빵집 것'], ex: '정답 ▶ ①\n이유: The box는 바로 앞의 a cake box를 가리켜요. 상자를 발견한 문장이 먼저 와야 해요.' },
      { lines: ['We had a lot of different cakes, but he just wanted the smallest one.', 'We sold only one cake that day, so I remember him clearly.', 'Oh, he had blue eyes.'], given: 1, flow: ['가장 작은 케이크를 원함', '한 개만 팔아서 똑똑히 기억함', '아, 파란 눈이었어요'], ex: '정답 ▶ ①\n이유: \'똑똑히 기억한다\'는 말 다음에 기억나는 특징(파란 눈)을 덧붙여요.' }
    ] },
    { type: 'odd', title: '어색한 문장', guide: '글의 흐름과 관계없는 문장을 고르세요.', items: [
      { lines: ['I went to the crime scene, and there were pieces of cake all over the painting.', 'There was also a wheelchair near the painting, and I found a cake box next to the wheelchair.', 'The guard didn\'t find anything at the crime scene.', 'The box was from Camila\'s Bakery.'], odd: 2, ex: '정답 ▶ ③\n이유: 경비원은 케이크 조각, 휠체어, 케이크 상자를 발견했어요.' },
      { lines: ['Last Friday, a young man came in.', 'I spoke to him in Spanish, but he didn\'t understand me.', 'The young man spoke Spanish very well.', 'He spoke only English.'], odd: 2, ex: '정답 ▶ ③\n이유: 그는 스페인어를 이해하지 못하고 영어만 했어요.' }
    ] },
    { type: 'blank', title: '빈칸추론', guide: '빈칸에 들어갈 말로 가장 알맞은 것을 고르세요.', items: [
      { s: 'The box was from Camila\'s ____.', opts: ['Bakery', 'Museum', 'School', 'Restaurant'], ex: '정답 ▶ Bakery\n이유: 케이크 상자의 출처 → Camila \'빵집\'. 다음 진술자도 빵집 주인이에요.' },
      { s: 'He spoke only ____.', opts: ['English', 'Spanish', 'French', 'Korean'], ex: '정답 ▶ English\n이유: 스페인어를 못 알아듣고 \'영어\'로만 말했어요. (범인 단서!)' },
      { s: 'Oh, he had ____ eyes.', opts: ['blue', 'brown', 'green', 'black'], ex: '정답 ▶ blue\n이유: 빵집 주인이 기억한 마지막 단서 = \'파란\' 눈' }
    ] },
    { type: 'mc', title: '핵심문법', guide: '알맞은 답을 고르세요.', items: [
      { q: '밑줄 친 <b>one</b>이 가리키는 것은?<br><b>We had a lot of different cakes, but he just wanted the smallest <u>one</u>.</b>', opts: ['cake', 'man', 'box', 'bakery'], ex: '정답 ▶ cake\n이유: one은 앞에 나온 명사(cake)를 반복하지 않으려고 쓴 말이에요. the smallest one = 가장 작은 케이크' },
      { q: '밑줄 친 <b>so</b>의 뜻으로 알맞은 것은?<br><b>We sold only one cake that day, <u>so</u> I remember him clearly.</b>', opts: ['그래서', '그러나', '왜냐하면', '또는'], ex: '정답 ▶ 그래서\n이유: 원인(한 개만 팔았다) → 결과(똑똑히 기억한다)' },
      { q: '의문문이 바르게 쓰인 것은?', opts: ['Who threw the cake?', 'Who did threw the cake?', 'Who did the cake throw?', 'Who throw did the cake?'], ex: '정답 ▶ Who threw the cake?\n이유: 의문사 Who가 주어 → \'Who + 동사(과거형) ~?\' (did를 쓰지 않아요)' },
      { q: '빈칸에 알맞은 것은?<br><b>I spoke to him ______ Spanish.</b>', opts: ['in', 'by', 'on', 'at'], ex: '정답 ▶ in\n이유: in + 언어 = ~어로 (in English, in Korean)' }
    ] },
    { type: 'mc', title: '요약문 완성', guide: '본문을 읽고 요약문의 빈칸 (A), (B)에 들어갈 말을 고르세요.', items: [
      { n: '❸', box: ['❸'], q: '다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 알맞은 것은?<br><b>The owner of Camila\'s Bakery said a young man who spoke only (A) ______ bought the (B) ______ cake.</b>', opts: ['(A) English – (B) smallest', '(A) Spanish – (B) smallest', '(A) English – (B) biggest', '(A) Spanish – (B) biggest', '(A) Korean – (B) sweetest'], ex: '정답 ▶ (A) English – (B) smallest\n(A) 스페인어를 못 알아듣고 \'영어\'만 → English\n(B) \'가장 작은\' 케이크를 원함 → smallest', ev: ['He spoke only English', 'he just wanted the smallest one'] },
      { n: '❹', box: ['❷', '❸', '❹'], q: '다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 알맞은 것은?<br><b>The criminal was a little taller than 170 cm, had long (A) ______ hair and blue eyes, and spoke only English, so he was (B) ______.</b>', opts: ['(A) brown – (B) Larry Johnson', '(A) brown – (B) Tim Baker', '(A) black – (B) Andres Lozano', '(A) gray – (B) Luca Ferez', '(A) black – (B) Larry Johnson'], ex: '정답 ▶ (A) brown – (B) Larry Johnson\n(A) 진짜 머리는 긴 \'갈색\' → brown (회색은 가발)\n(B) 173cm · 긴 갈색 머리 · 영어만 · 파란 눈 → Larry Johnson', ev: ['He was a young man with long brown hair', 'Larry Johnson | Height: 173 cm'] }
    ] }
  ] }
  ]
};
