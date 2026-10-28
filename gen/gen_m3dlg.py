import sys, json, subprocess
sys.path.insert(0, '/tmp/claude-0/-home-claude/a9e3e882-1f02-5d62-8f70-aced81bc59d2/scratchpad')
from gencommon import *
from dlgcommon import *
# 중3 지학사(민찬규) 7·8과 대화문 (10/28). 출처: hwp18(7과 All the Dialogue), hwp19(8과). 10분 단위 DAY, pick

T = lambda R, i: R[i][1]
def S(box, s, o, x, ev): return (None, box, s, o, x, ev)
def ER(s, w, f, x): return (s, w, f, x)

# ═════════════ 7과 ① Listen & Speak 1 (바람·소원 표현하기) ═════════════
T1 = [('G', "Have you heard from Julia? She's traveling in Türkiye, right?", "Julia에게서 소식 들었어? 그녀는 튀르키예에서 여행 중이잖아, 맞지?"),
      ('B', "Yes, she sent me some pictures. Do you want to see them?", "응, 그녀가 나에게 사진 몇 장을 보내왔어. 사진 볼래?"), ('G', "Yes, please.", "응, 보여 줘."),
      ('B', "Okay, take a look.", "좋아, 한번 봐."),
      ('G', "Oh, look at those cave houses! They look so unique, don't they? I wish I could try living there.", "오, 저 동굴 집들을 봐! 매우 독특해 보여, 그렇지 않니? 난 그곳에서 살아 봤으면 좋겠어."),
      ('B', "I like those balloons. They look so beautiful!", "난 저 풍선들이 멋져. 매우 아름다워 보여!"),
      ('G', "I think Türkiye is a wonderful place to visit. I hope to visit there some day.", "내 생각에 튀르키예는 방문하기에 멋진 곳인 것 같아. 언젠가 그곳을 방문해 보고 싶어."),
      ('B', "Me too!", "나도 그래!")]
T2 = [('B', "Will it snow today?", "오늘 눈이 올까?"), ('G', "I have no idea. Why are you waiting for snow, Taeho?", "모르겠어. 넌 왜 눈을 기다리고 있니, 태호야?"),
      ('B', "I got a new sled for my birthday. I can't wait to test it out.", "난 생일 선물로 새 썰매를 받았어. 빨리 그것을 시험해 보고 싶어."),
      ('G', "Let me check the weather. Umm, there will be no snow for a while.", "내가 날씨를 확인해 볼게. 음, 당분간은 눈 소식이 없는데."),
      ('B', "I wish I could live in Alaska. Then I could go sledding all day!", "난 알래스카에서 살았으면 좋겠어. 그러면 온종일 썰매 탈 수 있을 텐데!"),
      ('G', "No kidding! Alaska is a very cold place.", "농담 마! 알래스카는 매우 추운 곳이야."),
      ('B', "I think it would be fun. I want to build a snow house and stay there on vacation.", "내 생각에는 재미있을 것 같아. 난 눈으로 만든 집을 짓고 방학 때 그곳에서 지내고 싶어."),
      ('G', "Living in a snow house sounds fun!", "눈으로 만든 집에서 사는 것은 재미있을 거 같아!")]
T3 = [('A', "Look at these houses. They look very natural.", "이 집들을 봐. 매우 자연 그대로인 것 같아."), ('B', "Wow, I wish I could try living there!", "와, 저곳에서 살아 봤으면 좋겠어!"),
      ('A', "Which house would you most like to live in?", "어떤 집에서 가장 살고 싶니?"), ('B', "I wish I could live in the stone house. It looks very strong.", "돌집에서 살아 보고 싶어. 매우 튼튼해 보여.")]
L7a = ['7과 Listen & Speak 1-A · 튀르키예 동굴 집', '7과 Listen & Speak 1-B · 알래스카 눈집', '7과 Listen & Speak 1-C · Talk Together']
P7a = dlg(L7a[0], T1) + dlg(L7a[1], T2) + dlg(L7a[2], T3)
j7a = build(
 vocab=[['hear from', '~에게서 소식을 듣다'], ['take a look', '한번 보다'], ['cave house', '동굴 집'], ['unique', '독특한'], ['I wish I could ~', '~할 수 있으면 좋을 텐데 (바람·소원)'],
        ['try -ing', '시험 삼아 ~해 보다'], ['balloon', '풍선'], ['some day', '언젠가'], ['I have no idea.', '모르겠어.'], ['sled', '썰매'],
        ["can't wait to ~", '빨리 ~하고 싶다'], ['test out', '~을 시험해 보다'], ['for a while', '당분간'], ['go sledding', '썰매 타러 가다'], ['No kidding!', '농담 마!'],
        ['on vacation', '방학 때, 휴가 중에'], ['natural', '자연 그대로의'], ['stone', '돌']],
 pickv=[
  (T(T1, 4).replace('so unique', 'so {unique|common}'), "정답 ▶ unique (독특한)\n오답 ▶ common (흔한): 동굴 집이 '독특해 보여서' 그곳에서 살아 보고 싶다고 해요."),
  (T(T2, 5).replace('very cold', 'very {cold|hot}'), "정답 ▶ cold (추운)\n오답 ▶ hot: 눈이 오고 썰매를 탈 수 있는 알래스카 → '추운' 곳"),
  (T(T3, 3).replace('very strong', 'very {strong|weak}'), "정답 ▶ strong (튼튼한)\n오답 ▶ weak (약한): 돌로 만든 집이니 '튼튼해 보인다'"),
 ],
 tf=[
  ("Julia is traveling in Türkiye.", True, "정답 ▶ T\n이유: She's traveling in Türkiye, right? → Yes", None, "She's traveling in Türkiye"),
  ("The girl wishes she could live in a balloon.", False, "정답 ▶ F\n이유: 소녀가 살아 보고 싶은 곳은 동굴 집(cave houses)이에요. 풍선을 좋아하는 건 소년이에요.", None, "I wish I could try living there"),
  ("Taeho got a new sled for his birthday.", True, "정답 ▶ T\n이유: I got a new sled for my birthday.", None, "I got a new sled for my birthday"),
  ("It will snow a lot soon.", False, "정답 ▶ F\n이유: 당분간 눈 소식이 없다(no snow for a while)고 했어요.", None, "there will be no snow for a while"),
  ("The girl thinks Alaska is a warm place.", False, "정답 ▶ F\n이유: Alaska is a very cold place.", None, "Alaska is a very cold place"),
  ("Taeho wants to build a snow house.", True, "정답 ▶ T\n이유: I want to build a snow house and stay there on vacation.", None, "I want to build a snow house"),
 ],
 resp=[
  ("A: Which house would you most like to live in?", ['I wish I could live in the stone house.', 'I got a new sled.', 'Yes, please.', 'I have no idea about the weather.'],
   "정답 ▶ I wish I could live in the stone house.\n이유: 어떤 집에서 가장 살고 싶은지 물었으니 → I wish I could live in ~.(~에서 살아 보고 싶어)로 답해요."),
  ("A: Will it snow today?", ['I have no idea.', 'Yes, please.', 'Me too!', 'Take a look.'],
   "정답 ▶ I have no idea.\n이유: 눈이 올지 묻는 말에 '모르겠어'로 답하고, 이어서 날씨를 확인해 봐요."),
 ],
 ilchi=[
  {'box': [L7a[0]], 'q': "대화의 내용과 일치하지 <u>않는</u> 것은?",
   'opts': ["The girl doesn't want to see the pictures.", "Julia sent some pictures to the boy.", "The girl thinks the cave houses look unique.", "The boy likes the balloons in the pictures.", "The girl hopes to visit Türkiye some day."],
   'ex': "정답 ▶ The girl doesn't want to see the pictures.\n이유: 사진을 볼래(Do you want to see them?)라는 말에 Yes, please.라고 했어요.",
   'per': [["소녀는 사진을 보고 싶어 하지 않는다.", "Yes, please", "불일치"], ["Julia가 소년에게 사진을 보냈다.", "she sent me some pictures", "일치"],
           ["소녀는 동굴 집이 독특해 보인다고 생각한다.", "They look so unique", "일치"], ["소년은 사진 속 풍선이 마음에 든다.", "I like those balloons", "일치"],
           ["소녀는 언젠가 튀르키예에 가 보고 싶어 한다.", "I hope to visit there some day", "일치"]]},
  {'box': [L7a[1]], 'q': "대화의 내용과 일치하지 <u>않는</u> 것은?",
   'opts': ["Taeho doesn't want to go sledding.", "Taeho got a sled for his birthday.", "There will be no snow for a while.", "Taeho wishes he could live in Alaska.", "The girl thinks living in a snow house sounds fun."],
   'ex': "정답 ▶ Taeho doesn't want to go sledding.\n이유: 알래스카에 살면 온종일 썰매를 탈 수 있다(I could go sledding all day!)며 썰매를 무척 타고 싶어 해요.",
   'per': [["태호는 썰매 타러 가고 싶지 않다.", "Then I could go sledding all day", "불일치"], ["태호는 생일 선물로 썰매를 받았다.", "I got a new sled for my birthday", "일치"],
           ["당분간 눈이 오지 않는다.", "there will be no snow for a while", "일치"], ["태호는 알래스카에서 살기를 바란다.", "I wish I could live in Alaska", "일치"],
           ["소녀는 눈집에서 사는 것이 재미있겠다고 한다.", "Living in a snow house sounds fun", "일치"]]},
 ],
 pickg=[
  (T(T1, 4).replace('I wish I could try', 'I wish I {could|can} try'), "정답 ▶ could\n이유: I wish + 주어 + 과거형(could) = ~할 수 있으면 좋을 텐데 (현재 이루기 힘든 바람). can은 쓰지 않아요."),
  (T(T1, 5).replace('look so beautiful', 'look so {beautiful|beautifully}'), "정답 ▶ beautiful\n이유: 감각동사 look + 형용사 = ~해 보이다. 부사(beautifully)는 쓰지 않아요."),
  (T(T1, 6).replace('place to visit', 'place {to visit|visiting}'), "정답 ▶ to visit\n이유: 명사(a wonderful place)를 뒤에서 꾸미는 to부정사(형용사적 용법) = 방문하기에 멋진 곳"),
  (T(T2, 2).replace("can't wait to test", "can't wait {to test|testing}"), "정답 ▶ to test\n이유: I can't wait to + 동사원형 = 빨리 ~하고 싶다 (기대)"),
  (T(T2, 7).replace('sounds fun', '{sounds|sound} fun'), "정답 ▶ sounds\n이유: 동명사구 주어(Living in a snow house)는 단수 취급 → sounds"),
 ],
 error=[
  ER("Yes, she [[sent]] me some pictures. Do you want [[seeing]] [[them]]?", 1, 'to see',
     "틀린 곳 ▶ ② seeing → to see\n이유: want는 to부정사를 목적어로 써요 (want to see).\n나머지 ▶ ① sent(send의 과거, send + 사람 + 사물) ✔ ③ them(= some pictures) ✔"),
  ER("I think it would be fun. I want to [[build]] a snow house and [[stays]] there [[on]] vacation.", 1, 'stay',
     "틀린 곳 ▶ ② stays → stay\n이유: want to build ~ and (to) stay ~. and 앞뒤가 to부정사로 나란히 연결돼요(병렬). to 뒤는 동사원형\n나머지 ▶ ① build ✔ ③ on vacation(방학 때) ✔"),
 ],
 scr=[("I wish I could try living there.", "난 그곳에서 살아 봤으면 좋겠어."), ("Then I could go sledding all day!", "그러면 온종일 썰매 탈 수 있을 텐데!")],
 order=[([T(T2, i) for i in range(5)], ["B: 오늘 눈이 올까?", "G: 모르겠어, 왜 눈을 기다려?", "B: 새 썰매를 받아서 시험해 보고 싶어", "G: 당분간 눈 소식이 없어", "B: 알래스카에 살면 좋겠다"])],
 blank=[
  (T(T2, 3).replace('for a while', 'for a ____'), ['while', 'sled', 'house', 'birthday'], "정답 ▶ while\n이유: for a while = 당분간. 눈을 기다리는 태호에게 '당분간 눈이 없다'고 알려 줘요."),
  (T(T1, 6).replace('I hope to visit', 'I hope to ____'), ['visit', 'leave', 'forget', 'sell'], "정답 ▶ visit\n이유: 튀르키예가 '방문하기에 멋진 곳'이라 했으니 언젠가 '방문하고' 싶다는 말이 이어져요."),
 ],
 awk=[(["A: Which house would you like to live in? B: Yes, I would.", "A: Have you heard from Julia? B: Yes, she sent me some pictures.", "A: Will it snow today? B: I have no idea.", "A: I wish I could live in Alaska. B: No kidding! It's a very cold place."],
       "정답 ▶ A: Which house would you like to live in? B: Yes, I would.\n이유: Which house ~?(어떤 집?)는 의문사 의문문이라 Yes/No로 답할 수 없어요. → I'd like to live in the stone house.처럼 답해요.")],
 func=[
  ("밑줄 친 문장과 의미가 가장 가까운 것은?<br><b><u>I wish I could live in Alaska.</u></b>", ["I'd like to live in Alaska, but I can't.", 'I live in Alaska now.', 'I lived in Alaska before.', "I don't want to live in Alaska."],
   "정답 ▶ I'd like to live in Alaska, but I can't.\n이유: I wish I could ~는 '(실제로는 못 하지만) ~할 수 있으면 좋을 텐데'라는 바람이에요. 지금 알래스카에 살고 있지 않다는 뜻이 들어 있어요."),
  ("밑줄 친 부분과 바꿔 쓸 수 있는 것은?<br><b>I <u>can't wait to</u> test it out.</b>", ['really want to', "don't want to", 'forgot to', 'decided not to'],
   "정답 ▶ really want to\n이유: can't wait to ~ = 빨리 ~하고 싶다 (기대). = I'm looking forward to testing it out."),
 ],
 summ=[
  S([L7a[0]], "The girl wishes she could try (A) ______ in the cave houses in Türkiye, and she hopes to (B) ______ there some day.",
    ['(A) living – (B) visit', '(A) cooking – (B) visit', '(A) living – (B) leave', '(A) flying – (B) work', '(A) sleeping – (B) forget'],
    "정답 ▶ (A) living – (B) visit\n(A) 동굴 집에서 '살아' 보고 싶다 → try living\n(B) 언젠가 '방문하고' 싶다 → visit",
    ["I wish I could try living there", "I hope to visit there some day"]),
  S([L7a[1]], "Taeho wishes he could live in Alaska because he could go (A) ______ all day, but the girl says Alaska is a very (B) ______ place.",
    ['(A) sledding – (B) cold', '(A) swimming – (B) cold', '(A) sledding – (B) hot', '(A) shopping – (B) busy', '(A) fishing – (B) warm'],
    "정답 ▶ (A) sledding – (B) cold\n(A) 온종일 '썰매'를 탈 수 있다 → sledding\n(B) 알래스카는 매우 '추운' 곳 → cold",
    ["Then I could go sledding all day", "Alaska is a very cold place"])],
)

# ═════════════ 7과 ② Listen & Speak 2-A (상상하여 말하기) ═════════════
U1 = [('B', "This is my dream house, Alice. What do you think?", "이건 내가 꿈꾸는 집이야, Alice. 어떻게 생각해?"), ('G', "Oh, the house has wheels! Is it a kind of car?", "오, 집에 바퀴가 달려 있네! 자동차의 일종이니?"),
      ('B', "Yes, it can move like a car.", "응, 이건 자동차처럼 움직일 수 있어."), ('G', "So what would you do if you lived in that house?", "그래서 만약 네가 그 집에 산다면 너는 무엇을 할 거니?"),
      ('B', "I would travel to many places with my family.", "난 가족과 함께 많은 곳을 여행할 거야."), ('G', "That sounds cool.", "멋진데.")]
U2 = [('G', "What would you do if you became a millionaire, Juwon?", "만약 네가 백만장자가 된다면 너는 무엇을 할 거니, 주원아?"), ('B', "I would build my own house.", "난 나만의 집을 지을 거야."),
      ('G', "What kind of house would you build?", "어떤 집을 지을 건데?"), ('B', "I would build a house that is completely covered with mirrors.", "난 거울로 완전히 뒤덮인 집을 지을 거야."),
      ('G', "Why?", "왜?"), ('B', "The mirrors would make the house almost invisible. Wouldn't that be cool?", "거울이 집을 거의 보이지 않게 해 줄 거야. 멋지지 않니?"),
      ('G', "That would be cool!", "멋지겠는데!")]
U3 = [('G', "Look. The house in this picture is upside down.", "봐. 이 사진 속의 집은 거꾸로 되어 있어."), ('B', "That's interesting. Does anybody live there?", "재미있는데. 거기 누군가가 살고 있니?"),
      ('G', "No, it would not be easy to live there because the inside is also upside down.", "아니, 집 안쪽도 거꾸로 되어 있어서 그곳에 살기가 쉽지는 않을 거야."),
      ('B', "Really? But I want to try living there.", "정말? 하지만 나는 그곳에서 살아 보고 싶어."), ('G', "What would you do if you lived in that house?", "만약 네가 그 집에 산다면 너는 무엇을 할 거니?"),
      ('B', "I would walk upside down like Spider-Man. I could also see things differently.", "스파이더맨처럼 거꾸로 매달려 걸어 다닐 거야. 난 또한 사물들을 다르게 볼 수 있을 거야.")]
L7b = ['7과 Listen & Speak 2-A 1 · 바퀴 달린 집', '7과 Listen & Speak 2-A 2 · 거울 집', '7과 Listen & Speak 2-A 3 · 거꾸로 된 집']
P7b = dlg(L7b[0], U1) + dlg(L7b[1], U2) + dlg(L7b[2], U3)
j7b = build(
 vocab=[['dream house', '꿈의 집'], ['wheel', '바퀴'], ['a kind of', '~의 일종'], ['move', '움직이다'], ['What would you do if ~?', '만약 ~라면 너는 무엇을 할 거니? (상상하여 말하기)'],
        ['travel', '여행하다'], ['millionaire', '백만장자'], ['own', '자신의'], ['completely', '완전히'], ['be covered with', '~으로 뒤덮이다'],
        ['mirror', '거울'], ['almost', '거의'], ['invisible', '보이지 않는'], ['upside down', '거꾸로'], ['anybody', '누군가'], ['inside', '안쪽, 내부'], ['differently', '다르게']],
 pickv=[
  (T(U1, 1).replace('has wheels', 'has {wheels|windows}'), "정답 ▶ wheels (바퀴)\n오답 ▶ windows (창문): 바로 뒤에 '자동차의 일종이니?'라고 묻고, 자동차처럼 움직인다고 해요."),
  (T(U2, 5).replace('almost invisible', 'almost {invisible|visible}'), "정답 ▶ invisible (보이지 않는)\n오답 ▶ visible (보이는): 거울이 주변을 비춰서 집이 '거의 안 보이게' 돼요. 그래서 멋지다고 해요."),
  (T(U3, 5).replace('things differently', 'things {differently|similarly}'), "정답 ▶ differently (다르게)\n오답 ▶ similarly (비슷하게): 거꾸로 매달려 다니면 사물을 '다르게' 볼 수 있어요."),
 ],
 tf=[
  ("The boy's dream house can move like a car.", True, "정답 ▶ T\n이유: Yes, it can move like a car.", None, "it can move like a car"),
  ("The boy would travel alone if he lived in the house.", False, "정답 ▶ F\n이유: 혼자가 아니라 가족과 함께(with my family) 여행할 거예요.", None, "I would travel to many places with my family"),
  ("Juwon would build a house covered with mirrors.", True, "정답 ▶ T\n이유: a house that is completely covered with mirrors", None, "I would build a house that is completely covered with mirrors"),
  ("Juwon wants a house that everyone can see easily.", False, "정답 ▶ F\n이유: 거울로 집이 거의 보이지 않게(almost invisible) 만들고 싶어 해요.", None, "The mirrors would make the house almost invisible"),
  ("Many people live in the upside-down house.", False, "정답 ▶ F\n이유: 누가 사냐는 질문에 No라고 했어요. 안쪽도 거꾸로라 살기 쉽지 않아요.", None, "No, it would not be easy to live there"),
  ("The boy wants to try living in the upside-down house.", True, "정답 ▶ T\n이유: But I want to try living there.", None, "But I want to try living there"),
 ],
 resp=[
  ("A: What would you do if you became a millionaire?", ['I would build my own house.', 'I built my own house.', 'Yes, I would.', 'That sounds cool.'],
   "정답 ▶ I would build my own house.\n이유: What would you do if ~?(상상하여 묻기)에는 I would + 동사원형으로 답해요.\n오답 ▶ built(과거 사실) / Yes, I would.(의문사 의문문에 Yes 불가)"),
  ("A: Does anybody live there?", ['No, it would not be easy to live there.', 'Yes, I would travel.', 'I would walk upside down.', 'That would be cool!'],
   "정답 ▶ No, it would not be easy to live there.\n이유: Does ~?에 No로 답하고 이유(살기 쉽지 않다)를 덧붙여요."),
 ],
 ilchi=[
  {'box': [L7b[1]], 'q': "대화의 내용과 일치하지 <u>않는</u> 것은?",
   'opts': ["Juwon is already a millionaire.", "Juwon would build his own house.", "The house would be completely covered with mirrors.", "The mirrors would make the house almost invisible.", "The girl thinks the house would be cool."],
   'ex': "정답 ▶ Juwon is already a millionaire.\n이유: What would you do if you became a millionaire?는 '만약 백만장자가 된다면'이라는 상상(가정법)이에요. 실제로는 백만장자가 아니에요.",
   'per': [["주원이는 이미 백만장자이다.", "What would you do if you became a millionaire", "불일치 → 상상"], ["주원이는 자신만의 집을 지을 것이다.", "I would build my own house", "일치"],
           ["그 집은 거울로 완전히 뒤덮일 것이다.", "completely covered with mirrors", "일치"], ["거울이 집을 거의 보이지 않게 할 것이다.", "almost invisible", "일치"],
           ["소녀는 그 집이 멋질 거라고 생각한다.", "That would be cool", "일치"]]},
  {'box': [L7b[2]], 'q': "대화의 내용과 일치하지 <u>않는</u> 것은?",
   'opts': ["The girl thinks it would be easy to live in the house.", "The house in the picture is upside down.", "Nobody lives in the house.", "The inside of the house is upside down, too.", "The boy would walk upside down like Spider-Man."],
   'ex': "정답 ▶ The girl thinks it would be easy to live in the house.\n이유: 소녀는 안쪽도 거꾸로라서 살기가 쉽지 않을 것(would not be easy)이라고 했어요.",
   'per': [["소녀는 그 집에 살기 쉬울 거라고 생각한다.", "it would not be easy to live there", "불일치"], ["사진 속 집은 거꾸로 되어 있다.", "The house in this picture is upside down", "일치"],
           ["그 집에는 아무도 살지 않는다.", "Does anybody live there", "일치 (No)"], ["집 안쪽도 거꾸로 되어 있다.", "the inside is also upside down", "일치"],
           ["소년은 스파이더맨처럼 거꾸로 걸어 다닐 것이다.", "I would walk upside down like Spider-Man", "일치"]]},
 ],
 pickg=[
  (T(U1, 3).replace('if you lived', 'if you {lived|live}'), "정답 ▶ lived\n이유: 가정법 과거 → What would you do if + 주어 + 동사의 과거형 ~? (현재 사실과 반대되는 상상)"),
  (T(U2, 3).replace('that is completely', 'that {is|are} completely'), "정답 ▶ is\n이유: 주격 관계대명사 that의 동사는 선행사(a house, 단수)에 맞춰요 → is"),
  (T(U2, 5).replace('almost invisible', 'almost {invisible|invisibly}'), "정답 ▶ invisible\n이유: make + 목적어(the house) + 형용사(목적격 보어) = ~을 …하게 만들다. 부사는 보어가 될 수 없어요."),
  (T(U3, 2).replace('easy to live', 'easy {to live|live}'), "정답 ▶ to live\n이유: 가주어 it ~ 진주어 to부정사: it would not be easy to live there (그곳에 사는 것은 쉽지 않을 것이다)"),
  (T(U3, 3).replace('try living', 'try {living|lived}'), "정답 ▶ living\n이유: try + 동명사 = 시험 삼아 ~해 보다. lived(과거형)는 try 뒤에 올 수 없어요."),
 ],
 error=[
  ER("What [[would]] you [[do]] if you [[become]] a millionaire, Juwon?", 2, 'became',
     "틀린 곳 ▶ ③ become → became\n이유: 가정법 과거: if절에는 동사의 과거형, 주절에는 would + 동사원형\n나머지 ▶ ① would ✔ ② do ✔"),
  ER("Look. The house [[in]] this picture [[are]] upside [[down]].", 1, 'is',
     "틀린 곳 ▶ ② are → is\n이유: 주어는 The house(단수). in this picture는 주어를 꾸미는 말이에요.\n나머지 ▶ ① in ✔ ③ upside down(거꾸로) ✔"),
 ],
 scr=[(T(U1, 4), U1[4][2]), (T(U2, 3), U2[3][2])],
 order=[([T(U3, i) for i in range(5)], ["G: 사진 속 집이 거꾸로야", "B: 재미있다, 누가 살아?", "G: 아니, 안쪽도 거꾸로라 살기 어려워", "B: 그래도 살아 보고 싶어", "G: 그 집에 살면 뭘 할 거야?"])],
 blank=[
  (T(U2, 3).replace('with mirrors', 'with ____'), ['mirrors', 'wheels', 'snow', 'flowers'], "정답 ▶ mirrors\n이유: 다음 말에서 The mirrors would make the house almost invisible.이라고 이유를 설명해요."),
  (T(U3, 2).replace('also upside down', 'also upside ____'), ['down', 'up', 'out', 'off'], "정답 ▶ down\n이유: upside down = 거꾸로. 집 바깥처럼 안쪽도 '거꾸로'라서 살기 어려워요."),
 ],
 awk=[(["A: Does anybody live there? B: Yes, I would live there yesterday.", "A: What would you do if you lived in a tree house? B: I would read books there.", "A: What kind of house would you build? B: I would build a house covered with mirrors.", "A: Wouldn't that be cool? B: That would be cool!"],
       "정답 ▶ A: Does anybody live there? B: Yes, I would live there yesterday.\n이유: 지금 누가 사는지(Does ~?) 물었는데, would와 yesterday(과거)를 섞어 엉뚱하게 답했어요.")],
 func=[
  ("상상하여 묻는 표현으로 알맞은 것은?", ['What would you do if you lived in that house?', 'What did you do in that house?', 'Do you live in that house?', 'Where is your house?'],
   "정답 ▶ What would you do if you lived in that house?\n이유: What would you do if + 과거형 ~? = 만약 ~라면 무엇을 할 거니? (= Imagine that ~. What would you do?)"),
  ("밑줄 친 말의 의도로 알맞은 것은?<br><b>B: The mirrors would make the house almost invisible. <u>Wouldn't that be cool?</u></b>", ['상대방의 동의를 구하기', '허락 구하기', '길 묻기', '사과하기'],
   "정답 ▶ 상대방의 동의를 구하기\n이유: Wouldn't that be cool? = 멋지지 않겠니? (부정의문문으로 상대도 그렇게 생각하는지 물어요.) → That would be cool!"),
 ],
 summ=[
  S([L7b[0], L7b[1]], "If the boy lived in his dream house with (A) ______, he would travel with his family, and if Juwon became a millionaire, he would build a house covered with (B) ______.",
    ['(A) wheels – (B) mirrors', '(A) mirrors – (B) wheels', '(A) wheels – (B) flowers', '(A) windows – (B) mirrors', '(A) wings – (B) snow'],
    "정답 ▶ (A) wheels – (B) mirrors\n(A) '바퀴' 달린 꿈의 집 → wheels\n(B) '거울'로 뒤덮인 집 → mirrors\n오답 ▶ ②는 두 낱말을 바꾼 함정!",
    ["the house has wheels", "completely covered with mirrors"]),
  S([L7b[2]], "It would not be (A) ______ to live in the upside-down house, but the boy wants to try living there to see things (B) ______.",
    ['(A) easy – (B) differently', '(A) hard – (B) differently', '(A) easy – (B) clearly', '(A) fun – (B) the same', '(A) safe – (B) slowly'],
    "정답 ▶ (A) easy – (B) differently\n(A) 살기 '쉽지' 않다 → not easy\n(B) 사물을 '다르게' 본다 → differently",
    ["it would not be easy to live there", "I could also see things differently"])],
)

# ═════════════ 7과 ③ Listen & Speak 2-B · Real Life Communication ═════════════
V1 = [('G', "Dohun, we need to start our project on our dream country to visit.", "도훈아, 우리가 가 보기를 꿈꾸는 나라에 대한 과제를 시작해야 해."),
      ('B', "That's right. Which country do you want to visit, Emma?", "맞아. 너는 어떤 나라를 가 보고 싶니, Emma?"), ('G', "In my case, I want to visit Spain.", "내 경우에는 스페인에 가 보고 싶어."),
      ('B', "What would you do if you visited Spain?", "만약 네가 스페인을 방문한다면 너는 무엇을 할 거니?"),
      ('G', "I'm interested in buildings. So I would go see La Sagrada Familia.", "난 건축물에 관심이 있어. 그래서 나는 사그라다 파밀리아 성당을 보러 갈 거야."),
      ('B', "Isn't that the church Antoni Gaudí designed?", "그 성당은 Antoni Gaudí가 설계한 거 아니니?"),
      ('G', "Yes, it is. It would be interesting to see how his design was inspired by nature.", "응, 맞아. 그의 디자인이 어떻게 자연으로부터 영감을 받았는지 보는 것은 재미있을 거야."),
      ('B', "Hmm... How about Gaudí and Spain as the title for our project?", "음…. 'Gaudí와 스페인'을 우리 과제의 제목으로 하면 어때?"), ('G', "I love it!", "아주 좋아!")]
V2 = [('Jinho', "I think living in a jungle would be really exciting. Don't you think so?", "내 생각에 정글에 사는 것은 정말 재미있을 것 같아. 그렇게 생각하지 않니?"),
      ('Claire', "But there are some dangerous animals in the jungle, Jinho.", "하지만 정글에는 몇몇 위험한 동물들이 있어, 진호야."),
      ('Jinho', "I know. But the jungle is full of adventure. I wish I could live there.", "나도 알아. 하지만 정글은 모험으로 가득 차 있어. 나는 그곳에서 살아 보고 싶어."),
      ('Claire', "What would you do if you lived in the jungle?", "만약 네가 정글에서 산다면 너는 무엇을 할 거니?"),
      ('Jinho', "I would explore it. Maybe I could make some animal friends.", "나는 정글 탐험을 할 거야. 어쩌면 난 몇몇 동물 친구들을 만들 수도 있겠지."),
      ('Claire', "Then where would you sleep? In a cave?", "그러면 잠은 어디서 잘 거야? 동굴 안에서?"),
      ('Jinho', "No, I would stay in a tree house. Then I would be safe from dangerous animals.", "아냐, 난 나무 집에서 지낼 거야. 그러면 위험한 동물들로부터 안전할 거야."),
      ('Claire', "That makes sense.", "일리가 있네.")]
L7c = ['7과 Listen & Speak 2-B · 스페인과 가우디', '7과 Real Life Communication · 정글에서 산다면']
P7c = dlg(L7c[0], V1) + dlg(L7c[1], V2)
j7c = build(
 vocab=[['project', '과제, 프로젝트'], ['dream country', '가 보기를 꿈꾸는 나라'], ["in one's case", '~의 경우에는'], ['go see', '보러 가다'], ['church', '성당, 교회'],
        ['design', '설계하다; 디자인'], ['be inspired by', '~에서 영감을 받다'], ['title', '제목'], ['jungle', '정글'], ['exciting', '신나는, 흥미진진한'],
        ["Don't you think so?", '그렇게 생각하지 않니? (동의 구하기)'], ['dangerous', '위험한'], ['be full of', '~으로 가득 차다'], ['adventure', '모험'],
        ['explore', '탐험하다'], ['cave', '동굴'], ['tree house', '나무 위의 집'], ['be safe from', '~로부터 안전하다'], ['That makes sense.', '일리가 있네.']],
 pickv=[
  (T(V1, 4).replace('interested in buildings', 'interested in {buildings|animals}'), "정답 ▶ buildings (건축물)\n오답 ▶ animals: 사그라다 파밀리아 '성당'을 보러 가는 이유 → 건축물에 관심이 있어서"),
  (T(V2, 2).replace('full of adventure', 'full of {adventure|boredom}'), "정답 ▶ adventure (모험)\n오답 ▶ boredom (지루함): 정글에 사는 게 정말 신날 것(exciting)이라 했으니 '모험'으로 가득해요."),
  (T(V2, 6).replace('be safe from', 'be {safe|afraid} from'), "정답 ▶ safe (안전한)\n오답 ▶ afraid: 나무 위의 집에서 지내면 위험한 동물로부터 '안전할' 거예요. (afraid는 of와 써요: be afraid of)"),
 ],
 tf=[
  ("Emma wants to visit Spain.", True, "정답 ▶ T\n이유: In my case, I want to visit Spain.", None, "I want to visit Spain"),
  ("Emma is interested in music.", False, "정답 ▶ F\n이유: 음악이 아니라 건축물(buildings)에 관심이 있어요.", None, "I'm interested in buildings"),
  ("La Sagrada Familia is the church Antoni Gaudí designed.", True, "정답 ▶ T\n이유: Isn't that the church Antoni Gaudí designed? → Yes, it is.", None, "Isn't that the church Antoni Gaudí designed"),
  ("Dohun suggests \"Gaudí and Spain\" as the title.", True, "정답 ▶ T\n이유: How about Gaudí and Spain as the title for our project?", None, "How about Gaudí and Spain as the title for our project"),
  ("Claire thinks there are no dangerous animals in the jungle.", False, "정답 ▶ F\n이유: there are some dangerous animals in the jungle", None, "there are some dangerous animals in the jungle"),
  ("Jinho would sleep in a cave in the jungle.", False, "정답 ▶ F\n이유: 동굴이 아니라 나무 위의 집(a tree house)에서 지낼 거예요.", None, "No, I would stay in a tree house"),
 ],
 resp=[
  ("A: What would you do if you visited Spain?", ['I would go see La Sagrada Familia.', 'I visited Spain last year.', 'I love it!', 'That makes sense.'],
   "정답 ▶ I would go see La Sagrada Familia.\n이유: 상상하여 묻는 말(What would you do if ~?) → I would + 동사원형으로 답해요."),
  ("A: Then where would you sleep? In a cave?", ['No, I would stay in a tree house.', 'Yes, I explored it.', "I'm interested in buildings.", 'I love it!'],
   "정답 ▶ No, I would stay in a tree house.\n이유: 어디서 잘지(동굴?) 물었으니 → 아니, 나무 위의 집에서 지낼 거야."),
 ],
 ilchi=[
  {'box': [L7c[0]], 'q': "대화의 내용과 일치하지 <u>않는</u> 것은?",
   'opts': ["Emma doesn't like the title Dohun suggested.", "Emma and Dohun need to start a project.", "Emma wants to visit Spain.", "Emma would go see La Sagrada Familia.", "Gaudí's design was inspired by nature."],
   'ex': "정답 ▶ Emma doesn't like the title Dohun suggested.\n이유: 도훈이가 제안한 제목에 I love it!(아주 좋아!)이라고 했어요.",
   'per': [["Emma는 도훈이가 제안한 제목이 마음에 들지 않는다.", "I love it", "불일치"], ["Emma와 도훈이는 과제를 시작해야 한다.", "we need to start our project", "일치"],
           ["Emma는 스페인에 가 보고 싶어 한다.", "I want to visit Spain", "일치"], ["Emma는 사그라다 파밀리아를 보러 갈 것이다.", "So I would go see La Sagrada Familia", "일치"],
           ["가우디의 디자인은 자연에서 영감을 받았다.", "how his design was inspired by nature", "일치"]]},
  {'box': [L7c[1]], 'q': "대화의 내용과 일치하지 <u>않는</u> 것은?",
   'opts': ["Claire disagrees with Jinho's idea of a tree house.", "Jinho thinks living in a jungle would be exciting.", "Claire says there are dangerous animals in the jungle.", "Jinho would explore the jungle.", "Jinho would stay in a tree house."],
   'ex': "정답 ▶ Claire disagrees with Jinho's idea of a tree house.\n이유: 나무 위의 집에서 지내겠다는 말에 That makes sense.(일리가 있네)라고 동의했어요.",
   'per': [["Claire는 나무 위의 집 생각에 반대한다.", "That makes sense", "불일치 → 동의함"], ["진호는 정글에 사는 것이 신날 거라고 생각한다.", "living in a jungle would be really exciting", "일치"],
           ["Claire는 정글에 위험한 동물이 있다고 말한다.", "there are some dangerous animals in the jungle", "일치"], ["진호는 정글을 탐험할 것이다.", "I would explore it", "일치"],
           ["진호는 나무 위의 집에서 지낼 것이다.", "I would stay in a tree house", "일치"]]},
 ],
 pickg=[
  (T(V1, 0).replace('country to visit', 'country {to visit|visit}'), "정답 ▶ to visit\n이유: 명사(our dream country)를 꾸미는 to부정사(형용사적 용법) = 방문하기를 꿈꾸는 나라"),
  (T(V1, 3).replace('if you visited', 'if you {visited|visit}'), "정답 ▶ visited\n이유: 가정법 과거: What would you do if + 주어 + 과거형 ~?"),
  (T(V1, 6).replace('how his design was inspired', 'how his design {was inspired|inspired}'), "정답 ▶ was inspired\n이유: 디자인이 자연에 의해 영감을 '받은' 것 → 수동태 be + p.p. + by"),
  (T(V1, 6).replace('how his design was inspired', '{how his design was|how was his design} inspired'), "정답 ▶ how his design was\n이유: 간접의문문(동사 see의 목적어) → 의문사 + 주어 + 동사 어순"),
  (T(V2, 0).replace('I think living', 'I think {living|live}'), "정답 ▶ living\n이유: that절의 주어 자리 → 동명사 living (= to live). 정글에 사는 것은 ~"),
  (T(V2, 1).replace('there are some', 'there {are|is} some'), "정답 ▶ are\n이유: there + be동사 뒤의 명사(some dangerous animals, 복수)에 맞춰 are"),
  (T(V2, 2).replace('I wish I could live', 'I wish I {could|can} live'), "정답 ▶ could\n이유: I wish + 주어 + could = ~할 수 있으면 좋을 텐데 (현재 이루기 힘든 바람)"),
 ],
 error=[
  ER("I'm [[interesting]] [[in]] buildings. So I [[would]] go see La Sagrada Familia.", 0, 'interested',
     "틀린 곳 ▶ ① interesting → interested\n이유: 사람이 관심을 '느끼는' 것 → be interested in. interesting은 '흥미를 주는'\n나머지 ▶ ② in ✔ ③ would(상상) ✔"),
  ER("No, I would [[stay]] in a tree house. Then I would be [[safety]] from [[dangerous]] animals.", 1, 'safe',
     "틀린 곳 ▶ ② safety → safe\n이유: be동사 뒤 보어 자리 → 형용사 safe. be safe from ~로부터 안전하다 (safety는 명사)\n나머지 ▶ ① stay ✔ ③ dangerous(형용사) ✔"),
 ],
 scr=[("It would be interesting to see how his design was inspired by nature.", "그의 디자인이 어떻게 자연으로부터 영감을 받았는지 보는 것은 재미있을 거야."),
      ("Then I would be safe from dangerous animals.", "그러면 위험한 동물들로부터 안전할 거야.")],
 order=[([T(V2, i) for i in range(4)], ["Jinho: 정글에 살면 신날 것 같아", "Claire: 위험한 동물이 있잖아", "Jinho: 알아, 그래도 모험이 가득해", "Claire: 정글에 살면 뭘 할 거야?"])],
 blank=[
  (T(V1, 7).replace('as the title', 'as the ____'), ['title', 'church', 'country', 'design'], "정답 ▶ title (제목)\n이유: 과제를 시작하며 'Gaudí and Spain'을 과제의 '제목'으로 제안해요."),
  (T(V2, 5).replace('In a cave?', 'In a ____?'), ['cave', 'tree house', 'church', 'project'], "정답 ▶ cave (동굴)\n이유: 다음 말이 No, I would stay in a tree house.예요. tree house를 물었다면 No라고 할 수 없어요."),
 ],
 awk=[(["A: What would you do if you visited Spain? B: I visited Spain last summer.", "A: Which country do you want to visit? B: In my case, I want to visit Spain.", "A: Don't you think so? B: Yes, I think so, too.", "A: I would stay in a tree house. B: That makes sense."],
       "정답 ▶ A: What would you do if you visited Spain? B: I visited Spain last summer.\n이유: 상상하여 물었는데(would) 과거 사실로 답했어요. → I would ~.로 답해야 해요.")],
 func=[("밑줄 친 말과 의미가 가장 가까운 것은?<br><b>Claire: <u>That makes sense.</u></b>", ['That sounds reasonable.', "That's not true.", "I don't understand.", "That's too bad."],
        "정답 ▶ That sounds reasonable.\n이유: That makes sense. = 일리가 있네, 말이 되네. (상대 말에 동의)")],
 summ=[
  S([L7c[0]], "Emma, who is interested in (A) ______, would visit La Sagrada Familia to see how Gaudí's design was inspired by (B) ______.",
    ['(A) buildings – (B) nature', '(A) music – (B) nature', '(A) buildings – (B) people', '(A) animals – (B) art', '(A) food – (B) history'],
    "정답 ▶ (A) buildings – (B) nature\n(A) '건축물'에 관심 → buildings\n(B) 가우디의 디자인은 '자연'에서 영감 → nature",
    ["I'm interested in buildings", "how his design was inspired by nature"]),
  S([L7c[1]], "Jinho thinks the jungle is full of (A) ______, and he would stay in a tree house to be (B) ______ from dangerous animals.",
    ['(A) adventure – (B) safe', '(A) trash – (B) safe', '(A) adventure – (B) bored', '(A) water – (B) tired', '(A) danger – (B) famous'],
    "정답 ▶ (A) adventure – (B) safe\n(A) 정글은 '모험'으로 가득 → adventure\n(B) 위험한 동물로부터 '안전' → safe",
    ["the jungle is full of adventure", "Then I would be safe from dangerous animals"])],
)

# ═════════════ 8과 ① Listen & Speak 1 (상술하기) ═════════════
W1 = [('B', "Minju, what is this graph about?", "민주야, 이 그래프는 무엇에 관한 거야?"), ('G', "I did a survey on the kinds of pets my classmates have.", "나는 우리 반 친구들이 가지고 있는 애완동물의 종류에 대해 설문 조사를 했어."),
      ('B', "What were the results?", "결과가 어땠어?"),
      ('G', "Eighty percent of the students have pets. Only five out of twenty-five students don't have pets.", "학생들의 80%가 애완동물을 가지고 있어. 25명의 학생들 중 5명만이 애완동물이 없어."),
      ('B', "What kind of pets do they have?", "그들은 어떤 종류의 애완동물을 가지고 있니?"), ('G', "Well, ten students have dogs and three students have cats.", "음, 10명은 강아지, 3명은 고양이를 가지고 있어."),
      ('B', "What about the rest?", "나머지는?"), ('G', "Seven students have fish.", "7명의 학생들은 물고기를 가지고 있어.")]
W2 = [('M', "Mason, how was the election?", "Mason, 선거는 어땠니?"), ('B', "It was bad. I didn't win.", "안 좋았어요. 저는 이기지 못했어요."), ('M', "How come?", "어째서?"),
      ('B', "Yura won. Over sixty percent of the students voted for her.", "유라가 이겼어요. 학생들의 60% 이상이 그녀에게 투표했어요."),
      ('M', "Well, you tried your best and that's what matters.", "음, 너는 최선을 다했고 그것이 중요한 거란다."),
      ('B', "I guess so. I have learned many things while running for class president.", "저도 그렇게 생각해요. 반장 선거에 출마한 동안 많은 것을 배웠어요."),
      ('M', "I'm really proud of you.", "나는 네가 정말 자랑스럽구나."), ('B', "Thanks, Dad.", "고마워요, 아빠.")]
W3 = [('A', "What can you tell from the pie chart?", "원그래프에서 무엇을 알 수 있니?"),
      ('B', "Six out of twenty students like romance movies. That is thirty percent of the total.", "20명의 학생들 중 6명이 로맨스 영화를 좋아해. 그것은 전체의 30%야.")]
L8a = ['8과 Listen & Speak 1-A · 반려동물 설문 조사', '8과 Listen & Speak 1-B · 반장 선거', '8과 Listen & Speak 1-C · Talk Together']
P8a = dlg(L8a[0], W1) + dlg(L8a[1], W2) + dlg(L8a[2], W3)
j8a = build(
 vocab=[['graph', '그래프'], ['do a survey on', '~에 대해 설문 조사를 하다'], ['result', '결과'], ['percent', '퍼센트'], ['A out of B', 'B 중에 A (상술하기)'],
        ['What about ~?', '~은 어때?'], ['the rest', '나머지'], ['election', '선거'], ['How come?', '어째서? 왜?'], ['vote for', '~에게 투표하다'],
        ["try one's best", '최선을 다하다'], ["That's what matters.", '그게 중요한 거야.'], ['I guess so.', '그런 것 같아.'], ['run for', '~에 출마하다'],
        ['class president', '반장'], ['be proud of', '~을 자랑스러워하다'], ['pie chart', '원그래프'], ['total', '전체']],
 pickv=[
  (T(W2, 1).replace("didn't win", "didn't {win|lose}"), "정답 ▶ win (이기다)\n오답 ▶ lose: 선거 결과가 안 좋았다(It was bad) → 이기지 '못했다'"),
  (T(W2, 3).replace('voted for her', 'voted {for|against} her'), "정답 ▶ for (~에게 찬성하여)\n오답 ▶ against (~에 반대하여): 유라가 이겼으니 60% 이상이 유라'에게' 투표했어요."),
  (T(W2, 6).replace('really proud', 'really {proud|ashamed}'), "정답 ▶ proud (자랑스러운)\n오답 ▶ ashamed (부끄러운): 최선을 다하고 많은 것을 배운 아들이 '자랑스럽다'"),
 ],
 tf=[
  ("Minju did a survey on her classmates' pets.", True, "정답 ▶ T\n이유: I did a survey on the kinds of pets my classmates have.", None, "I did a survey on the kinds of pets my classmates have"),
  ("Twenty out of twenty-five students don't have pets.", False, "정답 ▶ F\n이유: 애완동물이 없는 학생은 25명 중 5명이에요. 20명(80%)은 애완동물이 있어요.", None, "Only five out of twenty-five students don't have pets"),
  ("Ten students have dogs.", True, "정답 ▶ T\n이유: ten students have dogs", None, "ten students have dogs"),
  ("Mason won the election.", False, "정답 ▶ F\n이유: I didn't win. 이긴 사람은 유라예요.", None, "I didn't win"),
  ("Less than half of the students voted for Yura.", False, "정답 ▶ F\n이유: 60% 이상(Over sixty percent)이 유라에게 투표했어요. 절반보다 많아요.", None, "Over sixty percent of the students voted for her"),
  ("Mason's dad is proud of him.", True, "정답 ▶ T\n이유: I'm really proud of you.", None, "I'm really proud of you"),
 ],
 resp=[
  ("A: What were the results?", ['Eighty percent of the students have pets.', 'I did a survey.', 'I guess so.', 'Thanks, Dad.'],
   "정답 ▶ Eighty percent of the students have pets.\n이유: 결과를 물었으니 → 숫자(퍼센트)로 자세히 말해요(상술하기)."),
  ("A: Mason, how was the election? B: It was bad. I didn't win. A: ______", ['How come?', 'Congratulations!', "That's what matters.", 'Seven students have fish.'],
   "정답 ▶ How come?\n이유: 선거에서 지지 못했다고 하니 '어째서?'라고 이유를 물어요. (How come? = Why?)"),
 ],
 ilchi=[
  {'box': [L8a[0]], 'q': "대화의 내용과 일치하지 <u>않는</u> 것은?",
   'opts': ["Three students have no pets.", "Twenty students have pets.", "Five students don't have pets.", "Ten students have dogs.", "Seven students have fish."],
   'ex': "정답 ▶ Three students have no pets.\n이유: 3명은 고양이를 기르는 학생이에요. 애완동물이 없는 학생은 5명이에요.\n계산 ▶ 25명 × 80% = 20명(애완동물 있음) = 개 10 + 고양이 3 + 물고기 7",
   'per': [["3명은 애완동물이 없다.", "three students have cats", "불일치 → 고양이 3명"], ["20명은 애완동물이 있다.", "Eighty percent of the students have pets", "일치 (25 × 80%)"],
           ["5명은 애완동물이 없다.", "Only five out of twenty-five students don't have pets", "일치"], ["10명은 개를 기른다.", "ten students have dogs", "일치"],
           ["7명은 물고기를 기른다.", "Seven students have fish", "일치"]]},
  {'box': [L8a[0]], 'q': "애완동물을 기르는 학생들 중에서 개를 기르는 학생의 비율은?",
   'opts': ['50%', '40%', '80%', '20%', '35%'],
   'ex': "정답 ▶ 50%\n이유: 애완동물을 기르는 학생은 20명(25명의 80%), 그중 개는 10명 → 10 ÷ 20 = 50%\n오답 ▶ 40%는 반 전체 25명을 기준으로 계산한 함정이에요. 질문의 기준(애완동물을 기르는 학생)을 꼭 확인!",
   'per': [["", ["Eighty percent of the students have pets", "ten students have dogs"], "정답"], ["", "", "✘ 10 ÷ 25 (전체 기준)"], ["", "", "✘ 애완동물 있는 비율"], ["", "", "✘ 애완동물 없는 비율"], ["", "", "✘"]]},
 ],
 pickg=[
  (T(W1, 1).replace('my classmates have', 'my classmates {have|has}'), "정답 ▶ have\n이유: pets 뒤에 목적격 관계대명사 that/which가 생략된 절. 그 절의 주어는 my classmates(복수) → have"),
  (T(W1, 3).replace("students don't have", "students {don't|doesn't} have"), "정답 ▶ don't\n이유: A out of B에서 동사는 A(five students, 복수)에 맞춰요 → don't"),
  (T(W2, 6).replace('proud of you', 'proud {of|for} you'), "정답 ▶ of\n이유: be proud of ~ = ~을 자랑스러워하다 (짝꿍 전치사 of)"),
 ],
 error=[
  ER("I guess so. I [[have learned]] many things [[while]] [[run]] for class president.", 2, 'running',
     "틀린 곳 ▶ ③ run → running\n이유: while 뒤에 주어 + be동사(I was)가 생략된 형태 → while + -ing (~하는 동안)\n나머지 ▶ ① have learned(현재완료: 출마한 때부터 지금까지 배워 옴) ✔ ② while ✔"),
  ER("Well, you [[tried]] your best and [[that's]] [[which]] matters.", 2, 'what',
     "틀린 곳 ▶ ③ which → what\n이유: 선행사가 없으니 관계대명사 what(~하는 것) = the thing which. that's what matters = 그게 중요한 것이다\n나머지 ▶ ① tried(try의 과거) ✔ ② that's ✔"),
 ],
 scr=[("Only five out of twenty-five students don't have pets.", "25명의 학생들 중 5명만이 애완동물이 없어."), (T(W2, 4), W2[4][2])],
 order=[([T(W1, i) for i in range(4, 8)], ["B: 어떤 애완동물을 기르니?", "G: 개 10명, 고양이 3명", "B: 나머지는?", "G: 물고기 7명"])],
 blank=[
  (T(W1, 6).replace('the rest', 'the ____'), ['rest', 'results', 'survey', 'graph'], "정답 ▶ rest (나머지)\n이유: 개와 고양이를 말한 뒤 '나머지는?'이라고 묻고, 물고기 7명이라고 답해요."),
  (T(W3, 1).replace('That is thirty percent', 'That is ____ percent'), ['thirty', 'twenty', 'sixty', 'six'], "정답 ▶ thirty\n이유: 20명 중 6명 → 6 ÷ 20 = 0.3 = 30%"),
 ],
 awk=[(["A: What can you tell from the pie chart? B: Yes, I can tell.", "A: What is this graph about? B: It's about the kinds of pets.", "A: I didn't win the election. B: How come?", "A: I'm really proud of you. B: Thanks, Dad."],
       "정답 ▶ A: What can you tell from the pie chart? B: Yes, I can tell.\n이유: What으로 시작하는 질문에는 Yes/No로 답할 수 없어요. → Six out of twenty students like ~.처럼 결과를 말해야 해요.")],
 func=[
  ("'20명 중 5명'을 바르게 나타낸 것은?", ['five out of twenty', 'twenty out of five', 'five percent of twenty', 'twenty of five percent'],
   "정답 ▶ five out of twenty\n이유: A out of B = B 중에 A (부분 out of 전체)"),
  ("원그래프 결과 '20명 중 6명이 로맨스 영화를 좋아함'을 바르게 말한 것은?", ['Thirty percent of the students like romance movies.', 'Six percent of the students like romance movies.', 'Twenty out of six students like romance movies.', 'Sixty percent of the students like romance movies.'],
   "정답 ▶ Thirty percent of the students like romance movies.\n이유: 6 ÷ 20 = 30% → Thirty percent of ~ (= Six out of twenty students ~)"),
 ],
 summ=[
  S([L8a[0]], "In Minju's survey, (A) ______ percent of her classmates have pets, and seven of the pet owners have (B) ______.",
    ['(A) eighty – (B) fish', '(A) twenty – (B) fish', '(A) eighty – (B) cats', '(A) five – (B) dogs', '(A) seventy – (B) birds'],
    "정답 ▶ (A) eighty – (B) fish\n(A) 학생들의 '80%'가 애완동물이 있음 → eighty\n(B) 나머지 7명은 '물고기' → fish\n오답 ▶ twenty: 애완동물이 '없는' 비율(5/25)이에요.",
    ["Eighty percent of the students have pets", "Seven students have fish"]),
  S([L8a[1]], "Mason lost the election because over sixty percent of the students voted for (A) ______, but his dad said trying his (B) ______ is what matters.",
    ['(A) Yura – (B) best', '(A) Mason – (B) best', '(A) Yura – (B) worst', '(A) Minju – (B) luck', '(A) Mason – (B) time'],
    "정답 ▶ (A) Yura – (B) best\n(A) 60% 이상이 '유라'에게 투표 → Yura\n(B) '최선'을 다한 게 중요 → try one's best",
    ["Over sixty percent of the students voted for her", "you tried your best and that's what matters"])],
)

# ═════════════ 8과 ② Listen & Speak 2 (이해 점검하기) ═════════════
X1 = [('B', "Emma, can you help me with this math problem?", "Emma, 이 수학 문제 좀 도와줄래?"), ('G', "Sure, what is it?", "물론이지, 뭔데?"),
      ('B', "You have to move one stick to make this sum right. How could four minus five equal six?", "너는 이 계산이 맞도록 한 개의 막대기만 옮겨야 해. 어떻게 4 빼기 5가 6이 될까?"),
      ('G', "Oh, it's simple. You need to move one of the sticks in number four to make it eleven. Do you see what I mean?", "아, 그것은 간단해. 너는 숫자 4를 11로 만들기 위해 막대기 하나를 옮기면 돼. 무슨 말인지 알겠니?"),
      ('B', "Yes, now I see what you mean. Eleven minus five equals six. How clever!", "응, 이제 네 말이 무슨 뜻인지 알겠어. 11 빼기 5는 6이지. 너 정말 똑똑하구나!"),
      ('G', "Thinking outside the box can be helpful sometimes.", "틀 밖에서 생각하는 것은 때때로 도움이 될 수 있지.")]
X2 = [('B', "Jian, what's the matter? You look very upset.", "지안아, 무슨 일 있니? 너 무척 속상해 보여."), ('G', "My brother broke my computer. I'm so angry.", "내 남동생이 내 컴퓨터를 고장 냈어. 난 정말 화나."),
      ('B', "I'm sorry to hear that, but your facial muscles must be tired.", "그렇다니 유감이지만, 너의 얼굴 근육은 피곤할 거야."), ('G', "What do you mean?", "무슨 뜻이니?"),
      ('B', "Well, it takes a lot of muscles to look angry, but only a few to smile. Do you see what I mean?", "음, 화난 표정을 지을 때는 많은 근육이 필요하지만, 미소 짓는 데는 몇 개의 근육만 필요하거든. 내 말이 무슨 뜻인지 알겠니?"),
      ('G', "Oh, I get it. I guess it's not good to stay angry for a long time.", "아, 알겠어. 오랫동안 화난 상태로 있으면 좋지 않겠구나."),
      ('B', "That's right. Remember, it's always better to smile.", "맞아. 기억해, 웃는 게 항상 더 낫다는 것을 말이야.")]
X3 = [('A', "How could five plus three equal six?", "어떻게 5 더하기 3이 6이 되지?"),
      ('B', "Why don't you move the stick in number five to make it three? Do you see what I mean?", "숫자 5를 3으로 만들기 위해 막대기를 옮기는 것은 어때? 내 말이 무슨 뜻인지 알겠니?"),
      ('A', "Do you mean the one on the top left?", "위쪽 왼쪽에 있는 것을 말하는 거니?"), ('B', "That's right.", "맞아.")]
L8b = ['8과 Listen & Speak 2-A · 성냥개비 수학 문제', '8과 Listen & Speak 2-B · 화난 표정과 미소', '8과 Listen & Speak 2-C · Talk Together']
P8b = dlg(L8b[0], X1) + dlg(L8b[1], X2) + dlg(L8b[2], X3)
j8b = build(
 vocab=[['help A with B', 'A가 B 하는 것을 돕다'], ['math problem', '수학 문제'], ['stick', '막대기'], ['sum', '계산(식), 합계'], ['minus', '빼기'],
        ['equal', '(수가) ~이 되다, 같다'], ['simple', '간단한'], ['Do you see what I mean?', '내 말이 무슨 뜻인지 알겠니? (이해 점검하기)'], ['clever', '영리한, 똑똑한'],
        ['think outside the box', '고정관념을 깨다, 틀 밖에서 생각하다'], ['helpful', '도움이 되는'], ['upset', '속상한'], ['facial muscle', '얼굴 근육'],
        ['must', '~임에 틀림없다'], ['What do you mean?', '무슨 뜻이니?'], ['I get it.', '알겠어, 이해했어.'], ['stay angry', '화난 채로 있다'], ['top left', '왼쪽 위']],
 pickv=[
  (T(X1, 3).replace("it's simple", "it's {simple|difficult}"), "정답 ▶ simple (간단한)\n오답 ▶ difficult: 막대 하나만 옮기면 되니 '간단하다'고 하고 바로 방법을 알려 줘요."),
  (T(X2, 1).replace("I'm so angry", "I'm so {angry|happy}"), "정답 ▶ angry (화난)\n오답 ▶ happy: 남동생이 컴퓨터를 고장 냈고 속상해 보인다(upset)고 했어요."),
  (T(X2, 4).replace('only a few to smile', 'only a {few|lot} to smile'), "정답 ▶ few (몇 개)\n오답 ▶ lot: but 앞뒤가 대조 → 화난 표정엔 근육이 '많이', 미소엔 '몇 개만'"),
 ],
 tf=[
  ("Emma helps the boy with a math problem.", True, "정답 ▶ T\n이유: can you help me with this math problem? → Sure", None, "can you help me with this math problem"),
  ("The boy has to move two sticks.", False, "정답 ▶ F\n이유: 막대기를 하나만(one stick) 옮겨야 해요.", None, "You have to move one stick to make this sum right"),
  ("Emma changes four into eleven.", True, "정답 ▶ T\n이유: move one of the sticks in number four to make it eleven", None, "to make it eleven"),
  ("Jian's brother broke her computer.", True, "정답 ▶ T\n이유: My brother broke my computer.", None, "My brother broke my computer"),
  ("It takes more muscles to smile than to look angry.", False, "정답 ▶ F\n이유: 화난 표정에 근육이 더 많이 필요해요. 미소에는 몇 개만 필요해요.", None, "it takes a lot of muscles to look angry, but only a few to smile"),
  ("In the Talk Together, A should move the stick on the bottom right.", False, "정답 ▶ F\n이유: 옮길 막대는 왼쪽 위(the one on the top left)에 있는 거예요.", None, "Do you mean the one on the top left"),
 ],
 resp=[
  ("A: Do you see what I mean?", ['Yes, now I see what you mean.', 'Sure, what is it?', "I'm sorry to hear that.", 'How come?'],
   "정답 ▶ Yes, now I see what you mean.\n이유: 이해했는지 묻는 말(Do you see what I mean?) → 이해했으면 I see what you mean. / I get it."),
  ("A: Your facial muscles must be tired.", ['What do you mean?', 'Yes, I did.', 'Sure, what is it?', 'Thinking outside the box.'],
   "정답 ▶ What do you mean?\n이유: 갑자기 얼굴 근육이 피곤하겠다는 말을 들으면 '무슨 뜻이니?'라고 되물어요."),
 ],
 ilchi=[
  {'box': [L8b[0]], 'q': "Emma가 알려 준 해결 방법으로 알맞은 것은?",
   'opts': ['숫자 4의 막대 하나를 옮겨 11로 만든다', '숫자 5의 막대 하나를 옮겨 6으로 만든다', '숫자 6의 막대 하나를 옮겨 0으로 만든다', '막대 두 개를 옮겨 4를 9로 만든다', '빼기 기호를 더하기 기호로 바꾼다'],
   'ex': "정답 ▶ 숫자 4의 막대 하나를 옮겨 11로 만든다\n이유: move one of the sticks in number four to make it eleven → 11 - 5 = 6",
   'per': [["", "to make it eleven", "정답"], ["", "", "✘"], ["", "", "✘"], ["", "You have to move one stick", "✘ 막대는 하나만"], ["", "Eleven minus five equals six", "✘ 빼기 그대로"]]},
  {'box': [L8b[1]], 'q': "대화의 내용과 일치하지 <u>않는</u> 것은?",
   'opts': ["The boy thinks staying angry is good for Jian.", "Jian looks very upset.", "Jian's brother broke her computer.", "It takes only a few muscles to smile.", "Jian understands what the boy means."],
   'ex': "정답 ▶ The boy thinks staying angry is good for Jian.\n이유: 소년은 웃는 게 항상 더 낫다(it's always better to smile)고 했어요.",
   'per': [["소년은 화난 채로 있는 것이 지안이에게 좋다고 생각한다.", "it's always better to smile", "불일치"], ["지안이는 무척 속상해 보인다.", "You look very upset", "일치"],
           ["지안이의 남동생이 컴퓨터를 고장 냈다.", "My brother broke my computer", "일치"], ["미소에는 몇 개의 근육만 필요하다.", "only a few to smile", "일치"],
           ["지안이는 소년의 말을 이해한다.", "Oh, I get it", "일치"]]},
 ],
 pickg=[
  (T(X1, 0).replace('help me with', 'help me {with|for}'), "정답 ▶ with\n이유: help + 사람 + with + 명사 = (사람)이 ~하는 것을 돕다"),
  (T(X1, 2).replace('one stick to make', 'one stick {to make|making}'), "정답 ▶ to make\n이유: '~하기 위해서'(목적) → to부정사의 부사적 용법"),
  (T(X1, 2).replace('could four minus five equal', 'could four minus five {equal|equals}'), "정답 ▶ equal\n이유: 조동사 could 뒤에는 동사원형 → equal"),
  (T(X1, 5).replace('Thinking outside', '{Thinking|Think} outside'), "정답 ▶ Thinking\n이유: 주어 자리 → 동명사(Thinking outside the box = 틀 밖에서 생각하는 것)"),
  (T(X1, 4).replace('I see what you mean', 'I see {what|that} you mean'), "정답 ▶ what\n이유: 관계대명사 what(~하는 것) = the thing which. mean의 목적어가 빠져 있으니 that은 쓸 수 없어요."),
  (T(X2, 6).replace('better to smile', 'better {to smile|smile}'), "정답 ▶ to smile\n이유: 가주어 it ~ 진주어 to부정사: it's always better to smile (웃는 것이 항상 더 낫다)"),
 ],
 error=[
  ER("Oh, I [[get]] it. I guess it's not good [[stay]] angry for a [[long]] time.", 1, 'to stay',
     "틀린 곳 ▶ ② stay → to stay\n이유: 가주어 it ~ 진주어 to부정사 (it's not good to stay angry = 화난 채로 있는 것은 좋지 않다)\n나머지 ▶ ① get(I get it. 알겠어) ✔ ③ for a long time ✔"),
  ER("You need to move [[one of the stick]] in number four [[to make]] it eleven. Do you see [[what]] I mean?", 0, 'one of the sticks',
     "틀린 곳 ▶ ① one of the stick → one of the sticks\n이유: one of + the + 복수 명사 (~ 중 하나)\n나머지 ▶ ② to make(목적) ✔ ③ what(관계대명사) ✔"),
 ],
 scr=[("Do you see what I mean?", "내 말이 무슨 뜻인지 알겠니?"), (T(X1, 5), X1[5][2])],
 order=[([T(X2, i) for i in range(4)], ["B: 무슨 일이야? 속상해 보여", "G: 남동생이 컴퓨터를 고장 냈어", "B: 안됐다, 그런데 얼굴 근육이 피곤하겠다", "G: 무슨 뜻이야?"])],
 blank=[
  (T(X1, 4).replace('Eleven minus five', '____ minus five'), ['Eleven', 'Four', 'Ten', 'Twelve'], "정답 ▶ Eleven\n이유: 4를 11로 바꿨으니 11 - 5 = 6 → 식이 맞아져요."),
  (T(X3, 0).replace('equal six', 'equal ____'), ['six', 'eight', 'five', 'nine'], "정답 ▶ six\n이유: 5를 3으로 바꾸면 3 + 3 = 6. 막대 하나로 식이 맞아지려면 답이 6이어야 해요.\n오답 ▶ eight(5+3)은 이미 맞는 식이라 고칠 필요가 없어요."),
 ],
 awk=[(["A: Do you mean the one on the top left? B: I'm sorry to hear that.", "A: Can you help me with this problem? B: Sure, what is it?", "A: Do you see what I mean? B: Oh, I get it.", "A: My brother broke my computer. B: I'm sorry to hear that."],
       "정답 ▶ A: Do you mean the one on the top left? B: I'm sorry to hear that.\n이유: 어느 막대를 말하는지 확인하는 질문에 '안됐다'는 어색해요. → That's right.처럼 답해요.")],
 func=[("이해했는지 확인하는 표현이 <b>아닌</b> 것은?", ["What's the matter?", 'Do you see what I mean?', 'Do you know what I mean?', 'Are you following me?'],
        "정답 ▶ What's the matter?\n이유: '무슨 일 있니?'는 상태를 묻는 말이에요. 나머지는 모두 '내 말 이해했니?'라는 이해 점검 표현이에요.")],
 summ=[
  S([L8b[0]], "By moving one stick in number four to make it (A) ______, Emma solved the problem, showing that thinking outside the box can be (B) ______.",
    ['(A) eleven – (B) helpful', '(A) seven – (B) helpful', '(A) eleven – (B) useless', '(A) nine – (B) boring', '(A) one – (B) dangerous'],
    "정답 ▶ (A) eleven – (B) helpful\n(A) 4를 '11'로 바꿈 → eleven\n(B) 틀 밖에서 생각하기는 '도움이 될' 수 있다 → helpful",
    ["to make it eleven", "Thinking outside the box can be helpful sometimes"]),
  S([L8b[1]], "The boy told Jian that it takes (A) ______ muscles to look angry than to smile, so it's not good to stay (B) ______ for a long time.",
    ['(A) more – (B) angry', '(A) fewer – (B) angry', '(A) more – (B) happy', '(A) fewer – (B) calm', '(A) less – (B) quiet'],
    "정답 ▶ (A) more – (B) angry\n(A) 화난 표정에 근육이 '더 많이' → more\n(B) 오랫동안 '화난' 채로 있는 건 좋지 않다 → angry",
    ["it takes a lot of muscles to look angry, but only a few to smile", "it's not good to stay angry for a long time"])],
)

# ═════════════ 8과 ③ Real Life Communication · Think and Talk · Communication Task ═════════════
Y1 = [('Mina', "Henry, what are you doing?", "Henry, 너 뭐하고 있니?"),
      ('Henry', "I'm writing an article about students' favorite snacks. I'm worried about their health.", "나는 학생들이 가장 좋아하는 간식에 관한 기사를 쓰고 있어. 난 그들의 건강이 걱정 돼."),
      ('Mina', "Why?", "왜?"),
      ('Henry', "Well, I surveyed 100 students and the results show that eighty percent of the students liked pizza and fried chicken for snacks. Do you see what I mean?", "음, 난 100명의 학생들에게 설문 조사를 했는데 80%의 학생들이 간식으로 피자와 프라이드치킨을 좋아한다는 결과가 나왔어. 내 말이 무슨 뜻인지 알겠니?"),
      ('Mina', "Oh, I get it. Students really like fast food. What else did they like?", "아, 알겠어. 학생들이 정말 패스트푸드를 좋아하는구나. 그 이외에 그들은 어떤 것을 좋아했니?"),
      ('Henry', "Twelve percent of the students chose chocolate cake as their favorite.", "학생들의 12%가 가장 좋아하는 것으로 초콜릿 케이크를 선택했어."),
      ('Mina', "Wow, students should really try to eat healthier snacks!", "와, 학생들은 더 건강한 간식을 먹으려고 정말로 노력해야겠다!")]
Y2 = [('A', "We should have more tennis classes for after-school classes.", "우리는 방과 후 수업으로 더 많은 테니스 수업이 필요해."), ('B', "What makes you say that?", "왜 그런 말을 하는 거니?"),
      ('A', "Look at the pie chart. Seventy percent of the students said that they wanted to learn tennis. Do you see what I mean?", "원그래프를 봐. 학생들의 70%가 테니스를 배우고 싶다고 했어. 내 말이 무슨 뜻인지 알겠니?"),
      ('B', "Oh, I see.", "아, 알겠어.")]
Y3 = [('Student', "I did a survey on the books we want for our school library.", "저는 우리가 학교 도서관에 원하는 책들에 대한 설문 조사를 했습니다."),
      ('Student', "The result says that thirteen out of twenty students chose novels. That is sixty-five percent of the total.", "그 결과 20명의 학생들 중 13명은 소설책을 원했습니다. 그것은 전체의 65%입니다."),
      ('Student', "Five out of twenty students chose science-fiction books.", "20명의 학생들 중 5명은 공상 과학 소설을 원했습니다."),
      ('Student', "However, only two out of twenty students chose history books.", "그러나 20명의 학생들 중 2명만 역사책을 원했습니다."),
      ('Student', "From this survey result, I think the school library should get more novels.", "이 설문 결과에서 저는 학교 도서관이 더 많은 소설책을 마련해야 한다고 생각합니다."),
      ('Student', "Do you see what I mean?", "제 말이 무슨 뜻인지 아시겠어요?")]
L8c = ['8과 Real Life Communication · 좋아하는 간식 기사', '8과 Think and Talk · 방과 후 수업', '8과 Communication Task · 도서관 책 설문 발표']
P8c = dlg(L8c[0], Y1) + dlg(L8c[1], Y2) + dlg(L8c[2], Y3)
j8c = build(
 vocab=[['article', '기사'], ['snack', '간식'], ['be worried about', '~을 걱정하다'], ['health', '건강'], ['survey', '설문 조사하다; 설문 조사'],
        ['result', '결과'], ['show', '보여 주다'], ['fast food', '패스트푸드'], ['What else ~?', '그 밖에 무엇을 ~?'], ['choose A as B', 'A를 B로 고르다 (choose - chose - chosen)'],
        ['healthier', '더 건강한 (healthy의 비교급)'], ['after-school class', '방과 후 수업'], ['What makes you say that?', '왜 그렇게 말하니? (이유 묻기)'],
        ['novel', '소설'], ['science-fiction', '공상 과학의'], ['however', '그러나'], ['library', '도서관']],
 pickv=[
  (T(Y1, 1).replace("I'm worried about", "I'm {worried|happy} about"), "정답 ▶ worried (걱정하는)\n오답 ▶ happy: 학생들이 패스트푸드를 너무 좋아해서 건강이 '걱정'된다고 해요."),
  (T(Y1, 6).replace('eat healthier snacks', 'eat {healthier|cheaper} snacks'), "정답 ▶ healthier (더 건강한)\n오답 ▶ cheaper (더 싼): 패스트푸드만 좋아하니 '더 건강한' 간식을 먹어야 한다는 결론이에요."),
  (T(Y3, 4).replace('get more novels', 'get more {novels|history books}'), "정답 ▶ novels (소설)\n오답 ▶ history books: 소설이 65%로 가장 많이 선택됐고, 역사책은 2명(10%)뿐이에요."),
 ],
 tf=[
  ("Henry is writing an article about students' favorite snacks.", True, "정답 ▶ T\n이유: I'm writing an article about students' favorite snacks.", None, "I'm writing an article about students' favorite snacks"),
  ("Henry surveyed 80 students.", False, "정답 ▶ F\n이유: 100명을 조사했어요. 80은 피자와 치킨을 좋아한 비율(80%)이에요.", None, "I surveyed 100 students"),
  ("Twelve percent of the students chose chocolate cake.", True, "정답 ▶ T\n이유: Twelve percent of the students chose chocolate cake as their favorite.", None, "Twelve percent of the students chose chocolate cake"),
  ("Mina thinks the students eat healthy snacks.", False, "정답 ▶ F\n이유: 학생들이 더 건강한 간식을 먹으려고 노력해야 한다(should really try to eat healthier snacks)고 했어요.", None, "students should really try to eat healthier snacks"),
  ("Seventy percent of the students wanted to learn tennis.", True, "정답 ▶ T\n이유: Seventy percent of the students said that they wanted to learn tennis.", None, "Seventy percent of the students said that they wanted to learn tennis"),
  ("Most students chose history books.", False, "정답 ▶ F\n이유: 역사책은 20명 중 2명뿐이에요. 가장 많이 고른 것은 소설(13명)이에요.", None, "only two out of twenty students chose history books"),
 ],
 resp=[
  ("A: We should have more tennis classes for after-school classes.", ['What makes you say that?', "I'm writing an article.", 'Twelve percent.', 'I did a survey on books.'],
   "정답 ▶ What makes you say that?\n이유: 주장을 듣고 '왜 그렇게 말하니?'라고 이유를 물어요. 그러면 상대가 그래프를 근거로 설명해요."),
  ("A: What else did they like?", ['Twelve percent of the students chose chocolate cake.', "I'm worried about their health.", 'Oh, I see.', 'What makes you say that?'],
   "정답 ▶ Twelve percent of the students chose chocolate cake.\n이유: '그 밖에 무엇을 좋아했니?' → 다른 결과를 숫자로 말해요."),
 ],
 ilchi=[
  {'box': [L8c[0]], 'q': "대화의 내용과 일치하지 <u>않는</u> 것은?",
   'opts': ["Mina thinks students eat enough healthy snacks.", "Henry is worried about students' health.", "Henry surveyed 100 students.", "Eighty students liked pizza and fried chicken.", "Twelve students chose chocolate cake."],
   'ex': "정답 ▶ Mina thinks students eat enough healthy snacks.\n이유: 미나는 학생들이 더 건강한 간식을 먹으려고 노력해야 한다고 했어요.\n계산 ▶ 100명 × 80% = 80명, 100명 × 12% = 12명",
   'per': [["미나는 학생들이 건강한 간식을 충분히 먹는다고 생각한다.", "students should really try to eat healthier snacks", "불일치"], ["Henry는 학생들의 건강을 걱정한다.", "I'm worried about their health", "일치"],
           ["Henry는 100명을 조사했다.", "I surveyed 100 students", "일치"], ["80명이 피자와 치킨을 좋아했다.", "eighty percent of the students liked pizza and fried chicken", "일치 (100 × 80%)"],
           ["12명이 초콜릿 케이크를 골랐다.", "Twelve percent of the students chose chocolate cake", "일치 (100 × 12%)"]]},
  {'box': [L8c[2]], 'q': "설문 결과에 대한 설명으로 알맞은 것은?",
   'opts': ["Novels were chosen by sixty-five percent of the students.", "Science-fiction books were chosen by thirty percent of the students.", "History books were chosen by twenty percent of the students.", "Most students chose science-fiction books.", "The speaker thinks the library should get more history books."],
   'ex': "정답 ▶ Novels were chosen by sixty-five percent of the students.\n이유: 20명 중 13명 = 65%\n오답 ▶ 공상 과학 5명 = 25% / 역사 2명 = 10% / 가장 많은 건 소설 / 소설을 더 들여야 한다고 함",
   'per': [["", ["thirteen out of twenty students chose novels", "That is sixty-five percent of the total"], "정답"], ["", "Five out of twenty students chose science-fiction books", "✘ 5/20 = 25%"],
           ["", "only two out of twenty students chose history books", "✘ 2/20 = 10%"], ["", "thirteen out of twenty students chose novels", "✘ 소설이 가장 많음"],
           ["", "the school library should get more novels", "✘ 소설"]]},
 ],
 pickg=[
  (T(Y1, 3).replace('results show that eighty', 'results show {that|what} eighty'), "정답 ▶ that\n이유: 뒤에 완전한 문장이 오는 목적어절 → 접속사 that (생략 가능). what 뒤에는 불완전한 문장이 와요."),
  (T(Y1, 6).replace('try to eat', 'try {to eat|eating}'), "정답 ▶ to eat\n이유: try to + 동사원형 = ~하려고 노력하다. try -ing는 '시험 삼아 ~해 보다'라서 여기 뜻(노력해야 한다)과 맞지 않아요."),
  (T(Y2, 1).replace('makes you say', 'makes you {say|to say}'), "정답 ▶ say\n이유: 사역동사 make + 목적어 + 동사원형 (무엇이 너를 그렇게 말하게 하니? = 왜 그렇게 말하니?)"),
  (T(Y2, 2).replace('they wanted to learn', 'they {wanted|want} to learn'), "정답 ▶ wanted\n이유: 주절이 과거(said) → that절도 과거(wanted)로 시제를 맞춰요."),
 ],
 error=[
  ER("Well, I [[surveyed]] 100 students and the results [[shows]] that eighty percent of the students [[liked]] pizza and fried chicken for snacks.", 1, 'show',
     "틀린 곳 ▶ ② shows → show\n이유: 주어 the results(복수) → show\n나머지 ▶ ① surveyed ✔ ③ liked(조사 당시 과거) ✔"),
  ER("[[However]], only two out of twenty students [[chose]] history [[book]].", 2, 'books',
     "틀린 곳 ▶ ③ book → books\n이유: 셀 수 있는 명사가 '종류 전체(역사책들)'를 나타내니 복수형 books. 앞 문장의 novels, science-fiction books와도 같아요.\n나머지 ▶ ① However ✔ ② chose(choose의 과거) ✔"),
 ],
 scr=[("Students really like fast food.", "학생들이 정말 패스트푸드를 좋아하는구나."), (T(Y3, 4), Y3[4][2])],
 order=[([T(Y2, i) for i in range(4)], ["A: 테니스 수업을 늘려야 해", "B: 왜 그렇게 말해?", "A: 그래프 봐, 70%가 테니스를 원해", "B: 아, 알겠어"])],
 blank=[
  (T(Y3, 1).replace('sixty-five', '____'), ['sixty-five', 'thirteen', 'twenty', 'thirty'], "정답 ▶ sixty-five\n이유: 20명 중 13명 → 13 ÷ 20 = 0.65 = 65%"),
  (T(Y1, 4).replace('like fast food', 'like ____ food'), ['fast', 'healthy', 'Korean', 'home-made'], "정답 ▶ fast\n이유: 80%가 피자와 프라이드치킨을 좋아한다 → '패스트'푸드를 좋아한다\n오답 ▶ healthy: 그래서 건강이 걱정된다고 했어요."),
 ],
 awk=[(["A: What else did they like? B: Yes, they did.", "A: What makes you say that? B: Look at the pie chart.", "A: Do you see what I mean? B: Oh, I see.", "A: What are you doing? B: I'm writing an article."],
       "정답 ▶ A: What else did they like? B: Yes, they did.\n이유: What으로 시작하는 질문에 Yes/No로 답할 수 없어요. → They liked chocolate cake.처럼 답해요.")],
 func=[("밑줄 친 말의 의도로 알맞은 것은?<br><b>B: <u>What makes you say that?</u></b>", ['그렇게 말하는 이유 묻기', '허락 구하기', '충고하기', '감사하기'],
        "정답 ▶ 그렇게 말하는 이유 묻기\n이유: What makes you say that? = Why do you say that? (왜 그렇게 말하니?)")],
 summ=[
  S([L8c[0]], "Henry is worried because (A) ______ percent of the students he surveyed liked fast food for snacks, so Mina thinks students should eat (B) ______ snacks.",
    ['(A) eighty – (B) healthier', '(A) twelve – (B) healthier', '(A) eighty – (B) sweeter', '(A) twenty – (B) more', '(A) hundred – (B) cheaper'],
    "정답 ▶ (A) eighty – (B) healthier\n(A) '80%'가 피자와 치킨(패스트푸드)을 좋아함 → eighty\n(B) '더 건강한' 간식 → healthier\n오답 ▶ twelve는 초콜릿 케이크를 고른 비율이에요.",
    ["eighty percent of the students liked pizza and fried chicken for snacks", "students should really try to eat healthier snacks"]),
  S([L8c[2]], "Since (A) ______ out of twenty students chose novels, the speaker thinks the school library should get more (B) ______.",
    ['(A) thirteen – (B) novels', '(A) five – (B) novels', '(A) thirteen – (B) history books', '(A) two – (B) science-fiction books', '(A) twenty – (B) magazines'],
    "정답 ▶ (A) thirteen – (B) novels\n(A) 20명 중 '13명'이 소설 → thirteen\n(B) 그래서 '소설'을 더 마련해야 한다 → novels",
    ["thirteen out of twenty students chose novels", "the school library should get more novels"])],
)

D = lambda i, r, st, p, s: {'id': i, 'name': 'DAY', 'range': r, 'story': st, 'passage': p, 'steps': s}
J7A = D('j7a', '7과 대화문 ① L&S 1', 'Lesson 7 · 바람·소원 표현하기 (I wish I could ~)', P7a, j7a)
J7B = D('j7b', '7과 대화문 ② L&S 2-A', 'Lesson 7 · 상상하여 말하기 (What would you do if ~?)', P7b, j7b)
J7C = D('j7c', '7과 대화문 ③ L&S 2-B·Real Life', 'Lesson 7 · 스페인과 가우디 · 정글에서 산다면', P7c, j7c)
J8A = D('j8a', '8과 대화문 ① L&S 1', 'Lesson 8 · 상술하기 (A out of B, ~ percent of)', P8a, j8a)
J8B = D('j8b', '8과 대화문 ② L&S 2', 'Lesson 8 · 이해 점검하기 (Do you see what I mean?)', P8b, j8b)
J8C = D('j8c', '8과 대화문 ③ Real Life·Task', 'Lesson 8 · 간식 기사 · 방과 후 수업 · 도서관 설문', P8c, j8c)

path = '/home/claude/proj/data/m3-jihak-min-L7.js'
PK = json.loads(subprocess.check_output(['node', '-e', "global.window={};require('%s');process.stdout.write(JSON.stringify(window.PKG))" % path]))
by = {d['id']: d for d in PK['days']}
assert all(k in by for k in ['d1', 'd2', 'd3', 'd4']), list(by)
order = [J7A, J7B, J7C, by['d1'], by['d2'], J8A, J8B, J8C, by['d3'], by['d4']]
for i, d in enumerate(order): d['name'] = 'DAY %d' % (i + 1)
for d in order: ansfirst(d['steps'])
for d in (J7A, J7B, J7C, J8A, J8B, J8C): d['steps'][0]['quizN'] = 12  # 10분 안쪽
PK['days'] = order
PK['pick'] = True
src = open(path).read(); head = src[:src.index('window.PKG')]
if '대화문' not in head: head = head.rstrip('\n') + '\n/* 10/28: 7·8과 대화문(scratchpad/gen_m3dlg.py) 각 과 본문 앞에 3 DAY씩, 10분 분량 · pick */\n'
write(PK, path, head)
print('ok', [(d['id'], d['name'], d['range']) for d in order])
