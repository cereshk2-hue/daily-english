# 11/15 너른터 8과 변형기출 1~4세트 (중3 지학사 민찬규 Lesson 8 · Pascal과 Robin Hood)
# 원본: 선생님이 다른 곳에서 만든 88문항 hwpx(work/nrt8). 검수해서 오류 고치고 객관식 80문항(20 × 4)으로 정리.
# 1세트 문법(too ~ to · enough to · so ~ that) + 본문 ① / 2세트 본문 ①② / 3세트 본문 ②③ / 4세트 본문 ③④
from wu_nrt7 import *
H = ('너른터 8과 변형기출', '중3 영어 지학사(민찬규) Lesson 8', '너른터 8과 변형기출', 'nrt8')
B = lambda *ls: BOX('<br>'.join(ls))
R, G = '본문', '문법'
P1 = ('Pascal was doing his math homework in his room. He was struggling with graphs. "It\'s too hard to read and draw graphs. Why do I need these anyways? No one needs graphs in real life." '
      'He put down his pen and picked up his favorite book, Robin Hood. He decided to read himself to sleep. When he was about to open the book, he heard a voice. He looked up from the book to see who was talking. '
      'He couldn\'t believe his eyes. It was his dog, Manny, who was talking! "Close your eyes and repeat after me. Cogito ergo sum," said Manny. "You can talk?" "Just repeat! Cogito ergo sum." Pascal closed his eyes and repeated the words.')
P2 = ('Suddenly, he heard men shouting. When he opened his eyes, he saw soldiers on horses. They were chasing a man with arrows in his hand. The man saw Pascal and shouted. "It\'s too dangerous for you to stand there. Come on." '
      'The man pulled Pascal onto his horse and rode into the woods. When they arrived at a house, the man stopped and got off his horse. "Hello, my name is Robin Hood." "Wow! Are you the Robin Hood from the book?" '
      '"No, I\'m the Robin Hood of Sherwood Forest. Who are you and why are you here?"')
P3 = ('"My name is Pascal. I don\'t know why I\'m here, but there must be a reason. You saved me from the soldiers. Thank you so much. Is there anything I can do for you?" '
      '"Well, can you help us get back the money that the king took from the people? He taxed them too much. He is too greedy to share with the people, so they don\'t have enough money to buy food. I want to help them get their money back. '
      'However, there are many soldiers in the tower, so no one can get inside." "Hmm... I think I have a solution. But first, can you take me to the tower? I need to count the number of soldiers."')
P4 = ('Robin and Pascal hid up in a tree and counted the soldiers one by one. "There are five soldiers from midnight to six in the morning. Next, there are three soldiers until noon, and then there are eight soldiers until six in the evening. '
      'Lastly, there are twelve soldiers until midnight. So, you should go inside between six in the morning and noon." "What? I don\'t get it." Pascal thought for a moment. \'Hmm... A graph might make this easier to understand.\' Pascal drew a graph and showed it to Robin.')
NOTICE = '너른터 8과 변형기출을 검수해서 정답 오류·문항 오류를 고치고, 서술형 일부는 객관식으로 바꿨어요. 답은 아래 OMR에 입력하세요.'
def UL(text, marks):
    """marks: [(번호, 바꿀 원문, 표시할 말)] → 본문 속 해당 말을 ①~⑤ 밑줄로"""
    for n, old, new in marks:
        assert text.count(old) == 1, old
        text = text.replace(old, old.replace(new, CN(n, new), 1) if new in old else CN(n, new))
    return text

# ═══════════════ 1세트 · 문법 + 본문 ① ═══════════════
T = Test('1', '1세트', '문법 too ~ to · enough to + 본문 ①', '8과 문법 · 본문 1', NOTICE, H=H)
# [원Q1]
T.flex('다음 우리말과 의미가 같은 것은?', G, B('너무 뜨거워서 나는 그것을 먹을 수가 없었다.'),
 ['It was too hot for me to eat.', 'It was so hot that I could eat it.', 'It was too hot for me to eat it.', "It was so hot that I can't eat it.", "It was so hot that I couldn't eat."],
 "이유 ▶ too + 형용사 + for 목적격 + to부정사(너무 ~해서 …할 수 없다). 주어 It과 eat의 목적어가 같으므로 to eat 뒤에 it을 쓰지 않는다.\n오답 ▶ {1} 긍정(could) {2} 목적어 it 중복 {3} 시제 불일치(was – can't) {4} so ~ that 절에서는 목적어 it이 필요\n포인트 ▶ so ~ that 절: it 필요 / too ~ to: it 빼기", [])
# [원Q2]
T.flex('다음 문장과 의미가 같은 것은?', G, B('He is so tall that he can reach the top shelf.'),
 ['He is tall enough to reach the top shelf.', 'He is enough tall to reach the top shelf.', 'He is so tall to reach the top shelf.', 'He is too tall for him to reach the top shelf.', 'He is too tall to reach the top shelf.'],
 "이유 ▶ so ~ that 주어 can = 형용사 + enough to(~할 만큼 충분히 …하다).\n오답 ▶ {1} enough는 형용사 뒤 {2} so ~ to ❌ {3}·{4} too ~ to는 '할 수 없다'(반대 의미)\n포인트 ▶ can → enough to / can't → too ~ to", [('shelf', '선반')])
# [원Q3]
T.flex('다음 문장 전환이 바르지 <u>않은</u> 것은?', G, '',
 ['He was confident enough to try that. = He was so confident that he can try that.', "He is too weak to do the task. = He is so weak that he can't do the task.", 'She seemed to be honest. = It seemed that she was honest.',
  'I found it easy to solve the conflict. = It was easy for me to solve the conflict.', "He didn't know what to do. = He didn't know what he should do."],
 "이유 ▶ 주절이 과거(was)이므로 that절도 과거 → could try.\n오답 ▶ {1} too ~ to = so ~ that ~ can't ✔ {2} seem to = It seems that ✔ {3} ✔ {4} 의문사 + to부정사 = 의문사 + 주어 + should ✔\n포인트 ▶ so ~ that 전환: 시제 일치!", [('confident', '자신감 있는'), ('conflict', '갈등')])
# [원Q4]
T.flex('다음 문장과 의미가 같은 것은?', G, B("This room is so small that we can't sleep in it."),
 ['This room is too small for us to sleep in.', 'This room is too small to sleep for us in.', 'This room is too small for we to sleep in it.', 'This room is too small for us to sleep in it.', 'This room is too small to sleep in it for us.'],
 "이유 ▶ 의미상 주어는 for + 목적격(us), 주어 This room = sleep in의 목적어 → it을 뺀다. 전치사 in은 남긴다.\n오답 ▶ {1}·{4} 의미상 주어 위치 {2} for we ❌ {3} it 중복", [])
# [원Q5]
T.flex('다음 문장과 의미가 같은 것은?', G, B("He is so busy that he can't play basketball."),
 ['He is too busy to play basketball.', "He isn't busy, so he can play basketball.", 'He wants to be busy playing basketball.', "He can't play basketball although he isn't busy.", 'He is very busy, but he wants to play basketball.'],
 "이유 ▶ so ~ that ~ can't = too ~ to.\n오답 ▶ {1}·{3} 바쁘지 않다(반대) {2} 바쁘고 싶다 {4} 하고 싶다는 말은 없음", [])
# [원Q6]
T.flex('다음 두 문장을 한 문장으로 바르게 나타낸 것은?', G, B('John is very tired. He can\'t walk any longer.'),
 ["John is so tired that he can't walk any longer.", 'John is so tired that to walk any longer.', 'John is so tired that he can walk any longer.', 'John is too tired to can walk any longer.', "John is too tired that he can't walk any longer."],
 "이유 ▶ so + 형용사 + that + 주어 + can't = 너무 ~해서 …할 수 없다 (= John is too tired to walk any longer.)\n오답 ▶ {1} that 뒤에는 주어 + 동사 {2} 긍정 {3} to can ❌ {4} too ~ that ❌\n수정 ▶ 원본 ④의 오타(the can't)를 고침", [('any longer', '더 이상')])
# [원Q7 서술형 → 객관식]
T.flex('다음 문장과 의미가 같은 것은?', G, B('I was too sick to attend the conference.'),
 ["I was so sick that I couldn't attend the conference.", "I was so sick that I can't attend the conference.", 'I was so sick that I could attend the conference.', 'I was sick enough to attend the conference.', "I was so sick to attend the conference."],
 "이유 ▶ too ~ to = so ~ that ~ can't. 주절이 과거(was) → couldn't.\n오답 ▶ {1} 시제 {2} 긍정 {3} enough to는 '할 수 있다' {4} so ~ to ❌\n수정 ▶ 원본 7번(주관식)을 객관식으로 바꿈", [('attend', '참석하다'), ('conference', '회의')])
# [원Q8 서술형 → 객관식]
T.flex('다음 문장과 의미가 같은 것은?', G, B("This car is so expensive that I can't buy it."),
 ['This car is too expensive for me to buy.', 'This car is too expensive for me to buy it.', 'This car is too expensive for I to buy.', 'This car is expensive enough for me to buy.', 'This car is so expensive for me to buy.'],
 "이유 ▶ too ~ for 목적격 to. 주어 This car = buy의 목적어 → it을 뺀다.\n오답 ▶ {1} it 중복 {2} for I ❌ {3} 반대 의미 {4} so ~ to ❌\n수정 ▶ 원본 8번(주관식)을 객관식으로 바꿈", [])
# [원Q9]
T.fixed('다음 중 어법상 <u>틀린</u> 것은?', G, '', ['He was enough smart to do the task.', 'She was pretty enough to get much attention.', 'He was fast enough to catch the thief.', 'This machine was simple enough to use.', "It was so expensive that we couldn't buy it."], 1,
 "이유 ▶ enough는 형용사 뒤에서 꾸민다 → smart enough to.\n오답 ▶ ②·③·④ 형용사 + enough to ✔ ⑤ so ~ that 절에 목적어 it ✔\n수정 ▶ 원본은 ⑤(couldn't buy, it 빠짐)도 틀려서 정답이 ①⑤ 두 개 → ⑤에 it을 넣어 정답 하나로", [])
# [원Q10]
T.fixed('다음 중 어법상 <u>틀린</u> 것은?', G, '', ['He was too hard to satisfy him.', 'It was easy enough to do.', 'He was sad to hear the news.', 'It was too boring to keep reading.', 'It is simple enough to solve.'], 1,
 "이유 ▶ 주어 He = satisfy의 목적어 → him을 뺀다. He was too hard to satisfy.(그는 너무 까다로워서 만족시킬 수 없었다)\n오답 ▶ ② 형용사 + enough ✔ ③ 감정의 원인 to부정사 ✔ ④·⑤ ✔\n수정 ▶ 원본은 ②(enough easy)도 틀려서 정답이 ①② 두 개 → ②를 easy enough로 고쳐 정답 하나로", [('satisfy', '만족시키다')])
# [원Q11]
T.fixed('다음 중 어법상 <u>잘못된</u> 문장의 개수는?', G, B(
 'ⓐ I was so sleepy to finish my homework.', 'ⓑ He is smart enough to solve the problem.', 'ⓒ My brother is too angrily to talk with me.', 'ⓓ She jogs every morning so that she can stay healthy.',
 'ⓔ The book is too hard to read it.', 'ⓕ Not everyone can sing well.', 'ⓖ He jogs every morning in order to he can stay healthy.', 'ⓗ Nobody go out in this hot weather.'),
 ['2개', '3개', '4개', '5개', '6개'], 4,
 "이유 ▶ 틀린 것 ⓐ so → too ⓒ angrily → angry ⓔ it 빼기 ⓖ in order to → so that ⓗ Nobody(단수) → goes → 5개\n맞는 것 ▶ ⓑ smart enough to ⓓ so that + 주어 + can ⓕ Not everyone(부분 부정)\n수정 ▶ 원본 보기 번호(①~⑧)가 선택지 번호와 겹쳐 ⓐ~ⓗ로 바꿈", [])
# [원Q12 서술형 → 객관식]
T.flex('밑줄 친 문장의 우리말 해석으로 알맞은 것은?', R, B('He couldn\'t believe his eyes. <u>It was his dog, Manny, who was talking!</u>'),
 ['말하고 있던 것은 바로 그의 개 Manny였다!', '그의 개 Manny는 말하는 것을 좋아했다!', '그것은 말을 할 줄 아는 개 Manny였다!', '그의 개 Manny가 누군가와 이야기하고 있었다!', '그는 개 Manny에게 말을 걸고 있었다!'],
 "이유 ▶ It was ~ who …: '…한 것은 바로 ~였다' 강조 구문. 강조된 말은 his dog, Manny.\n오답 ▶ {1} 좋아했다 ❌ {2} 강조의 뜻이 빠짐 {3} 누군가와 ❌ {4} 말을 건 사람이 바뀜\n수정 ▶ 원본 12번(주관식)을 객관식으로 바꿈", [])
# [원Q13]
T.fixed('다음 글의 밑줄 친 부분 중 어법상 가장 어색한 것은?', R, B(UL(P1, [(1, "It's too hard", 'too'), (2, 'No one needs', 'needs'), (3, 'read himself', 'himself'), (4, 'about to open', 'open'), (5, 'Manny, who', 'who')]).replace('needs</u>', 'need</u>')),
 None, 2,
 "이유 ▶ No one(아무도 ~ 않다)은 단수 취급 → needs.\n오답 ▶ ① too ~ to ✔ ③ 주어 = 목적어 → 재귀대명사 ✔ ④ be about to + 동사원형 ✔ ⑤ It was ~ who 강조 ✔\n포인트 ▶ No one, Nobody, Everyone + 단수 동사", [])
# [원Q14]
T.fixed('글의 흐름으로 보아, 주어진 문장이 들어갈 위치로 가장 적절한 곳은?', R, B('Why do I need these anyways?') + '\n' + B(
 'Pascal was doing his math homework in his room. He was struggling with graphs.' + GP(1) + '"It\'s too hard to read and draw graphs.' + GP(2) + 'No one needs graphs in real life." He put down his pen and picked up his favorite book, Robin Hood. He decided to read himself to sleep.' +
 GP(3) + 'When he was about to open the book, he heard a voice.' + GP(4) + 'He looked up from the book to see who was talking.' + GP(5) + 'He couldn\'t believe his eyes.'), None, 2,
 "이유 ▶ 그래프는 너무 어렵다 → '도대체 이것들(these = 그래프 읽고 그리기)이 왜 필요해?' → 실생활에서 아무도 필요 없어.\n포인트 ▶ these가 가리키는 graphs 바로 뒤", [('anyways', '도대체, 어쨌든')])
# [원Q16 서술형 → 객관식]
T.flex('[ ] 안의 단어를 바르게 배열한 것은?', R, B('He was struggling with graphs. "[ graphs / and / to / too / hard / draw / read / it\'s ]. Why do I need these anyways?"'),
 ["It's too hard to read and draw graphs.", "It's too hard to graphs read and draw.", "It's hard too to read and draw graphs.", "It's to read and draw too hard graphs.", "It's too hard graphs to read and draw."],
 "이유 ▶ It's too + 형용사 + to + 동사원형: 그래프를 읽고 그리는 것은 너무 어렵다.\n수정 ▶ 원본 16번(주관식)을 객관식으로 바꿈", [('struggle with', '~으로 고생하다')])
# [원Q17]
T.fixed('다음 글의 밑줄 친 부분 중 어법상 가장 어색한 것은?', R, B(UL(P1, [(1, 'need these', 'these'), (2, 'No one needs', 'needs'), (3, 'read himself', 'himself'), (4, 'see who', 'who'), (5, 'and repeated the words', 'repeated')]).replace('himself</u>', 'him</u>')),
 None, 3,
 "이유 ▶ 주어(He)와 목적어가 같은 사람 → 재귀대명사 himself. read oneself to sleep = 책을 읽다가 잠들다.\n오답 ▶ ① 그래프들 ✔ ② 단수 ✔ ④ 간접의문문(누가 말하는지) ✔ ⑤ closed와 병렬 ✔", [])
# [원Q18]
T.fixed('다음 글의 밑줄 친 문장 ①~⑤ 중 어법상 가장 어색한 것은?', R, B(
 CN(1, 'Pascal was doing his math homework in his room') + '. He was struggling with graphs. "It\'s too hard to read and draw graphs. Why do I need these anyways? ' + CN(2, 'No one needs graphs in real life') + '." ' +
 CN(3, 'He put down his pen and pick up his favorite book, Robin Hood') + '. He decided to read himself to sleep. When he was about to open the book, he heard a voice. ' + CN(4, 'He looked up from the book to see who was talking') + '. ... ' + CN(5, 'Pascal closed his eyes and repeated the words') + '.'), None, 3,
 "이유 ▶ 과거 동사 put과 and로 나란히 → picked up.\n오답 ▶ ①·②·④·⑤ 본문 그대로 ✔\n포인트 ▶ and 앞뒤 동사의 시제 일치", [])
# [원Q20]
T.fixed('글의 흐름으로 보아, 주어진 문장이 들어갈 위치로 가장 적절한 곳은?', R, B('He looked up from the book to see who was talking.') + '\n' + B(
 'No one needs graphs in real life."' + GP(1) + 'He put down his pen and picked up his favorite book, Robin Hood.' + GP(2) + 'He decided to read himself to sleep.' + GP(3) + 'When he was about to open the book, he heard a voice.' + GP(4) +
 'He couldn\'t believe his eyes.' + GP(5) + 'It was his dog, Manny, who was talking!'), None, 4,
 "이유 ▶ 목소리를 들었다 → 누가 말하는지 보려고 고개를 들었다 → 자기 눈을 믿을 수 없었다.\n포인트 ▶ 소리를 듣고(heard a voice) → 확인하러 봄(looked up)", [])
# [원Q21]
T.flex('다음 글의 내용과 일치하지 <u>않는</u> 것은?', R, B(P1),
 ['Manny was a character in the book Pascal was reading.', 'Pascal had difficulty with a part of math.', 'Pascal didn\'t understand why he had to learn graphs.', 'Pascal\'s favorite book was Robin Hood.', 'Pascal did what Manny told him to do.'],
 "이유 ▶ Manny는 Pascal의 개(his dog)이지 책 속 인물이 아니다.\n오답 ▶ {1} struggling with graphs ✔ {2} Why do I need these anyways? ✔ {3} his favorite book, Robin Hood ✔ {4} 눈을 감고 따라 말함 ✔\n수정 ▶ 원본 선택지의 어색한 표현(had a difficulty 등)을 다듬음", [])
# [원Q22]
T.fixed('다음 글의 밑줄 친 부분 중 가리키는 대상이 나머지 넷과 <u>다른</u> 것은?', R, B(
 'Pascal was doing his math homework in his room. ' + CN(1, 'He') + ' was struggling with graphs. ' + CN(2, 'He') + ' put down his pen and picked up his favorite book, Robin Hood. When he was about to open the book, ' + CN(3, 'he') +
 ' heard a voice. He couldn\'t believe ' + CN(4, 'his') + ' eyes. It was his dog, Manny, who was talking! "Close your eyes and repeat after me," said Manny. Pascal closed his eyes and repeated what ' + CN(5, 'he') + ' said.'), None, 5,
 "이유 ▶ ⑤ 따라 말한 것은 'Manny가 한 말' → ⑤ he = Manny. 나머지는 모두 Pascal.\n수정 ▶ 원본 22번은 발문만 있고 지문이 21번에 붙어 있어 지문을 함께 실음", [])
T.render()

# ═══════════════ 2세트 · 본문 ① ② ═══════════════
T = Test('2', '2세트', '본문 ① Pascal의 방 · ② Robin Hood와의 만남', '8과 본문 1~2', NOTICE, H=H)
# [원Q23]
T.flex('다음 글의 내용과 일치하는 것은?', R, B(P1),
 ['Pascal might have fallen asleep and started dreaming.', 'Studying graphs was Pascal\'s favorite part of math.', 'Pascal could easily read and draw graphs.', 'Manny is the only dog in the world that can talk.', 'Pascal refused to repeat what his dog said.'],
 "이유 ▶ 책을 읽다 잠들려고 했고(read himself to sleep), 개가 말을 하는 이상한 일이 일어남 → 잠들어 꿈을 꾸기 시작한 것으로 볼 수 있다.\n오답 ▶ {1}·{2} 그래프로 고생함 {3} 세상에 유일하다는 말은 없음 {4} 따라 말함\n수정 ▶ 원본 ③(as soon as opening the book)은 어법이 틀리고 내용도 부정확해 다시 씀", [('refuse', '거절하다')])
# [원Q24]
T.flex('다음 글의 주제로 가장 적절한 것은?', R, B(P1),
 ['falling asleep in his room and meeting a talking dog', 'how to stay awake in class', 'sleeping in class: do\'s and don\'ts', 'how to motivate students to focus on graphs', 'the history of the book Robin Hood'],
 "이유 ▶ 수학 숙제 중 책을 읽다 잠들려다 말하는 개 Manny를 만난 이야기.\n오답 ▶ {1}·{2} 수업 중 이야기가 아님 {3} 동기 부여 방법이 아님 {4} 책의 역사 – 언급 없음", [])
# [원Q25]
T.flex('다음 글을 읽고 답할 수 <u>없는</u> 질문은?', R, B(P1),
 ['Why did Manny ask Pascal to repeat the words?', 'Who is Manny?', 'Where was Pascal?', 'What was Pascal doing?', "What is Pascal's favorite book?"],
 "이유 ▶ Manny가 왜 따라 말하라고 했는지는 나오지 않는다.\n오답 ▶ {1} 그의 개 {2} 그의 방 {3} 수학 숙제 {4} Robin Hood\n수정 ▶ 원본의 오타(Pacal)를 고침", [])
# [원Q26]
T.flex('다음 글에 드러난 Pascal의 심경 변화로 가장 적절한 것은?', R, B(P1),
 ['frustrated → surprised', 'excited → bored', 'relieved → worried', 'proud → ashamed', 'calm → angry'],
 "이유 ▶ 그래프가 너무 어렵다며 짜증을 냄(frustrated) → 개가 말을 해서 자기 눈을 믿을 수 없음(surprised).\n오답 ▶ {1} 신났다가 지루함 {2} 안도했다가 걱정 {3} 자랑스러웠다가 부끄러움 {4} 침착했다가 화남\n수정 ▶ 원본 정답 'tedious → curious'의 tedious(지루한)는 사람의 기분이 아니라 일을 꾸미는 말이라 선택지를 새로 만듦", [('frustrated', '짜증 난, 좌절한'), ('surprised', '놀란')])
# [원Q27 서술형 → 객관식]
T.flex('밑줄 친 문장과 의미가 같은 것은?', R, B('"<u>It\'s too hard to read and draw graphs.</u> Why do I need these anyways?"'),
 ["It's so hard that I can't read and draw graphs.", "It's so hard that I can read and draw graphs.", "It's hard enough to read and draw graphs.", "It's not hard to read and draw graphs.", "It's so hard to read and draw graphs that I can."],
 "이유 ▶ too ~ to = so ~ that ~ can't(너무 어려워서 읽고 그릴 수 없다).\n오답 ▶ {1}·{4} 긍정 {2} enough to는 '할 수 있다' {3} 반대 의미\n수정 ▶ 원본 27번은 'he'로 바꿔 쓰게 했지만 말하는 사람이 Pascal 자신이라 I로 고치고 객관식으로 바꿈", [])
# [원Q28 서술형 → 객관식]
T.flex('밑줄 친 these가 가리키는 것으로 알맞은 것은?', R, B('"It\'s too hard to read and draw graphs. Why do I need <u>these</u> anyways? No one needs graphs in real life."'),
 ['reading and drawing graphs', 'his math homework books', 'his pens', 'the words Manny said', 'his favorite books'],
 "이유 ▶ 바로 앞 문장의 '그래프 읽고 그리기'가 왜 필요하냐고 불평하는 말.\n수정 ▶ 원본 28번(주관식)을 객관식으로 바꿈", [])
# [원Q19 서술형 → 객관식]
T.flex('밑줄 친 부분과 의미가 같은 것은?', R, B('When <u>he was about to open the book</u>, he heard a voice.'),
 ['he was on the point of opening the book', 'he was used to opening the book', 'he was tired of opening the book', 'he had already opened the book', 'he was afraid of opening the book'],
 "이유 ▶ be about to + 동사원형 = be on the point of -ing = 막 ~하려던 참이다.\n오답 ▶ {1} ~에 익숙하다 {2} ~에 싫증 나다 {3} 이미 열었다 {4} ~을 두려워하다\n수정 ▶ 원본 19번(주관식)을 객관식으로 바꿈", [('be about to', '막 ~하려고 하다')])
# [원Q30]
T.flex("Why couldn't Pascal believe his eyes?", R, B(P1),
 ['Because his dog Manny was talking like a person.', 'Because his lost dog came back home.', 'Because he met his favorite story character.', "Because he couldn't understand some Latin words.", "Because he couldn't read and draw graphs."],
 "이유 ▶ It was his dog, Manny, who was talking! → 개가 말을 하고 있었다.\n오답 ▶ {1} 잃어버린 개 – 언급 없음 {2} Robin Hood는 아직 안 나옴 {3}·{4} 눈을 믿지 못한 이유가 아님", [])
# [원Q31]
T.flex('다음 글의 내용과 일치하지 <u>않는</u> 것은?', R, B(P2),
 ['Robin Hood kidnapped Pascal in the woods.', 'Some soldiers were riding on horses.', 'A man was being chased by some soldiers.', 'Pascal rode the same horse as the man being chased.', 'Robin Hood wondered why Pascal was there.'],
 "이유 ▶ 위험하다며 Pascal을 말에 태워 구해 준 것 → 납치(kidnap)가 아니다.\n오답 ▶ {1} soldiers on horses ✔ {2} chasing a man ✔ {3} pulled Pascal onto his horse ✔ {4} why are you here? ✔", [('kidnap', '납치하다'), ('chase', '뒤쫓다')])
# [원Q33]
T.flex('다음 글에 드러난 Pascal의 심경 변화로 가장 적절한 것은?', R, B(P2),
 ['scared → amazed', 'bored → angry', 'excited → disappointed', 'calm → lonely', 'proud → nervous'],
 "이유 ▶ 군인들이 쫓아오는 위험한 상황(scared) → '와! 책 속의 Robin Hood예요?'(amazed).\n오답 ▶ {1} 지루함 – 위험한 상황과 맞지 않음 {2} 실망 – 반대 {3} 외로움 – 언급 없음 {4} 자랑스러움 – 언급 없음\n수정 ▶ 원본 선택지(urgent, pressing 등)는 사람의 심경이 아니라 상황을 꾸미는 말이라 새로 만듦", [('amazed', '깜짝 놀란')])
# [원Q35]
T.flex('다음 글의 내용과 일치하는 것은?', R, B(P2),
 ['Robin Hood wanted to protect Pascal from a dangerous situation.', 'Pascal closed his eyes when he met soldiers on horses.', 'Robin Hood was chasing soldiers on horses in the woods.', 'When they arrived at a house, both of them got on the horse.', 'Robin Hood already knew about Pascal.'],
 "이유 ▶ '거기 서 있으면 너무 위험해, 어서 와' → 말에 태워 숲으로 데려감.\n오답 ▶ {1} 눈을 뜨자 군인들이 보임 {2} 쫓긴 쪽이 Robin Hood {3} 내렸다(got off) {4} 누구냐고 물음", [])
# [원Q36]
T.flex('다음 글의 제목으로 가장 적절한 것은?', R, B(P2),
 ['Unexpected Encounter with Robin Hood in a Forest', 'Struggle against the Enemy in the Woods', 'The Reason Pascal Went to the Woods', 'How to Avoid Accidents while Riding Horses', 'Robin Hood Becomes a Soldier'],
 "이유 ▶ 갑자기 숲에서 Robin Hood를 우연히 만나는 장면.\n오답 ▶ {1} 싸움 장면 없음 {2} 이유는 모름(why are you here?) {3}·{4} 언급 없음", [('encounter', '(우연한) 만남')])
# [원Q37]
T.flex('다음 글의 빈칸에 들어갈 말로 가장 적절한 것은?', R, B('They were chasing a man with arrows in his hand. The man saw Pascal and shouted. "It\'s ' + BL + '. Come on." The man pulled Pascal onto his horse and rode into the woods.'),
 ['too dangerous for you to stand there', 'good to see you here in the woods', 'safe for you to stay here in the forest', 'been a long time since we met before', 'a long way for us to go together'],
 "이유 ▶ 군인들이 쫓아옴 + Come on(어서 와) → 거기 서 있기에는 너무 위험해.\n오답 ▶ {1} 반가운 인사 {2} 안전하다 – 반대 {3} 처음 만남 {4} 흐름과 무관", [])
# [원Q38]
T.fixed('다음 글의 밑줄 친 ①~⑤ 중 어법상 <u>틀린</u> 것은?', R, B(
 'Suddenly, he heard men ' + CN(1, 'shouting') + '. When he opened his eyes, he saw soldiers on horses. They were chasing a man with arrows in his hand. The man saw Pascal and ' + CN(2, 'shouting') + '. "It\'s too dangerous for you to stand there. Come on." The man pulled Pascal onto his horse and ' +
 CN(3, 'rode') + ' into the woods. When they ' + CN(4, 'arrived') + ' at a house, the man stopped and ' + CN(5, 'got off') + ' his horse.'), None, 2,
 "이유 ▶ 과거 동사 saw와 and로 나란히 → shouted.\n오답 ▶ ① 지각동사 hear + 목적어 + -ing ✔ ③ ride의 과거 ✔ ④ arrive at(~에 도착하다) ✔ ⑤ 말에서 내렸다 ✔\n수정 ▶ 원본은 37번 지문에 밑줄이 섞여 있어 따로 정리", [])
# [원Q39]
T.flex('(A), (B), (C)의 각 괄호 안에서 문맥에 맞는 낱말로 가장 적절한 것은?', R, B('Suddenly, he heard men (A) [shouting / sleeping]. When he opened his eyes, he saw soldiers on horses. They were (B) [chasing / choosing] a man with arrows in his hand. ... The man (C) [pulled / pushed] Pascal onto his horse and rode into the woods.'),
 ['shouting − chasing − pulled', 'sleeping − chasing − pushed', 'sleeping − choosing − pulled', 'shouting − choosing − pushed', 'sleeping − chasing − pulled'],
 "이유 ▶ (A) 소리를 들음 → 외치는 (B) 군인들이 한 남자를 → 뒤쫓는 (C) 말 위로 → 끌어당겼다\n오답 ▶ choose(고르다), push(밀다)는 문맥에 맞지 않음", [])
# [원Q43]
T.flex('주어진 글 다음에 이어질 대화의 순서로 가장 적절한 것은?', R, B('When they arrived at a house, the man stopped and got off his horse.') + '\n' + BOX('<b>(A)</b> "Hello, my name is Robin Hood."<br><b>(B)</b> "No, I\'m the Robin Hood of Sherwood Forest. Who are you and why are you here?"<br><b>(C)</b> "Wow! Are you the Robin Hood from the book?"'),
 ['(A) − (C) − (B)', '(C) − (A) − (B)', '(C) − (B) − (A)', '(B) − (C) − (A)', '(B) − (A) − (C)'],
 "이유 ▶ (A) 자기소개 → (C) 책 속의 Robin Hood예요? → (B) 아니, Sherwood 숲의 Robin Hood야.\n포인트 ▶ (B)의 No는 (C)의 질문에 대한 대답", [])
# [원Q44]
T.flex('밑줄 친 문장과 의미가 같도록 빈칸에 알맞은 것은?', G, B('<u>When he opened his eyes, he saw soldiers on horses.</u>', '= ' + BL + ' his eyes, he saw soldiers on horses.'),
 ['Opening', 'He opened', 'He opening', 'Did he open', 'Had opening'],
 "이유 ▶ 접속사와 주어를 빼고 동사를 -ing로 바꾼 분사구문 → Opening his eyes.\n오답 ▶ {1} 접속사 없이 절이 두 개 {2}·{4} 형태 오류 {3} 의문문 형태", [])
# [원Q46]
T.fixed('다음 글의 밑줄 친 부분 중 어법상 가장 어색한 것은?', R, B(
 'Suddenly, he heard men ' + CN(1, 'shouting') + '. When he opened his eyes, he saw soldiers on horses. They were chasing a man with arrows in ' + CN(2, 'their') + ' hand. The man saw Pascal and ' + CN(3, 'shouted') + '. "It\'s too dangerous ' +
 CN(4, 'for') + ' you to stand there. Come on." The man pulled Pascal onto his horse and ' + CN(5, 'rode') + ' into the woods.'), ['shouting', 'their', 'shouted', 'for', 'rode'], 2,
 "이유 ▶ 화살을 든 것은 a man(단수) → his hand.\n오답 ▶ ① hear + 목적어 + -ing ✔ ③ saw와 병렬 ✔ ④ 의미상 주어 for + 목적격 ✔ ⑤ ✔", [])
# [원Q47]
T.fixed('글의 흐름으로 보아, 주어진 문장이 들어갈 위치로 가장 적절한 곳은?', R, B('The man saw Pascal and shouted.') + '\n' + B(
 'Suddenly, he heard men shouting.' + GP(1) + 'When he opened his eyes, he saw soldiers on horses.' + GP(2) + 'They were chasing a man with arrows in his hand.' + GP(3) + '"It\'s too dangerous for you to stand there. Come on."' + GP(4) +
 'The man pulled Pascal onto his horse and rode into the woods.' + GP(5) + 'When they arrived at a house, the man stopped and got off his horse.'), None, 3,
 "이유 ▶ 화살을 든 한 남자(a man) → 그 남자(The man)가 Pascal을 보고 외쳤다 → 외친 말 '너무 위험해, 어서 와'.\n포인트 ▶ a man(처음) → The man(두 번째), shouted 뒤에 따옴표 속 말", [])
# [원Q48]
T.fixed('다음 글의 밑줄 친 부분 중 가리키는 대상이 나머지 넷과 <u>다른</u> 것은?', R, B(
 'They were chasing a man with arrows in his hand. ' + CN(1, 'The man') + ' saw Pascal and shouted. "It\'s too dangerous for ' + CN(2, 'you') + ' to stand there. Come on." The man pulled Pascal onto ' + CN(3, 'his') +
 ' horse and rode into the woods. When they arrived at a house, the man stopped and got off his horse. "Hello, my name is Robin Hood." "Wow! Are ' + CN(4, 'you') + ' the Robin Hood from the book?" "No, ' + CN(5, 'I') + '\'m the Robin Hood of Sherwood Forest."'), None, 2,
 "이유 ▶ ② you = Pascal. 나머지 ①·③·④·⑤는 모두 Robin Hood.", [])
T.render()

# ═══════════════ 3세트 · 본문 ② ③ ═══════════════
T = Test('3', '3세트', '본문 ② · ③ 왕에게서 돈 되찾기', '8과 본문 2~3', NOTICE, H=H)
# [원Q41 서술형 → 객관식]
T.flex('밑줄 친 문장과 의미가 같은 것은?', R, B('The man saw Pascal and shouted. "<u>It\'s too dangerous for you to stand there.</u> Come on."'),
 ["It's so dangerous that you can't stand there.", "It's so dangerous that you can stand there.", "It's dangerous enough for you to stand there.", "It's so dangerous that you couldn't stand there.", "It's too dangerous that you can't stand there."],
 "이유 ▶ too ~ for 목적격 to = so ~ that 주어 can't (현재).\n오답 ▶ {1} 긍정 {2} 반대 의미 {3} 시제 {4} too ~ that ❌\n수정 ▶ 원본 40·41번(같은 문제, 주관식)을 하나로 합쳐 객관식으로 바꿈", [])
# [원Q45 서술형 → 객관식]
T.flex('두 문장의 의미가 같도록 빈칸에 알맞은 것은?', G, B('They were chasing a man with arrows in his hand.', '= They were chasing a man ' + BL + ' arrows in his hand.'),
 ['who had', 'which had', 'who has', 'whom had', 'what had'],
 "이유 ▶ with(~을 가진) = 주격 관계대명사 + have. 선행사 a man(사람), 과거 시제 → who had.\n오답 ▶ {1} which는 사물 {2} 시제 {3} whom은 목적격 {4} what은 선행사 없음\n수정 ▶ 원본 45번(주관식)을 객관식으로 바꿈", [])
# [원Q49 서술형 → 객관식]
T.flex('다음 우리말을 영어로 바르게 옮긴 것은?', R, B('그들은 손에 화살을 들고 있는 한 남자를 뒤쫓고 있었다.'),
 ['They were chasing a man with arrows in his hand.', 'They were chasing with arrows a man in his hand.', 'They were chased a man with arrows in his hand.', 'They chasing a man with arrows in his hand.', 'They were chasing a man in arrows with his hand.'],
 "이유 ▶ 과거진행 were chasing + a man with arrows in his hand(손에 화살을 든 남자).\n수정 ▶ 원본 49번(배열 서술형)을 객관식으로 바꿈", [('arrow', '화살')])
# [원Q50 서술형 → 객관식]
T.flex('다음 영영풀이에 해당하는 단어로, 본문에 쓰인 것은?', R, B('[영영풀이] a weapon that is like a long, thin stick with a sharp point at one end and often feathers at the other'),
 ['arrow', 'horse', 'sword', 'pen', 'tower'],
 "이유 ▶ 한쪽 끝은 뾰족하고 다른 쪽에 깃털이 있는 길고 가는 막대 같은 무기 = 화살(arrow).\n오답 ▶ {1} 말 {2} 칼 – 본문에 없음 {3} 펜 – 무기가 아님 {4} 탑\n수정 ▶ 원본 50번(주관식)을 객관식으로 바꿈", [('weapon', '무기'), ('feather', '깃털')])
# [원Q54]
T.flex('Which of the following is NOT true about the passage?', R, B(P3),
 ['Robin Hood wanted to get back his own money from the king.', 'Pascal has no idea why he is here.', 'Pascal is grateful to the man for saving him from the soldiers.', 'The king was so greedy that he didn\'t share with his people.', 'The people don\'t have enough money to buy food.'],
 "이유 ▶ Robin Hood가 되찾으려는 돈은 왕이 '백성에게서' 빼앗은 돈 → 자기 돈이 아니다.\n오답 ▶ {1} I don't know why I'm here ✔ {2} You saved me ~ Thank you ✔ {3} too greedy to share ✔ {4} don't have enough money to buy food ✔\n수정 ▶ 원본 ②③의 틀린 문장과, 본문에 없는 내용(가족 부양)이 든 ⑤ 때문에 답이 애매해 선택지를 다시 만듦", [('grateful', '고마워하는')])
# [원Q55]
T.flex('What did Robin Hood ask Pascal to do?', R, B(P3),
 ['to help him get back the money from the king', 'to save him from the soldiers', 'to help the king tax his people', 'to become a soldier in the tower', 'to attack the king at night'],
 "이유 ▶ can you help us get back the money that the king took from the people?\n오답 ▶ {1} 구해 준 쪽은 Robin Hood {2} 반대 {3}·{4} 언급 없음\n수정 ▶ 원본 발문 'What was I asked to do?'를 분명하게 바꿈", [])
# [원Q56]
T.flex('빈칸 (A), (B)에 들어갈 말로 가장 적절한 것은?', R, B('He taxed them too much. He is too <b>(A)</b> ' + BL + ' to share with the people, so they don\'t have enough money to buy food. ... "Hmm... I think I have a <b>(B)</b> ' + BL + '. But first, can you take me to the tower?"'),
 ['greedy − solution', 'ambitious − solution', 'ambitious − problem', 'greedy − problem', 'generous − difficulty'],
 "이유 ▶ (A) 세금을 너무 많이 걷고 나누지 않음 → 욕심 많은 (B) 탑에 데려가 달라, 군인 수를 세야 해 → 해결책이 있다\n오답 ▶ ambitious(야망 있는), generous(너그러운) / problem, difficulty(문제)는 '방법이 있다'는 흐름과 반대", [('greedy', '욕심 많은'), ('solution', '해결책')])
# [원Q57]
T.flex('(A), (B), (C)의 각 괄호 안에서 문맥에 맞는 낱말로 가장 적절한 것은?', R, B('"Well, can you help us (A) [get back / deposit] the money that the king took from the people? He taxed them too much. He is too (B) [greedy / generous] to share with the people ... " "Hmm... I think I have a (C) [solution / trouble]."'),
 ['get back − greedy − solution', 'deposit − generous − solution', 'deposit − greedy − solution', 'deposit − greedy − trouble', 'get back − generous − trouble'],
 "이유 ▶ (A) 빼앗긴 돈을 → 되찾다 (B) 나누지 않음 → 욕심 많은 (C) 해결책\n오답 ▶ deposit(예금하다), generous(너그러운), trouble(골칫거리)", [('deposit', '예금하다')])
# [원Q58]
T.flex('밑줄 친 to buy와 쓰임이 같은 것은?', G, B('They don\'t have enough money <u>to buy</u> food.'),
 ['I know a lot of fun stories to tell the kids.', 'His advice was to send an e-mail to the teacher.', 'Tom asked Cindy to take care of his dog.', 'I want to have true friends.', 'I was delighted to find the frog alive.'],
 "이유 ▶ to buy가 money를 꾸밈(음식을 살 돈) = 형용사적 용법. to tell도 stories를 꾸밈.\n오답 ▶ {1} 보어 – 명사적 {2} 목적격 보어 {3} 목적어 – 명사적 {4} 감정의 원인 – 부사적", [])
# [원Q59]
T.flex('밑줄 친 to share와 to부정사의 쓰임이 같은 것은?', G, B('He is too greedy <u>to share</u> with the people.'),
 ["I'm going to the market to buy some cheese and milk.", 'He agreed to join our club.', 'The only way to get there is to take a subway.', 'What I want is to pass the exam.', 'I have a lot of homework to do.'],
 "이유 ▶ too ~ to의 to share는 부사적 용법. to buy(사기 위해)도 부사적 용법(목적).\n오답 ▶ {1} 목적어 – 명사적 {2} way를 꾸밈 – 형용사적 {3} 보어 – 명사적 {4} homework를 꾸밈 – 형용사적\n수정 ▶ 원본 ④ 'Not a star was to be seen'(be to 용법)을 쉬운 형용사적 용법 문장으로 바꿈", [])
# [원Q60]
T.flex('밑줄 친 to share와 to부정사의 쓰임이 <u>다른</u> 것은?', G, B('He is too greedy <u>to share</u> with the people.'),
 ['You are to hand in the lab report by tomorrow.', 'I dropped by his house to give him the invitation card.', 'I woke up to find that no one was around me.', 'He was depressed to see homeless people.', 'His movie is difficult to understand.'],
 "이유 ▶ be to 용법(~해야 한다) → 부사적 용법이 아님. 나머지는 모두 부사적 용법.\n오답 ▶ {1} 목적 {2} 결과 {3} 감정의 원인 {4} 형용사 수식(~하기에)", [('hand in', '제출하다')])
# [원Q63]
T.fixed('다음 글의 밑줄 친 부분 중 어법상 가장 어색한 것은?', R, B(
 '"My name is Pascal. ' + CN(1, 'I don\'t know why I\'m here, but there must be a reason') + '. You saved me from the soldiers. Thank you so much. ' + CN(2, 'Is there anything I can do for you?') + '" "Well, ' +
 CN(3, 'can you help us get back the money that the king took from the people?') + ' He taxed them too much. ' + CN(4, 'He is too greedy to share with the people, they don\'t have enough money to buy food') + '. I want to help them get their money back. However, ' +
 CN(5, 'there are many soldiers in the tower, so no one can get inside') + '."'), None, 4,
 "이유 ▶ 절이 두 개(He is ~ / they don't have ~)인데 이어 주는 접속사가 없다 → ~ with the people, so they don't have ~.\n오답 ▶ ① 간접의문문 + must ✔ ② -thing + 주어 + can ✔ ③ help + 목적어 + 동사원형 ✔ ⑤ so로 연결 ✔", [])
# [원Q65]
T.fixed('다음 글의 밑줄 친 부분 중 어법상 가장 어색한 것은?', R, B(
 '"My name is Pascal. I don\'t know ' + CN(1, 'why') + ' I\'m here, but there must be a reason. You saved me from the soldiers. Is there ' + CN(2, 'anything') + ' I can do for you?" "Well, can you help us get back the money ' + CN(3, 'what') +
 ' the king took from the people? He taxed them too much. He is too greedy to share with the people, so they don\'t have enough money ' + CN(4, 'to buy') + ' food. I want to help them ' + CN(5, 'get') + ' their money back."'), ['why', 'anything', 'what', 'to buy', 'get'], 3,
 "이유 ▶ 선행사(the money)가 있으므로 what ❌ → that(which).\n오답 ▶ ① 간접의문문 ✔ ② ✔ ④ money를 꾸미는 to부정사 ✔ ⑤ help + 목적어 + 동사원형 ✔\n포인트 ▶ what = the thing which (선행사 포함)", [])
# [원Q66]
T.fixed('다음 글의 밑줄 친 문장 중 어법상 가장 어색한 것은?', R, B(
 '"My name is Pascal. I don\'t know why I\'m here, but there must be a reason. ' + CN(1, 'You saved me from the soldiers') + '. Thank you so much." "Well, ' + CN(2, 'can you help us get back the money that the king took from the people?') + ' He taxed them too much. ' +
 CN(3, 'He is too greedy to share with the people') + ', so they don\'t have enough money to buy food. However, ' + CN(4, 'there are many soldiers in the tower, so no one can get to inside') + '." "Hmm... But first, can you take me to the tower? ' + CN(5, 'I need to count the number of soldiers') + '."'), None, 4,
 "이유 ▶ inside(안으로)는 부사 → 앞에 전치사 to가 필요 없다: get inside.\n오답 ▶ ①·②·③·⑤ 본문 그대로 ✔\n포인트 ▶ go home, go inside, go abroad (to ❌)", [])
# [원Q67]
T.fixed('다음 글의 밑줄 친 문장 ①~⑤ 중 어법상 가장 어색한 것은?', R, B(
 '"My name is Pascal. ' + CN(1, 'I don\'t know why I\'m here') + ', but there must be a reason. ' + CN(2, 'Is there anything I can do for you?') + '" "Well, can you help us get back the money that the king took from the people? ' +
 CN(3, 'He is too greedy to share with the people') + ', so they don\'t have enough money to buy food. However, ' + CN(4, 'there are many soldier in the tower, so no one can get inside') + '." "Hmm... I think I have a solution. ' + CN(5, 'I need to count the number of soldiers') + '."'), None, 4,
 "이유 ▶ many + 복수명사 → many soldiers.\n오답 ▶ ①·②·③·⑤ 본문 그대로 ✔", [])
# [원Q68]
T.fixed('다음 글의 밑줄 친 부분 중 어법상 가장 어색한 것은?', R, B(
 '"My name is Pascal. ' + CN(1, 'I don\'t know why I\'m here, but there must be a reason') + '." "Well, ' + CN(2, 'can you help us get back the money that the king took from the people?') + ' He is too greedy to share with the people, ' +
 CN(3, 'so they don\'t have enough money to buy food') + '. However, there are many soldiers in the tower, ' + CN(4, 'so no one can get inside') + '." "Hmm... I think I have a solution. But first, can you take me to the tower? ' + CN(5, 'I need to count a number of soldiers.') + '"'), None, 5,
 "이유 ▶ 군인의 '수'를 세야 한다 → the number of(~의 수). a number of는 '많은'.\n오답 ▶ ①~④ 본문 그대로 ✔\n포인트 ▶ the number of + 복수명사 + 단수 동사 / a number of + 복수명사 + 복수 동사", [])
# [원Q71]
T.fixed('다음 글의 밑줄 친 부분 중 가리키는 대상이 나머지 넷과 <u>다른</u> 것은?', R, B(
 '"My name is Pascal. I don\'t know why ' + CN(1, 'I') + '\'m here, but there must be a reason. Is there anything I can do for you?" "Well, can ' + CN(2, 'you') + ' help us get back the money that the king took from the people? ... ' + CN(3, 'I') +
 ' want to help them get their money back." "Hmm... I think ' + CN(4, 'I') + ' have a solution. But first, can you take ' + CN(5, 'me') + ' to the tower?"'), None, 3,
 "이유 ▶ ③ I = Robin Hood(백성을 돕고 싶은 사람). 나머지는 모두 Pascal.", [])
# [원Q74]
T.fixed('다음 글의 밑줄 친 낱말의 쓰임이 적절하지 <u>않은</u> 것은?', R, B(
 '"You ' + CN(1, 'saved') + ' me from the soldiers. Thank you so much. Is there ' + CN(2, 'anything') + ' I can do for you?" "Well, can you help us ' + CN(3, 'recover') + ' the money that the king took from the people? He taxed them too much. He is too ' +
 CN(4, 'greedy') + ' to share with the people." "Hmm... I think I have a solution. But first, can you take me to the tower? I need to ' + CN(5, 'account') + ' the number of soldiers."'), ['saved', 'anything', 'recover', 'greedy', 'account'], 5,
 "이유 ▶ 군인의 수를 '세다' → count. account는 '계좌, 설명하다'.\n오답 ▶ ① 구하다 ② 무엇이든 ③ 되찾다(= get back) ④ 욕심 많은", [('recover', '되찾다'), ('account', '계좌, 설명(하다)')])
# [원Q75]
T.flex('주어진 글 다음에 이어질 글의 순서로 가장 적절한 것은?', R, B('"... Is there anything I can do for you?"') + '\n' + BOX(
 '<b>(A)</b> "However, there are many soldiers in the tower, so no one can get inside."<br><b>(B)</b> "Hmm... I think I have a solution. But first, can you take me to the tower?"<br><b>(C)</b> "Well, can you help us get back the money that the king took from the people?"<br><b>(D)</b> "I want to help them get their money back."<br><b>(E)</b> "He taxed them too much. He is too greedy to share with the people, so they don\'t have enough money to buy food."'),
 ['(C) − (E) − (D) − (A) − (B)', '(A) − (C) − (B) − (E) − (D)', '(B) − (A) − (D) − (C) − (E)', '(C) − (E) − (A) − (D) − (B)', '(C) − (E) − (D) − (B) − (A)'],
 "이유 ▶ (C) 돈을 되찾게 도와줄래? → (E) 왕이 세금을 너무 많이 걷음 → (D) 백성들이 돈을 되찾게 돕고 싶어 → (A) 하지만 탑에 군인이 많음 → (B) 해결책이 있어\n포인트 ▶ (A)의 However는 (D)의 '돕고 싶다'와 반대되는 어려움", [])
# [원Q72]
T.flex('Which of the following is NOT true about the passage?', R, B(P3),
 ['Robin Hood asked Pascal to take him to the tower.', 'The king took money from the people.', 'The king taxed the people too much.', 'There are many soldiers in the tower.', 'Pascal wants to count the number of soldiers.'],
 "이유 ▶ 탑에 데려가 달라고 부탁한 사람은 Pascal(can you take me to the tower?)이다.\n오답 ▶ {1} the money that the king took from the people ✔ {2} taxed them too much ✔ {3} many soldiers in the tower ✔ {4} I need to count the number of soldiers ✔", [])
T.render()

# ═══════════════ 4세트 · 본문 ③ ④ ═══════════════
T = Test('4', '4세트', '본문 ③ · ④ 그래프로 해결하기', '8과 본문 3~4', NOTICE, H=H)
# [원Q62 서술형 → 객관식]
T.flex('밑줄 친 문장과 의미가 같은 것은?', G, B('He taxed them too much. <u>He is too greedy to share with the people.</u>'),
 ["He is so greedy that he can't share with the people.", 'He is so greedy that he can share with the people.', "He is so greedy that he couldn't share with the people.", 'He is greedy enough to share with the people.', "He is too greedy that he can't share with the people."],
 "이유 ▶ too ~ to = so ~ that 주어 can't (현재 시제 is → can't).\n오답 ▶ {1} 긍정 {2} 시제 {3} 반대 의미 {4} too ~ that ❌\n수정 ▶ 원본 62번(주관식)을 객관식으로 바꿈", [])
# [원Q64 서술형 → 객관식]
T.flex('[ ] 안의 단어를 바르게 배열한 것은?', R, B('He is too greedy to share with the people, so [ don\'t / they / have / money / food / to / buy / enough ].'),
 ["they don't have enough money to buy food", "they don't have money enough food to buy", "they don't have enough food to buy money", "they have don't enough money to buy food", "they don't enough have money to buy food"],
 "이유 ▶ enough + 명사 + to부정사: 음식을 살 충분한 돈.\n수정 ▶ 원본 64번(주관식)을 객관식으로 바꿈", [])
# [원Q69 서술형 → 객관식]
T.flex('다음 우리말을 영어로 바르게 옮긴 것은?', R, B('왕이 백성에게서 빼앗은 돈을 우리가 돌려받을 수 있게 도와줄 수 있겠소?'),
 ['Can you help us get back the money that the king took from the people?', 'Can you help us get back the people that the king took from the money?', 'Can you help the king get back the money that we took from the people?',
  'Can you help us get back the money what the king took from the people?', 'Can you help us got back the money that the king took from the people?'],
 "이유 ▶ help + 목적어(us) + 동사원형(get back) + the money that the king took from the people.\n오답 ▶ {1} 돈과 백성이 뒤바뀜 {2} 도움 받는 사람이 바뀜 {3} 선행사가 있어 what ❌ {4} help + 목적어 + 동사원형\n수정 ▶ 원본 69번(배열 서술형)을 객관식으로 바꿈", [])
# [원Q70 서술형 → 객관식]
T.flex('빈칸에 들어갈 말로, 영영풀이에 해당하는 단어는?', R, B('[영영풀이] wanting a lot more food, money, etc. than you need', '', 'He taxed them too much. He is too ' + BL + ' to share with the people, so they don\'t have enough money to buy food.'),
 ['greedy', 'generous', 'brave', 'lazy', 'honest'],
 "이유 ▶ 필요한 것보다 훨씬 많은 음식·돈 등을 원하는 = 욕심 많은(greedy).\n오답 ▶ {1} 너그러운 {2} 용감한 {3} 게으른 {4} 정직한\n수정 ▶ 원본 70번(주관식)을 객관식으로 바꿈", [])
# [원Q73]
T.flex('다음 글의 내용과 일치하지 <u>않는</u> 것은?', R, B(P3),
 ['Robin Hood는 왕이 빼앗아 간 자신의 재산을 되찾기를 바란다.', 'Pascal은 자신이 왜 이곳에 있는지 모른다.', 'Pascal은 자신을 구해 준 Robin Hood에게 도울 일이 있는지 묻는다.', '왕은 백성에게 세금을 너무 많이 걷었다.', '탑에는 군인이 많아서 아무도 들어갈 수 없다.'],
 "이유 ▶ Robin Hood가 되찾으려는 것은 왕이 '백성에게서' 빼앗은 돈이다.\n오답 ▶ {1} I don't know why I'm here ✔ {2} Is there anything I can do for you? ✔ {3} He taxed them too much ✔ {4} no one can get inside ✔\n수정 ▶ 원본 선택지의 맞춤법(뺏아간 등)과 추측이 섞인 표현을 다듬음", [])
# [원Q76]
T.flex('다음 빈칸에 들어갈 말로 가장 적절한 것은?', R, B('Robin and Pascal hid up in a tree and counted the soldiers ' + BL + '. "There are five soldiers from midnight to six in the morning."'),
 ['one by one', 'one to one', 'less and less', 'more and more', 'little by little'],
 "이유 ▶ 군인을 '한 명씩' 세었다 → one by one.\n오답 ▶ {1} 일대일 {2} 점점 적게 {3} 점점 많이 {4} 조금씩(양이 서서히)", [])
# [원Q77]
T.flex('(A), (B), (C)의 각 괄호 안에서 문맥에 맞는 낱말로 가장 적절한 것은?', R, B('Robin and Pascal hid up in a tree and (A) [counted / accounted] the soldiers one by one. ... So, you should go (B) [inside / outside] between six in the morning and noon." ... Pascal drew a (C) [graph / tower] and showed it to Robin.'),
 ['counted − inside − graph', 'accounted − outside − graph', 'counted − outside − tower', 'counted − inside − tower', 'accounted − inside − tower'],
 "이유 ▶ (A) 군인 수를 세다 → counted (B) 탑 안으로 들어가야 → inside (C) 이해하기 쉽게 → graph", [])
# [원Q78]
T.flex('Why does Pascal tell Robin to go inside between 6 a.m. and noon?', R, B(P4),
 ['Because there are the fewest soldiers at that time.', 'Because there are the most soldiers at that time.', 'Because the soldiers are sleeping at that time.', 'Because Pascal wants to draw a graph.', 'Because Robin Hood likes the morning.'],
 "이유 ▶ 오전 6시~정오에는 군인이 3명으로 가장 적다.\n오답 ▶ {1} 가장 많은 때는 오후 6시~자정(12명) {2}·{3}·{4} 언급 없음", [('fewest', '가장 적은')])
# [원Q79]
T.flex('Which of the following is NOT true about the passage?', R, B(P4),
 ['The most soldiers guard the tower from 6 a.m. till noon.', 'Five soldiers guard the tower from midnight till 6 a.m.', 'Three soldiers guard the tower from 6 a.m. till noon.', 'Eight soldiers guard the tower from noon till 6 p.m.', 'Twelve soldiers guard the tower from 6 p.m. till midnight.'],
 "이유 ▶ 군인이 가장 많은 때는 오후 6시~자정(12명). 오전 6시~정오는 가장 적다(3명).\n수정 ▶ 원본 ⑤(from 6 am till midnight)는 뜻이 애매해 분명한 문장으로 바꿈", [('guard', '지키다')])
# [원Q80]
T.flex('Which of the following is true about the passage?', R, B(P4),
 ['Robin Hood had a chance of not being noticed in the morning shift.', 'Robin Hood clearly understood what Pascal meant at first.', 'Pascal needed a graph to count the soldiers.', 'The number of soldiers is second largest from 6 p.m. till midnight.', 'Robin Hood drew a graph to find the right time.'],
 "이유 ▶ 오전(6시~정오)에는 군인이 가장 적어 들킬 가능성이 가장 낮다.\n오답 ▶ {1} I don't get it(이해 못 함) {2} 그래프는 '설명하려고' 그림 {3} 가장 많음 {4} 그래프를 그린 사람은 Pascal\n수정 ▶ 원본 ④(The morning shift is the least likely to be noticed)는 뜻이 어색해 다듬음", [('shift', '근무 시간대'), ('notice', '알아차리다')])
# [원Q81]
T.flex('다음 빈칸에 들어갈 말로 가장 알맞은 것은?', R, B('"There are five soldiers from midnight to six in the morning. Next, there are three soldiers until noon, and then there are eight soldiers until six in the evening. Lastly, there are twelve soldiers until midnight. So, ' + BL + '" "What? I don\'t get it."'),
 ['you should go inside between six in the morning and noon.', 'you should go inside between six in the evening and midnight.', 'you should go inside between noon and six in the evening.', "you should go inside at 12 o'clock sharp.", 'you should go inside between midnight and six in the morning.'],
 "이유 ▶ 군인이 가장 적은(3명) 오전 6시~정오에 들어가야 한다.\n오답 ▶ {1} 12명 {2} 8명 {3} 근거 없음 {4} 5명", [])
# [원Q82 서술형 → 객관식]
T.flex("밑줄 친 문장에서 'between six in the morning and noon'을 강조한 문장으로 알맞은 것은?", G, B('So, <u>you should go inside between six in the morning and noon.</u>'),
 ['It is between six in the morning and noon that you should go inside.', 'It is you that should go inside between six in the morning and noon.', 'It is between six in the morning and noon what you should go inside.',
  'That is between six in the morning and noon it you should go inside.', 'It is between six in the morning and noon that should you go inside.'],
 "이유 ▶ It is + 강조할 말 + that + 나머지. 강조할 말 = between six in the morning and noon.\n오답 ▶ {1} you를 강조 {2} what ❌ {3} 순서 오류 {4} that 뒤는 평서문 어순\n수정 ▶ 원본 82번(주관식)을 객관식으로 바꿈", [])
# [원Q83]
T.fixed('다음 글의 밑줄 친 문장 ①~⑤ 중 어법상 가장 어색한 것은?', R, B(
 CN(1, 'Robin and Pascal hid up in a tree and counted the soldiers one by one') + '. "' + CN(2, 'There are five soldiers from midnight to six in the morning') + '. ... So, ' + CN(3, 'you should go inside between six in the morning and noon') + '." "What? I don\'t get it." Pascal thought for a moment. \'Hmm... ' +
 CN(4, 'A graph might make this easier to understand') + '.\' ' + CN(5, 'Pascal drew a graph and showed to Robin') + '.'), None, 5,
 "이유 ▶ show는 목적어가 필요 → showed it to Robin.\n오답 ▶ ①~④ 본문 그대로 ✔ (④ make + 목적어 + 형용사)", [])
# [원Q84]
T.flex('밑줄 친 부분의 의미로 가장 적절한 것은?', R, B('So, you should go inside between six in the morning and noon." "What? <u>I don\'t get it.</u>" Pascal thought for a moment.'),
 ["He doesn't understand what Pascal means.", "He couldn't get in the tower.", 'He had never drawn a graph.', "He can't read and draw a graph.", "He doesn't want to fight against them."],
 "이유 ▶ get = 이해하다. I don't get it = 무슨 말인지 모르겠어 → 그래서 Pascal이 그래프를 그려 줌.\n오답 ▶ {1} get(얻다, 들어가다)을 글자 그대로 해석 {2}·{3}·{4} 언급 없음", [])
# [원Q85 서술형 → 객관식]
T.flex('다음 빈칸에 들어갈 말로 가장 알맞은 것은?', R, B('"What? I don\'t get it." Pascal thought for a moment. \'Hmm... A ' + BL + ' might make this easier to understand.\''),
 ['graph', 'sword', 'map', 'ladder', 'book'],
 "이유 ▶ 말로 한 설명을 이해 못 함 → 그래프(graph)로 보여 주면 이해하기 쉽다. 이어서 Pascal drew a graph.\n수정 ▶ 원본 85번(주관식)을 객관식으로 바꿈", [])
# [원Q86]
T.fixed('다음 글의 밑줄 친 부분 중 낱말의 쓰임이 적절하지 <u>않은</u> 것은?', R, B(
 'Robin and Pascal ' + CN(1, 'put themselves out of sight') + ' in a tree and ' + CN(2, 'counted') + ' the soldiers one by one. "There are five soldiers from midnight to six in the morning. Next, there are three soldiers ' + CN(3, 'until') +
 ' noon. ... So, you should go inside ' + CN(4, 'between') + ' six in the morning and noon." "What? I don\'t get it." Pascal thought for a moment. \'Hmm... A graph might make this ' + CN(5, 'harder') + ' to understand.\''),
 ['put themselves out of sight', 'counted', 'until', 'between', 'harder'], 5,
 "이유 ▶ 이해 못 하는 Robin에게 그래프를 보여 준다 → 이해하기 '더 쉽게' → easier.\n오답 ▶ ① 몸을 숨겼다(= hid) ② 세었다 ③ ~까지 ④ ~ 사이에", [])
# [원Q87]
T.fixed('다음 글의 밑줄 친 문장 중 어법상 가장 어색한 것은?', R, B(
 CN(1, 'Robin and Pascal hid up in a tree and counted the soldiers one by one') + '. "There are five soldiers from midnight to six in the morning. Next, there are three soldiers until noon, ' + CN(2, 'and then there are eight soldiers until six in the evening') + '. Lastly, there are twelve soldiers until midnight. So, ' +
 CN(3, 'you should go to inside between six in the morning and noon') + '." Pascal thought for a moment. \'Hmm... ' + CN(4, 'A graph might make this easier to understand') + '.\' ' + CN(5, 'Pascal drew a graph and showed it to Robin') + '.'), None, 3,
 "이유 ▶ inside는 부사 → 전치사 to 없이 go inside.\n오답 ▶ ①·②·④·⑤ 본문 그대로 ✔", [])
# [원Q53 서술형 → 객관식]
T.flex('다음 우리말을 [보기]의 단어를 모두 써서 바르게 영작한 것은?', G, B('네가 거기에 서 있는 것은 너무 위험해.', '[보기] there, too, stand, it, for'),
 ["It's too dangerous for you to stand there.", "It's too dangerous of you to stand there.", "It's too dangerous for you stand there.", "It's too dangerous for you to stand it there.", "For you it's too dangerous stand there."],
 "이유 ▶ 가주어 It + too 형용사 + 의미상 주어 for you + 진주어 to stand there.\n오답 ▶ {1} 사람의 성격을 말할 때만 of {2} to 빠짐 {3} it 중복 {4} 어순·to 빠짐\n수정 ▶ 원본 53번(영작 서술형)을 객관식으로 바꿈", [])
# [원Q51]
T.fixed('다음 글의 밑줄 친 부분 중 어법상 <u>틀린</u> 것은?', R, B(
 'He ' + CN(1, 'put down') + ' his pen and picked up his favorite book, Robin Hood. When he ' + CN(2, 'was about to open') + ' the book, he heard a voice. ... Pascal closed his eyes and ' + CN(3, 'repeat') + ' the words. Suddenly, he heard men ' + CN(4, 'shout') +
 '. When he opened his eyes, he saw soldiers on horses. They were ' + CN(5, 'chasing') + ' a man with arrows in his hand.'), ['put down', 'was about to open', 'repeat', 'shout', 'chasing'], 3,
 "이유 ▶ 과거 동사 closed와 and로 나란히 → repeated.\n오답 ▶ ① put의 과거 ✔ ② be about to ✔ ④ 지각동사 hear + 목적어 + 동사원형 ✔ ⑤ 과거진행 ✔\n수정 ▶ 원본 51번은 53번 영작 조건과 52번 빈칸이 한 지문에 섞여 있어 어법 문제만 남김", [])
# [원Q52]
T.flex('다음 빈칸에 들어갈 말로 가장 적절한 것은?', R, B('When they arrived at a house, the man stopped and ' + BL + ' his horse. "Hello, my name is Robin Hood."'),
 ['got off', 'get off', 'took off', 'take off', 'showed off'],
 "이유 ▶ 말에서 '내렸다' → get off의 과거 got off (stopped와 시제 일치).\n오답 ▶ {1}·{3} 현재형 {2} 이륙했다, 벗었다 {4} 뽐냈다", [])
T.render()
