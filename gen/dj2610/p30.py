from jfw import *
S = PREP['30']['sents'][:]; assert 'a smiling expression' in S[5]; S[5] = S[5].replace('a smiling expression', 'a grumpy expression')
p = load(30, '30번 · 어휘', sents=S)
VOCAB = words(30)
EXAM = [EXQ(30, '30. 다음 글의 밑줄 친 부분 중, 문맥상 낱말의 쓰임이 적절하지 않은 것은?', underlined(30, ['fail', 'more', 'believe', 'smiling', 'replacing']), [
 "①", "②", "③", "④", "⑤"], 3,
 "정답 ▶ ④ smiling → grumpy (언짢은)\n이유: 뒤 문장 You might not believe that they enjoyed ~ — 말(즐거웠다)과 표정이 '모순'되어야 믿지 않음 → 말은 즐거웠다는데 표정은 '언짢은' 상황\n오답 ▶ ① 비언어와 말이 안 맞으면 조종 시도는 실패(fail) ✔ ② 비언어를 언어보다 '더' 신뢰 ✔ ③ 눈길을 돌리고 억지웃음 → 말을 덜 '믿게' 됨 ✔ ⑤ 없는 동안 여러분을 '대신한' 것 ✔\n포인트 ▶ The same is probably true — 앞 예시(말 ≠ 표정)와 '같은' 구조여야 해요.", v=False),
 EXQ(30, '다음 글의 요지로 가장 적절한 것은?', p.full(), [
 "말과 비언어적 신호가 모순될 때 사람들은 비언어적 신호를 더 믿는다.", "말을 잘하는 사람이 다른 사람을 더 쉽게 설득한다.", "직장 동료와의 갈등은 솔직한 대화로 해결해야 한다.",
 "웃는 표정은 상대방의 신뢰를 얻는 가장 좋은 방법이다.", "비언어적 신호는 문화마다 다르게 해석된다."], 0,
 "정답 ▶ ① 말과 비언어적 신호가 모순될 때 사람들은 비언어적 신호를 더 믿는다.\n이유: 비언어 신호의 우위 → 모순되는 메시지 상황에서 특히 두드러짐 → people trust nonverbal messages more than verbal ones\n오답 ▶ ② 말로 조종하는 시도는 실패할 가능성 ③ 갈등 해결법 아님 ④ 웃는 표정 자체가 아니라 '일치'가 중요 ⑤ 문화 차이 없음\n포인트 ▶ conflicting messages = 언어 ≠ 비언어"),
 EXQ(30, '다음 빈칸에 들어갈 말로 가장 적절한 것은?', p.blank('nonverbal messages more than verbal ones'), [
 "nonverbal messages more than verbal ones", "verbal messages more than nonverbal ones", "written messages more than spoken ones", "friends more than colleagues", "smiles more than words of praise"], 0,
 "정답 ▶ ① 언어적 메시지보다 비언어적 메시지를 더\n이유: 비언어가 말과 안 맞으면 말로 조종하려는 시도가 실패 → 이유: 사람들은 '비언어'를 더 신뢰\n오답 ▶ ② 거꾸로 ③ 글/말 비교 아님 ④ 친구/동료 비교 아님 ⑤ 웃음이 아니라 비언어 전체\n포인트 ▶ This is because ~ = 앞 문장의 이유")]
PICK1 = [PK(p, 'A study by Eva', 'dominance', 'weakness', "정답 ▶ dominance (우위)\n오답 ▶ weakness (약함)\n이유: 사람들이 비언어를 더 믿음 → 비언어 신호의 '우위'"),
 PK(p, 'The phenomenon', 'pronounced', 'hidden', "정답 ▶ pronounced (두드러진)\n오답 ▶ hidden (숨겨진)\n이유: 메시지가 모순될 때 비언어 우위가 특히 '두드러짐'"),
 PK(p, 'The phenomenon', 'conflicting', 'matching', "정답 ▶ conflicting (모순되는)\n오답 ▶ matching (일치하는)\n이유: 괄호 설명 — 언어와 비언어 메시지 내용이 '다른(differ)' 상황"),
 PK(p, 'Attempts to manipulate', 'match', 'contradict', "정답 ▶ match (일치하다)\n오답 ▶ contradict (모순되다)\n이유: 비언어가 말과 '일치하지 않으면(does not match)' 실패 — not contradict면 일치한다는 뜻이 되어 반대"),
 PK(p, 'When somebody tells', 'less', 'more', "정답 ▶ less (덜)\n오답 ▶ more (더)\n이유: 눈길을 돌리고 억지웃음 → 말을 '덜' 믿게 됨"),
 PK(p, 'The same is probably', 'grumpy', 'cheerful', "정답 ▶ grumpy (언짢은)\n오답 ▶ cheerful (쾌활한)\n이유: 즐거웠다는 '말'과 모순되는 표정이어야 믿지 않음 — 원문항 ④번 포인트")]
TF = [TF(p, "Eva McMahan’s study showed that nonverbal signals are dominant.", True, "confirmed the dominance of nonverbal signals", "정답 ▶ T\n이유: 비언어 신호의 우위를 확인했어요."),
 TF(p, "The effect was weaker when verbal and nonverbal messages differed.", False, "was especially pronounced when adults found themselves in situations with conflicting messages", "정답 ▶ F\n이유: 메시지가 모순될 때 특히 '두드러졌어요'."),
 TF(p, "Trying to manipulate someone with words often fails if your body language does not match.", True, "are therefore likely to fail if the accompanying nonverbal communication does not match", "정답 ▶ T\n이유: 비언어가 말과 일치하지 않으면 실패할 가능성이 있어요."),
 TF(p, "People generally trust words more than body language.", False, "people trust nonverbal messages more than verbal ones", "정답 ▶ F\n이유: 비언어 메시지를 더 신뢰해요."),
 TF(p, "Looking away while saying something nice can make your words less believable.", True, "you are probably less inclined to believe their words", "정답 ▶ T\n이유: 눈길을 돌리고 억지웃음을 지으면 말을 덜 믿게 돼요."),
 TF(p, "Your colleague’s grumpy face makes you believe they enjoyed your work.", False, "You might not believe that they enjoyed replacing you", "정답 ▶ F\n이유: 언짢은 표정 때문에 즐거웠다는 말을 믿지 않아요.")]
MC = [MC(p, "글의 내용과 일치하지 <u>않는</u> 것은?", [
 "Verbal messages win when they conflict with nonverbal ones.", "Eva McMahan is a professor of speech communication.", "A forced smile can reduce trust in someone’s words.",
 "Nonverbal signals are trusted more than words.", "A colleague may say they were happy to take over your workload."],
 "정답 ▶ Verbal messages win when they conflict with nonverbal ones.\n이유: people trust nonverbal messages more than verbal ones (모순되면 비언어를 믿음)\n포인트 ▶ forced smile = 억지웃음 · take over = 넘겨받다",
 [["언어 메시지가 비언어 메시지와 모순되면 언어 메시지가 이긴다.", "people trust nonverbal messages more than verbal ones", "✗ 비언어 우위"], ["Eva McMahan은 발화 의사소통 교수이다.", "professor of speech communication", "일치"], ["억지웃음은 말에 대한 신뢰를 줄일 수 있다.", "are forcing a smile, you are probably less inclined to believe", "일치"], ["비언어 신호가 말보다 더 신뢰받는다.", "trust nonverbal messages more", "일치"], ["동료가 업무를 넘겨받아 즐거웠다고 말할 수 있다.", "they were happy to take over your workload", "일치"]]),
 MC(p, "글의 내용과 <u>일치하는</u> 것은?", ["비언어 우위 현상은 메시지가 모순될 때 특히 두드러졌다.", "Eva McMahan의 연구는 언어 신호의 우위를 확인했다.", "말로 다른 사람을 조종하는 것은 언제나 성공한다.", "억지웃음은 상대의 말을 더 믿게 만든다.", "동료는 웃는 얼굴로 기쁨을 표현했다."],
 "정답 ▶ 비언어 우위 현상은 메시지가 모순될 때 특히 두드러졌다.\n이유: was especially pronounced when adults found themselves in situations with conflicting messages\n오답 ▶ ② 비언어 ③ 실패할 가능성 ④ 덜 믿음 ⑤ 언짢은 표정",
 [["", "especially pronounced", "일치 ✔"], ["", "the dominance of nonverbal signals", "비언어"], ["", "likely to fail", "실패"], ["", "less inclined to believe", "덜"], ["", "a grumpy expression", "언짢은"]])]
PICK2 = [PK(p, 'The phenomenon', 'found themselves', 'found them', "정답 ▶ themselves\n이유: 주어 adults와 목적어가 같은 대상 → 재귀대명사"),
 PK(p, 'The phenomenon', 'in which', 'which', "정답 ▶ in which\n이유: 뒤가 완전한 절(the contents ~ differ) → 전치사 + 관계대명사"),
 PK(p, 'Attempts to manipulate', 'are', 'is', "정답 ▶ are\n이유: 주어 Attempts(복수), to manipulate ~ verbally는 수식어"),
 PK(p, 'Attempts to manipulate', 'accompanying', 'accompanied', "정답 ▶ accompanying\n이유: 비언어 의사소통이 말에 '동반하는' 능동 의미 → 현재분사(형용사)"),
 PK(p, 'When somebody tells', 'spending', 'to spend', "정답 ▶ spending\n이유: enjoy + 동명사"),
 PK(p, 'You might not believe', 'replacing', 'to replace', "정답 ▶ replacing\n이유: enjoy + 동명사")]
VERB = [VB(p, 'A study by Eva', 'confirmed', 'confirm', "정답 ▶ confirmed\n이유: 주어 A study, 과거에 확인한 사실 → 과거시제"),
 VB(p, 'Attempts to manipulate', 'spoken', 'speak', "정답 ▶ spoken\n이유: message를 꾸미는 과거분사 — '말해진' 메시지"),
 VB(p, 'When somebody tells', 'forcing', 'force', "정답 ▶ forcing\n이유: are looking away and are forcing — 진행형 병렬"),
 VB(p, 'The same is probably', 'to take', 'take', "정답 ▶ to take\n이유: 감정 형용사 happy + to부정사 (~해서 즐거운)")]
VERB = [v for v in VERB if v['v'] != v['a'][0]]
ERR = [ER(p, 'Attempts to manipulate', [('are', 'is'), 'to fail', 'does not match'], 0, 'are', "틀린 곳 ▶ ① is → are\n이유: 주어 Attempts(복수) — to manipulate another person verbally는 수식어\n나머지 ▶ ② be likely + to부정사 ✔ ③ 주어 communication(단수) → does ✔"),
 ER(p, 'When somebody tells', ['that', ('spending', 'to spend'), 'less'], 1, 'spending', "틀린 곳 ▶ ② to spend → spending\n이유: enjoy는 동명사만 목적어로 취함\n나머지 ▶ ① 명사절 접속사 that ✔ ③ less inclined(덜 ~하고 싶은) ✔"),
 ER(p, 'The phenomenon', [('pronounced', 'pronouncing'), 'themselves', 'in which'], 0, 'pronounced', "틀린 곳 ▶ ① pronouncing → pronounced\n이유: '두드러진' 상태를 나타내는 형용사 pronounced (be동사의 보어)\n나머지 ▶ ② 재귀대명사 ✔ ③ 전치사 + 관계대명사 ✔")]
SCR = [0, 2, 3, 4, 6]
ORDER = [[0, 1, 2, 3], [3, 4, 5, 6]]
INSERT = [([1, 2, 3, 4], 3, "정답 ▶ ③ (This is because ~ 문장)\n이유: 말로 조종하려는 시도는 실패 → 이유(This is because): 비언어를 더 신뢰 → 예시(When somebody ~)"),
 ([3, 4, 5, 6], 2, "정답 ▶ ② (The same is probably true ~ 문장)\n이유: 억지웃음 예시 → '마찬가지로'(The same) 동료 예시 → 그래서 그들이 즐거워했다고 믿지 않음")]
ODD = [([2, 3, "Learning a foreign language helps people understand other cultures.", 4], 2, "정답 ▶ ③\n이유: 말과 비언어가 모순되면 비언어를 믿는다는 흐름이에요. 외국어 학습 이야기는 관계없어요.")]
BLANK = [BL(p, 'A study by Eva', 'nonverbal', ["written", "musical", "scientific"], "정답 ▶ nonverbal (비언어적인)\n이유: 글 전체가 '비언어' 신호의 우위\n오답 ▶ written · musical · scientific"),
 BL(p, 'Attempts to manipulate', 'manipulate', ["thank", "comfort", "forgive"], "정답 ▶ manipulate (조종하다)\n이유: 말로 다른 사람을 '조종하려는' 시도는 비언어가 안 맞으면 실패\n오답 ▶ thank 감사하다 · comfort 위로하다 · forgive 용서하다"),
 BL(p, 'The same is probably', 'workload', ["salary", "vacation", "office"], "정답 ▶ workload (업무량)\n이유: 아파서 없는 동안 동료가 '업무량'을 떠맡음 → 마지막 문장 replacing you\n오답 ▶ salary · vacation · office")]
GRAM = [{'q': "빈칸에 알맞은 것은?<br><b>Attempts to change his mind ______ likely to fail.</b>", 'opts': ["are", "is", "being", "to be"], 'ex': "정답 ▶ are\n이유: 주어 Attempts(복수)"},
 {'q': "빈칸에 알맞은 것은?<br><b>They enjoyed ______ me while I was gone.</b>", 'opts': ["replacing", "to replace", "replace", "replaced"], 'ex': "정답 ▶ replacing\n이유: enjoy + 동명사"},
 {'q': "빈칸에 알맞은 것은?<br><b>Adults found ______ in situations with conflicting messages.</b>", 'opts': ["themselves", "them", "theirs", "they"], 'ex': "정답 ▶ themselves\n이유: 주어와 목적어가 같음 → 재귀대명사"},
 {'q': "빈칸에 알맞은 것은?<br><b>They were happy ______ over your workload.</b>", 'opts': ["to take", "taking", "take", "taken"], 'ex': "정답 ▶ to take\n이유: 감정 형용사 + to부정사(감정의 원인)"}]
SUMQ = [SUM(p, "When verbal and nonverbal messages (A) ______, people tend to (B) ______ the nonverbal ones.", [
 "(A) conflict – (B) trust", "(A) conflict – (B) ignore", "(A) match – (B) trust", "(A) match – (B) forget", "(A) repeat – (B) avoid"],
 "정답 ▶ (A) conflict – (B) trust\n(A) situations with conflicting messages (B) people trust nonverbal messages more\n오답 ▶ ignore 무시하다(반대) · match 일치하다: 일치할 때가 아니라 '모순'될 때 특히 두드러짐",
 ["conflicting messages", "people trust nonverbal messages more"])]
