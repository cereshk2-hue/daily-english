from jfw import *
R = PREP['39']['sents']; G = PREP['39']['given']
S = R[:4] + [G] + R[4:]
p = load(39, '39번 · 문장 삽입', sents=S)
VOCAB = words(39)
EXAM = [EXQ(39, '39. 글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳은?', p.insert_q(4, [2, 3, 5, 6, 7]), SLOT, 2,
 "정답 ▶ ③\n이유: 개미는 이 잎을 먹지 않는다(However) → 주어진 문장: 대신에(Instead) 작은 일개미가 잎을 씹어 균류를 키우는 비료로 쓴다 → 개미가 그 균류(the fungus)에 먹이를 주고 균류가 자실체로 피어나 개미가 먹는다\n오답 ▶ ①② 아직 잎을 '먹지 않는다'는 말이 없어 Instead가 받을 내용이 없음 ④⑤ the fungus가 주어진 문장보다 먼저 나오게 됨\n포인트 ▶ Instead(대신에) 앞에는 부정문(don't eat), 뒤 문장의 the fungus는 주어진 문장의 fungus를 받음", v=False),
 EXQ(39, '다음 글의 제목으로 가장 적절한 것은?', p.full(), [
 "Leaf-Cutter Ants: Tiny Farmers Underground", "Why Ants Eat Fresh Leaves", "How Humans Learned Farming from Ants",
 "The Danger of Fungus in Ant Nests", "Ants That Live Alone"], 0,
 "정답 ▶ ① 절엽 개미: 땅속의 작은 농부\n이유: 인간처럼 농부 → 잎으로 균류를 키워 먹음 → 지하 거대 둥지, 농업 문명 완성\n오답 ▶ ② 잎을 먹지 않음(반대) ③ 인간이 개미에게 배웠다는 말 없음 ④ 균류는 먹이 ⑤ 수백만 마리가 한 군락"),
 EXQ(39, '다음 빈칸에 들어갈 말로 가장 적절한 것은?', p.blank('fertilizer'), [
 "fertilizer", "food", "building material", "medicine", "bedding"], 0,
 "정답 ▶ ① fertilizer (비료)\n이유: 잎은 먹지 않음 → 균류를 '키우기 위한(to grow fungus)' 것 → 비료\n오답 ▶ ② 먹이(잎은 먹지 않음) ③ 건축 재료 ④ 약 ⑤ 잠자리")]
PICK1 = [PK(p, 'With millions of members', 'cultivate', 'steal', "정답 ▶ cultivate (경작하다)\n오답 ▶ steal (훔치다)\n이유: 다음 문장 — 인간처럼 농부"),
 PK(p, 'Some of the ants set forth', 'fresh', 'dead', "정답 ▶ fresh (신선한)\n오답 ▶ dead (죽은)\n이유: 신선한 식물을 찾아 큰 조각을 씹어 떼어 냄"),
 PK(p, 'However, the ants', 'don’t eat', 'eat', "정답 ▶ don't eat\n오답 ▶ eat\n이유: However + 다음 Instead(대신 비료로 씀) → 먹지 '않음'"),
 PK(p, 'Instead, smaller worker ants', 'smaller', 'bigger', "정답 ▶ smaller (더 작은)\n오답 ▶ bigger (더 큰)\n이유: 잎을 더 작은 조각으로 씹는 일은 '더 작은' 일개미"),
 PK(p, 'Using this successful farming', 'enormous', 'tiny', "정답 ▶ enormous (거대한)\n오답 ▶ tiny (아주 작은)\n이유: 수백 제곱미터에 달하는 둥지")]
TF = [TF(p, "Leaf-cutter ants grow their own food.", True, "leaf-cutter ants cultivate their own food", "정답 ▶ T\n이유: 스스로 먹이를 경작해요."),
 TF(p, "The ants eat the leaves they carry back to the nest.", False, "the ants don’t eat these leaves", "정답 ▶ F\n이유: 잎을 먹지 않아요."),
 TF(p, "Smaller worker ants use leaf pieces to grow fungus.", True, "use these as fertilizer to grow fungus", "정답 ▶ T\n이유: 잎 조각을 비료로 써서 균류를 키워요."),
 TF(p, "The fungus produces small fruiting bodies that the ants eat.", True, "small fruiting bodies which the ants later eat", "정답 ▶ T\n이유: 균류가 피워 낸 작은 자실체를 개미가 먹어요."),
 TF(p, "Leaf-cutter ants build small nests above the ground.", False, "build enormous nests underground", "정답 ▶ F\n이유: 지하에 거대한 둥지를 지어요.")]
MC = [MC(p, "글의 내용과 일치하지 <u>않는</u> 것은?", [
 "All the ants in a colony go out to find fresh leaves.", "A colony can have millions of members.", "The ants carry large pieces of leaves back to the nest.",
 "The fungus is grown in underground ‘gardens.’", "Some nests span hundreds of square meters."],
 "정답 ▶ All the ants in a colony go out to find fresh leaves.\n이유: Some of the ants — 일부 개미만 신선한 식물을 찾으러 나가요.",
 [["군락의 모든 개미가 신선한 잎을 찾으러 나간다.", "Some of the ants set forth from the nest", "✗ 일부"], ["한 군락에는 수백만 마리가 있을 수 있다.", "With millions of members in a colony", "일치"], ["개미들은 큰 잎 조각을 둥지로 가져온다.", "large pieces that they carry back to the nest", "일치"],
  ["균류는 지하 '정원'에서 길러진다.", "large underground ‘gardens.’", "일치"], ["어떤 둥지는 수백 제곱미터에 달한다.", "spanning hundreds of square meters", "일치"]])]
PICK2 = [PK(p, 'Some of the ants set forth', 'to find', 'finding', "정답 ▶ to find\n이유: 목적의 to부정사(~하기 위해)"),
 PK(p, 'Some of the ants set forth', 'that they carry', 'what they carry', "정답 ▶ that\n이유: 선행사 large pieces가 있음 → 목적격 관계대명사 that (what은 선행사 X)"),
 PK(p, 'Instead, smaller worker ants', 'chew', 'chews', "정답 ▶ chew\n이유: 주어 smaller worker ants(복수) — take, chew, use 병렬"),
 PK(p, 'Instead, smaller worker ants', 'to grow', 'growing', "정답 ▶ to grow\n이유: 목적의 to부정사"),
 PK(p, 'The ants feed the fungus', 'which', 'what', "정답 ▶ which\n이유: 선행사 small fruiting bodies + 목적어 없는 절 → 관계대명사 which"),
 PK(p, 'Using this successful farming', 'Using', 'Used', "정답 ▶ Using\n이유: 개미가 전략을 '사용하는'(능동) 분사구문")]
VERB = [VB(p, 'Using this successful farming', 'spanning', 'span', "정답 ▶ spanning\n이유: something을 꾸미는 현재분사(~에 달하는)"),
 VB(p, 'Just like humans, they have perfected', 'perfected', 'perfect', "정답 ▶ perfected\n이유: have + p.p. 현재완료"),
 VB(p, 'The ants feed the fungus', 'blossoms', 'blossom', "정답 ▶ blossoms\n이유: 주어 the fungus(단수) → 3인칭 단수 현재")]
ERR = [ER(p, 'Some of the ants set forth', ['to find', 'they find', ('that', 'what')], 2, 'that', "틀린 곳 ▶ ③ what → that\n이유: 선행사 large pieces가 있음 → that(which)\n나머지 ▶ ① 목적 to부정사 ✔ ② 주어 they(복수) ✔"),
 ER(p, 'The ants feed the fungus', [('feed', 'feeds'), 'blossoms', 'which'], 0, 'feed', "틀린 곳 ▶ ① feeds → feed\n이유: 주어 The ants(복수)\n나머지 ▶ ② 주어 the fungus(단수) ✔ ③ 관계대명사 which ✔")]
SCR = [0, 1, 3, 7]
ORDER = [[0, 1, 2, 3], [4, 5, 6, 7]]
INSERT = [([2, 3, 4, 5], 2, "정답 ▶ ③ (Instead, smaller worker ants ~)\n이유: 개미는 이 잎을 먹지 않는다 → 대신(Instead) 비료로 균류를 키운다 → 그 균류에 먹이를 주고 자실체를 먹는다")]
ODD = [([2, 3, "Some kinds of ants can lift objects fifty times their own weight.", 4], 2, "정답 ▶ ③\n이유: 개미가 잎으로 균류를 키우는 '농사' 과정을 설명하는 흐름이에요. 개미의 힘 이야기는 관계없어요.")]
BLANK = [BL(p, 'Just like humans, they’re', 'farmers', ["hunters", "builders", "travelers"], "정답 ▶ farmers (농부)\n이유: 앞 문장 cultivate their own food(먹이를 경작함)\n오답 ▶ 사냥꾼 · 건축가 · 여행자"),
 BL(p, 'Just like humans, they have perfected', 'an agricultural civilization', ["a hunting society", "a written language", "a city of glass"], "정답 ▶ an agricultural civilization (농업 문명)\n이유: 성공적인 농업 전략으로 거대한 둥지 → 농업 문명\n오답 ▶ 사냥 사회 · 문자 언어 · 유리 도시")]
GRAM = [{'q': "빈칸에 알맞은 것은?<br><b>They chew off large pieces ______ they carry back to the nest.</b>", 'opts': ["that", "what", "where", "who"], 'ex': "정답 ▶ that\n이유: 선행사 있음 → 목적격 관계대명사"},
 {'q': "빈칸에 알맞은 것은?<br><b>The fungus blossoms into fruiting bodies ______ the ants later eat.</b>", 'opts': ["which", "what", "who", "whose"], 'ex': "정답 ▶ which\n이유: 사물 선행사 + 목적어 없는 절"},
 {'q': "빈칸에 알맞은 것은?<br><b>______ this strategy, the ants build enormous nests.</b>", 'opts': ["Using", "Used", "Use", "Uses"], 'ex': "정답 ▶ Using\n이유: 능동 분사구문"}]
SUMQ = [SUM(p, "Leaf-cutter ants do not eat leaves directly; instead, they use them to (A) ______ fungus, which then becomes their (B) ______.", [
 "(A) grow – (B) food", "(A) grow – (B) home", "(A) destroy – (B) food", "(A) sell – (B) weapon", "(A) hide – (B) enemy"],
 "정답 ▶ (A) grow – (B) food\n(A) use these as fertilizer to grow fungus → grow\n(B) fruiting bodies which the ants later eat → food\n오답 ▶ home 집 · destroy 파괴하다 · sell 팔다 · hide 숨기다",
 ["use these as fertilizer to grow fungus", "which the ants later eat"])]
