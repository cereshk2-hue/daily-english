from fw import *
p=P(33,'10월 33번 · 빈칸',[
("Human development is now increasingly understood as an ongoing, flexible, and evolving process rather than a fixed sequence of stages.","인간 발달은 이제 고정된 단계의 연속이 아니라 지속적이고 유연하며 진화하는 과정으로 점점 더 이해되고 있다."),
("At the core of this perspective lies the concept of plasticity.","이 관점의 핵심에는 가소성이라는 개념이 있다."),
("Plasticity refers to the human capacity to change, adapt, and reorganize cognitive, emotional, and behavioural patterns in response to life experiences, environmental demands, and biological changes.","가소성은 삶의 경험, 환경적 요구, 생물학적 변화에 반응하여 인지적·정서적·행동적 패턴을 바꾸고, 적응시키고, 재구성하는 인간의 능력을 가리킨다."),
("It highlights that individuals are not merely passive recipients of development but active agents capable of growth throughout their lives.","그것은 개인이 단지 발달을 수동적으로 받아들이는 존재가 아니라 평생에 걸쳐 성장할 수 있는 능동적인 주체라는 점을 강조한다."),
("In earlier views, development was believed to occur mainly during childhood, with adulthood seen as a period of stability and old age as a phase of decline.","이전의 관점에서는 발달이 주로 아동기에 일어난다고 믿었고, 성인기는 안정의 시기로, 노년기는 쇠퇴의 단계로 여겨졌다."),
("The concept of plasticity challenges this rigid outlook by emphasizing that development continues across the entire lifespan.","가소성 개념은 발달이 전 생애에 걸쳐 계속된다는 점을 강조함으로써 이 경직된 관점에 이의를 제기한다."),
("Although the extent of change may vary at different stages, every phase of life allows room for adaptation and transformation.","변화의 정도는 단계마다 다를 수 있지만, 삶의 모든 단계는 적응과 변화의 여지를 허용한다.")])
VOCAB=[["increasingly","점점 더"],["ongoing","지속적인, 진행 중인"],["flexible","유연한"],["evolve","진화하다, 발전하다"],["fixed","고정된"],["sequence","연속, 순서"],
 ["perspective","관점"],["plasticity","가소성(변화·적응할 수 있는 성질)"],["refer to","~을 가리키다"],["capacity","능력"],["adapt","적응하다"],["reorganize","~을 재구성하다"],
 ["cognitive","인지의"],["in response to","~에 반응하여"],["highlight","~을 강조하다"],["merely","단지"],["passive","수동적인"],["recipient","받는 사람, 수용자"],
 ["agent","주체, 행위자"],["decline","쇠퇴"],["challenge","~에 이의를 제기하다"],["rigid","경직된"],["outlook","관점, 견해"],["lifespan","수명, 생애"],
 ["extent","정도"],["vary","다르다, 달라지다"],["phase","단계"],["room","여지"],["transformation","변화, 변형"]]
EXAM=[EXQ(33,'33. 다음 빈칸에 들어갈 말로 가장 적절한 것은?',p.blank('allows room for adaptation and transformation'),[
 "is independent of the previous change","allows room for adaptation and transformation","leads to less variation in human development","requires stability for meaningful growth to occur","has its own limit in adjusting to new experiences"],1,
 "정답 ▶ ② 적응과 변화의 여지를 허용한다\n이유: 가소성은 발달이 '전 생애에 걸쳐 계속된다(continues across the entire lifespan)'는 개념이에요. Although(변화의 정도는 다를 수 있지만) 뒤에는 '그래도 모든 단계에서 변할 수 있다'가 와야 해요.\n오답 ▶ ① 이전 변화와 무관하다 — 언급 없음 ③ 변화가 줄어든다 — 반대 ④ 안정이 필요하다 — 이전 관점의 성인기 ⑤ 새 경험에 적응하는 데 한계가 있다 — 반대\n포인트 ▶ Although A, B: A(차이)를 인정하고 B(핵심 주장)",v=False),
 EXQ(33,'다음 글의 제목으로 가장 적절한 것은?',p.full(),["Plasticity: Growth Has No Age Limit","Childhood: The Only Window for Development","Why Old Age Means Inevitable Decline","The Fixed Stages of Human Development","How the Environment Controls Our Behavior"],0,
 "정답 ▶ ① 가소성: 성장에는 나이 제한이 없다\n이유: 발달은 아동기에만 일어나는 게 아니라 전 생애에 걸쳐 계속되고, 모든 단계에 적응과 변화의 여지가 있다\n오답 ▶ ② ③ ④ 모두 이 글이 반박하는 '이전 관점' ⑤ 환경은 변화를 일으키는 요인 중 하나일 뿐, 개인은 능동적인 주체\n포인트 ▶ 제목은 핵심 개념(plasticity) + 주장(전 생애 성장)"),
 EXQ(33,'글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳은?',p.insert_q(4,[1,2,3,5,6]),SLOT,3,
 "정답 ▶ ④\n이유: 주어진 문장은 '이전 관점(발달은 아동기에만, 노년은 쇠퇴)'이에요. 다음 문장의 this rigid outlook(이 경직된 관점)이 바로 이것을 가리키니까, 그 문장 바로 앞!\n오답 ▶ ①~③ 아직 가소성 설명 중 ⑤ 이미 경직된 관점을 비판한 뒤\n포인트 ▶ this + 명사(this rigid outlook)는 바로 앞에 가리킬 대상이 있어야 해요.")]
PICK1=[PK(p,'Human development','fixed sequence','changing sequence',"정답 ▶ fixed (고정된)\n오답 ▶ changing (변하는)\n이유: rather than(~가 아니라) → 앞의 ongoing, flexible, evolving과 반대되는 말"),
 PK(p,'It highlights','passive','active',"정답 ▶ passive (수동적인)\n오답 ▶ active (능동적인)\n이유: not merely A but B: A(수동적 수용자)가 아니라 B(능동적 주체)"),
 PK(p,'In earlier views','decline','growth',"정답 ▶ decline (쇠퇴)\n오답 ▶ growth (성장)\n이유: 이전 관점 = 발달은 아동기뿐 → 노년은 '쇠퇴'의 단계"),
 PK(p,'The concept of plasticity','rigid','flexible',"정답 ▶ rigid (경직된)\n오답 ▶ flexible (유연한)\n이유: 가소성이 '반박하는(challenges)' 이전 관점 → 경직된 관점"),
 PK(p,'The concept of plasticity','entire','early',"정답 ▶ entire (전체의)\n오답 ▶ early (초기의)\n이유: 아동기에만이 아니라 '전 생애'에 걸쳐 발달"),
 PK(p,'Although the extent','vary','disappear',"정답 ▶ vary (다르다)\n오답 ▶ disappear (사라지다)\n이유: Although(~이지만)로 '모든 단계에 변화의 여지'와 대비 → 정도는 '다를' 수 있다")]
TF=[TF(p,"Human development is now seen as a fixed series of stages.",False,"rather than a fixed sequence of stages","정답 ▶ F\n이유: 고정된 단계의 연속이 '아니라' 지속적이고 유연한 과정이에요.\n어휘 ▶ series = sequence"),
 TF(p,"Plasticity is the ability to change in response to experiences and surroundings.",True,"in response to life experiences, environmental demands","정답 ▶ T\n어휘 ▶ ability = capacity · surroundings ≒ environment"),
 TF(p,"According to the concept of plasticity, people simply receive development passively.",False,"not merely passive recipients","정답 ▶ F\n이유: 수동적인 수용자가 아니라 능동적인 주체예요."),
 TF(p,"Earlier views held that development happened mostly in childhood.",True,"development was believed to occur mainly during childhood","정답 ▶ T\n어휘 ▶ mostly = mainly · happen = occur"),
 TF(p,"In earlier views, old age was regarded as a time of decline.",True,"old age as a phase of decline","정답 ▶ T\n어휘 ▶ be regarded as = be seen as · time ≒ phase"),
 TF(p,"The amount of change is the same at every stage of life.",False,"the extent of change may vary at different stages","정답 ▶ F\n이유: 변화의 정도는 단계마다 다를 수 있어요.\n어휘 ▶ amount ≒ extent · the same ↔ vary")]
MC=[MC(p,"글의 내용과 일치하지 <u>않는</u> 것은?",["Plasticity suggests that development comes to an end in adulthood.","Development is increasingly viewed as a continuous and changing process.","Plasticity lies at the heart of the modern view of development.","People are seen as active participants in their own growth.","Older views considered adulthood a stable period."],
 "정답 ▶ Plasticity suggests that development comes to an end in adulthood.\n이유: development continues across the entire lifespan. 전 생애에 걸쳐 계속돼요.\n오답 ▶ 나머지는 모두 본문을 다른 어휘로 바꿔 쓴 일치 문장\n포인트 ▶ continuous = ongoing · at the heart of = at the core of · participant ≒ agent · stable = a period of stability",
 [["가소성은 발달이 성인기에 끝난다고 본다.","development continues across the entire lifespan","✗ 전 생애 계속"],["발달은 점점 더 지속적이고 변하는 과정으로 여겨진다.","an ongoing, flexible, and evolving process","continuous = ongoing"],["가소성은 현대 발달 관점의 핵심에 있다.","At the core of this perspective lies the concept of plasticity","at the heart of = at the core of"],["사람들은 자기 성장의 능동적인 참여자로 여겨진다.","active agents capable of growth","participant ≒ agent"],["이전 관점은 성인기를 안정된 시기로 보았다.","adulthood seen as a period of stability","stable ≒ stability"]]),
 MC(p,"글의 내용과 <u>일치하는</u> 것은?",["삶의 모든 단계에는 적응하고 변화할 여지가 있다.","가소성은 생물학적 변화와는 관계가 없다.","이전 관점에서는 발달이 주로 노년기에 일어난다고 보았다.","가소성 개념은 이전의 경직된 관점을 그대로 받아들인다.","변화의 정도는 모든 단계에서 똑같다."],
 "정답 ▶ 삶의 모든 단계에는 적응하고 변화할 여지가 있다.\n이유: every phase of life allows room for adaptation and transformation\n오답 ▶ ② and biological changes에 반응 ③ mainly during childhood ④ challenges(이의를 제기함) ⑤ may vary\n포인트 ▶ room 여지 · challenge 이의를 제기하다",
 [["","every phase of life allows room for adaptation and transformation","일치 ✔"],["","and biological changes","생물학적 변화 포함"],["","mainly during childhood","아동기"],["","challenges this rigid outlook","반박"],["","may vary at different stages","다를 수 있음"]])]
PICK2=[PK(p,'Human development','understood','understanding',"정답 ▶ understood\n이유: 발달이 '이해되는' 수동 → is understood as ~로 이해되다"),
 PK(p,'At the core','lies the','lie the',"정답 ▶ lies\n이유: 장소 부사구(At the core of ~)가 앞으로 나간 도치. 진짜 주어는 the concept(단수)"),
 PK(p,'Plasticity refers','to change','changing',"정답 ▶ to change\n이유: the human capacity to do ~할 수 있는 인간의 능력 (to부정사가 capacity 수식)"),
 PK(p,'It highlights','that individuals','what individuals',"정답 ▶ that\n이유: highlights의 목적어절, 뒤가 완전한 문장 → that"),
 PK(p,'In earlier views','to occur','occurring',"정답 ▶ to occur\n이유: be believed to do ~한다고 믿어지다"),
 PK(p,'The concept of plasticity','emphasizing','emphasize',"정답 ▶ emphasizing\n이유: 전치사 by + 동명사 ~함으로써")]
VERB=[VB(p,'Plasticity refers','reorganize','reorganize',"정답 ▶ reorganize\n이유: to change, adapt, and reorganize — to에 걸리는 동사원형 병렬"),
 VB(p,'In earlier views','seen','see',"정답 ▶ seen\n이유: with + 명사 + 과거분사: 성인기가 '여겨지는' 수동 (see - saw - seen)"),
 VB(p,'The concept of plasticity','continues','continue',"정답 ▶ continues\n이유: that절 주어 development(단수), 현재시제"),
 VB(p,'Although the extent','allows','allow',"정답 ▶ allows\n이유: 주어 every phase(every + 단수명사 → 단수)")]
ERR=[ER(p,'At the core',['At the core',('lies','lie'),'plasticity'],1,'lies',"틀린 곳 ▶ ② lie → lies\n이유: 도치 구문, 진짜 주어는 the concept(단수)\n나머지 ▶ ① 장소 부사구 ✔ ③ ✔"),
 ER(p,'It highlights',[('highlights','highlight'),'passive','capable'],0,'highlights',"틀린 곳 ▶ ① highlight → highlights\n이유: 주어 It(= plasticity, 단수)\n나머지 ▶ ② 명사 수식 형용사 ✔ ③ capable of ~할 수 있는 ✔"),
 ER(p,'In earlier views',[('believed','believing'),'mainly','seen'],0,'believed',"틀린 곳 ▶ ① believing → believed\n이유: 발달이 ~한다고 '믿어졌다' → was believed to\n나머지 ▶ ② 부사 ✔ ③ with + 명사 + p.p. ✔")]
SCR=[1,3,5,6,4]
ORDER=[[0,1,2,3],[3,4,5,6]]
INSERT=[([0,1,2,3],1,"정답 ▶ ①\n이유: this perspective(이 관점)는 첫 문장의 '발달은 지속적이고 유연한 과정'이라는 관점이에요. 다음 문장 Plasticity refers to ~는 주어진 문장의 plasticity를 풀어 설명해요."),
 ([3,4,5,6],2,"정답 ▶ ②\n이유: this rigid outlook(이 경직된 관점)은 바로 앞 '이전 관점(발달은 아동기에만)'을 가리켜요.")]
ODD=[([2,3,"Many children learn a second language more easily than adults do.",4],2,"정답 ▶ ③\n이유: 가소성 설명(능동적 주체) → 이전 관점 소개로 이어지는 흐름이에요. 외국어 학습 속도 비교는 관계없어요.")]
BLANK=[BL(p,'At the core','plasticity',["stability","decline","childhood"],"정답 ▶ plasticity (가소성)\n이유: 다음 문장 Plasticity refers to ~로 바로 설명이 이어져요.\n오답 ▶ stability 안정 · decline 쇠퇴 · childhood 아동기 — 모두 이전 관점의 말"),
 BL(p,'It highlights','active',["silent","temporary","helpless"],"정답 ▶ active (능동적인)\n이유: not merely passive ~ but ~ → passive(수동적)의 반대\n오답 ▶ silent 조용한 · temporary 일시적인 · helpless 무력한"),
 BL(p,'The concept of plasticity','rigid',["flexible","hopeful","modern"],"정답 ▶ rigid (경직된)\n이유: 가소성이 '이의를 제기하는' 관점 = 발달은 아동기에만이라는 굳은 생각\n오답 ▶ flexible 유연한 — 가소성 쪽의 말 · hopeful 희망적인 · modern 현대의")]
GRAM=[{'q':"빈칸에 알맞은 것은?<br><b>At the core of this perspective ______ the concept of plasticity.</b>",'opts':["lies","lie","lying","to lie"],'ex':"정답 ▶ lies\n이유: 장소 부사구 + 동사 + 주어 도치. 주어 the concept(단수)"},
 {'q':"빈칸에 알맞은 것은?<br><b>Individuals are not passive recipients ______ active agents.</b>",'opts':["but","and","or","so"],'ex':"정답 ▶ but\n이유: not (merely) A but B = A가 아니라 B"},
 {'q':"빈칸에 알맞은 것은?<br><b>Development was believed ______ mainly during childhood.</b>",'opts':["to occur","occurring","occur","occurred"],'ex':"정답 ▶ to occur\n이유: 주어 + be believed + to부정사 ~한다고 믿어지다 (= It was believed that development occurred ~)"},
 {'q':"빈칸에 알맞은 것은?<br><b>with adulthood ______ as a period of stability</b>",'opts':["seen","seeing","see","to see"],'ex':"정답 ▶ seen\n이유: with + 명사 + 분사. 성인기가 '여겨지는' 수동 → 과거분사"}]
