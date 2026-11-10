from jfw import *
S = PREP['29']['sents'][:]; assert 'making them' in S[5]; S[5] = S[5].replace('making them', 'makes them')
p = load(29, '29번 · 어법', sents=S, fix_ko={1: "이것이 그것들이 죽지 않는다는 것을 의미하지는 않는다."})
VOCAB = words(29)
EXAM = [EXQ(29, '29. 다음 글의 밑줄 친 부분 중, 어법상 틀린 것은?', underlined(29, ['mean', 'making', 'relevant', 'which', 'are']), [
 "①", "②", "③", "④", "⑤"], 1,
 "정답 ▶ ② making → makes\n이유: 주어 their property(단수) of being able to regenerate ~ organism까지가 긴 주어 → 문장의 동사가 없음 → 단수 동사 makes\n오답 ▶ ① Nor does it mean — 부정어 Nor 도치 뒤 조동사 does + 동사원형 ✔ ③ how relevant those findings will be — be동사의 보어 → 형용사 ✔ ④ 사람 아닌 선행사(rats or mice) + 콤마 → 계속적 용법 which ✔ ⑤ before가 이끄는 시간 부사절, 주어 findings(복수) → are ✔\n포인트 ▶ 긴 주어 뒤 '진짜 동사' 찾기 — 수식어(of ~, 콤마 삽입)를 걷어 내요.", v=False),
 EXQ(29, '다음 글의 주제로 가장 적절한 것은?', p.full(), [
 "limits of applying findings on biologically immortal species to humans", "reasons why hydra and jellyfish live longer than trees", "ways to slow human aging through animal experiments",
 "the universal mechanisms shared by all living things", "why scientists have stopped studying aging"], 0,
 "정답 ▶ ① 생물학적으로 불멸인 종에 대한 발견을 인간에게 적용하는 것의 한계\n이유: 히드라·해파리의 재생 능력은 우리보다 나무에 가깝다 → 인간 노화와 얼마나 관련 있을지 불명확 → 쥐 연구도 인간에게 적용하기 어려움 → 유용해지기까지 오래 걸릴 것\n오답 ▶ ② 나무와 수명 비교 ✗ ③ 노화를 늦추는 방법 제시 ✗ ④ 보편적인 경우도 '때때로'일 뿐 ⑤ 연구를 멈췄다는 말 없음\n포인트 ▶ translate into humans = 인간에게 적용하다"),
 EXQ(29, '다음 빈칸에 들어갈 말로 가장 적절한 것은?', p.blank('trees'), [
 "trees", "humans", "mammals", "fish", "insects"], 0,
 "정답 ▶ ① trees (나무)\n이유: 신체 부위나 생물체 전체를 '재생'하는 능력 → 우리(인간)보다 '나무'와 더 비슷 → 그래서 인간 노화에 적용하기 어려움\n오답 ▶ ② humans: than to us와 같은 말 ③ mammals: 쥐·생쥐가 포유류로 '우리에게 가까운' 쪽 ④⑤ 근거 없음\n포인트 ▶ more similar to A than to B")]
PICK1 = [PK(p, 'Since hydra', 'obvious', 'hidden', "정답 ▶ obvious (명백한)\n오답 ▶ hidden (숨겨진)\n이유: 노화의 '명백한' 징후를 보이지 않아서 불멸이라 불림"),
 PK(p, 'But, unlike', 'increase', 'decrease', "정답 ▶ increase (증가하다)\n오답 ▶ decrease (감소하다)\n이유: 대부분 동물과 '달리' 나이가 들어도 죽을 가능성이 '증가하지' 않음"),
 PK(p, 'Species such as', 'defeat', 'speed up', "정답 ▶ defeat (물리치다)\n오답 ▶ speed up (가속하다)\n이유: 노화학자들이 흥분하는 이유 → 노화를 '물리치는' 단서"),
 PK(p, 'But their property', 'regenerate', 'destroy', "정답 ▶ regenerate (재생하다)\n오답 ▶ destroy (파괴하다)\n이유: 신체 부위·생물체 전체를 '재생'하는 능력 → 나무와 비슷"),
 PK(p, 'Sometimes biology', 'universal', 'unique', "정답 ▶ universal (보편적인)\n오답 ▶ unique (독특한)\n이유: But in other cases(다른 경우엔 적용이 어렵다)와 대조 → 때로는 '보편적'"),
 PK(p, 'But in other cases', 'closer', 'farther', "정답 ▶ closer (더 가까운)\n오답 ▶ farther (더 먼)\n이유: 쥐는 포유류라 생물학적으로 우리에게 훨씬 '가까운데도' 적용이 어렵다(even)")]
TF = [TF(p, "Hydra and the immortal jellyfish show clear signs of aging.", False, "don’t exhibit obvious signs of aging", "정답 ▶ F\n이유: 명백한 노화의 징후를 보이지 않아요.\n어휘 ▶ clear = obvious · show = exhibit"),
 TF(p, "Being called biologically immortal does not mean they never die.", True, "This doesn’t mean they don’t die", "정답 ▶ T\n이유: 불멸이라 불린다고 죽지 않는다는 뜻은 아니에요."),
 TF(p, "Their chance of dying does not rise as they get older.", True, "their likelihood of dying does not increase with age", "정답 ▶ T\n이유: 나이가 들어도 죽을 가능성이 증가하지 않아요.\n어휘 ▶ chance = likelihood · rise = increase"),
 TF(p, "Gerontologists have no interest in these species.", False, "excite gerontologists", "정답 ▶ F\n이유: 노화학자들을 흥분시켜요."),
 TF(p, "It is clear how relevant the findings will be to human aging.", False, "it is not at all clear how relevant", "정답 ▶ F\n이유: 전혀 명확하지 않아요."),
 TF(p, "Even findings from rats can be hard to apply to humans.", True, "even discoveries in rats or mice", "정답 ▶ T\n이유: 쥐나 생쥐의 발견조차 인간에게 적용하기 어려워요.\n어휘 ▶ apply to = translate into")]
MC = [MC(p, "글의 내용과 일치하지 <u>않는</u> 것은?", [
 "Findings from hydra will soon be useful for human medicine.", "Hydra can regenerate whole body parts.", "Rats and mice are mammals.",
 "Biology can be universal when it relates to basic mechanisms.", "These species are often called biologically immortal."],
 "정답 ▶ Findings from hydra will soon be useful for human medicine.\n이유: It may be a very long time before any findings ~ are useful to us. (유용해지기까지 매우 오래 걸릴 수 있음)\n포인트 ▶ basic = fundamental · regenerate = 재생하다",
 [["히드라의 발견은 곧 인간 의학에 유용해질 것이다.", "It may be a very long time before", "✗ 오래 걸림"], ["히드라는 신체 부위 전체를 재생할 수 있다.", "regenerate entire body parts", "일치"], ["쥐와 생쥐는 포유류이다.", "which are mammals", "일치"], ["생명 작용은 근본 기제와 관련될 때 보편적일 수 있다.", "especially if it relates to fundamental mechanisms", "basic = fundamental"], ["이 종들은 흔히 생물학적으로 불멸이라 불린다.", "they are often called biologically immortal", "일치"]]),
 MC(p, "글의 내용과 <u>일치하는</u> 것은?", ["히드라와 불멸의 해파리는 생물학적 원인으로 죽을 수도 있다.", "히드라는 나이가 들수록 죽을 가능성이 커진다.", "히드라는 인간과 가장 비슷한 생물이다.", "쥐 연구 결과는 언제나 인간에게 그대로 적용된다.", "노화학자들은 히드라 연구를 중단했다."],
 "정답 ▶ 히드라와 불멸의 해파리는 생물학적 원인으로 죽을 수도 있다.\n이유: Nor does it even mean that they cannot die of biological causes. (죽을 수 '없다'는 뜻도 아님 → 죽을 수 있음)\n오답 ▶ ② 증가하지 않음 ③ 나무와 더 비슷 ④ 적용하기 어려움 ⑤ 흥분시킴",
 [["", "Nor does it even mean that they cannot die of biological causes", "일치 ✔"], ["", "does not increase with age", "증가 안 함"], ["", "more similar to trees than to us", "나무와 비슷"], ["", "are difficult to translate into humans", "어려움"], ["", "excite gerontologists", "흥분"]])]
PICK2 = [PK(p, 'Since hydra', 'called', 'calling', "정답 ▶ called\n이유: 그것들이 불멸이라고 '불리는' 수동 → are called"),
 PK(p, 'Nor does', 'does it', 'it does', "정답 ▶ does it\n이유: 부정어 Nor가 문장 앞 → 조동사 + 주어 도치"),
 PK(p, 'But, unlike', 'dying', 'die', "정답 ▶ dying\n이유: 전치사 of 뒤 동명사 (likelihood of dying)"),
 PK(p, 'Species such as', 'excite', 'excites', "정답 ▶ excite\n이유: 주어 Species(여기서는 복수 — hydra and jellyfish), such as ~는 수식어"),
 PK(p, 'Species such as', 'to defeat', 'defeat', "정답 ▶ to defeat\n이유: 의문사 + to부정사 (how to defeat = 물리치는 방법)"),
 PK(p, 'But their property', 'similar', 'similarly', "정답 ▶ similar\n이유: make + 목적어 + 형용사 보어 (more similar to)"),
 PK(p, 'It may be', 'gained', 'are gained', "정답 ▶ gained\n이유: findings를 뒤에서 꾸미는 과거분사(얻어진). 동사는 뒤의 are — 동사가 두 개가 되면 안 돼요.")]
VERB = [VB(p, 'Since hydra', 'exhibit', 'exhibit', "x"),
 VB(p, 'But their property', 'makes', 'make', "정답 ▶ makes\n이유: 주어 their property(단수) — 원문항 ②번 정답 포인트"),
 VB(p, 'Although we', 'fascinating', 'fascinate', "정답 ▶ fascinating\n이유: 사실이 '흥미를 주는' 능동 → 현재분사 (fascinated는 사람이 흥미를 느낄 때)"),
 VB(p, 'It may be', 'are', 'be', "정답 ▶ are\n이유: before절(시간 부사절)은 현재시제, 주어 findings(복수)")]
VERB = [v for v in VERB if v['v'] != v['a'][0]]
ERR = [ER(p, 'But their property', ['being able', 'regenerate', ('makes', 'making')], 2, 'makes', "틀린 곳 ▶ ③ making → makes\n이유: 주어 their property ~ organism에 동사가 없음 → 단수 동사 makes\n나머지 ▶ ① 전치사 of 뒤 동명사 ✔ ② be able to + 동사원형 ✔"),
 ER(p, 'Although we', ['fascinating', 'it', ('relevant', 'relevantly')], 2, 'relevant', "틀린 곳 ▶ ③ relevantly → relevant\n이유: those findings will be relevant — be의 보어는 형용사\n나머지 ▶ ① 능동 현재분사 ✔ ② 가주어 it ✔"),
 ER(p, 'But in other cases', [('which', 'that'), 'closer', 'are difficult'], 0, 'which', "틀린 곳 ▶ ① that → which\n이유: 콤마 뒤 계속적 용법에는 that을 쓸 수 없음\n나머지 ▶ ② much + 비교급 closer ✔ ③ 주어 discoveries(복수) → are ✔")]
SCR = [0, 3, 5, 6, 8]
ORDER = [[0, 1, 2, 3], [5, 6, 7, 8, 9]]
INSERT = [([3, 4, 5, 6], 2, "정답 ▶ ② (But their property ~ 문장)\n이유: 노화학자들이 흥분한다(기대) → But 재생 능력 때문에 우리보다 나무에 가깝다(한계) → 그래서 인간 노화와의 관련성이 불명확"),
 ([7, 8, 9], 1, "정답 ▶ ① (But in other cases ~ 문장)\n이유: Sometimes 보편적이다 ↔ But in other cases 적용이 어렵다 — Sometimes와 in other cases가 짝")]
ODD = [([4, 5, "Jellyfish are popular animals in many public aquariums around the world.", 6], 2, "정답 ▶ ③\n이유: 불멸 종의 연구 결과를 인간에게 적용하기 어렵다는 흐름이에요. 수족관에서 인기 있다는 이야기는 관계없어요.")]
BLANK = [BL(p, 'Since hydra', 'immortal', ["mortal", "dangerous", "colorful"], "정답 ▶ immortal (죽지 않는)\n이유: 노화 징후가 없어서 '불멸'이라 불림\n오답 ▶ mortal 죽을 운명의(반대) · dangerous 위험한 · colorful 화려한"),
 BL(p, 'Although we', 'relevant', ["harmful", "expensive", "popular"], "정답 ▶ relevant (관련 있는)\n이유: 그 발견이 인간 노화에 얼마나 '관련 있을지' 불명확 → 적용의 한계\n오답 ▶ harmful 해로운 · expensive 비싼 · popular 인기 있는"),
 BL(p, 'But in other cases', 'translate', ["compare", "return", "sell"], "정답 ▶ translate (적용하다)\n이유: translate A into B = A를 B에 적용하다(옮기다) — 동물 연구를 인간에게\n오답 ▶ compare 비교하다 · return 돌려주다 · sell 팔다")]
GRAM = [{'q': "빈칸에 알맞은 것은?<br><b>Nor ______ it mean that they cannot die.</b>", 'opts': ["does", "do", "is", "has"], 'ex': "정답 ▶ does\n이유: Nor + 조동사 + 주어 + 동사원형 도치, 주어 it(단수) → does"},
 {'q': "빈칸에 알맞은 것은?<br><b>Their property of being able to regenerate body parts ______ them similar to trees.</b>", 'opts': ["makes", "make", "making", "to make"], 'ex': "정답 ▶ makes\n이유: 주어의 핵 property(단수) → makes"},
 {'q': "빈칸에 알맞은 것은?<br><b>It is not clear how ______ those findings will be.</b>", 'opts': ["relevant", "relevantly", "relevance", "relate"], 'ex': "정답 ▶ relevant\n이유: how + 형용사 + 주어 + be → be의 보어는 형용사"},
 {'q': "빈칸에 알맞은 것은?<br><b>It may be a long time before the findings ______ useful to us.</b>", 'opts': ["are", "will be", "to be", "being"], 'ex': "정답 ▶ are\n이유: 시간 부사절(before ~)은 미래라도 현재시제"}]
SUMQ = [SUM(p, "Although hydra and jellyfish do not seem to (A) ______, their unique abilities make it (B) ______ to apply findings about them to human aging.", [
 "(A) age – (B) difficult", "(A) age – (B) easy", "(A) move – (B) difficult", "(A) grow – (B) necessary", "(A) eat – (B) possible"],
 "정답 ▶ (A) age – (B) difficult\n(A) 노화의 징후를 보이지 않음 → 늙지(age) 않는 것 같다\n(B) 나무와 더 비슷해서 인간에게 적용하기 '어렵다'\n오답 ▶ easy 쉬운(반대) · necessary 필요한 · possible 가능한",
 ["don’t exhibit obvious signs of aging", "difficult to translate into humans"])]
