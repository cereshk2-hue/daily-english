from jfw import *
p = load(21, '21번 · 밑줄 함축 의미')
VOCAB = words(21, add=[("rearrange deck chairs on the Titanic", "(가라앉는 배의 갑판 의자 재배치) 근본 문제는 두고 쓸모없는 일만 하다")])
U = 'rearranging deck chairs on the Titanic'
EXAM = [EXQ(21, '21. 밑줄 친 rearranging deck chairs on the Titanic이 다음 글에서 의미하는 바로 가장 적절한 것은?', p.full(p.text().replace(U, '<u>' + U + '</u>')), [
 "making useless actions that fail to improve an unsatisfactory career", "pushing oneself to stay competent in a changing job market", "keeping the current satisfactory office environment as it is",
 "following others instead of pursuing the career they want", "maintaining career stability despite workplace challenges"], 0,
 "정답 ▶ ① 만족스럽지 못한 경력을 개선하지 못하는 쓸모없는 행동을 하는 것\n이유: 일이 싫으면 비슷한 직책을 다른 부서·회사에서 다시 찾는다(새로 고침 버튼만 누름) → 뭔가 하는 것 같지만 결국 예전처럼 환상이 깨진다. 가라앉는 타이타닉호에서 갑판 의자를 옮기는 것처럼 근본 문제는 그대로 둔 '헛된 노력'이에요. 뒤 문장 You’ve got to completely switch up your approach.도 근거\n오답 ▶ ② 변하는 시장에서 능력 유지 — 글에 없음 ③ 현재 환경이 '만족스럽다'는 반대(unsatisfied) ④ 남을 따라 한다는 말 없음 ⑤ 안정 유지가 아니라 헛된 변화\n포인트 ▶ 함축 의미 = 비유가 가리키는 앞뒤 내용(Efforts like this / switch up your approach)", v=False),
 EXQ(21, '다음 글의 요지로 가장 적절한 것은?', p.full(), [
 "직업에 불만족스럽다면 비슷한 일을 찾기보다 접근 방식을 완전히 바꿔야 한다.", "언젠가 완벽한 직업을 우연히 만나게 될 것이라는 믿음을 가져야 한다.", "다른 회사로 옮기면 직업 만족도는 자연스럽게 높아진다.",
 "구인란을 자주 확인하는 것이 경력 성공의 핵심이다.", "현재 직업에 만족하는 사람은 변화를 피해야 한다."], 0,
 "정답 ▶ ① 직업에 불만족스럽다면 비슷한 일을 찾기보다 접근 방식을 완전히 바꿔야 한다.\n이유: You’ve got to completely switch up your approach. If you keep playing the same game, you’ll win the same prizes.\n오답 ▶ ② 필자가 비판하는 믿음 ③ 다른 회사·부서로 옮겨도 곧 다시 환상이 깨진다고 함 ④ 구인란 검색은 헛된 노력의 예 ⑤ 글은 불만족한 사람 이야기\n포인트 ▶ 같은 게임 = 같은 결과"),
 EXQ(21, '다음 빈칸에 들어갈 말로 가장 적절한 것은?', p.blank('the same prizes'), [
 "the same prizes", "a better position", "a perfect career", "a lot of money", "new opportunities"], 0,
 "정답 ▶ ① the same prizes (똑같은 보상)\n이유: 같은 게임을 계속하면(같은 방식으로 비슷한 직책만 찾으면) 결과도 '같다' → 그래서 접근 방식을 완전히 바꿔야 한다는 결론\n오답 ▶ ②③④⑤ 모두 '좋아진다'는 뜻 → 글의 논리(바뀌지 않는다)와 반대\n포인트 ▶ keep playing the same game ↔ switch up your approach")]
PICK1 = [PK(p, 'Among unsatisfied', 'unsatisfied', 'satisfied', "정답 ▶ unsatisfied (만족하지 못하는)\n오답 ▶ satisfied (만족하는)\n이유: 일이 싫어서(don’t like their job) 다른 일을 찾는 사람들 이야기"),
 PK(p, 'Among unsatisfied', 'miraculously', 'gradually', "정답 ▶ miraculously (기적적으로)\n오답 ▶ gradually (점차)\n이유: 스스로 아무것도 안 하는데 상황이 '기적처럼' 바뀔 거라는 막연한 믿음"),
 PK(p, 'At the same time', 'little', 'much', "정답 ▶ little (거의 ~ 않는)\n오답 ▶ much (많이)\n이유: 기적을 바라면서도 상황을 바꾸려는 일은 '거의 하지 않는다'"),
 PK(p, 'They head to', 'similar', 'different', "정답 ▶ similar (비슷한)\n오답 ▶ different (다른)\n이유: 비슷한 직책만 다시 찾으니 같은 게임을 반복 → 같은 결과"),
 PK(p, 'Efforts like this', 'disenchanted', 'delighted', "정답 ▶ disenchanted (환상이 깨진)\n오답 ▶ delighted (아주 기쁜)\n이유: 새 일자리에서도 '예전만큼(just as ~ as before)' 금방 실망하게 됨"),
 PK(p, 'You’ve got to', 'completely', 'slightly', "정답 ▶ completely (완전히)\n오답 ▶ slightly (약간)\n이유: 같은 게임을 하면 같은 결과 → 접근 방식을 '완전히' 바꿔야 함")]
TF = [TF(p, "Many unsatisfied professionals believe their situation will change someday.", True, "the belief that someday", "정답 ▶ T\n이유: 언젠가 상황이 기적적으로 바뀔 거라는 믿음이 반복되는 주제예요."),
 TF(p, "Unsatisfied professionals usually work hard to change their current situation.", False, "do little to meaningfully alter their current situation", "정답 ▶ F\n이유: 현재 상황을 의미 있게 바꾸려고 하는 일이 거의 없어요.\n어휘 ▶ change = alter"),
 TF(p, "They often look for jobs with titles similar to their current ones.", True, "search for roles with a similar job title", "정답 ▶ T\n이유: 구인란에서 비슷한 직책을 찾아요."),
 TF(p, "Finding a new role in another company solves their problem for good.", False, "quickly become just as disenchanted as they were before", "정답 ▶ F\n이유: 새 일자리에서도 금방 예전처럼 환상이 깨져요.\n어휘 ▶ for good = 영원히"),
 TF(p, "Such efforts make them feel as if they are doing something.", True, "feel like they are doing something", "정답 ▶ T\n이유: 무언가를 하고 있는 것처럼 느끼게 해요.\n어휘 ▶ feel as if = feel like + 절"),
 TF(p, "The writer advises keeping the same approach to win better prizes.", False, "You’ve got to completely switch up your approach", "정답 ▶ F\n이유: 접근 방식을 완전히 바꿔야 한다고 해요.")]
MC = [MC(p, "글의 내용과 일치하지 <u>않는</u> 것은?", [
 "Moving to a different department is a reliable way to find job satisfaction.", "Unsatisfied workers often hope for a miracle in their careers.", "They rarely take meaningful action to change their situation.",
 "They look for roles similar to their current job title.", "The writer suggests changing one’s approach entirely."],
 "정답 ▶ Moving to a different department is a reliable way to find job satisfaction.\n이유: 다른 부서·회사에서 '새로 고침'만 하면 곧 예전처럼 환상이 깨진다(just as disenchanted as they were before)\n포인트 ▶ rarely ≒ do little · entirely = completely · hope for a miracle ≒ things will miraculously change",
 [["다른 부서로 옮기는 것은 직업 만족을 찾는 확실한 방법이다.", "quickly become just as disenchanted as they were before", "✗ 다시 실망"], ["만족 못 하는 직장인들은 경력에 기적을 바란다.", "things will miraculously change", "hope for a miracle"], ["그들은 상황을 바꾸기 위한 의미 있는 행동을 거의 하지 않는다.", "do little to meaningfully alter their current situation", "rarely ≒ do little"], ["그들은 현재 직책과 비슷한 일자리를 찾는다.", "search for roles with a similar job title", "일치"], ["필자는 접근 방식을 완전히 바꾸라고 제안한다.", "completely switch up your approach", "entirely = completely"]]),
 MC(p, "글의 내용과 <u>일치하는</u> 것은?", ["같은 방식을 계속하면 같은 결과를 얻게 된다.", "만족하지 못하는 직업인들은 현재 상황을 바꾸려고 많이 노력한다.", "그들은 전혀 다른 분야의 직업을 찾는다.", "새로운 일자리를 얻으면 오랫동안 만족한다.", "필자는 기적을 기다리라고 조언한다."],
 "정답 ▶ 같은 방식을 계속하면 같은 결과를 얻게 된다.\n이유: If you keep playing the same game, you’ll win the same prizes.\n오답 ▶ ② do little ③ 비슷한 직책(similar job title) ④ 금방 다시 실망 ⑤ 접근 방식을 바꾸라고 함",
 [["", "you’ll win the same prizes", "일치 ✔"], ["", "do little to meaningfully alter", "거의 안 함"], ["", "a similar job title", "비슷한 직책"], ["", "quickly become just as disenchanted", "금방 실망"], ["", "completely switch up your approach", "방식 바꾸기"]])]
PICK2 = [PK(p, 'Among unsatisfied', 'there’s', 'there’re', "정답 ▶ there’s\n이유: There + be + 주어. 주어 a repeating theme(단수) → is"),
 PK(p, 'Among unsatisfied', 'the belief that', 'the belief which', "정답 ▶ that\n이유: 뒤가 완전한 절(things will change ~) → 동격의 that (the belief = 그 내용). which는 불완전한 절이 와야 해요."),
 PK(p, 'At the same time', 'alter', 'altering', "정답 ▶ alter\n이유: to (meaningfully) alter — to부정사(부사 meaningfully가 끼어든 형태) → 동사원형"),
 PK(p, 'They head to', 'hoping', 'hoped', "정답 ▶ hoping\n이유: 주어 They가 '바라면서' — 능동의 분사구문 → hoping"),
 PK(p, 'They head to', 'hit the', 'will hit the', "정답 ▶ hit\n이유: 조건 부사절(if ~)은 미래라도 현재시제"),
 PK(p, 'Efforts like this', 'feel like', 'to feel like', "정답 ▶ feel\n이유: 사역동사 make + 목적어 + 동사원형"),
 PK(p, 'It’s like', 'rearranging', 'rearrange', "정답 ▶ rearranging\n이유: 전치사 like 뒤 → 동명사")]
VERB = [VB(p, 'Efforts like this', 'setting', 'set', "정답 ▶ setting\n이유: are + -ing 현재진행 (they’re just setting themselves up)"),
 VB(p, 'Efforts like this', 'disenchanted', 'disenchant', "정답 ▶ disenchanted\n이유: become + 형용사(과거분사) — 사람이 '환상이 깨진' 상태"),
 VB(p, 'If you keep', 'playing', 'play', "정답 ▶ playing\n이유: keep + -ing (계속 ~하다)")]
ERR = [ER(p, 'They head to', ['similar', ('hoping', 'hoped'), 'hit'], 1, 'hoping', "틀린 곳 ▶ ② hoped → hoping\n이유: 주어 They가 바라는 능동 → 현재분사(분사구문)\n나머지 ▶ ① 비슷한 ✔ ③ 조건절 현재시제 ✔"),
 ER(p, 'Efforts like this', [('make', 'makes'), 'feel', 'disenchanted'], 0, 'make', "틀린 곳 ▶ ① makes → make\n이유: 주어 Efforts(복수). like this는 수식어\n나머지 ▶ ② 사역동사 + 동사원형 ✔ ③ become + 과거분사(형용사) ✔"),
 ER(p, 'If you keep', [('keep', 'will keep'), 'playing', 'win'], 0, 'keep', "틀린 곳 ▶ ① will keep → keep\n이유: 조건 부사절은 현재시제가 미래를 대신\n나머지 ▶ ② keep -ing ✔ ③ 주절 you’ll win ✔")]
SCR = [1, 2, 4, 5, 6, 7]
ORDER = [[0, 1, 2, 3], [4, 5, 6, 7]]
INSERT = [([1, 2, 3, 4], 2, "정답 ▶ ② (They head to ~ 문장)\n이유: '그래서 그들은 무엇을 하는가?'라는 질문 바로 뒤에 답(구인란에서 비슷한 직책을 찾는다)이 와요. 그다음 Efforts like this가 이 행동을 가리켜요."),
 ([4, 5, 6, 7], 2, "정답 ▶ ② (You’ve got to ~ 문장)\n이유: 타이타닉호 비유(헛된 노력) → 그러니 접근 방식을 완전히 바꿔야 한다(해결책) → 같은 게임 = 같은 결과(이유)")]
ODD = [([3, 4, "Searching job boards regularly is the most effective way to build a successful career.", 5], 2, "정답 ▶ ③\n이유: 필자는 구인란 검색을 '헛된 노력'으로 비판해요. 가장 효과적인 방법이라는 문장은 흐름과 반대예요.")]
BLANK = [BL(p, 'At the same time', 'alter', ["accept", "describe", "enjoy"], "정답 ▶ alter (바꾸다)\n이유: 기적을 기다리면서도 현재 상황을 '바꾸려는' 노력은 거의 안 함\n오답 ▶ accept 받아들이다 · describe 묘사하다 · enjoy 즐기다"),
 BL(p, 'Efforts like this', 'disenchanted', ["successful", "excited", "confident"], "정답 ▶ disenchanted (환상이 깨진)\n이유: just as ~ as they were before — 예전처럼 다시 '실망'\n오답 ▶ successful 성공한 · excited 신난 · confident 자신 있는"),
 BL(p, 'You’ve got to', 'approach', ["salary", "office", "title"], "정답 ▶ approach (접근 방식)\n이유: 같은 게임(같은 방식)을 하면 같은 결과 → '방식'을 바꿔야 함\n오답 ▶ salary 월급 · office 사무실 · title 직책(직책만 바꾸는 게 바로 헛된 노력)")]
GRAM = [{'q': "빈칸에 알맞은 것은?<br><b>They do little to meaningfully ______ their current situation.</b>", 'opts': ["alter", "altering", "altered", "alters"], 'ex': "정답 ▶ alter\n이유: to + (부사) + 동사원형. 분리 부정사: to meaningfully alter"},
 {'q': "빈칸에 알맞은 것은?<br><b>Efforts like this make professionals ______ like they are doing something.</b>", 'opts': ["feel", "to feel", "feeling", "felt"], 'ex': "정답 ▶ feel\n이유: make + 목적어 + 동사원형 (사역)"},
 {'q': "빈칸에 알맞은 것은?<br><b>It’s like ______ deck chairs on the Titanic.</b>", 'opts': ["rearranging", "rearrange", "to rearrange", "rearranged"], 'ex': "정답 ▶ rearranging\n이유: 전치사 like + 동명사"},
 {'q': "빈칸에 알맞은 것은?<br><b>If you ______ playing the same game, you’ll win the same prizes.</b>", 'opts': ["keep", "will keep", "kept", "to keep"], 'ex': "정답 ▶ keep\n이유: 조건 부사절은 현재시제로 미래를 나타냄"}]
SUMQ = [SUM(p, "Professionals who only look for (A) ______ roles end up just as unhappy, so they need to (B) ______ their approach completely.", [
 "(A) similar – (B) change", "(A) similar – (B) keep", "(A) different – (B) change", "(A) better – (B) repeat", "(A) perfect – (B) defend"],
 "정답 ▶ (A) similar – (B) change\n(A) 비슷한 직책만 찾는다 → similar\n(B) 접근 방식을 완전히 바꿔야(switch up) 한다 → change\n오답 ▶ keep 유지하다 · repeat 반복하다 · defend 옹호하다 → 필자 주장과 반대",
 ["search for roles with a similar job title", "completely switch up your approach"])]
