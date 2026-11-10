from jfw import *
S = PREP['33']['sents'][:]; S[2] = S[2].replace('________________________________________', 'challenges the idea of place as passive backdrop'); assert S[2].endswith('backdrop.')
S = S[:4] + [S[4] + ' ' + S[5]]
p = load(33, '33번 · 빈칸', sents=S)
VOCAB = words(33, add=[("passive", "수동적인"), ("backdrop", "배경")])
B = 'challenges the idea of place as passive backdrop'
EXAM = [EXQ(33, '33. 다음 빈칸에 들어갈 말로 가장 적절한 것은?', p.blank(B), [
 "limits our ability to recall past events", "explains how actions influence thoughts", "shows how time settings work in literature", "makes it difficult for us to define our feelings", "challenges the idea of place as passive backdrop"], 4,
 "정답 ▶ ⑤ 수동적 배경으로서의 장소라는 개념에 이의를 제기한다\n이유: 공간은 그 안에서 일어난 사건과 분리할 수 없다 → 공간적 틀은 모든 경험의 '매개체(medium)'이지 (흔히 생각하듯) 경험 바깥의 단순한 배경이 아니다(not merely a background) → Poulet: 장소가 없으면 존재는 추상적 개념일 뿐. 장소의 적극적 역할 = 수동적 배경이라는 생각에 '이의 제기'\n오답 ▶ ① 과거 사건을 기억하는 능력을 제한 ② 행동이 생각에 미치는 영향 ③ 문학의 시간 배경 ④ 감정 정의의 어려움 — 모두 '장소의 역할'과 무관\n포인트 ▶ not merely a background ~ (as commonly supposed) = 흔한 생각(수동적 배경)을 반박", v=False),
 EXQ(33, '다음 글의 주제로 가장 적절한 것은?', p.full(), [
 "the essential role of place in shaping experience", "the history of Proust’s great novel", "how to describe trees in literature",
 "the difference between space and time", "ways to escape from physical spaces"], 0,
 "정답 ▶ ① 경험을 형성하는 데 있어 장소의 필수적인 역할\n이유: 공간·장소·경험은 뒤얽혀 있고, 공간적 틀은 모든 경험의 매개체. 장소가 없으면 존재는 추상적 개념일 뿐\n오답 ▶ ② Proust 소설은 인용 출처일 뿐 ③ 나무는 예시 ④ 시간 이야기 없음 ⑤ 공간에서 벗어나기 ✗\n포인트 ▶ essential = 필수적인 · shape = 형성하다"),
 EXQ(33, '다음 빈칸에 들어갈 말로 가장 적절한 것은?', p.blank('abstractions'), ["abstractions", "travelers", "decorations", "memories", "strangers"], 0,
 "정답 ▶ ① abstractions (추상적 개념)\n이유: 존재는 장소로 자신을 감싸 '특징짓는다(characterization)' → 장소가 없으면 구체적인 모습이 없는 '추상적인 것'에 불과\n오답 ▶ ② 여행자 ③ 장식 ④ 기억 ⑤ 낯선 사람 — 의복 비유(장소 = 그 존재를 드러내는 옷)와 연결되지 않음")]
PICK1 = [PK(p, 'The very fact', 'inseparable', 'independent', "정답 ▶ inseparable (분리할 수 없는)\n오답 ▶ independent (독립적인)\n이유: 경험이 공간 '안에서' 일어나므로 공간은 그 사건과 '분리할 수 없다'"),
 PK(p, 'If place and space', 'central', 'irrelevant', "정답 ▶ central (중심적인)\n오답 ▶ irrelevant (무관한)\n이유: 장소와 공간이 경험의 바로 그 핵심의 '중심'이라면 → 경험의 매개체"),
 PK(p, 'If place and space', 'medium', 'obstacle', "정답 ▶ medium (매개체)\n오답 ▶ obstacle (장애물)\n이유: 행동·생각·기억·감정이 모두 공간을 '통해' 이루어짐"),
 PK(p, 'If place and space', 'exterior', 'essential', "정답 ▶ exterior (외부의)\n오답 ▶ essential (필수적인)\n이유: not merely ~ — '경험 바깥의' 단순한 배경이 아니라는 부정"),
 PK(p, 'Belgian literary', 'elegantly', 'clumsily', "정답 ▶ elegantly (유려하게)\n오답 ▶ clumsily (서투르게)\n이유: 의복 비유로 그 점을 '멋지게' 표현"),
 PK(p, 'Belgian literary', 'disguise', 'weapon', "정답 ▶ disguise (변장)\n오답 ▶ weapon (무기)\n이유: 옷은 '변장'이자 동시에 그 사람을 특징짓는 것 — 의복 비유")]
TF = [TF(p, "All of our experiences take place in a physical space.", True, "all of our experiences “take place” in a physical space", "정답 ▶ T\n이유: 우리의 모든 경험은 물리적 공간에서 일어나요."),
 TF(p, "A space can easily be separated from the events that took place in it.", False, "makes the space inseparable from what defines it", "정답 ▶ F\n이유: 공간은 그 안에서 일어난 사건과 분리될 수 없어요."),
 TF(p, "People commonly think of space as a background outside of experience.", True, "not merely a background or context exterior to experience (as commonly supposed)", "정답 ▶ T\n이유: 흔히 공간을 경험 외부의 배경으로 생각한다고 괄호 안에서 말해요."),
 TF(p, "The writer argues that space is merely a background to experience.", False, "not merely a background or context exterior to experience", "정답 ▶ F\n이유: 단지 배경이 아니라 모든 경험의 매개체라고 해요."),
 TF(p, "Georges Poulet was a Belgian literary critic.", True, "Belgian literary critic Georges Poulet", "정답 ▶ T\n이유: 벨기에의 문학 평론가예요."),
 TF(p, "Poulet compared places to garments that beings wrap themselves in.", True, "the way one wraps oneself up in a garment", "정답 ▶ T\n이유: 장소를 사람이 몸을 감싸는 옷에 비유했어요.")]
MC = [MC(p, "글의 내용과 일치하지 <u>않는</u> 것은?", [
 "Without places, beings would become more real.", "Experiences cannot be separated from the spaces where they happen.", "The spatial framework is the medium of all experiences.",
 "Poulet wrote about the space in Proust’s novel.", "The writer questions a common belief about place."],
 "정답 ▶ Without places, beings would become more real.\n이유: Without places, beings would be only abstractions. (장소가 없으면 추상적 개념일 뿐)\n포인트 ▶ abstraction(추상) ↔ real/concrete(구체적)",
 [["장소가 없으면 존재는 더 실재적이 될 것이다.", "beings would be only abstractions", "✗ 추상적"], ["경험은 그것이 일어나는 공간과 분리될 수 없다.", "inseparable from what took place there", "일치"], ["공간적 틀은 모든 경험의 매개체이다.", "the spatial framework is the medium of all experiences", "일치"], ["Poulet는 Proust 소설 속 공간에 대해 썼다.", "writing of the space created in Marcel Proust’s great novel", "일치"], ["필자는 장소에 대한 흔한 믿음에 의문을 제기한다.", "as commonly supposed", "일치"]])]
PICK2 = [PK(p, 'The very fact', 'makes the space', 'make the space', "정답 ▶ makes\n이유: 주어 The very fact(단수), that ~ space는 동격절"),
 PK(p, 'The very fact', 'inseparable', 'inseparably', "정답 ▶ inseparable\n이유: make + 목적어 + 형용사 보어"),
 PK(p, 'The tree and', 'are inseparable', 'is inseparable', "정답 ▶ are\n이유: 주어 The tree and the ground (A and B) → 복수"),
 PK(p, 'The tree and', 'what took place', 'that took place', "정답 ▶ what\n이유: 전치사 from 뒤 + 주어가 빠진 절, 선행사 없음 → what"),
 PK(p, 'This intertwining', 'challenges', 'challenge', "정답 ▶ challenges\n이유: 주어 This intertwining(단수), of ~ experience는 수식어"),
 PK(p, 'If place and space', 'possibility that', 'possibility of', "정답 ▶ that\n이유: 뒤에 완전한 절(the spatial framework is ~) → 동격의 접속사 that. of는 전치사라 절이 못 옴"),
 PK(p, 'Belgian literary', 'created', 'creating', "정답 ▶ created\n이유: 소설 속에서 '창조된' 공간 — 과거분사가 the space 수식")]
VERB = [VB(p, 'If place and space', 'supposed', 'suppose', "정답 ▶ supposed\n이유: as (it is) commonly supposed — '흔히 생각되는' 수동"),
 VB(p, 'Belgian literary', 'writing', 'write', "정답 ▶ writing\n이유: 콤마 뒤 분사구문 — Poulet가 '쓰면서'(능동)"),
 VB(p, 'Belgian literary', 'surround', 'surround', "x")]
VERB = [v for v in VERB if v['v'] != v['a'][0]]
ERR = [ER(p, 'The tree and', [('are', 'is'), 'inseparable', 'what'], 0, 'are', "틀린 곳 ▶ ① is → are\n이유: The tree and the ground → 복수\n나머지 ▶ ② 형용사 보어 ✔ ③ 선행사 없는 what ✔"),
 ER(p, 'This intertwining', ['intertwining', ('challenges', 'challenge'), 'passive'], 1, 'challenges', "틀린 곳 ▶ ② challenge → challenges\n이유: 주어의 핵 intertwining(단수 동명사/명사)\n나머지 ▶ ① 주어 자리 동명사(명사) ✔ ③ 형용사 ✔"),
 ER(p, 'Belgian literary', ['elegantly', ('created', 'creating'), 'themselves'], 1, 'created', "틀린 곳 ▶ ② creating → created\n이유: 공간이 소설 속에서 '창조된' 수동 → 과거분사\n나머지 ▶ ① 동사 made를 꾸미는 부사 ✔ ③ 주어 Beings = 목적어 → 재귀대명사 ✔")]
SCR = [0, 1, 2, 3]
ORDER = [[0, 1, 2, 3, 4]]
INSERT = [([0, 1, 2, 3], 2, "정답 ▶ ② (This intertwining ~ 문장)\n이유: 공간은 사건과 분리될 수 없다(나무와 땅의 예) → This intertwining(이런 뒤얽힘)이 앞 내용을 받아 '장소 = 수동적 배경' 생각에 이의 제기 → If 장소가 경험의 중심이라면 …"),
 ([2, 3, 4], 2, "정답 ▶ ② (Belgian literary critic ~ 문장)\n이유: 공간은 경험의 매개체라는 주장 → Poulet가 그 점(the point)을 유려하게 표현 — the point가 앞의 주장을 가리켜요.")]
ODD = [([0, 1, "Many trees in city parks are planted to reduce air pollution.", 2], 2, "정답 ▶ ③\n이유: 공간과 경험이 분리될 수 없다는 흐름에서 나무는 예시일 뿐이에요. 공원 나무가 대기 오염을 줄인다는 이야기는 관계없어요.")]
BLANK = [BL(p, 'The very fact', 'physical', ["imaginary", "digital", "musical"], "정답 ▶ physical (물리적인)\n이유: 경험이 '물리적' 공간에서 일어남 — 나무와 땅 예시\n오답 ▶ imaginary 상상의 · digital 디지털의 · musical 음악의"),
 BL(p, 'If place and space', 'background', ["foundation", "medium", "core"], "정답 ▶ background (배경)\n이유: not merely a ~ exterior to experience — 경험 '바깥의' 단순한 배경\n오답 ▶ foundation 기초 · medium 매개체 · core 핵심 → 필자가 긍정하는 쪽이라 not merely와 안 맞음"),
 BL(p, 'Belgian literary', 'garment', ["mirror", "prison", "ladder"], "정답 ▶ garment (의복)\n이유: wraps oneself up in(몸을 감싸다) + 변장이자 특징 → 옷\n오답 ▶ mirror 거울 · prison 감옥 · ladder 사다리")]
GRAM = [{'q': "빈칸에 알맞은 것은?<br><b>The very fact that our experiences take place in a space ______ the space inseparable from them.</b>", 'opts': ["makes", "make", "making", "to make"], 'ex': "정답 ▶ makes\n이유: 주어 The very fact(단수) — that절은 동격"},
 {'q': "빈칸에 알맞은 것은?<br><b>The tree and the ground ______ inseparable from what took place there.</b>", 'opts': ["are", "is", "being", "be"], 'ex': "정답 ▶ are\n이유: A and B 주어 → 복수"},
 {'q': "빈칸에 알맞은 것은?<br><b>We must accept the possibility ______ the spatial framework is the medium of all experiences.</b>", 'opts': ["that", "of", "which", "what"], 'ex': "정답 ▶ that\n이유: 동격의 that + 완전한 절"},
 {'q': "빈칸에 알맞은 것은?<br><b>Beings surround ______ with the places where they find themselves.</b>", 'opts': ["themselves", "them", "their", "theirs"], 'ex': "정답 ▶ themselves\n이유: 주어 Beings = 목적어 → 재귀대명사"}]
SUMQ = [SUM(p, "Places are not simply a (A) ______ background to our experiences; rather, they are the (B) ______ through which all experiences happen.", [
 "(A) passive – (B) medium", "(A) passive – (B) barrier", "(A) active – (B) medium", "(A) colorful – (B) result", "(A) temporary – (B) memory"],
 "정답 ▶ (A) passive – (B) medium\n(A) 단순한 '수동적' 배경이 아니다 → passive\n(B) 모든 경험의 '매개체' → medium\n오답 ▶ active 적극적인(장소의 역할을 표현하는 말이라 '아니다'와 안 맞음) · barrier 장애물",
 ["the spatial framework is the medium of all experiences", "not merely a background"])]
