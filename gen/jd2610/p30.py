from jfw import *
S = PREP['30']['sents'][:]; assert 'is decreased' in S[6]; S[6] = S[6].replace('is decreased', 'is increased')
p = load(30, '30번 · 어휘', sents=S)
VOCAB = words(30, add=[("emission", "배출(량)"), ("opportunity set", "기회 집합(선택할 수 있는 범위)")])
EXAM = [EXQ(30, '30. 다음 글의 밑줄 친 부분 중, 문맥상 낱말의 쓰임이 적절하지 않은 것은?', underlined(30, ['higher', 'obvious', 'decreased', 'distorts', 'lower']), ["①", "②", "③", "④", "⑤"], 2,
 "정답 ▶ ③ decreased → increased\n이유: 보조금으로 전력 회사의 기회 집합은 '확대(expansion)'되고, 그만큼 다른 사람들의 기회 집합은 '축소(contraction)' → 전력 회사의 '자유'는 보통 개인을 희생시켜(at the expense of) '증가'한다. 개인은 보조금을 대기 위한 세금 증가로 고통받음\n오답 ▶ ① 전환해도 이익이 '더 높을' 수 있음 ✔ ② 이유는 '명백' — 자기 돈 대신 정부 돈을 받고 싶으니까 ✔ ④ 전체 비용을 직면하지 않으니 경제를 '왜곡' ✔ ⑤ 비용을 다 안 내니 전기 가격이 원래보다 '낮아지고' 소비는 늘어남 ✔\n포인트 ▶ at the expense of ~(~을 희생시켜) → 한쪽은 늘고 다른 쪽은 줄어듦", v=False),
 EXQ(30, '다음 글의 요지로 가장 적절한 것은?', p.full(), [
 "발전소 보조금은 일반 개인에게 부담을 지우고 경제를 왜곡할 수 있다.", "보조금은 오염을 줄이는 가장 공정하고 효율적인 방법이다.", "석탄 발전은 비용이 가장 적게 드는 에너지원이다.",
 "전기 가격이 낮을수록 지구 온난화가 줄어든다.", "규제와 세금은 발전소의 이익을 항상 줄인다."], 0,
 "정답 ▶ ① 발전소 보조금은 일반 개인에게 부담을 지우고 경제를 왜곡할 수 있다.\n이유: 회사의 자유는 개인을 희생시켜 증가(세금 부담) + 보조금은 경제를 왜곡(distorts) → 전기 가격이 낮아져 소비가 늘고 온난화 악화\n오답 ▶ ② 반대 ③ 석탄에서 '전환'하는 이야기 ④ 낮은 가격 → 소비 증가 → 온난화 '악화' ⑤ 모든 경우 이익이 더 높을 수 있다고 함"),
 EXQ(30, '다음 빈칸에 들어갈 말로 가장 적절한 것은?', p.blank('full costs'), ["full costs", "small benefits", "new rules", "public support", "high taxes"], 0,
 "정답 ▶ ① full costs (전체 비용)\n이유: 보조금을 받으니 자신이 하는 일의 비용을 '전부' 부담하지 않음 → 그래서 효율성 관점에서 경제가 왜곡되고, 전기 가격이 원래보다 낮아짐\n오답 ▶ ② 작은 이익 ③ 새 규칙 ④ 대중의 지지 ⑤ 높은 세금 — 세금은 개인이 부담")]
PICK1 = [PK(p, 'Subsidies, taxes', 'less', 'more', "정답 ▶ less (덜)\n오답 ▶ more (더)\n이유: 석탄에서 '벗어나' 전환하면 오염을 '덜' 일으킴"),
 PK(p, 'The power plants prefer', 'subsidies', 'taxes', "정답 ▶ subsidies (보조금)\n오답 ▶ taxes (세금)\n이유: 다음 문장 — 직접 비용을 내기보다 정부 돈을 '받는' 걸 선호 → 보조금"),
 PK(p, 'But the “expansion”', 'contraction', 'expansion', "정답 ▶ contraction (축소)\n오답 ▶ expansion (확대)\n이유: 한쪽의 '확대'는 다른 쪽의 '축소'로 맞춰져야 함"),
 PK(p, 'The electricity companies', 'increased', 'decreased', "정답 ▶ increased (증가된)\n오답 ▶ decreased (감소된)\n이유: 개인을 희생시켜(at the expense of) 회사의 자유는 '증가' — 원문항 ③번"),
 PK(p, 'Moreover', 'distorts', 'stabilizes', "정답 ▶ distorts (왜곡하다)\n오답 ▶ stabilizes (안정시키다)\n이유: 전체 비용을 직면하지 않으니 순수 효율성 관점에서 경제를 '왜곡'"),
 PK(p, 'Indeed, electricity', 'worsen', 'slow', "정답 ▶ worsen (악화시키다)\n오답 ▶ slow (늦추다)\n이유: 가격이 낮아지고 소비가 늘어나 지구 온난화를 '악화'")]
TF = [TF(p, "Subsidies, taxes, and regulations can all lead to less polluting power plants.", True, "power plants that pollute less", "정답 ▶ T\n이유: 셋 다 오염을 덜 일으키는 발전소로 이어질 수 있어요."),
 TF(p, "Power plants prefer taxes to subsidies.", False, "The power plants prefer subsidies over regulations or taxes", "정답 ▶ F\n이유: 규제나 세금보다 보조금을 선호해요."),
 TF(p, "Power plants would rather receive money from the government than pay costs themselves.", True, "prefer to receive money from the government rather than pay the costs themselves", "정답 ▶ T\n이유: 직접 비용을 내기보다 정부 돈을 받는 걸 선호해요.\n어휘 ▶ would rather A than B = prefer to A rather than B"),
 TF(p, "Ordinary individuals pay for the subsidy through increased taxes.", True, "suffer from increased taxation to pay for the subsidy", "정답 ▶ T\n이유: 보조금을 대기 위한 세금 증가로 고통받아요."),
 TF(p, "With subsidies, electricity companies face the full costs of what they do.", False, "is not facing the full costs of what it does", "정답 ▶ F\n이유: 전체 비용을 직면하지 않아요."),
 TF(p, "Lower electricity prices may lead to higher electricity consumption.", True, "electricity prices may end up lower than they should be and electricity consumption higher", "정답 ▶ T\n이유: 가격이 낮아지고 소비가 늘어날 수 있어요.")]
MC = [MC(p, "글의 내용과 일치하지 <u>않는</u> 것은?", [
 "Subsidies always reduce global warming.", "Profits can be higher after switching from coal.", "The expansion for some must be matched by contraction for others.",
 "The subsidy is paid for by increased taxation.", "Emissions per unit of electricity may be reduced."],
 "정답 ▶ Subsidies always reduce global warming.\n이유: which will worsen global warming, even though the emissions per unit of electricity have been reduced\n포인트 ▶ even though(비록 ~일지라도) — 단위당 배출은 줄어도 전체로는 악화",
 [["보조금은 항상 지구 온난화를 줄인다.", "which will worsen global warming", "✗ 악화"], ["석탄에서 전환한 뒤 이익이 더 높을 수 있다.", "profits can be higher from making the transition", "일치"], ["일부의 확대는 다른 이들의 축소로 맞춰져야 한다.", "has to be matched by the contraction", "일치"], ["보조금은 늘어난 세금으로 충당된다.", "increased taxation to pay for the subsidy", "일치"], ["전기 단위당 배출량은 줄 수 있다.", "the emissions per unit of electricity have been reduced", "일치"]])]
PICK2 = [PK(p, 'Subsidies, taxes', 'that pollute', 'pollute', "정답 ▶ that pollute\n이유: power plants를 꾸미는 관계절 — 주격 관계대명사 that 필요 (동사 can lead가 이미 있음)"),
 PK(p, 'Subsidies, taxes', 'switching', 'switch', "정답 ▶ switching\n이유: 전치사 by 뒤 동명사 (~함으로써)"),
 PK(p, 'In all cases', 'taking', 'take', "정답 ▶ taking\n이유: even + 분사구문 (~을 고려하더라도)"),
 PK(p, 'In all cases', 'related', 'relating', "정답 ▶ related\n이유: 관련된(수동) 비용 → 과거분사"),
 PK(p, 'They prefer', 'themselves', 'them', "정답 ▶ themselves\n이유: 주어 They가 '직접' — 강조의 재귀대명사"),
 PK(p, 'But the “expansion”', 'be matched', 'match', "정답 ▶ be matched\n이유: 확대가 축소에 의해 '맞춰지는' 수동 (by ~)"),
 PK(p, 'The electricity companies', 'who must', 'they must', "정답 ▶ who\n이유: 콤마 뒤에서 the ordinary individual을 설명하는 계속적 용법 관계대명사. they를 쓰면 접속사 없이 두 절이 이어져요.")]
VERB = [VB(p, 'The electricity companies', 'to pay', 'pay', "정답 ▶ to pay\n이유: 목적의 to부정사 (보조금을 지급하기 위해)"),
 VB(p, 'Moreover', 'facing', 'face', "정답 ▶ facing\n이유: is not + -ing 현재진행"),
 VB(p, 'Moreover', 'limiting', 'limit', "정답 ▶ limiting\n이유: be successful in + 동명사"),
 VB(p, 'Indeed, electricity', 'reduced', 'reduce', "정답 ▶ reduced\n이유: 배출량이 '줄어든' 수동 → have been reduced")]
ERR = [ER(p, 'They prefer', ['to receive', ('pay', 'pays'), 'themselves'], 1, 'pay', "틀린 곳 ▶ ② pays → pay\n이유: prefer to A rather than B — B도 동사원형 (to receive와 병렬)\n나머지 ▶ ① prefer + to부정사 ✔ ③ 재귀대명사 ✔"),
 ER(p, 'Moreover', [('because', 'because of'), 'facing', 'what'], 0, 'because', "틀린 곳 ▶ ① because of → because\n이유: 뒤에 절(the electricity company is ~) → 접속사\n나머지 ▶ ② 진행형 ✔ ③ of 뒤 + does의 목적어 없음 → what ✔"),
 ER(p, 'Indeed, electricity', [('they', 'it'), 'which', 'have'], 0, 'they', "틀린 곳 ▶ ① it → they\n이유: 가리키는 것 electricity prices(복수)\n나머지 ▶ ② 앞 절 전체를 받는 계속적 용법 which ✔ ③ 주어 the emissions(복수) → have ✔")]
SCR = [1, 2, 4, 5, 7]
ORDER = [[1, 2, 3, 4], [5, 6, 7, 8]]
INSERT = [([2, 3, 4, 5], 2, "정답 ▶ ② (They prefer ~ 문장)\n이유: 이유는 명백하다 → 그 이유: 직접 내기보다 정부 돈을 받고 싶으니까 → But 그 확대는 다른 이의 축소로 맞춰져야"),
 ([6, 7, 8], 1, "정답 ▶ ① (Moreover ~ 문장)\n이유: 개인의 희생(공정성 문제) → Moreover(게다가) 효율성 관점에서도 왜곡 → Indeed 가격·소비·온난화")]
ODD = [([2, 3, "Solar panels have become cheaper and more popular in many countries.", 4], 2, "정답 ▶ ③\n이유: 발전소가 보조금을 선호하는 이유와 그 문제점을 설명하는 흐름이에요. 태양광 패널 가격 이야기는 관계없어요.")]
BLANK = [BL(p, 'Subsidies, taxes', 'coal', ["water", "wind", "sunlight"], "정답 ▶ coal (석탄)\n이유: 오염을 덜 일으키려면 '석탄'에서 벗어나야(switching away from)\n오답 ▶ water 물 · wind 바람 · sunlight 햇빛 — 모두 친환경 에너지라 벗어날 대상이 아님"),
 BL(p, 'The electricity companies', 'at the expense of', ["for the benefit of", "with the help of", "in honor of"], "정답 ▶ at the expense of (~을 희생시켜)\n이유: 개인은 늘어난 세금으로 '고통받아야(must suffer)' 함 → 개인의 희생\n오답 ▶ ~의 이익을 위해 · ~의 도움으로 · ~을 기념하여"),
 BL(p, 'Moreover', 'efficiency', ["fairness", "beauty", "tradition"], "정답 ▶ efficiency (효율성)\n이유: 앞 문장(개인의 희생)은 공정성 문제, Moreover로 '효율성' 관점 추가 → 전체 비용을 안 내서 경제 왜곡\n오답 ▶ fairness 공정성(앞에서 다룸) · beauty 아름다움 · tradition 전통")]
GRAM = [{'q': "빈칸에 알맞은 것은?<br><b>They prefer to receive money rather than ______ the costs themselves.</b>", 'opts': ["pay", "pays", "paying", "paid"], 'ex': "정답 ▶ pay\n이유: prefer to A rather than (to) B → 동사원형"},
 {'q': "빈칸에 알맞은 것은?<br><b>The expansion has to ______ by the contraction of others.</b>", 'opts': ["be matched", "match", "matching", "matched"], 'ex': "정답 ▶ be matched\n이유: has to be p.p. 수동"},
 {'q': "빈칸에 알맞은 것은?<br><b>The company is successful in ______ emissions.</b>", 'opts': ["limiting", "limit", "limited", "to limit"], 'ex': "정답 ▶ limiting\n이유: be successful in + 동명사"},
 {'q': "빈칸에 알맞은 것은?<br><b>Prices may end up lower, ______ will worsen global warming.</b>", 'opts': ["which", "that", "what", "it"], 'ex': "정답 ▶ which\n이유: 콤마 뒤 앞 절 전체를 받는 계속적 용법 → which (that 불가)"}]
SUMQ = [SUM(p, "Power plants prefer subsidies, but subsidies place a burden on (A) ______ taxpayers and can make electricity prices (B) ______ than they should be.", [
 "(A) ordinary – (B) lower", "(A) ordinary – (B) higher", "(A) wealthy – (B) lower", "(A) foreign – (B) higher", "(A) young – (B) stabler"],
 "정답 ▶ (A) ordinary – (B) lower\n(A) 보통 개인(the ordinary individual)이 세금 부담 → ordinary\n(B) 전기 가격이 원래보다 '낮아질' 수 있음 → lower\n오답 ▶ higher 더 높은(반대) · wealthy 부유한 · foreign 외국의",
 ["at the expense of the ordinary individual", "electricity prices may end up lower"])]
