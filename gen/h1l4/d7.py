VOCAB=[
 ["environment","환경","❶"],["in trouble","곤경[위기]에 처한","❶"],["sea level","해수면","❶"],["natural disaster","자연재해","❶"],
 ["flood","홍수","❶"],["waste","쓰레기, 폐기물","❶"],["in particular","특히","❶"],["pollution","오염","❶"],
 ["contributor","(~의) 원인 제공자, 기여자","❶"],["destruction","파괴","❶"],["climate change","기후 변화","❶"],
 ["stop A from -ing","A가 ~하지 못하게 막다","❶"],["reach","~에 이르다, 도달하다","❶"],["achieve","~을 달성하다, 이루다","❶"],
 ["provide A with B","A에게 B를 제공하다","❶"],["solution","해결책","❶"],["area","영역, 분야","❶"],
 ["deal with","~을 처리하다, 다루다","❷"],["single-use","일회용의","❷"],["discard","~을 버리다","❷"],["throw away","~을 버리다","❷"],
 ["recycle","~을 재활용하다","❷"],["landfill","쓰레기 매립지","❷"],["so far","지금까지","❷"],["dump","(쓰레기 등을) 내버리다","❷"],
 ["end up in","결국 ~에 이르게 되다","❷"],["marine","바다의, 해양의","❷"],["species","(생물의) 종","❷"],
 ["put ~ in danger","~을 위험에 빠뜨리다","❷"],["with ~ in mind","~을 염두에 두고","❷"],["turn to","~에 의지하다, ~로 눈을 돌리다","❷"],
 ["larva","유충, 애벌레 (복수형 larvae)","❷","larvae"],["beetle","딱정벌레","❷"],["break down","~을 분해하다","❷"],
 ["feed on","~을 먹고 살다","❷"],["cultivate","(세균 등을) 배양하다; 경작하다","❷"],["speed up","~의 속도를 높이다","❷"],
 ["plastic-free","플라스틱이 없는","❷"]]
PICK1=[
 {"s":"With the planet becoming warmer, sea levels are {rising|falling} and natural disasters such as forest fires and floods are increasing.","ex":"정답 ▶ rising (상승하는)\n오답 ▶ falling (떨어지는)\n이유: 지구가 따뜻해지면 빙하가 녹아 해수면이 '올라가요'. 뒤의 are increasing(증가하고 있다)과도 같은 방향이에요."},
 {"s":"More and more waste is also being {produced|reduced}.","ex":"정답 ▶ produced (생산되는)\n오답 ▶ reduced (줄어드는)\n이유: More and more(점점 더 많은) 쓰레기가 '만들어지고' 있다 → 환경이 위기라는 흐름"},
 {"s":"It is clear that humans are a major {contributor|distributor} to the destruction of nature.","ex":"정답 ▶ contributor (원인 제공자)\n오답 ▶ distributor (유통업자, 배급자)\n포인트 ▶ a contributor to ~ = ~의 한 원인 · contribute to ~의 원인이 되다"},
 {"s":"It is clear that humans are a major contributor to the {destruction|construction} of nature.","ex":"정답 ▶ destruction (파괴)\n오답 ▶ construction (건설)\n포인트 ▶ destroy 파괴하다 → destruction ↔ construct 건설하다 → construction"},
 {"s":"Achieving these goals seems {difficult|easy}.","ex":"정답 ▶ difficult (어려운)\n오답 ▶ easy (쉬운)\n이유: 다음 문장이 'Nature, however, ~'(그러나 자연은 해결책을 줬을지도 몰라)예요. however로 뒤집으려면 앞은 '어렵다'여야 해요."},
 {"s":"That means the items are used just once and then {discarded|discovered}.","ex":"정답 ▶ discarded (버려지는)\n오답 ▶ discovered (발견되는)\n이유: 일회용(single-use) 제품 → 한 번 쓰고 '버려져요'.\n포인트 ▶ discard = throw away"},
 {"s":"Recycling can help {reduce|increase} the amount of plastic in our landfills.","ex":"정답 ▶ reduce (줄이다)\n오답 ▶ increase (늘리다)\n이유: 재활용하면 매립지로 가는 플라스틱의 양이 '줄어요'."},
 {"s":"This puts many {marine|desert} species in danger.","ex":"정답 ▶ marine (바다의, 해양의)\n오답 ▶ desert (사막의)\n이유: 앞 문장에서 플라스틱이 '바다(ocean)'로 흘러든다고 했어요."},
 {"s":"Scientists are now looking for ways to {cultivate|eliminate} the bacteria outside of mealworms.","ex":"정답 ▶ cultivate (배양하다, 기르다)\n오답 ▶ eliminate (없애다)\n이유: 이 박테리아는 플라스틱을 분해하는 '고마운' 박테리아 → 밀웜 밖에서도 '키우고' 싶어 해요."},
 {"s":"They also want to {speed|slow} up the process by which the bacteria break down plastic.","ex":"정답 ▶ speed (speed up 속도를 높이다)\n오답 ▶ slow (slow up 속도를 늦추다)\n이유: 플라스틱을 빨리 분해할수록 매립지를 플라스틱 없이 유지할 수 있어요."}]
TF=[
 ["Warmer temperatures are making sea levels go up.",True,"정답 ▶ T\n이유: 지구가 따뜻해지면서 해수면이 상승하고 있어요.\n어휘 ▶ go up = rise 오르다","❶","sea levels are rising"],
 ["Natural disasters like floods are becoming less frequent.",False,"정답 ▶ F\n이유: 산불과 홍수 같은 자연재해는 '증가하고(increasing)' 있어요.\n어휘 ▶ frequent 잦은 · less frequent 덜 잦은 ↔ increasing","❶","natural disasters such as forest fires and floods are increasing"],
 ["The amount of waste we produce is going down.",False,"정답 ▶ F\n이유: 점점 더 많은(More and more) 쓰레기가 생산되고 있어요.\n어휘 ▶ go down 줄다 ↔ more and more","❶","More and more waste is also being produced"],
 ["Humans are clearly one of the main causes of damage to nature.",True,"정답 ▶ T\n이유: 인간이 자연 파괴의 주요 원인 제공자인 것은 분명해요.\n어휘 ▶ main = major · cause = contributor · damage ≒ destruction","❶","humans are a major contributor to the destruction of nature"],
 ["The writer suggests that nature may have already given us answers to our problems.",True,"정답 ▶ T\n이유: 자연이 이 문제들에 대한 해결책을 제공했을지도 모른다고 했어요.\n어휘 ▶ give = provide · answer = solution","❶","may have provided us with solutions to these problems"],
 ["Roughly half of all plastic is made for products that are used only once.",True,"정답 ▶ T\n이유: 플라스틱의 약 50%가 일회용 제품을 위해 생산돼요.\n어휘 ▶ roughly = about 약 · half = fifty percent · used only once = single-use","❷","About fifty percent of plastic is produced for single-use products"],
 ["Most of the world's plastic waste has been recycled so far.",False,"정답 ▶ F\n이유: 지금까지 10%도 안 되는 양만 재활용됐어요.\n어휘 ▶ most 대부분 ↔ less than ten percent 10% 미만","❷","less than ten percent"],
 ["Plastic that ends up in the ocean threatens many sea creatures.",True,"정답 ▶ T\n이유: 바다로 흘러든 플라스틱이 많은 해양 생물 종을 위험에 빠뜨려요.\n어휘 ▶ threaten = put ~ in danger · sea creatures = marine species","❷","This puts many marine species in danger"],
 ["Mealworms are young beetles.",True,"정답 ▶ T\n이유: 밀웜은 어떤 딱정벌레 종의 유충이에요.\n어휘 ▶ young beetles(어린 딱정벌레) ≒ the larvae of a beetle","❷","Mealworms are the larvae of a certain species of beetle"],
 ["Scientists want to slow down the process of breaking down plastic.",False,"정답 ▶ F\n이유: 분해 과정의 속도를 '높이고(speed up)' 싶어 해요.\n어휘 ▶ slow down ↔ speed up","❷","speed up the process"],
 ["Scientists hope to grow the bacteria outside the mealworms' bodies.",True,"정답 ▶ T\n이유: 밀웜 밖에서 박테리아를 배양할 방법을 찾고 있어요.\n어휘 ▶ grow = cultivate 배양하다","❷","cultivate the bacteria outside of mealworms"]]
MC=[
 dict(n="❶",box=["❶"],q="본문 ❶의 내용과 <u>일치하는</u> 것은?",opts=[
  "Warmer temperatures are leading to higher sea levels.",
  "Forest fires and floods are on the decline.",
  "Plastic mainly pollutes the air rather than soil and water.",
  "Humans play only a minor role in damaging nature.",
  "The writer believes that achieving environmental goals is simple."],
  ex="정답 ▶ Warmer temperatures are leading to higher sea levels.\n이유: With the planet becoming warmer, sea levels are rising\n오답 ▶ ② on the decline(감소하는) ↔ increasing ③ 토양과 수질(soil and water) 오염 ④ minor(사소한) ↔ major(주요한) ⑤ simple ↔ seems difficult\n포인트 ▶ lead to ~로 이어지다 · higher sea levels = sea levels are rising",
  per=[["더 따뜻해진 기온이 해수면 상승으로 이어지고 있다.","sea levels are rising","lead to = ~을 일으키다 ✔"],
       ["산불과 홍수는 줄어들고 있다.","are increasing","on the decline 감소하는 ↔ increasing"],
       ["플라스틱은 토양과 물보다 주로 공기를 오염시킨다.","problems with soil and water pollution","air ✗ → soil and water"],
       ["인간은 자연 훼손에 사소한 역할만 한다.","a major contributor","minor ↔ major"],
       ["필자는 환경 목표를 이루는 것이 간단하다고 믿는다.","Achieving these goals seems difficult","simple ↔ difficult"]]),
 dict(n="❷",box=["❷"],q="본문 ❷의 내용과 일치하지 <u>않는</u> 것은?",opts=[
  "Most of the world's plastic waste has already been recycled.",
  "Single-use plastic items are thrown away after one use.",
  "Millions of tons of plastic flow into the sea annually.",
  "Mealworms carry bacteria that are capable of decomposing plastic.",
  "Scientists aim to accelerate the process of breaking down plastic."],
  ex="정답 ▶ Most of the world's plastic waste has already been recycled.\n이유: less than ten percent of the world's plastic waste has been recycled so far. 10%도 안 돼요.\n오답 ▶ 나머지는 모두 본문을 다른 어휘로 바꿔 쓴 일치 문장\n포인트 ▶ annually = every year · decompose 분해하다 = break down · accelerate 가속하다 = speed up · aim to = want to",
  per=[["세계 플라스틱 쓰레기의 대부분은 이미 재활용되었다.","less than ten percent","most ✗ → 10% 미만"],
       ["일회용 플라스틱 제품은 한 번 쓰고 버려진다.","used just once and then discarded","throw away = discard ✔"],
       ["매년 수백만 톤의 플라스틱이 바다로 흘러든다.","end up in the ocean every year","annually = every year · flow into ≒ end up in"],
       ["밀웜은 플라스틱을 분해할 수 있는 박테리아를 지니고 있다.","These bacteria can break down plastic","decompose = break down"],
       ["과학자들은 플라스틱 분해 과정을 가속화하는 것을 목표로 한다.","speed up the process","accelerate = speed up · aim to ≒ want to"]]),
 dict(n="❷",box=["❷"],q="본문 ❷의 내용과 <u>일치하는</u> 것은?",opts=[
  "밀웜 안에 사는 박테리아는 플라스틱을 분해할 수 있다.",
  "플라스틱의 약 10%가 일회용 제품을 위해 생산된다.",
  "버려진 플라스틱은 대부분 재활용 시설로 보내진다.",
  "매년 1억 톤이 넘는 플라스틱이 바다로 흘러든다.",
  "과학자들은 밀웜 속 박테리아의 수를 줄이려고 한다."],
  ex="정답 ▶ 밀웜 안에 사는 박테리아는 플라스틱을 분해할 수 있다.\n이유: Special bacteria live inside them. These bacteria can break down plastic.\n오답 ▶ ② 약 50%(About fifty percent) ③ 그냥 버려지거나 태워지는 곳(dumped or burned)으로, 재활용은 10% 미만 ④ 8백만~1천4백만 톤(between 8 and 14 million metric tons) ⑤ 밀웜 밖에서 배양(cultivate)하려 함\n포인트 ▶ 숫자(50%, 10%, 8~14 million) 정확히 기억하기!",
  per=[["","These bacteria can break down plastic","일치 ✔"],
       ["","About fifty percent of plastic is produced for single-use products","약 50%"],
       ["","where it is just dumped or burned","버려지거나 태워짐"],
       ["","between 8 and 14 million metric tons","8백만~1천4백만 톤"],
       ["","cultivate the bacteria outside of mealworms","배양(늘리기)"]])]
PICK2=[
 {"s":"With the planet {becoming|became} warmer, sea levels are rising and natural disasters such as forest fires and floods are increasing.","ex":"정답 ▶ becoming\n이유: with + 명사(the planet) + 분사: 지구가 '~해지면서'. 지구가 스스로 따뜻해지는 능동 → 현재분사\n포인트 ▶ = As the planet becomes warmer"},
 {"s":"More and more waste is also being {produced|producing}.","ex":"정답 ▶ produced\n이유: 쓰레기가 '생산되는' 수동 + 진행 → is being p.p.(현재진행 수동태)"},
 {"s":"Plastic, in particular, {is|are} causing problems with soil and water pollution.","ex":"정답 ▶ is\n이유: 주어 Plastic(셀 수 없는 명사, 단수). in particular는 삽입구"},
 {"s":"It is clear {that|what} humans are a major contributor to the destruction of nature.","ex":"정답 ▶ that\n이유: 가주어 It - 진주어 that절. 뒤가 완전한 문장(humans are ~) → that\n오답 ▶ what은 뒤에 불완전한 문장"},
 {"s":"Can we stop climate change from {reaching|reach} dangerous levels?","ex":"정답 ▶ reaching\n이유: stop A from -ing A가 ~하지 못하게 막다. from은 전치사 → 동명사"},
 {"s":"Achieving these goals {seems|seem} difficult.","ex":"정답 ▶ seems\n이유: 동명사구 주어(Achieving these goals)는 단수 취급. goals(복수)에 속지 마세요!"},
 {"s":"Nature, however, may have {provided|provide} us with solutions to these problems.","ex":"정답 ▶ provided\n이유: may have + p.p. = ~했을지도 모른다(과거에 대한 추측)\n포인트 ▶ provide A with B A에게 B를 제공하다"},
 {"s":"Here {are|is} three areas where changes are already happening.","ex":"정답 ▶ are\n이유: Here + 동사 + 주어 도치. 진짜 주어는 three areas(복수)"},
 {"s":"Here are three areas {where|which} changes are already happening.","ex":"정답 ▶ where\n이유: 선행사 three areas(장소·영역) + 뒤가 완전한 문장(changes are happening) → 관계부사 where\n오답 ▶ which는 뒤에 주어나 목적어가 빠진 불완전한 문장"},
 {"s":"About fifty percent of plastic {is|are} produced for single-use products.","ex":"정답 ▶ is\n이유: 퍼센트 of + 명사 → of 뒤의 명사에 수일치. plastic(셀 수 없는 명사) → 단수 is"},
 {"s":"However, less than ten percent of the world's plastic waste has {been recycled|recycled} so far.","ex":"정답 ▶ been recycled\n이유: 쓰레기가 '재활용되는' 수동 + so far(지금까지) → 현재완료 수동 has been p.p."},
 {"s":"They also want to speed up the process {by which|which} the bacteria break down plastic.","ex":"정답 ▶ by which\n이유: 뒤가 완전한 문장(the bacteria break down plastic) → 전치사 + 관계대명사. the bacteria break down plastic by the process에서 by가 앞으로\n포인트 ▶ 전치사 + which 뒤에는 완전한 문장"},
 {"s":"This may help us {keep|keeping} our landfills plastic-free.","ex":"정답 ▶ keep\n이유: help + 목적어 + 동사원형(또는 to부정사)\n포인트 ▶ keep + 목적어 + 형용사(plastic-free) ~을 …한 상태로 유지하다"}]
VERB=[
 {"s":"With the planet ___ warmer, sea levels are rising and natural disasters such as forest fires and floods are increasing.","v":"become","a":["becoming"],"ex":"정답 ▶ becoming\n이유: with + 명사 + 현재분사(능동): 지구가 따뜻해지면서"},
 {"s":"More and more waste is also ___ produced.","v":"be","a":["being"],"ex":"정답 ▶ being\n이유: 현재진행 수동태 is being p.p. = ~되고 있다"},
 {"s":"Will we be able ___ the environment from mountains of plastic?","v":"protect","a":["to protect"],"ex":"정답 ▶ to protect\n이유: be able to + 동사원형 ~할 수 있다\n포인트 ▶ protect A from B B로부터 A를 보호하다"},
 {"s":"Nature, however, may have ___ us with solutions to these problems.","v":"provide","a":["provided"],"ex":"정답 ▶ provided\n이유: may have + p.p. ~했을지도 모른다"},
 {"s":"Do you ever stop ___ about where these plastic items go after you throw them away?","v":"think","a":["to think"],"ex":"정답 ▶ to think\n이유: stop + to부정사 = ~하기 위해 (하던 일을) 멈추다 → 멈춰서 생각해 보다\n포인트 ▶ stop -ing는 '~하던 것을 그만두다'라서 뜻이 달라져요."},
 {"s":"That means the items are used just once and then ___.","v":"discard","a":["discarded"],"ex":"정답 ▶ discarded\n이유: are used and then (are) discarded — 수동태 병렬"},
 {"s":"However, less than ten percent of the world's plastic waste has been ___ so far.","v":"recycle","a":["recycled"],"ex":"정답 ▶ recycled\n이유: has been + p.p. 현재완료 수동"},
 {"s":"With this in mind, scientists are ___ to mealworms.","v":"turn","a":["turning"],"ex":"정답 ▶ turning\n이유: are + -ing 현재진행형\n포인트 ▶ turn to ~에 의지하다, ~로 눈을 돌리다"},
 {"s":"Scientists are now looking for ways ___ the bacteria outside of mealworms.","v":"cultivate","a":["to cultivate"],"ex":"정답 ▶ to cultivate\n이유: ways를 꾸미는 to부정사(형용사적 용법) = 배양할 방법"}]
ERR=[
 {"s":"Our environment is in trouble. With the planet [[became]] warmer, sea levels are [[rising]] and natural disasters such as forest fires and floods [[are]] increasing.","w":0,"fix":"becoming","ex":"틀린 곳 ▶ ① became → becoming\n이유: with + 명사 + 분사 구문 → 동사 자리가 아니라 분사 자리\n나머지 ▶ ② 현재진행 ✔ ③ 주어 natural disasters(복수) ✔"},
 {"s":"More and more waste is also being [[producing]]. Plastic, [[in particular]], [[is]] causing problems with soil and water pollution.","w":0,"fix":"produced","ex":"틀린 곳 ▶ ① producing → produced\n이유: 쓰레기는 '생산되는' 것 → is being p.p.\n나머지 ▶ ② 특히 ✔ ③ 주어 Plastic(단수) ✔"},
 {"s":"It is clear [[what]] humans are a major contributor to the destruction of nature. Will we be able [[to protect]] the environment [[from]] mountains of plastic?","w":0,"fix":"that","ex":"틀린 곳 ▶ ① what → that\n이유: 가주어 It의 진주어. 뒤가 완전한 문장 → that\n나머지 ▶ ② be able to ✔ ③ protect A from B ✔"},
 {"s":"Can we stop climate change from [[reach]] dangerous levels? Achieving these goals [[seems]] [[difficult]].","w":0,"fix":"reaching","ex":"틀린 곳 ▶ ① reach → reaching\n이유: stop A from -ing\n나머지 ▶ ② 동명사 주어 단수 ✔ ③ seem + 형용사 ✔"},
 {"s":"About fifty percent of plastic [[are]] [[produced]] for single-use products. That means the items are used just once and then [[discarded]].","w":0,"fix":"is","ex":"틀린 곳 ▶ ① are → is\n이유: percent of + plastic(셀 수 없는 명사) → 단수\n나머지 ▶ ② 생산되는 수동 ✔ ③ (are) discarded 수동 병렬 ✔"},
 {"s":"However, less than ten percent of the world's plastic waste [[has recycled]] so far. Often, plastic waste is moved to places [[where]] it is just dumped or [[burned]].","w":0,"fix":"has been recycled","ex":"틀린 곳 ▶ ① has recycled → has been recycled\n이유: 쓰레기가 '재활용되는' 수동\n나머지 ▶ ② 장소 선행사 + 완전한 문장 → where ✔ ③ (is) dumped or burned 수동 병렬 ✔"},
 {"s":"They also want to speed up the process [[which]] the bacteria break down plastic. This may help us [[keep]] our landfills [[plastic-free]].","w":0,"fix":"by which","ex":"틀린 곳 ▶ ① which → by which\n이유: 뒤가 완전한 문장 → 전치사 + 관계대명사\n나머지 ▶ ② help + O + 동사원형 ✔ ③ keep + O + 형용사 ✔"}]
SCR=["A5","A7","A9","B4","B9","B13","B14"]
ORDER=[
 (["A1","A2","A3","A4"],["환경이 위기에 처해 있음","지구 온난화: 해수면 상승, 자연재해 증가","또한(also) 쓰레기도 점점 많아짐","특히(in particular) 플라스틱이 토양·수질 오염"]),
 (["B4","B5","B6","B7"],["재활용은 매립지 플라스틱을 줄일 수 있음","그러나(However) 재활용은 10% 미만","종종(Often) 그냥 버려지거나 태워짐","게다가(Furthermore) 매년 수백만 톤이 바다로"]),
 (["B10","B11","B12","B13"],["밀웜 = 딱정벌레 유충","그 안에 특별한 박테리아가 삶","이 박테리아는 플라스틱을 분해","즉 밀웜은 플라스틱을 먹고 살 수 있음"])]
INSERT=[
 (["A7","A8","A9","A10"],2,["기후 변화를 막을 수 있을까?","이 목표들은 어려워 보임","그러나(however) 자연이 해결책을 줬을지도","여기 변화가 일어나는 세 영역"],"정답 ▶ ②\n이유: '어려워 보인다' 뒤에 however(그러나)로 '자연이 해결책을 줬을지도 모른다'고 뒤집어요. 그리고 these problems의 해결책인 '세 영역'이 이어져요.\n포인트 ▶ however는 앞 내용과 반대되는 내용을 이끌어요."),
 (["B7","B8","B9","B10"],1,["매년 수백만 톤의 플라스틱이 바다로","이것(This)이 해양 종을 위험에 빠뜨림","이를 염두에 두고 과학자들이 밀웜에 눈을 돌림","밀웜 = 딱정벌레 유충"],"정답 ▶ ①\n이유: This는 '플라스틱이 바다로 흘러드는 것'을 가리켜요. 그리고 With this in mind(이것을 염두에 두고)가 바로 그 위험을 받아요."),
 (["B13","B14","B15","B16"],2,["밀웜은 플라스틱을 먹고 살 수 있음","과학자들은 밀웜 밖에서 박테리아를 배양할 방법을 찾음","그들(They)은 또한(also) 분해 속도도 높이고 싶어 함","이것이 매립지를 플라스틱 없게 도울지도"],"정답 ▶ ②\n이유: They = Scientists, also(또한)로 과학자들이 원하는 두 번째 일을 덧붙여요. 그래서 '배양할 방법을 찾는다' 바로 뒤!")]
ODD=[
 (["B1","B2","The first plastic was invented in the early 1900s.","B3"],2,"정답 ▶ ③\n이유: 글은 일회용 플라스틱이 한 번 쓰고 버려진 뒤 어디로 가는지를 이야기해요. 플라스틱이 처음 발명된 시기는 흐름과 관계없어요."),
 (["B11","B12","Because of this, mealworms have become popular pets in many countries.","B13"],2,"정답 ▶ ③\n이유: 박테리아가 플라스틱을 분해한다 → 그래서 밀웜이 플라스틱을 먹고 살 수 있다는 흐름이에요. 애완동물 이야기는 관계없어요.")]
BLANK=[
 {"s":"It is clear that humans are a major ____ to the destruction of nature.","opts":["contributor","victim","solution","witness"],"ex":"정답 ▶ contributor (원인 제공자)\n이유: 인간이 자연 파괴의 '원인'이라는 게 분명하다는 뜻\n오답 ▶ victim 피해자 · solution 해결책 · witness 목격자"},
 {"s":"Nature, however, may have provided us with ____ to these problems.","opts":["solutions","causes","questions","obstacles"],"ex":"정답 ▶ solutions (해결책)\n이유: however로 '어렵다'를 뒤집고, 뒤에서 '변화가 일어나는 세 영역'을 소개해요.\n오답 ▶ causes 원인 · questions 질문 · obstacles 장애물"},
 {"s":"Recycling can help ____ the amount of plastic in our landfills.","opts":["reduce","increase","measure","hide"],"ex":"정답 ▶ reduce (줄이다)\n이유: 재활용하면 매립지의 플라스틱이 줄어요. 다음 문장 However로 '하지만 재활용은 10% 미만'이 이어져요.\n오답 ▶ increase 늘리다 · measure 측정하다 · hide 숨기다"},
 {"s":"This means that mealworms can actually ____ plastic.","opts":["feed on","give up","look for","put off"],"ex":"정답 ▶ feed on (~을 먹고 살다)\n이유: 밀웜 속 박테리아가 플라스틱을 분해 → 밀웜이 플라스틱을 '먹고 살 수' 있어요.\n오답 ▶ give up 포기하다 · look for 찾다 · put off 미루다"},
 {"s":"They also want to ____ the process by which the bacteria break down plastic.","opts":["speed up","slow down","give up","put off"],"ex":"정답 ▶ speed up (속도를 높이다)\n이유: 분해가 빨라야 매립지를 플라스틱 없이(plastic-free) 유지할 수 있어요.\n오답 ▶ slow down 늦추다 · give up 포기하다 · put off 미루다"}]
GRAM=[
 {"q":"빈칸에 알맞은 것은?<br><b>______ the planet becoming warmer, sea levels are rising.</b>","opts":["With","As","Because","When"],"ex":"정답 ▶ With\n이유: with + 명사 + 분사 = ~가 …하면서. As·Because·When은 접속사라 뒤에 동사가 있어야 해요(As the planet becomes warmer).\n본문 ▶ With the planet becoming warmer"},
 {"q":"빈칸에 알맞은 것은?<br><b>More and more waste is also ______ produced.</b>","opts":["being","been","be","to be"],"ex":"정답 ▶ being\n이유: 현재진행 수동태 be being p.p. = ~되고 있다\n본문 ▶ More and more waste is also being produced."},
 {"q":"빈칸에 알맞은 것은?<br><b>______ is clear that humans are a major cause of the problem.</b>","opts":["It","That","What","This"],"ex":"정답 ▶ It\n이유: 가주어 It + 진주어 that절\n본문 ▶ It is clear that humans are a major contributor"},
 {"q":"빈칸에 알맞은 것은?<br><b>We must stop the river from ______ dirty.</b>","opts":["becoming","become","to become","became"],"ex":"정답 ▶ becoming\n이유: stop A from -ing A가 ~하지 못하게 막다 (= prevent/keep A from -ing)\n본문 ▶ stop climate change from reaching dangerous levels"},
 {"q":"밑줄 친 부분의 뜻으로 알맞은 것은?<br><b>Nature <u>may have provided</u> us with solutions.</b>","opts":["제공했을지도 모른다","제공해야 했다","제공했음에 틀림없다","제공했을 리가 없다"],"ex":"정답 ▶ 제공했을지도 모른다\n이유: may have p.p. 과거에 대한 약한 추측\n포인트 ▶ must have p.p. ~했음에 틀림없다 · should have p.p. ~했어야 했다 · can't have p.p. ~했을 리가 없다"},
 {"q":"빈칸에 알맞은 것은?<br><b>The school provides students ______ free lunch.</b>","opts":["with","for","to","of"],"ex":"정답 ▶ with\n이유: provide A with B = provide B for[to] A A에게 B를 제공하다\n본문 ▶ provided us with solutions"},
 {"q":"빈칸에 알맞은 것은?<br><b>Less than ten percent of plastic waste ______ recycled so far.</b>","opts":["has been","have been","has","is being"],"ex":"정답 ▶ has been\n이유: so far(지금까지) → 현재완료, 재활용'되는' 수동 → has been p.p. 주어는 percent of + 셀 수 없는 명사 → 단수 has"},
 {"q":"빈칸에 알맞은 것은?<br><b>This is the process ______ the bacteria break down plastic.</b>","opts":["by which","which","what","by that"],"ex":"정답 ▶ by which\n이유: 뒤가 완전한 문장 → 전치사 + 관계대명사. 전치사 뒤에 that은 못 써요.\n본문 ▶ the process by which the bacteria break down plastic"},
 {"q":"빈칸에 알맞은 것은?<br><b>This may help us ______ our landfills plastic-free.</b>","opts":["keep","keeping","kept","to keeping"],"ex":"정답 ▶ keep\n이유: help + 목적어 + 동사원형/to부정사\n포인트 ▶ keep + 목적어 + 형용사 ~을 …하게 유지하다"}]
