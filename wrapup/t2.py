from wu import *
# 32·33번
C1 = "Although you may put off going to sleep in order to squeeze more activities into your day, eventually your need for sleep becomes overwhelming and you are forced to get some sleep."
C2 = "This daily drive for sleep appears to be due, in part, to a compound known as adenosine."
C3 = "This natural chemical builds up in your blood as time awake increases."
C4 = "While you sleep, your body breaks down the adenosine."
C5 = "Thus, this molecule may be what your body uses to keep track of lost sleep and to trigger sleep when needed."
C6 = "An accumulation of adenosine and other factors might explain why, after several nights of less than optimal amounts of sleep, you build up a sleep debt that you must make up by sleeping longer than normal."
C7 = "Because of such built-in molecular feedback, you can't become accustomed to getting less sleep than your body needs."
C8 = "Eventually, a lack of sleep catches up with you."
P32 = ' '.join([C1, C2, C3, C4, C5, C6, C7, C8])
D1 = "One of the things that makes uncertainty difficult for members of the public to appreciate is that the significance of uncertainty is relative."
D2 = "Take, for example, the distance between Earth and the sun: 1.49597 × 10⁸ km, as measured at one point during the year."
D3 = "This seems relatively precise; after all, using six significant digits means I know the distance to an accuracy of one part in a million or so."
D4 = "However, if the next digit is uncertain, that means the uncertainty in knowing the precise Earth-sun distance is larger than the distance between New York and Chicago!"
D5 = "Whether or not the quoted number is “precise” therefore depends on what I'm intending to do with it."
D6 = "If I care only about what minute the sun will rise tomorrow, then the number quoted here is fine."
D7 = "If I want to send a satellite to orbit just above the sun, however, then I would need to know distances more accurately."
P33 = ' '.join([D1, D2, D3, D4, D5, D6, D7])

T = Test('3233', '32·33번', '아데노신과 수면 빚 · 불확실성은 상대적이다', '32·33번',
         '범위: 32번(아데노신과 수면 빚 — 잠 부족에는 적응할 수 없다) · 33번(불확실성의 중요성은 수치를 어디에 쓰느냐에 달려 있다). 지문은 원문을 일부 바꾼 것이 있어요. 선택지는 본문 표현을 다른 말로 바꿔 썼으니 뜻을 정확히 따져 보세요.')

# ── 32번 ──
T.flex('다음 글의 주제로 가장 적절한 것은?', '32번', BOX(P32), [
    ('the role of a natural chemical in controlling our need for sleep', '수면 욕구를 조절하는 데 있어 한 천연 화학 물질의 역할'),
    ('the benefits of fitting more activities into a busy day', '바쁜 하루에 더 많은 활동을 끼워 넣는 것의 이점'),
    ('how to pay off a sleep debt in a single night', '수면 빚을 하룻밤에 갚는 방법'),
    ('why some people adapt easily to short sleep', '어떤 사람들이 짧은 수면에 쉽게 적응하는 이유'),
    ('the harmful effects of chemicals in the blood', '혈액 속 화학 물질의 해로운 영향')],
    "이유 ▶ 아데노신(adenosine)이 깨어 있는 동안 쌓이고 자는 동안 분해되면서, 잃어버린 잠을 기록하고 잠을 유발한다 → 수면 욕구를 조절하는 천연 화학 물질의 역할.\n오답 ▶ {1} 활동을 끼워 넣으려 잠을 미뤄도 결국 자야 한다는 도입부일 뿐 {2} 평소보다 오래 자서 갚아야 한다고만 했고 하룻밤 방법은 없다 {3} 적은 잠에 익숙해질 수 없다(can't become accustomed)고 했다 {4} 해로운 영향은 다루지 않는다\n포인트 ▶ 글의 중심 소재(adenosine)와 그 기능(keep track of lost sleep, trigger sleep)을 함께 담은 선택지.",
    [['compound', '화합물'], ['adenosine', '아데노신'], ['regulate / control', '조절하다'], ['adapt', '적응하다']])

T.flex('다음 글의 내용과 일치하는 것은?', '32번', BOX(P32), [
    ('Adenosine is broken down while we are asleep.', '아데노신은 우리가 자는 동안 분해된다.'),
    ('Adenosine levels drop the longer we stay awake.', '아데노신 수치는 오래 깨어 있을수록 떨어진다.'),
    ('Our body can gradually get used to less sleep.', '우리 몸은 적은 잠에 점차 익숙해질 수 있다.'),
    ('A sleep debt can be repaid by sleeping less than usual.', '수면 빚은 평소보다 적게 자서 갚을 수 있다.'),
    ('Adenosine is the only cause of a sleep debt.', '아데노신은 수면 빚의 유일한 원인이다.')],
    "이유 ▶ While you sleep, your body breaks down the adenosine = 자는 동안 분해된다 ✔\n오답 ▶ {1} 깨어 있는 시간이 늘수록 쌓인다(builds up) ↔ drop {2} 적은 잠에 익숙해질 수 없다 {3} 평소보다 오래(longer than normal) 자서 갚는다 {4} in part(부분적으로), adenosine and other factors(다른 요인들도) → only ✗\n포인트 ▶ in part, other factors 같은 '부분' 표현이 있으면 only·always 선택지는 틀린다.",
    [['break down', '분해하다'], ['repay', '갚다'], ['in part', '부분적으로'], ['factor', '요인']])

T.flex('다음 빈칸에 들어갈 말로 가장 적절한 것은?', '32번 변형', BOX(
    C1 + ' ' + C2 + ' ' + C3 + ' ' + C4 + ' ' + C5 + ' ' + C6 + ' Because of such built-in molecular feedback, ' + BL + '. ' + C8), [
    ('our body never adjusts to running on less sleep than it requires', '우리 몸은 필요한 것보다 적은 잠으로 지내는 데 결코 적응하지 못한다'),
    ('we can train ourselves to need less sleep', '우리는 잠이 덜 필요하도록 스스로를 훈련할 수 있다'),
    ('adenosine stops building up after a few nights', '며칠 밤이 지나면 아데노신이 더 이상 쌓이지 않는다'),
    ('the need for sleep disappears when we are busy', '바쁠 때는 잠에 대한 욕구가 사라진다'),
    ('sleeping longer than normal becomes harmful', '평소보다 오래 자는 것은 해로워진다')],
    "이유 ▶ 원문: you can't become accustomed to getting less sleep than your body needs. 몸속 피드백(아데노신이 쌓이고 수면 빚을 기억함) 때문에 적은 잠에 적응할 수 없다 → 뒤 문장 '결국 잠 부족이 따라잡는다'와 연결.\n오답 ▶ {1} 정반대 {2} 아데노신은 깨어 있는 동안 계속 쌓인다 {3} 결국 잠의 욕구가 압도적이 된다(overwhelming) {4} 오래 자는 것은 빚을 갚는 방법\n포인트 ▶ such built-in molecular feedback(그런 내장된 분자 피드백) = 앞에 설명한 아데노신의 작용 → 결론 자리.",
    [['built-in', '내장된'], ['molecular', '분자의'], ['adjust to', '~에 적응하다'], ['require', '필요로 하다']])

T.fixed('다음 글의 밑줄 친 부분 중, 문맥상 낱말의 쓰임이 적절하지 <u>않은</u> 것은?', '32번 변형', BOX(
    "Although you may put off going to sleep in order to squeeze more activities into your day, eventually your need for sleep becomes " + CN(1, 'overwhelming') + " and you are forced to get some sleep. " + C2 + " This natural chemical " + CN(2, 'builds up') + " in your blood as time awake increases. While you sleep, your body " + CN(3, 'accumulates') + " the adenosine. Thus, this molecule may be what your body uses to keep track of lost sleep and to " + CN(4, 'trigger') + " sleep when needed. An accumulation of adenosine and other factors might explain why, after several nights of less than optimal amounts of sleep, you build up a sleep debt that you must make up by sleeping " + CN(5, 'longer') + " than normal. " + C7),
    ['overwhelming', 'builds up', 'accumulates', 'trigger', 'longer'], 3,
    "이유 ▶ 깨어 있을 때 쌓인(builds up) 아데노신을 자는 동안에는 '분해한다' <i>breaks down</i>. accumulates(쌓다)면 깨어 있을 때와 같아져서 잃어버린 잠을 기록하는 장치가 될 수 없다.\n오답 ▶ ① 잠의 욕구가 결국 '압도적'이 된다 ✔ ② 깨어 있는 시간이 늘수록 '쌓인다' ✔ ④ 필요할 때 잠을 '유발한다' ✔ ⑤ 수면 빚은 평소보다 '더 오래' 자서 갚는다 ✔\n포인트 ▶ 깨어 있을 때 ↔ 잘 때의 대조(builds up ↔ breaks down)가 이 글의 핵심 구조.",
    [['overwhelming', '압도적인'], ['accumulate', '쌓다, 축적하다'], ['trigger', '유발하다'], ['make up', '보충하다, 갚다']])

T.fixed('다음 글의 밑줄 친 부분 중, 어법상 <u>틀린</u> 것은?', '32번 변형', BOX(
    "Although you may put off " + CN(1, 'going') + " to sleep in order to squeeze more activities into your day, eventually your need for sleep becomes overwhelming and you are " + CN(2, 'forced') + " to get some sleep. This daily drive for sleep appears " + CN(3, 'to be') + " due, in part, to a compound " + CN(4, 'knowing') + " as adenosine. This natural chemical builds up in your blood as time awake increases. While you sleep, your body breaks down the adenosine. Thus, this molecule may be " + CN(5, 'what') + " your body uses to keep track of lost sleep and to trigger sleep when needed."),
    ['going', 'forced', 'to be', 'knowing', 'what'], 4,
    "이유 ▶ 화합물이 아데노신으로 '알려진' → 수동 과거분사 <i>known</i> (be known as ~로 알려지다).\n오답 ▶ ① put off(미루다) + 동명사 ✔ ② 어쩔 수 없이 자게 '되는' 수동태 be forced to ✔ ③ appear to be(~인 것 같다) ✔ ⑤ 선행사 없이 uses의 목적어가 빠진 절을 이끄는 관계대명사 what(~하는 것) ✔\n포인트 ▶ 명사 + 분사: 명사가 동작을 '받으면' p.p. → a compound known as ~.",
    [['put off', '미루다'], ['squeeze', '끼워 넣다'], ['drive', '욕구, 충동'], ['keep track of', '~을 기록하다, 추적하다']])

T.table('(A), (B), (C)의 각 네모 안에서 어법에 맞는 표현으로 가장 적절한 것은?', '32번', BOX(
    "This natural chemical builds up in your blood as time awake <b>(A)</b> [ increases / is increased ]. … An accumulation of adenosine and other factors might explain why, after several nights of less than optimal amounts of sleep, you build up a sleep debt <b>(B)</b> [ that / what ] you must make up by sleeping longer than normal. Because of such built-in molecular feedback, you can't become accustomed to <b>(C)</b> [ get / getting ] less sleep than your body needs."),
    ['(A)', '(B)', '(C)'], [['increases', 'that', 'getting'], ['is increased', 'that', 'getting'], ['increases', 'what', 'getting'], ['increases', 'that', 'get'], ['is increased', 'what', 'get']],
    "이유 ▶ (A) increase(늘다)는 여기서 자동사, 깨어 있는 시간이 '스스로 늘어남' → <i>increases</i> (B) 선행사 a sleep debt가 있고 make up의 목적어가 빠진 절 → 관계대명사 <i>that</i> (C) become accustomed to의 to는 전치사 → 동명사 <i>getting</i>\n오답 ▶ is increased: 누가 늘리는 게 아니라 시간이 저절로 는다 / what: 선행사가 있으면 못 쓴다 / get: to부정사로 착각\n포인트 ▶ be(become) accustomed to + -ing = be used to + -ing (~에 익숙하다).",
    [['increase', '늘다 (자동사) / 늘리다 (타동사)'], ['sleep debt', '수면 빚'], ['accustomed to', '~에 익숙한']])

T.fixed('주어진 글 다음에 이어질 글의 순서로 가장 적절한 것은?', '32번', GIV(C1) + '\n' + BOX(
    '<b>(A)</b> ' + C4 + ' ' + C5 + '</p><p><b>(B)</b> ' + C2 + ' ' + C3 + '</p><p><b>(C)</b> ' + C6 + ' ' + C7 + ' ' + C8),
    ['(A) − (C) − (B)', '(B) − (A) − (C)', '(B) − (C) − (A)', '(C) − (A) − (B)', '(C) − (B) − (A)'], 2,
    "이유 ▶ 주어진 글: 잠을 미뤄도 결국 자게 된다 → (B) This daily drive for sleep(이 매일의 수면 욕구)은 아데노신 때문, 깨어 있으면 쌓인다 → (A) 자는 동안 분해된다, Thus 이 분자가 잃어버린 잠을 기록한다 → (C) 아데노신의 축적이 수면 빚을 설명하고, 그래서 적은 잠에 익숙해질 수 없다.\n오답 ▶ (A)의 the adenosine은 (B)에서 처음 소개된 뒤에야 쓸 수 있다 / (C)의 such built-in molecular feedback은 (A)·(B)의 설명을 받는다\n포인트 ▶ 정관사·지시어(This daily drive, the adenosine, such)로 앞뒤를 연결.",
    [['daily drive', '매일의 욕구'], ['molecule', '분자'], ['accumulation', '축적']], en=False)

T.fixed('글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳은?', '32번', GIV(C4) + '\n' + BOX(
    C1 + GP(1) + C2 + GP(2) + C3 + GP(3) + C5 + GP(4) + C6 + GP(5) + C7),
    None, 3,
    "이유 ▶ 깨어 있는 동안 쌓인다(C3) ↔ 자는 동안 분해된다(주어진 문장)의 대조가 있어야, Thus(그러므로) 이 분자가 잃어버린 잠을 기록하는 데 쓰인다는 결론이 나온다 → ③.\n오답 ▶ ①② 아데노신이 아직 소개되지 않았거나 쌓인다는 말이 아직 없다 ④⑤ Thus의 근거가 빠진 채 결론이 먼저 나온다\n포인트 ▶ Thus 앞에는 그 결론의 근거가 모두 나와 있어야 한다.",
    [['break down', '분해하다'], ['thus', '그러므로']])

T.table('다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 적절한 것은?', '32번', BOX(P32) + '\n' + SUM(
    'Adenosine, which <b>(A)</b> ' + BL + ' while we are awake, helps our body keep track of lost sleep, so we cannot simply <b>(B)</b> ' + BL + ' to a lack of sleep.'),
    ['(A)', '(B)'], [['accumulates', 'adapt'], ['decreases', 'adapt'], ['accumulates', 'contribute'], ['disappears', 'adapt'], ['decreases', 'return']],
    "이유 ▶ (A) 깨어 있는 시간이 늘수록 쌓인다(builds up) → <i>accumulates</i> (B) 적은 잠에 익숙해질 수 없다(can't become accustomed) → <i>adapt</i>(적응하다)\n오답 ▶ decreases(줄어든다)·disappears(사라진다): 깨어 있을 때 쌓인다는 말과 반대 / contribute(기여하다)·return(돌아가다): 본문 근거 없음\n포인트 ▶ become accustomed to = adapt to = get used to.",
    [['accumulate', '쌓이다'], ['adapt to', '~에 적응하다'], ['contribute to', '~에 기여하다']],
    ko=['쌓인다 / 적응하다', '줄어든다 / 적응하다', '쌓인다 / 기여하다', '사라진다 / 적응하다', '줄어든다 / 돌아가다'])

T.flex('밑줄 친 <u>a lack of sleep catches up with you</u>가 의미하는 바로 가장 적절한 것은?', '32번', BOX(P32.replace('a lack of sleep catches up with you', U('a lack of sleep catches up with you'))), [
    '부족했던 잠은 결국 몸이 그 대가를 치르게 만든다.',
    '잠이 부족해도 활동을 늘리면 극복할 수 있다.',
    '잠이 부족한 사람은 다른 사람을 따라잡을 수 없다.',
    '잠을 줄이면 몸이 곧 그 상태에 적응한다.',
    '잠을 많이 잘수록 아데노신이 더 많이 쌓인다.'],
    "이유 ▶ catch up with = (나쁜 결과가) 결국 ~에게 닥치다. 앞에서 적은 잠에 익숙해질 수 없고 수면 빚은 더 오래 자서 갚아야 한다고 했으므로, 미뤄 둔 잠의 대가를 결국 치른다는 뜻.\n오답 ▶ {1} 잠을 미뤄도 결국 자야 한다 {2} catch up with를 '따라잡다'로 직역한 함정 {3} 적응할 수 없다고 했다 {4} 아데노신은 깨어 있을 때 쌓인다\n포인트 ▶ Eventually(결국) + 앞 문장의 결론(can't become accustomed)을 함께 읽기.",
    [['catch up with', '(나쁜 결과가) 결국 닥치다, 따라잡다'], ['lack', '부족'], ['eventually', '결국']], en=False)

# ── 33번 ──
T.flex('다음 글의 요지로 가장 적절한 것은?', '33번', BOX(P33), [
    '불확실성이 얼마나 중요한지는 수치를 어디에 쓰려는지에 따라 달라진다.',
    '과학적 수치는 유효숫자가 많을수록 언제나 충분히 정확하다.',
    '지구와 태양 사이의 거리는 정확하게 측정할 수 없다.',
    '일반 대중은 과학자보다 불확실성을 더 잘 이해한다.',
    '인공위성을 띄우려면 해 뜨는 시각부터 정확히 알아야 한다.'],
    "이유 ▶ 첫 문장 the significance of uncertainty is relative(불확실성의 중요성은 상대적이다) + Whether or not the quoted number is precise depends on what I'm intending to do with it(정밀한지는 그것으로 무엇을 하려는지에 달려 있다).\n오답 ▶ {1} 여섯 자리도 위성에는 부족하다 {2} 측정 불가능하다는 말이 아니다 {3} 대중이 이해하기 어려워한다(difficult to appreciate) {4} 해 뜨는 분 단위면 지금 수치로 충분하다는 예일 뿐\n포인트 ▶ 첫 문장(주장) → 예시(지구-태양 거리) → 다시 정리(therefore ~)의 두괄식·미괄식 구조.",
    [['uncertainty', '불확실성'], ['significance', '중요성'], ['relative', '상대적인'], ['appreciate', '제대로 이해하다']], en=False)

T.flex('다음 빈칸에 들어갈 말로 가장 적절한 것은?', '33번 변형', BOX(
    'One of the things that makes uncertainty difficult for members of the public to appreciate is that ' + BL + '. ' + D2 + ' ' + D3 + ' ' + D4 + ' ' + D5 + ' ' + D6 + ' ' + D7), [
    ('how much uncertainty matters depends on the situation', '불확실성이 얼마나 중요한지는 상황에 따라 다르다'),
    ('scientists rarely share their measurements with the public', '과학자들은 측정값을 대중과 거의 공유하지 않는다'),
    ('large numbers are always more precise than small ones', '큰 수는 언제나 작은 수보다 더 정밀하다'),
    ('uncertainty can be completely removed by careful measurement', '불확실성은 신중한 측정으로 완전히 없앨 수 있다'),
    ('the distance between Earth and the sun never changes', '지구와 태양 사이의 거리는 결코 변하지 않는다')],
    "이유 ▶ 원문: the significance of uncertainty is relative. 같은 수치라도 해 뜨는 시각을 알 때는 충분하고 위성을 보낼 때는 부족하다 → 불확실성의 중요성은 상황(목적)에 따라 다르다.\n오답 ▶ {1} 공유 여부는 다루지 않는다 {2} 수의 크기와 정밀도는 관계가 없다 {3} 불확실성을 없앤다는 말은 없다 {4} as measured at one point during the year(1년 중 한 시점에 잰) → 시기에 따라 달라짐을 암시\n포인트 ▶ 빈칸이 첫 문장이면 글 전체의 결론(D5 therefore ~)을 바꿔 쓴 선택지를 찾는다.",
    [['matter', '중요하다'], ['measurement', '측정값'], ['precise', '정밀한'], ['remove', '없애다']])

T.flex('다음 글의 내용과 일치하지 <u>않는</u> 것은?', '33번', BOX(P33), [
    ('Six significant digits are precise enough for any purpose.', '유효숫자 여섯 자리면 어떤 목적에도 충분히 정밀하다.'),
    ('The Earth-sun distance in the passage was measured at a particular time of year.', '글 속 지구-태양 거리는 1년 중 특정한 시기에 측정되었다.'),
    ('An uncertain seventh digit would mean an error larger than the distance between two American cities.', '일곱 번째 자리가 불확실하면 미국 두 도시 사이 거리보다 큰 오차가 된다.'),
    ('Predicting sunrise to the minute requires less precision than placing a satellite near the sun.', '해 뜨는 시각을 분 단위로 예측하는 데는 태양 근처에 위성을 보내는 것보다 덜 정밀해도 된다.'),
    ('Whether a figure counts as precise depends on how it will be used.', '어떤 수치가 정밀하다고 여겨지는지는 그것이 어떻게 쓰일지에 달려 있다.')],
    "이유 ▶ 해 뜨는 시각에는 충분하지만 태양 바로 위 궤도에 위성을 보내려면 더 정확해야 한다 → any purpose(어떤 목적에도) ✗\n오답 ▶ {1} as measured at one point during the year ✔ {2} 여섯 자리 다음(next digit) = 일곱 번째 자리, 오차가 뉴욕~시카고 거리보다 크다 ✔ {3} D6·D7의 대조 ✔ {4} D5 그대로 ✔\n포인트 ▶ any, always, never 같은 단정 표현은 본문 근거를 꼭 확인!",
    [['significant digit', '유효숫자'], ['particular', '특정한'], ['precision', '정밀도'], ['figure', '수치']])

T.fixed('다음 글의 밑줄 친 부분 중, 문맥상 낱말의 쓰임이 적절하지 <u>않은</u> 것은?', '33번 변형', BOX(
    "One of the things that makes uncertainty " + CN(1, 'difficult') + " for members of the public to appreciate is that the significance of uncertainty is " + CN(2, 'absolute') + ". " + D2 + " This seems relatively " + CN(3, 'precise') + "; after all, using six significant digits means I know the distance to an accuracy of one part in a million or so. However, if the next digit is uncertain, that means the uncertainty in knowing the precise Earth-sun distance is " + CN(4, 'larger') + " than the distance between New York and Chicago! " + D5 + ' ' + D6 + " If I want to send a satellite to orbit just above the sun, however, then I would need to know distances " + CN(5, 'more') + " accurately."),
    ['difficult', 'absolute', 'precise', 'larger', 'more'], 2,
    "이유 ▶ 같은 수치도 목적에 따라 충분하기도 부족하기도 하다(D5~D7) → 불확실성의 중요성은 '상대적' <i>relative</i>. absolute(절대적인)는 반대.\n오답 ▶ ① 대중이 이해하기 '어렵다' ✔ ③ 여섯 자리면 비교적 '정밀해' 보인다 ✔ ④ 오차가 두 도시 거리보다 '크다' ✔ ⑤ 위성에는 '더' 정확한 거리가 필요하다 ✔\n포인트 ▶ relative(상대적인) ↔ absolute(절대적인) — 반의어 짝으로 출제되기 쉽다.",
    [['absolute', '절대적인'], ['relative', '상대적인'], ['accuracy', '정확도'], ['orbit', '궤도를 돌다']])

T.fixed('다음 글의 밑줄 친 부분 중, 어법상 <u>틀린</u> 것은?', '33번 변형', BOX(
    "Take, for example, the distance between Earth and the sun: 1.49597 × 10⁸ km, as " + CN(1, 'measured') + " at one point during the year. This seems " + CN(2, 'relatively') + " precise; after all, " + CN(3, 'using') + " six significant digits " + CN(4, 'mean') + " I know the distance to an accuracy of one part in a million or so. However, if the next digit is uncertain, that means the uncertainty in knowing the precise Earth-sun distance is larger than the distance between New York and Chicago! Whether or not the quoted number is “precise” therefore " + CN(5, 'depends') + " on what I'm intending to do with it."),
    ['measured', 'relatively', 'using', 'mean', 'depends'], 4,
    "이유 ▶ 주어는 동명사구 using six significant digits(유효숫자 여섯 자리를 쓰는 것) → 단수 → <i>means</i>.\n오답 ▶ ① as (it was) measured: 거리가 '측정된' 수동 ✔ ② 형용사 precise를 꾸미는 부사 ✔ ③ 주어 자리 동명사 ✔ ⑤ 명사절 주어 Whether or not ~ → 단수 depends ✔\n포인트 ▶ 동명사(구)·명사절 주어 → 단수 동사. digits(복수)에 속지 말 것!",
    [['take ~ for example', '~을 예로 들다'], ['relatively', '비교적'], ['quote', '인용하다, 제시하다']])

T.table('(A), (B), (C)의 각 네모 안에서 어법에 맞는 표현으로 가장 적절한 것은?', '33번', BOX(
    "This seems relatively <b>(A)</b> [ precise / precisely ]; after all, using six significant digits means I know the distance to an accuracy of one part in a million or so. … <b>(B)</b> [ Whether / If ] or not the quoted number is “precise” therefore depends on what I'm intending to do with it. … If I want to send a satellite to orbit just above the sun, however, then I would need to know distances more <b>(C)</b> [ accurate / accurately ]."),
    ['(A)', '(B)', '(C)'], [['precise', 'Whether', 'accurately'], ['precisely', 'Whether', 'accurately'], ['precise', 'If', 'accurately'], ['precise', 'Whether', 'accurate'], ['precisely', 'If', 'accurate']],
    "이유 ▶ (A) seem + 형용사 보어 → <i>precise</i> (B) 문장의 주어가 되는 명사절 + or not 바로 앞 → <i>Whether</i> (C) 동사 know를 꾸미는 부사 → <i>accurately</i>\n오답 ▶ precisely: seem 뒤 보어 자리에 부사 불가 / If: if 명사절은 주어 자리에 못 오고 if or not도 불가 / accurate: distances를 꾸미는 게 아니라 '얼마나 정확하게 아는지'\n포인트 ▶ Whether는 주어·or not 바로 앞 모두 OK, If는 둘 다 안 된다.",
    [['seem + 형용사', '~해 보이다'], ['whether or not', '~인지 아닌지'], ['accurately', '정확하게']])

T.fixed('글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳은?', '33번', GIV(D4) + '\n' + BOX(
    D1 + GP(1) + D2 + GP(2) + D3 + GP(3) + D5 + GP(4) + D6 + GP(5) + D7),
    None, 3,
    "이유 ▶ However(하지만) → 앞에서 '여섯 자리면 꽤 정밀해 보인다'(D3)고 한 뒤, 다음 자리가 불확실하면 오차가 뉴욕~시카고보다 크다고 뒤집어야 한다. 뒤의 therefore(그러므로) 정밀한지는 목적에 달려 있다는 결론으로 이어진다 → ③.\n오답 ▶ ①② 아직 수치나 '정밀해 보인다'는 말이 없어 However가 뒤집을 내용이 없다 ④⑤ therefore 결론 뒤라 흐름이 거꾸로 된다\n포인트 ▶ However는 바로 앞 내용(seems precise)과 반대여야 한다.",
    [['digit', '자리(숫자)'], ['uncertain', '불확실한'], ['precise', '정확한']])

T.table('다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 적절한 것은?', '33번', BOX(P33) + '\n' + SUM(
    'A figure that is <b>(A)</b> ' + BL + ' enough for predicting tomorrow\'s sunrise may be <b>(B)</b> ' + BL + ' for sending a satellite close to the sun.'),
    ['(A)', '(B)'], [['precise', 'inadequate'], ['vague', 'inadequate'], ['precise', 'unnecessary'], ['useless', 'sufficient'], ['vague', 'ideal']],
    "이유 ▶ (A) 해 뜨는 시각에는 지금 수치로 충분하다(fine) → <i>precise</i> enough (B) 위성에는 더 정확한 거리가 필요하다 → <i>inadequate</i>(불충분한)\n오답 ▶ vague(모호한)·useless(쓸모없는): 해 뜨는 시각에는 충분하다고 했다 / unnecessary(불필요한)·sufficient(충분한)·ideal(이상적인): 위성에는 부족하다는 말과 반대\n포인트 ▶ 같은 수치 + 다른 목적 → 다른 평가(relative).",
    [['inadequate', '불충분한'], ['vague', '모호한'], ['sufficient', '충분한']],
    ko=['정밀한 / 불충분한', '모호한 / 불충분한', '정밀한 / 불필요한', '쓸모없는 / 충분한', '모호한 / 이상적인'])

T.flex('다음 글의 제목으로 가장 적절한 것은?', '33번', BOX(P33), [
    ('How Precise Is Precise Enough? It Depends on the Purpose', '얼마나 정밀해야 충분히 정밀한가? 목적에 달려 있다'),
    ('Why the Sun Rises at a Different Minute Every Day', '해가 매일 다른 분에 뜨는 이유'),
    ('Satellites: The Future of Space Travel', '인공위성: 우주여행의 미래'),
    ('Measuring the Distance Between New York and Chicago', '뉴욕과 시카고 사이의 거리 재기'),
    ('More Digits Always Guarantee Better Science', '자릿수가 많으면 언제나 더 나은 과학이 보장된다')],
    "이유 ▶ 같은 지구-태양 거리도 해 뜨는 시각에는 충분하고 위성에는 부족하다 → 정밀함의 기준은 목적에 달려 있다.\n오답 ▶ {1} 해 뜨는 시각은 예시의 일부 {2} 위성은 예시일 뿐 우주여행 이야기가 아니다 {3} 두 도시 거리는 오차의 크기를 보여 주는 비유 {4} 여섯 자리도 목적에 따라 부족하다\n포인트 ▶ 제목은 예시가 아니라 예시가 보여 주는 결론(relative)을 담는다.",
    [['precise', '정밀한'], ['purpose', '목적'], ['guarantee', '보장하다']])

# ── 종합 ──
T.flex('32·33번 지문에 나온 단어와 영영풀이가 바르게 짝지어지지 <u>않은</u> 것은?', '종합', '', [
    '<b>optimal</b> : less than what is needed or expected',
    '<b>accumulation</b> : the gradual gathering of something over time',
    '<b>accustomed</b> : used to something because it is familiar',
    '<b>significance</b> : the importance or meaning of something',
    '<b>orbit</b> : to move in a curved path around a planet or star'],
    "이유 ▶ optimal은 '최적의, 가장 좋은'(best or most effective). less than optimal(최적보다 적은)이라는 본문 표현을 보고 optimal 자체를 '부족한'으로 착각하면 안 된다.\n오답 ▶ {1} accumulation 축적 ✔ {2} accustomed 익숙한 ✔ {3} significance 중요성 ✔ {4} orbit 궤도를 돌다 ✔\n포인트 ▶ less than optimal = 최적에 못 미치는(충분하지 않은).",
    [['optimal', '최적의'], ['gradual', '점진적인'], ['familiar', '익숙한'], ['curved', '곡선의']])

T.render()
