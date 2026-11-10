from common import *
d, e = SEC['❹'], SEC['❺']
VOCAB = V('❹', [["repairability", "수리 가능성"], ["index", "지수, 지표"], ["at a glance", "한눈에"], ["pass a bill", "법안을 통과시키다", "passed a bill"], ["category", "범주, 종류", "categories"],
  ["lawn mower", "잔디 깎는 기계", "lawn mowers"], ["range from A to B", "범위가 A에서 B에 이르다", "ranging from 0 to 10"], ["color-coded", "색깔로 구분된"], ["take into account", "~을 고려하다 (= consider)", "takes into account"],
  ["element", "요소"], ["availability", "이용 가능성"], ["ease", "용이함, 쉬움"], ["disassembly", "분해"], ["spare part", "예비 부품", "spare parts"], ["label", "라벨, 표; ~에 라벨을 붙이다"],
  ["whereas", "~인 반면에 (= while)"], ["indicate", "~을 나타내다", "indicates"]]) + \
 V('❺', [["informed", "정보에 근거한, 잘 아는"], ["encourage A to-v", "A가 ~하도록 장려하다", "encourages manufacturers to make"], ["end up in", "결국 ~에 이르게 되다", "ending up in"], ["landfill", "쓰레기 매립지", "landfills"],
  ["make a transition to", "~로 전환하다, 이행하다", "make a transition to"], ["sustainable", "지속 가능한"], ["impact", "영향, 효과"], ["be likely to-v", "~할 가능성이 있다", "is likely to spread"],
  ["far beyond", "~을 훨씬 넘어"], ["global economy", "세계 경제"], ["according to", "~에 따라"], ["anticipate", "~을 예상하다, 기대하다 (= expect)"], ["follow one's lead", "~의 선례를 따르다", "following France's innovative lead"],
  ["innovative", "혁신적인"]])
PICK1 = [PK(d, 'In January 2021', 'passed', 'rejected', "정답 ▶ passed (통과시켰다)\n오답 ▶ rejected (거부했다)\n이유: 법안이 제조사에게 지수를 '요구한다(requires)' → 실제로 시행됨 → 통과"),
 PK(d, 'Using a score', 'easily', 'quickly', "정답 ▶ easily (쉽게)\n오답 ▶ quickly (빨리)\n이유: '수리 가능성(repairability)' 지수 → 얼마나 '쉽게' 수리될 수 있는지"),
 PK(d, 'Using a score', 'before', 'after', "정답 ▶ before (~하기 전에)\n오답 ▶ after (~한 후에)\n이유: 구입 '전에' 확인해야 정보에 근거한 결정(informed decisions)을 할 수 있어요."),
 PK(d, 'The index takes', 'availability', 'absence', "정답 ▶ availability (이용 가능성)\n오답 ▶ absence (부재)\n이유: 지수가 고려하는 요소 → 수리 정보를 '얼마나 이용할 수 있는지'"),
 PK(d, 'A low number', 'difficult', 'simple', "정답 ▶ difficult (어려운)\n오답 ▶ simple (간단한)\n이유: whereas(반면에) 뒤 '높은 숫자 = 수리 쉬움'과 대조 → 낮은 숫자 = 어려움"),
 PK(e, 'Firstly, it allows', 'informed', 'impulsive', "정답 ▶ informed (정보에 근거한)\n오답 ▶ impulsive (충동적인)\n이유: 지수로 구입 전에 수리 가능성을 알 수 있음 → '정보에 근거한' 결정"),
 PK(e, 'Secondly, it encourages', 'easier', 'harder', "정답 ▶ easier (더 쉬운)\n오답 ▶ harder (더 어려운)\n이유: 긍정적 효과 두 번째 → 제조사가 제품을 수리하기 '더 쉽게' 만들도록 장려"),
 PK(e, 'As a result', 'fewer', 'more', "정답 ▶ fewer (더 적은)\n오답 ▶ more (더 많은)\n이유: 지속 가능한 사회로의 전환 → 매립지로 가는 제품이 '더 적어짐'"),
 PK(e, 'The impact of', 'beyond', 'within', "정답 ▶ beyond (~을 넘어)\n오답 ▶ within (~ 안에서)\n이유: however(하지만) + 다음 문장(세계 경제, 프랑스 시장에 팔려는 모든 회사) → 영향이 프랑스를 '넘어' 퍼짐"),
 PK(e, 'If the index', 'innovative', 'outdated', "정답 ▶ innovative (혁신적인)\n오답 ▶ outdated (구식의)\n이유: 다른 나라들이 '따라 할' 선례 → 혁신적인")]
TF = [TF(d, "The French government passed the bill in January 2021.", True, "In January 2021, the French government passed a bill", "정답 ▶ T\n이유: 2021년 1월에 법안을 통과시켰어요."),
 TF(d, "The repairability index applies to all electronic products sold in France.", False, "on five categories of electronic devices and electrical appliances", "정답 ▶ F\n이유: 다섯 가지 범주에만 적용돼요."),
 TF(d, "Televisions are one of the product categories covered by the index.", True, "televisions", "정답 ▶ T\n이유: 스마트폰, 노트북, 세탁기, 텔레비전, 잔디 깎는 기계예요."),
 TF(d, "The index uses both a numerical score and colors.", True, "Using a score ranging from 0 to 10, as well as a color-coded system", "정답 ▶ T\n이유: 0~10점 점수와 색상 체계를 함께 써요.\n어휘 ▶ numerical = 숫자의"),
 TF(d, "The price of spare parts is not considered in the index.", False, "the price of spare parts", "정답 ▶ F\n이유: 예비 부품 가격도 고려해요.\n어휘 ▶ consider = take into account"),
 TF(d, "A high number on a red label means the product is easy to repair.", False, "a high number on a green label indicates that the product is easy to repair", "정답 ▶ F\n이유: 수리가 쉬운 건 초록색 라벨의 높은 숫자예요."),
 TF(e, "The index helps consumers make better-informed choices when buying devices.", True, "make informed decisions when purchasing new devices and appliances", "정답 ▶ T\n이유: 구입할 때 정보에 근거한 결정을 하게 해 줘요."),
 TF(e, "The index only affects companies based in France.", False, "any company that wants to sell its appliances on the French market", "정답 ▶ F\n이유: 프랑스 시장에 팔려는 모든 회사가 라벨을 붙여야 해요."),
 TF(e, "The writer expects other countries may follow France's example if the index succeeds.", True, "more countries around the world following France's innovative lead", "정답 ▶ T\n이유: 성공하면 더 많은 나라가 프랑스의 선례를 따를 거라 예상해요.\n어휘 ▶ example ≒ lead")]
MC = [MULTI("본문 ❹❺의 내용과 일치하지 <u>않는</u> 것은?", [
 "The index evaluates products based solely on their retail price.", "The index is displayed on smartphones and lawn mowers alike.", "Consumers can check repairability prior to purchase.",
 "The index motivates producers to design more repairable goods.", "Fewer discarded items in landfills could help France become more sustainable."],
 "정답 ▶ The index evaluates products based solely on their retail price.\n이유: takes into account several elements — 수리 정보 이용 가능성, 분해 용이성, 예비 부품 가격 등 여러 요소. 소매가격'만' 보지 않아요.\n포인트 ▶ evaluate = 평가하다 · solely = only · retail price = 소매가 · prior to = before · motivate ≒ encourage · producer = manufacturer",
 [["지수는 오직 소매가격만으로 제품을 평가한다.", "takes into account several elements", "✗ 여러 요소"], ["지수는 스마트폰과 잔디 깎는 기계 모두에 표시된다.", "smartphones, laptops, washing machines, televisions, and lawn mowers", "일치 ✔"],
  ["소비자는 구입 전에 수리 가능성을 확인할 수 있다.", "before they purchase it", "prior to = before ✔"], ["지수는 생산자가 더 수리하기 쉬운 상품을 설계하도록 동기를 준다.", "encourages manufacturers to make their products easier to repair", "motivate ≒ encourage ✔"], ["매립지에 버려지는 물건이 줄면 프랑스가 더 지속 가능해질 수 있다.", "with fewer electronic and electrical items ending up in its landfills", "일치 ✔"]], ['❹', '❺']),
 MULTI("본문 ❹❺의 내용과 <u>일치하는</u> 것은?", ["A bright red label with a low score signals that repairs will be hard.", "The index scores products from 1 to 100.", "The index was intended to have a single effect.", "Foreign companies are exempt from labeling their products.", "The writer is certain the index will fail."],
 "정답 ▶ A bright red label with a low score signals that repairs will be hard.\n이유: A low number on a bright red label means that repairing the product will be difficult\n오답 ▶ ② 0~10 ③ 두 가지 효과 ④ 프랑스 시장에 팔려는 모든 회사 ⑤ 성공하면 다른 나라도 따를 것으로 기대\n포인트 ▶ signal = indicate · exempt from = ~에서 면제된",
 [["", "A low number on a bright red label means that repairing the product will be difficult", "일치 ✔"], ["", "ranging from 0 to 10", "0~10"], ["", "two positive effects", "두 가지"], ["", "any company that wants to sell", "모든 회사"], ["", "If the index is successful", "기대"]], ['❹', '❺'])]
PICK2 = [PK(d, 'In January 2021', 'include', 'includes', "정답 ▶ include\n이유: 요구 동사 require + that + 주어 + (should) 동사원형 → every manufacturer (should) include"),
 PK(d, 'Using a score', 'Using', 'Used', "정답 ▶ Using\n이유: 분사구문의 의미상 주어 = the index — 지수가 점수를 '사용하는' 능동"),
 PK(d, 'Using a score', 'ranging', 'ranged', "정답 ▶ ranging\n이유: 점수가 0~10에 '이르는' — 자동사 range의 현재분사가 a score 수식"),
 PK(d, 'Using a score', 'see', 'to see', "정답 ▶ see\n이유: 사역동사 let + 목적어 + 동사원형"),
 PK(d, 'Using a score', 'how easily', 'how easy', "정답 ▶ how easily\n이유: 동사 can be repaired를 꾸미는 부사 → easily (간접의문문 how + 부사 + 주어 + 동사)"),
 PK(d, 'A low number', 'whereas', 'despite', "정답 ▶ whereas\n이유: 뒤에 절(a high number ~ indicates ~) → 접속사 whereas. despite는 전치사"),
 PK(e, 'Firstly, it allows', 'to make', 'make', "정답 ▶ to make\n이유: allow + 목적어 + to부정사"),
 PK(e, 'As a result', 'ending', 'ended', "정답 ▶ ending\n이유: with + 목적어 + 분사 — 제품들이 매립지에 '이르는' 능동(자동사 end up)"),
 PK(e, 'We live in', 'wants', 'want', "정답 ▶ wants\n이유: 관계대명사 that의 선행사 any company(단수)"),
 PK(e, 'If the index', 'seeing', 'to see', "정답 ▶ seeing\n이유: anticipate + 동명사 (~할 것을 예상하다)")]
VERB = [VB(d, 'The index takes', 'including', 'include', "정답 ▶ including\n이유: 전치사처럼 쓰이는 including(~을 포함하여)"),
 VB(d, 'A low number', 'repairing', 'repair', "정답 ▶ repairing\n이유: that절의 주어 자리 → 동명사 repairing"),
 VB(e, 'The index was', 'designed', 'design', "정답 ▶ designed\n이유: 지수가 '만들어진' 수동 → was designed"),
 VB(e, 'As a result', 'to make', 'make', "정답 ▶ to make\n이유: expect + to부정사"),
 VB(e, 'We live in', 'to label', 'label', "정답 ▶ to label\n이유: need + to부정사"),
 VB(e, 'If the index', 'following', 'follow', "정답 ▶ following\n이유: see + 목적어 + -ing (~가 …하는 것을 보다) — 지각동사의 목적격보어")]
ERR = [ER(d, 'In January 2021', ['passed', 'that requires', ('include', 'includes')], 2, 'include', "틀린 곳 ▶ ③ includes → include\n이유: require that + 주어 + (should) 동사원형\n나머지 ▶ ① 과거시제 ✔ ② 선행사 a bill + 주격 관계대명사, 단수 동사 ✔"),
 ER(d, 'Using a score', ['ranging', ('see', 'seeing'), 'easily'], 1, 'see', "틀린 곳 ▶ ② seeing → see\n이유: let + 목적어 + 동사원형\n나머지 ▶ ① 현재분사 ✔ ③ 부사 ✔"),
 ER(e, 'Secondly, it encourages', ['encourages', ('to make', 'making'), 'easier'], 1, 'to make', "틀린 곳 ▶ ② making → to make\n이유: encourage + 목적어 + to부정사\n나머지 ▶ ① 주어 it(단수) ✔ ③ make + 목적어 + 형용사(비교급) 보어 ✔"),
 ER(e, 'If the index', [('is', 'will be'), 'seeing', 'following'], 0, 'is', "틀린 곳 ▶ ① will be → is\n이유: 조건 부사절(If ~)은 미래라도 현재시제\n나머지 ▶ ② anticipate + 동명사 ✔ ③ see + 목적어 + -ing ✔")]
SCR = [('❹', 1), ('❹', 2), ('❹', 3), ('❺', 1), ('❺', 2), ('❺', 4), ('❺', 6)]
ORDER = [[('❹', 0), ('❹', 1), ('❹', 2), ('❹', 3)], [('❺', 0), ('❺', 1), ('❺', 2), ('❺', 3)], [('❺', 4), ('❺', 5), ('❺', 6)]]
INSERT = [([('❺', 0), ('❺', 1), ('❺', 2), ('❺', 3)], 2, "정답 ▶ ② (Secondly ~ 문장)\n이유: 두 가지 긍정적 효과 → Firstly(소비자) → Secondly(제조사) → As a result(결과: 지속 가능한 사회)"),
 ([('❺', 3), ('❺', 4), ('❺', 5), ('❺', 6)], 1, "정답 ▶ ① (The impact of the index, however ~ 문장)\n이유: 프랑스 안의 효과 → however(하지만) 영향은 프랑스를 넘어 퍼질 것 → 이유: 세계 경제 → 다른 나라도 따를 것")]
ODD = [([('❹', 1), ('❹', 2), "Many French consumers still prefer to buy products with a red label.", ('❹', 3)], 2, "정답 ▶ ③\n이유: 지수가 어떻게 매겨지고 어떻게 표시되는지 설명하는 흐름이에요. 소비자가 빨간 라벨(수리 어려움) 제품을 선호한다는 말은 관계없고 지수의 목적과도 반대예요."),
 ([('❺', 4), ('❺', 5), "French companies are not allowed to sell their products abroad.", ('❺', 6)], 2, "정답 ▶ ③\n이유: 지수의 영향이 세계로 퍼진다는 흐름이에요. 프랑스 회사가 해외에서 팔 수 없다는 말은 관계없어요.")]
BLANK = [BL(d, 'Using a score', 'color-coded', ["handwritten", "secret", "voice-activated"], "정답 ▶ color-coded (색깔로 구분된)\n이유: 뒤에서 빨간 라벨·초록 라벨로 구분 → 색상 체계\n오답 ▶ handwritten 손으로 쓴 · secret 비밀의 · voice-activated 음성으로 작동하는"),
 BL(d, 'The index takes', 'the ease of disassembly', ["the color of the product", "the brand's popularity", "the weight of the box"], "정답 ▶ the ease of disassembly (분해의 용이성)\n이유: '수리 가능성'과 관련된 요소 → 수리 정보·분해 용이성·예비 부품 가격\n오답 ▶ 제품 색깔 · 브랜드 인기 · 상자 무게 → 수리와 무관"),
 BL(e, 'As a result', 'sustainable', ["wasteful", "crowded", "traditional"], "정답 ▶ sustainable (지속 가능한)\n이유: 매립지로 가는 쓰레기가 줄어듦 → '지속 가능한' 사회\n오답 ▶ wasteful 낭비하는 · crowded 붐비는 · traditional 전통적인")]
GRAM = [{'q': "빈칸에 알맞은 것은?<br><b>The bill requires that every manufacturer ______ a repairability index.</b>", 'opts': ["include", "includes", "included", "including"], 'ex': "정답 ▶ include\n이유: require that + 주어 + (should) 동사원형"},
 {'q': "빈칸에 알맞은 것은?<br><b>The index lets consumers see how ______ the product can be repaired.</b>", 'opts': ["easily", "easy", "ease", "easier"], 'ex': "정답 ▶ easily\n이유: can be repaired(동사)를 꾸미는 부사"},
 {'q': "빈칸에 알맞은 것은?<br><b>A low number means repairing will be difficult, ______ a high number indicates it is easy.</b>", 'opts': ["whereas", "despite", "because of", "unless"], 'ex': "정답 ▶ whereas\n이유: 대조의 접속사(~인 반면에). despite/because of는 전치사"},
 {'q': "빈칸에 알맞은 것은?<br><b>We can anticipate ______ more countries following France's lead.</b>", 'opts': ["seeing", "to see", "see", "seen"], 'ex': "정답 ▶ seeing\n이유: anticipate + 동명사"}]
