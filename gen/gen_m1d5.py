import sys, json, subprocess
sys.path.insert(0, '/tmp/claude-0/-home-claude/a9e3e882-1f02-5d62-8f70-aced81bc59d2/scratchpad')
from gencommon import *

# 중1 동아(윤정미): 7과 대화문 · 5과 대화문 · 5과 본문(Who Threw a Cake at the Monalisa?)
# 시험 범위 5·6·7과 (8과 제외). 순서: 6과 → 7과(대화문, 본문) → 5과(대화문, 본문)

from dlgcommon import *
# ═════════════ 7과 대화문 ═════════════
A1 = [('G', "What do you want to be in the future, Minsu?", "앞으로 무엇이 되고 싶니, 민수야?"), ('B', "I want to be a sports reporter.", "나는 스포츠 기자가 되고 싶어."),
      ('G', "Oh, really? Do you watch a lot of sports games?", "오, 정말? 스포츠 경기를 많이 보니?"), ('B', "Yes, I do. I'm interested in all kinds of sports.", "응, 그래. 나는 모든 종류의 스포츠에 관심이 있어.")]
A2 = [('G', "David, what are you making?", "David, 무엇을 만들고 있니?"), ('B', "I'm making pizza and pasta.", "피자와 파스타를 만들고 있어."),
      ('G', "They look delicious. Are you interested in Italian food?", "맛있어 보인다. 너는 이탈리아 음식에 관심 있니?"), ('B', "Yes, I am. I want to be a world-famous chef in the future!", "응, 그래. 나는 앞으로 세계적으로 유명한 요리사가 되고 싶어!")]
A3 = [('G', "What's this music, Hojin? It's awesome.", "이 음악 뭐야, 호진아? 굉장하다."), ('B', "I'm writing a song with this computer program.", "나는 이 컴퓨터 프로그램으로 노래를 만들고 있어."),
      ('G', "You're very good. Do you want to be a songwriter?", "정말 잘하는구나. 너는 작곡가가 되고 싶니?"), ('B', "Yes, I'm really interested in writing songs.", "응, 나는 노래를 만드는 것에 정말로 관심이 있어.")]
A4 = [('G', "Are you interested in fashion, Jacob?", "패션에 관심이 있니, Jacob?"), ('B', "Yes, I love to make clothes.", "응, 나는 옷 만드는 것을 매우 좋아해."),
      ('G', "Really? That's so cool!", "정말? 너무 멋있다!"), ('B', "Thanks. I want to be a fashion designer. I'll make clothes for you someday.", "고마워. 나는 패션 디자이너가 되고 싶어. 언젠가 너에게 옷을 만들어 줄게.")]
A5 = [('G', "Jiho, why don't we try this? We can fly an airplane!", "지호야, 우리 이거 한번 해 보는 게 어때? 우리는 비행기를 조종해 볼 수 있어!"), ('B', "Sure. It looks like fun!", "물론이야. 재미있어 보인다!"),
      ('G', "Do you want to be a pilot in the future?", "너는 앞으로 조종사가 되고 싶니?"), ('B', "Yes, I'm interested in flying airplanes. How about you, Lucy?", "응, 나는 비행기를 조종하는 것에 관심이 있어. 너는 어때, Lucy?"),
      ('G', "I'm interested in making airplanes, not flying. I want to be an airplane engineer.", "나는 비행기를 만드는 것에 관심이 있어, 조종하는 것 말고. 나는 비행기 엔지니어가 되고 싶어."),
      ('B', "That sounds cool!", "멋있다!"), ('G', "Thank you. I want to make an airplane someday!", "고마워. 나는 언젠가 비행기를 만들고 싶어!"),
      ('B', "Let's fly this airplane, and then we can try making an airplane, too.", "이 비행기를 조종해 보자, 그런 다음에 비행기를 만들어 볼 수도 있어."), ('G', "Good idea.", "좋은 생각이야.")]
M7 = '7과 대화 5 · 비행기 체험 (Watch, Answer, and Talk)'
c7 = build(
 vocab=[['future', '미래'], ['be interested in', '~에 관심이 있다'], ['reporter', '기자'], ['all kinds of', '모든 종류의'], ['look delicious', '맛있어 보이다'],
        ['world-famous', '세계적으로 유명한'], ['chef', '요리사'], ['awesome', '굉장한'], ['songwriter', '작곡가'], ['fashion designer', '패션 디자이너'],
        ['someday', '언젠가'], ["Why don't we ~?", '~하는 게 어때?'], ['fly', '(비행기를) 조종하다; 날다'], ['pilot', '조종사'], ['engineer', '엔지니어'],
        ['sound cool', '멋지게 들리다'], ['How about you?', '너는 어때?'], ["Let's ~", '~하자'], ['try -ing', '(시험 삼아) ~해 보다']],
 pickv=[
  (T(A2, 2).replace('look delicious', 'look {delicious|terrible}'), "정답 ▶ delicious (맛있는)\n오답 ▶ terrible (끔찍한): 요리사가 꿈인 친구가 만든 피자와 파스타 → '맛있어 보인다'는 칭찬이에요."),
  (T(A3, 2).replace('a songwriter', 'a {songwriter|chef}'), "정답 ▶ songwriter (작곡가)\n오답 ▶ chef (요리사): 컴퓨터 프로그램으로 노래를 만들고 있으니 '작곡가'가 되고 싶은지 물어요."),
  (T(A4, 1).replace('make clothes', 'make {clothes|songs}'), "정답 ▶ clothes (옷)\n오답 ▶ songs (노래): 패션에 관심 있냐는 질문의 대답 → '옷 만드는 것'을 좋아해요."),
  (T(A5, 2).replace('a pilot', 'a {pilot|chef}'), "정답 ▶ pilot (조종사)\n오답 ▶ chef: 비행기를 조종해 볼 수 있다고 했으니 '조종사'가 되고 싶은지 물어요."),
  (T(A5, 4).replace('not flying', 'not {flying|cooking}'), "정답 ▶ flying (조종하는 것)\n오답 ▶ cooking: Lucy는 비행기를 '조종하는 것'이 아니라 '만드는 것'에 관심이 있어요."),
 ],
 tf=[
  ("Minsu wants to be a cameraman.", False, "정답 ▶ F\n이유: 민수는 스포츠 기자(a sports reporter)가 되고 싶어 해요.", None, "I want to be a sports reporter"),
  ("David is making Italian food.", True, "정답 ▶ T\n이유: 피자와 파스타 = 이탈리아 음식을 만들고 있어요.", None, "I'm making pizza and pasta"),
  ("Hojin is writing a song with a computer program.", True, "정답 ▶ T\n이유: I'm writing a song with this computer program.", None, "I'm writing a song with this computer program"),
  ("Jacob wants to be a fashion model.", False, "정답 ▶ F\n이유: 모델이 아니라 패션 디자이너(a fashion designer)가 되고 싶어 해요.", None, "I want to be a fashion designer"),
  ("Lucy wants to be a pilot.", False, "정답 ▶ F\n이유: 조종사가 되고 싶은 건 지호예요. Lucy는 비행기 엔지니어가 되고 싶어 해요.", None, "I want to be an airplane engineer"),
  ("Jiho is interested in flying airplanes.", True, "정답 ▶ T\n이유: Yes, I'm interested in flying airplanes.", None, "I'm interested in flying airplanes"),
 ],
 resp=[
  ("A: What do you want to be in the future?", ['I want to be a chef.', "I'm making pizza.", 'Yes, I do.', 'I like sports games.'],
   "정답 ▶ I want to be a chef.\n이유: 장래 희망(What do you want to be ~?)을 물으면 'I want to be + 직업'으로 답해요.\n오답 ▶ Yes, I do.는 Do you ~? 질문의 대답"),
  ("A: Are you interested in Italian food?", ['Yes, I am.', 'Yes, I do.', "No, I don't.", 'Yes, it is.'],
   "정답 ▶ Yes, I am.\n이유: Are you ~?(be동사 의문문)에는 Yes, I am. / No, I'm not.으로 답해요.\n오답 ▶ Yes, I do. / No, I don't.는 Do you ~? 질문의 대답"),
  ("A: Do you want to be a songwriter?", ['Yes, I do.', 'Yes, I am.', "No, I'm not.", 'Yes, it does.'],
   "정답 ▶ Yes, I do.\n이유: Do you ~?(일반동사 의문문)에는 Yes, I do. / No, I don't.로 답해요."),
  ("A: Why don't we try this? We can fly an airplane!", ['Sure. It looks like fun!', "No, I'm not.", 'I want to be a pilot.', 'Yes, I do.'],
   "정답 ▶ Sure. It looks like fun!\n이유: Why don't we ~?(~하는 게 어때?)는 제안이에요. 수락은 Sure. / Good idea. / Sounds good."),
 ],
 pickg=[
  (T(A1, 3).replace('interested in all', 'interested {in|on} all'), "정답 ▶ in\n이유: be interested in ~ = ~에 관심이 있다 (짝꿍 전치사 in)"),
  (T(A2, 1).replace("I'm making", "I'm {making|make}"), "정답 ▶ making\n이유: 지금 하고 있는 일 → 현재진행형 be + -ing (I'm making)"),
  (T(A3, 3).replace('in writing', 'in {writing|write}'), "정답 ▶ writing\n이유: 전치사 in 뒤에는 동명사(-ing). be interested in -ing = ~하는 것에 관심이 있다"),
  (T(A5, 0).replace("don't we try", "don't we {try|trying}"), "정답 ▶ try\n이유: Why don't we + 동사원형 ~? = ~하는 게 어때?"),
  (T(A4, 3).replace('I want to be a fashion', 'I want {to be|being} a fashion'), "정답 ▶ to be\n이유: want + to부정사 = ~하고 싶다. want 뒤에 -ing는 쓰지 않아요."),
 ],
 scr=[(T(A1, 0), A1[0][2]), (T(A5, 2), A5[2][2]), ("I'm interested in making airplanes, not flying.", "나는 비행기를 만드는 것에 관심이 있어, 조종하는 것 말고.")],
 order=[
  ([T(A2, i) for i in range(4)], ["G: 무엇을 만들고 있니?", "B: 피자와 파스타", "G: 맛있어 보여, 이탈리아 음식에 관심 있니?", "B: 응, 요리사가 되고 싶어"]),
  ([T(A5, i) for i in range(5)], ["G: 이거 해 보는 게 어때? 비행기 조종!", "B: 물론, 재미있겠다", "G: 조종사가 되고 싶니?", "B: 응, 조종에 관심 있어. 너는?", "G: 나는 만드는 것에 관심, 엔지니어가 꿈"]),
 ],
 blank=[
  (T(A1, 0).replace('want to be', 'want to ____'), ['be', 'do', 'make', 'play'], "정답 ▶ be\n이유: What do you want to be ~? = 무엇이 되고 싶니? (장래 희망 묻기)"),
  (T(A5, 4).replace('an airplane engineer', 'an airplane ____'), ['engineer', 'pilot', 'chef', 'reporter'], "정답 ▶ engineer\n이유: 비행기를 '만드는 것'에 관심 있으니 비행기 '엔지니어'. pilot은 조종하는 사람"),
  (T(A5, 0).replace('fly an airplane', 'fly an ____'), ['airplane', 'car', 'bike', 'boat'], "정답 ▶ airplane\n이유: fly(조종하다)할 수 있는 것은 비행기예요."),
 ],
 awk=[
  (['A: Are you interested in music? B: Yes, I do.', "A: What are you interested in? B: I'm interested in cooking.", 'A: What do you want to be? B: I want to be a pilot.', "A: Why don't we play soccer? B: Sure. Sounds fun!"],
   "정답 ▶ A: Are you interested in music? B: Yes, I do.\n이유: Are you ~? 질문이니 Yes, I am.으로 답해야 해요."),
  (["A: What do you want to be in the future? B: I'm making pizza.", 'A: Do you want to be a songwriter? B: Yes, I do.', "A: What are you making? B: I'm making a cake.", 'A: How about you? B: I want to be a chef.'],
   "정답 ▶ A: What do you want to be in the future? B: I'm making pizza.\n이유: 장래 희망을 물었는데 지금 만드는 음식을 말했어요. → I want to be a chef. 처럼 답해야 해요."),
 ],
 func=[
  ("관심 있는 것을 묻는 표현으로 알맞은 것은?", ['What are you interested in?', 'What do you want to be?', 'What are you making?', 'Why not?'],
   "정답 ▶ What are you interested in?\n이유: 관심 묻기 = What are you interested in? / Are you interested in ~?\n대답 ▶ I'm interested in + 명사/동명사"),
  ("장래 희망을 묻는 표현이 <b>아닌</b> 것은?", ['What are you good at?', 'What do you want to be in the future?', 'What do you want to do in the future?', "What's your dream job?"],
   "정답 ▶ What are you good at?\n이유: '무엇을 잘하니?'는 잘하는 것을 묻는 표현이에요. 나머지는 모두 장래 희망을 물어요."),
 ],
 ilchi=[
  {'box': [M7], 'q': "대화의 내용과 일치하지 <u>않는</u> 것은?",
   'opts': ["Lucy wants to be a pilot.", "Jiho is interested in flying airplanes.", "Lucy wants to make an airplane someday.", "They will fly an airplane first.", "Jiho thinks Lucy's dream sounds cool."],
   'ex': "정답 ▶ Lucy wants to be a pilot.\n이유: 조종사(pilot)가 꿈인 사람은 지호예요. Lucy는 비행기 엔지니어가 되고 싶어 해요.",
   'per': [["Lucy는 조종사가 되고 싶어 한다.", "I want to be an airplane engineer", "불일치 → 엔지니어"],
           ["지호는 비행기 조종에 관심이 있다.", "I'm interested in flying airplanes", "일치"],
           ["Lucy는 언젠가 비행기를 만들고 싶어 한다.", "I want to make an airplane someday", "일치"],
           ["그들은 먼저 비행기를 조종할 것이다.", "Let's fly this airplane, and then", "일치"],
           ["지호는 Lucy의 꿈이 멋지다고 생각한다.", "That sounds cool", "일치"]]},
  {'box': [M7], 'q': "두 사람이 대화 직후에 할 일로 알맞은 것은?",
   'opts': ['비행기 조종 체험하기', '비행기 만들기', '피자 만들기', '노래 만들기', '옷 만들기'],
   'ex': "정답 ▶ 비행기 조종 체험하기\n이유: Let's fly this airplane, and then we can try making an airplane, too. → 먼저 조종(fly), 그다음에 만들기\n포인트 ▶ and then(그런 다음에) 앞뒤 순서 확인!",
   'per': [["", "Let's fly this airplane", "정답"], ["", "and then we can try making an airplane", "✘ 그다음 할 일"], ["", "", "✘"], ["", "", "✘"], ["", "", "✘"]]},
 ],
 summ=[(None, [M7], "Jiho is interested in (A) ______ airplanes, but Lucy wants to (B) ______ airplanes as an engineer.",
        ['(A) flying – (B) make', '(A) making – (B) fly', '(A) flying – (B) fly', '(A) selling – (B) buy', '(A) drawing – (B) clean'],
        "정답 ▶ (A) flying – (B) make\n(A) 지호: 비행기 '조종'에 관심 → flying\n(B) Lucy: 비행기를 '만드는' 엔지니어 → make\n오답 ▶ 두 사람의 관심을 바꾼 ②에 주의!",
        ["I'm interested in flying airplanes", "I'm interested in making airplanes, not flying"])],
)
P7 = dlg('7과 대화 1 · 스포츠 기자', A1) + dlg('7과 대화 2 · 요리사', A2) + dlg('7과 대화 3 · 작곡가', A3) + dlg('7과 대화 4 · 패션 디자이너', A4) + dlg(M7, A5)

# ═════════════ 5과 대화문 ═════════════
B1 = [('W', "Excuse me, but you must not talk on the phone here.", "실례합니다만, 여기서는 통화하시면 안 됩니다."), ('B', "I'm terribly sorry. I'll turn off my phone.", "정말 죄송합니다. 휴대폰을 끌게요."),
      ('W', "You don't have to. Texting is OK.", "그럴 필요는 없어요. 문자하는 것은 괜찮아요."), ('B', "I see. Thank you.", "알겠습니다. 감사합니다.")]
B2 = [('G', "Excuse me. May I touch this golden bear?", "실례합니다. 이 황금 곰을 만져 봐도 될까요?"), ('M', "No, you may not. You must not touch anything in this room.", "아니요, 안 됩니다. 이 방에서는 어떤 것도 만지면 안 됩니다."),
      ('G', "OK, I understand.", "네, 알겠습니다.")]
B3 = [('B', "May I go to the video room, Mom?", "엄마, 비디오방에 가도 돼요?"), ('W', "Of course, but don't run.", "물론이지, 하지만 뛰지는 마라."),
      ('B', "Why not?", "왜 안 돼요?"), ('W', "Look at that sign. You must not run inside the museum.", "저 표지판을 보렴. 박물관 안에서 뛰면 안 된단다.")]
B4 = [('B', "May I take food into the museum?", "박물관에 음식을 가지고 들어가도 되나요?"), ('W', "No, you may not. You must not bring any food inside.", "아니요, 안 됩니다. 어떤 음식도 내부로 가져오시면 안 됩니다."),
      ('B', "How about water?", "물은 어떤가요?"), ('W', "Only bottled water is OK.", "병에 든 물만 괜찮습니다.")]
B5 = [('M', "Everybody, look over here, please. This is Sunflowers by Van Gogh.", "여러분, 이쪽을 봐 주세요. 이것은 반 고흐의 '해바라기'입니다."),
      ('G', "Wow, this is my favorite painting. May I take a picture of it?", "와, 제가 가장 좋아하는 그림이에요. 이 그림의 사진을 찍어도 될까요?"),
      ('M', "Yes, you may, but you must not use the flash.", "네, 됩니다. 하지만 플래시를 사용하시면 안 됩니다."), ('G', "Why not? It's a little dark in here.", "왜 안 되나요? 여기는 좀 어두운데요."),
      ('M', "I'm sorry, but using the flash can damage paintings.", "죄송하지만, 플래시를 사용하는 것은 그림들을 훼손할 수 있습니다."), ('G', "Oh, I didn't know that.", "아, 그건 몰랐어요."),
      ('M', "Everyone, we'll move on to Monet's paintings next.", "여러분, 우리는 다음에 모네의 그림으로 이동하겠습니다."), ('G', "Great!", "좋아요!")]
M5 = '5과 대화 5 · 미술관에서 (Watch, Answer, and Talk)'
c5 = build(
 vocab=[['must not', '~하면 안 된다'], ['talk on the phone', '통화하다'], ['terribly', '정말, 몹시'], ['turn off', '(전원을) 끄다'], ["don't have to", '~할 필요 없다'],
        ['text', '문자를 보내다'], ['May I ~?', '~해도 될까요?'], ['touch', '만지다'], ['golden', '황금의'], ['understand', '이해하다'],
        ['sign', '표지판'], ['inside', '~ 안에(서)'], ['bring', '가져오다'], ['How about ~?', '~은 어때요?'], ['bottled water', '병에 든 물'],
        ['look over here', '이쪽을 보다'], ['favorite', '가장 좋아하는'], ['take a picture', '사진을 찍다'], ['flash', '(카메라) 플래시'], ['dark', '어두운'],
        ['damage', '손상시키다'], ['move on to', '~로 이동하다']],
 pickv=[
  (T(B1, 1).replace('turn off', 'turn {off|on}'), "정답 ▶ off\n이유: 통화하면 안 된다는 말에 사과하며 휴대폰을 '끈다(turn off)'고 해요. turn on은 켜다"),
  (T(B3, 3).replace('that sign', 'that {sign|picture}'), "정답 ▶ sign (표지판)\n오답 ▶ picture (그림): '뛰지 마시오' 같은 규칙은 '표지판'에 적혀 있어요."),
  (T(B4, 3).replace('Only bottled', 'Only {bottled|hot}'), "정답 ▶ bottled (병에 든)\n오답 ▶ hot (뜨거운): 음식은 안 되지만 '병에 든' 물은 괜찮아요."),
  (T(B5, 4).replace('can damage', 'can {damage|clean}'), "정답 ▶ damage (손상시키다)\n오답 ▶ clean (깨끗하게 하다): 플래시를 쓰면 안 되는 이유 → 그림을 '훼손할' 수 있어서"),
  (T(B5, 3).replace('a little dark', 'a little {dark|hot}'), "정답 ▶ dark (어두운)\n오답 ▶ hot (더운): 플래시가 필요한 이유 → 안이 좀 '어두워서'"),
 ],
 tf=[
  ("The boy can send text messages there.", True, "정답 ▶ T\n이유: Texting is OK. 문자하는 것은 괜찮아요.", None, "Texting is OK"),
  ("The girl can touch the golden bear.", False, "정답 ▶ F\n이유: No, you may not. 이 방에서는 어떤 것도 만지면 안 돼요.", None, "You must not touch anything in this room"),
  ("The boy can run inside the museum.", False, "정답 ▶ F\n이유: 박물관 안에서 뛰면 안 돼요(must not run).", None, "You must not run inside the museum"),
  ("Visitors may bring bottled water into the museum.", True, "정답 ▶ T\n이유: Only bottled water is OK.", None, "Only bottled water is OK"),
  ("The girl can take a picture of the painting.", True, "정답 ▶ T\n이유: Yes, you may. 사진은 찍어도 돼요.", None, "Yes, you may, but you must not use the flash"),
  ("The girl can use the flash.", False, "정답 ▶ F\n이유: 플래시는 사용하면 안 돼요(must not use the flash).", None, "you must not use the flash"),
 ],
 resp=[
  ("A: May I touch this golden bear?", ['No, you may not.', 'Yes, I may.', "No, I don't.", 'Yes, it is.'],
   "정답 ▶ No, you may not.\n이유: May I ~?(허락 구하기) → 수락 Yes, you may. / 거절 No, you may not.\n오답 ▶ Yes, I may.(주어가 you여야 해요)"),
  ("A: Excuse me, but you must not talk on the phone here.", ["I'm terribly sorry.", "You're welcome.", 'Yes, you may.', 'Good idea.'],
   "정답 ▶ I'm terribly sorry.\n이유: 금지(must not)를 들으면 사과하고 따르는 게 자연스러워요."),
  ("A: May I go to the video room, Mom?", ["Of course, but don't run.", 'No, I may not.', "I'm sorry to hear that.", 'Yes, I do.'],
   "정답 ▶ Of course, but don't run.\n이유: 허락(Of course) + 조건(but don't run). Of course = Yes, you may."),
  ("A: Why not? It's a little dark in here.", ["I'm sorry, but using the flash can damage paintings.", 'Yes, you may.', 'Great!', 'Only bottled water is OK.'],
   "정답 ▶ I'm sorry, but using the flash can damage paintings.\n이유: Why not?(왜 안 되나요?)에는 '이유'로 답해요."),
 ],
 pickg=[
  (T(B1, 0).replace('must not talk', 'must not {talk|talking}'), "정답 ▶ talk\n이유: must not + 동사원형 = ~하면 안 된다 (금지)"),
  (T(B5, 1).replace('a picture of it', 'a picture of {it|them}'), "정답 ▶ it\n이유: 가리키는 것은 this painting(단수) → it"),
  (T(B5, 4).replace('but using the flash', 'but {using|use} the flash'), "정답 ▶ using\n이유: '플래시를 사용하는 것은'이 주어 → 동명사(-ing). 동사원형 use는 주어가 될 수 없어요."),
  (T(B1, 2).replace('Texting is', '{Texting|Text} is'), "정답 ▶ Texting\n이유: '문자하는 것은'이 주어 → 동명사(-ing). 동사원형 Text는 주어 자리에 올 수 없어요."),
  (T(B2, 0).replace('May I touch', 'May I {touch|touching}'), "정답 ▶ touch\n이유: May I + 동사원형 ~? = ~해도 될까요?"),
 ],
 scr=[(T(B2, 1).split('. ')[1], "이 방에서는 어떤 것도 만지면 안 됩니다."), (T(B3, 3).split('. ')[1], "박물관 안에서 뛰면 안 된단다."), ("May I take a picture of it?", "이 그림의 사진을 찍어도 될까요?")],
 order=[
  ([T(B3, i) for i in range(4)], ["B: 비디오방에 가도 돼요?", "W: 물론, 하지만 뛰지 마", "B: 왜 안 돼요?", "W: 표지판 봐, 뛰면 안 돼"]),
  ([T(B5, i) for i in range(4)], ["M: 이쪽을 보세요, 고흐의 해바라기", "G: 사진 찍어도 될까요?", "M: 네, 하지만 플래시는 안 돼요", "G: 왜요? 어두운데요"]),
 ],
 blank=[
  (T(B1, 2).replace('Texting', '____'), ['Texting', 'Talking', 'Eating', 'Running'], "정답 ▶ Texting\n이유: 통화(talk)는 안 되지만 '문자하는 것'은 괜찮다고 해서 휴대폰을 끌 필요가 없어요."),
  (T(B4, 1).replace('any food', 'any ____'), ['food', 'books', 'friends', 'shoes'], "정답 ▶ food\n이유: 음식을 가지고 들어가도 되냐는 질문에 '어떤 음식도' 안 된다고 답해요."),
  (T(B5, 6).replace("Monet's", "____'s"), ['Monet', 'Van Gogh', 'Botero', 'Picasso'], "정답 ▶ Monet\n이유: 고흐의 '해바라기' 다음에 '모네'의 그림으로 이동해요."),
 ],
 awk=[
  (['A: May I sit here? B: Yes, I may.', 'A: May I use your pen? B: Sure, go ahead.', "A: May I open the window? B: No, you may not. It's cold.", "A: You must not eat here. B: Oh, I'm sorry."],
   "정답 ▶ A: May I sit here? B: Yes, I may.\n이유: 허락해 줄 때는 Yes, you may.예요. (주어 you)"),
  (['A: Can I take pictures here? B: Yes, you must not.', 'A: May I come in? B: Of course.', "A: Don't run here. B: OK, I won't.", 'A: How about water? B: Only bottled water is OK.'],
   "정답 ▶ A: Can I take pictures here? B: Yes, you must not.\n이유: Yes(허락)와 must not(금지)이 서로 반대예요. Yes, you can. / No, you must not.처럼 말해야 해요."),
 ],
 func=[
  ("허락을 구하는 표현으로 알맞은 것은?", ['May I use your phone?', 'You must not use your phone.', "Don't use your phone.", 'Why not?'],
   "정답 ▶ May I use your phone?\n이유: May I ~? / Can I ~? = ~해도 될까요? (허락 구하기)\n오답 ▶ must not, Don't ~는 금지하기"),
  ("빈칸에 들어갈 말로 알맞지 <b>않은</b> 것은?<br><b>A: May I eat snacks here?<br>B: ______ You must not eat in the library.</b>", ['Sure, go ahead.', 'No, you may not.', "I'm sorry, but you can't.", "No, you can't."],
   "정답 ▶ Sure, go ahead.\n이유: 뒤에 '먹으면 안 된다(must not)'가 오니 거절이 와야 해요. Sure, go ahead.는 허락이에요."),
  ("밑줄 친 부분의 뜻으로 알맞은 것은?<br><b>B: I'll turn off my phone.<br>W: <u>You don't have to.</u> Texting is OK.</b>", ['그럴 필요 없어요.', '그러면 안 돼요.', '그렇게 해야 해요.', '그렇게 해도 돼요.'],
   "정답 ▶ 그럴 필요 없어요.\n이유: don't have to = ~할 필요가 없다 (금지가 아님!)\n비교 ▶ must not = ~하면 안 된다"),
 ],
 ilchi=[
  {'box': [M5], 'q': "대화의 내용과 일치하지 <u>않는</u> 것은?",
   'opts': ["The girl may use the flash.", "Sunflowers is the girl's favorite painting.", "It is a little dark in the room.", "Using the flash can damage paintings.", "They will see Monet's paintings next."],
   'ex': "정답 ▶ The girl may use the flash.\n이유: 사진은 찍어도 되지만 플래시는 사용하면 안 돼요(must not use the flash).",
   'per': [["소녀는 플래시를 사용해도 된다.", "you must not use the flash", "불일치"],
           ["'해바라기'는 소녀가 가장 좋아하는 그림이다.", "this is my favorite painting", "일치"],
           ["방 안이 조금 어둡다.", "It's a little dark in here", "일치"],
           ["플래시는 그림을 훼손할 수 있다.", "using the flash can damage paintings", "일치"],
           ["다음에 모네의 그림을 볼 것이다.", "we'll move on to Monet's paintings next", "일치"]]},
  {'box': [M5], 'q': "소녀가 플래시를 사용하면 안 되는 이유로 알맞은 것은?",
   'opts': ['플래시가 그림을 훼손할 수 있어서', '방이 너무 밝아서', '미술관이 문을 닫아서', '카메라가 없어서', '사진 촬영이 금지라서'],
   'ex': "정답 ▶ 플래시가 그림을 훼손할 수 있어서\n이유: I'm sorry, but using the flash can damage paintings.\n오답 ▶ 사진 촬영 자체는 허락됐어요(Yes, you may).",
   'per': [["", "using the flash can damage paintings", "정답"], ["", "It's a little dark in here", "✘ 오히려 어두움"], ["", "", "✘"], ["", "", "✘"], ["", "Yes, you may", "✘ 사진은 됨"]]},
 ],
 summ=[(None, [M5], "In the museum, the girl may (A) ______ a picture of the painting, but she must not use the (B) ______.",
        ['(A) take – (B) flash', '(A) take – (B) phone', '(A) draw – (B) flash', '(A) sell – (B) camera', '(A) touch – (B) light'],
        "정답 ▶ (A) take – (B) flash\n(A) 사진을 '찍어도' 된다 → take a picture\n(B) '플래시'는 안 된다 → flash",
        ["May I take a picture of it", "you must not use the flash"])],
)
P5 = dlg('5과 대화 1 · 통화 금지', B1) + dlg('5과 대화 2 · 만지기 금지', B2) + dlg('5과 대화 3 · 뛰기 금지', B3) + dlg('5과 대화 4 · 음식 금지', B4) + dlg(M5, B5)

# ═════════════ 5과 본문 ═════════════
S1 = [("Last Saturday, someone threw a cake at the Monalisa in the Botero Museum in Bogota, Colombia.", "지난 토요일, 누군가 콜롬비아 보고타의 보테로 박물관에 있는 '모나리자'에 케이크를 던졌다."),
      ("There were four eyewitnesses.", "네 명의 목격자가 있었다."), ("What did they say?", "그들은 뭐라고 말했을까?"), ("Read the following, and find the criminal.", "다음을 읽고, 범인을 찾아보자.")]
S2 = [("Ann Jones, a visitor", "Ann Jones, 방문객"),
      ("I was looking at the Monalisa, and someone threw a cake at the painting.", "저는 '모나리자'를 보고 있었는데, 누군가 그 그림을 향해 케이크를 던졌어요."),
      ("I turned around and saw an old man.", "저는 뒤를 돌아 한 노인을 봤어요."), ("He was standing in front of a wheelchair.", "그는 휠체어 앞에 서 있었어요."),
      ("I'm about 170 cm tall, and he was a little taller than me.", "저는 키가 170cm 정도인데, 그는 저보다 조금 더 컸어요."),
      ("Carlos Diaz, a janitor", "Carlos Diaz, 청소부"),
      ("An old man with gray hair was running away, and something fell off his head.", "회색 머리의 한 노인이 도망가고 있었는데, 그의 머리에서 무언가 떨어졌어요."),
      ("It was his wig.", "그것은 그의 가발이었어요."), ("I ran after him, but I couldn't catch him.", "저는 그를 뒤쫓았지만, 잡을 수 없었어요."),
      ("He was faster than me.", "그는 저보다 더 빨랐거든요."), ("In fact, the old man was not old.", "사실, 그 노인은 나이 든 사람이 아니었어요."),
      ("He was a young man with long brown hair.", "그는 긴 갈색 머리의 젊은 남자였어요.")]
S3 = [("Diego Perez, a guard", "Diego Perez, 경비원"),
      ("I went to the crime scene, and there were pieces of cake all over the painting.", "저는 범죄 현장에 갔는데, 그림 곳곳에 케이크 조각들이 있었어요."),
      ("There was also a wheelchair near the painting, and I found a cake box next to the wheelchair.", "그림 근처에 휠체어도 있었는데, 저는 휠체어 옆에서 케이크 상자를 발견했어요."),
      ("The box was from Camila's Bakery.", "그 상자는 Camila 빵집의 것이었어요."),
      ("Camila Santos, the owner of Camila's Bakery", "Camila Santos, Camila 빵집 주인"),
      ("Last Friday, a young man came in.", "지난 금요일, 한 젊은 남자가 들어왔어요."),
      ("I spoke to him in Spanish, but he didn't understand me.", "저는 그에게 스페인어로 말했지만, 그는 제 말을 이해하지 못했어요."),
      ("He spoke only English.", "그는 영어로만 말했어요."),
      ("We had a lot of different cakes, but he just wanted the smallest one.", "우리 가게에는 다양한 케이크가 많이 있었지만, 그는 그저 가장 작은 것을 원했어요."),
      ("We sold only one cake that day, so I remember him clearly.", "우리는 그날 케이크를 한 개만 팔아서, 저는 그를 똑똑히 기억해요."),
      ("Oh, he had blue eyes.", "아, 그는 파란색 눈을 가지고 있었어요.")]
S4 = [("Now, look at the information about the suspects.", "이제, 용의자들에 대한 정보를 보자."), ("Who threw the cake at the Monalisa?", "누가 '모나리자'에 케이크를 던졌을까?"),
      ("Andres Lozano | Height: 176 cm | Hair: long, black | Languages: Spanish, English | Eyes: brown", "Andres Lozano | 키: 176cm | 머리: 긴 검은색 | 언어: 스페인어, 영어 | 눈: 갈색"),
      ("Larry Johnson | Height: 173 cm | Hair: long, brown | Languages: English | Eyes: blue", "Larry Johnson | 키: 173cm | 머리: 긴 갈색 | 언어: 영어 | 눈: 파란색"),
      ("Tim Baker | Height: 182 cm | Hair: long, brown | Languages: English | Eyes: green", "Tim Baker | 키: 182cm | 머리: 긴 갈색 | 언어: 영어 | 눈: 초록색"),
      ("Luca Ferez | Height: 166 cm | Hair: short, gray | Languages: Spanish | Eyes: blue", "Luca Ferez | 키: 166cm | 머리: 짧은 회색 | 언어: 스페인어 | 눈: 파란색")]
L = lambda S, i: S[i][0]

da = steps(
 vocab=[['last Saturday', '지난 토요일'], ['throw', '던지다 (throw - threw - thrown)'], ['eyewitness', '목격자'], ['the following', '다음 내용'], ['criminal', '범인'],
        ['visitor', '방문객'], ['turn around', '뒤돌아보다'], ['in front of', '~ 앞에'], ['wheelchair', '휠체어'], ['about', '대략, ~쯤'],
        ['a little', '조금'], ['janitor', '청소부'], ['gray', '회색의'], ['run away', '도망가다'], ['fall off', '~에서 떨어지다 (fall - fell - fallen)'],
        ['wig', '가발'], ['run after', '~을 뒤쫓다'], ['catch', '잡다'], ['in fact', '사실은'], ['young', '젊은']],
 pickv=[
  (L(S1, 1).replace('eyewitnesses', '{eyewitnesses|criminals}'), "정답 ▶ eyewitnesses (목격자들)\n오답 ▶ criminals (범인들): 뒤에 '그들은 뭐라고 말했을까?'가 나오고, 네 사람의 진술이 이어져요."),
  (L(S1, 3).replace('the criminal', 'the {criminal|painting}'), "정답 ▶ criminal (범인)\n오답 ▶ painting: 진술을 읽고 '범인'을 찾아보는 추리 이야기예요."),
  (L(S2, 3).replace('a wheelchair', 'a {wheelchair|window}'), "정답 ▶ wheelchair (휠체어)\n오답 ▶ window: 나중에 경비원이 그림 근처에서 '휠체어'를 발견해요."),
  (L(S2, 9).replace('faster', '{faster|slower}'), "정답 ▶ faster (더 빠른)\n오답 ▶ slower: 뒤쫓았지만 '잡을 수 없었던' 이유 → 그가 더 빨라서"),
  (L(S2, 11).replace('a young man', 'a {young|old} man'), "정답 ▶ young (젊은)\n오답 ▶ old: 바로 앞 문장 '그 노인은 사실 나이 든 사람이 아니었다' → 가발을 쓴 '젊은' 남자"),
 ],
 tf=[
  ["The Monalisa was in a museum in Colombia.", True, "정답 ▶ T\n이유: the Botero Museum in Bogota, Colombia", '❶', "in the Botero Museum in Bogota, Colombia"],
  ["There were three eyewitnesses.", False, "정답 ▶ F\n이유: 목격자는 네 명(four eyewitnesses)이었어요.", '❶', "There were four eyewitnesses"],
  ["Ann saw an old man in front of a wheelchair.", True, "정답 ▶ T\n이유: He was standing in front of a wheelchair.", '❷', "He was standing in front of a wheelchair"],
  ["The man was shorter than Ann.", False, "정답 ▶ F\n이유: Ann보다 조금 더 컸어요(a little taller than me).", '❷', "he was a little taller than me"],
  ["Carlos caught the man.", False, "정답 ▶ F\n이유: 뒤쫓았지만 잡을 수 없었어요(couldn't catch him).", '❷', "I couldn't catch him"],
  ["The man was wearing a wig.", True, "정답 ▶ T\n이유: 머리에서 떨어진 것은 그의 가발(his wig)이었어요.", '❷', "It was his wig"],
 ],
 ilchi=[
  {'n': '❷', 'box': ['❷'], 'q': "글의 내용과 일치하지 <u>않는</u> 것은?",
   'opts': ["The man had short gray hair.", "Ann was looking at the Monalisa.", "Ann is about 170 cm tall.", "Something fell off the man's head.", "The man was faster than Carlos."],
   'ex': "정답 ▶ The man had short gray hair.\n이유: 회색 머리는 가발이었고, 실제로는 '긴 갈색 머리(long brown hair)'의 젊은 남자였어요.",
   'per': [["그 남자는 짧은 회색 머리였다.", "He was a young man with long brown hair", "불일치 → 긴 갈색 머리"],
           ["Ann은 '모나리자'를 보고 있었다.", "I was looking at the Monalisa", "일치"],
           ["Ann의 키는 약 170cm이다.", "I'm about 170 cm tall", "일치"],
           ["남자의 머리에서 무언가 떨어졌다.", "something fell off his head", "일치"],
           ["그 남자는 Carlos보다 빨랐다.", "He was faster than me", "일치"]]},
 ],
 pickg=[
  (L(S1, 3).replace('and find', 'and {find|found}'), "정답 ▶ find\n이유: Read ~, and find ~. 앞의 Read처럼 명령문 → 동사원형 find"),
  (L(S1, 1).replace('There were', 'There {were|was}'), "정답 ▶ were\n이유: 주어 four eyewitnesses(복수) → There were"),
  (L(S2, 1).replace('I was looking', 'I was {looking|look}'), "정답 ▶ looking\n이유: was + -ing = 과거진행형 (~하고 있었다). 케이크가 날아온 그 순간 보고 '있던' 중"),
  (L(S2, 3).replace('was standing', 'was {standing|stand}'), "정답 ▶ standing\n이유: 과거진행형 was + -ing (서 있었다)"),
  (L(S2, 4).replace('a little taller', 'a little {taller|tallest}'), "정답 ▶ taller\n이유: 두 사람 비교 + than → 비교급 taller (tall - taller - tallest)"),
  (L(S2, 8).replace("I couldn't catch", "I {couldn't|can't} catch"), "정답 ▶ couldn't\n이유: 지난 일 → can의 과거형 could. couldn't = could not"),
  (L(S2, 11).replace('man with long', 'man {with|in} long'), "정답 ▶ with\n이유: with + 특징 = ~을 가진 (a man with long hair 긴 머리를 가진 남자)"),
 ],
 verb=[
  (L(S2, 6).replace('something fell', 'something ___'), 'fall', ['fell'], "정답 ▶ fell\n이유: fall - fell - fallen (불규칙). fall off ~에서 떨어지다"),
  (L(S2, 8).replace('I ran after', 'I ___ after'), 'run', ['ran'], "정답 ▶ ran\n이유: run - ran - run (불규칙). run after ~을 뒤쫓다"),
  (L(S2, 2).replace('I turned', 'I ___'), 'turn', ['turned'], "정답 ▶ turned\n이유: 규칙 변화 turn + -ed. turn around 뒤돌아보다"),
  (L(S1, 2).replace('What did', 'What ___'), 'do', ['did'], "정답 ▶ did\n이유: 과거의 일을 묻는 일반동사 의문문 → What did + 주어 + 동사원형?"),
 ],
 error=[
  ("I'm [[about]] 170 cm tall, and he was a little [[more tall]] than [[me]].", 1, 'taller',
   "틀린 곳 ▶ ② more tall → taller\n이유: 짧은 형용사의 비교급은 -er (tall → taller)\n나머지 ▶ ① about(대략) ✔ ③ than me ✔"),
  ("It was his wig. I ran after him, but I couldn't [[catching]] him. He [[was]] faster than [[me]].", 0, 'catch',
   "틀린 곳 ▶ ① catching → catch\n이유: could(n't) + 동사원형\n나머지 ▶ ② was ✔ ③ me ✔"),
  ("In fact, the old man [[were]] not old. He was a [[young]] man [[with]] long brown hair.", 0, 'was',
   "틀린 곳 ▶ ① were → was\n이유: 주어 the old man(단수) → was\n나머지 ▶ ② young ✔ ③ with(~을 가진) ✔"),
  ("[[Read]] the following, and [[finds]] the [[criminal]].", 1, 'find',
   "틀린 곳 ▶ ② finds → find\n이유: Read ~, and find ~. 명령문 두 개 → 둘 다 동사원형\n나머지 ▶ ① Read ✔ ③ criminal ✔"),
 ],
 scr=[(L(S2, 2), S2[2][1]), (L(S2, 3), S2[3][1]), (L(S2, 9), S2[9][1]), (L(S2, 10), S2[10][1]), (L(S2, 11), S2[11][1])],
 order=[
  ([L(S2, 1), L(S2, 2), L(S2, 3), L(S2, 4)], ["모나리자를 보던 중 케이크가 날아옴", "돌아보니 노인이 있었음", "휠체어 앞에 서 있었음", "나보다 조금 컸음"]),
  ([L(S2, 6), L(S2, 7), L(S2, 8), L(S2, 9)], ["회색 머리 노인이 도망가다 무언가 떨어짐", "그것은 가발", "뒤쫓았지만 못 잡음", "그가 더 빨랐음"]),
 ],
 insert=[
  ([L(S2, 6), L(S2, 7), L(S2, 8)], 1, ["노인의 머리에서 무언가 떨어짐", "그것(It)은 가발이었음", "뒤쫓았지만 못 잡음"],
   "정답 ▶ ①\n이유: It은 바로 앞의 something(머리에서 떨어진 것)을 가리켜요."),
  ([L(S2, 9), L(S2, 10), L(S2, 11)], 1, ["그가 더 빨랐음", "사실 그 노인은 나이 든 사람이 아니었음", "긴 갈색 머리의 젊은 남자였음"],
   "정답 ▶ ①\n이유: '노인이 아니었다'고 먼저 말한 뒤, 실제 모습(젊은 남자)을 밝혀요."),
 ],
 odd=[
  ([L(S2, 2), L(S2, 3), "The old man was sitting in the wheelchair.", L(S2, 4)], 2,
   "정답 ▶ ③\n이유: 노인은 휠체어 '앞에 서 있었어요(standing)'. 휠체어에 앉아 있었다는 건 바로 앞 문장과 모순이에요."),
  ([L(S2, 8), L(S2, 9), "The old man walked very slowly.", L(S2, 10)], 2,
   "정답 ▶ ③\n이유: 그는 Carlos보다 더 빨랐어요. '아주 천천히 걸었다'는 반대예요."),
 ],
 blank=[
  (L(S1, 0).replace('threw a cake', 'threw a ____'), ['cake', 'ball', 'shoe', 'cup'], "정답 ▶ cake\n이유: 경비원이 그림 곳곳에서 '케이크' 조각을 발견해요."),
  (L(S2, 6).replace('with gray hair', 'with ____ hair'), ['gray', 'brown', 'black', 'red'], "정답 ▶ gray\n이유: 도망가던 '노인'처럼 보이게 회색 머리 가발을 썼어요. 진짜 머리는 갈색이었죠."),
  (L(S2, 11).replace('long brown', 'long ____'), ['brown', 'gray', 'blond', 'red'], "정답 ▶ brown\n이유: 가발이 벗겨진 진짜 모습 = 긴 '갈색' 머리의 젊은 남자 (범인 찾기의 단서!)"),
 ],
 gram=[
  ("밑줄 친 부분의 뜻으로 알맞은 것은?<br><b><u>In fact</u>, the old man was not old.</b>", ['사실은', '마침내', '예를 들어', '게다가'],
   "정답 ▶ 사실은\n이유: in fact = 사실은. 앞에서 '노인'이라고 했는데 실제로는 아니었다고 바로잡아요."),
  ("밑줄 친 <b>It</b>이 가리키는 것은?<br><b>Something fell off his head. <u>It</u> was his wig.</b>", ['머리에서 떨어진 것', '그 그림', '휠체어', '케이크'],
   "정답 ▶ 머리에서 떨어진 것\n이유: It은 바로 앞의 something을 가리켜요."),
  ("다음 문장의 뜻으로 알맞은 것은?<br><b>I ran after him, but I couldn't catch him.</b>", ['나는 그를 뒤쫓았지만, 잡을 수 없었다.', '나는 그에게서 도망쳤지만, 잡혔다.', '나는 그를 뒤쫓아 잡았다.', '나는 그를 기다렸지만, 오지 않았다.'],
   "정답 ▶ 나는 그를 뒤쫓았지만, 잡을 수 없었다.\n이유: run after = 뒤쫓다 / couldn't = ~할 수 없었다"),
  ("밑줄 친 <b>with</b>와 쓰임이 <b>같은</b> 것은?<br><b>He was a young man <u>with</u> long brown hair.</b>", ['a girl with blue eyes', 'I went there with my mom.', 'He cut it with a knife.', 'I agree with you.'],
   "정답 ▶ a girl with blue eyes\n이유: '~을 가진'(특징)의 with. 파란 눈을 가진 소녀\n오답 ▶ ~와 함께 / ~으로(도구) / ~에게(동의)"),
  ("다음 질문에 알맞은 대답은?<br><b>Why couldn't Carlos catch the man?</b>", ['Because the man was faster than him.', 'Because the man was in a wheelchair.', 'Because Carlos was sleeping.', 'Because the man was very old.'],
   "정답 ▶ Because the man was faster than him.\n이유: He was faster than me. → 남자가 Carlos보다 더 빨랐어요."),
 ])

db = steps(
 vocab=[['guard', '경비원'], ['crime scene', '범죄 현장'], ['piece', '조각'], ['all over', '~ 곳곳에'], ['near', '~ 근처에'], ['find', '발견하다 (find - found - found)'],
        ['next to', '~ 옆에'], ['bakery', '빵집'], ['owner', '주인'], ['come in', '들어오다'], ['speak', '말하다 (speak - spoke - spoken)'], ['Spanish', '스페인어'],
        ['understand', '이해하다'], ['different', '다양한'], ['sell', '팔다 (sell - sold - sold)'], ['remember', '기억하다'], ['clearly', '분명히, 똑똑히'],
        ['information', '정보'], ['suspect', '용의자'], ['height', '키'], ['language', '언어']],
 pickv=[
  (L(S3, 1).replace('there were pieces', 'there were {pieces|boxes}'), "정답 ▶ pieces (조각들)\n오답 ▶ boxes (상자들): 그림에 던진 케이크 '조각들'이 곳곳에 묻어 있었어요. 상자는 하나(a cake box)예요."),
  (L(S3, 2).replace('box next to', 'box {next to|far from}'), "정답 ▶ next to (~ 옆에)\n오답 ▶ far from (~에서 멀리): 휠체어 '옆에서' 케이크 상자를 발견했어요."),
  (L(S3, 5).replace('came in', 'came {in|out}'), "정답 ▶ in\n이유: 빵집 주인의 말 → 남자가 가게에 '들어왔다(came in)'"),
  (L(S3, 6).replace("didn't understand", "didn't {understand|remember}"), "정답 ▶ understand (이해하다)\n오답 ▶ remember: 스페인어로 말했는데 '알아듣지 못했다' → 영어만 했으니까요."),
  (L(S3, 9).replace('him clearly', 'him {clearly|badly}'), "정답 ▶ clearly (똑똑히)\n오답 ▶ badly: 그날 케이크를 하나만 팔아서 그를 '똑똑히' 기억해요."),
 ],
 tf=[
  ["The guard found pieces of cake on the painting.", True, "정답 ▶ T\n이유: there were pieces of cake all over the painting", '❸', "there were pieces of cake all over the painting"],
  ["The cake box was from a bakery near the museum.", False, "정답 ▶ F\n이유: 상자는 Camila 빵집의 것이었어요. 박물관 근처라는 말은 없어요.", '❸', "The box was from Camila's Bakery"],
  ["The young man spoke Spanish well.", False, "정답 ▶ F\n이유: 스페인어를 알아듣지 못했고 영어로만 말했어요.", '❸', "He spoke only English"],
  ["The young man bought the smallest cake.", True, "정답 ▶ T\n이유: he just wanted the smallest one", '❸', "he just wanted the smallest one"],
  ["The bakery sold many cakes that day.", False, "정답 ▶ F\n이유: 그날 케이크를 한 개만(only one) 팔았어요.", '❸', "We sold only one cake that day"],
 ],
 ilchi=[
  {'n': '❹', 'box': ['❷', '❸', '❹'], 'q': "Who threw the cake at the Monalisa? (진술과 용의자 정보를 비교해 범인을 고르세요.)",
   'opts': ['Larry Johnson', 'Andres Lozano', 'Tim Baker', 'Luca Ferez'],
   'ex': "정답 ▶ Larry Johnson\n단서 ① 키: 170cm인 Ann보다 '조금' 큼 → 173cm (182cm는 너무 큼, 166cm는 더 작음)\n단서 ② 머리: 회색은 가발, 진짜는 긴 갈색 머리\n단서 ③ 언어: 스페인어를 못하고 영어만 함\n단서 ④ 눈: 파란색\n→ 네 가지가 모두 맞는 사람은 Larry Johnson\n오답 ▶ Andres(검은 머리, 스페인어 함) / Tim(182cm, 초록 눈) / Luca(166cm, 스페인어만)",
   'per': [["범인", ["he was a little taller than me", "He spoke only English", "he had blue eyes"], "173cm · 긴 갈색 머리 · 영어 · 파란 눈"],
           ["", "Andres Lozano | Height: 176 cm", "✘ 검은 머리, 스페인어도 함, 갈색 눈"],
           ["", "Tim Baker | Height: 182 cm", "✘ 너무 큼, 초록 눈"],
           ["", "Luca Ferez | Height: 166 cm", "✘ 170보다 작음, 짧은 회색 머리, 스페인어만"]]},
 ],
 pickg=[
  (L(S3, 1).replace('there were pieces', 'there {were|was} pieces'), "정답 ▶ were\n이유: 주어 pieces of cake(복수) → there were"),
  (L(S3, 6).replace("he didn't understand", "he {didn't|doesn't} understand"), "정답 ▶ didn't\n이유: 과거의 부정 → didn't + 동사원형"),
  (L(S3, 8).replace('the smallest one', 'the {smallest|smaller} one'), "정답 ▶ smallest\n이유: 많은 케이크 중에서 가장 → 최상급 the smallest"),
  (L(S3, 9).replace(', so I', ', {so|but} I'), "정답 ▶ so\n이유: 하나만 팔았다(원인) → 그래서 똑똑히 기억한다(결과) → so"),
  (L(S4, 1).replace('Who threw', 'Who {threw|did throw}'), "정답 ▶ threw\n이유: 의문사 Who가 주어일 때는 do/did 없이 'Who + 동사'로 물어요."),
 ],
 verb=[
  (L(S3, 7).replace('He spoke', 'He ___'), 'speak', ['spoke'], "정답 ▶ spoke\n이유: speak - spoke - spoken (불규칙)"),
  (L(S3, 9).replace('We sold', 'We ___'), 'sell', ['sold'], "정답 ▶ sold\n이유: sell - sold - sold (불규칙)"),
  (L(S3, 8).replace('he just wanted', 'he just ___'), 'want', ['wanted'], "정답 ▶ wanted\n이유: 규칙 변화 want + -ed. 지난 금요일의 일이라 과거형"),
 ],
 error=[
  ("There [[were]] also a wheelchair near the painting, and I found a cake box [[next]] to the [[wheelchair]].", 0, 'was',
   "틀린 곳 ▶ ① were → was\n이유: 주어 a wheelchair(단수) → There was\n나머지 ▶ ② next to ✔ ③ wheelchair ✔"),
  ("I spoke to him [[in]] Spanish, but he [[didn't]] [[understood]] me.", 2, 'understand',
   "틀린 곳 ▶ ③ understood → understand\n이유: didn't + 동사원형\n나머지 ▶ ① in + 언어(~어로) ✔ ② didn't ✔"),
  ("We had a lot of [[different]] cakes, but he just wanted the [[small]] [[one]].", 1, 'smallest',
   "틀린 곳 ▶ ② small → smallest\n이유: the + 최상급 → the smallest one(가장 작은 것)\n나머지 ▶ ① different ✔ ③ one(= cake) ✔"),
  ("Now, [[looks]] at the [[information]] about the [[suspects]].", 0, 'look',
   "틀린 곳 ▶ ① looks → look\n이유: 주어 없이 시작하는 명령문 → 동사원형\n나머지 ▶ ② information ✔ ③ suspects ✔"),
 ],
 scr=[(L(S3, 3), S3[3][1]), (L(S3, 5), S3[5][1]), (L(S4, 0), S4[0][1]), (L(S4, 1), S4[1][1])],
 order=[
  ([L(S3, 1), L(S3, 2), L(S3, 3)], ["범죄 현장, 그림 곳곳에 케이크 조각", "휠체어 옆에서 케이크 상자 발견", "상자는 Camila 빵집 것"]),
  ([L(S3, 5), L(S3, 6), L(S3, 7), L(S3, 8)], ["지난 금요일 젊은 남자가 들어옴", "스페인어를 못 알아들음", "영어만 함", "가장 작은 케이크를 원함"]),
 ],
 insert=[
  ([L(S3, 1), L(S3, 2), L(S3, 3)], 1, ["그림 곳곳에 케이크 조각", "휠체어 옆에서 케이크 상자 발견", "그 상자(The box)는 Camila 빵집 것"],
   "정답 ▶ ①\n이유: The box는 바로 앞의 a cake box를 가리켜요. 상자를 발견한 문장이 먼저 와야 해요."),
  ([L(S3, 8), L(S3, 9), L(S3, 10)], 1, ["가장 작은 케이크를 원함", "한 개만 팔아서 똑똑히 기억함", "아, 파란 눈이었어요"],
   "정답 ▶ ①\n이유: '똑똑히 기억한다'는 말 다음에 기억나는 특징(파란 눈)을 덧붙여요."),
 ],
 odd=[
  ([L(S3, 1), L(S3, 2), "The guard didn't find anything at the crime scene.", L(S3, 3)], 2,
   "정답 ▶ ③\n이유: 경비원은 케이크 조각, 휠체어, 케이크 상자를 발견했어요."),
  ([L(S3, 5), L(S3, 6), "The young man spoke Spanish very well.", L(S3, 7)], 2,
   "정답 ▶ ③\n이유: 그는 스페인어를 이해하지 못하고 영어만 했어요."),
 ],
 blank=[
  (L(S3, 3).replace("Camila's Bakery", "Camila's ____"), ['Bakery', 'Museum', 'School', 'Restaurant'], "정답 ▶ Bakery\n이유: 케이크 상자의 출처 → Camila '빵집'. 다음 진술자도 빵집 주인이에요."),
  (L(S3, 7).replace('only English', 'only ____'), ['English', 'Spanish', 'French', 'Korean'], "정답 ▶ English\n이유: 스페인어를 못 알아듣고 '영어'로만 말했어요. (범인 단서!)"),
  (L(S3, 10).replace('blue eyes', '____ eyes'), ['blue', 'brown', 'green', 'black'], "정답 ▶ blue\n이유: 빵집 주인이 기억한 마지막 단서 = '파란' 눈"),
 ],
 gram=[
  ("밑줄 친 <b>one</b>이 가리키는 것은?<br><b>We had a lot of different cakes, but he just wanted the smallest <u>one</u>.</b>", ['cake', 'man', 'box', 'bakery'],
   "정답 ▶ cake\n이유: one은 앞에 나온 명사(cake)를 반복하지 않으려고 쓴 말이에요. the smallest one = 가장 작은 케이크"),
  ("밑줄 친 <b>so</b>의 뜻으로 알맞은 것은?<br><b>We sold only one cake that day, <u>so</u> I remember him clearly.</b>", ['그래서', '그러나', '왜냐하면', '또는'],
   "정답 ▶ 그래서\n이유: 원인(한 개만 팔았다) → 결과(똑똑히 기억한다)"),
  ("의문문이 바르게 쓰인 것은?", ['Who threw the cake?', 'Who did threw the cake?', 'Who did the cake throw?', 'Who throw did the cake?'],
   "정답 ▶ Who threw the cake?\n이유: 의문사 Who가 주어 → 'Who + 동사(과거형) ~?' (did를 쓰지 않아요)"),
  ("빈칸에 알맞은 것은?<br><b>I spoke to him ______ Spanish.</b>", ['in', 'by', 'on', 'at'],
   "정답 ▶ in\n이유: in + 언어 = ~어로 (in English, in Korean)"),
 ])
SUMQ = '다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 알맞은 것은?'
def SUMSTEP(items):
    return {'type': 'mc', 'title': '요약문 완성', 'guide': '본문을 읽고 요약문의 빈칸 (A), (B)에 들어갈 말을 고르세요.',
            'items': [{'n': n, 'box': box, 'q': SUMQ + '<br><b>' + s + '</b>', 'opts': o, 'ex': x, 'ev': evl} for n, box, s, o, x, evl in items]}
da.append(SUMSTEP([
  ('❷', ['❷'], "The man who threw the cake looked like an old man, but he was actually a (A) ______ man wearing a (B) ______.",
   ['(A) young – (B) wig', '(A) young – (B) hat', '(A) tall – (B) mask', '(A) old – (B) wig', '(A) short – (B) cap'],
   "정답 ▶ (A) young – (B) wig\n(A) 사실 노인이 아니라 '젊은' 남자 → young\n(B) 머리에서 떨어진 것 = '가발' → wig",
   ["He was a young man with long brown hair", "It was his wig"]),
  ('❷', ['❷'], "Ann said the man was a little (A) ______ than 170 cm, and Carlos said the man was (B) ______ than him.",
   ['(A) taller – (B) faster', '(A) shorter – (B) faster', '(A) taller – (B) slower', '(A) shorter – (B) slower', '(A) older – (B) weaker'],
   "정답 ▶ (A) taller – (B) faster\n(A) 170cm인 Ann보다 조금 '더 큼' → taller\n(B) Carlos보다 '더 빨라서' 못 잡음 → faster",
   ["he was a little taller than me", "He was faster than me"]),
]))
db.append(SUMSTEP([
  ('❸', ['❸'], "The owner of Camila's Bakery said a young man who spoke only (A) ______ bought the (B) ______ cake.",
   ['(A) English – (B) smallest', '(A) Spanish – (B) smallest', '(A) English – (B) biggest', '(A) Spanish – (B) biggest', '(A) Korean – (B) sweetest'],
   "정답 ▶ (A) English – (B) smallest\n(A) 스페인어를 못 알아듣고 '영어'만 → English\n(B) '가장 작은' 케이크를 원함 → smallest",
   ["He spoke only English", "he just wanted the smallest one"]),
  ('❹', ['❷', '❸', '❹'], "The criminal was a little taller than 170 cm, had long (A) ______ hair and blue eyes, and spoke only English, so he was (B) ______.",
   ['(A) brown – (B) Larry Johnson', '(A) brown – (B) Tim Baker', '(A) black – (B) Andres Lozano', '(A) gray – (B) Luca Ferez', '(A) black – (B) Larry Johnson'],
   "정답 ▶ (A) brown – (B) Larry Johnson\n(A) 진짜 머리는 긴 '갈색' → brown (회색은 가발)\n(B) 173cm · 긴 갈색 머리 · 영어만 · 파란 눈 → Larry Johnson",
   ["He was a young man with long brown hair", "Larry Johnson | Height: 173 cm"]),
]))

def P(n, rows, sp=None): return [['', n, '']] + [['', a, b] for a, b in rows]
# ── 대화문은 10분 안에 끝나게 쪼갠다 (10/28 선생님 요청): 대화 1~4 / 대화 5 ──
L7 = ['7과 대화 1 · 스포츠 기자', '7과 대화 2 · 요리사', '7과 대화 3 · 작곡가', '7과 대화 4 · 패션 디자이너']
L5 = ['5과 대화 1 · 통화 금지', '5과 대화 2 · 만지기 금지', '5과 대화 3 · 뛰기 금지', '5과 대화 4 · 음식 금지']
c7a, c7b = split(c7, P7, [L7, [M7]])
c5a, c5b = split(c5, P5, [L5, [M5]])
add(c7a, '일치·불일치', MCST, [{'box': L7, 'q': "대화의 내용과 일치하지 <u>않는</u> 것은?",
   'opts': ["Minsu is interested in all kinds of sports.", "David wants to be a sports reporter.", "Hojin is writing a song with a computer program.", "Jacob loves to make clothes.", "Jacob will make clothes for the girl someday."],
   'ex': "정답 ▶ David wants to be a sports reporter.\n이유: 스포츠 기자가 꿈인 사람은 민수예요. David는 세계적으로 유명한 요리사(chef)가 되고 싶어 해요.",
   'per': [["민수는 모든 종류의 스포츠에 관심이 있다.", "I'm interested in all kinds of sports", "일치"],
           ["David는 스포츠 기자가 되고 싶어 한다.", "I want to be a world-famous chef", "불일치 → 요리사"],
           ["호진이는 컴퓨터 프로그램으로 노래를 만들고 있다.", "I'm writing a song with this computer program", "일치"],
           ["Jacob은 옷 만드는 것을 매우 좋아한다.", "I love to make clothes", "일치"],
           ["Jacob은 언젠가 소녀에게 옷을 만들어 줄 것이다.", "I'll make clothes for you someday", "일치"]]}])
add(c7a, '요약문 완성', SUMST, [
  summ([L7[0], L7[1]], "Minsu wants to be a sports (A) ______, and David wants to be a world-famous (B) ______.",
       ['(A) reporter – (B) chef', '(A) chef – (B) reporter', '(A) player – (B) chef', '(A) reporter – (B) songwriter', '(A) designer – (B) pilot'],
       "정답 ▶ (A) reporter – (B) chef\n(A) 민수: 스포츠 '기자' → reporter\n(B) David: 세계적으로 유명한 '요리사' → chef\n오답 ▶ player(선수): 민수는 경기를 많이 보지만 꿈은 기자예요.",
       ["I want to be a sports reporter", "I want to be a world-famous chef"]),
  summ([L7[2], L7[3]], "Hojin is interested in (A) ______ songs, and Jacob loves to (B) ______ clothes.",
       ['(A) writing – (B) make', '(A) singing – (B) make', '(A) writing – (B) buy', '(A) listening – (B) sell', '(A) singing – (B) wear'],
       "정답 ▶ (A) writing – (B) make\n(A) 호진: 노래를 '만드는(작곡하는)' 것 → writing\n(B) Jacob: 옷을 '만드는' 것 → make\n오답 ▶ singing(노래 부르기)이 아니라 writing(작곡)이에요.",
       ["I'm really interested in writing songs", "I love to make clothes"])])
add(c7b, '요약문 완성', SUMST, [
  summ([M7], "Jiho and Lucy will (A) ______ an airplane first, and then they will try (B) ______ one.",
       ['(A) fly – (B) making', '(A) make – (B) flying', '(A) fly – (B) drawing', '(A) buy – (B) selling', '(A) clean – (B) making'],
       "정답 ▶ (A) fly – (B) making\n(A) 먼저 비행기를 '조종'해 보고 → fly\n(B) 그다음 비행기를 '만들어' 본다 → try making\n포인트 ▶ and then(그런 다음에) 앞이 먼저, 뒤가 나중!",
       ["Let's fly this airplane, and then we can try making an airplane, too"])])
add(c5a, '일치·불일치', MCST, [{'box': L5, 'q': "대화의 내용과 일치하지 <u>않는</u> 것은?",
   'opts': ["Texting is OK there.", "The girl must not touch the golden bear.", "The boy may go to the video room.", "Visitors may bring any food into the museum.", "Bottled water is OK in the museum."],
   'ex': "정답 ▶ Visitors may bring any food into the museum.\n이유: 어떤 음식도 가지고 들어오면 안 돼요(must not bring any food). 병에 든 물만 괜찮아요.",
   'per': [["그곳에서 문자하는 것은 괜찮다.", "Texting is OK", "일치"],
           ["소녀는 황금 곰을 만지면 안 된다.", "You must not touch anything in this room", "일치"],
           ["소년은 비디오방에 가도 된다.", "Of course, but don't run", "일치"],
           ["방문객은 어떤 음식이든 박물관에 가져와도 된다.", "You must not bring any food inside", "불일치"],
           ["박물관에서 병에 든 물은 괜찮다.", "Only bottled water is OK", "일치"]]}])
add(c5a, '요약문 완성', SUMST, [
  summ([L5[0]], "The boy must not (A) ______ on the phone there, but (B) ______ is OK.",
       ['(A) talk – (B) texting', '(A) text – (B) talking', '(A) talk – (B) running', '(A) play – (B) eating', '(A) sing – (B) texting'],
       "정답 ▶ (A) talk – (B) texting\n(A) '통화하면' 안 된다 → talk on the phone\n(B) '문자하는 것'은 괜찮다 → texting\n오답 ▶ ②는 반대로 바꾼 함정이에요.",
       ["you must not talk on the phone here", "Texting is OK"]),
  summ([L5[2], L5[3]], "Inside the museum, you must not (A) ______ or bring any food, but (B) ______ water is OK.",
       ['(A) run – (B) bottled', '(A) walk – (B) bottled', '(A) run – (B) hot', '(A) sit – (B) cold', '(A) talk – (B) any'],
       "정답 ▶ (A) run – (B) bottled\n(A) 박물관 안에서 '뛰면' 안 된다 → run\n(B) '병에 든' 물만 괜찮다 → bottled",
       ["You must not run inside the museum", "Only bottled water is OK"])])
add(c5b, '요약문 완성', SUMST, [
  summ([M5], "The girl must not use the flash because it can (A) ______ paintings, and next they will (B) ______ on to Monet's paintings.",
       ['(A) damage – (B) move', '(A) clean – (B) move', '(A) damage – (B) look', '(A) protect – (B) go', '(A) paint – (B) move'],
       "정답 ▶ (A) damage – (B) move\n(A) 플래시는 그림을 '훼손할' 수 있다 → damage\n(B) 모네의 그림으로 '이동한다' → move on to\n오답 ▶ protect(보호하다)는 반대 뜻이에요.",
       ["using the flash can damage paintings", "we'll move on to Monet's paintings next"])])
C7A = {'id': 'c7a', 'name': 'DAY', 'range': '7과 대화문 ① 대화 1~4', 'story': 'Lesson 7 · 관심과 장래 희망 묻고 답하기 · 대화 1~4', 'passage': sub(P7, L7), 'steps': c7a}
C7B = {'id': 'c7b', 'name': 'DAY', 'range': '7과 대화문 ② 대화 5', 'story': 'Lesson 7 · 비행기 체험 (Watch, Answer, and Talk)', 'passage': sub(P7, [M7]), 'steps': c7b}
C5A = {'id': 'c5a', 'name': 'DAY', 'range': '5과 대화문 ① 대화 1~4', 'story': 'Lesson 5 · 허락 구하기 · 금지하기 · 대화 1~4', 'passage': sub(P5, L5), 'steps': c5a}
C5B = {'id': 'c5b', 'name': 'DAY', 'range': '5과 대화문 ② 대화 5', 'story': 'Lesson 5 · 미술관에서 (Watch, Answer, and Talk)', 'passage': sub(P5, [M5]), 'steps': c5b}
L5A = {'id': 'L5a', 'name': 'DAY', 'range': '5과 본문 ❶❷', 'story': 'Lesson 5 · 모나리자에 케이크를 던진 사람 · 목격자 진술 1', 'passage': P('❶', S1) + P('❷', S2), 'steps': da}
L5B = {'id': 'L5b', 'name': 'DAY', 'range': '5과 본문 ❸❹', 'story': 'Lesson 5 · 목격자 진술 2 · 용의자 정보와 범인 찾기', 'passage': P('❸', S3) + P('❹', S4), 'steps': db}

# ═════════════ 6과 대화문 (Watch and Choose 1~4 / Watch, Answer, and Talk) ═════════════
def S6(box, s, o, x, ev): return (None, box, s, o, x, ev)
E1 = [('W', "Excuse me, but can you please close the door? The air conditioner is on.", "실례지만, 문을 닫아 주시겠어요? 에어컨이 켜져 있어서요."),
      ('B', "Oh, I didn't know that. I'll close it right away.", "아, 몰랐네요. 즉시 닫을게요."), ('W', "Thanks.", "감사합니다.")]
E2 = [('M', "For here or to go?", "여기에서 드실 건가요, 아니면 가져가실 건가요?"),
      ('G', "For here, please. And can you please put my smoothie in a plastic cup, not in a glass?", "여기서 먹고 갈게요. 그리고 제 스무디를 유리잔 말고 플라스틱 컵에 담아 주시겠어요?"),
      ('M', "I'm sorry, but we don't use single-use plastic cups inside the café.", "죄송하지만, 카페 안에서는 일회용 플라스틱 컵을 사용하지 않아요."), ('G', "Oh, I see.", "아, 그렇군요.")]
E3 = [('W', "Look. Somebody forgot to turn off the water.", "봐. 누군가 물을 잠그는 걸 깜빡했네."), ('B', "Again? People are so forgetful.", "또요? 사람들은 너무 잘 잊어요."),
      ('W', "I know. Can you run over there and turn off the water?", "그러게. 저기로 뛰어가서 물을 잠가 주겠니?"), ('B', "Sure. No problem.", "물론이죠. 문제없어요.")]
E4 = [('M', "Can you please carry this box to my car?", "이 상자를 내 차로 옮겨 줄래?"), ('G', "I'm really sorry, Dad, but I'm late for my class.", "정말 죄송해요, 아빠, 그런데 제가 수업에 늦었어요."),
      ('M', "Oh, I see. I'll ask somebody else.", "아, 그렇구나. 다른 사람에게 부탁할게.")]
L6 = ['6과 대화 1 · 문 닫기 (Watch and Choose)', '6과 대화 2 · 카페에서 (Watch and Choose)', '6과 대화 3 · 물 잠그기 (Watch and Choose)', '6과 대화 4 · 상자 옮기기 (Watch and Choose)']
P6a = dlg(L6[0], E1) + dlg(L6[1], E2) + dlg(L6[2], E3) + dlg(L6[3], E4)
c6a = build(
 vocab=[['Can you please ~?', '~해 주시겠어요? (도움 요청)'], ['close', '닫다'], ['air conditioner', '에어컨'], ['be on', '켜져 있다'], ['right away', '즉시, 바로'],
        ['For here or to go?', '여기서 드세요, 가져가세요?'], ['plastic cup', '플라스틱 컵'], ['glass', '유리잔'], ['single-use', '일회용의'], ['inside', '~ 안에서'],
        ['forget to', '~할 것을 잊다 (forget - forgot - forgotten)'], ['turn off', '(물·전기를) 잠그다, 끄다'], ['forgetful', '잘 잊어버리는'], ['No problem.', '문제없어요.'],
        ['carry', '옮기다, 나르다'], ['be late for', '~에 늦다'], ['somebody else', '다른 누군가']],
 pickv=[
  (T(E1, 0).replace('is on', 'is {on|off}'), "정답 ▶ on (켜져 있는)\n오답 ▶ off (꺼져 있는): 에어컨이 '켜져 있어서' 찬 바람이 나가지 않게 문을 닫아 달라고 해요."),
  (T(E3, 0).replace('turn off the water', 'turn {off|on} the water'), "정답 ▶ off\n오답 ▶ on: 누군가 물을 '잠그는(turn off)' 것을 깜빡해서 물이 계속 나오고 있어요."),
  (T(E3, 1).replace('so forgetful', 'so {forgetful|careful}'), "정답 ▶ forgetful (잘 잊어버리는)\n오답 ▶ careful (조심성 있는): 물 잠그는 걸 또(Again?) 잊었으니 '잘 잊어버린다'"),
 ],
 tf=[
  ("The woman asks the boy to open the door.", False, "정답 ▶ F\n이유: 문을 여는 게 아니라 닫아(close the door) 달라고 했어요.", None, "can you please close the door"),
  ("The girl will eat at the café.", True, "정답 ▶ T\n이유: For here, please. → 가게 안에서 먹고 가요.", None, "For here, please"),
  ("The café uses single-use plastic cups inside.", False, "정답 ▶ F\n이유: 카페 안에서는 일회용 플라스틱 컵을 쓰지 않아요(don't use).", None, "we don't use single-use plastic cups inside the café"),
  ("The boy will turn off the water.", True, "정답 ▶ T\n이유: 물을 잠가 달라는 부탁에 Sure. No problem.이라고 했어요.", None, "Can you run over there and turn off the water"),
  ("The girl will carry the box for her dad.", False, "정답 ▶ F\n이유: 수업에 늦어서 거절했고, 아빠는 다른 사람에게 부탁할 거예요.", None, "I'm late for my class"),
 ],
 resp=[
  ("A: Can you please close the door?", ['Sure. No problem.', 'For here, please.', "You're welcome.", 'Yes, I did.'],
   "정답 ▶ Sure. No problem.\n이유: 도움 요청(Can you please ~?)을 들어줄 때 → Sure. No problem. / 거절할 때 → I'm sorry, but I can't."),
  ("A: For here or to go?", ['For here, please.', 'Sure. No problem.', "I'll ask somebody else.", 'Thanks.'],
   "정답 ▶ For here, please.\n이유: '여기서 드세요, 가져가세요?' → For here.(여기서요) / To go.(가져갈게요)"),
 ],
 ilchi=[{'box': L6, 'q': "대화의 내용과 일치하지 <u>않는</u> 것은?",
   'opts': ["The air conditioner is on.", "The girl wants her smoothie in a plastic cup.", "Somebody forgot to turn off the water.", "The boy thinks people are forgetful.", "The girl helps her dad carry the box."],
   'ex': "정답 ▶ The girl helps her dad carry the box.\n이유: 소녀는 수업에 늦어서 도와드릴 수 없다고 했어요(I'm really sorry, Dad, but ~).",
   'per': [["에어컨이 켜져 있다.", "The air conditioner is on", "일치"],
           ["소녀는 스무디를 플라스틱 컵에 담기를 원한다.", "can you please put my smoothie in a plastic cup", "일치"],
           ["누군가 물 잠그는 것을 잊었다.", "Somebody forgot to turn off the water", "일치"],
           ["소년은 사람들이 잘 잊어버린다고 생각한다.", "People are so forgetful", "일치"],
           ["소녀는 아빠가 상자 옮기는 것을 돕는다.", "I'm late for my class", "불일치 → 거절함"]]}],
 pickg=[
  (T(E3, 0).replace('forgot to turn', 'forgot {to turn|turning}'), "정답 ▶ to turn\n이유: forget to + 동사원형 = (앞으로) ~할 것을 잊다. 물을 잠가야 하는데 잊어버렸어요."),
  (T(E1, 1).replace("I'll close it", "I'll close {it|them}"), "정답 ▶ it\n이유: 가리키는 것은 the door(단수) → it"),
  (T(E3, 2).replace('and turn off', 'and {turn|turned} off'), "정답 ▶ turn\n이유: Can you + 동사원형 ~? run과 turn이 and로 나란히 연결돼요."),
  (T(E4, 1).replace('late for my class', 'late {for|of} my class'), "정답 ▶ for\n이유: be late for ~ = ~에 늦다 (짝꿍 전치사 for)"),
 ],
 scr=[(T(E4, 0), E4[0][2]), (T(E2, 2), E2[2][2])],
 order=[([T(E3, i) for i in range(4)], ["W: 누군가 물 잠그는 걸 잊었네", "B: 또요? 사람들은 너무 잘 잊어요", "W: 뛰어가서 물 좀 잠가 줄래?", "B: 물론이죠"])],
 blank=[
  (T(E1, 0).replace('is on', 'is ____'), ['on', 'off', 'small', 'cheap'], "정답 ▶ on\n이유: 에어컨이 '켜져 있어서' 문을 닫아 달라는 거예요. 꺼져 있으면(off) 닫을 이유가 없어요."),
  (T(E4, 1).replace("I'm late", "I'm ____"), ['late', 'early', 'ready', 'happy'], "정답 ▶ late\n이유: 부탁을 거절하는 이유 → 수업에 '늦었다(late)'"),
 ],
 awk=[(['A: Can you please help me? B: Sure. No problem.', "A: Can you carry this box? B: I'm sorry, but I can't. I'm busy now.", 'A: For here or to go? B: To go, please.', 'A: Can you please close the window? B: Yes, I did.'],
       "정답 ▶ A: Can you please close the window? B: Yes, I did.\n이유: 도움 요청에는 Sure. No problem. / I'm sorry, but I can't.로 답해요. Yes, I did.는 Did you ~?의 대답이에요.")],
 func=[
  ("도움을 요청하는 표현이 <b>아닌</b> 것은?", ["I'm sorry, but I can't.", 'Can you please close the door?', 'Can you do me a favor?', 'I need a favor.'],
   "정답 ▶ I'm sorry, but I can't.\n이유: 요청을 '거절'하는 말이에요. 나머지는 모두 도움을 요청하는 표현이에요."),
  ("요청을 거절하며 이유를 말하는 것은?", ["I'm sorry, but I can't. I'm busy now.", 'Sure. No problem.', 'Of course, I can.', "I'll close it right away."],
   "정답 ▶ I'm sorry, but I can't. I'm busy now.\n이유: 거절(I'm sorry, but I can't.) + 이유(I'm busy now.)\n오답 ▶ 나머지는 모두 들어주는 말"),
 ],
 summ=[
  S6([L6[0], L6[1]], "The woman asked the boy to (A) ______ the door, and the café doesn't use single-use plastic (B) ______ inside.",
    ['(A) close – (B) cups', '(A) open – (B) cups', '(A) close – (B) bags', '(A) paint – (B) straws', '(A) open – (B) glasses'],
    "정답 ▶ (A) close – (B) cups\n(A) 문을 '닫아' 달라 → close\n(B) 일회용 플라스틱 '컵'을 쓰지 않는다 → cups",
    ["can you please close the door", "we don't use single-use plastic cups inside the café"]),
  S6([L6[2], L6[3]], "The boy agreed to turn off the water, but the girl couldn't carry the box because she was (A) ______ for her class, so her dad will ask somebody (B) ______.",
    ['(A) late – (B) else', '(A) early – (B) else', '(A) late – (B) first', '(A) ready – (B) again', '(A) busy – (B) never'],
    "정답 ▶ (A) late – (B) else\n(A) 수업에 '늦어서' 거절 → late\n(B) '다른' 사람에게 부탁하겠다 → somebody else",
    ["I'm late for my class", "I'll ask somebody else"])],
)
E5 = [('Alex', "Hi, Yuna. What are you doing here?", "안녕, 유나야. 여기에서 뭐 하고 있니?"), ('Yuna', "Hi, Alex. I'm plogging with my club members.", "안녕, Alex. 동아리 회원들과 플로깅을 하고 있어."),
      ('Alex', "Excuse me?", "뭐라고?"), ('Yuna', "Plogging. It means jogging and picking up trash at the same time.", "플로깅. 조깅과 쓰레기 줍기를 동시에 한다는 뜻이야."),
      ('Alex', "Sounds cool! So you're a member of a plogging club.", "멋지다! 그럼 너는 플로깅 동아리의 회원이구나."),
      ('Yuna', "Yes. We plog together every Saturday morning from 10 to 12. Interested?", "응. 우리는 매주 토요일 아침 10시부터 12시까지 함께 플로깅을 해. 관심 있니?"),
      ('Alex', "Well, I'll think about it.", "음, 생각해 볼게."), ('Yuna', "OK. By the way, can you please help me with this trash bag? It's heavy.", "알겠어. 그런데, 이 쓰레기봉투 드는 것 좀 도와줄래? 무거워."),
      ('Alex', "Sure. No problem.", "물론이지. 문제없어.")]
M6 = '6과 대화 5 · 플로깅 (Watch, Answer, and Talk)'
P6b = dlg(M6, E5)
c6b = build(
 vocab=[['club member', '동아리 회원'], ['plog', '플로깅하다 (조깅하며 쓰레기 줍기)'], ['Excuse me?', '뭐라고? (되묻기)'], ['mean', '의미하다'], ['jog', '조깅하다'],
        ['pick up', '줍다'], ['trash', '쓰레기'], ['at the same time', '동시에'], ['Sounds cool!', '멋지다!'], ['every Saturday', '매주 토요일'],
        ['Interested?', '관심 있니?'], ['think about', '~에 대해 생각하다'], ['by the way', '그런데 (화제 바꾸기)'], ['help A with B', 'A가 B 하는 것을 돕다'],
        ['trash bag', '쓰레기봉투'], ['heavy', '무거운']],
 pickv=[
  (T(E5, 3).replace('picking up trash', 'picking up {trash|flowers}'), "정답 ▶ trash (쓰레기)\n오답 ▶ flowers: 플로깅 = 조깅 + '쓰레기' 줍기. 나중에 쓰레기봉투도 나와요."),
  (T(E5, 7).replace("It's heavy", "It's {heavy|light}"), "정답 ▶ heavy (무거운)\n오답 ▶ light (가벼운): 도와 달라고 하는 이유 → 봉투가 '무거워서'"),
  (T(E5, 6).replace("I'll think", "I'll {think|forget}"), "정답 ▶ think\n오답 ▶ forget: 관심 있냐는 말에 바로 답하지 않고 '생각해 볼게'라고 해요."),
 ],
 tf=[
  ("Yuna is plogging alone.", False, "정답 ▶ F\n이유: 혼자가 아니라 동아리 회원들(my club members)과 하고 있어요.", None, "I'm plogging with my club members"),
  ("Plogging means jogging and picking up trash at the same time.", True, "정답 ▶ T\n이유: It means jogging and picking up trash at the same time.", None, "It means jogging and picking up trash at the same time"),
  ("Yuna's club plogs every Sunday.", False, "정답 ▶ F\n이유: 일요일이 아니라 매주 토요일(every Saturday) 아침이에요.", None, "We plog together every Saturday morning from 10 to 12"),
  ("Alex joins the club right away.", False, "정답 ▶ F\n이유: 바로 가입하지 않고 생각해 보겠다(I'll think about it)고 했어요.", None, "Well, I'll think about it"),
  ("Alex will help Yuna with the trash bag.", True, "정답 ▶ T\n이유: Sure. No problem.", None, "can you please help me with this trash bag"),
 ],
 resp=[
  ("A: Can you please help me with this trash bag? It's heavy.", ['Sure. No problem.', 'Excuse me?', 'Sounds cool!', 'For here, please.'],
   "정답 ▶ Sure. No problem.\n이유: 도움 요청을 들어주는 말 → Sure. No problem."),
  ("A: We plog every Saturday. Interested?", ["Well, I'll think about it.", 'For here, please.', "It's heavy.", "I'm sorry to hear that."],
   "정답 ▶ Well, I'll think about it.\n이유: 관심 있냐는 제안에 바로 답하지 않을 때 → I'll think about it.(생각해 볼게)"),
 ],
 ilchi=[
  {'box': [M6], 'q': "대화의 내용과 일치하지 <u>않는</u> 것은?",
   'opts': ["Yuna is plogging with her club members.", "Plogging is jogging and picking up trash.", "The club plogs from 10 to 12.", "Alex is already a member of the plogging club.", "The trash bag is heavy."],
   'ex': "정답 ▶ Alex is already a member of the plogging club.\n이유: 동아리 회원은 유나예요. Alex는 생각해 보겠다고만 했어요.",
   'per': [["유나는 동아리 회원들과 플로깅을 하고 있다.", "I'm plogging with my club members", "일치"],
           ["플로깅은 조깅하면서 쓰레기를 줍는 것이다.", "It means jogging and picking up trash at the same time", "일치"],
           ["동아리는 10시부터 12시까지 플로깅을 한다.", "from 10 to 12", "일치"],
           ["Alex는 이미 플로깅 동아리 회원이다.", ["So you're a member of a plogging club", "I'll think about it"], "불일치 → 회원은 유나"],
           ["쓰레기봉투는 무겁다.", "It's heavy", "일치"]]},
  {'box': [M6], 'q': "Alex가 대화 직후에 유나를 위해 할 일로 알맞은 것은?",
   'opts': ['쓰레기봉투 드는 것 도와주기', '플로깅 동아리에 가입하기', '함께 조깅하기', '포스터 만들기', '물 잠그기'],
   'ex': "정답 ▶ 쓰레기봉투 드는 것 도와주기\n이유: can you please help me with this trash bag? → Sure. No problem.\n오답 ▶ 동아리 가입은 '생각해 볼게'라고만 했어요.",
   'per': [["", "can you please help me with this trash bag", "정답"], ["", "I'll think about it", "✘ 아직 생각 중"], ["", "", "✘"], ["", "", "✘"], ["", "", "✘"]]},
 ],
 pickg=[
  (T(E5, 3).replace('means jogging', 'means {jogging|jog}'), "정답 ▶ jogging\n이유: means의 목적어 자리 → 동명사(-ing). jogging과 picking up이 and로 나란히 연결돼요."),
  (T(E5, 5).replace('every Saturday morning', 'every {Saturday|Saturdays} morning'), "정답 ▶ Saturday\n이유: every + 단수 명사 (매주 토요일 = every Saturday = on Saturdays)"),
  (T(E5, 7).replace("It's heavy", "It's {heavy|heavily}"), "정답 ▶ heavy\n이유: be동사 뒤에서 주어를 설명 → 형용사 heavy. heavily는 부사예요."),
  (T(E5, 7).replace('please help me', 'please {help|helping} me'), "정답 ▶ help\n이유: Can you (please) + 동사원형 ~? = ~해 주겠니? (도움 요청)"),
 ],
 scr=[(T(E5, 3).split('. ')[1], "조깅과 쓰레기 줍기를 동시에 한다는 뜻이야."), (T(E5, 6), E5[6][2])],
 order=[([T(E5, i) for i in range(4)], ["Alex: 여기서 뭐 하고 있니?", "Yuna: 동아리 회원들과 플로깅 중", "Alex: 뭐라고?", "Yuna: 조깅하며 쓰레기 줍기라는 뜻이야"])],
 blank=[
  (T(E5, 5).replace('every Saturday', 'every ____'), ['Saturday', 'Sunday', 'Monday', 'Friday'], "정답 ▶ Saturday\n이유: 매주 '토요일' 아침 10시부터 12시까지 플로깅을 해요."),
  (T(E5, 4).replace('a member of', 'a ____ of'), ['member', 'teacher', 'doctor', 'driver'], "정답 ▶ member\n이유: 유나는 동아리 회원들과 플로깅 중 → 플로깅 동아리의 '회원'"),
 ],
 awk=[(["A: What are you doing here? B: I'm plogging.", "A: Interested? B: Well, I'll think about it.", "A: Can you help me? B: Sure. No problem.", "A: Can you help me with this bag? B: Yes, please."],
       "정답 ▶ A: Can you help me with this bag? B: Yes, please.\n이유: Yes, please.는 무언가를 권할 때 받는 말이에요. 도움 요청에는 Sure. No problem.으로 답해요.")],
 func=[("밑줄 친 말과 바꿔 쓸 수 있는 것은?<br><b>Alex: <u>Excuse me?</u></b>", ['Can you say that again?', "I'm sorry, but I can't.", 'Thank you.', 'Here you are.'],
        "정답 ▶ Can you say that again?\n이유: 여기서 Excuse me?는 잘 못 알아듣고 '뭐라고?' 하고 되묻는 말이에요. = Sorry? / Can you say that again?")],
 summ=[
  S6([M6], "Yuna's club goes plogging, which means jogging and picking up (A) ______, and Alex will think about (B) ______ the club.",
    ['(A) trash – (B) joining', '(A) flowers – (B) joining', '(A) trash – (B) leaving', '(A) friends – (B) closing', '(A) bottles – (B) selling'],
    "정답 ▶ (A) trash – (B) joining\n(A) 조깅하며 '쓰레기' 줍기 → trash\n(B) 동아리에 '가입하는' 것을 생각해 본다 → joining",
    ["It means jogging and picking up trash at the same time", "Well, I'll think about it"]),
  S6([M6], "At the end, Yuna asks Alex for (A) ______ with the trash bag because it is (B) ______.",
    ['(A) help – (B) heavy', '(A) help – (B) light', '(A) money – (B) heavy', '(A) a picture – (B) dirty', '(A) advice – (B) empty'],
    "정답 ▶ (A) help – (B) heavy\n(A) 쓰레기봉투 드는 것을 '도와' 달라 → help\n(B) 봉투가 '무거워서' → heavy",
    ["can you please help me with this trash bag", "It's heavy"])],
)
C6A = {'id': 'c6a', 'name': 'DAY', 'range': '6과 대화문 ① 대화 1~4', 'story': 'Lesson 6 · 도움 요청하고 답하기 · 거절의 이유 말하기 · 대화 1~4', 'passage': P6a, 'steps': c6a}
C6B = {'id': 'c6b', 'name': 'DAY', 'range': '6과 대화문 ② 대화 5', 'story': 'Lesson 6 · 플로깅 (Watch, Answer, and Talk)', 'passage': P6b, 'steps': c6b}

path = '/home/claude/proj/data/m1-donga-yoon-L6.js'
PK = json.loads(subprocess.check_output(['node', '-e', "global.window={};require('%s');process.stdout.write(JSON.stringify(window.PKG))" % path]))
by = {d['id']: d for d in PK['days']}
assert set(by) >= {'d1', 'd2', 'd3', 'd4'}, list(by)
order = [C6A, C6B, by['d1'], by['d2'], C7A, C7B, by['d3'], by['d4'], C5A, C5B, L5A, L5B]
for i, d in enumerate(order): d['name'] = 'DAY %d' % (i + 1)
PK['days'] = order
PK['unit'] = 'Lesson 5~7'
PK['title'] = 'Zero-Waste Challenge · Let’s Make a Movie! · Who Threw a Cake at the Monalisa?'
PK['titleKo'] = '제로 웨이스트 챌린지 · 영화 만들기 · 모나리자 케이크 사건'
PK.pop('startAt', None)
PK['skip'] = ['d1', 'd2']  # 6과 본문은 이미 함(선생님 지정). 6과 대화문은 새로 추가돼서 해야 함
PK['pick'] = True
write(PK, path, "/* 중1 동아(윤정미) Lesson 5~7 (시험 범위 5·6·7과, 8과 제외 10/28). 순서: 6과 → 7과(대화문·본문) → 5과(대화문·본문)\n"
      "   6·7과 본문: 예전 파일(id d1~d4 유지) · 7과·5과 대화문, 5과 본문: scratchpad/gen_m1d5.py · skip d1,d2 = 6과 본문은 이미 함(건너뜀 표시)\n"
      "   prose: true → 본문을 설명문으로 표시(대화문은 화자 표시) */\n")
print('ok', [(d['id'], d['name'], d['range'], len(d['steps'])) for d in PK['days']])
