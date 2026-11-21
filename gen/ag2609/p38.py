from jfw import *
R = PREP['38']['sents']; G = PREP['38']['given']; assert R[2].endswith('Theodore M.')
S = [R[0], R[1], R[2] + ' ' + R[3], R[4], R[5], G, R[6]]
p = load(38, '38번 · 문장 삽입', sents=S)
VOCAB = words(38)
EXAM = [EXQ(38, '38. 글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳은?', p.insert_q(5, [1, 2, 3, 4, 6]), SLOT, 4,
 "정답 ▶ ⑤\n이유: 가장 초기 사회에서는 정의가 한 정착지 안에서만 공유되면 되므로 '한 단위 = 특정 신체 부위' 정도로 충분 → 주어진 문장: 하지만(though) 이 공동체들(these communities = settlements)이 커지면서 이 체계(this system = 신체 부위 기준)의 불충분함이 분명해짐 → 무역·조공의 불일치를 상상해 보라(더 큰 일관성이 필요한 갈등의 순간)\n오답 ▶ ①~④ these communities·this system이 가리킬 대상(정착지, 신체 부위 정의)이 아직 나오지 않음\n포인트 ▶ 지시어(these communities, this system) + 역접(though)", v=False),
 EXQ(38, '다음 글의 주제로 가장 적절한 것은?', p.full(), [
 "the growing need for consistent units of measurement", "the history of body parts used as names", "why subjective measures are always wrong",
 "the role of language in trade", "how settlements chose their leaders"], 0,
 "정답 ▶ ① 일관된 측정 단위에 대한 커져 가는 필요성\n이유: 측정 단위의 잠재력을 쓰려면 일관성 필요 → 측정 = 언어 → 신뢰할 만한 정의 필요 → 공동체가 커지며 신체 기준의 한계 → 더 큰 일관성 요구\n오답 ▶ ② 일부 ③ 주관적 측정도 유용한 지식을 담음 ④ 언어는 비유 ⑤ 언급 없음"),
 EXQ(38, '다음 빈칸에 들어갈 말로 가장 적절한 것은?', p.blank('reliable definitions'), [
 "reliable definitions", "beautiful names", "personal feelings", "secret codes", "loud voices"], 0,
 "정답 ▶ ① reliable definitions (신뢰할 만한 정의)\n이유: 측정이 또 다른 언어라면 → 단어처럼 단위도 의사소통하려면 '신뢰할 만한 정의'가 필요\n오답 ▶ ② 아름다운 이름 ③ 개인적 느낌(주관적 측정은 공유가 어려움) ④ 비밀 암호 ⑤ 큰 목소리")]
PICK1 = [PK(p, 'To harness', 'consistency', 'variety', "정답 ▶ consistency (일관성)\n오답 ▶ variety (다양성)\n이유: 글 끝 demands greater consistency in measurement"),
 PK(p, 'Subjective measures', 'difficult', 'easy', "정답 ▶ difficult (어려운)\n오답 ▶ easy (쉬운)\n이유: 개인의 경험에 기반 → 다른 사람과 공유하기 어려움"),
 PK(p, 'The historian of science', 'bridge', 'widen', "정답 ▶ bridge (메우다)\n오답 ▶ widen (넓히다)\n이유: 공유된 규칙으로 문화·지리의 차이를 '메워' 정보 교환을 가능하게 함"),
 PK(p, 'As these communities', 'inadequacies', 'advantages', "정답 ▶ inadequacies (불충분함)\n오답 ▶ advantages (장점)\n이유: though(하지만) + 뒤에 불일치·갈등 → 이 체계의 '한계'가 드러남"),
 PK(p, 'Imagine a disagreement', 'greater', 'less', "정답 ▶ greater (더 큰)\n오답 ▶ less (더 적은)\n이유: 갈등의 순간 → '더 큰' 일관성이 필요")]
TF = [TF(p, "We need some degree of consistency to use units of measurement fully.", True, "we need some degree of consistency", "정답 ▶ T\n이유: 측정 단위의 잠재력을 다 쓰려면 일관성이 필요해요."),
 TF(p, "Subjective measures contain no useful knowledge.", False, "Subjective measures contain useful knowledge", "정답 ▶ F\n이유: 유용한 지식을 담고 있지만 공유하기 어려워요."),
 TF(p, "Porter describes measurement as a ‘technology of distance.’", True, "describes measurement as a ‘technology of distance’", "정답 ▶ T\n이유: Porter는 측정을 '거리의 기술'이라고 묘사해요."),
 TF(p, "In the earliest societies, units of measurement needed very complex definitions.", False, "the definition can be no more complex than knowing that a unit was equal to a certain body part", "정답 ▶ F\n이유: 특정 신체 부위와 같다는 것을 아는 정도면 됐어요."),
 TF(p, "Disagreements over trade demand greater consistency in measurement.", True, "demands greater consistency in measurement", "정답 ▶ T\n이유: 무역·조공의 불일치는 더 큰 일관성을 요구해요.")]
MC = [MC(p, "글의 내용과 일치하지 <u>않는</u> 것은?", [
 "Measurement based on body parts worked well as communities grew.", "Subjective measures are based on an individual’s experience.", "Measurement allows for the exchange of information.",
 "Measurement is compared to a kind of language.", "Early settlements shared definitions only within a small area."],
 "정답 ▶ Measurement based on body parts worked well as communities grew.\n이유: 공동체가 커지면서 이 체계의 불충분함이 분명해졌어요.",
 [["신체 부위를 기준으로 한 측정은 공동체가 커져도 잘 작동했다.", "the inadequacies of this system would become evident", "✗ 반대"], ["주관적 측정은 개인의 경험에 기반한다.", "based as it is on an individual’s experience", "일치"],
  ["측정은 정보 교환을 가능하게 한다.", "allowing for the exchange of information", "일치"], ["측정은 일종의 언어에 비유된다.", "if measurement is another sort of language", "일치"], ["초기 정착지는 좁은 범위에서만 정의를 공유했다.", "shared no more widely than a single settlement", "일치"]])]
PICK2 = [PK(p, 'To harness', 'To harness', 'Harness', "정답 ▶ To harness\n이유: 목적의 to부정사(~하기 위해) — Harness로 시작하면 명령문이 되어 뒤 절과 연결 불가"),
 PK(p, 'Subjective measures', 'to share', 'sharing', "정답 ▶ to share\n이유: difficult + to부정사(~하기 어려운)"),
 PK(p, 'The historian of science', 'allowing', 'allowed', "정답 ▶ allowing\n이유: 도구가 정보 교환을 '가능하게 하는'(능동) 분사구문"),
 PK(p, 'Following this logic', 'to communicate', 'communicating', "정답 ▶ to communicate\n이유: in order to + 동사원형(~하기 위해)"),
 PK(p, 'In the earliest societies', 'meaning', 'meant', "정답 ▶ meaning\n이유: 앞 절 전체를 받는 분사구문(이는 ~을 의미한다)"),
 PK(p, 'Imagine a disagreement', 'demands', 'demand', "정답 ▶ demands\n이유: 선행사 a moment of conflict(단수)")]
VERB = [VB(p, 'As these communities', 'grew', 'grow', "정답 ▶ grew\n이유: 과거 사실(As + 과거) — grow의 과거형"),
 VB(p, 'In the earliest societies', 'shared', 'share', "정답 ▶ shared\n이유: 정의가 '공유되는' → need to be p.p."),
 VB(p, 'The historian of science', 'uses', 'use', "정답 ▶ uses\n이유: 선행사 a tool(단수) → 3인칭 단수")]
ERR = [ER(p, 'Subjective measures', ['contain', ('to share', 'sharing'), 'based'], 1, 'to share', "틀린 곳 ▶ ② sharing → to share\n이유: difficult + to부정사\n나머지 ▶ ① 주어 Subjective measures(복수) ✔ ③ based as it is on ~ (~에 기반하므로) ✔"),
 ER(p, 'Imagine a disagreement', ['Imagine', 'it is', ('demands', 'demand')], 2, 'demands', "틀린 곳 ▶ ③ demand → demands\n이유: 선행사 a moment of conflict(단수)에 수 일치\n나머지 ▶ ① 명령문 ✔ ② it = a disagreement ✔")]
SCR = [0, 1, 3, 5]
ORDER = [[0, 1, 2, 3], [3, 4, 5, 6]]
INSERT = [([3, 4, 5, 6], 2, "정답 ▶ ③ (As these communities grew ~)\n이유: 초기 사회에서는 한 정착지 안에서만 공유하면 됨(신체 부위 정의) → 하지만 공동체가 커지자 이 체계의 한계가 드러남 → 무역·조공의 불일치. these communities = 앞 문장의 settlements")]
ODD = [([0, 1, "Many people today measure their steps with smartwatches.", 2], 2, "정답 ▶ ③\n이유: 측정 단위에 일관성이 필요한 이유를 설명하는 흐름이에요. 스마트워치 걸음 수 이야기는 관계없어요.")]
BLANK = [BL(p, 'In the earliest societies', 'a certain body part', ["a famous king", "a large building", "a written law"], "정답 ▶ a certain body part (특정 신체 부위)\n이유: 한 정착지 안에서만 공유 → 단순한 정의로 충분 → 몸의 일부를 기준\n오답 ▶ 유명한 왕 · 큰 건물 · 성문법"),
 BL(p, 'Imagine a disagreement', 'trade or tribute', ["music or art", "sports or games", "weather or seasons"], "정답 ▶ trade or tribute (무역이나 조공)\n이유: 측정의 일관성이 중요한 갈등 → 물건의 양을 재는 무역·조공\n오답 ▶ 음악이나 예술 · 운동이나 게임 · 날씨나 계절")]
GRAM = [{'q': "빈칸에 알맞은 것은?<br><b>Subjective measures can be difficult ______.</b>", 'opts': ["to share", "sharing", "share", "shared"], 'ex': "정답 ▶ to share\n이유: difficult + to부정사"},
 {'q': "빈칸에 알맞은 것은?<br><b>Units need reliable definitions in order ______.</b>", 'opts': ["to communicate", "communicate", "communicating", "communicated"], 'ex': "정답 ▶ to communicate\n이유: in order to + 동사원형"},
 {'q': "빈칸에 알맞은 것은?<br><b>It is a moment of conflict that ______ greater consistency.</b>", 'opts': ["demands", "demand", "demanding", "to demand"], 'ex': "정답 ▶ demands\n이유: 선행사 단수"}]
SUMQ = [SUM(p, "Simple definitions based on body parts worked in small settlements, but as communities grew, measurement needed greater (A) ______ to avoid (B) ______ over trade.", [
 "(A) consistency – (B) conflicts", "(A) consistency – (B) profits", "(A) variety – (B) conflicts", "(A) beauty – (B) travel", "(A) speed – (B) taxes"],
 "정답 ▶ (A) consistency – (B) conflicts\n(A) demands greater consistency in measurement → consistency\n(B) a disagreement over trade ~ a moment of conflict → conflicts\n오답 ▶ profits 이익 · variety 다양성(반대) · beauty 아름다움 · speed 속도",
 ["demands greater consistency in measurement", "a moment of conflict"])]
