from jfw import *
R = PREP['41~42']['sents']
S = [re.sub(r'\([a-e]\)', '', x) for x in R[:11]]
S[10] = S[10].split(' 윗글의')[0].replace('weaker', 'stronger'); assert S[10].endswith('rapid pace.')
p = load('41~42', '41~42번 · 장문', sents=S)
VOCAB = words('41~42')
ORIG = re.sub(r'\(([a-e])\)(\w+)', r'(\1)<u>\2</u>', ' '.join(R[:10]) + ' ' + R[10].split(' 윗글의')[0])
EXAM = [EXQ('41~42', '41. 윗글의 제목으로 가장 적절한 것은?', p.full(), [
 "When Slang Meets New Media", "Slang: Respected Throughout History", "Content Creators, Use Standard Language!", "Break the Barrier Between Social Networks", "How Language Evolves in Traditional Media"], 0,
 "정답 ▶ ① When Slang Meets New Media (슬랭이 새로운 미디어를 만날 때)\n이유: 인터넷(소셜 미디어)이 표준어 규칙 제정자의 장벽을 허물어 → 콘텐츠 제작자가 슬랭을 쓰고 퍼뜨림 → 슬랭의 역할이 근본적으로 바뀜\n오답 ▶ ② 역사 내내 존중받음(오히려 규범에 막힘) ③ 표준어를 쓰라(반대) ④ 소셜 네트워크 사이의 장벽은 핵심 아님 ⑤ 전통 매체가 아니라 새 미디어", v=False),
 EXQ('41~42', '42. 밑줄 친 (a)~(e) 중에서 문맥상 낱말의 쓰임이 적절하지 않은 것은?', box(ORIG + '<br><small>' + ' '.join(Q['41~42']['foot']) + '</small>'), ["(a)", "(b)", "(c)", "(d)", "(e)"], 4,
 "정답 ▶ ⑤ (e) weaker → stronger\n이유: 밈이 이제 빠른 속도로 전파된다(memes are now transmitted at rapid pace) → 예전엔 지리적으로 우리를 연결하던 느슨한 사회적 네트워크가 온라인에서는 '더 강하다'\n오답 ▶ (a) 규범이 의사소통 '경로'를 지배 ✔ (b) 그들의 제약 '안에서' 활동해야 했음 ✔ (c) 옛 규칙을 '강제할' 사람이 없음 ✔ (d) 전통 매체보다 '더 다양한' 배경 → 장벽을 넘음 ✔", v=False),
 EXQ('41~42', '다음 빈칸에 들어갈 말로 가장 적절한 것은?', p.blank('Social media completely broke that barrier.'), [
 "Social media completely broke that barrier.", "Traditional media became even stronger.", "Slang slowly disappeared from public life.", "Rule makers gained more power.", "People stopped using the internet."], 0,
 "정답 ▶ ① 소셜 미디어가 그 장벽을 완전히 허물었다.\n이유: 앞 — 대중에게 목소리를 내려면 인쇄·방송 매체의 엄격한 기대에 순응해야 했음(장벽) → 뒤 — 이제 경기장은 평평하고 대중의 접근은 민주화됨\n오답 ▶ ② 전통 매체 강화 ③ 슬랭 소멸 ④ 규칙 제정자 강화 ⑤ 인터넷 사용 중단 — 뒤 내용과 모두 반대")]
PICK1 = [PK(p, 'Since the emergence', 'dominated', 'abandoned', "정답 ▶ dominated (지배했다)\n오답 ▶ abandoned (버렸다)\n이유: 규칙 제정자들이 통제(in charge) → 그들의 규범이 의사소통 경로를 지배"),
 PK(p, 'If you wanted your voice', 'strict', 'loose', "정답 ▶ strict (엄격한)\n오답 ▶ loose (느슨한)\n이유: 그들의 제약 안에서 순응해야 했음 → 엄격한 기대"),
 PK(p, 'The playing field', 'democratized', 'limited', "정답 ▶ democratized (민주화된)\n오답 ▶ limited (제한된)\n이유: 경기장이 평평함(level) → 누구나 접근 가능"),
 PK(p, 'Anybody and everybody', 'nobody’s', 'everybody’s', "정답 ▶ nobody's\n오답 ▶ everybody's\n이유: 누구나 공인이 될 수 있음 → 옛 규칙을 강제할 사람이 '아무도' 남지 않음"),
 PK(p, 'This means that slang', 'beyond', 'within', "정답 ▶ beyond (넘어서)\n오답 ▶ within (안에서)\n이유: 다양한 배경의 제작자들 → 성장을 막던 경제적·사회적 장벽을 '넘어섬'"),
 PK(p, 'The loose social networks', 'stronger', 'weaker', "정답 ▶ stronger (더 강한)\n오답 ▶ weaker (더 약한)\n이유: 밈이 빠르게 전파됨 → 온라인에서 네트워크가 더 강함 — 원문항 42번 (e)")]
TF = [TF(p, "The internet has changed the role of slang in popular culture.", True, "has fundamentally changed because of the internet", "정답 ▶ T\n이유: 인터넷 때문에 근본적으로 바뀌었어요."),
 TF(p, "In the past, people had to follow the rules of print or broadcast media to be heard.", True, "conforming to the strict expectations of either print or broadcast media", "정답 ▶ T\n이유: 대중에게 들리려면 인쇄·방송 매체의 엄격한 기대에 순응해야 했어요."),
 TF(p, "Content creators are not allowed to use slang.", False, "but content creators can", "정답 ▶ F\n이유: TV 진행자와 달리 콘텐츠 제작자는 슬랭을 쓸 수 있어요."),
 TF(p, "Content creators come from fewer backgrounds than people in traditional media.", False, "come from a greater variety of backgrounds", "정답 ▶ F\n이유: 전통 매체 종사자보다 더 다양한 배경 출신이에요."),
 TF(p, "Memes are now transmitted quickly online.", True, "memes are now transmitted at rapid pace", "정답 ▶ T\n이유: 밈은 이제 빠른 속도로 전파돼요.")]
MC = [MC(p, "글의 내용과 일치하지 <u>않는</u> 것은?", [
 "Standard English rule makers welcomed slang in the media.", "Social media broke the barrier of traditional media.", "Anybody can become a public figure on new platforms.",
 "TV presenters might not have been able to use slang.", "Slang can now spread faster than before."],
 "정답 ▶ Standard English rule makers welcomed slang in the media.\n이유: 규칙 제정자들의 '올바른' 영어 규범이 의사소통 경로를 지배했어요 — 슬랭을 환영하지 않았어요.",
 [["표준 영어 규칙 제정자들은 매체에서 슬랭을 환영했다.", "their prescriptive norms about a ‘correct’ version of the English language have dominated", "✗ 반대"], ["소셜 미디어가 전통 매체의 장벽을 허물었다.", "Social media completely broke that barrier", "일치"],
  ["누구나 새 플랫폼에서 공인이 될 수 있다.", "Anybody and everybody can become a public figure", "일치"], ["TV 진행자들은 슬랭을 쓸 수 없었을지도 모른다.", "TV presenters and journalists might not have been able to use slang", "일치"], ["슬랭은 이제 이전보다 빨리 퍼질 수 있다.", "to spread quicker than they could have before", "일치"]])]
PICK2 = [PK(p, 'The role of ‘slang’', 'has fundamentally changed', 'have fundamentally changed', "정답 ▶ has\n이유: 주어 The role(단수) — of ~ culture는 수식어"),
 PK(p, 'If you wanted your voice', 'to be heard', 'to hear', "정답 ▶ to be heard\n이유: want + 목적어 + to부정사, 목소리가 '들리는'(수동)"),
 PK(p, 'If you wanted your voice', 'conforming', 'conformed', "정답 ▶ conforming\n이유: 당신이 '순응하면서'(능동) 분사구문"),
 PK(p, 'Anybody and everybody', 'meaning', 'meant', "정답 ▶ meaning\n이유: 앞 절 전체를 받는 분사구문(이는 ~을 의미한다)"),
 PK(p, 'Content creators also come', 'working', 'worked', "정답 ▶ working\n이유: 사람들이 '일하는'(능동) → people을 꾸미는 현재분사"),
 PK(p, 'This means that slang', 'that once limited', 'what once limited', "정답 ▶ that\n이유: 선행사 the barriers + 주어 없는 절 → 주격 관계대명사")]
VERB = [VB(p, 'TV presenters and journalists', 'been', 'be', "정답 ▶ been\n이유: might have p.p.(~였을지도 모른다)"),
 VB(p, 'We regularly use', 'legitimizes', 'legitimize', "정답 ▶ legitimizes\n이유: 주어 our influence(단수) — both A and B 병렬(legitimizes ~ and gives ~)"),
 VB(p, 'The loose social networks', 'connected', 'connect', "정답 ▶ connected\n이유: previously(이전에) → 과거형")]
ERR = [ER(p, 'We regularly use', ['use', ('legitimizes', 'legitimize'), 'to spread'], 1, 'legitimizes', "틀린 곳 ▶ ② legitimize → legitimizes\n이유: 주어 our influence(단수)\n나머지 ▶ ① 주어 We ✔ ③ a large platform을 꾸미는 to부정사 ✔"),
 ER(p, 'The loose social networks', [('that', 'what'), 'are', 'transmitted'], 0, 'that', "틀린 곳 ▶ ① what → that\n이유: 선행사 The loose social networks가 있음 → 주격 관계대명사 that\n나머지 ▶ ② 주어 networks(복수) ✔ ③ 밈이 '전파되는'(수동) ✔")]
SCR = [0, 3, 6, 9]
ORDER = [[0, 1, 2, 3], [5, 6, 7, 8], [8, 9, 10]]
INSERT = [([1, 2, 3, 4], 2, "정답 ▶ ③ (Social media completely broke that barrier.)\n이유: 예전엔 인쇄·방송 매체의 엄격한 기대에 순응해야 했음(장벽) → 소셜 미디어가 그 장벽(that barrier)을 허묾 → 이제 경기장은 평평"),
 ([6, 7, 8, 9], 2, "정답 ▶ ③ (Content creators also come from ~)\n이유: 우리(제작자)의 영향력이 슬랭을 퍼뜨림 → 또한(also) 제작자들은 더 다양한 배경 출신 → 이것(This)은 슬랭이 경제적·사회적 장벽을 넘을 수 있다는 뜻")]
ODD = [([3, 4, "Many people still prefer reading printed newspapers in the morning.", 5], 2, "정답 ▶ ③\n이유: 소셜 미디어가 장벽을 허물고 누구나 공인이 될 수 있다는 흐름이에요. 아침 종이 신문 선호는 관계없어요.")]
BLANK = [BL(p, 'TV presenters and journalists', 'content creators', ["rule makers", "teachers", "news editors"], "정답 ▶ content creators (콘텐츠 제작자)\n이유: 새로운 플랫폼에서 누구나 공인 → TV 진행자와 달리 슬랭을 쓸 수 있는 사람들\n오답 ▶ 규칙 제정자 · 교사 · 뉴스 편집자"),
 BL(p, 'This means that slang', 'economic and social barriers', ["language learning apps", "television programs", "school textbooks"], "정답 ▶ economic and social barriers (경제적·사회적 장벽)\n이유: 앞 문장 — 더 다양한 배경 출신 → 예전에 슬랭의 성장을 막던 장벽을 넘음\n오답 ▶ 언어 학습 앱 · TV 프로그램 · 학교 교과서")]
GRAM = [{'q': "빈칸에 알맞은 것은?<br><b>If you wanted your voice ______ by the public, you had to follow the rules.</b>", 'opts': ["to be heard", "to hear", "hearing", "heard of"], 'ex': "정답 ▶ to be heard\n이유: want + 목적어 + to부정사(수동)"},
 {'q': "빈칸에 알맞은 것은?<br><b>TV presenters might not have ______ able to use slang.</b>", 'opts': ["been", "be", "being", "was"], 'ex': "정답 ▶ been\n이유: might have p.p."},
 {'q': "빈칸에 알맞은 것은?<br><b>Our influence both ______ these terms and gives them a platform.</b>", 'opts': ["legitimizes", "legitimize", "legitimizing", "to legitimize"], 'ex': "정답 ▶ legitimizes\n이유: 주어 단수, gives와 병렬"}]
SUMQ = [SUM(p, "Social media has (A) ______ the old barriers of Standard English, allowing slang to spread (B) ______ through content creators from diverse backgrounds.", [
 "(A) removed – (B) rapidly", "(A) removed – (B) slowly", "(A) strengthened – (B) rapidly", "(A) created – (B) secretly", "(A) followed – (B) rarely"],
 "정답 ▶ (A) removed – (B) rapidly\n(A) Social media completely broke that barrier → removed\n(B) spread quicker than they could have before / at rapid pace → rapidly\n오답 ▶ slowly 천천히(반대) · strengthened 강화했다(반대) · created 만들었다 · followed 따랐다",
 ["Social media completely broke that barrier", "memes are now transmitted at rapid pace"])]
