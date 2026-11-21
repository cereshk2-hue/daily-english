from jfw import *
R = PREP['37']['sents']; st = lambda x: x.split(') ', 1)[1] if x.startswith('(') else x
S = [R[0], st(R[8]), R[9], R[10], st(R[4]), R[5], R[6], R[7], st(R[1]), R[2], R[3]]
p = load(37, '37번 · 글의 순서', sents=S)
VOCAB = words(37)
EXAM = [EXQ(37, '37. 주어진 글 다음에 이어질 글의 순서로 가장 적절한 것은?', p.order_q([0], {'A': [8, 9, 10], 'B': [4, 5, 6, 7], 'C': [1, 2, 3]}), ORD, 4,
 "정답 ▶ ⑤ (C)-(B)-(A)\n이유: 주어진 글 — 망원경 이전에도 우주를 이해하려 함 → (C) 이집트·바빌로니아·그리스·마야인, 16세기 Copernicus가 맨눈으로 별을 관측 → (B) 그(He = Copernicus)는 지구가 태양 주위를 돈다고 결론, 책 출판 + 17세기 초 망원경 개발 → (A) 망원경(a telescope)을 사용해 Galileo가 목성의 위성 발견, Copernicus 이론 확증\n오답 ▶ (B)의 He는 (C)의 Copernicus / (A)의 Using a telescope는 (B) 끝 '망원경의 개발' 다음\n포인트 ▶ 시간 순서(고대 → 16세기 → 17세기)와 대명사 He", v=False),
 EXQ(37, '다음 글의 제목으로 가장 적절한 것은?', p.full(), [
 "From Naked Eyes to Telescopes: How We Came to Understand the Universe", "Why Galileo Rejected Copernicus’ Theory", "The Ancient Maya: Masters of Mathematics",
 "Telescopes Made the Stars Disappear", "How to Build Your Own Telescope"], 0,
 "정답 ▶ ① 맨눈에서 망원경까지: 우리는 어떻게 우주를 이해하게 되었나\n이유: 고대인의 별 지도 → Copernicus의 맨눈 관측과 지동설 → 망원경 개발 → Galileo의 발견 → 지식의 발전\n오답 ▶ ② Galileo는 확증함(반대) ③ 일부 ④ 언급 없음 ⑤ 만드는 법 없음"),
 EXQ(37, '다음 빈칸에 들어갈 말로 가장 적절한 것은?', p.blank('Earth that traveled around the Sun'), [
 "Earth that traveled around the Sun", "the Sun that traveled around Earth", "the Moon that traveled around Jupiter", "the stars that stood still", "Mars that traveled around Earth"], 0,
 "정답 ▶ ① 태양 주위를 이동한 것은 지구였다\n이유: 당시 받아들여진 관점(태양이 지구 주위를 돈다)이 틀렸다고 결론 → 사실은 반대\n오답 ▶ ② 당시의 틀린 관점 ③④⑤ 언급 없음")]
PICK1 = [PK(p, 'Even before telescopes', 'before', 'after', "정답 ▶ before\n오답 ▶ after\n이유: 이어지는 글 — 망원경 없이(맨눈으로) 관측한 고대인과 Copernicus"),
 PK(p, 'In Europe, a 16th-century', 'revolutionary', 'traditional', "정답 ▶ revolutionary (혁명적인)\n오답 ▶ traditional (전통적인)\n이유: 당시 받아들여진 관점을 뒤집은 생각(지동설)"),
 PK(p, 'Despite widespread objections', 'objections', 'support', "정답 ▶ objections (반대)\n오답 ▶ support (지지)\n이유: Despite(~에도 불구하고) + 그래도 출판 → 반대가 있었음"),
 PK(p, 'He also confirmed', 'correct', 'wrong', "정답 ▶ correct (옳은)\n오답 ▶ wrong (틀린)\n이유: 망원경 관측으로 Copernicus 이론이 '옳았음'을 확증"),
 PK(p, 'Over the centuries', 'advanced', 'limited', "정답 ▶ advanced (발전시켰다)\n오답 ▶ limited (제한했다)\n이유: 과학적 발견과 망원경 정보 → 지식이 발전")]
TF = [TF(p, "People tried to understand the universe even before telescopes existed.", True, "Even before telescopes existed, people looked out into space", "정답 ▶ T\n이유: 망원경 이전에도 우주를 이해하려 했어요."),
 TF(p, "Copernicus used a telescope to take measurements.", False, "Copernicus watched the stars and took measurements by eye", "정답 ▶ F\n이유: 맨눈으로 측정했어요."),
 TF(p, "Copernicus’ theory was accepted by everyone at the time.", False, "Despite widespread objections to his ideas", "정답 ▶ F\n이유: 널리 퍼진 반대가 있었어요."),
 TF(p, "The telescope was developed in the early 17th century.", True, "the development of the telescope in the early 17th century", "정답 ▶ T\n이유: 17세기 초에 망원경이 개발됐어요."),
 TF(p, "Galileo discovered the four largest moons of Jupiter.", True, "discovered the four largest moons of Jupiter", "정답 ▶ T\n이유: 망원경으로 목성의 가장 큰 위성 네 개를 발견했어요.")]
MC = [MC(p, "글의 내용과 일치하지 <u>않는</u> 것은?", [
 "Copernicus was an Italian scientist who used a telescope.", "The Maya were among the first peoples to map the stars.", "Copernicus published his theory in a book.",
 "Later astronomers built on Copernicus’ work.", "Galileo observed craters on Earth’s Moon."],
 "정답 ▶ Copernicus was an Italian scientist who used a telescope.\n이유: Copernicus는 폴란드 수학자이고 맨눈으로 관측했어요. 망원경을 쓴 이탈리아 과학자는 Galileo예요.",
 [["Copernicus는 망원경을 사용한 이탈리아 과학자였다.", "a 16th-century Polish mathematician named Nicolaus Copernicus", "✗ 폴란드, 맨눈"], ["마야인은 별을 지도로 만든 최초의 민족 중 하나였다.", "among the first peoples to map the movements of the stars", "일치"],
  ["Copernicus는 책으로 이론을 출판했다.", "he published his theory in a book", "일치"], ["후대 천문학자들은 Copernicus의 연구를 바탕으로 했다.", "Later astronomers built on Copernicus’ work", "일치"], ["Galileo는 지구의 달에 있는 분화구를 관찰했다.", "observed craters on Earth’s Moon", "일치"]])]
PICK2 = [PK(p, 'In Europe, a 16th-century', 'named', 'naming', "정답 ▶ named\n이유: Copernicus라고 '불리는'(수동) → 과거분사"),
 PK(p, 'He concluded that', 'accepted', 'accepting', "정답 ▶ accepted\n이유: 당시에 '받아들여진'(수동) 관점 → 과거분사"),
 PK(p, 'He concluded that', 'that traveled around the Sun', 'which traveled around the Sun', "정답 ▶ that\n이유: it was ~ that 강조 구문 (지구를 강조)"),
 PK(p, 'Despite widespread objections', 'Despite', 'Although', "정답 ▶ Despite\n이유: 뒤에 명사구(widespread objections) → 전치사 Despite"),
 PK(p, 'Using a telescope', 'Using', 'Used', "정답 ▶ Using\n이유: Galileo가 망원경을 '사용하는'(능동) → 분사구문 Using"),
 PK(p, 'Over the centuries', 'works', 'work', "정답 ▶ works\n이유: 간접의문문 how the universe works — 주어 the universe(단수)")]
VERB = [VB(p, 'Even before telescopes', 'to understand', 'understand', "정답 ▶ to understand\n이유: try + to부정사(~하려고 노력하다)"),
 VB(p, 'The Egyptians, Babylonians', 'to map', 'map', "정답 ▶ to map\n이유: the first + 명사 + to부정사(~한 최초의)"),
 VB(p, 'Technological improvements', 'led', 'lead', "정답 ▶ led\n이유: 과거 사실 → lead의 과거형 led (lead to ~로 이어지다)")]
ERR = [ER(p, 'He concluded that', ['concluded', ('accepted', 'accepting'), 'was wrong'], 1, 'accepted', "틀린 곳 ▶ ② accepting → accepted\n이유: 관점이 '받아들여진'(수동)\n나머지 ▶ ① 과거 동사 ✔ ③ 주어 the view(단수) → was ✔"),
 ER(p, 'Despite widespread objections', [('Despite', 'Although'), 'his ideas', 'published'], 0, 'Despite', "틀린 곳 ▶ ① Although → Despite\n이유: 뒤에 명사구 → 전치사\n나머지 ▶ ② ✔ ③ 과거 동사 ✔")]
SCR = [0, 3, 6, 9]
ORDER = [[0, 1, 2, 3], [4, 5, 6, 7], [7, 8, 9, 10]]
INSERT = [([6, 7, 8, 9], 2, "정답 ▶ ③ (Using a telescope, ~ Galileo ~)\n이유: 17세기 초 망원경 개발 → 그 망원경을 사용해 Galileo가 발견 → 그는 Copernicus 이론을 확증. 망원경이 '생긴 뒤'에야 망원경 사용 가능")]
ODD = [([1, 2, "Many people today enjoy watching the stars while camping.", 3], 2, "정답 ▶ ③\n이유: 망원경 이전 별 관측의 역사(고대인 → Copernicus)를 설명하는 흐름이에요. 오늘날 캠핑 이야기는 관계없어요.")]
BLANK = [BL(p, 'Copernicus watched', 'by eye', ["with a telescope", "in a book", "with a computer"], "정답 ▶ by eye (맨눈으로)\n이유: 망원경은 17세기 초에 개발 → 16세기 Copernicus는 맨눈 관측\n오답 ▶ 망원경으로(아직 없음) · 책으로 · 컴퓨터로"),
 BL(p, 'Technological improvements', 'the telescope', ["the calendar", "the compass", "the printing press"], "정답 ▶ the telescope (망원경)\n이유: 다음 (A) Using a telescope, Galileo ~\n오답 ▶ 달력 · 나침반 · 인쇄기")]
GRAM = [{'q': "빈칸에 알맞은 것은?<br><b>It was in fact Earth ______ traveled around the Sun.</b>", 'opts': ["that", "what", "where", "when"], 'ex': "정답 ▶ that\n이유: It was ~ that 강조"},
 {'q': "빈칸에 알맞은 것은?<br><b>______ widespread objections, he published his theory.</b>", 'opts': ["Despite", "Although", "Because", "Unless"], 'ex': "정답 ▶ Despite\n이유: 명사구 앞 → 전치사"},
 {'q': "빈칸에 알맞은 것은?<br><b>______ a telescope, Galileo discovered four moons of Jupiter.</b>", 'opts': ["Using", "Used", "Use", "To used"], 'ex': "정답 ▶ Using\n이유: 능동 분사구문"}]
SUMQ = [SUM(p, "Long before telescopes, people studied the sky by eye, and Copernicus’ (A) ______ idea was later (B) ______ by Galileo using a telescope.", [
 "(A) revolutionary – (B) confirmed", "(A) revolutionary – (B) rejected", "(A) traditional – (B) confirmed", "(A) simple – (B) forgotten", "(A) false – (B) published"],
 "정답 ▶ (A) revolutionary – (B) confirmed\n(A) put forth a revolutionary idea → revolutionary\n(B) He also confirmed that Copernicus’ theory was correct → confirmed\n오답 ▶ rejected 거부된(반대) · traditional 전통적인(당시 관점을 뒤집음) · forgotten 잊힌 · false 틀린",
 ["put forth a revolutionary idea", "He also confirmed that Copernicus’ theory was correct"])]
