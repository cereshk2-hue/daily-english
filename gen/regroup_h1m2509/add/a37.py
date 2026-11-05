N=37
MC=[
 dict(q="글의 내용과 <u>일치하는</u> 것은?",opts=[
  "Applying the brakes lets a bicycle slow down within a shorter distance.",
  "Once you stop pedalling, a forward force keeps acting on you.",
  "Friction pushes moving objects in the same direction as their motion.",
  "Without the brakes on, nothing slows a bicycle down.",
  "Air resistance helps push the cyclist forward."],
  ex="정답 ▶ Applying the brakes lets a bicycle slow down within a shorter distance.\n이유: How could you slow down more suddenly, in a shorter distance? By putting the brakes on.\n오답 ▶ ② no force is now acting to move you forward ③ opposite to movement(반대 방향) ④ other friction forces(다른 마찰력들)가 있음 ⑤ pushing you backwards(뒤로 밂)\n포인트 ▶ apply the brakes = put the brakes on 브레이크를 걸다",
  per=[["브레이크를 걸면 자전거가 더 짧은 거리 안에서 속도를 줄인다.","By putting the brakes on","apply the brakes = put the brakes on ✔"],
       ["페달을 멈춰도 앞으로 미는 힘이 계속 작용한다.","no force is now acting to move you forward","no force ✗"],
       ["마찰력은 움직이는 물체를 운동 방향과 같은 쪽으로 민다.","acting in the direction opposite to movement","the same ↔ opposite"],
       ["브레이크를 걸지 않으면 자전거를 느리게 하는 것은 없다.","there are other friction forces acting on you and your bicycle","nothing ✗ → other friction forces"],
       ["공기 저항은 자전거 탄 사람을 앞으로 밀어 준다.","pushing you backwards","forward ↔ backwards"]]),
 dict(q="글의 내용과 일치하지 <u>않는</u> 것은?",opts=[
  "In a cart, friction comes mostly from the wheels rubbing on the road.",
  "Brakes work by gripping and rubbing against the wheel-rims.",
  "Friction generally makes moving objects lose speed.",
  "The wheels rubbing against the axles produce a kind of friction.",
  "You can sense air resistance pushing you back as you ride."],
  ex="정답 ▶ In a cart, friction comes mostly from the wheels rubbing on the road.\n이유: mainly the axles rubbing on the body as they rotate. 수레의 마찰은 주로 '축이 본체에' 문질러지는 데서 생겨요.\n오답 ▶ 나머지는 모두 본문을 바꿔 쓴 일치 문장\n포인트 ▶ mostly = mainly · lose speed = slow down · produce = generate · sense = feel",
  per=[["수레에서 마찰은 주로 바퀴가 도로에 문질러지는 데서 생긴다.","mainly the axles rubbing on the body as they rotate","wheels on the road ✗ → axles on the body"],
       ["브레이크는 바퀴 테두리를 붙잡고 문질러서 작동한다.","as they grip and rub on the wheel-rims","일치"],
       ["마찰력은 대체로 움직이는 물체의 속도를 잃게 한다.","which tends to slow down moving things","lose speed = slow down · generally ≒ tends to"],
       ["바퀴가 축에 문질러지면서 일종의 마찰이 생긴다.","friction in the wheels rubbing on the axles","일치"],
       ["자전거를 탈 때 공기 저항이 뒤로 미는 것을 느낄 수 있다.","which you can feel, pushing you backwards","sense = feel · back = backwards"]]),
 dict(q="글의 내용과 <u>일치하는</u> 것은?",opts=[
  "브레이크를 걸지 않아도 자전거를 느리게 하는 마찰력이 있다.",
  "평평한 길에서 페달을 멈추면 자전거는 그 자리에서 바로 멈춘다.",
  "브레이크는 바퀴 축을 붙잡아 자전거를 멈춘다.",
  "마찰력은 움직이는 방향과 같은 방향으로 작용한다.",
  "공기 저항은 자전거가 멈춰 있을 때만 느낄 수 있다."],
  ex="정답 ▶ 브레이크를 걸지 않아도 자전거를 느리게 하는 마찰력이 있다.\n이유: Even without the brakes on, there are other friction forces acting on you and your bicycle, which also slow you down.\n오답 ▶ ② gradually slow down 점점 느려짐 ③ wheel-rims 바퀴 테두리를 붙잡음 ④ opposite 반대 방향 ⑤ as you and the bicycle move forwards 앞으로 갈 때 느껴짐\n포인트 ▶ wheel-rim 바퀴 테두리 · axle 축",
  per=[["","Even without the brakes on, there are other friction forces","일치 ✔"],
       ["","You gradually slow down","점점 느려짐"],
       ["","as they grip and rub on the wheel-rims","바퀴 테두리"],
       ["","in the direction opposite to movement","반대 방향"],
       ["","as you and the bicycle move forwards","앞으로 갈 때"]])]
TF=[
 ["The road in the example is flat.",True,"정답 ▶ T\n이유: 평평한 도로(a level road)에서 페달을 밟는다고 상상해요.\n어휘 ▶ flat = level 평평한","on a level road"],
 ["After you stop pedalling, nothing keeps pushing you forward.",True,"정답 ▶ T\n이유: 이제 앞으로 나아가게 하는 힘은 전혀 작용하지 않아요.\n어휘 ▶ nothing = no force","no force is now acting to move you forward"],
 ["Putting the brakes on makes you slow down more gradually.",False,"정답 ▶ F\n이유: 브레이크는 더 '갑자기(suddenly)' 느려지게 해요.\n어휘 ▶ gradually 점점 ↔ suddenly 갑자기","making you slow down more suddenly"],
 ["Brakes apply a force to both the bicycle and the rider.",True,"정답 ▶ T\n이유: 자전거와 여러분에게 힘을 가해요.\n어휘 ▶ apply a force = exert a force 힘을 가하다 · the rider = you","exerting a force on the bicycle and you"],
 ["Friction acts in the same direction in which an object is moving.",False,"정답 ▶ F\n이유: 움직임과 '반대' 방향, 즉 뒤쪽으로 작용해요.\n어휘 ▶ the same ↔ opposite","acting in the direction opposite to movement"],
 ["Brakes are the only source of friction on a moving bicycle.",False,"정답 ▶ F\n이유: 브레이크가 없어도 다른 마찰력들(바퀴-축 마찰, 공기 저항)이 있어요.\n어휘 ▶ the only source 유일한 원천","there are other friction forces acting on you and your bicycle"],
 ["In a cart, friction is produced mainly where the axles rub on the body.",True,"정답 ▶ T\n이유: 주로 축이 회전하면서 본체에 문질러지는 것이 마찰을 만들어요.\n어휘 ▶ produce = generate · mainly 주로","mainly the axles rubbing on the body as they rotate"]]
PICK1=[
 {"s":"Imagine you are pedalling your bicycle on a {level|lever} road.","ex":"정답 ▶ level (평평한)\n오답 ▶ lever (지렛대)\n포인트 ▶ level은 명사 '수준' 외에 형용사 '평평한'으로도 써요. 오르막·내리막이 없어야 마찰의 효과만 볼 수 있어요."},
 {"s":"Because the brakes change your movement, making you slow down more suddenly, they must be exerting a force on the bicycle and you, as they {grip|gripe} and rub on the wheel-rims.","ex":"정답 ▶ grip (꽉 잡다)\n오답 ▶ gripe (불평하다)\n이유: 브레이크가 바퀴 테두리를 '붙잡고' 문질러서 힘을 가해요."},
 {"s":"Another is air {resistance|assistance}, which you can feel, pushing you backwards as you and the bicycle move forwards.","ex":"정답 ▶ resistance (저항)\n오답 ▶ assistance (도움)\n이유: 뒤로 미는(pushing you backwards) 힘 → 저항\n포인트 ▶ resist 저항하다"},
 {"s":"When you {apply|supply} these ideas to something around you, like a cart, you can see what could be generating friction: mainly the axles rubbing on the body as they rotate.","ex":"정답 ▶ apply (적용하다)\n오답 ▶ supply (공급하다)\n포인트 ▶ apply A to B A를 B에 적용하다"}]
PICK2=[
 {"s":"How could you slow down more {suddenly|sudden}, in a shorter distance?","ex":"정답 ▶ suddenly\n이유: 동사 slow down을 꾸미는 부사 자리"},
 {"s":"By {putting|put} the brakes on.","ex":"정답 ▶ putting\n이유: 전치사 By 뒤 → 동명사 (by -ing ~함으로써)\n포인트 ▶ put the brakes on 브레이크를 걸다"},
 {"s":"This is the force called friction, which tends to slow down moving things by {acting|act} in the direction opposite to movement, that is backwards.","ex":"정답 ▶ acting\n이유: 전치사 by 뒤 → 동명사"},
 {"s":"One of these {is|are} friction in the wheels rubbing on the axles.","ex":"정답 ▶ is\n이유: 주어는 One(하나) → 단수 동사\n포인트 ▶ One of + 복수명사 + 단수동사"},
 {"s":"Another is air resistance, which you can feel, pushing you backwards as you and the bicycle {move|moves} forwards.","ex":"정답 ▶ move\n이유: as절의 주어 you and the bicycle(A and B, 복수) → move"}]
VERB=[
 {"s":"Imagine you are ___ your bicycle on a level road.","v":"pedal","a":["pedalling","pedaling"],"ex":"정답 ▶ pedalling (미국식 pedaling)\n이유: are + -ing 진행형\n포인트 ▶ 영국식은 l을 겹쳐 pedalling"},
 {"s":"Because the brakes change your movement, making you slow down more suddenly, they must be ___ a force on the bicycle and you, as they grip and rub on the wheel-rims.","v":"exert","a":["exerting"],"ex":"정답 ▶ exerting\n이유: must be + -ing ~하고 있음에 틀림없다 (진행 + 강한 추측)\n포인트 ▶ exert a force 힘을 가하다"},
 {"s":"When you apply these ideas to something around you, like a cart, you can see what could be generating friction: mainly the axles ___ on the body as they rotate.","v":"rub","a":["rubbing"],"ex":"정답 ▶ rubbing\n이유: 축이 본체에 '문질러지는' 동작을 나타내는 현재분사 (the axles rubbing ~ 문지르는 축). rub은 b를 겹쳐 rubbing"}]
ERR=[
 {"s":"Imagine you [[are pedalling]] your bicycle on a [[level]] road. You stop [[to pedal]]: no force is now acting to move you forward.","w":2,"fix":"pedalling","ex":"틀린 곳 ▶ ③ to pedal → pedalling\n이유: 페달 밟기를 '멈추다' → stop + 동명사. stop to pedal은 '페달을 밟기 위해 멈추다'라는 뜻이 돼요.\n나머지 ▶ ① 진행형 ✔ ② level 평평한 ✔"},
 {"s":"This is the force called friction, which [[tend]] to slow down [[moving]] things by acting in the direction [[opposite]] to movement, that is backwards.","w":0,"fix":"tends","ex":"틀린 곳 ▶ ① tend → tends\n이유: which의 선행사 friction(단수)\n나머지 ▶ ② 움직이는(능동) 물체 → moving ✔ ③ opposite to ~와 반대인 ✔"},
 {"s":"Another is air resistance, [[which]] you can feel, [[pushing]] you backwards as you and the bicycle [[moves]] forwards.","w":2,"fix":"move","ex":"틀린 곳 ▶ ③ moves → move\n이유: 주어 you and the bicycle은 복수\n나머지 ▶ ① 계속적 용법 which(선행사 air resistance) ✔ ② 뒤로 미는(능동) ✔"}]
SCR=[0,1,9,10]
ORDER=[{"idx":[3,4,5,6],"flow":["(페달을 멈추면) 점점 느려짐","더 짧은 거리에서 갑자기 멈추려면?","브레이크를 걸면 됨","브레이크가 바퀴 테두리를 잡고 문지르며 힘을 가함"]}]
INSERT=[{"idx":[8,9,10,11],"given":2,"flow":["브레이크 없이도 다른 마찰력들이 있음","하나는(One) 바퀴-축 마찰","또 하나는(Another) 공기 저항","수레에 적용: 주로 축-본체 마찰"],"ex":"정답 ▶ ②\n이유: '다른 마찰력들' → One of these(그중 하나) → Another(또 하나)의 순서예요.\n포인트 ▶ One ~ Another ~ 열거 신호"}]
ODD=[{"lines":[8,9,"Oiling the axles, however, makes this friction even stronger.",10],"odd":2,"ex":"정답 ▶ ③\n이유: 글은 자전거를 느리게 하는 마찰력들을 열거(One ~ Another ~)하는 흐름이에요. 축에 기름칠하는 이야기는 흐름에서 벗어나고, 내용도 사실과 반대예요(기름칠은 마찰을 줄여요)."}]
BLANK=[
 {"s":"You stop pedalling: no force is now acting to move you ____.","opts":["forward","backwards","upward","sideways"],"ex":"정답 ▶ forward (앞으로)\n이유: 페달을 밟는 것이 앞으로 나아가게 하는 힘이었는데, 멈추면 그 힘이 없어져요.\n오답 ▶ backwards 뒤로 · upward 위로 · sideways 옆으로"},
 {"s":"Because the brakes change your movement, making you slow down more suddenly, they must be exerting a force on the bicycle and you, as they grip and ____ on the wheel-rims.","opts":["rub","roll","float","melt"],"ex":"정답 ▶ rub (문지르다)\n이유: 문질러야 마찰(friction)이 생겨요. 뒤에도 rubbing on the axles, rubbing on the body가 반복돼요.\n오답 ▶ roll 구르다 · float 뜨다 · melt 녹다"},
 {"s":"Another is air ____, which you can feel, pushing you backwards as you and the bicycle move forwards.","opts":["resistance","quality","pollution","traffic"],"ex":"정답 ▶ resistance (저항)\n이유: 앞으로 갈 때 뒤로 미는 공기의 힘 = 공기 저항\n오답 ▶ air quality 대기 질 · air pollution 대기 오염 · air traffic 항공 교통"}]
GRAM=[
 {"q":"빈칸에 알맞은 것은?<br><b>He stopped ______ to rest his legs.</b>","opts":["pedalling","to pedal","pedal","pedalled"],"ex":"정답 ▶ pedalling\n이유: stop + -ing ~하던 것을 멈추다 (다리를 쉬려고 페달 밟기를 멈춤)\n오답 ▶ stop to pedal = 페달을 밟기 위해 (하던 일을) 멈추다\n본문 ▶ You stop pedalling"},
 {"q":"밑줄 친 <b>must</b>의 뜻으로 알맞은 것은?<br><b>They <u>must</u> be exerting a force on the bicycle.</b>","opts":["~임에 틀림없다","~해야 한다","~해도 된다","~할 리가 없다"],"ex":"정답 ▶ ~임에 틀림없다 (강한 추측)\n이유: 브레이크가 움직임을 바꾸니 힘을 가하고 있는 게 '틀림없다'는 추론이에요.\n포인트 ▶ must be ~ 강한 추측 ↔ can't be ~일 리가 없다"},
 {"q":"빈칸에 알맞은 것은?<br><b>The brakes make you ______ down more suddenly.</b>","opts":["slow","to slow","slowing","slowed"],"ex":"정답 ▶ slow\n이유: 사역동사 make + 목적어 + 동사원형\n본문 ▶ making you slow down more suddenly"},
 {"q":"빈칸에 알맞은 것은?<br><b>You can apply these ideas ______ something around you, like a cart.</b>","opts":["to","for","with","at"],"ex":"정답 ▶ to\n이유: apply A to B = A를 B에 적용하다\n본문 ▶ When you apply these ideas to something around you"}]
