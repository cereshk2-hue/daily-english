exec(open('wcommon.py',encoding='utf-8').read())
T2=lambda a,b,c:'    <div class="box"><p><span class="tag">(A)</span> %s</p><p><span class="tag">(B)</span> %s</p><p><span class="tag">(C)</span> %s</p></div>'%(a,b,c)
OR2=lambda seq: OL(seq,False)
P1="We make many personal choices in our lives, from who to have lunch with to what career to pursue. However, there are many situations where we must make decisions as a group. Group decision-making is not as simple as our personal choices, as it involves numerous voices with differing opinions. Voting is often used to make group decisions fairer and more efficient, and various voting methods have been developed over time. The following story illustrates how these different voting methods work."
u=lambda t,x:'<span class="tag">(%s)</span><u>%s</u>'%(t,x)
qs=[]
qs.append(Q(1,'다음 글의 내용과 일치하지 <u>않는</u> 것은?'+src('본문 ❶'),BOX(P1)+'\n'+OL([
 "Personal decisions can range from trivial everyday matters to major life choices.",
 "Collective decisions are complicated by the presence of divergent viewpoints.",
 "Voting methods have remained largely unchanged since they were first devised.",
 "Voting is employed to render group decisions more equitable and efficient.",
 "The passage goes on to present a narrative illustrating how voting methods operate."])))
qs.append(Q(2,'다음 글의 밑줄 친 (a)~(h) 중 어법상 <u>틀린</u> 것의 개수는?'+src('본문 ❶ 변형'),BOX(
 "We make many personal choices in our lives, from "+u('a','who having')+" lunch with to what career to pursue. However, there are many situations "+u('b','where')+" we must make decisions as a group. Group decision-making is not as "+u('c','simpler')+" as our personal choices, as it "+u('d','involves')+" numerous voices with "+u('e','differing')+" opinions. Voting is often used to make group decisions "+u('f','more fairly')+" and more efficient, and various voting methods "+u('g','have developed')+" over time. The following story illustrates "+u('h','how')+" these different voting methods work.")+'\n'+OL(['1개','2개','3개','4개','5개'],False)))
qs.append(Q(3,'다음 빈칸에 들어갈 말로 가장 적절한 것은?'+src('본문 ❶'),BOX(
 "We make many personal choices in our lives, from who to have lunch with to what career to pursue. However, there are many situations where we must make decisions as a group. Group decision-making is not as simple as our personal choices, as it <span class=\"blank\"></span>. Voting is often used to make group decisions fairer and more efficient.")+'\n'+OL([
 "relies on the judgment of a single leader","involves numerous voices with differing opinions","requires no discussion among its members","is usually settled by pure chance","concerns only trivial matters"])))
qs.append(Q(4,'다음 글의 밑줄 친 부분 중, 문맥상 낱말의 쓰임이 적절하지 <u>않은</u> 것은?'+src('본문 ❷ 변형'),BOX(
 "The members of the Greenville High School student council needed to decide how to raise money for children ①<u>in need</u>. Their three options were an art show, a bake sale, and a charity concert, but there were ②<u>conflicting</u> opinions. So they decided to put it to a ③<u>vote</u>. When they asked for advice from Ms. Akers, the council's advisor, she encouraged them not to use the ④<u>familiar</u> voting method, but to try something different instead. After doing some research, the council members decided to ⑤<u>abandon</u> three different voting systems: the first-past-the-post (FPTP) method, the alternative vote (AV) method, and the Condorcet method.")))
qs.append(Q(5,'(A), (B), (C)의 각 네모 안에서 어법에 맞는 표현으로 가장 적절한 것은?'+src('본문 ❷'),BOX(
 "The members of the Greenville High School student council needed to decide <b>(A)</b> [how to raise / how raising] money for children in need. ... When they asked for advice from Ms. Akers, the council's advisor, she encouraged them <b>(B)</b> [not to use / not using] the familiar voting method, but to try something different instead. ... The entire council was curious to find out <b>(C)</b> [if / that] the different methods would yield different results.")+'\n'+TB(['(A)','(B)','(C)'],[
 ['how to raise','not to use','if'],['how to raise','not using','that'],['how raising','not to use','if'],['how raising','not using','if'],['how to raise','not to use','that']])))
P2="The members of the Greenville High School student council needed to decide how to raise money for children in need. Their three options were an art show, a bake sale, and a charity concert, but there were conflicting opinions. So they decided to put it to a vote. When they asked for advice from Ms. Akers, the council's advisor, she encouraged them not to use the familiar voting method, but to try something different instead. After doing some research, the council members decided to try three different voting systems: the first-past-the-post (FPTP) method, the alternative vote (AV) method, and the Condorcet method. The entire council was curious to find out if the different methods would yield different results."
qs.append(Q(6,'다음 글의 내용과 일치하는 것은?'+src('본문 ❷'),BOX(P2)+'\n'+OL([
 "The council unanimously agreed on which event to hold before any vote took place.",
 "Ms. Akers advised the council to stick with the conventional voting method.",
 "The council settled on a single voting system after conducting research.",
 "The council intended to raise funds for underprivileged children.",
 "The members were indifferent to whether the methods would produce different outcomes."])))
qs.append(Q(7,'주어진 글 다음에 이어질 글의 순서로 가장 적절한 것은?'+src('본문 ❷'),GIV("The members of the Greenville High School student council needed to decide how to raise money for children in need.")+'\n'+T2(
 "When they asked for advice from Ms. Akers, the council's advisor, she encouraged them not to use the familiar voting method, but to try something different instead.",
 "Their three options were an art show, a bake sale, and a charity concert, but there were conflicting opinions. So they decided to put it to a vote.",
 "After doing some research, the council members decided to try three different voting systems: the FPTP method, the AV method, and the Condorcet method.")+'\n'+OR2(['(A) − (C) − (B)','(B) − (C) − (A)','(B) − (A) − (C)','(C) − (A) − (B)','(C) − (B) − (A)'])))
qs.append(Q(8,'글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳은?'+src('본문 ❸'),GIV("Each of the 20 council members was given a voting slip and instructed to write down the options in order of preference.")+'\n'+BOX(
 "The entire council was curious to find out if the different methods would yield different results. ( ① ) On the day of the vote, each possible event was given a letter: \"art show\" was represented by the letter A, the letter B indicated \"bake sale,\" and C stood for \"charity concert.\" ( ② ) For example, if the charity concert was their first choice, followed by the bake sale and the art show, they would write CBA. ( ③ ) After every member had voted, the voting slips were counted. ( ④ ) The results were as follows. ( ⑤ )")))
P3="On the day of the vote, each possible event was given a letter: \"art show\" was represented by the letter A, the letter B indicated \"bake sale,\" and C stood for \"charity concert.\" Each of the 20 council members was given a voting slip and instructed to write down the options in order of preference. For example, if the charity concert was their first choice, followed by the bake sale and the art show, they would write CBA. After every member had voted, the voting slips were counted."
qs.append(Q(9,'다음 글의 내용과 일치하지 <u>않는</u> 것은?'+src('본문 ❸'),BOX(P3)+'\n'+OL([
 "Each of the options was assigned a letter to represent it.",
 "Every member ranked all of the options according to personal preference.",
 "A voter favoring the concert, then the bake sale, then the art show would write CBA.",
 "The slips were tallied only after all members had cast their votes.",
 "Members were permitted to mark only a single option on their voting slips."])))
qs.append(Q(10,'다음 글의 밑줄 친 (a)~(e) 중 어법상 <u>틀린</u> 것끼리 짝지은 것은?'+src('본문 ❸ 변형'),BOX(
 "On the day of the vote, each possible event "+u('a','gave')+" a letter: \"art show\" "+u('b','was represented')+" by the letter A, the letter B indicated \"bake sale,\" and C stood for \"charity concert.\" Each of the 20 council members "+u('c','were given')+" a voting slip and instructed to write down the options in order of preference. For example, if the charity concert was their first choice, "+u('d','followed')+" by the bake sale and the art show, they would write CBA. After every member "+u('e','had voted')+", the voting slips were counted.")+'\n'+OL(['(a), (c)','(a), (d)','(b), (c)','(b), (e)','(d), (e)'],False)))
P4="The FPTP method is the simplest of the three methods. Voters are given several options, and whichever gets the most first-preference votes wins. Neither the second nor third preference matters at all, so they are ignored. This method is commonly used in political elections around the world. The student council quickly determined that the winner would be option C, the charity concert. This was because it received 8 first-preference votes, while option A received 5 and option B received 7."
qs.append(Q(11,'다음 빈칸에 들어갈 말로 가장 적절한 것은?'+src('본문 ❹'),BOX(
 "The FPTP method is uncomplicated and easy to understand, but it has a significant weakness. It is possible to <span class=\"blank\"></span>. That was the case here. According to the results of the FPTP method, the council's choice was to hold a charity concert. However, only 8 out of 20 council members chose the charity concert as their first preference, which equaled 40% of the total votes.")+'\n'+OL([
 "ignore first-preference votes entirely","require several rounds of counting","give second preferences too much weight","win a vote without the support of the majority","end up in a tie in almost every election"])))
qs.append(Q(12,'본문 ❹의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 적절한 것은?'+src('본문 ❹'),SUM(
 "Under the FPTP method, an option can win simply by securing a <b>(A)</b> ________ of first-preference votes, even if it lacks <b>(B)</b> ________ support.")+'\n'+TB(['(A)','(B)'],[
 ['majority','minority'],['plurality','majority'],['minority','unanimous'],['plurality','minority'],['majority','unanimous']])))
qs.append(Q(13,'본문 ❹의 내용과 일치하지 <u>않는</u> 것은?'+src('본문 ❹'),BOX(P4+" The FPTP method is uncomplicated and easy to understand, but it has a significant weakness.")+'\n'+OL([
 "Under FPTP, only first-preference votes are taken into account.",
 "FPTP is widely adopted in political elections across the globe.",
 "The charity concert secured an outright majority of first-preference votes.",
 "The art show received the fewest first-preference votes of the three options.",
 "The two leading options were separated by a single first-preference vote."])))
qs.append(Q(14,'다음 글에서 전체 흐름과 관계 <u>없는</u> 문장은?'+src('본문 ❹ 변형'),BOX(
 "The FPTP method is the simplest of the three methods. ① Voters are given several options, and whichever gets the most first-preference votes wins. ② Neither the second nor third preference matters at all, so they are ignored. ③ This method is commonly used in political elections around the world. ④ The student council quickly determined that the winner would be option C, the charity concert. ⑤ Charity concerts tend to attract larger audiences because famous singers often perform at them for free.")))
qs.append(Q(15,'(A), (B), (C)의 각 네모 안에서 어법에 맞는 표현으로 가장 적절한 것은?'+src('본문 ❹'),BOX(
 "The FPTP method is the <b>(A)</b> [simplest / simpler] of the three methods. Voters are given several options, and <b>(B)</b> [whichever / however] gets the most first-preference votes wins. Neither the second <b>(C)</b> [nor / or] third preference matters at all, so they are ignored.")+'\n'+TB(['(A)','(B)','(C)'],[
 ['simplest','whichever','nor'],['simpler','whichever','or'],['simplest','however','nor'],['simpler','however','or'],['simplest','whichever','or']])))
qs.append(Q(16,'글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳은?'+src('본문 ❺'),GIV("Therefore, option A was eliminated, and the 5 council members' votes were redistributed based on their second preferences.")+'\n'+BOX(
 "The AV method can potentially include more than one round of counting. ( ① ) For an option to win in the first round, it needs to get more than 50% of the first-preference votes. ( ② ) As the charity concert only received 40% of the total votes, a second round of counting was required. ( ③ ) Option A, the art show, received the fewest first-preference votes, with only 5 council members voting for it. ( ④ ) As a result, 4 votes for option B (ABC) and 1 for option C (ACB) were added to the total. ( ⑤ ) This meant that option B had 11 total votes, while option C had only 9.")))
qs.append(Q(17,'다음 빈칸에 들어갈 말로 가장 적절한 것은?'+src('본문 ❺'),BOX(
 "This meant that option B had 11 total votes, while option C had only 9. As a result, the bake sale would be the winner. Unfortunately, the AV method is not perfect either. It sometimes allows <span class=\"blank\"></span>. In this case, the bake sale won, but this was mainly due to the second-preference votes it received.")+'\n'+OL([
 "first-preference votes to be disregarded altogether",
 "second-preference votes to have a greater influence than first-preference votes",
 "the most popular option to win outright in the first round",
 "voters to change their minds after the votes are counted",
 "every option to end up with the same number of votes"])))
qs.append(Q(18,'다음 글의 밑줄 친 부분 중, 문맥상 낱말의 쓰임이 적절하지 <u>않은</u> 것은?'+src('본문 ❺ 변형'),BOX(
 "Next, the council members examined the votes using the AV method, and they soon realized that there would be a ①<u>different</u> result. The AV method can ②<u>potentially</u> include more than one round of counting. ... Option A, the art show, received the ③<u>most</u> first-preference votes, with only 5 council members voting for it. Therefore, option A was ④<u>eliminated</u>, and the 5 council members' votes were ⑤<u>redistributed</u> based on their second preferences.")))
qs.append(Q(19,'본문 ❺의 내용과 일치하는 것은?'+src('본문 ❺'),OL([
 "After the redistribution, the bake sale outnumbered the charity concert by two votes.",
 "The charity concert won outright in the first round of counting under AV.",
 "All five votes originally cast for the art show were transferred to the charity concert.",
 "The bake sale secured a majority on first-preference votes alone.",
 "The writer regards AV as a flawless alternative to the FPTP method."])))
qs.append(Q(20,'본문 ❶~❺ 전체의 요지로 가장 적절한 것은?'+src('본문 ❶~❺'),OL([
 "집단 의사 결정은 개인의 선택보다 언제나 더 공정하다.",
 "단순 다수결 방식이 가장 공정하고 효율적인 투표 방식이다.",
 "대안 투표 방식은 단순 다수결 방식의 약점을 완벽하게 해결한다.",
 "학생 자치회는 결국 자선 콘서트를 열기로 최종 결정했다.",
 "같은 투표 결과라도 어떤 투표 방식을 쓰느냐에 따라 승자가 달라질 수 있다."],False)))
ans='③④②⑤①④③②⑤①④②③⑤①④②③①⑤'
E=["시간이 흐르며 다양한 투표 방법이 개발되어 왔다(have been developed over time) → 거의 변하지 않았다는 틀림. devise 고안하다 ① range from A to B ② divergent = differing ④ render + O + 형용사 · equitable = fair",
 "틀린 것 (a)(c)(f)(g) 4개. (a) 의문사 + to부정사 → <i>who to have</i> (c) as + 원급 + as → <i>simple</i> (f) make + O + 형용사, efficient와 병렬 → <i>fairer</i> (g) 방법이 '개발되는' 수동 → <i>have been developed</i>",
 "as(~ 때문에) 뒤에 이유 → 다른 의견을 가진 수많은 목소리가 관련되기 때문에 개인 선택보다 복잡하다.",
 "조사 후 세 가지 투표 방식을 '시도해 보기로(try)' 함. abandon은 '버리다'.",
 "(A) 의문사 + to부정사 (B) encourage + O + to부정사, 부정은 not to (C) find out의 목적어 '~인지 아닌지' → <i>if</i>",
 "어려움에 처한 아이들(children in need = underprivileged children)을 위한 모금. ① unanimously 만장일치로 → 상충되는 의견 ② stick with 고수하다 → 다른 방법을 권함 ③ 세 가지 방식 ⑤ indifferent 무관심한 → curious",
 "(B) 세 선택지와 의견 충돌 → 투표하기로 함 → (A) 고문 교사가 다른 방식을 권함 → (C) 조사 후 세 가지 방식을 시도.",
 "글자를 정한 뒤 투표용지를 받고 선호 순으로 적으라는 지시(주어진 문장) → 그 예시(For example, CBA).",
 "선호하는 순서대로 모든 선택지를 적었다(in order of preference) → 하나만 적었다는 틀림. tally 집계하다 · cast a vote 투표하다",
 "(a) 행사에 글자가 '주어진' 수동 → <i>was given</i> (c) each of + 복수명사 → 단수동사 <i>was given</i>. (d) 분사구문(수동) (e) 집계보다 먼저 → 과거완료",
 "8/20 = 40%, 과반수 지지 없이도 이길 수 있다는 약점. That was the case here가 단서.",
 "plurality 최다 득표(과반이 아닌 상대 다수) · majority 과반수. 40%만으로 이긴 상황.",
 "자선 콘서트는 40%(8/20)만 얻음 → 과반(outright majority)이 아님. ⑤ 8표와 7표, 한 표 차이",
 "콘서트에 유명 가수가 무료로 공연한다는 내용 → FPTP 방식 설명과 관계없음.",
 "(A) 최상급 + of + 복수명사 (B) 복합관계대명사 whichever(~하는 어느 것이든)가 주어 역할 (C) neither A nor B",
 "가장 적은 표를 받은 A가 제거되고(주어진 문장) → 그 결과(As a result) B에 4표, C에 1표가 더해짐.",
 "빵 바자회는 2지망 표 덕분에 이겼다 → 2지망이 1지망보다 더 큰 영향을 미친다.",
 "5명만 투표했다(only 5) → 가장 '적은(fewest)' 1지망 표. most는 반대.",
 "재분배 후 B 11표, C 9표 → 2표 차이. outnumber ~보다 수가 많다 ② 40%라 2차 집계 필요 ③ B에 4표, C에 1표 ④ 1지망 7표 ⑤ flawless 결함 없는 → not perfect either",
 "같은 표를 FPTP로 세면 자선 콘서트, AV로 세면 빵 바자회가 이긴다 → 투표 방식에 따라 결과가 달라진다.",
]

SW='''
  <div class="part"><h2>서술형</h2><p>요약문 완성 · 답안은 아래 칸에 쓰세요.</p></div>
  <div class="swq">
    <div class="q">
      <div class="stem"><span class="n">서술형 1.</span>본문 ❹의 내용을 요약한 문장의 빈칸 (A), (B)에 들어갈 말을 <b>본문에서 찾아</b> 각각 한 단어로 쓰시오. <span class="pt">[6점]</span><span class="src">[본문 ❹]</span></div>
      <div class="sum">Although the FPTP method is <b>(A)</b> ____________ and easy to understand, it can let an option win without the support of the <b>(B)</b> ____________.</div>
      <div class="ans"><span>(A)</span><i></i><span>(B)</span><i></i></div>
    </div>
    <div class="q">
      <div class="stem"><span class="n">서술형 2.</span>본문 ❺의 내용을 요약한 문장이 되도록 &lt;보기&gt;의 말을 <b>모두 한 번씩</b> 바르게 배열하여 빈칸을 완성하시오. <span class="pt">[7점]</span><span class="src">[본문 ❺]</span></div>
      <div class="sum">In the AV method, if no option wins more than half of the first-preference votes, the option with the fewest votes is eliminated, and its votes ________________________________________.</div>
      <div class="cond"><b>&lt;보기&gt;</b> second preferences / redistribute / voters' / according / to</div>
      <div class="cond"><b>&lt;조건&gt;</b> 필요하면 어형을 바꾸고, 문맥에 맞게 <u>be동사 한 단어</u>를 추가할 것</div>
      <div class="ans wide"><i></i></div>
    </div>
    <div class="q">
      <div class="stem"><span class="n">서술형 3.</span>본문 ❶~❺의 내용을 요약한 문장을 &lt;조건&gt;에 맞게 완성하시오. <span class="pt">[7점]</span><span class="src">[본문 ❶~❺]</span></div>
      <div class="sum">The story of the student council shows that <b>(A)</b> ________________________________, as the FPTP method chose the charity concert while the AV method chose the bake sale, mainly because of <b>(B)</b> ________________________________.</div>
      <div class="cond"><b>&lt;조건&gt;</b> (A) <u>result, depend, voting method</u>를 반드시 사용하여 주어와 동사를 갖춘 절로 쓸 것 (9~11단어, 어형 변화 가능)<br>(B) <u>본문에서 찾아</u> 5단어로 쓸 것 (하이픈으로 연결된 말은 한 단어)</div>
      <div class="ans"><span>(A)</span><i></i></div><div class="ans"><span>(B)</span><i></i></div>
    </div>
  </div>
'''
SK='''
  <div class="part"><h2>서술형</h2><p>모범 답안과 채점 기준</p></div>
  <div class="exp one">
    <p><b>서술형 1</b> <span class="k">(A) uncomplicated (B) majority</span> 근거: <i>The FPTP method is uncomplicated and easy to understand ... It is possible to win a vote without the support of the majority.</i> 각 3점. (A)는 본문 단어 uncomplicated가 정답이에요. simple(본문 ❹ 첫 문장의 simplest)을 인정할지는 학교 채점 기준에 맞춰 정해 주세요.</p>
    <p><b>서술형 2</b> <span class="k">are redistributed according to voters' second preferences</span> 근거: <i>the 5 council members' votes were redistributed based on their second preferences</i> → its votes(복수, 현재 일반 서술) + 수동태 are redistributed. according to = based on. 어순 완벽 7점 · be동사 누락/시제 오류 −2점 · redistribute 형태 오류 −2점.</p>
    <p><b>서술형 3</b> <span class="k">(A) the result of a vote can depend on the voting method</span> (11단어) 또는 <i>the result can depend on which voting method is used</i>(10단어) 등 인정. <span class="k">(B) the second-preference votes it received</span> (본문 ❺ 마지막 문장 · the / second-preference / votes / it / received 5단어). (A) 4점: 세 단어 모두 사용 2점 + 문법·단어 수 2점 · (B) 3점.</p>
  </div>
'''

assert len(qs)==20 and len(ans)==20 and len(E)==20
from collections import Counter; print(Counter(ans))
key='<div class="keygrid">\n    '+''.join('<div>%d<b>%s</b></div>'%(k+1,a) for k,a in enumerate(ans[:10]))+'\n    '+''.join('<div>%d<b>%s</b></div>'%(k+11,a) for k,a in enumerate(ans[10:]))+'\n  </div>\n  <div class="exp">\n'+''.join('    <p><b>%d</b> <span class="k">%s</span> %s</p>\n'%(k+1,ans[k],e) for k,e in enumerate(E))+'  </div>'
html=('<title>대진고 능률 L3 Wrap-up</title>\n<meta name="claude:viewport-fit-sides" content="cover">\n'+fonts+css+'''<style>
.part { margin: 6px 0 10px; display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap; border-top: 2px solid var(--navy); padding-top: 10px }
.part h2 { margin: 0; font: 900 14px var(--f-ko); color: #fff; background: var(--navy); padding: 3px 10px }
.part p { margin: 0; font-size: 12.5px; color: var(--muted) }
.swq { display: grid; gap: 4px }
.pt { font-size: 12px; color: var(--key); font-weight: 700; margin-left: 4px }
.cond { font-size: 13px; line-height: 1.6 }
.ans { display: grid; grid-template-columns: auto 1fr auto 1fr; gap: 8px; align-items: end; margin-top: 4px }
.ans.wide, .swq .q .ans:has(span:only-of-type) { grid-template-columns: auto 1fr }
.ans.wide { grid-template-columns: 1fr }
.ans span { font-weight: 700; font-size: 13px }
.ans i { display: block; border-bottom: 1px solid var(--ink); height: 30px }
.exp.one { columns: 1 }
</style>

<main>
<section class="page">
  <div class="top"><span>영어Ⅱ NE능률(오선영) Lesson 3 · <b>본문 ❶~❺ Wrap-up</b></span><span>대진고등학교 2학년 · 2학기 기말 대비</span></div>
  <div class="title">
    <div class="g">영어Ⅱ</div>
    <h1>능률 L3 본문 Wrap-up<small>Life Is a Sum of Choices · 고난도</small></h1>
    <div class="when">선택형 20 × 4점 · 서술형 3<br>제한 시간 45분</div>
  </div>
  <div class="idrow"><div>반</div><div>번호</div><div>이름</div><div>점수 &nbsp;&nbsp;&nbsp; / 100</div></div>
  <p class="notice">범위: 데일리 학습 DAY 1~2 (본문 ❶~❺). 지문은 일부 바꾼 것이 있어요. 내용 일치 문항의 선택지는 본문 표현을 어려운 어휘로 바꿔 썼고, 표 수 계산이 필요한 선택지도 있어요.</p>

  <div class="qs">'''+''.join(qs)+'''  </div>
'''+SW+'''  <div class="foot"><span>NE능률(오선영) 영어Ⅱ Lesson 3 · 본문 ❶~❺ · 원문 일부 변형</span><span>대진고 2학년 영어 · Wrap-up</span></div>
</section>

<section class="page">
  <div class="top"><span>능률 L3 본문 Wrap-up · <b>정답과 해설</b></span><span>대진고등학교 2학년</span></div>
  <div class="title"><div class="g">영어Ⅱ</div><h1>정답과 해설</h1><div class="when">선택형 80점 · 서술형 20점</div></div>
  '''+key+SK+'''
  <div class="foot"><span>정답 분포 ①~⑤ 각 4개</span><span>대진고 2학년 영어 · Wrap-up</span></div>
</section>
</main>
''')
open('wrapup-daejin-ne-oh-L3.html','w',encoding='utf-8').write(html)
