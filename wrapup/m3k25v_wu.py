# 11/20 중산중3 2025 기출(2학기 2차 지필) 변형 1회 — 기출 25문항과 같은 순서·유형·배점, 지문·보기를 바꿔 조금 더 어렵게
# 교과서 지문(7·8과 대화문·본문)은 교과서 문장 그대로, 응용 지문(한옥·은데벨레·행운의 숫자)은 새로 씀. 정답 ①~⑤ 각 5개
from wu_k25v import *
H = ('기출 변형', '중산중 2025 2학기 2차 지필 변형', '중산중 2025 기출 변형', 'k25v')
Bx = lambda *ls: BOX('<br>'.join(ls))
N = '작년(2025) 중산중 2학기 2차 지필평가와 같은 유형·배점으로 만든 변형 문제예요. 조금 더 어려워요. 45분 안에 풀고 OMR에 답을 입력하세요.'
T = Test('1', '1회', '2025 2학기 2차 지필 변형', '중산중 기출 변형', N, H=H)
# 1~2 반려동물 설문 (8과 L&S 1-A)
PET = Bx("Alex: Minju, what is this graph about?", "Minju: I did a survey on the kinds of pets my classmates have.", "Alex: What were the results?",
         "Minju: Eighty percent of the students have pets. Only five out of twenty-five students don't have pets.", "Alex: ________ (A) ________",
         "Minju: Well, ten students have dogs and three students have cats.", "Alex: What about the rest?", "Minju: Seven students have fish.")
T.flex('[1~2] 위 대화의 내용과 일치하지 <u>않는</u> 것은?', '8과', PET,
 ['More than half of the pet owners have cats.', 'Twenty students in the class have pets.', 'Dogs are the most common pets in the class.', 'Fewer students have cats than fish.', 'Half of the pet owners have dogs.'],
 "이유 ▶ 반려동물을 기르는 학생 20명 중 고양이는 3명뿐 → 절반이 넘지 않음\n오답 ▶ {1} 25명의 80% = 20명 {2} 개 10명이 가장 많음 {3} 고양이 3명 < 물고기 7명 {4} 20명 중 개 10명 = 절반",
 [('pet owner', '반려동물 주인'), ('common', '흔한')], 3)
T.flex('위 대화(1번)의 빈칸 (A)에 들어갈 말로 가장 알맞은 것은?', '8과', '',
 ['What kind of pets do they have?', 'How many students have pets?', "Why don't some students have pets?", 'Which pet is the most expensive?', 'How often do they walk their pets?'],
 "이유 ▶ 대답이 '개 10명, 고양이 3명' → 어떤 종류의 반려동물을 기르는지 묻는 말\n오답 ▶ {1} 몇 명인지는 이미 말함 {2} 이유 {3} 가격 {4} 산책 횟수 → 대답과 맞지 않음", [], 3)
# 3 도서관 설문 발표 (8과 Communication Task)
T.flex('다음 발표의 목적으로 가장 알맞은 것은?', '8과', Bx(
 "I did a survey on the books we want for our school library. The result says that thirteen out of twenty students chose novels. That is sixty-five percent of the total. "
 "Five out of twenty students chose science-fiction books. However, only two out of twenty students chose history books. From this survey result, I think the school library should get more novels. Do you see what I mean?"),
 ['to suggest that the school library buy more novels', 'to complain that the library has too many history books', 'to introduce some popular science-fiction books', 'to encourage students to read more history books', 'to explain how to borrow books from the library'],
 "이유 ▶ I think the school library should get more novels. → 설문 결과를 근거로 소설을 더 들여놓자고 제안\n오답 ▶ {1} 역사책이 많다는 불평 없음 {2} 공상 과학 책 소개 아님 {3} 역사책 권장 아님 {4} 대출 방법 없음",
 [('survey', '설문 조사'), ('novel', '소설')], 3)
# 4 한옥 (7과 응용, 새로 씀)
T.flex('다음 글의 내용과 일치하지 <u>않는</u> 것은?', '7과 응용', Bx(
 "Have you ever stayed in a <i>hanok</i>, a traditional Korean house? If you stayed in a <i>hanok</i>, you would sleep on the floor because there are no beds. "
 "Most <i>hanok</i> are built with natural materials such as wood, stone, straw, paper, and earth. In winter, the <i>ondol</i> heats the floor, so you would feel warm even on the coldest night. "
 "The doors are covered with thin paper, which lets air pass through. That is why the rooms stay cool in summer."),
 ['The doors of a hanok are made of thick wood to keep out the cold.', 'There are no beds in a hanok.', 'Hanok are mostly built with natural materials.', 'The ondol keeps the floor warm in winter.', 'Thin paper on the doors helps the rooms stay cool in summer.'],
 "이유 ▶ The doors are covered with thin paper → 두꺼운 나무 문이 아니라 얇은 종이를 바른 문\n오답 ▶ {1} there are no beds {2} natural materials {3} the ondol heats the floor {4} rooms stay cool in summer → 모두 일치",
 [('traditional', '전통적인'), ('material', '재료'), ('pass through', '통과하다')], 3)
# 5~7 Pascal (8과 본문 ❶❷, 교과서 그대로)
PAS = Bx("Pascal was doing his math homework in his room. He was struggling with graphs.",
 "\"It's too hard to read and draw graphs. Why do I need these anyway? No one needs graphs in real life.\" He put down his pen and picked up his favorite book, <i>Robin Hood</i>. He decided to read himself to sleep. When he was about to open the book, he heard a voice. He looked up from the book to see who was talking. He couldn't believe his eyes. It was his dog, Manny, who was talking!",
 "\"Close your eyes and repeat after me. <i>Cogito ergo sum</i>,\" said Manny.", "\"You can talk?\"", "\"Just repeat! <i>Cogito ergo sum</i>.\"",
 "Pascal closed his eyes and repeated the words. Suddenly, he heard men shouting. When he opened his eyes, he saw soldiers on horses. They were chasing a man with arrows in his hand. The man saw Pascal and shouted.",
 "\"It's too dangerous for you to stand there. Come on.\" The man pulled Pascal onto his horse and rode into the woods.", "When they arrived at a house, the man stopped and got off his horse.",
 "\"Hello, my name is Robin Hood.\"", "\"Wow! Are you the Robin Hood from the book?\"", "\"No, I'm the Robin Hood of Sherwood Forest. Who are you and why are you here?\"")
T.flex('[5~7] 위 글을 읽고 답할 수 <u>없는</u> 질문은?', '8과', PAS,
 ['What does <i>Cogito ergo sum</i> mean?', 'What was Pascal having trouble with?', 'Who was talking to Pascal in his room?', 'What did Pascal see when he opened his eyes?', 'Where did the man take Pascal on his horse?'],
 "이유 ▶ Cogito ergo sum의 뜻은 글에 나오지 않음\n오답 ▶ {1} graphs {2} his dog, Manny {3} soldiers on horses {4} into the woods (a house) → 모두 답할 수 있음",
 [('have trouble with', '~에 어려움을 겪다')], 4)
T.flex('위 글(5번)에서 일어난 일을 순서대로 바르게 나열한 것은?', '8과', Bx('(a) Pascal heard a voice.', '(b) Pascal picked up <i>Robin Hood</i>.', '(c) Pascal repeated some strange words.', '(d) Pascal saw soldiers on horses.', '(e) Pascal rode into the woods.'),
 ['(b) − (a) − (c) − (d) − (e)', '(a) − (b) − (c) − (d) − (e)', '(b) − (c) − (a) − (d) − (e)', '(b) − (a) − (d) − (c) − (e)', '(a) − (c) − (b) − (e) − (d)'],
 "이유 ▶ 책을 집어 듦(b) → 책을 펴려는 순간 목소리를 들음(a) → Cogito ergo sum을 따라 말함(c) → 눈을 뜨자 말 탄 군인들(d) → 남자의 말을 타고 숲으로(e)\n포인트 ▶ When he was about to open the book, he heard a voice. = 책을 펴려던 참에 목소리를 들었다",
 [('be about to', '막 ~하려던 참이다')], 3)
T.flex('위 글(5번)의 내용과 일치하는 것은?', '8과', '',
 ["The man said he was not the Robin Hood from Pascal's book.", 'Pascal fell asleep while he was reading <i>Robin Hood</i>.', 'Manny told Pascal to keep his eyes open.', 'The soldiers were chasing Pascal with arrows.', 'Pascal asked Robin Hood to take him back home.'],
 "이유 ▶ \"Are you the Robin Hood from the book?\" \"No, I'm the Robin Hood of Sherwood Forest.\" ✔\n오답 ▶ {1} 책을 펴기도 전에 목소리를 들었다 {2} Close your eyes {3} 쫓긴 사람은 화살을 든 남자 {4} 집에 데려다 달라는 말 없음",
 [('chase', '뒤쫓다')], 4)
# 8~9 은데벨레 (7과 응용, 새로 씀)
NDE = Bx("If you visited a village of the Ndebele in South Africa, you (A) <b>[ will / would ]</b> find houses with ⓐ <u>colorful</u> patterns. Each house tells its own story. Some patterns ⓑ <u>express</u> the feelings or ideas of the family.",
 "A long time ago, the Ndebele were in a terrible war with the Boers. When the Boers ⓒ <u>invaded</u> their land, the Ndebele painted their houses with symbols. The symbols were known only to the Ndebele people, so their enemies couldn't understand (B) <b>[ that / what ]</b> the messages meant. "
 "In other words, the Ndebele found the symbols ⓓ <u>easy</u> for their enemies to read. Since then, the art of painting the symbols (C) <b>[ has handed / has been handed ]</b> down from mothers to daughters, and it is still ⓔ <u>alive</u> today.")
T.flex('[8~9] 위 글의 (A), (B), (C)의 각 네모 안에서 어법에 맞는 표현을 골라 짝지은 것으로 가장 적절한 것은?', '7과 응용', NDE,
 ['would − what − has been handed', 'will − what − has been handed', 'would − that − has been handed', 'would − what − has handed', 'will − that − has handed'],
 "이유 ▶ (A) If + 과거(visited) → 주절 would find (가정법 과거) (B) meant의 목적어가 없음 → '~하는 것' what (간접의문문: 무엇을 의미하는지) (C) 기술이 '전해진' 것 → 수동 has been handed down\n오답 ▶ will은 가정법 아님 / that 뒤에는 완전한 문장 / has handed는 능동(hand down은 목적어가 필요)",
 [('invade', '침략하다'), ('symbol', '상징'), ('hand down', '물려주다')], 5)
T.fixed('위 글(8번)의 밑줄 친 ⓐ~ⓔ 중 문맥상 낱말의 쓰임이 어색한 것은?', '7과 응용', '', ['ⓐ', 'ⓑ', 'ⓒ', 'ⓓ', 'ⓔ'], 4,
 "이유 ▶ 적들이 메시지를 이해하지 못했다(In other words로 바꿔 말함) → 적들이 읽기 '쉬운(easy)'이 아니라 '어려운(hard / impossible)' 상징\n오답 ▶ ⓐ 다채로운 ⓑ 표현하다 ⓒ 침략했다 ⓔ 살아 있는 → 모두 자연스러움",
 [('in other words', '다시 말해')], 4)
# 10~11 탑과 군인 (8과 본문 ❸❹, 교과서 그대로)
TOW = Bx("\"My name is Pascal. I don't know why I'm here, but there must be a reason. You saved me from the soldiers. Thank you so much. Is there anything I can do for you?\"",
 "\"Well, can you help us get back the money that the king took from the people? He taxed them too much. He is too greedy to share with the people, so they don't have enough money to buy food. I want to help them get their money back. However, there are many soldiers in the tower, so no one can get inside.\"",
 "\"Hmm... I think I have a solution. But first, can you take me to the tower? I need to count the number of soldiers.\"",
 "Robin and Pascal hid up in a tree and counted the soldiers one by one.",
 "\"There are five soldiers from midnight to six in the morning. Next, there are three soldiers until noon, and then there are eight soldiers until six in the evening. Lastly, there are twelve soldiers until midnight. So, you should go inside between six in the morning and noon.\"",
 "\"What? I don't get it.\"", "Pascal thought for a moment. 'Hmm... A graph might make this easier to understand.' Pascal drew a graph and showed it to Robin.")
T.flex('[10~11] 위 글에서 Pascal이 센 군인 수에 대한 설명으로 옳지 <u>않은</u> 것은?', '8과', TOW,
 ['There are fewer soldiers from midnight to 6 a.m. than from 6 a.m. to noon.', 'The largest number of soldiers work from 6 p.m. to midnight.', 'There are four times as many soldiers from 6 p.m. to midnight as from 6 a.m. to noon.', 'There are more soldiers from noon to 6 p.m. than from midnight to 6 a.m.', 'The number of soldiers keeps going up from 6 a.m. until midnight.'],
 "이유 ▶ 자정~오전 6시 5명, 오전 6시~정오 3명 → 자정~오전 6시가 더 많음\n오답 ▶ {1} 오후 6시~자정 12명이 가장 많음 {2} 12명은 3명의 4배 {3} 8명 > 5명 {4} 3명 → 8명 → 12명으로 계속 늘어남",
 [('four times as many A as B', 'B보다 4배 많은 A')], 3)
T.flex('위 글(10번)의 내용과 일치하지 <u>않는</u> 것은?', '8과', '',
 ["Robin wanted to keep the king's money for himself.", 'Robin thinks the king is too greedy to share with the people.', 'Pascal wanted to count the soldiers before explaining his solution.', "Robin didn't understand Pascal's explanation at first.", 'Robin and Pascal counted the soldiers while hiding in a tree.'],
 "이유 ▶ I want to help them get their money back. → 돈을 사람들에게 돌려주려는 것이지 자기가 가지려는 것이 아님\n오답 ▶ {1} He is too greedy to share {2} But first ... I need to count the number of soldiers {3} What? I don't get it. {4} hid up in a tree and counted",
 [('greedy', '욕심 많은'), ('tax', '세금을 매기다')], 4)
# 12 숫자의 의미 (8과 응용, 새로 씀)
T.flex('주어진 글 다음에 이어질 글의 순서로 가장 적절한 것은?', '8과 응용', Bx(
 "Numbers can have special meanings in different cultures. A number that is lucky in one culture may be unlucky in another. The number 13 is a good example.",
 "(A) This is why some buildings in the USA do not have a 13th floor. People believe the floor number might bring them bad luck.",
 "(B) In many Western countries, people think 13 is unlucky. Some of them even feel nervous on Friday the 13th.",
 "(C) In Italy, however, 13 is often seen as a lucky number. There, it is 17 that many people try to avoid."),
 ['(B) − (A) − (C)', '(A) − (B) − (C)', '(A) − (C) − (B)', '(B) − (C) − (A)', '(C) − (A) − (B)'],
 "이유 ▶ 13이 좋은 예 → (B) 서양에서는 13이 불운 → (A) 그래서(This is why) 미국 건물엔 13층이 없음 → (C) 하지만(however) 이탈리아에선 13이 행운\n포인트 ▶ This is why는 바로 앞 내용의 결과, however는 앞과 반대 내용",
 [('avoid', '피하다'), ('nervous', '불안한')], 4)
# 13 성냥개비 대화 (8과 L&S 2-A)
T.flex('두 사람의 대화가 자연스럽도록 (A)~(D)를 바르게 배열한 것은?', '8과', Bx(
 "Jinsu: Emma, can you help me with this math problem?",
 "(A) You have to move one stick to make this sum right. How could four minus five equal six?",
 "(B) Yes, now I see what you mean. Eleven minus five equals six. How clever!",
 "(C) Sure, what is it?",
 "(D) Oh, it's simple. You need to move one of the sticks in number four to make it eleven. Do you see what I mean?",
 "Emma: Thinking outside the box can be helpful sometimes."),
 ['(C) − (A) − (D) − (B)', '(A) − (C) − (D) − (B)', '(C) − (D) − (A) − (B)', '(D) − (A) − (C) − (B)', '(C) − (A) − (B) − (D)'],
 "이유 ▶ Emma (C) 그래, 뭔데? → Jinsu (A) 성냥개비 하나를 옮겨 4 − 5 = 6을 맞춰야 해 → Emma (D) 4의 성냥개비를 옮겨 11로 → Jinsu (B) 알겠다, 11 − 5 = 6 → Emma 틀에서 벗어난 생각",
 [('think outside the box', '틀에서 벗어나 생각하다')], 3)
# 14 알래스카 대화 (7과 L&S 1-B)
T.flex('두 사람의 대화가 자연스럽도록 (A)~(E)를 바르게 배열한 것은?', '7과', Bx(
 "Taeho: Will it snow today?",
 "(A) Let me check the weather. Umm, there will be no snow for a while.",
 "(B) No kidding! Alaska is a very cold place.",
 "(C) I have no idea. Why are you waiting for snow, Taeho?",
 "(D) I wish I could live in Alaska. Then I could go sledding all day!",
 "(E) I got a new sled for my birthday. I can't wait to test it out.",
 "Taeho: I think it would be fun. I want to build a snow house and stay there on vacation.", "Sora: Living in a snow house sounds fun!"),
 ['(C) − (E) − (A) − (D) − (B)', '(A) − (C) − (E) − (D) − (B)', '(C) − (E) − (D) − (A) − (B)', '(C) − (A) − (E) − (D) − (B)', '(E) − (C) − (A) − (B) − (D)'],
 "이유 ▶ Sora (C) 모르겠어, 왜 눈을 기다려? → Taeho (E) 새 썰매를 받았어 → Sora (A) 날씨 확인, 한동안 눈 없음 → Taeho (D) 알래스카에 살면 좋을 텐데 → Sora (B) 말도 안 돼, 거긴 아주 추워 → Taeho I think it would be fun.",
 [('sled', '썰매'), ('No kidding!', '설마! 농담이지?')], 4)
# 15 가정법 전환
T.flex('다음 문장을 가정법으로 바꾼 것 중 <u>틀린</u> 것은?', '7과', '',
 ["As Mina has a cold, she can't go swimming.<br>→ If Mina had a cold, she could go swimming.",
  "As I don't live in a jungle, I can't make animal friends.<br>→ If I lived in a jungle, I could make animal friends.",
  "As I am not a millionaire, I won't build my own house.<br>→ If I were a millionaire, I would build my own house.",
  "As I don't know her phone number, I can't call her.<br>→ If I knew her phone number, I could call her.",
  "As the house is upside down, it isn't easy to live there.<br>→ If the house weren't upside down, it would be easy to live there."],
 "이유 ▶ 사실(감기에 걸림)의 반대로 바꿔야 함 → If Mina didn't have a cold, she could go swimming.\n오답 ▶ {1}{2}{3}{4} 긍정·부정을 반대로, 현재 → 과거, can't/won't → could/would로 바르게 바꿈",
 [], 5)
# 16 거울 집 대화 (7과 L&S 2-A)
T.flex('다음 대화의 내용과 일치하지 <u>않는</u> 것은?', '7과', Bx(
 "Sora: What would you do if you became a millionaire, Juwon?", "Juwon: I would build my own house.", "Sora: What kind of house would you build?",
 "Juwon: I would build a house that is completely covered with mirrors.", "Sora: Why?", "Juwon: The mirrors would make the house almost invisible. Wouldn't that be cool?", "Sora: That would be cool!"),
 ['Juwon is going to build a mirror house because he became a millionaire.', 'Sora asked Juwon about an imaginary situation.', 'Juwon wants his house to be covered with mirrors.', 'Juwon thinks the mirrors would make the house hard to see.', "Sora agreed that Juwon's house would be cool."],
 "이유 ▶ What would you do if you became a millionaire? → 가정법 과거: 실제로 백만장자가 된 것이 아님\n오답 ▶ {1} 가정 상황을 물음 {2} completely covered with mirrors {3} almost invisible = 거의 보이지 않는 {4} That would be cool!",
 [('millionaire', '백만장자'), ('invisible', '보이지 않는')], 4)
# 17 어법 (5형식)
T.flex('다음 중 어법상 옳지 <u>않은</u> 것은?', '8과 문법', '',
 ['Her parents made her to practice the piano every day.', 'He kept me waiting for an hour.', 'The thick walls keep the house cool in summer.', 'The mirrors would make the house almost invisible.', "Don't leave the door open."],
 "이유 ▶ 사역동사 make + 목적어 + 동사원형 → made her practice (to practice ❌)\n오답 ▶ {1} keep + 목적어 + -ing(능동) {2} keep + 목적어 + 형용사 {3} make + 목적어 + 형용사 {4} leave + 목적어 + 형용사 → 모두 바름",
 [], 5)
# 18 어법 (too ~ to · No one · 부분 부정)
T.flex('다음 중 어법상 옳은 것은?', '8과 문법', '',
 ['The box was too heavy for me to carry.', 'No one want to go out in this cold weather.', 'This soup is too hot to eat it.', 'Not every student like history.', "The question was so difficult that I couldn't answer."],
 "이유 ▶ too ~ for 의미상 주어 to … ✔ (주어 The box가 carry의 목적어라 it을 쓰지 않음)\n오답 ▶ {1} No one은 단수 → wants {2} 주어 = 목적어 → to eat (it ❌) {3} every + 단수 → likes {4} so ~ that 절엔 목적어 필요 → answer it",
 [], 5)
# 19~20 베네치아 (7과 본문 ❷)
VEN = Bx("If I lived in Venice, I ⓐ <u>would take</u> a gondola to school every morning. Venice has 118 small islands. On weekends, I would travel from island to island by a <i>vaporetto</i>, a water bus. At high tide, the water from the Adriatic Sea often rises and ⓑ <u>leaves</u> the streets full of water. However, I would be able to walk around the town through the ⓒ <u>raised</u> walkways.",
 "Venice is known ⓓ <u>as</u> the \"floating city.\" In Venice, there are many colorful houses on the water. You may wonder how and why ⓔ <u>did they build</u> the houses on the water. The old Venetians decided to live there to keep themselves safe from invaders. But it was not easy for them to build their homes on this swampy surface. So ________ (A) ________. It is these wooden poles that support Venice to this day.")
T.fixed('[19~20] 위 글의 밑줄 친 ⓐ~ⓔ 중 어법상 옳지 <u>않은</u> 것은?', '7과', VEN, ['ⓐ', 'ⓑ', 'ⓒ', 'ⓓ', 'ⓔ'], 5,
 "이유 ▶ 간접의문문은 의문사 + 주어 + 동사 → how and why they built (did they build ❌)\n오답 ▶ ⓐ 가정법 과거 would + 동사원형 ⓑ 주어 the water(단수) → rises and leaves ⓒ '높여진' 보도 → 과거분사 raised ⓓ be known as ~로 알려지다 → 모두 바름",
 [('raised', '높여진, 높인'), ('be known as', '~로 알려지다')], 5)
T.flex('위 글(19번)의 빈칸 (A)에 들어갈 말로 가장 알맞은 것은?', '7과', '',
 ['they installed more than 10 million wooden poles in the ground', 'they pulled all the wooden poles out of the ground', 'they moved their homes to the top of a mountain', 'they built high stone walls around the islands', 'they decided to live on boats instead of in houses'],
 "이유 ▶ 늪지에 집을 짓기 어려움 → 그래서 나무 기둥을 박았다 → 바로 뒤 these wooden poles가 그 기둥을 가리킴\n오답 ▶ {1} 기둥을 뽑았다면 기둥이 도시를 받칠 수 없음 {2}{3}{4} 뒤 문장의 these wooden poles와 이어지지 않음",
 [('install', '설치하다'), ('swampy', '늪 같은'), ('pole', '기둥')], 5)
# 21 의미가 다른 것 (전체 부정 / 부분 부정)
T.flex('다음 중 의미가 <u>다른</u> 하나는?', '8과 문법', '',
 ['Not everyone can eat snacks in this library.', 'No one can eat snacks in this library.', 'Nobody can eat snacks in this library.', 'Eating snacks is not allowed in this library.', 'Eating snacks is not permitted in this library.'],
 "이유 ▶ Not everyone = 모두가 ~할 수 있는 것은 아니다(부분 부정) → 먹을 수 있는 사람도 있음\n오답 ▶ {1}{2}{3}{4} 아무도 먹을 수 없다(전체 부정)\n포인트 ▶ no one / nobody = 전체 부정, not everyone / not all = 부분 부정",
 [('permit', '허락하다')], 3)
# 22 푸에블로 요약 (7과 본문 ❶)
T.flex('다음 글의 내용을 한 문장으로 요약하고자 한다. 빈칸 (A), (B)에 들어갈 말로 가장 적절한 것은?', '7과', Bx(
 "If I lived in a pueblo, I would climb up a ladder to enter my house. There's a hidden opening on top of the house. If unwelcome visitors appeared, I would pull the ladder up to stop them from entering. "
 "The thick walls are made of earth, straw, and water. They would keep me cool in summer and warm in winter. The house has a flat roof. I would sometimes sleep up on the roof under the moon and stars.",
 "↓", "A pueblo is designed to ____(A)____ the people inside from unwelcome visitors and to keep them comfortable ____(B)____."),
 ['protect − in both summer and winter', 'invite − only in summer', 'protect − only in winter', 'hide − only at night', 'separate − during the rainy season'],
 "이유 ▶ 사다리를 끌어올려 낯선 방문객을 막음 → (A) 보호하다(protect … from) / 두꺼운 벽이 여름엔 시원하게, 겨울엔 따뜻하게 → (B) 여름과 겨울 모두\n오답 ▶ {1} 초대 ✗ {2} 겨울만 ✗ {3} 숨기다·밤만 ✗ {4} 분리·우기 ✗",
 [('unwelcome', '반갑지 않은'), ('comfortable', '편안한')], 5)
# 23 토루 낱말 (7과 본문 ❸)
T.fixed('다음 글의 밑줄 친 ⓐ~ⓔ 중 문맥상 낱말의 쓰임이 어색한 것은?', '7과', Bx(
 "If I lived in a tulou, a huge round house in Fujian, China, I would ⓐ <u>rarely</u> have friends at home to play with. I would sometimes hear my neighbor ⓑ <u>calling</u> me to come over for tea or dinner. In a tulou, there are usually three to five floors. "
 "The first floor is used for cooking and eating. And people ⓒ <u>store</u> food and tools on the second floor. A tulou is like a ⓓ <u>village</u>. Some large tulou can house up to 50 families. They work together and share many things. Living together in one building keeps them ⓔ <u>safe</u>."),
 ['ⓐ', 'ⓑ', 'ⓒ', 'ⓓ', 'ⓔ'], 1,
 "이유 ▶ 이웃이 차·저녁 먹으러 오라고 부르고, 50가구까지 함께 사는 마을 같은 집 → 함께 놀 친구가 '거의 없는(rarely)'이 아니라 '언제나(always)' 있음\n오답 ▶ ⓑ 부르는 ⓒ 보관하다 ⓓ 마을 ⓔ 안전한 → 모두 자연스러움",
 [('rarely', '좀처럼 ~않는'), ('store', '보관하다')], 4)
# 24 어법 ⓐ~ⓔ (8과 본문 ❹)
T.fixed('다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 옳지 <u>않은</u> 것은?', '8과', Bx(
 "\"Look, the most dangerous time is between six in the evening and midnight. Four times ⓐ <u>more</u> soldiers work at that time than from six in the morning until noon. Do you see ⓑ <u>what</u> I mean?\"",
 "\"Aha! I get it now. Thank you so much, Pascal!\"", "\"You're welcome. Now I realize the importance of graphs. No one can say that we don't need ⓒ <u>them</u> anymore.\"",
 "Pascal walked out of the woods. When he looked back, he saw Robin Hood ⓓ <u>to wave</u> at him. Pascal waved back and said to ⓔ <u>himself</u>, \"It was a great adventure. How do I go back? Oh, I know. I should say the words <i>Cogito ergo sum</i>!\""),
 ['ⓐ', 'ⓑ', 'ⓒ', 'ⓓ', 'ⓔ'], 4,
 "이유 ▶ 지각동사 see + 목적어 + 동사원형/-ing → saw Robin Hood waving (wave) at him (to wave ❌)\n오답 ▶ ⓐ 배수 + more ~ than ⓑ 관계대명사 what(~하는 것) ⓒ graphs(복수) → them ⓔ say to oneself 혼잣말하다 → 모두 바름",
 [('say to oneself', '혼잣말하다')], 5)
# 25 too ~ to 한 문장
T.flex('다음 두 문장을 한 문장으로 바꾼 것 중 가장 적절한 것은?', '8과 문법', Bx('• This coffee is too hot.', "• My sister can't drink it."),
 ['This coffee is too hot for my sister to drink.', 'This coffee is too hot for my sister to drink it.', 'This coffee is so hot that my sister can drink it.', 'This coffee is too hot to drink it for my sister.', 'This coffee is hot enough for my sister to drink.'],
 "이유 ▶ too ~ for 의미상 주어 to … : 너무 ~해서 (누가) …할 수 없다, 주어(This coffee) = drink의 목적어 → it 생략 ✔\n오답 ▶ {1} it을 또 씀 {2} 뜻이 반대(can) {3} 어순·it 모두 틀림 {4} enough는 '충분히 ~해서 할 수 있다'로 뜻이 반대",
 [], 4)
assert [it['pts'] for it in T.items] == [3, 3, 3, 3, 4, 3, 4, 5, 4, 3, 4, 4, 3, 4, 5, 4, 5, 5, 5, 5, 3, 5, 4, 5, 4], [it['pts'] for it in T.items]
for it in T.items:
    if it['opts']: assert len(set(map(str, it['opts']))) == 5, it['stem']
T.render()
