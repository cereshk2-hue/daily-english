from jfw import *
p = load(22, '22번 · 글의 요지')
VOCAB = words(22)
EXAM = [EXQ(22, '22. 다음 글의 요지로 가장 적절한 것은?', p.full(), [
 "콘텐츠 제작자는 사회와 환경 개선에 기여하는 창작물을 만들 책임이 있다.", "공익을 위한 콘텐츠는 특정 이익 집단에 편향되지 않는 중립성이 요구된다.", "콘텐츠 플랫폼은 사회적으로 유해한 콘텐츠를 엄격히 규제할 의무가 있다.",
 "콘텐츠 소비자에게는 정보를 비판적으로 수용하는 태도가 필요하다.", "전문가와의 협업은 신뢰할 수 있는 창작물을 만드는 데 중요하다."], 0,
 "정답 ▶ ① 콘텐츠 제작자는 사회와 환경 개선에 기여하는 창작물을 만들 책임이 있다.\n이유: 주제문 they have a responsibility to use that platform for positive change + 사회적·환경적 책임이 중요한 윤리적 고려 사항\n오답 ▶ ② 중립성 언급 없음 ③ 플랫폼의 '규제' 의무 아님(제작자의 책임) ④ 소비자 태도 아님 ⑤ 전문가 협업 없음\n포인트 ▶ 요지 = 누구(제작자)의 무엇(책임)인지 주어부터 확인", v=False),
 EXQ(22, '다음 글의 제목으로 가장 적절한 것은?', p.full(), [
 "Creating Content with Social and Environmental Responsibility", "How to Become a Popular Content Creator", "Why Audiences Ignore Ethical Messages",
 "The Rising Cost of Sustainable Products", "Climate Change: A Problem Too Big to Solve"], 0,
 "정답 ▶ ① 사회적·환경적 책임을 지고 콘텐츠 만들기\n이유: 첫 문장 + 마지막 문장(가치·대의명분 고려, 원칙과 일치) 모두 제작자의 '책임'\n오답 ▶ ② 인기 비결 아님 ③ 청중이 무시한다는 말 없음 ④ 지속 가능 제품 가격 없음 ⑤ 해결 불가능하다는 말 없음\n포인트 ▶ 첫 문장 = 주제문인 글"),
 EXQ(22, '다음 빈칸에 들어갈 말로 가장 적절한 것은?', p.blank('aligns with'), [
 "aligns with", "competes with", "breaks away from", "has nothing to do with", "hides"], 0,
 "정답 ▶ ① aligns with (~와 일치하다)\n이유: 윤리적 제작자는 자신의 가치·대의명분도 고려 → 콘텐츠가 사회적·환경적 원칙과 '일치하게' 함\n오답 ▶ ② 경쟁하다 ③ 벗어나다 ④ 관계없다 ⑤ 숨기다 — 모두 반대 방향\n포인트 ▶ ensure that ~ = 반드시 ~하게 하다")]
PICK1 = [PK(p, 'Social and environmental', 'increasingly', 'decreasingly', "정답 ▶ increasingly (점점 더)\n오답 ▶ decreasingly (점점 덜)\n이유: 전 세계적 인식이 커짐 → 책임이 '점점 더' 중요해짐"),
 PK(p, 'As global awareness', 'grows', 'fades', "정답 ▶ grows (커지다)\n오답 ▶ fades (희미해지다)\n이유: 인식이 '커짐에 따라' 더 폭넓은 영향을 고려하도록 요구받음"),
 PK(p, 'As global awareness', 'broader', 'narrower', "정답 ▶ broader (더 폭넓은)\n오답 ▶ narrower (더 좁은)\n이유: 사회·환경까지 — 작업의 '더 폭넓은' 영향"),
 PK(p, 'Content creators have', 'influence', 'ignore', "정답 ▶ influence (영향을 미치다)\n오답 ▶ ignore (무시하다)\n이유: 청중의 태도와 행동에 '영향을 미칠 수 있는' 플랫폼 → 그래서 책임이 있음"),
 PK(p, 'For example, promoting', 'raise', 'lower', "정답 ▶ raise (높이다)\n오답 ▶ lower (낮추다)\n이유: 지속 가능 제품 홍보·대의 지지 → 인식을 '높임'"),
 PK(p, 'Ethical content creators', 'principles', 'profits', "정답 ▶ principles (원칙)\n오답 ▶ profits (이익)\n이유: 제품 홍보에만 초점 맞추지 않고 → 사회적·환경적 '원칙'과 일치")]
TF = [TF(p, "Content creators are increasingly asked to think about the wider effects of their work.", True, "are being called upon to consider the broader impact of their work", "정답 ▶ T\n이유: 작업의 더 폭넓은 영향을 고려하도록 요구받고 있어요.\n어휘 ▶ be asked to = be called upon to · wider = broader"),
 TF(p, "Topics like climate change should be avoided in content.", False, "addressing topics such as climate change", "정답 ▶ F\n이유: 기후 변화 같은 주제를 '다루는' 것이 포함돼요."),
 TF(p, "Creators’ platforms can affect how their audience thinks and acts.", True, "can influence their audience’s attitudes and behaviors", "정답 ▶ T\n이유: 청중의 태도와 행동에 영향을 줄 수 있어요."),
 TF(p, "Supporting causes of equality can help drive meaningful social impact.", True, "supporting causes related to equality and justice", "정답 ▶ T\n이유: 평등·정의 관련 대의 지지는 의미 있는 사회적 영향을 이끌어요."),
 TF(p, "Ethical creators focus only on promoting their products.", False, "not only focus on promoting their products or services but also consider the values", "정답 ▶ F\n이유: 제품 홍보뿐 아니라 가치와 대의도 고려해요.\n포인트 ▶ not only A but also B"),
 TF(p, "Global awareness of sustainability issues is decreasing.", False, "As global awareness of social, environmental, and sustainability issues grows", "정답 ▶ F\n이유: 인식이 커지고 있어요.")]
MC = [MC(p, "글의 내용과 일치하지 <u>않는</u> 것은?", [
 "Ethical creators care only about selling more products.", "Creators may deal with social justice in their content.", "Promoting sustainable products can raise awareness.",
 "Creators have a duty to use their platform for good.", "Ethical consumerism is one topic creators may address."],
 "정답 ▶ Ethical creators care only about selling more products.\n이유: not only focus on promoting their products or services but also consider the values and causes they support\n포인트 ▶ deal with = address · duty = responsibility · for good = for positive change",
 [["윤리적 제작자는 제품을 더 많이 파는 것만 신경 쓴다.", "not only focus on promoting their products or services but also consider", "✗ 가치도 고려"], ["제작자는 콘텐츠에서 사회 정의를 다룰 수 있다.", "addressing topics such as climate change, social justice", "deal with = address"], ["지속 가능 제품 홍보는 인식을 높일 수 있다.", "can help raise awareness", "일치"], ["제작자는 플랫폼을 좋은 일에 쓸 책임이 있다.", "a responsibility to use that platform for positive change", "duty = responsibility"], ["윤리적 소비주의는 제작자가 다룰 수 있는 주제이다.", "ethical consumerism", "일치"]]),
 MC(p, "글의 내용과 <u>일치하는</u> 것은?", ["콘텐츠 제작자는 청중의 태도에 영향을 미칠 수 있다.", "사회적 책임은 콘텐츠 제작자에게 점점 덜 중요해지고 있다.", "윤리적 제작자는 자신의 원칙과 다른 콘텐츠를 만든다.", "기후 변화는 콘텐츠의 주제로 적절하지 않다.", "지속 가능성 문제에 대한 인식은 줄어들고 있다."],
 "정답 ▶ 콘텐츠 제작자는 청중의 태도에 영향을 미칠 수 있다.\n이유: a platform that can influence their audience’s attitudes and behaviors\n오답 ▶ ② 점점 더 중요 ③ 원칙과 일치 ④ 다루는 주제 ⑤ 커지고 있음",
 [["", "can influence their audience’s attitudes", "일치 ✔"], ["", "increasingly important", "더 중요"], ["", "aligns with their social and environmental principles", "일치시킴"], ["", "climate change", "다룸"], ["", "As global awareness", "커짐"]])]
PICK2 = [PK(p, 'Social and environmental', 'has become', 'have become', "정답 ▶ has become\n이유: 주어 Social and environmental responsibility — 형용사 두 개가 명사 responsibility 하나를 꾸밈 → 단수"),
 PK(p, 'As global awareness', 'are being called', 'are calling', "정답 ▶ are being called\n이유: 제작자들이 '요구받는' 수동 + 진행 → be being p.p."),
 PK(p, 'This includes', 'addressing', 'to address', "정답 ▶ addressing\n이유: include는 동명사를 목적어로 취함"),
 PK(p, 'Content creators have', 'that can', 'what can', "정답 ▶ that\n이유: 선행사 a platform 있음 → 주격 관계대명사 that"),
 PK(p, 'For example, promoting', 'can help', 'can helps', "정답 ▶ can help\n이유: 조동사 can + 동사원형 (주어는 동명사구 promoting ~ or supporting ~)"),
 PK(p, 'Ethical content creators', 'ensuring', 'ensured', "정답 ▶ ensuring\n이유: 분사구문, 제작자들이 '확실히 하는' 능동 → 현재분사")]
VERB = [VB(p, 'For example, promoting', 'related', 'relate', "정답 ▶ related\n이유: causes를 꾸미는 과거분사 — related to ~ (~와 관련된)"),
 VB(p, 'Ethical content creators', 'aligns', 'align', "정답 ▶ aligns\n이유: that절 주어 their content(단수) → aligns"),
 VB(p, 'Content creators have', 'to use', 'use', "정답 ▶ to use\n이유: a responsibility를 꾸미는 형용사적 to부정사 (~할 책임)"),
 VB(p, 'Ethical content creators', 'promoting', 'promote', "정답 ▶ promoting\n이유: 전치사 on 뒤 동명사 (focus on -ing)")]
VERB = [v for v in VERB if v['v'] != v['a'][0]]
ERR = [ER(p, 'As global awareness', ['As', ('are being called', 'are calling'), 'to consider'], 1, 'are being called', "틀린 곳 ▶ ② are calling → are being called\n이유: 제작자들이 (사회에 의해) '요구받는' 수동 → call upon A to V의 수동 be called upon to V\n나머지 ▶ ① 접속사 As(~함에 따라) ✔ ③ be called upon + to부정사 ✔"),
 ER(p, 'For example, promoting', ['promoting', ('related', 'relating'), 'raise'], 1, 'related', "틀린 곳 ▶ ② relating → related\n이유: causes가 평등·정의와 '관련된' → related to (과거분사)\n나머지 ▶ ① 주어 역할 동명사 ✔ ③ help + (to) 동사원형 → raise ✔"),
 ER(p, 'Ethical content creators', ['not only', 'consider', ('aligns', 'align')], 2, 'aligns', "틀린 곳 ▶ ③ align → aligns\n이유: that절 주어 their content(단수) → aligns\n나머지 ▶ ① not only A but also B ✔ ② also 뒤 creators의 동사 consider(복수) ✔")]
SCR = [0, 1, 3, 4, 5]
ORDER = [[0, 1, 2, 3], [2, 3, 4, 5]]
INSERT = [([1, 2, 3, 4], 1, "정답 ▶ ① (This includes ~ 문장)\n이유: 더 폭넓은 영향을 고려하도록 요구받음 → This(그 고려)는 기후 변화 등을 다루는 것을 포함"),
 ([3, 4, 5], 1, "정답 ▶ ① (For example ~ 문장)\n이유: 플랫폼을 긍정적 변화에 쓸 책임 → For example 지속 가능 제품 홍보·대의 지지")]
ODD = [([2, 3, "Some content creators earn millions of dollars a year from advertising.", 4], 2, "정답 ▶ ③\n이유: 제작자의 사회적·환경적 책임이 흐름이에요. 광고로 큰돈을 번다는 이야기는 관계없어요.")]
BLANK = [BL(p, 'Social and environmental', 'ethical', ["financial", "technical", "physical"], "정답 ▶ ethical (윤리적인)\n이유: 책임 → '윤리적' 고려 사항 — 마지막 문장 Ethical content creators와 연결\n오답 ▶ financial 재정적인 · technical 기술적인 · physical 신체적인"),
 BL(p, 'Content creators have', 'positive change', ["personal profit", "quick fame", "free time"], "정답 ▶ positive change (긍정적인 변화)\n이유: 영향을 미칠 수 있는 플랫폼 → 책임 → '긍정적인 변화'를 위해\n오답 ▶ 개인 이익 · 빠른 명성 · 여가"),
 BL(p, 'For example, promoting', 'sustainable', ["disposable", "expensive", "foreign"], "정답 ▶ sustainable (지속 가능한)\n이유: 환경적 책임의 예 → 환경적으로 '지속 가능한' 제품\n오답 ▶ disposable 일회용의(반대) · expensive · foreign")]
GRAM = [{'q': "빈칸에 알맞은 것은?<br><b>Many creators ______ upon to consider the impact of their work.</b>", 'opts': ["are being called", "are calling", "is being called", "have called"], 'ex': "정답 ▶ are being called\n이유: 주어 creators(복수)가 '요구받는' 수동 + 진행"},
 {'q': "빈칸에 알맞은 것은?<br><b>This includes ______ topics such as climate change.</b>", 'opts': ["addressing", "to address", "address", "addressed"], 'ex': "정답 ▶ addressing\n이유: include + 동명사"},
 {'q': "빈칸에 알맞은 것은?<br><b>They not only promote products ______ consider the values they support.</b>", 'opts': ["but also", "and so", "or else", "but not"], 'ex': "정답 ▶ but also\n이유: not only A but also B"},
 {'q': "빈칸에 알맞은 것은?<br><b>They ensure that their content ______ with their principles.</b>", 'opts': ["aligns", "align", "aligning", "to align"], 'ex': "정답 ▶ aligns\n이유: that절 주어 their content(단수) + 현재시제 동사"}]
SUMQ = [SUM(p, "Because content creators can (A) ______ their audience, they should take social and environmental (B) ______ into account in their work.", [
 "(A) influence – (B) responsibility", "(A) influence – (B) profit", "(A) ignore – (B) responsibility", "(A) entertain – (B) fashion", "(A) avoid – (B) risk"],
 "정답 ▶ (A) influence – (B) responsibility\n(A) a platform that can influence their audience’s attitudes (B) Social and environmental responsibility\n오답 ▶ profit 이익: 홍보에'만' 초점 맞추지 않음 · ignore 무시하다",
 ["can influence their audience’s attitudes", "Social and environmental responsibility"])]
