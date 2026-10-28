import sys, json, subprocess
sys.path.insert(0, '/tmp/claude-0/-home-claude/a9e3e882-1f02-5d62-8f70-aced81bc59d2/scratchpad')
from gencommon import *
from dlgcommon import *
# 중2 비상(황종배) 7과 대화문 (10/28). 출처: hwp20 (Everyday Communication 1·2). 10분 단위 DAY, pick

T = lambda R, i: R[i][1]
def S(box, s, o, x, ev): return (None, box, s, o, x, ev)
def ER(s, w, f, x): return (s, w, f, x)

# ═════════════ 7과 ① Everyday Communication 1 (경험한 일 묻고 답하기) ═════════════
A1 = [('W', "Have you climbed Hallasan?", "너는 한라산에 올라가 본 적 있어?"), ('M', "No, I haven't. Have you?", "아니, 없어. 너는?"),
      ('W', "No, but I'm going to go there with my uncle this weekend.", "나는 없지만, 이번 주말에 삼촌과 함께 거기에 갈 거야."),
      ('M', "That's cool. I hope you have a great time with your family.", "멋지다. 네가 가족과 좋은 시간 보내길 바라."), ('W', "Thanks.", "고마워.")]
A2 = [('W', "What are you going to do this winter?", "너는 이번 겨울에 뭐 할 거야?"), ('M', "I'm going to travel to Sydney. Have you been there?", "나는 시드니로 여행 갈 거야. 너는 거기 가 본 적 있어?"),
      ('W', "No, I haven't. What are your plans there?", "아니, 없어. 거기서 너의 계획은 뭐야?"), ('M', "I'm going to visit the Sydney Opera House with my family.", "나는 가족과 함께 시드니 오페라하우스를 방문할 거야."),
      ('W', "Sounds exciting!", "정말 신나겠다!")]
A3 = [('W', "What are you watching?", "너는 무엇을 보고 있니?"), ('M', "I'm watching Steve Kim's magic show. Have you watched his show before?", "난 Steve Kim의 마술쇼를 보고 있어. 너는 그의 쇼를 전에 본 적 있어?"),
      ('W', "Yes, I have. I really like his show.", "응, 있어. 난 그의 쇼를 정말 좋아해."), ('M', "Look at this card magic. It is amazing.", "이 카드 마술 좀 봐. 정말 놀라워."),
      ('W', "Yeah, he moves his hands really fast!", "응, 그는 손을 정말 빠르게 움직인다!")]
A4 = [('M', "Excuse me, I'd like to sign up for a one-day class.", "실례합니다, 저는 원데이 클래스를 신청하고 싶어요."), ('W', "Have you taken a one-day class here before?", "여기서 전에 원데이 클래스를 들어본 적 있으세요?"),
      ('M', "No, this is my first time.", "아니요, 이번이 처음이에요."), ('W', "Okay, I'll help you. What do you want to learn?", "알겠습니다, 제가 도와드릴게요. 무엇을 배우고 싶으세요?"),
      ('M', "I'm interested in experiencing foreign cultures.", "저는 외국 문화를 체험하는 데 관심이 있어요."),
      ('W', "Then, we have two Vietnamese culture classes. One is hat-making and the other is traditional cooking.", "그러면 베트남 문화 수업이 두 가지가 있어요. 하나는 모자 만들기이고, 다른 하나는 전통 요리예요."),
      ('M', "Oh, I'd love to make a Vietnamese hat.", "오, 저는 베트남 모자를 만들어 보고 싶어요."), ('W', "That's a great choice! The hat-making class is a lot of fun.", "좋은 선택이에요! 모자 만들기 수업은 매우 재미있어요.")]
K7a = ['7과 Listen & Choose 1 · 한라산', '7과 Listen & Choose 2 · 시드니', '7과 Listen & Choose 3 · 마술쇼', '7과 Watch & Guess · 원데이 클래스']
P7a = dlg(K7a[0], A1) + dlg(K7a[1], A2) + dlg(K7a[2], A3) + dlg(K7a[3], A4)
v7a = build(
 vocab=[['climb', '오르다'], ['Have you (ever) p.p. ~?', '~해 본 적 있니? (경험 묻기)'], ["That's cool.", '멋지다.'], ['I hope ~', '~하길 바라'], ['travel to', '~로 여행 가다'],
        ['plan', '계획'], ['Sounds exciting!', '신나겠다!'], ['magic show', '마술쇼'], ['before', '전에'], ['amazing', '놀라운'],
        ['sign up for', '~을 신청하다'], ['one-day class', '원데이 클래스, 일일 강좌'], ['this is my first time', '이번이 처음이다'], ['experience', '체험하다, 경험하다'],
        ['foreign culture', '외국 문화'], ['Vietnamese', '베트남의'], ['one ~, the other ...', '(둘 중) 하나는 ~, 다른 하나는 …'], ['traditional', '전통의'], ['choice', '선택']],
 pickv=[
  (T(A1, 2).replace('with my uncle', 'with my {uncle|teacher}'), "정답 ▶ uncle (삼촌)\n오답 ▶ teacher: 바로 뒤에 '가족과(with your family) 좋은 시간 보내길 바라'라고 해요. 삼촌은 가족이에요."),
  (T(A3, 4).replace('really fast', 'really {fast|slowly}'), "정답 ▶ fast (빠르게)\n오답 ▶ slowly: 카드 마술이 놀라운(amazing) 이유 → 손을 정말 '빠르게' 움직여서"),
  (T(A4, 4).replace('experiencing foreign', 'experiencing {foreign|Korean}'), "정답 ▶ foreign (외국의)\n오답 ▶ Korean: 이어서 '베트남' 문화 수업을 추천받아요 → 외국 문화"),
 ],
 tf=[
  ("The girl has climbed Hallasan before.", False, "정답 ▶ F\n이유: Have you? 하고 되묻자 No라고 했어요. 이번 주말에 처음 가요.", None, "No, but I'm going to go there with my uncle this weekend"),
  ("The girl will go to Hallasan with her uncle this weekend.", True, "정답 ▶ T\n이유: I'm going to go there with my uncle this weekend.", None, "I'm going to go there with my uncle this weekend"),
  ("The boy is going to visit the Sydney Opera House.", True, "정답 ▶ T\n이유: I'm going to visit the Sydney Opera House with my family.", None, "I'm going to visit the Sydney Opera House"),
  ("The girl has never watched Steve Kim's show.", False, "정답 ▶ F\n이유: Have you watched his show before? → Yes, I have. 본 적이 있어요.", None, "Yes, I have. I really like his show"),
  ("The man has taken a one-day class there before.", False, "정답 ▶ F\n이유: No, this is my first time. 이번이 처음이에요.", None, "No, this is my first time"),
  ("The man wants to make a Vietnamese hat.", True, "정답 ▶ T\n이유: Oh, I'd love to make a Vietnamese hat.", None, "I'd love to make a Vietnamese hat"),
 ],
 resp=[
  ("A: Have you been to Sydney?", ["No, I haven't.", "No, I didn't.", 'Yes, I do.', 'Sounds exciting!'],
   "정답 ▶ No, I haven't.\n이유: Have you + p.p. ~?(현재완료 경험 묻기) → Yes, I have. / No, I haven't.\n오답 ▶ didn't, do는 질문의 조동사(have)와 맞지 않아요."),
  ("A: Have you watched his show before?", ['Yes, I have. I really like his show.', 'Yes, I am.', "No, I don't.", "I'm watching a magic show."],
   "정답 ▶ Yes, I have. I really like his show.\n이유: Have you ~?에는 have로 답해요."),
 ],
 ilchi=[
  {'box': [K7a[0], K7a[1], K7a[2]], 'q': "대화의 내용과 일치하지 <u>않는</u> 것은?",
   'opts': ["The girl has been to Sydney.", "The boy has not climbed Hallasan.", "The boy is going to travel to Sydney this winter.", "The girl really likes Steve Kim's show.", "The boy thinks the card magic is amazing."],
   'ex': "정답 ▶ The girl has been to Sydney.\n이유: Have you been there?(시드니에 가 봤니?)에 No, I haven't.라고 했어요.",
   'per': [["소녀는 시드니에 가 본 적이 있다.", "No, I haven't. What are your plans there", "불일치"], ["소년은 한라산에 올라가 본 적이 없다.", "No, I haven't. Have you", "일치"],
           ["소년은 이번 겨울에 시드니로 여행 갈 것이다.", "I'm going to travel to Sydney", "일치"], ["소녀는 Steve Kim의 쇼를 정말 좋아한다.", "I really like his show", "일치"],
           ["소년은 카드 마술이 놀랍다고 생각한다.", "It is amazing", "일치"]]},
  {'box': [K7a[3]], 'q': "대화의 내용과 일치하지 <u>않는</u> 것은?",
   'opts': ["The man chooses the traditional cooking class.", "The man wants to sign up for a one-day class.", "It is the man's first time taking a one-day class there.", "There are two Vietnamese culture classes.", "The man is interested in experiencing foreign cultures."],
   'ex': "정답 ▶ The man chooses the traditional cooking class.\n이유: 남자는 베트남 모자를 만들고 싶다(I'd love to make a Vietnamese hat)고 했어요. → 모자 만들기 수업",
   'per': [["남자는 전통 요리 수업을 고른다.", "I'd love to make a Vietnamese hat", "불일치 → 모자 만들기"], ["남자는 원데이 클래스를 신청하고 싶어 한다.", "I'd like to sign up for a one-day class", "일치"],
           ["남자는 그곳에서 원데이 클래스를 처음 듣는다.", "this is my first time", "일치"], ["베트남 문화 수업은 두 가지가 있다.", "we have two Vietnamese culture classes", "일치"],
           ["남자는 외국 문화 체험에 관심이 있다.", "I'm interested in experiencing foreign cultures", "일치"]]},
 ],
 pickg=[
  (T(A1, 0).replace('Have you climbed', 'Have you {climbed|climb}'), "정답 ▶ climbed\n이유: 경험 묻기 → 현재완료 Have you + 과거분사(p.p.) ~?"),
  (T(A1, 3).replace('I hope you have', 'I hope you {have|having}'), "정답 ▶ have\n이유: I hope (that) + 주어 + 동사 → you have (네가 ~하길 바라)"),
  (T(A4, 0).replace("I'd like to sign", "I'd like {to sign|signing}"), "정답 ▶ to sign\n이유: would like + to부정사 = ~하고 싶다 (I'd = I would)"),
  (T(A4, 4).replace('in experiencing', 'in {experiencing|experience}'), "정답 ▶ experiencing\n이유: 전치사 in 뒤에는 동명사(-ing). be interested in -ing"),
  (T(A4, 5).replace('and the other is', 'and {the other|another} is'), "정답 ▶ the other\n이유: 둘 중 하나는 one, 나머지 하나는 the other. (셋 이상일 때 '또 다른 하나'가 another)"),
 ],
 error=[
  ER("No, I [[haven't]]. What [[is]] your [[plans]] there?", 1, 'are',
     "틀린 곳 ▶ ② is → are\n이유: 주어 your plans(복수) → are\n나머지 ▶ ① haven't(Have you been ~?의 대답) ✔ ③ plans ✔"),
  ER("I'm [[watching]] Steve Kim's magic show. Have you [[watch]] his show [[before]]?", 1, 'watched',
     "틀린 곳 ▶ ② watch → watched\n이유: 현재완료 Have you + 과거분사(p.p.) ~? (watch - watched - watched)\n나머지 ▶ ① watching(현재진행) ✔ ③ before ✔"),
 ],
 scr=[(T(A4, 1), A4[1][2]), ("I hope you have a great time with your family.", "네가 가족과 좋은 시간 보내길 바라.")],
 order=[([T(A2, i) for i in range(5)], ["W: 이번 겨울에 뭐 할 거야?", "M: 시드니로 여행 가, 가 본 적 있어?", "W: 아니, 거기서 계획은?", "M: 가족과 오페라하우스 방문", "W: 신나겠다!"])],
 blank=[
  (T(A4, 6).replace('Vietnamese hat', 'Vietnamese ____'), ['hat', 'cake', 'dish', 'song'], "정답 ▶ hat\n이유: 바로 뒤에 The hat-making class is a lot of fun.이라고 해요. → 모자 만들기 수업을 골랐어요."),
  (T(A3, 3).replace('this card magic', 'this card ____'), ['magic', 'game', 'letter', 'shop'], "정답 ▶ magic\n이유: Steve Kim의 '마술'쇼를 보며 카드 '마술'이 놀랍다고 해요."),
 ],
 awk=[(["A: Have you tried Vietnamese food? B: Yes, I did.", "A: Have you climbed Hallasan? B: No, I haven't.", "A: What are you watching? B: I'm watching a magic show.", "A: I'm going to travel to Sydney. B: Sounds exciting!"],
       "정답 ▶ A: Have you tried Vietnamese food? B: Yes, I did.\n이유: Have you + p.p. ~? 질문에는 Yes, I have. / No, I haven't.로 답해요.")],
 func=[
  ("경험을 묻는 표현으로 알맞은 것은?", ['Have you ever tried sushi?', 'Would you like some sushi?', 'Do you want to try sushi?', 'What are you going to eat?'],
   "정답 ▶ Have you ever tried sushi?\n이유: Have you (ever) + p.p. ~? = ~해 본 적 있니? (경험 묻기)\n오답 ▶ Would you like ~? / Do you want ~?는 음식 권하기"),
  ("빈칸에 알맞은 말은?<br><b>A: Have you ever been to Jeju Island?<br>B: No, ______. I've never been there.</b>", ["I haven't", "I didn't", "I don't", "I wasn't"],
   "정답 ▶ I haven't\n이유: Have you ~? → No, I haven't. 뒤 문장 I've never been there.(한 번도 가 본 적 없어)와도 이어져요."),
 ],
 summ=[
  S([K7a[0], K7a[1]], "The girl hasn't climbed Hallasan, but she will go there with her (A) ______ this weekend, and the boy is going to (B) ______ to Sydney this winter.",
    ['(A) uncle – (B) travel', '(A) friends – (B) travel', '(A) uncle – (B) move', '(A) dad – (B) write', '(A) teacher – (B) swim'],
    "정답 ▶ (A) uncle – (B) travel\n(A) 이번 주말 '삼촌'과 한라산에 감 → uncle\n(B) 이번 겨울 시드니로 '여행' 감 → travel",
    ["I'm going to go there with my uncle this weekend", "I'm going to travel to Sydney"]),
  S([K7a[3]], "The man is interested in experiencing foreign cultures, so he chooses the Vietnamese (A) ______ class instead of the traditional (B) ______ class.",
    ['(A) hat-making – (B) cooking', '(A) cooking – (B) hat-making', '(A) dancing – (B) cooking', '(A) hat-making – (B) music', '(A) painting – (B) sports'],
    "정답 ▶ (A) hat-making – (B) cooking\n(A) 베트남 모자를 만들고 싶다 → hat-making\n(B) 다른 하나는 전통 '요리' 수업 → cooking\n오답 ▶ ②는 두 수업을 바꾼 함정!",
    ["I'd love to make a Vietnamese hat", "One is hat-making and the other is traditional cooking"])],
)

# ═════════════ 7과 ② Everyday Communication 2 (음식 권하고 답하기) ═════════════
B1 = [('W', "Hi, Dad. I'm home.", "안녕하세요, 아빠. 저 집에 왔어요."), ('M', "Hi, Susan. I've made some hot dogs for a snack. Would you like some?", "안녕, Susan. 간식으로 핫도그를 만들었어. 좀 먹어 볼래?"),
      ('W', "Actually, I just had gimbap with my friends. Can I have them later?", "사실, 방금 친구들과 김밥을 먹고 왔어요. 나중에 먹어도 될까요?"),
      ('M', "Sure. I'll put them in the refrigerator.", "물론이지. 냉장고에 넣어 둘게."), ('W', "Thank you, Dad.", "감사합니다, 아빠.")]
B2 = [('W', "Are you making spaghetti, Uncle David? It smells really good.", "David 삼촌, 스파게티 만들고 계세요? 냄새가 정말 좋아요."), ('M', "No. I'm making tteokbokki.", "아니야. 떡볶이를 만들고 있어."),
      ('W', "Is it really tteokbokki? The sauce is white.", "정말 떡볶이 맞아요? 소스가 하얀데요."), ('M', "Yes. I've made a creamy one. Would you like some?", "응. 크림 소스로 만들었어. 좀 먹어 볼래?"),
      ('W', "Okay, I'll try it.", "네, 한 번 먹어 볼게요.")]
B3 = [('W', "I'm so hungry, but it's only 10 a.m.", "나 배가 너무 고파, 그런데 아직 오전 10시야."), ('M', "Didn't you eat anything in the morning?", "너는 아침에 아무것도 안 먹었어?"),
      ('W', "No. I woke up late, so I couldn't.", "응. 나는 늦게 일어나서 못 먹었어."), ('M', "I brought some sandwiches. Would you like some?", "내가 샌드위치를 좀 가져왔어. 좀 먹어 볼래?"),
      ('W', "Oh, that would be great. Thank you.", "오, 너무 좋아. 고마워.")]
B4 = [('M', "What are you cooking, Lucy?", "Lucy, 너는 뭐 요리하고 있어?"), ('W', "I'm making paella. I'm going to share it with my friends at school tomorrow.", "나는 파에야를 만들고 있어. 내일 학교에서 친구들과 그걸 나눠 먹을 거야."),
      ('M', "Oh, what is paella?", "오, 파에야가 뭐야?"), ('W', "It's a traditional Spanish rice dish with seafood and vegetables.", "그건 해산물과 채소가 들어간 스페인 전통 쌀 요리야."),
      ('M', "It smells nice.", "냄새가 좋다."), ('W', "Would you like some?", "좀 먹어 볼래?"),
      ('M', "Yes, I'd like some. Wow, it tastes really good. I'm sure your friends will love this.", "응, 먹어 볼게. 와, 정말 맛있다. 네 친구들은 분명 이걸 좋아할 거야."),
      ('W', "Thanks. I hope so.", "고마워. 그러길 바라.")]
K7b = ['7과 Listen & Number 1 · 핫도그', '7과 Listen & Number 2 · 크림 떡볶이', '7과 Listen & Number 3 · 샌드위치', '7과 Watch & Present · 파에야']
P7b = dlg(K7b[0], B1) + dlg(K7b[1], B2) + dlg(K7b[2], B3) + dlg(K7b[3], B4)
v7b = build(
 vocab=[["I'm home.", '다녀왔습니다.'], ['snack', '간식'], ['Would you like some?', '좀 드실래요? (음식 권하기)'], ['actually', '사실은'], ['later', '나중에'],
        ['refrigerator', '냉장고'], ['smell good', '좋은 냄새가 나다'], ['sauce', '소스'], ['creamy', '크림 같은, 크림이 든'], ['try', '(음식을) 먹어 보다'],
        ['hungry', '배고픈'], ['wake up late', '늦게 일어나다 (wake - woke - woken)'], ['bring', '가져오다 (bring - brought - brought)'], ['That would be great.', '그거 좋겠다.'],
        ['share A with B', 'A를 B와 나누다'], ['rice dish', '쌀 요리'], ['seafood', '해산물'], ['taste good', '맛이 좋다'], ["I'm sure ~", '분명 ~일 거야'], ['I hope so.', '그러길 바라.']],
 pickv=[
  (T(B1, 3).replace('in the refrigerator', 'in the {refrigerator|oven}'), "정답 ▶ refrigerator (냉장고)\n오답 ▶ oven: 지금은 안 먹고 나중에 먹겠다고 하니 상하지 않게 '냉장고'에 넣어 둬요."),
  (T(B2, 2).replace('is white', 'is {white|red}'), "정답 ▶ white (하얀)\n오답 ▶ red: 보통 떡볶이는 빨간데 크림 소스로 만들어서 '하얘서' 정말 떡볶이냐고 물어요."),
  (T(B4, 3).replace('with seafood', 'with {seafood|chocolate}'), "정답 ▶ seafood (해산물)\n오답 ▶ chocolate: 파에야는 해산물과 채소가 들어간 스페인 전통 쌀 요리예요."),
 ],
 tf=[
  ("Susan's dad made some hot dogs.", True, "정답 ▶ T\n이유: I've made some hot dogs for a snack.", None, "I've made some hot dogs for a snack"),
  ("Susan eats the hot dogs right away.", False, "정답 ▶ F\n이유: 방금 김밥을 먹어서 나중에 먹겠다(Can I have them later?)고 해요.", None, "Can I have them later"),
  ("Uncle David is making spaghetti.", False, "정답 ▶ F\n이유: 스파게티가 아니라 떡볶이(tteokbokki)를 만들고 있어요.", None, "No. I'm making tteokbokki"),
  ("The tteokbokki has a creamy sauce.", True, "정답 ▶ T\n이유: I've made a creamy one.", None, "I've made a creamy one"),
  ("The girl ate breakfast in the morning.", False, "정답 ▶ F\n이유: 늦게 일어나서 못 먹었어요(I couldn't).", None, "I woke up late, so I couldn't"),
  ("Lucy is going to share the paella with her friends.", True, "정답 ▶ T\n이유: I'm going to share it with my friends at school tomorrow.", None, "I'm going to share it with my friends at school tomorrow"),
 ],
 resp=[
  ("A: I've made some hot dogs. Would you like some?", ['Yes, please.', 'Yes, I have.', "No, I didn't.", "I'm home."],
   "정답 ▶ Yes, please.\n이유: 음식을 권하면(Would you like some?) → 수락 Yes, please. / 거절 No, thanks.\n오답 ▶ Yes, I have.는 Have you ~?의 대답"),
  ("A: Wow, it tastes really good. I'm sure your friends will love this.", ['Thanks. I hope so.', 'Yes, please.', 'No, thanks.', "I'm so hungry."],
   "정답 ▶ Thanks. I hope so.\n이유: 친구들이 좋아할 거라는 칭찬에 → 고마워, 그러길 바라. (so = 친구들이 좋아하는 것)"),
 ],
 ilchi=[
  {'box': [K7b[0], K7b[1], K7b[2]], 'q': "대화의 내용과 일치하지 <u>않는</u> 것은?",
   'opts': ["The boy brought some hot dogs for the girl.", "Susan had gimbap with her friends.", "Susan's dad will put the hot dogs in the refrigerator.", "Uncle David made tteokbokki with a creamy sauce.", "The girl woke up late."],
   'ex': "정답 ▶ The boy brought some hot dogs for the girl.\n이유: 대화 3에서 소년이 가져온 것은 핫도그가 아니라 샌드위치(sandwiches)예요. 핫도그는 대화 1에서 Susan의 아빠가 만들었어요.",
   'per': [["소년은 소녀를 위해 핫도그를 가져왔다.", "I brought some sandwiches", "불일치 → 샌드위치"], ["Susan은 친구들과 김밥을 먹었다.", "I just had gimbap with my friends", "일치"],
           ["아빠는 핫도그를 냉장고에 넣을 것이다.", "I'll put them in the refrigerator", "일치"], ["David 삼촌은 크림 소스 떡볶이를 만들었다.", "I've made a creamy one", "일치"],
           ["소녀는 늦게 일어났다.", "I woke up late", "일치"]]},
  {'box': [K7b[3]], 'q': "대화의 내용과 일치하지 <u>않는</u> 것은?",
   'opts': ["The boy doesn't like the paella.", "Lucy is making paella.", "Paella is a traditional Spanish rice dish.", "Lucy will share the paella at school tomorrow.", "The boy tastes the paella."],
   'ex': "정답 ▶ The boy doesn't like the paella.\n이유: 먹어 보고 정말 맛있다(it tastes really good)며 친구들도 좋아할 거라고 했어요.",
   'per': [["소년은 파에야를 좋아하지 않는다.", "it tastes really good", "불일치"], ["Lucy는 파에야를 만들고 있다.", "I'm making paella", "일치"],
           ["파에야는 스페인 전통 쌀 요리이다.", "It's a traditional Spanish rice dish", "일치"], ["Lucy는 내일 학교에서 파에야를 나눠 먹을 것이다.", "share it with my friends at school tomorrow", "일치"],
           ["소년은 파에야를 먹어 본다.", "Yes, I'd like some", "일치"]]},
 ],
 pickg=[
  (T(B1, 1).replace("I've made some", "I've {made|make} some"), "정답 ▶ made\n이유: 현재완료 have + 과거분사(p.p.) → I've made (만들어 놨어)"),
  (T(B2, 0).replace('smells really good', 'smells really {good|well}'), "정답 ▶ good\n이유: 감각동사 smell + 형용사 = ~한 냄새가 나다. well(부사)은 보어가 될 수 없어요."),
  (T(B3, 2).replace('so I couldn\'t', 'so I {couldn\'t|can\'t}'), "정답 ▶ couldn't\n이유: 아침에 못 먹은 건 지난 일 → can의 과거 could (I couldn't = 먹을 수 없었어)"),
  (T(B4, 1).replace('share it with', 'share it {with|to}'), "정답 ▶ with\n이유: share A with B = A를 B와 나누다 (짝꿍 전치사 with)"),
  (T(B2, 3).replace('a creamy one', 'a creamy {one|it}'), "정답 ▶ one\n이유: 앞에 나온 명사(sauce)와 같은 종류의 '하나'를 가리킬 때는 one. a + 형용사 + one (a creamy one = 크림 소스)"),
 ],
 error=[
  ER("I [[brought]] some sandwiches. Would you [[like]] [[any]]?", 2, 'some',
     "틀린 곳 ▶ ③ any → some\n이유: 무언가를 권하는 의문문(Would you like ~?)에서는 some을 써요. any는 일반적인 의문문·부정문에서 써요.\n나머지 ▶ ① brought(bring의 과거) ✔ ② like ✔"),
  ER("Actually, I just [[had]] gimbap with my friends. Can I [[had]] them [[later]]?", 1, 'have',
     "틀린 곳 ▶ ② had → have\n이유: 조동사 Can + 동사원형\n나머지 ▶ ① had(have의 과거, 먹었다) ✔ ③ later ✔"),
 ],
 scr=[("I'm sure your friends will love this.", "네 친구들은 분명 이걸 좋아할 거야."), (T(B1, 3), B1[3][2])],
 order=[([T(B4, i) for i in range(4)], ["M: 뭐 요리하고 있어?", "W: 파에야, 내일 친구들과 나눠 먹을 거야", "M: 파에야가 뭐야?", "W: 해산물과 채소가 든 스페인 쌀 요리"])],
 blank=[
  (T(B3, 0).replace("I'm so hungry", "I'm so ____"), ['hungry', 'full', 'sleepy', 'busy'], "정답 ▶ hungry\n이유: 늦게 일어나 아침을 못 먹어서 '배고파'요. 그래서 샌드위치를 권받아요.\n오답 ▶ full(배부른)은 반대"),
  (T(B2, 1).replace("I'm making tteokbokki", "I'm making ____"), ['tteokbokki', 'spaghetti', 'pizza', 'gimbap'], "정답 ▶ tteokbokki\n이유: 바로 뒤에 Is it really tteokbokki?라고 놀라며 되물어요. 스파게티냐는 질문에는 No라고 했어요."),
 ],
 awk=[(["A: Would you like some pizza? B: Yes, I have.", "A: Would you like some? B: No, thanks. I'm full.", "A: I'm sure your friends will love this. B: I hope so.", "A: I'm so hungry. B: I brought some sandwiches. Would you like some?"],
       "정답 ▶ A: Would you like some pizza? B: Yes, I have.\n이유: 음식을 권하는 말에는 Yes, please. / No, thanks.로 답해요. Yes, I have.는 Have you ~?의 대답이에요.")],
 func=[
  ("음식을 권하는 표현이 <b>아닌</b> 것은?", ['Have you tried pasta?', 'Would you like some pasta?', 'Please try some pasta.', 'Do you want some pasta?'],
   "정답 ▶ Have you tried pasta?\n이유: '파스타 먹어 본 적 있니?'는 경험을 묻는 말이에요. 나머지는 모두 음식을 권하는 표현이에요."),
  ("권하는 음식을 거절하는 말로 알맞은 것은?", ['No, thanks.', 'Yes, please.', "Okay, I'll try it.", "Yes, I'd like some."],
   "정답 ▶ No, thanks.\n이유: 거절 → No, thanks. / I'm good, thank you.\n오답 ▶ 나머지는 모두 수락하는 말"),
 ],
 summ=[
  S([K7b[0], K7b[1]], "Susan will have the hot dogs (A) ______ because she just had gimbap, and Uncle David's tteokbokki has a (B) ______ sauce.",
    ['(A) later – (B) white', '(A) now – (B) white', '(A) later – (B) red', '(A) tomorrow – (B) spicy', '(A) never – (B) brown'],
    "정답 ▶ (A) later – (B) white\n(A) 방금 김밥을 먹어서 '나중에' 먹겠다 → later\n(B) 크림 소스라 '하얀' 소스 → white",
    ["Can I have them later", "The sauce is white"]),
  S([K7b[3]], "Lucy made paella, a traditional Spanish rice dish, to (A) ______ with her friends, and the boy thinks her friends will (B) ______ it.",
    ['(A) share – (B) love', '(A) sell – (B) love', '(A) share – (B) hate', '(A) cook – (B) throw', '(A) buy – (B) forget'],
    "정답 ▶ (A) share – (B) love\n(A) 친구들과 '나눠' 먹을 것 → share\n(B) 친구들이 분명 '좋아할' 것 → love",
    ["I'm going to share it with my friends at school tomorrow", "I'm sure your friends will love this"])],
)

D = lambda i, r, st, p, s: {'id': i, 'name': 'DAY', 'range': r, 'story': st, 'passage': p, 'steps': s}
V7A = D('v7a', '7과 대화문 ① 경험 묻기', 'Lesson 7 · 경험한 일 묻고 답하기 (Have you ~?)', P7a, v7a)
V7B = D('v7b', '7과 대화문 ② 음식 권하기', 'Lesson 7 · 음식 권하고 답하기 (Would you like some?)', P7b, v7b)

path = '/home/claude/proj/data/m2-visang-hwang-L7.js'
PK = json.loads(subprocess.check_output(['node', '-e', "global.window={};require('%s');process.stdout.write(JSON.stringify(window.PKG))" % path]))
by = {d['id']: d for d in PK['days']}
assert all(k in by for k in ['d1', 'd2', 'd3', 'd4']), list(by)
extra8 = [by[k] for k in ('v8a', 'v8b') if k in by]  # 8과 대화문(나중에 추가)
order = [V7A, V7B, by['d1'], by['d2']] + extra8 + [by['d3'], by['d4']]
for i, d in enumerate(order): d['name'] = 'DAY %d' % (i + 1)
for d in order: ansfirst(d['steps'])
for d in (V7A, V7B): d['steps'][0]['quizN'] = 12
PK['days'] = order
PK['pick'] = True
src = open(path).read(); head = src[:src.index('window.PKG')]
if '대화문' not in head: head = head.rstrip('\n') + '\n/* 10/28: 7과 대화문 v7a/v7b (scratchpad/gen_m2vdlg.py) 7과 본문 앞, 10분 분량 · pick */\n'
write(PK, path, head)
print('ok', [(d['id'], d['name'], d['range']) for d in order])
