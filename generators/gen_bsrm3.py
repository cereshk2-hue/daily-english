# 11/27 발산중2 외부지문 3 (Reading Material 3 · 큰곰·작은곰자리 신화) → m2-visang-hwang-L7 맨 끝 DAY 2개
#  ex3  = 한 줄씩 완벽 학습 13단계 (rf7 구조: 어휘·어휘선택·T/F·일치·어법선택·동사변형·오류·21문장 스크램블·순서·삽입·무관·빈칸·핵심문법)
#  ex3g = 어법·어휘 한 판 (ex1·ex2와 같은 gate, 21문장 전부 괄호)
# 데이터: bsrm3_data.py. 바꾼 문장이 원문과 같은지 전부 assert. BS8CS-TESTS 꼬리 블록 보존
import sys, json, re, subprocess
sys.path.insert(0, '/home/claude/srcrepo/generators')
from gencommon import write
from bsrm3_data import S, E, K, VOC, TITLE
path = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/proj/data/m2-visang-hwang-L7.js'
PK = json.loads(subprocess.check_output(['node', '-e', "global.window={};require('%s');process.stdout.write(JSON.stringify(window.PKG))" % path]))
P1 = [
 ("There is a {sad|happy} story behind these stars.", "뒤에 아내의 복수·엄마를 쏘려는 아들 → 슬픈(sad) 이야기 (마지막 문장 this sad story)"),
 ("Callisto was so beautiful that Zeus, the king of the gods, fell in love with her {even though|because} he had a wife.", "아내가 있었는데'도' 사랑에 빠짐 → 양보 even though (because는 이유)"),
 ("As Arcas grew, the {anger|joy} of Zeus' wife also grew.", "다음에 복수가 이어짐 → 분노(anger)"),
 ("She thought this was the perfect moment to {get back at|thank} Callisto for stealing her husband.", "남편을 빼앗은 것에 대해 → 복수하다(get back at)"),
 ("So she turned Callisto into an {ugly|beautiful} bear.", "복수로 바꾼 것 → 못생긴(ugly) 곰"),
 ("{Poor|Lucky} Callisto!", "곰이 되어 버림 → 불쌍한(poor) 칼리스토"),
 ("Arcas grew up to be a strong {hunter|singer}.", "다음 문장 while hunting in the forest → 사냥꾼(hunter)"),
 ("How {happy|angry} she was to see her son!", "엄마가 아들을 보게 됨 → 기쁜(happy)"),
 ("But Arcas didn't {recognize|forget} his mother and got ready to shoot her.", "엄마를 쏘려 함 → 알아보지(recognize) 못함"),
 ("To {save|punish} the woman he loved, Zeus turned Arcas into a bear, too.", "사랑한 여인을 → 구하기(save) 위해"),
 ("If you ever see the Great Bear and the Little Bear in the night sky, remember this sad story and wish them {happiness|anger}.", "슬픈 이야기의 주인공들에게 → 행복(happiness)을 빌어 줌"),
]
def tfx(b, kor, ev, why):
    return ('정답 %s\n문장 해석 ▶ %s\n본문 ▶ %s\n왜 %s일까? ▶ %s' % ('T ✔' if b else 'F ✘', kor, ev, 'T' if b else 'F', why))
TF = [
 ("We can see the Great Bear and the Little Bear in the south sky.", False, "우리는 남쪽 하늘에서 큰곰자리와 작은곰자리를 볼 수 있다.", "in the north sky", "본문은 북쪽 하늘(north sky)이에요. south(남쪽)가 아니라서 F."),
 ("Callisto's job was to help the hunting goddess.", True, "칼리스토의 일은 사냥의 여신을 돕는 것이었다.", "whose job was to help the hunting goddess", "4번 문장 그대로예요. whose job = Callisto's job → T."),
 ("Zeus did not have a wife when he fell in love with Callisto.", False, "제우스는 칼리스토와 사랑에 빠졌을 때 아내가 없었다.", "even though he had a wife", "아내가 있었는데도(even though he had a wife) 사랑에 빠졌어요 → F."),
 ("Arcas was the son of Zeus and Callisto.", True, "아르카스는 제우스와 칼리스토의 아들이었다.", "From them, Arcas was born.", "them = 제우스와 칼리스토, 그들에게서 태어났으니 아들 → T."),
 ("Zeus' wife turned Callisto into a bear.", True, "제우스의 아내가 칼리스토를 곰으로 바꾸었다.", "So she turned Callisto into an ugly bear.", "she = 제우스의 아내(앞 문장 Zeus' wife) → T."),
 ("Arcas grew up to be a farmer.", False, "아르카스는 자라서 농부가 되었다.", "Arcas grew up to be a strong hunter.", "농부(farmer)가 아니라 강한 사냥꾼(hunter) → F."),
 ("Arcas knew that the bear was his mother.", False, "아르카스는 그 곰이 자기 어머니라는 것을 알았다.", "Arcas didn't recognize his mother", "어머니를 알아보지 못했어요(didn't recognize) → 몰랐으니 F."),
 ("Zeus turned Arcas into a bear to save Callisto.", True, "제우스는 칼리스토를 구하려고 아르카스를 곰으로 바꾸었다.", "To save the woman he loved, Zeus turned Arcas into a bear, too.", "the woman he loved = 칼리스토 → T."),
 ("Zeus placed only Callisto in the night sky.", False, "제우스는 칼리스토만 밤하늘에 올려놓았다.", "He placed both of them up in the night sky.", "둘 다(both of them) 올려놓았어요. only Callisto(칼리스토만)가 아니라서 F."),
]
MC1 = [
 {"n": "Reading Material 3", "box": ["Reading Material 3"], "q": "글의 내용과 일치하지 <u>않는</u> 것은?",
  "opts": ["Arcas tried to shoot the bear because he knew it was his mother.", "Callisto helped the hunting goddess.", "Zeus' wife got angrier as Arcas grew.",
           "Zeus' wife met Callisto in the forest by chance.", "Zeus put both of them in the night sky."],
  "ex": "정답 근거: Arcas didn't recognize his mother and got ready to shoot her.\n· 바꿔 쓴 표현: happened to see = met ~ by chance · placed = put · the anger also grew = got angrier",
  "per": [["아르카스는 그 곰이 어머니인 것을 알고 쏘려 했다.", "Arcas didn't recognize his mother", "불일치 → 알아보지 못함"],
          ["칼리스토는 사냥의 여신을 도왔다.", "whose job was to help the hunting goddess", "일치"],
          ["아르카스가 자라면서 제우스의 아내는 더 화가 났다.", "As Arcas grew, the anger of Zeus' wife also grew", "일치"],
          ["제우스의 아내는 숲에서 우연히 칼리스토를 만났다.", "she happened to see Callisto in the forest", "일치 (happen to = by chance)"],
          ["제우스는 둘 다 밤하늘에 두었다.", "He placed both of them up in the night sky", "일치 (placed = put)"]]},
 {"n": "Reading Material 3", "box": ["Reading Material 3"], "q": "글의 내용으로 보아 빈칸에 들어갈 말로 알맞은 것은?<br><b>Zeus' wife wanted to ________________.</b>",
  "opts": ["take revenge on Callisto for taking her husband", "help Callisto hunt in the forest", "thank Zeus for his love",
           "make Callisto more beautiful", "find a good job for Arcas"],
  "ex": "정답 근거: the perfect moment to get back at Callisto for stealing her husband\n· 바꿔 쓴 표현: get back at = take revenge on · stealing = taking (프린트 단어장: get back at = take revenge on)",
  "per": [["남편을 빼앗은 것에 대해 칼리스토에게 복수하기", "to get back at Callisto for stealing her husband", "일치"],
          ["칼리스토가 숲에서 사냥하도록 돕기", "to get back at Callisto", "불일치 → 복수하려 함"],
          ["제우스의 사랑에 감사하기", "the anger of Zeus' wife also grew", "불일치 → 분노가 커짐"],
          ["칼리스토를 더 아름답게 만들기", "she turned Callisto into an ugly bear", "불일치 → 못생긴 곰으로"],
          ["아르카스에게 좋은 일자리 찾아 주기", "to get back at Callisto", "본문에 없음"]]},
]
P2 = [
 ("How did the bears {end up|ended up} among the stars?", "did + 주어 + 동사원형 → end up"),
 ("There {is|are} a sad story behind these stars.", "주어 a sad story(단수) → is"),
 ("According to a Greek myth, there was a beautiful woman {called|calling} Callisto whose job was to help the hunting goddess.", "'불리는' 수동 → 과거분사 called"),
 ("According to a Greek myth, there was a beautiful woman called Callisto {whose|who} job was to help the hunting goddess.", "뒤에 명사 job → 소유격 관계대명사 whose"),
 ("Callisto was {so|such} beautiful that Zeus, the king of the gods, fell in love with her even though he had a wife.", "so + 형용사 + that (such는 such a + 형용사 + 명사)"),
 ("Callisto was so beautiful that Zeus, the king of the gods, fell in love with her {even though|despite} he had a wife.", "뒤에 주어 + 동사(he had) → 접속사 even though (despite는 전치사)"),
 ("From them, Arcas {was born|born}.", "태어나다 = be born"),
 ("One day, she happened {to see|seeing} Callisto in the forest.", "happen + to부정사: 우연히 ~하다"),
 ("She thought this was the perfect moment {to get|getting} back at Callisto for stealing her husband.", "명사 moment를 꾸미는 to부정사(~할)"),
 ("She thought this was the perfect moment to get back at Callisto for {stealing|steal} her husband.", "전치사 for + 동명사"),
 ("So she turned Callisto {into|to} an ugly bear.", "turn A into B: A를 B로 바꾸다"),
 ("Arcas grew up {to be|being} a strong hunter.", "grow up to be: 자라서 ~이 되다(결과)"),
 ("One day while {hunting|hunted} in the forest, he ran into a huge bear.", "while (he was) hunting — 그가 '사냥하는' 능동"),
 ("How {happy|happily} she was to see her son!", "be동사의 보어 → 형용사 happy (How + 형용사 + 주어 + 동사)"),
 ("But Arcas didn't recognize his mother and got ready {to shoot|shooting} her.", "get ready + to부정사"),
 ("To save the woman {he loved|he loved her}, Zeus turned Arcas into a bear, too.", "목적격 관계대명사 생략 — 선행사 the woman이 loved의 목적어 → her 또 쓰면 ✘"),
 ("If you ever {see|will see} the Great Bear and the Little Bear in the night sky, remember this sad story and wish them happiness.", "조건의 if절은 현재 시제(미래 뜻)"),
 ("If you ever see the Great Bear and the Little Bear in the night sky, remember this sad story and wish them {happiness|happy}.", "wish + 사람 + 명사(4형식) → happiness"),
]
VB = [
 ("Callisto was so beautiful that Zeus, the king of the gods, ___ in love with her even though he had a wife.", "fall", ["fell"], "과거 이야기 → fall - fell - fallen"),
 ("According to a Greek myth, there was a beautiful woman ___ Callisto whose job was to help the hunting goddess.", "call", ["called"], "'~라고 불리는' → 과거분사 called"),
 ("From them, Arcas was ___.", "bear", ["born"], "be born: 태어나다 (bear - bore - born)"),
 ("One day, she happened ___ Callisto in the forest.", "see", ["to see"], "happen + to부정사"),
 ("She ___ this was the perfect moment to get back at Callisto for stealing her husband.", "think", ["thought"], "think - thought - thought"),
 ("She thought this was the perfect moment to get back at Callisto for ___ her husband.", "steal", ["stealing"], "전치사 for + 동명사"),
 ("Many years ___.", "pass", ["passed"], "시간이 지났다 → 과거 passed (past ✘)"),
 ("One day while ___ in the forest, he ran into a huge bear.", "hunt", ["hunting"], "while + -ing (= while he was hunting)"),
 ("One day while hunting in the forest, he ___ into a huge bear.", "run", ["ran"], "run - ran - run / run into: 마주치다"),
 ("He ___ both of them up in the night sky.", "place", ["placed"], "place(놓다)의 과거 placed"),
]
ER = [
 ("According to a Greek myth, there [[was]] a beautiful woman [[calling]] Callisto [[whose]] job was [[to help]] the hunting goddess.", 1, "called", "'불리는' 수동 → 과거분사 called"),
 ("Callisto was [[such]] beautiful [[that]] Zeus, the king of the gods, [[fell]] in love with her [[even though]] he had a wife.", 0, "so", "so + 형용사 + that"),
 ("One day, she [[happened]] [[seeing]] Callisto [[in]] the [[forest]].", 1, "to see", "happen + to부정사"),
 ("She thought this was the perfect moment [[to get]] back at Callisto [[for]] [[steal]] her [[husband]].", 2, "stealing", "전치사 for + 동명사"),
 ("So she [[turned]] Callisto [[to]] an [[ugly]] [[bear]].", 1, "into", "turn A into B"),
 ("[[How]] [[happily]] she [[was]] [[to see]] her son!", 1, "happy", "be동사의 보어 → 형용사 happy"),
 ("If you ever [[will see]] the Great Bear and the Little Bear in the night sky, [[remember]] this sad story and [[wish]] them [[happiness]].", 0, "see", "조건의 if절은 현재 시제"),
]
ORD = [E[3:7], E[6:10], E[13:17], E[17:21]]
FLOWO = ['칼리스토 소개(사냥의 여신을 도움) → 너무 아름다워 제우스가 사랑에 빠짐 → 아르카스 탄생 → 아르카스가 자라며 아내의 분노도 커짐',
         '아내의 분노 → 어느 날 숲에서 칼리스토를 봄 → 복수할 때라고 생각 → 그래서(So) 곰으로 바꿈',
         '사냥꾼이 된 아르카스 → 사냥하다 곰과 마주침 → 엄마는 기쁨(How happy!) → 하지만(But) 알아보지 못하고 쏘려 함',
         '그 순간 제우스가 봄 → 구하려고 아르카스도 곰으로 → 둘을 밤하늘에 → 별을 보면 행복을 빌어 주자']
INS = [(E[6:10], 3, "'복수할 완벽한 순간이라고 생각했다' 뒤에 So(그래서) 곰으로 바꾸었다가 온다."),
       (E[14:18], 2, "'엄마는 기뻤다' 뒤에 But(하지만) 아르카스는 알아보지 못하고 쏘려 했다 — 반대되는 상황."),
       (E[17:21], 2, "아르카스도 곰으로 바꾼 뒤 → 둘 다(both of them) 밤하늘에 올려놓았다.")]
ODD = [([E[6], E[7], "Zeus' wife loved Callisto like her own daughter.", E[8]], 2, "아내는 칼리스토에게 화가 나 복수하려 했다 — '딸처럼 사랑했다'는 흐름과 반대."),
       ([E[13], E[14], "Arcas wanted to become a famous singer in the city.", E[15]], 2, "사냥꾼 아르카스가 숲에서 곰과 마주치는 장면과 관계없다.")]
BL = [
 ("She thought this was the perfect moment to ____ Callisto for stealing her husband.", ["get back at", "fall in love with", "say thank you to", "run away from"], "남편을 빼앗은 것에 대해 → 복수하다(get back at = take revenge on)"),
 ("But Arcas didn't ____ his mother and got ready to shoot her.", ["recognize", "miss", "call", "love"], "엄마를 쏘려 함 → 알아보지(recognize) 못했다"),
 ("To save the woman he loved, Zeus ____.", ["turned Arcas into a bear, too", "made Arcas a stronger hunter", "sent Arcas to another forest", "forgot about Callisto"], "아르카스도 곰으로 바꿔 둘을 하늘에 올림"),
]
GM = [
 {"q": "빈칸에 알맞은 것은?<br><b>Callisto was ______ beautiful that Zeus fell in love with her.</b>", "opts": ["so", "such", "too", "very"], "ex": "so + 형용사 + that ~: 너무 ~해서 …하다"},
 {"q": "빈칸에 알맞은 것은?<br><b>There was a woman called Callisto ______ job was to help the hunting goddess.</b>", "opts": ["whose", "who", "which", "what"], "ex": "뒤에 명사 job → 소유격 관계대명사 whose"},
 {"q": "밑줄 친 <u>to be</u>의 쓰임은?<br><b>Arcas grew up <u>to be</u> a strong hunter.</b>", "opts": ["결과 (자라서 ~이 되다)", "목적 (~하기 위해)", "감정의 원인 (~해서)", "명사 (~하는 것)"], "ex": "grow up to be: 자라서 ~이 되다 (결과)"},
 {"q": "밑줄 친 <u>to see</u>의 쓰임은?<br><b>How happy she was <u>to see</u> her son!</b>", "opts": ["감정의 원인 (~해서)", "목적 (~하기 위해)", "결과 (그 결과 ~하다)", "명사 (~하는 것)"], "ex": "감정(happy) 뒤 to부정사 = 감정의 원인"},
 {"q": "같은 뜻이 되도록 빈칸에 알맞은 것은?<br><b>Zeus fell in love with her even though he had a wife.<br>= Zeus fell in love with her ______ he had a wife.</b>", "opts": ["although", "because", "so", "if"], "ex": "even though = although (비록 ~일지라도)"},
 {"q": "어법상 <u>틀린</u> 문장은?", "opts": ["To save the woman he loved her, Zeus turned Arcas into a bear.", "She happened to see Callisto in the forest.", "She turned Callisto into an ugly bear.",
   "Arcas grew up to be a strong hunter.", "He placed both of them up in the night sky."], "ex": "the woman (that) he loved — 관계대명사가 목적어 역할 → her를 또 쓰면 ✘"},
]
fill = lambda s: re.sub(r'\{([^|}]*)\|[^}]*\}', r'\1', s)
for s, _ in P1 + P2: assert fill(s) in E, s
for s, v, a, _ in VB: assert s.replace('___', a[0]) in E, s
for s, w, fx, _ in ER:
    marks = re.findall(r'\[\[(.*?)\]\]', s); assert len(marks) == 4, s
    c = [0]
    def rp(m):
        c[0] += 1; return fx if c[0] - 1 == w else m.group(1)
    assert re.sub(r'\[\[(.*?)\]\]', rp, s) in E, s
for s, o, _ in BL: assert s.replace('____', o[0]) in E, s
for b, ev in [(t[1], t[3]) for t in TF]: assert ev in ' '.join(E), ev
for m in MC1:
    for p in m['per']: assert p[1] in ' '.join(E), p[1]
for l, g, _ in INS: assert 0 < g < len(l)
passage = [["#", "Reading Material 3 · 외부지문 (발산중 프린트)", ""], ["", "The Great Bear and the Little Bear", "큰곰자리와 작은곰자리"]] + [["", s, k] for s, k in S]
D1 = {'id': 'ex3', 'name': '', 'range': '외부지문 3 · 한 줄씩 완벽 학습 (큰곰·작은곰자리)', 'story': 'Reading Material 3 · 21문장 한 줄씩 꼼꼼하게 — 이것만 하면 다 외워져요',
      'passage': passage, 'steps': [
  {'type': 'vocab', 'title': '핵심어휘·숙어', 'quizN': 15, 'items': [list(v) for v in VOC]},
  {'type': 'pick', 'title': '어휘선택', 'guide': '문맥에 맞는 낱말을 고르세요.', 'items': [{'s': s, 'ex': e} for s, e in P1]},
  {'type': 'tf', 'title': 'T/F 내용 확인', 'guide': '본문 내용과 일치하면 T, 다르면 F를 고르세요.', 'items': [[a, b, tfx(b, k, ev, why), None, ev] for a, b, k, ev, why in TF]},
  {'type': 'mc', 'title': '일치·불일치', 'guide': '선택지는 본문 표현을 쉬운 말로 조금 바꿔 썼어요. 해설의 "바꿔 쓴 표현"을 꼭 확인하세요.', 'items': MC1},
  {'type': 'pick', 'title': '어법선택', 'guide': '어법상 알맞은 것을 고르세요.', 'items': [{'s': s, 'ex': e} for s, e in P2]},
  {'type': 'verb', 'title': '동사변형', 'guide': '( ) 안의 동사를 알맞은 형태로 바꿔 쓰세요.', 'items': [{'s': s, 'v': v, 'a': a, 'ex': e} for s, v, a, e in VB]},
  {'type': 'error', 'title': '오류찾기', 'guide': '어법상 틀린 곳을 고르세요.', 'items': [{'s': s, 'w': w, 'fix': f, 'ex': e} for s, w, f, e in ER]},
  {'type': 'scramble', 'title': '본문 스크램블 (21문장 전부)', 'guide': '우리말에 맞게 단어를 눌러 문장을 완성하세요. 본문 한 줄씩 전부 나와요.', 'items': [{'ko': k, 'en': s} for s, k in S]},
  {'type': 'order', 'title': '문장순서', 'guide': '문장을 본문 순서대로 눌러서 배열하세요.', 'items': [{'lines': l, 'flow': [f]} for l, f in zip(ORD, FLOWO)]},
  {'type': 'insert', 'title': '문장삽입', 'guide': '주어진 문장이 들어가기에 가장 알맞은 곳을 고르세요.', 'items': [{'lines': l, 'given': g, 'ex': e} for l, g, e in INS]},
  {'type': 'odd', 'title': '어색한 문장', 'guide': '글의 흐름과 관계없는 문장을 고르세요.', 'items': [{'lines': l, 'odd': o, 'ex': e} for l, o, e in ODD]},
  {'type': 'blank', 'title': '빈칸추론', 'guide': '빈칸에 들어갈 말로 가장 알맞은 것을 고르세요.', 'items': [{'s': s, 'opts': o, 'ex': e} for s, o, e in BL]},
  {'type': 'mc', 'title': '핵심문법', 'guide': '알맞은 답을 고르세요.', 'items': GM},
]}
# ex3g: 어법·어휘 한 판 (21문장 전부 괄호)
R3 = [
 ("Every night, we can {see|seeing} the Great Bear and the Little Bear in the north sky.", "can + 동사원형 → see"),
 ("How did the bears {end up|ended up} among the stars?", "did + 주어 + 동사원형 → end up"),
 ("There {is|are} a {sad|happy} story behind these stars.", "a sad story(단수) → is / 뒤에 복수·아들이 엄마를 쏘려는 이야기 → sad"),
 ("According to a Greek myth, there was a beautiful woman {called|calling} Callisto {whose|who} job was to help the hunting goddess.", "'불리는' → 과거분사 called / 뒤에 명사 job → 소유격 whose"),
 ("Callisto was {so|such} beautiful that Zeus, the king of the gods, fell in love with her {even though|because} he had a wife.", "so + 형용사 + that / 아내가 있었는데'도' → even though"),
 ("From them, Arcas {was born|born}.", "태어나다 = be born"),
 ("As Arcas grew, the {anger|joy} of Zeus' wife also grew.", "뒤에 복수가 이어짐 → 분노(anger)"),
 ("One day, she happened {to see|seeing} Callisto in the forest.", "happen + to부정사"),
 ("She thought this was the perfect moment to {get back at|thank} Callisto for {stealing|steal} her husband.", "남편을 빼앗은 것에 → 복수하다(get back at) / 전치사 for + 동명사 stealing"),
 ("So she turned Callisto {into|to} an {ugly|beautiful} bear.", "turn A into B / 복수 → 못생긴(ugly)"),
 ("{Poor|Lucky} Callisto!", "곰이 되어 버림 → 불쌍한(poor)"),
 ("She became a {huge|tiny} bear.", "뒤에 아르카스가 '거대한 곰(a huge bear)'과 마주침 → huge"),
 ("Many years {passed|stopped}.", "시간이 지나다 → passed (뒤에 아르카스가 자라서 사냥꾼이 됨)"),
 ("Arcas grew up {to be|being} a strong {hunter|singer}.", "grow up to be(결과) / 다음 문장 hunting → hunter"),
 ("One day while {hunting|hunted} in the forest, he {ran into|ran away from} a huge bear.", "while (he was) hunting / 뒤에 곰을 쏘려 함 → 마주쳤다(ran into)"),
 ("How {happy|happily} she was to see her son!", "be동사의 보어 → 형용사 happy"),
 ("But Arcas didn't {recognize|recognized} his mother and got ready {to shoot|shooting} her.", "didn't + 동사원형 / get ready + to부정사"),
 ("At that moment, Zeus happened {to see|seeing} them.", "happen + to부정사"),
 ("To {save|punish} the woman {he loved|he loved her}, Zeus turned Arcas into a bear, too.", "사랑한 여인을 → 구하다(save) / 목적격 관계대명사 생략 → her 또 쓰면 ✘"),
 ("He {placed|place} both of them up in the night sky.", "과거 이야기, 주어 He → placed (place ✘)"),
 ("If you ever {see|will see} the Great Bear and the Little Bear in the night sky, remember this sad story and wish them {happiness|happy}.", "조건 if절은 현재 → see / wish + 사람 + 명사 → happiness"),
]
parts, nb = [], 0
for i, (s, ex) in enumerate(R3):
    p = fill(s); assert p == E[i], (p, E[i])
    for m in re.findall(r'\{([^}]*)\}', s): o = m.split('|'); assert len(o) == 2 and o[0] != o[1]; nb += 1
    parts.append({'s': s, 'ko': K[i], 'ex': ex})
guide = "지문 전체를 한 번에 풀어요. 어법(문법)과 어휘(문맥에 맞는 낱말) 괄호를 모두 맞혀야 100점, 하나라도 틀리면 0점! 3번 안에 통과 못 하면 틀린 문장만 해설과 함께 연습하고 다시 도전해요."
D2 = {'id': 'ex3g', 'name': '', 'range': '외부지문 3 · 어법·어휘 한 판', 'story': 'Reading Material 3 · %s · 괄호 %d개, 모두 맞혀야 100점' % (TITLE, nb),
      'passage': [['#', 'Reading Material 3 · %s' % TITLE, '']] + [['', s, k] for s, k in S],
      'steps': [{'type': 'gate', 'title': '어법·어휘 한 판', 'guide': guide, 'items': [{'title': 'Reading Material 3 · %s (괄호 %d개)' % (TITLE, nb), 'parts': parts}]}]}
src = open(path, encoding='utf-8').read(); head = src[:src.index('window.PKG')]
tail = src[src.index('/* BS8CS-TESTS'):] if '/* BS8CS-TESTS' in src else ''
if tail: PK['tests'] = [t for t in PK['tests'] if not t['id'].startswith('bs8cs-')]
PK['days'] = [d for d in PK['days'] if d['id'] not in ('ex3', 'ex3g')] + [D1, D2]
for i, d in enumerate(PK['days']): d['name'] = 'DAY %d' % (i + 1)
if 'gen_bsrm3' not in head: head = head.rstrip('\n') + '\n/* 11/27: 외부지문 3 DAY ex3(한 줄씩 완벽 학습 13단계)·ex3g(어법·어휘 한 판) 맨 끝 (generators/gen_bsrm3.py) */\n'
write(PK, path, head)
if tail: open(path, 'a', encoding='utf-8').write(tail)
print('괄호', nb, [(d['name'], d['range'], [len(s['items']) for s in d['steps']]) for d in PK['days'][-2:]])
