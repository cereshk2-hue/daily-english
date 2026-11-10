from jfw import *
p = load(24, '24번 · 글의 제목')
VOCAB = words(24)
EXAM = [EXQ(24, '24. 다음 글의 제목으로 가장 적절한 것은?', p.full(), [
 "Love Yourself to Better Your Future!", "When an Ambitious Goal Brings Stress", "How Can We Plan Good Daily Routines?",
 "Fantasizing About the Future: A Barrier to Action", "Too Many Goals, Too Little Time: A Recipe for Failure"], 3,
 "정답 ▶ ④ 미래에 대한 환상: 행동의 장애물\n이유: 목표에 대한 '상상'과 사랑에 빠지면 일상이 얼마나 달라져야 하는지 생각하지 않음 → 긍정적 환상이 거짓되고 때 이른 성취감을 줘서 노력을 '덜' 하게 함 → 행동해야 할 필요가 유발되지 않음(a necessity to act is not induced)\n오답 ▶ ① 자기 사랑 ✗ ② 목표가 주는 스트레스 ✗ ③ 일과 계획법 ✗ ⑤ 목표가 너무 많다는 이야기 ✗\n포인트 ▶ barrier = 장애물 · fantasize = 환상을 품다", v=False),
 EXQ(24, '다음 글의 요지로 가장 적절한 것은?', p.full(), [
 "미래에 대한 긍정적 환상은 노력을 줄여 목표 달성을 방해할 수 있다.", "긍정적인 상상은 목표 달성의 가장 강력한 동기이다.", "목표는 크고 낭만적일수록 달성하기 쉽다.",
 "새로운 행동은 삶에 쉽게 통합될 수 있다.", "연구에 따르면 목표를 자주 바꾸는 것이 좋다."], 0,
 "정답 ▶ ① 미래에 대한 긍정적 환상은 노력을 줄여 목표 달성을 방해할 수 있다.\n이유: positive fantasies about our future can lead us to put less effort into our goals\n오답 ▶ ② 반대 ③ 낭만화(romanticize)는 문제점 ④ 복잡함과 어려움을 얼버무린다고 함 ⑤ 언급 없음"),
 EXQ(24, '다음 빈칸에 들어갈 말로 가장 적절한 것은?', p.blank('less'), [
 "less", "more", "equal", "regular", "creative"], 0,
 "정답 ▶ ① less (더 적은)\n이유: because 이하 — 환상이 '거짓되고 때 이른 성취감'을 주니, 이미 이룬 것 같아서 노력을 '덜' 기울여요.\n오답 ▶ ② more 더 많은(반대) ③ equal 같은 ④ regular 규칙적인 ⑤ creative 창의적인\n포인트 ▶ premature sense of accomplishment = 때 이른 성취감")]
PICK1 = [PK(p, 'Unfortunately', 'disconnected', 'connected', "정답 ▶ disconnected (동떨어진)\n오답 ▶ connected (연결된)\n이유: Unfortunately(안타깝게도) — 목표에 대한 상상이 현실과 '동떨어져' 있다는 문제 제기"),
 PK(p, 'We fall in love', 'different', 'similar', "정답 ▶ different (다른)\n오답 ▶ similar (비슷한)\n이유: 목표를 이루려면 하루하루가 얼마나 '달라져야' 하는지를 생각에서 밀어냄"),
 PK(p, 'In fact, research', 'false', 'genuine', "정답 ▶ false (거짓된)\n오답 ▶ genuine (진짜의)\n이유: 아직 이루지 않았는데 느끼는 성취감 → '거짓되고 때 이른'"),
 PK(p, 'In fact, research', 'premature', 'delayed', "정답 ▶ premature (때 이른)\n오답 ▶ delayed (늦은)\n이유: 실제로 이루기 '전에' 미리 느끼는 성취감"),
 PK(p, 'In the process', 'complex', 'simple', "정답 ▶ complex (복잡한)\n오답 ▶ simple (단순한)\n이유: 복잡함과 어려움(intricacies and challenges)을 얼버무린다 → 새 행동은 '복잡한' 것"),
 PK(p, 'As one study', 'not induced', 'strongly induced', "정답 ▶ not induced (유발되지 않는)\n오답 ▶ strongly induced (강하게 유발되는)\n이유: 미래를 머릿속으로 미리 즐기니 행동할 필요를 느끼지 못함")]
TF = [TF(p, "The idea of a goal is sometimes separated from the daily reality of achieving it.", True, "the idea of a goal is disconnected from the daily reality", "정답 ▶ T\n이유: 목표에 대한 상상이 일상의 현실과 동떨어져 있어요.\n어휘 ▶ separated ≒ disconnected"),
 TF(p, "We carefully think about how our daily life must change to reach a goal.", False, "pushing out of mind how different our day-to-day will need to be", "정답 ▶ F\n이유: 하루하루가 얼마나 달라져야 할지를 생각에서 밀어내요."),
 TF(p, "Research suggests positive fantasies can make us put less effort into our goals.", True, "lead us to put less effort into our goals", "정답 ▶ T\n이유: 긍정적 환상이 노력을 덜 기울이게 할 수 있어요."),
 TF(p, "Our fantasies give us a real sense of accomplishment.", False, "a false and premature sense of accomplishment", "정답 ▶ F\n이유: 거짓되고 때 이른 성취감이에요."),
 TF(p, "When we romanticize a goal, we pay close attention to its challenges.", False, "we gloss over the intricacies and challenges", "정답 ▶ F\n이유: 복잡함과 어려움을 얼버무리고 넘어가요.\n어휘 ▶ gloss over ↔ pay close attention to"),
 TF(p, "Fantasizing lets a person enjoy the desired future in the mind now.", True, "mentally enjoy the desired future in the here and now", "정답 ▶ T\n이유: 원하는 미래를 지금 머릿속으로 즐기게 해요.")]
MC = [MC(p, "글의 내용과 일치하지 <u>않는</u> 것은?", [
 "Positive fantasies strongly encourage people to take action.", "We may fall in love with the idea of a change.", "Fantasies can give us a feeling of success too early.",
 "We tend to ignore how hard it is to adopt a new behavior.", "We often fail to think about why our fantasy has not come true."],
 "정답 ▶ Positive fantasies strongly encourage people to take action.\n이유: a necessity to act is not induced (행동해야 할 필요가 유발되지 않음)\n포인트 ▶ too early = premature · ignore ≒ gloss over · adopt a new behavior ≒ integrate a new behavior into our life · fail to think about ≒ don’t reflect on",
 [["긍정적 환상은 사람들이 행동하도록 강하게 격려한다.", "a necessity to act is not induced", "✗ 반대"], ["우리는 변화에 대한 상상과 사랑에 빠질 수 있다.", "falling in love with the idea of a change", "일치"], ["환상은 너무 일찍 성공의 느낌을 줄 수 있다.", "a false and premature sense of accomplishment", "too early = premature"], ["새 행동을 받아들이는 것이 얼마나 어려운지 무시하는 경향이 있다.", "we gloss over the intricacies and challenges", "ignore ≒ gloss over"], ["왜 환상이 실현되지 않았는지 생각하지 않는다.", "we don’t reflect on why our fantasy is not yet our future", "일치"]]),
 MC(p, "글의 내용과 <u>일치하는</u> 것은?", ["우리는 목표를 낭만화하며 새로운 행동의 어려움을 얼버무린다.", "긍정적 환상은 노력을 더 많이 기울이게 한다.", "목표에 대한 상상은 항상 현실과 일치한다.", "환상은 진짜 성취감을 준다.", "환상을 품으면 행동할 필요를 강하게 느낀다."],
 "정답 ▶ 우리는 목표를 낭만화하며 새로운 행동의 어려움을 얼버무린다.\n이유: We romanticize a goal ~ we gloss over the intricacies and challenges\n오답 ▶ ② less effort ③ disconnected ④ false ⑤ not induced",
 [["", "we gloss over the intricacies and challenges", "일치 ✔"], ["", "put less effort", "덜"], ["", "is disconnected from the daily reality", "동떨어짐"], ["", "a false and premature sense", "거짓"], ["", "a necessity to act is not induced", "유발 안 됨"]])]
PICK2 = [PK(p, 'Unfortunately', 'what it will take', 'that it will take', "정답 ▶ what\n이유: 전치사 of 뒤 + take의 목적어가 빠진 불완전한 절 → 선행사를 포함한 what(~하는 것)"),
 PK(p, 'Unfortunately', 'to achieve', 'achieving', "정답 ▶ to achieve\n이유: it takes A to do — '~하는 데 A가 필요하다' 구문의 to부정사"),
 PK(p, 'We fall in love', 'pushing', 'push', "정답 ▶ pushing\n이유: 주절 We fall ~ 뒤 콤마 + 분사구문 (주어 We가 밀어내는 능동)"),
 PK(p, 'We fall in love', 'our day-to-day will', 'will our day-to-day', "정답 ▶ our day-to-day will\n이유: 간접의문문(how different + 주어 + 동사) → 평서문 어순"),
 PK(p, 'We fall in love', 'for us', 'of us', "정답 ▶ for\n이유: to부정사의 의미상 주어 = for + 목적격 (for us to make it happen)"),
 PK(p, 'We fall in love', 'happen.', 'to happen.', "정답 ▶ happen\n이유: 사역동사 make + 목적어 + 동사원형"),
 PK(p, 'In fact, research', 'with a false', 'to a false', "정답 ▶ with\n이유: provide A with B (A에게 B를 제공하다)")]
VERB = [VB(p, 'In fact, research', 'put', 'put', "x"),
 VB(p, 'In the process', 'integrating', 'integrate', "정답 ▶ integrating\n이유: 전치사 of 뒤 동명사"),
 VB(p, 'We romanticize', 'falling', 'fall', "정답 ▶ falling\n이유: 대시(—) 뒤 분사구문 — 우리가 '사랑에 빠지면서'(능동)"),
 VB(p, 'As one study', 'induced', 'induce', "정답 ▶ induced\n이유: 필요가 '유발되는' 수동 → is not induced")]
VERB = [v for v in VERB if v['v'] != v['a'][0]]
ERR = [ER(p, 'Unfortunately', ['disconnected', ('what', 'that'), 'to achieve'], 1, 'what', "틀린 곳 ▶ ② that → what\n이유: 전치사 of의 목적어 + take의 목적어 없는 불완전한 절 → what\n나머지 ▶ ① 동떨어진(수동) ✔ ③ it takes ~ to부정사 ✔"),
 ER(p, 'In fact, research', ['that', ('put', 'putting'), 'with'], 1, 'put', "틀린 곳 ▶ ② putting → put\n이유: lead + 목적어 + to부정사 (lead us to put)\n나머지 ▶ ① 명사절 that ✔ ③ provide A with B ✔"),
 ER(p, 'In the process', ['gloss over', ('integrating', 'integrate'), 'complex'], 1, 'integrating', "틀린 곳 ▶ ② integrate → integrating\n이유: 전치사 of 뒤 동명사\n나머지 ▶ ① ✔ ③ 형용사 ✔")]
SCR = [0, 1, 3, 4]
ORDER = [[0, 1, 2, 3], [2, 3, 4, 5]]
INSERT = [([1, 2, 3, 4], 1, "정답 ▶ ① (In fact ~ 문장)\n이유: 목표의 상상에 빠져 현실을 외면한다(주장) → In fact(실제로) 연구도 그걸 보여 준다(근거). 그다음 We romanticize a goal로 다시 정리"),
 ([3, 4, 5], 1, "정답 ▶ ① (In the process ~ 문장)\n이유: 목표를 낭만화한다 → In the process(그 과정에서) 어려움을 얼버무린다 → 한 연구의 요약(행동할 필요가 생기지 않음)")]
ODD = [([1, 2, "Setting clear daily routines is the easiest way to enjoy our free time.", 3], 2, "정답 ▶ ③\n이유: 긍정적 환상이 노력을 줄인다는 흐름이에요. 여가를 즐기는 일과 이야기는 관계없어요.")]
BLANK = [BL(p, 'Unfortunately', 'disconnected', ["inseparable", "copied", "protected"], "정답 ▶ disconnected (동떨어진)\n이유: Unfortunately — 상상과 현실 사이의 '단절'이 문제\n오답 ▶ inseparable 분리할 수 없는 · copied 복사된 · protected 보호된"),
 BL(p, 'We romanticize', 'romanticize', ["abandon", "analyze", "share"], "정답 ▶ romanticize (낭만화하다)\n이유: 대시 뒤 '변화에 대한 상상과 사랑에 빠진다'가 같은 뜻의 설명\n오답 ▶ abandon 포기하다 · analyze 분석하다 · share 공유하다"),
 BL(p, 'As one study', 'reflect on', ["give up", "write down", "brag about"], "정답 ▶ reflect on (곰곰이 생각하다)\n이유: 환상이 '왜' 아직 미래가 아닌지 돌아보지 않으니 행동할 필요가 생기지 않음\n오답 ▶ give up 포기하다 · write down 적다 · brag about 자랑하다")]
GRAM = [{'q': "빈칸에 알맞은 것은?<br><b>The idea is disconnected from the reality of ______ it will take to achieve it.</b>", 'opts': ["what", "that", "which", "how"], 'ex': "정답 ▶ what\n이유: 전치사 뒤 + 불완전한 절(take의 목적어 없음) → what"},
 {'q': "빈칸에 알맞은 것은?<br><b>We push out of mind how different ______ to be.</b>", 'opts': ["our day-to-day will need", "will our day-to-day need", "does our day-to-day need", "need our day-to-day will"], 'ex': "정답 ▶ our day-to-day will need\n이유: 간접의문문 = 의문사 + 주어 + 동사"},
 {'q': "빈칸에 알맞은 것은?<br><b>Positive fantasies can lead us ______ less effort into our goals.</b>", 'opts': ["to put", "put", "putting", "to putting"], 'ex': "정답 ▶ to put\n이유: lead + 목적어 + to부정사"},
 {'q': "빈칸에 알맞은 것은?<br><b>Our fantasies provide us ______ a false sense of accomplishment.</b>", 'opts': ["with", "to", "for", "of"], 'ex': "정답 ▶ with\n이유: provide A with B = provide B for[to] A"}]
SUMQ = [SUM(p, "Positive fantasies about a goal can give us a (A) ______ sense of accomplishment, which makes us feel (B) ______ need to take action.", [
 "(A) false – (B) little", "(A) false – (B) a strong", "(A) real – (B) little", "(A) deep – (B) an urgent", "(A) shared – (B) no"],
 "정답 ▶ (A) false – (B) little\n(A) 거짓되고 때 이른 성취감 → false\n(B) 행동해야 할 필요가 유발되지 않음 → little(거의 없는)\n오답 ▶ real 진짜의 · a strong / an urgent 강한·긴급한(반대)",
 ["a false and premature sense of accomplishment", "a necessity to act is not induced"])]
