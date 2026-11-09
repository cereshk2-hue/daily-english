from wu import *
# 40·41~42번
K1 = "Vision is influenced by our preconceptions about reality."
K2 = "In viewing a scene, we establish unconscious hierarchies that reflect our functional relationship to objects and our momentary priorities."
K3 = "For example, when visualizing a hammer in our mind's eye, we tend to “see” it in profile or at some other “ready for use” angle."
K4 = "One would probably not visualize a hammer as seen from the top so that the handle is hidden by the hammer's head."
K5 = "The functional relationship we have with objects creates visual expectations that interfere with our ability to see “like a camera.”"
K6 = "The camera, like the human eye, sees only shapes and colors."
K7 = "It documents the world impartially through a lens that is similar to the eye."
K8 = "When we look at them carefully, photographs are often surprising because they don't interpret confusing details but simply serve them up to us with a mechanical indifference."
K9 = "And because of their flatness, photographs often contain areas that appear as unrecognizable colors and shapes."
P40 = ' '.join([K1, K2, K3, K4, K5, K6, K7, K8, K9])
L1 = "“May I help you?” are the worst four words that a retail salesperson can utter because they don't encourage the customer to talk and put them on the defensive."
L2 = "The four words usually draw out a negative response that stops cold a sales transaction."
L3 = "Examples of better questions to use when approaching customers are “Is there anything in particular that you are looking for?” and “Are you shopping for a gift?”"
L4 = "If a fashion salesperson approached you with “May I help you?” chances are you would feel the salesperson didn't care."
L5 = "This line is a rote approach that is so overused by untrained and uninterested salespeople."
L6 = "In fact, most of us shudder in horror on hearing these words."
L7 = "The very meaning of the question “May I help you?” implies that the customer is in trouble of some sort and needs rescuing."
L8 = "This almost always puts the customer on the defense."
L9 = "“No, thank you” is usually the immediate response, even if the customer is actually in need of assistance."
L10 = "The subconscious thought by the customer is often “I'm smart enough to figure out what I want, and I don't need your help!”"
L11 = "If customers feel pressured or cornered, then salespeople won't make any sales."
L12 = "The approach has to promote a comfortable environment that makes customers feel there is no rush."
L13 = "Furthermore, if customers just want to look around, they should feel that it is all right to do so."
L14 = "In situations where customers really do want to look around on their own, salespeople should give customers their business cards and keep themselves accessible in case customers have questions or concerns."
P41 = ' '.join([L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12, L13, L14])

T = Test('4042', '40·41~42번', '기대가 만드는 시각 · "May I help you?"의 함정', '40·41~42번',
         '범위: 40번(사물과의 기능적 관계 때문에 우리는 카메라처럼 보지 못한다) · 41~42번(손님을 방어적으로 만드는 "May I help you?"). 지문은 원문을 일부 바꾼 것이 있어요. 선택지는 본문 표현을 다른 말로 바꿔 썼으니 뜻을 정확히 따져 보세요.')

# ── 40번 ──
T.flex('다음 글의 요지로 가장 적절한 것은?', '40번', BOX(P40), [
    '우리는 사물을 어떻게 쓰는지에서 생긴 기대 때문에 카메라처럼 있는 그대로 보지 못한다.',
    '카메라는 사람의 눈보다 세상을 더 심하게 왜곡해서 보여 준다.',
    '망치는 옆에서 볼 때 가장 쓰기 편한 모양을 하고 있다.',
    '사진은 평평하기 때문에 아무런 정보도 전해 주지 못한다.',
    '우선순위를 분명히 정하면 시각적 기억력이 좋아진다.'],
    "이유 ▶ Vision is influenced by our preconceptions(시각은 선입견의 영향을 받는다) + 사물과의 기능적 관계가 만든 시각적 기대가 카메라처럼 보는 능력을 방해한다(K5).\n오답 ▶ {1} 카메라는 공정하게(impartially) 기록한다 {2} 망치는 예시일 뿐, 망치의 모양이 주제가 아니다 {3} 알아보기 힘든 부분이 있을 뿐 정보가 없다는 말은 아니다 {4} 기억력 이야기는 없다\n포인트 ▶ 첫 문장(주제문) + 예시(망치) + 카메라와의 대조.",
    [['preconception', '선입견'], ['distort', '왜곡하다'], ['functional', '기능적인'], ['priority', '우선순위']], en=False)

T.flex('다음 빈칸에 들어갈 말로 가장 적절한 것은?', '40번 변형', BOX(
    'Vision is influenced by ' + BL + '. ' + K2 + ' ' + K3 + ' ' + K4 + ' ' + K5), [
    ('what we already believe about the world', '세상에 대해 우리가 이미 믿고 있는 것'),
    ('the quality of the camera we use', '우리가 쓰는 카메라의 품질'),
    ('the amount of light in the room', '방 안의 빛의 양'),
    ('the colors that surround us', '우리를 둘러싼 색깔들'),
    ('the actual size of the objects we see', '우리가 보는 물체의 실제 크기')],
    "이유 ▶ 원문: our preconceptions about reality(현실에 대한 선입견). 망치를 쓰기 좋은 각도로 떠올리듯, 사물과의 관계에서 생긴 기대가 보는 방식을 정한다 = 우리가 이미 믿고 있는 것.\n오답 ▶ {1} 카메라는 대조 대상일 뿐 {2}·{3}·{4} 빛·색·크기 같은 물리적 조건은 다루지 않는다\n포인트 ▶ preconception = pre(미리) + conception(생각) → 이미 가지고 있는 생각.",
    [['preconception', '선입견'], ['quality', '품질'], ['surround', '둘러싸다']])

T.flex('다음 글의 내용과 일치하지 <u>않는</u> 것은?', '40번', BOX(P40), [
    ('People usually imagine a hammer as viewed from directly above.', '사람들은 보통 망치를 바로 위에서 본 모습으로 떠올린다.'),
    ('The way we see things reflects how we use them.', '우리가 사물을 보는 방식은 그것을 어떻게 쓰는지를 반영한다.'),
    ('A camera records nothing but shapes and colors.', '카메라는 모양과 색깔만을 기록한다.'),
    ('Photographs present confusing details without interpreting them.', '사진은 혼란스러운 세부를 해석하지 않고 보여 준다.'),
    ('Flat photographs may include parts that are hard to recognize.', '평평한 사진에는 알아보기 어려운 부분이 있을 수 있다.')],
    "이유 ▶ One would probably not visualize a hammer as seen from the top(위에서 본 망치는 아마 떠올리지 않을 것이다) → 옆모습이나 '쓰기 좋은' 각도로 떠올린다 ✗\n오답 ▶ {1} hierarchies that reflect our functional relationship to objects ✔ {2} sees only shapes and colors ✔ (nothing but = only) {3} they don't interpret confusing details but simply serve them up ✔ {4} because of their flatness ~ unrecognizable colors and shapes ✔\n포인트 ▶ in profile(옆모습) ↔ from the top(위에서).",
    [['directly above', '바로 위에서'], ['nothing but', '오직 ~만'], ['interpret', '해석하다']])

T.fixed('다음 글의 밑줄 친 부분 중, 문맥상 낱말의 쓰임이 적절하지 <u>않은</u> 것은?', '40번 변형', BOX(
    K1 + " In viewing a scene, we establish " + CN(1, 'unconscious') + " hierarchies that reflect our functional relationship to objects and our momentary priorities. " + K3 + " One would probably not visualize a hammer as seen from the top so that the handle is " + CN(2, 'hidden') + " by the hammer's head. The functional relationship we have with objects creates visual expectations that " + CN(3, 'enhance') + " our ability to see “like a camera.” " + K6 + " It documents the world " + CN(4, 'impartially') + " through a lens that is similar to the eye. " + K8 + " And because of their flatness, photographs often contain areas that appear as " + CN(5, 'unrecognizable') + " colors and shapes."),
    ['unconscious', 'hidden', 'enhance', 'impartially', 'unrecognizable'], 3,
    "이유 ▶ 기능적 관계가 만든 기대 때문에 우리는 카메라처럼 보지 '못한다' → 그 능력을 '방해한다' <i>interfere with</i>. enhance(높이다)는 반대.\n오답 ▶ ① '무의식적인' 위계를 세운다 ✔ ② 위에서 보면 손잡이가 망치 머리에 '가려진다' ✔ ④ 카메라는 세상을 '공정하게(치우침 없이)' 기록한다 ✔ ⑤ 평평해서 '알아볼 수 없는' 색과 모양이 생긴다 ✔\n포인트 ▶ 사람의 눈(기대·해석 있음) ↔ 카메라(공정·기계적) 대조.",
    [['unconscious', '무의식적인'], ['enhance', '높이다, 향상시키다'], ['interfere with', '~을 방해하다'], ['impartially', '공정하게']])

T.fixed('다음 글의 밑줄 친 부분 중, 어법상 <u>틀린</u> 것은?', '40번 변형', BOX(
    "In viewing a scene, we establish unconscious hierarchies " + CN(1, 'that') + " reflect our functional relationship to objects and our momentary priorities. For example, when " + CN(2, 'visualizing') + " a hammer in our mind's eye, we tend to “see” it in profile or at some other “ready for use” angle. One would probably not visualize a hammer as " + CN(3, 'seen') + " from the top so that the handle is hidden by the hammer's head. The functional relationship we have with objects " + CN(4, 'create') + " visual expectations that interfere with our ability " + CN(5, 'to see') + " “like a camera.”"),
    ['that', 'visualizing', 'seen', 'create', 'to see'], 4,
    "이유 ▶ 주어는 The functional relationship(단수), we have with objects는 목적격 관계대명사가 생략된 수식어 → <i>creates</i>.\n오답 ▶ ① 선행사 hierarchies, 주어 역할 관계대명사 ✔ ② when (we are) visualizing: 접속사 뒤 분사, 우리가 '떠올리는' 능동 ✔ ③ 망치가 위에서 '보이는' 수동 ✔ ⑤ ability를 꾸미는 to부정사 ✔\n포인트 ▶ 명사 + (that) 주어 + 동사 수식어가 붙은 긴 주어 → 맨 앞 명사에 수 일치.",
    [['hierarchy', '위계, 서열'], ['visualize', '마음속에 그리다'], ['in profile', '옆모습으로']])

T.table('(A), (B), (C)의 각 네모 안에서 어법에 맞는 표현으로 가장 적절한 것은?', '40번', BOX(
    "In <b>(A)</b> [ viewing / viewed ] a scene, we establish unconscious hierarchies that reflect our functional relationship to objects and our momentary priorities. … When we look at them carefully, photographs are often surprising because they don't interpret confusing details but simply <b>(B)</b> [ serve / serving ] them up to us with a mechanical indifference. And because of their flatness, photographs often contain areas that <b>(C)</b> [ appear / appears ] as unrecognizable colors and shapes."),
    ['(A)', '(B)', '(C)'], [['viewing', 'serve', 'appear'], ['viewed', 'serve', 'appear'], ['viewing', 'serving', 'appear'], ['viewing', 'serve', 'appears'], ['viewed', 'serving', 'appears']],
    "이유 ▶ (A) 전치사 In + 동명사, 뒤에 목적어 a scene → <i>viewing</i> (B) don't interpret과 but으로 병렬, don't에 이어지는 동사원형 → <i>serve</i> (C) 관계대명사 that의 선행사 areas(복수) → <i>appear</i>\n오답 ▶ viewed: 전치사 뒤 과거분사 불가, 목적어도 있다 / serving: not A but B 병렬이 깨진다 / appears: 선행사를 단수로 착각\n포인트 ▶ not A but B (A가 아니라 B) — A, B는 같은 형태.",
    [['view', '보다'], ['serve up', '내놓다, 제공하다'], ['indifference', '무관심']])

T.fixed('글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳은?', '40번', GIV(K4) + '\n' + BOX(
    K1 + GP(1) + K2 + GP(2) + K3 + GP(3) + K5 + GP(4) + K6 + GP(5) + K7),
    None, 3,
    "이유 ▶ 망치를 옆모습이나 '쓰기 좋은' 각도로 떠올린다(K3) → 위에서 본 망치는 떠올리지 않는다(주어진 문장, 같은 예의 반대쪽) → 기능적 관계가 시각적 기대를 만든다는 정리(K5). ③.\n오답 ▶ ①② 망치 예시(For example)가 나오기 전이라 a hammer가 갑자기 나온다 ④⑤ 카메라 이야기로 넘어간 뒤라 흐름이 끊긴다\n포인트 ▶ 같은 예시(망치)의 긍정(see it in profile)과 부정(would not visualize ~ from the top)은 붙어 있다.",
    [['handle', '손잡이'], ['hide', '가리다']])

T.table('다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 적절한 것은?', '40번', BOX(P40) + '\n' + SUM(
    'Unlike a camera, which records the world <b>(A)</b> ' + BL + ', we see things through <b>(B)</b> ' + BL + ' shaped by how we use them.'),
    ['(A)', '(B)'], [['neutrally', 'expectations'], ['selectively', 'expectations'], ['neutrally', 'accidents'], ['emotionally', 'colors'], ['selectively', 'accidents']],
    "이유 ▶ (A) 카메라는 세상을 공정하게(impartially), 기계적인 무관심으로 기록한다 → <i>neutrally</i>(중립적으로) (B) 사물과의 기능적 관계가 시각적 기대를 만든다 → <i>expectations</i>\n오답 ▶ selectively(선택적으로)·emotionally(감정적으로): 카메라와 반대로 사람의 특징에 가깝다 / accidents(우연)·colors: 사물을 쓰는 방식에서 생기는 것은 기대\n포인트 ▶ impartially = neutrally = without bias.",
    [['neutrally', '중립적으로'], ['selectively', '선택적으로'], ['expectation', '기대']],
    ko=['중립적으로 / 기대', '선택적으로 / 기대', '중립적으로 / 우연', '감정적으로 / 색깔', '선택적으로 / 우연'])

T.flex('밑줄 친 <u>see “like a camera”</u>가 의미하는 바로 가장 적절한 것은?', '40번', BOX(P40.replace('see “like a camera.”', U('see “like a camera.”'))), [
    ('to see things just as they are, without interpreting them', '해석하지 않고 사물을 있는 그대로 보는 것'),
    ('to remember everything we have ever seen', '지금까지 본 모든 것을 기억하는 것'),
    ('to take pictures of objects quickly', '물체의 사진을 빨리 찍는 것'),
    ('to focus only on objects that are useful to us', '우리에게 쓸모 있는 물체에만 집중하는 것'),
    ('to see clearly even in the dark', '어둠 속에서도 분명히 보는 것')],
    "이유 ▶ 카메라는 모양과 색만 보고, 세상을 공정하게 기록하며, 세부를 해석하지 않고 그대로 내놓는다 → 기대나 해석 없이 있는 그대로 보는 것.\n오답 ▶ {1} 기억 이야기 아님 {2} 사진 찍는 속도가 아니다 {3} 쓸모(기능) 중심으로 보는 것은 오히려 사람의 방식 {4} 어둠 이야기는 없다\n포인트 ▶ 따옴표 친 비유는 뒤의 설명(only shapes and colors, impartially, don't interpret)에서 뜻을 찾는다.",
    [['interpret', '해석하다'], ['focus on', '~에 집중하다']])

# ── 41~42번 ──
T.flex('다음 글의 제목으로 가장 적절한 것은?', '41~42번', BOX(P41), [
    ('Stop Asking “May I Help You?”: Help Customers Feel at Ease', '"May I help you?"는 그만: 손님이 편안하게 느끼도록 하라'),
    ('How to Rescue Customers Who Are in Trouble', '곤경에 처한 손님을 구하는 방법'),
    ('Why Customers Never Need Any Help', '손님들이 결코 도움이 필요 없는 이유'),
    ('Business Cards: The Secret to Doubling Sales', '명함: 매출을 두 배로 올리는 비결'),
    ('Training Salespeople to Talk More Than Customers', '손님보다 더 많이 말하도록 판매원 훈련하기')],
    "이유 ▶ \"May I help you?\"는 손님을 방어적으로 만드는 최악의 말 → 더 나은 질문을 쓰고, 서두르지 않아도 되는 편안한 환경(comfortable environment, no rush)을 만들어야 한다.\n오답 ▶ {1} 손님이 곤경에 처했다고 암시하는 것이 문제라고 했다 {2} 실제로 도움이 필요할 때도 거절한다고 했을 뿐 {3} 명함은 혼자 둘러보려는 손님에 대한 방법의 하나 {4} 손님이 말하게 하는 것이 좋다(encourage the customer to talk)\n포인트 ▶ 문제(최악의 말) + 해결(편안한 환경)을 모두 담은 제목.",
    [['at ease', '편안한'], ['rescue', '구하다'], ['double', '두 배로 만들다']])

T.flex('다음 글의 내용과 일치하는 것은?', '41~42번', BOX(P41), [
    ('Customers often say “No, thank you” even when they actually need help.', '손님들은 실제로 도움이 필요할 때도 종종 "괜찮아요"라고 말한다.'),
    ('“May I help you?” encourages customers to talk freely.', '"May I help you?"는 손님이 자유롭게 말하도록 북돋운다.'),
    ('Most shoppers are pleased to hear “May I help you?”', '대부분의 쇼핑객은 "May I help you?"를 들으면 기뻐한다.'),
    ('Salespeople should stay close to customers who want to look around alone.', '판매원은 혼자 둘러보고 싶어 하는 손님 곁에 바짝 붙어 있어야 한다.'),
    ('The writer suggests asking customers whether they are in trouble.', '글쓴이는 손님에게 곤경에 처했는지 물어보라고 제안한다.')],
    "이유 ▶ \"No, thank you\" is usually the immediate response, even if the customer is actually in need of assistance ✔\n오답 ▶ {1} they don't encourage the customer to talk ✗ {2} most of us shudder in horror on hearing these words(대부분 이 말을 들으면 몸서리친다) {3} 명함을 주고 필요할 때 다가갈 수 있게(accessible) 있으라 — 바짝 붙어 있으라는 말이 아니다 {4} 곤경에 처했다고 암시하는 것이 바로 문제\n포인트 ▶ accessible(필요할 때 다가갈 수 있는) ≠ stay close(바짝 붙어 있다).",
    [['be in need of', '~이 필요하다'], ['shopper', '쇼핑객'], ['stay close to', '~ 곁에 바짝 있다']])

T.flex('다음 빈칸에 들어갈 말로 가장 적절한 것은?', '41~42번 변형', BOX(
    L10 + ' ' + L11 + ' The approach has to promote a comfortable environment that makes customers feel ' + BL + '. ' + L13 + ' ' + L14), [
    ('they can take their time', '시간을 충분히 가져도 된다'),
    ('they must buy something quickly', '빨리 무언가를 사야 한다'),
    ('the salesperson is watching them closely', '판매원이 자신을 가까이서 지켜보고 있다'),
    ('they are in trouble and need rescuing', '곤경에 처해 구조가 필요하다'),
    ('the store is about to close', '가게가 곧 문을 닫는다')],
    "이유 ▶ 원문: there is no rush(서두를 필요가 없다) = they can take their time(시간을 충분히 가져도 된다). 압박을 느끼면 사지 않고, 그냥 둘러보고 싶으면 그래도 괜찮다고 느껴야 한다.\n오답 ▶ {1}·{4} 압박감(pressured)을 주는 상황 {2} 감시받는 느낌도 편안한 환경과 반대 {3} \"May I help you?\"가 주는 잘못된 느낌\n포인트 ▶ comfortable environment(편안한 환경)와 앞뒤의 pressured(압박을 받는) ↔ all right to look around로 판단.",
    [['take one\'s time', '천천히 하다'], ['rush', '서두름'], ['be about to V', '막 ~하려 하다']])

T.fixed('다음 글의 밑줄 친 부분 중, 문맥상 낱말의 쓰임이 적절하지 <u>않은</u> 것은?', '41~42번 변형', BOX(
    "“May I help you?” are the worst four words that a retail salesperson can utter because they don't encourage the customer to talk and put them on the defensive. The four words usually draw out a " + CN(1, 'positive') + " response that stops cold a sales transaction. Examples of " + CN(2, 'better') + " questions to use when approaching customers are “Is there anything in particular that you are looking for?” and “Are you shopping for a gift?” " + L4 + " This line is a rote approach that is so " + CN(3, 'overused') + " by untrained and uninterested salespeople. " + L6 + ' ' + L7 + ' ' + L8 + " “No, thank you” is usually the " + CN(4, 'immediate') + " response, even if the customer is actually in need of assistance. … In situations where customers really do want to look around on their own, salespeople should give customers their business cards and keep themselves " + CN(5, 'accessible') + " in case customers have questions or concerns."),
    ['positive', 'better', 'overused', 'immediate', 'accessible'], 1,
    "이유 ▶ 판매를 즉시 멈추게 하는(stops cold a sales transaction) 반응이므로 '부정적인' 반응 → <i>negative</i>. positive(긍정적인)는 거래를 멈추게 한다는 말과 맞지 않는다.\n오답 ▶ ② '더 나은' 질문의 예 ✔ ③ 훈련받지 않은 판매원들이 '너무 많이 쓰는' 판에 박힌 말 ✔ ④ \"괜찮아요\"가 보통 '즉각적인' 반응 ✔ ⑤ 질문이 있을 때 '다가갈 수 있게' 있어야 한다 ✔\n포인트 ▶ stop cold(딱 멈추게 하다) → 앞의 response는 부정적.",
    [['draw out', '끌어내다'], ['stop cold', '딱 멈추게 하다'], ['rote', '기계적인, 판에 박힌'], ['accessible', '다가가기 쉬운']])

T.fixed('다음 글의 밑줄 친 부분 중, 어법상 <u>틀린</u> 것은?', '41~42번 변형', BOX(
    "“May I help you?” is the worst question that a retail salesperson can ask because it doesn't encourage the customer " + CN(1, 'to talk') + ". Examples of better questions to use when approaching customers " + CN(2, 'is') + " “Is there anything in particular that you are looking for?” and “Are you shopping for a gift?” If a fashion salesperson approached you with “May I help you?” chances are you " + CN(3, 'would feel') + " the salesperson didn't care. In fact, most of us shudder in horror on " + CN(4, 'hearing') + " these words. The very meaning of the question implies that the customer is in trouble of some sort and needs " + CN(5, 'rescuing') + "."),
    ['to talk', 'is', 'would feel', 'hearing', 'rescuing'], 2,
    "이유 ▶ 주어는 Examples(복수), of better questions to use ~ customers는 수식어 → <i>are</i>.\n오답 ▶ ① encourage + 목적어 + to부정사 ✔ ③ If + 과거(approached), 주절 would + 동사원형: 가정법 과거 ✔ ④ on -ing(~하자마자) ✔ ⑤ need -ing = need to be p.p.(구조될 필요가 있다) ✔\n포인트 ▶ 'Examples of ~ are A and B': 주어 Examples에 수 일치.",
    [['retail', '소매의'], ['chances are (that)', '아마 ~일 것이다'], ['shudder', '몸서리치다'], ['need -ing', '~될 필요가 있다']])

T.table('(A), (B), (C)의 각 네모 안에서 어법에 맞는 표현으로 가장 적절한 것은?', '41~42번', BOX(
    "If customers feel <b>(A)</b> [ pressured / pressuring ] or cornered, then salespeople won't make any sales. … In situations <b>(B)</b> [ where / which ] customers really do want to look around on their own, salespeople should give customers their business cards and keep <b>(C)</b> [ themselves / them ] accessible in case customers have questions or concerns."),
    ['(A)', '(B)', '(C)'], [['pressured', 'where', 'themselves'], ['pressuring', 'where', 'themselves'], ['pressured', 'which', 'themselves'], ['pressured', 'where', 'them'], ['pressuring', 'which', 'them']],
    "이유 ▶ (A) 손님이 압박을 '받는' 느낌 → 과거분사 <i>pressured</i> (뒤의 cornered와 병렬) (B) 선행사 situations + 완전한 절(customers really do want to look around) → 관계부사 <i>where</i> (C) keep의 목적어가 주어 salespeople 자신 → 재귀대명사 <i>themselves</i>\n오답 ▶ pressuring: 손님이 남을 압박하는 뜻 / which: 뒤에 빠진 성분이 없는 완전한 절 / them: 주어와 같은 대상이면 재귀대명사\n포인트 ▶ 관계부사(where) + 완전한 절, 관계대명사(which) + 불완전한 절.",
    [['pressure', '압박하다'], ['corner', '궁지에 몰다'], ['on one\'s own', '혼자서']])

T.fixed('주어진 글 다음에 이어질 글의 순서로 가장 적절한 것은?', '41~42번', GIV(L4 + ' ' + L5 + ' ' + L6) + '\n' + BOX(
    '<b>(A)</b> ' + L11 + ' ' + L12 + '</p><p><b>(B)</b> ' + L7 + ' ' + L8 + '</p><p><b>(C)</b> ' + L9 + ' ' + L10),
    ['(A) − (C) − (B)', '(B) − (A) − (C)', '(B) − (C) − (A)', '(C) − (A) − (B)', '(C) − (B) − (A)'], 3,
    "이유 ▶ 주어진 글: 대부분 이 말을 들으면 몸서리친다 → (B) 그 질문의 뜻 자체가 손님이 곤경에 처했다고 암시, 이것이 손님을 방어적으로 만든다 → (C) 그래서 \"괜찮아요\"가 즉각적인 반응, 속으로는 '도움 필요 없어!' → (A) 손님이 압박을 느끼면 팔지 못하니 편안한 환경을 만들어야 한다.\n오답 ▶ (C)의 \"No, thank you\"는 (B)의 '방어적이 됨'의 결과 / (A)의 pressured or cornered는 (C)의 방어적인 속마음을 일반화한 해결책\n포인트 ▶ 원인(곤경 암시) → 반응(거절) → 해결(편안한 환경).",
    [['imply', '암시하다'], ['on the defense', '방어적인'], ['subconscious', '잠재의식의']], en=False)

T.fixed('글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳은?', '41~42번', GIV(L3) + '\n' + BOX(
    L1 + GP(1) + L2 + GP(2) + L4 + GP(3) + L5 + GP(4) + L6 + GP(5) + L7),
    None, 2,
    "이유 ▶ 앞에서 \"May I help you?\"가 최악의 말이고 부정적인 반응을 끌어낸다(L1·L2)고 한 뒤 '더 나은 질문의 예(Examples of better questions)'가 와야 한다. 뒤의 L4는 다시 \"May I help you?\"로 다가오면 어떻게 느끼는지로 이어진다 → ②.\n오답 ▶ ① L2의 The four words(그 네 단어)는 L1의 \"May I help you?\"를 바로 받아야 하므로 사이에 넣을 수 없다 ③~⑤ This line(L5)·these words(L6)·the question(L7)이 모두 \"May I help you?\"를 가리켜 흐름이 끊긴다\n포인트 ▶ better(더 나은) → 앞에 나쁜 예가 먼저 나와야 한다.",
    [['in particular', '특별히'], ['approach', '다가가다']])

T.flex('글에 따르면 “May I help you?”라는 말이 손님을 방어적으로 만드는 이유로 가장 적절한 것은?', '41~42번', BOX(P41), [
    '손님이 무언가 곤란한 상황에 있어 구조가 필요하다는 뜻을 담고 있어서',
    '판매원이 너무 많은 정보를 한꺼번에 전해서',
    '손님에게 선물을 사라고 강요하는 말이어서',
    '판매원이 명함을 먼저 건네지 않아서',
    '질문이 너무 길고 복잡해서'],
    "이유 ▶ The very meaning of the question implies that the customer is in trouble of some sort and needs rescuing. This almost always puts the customer on the defense. = 곤경에 처해 구조가 필요하다는 뜻이 손님을 방어적으로 만든다.\n오답 ▶ {1} 정보량 이야기는 없다 {2} \"Are you shopping for a gift?\"는 오히려 더 나은 질문 {3} 명함은 혼자 둘러보는 손님을 위한 방법 {4} 네 단어(four words)로 짧다\n포인트 ▶ 원인 문장(implies that ~) 바로 뒤에 This puts ~ on the defense.",
    [['imply', '암시하다'], ['in trouble', '곤경에 처한'], ['force', '강요하다']], en=False)

T.table('다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 적절한 것은?', '41~42번', BOX(P41) + '\n' + SUM(
    'Instead of asking “May I help you?”, which tends to make customers <b>(A)</b> ' + BL + ', salespeople should create a(n) <b>(B)</b> ' + BL + ' atmosphere where customers can look around freely.'),
    ['(A)', '(B)'], [['defensive', 'relaxed'], ['defensive', 'urgent'], ['grateful', 'relaxed'], ['curious', 'competitive'], ['grateful', 'formal']],
    "이유 ▶ (A) 이 말은 손님을 방어적으로 만든다(puts them on the defensive) → <i>defensive</i> (B) 서두르지 않아도 되는 편안한 환경(comfortable environment, no rush) → <i>relaxed</i>\n오답 ▶ grateful(고마워하는)·curious(호기심 있는): 대부분 몸서리친다(shudder in horror)고 했다 / urgent(급한)·competitive(경쟁적인)·formal(격식 있는): 편안한 분위기와 거리가 멀다\n포인트 ▶ on the defensive = defensive(방어적인).",
    [['defensive', '방어적인'], ['relaxed', '편안한'], ['urgent', '급한']],
    ko=['방어적인 / 편안한', '방어적인 / 급한', '고마워하는 / 편안한', '호기심 있는 / 경쟁적인', '고마워하는 / 격식 있는'])

# ── 종합 ──
T.flex('40·41~42번 지문에 나온 단어와 영영풀이가 바르게 짝지어지지 <u>않은</u> 것은?', '종합', '', [
    '<b>impartially</b> : in a way that favors one side over another',
    '<b>preconception</b> : an idea formed before having enough information or experience',
    '<b>utter</b> : to say something out loud',
    '<b>rote</b> : done from habit, without thinking about the meaning',
    '<b>accessible</b> : easy to reach, approach, or talk to'],
    "이유 ▶ impartially는 '공정하게, 치우침 없이'(without favoring one side). 한쪽 편을 든다는 풀이는 반대(partially, with bias).\n오답 ▶ {1} preconception 선입견 ✔ {2} utter (말을) 하다 ✔ {3} rote 기계적인, 판에 박힌 ✔ {4} accessible 다가가기 쉬운 ✔\n포인트 ▶ im-(= not) + partial(편파적인) → 편파적이지 않게.",
    [['impartially', '공정하게'], ['favor', '편들다'], ['habit', '습관']])

T.render()
