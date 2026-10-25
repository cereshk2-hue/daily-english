import re
base=open('wrapup-2509-22.html',encoding='utf-8').read()
css=base[base.index('<style>'):base.index('</style>')+8]
fonts=base[base.index('<link rel="preconnect"'):base.index('<style>')]
def Q(n,stem,body): return '\n  <div class="q">\n    <div class="stem"><span class="n">%d.</span>%s</div>\n%s\n  </div>\n'%(n,stem,body)
def OL(items,en=True): return '    <ol class="ol'+(' en' if en else '')+'">'+''.join('<li><span>%s</span><span>%s</span></li>'%(c,x) for c,x in zip('①②③④⑤',items))+'</ol>'
def TB(cols,rows): return '    <table class="ch"><thead><tr><th></th>'+''.join('<th>%s</th>'%c for c in cols)+'</tr></thead><tbody>'+''.join('<tr><td>%s</td>'%c+''.join('<td>%s</td>'%x for x in r)+'</tr>' for c,r in zip('①②③④⑤',rows))+'</tbody></table>'
BOX=lambda x:'    <div class="box"><p>'+x+'</p></div>'
GIV=lambda x:'    <div class="given">'+x+'</div>'
SUM=lambda x:'    <div class="sum">'+x+'</div>'
ORD=lambda: OL(['(A) − (C) − (B)','(B) − (A) − (C)','(B) − (C) − (A)','(C) − (A) − (B)','(C) − (B) − (A)'],False)
src=lambda x:'<span class="src">[%s]</span>'%x
T='<i>When You Trap a Tiger</i>'
P1=("Children around the world learned a bit more about Korean culture when writer Tae Keller published her book "+T+" in 2020. Its story starts with a girl who meets a tiger. Her grandmother knows the tiger as well. When her grandmother gets sick, the girl makes a deal with the tiger. Keller's inspiration for her award-winning book was an old folktale that her <i>halmoni</i> (grandmother) used to tell her. It is called \"The Sun and the Moon,\" and it is about a brother, a sister, and a tiger. Keller wanted to revive the public's interest in tigers by writing her own book.")
qs=[]
qs.append(Q(1,'다음 글의 내용과 일치하지 <u>않는</u> 것은?'+src('본문 ❶'),BOX(P1)+'\n'+OL([
 "Keller's book acquainted young readers worldwide with aspects of Korean culture.",
 "The protagonist's grandmother is already familiar with the tiger.",
 "The girl strikes a bargain with the tiger when her grandmother falls ill.",
 "Keller drew on a folktale she had come across while doing research in a library.",
 "Keller aimed to rekindle public curiosity about tigers through her own writing."])))
qs.append(Q(2,'다음 글의 밑줄 친 (a)~(g) 중 어법상 <u>틀린</u> 것의 개수는?'+src('본문 ❶ 변형'),BOX(
 "Children around the world learned a bit more about Korean culture when writer Tae Keller <span class=\"tag\">(a)</span><u>published</u> her book "+T+" in 2020. Its story starts with a girl <span class=\"tag\">(b)</span><u>which</u> meets a tiger. Her grandmother knows the tiger <span class=\"tag\">(c)</span><u>as well</u>. When her grandmother <span class=\"tag\">(d)</span><u>gets</u> sick, the girl makes a deal with the tiger. Keller's inspiration for her award-winning book was an old folktale that her <i>halmoni</i> used to <span class=\"tag\">(e)</span><u>telling</u> her. It <span class=\"tag\">(f)</span><u>is called</u> \"The Sun and the Moon.\" Keller wanted to revive the public's interest in tigers by <span class=\"tag\">(g)</span><u>writing</u> her own book.")+'\n'+OL(['1개','2개','3개','4개','5개'],False)))
qs.append(Q(3,'다음 글의 밑줄 친 부분 중, 문맥상 낱말의 쓰임이 적절하지 <u>않은</u> 것은?'+src('본문 ❶ 변형'),BOX(
 "Children around the world learned a bit more about Korean culture when writer Tae Keller ①<u>concealed</u> her book "+T+" in 2020. Its story starts with a girl who ②<u>meets</u> a tiger. Her grandmother knows the tiger as well. When her grandmother gets ③<u>sick</u>, the girl makes a deal with the tiger. Keller's ④<u>inspiration</u> for her award-winning book was an old folktale that her <i>halmoni</i> used to tell her. Keller wanted to ⑤<u>revive</u> the public's interest in tigers by writing her own book.")))
qs.append(Q(4,'다음 빈칸에 들어갈 말로 가장 적절한 것은?'+src('본문 ❷'),BOX(
 "How is the tiger related to Korean culture? Long ago, tigers were so <span class=\"blank\"></span> in Korea that people often called the country the \"Land of Tigers.\" It is estimated that tigers lived in Korea for at least 100,000 years.")+'\n'+OL(['elusive','revered','plentiful','menacing','domesticated'])))
P2=("Long ago, tigers were so abundant in Korea that people often called the country the \"Land of Tigers.\" It is estimated that tigers lived in Korea for at least 100,000 years. The first appearance of a tiger in Korean culture dates back to the rock art of the Bronze Age. It depicts people hunting various animals, including tigers. Since then, tigers have appeared in many aspects of Korean culture, from legends to art and musical instruments. Some of you may have heard Korean folktales featuring tigers. In fact, approximately forty percent of Korean folktales about animals include a tiger. Tigers in Korean folktales are sometimes shown in a positive light and sometimes as foolish creatures. For example, in one story, a tiger helps a human become rich after the human saves the tiger's life.")
qs.append(Q(5,'다음 글의 내용과 일치하는 것은?'+src('본문 ❷'),BOX(P2)+'\n'+OL([
 "Tigers are estimated to have inhabited Korea for no more than ten millennia.",
 "The earliest depiction of tigers in Korea can be traced to medieval paintings.",
 "Tigers have featured in Korean legends but never in its musical instruments.",
 "Nearly half of all Korean folktales, regardless of subject, feature a tiger.",
 "In one tale, a tiger repays a human's kindness by helping that person prosper."])))
qs.append(Q(6,'(A), (B), (C)의 각 네모 안에서 어법에 맞는 표현으로 가장 적절한 것은?'+src('본문 ❷'),BOX(
 "It is estimated <b>(A)</b> [that / what] tigers lived in Korea for at least 100,000 years. The first appearance of a tiger in Korean culture dates back to the rock art of the Bronze Age. It depicts people <b>(B)</b> [hunting / hunted] various animals, including tigers. Since then, tigers <b>(C)</b> [appeared / have appeared] in many aspects of Korean culture.")+'\n'+TB(['(A)','(B)','(C)'],[
 ['what','hunting','have appeared'],['that','hunted','appeared'],['that','hunting','appeared'],['that','hunting','have appeared'],['what','hunted','have appeared']])))
qs.append(Q(7,'글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳은?'+src('본문 ❷'),GIV("It depicts people hunting various animals, including tigers.")+'\n'+BOX(
 "It is estimated that tigers lived in Korea for at least 100,000 years. ( ① ) The first appearance of a tiger in Korean culture dates back to the rock art of the Bronze Age. ( ② ) Since then, tigers have appeared in many aspects of Korean culture, from legends to art and musical instruments. ( ③ ) Some of you may have heard Korean folktales featuring tigers. ( ④ ) In fact, approximately forty percent of Korean folktales about animals include a tiger. ( ⑤ ) Tigers in Korean folktales are sometimes shown in a positive light and sometimes as foolish creatures.")))
qs.append(Q(8,'다음 글의 밑줄 친 (a)~(e)를 바꿔 쓴 말로 적절하지 <u>않은</u> 것은?'+src('본문 ❷'),BOX(
 "Long ago, tigers were so <span class=\"tag\">(a)</span><u>abundant</u> in Korea that people often called the country the \"Land of Tigers.\" It is <span class=\"tag\">(b)</span><u>estimated</u> that tigers lived in Korea for at least 100,000 years. The first appearance of a tiger in Korean culture dates back to the rock art of the Bronze Age. It <span class=\"tag\">(c)</span><u>depicts</u> people hunting various animals, including tigers. Some of you may have heard Korean folktales <span class=\"tag\">(d)</span><u>featuring</u> tigers. In fact, <span class=\"tag\">(e)</span><u>approximately</u> forty percent of Korean folktales about animals include a tiger.")+'\n'+OL(['(a) → plentiful','(b) → reckoned','(c) → conceals','(d) → showcasing','(e) → roughly'])))
qs.append(Q(9,'주어진 글 다음에 이어질 글의 순서로 가장 적절한 것은?'+src('본문 ❷'),GIV("Some of you may have heard Korean folktales featuring tigers.")+'\n'+
 '    <div class="box"><p><span class="tag">(A)</span> In fact, approximately forty percent of Korean folktales about animals include a tiger.</p><p><span class="tag">(B)</span> For example, in one story, a tiger helps a human become rich after the human saves the tiger\'s life.</p><p><span class="tag">(C)</span> Tigers in Korean folktales are sometimes shown in a positive light and sometimes as foolish creatures.</p></div>\n'+ORD()))
qs.append(Q(10,'본문 ❷의 내용과 일치하지 <u>않는</u> 것은?'+src('본문 ❷'),OL([
 "Korea was once known by a nickname alluding to its many tigers.",
 "Tigers largely vanished from Korean culture after the Bronze Age.",
 "The presence of tigers in Korea is thought to span at least a hundred millennia.",
 "Korean folktales portray tigers in both favorable and unflattering ways.",
 "Tigers appear in Korean art as well as in its legends."])))
qs.append(Q(11,'다음 빈칸에 들어갈 말로 가장 적절한 것은?'+src('본문 ❸'),BOX(
 "In another story, a tiger hears a mother tell her crying baby, \"Don't cry. Here's a <i>gotgam</i>.\" Because the baby stops crying, the tiger mistakenly thinks the <i>gotgam</i> is a very scary creature and runs away. It seems that people at the time had conflicting feelings about tigers. They had respect for tigers' power and courage. However, they were also scared of tigers because being injured or even killed by tigers was common in the past. They may have made tigers into foolish characters in order to <span class=\"blank\"></span>.")+'\n'+OL([
 "show respect for their courage","warn children about hunting","help the tiger population recover","make tigers seem more frightening","ease their own fear of them"])))
qs.append(Q(12,'밑줄 친 <u>people at the time had conflicting feelings about tigers</u>가 의미하는 바로 가장 적절한 것은?'+src('본문 ❸'),OL([
 "People could not decide whether tigers were real or imaginary.",
 "People loved tigers but disliked the foolish stories about them.",
 "People feared tigers more than any other animal.",
 "People admired tigers' strength while also dreading them.",
 "People disagreed with one another about how to hunt tigers."])))
qs.append(Q(13,'다음 글의 밑줄 친 (a)~(e) 중 어법상 <u>틀린</u> 것끼리 짝지은 것은?'+src('본문 ❸ 변형'),BOX(
 "In another story, a tiger hears a mother <span class=\"tag\">(a)</span><u>tell</u> her crying baby, \"Don't cry. Here's a <i>gotgam</i>.\" Because the baby stops crying, the tiger <span class=\"tag\">(b)</span><u>mistakenly</u> thinks the <i>gotgam</i> is a very scary creature and runs away. ... They were also scared of tigers because <span class=\"tag\">(c)</span><u>being injured</u> or even killed by tigers was common in the past. They may have made tigers into foolish characters in order <span class=\"tag\">(d)</span><u>to being</u> less scared of them. ... With the disappearance of tigers in Korea, their use as a symbol of the nation <span class=\"tag\">(e)</span><u>were faded</u> away.")+'\n'+OL(['(a), (c)','(b), (d)','(a), (e)','(c), (d)','(d), (e)'],False)))
qs.append(Q(14,'다음 글의 밑줄 친 부분 중, 문맥상 낱말의 쓰임이 적절하지 <u>않은</u> 것은?'+src('본문 ❸ 변형'),BOX(
 "Because the baby stops crying, the tiger ①<u>mistakenly</u> thinks the <i>gotgam</i> is a very scary creature and runs away. It seems that people at the time had conflicting feelings about tigers. They had respect for tigers' power and courage. However, they were also ②<u>fond</u> of tigers because being injured or even killed by tigers was common in the past. They may have made tigers into ③<u>foolish</u> characters in order to be less scared of them. Tigers in Korea faced a ④<u>decline</u> in population due to hunting during the Joseon period. However, their symbolism was ⑤<u>revived</u> in modern times through their selection as the mascot for both Olympics hosted by Korea.")))
P3b=("Tigers in Korea faced a decline in population due to hunting during the Joseon period and nearly went extinct during the Japanese colonial era. With the disappearance of tigers in Korea, their use as a symbol of the nation faded away. However, their symbolism was revived in modern times through their selection as the mascot for both Olympics hosted by Korea. Hodori was the mascot for the Seoul Summer Olympics in 1988. It was a Siberian tiger, which represents courage. The PyeongChang Winter Olympics in 2018 created Soohorang, a white tiger, as its mascot. White tigers are considered sacred guardians.")
qs.append(Q(15,'본문 ❸의 내용과 일치하지 <u>않는</u> 것은?'+src('본문 ❸'),OL([
 "The tiger flees because it correctly perceives the <i>gotgam</i> as a threat.",
 "In the past, it was not unusual for people to be wounded or killed by tigers.",
 "Hunting during the Joseon period contributed to a fall in tiger numbers.",
 "The tiger's role as a national emblem diminished as tigers disappeared.",
 "Both Olympic Games hosted by Korea adopted a tiger as their mascot."])))
qs.append(Q(16,'다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 적절한 것은?'+src('본문 ❸'),BOX(P3b)+'\n'+SUM(
 "Although the tiger's symbolic role <b>(A)</b> ________ as tigers nearly became extinct, it was <b>(B)</b> ________ when Korea chose tigers as its Olympic mascots.")+'\n'+TB(['(A)','(B)'],[
 ['strengthened','abandoned'],['strengthened','restored'],['diminished','restored'],['diminished','abandoned'],['remained','questioned']])))
qs.append(Q(17,'다음 글에서 전체 흐름과 관계 <u>없는</u> 문장은?'+src('본문 ❸ 변형'),BOX(
 "Tigers in Korea faced a decline in population due to hunting during the Joseon period and nearly went extinct during the Japanese colonial era. ① With the disappearance of tigers in Korea, their use as a symbol of the nation faded away. ② However, their symbolism was revived in modern times through their selection as the mascot for both Olympics hosted by Korea. ③ Hodori was the mascot for the Seoul Summer Olympics in 1988. ④ Mascots are often sold as dolls and souvenirs, which brings in a great deal of money for the host city. ⑤ The PyeongChang Winter Olympics in 2018 created Soohorang, a white tiger, as its mascot.")))
qs.append(Q(18,'주어진 글 다음에 이어질 글의 순서로 가장 적절한 것은?'+src('본문 ❸'),GIV("It seems that people at the time had conflicting feelings about tigers.")+'\n'+
 '    <div class="box"><p><span class="tag">(A)</span> They may have made tigers into foolish characters in order to be less scared of them.</p><p><span class="tag">(B)</span> They had respect for tigers\' power and courage.</p><p><span class="tag">(C)</span> However, they were also scared of tigers because being injured or even killed by tigers was common in the past.</p></div>\n'+ORD()))
qs.append(Q(19,'본문 ❸의 내용과 일치하는 것은?'+src('본문 ❸'),OL([
 "The 1988 mascot was modeled on a tiger species associated with bravery.",
 "Soohorang was created for the Seoul Summer Olympics.",
 "White tigers are regarded as symbols of foolishness.",
 "Tigers became completely extinct in Korea during the Joseon period.",
 "The baby in the story keeps crying even after hearing about the <i>gotgam</i>."])))
qs.append(Q(20,'본문 ❶~❸ 전체의 제목으로 가장 적절한 것은?'+src('본문 ❶~❸'),OL([
 "How Tae Keller Became an Award-Winning Writer",
 "The Tragic Extinction of Tigers in East Asia",
 "Why Tigers Are Feared More Than Any Other Animal",
 "Olympic Mascots: Symbols of Peace and Harmony",
 "The Tiger: An Enduring Presence in Korean Culture"])))
ans='④②①③⑤④②③①②⑤④⑤②①③④③①⑤'
E=["할머니가 들려주던 옛 설화에서 영감을 얻었다(that her halmoni used to tell her). 도서관 조사는 없음. ① acquaint A with B A에게 B를 알게 하다 ② be familiar with = know ③ strike a bargain = make a deal · fall ill = get sick ⑤ rekindle = revive",
 "틀린 것 (b) (e) 2개. (b) 선행사 a girl(사람) → <i>who</i> (e) used to + 동사원형 → <i>tell</i>. (d) get + 형용사 (f) 설화가 '불리는' 수동 (g) by + 동명사",
 "책을 '출판해서' 아이들이 한국 문화를 알게 됨 → <i>published</i>. conceal은 '숨기다'.",
 "'호랑이의 땅'이라 불릴 만큼 많았다 → plentiful = abundant. elusive 찾기 힘든 · revered 숭배받는 · menacing 위협적인 · domesticated 길들여진",
 "사람이 호랑이를 구해 주자 호랑이가 그를 부자가 되게 도와줌. repay one's kindness 은혜를 갚다 · prosper 번창하다 ① millennium 천 년 → 적어도 10만 년 ② 청동기 시대 바위 그림 ③ 악기에도 등장 ④ 전체 설화가 아니라 '동물 설화'의 약 40%",
 "(A) 가주어 It ~ 진주어 that절(완전한 절) (B) 사람들이 '사냥하는' 능동 → <i>hunting</i> (C) Since then(그때 이후 지금까지) → 현재완료 <i>have appeared</i>",
 "It(그것)은 청동기 시대 바위 그림(the rock art)을 가리킨다 → 바위 그림 문장 바로 뒤.",
 "depict는 '묘사하다(portray)'. conceal은 '숨기다'라서 뜻이 반대. reckon 추정하다 · showcase 보여 주다 · roughly 대략",
 "(A) 사실 동물 설화의 약 40%에 호랑이가 나옴 → (C) 호랑이는 긍정적으로도, 어리석게도 그려짐 → (B) 예를 들어(For example) 은혜 갚은 호랑이.",
 "청동기 시대 이후 전설, 미술, 악기 등 여러 분야에 계속 등장했다(Since then, tigers have appeared ...). alluding to ~을 암시하는 · unflattering 좋지 않게 그리는",
 "호랑이를 어리석은 캐릭터로 만든 이유 → 덜 무서워하기 위해(to be less scared of them). ease 덜어 주다",
 "호랑이의 힘과 용기를 존경했지만(respect) 동시에 무서워했다(scared). conflicting 상충하는 · dread 몹시 두려워하다",
 "(d) in order to + 동사원형 → <i>to be</i> (e) fade는 자동사 → 수동태 불가, 주어 their use(단수) → <i>faded</i>. (a) 지각동사 hear + O + 동사원형 (c) 동명사 주어",
 "호랑이에게 다치거나 죽는 일이 흔했기 때문에 → 무서워했다(<i>scared</i>). fond of는 '좋아하는'.",
 "호랑이는 곶감을 무서운 생물로 '잘못(mistakenly)' 생각하고 달아남. correctly는 반대. ② not unusual = common · wounded = injured ④ emblem = symbol · diminish = fade away",
 "멸종 위기로 상징성이 희미해졌다가(diminished = faded away) 올림픽 마스코트로 되살아남(restored = revived).",
 "마스코트 기념품 판매 수익 → 호랑이 상징성이 사라졌다가 되살아난 흐름과 관계없음.",
 "(B) 힘과 용기를 존경함 → (C) 그러나(However) 무서워하기도 함 → (A) 그래서 덜 무섭도록 어리석은 캐릭터로 만들었을 것.",
 "호돌이는 용기를 상징하는 시베리아 호랑이(It was a Siberian tiger, which represents courage). ② 수호랑은 평창 동계 올림픽 ③ 백호는 신성한 수호자 ④ 조선 시대엔 개체 수 감소, 일제 강점기에 거의 멸종 ⑤ 아기가 울음을 그침",
 "Keller의 책 → 한국 문화 속 오랜 호랑이의 역사와 설화 → 사라졌다가 올림픽 마스코트로 되살아난 상징 → 한국 문화에 늘 함께해 온 호랑이. enduring 오래 지속되는",
]
assert len(qs)==20 and len(ans)==20 and len(E)==20
from collections import Counter; print(Counter(ans))
key='<div class="keygrid">\n    '+''.join('<div>%d<b>%s</b></div>'%(k+1,a) for k,a in enumerate(ans[:10]))+'\n    '+''.join('<div>%d<b>%s</b></div>'%(k+11,a) for k,a in enumerate(ans[10:]))+'\n  </div>\n  <div class="exp">\n'+''.join('    <p><b>%d</b> <span class="k">%s</span> %s</p>\n'%(k+1,ans[k],e) for k,e in enumerate(E))+'  </div>'
html=('<title>저동고 능률 L3 Wrap-up</title>\n<meta name="claude:viewport-fit-sides" content="cover">\n'+fonts+css+'''

<main>
<section class="page">
  <div class="top"><span>공통영어2 NE능률(민병천) Lesson 3 · <b>본문 ❶~❸ Wrap-up</b></span><span>저동고등학교 1학년 · 2학기 기말 대비</span></div>
  <div class="title">
    <div class="g">영어</div>
    <h1>능률 L3 본문 Wrap-up<small>A Timeless Symbol of Korea · 어휘 심화</small></h1>
    <div class="when">20문항 · 각 5점<br>제한 시간 30분</div>
  </div>
  <div class="idrow"><div>반</div><div>번호</div><div>이름</div><div>점수 &nbsp;&nbsp;&nbsp; / 100</div></div>
  <p class="notice">범위: 데일리 학습 DAY 1~2 (본문 ❶❷❸). 지문은 일부 바꾼 것이 있어요. 내용 일치 문항의 선택지는 본문 표현을 어려운 어휘로 바꿔 썼으니 뜻을 정확히 따져 보세요.</p>

  <div class="qs">'''+''.join(qs)+'''  </div>
  <div class="foot"><span>NE능률(민병천) 공통영어2 Lesson 3 · 본문 ❶~❸ · 원문 일부 변형</span><span>저동고 1학년 영어 · Wrap-up</span></div>
</section>

<section class="page">
  <div class="top"><span>능률 L3 본문 Wrap-up · <b>정답과 해설</b></span><span>저동고등학교 1학년</span></div>
  <div class="title"><div class="g">영어</div><h1>정답과 해설</h1><div class="when">각 5점 · 100점</div></div>
  '''+key+'''
  <div class="foot"><span>정답 분포 ①~⑤ 각 4개</span><span>저동고 1학년 영어 · Wrap-up</span></div>
</section>
</main>
''')
open('wrapup-jeodong-ne-L3.html','w',encoding='utf-8').write(html)
