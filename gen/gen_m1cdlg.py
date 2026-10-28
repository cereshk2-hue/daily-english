import sys, json, subprocess
sys.path.insert(0, '/tmp/claude-0/-home-claude/a9e3e882-1f02-5d62-8f70-aced81bc59d2/scratchpad')
from gencommon import *
from dlgcommon import *
# 중1 천재(소영순) 4·5과 대화문 (10/28). 대화문은 10분 분량으로 쪼개서 고르기(pick) 버튼으로

T = lambda R, i: R[i][1]
def S(box, s, o, x, ev): return (None, box, s, o, x, ev)

# ═════════════ 4과 대화문 ① Listen and Check 1~3 ═════════════
Q1 = [('M', "Would you like some ice cream?", "아이스크림 드시겠어요?"), ('G', "Yes, please.", "네, 좋아요."),
      ('M', "We have strawberry and chocolate.", "딸기와 초콜릿이 있어요."), ('G', "Strawberry ice cream, please.", "딸기 아이스크림 주세요.")]
Q2 = [('M', "Hello. Are you ready to order?", "안녕하세요. 주문하시겠어요?"), ('G', "Yes, I'll have a kebab.", "네, 저는 케밥을 먹을래요."),
      ('M', "Would you like a drink?", "마실 것 드실래요?"), ('G', "Sure. Orange juice, please.", "물론이죠. 오렌지 주스 주세요.")]
Q3 = [('B', "Jane, how was your trip to Vietnam?", "Jane, 베트남 여행은 어땠어?"),
      ('G', "It was great. I enjoyed the beautiful nature and ate famous local foods.", "아주 좋았어. 나는 아름다운 자연을 즐겼고 유명한 현지 음식을 먹었어."),
      ('B', "What did you eat?", "무엇을 먹었니?"),
      ('G', "I ate rice noodle soup. It had a lot of vegetables and meat. It was tasty.", "쌀국수를 먹었어. 채소와 고기가 많았어. 정말 맛있었어.")]
K4 = ['4과 대화 1 · 아이스크림 (Listen and Check)', '4과 대화 2 · 주문하기 (Listen and Check)', '4과 대화 3 · 베트남 여행 (Listen and Check)']
P4a = dlg(K4[0], Q1) + dlg(K4[1], Q2) + dlg(K4[2], Q3)
k4a = build(
 vocab=[["Would you like ~?", '~ 드시겠어요? (음식 권하기)'], ['strawberry', '딸기'], ['be ready to', '~할 준비가 되다'], ['order', '주문하다'],
        ["I'll have ~", '~을 먹을게요 (주문하기)'], ['drink', '음료, 마실 것'], ['trip', '여행'], ['enjoy', '즐기다'], ['nature', '자연'],
        ['famous', '유명한'], ['local', '현지의, 지역의'], ['rice noodle soup', '쌀국수'], ['vegetable', '채소'], ['meat', '고기'], ['tasty', '맛있는']],
 pickv=[
  (T(Q1, 3).replace('Strawberry', '{Strawberry|Vanilla}'), "정답 ▶ Strawberry (딸기)\n오답 ▶ Vanilla (바닐라): 가게에 있는 맛은 딸기와 초콜릿(strawberry and chocolate)뿐이에요."),
  (T(Q2, 0).replace('ready to order', 'ready to {order|sleep}'), "정답 ▶ order (주문하다)\n오답 ▶ sleep: 식당에서 점원이 손님에게 → '주문하시겠어요?'"),
  (T(Q3, 1).replace('beautiful nature', 'beautiful {nature|noise}'), "정답 ▶ nature (자연)\n오답 ▶ noise (소음): '아름다운 ~을 즐겼다' → 자연"),
 ],
 tf=[
  ("The girl wants chocolate ice cream.", False, "정답 ▶ F\n이유: 소녀는 딸기 아이스크림(Strawberry ice cream)을 주문했어요.", None, "Strawberry ice cream, please"),
  ("The girl ordered a kebab.", True, "정답 ▶ T\n이유: Yes, I'll have a kebab. → I'll have ~ = ~을 먹을게요(주문)", None, "I'll have a kebab"),
  ("The girl doesn't want a drink.", False, "정답 ▶ F\n이유: 음료를 권하자 Sure.라고 하고 오렌지 주스를 주문했어요.", None, "Sure. Orange juice, please"),
  ("Jane didn't enjoy her trip to Vietnam.", False, "정답 ▶ F\n이유: It was great. 아름다운 자연을 즐겼다(enjoyed)고 했어요.", None, "It was great"),
  ("Jane ate rice noodle soup in Vietnam.", True, "정답 ▶ T\n이유: I ate rice noodle soup.", None, "I ate rice noodle soup"),
 ],
 resp=[
  ("A: Would you like some ice cream?", ['Yes, please.', 'Yes, I did.', 'I ate pizza.', 'It was great.'],
   "정답 ▶ Yes, please.\n이유: Would you like ~?(음식 권하기)에 승낙할 때 → Yes, please. / 거절할 때 → No, thanks.\n오답 ▶ Yes, I did.는 Did you ~? 질문의 대답"),
  ("A: How was your trip to Vietnam?", ['It was great.', 'Yes, please.', "I'll have a kebab.", 'No, thanks.'],
   "정답 ▶ It was great.\n이유: How was ~?(~은 어땠니?)는 소감을 묻는 말 → 과거형으로 느낌을 말해요."),
 ],
 ilchi=[{'box': K4, 'q': "대화의 내용과 일치하지 <u>않는</u> 것은?",
   'opts': ["The man has strawberry and chocolate ice cream.", "The girl is ready to order.", "The girl will have a kebab and orange juice.", "Jane enjoyed the nature in Vietnam.", "The rice noodle soup had no meat."],
   'ex': "정답 ▶ The rice noodle soup had no meat.\n이유: 쌀국수에는 채소와 고기가 많았어요(a lot of vegetables and meat).",
   'per': [["남자에게는 딸기와 초콜릿 아이스크림이 있다.", "We have strawberry and chocolate", "일치"],
           ["소녀는 주문할 준비가 되었다.", "Yes, I'll have a kebab", "일치"],
           ["소녀는 케밥과 오렌지 주스를 먹을 것이다.", ["I'll have a kebab", "Orange juice, please"], "일치"],
           ["Jane은 베트남의 자연을 즐겼다.", "I enjoyed the beautiful nature", "일치"],
           ["쌀국수에는 고기가 없었다.", "It had a lot of vegetables and meat", "불일치 → 고기가 많았음"]]}],
 pickg=[
  (T(Q2, 0).replace('ready to order', 'ready {to order|ordering}'), "정답 ▶ to order\n이유: be ready to + 동사원형 = ~할 준비가 되다"),
  (T(Q3, 2).replace('did you eat', 'did you {eat|ate}'), "정답 ▶ eat\n이유: 의문사 + did + 주어 + 동사원형 ~? (did가 과거를 나타내니 동사는 원형)"),
  (T(Q3, 1).replace('and ate famous', 'and {ate|eat} famous'), "정답 ▶ ate\n이유: 지난 여행 이야기 → 과거형. 앞의 enjoyed와 and로 나란히 연결돼요. (eat - ate - eaten)"),
 ],
 scr=[(T(Q1, 0), Q1[0][2]), (T(Q3, 1).split('. ')[1], "나는 아름다운 자연을 즐겼고 유명한 현지 음식을 먹었어.")],
 order=[([T(Q3, i) for i in range(4)], ["B: 베트남 여행은 어땠어?", "G: 좋았어, 자연을 즐기고 현지 음식을 먹었어", "B: 무엇을 먹었니?", "G: 쌀국수, 맛있었어"])],
 blank=[
  (T(Q2, 2).replace('a drink', 'a ____'), ['drink', 'kebab', 'pizza', 'table'], "정답 ▶ drink\n이유: 대답이 Orange juice, please.이니 '마실 것'을 권한 거예요."),
  (T(Q3, 3).replace('It was tasty', 'It was ____'), ['tasty', 'terrible', 'boring', 'expensive'], "정답 ▶ tasty (맛있는)\n이유: 여행이 좋았다고(It was great) 했으니 먹은 음식도 '맛있었다'가 자연스러워요."),
 ],
 awk=[(["A: Would you like some cake? B: No, thanks. I'm full.", "A: Are you ready to order? B: Yes, I'll have a sandwich.", 'A: What did you eat? B: I ate bibimbap.', 'A: How was your trip? B: Yes, please.'],
       "정답 ▶ A: How was your trip? B: Yes, please.\n이유: 여행 소감을 물었으니 It was great. 처럼 답해야 해요. Yes, please.는 음식을 권할 때의 대답이에요.")],
 func=[("음식을 권하는 표현이 <b>아닌</b> 것은?", ['What did you eat?', 'Would you like some juice?', 'Would you like to try some?', 'Do you want some cookies?'],
        "정답 ▶ What did you eat?\n이유: '무엇을 먹었니?'는 경험을 묻는 말이에요. 나머지는 모두 음식을 권하는 표현이에요.\n참고 ▶ Would you like + 명사 / Would you like to + 동사원형")],
 summ=[
  S([K4[0], K4[1]], "The girl chose (A) ______ ice cream, and at the restaurant she ordered a kebab and orange (B) ______.",
    ['(A) strawberry – (B) juice', '(A) chocolate – (B) juice', '(A) strawberry – (B) soup', '(A) chocolate – (B) cake', '(A) vanilla – (B) juice'],
    "정답 ▶ (A) strawberry – (B) juice\n(A) 딸기 아이스크림을 골랐다 → strawberry\n(B) 케밥과 오렌지 '주스' → juice",
    ["Strawberry ice cream, please", "Orange juice, please"]),
  S([K4[2]], "Jane (A) ______ the nature in Vietnam and ate rice noodle soup with a lot of vegetables and (B) ______.",
    ['(A) enjoyed – (B) meat', '(A) hated – (B) meat', '(A) enjoyed – (B) fruit', '(A) painted – (B) rice', '(A) missed – (B) fish'],
    "정답 ▶ (A) enjoyed – (B) meat\n(A) 아름다운 자연을 '즐겼다' → enjoyed\n(B) 채소와 '고기'가 많았다 → meat",
    ["I enjoyed the beautiful nature", "It had a lot of vegetables and meat"])],
)

# ═════════════ 4과 대화문 ② In Everyday Life + Enjoy the Clip ═════════════
Q4 = [('Mina', "How was your weekend, Jason?", "주말은 어땠어, Jason?"), ('Jason', "It was good. I went to a baking class on Saturday.", "좋았어. 나는 토요일에 제빵 수업을 들으러 갔어."),
      ('Mina', "Oh, what did you make?", "오, 무엇을 만들었니?"), ('Jason', "I made apple pies and chocolate cookies.", "사과 파이와 초콜릿 쿠키를 만들었어."),
      ('Mina', "Sounds delicious!", "맛있겠다!"), ('Jason', "I brought some of them with me. Would you like some, Mina?", "내가 그중 몇 개를 가져왔어. 좀 먹어 볼래, 미나야?"),
      ('Mina', "Sure. Wow, they're so good.", "물론이지. 와, 정말 맛있다.")]
Q5 = [('Jisu', "Welcome to Jisu's channel!", "지수의 채널에 오신 걸 환영해요!"), ('Jisu', "Today is a traditional Korean holiday, Dano.", "오늘은 한국의 전통적인 명절인 단오입니다."),
      ('Jisu', "So I'm making surichwitteok with my dad now.", "그래서 저는 지금 아빠와 함께 수리취떡을 만들고 있어요."), ('Jisu', "It's rice cake with a wheel pattern.", "그것은 바퀴 문양을 가진 떡이랍니다."),
      ('Jisu', "It's finally ready!", "마침내 떡이 준비되었어요!"), ('Jisu', "It looks delicious.", "맛있어 보이네요."), ('Jisu', "Would you like some?", "좀 드셔 보실래요?")]
K4b = ['4과 대화 4 · 제빵 수업 (In Everyday Life)', '4과 클립 · 단오 수리취떡 (Enjoy the Clip)']
P4b = dlg(K4b[0], Q4) + dlg(K4b[1], Q5)
k4b = build(
 vocab=[['weekend', '주말'], ['baking class', '제빵 수업'], ['cookie', '쿠키'], ['Sounds delicious!', '맛있겠다!'], ['bring', '가져오다 (bring - brought - brought)'],
        ['some of them', '그중 몇 개'], ['Welcome to ~', '~에 오신 걸 환영합니다'], ['traditional', '전통적인'], ['holiday', '명절, 휴일'], ['rice cake', '떡'],
        ['wheel', '바퀴'], ['pattern', '무늬, 문양'], ['finally', '마침내'], ['ready', '준비된'], ['look delicious', '맛있어 보이다']],
 pickv=[
  (T(Q4, 1).replace('a baking class', 'a {baking|swimming} class'), "정답 ▶ baking (제빵)\n오답 ▶ swimming: 그 수업에서 파이와 쿠키를 만들었으니 '제빵' 수업이에요."),
  (T(Q5, 1).replace('Korean holiday', 'Korean {holiday|food}'), "정답 ▶ holiday (명절)\n오답 ▶ food: 단오(Dano)는 한국의 전통 '명절'이에요."),
  (T(Q5, 3).replace('wheel pattern', 'wheel {pattern|color}'), "정답 ▶ pattern (무늬)\n오답 ▶ color (색): 수리취떡에는 떡살로 찍은 바퀴 '무늬'가 있어요."),
 ],
 tf=[
  ("Jason went to a baking class on Sunday.", False, "정답 ▶ F\n이유: 일요일이 아니라 토요일(on Saturday)에 갔어요.", None, "I went to a baking class on Saturday"),
  ("Jason made apple pies and chocolate cookies.", True, "정답 ▶ T\n이유: I made apple pies and chocolate cookies.", None, "I made apple pies and chocolate cookies"),
  ("Mina didn't like Jason's food.", False, "정답 ▶ F\n이유: Wow, they're so good. 정말 맛있다고 했어요.", None, "they're so good"),
  ("Jisu is making surichwitteok with his mom.", False, "정답 ▶ F\n이유: 엄마가 아니라 아빠(my dad)와 만들고 있어요.", None, "I'm making surichwitteok with my dad now"),
  ("Dano is a traditional Korean holiday.", True, "정답 ▶ T\n이유: Today is a traditional Korean holiday, Dano.", None, "Today is a traditional Korean holiday, Dano"),
 ],
 resp=[
  ("A: How was your weekend?", ['It was good. I went to a baking class.', 'Yes, please.', "I'm making rice cake.", 'Sounds delicious!'],
   "정답 ▶ It was good. I went to a baking class.\n이유: 주말 소감(How was ~?)을 물으면 → 느낌(It was good) + 한 일(과거형)로 답해요."),
  ("A: I brought some cookies. Would you like some?", ['Sure. Wow, they are so good.', 'I made cookies.', 'It was good.', 'Welcome to my channel!'],
   "정답 ▶ Sure. Wow, they are so good.\n이유: 음식을 권하면(Would you like some?) → 승낙 Sure. / Yes, please. 거절 No, thanks."),
 ],
 ilchi=[
  {'box': [K4b[0]], 'q': "대화의 내용과 일치하지 <u>않는</u> 것은?",
   'opts': ["Jason took a baking class on Saturday.", "Jason made apple pies.", "Jason brought some cookies with him.", "Mina tried Jason's food.", "Mina made chocolate cookies."],
   'ex': "정답 ▶ Mina made chocolate cookies.\n이유: 초콜릿 쿠키를 만든 사람은 Jason이에요. 미나는 Jason이 가져온 것을 먹어 봤어요.",
   'per': [["Jason은 토요일에 제빵 수업을 들었다.", "I went to a baking class on Saturday", "일치"],
           ["Jason은 사과 파이를 만들었다.", "I made apple pies and chocolate cookies", "일치"],
           ["Jason은 쿠키 몇 개를 가져왔다.", "I brought some of them with me", "일치"],
           ["미나는 Jason의 음식을 먹어 봤다.", "Sure. Wow, they're so good", "일치"],
           ["미나가 초콜릿 쿠키를 만들었다.", "I made apple pies and chocolate cookies", "불일치 → Jason이 만듦"]]},
  {'box': [K4b[1]], 'q': "클립의 내용과 일치하지 <u>않는</u> 것은?",
   'opts': ["Jisu has a channel.", "Today is Dano.", "Jisu is making rice cake with his dad.", "The rice cake has a wheel pattern.", "The rice cake isn't ready yet."],
   'ex': "정답 ▶ The rice cake isn't ready yet.\n이유: It's finally ready! 마침내 떡이 준비됐다고 했어요.",
   'per': [["지수는 채널을 가지고 있다.", "Welcome to Jisu's channel", "일치"],
           ["오늘은 단오이다.", "Today is a traditional Korean holiday, Dano", "일치"],
           ["지수는 아빠와 떡을 만들고 있다.", "I'm making surichwitteok with my dad now", "일치"],
           ["떡에는 바퀴 문양이 있다.", "It's rice cake with a wheel pattern", "일치"],
           ["떡은 아직 준비되지 않았다.", "It's finally ready", "불일치"]]},
 ],
 pickg=[
  (T(Q4, 5).replace('I brought', 'I {brought|bringed}'), "정답 ▶ brought\n이유: bring의 과거형은 불규칙 brought (bring - brought - brought)"),
  (T(Q5, 2).replace("I'm making", "I'm {making|make}"), "정답 ▶ making\n이유: now(지금) 하는 중 → 현재진행형 am + -ing"),
  (T(Q5, 5).replace('looks delicious', 'looks {delicious|deliciously}'), "정답 ▶ delicious\n이유: 감각동사 look + 형용사 = ~해 보이다. 부사(deliciously)는 쓰지 않아요."),
 ],
 scr=[(T(Q4, 5).split('. ')[0] + '.', "내가 그중 몇 개를 가져왔어."), (T(Q5, 3), Q5[3][2])],
 order=[([T(Q4, i) for i in range(4)], ["Mina: 주말은 어땠어?", "Jason: 좋았어, 제빵 수업에 갔어", "Mina: 무엇을 만들었니?", "Jason: 사과 파이와 초콜릿 쿠키"])],
 blank=[
  (T(Q4, 3).replace('chocolate cookies', 'chocolate ____'), ['cookies', 'juice', 'soup', 'noodles'], "정답 ▶ cookies\n이유: 제빵 수업에서 만든 것 = 사과 파이와 초콜릿 '쿠키'"),
  (T(Q5, 1).replace('Dano', '____'), ['Dano', 'Chuseok', 'Seollal', 'Christmas'], "정답 ▶ Dano\n이유: 수리취떡은 단오에 먹는 떡이에요. 클립에서 오늘은 단오라고 했어요."),
 ],
 awk=[(['A: Would you like some cookies? B: Sure, thanks.', 'A: What did you make? B: I made apple pies.', 'A: How was your weekend? B: It was good.', 'A: Would you like some juice? B: Yes, I did.'],
       "정답 ▶ A: Would you like some juice? B: Yes, I did.\n이유: 음식을 권하는 말에는 Yes, please. / No, thanks.로 답해요. Yes, I did.는 Did you ~?의 대답이에요.")],
 func=[("밑줄 친 말과 바꿔 쓸 수 있는 것은?<br><b>Mina: <u>How was your weekend</u>, Jason?</b>", ['What was your weekend like', 'Where did you go', 'What will you do this weekend', 'Do you like weekends'],
        "정답 ▶ What was your weekend like\n이유: How was ~? = What was ~ like? (~은 어땠니? 소감 묻기)")],
 summ=[
  S([K4b[0]], "Jason took a (A) ______ class on Saturday and (B) ______ some cookies to share with Mina.",
    ['(A) baking – (B) brought', '(A) swimming – (B) brought', '(A) baking – (B) sold', '(A) painting – (B) bought', '(A) baking – (B) threw'],
    "정답 ▶ (A) baking – (B) brought\n(A) '제빵' 수업 → baking\n(B) 만든 것을 '가져왔다' → brought (bring의 과거형)",
    ["I went to a baking class on Saturday", "I brought some of them with me"]),
  S([K4b[1]], "On Dano, Jisu is making rice cake with a (A) ______ pattern, and he (B) ______ some to the viewers.",
    ['(A) wheel – (B) offers', '(A) flower – (B) offers', '(A) wheel – (B) sells', '(A) star – (B) throws', '(A) flower – (B) sells'],
    "정답 ▶ (A) wheel – (B) offers\n(A) '바퀴' 문양 → wheel\n(B) Would you like some?(좀 드셔 보실래요?) = 음식을 '권한다' → offers",
    ["It's rice cake with a wheel pattern", "Would you like some?"])],
)

# ═════════════ 5과 대화문 ① Listen and Circle 1~3 ═════════════
R1 = [('M', "You look upset. What's the matter?", "너 속상해 보인다. 무슨 일 있니?"), ('G', "I broke a flower pot in the garden. I'm sorry, Dad.", "제가 정원에 있는 화분을 깼어요. 죄송해요, 아빠."),
      ('M', "Oh, don't worry. It's okay. We can clean the garden together.", "오, 걱정하지 마. 괜찮아. 정원을 같이 치우면 돼.")]
R2 = [('G', "Isaac, are you okay?", "Isaac, 너 괜찮니?"), ('B', "I'm worried about my dog. He isn't eating a lot these days.", "우리 개가 걱정돼. 요새 밥을 많이 먹지 않아."),
      ('G', "I'm sorry to hear that. He needs to go to the animal hospital.", "안됐구나. 동물 병원에 가 봐야 할 것 같아.")]
R3 = [('G', "I'm worried about my little brother. He plays video games too much.", "나는 내 남동생이 걱정돼. 남동생은 비디오 게임을 너무 많이 해."),
      ('B', "Why don't you play with him outside? That can help.", "밖에서 남동생과 함께 노는 건 어때? 도움이 될 수 있어."),
      ('G', "You are right. I'll play soccer with him on weekends.", "네 말이 맞아. 주말마다 남동생과 함께 축구를 할게.")]
K5 = ['5과 대화 1 · 깨진 화분 (Listen and Circle)', '5과 대화 2 · 강아지 걱정 (Listen and Circle)', '5과 대화 3 · 동생 걱정 (Listen and Circle)']
P5a = dlg(K5[0], R1) + dlg(K5[1], R2) + dlg(K5[2], R3)
k5a = build(
 vocab=[['upset', '속상한'], ["What's the matter?", '무슨 일 있니?'], ['break', '깨다 (break - broke - broken)'], ['flower pot', '화분'], ['garden', '정원'],
        ["Don't worry.", '걱정하지 마.'], ['clean', '치우다, 청소하다'], ['together', '함께'], ['be worried about', '~을 걱정하다'], ['these days', '요즘'],
        ["I'm sorry to hear that.", '그것참 안됐구나.'], ['animal hospital', '동물 병원'], ['too much', '너무 많이'], ["Why don't you ~?", '~하는 게 어때?'],
        ['outside', '밖에서'], ['on weekends', '주말마다']],
 pickv=[
  (T(R1, 0).replace('look upset', 'look {upset|happy}'), "정답 ▶ upset (속상한)\n오답 ▶ happy: 뒤에 '무슨 일 있니?'라고 묻고, 소녀가 화분을 깼다고 사과해요."),
  (T(R2, 2).replace('animal hospital', 'animal {hospital|school}'), "정답 ▶ hospital (병원)\n오답 ▶ school: 개가 밥을 잘 안 먹으니 '동물 병원'에 가 봐야 해요."),
  (T(R3, 0).replace('too much', 'too {much|little}'), "정답 ▶ much\n오답 ▶ little: 동생이 걱정되는 이유 → 게임을 '너무 많이' 해서"),
 ],
 tf=[
  ("The girl broke a flower pot.", True, "정답 ▶ T\n이유: I broke a flower pot in the garden.", None, "I broke a flower pot in the garden"),
  ("The dad is angry at the girl.", False, "정답 ▶ F\n이유: don't worry. It's okay. 아빠는 괜찮다며 함께 치우자고 해요.", None, "Oh, don't worry. It's okay"),
  ("Isaac's dog is eating a lot these days.", False, "정답 ▶ F\n이유: 요즘 밥을 많이 먹지 않아요(isn't eating a lot).", None, "He isn't eating a lot these days"),
  ("The girl's little brother plays video games too much.", True, "정답 ▶ T\n이유: He plays video games too much.", None, "He plays video games too much"),
  ("The girl will play basketball with her brother.", False, "정답 ▶ F\n이유: 농구가 아니라 축구(soccer)를 할 거예요.", None, "I'll play soccer with him on weekends"),
 ],
 resp=[
  ("A: You look upset. What's the matter?", ['I broke a flower pot.', "I'm sorry to hear that.", "Don't worry.", 'You are right.'],
   "정답 ▶ I broke a flower pot.\n이유: What's the matter?(무슨 일 있니?)에는 → 안 좋은 일이나 걱정거리를 말해요."),
  ("A: I'm worried about my dog. He isn't eating a lot.", ["I'm sorry to hear that.", 'Sounds delicious!', 'Yes, please.', 'Good for you.'],
   "정답 ▶ I'm sorry to hear that.\n이유: 걱정을 들으면 → 위로 I'm sorry to hear that. / Don't worry.\n오답 ▶ Good for you.(잘됐다)는 좋은 소식에 하는 말"),
 ],
 ilchi=[{'box': K5, 'q': "대화의 내용과 일치하지 <u>않는</u> 것은?",
   'opts': ["The girl broke a flower pot in the garden.", "The dad says they can clean the garden together.", "Isaac is worried about his dog.", "The girl thinks Isaac's dog needs to see an animal doctor.", "The girl's brother plays outside too much."],
   'ex': "정답 ▶ The girl's brother plays outside too much.\n이유: 동생은 비디오 게임을 너무 많이 해요. 그래서 밖에서 같이 놀아 주라는 조언을 들었어요.",
   'per': [["소녀는 정원에서 화분을 깼다.", "I broke a flower pot in the garden", "일치"],
           ["아빠는 함께 정원을 치우면 된다고 말한다.", "We can clean the garden together", "일치"],
           ["Isaac은 자기 개를 걱정한다.", "I'm worried about my dog", "일치"],
           ["소녀는 Isaac의 개가 동물 병원에 가야 한다고 생각한다.", "He needs to go to the animal hospital", "일치"],
           ["소녀의 남동생은 밖에서 너무 많이 논다.", "He plays video games too much", "불일치 → 게임을 너무 많이 함"]]}],
 pickg=[
  (T(R1, 1).replace('I broke', 'I {broke|breaked}'), "정답 ▶ broke\n이유: break의 과거형은 불규칙 broke (break - broke - broken)"),
  (T(R2, 1).replace('worried about my dog', 'worried {about|of} my dog'), "정답 ▶ about\n이유: be worried about ~ = ~을 걱정하다 (짝꿍 전치사 about)"),
  (T(R2, 1).replace("He isn't eating", "He {isn't|doesn't} eating"), "정답 ▶ isn't\n이유: 현재진행형의 부정 = be동사 + not + -ing. doesn't 뒤에는 동사원형이 와요."),
  (T(R3, 1).replace("don't you play", "don't you {play|playing}"), "정답 ▶ play\n이유: Why don't you + 동사원형 ~? = ~하는 게 어때? (제안)"),
 ],
 scr=[(T(R1, 2).split('. ')[-1], "정원을 같이 치우면 돼."), (T(R2, 2).split('. ')[1], "동물 병원에 가 봐야 할 것 같아.")],
 order=[([T(R3, i) for i in range(3)], ["G: 남동생이 게임을 너무 많이 해서 걱정돼", "B: 밖에서 같이 노는 게 어때?", "G: 맞아, 주말마다 축구를 할게"])],
 blank=[
  (T(R2, 1).replace('these days', 'these ____'), ['days', 'years', 'times', 'pots'], "정답 ▶ days\n이유: these days = 요즘"),
  (T(R3, 2).replace("I'll play soccer", "I'll play ____"), ['soccer', 'video games', 'the piano', 'computer games'], "정답 ▶ soccer\n이유: 게임 대신 '밖에서' 함께 놀라는 조언 → 축구를 할게\n오답 ▶ video/computer games는 걱정거리 그 자체예요."),
 ],
 awk=[(['A: What\'s the matter? B: I have a bad cold.', "A: I'm worried about my test. B: Don't worry. You'll do well.", "A: Are you okay? B: I'm worried about my cat.", 'A: I broke my leg. B: That sounds great!'],
       "정답 ▶ A: I broke my leg. B: That sounds great!\n이유: 다리가 부러졌다는 말에는 I'm sorry to hear that.처럼 위로해야 해요.")],
 func=[
  ("걱정을 표현하는 말로 알맞은 것은?", ["I'm worried about my dog.", "What's the matter?", "Don't worry.", "I'm sorry to hear that."],
   "정답 ▶ I'm worried about my dog.\n이유: I'm worried about ~ = ~이 걱정돼 (걱정 표현)\n오답 ▶ What's the matter?(묻기) / Don't worry.(위로) / I'm sorry to hear that.(위로)"),
  ("무슨 일인지 묻는 표현이 <b>아닌</b> 것은?", ["What's your hobby?", "What's wrong?", "What's the problem?", "Is there anything wrong?"],
   "정답 ▶ What's your hobby?\n이유: '취미가 뭐니?'는 취미를 묻는 말이에요. 나머지는 모두 What's the matter?와 같은 뜻이에요."),
 ],
 summ=[
  S([K5[0]], "The girl (A) ______ a flower pot, but her dad told her not to (B) ______.",
    ['(A) broke – (B) worry', '(A) bought – (B) worry', '(A) broke – (B) clean', '(A) sold – (B) cry', '(A) made – (B) worry'],
    "정답 ▶ (A) broke – (B) worry\n(A) 화분을 '깼다' → broke\n(B) 아빠: '걱정하지 마' → not to worry\n오답 ▶ clean: 아빠는 오히려 같이 치우자고 했어요.",
    ["I broke a flower pot in the garden", "Oh, don't worry"]),
  S([K5[1], K5[2]], "Isaac's dog isn't eating a lot, and the girl's brother plays (A) ______ too much, so she will play (B) ______ with him.",
    ['(A) video games – (B) soccer', '(A) soccer – (B) video games', '(A) video games – (B) the piano', '(A) basketball – (B) soccer', '(A) the guitar – (B) chess'],
    "정답 ▶ (A) video games – (B) soccer\n(A) 동생은 '비디오 게임'을 너무 많이 함 → video games\n(B) 주말마다 함께 '축구' → soccer\n오답 ▶ ②는 두 낱말을 바꾼 함정!",
    ["He plays video games too much", "I'll play soccer with him on weekends"])],
)

# ═════════════ 5과 대화문 ② In Everyday Life + Enjoy the Clip ═════════════
R4 = [('Eric', "What's the matter, Bomin?", "보민아, 무슨 일이야?"), ('Bomin', "I'm too nervous about tomorrow's basketball game, Eric.", "내일 농구 경기 때문에 너무 긴장돼, Eric."),
      ('Eric', "I feel just like you, but we practiced a lot.", "나도 너와 같은 기분이지만, 우리 연습 많이 했잖아."),
      ('Bomin', "I missed the ball many times during the last game. So I'm worried about tomorrow's game.", "나는 지난 경기 때 공을 여러 번 놓쳤어. 그래서 내일 경기가 걱정돼."),
      ('Eric', "Don't worry. We all learn from our mistakes. You'll do better this time.", "걱정하지 마. 우리 모두 실수에서 배우는 거야. 너는 이번에는 더 잘할 거야."),
      ('Bomin', "Thanks, Eric. I feel better now.", "고마워, Eric. 이제 기분이 훨씬 나아졌어.")]
R5 = [('Maria', "Hi, I'm Maria from Guatemala.", "안녕, 나는 과테말라에서 온 Maria야."), ('Maria', "In my country, many children have worry dolls.", "우리나라에서는 많은 어린이가 걱정 인형을 가지고 있어."),
      ('Maria', "Look at my worry doll.", "내 걱정 인형을 봐."), ('Maria', "I tell her about my worries and keep her under my pillow.", "나는 내 걱정 인형에게 걱정을 말하고, 베개 밑에 보관해."),
      ('Maria', "Like this.", "이렇게."), ('Maria', "Now I'm worried about the weather on my camp day next week.", "지금 나는 다음 주 캠핑 날의 날씨가 걱정돼."),
      ('Maria', "So I'll tell her about it.", "그래서 그것에 대해 인형에게 이야기할 거야."), ('Maria', "During the night, she will take away my worries!", "밤 동안 인형이 내 걱정을 가져갈 거야!")]
K5b = ['5과 대화 4 · 농구 경기 걱정 (In Everyday Life)', '5과 클립 · 걱정 인형 (Enjoy the Clip)']
P5b = dlg(K5b[0], R4) + dlg(K5b[1], R5)
k5b = build(
 vocab=[['nervous', '긴장한'], ["tomorrow's", '내일의'], ['feel just like you', '너와 똑같이 느끼다'], ['practice', '연습하다'], ['miss', '놓치다'],
        ['many times', '여러 번'], ['during', '~ 동안'], ['learn from', '~에서 배우다'], ['mistake', '실수'], ['do better', '더 잘하다'],
        ['feel better', '기분이 나아지다'], ['country', '나라'], ['worry doll', '걱정 인형'], ['pillow', '베개'], ['weather', '날씨'],
        ['camp day', '캠핑 날'], ['take away', '가져가다, 없애 주다']],
 pickv=[
  (T(R4, 4).replace('our mistakes', 'our {mistakes|games}'), "정답 ▶ mistakes (실수)\n오답 ▶ games: 공을 여러 번 놓친 보민이에게 → '실수에서 배운다'고 위로해요."),
  (T(R5, 3).replace('under my pillow', 'under my {pillow|desk}'), "정답 ▶ pillow (베개)\n오답 ▶ desk: 밤 동안(During the night) 걱정을 가져가는 인형 → 잘 때 '베개' 밑에 둬요."),
  (T(R5, 5).replace('about the weather', 'about the {weather|food}'), "정답 ▶ weather (날씨)\n오답 ▶ food: 캠핑 날에 걱정되는 것 → '날씨'"),
 ],
 tf=[
  ("Bomin is nervous about tomorrow's soccer game.", False, "정답 ▶ F\n이유: 축구가 아니라 농구 경기(basketball game)예요.", None, "I'm too nervous about tomorrow's basketball game"),
  ("Eric and Bomin practiced a lot.", True, "정답 ▶ T\n이유: we practiced a lot", None, "we practiced a lot"),
  ("Bomin still feels bad at the end.", False, "정답 ▶ F\n이유: 마지막에 I feel better now. 기분이 나아졌다고 해요.", None, "I feel better now"),
  ("Maria keeps her worry doll under her pillow.", True, "정답 ▶ T\n이유: keep her under my pillow", None, "keep her under my pillow"),
  ("Maria is worried about her test.", False, "정답 ▶ F\n이유: 시험이 아니라 다음 주 캠핑 날의 날씨(the weather)가 걱정이에요.", None, "Now I'm worried about the weather on my camp day next week"),
 ],
 resp=[
  ("A: What's the matter, Bomin?", ["I'm too nervous about tomorrow's game.", 'I feel better now.', "You'll do better this time.", 'Thanks, Eric.'],
   "정답 ▶ I'm too nervous about tomorrow's game.\n이유: 무슨 일인지 물으면(What's the matter?) → 걱정이나 문제를 말해요."),
  ("A: Don't worry. You'll do better this time.", ['Thanks. I feel better now.', "I'm sorry to hear that.", "What's the matter?", 'Yes, please.'],
   "정답 ▶ Thanks. I feel better now.\n이유: 위로를 받으면 → 고맙다고 하며 기분이 나아졌다고 답해요."),
 ],
 ilchi=[
  {'box': [K5b[0]], 'q': "대화의 내용과 일치하지 <u>않는</u> 것은?",
   'opts': ["Bomin has a basketball game tomorrow.", "Eric feels nervous, too.", "Eric and Bomin practiced a lot.", "Bomin missed the ball many times in the last game.", "Bomin feels worse after talking with Eric."],
   'ex': "정답 ▶ Bomin feels worse after talking with Eric.\n이유: Eric의 위로를 듣고 I feel better now.(기분이 나아졌어)라고 했어요.",
   'per': [["보민이는 내일 농구 경기가 있다.", "I'm too nervous about tomorrow's basketball game", "일치"],
           ["Eric도 긴장된다.", "I feel just like you", "일치"],
           ["둘은 연습을 많이 했다.", "we practiced a lot", "일치"],
           ["보민이는 지난 경기에서 공을 여러 번 놓쳤다.", "I missed the ball many times during the last game", "일치"],
           ["보민이는 Eric과 이야기한 뒤 기분이 더 나빠졌다.", "I feel better now", "불일치 → 나아짐"]]},
  {'box': [K5b[1]], 'q': "클립의 내용과 일치하지 <u>않는</u> 것은?",
   'opts': ["Maria is from Guatemala.", "Many children in her country have worry dolls.", "Maria tells her doll about her worries.", "Maria is worried about the weather on her camp day.", "Maria's camp day is tomorrow."],
   'ex': "정답 ▶ Maria's camp day is tomorrow.\n이유: 캠핑 날은 내일이 아니라 다음 주(next week)예요.",
   'per': [["Maria는 과테말라 출신이다.", "Hi, I'm Maria from Guatemala", "일치"],
           ["그 나라의 많은 어린이가 걱정 인형을 가지고 있다.", "many children have worry dolls", "일치"],
           ["Maria는 인형에게 걱정을 이야기한다.", "I tell her about my worries", "일치"],
           ["Maria는 캠핑 날의 날씨를 걱정한다.", "I'm worried about the weather on my camp day", "일치"],
           ["Maria의 캠핑 날은 내일이다.", "on my camp day next week", "불일치 → 다음 주"]]},
 ],
 pickg=[
  (T(R4, 2).replace('we practiced', 'we {practiced|practice}'), "정답 ▶ practiced\n이유: 경기 전까지 이미 '연습했다' → 과거형 practiced"),
  (T(R4, 4).replace("You'll do better", "You'll {do|doing} better"), "정답 ▶ do\n이유: You'll = You will. 조동사 will + 동사원형"),
  (T(R5, 1).replace('many children', 'many {children|child}'), "정답 ▶ children\n이유: many + 셀 수 있는 명사의 복수형. child의 복수형은 불규칙 children"),
  (T(R5, 7).replace('During the night', '{During|For} the night'), "정답 ▶ During\n이유: during + 특정 기간(the night, the game) = ~ 동안. for + 기간의 길이(an hour, two days)"),
 ],
 scr=[(T(R4, 4).split('. ')[1] + '.', "우리 모두 실수에서 배우는 거야."), (T(R5, 3), R5[3][2])],
 order=[([T(R4, i) for i in range(4)], ["Eric: 무슨 일이야?", "Bomin: 내일 농구 경기 때문에 너무 긴장돼", "Eric: 나도 그래, 하지만 연습 많이 했잖아", "Bomin: 지난번에 공을 많이 놓쳐서 걱정돼"])],
 blank=[
  (T(R4, 3).replace('missed the ball', 'missed the ____'), ['ball', 'bus', 'class', 'test'], "정답 ▶ ball\n이유: 농구 경기 이야기 → '공'을 여러 번 놓쳤다"),
  (T(R5, 7).replace('my worries', 'my ____'), ['worries', 'dolls', 'pillows', 'dreams'], "정답 ▶ worries\n이유: '걱정 인형'은 밤 동안 '걱정'을 가져가 줘요."),
 ],
 awk=[(["A: What's wrong? B: I lost my bag.", "A: I'm nervous about the test. B: Don't worry. You'll do well.", 'A: Thanks. I feel better now. B: Glad to hear that.', "A: I'm worried about my grandma. B: Sounds fun!"],
       "정답 ▶ A: I'm worried about my grandma. B: Sounds fun!\n이유: 걱정을 말하는 친구에게 '재미있겠다!'는 어색해요. → I'm sorry to hear that. / Don't worry.")],
 func=[("밑줄 친 말과 의미가 같은 것은?<br><b>Eric: <u>What's the matter</u>, Bomin?</b>", ["What's wrong", "What's your name", "What time is it", "What do you want"],
        "정답 ▶ What's wrong\n이유: What's the matter? = What's wrong? = What's the problem? (무슨 일이야?)")],
 summ=[
  S([K5b[0]], "Bomin was worried after (A) ______ the ball many times, but Eric said we all learn from our (B) ______.",
    ['(A) missing – (B) mistakes', '(A) catching – (B) mistakes', '(A) missing – (B) friends', '(A) kicking – (B) games', '(A) throwing – (B) teachers'],
    "정답 ▶ (A) missing – (B) mistakes\n(A) 공을 여러 번 '놓쳐서' 걱정 → missing\n(B) 우리 모두 '실수'에서 배운다 → mistakes",
    ["I missed the ball many times during the last game", "We all learn from our mistakes"]),
  S([K5b[1]], "Maria tells her worry doll about her (A) ______, and the doll will take them (B) ______ during the night.",
    ['(A) worries – (B) away', '(A) dreams – (B) away', '(A) worries – (B) back', '(A) toys – (B) out', '(A) friends – (B) home'],
    "정답 ▶ (A) worries – (B) away\n(A) 인형에게 '걱정'을 말한다 → worries\n(B) 밤 동안 걱정을 '가져간다' → take away",
    ["I tell her about my worries", "she will take away my worries"])],
)

D = lambda i, r, st, p, s: {'id': i, 'name': 'DAY', 'range': r, 'story': st, 'passage': p, 'steps': s}
K4A = D('k4a', '4과 대화문 ① 대화 1~3', 'Lesson 4 · 음식 권하기 · 경험 묘사하기 (Listen and Check)', P4a, k4a)
K4B = D('k4b', '4과 대화문 ② 대화 4·클립', 'Lesson 4 · 제빵 수업 · 단오 수리취떡', P4b, k4b)
K5A = D('k5a', '5과 대화문 ① 대화 1~3', 'Lesson 5 · 감정이나 상태 묻기 · 걱정 표현하기 (Listen and Circle)', P5a, k5a)
K5B = D('k5b', '5과 대화문 ② 대화 4·클립', 'Lesson 5 · 농구 경기 걱정 · 걱정 인형', P5b, k5b)

path = '/home/claude/proj/data/m1-chunjae-so-L6.js'
PK = json.loads(subprocess.check_output(['node', '-e', "global.window={};require('%s');process.stdout.write(JSON.stringify(window.PKG))" % path]))
by = {d['id']: d for d in PK['days']}
base = [d for d in PK['days'] if not d['id'].startswith('k')]
assert [d['id'] for d in base] == ['L4a', 'L4b', 'L5a', 'L5b', 'd1', 'd2'], [d['id'] for d in base]
order = [K4A, K4B, by['L4a'], by['L4b'], K5A, K5B, by['L5a'], by['L5b'], by['d1'], by['d2']]
for i, d in enumerate(order): d['name'] = 'DAY %d' % (i + 1)
PK['days'] = order
PK['pick'] = True
src = open(path).read(); head = src[:src.index('window.PKG')]
if '대화문' not in head: head = head.rstrip('\n') + '\n/* 10/28: 4·5과 대화문 추가(scratchpad/gen_m1cdlg.py), 10분 분량으로 쪼개서 pick(고르기) */\n'
write(PK, path, head)
print('ok', [(d['id'], d['name'], d['range']) for d in order])
