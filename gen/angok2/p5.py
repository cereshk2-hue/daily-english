from fw import *
p=P(37,'10월 37번 · 글의 순서',[
("Reappraisal—changing the way one thinks about emotional situations—might present a particularly effective avenue to regulating emotions because it transforms emotions at their root.","재평가, 즉 감정적 상황에 대해 생각하는 방식을 바꾸는 것은 감정을 근본에서 변화시키기 때문에 감정을 조절하는 특히 효과적인 방법이 될 수 있다."),
("Take, for example, someone who is going through a divorce.","예를 들어, 이혼을 겪고 있는 사람을 생각해 보자."),
("This is often an adverse event, and yet, it can be construed in different ways.","이것은 흔히 불행한 사건이지만, 그런데도 여러 방식으로 해석될 수 있다."),
("One might view it as an overpowering loss that will mark one's family for life.","어떤 사람은 그것을 가족에게 평생 흔적을 남길 압도적인 상실로 볼 수 있다."),
("Alternatively, one might see it as something that is painful but that might lead to positive outcomes in the long run, such as improved relationships.","또는, 그것을 고통스럽지만 장기적으로는 개선된 관계 같은 긍정적인 결과로 이어질 수 있는 것으로 볼 수도 있다."),
("As a result of these different construals, one might feel different emotions.","이러한 서로 다른 해석의 결과로, 사람은 서로 다른 감정을 느낄 수 있다."),
("The first construal may bring intense sadness and anger.","첫 번째 해석은 강렬한 슬픔과 분노를 가져올 수 있다."),
("The second construal might also bring sadness and anger but perhaps at lower levels.","두 번째 해석도 슬픔과 분노를 가져올 수 있지만 아마 더 낮은 수준일 것이다."),
("Crucially, it might also bring some positive emotions, such as hope, strength, or gratitude.","결정적으로, 그것은 희망, 힘, 감사 같은 긍정적인 감정도 가져올 수 있다."),
("This example illustrates how reappraisal might powerfully transform short-term emotional responses.","이 예는 재평가가 단기적인 감정 반응을 얼마나 강력하게 변화시킬 수 있는지 보여 준다."),
("When repeated over time, these short-term emotional consequences of reappraisal might accumulate to shape people's psychological health.","시간이 지나며 반복되면, 재평가가 낳은 이러한 단기적인 감정 결과는 쌓여서 사람들의 심리적 건강을 형성할 수 있다."),
("Thereby, reappraisal might be a key to resilience.","그렇게 함으로써, 재평가는 회복 탄력성의 열쇠가 될 수 있다.")],
"* resilience: 회복 탄력성 ** construe: 해석하다")
VOCAB=[["reappraisal","재평가"],["avenue","방법, 수단"],["regulate","~을 조절하다"],["transform","~을 변화시키다"],["at one's root","근본에서","at their root"],
 ["go through","~을 겪다"],["divorce","이혼"],["adverse","불리한, 불행한"],["construe","~을 해석하다"],["overpowering","압도적인"],["mark","~에 흔적을 남기다"],
 ["for life","평생"],["alternatively","또는, 그 대신에"],["outcome","결과"],["in the long run","장기적으로"],["construal","해석"],["intense","강렬한"],
 ["crucially","결정적으로"],["gratitude","감사"],["illustrate","~을 보여 주다, 설명하다"],["short-term","단기적인"],["accumulate","쌓이다, 축적되다"],
 ["psychological","심리적인"],["thereby","그렇게 함으로써"],["resilience","회복 탄력성"]]
EXAM=[EXQ(37,'37. 주어진 글 다음에 이어질 글의 순서로 가장 적절한 것은? [3점]',p.order_q([0],{'A':[9,10,11],'B':[1,2,3,4],'C':[5,6,7,8]}),ORD,2,
 "정답 ▶ ③ (B)-(C)-(A)\n이유: 주어진 글(재평가는 감정을 근본에서 바꾸는 효과적인 방법) → (B) 예를 들어(Take, for example) 이혼을 두 가지로 해석 → (C) 이 다른 해석들(these different construals)의 결과 다른 감정 → (A) 이 예(This example)는 재평가의 힘을 보여 주고, 반복되면 회복 탄력성의 열쇠\n포인트 ▶ (C)의 these different construals는 (B)의 두 해석을, (A)의 This example은 (B)~(C)의 이혼 예시 전체를 받아요.",v=False),
 EXQ(37,'다음 글의 요지로 가장 적절한 것은?',p.full(),["상황을 다르게 해석하는 재평가는 감정을 근본적으로 바꾸어 회복 탄력성을 키울 수 있다.","이혼과 같은 불행한 사건은 반드시 부정적인 감정만 남긴다.","부정적인 감정은 억누르는 것이 가장 효과적이다.","단기적인 감정 반응은 심리적 건강과 관계가 없다.","가족 관계는 시간이 지나면 저절로 회복된다."],0,
 "정답 ▶ ① 상황을 다르게 해석하는 재평가는 감정을 근본적으로 바꾸어 회복 탄력성을 키울 수 있다.\n이유: 첫 문장(재평가는 감정을 근본에서 변화) + 마지막 문장(회복 탄력성의 열쇠)이 요지, 이혼은 예시\n오답 ▶ ② 다르게 해석하면 긍정적 감정도 생김 ③ 억누르기가 아니라 '생각 바꾸기' ④ 쌓여서 심리적 건강을 형성 ⑤ 언급 없음\n포인트 ▶ 요지 = 첫 문장 + 결론(Thereby)"),
 EXQ(37,'다음 빈칸에 들어갈 말로 가장 적절한 것은?',p.blank('transforms emotions at their root'),["transforms emotions at their root","prevents painful events from happening","helps us forget negative experiences","replaces emotions with pure logic","makes people avoid emotional situations"],0,
 "정답 ▶ ① 감정을 근본에서 변화시킨다\n이유: 같은 이혼도 다르게 해석하면 '느끼는 감정 자체'가 달라져요(슬픔이 줄고 희망·감사가 생김) → 감정의 뿌리(해석)를 바꿈\n오답 ▶ ② 사건 자체는 막지 못함 ③ 잊는 게 아니라 다르게 봄 ④ 감정을 없애지 않음 ⑤ 상황을 피하는 게 아니라 다르게 생각함\n포인트 ▶ because 뒤 = 효과적인 '이유'")]
PICK1=[PK(p,'Reappraisal','effective','ineffective',"정답 ▶ effective (효과적인)\n오답 ▶ ineffective (효과 없는)\n이유: 감정을 '근본에서' 바꾸기 때문에 → 특히 효과적인 방법"),
 PK(p,'This is often','adverse','advantageous',"정답 ▶ adverse (불행한, 불리한)\n오답 ▶ advantageous (유리한)\n이유: and yet(그런데도) 다르게 해석될 수 있다 → 앞은 '불행한' 사건"),
 PK(p,'One might view','overpowering','overlooked',"정답 ▶ overpowering (압도적인)\n오답 ▶ overlooked (간과된)\n이유: 가족에게 평생 흔적을 남길 '압도적인' 상실 → 첫 번째(부정적) 해석"),
 PK(p,'Alternatively','positive','negative',"정답 ▶ positive (긍정적인)\n오답 ▶ negative (부정적인)\n이유: but으로 painful과 대조 + such as improved relationships(개선된 관계)"),
 PK(p,'The second construal','lower','higher',"정답 ▶ lower (더 낮은)\n오답 ▶ higher (더 높은)\n이유: 두 번째(긍정적) 해석 → 슬픔과 분노가 '덜함'"),
 PK(p,'When repeated','accumulate','disappear',"정답 ▶ accumulate (쌓이다)\n오답 ▶ disappear (사라지다)\n이유: 시간이 지나며 반복되면 '쌓여서' 심리적 건강을 형성")]
TF=[TF(p,"Reappraisal means changing how one thinks about emotional situations.",True,"changing the way one thinks about emotional situations","정답 ▶ T\n이유: 대시(—) 사이가 reappraisal의 정의예요."),
 TF(p,"A divorce can be understood in only one way.",False,"it can be construed in different ways","정답 ▶ F\n이유: 여러 방식으로 해석될 수 있어요.\n어휘 ▶ understand ≒ construe"),
 TF(p,"Seeing a divorce as a lifelong loss may lead to strong sadness and anger.",True,"The first construal may bring intense sadness and anger","정답 ▶ T\n어휘 ▶ strong = intense · lifelong = for life"),
 TF(p,"The second way of thinking removes all sadness and anger.",False,"might also bring sadness and anger but perhaps at lower levels","정답 ▶ F\n이유: 슬픔과 분노도 오지만 '더 낮은 수준'이에요."),
 TF(p,"Positive emotions such as hope can come from seeing a painful event differently.",True,"some positive emotions, such as hope, strength, or gratitude","정답 ▶ T\n이유: 두 번째 해석은 희망, 힘, 감사도 가져올 수 있어요."),
 TF(p,"The short-term effects of reappraisal have no influence on psychological health.",False,"might accumulate to shape people's psychological health","정답 ▶ F\n이유: 반복되면 쌓여서 심리적 건강을 형성할 수 있어요.")]
MC=[MC(p,"글의 내용과 일치하지 <u>않는</u> 것은?",["Reappraisal works by changing the situation itself rather than one's view of it.","A divorce is often an unfortunate event that can be interpreted differently.","Seeing a divorce as painful but possibly beneficial is one possible view.","Different interpretations can produce different feelings.","Reappraisal may help people bounce back from hardship."],
 "정답 ▶ Reappraisal works by changing the situation itself rather than one's view of it.\n이유: changing the way one thinks about emotional situations. 상황이 아니라 '생각하는 방식'을 바꿔요.\n오답 ▶ 나머지는 모두 본문을 다른 어휘로 바꿔 쓴 일치 문장\n포인트 ▶ unfortunate = adverse · interpret = construe · beneficial ≒ lead to positive outcomes · bounce back 회복하다 ≒ resilience",
 [["재평가는 상황에 대한 관점이 아니라 상황 자체를 바꿔서 작동한다.","changing the way one thinks about emotional situations","✗ 생각하는 방식을 바꿈"],["이혼은 흔히 불행한 사건이지만 다르게 해석될 수 있다.","often an adverse event, and yet, it can be construed in different ways","unfortunate = adverse · interpret = construe"],["이혼을 고통스럽지만 이로울 수도 있는 것으로 보는 것도 가능한 관점이다.","painful but that might lead to positive outcomes","beneficial ≒ positive outcomes"],["다른 해석은 다른 감정을 낳을 수 있다.","As a result of these different construals, one might feel different emotions","일치"],["재평가는 사람들이 역경에서 회복하도록 도울 수 있다.","reappraisal might be a key to resilience","bounce back ≒ resilience"]]),
 MC(p,"글의 내용과 <u>일치하는</u> 것은?",["재평가로 생긴 단기적인 감정 결과가 쌓이면 심리적 건강에 영향을 줄 수 있다.","재평가는 감정을 겉으로만 바꾸기 때문에 효과가 약하다.","이혼을 평생의 상실로 보면 긍정적인 감정이 생긴다.","두 번째 해석은 슬픔과 분노를 더 강하게 만든다.","재평가는 회복 탄력성과 관계가 없다."],
 "정답 ▶ 재평가로 생긴 단기적인 감정 결과가 쌓이면 심리적 건강에 영향을 줄 수 있다.\n이유: these short-term emotional consequences of reappraisal might accumulate to shape people's psychological health\n오답 ▶ ② at their root 근본에서 ③ 강렬한 슬픔과 분노 ④ at lower levels ⑤ a key to resilience\n포인트 ▶ accumulate 쌓이다 · shape 형성하다",
 [["","might accumulate to shape people's psychological health","일치 ✔"],["","transforms emotions at their root","근본에서"],["","The first construal may bring intense sadness and anger","부정적 감정"],["","perhaps at lower levels","더 낮음"],["","a key to resilience","열쇠"]])]
PICK2=[PK(p,'Reappraisal','regulating','regulate',"정답 ▶ regulating\n이유: avenue to ~ 의 to는 전치사(~으로 가는 길) → 동명사"),
 PK(p,'Take, for example','is going','are going',"정답 ▶ is going\n이유: who의 선행사 someone(단수)"),
 PK(p,'This is often','be construed','construe',"정답 ▶ be construed\n이유: 사건이 '해석되는' 수동 → can be p.p."),
 PK(p,'Alternatively','might lead','might leads',"정답 ▶ lead\n이유: 조동사 might + 동사원형"),
 PK(p,'This example','how reappraisal','what reappraisal',"정답 ▶ how\n이유: 뒤가 완전한 문장(reappraisal might transform ~) → 의문부사 how(어떻게, 얼마나)"),
 PK(p,'When repeated','repeated','repeating',"정답 ▶ repeated\n이유: When (they are) repeated — 감정 결과가 '반복되는' 수동 → 과거분사")]
VERB=[VB(p,'Reappraisal','transforms','transform',"정답 ▶ transforms\n이유: because절 주어 it(= reappraisal, 단수), 현재시제"),
 VB(p,'This is often','construed','construe',"정답 ▶ construed\n이유: can be + p.p. 조동사 수동"),
 VB(p,'This example','illustrates','illustrate',"정답 ▶ illustrates\n이유: 주어 This example(단수)"),
 VB(p,'When repeated','accumulate','accumulate',"정답 ▶ accumulate\n이유: 조동사 might + 동사원형")]
ERR=[ER(p,'Take, for example',['Take','for example',('is going','are going')],2,'is going',"틀린 곳 ▶ ③ are going → is going\n이유: 선행사 someone(단수)\n나머지 ▶ ① 명령문 Take ✔ ② 삽입구 ✔"),
 ER(p,'Alternatively',['Alternatively',('see','seeing'),'lead'],1,'see',"틀린 곳 ▶ ② seeing → see\n이유: 조동사 might + 동사원형\n나머지 ▶ ① 부사 ✔ ③ might lead ✔"),
 ER(p,'When repeated',[('repeated','repeating'),'consequences','to shape'],0,'repeated',"틀린 곳 ▶ ① repeating → repeated\n이유: 결과가 '반복되는' 수동 → When (they are) repeated\n나머지 ▶ ② 주어 ✔ ③ 결과의 to부정사(쌓여서 ~을 형성하다) ✔")]
SCR=[1,2,3,5,9,11]
ORDER=[[1,2,3,4],[5,6,7,8]]
INSERT=[([0,1,2,3],1,"정답 ▶ ①\n이유: Take, for example(예를 들어)은 첫 문장(재평가가 효과적인 방법)의 예시를 시작해요. 그리고 다음 문장 This가 바로 그 이혼을 받아요."),
 ([4,5,6,7],1,"정답 ▶ ①\n이유: these different construals(이런 다른 해석들)는 앞의 두 해석(평생의 상실 / 고통스럽지만 긍정적 결과)을 가리켜요. 두 번째 해석이 나온 바로 뒤!")]
ODD=[([5,6,"Divorce rates have risen steadily in many countries over the past fifty years.",7],2,"정답 ▶ ③\n이유: 두 해석이 가져오는 감정의 차이를 비교하는 흐름이에요. 이혼율 통계는 관계없어요.")]
BLANK=[BL(p,'This is often','construed',["avoided","forgotten","prevented"],"정답 ▶ construed (해석된)\n이유: 다음 문장들에서 두 가지 '해석'(view it as / see it as)이 나와요.\n오답 ▶ avoided 피해진 · forgotten 잊힌 · prevented 예방된"),
 BL(p,'Crucially','gratitude',["jealousy","guilt","fear"],"정답 ▶ gratitude (감사)\n이유: positive emotions(긍정적인 감정)의 예 → 희망, 힘, 감사\n오답 ▶ jealousy 질투 · guilt 죄책감 · fear 두려움 — 모두 부정적 감정"),
 BL(p,'Thereby','resilience',["divorce","anger","isolation"],"정답 ▶ resilience (회복 탄력성)\n이유: 긍정적인 감정 결과가 쌓여 심리적 건강을 형성 → 어려움에서 다시 일어서는 힘\n오답 ▶ divorce 이혼 · anger 분노 · isolation 고립")]
GRAM=[{'q':"빈칸에 알맞은 것은?<br><b>I look forward to ______ you again.</b>",'opts':["seeing","see","saw","seen"],'ex':"정답 ▶ seeing\n이유: look forward to의 to는 전치사 → 동명사\n본문 ▶ an avenue to regulating emotions (전치사 to + -ing)"},
 {'q':"빈칸에 알맞은 것은?<br><b>The event can ______ in different ways.</b>",'opts':["be construed","construe","construing","be construing"],'ex':"정답 ▶ be construed\n이유: 사건이 '해석되는' 수동 → 조동사 + be + p.p."},
 {'q':"빈칸에 알맞은 것은?<br><b>When ______ over time, these responses may accumulate.</b>",'opts':["repeated","repeating","repeat","to repeat"],'ex':"정답 ▶ repeated\n이유: 접속사를 남긴 분사구문. 반응이 '반복되는' 수동 → 과거분사"},
 {'q':"빈칸에 알맞은 것은?<br><b>This example illustrates ______ reappraisal can transform emotions.</b>",'opts':["how","what","which","who"],'ex':"정답 ▶ how\n이유: 뒤가 완전한 문장 → how(어떻게)가 이끄는 간접의문문"}]
