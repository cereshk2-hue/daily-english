from jfw import *
S = PREP['34']['sents'][:]; assert S[1].endswith('_.'); S[1] = re.sub(r'_+', 'our bodies are so very good at it', S[1])
p = load(34, '34번 · 빈칸', sents=S)
VOCAB = words(34)
O = [re.sub(r'^[①-⑤]\s*', '', x) for x in Q['34']['opts']]
EXAM = [EXQ(34, '34. 다음 빈칸에 들어갈 말로 가장 적절한 것은?', p.blank('our bodies are so very good at it'), O, 1,
 "정답 ▶ ② our bodies are so very good at it (우리 몸이 그것을 아주 잘하기 때문)\n이유: 달리기는 슈퍼컴퓨터도 처리 못 할 만큼 엄청난 계산이 필요하고 너무 복잡함 → 그런데도 쉬워 '보이는' 건 우리 몸이 그것을 아주 잘하기 때문 + 마지막 문장 our bodies know more about running than we ever will\n오답 ▶ ① 장비가 많이 필요 없다 ③ 생각보다 에너지가 덜 든다 ④ 어릴 때부터 연습했다 ⑤ 단순한 동작이 의식적 사고를 요구한다(달리기는 완전히 의식적이지 않음 — 반대)\n포인트 ▶ seems very easy, but that is only because ~ = 쉬워 보이는 진짜 이유", v=False),
 EXQ(34, '다음 글의 요지로 가장 적절한 것은?', p.full(), [
 "달리기는 매우 복잡하지만 우리 몸은 그것을 우리가 설명할 수 있는 것보다 더 잘 안다.", "달리기는 단순한 동작이라 누구나 쉽게 설명할 수 있다.", "부상을 막으려면 슈퍼컴퓨터로 달리기를 분석해야 한다.",
 "달리기 실력은 의식적인 연습으로만 늘 수 있다.", "우리 몸은 달리기를 하는 방법을 전혀 모른다."], 0,
 "정답 ▶ ①\n이유: 달리기 지식은 근섬유·세포·DNA 깊이 묻혀 있어 완전히 설명할 수 없지만, 그것이 몸이 모른다는 뜻은 아님 → 몸이 우리보다 더 잘 안다\n오답 ▶ ② 너무 복잡해 설명 불가 ③ 슈퍼컴퓨터도 못 함 ④ 달리기는 완전히 의식적이지 않음 ⑤ 반대(That doesn't mean our bodies don't know)"),
 EXQ(34, '다음 빈칸에 들어갈 말로 가장 적절한 것은?', p.blank('not all conscious'), [
 "not all conscious", "completely simple", "easy to explain", "fully controlled", "rarely natural"], 0,
 "정답 ▶ ① not all conscious (완전히 의식적이지는 않은)\n이유: 달리기 지식은 근섬유·세포·DNA 깊이 묻혀 있음 → 우리가 다 의식하지 못함\n오답 ▶ ② 완전히 단순한(너무 복잡함) ③ 설명하기 쉬운(설명 불가) ④ 완전히 통제되는 ⑤ 거의 자연스럽지 않은")]
PICK1 = [PK(p, 'If our bodies know best', 'injured', 'healed', "정답 ▶ injured (다친)\n오답 ▶ healed (치유된)\n이유: 몸이 가장 잘 안다면 왜 '다칠까?' — 질문의 반전"),
 PK(p, 'The most powerful supercomputer', 'cannot', 'can easily', "정답 ▶ cannot\n오답 ▶ can easily\n이유: 달리기는 너무 복잡해 상상 속 터미네이터만 할 수 있음 → 슈퍼컴퓨터도 처리 '못 함'"),
 PK(p, 'Wherever our running', 'complicated', 'simple', "정답 ▶ complicated (복잡한)\n오답 ▶ simple (단순한)\n이유: 상상 속 T-1000 터미네이터만 할 수 있을 만큼 → 복잡"),
 PK(p, 'Because our running knowledge', 'deeply', 'lightly', "정답 ▶ deeply (깊이)\n오답 ▶ lightly (가볍게)\n이유: 근섬유·세포·DNA 속에 '깊이' 묻혀 있어 설명할 수 없음"),
 PK(p, 'We may feel our way', 'more', 'less', "정답 ▶ more\n오답 ▶ less\n이유: 몸은 우리가 아는 것보다 달리기에 대해 '더' 많이 앎")]
TF = [TF(p, "Running seems easy because our bodies are very good at it.", True, "our bodies are so very good at it", "정답 ▶ T\n이유: 쉬워 보이는 건 몸이 아주 잘하기 때문이에요."),
 TF(p, "A supercomputer can easily perform the computations needed for running.", False, "cannot administer the enormous number of computations", "정답 ▶ F\n이유: 가장 강력한 슈퍼컴퓨터도 처리할 수 없어요."),
 TF(p, "Our running knowledge is buried deep in our muscle fibres, cells and DNA.", True, "buried so deeply within muscle fibres, cells and our DNA", "정답 ▶ T\n이유: 근섬유·세포·DNA 속 깊이 묻혀 있어요."),
 TF(p, "Since we cannot explain running, our bodies do not know how to run.", False, "That doesn’t mean our bodies don’t know how to do it", "정답 ▶ F\n이유: 설명할 수 없다고 몸이 모르는 건 아니에요."),
 TF(p, "Learning to use our senses can help us understand running.", True, "by learning how to use our senses", "정답 ▶ T\n이유: 감각을 쓰는 법을 배우며 이해하는 쪽으로 나아갈 수 있어요.")]
MC = [MC(p, "글의 내용과 일치하지 <u>않는</u> 것은?", [
 "We can fully explain the complexities of running.", "Running is something that seems natural.", "Running is too complicated even for a supercomputer.",
 "Our bodies know more about running than we do.", "Running is not all conscious to us."],
 "정답 ▶ We can fully explain the complexities of running.\n이유: we cannot fully explain its complexities — 완전히 설명할 수 없어요.",
 [["우리는 달리기의 복잡성을 완전히 설명할 수 있다.", "we cannot fully explain its complexities", "✗ 반대"], ["달리기는 자연스러워 보이는 것이다.", "so seemingly natural as running", "일치"], ["달리기는 슈퍼컴퓨터에게도 너무 복잡하다.", "cannot administer the enormous number of computations", "일치"],
  ["우리 몸은 우리보다 달리기에 대해 더 많이 안다.", "our bodies know more about running than we ever will", "일치"], ["달리기는 우리에게 완전히 의식적이지 않다.", "running is not all conscious to us", "일치"]])]
PICK2 = [PK(p, 'If our bodies know best', 'injured', 'injuring', "정답 ▶ injured\n이유: 몸이 '다치는'(수동) → are injured"),
 PK(p, 'The most powerful supercomputer', 'it takes', 'what takes', "정답 ▶ it takes\n이유: computations를 꾸미는 관계절(목적격 관계대명사 생략) — it takes + to부정사(~하는 데 필요하다)"),
 PK(p, 'Wherever our running', 'so complicated that', 'such complicated that', "정답 ▶ so\n이유: so + 형용사 + that (너무 ~해서 …하다)"),
 PK(p, 'Because our running knowledge', 'is buried', 'buries', "정답 ▶ is buried\n이유: 지식이 '묻혀 있는'(수동)"),
 PK(p, 'We may feel our way', 'learning', 'learn', "정답 ▶ learning\n이유: 전치사 by 뒤 동명사"),
 PK(p, 'We may feel our way', 'firing', 'to fire', "정답 ▶ firing\n이유: get + 목적어 + -ing (~하게 하다, 움직이게 하다)")]
VERB = [VB(p, 'We may feel our way', 'accepting', 'accept', "정답 ▶ accepting\n이유: towards understanding ~ and accepting — 전치사 towards의 목적어 동명사 병렬"),
 VB(p, 'We may feel our way', 'seeing', 'see', "정답 ▶ seeing\n이유: by learning ~, getting ~, and seeing — by의 목적어 동명사 병렬"),
 VB(p, 'The most powerful supercomputer', 'to run', 'run', "정답 ▶ to run\n이유: it takes + (명사) + to부정사")]
ERR = [ER(p, 'Because our running knowledge', [('is buried', 'buries'), 'deeply', 'that'], 0, 'is buried', "틀린 곳 ▶ ① buries → is buried\n이유: 지식이 '묻히는' 것 → 수동태\n나머지 ▶ ② 부사 deeply ✔ ③ 명사절 접속사 that ✔"),
 ER(p, 'Wherever our running', ['Wherever', ('so', 'such'), 'able'], 1, 'so', "틀린 곳 ▶ ② such → so\n이유: 형용사(complicated) 앞 → so ~ that\n나머지 ▶ ① 복합관계부사 Wherever ✔ ③ be able to ✔")]
SCR = [0, 1, 4, 5]
ORDER = [[0, 1, 2, 3], [3, 4, 5, 6]]
INSERT = [([3, 4, 5, 6], 2, "정답 ▶ ③ (That doesn't mean ~)\n이유: 우리는 달리기의 복잡성을 완전히 설명할 수 없다 → 그렇다고 몸이 모른다는 뜻은 아니다 → 감각을 통해 이해하는 쪽으로. That = 설명할 수 없다는 것")]
ODD = [([1, 2, "Running shoes have become much more expensive over the last ten years.", 3], 2, "정답 ▶ ③\n이유: 달리기가 얼마나 복잡한지(슈퍼컴퓨터도 못 함)를 설명하는 흐름이에요. 운동화 가격 이야기는 관계없어요.")]
BLANK = [BL(p, 'If our bodies know best', 'seemingly natural', ["truly dangerous", "rarely done", "highly technical"], "정답 ▶ seemingly natural (겉보기에 자연스러운)\n이유: 뒤 문장 running seems very easy\n오답 ▶ 정말 위험한 · 거의 하지 않는 · 매우 기술적인"),
 BL(p, 'Because our running knowledge', 'cannot fully explain', ["can easily explain", "must forget", "should ignore"], "정답 ▶ cannot fully explain (완전히 설명할 수 없다)\n이유: 지식이 깊이 묻혀 있음 → 설명 불가 + 다음 문장 That doesn't mean ~\n오답 ▶ 쉽게 설명할 수 있다 · 잊어야 한다 · 무시해야 한다")]
GRAM = [{'q': "빈칸에 알맞은 것은?<br><b>Running is ______ complicated that only Terminators can do it.</b>", 'opts': ["so", "such", "very", "too"], 'ex': "정답 ▶ so\n이유: so + 형용사 + that"},
 {'q': "빈칸에 알맞은 것은?<br><b>Our running knowledge ______ deeply within our DNA.</b>", 'opts': ["is buried", "buries", "burying", "to bury"], 'ex': "정답 ▶ is buried\n이유: 수동태"},
 {'q': "빈칸에 알맞은 것은?<br><b>We may understand running by ______ how to use our senses.</b>", 'opts': ["learning", "learn", "learned", "to learn"], 'ex': "정답 ▶ learning\n이유: 전치사 + 동명사"}]
SUMQ = [SUM(p, "Running seems easy only because our bodies handle its enormous (A) ______ so well, even though we cannot fully (B) ______ how they do it.", [
 "(A) complexity – (B) explain", "(A) complexity – (B) enjoy", "(A) simplicity – (B) explain", "(A) speed – (B) stop", "(A) cost – (B) measure"],
 "정답 ▶ (A) complexity – (B) explain\n(A) 너무 복잡해 슈퍼컴퓨터도 처리 못 함 → complexity\n(B) we cannot fully explain its complexities → explain\n오답 ▶ enjoy 즐기다 · simplicity 단순함(반대) · speed 속도 · cost 비용",
 ["is so complicated", "we cannot fully explain its complexities"])]
