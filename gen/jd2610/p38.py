from jfw import *
R = PREP['38']['sents']; G = PREP['38']['given']
S = R[:5] + [G] + R[5:]
p = load(38, '38번 · 문장 삽입', sents=S)
VOCAB = words(38)
EXAM = [EXQ(38, '38. 글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳은?', p.insert_q(5, [2, 3, 4, 6, 7]), SLOT, 3,
 "정답 ▶ ④\n이유: What they found was astonishing.(그들이 알아낸 것은 놀라웠다) 뒤에는 '무엇을' 알아냈는지 나와야 함 → 주어진 문장: 참이든 거짓이든 반복될수록 진실이라는 믿음이 올라갔다 → In other words(다시 말해) 더 자주 들을수록 더 참처럼 들린다(주어진 문장을 쉽게 바꿔 말함) → 이것이 진실 착각 효과\n오답 ▶ ③ 자리에 넣으면 '놀라운 발견' 문장 앞에 결과가 먼저 나와 순서가 어색 / ⑤ 자리는 In other words가 받을 내용이 없어짐\n포인트 ▶ In other words 앞에는 같은 내용을 어려운 말로 한 문장이 와야 해요.", v=False),
 EXQ(38, '다음 글의 제목으로 가장 적절한 것은?', p.full(), [
 "Repeat It Enough, and It Sounds True", "How to Tell True Statements from False Ones", "Why College Students Forget Trivia",
 "New Statements Are More Believable", "Testing Memory Every Two Weeks"], 0,
 "정답 ▶ ① 충분히 반복하면 그것은 참처럼 들린다\n이유: the more often you hear a statement, the more ‘true’ it sounds — 진실 착각 효과\n오답 ▶ ② 참·거짓 구별법 ✗ ③ 잊어버림 ✗ ④ 반대 — 반복된 진술이 더 믿어짐 ⑤ 2주 간격은 실험 방식일 뿐"),
 EXQ(38, '다음 빈칸에 들어갈 말로 가장 적절한 것은?', p.blank('repetition'), ["repetition", "intelligence", "evidence", "age", "interest"], 0,
 "정답 ▶ ① repetition (반복)\n이유: 20개만 매번 반복 → 반복된 것과 아닌 것을 비교 → 참·거짓과 '상관없이' 반복될수록 믿음이 올라감. 다음 문장 the more often you hear도 근거\n오답 ▶ ② 지능 ③ 증거(참·거짓과 상관없다고 했음) ④ 나이 ⑤ 흥미\n포인트 ▶ as a function of ~ = ~에 따라 (변하는)")]
PICK1 = [PK(p, 'In 1977', 'certain', 'careless', "정답 ▶ certain (확신하는)\n오답 ▶ careless (부주의한)\n이유: 진술이 참인지 거짓인지 얼마나 '확신하는지' 물음"),
 PK(p, 'Crucially', 'repeated', 'deleted', "정답 ▶ repeated (반복된)\n오답 ▶ deleted (삭제된)\n이유: 20개는 매번 '반복', 나머지 40개는 새로운 것 — 실험의 핵심"),
 PK(p, 'What they found', 'astonishing', 'predictable', "정답 ▶ astonishing (놀라운)\n오답 ▶ predictable (예측 가능한)\n이유: 참이든 거짓이든 반복만으로 믿음이 올라간다는 '놀라운' 결과"),
 PK(p, 'Regardless of', 'Regardless of', 'Because of', "정답 ▶ Regardless of (~와 상관없이)\n오답 ▶ Because of (~ 때문에)\n이유: 진술이 참이든 거짓이든 '상관없이' 반복이 믿음을 높임"),
 PK(p, 'In other words', 'more often', 'less often', "정답 ▶ more often (더 자주)\n오답 ▶ less often (덜 자주)\n이유: 반복될수록(더 자주 들을수록) 더 참처럼 들림"),
 PK(p, 'This became', 'illusory', 'scientific', "정답 ▶ illusory (착각의, 환상에 불과한)\n오답 ▶ scientific (과학적인)\n이유: 거짓도 참처럼 느끼게 되니 '착각' 효과")]
TF = [TF(p, "The study was conducted by two psychologists in 1977.", True, "In 1977, psychologists Lynn Hasher and David Goldstein", "정답 ▶ T\n이유: 1977년 두 심리학자가 진행했어요."),
 TF(p, "The students evaluated the statements only once.", False, "evaluate the sixty statements three times", "정답 ▶ F\n이유: 2주 간격으로 세 번 평가했어요."),
 TF(p, "All sixty statements were repeated each time.", False, "only twenty of the statements were repeated each time", "정답 ▶ F\n이유: 20개만 반복되었어요."),
 TF(p, "The researchers compared repeated and non-repeated statements.", True, "compared the ‘truth-ratings’ of the repeated versus non-repeated statements", "정답 ▶ T\n이유: 반복된 진술과 반복되지 않은 진술의 진실성 평가를 비교했어요."),
 TF(p, "Only true statements became more believable with repetition.", False, "Regardless of whether the statement was true or false", "정답 ▶ F\n이유: 참이든 거짓이든 상관없이 믿음이 올라갔어요."),
 TF(p, "This finding is called the illusory truth effect.", True, "the illusory truth effect", "정답 ▶ T\n이유: 진실 착각 효과로 알려졌어요.")]
MC = [MC(p, "글의 내용과 일치하지 <u>않는</u> 것은?", [
 "False statements were not affected by repetition.", "Sixty trivia-like statements were used.", "The evaluations took place at two-week intervals.",
 "Forty of the statements were new each time.", "Hearing a statement often makes it sound truer."],
 "정답 ▶ False statements were not affected by repetition.\n이유: Regardless of whether the statement was true or false — 거짓 진술도 반복되면 믿음이 올라감\n포인트 ▶ regardless of = ~와 상관없이 · interval = 간격",
 [["거짓 진술은 반복의 영향을 받지 않았다.", "Regardless of whether the statement was true or false", "✗ 영향 받음"], ["60개의 잡학 같은 진술이 쓰였다.", "sixty general-knowledge trivia-like statements", "일치"], ["평가는 2주 간격으로 이루어졌다.", "at two-week intervals", "일치"], ["매번 40개의 진술은 새로운 것이었다.", "the other forty were new", "일치"], ["진술을 자주 들으면 더 참처럼 들린다.", "the more often you hear a statement, the more ‘true’ it sounds", "일치"]])]
PICK2 = [PK(p, 'In 1977', 'how certain', 'how certainly', "정답 ▶ certain\n이유: they were certain — be의 보어 → 형용사 (how certain they were)"),
 PK(p, 'In 1977', 'true or false', 'true and false', "정답 ▶ or\n이유: either A or B"),
 PK(p, 'The students were', 'were asked', 'asked', "정답 ▶ were asked\n이유: 학생들이 '요청받은' 수동 → were asked to부정사"),
 PK(p, 'The students were', 'to evaluate', 'evaluating', "정답 ▶ to evaluate\n이유: be asked + to부정사"),
 PK(p, 'What they found', 'What', 'That', "정답 ▶ What\n이유: found의 목적어가 빠진 절 + 선행사 없음 → What(~하는 것)이 주어절"),
 PK(p, 'Regardless of', 'whether', 'which', "정답 ▶ whether\n이유: whether A or B = A이든 B이든"),
 PK(p, 'This became', 'known', 'knowing', "정답 ▶ known\n이유: become known as (~로 알려지다) — 수동")]
VERB = [VB(p, 'Crucially', 'repeated', 'repeat', "정답 ▶ repeated\n이유: 진술이 '반복된' 수동 → were repeated"),
 VB(p, 'The researchers', 'compared', 'compare', "정답 ▶ compared\n이유: 과거의 일 → 과거시제(능동, 연구자들이 비교함)"),
 VB(p, 'Regardless of', 'went', 'go', "정답 ▶ went\n이유: 과거의 실험 결과 → 과거시제 (go - went - gone)"),
 VB(p, 'In other words', 'sounds', 'sound', "정답 ▶ sounds\n이유: 주어 it(단수), 일반적 사실 현재시제")]
ERR = [ER(p, 'In 1977', ['asked', ('certain', 'certainly'), 'that'], 1, 'certain', "틀린 곳 ▶ ② certainly → certain\n이유: they were certain — be동사의 보어 형용사\n나머지 ▶ ① 연구자들이 물은 능동 ✔ ③ 명사절 that ✔"),
 ER(p, 'The researchers', [('compared', 'were compared'), 'repeated', 'non-repeated'], 0, 'compared', "틀린 곳 ▶ ① were compared → compared\n이유: 연구자들이 '비교한' 능동, 목적어(the truth-ratings)가 있음\n나머지 ▶ ② ③ 반복된(수동) ✔"),
 ER(p, 'In other words', [('more', 'most'), 'often', 'true'], 0, 'more', "틀린 곳 ▶ ① most → more\n이유: the 비교급 ~, the 비교급 … (~할수록 더 …하다)\n나머지 ▶ ② 부사 ✔ ③ sounds + 형용사 보어 ✔")]
SCR = [0, 1, 2, 5, 6]
ORDER = [[0, 1, 2, 3], [3, 4, 5, 6, 7]]
INSERT = [([1, 2, 3, 4], 1, "정답 ▶ ① (Crucially ~ 문장)\n이유: 60개를 세 번 평가 → Crucially(결정적으로) 20개만 반복 → 그다음 반복 vs 비반복 비교"),
 ([4, 5, 6, 7], 1, "정답 ▶ ① (Regardless of ~ 문장 = 원문항 주어진 문장)\n이유: 놀라운 발견 → 그 내용 → In other words로 다시 말함")]
ODD = [([1, 2, "Many college students prefer studying in groups to studying alone.", 3], 2, "정답 ▶ ③\n이유: 반복이 진실 믿음을 높인다는 실험 흐름이에요. 그룹 공부 선호는 관계없어요.")]
BLANK = [BL(p, 'Crucially', 'twenty', ["sixty", "forty", "ten"], "정답 ▶ twenty (20개)\n이유: 60개 중 20개만 반복, 나머지 40개(the other forty)는 새로운 것\n오답 ▶ 숫자 함정 — 20 + 40 = 60"),
 BL(p, 'The researchers', 'truth-ratings', ["test scores", "reading speeds", "grades"], "정답 ▶ truth-ratings (진실성 평가)\n이유: 진술이 얼마나 참인지 '확신'하는 정도를 비교\n오답 ▶ 시험 점수 · 읽기 속도 · 성적"),
 BL(p, 'In other words', 'true', ["boring", "strange", "difficult"], "정답 ▶ true (참인)\n이유: 반복될수록 진실이라는 믿음이 올라감 → 더 '참처럼' 들림\n오답 ▶ boring 지루한 · strange 이상한 · difficult 어려운")]
GRAM = [{'q': "빈칸에 알맞은 것은?<br><b>They asked the students how ______ they were.</b>", 'opts': ["certain", "certainly", "certainty", "to certain"], 'ex': "정답 ▶ certain\n이유: how + 형용사 + 주어 + be"},
 {'q': "빈칸에 알맞은 것은?<br><b>The students were asked ______ the statements three times.</b>", 'opts': ["to evaluate", "evaluating", "evaluate", "evaluated"], 'ex': "정답 ▶ to evaluate\n이유: ask + 목적어 + to부정사 → 수동 be asked + to부정사"},
 {'q': "빈칸에 알맞은 것은?<br><b>______ they found was astonishing.</b>", 'opts': ["What", "That", "Which", "It"], 'ex': "정답 ▶ What\n이유: 선행사 없음 + found의 목적어 빠짐 → What"},
 {'q': "빈칸에 알맞은 것은?<br><b>The more often you hear a statement, the ______ it sounds.</b>", 'opts': ["truer", "truest", "true", "more truly"], 'ex': "정답 ▶ truer\n이유: the 비교급, the 비교급. sound + 형용사 → true의 비교급 truer (본문은 the more ‘true’)"}]
SUMQ = [SUM(p, "A 1977 study showed that people tend to believe a statement is true when it is (A) ______, whether it is actually true or (B) ______.", [
 "(A) repeated – (B) false", "(A) repeated – (B) new", "(A) written – (B) false", "(A) new – (B) old", "(A) short – (B) long"],
 "정답 ▶ (A) repeated – (B) false\n(A) 반복될수록 믿음이 올라감 → repeated\n(B) 참이든 '거짓'이든 상관없이 → false\n오답 ▶ new 새로운 — 새 진술은 비교 대상(반복 안 된 쪽)",
 ["as a function of repetition", "true or false"])]
