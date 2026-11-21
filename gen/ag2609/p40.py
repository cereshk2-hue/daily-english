from jfw import *
R = PREP['40']['sents']; K = PREP['40']['ko']
S = R[:4] + [R[4] + ' ' + R[5]] + R[6:9] + [R[9].replace(' ??', '').strip()]
p = mk(40, '40번 · 요약문', S, K[:9])
VOCAB = words(40)
SUMS = "Self-esteem works as a monitoring mechanism that signals that there might be (A) <u>　　　　　</u> in people’s social bonds, allowing them to adjust their behavior to enhance (B) <u>　　　　　</u>."
EXAM = [EXQ(40, '40. 다음 글의 내용을 한 문장으로 요약하고자 한다. 빈칸 (A), (B)에 들어갈 말로 가장 적절한 것은?', p.full() + box(SUMS), [
 "(A) problems – (B) relationships", "(A) improvements – (B) interactions", "(A) improvements – (B) adaptation", "(A) patterns – (B) comfort", "(A) problems – (B) worry"], 0,
 "정답 ▶ ① (A) problems – (B) relationships\n(A) 관계적 가치가 떨어지거나 낮다는 것을 탐지하면 경보 → 사회적 유대에 '문제'가 있을지 모른다는 신호 → problems\n(B) 관계를 바로잡기 위해 행동을 조정(adjust my behaviors to fix the relationship) → '관계'를 향상 → relationships\n오답 ▶ improvements 개선(경보는 위협을 알림) · adaptation 적응 · comfort 편안함 · worry 걱정(향상시킬 대상이 아님)\n포인트 ▶ alarm·threat = problems / fix the relationship = enhance relationships", v=False),
 EXQ(40, '다음 글의 주제로 가장 적절한 것은?', p.full(), [
 "self-esteem as a system for monitoring social relationships", "ways to raise self-esteem quickly", "why people avoid social contact",
 "the danger of thinking about relationships too much", "how the brain stores memories"], 0,
 "정답 ▶ ① 사회적 관계를 감시하는 체계로서의 자아존중감\n이유: 진화적 관점에서 자아존중감은 관계의 질을 감시하는 기제 → 경보 → 행동 조정\n오답 ▶ ② 높이는 방법 없음 ③ 언급 없음 ④ 지속적 점검은 정상(normal) ⑤ 기억 저장 아님"),
 EXQ(40, '다음 빈칸에 들어갈 말로 가장 적절한 것은?', p.blank('nonconsciously'), [
 "nonconsciously", "loudly", "only at night", "very slowly", "only in childhood"], 0,
 "정답 ▶ ① nonconsciously (무의식적으로)\n이유: 경보가 울리면 위협이 '의식적 인식(conscious awareness)'으로 밀려 들어옴 → 그 전까지는 무의식적으로 작동\n오답 ▶ ② 시끄럽게 ③ 밤에만 ④ 아주 천천히 ⑤ 어릴 때만")]
PICK1 = [PK(p, 'The system monitors', 'alarm', 'reward', "정답 ▶ alarm (경보)\n오답 ▶ reward (보상)\n이유: 포함 상태의 변화에 대해 '경계시키는(alerts)' 것 → 경보"),
 PK(p, 'The monitoring system generally', 'falling', 'rising', "정답 ▶ falling (떨어지는)\n오답 ▶ rising (올라가는)\n이유: falling or low — 관계적 가치가 낮아질 때 경보"),
 PK(p, 'When the alarm bell rings', 'threat', 'gift', "정답 ▶ threat (위협)\n오답 ▶ gift (선물)\n이유: 경보가 울림 → 사회적 유대에 대한 '위협'"),
 PK(p, 'It also makes sense', 'minimizing rejection', 'maximizing rejection', "정답 ▶ minimizing (최소화하는)\n오답 ▶ maximizing (최대화하는)\n이유: 거절은 줄이고(minimize) 수용은 늘리는(enhance)"),
 PK(p, 'The continuous scanning', 'normal', 'harmful', "정답 ▶ normal (정상적인)\n오답 ▶ harmful (해로운)\n이유: a part of being human — 인간다움의 한 부분")]
TF = [TF(p, "Self-esteem developed to monitor the quality of our relationships.", True, "self-esteem has developed as a monitoring mechanism for the quality of our relationships", "정답 ▶ T\n이유: 진화적으로 관계의 질을 감시하는 기제로 발달했어요."),
 TF(p, "The monitoring system always works consciously.", False, "generally operates nonconsciously", "정답 ▶ F\n이유: 보통은 무의식적으로 작동해요."),
 TF(p, "When the alarm rings, we evaluate the situation consciously.", True, "is pushed into conscious awareness and we evaluate the situation", "정답 ▶ T\n이유: 위협이 의식으로 밀려 들어와 상황을 평가해요."),
 TF(p, "Constantly scanning our social value is abnormal.", False, "The continuous scanning is normal", "정답 ▶ F\n이유: 지속적인 점검은 정상이에요."),
 TF(p, "We search the environment for cues to assess our social value.", True, "searching for cues from the environment to assess our value", "정답 ▶ T\n이유: 환경에서 단서를 찾아 사회적 가치를 평가해요.")]
MC = [MC(p, "글의 내용과 일치하지 <u>않는</u> 것은?", [
 "Relationships have little value for human survival.", "The system watches other people’s reactions to our behaviors.", "The alarm alerts us to changes in our inclusion status.",
 "We may ask whether we need to adjust our behaviors.", "We developed mechanisms to minimize rejection."],
 "정답 ▶ Relationships have little value for human survival.\n이유: such a high value for survival closely tied with relationships — 관계는 생존에 매우 중요해요.",
 [["관계는 인간의 생존에 별 가치가 없다.", "such a high value for survival closely tied with relationships", "✗ 반대"], ["이 체계는 우리 행동에 대한 남의 반응을 감시한다.", "monitors other people’s reactions to our behaviors", "일치"],
  ["경보는 포함 상태의 변화를 알려 준다.", "alerts us to any possible changes in our inclusion status", "일치"], ["우리는 행동을 조정해야 하는지 묻게 될 수 있다.", "Do I need to adjust my behaviors", "일치"], ["우리는 거절을 최소화하는 기제를 발달시켰다.", "minimizing rejection", "일치"]])]
PICK2 = [PK(p, 'The system monitors', 'sends', 'send', "정답 ▶ sends\n이유: 주어 The system(단수) — monitors와 병렬"),
 PK(p, 'The system monitors', 'that alerts', 'what alerts', "정답 ▶ that\n이유: 선행사 an alarm + 주어 없는 절 → 주격 관계대명사"),
 PK(p, 'The monitoring system generally', 'until', 'unless', "정답 ▶ until\n이유: 탐지할 '때까지' 무의식적으로 작동 — 시간의 접속사"),
 PK(p, 'When the alarm bell rings', 'is pushed', 'pushes', "정답 ▶ is pushed\n이유: 위협이 의식으로 '밀려 들어오는'(수동)"),
 PK(p, 'Am I being accepted', 'to fix', 'fixing', "정답 ▶ to fix\n이유: 목적의 to부정사(관계를 바로잡기 위해)"),
 PK(p, 'With such a high value', 'networked', 'networking', "정답 ▶ networked\n이유: 방식이 '연결되어 있는'(수동) → be + p.p.")]
VERB = [VB(p, 'Am I being accepted', 'accepted', 'accept', "정답 ▶ accepted\n이유: 진행 수동 be being p.p.(받아들여지고 있는)"),
 VB(p, 'We all have an interpersonal', 'searching', 'search', "정답 ▶ searching\n이유: 전치사 of 뒤 동명사"),
 VB(p, 'We all have an interpersonal', 'to assess', 'assess', "정답 ▶ to assess\n이유: 목적의 to부정사")]
ERR = [ER(p, 'The system monitors', ['monitors', ('sends', 'send'), 'alerts'], 1, 'sends', "틀린 곳 ▶ ② send → sends\n이유: 주어 The system(단수) — monitors와 병렬\n나머지 ▶ ① ✔ ③ 선행사 an alarm(단수) ✔"),
 ER(p, 'With such a high value', ['tied', 'that', ('would be', 'would being')], 2, 'would be', "틀린 곳 ▶ ③ would being → would be\n이유: 조동사 뒤 동사원형\n나머지 ▶ ① 과거분사(연결된) ✔ ② 진주어 that절 ✔")]
SCR = [0, 2, 3, 7]
ORDER = [[0, 1, 2, 3], [5, 6, 7, 8]]
INSERT = [([1, 2, 3, 4], 2, "정답 ▶ ③ (When the alarm bell rings ~)\n이유: 보통은 무의식적으로 작동하다가 관계적 가치가 떨어짐을 탐지 → 경보가 울리면 의식으로 밀려와 상황 평가 → 수용되고 있나, 행동을 조정해야 하나? (평가의 내용)")]
ODD = [([0, 1, "Many people use social media to share photos with their friends.", 2], 2, "정답 ▶ ③\n이유: 자아존중감이 관계를 감시하는 기제라는 설명이에요. 소셜 미디어 사진 공유는 관계없어요.")]
BLANK = [BL(p, 'From an evolutionary perspective', 'the quality of our relationships', ["the size of our brain", "the speed of our thoughts", "the amount of our money"], "정답 ▶ the quality of our relationships (관계의 질)\n이유: 다른 사람의 반응, 포함 상태, 관계적 가치 → 관계\n오답 ▶ 뇌 크기 · 생각 속도 · 돈의 양"),
 BL(p, 'It also makes sense', 'enhancing acceptance', ["avoiding people", "increasing rejection", "hiding feelings"], "정답 ▶ enhancing acceptance (수용을 높이는)\n이유: 거절은 최소화(minimizing rejection)와 짝 → 수용은 높임\n오답 ▶ 사람 피하기 · 거절 늘리기(반대) · 감정 숨기기")]
GRAM = [{'q': "빈칸에 알맞은 것은?<br><b>Am I being ______ or am I being pushed out?</b>", 'opts': ["accepted", "accepting", "accept", "to accept"], 'ex': "정답 ▶ accepted\n이유: be being p.p. 진행 수동"},
 {'q': "빈칸에 알맞은 것은?<br><b>The system operates nonconsciously ______ it detects that our value is low.</b>", 'opts': ["until", "unless", "because of", "despite"], 'ex': "정답 ▶ until\n이유: ~할 때까지"},
 {'q': "빈칸에 알맞은 것은?<br><b>The system monitors reactions and ______ an alarm.</b>", 'opts': ["sends", "send", "sending", "to send"], 'ex': "정답 ▶ sends\n이유: 주어 단수, 동사 병렬"}]
SUMQ = []
