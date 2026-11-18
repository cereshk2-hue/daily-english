from jfw import *
p = load(21, '21번 · 밑줄 함축 의미')
VOCAB = words(21)
EXAM = [EXQ(21, '21. 밑줄 친 a bird in the hand is worth two in the bush가 다음 글에서 의미하는 바로 가장 적절한 것은? [3점]', p.under([('', 'a bird in the hand is worth two in the bush', 'a bird in the hand is worth two in the bush')]), [
 "Lenders and borrowers benefit from each other.", "Spending money now is wiser than keeping it for later.", "The lender decides the interest rate for the borrower.",
 "Borrowing money involves the risk of damaging one’s credit.", "Money you have now is more valuable than the same amount later."], 4,
 "정답 ▶ ⑤ 지금 가진 돈은 나중의 같은 금액보다 더 가치 있다.\n이유: 돈을 빌려주면 ① 못 받을 위험 ② 직접 쓰지 못하는 기회비용 → 그래서 이자(시간의 가치)를 받음 → 손 안의 새 한 마리(지금의 돈) = 덤불 속 두 마리(나중의 더 많은 돈)\n오답 ▶ ① 서로 이익 — 논점 아님 ② 지금 '쓰는' 게 현명하다는 말 아님(가치 비교) ③ 이자율 결정 주체 이야기 없음 ④ 신용 손상 언급 없음\n포인트 ▶ This price factors in the value of time. (시간의 가치 감안)", v=False),
 EXQ(21, '다음 글의 주제로 가장 적절한 것은?', p.full(), [
 "how interest rates reflect the value of time", "why people should avoid borrowing money", "ways to pay back loans more quickly",
 "the history of banks and lending", "the dangers of spending money too early"], 0,
 "정답 ▶ ① 이자율이 시간의 가치를 어떻게 반영하는가\n이유: 이자율 = 상환받지 못할 위험 + 기회비용 → 기간이 길수록 커짐 → This price factors in the value of time.\n오답 ▶ ② 빌리지 말라는 조언 없음 ③ 빨리 갚는 방법 없음 ④ 은행 역사 없음 ⑤ 일찍 쓰는 것의 위험 아님\n포인트 ▶ reflect = factor in(감안하다)"),
 EXQ(21, '다음 빈칸에 들어갈 말로 가장 적절한 것은?', p.blank('the higher the chance'), [
 "the higher the chance", "the lower the risk", "the smaller the cost", "the faster the payment", "the safer the money"], 0,
 "정답 ▶ ① 가능성이 더 높아진다\n이유: The longer the term ~, the 비교급 ~ : 기간이 길수록 → 먼 미래(알 수 없음) → 못 받을 가능성 '더 높음'\n오답 ▶ ② 위험이 낮아짐(반대) ③ 비용이 작아짐(반대) ④⑤ 근거 없음\n포인트 ▶ The 비교급 ~, the 비교급 … (~할수록 더 …하다)")]
PICK1 = [PK(p, 'To see how', 'perception', 'reception', "정답 ▶ perception (인식)\n오답 ▶ reception (환영회, 수신)\n이유: 이자율이 시간에 대한 사람들의 '인식'에 무슨 일을 하는가"),
 PK(p, 'This rate tells', 'reflects', 'ignores', "정답 ▶ reflects (반영하다)\n오답 ▶ ignores (무시하다)\n이유: 빌려준 돈의 대가는 상환받지 못할 위험과 기회비용을 '반영'함"),
 PK(p, 'This rate tells', 'risk', 'hope', "정답 ▶ risk (위험)\n오답 ▶ hope (희망)\n이유: 상환받지 '못할' 위험"),
 PK(p, 'The longer the term', 'unknowable', 'predictable', "정답 ▶ unknowable (알 수 없는)\n오답 ▶ predictable (예측 가능한)\n이유: 먼 미래는 정의상 '알 수 없음' → 그래서 못 받을 가능성이 커짐"),
 PK(p, 'In order to make', 'worthwhile', 'pointless', "정답 ▶ worthwhile (가치 있는)\n오답 ▶ pointless (무의미한)\n이유: 빌려주는 사람에게 '가치 있게' 만들려면 돈에 가격(이자)이 있어야 함"),
 PK(p, 'In order to make', 'income', 'loss', "정답 ▶ income (수입)\n오답 ▶ loss (손실)\n이유: 이자는 빌린 사람에게 대가(cost), 빌려준 사람에게 '수입'")]
TF = [TF(p, "The rate of interest affects how people perceive time.", True, "what the rate of interest does to people’s perception of time", "정답 ▶ T\n이유: 이자율이 시간에 대한 인식에 영향을 줘요.\n어휘 ▶ perceive (동) 인식하다 ↔ perception (명)"),
 TF(p, "The interest rate reflects the risk of not being repaid.", True, "reflects the risk of you not being repaid", "정답 ▶ T\n이유: 상환받지 못할 위험을 반영해요."),
 TF(p, "A longer loan makes it more certain that you will be paid back.", False, "the higher the chance you won’t be paid back", "정답 ▶ F\n이유: 기간이 길수록 '못 받을' 가능성이 높아져요."),
 TF(p, "Lending money means you cannot spend that money yourself for a while.", True, "the opportunity cost of not spending that money yourself", "정답 ▶ T\n이유: 직접 쓰지 못하는 기회비용이 생겨요."),
 TF(p, "Interest is a cost to the lender and income to the borrower.", False, "a cost to the borrower and income to the lender", "정답 ▶ F\n이유: 빌린 사람(borrower)에게 비용, 빌려준 사람(lender)에게 수입 — 거꾸로예요."),
 TF(p, "The price of money takes the value of time into account.", True, "This price factors in the value of time", "정답 ▶ T\n이유: 돈의 가격은 시간의 가치를 감안해요.\n어휘 ▶ take ~ into account = factor in")]
MC = [MC(p, "글의 내용과 일치하지 <u>않는</u> 것은?", [
 "The future of a loan can be known exactly in advance.", "The interest rate in the example is 10 percent a year.", "Money that is lent has a cost.",
 "Lenders must wait longer for longer loans.", "Money needs a price to be worth lending."],
 "정답 ▶ The future of a loan can be known exactly in advance.\n이유: further into the future — which by definition is unknowable (미래는 정의상 알 수 없음)\n포인트 ▶ unknowable = cannot be known · worthwhile = worth ~ing",
 [["대출의 미래는 미리 정확히 알 수 있다.", "which by definition is unknowable", "✗ 알 수 없음"], ["예시의 이자율은 연 10퍼센트이다.", "an interest rate of 10 percent per year", "일치"], ["빌려준 돈에는 대가가 있다.", "the money lent has a cost", "일치"], ["기간이 긴 대출일수록 더 오래 기다려야 한다.", "the longer you will have to wait", "일치"], ["돈을 빌려줄 가치가 있으려면 가격이 필요하다.", "money has to have a price", "worth lending = worthwhile"]]),
 MC(p, "글의 내용과 <u>일치하는</u> 것은?", ["이자는 빌린 사람에게는 대가이다.", "예시에서 대출 기간은 10년이다.", "기회비용은 이자율과 관계없다.", "대출 기간이 짧을수록 상환받지 못할 위험이 커진다.", "돈의 가격은 시간의 가치와 무관하다."],
 "정답 ▶ 이자는 빌린 사람에게는 대가이다.\n이유: a cost to the borrower and income to the lender\n오답 ▶ ② 5년 ③ 이자율이 기회비용을 반영 ④ 길수록 ⑤ 시간의 가치를 감안",
 [["", "a cost to the borrower", "일치 ✔"], ["", "for five years", "5년"], ["", "the opportunity cost", "반영"], ["", "The longer the term of the loan", "길수록"], ["", "factors in the value of time", "감안"]])]
PICK2 = [PK(p, 'To see how', 'changes', 'change', "정답 ▶ changes\n이유: 의문사절의 주어 borrowing and lending(빌리고 빌려주는 '일' 하나의 활동) → 단수 changes"),
 PK(p, 'Imagine you are', 'lending', 'lent', "정답 ▶ lending\n이유: are + -ing 진행형 (빌려주고 있다)"),
 PK(p, 'This rate tells', 'lent', 'lending', "정답 ▶ lent\n이유: the money를 뒤에서 꾸미는 과거분사 — 돈이 '빌려진' 수동"),
 PK(p, 'This rate tells', 'that reflects', 'what reflects', "정답 ▶ that\n이유: 선행사 a cost가 있음 → 주격 관계대명사 that (what은 선행사 포함)"),
 PK(p, 'The longer the term', 'which', 'what', "정답 ▶ which\n이유: 대시 뒤 삽입, 앞의 the future를 받는 관계대명사 which"),
 PK(p, 'In order to make', 'worthwhile', 'worthwhilely', "정답 ▶ worthwhile\n이유: make + 목적어(this) + 형용사 보어")]
VERB = [VB(p, 'This rate tells', 'tells', 'tell', "정답 ▶ tells\n이유: 주어 This rate(단수), 현재시제"),
 VB(p, 'This rate tells', 'being', 'be', "정답 ▶ being\n이유: 전치사 of 뒤 동명사, 의미상 주어 you가 '상환받는' 수동 → being repaid"),
 VB(p, 'The longer the term', 'spending', 'spend', "정답 ▶ spending\n이유: 전치사 before 뒤 동명사"),
 VB(p, 'In order to make', 'has', 'have', "정답 ▶ has\n이유: 주어 money(셀 수 없는 명사 → 단수), has to = ~해야 한다")]
VERB = [v for v in VERB if v['v'] != v['a'][0]]
ERR = [ER(p, 'This rate tells', ['lent', ('reflects', 'reflect'), 'being repaid'], 1, 'reflects', "틀린 곳 ▶ ② reflect → reflects\n이유: 관계대명사 that의 선행사 a cost(단수) → reflects\n나머지 ▶ ① 과거분사 lent(빌려진 돈) ✔ ③ 상환받는 수동 → being repaid ✔"),
 ER(p, 'The longer the term', [('the higher', 'the highest'), 'further', 'the longer'], 0, 'the higher', "틀린 곳 ▶ ① the highest → the higher\n이유: The 비교급 ~, the 비교급 … 구문 — 최상급을 쓸 수 없음\n나머지 ▶ ② 거리·정도의 비교급 further ✔ ③ the longer ✔"),
 ER(p, 'In order to make', [('to make', 'making'), 'has', 'income'], 0, 'to make', "틀린 곳 ▶ ① making → to make\n이유: in order + to부정사 (~하기 위해서)\n나머지 ▶ ② 주어 money(단수) → has ✔ ③ 명사 income ✔")]
SCR = [0, 2, 4, 5, 6]
ORDER = [[0, 1, 2, 3], [3, 4, 5, 6]]
INSERT = [([2, 3, 4, 5], 2, "정답 ▶ ② (In order to make ~ 문장)\n이유: 위험·기다림이 커짐(문제) → 이것(this)을 가치 있게 만들려면 돈에 가격이 필요 → This price(이 가격)가 시간의 가치를 감안"),
 ([3, 4, 5, 6], 3, "정답 ▶ ③ (This price factors in ~ 문장)\n이유: 돈에 가격이 있어야 함 → This price(그 가격)는 시간의 가치를 감안 → 달리 말하면(To put it another way) 손 안의 새")]
ODD = [([2, 3, "Many people today prefer using credit cards to carrying cash.", 4], 2, "정답 ▶ ③\n이유: 이자율이 위험·기회비용·시간의 가치를 반영한다는 흐름이에요. 신용카드 선호 이야기는 관계없어요.")]
BLANK = [BL(p, 'This rate tells', 'opportunity cost', ["shipping cost", "tax rate", "credit score"], "정답 ▶ opportunity cost (기회비용)\n이유: 그 돈을 직접 '쓰지 못하는' 데서 생기는 비용 = 기회비용\n오답 ▶ 배송비 · 세율 · 신용 점수"),
 BL(p, 'In order to make', 'price', ["limit", "name", "color"], "정답 ▶ price (가격)\n이유: 빌린 사람에게 대가, 빌려준 사람에게 수입 = 돈의 '가격'(이자)\n오답 ▶ limit · name · color"),
 BL(p, 'This price factors', 'time', ["friendship", "health", "beauty"], "정답 ▶ time (시간)\n이유: 기간이 길수록 위험·기다림이 커짐 → 이자는 '시간'의 가치를 감안\n오답 ▶ friendship · health · beauty")]
GRAM = [{'q': "빈칸에 알맞은 것은?<br><b>The longer the term of the loan, ______ the risk.</b>", 'opts': ["the higher", "higher", "the highest", "high"], 'ex': "정답 ▶ the higher\n이유: The 비교급 ~, the 비교급 … (~할수록 더 …하다)"},
 {'q': "빈칸에 알맞은 것은?<br><b>The cost reflects the risk of you not ______ repaid.</b>", 'opts': ["being", "be", "been", "to be"], 'ex': "정답 ▶ being\n이유: 전치사 of + (의미상 주어 you) + not + 동명사 수동 being p.p."},
 {'q': "빈칸에 알맞은 것은?<br><b>A bird in the hand is ______ two in the bush.</b>", 'opts': ["worth", "worthy", "worthwhile", "worths"], 'ex': "정답 ▶ worth\n이유: worth + 명사(구) '~의 가치가 있는' (worthy는 of와 함께)"},
 {'q': "빈칸에 알맞은 것은?<br><b>The future, ______ by definition is unknowable, makes lending risky.</b>", 'opts': ["which", "what", "that", "who"], 'ex': "정답 ▶ which\n이유: 콤마 뒤 계속적 용법, 사물 선행사 → which (that 불가)"}]
SUMQ = [SUM(p, "Interest rates show that money has a (A) ______ over time, because lending involves risk and a delay in (B) ______ the money oneself.", [
 "(A) cost – (B) spending", "(A) cost – (B) earning", "(A) limit – (B) spending", "(A) shape – (B) printing", "(A) color – (B) hiding"],
 "정답 ▶ (A) cost – (B) spending\n(A) the money lent has a cost (B) the opportunity cost of not spending that money yourself / wait before spending the money yourself\n오답 ▶ earning 버는 것: 빌려준 사람은 이자로 '번다' — 지연되는 건 '쓰는' 것",
 ["the money lent has a cost", "before spending the money yourself"])]
