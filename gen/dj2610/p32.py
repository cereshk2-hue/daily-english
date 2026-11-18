from jfw import *
S = PREP['32']['sents'][:]; assert S[4].endswith('_.'); S[4] = re.sub(r'_+\.$', 'immune to popular pressure.', S[4])
p = load(32, '32번 · 빈칸 추론', sents=S)
VOCAB = words(32)
EXAM = [EXQ(32, '32. 다음 빈칸에 들어갈 말로 가장 적절한 것은?', p.blank('immune to popular pressure'), [
 "immune to popular pressure", "supportive for the minority", "responsive to social change", "open to political negotiation", "aligned with public expectations"], 0,
 "정답 ▶ ① immune to popular pressure (대중의 압박에 영향을 받지 않는)\n이유: 사람들이 소셜 네트워크로 사법적 결정에 '압박을 가하는' 관행은 해롭다 → 재판은 대중 광장(소셜 네트워크)에서 이루어지면 안 된다 → 법정은 대중의 압박에 '면역된' 방식이어야\n오답 ▶ ② 소수자 지지 — 언급 없음 ③ 사회 변화에 반응 ④ 정치적 협상에 열린 ⑤ 대중의 기대에 맞춘 — 모두 대중·정치의 영향을 받아들이는 쪽이라 반대\n포인트 ▶ put pressure on judicial decisions ↔ immune to popular pressure", v=False),
 EXQ(32, '다음 글의 주제로 가장 적절한 것은?', p.full(), [
 "the danger of public pressure through social networks on court decisions", "the role of schools in passing on cultural traditions", "how social networks help courts make faster decisions",
 "why mass culture strengthens family ties", "the history of the public square in democracy"], 0,
 "정답 ▶ ① 소셜 네트워크를 통한 대중의 압박이 법원 판결에 미치는 위험\n이유: 대중문화가 매개 제도를 약화 → 예: 소셜 네트워크로 사법적 결정에 압박 → 해롭다 → 재판은 법정에서, 대중의 압박 없이\n오답 ▶ ② 학교는 예로만 잠깐 ③ 더 빠른 판결을 돕는다(반대) ④ 유대를 '약화'시킴 ⑤ 광장의 역사 아님\n포인트 ▶ For example 뒤 법정 사례가 글의 핵심"),
 EXQ(32, '다음 빈칸에 들어갈 말로 가장 적절한 것은?', p.blank('harmful'), [
 "harmful", "beneficial", "democratic", "traditional", "necessary"], 0,
 "정답 ▶ ① harmful (해로운)\n이유: 소셜 네트워크로 판결에 압박을 가하는 관행이 습관적 문화가 됨 → 다음 문장 Justice must not be done in the public square → 부정적 평가\n오답 ▶ ② 유익한 ③ 민주적인 ⑤ 필요한 — 필자의 비판과 반대 ④ 전통적인: 오히려 '전통적' 제도는 법정\n포인트 ▶ , which is harmful = 앞 내용 전체에 대한 평가")]
PICK1 = [PK(p, 'If we understand', 'weakening', 'strengthening', "정답 ▶ weakening (약화시키는)\n오답 ▶ strengthening (강화하는)\n이유: 대중문화는 매개 제도를 '약화시킴'(weakens) — 같은 방향"),
 PK(p, 'If we understand', 'diminishing', 'expanding', "정답 ▶ diminishing (축소시키는)\n오답 ▶ expanding (확대하는)\n이유: 제도를 약화시켜 그 역할을 '축소'함"),
 PK(p, 'For example, courts', 'harmonious', 'chaotic', "정답 ▶ harmonious (조화로운)\n오답 ▶ chaotic (혼란스러운)\n이유: 법정은 집단생활의 정상적이고 '조화로운' 기능을 위해 중요"),
 PK(p, 'However, when people', 'pressure', 'support', "정답 ▶ pressure (압박)\n오답 ▶ support (지지)\n이유: 사법적 결정에 '압박'을 가함 → 해롭다"),
 PK(p, 'However, when people', 'habitual', 'rare', "정답 ▶ habitual (습관적인)\n오답 ▶ rare (드문)\n이유: 관행이 대중화되어 '습관적인' 문화 형태가 됨"),
 PK(p, 'In a democratic state', 'appropriate', 'temporary', "정답 ▶ appropriate (적절한)\n오답 ▶ temporary (일시적인)\n이유: 재판하기에 '적절한' 장소는 법정")]
TF = [TF(p, "Mass culture can weaken institutions such as the family or the school.", True, "mass culture weakens the intermediary institutions in society (e.g. the family or the school)", "정답 ▶ T\n이유: 대중문화는 가족·학교 같은 매개 제도를 약화시켜요."),
 TF(p, "Courts are new institutions created by social networks.", False, "courts are traditional social institutions", "정답 ▶ F\n이유: 법정은 '전통적인' 사회 기관이에요."),
 TF(p, "The writer welcomes using social networks to pressure judges.", False, "which is harmful", "정답 ▶ F\n이유: 그 관행은 '해롭다'고 했어요."),
 TF(p, "Today, the public square has turned into social networks.", True, "the public square, which today is converted into a virtual dimension, the social networks", "정답 ▶ T\n이유: 대중 광장은 오늘날 가상의 차원, 소셜 네트워크로 바뀌었어요.\n어휘 ▶ turn into = be converted into"),
 TF(p, "In a democratic state, justice should be made in court.", True, "the appropriate place to judge and make justice is the court", "정답 ▶ T\n이유: 재판하고 정의를 실현할 적절한 곳은 법정이에요."),
 TF(p, "Courts are unimportant for collective life.", False, "important for the normal and harmonious functioning of collective life", "정답 ▶ F\n이유: 집단생활의 정상적이고 조화로운 기능에 중요해요.")]
MC = [MC(p, "글의 내용과 일치하지 <u>않는</u> 것은?", [
 "Justice should be decided by public opinion on social networks.", "Mass culture can weaken cultural ties to tradition.", "Courts help collective life function smoothly.",
 "Pressuring judicial decisions through social networks can become habitual.", "The public square today exists in a virtual form."],
 "정답 ▶ Justice should be decided by public opinion on social networks.\n이유: Justice must not be done in the public square ~ the social networks (소셜 네트워크에서 재판하면 안 됨)\n포인트 ▶ smoothly ≈ harmonious · virtual form = virtual dimension",
 [["정의는 소셜 네트워크의 여론으로 결정되어야 한다.", "Justice must not be done in the public square", "✗ 안 됨"], ["대중문화는 전통에 대한 문화적 유대를 약화시킬 수 있다.", "a weakening factor of the cultural ties", "일치"], ["법정은 집단생활이 원활하게 기능하도록 돕는다.", "harmonious functioning of collective life", "일치"], ["소셜 네트워크로 판결에 압박을 가하는 것은 습관이 될 수 있다.", "becomes a habitual form of culture", "일치"], ["오늘날 대중 광장은 가상의 형태로 존재한다.", "converted into a virtual dimension", "일치"]]),
 MC(p, "글의 내용과 <u>일치하는</u> 것은?", ["법정은 집단생활을 위해 중요한 전통적 기관이다.", "대중문화는 가족의 역할을 강화한다.", "소셜 네트워크를 통한 압박은 정의 실현에 도움이 된다.", "대중 광장은 오늘날 사라지지 않고 그대로 남아 있다.", "필자는 재판을 소셜 네트워크로 옮겨야 한다고 주장한다."],
 "정답 ▶ 법정은 집단생활을 위해 중요한 전통적 기관이다.\n이유: courts are traditional social institutions and important for ~ collective life\n오답 ▶ ② 약화 ③ 해롭다 ④ 가상 차원으로 전환 ⑤ 법정에서",
 [["", "courts are traditional social institutions", "일치 ✔"], ["", "diminishing their role", "축소"], ["", "which is harmful", "해로움"], ["", "converted into a virtual dimension", "전환"], ["", "the appropriate place to judge and make justice is the court", "법정"]])]
PICK2 = [PK(p, 'If we understand', 'that unite', 'what unite', "정답 ▶ that\n이유: 선행사 the cultural ties 있음 → 주격 관계대명사 that (what은 선행사 포함)"),
 PK(p, 'If we understand', 'diminishing', 'diminished', "정답 ▶ diminishing\n이유: 분사구문, 대중문화가 역할을 '축소시키는' 능동"),
 PK(p, 'However, when people', 'to put', 'putting', "정답 ▶ to put\n이유: 목적의 to부정사 (압박을 가하기 위해)"),
 PK(p, 'However, when people', 'is popularized', 'popularizes', "정답 ▶ is popularized\n이유: 관행이 '대중화되는' 수동"),
 PK(p, 'Justice must not', 'be done', 'do', "정답 ▶ be done\n이유: 재판이 '집행되는' 수동 → 조동사 + be p.p."),
 PK(p, 'Justice must not', 'which today', 'what today', "정답 ▶ which\n이유: 콤마 뒤 계속적 용법, 선행사 the public square → which")]
VERB = [VB(p, 'If we understand', 'weakens', 'weaken', "정답 ▶ weakens\n이유: 주절 주어 mass culture(단수), 현재시제"),
 VB(p, 'However, when people', 'becomes', 'become', "정답 ▶ becomes\n이유: is popularized and becomes — 주어 this practice(단수) 동사 병렬"),
 VB(p, 'Justice must not', 'converted', 'convert', "정답 ▶ converted\n이유: 광장이 '전환되는' 수동 → is converted"),
 VB(p, 'In a democratic state', 'to judge', 'judge', "정답 ▶ to judge\n이유: the appropriate place를 꾸미는 형용사적 to부정사 (재판할 장소)")]
VERB = [v for v in VERB if v['v'] != v['a'][0]]
ERR = [ER(p, 'However, when people', ['to put', ('is popularized', 'popularizes'), 'which'], 1, 'is popularized', "틀린 곳 ▶ ② popularizes → is popularized\n이유: 이 관행이 '대중화되는' 수동 (popularize는 타동사인데 목적어도 없음)\n나머지 ▶ ① 목적의 to부정사 ✔ ③ 앞 절을 받는 계속적 용법 which ✔"),
 ER(p, 'Justice must not', [('be done', 'do'), 'which', 'converted'], 0, 'be done', "틀린 곳 ▶ ① do → be done\n이유: 주어 Justice(재판)가 '집행되는' 수동 → must not be done\n나머지 ▶ ② 계속적 용법 which ✔ ③ is converted 수동 ✔"),
 ER(p, 'If we understand', [('that', 'what'), 'weakens', 'diminishing'], 0, 'that', "틀린 곳 ▶ ① what → that\n이유: 선행사 the cultural ties가 있으므로 관계대명사 that (what은 선행사를 포함)\n나머지 ▶ ② 주어 mass culture → weakens ✔ ③ 능동 분사구문 ✔")]
SCR = [1, 2, 3, 4]
ORDER = [[0, 1, 2, 3], [1, 2, 3, 4]]
INSERT = [([0, 1, 2, 3], 1, "정답 ▶ ① (For example, courts ~ 문장)\n이유: 대중문화가 매개 제도를 약화 → 예: 법정은 전통적 기관 → However 소셜 네트워크로 압박"),
 ([1, 2, 3, 4], 2, "정답 ▶ ② (However, when people ~ 문장)\n이유: 법정은 중요한 전통 기관 → However 소셜 네트워크 압박 관행은 해롭다 → 재판은 광장에서 하면 안 됨")]
ODD = [([1, 2, "Many people use social networks to share photos with their friends.", 3], 2, "정답 ▶ ③\n이유: 소셜 네트워크로 판결에 압박을 가하는 관행이 해롭다는 흐름이에요. 친구와 사진 공유 이야기는 관계없어요.")]
BLANK = [BL(p, 'If we understand', 'traditions', ["markets", "screens", "machines"], "정답 ▶ traditions (전통)\n이유: 문화적 유대 → 사람들을 '전통'에 결속시킴 → 법정도 '전통적' 기관\n오답 ▶ markets · screens · machines"),
 BL(p, 'For example, courts', 'collective', ["private", "virtual", "secret"], "정답 ▶ collective (집단적인)\n이유: 법정은 '집단'생활의 조화로운 기능에 중요\n오답 ▶ private 사적인 · virtual 가상의 · secret 비밀의"),
 BL(p, 'Justice must not', 'virtual', ["physical", "ancient", "royal"], "정답 ▶ virtual (가상의)\n이유: 오늘날 광장 = 소셜 네트워크 = '가상의' 차원\n오답 ▶ physical 물리적인(반대) · ancient · royal")]
GRAM = [{'q': "빈칸에 알맞은 것은?<br><b>Justice must not ______ in the public square.</b>", 'opts': ["be done", "do", "done", "doing"], 'ex': "정답 ▶ be done\n이유: 조동사 + be p.p. 수동"},
 {'q': "빈칸에 알맞은 것은?<br><b>People turn to social networks ______ pressure on judges.</b>", 'opts': ["to put", "put", "putting", "puts"], 'ex': "정답 ▶ to put\n이유: 목적의 to부정사"},
 {'q': "빈칸에 알맞은 것은?<br><b>This practice becomes a habit, ______ is harmful.</b>", 'opts': ["which", "that", "what", "it"], 'ex': "정답 ▶ which\n이유: 콤마 뒤 앞 절 전체를 받는 계속적 용법 which (that 불가)"},
 {'q': "빈칸에 알맞은 것은?<br><b>The court is the appropriate place ______ justice.</b>", 'opts': ["to make", "making", "made", "makes"], 'ex': "정답 ▶ to make\n이유: 명사를 꾸미는 형용사적 to부정사"}]
SUMQ = [SUM(p, "Pressuring judicial decisions through social networks is (A) ______, so justice should be made in court, free from (B) ______ pressure.", [
 "(A) harmful – (B) popular", "(A) harmful – (B) legal", "(A) helpful – (B) popular", "(A) traditional – (B) family", "(A) necessary – (B) political"],
 "정답 ▶ (A) harmful – (B) popular\n(A) which is harmful (B) immune to popular pressure\n오답 ▶ helpful · necessary는 필자의 평가와 반대",
 ["which is harmful", "immune to popular pressure"])]
