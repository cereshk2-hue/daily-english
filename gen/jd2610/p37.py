from jfw import *
R = PREP['37']['sents']; st = lambda x: x.split(') ', 1)[1] if x.startswith('(') else x
S = [R[0], st(R[3]), R[4], st(R[5]), R[6], st(R[1]), R[2]]
p = load(37, '37번 · 글의 순서', sents=S)
VOCAB = words(37)
EXAM = [EXQ(37, '37. 주어진 글 다음에 이어질 글의 순서로 가장 적절한 것은?', p.order_q([0], {'A': [5, 6], 'B': [1, 2], 'C': [3, 4]}), ORD, 2,
 "정답 ▶ ③ (B)-(C)-(A)\n이유: 주어진 글 — 대면 협업에서는 작업 공간이 의사소통 공간의 부분 집합 → (B) Ishii는 이것(this)을 '틈 없는 의사소통'이라 부름. However, 원격 작업에서는 작업 공간이 분리됨 → (C) For example 화상 회의에서 한 화면엔 얼굴, 다른 화면엔 문서 → 동시에 볼 수 없음 → (A) So, 두 공간 사이에 인위적인 틈(seam)이 생김 → 이것이 예측해야 할 원격 기술의 영향\n오답 ▶ (A)의 So와 artificial seam은 '분리' 이야기 뒤에만 가능 / (C)의 For example은 원격 작업에서의 분리(B 후반) 뒤에 와야 함\n포인트 ▶ this(B) = 주어진 글 · seamless(B) ↔ seam(A) · For example(C) = 앞의 일반 진술 뒤", v=False),
 EXQ(37, '다음 글의 주제로 가장 적절한 것은?', p.full(), [
 "how remote technology separates task space from communication space", "advantages of face-to-face meetings over online classes", "ways to design better computer screens",
 "the history of the MIT Media Lab", "why video conferencing is more efficient than meeting in person"], 0,
 "정답 ▶ ① 원격 기술이 작업 공간을 의사소통 공간에서 분리하는 방식\n이유: 대면에서는 틈이 없음(seamless) ↔ 원격에서는 분리 → 화상 회의 예시 → 인위적인 틈\n오답 ▶ ② 온라인 수업 ✗ ③ 화면 디자인 ✗ ④ Ishii는 인용일 뿐 ⑤ 반대"),
 EXQ(37, '다음 빈칸에 들어갈 말로 가장 적절한 것은?', p.blank('seamless'), ["seamless", "remote", "artificial", "limited", "delayed"], 0,
 "정답 ▶ ① seamless (갈라진 틈이 없는)\n이유: because 이하 — 작업 공간과 의사소통 공간 사이에 기능적 분리가 '없다' → 틈이 없는 의사소통\n오답 ▶ ② 원격의 ③ 인위적인(틈이 생긴 원격 쪽) ④ 제한된 ⑤ 지연된 — 대면 협업의 특징이 아님\n포인트 ▶ seam(틈) + less(없는) = seamless")]
PICK1 = [PK(p, 'When people are', 'easily', 'hardly', "정답 ▶ easily (쉽게)\n오답 ▶ hardly (거의 ~않는)\n이유: 대면에서는 서로와 의사소통 단서를 '쉽게' 볼 수 있음"),
 PK(p, 'When people are', 'subset', 'superset', "정답 ▶ subset (부분 집합)\n오답 ▶ superset (상위 집합)\n이유: 대면에서는 작업 공간이 의사소통 공간 '안에' 포함됨"),
 PK(p, 'Ishii, a professor', 'no functional separation', 'a clear separation', "정답 ▶ no functional separation (기능적 분리가 없음)\n오답 ▶ a clear separation (뚜렷한 분리)\n이유: seamless(틈 없는)의 이유 → 분리가 '없다'"),
 PK(p, 'However, when', 'separated', 'combined', "정답 ▶ separated (분리된)\n오답 ▶ combined (합쳐진)\n이유: However — 대면과 반대로 원격에서는 '분리'됨"),
 PK(p, 'In this case', 'impossible', 'easy', "정답 ▶ impossible (불가능한)\n오답 ▶ easy (쉬운)\n이유: 화면이 나뉘어 있으니 단서와 작업 공간을 '동시에' 볼 수 없음"),
 PK(p, 'So, there is', 'artificial', 'natural', "정답 ▶ artificial (인위적인)\n오답 ▶ natural (자연적인)\n이유: 기술(화면 분리) 때문에 생긴 틈 → '인위적인'")]
TF = [TF(p, "In face-to-face collaboration, people can easily see communication cues.", True, "can easily see each other and the range of different communication cues", "정답 ▶ T\n이유: 대면 협업에서는 의사소통 단서를 쉽게 볼 수 있어요."),
 TF(p, "Ishii is a professor at the MIT Media Lab.", True, "a professor at the MIT Media Lab", "정답 ▶ T\n이유: MIT Media Lab의 교수예요."),
 TF(p, "When people work remotely, the task space is always part of the communication space.", False, "the task space is often separated from the communication space", "정답 ▶ F\n이유: 원격 작업에서는 흔히 분리돼요."),
 TF(p, "In video conferencing, people may look at a document on one screen and a face on another.", True, "the face of their collaborator on one screen, while looking at a shared document on another", "정답 ▶ T\n이유: 한 화면엔 얼굴, 다른 화면엔 공유 문서를 둘 수 있어요."),
 TF(p, "During video calls, it is easy to see the partner’s cues while looking at the task space.", False, "it is impossible to see many of the remote collaborator’s communication cues", "정답 ▶ F\n이유: 작업 공간을 보면서 동시에 단서를 보는 것은 불가능해요."),
 TF(p, "The writer says the impact of remote technology needs to be predicted.", True, "needs to be predicted through communication models", "정답 ▶ T\n이유: 의사소통 모델을 통해 예측될 필요가 있어요.")]
MC = [MC(p, "글의 내용과 일치하지 <u>않는</u> 것은?", [
 "Remote communication technology removes the seam between the two spaces.", "Face-to-face work has no functional separation between the spaces.", "Ishii calls face-to-face collaboration seamless communication.",
 "In remote work, the task space is often separated.", "Communication models can help predict the effects of remote technology."],
 "정답 ▶ Remote communication technology removes the seam between the two spaces.\n이유: So, there is an artificial seam — 원격 기술 때문에 틈이 '생김'\n포인트 ▶ seam = 갈라진 틈 · remove ↔ create",
 [["원격 의사소통 기술은 두 공간 사이의 틈을 없앤다.", "there is an artificial seam", "✗ 틈이 생김"], ["대면 작업에는 공간 사이 기능적 분리가 없다.", "no functional separation", "일치"], ["Ishii는 대면 협업을 틈 없는 의사소통이라 부른다.", "describes this as seamless communication", "일치"], ["원격 작업에서는 작업 공간이 흔히 분리된다.", "often separated from the communication space", "일치"], ["의사소통 모델은 원격 기술의 영향 예측에 도움이 될 수 있다.", "predicted through communication models", "일치"]])]
PICK2 = [PK(p, 'When people are', 'easily', 'easy', "정답 ▶ easily\n이유: 동사 see를 꾸미는 부사"),
 PK(p, 'When people are', 'being used', 'using', "정답 ▶ being used\n이유: 단서가 '사용되고 있는' 수동 진행 → 명사 cues를 뒤에서 수식하는 being p.p."),
 PK(p, 'Ishii, a professor', 'describes', 'describing', "정답 ▶ describes\n이유: 주어 Ishii(동격 a professor ~는 삽입)의 동사 자리"),
 PK(p, 'Ishii, a professor', 'because there', 'because of there', "정답 ▶ because\n이유: 뒤에 절(there is ~) → 접속사 because"),
 PK(p, 'For example', 'looking', 'looked', "정답 ▶ looking\n이유: while + -ing (사람들이 '보면서' 능동, 접속사 뒤 분사)"),
 PK(p, 'For example', 'shared', 'sharing', "정답 ▶ shared\n이유: 문서가 '공유된' 수동 → 과거분사"),
 PK(p, 'This is the type', 'be predicted', 'predict', "정답 ▶ be predicted\n이유: 영향이 '예측되어야' 하는 수동 → needs to be p.p.")]
VERB = [VB(p, 'When people are', 'collaborating', 'collaborate', "정답 ▶ collaborating\n이유: are + -ing 현재진행"),
 VB(p, 'However, when', 'working', 'work', "정답 ▶ working\n이유: are + -ing 현재진행"),
 VB(p, 'In this case', 'to see', 'see', "정답 ▶ to see\n이유: 가주어 it ~ 진주어 to부정사"),
 VB(p, 'This is the type', 'needs', 'need', "정답 ▶ needs\n이유: 관계대명사 that의 선행사 the type(단수) → needs")]
ERR = [ER(p, 'However, when', ['when', 'working', ('separated', 'separating')], 2, 'separated', "틀린 곳 ▶ ③ separating → separated\n이유: 작업 공간이 '분리되는' 수동 → is separated\n나머지 ▶ ① 접속사 ✔ ② 진행형 ✔"),
 ER(p, 'In this case', [('it', 'this'), 'to see', 'looking'], 0, 'it', "틀린 곳 ▶ ① this → it\n이유: 진주어 to see ~를 받는 가주어는 it\n나머지 ▶ ② 진주어 to부정사 ✔ ③ 전치사 as 뒤 동명사 ✔"),
 ER(p, 'This is the type', [('that', 'what'), 'needs', 'be predicted'], 0, 'that', "틀린 곳 ▶ ① what → that\n이유: 선행사(the type of impact ~)가 있음 → 관계대명사 that\n나머지 ▶ ② 단수 동사 ✔ ③ 수동 ✔")]
SCR = [0, 1, 2, 3, 5, 6]
ORDER = [[0, 1, 2, 3], [3, 4, 5, 6]]
INSERT = [([1, 2, 3, 4], 1, "정답 ▶ ① (However ~ 문장)\n이유: 대면 = 틈 없는 의사소통 → However 원격에서는 분리 → For example 화상 회의"),
 ([3, 4, 5, 6], 2, "정답 ▶ ② (So, there is ~ 문장)\n이유: 동시에 볼 수 없음(예시) → So 인위적인 틈이 존재(결론) → This is the type of impact …")]
ODD = [([2, 3, "Video conferencing has become popular because it saves travel costs.", 4], 2, "정답 ▶ ③\n이유: 화상 회의에서 두 공간이 분리되는 문제를 설명하는 흐름이에요. 이동 비용 절약으로 인기라는 이야기는 관계없어요.")]
BLANK = [BL(p, 'When people are', 'face to face', ["online", "alone", "in silence"], "정답 ▶ face to face (대면하여)\n이유: 서로를 쉽게 볼 수 있는 협업 → 대면\n오답 ▶ online 온라인으로 · alone 혼자 · in silence 침묵 속에서"),
 BL(p, 'However, when', 'remotely', ["together", "happily", "quickly"], "정답 ▶ remotely (원격으로)\n이유: However — 대면과 대조되는 '원격' 작업\n오답 ▶ together 함께 · happily 행복하게 · quickly 빨리"),
 BL(p, 'So, there is', 'seam', ["bridge", "link", "balance"], "정답 ▶ seam (갈라진 틈)\n이유: 두 공간이 분리됨 → '틈'. 앞의 seamless와 대비\n오답 ▶ bridge 다리 · link 연결 · balance 균형 → 연결 쪽 의미")]
GRAM = [{'q': "빈칸에 알맞은 것은?<br><b>They can see the range of communication cues ______.</b>", 'opts': ["being used", "using", "to use", "use"], 'ex': "정답 ▶ being used\n이유: 단서가 사용되고 있는(수동 진행) → being p.p."},
 {'q': "빈칸에 알맞은 것은?<br><b>Ishii describes this as seamless communication ______ there is no separation.</b>", 'opts': ["because", "because of", "despite", "due to"], 'ex': "정답 ▶ because\n이유: 뒤에 절 → 접속사"},
 {'q': "빈칸에 알맞은 것은?<br><b>People look at a ______ document on another screen.</b>", 'opts': ["shared", "sharing", "share", "shares"], 'ex': "정답 ▶ shared\n이유: 공유된(수동) 문서 → 과거분사"},
 {'q': "빈칸에 알맞은 것은?<br><b>This is the impact that needs to ______ through models.</b>", 'opts': ["be predicted", "predict", "predicting", "be predicting"], 'ex': "정답 ▶ be predicted\n이유: need to be p.p. (예측될 필요가 있다)"}]
SUMQ = [SUM(p, "Unlike face-to-face collaboration, remote work often (A) ______ the task space from the communication space, creating an artificial (B) ______.", [
 "(A) separates – (B) seam", "(A) separates – (B) bond", "(A) combines – (B) seam", "(A) protects – (B) rule", "(A) hides – (B) model"],
 "정답 ▶ (A) separates – (B) seam\n(A) 원격 작업에서는 작업 공간이 '분리됨' → separates\n(B) 인위적인 '틈' → seam\n오답 ▶ combines 합치다(반대) · bond 유대",
 ["often separated from the communication space", "an artificial seam"])]
