from wu import *
# 36·37번
G1 = "The desert tortoise has a simple solution for coping with Death Valley's extreme heat: It avoids it."
G2 = "The slow-moving creature hibernates during the winter and stays in its tunnel for much of the summer, meaning that it spends more than 90 percent of its life immobile."
G3 = "In fact, the tortoise usually only surfaces after a good rain."
G4 = "Then, it gets to work."
G5 = "The tortoise stocks up on water by eating plants and digging holes to collect rain."
G6 = "But to stay supplied with water through its extended hibernation, the reptile relies on something else — its highly sophisticated bladder."
G7 = "Unlike most animals, the tortoise's bladder acts as a holding tank, allowing it to reabsorb water back into its body."
G8 = "Incredibly, a desert tortoise can go a full year without taking in any freshwater at all."
G9 = "And because its bladder is so important to a tortoise's survival, park rangers often remind visitors not to stop and help the slow-movers across the road."
G10 = "Tortoises become so terrified when people pick them up that they empty their bladders, losing their precious water reserves."
P36 = ' '.join([G1, G2, G3, G4, G5, G6, G7, G8, G9, G10])
H1 = "Imagine you are pedalling your bicycle on a level road."
H2 = "You stop pedalling: no force is now acting to move you forward."
H3 = "What happens?"
H4 = "You gradually slow down."
H5 = "How could you slow down more suddenly, in a shorter distance?"
H6 = "By putting the brakes on."
H7 = "Because the brakes change your movement, making you slow down more suddenly, they must be exerting a force on the bicycle and you, as they grip and rub on the wheel-rims."
H8 = "This is the force called friction, which tends to slow down moving things by acting in the direction opposite to movement, that is backwards."
H9 = "Even without the brakes on, there are other friction forces acting on you and your bicycle, which also slow you down."
H10 = "One of these is friction in the wheels rubbing on the axles."
H11 = "Another is air resistance, which you can feel, pushing you backwards as you and the bicycle move forwards."
H12 = "When you apply these ideas to something around you, like a cart, you can see what could be generating friction: mainly the axles rubbing on the body as they rotate."
P37 = ' '.join([H1, H2, H3, H4, H5, H6, H7, H8, H9, H10, H11, H12])

T = Test('3637', '36·37번', '사막거북의 생존법 · 마찰력', '36·37번',
         '범위: 36번(더위를 피하고 방광에 물을 저장하는 사막거북) · 37번(움직임을 늦추는 힘, 마찰력). 지문은 원문을 일부 바꾼 것이 있어요. 선택지는 본문 표현을 다른 말로 바꿔 썼으니 뜻을 정확히 따져 보세요.')

# ── 36번 ──
T.flex('다음 글의 주제로 가장 적절한 것은?', '36번', BOX(P36), [
    ('how the desert tortoise survives extreme heat and lack of water', '사막거북이 극심한 더위와 물 부족을 견뎌 내는 방법'),
    ('why park rangers protect visitors from desert tortoises', '공원 관리인이 사막거북으로부터 방문객을 보호하는 이유'),
    ('the eating habits of reptiles during the winter', '겨울 동안 파충류의 먹이 습관'),
    ('the dangers that roads pose to visitors in national parks', '도로가 국립공원 방문객에게 주는 위험'),
    ('how tortoises dig tunnels to escape from predators', '거북이 포식자를 피하려고 굴을 파는 방법')],
    "이유 ▶ 더위는 피하고(굴속에서 동면·여름잠), 비가 오면 물을 모으고, 방광에 물을 저장해 1년을 버틴다 → 더위와 물 부족을 견디는 생존법.\n오답 ▶ {1} 방문객이 아니라 거북을 보호하려는 것 {2} 겨울에는 동면한다(hibernates) {3} 도로는 거북을 들어 올리지 말라는 예의 배경일 뿐 {4} 굴은 더위를 피하려는 것이고 포식자 이야기는 없다\n포인트 ▶ 글 전체가 '더위 피하기 + 물 확보·저장' 두 가지 생존 전략.",
    [['cope with', '~에 대처하다'], ['extreme', '극심한'], ['predator', '포식자'], ['pose', '(위험을) 주다']])

T.flex('다음 글의 내용과 일치하지 <u>않는</u> 것은?', '36번', BOX(P36), [
    ('The tortoise spends most of its life actively searching for food.', '거북은 삶의 대부분을 활발하게 먹이를 찾으며 보낸다.'),
    ('The tortoise spends the winter in hibernation.', '거북은 겨울을 동면하며 보낸다.'),
    ('The tortoise collects rainwater by digging holes.', '거북은 구멍을 파서 빗물을 모은다.'),
    ('The tortoise can survive a year without drinking any fresh water.', '거북은 민물을 전혀 마시지 않고 1년을 버틸 수 있다.'),
    ('Picking up a tortoise can make it lose the water it has stored.', '거북을 들어 올리면 저장해 둔 물을 잃게 될 수 있다.')],
    "이유 ▶ it spends more than 90 percent of its life immobile(삶의 90% 넘게 움직이지 않고 지낸다) → 대부분 활발하게 먹이를 찾는다 ✗\n오답 ▶ {1} hibernates during the winter ✔ {2} digging holes to collect rain ✔ {3} go a full year without taking in any freshwater ✔ {4} 겁에 질려 방광을 비워 물을 잃는다 ✔\n포인트 ▶ immobile(움직이지 않는) ↔ actively(활발하게).",
    [['hibernation', '동면'], ['immobile', '움직이지 않는'], ['store', '저장하다']])

T.flex('다음 빈칸에 들어갈 말로 가장 적절한 것은?', '36번 변형', BOX(
    "The desert tortoise has a simple solution for coping with Death Valley's extreme heat: " + BL + ". " + G2 + ' ' + G3 + ' ' + G4 + ' ' + G5), [
    ('it simply stays out of the heat', '그냥 더위를 피해 있는다'),
    ('it drinks large amounts of water every day', '매일 많은 양의 물을 마신다'),
    ('it moves faster than most other reptiles', '다른 대부분의 파충류보다 빨리 움직인다'),
    ('it changes the color of its shell', '등딱지 색을 바꾼다'),
    ('it gathers in groups to share the shade', '무리 지어 모여 그늘을 나눈다')],
    "이유 ▶ 원문: It avoids it(더위를 피한다). 뒤 문장에서 겨울엔 동면하고 여름 대부분은 굴속에 머물러 삶의 90% 넘게 움직이지 않는다 = 더위를 피해 있는다(stays out of the heat).\n오답 ▶ {1} 물은 비가 온 뒤에만 모으고 1년을 안 마시고도 버틴다 {2} slow-moving(느리게 움직이는) 동물 {3} 등딱지 색 이야기는 없다 {4} 무리 짓는다는 말은 없다\n포인트 ▶ 콜론(:) 뒤 빈칸 = 앞의 a simple solution의 구체적 내용, 바로 다음 문장들이 근거.",
    [['stay out of', '~을 피해 있다'], ['shell', '등딱지'], ['shade', '그늘'], ['reptile', '파충류']])

T.fixed('다음 글의 밑줄 친 부분 중, 문맥상 낱말의 쓰임이 적절하지 <u>않은</u> 것은?', '36번 변형', BOX(
    "The desert tortoise has a simple solution for coping with Death Valley's extreme heat: It " + CN(1, 'enjoys') + " it. The slow-moving creature hibernates during the winter and stays in its tunnel for much of the summer, meaning that it spends more than 90 percent of its life " + CN(2, 'immobile') + ". In fact, the tortoise usually only " + CN(3, 'surfaces') + " after a good rain. " + G4 + ' ' + G5 + ' ' + G6 + " Unlike most animals, the tortoise's bladder acts as a holding tank, allowing it to " + CN(4, 'reabsorb') + " water back into its body. " + G8 + ' ' + G9 + " Tortoises become so " + CN(5, 'terrified') + " when people pick them up that they empty their bladders, losing their precious water reserves."),
    ['enjoys', 'immobile', 'surfaces', 'reabsorb', 'terrified'], 1,
    "이유 ▶ 겨울엔 동면하고 여름 대부분을 굴속에서 보낸다 → 더위를 '피한다' <i>avoids</i>. enjoys(즐긴다)는 굴속에 숨어 지내는 내용과 반대.\n오답 ▶ ② 삶의 90% 넘게 '움직이지 않는' ✔ ③ 비가 온 뒤에만 '땅 위로 나온다' ✔ ④ 물을 몸속으로 '다시 흡수한다' ✔ ⑤ 사람이 들어 올리면 '겁에 질려' 방광을 비운다 ✔\n포인트 ▶ 콜론 뒤 내용(It avoids it)과 다음 문장의 행동(굴속에 머묾)이 일치해야 한다.",
    [['surface', '(땅 위로) 나오다'], ['reabsorb', '재흡수하다'], ['terrified', '겁에 질린'], ['immobile', '움직이지 않는']])

T.fixed('다음 글의 밑줄 친 부분 중, 어법상 <u>틀린</u> 것은?', '36번 변형', BOX(
    "The slow-moving creature hibernates during the winter and stays in its tunnel for much of the summer, " + CN(1, 'meaning') + " that it spends more than 90 percent of its life immobile. In fact, the tortoise usually only " + CN(2, 'surfaces') + " after a good rain. Then, it gets to work. The tortoise stocks up on water by eating plants and " + CN(3, 'dig') + " holes to collect rain. … Unlike most animals, the tortoise's bladder acts as a holding tank, " + CN(4, 'allowing') + " it to reabsorb water back into its body. … Tortoises become so terrified when people pick them up " + CN(5, 'that') + " they empty their bladders, losing their precious water reserves."),
    ['meaning', 'surfaces', 'dig', 'allowing', 'that'], 3,
    "이유 ▶ 전치사 by의 목적어 eating plants와 and로 병렬 → 동명사 <i>digging</i>.\n오답 ▶ ① 앞 절 전체를 받아 '~라는 뜻이다'를 나타내는 분사구문 ✔ ② 주어 the tortoise(단수) 현재 동사 ✔ ④ 방광이 물을 다시 흡수하게 '해 주는' 능동 분사구문(allow A to V) ✔ ⑤ so + 형용사 + that(너무 ~해서 …하다) ✔\n포인트 ▶ by -ing and -ing: 전치사 뒤 병렬은 둘 다 동명사.",
    [['stock up on', '~을 비축하다'], ['holding tank', '저장 탱크'], ['so ~ that …', '너무 ~해서 …하다']])

T.table('(A), (B), (C)의 각 네모 안에서 어법에 맞는 표현으로 가장 적절한 것은?', '36번', BOX(
    "The slow-moving creature hibernates during the winter and stays in its tunnel for much of the summer, meaning that it spends more than 90 percent of its life <b>(A)</b> [ immobile / immobility ]. … And because its bladder is so important to a tortoise's survival, park rangers often remind visitors <b>(B)</b> [ not to stop / not stopping ] and help the slow-movers across the road. Tortoises become so terrified when people pick them up that they empty their bladders, <b>(C)</b> [ losing / lost ] their precious water reserves."),
    ['(A)', '(B)', '(C)'], [['immobile', 'not to stop', 'losing'], ['immobility', 'not to stop', 'losing'], ['immobile', 'not stopping', 'losing'], ['immobile', 'not to stop', 'lost'], ['immobility', 'not stopping', 'lost']],
    "이유 ▶ (A) 삶을 '움직이지 않는 상태로' 보낸다 → 상태를 나타내는 형용사 <i>immobile</i> (B) remind + 목적어 + to부정사, 부정은 not to → <i>not to stop</i> (C) 거북이 물을 '잃는' 능동, 뒤에 목적어 water reserves → 현재분사 <i>losing</i>\n오답 ▶ immobility(움직이지 않음, 명사): spend 시간 뒤 목적어 자리가 아니다 / not stopping: remind O to V 구조 / lost: 뒤에 목적어가 있으므로 능동\n포인트 ▶ remind / tell / ask / advise + O + (not) to V.",
    [['immobile', '움직이지 않는'], ['remind A to V', 'A에게 ~하라고 상기시키다'], ['reserve', '비축(량)']])

T.fixed('주어진 글 다음에 이어질 글의 순서로 가장 적절한 것은?', '36번', GIV(G1 + ' ' + G2) + '\n' + BOX(
    '<b>(A)</b> ' + G3 + ' ' + G4 + ' ' + G5 + '</p><p><b>(B)</b> ' + G9 + ' ' + G10 + '</p><p><b>(C)</b> ' + G6 + ' ' + G7 + ' ' + G8),
    ['(A) − (C) − (B)', '(B) − (A) − (C)', '(B) − (C) − (A)', '(C) − (A) − (B)', '(C) − (B) − (A)'], 1,
    "이유 ▶ 주어진 글: 삶의 90% 넘게 움직이지 않는다 → (A) In fact 비 온 뒤에만 나와 물을 비축한다 → (C) But 긴 동면 동안 물을 공급받으려면 다른 것, 방광에 의존 → (B) And because 방광이 그렇게 중요하기 때문에 관리인은 길 건너는 거북을 돕지 말라고 한다.\n오답 ▶ (C)의 But은 (A)의 '비 온 뒤 물 모으기'와 대조 / (B)의 its bladder is so important는 (C)의 방광 설명 뒤에만 가능\n포인트 ▶ 연결어(In fact, But, And because)와 소재 등장 순서(물 모으기 → 방광 → 방광의 중요성).",
    [['in fact', '실제로'], ['extended', '길어진, 연장된'], ['bladder', '방광']], en=False)

T.fixed('글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳은?', '36번', GIV(G8) + '\n' + BOX(
    G4 + GP(1) + G5 + GP(2) + G6 + GP(3) + G7 + GP(4) + G9 + GP(5) + G10),
    None, 4,
    "이유 ▶ 방광이 저장 탱크 역할을 해서 물을 다시 흡수한다(G7) → Incredibly(놀랍게도) 1년 동안 민물을 전혀 안 마셔도 된다 → And because 방광이 그렇게 중요하므로(G9). ④.\n오답 ▶ ①② 아직 방광의 저장 기능이 나오지 않아 1년을 버티는 근거가 없다 ③ 방광이 어떻게 작동하는지(G7)보다 먼저 결과가 나온다 ⑤ 관리인 이야기 중간을 끊는다\n포인트 ▶ 놀라운 결과(Incredibly ~)는 그 원리 설명 바로 뒤.",
    [['incredibly', '놀랍게도'], ['take in', '섭취하다'], ['freshwater', '민물']])

T.table('다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 적절한 것은?', '36번', BOX(P36) + '\n' + SUM(
    'The desert tortoise survives by <b>(A)</b> ' + BL + ' the heat and <b>(B)</b> ' + BL + ' water in its bladder, so it should not be picked up by people.'),
    ['(A)', '(B)'], [['avoiding', 'storing'], ['enduring', 'storing'], ['avoiding', 'wasting'], ['seeking', 'releasing'], ['enduring', 'wasting']],
    "이유 ▶ (A) It avoids it(더위를 피한다) → <i>avoiding</i> (B) 방광이 저장 탱크 역할(holding tank) → <i>storing</i>(저장하는)\n오답 ▶ enduring(견디는)·seeking(찾는): 더위를 정면으로 견디거나 찾지 않고 피한다 / wasting(낭비하는)·releasing(내보내는): 물을 저장한다는 말과 반대(물을 비우는 건 겁에 질렸을 때)\n포인트 ▶ 요약문의 so 뒤(사람이 들어 올리면 안 된다)는 (B) 저장한 물을 잃기 때문.",
    [['endure', '견디다'], ['store', '저장하다'], ['release', '내보내다']],
    ko=['피하는 / 저장하는', '견디는 / 저장하는', '피하는 / 낭비하는', '찾는 / 내보내는', '견디는 / 낭비하는'])

T.flex('공원 관리인들이 방문객에게 길을 건너는 거북을 돕지 말라고 하는 이유로 가장 적절한 것은?', '36번', BOX(P36), [
    '사람이 들어 올리면 거북이 겁에 질려 저장해 둔 물을 잃기 때문에',
    '거북이 사람을 물 수 있어 위험하기 때문에',
    '거북은 길을 건너는 속도가 빨라서 도움이 필요 없기 때문에',
    '사람이 만지면 거북에게 병이 옮기 때문에',
    '거북은 도로 위에서 체온을 조절해야 하기 때문에'],
    "이유 ▶ Tortoises become so terrified when people pick them up that they empty their bladders, losing their precious water reserves = 겁에 질려 방광을 비워 소중한 저장 물을 잃는다.\n오답 ▶ {1} 무는 이야기는 없다 {2} slow-movers(느리게 움직이는 동물) {3} 병 이야기는 없다 {4} 체온 조절은 나오지 않는다\n포인트 ▶ because its bladder is so important(방광이 매우 중요하므로)와 바로 다음 문장이 이유.",
    [['park ranger', '공원 관리인'], ['pick up', '들어 올리다'], ['precious', '소중한']], en=False)

# ── 37번 ──
T.flex('다음 글의 주제로 가장 적절한 것은?', '37번', BOX(P37), [
    ('friction as a force that slows down moving objects', '움직이는 물체를 느려지게 하는 힘으로서의 마찰력'),
    ('how to ride a bicycle safely down a hill', '언덕길을 자전거로 안전하게 내려가는 방법'),
    ('the history of the bicycle brake', '자전거 브레이크의 역사'),
    ('why air resistance helps cyclists move faster', '공기 저항이 자전거 타는 사람을 더 빨리 가게 돕는 이유'),
    ('the best materials for making strong wheels', '튼튼한 바퀴를 만드는 데 가장 좋은 재료')],
    "이유 ▶ 페달을 멈추면 서서히 느려지고, 브레이크를 잡으면 더 빨리 멈춘다 → 이 힘이 마찰력(friction)이며 움직임과 반대 방향으로 작용해 물체를 느리게 한다. 바퀴 축·공기 저항도 마찰.\n오답 ▶ {1} level road(평평한 길)이고 안전 수칙이 아니다 {2} 역사 이야기 아님 {3} 공기 저항은 뒤로 민다(pushing you backwards) {4} 재료 이야기는 없다\n포인트 ▶ 자전거는 예시, 설명 대상은 friction.",
    [['friction', '마찰(력)'], ['slow down', '느려지게 하다'], ['cyclist', '자전거 타는 사람']])

T.flex('다음 글의 내용과 일치하는 것은?', '37번', BOX(P37), [
    ('Air resistance pushes against a cyclist who is moving forward.', '공기 저항은 앞으로 가는 자전거 타는 사람을 반대로 민다.'),
    ('A bicycle keeps the same speed after you stop pedalling.', '페달을 멈춘 뒤에도 자전거는 같은 속도를 유지한다.'),
    ('Friction acts in the same direction as movement.', '마찰력은 움직임과 같은 방향으로 작용한다.'),
    ('When the brakes are off, no friction acts on a bicycle.', '브레이크를 잡지 않으면 자전거에 마찰력이 전혀 작용하지 않는다.'),
    ('The friction in a cart comes mainly from its wheels touching the road.', '수레의 마찰은 주로 바퀴가 땅에 닿는 데서 생긴다.')],
    "이유 ▶ air resistance ... pushing you backwards as you and the bicycle move forwards ✔ (push against = 반대로 밀다)\n오답 ▶ {1} You gradually slow down(서서히 느려진다) {2} in the direction opposite to movement(움직임과 반대 방향) {3} Even without the brakes on, there are other friction forces(브레이크 없이도 다른 마찰력이 있다) {4} mainly the axles rubbing on the body(주로 축이 몸체에 문질러지는 것)\n포인트 ▶ 같은/반대, 있다/없다, 주로(mainly) 무엇인지 하나씩 대조.",
    [['push against', '~에 맞서 밀다'], ['pedal', '페달을 밟다'], ['cart', '수레']])

T.flex('다음 빈칸에 들어갈 말로 가장 적절한 것은?', '37번 변형', BOX(
    H5 + ' ' + H6 + ' ' + H7 + ' This is the force called friction, which tends to slow down moving things by acting ' + BL + '. ' + H9 + ' ' + H10 + ' ' + H11), [
    ('against the direction in which they are moving', '그것들이 움직이는 방향과 반대로'),
    ('in the same direction as their movement', '그것들의 움직임과 같은 방향으로'),
    ('only when the brakes are put on', '브레이크를 잡을 때만'),
    ('only on objects that are standing still', '가만히 서 있는 물체에만'),
    ('to push them forward even faster', '그것들을 앞으로 훨씬 더 빨리 밀기 위해')],
    "이유 ▶ 원문: in the direction opposite to movement, that is backwards. 마찰력은 움직이는 물체를 느리게 하므로 움직임과 '반대 방향'으로 작용한다. 뒤의 공기 저항도 앞으로 갈 때 뒤로 민다.\n오답 ▶ {1} 같은 방향이면 더 빨라진다 {2} 브레이크 없이도 다른 마찰력이 있다 {3} moving things(움직이는 것들)를 느리게 한다 {4} 느리게 한다는 말과 반대\n포인트 ▶ opposite to movement = against the direction of motion = backwards.",
    [['against', '~에 반대하여'], ['direction', '방향'], ['stand still', '가만히 있다']])

T.fixed('다음 글의 밑줄 친 부분 중, 문맥상 낱말의 쓰임이 적절하지 <u>않은</u> 것은?', '37번 변형', BOX(
    H1 + ' ' + H2 + " What happens? You " + CN(1, 'gradually') + " slow down. How could you slow down more suddenly, in a " + CN(2, 'longer') + " distance? By putting the brakes on. Because the brakes change your movement, making you slow down more suddenly, they must be exerting a force on the bicycle and you, as they " + CN(3, 'grip') + " and rub on the wheel-rims. This is the force called friction, which tends to slow down moving things by acting in the direction " + CN(4, 'opposite') + " to movement, that is backwards. " + H9 + ' ' + H10 + " Another is air resistance, which you can feel, pushing you " + CN(5, 'backwards') + " as you and the bicycle move forwards."),
    ['gradually', 'longer', 'grip', 'opposite', 'backwards'], 2,
    "이유 ▶ 더 갑자기(more suddenly) 멈춘다는 것은 '더 짧은' 거리에서 멈춘다는 뜻 → <i>shorter</i>. longer(더 긴)는 앞의 suddenly와 맞지 않는다.\n오답 ▶ ① 페달을 멈추면 '서서히' 느려진다 ✔ ③ 브레이크가 바퀴 테를 '꽉 잡고' 문지른다 ✔ ④ 움직임과 '반대' 방향 ✔ ⑤ 공기 저항은 '뒤로' 민다 ✔\n포인트 ▶ 같은 문장 안의 짝(more suddenly ↔ in a shorter distance)이 같은 방향인지 확인.",
    [['gradually', '서서히'], ['grip', '꽉 잡다'], ['rub', '문지르다'], ['wheel-rim', '바퀴 테']])

T.fixed('다음 글의 밑줄 친 부분 중, 어법상 <u>틀린</u> 것은?', '37번 변형', BOX(
    "Because the brakes change your movement, " + CN(1, 'making') + " you slow down more suddenly, they must be " + CN(2, 'exerting') + " a force on the bicycle and you, as they grip and rub on the wheel-rims. This is the force " + CN(3, 'called') + " friction, " + CN(4, 'which') + " tends to slow down moving things by acting in the direction opposite to movement, that is backwards. Even without the brakes on, there " + CN(5, 'is') + " other friction forces acting on you and your bicycle, which also slow you down."),
    ['making', 'exerting', 'called', 'which', 'is'], 5,
    "이유 ▶ There + be + 주어: 진짜 주어는 other friction forces(복수) → <i>are</i>.\n오답 ▶ ① 브레이크가 '~하게 만드는' 능동 분사구문 + make O 동사원형(slow) ✔ ② must be -ing(~하고 있음에 틀림없다), 뒤에 목적어 a force ✔ ③ 힘이 마찰력이라고 '불리는' 수동 ✔ ④ 콤마 뒤 계속적 용법, 선행사 friction ✔\n포인트 ▶ There is/are 뒤 명사가 진짜 주어 → 그 명사에 수 일치.",
    [['exert', '(힘을) 가하다'], ['tend to', '~하는 경향이 있다'], ['that is', '즉']])

T.table('(A), (B), (C)의 각 네모 안에서 어법에 맞는 표현으로 가장 적절한 것은?', '37번', BOX(
    "Because the brakes change your movement, making you slow down more suddenly, they must be <b>(A)</b> [ exerting / exerted ] a force on the bicycle and you. … Another is air resistance, <b>(B)</b> [ which / what ] you can feel, pushing you backwards as you and the bicycle move forwards. When you apply these ideas to something around you, like a cart, you can see <b>(C)</b> [ what / that ] could be generating friction: mainly the axles rubbing on the body as they rotate."),
    ['(A)', '(B)', '(C)'], [['exerting', 'which', 'what'], ['exerted', 'which', 'what'], ['exerting', 'what', 'what'], ['exerting', 'which', 'that'], ['exerted', 'what', 'that']],
    "이유 ▶ (A) 브레이크가 힘을 '가하는' 능동, 뒤에 목적어 a force → <i>exerting</i> (B) 선행사 air resistance + 콤마, feel의 목적어가 빠진 절 → <i>which</i> (C) see의 목적어절이면서 그 안에 주어가 빠짐(___ could be generating) → <i>what</i>(무엇이 ~인지)\n오답 ▶ exerted: 목적어 a force가 있으므로 수동 불가 / what(B): 선행사가 있으면 못 쓴다 / that(C): 뒤에 주어가 빠진 불완전한 절이라 접속사 that 불가\n포인트 ▶ 선행사 O → which/that, 선행사 X + 불완전한 절 → what.",
    [['exert', '(힘을) 가하다'], ['generate', '만들어 내다'], ['axle', '바퀴 축'], ['rotate', '회전하다']])

T.fixed('주어진 글 다음에 이어질 글의 순서로 가장 적절한 것은?', '37번', GIV(H1 + ' ' + H2 + ' ' + H3 + ' ' + H4) + '\n' + BOX(
    '<b>(A)</b> ' + H8 + ' ' + H9 + '</p><p><b>(B)</b> ' + H5 + ' ' + H6 + ' ' + H7 + '</p><p><b>(C)</b> ' + H10 + ' ' + H11 + ' ' + H12),
    ['(A) − (C) − (B)', '(B) − (A) − (C)', '(B) − (C) − (A)', '(C) − (A) − (B)', '(C) − (B) − (A)'], 2,
    "이유 ▶ 주어진 글: 페달을 멈추면 서서히 느려진다 → (B) 더 빨리 멈추려면? 브레이크, 브레이크가 힘을 가한다 → (A) This is the force called friction(이 힘이 마찰력), 브레이크 없이도 다른 마찰력이 있다 → (C) One of these(그중 하나)는 바퀴 축, Another(또 하나)는 공기 저항, 수레에 적용.\n오답 ▶ (A)의 This is the force는 (B)의 a force를 받는다 / (C)의 One of these는 (A)의 other friction forces를 받는다\n포인트 ▶ 지시어(This, these)가 가리키는 말이 바로 앞 단락에 있어야 한다.",
    [['brake', '브레이크'], ['friction force', '마찰력'], ['air resistance', '공기 저항']], en=False)

T.fixed('글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳은?', '37번', GIV(H9) + '\n' + BOX(
    H6 + GP(1) + H7 + GP(2) + H8 + GP(3) + H10 + GP(4) + H11 + GP(5) + H12),
    None, 3,
    "이유 ▶ 브레이크의 힘 = 마찰력(H8) 다음에 '브레이크 없이도(Even without the brakes on) 다른 마찰력이 있다'가 와야, One of these(그중 하나 = 다른 마찰력 중 하나)와 Another로 바퀴 축·공기 저항을 설명할 수 있다 → ③.\n오답 ▶ ①② 아직 마찰력이라는 말이 나오기 전 ④⑤ One of these가 가리킬 대상이 없어진다\n포인트 ▶ One of these / Another 앞에는 여러 개(복수)를 묶어 말하는 문장이 있어야 한다.",
    [['even without', '~이 없어도'], ['act on', '~에 작용하다']])

T.table('다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 적절한 것은?', '37번', BOX(P37) + '\n' + SUM(
    'Friction, which <b>(A)</b> ' + BL + ' movement, is produced not only by brakes but also by rubbing axles and the <b>(B)</b> ' + BL + ' that pushes against us.'),
    ['(A)', '(B)'], [['opposes', 'air'], ['assists', 'air'], ['opposes', 'pedals'], ['creates', 'sunlight'], ['assists', 'road signs']],
    "이유 ▶ (A) 움직임과 반대 방향으로 작용해 느리게 한다 → <i>opposes</i>(~에 맞선다) (B) 공기 저항(air resistance)이 뒤로 민다 → <i>air</i>\n오답 ▶ assists(돕는다)·creates(만든다): 움직임을 늦춘다는 말과 반대 / pedals(페달)·sunlight·road signs: 우리를 뒤로 미는 것으로 나오지 않는다\n포인트 ▶ 마찰력의 세 가지 예: 브레이크, 바퀴 축, 공기 저항.",
    [['oppose', '~에 맞서다, 반대하다'], ['assist', '돕다'], ['produce', '만들어 내다']],
    ko=['맞선다 / 공기', '돕는다 / 공기', '맞선다 / 페달', '만든다 / 햇빛', '돕는다 / 도로 표지판'])

# ── 종합 ──
T.flex('36·37번 지문에 나온 단어와 영영풀이가 바르게 짝지어지지 <u>않은</u> 것은?', '종합', '', [
    '<b>immobile</b> : moving quickly from place to place',
    '<b>hibernate</b> : to spend the winter in a state like deep sleep',
    '<b>reabsorb</b> : to take something back in',
    '<b>friction</b> : the force that resists movement when one surface rubs against another',
    '<b>rotate</b> : to turn around a central point'],
    "이유 ▶ immobile은 '움직이지 않는'(not moving). 여기저기 빠르게 움직인다는 풀이는 반대.\n오답 ▶ {1} hibernate 동면하다 ✔ {2} reabsorb 재흡수하다 ✔ {3} friction 마찰(력) ✔ {4} rotate 회전하다 ✔\n포인트 ▶ 접두사 im-(= not) + mobile(움직이는) → 움직이지 않는.",
    [['immobile', '움직이지 않는'], ['resist', '저항하다'], ['surface', '표면']])

T.render()
