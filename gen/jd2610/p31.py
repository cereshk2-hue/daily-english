from jfw import *
S = PREP['31']['sents'][:]; S[3] = S[3].replace('______________', 'scarcity'); assert 'scarcity.' in S[3]
p = load(31, '31번 · 빈칸', sents=S, fix_ko={0: "Star Trek의 세계를 경제학적 렌즈로 바라보는 사람은 거의 없을지도 모르지만, 그렇게 하는 것은 머지않아 우리에게 닥칠지도 모르는 세계를 들여다보는 창을 제공한다."})
VOCAB = words(31)
EXAM = [EXQ(31, '31. 다음 빈칸에 들어갈 말로 가장 적절한 것은?', p.blank('scarcity'), ["bias", "scarcity", "pollution", "diversity", "efficiency"], 1,
 "정답 ▶ ② scarcity (희소성)\n이유: 고전 경제학은 '모두에게 원하는 걸 줄 만큼 충분하지 않다(isn’t usually enough)'는 전제 → 그래서 시장과 가격으로 배분 → However, Star Trek에서는 기술 덕분에 무엇이든 복제·이동 → 풍요(prosperity, highly abundant). 그러니 '희소성'이 거의 없다\n오답 ▶ ① 편견 ③ 오염 ④ 다양성 — 모두 경제학의 전제(부족함)와 연결 안 됨 ⑤ 효율성 — 풍요와 반대 개념이 아님\n포인트 ▶ not enough = scarcity ↔ abundant / prosperity", v=False),
 EXQ(31, '다음 글의 요지로 가장 적절한 것은?', p.full(), [
 "기술 발전은 희소성을 전제로 한 경제를 풍요로운 사회로 바꿀 잠재력이 있다.", "시장과 가격은 자원을 배분하는 유일하고 영원한 방법이다.", "공상 과학 영화는 경제학 연구에 도움이 되지 않는다.",
 "생성형 AI는 일자리를 줄여 사회를 더 가난하게 만든다.", "모든 사람이 같은 직업을 가질 때 사회가 풍요로워진다."], 0,
 "정답 ▶ ① 기술 발전은 희소성을 전제로 한 경제를 풍요로운 사회로 바꿀 잠재력이 있다.\n이유: Star Trek의 기술 → 희소성이 거의 없는 풍요 → Generative AI has the potential to allow ~ our own society to be similarly highly abundant.\n오답 ▶ ② Star Trek에서는 필요 없어짐 ③ 오히려 미래를 보는 창(a window) ④ 반대 ⑤ 직업은 다양함(탐험가·연구원·…)"),
 EXQ(31, '다음 빈칸에 들어갈 말로 가장 적절한 것은?', p.blank('highly abundant'), ["highly abundant", "strictly limited", "deeply divided", "slowly declining", "fairly competitive"], 0,
 "정답 ▶ ① highly abundant (매우 풍요로운)\n이유: similarly(마찬가지로) — Star Trek의 '풍요(prosperity)'처럼 우리 사회도 AI로 풍요로워질 수 있음\n오답 ▶ ② 엄격히 제한된 — 희소성 쪽 ③ 깊이 분열된 ④ 서서히 쇠퇴하는 ⑤ 꽤 경쟁적인\n포인트 ▶ similarly는 앞 내용과 같은 방향")]
PICK1 = [PK(p, 'Few people', 'Few', 'Many', "정답 ▶ Few (거의 없는)\n오답 ▶ Many (많은)\n이유: but(그러나) 그렇게 보면 미래를 보는 창이 된다 → 앞은 '그렇게 보는 사람이 거의 없다'"),
 PK(p, 'All of classical', 'enough', 'little', "정답 ▶ enough (충분한)\n오답 ▶ little (거의 없음)\n이유: there isn’t usually enough of anything — 고전 경제학의 전제는 '부족함'"),
 PK(p, 'Because of that', 'allocate', 'waste', "정답 ▶ allocate (배분하다)\n오답 ▶ waste (낭비하다)\n이유: 부족하니까 가장 큰 이익을 낼 곳에 '배분'"),
 PK(p, 'Technology has', 'reproduce', 'restrict', "정답 ▶ reproduce (복제하다)\n오답 ▶ restrict (제한하다)\n이유: 원하는 어떤 음식이든 '복제' → 부족함이 없음"),
 PK(p, 'All of humanity', 'prosperity', 'poverty', "정답 ▶ prosperity (풍요, 번영)\n오답 ▶ poverty (가난)\n이유: 희소성이 없는 세계 → '풍요'"),
 PK(p, 'Generative AI', 'abundant', 'scarce', "정답 ▶ abundant (풍요로운)\n오답 ▶ scarce (부족한)\n이유: similarly — Star Trek처럼 우리 사회도 '풍요로워질' 잠재력")]
TF = [TF(p, "Many people already study Star Trek from an economic point of view.", False, "Few people may view the Star Trek universe through an economic lens", "정답 ▶ F\n이유: 경제학 렌즈로 보는 사람은 거의 없을지도 모른다고 해요."),
 TF(p, "Classical economics is based on the idea that there is usually not enough of things.", True, "there isn’t usually enough of anything", "정답 ▶ T\n이유: 고전 경제학은 대개 충분하지 않다는 개념에 기초해요."),
 TF(p, "Markets and pricing are used to send resources where they bring the most benefit.", True, "result in the highest benefit", "정답 ▶ T\n이유: 가장 큰 이익을 낳을 곳에 배분하기 위해 시장과 가격을 써요."),
 TF(p, "In Star Trek, people must buy food at high prices.", False, "reproduce any food they want", "정답 ▶ F\n이유: 원하는 어떤 음식이든 복제할 수 있어요."),
 TF(p, "Only a few people in the Star Trek world are educated.", False, "All of humanity in that world has been fully educated", "정답 ▶ F\n이유: 그 세계의 모든 인류가 충분히 교육받았어요."),
 TF(p, "The writer thinks generative AI could make our society more abundant.", True, "has the potential to allow many dimensions of our own society to be similarly highly abundant", "정답 ▶ T\n이유: 생성형 AI가 우리 사회를 풍요롭게 할 잠재력이 있다고 해요.")]
MC = [MC(p, "글의 내용과 일치하지 <u>않는</u> 것은?", [
 "In Star Trek, traveling long distances takes a lot of time.", "Classical economics assumes resources are usually limited.", "Technology lets the Star Trek society copy any food.",
 "Everyone in Star Trek has a job such as explorer or doctor.", "Generative AI could make parts of our society abundant."],
 "정답 ▶ In Star Trek, traveling long distances takes a lot of time.\n이유: transport themselves thousands of miles in the blink of an eye (눈 깜짝할 사이에 수천 마일 이동)\n포인트 ▶ in the blink of an eye = 순식간에 · copy = reproduce · assume ≒ be based on the notion",
 [["Star Trek에서 장거리 이동은 시간이 많이 걸린다.", "in the blink of an eye", "✗ 순식간"], ["고전 경제학은 자원이 대개 한정되어 있다고 가정한다.", "there isn’t usually enough of anything", "일치"], ["기술은 Star Trek 사회가 어떤 음식이든 복제하게 한다.", "reproduce any food they want", "copy = reproduce"], ["Star Trek의 모든 사람은 탐험가나 의사 같은 직업이 있다.", "Everyone is an explorer, researcher, engineer, artist, doctor, or counselor", "일치"], ["생성형 AI는 우리 사회의 일부를 풍요롭게 할 수 있다.", "similarly highly abundant", "일치"]])]
PICK2 = [PK(p, 'Few people', 'doing so provides', 'do so provides', "정답 ▶ doing\n이유: but 뒤 절의 주어 자리 → 동명사 doing so (그렇게 하는 것)"),
 PK(p, 'Few people', 'provides', 'provide', "정답 ▶ provides\n이유: 동명사 주어(doing so)는 단수"),
 PK(p, 'All of classical', 'is based', 'are based', "정답 ▶ is\n이유: All of + 단수명사(economics는 학문명, 단수 취급) → is"),
 PK(p, 'All of classical', 'to give', 'give', "정답 ▶ to give\n이유: enough ~ to부정사 (~할 만큼 충분한)"),
 PK(p, 'Because of that', 'Because of', 'Because', "정답 ▶ Because of\n이유: 뒤에 명사(that)만 옴 → 전치사 Because of. Because는 뒤에 절(주어+동사)"),
 PK(p, 'Technology has', 'to reproduce', 'reproduce', "정답 ▶ to reproduce\n이유: allow + 목적어 + to부정사"),
 PK(p, 'All of humanity', 'been fully educated', 'fully educated', "정답 ▶ been fully educated\n이유: 인류가 '교육받은' 수동 → has been educated")]
VERB = [VB(p, 'Technology has', 'allowed', 'allow', "정답 ▶ allowed\n이유: has + p.p. 현재완료"),
 VB(p, 'Because of that', 'result', 'result', "x"),
 VB(p, 'Generative AI', 'to allow', 'allow', "정답 ▶ to allow\n이유: the potential + to부정사 (~할 잠재력)")]
VERB = [v for v in VERB if v['v'] != v['a'][0]]
ERR = [ER(p, 'Few people', ['view', ('doing', 'do'), 'that'], 1, 'doing', "틀린 곳 ▶ ② do → doing\n이유: 절의 주어 자리 → 동명사\n나머지 ▶ ① 조동사 may + 동사원형 ✔ ③ 선행사 a world + 주어 없는 절 → 주격 관계대명사 that ✔"),
 ER(p, 'Technology has', ['allowed', ('to reproduce', 'reproduce'), 'thousands'], 1, 'to reproduce', "틀린 곳 ▶ ② reproduce → to reproduce\n이유: allow + 목적어 + to부정사\n나머지 ▶ ① 현재완료 ✔ ③ thousands of (수천의) ✔"),
 ER(p, 'Generative AI', ['to allow', 'to be', ('abundant', 'abundantly')], 2, 'abundant', "틀린 곳 ▶ ③ abundantly → abundant\n이유: be동사의 보어 → 형용사 (to be ~ abundant)\n나머지 ▶ ① potential to부정사 ✔ ② allow + 목적어 + to be ✔")]
SCR = [0, 1, 2, 4, 7]
ORDER = [[0, 1, 2, 3], [3, 4, 5, 6, 7]]
INSERT = [([1, 2, 3, 4], 2, "정답 ▶ ② (In Star Trek, however ~ 문장)\n이유: 고전 경제학(부족 → 시장으로 배분) → however, Star Trek엔 희소성이 없다(전환) → 그 이유(기술로 무엇이든 복제)"),
 ([4, 5, 6, 7], 3, "정답 ▶ ③ (Generative AI ~ 문장)\n이유: Star Trek 세계의 풍요 묘사 → 우리 사회(our own society)도 AI로 '마찬가지로(similarly)' 풍요로워질 수 있다는 결론")]
ODD = [([1, 2, "Many economists believe that Star Trek is the most popular science fiction series ever made.", 3], 2, "정답 ▶ ③\n이유: 고전 경제학의 전제(희소성)와 Star Trek의 풍요를 대조하는 흐름이에요. 가장 인기 있는 시리즈라는 이야기는 관계없어요.")]
BLANK = [BL(p, 'Because of that', 'markets and pricing', ["wars and conflicts", "games and sports", "dreams and wishes"], "정답 ▶ markets and pricing (시장과 가격 책정)\n이유: 부족한 자원을 배분하는 경제학의 도구\n오답 ▶ 전쟁과 갈등 · 경기와 스포츠 · 꿈과 소망"),
 BL(p, 'All of humanity', 'educated', ["isolated", "punished", "controlled"], "정답 ▶ educated (교육받은)\n이유: 모두가 풍요에 '참여할 수 있도록' 교육받음 → 모두 탐험가·연구원·의사 등\n오답 ▶ isolated 고립된 · punished 처벌받은 · controlled 통제된"),
 BL(p, 'Technology has', 'in the blink of an eye', ["over many years", "with great difficulty", "on foot"], "정답 ▶ in the blink of an eye (눈 깜짝할 사이에)\n이유: 기술 덕분에 부족함·제약이 없는 세계\n오답 ▶ 여러 해에 걸쳐 · 아주 어렵게 · 걸어서")]
GRAM = [{'q': "빈칸에 알맞은 것은?<br><b>______ people may view Star Trek through an economic lens.</b>", 'opts': ["Few", "Little", "Much", "A little"], 'ex': "정답 ▶ Few\n이유: 셀 수 있는 복수명사(people) → few. little은 셀 수 없는 명사"},
 {'q': "빈칸에 알맞은 것은?<br><b>There isn’t enough of anything ______ everyone everything they want.</b>", 'opts': ["to give", "give", "giving", "given"], 'ex': "정답 ▶ to give\n이유: enough + to부정사"},
 {'q': "빈칸에 알맞은 것은?<br><b>______ that, we use markets and pricing.</b>", 'opts': ["Because of", "Because", "Although", "While"], 'ex': "정답 ▶ Because of\n이유: 뒤에 명사(대명사 that) → 전치사"},
 {'q': "빈칸에 알맞은 것은?<br><b>Technology has allowed that society ______ any food they want.</b>", 'opts': ["to reproduce", "reproduce", "reproducing", "reproduced"], 'ex': "정답 ▶ to reproduce\n이유: allow + 목적어 + to부정사"}]
SUMQ = [SUM(p, "While classical economics starts from the idea that resources are (A) ______, the world of Star Trek shows how technology could create (B) ______.", [
 "(A) limited – (B) abundance", "(A) limited – (B) shortage", "(A) unlimited – (B) abundance", "(A) expensive – (B) conflict", "(A) natural – (B) pollution"],
 "정답 ▶ (A) limited – (B) abundance\n(A) 대개 충분하지 않다 → 한정된(limited)\n(B) 기술이 만든 풍요(prosperity, highly abundant) → abundance\n오답 ▶ shortage 부족(반대) · unlimited 무한한(고전 경제학 전제와 반대)",
 ["there isn’t usually enough of anything", "similarly highly abundant"])]
