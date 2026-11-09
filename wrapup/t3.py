from wu import *
# 34·35번
E1 = "Richard Heinberg, an American journalist, argues that in building the renewable energy infrastructure to stop global warming, we are actually involved in one of the greatest change projects in human history."
E2 = "In addition to solar panels and wind turbines, we have to build an alternative transport infrastructure, farming procedures and industrial processes."
E3 = "This transformation cannot happen without fossil fuels."
E4 = "For instance, production of concrete structures and steel elements require amounts of energy that is only possible to produce with fossil energy."
E5 = "Production of solar panels requires scarce and expensive minerals which must be excavated, again requiring the use of fossil fuels."
E6 = "Thus, the harder we push towards a renewable energy system, the faster we have to use fossil energy for the construction process."
E7 = "This is not only expensive, but also an undermining factor for our efforts to cut global emissions."
E8 = "Heinberg remarks that the cost of building this new energy infrastructure is seldom counted in transition proposals, which tend to focus just on energy supply requirements."
P34 = ' '.join([E1, E2, E3, E4, E5, E6, E7, E8])
F1 = "Humans for centuries have dreamed of machines that could become intelligent and make human-like decisions."
F2 = "There have been myths about robots, automatons, and artificial beings since ancient Greece (e.g., the myth of Pandora, who released ills upon the world)."
F3 = "Likewise, literature throughout history has dreamed of creating human-like creatures and thinking machines (e.g., Mary Shelley's <i>Frankenstein</i>)."
F4 = "In 1950, British mathematician Alan Turing asked whether machines could think and reason like humans and then developed the Turing test to measure a machine's intelligence and whether the machines can think autonomously."
F5 = "A few years later, MIT professor John McCarthy coined “artificial intelligence,” replacing the previously used expression “automata studies.”"
F6 = "Since then, artificial intelligence has become the study and practice of “making intelligent machines” that are programmed to think like humans — endowed by their creators with reasoning and learning."
P35 = ' '.join([F1, F2, F3, F4, F5, F6])

T = Test('3435', '34·35번', '재생에너지 전환의 숨은 비용 · 인공지능이라는 꿈', '34·35번',
         '범위: 34번(재생에너지 기반 시설을 짓는 데도 화석 연료가 든다) · 35번(생각하는 기계라는 오랜 꿈과 인공지능의 탄생). 지문은 원문을 일부 바꾼 것이 있어요. 선택지는 본문 표현을 다른 말로 바꿔 썼으니 뜻을 정확히 따져 보세요.')

# ── 34번 ──
T.flex('다음 글의 요지로 가장 적절한 것은?', '34번', BOX(P34), [
    '재생에너지 체계를 짓는 일 자체에 화석 연료가 많이 들기 때문에 그 건설 비용도 따져 봐야 한다.',
    '지구 온난화를 막으려면 화석 연료 사용을 지금 당장 모두 멈춰야 한다.',
    '태양광 패널 생산비를 줄이는 기술 개발이 무엇보다 시급하다.',
    '재생에너지는 어떤 경우에도 화석 연료보다 경제적이다.',
    '농업 방식을 바꾸는 것이 탄소 배출을 줄이는 가장 쉬운 방법이다.'],
    "이유 ▶ 재생에너지 기반 시설로의 전환은 화석 연료 없이는 불가능하고(cannot happen without fossil fuels), 그 건설 비용이 전환 계획에서 거의 고려되지 않는다(seldom counted)는 것이 요지.\n오답 ▶ {1} 오히려 전환하려면 화석 연료가 필요하다고 했다 {2} 태양광 패널은 광물 채굴의 예시일 뿐 {3} 비싸다(expensive)고 했다 {4} 농업 방식은 지어야 할 것들의 나열 중 하나\n포인트 ▶ 마지막 문장(Heinberg remarks ~ seldom counted)이 글쓴이가 전하려는 핵심.",
    [['renewable energy', '재생에너지'], ['infrastructure', '기반 시설'], ['fossil fuel', '화석 연료'], ['transition', '전환']], en=False)

T.flex('다음 빈칸에 들어갈 말로 가장 적절한 것은?', '34번 변형', BOX(
    E1 + ' ' + E2 + ' ' + E3 + ' ' + E4 + ' ' + E5 + ' Thus, the harder we push towards a renewable energy system, ' + BL + '. ' + E7 + ' ' + E8), [
    ('the more fossil fuel we must burn to build it', '그것을 짓기 위해 더 많은 화석 연료를 태워야 한다'),
    ('the sooner we can stop using fossil fuels altogether', '화석 연료 사용을 더 빨리 완전히 멈출 수 있다'),
    ('the cheaper solar panels and wind turbines become', '태양광 패널과 풍력 터빈이 더 싸진다'),
    ('the less energy the construction process requires', '건설 과정에 드는 에너지가 더 적어진다'),
    ('the more scarce minerals we can save', '더 많은 희귀 광물을 아낄 수 있다')],
    "이유 ▶ 원문: the faster we have to use fossil energy for the construction process. 콘크리트·철강 생산, 광물 채굴에 모두 화석 연료가 든다(앞 예시) → Thus 재생에너지 체계로 세게 밀어붙일수록 짓는 데 화석 연료를 더 많이(빨리) 써야 한다.\n오답 ▶ {1} 전환 과정에서는 오히려 더 써야 한다 {2} 비싸다(expensive)고 했다 {3} 건설에는 많은 에너지가 든다 {4} 광물은 채굴해야 한다(must be excavated)\n포인트 ▶ 뒤 문장 This is not only expensive ~ undermining factor: This = 화석 연료를 더 쓰는 것.",
    [['push towards', '~을 향해 밀어붙이다'], ['altogether', '완전히'], ['construction', '건설'], ['scarce', '희귀한, 부족한']])

T.flex('다음 글의 내용과 일치하는 것은?', '34번', BOX(P34), [
    ('Making solar panels involves mining rare and costly minerals.', '태양광 패널을 만드는 데는 희귀하고 값비싼 광물을 캐는 일이 따른다.'),
    ('Heinberg sees the energy transition as a small-scale project.', 'Heinberg는 에너지 전환을 작은 규모의 사업으로 본다.'),
    ('Concrete and steel can easily be produced with renewable energy alone.', '콘크리트와 철강은 재생에너지만으로 쉽게 생산할 수 있다.'),
    ('Transition proposals usually include the full cost of building new infrastructure.', '전환 계획은 대개 새 기반 시설을 짓는 비용 전체를 포함한다.'),
    ('Using fossil fuels during construction helps lower global emissions.', '건설 중에 화석 연료를 쓰는 것은 전 세계 배출량을 낮추는 데 도움이 된다.')],
    "이유 ▶ Production of solar panels requires scarce and expensive minerals which must be excavated = 희귀하고(rare) 값비싼(costly) 광물을 캐야(mining) 한다 ✔\n오답 ▶ {1} one of the greatest change projects in human history(인류 역사상 가장 큰 변화 사업 중 하나) {2} 화석 에너지로만 생산 가능한 양의 에너지가 든다 {3} 건설 비용은 거의 계산되지 않는다(seldom counted) {4} 배출량 감축 노력을 약화시키는 요인(undermining factor)\n포인트 ▶ excavate = dig out = mine(캐다), scarce = rare.",
    [['mine', '캐다, 채굴하다'], ['costly', '값비싼'], ['small-scale', '소규모의'], ['emission', '배출(량)']])

T.fixed('다음 글의 밑줄 친 부분 중, 문맥상 낱말의 쓰임이 적절하지 <u>않은</u> 것은?', '34번 변형', BOX(
    E1 + " In addition to solar panels and wind turbines, we have to build an " + CN(1, 'alternative') + " transport infrastructure, farming procedures and industrial processes. " + E3 + " For instance, producing concrete structures and steel elements requires amounts of energy that are only possible to produce with fossil energy. Production of solar panels requires " + CN(2, 'scarce') + " and expensive minerals which must be " + CN(3, 'excavated') + ", again requiring the use of fossil fuels. Thus, the harder we push towards a renewable energy system, the " + CN(4, 'slower') + " we have to use fossil energy for the construction process. " + E7 + " Heinberg remarks that the cost of building this new energy infrastructure is " + CN(5, 'seldom') + " counted in transition proposals, which tend to focus just on energy supply requirements."),
    ['alternative', 'scarce', 'excavated', 'slower', 'seldom'], 4,
    "이유 ▶ 콘크리트·철강·광물 모두 화석 연료가 필요하므로, 재생에너지 체계로 세게 밀어붙일수록 화석 에너지를 '더 빨리' 써야 한다 → <i>faster</i>. slower(더 느리게)는 반대이고, 뒤 문장 '비싸고 배출 감축을 약화시킨다'와도 맞지 않는다.\n오답 ▶ ① '대체' 교통 기반 시설 ✔ ② '희귀하고' 비싼 광물 ✔ ③ 광물은 '채굴되어야' 한다 ✔ ⑤ 건설 비용은 전환 계획에서 '거의 ~않게' 계산된다 ✔\n포인트 ▶ the 비교급 ~, the 비교급 …에서 두 비교급의 방향(harder ↔ faster)이 맞는지 확인.",
    [['alternative', '대체의'], ['excavate', '파내다, 채굴하다'], ['seldom', '좀처럼 ~않는'], ['procedure', '절차, 방식']])

T.fixed('다음 글의 밑줄 친 부분 중, 어법상 <u>틀린</u> 것은?', '34번 변형', BOX(
    "Richard Heinberg, an American journalist, " + CN(1, 'argues') + " that in building the renewable energy infrastructure to stop global warming, we are actually involved in one of the greatest change projects in human history. … Production of solar panels requires scarce and expensive minerals " + CN(2, 'which') + " must be excavated, again " + CN(3, 'required') + " the use of fossil fuels. … This is not only expensive, but also an " + CN(4, 'undermining') + " factor for our efforts to cut global emissions. Heinberg remarks that the cost of building this new energy infrastructure " + CN(5, 'is') + " seldom counted in transition proposals, which tend to focus just on energy supply requirements."),
    ['argues', 'which', 'required', 'undermining', 'is'], 3,
    "이유 ▶ 앞 절 전체(광물을 채굴해야 한다는 것)가 다시 화석 연료 사용을 '요구하는' 능동 의미의 분사구문 → <i>requiring</i>. required는 동사로 보면 접속사 없이 동사가 하나 더 생긴다.\n오답 ▶ ① 주어 Richard Heinberg(단수), 콤마 사이는 동격 → argues ✔ ② 선행사 minerals(사물), 주어 역할 관계대명사 ✔ ④ factor를 꾸미는 현재분사(약화시키는 요인) ✔ ⑤ 주어 the cost(단수), of building ~은 수식어 → is ✔\n포인트 ▶ 콤마 뒤 접속사 없는 동사 자리 → 분사구문(-ing / p.p.)인지 확인.",
    [['argue', '주장하다'], ['excavate', '채굴하다'], ['undermine', '약화시키다'], ['remark', '언급하다']])

T.table('(A), (B), (C)의 각 네모 안에서 어법에 맞는 표현으로 가장 적절한 것은?', '34번', BOX(
    "Richard Heinberg argues that in building the renewable energy infrastructure to stop global warming, we are actually <b>(A)</b> [ involved / involving ] in one of the greatest change projects in human history. … Thus, the harder we push towards a renewable energy system, the <b>(B)</b> [ faster / fast ] we have to use fossil energy for the construction process. … Heinberg remarks that the cost of building this new energy infrastructure is seldom counted in transition proposals, <b>(C)</b> [ which / that ] tend to focus just on energy supply requirements."),
    ['(A)', '(B)', '(C)'], [['involved', 'faster', 'which'], ['involving', 'faster', 'which'], ['involved', 'fast', 'which'], ['involved', 'faster', 'that'], ['involving', 'fast', 'that']],
    "이유 ▶ (A) be involved in(~에 관여하다, 참여하다) → <i>involved</i> (B) the 비교급 ~, the 비교급 … → <i>faster</i> (C) 콤마 뒤 계속적 용법 → <i>which</i> (that은 계속적 용법 불가)\n오답 ▶ involving: 뒤에 목적어 없이 in이 오므로 수동 / fast: the harder와 짝을 이루려면 비교급 / that: 콤마 뒤 불가\n포인트 ▶ 콤마 + that ✗, 전치사 + that ✗ — 관계대명사 that의 두 가지 금지!",
    [['be involved in', '~에 관여하다'], ['the 비교급, the 비교급', '~할수록 더 …하다'], ['proposal', '제안, 계획']])

T.fixed('글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳은?', '34번', GIV(E3) + '\n' + BOX(
    E1 + GP(1) + E2 + GP(2) + E4 + GP(3) + E5 + GP(4) + E6 + GP(5) + E7),
    None, 2,
    "이유 ▶ This transformation(이 변화) = 앞 문장의 태양광·풍력·교통·농업·산업을 모두 새로 짓는 일. 그리고 뒤의 For instance(예를 들어) 콘크리트·철강 생산에 화석 에너지가 든다는 예가 '화석 연료 없이는 불가능하다'를 뒷받침한다 → ②.\n오답 ▶ ① 아직 무엇을 지어야 하는지 나오지 않았다 ③④ For instance 예시가 주장보다 먼저 나오게 된다 ⑤ Thus 결론 뒤라 늦다\n포인트 ▶ For instance 바로 앞에는 그 예시가 뒷받침할 주장이 있어야 한다.",
    [['transformation', '변화, 전환'], ['for instance', '예를 들어']])

T.table('다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 적절한 것은?', '34번', BOX(P34) + '\n' + SUM(
    'Building a renewable energy system <b>(A)</b> ' + BL + ' heavily on fossil fuels, but this cost is something that transition proposals often <b>(B)</b> ' + BL + '.'),
    ['(A)', '(B)'], [['depends', 'overlook'], ['depends', 'emphasize'], ['saves', 'overlook'], ['saves', 'calculate'], ['focuses', 'exaggerate']],
    "이유 ▶ (A) 이 전환은 화석 연료 없이는 불가능 → <i>depends</i> heavily on(크게 의존한다) (B) 건설 비용은 전환 계획에서 거의 계산되지 않는다(seldom counted) → <i>overlook</i>(간과하다)\n오답 ▶ saves(아낀다)·focuses(집중한다): 화석 연료에 의존한다는 말과 다르다 / emphasize(강조하다)·calculate(계산하다)·exaggerate(과장하다): 비용을 무시한다는 말과 반대\n포인트 ▶ seldom counted = overlooked = ignored.",
    [['depend on', '~에 의존하다'], ['overlook', '간과하다'], ['exaggerate', '과장하다']],
    ko=['의존한다 / 간과하다', '의존한다 / 강조하다', '아낀다 / 간과하다', '아낀다 / 계산하다', '집중한다 / 과장하다'])

T.flex('밑줄 친 <u>an undermining factor for our efforts to cut global emissions</u>가 의미하는 바로 가장 적절한 것은?', '34번', BOX(P34.replace('an undermining factor for our efforts to cut global emissions', U('an undermining factor for our efforts to cut global emissions'))), [
    '건설에 쓰이는 화석 연료가 늘어나 배출량을 줄이려는 노력을 방해하는 요인',
    '재생에너지 기술의 발전을 앞당기는 요인',
    '기반 시설을 짓는 비용을 줄여 주는 요인',
    '희귀 광물을 채굴할 필요를 없애 주는 요인',
    '에너지 공급량을 안정적으로 늘려 주는 요인'],
    "이유 ▶ This = 재생에너지 체계를 지으려고 화석 에너지를 더 빨리 쓰는 것. 화석 연료를 쓰면 배출이 늘어나므로 배출량 감축 노력을 약화시키는(undermining) 요인이 된다.\n오답 ▶ {1} 기술 발전 이야기가 아니다 {2} 비싸다(expensive)고 했다 {3} 광물은 채굴해야 한다 {4} 에너지 공급만 보는 것은 전환 계획의 한계로 나온다\n포인트 ▶ undermine = weaken(약화시키다).",
    [['undermine', '약화시키다'], ['effort', '노력'], ['cut', '줄이다']], en=False)

T.flex('다음 글의 제목으로 가장 적절한 것은?', '34번', BOX(P34), [
    ('The Hidden Fossil Fuel Cost of Going Green', '친환경으로 가는 데 숨은 화석 연료 비용'),
    ('Wind Turbines: The Cheapest Energy Source', '풍력 터빈: 가장 싼 에너지원'),
    ('Why Journalists Oppose Renewable Energy', '언론인들이 재생에너지에 반대하는 이유'),
    ('How New Farming Methods Will Save the Planet', '새로운 농업 방식이 지구를 구하는 방법'),
    ('Fossil Fuels Will Soon Run Out', '화석 연료는 곧 바닥날 것이다')],
    "이유 ▶ 재생에너지 체계를 짓는 데 화석 연료가 많이 들고, 그 비용은 전환 계획에서 잘 계산되지 않는다 → 친환경 전환의 숨은(hidden) 화석 연료 비용.\n오답 ▶ {1} 비용이 싸다는 말은 없다 {2} Heinberg는 반대하는 것이 아니라 숨은 비용을 지적할 뿐 {3} 농업은 나열의 일부 {4} 화석 연료 고갈은 다루지 않는다\n포인트 ▶ seldom counted(거의 계산되지 않는) = hidden(숨겨진).",
    [['hidden', '숨겨진'], ['go green', '친환경으로 바꾸다'], ['oppose', '반대하다'], ['run out', '바닥나다']])

# ── 35번 ──
T.flex('다음 글의 주제로 가장 적절한 것은?', '35번', BOX(P35), [
    ('the long-held human dream of thinking machines and the birth of AI', '생각하는 기계에 대한 인간의 오랜 꿈과 인공지능의 탄생'),
    ('the dangers of robots described in Greek myths', '그리스 신화에 묘사된 로봇의 위험성'),
    ('how Mary Shelley built the first robot', 'Mary Shelley가 최초의 로봇을 만든 방법'),
    ('the limitations of the Turing test', '튜링 테스트의 한계'),
    ('why machines will never learn like humans', '기계가 결코 인간처럼 배우지 못하는 이유')],
    "이유 ▶ 수 세기 동안의 꿈(신화·문학) → 튜링의 질문과 테스트 → 매카시의 '인공지능' 명명 → 학문이 된 인공지능. 오랜 꿈이 인공지능으로 이어진 역사.\n오답 ▶ {1} 판도라 신화는 예시일 뿐, 위험성이 주제가 아니다 {2} 프랑켄슈타인은 소설 속 이야기 {3} 테스트의 한계는 나오지 않는다 {4} 오히려 추론·학습 능력을 부여받은(endowed with reasoning and learning) 기계를 만든다\n포인트 ▶ 시간 순서(since ancient Greece → 1950 → a few years later → since then)로 전개되는 글의 주제 = 그 흐름 전체.",
    [['long-held', '오래 품어 온'], ['birth', '탄생'], ['limitation', '한계']])

T.flex('다음 글의 내용과 일치하지 <u>않는</u> 것은?', '35번', BOX(P35), [
    ('John McCarthy developed a test to measure machine intelligence.', 'John McCarthy는 기계의 지능을 측정하는 테스트를 개발했다.'),
    ('Stories of artificial beings date back to ancient Greece.', '인공적인 존재에 관한 이야기는 고대 그리스로 거슬러 올라간다.'),
    ('<i>Frankenstein</i> is an example of literature that imagined human-like creatures.', '<i>프랑켄슈타인</i>은 인간 같은 존재를 상상한 문학의 한 예이다.'),
    ('Turing questioned whether machines could reason like people.', '튜링은 기계가 사람처럼 추론할 수 있는지 물었다.'),
    ('The term “artificial intelligence” took the place of an earlier expression.', '"인공지능"이라는 용어는 이전 표현을 대신했다.')],
    "이유 ▶ 기계의 지능을 재는 테스트(Turing test)를 만든 사람은 앨런 튜링. 매카시는 '인공지능'이라는 용어를 만들었다(coined) ✗\n오답 ▶ {1} myths ~ since ancient Greece ✔ (date back to 거슬러 올라가다) {2} Mary Shelley's Frankenstein ✔ {3} asked whether machines could think and reason like humans ✔ {4} replacing the previously used expression \"automata studies\" ✔ (take the place of = replace)\n포인트 ▶ 인물이 여러 명 나오면 '누가 무엇을 했는지' 짝을 정확히!",
    [['date back to', '~로 거슬러 올라가다'], ['reason', '추론하다'], ['take the place of', '~을 대신하다'], ['term', '용어']])

T.flex('다음 빈칸에 들어갈 말로 가장 적절한 것은?', '35번 변형', BOX(
    F1 + ' ' + F2 + ' ' + F3 + ' ' + F4 + ' A few years later, MIT professor John McCarthy ' + BL + ', replacing the previously used expression “automata studies.” ' + F6), [
    ('came up with the term “artificial intelligence”', '"인공지능"이라는 용어를 만들어 냈다'),
    ('built the first human-like robot', '최초의 인간 같은 로봇을 만들었다'),
    ('proved that machines can never think', '기계는 결코 생각할 수 없다는 것을 증명했다'),
    ('criticized the Turing test as useless', '튜링 테스트가 쓸모없다고 비판했다'),
    ('wrote a famous novel about thinking machines', '생각하는 기계에 관한 유명한 소설을 썼다')],
    "이유 ▶ 원문: coined \"artificial intelligence\"(인공지능이라는 말을 만들었다). 뒤의 replacing the previously used expression(이전에 쓰던 '표현'을 대체하며)은 새 '용어'가 나왔다는 단서 → came up with the term.\n오답 ▶ {1} 로봇 제작은 나오지 않는다 {2} 이후 인공지능이 학문이 되었으므로 반대 {3} 테스트 비판은 없다 {4} 소설은 Mary Shelley의 예\n포인트 ▶ coin a word = 새 말을 만들다(= come up with a term).",
    [['come up with', '~을 생각해 내다'], ['coin', '(새 말을) 만들다'], ['criticize', '비판하다']])

T.fixed('다음 글의 밑줄 친 부분 중, 문맥상 낱말의 쓰임이 적절하지 <u>않은</u> 것은?', '35번 변형', BOX(
    "Humans for centuries have dreamed of machines that could become " + CN(1, 'intelligent') + " and make human-like decisions. There have been " + CN(2, 'myths') + " about robots, automatons, and artificial beings since ancient Greece (e.g., the myth of Pandora, who released ills upon the world). " + CN(3, 'In contrast') + ", literature throughout history has dreamed of creating human-like creatures and thinking machines (e.g., Mary Shelley's <i>Frankenstein</i>). " + F4 + " A few years later, MIT professor John McCarthy " + CN(4, 'coined') + " “artificial intelligence,” replacing the previously used expression “automata studies.” Since then, artificial intelligence has become the study and practice of “making intelligent machines” that are programmed to think like humans — " + CN(5, 'endowed') + " by their creators with reasoning and learning."),
    ['intelligent', 'myths', 'In contrast', 'coined', 'endowed'], 3,
    "이유 ▶ 신화에도 인공 존재가 있었고, 문학도 '마찬가지로' 인간 같은 존재를 꿈꿨다 → 같은 내용의 나열이므로 <i>Likewise</i>. In contrast(대조적으로)는 앞뒤가 반대일 때.\n오답 ▶ ① '지능을 가진' 기계 ✔ ② 고대 그리스 이래 '신화' ✔ ④ 인공지능이라는 말을 '만들었다' ✔ ⑤ 만든 사람에게서 추론·학습 능력을 '부여받은' ✔\n포인트 ▶ 연결어 문제: 앞뒤 내용이 같은 방향(신화도·문학도 꿈꿨다)이면 Likewise / Similarly.",
    [['likewise', '마찬가지로'], ['in contrast', '대조적으로'], ['automaton', '자동 기계(로봇)'], ['endow A with B', 'A에게 B를 부여하다']], en=False)

T.fixed('다음 글의 밑줄 친 부분 중, 어법상 <u>틀린</u> 것은?', '35번 변형', BOX(
    "Humans for centuries " + CN(1, 'have dreamed') + " of machines " + CN(2, 'that') + " could become intelligent and make human-like decisions. There " + CN(3, 'have been') + " myths about robots, automatons, and artificial beings since ancient Greece. … In 1950, British mathematician Alan Turing asked " + CN(4, 'whether') + " machines could think and reason like humans and then " + CN(5, 'developing') + " the Turing test to measure a machine's intelligence."),
    ['have dreamed', 'that', 'have been', 'whether', 'developing'], 5,
    "이유 ▶ 주어 Alan Turing의 동사 asked와 and then으로 병렬 → 과거 동사 <i>developed</i>.\n오답 ▶ ① for centuries(수 세기 동안) 지금까지 이어진 일 → 현재완료 ✔ ② 선행사 machines, 주어 역할 관계대명사 ✔ ③ There + be + 복수 주어 myths, since ~ → 현재완료 have been ✔ ④ asked의 목적어 명사절(~인지 아닌지) ✔\n포인트 ▶ and 앞뒤 병렬: asked ~ and then developed (같은 시제·형태).",
    [['for centuries', '수 세기 동안'], ['mathematician', '수학자'], ['measure', '측정하다']], en=False)

T.table('(A), (B), (C)의 각 네모 안에서 어법에 맞는 표현으로 가장 적절한 것은?', '35번', BOX(
    "In 1950, British mathematician Alan Turing asked <b>(A)</b> [ whether / that ] machines could think and reason like humans. … A few years later, MIT professor John McCarthy coined “artificial intelligence,” replacing the <b>(B)</b> [ previous / previously ] used expression “automata studies.” Since then, artificial intelligence has become the study and practice of “making intelligent machines” that <b>(C)</b> [ is / are ] programmed to think like humans."),
    ['(A)', '(B)', '(C)'], [['whether', 'previously', 'are'], ['that', 'previously', 'are'], ['whether', 'previous', 'are'], ['whether', 'previously', 'is'], ['that', 'previous', 'is']],
    "이유 ▶ (A) ask의 목적어로 '~인지 아닌지' → <i>whether</i> (B) 과거분사 used(쓰인)를 꾸미는 부사 → <i>previously</i> (이전에 쓰인 표현) (C) 관계대명사 that의 선행사 intelligent machines(복수) → <i>are</i>\n오답 ▶ that: ask(묻다)는 의문의 내용이 필요 / previous: 형용사는 분사 used를 꾸밀 수 없다 / is: 선행사를 the study로 착각\n포인트 ▶ 주격 관계대명사 뒤 동사는 선행사에 수 일치!",
    [['ask whether', '~인지 묻다'], ['previously', '이전에'], ['program', '프로그램을 짜다']])

T.fixed('주어진 글 다음에 이어질 글의 순서로 가장 적절한 것은?', '35번', GIV(F1) + '\n' + BOX(
    '<b>(A)</b> ' + F5 + ' ' + F6 + '</p><p><b>(B)</b> ' + F4 + '</p><p><b>(C)</b> ' + F2 + ' ' + F3),
    ['(A) − (C) − (B)', '(B) − (A) − (C)', '(B) − (C) − (A)', '(C) − (A) − (B)', '(C) − (B) − (A)'], 5,
    "이유 ▶ 주어진 글: 사람들은 수 세기 동안 생각하는 기계를 꿈꿔 왔다 → (C) 고대 그리스 신화, Likewise 문학도 → (B) 1950년 튜링 → (A) A few years later(몇 년 뒤) 매카시의 '인공지능', Since then(그때부터) 학문이 됨.\n오답 ▶ (A)의 A few years later는 1950년(B) 뒤에만 올 수 있다 / (C)의 since ancient Greece가 가장 오래된 시기\n포인트 ▶ 시간 표현(since ancient Greece → In 1950 → A few years later → Since then)으로 순서 잡기.",
    [['a few years later', '몇 년 뒤'], ['since then', '그때부터'], ['myth', '신화']], en=False)

T.fixed('다음 글에서 전체 흐름과 관계 <u>없는</u> 문장은?', '35번 변형', BOX(
    F1 + ' ' + CN(1, F2) + ' ' + CN(2, F3) + ' ' + CN(3, F4) + ' ' + CN(4, 'Today, many people fear that intelligent machines will take away jobs that humans now do.') + ' ' + CN(5, F5) + ' ' + F6),
    None, 4,
    "이유 ▶ 글은 생각하는 기계라는 꿈이 신화·문학 → 튜링 → 매카시의 '인공지능'으로 이어진 역사. ④ 오늘날 일자리를 빼앗길까 걱정한다는 내용은 이 역사의 흐름과 관계없다. 또 ④ 때문에 ⑤의 A few years later(1950년의 몇 년 뒤)가 오늘날(Today) 뒤에 오는 어색한 흐름이 된다.\n오답 ▶ ① 고대 신화 ② 문학 ③ 1950년 튜링 ⑤ 몇 년 뒤 매카시 — 모두 시간 순서로 이어진다\n포인트 ▶ 무관한 문장은 소재(기계·인공지능)는 같지만 글의 초점(꿈의 역사)에서 벗어난 문장.",
    [['take away', '빼앗다'], ['fear', '두려워하다']])

T.table('다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 적절한 것은?', '35번', BOX(P35) + '\n' + SUM(
    'From ancient <b>(A)</b> ' + BL + ' to modern science, humans have long imagined thinking machines, a dream that eventually gave rise to the <b>(B)</b> ' + BL + ' of artificial intelligence.'),
    ['(A)', '(B)'], [['myths', 'field'], ['myths', 'failure'], ['wars', 'field'], ['machines', 'end'], ['laws', 'rejection']],
    "이유 ▶ (A) 고대 그리스 신화(myths)부터 → <i>myths</i> (B) 인공지능이 '지능을 가진 기계를 만드는 연구와 실천'이 되었다 → 인공지능이라는 <i>field</i>(분야)\n오답 ▶ wars·laws: 본문에 없다 / machines: 고대에는 기계가 아니라 신화 속 이야기 / failure(실패)·end(끝)·rejection(거부): 인공지능이 학문이 되었다는 말과 반대\n포인트 ▶ give rise to = ~을 낳다, 생기게 하다.",
    [['give rise to', '~을 낳다'], ['field', '분야'], ['rejection', '거부']],
    ko=['신화 / 분야', '신화 / 실패', '전쟁 / 분야', '기계 / 끝', '법 / 거부'])

# ── 종합 ──
T.flex('34·35번 지문에 나온 단어와 영영풀이가 바르게 짝지어지지 <u>않은</u> 것은?', '종합', '', [
    '<b>excavate</b> : to build something on top of the ground',
    '<b>infrastructure</b> : the basic systems and structures that a society needs',
    '<b>scarce</b> : not available in large amounts',
    '<b>coin</b> : to invent a new word or phrase',
    '<b>autonomously</b> : without being controlled by others'],
    "이유 ▶ excavate는 '땅을 파내다, 채굴하다'(to dig out of the ground). 땅 위에 무언가를 짓는 것과 반대.\n오답 ▶ {1} infrastructure 기반 시설 ✔ {2} scarce 부족한, 희귀한 ✔ {3} coin (새 말을) 만들다 ✔ {4} autonomously 자율적으로 ✔\n포인트 ▶ excavate = dig out, mine.",
    [['excavate', '파내다, 채굴하다'], ['dig', '파다'], ['autonomously', '자율적으로']])

T.render()
