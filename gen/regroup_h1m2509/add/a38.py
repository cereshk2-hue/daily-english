N=38
MC=[
 dict(q="글의 내용과 <u>일치하는</u> 것은?",opts=[
  "Nonlinear systems are capable of producing various special effects.",
  "Some editing systems today still rely on linear tape methods.",
  "In nonlinear editing, editors must rewind videotape to locate a scene.",
  "Linear editing is compared to using a word processor.",
  "In linear editing, an error could be fixed with a few keystrokes."],
  ex="정답 ▶ Nonlinear systems are capable of producing various special effects.\n이유: Nonlinear systems can create a range of special effects, such as slow motion, wipes and dissolves.\n오답 ▶ ② All editing systems are now nonlinear(이제 '모든' 시스템이 비선형) ③ 되감을 필요 없음(without having to ~ rewinding) ④ 선형 = 타자기, 비선형 = 워드 프로세서 ⑤ 선형은 글 전체를 다시 쳐야 했음\n포인트 ▶ various 다양한 = a range of · be capable of -ing ~할 수 있다 · locate 찾다 = find",
  per=[["비선형 시스템은 다양한 특수 효과를 만들어 낼 수 있다.","can create a range of special effects","various = a range of · produce = create ✔"],
       ["오늘날 일부 편집 시스템은 여전히 선형 테이프 방식에 의존한다.","All editing systems are now nonlinear computer-based systems","All ~ nonlinear → some linear ✗"],
       ["비선형 편집에서 편집자는 장면을 찾으려면 테이프를 되감아야 한다.","without having to spend time fast forwarding or rewinding videotape","must rewind ✗"],
       ["선형 편집은 워드 프로세서 사용에 비유된다.","Linear editing was like composing a paper on a typewriter","선형 = typewriter"],
       ["선형 편집에서는 몇 번의 키 입력으로 오류를 고칠 수 있었다.","the whole piece had to be retyped","키 몇 번 = 비선형"]]),
 dict(q="글의 내용과 일치하지 <u>않는</u> 것은?",opts=[
  "Adding a new scene in nonlinear editing requires rebuilding the whole program.",
  "Nonlinear systems give editors instant access to any shot.",
  "Slow motion is one of the effects nonlinear systems can produce.",
  "Fixing a mistake in linear editing meant redoing the entire piece.",
  "Word processors allow new information to be inserted with ease."],
  ex="정답 ▶ Adding a new scene in nonlinear editing requires rebuilding the whole program.\n이유: shots or scenes can be easily added or removed anywhere in the program, and the computer adjusts the program length automatically.\n오답 ▶ 나머지는 모두 본문을 바꿔 쓴 일치 문장\n포인트 ▶ instant access 즉시 접근 ≒ random access · redo = retype · entire = whole · with ease = easily · insert = add",
  per=[["비선형 편집에서 새 장면을 넣으려면 프로그램 전체를 다시 만들어야 한다.","can be easily added or removed anywhere in the program","rebuild the whole ✗ → easily added"],
       ["비선형 시스템은 편집자가 어떤 숏에도 즉시 접근하게 해 준다.","allow random access to any video shot or scene","instant access ≒ random access(원하는 곳에 바로 접근)"],
       ["슬로 모션은 비선형 시스템이 만들 수 있는 효과 중 하나다.","such as slow motion, wipes and dissolves","일치"],
       ["선형 편집에서 실수를 고치려면 글 전체를 다시 해야 했다.","the whole piece had to be retyped","redo ≒ retype · entire = whole"],
       ["워드 프로세서는 새로운 정보를 쉽게 넣을 수 있게 해 준다.","new information can be added easily","with ease = easily · insert = add"]]),
 dict(q="글의 내용과 <u>일치하는</u> 것은?",opts=[
  "비선형 편집에서는 컴퓨터가 프로그램 길이를 자동으로 맞춘다.",
  "선형 편집은 워드 프로세서로 글을 쓰는 것과 비슷했다.",
  "비선형 시스템으로는 특수 효과를 만들 수 없다.",
  "비선형 편집에서도 원하는 장면을 찾으려면 테이프를 되감아야 한다.",
  "오늘날에도 편집 시스템의 상당수는 선형 방식이다."],
  ex="정답 ▶ 비선형 편집에서는 컴퓨터가 프로그램 길이를 자동으로 맞춘다.\n이유: the computer adjusts the program length automatically\n오답 ▶ ② 선형 = 타자기(typewriter) ③ a range of special effects를 만듦 ④ 빨리 감기·되감기 필요 없음 ⑤ All editing systems are now nonlinear\n포인트 ▶ adjust 조정하다 · automatically 자동으로",
  per=[["","the computer adjusts the program length automatically","일치 ✔"],
       ["","Linear editing was like composing a paper on a typewriter","타자기"],
       ["","can create a range of special effects","특수 효과 가능"],
       ["","without having to fast forward or fast reverse to find it","되감기 불필요"],
       ["","All editing systems are now nonlinear","모두 비선형"]])]
TF=[
 ["Today, every editing system is nonlinear and computer-based.",True,"정답 ▶ T\n이유: 이제 모든 편집 시스템은 비선형 컴퓨터 기반이에요.\n어휘 ▶ every = all · today = now","All editing systems are now nonlinear computer-based systems"],
 ["Nonlinear systems can produce effects such as dissolves.",True,"정답 ▶ T\n이유: 슬로 모션, 와이프, 디졸브 같은 특수 효과를 만들 수 있어요.\n어휘 ▶ produce = create","such as slow motion, wipes and dissolves"],
 ["With nonlinear systems, editors still have to fast forward to find a shot.",False,"정답 ▶ F\n이유: 빨리 감거나 되감을 필요 없이 바로 찾아요.\n어휘 ▶ without having to ~할 필요 없이","without having to fast forward or fast reverse to find it"],
 ["In nonlinear editing, scenes can be inserted or deleted at any point in the program.",True,"정답 ▶ T\n이유: 프로그램 어디에서나 쉽게 추가하거나 삭제할 수 있어요.\n어휘 ▶ insert = add · delete = remove · at any point = anywhere","can be easily added or removed anywhere in the program"],
 ["Linear editing is compared to writing on a typewriter.",True,"정답 ▶ T\n이유: 선형 편집은 타자기로 글을 쓰는 것과 같았어요.\n어휘 ▶ compare A to B A를 B에 비유하다 · write = compose","Linear editing was like composing a paper on a typewriter"],
 ["In linear editing, adding new information meant retyping only the changed part.",False,"정답 ▶ F\n이유: 글 '전체(the whole piece)'를 다시 쳐야 했어요.\n어휘 ▶ only the changed part ↔ the whole piece","the whole piece had to be retyped"],
 ["Nonlinear editing is likened to working with a word processor.",True,"정답 ▶ T\n이유: 반면에 비선형 편집은 워드 프로세서를 쓰는 것과 같아요.\n어휘 ▶ be likened to ~에 비유되다 = be like","is like using a word processing program"]]
PICK1=[
 {"s":"Nonlinear systems can create a {range|rage} of special effects, such as slow motion, wipes and dissolves.","ex":"정답 ▶ range (a range of 다양한)\n오답 ▶ rage (분노)\n포인트 ▶ a range of = various = a variety of"},
 {"s":"Another {highlight|headlight} of a digital nonlinear system is its random access process that makes it easy for an editor to find desired shots or scenes without having to spend time fast forwarding or rewinding videotape.","ex":"정답 ▶ highlight (가장 중요한 부분, 장점)\n오답 ▶ headlight (전조등)\n이유: Another highlight = 또 다른 주요 장점 (앞의 특수 효과에 이어)"},
 {"s":"Another highlight of a digital nonlinear system is its random access process that makes it easy for an editor to find {desired|deserted} shots or scenes without having to spend time fast forwarding or rewinding videotape.","ex":"정답 ▶ desired (원하는)\n오답 ▶ deserted (버려진, 사람이 없는)\n포인트 ▶ desire 바라다 → desired 바라던, 원하는"},
 {"s":"With nonlinear editing, shots or scenes can be easily added or {removed|reviewed} anywhere in the program, and the computer adjusts the program length automatically.","ex":"정답 ▶ removed (제거된)\n오답 ▶ reviewed (검토된)\n이유: added or removed 추가하거나 삭제하거나 → 그래서 길이를 자동으로 조정(adjusts)해요."}]
PICK2=[
 {"s":"Nonlinear editing, on the other hand, is like {using|use} a word processing program.","ex":"정답 ▶ using\n이유: 여기서 like는 전치사(~와 같은) → 뒤에 동명사"},
 {"s":"With nonlinear editing, shots or scenes can be easily added or removed anywhere in the program, and the computer {adjusts|adjust} the program length automatically.","ex":"정답 ▶ adjusts\n이유: and 뒤 절의 주어 the computer(단수)"},
 {"s":"If a mistake was made or new information needed to be added the whole piece had to {be retyped|retype}.","ex":"정답 ▶ be retyped\n이유: 글 전체(the whole piece)가 '다시 타이핑되는' 수동 → had to + be + p.p.\n포인트 ▶ 주어가 사람이 아니라 '글'이면 수동을 먼저 의심!"},
 {"s":"If a mistake is made, it {is easily deleted|easily deletes} and fixed with a few keystrokes, and new information can be added easily.","ex":"정답 ▶ is easily deleted\n이유: 실수(it)가 '지워지는' 수동 → be + p.p. 뒤의 fixed도 (is) fixed"},
 {"s":"Another highlight of a digital nonlinear system is its random access process that makes it easy for an editor to find desired shots or scenes without having to spend time {fast forwarding|to fast forward} or rewinding videotape.","ex":"정답 ▶ fast forwarding\n이유: spend + 시간 + -ing ~하는 데 시간을 쓰다. 뒤의 rewinding과도 병렬"}]
VERB=[
 {"s":"All editing systems are now nonlinear computer-based systems that allow random access to any video shot or scene without ___ to fast forward or fast reverse to find it.","v":"have","a":["having"],"ex":"정답 ▶ having\n이유: 전치사 without 뒤 → 동명사 (without having to ~할 필요 없이)"},
 {"s":"With nonlinear editing, shots or scenes can be easily added or ___ anywhere in the program, and the computer adjusts the program length automatically.","v":"remove","a":["removed"],"ex":"정답 ▶ removed\n이유: can be added or (be) removed — 장면이 '삭제되는' 수동, added와 병렬"},
 {"s":"If a mistake is made, it is easily ___ and fixed with a few keystrokes, and new information can be added easily.","v":"delete","a":["deleted"],"ex":"정답 ▶ deleted\n이유: 실수가 '지워지는' 수동 → is deleted (fixed와 병렬)"}]
ERR=[
 {"s":"Nonlinear editing, [[on the other hand]], is like [[use]] a word [[processing]] program.","w":1,"fix":"using","ex":"틀린 곳 ▶ ② use → using\n이유: 전치사 like 뒤 → 동명사\n나머지 ▶ ① 반면에 ✔ ③ word processing program 워드 프로세서 ✔"},
 {"s":"With nonlinear editing, shots or scenes can be easily [[added]] or [[removed]] anywhere in the program, and the computer [[adjust]] the program length automatically.","w":2,"fix":"adjusts","ex":"틀린 곳 ▶ ③ adjust → adjusts\n이유: 주어 the computer(단수), 현재시제\n나머지 ▶ ① ② 장면이 추가·삭제되는 수동 ✔"},
 {"s":"If a mistake is made, it is easily deleted and [[fixed]] with a few keystrokes, and new information [[can add]] [[easily]].","w":1,"fix":"can be added","ex":"틀린 곳 ▶ ② can add → can be added\n이유: 정보가 '추가되는' 수동 → 조동사 + be + p.p.\n나머지 ▶ ① (is) fixed ✔ ③ 부사 easily ✔"}]
SCR=[1,3,5,7]
ORDER=[{"idx":[0,1,2,3],"flow":["이제 모든 편집 = 비선형(임의 접근)","비선형은 다양한 특수 효과 가능","또 다른(Another) 장점: 원하는 장면을 바로 찾음","장면을 쉽게 추가·삭제, 길이는 자동 조정"]}]
INSERT=[{"idx":[4,5,6,7],"given":1,"flow":["선형 편집 = 타자기로 글쓰기","실수·추가가 생기면 전체를 다시 쳐야 했음","반면에(on the other hand) 비선형 = 워드 프로세서","실수는 키 몇 번으로 고침"],"ex":"정답 ▶ ①\n이유: 주어진 문장은 과거시제(was made, had to be)로 '타자기(선형)'의 불편함을 설명해요. 타자기 비유 바로 뒤, on the other hand(반면에) 앞!\n포인트 ▶ 선형(과거, was) ↔ 비선형(현재, is) 시제 대비"}]
ODD=[{"lines":[0,1,"Many film directors, however, still prefer watching movies in theaters.",2],"odd":2,"ex":"정답 ▶ ③\n이유: 글은 비선형 편집 시스템의 장점(특수 효과 → 또 다른 장점: 임의 접근)을 이어 가요. 영화를 극장에서 보는 취향 이야기는 주제와 관계없어요."}]
BLANK=[
 {"s":"Nonlinear systems can create a range of special ____, such as slow motion, wipes and dissolves.","opts":["effects","budgets","actors","cameras"],"ex":"정답 ▶ effects (효과)\n이유: 슬로 모션, 와이프, 디졸브는 화면 '특수 효과'예요.\n포인트 ▶ effect 효과(명사) / affect 영향을 주다(동사)"},
 {"s":"If a mistake was made or new information needed to be added the ____ piece had to be retyped.","opts":["whole","last","shortest","missing"],"ex":"정답 ▶ whole (전체의)\n이유: 타자기는 중간을 고칠 수 없어 글 '전체'를 다시 쳐야 했어요. 그래서 비선형(어디서나 추가·삭제)과 대조돼요.\n오답 ▶ last 마지막 · shortest 가장 짧은 · missing 빠진"},
 {"s":"If a mistake is made, it is easily deleted and fixed with a few ____, and new information can be added easily.","opts":["keystrokes","tapes","scissors","days"],"ex":"정답 ▶ keystrokes (키 입력)\n이유: 워드 프로세서에서는 '키 몇 번'으로 지우고 고쳐요.\n오답 ▶ tapes 테이프 · scissors 가위 · days 며칠"}]
GRAM=[
 {"q":"빈칸에 알맞은 것은?<br><b>The new app makes it easy ______ us to edit videos.</b>","opts":["for","of","to","with"],"ex":"정답 ▶ for\n이유: make + it(가목적어) + 형용사 + for 의미상 주어 + to부정사(진목적어)\n본문 ▶ makes it easy for an editor to find desired shots"},
 {"q":"빈칸에 알맞은 것은?<br><b>You can find any scene without ______ to rewind the tape.</b>","opts":["having","have","had","to have"],"ex":"정답 ▶ having\n이유: 전치사 without + 동명사. without having to ~할 필요 없이\n본문 ▶ without having to fast forward or fast reverse"},
 {"q":"빈칸에 알맞은 것은?<br><b>New information needed ______ to the report.</b>","opts":["to be added","to add","adding to","be added"],"ex":"정답 ▶ to be added\n이유: 정보가 '추가되어야' 하는 수동 → need to be p.p.\n본문 ▶ new information needed to be added"},
 {"q":"빈칸에 알맞은 것은?<br><b>Nonlinear systems can create special effects, ______ slow motion and wipes.</b>","opts":["such as","so as","as well","as if"],"ex":"정답 ▶ such as (~와 같은)\n이유: 예를 들 때 such as + 명사\n오답 ▶ so as to ~하기 위해 · as well 또한 · as if 마치 ~처럼\n본문 ▶ such as slow motion, wipes and dissolves"}]
