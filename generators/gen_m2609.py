import sys, html
sys.path.insert(0, '/tmp/claude-0/-home-claude/a9e3e882-1f02-5d62-8f70-aced81bc59d2/scratchpad')
from gencommon import *

def esc(s): return html.escape(s, quote=False)
def box(t): return '<span class="exam-box en">' + t + '</span>'
def exam(no, stem, body_html, extra=''):
    return '<b>' + str(no) + '. ' + stem + '</b>' + extra + box(body_html)
def body(T): return ' '.join(esc(r[0]) for r in T)
def sec(t): return [['#', t, '']]
def rows(T): return [['', a, b] for a, b in T]

T24 = [
 ("Progressive educators and librarians are developing curricula to teach what we might call attention literacy.", "진보적인 교육자들과 사서들은 우리가 주의력 문해력이라 부를 만한 것을 가르치기 위한 교육과정을 개발하고 있다."),
 ("This means helping students recognize, for example, how the architecture of a social media feed or a news site is deliberately designed to distract or provoke them.", "예를 들어, 이것은 소셜 미디어 피드나 뉴스 사이트의 구조가 학생들을 산만하게 하거나 자극하도록 어떻게 의도적으로 설계되었는지 그들이 인식하도록 돕는 것을 의미한다."),
 ("Classes in media literacy traditionally cover how to evaluate the credibility of sources — now they also include recognizing clickbait, understanding the role of algorithms in what content is served up, and observing one's own patterns of distraction.", "미디어 문해력 수업은 전통적으로 어떻게 정보원의 신뢰성을 평가하는지 다루었지만, 이제는 클릭베이트를 인식하고, 어떤 콘텐츠가 제공되는 것에 있어 알고리즘의 역할을 이해하며, 자신만의 주의 산만 패턴을 관찰하는 것도 포함한다."),
 ("A student might be tasked with tracking how many times they switch tasks or check their phone in an hour of homework, to raise self-awareness about fragmentation.", "학생은 (주의력) 파편화에 대한 자기 인식을 높이기 위해, 숙제하는 한 시간에 얼마나 여러 번 작업을 전환하거나 전화기를 확인하는지 추적하는 과제를 받을 수도 있다."),
 ("Another lesson might involve unpacking the design of popular apps: Why does an app use infinite scrolling instead of pages?", "또 다른 수업은 인기 앱들의 설계를 분석하는 것을 포함할 수 있다. 왜 앱은 페이지 대신 무한 스크롤을 사용할까?"),
 ("Why do notifications appear with specific colors and sounds?", "왜 알림은 특정한 색상과 소리로 나타날까?"),
 ("By treating these as deliberate design choices (often rooted in psychology and profit motives), young people become more critical users rather than passive consumers.", "이러한 것들을 (흔히 심리학과 이윤 동기에 뿌리를 둔) 의도적인 디자인 선택으로 취급함으로써, 젊은이들은 수동적인 소비자가 아니라 더 비판적인 사용자가 된다."),
]
T29 = [
 ("Capitalism is not a system where cash is everywhere but rather one in which islands of cash exchange exist within oceans of cheap — or potentially cheap — natures.", "자본주의는 현금이 어디에나 존재하는 시스템이라기보다는, 값싼 혹은 잠재적으로 값싼 만물의 바다 안에 현금 교환이라는 섬들이 존재하는 시스템이다."),
 ("Reproducing life within the cash nexus is expensive, and it grows more expensive over time.", "현금 거래 관계 내에서 삶을 재생산하는 것은 비싸고, 시간이 흐를수록 그것은 더 비싸진다."),
 ("Workers' wages can be frozen, even rolled back, but in the end inequality leads to crises of the kind we've recently seen bring about populist protests in the United States and the United Kingdom.", "노동자의 임금은 동결되거나 심지어 삭감될 수 있지만, 결국 불평등은 우리가 최근 미국과 영국에서 포퓰리스트 시위를 발생시켰다고 목격한 것과 같은 종류의 위기를 초래한다."),
 ("Workers demand dignity, and their labor becomes expensive.", "노동자들은 존엄성을 요구하고, 그들의 노동력은 비싸진다."),
 ("Production processes burn through an island, and energy is no longer cheap.", "생산 과정은 섬(현금 교환의 섬)을 고갈시키며, 에너지는 더 이상 값싸지 않게 된다."),
 ("The climate changes, and crops can no longer grow as abundantly as they once did.", "기후가 변화하고, 작물은 한때 그랬던 것처럼 더 이상 풍부하게 자라지 않는다."),
 ("Frontiers are so important in these processes because they offer places where the new cheap things can be seized — and the cheap work of humans and other natures can be forcefully taken.", "이러한 과정에서 미개척 영역이 중요한데, 왜냐하면 그것이 새로운 값싼 것들이 확보될 수 있는 장소를 제공하기 때문이다. 즉, 값싼 인간의 노동력과 다른 만물이 강제로 취해질 수 있다는 것이다."),
]
T30 = [
 ('Some people are more likely to cheat and steal after purchasing "eco-friendly" products, probably because they feel licensed to do so since they morally account the "eco-friendly" choice as a "good" deed.', "어떤 사람들은 '친환경' 제품을 구매한 후에 속이거나 훔칠 가능성이 더 높은데, 아마도 그들은 '친환경적' 선택을 '착한' 행위라고 도덕적으로 간주하여 그렇게 할 자격이 있다고 느끼기 때문일 것이다."),
 ("Moral licensing has also been observed in the context of cooperation for the good of the environment.", "도덕적 허가는 환경의 이익을 위한 협조의 맥락 안에서도 관찰되어 왔다."),
 ('When people are reminded of deeds they have done that they know were harmful to the environment, they might be left with a feeling of "eco-guilt."', "사람들이 자신이 해왔던 환경에 해롭다고 알고 있는 행동들을 떠올릴 때, 그들에게는 '환경에 대한 죄책감'이라는 감정이 남을 수 있다."),
 ("People who experience eco-guilt seek pro-environmental actions to compensate for this guilt and restore balance.", "환경에 대한 죄책감을 경험하는 사람들은 이 죄책감을 보상하고 균형을 회복하기 위한 친환경적인 행동을 추구한다."),
 ('In their search for such a balance, people are inclined to believe in "quick-fixes," because they want to re-establish the moral balance and escape the guilt as quickly and easily as possible.', "이러한 균형을 찾는 과정에서 사람들은 '임시방편'을 믿으려 하는 경향이 있는데, 이는 그들이 도덕적 균형을 재정립하고 가능한 한 빠르고 쉽게 죄책감을 벗어나고 싶어 하기 때문이다."),
 ("In the same way that people may change their attitudes to reduce inconsistencies between attitudes and behavior, people may also change their evaluation of past environmentally burdening behaviors and future environmentally friendly behaviors.", "사람들이 태도와 행동 사이의 불일치를 줄이기 위해 태도를 바꿀 수 있는 것과 같은 방식으로, 사람들은 과거의 환경에 부담을 주는 행동과 미래의 친환경적 행동에 대한 평가를 바꿀 수도 있다."),
 ("For instance, people are more likely to sign a petition addressing environmental damage after viewing evidence of human-caused environmental damage.", "예를 들어, 사람들은 인간이 유발한 환경 훼손의 증거를 본 후에 환경 훼손을 다루는 청원서에 서명할 가능성이 더 높다."),
]
T34 = [
 ("When we focus on the obvious aspects of media, we miss the changes that accumulate over time but are not apparent day to day.", "우리가 매체의 분명한 측면에 집중할 때, 우리는 시간이 흐름에 따라 축적되지만 하루하루 뚜렷하게 보이지 않는 변화를 놓친다."),
 ("Most of us notice the obvious aspects of a new medium or technology while missing the more subtle aspects.", "우리들 대부분은 더 미묘한 측면들을 놓치는 동안 새로운 매체나 기술의 분명한 측면은 알아차린다."),
 ("Take, for example, the microwave oven.", "예를 들어, 전자레인지를 보라."),
 ("It was introduced in the early 1980s and revolutionized food preparation.", "그것은 1980년대 초반에 도입되었고 음식 준비 과정에 혁명을 일으켰다."),
 ("Traditionally, one person spent the better part of an afternoon fixing an evening meal for a family.", "전통적으로, 한 사람이 가족을 위한 저녁 식사를 준비하느라 오후의 대부분을 보냈다."),
 ("Now, it was possible to prepare foods very quickly, and this shortening of preparation time was liberating for the cooks in the family, most of whom tended to be women.", "이제 음식을 매우 빠르게 준비하는 것이 가능해졌고, 이러한 준비 시간의 단축은 대부분 여성인 경향이 있었던 가족 내 요리사들을 해방시켰다."),
 ("But the short-term, obvious implications of greater convenience made it easy to overlook the long-term implications of no longer having one person fix food for the family to eat together at an evening meal.", "하지만 더 큰 편리함이라는 단기적이고 분명한 영향은 더 이상 한 사람이 가족이 저녁 식사에서 함께 먹기 위해 음식을 준비하지 않게 되는 것의 장기적인 영향을 간과하기 쉽게 만들었다."),
 ("As time went on, fewer and fewer families sat down together to eat dinner.", "시간이 흐르면서, 점점 더 적은 수의 가족들이 저녁을 먹기 위해 함께 둘러앉았다."),
 ("Meals that took a long time to prepare became a luxury of the past, except perhaps for special occasions.", "아마도 특별한 경우를 제외하고는, 준비하는 데 오랜 시간이 걸리는 식사는 과거의 사치품이 되었다."),
 ("The effects of the microwave oven on family life were not anticipated and would have been difficult to foresee.", "전자레인지가 가정생활에 미친 영향은 예상되지 못했으며, 예견하기도 어려웠을 것이다."),
]
T38 = [
 ("Environmental psychologists make a distinction between the physical measurement of density (how many people are in a particular space) and crowding (the psychological feeling of not having enough space).", "환경심리학자들은 밀도(특정 장소에 얼마나 많은 사람들이 있는가)의 물리적 측정과 혼잡성(공간이 충분치 않다는 심리적 감정)을 구분한다."),
 ("Usually, high density is needed for the phenomenon of crowding, which makes people experience sensory overload, a lack of control, and rising stress and anxiety.", "대개 혼잡 현상에는 높은 밀도가 필요하고, 이는 사람들이 감각적 과부하, 통제 결여와 증가하는 스트레스와 불안을 경험하게 한다."),
 ("However, some psychologists see crowding as neutral rather than invariably negative, and believe that people's moods and behaviors intensify as density increases.", "하지만 몇몇 심리학자들은 혼잡성을 변함없이 부정적인 것으로 보기보다 중립적으로 보고, 밀도가 올라감에 따라 사람들의 기분과 행동도 강화된다고 믿는다."),
 ("So if an individual is looking forward to a concert, say, the feeling of crowding enhances their enjoyment of the performance.", "그래서, 예를 들어, 한 개인이 콘서트를 기대하고 있다면, 혼잡성의 느낌은 공연의 즐거움을 높인다."),
 ("But if they are dreading an event, crowding will make the person's experience of it even worse.", "그러나 만약 그들이 행사를 두려워하고 있다면, 혼잡성은 그것을 겪는 개인의 경험을 훨씬 더 나쁘게 만들 것이다."),
 ("Put into a community setting, crowding may accentuate the dominant behavior — an aggressive group may turn violent as density rises.", "공동체 환경에 놓이면, 혼잡성은 지배적 행동을 두드러지게 할 수 있는데, 공격적인 집단은 밀도가 올라감에 따라 폭력적으로 변할 수 있다."),
 ("Conversely, creating positive social spaces such as parks and pedestrian areas in high-density urban environments may help to lift the general mood and defuse tension.", "반대로 높은 밀도의 도시 환경에 공원이나 보행 구역과 같은 긍정적인 사회적 공간을 만드는 것은 전체적인 기분을 올리고 긴장감을 완화하는 것을 도울 수 있다."),
]
T40 = [
 ("Our adult brains retain a preference for perpetuating good, fair behavior.", "우리의 성인 뇌는 선하고 공정한 행동을 영속시키는 것에 대한 선호를 유지한다."),
 ("Simply perceiving ourselves as people who do good deeds and behaving accordingly motivates us to do greater good in the future.", "단순히 우리 자신을 좋은 행위를 하는 사람으로 인식하고 그에 맞춰 행동하는 것만으로도 우리가 미래에 더 큰 선을 행하도록 동기를 부여한다."),
 ("In one paid study of one hundred college students, subjects who wrote down a list of past good deeds and were then asked to donate money to a charity gave, on average, over half the earnings they'd made from the study — almost twice as much as those who had been instructed to recall previous bad deeds.", "100명의 대학생을 대상으로 한 보수가 지급되는 한 연구에서, 과거 좋은 행위의 목록을 작성한 후 자선 단체에 기부할 것을 요청받은 피실험자들은 평균적으로 연구를 통해 번 수익의 절반 이상을 기부했다. 이는 이전의 나쁜 행위를 회상하도록 지시받았던 사람들보다 거의 두 배였다."),
 ("In addition, subjects who'd taken pains to describe not only how they'd been nice to others but how people responded were likely to donate significantly less than those who focused purely on the actions themselves.", "게다가, 자신이 타인에게 얼마나 친절했는지뿐만 아니라 사람들이 어떻게 반응했는지까지 공들여 묘사했던 피실험자들은, 순수하게 행위 그 자체에만 초점을 둔 사람들보다 훨씬 적게 기부하는 경향이 있었다."),
 ("In other words, people who seemed concerned about appearances (e.g., the impact of their good deed, as much as the deed itself) were less generous than those who cared more about doing good for its own sake.", "다시 말해서, 겉모습(예를 들어, 좋은 행위 그 자체만큼이나 자신의 좋은 행위가 미칠 영향력)에 신경을 쓰는 것처럼 보이는 사람들은, 선을 그 자체를 위해 행하는 것에 더 마음을 쓰는 사람들보다 덜 관대했다."),
]
T41 = [
 ('The concept of "choice architecture," popularized in behavioral economics, highlights how the design of the environment in which choices are made can significantly influence the decisions people make.', "행동 경제학에서 대중화된 '선택 구조'라는 개념은 선택이 이루어지는 환경의 설계가 사람들이 내리는 결정에 어떻게 큰 영향을 미칠 수 있는지를 강조한다."),
 ("Algorithms are, in essence, sophisticated architects of our digital environments.", "알고리즘은 본질적으로 우리 디지털 환경의 정교한 설계자이다."),
 ("By curating what we see, what we are recommended, and what options are presented to us, they subtly, and sometimes not so subtly, nudge us towards particular paths.", "우리가 무엇을 보고, 무엇을 추천받으며, 어떤 옵션이 우리에게 제시되는지를 선별함으로써, 그것들은 미묘하게, 때로는 그렇게 미묘하지 않게 우리를 특정 경로로 향하도록 가볍게 자극한다."),
 ("While nudges can be used for beneficial purposes, such as encouraging healthier habits, they also carry the potential for manipulation, particularly when the underlying objectives of the architects are not aligned with the well-being or autonomy of the individual.", "넛지는 더 건강한 습관을 권장하는 것과 같이 유익한 목적으로 사용될 수 있지만, 특히 설계자의 잠재적인 목표가 개인의 복지나 자율성과 일치하지 않을 때 그것들은 조작의 가능성 또한 내포하고 있다."),
 ("The question then becomes: how can we cultivate and protect our human agency in an increasingly algorithmic world?", "그러면 질문은 다음과 같다. 점점 더 알고리즘화되는 세상에서 우리는 어떻게 인간의 주체성을 기르고 보호할 수 있을까?"),
 ("It requires a conscious effort to maintain critical engagement with the technologies we use.", "그것은 우리가 사용하는 기술과 비판적인 관계를 유지하려는 의식적인 노력을 필요로 한다."),
 ("It means actively seeking out diverse perspectives, challenging algorithmic recommendations, and making deliberate choices that go against the predicted grain.", "이는 적극적으로 다양한 관점을 찾고, 알고리즘의 추천에 도전하며, 예측된 흐름에 반하는 의도적인 선택을 하는 것을 의미한다."),
 ("It involves cultivating a healthy skepticism towards the seemingly objective outputs of algorithms and remembering that these systems are designed by humans with specific goals, and that their data is a reflection of past realities, not necessarily a prescription for future flourishing.", "그것은 알고리즘의 겉보기에 객관적인 결과물에 대해 건전한 회의론을 기르고, 이러한 시스템이 특정 목표를 가진 인간에 의해 설계되었으며, 그 데이터는 과거 현실의 반영일 뿐 반드시 미래의 번영을 위한 처방은 아니라는 점을 기억하는 것을 포함한다."),
]

def ilchi(n, T, neg, opts, ex, per):
    q = "글의 내용과 일치하지 <u>않는</u> 것은?" if neg else "글의 내용과 <u>일치하는</u> 것은?"
    return {'n': n, 'q': exam(n, q, body(T)), 'opts': opts, 'ex': ex, 'per': per}

def day(vocab, real, **kw):
    st = steps(vocab=vocab, **kw)
    st.insert(1, {'type': 'mc', 'title': '실전 문항', 'guide': '시험지 원문항이에요. 지문을 읽고 답을 고르세요.', 'items': real})
    return st

# ───── 실전 문항 원문 ─────
Q29 = ("Capitalism is not a system where cash is everywhere but rather ①<u>one</u> in which islands of cash exchange exist within oceans of cheap — or potentially cheap — natures. "
       "②<u>Reproducing</u> life within the cash nexus is expensive, and it grows more expensive over time. Workers' wages can be frozen, even rolled back, but in the end inequality leads to crises of the kind we've recently seen ③<u>bring</u> about populist protests in the United States and the United Kingdom. "
       "Workers demand dignity, and their labor becomes expensive. Production processes burn through an island, and energy is no longer cheap. The climate changes, and crops can no longer grow as ④<u>abundantly</u> as they once did. "
       "Frontiers are so important in these processes because they offer places ⑤<u>which</u> the new cheap things can be seized — and the cheap work of humans and other natures can be forcefully taken.<br><small>*cash nexus: 현금 거래 관계</small>")
Q30 = ("Some people are more likely to cheat and steal after purchasing \"eco-friendly\" products, probably because they feel licensed to do so since they morally account the \"eco-friendly\" choice as a \"good\" deed. "
       "Moral licensing has also been ①<u>observed</u> in the context of cooperation for the good of the environment. When people are reminded of deeds they have done that they know were harmful to the environment, they might be left with a feeling of \"eco-guilt.\" "
       "People who experience eco-guilt seek pro-environmental actions to compensate for this guilt and ②<u>restore</u> balance. In their search for such a balance, people are ③<u>reluctant</u> to believe in \"quick-fixes,\" because they want to re-establish the moral balance and escape the guilt as quickly and easily as possible. "
       "In the same way that people may change their attitudes to reduce inconsistencies between attitudes and behavior, people may also change their ④<u>evaluation</u> of past environmentally burdening behaviors and future environmentally friendly behaviors. "
       "For instance, people are ⑤<u>more</u> likely to sign a petition addressing environmental damage after viewing evidence of human-caused environmental damage.<br><small>*petition: 청원서</small>")
Q34 = esc(T34[0][0]).replace("accumulate over time but are not apparent day to day", "<u>　　　　　　　　　　</u>") + ' ' + body(T34[1:])
Q38 = ("Environmental psychologists make a distinction between the physical measurement of density (how many people are in a particular space) and crowding (the psychological feeling of not having enough space). ( ① ) "
       "Usually, high density is needed for the phenomenon of crowding, which makes people experience sensory overload, a lack of control, and rising stress and anxiety. ( ② ) "
       "However, some psychologists see crowding as neutral rather than invariably negative, and believe that people's moods and behaviors intensify as density increases. ( ③ ) "
       "But if they are dreading an event, crowding will make the person's experience of it even worse. ( ④ ) Put into a community setting, crowding may accentuate the dominant behavior — an aggressive group may turn violent as density rises. ( ⑤ ) "
       "Conversely, creating positive social spaces such as parks and pedestrian areas in high-density urban environments may help to lift the general mood and defuse tension.<br><small>*accentuate: 두드러지게 하다 **defuse: 완화하다</small>")
G38 = box(esc(T38[3][0]))
S40 = box("According to the study, the motivation to do good deeds was more <b>(A)</b>＿＿＿ in those who recalled their past virtues and those who focused purely on their good deeds than those who recalled their previous bad deeds and those who seemed highly <b>(B)</b>＿＿＿ of the appearances of their deeds.")
Q41 = (body(T41[:4]).replace("sophisticated architects", "<b>(a)</b><u>sophisticated</u> architects").replace("towards particular paths", "towards <b>(b)</b><u>particular</u> paths") + '<br><br>' +
       body(T41[4:]).replace("a conscious effort", "a <b>(c)</b><u>conscious</u> effort").replace("challenging algorithmic", "<b>(d)</b><u>following</u> algorithmic").replace("is a reflection", "is a <b>(e)</b><u>reflection</u>") + '<br><small>*nudge: 가볍게 자극하다</small>')

# ═════════════ DAY 1 · 24, 29 ═════════════
d1 = day(
 vocab=[['progressive', '진보적인', 24], ['curriculum (pl. curricula)', '교육과정', 24], ['literacy', '문해력', 24], ['architecture', '구조, 설계', 24],
        ['deliberately', '의도적으로', 24], ['distract', '산만하게 하다', 24], ['provoke', '자극하다, 도발하다', 24], ['credibility', '신뢰성', 24],
        ['serve up', '제공하다', 24], ['distraction', '주의 산만', 24], ['be tasked with', '~의 임무를 맡다', 24], ['fragmentation', '파편화', 24],
        ['unpack', '분석하다, 풀어내다', 24], ['infinite', '무한한', 24], ['notification', '알림', 24], ['rooted in', '~에 뿌리를 둔', 24],
        ['profit motive', '이윤 동기', 24], ['passive', '수동적인', 24], ['capitalism', '자본주의', 29], ['potentially', '잠재적으로', 29],
        ['reproduce', '재생산하다', 29], ['wage', '임금', 29], ['freeze', '동결하다', 29], ['roll back', '인하하다, 되돌리다', 29],
        ['inequality', '불평등', 29], ['bring about', '초래하다', 29], ['populist', '대중 영합적인', 29], ['dignity', '존엄성', 29],
        ['burn through', '다 써 버리다', 29], ['abundantly', '풍부하게', 29], ['frontier', '미개척 영역, 변경', 29], ['seize', '빼앗다, 장악하다', 29],
        ['forcefully', '강제로', 29]],
 real=[
  {'n': 24, 'q': exam(24, '다음 글의 제목으로 가장 적절한 것은?', body(T24)),
   'opts': ["Raising Media Awareness: Noticing Intended Manipulations", "Can Students Learn to Identify the Credibility of Information?", "Application Developers' Focus on Users' Activeness", "The Dark Side of Algorithms: A Threat to Privacy", "Using Social Media to Communicate: Treasure or Poison?"],
   'ex': "정답 ② · 매체가 학생을 산만하게 하도록 '의도적으로 설계된(deliberately designed)' 방식을 알아차리게 하는 주의력 문해력 교육 → 의도된 조작을 알아차리기",
   'per': [["미디어 인식 높이기: 의도된 조작 알아차리기", ["is deliberately designed to distract or provoke them", "By treating these as deliberate design choices"], "의도적 설계를 알아차려 비판적 사용자가 됨 → 정답"],
           ["학생들은 정보의 신뢰성을 판별하는 법을 배울 수 있는가?", "traditionally cover how to evaluate the credibility of sources", "신뢰성 평가는 '전통적인' 수업 내용일 뿐, 핵심이 아님 (오답률 1위 매력 선지)"],
           ["앱 개발자들의 사용자 능동성에 대한 관심", "often rooted in psychology and profit motives", "개발자는 오히려 이윤을 위해 산만하게 만듦"],
           ["알고리즘의 어두운 면: 사생활 위협", "", "사생활 이야기는 없음"],
           ["소통을 위한 소셜 미디어: 보물인가 독인가?", "", "소통 수단으로서의 SNS 평가가 아님"]]},
  {'n': 29, 'q': exam(29, '다음 글의 밑줄 친 부분 중, 어법상 <u>틀린</u> 것은?', Q29),
   'opts': ["⑤ which", "① one", "② Reproducing", "③ bring", "④ abundantly"],
   'ex': "정답 ⑤ which → where (in which). places 뒤에 완전한 절(the new cheap things can be seized)이 오므로 관계부사",
   'per': [["", "they offer places where the new cheap things can be seized", "뒤에 주어·동사가 다 갖춰진 완전한 절 → where / in which"],
           ["", "but rather one in which islands of cash exchange exist", "a system(단수 가산명사) 반복 → 부정대명사 one ✓"],
           ["", "Reproducing life within the cash nexus is expensive", "주어 자리 동명사 → 단수동사 is ✓"],
           ["", "we've recently seen bring about populist protests", "지각동사 see + O(crises) + 동사원형 ✓ (O는 앞의 crises, 관계대명사 생략)"],
           ["", "crops can no longer grow as abundantly as they once did", "동사 grow 수식 → 부사 abundantly ✓"]]},
 ],
 pickv=[
  ("Progressive educators and librarians are developing curricula to teach what we might call attention {literacy|literature}.", "literacy 문해력 vs literature 문학"),
  ("This means helping students recognize, for example, how the architecture of a social media feed or a news site is {deliberately|accidentally} designed to distract or provoke them.", "설계는 '의도적으로' → deliberately"),
  ("Classes in media literacy traditionally cover how to evaluate the {credibility|incredibility} of sources — now they also include recognizing clickbait, understanding the role of algorithms in what content is served up, and observing one's own patterns of distraction.", "정보원의 '신뢰성' 평가 → credibility"),
  ("A student might be tasked with tracking how many times they switch tasks or check their phone in an hour of homework, to raise self-awareness about {fragmentation|concentration}.", "작업 전환·폰 확인 = 주의가 쪼개짐 → fragmentation"),
  ("By treating these as {deliberate|accidental} design choices (often rooted in psychology and profit motives), young people become more critical users rather than passive consumers.", "이윤 동기에 뿌리 → 의도적인(deliberate) 선택"),
  ("By treating these as deliberate design choices (often rooted in psychology and profit motives), young people become more critical users rather than {passive|active} consumers.", "critical users와 대비 → passive"),
  ("Workers' wages can be frozen, even rolled back, but in the end {inequality|equality} leads to crises of the kind we've recently seen bring about populist protests in the United States and the United Kingdom.", "위기와 시위를 초래하는 것 → inequality 불평등"),
  ("Workers demand {dignity|dignify}, and their labor becomes expensive.", "명사 자리 dignity 존엄성 (dignify는 동사)"),
  ("The climate changes, and crops can no longer grow as {abundantly|scarcely} as they once did.", "no longer와 함께 '예전만큼 풍부하게' → abundantly"),
  ("Frontiers are so important in these processes because they offer places where the new cheap things can be {seized|ceased} — and the cheap work of humans and other natures can be forcefully taken.", "seize 빼앗다 vs cease 중단하다"),
 ],
 tf=[
  ["Educators are designing courses to cultivate what could be termed attention literacy.", True, "design courses = develop curricula · be termed = be called", 24, "developing curricula to teach what we might call attention literacy"],
  ["Media literacy classes now focus solely on judging the reliability of sources.", False, "solely 오로지 · reliability = credibility → 이제는 클릭베이트·알고리즘·주의 산만 관찰도 포함", 24, "now they also include recognizing clickbait"],
  ["Students may be asked to monitor how often they switch tasks during homework.", True, "monitor = track · how often = how many times", 24, "tracking how many times they switch tasks"],
  ["The writer believes app features like infinite scrolling are accidental.", False, "accidental 우연한 → 의도적인 디자인 선택(deliberate design choices)", 24, "By treating these as deliberate design choices"],
  ["Under capitalism, cash exchange occurs everywhere.", False, "현금이 어디에나 있는 체제가 아니라, 값싼 것들의 바다 속 현금 교환의 섬", 29, "Capitalism is not a system where cash is everywhere"],
  ["Sustaining life within the cash nexus becomes costlier as time passes.", True, "sustain ≒ reproduce · costlier = more expensive · as time passes = over time", 29, "it grows more expensive over time"],
  ["Inequality eventually triggers crises that can provoke populist protests.", True, "eventually = in the end · trigger = lead to · provoke = bring about", 29, "in the end inequality leads to crises"],
  ["Frontiers matter little in capitalism.", False, "matter little 별로 중요하지 않다 → 매우 중요(so important)", 29, "Frontiers are so important in these processes"],
 ],
 ilchi=[
  ilchi(24, T24, True, ["Attention literacy classes encourage students to remain passive consumers of media.", "The design of news sites and social media feeds can be intended to distract users.", "Media literacy classes have traditionally dealt with assessing the credibility of sources.", "Students might keep a record of how frequently they check their phones while studying.", "Many app design features stem from psychology and profit motives."],
        "정답: remain passive consumers 수동적 소비자로 남다 → 오히려 비판적 사용자가 됨\n· be intended to ~하도록 의도되다 = be deliberately designed to\n· deal with = cover · assess = evaluate\n· keep a record of = track · frequently = many times\n· stem from = be rooted in",
        [["주의력 문해력 수업은 학생들이 수동적 소비자로 남도록 장려한다.", "young people become more critical users rather than passive consumers", "불일치"],
         ["뉴스 사이트와 SNS 피드의 설계는 사용자를 산만하게 하도록 의도될 수 있다.", "is deliberately designed to distract or provoke them", "일치"],
         ["미디어 문해력 수업은 전통적으로 정보원의 신뢰성 평가를 다뤄 왔다.", "traditionally cover how to evaluate the credibility of sources", "일치"],
         ["학생들은 공부하면서 휴대폰을 얼마나 자주 확인하는지 기록할 수도 있다.", "tracking how many times they switch tasks or check their phone", "일치"],
         ["많은 앱 디자인 요소는 심리학과 이윤 동기에서 비롯된다.", "often rooted in psychology and profit motives", "일치"]]),
  ilchi(29, T29, False, ["Workers' demand for dignity makes their labor more costly.", "Capitalism is a system in which cash is present everywhere.", "Workers' wages can never be reduced under capitalism.", "Crops now grow more abundantly than before.", "Energy becomes cheaper as production processes continue."],
        "정답: demand for dignity 존엄성 요구 · costly = expensive\n· present everywhere → 어디에나 있는 체제가 아님(not a system where cash is everywhere)\n· never be reduced → 동결되거나 삭감될 수 있음(rolled back)\n· more abundantly → 더 이상 풍부하게 자라지 않음\n· cheaper → 더 이상 값싸지 않음(no longer cheap)",
        [["노동자의 존엄성 요구가 노동력을 더 비싸게 만든다.", "Workers demand dignity, and their labor becomes expensive", "일치"],
         ["자본주의는 현금이 어디에나 존재하는 체제이다.", "Capitalism is not a system where cash is everywhere", "불일치"],
         ["자본주의에서 노동자의 임금은 결코 깎일 수 없다.", "can be frozen, even rolled back", "불일치"],
         ["작물이 지금 예전보다 더 풍부하게 자란다.", "crops can no longer grow as abundantly as they once did", "불일치"],
         ["생산 과정이 계속되며 에너지가 더 싸진다.", "energy is no longer cheap", "불일치"]]),
 ],
 pickg=[
  ("Progressive educators and librarians are developing curricula to teach {what|that} we might call attention literacy.", "teach의 목적어 + call의 목적어가 빠진 절 → 관계대명사 what"),
  ("This means {helping|to help} students recognize, for example, how the architecture of a social media feed or a news site is deliberately designed to distract or provoke them.", "mean -ing: ~하는 것을 의미하다 (mean to: ~할 작정이다)"),
  ("This means helping students recognize, for example, how the architecture of a social media feed or a news site {is|are} deliberately designed to distract or provoke them.", "주어 the architecture(단수) → is"),
  ("Classes in media literacy traditionally cover how to evaluate the credibility of sources — now they also include recognizing clickbait, understanding the role of algorithms in what content {is served|serves} up, and observing one's own patterns of distraction.", "콘텐츠가 '제공되는' 수동"),
  ("A student might be tasked with {tracking|track} how many times they switch tasks or check their phone in an hour of homework, to raise self-awareness about fragmentation.", "전치사 with + 동명사"),
  ("By treating these as deliberate design choices (often {rooted|rooting} in psychology and profit motives), young people become more critical users rather than passive consumers.", "'뿌리를 둔' 수동 → rooted"),
  ("Capitalism is not a system where cash is everywhere but rather {one|it} in which islands of cash exchange exist within oceans of cheap — or potentially cheap — natures.", "a system 반복 + 뒤에 수식어 → 부정대명사 one"),
  ("{Reproducing|Reproduce} life within the cash nexus is expensive, and it grows more expensive over time.", "주어 자리 → 동명사"),
  ("Workers' wages can be frozen, even rolled back, but in the end inequality leads to crises of the kind we've recently seen {bring|to bring} about populist protests in the United States and the United Kingdom.", "지각동사 see + O + 동사원형"),
  ("The climate changes, and crops can no longer grow as {abundantly|abundant} as they once did.", "동사 grow 수식 → 부사"),
  ("Frontiers are so important in these processes because they offer places {where|which} the new cheap things can be seized — and the cheap work of humans and other natures can be forcefully taken.", "뒤에 완전한 절 → 관계부사 where ★29번 정답"),
  ("Frontiers are so important in these processes because they offer places where the new cheap things can be seized — and the cheap work of humans and {other|another} natures can be forcefully taken.", "복수명사 natures 앞 → other"),
 ],
 verb=[
  ("This means helping students recognize, for example, how the architecture of a social media feed or a news site is deliberately ___ to distract or provoke them.", 'design', ['designed'], "be designed to ~하도록 설계되다"),
  ("A student might be ___ with tracking how many times they switch tasks or check their phone in an hour of homework, to raise self-awareness about fragmentation.", 'task', ['tasked'], "be tasked with ~의 임무를 맡다"),
  ("By ___ these as deliberate design choices (often rooted in psychology and profit motives), young people become more critical users rather than passive consumers.", 'treat', ['treating'], "By + 동명사"),
  ("___ life within the cash nexus is expensive, and it grows more expensive over time.", 'reproduce', ['Reproducing', 'To reproduce'], "주어 자리 동명사(to부정사)"),
  ("Workers' wages can be ___, even rolled back, but in the end inequality leads to crises of the kind we've recently seen bring about populist protests in the United States and the United Kingdom.", 'freeze', ['frozen'], "freeze - froze - frozen, 수동태"),
  ("Workers' wages can be frozen, even rolled back, but in the end inequality leads to crises of the kind we've recently ___ bring about populist protests in the United States and the United Kingdom.", 'see', ['seen'], "현재완료 have p.p."),
  ("Frontiers are so important in these processes because they offer places where the new cheap things can be ___ — and the cheap work of humans and other natures can be forcefully taken.", 'seize', ['seized'], "조동사 + be + p.p."),
 ],
 error=[
  ("Progressive educators and librarians [[are developing]] curricula [[to teach]] [[that]] we might [[call]] attention literacy.", 2, 'what', "teach의 목적어 역할 + 불완전한 절 → what"),
  ("This means [[to help]] students [[recognize]], for example, how the architecture of a social media feed or a news site [[is]] deliberately [[designed]] to distract or provoke them.", 0, 'helping', "mean -ing (~하는 것을 의미하다)"),
  ("By treating these as deliberate design choices (often [[rooting]] in psychology and profit motives), young people [[become]] more [[critical]] users rather than [[passive]] consumers.", 0, 'rooted', "'뿌리를 둔' 수동 → rooted"),
  ("Capitalism is not a system [[where]] cash is everywhere but rather [[it]] in which islands of cash exchange [[exist]] within oceans of [[cheap]] — or potentially cheap — natures.", 1, 'one', "수식어가 붙는 대명사 → one"),
  ("[[Reproducing]] life within the cash nexus [[are]] expensive, and it grows more [[expensive]] over time. Workers' wages can be [[frozen]], even rolled back.", 1, 'is', "동명사 주어 → 단수동사"),
  ("The climate changes, and crops can no longer grow as [[abundantly]] as they once [[did]]. Frontiers are so important in these processes because they offer places [[which]] the new cheap things can be [[seized]].", 2, 'where', "뒤에 완전한 절 → where"),
 ],
 scr=[(T24[0][0], T24[0][1]), (T24[5][0], T24[5][1]), (T29[1][0], T29[1][1]), (T29[3][0], T29[3][1]), (T29[5][0], T29[5][1])],
 order=[
  ([T24[0][0], T24[1][0], T24[2][0], T24[3][0]], ["교육자들이 주의력 문해력 교육과정을 개발 중", "의도적 설계를 인식하도록 돕는 것", "전통적 신뢰성 평가 + 클릭베이트·알고리즘·주의 산만 관찰", "예: 숙제 중 작업 전환·폰 확인 횟수 추적"]),
  ([T24[3][0], T24[4][0], T24[5][0], T24[6][0]], ["작업 전환 횟수 추적", "또 다른 수업: 무한 스크롤은 왜?", "알림 색과 소리는 왜?", "의도적 설계로 보면 비판적 사용자가 됨"]),
  ([T29[0][0], T29[1][0], T29[2][0], T29[3][0]], ["자본주의 = 값싼 것들의 바다 속 현금 교환의 섬", "현금 관계 속 삶의 재생산은 점점 비싸짐", "임금을 묶어도 결국 불평등이 위기·시위 초래", "노동자가 존엄성 요구 → 노동력 비싸짐"]),
  ([T29[4][0], T29[5][0], T29[6][0]], ["생산이 섬을 소진 → 에너지 비싸짐", "기후 변화 → 작물 감소", "그래서 새 값싼 것을 빼앗을 미개척 영역이 중요"]),
 ],
 insert=[
  ([T24[1][0], T24[2][0], T24[3][0], T24[4][0]], 2, ["의도적 설계 인식", "수업 내용 확장", "예: 작업 전환 추적 (A student ~)", "또 다른 수업(Another lesson)"], "Another lesson의 앞에는 첫 번째 수업 예시(A student ~)가 와야 한다."),
  ([T29[2][0], T29[3][0], T29[4][0], T29[5][0]], 1, ["불평등이 위기 초래", "노동력이 비싸짐", "에너지가 비싸짐", "작물이 줄어듦"], "값싼 것들이 하나씩 비싸지는 흐름: 노동 → 에너지 → 작물"),
 ],
 odd=[
  ([T24[2][0], T24[3][0], "Many schools now provide students with free laptops for online classes.", T24[4][0]], 2, "노트북 지급 → 주의력 문해력 수업 내용과 관계없음"),
  ([T29[3][0], T29[4][0], "Some economists argue that cash will soon be replaced by digital currency.", T29[5][0]], 2, "디지털 화폐 → 값싼 것들이 비싸지는 흐름과 관계없음"),
 ],
 blank=[
  ("This means helping students recognize, for example, how the architecture of a social media feed or a news site is ____ to distract or provoke them.", ["deliberately designed", "accidentally created", "carefully protected", "rarely updated"], "의도적 설계를 알아차리는 것이 핵심"),
  ("By treating these as deliberate design choices (often rooted in psychology and profit motives), young people become ____.", ["more critical users rather than passive consumers", "more loyal customers of popular apps", "less interested in technology", "skilled app developers"], "결론: 비판적 사용자"),
  ("Frontiers are so important in these processes because they offer places where ____.", ["the new cheap things can be seized", "cash is exchanged fairly", "workers' wages are raised", "the climate is protected"], "값싼 것들이 사라지므로 새로 빼앗을 곳이 필요"),
 ],
 gram=[
  (B + "They teach ______ we might call attention literacy.</b>", ['what', 'that', 'which', 'how'], "선행사 없는 불완전한 절 → what"),
  ("다음 문장의 뜻으로 알맞은 것은?<br><b>This means helping students recognize it.</b>", ["이것은 학생들이 그것을 인식하도록 돕는 것을 의미한다.", "이것은 학생들이 그것을 인식하도록 도울 작정이다.", "이것은 학생들을 도와서 인식할 필요가 없다.", "이것은 학생들이 돕는 것을 인식한다는 뜻이다."], "mean -ing: ~을 의미하다 / mean to: ~할 작정이다"),
  (B + "It is ______ in psychology and profit motives.</b>", ['rooted', 'rooting', 'root', 'to root'], "be rooted in"),
  (B + "Capitalism is not a system where cash is everywhere but rather ______ in which islands exist.</b>", ['one', 'it', 'them', 'ones'], "단수 가산명사 반복 + 수식어 → one"),
  (B + "crises of the kind we've seen ______ about protests</b>", ['bring', 'to bring', 'brought', 'brings'], "지각동사 see + O + 동사원형"),
  (B + "Crops can no longer grow as ______ as they once did.</b>", ['abundantly', 'abundant', 'abundance', 'abound'], "동사 수식 → 부사"),
  ("빈칸에 들어갈 수 <u>없는</u> 것은?<br><b>They offer places ______ the new cheap things can be seized.</b>", ['which', 'where', 'in which', 'that'], "완전한 절 앞 → where / in which / (관계부사 대용) that 가능, which는 불가"),
 ])

# ═════════════ DAY 2 · 30, 34 ═════════════
d2 = day(
 vocab=[['eco-friendly', '친환경적인', 30], ['licensed', '허가받은, 자격이 있는', 30], ['account A as B', 'A를 B로 여기다', 30], ['deed', '행위', 30],
        ['moral licensing', '도덕적 허가', 30], ['observe', '관찰하다', 30], ['cooperation', '협력', 30], ['remind A of B', 'A에게 B를 떠올리게 하다', 30],
        ['guilt', '죄책감', 30], ['pro-environmental', '친환경적인', 30], ['compensate for', '~을 보상하다', 30], ['restore', '회복하다', 30],
        ['be inclined to', '~하는 경향이 있다', 30], ['reluctant', '꺼리는', 30], ['quick-fix', '임시방편', 30], ['re-establish', '재정립하다', 30],
        ['inconsistency', '불일치', 30], ['evaluation', '평가', 30], ['burdening', '부담을 주는', 30], ['petition', '청원서', 30],
        ['address', '다루다', 30], ['obvious', '분명한', 34], ['accumulate', '축적되다', 34], ['apparent', '뚜렷한', 34],
        ['subtle', '미묘한', 34], ['revolutionize', '혁명을 일으키다', 34], ['the better part of', '~의 대부분', 34], ['fix a meal', '식사를 준비하다', 34],
        ['liberating', '해방감을 주는', 34], ['implication', '영향, 함축', 34], ['overlook', '간과하다', 34], ['luxury', '사치품', 34],
        ['occasion', '경우, 행사', 34], ['anticipate', '예상하다', 34], ['foresee', '예견하다', 34]],
 real=[
  {'n': 30, 'q': exam(30, '다음 글의 밑줄 친 부분 중, 문맥상 낱말의 쓰임이 적절하지 <u>않은</u> 것은?', Q30),
   'opts': ["③ reluctant", "① observed", "② restore", "④ evaluation", "⑤ more"],
   'ex': "정답 ③ reluctant → inclined. 뒤에 '가능한 한 빠르고 쉽게 죄책감에서 벗어나고 싶어서'라는 이유가 오므로 임시방편을 믿으려 하는(inclined) 경향",
   'per': [["꺼리는 → 하려는 경향이 있는", "because they want to re-establish the moral balance and escape the guilt as quickly and easily as possible", "빨리 벗어나고 싶다 → 임시방편을 '믿으려' 함"],
           ["관찰된", "Moral licensing has also been observed", "도덕적 허가가 환경 맥락에서도 관찰됨 ✓"],
           ["회복하다", "to compensate for this guilt and restore balance", "죄책감을 보상하고 균형을 '회복' ✓"],
           ["평가", "may also change their evaluation of past environmentally burdening behaviors", "태도를 바꾸듯 '평가'도 바꿈 ✓"],
           ["더 (가능성이 높은)", "after viewing evidence of human-caused environmental damage", "훼손 증거를 보면 죄책감 → 청원 서명 가능성이 '더' 높음 ✓"]]},
  {'n': 34, 'q': exam(34, '다음 빈칸에 들어갈 말로 가장 적절한 것은?', Q34),
   'opts': ["accumulate over time but are not apparent day to day", "strengthen family bonds in ways we did not anticipate", "are solely technical and have no social consequences", "slowly reshape the global economy and labor market", "gradually harm our health without any symptoms"],
   'ex': "정답 ③ · 분명한 측면만 보면 시간이 흐르며 쌓이지만 당장은 안 보이는 변화를 놓친다 (전자레인지 → 가족 저녁 식사가 점점 사라짐)",
   'per': [["시간이 지나며 쌓이지만 하루하루는 뚜렷하지 않은", ["the long-term implications", "As time went on, fewer and fewer families sat down together"], "장기적·미묘한 변화 → 정답"],
           ["예상치 못한 방식으로 가족 유대를 강화하는", "fewer and fewer families sat down together", "유대가 오히려 약해짐"],
           ["순전히 기술적이고 사회적 결과가 없는", "The effects of the microwave oven on family life", "가족생활에 사회적 영향이 있었음"],
           ["세계 경제와 노동 시장을 서서히 바꾸는", "", "경제·노동 시장 이야기 아님"],
           ["증상 없이 건강을 서서히 해치는", "", "건강 이야기 아님"]]},
 ],
 pickv=[
  ('Some people are more likely to cheat and steal after purchasing "eco-friendly" products, probably because they feel {licensed|limited} to do so since they morally account the "eco-friendly" choice as a "good" deed.', "착한 일을 했으니 나쁜 일을 할 '자격'이 있다고 느낌 → licensed"),
  ("Moral licensing has also been {observed|obscured} in the context of cooperation for the good of the environment.", "observe 관찰하다 vs obscure 가리다"),
  ("People who experience eco-guilt seek pro-environmental actions to {compensate|complicate} for this guilt and restore balance.", "compensate for 보상하다"),
  ("People who experience eco-guilt seek pro-environmental actions to compensate for this guilt and {restore|disturb} balance.", "균형을 '회복' → restore ★30번 ② 적절"),
  ('In their search for such a balance, people are {inclined|reluctant} to believe in "quick-fixes," because they want to re-establish the moral balance and escape the guilt as quickly and easily as possible.', "빨리 벗어나고 싶음 → inclined ★30번 정답(reluctant는 틀림)"),
  ("In the same way that people may change their attitudes to reduce {inconsistencies|consistencies} between attitudes and behavior, people may also change their evaluation of past environmentally burdening behaviors and future environmentally friendly behaviors.", "태도를 바꾸는 이유 → 불일치(inconsistencies)를 줄이려고"),
  ("Most of us notice the obvious aspects of a new medium or technology while missing the more {subtle|obvious} aspects.", "obvious와 대비 → subtle"),
  ("It was introduced in the early 1980s and {revolutionized|reversed} food preparation.", "revolutionize 혁명을 일으키다"),
  ("But the short-term, obvious implications of greater convenience made it easy to {overlook|overcome} the long-term implications of no longer having one person fix food for the family to eat together at an evening meal.", "overlook 간과하다 vs overcome 극복하다"),
  ("The effects of the microwave oven on family life were not {anticipated|appreciated} and would have been difficult to foresee.", "foresee와 짝 → anticipated 예상된"),
 ],
 tf=[
  ["Buying green products may make some people feel entitled to behave unethically.", True, "green = eco-friendly · feel entitled to = feel licensed to · behave unethically ≒ cheat and steal", 30, "they feel licensed to do so"],
  ["Recalling environmentally harmful deeds can leave people feeling guilty.", True, "recall ≒ be reminded of · leave A feeling guilty = be left with a feeling of eco-guilt", 30, "they might be left with a feeling of \"eco-guilt.\""],
  ["People with eco-guilt tend to avoid pro-environmental actions.", False, "avoid 피하다 → 친환경 행동을 추구(seek)", 30, "seek pro-environmental actions"],
  ["Viewing evidence of human-caused damage makes people less willing to sign petitions.", False, "less willing → 서명할 가능성이 더 높음", 30, "people are more likely to sign a petition"],
  ["People tend to miss the gradual, less visible effects of new technologies.", True, "gradual = accumulate over time · less visible = not apparent", 34, "missing the more subtle aspects"],
  ["The microwave oven was introduced in the early 1990s.", False, "1980년대 초반에 도입", 34, "It was introduced in the early 1980s"],
  ["Shorter cooking times freed family cooks, most of whom were women.", True, "free = liberate · shorter cooking times = this shortening of preparation time", 34, "this shortening of preparation time was liberating for the cooks in the family"],
  ["The decline in family dinners had been widely predicted.", False, "widely predicted 널리 예측된 → 예상되지 못함", 34, "were not anticipated and would have been difficult to foresee"],
 ],
 ilchi=[
  ilchi(30, T30, True, ["People with eco-guilt are unwilling to take quick measures to ease their guilt.", "Some people regard eco-friendly purchases as morally good deeds.", "Moral licensing appears in environmental cooperation as well.", "People may reassess their past behaviors that burdened the environment.", "Evidence of environmental harm can prompt people to sign petitions."],
        "정답: unwilling = reluctant · quick measures = quick-fixes → 실제로는 임시방편을 믿으려 함(inclined)\n· regard A as B = account A as B\n· as well = also\n· reassess = change one's evaluation · burden 부담을 주다\n· prompt A to ~ A가 ~하도록 자극하다",
        [["환경 죄책감을 느끼는 사람들은 죄책감을 덜기 위한 빠른 조치를 꺼린다.", "people are inclined to believe in \"quick-fixes,\"", "불일치 → 오히려 믿으려 함"],
         ["어떤 사람들은 친환경 구매를 도덕적으로 좋은 행위로 여긴다.", "they morally account the \"eco-friendly\" choice as a \"good\" deed", "일치"],
         ["도덕적 허가는 환경 협력에서도 나타난다.", "Moral licensing has also been observed in the context of cooperation", "일치"],
         ["사람들은 환경에 부담을 준 과거 행동을 재평가할 수 있다.", "change their evaluation of past environmentally burdening behaviors", "일치"],
         ["환경 피해의 증거는 사람들이 청원에 서명하게 할 수 있다.", "more likely to sign a petition addressing environmental damage", "일치"]]),
  ilchi(34, T34, False, ["Convenience made people overlook the long-term consequences of the microwave.", "Most people readily notice the subtle aspects of new technologies.", "Before microwaves, preparing dinner took only a few minutes.", "The microwave increased the number of families dining together.", "The effects of the microwave were easy to predict."],
        "정답: overlook 간과하다 · long-term consequences = long-term implications\n· readily notice subtle aspects → 미묘한 측면은 놓침\n· only a few minutes → 오후의 대부분(the better part of an afternoon)\n· increased → 점점 줄어듦(fewer and fewer)\n· easy to predict → 예견하기 어려웠음",
        [["편리함 때문에 사람들은 전자레인지의 장기적 결과를 간과했다.", "made it easy to overlook the long-term implications", "일치"],
         ["대부분의 사람들은 새 기술의 미묘한 측면을 쉽게 알아차린다.", "while missing the more subtle aspects", "불일치"],
         ["전자레인지 이전에 저녁 준비는 몇 분이면 됐다.", "spent the better part of an afternoon fixing an evening meal", "불일치"],
         ["전자레인지는 함께 식사하는 가족의 수를 늘렸다.", "fewer and fewer families sat down together", "불일치"],
         ["전자레인지의 영향은 예측하기 쉬웠다.", "would have been difficult to foresee", "불일치"]]),
 ],
 pickg=[
  ('Some people are more likely to cheat and steal after {purchasing|purchase} "eco-friendly" products, probably because they feel licensed to do so since they morally account the "eco-friendly" choice as a "good" deed.', "전치사 after + 동명사"),
  ("Moral licensing has also {been observed|observed} in the context of cooperation for the good of the environment.", "허가가 '관찰된' 수동 → has been observed"),
  ('When people {are reminded|remind} of deeds they have done that they know were harmful to the environment, they might be left with a feeling of "eco-guilt."', "remind A of B의 수동 → be reminded of"),
  ('When people are reminded of deeds they have done that they know {were|was} harmful to the environment, they might be left with a feeling of "eco-guilt."', "선행사 deeds(복수) + 삽입절 they know → were"),
  ("People who experience eco-guilt seek pro-environmental actions {to compensate|compensating} for this guilt and restore balance.", "목적의 to부정사"),
  ('In their search for such a balance, people are inclined to believe in "quick-fixes," because they want to re-establish the moral balance and escape the guilt as quickly and easily {as|than} possible.', "as ~ as possible"),
  ("For instance, people are more likely to sign a petition {addressing|addressed} environmental damage after viewing evidence of human-caused environmental damage.", "청원서가 피해를 '다루는' 능동 → addressing"),
  ("Traditionally, one person spent the better part of an afternoon {fixing|to fix} an evening meal for a family.", "spend + 시간 + -ing"),
  ("Now, it was possible to prepare foods very quickly, and this shortening of preparation time was liberating for the cooks in the family, most of {whom|them} tended to be women.", "콤마 뒤 접속사 없이 → 관계대명사 whom"),
  ("But the short-term, obvious implications of greater convenience made {it|that} easy to overlook the long-term implications of no longer having one person fix food for the family to eat together at an evening meal.", "가목적어 it"),
  ("But the short-term, obvious implications of greater convenience made it easy to overlook the long-term implications of no longer having one person {fix|to fix} food for the family to eat together at an evening meal.", "사역동사 have + O + 동사원형"),
  ("The effects of the microwave oven on family life were not anticipated and would have been difficult {to foresee|foreseeing}.", "difficult + to부정사"),
 ],
 verb=[
  ('Some people are more likely to cheat and steal after purchasing "eco-friendly" products, probably because they feel ___ to do so since they morally account the "eco-friendly" choice as a "good" deed.', 'license', ['licensed'], "feel + 과거분사(자격을 받은)"),
  ('When people are reminded of deeds they have done that they know were harmful to the environment, they might be ___ with a feeling of "eco-guilt."', 'leave', ['left'], "be left with ~이 남다"),
  ('In their search for such a balance, people are ___ to believe in "quick-fixes," because they want to re-establish the moral balance and escape the guilt as quickly and easily as possible.', 'incline', ['inclined'], "be inclined to"),
  ("For instance, people are more likely to sign a petition addressing environmental damage after ___ evidence of human-caused environmental damage.", 'view', ['viewing'], "after + 동명사"),
  ("Most of us notice the obvious aspects of a new medium or technology while ___ the more subtle aspects.", 'miss', ['missing'], "접속사 while + 현재분사"),
  ("Traditionally, one person spent the better part of an afternoon ___ an evening meal for a family.", 'fix', ['fixing'], "spend 시간 -ing"),
  ("Now, it was possible to prepare foods very quickly, and this shortening of preparation time was liberating for the cooks in the family, most of whom ___ to be women.", 'tend', ['tended'], "과거형"),
  ("The effects of the microwave oven on family life were not anticipated and would have ___ difficult to foresee.", 'be', ['been'], "would have p.p."),
 ],
 error=[
  ("Moral licensing has also [[observed]] in the context of cooperation for the good of the environment. When people [[are reminded]] of deeds they have done that they know [[were]] harmful to the environment, they might be [[left]] with a feeling of \"eco-guilt.\"", 0, 'been observed', "수동 완료 has been observed"),
  ("People who [[experience]] eco-guilt [[seeks]] pro-environmental actions [[to compensate]] for this guilt and [[restore]] balance.", 1, 'seek', "주어 People(복수) → seek"),
  ("For instance, people are more likely [[signing]] a petition [[addressing]] environmental damage after [[viewing]] evidence of [[human-caused]] environmental damage.", 0, 'to sign', "be likely to + 동사원형"),
  ("Now, it was possible [[to prepare]] foods very quickly, and this shortening of preparation time [[was]] liberating for the cooks in the family, most of [[them]] [[tended]] to be women.", 2, 'whom', "접속사 없이 절 연결 → 관계대명사 whom"),
  ("But the short-term, obvious implications of greater convenience [[made]] it easy [[to overlook]] the long-term implications of no longer [[having]] one person [[to fix]] food for the family.", 3, 'fix', "사역동사 have + O + 동사원형"),
  ("As time [[went]] on, [[fewer and fewer]] families sat down together to eat dinner. Meals that [[took]] a long time to prepare [[becoming]] a luxury of the past.", 3, 'became', "주어 Meals의 본동사 → became"),
 ],
 scr=[(T30[1][0], T30[1][1]), (T30[3][0], T30[3][1]), (T34[2][0], T34[2][1]), (T34[3][0], T34[3][1]), (T34[7][0], T34[7][1])],
 order=[
  ([T30[0][0], T30[1][0], T30[2][0], T30[3][0]], ["친환경 구매 후 '착한 일 했으니' 속이고 훔치기도 함", "도덕적 허가는 환경 협력에서도 관찰됨", "환경에 해로운 행동을 떠올리면 환경 죄책감", "죄책감을 보상하려 친환경 행동 추구"]),
  ([T30[4][0], T30[5][0], T30[6][0]], ["빨리 벗어나려 임시방편을 믿으려 함", "태도처럼 행동에 대한 평가도 바꿈", "예: 환경 피해 증거를 보면 청원 서명↑"]),
  ([T34[0][0], T34[1][0], T34[2][0], T34[3][0], T34[4][0]], ["분명한 측면만 보면 쌓이는 변화를 놓침", "미묘한 측면은 놓침", "예: 전자레인지", "1980년대 도입, 음식 준비 혁명", "예전엔 저녁 준비에 오후 대부분"]),
  ([T34[6][0], T34[7][0], T34[8][0], T34[9][0]], ["하지만 편리함 때문에 장기 영향을 간과", "함께 저녁 먹는 가족이 줄어듦", "오래 걸리는 식사는 과거의 사치", "그 영향은 예상하기 어려웠음"]),
 ],
 insert=[
  ([T30[2][0], T30[3][0], T30[4][0]], 1, ["환경 죄책감이 남음", "이 죄책감(this guilt)을 보상하려 함", "그런 균형(such a balance)을 찾는 과정"], "this guilt는 eco-guilt, such a balance는 앞의 restore balance를 받는다."),
  ([T34[4][0], T34[5][0], T34[6][0]], 1, ["예전: 오후 내내 저녁 준비", "이제(Now) 빨라져 요리사 해방", "하지만(But) 장기 영향 간과"], "Traditionally ↔ Now 대비 후 But으로 반전"),
  ([T34[6][0], T34[7][0], T34[8][0]], 1, ["장기 영향 간과", "시간이 지나며 함께 먹는 가족 감소", "오래 걸리는 식사는 사치가 됨"], "장기 영향의 구체적 내용"),
 ],
 odd=[
  ([T30[2][0], T30[3][0], "Recycling programs have been adopted by many cities worldwide.", T30[4][0]], 2, "재활용 프로그램 확산 → 죄책감과 균형 이야기와 관계없음"),
  ([T34[3][0], T34[4][0], "Microwave ovens use electromagnetic waves to heat water molecules in food.", T34[5][0]], 2, "전자레인지 작동 원리 → 가족생활 변화와 관계없음"),
 ],
 blank=[
  ('In their search for such a balance, people are inclined to believe in "quick-fixes," because they want to ____.', ["re-establish the moral balance and escape the guilt as quickly and easily as possible", "take time to solve environmental problems completely", "avoid thinking about the environment", "buy more eco-friendly products"], "임시방편을 믿는 이유: 빨리, 쉽게 벗어나려고"),
  ("For instance, people are more likely to sign a petition addressing environmental damage after ____.", ["viewing evidence of human-caused environmental damage", "buying eco-friendly products", "forgetting their past behaviors", "receiving money from charities"], "죄책감을 일으키는 계기 → 피해 증거를 봄"),
  ("Most of us notice the obvious aspects of a new medium or technology while ____.", ["missing the more subtle aspects", "predicting its long-term effects", "ignoring its convenience", "rejecting it completely"], "obvious ↔ subtle"),
  ("But the short-term, obvious implications of greater convenience made it easy to overlook ____.", ["the long-term implications", "the price of the oven", "the speed of cooking", "the role of women"], "short-term ↔ long-term"),
 ],
 gram=[
  (B + "Moral licensing has also ______ in that context.</b>", ['been observed', 'observed', 'being observed', 'to be observed'], "현재완료 수동태"),
  (B + "When people are reminded ______ deeds they have done</b>", ['of', 'to', 'with', 'for'], "remind A of B → be reminded of B"),
  (B + "deeds they have done that they know ______ harmful</b>", ['were', 'was', 'being', 'to be'], "선행사 deeds(복수) + 삽입절"),
  (B + "Escape the guilt as quickly ______ possible.</b>", ['as', 'than', 'so', 'that'], "as ~ as possible"),
  (B + "the cooks in the family, most of ______ tended to be women</b>", ['whom', 'them', 'who', 'which'], "부분 표현 + 관계대명사 whom"),
  (B + "The convenience made ______ easy to overlook the long-term effects.</b>", ['it', 'that', 'this', 'what'], "가목적어 it"),
  (B + "no longer having one person ______ food</b>", ['fix', 'to fix', 'fixed', 'fixes'], "사역동사 have + O + 동사원형"),
  ("다음 문장의 뜻으로 알맞은 것은?<br><b>The effects would have been difficult to foresee.</b>", ["그 영향은 예견하기 어려웠을 것이다.", "그 영향은 예견하기 쉬웠다.", "그 영향은 앞으로 예견하기 어려울 것이다.", "그 영향을 예견했어야 했다."], "would have p.p.: (과거에) ~했을 것이다"),
 ])

# ═════════════ DAY 3 · 38, 40 ═════════════
d3 = day(
 vocab=[['make a distinction between A and B', 'A와 B를 구분하다', 38], ['density', '밀도', 38], ['crowding', '혼잡(감)', 38], ['phenomenon', '현상', 38],
        ['sensory overload', '감각 과부하', 38], ['anxiety', '불안', 38], ['neutral', '중립적인', 38], ['invariably', '변함없이, 언제나', 38],
        ['intensify', '강해지다', 38], ['look forward to', '~을 기대하다', 38], ['enhance', '높이다', 38], ['dread', '두려워하다', 38],
        ['accentuate', '두드러지게 하다', 38], ['dominant', '지배적인', 38], ['aggressive', '공격적인', 38], ['conversely', '반대로', 38],
        ['pedestrian', '보행자(의)', 38], ['defuse', '완화하다', 38], ['retain', '유지하다', 40], ['perpetuate', '영속시키다', 40],
        ['perceive A as B', 'A를 B로 인식하다', 40], ['accordingly', '그에 맞춰', 40], ['motivate A to', 'A가 ~하도록 동기를 부여하다', 40], ['subject', '피실험자', 40],
        ['donate', '기부하다', 40], ['charity', '자선 단체', 40], ['earnings', '수익', 40], ['recall', '회상하다', 40],
        ['take pains to', '공들여 ~하다', 40], ['purely', '순수하게', 40], ['appearance', '겉모습', 40], ['generous', '관대한', 40],
        ['for its own sake', '그 자체를 위해', 40], ['evident', '분명한', 40], ['conscious of', '~을 의식하는', 40]],
 real=[
  {'n': 38, 'q': exam(38, '글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳은?', Q38, G38),
   'opts': ["③", "①", "②", "④", "⑤"],
   'ex': "정답 ③ · 기분과 행동이 강해진다(③ 앞) → 그래서(So) 기대하면 즐거움↑ → 그러나(But) 두려워하면 더 나빠짐(③ 뒤)",
   'per': [["③번 자리", ["believe that people's moods and behaviors intensify as density increases", "But if they are dreading an event"], "So로 앞 문장의 예시를 들고, 뒤 But 문장(반대 예시)과 짝을 이룸"],
           ["①번 자리", "", "밀도와 혼잡성 구분 직후 → 예시가 올 자리 아님"],
           ["②번 자리", "", "혼잡이 부정적이라는 설명 뒤 → '즐거움이 높아진다'와 충돌"],
           ["④번 자리", "But if they are dreading an event", "But 반대 예시가 먼저 나오면 순서가 뒤바뀜"],
           ["⑤번 자리", "", "공동체 이야기 뒤 → 개인 콘서트 예시가 올 자리 아님"]]},
  {'n': 40, 'q': exam(40, '다음 글의 내용을 한 문장으로 요약하고자 한다. 빈칸 (A), (B)에 들어갈 말로 가장 적절한 것은?', body(T40), '') + S40,
   'opts': ["evident — conscious", "lacking — observant", "noticeable — ignorant", "suspended — tolerant", "activated — forgetful"],
   'ex': "정답 ① · 과거 선행을 떠올리고 행위 자체에 집중한 사람에게 선행 동기가 더 분명(evident), 겉모습을 강하게 의식하는(conscious) 사람에게는 덜",
   'per': [["분명한 — 의식하는", ["almost twice as much as those who had been instructed to recall previous bad deeds", "people who seemed concerned about appearances"], "더 많이 기부 = 동기가 분명 / 겉모습에 신경 씀 = 의식하는"],
           ["부족한 — 관찰하는", "", "(A) 반대: 오히려 더 많이 기부함"],
           ["눈에 띄는 — 무지한", "seemed concerned about appearances", "(B) 반대: 겉모습에 신경을 씀"],
           ["중단된 — 관대한", "", "(A) 반대, (B) 관대하지 않았음"],
           ["활성화된 — 잊어버리는", "seemed concerned about appearances", "(A)는 가능하나 (B) 반대"]]},
 ],
 pickv=[
  ("Environmental psychologists make a distinction between the physical measurement of {density|destiny} (how many people are in a particular space) and crowding (the psychological feeling of not having enough space).", "density 밀도 vs destiny 운명"),
  ("However, some psychologists see crowding as {neutral|negative} rather than invariably negative, and believe that people's moods and behaviors intensify as density increases.", "rather than invariably negative와 대비 → neutral"),
  ("So if an individual is looking forward to a concert, say, the feeling of crowding {enhances|reduces} their enjoyment of the performance.", "기분이 강화됨 → 기대하던 즐거움이 높아짐(enhances)"),
  ("But if they are {dreading|anticipating} an event, crowding will make the person's experience of it even worse.", "even worse와 연결 → dread 두려워하다"),
  ("Put into a community setting, crowding may accentuate the {dominant|minor} behavior — an aggressive group may turn violent as density rises.", "지배적인(dominant) 행동이 두드러짐"),
  ("Conversely, creating positive social spaces such as parks and pedestrian areas in high-density urban environments may help to lift the general mood and {defuse|diffuse} tension.", "defuse 완화하다 vs diffuse 퍼뜨리다"),
  ("Our adult brains {retain|refrain} a preference for perpetuating good, fair behavior.", "retain 유지하다 vs refrain 삼가다"),
  ("Simply perceiving ourselves as people who do good deeds and behaving accordingly {motivates|discourages} us to do greater good in the future.", "더 큰 선을 하도록 → motivates"),
  ("In other words, people who seemed concerned about appearances (e.g., the impact of their good deed, as much as the deed itself) were less {generous|selfish} than those who cared more about doing good for its own sake.", "기부를 덜 함 → 덜 관대(generous)"),
 ],
 tf=[
  ["Environmental psychologists differentiate density from crowding.", True, "differentiate A from B = make a distinction between A and B", 38, "make a distinction between the physical measurement of density"],
  ["Crowding usually occurs without high density.", False, "대개 혼잡에는 높은 밀도가 필요(is needed)", 38, "high density is needed for the phenomenon of crowding"],
  ["Some psychologists regard crowding as always harmful.", False, "always harmful → 중립적(neutral)으로 봄", 38, "see crowding as neutral rather than invariably negative"],
  ["Crowding may amplify the prevailing behavior of a group.", True, "amplify = accentuate · prevailing = dominant", 38, "crowding may accentuate the dominant behavior"],
  ["Recognizing ourselves as good people can spur us to further good deeds.", True, "spur 자극하다 = motivate · further = greater", 40, "motivates us to do greater good in the future"],
  ["Subjects who recalled bad deeds donated about twice as much as others.", False, "좋은 행위를 쓴 사람이 거의 두 배", 40, "almost twice as much as those who had been instructed to recall previous bad deeds"],
  ["Those focused on others' reactions donated less than those focused on the acts themselves.", True, "reactions = how people responded · acts = actions", 40, "were likely to donate significantly less than those who focused purely on the actions themselves"],
  ["People concerned about appearances proved to be more generous.", False, "덜 관대했음(less generous)", 40, "were less generous"],
 ],
 ilchi=[
  ilchi(38, T38, True, ["All psychologists agree that crowding is invariably harmful.", "Crowding refers to the feeling of lacking sufficient space.", "Crowding can heighten stress and anxiety.", "Density may make an aggressive group more violent.", "Pedestrian areas in dense cities can help ease tension."],
        "정답: All psychologists agree → '몇몇' 심리학자는 중립적으로 봄\n· refer to ~을 가리키다 · lack 부족하다 · sufficient = enough\n· heighten 높이다 ≒ rising stress\n· ease = defuse · dense = high-density",
        [["모든 심리학자는 혼잡이 언제나 해롭다는 데 동의한다.", "some psychologists see crowding as neutral", "불일치"],
         ["혼잡성은 공간이 충분하지 않다는 느낌을 말한다.", "the psychological feeling of not having enough space", "일치"],
         ["혼잡은 스트레스와 불안을 높일 수 있다.", "rising stress and anxiety", "일치"],
         ["밀도는 공격적 집단을 더 폭력적으로 만들 수 있다.", "an aggressive group may turn violent as density rises", "일치"],
         ["밀집 도시의 보행 구역은 긴장을 푸는 데 도움이 될 수 있다.", "may help to lift the general mood and defuse tension", "일치"]]),
  ilchi(40, T40, False, ["The study involved one hundred college students who were paid.", "Subjects who wrote about bad deeds donated over half their earnings.", "Describing others' responses increased the amount donated.", "Concern about appearances made people more generous.", "Adult brains lose their preference for good behavior."],
        "정답: involve 대상으로 하다 · paid study = 보수가 지급된 연구\n· over half → 좋은 행위를 쓴 사람들이 절반 이상\n· increased → 훨씬 적게 기부(significantly less)\n· more generous → 덜 관대\n· lose → 유지함(retain)",
        [["연구는 보수를 받은 대학생 100명을 대상으로 했다.", "In one paid study of one hundred college students", "일치"],
         ["나쁜 행위를 쓴 피실험자들이 수익의 절반 넘게 기부했다.", "subjects who wrote down a list of past good deeds", "불일치 → 좋은 행위를 쓴 쪽"],
         ["남들의 반응을 묘사하는 것이 기부액을 늘렸다.", "were likely to donate significantly less", "불일치"],
         ["겉모습에 대한 관심은 사람들을 더 관대하게 했다.", "were less generous", "불일치"],
         ["성인의 뇌는 선한 행동에 대한 선호를 잃는다.", "Our adult brains retain a preference", "불일치"]]),
 ],
 pickg=[
  ("Environmental psychologists make a distinction between the physical measurement of density (how many people are in a particular space) and crowding (the psychological feeling of not {having|have} enough space).", "전치사 of + 동명사"),
  ("Usually, high density {is needed|needs} for the phenomenon of crowding, which makes people experience sensory overload, a lack of control, and rising stress and anxiety.", "밀도가 '필요한' 수동"),
  ("Usually, high density is needed for the phenomenon of crowding, {which|that} makes people experience sensory overload, a lack of control, and rising stress and anxiety.", "콤마 뒤 계속적 용법 → which"),
  ("Usually, high density is needed for the phenomenon of crowding, which makes people {experience|to experience} sensory overload, a lack of control, and rising stress and anxiety.", "사역동사 make + O + 동사원형"),
  ("However, some psychologists see crowding as neutral rather than invariably negative, and {believe|believing} that people's moods and behaviors intensify as density increases.", "see와 병렬 → believe"),
  ("{Put|Putting} into a community setting, crowding may accentuate the dominant behavior — an aggressive group may turn violent as density rises.", "혼잡이 '놓이는' 수동 분사구문 → Put(과거분사)"),
  ("Conversely, {creating|create} positive social spaces such as parks and pedestrian areas in high-density urban environments may help to lift the general mood and defuse tension.", "주어 자리 → 동명사"),
  ("Simply perceiving ourselves as people who do good deeds and behaving accordingly {motivates|motivate} us to do greater good in the future.", "동명사구 주어 → 단수동사"),
  ("Subjects who wrote down a list of past good deeds and were then asked to donate money to a charity gave, on average, over half the earnings they'd made from the study — almost twice as much as those who {had been instructed|had instructed} to recall previous bad deeds.", "'지시받은' 수동 과거완료"),
  ("In addition, subjects who'd taken pains to describe not only how they'd been nice to others but how people responded {were|was} likely to donate significantly less than those who focused purely on the actions themselves.", "주어 subjects(복수) → were"),
  ("In other words, people who seemed {concerned|concerning} about appearances (e.g., the impact of their good deed, as much as the deed itself) were less generous than those who cared more about doing good for its own sake.", "be concerned about ~에 신경 쓰다"),
 ],
 verb=[
  ("However, some psychologists see crowding as neutral rather than invariably negative, and believe that people's moods and behaviors ___ as density increases.", 'intensify', ['intensify'], "복수 주어 → intensify"),
  ("So if an individual is ___ forward to a concert, say, the feeling of crowding enhances their enjoyment of the performance.", 'look', ['looking'], "진행형 be looking forward to"),
  ("___ into a community setting, crowding may accentuate the dominant behavior — an aggressive group may turn violent as density rises.", 'put', ['Put'], "수동 분사구문(Being) Put"),
  ("Conversely, ___ positive social spaces such as parks and pedestrian areas in high-density urban environments may help to lift the general mood and defuse tension.", 'create', ['creating', 'Creating'], "주어 동명사"),
  ("Our adult brains retain a preference for ___ good, fair behavior.", 'perpetuate', ['perpetuating'], "전치사 + 동명사"),
  ("Simply ___ ourselves as people who do good deeds and behaving accordingly motivates us to do greater good in the future.", 'perceive', ['perceiving', 'Perceiving'], "주어 동명사 (behaving과 병렬)"),
  ("In addition, subjects who'd ___ pains to describe not only how they'd been nice to others but how people responded were likely to donate significantly less than those who focused purely on the actions themselves.", 'take', ['taken'], "had p.p. (who'd = who had)"),
 ],
 error=[
  ("Usually, high density [[needs]] for the phenomenon of crowding, [[which]] makes people [[experience]] sensory overload, a lack of control, and [[rising]] stress and anxiety.", 0, 'is needed', "밀도가 '필요한' 수동"),
  ("However, some psychologists see crowding [[as]] neutral rather than [[invariably]] negative, and [[believing]] that people's moods and behaviors [[intensify]] as density increases.", 2, 'believe', "see와 병렬 → believe"),
  ("[[Putting]] into a community setting, crowding may [[accentuate]] the dominant behavior — an aggressive group may turn [[violent]] as density [[rises]].", 0, 'Put', "수동 분사구문"),
  ("Simply [[perceiving]] ourselves as people who [[do]] good deeds and behaving accordingly [[motivate]] us [[to do]] greater good in the future.", 2, 'motivates', "동명사구 주어 → 단수"),
  ("In other words, people who seemed [[concerning]] about appearances (e.g., the impact of their good deed, as much as the deed itself) [[were]] less generous than those who [[cared]] more about [[doing]] good for its own sake.", 0, 'concerned', "be concerned about"),
 ],
 scr=[(T38[4][0], T38[4][1]), (T40[0][0], T40[0][1]), ("People's moods and behaviors intensify as density increases.", "밀도가 올라감에 따라 사람들의 기분과 행동이 강화된다."), ("Crowding may accentuate the dominant behavior.", "혼잡성은 지배적 행동을 두드러지게 할 수 있다.")],
 order=[
  ([T38[0][0], T38[1][0], T38[2][0], T38[3][0]], ["밀도와 혼잡성을 구분", "대개 혼잡엔 높은 밀도가 필요, 스트레스·불안", "그러나 중립적으로 보고 기분·행동이 강해진다고 봄", "그래서 콘서트를 기대하면 즐거움↑"]),
  ([T38[3][0], T38[4][0], T38[5][0], T38[6][0]], ["기대하면 즐거움↑", "두려워하면 더 나빠짐", "공동체: 지배적 행동이 두드러짐", "반대로 긍정적 공간은 긴장 완화"]),
  ([T40[0][0], T40[1][0], T40[2][0]], ["성인 뇌는 선한 행동을 지속하려는 선호를 유지", "자신을 좋은 사람으로 인식하면 더 큰 선을 함", "연구: 좋은 행위를 쓴 쪽이 거의 두 배 기부"]),
  ([T40[2][0], T40[3][0], T40[4][0]], ["좋은 행위를 쓴 쪽이 두 배 기부", "게다가 반응까지 묘사한 쪽은 훨씬 덜 기부", "즉 겉모습을 신경 쓰면 덜 관대"]),
 ],
 insert=[
  ([T38[2][0], T38[3][0], T38[4][0], T38[5][0]], 1, ["기분·행동이 강해진다", "그래서(So) 기대하면 즐거움↑", "그러나(But) 두려우면 더 나빠짐", "공동체 환경"], "★38번 정답 위치: So 예시 → But 반대 예시"),
  ([T40[2][0], T40[3][0], T40[4][0]], 1, ["두 배 기부", "게다가(In addition) 반응 묘사 쪽은 덜 기부", "다시 말해(In other words)"], "In addition으로 두 번째 결과를 덧붙인다."),
 ],
 odd=[
  ([T38[1][0], T38[2][0], "Concert tickets have become more expensive in recent years.", T38[3][0]], 2, "티켓 가격 → 혼잡성의 효과와 관계없음"),
  ([T40[1][0], T40[2][0], "Many universities require students to do volunteer work before graduation.", T40[3][0]], 2, "대학의 봉사 요건 → 연구 결과와 관계없음"),
 ],
 blank=[
  ("However, some psychologists see crowding as neutral rather than invariably negative, and believe that people's moods and behaviors ____ as density increases.", ["intensify", "disappear", "stay the same", "become calm"], "기대하면 더 즐겁고, 두려우면 더 나빠짐 → 강화"),
  ("Simply perceiving ourselves as people who do good deeds and behaving accordingly motivates us to ____ in the future.", ["do greater good", "forget our deeds", "care about appearances", "donate less"], "선한 자기 인식 → 더 큰 선"),
  ("In other words, people who seemed concerned about appearances (e.g., the impact of their good deed, as much as the deed itself) were ____ than those who cared more about doing good for its own sake.", ["less generous", "more generous", "happier", "more honest"], "덜 기부함 = 덜 관대"),
 ],
 gram=[
  (B + "crowding, ______ makes people experience stress</b>", ['which', 'that', 'what', 'it'], "계속적 용법 → which"),
  (B + "It makes people ______ sensory overload.</b>", ['experience', 'to experience', 'experiencing', 'experienced'], "사역동사 make + O + 동사원형"),
  (B + "______ into a community setting, crowding may accentuate the dominant behavior.</b>", ['Put', 'Putting', 'To put', 'Puts'], "수동 분사구문 (put-put-put)"),
  (B + "______ positive social spaces may help to lift the mood.</b>", ['Creating', 'Create', 'Created', 'Creates'], "주어 동명사"),
  (B + "Perceiving ourselves as good people ______ us to do greater good.</b>", ['motivates', 'motivate', 'motivating', 'to motivate'], "동명사 주어 → 단수"),
  (B + "They gave almost twice as ______ as those who recalled bad deeds.</b>", ['much', 'more', 'many', 'most'], "배수사 + as much as"),
  (B + "people who seemed ______ about appearances</b>", ['concerned', 'concerning', 'concern', 'to concern'], "be concerned about"),
 ])

# ═════════════ DAY 4 · 41~42 ═════════════
d4 = day(
 vocab=[['choice architecture', '선택 구조', 41], ['popularize', '대중화하다', 41], ['behavioral economics', '행동 경제학', 41], ['highlight', '강조하다', 41],
        ['in essence', '본질적으로', 41], ['sophisticated', '정교한', 41], ['curate', '선별하다', 41], ['subtly', '미묘하게', 41],
        ['nudge', '가볍게 자극하다(넛지)', 41], ['beneficial', '유익한', 41], ['manipulation', '조작', 41], ['underlying', '근본적인, 숨은', 41],
        ['objective', '목표', 41], ['be aligned with', '~와 일치하다', 41], ['well-being', '복지, 행복', 41], ['autonomy', '자율성', 41],
        ['cultivate', '기르다', 41], ['agency', '주체성', 41], ['algorithmic', '알고리즘의', 41], ['conscious', '의식적인', 41],
        ['engagement', '관계, 관여', 41], ['seek out', '찾아내다', 41], ['diverse', '다양한', 41], ['deliberate', '의도적인', 41],
        ['go against the grain', '흐름을 거스르다', 41], ['skepticism', '회의론, 의심', 41], ['seemingly', '겉보기에', 41], ['objective', '객관적인', 41],
        ['reflection', '반영', 41], ['prescription', '처방', 41], ['flourishing', '번영', 41]],
 real=[
  {'n': 41, 'q': exam('41', '윗글의 제목으로 가장 적절한 것은?', Q41),
   'opts': ["Fostering Human Agency in Designed Digital Spaces", "Reclaim Creativity in an Excessively Automated World", "The Ethical Controversy of Algorithmic Decision-Making", "Emotional Bias: The Primary Force Behind Online Choices", "Human Intuition: The Key to Innovating Digital Environments"],
   'ex': "정답 ① · 알고리즘이 설계한 디지털 환경 속에서 인간의 주체성(human agency)을 기르고 지키는 방법",
   'per': [["설계된 디지털 공간에서 인간의 주체성 기르기", "how can we cultivate and protect our human agency in an increasingly algorithmic world?", "질문과 답이 글의 핵심 → 정답"],
           ["지나치게 자동화된 세상에서 창의성 되찾기", "", "창의성이 아니라 주체성"],
           ["알고리즘 의사결정의 윤리적 논란", "", "윤리 논쟁이 중심이 아님"],
           ["감정적 편향: 온라인 선택의 주된 힘", "", "감정 이야기 없음"],
           ["인간의 직관: 디지털 환경 혁신의 열쇠", "", "직관·혁신 이야기 없음"]]},
  {'n': 41, 'q': exam('42', '밑줄 친 (a)~(e) 중에서 문맥상 낱말의 쓰임이 적절하지 <u>않은</u> 것은?', Q41),
   'opts': ["(d) following", "(a) sophisticated", "(b) particular", "(c) conscious", "(e) reflection"],
   'ex': "정답 ④ (d) following → challenging. 다양한 관점을 찾고 예측된 흐름을 거스르는 선택과 나란히 → 추천에 '도전하기'",
   'per': [["(d) 따르는 → 도전하는", ["actively seeking out diverse perspectives", "making deliberate choices that go against the predicted grain"], "주체성을 지키려면 추천을 따르면 안 됨"],
           ["(a) 정교한", "they subtly, and sometimes not so subtly, nudge us", "미묘하게 자극하는 정교한 설계자 ✓"],
           ["(b) 특정한", "nudge us towards particular paths", "특정 경로로 유도 ✓"],
           ["(c) 의식적인", "to maintain critical engagement with the technologies we use", "비판적 관계 유지를 위한 의식적 노력 ✓"],
           ["(e) 반영", "a reflection of past realities, not necessarily a prescription for future flourishing", "과거의 반영일 뿐 미래 처방은 아님 ✓"]]},
 ],
 pickv=[
  ('The concept of "choice architecture," popularized in behavioral economics, highlights how the design of the environment in which choices are made can {significantly|slightly} influence the decisions people make.', "글 전체 → 설계가 결정에 '큰' 영향 → significantly"),
  ("Algorithms are, in essence, {sophisticated|simple} architects of our digital environments.", "미묘하게 유도하는 설계자 → sophisticated ★42번 (a) 적절"),
  ("By curating what we see, what we are recommended, and what options are presented to us, they subtly, and sometimes not so subtly, nudge us towards {particular|random} paths.", "nudge → 특정(particular) 경로 ★(b) 적절"),
  ("While nudges can be used for beneficial purposes, such as encouraging healthier habits, they also carry the potential for {manipulation|motivation}, particularly when the underlying objectives of the architects are not aligned with the well-being or autonomy of the individual.", "개인의 목표와 어긋날 때 → 조작(manipulation)"),
  ("The question then becomes: how can we cultivate and protect our human {agency|agenda} in an increasingly algorithmic world?", "agency 주체성 vs agenda 의제"),
  ("It requires a {conscious|unconscious} effort to maintain critical engagement with the technologies we use.", "의식적인 노력 ★(c) 적절"),
  ("It means actively seeking out diverse perspectives, {challenging|following} algorithmic recommendations, and making deliberate choices that go against the predicted grain.", "★42번 정답: following → challenging"),
  ("It involves cultivating a healthy {skepticism|optimism} towards the seemingly objective outputs of algorithms and remembering that these systems are designed by humans with specific goals, and that their data is a reflection of past realities, not necessarily a prescription for future flourishing.", "겉보기에 객관적인 결과를 의심 → skepticism"),
  ("It involves cultivating a healthy skepticism towards the seemingly objective outputs of algorithms and remembering that these systems are designed by humans with specific goals, and that their data is a {reflection|prediction} of past realities, not necessarily a prescription for future flourishing.", "과거 현실의 '반영' ★(e) 적절"),
 ],
 tf=[
  ["Choice architecture holds that the setting of a decision can sway what people choose.", True, "setting = environment · sway = influence", 41, "the design of the environment in which choices are made can significantly influence the decisions people make"],
  ["Algorithms nudge us only in very obvious ways.", False, "subtly, and sometimes not so subtly → 주로 미묘하게", 41, "they subtly, and sometimes not so subtly, nudge us"],
  ["Nudges can serve good purposes, like promoting healthier routines.", True, "serve purposes · promote = encourage · routines = habits", 41, "such as encouraging healthier habits"],
  ["Manipulation is especially likely when designers' goals conflict with individuals' autonomy.", True, "conflict with = not aligned with", 41, "particularly when the underlying objectives of the architects are not aligned with the well-being or autonomy of the individual"],
  ["The writer advises us to trust algorithmic outputs without question.", False, "without question 의심 없이 → 건전한 회의론을 기르라", 41, "cultivating a healthy skepticism towards the seemingly objective outputs"],
  ["The writer claims that algorithmic data guarantees future prosperity.", False, "guarantee 보장하다 · prosperity = flourishing → 반드시 처방은 아님", 41, "not necessarily a prescription for future flourishing"],
 ],
 ilchi=[
  ilchi(41, T41, True, ["Algorithms are neutral tools designed without any particular goals.", "Choice architecture was popularized in behavioral economics.", "Algorithms shape what options are presented to us.", "Preserving human agency demands a deliberate effort.", "Algorithmic data reflects past realities."],
        "정답: neutral tools without any particular goals → 특정 목표를 가진 인간이 설계(designed by humans with specific goals)\n· shape = curate · present\n· preserve = protect · demand = require · deliberate = conscious\n· reflect = be a reflection of",
        [["알고리즘은 특정 목표 없이 설계된 중립적 도구이다.", "these systems are designed by humans with specific goals", "불일치"],
         ["선택 구조는 행동 경제학에서 대중화되었다.", "popularized in behavioral economics", "일치"],
         ["알고리즘은 우리에게 제시되는 선택지를 정한다.", "what options are presented to us", "일치"],
         ["인간의 주체성을 지키려면 의식적인 노력이 필요하다.", "It requires a conscious effort", "일치"],
         ["알고리즘 데이터는 과거 현실을 반영한다.", "their data is a reflection of past realities", "일치"]]),
  ilchi(41, T41, False, ["We should make choices that run counter to predicted patterns.", "Nudges are always used for harmful purposes.", "Algorithms only present options without influencing our decisions.", "The writer suggests accepting all recommendations from algorithms.", "Human agency naturally grows stronger in an algorithmic world."],
        "정답: run counter to = go against · predicted patterns = predicted grain\n· always harmful → 유익한 목적도 가능\n· without influencing → 우리를 특정 경로로 유도함\n· accepting all → 추천에 도전하라\n· naturally grows → 의식적 노력이 필요",
        [["예측된 패턴을 거스르는 선택을 해야 한다.", "making deliberate choices that go against the predicted grain", "일치"],
         ["넛지는 항상 해로운 목적으로 쓰인다.", "can be used for beneficial purposes", "불일치"],
         ["알고리즘은 결정에 영향을 주지 않고 선택지만 보여 준다.", "nudge us towards particular paths", "불일치"],
         ["필자는 알고리즘의 모든 추천을 받아들이라고 한다.", "challenging algorithmic recommendations", "불일치"],
         ["알고리즘 세상에서 인간의 주체성은 저절로 강해진다.", "It requires a conscious effort", "불일치"]]),
 ],
 pickg=[
  ('The concept of "choice architecture," {popularized|popularizing} in behavioral economics, highlights how the design of the environment in which choices are made can significantly influence the decisions people make.', "개념이 '대중화된' 수동"),
  ('The concept of "choice architecture," popularized in behavioral economics, {highlights|highlight} how the design of the environment in which choices are made can significantly influence the decisions people make.', "주어 The concept(단수) → highlights"),
  ('The concept of "choice architecture," popularized in behavioral economics, highlights how the design of the environment {in which|which} choices are made can significantly influence the decisions people make.', "뒤에 완전한 수동절 → in which"),
  ("By curating what we see, what we {are recommended|recommend}, and what options are presented to us, they subtly, and sometimes not so subtly, nudge us towards particular paths.", "우리가 '추천받는' 수동"),
  ("While nudges can be used for beneficial purposes, such as {encouraging|to encourage} healthier habits, they also carry the potential for manipulation, particularly when the underlying objectives of the architects are not aligned with the well-being or autonomy of the individual.", "such as(전치사) + 동명사"),
  ("While nudges can be used for beneficial purposes, such as encouraging healthier habits, they also carry the potential for manipulation, particularly when the underlying objectives of the architects {are|is} not aligned with the well-being or autonomy of the individual.", "주어 objectives(복수) → are"),
  ("The question then becomes: how can we cultivate and {protect|protecting} our human agency in an increasingly algorithmic world?", "cultivate와 병렬 → protect"),
  ("It means actively seeking out diverse perspectives, challenging algorithmic recommendations, and {making|make} deliberate choices that go against the predicted grain.", "seeking, challenging과 병렬 → making"),
  ("It involves cultivating a healthy skepticism towards the {seemingly|seeming} objective outputs of algorithms and remembering that these systems are designed by humans with specific goals, and that their data is a reflection of past realities, not necessarily a prescription for future flourishing.", "형용사 수식 → 부사 seemingly"),
  ("It involves cultivating a healthy skepticism towards the seemingly objective outputs of algorithms and remembering that these systems {are designed|design} by humans with specific goals, and that their data is a reflection of past realities, not necessarily a prescription for future flourishing.", "시스템이 '설계된' 수동"),
 ],
 verb=[
  ("By ___ what we see, what we are recommended, and what options are presented to us, they subtly, and sometimes not so subtly, nudge us towards particular paths.", 'curate', ['curating'], "By + 동명사"),
  ("While nudges can be ___ for beneficial purposes, such as encouraging healthier habits, they also carry the potential for manipulation, particularly when the underlying objectives of the architects are not aligned with the well-being or autonomy of the individual.", 'use', ['used'], "조동사 + be + p.p."),
  ("While nudges can be used for beneficial purposes, such as encouraging healthier habits, they also carry the potential for manipulation, particularly when the underlying objectives of the architects are not ___ with the well-being or autonomy of the individual.", 'align', ['aligned'], "be aligned with"),
  ("It requires a conscious effort ___ critical engagement with the technologies we use.", 'maintain', ['to maintain'], "명사 수식 to부정사"),
  ("It means actively ___ out diverse perspectives, challenging algorithmic recommendations, and making deliberate choices that go against the predicted grain.", 'seek', ['seeking'], "mean -ing"),
  ("It involves ___ a healthy skepticism towards the seemingly objective outputs of algorithms and remembering that these systems are designed by humans with specific goals, and that their data is a reflection of past realities, not necessarily a prescription for future flourishing.", 'cultivate', ['cultivating'], "involve + 동명사"),
 ],
 error=[
  ('The concept of "choice architecture," [[popularizing]] in behavioral economics, [[highlights]] how the design of the environment [[in which]] choices are made can significantly influence the decisions people [[make]].', 0, 'popularized', "수동 과거분사"),
  ("By curating what we see, what we [[recommend]], and what options [[are presented]] to us, they [[subtly]], and sometimes not so subtly, [[nudge]] us towards particular paths.", 0, 'are recommended', "우리가 '추천받는' 수동"),
  ("While nudges can [[be used]] for beneficial purposes, such as [[encouraging]] healthier habits, they also carry the potential for manipulation, particularly when the underlying objectives of the architects [[is]] not [[aligned]] with the well-being or autonomy of the individual.", 2, 'are', "주어 objectives(복수) → are"),
  ("It means actively [[seeking]] out diverse perspectives, [[challenging]] algorithmic recommendations, and [[make]] deliberate choices that [[go]] against the predicted grain.", 2, 'making', "병렬 → making"),
  ("It involves cultivating a healthy skepticism towards the [[seeming]] objective outputs of algorithms and [[remembering]] that these systems [[are designed]] by humans with specific goals, and that their data [[is]] a reflection of past realities.", 0, 'seemingly', "형용사 수식 → 부사"),
 ],
 scr=[(T41[1][0], T41[1][1]), (T41[5][0], T41[5][1]), ("they also carry the potential for manipulation", "그것들은 조작의 가능성 또한 내포하고 있다"), ("these systems are designed by humans with specific goals", "이러한 시스템은 특정 목표를 가진 인간에 의해 설계되었다")],
 order=[
  ([T41[0][0], T41[1][0], T41[2][0], T41[3][0]], ["선택 구조: 환경 설계가 결정에 큰 영향", "알고리즘 = 디지털 환경의 정교한 설계자", "선별을 통해 우리를 특정 경로로 유도", "넛지는 유익할 수 있지만 조작 가능성도"]),
  ([T41[4][0], T41[5][0], T41[6][0], T41[7][0]], ["질문: 어떻게 주체성을 기르고 지킬까?", "비판적 관계를 유지하는 의식적 노력", "다양한 관점 찾기·추천에 도전·흐름 거스르기", "알고리즘 결과에 대한 건전한 회의론"]),
 ],
 insert=[
  ([T41[0][0], T41[1][0], T41[2][0]], 1, ["선택 구조 개념", "알고리즘은 본질적으로 설계자", "그것들(they)이 우리를 유도"], "알고리즘을 '설계자(architects)'로 연결해야 선택 구조(architecture)와 이어진다."),
  ([T41[4][0], T41[5][0], T41[6][0], T41[7][0]], 2, ["질문 제기", "의식적 노력이 필요(It requires)", "그것은(It means) 구체적으로", "또한(It involves)"], "It requires → It means → It involves로 답을 구체화한다."),
 ],
 odd=[
  ([T41[1][0], T41[2][0], "Many architects today use computer software to design buildings.", T41[3][0]], 2, "건축가 이야기 → 알고리즘 설계자(비유)와 관계없음"),
  ([T41[5][0], T41[6][0], "Smartphone sales have slowed down in many countries.", T41[7][0]], 2, "스마트폰 판매 → 주체성 지키기와 관계없음"),
 ],
 blank=[
  ("By curating what we see, what we are recommended, and what options are presented to us, they subtly, and sometimes not so subtly, ____.", ["nudge us towards particular paths", "leave all choices to us", "stop recommending content", "make us more independent"], "선별 → 특정 경로로 유도"),
  ("While nudges can be used for beneficial purposes, such as encouraging healthier habits, they also carry ____.", ["the potential for manipulation", "no risk at all", "a guarantee of well-being", "the end of autonomy"], "While(~이지만) 뒤 → 부정적 측면"),
  ("It means actively seeking out diverse perspectives, challenging algorithmic recommendations, and making deliberate choices that ____.", ["go against the predicted grain", "follow the most popular trends", "save time and effort", "please the architects"], "주체성 → 예측을 거스름"),
 ],
 gram=[
  (B + 'The concept, ______ in behavioral economics, highlights it.</b>', ['popularized', 'popularizing', 'popularize', 'to popularize'], "수동 과거분사"),
  (B + "the environment ______ choices are made</b>", ['in which', 'which', 'what', 'that which'], "완전한 절 → 전치사 + 관계대명사"),
  (B + "what we ______ by algorithms</b>", ['are recommended', 'recommend', 'recommending', 'have recommended'], "4형식 수동: 우리가 추천받는"),
  (B + "such as ______ healthier habits</b>", ['encouraging', 'to encourage', 'encourage', 'encouraged'], "전치사 such as + 동명사"),
  (B + "how can we cultivate and ______ our agency?</b>", ['protect', 'protecting', 'protected', 'to protecting'], "조동사 뒤 동사원형 병렬"),
  (B + "the ______ objective outputs of algorithms</b>", ['seemingly', 'seeming', 'seem', 'seemed'], "형용사 앞 부사"),
 ])

for st in d4:
    for it in st['items']:
        if st['type'] == 'vocab' and it[2] == 41: it[2] = '41~42'
        elif st['type'] == 'tf' and it[3] == 41: it[3] = '41~42'
        elif isinstance(it, dict) and it.get('n') == 41: it['n'] = '41~42'

PKG = {
 'id': 'h2-mock-2609-angok', 'school': '고2 모의고사(2026년 9월 학평·안곡고)', 'unit': '24·29·30·34·38·40·41~42번', 'title': 'September 2026 Mock Test',
 'titleKo': '2026년 9월 고2 학력평가 · 안곡고 내신 범위', 'exam': '내신·모의고사', 'prose': True, 'teacherPhone': '',
 'days': [
  {'id': 'd1', 'name': 'DAY 1', 'range': '24·29번', 'story': '24 제목 · 29 어법', 'passage': sec('24번 · 제목') + rows(T24) + sec('29번 · 어법') + rows(T29), 'steps': d1},
  {'id': 'd2', 'name': 'DAY 2', 'range': '30·34번', 'story': '30 어휘 · 34 빈칸', 'passage': sec('30번 · 어휘') + rows(T30) + sec('34번 · 빈칸') + rows(T34), 'steps': d2},
  {'id': 'd3', 'name': 'DAY 3', 'range': '38·40번', 'story': '38 문장 넣기 · 40 요약', 'passage': sec('38번 · 문장 넣기') + rows(T38) + sec('40번 · 요약') + rows(T40), 'steps': d3},
  {'id': 'd4', 'name': 'DAY 4', 'range': '41~42번', 'story': '41 제목 · 42 어휘 (장문)', 'passage': sec('41~42번 · 장문') + rows(T41), 'steps': d4},
 ]}
write(PKG, '/home/claude/proj/data/h2-mock-2609-angok.js',
      "/* 고2 2026년 9월 학력평가(인천광역시교육청) · 안곡고 내신 범위 24·29·30·34·38·40·41~42번\n"
      "   이 파일은 scratchpad/gen_m2609.py 로 만들었음. 지문은 정답이 반영된 원문, 실전 문항에는 시험지 원문(밑줄·빈칸) 그대로 */\n")
print('ok')
