# 11/25 8과 심경 변화 + 비튼 내용 T/F — gen.py가 exec. DAY oe8(DAY 19) · 시험 m2oi-9 (심경 5 + T/F 20 = 25문항)
# 심경: (단락들, 문항, 정답, 오답 4, 근거 문장들, 해설)  ※ 오답에 정답의 비슷한 말 넣지 않음
MOOD = [
 (['❸', '❹'], "글에 드러난 Eckels의 심경 변화로 가장 적절한 것은?", 'excited → scared', ['bored → excited', 'angry → calm', 'nervous → relieved', 'scared → proud'],
  ['"I\'m so excited," said Eckels', "I'm so scared", 'He was so terrified'],
  "정글에 도착해서는 \"I'm so excited(정말 신나요)\" → 티라노를 보고 \"I'm so scared(너무 무서워요)\", I can't breathe, so terrified(겁에 질린)"),
 (['❻'], "글에 드러난 Eckels의 심경 변화로 가장 적절한 것은?", 'confused → shocked', ['bored → happy', 'shocked → relieved', 'excited → proud', 'calm → grateful'],
  ['Eckels was confused', 'He got more confused', 'He was shocked'],
  "이상한 간판을 보고 Eckels was confused → 대통령까지 바뀌자 more confused → 죽은 나비를 보고 He was shocked(충격을 받았다)"),
 (['❹', '❺'], "글에 드러난 Travis의 심경으로 가장 적절한 것은?", 'angry', ['bored', 'proud', 'thankful', 'jealous'],
  ['Travis said angrily', 'said Travis to Eckels in an angry voice'],
  "\"Sh ... quiet!\" Travis said angrily(화를 내며) / You put all of us in danger ~ in an angry voice(화난 목소리로) → 길을 벗어나 모두를 위험에 빠뜨린 Eckels에게 화가 남"),
 (['❹'], "티라노사우루스를 본 뒤 Eckels의 심경으로 가장 적절한 것은?", 'terrified', ['relaxed', 'bored', 'satisfied', 'proud'],
  ["I'm so scared", "I can't breathe", 'He was so terrified'],
  "\"I'm so scared\", \"I can't breathe\", \"Get me out of here!\", so terrified that he left the path → 겁에 질림"),
 (['❶'], "글에 드러난 Eckels의 심경으로 가장 적절한 것은?", 'excited and eager', ['bored and tired', 'sad and lonely', 'angry and upset', 'scared and worried'],
  ["I've always wanted to see a dinosaur", '"Great," said Eckels. "Can you take me there now?"'],
  "늘 공룡을 보고 싶었다 → 데려가 줄 수 있다는 말에 \"Great!\", 지금 당장(now) 데려가 달라고 함 → 들뜨고 간절함"),
]
KO = {'excited': '신이 난', 'scared': '겁먹은', 'bored': '지루한', 'angry': '화난', 'calm': '차분한', 'nervous': '긴장한', 'relieved': '안도한', 'proud': '자랑스러운',
      'confused': '혼란스러운', 'shocked': '충격받은', 'happy': '행복한', 'grateful': '고마워하는', 'thankful': '고마워하는', 'jealous': '질투하는', 'terrified': '겁에 질린',
      'relaxed': '느긋한', 'satisfied': '만족한', 'eager': '간절한', 'tired': '피곤한', 'sad': '슬픈', 'lonely': '외로운', 'upset': '속상한', 'worried': '걱정하는'}
def ko(o): return re.sub(r'[a-z]+', lambda m: KO.get(m.group(0), m.group(0)), o)
# T/F: (단락, 문장, T/F, 근거, 비튼 곳)
TF = [
 ('❶', "Time Travel promised to take customers to any year in the future.", False, 'NAME ANY YEAR IN THE PAST', "future(미래) ↔ 본문은 THE PAST(과거)"),
 ('❶', "Eckels did not have to wait long for a time machine.", True, "There's a time machine that leaves in 10 minutes", "10분 뒤 출발 → 오래 기다릴 필요 없음 (You're lucky)"),
 ('❶', "Travis introduced himself to Eckels as a travel guide.", False, '"This is Travis, your travel guide," he continued', "Travis가 직접 소개한 게 아니라 Mr. Parker(he continued)가 소개함"),
 ('❷', "Eckels kept his eyes open while the machine was moving.", False, 'Eckels sat down and closed his eyes', "눈을 뜨고 있었다 ↔ closed his eyes(눈을 감았다)"),
 ('❷', "The machine reached the jungle in just a few minutes.", True, 'After only a few minutes, the machine stopped', "only a few minutes = just a few minutes"),
 ('❷', "Travis said that a small change in the past could not affect the future.", False, 'A little change here can cause something unthinkable in the future', "could not affect(영향 없다) ↔ can cause something unthinkable(상상 못 할 일을 일으킬 수 있다)"),
 ('❷', "Travis said they might kill something without meaning to.", True, 'You might kill something by accident', "by accident(실수로) = without meaning to(의도하지 않고)"),
 ('❸', "Everyone jumped out of the time machine quickly.", False, 'Slowly, everyone got out of the time machine', "quickly ↔ Slowly(천천히)"),
 ('❸', "Travis warned that some of the dinosaurs were hungry.", True, 'Some of the dinosaurs are hungry', "본문 그대로를 간접 화법(warned that ~ were)으로 바꿈"),
 ('❸', "Eckels felt nervous and wanted to go home as soon as they arrived.", False, '"I\'m so excited," said Eckels', "도착했을 때는 nervous가 아니라 excited(신남). 집에 가고 싶다는 말도 없음"),
 ('❹', "The T. rex ran toward the travelers as soon as it appeared.", False, 'There was a moment of silence', "나타나자마자(as soon as) ✘ → 서서히 나타났고, Travis의 외침을 듣고 잠시 정적 뒤에 달려옴"),
 ('❹', "Travis told Eckels to walk back quietly, but Eckels ran.", True, 'Eckels turned around and started to run', "walk quietly back 지시 ↔ started to run(뛰기 시작함)"),
 ('❹', "The T. rex turned its head because it heard Eckels scream.", False, 'The T. rex heard Travis', "Eckels의 비명 ✘ → Travis의 외침(\"Eckels!\")을 들음"),
 ('❺', "Eckels got back to the machine before Travis and the others.", True, 'returned safely to the machine and found Eckels inside', "다른 사람들이 돌아왔을 때 Eckels는 이미 안에 있었음"),
 ('❺', "Travis yelled at Eckels for a long time.", False, 'Travis stared at Eckels for a long time without saying anything', "오래 소리쳤다 ✘ → 아무 말 없이 오래 쳐다봄(stared)"),
 ('❺', "Eckels admitted that there was a little mud on his shoes.", True, "There's only a little mud on my shoes", "Eckels 스스로 신발에 진흙이 조금 묻었다고 말함"),
 ('❻', "Mr. Parker said that something was wrong in the present.", False, '"Fine. Welcome home!" said Mr. Parker', "문제가 있다 ✘ → Fine(괜찮다), Welcome home!"),
 ('❻', "In the office, the sign was the only thing that looked different.", True, 'Everything looked the same, except the big sign on the wall', "except the big sign = 간판만 달라 보임"),
 ('❻', "The TV news made Eckels even more confused.", True, 'He got more confused', "TV에서 Keith가 아닌 새 대통령을 보고 more confused"),
 ('❻', "Eckels found a dead butterfly in the mud on his left shoe.", False, 'In the mud on his right shoe', "left(왼쪽) ↔ right shoe(오른쪽 신발)"),
]
assert sum(t[2] for t in TF) == 9 and len(TF) == 20
TXT8 = ' '.join(x[0] for m in S8 for x in S8[m])
for t in TF: assert t[3] in TXT8, t[3]
for m in MOOD:
    for e in m[4]: assert e in TXT8, e
def tf_ex(t): return '정답 ▶ %s\n이유: %s\n근거 ▶ %s' % ('T' if t[2] else 'F', t[4], t[3])
def mood_ex(m): return '정답 ▶ %s (%s)\n이유: %s\n오답 ▶ %s' % (m[2], ko(m[2]), m[5], ' / '.join('%s(%s)' % (o, ko(o)) for o in m[3]))
oe8 = {'id': 'oe8', 'name': '', 'range': '8과 본문 · 심경 변화 + 비튼 T/F', 'story': '8과 본문 · 심경 변화 5문항 + 말을 바꾼(비튼) 내용 T/F 20문항',
       'passage': None,
       'steps': [{'type': 'mc', 'title': '심경 변화', 'guide': "감정 단어(excited·scared·terrified·confused·shocked·angrily)가 단서예요. 어느 장면에서 바뀌는지 근거 문장을 찾아요.",
                  'items': [{'n': m[0][0], 'box': m[0], 'q': m[1], 'opts': [m[2]] + m[3], 'ex': mood_ex(m), 'ev': m[4]} for m in MOOD]},
                 {'type': 'tf', 'title': '비튼 T/F 내용 확인', 'guide': "본문 문장을 다른 말로 바꾸거나 한 군데만 살짝 틀리게 비틀었어요. 누가·언제·어떻게·왜를 본문과 꼼꼼히 맞춰 봐요.",
                  'items': [[t[1], t[2], tf_ex(t), t[0], t[3]] for t in TF]}]}
def mood_test_items():
    out = []
    rr = random.Random(2511); tg = [0, 3, 1, 4, 2]
    for m, t in zip(MOOD, tg):
        opts = m[3][:]; opts.insert(t, m[2])
        bodyh = '<div class="wbox"><p>%s</p></div>' % E(' '.join(x[0] for s in m[0] for x in S8[s]))
        out.append({'src': '8과 본문 %s · 심경' % ''.join(m[0]), 'stem': m[1], 'body': bodyh, 'opts': opts, 'ans': t, 'ex': mood_ex(m).replace('정답 ▶ ', '정답 ▶ %s ' % C[t], 1)})
    for t in TF:
        out.append({'src': '8과 본문 %s · 내용 T/F' % t[0], 'stem': '글의 내용과 일치하면 ①(T), 일치하지 <u>않으면</u> ②(F)를 고르시오.',
                    'body': '<p>%s</p>' % E(t[1]), 'opts': ['T', 'F'], 'ans': 0 if t[2] else 1, 'ex': tf_ex(t).replace('정답 ▶ ', '정답 ▶ %s ' % ('①' if t[2] else '②'), 1)})
    return out
