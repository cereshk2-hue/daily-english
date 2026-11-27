# 11/27 21시 발산중2 외부지문 1·2·3 고난도 DAY (m2-visang-hwang-L7 맨 끝 hx1·hx2·hx3)
# 선생님: 삽입을 여전히 어려워함 + 내용 일치·불일치를 정말 다양하고 난이도 있게 다각도로
#  단계: ① T/F 고난도(본문 안 보고, 바꿔 쓴 표현) ② 내용 다각도(본문 상자 + 선택지별 해설: 불일치·일치(우리말)·개수·답할 수 없는 질문·함축·요약·순서·지칭·연결·제목)
#        ③ 문장삽입 고난도(6문장 창 · 빈칸 5곳, 답이 하나로만 정해지는 것만 — 애매한 후보는 뺌)
import sys, json, re, subprocess
sys.path.insert(0, '/home/claude/srcrepo/generators')
from gencommon import write
import bsrm3_data as R3
path = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/proj/data/m2-visang-hwang-L7.js'
PK = json.loads(subprocess.check_output(['node', '-e', "global.window={};require('%s');process.stdout.write(JSON.stringify(window.PKG))" % path]))
D = {d['id']: d for d in PK['days']}
def sents(did):
    return [(l[1], l[2]) for l in D[did]['passage'] if l[0] != '#']
S1, S2, S3 = sents('ex1'), sents('ex2'), R3.S
assert len(S1) == 12 and len(S2) == 19 and len(S3) == 21
H = {1: 'Reading Material 1', 2: 'Reading Material 2', 3: 'Reading Material 3'}
TITLE = {1: '나라별 대화 방식 (스포츠 비유)', 2: '우주 비행사의 사인 보험', 3: '큰곰자리와 작은곰자리 (그리스 신화)'}
CNT = ['1개', '2개', '3개', '4개', '5개']
def tfx(b, ko, ev, why):
    return '정답 %s\n문장 해석 ▶ %s\n본문 ▶ %s\n왜 %s일까? ▶ %s' % ('T ✔' if b else 'F ✘', ko, ev, 'T' if b else 'F', why)
# ───────── 외부지문 1 ─────────
TF1 = [
 ("In Japan, someone usually breaks in when there is a long pause.", False, "일본에서는 긴 멈춤이 있으면 보통 누군가 끼어든다.", "others never break in", "긴 멈춤이 있어도 절대(never) 끼어들지 않아요."),
 ("Japanese speakers wait for their turn, and so do bowlers.", True, "일본인은 차례를 기다리고, 볼링 선수들도 그렇다.", "Each person waits for their turn, just like bowlers.", "just like bowlers = 볼링 선수들과 똑같이 → and so do bowlers로 바꿔 씀."),
 ("In American conversations, a person may start talking when the speaker hesitates.", True, "미국인의 대화에서는 말하는 사람이 머뭇거리면 다른 사람이 말을 시작할 수 있다.", "When someone hesitates, another person interrupts.", "interrupts(끼어든다) = start talking."),
 ("American conversations are compared to rugby players stealing the ball.", False, "미국인의 대화는 공을 가로채는 럭비 선수에 비유된다.", "It's like when basketball players steal the ball.", "공을 가로채는 건 농구(basketball) 선수예요. 럭비는 이탈리아."),
 ("Italians hardly use their hands when they talk.", False, "이탈리아인들은 말할 때 손을 거의 쓰지 않는다.", "Italians use a lot of hand gestures", "손짓을 많이(a lot of) 써요. hardly = 거의 ~않다."),
 ("Italians consider interruptions rude and thoughtless.", False, "이탈리아인들은 끼어들기를 무례하고 배려 없는 행동으로 여긴다.", "rather than a lack of thoughtfulness", "배려 부족이 '아니라'(rather than) 관심의 표시로 여겨요."),
 ("To Italians, being interrupted can mean that the other person is interested.", True, "이탈리아인에게 말이 끊기는 것은 상대가 관심이 있다는 뜻일 수 있다.", "take interruptions as a sign of interest in the conversation", "끼어들기 = 대화에 대한 관심의 표시."),
 ("The writer says all countries share one conversation style.", False, "글쓴이는 모든 나라가 하나의 대화 방식을 공유한다고 말한다.", "Every country has its own unique conversation style.", "나라마다 고유한(own unique) 방식이 있어요."),
 ("The writer advises us to adjust to our foreign friends' ways of talking.", True, "글쓴이는 외국인 친구들의 대화 방식에 맞추라고 조언한다.", "try to match them", "match them = 그들의 방식에 맞추다 = adjust to."),
 ("Three different sports are used to describe the conversation styles.", True, "대화 방식을 설명하는 데 세 가지 스포츠가 쓰였다.", "Italian conversations are like rugby.", "볼링(일본)·농구(미국)·럭비(이탈리아) 세 가지."),
]
MC1 = [
 {"q": "글의 내용과 일치하지 <u>않는</u> 것은?", "opts": ["Americans wait until the other person has completely finished speaking.", "Japanese speakers do not cut in even during long pauses.",
   "The writer uses three sports to explain different conversation styles.", "Italians often use their hands while talking.", "The writer advises readers to match foreign friends' styles."],
  "ex": "정답 근거: When someone hesitates, another person interrupts.\n· 미국인은 상대가 머뭇거리면 바로 끼어듦 → 끝날 때까지 기다리지 않음",
  "per": [["미국인은 상대가 말을 완전히 끝낼 때까지 기다린다.", "When someone hesitates, another person interrupts.", "불일치 → 머뭇거리면 끼어듦"],
          ["일본인은 긴 멈춤에도 끼어들지 않는다.", "others never break in", "일치 (break in = cut in)"],
          ["글쓴이는 세 가지 스포츠로 대화 방식을 설명한다.", ["Japanese conversations are like bowling.", "American conversations are like basketball.", "Italian conversations are like rugby."], "일치 (볼링·농구·럭비)"],
          ["이탈리아인은 말할 때 손을 자주 쓴다.", "use a lot of hand gestures", "일치"],
          ["외국 친구의 방식에 맞추라고 조언한다.", "try to match them", "일치"]]},
 {"q": "글의 내용과 일치하는 것은?", "opts": ["이탈리아인은 끼어들기를 상대가 대화에 관심이 있다는 신호로 받아들이는 편이다.", "일본인은 대화가 잠시 멈추면 다른 사람이 이어서 말을 시작한다.",
   "미국인의 대화 방식은 럭비 선수가 공을 빼앗는 모습에 비유된다.", "글쓴이는 모든 나라가 같은 대화 규칙을 따라야 한다고 주장한다.", "이탈리아인은 끼어들기를 배려가 부족한 행동으로 여긴다."],
  "ex": "정답 근거: Italians tend to take interruptions as a sign of interest in the conversation rather than a lack of thoughtfulness.\n· tend to = ~하는 경향이 있다(편이다)",
  "per": [["(정답)", "take interruptions as a sign of interest", "일치"], ["", "others never break in", "불일치 → 절대 끼어들지 않음"],
          ["", "It's like when basketball players steal the ball.", "불일치 → 농구"], ["", "Every country has its own unique conversation style.", "불일치 → 나라마다 다름, 맞추라고 함"],
          ["", "rather than a lack of thoughtfulness", "불일치 → 배려 부족이 아니라 관심"]]},
 {"q": "다음 중 글의 내용과 일치하는 것의 <b>개수</b>는?<br>ⓐ In Japanese conversations, people speak in turns.<br>ⓑ Long pauses rarely happen in Japanese conversations.<br>ⓒ An American may start talking when the speaker hesitates.<br>ⓓ Italians hardly ever interrupt others.<br>ⓔ The writer compares conversation styles to sports.",
  "opts": CNT, "keep": True, "a": 2,
  "ex": "일치: ⓐⓒⓔ → 3개\nⓑ 본문은 '긴 멈춤이 있어도(Even if there are long pauses) 끼어들지 않는다' — 멈춤이 드물다는 말은 없음 (함정)\nⓓ 이탈리아인은 자주(frequently) 끼어듦",
  "ev": ["Each person waits for their turn", "Even if there are long pauses", "When someone hesitates, another person interrupts.", "interrupt others frequently", "You can compare the different styles to sports."]},
 {"q": "글을 읽고 답할 수 <u>없는</u> 질문은?", "opts": ["Why do Japanese people wait for their turn?", "What sport are American conversations compared to?",
   "What do Italians use a lot of when they talk?", "How do Italians tend to see interruptions?", "What should you remember when you talk with foreign friends?"],
  "ex": "일본인이 차례를 기다리는 '이유'는 나오지 않아요. (기다린다는 사실만 나옴)\n· 농구 / 손짓(hand gestures) / 관심의 표시 / 그들만의 '공놀이 방식'이 있다는 것",
  "per": [["일본인은 왜 차례를 기다리는가?", "Each person waits for their turn", "답할 수 없음 → 이유 없음"], ["미국인의 대화는 어떤 스포츠에 비유되는가?", "American conversations are like basketball.", "농구"],
          ["이탈리아인은 말할 때 무엇을 많이 쓰는가?", "use a lot of hand gestures", "손짓"], ["이탈리아인은 끼어들기를 어떻게 여기는가?", "a sign of interest in the conversation", "관심의 표시"],
          ["외국 친구와 말할 때 무엇을 기억해야 하는가?", "they have their ways of \"playing ball\"", "그들만의 방식이 있다는 것"]]},
 {"q": "밑줄 친 <u>\"playing ball\"</u>이 뜻하는 것으로 가장 알맞은 것은?<br><span class=\"en\">remember that they have their ways of <u>\"playing ball\"</u> and try to match them.</span>",
  "opts": ["각 나라 사람들이 대화를 주고받는 방식", "외국 친구와 실제로 함께 운동하는 것", "공을 가로채듯 상대의 말을 빼앗는 것", "외국 친구와 스포츠 경기를 보러 가는 것", "대화 중에 손짓을 많이 쓰는 것"],
  "ex": "글 전체가 대화 방식을 스포츠(공놀이)에 비유함 → \"playing ball\" = 그 나라의 대화 방식\n· ③은 미국, ⑤는 이탈리아만의 특징이라 전체 뜻이 아님",
  "per": [["(정답)", "You can compare the different styles to sports.", "대화 방식 = 공놀이"], ["", "", "비유일 뿐 실제 운동 ✘"], ["", "It's like when basketball players steal the ball.", "미국인만의 특징"],
          ["", "", "본문에 없음"], ["", "use a lot of hand gestures", "이탈리아인만의 특징"]]},
 {"q": "글의 내용을 요약할 때 빈칸 (A), (B)에 알맞은 것은?<br><span class=\"en\">Conversation styles <b>(A)</b> from country to country, so when we talk with foreign friends, we should try to <b>(B)</b> their styles.</span>",
  "opts": ["(A) differ – (B) match", "(A) differ – (B) ignore", "(A) stay the same – (B) match", "(A) change – (B) criticize", "(A) stay the same – (B) avoid"],
  "ex": "(A) 나라마다 고유한 방식 → differ(다르다)\n(B) try to match them → match(맞추다)",
  "ev": ["Every country has its own unique conversation style.", "try to match them"]},
 {"q": "나라 – 비유한 스포츠 – 대화 특징의 연결이 바른 것은?", "opts": ["미국 – 농구 – 상대가 머뭇거리면 말을 끊고 들어온다", "일본 – 볼링 – 손짓을 많이 쓴다",
   "이탈리아 – 농구 – 자기 차례를 기다린다", "일본 – 럭비 – 긴 멈춤에도 끼어들지 않는다", "이탈리아 – 볼링 – 끼어들기를 무례하다고 여긴다"],
  "ex": "일본 = 볼링 = 차례를 기다림·끼어들지 않음 / 미국 = 농구 = 머뭇거리면 끼어듦 / 이탈리아 = 럭비 = 손짓·잦은 끼어들기, 끼어들기 = 관심",
  "per": [["(정답)", ["American conversations are like basketball.", "When someone hesitates, another person interrupts."], "바른 연결"], ["", "Japanese conversations are like bowling.", "손짓은 이탈리아"],
          ["", "Italian conversations are like rugby.", "이탈리아는 럭비, 기다림은 일본"], ["", "Japanese conversations are like bowling.", "일본은 볼링"], ["", "Italian conversations are like rugby.", "럭비이고, 끼어들기 = 관심"]]},
 {"q": "글의 제목으로 가장 알맞은 것은?", "opts": ["Different Countries, Different Ways of \"Playing Ball\" in Conversation", "Why Italians Love Rugby More Than Bowling",
   "How to Become a Good Basketball Player", "Long Pauses Make Conversations Boring", "Never Interrupt Others When They Talk"],
  "ex": "나라마다 다른 대화 방식을 스포츠에 비유하고, 상대 방식에 맞추라는 글\n· ⑤ 이탈리아에서는 끼어들기가 관심의 표시 — 글의 요지와 반대",
  "ev": ["Every country has its own unique conversation style.", "try to match them"]},
]
I1 = [  # (창 시작, 주어진 문장 번호(창 안 위치), 해설)
 (0, 1, "주어진 문장 'the different styles' = 1번의 conversation style. 그리고 3번부터 볼링·농구·럭비가 나오려면 '스포츠에 비유한다'가 먼저 와야 해요."),
 (3, 2, "On the other hand(반면에) → 앞의 '일본인은 절대 끼어들지 않는다'와 대조. 뒤의 'another person interrupts'는 미국인 이야기라 그 앞에 미국이 소개돼야 해요."),
 (6, 3, "'Just like rugby players' → 앞에 럭비(Italian conversations are like rugby)가 나와야 하고, 뒤 문장의 interruptions는 이 문장의 'interrupt others frequently'를 받아요."),
 (5, 3, "'Italian conversations are like rugby.' → 뒤 문장 'Just like rugby players'가 나오려면 럭비가 먼저 소개돼야 해요. 앞은 미국(농구) 이야기의 끝."),
 (6, 4, "'take interruptions as a sign of interest' → 이탈리아인이 자주 끼어든다는 내용(10번) 바로 뒤. 마지막 문장(외국 친구에게 맞추라)은 결론이라 맨 끝."),
 (6, 5, "'The next time you talk with foreign friends ~ try to match them' → 세 나라를 다 설명한 뒤의 결론(글쓴이의 조언)이라 맨 끝."),
]
# ───────── 외부지문 2 ─────────
TF2 = [
 ("In the 1960s, traveling to space was already common.", False, "1960년대에 우주여행은 이미 흔한 일이었다.", "going to space was a new venture", "새로운 모험(a new venture)이었어요."),
 ("The astronauts worried about nothing but their training.", False, "우주 비행사들은 오직 훈련만 걱정했다.", "Besides worrying about training, they were worried about their wives and children.", "훈련 외에도(Besides) 아내와 아이들을 걱정했어요. nothing but = 오직."),
 ("Insurance companies refused because insuring astronauts was too risky.", True, "보험 회사들은 우주 비행사에게 보험을 드는 것이 너무 위험해서 거절했다.", "It was simply too risky.", "6번 거절 + 7번 이유(too risky)."),
 ("The astronauts sold their autographs directly to eager fans.", False, "우주 비행사들은 사인을 열성 팬들에게 직접 팔았다.", "They gave the autographs to their friends.", "사인은 친구들에게 주었어요. 판 적이 없어요."),
 ("On launch day, the friends had the envelopes stamped with the date at the post office.", True, "발사 날, 친구들은 우체국에서 봉투에 날짜 소인을 받았다.", "the friends took them to the post office to have the envelopes stamped with the date", "12번 문장 그대로 — have + 목적어 + p.p.(소인이 찍히게 하다)."),
 ("The stamped envelopes were sent to insurance companies.", False, "소인이 찍힌 봉투는 보험 회사로 보내졌다.", "the envelopes were given to the astronauts' families", "우주 비행사들의 가족에게 전달됐어요."),
 ("The families could sell the autographs if the astronauts died on the mission.", True, "임무 중 우주 비행사가 죽으면 가족은 사인을 팔 수 있었다.", "If the astronauts did not return from the moon, their families could sell them.", "did not return from the moon = 돌아오지 못하면."),
 ("In the end, the families had to sell the autographs.", False, "결국 가족들은 사인을 팔아야 했다.", "life insurance autographs were not needed", "다행히 필요하지 않았어요 — 무사히 돌아옴."),
 ("After their return, the astronauts kept signing autographs without getting paid.", True, "돌아온 뒤 우주 비행사들은 돈을 받지 않고 계속 사인을 해 주었다.", "They probably signed tens of thousands more autographs for free.", "for free = 돈을 받지 않고. (probably = 아마도)"),
 ("People showed little interest in the astronauts' autographs.", False, "사람들은 우주 비행사들의 사인에 거의 관심이 없었다.", "People really wanted their autographs.", "정말로 원했어요(really wanted)."),
]
MC2 = [
 {"q": "글의 내용과 일치하지 <u>않는</u> 것은?", "opts": ["Insurance companies gladly offered life insurance to the astronauts.", "Going to space was very risky in the 1960s.",
   "Many of the young men had wives and children to worry about.", "The astronauts' friends took the envelopes to the post office on launch day.", "The astronauts came back from the moon safely."],
  "ex": "정답 근거: insurance companies did not want to give life insurance policies to these astronauts.\n· gladly(기꺼이) ↔ did not want to",
  "per": [["보험 회사는 기꺼이 생명 보험을 들어 주었다.", "insurance companies did not want to give life insurance policies", "불일치 → 원하지 않음"],
          ["1960년대 우주에 가는 것은 매우 위험했다.", "It was incredibly dangerous.", "일치 (incredibly dangerous = very risky)"],
          ["많은 젊은이에게 걱정할 아내와 아이가 있었다.", ["had families", "they were worried about their wives and children"], "일치"],
          ["친구들이 발사 날 봉투를 우체국에 가져갔다.", "On the day of the launch, the friends took them to the post office", "일치"],
          ["우주 비행사들은 달에서 무사히 돌아왔다.", "came home safely", "일치"]]},
 {"q": "글의 내용과 일치하는 것은?", "opts": ["날짜 소인이 찍힌 사인 봉투는 우주 비행사의 가족에게 전달되었다.", "우주 비행사들은 사인을 팬들에게 직접 팔아 돈을 모았다.",
   "보험 회사는 우주 비행사의 가족에게만 보험을 들어 주었다.", "우주 비행사들은 돌아온 뒤 더 이상 사인을 하지 않았다.", "가족들은 결국 사인을 팔아 큰돈을 벌었다."],
  "ex": "정답 근거: Then, the envelopes were given to the astronauts' families.",
  "per": [["(정답)", "the envelopes were given to the astronauts' families", "일치"], ["", "They gave the autographs to their friends.", "불일치 → 친구들에게 줌"],
          ["", "insurance companies did not want to give life insurance policies", "본문에 없음 → 보험을 거절함"], ["", "signed tens of thousands more autographs for free", "불일치 → 무료로 더 해 줌"],
          ["", "life insurance autographs were not needed", "불일치 → 필요 없었음"]]},
 {"q": "다음 중 글의 내용과 일치하는 것의 <b>개수</b>는?<br>ⓐ The astronauts worried only about their training.<br>ⓑ Insurance companies thought insuring the astronauts was too risky.<br>ⓒ The envelopes were stamped with the date of the launch.<br>ⓓ The families sold the autographs after the launch.<br>ⓔ After returning, the astronauts signed autographs only for money.",
  "opts": CNT, "keep": True, "a": 1,
  "ex": "일치: ⓑⓒ → 2개\nⓐ 훈련 외에도(Besides) 가족 걱정 ⓓ 필요 없었음(not needed) ⓔ 무료로(for free)",
  "ev": ["Besides worrying about training", "It was simply too risky.", "On the day of the launch", "life insurance autographs were not needed", "for free"]},
 {"q": "글을 읽고 답할 수 <u>없는</u> 질문은?", "opts": ["How much money could one autograph be sold for?", "Why did insurance companies refuse the astronauts?",
   "Who took the envelopes to the post office?", "What did the astronauts worry about besides training?", "What happened after the astronauts walked on the moon?"],
  "ex": "사인 한 장의 가격은 나오지 않아요.\n· 너무 위험해서 / 친구들 / 아내와 아이들 / 무사히 집에 돌아옴",
  "per": [["사인 한 장을 얼마에 팔 수 있었나?", "", "답할 수 없음"], ["보험 회사는 왜 거절했나?", "It was simply too risky.", "너무 위험해서"],
          ["누가 봉투를 우체국에 가져갔나?", "the friends took them to the post office", "친구들"], ["훈련 외에 무엇을 걱정했나?", "worried about their wives and children", "아내와 아이들"],
          ["달을 걸은 뒤 어떻게 되었나?", "came home safely", "무사히 돌아옴"]]},
 {"q": "밑줄 친 <u>life insurance in the form of autographs</u>가 뜻하는 것으로 가장 알맞은 것은?", "opts": ["돌아오지 못할 경우 가족이 사인을 팔아 돈을 마련할 수 있게 한 것", "사인을 받은 팬들이 생명 보험에 가입한 것",
   "보험 회사가 사인을 받고 보험을 들어 준 것", "우주 비행사들이 사인을 해 주고 그 자리에서 돈을 받은 것", "사인이 있어야 보험금을 받을 수 있었던 것"],
  "ex": "보험 대신 사인: 돌아오지 못하면 가족이 사인을 팔 수 있음 = 생명 보험 역할",
  "per": [["(정답)", "If the astronauts did not return from the moon, their families could sell them.", "가족을 위한 대비"], ["", "", "본문에 없음"],
          ["", "insurance companies did not want to give life insurance policies", "보험 회사는 거절함"], ["", "They gave the autographs to their friends.", "돈을 받지 않고 친구에게 줌"], ["", "", "본문에 없음"]]},
 {"q": "다음 일들을 일어난 순서대로 바르게 배열한 것은?<br>(A) Friends took the envelopes to the post office.<br>(B) Insurance companies refused to insure the astronauts.<br>(C) The astronauts signed thousands of autographs.<br>(D) The envelopes were given to the families.",
  "opts": ["(B) – (C) – (A) – (D)", "(C) – (B) – (A) – (D)", "(B) – (A) – (C) – (D)", "(C) – (A) – (B) – (D)", "(B) – (C) – (D) – (A)"], "sort": True,
  "ex": "보험 거절(6) → 창의적 방법으로 사인(8~9) → 친구들이 우체국에서 소인(12) → 가족에게 전달(13)",
  "ev": ["insurance companies did not want to give life insurance policies", "They signed thousands of autographs", "the friends took them to the post office", "the envelopes were given to the astronauts' families"]},
 {"q": "글의 내용을 요약할 때 빈칸 (A), (B)에 알맞은 것은?<br><span class=\"en\">Because insurance companies would not <b>(A)</b> the astronauts, the astronauts used their <b>(B)</b> as a kind of life insurance for their families.</span>",
  "opts": ["(A) insure – (B) autographs", "(A) hire – (B) photos", "(A) insure – (B) salaries", "(A) train – (B) autographs", "(A) pay – (B) letters"],
  "ex": "(A) 생명 보험을 들어 주지 않음 → insure(보험에 들다)\n(B) life insurance in the form of autographs → autographs",
  "ev": ["did not want to give life insurance policies", "It was life insurance in the form of autographs."]},
 {"q": "우주 비행사들이 수천 장의 사인을 한 이유로 가장 알맞은 것은?", "opts": ["자신이 돌아오지 못할 경우 가족의 생계가 걱정되어서", "팬들에게 더 인기를 얻고 싶어서",
   "보험 회사가 사인을 요구해서", "우체국에서 사인을 부탁해서", "유명한 물건을 모으는 것이 취미여서"],
  "ex": "죽더라도 가족이 보살핌을 받게 하고 싶었는데(5) 보험이 안 되자(6) 돈을 마련할 창의적인 방법(8)으로 사인을 함\n· ⑤ 유명한 물건을 모으는 건 '사람들'이 좋아한 것",
  "per": [["(정답)", ["They wanted to make sure if they died, their families would be taken care of.", "a creative way to get money"], "가족 걱정"], ["", "", "본문에 없음"],
          ["", "insurance companies did not want to give life insurance policies", "보험 회사는 거절함"], ["", "", "본문에 없음"], ["", "They knew that people liked to collect famous things.", "사람들의 취미"]]},
]
I2 = [
 (2, 3, "However(하지만) → '가족을 보살피고 싶었다'와 반대되는 상황(보험 거절). 뒤 문장 It was simply too risky.는 거절의 이유."),
 (2, 4, "'It was simply too risky.'의 It = 앞 문장의 '우주 비행사에게 생명 보험을 들어 주는 것' → 거절의 이유. 뒤 문장은 그래서 찾은 창의적인 방법."),
 (5, 2, "보험 거절과 그 이유(too risky) 다음, '돈을 얻을 창의적인 방법' → 뒤의 '수천 장의 사인'이 바로 그 방법이에요."),
 (8, 3, "'the friends' → 앞에 '친구들에게 주었다'가 먼저. 뒤 문장 'the envelopes'는 이 문장에서 처음 나온 봉투를 받아요."),
 (8, 4, "'the envelopes' → 앞 문장(우체국에서 봉투에 소인)에서 봉투가 처음 나와야 해요. 뒤 문장 'It was life insurance ~'는 가족에게 전달된 이 봉투를 가리켜요."),
 (13, 3, "Thankfully, however → 앞의 '돌아오지 못하면 팔 수 있었다'와 반대되는 실제 결과. 뒤 문장 '무사히 돌아왔다'가 그 이유."),
 (13, 5, "'more autographs for free' → 무사히 돌아온 뒤(18번)의 이야기라 맨 끝. 보험용 사인이 필요 없어진 다음에 '더' 무료로 해 줌."),
]
# ───────── 외부지문 3 ─────────
TF3 = [
 ("The Great Bear and the Little Bear can be seen in the north sky every night.", True, "큰곰자리와 작은곰자리는 매일 밤 북쪽 하늘에서 볼 수 있다.", "Every night, we can see the Great Bear and the Little Bear in the north sky.", "1번 문장을 수동태로 바꿔 씀."),
 ("According to a Roman myth, Callisto helped a goddess.", False, "로마 신화에 따르면 칼리스토는 여신을 도왔다.", "According to a Greek myth", "로마(Roman)가 아니라 그리스(Greek) 신화예요."),
 ("Zeus fell in love with Callisto because he did not have a wife.", False, "제우스는 아내가 없었기 때문에 칼리스토와 사랑에 빠졌다.", "even though he had a wife", "아내가 있었는데도(even though) 사랑에 빠졌어요."),
 ("The older Arcas got, the angrier Zeus' wife became.", True, "아르카스가 나이를 먹을수록 제우스의 아내는 더 화가 났다.", "As Arcas grew, the anger of Zeus' wife also grew.", "As ~ also grew = the 비교급, the 비교급(~할수록 더 …하다)."),
 ("Zeus' wife went into the forest on purpose to find Callisto.", False, "제우스의 아내는 칼리스토를 찾으려고 일부러 숲에 갔다.", "she happened to see Callisto in the forest", "우연히(happened to) 봤어요. on purpose = 일부러."),
 ("Callisto was changed into a small, cute bear.", False, "칼리스토는 작고 귀여운 곰으로 변했다.", "She became a huge bear.", "못생기고(ugly) 거대한(huge) 곰이에요."),
 ("When many years passed, Arcas became a strong hunter.", True, "여러 해가 지나 아르카스는 강한 사냥꾼이 되었다.", "Arcas grew up to be a strong hunter.", "grew up to be = 자라서 ~이 되었다."),
 ("The bear felt very happy when she saw her son.", True, "곰은 아들을 보았을 때 무척 기뻤다.", "How happy she was to see her son!", "감탄문 How happy ~ = 아주 기뻤다."),
 ("Zeus turned Callisto back into a beautiful woman.", False, "제우스는 칼리스토를 다시 아름다운 여인으로 되돌렸다.", "Zeus turned Arcas into a bear, too.", "칼리스토를 되돌린 게 아니라 아르카스'도' 곰으로 바꿨어요."),
 ("The writer asks readers to wish the two bears happiness.", True, "글쓴이는 독자들에게 두 곰의 행복을 빌어 달라고 한다.", "wish them happiness", "마지막 문장 — them = 두 곰(칼리스토와 아르카스)."),
]
MC3 = [
 {"q": "글의 내용과 일치하지 <u>않는</u> 것은?", "opts": ["Zeus' wife turned both Callisto and Arcas into bears.", "Callisto worked for the hunting goddess.",
   "Zeus already had a wife when he fell for Callisto.", "Arcas became a hunter when he grew up.", "Zeus put the mother and son in the sky."],
  "ex": "정답 근거: 칼리스토는 제우스의 아내가(10번), 아르카스는 제우스가(19번) 곰으로 바꿈\n· fell for = fell in love with",
  "per": [["제우스의 아내가 칼리스토와 아르카스를 둘 다 곰으로 바꾸었다.", ["So she turned Callisto into an ugly bear.", "Zeus turned Arcas into a bear, too."], "불일치 → 아르카스는 제우스가 바꿈"],
          ["칼리스토는 사냥의 여신을 위해 일했다.", "whose job was to help the hunting goddess", "일치"], ["제우스는 이미 아내가 있었다.", "even though he had a wife", "일치"],
          ["아르카스는 자라서 사냥꾼이 되었다.", "Arcas grew up to be a strong hunter.", "일치"], ["제우스는 엄마와 아들을 하늘에 두었다.", "He placed both of them up in the night sky.", "일치"]]},
 {"q": "글의 내용과 일치하는 것은?", "opts": ["아르카스가 자랄수록 제우스 아내의 분노도 커졌다.", "제우스의 아내는 칼리스토를 찾으려고 일부러 숲으로 갔다.",
   "곰이 된 칼리스토는 아들을 보자 숲으로 도망쳤다.", "아르카스는 곰이 어머니라는 것을 알고 활을 내려놓았다.", "제우스는 칼리스토에게 벌을 주려고 아르카스를 곰으로 바꾸었다."],
  "ex": "정답 근거: As Arcas grew, the anger of Zeus' wife also grew.",
  "per": [["(정답)", "As Arcas grew, the anger of Zeus' wife also grew.", "일치"], ["", "she happened to see Callisto in the forest", "불일치 → 우연히 봄"],
          ["", "How happy she was to see her son!", "불일치 → 아들을 보고 기뻐함"], ["", "Arcas didn't recognize his mother", "불일치 → 알아보지 못하고 쏘려 함"],
          ["", "To save the woman he loved", "불일치 → 구하려고"]]},
 {"q": "다음 중 글의 내용과 일치하는 것의 <b>개수</b>는?<br>ⓐ Callisto was turned into a bear by Zeus.<br>ⓑ Zeus' wife saw Callisto in the forest by chance.<br>ⓒ Arcas recognized the bear at first sight.<br>ⓓ Zeus saved Callisto by changing Arcas into a bear.<br>ⓔ The two bears can be seen in the south sky.",
  "opts": CNT, "keep": True, "a": 1,
  "ex": "일치: ⓑⓓ → 2개\nⓐ 칼리스토를 곰으로 바꾼 건 제우스의 아내 ⓒ 알아보지 못함 ⓔ 북쪽 하늘",
  "ev": ["So she turned Callisto into an ugly bear.", "she happened to see Callisto", "Arcas didn't recognize his mother", "To save the woman he loved", "in the north sky"]},
 {"q": "글을 읽고 답할 수 <u>없는</u> 질문은?", "opts": ["What was the name of Zeus' wife?", "What was Callisto's job?", "Who turned Callisto into a bear?",
   "What did Arcas become when he grew up?", "Where did Zeus place the two bears?"],
  "ex": "제우스 아내의 이름은 나오지 않아요 (Zeus' wife, she로만 나옴).",
  "per": [["제우스 아내의 이름은?", "", "답할 수 없음"], ["칼리스토의 일은?", "whose job was to help the hunting goddess", "사냥의 여신 돕기"],
          ["누가 칼리스토를 곰으로 바꾸었나?", "So she turned Callisto into an ugly bear.", "제우스의 아내"], ["아르카스는 자라서 무엇이 되었나?", "Arcas grew up to be a strong hunter.", "강한 사냥꾼"],
          ["제우스는 두 곰을 어디에 두었나?", "He placed both of them up in the night sky.", "밤하늘"]]},
 {"q": "밑줄 친 말이 가리키는 대상이 나머지 넷과 <u>다른</u> 것은?", "opts": ["One day, <u>she</u> happened to see Callisto in the forest.", "<u>She</u> became a huge bear.",
   "How happy <u>she</u> was to see her son!", "Arcas got ready to shoot <u>her</u>.", "To save <u>the woman</u> he loved, Zeus turned Arcas into a bear."],
  "ex": "①의 she = 제우스의 아내 / 나머지 = 칼리스토",
  "per": [["어느 날, 그녀는 숲에서 칼리스토를 보았다.", "she happened to see Callisto", "제우스의 아내"], ["그녀는 거대한 곰이 되었다.", "She became a huge bear.", "칼리스토"],
          ["그녀는 아들을 보아 얼마나 기뻤을까!", "How happy she was to see her son!", "칼리스토(곰)"], ["아르카스는 그녀를 쏠 준비를 했다.", "got ready to shoot her", "칼리스토(곰)"],
          ["그가 사랑한 여인을 구하려고", "To save the woman he loved", "칼리스토"]]},
 {"q": "다음 일들을 일어난 순서대로 바르게 배열한 것은?<br>(A) Zeus' wife turned Callisto into a bear.<br>(B) Arcas was born.<br>(C) Arcas ran into a huge bear.<br>(D) Zeus placed both of them in the sky.<br>(E) Arcas grew up to be a hunter.",
  "opts": ["(B) – (A) – (E) – (C) – (D)", "(A) – (B) – (E) – (C) – (D)", "(B) – (E) – (A) – (C) – (D)", "(B) – (A) – (C) – (E) – (D)", "(A) – (E) – (B) – (C) – (D)"], "sort": True,
  "ex": "탄생(6) → 칼리스토가 곰이 됨(10) → 사냥꾼으로 자람(14) → 곰과 마주침(15) → 하늘에 올림(20)",
  "ev": ["From them, Arcas was born.", "So she turned Callisto into an ugly bear.", "Arcas grew up to be a strong hunter.", "he ran into a huge bear", "He placed both of them up in the night sky."]},
 {"q": "글의 내용을 요약할 때 빈칸 (A), (B)에 알맞은 것은?<br><span class=\"en\">Out of <b>(A)</b>, Zeus' wife turned Callisto into a bear, and later Zeus turned their son into a bear, too, to <b>(B)</b> her.</span>",
  "opts": ["(A) anger – (B) save", "(A) love – (B) punish", "(A) anger – (B) punish", "(A) fear – (B) find", "(A) joy – (B) save"],
  "ex": "(A) 아내의 분노(anger)에서 비롯됨 (B) To save the woman he loved → save",
  "ev": ["the anger of Zeus' wife also grew", "To save the woman he loved"]},
 {"q": "칼리스토에 대한 제우스 아내의 마음으로 가장 알맞은 것은?", "opts": ["분노하고 앙갚음하고 싶음", "고맙고 미안함", "안타깝고 불쌍함", "관심이 없음", "존경하고 부러움"],
  "ex": "분노가 커짐(7) + 남편을 빼앗은 것에 대해 복수할 완벽한 순간(9) → 분노·복수심\n· ③ '불쌍한 칼리스토!'는 글쓴이의 마음",
  "per": [["(정답)", ["the anger of Zeus' wife also grew", "to get back at Callisto"], "분노·복수"], ["", "", "본문과 반대"], ["", "Poor Callisto!", "글쓴이의 마음"], ["", "", "본문과 반대"], ["", "", "본문에 없음"]]},
]
I3 = [
 (3, 2, "'From them' = 앞 문장의 제우스와 칼리스토. 뒤 문장 'As Arcas grew'에서 아르카스가 이미 소개돼 있어야 해요."),
 (4, 3, "'she' = 앞 문장의 Zeus' wife. 뒤 문장 'this was the perfect moment'의 this = 숲에서 칼리스토를 본 지금 이 순간."),
 (6, 3, "So(그래서) → 앞의 '복수할 완벽한 순간이라고 생각했다'의 결과. 뒤의 'Poor Callisto! / She became a huge bear.'가 곰이 된 뒤 이야기."),
 (10, 3, "'Many years passed.' 다음에 자라서 사냥꾼이 됨 → 뒤 문장 'while hunting'으로 이어져요."),
 (12, 3, "'she / her son' = 곰(칼리스토)과 아르카스 → 곰과 마주친(15번) 바로 뒤. 뒤 문장 But(하지만)은 '엄마는 기뻤지만 아들은 알아보지 못했다'는 대조."),
 (13, 3, "But → 앞의 '엄마는 기뻤다'와 반대 상황. 뒤 문장 'At that moment'(바로 그 순간) = 쏘려던 순간."),
 (15, 3, "제우스가 그들을 본 순간(18번) → 사랑하는 여인을 구하려고 아르카스도 곰으로 → 뒤 문장 'both of them'(둘 다 곰)이 하늘로."),
]
def insert_items(S, spec):
    E = [s for s, _ in S]; out = []
    for st, g, ex in spec:
        L = E[st:st + 6]; assert len(L) == 6 and 1 <= g <= 5, (st, g)
        out.append({'lines': L, 'given': g, 'ex': '정답 ▶ %s번 자리\n단서 ▶ %s' % ('①②③④⑤'[g - 1], ex)})
    return out
def build(n, S, TF, MC, INS):
    E = [s for s, _ in S]; full = ' '.join(E)
    for t in TF: assert t[3] in full, t[3]
    for m in MC:
        m['n'] = H[n]; m['box'] = [H[n]]
        assert len(m['opts']) == 5 and len(set(m['opts'])) == 5, m['q']
        for p in m.get('per', []):
            for e in ([p[1]] if isinstance(p[1], str) else p[1]):
                if e: assert e in full, e
        for e in m.get('ev', []): assert e in full, e
        if 'per' in m:
            m['per'] = [[p[0] if p[0] not in ('', '(정답)') else re.sub('<[^>]+>', '', o), p[1], p[2]] for p, o in zip(m['per'], m['opts'])]
    pas = [['#', H[n], '']] + [['', s, k] for s, k in S]
    return {'id': 'hx%d' % n, 'name': '', 'range': '외부지문 %d · 고난도 (내용 다각도·문장삽입)' % n,
            'story': 'Reading Material %d · %s · 바꿔 쓴 T/F → 다각도 내용 문제 → 빈칸 5곳 문장삽입' % (n, TITLE[n]), 'passage': pas, 'steps': [
        {'type': 'tf', 'title': 'T/F 고난도 (본문 안 보고)', 'guide': '본문 표현을 다른 말로 바꿔 썼어요. 본문을 떠올리며 T/F를 고르세요. 해설의 근거 문장을 꼭 확인해요.',
         'items': [[a, b, tfx(b, k, ev, why), None, ev] for a, b, k, ev, why in TF]},
        {'type': 'mc', 'title': '내용 일치·불일치 다각도', 'guide': '불일치·일치·개수·답할 수 없는 질문·함축 의미·요약·순서·지칭까지 — 진짜 시험처럼 여러 각도로 물어요. 본문은 문제 아래 상자에 있어요.', 'items': MC},
        {'type': 'insert', 'title': '문장삽입 고난도 (빈칸 5곳)', 'guide': '주어진 문장이 들어갈 곳을 고르세요. 대명사(it, they, she)·연결어(However, So, But)·앞뒤 내용이 단서예요.', 'items': insert_items(S, INS)},
    ]}
NEW = [build(1, S1, TF1, MC1, I1), build(2, S2, TF2, MC2, I2), build(3, S3, TF3, MC3, I3)]
src = open(path, encoding='utf-8').read(); head = src[:src.index('window.PKG')]
tail = src[src.index('/* BS8CS-TESTS'):] if '/* BS8CS-TESTS' in src else ''
if tail: PK['tests'] = [t for t in PK['tests'] if not t['id'].startswith('bs8cs-')]
PK['days'] = [d for d in PK['days'] if d['id'] not in ('hx1', 'hx2', 'hx3')] + NEW
for i, d in enumerate(PK['days']): d['name'] = 'DAY %d' % (i + 1)
if 'gen_bshard' not in head: head = head.rstrip('\n') + '\n/* 11/27 21시: 외부지문 1·2·3 고난도 DAY hx1·hx2·hx3 맨 끝 (generators/gen_bshard.py) */\n'
write(PK, path, head)
if tail: open(path, 'a', encoding='utf-8').write(tail)
print([(d['name'], d['range'], [len(s['items']) for s in d['steps']]) for d in NEW])
