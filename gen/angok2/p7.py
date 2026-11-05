from fw import *
p=P(24,'고3 6월 24번 · 제목',[
("Food, as we all know, is essential for human life.","우리 모두 알듯이, 음식은 인간의 삶에 필수적이다."),
("It also is the basis for several major industries found in many countries around the world such as in agriculture, food processing, food retailing and food service.","음식은 또한 농업, 식품 가공, 식품 소매, 외식업처럼 전 세계 많은 나라에서 볼 수 있는 몇몇 주요 산업의 기반이기도 하다."),
("For millennia, the focus of those involved with food as a human and economic phenomenon was on its production, preservation, distribution, pricing and other practical concerns.","수천 년 동안, 인간적·경제적 현상으로서의 음식에 관여한 사람들의 초점은 음식의 생산, 보존, 유통, 가격 책정 및 기타 실용적인 관심사에 있었다."),
("But in the late 18th century this began to change.","그러나 18세기 후반에 이것이 바뀌기 시작했다."),
("Food became more than just a life necessity.","음식은 단순한 생활 필수품 이상이 되었다."),
("Restaurants began to be developed, initially in France but eventually in other nations, as a distinct institution offering people dining choices and table service, the opportunity for socialization and, over time, a finer and finer atmosphere.","식당은 처음에는 프랑스에서, 결국에는 다른 나라들에서도, 사람들에게 식사 선택권과 테이블 서비스, 사교의 기회, 그리고 시간이 지나면서 점점 더 고급스러운 분위기를 제공하는 독특한 기관으로 발전하기 시작했다."),
("The rise of restaurants eventually led to a class of diners who prided themselves on being critics of taste, food and cooking.","식당의 등장은 결국 맛, 음식, 요리의 비평가인 것을 자랑으로 여기는 식객 계층을 낳았다."),
("Brillat-Savarin is probably the best known of the 'culinary philosophers' or, in today's parlance, a 'foodie'.","브리야사바랭은 아마도 '요리 철학자', 오늘날의 말로 하면 '미식가' 중 가장 잘 알려진 인물일 것이다."),
("One of Brillat-Savarin's better known sayings was, '[t]ell me what you eat, and I'll tell you who you are.'","브리야사바랭의 잘 알려진 말 중 하나는 '당신이 무엇을 먹는지 말해 주면, 당신이 어떤 사람인지 말해 주겠다'였다.")],
"* culinary: 요리의 ** parlance: 용어")
VOCAB=[["essential","필수적인"],["basis","기반, 토대"],["agriculture","농업"],["processing","가공"],["retailing","소매(업)"],["millennia","수천 년 (millennium의 복수)"],
 ["involved with","~에 관여한"],["phenomenon","현상"],["preservation","보존"],["distribution","유통, 분배"],["practical","실용적인"],["concern","관심사"],
 ["necessity","필수품"],["initially","처음에는"],["distinct","독특한, 별개의"],["institution","기관, 제도"],["dining","식사"],["socialization","사교, 사회화"],
 ["atmosphere","분위기"],["rise","등장, 증가"],["lead to","~로 이어지다","led to"],["diner","식사하는 사람, 식객"],["pride oneself on","~을 자랑으로 여기다","prided themselves on"],
 ["critic","비평가"],["culinary","요리의"],["parlance","용어, 말투"],["foodie","미식가"]]
EXAM=[EXQ(24,'24. 다음 글의 제목으로 가장 적절한 것은?',p.full(),["Changing Appetites: The Return of Fine Dining","Beyond Mere Necessity: The Rise of Food Culture","Tips for Choosing Restaurants for Social Occasions","Why Table Manners Matter: Food and Class Identity","How Industrialization Is Taking Over Food Production"],1,
 "정답 ▶ ② 단순한 필수품을 넘어: 음식 문화의 부상\n이유: 수천 년간 음식은 생산·보존·유통 같은 실용적 관심사였지만, 18세기 후반부터 '생활 필수품 이상'이 되어 식당, 미식 비평가, 미식가가 등장했다는 글\n오답 ▶ ① 고급 식사가 '돌아왔다'는 게 아니라 새로 생겨남 ③ 식당 고르는 팁 아님 ④ 식사 예절 이야기 아님 ⑤ 산업화가 아니라 문화\n포인트 ▶ more than just a life necessity = Beyond Mere Necessity",v=False),
 EXQ(24,'다음 글의 요지로 가장 적절한 것은?',p.full(),["18세기 후반 이후 음식은 생존 수단을 넘어 문화적 의미를 지니게 되었다.","음식 산업은 농업보다 외식업에서 더 크게 성장했다.","프랑스 식당은 다른 나라 식당보다 항상 더 고급스러웠다.","음식의 보존과 유통은 오늘날에도 가장 중요한 관심사이다.","미식가는 요리 실력이 뛰어난 요리사를 뜻한다."],0,
 "정답 ▶ ① 18세기 후반 이후 음식은 생존 수단을 넘어 문화적 의미를 지니게 되었다.\n이유: But in the late 18th century this began to change. Food became more than just a life necessity. → 식당, 비평가, 미식가의 등장\n오답 ▶ ② 산업 비교 없음 ③ 프랑스에서 '처음' 발전했을 뿐 ④ 그건 18세기 이전의 초점 ⑤ 미식가는 맛을 비평하는 식객\n포인트 ▶ But 뒤가 글의 중심"),
 EXQ(24,'글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳은?',p.insert_q(3,[1,2,4,5,6]),SLOT,2,
 "정답 ▶ ③\n이유: 주어진 문장의 But과 this는 '수천 년간 음식의 초점은 실용적 관심사였다'는 앞 문장을 받아 뒤집어요. 그 뒤에 '음식은 필수품 이상이 되었다'가 와야 자연스러워요.\n오답 ▶ ① ② 아직 '이전의 초점'이 나오기 전 ④ ⑤ 이미 변화가 설명된 뒤\n포인트 ▶ 과거(For millennia) → But(전환) → 변화 내용")]
PICK1=[PK(p,'Food, as we','essential','optional',"정답 ▶ essential (필수적인)\n오답 ▶ optional (선택적인)\n이유: as we all know(우리 모두 알듯이) → 음식은 삶에 '필수'"),
 PK(p,'For millennia','practical','artistic',"정답 ▶ practical (실용적인)\n오답 ▶ artistic (예술적인)\n이유: 생산, 보존, 유통, 가격 → 모두 실용적인 문제. 18세기 후반 이후의 '문화'와 대조"),
 PK(p,'Food became','necessity','luxury',"정답 ▶ necessity (필수품)\n오답 ▶ luxury (사치품)\n이유: more than just(~ 이상) → 음식이 '단순한 필수품'을 넘어섬"),
 PK(p,'Restaurants began','eventually in','previously in',"정답 ▶ eventually (결국)\n오답 ▶ previously (이전에)\n이유: initially(처음에는) France → eventually(결국) 다른 나라들. 시간 순서"),
 PK(p,'Restaurants began','socialization','isolation',"정답 ▶ socialization (사교)\n오답 ▶ isolation (고립)\n이유: 식당이 '제공한' 좋은 것들(식사 선택권, 테이블 서비스, 고급 분위기)과 나란히 → 사교의 기회"),
 PK(p,'The rise of restaurants','critics','victims',"정답 ▶ critics (비평가)\n오답 ▶ victims (피해자)\n이유: '자랑으로 여겼다(prided themselves)' → 맛과 요리를 평가하는 비평가. 다음 문장 '요리 철학자', '미식가'와 연결")]
TF=[TF(p,"Food is the basis of industries such as agriculture and food service.",True,"the basis for several major industries","정답 ▶ T\n이유: 농업, 식품 가공, 소매, 외식업 같은 주요 산업의 기반이에요."),
 TF(p,"For thousands of years, people focused mainly on the artistic side of food.",False,"pricing and other practical concerns","정답 ▶ F\n이유: 생산, 보존, 유통, 가격 같은 '실용적인' 관심사에 초점이 있었어요.\n어휘 ▶ thousands of years = millennia"),
 TF(p,"A change in how people saw food began in the late 18th century.",True,"But in the late 18th century this began to change","정답 ▶ T"),
 TF(p,"Restaurants first developed in Italy.",False,"initially in France","정답 ▶ F\n이유: 처음에는 프랑스에서 발전했어요.\n어휘 ▶ first = initially"),
 TF(p,"Restaurants offered people chances to socialize.",True,"the opportunity for socialization","정답 ▶ T\n어휘 ▶ chance = opportunity · socialize 사교하다"),
 TF(p,"Brillat-Savarin is known as one of the earliest restaurant owners.",False,"the best known of the 'culinary philosophers'","정답 ▶ F\n이유: 가장 잘 알려진 '요리 철학자', 즉 미식가예요. 식당 주인이라는 말은 없어요.")]
MC=[MC(p,"글의 내용과 일치하지 <u>않는</u> 것은?",["Restaurants became less refined as time passed.","Food supports several major industries around the world.","For a long time, those involved with food cared mostly about practical matters.","Food came to mean more than simply something needed for survival.","A group of diners emerged who were proud of judging food."],
 "정답 ▶ Restaurants became less refined as time passed.\n이유: over time, a finer and finer atmosphere. 시간이 지나며 점점 더 고급스러워졌어요.\n오답 ▶ 나머지는 모두 본문을 다른 어휘로 바꿔 쓴 일치 문장\n포인트 ▶ refined 세련된 ≒ fine · support ≒ be the basis for · matters = concerns · something needed for survival = a life necessity · emerge 생겨나다 · judge ≒ be critics of",
 [["식당은 시간이 지나며 덜 세련되어졌다.","a finer and finer atmosphere","✗ 점점 더 고급"],["음식은 전 세계 몇몇 주요 산업을 떠받친다.","the basis for several major industries","support ≒ be the basis for"],["오랫동안 음식 관계자들은 주로 실용적인 문제에 관심을 가졌다.","pricing and other practical concerns","matters = concerns"],["음식은 단순히 생존에 필요한 것 이상을 의미하게 되었다.","Food became more than just a life necessity","something needed for survival = a life necessity"],["음식을 평가하는 것을 자랑스러워하는 식객 집단이 생겨났다.","prided themselves on being critics","proud of = prided themselves on"]]),
 MC(p,"글의 내용과 <u>일치하는</u> 것은?",["식당은 사람들에게 식사 선택권과 사교의 기회를 제공했다.","음식은 18세기 초부터 생활 필수품 이상의 의미를 갖기 시작했다.","식당은 프랑스에서만 발전했다.","브리야사바랭은 오늘날의 말로 '요리사'라고 불린다.","수천 년 동안 음식의 맛이 가장 중요한 관심사였다."],
 "정답 ▶ 식당은 사람들에게 식사 선택권과 사교의 기회를 제공했다.\n이유: offering people dining choices and table service, the opportunity for socialization\n오답 ▶ ② the late 18th century(18세기 후반) ③ eventually in other nations ④ a 'foodie'(미식가) ⑤ practical concerns(실용적 관심사)\n포인트 ▶ late 18th century = 18세기 후반",
 [["","the opportunity for socialization","일치 ✔"],["","in the late 18th century","18세기 후반"],["","eventually in other nations","다른 나라에서도"],["","a 'foodie'","미식가"],["","other practical concerns","실용적 관심사"]])]
PICK2=[PK(p,'It also is','found in','finding in',"정답 ▶ found\n이유: 산업이 '발견되는' 수동 → 과거분사가 industries를 뒤에서 수식"),
 PK(p,'For millennia','involved','involving',"정답 ▶ involved\n이유: those (who are) involved with ~ — ~에 관여한 사람들 (be involved with)"),
 PK(p,'For millennia','was on','were on',"정답 ▶ was\n이유: 주어는 the focus(단수). of those ~ phenomenon은 수식어"),
 PK(p,'Restaurants began','offering','offered',"정답 ▶ offering\n이유: 기관이 사람들에게 '제공하는' 능동 → 현재분사가 institution 수식"),
 PK(p,'The rise of restaurants','themselves','them',"정답 ▶ themselves\n이유: 주어(who = diners)와 목적어가 같은 대상 → 재귀대명사 (pride oneself on)"),
 PK(p,'One of Brillat','was,','were,',"정답 ▶ was\n이유: One of + 복수명사 → 주어는 One(단수)")]
VERB=[VB(p,'Restaurants began','developed','develop',"정답 ▶ developed\n이유: began to be + p.p. — 식당이 '발전되기' 시작했다(수동)"),
 VB(p,'The rise of restaurants','led','lead',"정답 ▶ led\n이유: 과거의 일 → 과거형 (lead - led - led)"),
 VB(p,'The rise of restaurants','prided','pride',"정답 ▶ prided\n이유: 과거의 식객 계층 → 과거형 (pride oneself on)"),
 VB(p,'Brillat-Savarin is','known','know',"정답 ▶ known\n이유: the best known 가장 잘 알려진 (과거분사)")]
ERR=[ER(p,'For millennia',[('involved','involving'),'phenomenon','practical'],0,'involved',"틀린 곳 ▶ ① involving → involved\n이유: those (who are) involved with ~에 관여한 사람들\n나머지 ▶ ② 단수 명사 phenomenon(복수 phenomena) ✔ ③ 형용사 ✔"),
 ER(p,'Restaurants began',[('to be developed','to be developing'),'offering','finer and finer'],0,'to be developed',"틀린 곳 ▶ ① to be developing → to be developed\n이유: 식당이 '발전되는' 수동 → to be p.p.\n나머지 ▶ ② 제공하는(능동) ✔ ③ 비교급 and 비교급(점점 더) ✔"),
 ER(p,'The rise of restaurants',['eventually',('themselves','them'),'being'],1,'themselves',"틀린 곳 ▶ ② them → themselves\n이유: pride oneself on — 주어와 같은 대상이라 재귀대명사\n나머지 ▶ ① 부사 ✔ ③ 전치사 on + 동명사 ✔")]
SCR=[0,3,4,6,7]
ORDER=[[0,1,2,3],[3,4,5,6]]
INSERT=[([4,5,6,7],2,"정답 ▶ ②\n이유: The rise of restaurants(식당의 등장)는 앞 문장의 '식당이 발전하기 시작했다'를 받아요. 그리고 다음 문장의 '요리 철학자'가 주어진 문장의 '비평가 식객'을 이어받아요."),
 ([5,6,7,8],3,"정답 ▶ ③\n이유: One of Brillat-Savarin's ~ sayings는 앞 문장에서 처음 소개된 브리야사바랭의 말을 이어서 소개해요. 맨 끝 자리!")]
ODD=[([4,5,"Many restaurants today use smartphone apps to take orders and payments.",6],2,"정답 ▶ ③\n이유: 18세기 후반 식당의 등장과 음식 문화의 발달을 설명하는 흐름이에요. 오늘날 주문 앱 이야기는 관계없어요.")]
BLANK=[BL(p,'Food became','necessity',["threat","mystery","burden"],"정답 ▶ necessity (필수품)\n이유: 앞에서 음식은 삶에 필수(essential)라고 했고, 이제 '단순한 필수품 이상'이 되었다는 흐름\n오답 ▶ threat 위협 · mystery 수수께끼 · burden 부담"),
 BL(p,'The rise of restaurants','critics',["farmers","sellers","producers"],"정답 ▶ critics (비평가)\n이유: 맛, 음식, 요리를 '평가'하는 걸 자랑으로 여긴 식객들. 다음 문장의 '요리 철학자', '미식가'와 연결\n오답 ▶ farmers 농부 · sellers 판매자 · producers 생산자"),
 BL(p,'Brillat-Savarin is',"'foodie'",["'waiter'","'farmer'","'chef'"],"정답 ▶ 'foodie' (미식가)\n이유: '요리 철학자'를 오늘날의 말(in today's parlance)로 바꾼 것 → 음식을 즐기고 평가하는 사람\n오답 ▶ waiter 종업원 · farmer 농부 · chef 요리사")]
GRAM=[{'q':"빈칸에 알맞은 것은?<br><b>several major industries ______ in many countries</b>",'opts':["found","finding","find","to find"],'ex':"정답 ▶ found\n이유: 산업이 '발견되는' 수동 → 과거분사 후치 수식"},
 {'q':"빈칸에 알맞은 것은?<br><b>the focus of those ______ with food</b>",'opts':["involved","involving","involve","to involve"],'ex':"정답 ▶ involved\n이유: those (who are) involved with ~에 관여한 사람들"},
 {'q':"빈칸에 알맞은 것은?<br><b>They prided themselves on ______ critics of taste.</b>",'opts':["being","be","been","to be"],'ex':"정답 ▶ being\n이유: pride oneself on + 동명사 (on은 전치사)"},
 {'q':"빈칸에 알맞은 것은?<br><b>Over time, the atmosphere became ______.</b>",'opts':["finer and finer","fine and fine","finest and finest","more fine and fine"],'ex':"정답 ▶ finer and finer\n이유: 비교급 and 비교급 = 점점 더 ~한"}]
