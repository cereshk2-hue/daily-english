from fw import *
ODDS="The various rocks and minerals contained in glaciers have become a popular subject of science projects in schools."
p=P(35,'고3 6월 35번 · 무관한 문장',[
("A genuine glacier must be permanent.","진정한 빙하는 영구적이어야 한다."),
("Generally, this implies that sufficient fresh snow must accumulate during the cold months to offset melting during the summer, although on a year-to-year basis, glaciers may expand or contract, depending on local and global climatic conditions.","일반적으로 이것은 여름 동안 녹는 것을 상쇄할 만큼 충분한 새 눈이 추운 달에 쌓여야 한다는 뜻이지만, 해마다 빙하는 지역적·지구적 기후 조건에 따라 커지거나 줄어들 수 있다."),
("Today, most glaciers around the world are melting because of the warming climate, and it appears that the rate of melting is accelerating.","오늘날 전 세계 대부분의 빙하가 따뜻해지는 기후 때문에 녹고 있으며, 녹는 속도가 빨라지고 있는 것으로 보인다."),
("This has been documented spectacularly in places such as the Alps, where historical records have been kept and dated sketches and photographs are available to compare with the present extent of ice.","이것은 알프스 같은 곳에서 극적으로 기록되어 왔는데, 그곳에는 역사적 기록이 보존되어 있고 날짜가 적힌 스케치와 사진을 현재의 얼음 범위와 비교할 수 있다."),
("Even over periods as short as a few decades, satellite images show that dramatic reduction of mountain glaciers has occurred in the Andes, the Himalayas, and elsewhere.","불과 수십 년의 짧은 기간 동안에도 안데스, 히말라야 및 다른 곳에서 산악 빙하가 극적으로 줄어들었다는 것을 위성 사진이 보여 준다."),
("It is estimated that many small mountain glaciers will disappear completely within ten to twenty years unless there is a sudden and unexpected change in the present warming trend.","현재의 온난화 추세에 갑작스럽고 예상치 못한 변화가 없다면, 많은 작은 산악 빙하가 10년에서 20년 안에 완전히 사라질 것으로 추정된다.")],
"* offset: 상쇄하다")
VOCAB=[["genuine","진짜의, 진정한"],["glacier","빙하"],["permanent","영구적인"],["imply","~을 의미하다, 암시하다"],["sufficient","충분한"],["accumulate","쌓이다"],
 ["offset","~을 상쇄하다"],["on a year-to-year basis","해마다"],["expand","커지다, 확장되다"],["contract","줄어들다, 수축하다"],["depending on","~에 따라"],
 ["climatic","기후의"],["accelerate","가속화되다"],["document","~을 기록하다"],["spectacularly","극적으로, 눈부시게"],["historical record","역사적 기록"],
 ["dated","날짜가 적힌"],["extent","범위, 정도"],["decade","10년"],["satellite image","위성 사진"],["dramatic","극적인"],["reduction","감소"],
 ["occur","일어나다"],["estimate","~을 추정하다"],["unless","~하지 않는 한"],["trend","추세"]]
E=p.E
EXAM=[EXQ(35,'35. 다음 글에서 전체 흐름과 관계 <u>없는</u> 문장은?',p.full(' '.join([E[0],E[1],'①'+E[2],'②'+E[3],'③'+E[4],'④'+ODDS,'⑤'+E[5]])),["①","②","③","④","⑤"],3,
 "정답 ▶ ④\n이유: 빙하는 영구적이어야 함 → 오늘날 대부분 녹고 속도가 빨라짐 → 알프스 기록 → 위성 사진으로 본 감소 → 10~20년 안에 사라질 것. '빙하 속 암석과 광물이 학교 과학 프로젝트 주제가 됐다'는 빙하가 '녹고 있다'는 흐름과 관계없어요.\n오답 ▶ ① 녹는 속도 가속 ② 알프스 기록(This = 녹는 현상) ③ 위성 사진 증거 ⑤ 미래 전망\n포인트 ▶ 무관한 문장은 소재(glaciers)는 같지만 주제(녹음)에서 벗어나요.",v=False),
 EXQ(35,'다음 글의 주제로 가장 적절한 것은?',p.full(),["the accelerating loss of glaciers due to a warming climate","how glaciers are formed during the cold months","the beauty of the Alps in historical photographs","the use of satellites in mountain climbing","why some glaciers grow larger every year"],0,
 "정답 ▶ ① 따뜻해지는 기후로 인한 빙하의 가속화되는 소실\n이유: most glaciers ~ are melting because of the warming climate, the rate of melting is accelerating + 알프스·위성 사진의 증거 + 10~20년 안에 사라질 전망\n오답 ▶ ② 빙하 형성은 도입부의 조건일 뿐 ③ 사진은 증거 자료 ④ 등산 이야기 아님 ⑤ 커지는 게 아니라 줄어듦\n포인트 ▶ Today 이후가 글의 중심"),
 EXQ(35,'다음 빈칸에 들어갈 말로 가장 적절한 것은?',p.blank('permanent'),["permanent","temporary","colorful","small","famous"],0,
 "정답 ▶ ① permanent (영구적인)\n이유: 바로 뒤 '이것은 여름에 녹는 양을 상쇄할 만큼 겨울에 눈이 쌓여야 한다는 뜻' → 계속 남아 있어야(영구적) 진짜 빙하\n오답 ▶ ② temporary 일시적인(반대) ③ colorful 다채로운 ④ small 작은 ⑤ famous 유명한\n포인트 ▶ this implies that ~ 이 앞 문장을 풀어 줘요.")]
PICK1=[PK(p,'A genuine','permanent','temporary',"정답 ▶ permanent (영구적인)\n오답 ▶ temporary (일시적인)\n이유: 여름 녹는 양을 겨울 눈이 상쇄해야 → 계속 남아 있는 빙하"),
 PK(p,'Generally','accumulate','evaporate',"정답 ▶ accumulate (쌓이다)\n오답 ▶ evaporate (증발하다)\n이유: 추운 달에 새 눈이 '쌓여야' 여름의 녹음을 상쇄"),
 PK(p,'Generally','offset','increase',"정답 ▶ offset (상쇄하다)\n오답 ▶ increase (늘리다)\n이유: 겨울에 쌓인 눈이 여름의 녹음을 '메워야' 빙하가 유지돼요."),
 PK(p,'Today, most','accelerating','slowing',"정답 ▶ accelerating (가속화되는)\n오답 ▶ slowing (느려지는)\n이유: 따뜻해지는 기후 + 뒤의 '극적인 감소', '10~20년 안에 사라짐' → 빨라지고 있음"),
 PK(p,'Even over periods','reduction','expansion',"정답 ▶ reduction (감소)\n오답 ▶ expansion (확장)\n이유: 빙하가 녹고 있다는 흐름 → 극적인 '감소'"),
 PK(p,'It is estimated','disappear','reappear',"정답 ▶ disappear (사라지다)\n오답 ▶ reappear (다시 나타나다)\n이유: 온난화 추세가 바뀌지 않으면 → 완전히 '사라질' 것")]
TF=[TF(p,"A true glacier has to last permanently.",True,"A genuine glacier must be permanent","정답 ▶ T\n어휘 ▶ true = genuine · has to = must"),
 TF(p,"Glaciers never change in size from year to year.",False,"glaciers may expand or contract","정답 ▶ F\n이유: 해마다 기후 조건에 따라 커지거나 줄어들 수 있어요."),
 TF(p,"Most glaciers today are melting because the climate is getting warmer.",True,"most glaciers around the world are melting because of the warming climate","정답 ▶ T"),
 TF(p,"Glaciers are melting at a steadily decreasing rate.",False,"the rate of melting is accelerating","정답 ▶ F\n이유: 녹는 속도가 빨라지고 있어요(accelerating)."),
 TF(p,"In the Alps, old sketches and photographs can be compared with today's ice.",True,"dated sketches and photographs are available to compare with the present extent of ice","정답 ▶ T\n어휘 ▶ today's ice = the present extent of ice"),
 TF(p,"Many small mountain glaciers are expected to last for hundreds of years.",False,"will disappear completely within ten to twenty years","정답 ▶ F\n이유: 10~20년 안에 완전히 사라질 것으로 추정돼요.")]
MC=[MC(p,"글의 내용과 일치하지 <u>않는</u> 것은?",["Satellite images reveal that mountain glaciers have barely changed in recent decades.","Enough new snow in winter is needed to make up for summer melting.","The size of a glacier can vary from year to year with climatic conditions.","Glacier melting appears to be speeding up.","Many small glaciers may vanish within two decades."],
 "정답 ▶ Satellite images reveal that mountain glaciers have barely changed in recent decades.\n이유: satellite images show that dramatic reduction of mountain glaciers has occurred. 극적으로 줄었어요.\n오답 ▶ 나머지는 모두 본문을 다른 어휘로 바꿔 쓴 일치 문장\n포인트 ▶ barely 거의 ~ 않다 ↔ dramatic · make up for = offset · vary = expand or contract · speed up = accelerate · vanish = disappear · two decades = twenty years",
 [["위성 사진은 최근 수십 년간 산악 빙하가 거의 변하지 않았음을 보여 준다.","dramatic reduction of mountain glaciers has occurred","✗ 극적으로 감소"],["여름의 녹음을 메우려면 겨울에 충분한 새 눈이 필요하다.","sufficient fresh snow must accumulate during the cold months to offset melting","make up for = offset"],["빙하의 크기는 기후 조건에 따라 해마다 달라질 수 있다.","glaciers may expand or contract","vary = expand or contract"],["빙하가 녹는 속도가 빨라지는 것 같다.","the rate of melting is accelerating","speed up = accelerate"],["많은 작은 빙하가 20년 안에 사라질 수 있다.","within ten to twenty years","vanish = disappear · two decades = twenty years"]]),
 MC(p,"글의 내용과 <u>일치하는</u> 것은?",["알프스에는 역사적 기록이 남아 있어 빙하의 변화를 비교할 수 있다.","진정한 빙하는 여름마다 완전히 녹았다가 다시 생긴다.","빙하는 지역 기후의 영향만 받는다.","위성 사진은 히말라야 빙하가 늘어났음을 보여 준다.","온난화 추세가 바뀌지 않아도 작은 빙하는 계속 남을 것이다."],
 "정답 ▶ 알프스에는 역사적 기록이 남아 있어 빙하의 변화를 비교할 수 있다.\n이유: historical records have been kept and dated sketches and photographs are available to compare\n오답 ▶ ② must be permanent ③ local and global(지역과 지구) ④ dramatic reduction ⑤ will disappear completely\n포인트 ▶ unless ~하지 않는 한",
 [["","historical records have been kept","일치 ✔"],["","A genuine glacier must be permanent","영구적"],["","local and global climatic conditions","지역 + 지구"],["","dramatic reduction","감소"],["","will disappear completely","사라짐"]])]
PICK2=[PK(p,'Generally','that sufficient','what sufficient',"정답 ▶ that\n이유: implies의 목적어절, 뒤가 완전한 문장 → that"),
 PK(p,'Generally','although','despite',"정답 ▶ although\n이유: 뒤에 주어+동사(glaciers may expand) → 접속사. despite는 전치사"),
 PK(p,'Generally','depending','depended',"정답 ▶ depending\n이유: depending on ~에 따라 (분사구문에서 굳어진 표현)"),
 PK(p,'This has been','documented','documenting',"정답 ▶ documented\n이유: 현상이 '기록되어 온' 수동 → has been p.p."),
 PK(p,'This has been','where historical','which historical',"정답 ▶ where\n이유: 선행사 the Alps(장소) + 뒤가 완전한 문장(historical records have been kept) → 관계부사 where"),
 PK(p,'It is estimated','estimated','estimating',"정답 ▶ estimated\n이유: It is estimated that ~ ~로 추정된다 (수동)")]
VERB=[VB(p,'Today, most','melting','melt',"정답 ▶ melting\n이유: are + -ing 현재진행형 (지금 녹고 있다)"),
 VB(p,'This has been','kept','keep',"정답 ▶ kept\n이유: have been + p.p. 현재완료 수동 (keep - kept - kept)"),
 VB(p,'Even over periods','show','show',"정답 ▶ show\n이유: 주어 satellite images(복수), 현재시제"),
 VB(p,'Even over periods','occurred','occur',"정답 ▶ occurred\n이유: has + p.p. 현재완료. occur는 r을 겹쳐 occurred")]
ERR=[ER(p,'Today, most',['melting',('appears','appear'),'accelerating'],1,'appears',"틀린 곳 ▶ ② appear → appears\n이유: 가주어 it(단수) → it appears that ~인 것 같다\n나머지 ▶ ① 진행형 ✔ ③ 진행형 ✔"),
 ER(p,'This has been',[('documented','documenting'),'where','available'],0,'documented',"틀린 곳 ▶ ① documenting → documented\n이유: 현상이 '기록되어 온' 수동\n나머지 ▶ ② 장소 + 완전한 문장 → where ✔ ③ 보어 형용사 ✔"),
 ER(p,'Even over periods',['as short as','show',('has occurred','have occurred')],2,'has occurred',"틀린 곳 ▶ ③ have occurred → has occurred\n이유: that절 주어는 dramatic reduction(단수). of mountain glaciers는 수식어\n나머지 ▶ ① as + 원급 + as ✔ ② 주어 images(복수) ✔")]
SCR=[0,2,4,5]
ORDER=[[0,1,2,3],[2,3,4,5]]
INSERT=[([1,2,3,4],2,"정답 ▶ ②\n이유: This has been documented ~의 This는 '빙하가 녹고 그 속도가 빨라지고 있다'는 앞 문장이에요."),
 ([2,3,4,5],3,"정답 ▶ ③\n이유: '수십 년 사이 극적으로 줄었다'는 증거 뒤에 '앞으로 10~20년 안에 사라질 것'이라는 전망이 와요. 맨 끝 자리!")]
ODD=[([2,3,"Glaciers also provide habitats for unique species of insects and algae.",4],2,"정답 ▶ ③\n이유: 빙하가 녹고 그 속도가 빨라진다는 증거(알프스 기록 → 위성 사진)를 이어 가는 흐름이에요. 빙하에 사는 생물 이야기는 관계없어요.")]
BLANK=[BL(p,'Generally','offset',["speed up","measure","ignore"],"정답 ▶ offset (상쇄하다)\n이유: 겨울에 쌓인 눈이 여름에 녹는 양을 '메워야' 빙하가 영구적일 수 있어요.\n오답 ▶ speed up 빠르게 하다 · measure 측정하다 · ignore 무시하다"),
 BL(p,'Today, most','accelerating',["decreasing","stopping","unknown"],"정답 ▶ accelerating (가속화되는)\n이유: 수십 년 사이 극적인 감소, 10~20년 안에 사라질 전망 → 빨라지고 있음\n오답 ▶ decreasing 줄어드는 · stopping 멈추는 · unknown 알려지지 않은"),
 BL(p,'It is estimated','warming',["cooling","fashion","population"],"정답 ▶ warming (온난화)\n이유: 빙하가 녹는 원인 = 따뜻해지는 기후(the warming climate)\n오답 ▶ cooling 냉각 · fashion 유행 · population 인구")]
GRAM=[{'q':"빈칸에 알맞은 것은?<br><b>It ______ that the rate of melting is accelerating.</b>",'opts':["appears","appear","appearing","is appeared"],'ex':"정답 ▶ appears\n이유: It appears that ~ = ~인 것 같다 (appear는 자동사라 수동 불가)"},
 {'q':"빈칸에 알맞은 것은?<br><b>the Alps, ______ historical records have been kept</b>",'opts':["where","which","what","that"],'ex':"정답 ▶ where\n이유: 장소 선행사 + 완전한 문장 → 관계부사 where (콤마 뒤 계속적 용법)"},
 {'q':"빈칸에 알맞은 것은?<br><b>over periods as ______ as a few decades</b>",'opts':["short","shorter","shortest","shortly"],'ex':"정답 ▶ short\n이유: as + 원급 + as (as short as = ~만큼 짧은, 불과 ~밖에 안 되는)"},
 {'q':"빈칸에 알맞은 것은?<br><b>Small glaciers will disappear ______ the warming trend suddenly changes.</b>",'opts':["unless","because","since","so that"],'ex':"정답 ▶ unless (~하지 않는 한)\n이유: 온난화 추세가 갑자기 바뀌지 '않는 한' 사라질 것 (= if ~ not)"}]
