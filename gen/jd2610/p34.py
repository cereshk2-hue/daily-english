from jfw import *
S = PREP['34']['sents'][:]; S[7] = S[7].replace('__________________________________________________', 'without a complete accounting of what’s happening at all other levels'); assert S[7].endswith('levels.')
p = load(34, '34번 · 빈칸', sents=S)
VOCAB = words(34)
B = 'without a complete accounting of what’s happening at all other levels'
EXAM = [EXQ(34, '34. 다음 빈칸에 들어갈 말로 가장 적절한 것은?', p.blank(B), [
 "with enough financial support for quality studies", "even in the absence of acceptance by other scientists", "by tracing how science has developed throughout history",
 "through a detailed examination of higher-level phenomena", "without a complete accounting of what’s happening at all other levels"], 4,
 "정답 ▶ ⑤ 다른 모든 수준에서 일어나고 있는 것에 대한 완전한 설명 없이\n이유: 모든 모델은 어떤 것을 '주어진 것(as a given)'으로 받아들이는 단순화 가정이 필요 → Wallace와 Darwin은 변이·유전의 작동 원리를 몰라도 진화 모델을 제시 → 물리학자도 전자가 '왜' 그 질량·전하를 갖는지 설명하지 않고 측정값을 받아들이고 넘어감 → 핵심: 다른 수준을 완전히 설명하지 않아도 한 수준에서 유용한 모델을 만들 수 있다\n오답 ▶ ① 재정 지원 ② 다른 과학자의 인정 ③ 과학사 추적 ④ 상위 현상의 상세한 조사 — 모두 '단순화 가정'과 무관하거나 반대\n포인트 ▶ take as a given = 기정사실로 받아들이다 = 설명하지 않고 넘어가다", v=False),
 EXQ(34, '다음 글의 요지로 가장 적절한 것은?', p.full(), [
 "모든 모델은 일부 사실을 설명 없이 받아들이는 단순화 가정을 필요로 한다.", "과학 모델은 모든 수준의 원리를 완벽히 설명해야 유용하다.", "Darwin의 진화론은 유전의 원리를 정확히 설명했다.",
 "물리학자들은 전자의 질량이 왜 그런지 밝혀냈다.", "휴대 전화의 발전은 생물의 진화와 똑같다."], 0,
 "정답 ▶ ① 모든 모델은 일부 사실을 설명 없이 받아들이는 단순화 가정을 필요로 한다.\n이유: all models must make simplifying assumptions of this nature + 마지막 문장(핵심)\n오답 ▶ ② 반대 ③ 유전 원리는 거의 몰랐음(little knowledge) ④ 설명하려 하지 않음 ⑤ 휴대 전화는 '관심 대상 시스템'의 예일 뿐"),
 EXQ(34, '다음 빈칸에 들어갈 말로 가장 적절한 것은?', p.blank('simplifying assumptions', ) if False else p.full(p.text().replace('make simplifying assumptions of this nature', 'make <u>　　　　　　　　　　</u> of this nature', 1)), [
 "simplifying assumptions", "detailed experiments", "accurate predictions", "historical records", "costly measurements"], 0,
 "정답 ▶ ① simplifying assumptions (단순화하는 가정)\n이유: 앞 문장 '모델이 그냥 주어진 것으로 받아들여야 하는 것들' = 이러한 성격(of this nature)의 '단순화 가정'. 뒤 Darwin·물리학 예시도 같은 내용\n오답 ▶ ② 상세한 실험 ③ 정확한 예측 ④ 역사 기록 ⑤ 비싼 측정 — '그냥 받아들이기'와 무관")]
PICK1 = [PK(p, 'Indeed, all models', 'simplifying', 'complicating', "정답 ▶ simplifying (단순화하는)\n오답 ▶ complicating (복잡하게 만드는)\n이유: 모든 걸 설명하지 않고 '주어진 것'으로 받아들임 → 단순화"),
 PK(p, 'When Wallace', 'little', 'much', "정답 ▶ little (거의 없는)\n오답 ▶ much (많은)\n이유: 다음 문장 '그냥 어떻게든 일어났다고 받아들였다' → 원리를 '거의 몰랐다'"),
 PK(p, 'They just took', 'somehow', 'precisely', "정답 ▶ somehow (어떻게든)\n오답 ▶ precisely (정확히)\n이유: 원리를 모르고 '어떻게든' 일어났다고만 받아들임"),
 PK(p, 'Even at the finest', 'finest', 'roughest', "정답 ▶ finest (가장 미세한)\n오답 ▶ roughest (가장 대략적인)\n이유: Even(~조차) — '가장 세밀한' 수준인 물리학에서조차 가정이 필요"),
 PK(p, 'In a model of', 'accept', 'question', "정답 ▶ accept (받아들이다)\n오답 ▶ question (의문을 제기하다)\n이유: 설명하려 하지 않고 측정값을 그냥 '받아들이고' 넘어감"),
 PK(p, 'The key point', 'useful', 'useless', "정답 ▶ useful (유용한)\n오답 ▶ useless (쓸모없는)\n이유: 완전한 설명 없이도 '유용한' 모델을 만들 수 있다는 결론")]
TF = [TF(p, "Every model must take some things as a given.", True, "all models must make simplifying assumptions", "정답 ▶ T\n이유: 모든 모델은 단순화 가정을 세워야 해요."),
 TF(p, "Wallace and Darwin fully understood how inheritance worked.", False, "there was little knowledge of how variation generation and inheritance worked", "정답 ▶ F\n이유: 변이 생성과 유전의 작동 방식을 거의 알지 못했어요."),
 TF(p, "Wallace and Darwin presented a verbal model of evolution.", True, "presented their verbal model of biological evolution", "정답 ▶ T\n이유: 생물학적 진화의 언어적 모델을 제시했어요."),
 TF(p, "Simplifying assumptions are unnecessary at the finest level of detail.", False, "Even at the finest level of detail, we need simplifying assumptions", "정답 ▶ F\n이유: 가장 미세한 수준에서조차 필요해요."),
 TF(p, "Physicists try hard to explain why electrons have a certain mass.", False, "physicists don’t attempt to explain why electrons have their particular mass", "정답 ▶ F\n이유: 왜 그런지 설명하려 하지 않아요."),
 TF(p, "Physicists accept the measured values of mass and charge.", True, "they just accept the measured values", "정답 ▶ T\n이유: 측정된 값을 받아들이고 넘어가요.")]
MC = [MC(p, "글의 내용과 일치하지 <u>않는</u> 것은?", [
 "A model is useful only when everything at every level is explained.", "Cell phones can be an example of an evolutionary system.", "Darwin did not know much about how variation was generated.",
 "Physicists take the charge of fundamental particles as a given.", "Physicists move on after accepting measured values."],
 "정답 ▶ A model is useful only when everything at every level is explained.\n이유: we can build useful models at one level of analysis without a complete accounting of what’s happening at all other levels\n포인트 ▶ take as a given = 기정사실로 받아들이다 · move on = 넘어가다",
 [["모델은 모든 수준이 다 설명될 때만 유용하다.", "without a complete accounting", "✗ 반대"], ["휴대 전화는 진화 시스템의 예가 될 수 있다.", "let’s say it’s cell phones", "일치"], ["Darwin은 변이가 어떻게 생기는지 잘 몰랐다.", "there was little knowledge", "일치"], ["물리학자들은 기본 입자의 전하를 주어진 것으로 받아들인다.", "must take as a given the mass and charge of fundamental particles", "일치"], ["물리학자들은 측정값을 받아들인 뒤 넘어간다.", "accept the measured values and move on", "일치"]])]
PICK2 = [PK(p, 'Indeed, all models', 'simplifying', 'simplify', "정답 ▶ simplifying\n이유: 명사 assumptions를 꾸미는 현재분사(단순화하는) — 가정이 '단순화하는' 능동"),
 PK(p, 'When Wallace', 'there was', 'there were', "정답 ▶ was\n이유: There + be + 주어, 주어 little knowledge(셀 수 없음, 단수)"),
 PK(p, 'When Wallace', 'how variation generation and inheritance worked', 'how did variation generation and inheritance work', "정답 ▶ how ~ worked\n이유: 전치사 of 뒤 간접의문문 → 의문사 + 주어 + 동사"),
 PK(p, 'They just took', 'that these things', 'which these things', "정답 ▶ that\n이유: took as a given의 목적어 — 뒤가 완전한 절 → 명사절 접속사 that"),
 PK(p, 'In a model of', 'to explain', 'explaining', "정답 ▶ to explain\n이유: attempt + to부정사 (~하려고 시도하다)"),
 PK(p, 'In a model of', 'measured', 'measuring', "정답 ▶ measured\n이유: 값이 '측정된' 수동 → 과거분사가 values 수식"),
 PK(p, 'The key point', 'without', 'unless', "정답 ▶ without\n이유: 뒤에 명사구(a complete accounting ~) → 전치사 without. unless는 접속사라 절이 와야 해요.")]
VERB = [VB(p, 'No matter how', 'to delineate', 'delineate', "정답 ▶ to delineate\n이유: choose + to부정사"),
 VB(p, 'No matter how', 'emerge', 'emerge', "x"),
 VB(p, 'When Wallace', 'presented', 'present', "정답 ▶ presented\n이유: 과거의 일(When ~) → 과거시제"),
 VB(p, 'In a model of', 'move', 'move', "x"),
 VB(p, 'The key point', 'happening', 'happen', "정답 ▶ happening\n이유: what’s(= what is) + -ing 현재진행")]
VERB = [v for v in VERB if v['v'] != v['a'][0]]
ERR = [ER(p, 'When Wallace', ['presented', ('was', 'were'), 'little'], 1, 'was', "틀린 곳 ▶ ② were → was\n이유: 주어 little knowledge(셀 수 없음) → was\n나머지 ▶ ① 과거시제 ✔ ③ 셀 수 없는 명사 knowledge → little ✔"),
 ER(p, 'In a model of', [('to explain', 'explaining'), 'have', 'measured'], 0, 'to explain', "틀린 곳 ▶ ① explaining → to explain\n이유: attempt + to부정사\n나머지 ▶ ② why + 주어(electrons) + 동사 have(간접의문문) ✔ ③ 측정된 → 과거분사 ✔"),
 ER(p, 'The key point', ['that', 'useful', ('without', 'unless')], 2, 'without', "틀린 곳 ▶ ③ unless → without\n이유: 뒤에 명사구 → 전치사\n나머지 ▶ ① 보어 명사절 that ✔ ② 형용사 ✔")]
SCR = [1, 2, 3, 4, 5, 7]
ORDER = [[0, 1, 2, 3], [4, 5, 6, 7]]
INSERT = [([1, 2, 3, 4], 2, "정답 ▶ ② (They just took ~ 문장)\n이유: 원리를 거의 몰랐다 → They(Wallace와 Darwin)는 그냥 일어났다고 받아들였다 → Even at the finest level(물리학)로 확장"),
 ([4, 5, 6, 7], 1, "정답 ▶ ① (Physicists, for example ~ 문장)\n이유: 가장 미세한 수준에서도 가정이 필요 → for example 물리학자 → In a model of atomic bonds(구체적 설명)")]
ODD = [([1, 2, "Darwin spent five years traveling around the world on a ship called the Beagle.", 3], 2, "정답 ▶ ③\n이유: 모델에 단순화 가정이 필요하다는 흐름에서 Darwin은 예시예요. 비글호 여행 이야기는 관계없어요.")]
BLANK = [BL(p, 'When Wallace', 'inheritance', ["advertising", "transportation", "taxation"], "정답 ▶ inheritance (유전)\n이유: 생물학적 진화 모델 → 변이 생성(variation generation)과 '유전'\n오답 ▶ advertising 광고 · transportation 교통 · taxation 과세"),
 BL(p, 'Physicists, for example', 'fundamental particles', ["ancient fossils", "cell phones", "living cells"], "정답 ▶ fundamental particles (기본 입자)\n이유: 물리학자 + 질량과 전하 → 기본 입자 (뒤에서 electrons)\n오답 ▶ 고대 화석 · 휴대 전화 · 살아 있는 세포"),
 BL(p, 'In a model of', 'measured values', ["guessed stories", "secret codes", "ancient myths"], "정답 ▶ measured values (측정된 값)\n이유: 이유는 설명하지 않고 '측정된 값'을 그대로 받아들임\n오답 ▶ 추측한 이야기 · 비밀 암호 · 고대 신화")]
GRAM = [{'q': "빈칸에 알맞은 것은?<br><b>______ how you choose to delineate the system, some things must be taken as a given.</b>", 'opts': ["No matter", "Whatever", "Although", "Because"], 'ex': "정답 ▶ No matter\n이유: No matter how = However (아무리[어떻게] ~하더라도) + 주어 + 동사"},
 {'q': "빈칸에 알맞은 것은?<br><b>There ______ little knowledge of how inheritance worked.</b>", 'opts': ["was", "were", "be", "being"], 'ex': "정답 ▶ was\n이유: 셀 수 없는 명사 knowledge → 단수"},
 {'q': "빈칸에 알맞은 것은?<br><b>Physicists don’t attempt ______ why electrons have their mass.</b>", 'opts': ["to explain", "explaining", "explain", "explained"], 'ex': "정답 ▶ to explain\n이유: attempt + to부정사"},
 {'q': "빈칸에 알맞은 것은?<br><b>We can build useful models ______ a complete accounting of all other levels.</b>", 'opts': ["without", "unless", "if", "because"], 'ex': "정답 ▶ without\n이유: 명사구 앞 → 전치사"}]
SUMQ = [SUM(p, "Scientific models need to take some facts as (A) ______, so a model can be useful at one level even without fully (B) ______ every other level.", [
 "(A) given – (B) explaining", "(A) given – (B) ignoring", "(A) false – (B) explaining", "(A) unknown – (B) measuring", "(A) secret – (B) changing"],
 "정답 ▶ (A) given – (B) explaining\n(A) take as a given = 주어진 것(기정사실)으로 받아들이다 → given\n(B) 다른 모든 수준을 완전히 '설명하지' 않아도 → explaining\n오답 ▶ ignoring 무시하는 — '무시하지 않아도'가 되어 뜻이 엉킴 · false 거짓으로",
 ["take as a given", "without a complete accounting"])]
