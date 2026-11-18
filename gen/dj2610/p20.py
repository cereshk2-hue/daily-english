from jfw import *
p = load(20, '20번 · 필자의 주장')
VOCAB = words(20)
EXAM = [EXQ(20, '20. 다음 글에서 필자가 주장하는 바로 가장 적절한 것은?', p.full(), [
 "부모는 자녀의 특성을 파악해서 그에 맞는 피드백을 주어야 한다.", "부모는 자녀가 실패를 두려워하지 않고 도전하도록 격려해야 한다.", "자녀가 방향을 잃지 않도록 부모는 명확한 목표와 기준을 제시해야 한다.",
 "자녀를 독립적인 사람으로 키우려면 과도한 물질적 지원을 경계해야 한다.", "부모는 자녀의 속도에 맞는 자연스러운 성장이 가능한 환경을 제공해야 한다."], 4,
 "정답 ▶ ⑤ 부모는 자녀의 속도에 맞는 자연스러운 성장이 가능한 환경을 제공해야 한다.\n이유: 주제문 As parents, our role should be that of gardeners, providing sunlight, rain, and fertile soil, allowing children to grow naturally at their own pace. — 목수처럼 '모양을 만들지' 말고 정원사처럼 '환경'을 주라\n오답 ▶ ① 피드백 이야기 없음 ② 도전은 정원사형 양육의 '결과'일 뿐 ③ 명확한 목표·기준 제시는 오히려 목수형(방향 감각을 잃게 함) ④ 물질적 지원 언급 없음\n포인트 ▶ 주장 = should 문장 (our role should be ~ / It should not be ~)", v=False),
 EXQ(20, '다음 글의 제목으로 가장 적절한 것은?', p.full(), [
 "Be a Gardener, Not a Carpenter, to Your Children", "How Carpenters Build the Perfect Home", "Why Children Need Clear Rules from Parents",
 "Gardening: A Hobby That Teaches Patience", "The Dangers of Giving Children Too Much Freedom"], 0,
 "정답 ▶ ① 아이들에게 목수가 아니라 정원사가 되어라\n이유: 정원사(환경 제공, 자기 속도) ↔ 목수(이상적인 모습으로 형태 만들기) 대조 → 부모는 정원사여야 한다\n오답 ▶ ② 실제 목수 이야기 아님(비유) ③ 명확한 규칙은 목수형 ④ 실제 원예 이야기 아님 ⑤ 자유가 위험하다는 건 정반대\n포인트 ▶ 비유(gardener / carpenter)는 제목에서도 그대로 살려 쓰기 좋아요"),
 EXQ(20, '다음 빈칸에 들어갈 말로 가장 적절한 것은?', p.blank('autonomy'), [
 "autonomy", "curiosity", "patience", "obedience", "responsibility"], 0,
 "정답 ▶ ① autonomy (자율성)\n이유: 목수처럼 형태를 만들면 → 타인의 지시를 따르는 데 익숙해짐 → '자율성'을 잃음\n오답 ▶ ② curiosity: 정원사형에서 '기르는' 것이라 잃는 것과 연결은 가능하지만 '지시를 따르는 데 익숙'과 직접 대비되는 건 자율성 ③ patience 인내 ④ obedience 순종: 오히려 '얻는' 쪽 ⑤ responsibility 책임감: 근거 없음\n포인트 ▶ lose autonomy ↔ following others’ instructions")]
PICK1 = [PK(p, 'If we, like gardeners', 'suitable', 'harsh', "정답 ▶ suitable (적절한)\n오답 ▶ harsh (가혹한)\n이유: 정원사처럼 '적절한' 환경을 제공하면 아이들이 스스로 탐구함"),
 PK(p, 'If we, like gardeners', 'spontaneously', 'reluctantly', "정답 ▶ spontaneously (자발적으로)\n오답 ▶ reluctantly (마지못해)\n이유: 자기 속도로 자라게 두면 '자발적으로' 세상을 탐구함"),
 PK(p, 'But if we, like carpenters', 'gradually', 'never', "정답 ▶ gradually (점점)\n오답 ▶ never (결코 ~않다)\n이유: 형태를 만들려 하면 '점점' 자율성을 잃음 — never면 잃지 않는다는 반대 뜻"),
 PK(p, 'Such children quickly', 'actively', 'passively', "정답 ▶ actively (능동적으로)\n오답 ▶ passively (수동적으로)\n이유: 놓여지는(being arranged for) 것에 익숙 ↔ '능동적으로' 길을 선택하기 — rather than 대조"),
 PK(p, 'As parents', 'fertile', 'barren', "정답 ▶ fertile (비옥한)\n오답 ▶ barren (척박한)\n이유: 정원사가 주는 것: 햇빛, 비, '기름진' 토양"),
 PK(p, 'The core of', 'complex', 'simple', "정답 ▶ complex (복잡한)\n오답 ▶ simple (단순한)\n이유: 자신만의 '지도'가 필요한 이유 → 세상이 '복잡'하기 때문")]
TF = [TF(p, "Children raised like plants in a garden develop curiosity and independence.", True, "developing curiosity, creativity, and independence", "정답 ▶ T\n이유: 정원사처럼 키우면 호기심, 창의성, 독립심을 발달시켜요."),
 TF(p, "Carpenter-like parents help children become more autonomous.", False, "they will gradually lose autonomy", "정답 ▶ F\n이유: 목수형 양육은 아이들이 자율성을 '잃게' 해요.\n어휘 ▶ autonomous (형) 자율적인 ↔ autonomy (명) 자율성"),
 TF(p, "Children shaped by their parents get used to following others’ instructions.", True, "becoming accustomed to following others’ instructions", "정답 ▶ T\n이유: 타인의 지시를 따르는 데 익숙해져요.\n어휘 ▶ get used to = become accustomed to"),
 TF(p, "Children who are always arranged for keep a strong sense of direction.", False, "quickly lose their sense of direction", "정답 ▶ F\n이유: 방향 감각을 빠르게 잃어버려요."),
 TF(p, "The writer says parents should carve out a perfect piece according to their will.", False, "It should not be that of carpenters", "정답 ▶ F\n이유: 그것은 목수의 역할이고, 부모는 그래서는 '안 된다'고 했어요."),
 TF(p, "Education begins with helping children find their own map.", True, "helping children find their own “map”", "정답 ▶ T\n이유: 교육의 핵심은 아이들이 자신만의 '지도'를 찾도록 돕는 것에서 시작해요.\n어휘 ▶ begin with = start with")]
MC = [MC(p, "글의 내용과 일치하지 <u>않는</u> 것은?", [
 "Children shaped by parents learn to choose their own path actively.", "Children allowed to grow at their own pace explore the world on their own.", "Gardener-like parents provide what children need to grow.",
 "Carpenter-like parents try to make children fit an ideal image.", "Children need their own map in a complex world."],
 "정답 ▶ Children shaped by parents learn to choose their own path actively.\n이유: they are used to being arranged for, rather than actively choosing their path (능동적으로 선택하기보다 놓여지는 데 익숙)\n포인트 ▶ fit an ideal image = shape into our ideal image · on their own = spontaneously",
 [["부모가 형태를 만든 아이들은 능동적으로 자신의 길을 고르게 된다.", "rather than actively choosing their path", "✗ 놓여지는 데 익숙"], ["자기 속도로 자라도록 허락된 아이들은 스스로 세상을 탐구한다.", "they will spontaneously explore the world", "on their own = spontaneously"], ["정원사 같은 부모는 아이가 자라는 데 필요한 것을 준다.", "providing sunlight, rain, and fertile soil", "일치"], ["목수 같은 부모는 아이를 이상적인 모습에 맞추려 한다.", "shape” children into our ideal image", "일치"], ["아이들은 복잡한 세상에서 자신만의 지도가 필요하다.", "find their own “map” to find their direction in a complex world", "일치"]]),
 MC(p, "글의 내용과 <u>일치하는</u> 것은?", ["정원사형 양육을 받은 아이들은 담대하게 도전한다.", "목수형 양육은 아이들의 창의성을 길러 준다.", "아이들은 부모가 정한 속도에 맞춰 자라야 한다.", "부모는 아이들을 '완벽한' 작품으로 조각해야 한다.", "교육의 핵심은 아이들에게 정답을 알려 주는 것이다."],
 "정답 ▶ 정원사형 양육을 받은 아이들은 담대하게 도전한다.\n이유: Such children love life, dare to challenge, and possess initiative.\n오답 ▶ ② 창의성은 정원사형에서 ③ 자신의 속도(their own pace) ④ 그래서는 안 됨 ⑤ 스스로 지도를 찾도록 '돕는' 것",
 [["", "dare to challenge", "일치 ✔"], ["", "developing curiosity, creativity", "정원사형"], ["", "at their own pace", "자기 속도"], ["", "It should not be that of carpenters", "안 됨"], ["", "helping children find their own “map”", "돕기"]])]
PICK2 = [PK(p, 'If we, like gardeners', 'provide', 'will provide', "정답 ▶ provide\n이유: 조건 부사절(If ~)에서는 미래 대신 현재시제"),
 PK(p, 'If we, like gardeners', 'grow at', 'to grow at', "정답 ▶ grow\n이유: 사역동사 let + 목적어 + 동사원형"),
 PK(p, 'If we, like gardeners', 'developing', 'developed', "정답 ▶ developing\n이유: 분사구문, 의미상 주어 they(아이들)가 '발달시키는' 능동 → 현재분사"),
 PK(p, 'But if we, like carpenters', 'following', 'follow', "정답 ▶ following\n이유: become accustomed to + 동명사 (to는 전치사)"),
 PK(p, 'Such children quickly', 'being arranged', 'arranging', "정답 ▶ being arranged\n이유: 아이들이 '마련받는(놓여지는)' 수동 → 동명사 수동형 being p.p."),
 PK(p, 'As parents', 'allowing', 'allowed', "정답 ▶ allowing\n이유: 분사구문, 주어 our role(정원사의 역할)이 아이들이 자라도록 '허락하는' 능동")]
VERB = [VB(p, 'Such children love', 'possess', 'possess', "x"),
 VB(p, 'But if we, like carpenters', 'becoming', 'become', "정답 ▶ becoming\n이유: 콤마 뒤 분사구문(결과), 아이들이 '익숙해지는' 능동 → 현재분사"),
 VB(p, 'Such children quickly', 'choosing', 'choose', "정답 ▶ choosing\n이유: rather than 뒤 — 앞의 being arranged for(동명사)와 병렬 → 동명사"),
 VB(p, 'It should not be', 'trying', 'try', "정답 ▶ trying\n이유: 콤마 뒤 분사구문 — 목수가 조각하려고 '노력하는' 능동"),
 VB(p, 'The core of', 'helping', 'help', "정답 ▶ helping\n이유: 전치사 with의 목적어 — understanding과 and로 병렬된 동명사")]
VERB = [v for v in VERB if v['v'] != v['a'][0]]
ERR = [ER(p, 'If we, like gardeners', [('provide', 'will provide'), 'grow', 'developing'], 0, 'provide', "틀린 곳 ▶ ① will provide → provide\n이유: 조건 부사절(If ~)에서는 미래 대신 현재시제\n나머지 ▶ ② let + 목적어 + 동사원형 ✔ ③ 능동 분사구문 ✔"),
 ER(p, 'But if we, like carpenters', ['try', 'gradually', ('following', 'follow')], 2, 'following', "틀린 곳 ▶ ③ follow → following\n이유: become accustomed to + 동명사 (to는 전치사)\n나머지 ▶ ① 조건절 현재시제 ✔ ② 부사 gradually가 동사 lose 수식 ✔"),
 ER(p, 'Such children quickly', ['as', ('being arranged', 'arranging'), 'choosing'], 1, 'being arranged', "틀린 곳 ▶ ② arranging → being arranged\n이유: 아이들이 (부모에 의해) '마련받는' 수동 → being p.p.\n나머지 ▶ ① 접속사 as(~하면서) ✔ ③ rather than 뒤 동명사 병렬 ✔")]
SCR = [1, 3, 4, 5, 7]
ORDER = [[0, 1, 2, 3], [3, 4, 5, 6, 7]]
INSERT = [([2, 3, 4, 5], 1, "정답 ▶ ① (But if we, like carpenters ~ 문장)\n이유: 정원사형 아이들(Such children love life ~) → But 목수형이면 자율성을 잃음 → Such children(목수형 아이들)이 방향 감각을 잃음 — 두 번째 Such children이 가리킬 대상이 필요"),
 ([4, 5, 6, 7], 1, "정답 ▶ ① (As parents ~ 문장)\n이유: 목수형의 문제 → 그러니 부모 역할은 정원사여야(As parents ~) → It should not be ~의 It이 our role을 가리킴")]
ODD = [([1, 2, "Gardeners usually plant flowers in spring and harvest vegetables in autumn.", 3], 2, "정답 ▶ ③\n이유: 정원사는 '양육의 비유'예요. 실제 원예 계절 이야기는 흐름과 관계없어요.")]
BLANK = [BL(p, 'If we, like gardeners', 'at their own pace', ["at a fixed speed", "by our schedule", "in a hurry"], "정답 ▶ at their own pace (그들 자신의 속도로)\n이유: 정원사형 = 아이의 속도에 맞춤\n오답 ▶ 정해진 속도로 · 우리 일정대로 · 서둘러서 — 모두 목수형에 가까움"),
 BL(p, 'But if we, like carpenters', 'ideal', ["natural", "own", "random"], "정답 ▶ ideal (이상적인)\n이유: 목수는 '우리의 이상적인' 모습으로 형태를 만듦\n오답 ▶ natural 자연스러운(정원사형) · own · random 무작위의"),
 BL(p, 'Such children quickly', 'direction', ["humor", "balance", "taste"], "정답 ▶ direction (방향)\n이유: 길을 스스로 고르지 않음 → '방향' 감각을 잃음 — 마지막 문장 find their direction과 연결\n오답 ▶ humor · balance · taste")]
GRAM = [{'q': "빈칸에 알맞은 것은?<br><b>If we ______ children grow at their own pace, they will explore the world.</b>", 'opts': ["let", "will let", "letting", "to let"], 'ex': "정답 ▶ let\n이유: 조건 부사절에서는 미래 대신 현재시제"},
 {'q': "빈칸에 알맞은 것은?<br><b>They are used to ______ for by their parents.</b>", 'opts': ["being arranged", "arrange", "arranging", "be arranged"], 'ex': "정답 ▶ being arranged\n이유: be used to + 동명사, 의미상 수동 → being p.p."},
 {'q': "빈칸에 알맞은 것은?<br><b>Our role should be ______ of gardeners, not carpenters.</b>", 'opts': ["that", "those", "it", "this"], 'ex': "정답 ▶ that\n이유: 앞의 단수 명사 role을 받는 지시대명사 that (복수면 those)"},
 {'q': "빈칸에 알맞은 것은?<br><b>Such children love life, dare ______, and possess initiative.</b>", 'opts': ["to challenge", "challenging", "challenged", "to challenging"], 'ex': "정답 ▶ to challenge\n이유: dare + to부정사 '감히 ~하다'"}]
SUMQ = [SUM(p, "Parents should act like gardeners who let children grow at their own (A) ______, not like carpenters who (B) ______ them into an ideal image.", [
 "(A) pace – (B) shape", "(A) pace – (B) free", "(A) risk – (B) shape", "(A) cost – (B) guide", "(A) home – (B) push"],
 "정답 ▶ (A) pace – (B) shape\n(A) at their own pace(자신의 속도로) (B) shape children into our ideal image(이상적인 모습으로 형태를 만들다)\n오답 ▶ free 풀어 주다(목수형과 반대) · risk · cost · home 근거 없음",
 ["at their own pace", "shape” children into our ideal image"])]
