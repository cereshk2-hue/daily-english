from jfw import *
p = load(20, '20번 · 필자의 주장')
VOCAB = words(20)
EXAM = [EXQ(20, '20. 다음 글에서 필자가 주장하는 바로 가장 적절한 것은?', p.full(), [
 "국제 문제 해결을 위해 국가 정체성을 강화해야 한다.", "국제 사회의 발전을 위해 세계 시민의 의무를 우선시해야 한다.", "세계 시민 정체성을 확립하려면 국가 간 협력을 확대해야 한다.",
 "세계 시민 교육을 통해 다른 문화를 존중하는 태도를 길러야 한다.", "세계인의 연결과 공통 과제를 고려해 세계 시민 정체성을 더해야 한다."], 4,
 "정답 ▶ ⑤ 세계인의 연결과 공통 과제를 고려해 세계 시민 정체성을 더해야 한다.\n이유: 주제문 Given the connections ~ and the common challenges we face, we need to layer global citizenship on to these other identities. 국가 시민 정체성이 역사 속에서 '더해졌듯이' 세계 시민 정체성도 기존 정체성 위에 '더해야(layer on to)' 한다는 주장이에요.\n오답 ▶ ① 국가 정체성 '강화'가 아니라 세계 시민 정체성을 '추가' ② 세계 시민 의무를 '우선시'하라는 말은 없음 — 오히려 가족·공동체·세계 모두에 의무가 있다고 함 ③ 국가 간 협력 이야기 없음 ④ 세계 시민 교육·문화 존중 이야기 없음\n포인트 ▶ layer A on to B = A를 B 위에 덧입히다(대체 replace가 아님!)", v=False),
 EXQ(20, '다음 글의 요지로 가장 적절한 것은?', p.full(), [
 "세계 시민 정체성은 기존의 정체성을 대체하는 것이 아니라 그 위에 더해지는 것이다.", "국민 국가는 인류 역사에서 가장 오래된 공동체 형태이다.", "가족과 종교에 대한 정체성은 시대가 바뀌면서 사라지고 있다.",
 "세계 시민이 되려면 자신의 국적을 포기해야 한다.", "정체성은 하나의 이야기로 통일될 때 가장 강해진다."], 0,
 "정답 ▶ ① 세계 시민 정체성은 기존의 정체성을 대체하는 것이 아니라 그 위에 더해지는 것이다.\n이유: we need to layer global citizenship on to these other identities + This doesn’t mean that global citizenship replaces these other identities.\n오답 ▶ ② 국민 국가는 인류 역사 대부분 동안 '존재하지 않았음'(nation-states didn’t exist) ③ 사라진다는 말 없음 — 그 위에 더해짐 ④ 국적 포기 → replace(대체)와 같은 오해 ⑤ There’s not a single story about our identities(정체성에 단 하나의 이야기는 없다)와 반대\n포인트 ▶ 요지 = 주제문 + This doesn’t mean ~(오해 바로잡기)"),
 EXQ(20, '다음 빈칸에 들어갈 말로 가장 적절한 것은?', p.blank('replaces'), [
 "replaces", "supports", "reflects", "includes", "follows"], 0,
 "정답 ▶ ① replaces (대체하다)\n이유: 앞 문장에서 세계 시민 정체성을 다른 정체성 '위에 덧입힌다(layer on to)'고 했으니, This doesn’t mean(그렇다고 ~라는 뜻은 아니다) 뒤에는 '대체한다'는 오해가 와야 자연스러워요. 이어서 정체성의 이야기는 하나가 아니라고 해요.\n오답 ▶ supports 지지하다 · reflects 반영하다 · includes 포함하다 · follows 따르다 → '그런 뜻은 아니다'로 부정할 이유가 없는 말\n포인트 ▶ This doesn’t mean that ~ = 예상되는 오해를 부정하는 표현")]
PICK1 = [PK(p, 'Some people are', 'skeptical', 'confident', "정답 ▶ skeptical (회의적인)\n오답 ▶ confident (확신하는)\n이유: but 뒤에 '사람들은 원래 국가 시민으로도 생각하지 않았다'며 반박하므로, 앞은 세계 시민 개념을 '의심하는' 사람들"),
 PK(p, 'After all', 'exist', 'collapse', "정답 ▶ exist (존재하다)\n오답 ▶ collapse (무너지다)\n이유: 인류 역사 대부분 동안 국민 국가는 아예 '존재하지' 않았기 때문에 국가 시민이라는 생각도 없었어요."),
 PK(p, 'The rise of', 'rise', 'fall', "정답 ▶ rise (부상, 등장)\n오답 ▶ fall (몰락)\n이유: 지난 몇 세기 동안 국민 국가가 '생겨나면서' 국가 시민 정체성이 더해졌어요."),
 PK(p, 'The rise of', 'add', 'remove', "정답 ▶ add (더하다)\n오답 ▶ remove (없애다)\n이유: 국가 시민 정체성을 가족·민족·종교 정체성에 '더했다' → 뒤에서 세계 시민도 같은 방식으로 더하자는 주장"),
 PK(p, 'Given the connections', 'common', 'private', "정답 ▶ common (공통의)\n오답 ▶ private (사적인)\n이유: 전 세계 사람들이 함께 직면한 '공통의' 과제 → 세계 시민 정체성이 필요한 이유"),
 PK(p, 'This doesn', 'replaces', 'complements', "정답 ▶ replaces (대체하다)\n오답 ▶ complements (보완하다)\n이유: doesn’t mean(~라는 뜻은 아니다)으로 부정되는 오해 = '대체'. 보완은 필자가 말하는 내용이라 부정할 필요가 없어요."),
 PK(p, 'Instead, it', 'obligations', 'complaints', "정답 ▶ obligations (의무)\n오답 ▶ complaints (불평)\n이유: 가족·공동체·세계 사람들에 대한 '의무'를 모두 지니기 때문에 정체성이 여러 겹이에요.")]
TF = [TF(p, "The writer says it is both necessary and possible to think of ourselves as global citizens.", True, "both necessary and possible to do so", "정답 ▶ T\n이유: 세계 시민이라고 생각하는 것은 필요하면서도 가능하다고 했어요.\n어휘 ▶ to do so = to think of ourselves as global citizens"),
 TF(p, "Everyone already accepts the idea of global citizenship.", False, "Some people are skeptical about the idea of global citizenship", "정답 ▶ F\n이유: 어떤 사람들은 세계 시민 개념에 회의적(skeptical)이에요."),
 TF(p, "Nation-states have existed for most of human history.", False, "for most of human history, nation-states didn’t exist", "정답 ▶ F\n이유: 인류 역사 대부분 동안 국민 국가는 존재하지 않았어요."),
 TF(p, "State citizenship was added to identities such as family and religion over the last few centuries.", True, "has led people to add state citizenship to other identities", "정답 ▶ T\n이유: 지난 몇 세기 동안 국민 국가의 부상으로 국가 시민 정체성이 가족·민족·종교 정체성에 더해졌어요."),
 TF(p, "The writer wants global citizenship to take the place of other identities.", False, "This doesn’t mean that global citizenship replaces these other identities", "정답 ▶ F\n이유: 세계 시민 정체성이 다른 정체성을 대체한다는 뜻이 아니라고 했어요.\n어휘 ▶ take the place of = replace"),
 TF(p, "According to the writer, we have obligations to people around the world as well as to our families.", True, "obligations to our families, those in our community, and those around the world", "정답 ▶ T\n이유: 가족, 공동체 사람들, 전 세계 사람들 모두에게 의무가 있어요.\n어휘 ▶ A as well as B = B뿐만 아니라 A도")]
MC = [MC(p, "글의 내용과 일치하지 <u>않는</u> 것은?", [
 "Our identities can be explained by just one story.", "Some people doubt the concept of global citizenship.", "People in the past did not see themselves as citizens of nation-states.",
 "The rise of nation-states added a new identity to existing ones.", "Connections between people worldwide are one reason for global citizenship."],
 "정답 ▶ Our identities can be explained by just one story.\n이유: There’s not a single story about our identities. (정체성에 단 하나의 이야기는 없다)\n오답 ▶ 나머지는 본문을 바꿔 쓴 일치 문장\n포인트 ▶ doubt ≒ be skeptical about · concept = idea · existing ones = other identities · worldwide = around the world",
 [["우리의 정체성은 단 하나의 이야기로 설명될 수 있다.", "There’s not a single story about our identities", "✗ 하나가 아님"], ["어떤 사람들은 세계 시민 개념을 의심한다.", "Some people are skeptical about the idea of global citizenship", "doubt ≒ be skeptical"], ["과거 사람들은 스스로를 국민 국가의 시민으로 보지 않았다.", "people didn’t think of themselves as citizens of nation-states", "see A as B = think of A as B"], ["국민 국가의 부상은 기존 정체성에 새 정체성을 더했다.", "has led people to add state citizenship to other identities", "existing = other"], ["전 세계 사람들 간의 연결은 세계 시민 의식의 한 이유이다.", "Given the connections between people around the world", "worldwide = around the world"]]),
 MC(p, "글의 내용과 <u>일치하는</u> 것은?", ["세계 시민 정체성을 다른 정체성 위에 쌓을 필요가 있다.", "국민 국가는 인류 역사 초기부터 존재했다.", "모든 사람이 세계 시민 개념에 동의한다.", "세계 시민 정체성은 가족 정체성을 대신한다.", "우리는 오직 가족에게만 의무를 진다."],
 "정답 ▶ 세계 시민 정체성을 다른 정체성 위에 쌓을 필요가 있다.\n이유: we need to layer global citizenship on to these other identities\n오답 ▶ ② 대부분의 역사 동안 존재하지 않음 ③ 회의적인 사람도 있음 ④ 대체(replace)하는 게 아님 ⑤ 공동체·전 세계 사람들에게도 의무\n포인트 ▶ layer A on to B = A를 B 위에 쌓다",
 [["", "we need to layer global citizenship on to these other identities", "일치 ✔"], ["", "nation-states didn’t exist", "존재 안 함"], ["", "Some people are skeptical", "회의적인 사람도"], ["", "doesn’t mean that global citizenship replaces", "대체 아님"], ["", "those in our community, and those around the world", "모두에게 의무"]])]
PICK2 = [PK(p, 'We might not', 'ourselves', 'us', "정답 ▶ ourselves\n이유: 주어 We와 전치사 of의 목적어가 같은 사람 → 재귀대명사 ourselves"),
 PK(p, 'We might not', 'to do so', 'doing so', "정답 ▶ to do\n이유: 가주어 it ~ 진주어 to부정사. it’s necessary and possible to do so"),
 PK(p, 'Some people are', 'themselves', 'them', "정답 ▶ themselves\n이유: 주어 people과 of의 목적어가 같은 사람 → 재귀대명사"),
 PK(p, 'The rise of', 'has led', 'have led', "정답 ▶ has\n이유: 주어의 핵은 The rise(단수). of nation-states ~ centuries는 수식어"),
 PK(p, 'The rise of', 'to add', 'adding', "정답 ▶ to add\n이유: lead + 목적어 + to부정사 (…가 ~하도록 이끌다)"),
 PK(p, 'Given the connections', 'Given', 'Give', "정답 ▶ Given\n이유: Given + 명사 = ~을 고려하면 (관용적 분사구문). 동사원형 Give로 시작하면 명령문이 되어 뒤 절과 연결이 안 돼요."),
 PK(p, 'Instead, it', 'those in our community', 'that in our community', "정답 ▶ those\n이유: '~한 사람들' = those (복수의 사람). that은 앞의 단수 명사를 받을 때만")]
VERB = [VB(p, 'The rise of', 'led', 'lead', "정답 ▶ led\n이유: has + p.p. 현재완료 (lead - led - led)"),
 VB(p, 'Given the connections', 'to layer', 'layer', "정답 ▶ to layer\n이유: need + to부정사 (~할 필요가 있다)"),
 VB(p, 'This doesn', 'replaces', 'replace', "정답 ▶ replaces\n이유: that절 주어 global citizenship(단수), 현재시제 → replaces")]
ERR = [ER(p, 'We might not', [('ourselves', 'us'), 'necessary', 'to do'], 0, 'ourselves', "틀린 곳 ▶ ① us → ourselves\n이유: 주어 We = 전치사 of의 목적어 → 재귀대명사\n나머지 ▶ ② both A and B, 형용사 보어 ✔ ③ 진주어 to부정사 ✔"),
 ER(p, 'The rise of', [('has', 'have'), 'to add', 'other'], 0, 'has', "틀린 곳 ▶ ① have → has\n이유: 주어 The rise(단수)\n나머지 ▶ ② lead + 목적어 + to부정사 ✔ ③ other + 복수명사 identities ✔"),
 ER(p, 'Instead, it', ['because', 'have', ('those', 'that')], 2, 'those', "틀린 곳 ▶ ③ that → those\n이유: ~한 사람들 = those (those in our community, those around the world 병렬)\n나머지 ▶ ① it’s because + 절 ✔ ② we have ✔")]
SCR = [0, 3, 4, 5, 7]
ORDER = [[1, 2, 3, 4], [4, 5, 6, 7]]
INSERT = [([2, 3, 4, 5], 2, "정답 ▶ ② (Given ~ 문장)\n이유: 국가 시민 정체성이 다른 정체성에 '더해졌다'(사례) → 그러니 세계 시민 정체성도 '더해야 한다'(주장) → This doesn’t mean(대체는 아님)으로 이어져요. This가 '덧입히는 것'을 가리켜요."),
 ([4, 5, 6, 7], 3, "정답 ▶ ③ (Instead ~ 문장)\n이유: 정체성에 단 하나의 이야기는 없다 → Instead(오히려) 우리는 가족·공동체·세계 모두에 의무가 있기 때문 → 앞의 부정 뒤에 Instead가 와요.")]
ODD = [([2, 3, "As a result, most people today feel that their family identity is no longer important.", 4], 2, "정답 ▶ ③\n이유: 국가 시민 정체성이 '더해졌다'는 흐름이고, 필자는 정체성이 대체되지 않는다고 말해요. 가족 정체성이 더 이상 중요하지 않다는 문장은 흐름과 반대예요.")]
BLANK = [BL(p, 'Some people are', 'skeptical', ["certain", "proud", "careful"], "정답 ▶ skeptical (회의적인)\n이유: but 뒤에서 반박(옛날엔 국가 시민 의식도 없었다)하므로 앞은 '의심하는' 태도\n오답 ▶ certain 확신하는 · proud 자랑스러운 · careful 조심스러운"),
 BL(p, 'Given the connections', 'layer', ["replace", "remove", "hide"], "정답 ▶ layer (덧입히다)\n이유: 국가 시민 정체성이 '더해졌듯' 세계 시민 정체성도 다른 정체성 위에 '얹어야' 해요. 바로 뒤 문장에서 대체(replace)는 아니라고 해요.\n오답 ▶ replace 대체하다 · remove 없애다 · hide 숨기다"),
 BL(p, 'There’s not', 'single', ["true", "long", "famous"], "정답 ▶ single (단 하나의)\n이유: 가족·공동체·세계에 대한 의무가 함께 있으니 정체성 이야기는 '하나가' 아니에요.\n오답 ▶ true 진실한 · long 긴 · famous 유명한")]
GRAM = [{'q': "빈칸에 알맞은 것은?<br><b>It’s both necessary and possible ______ so.</b>", 'opts': ["to do", "doing", "do", "done"], 'ex': "정답 ▶ to do\n이유: 가주어 it ~ 진주어 to부정사\n포인트 ▶ It is + 형용사 + to부정사"},
 {'q': "빈칸에 알맞은 것은?<br><b>The rise of nation-states ______ led people to add state citizenship.</b>", 'opts': ["has", "have", "having", "to have"], 'ex': "정답 ▶ has\n이유: 주어의 핵 rise(단수) → has. of nation-states에 속지 않기"},
 {'q': "빈칸에 알맞은 것은?<br><b>______ the challenges we face, we need to layer global citizenship on to other identities.</b>", 'opts': ["Given", "Give", "To give", "Gave"], 'ex': "정답 ▶ Given\n이유: Given + 명사 = ~을 고려하면 (= Considering)\n포인트 ▶ given ~ = considering ~ = taking ~ into consideration"},
 {'q': "빈칸에 알맞은 것은?<br><b>We have obligations to our families and ______ around the world.</b>", 'opts': ["those", "that", "them", "this"], 'ex': "정답 ▶ those\n이유: those (who are) around the world = 전 세계 사람들"}]
SUMQ = [SUM(p, "Just as state citizenship was (A) ______ to older identities, global citizenship should be layered on to them rather than (B) ______ them.", [
 "(A) added – (B) replacing", "(A) added – (B) supporting", "(A) compared – (B) replacing", "(A) opposed – (B) following", "(A) limited – (B) joining"],
 "정답 ▶ (A) added – (B) replacing\n(A) 국가 시민 정체성은 기존 정체성에 '더해졌다' → added\n(B) 세계 시민 정체성은 기존 정체성을 '대체하는' 것이 아니다 → replacing\n오답 ▶ compared 비교된 · opposed 반대된 · limited 제한된 / support 지지하다 · follow 따르다 · join 합류하다",
 ["add state citizenship to other identities", "This doesn’t mean that global citizenship replaces these other identities"])]
