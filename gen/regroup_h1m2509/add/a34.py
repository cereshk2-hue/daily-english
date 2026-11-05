N=34
MC=[
 dict(q="글의 내용과 <u>일치하는</u> 것은?",opts=[
  "Constructing green energy systems itself consumes a great deal of fossil energy.",
  "Heinberg is an American engineer who specializes in solar power.",
  "Solar panels can be made from cheap and plentiful materials.",
  "Switching to renewables only requires installing solar panels and wind turbines.",
  "Most transition proposals carefully calculate construction costs."],
  ex="정답 ▶ Constructing green energy systems itself consumes a great deal of fossil energy.\n이유: the harder we push towards a renewable energy system, the faster we have to use fossil energy for the construction process.\n오답 ▶ ② engineer(기술자) ↔ journalist(언론인) ③ scarce and expensive(희귀하고 비싼) ↔ cheap and plentiful ④ In addition to(~ 외에도) 교통·농업·산업까지 ⑤ seldom counted(좀처럼 계산되지 않음)\n포인트 ▶ consume 소비하다 = use · green energy = renewable energy · plentiful 풍부한 ↔ scarce",
  per=[["친환경 에너지 시스템을 짓는 것 자체가 많은 화석 에너지를 소비한다.","we have to use fossil energy for the construction process","일치 ✔ consume = use"],
       ["Heinberg는 태양광을 전문으로 하는 미국인 기술자이다.","Richard Heinberg, an American journalist","engineer ↔ journalist"],
       ["태양 전지판은 싸고 풍부한 재료로 만들 수 있다.","requires scarce and expensive minerals","plentiful ↔ scarce · cheap ↔ expensive"],
       ["재생 에너지 전환에는 태양 전지판과 풍력 터빈 설치만 필요하다.","In addition to solar panels and wind turbines, we have to build an alternative transport infrastructure","only ✗ → in addition to"],
       ["대부분의 전환 제안서는 건설 비용을 꼼꼼히 계산한다.","is seldom counted in transition proposals","seldom(좀처럼 ~ 않다) ↔ carefully calculate"]]),
 dict(q="글의 내용과 일치하지 <u>않는</u> 것은?",opts=[
  "Pushing harder for renewables slows down our use of fossil fuels during construction.",
  "Heinberg views the shift to renewables as one of the largest change projects in history.",
  "Making concrete and steel needs energy that only fossil fuels can provide.",
  "Extracting minerals for solar panels also involves the use of fossil fuels.",
  "Transition plans tend to concentrate solely on energy supply needs."],
  ex="정답 ▶ Pushing harder for renewables slows down our use of fossil fuels during construction.\n이유: the harder we push ..., the FASTER we have to use fossil energy. 더 빨리 써야 해요.\n오답 ▶ 나머지는 모두 본문을 바꿔 쓴 일치 문장\n포인트 ▶ shift = transition 전환 · extract 추출하다 = excavate 채굴하다 · solely = just 오로지 · concentrate on = focus on",
  per=[["재생 에너지를 강하게 추진할수록 건설 중 화석 연료 사용이 느려진다.","the faster we have to use fossil energy for the construction process","slows down ↔ the faster ✗"],
       ["Heinberg는 재생 에너지 전환을 역사상 가장 큰 변화 프로젝트 중 하나로 본다.","one of the greatest change projects in human history","largest = greatest · shift = building the renewable energy infrastructure"],
       ["콘크리트와 철강을 만드는 데는 화석 연료만 제공할 수 있는 에너지가 필요하다.","only possible to produce with fossil energy","일치"],
       ["태양 전지판용 광물을 캐내는 데도 화석 연료가 쓰인다.","which must be excavated, again requiring the use of fossil fuels","extract ≒ excavate · involve ≒ require"],
       ["전환 계획은 오로지 에너지 공급 요건에만 집중하는 경향이 있다.","which tend to focus just on energy supply requirements","solely = just · concentrate on = focus on · needs = requirements"]]),
 dict(q="글의 내용과 <u>일치하는</u> 것은?",opts=[
  "태양 전지판 생산에 필요한 광물은 희귀하고 값이 비싸다.",
  "Heinberg는 미국의 환경 과학자이다.",
  "재생 에너지로의 전환은 화석 연료 없이도 가능하다.",
  "에너지 전환 제안서는 기반 시설 구축 비용을 자세히 계산한다.",
  "건설에 쓰이는 화석 에너지는 배출량을 줄이는 데 도움이 된다."],
  ex="정답 ▶ 태양 전지판 생산에 필요한 광물은 희귀하고 값이 비싸다.\n이유: Production of solar panels requires scarce and expensive minerals\n오답 ▶ ② journalist = 언론인 ③ cannot happen without fossil fuels ④ seldom counted 좀처럼 계산되지 않음 ⑤ undermining factor 노력을 '약화시키는' 요인\n포인트 ▶ scarce 희귀한, 부족한 · undermine 약화시키다",
  per=[["","requires scarce and expensive minerals","일치 ✔"],
       ["","Richard Heinberg, an American journalist","언론인"],
       ["","This transformation cannot happen without fossil fuels","화석 연료 없이는 불가능"],
       ["","is seldom counted in transition proposals","좀처럼 계산되지 않음"],
       ["","an undermining factor for our efforts to cut global emissions","배출 감축 노력을 약화"]])]
TF=[
 ["Heinberg is a reporter from the United States.",True,"정답 ▶ T\n이유: 미국의 언론인이에요.\n어휘 ▶ reporter 기자 = journalist","Richard Heinberg, an American journalist"],
 ["Heinberg describes building renewable energy infrastructure as a minor change.",False,"정답 ▶ F\n이유: 인류 역사상 가장 거대한 변화 프로젝트 중 하나라고 했어요.\n어휘 ▶ minor 사소한 ↔ greatest","one of the greatest change projects in human history"],
 ["Besides solar panels and wind turbines, new transport systems must also be built.",True,"정답 ▶ T\n이유: 태양 전지판·풍력 터빈 외에도 대체 교통 기반 시설 등을 지어야 해요.\n어휘 ▶ besides = in addition to ~ 외에도","In addition to solar panels and wind turbines"],
 ["The minerals needed for solar panels are abundant and cheap.",False,"정답 ▶ F\n이유: 희귀하고 비싼(scarce and expensive) 광물이에요.\n어휘 ▶ abundant 풍부한 ↔ scarce 희귀한","scarce and expensive minerals"],
 ["The more quickly we move to renewables, the less fossil energy we need for construction.",False,"정답 ▶ F\n이유: 더 강하게 추진할수록 화석 에너지를 '더 빨리' 써야 해요.\n어휘 ▶ the 비교급 ~, the 비교급 … ~할수록 더 …하다","the faster we have to use fossil energy"],
 ["Using fossil energy for construction weakens efforts to reduce global emissions.",True,"정답 ▶ T\n이유: 배출량을 줄이려는 노력을 약화시키는(undermining) 요인이에요.\n어휘 ▶ weaken = undermine 약화시키다 · reduce = cut 줄이다","an undermining factor for our efforts to cut global emissions"],
 ["Transition proposals rarely take the cost of new infrastructure into account.",True,"정답 ▶ T\n이유: 새 기반 시설 구축 비용은 전환 제안서에서 좀처럼 계산되지 않아요.\n어휘 ▶ rarely = seldom · take A into account A를 고려하다 = count","is seldom counted in transition proposals"]]
PICK1=[
 {"s":"Richard Heinberg, an American journalist, argues that in building the renewable energy infrastructure to stop global warming, we are actually {involved|evolved} in one of the greatest change projects in human history.","ex":"정답 ▶ involved (be involved in ~에 관여하다, 참여하다)\n오답 ▶ evolved (진화한)\n포인트 ▶ involve 포함하다, 관련시키다"},
 {"s":"This {transformation|transportation} cannot happen without fossil fuels.","ex":"정답 ▶ transformation (변화, 탈바꿈)\n오답 ▶ transportation (교통, 운송)\n이유: This transformation은 앞 문장의 '교통·농업·산업까지 새로 짓는 거대한 변화'를 가리켜요. 앞에 transport가 나와서 헷갈리기 쉬워요!"},
 {"s":"Production of solar panels requires scarce and expensive minerals which must be {excavated|evacuated}, again requiring the use of fossil fuels.","ex":"정답 ▶ excavated (채굴되다, 파내다)\n오답 ▶ evacuated (대피되다)\n이유: 광물은 땅에서 '캐내야' 하고, 그 과정에도 화석 연료가 쓰여요."},
 {"s":"This is not only expensive, but also an undermining factor for our efforts to cut global {emissions|missions}.","ex":"정답 ▶ emissions (배출, 배출량)\n오답 ▶ missions (임무)\n포인트 ▶ emit 배출하다 → emission. cut emissions 배출량을 줄이다"}]
PICK2=[
 {"s":"Richard Heinberg, an American journalist, argues that in {building|build} the renewable energy infrastructure to stop global warming, we are actually involved in one of the greatest change projects in human history.","ex":"정답 ▶ building\n이유: 전치사 in 뒤 → 동명사. in -ing ~할 때, ~하는 과정에서"},
 {"s":"Richard Heinberg, an American journalist, argues that in building the renewable energy infrastructure to stop global warming, we are actually {involved|involving} in one of the greatest change projects in human history.","ex":"정답 ▶ involved\n이유: be involved in ~에 관여하다 (수동 형태로 굳은 표현)"},
 {"s":"This is not only {expensive|expensively}, but also an undermining factor for our efforts to cut global emissions.","ex":"정답 ▶ expensive\n이유: be동사 뒤 보어 → 형용사. not only A but also B에서 A(expensive, 형용사)와 B(an undermining factor, 명사구) 모두 보어"},
 {"s":"Heinberg remarks that the cost of building this new energy infrastructure is seldom counted in transition proposals, which tend {to focus|focusing} just on energy supply requirements.","ex":"정답 ▶ to focus\n이유: tend to + 동사원형 = ~하는 경향이 있다"}]
VERB=[
 {"s":"Richard Heinberg, an American journalist, argues that in building the renewable energy infrastructure to stop global warming, we are actually ___ in one of the greatest change projects in human history.","v":"involve","a":["involved"],"ex":"정답 ▶ involved\n이유: be involved in ~에 관여하다 → 과거분사"},
 {"s":"Heinberg ___ that the cost of building this new energy infrastructure is seldom counted in transition proposals, which tend to focus just on energy supply requirements.","v":"remark","a":["remarks"],"ex":"정답 ▶ remarks\n이유: 주어 Heinberg(3인칭 단수), 현재시제(앞의 argues와 같은 시제) → remarks"},
 {"s":"Heinberg remarks that the cost of building this new energy infrastructure is seldom counted in transition proposals, which ___ to focus just on energy supply requirements.","v":"tend","a":["tend"],"ex":"정답 ▶ tend\n이유: 계속적 용법 which의 선행사 transition proposals(복수) → tend"}]
ERR=[
 {"s":"Richard Heinberg, an American journalist, [[argue]] that in [[building]] the renewable energy infrastructure [[to stop]] global warming, we are actually involved in one of the greatest change projects in human history.","w":0,"fix":"argues","ex":"틀린 곳 ▶ ① argue → argues\n이유: 주어 Richard Heinberg(단수). an American journalist는 동격 삽입구\n나머지 ▶ ② 전치사 in + 동명사 ✔ ③ to stop ~을 막기 위해(목적) ✔"},
 {"s":"This is not only [[expensively]], but also an [[undermining]] factor for our efforts [[to cut]] global emissions.","w":0,"fix":"expensive","ex":"틀린 곳 ▶ ① expensively → expensive\n이유: be동사 뒤 보어 → 형용사\n나머지 ▶ ② 약화시키는 요인(능동) → 현재분사 ✔ ③ efforts to cut ~을 줄이려는 노력 ✔"},
 {"s":"Heinberg remarks that the cost of building this new energy infrastructure [[is]] seldom [[counted]] in transition proposals, which [[tends]] to focus just on energy supply requirements.","w":2,"fix":"tend","ex":"틀린 곳 ▶ ③ tends → tend\n이유: which의 선행사는 transition proposals(복수)\n나머지 ▶ ① 주어 the cost(단수) ✔ ② 비용이 '계산되는' 수동 ✔"}]
SCR=[6,7,1,4]
ORDER=[{"idx":[0,1,2,3],"flow":["Heinberg: 재생 에너지 구축 = 역사상 최대 변화 프로젝트","태양광·풍력 외에 교통·농업·산업도 새로 지어야","이 변화는 화석 연료 없이 불가능","예: 콘크리트·철강 생산엔 화석 에너지가 필요"]}]
INSERT=[{"idx":[4,5,6,7],"given":2,"flow":["태양 전지판 광물 채굴에도 화석 연료","따라서 강하게 추진할수록 화석 에너지를 더 빨리 씀","이건 비쌀 뿐 아니라 배출 감축 노력도 약화","하지만 이 비용은 전환 제안서에서 거의 계산 안 됨"],"ex":"정답 ▶ ②\n이유: 주어진 문장의 This는 '건설에 화석 에너지를 더 빨리 쓰는 것'을 가리켜요. 그래서 Thus 문장 바로 뒤!\n포인트 ▶ not only expensive(비용) → 마지막 문장의 the cost(비용)로 이어져요."}]
ODD=[{"lines":[0,1,"Fortunately, these new systems can be built using only the clean energy they produce.",2],"odd":2,"ex":"정답 ▶ ③\n이유: 바로 다음 문장이 '이 변화는 화석 연료 없이는 일어날 수 없다'예요. 깨끗한 에너지만으로 지을 수 있다는 문장은 정반대예요."}]
BLANK=[
 {"s":"Production of solar panels requires ____ and expensive minerals which must be excavated, again requiring the use of fossil fuels.","opts":["scarce","plentiful","recycled","lightweight"],"ex":"정답 ▶ scarce (희귀한)\n이유: and expensive(비싼)와 나란히 → 구하기 어려운 광물\n오답 ▶ plentiful 풍부한 · recycled 재활용된 · lightweight 가벼운"},
 {"s":"This is not only expensive, but also an ____ factor for our efforts to cut global emissions.","opts":["undermining","encouraging","unrelated","essential"],"ex":"정답 ▶ undermining (약화시키는)\n이유: 재생 에너지를 지으려고 화석 에너지를 더 빨리 쓰면 배출 감축 노력이 '약해져요'.\n오답 ▶ encouraging 장려하는 · unrelated 관계없는 · essential 필수적인"},
 {"s":"Heinberg remarks that the cost of building this new energy infrastructure is ____ counted in transition proposals, which tend to focus just on energy supply requirements.","opts":["seldom","always","carefully","fully"],"ex":"정답 ▶ seldom (좀처럼 ~하지 않는)\n이유: 제안서는 에너지 공급 요건에'만(just)' 집중 → 건설 비용은 거의 계산하지 않아요.\n오답 ▶ always 항상 · carefully 꼼꼼히 · fully 완전히"}]
GRAM=[
 {"q":"빈칸에 알맞은 것은?<br><b>This plan is not only expensive ______ also dangerous.</b>","opts":["but","and","or","so"],"ex":"정답 ▶ but\n이유: not only A but (also) B = A뿐만 아니라 B도\n본문 ▶ This is not only expensive, but also an undermining factor"},
 {"q":"빈칸에 알맞은 것은?<br><b>People tend ______ on short-term costs.</b>","opts":["to focus","focusing","focus","focused"],"ex":"정답 ▶ to focus\n이유: tend to + 동사원형 ~하는 경향이 있다\n본문 ▶ which tend to focus just on energy supply requirements"},
 {"q":"다음 중 어법상 <b>틀린</b> 것은?","opts":["I read the proposals, that focus only on supply.","I read the proposals, which focus only on supply.","I read the proposals that focus only on supply.","I read the proposals which focus only on supply."],"ex":"정답 ▶ I read the proposals, that focus only on supply.\n이유: 콤마 뒤 계속적 용법에는 that을 쓸 수 없어요 → which\n본문 ▶ transition proposals, which tend to focus"},
 {"q":"빈칸에 알맞은 것은?<br><b>In addition to ______ solar panels, we need new roads.</b>","opts":["building","build","built","builds"],"ex":"정답 ▶ building\n이유: in addition to의 to는 전치사 → 명사나 동명사\n본문 ▶ In addition to solar panels and wind turbines"}]
