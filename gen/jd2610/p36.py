from jfw import *
# 11/23 선생님 요청으로 추가 (36번 · 글의 순서 · 소리는 뇌의 산물). 정답 ② (B)-(A)-(C). 원문 riddle 문장('does it make it sound?')은 시험지 그대로 두고 문항으로는 안 씀
R = PREP['36']['sents']; st = lambda x: x.split(') ', 1)[1] if x.startswith('(') else x
S = [R[0], R[1], st(R[4]), R[5], st(R[2]), R[3], st(R[6]), R[7]]   # 바른 순서: 주어진 글 → (B) → (A) → (C)
p = load(36, '36번 · 글의 순서', sents=S)
VOCAB = words(36)
EXAM = [EXQ(36, '36. 주어진 글 다음에 이어질 글의 순서로 가장 적절한 것은?', p.order_q([0, 1], {'A': [4, 5], 'B': [2, 3], 'C': [6, 7]}), ORD, 1,
 "정답 ▶ ② (B)-(A)-(C)\n이유: 주어진 글 — 색의 인식은 뇌에서만 일어남 → (B) The same is true of sound(소리도 마찬가지), 고막에 닿기 전엔 분자의 교란일 뿐 → (A) that disturbance(그 교란)는 측정할 수 있지만 뇌에 닿기 전엔 소리가 아님 + 나무 수수께끼 → (C) No(수수께끼에 대한 대답), 소리는 심리적 개념\n오답 ▶ (A)의 that disturbance는 (B)의 the disturbance of molecules 뒤 / (C)의 No는 (A)의 질문 뒤\n포인트 ▶ The same(B) = 색 이야기 · that disturbance(A) = (B) · No(C) = 수수께끼의 답", v=False),
 EXQ(36, '다음 글의 주제로 가장 적절한 것은?', p.full(), [
 "sound as something created by the brain, not just physical motion", "ways to measure sound waves with instruments", "reasons why light waves have no color",
 "the noise that trees make when they fall", "differences between animal and human hearing"], 0,
 "정답 ▶ ① 단순한 물리적 운동이 아니라 뇌가 만들어 내는 것으로서의 소리\n이유: 고막에 닿기 전엔 분자의 교란일 뿐 · 뇌에 닿기 전엔 소리가 아님 · 소리는 심리적 개념, 뇌의 산물\n오답 ▶ ② 측정은 언급만 ③ 색 이야기는 비유 ④ 나무는 예시 ⑤ 동물·사람 비교 ✗"),
 EXQ(36, '다음 빈칸에 들어갈 말로 가장 적절한 것은?', p.blank('psychological'), ["psychological", "physical", "musical", "natural", "mechanical"], 0,
 "정답 ▶ ① psychological (심리적인)\n이유: 바로 뒤 a product of brains(뇌의 산물)와 같은 말 → 심리적 개념\n오답 ▶ ② 물리적인 — 분자의 교란 쪽(글이 '소리가 아니다'라고 한 것) ③ 음악적인 ④ 자연의 ⑤ 기계적인\n포인트 ▶ 콤마 뒤 동격(a product of brains)이 빈칸의 단서")]
PICK1 = [PK(p, 'All sound begins', 'motion', 'stillness', "정답 ▶ motion (운동, 움직임)\n오답 ▶ stillness (정지)\n이유: 분자를 교란하는 것 = 움직임에서 소리가 시작"),
 PK(p, 'Isaac Newton', 'colorless', 'colorful', "정답 ▶ colorless (색이 없는)\n오답 ▶ colorful (다채로운)\n이유: 색의 인식은 뇌에서만 일어남 → 빛의 파동 자체는 '색이 없다'"),
 PK(p, 'Isaac Newton', 'brain', 'eye', "정답 ▶ brain (뇌)\n오답 ▶ eye (눈)\n이유: 소리도 '뇌'에 닿아야 소리가 된다는 흐름과 같음"),
 PK(p, 'Thus perception', 'nothing more than', 'far more than', "정답 ▶ nothing more than (~에 불과한)\n오답 ▶ far more than (~보다 훨씬 더한)\n이유: 고막에 닿기 전엔 분자의 교란 '일 뿐'"),
 PK(p, 'We can measure', 'until', 'after', "정답 ▶ until (~할 때까지)\n오답 ▶ after (~한 후에)\n이유: 뇌에 닿을 '때까지는' 소리가 아님 → 뇌에 닿은 뒤에야 소리"),
 PK(p, 'No, because', 'psychological', 'physical', "정답 ▶ psychological (심리적인)\n오답 ▶ physical (물리적인)\n이유: a product of brains(뇌의 산물) = 심리적 개념"),
 PK(p, 'That tree will', 'no creature', 'every creature', "정답 ▶ no creature (어떤 생물도 ~않는)\n오답 ▶ every creature (모든 생물)\n이유: 아무도 듣지 않으면 소리를 낸 것이 아님 → no creature")]
TF = [TF(p, "All sound starts with some kind of motion.", True, "All sound begins with some kind of motion", "정답 ▶ T\n이유: 모든 소리는 어떤 종류의 운동에서 시작돼요."),
 TF(p, "Isaac Newton said that light waves have colors of their own.", False, "light waves are colorless", "정답 ▶ F\n이유: 빛의 파동은 색이 없다고 했어요."),
 TF(p, "Before sound reaches our eardrums, it is only a disturbance of molecules.", True, "it is nothing more than the disturbance of molecules", "정답 ▶ T\n이유: 고막에 닿기 전엔 분자의 교란에 불과해요."),
 TF(p, "Gauges and instruments can measure the disturbance.", True, "We can measure that disturbance with gauges and instruments", "정답 ▶ T\n이유: 측정기와 도구로 그 교란을 측정할 수 있어요."),
 TF(p, "According to the writer, a falling tree makes sound even if no creature hears it.", False, "it has not made sound", "정답 ▶ F\n이유: 아무도 듣지 않으면 소리를 낸 것이 아니에요."),
 TF(p, "The writer sees sound as a product of brains.", True, "a product of brains", "정답 ▶ T\n이유: 소리는 뇌의 산물이라고 해요.")]
MC = [MC(p, "글의 내용과 일치하지 <u>않는</u> 것은?", [
 "A falling tree does not disturb molecules if no one hears it.", "Sound begins with motion that disturbs molecules.", "The perception of color happens in the brain.",
 "Instruments can measure a disturbance of molecules.", "Sound is described as a psychological concept."],
 "정답 ▶ A falling tree does not disturb molecules if no one hears it.\n이유: That tree will disturb molecules — 듣는 이가 없어도 분자는 교란함(다만 '소리'가 아닐 뿐)\n포인트 ▶ 분자의 교란 ≠ 소리",
 [["아무도 듣지 않으면 쓰러지는 나무는 분자를 교란하지 않는다.", "That tree will disturb molecules", "✗ 교란은 함"], ["소리는 분자를 교란하는 운동에서 시작된다.", "All sound begins with some kind of motion", "일치"], ["색의 인식은 뇌에서 일어난다.", "the perception of color only occurs in the brain", "일치"], ["도구로 분자의 교란을 측정할 수 있다.", "We can measure that disturbance with gauges and instruments", "일치"], ["소리는 심리적 개념으로 설명된다.", "sound is a psychological concept", "일치"]])]
PICK2 = [PK(p, 'All sound begins', 'disturbs', 'disturbing', "정답 ▶ disturbs\n이유: 관계대명사 that(선행사 something)의 동사 자리 → 단수 disturbs"),
 PK(p, 'Isaac Newton', 'occurs', 'is occurred', "정답 ▶ occurs\n이유: occur(일어나다)는 자동사 → 수동태 ✗"),
 PK(p, 'The same is true', 'is', 'are', "정답 ▶ is\n이유: 주어 The same(같은 것) → 단수 is"),
 PK(p, 'We can measure', 'until it hits', 'until it will hit', "정답 ▶ hits\n이유: 시간 부사절(until)은 미래 대신 현재"),
 PK(p, 'You may have heard', 'falls', 'will fall', "정답 ▶ falls\n이유: 조건 부사절(If)은 미래 대신 현재"),
 PK(p, 'No, because', 'because', 'because of', "정답 ▶ because\n이유: 뒤에 절(sound is ~) → 접속사 because"),
 PK(p, 'That tree will', 'hears', 'hear', "정답 ▶ hears\n이유: no + 단수 명사(creature) 주어 → hears")]
VERB = [VB(p, 'All sound begins', 'disturbs', 'disturb', "정답 ▶ disturbs\n이유: 선행사 something(단수) → disturbs"),
 VB(p, 'Isaac Newton', 'noted', 'note', "정답 ▶ noted\n이유: 과거의 일(Newton이 지적했다) → 과거형"),
 VB(p, 'You may have heard', 'heard', 'hear', "정답 ▶ heard\n이유: may have + p.p.(~했을지도 모른다)"),
 VB(p, 'That tree will', 'made', 'make', "정답 ▶ made\n이유: has not + p.p. 현재완료")]
ERR = [ER(p, 'All sound begins', ['with', ('disturbs', 'disturb'), 'medium'], 1, 'disturbs', "틀린 곳 ▶ ② disturb → disturbs\n이유: 관계대명사 that의 선행사 something은 단수\n나머지 ▶ ① begin with ✔ ③ ✔"),
 ER(p, 'Thus perception', ['begins', ('hits', 'hit'), 'nothing more than'], 1, 'hits', "틀린 곳 ▶ ② hit → hits\n이유: 주어 it(단수) · 현재 → hits\n나머지 ▶ ① 주어 perception(단수) ✔ ③ ✔"),
 ER(p, 'No, because', [('because', 'because of'), 'psychological', 'a product of'], 0, 'because', "틀린 곳 ▶ ① because of → because\n이유: 뒤에 주어+동사(sound is) → 접속사\n나머지 ▶ ② ✔ ③ 동격 ✔")]
SCR = [0, 1, 2, 4, 6, 7]
ORDER = [[0, 1, 2, 3], [4, 5, 6, 7]]
INSERT = [([1, 2, 3, 4], 1, "정답 ▶ ① (The same is true of sound. 문장)\n이유: 색의 인식은 뇌에서만 → 소리도 마찬가지 → Thus(따라서) 소리의 인식은 고막에서 시작"),
 ([4, 5, 6, 7], 2, "정답 ▶ ② (No, because ~ 문장)\n이유: 나무 수수께끼(질문) → No(대답), 소리는 심리적 개념 → That tree will ~")]
ODD = [([3, 4, "Many musicians prefer wooden instruments because they produce warmer sounds.", 5], 2, "정답 ▶ ③\n이유: 소리는 뇌에 닿아야 소리가 된다는 흐름이에요. 음악가가 나무 악기를 좋아하는 이유는 관계없어요.")]
BLANK = [BL(p, 'Thus perception', 'nothing more than', ["much more than", "completely different from", "the opposite of"], "정답 ▶ nothing more than (~에 불과한)\n이유: 고막에 닿기 전에는 분자의 교란'일 뿐'\n오답 ▶ much more than ~보다 훨씬 더 · completely different from 완전히 다른 · the opposite of ~의 반대"),
 BL(p, 'No, because', 'a product of brains', ["a property of air", "a kind of light", "a result of measurement"], "정답 ▶ a product of brains (뇌의 산물)\n이유: psychological concept와 동격 → 뇌가 만드는 것\n오답 ▶ 공기의 성질 · 빛의 일종 · 측정의 결과"),
 BL(p, 'That tree will', 'no creature', ["every creature", "some birds", "many humans"], "정답 ▶ no creature (어떤 생물도 ~않는)\n이유: 듣는 이가 없을 때 소리가 아님 → no bird, fox, or human과 같은 말\n오답 ▶ 모두 '듣는 이가 있다'는 뜻")]
GRAM = [{'q': "빈칸에 알맞은 것은?<br><b>Sound begins with something that ______ molecules in air.</b>", 'opts': ["disturbs", "disturb", "disturbing", "to disturb"], 'ex': "정답 ▶ disturbs\n이유: 관계대명사절 동사, 선행사 something(단수)"},
 {'q': "빈칸에 알맞은 것은?<br><b>Before it ______ our eardrums, it is only a disturbance.</b>", 'opts': ["hits", "will hit", "hitting", "to hit"], 'ex': "정답 ▶ hits\n이유: 시간 부사절(before)은 미래 대신 현재"},
 {'q': "빈칸에 알맞은 것은? (들어 봤을지도 모른다)<br><b>You ______ the old philosophical riddle.</b>", 'opts': ["may have heard", "may hear", "must hear", "may have hear"], 'ex': "정답 ▶ may have heard\n이유: 과거에 대한 추측 may have + p.p."},
 {'q': "빈칸에 알맞은 것은?<br><b>No, ______ sound is a psychological concept.</b>", 'opts': ["because", "because of", "despite", "due to"], 'ex': "정답 ▶ because\n이유: 뒤에 절 → 접속사"}]
SUMQ = [SUM(p, "Sound is not just a (A) ______ of molecules; it becomes sound only when it is (B) ______ by a brain.", [
 "(A) disturbance – (B) perceived", "(A) disturbance – (B) ignored", "(A) measurement – (B) perceived", "(A) color – (B) produced", "(A) motion – (B) measured"],
 "정답 ▶ (A) disturbance – (B) perceived\n(A) 고막에 닿기 전엔 분자의 '교란'일 뿐 → disturbance\n(B) 뇌에 닿아야(인식되어야) 소리 → perceived\n오답 ▶ ignored 무시된 · measured 측정된(측정은 할 수 있지만 소리는 아님)",
 ["nothing more than the disturbance of molecules", "until it hits a brain, it is not sound"])]
