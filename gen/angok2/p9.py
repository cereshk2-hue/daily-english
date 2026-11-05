from fw import *
p=P(40,'고3 6월 40번 · 요약문',[
("A serious deterioration in people's working lives would be deeply disturbing to the social order.","사람들의 직장 생활이 심각하게 악화된다면 사회 질서를 크게 어지럽힐 것이다."),
("Indeed, few consequences of technological change would be as dangerous.","실제로, 기술 변화가 가져올 결과 중 이만큼 위험한 것은 거의 없을 것이다."),
("Today, the world of work is the main way that we share out the fruits of growth: for most people, their job is their main, if not their only, source of income.","오늘날 일의 세계는 우리가 성장의 결실을 나누는 주된 방식이다. 대부분의 사람들에게 직업은 유일하지는 않더라도 주된 소득원이다."),
("Technological unemployment would weaken that longstanding arrangement, encouraging an even more extreme version of inequality in which some people receive more income than others and many receive nothing at all.","기술적 실업은 그 오래된 체계를 약화시키고, 어떤 사람들은 남보다 더 많은 소득을 얻고 많은 사람은 전혀 얻지 못하는 훨씬 더 극단적인 불평등을 부추길 것이다."),
("Nor would the disturbance be only economic.","또한 그 혼란은 경제적인 것에만 그치지도 않을 것이다."),
("For many people, their work is both a source of income and of meaning.","많은 사람들에게 일은 소득의 원천이자 의미의 원천이다."),
("And with that in mind, the threat is even broader: not only that the labor market might be hollowed out, leaving some unable to find a good job and a reliable income, but that this sense of fulfilment that some people are fortunate to feel in their jobs might be hollowed out as well, leaving them unable to find purpose and live a satisfying life.","그리고 그 점을 염두에 두면 위협은 훨씬 더 넓다. 노동 시장이 텅 비어 일부 사람들이 좋은 일자리와 안정적인 소득을 찾지 못하게 될 수 있을 뿐 아니라, 일부 사람들이 운 좋게 일에서 느끼는 성취감마저 텅 비어 그들이 목적을 찾고 만족스러운 삶을 살 수 없게 될 수도 있다는 것이다.")],
"* deterioration: 악화 ** hollow: 속이 비게 하다")
VOCAB=[["deterioration","악화"],["disturbing","혼란을 주는, 불안하게 하는"],["social order","사회 질서"],["consequence","결과"],["share out","~을 나누다, 분배하다"],
 ["fruit","결실, 성과"],["if not","~은 아니더라도","if not their only"],["source of income","소득원"],["unemployment","실업"],["weaken","~을 약화시키다"],
 ["longstanding","오래된, 오래 지속된"],["arrangement","체계, 방식"],["encourage","~을 부추기다, 조장하다"],["extreme","극단적인"],["inequality","불평등"],
 ["disturbance","혼란"],["with ~ in mind","~을 염두에 두고"],["threat","위협"],["labor market","노동 시장"],["hollow out","~의 속을 비게 하다","hollowed out"],
 ["reliable","믿을 만한, 안정적인"],["fulfilment","성취감"],["fortunate","운이 좋은"],["purpose","목적"],["satisfying","만족스러운"]]
SUMM='<span class="exam-box en"><b>요약문</b> By creating unemployment, technology would upset the social order, affecting the <u>&nbsp;&nbsp;(A)&nbsp;&nbsp;</u> of wealth and possibly eliminating the emotional <u>&nbsp;&nbsp;(B)&nbsp;&nbsp;</u> that some discover in work.</span>'
EXAM=[EXQ(40,'40. 다음 글의 내용을 한 문장으로 요약하고자 한다. 빈칸 (A), (B)에 들어갈 말로 가장 적절한 것은?',p.full()+SUMM,["distribution …… emptiness","distribution …… rewards","concentration …… conflicts","investment …… challenges","investment …… growth"],1,
 "정답 ▶ ② distribution(분배) …… rewards(보상)\n이유: (A) 일은 성장의 결실을 '나누는(share out)' 주된 방식인데, 기술적 실업은 이를 약화시켜 불평등을 키움 → 부의 '분배'에 영향 (B) 일은 소득뿐 아니라 '의미'와 '성취감(fulfilment)'의 원천 → 일에서 발견하는 정서적 '보상'을 없앨 수 있음\n오답 ▶ ① emptiness(공허함)를 없앤다면 좋은 일이 됨 ③ concentration 집중, conflicts 갈등 ④ ⑤ investment 투자 — 본문은 '나눔'의 문제\n포인트 ▶ share out the fruits of growth = distribution of wealth · sense of fulfilment = emotional rewards",v=False),
 EXQ(40,'다음 글의 주제로 가장 적절한 것은?',p.full(),["the economic and emotional threats of technological unemployment","ways technology creates new kinds of jobs","why income inequality has disappeared","how to find a job with a reliable income","the history of the modern labor market"],0,
 "정답 ▶ ① 기술적 실업의 경제적·정서적 위협\n이유: 기술적 실업 → 소득 분배 체계 약화와 불평등(경제적), Nor would the disturbance be only economic → 일의 의미와 성취감 상실(정서적)\n오답 ▶ ② 일자리 창출 이야기 아님 ③ 불평등이 더 심해짐 ④ 구직 방법 아님 ⑤ 역사 아님\n포인트 ▶ 글이 두 단계(경제 → 의미)로 위협을 넓혀 가요."),
 EXQ(40,'밑줄 친 부분이 다음 글에서 의미하는 바로 가장 적절한 것은?',p.full(p.text().replace('the threat is even broader','<u>the threat is even broader</u>')),["Technology could take away not only people's income but also the meaning they find in work.","Technology will create more jobs than it destroys.","Only people with low incomes will be affected by technology.","The labor market will become larger than ever before.","People will find more purpose outside of work."],0,
 "정답 ▶ ① 기술은 사람들의 소득뿐 아니라 일에서 찾는 의미까지 빼앗을 수 있다.\n이유: 콜론(:) 뒤 not only (노동 시장이 비어 소득을 잃음) but (일에서 느끼는 성취감도 비어 목적을 잃음) → 위협이 경제를 넘어 '의미'까지 넓어짐\n오답 ▶ ② 일자리가 오히려 줄어듦 ③ 일부(some)만이 아니라 성취감을 느끼던 사람들까지 ④ 노동 시장이 텅 빔 ⑤ 목적을 찾지 못하게 됨\n포인트 ▶ 콜론 뒤는 앞말의 구체적인 설명")]
PICK1=[PK(p,'A serious deterioration','disturbing','comforting',"정답 ▶ disturbing (혼란을 주는)\n오답 ▶ comforting (위안을 주는)\n이유: 직장 생활의 '심각한 악화' → 사회 질서를 어지럽힘. 다음 문장의 dangerous와 같은 방향"),
 PK(p,'Today, the world','income','expense',"정답 ▶ income (소득)\n오답 ▶ expense (지출)\n이유: 일 = 성장의 결실을 나누는 방식 → 직업은 주된 '소득원'"),
 PK(p,'Technological unemployment','weaken','strengthen',"정답 ▶ weaken (약화시키다)\n오답 ▶ strengthen (강화하다)\n이유: 기술 때문에 일자리가 없어지면 '일로 소득을 나누는' 오래된 체계가 약해져요."),
 PK(p,'Technological unemployment','of inequality','of equality',"정답 ▶ inequality (불평등)\n오답 ▶ equality (평등)\n이유: 어떤 사람은 더 많이, 많은 사람은 전혀 못 받음 → 극단적인 불평등"),
 PK(p,'And with that','reliable','unstable',"정답 ▶ reliable (믿을 만한)\n오답 ▶ unstable (불안정한)\n이유: a good job과 나란히 → 찾지 못하게 되는 '좋은 것' = 안정적인 소득"),
 PK(p,'And with that','fulfilment','frustration',"정답 ▶ fulfilment (성취감)\n오답 ▶ frustration (좌절감)\n이유: 운 좋게(fortunate) 일에서 느끼는 것 → 좋은 감정. 그것이 사라지면 목적을 잃어요.")]
TF=[TF(p,"Worsening working lives would seriously disrupt the social order.",True,"would be deeply disturbing to the social order","정답 ▶ T\n어휘 ▶ worsening ≒ deterioration · disrupt ≒ be disturbing to"),
 TF(p,"For most people, a job is their main source of income.",True,"their job is their main, if not their only, source of income","정답 ▶ T"),
 TF(p,"Technological unemployment would reduce inequality.",False,"encouraging an even more extreme version of inequality","정답 ▶ F\n이유: 훨씬 더 극단적인 불평등을 부추길 거예요."),
 TF(p,"The writer says the effects of job loss would be only economic.",False,"Nor would the disturbance be only economic","정답 ▶ F\n이유: 혼란은 경제적인 것만이 아니라고 했어요."),
 TF(p,"Work gives many people both money and meaning.",True,"both a source of income and of meaning","정답 ▶ T\n어휘 ▶ money ≒ income"),
 TF(p,"Everyone feels a sense of fulfilment in their job.",False,"some people are fortunate to feel in their jobs","정답 ▶ F\n이유: '일부' 사람들만 운 좋게 성취감을 느껴요.")]
MC=[MC(p,"글의 내용과 일치하지 <u>않는</u> 것은?",["Technological unemployment would make income more evenly distributed.","Few results of technological change would be as dangerous as worsening working lives.","Jobs are the main way people get a share of economic growth.","Losing jobs to technology could harm more than people's finances.","Some people might lose the sense of purpose they gain from their jobs."],
 "정답 ▶ Technological unemployment would make income more evenly distributed.\n이유: encouraging an even more extreme version of inequality. 오히려 불평등이 심해져요.\n오답 ▶ 나머지는 모두 본문을 다른 어휘로 바꿔 쓴 일치 문장\n포인트 ▶ evenly distributed 고르게 분배된 ↔ inequality · results = consequences · get a share of ≒ share out · finances ≒ economic",
 [["기술적 실업은 소득을 더 고르게 분배할 것이다.","an even more extreme version of inequality","✗ 불평등 심화"],["기술 변화의 결과 중 직장 생활 악화만큼 위험한 것은 거의 없다.","few consequences of technological change would be as dangerous","results = consequences"],["직업은 사람들이 경제 성장의 몫을 얻는 주된 방식이다.","the main way that we share out the fruits of growth","get a share ≒ share out"],["기술에 일자리를 잃으면 재정 이상의 피해가 생길 수 있다.","Nor would the disturbance be only economic","more than finances = not only economic"],["일부는 일에서 얻는 목적의식을 잃을 수 있다.","leaving them unable to find purpose","일치"]]),
 MC(p,"글의 내용과 <u>일치하는</u> 것은?",["기술적 실업은 사람들이 일에서 얻는 성취감까지 빼앗을 수 있다.","기술 변화는 사회 질서에 거의 영향을 주지 않는다.","대부분의 사람에게 직업은 부수적인 소득원일 뿐이다.","기술적 실업은 모든 사람의 소득을 똑같이 줄인다.","모든 사람은 자신의 일에서 성취감을 느낀다."],
 "정답 ▶ 기술적 실업은 사람들이 일에서 얻는 성취감까지 빼앗을 수 있다.\n이유: this sense of fulfilment ~ might be hollowed out as well\n오답 ▶ ② deeply disturbing ③ main(주된) 소득원 ④ some more, many nothing(불평등) ⑤ some people(일부)\n포인트 ▶ hollow out 속을 비게 하다",
 [["","this sense of fulfilment","일치 ✔"],["","deeply disturbing to the social order","크게 어지럽힘"],["","their main, if not their only, source of income","주된 소득원"],["","some people receive more income than others","불평등"],["","some people are fortunate to feel","일부만"]])]
PICK2=[PK(p,'Indeed','as dangerous','as dangerously',"정답 ▶ dangerous\n이유: be동사의 보어 → 형용사 (as + 원급 + (as ~))"),
 PK(p,'Today, the world','that we share','what we share',"정답 ▶ that\n이유: 선행사 the main way + 뒤가 완전한 문장 → 관계부사 대용 that (= in which)"),
 PK(p,'Technological unemployment','encouraging','encouraged',"정답 ▶ encouraging\n이유: 분사구문. 기술적 실업이 불평등을 '부추기는' 능동 + 목적어(an even more extreme version) → 현재분사"),
 PK(p,'Technological unemployment','even more','very more',"정답 ▶ even\n이유: 비교급 강조 → even, much, far, still (very는 비교급 강조 불가)"),
 PK(p,'Technological unemployment','in which','which some',"정답 ▶ in which\n이유: 뒤가 완전한 문장(some people receive more income) → 전치사 + 관계대명사"),
 PK(p,'Nor would','would the disturbance be','the disturbance would be',"정답 ▶ would the disturbance be\n이유: 부정어 Nor가 문장 앞 → 조동사 + 주어 + 동사 도치")]
VERB=[VB(p,'A serious deterioration','disturbing','disturb',"정답 ▶ disturbing\n이유: 사회 질서를 '어지럽히는' 능동의 성질 → 현재분사형 형용사"),
 VB(p,'Technological unemployment','receive nothing','receive',"정답 ▶ receive\n이유: 주어 many (people)(복수), in which절의 현재시제"),
 VB(p,'And with that','hollowed','hollow',"정답 ▶ hollowed\n이유: 노동 시장이 '텅 비게 되는' 수동 → might be + p.p."),
 VB(p,'And with that','leaving','leave',"정답 ▶ leaving\n이유: 결과를 나타내는 분사구문(그래서 ~하게 만들며) → 현재분사")]
ERR=[ER(p,'Today, the world',[('that','what'),'their main','source'],0,'that',"틀린 곳 ▶ ① what → that\n이유: 선행사 the main way가 있고 뒤가 완전한 문장 → that(= in which)\n나머지 ▶ ② ③ ✔"),
 ER(p,'Technological unemployment',['weaken',('encouraging','encouraged'),'in which'],1,'encouraging',"틀린 곳 ▶ ② encouraged → encouraging\n이유: 뒤에 목적어(an even more extreme version)가 있는 능동 분사구문\n나머지 ▶ ① would + 동사원형 ✔ ③ 전치사 + 관계대명사 ✔"),
 ER(p,'For many people',[('is','are'),'both','of meaning'],0,'is',"틀린 곳 ▶ ① are → is\n이유: 주어 their work(단수, 셀 수 없음)\n나머지 ▶ ② both A and B ✔ ③ a source of income and (a source) of meaning ✔")]
SCR=[0,1,4,5]
ORDER=[[0,1,2,3],[3,4,5,6]]
INSERT=[([1,2,3,4],2,"정답 ▶ ②\n이유: that longstanding arrangement(그 오래된 체계)는 앞 문장의 '일이 성장의 결실을 나누는 주된 방식'을 가리켜요."),
 ([3,4,5,6],1,"정답 ▶ ①\n이유: Nor(~도 아니다)는 앞의 경제적 피해(불평등)에 '경제적인 것만도 아니다'라고 덧붙이며, 다음 문장(일 = 의미의 원천)으로 넘어가는 다리예요.")]
ODD=[([1,2,"Many companies today offer flexible working hours to their employees.",3],2,"정답 ▶ ③\n이유: 기술적 실업이 사회 질서와 소득 분배를 위협한다는 흐름이에요. 유연 근무제 이야기는 관계없어요.")]
BLANK=[BL(p,'Today, the world','income',["stress","danger","entertainment"],"정답 ▶ income (소득)\n이유: 일 = 성장의 결실을 나누는 방식 → 소득원\n오답 ▶ stress 스트레스 · danger 위험 · entertainment 오락"),
 BL(p,'Technological unemployment','inequality',["equality","cooperation","freedom"],"정답 ▶ inequality (불평등)\n이유: 어떤 사람은 더 많이, 많은 사람은 전혀 받지 못함\n오답 ▶ equality 평등 · cooperation 협력 · freedom 자유"),
 BL(p,'For many people','meaning',["debt","boredom","conflict"],"정답 ▶ meaning (의미)\n이유: 앞 문장 '혼란은 경제적인 것만이 아니다' → 일은 소득뿐 아니라 '의미'의 원천. 뒤의 purpose, fulfilment와 연결\n오답 ▶ debt 빚 · boredom 지루함 · conflict 갈등")]
GRAM=[{'q':"다음 문장과 뜻이 가장 가까운 것은?<br><b>Few consequences of technological change would be as dangerous.</b>",'opts':["This would be one of the most dangerous consequences.","Many consequences would be equally dangerous.","This would be the least dangerous consequence.","No consequence would be dangerous at all."],'ex':"정답 ▶ This would be one of the most dangerous consequences.\n이유: Few ~ as 원급 (이만큼 ~한 것은 거의 없다) → 최상급에 가까운 의미"},
 {'q':"밑줄 친 <b>if not</b>의 뜻으로 알맞은 것은?<br><b>their main, <u>if not</u> their only, source of income</b>",'opts':["~은 아니더라도","~이 아니라면","~ 때문에","~하자마자"],'ex':"정답 ▶ ~은 아니더라도\n이유: A, if not B = B는 아닐지라도 A인 (유일한 소득원은 아니더라도 주된 소득원)"},
 {'q':"빈칸에 알맞은 것은?<br><b>Nor ______ the disturbance be only economic.</b>",'opts':["would","it would","did","has"],'ex':"정답 ▶ would\n이유: 부정어 Nor + 조동사 + 주어 + 동사원형 (도치)"},
 {'q':"빈칸에 알맞은 것은?<br><b>It might leave them ______ to find purpose.</b>",'opts':["unable","unably","inability","to unable"],'ex':"정답 ▶ unable\n이유: leave + 목적어 + 형용사(목적격보어) ~을 …한 상태로 두다 (unable to do ~할 수 없는)"}]
