from jfw import *
R = PREP['38']['sents']; G = PREP['38']['given']
S = R[:4] + [G] + R[4:]
p = load(38, '38번 · 문장 삽입', sents=S)
VOCAB = words(38)
EXAM = [EXQ(38, '38. 글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳은?', p.insert_q(4, [1, 2, 3, 5, 6]), SLOT, 3,
 "정답 ▶ ④\n이유: 규칙은 물을 어디에 쓰든(마시기·작물·보일러) 안전하게 보장 → 주어진 문장: 물을 매우 다양한 일에 쓰므로 '일률적인' 규칙을 쓸 수 없다 → For instance 발전기 냉각수는 마시는 물만큼 깨끗할 필요 없음 → 그래서 용도에 따라 다른 안전 허용치\n오답 ▶ ①~③ 아직 '기준·지침'을 설명하는 중 — 다양한 용도 이야기가 나오기 전 ⑤ For instance(예시)가 주어진 문장의 '다른 기준' 주장보다 먼저 나오게 됨\n포인트 ▶ For instance 앞에는 그 예시가 뒷받침할 주장(one size fits all 불가)이 있어야 해요.", v=False),
 EXQ(38, '다음 글의 제목으로 가장 적절한 것은?', p.full(), [
 "Clean Water Depends on How It Is Used", "Why Tap Water Is Always Safe to Drink", "How Power Plants Pollute Rivers",
 "One Rule for All: The Best Water Policy", "The Taste of Clean Water"], 0,
 "정답 ▶ ① 깨끗한 물은 용도에 달려 있다\n이유: '깨끗하다'는 겉모습이 아니라 기준을 따르는 것 → 용도가 다양해 일률적 규칙 불가 → 용도에 따라 다른 안전 허용치\n오답 ▶ ② 수돗물 안전성 아님 ③ 오염 이야기 아님 ④ 일률적 규칙은 '불가'(반대) ⑤ 맛 이야기 없음\n포인트 ▶ dependent on how it will be utilized = 용도에 따라"),
 EXQ(38, '다음 빈칸에 들어갈 말로 가장 적절한 것은?', p.blank('different “safety limits”'), [
 "different “safety limits”", "the same “safety limits”", "lower water prices", "stricter drinking rules", "no limits at all"], 0,
 "정답 ▶ ① 각기 다른 '안전 허용치'\n이유: 발전기 냉각수 ≠ 마시는 물 → 그래서(This is why) 용도에 따라 '다른' 허용치\n오답 ▶ ② 같은 허용치(one size fits all — 반대) ③ 가격 아님 ④ 더 엄격한 식수 규칙만이 아님 ⑤ 허용치가 없다는 것도 아님\n포인트 ▶ This is why ~ = 앞 예시의 결론")]
PICK1 = [PK(p, 'When we say', 'looks like', 'tastes like', "정답 ▶ looks like (~처럼 보이다)\n오답 ▶ tastes like (~ 맛이 나다)\n이유: 깨끗함은 겉으로 물 한 잔처럼 '보이는' 것만이 아님 — 겉모습 대 기준"),
 PK(p, 'Water quality is', 'criteria', 'rumors', "정답 ▶ criteria (기준들)\n오답 ▶ rumors (소문들)\n이유: 수질 = 특정한 '기준들'의 집합(지표)을 따르는 것"),
 PK(p, 'These guidelines', 'exactly', 'roughly', "정답 ▶ exactly (정확히)\n오답 ▶ roughly (대략)\n이유: 지침은 물질이 '정확히' 얼마나 있어도 되는지 알려 줌"),
 PK(p, 'These rules ensure', 'safe', 'dangerous', "정답 ▶ safe (안전한)\n오답 ▶ dangerous (위험한)\n이유: 규칙은 어떤 용도든 물이 '안전하다'고 보장"),
 PK(p, 'We can’t utilize', 'diverse', 'similar', "정답 ▶ diverse (다양한)\n오답 ▶ similar (비슷한)\n이유: 물을 '다양한' 일에 쓰므로 일률적 규칙을 쓸 수 없음"),
 PK(p, 'For instance', 'as clean as', 'cleaner than', "정답 ▶ as clean as\n오답 ▶ cleaner than\n이유: 냉각수는 마시는 물'만큼' 깨끗할 필요가 없음 — 덜 깨끗해도 됨")]
TF = [TF(p, "Clean water simply means water that looks clear.", False, "we don’t just mean that it looks like a glass of water", "정답 ▶ F\n이유: 단지 물 한 잔처럼 보인다는 뜻이 아니에요."),
 TF(p, "Water quality is about meeting a certain set of standards.", True, "following a certain set of criteria", "정답 ▶ T\n이유: 특정 기준들의 집합을 따르는 것이에요.\n어휘 ▶ standards = criteria · benchmarks"),
 TF(p, "Guidelines tell us how much chemical stuff can be in the water.", True, "how much physical, chemical, or biological stuff can be in the water", "정답 ▶ T\n이유: 물리적·화학적·생물학적 물질이 얼마나 있어도 되는지 알려 줘요."),
 TF(p, "The same water rule can be used for every purpose.", False, "We can’t utilize the same “one size fits all” rule", "정답 ▶ F\n이유: 일률적인 규칙은 쓸 수 없어요."),
 TF(p, "Water for cooling a power plant must be cleaner than drinking water.", False, "doesn’t need to be as clean as the water you drink", "정답 ▶ F\n이유: 마시는 물만큼 깨끗할 필요가 없어요."),
 TF(p, "Safety limits vary depending on how the water will be used.", True, "dependent on how it will be utilized", "정답 ▶ T\n이유: 용도에 따라 다른 안전 허용치를 정해요.\n어휘 ▶ vary = be different · depending on = dependent on")]
MC = [MC(p, "글의 내용과 일치하지 <u>않는</u> 것은?", [
 "All water must meet drinking-water standards.", "Water is used for drinking, farming, and industry.", "Benchmarks are used to judge water quality.",
 "Cooling water for a generator can be less clean.", "Different groups set different safety limits."],
 "정답 ▶ All water must meet drinking-water standards.\n이유: the water that cools down ~ generator doesn’t need to be as clean as the water you drink (모든 물이 식수 기준일 필요 없음)\n포인트 ▶ meet standards = 기준을 충족하다",
 [["모든 물은 식수 기준을 충족해야 한다.", "doesn’t need to be as clean as the water you drink", "✗ 용도별"], ["물은 마시기, 농사, 산업에 쓰인다.", "drinking it at home, watering crops on a farm, or running it through a huge industrial boiler", "일치"], ["수질 판단에 지표가 쓰인다.", "criteria, or “benchmarks.”", "일치"], ["발전기 냉각수는 덜 깨끗해도 된다.", "doesn’t need to be as clean", "일치"], ["집단들은 각기 다른 안전 허용치를 정한다.", "groups set different “safety limits”", "일치"]]),
 MC(p, "글의 내용과 <u>일치하는</u> 것은?", ["지침은 물속 물질의 허용량을 정확히 알려 준다.", "깨끗한 물은 겉모습으로 판단한다.", "모든 용도에 같은 규칙을 적용해야 한다.", "발전소 냉각수는 식수보다 더 깨끗해야 한다.", "안전 허용치는 물의 색깔에 따라 정해진다."],
 "정답 ▶ 지침은 물속 물질의 허용량을 정확히 알려 준다.\n이유: These guidelines inform us exactly how much ~ stuff can be in the water.\n오답 ▶ ② 기준을 따름 ③ 일률적 규칙 불가 ④ 덜 깨끗해도 됨 ⑤ 용도에 따라",
 [["", "inform us exactly how much", "일치 ✔"], ["", "we don’t just mean that it looks like", "기준"], ["", "We can’t utilize the same", "불가"], ["", "doesn’t need to be as clean", "덜"], ["", "dependent on how it will be utilized", "용도"]])]
PICK2 = [PK(p, 'When we say', 'that it looks', 'what it looks', "정답 ▶ that\n이유: mean의 목적어 명사절, 뒤가 완전한 절 → 접속사 that"),
 PK(p, 'Water quality is', 'following', 'follow', "정답 ▶ following\n이유: 전치사 about 뒤 동명사"),
 PK(p, 'These guidelines', 'how much', 'how many', "정답 ▶ how much\n이유: stuff(물질)는 셀 수 없는 명사 → how much"),
 PK(p, 'These rules ensure', 'whether', 'if', "정답 ▶ whether\n이유: whether A, B, or C (A이든 B이든 C이든) — 양보 부사절은 if 불가"),
 PK(p, 'For instance', 'cools', 'cool', "정답 ▶ cools\n이유: 관계절 주어 that = the water(단수) → cools"),
 PK(p, 'For instance', 'doesn’t', 'don’t', "정답 ▶ doesn’t\n이유: 주어 the water(단수) — that ~ generator는 관계절")]
VERB = [VB(p, 'These rules ensure', 'drinking', 'drink', "정답 ▶ drinking\n이유: that’s(=that is) 뒤 보어 자리 동명사, watering · running과 병렬"),
 VB(p, 'This is why', 'utilized', 'utilize', "정답 ▶ utilized\n이유: 물이 '활용될' 수동 → will be p.p."),
 VB(p, 'For instance', 'to be', 'be', "정답 ▶ to be\n이유: need + to부정사"),
 VB(p, 'These rules ensure', 'running', 'run', "정답 ▶ running\n이유: drinking, watering, or running — 동명사 병렬")]
VERB = [v for v in VERB if v['v'] != v['a'][0]]
ERR = [ER(p, 'For instance', [('cools', 'cool'), 'doesn’t need', 'as clean as'], 0, 'cools', "틀린 곳 ▶ ① cool → cools\n이유: 관계대명사 that의 선행사 the water(단수)\n나머지 ▶ ② 주어 the water → doesn’t ✔ ③ as + 원급 + as ✔"),
 ER(p, 'These guidelines', ['inform', 'exactly', ('how much', 'how many')], 2, 'how much', "틀린 곳 ▶ ③ how many → how much\n이유: stuff는 셀 수 없는 명사\n나머지 ▶ ① inform + 사람 목적어 ✔ ② 부사 exactly ✔"),
 ER(p, 'This is why', ['This is why', 'set', ('utilized', 'utilizing')], 2, 'utilized', "틀린 곳 ▶ ③ utilizing → utilized\n이유: 물이 '활용되는' 수동 → will be utilized\n나머지 ▶ ① This is why + 결과 ✔ ② 주어 groups(복수) → set ✔")]
SCR = [0, 1, 2, 4, 6]
ORDER = [[0, 1, 2, 3], [3, 4, 5, 6]]
INSERT = [([0, 1, 2, 3], 2, "정답 ▶ ② (These guidelines ~ 문장)\n이유: 수질 = 기준(benchmarks) → 이러한 지침(These guidelines)이 허용량을 알려 줌 → 이러한 규칙이 안전 보장"),
 ([3, 4, 5, 6], 2, "정답 ▶ ② (For instance ~ 문장)\n이유: 다양한 용도라 일률적 규칙 불가 → 예: 발전기 냉각수 → 그래서 용도별 허용치")]
ODD = [([1, 2, "Bottled water has become more popular than tap water in many countries.", 3], 2, "정답 ▶ ③\n이유: 수질 기준이 용도에 따라 다르다는 흐름이에요. 생수의 인기 이야기는 관계없어요.")]
BLANK = [BL(p, 'Water quality is', 'benchmarks', ["colors", "prices", "legends"], "정답 ▶ benchmarks (지표)\n이유: criteria(기준) = '지표' — or는 바꿔 말하기\n오답 ▶ colors · prices · legends"),
 BL(p, 'These guidelines', 'biological', ["political", "musical", "financial"], "정답 ▶ biological (생물학적인)\n이유: 물속 물질의 종류: 물리적, 화학적, '생물학적'\n오답 ▶ political · musical · financial"),
 BL(p, 'We can’t utilize', 'one size fits all', ["better late than never", "first come, first served", "less is more"], "정답 ▶ one size fits all (일률적인)\n이유: 모두에게 '같은' 규칙 — 용도가 다양해서 불가\n오답 ▶ 늦어도 안 하는 것보다 낫다 · 선착순 · 적을수록 좋다")]
GRAM = [{'q': "빈칸에 알맞은 것은?<br><b>The water ______ cools the generator doesn’t need to be clean.</b>", 'opts': ["that", "what", "who", "whose"], 'ex': "정답 ▶ that\n이유: 선행사 The water(사물) + 주격 관계대명사"},
 {'q': "빈칸에 알맞은 것은?<br><b>It is safe ______ that’s drinking it, watering crops, or cooling machines.</b>", 'opts': ["whether", "if", "unless", "because"], 'ex': "정답 ▶ whether\n이유: whether A, B, or C (A이든 B이든 C이든)"},
 {'q': "빈칸에 알맞은 것은?<br><b>It doesn’t need to be as clean ______ the water you drink.</b>", 'opts': ["as", "than", "so", "like"], 'ex': "정답 ▶ as\n이유: as + 원급 + as"},
 {'q': "빈칸에 알맞은 것은?<br><b>Limits differ depending on how the water will ______.</b>", 'opts': ["be utilized", "utilize", "utilizing", "utilized"], 'ex': "정답 ▶ be utilized\n이유: 물이 활용'되는' 수동 → will be p.p."}]
SUMQ = [SUM(p, "Since water is used for many (A) ______ purposes, the standards for clean water are set (B) ______ for each use.", [
 "(A) different – (B) differently", "(A) different – (B) identically", "(A) similar – (B) differently", "(A) secret – (B) randomly", "(A) single – (B) equally"],
 "정답 ▶ (A) different – (B) differently\n(A) we use water for so many diverse things (B) set different “safety limits”\n오답 ▶ identically 동일하게 · equally 똑같이 — one size fits all(불가)",
 ["so many diverse things", "different “safety limits”"])]
