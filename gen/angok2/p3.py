from fw import *
p=P(31,'10월 31번 · 빈칸',[
("A person who lives eighty years lives some twenty-nine thousand days, and the overwhelming majority of the behaviour packed into them runs on settings laid down, most of them, decades earlier and rarely inspected since.","80년을 사는 사람은 약 2만 9천 일을 살며, 그 날들에 채워진 행동의 압도적 다수는 대부분 수십 년 전에 정해지고 그 이후로 거의 점검되지 않은 설정에 따라 작동한다."),
("This need not be a hopeless thought.","이것이 절망적인 생각일 필요는 없다."),
("In one light it is a triumph of engineering.","어떤 관점에서 보면 그것은 공학의 승리이다."),
("If you had to consciously decide every footstep and every fork-grip and every word, you would never make it out of bed; the deliberate mind is far too slow and too costly to run a whole life in real time, and any creature that tried would be outcompeted by a creature that didn't.","걸음 하나, 포크 쥐기 하나, 말 한마디까지 모두 의식적으로 결정해야 한다면 침대에서 나오지도 못할 것이다. 숙고하는 정신은 삶 전체를 실시간으로 운영하기에는 너무 느리고 비용이 너무 많이 들며, 그렇게 하려는 생물은 그러지 않는 생물에게 경쟁에서 밀릴 것이다."),
("The automation is precisely what frees the captain to come up on deck for the few problems that actually require him.","자동화야말로 선장이 실제로 그를 필요로 하는 몇 안 되는 문제를 위해 갑판으로 올라올 수 있게 해 주는 바로 그것이다."),
("The default is not a flaw in the human design.","기본 설정은 인간 설계의 결함이 아니다."),
("It is arguably the central feature, the thing that makes a complex life affordable at all.","그것은 아마도 핵심적인 특징, 즉 복잡한 삶을 감당할 수 있게 해 주는 바로 그것이다.")],
"* default: 기본 설정")
VOCAB=[["overwhelming","압도적인"],["majority","대다수"],["pack into","~에 채워 넣다","packed into"],["run on","~로 작동하다"],["setting","설정"],
 ["lay down","~을 정하다, 확립하다","laid down"],["rarely","거의 ~하지 않는"],["inspect","~을 점검하다"],["need not","~할 필요가 없다","need not be"],["hopeless","절망적인"],
 ["in one light","어떤 관점에서 보면"],["triumph","승리, 대성공"],["consciously","의식적으로"],["make it out of","~에서 (간신히) 빠져나오다","make it out of bed"],
 ["deliberate","숙고하는, 신중한"],["costly","비용이 많이 드는"],["in real time","실시간으로"],["outcompete","경쟁에서 이기다"],["precisely","바로, 정확히"],
 ["free A to do","A가 ~할 수 있게 해 주다","frees the captain to"],["default","기본 설정"],["flaw","결함"],["arguably","아마도, 거의 틀림없이"],["affordable","감당할 수 있는"]]
EXAM=[EXQ(31,'31. 다음 빈칸에 들어갈 말로 가장 적절한 것은?',p.blank('automation'),["reflection","automation","prediction","manipulation","calculation"],1,
 "정답 ▶ ② automation (자동화)\n이유: 행동 대부분이 오래전 정해진 '설정'대로 자동으로 돌아가요. 모든 것을 의식적으로 결정하면 침대에서 나오지도 못하니, 이 '자동화'가 선장(의식적인 정신)을 정말 필요한 문제에만 나서게 해 줘요. 다음 문장의 The default(기본 설정)와 같은 말\n오답 ▶ ① reflection 숙고 — 오히려 너무 느리고 비싼 쪽 ③ prediction 예측 ④ manipulation 조작 ⑤ calculation 계산 — 모두 '설정대로 저절로 돌아감'과 무관\n포인트 ▶ 빈칸 = 글 전체의 핵심 개념(settings, default)",v=False),
 EXQ(31,'다음 글의 주제로 가장 적절한 것은?',p.full(),["the value of automatic habits in managing a complex life","the dangers of relying on old habits","how to consciously control every single action","why machines will replace human decision-making","the high cost of large engineering projects"],0,
 "정답 ▶ ① 복잡한 삶을 꾸려 가는 데 있어 자동화된 습관의 가치\n이유: 오래된 설정대로 돌아가는 행동은 절망적인 게 아니라 '공학의 승리', 복잡한 삶을 감당하게 해 주는 핵심 특징이라는 글\n오답 ▶ ② 위험이 아니라 가치 ③ 모든 것을 의식적으로 하면 침대에서도 못 나옴 ④ 기계 이야기 아님(engineering은 비유) ⑤ 비용(costly)은 숙고하는 정신의 단점일 뿐\n포인트 ▶ need not be a hopeless thought → 통념 뒤집기"),
 EXQ(31,'밑줄 친 부분이 다음 글에서 의미하는 바로 가장 적절한 것은?',p.full(p.text().replace('The default is not a flaw in the human design.','<u>The default is not a flaw in the human design.</u>')),[
 "Automatic behaviors are an essential part of how humans are built to function.","Humans should replace their habits with conscious decisions.","Our default settings are mistakes that need to be fixed.","Human design is too slow to work in real time.","Most human behaviors are designed by engineers."],0,
 "정답 ▶ ① 자동화된 행동은 인간이 기능하도록 만들어진 방식의 필수적인 부분이다.\n이유: 바로 뒤 '그것은 핵심 특징이며 복잡한 삶을 감당하게 해 준다' → 기본 설정은 결함이 아니라 '필수 기능'\n오답 ▶ ② 의식적 결정은 너무 느리고 비쌈 ③ 결함이 아니라고 함(반대) ④ 느린 것은 '숙고하는 정신' ⑤ engineering은 비유\n포인트 ▶ 밑줄 의미 = 바로 뒤 문장이 풀어 줘요.")]
PICK1=[PK(p,'A person who','rarely','frequently',"정답 ▶ rarely (거의 ~ 않는)\n오답 ▶ frequently (자주)\n이유: 수십 년 전에 정해진 뒤 '거의 점검되지 않은' 설정 → 자동으로 돌아감"),
 PK(p,'This need not','hopeless','hopeful',"정답 ▶ hopeless (절망적인)\n오답 ▶ hopeful (희망적인)\n이유: '오래된 설정대로 산다'는 게 절망적으로 들릴 수 있지만 그럴 필요 없다 → 다음 문장 '공학의 승리'로 반전"),
 PK(p,'In one light','triumph','failure',"정답 ▶ triumph (승리, 대성공)\n오답 ▶ failure (실패)\n이유: 앞 문장 '절망할 필요 없다'와 같은 방향 → 긍정"),
 PK(p,'If you had to','slow','fast',"정답 ▶ slow (느린)\n오답 ▶ fast (빠른)\n이유: 모든 걸 의식적으로 결정하면 침대에서도 못 나옴 → 숙고하는 정신은 '너무 느림'"),
 PK(p,'It is arguably','affordable','impossible',"정답 ▶ affordable (감당할 수 있는)\n오답 ▶ impossible (불가능한)\n이유: 기본 설정 덕분에 복잡한 삶을 '감당할' 수 있어요. 핵심 특징(central feature)과 같은 방향")]
TF=[TF(p,"Someone who lives to 80 lives about 29,000 days.",True,"lives some twenty-nine thousand days","정답 ▶ T\n어휘 ▶ some + 숫자 = 약 · twenty-nine thousand = 2만 9천"),
 TF(p,"Most of our everyday behavior follows settings formed long ago.",True,"runs on settings laid down","정답 ▶ T\n이유: 행동의 압도적 다수가 수십 년 전에 정해진 설정대로 돌아가요.\n어휘 ▶ form = lay down · long ago = decades earlier"),
 TF(p,"We regularly check and update most of our behavioral settings.",False,"rarely inspected since","정답 ▶ F\n이유: 그 이후로 거의 점검되지 않아요.\n어휘 ▶ check = inspect · regularly ↔ rarely"),
 TF(p,"The writer sees our automatic behavior as a hopeless problem.",False,"This need not be a hopeless thought","정답 ▶ F\n이유: 절망적인 생각일 필요가 없다고 했어요."),
 TF(p,"Consciously deciding every small action would be too slow and costly.",True,"the deliberate mind is far too slow and too costly","정답 ▶ T\n어휘 ▶ deliberate mind 숙고하는 정신 = consciously deciding"),
 TF(p,"The writer thinks our default settings are a defect in human design.",False,"The default is not a flaw in the human design","정답 ▶ F\n이유: 결함이 아니라 핵심 특징이라고 했어요.\n어휘 ▶ defect = flaw")]
MC=[MC(p,"글의 내용과 일치하지 <u>않는</u> 것은?",["Creatures that consciously decide every action have a competitive advantage.","The bulk of our behavior relies on settings from decades ago.","Our automatic settings are seldom examined once they are formed.","Automation lets the conscious mind deal with the few problems that need it.","Defaults make a complicated life manageable."],
 "정답 ▶ Creatures that consciously decide every action have a competitive advantage.\n이유: any creature that tried would be outcompeted by a creature that didn't. 오히려 경쟁에서 밀려요.\n오답 ▶ 나머지는 모두 본문을 다른 어휘로 바꿔 쓴 일치 문장\n포인트 ▶ bulk 대부분 = majority · seldom examined = rarely inspected · manageable = affordable · competitive advantage ↔ be outcompeted",
 [["모든 행동을 의식적으로 결정하는 생물이 경쟁 우위를 갖는다.","would be outcompeted by a creature that didn't","✗ 경쟁에서 밀림"],["우리 행동의 대부분은 수십 년 전의 설정에 의존한다.","the overwhelming majority of the behaviour","bulk = majority"],["자동 설정은 일단 만들어지면 좀처럼 점검되지 않는다.","rarely inspected since","seldom examined = rarely inspected"],["자동화는 의식적인 정신이 필요한 몇 안 되는 문제를 다루게 해 준다.","frees the captain to come up on deck for the few problems","captain = 의식적인 정신(비유)"],["기본 설정은 복잡한 삶을 감당할 만하게 만든다.","makes a complex life affordable at all","manageable = affordable"]]),
 MC(p,"글의 내용과 <u>일치하는</u> 것은?",["자동화된 행동 덕분에 의식적인 정신은 정말 필요한 문제에만 나설 수 있다.","80년을 사는 사람은 약 2천 9백 일을 산다.","필자는 기본 설정이 인간 설계의 결함이라고 본다.","숙고하는 정신은 삶 전체를 실시간으로 운영할 만큼 빠르다.","모든 행동을 의식적으로 결정하는 생물이 경쟁에서 이긴다."],
 "정답 ▶ 자동화된 행동 덕분에 의식적인 정신은 정말 필요한 문제에만 나설 수 있다.\n이유: The automation is precisely what frees the captain to come up on deck for the few problems that actually require him.\n오답 ▶ ② twenty-nine thousand = 2만 9천 ③ not a flaw ④ far too slow ⑤ would be outcompeted\n포인트 ▶ captain(선장) = 의식, 배의 자동 운항 = 습관이라는 비유",
 [["","for the few problems that actually require him","일치 ✔"],["","some twenty-nine thousand days","2만 9천 일"],["","is not a flaw","결함 아님"],["","far too slow","너무 느림"],["","would be outcompeted","밀림"]])]
PICK2=[PK(p,'A person who','runs on','run on',"정답 ▶ runs\n이유: the overwhelming majority of the behaviour → of 뒤 behaviour(셀 수 없는 명사)에 맞춰 단수"),
 PK(p,'A person who','packed into','packing into',"정답 ▶ packed\n이유: 행동이 날들 속에 '채워진' 수동 → 과거분사가 behaviour를 뒤에서 수식"),
 PK(p,'This need not','be a','to be a',"정답 ▶ be\n이유: 조동사 need not + 동사원형"),
 PK(p,'If you had to','would never','will never',"정답 ▶ would\n이유: If + 과거(had to), 주어 + would + 동사원형 → 가정법 과거(현재 사실과 반대 가정)"),
 PK(p,'If you had to','to run','running',"정답 ▶ to run\n이유: too + 형용사 + to부정사 = 너무 ~해서 …할 수 없다"),
 PK(p,'The automation','what frees','that frees',"정답 ▶ what\n이유: is 뒤 보어 자리에 선행사 없는 명사절 → what(~하는 것)")]
VERB=[VB(p,'A person who','laid','lay',"정답 ▶ laid\n이유: 설정이 '정해진' 수동 → 과거분사 (lay - laid - laid)\n포인트 ▶ lie(눕다) - lay - lain과 헷갈리지 않기!"),
 VB(p,'A person who','inspected','inspect',"정답 ▶ inspected\n이유: 설정이 '점검되는' 수동 → 과거분사 (laid down and rarely inspected 병렬)"),
 VB(p,'If you had to','outcompeted','outcompete',"정답 ▶ outcompeted\n이유: would be + p.p. 수동 (경쟁에서 밀리다)"),
 VB(p,'The automation','to come','come',"정답 ▶ to come\n이유: free + 목적어 + to부정사 ~가 …할 수 있게 해 주다")]
ERR=[ER(p,'A person who',[('lives','live'),'packed','laid'],0,'lives',"틀린 곳 ▶ ① live → lives\n이유: 주격 관계대명사 who의 선행사 A person(단수)\n나머지 ▶ ② 채워진(수동) ✔ ③ 정해진(수동, lay - laid - laid) ✔"),
 ER(p,'The automation',[('what','that'),'frees','to come'],0,'what',"틀린 곳 ▶ ① that → what\n이유: 선행사가 없고 뒤가 불완전(주어 빠짐) → what\n나머지 ▶ ② 주어 what절(단수) ✔ ③ free O to-v ✔"),
 ER(p,'It is arguably',['arguably',('makes','make'),'affordable'],1,'makes',"틀린 곳 ▶ ② make → makes\n이유: that의 선행사 the thing(단수)\n나머지 ▶ ① 부사 ✔ ③ make + O + 형용사 ✔")]
SCR=[1,2,4,5,6]
ORDER=[[0,1,2,3],[3,4,5,6]]
INSERT=[([0,1,2,3],1,"정답 ▶ ①\n이유: This need not be a hopeless thought의 This는 '행동 대부분이 오래전 설정대로 돌아간다'는 첫 문장이에요. 그다음 In one light(어떤 관점에서는) '공학의 승리'로 반전해요."),
 ([3,4,5,6],2,"정답 ▶ ②\n이유: '기본 설정은 결함이 아니다' 바로 뒤에 It is arguably the central feature(오히려 핵심 특징)가 와야 해요. It = The default")]
ODD=[([1,2,"Many engineers today design robots that can walk and hold forks like humans.",3],2,"정답 ▶ ③\n이유: engineering(공학)은 인간의 자동화된 행동을 비유한 말이에요. 실제 로봇 공학 이야기는 흐름과 관계없어요.")]
BLANK=[BL(p,'This need not','hopeless',["happy","new","simple"],"정답 ▶ hopeless (절망적인)\n이유: '수십 년 전 설정대로 산다'는 말이 절망적으로 들릴 수 있지만 그럴 필요 없다 → 다음 문장 '공학의 승리'\n오답 ▶ happy 행복한 · new 새로운 · simple 단순한"),
 BL(p,'If you had to','costly',["cheap","simple","quiet"],"정답 ▶ costly (비용이 많이 드는)\n이유: too slow and too ~ → 둘 다 숙고하는 정신의 '단점'\n오답 ▶ cheap 값싼 · simple 단순한 · quiet 조용한"),
 BL(p,'The default','flaw',["feature","part","success"],"정답 ▶ flaw (결함)\n이유: 다음 문장 It is arguably the central feature(오히려 핵심 특징) → '결함이 아니다'\n오답 ▶ feature 특징 — 다음 문장과 모순 · part 부분 · success 성공")]
GRAM=[{'q':"빈칸에 알맞은 것은?<br><b>If you had to decide every step, you ______ never get out of bed.</b>",'opts':["would","will","can","are"],'ex':"정답 ▶ would\n이유: 가정법 과거: If + 주어 + 과거동사, 주어 + would/could + 동사원형 (현재 사실의 반대)"},
 {'q':"빈칸에 알맞은 것은?<br><b>This need not ______ a hopeless thought.</b>",'opts':["be","to be","being","been"],'ex':"정답 ▶ be\n이유: 조동사 need not + 동사원형 (= don't need to be)"},
 {'q':"빈칸에 알맞은 것은?<br><b>The mind is too slow ______ a whole life in real time.</b>",'opts':["to run","running","run","ran"],'ex':"정답 ▶ to run\n이유: too + 형용사 + to부정사 너무 ~해서 …할 수 없다"},
 {'q':"빈칸에 알맞은 것은?<br><b>Automation is precisely ______ frees the captain.</b>",'opts':["what","that","which","where"],'ex':"정답 ▶ what\n이유: 선행사 없는 관계대명사 what(~하는 것) — 보어 자리 명사절"}]
