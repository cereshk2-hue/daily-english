VOCAB=[[w,m,n]+x for w,m,n,*x in [
 ["statistics","통계 (자료)","❹"],["generate","~을 만들어 내다, 발생시키다","❹"],["grounds","(커피) 찌꺼기","❹"],["normally","보통, 일반적으로","❹"],
 ["greenhouse gas","온실가스","❹"],["unfortunately","불행하게도","❹"],["emission","배출(량), 배출물","❹"],["turn A into B","A를 B로 바꾸다","❹"],
 ["biofuel","바이오 연료","❹"],["fuel","연료","❹"],["be made from","~로 만들어지다 (원료가 변함)","❹"],["source","원천, 원료","❹"],
 ["researcher","연구자","❹"],["algae","조류(물속에 사는 식물성 생물)","❹"],["nutrient","영양소, 영양분","❹"],["be exposed to","~에 노출되다","❹"],
 ["darkness","어둠","❹"],["eventually","결국, 마침내","❹"],["high-quality","양질의, 고품질의","❹"],["renewable","재생 가능한","❹"],
 ["sustainable","지속 가능한","❹"],["a small amount of","적은 양의","❹"],
 ["possible","가능한","❺"],["currently","현재","❺"],["face","~에 직면하다","❺"],["it seems that","~인 것 같다","❺"],["Mother Nature","대자연","❺"],
 ["chance","기회","❺"],["in return","보답으로, 답례로","❺"],["look for","~을 찾다","❺"],["after all","결국","❺"]]]
PICK1=[
 {"s":"The coffee-making process, however, generates used coffee grounds, which are {normally|rarely} sent to landfills.","ex":"정답 ▶ normally (보통)\n오답 ▶ rarely (좀처럼 ~하지 않는)\n이유: 다음 문장 There(매립지에서) 온실가스가 생긴다고 했으니, 찌꺼기는 '보통' 매립지로 가요."},
 {"s":"There, they can create a {harmful|harmless} greenhouse gas.","ex":"정답 ▶ harmful (해로운)\n오답 ▶ harmless (해가 없는)\n이유: 바로 뒤에 Unfortunately(불행하게도)와 '배출을 줄이자'가 나와요 → 해로운 가스"},
 {"s":"{Unfortunately|Fortunately}, there's no way to stop everyone in the world from drinking coffee.","ex":"정답 ▶ Unfortunately (불행하게도)\n오답 ▶ Fortunately (다행히도)\n이유: 커피를 못 마시게 할 방법이 '없다' → 아쉬운 일. 다음 문장 However로 '그래도 줄일 수는 있다'"},
 {"s":"However, we can {reduce|increase} greenhouse gas emissions by turning used coffee grounds into biofuel.","ex":"정답 ▶ reduce (줄이다)\n오답 ▶ increase (늘리다)\n이유: 찌꺼기를 매립지에 버리지 않고 연료로 바꾸면 온실가스가 '줄어요'."},
 {"s":"Biofuel is a {natural|artificial} fuel that is made from plant or animal sources.","ex":"정답 ▶ natural (천연의)\n오답 ▶ artificial (인공의)\n이유: 식물이나 동물에서 얻은 연료 → 천연 연료"},
 {"s":"Researchers have found that they can grow algae on old coffee grounds without adding any other {nutrients|pollutants}.","ex":"정답 ▶ nutrients (영양분)\n오답 ▶ pollutants (오염 물질)\n이유: 조류를 '키우는' 데 다른 '영양분'을 더할 필요 없이 커피 찌꺼기만으로 충분해요."},
 {"s":"If these algae are {exposed|opposed} to twenty hours of light and four hours of darkness each day, they eventually produce high-quality biofuel.","ex":"정답 ▶ exposed (be exposed to ~에 노출되다)\n오답 ▶ opposed (be opposed to ~에 반대하다)"},
 {"s":"The biofuel is {renewable|removable} and sustainable, and it creates only a small amount of emissions.","ex":"정답 ▶ renewable (재생 가능한)\n오답 ▶ removable (제거할 수 있는)\n이유: sustainable(지속 가능한)과 나란히 → 다시 만들어 쓸 수 있는"},
 {"s":"There could be many more possible solutions to the problems we {currently|previously} face.","ex":"정답 ▶ currently (현재)\n오답 ▶ previously (이전에)\n이유: face(현재시제) → 지금 우리가 직면한 문제들"},
 {"s":"If we do, the future of our planet may be {bright|dark} after all.","ex":"정답 ▶ bright (밝은)\n오답 ▶ dark (어두운)\n이유: If we do(우리가 환경을 지킬 방법을 찾는다면) → 미래가 '밝을' 수 있다는 희망적인 결론"}]
TF=[
 ["Between 30 and 40 percent of people in the world drink coffee every day.",True,"정답 ▶ T\n이유: 통계에 따르면 세계 인구의 약 30~40%가 매일 커피를 마셔요.\n어휘 ▶ every day = each day","❹","about thirty to forty percent of people in the world drink coffee each day"],
 ["Used coffee grounds are usually recycled into new products.",False,"정답 ▶ F\n이유: 보통 매립지로 보내져요(normally sent to landfills).\n어휘 ▶ usually = normally","❹","which are normally sent to landfills"],
 ["Coffee grounds in landfills can give off a harmful gas.",True,"정답 ▶ T\n이유: 매립지에서 해로운 온실가스를 만들어 낼 수 있어요.\n어휘 ▶ give off (가스·냄새 등을) 내뿜다 ≒ create","❹","they can create a harmful greenhouse gas"],
 ["The writer suggests that people should give up drinking coffee.",False,"정답 ▶ F\n이유: 모든 사람이 커피를 못 마시게 할 방법은 없다고 했어요. 대신 찌꺼기를 연료로 바꾸자고 해요.\n어휘 ▶ give up 포기하다","❹","there's no way to stop everyone in the world from drinking coffee"],
 ["Biofuel comes from plant or animal materials.",True,"정답 ▶ T\n이유: 바이오 연료는 식물이나 동물성 원료로 만들어져요.\n어휘 ▶ come from = be made from · materials ≒ sources","❹","made from plant or animal sources"],
 ["Extra nutrients must be added for algae to grow on coffee grounds.",False,"정답 ▶ F\n이유: 다른 영양분을 더하지 않고도 키울 수 있어요.\n어휘 ▶ extra 추가의 = any other","❹","without adding any other nutrients"],
 ["The algae need some hours of darkness each day to produce good biofuel.",True,"정답 ▶ T\n이유: 매일 20시간의 빛과 4시간의 어둠에 노출되면 양질의 바이오 연료를 만들어요.\n어휘 ▶ good = high-quality","❹","four hours of darkness each day"],
 ["Biofuel made from algae gives off large amounts of emissions.",False,"정답 ▶ F\n이유: 적은 양의 배출물만 만들어요.\n어휘 ▶ large ↔ small","❹","only a small amount of emissions"],
 ["The writer says the solutions in the passage are the only ones nature offers.",False,"정답 ▶ F\n이유: 이것들은 자연에서 찾을 수 있는 해결책 중 '몇 가지일 뿐'이에요.\n어휘 ▶ the only ones ↔ just a few","❺","These are just a few solutions we can find in nature"],
 ["The writer believes we should search for more ways to protect the environment in return.",True,"정답 ▶ T\n이유: 보답으로 환경을 건강하고 깨끗하게 지킬 방법을 더 찾아야 해요.\n어휘 ▶ search for = look for · protect ≒ keep ~ healthy and clean","❺","we need to look for more ways to keep the environment healthy and clean"]]
MC=[
 dict(n="❹",box=["❹"],q="본문 ❹의 내용과 <u>일치하는</u> 것은?",opts=[
  "Biofuel from algae can be renewed and used for a long time.",
  "Most people around the world drink coffee every day.",
  "Used coffee grounds are typically turned into fertilizer.",
  "Algae need extra nutrients to grow on coffee grounds.",
  "The algae must be kept in constant light to produce biofuel."],
  ex="정답 ▶ Biofuel from algae can be renewed and used for a long time.\n이유: The biofuel is renewable and sustainable\n오답 ▶ ② 약 30~40%(Most ✗) ③ 보통 매립지로 보내짐 ④ 다른 영양분 없이 ⑤ 20시간 빛 + 4시간 어둠\n포인트 ▶ renewable 재생 가능한 = can be renewed · sustainable 지속 가능한 ≒ used for a long time · typically = normally · constant 끊임없는",
  per=[["조류 바이오 연료는 재생 가능하고 오래 쓸 수 있다.","renewable and sustainable","일치 ✔"],
       ["세계 대부분의 사람이 매일 커피를 마신다.","about thirty to forty percent","most ✗ → 30~40%"],
       ["사용한 커피 찌꺼기는 보통 비료가 된다.","normally sent to landfills","fertilizer ✗ → landfills"],
       ["조류가 커피 찌꺼기에서 자라려면 추가 영양분이 필요하다.","without adding any other nutrients","extra nutrients ✗"],
       ["바이오 연료를 만들려면 조류를 계속 빛에 두어야 한다.","twenty hours of light and four hours of darkness","constant light ✗ → 어둠 4시간도"]]),
 dict(n="❹",box=["❹"],q="본문 ❹의 내용과 일치하지 <u>않는</u> 것은?",opts=[
  "Biofuel is an artificial fuel made from chemicals in factories.",
  "Making coffee leaves behind used grounds.",
  "Coffee grounds sent to landfills can release a harmful gas.",
  "Turning coffee waste into fuel can cut greenhouse gas emissions.",
  "Under a set cycle of light and darkness, algae ultimately produce high-quality biofuel."],
  ex="정답 ▶ Biofuel is an artificial fuel made from chemicals in factories.\n이유: Biofuel is a natural fuel that is made from plant or animal sources. 천연 연료예요.\n오답 ▶ 나머지는 모두 본문을 다른 어휘로 바꿔 쓴 일치 문장\n포인트 ▶ artificial 인공의 ↔ natural · leave behind 남기다 ≒ generate · release 내뿜다 ≒ create · cut = reduce · ultimately = eventually",
  per=[["바이오 연료는 공장에서 화학 물질로 만든 인공 연료이다.","a natural fuel that is made from plant or animal sources","artificial ↔ natural ✗"],
       ["커피를 만들면 사용한 찌꺼기가 남는다.","generates used coffee grounds","leave behind ≒ generate"],
       ["매립지로 간 커피 찌꺼기는 해로운 가스를 내뿜을 수 있다.","they can create a harmful greenhouse gas","release ≒ create"],
       ["커피 쓰레기를 연료로 바꾸면 온실가스 배출을 줄일 수 있다.","reduce greenhouse gas emissions","cut = reduce"],
       ["정해진 빛과 어둠의 주기에서 조류는 결국 양질의 바이오 연료를 만든다.","they eventually produce high-quality biofuel","ultimately = eventually"]]),
 dict(n="❺",box=["❺"],q="본문 ❺의 내용과 <u>일치하는</u> 것은?",opts=[
  "필자는 자연이 우리에게 또 한 번의 기회를 준 것 같다고 말한다.",
  "필자는 본문에 소개된 해결책이 자연이 주는 전부라고 말한다.",
  "우리가 직면한 문제에 대한 해결책은 더 이상 없다.",
  "필자는 환경을 지키기 위해 새로운 방법을 찾을 필요는 없다고 본다.",
  "필자는 지구의 미래가 결국 어두울 것이라고 예측한다."],
  ex="정답 ▶ 필자는 자연이 우리에게 또 한 번의 기회를 준 것 같다고 말한다.\n이유: It seems that Mother Nature has given us one more chance.\n오답 ▶ ② just a few solutions(몇 가지일 뿐) ③ many more possible solutions(훨씬 더 많은 해결책이 있을 수 있음) ④ need to look for more ways(더 찾아야 함) ⑤ may be bright(밝을지도)\n포인트 ▶ in return 보답으로 · after all 결국",
  per=[["","Mother Nature has given us one more chance","일치 ✔"],
       ["","These are just a few solutions","몇 가지일 뿐"],
       ["","many more possible solutions","더 많은 해결책 가능"],
       ["","we need to look for more ways","더 찾아야 함"],
       ["","may be bright after all","밝을지도"]])]
PICK2=[
 {"s":"Statistics show {that|what} about thirty to forty percent of people in the world drink coffee each day.","ex":"정답 ▶ that\n이유: show의 목적어절. 뒤가 완전한 문장 → 접속사 that"},
 {"s":"Statistics show that about thirty to forty percent of people in the world {drink|drinks} coffee each day.","ex":"정답 ▶ drink\n이유: 퍼센트 of + 명사 → of 뒤 명사에 수일치. people(복수) → drink"},
 {"s":"The coffee-making process, however, generates used coffee grounds, {which|that} are normally sent to landfills.","ex":"정답 ▶ which\n이유: 콤마 뒤 계속적 용법 → which (that 불가)"},
 {"s":"The coffee-making process, however, generates used coffee grounds, which are normally {sent|sending} to landfills.","ex":"정답 ▶ sent\n이유: 찌꺼기가 '보내지는' 수동 → are + p.p. (send - sent - sent)"},
 {"s":"Unfortunately, there's no way to stop everyone in the world from {drinking|drink} coffee.","ex":"정답 ▶ drinking\n이유: stop A from -ing"},
 {"s":"However, we can reduce greenhouse gas emissions by {turning|turn} used coffee grounds into biofuel.","ex":"정답 ▶ turning\n이유: 전치사 by + 동명사 ~함으로써\n포인트 ▶ turn A into B A를 B로 바꾸다"},
 {"s":"Biofuel is a natural fuel that {is|are} made from plant or animal sources.","ex":"정답 ▶ is\n이유: 주격 관계대명사 that의 선행사 a natural fuel(단수)"},
 {"s":"Researchers have found that they can grow algae on old coffee grounds without {adding|add} any other nutrients.","ex":"정답 ▶ adding\n이유: 전치사 without + 동명사"},
 {"s":"If these algae {are exposed|expose} to twenty hours of light and four hours of darkness each day, they eventually produce high-quality biofuel.","ex":"정답 ▶ are exposed\n이유: 조류가 빛에 '노출되는' 수동 → be exposed to"},
 {"s":"There could be many more possible solutions to the problems {we currently face|we currently face them}.","ex":"정답 ▶ we currently face\n이유: the problems (that) we currently face — 목적격 관계대명사가 생략된 절. face의 목적어가 앞의 the problems라 them을 또 쓰면 안 돼요."},
 {"s":"It seems {that|what} Mother Nature has given us one more chance.","ex":"정답 ▶ that\n이유: It seems that + 완전한 문장 = ~인 것 같다"},
 {"s":"In return, we need to look for more ways to keep the environment {healthy|healthily} and clean.","ex":"정답 ▶ healthy\n이유: keep + 목적어 + 형용사(목적격보어). and clean(형용사)과도 병렬"}]
VERB=[
 {"s":"Statistics ___ that about thirty to forty percent of people in the world drink coffee each day.","v":"show","a":["show"],"ex":"정답 ▶ show\n이유: Statistics(통계 자료)는 복수 취급 → show\n포인트 ▶ '통계학'이라는 학문일 때만 단수"},
 {"s":"The coffee-making process, however, ___ used coffee grounds, which are normally sent to landfills.","v":"generate","a":["generates"],"ex":"정답 ▶ generates\n이유: 주어 The coffee-making process(단수), 현재시제"},
 {"s":"Biofuel is a natural fuel that is ___ from plant or animal sources.","v":"make","a":["made"],"ex":"정답 ▶ made\n이유: be made from ~로 만들어지다 (수동)"},
 {"s":"Researchers have ___ that they can grow algae on old coffee grounds without adding any other nutrients.","v":"find","a":["found"],"ex":"정답 ▶ found\n이유: have + p.p. 현재완료"},
 {"s":"If these algae are ___ to twenty hours of light and four hours of darkness each day, they eventually produce high-quality biofuel.","v":"expose","a":["exposed"],"ex":"정답 ▶ exposed\n이유: be exposed to ~에 노출되다"},
 {"s":"The biofuel is renewable and sustainable, and it ___ only a small amount of emissions.","v":"create","a":["creates"],"ex":"정답 ▶ creates\n이유: 주어 it(= the biofuel, 단수), 현재시제"},
 {"s":"It seems that Mother Nature has ___ us one more chance.","v":"give","a":["given"],"ex":"정답 ▶ given\n이유: has + p.p. 현재완료 (give - gave - given)"},
 {"s":"In return, we need ___ for more ways to keep the environment healthy and clean.","v":"look","a":["to look"],"ex":"정답 ▶ to look\n이유: need + to부정사 ~할 필요가 있다"}]
ERR=[
 {"s":"Statistics [[shows]] that about thirty to forty percent of people in the world [[drink]] coffee each day. The coffee-making process, however, [[generates]] used coffee grounds, which are normally sent to landfills.","w":0,"fix":"show","ex":"틀린 곳 ▶ ① shows → show\n이유: Statistics(통계 자료)는 복수\n나머지 ▶ ② percent of people(복수) ✔ ③ 주어 process(단수) ✔"},
 {"s":"The coffee-making process, however, generates used coffee grounds, [[that]] are normally [[sent]] to landfills. There, they can [[create]] a harmful greenhouse gas.","w":0,"fix":"which","ex":"틀린 곳 ▶ ① that → which\n이유: 콤마 뒤 계속적 용법에는 that을 못 써요.\n나머지 ▶ ② 보내지는 수동 ✔ ③ can + 동사원형 ✔"},
 {"s":"Unfortunately, there's no way to stop everyone in the world from [[drink]] coffee. However, we can reduce greenhouse gas emissions by [[turning]] used coffee grounds [[into]] biofuel.","w":0,"fix":"drinking","ex":"틀린 곳 ▶ ① drink → drinking\n이유: stop A from -ing (from은 전치사)\n나머지 ▶ ② by + 동명사 ✔ ③ turn A into B ✔"},
 {"s":"Researchers have found that they can grow algae on old coffee grounds without [[add]] any other nutrients. If these algae [[are exposed]] to twenty hours of light and four hours of darkness each day, they [[eventually]] produce high-quality biofuel.","w":0,"fix":"adding","ex":"틀린 곳 ▶ ① add → adding\n이유: 전치사 without + 동명사\n나머지 ▶ ② 노출되는 수동 ✔ ③ 동사 produce 수식 부사 ✔"},
 {"s":"It seems [[what]] Mother Nature [[has given]] us one more chance. In return, we need [[to look]] for more ways to keep the environment healthy and clean.","w":0,"fix":"that","ex":"틀린 곳 ▶ ① what → that\n이유: It seems that + 완전한 문장\n나머지 ▶ ② 현재완료 ✔ ③ need to ✔"},
 {"s":"In return, we need to look for more ways to keep the environment [[healthily]] and clean. If we [[do]], the future of our planet [[may be]] bright after all.","w":0,"fix":"healthy","ex":"틀린 곳 ▶ ① healthily → healthy\n이유: keep + 목적어 + 형용사, and clean과 병렬\n나머지 ▶ ② do = look for more ways(대동사) ✔ ③ may + 동사원형 ✔"}]
SCR=["D3","D5","D6","D7","E2","E4"]
ORDER=[
 (["D1","D2","D3","D4"],["세계 30~40%가 매일 커피를 마심","그러나 커피 찌꺼기가 생기고 보통 매립지로 감","거기서(There) 해로운 온실가스가 생김","불행히도 모두가 커피를 끊게 할 순 없음"]),
 (["D4","D5","D6","D7"],["커피를 끊게 할 순 없음","그러나(However) 찌꺼기를 바이오 연료로 바꿔 배출을 줄일 수 있음","바이오 연료 = 식물·동물 원료의 천연 연료","커피 찌꺼기에서 영양분 없이 조류를 키울 수 있음"]),
 (["E1","E2","E3","E4"],["이것들은 자연 속 해결책 중 일부일 뿐","더 많은 해결책이 있을 수 있음","대자연이 한 번 더 기회를 준 것 같음","보답으로(In return) 환경을 지킬 방법을 더 찾아야"])]
INSERT=[
 (["D2","D3","D4","D5"],1,["커피 찌꺼기는 보통 매립지로","거기서(There) 온실가스가 생김","불행히도 커피를 끊게 할 순 없음","그러나 연료로 바꿔 배출을 줄일 수 있음"],"정답 ▶ ①\n이유: There = landfills(매립지). 매립지가 나온 문장 바로 뒤에 와야 '거기서'가 가리킬 곳이 있어요."),
 (["D6","D7","D8","D9"],2,["바이오 연료의 정의","커피 찌꺼기에서 조류를 키울 수 있음","이 조류(these algae)가 빛·어둠에 노출되면 바이오 연료 생산","이 바이오 연료(The biofuel)는 재생 가능"],"정답 ▶ ②\n이유: these algae는 바로 앞에서 커피 찌꺼기로 키운 조류를 가리켜요. 그리고 다음 문장 The biofuel은 주어진 문장의 high-quality biofuel을 받아요."),
 (["E2","E3","E4","E5"],2,["더 많은 해결책이 있을 수 있음","대자연이 한 번 더 기회를 준 것 같음","보답으로(In return) 환경을 지킬 방법을 더 찾아야","그렇게 하면(If we do) 미래가 밝을지도"],"정답 ▶ ②\n이유: In return(보답으로)은 '기회를 받은 것'에 대한 보답이에요. 그리고 If we do의 do가 '더 많은 방법을 찾는다'를 받아요.")]
ODD=[
 (["D5","D6","Many cafés now offer discounts to customers who bring their own cups.","D7"],2,"정답 ▶ ③\n이유: 글은 커피 찌꺼기를 바이오 연료로 바꾸는 과정을 설명해요. 개인 컵 할인 이야기는 흐름과 관계없어요."),
 (["E1","E2","Unfortunately, most scientists have given up looking for solutions in nature.","E3"],2,"정답 ▶ ③\n이유: 앞뒤는 '자연에 해결책이 더 많을 수 있다 → 자연이 또 기회를 줬다'는 희망적인 흐름이에요. 과학자들이 포기했다는 문장은 흐름과 반대예요.")]
BLANK=[
 {"s":"The coffee-making process, however, ____ used coffee grounds, which are normally sent to landfills.","opts":["generates","removes","recycles","sells"],"ex":"정답 ▶ generates (만들어 내다)\n이유: 커피를 만들면 찌꺼기가 '생겨요'. 그 찌꺼기가 매립지로 가요.\n오답 ▶ removes 제거하다 · recycles 재활용하다 · sells 팔다"},
 {"s":"However, we can reduce greenhouse gas emissions by turning used coffee grounds into ____.","opts":["biofuel","plastic","landfills","coffee beans"],"ex":"정답 ▶ biofuel (바이오 연료)\n이유: 다음 문장에서 바로 바이오 연료를 설명해요(Biofuel is a natural fuel ~).\n오답 ▶ plastic 플라스틱 · landfills 매립지 · coffee beans 커피콩"},
 {"s":"Researchers have found that they can grow algae on old coffee grounds without adding any other ____.","opts":["nutrients","problems","emissions","costs"],"ex":"정답 ▶ nutrients (영양분)\n이유: 식물(조류)을 '키울' 때 더하는 것 → 영양분. 커피 찌꺼기만으로 충분하다는 뜻\n오답 ▶ problems 문제 · emissions 배출물 · costs 비용"},
 {"s":"The biofuel is renewable and ____, and it creates only a small amount of emissions.","opts":["sustainable","harmful","expensive","temporary"],"ex":"정답 ▶ sustainable (지속 가능한)\n이유: renewable(재생 가능한)과 나란히 쓰는 긍정적인 말\n오답 ▶ harmful 해로운 · expensive 비싼 · temporary 일시적인"},
 {"s":"It seems that Mother Nature has given us one more ____.","opts":["chance","disaster","bill","punishment"],"ex":"정답 ▶ chance (기회)\n이유: 다음 문장 In return(보답으로) → 고마운 것을 받았다는 뜻 → 기회\n오답 ▶ disaster 재난 · bill 청구서 · punishment 벌"}]
GRAM=[
 {"q":"빈칸에 알맞은 것은?<br><b>The process generates coffee grounds, ______ are sent to landfills.</b>","opts":["which","that","what","who"],"ex":"정답 ▶ which\n이유: 사물 선행사 + 콤마(계속적 용법) → which. that은 콤마 뒤에 못 써요.\n본문 ▶ used coffee grounds, which are normally sent to landfills"},
 {"q":"빈칸에 알맞은 것은?<br><b>We can reduce emissions by ______ coffee grounds into biofuel.</b>","opts":["turning","turn","turned","to turn"],"ex":"정답 ▶ turning\n이유: 전치사 by + 동명사 ~함으로써"},
 {"q":"빈칸에 알맞은 것은?<br><b>They turned the old factory ______ a museum.</b>","opts":["into","onto","from","with"],"ex":"정답 ▶ into\n이유: turn A into B A를 B로 바꾸다\n본문 ▶ turning used coffee grounds into biofuel"},
 {"q":"빈칸에 알맞은 것은?<br><b>They grew algae without ______ any nutrients.</b>","opts":["adding","add","added","to add"],"ex":"정답 ▶ adding\n이유: 전치사 without + 동명사"},
 {"q":"빈칸에 알맞은 것은?<br><b>If the algae ______ to light, they produce biofuel.</b>","opts":["are exposed","expose","exposing","are exposing"],"ex":"정답 ▶ are exposed\n이유: 조류가 빛에 '노출되는' 수동 → be exposed to"},
 {"q":"다음 문장과 뜻이 같은 것은?<br><b>It seems that Mother Nature has given us one more chance.</b>","opts":["Mother Nature seems to have given us one more chance.","Mother Nature seems to give us one more chance.","Mother Nature seemed to have given us one more chance.","Mother Nature seems giving us one more chance."],"ex":"정답 ▶ Mother Nature seems to have given us one more chance.\n이유: It seems that + 주어 + 동사 = 주어 + seem(s) + to부정사. that절(has given)이 seems(현재)보다 앞선 일 → 완료부정사 to have p.p.\n오답 ▶ ② 시제 차이를 못 나타냄 ③ seemed(과거)로 바뀜 ④ seem + -ing ✗"},
 {"q":"빈칸에 알맞은 것은?<br><b>We need to keep the environment ______.</b>","opts":["clean","cleanly","cleaning","to clean"],"ex":"정답 ▶ clean\n이유: keep + 목적어 + 형용사(목적격보어) ~을 …한 상태로 유지하다\n본문 ▶ to keep the environment healthy and clean"}]
