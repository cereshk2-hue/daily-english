from fw import *
p=P(41,'10월 41~42번 · 장문 (제목 · 어휘)',[
("It is crucial to recognize that boredom can give rise to harmful emotions such as depression, despair, and irritation if not adequately addressed.","지루함이 적절히 다루어지지 않으면 우울, 절망, 짜증 같은 해로운 감정을 일으킬 수 있다는 것을 인식하는 것이 매우 중요하다."),
("When we believe that the only way to be happy is by searching for fun activities, then we become dependent on those activities, and negative thoughts and emotions arise.","행복해지는 유일한 방법이 재미있는 활동을 찾는 것이라고 믿으면, 우리는 그런 활동에 의존하게 되고 부정적인 생각과 감정이 생겨난다."),
("It is suggested that 'Idle time is the devil's workshop' implies that those with too much time on their hands may fill that time with troubling thoughts and behavior.","'한가한 시간은 악마의 작업장'이라는 말은 시간이 너무 많은 사람들이 그 시간을 골치 아픈 생각과 행동으로 채울 수 있다는 것을 암시한다고 한다."),
("The balance is to not see it as idle time, wasted time, or boredom but rather as a perfect time for self-improvement, self-identification, and positive reflection time.","균형은 그것을 한가한 시간, 낭비된 시간, 지루함으로 보지 않고, 오히려 자기 계발, 자기 정체성 확인, 긍정적인 성찰을 위한 완벽한 시간으로 보는 것이다."),
("Reflecting, just how lucky are we to be bored?","생각해 보면, 지루할 수 있다니 우리는 얼마나 운이 좋은가?"),
("Boredom doesn't exist in the presence of danger, as it is only an indulgence pastime in a safe zone.","지루함은 안전한 영역에서만 누리는 탐닉의 소일거리이기 때문에 위험이 있는 곳에서는 존재하지 않는다."),
("Boredom can be perceived as a luxury that typically manifests in safe and inactive situations, providing an occasion to appreciate and comprehend the environment.","지루함은 대개 안전하고 활동이 없는 상황에서 나타나는 사치로 여겨질 수 있으며, 환경을 감상하고 이해할 기회를 제공한다."),
("In hazardous circumstances, the luxury of boredom is unavailable.","위험한 상황에서는 지루함이라는 사치를 누릴 수 없다."),
("Thus, it is paramount to utilize idle moments for profound self-reflection.","따라서 한가한 순간을 깊은 자기 성찰에 활용하는 것이 가장 중요하다."),
("It represents an occasion to listen, observe, and appreciate before expressing.","그것은 표현하기 전에 듣고, 관찰하고, 감상할 기회를 나타낸다."),
("Rather than viewing boredom as unproductive, it should be regarded as an opportunity for personal development and constructive contemplation.","지루함을 비생산적인 것으로 보기보다는 개인적 발달과 건설적인 사색의 기회로 여겨야 한다.")],
"* indulgence: 탐닉 ** paramount: 가장 중요한")
VOCAB=[["crucial","매우 중요한"],["give rise to","~을 일으키다"],["depression","우울(증)"],["despair","절망"],["irritation","짜증"],["adequately","적절히"],
 ["address","(문제를) 다루다"],["dependent on","~에 의존하는"],["arise","생겨나다"],["idle","한가한, 놀고 있는"],["imply","~을 암시하다"],["troubling","골치 아픈, 걱정스러운"],
 ["self-improvement","자기 계발"],["reflection","성찰, 반성"],["indulgence","탐닉"],["pastime","소일거리, 취미"],["perceive A as B","A를 B로 인식하다"],["luxury","사치"],
 ["manifest","나타나다"],["inactive","활동하지 않는"],["occasion","기회, 때"],["appreciate","~을 감상하다, 진가를 알다"],["comprehend","~을 이해하다"],["hazardous","위험한"],
 ["unavailable","이용할 수 없는"],["paramount","가장 중요한"],["utilize","~을 활용하다"],["profound","깊은"],["unproductive","비생산적인"],["constructive","건설적인"],["contemplation","사색, 숙고"]]
B=p.under([('(a)','dependent','dependent'),('(b)','troubling','troubling'),('(c)','providing','removing'),('(d)','unavailable','unavailable'),('(e)','constructive','constructive')])
EXAM=[EXQ(41,'41. 윗글의 제목으로 가장 적절한 것은?',B,["Boredom: An Opportunity in Disguise","The Irony of Choosing Danger Over Safety","Why Do We Pursue Safety and Comfort in Life?","What Harmful Effects Boredom Has on Our Minds","The Harder Our Life Is, the More Meaningful It Becomes"],0,
 "정답 ▶ ① 지루함: 변장한 기회\n이유: 지루함은 해로울 수 있지만, 안전할 때만 누리는 '사치'이고 자기 성찰과 개인적 발달의 '기회'로 봐야 한다는 글 → 겉보기와 달리 기회(in disguise)\n오답 ▶ ② 위험을 고르는 역설 이야기 아님 ③ 안전을 추구하는 이유가 주제 아님 ④ 해로운 영향은 도입부일 뿐 ⑤ 힘든 삶이 의미 있다는 글 아님\n포인트 ▶ in disguise 변장한, 겉보기와 다른",v=False),
 EXQ(42,'42. 밑줄 친 (a)~(e) 중에서 문맥상 낱말의 쓰임이 적절하지 <u>않은</u> 것은?',B,["(a) dependent","(b) troubling","(c) removing","(d) unavailable","(e) constructive"],2,
 "정답 ▶ ③ (c) removing → providing\n이유: 지루함은 안전하고 활동 없는 상황에서 나타나는 사치로, 환경을 감상하고 이해할 기회를 '제공해요(providing)'. 기회를 '없앤다(removing)'면 뒤의 '한가한 순간을 깊은 성찰에 활용하라'와 맞지 않아요.\n오답 ▶ (a) 재미있는 활동에 '의존하게' 됨 ✔ (b) '골치 아픈' 생각과 행동 ✔ (d) 위험한 상황에서는 지루함을 누릴 수 '없음' ✔ (e) '건설적인' 사색 ✔\n포인트 ▶ 어휘 문제는 그 낱말을 반대말로 바꿔 넣어 보고 흐름을 확인",v=False),
 EXQ(41,'다음 글의 요지로 가장 적절한 것은?',p.full(),["지루한 시간을 자기 성찰과 성장의 기회로 활용해야 한다.","지루함은 위험한 상황에서 더 자주 나타난다.","행복해지려면 재미있는 활동을 끊임없이 찾아야 한다.","한가한 시간을 줄이고 일을 더 많이 해야 한다.","지루함은 우울의 직접적인 원인이므로 무조건 피해야 한다."],0,
 "정답 ▶ ① 지루한 시간을 자기 성찰과 성장의 기회로 활용해야 한다.\n이유: it is paramount to utilize idle moments for profound self-reflection / it should be regarded as an opportunity for personal development\n오답 ▶ ② 위험한 곳에는 지루함이 없음 ③ 그러면 활동에 의존하게 됨 ④ 일을 더 하라는 글 아님 ⑤ 잘 다루면 기회\n포인트 ▶ should, paramount가 있는 문장 = 필자의 주장")]
PICK1=[PK(p,'It is crucial','harmful','helpful',"정답 ▶ harmful (해로운)\n오답 ▶ helpful (도움이 되는)\n이유: such as depression, despair, irritation(우울, 절망, 짜증) → 해로운 감정"),
 PK(p,'When we believe','dependent','independent',"정답 ▶ dependent (의존하는)\n오답 ▶ independent (독립적인)\n이유: 재미있는 활동만이 행복의 길이라 믿으면 그 활동에 '의존'하게 되고 부정적 감정이 생겨요."),
 PK(p,'The balance','positive reflection','negative reflection',"정답 ▶ positive (긍정적인)\n오답 ▶ negative (부정적인)\n이유: self-improvement(자기 계발)와 나란히 → 긍정적인 성찰"),
 PK(p,'Boredom doesn','danger','safety',"정답 ▶ danger (위험)\n오답 ▶ safety (안전)\n이유: 지루함은 안전한 영역(a safe zone)에서만 누리는 것 → 위험이 있으면 존재하지 않음"),
 PK(p,'In hazardous','hazardous','harmless',"정답 ▶ hazardous (위험한)\n오답 ▶ harmless (해 없는)\n이유: 지루함이라는 사치를 '누릴 수 없는' 상황 → 위험한 상황"),
 PK(p,'Rather than viewing','unproductive','productive',"정답 ▶ unproductive (비생산적인)\n오답 ▶ productive (생산적인)\n이유: Rather than(~보다는)으로 '발달의 기회'와 대조 → 비생산적이라고 보는 대신")]
TF=[TF(p,"Boredom, if not handled properly, can lead to feelings like depression.",True,"boredom can give rise to harmful emotions such as depression","정답 ▶ T\n어휘 ▶ handle = address · properly = adequately · lead to = give rise to"),
 TF(p,"Relying on fun activities for happiness can cause negative emotions.",True,"we become dependent on those activities, and negative thoughts and emotions arise","정답 ▶ T\n어휘 ▶ rely on = be dependent on"),
 TF(p,"The writer thinks idle time should be seen as wasted time.",False,"to not see it as idle time, wasted time, or boredom","정답 ▶ F\n이유: 낭비된 시간으로 '보지 말고' 자기 계발의 시간으로 보라고 해요."),
 TF(p,"People often feel bored even in dangerous situations.",False,"Boredom doesn't exist in the presence of danger","정답 ▶ F\n이유: 위험이 있는 곳에는 지루함이 존재하지 않아요."),
 TF(p,"Boredom usually appears in safe and inactive situations.",True,"typically manifests in safe and inactive situations","정답 ▶ T\n어휘 ▶ appear = manifest · usually = typically"),
 TF(p,"The writer suggests using idle moments for deep self-reflection.",True,"utilize idle moments for profound self-reflection","정답 ▶ T\n어휘 ▶ use = utilize · deep = profound")]
MC=[MC(p,"글의 내용과 일치하지 <u>않는</u> 것은?",["Boredom is a common experience in hazardous situations.","Unaddressed boredom can bring about despair and irritation.","Relying only on fun activities for happiness can backfire.","Boredom can be regarded as a kind of luxury.","Boredom offers a chance to listen and observe before speaking."],
 "정답 ▶ Boredom is a common experience in hazardous situations.\n이유: In hazardous circumstances, the luxury of boredom is unavailable. 위험한 상황에서는 지루함을 누릴 수 없어요.\n오답 ▶ 나머지는 모두 본문을 다른 어휘로 바꿔 쓴 일치 문장\n포인트 ▶ unaddressed = not adequately addressed · bring about = give rise to · backfire 역효과를 내다 · be regarded as = be perceived as · speak ≒ express",
 [["지루함은 위험한 상황에서 흔한 경험이다.","the luxury of boredom is unavailable","✗ 누릴 수 없음"],["다루어지지 않은 지루함은 절망과 짜증을 일으킬 수 있다.","can give rise to harmful emotions such as depression, despair, and irritation","bring about = give rise to"],["행복을 재미있는 활동에만 의존하면 역효과가 날 수 있다.","we become dependent on those activities, and negative thoughts and emotions arise","backfire 역효과"],["지루함은 일종의 사치로 여겨질 수 있다.","Boredom can be perceived as a luxury","regarded = perceived"],["지루함은 말하기 전에 듣고 관찰할 기회를 준다.","an occasion to listen, observe, and appreciate before expressing","chance = occasion · speaking ≒ expressing"]]),
 MC(p,"글의 내용과 <u>일치하는</u> 것은?",["지루함은 개인적 발달과 건설적인 사색의 기회로 여겨져야 한다.","지루함은 위험한 상황에서 더 강하게 느껴진다.","필자는 행복해지는 유일한 방법이 재미있는 활동을 찾는 것이라고 본다.","필자는 한가한 시간을 낭비된 시간으로 본다.","지루함은 환경을 이해할 기회를 빼앗는다."],
 "정답 ▶ 지루함은 개인적 발달과 건설적인 사색의 기회로 여겨져야 한다.\n이유: it should be regarded as an opportunity for personal development and constructive contemplation\n오답 ▶ ② 위험한 곳엔 존재하지 않음 ③ 그렇게 믿으면 활동에 의존하게 된다고 비판 ④ 낭비된 시간으로 보지 말라 ⑤ 기회를 '제공'함(providing)\n포인트 ▶ 42번 정답 (c)와 연결: providing an occasion",
 [["","an opportunity for personal development and constructive contemplation","일치 ✔"],["","Boredom doesn't exist in the presence of danger","위험한 곳엔 없음"],["","we become dependent on those activities","비판"],["","to not see it as idle time, wasted time","낭비로 보지 않음"],["","providing an occasion to appreciate and comprehend the environment","기회 제공"]])]
PICK2=[PK(p,'It is crucial','to recognize','recognizing',"정답 ▶ to recognize\n이유: 가주어 It - 진주어 to부정사"),
 PK(p,'It is crucial','addressed','addressing',"정답 ▶ addressed\n이유: if (it is) not adequately addressed — 지루함이 '다루어지는' 수동 → 과거분사"),
 PK(p,'When we believe','searching','search',"정답 ▶ searching\n이유: 전치사 by + 동명사"),
 PK(p,'Boredom can be','be perceived','perceive',"정답 ▶ be perceived\n이유: 지루함이 '인식되는' 수동 → can be p.p. (perceive A as B → A is perceived as B)"),
 PK(p,'Boredom can be','manifests','manifest',"정답 ▶ manifests\n이유: 주격 관계대명사 that의 선행사 a luxury(단수)"),
 PK(p,'Rather than viewing','be regarded','regard',"정답 ▶ be regarded\n이유: 지루함이 '여겨지는' 수동 → should be p.p.")]
VERB=[VB(p,'When we believe','arise','arise',"정답 ▶ arise\n이유: 주어 negative thoughts and emotions(복수), 현재시제"),
 VB(p,'It is suggested','implies','imply',"정답 ▶ implies\n이유: 주어는 인용된 속담(하나의 말) → 단수 implies"),
 VB(p,'Boredom can be','providing','provide',"정답 ▶ providing\n이유: 콤마 뒤 분사구문, 지루함이 기회를 '제공하는' 능동 → 현재분사"),
 VB(p,'It represents','represents','represent',"정답 ▶ represents\n이유: 주어 It(단수), 현재시제")]
ERR=[ER(p,'When we believe',[('searching','search'),'dependent','arise'],0,'searching',"틀린 곳 ▶ ① search → searching\n이유: 전치사 by + 동명사\n나머지 ▶ ② become dependent on ✔ ③ 자동사 arise ✔"),
 ER(p,'Boredom can be',[('be perceived','perceive'),'manifests','providing'],0,'be perceived',"틀린 곳 ▶ ① perceive → be perceived\n이유: 지루함이 '인식되는' 수동\n나머지 ▶ ② 선행사 a luxury(단수) ✔ ③ 분사구문 능동 ✔"),
 ER(p,'Rather than viewing',['viewing','unproductive',('be regarded','regard')],2,'be regarded',"틀린 곳 ▶ ③ regard → be regarded\n이유: 주어 it(= boredom)이 '여겨지는' 수동\n나머지 ▶ ① Rather than + 동명사 ✔ ② view A as B의 형용사 보어 ✔")]
SCR=[4,5,7,8,9,10]
ORDER=[[0,1,2,3],[5,6,7,8]]
INSERT=[([4,5,6,7],3,"정답 ▶ ③\n이유: In hazardous circumstances(위험한 상황에서는)는 앞 문장의 safe and inactive situations(안전하고 활동 없는 상황)와 대조돼요. 맨 끝 자리!"),
 ([7,8,9,10],1,"정답 ▶ ①\n이유: Thus(따라서)는 '위험할 땐 지루함을 누릴 수 없다 → 그러니 한가한 순간이 소중하다'로 이어져요. 다음 문장의 It도 이 문장(한가한 순간의 활용)을 받아요.")]
ODD=[([0,1,"Many modern video games are designed to be as entertaining as possible.",2],2,"정답 ▶ ③\n이유: 지루함을 잘못 다루면 생기는 해로운 감정 이야기예요. 비디오 게임 설계 이야기는 관계없어요.")]
BLANK=[BL(p,'It is crucial','addressed',["enjoyed","praised","shared"],"정답 ▶ addressed (다루어진)\n이유: 지루함을 '제대로 다루지 않으면' 해로운 감정이 생겨요.\n오답 ▶ enjoyed 즐긴 · praised 칭찬받은 · shared 공유된"),
 BL(p,'Boredom doesn','safe',["war","danger","busy"],"정답 ▶ safe (안전한)\n이유: 위험이 있는 곳에는 지루함이 없다 → 지루함은 '안전한' 곳에서만 누림\n오답 ▶ war 전쟁 · danger 위험 · busy 바쁜"),
 BL(p,'Thus, it is paramount','self-reflection',["entertainment","competition","shopping"],"정답 ▶ self-reflection (자기 성찰)\n이유: 앞에서 지루한 시간을 '자기 계발, 긍정적 성찰의 시간'으로 보라고 했어요.\n오답 ▶ entertainment 오락 · competition 경쟁 · shopping 쇼핑")]
GRAM=[{'q':"빈칸에 알맞은 것은?<br><b>It is crucial ______ that boredom can be harmful.</b>",'opts':["to recognize","recognize","recognized","recognizes"],'ex':"정답 ▶ to recognize\n이유: 가주어 It - 진주어 to부정사"},
 {'q':"빈칸에 알맞은 것은?<br><b>Boredom can be harmful if not adequately ______.</b>",'opts':["addressed","addressing","address","to address"],'ex':"정답 ▶ addressed\n이유: if (it is) not addressed — 접속사 뒤 '주어 + be동사' 생략, 수동 → 과거분사"},
 {'q':"빈칸에 알맞은 것은?<br><b>Reflecting, just how lucky ______ to be bored?</b>",'opts':["are we","we are","do we","we do"],'ex':"정답 ▶ are we\n이유: 물음표로 끝나는 의문문 → how + 형용사 + be동사 + 주어"},
 {'q':"빈칸에 알맞은 것은?<br><b>Boredom should ______ as an opportunity.</b>",'opts':["be regarded","regard","regarding","been regarded"],'ex':"정답 ▶ be regarded\n이유: 조동사 + be + p.p. (regard A as B → A is regarded as B)"}]
