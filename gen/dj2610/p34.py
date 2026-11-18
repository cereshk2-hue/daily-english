from jfw import *
A34 = 'interconnectedness instantly spreads the impact of small failures'
S = PREP['34']['sents'][:]; assert S[8].endswith('_.'); S[8] = re.sub(r'_+\.$', A34 + '.', S[8])
p = load(34, '34번 · 빈칸 추론', sents=S)
VOCAB = words(34)
EXAM = [EXQ(34, '34. 다음 빈칸에 들어갈 말로 가장 적절한 것은? [3점]', p.blank(A34), [
 "complex issues involving smart systems are oversimplified", "vast amounts of online information destroy social hierarchy", "digitization widens the information gap between institutions",
 A34, "digital networks fall like dominoes due to increasing computing costs"], 3,
 "정답 ▶ ④ 상호 연결성이 작은 실패들의 영향을 즉각적으로 확산시키기 때문에\n이유: 예전엔 기관들이 분리되어 바깥 오류로부터 보호됨 → 더 이상 아님 → 금융 산업이 모두를 연결해 지구 반대편 오류에도 취약 → 이 상호 의존성이 복합적 실패의 온상\n오답 ▶ ① 지나친 단순화 이야기 없음 ② 사회 계층 파괴 없음 ③ 정보 격차 아님 ⑤ 컴퓨팅 비용은 '감소'했음\n포인트 ▶ separate / buffered (과거) ↔ interdependence / bump up against each other (현재)", v=False),
 EXQ(34, '다음 글의 제목으로 가장 적절한 것은?', p.full(), [
 "Connected Systems, Contagious Failures", "How Social Media Made Business Easier", "Why Banks Should Work Alone",
 "Smart Systems That Never Break Down", "The Falling Cost of Computers"], 0,
 "정답 ▶ ① 연결된 시스템, 전염되는 실패\n이유: 상호 연결 → 지구 반대편 오류에 취약 → 상호 의존성은 복합적 실패의 온상\n오답 ▶ ② 쉬워졌다는 이야기 아님 ③ 은행이 혼자 일해야 한다는 주장 없음 ④ 고장이 '무한히 다양' ⑤ 비용 감소는 배경일 뿐\n포인트 ▶ contagious = 전염성의(퍼지는)"),
 EXQ(34, '다음 빈칸에 들어갈 말로 가장 적절한 것은?', p.blank('buffered'), [
 "buffered", "damaged", "connected", "exposed", "controlled"], 0,
 "정답 ▶ ① buffered (보호된)\n이유: 기관들이 분리되어(separate) 있었으므로(thereby) → 바깥 오류의 영향으로부터 '보호됨'\n오답 ▶ ② 손상된 ③ 연결된 ④ 노출된 — 분리된 상태와 반대 ⑤ 통제된: 근거 없음\n포인트 ▶ thereby = 그것에 의해, 따라서")]
PICK1 = [PK(p, 'Social media has', 'altered', 'preserved', "정답 ▶ altered (변화시켰다)\n오답 ▶ preserved (보존했다)\n이유: '입소문'이 일상어가 될 만큼 → 비즈니스·정치·친목을 '변화시킴'"),
 PK(p, 'The global financial', 'vulnerable', 'immune', "정답 ▶ vulnerable (취약한)\n오답 ▶ immune (면역된)\n이유: 모든 은행·가정을 연결 → 지구 반대편 오류에도 '취약해짐'"),
 PK(p, 'As Columbia University', 'separate', 'connected', "정답 ▶ separate (분리된)\n오답 ▶ connected (연결된)\n이유: 수년 전엔 '분리'되어 있어서 바깥 오류로부터 보호됨"),
 PK(p, 'The digitization of', 'decreased', 'increased', "정답 ▶ decreased (감소했다)\n오답 ▶ increased (증가했다)\n이유: 컴퓨팅 비용이 '떨어지면서' 디지털화가 엄청나게 증가"),
 PK(p, 'This interdependence', 'interdependence', 'independence', "정답 ▶ interdependence (상호 의존성)\n오답 ▶ independence (독립성)\n이유: 스마트 시스템이 서로 소통 → '상호 의존' → 복합적 실패의 온상"),
 PK(p, 'As Rita puts it', 'difficult', 'easy', "정답 ▶ difficult (어려운)\n오답 ▶ easy (쉬운)\n이유: 분리되어 있던 것들이 부딪치면 → 다음 일을 예측하기 '훨씬 더 어려워짐'")]
TF = [TF(p, "Social media made ‘going viral’ a common expression.", True, "making going viral a household term", "정답 ▶ T\n이유: '입소문이 나다'를 일상 용어로 만들었어요.\n어휘 ▶ common expression = household term"),
 TF(p, "The global financial industry has made us safe from errors abroad.", False, "making us vulnerable to human error taking place on the other side of the world", "정답 ▶ F\n이유: 지구 반대편 오류에 '취약해지게' 만들었어요."),
 TF(p, "Years ago, most institutions were protected from outside errors because they were separate.", True, "were separate and thereby buffered from the effects of errors outside their walls", "정답 ▶ T\n이유: 분리되어 있어서 바깥 오류로부터 보호됐어요."),
 TF(p, "The cost of computing power has risen sharply.", False, "as the cost of computing power has decreased", "정답 ▶ F\n이유: 컴퓨팅 비용은 '감소'했어요."),
 TF(p, "Smart systems that communicate on their own have led to many possible breakdowns.", True, "gave rise to an infinite variety of potential breakdowns", "정답 ▶ T\n이유: 무한히 다양한 잠재적 고장을 초래했어요.\n어휘 ▶ on their own = autonomously · lead to = give rise to"),
 TF(p, "When separate things collide, the future becomes easier to predict.", False, "it becomes far more difficult to predict", "정답 ▶ F\n이유: 예측하기 훨씬 더 '어려워져요'.")]
MC = [MC(p, "글의 내용과 일치하지 <u>않는</u> 것은?", [
 "Institutions today are still separate from one another.", "Rita McGrath is a strategy professor.", "Digitization of information has grown greatly.",
 "Interdependence can lead to complex failure.", "The global financial industry connects banks and households."],
 "정답 ▶ Institutions today are still separate from one another.\n이유: years ago most ~ were separate ~ That is no longer the case. (더 이상 그렇지 않음)\n포인트 ▶ no longer = 더 이상 ~ 아닌 · lead to = be a breeding ground for",
 [["오늘날 기관들은 여전히 서로 분리되어 있다.", "That is no longer the case", "✗ 더 이상 아님"], ["Rita McGrath는 전략학 교수이다.", "strategy professor Rita McGrath", "일치"], ["정보의 디지털화는 크게 증가했다.", "has continued to grow enormously", "일치"], ["상호 의존성은 복합적 실패로 이어질 수 있다.", "a breeding ground for complex failure", "일치"], ["세계 금융 산업은 은행과 가정을 연결한다.", "links every bank and countless households", "일치"]]),
 MC(p, "글의 내용과 <u>일치하는</u> 것은?", ["자율적으로 소통하는 시스템은 잠재적 고장을 매우 다양하게 만들었다.", "소셜 미디어는 정치에는 영향을 주지 않았다.", "오늘날 기관들은 장벽 밖의 오류로부터 보호된다.", "컴퓨팅 비용이 올라 디지털화가 줄었다.", "분리된 것들이 부딪치면 미래 예측이 쉬워진다."],
 "정답 ▶ 자율적으로 소통하는 시스템은 잠재적 고장을 매우 다양하게 만들었다.\n이유: smart systems that communicate autonomously gave rise to an infinite variety of potential breakdowns\n오답 ▶ ② 정치도 변화 ③ 더 이상 아님 ④ 비용 감소·디지털화 증가 ⑤ 어려워짐",
 [["", "an infinite variety of potential breakdowns", "일치 ✔"], ["", "altered business, politics", "정치도"], ["", "That is no longer the case", "아님"], ["", "the cost of computing power has decreased", "감소"], ["", "far more difficult to predict", "어려움"]])]
PICK2 = [PK(p, 'Social media has', 'making', 'made', "정답 ▶ making\n이유: 분사구문, 소셜 미디어가 '만드는' 능동"),
 PK(p, 'The global financial', 'taking place', 'taken place', "정답 ▶ taking place\n이유: human error를 꾸미는 현재분사 — take place는 자동사라 수동(과거분사) 불가"),
 PK(p, 'As Columbia University', 'buffered', 'buffering', "정답 ▶ buffered\n이유: 기관들이 '보호된' 수동 → were (separate and) buffered"),
 PK(p, 'The digitization of', 'has continued', 'have continued', "정답 ▶ has continued\n이유: 주어 The digitization(단수), of ~ information은 수식어"),
 PK(p, 'The development of', 'gave', 'giving', "정답 ▶ gave\n이유: 주어 The development의 동사 자리 (that communicate autonomously는 관계절)"),
 PK(p, 'As Rita puts it', 'to be kept', 'to keep', "정답 ▶ to be kept\n이유: used to + 동사원형, 사물이 '분리되어 유지되던' 수동 → used to be kept")]
VERB = [VB(p, 'The global financial', 'links', 'link', "정답 ▶ links\n이유: 주어 The global financial industry(단수), 현재시제"),
 VB(p, 'The digitization of', 'to grow', 'grow', "정답 ▶ to grow\n이유: continue + to부정사 (continue -ing도 가능하지만 원문은 to grow)", alt=('growing',)),
 VB(p, 'The development of', 'communicate', 'communicate', "x"),
 VB(p, 'As Rita puts it', 'to predict', 'predict', "정답 ▶ to predict\n이유: 가주어 it — 진주어 to부정사 (예측하는 것)")]
VERB = [v for v in VERB if v['v'] != v['a'][0]]
ERR = [ER(p, 'The digitization of', [('has continued', 'have continued'), 'enormously', 'has decreased'], 0, 'has continued', "틀린 곳 ▶ ① have continued → has continued\n이유: 주어 The digitization(단수) — of massive amounts of information은 수식어\n나머지 ▶ ② 부사 enormously가 동사 grow 수식 ✔ ③ 주어 the cost(단수) → has decreased ✔"),
 ER(p, 'The global financial', ['links', 'vulnerable', ('taking place', 'taken place')], 2, 'taking place', "틀린 곳 ▶ ③ taken place → taking place\n이유: take place(발생하다)는 자동사 → 수동형 과거분사 불가, 능동 현재분사로 error를 꾸밈\n나머지 ▶ ① 주어 industry(단수) → links ✔ ② make + 목적어 + 형용사 보어 ✔"),
 ER(p, 'As Rita puts it', [('to be kept', 'to keep'), 'far more', 'what'], 0, 'to be kept', "틀린 곳 ▶ ① to keep → to be kept\n이유: 사물(things)이 '분리된 채 유지되던' 수동 → used to be kept\n나머지 ▶ ② far + 비교급 ✔ ③ predict의 목적어 명사절 what ✔")]
SCR = [1, 2, 4, 5, 6]
ORDER = [[1, 2, 3, 4], [4, 5, 6, 7]]
INSERT = [([2, 3, 4, 5], 1, "정답 ▶ ① (That is no longer the case. 문장)\n이유: 예전엔 분리되어 보호됨 → 더 이상 그렇지 않다 → 디지털화 증가 — That이 앞 문장 전체를 가리킴"),
 ([4, 5, 6, 7], 2, "정답 ▶ ② (This interdependence ~ 문장)\n이유: 자율적으로 소통하는 스마트 시스템 → 이 상호 의존성(This interdependence)이 실패의 온상 → Rita의 말")]
ODD = [([2, 3, "Columbia University is one of the oldest universities in the United States.", 4], 2, "정답 ▶ ③\n이유: 상호 연결이 실패를 퍼뜨린다는 흐름이에요. 대학의 역사 이야기는 관계없어요.")]
BLANK = [BL(p, 'This interdependence', 'complex failure', ["simple success", "fair competition", "steady growth"], "정답 ▶ complex failure (복합적 실패)\n이유: 무한히 다양한 잠재적 고장 → 상호 의존성은 '복합적 실패'의 온상\n오답 ▶ 단순한 성공 · 공정한 경쟁 · 꾸준한 성장"),
 BL(p, 'The development of', 'autonomously', ["rarely", "manually", "silently"], "정답 ▶ autonomously (자율적으로)\n이유: 스마트 시스템이 사람 없이 '스스로' 소통 → 예측하기 어려운 고장\n오답 ▶ rarely 거의 ~않게 · manually 수동으로 · silently 조용히"),
 BL(p, 'The global financial', 'the other side of the world', ["our own home", "the same building", "our local bank"], "정답 ▶ the other side of the world (지구 반대편)\n이유: 세계 금융 산업이 '모든 나라'를 연결 → 멀리서 난 오류에도 취약\n오답 ▶ 우리 집 · 같은 건물 · 동네 은행 — 연결성의 범위를 놓친 말")]
GRAM = [{'q': "빈칸에 알맞은 것은?<br><b>The digitization of massive amounts of information ______ to grow.</b>", 'opts': ["has continued", "have continued", "continuing", "to continue"], 'ex': "정답 ▶ has continued\n이유: 주어 The digitization(단수)"},
 {'q': "빈칸에 알맞은 것은?<br><b>We are vulnerable to errors ______ place far away.</b>", 'opts': ["taking", "taken", "to be taken", "are taking"], 'ex': "정답 ▶ taking\n이유: take place는 자동사 → 현재분사로 명사 수식"},
 {'q': "빈칸에 알맞은 것은?<br><b>Things that used to ______ separate now bump into each other.</b>", 'opts': ["be kept", "keep", "keeping", "kept"], 'ex': "정답 ▶ be kept\n이유: used to + 동사원형, 수동 be p.p."},
 {'q': "빈칸에 알맞은 것은?<br><b>It becomes far more difficult ______ what will happen next.</b>", 'opts': ["to predict", "predict", "predicted", "predicts"], 'ex': "정답 ▶ to predict\n이유: 가주어 it — 진주어 to부정사"}]
SUMQ = [SUM(p, "Once institutions were (A) ______, but now that everything is connected, even a small error can (B) ______ across the world.", [
 "(A) separate – (B) spread", "(A) separate – (B) disappear", "(A) connected – (B) spread", "(A) famous – (B) stop", "(A) digital – (B) shrink"],
 "정답 ▶ (A) separate – (B) spread\n(A) most of our institutions were separate (B) 지구 반대편 오류에도 취약 → 오류가 '퍼짐'\n오답 ▶ disappear 사라지다 · connected: 예전엔 '분리'",
 ["most of our institutions were separate", "on the other side of the world"])]
