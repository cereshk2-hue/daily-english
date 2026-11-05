from fw import *
p=P(24,'10월 24번 · 제목',[
("Consistent though he may be, some of Aristotle's ideas meet us today as strange.","그가 일관성은 있을지 몰라도, 아리스토텔레스의 생각 중 일부는 오늘날 우리에게 이상하게 다가온다."),
("He had no difficulty justifying slavery, for example, and in his era, philosophers enjoyed positions of high privilege and influence.","예를 들어 그는 노예 제도를 정당화하는 데 아무런 어려움이 없었고, 그의 시대에 철학자들은 높은 특권과 영향력을 지닌 지위를 누렸다."),
("Because of their practice of contemplation for the highest human good, philosophers were considered worthy to have all the best things in life.","인간의 최고선을 위해 사유를 실천한다는 이유로, 철학자들은 삶의 모든 좋은 것을 누릴 자격이 있다고 여겨졌다."),
("Somehow that assertion seems oddly self-serving.","어쩐지 그 주장은 묘하게 자기 잇속만 차리는 것처럼 보인다."),
("It serves us to remember that every great thinker is of her own time and speaks to a particular audience, and certainly Aristotle is no exception.","모든 위대한 사상가는 자기 시대에 속해 있고 특정한 청중에게 말한다는 것을 기억하는 것이 우리에게 도움이 되며, 분명 아리스토텔레스도 예외가 아니다."),
("Human flourishing as he understood it probably would not be nearly as inclusive as we would want it to be today.","그가 이해한 인간의 번영은 아마 오늘날 우리가 원하는 만큼 포용적인 것과는 거리가 멀 것이다."),
("How he understood right and good is best taken to be an indicator of how the privileged elite of ancient Greek society tended to understand right and good.","그가 옳음과 선을 어떻게 이해했는지는 고대 그리스 사회의 특권층 엘리트가 옳음과 선을 어떻게 이해하는 경향이 있었는지 보여 주는 지표로 받아들이는 것이 가장 좋다."),
("As a result, for all it does well, it is also deeply flawed.","그 결과, 그것이 잘하는 모든 점에도 불구하고, 그것은 또한 깊은 결함을 지니고 있다.")],
"* contemplation: 사유")
VOCAB=[["consistent","일관된"],["justify","~을 정당화하다"],["slavery","노예 제도"],["era","시대"],["privilege","특권"],["influence","영향력"],
 ["contemplation","사유, 숙고"],["worthy","~할 자격이 있는, 가치 있는"],["assertion","주장"],["oddly","묘하게, 이상하게"],["self-serving","자기 잇속만 차리는"],
 ["serve","~에게 도움이 되다","It serves us"],["of one's own time","자기 시대에 속하는","of her own time"],["exception","예외"],["flourishing","번영, 번성"],
 ["inclusive","포용적인, 포괄적인"],["indicator","지표"],["privileged","특권을 가진"],["elite","엘리트, 상류층"],["for all","~에도 불구하고","for all it does well"],["flawed","결함이 있는"]]
EXAM=[EXQ(24,'24. 다음 글의 제목으로 가장 적절한 것은?',p.full(),[
 "Aristotle's Ethics Trapped in His Time and Class","Aristotle's Highest Good for the Underprivileged","Why Philosophers Deserve the Best Things in Life","Aristotle's Lonely Struggle to Build an Inclusive Society","Limits of Greek Philosophers: Thoughts Without Actions"],0,
 "정답 ▶ ① 그의 시대와 계층에 갇힌 아리스토텔레스의 윤리학\n이유: 위대한 사상가도 자기 시대에 속하고(of her own time), 아리스토텔레스의 옳음과 선은 고대 그리스 '특권층 엘리트'의 이해를 보여 주는 지표 → 시대(Time)와 계층(Class)에 갇혀 있어 결함이 있다\n오답 ▶ ② 소외 계층(underprivileged)이 아니라 특권층의 시각 ③ 그 주장은 자기 잇속만 차리는 듯하다고 비판 ④ 포용적인 사회를 만들려 한 게 아니라 포용적이지 않음 ⑤ 행동 없는 생각이 문제라는 글이 아님\n포인트 ▶ trapped in ~에 갇힌",v=False),
 EXQ(24,'다음 글의 요지로 가장 적절한 것은?',p.full(),[
 "아리스토텔레스의 윤리관은 당대 특권층의 시각을 반영하므로 한계가 있다.","아리스토텔레스는 모든 사람이 평등하게 번영해야 한다고 주장했다.","철학자는 사회에서 높은 특권을 누릴 자격이 있다.","위대한 사상가의 생각은 시대를 넘어 그대로 적용된다.","고대 그리스 사회는 오늘날보다 더 포용적이었다."],0,
 "정답 ▶ ① 아리스토텔레스의 윤리관은 당대 특권층의 시각을 반영하므로 한계가 있다.\n이유: 옳음과 선에 대한 그의 이해 = 특권층 엘리트의 이해를 보여 주는 지표 → As a result, ~ deeply flawed\n오답 ▶ ② 노예제를 정당화했고 포용적이지 않음 ③ 필자는 그 주장을 비판 ④ 모든 사상가는 자기 시대에 속함 ⑤ 오늘날만큼 포용적이지 않음\n포인트 ▶ 요지는 As a result 같은 결론 신호 뒤에"),
 EXQ(24,'다음 빈칸에 들어갈 말로 가장 적절한 것은?',p.blank('of her own time'),[
 "of her own time","ahead of every era","free from social influence","a voice for all humanity","beyond any criticism"],0,
 "정답 ▶ ① 자기 시대에 속하는\n이유: 빈칸 뒤 '특정한 청중에게 말한다', '아리스토텔레스도 예외가 아니다', 그리고 그의 생각이 고대 그리스 특권층의 시각을 보여 준다는 흐름 → 사상가는 '자기 시대'의 산물\n오답 ▶ ② 모든 시대를 앞서는 ③ 사회의 영향에서 자유로운 ④ 모든 인류의 목소리 ⑤ 어떤 비판도 넘어서는 → 모두 반대\n포인트 ▶ be of + 명사 = ~에 속하다, ~의 성질을 지니다")]
PICK1=[PK(p,'He had no difficulty','justifying','criticizing',"정답 ▶ justifying (정당화하는)\n오답 ▶ criticizing (비판하는)\n이유: 오늘날 이상하게 보이는 생각의 예 → 노예제를 '정당화'했어요."),
 PK(p,'He had no difficulty','privilege','poverty',"정답 ▶ privilege (특권)\n오답 ▶ poverty (가난)\n이유: and influence(영향력)와 나란히 → 높은 특권. 다음 문장의 '모든 좋은 것을 누릴 자격'과도 연결"),
 PK(p,'Somehow','self-serving','selfless',"정답 ▶ self-serving (자기 잇속만 차리는)\n오답 ▶ selfless (이타적인)\n이유: 철학자들 스스로 '철학자는 좋은 것을 다 누릴 자격이 있다'고 한 셈 → 자기에게 유리한 주장"),
 PK(p,'It serves us','exception','example',"정답 ▶ exception (예외)\n이유: 모든 위대한 사상가가 자기 시대에 속하고, 아리스토텔레스도 '예외가 아니다'\n포인트 ▶ be no exception 예외가 아니다"),
 PK(p,'Human flourishing','inclusive','exclusive',"정답 ▶ inclusive (포용적인)\n오답 ▶ exclusive (배타적인)\n이유: not nearly as ~ as we would want today → 오늘날 우리가 원하는 '포용성'에 못 미침. 노예제를 정당화했으니까요."),
 PK(p,'As a result','flawed','flawless',"정답 ▶ flawed (결함이 있는)\n오답 ▶ flawless (흠 없는)\n이유: for all it does well(잘하는 점에도 불구하고)과 대조 → 깊은 결함")]
TF=[TF(p,"Aristotle saw nothing wrong with slavery.",True,"He had no difficulty justifying slavery","정답 ▶ T\n이유: 노예 제도를 정당화하는 데 아무 어려움이 없었어요."),
 TF(p,"In Aristotle's time, philosophers had little social influence.",False,"philosophers enjoyed positions of high privilege and influence","정답 ▶ F\n이유: 높은 특권과 영향력을 누렸어요."),
 TF(p,"Philosophers were thought to deserve the best things in life because of their contemplation.",True,"philosophers were considered worthy to have all the best things in life","정답 ▶ T\n어휘 ▶ deserve = be worthy to have · be thought to = be considered"),
 TF(p,"The writer believes great thinkers speak equally to all people in all times.",False,"every great thinker is of her own time and speaks to a particular audience","정답 ▶ F\n이유: 위대한 사상가도 자기 시대에 속하고 '특정한' 청중에게 말해요."),
 TF(p,"Aristotle's idea of human flourishing was probably less inclusive than what we want today.",True,"would not be nearly as inclusive as we would want it to be today","정답 ▶ T\n이유: 오늘날 우리가 원하는 만큼 포용적이지 않았을 거예요."),
 TF(p,"The writer considers Aristotle's ethics completely flawless.",False,"it is also deeply flawed","정답 ▶ F\n이유: 잘하는 점도 있지만 깊은 결함이 있다고 했어요.")]
MC=[MC(p,"글의 내용과 일치하지 <u>않는</u> 것은?",[
 "The writer argues that Aristotle's ideas are entirely free from the biases of his era.","Aristotle found it easy to defend slavery.","The claim that philosophers deserved the best things seems to benefit philosophers themselves.","Like every great thinker, Aristotle belonged to his own time.","Aristotle's view shows how the elite of ancient Greece thought about right and good."],
 "정답 ▶ The writer argues that Aristotle's ideas are entirely free from the biases of his era.\n이유: 아리스토텔레스도 자기 시대에 속하고(no exception), 특권층의 시각을 보여 준다고 했어요.\n오답 ▶ 나머지는 모두 본문을 다른 어휘로 바꿔 쓴 일치 문장\n포인트 ▶ defend ≒ justify · benefit oneself ≒ self-serving · belong to one's time = be of one's own time · bias 편견",
 [["필자는 아리스토텔레스의 생각이 그 시대의 편견에서 완전히 자유롭다고 주장한다.","certainly Aristotle is no exception","✗ 예외가 아님"],["아리스토텔레스는 노예제를 옹호하는 것을 쉽게 여겼다.","He had no difficulty justifying slavery","defend ≒ justify"],["철학자가 좋은 것을 누릴 자격이 있다는 주장은 철학자 자신에게 이로운 것 같다.","seems oddly self-serving","self-serving 자기 잇속만 차리는"],["모든 위대한 사상가처럼 아리스토텔레스도 자기 시대에 속했다.","every great thinker is of her own time","belong to = be of"],["아리스토텔레스의 관점은 고대 그리스 엘리트가 옳음과 선을 어떻게 생각했는지 보여 준다.","an indicator of how the privileged elite of ancient Greek society","show ≒ be an indicator of"]]),
 MC(p,"글의 내용과 <u>일치하는</u> 것은?",["필자는 아리스토텔레스의 사상에 잘한 점이 있지만 깊은 결함도 있다고 본다.","아리스토텔레스는 노예 제도에 반대했다.","아리스토텔레스 시대의 철학자들은 낮은 지위에 머물렀다.","필자는 철학자가 최고의 것을 누려야 한다는 주장에 동의한다.","아리스토텔레스가 생각한 번영은 오늘날보다 더 포용적이었다."],
 "정답 ▶ 필자는 아리스토텔레스의 사상에 잘한 점이 있지만 깊은 결함도 있다고 본다.\n이유: for all it does well, it is also deeply flawed\n오답 ▶ ② justifying slavery 정당화 ③ high privilege and influence ④ oddly self-serving이라고 비판 ⑤ not nearly as inclusive\n포인트 ▶ for all = despite ~에도 불구하고",
 [["","for all it does well, it is also deeply flawed","일치 ✔"],["","justifying slavery","정당화"],["","positions of high privilege and influence","높은 지위"],["","seems oddly self-serving","비판"],["","would not be nearly as inclusive","덜 포용적"]])]
PICK2=[PK(p,'Consistent though','Consistent','Consistently',"정답 ▶ Consistent\n이유: 형용사 보어 + though + 주어 + 동사 = Though he may be consistent (양보의 도치). be동사의 보어라 형용사"),
 PK(p,'He had no difficulty','justifying','to justify',"정답 ▶ justifying\n이유: have (no) difficulty (in) -ing ~하는 데 어려움이 있다(없다)"),
 PK(p,'Because of their practice','to have','having',"정답 ▶ to have\n이유: be considered worthy to do ~할 자격이 있다고 여겨지다"),
 PK(p,'It serves us','to remember','remembering',"정답 ▶ to remember\n이유: 가주어 It - 진주어 to부정사(to remember that ~)"),
 PK(p,'Human flourishing','to be today','being today',"정답 ▶ to be\n이유: want + 목적어(it) + to부정사"),
 PK(p,'How he understood','is best','are best',"정답 ▶ is\n이유: 의문사절 주어(How he understood right and good)는 단수")]
VERB=[VB(p,'He had no difficulty','enjoyed','enjoy',"정답 ▶ enjoyed\n이유: in his era(과거) → 과거형"),
 VB(p,'Because of their practice','considered','consider',"정답 ▶ considered\n이유: were + p.p. 수동 (be considered ~하다고 여겨지다)"),
 VB(p,'How he understood','taken','take',"정답 ▶ taken\n이유: is best taken to be ~으로 받아들이는 것이 가장 좋다 (수동, take - took - taken)"),
 VB(p,'How he understood','tended','tend',"정답 ▶ tended\n이유: 고대 그리스(과거)의 경향 → 과거형")]
ERR=[ER(p,'He had no difficulty',[('justifying','to justify'),'era','enjoyed'],0,'justifying',"틀린 곳 ▶ ① to justify → justifying\n이유: have no difficulty -ing\n나머지 ▶ ② ③ ✔"),
 ER(p,'Somehow',['assertion',('seems','seem'),'oddly'],1,'seems',"틀린 곳 ▶ ② seem → seems\n이유: 주어 that assertion(단수)\n나머지 ▶ ① ③ 형용사 self-serving을 꾸미는 부사 oddly ✔"),
 ER(p,'How he understood',[('is','are'),'to be','tended'],0,'is',"틀린 곳 ▶ ① are → is\n이유: 의문사절 주어는 단수\n나머지 ▶ ② be taken to be ~으로 여겨지다 ✔ ③ tend to ✔")]
SCR=[0,3,4,5,7,2]
ORDER=[[0,1,2,3],[4,5,6,7]]
INSERT=[([1,2,3,4],2,"정답 ▶ ②\n이유: that assertion(그 주장)은 '철학자는 삶의 좋은 것을 다 누릴 자격이 있다'는 앞 문장을 가리켜요."),
 ([4,5,6,7],3,"정답 ▶ ③\n이유: As a result(그 결과)는 '그의 이해는 특권층 엘리트의 시각을 보여 주는 지표'라는 앞 문장의 결과예요. 그래서 깊은 결함이 있다 → 맨 끝")]
ODD=[([1,2,"Aristotle also studied biology and classified hundreds of animal species.",3],2,"정답 ▶ ③\n이유: 철학자의 특권 → 그 주장(that assertion)은 자기 잇속만 차리는 듯하다는 흐름이에요. 생물학 연구 이야기는 관계없고 that assertion이 가리킬 대상도 끊어져요.")]
BLANK=[BL(p,'Because of their practice','worthy',["afraid","unable","ashamed"],"정답 ▶ worthy (자격이 있는)\n이유: 사유를 실천한다는 이유로 삶의 좋은 것을 다 누릴 '자격이 있다'고 여겨졌어요.\n오답 ▶ afraid 두려워하는 · unable ~할 수 없는 · ashamed 부끄러운"),
 BL(p,'Human flourishing','inclusive',["ancient","expensive","popular"],"정답 ▶ inclusive (포용적인)\n이유: 노예제를 정당화한 사상 → 오늘날 우리가 원하는 만큼 '모두를 포함하지' 못함\n오답 ▶ ancient 고대의 · expensive 비싼 · popular 인기 있는"),
 BL(p,'As a result','flawed',["admired","ignored","original"],"정답 ▶ flawed (결함이 있는)\n이유: for all it does well(잘하는 점이 있지만)과 대조\n오답 ▶ admired 존경받는 · ignored 무시된 · original 독창적인")]
GRAM=[{'q':"다음 문장과 뜻이 같은 것은?<br><b>Consistent though he may be, some of his ideas seem strange.</b>",'opts':["Though he may be consistent, some of his ideas seem strange.","Because he is consistent, some of his ideas seem strange.","If he were consistent, some of his ideas would seem strange.","Unless he is consistent, some of his ideas seem strange."],'ex':"정답 ▶ Though he may be consistent, ~\n이유: 형용사/명사 + though[as] + 주어 + 동사 = 양보(~이긴 하지만)의 도치"},
 {'q':"빈칸에 알맞은 것은?<br><b>He had no difficulty ______ slavery.</b>",'opts':["justifying","to justify","justify","justified"],'ex':"정답 ▶ justifying\n이유: have difficulty (in) -ing"},
 {'q':"빈칸에 알맞은 것은?<br><b>It serves us ______ that every thinker is of her own time.</b>",'opts':["to remember","remember","remembered","to remembering"],'ex':"정답 ▶ to remember\n이유: 가주어 It - 진주어 to부정사"},
 {'q':"빈칸에 알맞은 것은?<br><b>His idea was not nearly as ______ as we want it to be today.</b>",'opts':["inclusive","more inclusive","most inclusive","inclusively"],'ex':"정답 ▶ inclusive\n이유: as + 형용사 원급 + as. be동사 보어라 형용사\n포인트 ▶ not nearly as ~ as … …에 훨씬 못 미치는"}]
