from wu import *
# 30·31번
A1 = "For a species born in a time when resources were limited and dangers were great, our natural tendency to share and cooperate is complicated when resources are plenty and outside dangers are few."
A2 = "When we have less, we tend to be more open to sharing what we have."
A3 = "Certain nomadic tribes don't have much, yet they are happy to share because it is in their interest to do so."
A4 = "If you happen upon them in your travels, they will open up their homes and give you their food and hospitality."
A5 = "It's not just because they are nice people; it's because their survival depends on sharing, for they know that they may be the travelers in need of food and shelter another day."
A6 = "Ironically, the more we have, the bigger our fences, the more sophisticated our security to keep people away and the less we want to share."
A7 = "Our desire for more, combined with our decreased physical interaction with the “common folk,” starts to create a disconnection or blindness to reality."
P30 = ' '.join([A1, A2, A3, A4, A5, A6, A7])
B1 = "Whether we feel happy or sad, content or discontent, is not determined merely by each individual successive moment of life experience — a good thing happens and I'm happy, a bad thing happens and I'm sad."
B2 = "While our experiences affect our mood, we are not blown in a completely new direction by each gust of wind."
B3 = "As humans, we adjust — to new information and events both good and bad — and return to our personal default level of well-being."
B4 = "There will be highs and lows, but over time, like water seeking its own level, we are pulled toward our baseline — back up after bad news and back down after good."
B5 = "The euphoria of first love fades, and so does the despair of a break-up."
B6 = "This tendency is best seen with little kids and their toy joy: When they get what they've longed for, they believe they will be happy for the rest of their lives."
B7 = "And for the first few minutes of the rest of their lives, they are."
B8 = "But then the kids — like adults — adapt."
P31 = ' '.join([B1, B2, B3, B4, B5, B6, B7, B8])

T = Test('3031', '30·31번', '나눔의 역설 · 행복의 기준선', '30·31번',
         '범위: 30번(가진 것이 많을수록 나누지 않는 역설) · 31번(좋은 일도 나쁜 일도 결국 행복의 기준선으로 돌아온다). 지문은 원문을 일부 바꾼 것이 있어요. 선택지는 본문 표현을 다른 말로 바꿔 썼으니 뜻을 정확히 따져 보세요.')

# ── 30번 ──
T.fixed('다음 글의 밑줄 친 부분 중, 문맥상 낱말의 쓰임이 적절하지 <u>않은</u> 것은?', '30번 변형', BOX(
    "For a species born in a time when resources were " + CN(1, 'limited') + " and dangers were great, our natural tendency to share and cooperate is complicated when resources are plenty and outside dangers are few. When we have less, we tend to be " + CN(2, 'less') + " open to sharing what we have. Certain nomadic tribes don't have much, yet they are happy to share because it is in their " + CN(3, 'interest') + " to do so. " + A4 + ' ' + A5 + " Ironically, the more we have, the bigger our fences, the more " + CN(4, 'sophisticated') + " our security to keep people away and the less we want to share. Our desire for more, combined with our " + CN(5, 'decreased') + " physical interaction with the “common folk,” starts to create a disconnection or blindness to reality."),
    ['limited', 'less', 'interest', 'sophisticated', 'decreased'], 2,
    "이유 ▶ 바로 뒤에서 가진 게 많지 않은 유목 부족이 기꺼이 나눈다고 하므로, 가진 것이 적을 때(When we have less) 나눔에 '더' 열려 있다 → <i>more</i> open이 맞다.\n오답 ▶ ① 자원이 '제한된' 시대에 태어난 종 ✔ ③ 나누는 것이 그들에게 '이익'(in their interest) ✔ ④ 사람을 막는 보안이 더 '정교해진다' ✔ ⑤ 보통 사람들과의 접촉이 '줄어서' 현실과 단절된다 ✔\n포인트 ▶ 글 전체의 대조: 가진 것이 적다 → 나눈다 / 가진 것이 많다 → 나누지 않는다.",
    [['complicated', '복잡해진'], ['nomadic', '유목의'], ['in one\'s interest', '~에게 이익이 되는'], ['sophisticated', '정교한'], ['decreased', '줄어든']])

T.flex('다음 글의 주제로 가장 적절한 것은?', '30번', BOX(P30), [
    ('how abundance can weaken our willingness to share', '풍요가 어떻게 나누려는 마음을 약하게 만드는가'),
    ('the role of nomadic tribes in preserving traditional hospitality', '전통적인 환대를 지키는 데 있어 유목 부족의 역할'),
    ('why modern security systems fail to protect our property', '현대의 보안 시스템이 재산을 지키지 못하는 이유'),
    ('the importance of physical activity for a healthy life', '건강한 삶을 위한 신체 활동의 중요성'),
    ('ways to divide limited resources fairly among travelers', '여행자들 사이에서 부족한 자원을 공정하게 나누는 방법')],
    "이유 ▶ 자원이 부족할 때는 나누지만, 가진 것이 많을수록(the more we have) 울타리를 높이고 덜 나누게 된다는 역설이 중심 → 풍요(abundance)가 나눔의 의지(willingness to share)를 약하게 만든다.\n오답 ▶ {1} 유목 부족은 예시일 뿐 {2} 보안이 실패한다는 말은 없다 {3} physical interaction(사람과의 접촉)을 신체 활동으로 바꾼 함정 {4} 공정한 분배 방법은 나오지 않는다\n포인트 ▶ Ironically 뒤 문장이 주제문: the more we have ~ the less we want to share.",
    [['abundance', '풍요, 풍부함'], ['willingness', '기꺼이 하는 마음'], ['hospitality', '환대'], ['preserve', '지키다, 보존하다']])

T.flex('다음 글의 내용과 일치하는 것은?', '30번', BOX(P30), [
    ('Nomadic tribes are generous partly because they may one day need the same help.', '유목 부족이 너그러운 것은 언젠가 자신들도 같은 도움이 필요할 수 있기 때문이기도 하다.'),
    ('Our instinct to cooperate becomes simpler when resources are abundant.', '자원이 풍부하면 협력하려는 본능이 더 단순해진다.'),
    ('Nomadic tribes share because they have more than they need.', '유목 부족은 필요한 것보다 많이 가지고 있어서 나눈다.'),
    ('Wealthier people tend to lower their fences to welcome others.', '더 부유한 사람들은 다른 사람을 맞이하려고 울타리를 낮추는 경향이 있다.'),
    ('Frequent contact with ordinary people leads us to lose touch with reality.', '보통 사람들과 자주 접촉하면 현실 감각을 잃게 된다.')],
    "이유 ▶ they know that they may be the travelers in need of food and shelter another day(언젠가는 자신들이 음식과 쉴 곳이 필요한 여행자가 될 수 있다) = may one day need the same help ✔\n오답 ▶ {1} 자원이 풍부하면 나누고 협력하는 성향이 '복잡해진다'(complicated) ↔ simpler {2} don't have much(많이 가지지 않았다) ↔ more than they need {3} 가진 게 많을수록 울타리가 더 커진다(bigger fences) {4} 접촉이 '줄어서'(decreased) 단절이 생긴다 ↔ frequent contact\n포인트 ▶ 일치 문제는 비교·증감 표현(simpler, more, lower, frequent)을 본문과 하나씩 대조!",
    [['generous', '너그러운'], ['instinct', '본능'], ['abundant', '풍부한'], ['lose touch with', '~와 접촉이 끊기다, ~을 모르게 되다']])

T.flex('다음 빈칸에 들어갈 말로 가장 적절한 것은?', '30번 변형', BOX(
    A1 + ' ' + A2 + ' ' + A3 + ' ' + A4 + ' ' + A5 + ' Ironically, the more we have, ' + BL + '. ' + A7), [
    ('the more we shut others out and the less willing we are to share', '우리는 다른 사람을 더 차단하고 덜 나누려 한다'),
    ('the more hospitality we show to travelers in need', '도움이 필요한 여행자에게 더 많은 환대를 베푼다'),
    ('the more we depend on others for our survival', '생존을 위해 다른 사람에게 더 의지한다'),
    ('the more clearly we come to see reality', '현실을 더 분명하게 보게 된다'),
    ('the more open we become to sharing what we have', '가진 것을 나누는 데 더 열려 있게 된다')],
    "이유 ▶ Ironically(역설적이게도) → 앞의 '없을수록 나눈다'와 반대 내용. 원문: the bigger our fences, the more sophisticated our security to keep people away and the less we want to share = 다른 사람을 막고(shut others out) 덜 나누려 한다.\n오답 ▶ {1}·{4} 가난한 유목 부족의 모습, 역설이 아니다 {2} 생존을 위해 나누는 것은 가진 게 적은 사람들 {3} 뒤 문장: 현실에 대한 단절·눈멂(blindness to reality)이 생긴다\n포인트 ▶ the 비교급 ~, the 비교급 …: ~할수록 더 …하다.",
    [['ironically', '역설적이게도'], ['shut out', '차단하다, 들이지 않다'], ['willing', '기꺼이 하는'], ['depend on', '~에 의지하다']])

T.fixed('다음 글의 밑줄 친 부분 중, 어법상 <u>틀린</u> 것은?', '30번 변형', BOX(
    "Certain nomadic tribes don't have much, yet they are happy " + CN(1, 'to share') + " because it is in their interest to do so. If you happen upon them in your travels, they will open up their homes and " + CN(2, 'give') + " you their food and hospitality. It's not just because they are nice people; it's because their survival " + CN(3, 'depend') + " on sharing, for they know that they may be the travelers in need of food and shelter another day. Ironically, the more we have, the " + CN(4, 'bigger') + " our fences and the less we want to share. Our desire for more, combined with our decreased physical interaction with the “common folk,” " + CN(5, 'starts') + " to create a disconnection or blindness to reality."),
    ['to share', 'give', 'depend', 'bigger', 'starts'], 3,
    "이유 ▶ 주어는 their survival(단수) → <i>depends</i>.\n오답 ▶ ① be happy to부정사(~해서 기쁘다, 기꺼이 ~하다) ✔ ② will open up과 병렬, 조동사 will 뒤 동사원형 give ✔ ④ the 비교급 ~, the 비교급: the more we have, the bigger ✔ ⑤ 주어 Our desire(단수), combined with ~는 삽입된 분사구 → starts ✔\n포인트 ▶ 주어와 동사 사이에 낀 수식어(for more, combined with ~)는 지우고 수 일치!",
    [['nomadic tribe', '유목 부족'], ['happen upon', '우연히 만나다'], ['depend on', '~에 달려 있다'], ['combined with', '~와 결합되어']])

T.table('(A), (B), (C)의 각 네모 안에서 어법에 맞는 표현으로 가장 적절한 것은?', '30번', BOX(
    "For a species <b>(A)</b> [ born / bearing ] in a time when resources were limited and dangers were great, our natural tendency to share and cooperate <b>(B)</b> [ is / are ] complicated when resources are plenty and outside dangers are few. … Our desire for more, <b>(C)</b> [ combining / combined ] with our decreased physical interaction with the “common folk,” starts to create a disconnection or blindness to reality."),
    ['(A)', '(B)', '(C)'], [['born', 'is', 'combined'], ['bearing', 'is', 'combined'], ['born', 'are', 'combined'], ['born', 'is', 'combining'], ['bearing', 'are', 'combining']],
    "이유 ▶ (A) 종(species)이 '태어난' → 수동 의미 과거분사 <i>born</i> (B) 주어 our natural tendency(단수), to share and cooperate는 tendency를 꾸미는 to부정사 → <i>is</i> (C) 욕망이 접촉 감소와 '결합된' → 수동 과거분사 <i>combined</i> (be combined with)\n오답 ▶ bearing(낳는, 견디는): 종이 무언가를 낳는다는 뜻이 되어 어색 / are: tendency를 복수로 착각 / combining: 능동이면 목적어가 필요\n포인트 ▶ 명사 뒤 분사: 꾸밈을 받는 명사가 하는 것(능동 -ing)인지 당하는 것(수동 p.p.)인지!",
    [['species', '(생물의) 종'], ['bear', '낳다 (bear-bore-born)'], ['tendency', '경향'], ['cooperate', '협력하다'], ['combine', '결합하다']])

T.flex('밑줄 친 <u>a disconnection or blindness to reality</u>가 의미하는 바로 가장 적절한 것은?', '30번', BOX(P30.replace('a disconnection or blindness to reality', U('a disconnection or blindness to reality'))), [
    '풍요 속에서 서로 기대고 나누며 살아야 한다는 사실을 보지 못하게 되는 것',
    '유목 부족의 생활 방식을 지나치게 이상화하는 것',
    '자원이 부족했던 과거의 위험을 과장해서 기억하는 것',
    '보안 시스템이 완벽하지 않다는 것을 깨닫지 못하는 것',
    '낯선 여행자를 아무 의심 없이 믿게 되는 것'],
    "이유 ▶ 더 많이 가지려는 욕망 + 보통 사람들과의 접촉 감소 → 나눔에 생존이 달려 있다는 현실(언젠가 나도 도움이 필요한 여행자가 될 수 있음)을 보지 못하게 된다.\n오답 ▶ {1} 유목 부족을 이상화한다는 내용은 없다 {2} 과거의 위험을 과장한다는 말은 없다 {3} 보안의 한계는 다루지 않는다 {4} 오히려 사람을 멀리하게(keep people away) 된다\n포인트 ▶ 함축 의미는 바로 앞 원인(desire for more + decreased interaction)과 글 전체 대조에서 찾는다.",
    [['disconnection', '단절'], ['blindness', '눈멂, 보지 못함'], ['reality', '현실'], ['common folk', '보통 사람들']], en=False)

T.fixed('글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳은?', '30번', GIV(A6) + '\n' + BOX(
    A1 + ' ' + A2 + GP(1) + A3 + GP(2) + A4 + GP(3) + A5 + GP(4) + A7 + GP(5).rstrip()),
    None, 4,
    "이유 ▶ Ironically(역설적이게도) → 앞의 '가진 게 적은 유목 부족은 생존을 위해 나눈다'와 반대되는 '가진 게 많을수록 덜 나눈다'가 와야 하고, 뒤 문장 Our desire for more(더 많이 가지려는 욕망)는 주어진 문장의 the more we have를 받는다 → ④.\n오답 ▶ ①~③ 유목 부족 이야기 중간이라 흐름이 끊긴다 ⑤ Our desire for more가 앞에 나올 근거(the more we have)가 사라진다\n포인트 ▶ 연결어(Ironically)와 뒤 문장의 지시어·반복어(more)를 함께 확인!",
    [['ironically', '역설적이게도'], ['fence', '울타리'], ['security', '보안'], ['keep away', '가까이 오지 못하게 하다']])

T.table('다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 적절한 것은?', '30번', BOX(P30) + '\n' + SUM(
    'People readily share when resources are <b>(A)</b> ' + BL + ', but as they grow <b>(B)</b> ' + BL + ', they become less willing to share and lose sight of reality.'),
    ['(A)', '(B)'], [['scarce', 'wealthier'], ['abundant', 'wealthier'], ['scarce', 'poorer'], ['abundant', 'poorer'], ['shared', 'busier']],
    "이유 ▶ (A) 가진 것이 적을 때(have less) 기꺼이 나눈다 → <i>scarce</i>(부족한) (B) 가진 것이 많아질수록(the more we have) 덜 나눈다 → <i>wealthier</i>(더 부유한)\n오답 ▶ abundant(풍부한)는 (A)와 반대 / poorer(더 가난한)는 (B)와 반대 / shared·busier는 본문 근거가 없다\n포인트 ▶ 요약문은 주제문(Ironically ~)의 대조 구조를 그대로 옮긴다.",
    [['readily', '기꺼이, 선뜻'], ['scarce', '부족한'], ['abundant', '풍부한'], ['lose sight of', '~을 보지 못하게 되다']],
    ko=['부족한 / 더 부유한', '풍부한 / 더 부유한', '부족한 / 더 가난한', '풍부한 / 더 가난한', '공유된 / 더 바쁜'])

# ── 31번 ──
T.flex('다음 글의 요지로 가장 적절한 것은?', '31번', BOX(P31), [
    '사람은 좋은 일과 나쁜 일에 적응하여 결국 각자의 기본 행복 수준으로 돌아온다.',
    '행복은 매 순간 일어나는 사건에 의해 전적으로 결정된다.',
    '어린 시절에 느낀 기쁨은 어른이 되어서도 오래 지속된다.',
    '좋은 소식이 나쁜 소식보다 기분에 더 오래 영향을 준다.',
    '원하는 것을 얻으면 평생 행복하게 살 수 있다.'],
    "이유 ▶ we adjust ... and return to our personal default level of well-being(우리는 적응해서 개인의 기본 행복 수준으로 돌아온다)이 요지. 첫사랑의 기쁨도 이별의 절망도 사라지고, 아이도 어른도 적응한다.\n오답 ▶ {1} 첫 문장에서 매 순간의 경험만으로 결정되지 않는다(not determined merely)고 했다 {2} 장난감의 기쁨도 몇 분뿐 {3} 좋은 일 뒤에도 내려오고 나쁜 일 뒤에도 올라온다 — 어느 쪽이 더 길다는 말은 없다 {4} 아이들의 믿음일 뿐, 곧 적응한다\n포인트 ▶ 요지 = 일반 진술(As humans, we adjust ~) + 예시(첫사랑, 아이의 장난감).",
    [['adjust', '적응하다'], ['default level', '기본 수준'], ['well-being', '행복, 안녕'], ['determine', '결정하다']], en=False)

T.flex('다음 빈칸에 들어갈 말로 가장 적절한 것은?', '31번 변형', BOX(
    B4 + ' ' + B5 + ' ' + B6 + ' ' + B7 + ' But then the kids — like adults — ' + BL + '.'), [
    ('get used to what they have', '가진 것에 익숙해진다'),
    ('keep longing for the same toy', '같은 장난감을 계속 갈망한다'),
    ('stay happy for the rest of their lives', '남은 평생 계속 행복하다'),
    ('become sadder than they were before', '전보다 더 슬퍼진다'),
    ('refuse to share their toys with others', '장난감을 다른 사람과 나누기를 거부한다')],
    "이유 ▶ 원문: adapt(적응하다). 처음 몇 분은 행복하지만 But then(그러나 그다음에는) 새 장난감에 익숙해져 기준선으로 돌아온다 = get used to what they have.\n오답 ▶ {1} 이미 얻은 장난감을 계속 갈망한다는 근거 없음 {2} But then과 맞지 않는다(평생 행복하리라는 건 아이들의 믿음) {3} 기준선으로 돌아올 뿐 더 슬퍼지지는 않는다 {4} 나눔은 이 글의 내용이 아니다\n포인트 ▶ like adults(어른처럼) → 앞의 일반 진술(we adjust, we are pulled toward our baseline)과 같은 내용.",
    [['adapt', '적응하다'], ['get used to', '~에 익숙해지다'], ['long for', '갈망하다'], ['refuse', '거부하다']])

T.flex('다음 글의 내용과 일치하지 <u>않는</u> 것은?', '31번', BOX(P31), [
    ('Each new experience completely changes the direction of our mood.', '새로운 경험 하나하나가 기분의 방향을 완전히 바꾼다.'),
    ('Our mood is influenced by what we go through.', '기분은 우리가 겪는 일에 영향을 받는다.'),
    ('Over time, we tend to drift back to our usual level of happiness.', '시간이 지나면 우리는 평소의 행복 수준으로 서서히 돌아가는 경향이 있다.'),
    ('The intense joy of a first romance does not last forever.', '첫사랑의 강렬한 기쁨은 영원히 지속되지 않는다.'),
    ('Children at first believe that getting a longed-for toy will keep them happy for good.', '아이들은 처음에 갈망하던 장난감을 얻으면 영원히 행복할 거라고 믿는다.')],
    "이유 ▶ we are not blown in a completely new direction by each gust of wind(바람이 불 때마다 완전히 새로운 방향으로 날려 가지 않는다) ↔ completely changes the direction ✗\n오답 ▶ {1} our experiences affect our mood ✔ {2} over time ... we are pulled toward our baseline ✔ (drift back 서서히 돌아가다) {3} The euphoria of first love fades ✔ (euphoria = intense joy) {4} they believe they will be happy for the rest of their lives ✔ (for good = 영원히)\n포인트 ▶ 비유(gust of wind 돌풍)를 그대로 해석하지 말고 뜻(사건 하나하나)으로 바꿔 읽기.",
    [['go through', '겪다'], ['drift back', '서서히 돌아가다'], ['euphoria', '큰 행복감'], ['for good', '영원히']])

T.fixed('다음 글의 밑줄 친 부분 중, 문맥상 낱말의 쓰임이 적절하지 <u>않은</u> 것은?', '31번 변형', BOX(
    B1 + " While our experiences " + CN(1, 'affect') + " our mood, we are not blown in a completely new direction by each gust of wind. As humans, we " + CN(2, 'adjust') + " — to new information and events both good and bad — and return to our personal default level of well-being. There will be highs and lows, but over time, like water seeking its own level, we are pulled toward our " + CN(3, 'baseline') + " — back up after bad news and back down after good. The euphoria of first love " + CN(4, 'intensifies') + ", and so does the despair of a break-up. " + B6 + ' ' + B7 + " But then the kids — like adults — " + CN(5, 'adapt') + "."),
    ['affect', 'adjust', 'baseline', 'intensifies', 'adapt'], 4,
    "이유 ▶ 좋은 일 뒤에도 기준선으로 '내려온다'(back down after good)는 흐름 → 첫사랑의 큰 기쁨은 '사라진다' <i>fades</i>. intensifies(더 강해지다)는 반대.\n오답 ▶ ① 경험이 기분에 영향을 준다 ✔ ② 우리는 적응한다 ✔ ③ 기준선 쪽으로 끌려간다 ✔ ⑤ 아이들도 어른처럼 적응한다 ✔\n포인트 ▶ and so does ~: ~도 그렇다 → 이별의 절망도 똑같이 '사라진다'. 둘 다 사라져야 기준선 이야기와 맞는다.",
    [['affect', '영향을 주다'], ['baseline', '기준선'], ['intensify', '강해지다'], ['fade', '희미해지다, 사라지다'], ['despair', '절망']])

T.fixed('다음 글의 밑줄 친 부분 중, 어법상 <u>틀린</u> 것은?', '31번 변형', BOX(
    "Whether we feel happy or sad, content or discontent, " + CN(1, 'are') + " not determined merely by each individual successive moment of life experience. While our experiences affect our mood, we are not " + CN(2, 'blown') + " in a completely new direction by each gust of wind. As humans, we adjust — to new information and events both good and bad — and " + CN(3, 'return') + " to our personal default level of well-being. There will be highs and lows, but over time, like water " + CN(4, 'seeking') + " its own level, we are pulled toward our baseline. The euphoria of first love fades, and so " + CN(5, 'does') + " the despair of a break-up."),
    ['are', 'blown', 'return', 'seeking', 'does'], 1,
    "이유 ▶ 주어는 명사절 Whether we feel happy or sad(행복하게 느끼는지 슬프게 느끼는지) → 명사절 주어는 단수 → <i>is</i>.\n오답 ▶ ② 바람에 '날려 가는' 수동태 be blown ✔ ③ adjust와 and로 병렬, 주어 we → return ✔ ④ water를 꾸미는 현재분사(물이 제 높이를 찾아가는) ✔ ⑤ 앞의 일반동사 fades를 받는 대동사, so + 동사 + 주어 도치 → does ✔\n포인트 ▶ Whether/That/What 명사절 주어 → 단수 동사!",
    [['whether', '~인지 (아닌지)'], ['content', '만족한'], ['successive', '연속적인'], ['gust', '돌풍'], ['break-up', '이별']])

T.fixed('주어진 글 다음에 이어질 글의 순서로 가장 적절한 것은?', '31번', GIV(B1) + '\n' + BOX(
    '<b>(A)</b> ' + B6 + ' ' + B7 + ' ' + B8 + '</p><p><b>(B)</b> ' + B2 + ' ' + B3 + '</p><p><b>(C)</b> ' + B4 + ' ' + B5),
    ['(A) − (C) − (B)', '(B) − (A) − (C)', '(B) − (C) − (A)', '(C) − (A) − (B)', '(C) − (B) − (A)'], 3,
    "이유 ▶ 주어진 글: 행복은 매 순간의 경험만으로 결정되지 않는다 → (B) 경험이 기분에 영향은 주지만 우리는 적응해서 기본 수준으로 돌아온다(일반 진술) → (C) 오르내림이 있어도 기준선으로 끌려간다 + 첫사랑·이별의 예 → (A) This tendency(이 경향 = 기준선으로 돌아가는 것)가 가장 잘 보이는 아이들의 장난감 예, 마무리 adapt.\n오답 ▶ (A)가 먼저 오면 This tendency가 가리킬 대상이 없다 / (C)의 highs and lows는 (B)의 adjust ~ return 설명을 이어받는다\n포인트 ▶ 지시어(This tendency)와 일반 → 구체(예시) 흐름으로 순서 잡기.",
    [['tendency', '경향'], ['longed for', '갈망하던'], ['adjust', '적응하다'], ['highs and lows', '좋을 때와 나쁠 때']], en=False)

T.flex('밑줄 친 <u>we are not blown in a completely new direction by each gust of wind</u>가 의미하는 바로 가장 적절한 것은?', '31번', BOX(P31.replace('we are not blown in a completely new direction by each gust of wind', U('we are not blown in a completely new direction by each gust of wind'))), [
    ('A single event does not permanently change how happy we are.', '사건 하나가 우리의 행복 정도를 영원히 바꾸지는 않는다.'),
    ('We cannot control the events that happen to us.', '우리는 우리에게 일어나는 일을 통제할 수 없다.'),
    ('Strong emotions always come from outside influences.', '강한 감정은 언제나 외부의 영향에서 온다.'),
    ('We should avoid situations that might upset us.', '우리를 속상하게 할 수 있는 상황은 피해야 한다.'),
    ('Our mood shifts completely with every experience.', '우리의 기분은 경험할 때마다 완전히 바뀐다.')],
    "이유 ▶ each gust of wind(돌풍 하나하나) = 하나하나의 사건, blown in a completely new direction = 완전히 새로운 방향으로 바뀜. 그렇지 않다 → 사건 하나가 행복 수준을 영원히 바꾸지 않는다(결국 기준선으로 돌아온다).\n오답 ▶ {1} 통제 가능 여부는 다루지 않는다 {2} 감정의 출처 이야기가 아니다 {3} 피하라는 충고는 없다 {4} 밑줄과 정반대\n포인트 ▶ While 양보절(경험이 기분에 영향은 주지만) 뒤의 주절이 핵심.",
    [['permanently', '영원히'], ['gust', '돌풍'], ['upset', '속상하게 하다'], ['shift', '바뀌다']])

T.table('다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 적절한 것은?', '31번', BOX(P31) + '\n' + SUM(
    'Although our mood <b>(A)</b> ' + BL + ' with good and bad events, over time we tend to <b>(B)</b> ' + BL + ' our usual level of happiness.'),
    ['(A)', '(B)'], [['fluctuates', 'return to'], ['remains stable', 'return to'], ['fluctuates', 'rise above'], ['fluctuates', 'move away from'], ['remains stable', 'sink below']],
    "이유 ▶ (A) 좋은 일·나쁜 일에 따라 오르내린다(highs and lows) → <i>fluctuates</i>(변동하다) (B) 기본 수준·기준선으로 돌아온다(return to our default level, pulled toward our baseline) → <i>return to</i>\n오답 ▶ remains stable(안정된 채로 있다): 오르내림이 있다는 말과 반대 / rise above(위로 올라가다)·sink below(아래로 가라앉다)·move away from(멀어지다): 기준선으로 돌아온다는 말과 반대\n포인트 ▶ Although 양보 구조: (A)는 변화, (B)는 결국 원래대로.",
    [['fluctuate', '변동하다, 오르내리다'], ['remain stable', '안정된 상태로 있다'], ['usual', '평소의'], ['sink', '가라앉다']],
    ko=['변동한다 / ~로 돌아가다', '안정된 채로 있다 / ~로 돌아가다', '변동한다 / ~보다 위로 올라가다', '변동한다 / ~에서 멀어지다', '안정된 채로 있다 / ~ 아래로 가라앉다'])

T.fixed('글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳은?', '31번', GIV(B7) + '\n' + BOX(
    B1 + ' ' + B2 + GP(1) + B3 + GP(2) + B4 + GP(3) + B5 + GP(4) + B6 + GP(5) + B8),
    None, 5,
    "이유 ▶ 주어진 문장의 they are = they are happy(그들은 정말 행복하다). 바로 앞에 '남은 평생 행복할 거라고 믿는다'(they believe they will be happy for the rest of their lives)가 있어야 하고, 뒤의 But then(그러나 그 후에는) 적응한다로 이어진다 → ⑤.\n오답 ▶ ①~④ 앞에 they가 가리킬 아이들(kids)과 happy가 없다\n포인트 ▶ 생략된 말(they are [happy])을 복원하고 앞 문장에서 짝을 찾기.",
    [['for the rest of one\'s life', '남은 평생'], ['adapt', '적응하다']])

# ── 종합 ──
T.flex('30·31번 지문에 나온 단어와 영영풀이가 바르게 짝지어지지 <u>않은</u> 것은?', '종합', '', [
    '<b>nomadic</b> : staying in one place for a long time and never moving',
    '<b>sophisticated</b> : highly developed and complex',
    '<b>hospitality</b> : friendly and generous treatment of guests or strangers',
    '<b>euphoria</b> : a feeling of great happiness and excitement',
    '<b>baseline</b> : a usual or starting level used for comparison'],
    "이유 ▶ nomadic(유목의)은 '한곳에 머물지 않고 옮겨 다니는'(moving from place to place). 한곳에 오래 머무는 것은 반대(settled).\n오답 ▶ {1} sophisticated 정교한 ✔ {2} hospitality 환대 ✔ {3} euphoria 큰 행복감 ✔ {4} baseline 기준선 ✔\n포인트 ▶ 영영풀이는 핵심 단어(moving, guests, comparison)로 판단.",
    [['nomadic', '유목의'], ['settled', '정착한'], ['generous', '너그러운'], ['comparison', '비교']])

T.fixed('다음 (a)~(g) 중 어법상 <u>틀린</u> 것의 개수는?', '종합', BOX(
    "(a) When we have less, we tend to be more open to " + U('share') + " what we have.<br>(b) They will open up their homes and " + U('give') + " you their food and hospitality.<br>(c) The more we have, the more sophisticated our security to keep people " + U('away') + ".<br>(d) The euphoria of first love fades, and so " + U('is') + " the despair of a break-up.<br>(e) When they get " + U('what') + " they've longed for, they believe they will be happy.<br>(f) This tendency is best " + U('seen') + " with little kids and their toy joy.<br>(g) Whether we feel happy or sad " + U('is') + " not determined merely by each moment."),
    ['1개', '2개', '3개', '4개', '5개'], 2,
    "이유 ▶ 틀린 것 (a) (d) 2개. (a) be open to의 to는 전치사 → 동명사 <i>sharing</i> (d) 앞의 일반동사 fades를 받으므로 대동사 <i>does</i>\n오답 ▶ (b) will 뒤 open up과 병렬 동사원형 ✔ (c) keep A away(A를 멀리하다) ✔ (e) 선행사 없는 관계대명사 what(~하는 것) + long for의 목적어 빠진 절 ✔ (f) 경향이 '보이는' 수동태 be seen ✔ (g) 명사절 주어 → 단수 is ✔\n포인트 ▶ to 뒤가 전치사인 표현: be open to, look forward to, be used to + -ing.",
    [['be open to -ing', '~하는 데 열려 있다'], ['so + 동사 + 주어', '~도 그렇다'], ['long for', '갈망하다']], en=False)

T.render()
