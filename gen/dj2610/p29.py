from jfw import *
S = PREP['29']['sents'][:]; assert 'a quarter of them' in S[6]; S[6] = S[6].replace('a quarter of them', 'a quarter of whom')
p = load(29, '29번 · 어법', sents=S)
VOCAB = words(29)
EXAM = [EXQ(29, '29. 다음 글의 밑줄 친 부분 중, 어법상 틀린 것은?', underlined(29, ['in which', 'become', 'is', 'those', 'them']), [
 "①", "②", "③", "④", "⑤"], 4,
 "정답 ▶ ⑤ them → whom\n이유: 콤마 앞뒤로 절이 두 개(Things were ~ / a quarter of ~ failed) — 접속사가 없으므로 대명사 them이 아니라 관계대명사 whom(a quarter of whom = 그들 중 4분의 1)\n오답 ▶ ① 전치사 + 관계대명사 in which(경주 안에서) ✔ ② 부정어구 From only a very small number ~ 도치 → will + 주어 + 동사원형 become ✔ ③ 앞 절 전체를 받는 which → 단수 is ✔ ④ Infant mortality rates(복수)를 받는 those ✔\n포인트 ▶ 콤마로 절 두 개를 이으려면 관계사(수량 표현 + of whom/which)가 필요해요.", v=False),
 EXQ(29, '다음 글의 요지로 가장 적절한 것은?', p.full(), [
 "과거 인류는 자연 상태에 가까워 생존의 초기 관문을 넘기 매우 어려웠다.", "현대 의학의 발전은 영장류의 수명도 늘렸다.", "농업 사회는 수렵 채집 사회보다 훨씬 안전했다.",
 "자연은 생명을 매우 효율적으로 보존한다.", "인구 증가는 19세기 이전에 이미 일어났다."], 0,
 "정답 ▶ ① 과거 인류는 자연 상태에 가까워 생존의 초기 관문을 넘기 매우 어려웠다.\n이유: 초기 허들이 매우 높았다 → 자연은 생명을 극도로 낭비 → 유아 사망률이 유인원과 비슷하거나 더 높았다\n오답 ▶ ② 영장류 수명 연장 없음 ③ 농업 사회도 유인원과 비슷 ④ 낭비한다(wasteful)의 반대 ⑤ 그랬다면 훨씬 일찍 일어났을 것 — 실제로는 일어나지 않음\n포인트 ▶ 가정법 과거완료 Had it been otherwise ~ (사실은 그렇지 않았다)"),
 EXQ(29, '다음 빈칸에 들어갈 말로 가장 적절한 것은?', p.blank('wasteful'), [
 "wasteful", "protective", "careful", "generous", "respectful"], 0,
 "정답 ▶ ① wasteful (낭비하는)\n이유: 무화과 씨앗 중 단 하나만 나무가 됨, 개코원숭이 4분의 1이 한 살 전에 죽음 → 자연은 생명을 '낭비'함\n오답 ▶ ② 보호하는 ③ 신중한 ④ 관대한 ⑤ 존중하는 — 모두 반대\n포인트 ▶ be wasteful of ~ = ~을 낭비하다")]
PICK1 = [PK(p, 'The early hurdles', 'high', 'low', "정답 ▶ high (높은)\n오답 ▶ low (낮은)\n이유: 많은 사람이 처음 몇 개를 넘기 전에 넘어짐 → 초기 허들이 '높았음'"),
 PK(p, 'Demographically', 'close to', 'far from', "정답 ▶ close to (~에 가깝게)\n오답 ▶ far from (~와 거리가 먼)\n이유: 인류가 자연 상태에 '가깝게' 살았음 → 자연처럼 생명이 낭비됨"),
 PK(p, 'Demographically', 'extremely', 'hardly', "정답 ▶ extremely (극도로)\n오답 ▶ hardly (거의 ~않게)\n이유: 씨앗 하나만 나무가 되고, 새끼 4분의 1이 일찍 죽음 → 자연은 생명을 '극도로' 낭비함"),
 PK(p, 'Almost a quarter', 'typical', 'rare', "정답 ▶ typical (전형적인)\n오답 ▶ rare (드문)\n이유: 4분의 1이 한 살 전에 죽는 것은 영장류에게 '전형적'"),
 PK(p, 'Infant mortality rates', 'higher', 'lower', "정답 ▶ higher (더 높은)\n오답 ▶ lower (더 낮은)\n이유: 인간의 유아 사망률이 유인원과 비슷했고 때로는 '더 높았음' — 사정이 나쁜 흐름"),
 PK(p, 'Had it been', 'earlier', 'later', "정답 ▶ earlier (더 일찍)\n오답 ▶ later (더 늦게)\n이유: 사망률이 그렇게 높지 않았다면 → 인구 증가가 '더 일찍' 일어났을 것")]
TF = [TF(p, "The writer compares survival to a race with hurdles.", True, "think of survival as a race in which a hurdle has to be jumped", "정답 ▶ T\n이유: 생존을 매년 허들을 넘는 경주에 비유해요."),
 TF(p, "Nature is very careful not to waste life.", False, "nature is extremely wasteful of life", "정답 ▶ F\n이유: 자연은 생명을 극도로 낭비해요."),
 TF(p, "About a quarter of wild baboons die before their first birthday.", True, "Almost a quarter of baboons born in the wild die before they are a year old", "정답 ▶ T\n이유: 야생 개코원숭이의 거의 4분의 1이 한 살 전에 죽어요."),
 TF(p, "Infant mortality in pre-modern farming societies was much lower than that of apes.", False, "were similar to, and sometimes higher, than those of apes", "정답 ▶ F\n이유: 유인원과 비슷했고 때로는 더 높았어요."),
 TF(p, "Hunter-gatherers had a much easier time surviving.", False, "Things were little better for our hunter-gatherer ancestors", "정답 ▶ F\n이유: 수렵 채집 조상들도 사정이 별로 나을 것이 없었어요.\n포인트 ▶ little better = 거의 나을 게 없는"),
 TF(p, "Human population grew hugely only in recent times.", True, "the huge recent growth in human population", "정답 ▶ T\n이유: 엄청난 인구 증가는 '최근'의 일이에요.")]
MC = [MC(p, "글의 내용과 일치하지 <u>않는</u> 것은?", [
 "Most seeds from figs grow into fig trees.", "Many people once failed to clear the early hurdles of life.", "Death in infancy was common among primates.",
 "A quarter of hunter-gatherers did not reach their first birthday.", "Population growth would have come earlier if survival had been easier."],
 "정답 ▶ Most seeds from figs grow into fig trees.\n이유: From only a very small number of figs will even one of many seeds become a fig tree. (극소수만 나무가 됨)\n포인트 ▶ in infancy = 유아기에 · otherwise = 그렇지 않았다면",
 [["무화과 씨앗 대부분이 무화과나무로 자란다.", "From only a very small number of figs", "✗ 극소수"], ["많은 사람이 한때 삶의 초기 허들을 넘지 못했다.", "many people fell before clearing the first few", "일치"], ["유아기 사망은 영장류에게 흔했다.", "which is fairly typical for primates", "common = typical"], ["수렵 채집인의 4분의 1은 첫 생일에 이르지 못했다.", "failed to reach their first birthday", "일치"], ["생존이 더 쉬웠다면 인구 증가가 더 일찍 왔을 것이다.", "would have occurred much earlier", "일치"]]),
 MC(p, "글의 내용과 <u>일치하는</u> 것은?", ["인류는 오랫동안 자연 상태에 가깝게 살았다.", "개코원숭이는 대부분 한 살 전에 죽는다.", "19세기 이전에도 모든 사람이 자손을 낳을 만큼 오래 살았다.", "초기의 허들은 오늘날보다 낮았다.", "인구 증가는 아주 오래전에 일어났다."],
 "정답 ▶ 인류는 오랫동안 자연 상태에 가깝게 살았다.\n이유: humankind was living close to a state of nature\n오답 ▶ ② 거의 4분의 1 ③ 또 다른 4분의 1은 그러지 못함 ④ 매우 높았음 ⑤ 최근",
 [["", "humankind was living close to a state of nature", "일치 ✔"], ["", "Almost a quarter of baboons", "4분의 1"], ["", "didn’t live long enough to reproduce", "못 함"], ["", "were once very high", "높음"], ["", "the huge recent growth", "최근"]])]
PICK2 = [PK(p, 'You might think', 'in which', 'which', "정답 ▶ in which\n이유: 뒤가 완전한 절(a hurdle has to be jumped) → 전치사 + 관계대명사"),
 PK(p, 'You might think', 'be jumped', 'jump', "정답 ▶ be jumped\n이유: 허들이 '뛰어넘어지는' 수동 → has to be p.p."),
 PK(p, 'The early hurdles', 'clearing', 'clear', "정답 ▶ clearing\n이유: 전치사 before 뒤 동명사"),
 PK(p, 'From only a very', 'become', 'becomes', "정답 ▶ become\n이유: 부정어구 도치 will + 주어 + 동사원형"),
 PK(p, 'Almost a quarter', 'born', 'bearing', "정답 ▶ born\n이유: baboons를 꾸미는 과거분사 — '태어난' 개코원숭이"),
 PK(p, 'Infant mortality rates', 'those', 'that', "정답 ▶ those\n이유: 앞의 복수 명사 Infant mortality rates를 받음 → those")]
VERB = [VB(p, 'Things were little', 'to reach', 'reach', "정답 ▶ to reach\n이유: fail + to부정사 (~하지 못하다)"),
 VB(p, 'Things were little', 'to reproduce', 'reproduce', "정답 ▶ to reproduce\n이유: 형용사/부사 + enough + to부정사 (~할 만큼 충분히)"),
 VB(p, 'Had it been', 'occurred', 'occur', "정답 ▶ occurred\n이유: 가정법 과거완료 주절 would have p.p."),
 VB(p, 'Demographically', 'was living', 'live', "정답 ▶ was living\n이유: 과거의 지속된 상태 — 과거진행형, 주어 humankind(단수)")]
VERB = [v for v in VERB if v['v'] != v['a'][0]]
ERR = [ER(p, 'Things were little', ['better', ('whom', 'them'), 'enough'], 1, 'whom', "틀린 곳 ▶ ② them → whom (원문항 ⑤번)\n이유: 접속사 없이 두 절을 콤마로 이을 수 없음 → a quarter of whom(관계대명사)\n나머지 ▶ ① little + 비교급 better ✔ ③ long enough to V ✔"),
 ER(p, 'Almost a quarter', [('born', 'bore'), 'which', 'typical'], 0, 'born', "틀린 곳 ▶ ① bore → born\n이유: 문장의 동사는 die → baboons를 꾸미는 과거분사 born(태어난)\n나머지 ▶ ② 앞 절을 받는 계속적 용법 which ✔ ③ be동사 보어 형용사 ✔"),
 ER(p, 'Had it been', [('Had it been', 'It had been'), 'would have', 'earlier'], 0, 'Had it been', "틀린 곳 ▶ ① It had been → Had it been\n이유: 가정법 과거완료 If it had been otherwise에서 If 생략 → 도치 Had it been\n나머지 ▶ ② would have p.p. ✔ ③ much + 비교급 ✔")]
SCR = [0, 2, 4, 5, 7]
ORDER = [[0, 1, 2, 3], [4, 5, 6, 7]]
INSERT = [([1, 2, 3, 4], 2, "정답 ▶ ② (From only a very small ~ 문장)\n이유: 자연은 생명을 낭비 → (예) 무화과 씨앗 하나만 나무가 됨 → 개코원숭이"),
 ([4, 5, 6, 7], 3, "정답 ▶ ③ (Things were little better ~ 문장)\n이유: 농업 사회 유아 사망률 높음 → 수렵 채집인도 나을 게 없음 → 그렇지 않았다면 인구 증가가 더 일찍")]
ODD = [([3, 4, "Baboons live in large groups and communicate with many different sounds.", 5], 2, "정답 ▶ ③\n이유: 높은 유아 사망률(생명의 낭비)이 흐름이에요. 개코원숭이의 무리·의사소통 이야기는 관계없어요.")]
BLANK = [BL(p, 'Infant mortality rates', 'mortality', ["birth", "literacy", "employment"], "정답 ▶ mortality (사망률)\n이유: 개코원숭이의 이른 죽음과 비교 → 인간의 유아 '사망'률\n오답 ▶ birth 출생 · literacy 문해 · employment 고용"),
 BL(p, 'Things were little', 'reproduce', ["travel", "vote", "retire"], "정답 ▶ reproduce (번식하다)\n이유: 4분의 1은 '자손을 낳을' 만큼 오래 살지 못함 → 인구가 늘지 못한 이유\n오답 ▶ travel · vote · retire"),
 BL(p, 'Demographically', 'state of nature', ["state of war", "modern city", "golden age"], "정답 ▶ state of nature (자연 상태)\n이유: 뒤에 'nature is extremely wasteful of life' — 자연 상태에 가까웠다\n오답 ▶ 전쟁 상태 · 현대 도시 · 황금기")]
GRAM = [{'q': "빈칸에 알맞은 것은?<br><b>He has three sons, two of ______ are doctors.</b>", 'opts': ["whom", "them", "who", "which"], 'ex': "정답 ▶ whom\n이유: 콤마 + 수량 표현 + of + 관계대명사(사람 whom) — 접속사가 없으니 them 불가"},
 {'q': "빈칸에 알맞은 것은?<br><b>Only from a few seeds ______ a tree grow.</b>", 'opts': ["will", "it will", "does it", "are"], 'ex': "정답 ▶ will\n이유: 부정어구(Only ~) 문두 → 조동사 + 주어 + 동사원형 도치 (will a tree grow)"},
 {'q': "빈칸에 알맞은 것은?<br><b>______ it been otherwise, the population would have grown earlier.</b>", 'opts': ["Had", "If", "Has", "Were"], 'ex': "정답 ▶ Had\n이유: If 생략 가정법 과거완료 도치 Had + 주어 + p.p."},
 {'q': "빈칸에 알맞은 것은?<br><b>Human mortality rates were similar to ______ of apes.</b>", 'opts': ["those", "that", "it", "them"], 'ex': "정답 ▶ those\n이유: 복수 명사 rates를 받는 지시대명사 those"}]
SUMQ = [SUM(p, "For most of history, humans lived close to nature, which is (A) ______ of life, so early death was common and population growth was (B) ______.", [
 "(A) wasteful – (B) delayed", "(A) wasteful – (B) rapid", "(A) protective – (B) delayed", "(A) careful – (B) constant", "(A) fond – (B) early"],
 "정답 ▶ (A) wasteful – (B) delayed\n(A) nature is extremely wasteful of life (B) 그렇지 않았다면 인구 증가가 훨씬 일찍 → 실제로는 '늦어졌음'\n오답 ▶ rapid 빠른 · early 이른: 인구 증가는 최근의 일",
 ["nature is extremely wasteful of life", "would have occurred much earlier"])]
