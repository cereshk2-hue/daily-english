from jfw import *
S = PREP['26']['sents'][:]; assert S[3].endswith('U.S.'); S[3] = S[3] + ' ' + S[4]; del S[4]
p = load(26, '26번 · 내용 일치', sents=S)
VOCAB = words(26)
EXAM = [EXQ(26, '26. Jacques Piccard에 관한 다음 글의 내용과 일치하지 않는 것은?', p.full(), [
 "과학자 집안에서 태어났다.", "University of Geneva에서 경제학을 가르쳤다.", "단독으로 10,916미터를 하강하면서 잠수 기록을 세웠다.",
 "1970년대에는 환경을 보호하는 것에 집중했다.", "바다와 호수를 연구하기 위해 스위스에 단체를 설립했다."], 2,
 "정답 ▶ ③ 단독으로 10,916미터를 하강하면서 잠수 기록을 세웠다.\n이유: together with U.S. Naval Officer Don Walsh — 미 해군 장교와 '함께' 세운 기록\n오답 ▶ ① a family of scientists ✔ ② taught economics at the University of Geneva ✔ ④ In the 1970s, Jacques focused on protecting the environment ✔ ⑤ founded an organization in Switzerland to study oceans and lakes ✔\n포인트 ▶ '단독으로 / 함께', 숫자·연도는 꼭 원문과 대조", v=False),
 EXQ(26, 'Jacques Piccard에 관한 다음 글의 내용과 일치하는 것은?', p.full(), [
 "6,000미터 도달 후 교직을 떠날 마음이 생겼다.", "스위스에서 태어나 벨기에의 대학을 졸업했다.", "아버지와 함께 우주선을 개발했다.",
 "1960년대에 해양 오염을 목격하고 단체를 설립했다.", "2008년에 마지막 심해 잠수 기록을 세웠다."], 0,
 "정답 ▶ ① 6,000미터 도달 후 교직을 떠날 마음이 생겼다.\n이유: When their machines successfully reached a depth of 6,000 meters, Jacques was inspired to leave his teaching career\n오답 ▶ ② 벨기에에서 태어나 스위스 대학 졸업(거꾸로) ③ 심해 탐사 기계(bathyscaphe) ④ 1970년대 ⑤ 2008년은 사망한 해\n포인트 ▶ be inspired to V = ~할 마음이 생기다"),
 EXQ(26, '다음 빈칸에 들어갈 말로 가장 적절한 것은?', p.blank('protecting the environment'), [
 "protecting the environment", "building faster submarines", "teaching economics again", "exploring the skies", "selling bathyscaphes"], 0,
 "정답 ▶ ① 환경을 보호하는 것\n이유: 심해 잠수 중 해양 '오염'을 목격한 후 → 환경 보호에 집중 → 바다·호수 연구 단체 설립\n오답 ▶ ② 더 빠른 잠수함 ③ 다시 경제학 ④ 하늘 탐험 ⑤ 판매 — 오염 목격과 연결 안 됨\n포인트 ▶ after seeing the ocean pollution이 원인")]
PICK1 = [PK(p, 'Jacques Piccard was born', 'famous', 'unknown', "정답 ▶ famous (유명한)\n오답 ▶ unknown (알려지지 않은)\n이유: 해양과 하늘 탐험으로 '유명한' 과학자 집안"),
 PK(p, 'After graduating', 'develop', 'destroy', "정답 ▶ develop (개발하다)\n오답 ▶ destroy (파괴하다)\n이유: 아버지가 심해 탐사 기계를 '개발하는' 것을 도움"),
 PK(p, 'When their machines', 'successfully', 'barely', "정답 ▶ successfully (성공적으로)\n오답 ▶ barely (간신히, 거의 ~않다)\n이유: 6,000미터 도달 '성공' → 교직을 떠날 마음이 생김"),
 PK(p, 'In 1960', 'descending', 'climbing', "정답 ▶ descending (하강하며)\n오답 ▶ climbing (올라가며)\n이유: 잠수 기록 → 10,916미터를 '내려감'"),
 PK(p, 'In the 1970s', 'pollution', 'beauty', "정답 ▶ pollution (오염)\n오답 ▶ beauty (아름다움)\n이유: 환경 보호에 집중하게 된 계기 → 해양 '오염'"),
 PK(p, 'He died on', 'legacy', 'debt', "정답 ▶ legacy (유산)\n오답 ▶ debt (빚)\n이유: 사망했지만 그의 '유산'이 동료들에게 영감으로 남아 있음")]
TF = [TF(p, "Piccard was born in Belgium.", True, "in Belgium", "정답 ▶ T\n이유: 1922년 벨기에에서 태어났어요."),
 TF(p, "Piccard taught physics at the University of Geneva.", False, "he taught economics at the University of Geneva", "정답 ▶ F\n이유: 물리학이 아니라 경제학(economics)을 가르쳤어요."),
 TF(p, "Piccard helped his father develop deep-sea exploration machines.", True, "while helping his father develop bathyscaphes", "정답 ▶ T\n이유: 아버지가 배시스케이프를 개발하는 것을 도왔어요."),
 TF(p, "Piccard and Don Walsh descended 10,916 meters in 1960.", True, "descending 10,916 meters", "정답 ▶ T\n이유: 1960년, 함께 10,916미터를 하강했어요."),
 TF(p, "Piccard became interested in the environment before his deep-sea dives.", False, "after seeing the ocean pollution during his deep-sea dives", "정답 ▶ F\n이유: 심해 잠수 중 오염을 본 '후에' 환경 보호에 집중했어요."),
 TF(p, "Piccard died in 2008.", True, "He died on November 1, 2008", "정답 ▶ T\n이유: 2008년 11월 1일에 사망했어요.")]
MC = [MC(p, "글의 내용과 일치하지 <u>않는</u> 것은?", [
 "Piccard set the diving record all by himself.", "Piccard graduated from a university in Switzerland.", "Piccard’s machines reached a depth of 6,000 meters.",
 "Piccard founded an organization to study oceans and lakes.", "Piccard is still an inspiration to ocean explorers."],
 "정답 ▶ Piccard set the diving record all by himself.\n이유: together with U.S. Naval Officer Don Walsh\n포인트 ▶ all by himself = 혼자서 ↔ together with",
 [["Piccard는 혼자 잠수 기록을 세웠다.", "together with U.S. Naval Officer Don Walsh", "✗ 함께"], ["Piccard는 스위스의 대학을 졸업했다.", "After graduating university in Switzerland", "일치"], ["Piccard의 기계는 6,000미터 깊이에 도달했다.", "reached a depth of 6,000 meters", "일치"], ["Piccard는 바다와 호수를 연구하는 단체를 세웠다.", "founded an organization in Switzerland to study oceans and lakes", "일치"], ["Piccard는 여전히 해양 탐험가들에게 영감이다.", "remains an inspiration", "일치"]]),
 MC(p, "글의 내용과 <u>일치하는</u> 것은?", ["Piccard는 수중 연구에 집중하려고 교직을 떠났다.", "Piccard는 하늘 탐험으로만 유명한 집안 출신이다.", "Piccard는 1960년에 처음으로 6,000미터에 도달했다.", "Piccard는 미국에 단체를 설립했다.", "Piccard의 유산은 오늘날 잊혔다."],
 "정답 ▶ Piccard는 수중 연구에 집중하려고 교직을 떠났다.\n이유: to leave his teaching career to focus on improving bathyscaphes for underwater research\n오답 ▶ ② 바다와 하늘 '모두' ③ 1960년은 10,916미터 기록 ④ 스위스 ⑤ 영감으로 남아 있음",
 [["", "to focus on improving bathyscaphes for underwater research", "일치 ✔"], ["", "both the oceans and the skies", "모두"], ["", "set a diving record", "10,916m"], ["", "an organization in Switzerland", "스위스"], ["", "remains an inspiration", "남아 있음"]])]
PICK2 = [PK(p, 'Jacques Piccard was born', 'was born', 'born', "정답 ▶ was born\n이유: '태어나다'는 수동형 be born"),
 PK(p, 'Jacques Piccard was born', 'exploring', 'explore', "정답 ▶ exploring\n이유: 전치사 for 뒤 동명사 (famous for -ing)"),
 PK(p, 'After graduating', 'graduating', 'graduated', "정답 ▶ graduating\n이유: 전치사 After 뒤 동명사"),
 PK(p, 'When their machines', 'to leave', 'leaving', "정답 ▶ to leave\n이유: be inspired + to부정사 (~할 마음이 생기다)"),
 PK(p, 'In the 1970s', 'protecting', 'protect', "정답 ▶ protecting\n이유: 전치사 on 뒤 동명사 (focus on -ing)"),
 PK(p, 'He even founded', 'founded', 'found', "정답 ▶ founded\n이유: found(설립하다)-founded-founded, 과거 이야기 → founded (find의 과거 found와 구별)")]
VERB = [VB(p, 'After graduating', 'taught', 'teach', "정답 ▶ taught\n이유: 과거 이야기, teach-taught-taught"),
 VB(p, 'After graduating', 'helping', 'help', "정답 ▶ helping\n이유: while 뒤 분사구문(주어 he 생략) — 돕는 능동"),
 VB(p, 'When their machines', 'improving', 'improve', "정답 ▶ improving\n이유: 전치사 on 뒤 동명사"),
 VB(p, 'He died on', 'remains', 'remain', "정답 ▶ remains\n이유: 주어 his legacy(단수), 지금도 남아 있음 → 현재시제")]
VERB = [v for v in VERB if v['v'] != v['a'][0]]
ERR = [ER(p, 'After graduating', ['After', ('taught', 'teached'), 'helping'], 1, 'taught', "틀린 곳 ▶ ② teached → taught\n이유: teach는 불규칙 동사 teach-taught-taught\n나머지 ▶ ① 전치사 After + 동명사 ✔ ③ while + 분사구문 ✔"),
 ER(p, 'When their machines', ['successfully', ('was inspired', 'inspired'), 'to focus'], 1, 'was inspired', "틀린 곳 ▶ ② inspired → was inspired\n이유: Jacques가 (성공에) '자극받은' 수동 → be inspired to V\n나머지 ▶ ① 부사 successfully ✔ ③ 목적의 to부정사 ✔"),
 ER(p, 'He died on', ['died', ('remains', 'remain'), 'fellow'], 1, 'remains', "틀린 곳 ▶ ② remain → remains\n이유: 주어 his legacy(단수) → remains\n나머지 ▶ ① 과거 사실 died ✔ ③ 형용사 fellow(동료의) ✔")]
SCR = [0, 1, 2, 3, 6]
ORDER = [[0, 1, 2, 3], [3, 4, 5, 6]]
INSERT = [([3, 4, 5, 6], 2, "정답 ▶ ② (He even founded ~ 문장)\n이유: 1970년대 환경 보호에 집중 → 심지어(even) 단체 설립 → 사망 후 유산"),
 ([1, 2, 3, 4], 2, "정답 ▶ ② (In 1960 ~ 문장)\n이유: 6,000미터 성공 후 교직을 떠나 심해 연구에 집중 → 1960년 10,916미터 기록 → 1970년대 환경 — 연도 순서")]
ODD = [([2, 3, "Belgium is famous for its chocolate and waffles.", 4], 2, "정답 ▶ ③\n이유: Jacques Piccard의 생애(연도 순)가 흐름이에요. 벨기에의 초콜릿 이야기는 관계없어요.")]
BLANK = [BL(p, 'After graduating', 'economics', ["biology", "music", "history"], "정답 ▶ economics (경제학)\n이유: University of Geneva에서 '경제학'을 가르침 — 원문항 ②번\n오답 ▶ biology · music · history"),
 BL(p, 'In 1960', 'record', ["mistake", "promise", "machine"], "정답 ▶ record (기록)\n이유: set a record = 기록을 세우다\n오답 ▶ mistake · promise · machine"),
 BL(p, 'He even founded', 'organization', ["restaurant", "museum", "factory"], "정답 ▶ organization (단체)\n이유: 바다와 호수를 '연구하기 위한' 단체\n오답 ▶ restaurant · museum · factory")]
GRAM = [{'q': "빈칸에 알맞은 것은?<br><b>He was inspired ______ his teaching career.</b>", 'opts': ["to leave", "leaving", "leave", "left"], 'ex': "정답 ▶ to leave\n이유: be inspired + to부정사"},
 {'q': "빈칸에 알맞은 것은?<br><b>He ______ an organization to study oceans and lakes in Switzerland.</b>", 'opts': ["founded", "found", "finded", "founds"], 'ex': "정답 ▶ founded\n이유: found(설립하다)의 과거형 founded"},
 {'q': "빈칸에 알맞은 것은?<br><b>He taught economics ______ helping his father develop bathyscaphes.</b>", 'opts': ["while", "during", "for", "because of"], 'ex': "정답 ▶ while\n이유: while + 분사구문(-ing) (during은 전치사라 명사가 옴)"},
 {'q': "빈칸에 알맞은 것은?<br><b>He was born to a family of scientists famous for ______ the oceans.</b>", 'opts': ["exploring", "explore", "explored", "to explore"], 'ex': "정답 ▶ exploring\n이유: 전치사 for + 동명사"}]
SUMQ = []
