from jfw import *
R = PREP['39']['sents']; G = PREP['39']['given']
S = R[:3] + [G] + R[3:]
p = load(39, '39번 · 문장 삽입', sents=S)
VOCAB = words(39)
EXAM = [EXQ(39, '39. 글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳은?', p.insert_q(3, [2, 4, 5, 6, 7]), SLOT, 1,
 "정답 ▶ ②\n이유: 잠수 중에는 대기압에 더해 물의 압력도 작용 → (주어진 문장) 물속에서 압력을 느끼지 않으려면 외부·내부 압력을 같게 유지해야 함 → To achieve this(이것을 달성하기 위해) 주변 물의 압력과 같은 압력으로 공기를 공급. this가 가리킬 '목표'가 주어진 문장에 있어요.\n오답 ▶ ① 자리: 아직 물의 압력 이야기가 나오기 전 ③~⑤ 자리: 이미 To achieve this가 나온 뒤라 this가 가리킬 대상이 없어짐\n포인트 ▶ To achieve this / this의 지칭 대상 찾기", v=False),
 EXQ(39, '다음 글의 주제로 가장 적절한 것은?', p.full(), [
 "how divers balance pressure underwater", "why people cannot feel air pressure at all", "the history of deep-sea diving equipment",
 "dangers of breathing pure oxygen", "how the lungs produce air pressure"], 0,
 "정답 ▶ ① 잠수부가 물속에서 압력의 균형을 맞추는 방법\n이유: 물속에서는 외부·내부 압력을 같게 유지 → 주변 수압과 같은 압력으로 호흡용 혼합물 공급 → 깊이에 따라 압력 계산\n오답 ▶ ② 지상에서 기압을 못 느끼는 이유는 도입일 뿐 ③ 장비 역사 ✗ ④ 순수 산소 ✗ ⑤ 폐가 압력을 만든다는 말 없음"),
 EXQ(39, '다음 빈칸에 들어갈 말로 가장 적절한 것은?', p.blank('2 bar'), ["2 bar", "1 bar", "10 bar", "16 bar", "20 bar"], 0,
 "정답 ▶ ① 2 bar\n이유: 지상(대기압) 1바 + 물속 10미터마다 1바 증가 → 10미터 깊이 = 1 + 1 = 2바. 뒤에서 2기압의 호흡용 혼합물이 필요하다고 함\n오답 ▶ ② 1바: 물의 압력을 빼먹음 ③ 10바: 깊이 숫자를 그대로 씀 ④ 16바: 지표면 기압 16~18톤과 혼동 ⑤ 20바\n포인트 ▶ 대기압 + 수압")]
PICK1 = [PK(p, 'The human body', 'constant', 'changing', "정답 ▶ constant (일정한)\n오답 ▶ changing (변하는)\n이유: 지표면에서 몸은 '일정한' 기압을 받음"),
 PK(p, 'However, this pressure', 'balanced', 'increased', "정답 ▶ balanced (균형이 맞춰진)\n오답 ▶ increased (증가된)\n이유: 기압을 못 느끼는 이유 → 내부 압력과 '균형'"),
 PK(p, 'During dives', 'in addition to', 'instead of', "정답 ▶ in addition to (~에 더해)\n오답 ▶ instead of (~ 대신)\n이유: 대기압에 '더해' 물의 압력도(also) 작용"),
 PK(p, 'When submerged', 'equal', 'different', "정답 ▶ equal (같은)\n오답 ▶ different (다른)\n이유: 압력을 느끼지 않으려면 외부와 내부 압력이 '같아야' 함"),
 PK(p, 'Water pressure', 'increases', 'decreases', "정답 ▶ increases (증가하다)\n오답 ▶ decreases (감소하다)\n이유: 깊이에 비례 → 10미터마다 1바씩 '증가'"),
 PK(p, 'It follows', 'stabilize', 'reduce', "정답 ▶ stabilize (안정시키다, 맞추다)\n오답 ▶ reduce (줄이다)\n이유: 2기압을 공급해서 외부·내부 압력을 '맞춤'")]
TF = [TF(p, "On the Earth’s surface, the body experiences air pressure of 16-18 tons per square meter.", True, "16-18 tons per square meter", "정답 ▶ T\n이유: 신체 표면 1제곱미터당 16~18톤의 기압을 받아요."),
 TF(p, "We feel air pressure strongly in daily life.", False, "this pressure is not felt", "정답 ▶ F\n이유: 내부 압력과 균형을 이뤄서 느껴지지 않아요."),
 TF(p, "During dives, only water pressure acts on the body.", False, "in addition to atmospheric pressure, the pressure of the water also acts", "정답 ▶ F\n이유: 대기압에 더해 물의 압력도 작용해요."),
 TF(p, "Air is supplied to divers at the same pressure as the surrounding water.", True, "under pressure equal to the pressure applied by the surrounding water", "정답 ▶ T\n이유: 주변 물의 압력과 같은 압력으로 공급돼요."),
 TF(p, "Water pressure increases by 1 bar for every 10 meters.", True, "It increases by 1 bar for every 10 meters", "정답 ▶ T\n이유: 10미터마다 1바씩 증가해요."),
 TF(p, "A diver at 10 meters needs a breathing mixture at 1 atmosphere.", False, "a pressure of 2 atmospheres is required", "정답 ▶ F\n이유: 2기압의 호흡용 혼합물이 필요해요.")]
MC = [MC(p, "글의 내용과 일치하지 <u>않는</u> 것은?", [
 "Water pressure stays the same regardless of depth.", "Internal pressure balances external pressure on land.", "Divers are supplied with air under pressure.",
 "The lungs contain internal pressure.", "A diver at 10 meters experiences 2 bar of pressure."],
 "정답 ▶ Water pressure stays the same regardless of depth.\n이유: Water pressure increases proportionally with depth.\n포인트 ▶ proportionally = 비례하여 · regardless of = ~와 상관없이",
 [["수압은 깊이와 상관없이 같다.", "Water pressure increases proportionally with depth", "✗ 증가"], ["지상에서는 내부 압력이 외부 압력과 균형을 이룬다.", "external pressure is balanced by internal pressure", "일치"], ["잠수부에게는 압력이 가해진 공기가 공급된다.", "supplied to the diver under pressure", "일치"], ["폐에는 내부 압력이 있다.", "internal pressure in the lungs", "일치"], ["10미터의 잠수부는 2바의 압력을 겪는다.", "a pressure of 2 bar", "일치"]])]
PICK2 = [PK(p, 'The human body', 'experiences', 'experience', "정답 ▶ experiences\n이유: 주어의 핵 The human body(단수), on ~ surface는 수식어"),
 PK(p, 'However, this pressure', 'felt', 'feeling', "정답 ▶ felt\n이유: 압력이 '느껴지지' 않는 수동 → is not felt"),
 PK(p, 'However, this pressure', 'is balanced', 'balances', "정답 ▶ is balanced\n이유: 외부 압력이 내부 압력에 의해 '균형이 맞춰지는' 수동 (by ~)"),
 PK(p, 'During dives', 'During', 'While', "정답 ▶ During\n이유: 뒤에 명사(dives) → 전치사 During. While은 접속사"),
 PK(p, 'When submerged', 'submerged', 'submerging', "정답 ▶ submerged\n이유: When (you are) submerged — 몸이 물속에 '잠기는' 수동"),
 PK(p, 'When submerged', 'feeling', 'to feel', "정답 ▶ feeling\n이유: avoid + 동명사"),
 PK(p, 'To achieve this', 'is supplied', 'supplies', "정답 ▶ is supplied\n이유: 공기가 잠수부에게 '공급되는' 수동")]
VERB = [VB(p, 'To achieve this', 'applied', 'apply', "정답 ▶ applied\n이유: 주변 물에 의해 '가해지는' 압력 — 과거분사가 the pressure 수식"),
 VB(p, 'Water pressure', 'increases', 'increase', "정답 ▶ increases\n이유: 주어 Water pressure(단수), 일반적 사실 현재"),
 VB(p, 'It follows', 'experiences', 'experience', "정답 ▶ experiences\n이유: that절 주어 a diver(단수)"),
 VB(p, 'It follows', 'required', 'require', "정답 ▶ required\n이유: 공급이 '요구되는' 수동 → is required")]
ERR = [ER(p, 'However, this pressure', [('felt', 'feeling'), 'because', 'is balanced'], 0, 'felt', "틀린 곳 ▶ ① feeling → felt\n이유: 압력이 느껴지지 않는 수동 → is not felt\n나머지 ▶ ② 뒤에 절 → 접속사 ✔ ③ 수동 ✔"),
 ER(p, 'When submerged', ['submerged', ('feeling', 'to feel'), 'it'], 1, 'feeling', "틀린 곳 ▶ ② to feel → feeling\n이유: avoid + 동명사\n나머지 ▶ ① 수동 분사 ✔ ③ 가주어 it ✔"),
 ER(p, 'It follows', ['that', 'experiences', ('is required', 'are required')], 2, 'is required', "틀린 곳 ▶ ③ are required → is required\n이유: 주어의 핵 the supply(단수), of a breathing mixture ~는 수식어\n나머지 ▶ ① 명사절 that ✔ ② 단수 주어 a diver ✔")]
SCR = [0, 1, 2, 3, 4, 7]
ORDER = [[0, 1, 2, 3], [4, 5, 6, 7]]
INSERT = [([0, 1, 2, 3], 1, "정답 ▶ ① (However, this pressure ~ 문장)\n이유: 엄청난 기압을 받음 → However 느끼지 못함(이유: 내부 압력과 균형) → During dives(물속) 이야기로 전환"),
 ([5, 6, 7], 1, "정답 ▶ ① (It increases ~ 문장)\n이유: 수압은 깊이에 비례 → It(수압)은 10미터마다 1바 증가 → 따라서 10미터에서는 2바")]
ODD = [([4, 5, "Many people enjoy diving because they can see colorful fish.", 6], 2, "정답 ▶ ③\n이유: 깊이에 따른 수압과 압력 맞추기를 설명하는 흐름이에요. 화려한 물고기를 보는 즐거움은 관계없어요.")]
BLANK = [BL(p, 'However, this pressure', 'lungs', ["bones", "muscles", "eyes"], "정답 ▶ lungs (폐)\n이유: 공기가 들어 있는 공간(air cavities)과 함께 내부 압력을 가진 곳 → 폐\n오답 ▶ bones 뼈 · muscles 근육 · eyes 눈"),
 BL(p, 'To achieve this', 'breathing mixture', ["warm clothing", "heavy weight", "bright light"], "정답 ▶ breathing mixture (호흡용 혼합물)\n이유: 공기 또는 '호흡용 혼합물'을 압력을 맞춰 공급\n오답 ▶ 따뜻한 옷 · 무거운 추 · 밝은 빛"),
 BL(p, 'Water pressure', 'proportionally', ["randomly", "rarely", "slowly"], "정답 ▶ proportionally (비례하여)\n이유: 10미터마다 1바씩 일정하게 증가 → 깊이에 '비례'\n오답 ▶ randomly 무작위로 · rarely 드물게 · slowly 천천히")]
GRAM = [{'q': "빈칸에 알맞은 것은?<br><b>This pressure is not ______ because it is balanced by internal pressure.</b>", 'opts': ["felt", "feeling", "feel", "to feel"], 'ex': "정답 ▶ felt\n이유: be + p.p. 수동 (느껴지다)"},
 {'q': "빈칸에 알맞은 것은?<br><b>______ dives, the pressure of the water also acts on the body.</b>", 'opts': ["During", "While", "When", "Although"], 'ex': "정답 ▶ During\n이유: 명사 앞 → 전치사"},
 {'q': "빈칸에 알맞은 것은?<br><b>To avoid ______ the pressure, equal pressure must be maintained.</b>", 'opts': ["feeling", "to feel", "feel", "felt"], 'ex': "정답 ▶ feeling\n이유: avoid + 동명사"},
 {'q': "빈칸에 알맞은 것은?<br><b>The supply of a breathing mixture under 2 atmospheres ______ required.</b>", 'opts': ["is", "are", "be", "being"], 'ex': "정답 ▶ is\n이유: 주어 the supply(단수)"}]
SUMQ = [SUM(p, "To keep from feeling water pressure, divers need external and internal pressure to be (A) ______, so they are supplied with air whose pressure (B) ______ with depth.", [
 "(A) equal – (B) increases", "(A) equal – (B) decreases", "(A) different – (B) increases", "(A) low – (B) disappears", "(A) high – (B) stops"],
 "정답 ▶ (A) equal – (B) increases\n(A) 외부·내부 압력을 '같게' 유지 → equal\n(B) 수압이 깊이에 따라 증가하므로 공급 압력도 '증가' → increases\n오답 ▶ decreases 감소(반대) · different 다른(반대)",
 ["equal external and internal pressure", "Water pressure increases proportionally with depth"])]
