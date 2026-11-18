from jfw import *
R = PREP['36']['sents']; st = lambda x: x.split(') ', 1)[1] if x.startswith('(') else x
S = [R[0], st(R[5]), R[6], R[7], st(R[3]), R[4], st(R[1]), R[2]]
p = load(36, '36번 · 글의 순서', sents=S)
VOCAB = words(36)
EXAM = [EXQ(36, '36. 주어진 글 다음에 이어질 글의 순서로 가장 적절한 것은?', p.order_q([0], {'A': [6, 7], 'B': [4, 5], 'C': [1, 2, 3]}), ORD, 4,
 "정답 ▶ ⑤ (C)-(B)-(A)\n이유: 주어진 글 — 우리는 사용자가 아니다 → (C) 우리는 만드는 것에 너무 가까워 객관적으로 못 봄 → 그러면 어떻게 더 효과적으로? (질문) → (B) 엄청나게 효과적인 방법(An incredibly effective way) = 사용성 테스트 → (A) 이 기술(This technique)은 실제 사용자 손에서 얼마나 잘 작동할지 이해하는 데 효과적\n오답 ▶ (A)의 This technique는 (B)의 usability testing을 가리켜야 하므로 (B) 다음 / (B)의 way는 (C)의 질문 how can designers ~?에 대한 답\n포인트 ▶ 질문 → 답(방법) → 지시어(This technique)", v=False),
 EXQ(36, '다음 글의 요지로 가장 적절한 것은?', p.full(), [
 "디자이너는 실제 사용자를 관찰하는 사용성 테스트로 작업을 개선해야 한다.", "디자이너는 자신의 경험을 바탕으로 제품을 설계해야 한다.", "좋은 제품은 화려한 디자인에서 나온다.",
 "사용자의 의견은 디자인에 큰 도움이 되지 않는다.", "제품 개발 비용을 줄이는 것이 가장 중요하다."], 0,
 "정답 ▶ ① 디자이너는 실제 사용자를 관찰하는 사용성 테스트로 작업을 개선해야 한다.\n이유: 우리는 사용자가 아니다 → 최고의 인터페이스는 실제 사용자 관찰로 만들어짐 → 사용성 테스트 → 대표 사용자로부터의 발견으로 수정·개선\n오답 ▶ ② 자신의 경험은 객관적이지 않음(too close) ③ 화려함 언급 없음 ④ 사용자 관찰이 핵심(반대) ⑤ 비용 언급 없음\n포인트 ▶ we are not the user = 디자이너 자신을 기준으로 삼지 말 것"),
 EXQ(36, '다음 빈칸에 들어갈 말로 가장 적절한 것은?', p.blank('we are not the user'), [
 "we are not the user", "users never change", "design is an art", "products sell themselves", "testing is expensive"], 0,
 "정답 ▶ ① 우리는 사용자가 아니다\n이유: 뒤 문장 — 우리는 만드는 것에 너무 가까워 사용자가 어떻게 쓸지 객관적으로 볼 수 없음 → 실제 사용자 관찰이 필요\n오답 ▶ ② 사용자는 변하지 않는다 ③ 디자인은 예술이다 ④ 제품은 저절로 팔린다 ⑤ 테스트는 비싸다 — 근거 없음\n포인트 ▶ 첫 문장의 '단순한 진리'를 다음 문장이 풀어서 설명")]
PICK1 = [PK(p, 'A simple truth', 'embrace', 'reject', "정답 ▶ embrace (기꺼이 받아들이다)\n오답 ▶ reject (거부하다)\n이유: 더 효과적인 제품을 만들기 위해 '받아들여야' 할 진리"),
 PK(p, 'We’re much too close', 'objectively', 'personally', "정답 ▶ objectively (객관적으로)\n오답 ▶ personally (개인적으로)\n이유: 너무 가까워서 '객관적으로' 볼 수 없음"),
 PK(p, 'The best user interfaces', 'observations', 'imaginations', "정답 ▶ observations (관찰)\n오답 ▶ imaginations (상상)\n이유: 실제 사용자에 대한 '관찰'로 만들어진 인터페이스가 최고"),
 PK(p, 'The goal of this method', 'uncover', 'hide', "정답 ▶ uncover (밝혀내다)\n오답 ▶ hide (숨기다)\n이유: 테스트의 목표 → 디자인상의 문제를 '밝혀냄'"),
 PK(p, 'The goal of this method', 'realistic', 'imaginary', "정답 ▶ realistic (현실적인)\n오답 ▶ imaginary (가상의)\n이유: 참가자에게 '실제적인' 활동을 시켜 실제 사용을 관찰"),
 PK(p, 'Designers can use', 'representative', 'imaginary', "정답 ▶ representative (대표적인)\n오답 ▶ imaginary (가상의)\n이유: 실제 사용자를 '대표하는' 사용자들로부터의 발견 — 가상의 사용자로는 실제 성능을 알 수 없음")]
TF = [TF(p, "Designers should assume they think the same way as users.", False, "we are not the user", "정답 ▶ F\n이유: 우리는 사용자가 '아니다'는 사실을 받아들여야 해요."),
 TF(p, "Designers are too close to their work to see it objectively.", True, "We’re much too close to what we build to objectively see it", "정답 ▶ T\n이유: 너무 가까워서 객관적으로 볼 수 없어요.\n포인트 ▶ much too ~ to V = 너무 ~해서 V할 수 없는"),
 TF(p, "The best interfaces are shaped by watching real users.", True, "shaped by observations of real users", "정답 ▶ T\n이유: 실제 사용자 관찰로 만들어진 인터페이스가 최고예요."),
 TF(p, "Usability testing asks participants to do unrealistic tasks.", False, "by asking participants to engage in realistic activities", "정답 ▶ F\n이유: '실제적인' 활동에 참여하도록 해요."),
 TF(p, "Usability testing shows how well a design works in real users’ hands.", True, "how well a design will perform once it is in the hands of real users", "정답 ▶ T\n이유: 실제 사용자 손에서 얼마나 잘 작동할지 이해하게 해 줘요."),
 TF(p, "Designers should stop revising their work after testing.", False, "through subsequent revisions based on the findings", "정답 ▶ F\n이유: 발견한 것에 기반한 차후의 '수정'으로 작업을 개선해요.")]
MC = [MC(p, "글의 내용과 일치하지 <u>않는</u> 것은?", [
 "Usability testing is mainly used to reduce production costs.", "Usability testing can reveal problems in a design.", "It helps designers learn about users’ preferences.",
 "Findings from representative users guide later revisions.", "Real users’ interactions shape the best interfaces."],
 "정답 ▶ Usability testing is mainly used to reduce production costs.\n이유: 목표는 문제를 밝히고, 기회를 발견하고, 사용자 행동·선호를 배우는 것 — 비용 절감 언급 없음\n포인트 ▶ reveal = uncover · later = subsequent",
 [["사용성 테스트는 주로 생산비를 줄이는 데 쓰인다.", "The goal of this method is to uncover problems", "✗ 비용 언급 없음"], ["사용성 테스트는 디자인의 문제를 드러낼 수 있다.", "to uncover problems in a design", "reveal = uncover"], ["디자이너가 사용자의 선호를 알게 돕는다.", "learn more about the behaviors and preferences of users", "일치"], ["대표 사용자의 발견이 이후 수정을 이끈다.", "subsequent revisions based on the findings from representative users", "later = subsequent"], ["실제 사용자의 상호 작용이 최고의 인터페이스를 만든다.", "shaped by observations of real users and their interactions", "일치"]]),
 MC(p, "글의 내용과 <u>일치하는</u> 것은?", ["사용성 테스트는 참가자에게 실제적인 활동을 하게 한다.", "디자이너는 자신이 곧 사용자라는 점을 받아들여야 한다.", "최고의 인터페이스는 디자이너의 상상에서 나온다.", "사용성 테스트는 디자인의 장점만 찾는다.", "디자이너는 테스트 후 작업을 수정하지 않는다."],
 "정답 ▶ 사용성 테스트는 참가자에게 실제적인 활동을 하게 한다.\n이유: by asking participants to engage in realistic activities\n오답 ▶ ② 사용자가 아님 ③ 실제 사용자 관찰 ④ 문제를 밝혀냄 ⑤ 차후 수정",
 [["", "engage in realistic activities", "일치 ✔"], ["", "we are not the user", "아님"], ["", "observations of real users", "관찰"], ["", "uncover problems in a design", "문제도"], ["", "subsequent revisions", "수정"]])]
PICK2 = [PK(p, 'A simple truth', 'is the fact', 'are the fact', "정답 ▶ is\n이유: 주어 A simple truth(단수) — that designers ~ experiences는 관계절"),
 PK(p, 'A simple truth', 'that we are', 'which we are', "정답 ▶ that\n이유: the fact와 동격인 that절 (뒤가 완전한 절)"),
 PK(p, 'We’re much too close', 'what we build', 'that we build', "정답 ▶ what\n이유: 전치사 to의 목적어 + 선행사 없음 + 뒤에 목적어 빠진 불완전한 절 → what"),
 PK(p, 'The best user interfaces', 'have been shaped', 'have shaped', "정답 ▶ have been shaped\n이유: 인터페이스가 관찰에 의해 '만들어진' 수동 (by ~)"),
 PK(p, 'The goal of this method', 'to uncover', 'uncovers', "정답 ▶ to uncover\n이유: be동사 보어 to부정사 (목표는 ~하는 것)"),
 PK(p, 'This technique is', 'understanding', 'understand', "정답 ▶ understanding\n이유: 전치사 for 뒤 동명사")]
VERB = [VB(p, 'The goal of this method', 'asking', 'ask', "정답 ▶ asking\n이유: 전치사 by 뒤 동명사 (by -ing ~함으로써)"),
 VB(p, 'The goal of this method', 'to engage', 'engage', "정답 ▶ to engage\n이유: ask + 목적어 + to부정사"),
 VB(p, 'Designers can use', 'based', 'base', "정답 ▶ based\n이유: revisions를 꾸미는 과거분사 — based on ~ (~에 기반한)"),
 VB(p, 'A simple truth', 'to create', 'create', "정답 ▶ to create\n이유: in order + to부정사")]
VERB = [v for v in VERB if v['v'] != v['a'][0]]
ERR = [ER(p, 'We’re much too close', ['much too', ('what', 'that'), 'how'], 1, 'what', "틀린 곳 ▶ ② that → what\n이유: 선행사가 없고 build의 목적어가 빠진 절 → what(~하는 것)\n나머지 ▶ ① much too + 형용사 + to V ✔ ③ 간접의문문 how + 주어 + 동사 ✔"),
 ER(p, 'The best user interfaces', ['those', ('have been shaped', 'have shaped'), 'their'], 1, 'have been shaped', "틀린 곳 ▶ ② have shaped → have been shaped\n이유: those(=interfaces)가 관찰에 '의해(by)' 만들어진 수동\n나머지 ▶ ① 복수 명사 interfaces를 받는 those ✔ ③ 소유격 their ✔"),
 ER(p, 'The goal of this method', [('is to', 'are to'), 'discover', 'asking'], 0, 'is to', "틀린 곳 ▶ ① are → is\n이유: 주어 The goal(단수) — of this method는 수식어\n나머지 ▶ ② to uncover, (to) discover, and (to) learn 병렬 ✔ ③ by + 동명사 ✔")]
SCR = [0, 1, 2, 4, 6]
ORDER = [[0, 1, 2, 3], [3, 4, 5, 6, 7]]
INSERT = [([2, 3, 4, 5], 2, "정답 ▶ ② (An incredibly effective way ~ 문장)\n이유: 어떻게 더 효과적으로? (질문) → 엄청나게 효과적인 방법 = 사용성 테스트 (답) → 이 방법(this method)의 목표"),
 ([4, 5, 6, 7], 2, "정답 ▶ ② (This technique is effective ~ 문장)\n이유: 사용성 테스트의 목표 → 이 기술(This technique)은 실제 사용자 손에서의 성능 이해에 효과적 → 이 방법으로 수정·개선")]
ODD = [([1, 2, "Many designers prefer working late at night when it is quiet.", 3], 2, "정답 ▶ ③\n이유: 디자이너는 사용자가 아니므로 실제 사용자를 관찰해야 한다는 흐름이에요. 밤에 일하는 습관은 관계없어요.")]
BLANK = [BL(p, 'An incredibly effective', 'usability testing', ["price comparison", "color selection", "online advertising"], "정답 ▶ usability testing (사용성 테스트)\n이유: 실제 사용자를 관찰하는 방법 → 뒤 문장: 참가자에게 실제적인 활동을 시켜 문제를 밝혀냄\n오답 ▶ 가격 비교 · 색 선택 · 온라인 광고"),
 BL(p, 'The best user interfaces', 'real users', ["famous designers", "rival companies", "computer programs"], "정답 ▶ real users (실제 사용자)\n이유: 우리는 사용자가 아니다 → '실제 사용자' 관찰로 만들어야\n오답 ▶ 유명 디자이너 · 경쟁사 · 컴퓨터 프로그램"),
 BL(p, 'Designers can use', 'revisions', ["prices", "holidays", "slogans"], "정답 ▶ revisions (수정)\n이유: 발견한 것에 기반한 차후의 '수정'으로 작업을 개선\n오답 ▶ prices · holidays · slogans")]
GRAM = [{'q': "빈칸에 알맞은 것은?<br><b>We are much too close to our work ______ it objectively.</b>", 'opts': ["to see", "seeing", "see", "seen"], 'ex': "정답 ▶ to see\n이유: too + 형용사 + to V (너무 ~해서 V할 수 없는)"},
 {'q': "빈칸에 알맞은 것은?<br><b>We cannot objectively see ______ we build.</b>", 'opts': ["what", "that", "which", "who"], 'ex': "정답 ▶ what\n이유: 선행사 없음 + 목적어 빠진 절 → what"},
 {'q': "빈칸에 알맞은 것은?<br><b>The goal is to uncover problems by ______ participants to do real tasks.</b>", 'opts': ["asking", "ask", "asked", "to ask"], 'ex': "정답 ▶ asking\n이유: 전치사 by + 동명사"},
 {'q': "빈칸에 알맞은 것은?<br><b>The best interfaces are those that ______ by observations of real users.</b>", 'opts': ["have been shaped", "have shaped", "shaping", "shape"], 'ex': "정답 ▶ have been shaped\n이유: by + 행위자 → 수동, 현재완료 수동 have been p.p."}]
SUMQ = [SUM(p, "Because designers are not the (A) ______, they should improve their products by (B) ______ how real users interact with them through usability testing.", [
 "(A) users – (B) observing", "(A) users – (B) ignoring", "(A) owners – (B) observing", "(A) sellers – (B) guessing", "(A) artists – (B) hiding"],
 "정답 ▶ (A) users – (B) observing\n(A) we are not the user (B) shaped by observations of real users\n오답 ▶ ignoring 무시하는(반대) · guessing 추측하는: 관찰이 아니라 추측이면 객관적이지 않음",
 ["we are not the user", "observations of real users"])]
