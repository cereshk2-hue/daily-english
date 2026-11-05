from fw import *
p=P(23,'10월 23번 · 주제',[
("Research on cephalopod neurobiology suggests that an octopus possesses roughly five hundred million neurons.","두족류 신경생물학 연구는 문어가 약 5억 개의 뉴런을 가지고 있다는 것을 보여 준다."),
("What makes this system unusual is where many of those neurons are located.","이 체계를 특이하게 만드는 것은 그 뉴런 중 상당수가 위치한 곳이다."),
("More than half are distributed throughout the arms rather than concentrated entirely in the central brain.","절반 이상이 중추 뇌에 전부 집중되어 있는 것이 아니라 팔 전체에 분포되어 있다."),
("Each arm contains networks of nerve cells capable of controlling complex movements and responding to sensory input locally.","각 팔에는 복잡한 움직임을 제어하고 감각 입력에 그 자리에서 반응할 수 있는 신경 세포망이 들어 있다."),
("This means that many actions do not require detailed instructions from the brain itself.","이는 많은 동작이 뇌 자체로부터의 세세한 지시를 필요로 하지 않는다는 것을 의미한다."),
("Instead, the arms function as highly capable extensions of the nervous system that interact with the environment directly.","대신, 팔은 환경과 직접 상호 작용하는, 신경계의 매우 유능한 연장선으로 기능한다."),
("The suckers lining each arm play an important role in this process.","각 팔에 줄지어 붙어 있는 빨판은 이 과정에서 중요한 역할을 한다."),
("These structures provide strong grip but also detect chemical signals on surfaces they contact.","이 구조들은 강한 접지력을 제공할 뿐 아니라 닿는 표면의 화학 신호도 감지한다."),
("Marine biologists studying octopus behavior have shown that this allows the animal to gather chemical information through touch.","문어의 행동을 연구하는 해양 생물학자들은 이것이 문어가 촉각을 통해 화학 정보를 모을 수 있게 한다는 것을 보여 주었다."),
("In practical terms, an octopus can effectively taste what it touches.","실질적으로 말하면, 문어는 사실상 자기가 만지는 것을 맛볼 수 있다.")],
"* cephalopod: (오징어, 문어 등의) 두족류 동물 ** sucker: 빨판")
VOCAB=[["neurobiology","신경생물학"],["possess","~을 가지고 있다, 소유하다"],["roughly","대략"],["neuron","뉴런, 신경 세포"],["unusual","특이한, 흔치 않은"],
 ["distribute","~을 분포시키다, 나누어 주다"],["concentrate","~을 집중시키다"],["entirely","전적으로, 완전히"],["nerve cell","신경 세포"],["capable of","~할 수 있는"],
 ["sensory input","감각 입력"],["locally","국소적으로, 그 자리에서"],["instruction","지시"],["function as","~로 기능하다"],["extension","연장(선), 확장된 부분"],
 ["nervous system","신경계"],["interact with","~와 상호 작용하다"],["line","~을 따라 늘어서다"],["grip","꽉 붙잡음, 접지력"],["detect","~을 감지하다"],
 ["chemical signal","화학 신호"],["marine biologist","해양 생물학자"],["in practical terms","실질적으로 말하면"],["effectively","사실상"]]
EXAM=[EXQ(23,'23. 다음 글의 주제로 가장 적절한 것은?',p.full(),[
 "characteristics of an environment that suits an octopus","function of the octopus's central brain in controlling its arms","benefit of an octopus relying more on vision than touch for survival","reasons for octopuses having more neurons than other marine animals","mechanism behind an octopus arms' direct interaction with its surroundings"],4,
 "정답 ▶ ⑤ 문어 팔이 주변 환경과 직접 상호 작용하는 원리\n이유: 뉴런의 절반 이상이 팔에 분포 → 팔이 뇌의 지시 없이 직접 움직이고 반응 → 빨판이 화학 신호까지 감지해 '만지는 것을 맛본다'. 모두 팔이 환경과 '직접(directly)' 상호 작용하는 구조(mechanism) 이야기\n오답 ▶ ① 문어에게 맞는 환경 이야기 아님 ② 중추 뇌가 아니라 '팔'이 핵심(반대) ③ 시각이 아니라 촉각(touch) ④ 다른 해양 동물과 뉴런 수를 비교하지 않음\n포인트 ▶ surroundings = the environment · interaction = interact",v=False),
 EXQ(23,'다음 글의 제목으로 가장 적절한 것은?',p.full(),[
 "Thinking Arms: How an Octopus Senses the World by Touch","The Giant Brain Behind Every Octopus Move","Why Octopuses Prefer Sight to Touch","Suckers: Simple Tools Only for Holding Prey","What Octopuses Learn from Marine Biologists"],0,
 "정답 ▶ ① 생각하는 팔: 문어가 촉각으로 세상을 느끼는 방법\n이유: 뉴런이 팔에 퍼져 있어 팔이 스스로 '생각하듯' 움직이고, 빨판으로 만지는 것을 맛봐요.\n오답 ▶ ② 뇌가 아니라 팔 ③ 촉각이 핵심 ④ 빨판은 붙잡기만 하는 게 아니라 화학 신호도 감지 ⑤ 생물학자는 연구한 사람일 뿐\n포인트 ▶ 제목은 비유(Thinking Arms)로 핵심을 담기도 해요."),
 EXQ(23,'다음 빈칸에 들어갈 말로 가장 적절한 것은?',p.blank('taste what it touches'),[
 "taste what it touches","see in complete darkness","move without any neurons","hear sounds through its skin","change its body color at will"],0,
 "정답 ▶ ① 자기가 만지는 것을 맛보다\n이유: 빨판이 닿는 표면의 화학 신호를 감지 → 촉각으로 화학 정보를 모음 → '실질적으로 말하면(In practical terms)' 만지는 것을 맛보는 셈\n오답 ▶ ② 어둠 속 시각 ③ 뉴런 없이(✗ 팔에 뉴런이 많음) ④ 청각 ⑤ 몸 색깔 → 모두 글에 없는 이야기\n포인트 ▶ In practical terms 뒤에는 앞 내용을 쉬운 말로 정리")]
PICK1=[PK(p,'What makes','unusual','ordinary',"정답 ▶ unusual (특이한)\n오답 ▶ ordinary (평범한)\n이유: 뉴런 대부분이 뇌가 아닌 '팔'에 있다는 점이 특이해요."),
 PK(p,'More than half','scattered','concentrated',"x") if False else {'s':p.sent('More than half').replace('rather than concentrated','rather than {concentrated|scattered}'),'ex':"정답 ▶ concentrated (집중된)\n오답 ▶ scattered (흩어진)\n이유: rather than(~가 아니라)으로 '팔 전체에 분포된(distributed)'과 대조 → 뇌에 '집중된'"},
 PK(p,'This means','detailed','delayed',"정답 ▶ detailed (세세한)\n오답 ▶ delayed (지연된)\n이유: 팔이 스스로 제어하니, 뇌의 '세세한' 지시가 필요 없어요."),
 PK(p,'Instead, the arms','directly','indirectly',"정답 ▶ directly (직접)\n오답 ▶ indirectly (간접적으로)\n이유: Instead(뇌를 거치는 대신) 팔이 환경과 '직접' 상호 작용"),
 PK(p,'These structures','detect','reject',"정답 ▶ detect (감지하다)\n오답 ▶ reject (거부하다)\n이유: 화학 신호를 '감지'해서 촉각으로 화학 정보를 모아요."),
 PK(p,'In practical terms','taste','ignore',"정답 ▶ taste (맛보다)\n오답 ▶ ignore (무시하다)\n이유: 만지면서 화학 정보를 얻으니 사실상 '맛보는' 셈")]
TF=[TF(p,"An octopus has about 500 million neurons.",True,"roughly five hundred million neurons","정답 ▶ T\n이유: 약 5억 개의 뉴런을 가지고 있어요.\n어휘 ▶ about = roughly · five hundred million = 5억"),
 TF(p,"Most of an octopus's neurons are found in its central brain.",False,"More than half are distributed throughout the arms","정답 ▶ F\n이유: 절반 이상이 팔에 분포되어 있어요."),
 TF(p,"Each arm can react to what it senses without waiting for the brain.",True,"responding to sensory input locally","정답 ▶ T\n이유: 각 팔이 감각 입력에 그 자리에서(locally) 반응해요.\n어휘 ▶ react to = respond to"),
 TF(p,"Every arm movement needs detailed orders from the brain.",False,"many actions do not require detailed instructions from the brain itself","정답 ▶ F\n이유: 많은 동작은 뇌의 세세한 지시가 필요 없어요.\n어휘 ▶ orders = instructions"),
 TF(p,"The suckers are used only for holding on to surfaces.",False,"provide strong grip but also detect chemical signals","정답 ▶ F\n이유: 붙잡는 것뿐 아니라 화학 신호도 감지해요.\n어휘 ▶ hold on to ≒ grip"),
 TF(p,"Scientists have found that octopuses collect chemical information by touching things.",True,"gather chemical information through touch","정답 ▶ T\n이유: 촉각을 통해 화학 정보를 모은다는 것을 해양 생물학자들이 보여 줬어요.\n어휘 ▶ collect = gather")]
MC=[MC(p,"글의 내용과 일치하지 <u>않는</u> 것은?",[
 "The octopus's brain must give step-by-step commands for every arm movement.","Over 50 percent of the neurons are spread across the arms.","Octopus arms can handle complicated motions on their own.","The suckers can sense chemicals on the things they touch.","By touching something, an octopus can in effect taste it."],
 "정답 ▶ The octopus's brain must give step-by-step commands for every arm movement.\n이유: many actions do not require detailed instructions from the brain itself\n오답 ▶ 나머지는 모두 본문을 다른 어휘로 바꿔 쓴 일치 문장\n포인트 ▶ step-by-step commands ≒ detailed instructions · spread = distributed · complicated motions = complex movements · on their own ≒ locally · sense = detect · in effect = effectively",
 [["문어의 뇌는 모든 팔 동작에 단계별 명령을 내려야 한다.","do not require detailed instructions from the brain itself","✗ 필요 없음"],["뉴런의 50% 이상이 팔에 퍼져 있다.","More than half are distributed throughout the arms","spread = distributed"],["문어의 팔은 복잡한 동작을 스스로 처리할 수 있다.","capable of controlling complex movements","complicated motions = complex movements"],["빨판은 닿는 물체의 화학 물질을 감지할 수 있다.","detect chemical signals on surfaces they contact","sense = detect"],["무언가를 만지면 문어는 사실상 그것을 맛볼 수 있다.","an octopus can effectively taste what it touches","in effect = effectively"]]),
 MC(p,"글의 내용과 <u>일치하는</u> 것은?",["문어의 팔은 환경과 직접 상호 작용하는 신경계의 연장선 역할을 한다.","문어의 뉴런은 약 5천만 개이다.","문어의 뉴런은 대부분 중추 뇌에 모여 있다.","빨판은 물체를 붙잡는 기능만 한다.","문어는 눈으로 화학 정보를 모은다."],
 "정답 ▶ 문어의 팔은 환경과 직접 상호 작용하는 신경계의 연장선 역할을 한다.\n이유: the arms function as highly capable extensions of the nervous system that interact with the environment directly\n오답 ▶ ② five hundred million = 5억 ③ 절반 이상이 팔에 ④ 화학 신호도 감지 ⑤ 촉각(through touch)으로\n포인트 ▶ hundred million = 억",
 [["","function as highly capable extensions of the nervous system","일치 ✔"],["","roughly five hundred million neurons","5억"],["","More than half are distributed throughout the arms","팔에 분포"],["","but also detect chemical signals","감지도 함"],["","gather chemical information through touch","촉각"]])]
PICK2=[PK(p,'What makes','is where','are where',"정답 ▶ is\n이유: What 명사절(What makes this system unusual) 주어는 단수 → is"),
 PK(p,'What makes','What','That',"정답 ▶ What\n이유: 뒤에 주어가 빠진 불완전한 절(makes this system unusual) + 앞에 선행사 없음 → What(~하는 것)"),
 PK(p,'More than half','are distributed','is distributed',"정답 ▶ are\n이유: More than half (of those neurons) → of 뒤 명사(neurons, 복수)에 수일치"),
 {'s':p.sent('More than half').replace('rather than concentrated','rather than {concentrated|concentrating}'),'ex':"정답 ▶ concentrated\n이유: are distributed ~ rather than (are) concentrated — 수동 병렬"},
 PK(p,'Each arm','responding','respond',"정답 ▶ responding\n이유: capable of controlling ~ and responding — 전치사 of 뒤 동명사 병렬"),
 PK(p,'Marine biologists','to gather','gathering',"정답 ▶ to gather\n이유: allow + 목적어 + to부정사")]
VERB=[VB(p,'Research on','possesses','possess',"정답 ▶ possesses\n이유: that절 주어 an octopus(단수), 현재시제"),
 VB(p,'Each arm','controlling','control',"정답 ▶ controlling\n이유: 전치사 of 뒤 동명사 (capable of -ing)"),
 VB(p,'The suckers','lining','line',"정답 ▶ lining\n이유: 빨판이 팔을 따라 '늘어서 있는' 능동 → 현재분사가 뒤에서 suckers 수식. 문장 동사는 play"),
 VB(p,'Marine biologists','shown','show',"정답 ▶ shown\n이유: have + p.p. 현재완료 (show - showed - shown)")]
ERR=[ER(p,'What makes',['What',('unusual','unusually'),'located'],1,'unusual',"틀린 곳 ▶ ② unusually → unusual\n이유: make + 목적어 + 형용사(목적격보어)\n나머지 ▶ ① 선행사 없는 명사절 What ✔ ③ 위치한(수동) ✔"),
 ER(p,'More than half',[('are','is'),'throughout','concentrated'],0,'are',"틀린 곳 ▶ ① is → are\n이유: More than half (of the neurons) → 복수\n나머지 ▶ ② ~ 전체에 ✔ ③ (are) concentrated 병렬 ✔"),
 ER(p,'The suckers',['lining',('play','plays'),'this process'],1,'play',"틀린 곳 ▶ ② plays → play\n이유: 주어 The suckers(복수). lining each arm은 수식어\n나머지 ▶ ① 현재분사 ✔ ③ ✔")]
SCR=[1,2,4,6,8,9]
ORDER=[[0,1,2,3],[5,6,7,8]]
INSERT=[([3,4,5,6],1,"정답 ▶ ①\n이유: This means that ~의 This는 '각 팔이 그 자리에서 움직임을 제어하고 반응한다'는 앞 문장이에요. 그 뒤 Instead(대신)로 '뇌 대신 팔이 직접' 기능한다고 이어져요."),
 ([6,7,8,9],1,"정답 ▶ ①\n이유: These structures(이 구조들)는 바로 앞의 The suckers(빨판)를 가리켜요. 그리고 다음 문장 this(화학 신호 감지)가 이 문장을 받아요.")]
ODD=[([2,3,"Octopuses are also famous for changing their skin color to hide from predators.",4],2,"정답 ▶ ③\n이유: 뉴런이 팔에 분포 → 팔이 스스로 제어 → 뇌의 지시가 필요 없음으로 이어지는 흐름이에요. 피부색을 바꾸는 위장 이야기는 관계없어요.")]
BLANK=[BL(p,'More than half','distributed',["missing","repaired","replaced"],"정답 ▶ distributed (분포된)\n이유: rather than concentrated(집중된 것이 아니라)와 대조 → 팔 전체에 '퍼져' 있음\n오답 ▶ missing 없어진 · repaired 수리된 · replaced 대체된"),
 BL(p,'Instead, the arms','extensions',["enemies","victims","obstacles"],"정답 ▶ extensions (연장선)\n이유: 팔이 뇌의 일부처럼 신경계를 '연장'해서 환경과 직접 상호 작용\n오답 ▶ enemies 적 · victims 피해자 · obstacles 장애물"),
 BL(p,'Marine biologists','touch',["sight","sound","memory"],"정답 ▶ touch (촉각)\n이유: 빨판이 '닿는' 표면의 화학 신호를 감지 → 촉각으로 정보를 모음. 마지막 문장도 what it touches\n오답 ▶ sight 시각 · sound 소리 · memory 기억")]
GRAM=[{'q':"빈칸에 알맞은 것은?<br><b>______ makes this system unusual is where the neurons are located.</b>",'opts':["What","That","Which","It"],'ex':"정답 ▶ What\n이유: 선행사를 포함한 관계대명사 what이 이끄는 절이 주어(~하는 것)\n포인트 ▶ What makes A B is C = A를 B하게 만드는 것은 C이다"},
 {'q':"빈칸에 알맞은 것은?<br><b>More than half of the neurons ______ in the arms.</b>",'opts':["are","is","being","to be"],'ex':"정답 ▶ are\n이유: 부분 표현(half of + 명사) → of 뒤 명사(neurons, 복수)에 수일치"},
 {'q':"빈칸에 알맞은 것은?<br><b>The arms are capable of ______ complex movements.</b>",'opts':["controlling","control","to control","controlled"],'ex':"정답 ▶ controlling\n이유: be capable of + -ing ~할 수 있다"},
 {'q':"빈칸에 알맞은 것은?<br><b>This allows the animal ______ information through touch.</b>",'opts':["to gather","gathering","gather","gathered"],'ex':"정답 ▶ to gather\n이유: allow + 목적어 + to부정사 ~가 …하게 해 주다"}]
