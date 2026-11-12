# 11/12 저동고1 능률(민) L4 본문 ❶~❺ Wrap-up 1차 (build_jd.py 형식 그대로)
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

U=lambda t,w: '<span class="tag">(%s)</span><u>%s</u>'%(t,w)
C=lambda n,w: '%s<u>%s</u>'%('①②③④⑤'[n-1],w)
P1=("Our environment is in trouble. With the planet becoming warmer, sea levels are rising and natural disasters such as forest fires and floods are increasing. More and more waste is also being produced. Plastic, in particular, is causing problems with soil and water pollution. It is clear that humans are a major contributor to the destruction of nature. Will we be able to protect the environment from mountains of plastic? Can we stop climate change from reaching dangerous levels? Achieving these goals seems difficult. Nature, however, may have provided us with solutions to these problems. Here are three areas where changes are already happening.")
qs=[]
qs.append(Q(1,'다음 글의 내용과 일치하지 <u>않는</u> 것은?'+src('본문 ❶'),BOX(P1)+'\n'+OL([
 "The rise in global temperatures is linked to higher sea levels.",
 "The quantity of waste being generated keeps growing.",
 "Humans play only a minor role in damaging the natural world.",
 "Plastic contributes to the contamination of both land and water.",
 "Nature might already offer answers to our environmental problems."])))
qs.append(Q(2,'다음 글의 밑줄 친 (a)~(g) 중 어법상 <u>틀린</u> 것의 개수는?'+src('본문 ❶ 변형'),BOX(
 "Our environment is in trouble. With the planet "+U('a','becoming')+" warmer, sea levels "+U('b','is rising')+" and natural disasters such as forest fires and floods are increasing. More and more waste is also "+U('c','producing')+". Plastic, in particular, "+U('d','are causing')+" problems with soil and water pollution. It is clear "+U('e','what')+" humans are a major contributor to the destruction of nature. Can we stop climate change from "+U('f','reaching')+" dangerous levels? Achieving these goals "+U('g','seem')+" difficult.")+'\n'+OL(['1개','2개','3개','4개','5개'],False)))
qs.append(Q(3,'다음 글의 밑줄 친 부분 중, 문맥상 낱말의 쓰임이 적절하지 <u>않은</u> 것은?'+src('본문 ❶ 변형'),BOX(
 "Our environment is in trouble. With the planet becoming warmer, sea levels are "+C(1,'rising')+" and natural disasters such as forest fires and floods are "+C(2,'decreasing')+". More and more waste is also being produced. It is clear that humans are a major "+C(3,'contributor')+" to the destruction of nature. Achieving these goals seems "+C(4,'difficult')+". Nature, however, may have provided us with "+C(5,'solutions')+" to these problems.")))
qs.append(Q(4,'다음 빈칸에 들어갈 말로 가장 적절한 것은?'+src('본문 ❷'),BOX(
 "With this in mind, scientists are turning to mealworms. Mealworms are the larvae of a certain species of beetle. Special bacteria live inside them. These bacteria can <span class=\"blank\"></span> plastic. This means that mealworms can actually feed on plastic.")+'\n'+OL(['give off','pile up','make up','break down','turn down'])))
P2=("About fifty percent of plastic is produced for single-use products. That means the items are used just once and then discarded. Do you ever stop to think about where these plastic items go after you throw them away? Recycling can help reduce the amount of plastic in our landfills. However, less than ten percent of the world's plastic waste has been recycled so far. Often, plastic waste is moved to places where it is just dumped or burned. Furthermore, between 8 and 14 million metric tons of plastic end up in the ocean every year. This puts many marine species in danger. With this in mind, scientists are turning to mealworms. Mealworms are the larvae of a certain species of beetle. Special bacteria live inside them. These bacteria can break down plastic. This means that mealworms can actually feed on plastic. Scientists are now looking for ways to cultivate the bacteria outside of mealworms. They also want to speed up the process by which the bacteria break down plastic.")
qs.append(Q(5,'다음 글의 내용과 일치하는 것은?'+src('본문 ❷'),BOX(P2)+'\n'+OL([
 "Roughly half of all plastic is manufactured for disposable items.",
 "Most of the world's plastic waste has already been recycled.",
 "Less than one million tons of plastic flow into the ocean each year.",
 "Mealworms are the fully grown adult form of a beetle.",
 "Scientists have already mass-produced the bacteria outside mealworms."])))
qs.append(Q(6,'(A), (B), (C)의 각 네모 안에서 어법에 맞는 표현으로 가장 적절한 것은?'+src('본문 ❷'),BOX(
 "That means the items are used just once and then <b>(A)</b> [discarded / discarding]. ... Often, plastic waste is moved to places <b>(B)</b> [where / which] it is just dumped or burned. ... They also want to speed up the process <b>(C)</b> [by which / which] the bacteria break down plastic.")+'\n'+TB(['(A)','(B)','(C)'],[
 ['discarding','where','by which'],['discarded','where','by which'],['discarded','which','by which'],['discarded','where','which'],['discarding','which','which']])))
qs.append(Q(7,'글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳은?'+src('본문 ❷'),GIV("Special bacteria live inside them.")+'\n'+BOX(
 "Furthermore, between 8 and 14 million metric tons of plastic end up in the ocean every year. ( ① ) This puts many marine species in danger. ( ② ) With this in mind, scientists are turning to mealworms. ( ③ ) Mealworms are the larvae of a certain species of beetle. ( ④ ) These bacteria can break down plastic. ( ⑤ ) This means that mealworms can actually feed on plastic.")))
qs.append(Q(8,'주어진 글 다음에 이어질 글의 순서로 가장 적절한 것은?'+src('본문 ❷'),GIV("About fifty percent of plastic is produced for single-use products.")+'\n'+
 '    <div class="box"><p><span class="tag">(A)</span> Often, plastic waste is moved to places where it is just dumped or burned. Furthermore, between 8 and 14 million metric tons of plastic end up in the ocean every year.</p><p><span class="tag">(B)</span> That means the items are used just once and then discarded. Do you ever stop to think about where these plastic items go after you throw them away?</p><p><span class="tag">(C)</span> Recycling can help reduce the amount of plastic in our landfills. However, less than ten percent of the world\'s plastic waste has been recycled so far.</p></div>\n'+ORD()))
qs.append(Q(9,'다음 빈칸에 들어갈 말로 가장 적절한 것은?'+src('본문 ❸'),BOX(
 "Mining and other industries are causing soil pollution across the globe. Although polluted soil can be dug up and transported to a landfill, this process is expensive. Moreover, it only moves the problem to another area and does not really solve it. Fortunately, there is an eco-friendly and <span class=\"blank\"></span> way to restore polluted soil — planting willow trees.")+'\n'+OL(['costly','temporary','complicated','dangerous','cost-effective'])))
P3=("Mining and other industries are causing soil pollution across the globe. Although polluted soil can be dug up and transported to a landfill, this process is expensive. Moreover, it only moves the problem to another area and does not really solve it. Fortunately, there is an eco-friendly and cost-effective way to restore polluted soil — planting willow trees. These amazing trees have extensive and well-developed root systems. As a result, they naturally extract a wide range of harmful materials from the soil. They can also grow quickly, even in soil with a high acidity level or a lot of heavy metals in it. Research on the effectiveness of using willow trees for this purpose is in development. Scientists have found that some species of willow trees are able to absorb harmful materials better than others. Therefore, this promising area should be further explored to find out which trees are the most effective.")
qs.append(Q(10,'다음 글의 내용과 일치하지 <u>않는</u> 것은?'+src('본문 ❸'),BOX(P3)+'\n'+OL([
 "Moving polluted soil to a landfill is a cheap and permanent solution.",
 "Mining is one of the causes of soil contamination worldwide.",
 "Willow trees possess wide and well-developed roots.",
 "Willows can grow rapidly even in highly acidic soil.",
 "Some willow species absorb harmful substances more effectively than others."])))
qs.append(Q(11,'다음 글의 밑줄 친 (a)~(e) 중 어법상 <u>틀린</u> 것끼리 짝지은 것은?'+src('본문 ❸ 변형'),BOX(
 "Although polluted soil can "+U('a','be dug up')+" and transported to a landfill, this process is expensive. Moreover, it only moves the problem to another area and does not really "+U('b','solve')+" it. ... These amazing trees have extensive and well-developed root systems. As a result, they naturally "+U('c','extracts')+" a wide range of harmful materials from the soil. They can also grow "+U('d','quickly')+", even in soil with a high acidity level. ... Scientists have found that some species of willow trees are able to absorb harmful materials better than "+U('e','another')+".")+'\n'+OL(['(a), (c)','(b), (d)','(a), (e)','(c), (e)','(d), (e)'],False)))
qs.append(Q(12,'다음 글에서 전체 흐름과 관계 <u>없는</u> 문장은?'+src('본문 ❸ 변형'),BOX(
 "Fortunately, there is an eco-friendly and cost-effective way to restore polluted soil — planting willow trees. ① These amazing trees have extensive and well-developed root systems. ② Willow branches have long been used to make baskets and furniture. ③ As a result, they naturally extract a wide range of harmful materials from the soil. ④ They can also grow quickly, even in soil with a high acidity level or a lot of heavy metals in it. ⑤ Research on the effectiveness of using willow trees for this purpose is in development.")))
qs.append(Q(13,'다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 적절한 것은?'+src('본문 ❸'),BOX(P3)+'\n'+SUM(
 "Willow trees offer a(n) <b>(A)</b> ________ way to clean polluted soil, but further <b>(B)</b> ________ is needed to identify the most effective species.")+'\n'+TB(['(A)','(B)'],[
 ['affordable','research'],['expensive','research'],['affordable','funding'],['temporary','testing'],['harmful','planting']])))
P4=("Statistics show that about thirty to forty percent of people in the world drink coffee each day. The coffee-making process, however, generates used coffee grounds, which are normally sent to landfills. There, they can create a harmful greenhouse gas. Unfortunately, there's no way to stop everyone in the world from drinking coffee. However, we can reduce greenhouse gas emissions by turning used coffee grounds into biofuel. Biofuel is a natural fuel that is made from plant or animal sources. Researchers have found that they can grow algae on old coffee grounds without adding any other nutrients. If these algae are exposed to twenty hours of light and four hours of darkness each day, they eventually produce high-quality biofuel. The biofuel is renewable and sustainable, and it creates only a small amount of emissions.")
qs.append(Q(14,'다음 글의 내용과 일치하는 것은?'+src('본문 ❹'),BOX(P4)+'\n'+OL([
 "Less than a fifth of the world's population drinks coffee daily.",
 "Used coffee grounds are usually recycled into fertilizer.",
 "Coffee grounds in landfills can release a harmful greenhouse gas.",
 "Algae need extra nutrients to grow on coffee grounds.",
 "The algae produce biofuel only when kept in constant light."])))
qs.append(Q(15,'주어진 글 다음에 이어질 글의 순서로 가장 적절한 것은?'+src('본문 ❹'),GIV("Statistics show that about thirty to forty percent of people in the world drink coffee each day.")+'\n'+
 '    <div class="box"><p><span class="tag">(A)</span> Biofuel is a natural fuel that is made from plant or animal sources. Researchers have found that they can grow algae on old coffee grounds without adding any other nutrients.</p><p><span class="tag">(B)</span> Unfortunately, there\'s no way to stop everyone in the world from drinking coffee. However, we can reduce greenhouse gas emissions by turning used coffee grounds into biofuel.</p><p><span class="tag">(C)</span> The coffee-making process, however, generates used coffee grounds, which are normally sent to landfills. There, they can create a harmful greenhouse gas.</p></div>\n'+ORD()))
qs.append(Q(16,'다음 글의 밑줄 친 부분 중, 문맥상 낱말의 쓰임이 적절하지 <u>않은</u> 것은?'+src('본문 ❹ 변형'),BOX(
 "The coffee-making process, however, "+C(1,'generates')+" used coffee grounds, which are normally sent to landfills. There, they can create a "+C(2,'harmful')+" greenhouse gas. Unfortunately, there's no way to stop everyone in the world from drinking coffee. However, we can "+C(3,'increase')+" greenhouse gas emissions by turning used coffee grounds into biofuel. Researchers have found that they can grow algae on old coffee grounds "+C(4,'without')+" adding any other nutrients. The biofuel is "+C(5,'renewable')+" and sustainable, and it creates only a small amount of emissions.")))
qs.append(Q(17,'글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳은?'+src('본문 ❹'),GIV("There, they can create a harmful greenhouse gas.")+'\n'+BOX(
 "The coffee-making process, however, generates used coffee grounds, which are normally sent to landfills. ( ① ) Unfortunately, there's no way to stop everyone in the world from drinking coffee. ( ② ) However, we can reduce greenhouse gas emissions by turning used coffee grounds into biofuel. ( ③ ) Biofuel is a natural fuel that is made from plant or animal sources. ( ④ ) Researchers have found that they can grow algae on old coffee grounds without adding any other nutrients. ( ⑤ ) If these algae are exposed to twenty hours of light and four hours of darkness each day, they eventually produce high-quality biofuel.")))
qs.append(Q(18,'밑줄 친 <u>Mother Nature has given us one more chance</u>가 의미하는 바로 가장 적절한 것은?'+src('본문 ❺'),BOX(
 "These are just a few solutions we can find in nature. There could be many more possible solutions to the problems we currently face. It seems that <u>Mother Nature has given us one more chance</u>. In return, we need to look for more ways to keep the environment healthy and clean. If we do, the future of our planet may be bright after all.")+'\n'+OL([
 "Nature will solve every environmental problem by itself.",
 "Humans no longer need to worry about the environment.",
 "Natural disasters will soon stop happening.",
 "We should return to a life without any technology.",
 "Nature's solutions give us an opportunity to repair the damage we have caused."])))
qs.append(Q(19,'다음 빈칸에 들어갈 말로 가장 적절한 것은?'+src('본문 ❺'),BOX(
 "These are just a few solutions we can find in nature. There could be many more possible solutions to the problems we currently face. It seems that Mother Nature has given us one more chance. In return, we need to <span class=\"blank\"></span>. If we do, the future of our planet may be bright after all.")+'\n'+OL([
 "stop using natural resources altogether","wait for nature to recover on its own","rely only on recycling programs",
 "actively seek further ways to protect the environment","focus on protecting the oceans alone"])))
qs.append(Q(20,'다음 글의 제목으로 가장 적절한 것은?'+src('본문 ❶·❺'),BOX(P1+' ... '+"These are just a few solutions we can find in nature. There could be many more possible solutions to the problems we currently face. It seems that Mother Nature has given us one more chance. In return, we need to look for more ways to keep the environment healthy and clean.")+'\n'+OL([
 "The Dangers of Drinking Too Much Coffee","Nature-Inspired Solutions to Environmental Problems","Why Recycling Is the Only Answer",
 "The Life Cycle of Beetles","How Willow Trees Became Popular in Gardens"])))
ans='③⑤②④①②④③⑤①④②①③⑤③①⑤④②'
E=["인간이 자연 파괴의 주된 원인(a major contributor)이라고 했으므로 '작은 역할(a minor role)'은 불일치. ① rise in global temperatures = the planet becoming warmer ② quantity = amount · generate = produce ④ contamination = pollution ⑤ offer answers = provide solutions",
 "틀린 것 (b) (c) (d) (e) (g) 5개. (b) 주어 sea levels(복수) → <i>are rising</i> (c) 쓰레기가 '만들어지는' 수동 진행 → <i>being produced</i> (d) 주어 Plastic(단수) → <i>is causing</i> (e) 가주어 It ~ 진주어 that절(완전한 절) → <i>that</i> (g) 동명사 주어 Achieving은 단수 → <i>seems</i>. (a) with + 명사 + 분사(지구가 '따뜻해지는' 능동) (f) stop A from -ing",
 "산불·홍수 같은 자연재해가 '늘고 있다' → <i>increasing</i>. decreasing은 반대.",
 "박테리아가 플라스틱을 '분해할' 수 있어서 밀웜이 플라스틱을 먹고 살 수 있다 → break down. give off 내뿜다 · pile up 쌓이다 · make up 구성하다 · turn down 거절하다",
 "About fifty percent ~ single-use products → roughly half · disposable = single-use. ② 10% 미만만 재활용 ③ 800만~1,400만 톤 ④ larvae 애벌레 ⑤ 밖에서 기르는 방법을 '찾는 중'",
 "(A) 물건이 '버려지는' 수동, used와 병렬 → <i>discarded</i> (B) 뒤가 완전한 절(it is just dumped) → 관계부사 <i>where</i> (C) 뒤가 완전한 절 + by the process → <i>by which</i>",
 "주어진 문장의 them = mealworms, 다음 문장의 These bacteria가 주어진 문장의 Special bacteria를 받음 → ④",
 "(B) That means(일회용이라는 것은) 한 번 쓰고 버려짐·버린 뒤 어디로 가는지 → (C) 재활용이 도움이 되지만 10% 미만 → (A) 종종 그냥 버려지거나 태워지고, 게다가(Furthermore) 바다로",
 "흙을 파서 옮기는 방법은 비싸고 문제를 옮길 뿐 → Fortunately 뒤에는 '친환경적이고 비용 효율적인' 방법 → cost-effective",
 "흙을 옮기는 방법은 비싸고(expensive) 문제를 다른 곳으로 옮길 뿐(only moves the problem)이라 '싸고 영구적인 해결책'은 불일치. ② contamination = pollution ③ possess = have ④ rapidly = quickly ⑤ substances = materials",
 "(c) 주어 they(복수) → <i>extract</i> (e) 다른 종들'과' 비교 → <i>others</i>. (a) 흙이 '파내지는' 수동 (b) does not + 동사원형 (d) 동사 grow를 꾸미는 부사",
 "버드나무가 오염된 흙을 정화한다는 흐름 → 버드나무 가지로 바구니·가구를 만든다는 ②는 관계없음. ③ As a result는 ①의 뿌리 이야기와 이어짐",
 "비용 효율적인(cost-effective = affordable) 방법이고, 어떤 나무가 가장 효과적인지 더 연구(further explored = research)해야 함. funding(자금)은 언급 없음",
 "매립지로 간 커피 찌꺼기는 해로운 온실가스를 만들 수 있다(There, they can create a harmful greenhouse gas). ① 30~40% ② 보통 매립지로 감 ④ 다른 영양분 없이 ⑤ 빛 20시간 + 어둠 4시간",
 "(C) 그러나(however) 커피를 만들면 찌꺼기가 생기고 매립지에서 온실가스 → (B) 커피를 끊게 할 수는 없지만 바이오 연료로 바꿔 배출을 줄일 수 있음 → (A) 바이오 연료란·커피 찌꺼기에 조류를 기름",
 "바이오 연료로 바꾸면 온실가스 배출을 '줄일' 수 있다 → <i>reduce</i>. increase는 반대.",
 "There = landfills(매립지), they = used coffee grounds → 매립지로 보내진다는 문장 바로 뒤 ①",
 "자연이 해결책을 보여 주어 우리가 망친 환경을 되돌릴 기회를 한 번 더 준 것 같다는 뜻. 그 대가로(In return) 우리도 방법을 더 찾아야 함 → ①~④는 지나친 해석",
 "자연이 기회를 주었으니 그 대가로 우리는 환경을 건강하고 깨끗하게 지킬 방법을 더 찾아야 한다(look for more ways to keep the environment healthy and clean) → actively seek further ways",
 "환경 문제 → 자연이 준 해결책(밀웜·버드나무·조류) → 더 많은 해결책을 찾자 = 자연에서 얻은 환경 문제 해결책",
]
assert len(qs)==20 and len(ans)==20 and len(E)==20
from collections import Counter; print(Counter(ans))
key='<div class="keygrid">\n    '+''.join('<div>%d<b>%s</b></div>'%(k+1,a) for k,a in enumerate(ans[:10]))+'\n    '+''.join('<div>%d<b>%s</b></div>'%(k+11,a) for k,a in enumerate(ans[10:]))+'\n  </div>\n  <div class="exp">\n'+''.join('    <p><b>%d</b> <span class="k">%s</span> %s</p>\n'%(k+1,ans[k],e) for k,e in enumerate(E))+'  </div>'
html=('<title>저동고 능률 L4 Wrap-up</title>\n<meta name="claude:viewport-fit-sides" content="cover">\n'+fonts+css+'''

<main>
<section class="page">
  <div class="top"><span>공통영어2 NE능률(민병천) Lesson 4 · <b>본문 ❶~❺ Wrap-up</b></span><span>저동고등학교 1학년 · 2학기 기말 대비</span></div>
  <div class="title">
    <div class="g">영어</div>
    <h1>능률 L4 본문 Wrap-up<small>Looking to Nature for Help · 어휘 심화</small></h1>
    <div class="when">20문항 · 각 5점<br>제한 시간 30분</div>
  </div>
  <div class="idrow"><div>반</div><div>번호</div><div>이름</div><div>점수 &nbsp;&nbsp;&nbsp; / 100</div></div>
  <p class="notice">범위: 데일리 학습 DAY 7~9 (4과 본문 ❶~❺). 지문은 일부 바꾼 것이 있어요. 내용 일치 문항의 선택지는 본문 표현을 어려운 어휘로 바꿔 썼으니 뜻을 정확히 따져 보세요.</p>

  <div class="qs">'''+''.join(qs)+'''  </div>
  <div class="foot"><span>NE능률(민병천) 공통영어2 Lesson 4 · 본문 ❶~❺ · 원문 일부 변형</span><span>저동고 1학년 영어 · Wrap-up</span></div>
</section>

<section class="page">
  <div class="top"><span>능률 L4 본문 Wrap-up · <b>정답과 해설</b></span><span>저동고등학교 1학년</span></div>
  <div class="title"><div class="g">영어</div><h1>정답과 해설</h1><div class="when">각 5점 · 100점</div></div>
  '''+key+'''
  <div class="foot"><span>정답 분포 ①~⑤ 각 4개</span><span>저동고 1학년 영어 · Wrap-up</span></div>
</section>
</main>
''')
open('wrapup-jeodong-ne-L4.html','w',encoding='utf-8').write(html)
