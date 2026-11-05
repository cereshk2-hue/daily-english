N=32
MC=[
 dict(q="글의 내용과 <u>일치하는</u> 것은?",opts=[
  "Adenosine is gradually broken down by the body during sleep.",
  "Adenosine levels drop the longer we remain awake.",
  "Postponing sleep permanently reduces our need for rest.",
  "A sleep debt is repaid by staying awake longer than normal.",
  "Adenosine is the only factor responsible for our drive to sleep."],
  ex="정답 ▶ Adenosine is gradually broken down by the body during sleep.\n이유: While you sleep, your body breaks down the adenosine. 자는 동안 분해돼요.\n오답 ▶ ② 깨어 있을수록 '쌓여요(builds up)' ③ 결국 잠을 자게 돼요(forced to get some sleep) ④ 더 '오래 자서' 갚아요 ⑤ in part(부분적으로) + other factors(다른 요인들)\n포인트 ▶ drop 떨어지다 ↔ build up 쌓이다 · postpone = put off 미루다 · repay 갚다 = make up 보충하다",
  per=[["아데노신은 잠자는 동안 몸에 의해 점차 분해된다.","your body breaks down the adenosine","일치 ✔"],
       ["깨어 있는 시간이 길수록 아데노신 수치가 떨어진다.","builds up in your blood as time awake increases","drop(떨어지다) ↔ build up(쌓이다)"],
       ["잠을 미루면 휴식 욕구가 영원히 줄어든다.","you are forced to get some sleep","postpone = put off. 결국 잠을 자게 됨"],
       ["수면 빚은 평소보다 더 오래 깨어 있으면 갚아진다.","make up by sleeping longer than normal","staying awake ↔ sleeping longer"],
       ["아데노신이 수면 욕구의 유일한 원인이다.","due, in part, to a compound","in part(부분적으로)·other factors → only(유일한) ✗"]]),
 dict(q="글의 내용과 일치하지 <u>않는</u> 것은?",opts=[
  "Our bodies can gradually adjust to getting less sleep than they require.",
  "Adenosine partly accounts for our daily urge to sleep.",
  "The body may rely on adenosine to monitor how much sleep it has missed.",
  "Several nights of insufficient sleep can lead to a sleep debt.",
  "People sometimes delay sleep to fit more activities into their day."],
  ex="정답 ▶ Our bodies can gradually adjust to getting less sleep than they require.\n이유: you can't become accustomed to getting less sleep than your body needs. 적게 자는 데 익숙해질 수 '없어요'.\n오답 ▶ 나머지는 모두 본문을 다른 어휘로 바꿔 쓴 일치 문장이에요.\n포인트 ▶ adjust to = become accustomed to 적응하다 · account for = be due to ~의 원인이 되다 · urge = drive 욕구 · monitor = keep track of · insufficient = less than optimal · delay = put off · fit A into B = squeeze A into B",
  per=[["우리 몸은 필요보다 적게 자는 것에 점차 적응할 수 있다.","you can't become accustomed to getting less sleep","adjust to = become accustomed to → can't ✗"],
       ["아데노신이 매일의 수면 욕구를 부분적으로 설명해 준다.","due, in part, to a compound known as adenosine","partly = in part · account for = be due to · urge = drive"],
       ["몸은 놓친 잠의 양을 파악하는 데 아데노신에 의존할 수 있다.","to keep track of lost sleep","monitor = keep track of · missed = lost"],
       ["며칠 밤 잠이 부족하면 수면 빚이 생길 수 있다.","after several nights of less than optimal amounts of sleep","insufficient(불충분한) = less than optimal"],
       ["사람들은 하루에 더 많은 활동을 넣으려고 잠을 미루기도 한다.","put off going to sleep in order to squeeze more activities into your day","delay = put off · fit into = squeeze into"]]),
 dict(q="글의 내용과 <u>일치하는</u> 것은?",opts=[
  "수면 빚은 평소보다 더 오래 자야 갚을 수 있다.",
  "아데노신은 잠을 자는 동안 혈액 속에 쌓인다.",
  "충분히 연습하면 적게 자는 것에 익숙해질 수 있다.",
  "아데노신은 수면 욕구의 유일한 원인이다.",
  "잠을 미룰수록 수면 욕구는 점점 약해진다."],
  ex="정답 ▶ 수면 빚은 평소보다 더 오래 자야 갚을 수 있다.\n이유: a sleep debt that you must make up by sleeping longer than normal\n오답 ▶ ② 쌓이는 건 '깨어 있는 동안(as time awake increases)', 자는 동안엔 분해(break down) ③ can't become accustomed ④ in part(부분적으로) ⑤ 결국 압도적이 됨(overwhelming)\n포인트 ▶ make up 보충하다 · break down 분해하다 · overwhelming 압도적인",
  per=[["","make up by sleeping longer than normal","일치 ✔ make up 보충하다"],
       ["","While you sleep, your body breaks down the adenosine","자는 동안에는 분해(break down)"],
       ["","you can't become accustomed to getting less sleep","익숙해질 수 없다"],
       ["","due, in part, to a compound","in part = 부분적으로"],
       ["","your need for sleep becomes overwhelming","약해지는 게 아니라 압도적이 됨"]])]
TF=[
 ["Our need for sleep eventually becomes too strong to resist.",True,"정답 ▶ T\n이유: 결국 잠에 대한 필요가 압도적이 돼요.\n어휘 ▶ too strong to resist 저항할 수 없을 만큼 강한 = overwhelming","eventually your need for sleep becomes overwhelming"],
 ["Adenosine is a substance that decreases as we stay awake longer.",False,"정답 ▶ F\n이유: 깨어 있는 시간이 늘수록 '쌓여요(builds up)'.\n어휘 ▶ substance 물질 = compound, chemical · decrease 줄다 ↔ build up 쌓이다","builds up in your blood as time awake increases"],
 ["The body may use adenosine as a signal to bring on sleep.",True,"정답 ▶ T\n이유: 필요할 때 잠을 유발하는(trigger) 데 쓰일 수 있어요.\n어휘 ▶ bring on = trigger 일으키다, 유발하다","to trigger sleep when needed"],
 ["Adenosine alone fully explains why we build up a sleep debt.",False,"정답 ▶ F\n이유: 아데노신 '과 다른 요인들'의 축적이 설명해 줄 수 있다고 했어요. 혼자서 완전히 설명하는 게 아니에요.\n어휘 ▶ alone 단독으로 · fully 완전히","An accumulation of adenosine and other factors"],
 ["To pay back a sleep debt, we need to sleep more than usual.",True,"정답 ▶ T\n이유: 평소보다 더 오래 자서 보충해야(make up) 해요.\n어휘 ▶ pay back 갚다 = make up · more than usual = longer than normal","make up by sleeping longer than normal"],
 ["Not getting enough sleep will sooner or later affect us.",True,"정답 ▶ T\n이유: 결국 수면 부족은 우리를 따라잡아요(catches up with you) = 결국 영향을 미쳐요.\n어휘 ▶ sooner or later 조만간, 결국 = eventually · catch up with (나쁜 결과가) 결국 닥치다","a lack of sleep catches up with you"]]
PICK1=[
 {"s":"This daily {drive|drift} for sleep appears to be due, in part, to a compound known as adenosine.","ex":"정답 ▶ drive (욕구, 충동)\n오답 ▶ drift (표류, 흐름)\n이유: 앞 문장의 '잠에 대한 필요(need for sleep)'를 '매일의 수면 욕구'로 받아요.\n포인트 ▶ drive는 '운전하다' 말고 명사 '욕구, 충동'으로 자주 나와요."},
 {"s":"Thus, this molecule may be what your body uses to keep {track|trace} of lost sleep and to trigger sleep when needed.","ex":"정답 ▶ track (keep track of ~을 계속 파악하다)\n오답 ▶ trace (흔적): keep trace of라는 표현은 쓰지 않아요.\n포인트 ▶ keep track of = monitor 추적하다 ↔ lose track of 놓치다"},
 {"s":"An {accumulation|acceleration} of adenosine and other factors might explain why, after several nights of less than optimal amounts of sleep, you build up a sleep debt that you must make up by sleeping longer than normal.","ex":"정답 ▶ accumulation (축적)\n오답 ▶ acceleration (가속)\n이유: 아데노신은 깨어 있을수록 '쌓이는(builds up)' 물질 → 축적\n포인트 ▶ accumulate 축적하다 = build up"},
 {"s":"Although you may put off going to sleep in order to squeeze more activities into your day, {eventually|occasionally} your need for sleep becomes overwhelming and you are forced to get some sleep.","ex":"정답 ▶ eventually (결국)\n오답 ▶ occasionally (가끔)\n이유: Although(~이지만) 잠을 미룰 수는 있어도 '결국' 자게 된다는 대조예요. 마지막 문장 Eventually, a lack of sleep catches up with you.와 같은 흐름."}]
PICK2=[
 {"s":"This natural chemical builds up in your blood as time awake {increases|is increased}.","ex":"정답 ▶ increases\n이유: increase(늘다)는 여기서 목적어 없는 자동사 → 수동태 불가\n포인트 ▶ as + 주어 + 동사: ~함에 따라"},
 {"s":"{While|During} you sleep, your body breaks down the adenosine.","ex":"정답 ▶ While\n이유: 뒤에 주어+동사(you sleep) → 접속사 While. During은 전치사라 뒤에 명사(during sleep)\n포인트 ▶ while + 절 / during + 명사"},
 {"s":"An accumulation of adenosine and other factors might explain {why|what}, after several nights of less than optimal amounts of sleep, you build up a sleep debt that you must make up by sleeping longer than normal.","ex":"정답 ▶ why\n이유: 뒤 절 you build up a sleep debt가 완전한 문장 → 의문부사 why(왜 ~하는지). what은 뒤가 불완전할 때\n포인트 ▶ 삽입구(after ~ sleep)를 걷어 내고 보면 구조가 보여요."},
 {"s":"An accumulation of adenosine and other factors might explain why, after several nights of less than optimal amounts of sleep, you build up a sleep debt {that|what} you must make up by sleeping longer than normal.","ex":"정답 ▶ that\n이유: 선행사 a sleep debt가 있고, make up의 목적어가 빠진 목적격 관계대명사 자리 → that(which)\n오답 ▶ what은 선행사를 품고 있어 앞에 명사가 있으면 못 써요."},
 {"s":"Because of such built-in molecular feedback, you can't become accustomed to getting less sleep than your body {needs|need}.","ex":"정답 ▶ needs\n이유: than 뒤 절의 주어는 your body(단수) → needs"}]
VERB=[
 {"s":"Thus, this molecule may be what your body ___ to keep track of lost sleep and to trigger sleep when needed.","v":"use","a":["uses"],"ex":"정답 ▶ uses\n이유: what 절의 주어 your body(단수), 일반적 사실 → 현재시제 uses\n포인트 ▶ what your body uses = 몸이 사용하는 것"},
 {"s":"This natural chemical ___ up in your blood as time awake increases.","v":"build","a":["builds"],"ex":"정답 ▶ builds\n이유: 주어 This natural chemical(단수) + 현재시제 → builds (build up 쌓이다)"},
 {"s":"Eventually, a lack of sleep ___ up with you.","v":"catch","a":["catches"],"ex":"정답 ▶ catches\n이유: 주어 a lack of sleep(단수) → catches. -ch로 끝나면 -es\n포인트 ▶ catch up with (나쁜 결과가) 결국 닥치다"}]
ERR=[
 {"s":"Although you may put off going to sleep in order [[to squeeze]] more activities into your day, eventually your need for sleep becomes [[overwhelmingly]] and you are [[forced]] to get some sleep.","w":1,"fix":"overwhelming","ex":"틀린 곳 ▶ ② overwhelmingly → overwhelming\n이유: become 뒤 보어 자리 → 형용사\n나머지 ▶ ① in order to + 동사원형 ✔ ③ be forced to ~하도록 강요받다 ✔"},
 {"s":"This natural chemical [[builds]] up in your blood as time [[awake]] [[increase]].","w":2,"fix":"increases","ex":"틀린 곳 ▶ ③ increase → increases\n이유: as 절의 주어 time(단수, 셀 수 없음) → increases\n나머지 ▶ ① 주어 chemical 단수 ✔ ② time awake 깨어 있는 시간(awake가 뒤에서 수식) ✔"},
 {"s":"An accumulation of adenosine and other factors might explain [[why]], after several nights of less than optimal amounts of sleep, you build up a sleep debt [[that]] you must make up by [[sleep]] longer than normal.","w":2,"fix":"sleeping","ex":"틀린 곳 ▶ ③ sleep → sleeping\n이유: 전치사 by 뒤 → 동명사 (by -ing ~함으로써)\n나머지 ▶ ① 뒤가 완전한 절 → why ✔ ② 선행사 a sleep debt, 목적격 관계대명사 ✔"}]
S=None  # filled from passage
SCR=[3,1,4]
ORDER=[{"idx":[4,5,6,7],"flow":["따라서 아데노신 = 잃은 잠 파악·잠 유발 장치","아데노신 등의 축적 → 수면 빚(더 오래 자서 갚아야)","이런 분자적 피드백 → 적게 자는 데 익숙해질 수 없음","결국(Eventually) 수면 부족이 따라잡음"]}]
INSERT=[{"idx":[0,1,2,3],"given":1,"flow":["잠을 미뤄도 결국 자게 됨","이 매일의 수면 욕구 = 아데노신 때문","이 화학물질은 깨어 있을수록 쌓임","자는 동안 분해됨"],"ex":"정답 ▶ ①\n이유: 주어진 문장의 This daily drive for sleep은 첫 문장의 '잠에 대한 필요'를 받고, 다음 문장 This natural chemical은 주어진 문장의 adenosine을 가리켜요. 그래서 첫 문장과 This natural chemical 사이!\n포인트 ▶ 지시어(this, such)가 가리키는 말을 찾으면 자리가 보여요."}]
ODD=[{"lines":[4,5,"As a result, most adults soon learn to function well on just a few hours of sleep.",6],"odd":2,"ex":"정답 ▶ ③\n이유: 바로 다음 문장에서 몸이 필요로 하는 것보다 적게 자는 데 익숙해질 수 '없다'고 해요. 몇 시간만 자도 잘 지내게 된다는 문장은 흐름과 정반대예요.\n어휘 ▶ function well 잘 지내다, 제 기능을 하다"}]
BLANK=[
 {"s":"Thus, this molecule may be what your body uses to ____ lost sleep and to trigger sleep when needed.","opts":["keep track of","make up for","get rid of","put off"],"ex":"정답 ▶ keep track of (~을 계속 파악하다)\n이유: 깨어 있으면 쌓이고 자면 분해되니, 아데노신의 양으로 몸이 '부족한 잠을 파악'할 수 있어요.\n오답 ▶ make up for 보충하다 · get rid of 없애다 · put off 미루다"},
 {"s":"An accumulation of adenosine and other factors might explain why, after several nights of less than ____ amounts of sleep, you build up a sleep debt.","opts":["optimal","excessive","unlimited","additional"],"ex":"정답 ▶ optimal (최적의)\n이유: 수면 빚이 쌓이는 건 '최적에 못 미치는(less than optimal)' 잠을 잤을 때예요.\n오답 ▶ excessive 지나친 · unlimited 무제한의 · additional 추가의 → 잠을 많이 잤다는 뜻이 되어 반대"},
 {"s":"Because of such built-in molecular feedback, you can't become ____ getting less sleep than your body needs.","opts":["accustomed to","opposed to","addicted to","devoted to"],"ex":"정답 ▶ accustomed to (~에 익숙한)\n이유: 몸에 내장된 피드백 때문에 적게 자는 데 '익숙해질' 수 없어요. 결국 수면 부족이 따라잡아요.\n오답 ▶ opposed to 반대하는 · addicted to 중독된 · devoted to 헌신하는\n포인트 ▶ to는 전치사 → 뒤에 -ing"}]
GRAM=[
 {"q":"빈칸에 알맞은 것은?<br><b>This daily drive for sleep appears ______ due to a compound.</b>","opts":["to be","being","be","been"],"ex":"정답 ▶ to be\n이유: appear + to부정사 = ~인 것 같다(= seem to)\n본문 ▶ This daily drive for sleep appears to be due, in part, to a compound"},
 {"q":"빈칸에 알맞은 것은?<br><b>I left home early in order ______ more time at the library.</b>","opts":["to spend","spending","spend","spent"],"ex":"정답 ▶ to spend\n이유: in order to + 동사원형 = ~하기 위해\n본문 ▶ in order to squeeze more activities into your day"},
 {"q":"다음 중 어법상 <b>틀린</b> 것은?","opts":["I'm accustomed to get up early.","I'm used to getting up early.","She got used to living alone.","He is accustomed to working at night."],"ex":"정답 ▶ I'm accustomed to get up early.\n이유: be accustomed to의 to는 전치사 → getting up\n포인트 ▶ be accustomed to -ing = be used to -ing ~에 익숙하다 (used to + 동사원형 '~하곤 했다'와 구별)"},
 {"q":"빈칸에 알맞은 것은?<br><b>A compound ______ as adenosine builds up in your blood.</b>","opts":["known","knowing","knows","to know"],"ex":"정답 ▶ known\n이유: 화합물이 '~로 알려진' 수동 → 과거분사가 뒤에서 수식. 문장의 동사는 builds\n본문 ▶ a compound known as adenosine"}]
