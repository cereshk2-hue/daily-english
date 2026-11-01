from gramcommon import *
# 중3 지학사(민찬규) 7·8과 문법 (11/1)
# 7과: 가정법 과거 · 5형식(make/keep + 목적어 + 목적격보어) → 7과 본문(d2) 뒤
# 8과: too ~ to … · 전체 부정(No one …) → 8과 본문(d4) 뒤
# 근거: Grammar Build Up 객관식 7·8과 유형(선생님 요청: 똑같이 말고 살짝 바꿔서) + 교과서 본문 문장

G7, G8 = [], []

# ═════════ 7과 문법 ① 가정법 과거 기본 ═════════
D = Day('k1', '7과 문법 ① 가정법 과거 기본', 'If + 주어 + 과거형, 주어 + would/could + 동사원형 · 만약 ~라면 …할 텐데')
D.note('개념 ① 가정법 과거', [
    ('If + 주어 + 동사의 과거형 ~, 주어 + would/could/might + 동사원형 …', '만약 ~라면, …할 텐데 (지금 사실과 반대되는 상상)'),
    ('If I lived in a pueblo, I would climb up a ladder to enter my house.', '교과서 7과 · 만약 내가 푸에블로에 산다면, 나는 집에 들어가기 위해 사다리를 오를 것이다.'),
    ('모양은 과거, 뜻은 현재', 'lived는 과거형이지만 "지금 산다면"이라는 현재의 상상이에요.'),
])
D.note('개념 ② 어법 체크', [
    ('be동사는 were', '주어가 I, he, she여도 were: If I were a bird, I would fly to you.'),
    ('주절은 조동사 과거형 + 동사원형', 'would fly ✔ / will fly ✗ / would flew ✗'),
    ('부정', 'If she did not tell lies, ~ / If he were not sick, ~'),
    ('조건문과 구별', 'If I have time, I will help you. (있을 수 있는 일, 조건문)\nIf I had time, I would help you. (지금은 시간이 없음, 가정법)'),
])
D.step(SCARDS(D, '해석 카드', [
    ('If I lived in a pueblo, I would climb up a ladder to enter my house.', '만약 내가 푸에블로에 산다면, 나는 집에 들어가기 위해 사다리를 오를 것이다. (교과서)'),
    ('If I lived in Venice, I would take a gondola to school every morning.', '만약 내가 베니스에 산다면, 나는 매일 아침 곤돌라를 타고 학교에 갈 것이다. (교과서)'),
    ('If unwelcome visitors appeared, I would pull the ladder up.', '만약 반갑지 않은 방문객이 나타난다면, 나는 사다리를 끌어 올릴 것이다. (교과서)'),
    ('What would you do if you lived in the jungle?', '만약 네가 정글에서 산다면 너는 무엇을 할 거니? (교과서)'),
    ('If I were a bird, I would fly to you.', '만약 내가 새라면, 너에게 날아갈 텐데.'),
    ('If I had a lot of money, I would buy a new laptop.', '만약 내가 돈이 많다면, 새 노트북을 살 텐데.'),
    ('If I were you, I would tell her the truth.', '내가 너라면, 그녀에게 사실을 말할 텐데.'),
    ('If he were not sick, he could go to school.', '만약 그가 아프지 않다면, 학교에 갈 수 있을 텐데.')],
    guide='가정법 과거는 "만약 ~라면, …할 텐데"로 해석해요.'))
D.step(TF('개념 확인 T/F', [
    ('가정법 과거는 지금 사실과 반대되는 일을 상상할 때 쓴다.', True, '정답 ▶ T\n이유: If I lived in Venice → 실제로는 베니스에 살지 않아요.'),
    ('If I was a bird, I would fly to you.는 교과서 문법 기준으로 바른 형태이다.', False, '정답 ▶ F\n이유: 가정법 과거의 be동사는 주어와 관계없이 were → If I were a bird'),
    ('If I had a car, I will pick you up.은 바른 문장이다.', False, '정답 ▶ F\n이유: 주절은 조동사 과거형 → I would pick you up'),
    ('If I had a lot of money, I would buy a car.는 "나는 지금 돈이 많지 않다"라는 뜻을 담고 있다.', True, '정답 ▶ T\n이유: 가정법 과거 = 현재 사실의 반대'),
    ('If it rains tomorrow, I will stay at home.은 가정법 과거이다.', False, '정답 ▶ F\n이유: 실제로 일어날 수 있는 일 → 조건문(현재시제 + will)'),
    ('If I lived in a tulou, I would always have friends at home.에서 lived는 과거의 일을 말한다.', False, '정답 ▶ F\n이유: 모양만 과거, 뜻은 "지금 산다면"(현재의 상상)'),
]))
D.step(PICK(D, '어법 선택', [
    ('If I {had|have} some money, I would lend it to you.', '만약 내가 돈이 좀 있다면, 너에게 빌려줄 텐데.', '정답 ▶ had\n이유: 가정법 과거 → if절은 과거형'),
    ('If I were you, I {would|will} apologize to her first.', '내가 너라면, 그녀에게 먼저 사과할 텐데.', '정답 ▶ would\n이유: 주절은 조동사 과거형'),
    ('If you {were|are} not busy, we could go to the movies.', '네가 바쁘지 않다면, 우리는 영화를 보러 갈 수 있을 텐데.', '정답 ▶ were\n이유: 가정법 과거의 be동사 → were'),
    ('If she {were|was} here right now, she would help us.', '만약 그녀가 지금 여기 있다면, 우리를 도와줄 텐데.', '정답 ▶ were\n이유: 주어가 she여도 were (교과서 기준)'),
    ('If I were a bird, I could {fly|flew} to school.', '만약 내가 새라면, 학교에 날아갈 수 있을 텐데.', '정답 ▶ fly\n이유: could + 동사원형'),
    ('If Minsu {worked|works} hard, he would do well in school.', '만약 민수가 열심히 한다면, 학교에서 잘할 텐데.', '정답 ▶ worked\n이유: 가정법 과거 → 과거형'),
    ('If I {didn\'t|don\'t} have any friends, I would be lonely.', '만약 내가 친구가 하나도 없다면, 외로울 텐데.', "정답 ▶ didn't\n이유: 가정법 과거의 부정 → didn't + 동사원형"),
    ('If I lived in Venice, I would {take|took} a gondola to school.', '만약 내가 베니스에 산다면, 곤돌라를 타고 학교에 갈 것이다.', '정답 ▶ take\n이유: would + 동사원형 (교과서 7과)'),
]))
D.step(MC('빈칸 짝 · 해석', [
    ('빈칸 (A), (B)에 알맞은 것은?<br><b>This bike is not mine, so I can\'t lend it to you. If the bike (A)____ mine, I (B)____ it to you.</b>', ['were - could lend', 'was - lend', 'were - can lend', 'had - could lend', 'were - lent'],
     '정답 ▶ were - could lend\n이유: (A) be동사 → were (B) could + 동사원형'),
    ('빈칸 ⓐ, ⓑ에 알맞은 것은?<br>• If Jina ⓐ____ more exercise, she would be healthier.<br>• If Tom ⓑ____ here now, he would help us.', ['did - were', 'does - is', 'were - did', "didn't - am"],
     '정답 ▶ did - were\n이유: ⓐ 일반동사 과거형 did (do exercise 운동하다) ⓑ be동사 → were'),
    ('주어진 문장에서 알 수 있는 것은?' + Q('If I had a lot of time, I would read more books.'), ["I don't have a lot of time.", 'I have a lot of time.', 'I read a lot of books.', 'I will have more time.'],
     "정답 ▶ I don't have a lot of time.\n이유: 가정법 과거 → 지금 사실은 반대(시간이 많지 않다)"),
    ('Mina가 한 말에 대한 설명으로 알맞은 것은?<br><b>Mina says, "If I didn\'t have any friends, I would be lonely."</b>', ['Mina has friends, so she is not lonely.', 'Mina has no friends.', 'Mina is lonely now.', 'Mina wants to have no friends.'],
     '정답 ▶ Mina has friends, so she is not lonely.\n이유: 친구가 없다면 외로울 텐데 → 실제로는 친구가 있고 외롭지 않다'),
]))
D.step(SCR(D, '우리말 → 영어 배열', [
    ('If I lived in Venice, I would take a gondola to school.', '만약 내가 베니스에 산다면, 나는 곤돌라를 타고 학교에 갈 것이다.'),
    ('If I were a bird, I would fly to you.', '만약 내가 새라면, 너에게 날아갈 텐데.'),
    ('What would you do if you lived in the jungle?', '만약 네가 정글에서 산다면 너는 무엇을 할 거니?'),
    ('If I knew his address, I would write to him.', '내가 그의 주소를 안다면, 그에게 편지를 쓸 텐데.'),
]))
G7.append(D.done())

# ═════════ 7과 문법 ② 가정법 ↔ 직설법 · 실전 ═════════
D = Day('k2', '7과 문법 ② 가정법 ↔ 직설법 · 실전', 'As I don\'t ~, I can\'t ~ ↔ If I ~ed, I could ~ · 영작 · 어법')
D.note('개념 · 바꿔 쓰기', [
    ('가정법 과거 → 직설법 현재', '긍정 ↔ 부정, 과거 → 현재\nIf I knew her number, I could call her. = As I don\'t know her number, I can\'t call her.'),
    ('직설법 → 가정법', 'As he is poor, he can\'t buy a car. → If he were not poor, he could buy a car.'),
    ('참고 · 가정법 과거완료', '과거 사실의 반대: If I had known ~, I would have p.p. … (~했더라면 …했을 텐데) — 모양이 달라요!'),
])
D.step(MC('같은 뜻 고르기', [
    ('주어진 문장과 의미가 같은 것은?' + Q("As I don't know her phone number, I can't call her."), ['If I knew her phone number, I could call her.', 'If I knew her phone number, I can call her.', "If I know her phone number, I can't call her.", 'If I had known her phone number, I can call her.'],
     '정답 ▶ If I knew her phone number, I could call her.\n이유: 현재 사실의 반대 → If + 과거, could + 동사원형'),
    ('주어진 문장과 의미가 같은 것은?' + Q('If he were not busy, he could go to the concert.'), ["He is busy, so he can't go to the concert.", "He was busy, so he couldn't go to the concert.", "He isn't busy, but he can't go to the concert.", 'He is busy, so he can go to the concert.'],
     "정답 ▶ He is busy, so he can't go to the concert.\n이유: 가정법 과거 → 현재 사실: 바쁘다(긍정), 갈 수 없다(부정)\n오답 ▶ was/couldn't(과거 ✗)"),
    ('주어진 문장과 의미가 같은 것은?' + Q("Kevin doesn't join the band because he doesn't sing well."), ['If Kevin sang well, he would join the band.', 'If Kevin sings well, he would join the band.', "If Kevin sang well, he wouldn't join the band.", "If Kevin doesn't sing well, he wouldn't join the band."],
     '정답 ▶ If Kevin sang well, he would join the band.\n이유: 노래를 못한다 → 잘한다면 / 가입 안 한다 → 가입할 텐데'),
    ('가정법 문장을 직설법으로 바르게 바꾼 것은?' + Q('If she had a key, she could open the door.'), ["She doesn't have a key, so she can't open the door.", "She has a key, so she couldn't open the door.", "She didn't have a key, so she couldn't open the door.", "She doesn't have a key, so she doesn't open the door."],
     "정답 ▶ She doesn't have a key, so she can't open the door.\n이유: 현재 · 반대(열쇠가 없다, 열 수 없다)"),
]))
D.step(MC('우리말 → 영어', [
    ('우리말을 바르게 영작한 것은?<br><b>만약 지금 그가 여기 있다면, 그가 나를 도와줄 텐데.</b>', ['If he were here right now, he would help me.', 'If he is here right now, he will help me.', 'If he was here right now, he will help me.', 'If he had been here right now, he would have helped me.'],
     '정답 ▶ If he were here right now, he would help me.\n오답 ▶ 조건문 / 주절 will ✗ / 과거완료(과거 사실의 반대)는 right now와 맞지 않아요'),
    ('우리말을 바르게 영작한 것은?<br><b>나에게 남동생이 있다면, 내 게임기를 빌려줄 텐데.</b>', ['If I had a brother, I would lend him my game machine.', 'If I have a brother, I would lend him my game machine.', 'If I had a brother, I will lend him my game machine.', 'If I have had a brother, I will lend him my game machine.'],
     '정답 ▶ If I had a brother, I would lend him my game machine.'),
    ('다음 상황에서 Sue가 할 말로 알맞은 것은?<br><b>Sue wants to text Steven, but she can\'t because she doesn\'t know his number.</b>', ['I would text him if I knew his number.', "I'll text him if I will know his number.", 'If I know his number, I could text him.', "If I didn't know his number, I didn't text him."],
     '정답 ▶ I would text him if I knew his number.\n이유: 번호를 모른다(현재) → 안다면 문자할 텐데'),
]))
D.sent('If I knew her phone number, I could call her.', '내가 그녀의 전화번호를 안다면, 그녀에게 전화할 수 있을 텐데.'); D.sent('If Kevin sang well, he would join the band.', 'Kevin이 노래를 잘한다면, 밴드에 가입할 텐데.')
D.sent('If he were here right now, he would help me.', '만약 지금 그가 여기 있다면, 그가 나를 도와줄 텐데.'); D.sent('I would text him if I knew his number.', '내가 그의 번호를 안다면, 그에게 문자를 보낼 텐데.')
D.step(MC('어법 · 개수', [
    ('어법상 <b>옳은</b> 문장은?', ['Steven would get a perfect score if he studied harder.', 'If I loved your sister, I will marry her.', 'If he won the lottery, he can buy a house.', 'What you would say if you are my brother?'],
     '정답 ▶ Steven would get a perfect score if he studied harder.\n오답 ▶ will → would / can → could / What would you say if you were ~?'),
    ('어법상 <b>어색한</b> 문장은?', ['If I had a car, I picked you up.', 'If I were you, I would tell her honestly.', "She would be sad if I didn't go to her party.", 'I would go to Mars if I could travel in space.'],
     '정답 ▶ If I had a car, I picked you up.\n이유: 주절 → would pick you up'),
    ('어법상 옳은 문장의 개수는?<br>• If it was sunny, we would go on a picnic.<br>• If I had two bikes, I would gave you one.<br>• If I had an umbrella, I would go out in the rain.<br>• If I were you, I would exercise harder.<br>• If I spend my whole day reading, what would happen?', ['2개', '1개', '3개', '4개', '5개'],
     '정답 ▶ 2개\n틀린 것 ▶ was → were / would gave → would give / spend → spent', True),
]))
D.step(ERR(D, '오류 찾기', [
    ('If a dog [[runs]] after me, I [[would]] run [[away]] [[quickly]].', 0, 'ran', '만약 개가 나를 쫓아온다면, 나는 빨리 도망갈 텐데.', '정답 ▶ runs → ran\n이유: 주절 would → 가정법 과거 → if절은 과거형'),
    ('If he [[had]] enough money, he [[bought]] [[the latest]] [[phone]].', 1, 'would buy', '만약 그가 돈이 충분하다면, 최신 휴대폰을 살 텐데.', '정답 ▶ bought → would buy\n이유: 주절은 조동사 과거형 + 동사원형'),
    ('If I [[know]] your address, I [[would]] [[mail]] this letter [[today]].', 0, 'knew', '내가 네 주소를 안다면, 오늘 이 편지를 보낼 텐데.', '정답 ▶ know → knew'),
    ('My friend [[would]] [[be]] very [[upset]] if I [[hitted]] him.', 3, 'hit', '내가 친구를 때린다면 친구는 매우 화가 날 텐데.', '정답 ▶ hitted → hit\n이유: hit의 과거형은 hit'),
]))
G7.append(D.done())

# ═════════ 7과 문법 ③ 5형식 make / keep ═════════
D = Day('k3', '7과 문법 ③ make / keep + 목적어 + 형용사', '~를 …하게 만들다 · ~를 …한 상태로 유지하다 · happy (happily ✗)')
D.note('개념 ① 5형식', [
    ('주어 + 동사 + 목적어 + 목적격보어', '목적격보어가 목적어의 상태를 설명해요.'),
    ('make + 목적어 + 형용사', '~를 …하게 만들다: Music makes us happy.'),
    ('keep + 목적어 + 형용사', '~를 …한 상태로 유지하다: They would keep me cool in summer and warm in winter. (교과서 7과)'),
    ('Living together in one building keeps them safe.', '교과서 7과 · 한 건물에 함께 사는 것은 그들을 안전하게 지켜 준다.'),
])
D.note('개념 ② 어법 체크', [
    ('부사 ✗', 'makes me happily ✗ → happy / keeps the fruit freshly ✗ → fresh'),
    ('감정 형용사', '목적어가 느끼면 -ed: made me bored · excited · interested (boring ✗)'),
    ('목적어는 목적격', 'made she lovely ✗ → her / made they happy ✗ → them'),
    ('동명사 주어는 단수', 'Wearing a helmet keeps them safe. (keep ✗)'),
    ('make + 목적어 + 명사 / 동사원형', 'made her a star (명사) / made me cry (동사원형, 사역)'),
])
D.step(SCARDS(D, '해석 카드', [
    ('They would keep me cool in summer and warm in winter.', '그것들은 여름에는 나를 시원하게, 겨울에는 따뜻하게 유지해 줄 것이다. (교과서)'),
    ('Living together in one building keeps them safe.', '한 건물에 함께 사는 것은 그들을 안전하게 지켜 준다. (교과서)'),
    ('The old Venetians decided to live there to keep themselves safe from invaders.', '옛 베니스인들은 침략자들로부터 자신들을 안전하게 지키기 위해 그곳에 살기로 결정했다. (교과서)'),
    ('The mirrors would make the house almost invisible.', '거울이 집을 거의 보이지 않게 해 줄 것이다. (교과서)'),
    ('Staying home all day makes Tim and Julie bored.', '하루 종일 집에 있는 것은 Tim과 Julie를 지루하게 한다.'),
    ('Wearing warm clothes keeps them warm.', '따뜻한 옷을 입는 것은 그들을 따뜻하게 해 준다.'),
    ('Sad movies always make me cry.', '슬픈 영화는 항상 나를 울게 만든다.'),
    ('The TV show made her a big star.', '그 TV 쇼는 그녀를 큰 스타로 만들었다.')],
    guide='make·keep 뒤 "목적어 + 형용사"는 "~를 …하게"로 해석해요.'))
D.step(PICK(D, '어법 선택', [
    ('Music makes us {happy|happily}.', '음악은 우리를 행복하게 만든다.', '정답 ▶ happy\n이유: 목적격보어 자리 → 형용사'),
    ('The ice box keeps the fruit {fresh|freshly}.', '아이스박스는 과일을 신선하게 유지한다.', '정답 ▶ fresh\n이유: keep + 목적어 + 형용사'),
    ('His long speech made me {bored|boring}.', '그의 긴 연설은 나를 지루하게 만들었다.', '정답 ▶ bored\n이유: 내가 지루함을 느낌 → 과거분사형 형용사 bored'),
    ('The dress made {her|she} lovely.', '그 드레스는 그녀를 사랑스러워 보이게 했다.', '정답 ▶ her\n이유: 목적어 자리 → 목적격'),
    ('Wearing a helmet {keeps|keep} Tim and Julie safe.', '헬멧을 쓰는 것은 Tim과 Julie를 안전하게 해 준다.', '정답 ▶ keeps\n이유: 동명사 주어(Wearing a helmet)는 단수'),
    ('Sad movies always make me {cry|to cry}.', '슬픈 영화는 항상 나를 울게 만든다.', '정답 ▶ cry\n이유: 사역동사 make + 목적어 + 동사원형'),
    ('Please keep me {updated|update} on your progress.', '진행 상황을 계속 알려 주세요.', '정답 ▶ updated\n이유: 내가 소식을 "전달받는" 상태 → 과거분사'),
    ('Jogging every morning makes me {healthy|health}.', '매일 아침 조깅하는 것은 나를 건강하게 만든다.', '정답 ▶ healthy\n이유: 목적격보어 → 형용사'),
]))
D.step(MC('쓰임 구별 · 어법', [
    ('밑줄 친 <i>made</i>의 쓰임이 나머지와 <b>다른</b> 것은?', ['My mom <u>made</u> me cookies.', 'She always <u>makes</u> me happy.', 'Sad movies always <u>make</u> me cry.', 'Eating too much <u>can make</u> you sick.'],
     '정답 ▶ My mom <u>made</u> me cookies.\n이유: "나에게 쿠키를 만들어 주었다"(4형식: 간접목적어 + 직접목적어). 나머지는 "~를 …하게 만들다"(5형식)'),
    ('<보기>의 밑줄 친 부분과 쓰임이 같은 것은?<br><보기> The smell of food <u>made</u> me hungry.', ['Math tests <u>made</u> me worried.', 'She <u>made</u> us all coffee.', 'I <u>make</u> my own clothes.', "I'll <u>make</u> you some sandwiches."],
     '정답 ▶ Math tests <u>made</u> me worried.\n이유: make + 목적어 + 형용사(5형식)\n오답 ▶ 4형식(만들어 주다) / 3형식(만들다)'),
    ('어법상 <b>옳은</b> 것은?', ['Children always make their mother busy.', 'She always makes me happily.', 'The book made her boring.', 'She made they happy.'],
     '정답 ▶ Children always make their mother busy.\n오답 ▶ happily → happy / boring → bored(그녀가 지루함을 느낌) / they → them'),
    ('어법상 <b>어색한</b> 것을 모두 고른 것은?<br>(A) It makes you healthier.<br>(B) The movie makes them sadly.<br>(C) Good friends make people happy.<br>(D) Do you want to make she angry?', ['(B), (D)', '(A), (B)', '(A), (C)', '(C), (D)'],
     '정답 ▶ (B), (D)\n이유: (B) sadly → sad (D) she → her', True),
]))
D.step(SCR(D, '우리말 → 영어 배열', [
    ('They would keep me cool in summer and warm in winter.', '그것들은 여름에는 나를 시원하게, 겨울에는 따뜻하게 유지해 줄 것이다.'),
    ('Living together in one building keeps them safe.', '한 건물에 함께 사는 것은 그들을 안전하게 지켜 준다.'),
    ('His lecture made me bored.', '그의 강의는 나를 따분하게 만들었다.'),
    ('Eating delicious food makes you fatter.', '맛있는 음식을 먹는 것은 너를 더 뚱뚱하게 만든다.'),
]))
G7.append(D.done())

# ═════════ 7과 문법 ④ 종합 ═════════
D = Day('k4', '7과 문법 ④ 가정법 · 5형식 종합', '교과서 7과 문장으로 · 어법 · 개수 세기 · 두 문법 섞어서')
D.note('시험 직전 체크리스트', [
    ('가정법 과거', 'If + 과거형(be → were), would/could + 동사원형 · 뜻은 현재의 반대'),
    ('5형식', 'make/keep + 목적어(목적격) + 형용사(부사 ✗) · 감정은 -ed · 동명사 주어는 단수'),
    ('교과서 7과', 'If I lived in ~, I would ~ / keep me cool / keeps them safe'),
])
D.step(MC('교과서 7과 문장', [
    ('교과서 문장에 대한 설명으로 <b>틀린</b> 것은?<br>ⓐ If I lived in a pueblo, I would climb up a ladder to enter my house.<br>ⓑ They would keep me cool in summer and warm in winter.<br>ⓒ Living together in one building keeps them safe.', ['ⓐ의 lived는 과거에 살았던 일을 나타낸다.', 'ⓐ는 지금 사실과 반대되는 상상이다.', 'ⓑ의 cool, warm은 목적어 me의 상태를 나타낸다.', 'ⓒ의 주어는 동명사구라서 keeps를 썼다.'],
     '정답 ▶ ⓐ의 lived는 과거에 살았던 일을 나타낸다.\n이유: 가정법 과거 → 모양만 과거, "지금 산다면"(현재의 상상)'),
    ('빈칸에 알맞은 것은?<br><b>If unwelcome visitors ______, I would pull the ladder up to stop them from entering.</b>', ['appeared', 'appear', 'will appear', 'have appeared'],
     '정답 ▶ appeared\n이유: 주절 would → 가정법 과거 → if절 과거형 (교과서 7과)'),
    ('빈칸에 알맞은 것은?<br><b>The old Venetians decided to live there to keep ______ safe from invaders.</b>', ['themselves', 'they', 'their', 'them self'],
     '정답 ▶ themselves\n이유: keep의 목적어가 주어 자신 → 재귀대명사 themselves (교과서 7과)'),
]))
D.sent('If unwelcome visitors appeared, I would pull the ladder up to stop them from entering.', '만약 반갑지 않은 방문객이 나타난다면, 나는 그들이 들어오지 못하게 사다리를 끌어 올릴 것이다.')
D.sent('The old Venetians decided to live there to keep themselves safe from invaders.', '옛 베니스인들은 침략자들로부터 자신들을 안전하게 지키기 위해 그곳에 살기로 결정했다.')
D.step(MC('개수 · 짝짓기', [
    ('어법상 옳은 문장끼리 짝지은 것은?<br>ⓐ If I had a robot, I would make it do my homework.<br>ⓑ If there were a flying car, we would not late for school.<br>ⓒ If I saw a famous actor, I would ask him to take a picture with me.<br>ⓓ If I were a poet, I would described this world.<br>ⓔ If I finded a lost wallet, I would take it to the police.', ['ⓐ, ⓒ', 'ⓑ, ⓓ', 'ⓐ, ⓒ, ⓔ', 'ⓐ, ⓑ, ⓒ'],
     '정답 ▶ ⓐ, ⓒ\n틀린 것 ▶ ⓑ would not be late / ⓓ would describe / ⓔ finded → found', True),
    ('어법상 옳은 것을 모두 고른 것은?<br>(A) I helped mom wash the dishes.<br>(B) The movie made me interesting.<br>(C) The cook kept the soup warm.<br>(D) Our manager made us working overnight.<br>(E) The mixed evidence made us confusing.', ['(A), (C)', '(A), (B)', '(B), (C)', '(B), (C), (E)'],
     '정답 ▶ (A), (C)\n틀린 것 ▶ (B) interesting → interested (D) working → work (E) confusing → confused', True),
]))
D.step(MC('가정법 + 5형식 섞어서', [
    ('어법상 <b>옳은</b> 문장은?', ['If I lived in a tulou, living with many people would make me happy.', 'If I live in a tulou, living with many people would make me happy.', 'If I lived in a tulou, living with many people would make me happily.', 'If I lived in a tulou, living with many people will make me happy.'],
     '정답 ▶ If I lived in a tulou, living with many people would make me happy.\n오답 ▶ live → lived / happily → happy / will → would'),
    ('우리말을 바르게 영작한 것은?<br><b>내가 그 집에 산다면, 두꺼운 벽이 나를 따뜻하게 지켜 줄 텐데.</b>', ['If I lived in the house, the thick walls would keep me warm.', 'If I lived in the house, the thick walls would keep me warmly.', 'If I live in the house, the thick walls will keep warm me.', 'If I lived in the house, the thick walls kept me warm.'],
     '정답 ▶ If I lived in the house, the thick walls would keep me warm.\n오답 ▶ warmly ✗ / 조건문 + 어순 ✗ / 주절 kept ✗ (would keep)'),
]))
D.sent('If I lived in a tulou, living with many people would make me happy.', '내가 토루에 산다면, 많은 사람과 함께 사는 것이 나를 행복하게 해 줄 텐데.'); D.sent('If I lived in the house, the thick walls would keep me warm.', '내가 그 집에 산다면, 두꺼운 벽이 나를 따뜻하게 지켜 줄 텐데.')
D.step(ERR(D, '오류 찾기', [
    ('If I [[was]] a famous movie star, I [[might not be]] [[interested]] in [[helping]] others.', 0, 'were', '만약 내가 유명한 영화배우라면, 나는 다른 사람을 돕는 것에 관심이 없을지도 모른다.', '정답 ▶ was → were\n이유: 가정법 과거의 be동사'),
    ('She [[kept]] you [[safely]] [[from]] [[him]].', 1, 'safe', '그녀는 너를 그에게서 안전하게 지켰다.', '정답 ▶ safely → safe\n이유: keep + 목적어 + 형용사'),
    ('This skirt [[makes]] her [[looks]] [[fat]] [[in]] the photo.', 1, 'look', '이 치마는 사진에서 그녀를 뚱뚱해 보이게 한다.', '정답 ▶ looks → look\n이유: 사역동사 make + 목적어 + 동사원형'),
    ('If ocean water [[weren\'t]] salty, people [[drank]] [[it]] [[easily]].', 1, 'would drink', '바닷물이 짜지 않다면, 사람들은 그것을 쉽게 마실 텐데.', '정답 ▶ drank → would drink\n이유: 주절은 조동사 과거형 + 동사원형'),
]))
G7.append(D.done())

# ═════════ 8과 문법 ① too ~ to … ═════════
D = Day('m1', '8과 문법 ① too ~ to … 기본', '너무 ~해서 …할 수 없다 = so ~ that 주어 can\'t')
D.note('개념 ① too ~ to …', [
    ('too + 형용사/부사 + to + 동사원형', '…하기에는 너무 ~하다 = 너무 ~해서 …할 수 없다'),
    ('"It\'s too hard to read and draw graphs."', '교과서 8과 · 그래프를 읽고 그리는 건 너무 어려워.'),
    ('He is too greedy to share with the people.', '교과서 8과 · 그는 너무 욕심이 많아서 백성들과 나누지 않는다.'),
    ('Tuesday will be too rainy to ride our bikes.', '화요일은 비가 너무 와서 자전거를 탈 수 없을 거야.'),
])
D.note('개념 ② 바꿔 쓰기 · 주의', [
    ('= so + 형용사/부사 + that + 주어 + can\'t(couldn\'t)', "He is too tired to go camping. = He is so tired that he can't go camping."),
    ('의미상 주어 for + 목적격', '"It\'s too dangerous for you to stand there." (교과서 8과)'),
    ('목적어 it', "The box was too heavy (for me) to carry. = The box was so heavy that I couldn't carry it."),
    ('not ✗', 'too에 이미 "~할 수 없다"는 뜻: too busy not to eat ✗'),
    ('enough to', '~할 만큼 충분히: He is tall enough to reach it. = so tall that he can reach it.'),
])
D.step(SCARDS(D, '해석 카드', [
    ("It's too hard to read and draw graphs.", '그래프를 읽고 그리는 건 너무 어렵다. (교과서)'),
    ("It's too dangerous for you to stand there.", '네가 거기 서 있는 건 너무 위험하다. (교과서)'),
    ('He is too greedy to share with the people.', '그는 너무 욕심이 많아서 백성들과 나누지 않는다. (교과서)'),
    ('Wednesday will be too snowy to go on a picnic.', '수요일은 눈이 너무 와서 소풍을 갈 수 없을 것이다.'),
    ('Thursday will be too windy to go to Ulleungdo.', '목요일은 바람이 너무 불어서 울릉도에 갈 수 없을 것이다.'),
    ('He is too young to drive a car.', '그는 너무 어려서 운전을 할 수 없다.'),
    ('The shoes are too big for the girl to wear.', '그 신발은 그 소녀가 신기에 너무 크다.'),
    ('She is smart enough to solve the problem.', '그녀는 그 문제를 풀 만큼 충분히 똑똑하다.')],
    guide='too ~ to는 "너무 ~해서 …할 수 없다"로 해석해요.'))
D.step(PICK(D, '어법 선택', [
    ('He was {too|very} excited to fall asleep.', '그는 너무 신이 나서 잠들 수 없었다.', '정답 ▶ too\n이유: 뒤에 to fall → too ~ to'),
    ('He is too young {to drive|driving} a car.', '그는 너무 어려서 운전을 할 수 없다.', '정답 ▶ to drive\n이유: too ~ to + 동사원형'),
    ("It's too dangerous {for|of} you to stand there.", '네가 거기 서 있는 건 너무 위험하다.', '정답 ▶ for\n이유: 의미상 주어 for + 목적격 (교과서 8과)'),
    ('The shoes are too big for {her|she} to wear.', '그 신발은 그녀가 신기에 너무 크다.', '정답 ▶ her\n이유: for 뒤 목적격'),
    ('This water is too dirty to {drink|drink it}.', '이 물은 너무 더러워서 마실 수 없다.', '정답 ▶ drink\n이유: 주어 This water가 drink의 목적어 → it을 또 쓰지 않아요.'),
    ('She is old {enough|too} to watch the movie.', '그녀는 그 영화를 볼 만큼 나이가 들었다.', '정답 ▶ enough\n이유: ~할 만큼 → 형용사 + enough + to'),
    ("The coffee was so hot that I couldn't drink {it|them}.", '커피가 너무 뜨거워서 나는 그것을 마실 수 없었다.', '정답 ▶ it\n이유: so ~ that절에는 목적어 it이 필요해요.'),
]))
D.step(MC('같은 뜻 · 빈칸', [
    ('두 문장이 같은 뜻이 되도록 빈칸에 알맞은 것은?<br><b>Mina is so tired that she can\'t go hiking.<br>= Mina is ______ tired ______ go hiking.</b>', ['too - to', 'enough - to', 'so - to', 'enough - that'],
     "정답 ▶ too - to\n이유: so ~ that 주어 can't = too ~ to"),
    ('빈칸에 들어갈 수 있는 것을 모두 고른 것은?<br><b>My dog is ____________ her three puppies.</b><br>ⓐ too weak to feed ⓑ weak enough to feed ⓒ so weak that she can\'t feed ⓓ strong enough to feed', ['ⓐ, ⓒ, ⓓ', 'ⓐ, ⓑ', 'ⓑ, ⓓ', 'ⓐ, ⓑ, ⓒ, ⓓ'],
     '정답 ▶ ⓐ, ⓒ, ⓓ\n이유: ⓐ 너무 약해서 못 먹임 = ⓒ / ⓓ 먹일 만큼 튼튼함 — 모두 말이 돼요.\n오답 ▶ ⓑ "먹일 만큼 충분히 약하다"는 말이 안 돼요.', True),
    ('주어진 문장과 의미가 같은 것은?' + Q('The box was too heavy for me to move.'), ["The box was so heavy that I couldn't move it.", 'The box was so heavy that I could move it.', 'The box was heavy enough for me to move.', 'The box was so heavy for me to move.'],
     "정답 ▶ The box was so heavy that I couldn't move it."),
    ('의미상 가장 자연스러운 것은?', ['They are too young to get married.', 'The fox is too tall to reach the grapes.', 'Jane is too strong to climb the mountain.', 'He is too rich to buy some bread.'],
     '정답 ▶ They are too young to get married.\n오답 ▶ too short / too weak / too poor라야 말이 돼요.'),
]))
D.sent('Mina is too tired to go hiking.', '미나는 너무 피곤해서 하이킹을 갈 수 없다.'); D.sent('The box was too heavy for me to move.', '그 상자는 너무 무거워서 나는 옮길 수 없었다.')
D.step(SCR(D, '우리말 → 영어 배열', [
    ("It's too hard to read and draw graphs.", '그래프를 읽고 그리는 건 너무 어렵다.'),
    ("It's too dangerous for you to stand there.", '네가 거기 서 있는 건 너무 위험하다.'),
    ('He is too greedy to share with the people.', '그는 너무 욕심이 많아서 백성들과 나누지 않는다.'),
    ('The shoes are too big for the girl to wear.', '그 신발은 그 소녀가 신기에 너무 크다.'),
]))
G8.append(D.done())

# ═════════ 8과 문법 ② too ~ to 실전 ═════════
D = Day('m2', '8과 문법 ② too ~ to 실전', '영작 · 의미가 같은 것/다른 것 · so that(목적)과 구별 · 어법')
D.note('개념 · 헷갈리는 것', [
    ('too ~ to (너무 ~해서 …할 수 없다)', "= so ~ that 주어 can't"),
    ('~ enough to (…할 만큼 충분히 ~하다)', '= so ~ that 주어 can'),
    ('so that 주어 can (~하기 위해)', '목적! so와 that이 붙어 있어요: I got up early so that I could catch the bus.'),
])
D.step(MC('우리말 → 영어', [
    ('우리말을 바르게 영작한 것은?<br><b>그 음식은 너무 뜨거워서 나는 먹을 수 없었다.</b>', ["The food was so hot that I couldn't eat it.", 'The food was so hot to eat it.', "The food was too hot that I couldn't eat.", "The food was too hot to I couldn't eat it."],
     "정답 ▶ The food was so hot that I couldn't eat it."),
    ('우리말을 바르게 영작한 것을 고른 것은?<br><b>그녀는 너무 아파서 학교에 올 수 없다.</b><br>ⓐ She is so sick that she can come to school.<br>ⓑ She is too sick to come to school.<br>ⓒ She is very sick that she can come to school.<br>ⓓ She is so sick that she can\'t come to school.', ['ⓑ, ⓓ', 'ⓐ, ⓑ', 'ⓑ, ⓒ', 'ⓒ, ⓓ'],
     "정답 ▶ ⓑ, ⓓ\n이유: too ~ to = so ~ that 주어 can't", True),
    ('우리말을 바르게 영작한 것은?<br><b>내 방은 너무 작아서 동생과 함께 쓸 수 없다.</b>', ['My room is too small to share with my brother.', 'My room is so small to share with my brother.', 'My room is so small that I can share it with my brother.', 'My room is too small that I can\'t share it with my brother.'],
     '정답 ▶ My room is too small to share with my brother.\n이유: 주어 My room이 share의 목적어 → to share 뒤 it ✗'),
]))
D.sent("The food was so hot that I couldn't eat it.", '그 음식은 너무 뜨거워서 나는 먹을 수 없었다.'); D.sent('My room is too small to share with my brother.', '내 방은 너무 작아서 동생과 함께 쓸 수 없다.')
D.step(MC('의미 비교', [
    ('의미가 나머지 넷과 <b>다른</b> 것은?', ['You are so young that you can see this movie.', 'You are too young to see this movie.', "You are very young, so you can't see this movie.", "You aren't old enough to see this movie.", "Because you are very young, you can't see this movie."],
     '정답 ▶ You are so young that you can see this movie.\n이유: 이것만 "볼 수 있다". 나머지는 "너무 어려서 볼 수 없다"'),
    ('짝지어진 두 문장의 의미가 서로 <b>다른</b> 것은?', ['It was so cold that I stayed home all day. = It was too cold to stay home all day.', 'She studied so hard that she could pass the test. = She studied hard enough to pass the test.', 'He runs every day so that he can stay healthy. = He runs every day to stay healthy.', "It was so hot that I couldn't study. = I couldn't study since it was too hot."],
     '정답 ▶ It was so cold that I stayed home all day. = It was too cold to stay home all day.\n이유: 뒤 문장은 "너무 추워서 집에 있을 수 없었다" → 반대 뜻'),
    ('밑줄 친 부분의 용법이 <b>다른</b> 것은?', ['He worked hard <u>so that</u> his family could live in comfort.', "She was <u>so</u> young <u>that</u> she couldn't enter the contest.", 'The boat rocked <u>so</u> much <u>that</u> I got sick.', "Jinho is <u>so</u> full <u>that</u> he can't eat anymore."],
     '정답 ▶ He worked hard <u>so that</u> his family could live in comfort.\n이유: so that = ~하기 위해(목적)'),
]))
D.step(ERR(D, '오류 찾기', [
    ('I was [[so]] sick [[to]] [[go]] to school [[yesterday]].', 0, 'too', '나는 어제 너무 아파서 학교에 갈 수 없었다.', '정답 ▶ so → too\n이유: so ~ to ✗ → too ~ to'),
    ('He is too [[busy]] [[not]] to [[call]] you [[back]].', 1, '', '그는 너무 바빠서 너에게 다시 전화할 수 없다.', '정답 ▶ not → 삭제\n이유: too ~ to에 이미 부정의 뜻'),
    ('This problem [[is]] too [[difficult]] [[of]] me [[to solve]].', 2, 'for', '이 문제는 내가 풀기에 너무 어렵다.', '정답 ▶ of → for\n이유: 의미상 주어 for + 목적격'),
    ('I am [[too]] tired [[that]] I [[can\'t]] play soccer [[today]].', 0, 'so', '나는 너무 피곤해서 오늘 축구를 할 수 없다.', '정답 ▶ too → so\n이유: too ~ that ✗ → so ~ that'),
]))
G8.append(D.done())

# ═════════ 8과 문법 ③ 전체 부정 ═════════
D = Day('m3', '8과 문법 ③ 전체 부정 No one …', 'No one · Nobody · None · Nothing + 단수 동사 · 부분 부정과 구별')
D.note('개념 ① 전체 부정', [
    ('No one(= Nobody) + 단수 동사', '아무도 …않다: No one lives in the house. / No one knows her name.'),
    ('No one needs graphs in real life.', '교과서 8과 · 실생활에서는 아무도 그래프가 필요 없어.'),
    ('No one can say that we don\'t need them anymore.', '교과서 8과 · 이제 아무도 우리에게 그래프가 더 이상 필요 없다고 말할 수 없어요.'),
    ('none of + 명사', '~ 중 아무도(아무것도) …않다: none of them came'),
    ('nothing', '아무것도 …않다: I know nothing about it.'),
    ('not 같이 쓰지 않기', 'No one doesn\'t ~ ✗ / None of them didn\'t ~ ✗ (이미 부정!)'),
])
D.note('개념 ② 부분 부정과 구별', [
    ('Not all / Not every / not always', '모두(항상) ~한 것은 아니다 (일부는 맞고 일부는 아님)'),
    ('Not all restaurants are clean.', '모든 식당이 깨끗한 것은 아니다. (깨끗한 곳도 있고 아닌 곳도 있음)'),
    ('None of the restaurants are clean.', '어떤 식당도 깨끗하지 않다. (전체 부정)'),
    ('Not every + 단수명사 + 단수동사', 'Not every student passed. (every students ✗)'),
])
D.step(SCARDS(D, '해석 카드', [
    ('No one needs graphs in real life.', '실생활에서는 아무도 그래프가 필요 없다. (교과서)'),
    ('There are many soldiers in the tower, so no one can get inside.', '탑에는 군인들이 많아서 아무도 안으로 들어갈 수 없다. (교과서)'),
    ("No one can say that we don't need them anymore.", '이제 아무도 우리에게 그것들이 더 이상 필요 없다고 말할 수 없다. (교과서)'),
    ('No one lives in the house.', '아무도 그 집에 살지 않는다.'),
    ('No one wears these hats now.', '지금은 아무도 이런 모자를 쓰지 않는다.'),
    ('I invited five people, but none of them came.', '나는 다섯 명을 초대했지만, 그들 중 아무도 오지 않았다.'),
    ('Not all restaurants are clean.', '모든 식당이 깨끗한 것은 아니다.'),
    ("The moon doesn't always look the same.", '달이 항상 같아 보이는 것은 아니다.')],
    guide='No one/Nobody/None은 "아무도 …않다", Not all/every/always는 "모두(항상) ~한 것은 아니다"예요.'))
D.step(PICK(D, '어법 선택', [
    ('No one {knows|know} how the world will change in the future.', '미래에 세상이 어떻게 바뀔지 아무도 모른다.', '정답 ▶ knows\n이유: No one + 단수 동사'),
    ('No one {was|were} home when I called.', '내가 전화했을 때 아무도 집에 없었다.', '정답 ▶ was\n이유: No one은 단수 취급'),
    ('Nobody here {seems|seem} to like me.', '여기 있는 아무도 나를 좋아하지 않는 것 같다.', '정답 ▶ seems\n이유: Nobody + 단수 동사'),
    ('No one {wants|doesn\'t want} to work for him anymore.', '아무도 더 이상 그를 위해 일하고 싶어 하지 않는다.', "정답 ▶ wants\n이유: No one에 이미 부정 뜻 → doesn't ✗"),
    ('Not every {student|students} passed the exam.', '모든 학생이 시험에 합격한 것은 아니다.', '정답 ▶ student\n이유: every + 단수명사'),
    ('I invited five friends, but {none|no one} of them came.', '나는 친구 다섯 명을 초대했지만, 그들 중 아무도 오지 않았다.', '정답 ▶ none\n이유: ~ 중 아무도 → none of (no one of ✗)'),
    ('There are many soldiers, so no one {can|can\'t} get inside.', '군인들이 많아서 아무도 안으로 들어갈 수 없다.', "정답 ▶ can\n이유: no one이 이미 부정 → can (교과서 8과)"),
]))
D.step(MC('전체 부정 vs 부분 부정', [
    ('우리말을 바르게 영작한 것을 모두 고른 것은?<br><b>아무도 회의에 참석하지 않았다.</b><br>ⓐ No one took part in the meeting.<br>ⓑ Not everyone took part in the meeting.<br>ⓒ Nobody took part in the meeting.<br>ⓓ None of them didn\'t take part in the meeting.', ['ⓐ, ⓒ', 'ⓐ, ⓑ', 'ⓑ, ⓓ', 'ⓐ, ⓒ, ⓓ'],
     "정답 ▶ ⓐ, ⓒ\n오답 ▶ ⓑ 부분 부정(모두가 참석한 것은 아니다) / ⓓ didn't를 또 쓰면 ✗", True),
    ('주어진 문장과 의미가 같은 것은?' + Q('Not all restaurants are clean.'), ["Some restaurants are clean, but others aren't.", 'There are no clean restaurants.', 'None of the restaurants are clean.', 'All restaurants are cleaner than you think.'],
     "정답 ▶ Some restaurants are clean, but others aren't.\n이유: 부분 부정 → 깨끗한 곳도 있고 아닌 곳도 있다"),
    ('의미가 나머지 넷과 <b>다른</b> 것은?', ['None of the students came to the party.', 'Not all students came to the party.', 'Not every student came to the party.', "Some students came to the party, and some didn't.", "There were some students who didn't come to the party."],
     '정답 ▶ None of the students came to the party.\n이유: 전체 부정(아무도 안 옴). 나머지는 "일부만 왔다"'),
    ('부정하는 범위가 나머지와 <b>다른</b> 것은?', ['Not all apples are red.', 'None of my friends came.', 'No one found the treasure.', 'There is nothing new about this.', 'Neither answer is correct.'],
     '정답 ▶ Not all apples are red.\n이유: 부분 부정. 나머지는 전체 부정(none, no one, nothing, neither)'),
]))
D.sent('No one took part in the meeting.', '아무도 회의에 참석하지 않았다.'); D.sent('Nobody took part in the meeting.', '아무도 회의에 참석하지 않았다.')
D.sent("Some restaurants are clean, but others aren't.", '어떤 식당은 깨끗하지만 다른 식당은 그렇지 않다.'); D.sent('None of the students came to the party.', '학생들 중 아무도 파티에 오지 않았다.')
D.step(SCR(D, '우리말 → 영어 배열', [
    ('No one needs graphs in real life.', '실생활에서는 아무도 그래프가 필요 없다.'),
    ('There are many soldiers in the tower, so no one can get inside.', '탑에는 군인들이 많아서 아무도 안으로 들어갈 수 없다.'),
    ('No one knows her name.', '아무도 그녀의 이름을 알지 못한다.'),
]))
G8.append(D.done())

# ═════════ 8과 문법 ④ 종합 ═════════
D = Day('m4', '8과 문법 ④ too ~ to · 전체 부정 종합', '교과서 8과 문장 · 의미 같은/다른 짝 · 어법 · 개수 세기')
D.note('시험 직전 체크리스트', [
    ('too ~ to', "= so ~ that 주어 can't / for + 목적격 / to 뒤 목적어 it ✗ / not ✗"),
    ('전체 부정', 'No one · Nobody · None · Nothing · Neither + (부정어 또 쓰지 않기) / No one + 단수 동사'),
    ('부분 부정', 'Not all · Not every(+ 단수명사) · not always · not necessarily'),
])
D.step(MC('교과서 8과 문장', [
    ('교과서 문장에 대한 설명으로 <b>틀린</b> 것은?<br>ⓐ It\'s too hard to read and draw graphs.<br>ⓑ He is too greedy to share with the people.<br>ⓒ No one can say that we don\'t need them anymore.', ['ⓒ는 "모든 사람이 그렇게 말할 수 있는 것은 아니다"라는 부분 부정이다.', 'ⓐ는 "너무 어려워서 읽고 그릴 수 없다"는 뜻이다.', 'ⓑ = He is so greedy that he can\'t share with the people.', 'ⓒ의 No one은 "아무도 …않다"라는 전체 부정이다.'],
     '정답 ▶ ⓒ는 "모든 사람이 그렇게 말할 수 있는 것은 아니다"라는 부분 부정이다.\n이유: No one = 아무도 …않다(전체 부정) → "아무도 말할 수 없다"'),
    ('두 문장의 의미가 같도록 할 때 알맞은 것은?<br><b>He is too greedy to share with the people.</b>', ["He is so greedy that he can't share with the people.", 'He is so greedy that he can share with the people.', 'He is greedy enough to share with the people.', 'He is not greedy, so he shares with the people.'],
     "정답 ▶ He is so greedy that he can't share with the people."),
]))
D.sent("He is so greedy that he can't share with the people.", '그는 너무 욕심이 많아서 백성들과 나눌 수 없다.')
D.step(MC('의미가 같은 짝 · 다른 짝', [
    ('서로 의미가 비슷한 것끼리 짝지은 것은?<br>ⓐ Nobody likes her. = Not everybody likes her.<br>ⓑ She invited none of them. = She did not invite any of them.<br>ⓒ Nobody has seen the movie yet. = No one has seen the movie yet.<br>ⓓ Not every person came. = Nobody came.', ['ⓑ, ⓒ', 'ⓐ, ⓑ', 'ⓐ, ⓓ', 'ⓒ, ⓓ'],
     '정답 ▶ ⓑ, ⓒ\n오답 ▶ ⓐ 전체 부정 ≠ 부분 부정 / ⓓ 부분 부정 ≠ 전체 부정', True),
    ('짝지어진 두 문장의 의미가 서로 <b>다른</b> 것은?', ['Tom never smiles at us. = Sometimes Tom doesn\'t smile at us.', 'Not everyone likes pizza. = Some people don\'t like pizza.', 'No one in my family likes watching TV. = None of my family like watching TV.', "She doesn't know anything about it. = She knows nothing about it."],
     "정답 ▶ Tom never smiles at us. = Sometimes Tom doesn't smile at us.\n이유: never(결코 ~않다) ≠ sometimes(때때로)"),
]))
D.step(MC('어법 · 개수', [
    ('어법상 <b>옳은</b> 것은?', ['No one has ever done this before.', 'None of the apples are not red.', 'All not the students like math.', 'Nobody here seem to like me.'],
     '정답 ▶ No one has ever done this before.\n오답 ▶ not 삭제 / Not all the students / seem → seems'),
    ('어법상 옳은 문장의 개수는?<br>• Not all of them wear glasses.<br>• Leaves are not necessarily green.<br>• Not every students passed the exam.<br>• None of the people we invited could come.<br>• The water was too dirty to drink it.', ['3개', '2개', '4개', '5개', '1개'],
     '정답 ▶ 3개\n틀린 것 ▶ every students → every student / drink it → drink', True),
]))
D.step(ERR(D, '오류 찾기', [
    ('No one [[were]] [[home]] when I [[called]] [[last night]].', 0, 'was', '어젯밤 내가 전화했을 때 아무도 집에 없었다.', '정답 ▶ were → was\n이유: No one + 단수 동사'),
    ('Nobody [[didn\'t solve]] [[the]] [[problem]] [[yesterday]].', 0, 'solved', '어제 아무도 그 문제를 풀지 못했다.', "정답 ▶ didn't solve → solved\n이유: Nobody에 이미 부정 뜻"),
    ('Not [[every]] [[students]] [[passed]] the exam [[last week]].', 1, 'student', '지난주에 모든 학생이 시험에 합격한 것은 아니다.', '정답 ▶ students → student\n이유: every + 단수명사'),
    ("It's [[too]] dangerous [[of]] you [[to stand]] [[there]].", 1, 'for', '네가 거기 서 있는 건 너무 위험하다.', '정답 ▶ of → for\n이유: 의미상 주어 for + 목적격 (교과서 8과)'),
]))
G8.append(D.done())

for d in G7 + G8: ansfirst(d['steps'])
path = '/home/claude/proj/data/m3-jihak-min-L7.js'
PK = json.loads(subprocess.check_output(['node', '-e', "global.window={};require('%s');process.stdout.write(JSON.stringify(window.PKG))" % path]))
base = [d for d in PK['days'] if not re.match(r'[km]\d$', d['id'])]
ids = [d['id'] for d in base]
a, b = ids.index('d2') + 1, ids.index('d4') + 1
PK['days'] = base[:a] + G7 + base[a:b] + G8 + base[b:]
for i, d in enumerate(PK['days']): d['name'] = 'DAY %d' % (i + 1)
src = open(path, encoding='utf-8').read(); head = src[:src.index('window.PKG')]
if '7과 문법' not in head: head = head.rstrip('\n') + '\n/* 11/1: 7과 본문 뒤 7과 문법(가정법 과거·5형식), 8과 본문 뒤 8과 문법(too~to·전체 부정) (gen/gen_j78gram.py) */\n'
write(PK, path, head)
print('ok', [(d['name'], d['id'], d['range'], len(d['steps']), sum(len(s['items']) for s in d['steps'])) for d in PK['days']])
