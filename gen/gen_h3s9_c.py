# 9월 모평 DAY 42~50 : 43~45 장문 → 21 함축 → 38 삽입 → 32 빈칸 → 41·42 장문 → 37 순서 → 33 빈칸 → 39 삽입 → 34 빈칸  (gen_h3s9.py 안에서 exec)

# ═══ 43~45번 장문 ═══
TA = [("Tim adopted a dog a few months ago.", "Tim은 몇 달 전에 개 한 마리를 입양했다."),
      ("When he met his dog for the first time, he named him after his favorite character, Mickey.", "개를 처음 만났을 때, 그는 자신이 가장 좋아하는 캐릭터인 Mickey의 이름을 따서 개의 이름을 지었다."),
      ("Mickey was a healthy dog, but he soon seemed to lack energy.", "Mickey는 건강한 개였지만, 얼마 안 가 기운이 없어 보였다."),
      ("Tim thought that taking care of a dog was much harder than he had expected.", "Tim은 개를 돌보는 것이 예상했던 것보다 훨씬 더 어렵다고 생각했다."),
      ("So, he decided to sign up for a dog training course.", "그래서 그는 개 훈련 과정에 등록하기로 결심했다."),
      ("At the training center, he met an instructor named Jack.", "훈련 센터에서 그는 Jack이라는 이름의 강사를 만났다."),
      ("He emphasized to Tim, “Be sure to walk your dog daily. Dogs need regular exercise to be happy and healthy.”", "그는 Tim에게 “당신의 개를 매일 꼭 산책시키세요. 개들은 행복하고 건강하려면 규칙적인 운동이 필요해요.”라고 강조했다.")]
TB = [("When Tim and Mickey arrived at the park Jack had recommended, dozens of dogs were already jumping and playing.", "Tim과 Mickey가 Jack이 추천했던 공원에 도착했을 때, 수십 마리의 개들이 이미 뛰어다니며 놀고 있었다."),
      ("Mickey looked nervous in the unfamiliar surroundings.", "Mickey는 낯선 환경에서 불안해 보였다."),
      ("Tim said, “Don’t worry, Mickey. It’ll be fun.”", "Tim은 “걱정하지 마, Mickey. 재미있을 거야.”라고 말했다."),
      ("Just then, Tim saw a boy about his age standing with a small dog.", "바로 그때, Tim은 작은 개와 함께 서 있는, 자신과 비슷한 나이의 소년을 보았다."),
      ("Gathering his courage, Tim walked over to him.", "용기를 내어 Tim은 그에게 걸어갔다."),
      ("“Hi, I’m Tim. Can I introduce my dog to yours?”", "“안녕하세요, 저는 Tim이에요. 제 개를 당신의 개에게 인사시켜도 될까요?”"),
      ("The boy replied, “Sure. I’m Daniel. Oh, it looks like they like each other already!”", "소년은 “물론이죠. 저는 Daniel이에요. 오, 벌써 서로 좋아하는 것 같아요!”라고 대답했다.")]
TC = [("Having something in common as dog owners, Tim and Daniel enjoyed talking to each other.", "반려견 주인으로서 공통점이 있었기 때문에, Tim과 Daniel은 서로 이야기하는 것을 즐겼다."),
      ("They spent the next two hours pleasantly chatting and decided to walk their dogs together regularly.", "그들은 그 뒤 두 시간 동안 즐겁게 이야기를 나누며 보냈고, 자신들의 개를 정기적으로 함께 산책시키기로 했다."),
      ("“See you soon,” said Tim as he and Mickey left the park.", "그와 Mickey가 공원을 떠나면서 Tim은 “곧 봐요.”라고 말했다."),
      ("Over the next few weeks, the boys and their dogs became great friends.", "그 후 몇 주 동안, 소년들과 그들의 개들은 아주 좋은 친구가 되었다."),
      ("After returning from a walk one day, Tim said to Mickey, “Walking you felt like a burden at first, but now I see doing things for you can be great for me, too!”", "어느 날 산책에서 돌아온 후, Tim은 Mickey에게 “처음에는 너를 산책시키는 것이 부담처럼 느껴졌지만, 이제는 너를 위해 무언가를 하는 것이 나에게도 참 좋을 수 있다는 걸 알겠어!”라고 말했다.")]
TDd = [("Being sure to follow Jack’s advice, Tim took Mickey for a walk every day.", "Jack의 조언을 확실히 따르며, Tim은 Mickey를 매일 산책시켰다."),
       ("However, this extra responsibility soon seemed like a burden, and Tim felt exhausted.", "하지만 이 추가적인 책임은 곧 부담처럼 느껴졌고, Tim은 지쳤다."),
       ("One day, Tim got a call from Jack.", "어느 날, Tim은 Jack에게 전화를 받았다."),
       ("“Hello, Tim. How’s everything going with Mickey?”", "“안녕하세요, Tim. Mickey와는 잘 지내고 있나요?”"),
       ("Tim replied, “Actually, it’s pretty hard walking him every day. We’ve been taking the same route, and it has become a little boring.”", "Tim은 “사실, 개를 매일 산책시키는 게 꽤 힘들어요. 계속 같은 길로 산책하고 있는데, 그게 좀 지루해졌어요.”라고 대답했다."),
       ("Jack offered him a new idea.", "Jack은 그에게 새로운 아이디어를 제안했다."),
       ("“How about going to Happy Dog Park?”", "“Happy Dog Park에 가 보는 건 어때요?”"),
       ("Tim said, “That’s a great idea!”", "Tim은 “정말 좋은 생각이에요!”라고 말했다.")]
P43 = ['<b>(A)</b> ' + para(TA, [(6, 'walk your dog', 'walk (a)<u>your</u> dog')]),
       '<b>(B)</b> ' + para(TB, [(3, 'about his age', 'about (b)<u>his</u> age')]),
       '<b>(C)</b> ' + para(TC, [(2, 'as he and', 'as (c)<u>he</u> and'), (4, 'for you can', 'for (d)<u>you</u> can')]),
       '<b>(D)</b> ' + para(TDd, [(5, 'offered him', 'offered (e)<u>him</u>')])]
T43 = [('(A) ' + TA[0][0], '(A) ' + TA[0][1])] + TA[1:] + [('(D) ' + TDd[0][0], '(D) ' + TDd[0][1])] + TDd[1:] + [('(B) ' + TB[0][0], '(B) ' + TB[0][1])] + TB[1:] + [('(C) ' + TC[0][0], '(C) ' + TC[0][1])] + TC[1:]
V43 = [('adopt', '입양하다'), ('name A after B', 'B의 이름을 따서 A의 이름을 짓다'), ('lack', '~이 없다, 부족하다'), ('take care of', '~을 돌보다'), ('sign up for', '~에 등록하다'), ('instructor', '강사'),
       ('emphasize', '강조하다'), ('regular', '규칙적인'), ('recommend', '추천하다'), ('dozens of', '수십의'), ('unfamiliar', '낯선'), ('surroundings', '환경'),
       ('gather one’s courage', '용기를 내다'), ('introduce', '소개하다'), ('have something in common', '공통점이 있다'), ('pleasantly', '즐겁게'), ('chat', '이야기를 나누다'), ('burden', '부담'),
       ('advice', '조언'), ('extra', '추가적인'), ('responsibility', '책임'), ('exhausted', '지친'), ('route', '길, 경로')]
K43 = [(TA[3][0], TA[3][1], "much + 비교급(harder) 훨씬 더 · than he had expected 과거완료(생각한 것보다 더 이전에 예상했던)"),
       (TC[0][0], TC[0][1], "분사구문(이유) Having something in common = Because they had ~ · enjoy -ing ~하는 것을 즐기다"),
       (TC[4][0], TC[4][1], "동명사 주어 Walking you felt ~ / doing things for you can be ~ (see 뒤 that 생략된 명사절의 동명사 주어)")]
day(43, 'q43', '순서', '장문 순서 · 조언(A) → 지침(D) → 공원(B) → 친구(C)', '주어진 글 (A)에 이어질 내용을 순서에 맞게 배열한 것으로 가장 적절한 것은?', T43,
 ['(B) - (D) - (C)', '(C) - (B) - (D)', '(C) - (D) - (B)', '(D) - (B) - (C)', '(D) - (C) - (B)'], 3,
 '(A) 강사 Jack: 개를 매일 산책시키라 → (D) Jack의 조언을 따라(Being sure to follow Jack’s advice) 매일 산책 → 지치고 지루함 → Jack이 Happy Dog Park를 추천 → (B) Jack이 추천한 공원(the park Jack had recommended)에 도착, Daniel을 만남 → (C) 공통점으로 친해져 함께 산책하기로 함, 몇 주 뒤 깨달음. 그래서 ④ (D)-(B)-(C).',
 ['①② (B)나 (C)가 먼저 오면, “Jack이 추천한 공원”이 아직 추천되지 않았어요.',
  '③ (C)의 Daniel은 (B)에서 처음 만나는 사람이에요. (B)보다 먼저 올 수 없어요.',
  '⑤ (D) 뒤에 (C)가 오면 Daniel을 만나지도 않았는데 “Tim과 Daniel”이 대화해요.'],
 '장문 순서는 앞 단락에 나온 말을 다시 받는 표현(Jack’s advice, the park Jack had recommended)과 새 인물이 처음 등장하는 단락(a boy → Daniel)을 찾으세요.',
 K43, V43, ['adopt', 'lack', 'instructor', 'emphasize', 'regular', 'recommend', 'unfamiliar', 'surroundings', 'burden', 'responsibility', 'exhausted', 'route'],
 paras=P43)
day(44, 'q44', '지칭', '장문 지칭', '밑줄 친 (a)~(e) 중에서 가리키는 대상이 나머지 넷과 다른 것은?', T43,
 ['(a)', '(b)', '(c)', '(d)', '(e)'], 3,
 '(d) you는 Tim이 Mickey에게 하는 말 속의 “너” = Mickey(개)예요. “너를 위해 무언가를 하는 것이 나에게도 좋을 수 있다.” 나머지는 모두 Tim이에요.',
 ['(a) your dog: 강사 Jack이 Tim에게 “당신의 개” → Tim',
  '(b) his age: Tim이 본 소년이 “그(Tim)와 비슷한 나이” → Tim',
  '(c) he: “곧 봐요”라고 말하며 Mickey와 함께 공원을 떠난 사람 → Tim',
  '(e) him: Jack이 새로운 아이디어를 제안한 상대 → Tim'],
 '지칭 문제는 따옴표 안의 you, your에 특히 주의하세요. 누가 누구에게 하는 말인지(Jack → Tim / Tim → Mickey)를 먼저 확인하면 바로 풀려요.',
 [], V43, [], paras=P43)
day(45, 'q45', '내용 불일치', '장문 내용 일치', '윗글에 관한 내용으로 적절하지 <u>않은</u> 것은?', T43,
 ['Mickey는 Tim이 좋아하는 캐릭터의 이름이었다.', 'Mickey는 공원에 도착하자마자 즐겁게 뛰어다녔다.', 'Tim은 Mickey를 다른 개에게 소개하려 했다.', 'Tim과 Daniel은 자신의 개를 함께 산책시키기로 했다.', 'Tim은 Jack과의 통화에서 고민을 이야기했다.'], 1,
 '공원에서 즐겁게 뛰어놀던 것은 이미 와 있던 수십 마리의 다른 개들(dozens of dogs were already jumping and playing)이에요. Mickey는 낯선 환경에서 불안해 보였어요(Mickey looked nervous in the unfamiliar surroundings).',
 ['① he named him after his favorite character, Mickey → 일치',
  '③ Can I introduce my dog to yours? → 일치',
  '④ decided to walk their dogs together regularly → 일치',
  '⑤ it’s pretty hard walking him every day ~ it has become a little boring → 통화에서 고민을 이야기함 → 일치'],
 '장문 일치는 주어를 꼭 확인하세요. “뛰어다녔다”는 행동의 주인이 Mickey인지 다른 개들(dozens of dogs)인지 바꿔 놓는 것이 단골 함정이에요.',
 [], V43, [], paras=P43)
multi('43~45번 장문 (순서·지칭·일치)', 3)

# ═══ 21번 함축 의미 ═══
T21 = [
 ("Social media companies are working to keep you on site or attempting to deliver results useful to you.", "소셜 미디어 기업들은 여러분을 사이트에 머물게 하려고 노력하거나 여러분에게 유용한 결과를 제공하려고 시도하고 있다."),
 ("You can see this personalization reflected in the results of search engines, which try to maximize relevance: searching for “bakery” in New York should return different results than searching in Paris.", "여러분은 관련성을 최대화하려고 노력하는 검색 엔진의 결과에 반영된 이러한 개인화를 볼 수 있는데, 뉴욕에서 ‘빵집’을 검색하는 것은 파리에서 검색하는 것과 다른 결과를 내놓아야 한다."),
 ("Features like the little predictive-text cues of autocomplete also look to maximize relevance by suggesting refinements: typing in “cats” might prompt the user with “cats movie” or “cats that don’t shed.”", "자동 완성의 작은 예측 입력 단서 같은 기능들도 다듬어진 검색어를 제안함으로써 관련성을 최대화하려고 하는데, ‘고양이’를 입력하면 사용자에게 ‘고양이 영화’나 ‘털 안 빠지는 고양이’를 제시할지도 모른다."),
 ("Autocomplete suggestions offer a look into the algorithm’s understanding of accumulated user behavior ― an immensely important part of how key social media algorithms work.", "자동 완성 제안은 누적된 사용자 행동에 대한 알고리즘의 이해를 들여다볼 수 있게 해 주는데, 이는 주요 소셜 미디어 알고리즘이 작동하는 방식의 매우 중요한 부분이다."),
 ("The outputs are personalized, but the data sets are massive, and the platforms are mining for similarities across vast quantities of user information.", "결과물은 개인화되지만, 데이터 세트는 거대하며 플랫폼은 방대한 양의 사용자 정보 전체에서 유사성을 채굴하고 있다."),
 ("If a whole lot of users near you or similar to you complete the search that you’ve begun with specific words, the autocomplete algorithm takes that into account and may be more likely to suggest them to you.", "여러분 근처에 있거나 여러분과 비슷한 수많은 사용자가 여러분이 특정 단어로 시작한 검색을 완성한다면, 자동 완성 알고리즘은 그것을 고려하여 그 단어들을 여러분에게 제안할 가능성이 더 높을 수 있다."),
 ("Since the results are derived from data related to millions of searches, autocomplete is, in a sense, holding a mirror up to society.", "그 결과는 수백만 건의 검색과 관련된 데이터에서 도출되기 때문에, 자동 완성은 어떤 의미에서 사회에 거울을 비추고 있는 것이다."),
]
day(21, 'q21', '함축 의미', '밑줄 함축 의미 · 거울 = 많은 사람의 공통점을 그대로 보여 줌', '밑줄 친 holding a mirror up to society가 다음 글에서 의미하는 바로 가장 적절한 것은?', T21,
 ['manipulating search results in favor of the socially influential', 'revealing commonalities in users and their shared interests', 'censoring personal data utilizing social media algorithms', 'collecting information useful for building user networks', 'examining apparently random data to find regularity'], 1,
 '거울은 앞에 있는 것을 “그대로 비춰 보여 주는” 물건이에요. 자동 완성은 수백만 건의 검색 데이터에서 나오고, 나와 비슷한 수많은 사용자가 완성한 검색어를 제안해요(mining for similarities). → 사회(많은 사용자)의 공통점과 공유된 관심사를 그대로 드러낸다 = ② revealing commonalities in users and their shared interests.',
 ['① 영향력 있는 사람에게 유리하게 결과를 ‘조작’한다 → 거울은 있는 그대로 비출 뿐 조작하지 않아요.',
  '③ 개인 데이터를 ‘검열’한다 → 나오지 않아요.',
  '④ 사용자 네트워크를 만들기 위한 정보 수집 → 정보를 모으는 목적이 네트워크 구축이 아니에요.',
  '⑤ 무작위 데이터에서 규칙성을 찾는다 → mining for similarities와 비슷해 보이지만, “사회를 비춘다(사람들의 공통 관심사를 보여 준다)”는 핵심이 빠졌어요. (가장 매력적인 오답)'],
 '함축 의미는 밑줄 바로 앞의 이유(Since ~ millions of searches)와 비유의 기본 뜻(거울 = 그대로 비춤)을 합치세요. 많은 사람의 데이터 → 사회의 모습을 보여 줌.',
 [(T21[1][0], T21[1][1], "see + O + p.p.(reflected) ~가 반영된 것을 보다 · 콤마 + which (= search engines) · return different results than ~ ~와 다른 결과를 내놓다"),
  (T21[5][0], T21[5][1], "the search that you’ve begun (목적격 관계대명사 that) · take ~ into account ~을 고려하다 · be likely to ~할 가능성이 있다"),
  (T21[6][0], T21[6][1], "be derived from ~에서 도출되다 · data related to ~ ~와 관련된 데이터 · hold a mirror up to ~을 거울에 비추다(그대로 보여 주다)")],
 [('attempt', '시도하다'), ('deliver', '제공하다, 전달하다'), ('personalization', '개인화'), ('reflect', '반영하다'), ('maximize', '최대화하다'), ('relevance', '관련성'),
  ('predictive', '예측의'), ('cue', '단서'), ('autocomplete', '자동 완성'), ('refinement', '다듬어진 검색어'), ('prompt', '(입력을) 유도하다, 제시하다'), ('shed', '털이 빠지다'),
  ('accumulated', '누적된'), ('immensely', '매우, 엄청나게'), ('massive', '거대한'), ('mine', '채굴하다, 탐색하다'), ('take ~ into account', '~을 고려하다'), ('derive', '도출하다, 얻다'),
  ('commonality', '공통점'), ('manipulate', '조작하다'), ('censor', '검열하다')],
 ['personalization', 'reflect', 'maximize', 'relevance', 'predictive', 'accumulated', 'immensely', 'massive', 'derive', 'commonality', 'manipulate', 'censor'],
 u='holding a mirror up to society', three=True)

# ═══ 38번 문장 삽입 ═══
G38 = "Citizen engagement involves people helping governments, rather than scientists, to improve public services and policies in their communities."
S38 = [
 ("The growth and success of citizen science and citizen engagement has been made possible by the Internet and mobile technology, encouraging and coordinating the efforts of millions of people throughout the world.", "시민 과학과 시민 참여의 성장과 성공은 인터넷과 모바일 기술에 의해 가능해졌는데, 이것들은 전 세계 수백만 명의 노력을 장려하고 조정한다."),
 ("Websites, smartphone apps, and social media have been instrumental in expanding the reach and impact of a diversity of citizen science projects across time and geographical zones.", "웹사이트, 스마트폰 앱, 소셜 미디어는 시간과 지리적 구역을 넘어 다양한 시민 과학 프로젝트의 범위와 영향력을 넓히는 데 중요한 역할을 해 왔다."),
 ("Citizen science involves local people helping scientists carry out a scientific project at scale.", "시민 과학은 지역 사람들이 과학자가 대규모 과학 프로젝트를 수행하는 것을 돕는 것을 포함한다."),
 ("Currently, thousands of such projects have been set up all over the world, whereby volunteers help out in a number of research areas, including biodiversity, air quality, astronomy, and environmental issues.", "현재 수천 개의 그런 프로젝트가 전 세계에 만들어져 있고, 이를 통해 자원봉사자들은 생물 다양성, 대기 질, 천문학, 환경 문제를 포함한 여러 연구 분야에서 돕는다."),
 ("They do so by participating in scientific activities such as monitoring plants and wildlife, collecting air and water samples, categorizing galaxies, and analyzing DNA sequences.", "그들은 식물과 야생 동물을 관찰하고, 공기와 물 표본을 수집하고, 은하를 분류하고, DNA 서열을 분석하는 것 같은 과학 활동에 참여함으로써 그렇게 한다."),
 ("Examples include setting up and managing a website that offers local services for community disasters and creating an emergency response team when a disaster occurs.", "예로는 지역 사회 재난에 대비한 지역 서비스를 제공하는 웹사이트를 만들고 관리하는 것, 그리고 재난이 발생했을 때 비상 대응팀을 만드는 것이 있다."),
]
day(38, 'q38', '삽입', '문장 삽입 · 과학자 돕기(시민 과학) → 정부 돕기(시민 참여) 전환점', '글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳은?',
 S38[:5] + [(G38, "(⑤ 자리) 시민 참여는 사람들이 과학자가 아니라 정부를 도와 지역 사회의 공공 서비스와 정책을 개선하는 것을 포함한다.")] + S38[5:],
 ['①', '②', '③', '④', '⑤'], 4,
 '첫 문장에서 citizen science(시민 과학)와 citizen engagement(시민 참여) 두 가지를 소개해요. ③~⑤ 앞까지는 모두 시민 과학(과학자를 도움, 과학 활동) 이야기예요. ⑤ 뒤의 Examples include … 재난 대비 지역 서비스 웹사이트, 비상 대응팀 → 과학 활동이 아니라 정부·지역 사회를 돕는 일이에요. 그러니 그 앞에 “시민 참여는 과학자가 아니라 정부를 돕는 것”이라는 주어진 문장이 들어가야 해요.',
 ['①② 아직 시민 과학이 무엇인지도 설명하기 전이에요. rather than scientists(과학자가 아니라)는 시민 과학 설명이 끝난 뒤에 와야 대조가 돼요.',
  '③ 바로 뒤 Currently, thousands of such projects(그런 프로젝트)는 시민 과학의 과학 프로젝트를 가리켜요. 여기에 넣으면 such projects가 정부 일이 돼 버려요.',
  '④ 바로 뒤 They do so by … scientific activities는 여전히 시민 과학 자원봉사자 이야기예요.'],
 '삽입 문제는 글에서 흐름이 “뚝 끊기는 곳”을 찾으세요. ⑤ 뒤의 Examples(재난 웹사이트·비상 대응팀)는 앞의 과학 활동과 전혀 다른 예라서, 그 사이에 새 개념(시민 참여)을 소개하는 문장이 필요해요.',
 [(G38, "시민 참여는 사람들이 과학자가 아니라 정부를 도와 지역 사회의 공공 서비스와 정책을 개선하는 것을 포함한다.", "involve + 의미상 주어(people) + -ing(helping) · help + O + to부정사 · A rather than B B가 아니라 A"),
  (S38[2][0], S38[2][1], "involve local people helping ~ (동명사 helping의 의미상 주어 local people) · help + O + 동사원형(carry out) · at scale 대규모로"),
  (S38[3][0], S38[3][1], "have been set up 현재완료 수동 · whereby = by which 그것에 의해, 그것을 통해 · including ~을 포함하여")],
 [('citizen science', '시민 과학'), ('engagement', '참여'), ('policy', '정책'), ('coordinate', '조정하다'), ('instrumental', '중요한 역할을 하는'), ('expand', '확장하다'),
  ('reach', '범위, 영향권'), ('diversity', '다양성'), ('geographical', '지리적인'), ('carry out', '수행하다'), ('at scale', '대규모로'), ('whereby', '그것에 의해'),
  ('volunteer', '자원봉사자'), ('biodiversity', '생물 다양성'), ('astronomy', '천문학'), ('monitor', '관찰하다'), ('categorize', '분류하다'), ('galaxy', '은하'),
  ('sequence', '서열'), ('disaster', '재난'), ('emergency', '비상(사태)')],
 ['engagement', 'policy', 'coordinate', 'instrumental', 'expand', 'diversity', 'geographical', 'volunteer', 'astronomy', 'categorize', 'disaster', 'emergency'],
 given=G38, paras=[esc(S38[0][0]) + ' ( ① ) ' + esc(S38[1][0]) + ' ( ② ) ' + esc(S38[2][0]) + ' ( ③ ) ' + esc(S38[3][0]) + ' ( ④ ) ' + esc(S38[4][0]) + ' ( ⑤ ) ' + esc(S38[5][0])])

# ═══ 32번 빈칸 ═══
day(32, 'q32', '빈칸', '빈칸 추론 · 빈칸 뒤 결과(놀라게 하기 어렵다)의 원인 찾기', '다음 빈칸에 들어갈 말로 가장 적절한 것은?', [
 ("Not only are our sensory systems organized to detect change, but they are most tuned to stimuli that are unexpected and surprising.", "우리의 감각 체계는 변화를 감지하도록 구성되어 있을 뿐만 아니라, 예상치 못하고 놀라운 자극에 가장 맞춰져 있다."),
 ("When you move your body and produce tactile sensations, these stimuli are less noticeable to you than are sensations produced by another individual.", "여러분이 몸을 움직여 촉각을 만들어 낼 때, 이 자극은 다른 사람이 만들어 내는 감각보다 여러분에게 덜 두드러진다."),
 ("The sensations of your own legs touching one another when you cross your legs, for example, are generally less noticeable than a similar touch on your leg would be if someone sitting next to you brushed their leg against yours.", "예를 들어, 다리를 꼬았을 때 자신의 다리가 서로 닿는 감각은, 옆에 앉은 누군가가 자기 다리를 여러분의 다리에 스칠 경우 느껴질 비슷한 접촉보다 일반적으로 덜 두드러진다."),
 ("Likewise, your reaction to your cat jumping onto your lap is likely to be much greater if you have your eyes closed when it happens.", "마찬가지로, 고양이가 여러분의 무릎 위로 뛰어오르는 것에 대한 반응은 그 일이 일어날 때 눈을 감고 있다면 훨씬 더 클 것이다."),
 ("This differential response to surprising tactile stimuli appears to be a defense mechanism that has adaptive significance.", "놀라운 촉각 자극에 대한 이러한 상이한 반응은 적응의 의미를 지닌 방어 기제인 것으로 보인다."),
 ("It is probably also the reason why being tickled by someone else is more effective at producing an emotional reaction than trying to tickle yourself.", "그것은 아마도 또한 다른 사람에게 간지럼을 당하는 것이 스스로 간지럽히려고 하는 것보다 감정적 반응을 일으키는 데 더 효과적인 이유일 것이다."),
 ("Our enjoyment of being tickled generally diminishes as we age.", "간지럼을 당하는 것에 대한 우리의 즐거움은 나이가 들면서 일반적으로 줄어든다."),
 ("This is likely due to the fact that adults are better at anticipating stimuli, and hence are more difficult to surprise, than are children.", "이것은 아마도 성인이 어린이보다 자극을 더 잘 예상하고, 그래서 놀라게 하기가 더 어렵다는 사실 때문일 것이다."),
], ['more cautious of acting immediately', 'less sensitive to others’ reactions', 'stronger in their ability to focus', 'slower in adapting to changes', 'better at anticipating stimuli'], 4,
 '첫 문장: 감각은 “예상치 못한(unexpected) 놀라운 자극”에 가장 맞춰져 있다. 내가 만든 자극, 눈을 뜨고 보는 자극처럼 예상 가능한 것은 덜 느껴진다. 빈칸 뒤: and hence(그래서) 놀라게 하기가 더 어렵다 → 빈칸은 그 원인 = 자극을 더 잘 예상한다(better at anticipating stimuli).',
 ['① 즉각 행동하는 것에 더 조심한다 → 행동 이야기가 아니라 감각·예상 이야기예요.',
  '② 다른 사람의 반응에 덜 민감하다 → 남의 반응이 아니라 자극을 예상하느냐가 핵심이에요.',
  '③ 집중하는 능력이 더 강하다 → 집중력은 나오지 않아요.',
  '④ 변화에 적응하는 것이 더 느리다 → 느리게 적응하면 오히려 더 잘 놀라겠죠. 방향이 반대예요.'],
 '빈칸 뒤에 and hence, so, therefore가 있으면 “빈칸 = 원인, 뒤 = 결과”예요. 결과(놀라게 하기 어렵다)를 만드는 원인을 첫 문장의 핵심(unexpected 자극에 반응)에서 찾으세요.',
 [("Not only are our sensory systems organized to detect change, but they are most tuned to stimuli that are unexpected and surprising.", "우리의 감각 체계는 변화를 감지하도록 구성되어 있을 뿐만 아니라, 예상치 못하고 놀라운 자극에 가장 맞춰져 있다.", "Not only + be동사 + 주어 (부정어 도치) ~, but … · be tuned to ~에 맞춰져 있다"),
  ("Likewise, your reaction to your cat jumping onto your lap is likely to be much greater if you have your eyes closed when it happens.", "마찬가지로, 고양이가 무릎 위로 뛰어오르는 것에 대한 반응은 그 일이 일어날 때 눈을 감고 있다면 훨씬 더 클 것이다.", "your cat jumping (동명사의 의미상 주어) · have + O + p.p.(your eyes closed) 눈을 감은 상태로 · much + 비교급"),
  ("This is likely due to the fact that adults are better at anticipating stimuli, and hence are more difficult to surprise, than are children.", "이것은 아마도 성인이 어린이보다 자극을 더 잘 예상하고, 그래서 놀라게 하기가 더 어렵다는 사실 때문일 것이다.", "the fact that ~ (동격) · be better at -ing ~을 더 잘하다 · than are children (than 뒤 도치)")],
 [('sensory', '감각의'), ('organize', '구성하다'), ('detect', '감지하다'), ('tune', '맞추다'), ('stimulus', '자극 (복수 stimuli)'), ('tactile', '촉각의'),
  ('sensation', '감각'), ('noticeable', '두드러진'), ('brush', '스치다'), ('likewise', '마찬가지로'), ('differential', '상이한, 차이를 보이는'), ('defense mechanism', '방어 기제'),
  ('adaptive', '적응의'), ('significance', '의미, 중요성'), ('tickle', '간지럽히다'), ('diminish', '줄어들다'), ('hence', '그래서'), ('anticipate', '예상하다'),
  ('cautious', '조심하는')],
 ['sensory', 'detect', 'stimulus', 'sensation', 'noticeable', 'likewise', 'adaptive', 'significance', 'tickle', 'diminish', 'anticipate', 'cautious'],
 blank='better at anticipating stimuli', notes='* tactile: 촉각의 ** tickle: 간질이다')

# ═══ 41·42번 장문 ═══
T41 = [
 ("In a consumer research classic, Maloney proposed that the disbelief most people experience when encountering exaggerated product claims is often overwhelmed by a natural curiosity.", "소비자 연구 분야의 고전적인 연구에서, Maloney는 대부분의 사람이 제품에 관한 과장된 주장을 접할 때 경험하는 불신이 흔히 자연스러운 호기심에 의해 압도된다는 견해를 제시했다."),
 ("When advertising information conflicts with existing beliefs, the resulting disagreement must be somehow resolved.", "광고 정보가 기존의 믿음과 충돌할 때, 그 결과로 생기는 불일치는 어떻게든 해소되어야 한다."),
 ("This is often done by yielding to the message and trying out the product in an attempt to readjust personal attitudes toward the brand.", "이는 흔히 그 브랜드에 대한 개인의 태도를 재조정하려는 시도로 메시지를 받아들이고 제품을 사용해 봄으로써 이루어진다."),
 ("In his study, a sample of housewives was exposed to advertisements for food products and then divided into two groups: those participants that found the ad claims to be believable and the others that thought they were hard to believe.", "그의 연구에서 표본으로 선정된 주부들은 식품 광고에 노출된 다음 두 집단, 즉 광고의 주장을 믿을 만하다고 여긴 참가자들과 그것을 믿기 어렵다고 생각한 나머지 참가자들로 나뉘었다."),
 ("The latter group was further divided into two groups, those who confidently disbelieved the claims and those who had what Maloney described as a curious nonbelief.", "후자의 집단은 다시 두 집단, 즉 확신을 갖고 그 주장을 불신한 사람들과 Maloney가 ‘호기심 어린 불신’이라고 묘사한 태도를 지닌 사람들로 나뉘었다."),
 ("The latter was tied into beliefs that actual product experience was necessary to fully judge the claims.", "후자는 그 주장을 충분히 판단하려면 실제 제품 경험이 필요하다는 믿음과 연결되어 있었다."),
 ("Few consumers who clearly disbelieved the message were interested in trying the product (18%).", "메시지를 분명히 불신한 소비자 중 제품을 사용해 보는 데 관심이 있었던 사람은 거의 없었다(18퍼센트)."),
 ("However, Maloney’s results showed that more consumers who were in the curious nonbelief group were ready to try the product (44%) than in the group that expressed no concerns about (i.e., believed) the advertising claims (34%).", "그러나 Maloney의 결과는 호기심 어린 불신 집단의 소비자들(44퍼센트)이 광고의 주장에 아무런 우려를 표하지 않은(즉, 믿은) 집단(34퍼센트)보다 더 많이 제품을 사용해 볼 준비가 되어 있었다는 것을 보여 주었다."),
 ("The results suggest that advertising that causes consumers not to believe the message claims but makes them curious may be the most effective form of new product advertising.", "이 결과는 소비자들이 메시지의 주장을 믿지 않게 하면서도 그들이 호기심을 갖게 만드는 광고가 신제품 광고의 가장 효과적인 형태일 수 있음을 시사한다. (시험지의 indifferent → curious)"),
 ("Convincing consumers that the claims about a new product are true is not necessary to create interest in product trial.", "제품을 사용해 보는 데 관심을 갖게 하기 위해 신제품에 관한 주장이 사실이라고 소비자들을 납득시킬 필요는 없다."),
]
Q41 = para(T41, [(2, 'by yielding', 'by (a)<u>yielding</u>'), (4, 'who confidently', 'who (b)<u>confidently</u>'), (5, 'was necessary', 'was (c)<u>necessary</u>'),
                 (8, 'them curious', 'them (d)<u>indifferent</u>'), (9, 'to create interest', 'to (e)<u>create</u> interest')])
V41 = [('consumer', '소비자'), ('classic', '고전(적인 연구)'), ('propose', '견해를 제시하다, 제안하다'), ('disbelief', '불신'), ('encounter', '접하다, 마주치다'), ('exaggerated', '과장된'),
       ('claim', '주장'), ('overwhelm', '압도하다'), ('curiosity', '호기심'), ('conflict with', '~과 충돌하다'), ('existing', '기존의'), ('disagreement', '불일치'),
       ('resolve', '해소하다, 해결하다'), ('yield to', '~을 받아들이다, ~에 굴복하다'), ('try out', '시험 삼아 사용해 보다'), ('readjust', '재조정하다'), ('attitude', '태도'), ('be exposed to', '~에 노출되다'),
       ('believable', '믿을 만한'), ('the latter', '후자'), ('confidently', '확신을 갖고'), ('concern', '우려'), ('indifferent', '무관심한'), ('convince', '납득시키다'),
       ('trial', '시험 사용, 시도')]
K41 = [(T41[0][0], T41[0][1], "propose that ~ ~라는 견해를 제시하다 · the disbelief (that) most people experience (목적격 관계대명사 생략) / 동사 is overwhelmed · when encountering = when they encounter"),
       (T41[7][0], T41[7][1], "more consumers ~ (44%) than in the group ~ (34%) 비교 · express no concerns about ~에 아무 우려도 표하지 않다"),
       (T41[8][0], T41[8][1], "cause + O + not to부정사 ~가 …하지 않게 하다 · make + O + 형용사(curious) · 주어 advertising (that ~) / 동사 may be")]
day(41, 'q41', '제목', '장문 제목 · 결론(호기심 > 믿음)을 담은 제목', '윗글의 제목으로 가장 적절한 것은?', T41,
 ['Why Do Advertisers Trick Careless People?', 'Accurate Claims Matter for Consumer Trust', 'Curiosity over Truth: How to Attract Consumers', 'How Can We Deal with Exaggerated Product Claims?', 'To Buy or Not to Buy? What Makes Consumers Hesitate'], 2,
 '첫 문장: 과장된 주장에 대한 불신은 자연스러운 호기심에 압도된다. 실험 결과: 광고를 믿은 집단(34%)보다 “믿지 않지만 호기심을 가진” 집단(44%)이 제품을 더 사용해 보려 했다. 결론: 주장이 사실이라고 납득시킬 필요는 없다. → 진실보다 호기심: 소비자를 끌어들이는 방법 = ③.',
 ['① 광고주가 부주의한 사람을 속이는 이유 → 속이는 이야기가 아니에요.',
  '② 정확한 주장이 신뢰에 중요하다 → 결론(사실이라고 납득시킬 필요 없다)과 정반대예요.',
  '④ 과장된 주장에 우리가 어떻게 대처할까 → 소비자의 대처법이 아니라 광고 효과 이야기예요. (첫 문장 단어만 빌린 오답)',
  '⑤ 소비자를 망설이게 하는 것 → 망설임이 아니라 제품을 사용해 보게 하는 요인(호기심)을 다뤄요.'],
 '장문 제목은 실험 결과 뒤의 결론(The results suggest that ~)을 꼭 보세요. 숫자 비교(44% > 34%)가 말하는 것을 한 문장으로 정리하면 제목이 보여요.',
 K41, V41, ['consumer', 'disbelief', 'encounter', 'exaggerated', 'claim', 'overwhelm', 'curiosity', 'existing', 'resolve', 'attitude', 'concern', 'convince'],
 paras=[Q41], notes='* overwhelm: 압도하다')
day(42, 'q42', '어휘', '장문 어휘', '밑줄 친 (a)~(e) 중에서 문맥상 낱말의 쓰임이 적절하지 <u>않은</u> 것은?', T41,
 ['(a) yielding', '(b) confidently', '(c) necessary', '(d) indifferent', '(e) create'], 3,
 '실험에서 가장 많이 제품을 써 보려 한 집단은 “믿지 않지만 호기심을 가진(curious nonbelief)” 집단(44%)이었어요. 그러니 가장 효과적인 광고는 소비자를 “무관심하게(indifferent)” 만드는 게 아니라 “호기심을 갖게(curious)” 만드는 광고예요.',
 ['(a) yielding: 불일치를 해소하려고 메시지를 “받아들이고” 제품을 써 본다 ✔',
  '(b) confidently: 호기심 어린 불신과 구별되는, “확신을 갖고” 불신한 사람들 ✔',
  '(c) necessary: 호기심 어린 불신 = 판단하려면 실제 경험이 “필요하다”는 믿음 ✔',
  '(e) create: 사실이라고 납득시키지 않아도 사용해 보려는 관심을 “만들 수” 있다 ✔'],
 '장문 어휘는 실험 결과(숫자)와 결론 문장의 방향이 맞는지 확인하세요. 호기심 집단이 1등 → 결론에는 curious가 와야 해요.',
 [], V41, [], paras=[Q41], notes='* overwhelm: 압도하다', three=True)
multi('41·42번 장문 (제목·어휘)', 2)

# ═══ 37번 순서 ═══
G37 = "The initial selection of farmed Atlantic salmon took place from fish drawn from forty different river systems."
A37 = ["But whatever the manifestation of difference that occurred in different species of salmon, the first salmon farmers realized that crossing and recrossing the specific families from the original forty rivers would result in salmon that grew faster."]
B37 = ["And because salmon, unlike cattle and sheep, can produce many thousands of offspring in the course of their lives, once favorable individuals were found, just a few strong males and females could form the basis of a whole new race of highly productive fish.",
       "A domestic population could be created quickly that would be quite different from the initial wild ancestors."]
C37 = ["Every salmon river has its own unique set of challenges to which fish must adapt.",
       "Some rivers are very long, like the Yukon, and require animals that can build up massive fat reserves in order to survive the extended journey.",
       "Others are very far north, with only a short season of warmer temperatures, and require a fish that can maximize growth, particularly during its younger phase."]
day(37, 'q37', '순서', '글의 순서 · 하천별 차이(C) → But whatever the difference(A) → And(B)', '주어진 글 다음에 이어질 글의 순서로 가장 적절한 것은?', [
 (G37, "양식 대서양 연어의 초기 선발은 40개의 서로 다른 하천 수계에서 가져온 물고기로부터 이루어졌다."),
 (C37[0], "(C) 모든 연어 하천에는 물고기가 적응해야 하는 고유한 일련의 난관이 있다."),
 (C37[1], "Yukon강처럼 어떤 하천은 매우 길어서, 길어진 여정에서 살아남기 위해 막대한 지방 비축량을 쌓을 수 있는 동물이 필요하다."),
 (C37[2], "다른 하천들은 아주 멀리 북쪽에 있어 따뜻한 시기가 짧아서, 특히 어린 시기에 성장을 극대화할 수 있는 물고기가 필요하다."),
 (A37[0], "(A) 그러나 서로 다른 연어 종들에서 나타난 차이가 어떤 형태였든, 최초의 연어 양식업자들은 원래의 40개 하천에서 가져온 특정 계통들을 교배하고 재교배하면 더 빨리 자라는 연어를 얻게 될 것임을 깨달았다."),
 (B37[0], "(B) 그리고 연어는 소나 양과 달리 일생 동안 수천 마리의 새끼를 낳을 수 있기 때문에, 일단 유리한 개체가 발견되면 소수의 강한 수컷과 암컷만으로도 생산성이 매우 높은 완전히 새로운 품종의 기반을 형성할 수 있었다."),
 (B37[1], "최초의 야생 조상들과는 상당히 다른 사육 집단이 빠르게 만들어질 수 있었다."),
], ['(A) - (C) - (B)', '(B) - (A) - (C)', '(B) - (C) - (A)', '(C) - (A) - (B)', '(C) - (B) - (A)'], 3,
 '① 주어진 글 → (C): 40개의 서로 다른 하천 → (C) “모든 연어 하천은 고유한 난관이 있다”(긴 하천은 지방 비축, 북쪽 하천은 빠른 성장)로 하천별 차이를 설명해요. ② (C) → (A): (C)에서 설명한 차이를 (A)가 But whatever the manifestation of difference(차이가 어떤 형태였든)로 받아요 → 40개 하천의 계통을 교배하면 더 빨리 자라는 연어. ③ (A) → (B): And로 이어서, 연어는 새끼를 수천 마리 낳으니 소수의 개체로 새 품종을 빨리 만들 수 있었다.',
 ['①② (A)나 (B)가 먼저 오면 (A)의 the manifestation of difference(차이)가 무엇인지 아직 나오지 않았어요.',
  '③ (B)가 주어진 글 바로 뒤에 오면 favorable individuals(유리한 개체)를 찾는 교배 이야기((A))가 빠져 있어요.',
  '⑤ (B)가 (A)보다 먼저 오면, 교배하면 더 빨리 자란다는 발견 전에 새 품종 이야기가 나와 버려요.'],
 '순서 문제에서 But, And로 시작하는 단락은 절대 첫 번째가 되기 어려워요. 연결어가 없는 단락(C)부터 놓고, (A)의 difference가 (C)의 내용(하천마다 다른 난관)을 받는지 확인하세요.',
 [(C37[0], "모든 연어 하천에는 물고기가 적응해야 하는 고유한 일련의 난관이 있다.", "전치사 + 관계대명사 to which (adapt to ~에 적응하다) · a set of 일련의"),
  (A37[0], "그러나 서로 다른 연어 종들에서 나타난 차이가 어떤 형태였든, 최초의 연어 양식업자들은 원래의 40개 하천에서 가져온 특정 계통들을 교배하고 재교배하면 더 빨리 자라는 연어를 얻게 될 것임을 깨달았다.", "whatever + 명사 (was) 어떤 ~이든 · 동명사 주어 crossing and recrossing ~ / 동사 would result in"),
  (B37[0], "그리고 연어는 소나 양과 달리 일생 동안 수천 마리의 새끼를 낳을 수 있기 때문에, 일단 유리한 개체가 발견되면 소수의 강한 수컷과 암컷만으로도 완전히 새로운 고생산성 품종의 기반을 형성할 수 있었다.", "because ~, once ~, 주절 순서 · unlike ~와 달리 · once 일단 ~하면(접속사)")],
 [('initial', '초기의'), ('selection', '선발'), ('farmed', '양식된'), ('take place', '이루어지다'), ('draw', '끌어오다, 가져오다'), ('river system', '수계'),
  ('manifestation', '표현, 나타남'), ('species', '종'), ('cross', '교배하다'), ('specific', '특정한'), ('result in', '~을 낳다, 초래하다'), ('cattle', '소'),
  ('offspring', '자손'), ('favorable', '유리한'), ('basis', '기반'), ('productive', '생산성이 높은'), ('domestic', '사육되는'), ('ancestor', '조상'),
  ('unique', '고유한'), ('adapt to', '~에 적응하다'), ('massive', '막대한'), ('reserve', '비축량'), ('extended', '길어진'), ('phase', '시기, 단계')],
 ['initial', 'selection', 'manifestation', 'species', 'specific', 'offspring', 'favorable', 'productive', 'domestic', 'ancestor', 'reserve', 'extended'],
 given=G37, paras=['<b>(A)</b> ' + esc(' '.join(A37)), '<b>(B)</b> ' + esc(' '.join(B37)), '<b>(C)</b> ' + esc(' '.join(C37))],
 notes='* manifestation: 표현 ** offspring: 자손', three=True)

# ═══ 33번 빈칸 ═══
day(33, 'q33', '빈칸', '빈칸 추론 · 빈칸 뒤 예시(집을 걸어 다니며 묘사)를 한마디로', '다음 빈칸에 들어갈 말로 가장 적절한 것은?', [
 ("While a picture transports the spectator almost instantly into a landscape, language can only describe it detail by detail, bringing it slowly into the reader’s mind.", "그림은 보는 사람을 거의 즉시 풍경 속으로 데려가지만, 언어는 그것을 세부 사항별로 하나하나 묘사하여 독자의 마음속에 서서히 가져올 수 있을 뿐이다."),
 ("How can a literary work capture the feel of a place in both its atmosphere and its topography without losing the reader in a descriptive forest?", "문학 작품은 어떻게 독자를 묘사의 숲에서 길을 잃게 하지 않으면서 어떤 장소의 분위기와 지형 모두에 깃든 그곳의 느낌을 담아낼 수 있을까?"),
 ("One solution, proposed by Balzac, is to tie description to a moving body.", "Balzac이 제안한 한 가지 해결책은 묘사를 움직이는 사람과 연결하는 것이다."),
 ("Balzac’s novels open with detailed portrayals of the setting, but the descriptions never threaten the reader’s sense of orientation because they trace a precise path through the fictional world.", "Balzac의 소설은 배경에 대한 상세한 묘사로 시작하지만, 그 묘사는 허구의 세계 속에서 정확한 경로를 따라가기 때문에 결코 독자의 방향 감각을 위협하지 않는다."),
 ("When the novel describes a house, the narrator inspects the building in a systematic manner, approaching it from the street, examining the garden and the front, entering through the main door, and walking from room to room, as would a real estate agent or a prospective resident.", "소설이 집을 묘사할 때, 화자는 부동산 중개인이나 미래의 거주자가 그러하듯 체계적인 방식으로 건물을 살펴보는데, 거리에서 그 집으로 다가가, 정원과 정면을 살펴보고, 현관문으로 들어가, 방에서 방으로 걸어 다닌다."),
 ("The reader ends up with a precise notion of the layout of the building, all the way down to the floor plan.", "결국 독자는 평면도에 이르기까지 그 건물의 배치에 대해 정확한 개념을 갖게 된다."),
], ['flood the reader’s mind with abstract images', 'present small objects in detail', 'tie description to a moving body', 'distance readers from a scene', 'portray a landscape from upward angles'], 2,
 '질문: 독자를 묘사의 숲에서 길을 잃게 하지 않으려면? 빈칸 뒤 예시: 묘사가 정확한 경로(precise path)를 따라가고, 화자가 거리에서 다가가 → 정원 → 현관 → 방에서 방으로 “걸어 다니며” 묘사한다. → 묘사를 움직이는 사람(의 이동 경로)과 연결한다 = ③ tie description to a moving body.',
 ['① 추상적인 이미지로 채운다 → 오히려 평면도까지 정확한 개념을 갖게 해요.',
  '② 작은 사물을 자세히 표현한다 → 상세한 묘사는 맞지만, 핵심은 ‘이동 경로를 따라’ 묘사하는 거예요. (부분 정보 함정)',
  '④ 독자를 장면에서 멀어지게 한다 → 반대로 독자가 집 안을 함께 걸어 다니는 느낌이에요.',
  '⑤ 아래에서 위를 올려다보는 시점 → 시점 각도 이야기는 없어요.'],
 '빈칸 뒤에 긴 예시가 나오면, 예시 속 동사들(approaching, examining, entering, walking)의 공통점을 한마디로 바꾸세요. 모두 “이동”이니 moving body가 답이에요.',
 [("While a picture transports the spectator almost instantly into a landscape, language can only describe it detail by detail, bringing it slowly into the reader’s mind.", "그림은 보는 사람을 거의 즉시 풍경 속으로 데려가지만, 언어는 그것을 세부 사항별로 하나하나 묘사하여 독자의 마음속에 서서히 가져올 수 있을 뿐이다.", "While ~ 반면에(대조) · detail by detail 하나하나 · 분사구문 bringing ~ (결과)"),
  ("One solution, proposed by Balzac, is to tie description to a moving body.", "Balzac이 제안한 한 가지 해결책은 묘사를 움직이는 사람과 연결하는 것이다.", "주어 One solution (, proposed by ~,) / 동사 is / 보어 to부정사 · tie A to B A를 B에 연결하다"),
  ("When the novel describes a house, the narrator inspects the building in a systematic manner, approaching it from the street, examining the garden and the front, entering through the main door, and walking from room to room, as would a real estate agent or a prospective resident.", "소설이 집을 묘사할 때, 화자는 부동산 중개인이나 미래의 거주자가 그러하듯 체계적인 방식으로 건물을 살펴보는데, 거리에서 다가가, 정원과 정면을 살펴보고, 현관문으로 들어가, 방에서 방으로 걸어 다닌다.", "분사구문 4개 병렬(approaching, examining, entering, walking) · as would + 주어 (~가 그러하듯, 도치)")],
 [('transport', '데려가다, 이동시키다'), ('spectator', '보는 사람, 관객'), ('instantly', '즉시'), ('landscape', '풍경'), ('literary', '문학의'), ('capture', '담아내다, 포착하다'),
  ('atmosphere', '분위기'), ('topography', '지형'), ('descriptive', '묘사의'), ('portrayal', '묘사'), ('setting', '배경'), ('threaten', '위협하다'),
  ('sense of orientation', '방향 감각'), ('trace', '따라가다'), ('precise', '정확한'), ('fictional', '허구의'), ('narrator', '화자, 서술자'), ('inspect', '살펴보다, 점검하다'),
  ('systematic', '체계적인'), ('real estate agent', '부동산 중개인'), ('prospective', '미래의, 장래의'), ('resident', '거주자'), ('notion', '개념'), ('layout', '배치')],
 ['transport', 'spectator', 'instantly', 'landscape', 'literary', 'capture', 'atmosphere', 'portrayal', 'threaten', 'precise', 'systematic', 'prospective'],
 blank='tie description to a moving body', notes='* topography: 지형', three=True)

# ═══ 39번 문장 삽입 ═══
G39 = "However, melody alone would not normally keep the listener’s attention for long because a piece of music needs some variety and contrasting elements from time to time."
S39 = [
 ("Regardless of musical style, an increase of focus on certain parameters in a musical passage should be accompanied by a decrease in focus on others.", "음악 양식과 상관없이, 음악의 한 악절에서 특정 요소에 대한 집중이 늘어나면 다른 요소에 대한 집중은 줄어들어야 한다."),
 ("The human mind has an attention limit, beyond which music is most likely to be perceived as lacking order or direction.", "인간의 정신에는 주의력의 한계가 있으며, 이를 넘어서면 음악은 질서나 방향성이 없는 것으로 인식될 가능성이 매우 높다."),
 ("For instance, if the intention is to focus on melodic lines, then one should avoid making too many contrasting timbre variations while the melodies are unfolding; otherwise, the timbre may distract attention away from the pitch.", "예를 들어, 의도가 선율에 집중하는 것이라면 선율이 전개되는 동안 대조되는 음색 변화를 너무 많이 만드는 것을 피해야 하는데, 그렇지 않으면 음색이 음높이로부터 주의를 딴 데로 돌릴 수 있다."),
 ("One of the most difficult issues in the practice of composition is to find the right balance between repetition and diversity: a well-balanced piece of music should unfold naturally to listeners.", "작곡 실무에서 가장 어려운 문제 중 하나는 반복과 다양성 사이의 적절한 균형을 찾는 것인데, 균형이 잘 잡힌 음악은 듣는 사람에게 자연스럽게 전개되어야 하기 때문이다."),
 ("In most Western musical styles, this unfolding results from a network of relationships between musical attributes that combine in different ways to create situations where contrasts can take place.", "대부분의 서양 음악 양식에서 이러한 전개는, 대조가 일어날 수 있는 상황을 만들기 위해 다양한 방식으로 결합하는 음악적 속성들 사이의 관계망에서 비롯된다."),
 ("Such contrasts are normally preceded by a preparatory stage, which builds upon the listener’s expectations.", "그러한 대조에는 보통 준비 단계가 앞서는데, 이 단계는 듣는 사람의 기대를 바탕으로 한다."),
]
day(39, 'q39', '삽입', '문장 삽입 · However로 “선율만 집중 → 다양성도 필요”로 뒤집는 곳', '글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳은?',
 S39[:3] + [(G39, "(③ 자리) 하지만 음악 한 곡은 때때로 어느 정도의 다양성과 대조되는 요소가 필요하기 때문에, 선율만으로는 보통 듣는 사람의 주의를 오래 붙잡지 못할 것이다.")] + S39[3:],
 ['①', '②', '③', '④', '⑤'], 2,
 '③ 앞: 선율에 집중하려면 음색 변화를 너무 많이 만들지 말라(한 요소에 집중). 주어진 문장: However, 선율만으로는 주의를 오래 끌지 못한다, 다양성과 대조도 필요하다. ③ 뒤: 그래서 작곡에서 가장 어려운 것은 반복과 다양성의 균형을 찾는 것이다. → 주어진 문장이 “집중(반복)”과 “다양성” 사이를 이어 주는 다리 역할이에요.',
 ['①② 아직 선율(melody) 이야기가 나오기 전이에요. 주어진 문장의 melody alone은 ③ 앞의 melodic lines를 받아야 해요.',
  '④ ③ 뒤에서 이미 “반복과 다양성의 균형”이 나왔는데, 그다음에 “다양성이 필요하다”가 오면 순서가 거꾸로예요.',
  '⑤ this unfolding, Such contrasts로 계속 이어지는 흐름이라 끼어들 자리가 없어요.'],
 '삽입 문제의 주어진 문장이 However로 시작하면, 앞 내용과 반대 방향으로 꺾이는 곳을 찾으세요. 주어진 문장의 핵심어(melody, variety)가 앞 문장(melodic lines)과 뒤 문장(diversity)에 각각 이어지는지 확인하면 확실해요.',
 [(G39, "하지만 음악 한 곡은 때때로 어느 정도의 다양성과 대조되는 요소가 필요하기 때문에, 선율만으로는 보통 듣는 사람의 주의를 오래 붙잡지 못할 것이다.", "melody alone 선율만으로는 · keep one’s attention 주의를 붙잡다 · from time to time 때때로"),
  (S39[1][0], S39[1][1], "콤마 + 전치사 + which (beyond which = beyond the attention limit) · be perceived as -ing ~하는 것으로 인식되다"),
  (S39[2][0], S39[2][1], "avoid -ing ~하는 것을 피하다 · otherwise 그렇지 않으면 · distract A away from B A를 B로부터 딴 데로 돌리다")],
 [('regardless of', '~와 상관없이'), ('parameter', '요소, 요인'), ('passage', '악절, 구절'), ('accompany', '동반하다'), ('attention', '주의(력)'), ('perceive', '인식하다'),
  ('intention', '의도'), ('melodic', '선율의'), ('contrasting', '대조되는'), ('timbre', '음색'), ('variation', '변화'), ('unfold', '전개되다'),
  ('distract', '(주의를) 딴 데로 돌리다'), ('pitch', '음높이'), ('composition', '작곡'), ('repetition', '반복'), ('diversity', '다양성'), ('attribute', '속성'),
  ('precede', '앞서다, 선행하다'), ('preparatory', '준비의'), ('variety', '다양성')],
 ['regardless of', 'accompany', 'perceive', 'intention', 'contrasting', 'variation', 'unfold', 'distract', 'composition', 'repetition', 'diversity', 'precede'],
 given=G39, paras=[esc(S39[0][0]) + ' ( ① ) ' + esc(S39[1][0]) + ' ( ② ) ' + esc(S39[2][0]) + ' ( ③ ) ' + esc(S39[3][0]) + ' ( ④ ) ' + esc(S39[4][0]) + ' ( ⑤ ) ' + esc(S39[5][0])],
 notes='* timbre: 음색', three=True)

# ═══ 34번 빈칸 ═══
day(34, 'q34', '빈칸', '빈칸 추론 · 협곡 비유(너무 멀지도 가깝지도 않게)를 풀기', '다음 빈칸에 들어갈 말로 가장 적절한 것은?', [
 ("Surprise is the fundamental joke mechanism.", "놀라움은 농담의 기본적인 작동 원리이다."),
 ("Most punch lines rely on an element of surprise for their effect ― that’s why they’re not funny the third time you hear them.", "농담의 결정적인 구절 대부분은 효과를 내기 위해 놀라움이라는 요소에 의존하는데, 그것이 세 번째 들을 때는 재미가 없는 이유이다."),
 ("The joke-teller’s skill lies in judging exactly how much of a surprise the audience is prepared to take.", "농담하는 사람의 기술은 청중이 정확히 얼마만큼의 놀라움을 받아들일 준비가 되어 있는지를 판단하는 데 있다."),
 ("He must make a series of assumptions about what they will understand, what their reference points are, and how relaxed they appear to be.", "그는 청중이 무엇을 이해할지, 그들의 기준점이 무엇인지, 그리고 그들이 얼마나 편안해 보이는지에 대해 일련의 가정을 세워야 한다."),
 ("Jerry Seinfeld once compared telling a joke to attempting to leap a metaphorical canyon, taking the audience with you.", "Jerry Seinfeld는 한때 농담하는 것을 청중을 데리고 은유적인 협곡을 뛰어넘으려고 하는 것에 비유했다."),
 ("The setup to the joke is the near-side cliff, and the punch line is the far side.", "농담의 설정은 가까운 쪽 절벽이고, 결정적인 구절은 건너편 절벽이다."),
 ("If they’re too far apart, the listeners don’t make it to the other side.", "그 둘이 너무 멀리 떨어져 있으면, 듣는 사람들은 반대편에 도달하지 못한다."),
 ("And if they are too close together, the audience just steps across the gap and doesn’t experience a thrilling leap of any kind.", "그리고 그 둘이 너무 가까우면, 청중은 그냥 그 틈을 걸어서 건너갈 뿐 어떤 짜릿한 도약도 경험하지 못한다."),
 ("The joke-hearers get far more pleasure from the joke if they have to do a little work.", "농담을 듣는 사람들은 약간의 노력을 해야 할 때 그 농담에서 훨씬 더 큰 즐거움을 얻는다."),
], ['if they feel relaxed enough to laugh', 'when it matches their expectations', 'if it is about someone else', 'if they have to do a little work', 'when they fail to fully understand it'], 3,
 '협곡 비유: 설정(가까운 절벽)과 결정적 구절(먼 절벽)이 너무 멀면 → 건너지 못함(이해 못 함), 너무 가까우면 → 그냥 걸어서 건넘(짜릿함 없음). → 딱 알맞게 “뛰어야” 하는 거리일 때 가장 재미있다 = 청중이 약간의 노력을 해야 할 때(if they have to do a little work).',
 ['① 웃을 만큼 편안할 때 → relaxed는 농담하는 사람이 고려하는 가정 중 하나일 뿐이에요.',
  '② 예상과 일치할 때 → 놀라움이 핵심이니 정반대예요. (너무 가까운 절벽)',
  '③ 다른 사람에 관한 것일 때 → 나오지 않아요.',
  '⑤ 완전히 이해하지 못할 때 → 너무 먼 절벽(건너지 못함)이에요. 이해를 못 하면 재미도 없어요. (가장 매력적인 오답)'],
 '비유가 나오는 빈칸은 비유의 양 끝(너무 멀다 ✕ / 너무 가깝다 ✕)을 정리하고 “적당한 중간”을 말하는 선택지를 고르세요. 양 극단 중 하나(②, ⑤)를 고르면 함정에 빠져요.',
 [("The joke-teller’s skill lies in judging exactly how much of a surprise the audience is prepared to take.", "농담하는 사람의 기술은 청중이 정확히 얼마만큼의 놀라움을 받아들일 준비가 되어 있는지를 판단하는 데 있다.", "lie in -ing ~하는 데 있다 · how much of a surprise + 주어 + 동사 (간접의문문, judging의 목적어)"),
  ("Jerry Seinfeld once compared telling a joke to attempting to leap a metaphorical canyon, taking the audience with you.", "Jerry Seinfeld는 한때 농담하는 것을 청중을 데리고 은유적인 협곡을 뛰어넘으려고 하는 것에 비유했다.", "compare A to B A를 B에 비유하다 (to는 전치사 → attempting) · 분사구문 taking ~ (동시 동작)"),
  ("And if they are too close together, the audience just steps across the gap and doesn’t experience a thrilling leap of any kind.", "그 둘이 너무 가까우면, 청중은 그냥 그 틈을 걸어서 건너갈 뿐 어떤 짜릿한 도약도 경험하지 못한다.", "they = the setup and the punch line · step across ~을 걸어서 건너다 · not ~ of any kind 어떤 종류의 ~도 없다")],
 [('fundamental', '기본적인'), ('mechanism', '작동 원리, 기제'), ('punch line', '(농담의) 결정적인 구절'), ('rely on', '~에 의존하다'), ('element', '요소'), ('lie in', '~에 있다'),
  ('judge', '판단하다'), ('assumption', '가정'), ('reference point', '기준점'), ('relaxed', '편안한'), ('compare A to B', 'A를 B에 비유하다'), ('leap', '뛰어넘다; 도약'),
  ('metaphorical', '은유적인'), ('canyon', '협곡'), ('setup', '(농담의) 설정, 도입'), ('cliff', '절벽'), ('gap', '틈'), ('thrilling', '짜릿한')],
 ['fundamental', 'mechanism', 'element', 'judge', 'assumption', 'relaxed', 'leap', 'metaphorical', 'canyon', 'cliff', 'gap', 'thrilling'],
 blank='if they have to do a little work', notes='* canyon: 협곡', three=True)
