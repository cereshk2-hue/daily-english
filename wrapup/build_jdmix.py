# 11/12 저동고1 능률(민) 3·4과 통합 Wrap-up 1차(중) · 2차(상·어휘 비틀기) — build_jd.py 형식
import re
from collections import Counter
src0 = open('build_jd.py', encoding='utf-8').read()
exec(src0[:src0.index("T='<i>When You Trap a Tiger</i>'")])
T = '<i>When You Trap a Tiger</i>'
U = lambda t, w: '<span class="tag">(%s)</span><u>%s</u>' % (t, w)
C = lambda n, w: '%s<u>%s</u>' % ('①②③④⑤'[n - 1], w)
GP = lambda n: ' ( %s ) ' % '①②③④⑤'[n - 1]
BL = '<span class="blank"></span>'
# ── 본문 ──
L31 = ["Children around the world learned a bit more about Korean culture when writer Tae Keller published her book " + T + " in 2020.", "Its story starts with a girl who meets a tiger.", "Her grandmother knows the tiger as well.", "When her grandmother gets sick, the girl makes a deal with the tiger.", "Keller's inspiration for her award-winning book was an old folktale that her <i>halmoni</i> (grandmother) used to tell her.", "It is called \"The Sun and the Moon,\" and it is about a brother, a sister, and a tiger.", "Keller wanted to revive the public's interest in tigers by writing her own book."]
L32 = ["Long ago, tigers were so abundant in Korea that people often called the country the \"Land of Tigers.\"", "It is estimated that tigers lived in Korea for at least 100,000 years.", "The first appearance of a tiger in Korean culture dates back to the rock art of the Bronze Age.", "It depicts people hunting various animals, including tigers.", "Since then, tigers have appeared in many aspects of Korean culture, from legends to art and musical instruments.", "Some of you may have heard Korean folktales featuring tigers.", "In fact, approximately forty percent of Korean folktales about animals include a tiger.", "Tigers in Korean folktales are sometimes shown in a positive light and sometimes as foolish creatures.", "For example, in one story, a tiger helps a human become rich after the human saves the tiger's life."]
L33 = ["In another story, a tiger hears a mother tell her crying baby, \"Don't cry. Here's a <i>gotgam</i>.\"", "Because the baby stops crying, the tiger mistakenly thinks the <i>gotgam</i> is a very scary creature and runs away.", "It seems that people at the time had conflicting feelings about tigers.", "They had respect for tigers' power and courage.", "However, they were also scared of tigers because being injured or even killed by tigers was common in the past.", "They may have made tigers into foolish characters in order to be less scared of them.", "Tigers in Korea faced a decline in population due to hunting during the Joseon period and nearly went extinct during the Japanese colonial era.", "With the disappearance of tigers in Korea, their use as a symbol of the nation faded away.", "However, their symbolism was revived in modern times through their selection as the mascot for both Olympics hosted by Korea.", "Hodori was the mascot for the Seoul Summer Olympics in 1988.", "It was a Siberian tiger, which represents courage.", "The PyeongChang Winter Olympics in 2018 created Soohorang, a white tiger, as its mascot.", "White tigers are considered sacred guardians."]
L34 = ["Tigers are also mentioned in the K-pop song \"Tiger is Coming.\"", "One verse of the song is a reinterpreted version of \"Sugungga,\" which is a traditional Korean song.", "The song drew worldwide attention, and its video was viewed millions of times online."]
L35 = ["These days, only a few wild tigers have been reported to be living in North Korea.", "However, the history, stories, and cultural meaning of tigers still have a place among modern Korean people.", "Who can deny that the tiger is a symbol of Korea?", "In 2021, the National Folk Museum of Korea published a book that collects all the stories about tigers in Korea.", "How about looking for tigers around you now?"]
M1 = ["Our environment is in trouble.", "With the planet becoming warmer, sea levels are rising and natural disasters such as forest fires and floods are increasing.", "More and more waste is also being produced.", "Plastic, in particular, is causing problems with soil and water pollution.", "It is clear that humans are a major contributor to the destruction of nature.", "Will we be able to protect the environment from mountains of plastic?", "Can we stop climate change from reaching dangerous levels?", "Achieving these goals seems difficult.", "Nature, however, may have provided us with solutions to these problems.", "Here are three areas where changes are already happening."]
M2 = ["About fifty percent of plastic is produced for single-use products.", "That means the items are used just once and then discarded.", "Do you ever stop to think about where these plastic items go after you throw them away?", "Recycling can help reduce the amount of plastic in our landfills.", "However, less than ten percent of the world's plastic waste has been recycled so far.", "Often, plastic waste is moved to places where it is just dumped or burned.", "Furthermore, between 8 and 14 million metric tons of plastic end up in the ocean every year.", "This puts many marine species in danger.", "With this in mind, scientists are turning to mealworms.", "Mealworms are the larvae of a certain species of beetle.", "Special bacteria live inside them.", "These bacteria can break down plastic.", "This means that mealworms can actually feed on plastic.", "Scientists are now looking for ways to cultivate the bacteria outside of mealworms.", "They also want to speed up the process by which the bacteria break down plastic.", "This may help us keep our landfills plastic-free."]
M3 = ["Mining and other industries are causing soil pollution across the globe.", "Although polluted soil can be dug up and transported to a landfill, this process is expensive.", "Moreover, it only moves the problem to another area and does not really solve it.", "Fortunately, there is an eco-friendly and cost-effective way to restore polluted soil — planting willow trees.", "These amazing trees have extensive and well-developed root systems.", "As a result, they naturally extract a wide range of harmful materials from the soil.", "They can also grow quickly, even in soil with a high acidity level or a lot of heavy metals in it.", "Research on the effectiveness of using willow trees for this purpose is in development.", "Scientists have found that some species of willow trees are able to absorb harmful materials better than others.", "Therefore, this promising area should be further explored to find out which trees are the most effective.", "In time, we may be able to clean up our land with willow trees."]
M4 = ["Statistics show that about thirty to forty percent of people in the world drink coffee each day.", "The coffee-making process, however, generates used coffee grounds, which are normally sent to landfills.", "There, they can create a harmful greenhouse gas.", "Unfortunately, there's no way to stop everyone in the world from drinking coffee.", "However, we can reduce greenhouse gas emissions by turning used coffee grounds into biofuel.", "Biofuel is a natural fuel that is made from plant or animal sources.", "Researchers have found that they can grow algae on old coffee grounds without adding any other nutrients.", "If these algae are exposed to twenty hours of light and four hours of darkness each day, they eventually produce high-quality biofuel.", "The biofuel is renewable and sustainable, and it creates only a small amount of emissions."]
M5 = ["These are just a few solutions we can find in nature.", "There could be many more possible solutions to the problems we currently face.", "It seems that Mother Nature has given us one more chance.", "In return, we need to look for more ways to keep the environment healthy and clean.", "If we do, the future of our planet may be bright after all."]
J = lambda L, a=0, b=None: ' '.join(L[a:b])
def INS(L, gi, a, b):
    """L[a:b] 지문에서 L[gi]를 빼고 첫 문장 뒤부터 ( ① )~( ⑤ ) → (주어진 문장, 지문, 정답 번호)"""
    rest = [x for i, x in enumerate(L[a:b], a) if i != gi]
    assert len(rest) in (5, 6), len(rest)
    body = rest[0] + ''.join(GP(k + 1) + (rest[k + 1] if k + 1 < len(rest) else '') for k in range(5))
    return GIV(L[gi]), BOX(body), gi - a
def ABCQ(n, stem, given, chunks, seq):
    lab = dict(zip(seq, chunks))
    box = '    <div class="box">' + ''.join('<p><span class="tag">(%s)</span> %s</p>' % (L, lab[L]) for L in 'ABC') + '</div>'
    ans = ['(A) − (C) − (B)', '(B) − (A) − (C)', '(B) − (C) − (A)', '(C) − (A) − (B)', '(C) − (B) − (A)'].index(' − '.join('(%s)' % L for L in seq)) + 1
    return Q(n, stem, GIV(given) + '\n' + box + '\n' + ORD()), ans

def page(fn, title, h1, small, notice, qs, ans, E, lv):
    assert len(qs) == 20 and len(ans) == 20 and len(E) == 20, (len(qs), len(ans), len(E))
    print(fn, ans, Counter(ans))
    key = '<div class="keygrid">\n    ' + ''.join('<div>%d<b>%s</b></div>' % (k + 1, a) for k, a in enumerate(ans[:10])) + '\n    ' + ''.join('<div>%d<b>%s</b></div>' % (k + 11, a) for k, a in enumerate(ans[10:])) + '\n  </div>\n  <div class="exp">\n' + ''.join('    <p><b>%d</b> <span class="k">%s</span> %s</p>\n' % (k + 1, ans[k], e) for k, e in enumerate(E)) + '  </div>'
    html = ('<title>%s</title>\n<meta name="claude:viewport-fit-sides" content="cover">\n' % title + fonts + css + '''

<main>
<section class="page">
  <div class="top"><span>공통영어2 NE능률(민병천) Lesson 3·4 · <b>통합 Wrap-up %s</b></span><span>저동고등학교 1학년 · 2학기 기말 대비</span></div>
  <div class="title">
    <div class="g">영어</div>
    <h1>%s<small>%s</small></h1>
    <div class="when">20문항 · 각 5점<br>제한 시간 30분</div>
  </div>
  <div class="idrow"><div>반</div><div>번호</div><div>이름</div><div>점수 &nbsp;&nbsp;&nbsp; / 100</div></div>
  <p class="notice">%s</p>

  <div class="qs">''' % (lv, h1, small, notice) + ''.join(qs) + '''  </div>
  <div class="foot"><span>NE능률(민병천) 공통영어2 Lesson 3·4 · 원문 일부 변형</span><span>저동고 1학년 영어 · 통합 Wrap-up</span></div>
</section>

<section class="page">
  <div class="top"><span>능률 3·4과 통합 Wrap-up %s · <b>정답과 해설</b></span><span>저동고등학교 1학년</span></div>
  <div class="title"><div class="g">영어</div><h1>정답과 해설</h1><div class="when">각 5점 · 100점</div></div>
  ''' % lv + key + '''
  <div class="foot"><span>정답 분포 ①~⑤ 각 4개</span><span>저동고 1학년 영어 · 통합 Wrap-up</span></div>
</section>
</main>
''')
    assert Counter(ans) == Counter({c: 4 for c in '①②③④⑤'}), Counter(ans)
    open(fn, 'w', encoding='utf-8').write(html)

# ═════════════ 1차 (중) ═════════════
qs = []; E = []; A = ''
def add(q, a, e):
    global A; qs.append(q); A += '①②③④⑤'[a - 1]; E.append(e)
add(Q(1, '다음 글의 내용과 일치하지 <u>않는</u> 것은?' + src('3과 본문 ❶'), BOX(J(L31)) + '\n' + OL([
 "Keller's novel introduced young readers around the globe to Korean culture.",
 "In the story, the girl's grandmother is already acquainted with the tiger.",
 "The girl makes a deal with the tiger after her grandmother recovers.",
 "A folktale that Keller's grandmother used to tell inspired the book.",
 "Keller hoped her book would renew public interest in tigers."])), 3,
 "할머니가 '아플 때'(When her grandmother gets sick) 호랑이와 거래를 한다 → '회복한 뒤(after ~ recovers)'는 불일치. ① introduce A to B = A에게 B를 소개하다 ② be acquainted with = know ④ inspire 영감을 주다 ⑤ renew = revive")
add(Q(2, '다음 빈칸에 들어갈 말로 가장 적절한 것은?' + src('3과 본문 ❷'), BOX(J(L32, 0, 2) + " The first appearance of a tiger in Korean culture " + BL + " the rock art of the Bronze Age. " + J(L32, 3, 5)) + '\n' + OL(['dates back to', 'gives way to', 'makes up for', 'looks down on', 'runs out of'])), 1,
 "호랑이가 한국 문화에 처음 나타난 것은 청동기 시대 바위 그림으로 '거슬러 올라간다' → dates back to. give way to ~에 자리를 내주다 · make up for 만회하다 · look down on 깔보다 · run out of ~이 바닥나다")
q, a = ABCQ(3, '주어진 글 다음에 이어질 글의 순서로 가장 적절한 것은?' + src('3과 본문 ❸'), L33[0], [L33[1], J(L33, 2, 4), J(L33, 4, 6)], 'CAB')
add(q, a, "엄마가 곶감 이야기를 함 → (C) 아기가 울음을 그치자 호랑이가 곶감을 무서운 존재로 착각하고 달아남 → (A) 당시 사람들은 호랑이에 대해 상반된 감정·힘과 용기를 존경 → (B) 그러나(However) 두려워하기도 해서 어리석은 캐릭터로 만들었을 것")
g, b, a = INS(L33, 10, 5, 12)
add(Q(4, '글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳은?' + src('3과 본문 ❸'), g + '\n' + b), a,
 "주어진 문장의 It = Hodori, a Siberian tiger. 호돌이가 1988년 서울 하계 올림픽 마스코트였다는 문장 바로 뒤 → ⑤. 이어서 평창 올림픽의 수호랑(백호) 이야기로 넘어감")
add(Q(5, '다음 글의 내용과 일치하는 것은?' + src('3과 본문 ❹'), BOX(J(L34)) + '\n' + OL([
 "\"Tiger is Coming\" is a traditional Korean song from the Joseon period.",
 "Part of the K-pop song reworks a traditional Korean song.",
 "The song's video was rarely watched outside Korea.",
 "\"Sugungga\" was originally written as a K-pop song.",
 "The song does not mention tigers at all."])), 2,
 "One verse ~ is a reinterpreted version of \"Sugungga\" = 노래의 일부가 전통 노래를 새롭게 바꿨다(rework). ① K-pop 노래 ③ 전 세계의 관심, 수백만 번 조회 ④ 수궁가는 전통 노래 ⑤ 호랑이가 나오는 노래")
add(Q(6, '밑줄 친 <u>Who can deny that the tiger is a symbol of Korea?</u>가 의미하는 바로 가장 적절한 것은?' + src('3과 본문 ❺'), BOX(J(L35).replace('Who can deny that the tiger is a symbol of Korea?', '<u>Who can deny that the tiger is a symbol of Korea?</u>')) + '\n' + OL([
 '호랑이가 한국의 상징이라는 데 의문을 갖는 사람이 많다.', '호랑이 대신 새로운 상징을 찾아야 한다.', '야생 호랑이가 거의 없으니 상징이 될 수 없다.', '호랑이는 누구도 부인할 수 없는 한국의 상징이다.', '북한에 사는 호랑이만이 한국의 상징이다.'], False)), 4,
 "'누가 부인할 수 있겠는가?'는 '아무도 부인할 수 없다'는 뜻의 수사의문문. 야생 호랑이는 거의 없어도 역사·이야기·문화적 의미는 여전히 남아 있다는 앞 문장과 이어짐")
add(Q(7, '다음 글의 밑줄 친 부분 중, 문맥상 낱말의 쓰임이 적절하지 <u>않은</u> 것은?' + src('3과 본문 ❷❸ 변형'), BOX(
 "Long ago, tigers were so " + C(1, 'scarce') + " in Korea that people often called the country the \"Land of Tigers.\" Tigers in Korean folktales are sometimes shown in a " + C(2, 'positive') + " light and sometimes as " + C(3, 'foolish') + " creatures. It seems that people at the time had " + C(4, 'conflicting') + " feelings about tigers. Tigers in Korea faced a " + C(5, 'decline') + " in population due to hunting during the Joseon period.")), 1,
 "'호랑이의 땅'이라 불릴 만큼 호랑이가 '많았다' → <i>abundant</i>. scarce(부족한)는 반대. ② 긍정적으로 ③ 어리석게 ④ 상반된 감정 ⑤ 개체 수 감소")
add(Q(8, '다음 글의 밑줄 친 부분 중, 어법상 <u>틀린</u> 것은?' + src('3과 본문 ❷❸ 변형'), BOX(
 "It " + C(1, 'depicts') + " people hunting various animals, including tigers. Since then, tigers " + C(2, 'have appeared') + " in many aspects of Korean culture. Because the baby stops crying, the tiger mistakenly thinks the <i>gotgam</i> " + C(3, 'being') + " a very scary creature. They may have made tigers into foolish characters in order " + C(4, 'to be') + " less scared of them. White tigers are " + C(5, 'considered') + " sacred guardians.")), 3,
 "thinks (that) 뒤 명사절의 동사가 필요 → <i>is</i>. ① 주어 It(단수) 현재 ② Since then → 현재완료 ④ in order to + 동사원형 ⑤ 백호가 '여겨지는' 수동")
add(Q(9, '다음 글의 주제로 가장 적절한 것은?' + src('4과 본문 ❶'), BOX(J(M1)) + '\n' + OL([
 "the history of plastic production", "why sea levels have stopped rising", "ways to stop people from producing waste at home",
 "the main causes of forest fires", "the environmental crisis and the possibility of solutions from nature"])), 5,
 "환경이 위기(온난화·재해·쓰레기·플라스틱) → 인간이 주된 원인 → 그러나 자연이 해결책을 주었을지도 모른다 → 환경 위기와 자연에서 찾는 해결책. ①③④ 일부 소재 ② 해수면은 상승 중")
add(Q(10, '다음 글의 내용과 일치하지 <u>않는</u> 것은?' + src('4과 본문 ❷'), BOX(J(M2, 0, 15)) + '\n' + OL([
 "About half of all plastic is made for single-use items.",
 "Most plastic waste in the world has already been recycled.",
 "Some plastic waste is simply dumped or burned.",
 "Plastic in the ocean threatens many sea creatures.",
 "Scientists hope to speed up how the bacteria break down plastic."])), 2,
 "less than ten percent ~ has been recycled → 대부분 재활용되었다는 말은 불일치. ① About fifty percent ③ dumped or burned ④ puts many marine species in danger ⑤ speed up the process")
add(Q(11, '다음 빈칸에 들어갈 말로 가장 적절한 것은?' + src('4과 본문 ❷'), BOX(J(M2, 8, 12) + " This means that mealworms can actually " + BL + " plastic.") + '\n' + OL(['produce', 'avoid', 'recycle', 'feed on', 'be made of'])), 4,
 "밀웜 속 박테리아가 플라스틱을 분해할 수 있다 → 밀웜이 플라스틱을 '먹고 살 수' 있다 → feed on. produce 만들다 · avoid 피하다 · recycle 재활용하다 · be made of ~로 만들어지다")
q, a = ABCQ(12, '주어진 글 다음에 이어질 글의 순서로 가장 적절한 것은?' + src('4과 본문 ❸'), M3[0], [J(M3, 1, 3), J(M3, 3, 6), J(M3, 8, 10)], 'ACB')
add(q, a, "광산 등이 흙을 오염시킴 → (A) 파서 옮기면 비싸고 문제를 옮길 뿐 → (C) 다행히(Fortunately) 버드나무를 심는 방법·뿌리가 해로운 물질을 뽑아냄 → (B) 어떤 종이 더 잘 흡수하므로 더 연구해야 함")
add(Q(13, '밑줄 친 <u>this promising area</u>가 가리키는 것으로 가장 적절한 것은?' + src('4과 본문 ❸'), BOX(J(M3, 3, 11).replace('this promising area', '<u>this promising area</u>')) + '\n' + OL([
 '광산과 같은 산업 분야', '오염된 흙을 매립지로 옮기는 방법', '버드나무로 오염된 흙을 정화하는 연구', '산성도가 높은 흙의 특성', '중금속을 거래하는 사업'], False)), 3,
 "앞 문장들: 버드나무를 이용하는 방법의 효과에 대한 연구가 진행 중, 어떤 종이 더 잘 흡수함 → 이 유망한 분야 = 버드나무로 흙을 정화하는 연구")
g, b, a = INS(M4, 6, 1, 8)
add(Q(14, '글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳은?' + src('4과 본문 ❹'), g + '\n' + b), a,
 "바이오 연료의 정의 뒤에, 커피 찌꺼기에서 조류를 기를 수 있다는 주어진 문장 → 다음 문장 these algae(이 조류)가 주어진 문장의 algae를 받음 → ⑤")
add(Q(15, '다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 적절한 것은?' + src('4과 본문 ❹'), BOX(J(M4)) + '\n' + SUM(
 "Used coffee grounds, which would otherwise <b>(A)</b> ________ greenhouse gases in landfills, can be <b>(B)</b> ________ into biofuel with the help of algae.") + '\n' + TB(['(A)', '(B)'], [
 ['reduce', 'converted'], ['release', 'converted'], ['release', 'thrown'], ['absorb', 'burned'], ['absorb', 'converted']])), 2,
 "매립지에서 해로운 온실가스를 만든다 → (A) release(내뿜다) / 조류를 길러 바이오 연료로 바꾼다 → (B) converted(바뀐). reduce·absorb는 반대")
add(Q(16, '다음 빈칸에 들어갈 말로 가장 적절한 것은?' + src('4과 본문 ❺'), BOX(J(M5, 0, 3) + " In return, " + BL + ". If we do, the future of our planet may be bright after all.") + '\n' + OL([
 "we can stop worrying about the planet", "nature will clean the earth by itself", "we should stop all scientific research",
 "we need to look for more ways to keep the environment healthy", "we should move to another planet"])), 4,
 "자연이 기회를 한 번 더 주었으니 그 대가로(In return) 우리도 환경을 건강하게 지킬 방법을 더 찾아야 한다. 뒤 문장 If we do(그렇게 하면)와 이어짐")
add(Q(17, '다음 글의 밑줄 친 부분 중, 어법상 <u>틀린</u> 것은?' + src('4과 본문 변형'), BOX(
 "With the planet " + C(1, 'becoming') + " warmer, sea levels are rising. Mealworms are the larvae " + C(2, 'of') + " a certain species of beetle. Scientists are now looking for ways " + C(3, 'cultivating') + " the bacteria outside of mealworms. Some species of willow trees " + C(4, 'are able to') + " absorb harmful materials better than others. The coffee-making process generates used coffee grounds, " + C(5, 'which') + " are normally sent to landfills.")), 3,
 "명사 ways를 꾸미는 to부정사 → <i>to cultivate</i>. ① with + 명사 + 분사 ② the larvae of ~ ④ be able to + 동사원형 ⑤ 콤마 뒤 계속적 용법 which")
add(Q(18, '다음 글의 밑줄 친 부분 중, 문맥상 낱말의 쓰임이 적절하지 <u>않은</u> 것은?' + src('4과 본문 변형'), BOX(
 "Recycling can help " + C(1, 'increase') + " the amount of plastic in our landfills. Often, plastic waste is moved to places where it is just " + C(2, 'dumped') + " or burned. Willow trees naturally " + C(3, 'extract') + " a wide range of harmful materials from the soil. The biofuel is " + C(4, 'renewable') + " and sustainable. It seems that Mother Nature has given us one more " + C(5, 'chance') + ".")), 1,
 "재활용은 매립지의 플라스틱 양을 '줄이는' 데 도움이 된다 → <i>reduce</i>. ② 버려지다 ③ 뽑아내다 ④ 재생 가능한 ⑤ 기회")
add(Q(19, '3·4과 본문에 나온 단어와 영영풀이가 바르게 짝지어지지 <u>않은</u> 것은?' + src('종합'), OL([
 "abundant: existing in large amounts", "depict: to show something in a picture or in words", "extinct: no longer existing",
 "discard: to throw something away", "extract: to put something into a place"])), 5,
 "extract는 '뽑아내다(to remove or take out)'. 어딘가에 넣는다는 뜻은 반대. ① 풍부한 ② 묘사하다 ③ 멸종된 ④ 버리다")
add(Q(20, '3·4과 본문의 단어와 바꿔 쓴 말이 잘못 짝지어진 것은?' + src('종합'), OL([
 "revive → bring back", "abundant → scarce", "approximately → roughly", "cultivate → grow", "sustainable → able to continue"])), 2,
 "abundant(풍부한)와 scarce(부족한)는 반대말. ① 되살리다 ③ 대략 ④ 기르다 ⑤ 지속 가능한")
page('wrapup-jeodong-ne-mix1.html', '저동고 능률 3·4과 통합 Wrap-up 1차', '능률 3·4과 통합 Wrap-up 1차', 'A Timeless Symbol of Korea · Looking to Nature for Help',
     '범위: 3과 본문 ❶~❺ + 4과 본문 ❶~❺ (데일리 학습 DAY 1~12). 3과·4과 문제가 섞여 있어요. 지문은 일부 바꾼 것이 있으니 선택지의 표현을 본문과 정확히 대조하세요.', qs, A, E, '1차')

# ═════════════ 2차 (상 · 어휘 비틀기) ═════════════
qs = []; E = []; A = ''
add(Q(1, '다음 글의 내용과 일치하는 것은?' + src('3과 본문 ❶❷'), BOX(J(L31) + ' ' + J(L32, 0, 7)) + '\n' + OL([
 "Keller's book came out before 2020 to promote tourism to Korea.",
 "\"The Sun and the Moon\" revolves around a grandmother and a tiger.",
 "Tigers were once so sparse in Korea that sightings were considered legendary.",
 "The earliest trace of tigers in Korean culture lies in prehistoric rock carvings.",
 "Roughly four in ten Korean folktales of every kind feature a tiger."])), 4,
 "The first appearance ~ dates back to the rock art of the Bronze Age = 가장 이른 흔적은 선사 시대 바위 그림. ① in 2020, 관광 홍보 아님 ② a brother, a sister, and a tiger ③ sparse(드문) ↔ abundant ⑤ 모든 설화가 아니라 '동물 설화'의 약 40%. revolve around ~을 중심으로 전개되다 · trace 흔적")
add(Q(2, '다음 글의 밑줄 친 (a)~(e)를 바꿔 쓴 말로 적절하지 <u>않은</u> 것은?' + src('3과 본문 ❷'), BOX(
 "Long ago, tigers were so " + U('a', 'abundant') + " in Korea that people often called the country the \"Land of Tigers.\" It is " + U('b', 'estimated') + " that tigers lived in Korea for at least 100,000 years. The rock art of the Bronze Age " + U('c', 'depicts') + " people hunting various animals. Some of you may have heard Korean folktales " + U('d', 'featuring') + " tigers. In fact, " + U('e', 'approximately') + " forty percent of Korean folktales about animals include a tiger.") + '\n' + OL(['(a) → plentiful', '(b) → verified', '(c) → portrays', '(d) → showcasing', '(e) → roughly'], False)), 2,
 "estimate는 '추정하다'. verify는 '사실임을 확인(입증)하다'라서 뜻이 다르다. plentiful 풍부한 · portray 묘사하다 · showcase 보여 주다 · roughly 대략")
add(Q(3, '다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 적절한 것은?' + src('3과 본문 ❸'), BOX(J(L33, 0, 6)) + '\n' + SUM(
 "People's <b>(A)</b> ________ attitude toward tigers — admiring yet fearing them — may explain why folktales sometimes <b>(B)</b> ________ them as foolish.") + '\n' + TB(['(A)', '(B)'], [
 ['indifferent', 'portrayed'], ['hostile', 'glorified'], ['consistent', 'portrayed'], ['ambivalent', 'glorified'], ['ambivalent', 'portrayed']])), 5,
 "존경(respect)과 두려움(scared)이 함께 → (A) ambivalent(상반된 감정을 지닌) = conflicting / 덜 무서워하려고 어리석은 캐릭터로 '그렸다' → (B) portrayed. indifferent 무관심한 · hostile 적대적인 · consistent 한결같은 · glorify 미화하다")
add(Q(4, '다음 빈칸에 들어갈 말로 가장 적절한 것은?' + src('3과 본문 ❸'), BOX(J(L33, 2, 5) + " They may have made tigers into foolish characters in order to " + BL + ".") + '\n' + OL([
 "alleviate their dread of the animals", "glorify the animals' bravery", "warn children against hunting", "justify the extinction of tigers", "attract foreign visitors"])), 1,
 "호랑이에게 다치거나 죽는 일이 흔해서 두려워함 → 어리석은 캐릭터로 만들어 '두려움을 덜려고'(= to be less scared of them). alleviate 덜다 · dread 두려움 · glorify 미화하다 · justify 정당화하다")
add(Q(5, '다음 글에서 전체 흐름과 관계 <u>없는</u> 문장은?' + src('3과 본문 ❸ 변형'), BOX(
 L33[6] + " ① " + L33[7] + " ② " + L33[8] + " ③ Tiger hunting was banned around the world in the early 1900s. ④ " + L33[9] + " ⑤ " + L33[11])), 3,
 "호랑이의 감소·상징성 쇠퇴 → 올림픽 마스코트로 되살아남(호돌이·수호랑)의 흐름. 전 세계 호랑이 사냥 금지는 본문과 관계없고 사실과도 다르다")
add(Q(6, '다음 글의 내용과 일치하지 <u>않는</u> 것은?' + src('3과 본문 ❺'), BOX(J(L35)) + '\n' + OL([
 "Wild tigers are now reportedly limited to a handful in North Korea.",
 "The cultural significance of tigers has largely vanished from modern Korean life.",
 "The writer regards the tiger's status as a national symbol as indisputable.",
 "A national museum compiled Korean tiger stories into a single book.",
 "Readers are encouraged to spot tigers in their surroundings."])), 2,
 "the history, stories, and cultural meaning of tigers still have a place among modern Korean people → 문화적 의미가 '사라졌다'는 불일치. ① a handful = only a few ③ indisputable(논쟁의 여지가 없는) = Who can deny ~? ④ compile 엮다 ⑤ spot 찾아내다")
add(Q(7, '다음 (a)~(g) 중 어법상 <u>틀린</u> 것의 개수는?' + src('3과 본문 변형'), BOX(
 "Its story starts with a girl " + U('a', 'who') + " meets a tiger. Keller's inspiration was an old folktale that her <i>halmoni</i> used to " + U('b', 'telling') + " her. Long ago, people often called the country " + U('c', 'as') + " the \"Land of Tigers.\" The rock art depicts people " + U('d', 'hunting') + " various animals. The tiger mistakenly thinks the <i>gotgam</i> is a very " + U('e', 'scared') + " creature. Being injured or even killed by tigers " + U('f', 'were') + " common in the past. White tigers are " + U('g', 'considered') + " sacred guardians.") + '\n' + OL(['1개', '2개', '3개', '4개', '5개'], False)), 4,
 "틀린 것 (b) (c) (e) (f) 4개. (b) used to + 동사원형 → <i>tell</i> (c) call + 목적어 + 명사(보어), as 불필요 (e) 무서움을 '주는' 존재 → <i>scary</i> (f) 동명사 주어는 단수 → <i>was</i>. (a) 사람 선행사 who (d) 지각 대상의 능동 hunting (g) 수동 considered")
add(Q(8, '다음 글의 밑줄 친 부분 중, 문맥상 낱말의 쓰임이 적절하지 <u>않은</u> 것은?' + src('3과 본문 ❸ 어휘 변형'), BOX(
 "Tigers in Korea faced a " + C(1, 'dwindling') + " population due to hunting during the Joseon period and nearly " + C(2, 'vanished') + " during the Japanese colonial era. With their disappearance, their role as a national emblem " + C(3, 'waned') + ". However, their symbolism was " + C(4, 'resurrected') + " through their selection as the mascot for both Olympics hosted by Korea. White tigers are regarded as " + C(5, 'profane') + " guardians.")), 5,
 "백호는 '신성한(sacred)' 수호자로 여겨진다 → profane(불경한, 세속적인)은 반대. ① dwindling 줄어드는 = decline ② vanish 사라지다 = go extinct ③ wane 약해지다 = fade away ④ resurrect 되살리다 = revive")
q, a = ABCQ(9, '주어진 글 다음에 이어질 글의 순서로 가장 적절한 것은?' + src('4과 본문 ❷'), M2[0], [J(M2, 1, 5), J(M2, 5, 8), J(M2, 8, 11)], 'ACB')
add(q, a, "일회용 플라스틱 50% → (A) 한 번 쓰고 버림·재활용은 10% 미만 → (C) 그냥 버리거나 태우고, 게다가 바다로 → 해양 생물 위험 → (B) 이를 염두에 두고(With this in mind) 밀웜에 주목, 몸속 박테리아")
add(Q(10, '다음 빈칸에 들어갈 말로 가장 적절한 것은?' + src('4과 본문 ❷ 어휘 변형'), BOX(J(M2, 9, 13) + " Scientists are now looking for ways to " + BL + " outside of mealworms. They also want to speed up the process by which the bacteria break down plastic.") + '\n' + OL([
 "eliminate the beetles", "dispose of the larvae", "propagate the plastic-degrading microbes", "export the plastic waste", "burn the landfills"])), 3,
 "원문: cultivate the bacteria outside of mealworms → 플라스틱을 분해하는 미생물을 밀웜 밖에서 '번식시키다(propagate)'. eliminate 없애다 · dispose of 처리하다 · degrade 분해하다 · microbe 미생물")
add(Q(11, '다음 글의 내용과 일치하는 것은?' + src('4과 본문 ❸'), BOX(J(M3)) + '\n' + OL([
 "Excavating polluted soil is an inexpensive and lasting remedy.",
 "Willow trees can survive only in soil free of heavy metals.",
 "Willows have shallow roots that limit their cleaning ability.",
 "All willow species absorb toxins equally well.",
 "Further investigation is needed to identify the most efficient willow species."])), 5,
 "this promising area should be further explored to find out which trees are the most effective ✔. ① 비싸고 문제를 옮길 뿐 ② 중금속이 많은 흙에서도 잘 자람 ③ extensive and well-developed root systems ④ some species ~ better than others. excavate 파내다 · remedy 해결책 · toxin 독소")
add(Q(12, '다음 빈칸에 들어갈 말로 가장 적절한 것은?' + src('4과 본문 ❸ 어휘 변형'), BOX(J(M3, 0, 3) + " Fortunately, there is an eco-friendly and " + BL + " way to restore polluted soil — planting willow trees.") + '\n' + OL([
 "labor-intensive", "short-lived", "hazardous", "economically viable", "prohibitively costly"])), 4,
 "흙을 파서 옮기는 방법은 비싸다(expensive) → Fortunately 뒤에는 '경제적으로 실행 가능한(= cost-effective)' 방법. labor-intensive 노동력이 많이 드는 · short-lived 오래가지 않는 · hazardous 위험한 · prohibitively costly 엄두를 못 낼 만큼 비싼")
add(Q(13, '다음 글의 내용과 일치하지 <u>않는</u> 것은?' + src('4과 본문 ❹'), BOX(J(M4)) + '\n' + OL([
 "Roughly a third of the world's population consumes coffee every day.",
 "Used coffee grounds are usually composted instead of being thrown away.",
 "Coffee grounds in landfills can emit a gas that warms the planet.",
 "Algae can thrive on coffee grounds without extra nourishment.",
 "The resulting biofuel is renewable and low in emissions."])), 2,
 "used coffee grounds, which are normally sent to landfills → 보통 매립지로 간다. 퇴비로 만든다(composted)는 불일치. ① 30~40% ≒ 약 3분의 1 ③ emit 내뿜다 · greenhouse gas ④ without adding any other nutrients ⑤ renewable, a small amount of emissions")
g, b, a = INS(M4, 4, 3, 9)
add(Q(14, '글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳은?' + src('4과 본문 ❹'), g + '\n' + b), a,
 "모두가 커피를 끊게 할 수는 없다(Unfortunately) → 그러나(However) 커피 찌꺼기를 바이오 연료로 바꿔 배출을 줄일 수 있다 → 이어서 바이오 연료의 정의 → ①")
add(Q(15, '다음 글의 요지로 가장 적절한 것은?' + src('4과 본문 ❺'), BOX(J(M5)) + '\n' + OL([
 "Technology alone will resolve every ecological crisis.",
 "Nature's remedies make human effort unnecessary.",
 "Nature's solutions are a second chance that we must repay by protecting the environment.",
 "Environmental problems are too complex to be addressed.",
 "Humanity should abandon modern industry altogether."])), 3,
 "자연이 해결책(기회)을 한 번 더 주었고, 그 대가로(In return) 우리는 환경을 지킬 방법을 더 찾아야 한다 → repay 보답하다. ② 노력이 필요 없다는 반대 ①④⑤ 근거 없음")
add(Q(16, '다음 (a)~(g) 중 어법상 <u>틀린</u> 것의 개수는?' + src('4과 본문 변형'), BOX(
 "Sea levels " + U('a', 'are rising') + ". More and more waste is also " + U('b', 'producing') + ". The items are used just once and then " + U('c', 'discarding') + ". Plastic waste is moved to places " + U('d', 'which') + " it is just dumped. Scientists want to speed up the process " + U('e', 'by which') + " the bacteria break down plastic. Willow trees naturally " + U('f', 'extracts') + " harmful materials. If these algae " + U('g', 'expose') + " to twenty hours of light, they produce biofuel.") + '\n' + OL(['1개', '2개', '3개', '4개', '5개'], False)), 5,
 "틀린 것 (b) (c) (d) (f) (g) 5개. (b) 수동 진행 being produced (c) used와 병렬인 수동 → discarded (d) 완전한 절 → where (f) 주어 trees(복수) → extract (g) 조류가 빛에 '노출되는' 수동 → are exposed. (a) 진행형 ✔ (e) 전치사 + 관계대명사 ✔")
add(Q(17, '다음 글의 밑줄 친 부분 중, 문맥상 낱말의 쓰임이 적절하지 <u>않은</u> 것은?' + src('4과 본문 어휘 변형'), BOX(
 "Plastic, in particular, is " + C(1, 'alleviating') + " problems with soil and water pollution. It is clear that humans are a major " + C(2, 'culprit') + " in the destruction of nature. The items are used just once and then " + C(3, 'disposed of') + ". Willow trees naturally " + C(4, 'draw out') + " a wide range of harmful materials from the soil. The biofuel is " + C(5, 'replenishable') + " and sustainable.")), 1,
 "플라스틱은 토양·수질 오염 문제를 '일으킨다(causing)' → alleviate(완화하다)는 반대. ② culprit 주범 = major contributor ③ dispose of 버리다 = discard ④ draw out 뽑아내다 = extract ⑤ replenishable 다시 채울 수 있는 = renewable")
add(Q(18, '4과 본문 전체의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 적절한 것은?' + src('4과 본문 ❶~❺'), BOX(M1[8] + ' ' + J(M2, 8, 12) + ' ' + J(M3, 3, 6) + ' ' + J(M4, 4, 8) + ' ' + M5[0]) + '\n' + SUM(
 "Nature offers <b>(A)</b> ________ solutions to environmental problems, from bacteria that <b>(B)</b> ________ plastic to willows that purify soil and algae that turn waste into fuel.") + '\n' + TB(['(A)', '(B)'], [
 ['costly', 'produce'], ['artificial', 'degrade'], ['eco-friendly', 'produce'], ['eco-friendly', 'degrade'], ['temporary', 'store']])), 4,
 "(A) 자연에서 얻은 친환경적인(eco-friendly) 해결책 (B) 박테리아는 플라스틱을 분해한다(break down = degrade). costly·artificial·temporary는 근거 없음, produce·store는 반대")
add(Q(19, '3·4과 본문에 나온 단어와 영영풀이가 바르게 짝지어지지 <u>않은</u> 것은?' + src('종합'), OL([
 "sacred: considered holy and deserving respect", "larva: the young form of an insect", "acidity: the state of being completely free of chemicals",
 "emission: a gas or substance sent out into the air", "reinterpret: to explain or present something in a new way"])), 3,
 "acidity는 '산성(도)'. 화학 물질이 전혀 없는 상태라는 뜻이 아니다. ① 신성한 ② 애벌레 ④ 배출(물) ⑤ 재해석하다")
add(Q(20, '3과와 4과 본문의 제목으로 바르게 짝지어진 것은?' + src('종합'), TB(['3과', '4과'], [
 ['The Fall of the Korean Tiger', 'Plastic: A Modern Miracle'], ['A Lasting Emblem of Korean Culture', "Nature's Answers to Our Environmental Crises"],
 ['Tigers Only in K-pop', 'Why Coffee Harms Us'], ['Olympic Mascots of Asia', "Nature's Answers to Our Environmental Crises"],
 ['A Lasting Emblem of Korean Culture', 'How to Recycle Plastic at Home']])), 2,
 "3과: 옛날부터 지금까지 한국 문화 속에 이어진 호랑이 = 오래 지속되는 상징(A Lasting Emblem) / 4과: 밀웜·버드나무·조류처럼 자연이 주는 환경 문제의 해답. ①③ 일부 소재 ④ 3과 제목이 좁다 ⑤ 4과 제목이 재활용에만 한정")
page('wrapup-jeodong-ne-mix2.html', '저동고 능률 3·4과 통합 Wrap-up 2차', '능률 3·4과 통합 Wrap-up 2차', '고난도 · 어휘 비틀기',
     '범위: 3과 본문 ❶~❺ + 4과 본문 ❶~❺. 2차는 고난도예요. 선택지와 지문의 낱말을 어려운 동의어로 바꿔 쓴(어휘 비틀기) 문제가 많으니, 뜻을 하나하나 따져 보세요.', qs, A, E, '2차')
