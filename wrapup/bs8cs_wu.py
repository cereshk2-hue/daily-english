# 11/25 발산중2 비상(황종배) 8과 실전 문법 CS — 간접의문문 1~5차 (각 20문항: 하 6 · 중 8 · 상 6, 세트마다 난이도 고루)
# 원본: 선생님 학습지 간접의문문(1)·(1-1)·(2)·(2-1)·(3).hwp (CS) → /home/claude/work/bs8n/*.txt
# 원본 객관식은 같은 문제가 여러 파일에 반복 → 하나만. 서술형 일부는 객관식으로 바꿈. 같은 유형으로 새 문장 몇 개 보탬
# ★ 원본 정답 오류 바로잡음: 'Do you think? + Are bats blind?' 원본 정답 ②④(if/whether) → think 뒤에는 if/whether ❌ → Do you think bats are blind?
#    'Did you know if Minjun carry ~' 원본 정답 처리 → carried가 맞아 안 씀 / 'Can you guess ~' 문항은 학습지끼리 설명이 엇갈려 안 씀
#    'James asked him how old this school is/was'(시제 일치)도 파일끼리 정답이 달라 안 씀 / 'if she comes next Saturday'(미래) 논쟁 소지 → 안 씀
import sys; sys.path.insert(0, '/home/claude/srcrepo/wrapup')
from wu_bs8cs import *
H = ('실전 문법', '중2 영어 비상(황종배) 8과 간접의문문', '비상(황종배) 8과 간접의문문 CS', 'bs8cs')
B = lambda *ls: BOX('<br>'.join(ls))
NUMS = ['1개', '2개', '3개', '4개', '5개']
W, I, F_, T_, S_ = '의문사 + 주어 + 동사', 'if / whether', 'think류 → 의문사 맨 앞', '간접의문문 판단', '화법 · 쓰임 구별'
NOTE = '범위: 8과 간접의문문 — 의문사 + 주어 + 동사(do/does/did 빼고 시제는 동사에), 의문사가 주어면 의문사 + 동사, 의문사 없으면 if/whether, think·believe·guess·suppose·imagine이면 의문사를 맨 앞으로. 쉬운 문제부터 어려운 문제까지 고루 섞었어요.'
ORD = '\n포인트 ▶ 간접의문문 = 의문사 + 주어 + 동사 (do/does/did는 빼고 시제·수는 동사에)'
THK = '\n포인트 ▶ think · believe · guess · suppose · imagine → 의문사 + do you think + 주어 + 동사 (know는 해당 ❌)'
IFW = '\n포인트 ▶ 의문사가 없는 의문문 → if / whether + 주어 + 동사 (~인지 아닌지)'
P = {1: [], 2: [], 3: []}
def F(lv, src_, stem, body, opts, ex): P[lv].append(('flex', stem, src_, body, opts, ex))
def X(lv, src_, stem, body, opts, ans, ex): P[lv].append(('fixed', stem, src_, body, opts, ans, ex))
CN = lambda n, x: '%s<u>%s</u>' % (CIR[n - 1], x)
ABC = lambda *ls: B(*['(%s) %s' % ('abcde'[i], l) for i, l in enumerate(ls)])

# ═══════════════ 하 (30) ═══════════════
F(1, W, '다음 대화의 빈칸에 들어갈 말로 알맞은 것은?', B('A: Do you know ' + BL + ' Nick arrives?', 'B: He arrives at 7 p.m.'),
  ['when', 'what', 'who', 'which', 'whose'], "이유 ▶ 7시에 도착한다 → 시간을 묻는 when\n오답 ▶ {1}·{2}·{3}·{4} 대답(7 p.m.)과 맞지 않음" + ORD)
F(1, I, '다음 빈칸에 들어갈 말로 알맞은 것은?', B("I don't know " + BL + ' he has a pet.'),
  ['whether', 'who', 'which', 'what', 'whose'], "이유 ▶ 그가 애완동물이 있는지 없는지 → 의문사 없는 간접의문문은 whether(if)\n오답 ▶ {1}·{2}·{3}·{4} 뒤 문장(he has a pet)에 빠진 말이 없어 의문사가 들어갈 수 없음" + IFW)
F(1, W, '두 문장을 한 문장으로 바르게 연결한 것은?', B("I don't know. + Why is she tired?"),
  ["I don't know why she is tired.", "I don't know why is she tired.", "I don't know why tired is she.", "Why I don't know she is tired.", "Why I don't know is she tired."],
  "이유 ▶ why + 주어(she) + 동사(is)\n오답 ▶ {1} 동사가 주어 앞 {2} 어순 엉킴 {3}·{4} know는 의문사를 앞으로 보내지 않음" + ORD)
F(1, W, '두 문장을 한 문장으로 바르게 연결한 것은?', B('Do you know? + Where does he live?'),
  ['Do you know where he lives?', 'Do you know where does he live?', 'Do you know where lives he?', 'Where do you know he lives?', 'Where do you know does he live?'],
  "이유 ▶ does를 빼고 수(3인칭 단수)는 동사에 → where he lives\n오답 ▶ {1} does 그대로 {2} 어순 {3}·{4} know는 의문사를 맨 앞으로 보내지 않음" + ORD)
F(1, W, '두 문장을 한 문장으로 바르게 연결한 것은?', B('Do you know? + Where did she go?'),
  ['Do you know where she went?', 'Do you know where did she go?', 'Do you know where she did go?', 'Do you know where does she go?', 'Do you know where she goes?'],
  "이유 ▶ did를 빼고 과거는 동사에 → where she went\n오답 ▶ {1} did 그대로 {2} did를 남기면 ❌ {3} 시제·어순 ❌ {4} 과거(did) → 현재로 바뀜" + ORD)
F(1, W, '두 문장을 한 문장으로 바르게 연결한 것은?', B('Do you know? + Why did he run?'),
  ['Do you know why he ran?', 'Do you know why did he run?', 'Do you know why he did run?', 'Do you know why he runs?', 'Do you know why does he run?'],
  "이유 ▶ did를 빼고 run → ran\n오답 ▶ {1} did 그대로 {2} did를 남기면 ❌ {3} 과거 → 현재로 바뀜 {4} 어순·시제 ❌" + ORD)
F(1, W, '다음 우리말을 영어로 바르게 옮긴 것은?', B('너는 그가 몇 살인지 아니?'),
  ['Do you know how old he is?', 'Do you know how old is he?', 'Do you know he is old?', 'How old do you know is he?', 'How old do you know he is?'],
  "이유 ▶ how old를 한 덩어리 의문사로 보고 + 주어 + 동사 → how old he is\n오답 ▶ {1} 동사가 주어 앞 {2} how old가 빠짐 {3}·{4} know는 의문사를 맨 앞으로 보내지 않음\n포인트 ▶ how old · how much · what time · which book은 한 덩어리로 움직임")
F(1, W, '다음 대화의 빈칸에 들어갈 말로 알맞은 것은?', B('A: How old is your new teacher?', "B: Well, I don't know " + BL + '.'),
  ['how old she is', 'how is she old', 'how old is she', 'how is old she', 'how she is old'],
  "이유 ▶ how old + 주어(she) + 동사(is)\n오답 ▶ {1}·{3} 어순 ❌ {2} 동사가 주어 앞 {4} how와 old가 떨어짐" + ORD)
F(1, W, '다음 빈칸에 들어갈 말로 알맞은 것은?', B('I know ' + BL + ' last summer.'),
  ['what you did', 'what did you do', 'what do you did', 'what did do', 'what do you do'],
  "이유 ▶ 네가 지난여름에 한 일을 안다 → what + you + did\n오답 ▶ {1} did가 주어 앞 {2} do와 did가 겹침 {3} 주어 없음 {4} last summer(과거)와 시제가 안 맞음" + ORD)
F(1, W, '주어진 문장을 간접의문문으로 바꿀 때 빈칸에 알맞은 것은?', B('What did you buy?', '→ Can you show me ' + BL + '?'),
  ['what you bought', 'what did you buy', 'what you buy', 'you buy what', 'you bought what'],
  "이유 ▶ did를 빼고 buy → bought\n오답 ▶ {1} did 그대로 {2} 과거 → 현재로 바뀜 {3}·{4} 의문사는 맨 앞" + ORD)
F(1, W, '두 문장을 한 문장으로 바르게 연결한 것은?', B("I don't know. + When will he be home for supper?"),
  ["I don't know when he will be home for supper.", "I don't know when will he be home for supper.", "I don't know when he be home for supper.", "I don't know that when he will be home for supper.", "I don't know when be he will home for supper."],
  "이유 ▶ when + 주어(he) + 동사(will be)\n오답 ▶ {1} will이 주어 앞 {2} will 빠짐 {3} 의문사 앞에 that ❌ {4} 어순 ❌" + ORD)
F(1, W, '다음 우리말을 영어로 바르게 옮긴 것은?', B('나는 어떤 책을 읽어야 할지 궁금하다.'),
  ['I wonder which book I should read.', 'I wonder I should read which book.', 'I wonder which book should I read.', 'Which book I wonder should I read.', 'Which book I wonder I should read.'],
  "이유 ▶ which book(한 덩어리) + 주어(I) + 동사(should read)\n오답 ▶ {1} 의문사는 맨 앞 {2} should가 주어 앞 {3}·{4} wonder는 의문사를 앞으로 보내지 않음" + ORD)
F(1, W, '다음 우리말과 뜻이 같도록 빈칸에 알맞은 것은?', B('이 기계를 어떻게 사용해야 하는지 아니?', '→ Do you know ' + BL + '?'),
  ['how I should use this machine', 'how should I use this machine', 'how should use I this machine', 'how to should use this machine', 'how to I should use this machine'],
  "이유 ▶ how + 주어(I) + 동사(should use)\n오답 ▶ {1} should가 주어 앞 {2} 어순 ❌ {3}·{4} to와 should를 함께 쓰지 않음" + ORD)
F(1, W, '괄호 안의 말을 바르게 배열한 것은?', B("I don't know ( took / this / he / where / picture )."),
  ['where he took this picture', 'where took he this picture', 'this picture where he took', 'this picture he where took', 'he took where this picture'],
  "이유 ▶ where + 주어(he) + 동사(took) + 목적어(this picture)\n오답 ▶ {1} 동사가 주어 앞 {2}·{3}·{4} 의문사가 맨 앞에 와야 함" + ORD)
F(1, F_, '다음 대화의 빈칸에 들어갈 말로 알맞은 것은?', B('A: Where do you ' + BL + ' they will meet?', 'B: They will meet at the bus stop.'),
  ['think', 'see', 'know', 'like', 'want'],
  "이유 ▶ 의문사(Where)가 맨 앞 + do you ___ + 주어 + 동사 → 이 어순은 think류만 가능\n오답 ▶ {2} know는 의문사를 맨 앞으로 보내지 않음(Do you know where ~?) {1}·{3}·{4} 뒤에 '주어 + 동사'가 올 수 없음" + THK)
F(1, I, '다음 빈칸에 들어갈 말로 알맞은 것은?', B("I don't know. + Is he diligent or lazy?", "→ I don't know " + BL + ' he is diligent or lazy.'),
  ['whether', 'what', 'where', 'who', 'when'],
  "이유 ▶ 의문사가 없는 의문문(Is he ~?) → whether + 주어 + 동사\n오답 ▶ {1}·{2}·{3}·{4} 원래 의문문에 의문사가 없음" + IFW)
F(1, W, '두 문장을 한 문장으로 바르게 연결한 것은?', B('Can you tell me? + Where is the bus stop?'),
  ['Can you tell me where the bus stop is?', 'Can you tell me where is the bus stop?', 'Can you tell me where the bus stop does?', 'Can you tell me is where the bus stop?', 'Can you tell me where does the bus stop?'],
  "이유 ▶ where + 주어(the bus stop) + 동사(is)\n오답 ▶ {1} 동사가 주어 앞 {2}·{4} does ❌ {3} 어순 ❌" + ORD)
F(1, W, '두 문장을 한 문장으로 바르게 연결한 것은?', B('I wonder. + Who ate my cookies?'),
  ['I wonder who ate my cookies.', 'I wonder who did eat my cookies.', 'I wonder who my cookies ate.', 'I wonder who ate did my cookies.', 'I wonder who eaten my cookies.'],
  "이유 ▶ 의문사(Who)가 주어 → 의문사 + 동사 그대로: who ate\n오답 ▶ {1} did를 넣지 않음 {2} 쿠키가 먹었다?(주어·목적어 뒤바뀜) {3} 어순 ❌ {4} eaten은 과거분사\n포인트 ▶ 의문사가 주어면 의문사 + 동사")
F(1, W, '두 문장을 한 문장으로 바르게 연결한 것은?', B('I want to know. + What time is it now?'),
  ['I want to know what time it is now.', 'I want to know what time is it now.', 'I want to know what is time it now.', 'I want to know it is what time now.', 'I want to know what time does it now.'],
  "이유 ▶ what time(한 덩어리) + 주어(it) + 동사(is)\n오답 ▶ {1} 동사가 주어 앞 {2} what과 time이 떨어짐 {3} 의문사는 맨 앞 {4} does ❌" + ORD)
F(1, I, '다음 빈칸에 들어갈 말로 알맞은 것은?', B('I wonder ' + BL + ' it will rain tomorrow.'),
  ['if', 'what', 'who', 'which', 'whose'],
  "이유 ▶ 내일 비가 올지 안 올지 궁금하다 → if(= whether)\n오답 ▶ {1}·{2}·{3}·{4} 뒤 문장(it will rain tomorrow)에 빠진 말이 없어 의문사 ❌" + IFW)
F(1, W, '다음 우리말을 영어로 바르게 옮긴 것은?', B('나는 그녀가 어디에 사는지 모른다.'),
  ["I don't know where she lives.", "I don't know where does she live.", "I don't know where she live.", "I don't know she lives where.", "I don't know where lives she."],
  "이유 ▶ where + 주어(she) + 동사(lives, 3인칭 단수)\n오답 ▶ {1} does 그대로 {2} 수 일치 ❌ {3} 의문사는 맨 앞 {4} 동사가 주어 앞" + ORD)
F(1, I, '두 문장을 한 문장으로 바르게 연결한 것은?', B('Do you know? + Is she Korean?'),
  ['Do you know if she is Korean?', 'Do you know is she Korean?', 'Do you know that is she Korean?', 'Do you know if is she Korean?', 'Do you know where she is Korean?'],
  "이유 ▶ 의문사 없음 → if + 주어 + 동사\n오답 ▶ {1} 접속사 없음 {2} that ❌·어순 ❌ {3} 어순 ❌ {4} 뜻이 바뀜(어디)" + IFW)
F(1, W, '두 문장을 한 문장으로 바르게 연결한 것은?', B('Do you know? + Who broke the window?'),
  ['Do you know who broke the window?', 'Do you know who did break the window?', 'Do you know who the window broke?', 'Who do you know broke the window?', 'Do you know who broken the window?'],
  "이유 ▶ 의문사(Who)가 주어 → who + broke\n오답 ▶ {1} did 넣지 않음 {2} 주어·목적어 뒤바뀜 {3} know는 의문사를 앞으로 보내지 않음 {4} broken은 과거분사\n포인트 ▶ 의문사가 주어면 의문사 + 동사")
F(1, W, '두 문장을 한 문장으로 바르게 연결한 것은?', B('Tell me. + What did she say?'),
  ['Tell me what she said.', 'Tell me what did she say.', 'Tell me what she did say.', 'Tell me what said she.', 'Tell me she said what.'],
  "이유 ▶ did를 빼고 say → said\n오답 ▶ {1} did 그대로 {2} did를 남기면 ❌ {3} 동사가 주어 앞 {4} 의문사는 맨 앞" + ORD)
F(1, F_, '다음 대화의 빈칸에 들어갈 말로 알맞은 것은?', B('A: Do you ' + BL + ' where the post office is?', "B: Yes. It's next to the bank."),
  ['know', 'think', 'believe', 'guess', 'suppose'],
  "이유 ▶ Do you ___ where ~? 어순 + Yes로 대답 → know\n오답 ▶ {1}·{2}·{3}·{4} think·believe·guess·suppose는 의문사를 맨 앞으로: Where do you think ~?" + THK)
F(1, I, '두 문장을 한 문장으로 바르게 연결한 것은?', B("I'm not sure. + Can she swim?"),
  ["I'm not sure if she can swim.", "I'm not sure can she swim.", "I'm not sure if can she swim.", "I'm not sure that can she swim.", "I'm not sure what she can swim."],
  "이유 ▶ 의문사 없음 → if + 주어(she) + 동사(can swim)\n오답 ▶ {1} 접속사 없음 {2} can이 주어 앞 {3} that ❌·어순 ❌ {4} what ❌(빠진 말 없음)" + IFW)
F(1, W, '다음 대화의 빈칸에 들어갈 말로 알맞은 것은?', B('A: How old are your grandparents?', "B: I'm not sure " + BL + '.'),
  ['how old they are', 'how old are they', 'how they are old', 'they are how old', 'how are old they'],
  "이유 ▶ how old + 주어(they) + 동사(are)\n오답 ▶ {1} 동사가 주어 앞 {2} how와 old가 떨어짐 {3} 의문사는 맨 앞 {4} 어순 ❌" + ORD)
F(1, W, '다음 우리말을 영어로 바르게 옮긴 것은?', B('너는 누가 내 의자를 옮겼는지 아니?'),
  ['Do you know who moved my chair?', 'Do you know who did move my chair?', 'Do you know who my chair moved?', 'Who do you know moved my chair?', 'Do you know who moving my chair?'],
  "이유 ▶ 의문사 Who가 주어 → who moved\n오답 ▶ {1} did 넣지 않음 {2} 의자가 옮겼다?(뒤바뀜) {3} know는 의문사를 앞으로 보내지 않음 {4} moving은 동사가 아님\n포인트 ▶ 의문사가 주어면 의문사 + 동사")
F(1, W, '다음 빈칸에 들어갈 말로 알맞은 것은?', B('A: Can you tell me ' + BL + ' the restroom is?', "B: It's on the second floor."),
  ['where', 'what', 'who', 'which', 'whose'],
  "이유 ▶ 2층에 있다 → 장소를 묻는 where\n오답 ▶ {1}·{2}·{3}·{4} 대답(on the second floor)과 맞지 않음" + ORD)
F(1, W, '주어진 문장을 간접의문문으로 바꿀 때 빈칸에 알맞은 것은?', B('Why did he leave here?', '→ Please tell me ' + BL + '.'),
  ['why he left here', 'why did he leave here', 'why left he here', 'why he leave here', 'he left why here'],
  "이유 ▶ did를 빼고 leave → left\n오답 ▶ {1} did 그대로 {2} 동사가 주어 앞 {3} 과거(did)인데 동사원형 {4} 의문사는 맨 앞" + ORD)

# ═══════════════ 중 (40) ═══════════════
F(2, W, '다음 빈칸에 들어갈 말로 알맞은 것은?', B("We can't expect " + BL + ' much the ticket will be.'),
  ['how', 'what', 'who', 'when', 'where'],
  "이유 ▶ 표가 얼마일지 → how much(한 덩어리) + 주어 + 동사\n오답 ▶ {1}·{2}·{3}·{4} much와 함께 '얼마나'를 나타내지 못함\n포인트 ▶ how + 형용사·부사(much, old, far, long)는 한 덩어리")
F(2, I, '다음 빈칸에 들어갈 말로 알맞은 것은?', B("I'm not sure " + BL + ' Ken comes back today or tomorrow.'),
  ['if', 'what', 'after', 'until', 'since'],
  "이유 ▶ 오늘 올지 내일 올지 확실하지 않다 → if(= whether) ~인지\n오답 ▶ {1} 뒤 문장에 빠진 말이 없어 what ❌ {2}·{3}·{4} 시간·이유 접속사는 not sure의 내용이 될 수 없음" + IFW)
F(2, I, '다음 빈칸에 들어갈 말로 알맞은 것은?', B('I have no idea whether ' + BL + '.'),
  ['he really wants it', 'what you want', 'when they left', 'who that boy is', 'where I parked the car'],
  "이유 ▶ whether 뒤에는 주어 + 동사 → he really wants it\n오답 ▶ {1}·{2}·{3}·{4} whether 뒤에 의문사를 또 쓸 수 없음" + IFW)
F(2, W, '두 문장을 한 문장으로 바르게 연결한 것은?', B('Do you know? + What time will they arrive?'),
  ['Do you know what time they will arrive?', 'Do you know what time will they arrive?', 'What time do you know they will arrive?', 'What time do you know will they arrive?', 'What time do you know they arrive?'],
  "이유 ▶ what time + 주어(they) + 동사(will arrive), know는 의문사를 앞으로 보내지 않음\n오답 ▶ {1} will이 주어 앞 {2}·{3}·{4} know인데 의문사를 맨 앞으로 보냄" + ORD)
F(2, F_, '두 문장을 한 문장으로 바르게 연결한 것은?', B('Do you think? + Why did he leave early?'),
  ['Why do you think he left early?', 'Do you think why he left early?', 'Why do you think he leave early?', 'Do you think why he had left early?', 'Do you think why did he leave early?'],
  "이유 ▶ think → 의문사(Why)를 맨 앞 + do you think + 주어 + 동사(left)\n오답 ▶ {1}·{3}·{4} 의문사가 뒤에 있음 {2} 과거(did)인데 동사원형 leave" + THK)
F(2, F_, '두 문장을 한 문장으로 바르게 연결한 것은?', B('Do you think? + When will the concert be held?'),
  ['When do you think the concert will be held?', 'Do you think when will the concert be held?', 'When do you think will the concert be held?', 'Do you think when the concert will be held?', 'When will you think the concert be held?'],
  "이유 ▶ When + do you think + 주어(the concert) + 동사(will be held)\n오답 ▶ {1}·{3} 의문사가 뒤 {2} will이 주어 앞 {4} 어순 ❌" + THK)
F(2, W, '두 문장을 한 문장으로 바르게 연결한 것은?', B("I'd like to know. + When did she come to the party?"),
  ["I'd like to know when she came to the party.", "I'd like to know when did she come to the party.", "I'd like to know when came she to the party.", "I'd like to know when she did came to the party.", "I'd like to know when did she came to the party."],
  "이유 ▶ did를 빼고 come → came\n오답 ▶ {1} did 그대로 {2} 동사가 주어 앞 {3}·{4} did와 came을 함께 쓸 수 없음" + ORD)
F(2, F_, '두 문장을 한 문장으로 바르게 연결한 것은?', B('Do you think? + What is that?'),
  ['What do you think that is?', 'Do you think what is that?', 'Do you think what that is?', 'What do you think is that?', 'What is that do you think?'],
  "이유 ▶ What + do you think + 주어(that) + 동사(is)\n오답 ▶ {1}·{2} 의문사가 뒤 {3} 의문사 What은 주어가 아니므로 that is 순서 {4} 어순 ❌" + THK)
F(2, T_, '다음 밑줄 친 부분이 어법상 틀린 것은?', '',
  ['Do you know <u>how far is it from here</u>?', 'Do you know <u>where he is going</u>?', 'Do you know <u>what time the shops close</u>?', 'Do you know <u>whether he can speak Korean</u>?', 'Do you know <u>why she quit her job</u>?'],
  "이유 ▶ how far is it → how far it is (의문사 + 주어 + 동사)\n오답 ▶ {1}·{2}·{3}·{4} 모두 어순이 바름" + ORD)
F(2, T_, '다음 중 어법상 어색한 문장은?', '',
  ['Do you know when she did leave?', 'Can you tell me where you want to go?', "I don't know exactly what happened.", 'She asked me how I got an A in math.', "He doesn't know when I'm going to arrive."],
  "이유 ▶ when she did leave → when she left (did 빼고 과거는 동사에)\n오답 ▶ {1} where + you + want {2} 의문사 what이 주어 → what happened {3} how + I + got {4} when + I + am going" + ORD)
F(2, T_, '다음 밑줄 친 부분이 어법상 틀린 것은?', '',
  ["He doesn't know <u>why is Cathy sad</u>.", "I can't remember <u>what the girl's name is</u>.", "Tom doesn't know <u>why the customer called him</u>.", 'The problem is <u>when they met that day</u>.', 'She knows <u>how much the computer is</u>.'],
  "이유 ▶ why is Cathy sad → why Cathy is sad\n오답 ▶ {2} 보어 자리 간접의문문도 바름 {1}·{3}·{4} 어순 바름" + ORD)
F(2, W, '괄호 안의 말을 바르게 배열한 것은?', B('Suppose you phone the bus terminal and ask ( the next / when / is / leaving / bus / to Gwangju ).'),
  ['when the next bus to Gwangju is leaving', 'when is leaving the next bus to Gwangju', 'when is the next bus to Gwangju leaving', 'the next bus to Gwangju is leaving when', 'the next bus to Gwangju is when leaving'],
  "이유 ▶ when + 주어(the next bus to Gwangju) + 동사(is leaving)\n오답 ▶ {1}·{2} 동사가 주어 앞 {3}·{4} 의문사는 맨 앞" + ORD)
F(2, W, '밑줄 친 우리말을 영어로 바르게 옮긴 것은?', B("People don't know <u>어떤 빵집이 가장 신선한 빵을 굽는지</u>."),
  ['which bakery bakes the freshest bread', 'which bakery the freshest bread bakes', 'which bakery bakes bread the freshest', 'bakes which bakery the freshest bread', 'bakes which bakery bread freshest'],
  "이유 ▶ which bakery(의문사 덩어리)가 주어 → which bakery + bakes + the freshest bread\n오답 ▶ {1} 동사가 맨 뒤 {2} the freshest가 bread 뒤 {3}·{4} 동사가 맨 앞\n포인트 ▶ 의문사 덩어리가 주어면 의문사 + 동사")
F(2, F_, '다음 대화의 빈칸에 들어갈 말로 알맞은 것은?', B('A: ' + BL, "B: No, I don't."),
  ['Do you know what her name is?', 'What do you believe that woman is doing?', 'How old do you think she is?', 'Where do you think she is going?', 'What do you think her hobby is?'],
  "이유 ▶ No, I don't.(Yes/No 대답) → Do you ~?로 묻는 Do you know ~?\n오답 ▶ {1}·{2}·{3}·{4} 의문사로 시작하는 질문은 Yes/No로 대답하지 않음" + THK)
X(2, T_, '다음 대화의 밑줄 친 ⓐ~ⓔ 중 어법상 틀린 것은?', B('A: <u>ⓐWho is he?</u>', "B: I don't know <u>ⓑwho he is</u>.", 'A: Do you know <u>ⓒwhat does he do</u> for a living?', 'B: I think <u>ⓓhe is a musician</u>.', 'A: Tell me <u>ⓔwhy you think so</u>.'),
  ['ⓐ', 'ⓑ', 'ⓒ', 'ⓓ', 'ⓔ'], 3, "이유 ▶ ⓒ what does he do → what he does\n오답 ▶ ⓐ 직접의문문이라 바름 ⓑ who + he + is ⓓ think 뒤 that절 ⓔ why + you + think" + ORD)
F(2, T_, '다음 중 어법상 맞는 문장은?', '',
  ["I don't know whether she will come or not.", 'Can you tell me where is the classroom?', 'How tall your brother is?', 'I want to know when does the plane leave.', 'If you like it or not, you must do it.'],
  "이유 ▶ whether + 주어 + 동사 + or not ✔\n오답 ▶ {1} where the classroom is {2} 직접의문문은 How tall is your brother? {3} when the plane leaves {4} '~이든 아니든'(부사절)은 Whether만 → Whether you like it or not" + IFW)
F(2, I, '다음 중 어법상 틀린 문장은?', '',
  ["I don't care that he is alive or not.", 'Do you believe that Jack will be back?', "Whether the apples are ripe or not doesn't matter.", "She didn't know what she should do.", 'What do you think the longest river is?'],
  "이유 ▶ ~인지 아닌지(or not) → that이 아니라 whether(if)\n오답 ▶ {1} believe + that절 {2} 주어 자리 Whether절 {3} what + 주어 + 동사 {4} think → 의문사 맨 앞" + IFW)
F(2, T_, '다음 중 밑줄 친 부분이 어법상 틀린 것은?', '',
  ['Just let me know <u>where will you stay</u>.', 'Do you remember <u>who I am</u>?', 'Do you know <u>who did this</u>?', "Why don't you tell me <u>what time you arrived</u>?", 'Tell me <u>how much money you spent</u> on this.'],
  "이유 ▶ where will you stay → where you will stay\n오답 ▶ {2} 의문사 who가 주어 → who did this {1}·{3}·{4} 어순 바름" + ORD)
F(2, W, '밑줄 친 부분을 어법에 맞게 고친 것은?', B("Why don't you ask her <u>how much did she pay</u> for it?"),
  ['how much she paid', 'how much did she paid', 'did she pay how much', 'how much she pays', 'she paid how much'],
  "이유 ▶ how much + 주어(she) + 동사(paid)\n오답 ▶ {1} did와 paid를 함께 ❌ {2}·{4} 의문사는 맨 앞 {3} 과거(did) → 현재로 바뀜" + ORD)
F(2, T_, '다음 중 어법상 틀린 문장은?', '',
  ['Do you know who is she?', "I don't know what she bought.", 'No one knows who invented it.', 'Tell me why she is so angry.', 'I want to know how old he is.'],
  "이유 ▶ who is she → who she is\n오답 ▶ {1} what + she + bought {2} 의문사 주어 + 동사 {3}·{4} 어순 바름" + ORD)
F(2, T_, '다음 중 어법상 바른 문장은?', '',
  ['What do you think we should do?', "I don't know why is he so down.", "I don't know where are we now.", 'Do you know how can we get to the post office?', "I don't know why is this happening to me."],
  "이유 ▶ think → 의문사 맨 앞 + 주어 + 동사 ✔\n오답 ▶ {1} why he is {2} where we are {3} how we can get {4} why this is happening" + THK)
F(2, T_, '다음 중 어법상 틀린 문장은?', '',
  ['Could you tell me where did he come from?', 'Do you know why the train was late?', 'We wonder what time the class starts.', 'She wants to know what you bought.', 'Do you know who sent this letter?'],
  "이유 ▶ where did he come from → where he came from\n오답 ▶ {1} why + the train + was {2} what time + the class + starts {3} what + you + bought {4} 의문사 주어 + 동사" + ORD)
F(2, F_, '다음 중 어법상 어색한 문장은?', '',
  ['When do you know he will come back?', 'Do you know when World War II broke out?', 'What do you think Pearl wants to eat?', 'Where do you think John lives?', 'How old do you think his sister is?'],
  "이유 ▶ know는 의문사를 맨 앞으로 보내지 않음 → Do you know when he will come back?\n오답 ▶ {1} know + when + 주어 + 동사 {2}·{3}·{4} think → 의문사 맨 앞" + THK)
F(2, S_, '다음 밑줄 친 if의 쓰임이 나머지 넷과 다른 것은?', '',
  ['I can go to the party <u>if</u> I finish the report.', 'I wonder <u>if</u> it is a good idea.', 'Go and see <u>if</u> your mother is OK.', 'I want to know <u>if</u> the story is true.', 'Could you tell me <u>if</u> Jason is at home?'],
  "이유 ▶ 보고서를 끝내면(조건) 파티에 갈 수 있다 → '만약 ~라면'\n오답 ▶ {1}·{2}·{3}·{4} 동사의 목적어 → '~인지 아닌지'(간접의문문)\n포인트 ▶ 목적어 자리 if = whether / 조건의 if는 whether로 못 바꿈")
F(2, S_, '다음 밑줄 친 if를 whether로 바꾸어 쓸 수 <u>없는</u> 것은?', '',
  ['<u>If</u> he visits my house, I will make him a nice dinner.', 'They want to know <u>if</u> I am married.', 'I wonder <u>if</u> you like sunflowers or not.', 'Tell me <u>if</u> she is in her room or not.', "They don't know <u>if</u> the pandas ate the bamboo."],
  "이유 ▶ 그가 우리 집에 오면(조건) → '만약 ~라면'이라 whether ❌\n오답 ▶ {1}·{2}·{3}·{4} '~인지 아닌지' → whether로 바꿀 수 있음")
F(2, S_, '다음 문장을 간접의문문을 써서 바르게 바꾼 것은?', B('I asked her, "Are you Pete\'s sister?"'),
  ["I asked her if she was Pete's sister.", "I asked her that she was Pete's sister.", "I asked her you are Pete's sister.", "I asked her whether you were Pete's sister.", "I asked her how she was Pete's sister."],
  "이유 ▶ 의문사 없는 질문 → if + 주어 + 동사, you → she, 과거(asked)에 맞춰 was\n오답 ▶ {1} that ❌ {2} 접속사 없음·you 그대로 {3} you → she로 바꿔야 함 {4} how ❌(의문사 없는 질문)" + IFW)
F(2, W, '괄호 안의 단어로 문장을 완성할 때 두 번째로 오는 단어는?', B('A: What did your mom buy yesterday?', "B: I don't know. Can you tell me ( bought / she / what / yesterday )?"),
  ['she', 'what', 'bought', 'yesterday', 'tell'],
  "이유 ▶ what + she + bought + yesterday → 두 번째는 she\n오답 ▶ {1} 첫 번째 {2} 세 번째 {3} 네 번째 {4} 괄호 밖의 말" + ORD)
F(2, W, '다음 대화의 빈칸에 들어갈 말로 알맞은 것은?', B('A: Do you know who invented Hangeul?', 'B: Yes. King Sejong invented it.', 'A: Then do you know ' + BL + '?'),
  ['how many letters Hangeul has', 'how many Hangeul has letters', 'how many letters has Hangeul', 'how Hangeul has many letters', 'Hangeul has how many letters'],
  "이유 ▶ how many letters(한 덩어리) + 주어(Hangeul) + 동사(has)\n오답 ▶ {1} letters가 떨어짐 {2} 동사가 주어 앞 {3} how와 many가 떨어짐 {4} 의문사는 맨 앞" + ORD)
F(2, W, '괄호 안의 말을 바르게 배열한 것은?', B('The city leaders found out ( the problem / was / serious / how ) and began cleanup programs.'),
  ['how serious the problem was', 'how the problem was serious', 'the problem how serious was', 'the problem how was serious', 'how serious was the problem'],
  "이유 ▶ how serious(한 덩어리) + 주어(the problem) + 동사(was)\n오답 ▶ {1} how와 serious가 떨어짐 {2}·{3} 의문사는 맨 앞 {4} 동사가 주어 앞\n포인트 ▶ how + 형용사는 붙어서 움직임")
F(2, T_, '다음 중 어법상 바른 문장은?', '',
  ['Tell me how you solved it.', 'Do you think who I am?', 'Do you know what does Peter want?', "I don't know when will he come back.", 'I want to know if can he come to my party.'],
  "이유 ▶ how + you + solved ✔\n오답 ▶ {1} Who do you think I am? {2} what Peter wants {3} when he will come back {4} if he can come" + ORD)
F(2, T_, '다음 중 어법상 바르지 <u>않은</u> 것은?', '',
  ['You must tell me what did he tell you.', 'What do you believe is true?', 'She asked me if I was single.', 'Nobody knows what the answer is.', 'Do you know how he escaped from prison?'],
  "이유 ▶ what did he tell you → what he told you\n오답 ▶ {1} believe → 의문사 맨 앞, 의문사가 주어라 바로 is {2} if + 주어 + 동사 {3}·{4} 어순 바름" + ORD)
F(2, F_, '다음 중 어법상 어색한 문장은?', '',
  ['Do you imagine where the birds go?', 'Do you know why he is running?', 'I wonder if she still likes chocolate.', "I don't know why he was absent today.", 'Ask her if she will come here tomorrow.'],
  "이유 ▶ imagine → 의문사 맨 앞: Where do you imagine the birds go?\n오답 ▶ {1} know는 그대로 {2}·{4} if + 주어 + 동사 {3} why + he + was" + THK)
F(2, W, '다음 중 어법상 어색한 문장은?', '',
  ["I can't remember how much money I had.".replace('how much money I had', 'how much I had money'), "I don't know how much it costs.", 'I wonder whether you are going to marry him.', "I don't know if it's good to invite her or not.", 'What do you think she will wear for the party?'],
  "이유 ▶ how much I had money → how much money I had (how much money가 한 덩어리)\n오답 ▶ {1} how much + it + costs {2}·{3} whether/if + 주어 + 동사 {4} think → 의문사 맨 앞\n포인트 ▶ how much + 명사도 붙어서 움직임")
F(2, F_, '다음 중 어법상 어색한 문장은?', '',
  ['Do you guess how long it will take to get there?', 'Can you show me how I get there?', 'Whether you succeed or fail, I will still love you.', 'I forgot where I met him.', 'What do you think she will wear for the party?'],
  "이유 ▶ guess → 의문사 맨 앞: How long do you guess it will take ~?\n오답 ▶ {1} how + I + get {2} '~이든 아니든' Whether {3} where + I + met {4} think → 의문사 맨 앞" + THK)
F(2, T_, '다음 중 어법상 올바른 문장은?', '',
  ['What do you believe is the best way?', 'I absolutely agree with your report if we need more trees.', 'Do you know which car will he choose?', "If you go there or not, I don't care.", "I'm just curious because he is happy or not."],
  "이유 ▶ believe → 의문사 What 맨 앞, What이 주어라 바로 is ✔\n오답 ▶ {1} agree ~ that we need {2} which car he will choose {3} Whether you go there or not {4} curious if(whether) he is happy" + THK)
F(2, T_, '다음 중 어법상 올바른 문장은?', '',
  ["I don't know how I should go there.", 'Nobody knows when did the war break out.', 'Where do you know she went?', "I don't remember what did I do.", "Do you think why he's so amazed?"],
  "이유 ▶ how + I + should go ✔\n오답 ▶ {1} when the war broke out {2} Do you know where she went? {3} what I did {4} Why do you think he's so amazed?" + ORD)
F(2, T_, '다음 중 어법상 올바른 문장은?', '',
  ['Tell me whether you will buy it.', 'Do you know where did she go?', 'Did you know why was he angry again?', 'Do you think how they get there?', "I don't know when will she call me."],
  "이유 ▶ whether + 주어 + 동사 ✔\n오답 ▶ {1} where she went {2} why he was {3} How do you think they get there? {4} when she will call" + IFW)
F(2, T_, '다음 중 어법상 올바른 문장은?', '',
  ['Why do you think she was late for the meeting?', 'Do you believe that will Suji be back?', 'Do you think where does she live?', "I don't know if the problem can solve by him.", 'Do you know when do we have to hand in the essay?'],
  "이유 ▶ think → 의문사 맨 앞 + 주어 + 동사 ✔\n오답 ▶ {1} that Suji will be back {2} Where do you think she lives? {3} can be solved(수동) {4} when we have to hand in" + THK)
F(2, W, '다음 우리말을 영어로 바르게 옮긴 것은?', B('우리는 외계인이 어떻게 생겼는지 모른다.'),
  ["We don't know what aliens look like.", "We don't know what do aliens look like.", "We don't know what aliens look.", "We don't know how aliens look like.", "We don't know what look aliens like."],
  "이유 ▶ What do aliens look like? → what + aliens + look like\n오답 ▶ {1} do 그대로 {2} like 빠짐 {3} how와 like를 함께 쓰지 않음 {4} 동사가 주어 앞\n포인트 ▶ 어떻게 생겼는지 = what + 주어 + look like")
F(2, F_, '두 문장을 한 문장으로 바르게 연결한 것은?', B('Do you think? + What will happen tomorrow?'),
  ['What do you think will happen tomorrow?', 'What do you think it will happen tomorrow?', 'Do you think what will happen tomorrow?', 'What will do you think happen tomorrow?', 'Do you think what happens tomorrow?'],
  "이유 ▶ 의문사 What이 주어 → What + do you think + 동사(will happen)\n오답 ▶ {1} 주어 What이 있는데 it을 또 씀 {2}·{4} 의문사가 뒤 {3} 어순 ❌" + THK)

# ═══════════════ 상 (30) ═══════════════
F(3, F_, '다음 우리말을 영어로 바르게 옮긴 것은?', B('너는 내일 경기에서 누가 이길 거라고 생각하니?'),
  ['Who do you think will win the game tomorrow?', 'Do you think who will win the game tomorrow?', 'Do you think who will the game win tomorrow?', 'Who do you think the game will win tomorrow?', 'Who will win do you think the game tomorrow?'],
  "이유 ▶ think → Who 맨 앞, Who가 주어라 바로 will win\n오답 ▶ {1}·{2} 의문사가 뒤 {3} 경기가 이긴다?(주어·목적어 뒤바뀜) {4} 어순 ❌" + THK)
F(3, F_, '두 문장을 한 문장으로 바르게 연결한 것은?', B('Do you think? + What subject does she like?'),
  ['What subject do you think she likes?', 'Do you think what subject does she like?', 'Do you think what subject she likes?', 'What subject do you think she like?', 'What subject do you think does she like?'],
  "이유 ▶ What subject(한 덩어리)를 맨 앞 + do you think + she + likes(does 빼고 3인칭 단수)\n오답 ▶ {1}·{2} 의문사가 뒤 {3} 수 일치 ❌(likes) {4} does 그대로" + THK)
F(3, F_, '두 문장을 한 문장으로 바르게 연결한 것은?', B('Do you guess? + Where did you lose it?'),
  ['Where do you guess you lost it?', 'Where do you guess you lose it?', 'Where did you guess you lost it?', 'Do you guess where you lost it?', 'Do you guess where did you lose it?'],
  "이유 ▶ Where + do you guess(주절은 현재 그대로) + you + lost(did 빼고 과거)\n오답 ▶ {1} 과거 → 현재로 바뀜 {2} 주절 do를 did로 바꾸면 ❌ {3}·{4} 의문사가 뒤" + THK)
F(3, S_, '다음 문장과 의미가 같은 것은?', B('He said to me, "Do you know her address?"'),
  ['He asked me if I knew her address.', 'He asked me that you knew her address.', 'He asked me if you knew her address.', 'He told me that you knew her address.', 'He asked me that I knew her address.'],
  "이유 ▶ 질문 → asked + if + 주어 + 동사, you(나에게 한 말) → I, 과거에 맞춰 knew\n오답 ▶ {1}·{4} that ❌ {2} you → I로 바꿔야 함 {3} told + that은 질문이 아님" + IFW)
F(3, S_, '대화의 내용을 한 문장으로 옮길 때 빈칸에 알맞은 말이 바르게 짝지어진 것은?', B('Tom: Can I borrow your dictionary?', 'Jane: OK, here you are.', '→ Tom asked Jane ' + BL + ' he could borrow ' + BL + ' dictionary.'),
  ['whether − her', 'that − his', 'that − my', 'if − your', "whether − Tom's"],
  "이유 ▶ 의문사 없는 질문 → whether(if) / your dictionary = Jane의 사전 → her\n오답 ▶ {1}·{2} that ❌ {3} your 그대로 ❌ {4} Tom의 사전이 아님" + IFW)
X(3, S_, '다음 문장을 간접의문문으로 바꾼 문장에서 밑줄 친 부분 중 어색한 것은?', B('Tom said to me, "Are you done with your homework?"', '→ Tom ' + CN(1, 'asked me') + ' ' + CN(2, 'if') + ' ' + CN(3, 'he') + ' ' + CN(4, 'was done') + ' with ' + CN(5, 'my homework') + '.'),
  None, 3, "이유 ▶ 질문 속 you는 '나(me)' → he가 아니라 I\n오답 ▶ ① 질문 → asked ② 의문사 없음 → if ④ 과거에 맞춰 was ⑤ your(나의 숙제) → my" + IFW)
F(3, S_, '다음 빈칸에 들어갈 말이 순서대로 바르게 짝지어진 것은?', B('• I wonder ' + BL + ' I should wear a cap.', '• ' + BL + ' he comes or not, the result will be the same.', '• It is true ' + BL + ' the pen is mightier than the sword.'),
  ['if − Whether − that', 'if − Whether − whether', 'whether − That − if', 'if − That − whether', 'whether − Whether − if'],
  "이유 ▶ wonder + if(~인지) / '~이든 아니든'(or not)은 Whether / It is true + that(~라는 것은 사실)\n오답 ▶ {1}·{3}·{4} 사실을 말하는 진주어 자리는 that {2} '~이든 아니든'은 That ❌" + IFW)
X(3, T_, '간접의문문을 바르게 만든 것은 모두 몇 개인가?', ABC("I didn't know. + What should I do? → I didn't know what I should do.", "Can you tell me? + How old is Tom? → Can you tell me how old Tom is?", "I'm not sure. + Why did Tom go home? → I'm not sure why did Tom go home.", 'Do you know? + Which way should I turn? → Which way do you know I should turn?', 'Do you suppose? + Which way will they go? → Which way do you suppose they will go?'),
  NUMS, 3, "이유 ▶ 바른 것 (a)·(b)·(e) 3개\n오답 ▶ (c) why Tom went home (d) know는 의문사를 앞으로 보내지 않음 → Do you know which way I should turn?" + THK)
F(3, S_, '다음 밑줄 친 what의 쓰임이 나머지 넷과 다른 것은?', '',
  ["I don't know <u>what</u> his name is.", "<u>What</u> people say isn't true.", "Don't believe <u>what</u> you see.", "That isn't <u>what</u> you really need.", '<u>What</u> they do for us is helpful.'],
  "이유 ▶ 그의 이름이 무엇인지 → '무엇'(의문사, 간접의문문)\n오답 ▶ {1}·{2}·{3}·{4} '~하는 것'(= the thing which, 관계대명사)\n포인트 ▶ '무엇인지'로 해석되면 의문사 what")
X(3, T_, '다음 중 어법상 옳은 문장은 모두 몇 개인가?', ABC('Tell me where were you.', 'Do you know who drew this?', 'Let me know how much the pencil is.', 'I wonder why she is always so busy.', 'She asked me when the show started.'),
  NUMS, 4, "이유 ▶ 옳은 것 (b)·(c)·(d)·(e) 4개\n오답 ▶ (a) where you were\n포인트 ▶ (b) 의문사 who가 주어 → who drew ✔")
X(3, T_, '다음 빈칸에 들어갈 수 있는 것은 모두 몇 개인가?', B('Can you tell me ' + BL + '?') + ABC('what is the truth', 'who owns this house', 'if the story was true', 'what does she look like', 'how long were you here'),
  NUMS, 2, "이유 ▶ 들어갈 수 있는 것 (b)·(c) 2개\n오답 ▶ (a) what the truth is (d) what she looks like (e) how long you were here\n포인트 ▶ (b) 의문사 who가 주어 → who owns ✔")
F(3, T_, '두 문장을 한 문장으로 바르게 연결한 것끼리 짝지은 것은?', ABC('Tell me. + What did you buy? → Tell me what you bought.', 'I wonder. + What made your parents upset? → I wonder what your parents made upset.', 'I know. + What did you do after school yesterday? → I know what you did after school yesterday.', 'Do you think? + Why did he cut the class? → Why did you think he cut the class?', 'We asked her, "Are you from America?" → We asked her you are from America or not.'),
  ['(a), (c)', '(a), (b)', '(b), (d)', '(c), (e)', '(d), (e)'],
  "이유 ▶ 바른 것 (a)·(c)\n오답 ▶ (b) 의문사 What이 주어 → what made your parents upset (d) 주절은 그대로 → Why do you think he cut the class? (e) We asked her if(whether) she was from America" + ORD)
F(3, T_, '다음 중 어법상 옳은 문장끼리 짝지은 것은?', ABC('Do you know what is his hobby?', 'Do you know what he bought for us?', "I don't know whether I should eat out tonight.", "I don't know when is he going there.", "We don't know if this picture expensive is."),
  ['(b), (c)', '(a), (b)', '(a), (d)', '(c), (e)', '(d), (e)'],
  "이유 ▶ 옳은 것 (b)·(c)\n오답 ▶ (a) what his hobby is (d) when he is going (e) if this picture is expensive" + ORD)
X(3, T_, '다음 중 어법상 <u>틀린</u> 문장은 모두 몇 개인가?', ABC('Do you know whether she can jump?', 'Do you guess where my car is now?', "He doesn't know how old is my dad.", 'When do you think will he come back?', 'Can you tell me what he thinks of her?'),
  NUMS, 3, "이유 ▶ 틀린 것 (b)·(c)·(d) 3개\n고치기 ▶ (b) Where do you guess my car is now? (c) how old my dad is (d) When do you think he will come back?" + THK)
F(3, T_, '다음 중 어법상 옳은 문장끼리 짝지은 것은?', ABC('Do you know where she went?', 'Tell me whether you will buy it.', 'Did you know why was he angry again?', 'Do you think how they get there?', "I don't know when she will call me."),
  ['(a), (b), (e)', '(a), (c), (d)', '(b), (c), (e)', '(a), (d), (e)', '(b), (d), (e)'],
  "이유 ▶ 옳은 것 (a)·(b)·(e)\n오답 ▶ (c) why he was angry (d) How do you think they get there?" + THK)
F(3, T_, '다음 중 어법상 <u>틀린</u> 문장끼리 짝지은 것은?', ABC('Do you know who stole her bag?', 'Do you know where she went last night?', "I don't know where is the flea market.", "I don't know what should I do.", 'I wonder if he was smart and diligent.'),
  ['(c), (d)', '(a), (c)', '(b), (d)', '(b), (e)', '(d), (e)'],
  "이유 ▶ 틀린 것 (c)·(d)\n고치기 ▶ (c) where the flea market is (d) what I should do\n포인트 ▶ (a) 의문사 who가 주어 → who stole ✔" + ORD)
F(3, F_, '다음 중 어법상 옳은 문장끼리 짝지은 것은?', ABC('When do you think Howard will go abroad?', 'Where do you think Gangnam Station is?', 'Do you think who will win the first prize?', 'Do you believe who is rich?', 'Do you think what is the best food?'),
  ['(a), (b)', '(a), (c)', '(b), (d)', '(c), (e)', '(d), (e)'],
  "이유 ▶ 옳은 것 (a)·(b)\n고치기 ▶ (c) Who do you think will win ~? (d) Who do you believe is rich? (e) What do you think is the best food?" + THK)
F(3, T_, '직접의문문을 간접의문문으로 바르게 바꾼 것은?', '',
  ['My mom is asking. + How much is the white skirt? → My mom is asking how much the white skirt is.', 'Tell me. + Does Andrew like spicy food? → Tell me if Andrew like spicy food.', 'I wonder. + Are you Chinese? → I wonder whether are you Chinese.', 'Do you think? + What will Allan do next? → Do you think what Allan will do next?', 'I wonder. + Did my brothers finish their homework? → I wonder if my brothers finish their homework.'],
  "이유 ▶ how much + 주어(the white skirt) + 동사(is) ✔\n오답 ▶ {1} if Andrew likes {2} whether you are {3} What do you think Allan will do next? {4} 과거(did) → finished" + ORD)
X(3, I, '다음 밑줄 친 부분 중 생략할 수 있는 것은?', B('The interviewer will ' + CN(1, 'let') + ' ' + CN(2, 'you') + ' know ' + CN(3, 'if') + ' she ' + CN(4, 'answered correctly') + ' ' + CN(5, 'or not') + '.'),
  None, 5, "이유 ▶ if(whether) + 주어 + 동사 뒤의 or not은 빼도 뜻이 같음(~인지 아닌지)\n오답 ▶ ① let + 목적어 + 동사원형 ② 목적어 ③ 접속사 if는 뺄 수 없음 ④ 간접의문문의 동사" + IFW)
X(3, T_, '간접의문문의 어순이 바른 문장은 모두 몇 개인가?', ABC('I wonder where my phone is.', 'Do you know what time does the bank open?', 'Who do you think broke the vase?', 'Can you tell me how tall the tower is?', "I'm not sure whether he will join us."),
  NUMS, 4, "이유 ▶ 바른 것 (a)·(c)·(d)·(e) 4개\n오답 ▶ (b) what time the bank opens\n포인트 ▶ (c) think → Who 맨 앞, Who가 주어라 바로 broke ✔")
F(3, S_, '다음 문장을 간접의문문을 써서 바르게 바꾼 것은?', B('She said to me, "Where do you live?"'),
  ['She asked me where I lived.', 'She asked me where did I live.', 'She asked me where you lived.', 'She told me where I lived.', 'She asked me that I lived where.'],
  "이유 ▶ 질문 → asked + where + 주어 + 동사, you(나에게 한 말) → I, 과거에 맞춰 lived\n오답 ▶ {1} did 그대로 {2} you → I {3} 질문은 told가 아니라 asked {4} that ❌·의문사는 앞" + ORD)
X(3, F_, '다음 대화의 밑줄 친 ⓐ~ⓔ 중 어법상 틀린 것은?', B('A: <u>ⓐDo you know where Mina is?</u>', 'B: No. <u>ⓑWhy do you think she is late?</u>', "A: I'm not sure <u>ⓒwhether she missed the bus</u>.", 'B: <u>ⓓDo you think when she will come?</u>', 'A: I wonder <u>ⓔif she is sick</u>.'),
  ['ⓐ', 'ⓑ', 'ⓒ', 'ⓓ', 'ⓔ'], 4, "이유 ▶ ⓓ think → 의문사 맨 앞: When do you think she will come?\n오답 ▶ ⓐ know는 그대로 ⓑ think → 의문사 맨 앞 ⓒ·ⓔ whether/if + 주어 + 동사" + THK)
F(3, F_, '두 문장을 한 문장으로 바르게 바꾼 것은?', B('Do you think? + Are bats blind?'),
  ['Do you think bats are blind?', 'Do you think if bats are blind?', 'Do you think whether bats are blind?', 'Do you think are bats blind?', 'Do you think do bats blind?'],
  "이유 ▶ 의문사 없는 의문문 + think → think 뒤에는 (that) + 주어 + 동사: 박쥐가 눈이 멀었다고 생각하니?\n오답 ▶ {1}·{2} think는 if/whether절을 목적어로 쓰지 않음(know라면 Do you know if/whether bats are blind? ✔) {3} 어순 ❌ {4} do ❌·동사 없음\n포인트 ▶ know·wonder·ask + if/whether / think·believe + (that)")
F(3, F_, '두 문장을 한 문장으로 바르게 연결한 것은?', B('Do you believe? + Who is guilty?'),
  ['Who do you believe is guilty?', 'Who do you believe he is guilty?', 'Do you believe who is guilty?', 'Who is guilty do you believe?', 'Do you believe who guilty is?'],
  "이유 ▶ believe → Who 맨 앞, Who가 주어라 바로 is\n오답 ▶ {1} 주어 Who가 있는데 he를 또 씀 {2}·{4} 의문사가 뒤 {3} 어순 ❌" + THK)
F(3, F_, '두 문장을 한 문장으로 바르게 연결한 것은?', B('Do you suppose? + Where does he come from?'),
  ['Where do you suppose he comes from?', 'Where do you suppose does he come from?', 'Do you suppose where he comes from?', 'Where do you suppose he come from?', 'Where does you suppose he comes from?'],
  "이유 ▶ Where + do you suppose + he + comes(does 빼고 3인칭 단수)\n오답 ▶ {1} does 그대로 {2} 의문사가 뒤 {3} 수 일치 ❌ {4} 주어 you → do" + THK)
F(3, F_, '두 문장을 한 문장으로 바르게 연결한 것은?', B('Do you imagine? + What did Melissa say to me?'),
  ['What do you imagine Melissa said to me?', 'What do you imagine Melissa say to me?', 'What did you imagine Melissa said to me?', 'Do you imagine what Melissa said to me?', 'What do you imagine did Melissa say to me?'],
  "이유 ▶ What + do you imagine(주절은 현재 그대로) + Melissa + said\n오답 ▶ {1} 과거(did)인데 동사원형 {2} 주절 do를 did로 바꾸면 ❌ {3} 의문사가 뒤 {4} did 그대로" + THK)
F(3, W, '두 문장을 한 문장으로 바르게 연결한 것은?', B('How did he get to the place? + It is a mystery.'),
  ['How he got to the place is a mystery.', 'How did he get to the place is a mystery.', 'How he did get to the place is a mystery.', 'How got he to the place is a mystery.', 'How he get to the place is a mystery.'],
  "이유 ▶ 간접의문문이 주어 자리 → How + he + got ~ + is(단수)\n오답 ▶ {1} did 그대로 {2} did를 남기면 ❌ {3} 동사가 주어 앞 {4} 과거(did)인데 동사원형\n포인트 ▶ 간접의문문은 주어·목적어·보어 자리에 모두 올 수 있음")
F(3, W, '다음 우리말을 영어로 바르게 옮긴 것은?', B('누가 내 방 유리창을 깼는지가 나에게는 의문이다.'),
  ['Who broke the window in my room is a question to me.', 'Who did break the window in my room is a question to me.', 'Who the window broke in my room is a question to me.', 'Whom broke the window in my room is a question to me.', 'Who broken the window in my room is a question to me.'],
  "이유 ▶ 의문사 Who가 주어 → Who + broke ~, 이 덩어리 전체가 주어(is)\n오답 ▶ {1} did 넣지 않음 {2} 주어·목적어 뒤바뀜 {3} 주어 자리는 who {4} broken은 과거분사\n포인트 ▶ 간접의문문 주어 + 단수 동사")
F(3, W, '두 문장을 한 문장으로 바르게 연결한 것은?', B('Can you tell me? + Who do you like most?'),
  ['Can you tell me who you like most?', 'Can you tell me who do you like most?', 'Who can you tell me you like most?', 'Can you tell me who like you most?', 'Can you tell me who you do like most?'],
  "이유 ▶ 여기 who는 목적어(누구를) → who + you + like (do 빼기)\n오답 ▶ {1} do 그대로 {2} tell은 의문사를 앞으로 보내지 않음 {3} 네가 좋아하는 사람 → 너를 좋아하는 사람(뜻이 바뀜) {4} do를 남기면 ❌\n포인트 ▶ 의문사가 목적어면 의문사 + 주어 + 동사")
F(3, W, '두 문장을 한 문장으로 바르게 연결한 것은?', B('I wonder. + How long have you been waiting for me?'),
  ['I wonder how long you have been waiting for me.', 'I wonder how long have you been waiting for me.', 'I wonder how long you been have waiting for me.', 'I wonder how you have been waiting long for me.', 'I wonder how long you waited have for me.'],
  "이유 ▶ how long + 주어(you) + 동사(have been waiting)\n오답 ▶ {1} have가 주어 앞 {2}·{4} 동사 덩어리 순서 ❌ {3} how와 long이 떨어짐" + ORD)

assert [len(P[k]) for k in (1, 2, 3)] == [30, 40, 30], [len(P[k]) for k in (1, 2, 3)]
NAME = {1: '하', 2: '중', 3: '상'}
for s in range(5):
    T = Test(str(s + 1), '간접의문문 %d차' % (s + 1), '간접의문문 · 하 6 · 중 8 · 상 6', '간접의문문', NOTE, H=H); T.rot0 = s * 2
    for lv in (1, 2, 3):
        for it in P[lv][s::5]:
            if it[0] == 'flex': T.flex(it[1], it[2] + ' · ' + NAME[lv], it[3], it[4], it[5], [])
            else: T.fixed(it[1], it[2] + ' · ' + NAME[lv], it[3], it[4], it[5], it[6], [])
    T.render()
