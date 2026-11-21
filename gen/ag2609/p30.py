from jfw import *
S = PREP['30']['sents'][:]; assert S[10].endswith('easier by chopping up a natural train of thought.'); S[10] = S[10].replace('easier', 'harder')
p = load(30, '30번 · 어휘', sents=S)
VOCAB = words(30)
EXAM = [EXQ(30, '30. 다음 글의 밑줄 친 부분 중, 문맥상 낱말의 쓰임이 적절하지 않은 것은?', underlined(30, ['visual', 'inviting', 'damage', 'annoying', 'easier']), ["①", "②", "③", "④", "⑤"], 4,
 "정답 ▶ ⑤ easier → harder\n이유: 동사 없는 아주 작은 단락들은 자연스러운 생각의 흐름을 잘라 버리므로(chopping up a natural train of thought) 독자의 일을 '더 어렵게' 만든다\n오답 ▶ ① 눈을 먼저 사로잡으니 글쓰기는 '시각적' ✔ ② whereas(반면) 뒤 긴 덩어리는 읽기를 꺼리게 함 ↔ 짧은 단락은 '매력적' ✔ ③ 잦은 단락 나누기가 요지 전개를 '해칠' 거라는 걱정 ✔ ④ 너무 지나치지 말라 → 아주 작은 단락의 연속도 긴 단락만큼 '짜증스럽다' ✔\n포인트 ▶ But don't go too far. 이후는 아주 작은 단락의 '단점' 이야기", v=False),
 EXQ(30, '다음 글의 요지로 가장 적절한 것은?', p.full(), [
 "단락은 짧게 쓰되, 생각의 흐름이 끊길 만큼 잘게 나누지는 말아야 한다.", "신문 기사는 긴 단락으로 써야 독자가 집중할 수 있다.", "글은 내용보다 겉모양이 더 중요하다.",
 "단락을 자주 나누면 요지 전개가 반드시 망가진다.", "현대 기자들의 짧은 문장은 기사를 이해하기 쉽게 만든다."], 0,
 "정답 ▶ ① 단락은 짧게 쓰되, 생각의 흐름이 끊길 만큼 잘게 나누지는 말아야 한다.\n이유: Keep your paragraphs short.(주제문) + But don't go too far.(아주 작은 단락의 연속은 생각의 흐름을 잘라 버림)\n오답 ▶ ② 신문 단락은 두세 문장(짧게) ③ 시각적이라는 말은 있지만 내용보다 중요하다는 말은 없음 ④ 걱정하지 말라고 함(이점이 더 큼) ⑤ 오히려 독자의 일을 더 어렵게 만듦"),
 EXQ(30, '다음 빈칸에 들어갈 말로 가장 적절한 것은?', p.blank('a natural train of thought'), [
 "a natural train of thought", "the length of the article", "the number of readers", "the price of newspapers", "the rules of grammar"], 0,
 "정답 ▶ ① a natural train of thought (자연스러운 생각의 흐름)\n이유: 동사도 없는 아주 작은 단락들이 이어지면 생각이 뚝뚝 끊김 → 독자의 일이 더 어려워짐\n오답 ▶ ② 기사 길이 ③ 독자 수 ④ 신문 가격 ⑤ 문법 규칙 — 모두 독자의 일을 어렵게 만드는 이유가 아님")]
PICK1 = [PK(p, 'Writing is visual', 'visual', 'verbal', "정답 ▶ visual (시각적인)\n오답 ▶ verbal (말의)\n이유: 뇌보다 '눈'을 먼저 사로잡는다 → 시각적"),
 PK(p, 'Short paragraphs put', 'inviting', 'tiring', "정답 ▶ inviting (매력적인)\n오답 ▶ tiring (피곤하게 하는)\n이유: whereas 뒤 긴 덩어리는 읽기를 꺼리게 함 ↔ 짧은 단락은 매력적"),
 PK(p, 'You may think', 'damage', 'improve', "정답 ▶ damage (해치다)\n오답 ▶ improve (개선하다)\n이유: 바로 뒤 '이 두려움(this fear)' → 해칠 거라는 걱정"),
 PK(p, 'Don’t worry', 'gains', 'losses', "정답 ▶ gains (이점)\n오답 ▶ losses (손실)\n이유: 걱정하지 마라 → '이점'이 위험보다 훨씬 큼"),
 PK(p, 'A succession', 'annoying', 'pleasant', "정답 ▶ annoying (짜증스러운)\n오답 ▶ pleasant (즐거운)\n이유: 너무 긴 단락만큼 → 둘 다 '나쁜' 것"),
 PK(p, 'Actually they make', 'harder', 'easier', "정답 ▶ harder (더 어려운)\n오답 ▶ easier (더 쉬운)\n이유: 생각의 흐름을 잘라 버림 → 독자의 일이 더 어려워짐 — 원문항 ⑤번")]
TF = [TF(p, "Writing catches the eye before it catches the brain.", True, "it catches the eye before it has a chance to catch the brain", "정답 ▶ T\n이유: 뇌를 사로잡기 전에 눈을 사로잡아요."),
 TF(p, "A long chunk of type encourages readers to start reading.", False, "a long chunk of type can discourage a reader from even starting to read", "정답 ▶ F\n이유: 긴 활자 덩어리는 읽기 시작하는 것조차 꺼리게 해요."),
 TF(p, "Newspaper paragraphs should be only two or three sentences long.", True, "Newspaper paragraphs should be only two or three sentences long", "정답 ▶ T\n이유: 신문 활자는 폭이 좁아 금방 길어지기 때문이에요."),
 TF(p, "The New Yorker is not afraid of frequent paragraphing.", False, "Obviously The New Yorker is obsessed by this fear", "정답 ▶ F\n이유: The New Yorker는 이 두려움에 사로잡혀 있어요(그래서 단락이 길어요)."),
 TF(p, "Too many tiny paragraphs can break up a natural train of thought.", True, "chopping up a natural train of thought", "정답 ▶ T\n이유: 아주 작은 단락들은 자연스러운 생각의 흐름을 잘라 버려요.")]
MC = [MC(p, "글의 내용과 일치하지 <u>않는</u> 것은?", [
 "The writer recommends writing as many tiny paragraphs as possible.", "The writer says the benefits of short paragraphs are greater than the risks.", "Newspaper type is set in a narrow width.",
 "Some modern journalists write tiny paragraphs without verbs.", "Short paragraphs leave space around the writing."],
 "정답 ▶ The writer recommends writing as many tiny paragraphs as possible.\n이유: But don't go too far. — 아주 작은 단락의 연속은 너무 긴 단락만큼 짜증스러워요.\n어휘 ▶ as ~ as possible 가능한 한 ~",
 [["필자는 아주 작은 단락을 가능한 한 많이 쓰라고 권한다.", "But don’t go too far.", "✗ 지나치지 말라"], ["필자는 짧은 단락의 이점이 위험보다 크다고 말한다.", "the gains far outweigh the hazards", "일치"], ["신문 활자는 좁은 폭으로 짜인다.", "newspaper type is set in a narrow width", "일치"],
  ["일부 현대 기자들은 동사 없는 아주 작은 단락을 쓴다.", "verbless wonders — written by modern journalists", "일치"], ["짧은 단락은 글 주변에 여백을 남긴다.", "Short paragraphs put air around what you write", "일치"]])]
PICK2 = [PK(p, 'Keep your paragraphs', 'short', 'shortly', "정답 ▶ short\n이유: keep + 목적어 + 형용사(목적격보어) — 부사 X"),
 PK(p, 'Writing is visual', 'to catch', 'catching', "정답 ▶ to catch\n이유: a chance를 꾸미는 형용사적 to부정사"),
 PK(p, 'Short paragraphs put', 'what', 'that', "정답 ▶ what\n이유: 전치사 around의 목적어 + 뒤 절에 목적어 없음(you write ___) → 선행사를 품은 what"),
 PK(p, 'Short paragraphs put', 'starting', 'to start', "정답 ▶ starting\n이유: discourage A from -ing — 전치사 from 뒤 동명사"),
 PK(p, 'Newspaper paragraphs', 'is set', 'sets', "정답 ▶ is set\n이유: 활자가 좁은 폭으로 '짜이는' 것 → 수동태"),
 PK(p, 'A succession', 'is as', 'are as', "정답 ▶ is\n이유: 주어의 핵은 A succession(단수) — of tiny paragraphs는 수식어"),
 PK(p, 'I’m thinking', 'written', 'writing', "정답 ▶ written\n이유: 단락들이 기자들에 의해 '쓰인'(수동) → 과거분사")]
VERB = [VB(p, 'Actually they make', 'chopping', 'chop', "정답 ▶ chopping\n이유: 전치사 by 뒤 동명사 (~함으로써)"),
 VB(p, 'I’m thinking', 'trying', 'try', "정답 ▶ trying\n이유: 기자들이 '애쓰는'(능동) → modern journalists를 꾸미는 현재분사"),
 VB(p, 'Short paragraphs put', 'inviting', 'invite', "정답 ▶ inviting\n이유: look + 형용사 보어 — '매력적인'(inviting)")]
ERR = [ER(p, 'Short paragraphs put', [('what', 'that'), 'make', 'inviting'], 0, 'what', "틀린 곳 ▶ ① that → what\n이유: around의 목적어 자리 + you write 뒤에 목적어가 없음 → 선행사 없는 관계대명사 what\n나머지 ▶ ② put과 병렬인 make ✔ ③ look + 형용사 ✔"),
 ER(p, 'A succession', ['tiny', ('is', 'are'), 'annoying'], 1, 'is', "틀린 곳 ▶ ② are → is\n이유: 주어 A succession(단수)에 수 일치\n나머지 ▶ ① 형용사 tiny ✔ ③ as + 형용사 + as, 짜증나게 '하는' annoying ✔")]
SCR = [0, 1, 6, 8, 10]
ORDER = [[0, 1, 2, 3], [7, 8, 9, 10]]
INSERT = [([5, 6, 7, 8], 2, "정답 ▶ ③ (But don't go too far.)\n이유: 걱정 마라, 이점이 위험보다 크다(짧은 단락 찬성) → But(하지만) 너무 지나치지는 마라 → 아주 작은 단락의 연속도 짜증스럽다. 흐름이 '찬성 → 경고'로 바뀌는 곳")]
ODD = [([1, 2, "Many writers today prefer typing on a computer to writing by hand.", 3], 2, "정답 ▶ ③\n이유: 짧은 단락이 왜 좋은지(시각적·여백·신문 단락) 설명하는 흐름이에요. 컴퓨터 타이핑 선호 이야기는 관계없어요.")]
BLANK = [BL(p, 'Writing is visual', 'the eye', ["the ear", "the heart", "the hand"], "정답 ▶ the eye (눈)\n이유: 글쓰기는 '시각적' → 뇌보다 '눈'을 먼저 사로잡음\n오답 ▶ 귀 · 마음 · 손"),
 BL(p, 'Don’t worry', 'outweigh', ["equal", "hide", "follow"], "정답 ▶ outweigh (~보다 크다)\n이유: 걱정하지 마라 → 이점이 위험을 '훨씬 능가'\n오답 ▶ 같다 · 숨기다 · 뒤따르다 — far(훨씬)와 함께 걱정할 필요 없는 이유가 되지 않음")]
GRAM = [{'q': "빈칸에 알맞은 것은?<br><b>Keep your paragraphs ______.</b>", 'opts': ["short", "shortly", "shortness", "to short"], 'ex': "정답 ▶ short\n이유: keep + 목적어 + 형용사"},
 {'q': "빈칸에 알맞은 것은?<br><b>A long chunk of type can discourage a reader from ______ to read.</b>", 'opts': ["starting", "start", "to start", "started"], 'ex': "정답 ▶ starting\n이유: discourage A from -ing"},
 {'q': "빈칸에 알맞은 것은?<br><b>Short paragraphs put air around ______ you write.</b>", 'opts': ["what", "that", "which", "it"], 'ex': "정답 ▶ what\n이유: 전치사의 목적어 + 불완전한 절 → what"},
 {'q': "빈칸에 알맞은 것은?<br><b>A succession of tiny paragraphs ______ as annoying as a long one.</b>", 'opts': ["is", "are", "be", "being"], 'ex': "정답 ▶ is\n이유: 주어 핵 succession(단수)"}]
SUMQ = [SUM(p, "Paragraphs should be kept (A) ______ to attract readers, but making them too tiny can (B) ______ the natural flow of thought.", [
 "(A) short – (B) break", "(A) short – (B) improve", "(A) long – (B) break", "(A) colorful – (B) speed", "(A) formal – (B) guide"],
 "정답 ▶ (A) short – (B) break\n(A) Keep your paragraphs short. → short\n(B) 아주 작은 단락은 생각의 흐름을 잘라 버림(chopping up) → break\n오답 ▶ improve 개선하다(반대) · long 긴(반대) · colorful 화려한 · formal 격식 있는",
 ["Keep your paragraphs short", "chopping up a natural train of thought"])]
