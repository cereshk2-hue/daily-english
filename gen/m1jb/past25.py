# 11/28 중산중1 작년(2025학년도 2학기 2차) 기출 형식 그대로 → 올해 범위 5·6·7과 모의고사 25문항 (선택형 23 90점 + 논술형 2 10점) → /* M1JBG25-TESTS */ m1jb-g25
# 원본 스캔 work_src/jsg/past.pdf. 작년은 4과(제주 대화·동명사·여행글 Ronda/Chefchaouen/Purple Island)가 섞여 있어 → 1·2·6·8·9·10번은 5~7과로 바꾸고,
# 나머지도 같은 번호·같은 유형·같은 배점으로 새로 씀(학교 시험지 무단 복제 금지 문구가 있어 그대로 옮기지 않음). 종이 시험지 + 앱 OMR(논술형은 입력칸), kind exam + retry 1
import json, re
from collections import Counter
path = '/home/claude/proj/data/m1-donga-yoon-L6.js'
W = lambda *ps: '<div class="wbox">' + ''.join('<p>%s</p>' % p for p in ps) + '</div>'
def CTX(h, *ps): return '<div class="ctx-h">%s</div>' % h + ''.join('<p>%s</p>' % p for p in ps)
D12 = CTX('[1-2] 다음 대화를 읽고 물음에 답하시오.', 'Guide: Everybody, look over here, please. This is <i>Sunflowers</i> by Van Gogh.', 'Mina: Wow, this is my favorite painting. May I take a picture of it?',
          'Guide: Yes, you may, but ________(A)________.', "Mina: Why not? It's a little dark in here.", "Guide: I'm sorry, but using the flash can damage paintings.", "Mina: Oh, I didn't know that.",
          "Guide: Everyone, we'll move on to Monet's paintings next.", 'Mina: Great!')
D45 = CTX('[4-5] 다음 대화를 읽고 물음에 답하시오.', 'Alex: Hi, Yuna. What are you doing here?', "Yuna: Hi, Alex. I'm plogging with my club members.", 'Alex: Excuse me?',
          'Yuna: Plogging. It means jogging and picking up trash at the same time.', "Alex: Sounds cool! So you're a member of a plogging club.",
          'Yuna: Yes. We plog together every Saturday morning from 10 to 12. Interested?', "Alex: Well, I'll think about it.",
          "Yuna: OK. By the way, can you please help me with this trash bag? It's heavy.", 'Alex: Sure. No problem.')
D1415 = CTX('[14-15] 다음을 읽고 물음에 답하시오.', 'Last Saturday, someone threw a cake at the <i>Monalisa</i> in the Botero Museum in Bogota, Colombia. There were four eyewitnesses. What did they say? Read the following, and find the criminal.',
            '<b>Ann Jones, a visitor</b>', "I was looking at the <i>Monalisa</i>, and someone threw a cake at the painting. I turned around and saw an old man. He was standing in front of a wheelchair. I'm about 170 cm tall, and he was a little ⓐ<u>taller</u> than me.",
            '<b>Carlos Diaz, a janitor</b>', "An old man with gray hair was running away, and something ⓑ<u>fall</u> off his head. It was his wig. I ran after him, but I couldn't catch him. He was faster than me. In fact, the old man was not old. He was a young man with long brown hair.",
            '<b>Diego Perez, a guard</b>', "I went to the crime scene, and there ⓒ<u>were</u> pieces of cake all over the painting. There was also a wheelchair near the painting, and I found a cake box next to the wheelchair. The box was from Camila's Bakery.",
            "<b>Camila Santos, the owner of Camila's Bakery</b>", "Last Friday, a young man came in. I spoke to him in Spanish, but he didn't understand me. He spoke only English. We had a lot of different cakes, but he just wanted ⓓ<u>the smallest</u> one. We sold only one cake that day, so I remember him ⓔ<u>clearly</u>. Oh, he had blue eyes.")
D1617 = CTX('[16-17] 다음을 읽고 물음에 답하시오.', "Hi, I'm Jim Brown, the director of <i>Happy Days</i>. It's a movie about the friendship between Tom and his dog Max. A lot of people are working hard ⓐ<u>to create</u> this movie. Do you want ⓑ<u>to meet</u> some of them?",
            "I'm Anna, and I found this beautiful beach. I'm a location manager, and my job is ⓒ<u>to find</u> perfect places for shooting. Of course, it is not easy, but I love my job. I like ⓓ<u>to travel</u> and enjoy challenges.",
            "I'm Peter, the director of photography for this movie. I'm in charge of all the cameras. Today, Tom and Max are going to play together with a ball on the beach. ⓔ<u>To capture</u> their happy moments, I'm going to use drones.")
D1921 = CTX('[19-21, 논술형1] 다음 글을 읽고 물음에 답하시오.', 'Every day, we produce lots of waste, and the Earth is getting sicker and sicker. Do you want to save the Earth? Then, join the zero-waste challenge, and share your stories.',
            '<b>Challenge 01 Reduce Food Waste</b>', 'Olivia: My birthday was last Saturday, and my family and I ate out. There were lots of leftovers, but we ________(A)________. The next day, I made a nice lunch out of them. FYI, you can find great cooking ideas for leftovers on the Internet.',
            '<b>Challenge 02 Reuse</b>', "Domingo: My dog tore my bag. I wanted to buy a new one, but I thought again. I learned that reusing is important for zero-waste living. So, I decided to fix it and reuse it. I'm not very good at sewing, and I don't think that the bag looks perfect. I guess it's all right.",
            '<b>Challenge 03 Say No to Single-Use Plastic</b>', "Emma: I often use food delivery services, but today I didn't. Instead, I walked to my favorite restaurant with a reusable container and picked up the food. I heard that plastic never goes away completely. I didn't use any single-use plastic today. I felt good!",
            '<b>Challenge 04 Recycle</b>', "Minsu: Yesterday, I took some plastic and glass bottles to a recycling machine near my house. I put them into the machine one by one, and I got some points ______(B)______. What can I do with those points? Well, I can use them like money. Don't you think that's cool?")
D2223 = CTX('[22-23, 논술형2] 다음 글을 읽고 물음에 답하시오.', "I'm Jennifer. I trained and ⓐ<u>took</u> care of Max for a long time. Max is a great actor, but he sometimes gets too ⓑ<u>excited</u> when a lot of people are around. So, I use hand signals to calm him. Who am I? I'm an animal wrangler.",
            "My name is Emma, and I'm a film editor. My work ⓒ<u>begins</u> after the shooting is over. To create a better story, I can change the order of scenes or delete some of them. Storytelling skills ⓓ<u>is</u> important for my job, so I read a lot.",
            "I'm Chris, and I'm a Foley artist. I create sound effects in my studio when recording on location is not easy. Listen carefully. Do you hear the sound of waves? I made that sound with rice and a plastic container. Doesn't it ⓔ<u>sound</u> real?")
L5 = ['ⓐ', 'ⓑ', 'ⓒ', 'ⓓ', 'ⓔ']
# (번호, 배점, 출처, 발문, ctx, 본문, 선택지(첫 번째 정답 / ('fix', i)), 해설)
I = [
 (1, 3, '5과 대화', '빈칸 (A)에 들어갈 표현으로 알맞은 것은?', D12, '',
  ['you must not use the flash', 'you must use the flash', "you don't have to take pictures", 'you must not take pictures', 'you may touch the painting'], None,
  "Yes, you may(찍어도 돼요), but ~ + 뒤에서 '플래시는 그림을 손상시킨다' → 플래시를 쓰면 안 된다\n④ 사진은 찍어도 된다고 했으므로 ✘"),
 (2, 3, '5과 대화', '위의 대화 내용과 일치하도록 빈칸 (B)에 들어갈 적절한 말만을 &lt;보기&gt;에서 있는 대로 고른 것은?', D12,
  W('Q: What will Mina do or see at the museum?', 'A: She will ________(B)________.', '&lt;보기&gt;', 'a. look at <i>Sunflowers</i> by Van Gogh', 'b. take a picture with the flash', "c. move on to Monet's paintings", 'd. touch the painting'),
  ['a, c', 'a, b', 'a, b, c', 'a, c, d', 'b, d'], None,
  "a ✓ 해바라기 그림을 봄 c ✓ 다음에 모네의 그림으로 이동\nb 플래시는 금지 d 만진다는 말은 없음(5과: must not touch)"),
 (3, 3, '5·6·7과 대화', '짝지어진 대화 중 자연스럽지 <u>않은</u> 것은?', '', '',
  ["A: You must not run in the hallway.<br>B: Sure. I'll run faster.", 'A: May I eat this sandwich here?<br>B: No, you may not. You must not eat food here.', "A: Can you please close the window?<br>B: I'm sorry, but I'm busy now.",
   'A: Are you interested in cooking?<br>B: Yes, I want to be a chef.', 'A: What do you want to be in the future?<br>B: I want to be a songwriter.'], None,
  "뛰지 말라는 말에 '더 빨리 뛸게'는 어색함 → Sorry. I won't run. 등"),
 (4, 3, '6과 대화', 'Yuna가 Alex에게 부탁한 것으로 알맞은 것은?', D45, '',
  ['쓰레기 봉투 드는 것을 도와주기', '플로깅 동아리에 가입하기', '토요일 아침에 함께 조깅하기', '길에서 쓰레기 줍기', '동아리 회원들을 소개해 주기'], None,
  "can you please help me with this trash bag? It's heavy. → 무거운 쓰레기 봉투를 도와 달라"),
 (5, 3, '6과 대화', '위의 대화의 내용과 일치하는 것은?', D45, '',
  ["Yuna's club plogs every Saturday morning.", 'Alex is already a member of the plogging club.', 'Plogging means walking and picking flowers.', 'Alex decided to join the club right away.', 'The trash bag was very light.'], None,
  "We plog together every Saturday morning ✓\n② Yuna가 회원 ③ jogging and picking up trash ④ I'll think about it(생각해 볼게) ⑤ heavy"),
 (6, 4, '6과 문법', '주어진 우리말과 의미가 통하도록 빈칸 ⓐ, ⓑ에 들어갈 말을 순서대로 바르게 짝지은 것은?', '',
  W('◦ My dream is ⓐ________ space.', '&nbsp;&nbsp;- 나의 꿈은 우주를 여행하는 것이다.', '◦ I think ⓑ________ he is honest.', '&nbsp;&nbsp;- 나는 그가 정직하다고 생각한다.'),
  ['to travel – that', 'travel – that', 'to travel – what', 'traveling – which', 'travels – that'], None,
  "ⓐ be동사 뒤 보어 '~하는 것' → to travel ⓑ think의 목적어절을 이끄는 접속사 that"),
 (7, 3, '6과 대화', '대화의 흐름으로 보아 빈칸 (A)에 들어갈 말로 알맞지 <u>않은</u> 것은?', '',
  W('A: Excuse me, but ________(A)________? The air conditioner is on.', "B: Oh, I didn't know that. I'll close it right away.", 'A: Thanks.'),
  ['why do you close the door', 'can you please close the door', 'could you close the door', 'will you close the door', 'would you close the door'], None,
  "에어컨이 켜져 있으니 문을 닫아 달라는 '요청' → ① '왜 문을 닫니?'는 요청이 아님"),
 (8, 4, '7과 본문', '다음 글의 제목으로 가장 적절한 것은?', '',
  W("Hi, I'm Jim Brown, the director of <i>Happy Days</i>. It's a movie about the friendship between Tom and his dog Max. A lot of people are working hard to create this movie. Do you want to meet some of them?",
    "I'm Anna, and I found this beautiful beach. I'm a location manager, and my job is to find perfect places for shooting. Of course, it is not easy, but I love my job.",
    "I'm Peter, the director of photography for this movie. I'm in charge of all the cameras. To capture their happy moments, I'm going to use drones."),
  ['The People Who Work Hard to Make a Movie', 'How to Train a Dog for a Movie', 'The Most Beautiful Beach in the World', 'Why Drones Are Dangerous', 'The Friendship Between Two Directors'], None,
  "감독이 영화를 만드는 사람들을 소개하고(Do you want to meet some of them?) 장소 섭외 담당·촬영 감독이 자기 일을 설명함"),
 (9, 4, '6과 본문', '글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳은?', '',
  W('So, I decided to fix it and reuse it.', '―――――――――――――――', "Domingo: My dog tore my bag. (A) I wanted to buy a new one, but I thought again. (B) I learned that reusing is important for zero-waste living. (C) I'm not very good at sewing, and I don't think that the bag looks perfect. (D) I guess it's all right. (E)"),
  ['(A)', '(B)', '(C)', '(D)', '(E)'], ('fix', 2),
  "'재사용이 중요하다는 걸 배웠다' → So(그래서) 고쳐서 다시 쓰기로 함 → 바느질을 잘 못해서 완벽해 보이진 않음 → (C)"),
 (10, 4, '6과 본문', '다음 글의 내용과 일치하지 <u>않는</u> 것은?', '',
  W("Emma: I often use food delivery services, but today I didn't. Instead, I walked to my favorite restaurant with a reusable container and picked up the food. I heard that plastic never goes away completely.",
    'Minsu: Yesterday, I took some plastic and glass bottles to a recycling machine near my house. I put them into the machine one by one, and I got some points in return. Well, I can use them like money.'),
  ['Minsu got real money from the recycling machine.', "Emma didn't use food delivery services today.", 'Emma took a reusable container to the restaurant.', 'Minsu took some bottles to a recycling machine.', 'Emma heard that plastic never goes away completely.'], None,
  "기계에서 받은 건 포인트(points) — 돈처럼 쓸 수 있을 뿐 실제 돈이 아님"),
 (11, 4, '5과 문법', '다음 중 어법상 옳지 <u>않은</u> 것은?', '', '',
  ['There was four eyewitnesses.', 'There is a wheelchair near the painting.', 'There were pieces of cake on the floor.', 'Is there a cake box next to the wheelchair?', "There aren't many people in the museum."], None,
  "four eyewitnesses(복수) → There were"),
 (12, 4, '5과 본문', '다음 용의자 정보의 내용과 일치하지 <u>않는</u> 것은?', '',
  W('• Andres Lozano | 176 cm | long, black hair | Spanish, English | brown eyes', '• Larry Johnson | 173 cm | long, brown hair | English | blue eyes', '• Tim Baker | 182 cm | long, brown hair | English | green eyes', '• Luca Ferez | 166 cm | short, gray hair | Spanish | blue eyes'),
  ['Andres Lozano is shorter than Luca Ferez.', 'Andres Lozano speaks two languages.', 'Tim Baker is the tallest of the four.', 'Luca Ferez has short gray hair.', 'Larry Johnson and Luca Ferez have blue eyes.'], None,
  "Andres 176 cm > Luca 166 cm → Andres가 더 큼"),
 (13, 3, '5과 문법', '다음 각 자전거에 대한 설명으로 <u>틀린</u> 것은?', '',
  W('<table class="tb"><tr><th></th><th>Bike A</th><th>Bike B</th><th>Bike C</th><th>Bike D</th></tr><tr><th>Speed</th><td>20 km/h</td><td>25 km/h</td><td>18 km/h</td><td>22 km/h</td></tr><tr><th>Weight</th><td>12 kg</td><td>15 kg</td><td>10 kg</td><td>14 kg</td></tr><tr><th>Price</th><td>$200</td><td>$350</td><td>$150</td><td>$300</td></tr></table>'),
  ['Bike A is slower than Bike C.', 'Bike B is the fastest of the four.', 'Bike C is lighter than Bike A.', 'Bike D is more expensive than Bike A.', 'Bike C is the cheapest of the four.'], None,
  "A 20 km/h > C 18 km/h → A가 더 빠름"),
 (14, 5, '5과 본문', '밑줄 친 ⓐ~ⓔ 중 어법상 옳지 <u>않은</u> 것은?', D1415, '', L5, ('fix', 1),
  "ⓑ 지난 일(was running) → 과거 fell (fall - fell - fallen)\nⓐ 비교급 ⓒ pieces(복수) ⓓ 최상급 ⓔ 동사를 꾸미는 부사"),
 (15, 4, '5과 본문', '윗글의 내용과 일치하지 <u>않는</u> 것은?', D1415, '',
  ['Carlos was faster than the young man.', 'The criminal wore a wig.', "The cake box came from Camila's Bakery.", 'The young man wanted the smallest cake.', 'The young man had blue eyes.'], None,
  "He was faster than me. → 그 남자가 Carlos보다 빨랐음"),
 (16, 5, '7과 본문', '밑줄 친 ⓐ~ⓔ 중 to부정사의 용법이 같은 것끼리 짝지은 것은?', D1617, '',
  ['ⓐ, ⓔ', 'ⓐ, ⓑ', 'ⓑ, ⓔ', 'ⓒ, ⓔ', 'ⓓ, ⓔ'], None,
  "ⓐ 만들기 위해 ⓔ 포착하기 위해 → 둘 다 목적(부사적)\nⓑ want의 목적어 ⓒ be동사 뒤 보어 ⓓ like의 목적어 → 명사적"),
 (17, 4, '7과 본문', '윗글의 내용과 일치하는 것은?', D1617, '',
  ['<i>Happy Days</i> is a movie about Tom and his dog Max.', 'Anna is the director of the movie.', "Anna doesn't like to travel.", 'Peter trains the dog Max.', "Peter won't use drones on the beach."], None,
  "a movie about the friendship between Tom and his dog Max ✓\n② 감독은 Jim Brown ③ I like to travel ④ Peter는 촬영 감독 ⑤ drones를 씀"),
 (18, 5, '5·6·7과 문법', '다음 중 어법상 옳은 것은?', '', '',
  ['My dream is to become a chef.', 'I went to the store to buying milk.', "When she will come, I'll call you.", 'There is many apples in the box.', 'He finished his homework before he watch TV.'], None,
  "be동사 뒤 보어 to부정사 ✓\n② to buy ③ When she comes(시간 부사절 현재) ④ There are ⑤ watched"),
 (19, 4, '6과 본문', '윗글의 주제로 알맞은 것은?', D1921, '',
  ['different ways people practice zero-waste living', 'how to make new bags out of old ones', 'the best restaurants for food delivery', 'why people should buy more plastic bottles', 'how to have a fun birthday party'], None,
  "zero-waste challenge 네 가지(음식물 줄이기·재사용·일회용 플라스틱 안 쓰기·재활용)를 사람들의 예로 보여 줌"),
 (20, 4, '6과 본문', '윗글의 Challenge와 사람이 바르게 연결된 것은?', D1921, '',
  ['Reduce Food Waste – Olivia', 'Reuse – Emma', 'Say No to Single-Use Plastic – Minsu', 'Recycle – Domingo', 'Reuse – Olivia'], None,
  "01 Olivia · 02 Domingo · 03 Emma · 04 Minsu"),
 (21, 5, '6과 본문', '윗글의 내용과 일치하는 것은?', D1921, '',
  ['Olivia made lunch with the leftovers the next day.', 'Olivia cooked dinner at home on her birthday.', 'Domingo bought a new bag.', 'Domingo is very good at sewing.', "Minsu can't use the points he got."], None,
  "The next day, I made a nice lunch out of them. ✓\n② ate out(외식) ③ 새로 사지 않고 고침 ④ not very good at sewing ⑤ 돈처럼 쓸 수 있음"),
 (22, 4, '7과 본문', '윗글의 내용과 일치하는 것은?', D2223, '',
  ['Jennifer uses hand signals to calm Max.', 'Max always stays calm around many people.', "Emma's work begins before the shooting.", "Emma doesn't need storytelling skills.", 'Chris made the sound of waves with sand and a bottle.'], None,
  "So, I use hand signals to calm him. ✓\n② 사람이 많으면 너무 흥분함 ③ after the shooting ④ 중요해서 책을 많이 읽음 ⑤ rice and a plastic container"),
 (23, 5, '7과 본문', '밑줄 친 ⓐ~ⓔ 중 어법상 옳지 <u>않은</u> 것은?', D2223, '', L5, ('fix', 3),
  "ⓓ 주어 Storytelling skills(복수) → are\nⓐ trained와 함께 과거 ⓑ 감정을 느끼는 Max → excited ⓒ My work(단수) → begins ⓔ 감각동사 sound + 형용사"),
]
W1 = {'kind': 'write', 'n': '서술형 1', 'src': '6과 본문 · 논술형1', 'pts': 5, 'ctx': D1921,
      'stem': '윗글의 빈칸 (A), (B)에 들어갈 알맞은 말을 &lt;조건&gt;에 맞게 완성하시오. [총 5점]',
      'body': W('[1-1] There were lots of leftovers, but we ________(A)________. (3단어) [3점]', '&nbsp;&nbsp;- 남은 음식이 많았지만, 우리는 그것들을 집으로 가져왔다.', '[1-2] I got some points ______(B)______. (2단어) [2점]', '&nbsp;&nbsp;- 나는 그 대가로 약간의 포인트를 얻었다.',
                '&lt;조건&gt; • 아래 단어만 사용할 것: bring, them, home, in, return • 필요하면 어형을 바꿀 것'),
      'blanks': [{'label': '(A)', 'pts': 3, 'ans': ['brought them home'], 'chk': []}, {'label': '(B)', 'pts': 2, 'ans': ['in return'], 'chk': []}],
      'model': '(A) brought them home (B) in return', 'ex': "(A) 지난 일 → bring의 과거 brought + them + home\n(B) in return = 그 대가로"}
W2 = {'kind': 'write', 'n': '서술형 2', 'src': '7과 본문 · 논술형2', 'pts': 5, 'ctx': D2223,
      'stem': '윗글을 바탕으로 직업 소개 카드를 완성할 때 빈칸 (A)~(D)에 들어갈 말을 &lt;보기&gt;의 단어만을 모두 한 번씩 사용하여 완성하시오. [5점]',
      'body': W('<table class="tb"><tr><th>animal wrangler</th><td>• train and (A) ____________ for a long time<br>• use hand signals (B) ____________</td></tr><tr><th>film editor</th><td>• change (C) ____________ to create a better story</td></tr><tr><th>Foley artist</th><td>• (D) ____________ in the studio</td></tr></table>',
                '&lt;보기&gt; take / care / of / Max / to / calm / him / the / order / of / scenes / create / sound / effects',
                '(A) 4단어 [1점] (B) 3단어 [1점] (C) 4단어 [2점] (D) 3단어 [1점]'),
      'blanks': [{'label': '(A)', 'pts': 1, 'ans': ['take care of Max'], 'chk': []}, {'label': '(B)', 'pts': 1, 'ans': ['to calm him'], 'chk': []},
                 {'label': '(C)', 'pts': 2, 'ans': ['the order of scenes'], 'chk': []}, {'label': '(D)', 'pts': 1, 'ans': ['create sound effects'], 'chk': []}],
      'model': '(A) take care of Max (B) to calm him (C) the order of scenes (D) create sound effects',
      'ex': "(A) take care of Max(Max를 돌보다) (B) to calm him(그를 진정시키기 위해, 목적) (C) the order of scenes(장면의 순서) (D) create sound effects(음향 효과를 만들다)"}
assert len(I) == 23 and sum(x[1] for x in I) == 90
fixed = Counter(x[7][1] for x in I if isinstance(x[7], tuple))
need = Counter({0: 5, 1: 5, 2: 5, 3: 4, 4: 4})
for k, v in fixed.items(): need[k] -= v
pool = sum([[k] * need[k] for k in range(5)], [])
order = [3, 1, 0, 4, 2, 1, 3, 0, 2, 4, 1, 0, 3, 2, 4, 0, 1, 3, 4, 2, 0, 1, 2]
items = []
for n, pts, src_, stem, ctx, body, opts, ans, ex in [(x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8]) for x in I]:
    if isinstance(ans, tuple): o, a = list(opts), ans[1]
    else:
        a = next(k for k in order[n - 1:] + order + list(range(5)) if k in pool); pool.remove(a)
        o = list(opts); right = o.pop(0); o.insert(a, right)
    assert len(o) == 5 and len(set(o)) == 5, n
    items.append({'n': n, 'src': src_, 'stem': stem + ' [%d점]' % pts, 'body': body, 'opts': o, 'en': True, 'ans': a,
                  'ex': '정답 ▶ %s\n이유 ▶ %s' % ('①②③④⑤'[a], ex), 'ctx': ctx, 'pts': pts, 'words': [], 'kos': []})
W1['words'] = W2['words'] = []; W1['kos'] = W2['kos'] = []
items = items[:21] + [W1] + items[21:23] + [W2]  # 작년 시험지처럼 [19-21, 논술형1] 바로 뒤, [22-23, 논술형2] 바로 뒤 (지문 한 번만 인쇄)
assert sum(i['pts'] for i in items) == 100
T = {'id': 'm1jb-g25', 'kind': 'exam', 'retry': 1, 'title': '작년 기출 형식 모의고사 (5·6·7과) 25문항', 'short': '작년 기출형 5~7과', 'school': '중산중 1학년', 'minutes': 45,
     'note': '작년 2학기 2차 지필평가와 같은 번호·유형·배점(선택형 23 + 논술형 2)으로, 올해 범위 5·6·7과에 맞춰 새로 만든 시험지예요. 문제는 종이로 풀고 여기엔 답만 입력해요.', 'items': items}
src = open(path, encoding='utf-8').read()
src = re.sub(r'/\* M1JBG25-TESTS.*?/\* /M1JBG25-TESTS \*/\n?', '', src, flags=re.S)
src = src.rstrip('\n') + '\n/* M1JBG25-TESTS: gen/m1jb/past25.py 로 만듦 (손으로 고치지 말 것) */\nwindow.PKG.tests = (window.PKG.tests || []).filter(function (t) { return t.id !== "m1jb-g25"; }).concat([%s]);\n/* /M1JBG25-TESTS */\n' % json.dumps(T, ensure_ascii=False)
open(path, 'w', encoding='utf-8').write(src)
print(''.join('①②③④⑤'[i['ans']] for i in items if i.get('kind') != 'write'), Counter(i['ans'] for i in items if i.get('kind') != 'write'))
