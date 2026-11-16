# 11/16 중산중3 2025학년도 2학기 2차 지필평가 영어 (지학사 7·8과) — 선생님이 주신 스캔 PDF 원본 그대로(25문항, 정답 위치·배점 원본)
# 정답(검수): 1② 2③ 3③ 4② 5⑤ 6⑤ 7⑤ 8③ 9⑤ 10④ 11③ 12⑤ 13③ 14① 15① 16④ 17① 18① 19② 20④ 21④ 22④ 23⑤ 24③ 25②
from wu_k25 import *
H = ('2025 기출', '중산중 2025학년도 2학기 2차 지필평가', '중산중 2025 기출', 'k25')
Bx = lambda *ls: BOX('<br>'.join(ls))
N = '작년(2025) 중산중 3학년 2학기 2차 지필평가 영어 원본이에요. 실제 시험처럼 45분 안에 풀고 OMR에 답을 입력하세요.'
T = Test('1', '중산중', '2학기 2차 지필평가 (7·8과)', '중산중 기출', N, H=H)
PET = Bx("Alex: John, what is this graph about?", "John: I did a survey on the kinds of pets my classmates have.", "Alex: What were the results?",
         "John: Eighty percent of the students have pets. Only five out of twenty-five students don't have pets.", "Alex: ________ (A) ________",
         "John: Well, ten students have dogs and three students have cats.", "Alex: What about the rest?", "John: Seven students have fish.")
T.fixed('[1~2] 위 대화의 내용과 일치하는 것은?', '8과', PET,
 ['Five students have fish.', 'Ten students have dogs.', 'Seven students have cats.', "John's classmates all have pets.", "Half of the students don't have pets."], 2,
 "이유 ▶ ten students have dogs ✔\n오답 ▶ ① 물고기는 7명 ③ 고양이는 3명 ④ 80%만 있음 ⑤ 없는 학생은 5명(20%)", [('the rest', '나머지')], 3)
T.fixed('위 글(1번)의 빈칸 (A)에 들어갈 말로 알맞은 것은?', '8과', '',
 ['Why do they have pets?', 'How much do the pets cost?', 'What kind of pets do they have?', 'Where do they mostly keep their pets?', 'How many students participated in the survey?'], 3,
 "이유 ▶ 대답이 '개 10명, 고양이 3명' → 어떤 종류의 애완동물을 기르는지 묻는 말\n오답 ▶ ① 이유 ② 가격 ④ 장소 ⑤ 참가 인원(이미 나옴)", [], 3)
T.fixed('다음 대화에서 Henry가 쓰는 글의 주제로 알맞은 것은?', '8과', Bx(
 "Mina: Henry, what are you doing?", "Henry: I'm writing an article about students' favorite snacks. I'm worried about their health.", "Mina: Why?",
 "Henry: Well, I surveyed 100 students and the results show that eighty percent of the students liked pizza and fried chicken for snacks. Do you see what I mean?",
 "Mina: Oh, I get it. Students really like fast food. What else did they like?", "Henry: Twelve percent of the students chose chocolate cake as their favorite.",
 "Mina: Wow, students should really try to eat healthier snacks!"),
 ["Students' favorite fruits", "Students' favorite sports", "Students' favorite snacks", 'How to cook healthy food', "Students' eating habits at school lunch"], 3,
 "이유 ▶ I'm writing an article about students' favorite snacks.\n오답 ▶ ① 과일 ② 운동 ④ 요리법 ⑤ 급식은 나오지 않음", [('article', '기사, 글')], 3)
T.fixed('다음 글의 제목으로 알맞은 것은?', '7과 응용', Bx(
 "When you visit Korea, you might wonder where you can stay. Why don't you stay in a <i>hanok</i>? A <i>hanok</i> is a traditional Korean house. If you stayed in a <i>hanok</i>, you would sleep on the floor because there are no beds. "
 "<i>Hanok</i> houses are mostly built with natural materials such as wood, stone, straw, paper, and earth. These materials help you keep your skin clean. In the cold winter, the warm <i>ondol</i> floors heat your body. "
 "The doors in <i>hanok</i> are covered with thin paper. They help keep you cool in summer."),
 ['The History of Korean Architecture', 'The Features and Functions of Hanok', 'Why Korean People Sleep on the Floor', 'How to Stay Cool in a Korean Summer', 'How to Make Your Skin Clean Naturally'], 2,
 "이유 ▶ 한옥의 특징(바닥에서 잠, 자연 재료, 온돌, 종이 문)과 기능(피부, 겨울 난방, 여름 시원함)을 소개 → 한옥의 특징과 기능\n오답 ▶ ① 역사 없음 ③④⑤ 글의 일부 내용만", [('material', '재료'), ('feature', '특징')], 3)
PAS = Bx("Pascal was doing his math homework in his room. He was struggling with graphs.",
 "\"It's too hard to read and draw graphs. Why do I need these anyway? No one needs graphs in real life.\" He put down his pen and picked up his favorite book, <i>Robin Hood</i>. He decided to read himself to sleep. When he was about to open the book, he heard a voice. He looked up from the book to see who was talking. He couldn't believe his eyes. It was his dog, Manny, who was talking!",
 "\"Close your eyes and repeat after me. <i>Cogito ergo sum</i>,\" said Manny.", "\"You can talk?\"", "\"Just repeat! <i>Cogito ergo sum</i>.\"",
 "Pascal closed his eyes and repeated the words. Suddenly, he heard men shouting. When he opened his eyes, he saw soldiers on horses. They were chasing a man with arrows in his hand. The man saw Pascal and shouted.",
 "\"It's too dangerous for you to stand there. Come on.\" The man pulled Pascal onto his horse and rode into the woods.", "When they arrived at a house, the man stopped and got off his horse.",
 "\"Hello, my name is Robin Hood.\"", "\"Wow! Are you the Robin Hood from the book?\"", "\"No, I'm the Robin Hood of Sherwood Forest. Who are you and why are you here?\"")
T.fixed('[5~7] 위 글에서 Pascal이 숙제하기를 어려워하는 이유는?', '8과', PAS,
 ["He didn't like writing essays.", 'He forgot to bring his math book.', 'He wanted to walk his dog instead.', "He didn't understand the book because he was not good at English grammar.", 'He found graphs hard to read and difficult to draw, and doubted their practical use.'], 5,
 "이유 ▶ It's too hard to read and draw graphs. Why do I need these anyway? No one needs graphs in real life.\n오답 ▶ ①②③④ 나오지 않음", [('struggle with', '~으로 애를 먹다'), ('practical', '실용적인')], 4)
T.fixed('위 글(5번)에서 Pascal이 "<i>Cogito ergo sum</i>"을 따라 말한 후에 일어난 일은?', '8과', '',
 ['He met his math teacher.', 'He started drawing graphs.', 'He woke up from a dream.', 'He went back to doing his homework.', 'He saw soldiers on horses chasing a man with arrows in his hand.'], 5,
 "이유 ▶ When he opened his eyes, he saw soldiers on horses. They were chasing a man with arrows in his hand.\n오답 ▶ ①②③④ 나오지 않음", [('chase', '뒤쫓다')], 3)
T.fixed('위 글(5번)의 내용과 일치하는 것은?', '8과', '',
 ['Robin saw Manny talking like a human.', 'Soldiers were helping Robin Hood escape.', "Pascal refused to follow Manny's instruction.", 'Manny helped Pascal with his math homework.', 'Pascal met the Robin Hood of Sherwood Forest.'], 5,
 "이유 ▶ I'm the Robin Hood of Sherwood Forest ✔\n오답 ▶ ① Manny가 말하는 걸 본 건 Pascal ② 군인들은 그를 쫓고 있었다 ③ 따라 했다(repeated) ④ 숙제를 돕지 않았다", [('instruction', '지시')], 4)
NDE = Bx("If you walked down a street in the village of the Ndebele in South Africa, you (A) <b>[ saw / would see ]</b> houses with many ⓐ <u>unique</u> patterns and styles. Each house tells a ⓑ <u>different</u> story. Some stories might be about neighbors' babies. Others express ⓒ <u>personal</u> opinions like their feelings or ideas.",
 "A long time ago, the Ndebele were in a terrible war with the Boers. When the Boers ⓓ <u>invaded</u> their land, the Ndebele painted their houses with many colorful symbols. These symbols were known only to the Ndebele people, and they used them to communicate ⓔ <u>publicly</u> with one another. Because of this, their enemies couldn't understand the meaning of their messages. The symbols expressed feelings such as sadness. Those symbols (B) <b>[ handed down / were handed down ]</b> from mothers to daughters. And they have kept their traditions (C) <b>[ alive / live ]</b>.")
T.fixed('[8~9] 위 글의 (A), (B), (C)의 각 네모 안에서 어법에 맞는 표현을 골라 짝지은 것으로 가장 적절한 것은?', '7과 응용', NDE,
 ['saw − were handed down − alive', 'saw − handed down − live', 'would see − were handed down − alive', 'would see − handed down − alive', 'would see − were handed down − live'], 3,
 "이유 ▶ (A) If + 과거(walked) → 주절 would see (가정법 과거) (B) 상징이 '전해진' 것 → 수동태 were handed down (C) keep + 목적어 + 형용사 보어 alive (live는 서술 보어로 못 씀)\n오답 ▶ saw는 가정법 아님 / handed down은 능동 / live ❌", [('hand down', '물려주다'), ('invade', '침략하다')], 5)
T.fixed('위 글(8번)의 밑줄 친 ⓐ~ⓔ 중 문맥상 낱말의 쓰임이 어색한 것은?', '7과 응용', '', ['ⓐ', 'ⓑ', 'ⓒ', 'ⓓ', 'ⓔ'], 5,
 "이유 ▶ 상징은 은데벨레 사람들만 알았고 적들이 의미를 몰랐다 → '공개적으로(publicly)'가 아니라 '몰래(secretly)' 소통했다\n오답 ▶ ⓐ 독특한 ⓑ 다른 ⓒ 개인적인 ⓓ 침략했다 → 모두 자연스러움", [('secretly', '몰래')], 4)
TOW = Bx("\"My name is Pascal. I don't know why I'm here, but there must be a reason. You saved me from the soldiers. Thank you so much. Is there anything I can do for you?\"",
 "\"Well, can you help us get back the money that the king took from the people? He taxed them too much. He is too greedy to share with the people, so they don't have enough money to buy food. I want to help them get their money back. However, there are many soldiers in the tower, so no one can get inside.\"",
 "\"Hmm... I think I have a solution. But first, can you take me to the tower? I need to count the number of soldiers.\"",
 "Robin and Pascal hid up in a tree and they counted the soldiers one by one. After that, Pascal gave Robin a summary of what they found.",
 "\"There are five soldiers from midnight to six in the morning. Next, there are three soldiers until noon, and then there are eight soldiers until six in the evening. Lastly, there are twelve soldiers until midnight. So, you should go inside between six in the morning and noon.\"",
 "\"What? I don't get it.\"", "Pascal thought for a moment. 'Hmm... A graph might make this easier to understand.' Pascal drew a graph and showed it to Robin.")
T.fixed('[10~11] 위 글에서 Pascal이 그래프를 그린 목적은?', '8과', TOW,
 ['to prove a math formula', 'to write down a history event', 'to design an experimental device', 'to look at data and compare it clearly', 'to explain an idea about life or thinking'], 4,
 "이유 ▶ 'A graph might make this easier to understand.' → 시간대별 군인 수(자료)를 한눈에 비교해서 Robin이 이해하게 하려고\n오답 ▶ ① 공식 ② 역사 ③ 실험 장치 ⑤ 삶·생각", [('compare', '비교하다')], 3)
T.fixed('위 글(10번)의 내용과 일치하지 <u>않는</u> 것은?', '8과', '',
 ['Pascal was saved from the soldiers.', 'Pascal counted the soldiers with Robin.', "Robin explained the soldiers' schedule to Pascal.", 'Robin wanted to help people get their money back from the king.', 'Pascal suggested that the best time to go inside the tower is between six in the morning and noon.'], 3,
 "이유 ▶ 군인 일정을 정리해 설명한 사람은 Pascal(Pascal gave Robin a summary) → 주어와 대상이 뒤바뀜\n오답 ▶ ①②④⑤ 본문과 일치", [('summary', '요약')], 4)
T.fixed('주어진 글 다음에 이어질 글의 순서로 가장 적절한 것은?', '8과 응용', Bx(
 "What kinds of numbers are thought to be lucky or unlucky? Do you think it is similar around the world? Usually, the number 7 is a lucky number in countries like England, the USA, and France. However, a lucky number in one country can be unlucky in another.",
 "(A) However, in China, the sound of the word for the number 4 is similar to that of the Chinese word for death. So, the number 4 is regarded as unlucky.",
 "(B) How about the number 4? In Germany, the number 4 is regarded as lucky because it matches the number of leaves on a four-leaf clover.",
 "(C) For example, Chinese people think 7 is unlucky because July or \"the seventh month\" is often thought of as a month for ghosts."),
 ['(A) − (C) − (B)', '(B) − (A) − (C)', '(B) − (C) − (A)', '(C) − (A) − (B)', '(C) − (B) − (A)'], 5,
 "이유 ▶ 한 나라의 행운의 숫자가 다른 나라에선 불운 → (C) 예: 중국의 7 → (B) 그럼 4는? 독일에선 행운 → (A) However, 중국에선 불운\n포인트 ▶ For example은 바로 앞 내용의 예, However는 앞과 반대 내용", [('regard A as B', 'A를 B로 여기다')], 4)
T.fixed('두 사람의 대화가 자연스럽도록 (A)~(D)를 바르게 배열한 것은?', '8과', Bx(
 "Emily: Jimmy, what's the matter? You look upset.", "Jimmy: My brother broke my computer. I'm so angry.",
 "(A) Oh, I get it. I guess it's not good to stay angry for a long time.", "(B) I'm sorry to hear that, but your facial muscles must be tired.",
 "(C) It takes a lot of muscles to look angry, but only a few to smile. Do you see what I mean?", "(D) What do you mean?",
 "Emily: That's right. Remember, it's always better to smile."),
 ['(A) − (B) − (C) − (D)', '(B) − (D) − (A) − (C)', '(B) − (D) − (C) − (A)', '(C) − (A) − (B) − (D)', '(D) − (B) − (A) − (C)'], 3,
 "이유 ▶ Emily (B) 안됐다, 얼굴 근육이 피곤하겠다 → Jimmy (D) 무슨 뜻이야? → Emily (C) 화난 표정엔 근육이 많이 필요해 → Jimmy (A) 알겠다 → Emily That's right.", [('facial', '얼굴의')], 3)
T.fixed('두 사람의 대화가 자연스럽도록 (A)~(E)를 바르게 배열한 것은?', '7과', Bx(
 "Jinho: I think living in a jungle would be really exciting. Don't you think so?", "(A) What would you do if you lived in the jungle?",
 "(B) But there are some dangerous animals in the jungle, Jinho.", "(C) Then where would you sleep? In a cave?", "(D) I know. But the jungle is full of adventure. I wish I could live there.",
 "(E) I would explore it. Maybe I could make some animal friends.", "Jinho: No, I would stay in a tree house. Then I would be safe from dangerous animals.", "Claire: That makes sense."),
 ['(B) − (D) − (A) − (E) − (C)', '(B) − (E) − (A) − (C) − (D)', '(C) − (D) − (B) − (A) − (E)', '(D) − (A) − (E) − (B) − (C)', '(D) − (B) − (A) − (E) − (C)'], 1,
 "이유 ▶ Claire (B) 위험한 동물이 있어 → Jinho (D) 알아, 하지만 모험 → Claire (A) 정글에 살면 뭘 할 거야? → Jinho (E) 탐험 → Claire (C) 어디서 자? 동굴? → Jinho No, tree house", [('explore', '탐험하다')], 4)
T.fixed('다음 문장을 가정법으로 바꾼 것 중 <u>틀린</u> 것은?', '7과', '',
 ["As I don't live in a jungle, I don't build a tree house and live there.<br>→ If I lived in a jungle, I would build a tree house and lived there.",
  "As we don't have much snow this year, we don't go sledding.<br>→ If it snowed a lot this year, we would go sledding.",
  "As I am not good at grammar, I can't answer the question.<br>→ If I were good at grammar, I could answer the question.",
  "As you are shorter than Jane, you can't reach that branch.<br>→ If you weren't shorter than Jane, you could reach that branch.",
  "As you don't do your homework, you won't get perfect grades in the test.<br>→ If you did your homework, you would get perfect grades in the test."], 1,
 "이유 ▶ would build ~ and (would) live → 조동사 뒤라 동사원형 live. lived ❌\n포인트 ▶ 가정법 과거: If + 주어 + 과거, 주어 + would/could + 동사원형", [], 5)
T.fixed('다음 대화의 내용과 일치하지 <u>않는</u> 것은?', '7과', Bx(
 "Emma: Dohun, we need to start our project on our dream country to visit.", "Dohun: That's right. Which country do you want to visit, Emma?", "Emma: In my case, I want to visit Spain.",
 "Dohun: What would you do if you visited Spain?", "Emma: I'm interested in buildings. So I would go see La Sagrada Familia.", "Dohun: That is the church Antoni Gaudí designed, isn't it?",
 "Emma: Yes, it is. It would be interesting to see how his design was inspired by nature.", "Dohun: Hmm... . How about <i>Gaudí and Spain</i> as the title for our project?", "Emma: I love it!"),
 ['It is Spain where Emma wants to visit.', 'Dohun might already know who designed La Sagrada Familia.', "Emma thought Gaudí's design showed a strong connection to nature.", "Dohun decided to make the project about Gaudí's buildings in several countries.", "Emma agreed with Dohun's idea for the project title."], 4,
 "이유 ▶ 제목은 'Gaudí and Spain' → 여러 나라가 아니라 스페인\n오답 ▶ ① I want to visit Spain ② That is the church Antoni Gaudí designed, isn't it? ③ inspired by nature ⑤ I love it!", [('inspire', '영감을 주다')], 4)
T.fixed('다음 중 어법상 옳지 <u>않은</u> 것은?', '8과 문법', '',
 ["Don't leave the door close.", 'Tests in school make students worried.', 'The new machine made our jobs easier.', 'Exercising every day makes me healthier.', 'Wearing sunscreen will keep you safe from sunburn.'], 1,
 "이유 ▶ leave + 목적어 + 형용사 보어: 문이 '닫힌' 상태 → closed. close ❌\n오답 ▶ ② make + 목적어 + worried ③ made + easier ④ makes + healthier ⑤ keep + safe → 모두 바름", [], 5)
T.fixed('다음 중 어법상 옳은 것은?', '8과 문법', '',
 ['This problem is too difficult to solve.', 'Not everyone agree with her opinion.', 'No pets is allowed in this apartment.', 'You have many friends at school to play.', "The laptop was so expensive that I couldn't buy."], 1,
 "이유 ▶ too ~ to … 너무 ~해서 …할 수 없다 ✔ (주어 This problem이 solve의 목적어라 it을 쓰지 않음)\n오답 ▶ ② everyone은 단수 → agrees ③ pets 복수 → are ④ 친구와 놀다 → to play with ⑤ so ~ that 절에는 목적어 필요 → buy it", [], 5)
VEN = Bx("ⓐ <u>If you live in Venice, you can take a gondola to school every morning</u>. Venice has 118 small islands. On weekends, you can travel from island to island by a vaporetto, a water bus. At high tide, ⓑ <u>the water from the Adriatic Sea often rises and leave the streets full of water</u>. However, you can walk around the town through the raised walkways.",
 "Venice is known as the \"floating city.\" In Venice, there are many colorful houses on the water. ⓒ <u>You may wonder how and why they built the houses on the water</u>. ⓓ <u>The old Venetians decided to live there to keep themselves safe from invaders</u>. But ⓔ <u>it was not easy for them to build their homes on this swampy surface</u>. So they installed more than 10 million wooden poles in the ground. It is these wooden poles which ________ (A) ________.")
T.fixed('[19~20] 위 글의 밑줄 친 ⓐ~ⓔ 중 어법상 옳지 <u>않은</u> 것은?', '7과', VEN, ['ⓐ', 'ⓑ', 'ⓒ', 'ⓓ', 'ⓔ'], 2,
 "이유 ▶ the water ~ rises and leave → 주어 the water(단수)에 맞춰 leaves\n오답 ▶ ⓐ 조건문 ⓒ 간접의문문 how and why + 주어 + 동사 ⓓ to부정사(목적) ⓔ 가주어 it ~ for them to → 모두 바름", [('swampy', '늪 같은')], 5)
T.fixed('위 글(19번)의 빈칸 (A)에 들어갈 말로 알맞은 것은?', '7과', '',
 ['connect the many small islands together like bridges', 'make Venice one of the most beautiful cities in the world', 'protect the people of Venice from the Adriatic Sea waves', 'hold up the buildings of Venice and keep the city standing', 'allow boats and gondolas to move easily through the canals'], 4,
 "이유 ▶ 늪지에 집을 짓기 어려워 나무 기둥을 박았다 → 기둥이 건물을 받치고 도시를 서 있게 한다 (본문: support Venice to this day)\n오답 ▶ ① 다리 ② 아름다움 ③ 파도 ⑤ 배의 이동", [('hold up', '떠받치다')], 5)
T.fixed('다음 중 의미가 <u>다른</u> 하나는?', '8과 문법', '',
 ['This area is smoke-free.', 'Nobody can smoke in this area.', 'No one can smoke in this area.', 'Not everyone can smoke in this area.', 'Smoking is not permitted in this area.'], 4,
 "이유 ▶ Not everyone = 모두가 ~인 것은 아니다(부분 부정) → 피울 수 있는 사람도 있음\n오답 ▶ ①②③⑤ 아무도 피울 수 없다(전체 부정)\n포인트 ▶ no one / nobody = 전체 부정, not everyone / not all = 부분 부정", [('smoke-free', '금연의'), ('permit', '허락하다')], 3)
T.fixed('다음 글의 내용을 두 문장으로 요약하고자 한다. 빈칸 (A), (B)에 들어갈 말로 가장 적절한 것은?', '7과', Bx(
 "Suppose you lived in a tulou, a huge round house in Fujian, China. You would always hang out with your friends at home. You might sometimes hear your neighbor calling you to come over for tea or dinner. A tulou usually has three to five floors. The first floor is used for cooking and eating, and people store food and tools on the second floor. Do you wonder where you would sleep? Your bedroom is on the third or fourth floor.",
 "A tulou is like a small village. The people living in a tulou usually have the same family name. Some large tulou can house up to fifty families. They work together, share many things, and protect each other by living together in one big building.",
 "↓", "A tulou is a massive circular residence in Fujian, China, designed for multiple families to live together in order to ____(A)____. Through constant interaction and shared responsibilities, its residents can ____(B)____ that strengthen their sense of unity and belonging."),
 ['expand trade − gain wealth', 'avoid noise − maintain privacy', 'save money − enjoy personal freedom', 'ensure safety − build strong social bonds', 'protect nature − reduce environmental damage'], 4,
 "이유 ▶ protect each other by living together → (A) 안전을 지키다(ensure safety) / work together, share many things → (B) 끈끈한 사회적 유대를 쌓다(build strong social bonds)\n오답 ▶ ① 무역·부 ② 소음·사생활 ③ 돈·자유 ⑤ 자연·환경", [('ensure', '보장하다'), ('bond', '유대')], 5)
T.fixed('다음 글의 밑줄 친 ⓐ~ⓔ 중 문맥상 낱말의 쓰임이 어색한 것은?', '7과', Bx(
 "Living in a pueblo, you can climb up a ladder to enter your house. There's a ⓐ <u>hidden</u> opening on top of the house. If ⓑ <u>unwelcome</u> visitors appeared, you would pull the ladder up to ⓒ <u>stop</u> them from entering. The thick walls are made of earth, straw, and water. They would keep me cool in summer and ⓓ <u>warm</u> in winter. The house has an extremely ⓔ <u>pointy</u> roof. Sometimes you would sleep comfortably up on the roof under the moon and stars."),
 ['ⓐ', 'ⓑ', 'ⓒ', 'ⓓ', 'ⓔ'], 5,
 "이유 ▶ 지붕 위에서 편하게 잔다 → 지붕은 뾰족한(pointy)이 아니라 평평한(flat) 지붕\n오답 ▶ ⓐ 숨겨진 ⓑ 반갑지 않은 ⓒ 막다 ⓓ 따뜻한 → 모두 자연스러움", [('pointy', '뾰족한')], 4)
T.fixed('다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 옳지 <u>않은</u> 것은?', '8과', Bx(
 "\"Look, the most dangerous time is between six in the evening and midnight. Four times more soldiers work at that time ⓐ <u>than</u> from six in the morning until noon. Do you see ⓑ <u>what</u> I mean?\"",
 "\"Aha! I get it now. Thank you so much, Pascal!\"", "\"You're welcome. I realize the importance of graphs, and everyone can agree that we still need ⓒ <u>it</u> in real life.\"",
 "Pascal walked out of the woods. When he looked back, he saw Robin Hood ⓓ <u>waving</u> at him. Pascal waved back and said to ⓔ <u>himself</u>, \"It was a great adventure. How do I go back? Oh, I know. I should say the words <i>Cogito ergo sum</i>!\""),
 ['ⓐ', 'ⓑ', 'ⓒ', 'ⓓ', 'ⓔ'], 3,
 "이유 ▶ 가리키는 말이 graphs(복수) → it이 아니라 them\n오답 ▶ ⓐ more ~ than ⓑ 관계대명사 what(~하는 것) ⓓ 지각동사 saw + 목적어 + -ing ⓔ say to oneself 혼잣말하다 → 모두 바름", [('say to oneself', '혼잣말하다')], 5)
T.fixed('다음 두 문장을 한 문장으로 바꾼 것 중 가장 적절한 것은?', '8과 문법', Bx("• The wind is too strong.", "• Jane can't wear a hat."),
 ['The wind is too strong to wear a hat.', 'The wind is too strong for Jane to wear a hat.', 'The wind is very strong, so Jane wears a hat.', 'Jane can wear a hat because the wind is so strong.', 'The wind is so strong that no one can wear a hat.'], 2,
 "이유 ▶ too ~ for 의미상 주어 to … : 너무 ~해서 (누가) …할 수 없다 → for Jane to wear ✔\n오답 ▶ ① Jane(의미상 주어)이 빠짐 ③④ 뜻이 반대 ⑤ Jane이 아니라 아무도(no one)", [], 4)
T.render()
