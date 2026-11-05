from fw import *
p=P(41,'고3 6월 41~42번 · 장문 (제목 · 어휘)',[
("In technological design, an aspiration towards seamlessness aims to make the technological experience for humans blend seamlessly into our everyday lives.","기술 디자인에서 이음매 없음에 대한 열망은 인간의 기술 경험이 일상생활에 매끄럽게 녹아들게 하는 것을 목표로 한다."),
("Essentially, this aspiration aims towards experiences where people are no longer aware of the technology, the interface or the differences between human-technology and human-human interaction.","본질적으로 이 열망은 사람들이 더 이상 기술이나 인터페이스, 또는 인간-기술 상호 작용과 인간-인간 상호 작용의 차이를 의식하지 않는 경험을 지향한다."),
("Considering the metaphor of seams in clothing, we can say that we aspire to seamless aesthetics by stitching the seams closely, pressing them flat and making sure they are hidden on the inside so that we wear clothing rather than pieces of fabric.","옷의 솔기라는 비유를 생각해 보면, 우리는 솔기를 촘촘히 꿰매고 납작하게 다리고 안쪽에 숨겨지도록 해서 이음매 없는 미학을 추구하며, 그래서 천 조각이 아니라 옷을 입는다고 말할 수 있다."),
("When designers and engineers talk about technological seamlessness, they are often referring to ease of use and convenience.","디자이너와 엔지니어가 기술적 이음매 없음에 대해 말할 때, 그들은 흔히 사용하기 쉬움과 편리함을 가리킨다."),
("For example, in interface design, an aspiration towards seamlessness ensures the experience for the user flows and is not stressful or irritating.","예를 들어 인터페이스 디자인에서 이음매 없음에 대한 열망은 사용자의 경험이 매끄럽게 흐르고 스트레스를 주거나 짜증 나지 않도록 보장한다."),
("Most of us would have had experiences of poor interface designs or apps in workplaces that make things more complicated and irritating, and have longed for more seamless interfaces.","우리 대부분은 직장에서 일을 더 복잡하고 짜증 나게 만드는 형편없는 인터페이스 디자인이나 앱을 겪고, 더 매끄러운 인터페이스를 간절히 바란 적이 있을 것이다."),
("Technological seamlessness can also include less visible screens in new technologies, or virtual reality technologies with a seamless technological design.","기술적 이음매 없음은 또한 새로운 기술의 덜 눈에 띄는 화면이나, 이음매 없는 기술 디자인을 갖춘 가상 현실 기술을 포함할 수 있다."),
("The aim is to immerse the user experience such that the visual interaction might be described as inside the screen rather than a body interacting with a digital console or object as separate entities.","그 목표는 사용자 경험을 몰입시켜서, 시각적 상호 작용이 몸이 디지털 콘솔이나 물체와 별개의 존재로 상호 작용하는 것이 아니라 화면 '안'에 있는 것으로 묘사될 수 있게 하는 것이다."),
("Similarly, seamlessness in humanoid robotic design aims to make humanoids indistinguishable from a human body.","마찬가지로, 휴머노이드 로봇 디자인에서 이음매 없음은 휴머노이드를 인간의 몸과 구별할 수 없게 만드는 것을 목표로 한다.")],
"* seamlessness: 이음매 없음 ** aesthetics: 미학 *** immerse: 담그다")
VOCAB=[["aspiration","열망, 포부"],["seamlessness","이음매 없음, 매끄러움"],["blend into","~에 녹아들다, 섞여 들다"],["essentially","본질적으로"],["aware of","~을 의식하는, 알고 있는"],
 ["interface","인터페이스(사용자와 기기를 잇는 화면·장치)"],["interaction","상호 작용"],["metaphor","비유, 은유"],["seam","솔기, 이음매"],["aspire to","~을 열망하다"],
 ["aesthetics","미학"],["stitch","~을 꿰매다"],["fabric","천, 직물"],["refer to","~을 가리키다"],["ease of use","사용하기 쉬움"],["convenience","편리함"],
 ["ensure","~을 보장하다"],["irritating","짜증 나는"],["complicated","복잡한"],["long for","~을 간절히 바라다","longed for"],["visible","눈에 보이는"],
 ["virtual reality","가상 현실"],["immerse","~을 몰입시키다, 담그다"],["entity","존재, 실체"],["indistinguishable","구별할 수 없는"]]
B=p.under([('(a)','aware','aware'),('(b)','hidden','hidden'),('(c)','ensures','ensures'),('(d)','poor','poor'),('(e)','indistinguishable','distinguishable')])
EXAM=[EXQ(41,'41. 윗글의 제목으로 가장 적절한 것은?',B,["Blending In: When Tech Stops Feeling Like Tech","Digital Interfaces Are Becoming Too Complicated!","Out-of-body Experience: A History of Virtual Reality","How Software Designs Affect Work Productivity","Wearable Technology in Contemporary Fashion"],0,
 "정답 ▶ ① 녹아들기: 기술이 더 이상 기술처럼 느껴지지 않을 때\n이유: 이음매 없음 = 사람들이 기술·인터페이스를 '더 이상 의식하지 않는(no longer aware)' 경험, 옷의 숨은 솔기, 매끄러운 인터페이스, 화면 안에 있는 듯한 VR, 인간과 구별 안 되는 휴머노이드 → 모두 기술이 일상에 녹아드는 것\n오답 ▶ ② 복잡한 인터페이스는 이음매 없음이 해결하려는 문제 ③ VR의 역사 아님 ④ 생산성 이야기 아님 ⑤ 옷은 비유일 뿐\n포인트 ▶ blend in 녹아들다 = blend seamlessly into",v=False),
 EXQ(42,'42. 밑줄 친 (a)~(e) 중에서 문맥상 낱말의 쓰임이 적절하지 <u>않은</u> 것은? [3점]',B,["(a) aware","(b) hidden","(c) ensures","(d) poor","(e) distinguishable"],4,
 "정답 ▶ ⑤ (e) distinguishable → indistinguishable\n이유: 이음매 없음은 차이를 '느끼지 못하게' 하는 것이에요. Similarly(마찬가지로)로 VR(몸과 화면이 별개가 아님)과 같은 원리 → 휴머노이드를 인간의 몸과 '구별할 수 없게' 만드는 것\n오답 ▶ (a) 더 이상 '의식하지' 않음 ✔ (b) 솔기가 안쪽에 '숨겨짐' ✔ (c) 매끄러운 경험을 '보장' ✔ (d) '형편없는' 인터페이스가 일을 복잡하게 함 ✔\n포인트 ▶ 접두사 in-/un-/dis- 하나로 정반대가 돼요.",v=False),
 EXQ(41,'다음 글의 요지로 가장 적절한 것은?',p.full(),["기술 디자인은 사용자가 기술을 의식하지 않을 만큼 자연스럽게 일상에 녹아드는 것을 지향한다.","기술 디자인은 인간과 기계의 차이를 분명히 드러내야 한다.","옷의 솔기는 겉으로 드러날수록 아름답다.","가상 현실 기술은 사용자에게 스트레스를 준다.","휴머노이드 로봇은 인간과 확실히 구별되어야 안전하다."],0,
 "정답 ▶ ① 기술 디자인은 사용자가 기술을 의식하지 않을 만큼 자연스럽게 일상에 녹아드는 것을 지향한다.\n이유: 첫 두 문장(이음매 없음 = 일상에 매끄럽게 녹아들어 기술을 의식하지 않게)이 요지, 옷·인터페이스·VR·휴머노이드는 예시\n오답 ▶ ② 차이를 못 느끼게 함 ③ 솔기는 숨김 ④ 스트레스를 '없애는' 것 ⑤ 구별할 수 없게\n포인트 ▶ Essentially(본질적으로) 뒤 = 핵심 정리")]
PICK1=[PK(p,'In technological design','blend seamlessly','blend awkwardly',"정답 ▶ seamlessly (매끄럽게)\n오답 ▶ awkwardly (어색하게)\n이유: 이음매 없음(seamlessness)을 지향 → 일상에 '매끄럽게' 녹아듦"),
 PK(p,'Considering the metaphor','hidden','exposed',"정답 ▶ hidden (숨겨진)\n오답 ▶ exposed (드러난)\n이유: 이음매 없는 미학 → 솔기를 안쪽에 '숨겨서' 천 조각이 아니라 옷을 입는 느낌"),
 PK(p,'For example, in interface','irritating','relaxing',"정답 ▶ irritating (짜증 나는)\n오답 ▶ relaxing (편안한)\n이유: is not stressful or ~ → 스트레스처럼 '부정적인' 말이 와야 해요."),
 PK(p,'Most of us','complicated','convenient',"정답 ▶ complicated (복잡한)\n오답 ▶ convenient (편리한)\n이유: poor(형편없는) 디자인이 만드는 것 → 더 복잡하고 짜증 나게"),
 PK(p,'Technological seamlessness can','visible','expensive',"정답 ▶ visible (눈에 보이는)\n이유: less visible screens = 덜 눈에 띄는 화면 → 기술을 의식하지 않게 함\n오답 ▶ expensive (비싼)"),
 PK(p,'The aim is','separate','connected',"정답 ▶ separate (별개의)\n오답 ▶ connected (연결된)\n이유: rather than(~이 아니라) → 몸과 콘솔이 '별개'인 상호 작용이 아니라 화면 안에 있는 듯한 경험")]
TF=[TF(p,"Seamless design aims to make technology fit naturally into everyday life.",True,"blend seamlessly into our everyday lives","정답 ▶ T\n어휘 ▶ fit naturally into ≒ blend seamlessly into"),
 TF(p,"Seamless technology makes people more conscious of the interface.",False,"people are no longer aware of the technology, the interface","정답 ▶ F\n이유: 더 이상 인터페이스를 의식하지 않게 해요.\n어휘 ▶ conscious of = aware of"),
 TF(p,"In seamless clothing, the seams are hidden on the inside.",True,"they are hidden on the inside","정답 ▶ T"),
 TF(p,"Designers often mean ease of use when they talk about seamlessness.",True,"they are often referring to ease of use and convenience","정답 ▶ T\n어휘 ▶ mean ≒ refer to"),
 TF(p,"Poor interface designs make tasks simpler.",False,"make things more complicated and irritating","정답 ▶ F\n이유: 일을 더 복잡하고 짜증 나게 만들어요."),
 TF(p,"Seamless humanoid robots are designed to look clearly different from humans.",False,"make humanoids indistinguishable from a human body","정답 ▶ F\n이유: 인간의 몸과 구별할 수 없게 만드는 게 목표예요.")]
MC=[MC(p,"글의 내용과 일치하지 <u>않는</u> 것은?",["Virtual reality aims to keep the user's body and the screen clearly separate.","The clothing metaphor shows how hiding seams creates a smooth look.","A seamless interface lets the user's experience flow without stress.","Many people have wished for less frustrating interfaces at work.","Seamless technology may involve screens that are less noticeable."],
 "정답 ▶ Virtual reality aims to keep the user's body and the screen clearly separate.\n이유: inside the screen rather than a body interacting with a digital console or object as separate entities. 별개가 '아니라' 화면 안에 있는 듯하게 해요.\n오답 ▶ 나머지는 모두 본문을 다른 어휘로 바꿔 쓴 일치 문장\n포인트 ▶ wish for = long for · frustrating ≒ irritating · noticeable = visible · involve ≒ include",
 [["가상 현실은 사용자의 몸과 화면을 분명히 분리하는 것을 목표로 한다.","rather than a body interacting with a digital console or object as separate entities","✗ 별개가 아님"],["옷의 비유는 솔기를 숨기면 매끈해 보인다는 것을 보여 준다.","making sure they are hidden on the inside","일치"],["이음매 없는 인터페이스는 사용자 경험이 스트레스 없이 흐르게 한다.","the experience for the user flows and is not stressful","일치"],["많은 사람이 직장에서 덜 답답한 인터페이스를 바랐다.","have longed for more seamless interfaces","wish for = long for"],["이음매 없는 기술은 덜 눈에 띄는 화면을 포함할 수 있다.","less visible screens","noticeable = visible"]]),
 MC(p,"글의 내용과 <u>일치하는</u> 것은?",["옷의 비유에서 우리는 천 조각이 아니라 옷을 입는다고 느끼게 된다.","이음매 없는 기술은 사람과 기술의 차이를 더 잘 느끼게 한다.","디자이너가 말하는 이음매 없음은 주로 화려한 외관을 뜻한다.","형편없는 인터페이스는 일을 더 단순하게 만든다.","휴머노이드 로봇 디자인은 인간과 다르게 보이는 것을 목표로 한다."],
 "정답 ▶ 옷의 비유에서 우리는 천 조각이 아니라 옷을 입는다고 느끼게 된다.\n이유: so that we wear clothing rather than pieces of fabric\n오답 ▶ ② no longer aware ③ ease of use and convenience(사용 편의) ④ more complicated ⑤ indistinguishable\n포인트 ▶ 42번 정답 (e)와 연결",
 [["","we wear clothing rather than pieces of fabric","일치 ✔"],["","no longer aware of","의식하지 않음"],["","ease of use and convenience","편의성"],["","more complicated and irritating","더 복잡"],["","indistinguishable from a human body","구별 불가"]])]
PICK2=[PK(p,'In technological design','blend seamlessly','to blend seamlessly',"정답 ▶ blend\n이유: 사역동사 make + 목적어 + 동사원형"),
 PK(p,'Essentially','where people','which people',"정답 ▶ where\n이유: 선행사 experiences + 뒤가 완전한 문장 → 관계부사 where (상황·경우도 where로 받음)"),
 PK(p,'Considering the metaphor','stitching','stitch',"정답 ▶ stitching\n이유: 전치사 by + 동명사. pressing, making과 병렬"),
 PK(p,'Considering the metaphor','flat','flatly',"정답 ▶ flat\n이유: press + 목적어 + 형용사(목적격보어) ~을 납작하게 누르다"),
 PK(p,'For example, in interface','flows','flow',"정답 ▶ flows\n이유: ensures (that) the experience flows — 생략된 that절의 주어 the experience(단수)"),
 PK(p,'Most of us','that make','that makes',"정답 ▶ make\n이유: that의 선행사 poor interface designs or apps(복수)")]
VERB=[VB(p,'Considering the metaphor','hidden','hide',"정답 ▶ hidden\n이유: 솔기가 '숨겨지는' 수동 → are + p.p. (hide - hid - hidden)"),
 VB(p,'When designers','referring','refer',"정답 ▶ referring\n이유: are + -ing 진행형. refer는 r을 겹쳐 referring"),
 VB(p,'Most of us','longed','long',"정답 ▶ longed\n이유: would have had ~, and (would) have longed — have + p.p. 병렬"),
 VB(p,'The aim is','interacting','interact',"정답 ▶ interacting\n이유: a body가 '상호 작용하는' 능동 → 현재분사가 뒤에서 수식")]
ERR=[ER(p,'In technological design',[('aims','aim'),'blend','seamlessly'],0,'aims',"틀린 곳 ▶ ① aim → aims\n이유: 주어 an aspiration(단수). towards seamlessness는 수식어\n나머지 ▶ ② make O 동사원형 ✔ ③ 동사 수식 부사 ✔"),
 ER(p,'Considering the metaphor',[('stitching','stitch'),'flat','hidden'],0,'stitching',"틀린 곳 ▶ ① stitch → stitching\n이유: 전치사 by + 동명사\n나머지 ▶ ② 목적격보어 형용사 ✔ ③ 숨겨지는 수동 ✔"),
 ER(p,'Most of us',['would have had',('make','makes'),'longed'],1,'make',"틀린 곳 ▶ ② makes → make\n이유: 선행사 poor interface designs or apps(복수)\n나머지 ▶ ① 과거 추측 ✔ ③ (would) have longed 병렬 ✔")]
SCR=[0,3,4,6,8]
ORDER=[[0,1,2,3],[3,4,5,6]]
INSERT=[([1,2,3,4],3,"정답 ▶ ③\n이유: For example, in interface design(예를 들어 인터페이스 디자인에서)은 앞 문장의 '디자이너가 말하는 이음매 없음 = 사용의 편리함'에 대한 예시예요. 맨 끝 자리!"),
 ([5,6,7,8],3,"정답 ▶ ③\n이유: Similarly(마찬가지로)는 앞의 가상 현실 예(몸과 화면이 별개로 느껴지지 않게)와 같은 원리를 휴머노이드에 적용해요. 맨 끝!")]
ODD=[([2,3,"Many fashion brands now make clothing from recycled plastic bottles.",4],2,"정답 ▶ ③\n이유: 옷은 '숨긴 솔기 = 이음매 없음'을 설명하는 비유일 뿐이에요. 재활용 소재로 옷을 만든다는 이야기는 흐름과 관계없어요.")]
BLANK=[BL(p,'Essentially','differences',["prices","rules","distances"],"정답 ▶ differences (차이)\n이유: 이음매 없음 = 기술과 사람 사이의 '경계·차이'를 느끼지 않게 함\n오답 ▶ prices 가격 · rules 규칙 · distances 거리"),
 BL(p,'When designers','convenience',["danger","difficulty","expense"],"정답 ▶ convenience (편리함)\n이유: ease of use(사용하기 쉬움)와 나란히 → 편리함\n오답 ▶ danger 위험 · difficulty 어려움 · expense 비용"),
 BL(p,'Similarly','indistinguishable',["distinguishable","separate","absent"],"정답 ▶ indistinguishable (구별할 수 없는)\n이유: Similarly → VR이 몸과 화면을 별개로 느끼지 않게 하듯, 휴머노이드도 사람과 '구별되지 않게'\n오답 ▶ distinguishable 구별되는(42번 함정) · separate 분리된 · absent 없는")]
GRAM=[{'q':"빈칸에 알맞은 것은?<br><b>Designers aim to make technology ______ into our lives.</b>",'opts':["blend","to blend","blending","blended"],'ex':"정답 ▶ blend\n이유: 사역동사 make + 목적어 + 동사원형"},
 {'q':"빈칸에 알맞은 것은?<br><b>experiences ______ people are no longer aware of the technology</b>",'opts':["where","which","what","who"],'ex':"정답 ▶ where\n이유: 선행사(experiences) + 완전한 문장 → 관계부사 where"},
 {'q':"빈칸에 알맞은 것은?<br><b>The seams are hidden ______ we wear clothing rather than fabric.</b>",'opts':["so that","so as","such as","in order"],'ex':"정답 ▶ so that\n이유: so that + 주어 + 동사 ~하도록, 그래서 ~하다\n오답 ▶ so as to · in order to 뒤에는 동사원형 · such as ~와 같은"},
 {'q':"밑줄 친 부분의 뜻으로 알맞은 것은?<br><b>Most of us <u>would have had</u> experiences of poor designs.</b>",'opts':["(아마) 겪어 본 적이 있을 것이다","겪었어야 했다","겪었을 리가 없다","겪게 될 것이다"],'ex':"정답 ▶ (아마) 겪어 본 적이 있을 것이다\n이유: would have p.p. = 과거에 대한 추측(~했을 것이다)\n포인트 ▶ should have p.p. ~했어야 했다 · can't have p.p. ~했을 리가 없다"}]
