from jfw import *
R = PREP['36']['sents']; st = lambda x: x.split(') ', 1)[1] if x.startswith('(') else x
a4, b1 = R[4].split(' (B) ')
S = [R[0], b1, R[5], st(R[1]), R[2], R[3], a4, st(R[6]), R[7], R[8]]
p = load(36, '36번 · 글의 순서', sents=S)
VOCAB = words(36)
EXAM = [EXQ(36, '36. 주어진 글 다음에 이어질 글의 순서로 가장 적절한 것은?', p.order_q([0], {'A': [3, 4, 5, 6], 'B': [1, 2], 'C': [7, 8, 9]}), ORD, 1,
 "정답 ▶ ② (B)-(A)-(C)\n이유: 주어진 글 — 수학의 관심사는 숫자가 아니라 패턴·구조 → (B) 예를 들어(Take, for example) 스도쿠: 1~9 숫자를 한 번씩 → (A) But 숫자의 값은 상관없고 아홉 개의 다른 기호면 됨, 중요한 건 패턴 + 한 신문은 '수학은 필요 없다'며 퍼즐을 실음 → (C) 수학이라는 '생각'만으로도 풀이자를 겁줌 → 스도쿠를 할 수 있다면 수학을 할 수 있다\n오답 ▶ (A)의 the digits·these puzzles는 (B)의 스도쿠 설명 뒤 / (C)는 (A) 끝의 '수학 없음' 광고 문구에 대한 반응\n포인트 ▶ 지시어(these puzzles)와 연결어(But)로 순서 잡기", v=False),
 EXQ(36, '다음 글의 요지로 가장 적절한 것은?', p.full(), [
 "수학의 핵심은 숫자가 아니라 패턴이므로, 스도쿠를 풀 수 있다면 수학도 할 수 있다.", "스도쿠는 수학과 전혀 관계없는 논리 게임이다.", "수학을 잘하려면 숫자 계산을 많이 연습해야 한다.",
 "신문은 퍼즐 대신 수학 문제를 실어야 한다.", "예술 전시회는 그림과 조각만 다루어야 한다."], 0,
 "정답 ▶ ①\n이유: 첫 문장(수학의 관심사 = 패턴) + 마지막 문장 If you can do Sudoku, you can do maths!\n오답 ▶ ② 신문의 주장일 뿐, 필자는 반박함 ③ 숫자가 핵심이 아님 ④ 언급 없음 ⑤ 비유일 뿐"),
 EXQ(36, '다음 빈칸에 들어갈 말로 가장 적절한 것은?', p.blank('patterns, structures, symmetries and connections'), [
 "patterns, structures, symmetries and connections", "numbers, values, and calculations", "rules made by famous mathematicians", "games printed in newspapers", "art, painting and sculpture"], 0,
 "정답 ▶ ① 패턴, 구조, 대칭 그리고 연결\n이유: not numbers, but ~ + 뒤 It's the pattern that matters.\n오답 ▶ ② 숫자·값(not numbers와 반대) ③ 유명 수학자의 규칙 ④ 신문 게임 ⑤ 예술(비유 소재)")]
PICK1 = [PK(p, 'But the numerical values', 'irrelevant', 'essential', "정답 ▶ irrelevant (관련 없는)\n오답 ▶ essential (필수적인)\n이유: 아홉 개 글자나 모양이어도 됨 → 숫자의 값은 상관없음"),
 PK(p, 'It’s the pattern', 'pattern', 'number', "정답 ▶ pattern (패턴)\n오답 ▶ number (숫자)\n이유: 첫 문장 수학의 관심사는 숫자가 아니라 패턴"),
 PK(p, 'It seems that even', 'scare off', 'attract', "정답 ▶ scare off (겁주어 쫓아 버리다)\n오답 ▶ attract (끌어들이다)\n이유: 수학이 '망칠지도' 모른다는 생각 → 풀이자들이 겁을 먹음"),
 PK(p, 'It seems that even', 'spoiled', 'improved', "정답 ▶ spoiled (망쳐진)\n오답 ▶ improved (개선된)\n이유: 신문이 '수학은 필요 없어요!'라고 광고한 이유 → 수학이 망칠 거라는 생각"),
 PK(p, 'The objective is', 'once and only once', 'at least twice', "정답 ▶ once and only once (딱 한 번씩)\n오답 ▶ at least twice (적어도 두 번)\n이유: 스도쿠 규칙 — 1~9를 각 행·열·블록에 한 번씩")]
TF = [TF(p, "The main concerns of mathematics are numbers.", False, "The central concerns of mathematics are not numbers", "정답 ▶ F\n이유: 숫자가 아니라 패턴·구조·대칭·연결이에요."),
 TF(p, "In Sudoku, each row must contain all the digits from 1 to 9 once.", True, "contains all the digits from 1 to 9 once and only once", "정답 ▶ T\n이유: 각 행·열·블록에 1~9가 딱 한 번씩 들어가요."),
 TF(p, "Sudoku would not work if letters were used instead of numbers.", False, "They could be nine letters or nine shapes", "정답 ▶ F\n이유: 아홉 개의 글자나 모양이어도 돼요."),
 TF(p, "An Irish newspaper said no maths was involved in its puzzles.", True, "There’s no maths involved", "정답 ▶ T\n이유: '수학은 필요 없다'는 문구와 함께 퍼즐을 실었어요."),
 TF(p, "The writer believes people who can do Sudoku can do maths.", True, "If you can do Sudoku, you can do maths!", "정답 ▶ T\n이유: 스도쿠를 할 수 있다면 수학을 할 수 있다고 해요.")]
MC = [MC(p, "글의 내용과 일치하지 <u>않는</u> 것은?", [
 "The numerical values of the digits are important in Sudoku.", "Sudoku puzzles appear daily in newspapers.", "A Sudoku puzzle starts from a few given numbers or clues.",
 "The writer compares the newspaper’s slogan to an art exhibition slogan.", "The idea of mathematics can scare off potential solvers."],
 "정답 ▶ The numerical values of the digits are important in Sudoku.\n이유: the numerical values of the digits are irrelevant — 숫자의 값은 상관없어요.",
 [["스도쿠에서 숫자의 수치적 값이 중요하다.", "the numerical values of the digits are irrelevant", "✗ 반대"], ["스도쿠 퍼즐은 신문에 매일 실린다.", "the Sudoku puzzles that appear daily in newspapers", "일치"], ["스도쿠는 몇 개의 주어진 숫자나 단서로 시작한다.", "starting from a few given numbers or clues", "일치"],
  ["필자는 신문 문구를 미술 전시회 문구에 비유한다.", "‘No art involved, just painting and sculpture’", "일치"], ["수학이라는 생각이 잠재적 풀이자를 겁줄 수 있다.", "is enough to scare off potential solvers", "일치"]])]
PICK2 = [PK(p, 'But the numerical values', 'what is important', 'that is important', "정답 ▶ what\n이유: 주어 자리 + is important의 주어 없음 → 선행사를 품은 what"),
 PK(p, 'Take, for example', 'that appear', 'that appears', "정답 ▶ that appear\n이유: 선행사 the Sudoku puzzles(복수)"),
 PK(p, 'The objective is', 'to complete', 'completing', "정답 ▶ to complete\n이유: be동사 보어 to부정사(목표는 ~하는 것) — 관용적으로 to부정사가 자연스러움"),
 PK(p, 'The objective is', 'contains', 'contain', "정답 ▶ contains\n이유: each row, each column and each block — each가 이끄는 주어는 단수 취급"),
 PK(p, 'It’s the pattern', 'that matters', 'what matters', "정답 ▶ that\n이유: It is ~ that 강조 구문"),
 PK(p, 'It seems that even', 'be spoiled', 'spoil', "정답 ▶ be spoiled\n이유: 무언가가 수학에 의해 '망쳐지는'(수동) — by mathematics")]
VERB = [VB(p, 'The objective is', 'ensuring', 'ensure', "정답 ▶ ensuring\n이유: while + 분사(~하면서)"),
 VB(p, 'The objective is', 'starting', 'start', "정답 ▶ starting\n이유: 분사구문(~에서 시작하여)"),
 VB(p, 'One Irish daily paper', 'involved', 'involve', "정답 ▶ involved\n이유: no maths (is) involved — 관련된(수동) 과거분사")]
ERR = [ER(p, 'But the numerical values', ['irrelevant', ('what', 'that'), 'are'], 1, 'what', "틀린 곳 ▶ ② that → what\n이유: 주어 자리 + 뒤 절에 주어 없음 → what\n나머지 ▶ ① 형용사 보어 ✔ ③ there are + nine symbols(복수) ✔"),
 ER(p, 'It seems that even', [('that', 'what'), 'might be spoiled', 'to scare'], 0, 'that', "틀린 곳 ▶ ① what → that\n이유: It seems that ~ (~인 것 같다) — 뒤에 완전한 절\n나머지 ▶ ② 수동 ✔ ③ enough to부정사 ✔")]
SCR = [0, 1, 5, 9]
ORDER = [[0, 1, 2, 3, 4, 5], [6, 7, 8, 9]]
INSERT = [([0, 1, 2, 3], 3, "정답 ▶ ④ (But the numerical values ~ irrelevant)\n이유: 스도쿠 = 1~9 숫자를 한 번씩 채우는 게임 → But(하지만) 숫자의 값은 상관없다. 숫자가 나온 뒤에야 '숫자 값은 상관없다'는 반전이 가능")]
ODD = [([0, 1, "Many students find geometry harder than algebra.", 2], 2, "정답 ▶ ③\n이유: 스도쿠를 예로 수학 = 패턴이라고 설명하는 흐름이에요. 기하·대수 난이도 비교는 관계없어요.")]
BLANK = [BL(p, 'But the numerical values', 'nine distinct symbols', ["nine large numbers", "one correct answer", "many difficult clues"], "정답 ▶ nine distinct symbols (아홉 개의 서로 다른 기호)\n이유: 다음 문장 — 아홉 개 글자나 모양이어도 됨\n오답 ▶ 아홉 개의 큰 숫자(숫자 값은 상관없음) · 하나의 정답 · 많은 어려운 단서"),
 BL(p, 'One Irish daily paper', 'reasoning and logic', ["speed and luck", "memory and practice", "numbers and formulas"], "정답 ▶ reasoning and logic (추론과 논리)\n이유: '수학 없음'이라며 대신 쓰라고 한 것 → 추론과 논리(필자는 그것이 곧 수학이라고 봄)\n오답 ▶ 속도와 운 · 기억과 연습 · 숫자와 공식(수학 없음과 모순)")]
GRAM = [{'q': "빈칸에 알맞은 것은?<br><b>______ is important is that there are nine distinct symbols.</b>", 'opts': ["What", "That", "Which", "It"], 'ex': "정답 ▶ What\n이유: 주어 자리 + 불완전한 절 → What"},
 {'q': "빈칸에 알맞은 것은?<br><b>It's the pattern ______ matters.</b>", 'opts': ["that", "what", "where", "how"], 'ex': "정답 ▶ that\n이유: It is ~ that 강조"},
 {'q': "빈칸에 알맞은 것은?<br><b>Each row and each column ______ all the digits from 1 to 9.</b>", 'opts': ["contains", "contain", "containing", "to contain"], 'ex': "정답 ▶ contains\n이유: each가 이끄는 주어 → 단수"}]
SUMQ = [SUM(p, "Sudoku shows that mathematics is about (A) ______ rather than numbers, so people who can solve it should not be (B) ______ of maths.", [
 "(A) patterns – (B) afraid", "(A) patterns – (B) proud", "(A) values – (B) afraid", "(A) speed – (B) tired", "(A) art – (B) capable"],
 "정답 ▶ (A) patterns – (B) afraid\n(A) It's the pattern that matters. → patterns\n(B) 수학이라는 생각만으로 겁먹음(scare off) → 그럴 필요 없음 → afraid\n오답 ▶ proud 자랑스러운 · values 값(상관없음) · speed 속도 · art 예술",
 ["It’s the pattern that matters", "scare off potential solvers"])]
