from jfw import *
R = PREP['40']['sents']; S = R[:5] + ['There will be no one to mate with, no one to help bring in pollinators.']
K = PREP['40']['ko'][:6]
p = P(40, '40번 · 요약문', list(zip(S, K)), ' '.join(Q['40']['foot']))
SUMS = "Compared to those in peaceful areas, goldenrods in more hostile environments send more (A)______ understandable chemical messages, thereby (B)______ both the senders and the receivers."
VOCAB = words(40)
EXAM = [EXQ(40, '40. 다음 글의 내용을 한 문장으로 요약하고자 한다. 빈칸 (A), (B)에 들어갈 말로 가장 적절한 것은?', p.full() + box('<b>↓</b><br>' + SUMS), [
 "(A) broadly – (B) benefiting", "(A) easily – (B) harming", "(A) narrowly – (B) protecting", "(A) accidentally – (B) profiting", "(A) specifically – (B) endangering"], 0,
 "정답 ▶ ① (A) broadly – (B) benefiting\n(A) 평화로운 지역의 미역취는 가까운 친족만 이해하는 '매우 특정한' 신호 ↔ 적대적 지역의 미역취는 그 지역 '모든' 미역취가 쉽게 이해하는 신호(확성기로 알리듯) → 더 '널리' 이해되는 → broadly\n(B) 이 교신은 받는 식물뿐 아니라 보내는 식물에게도 이롭다(beneficial) → 발신자·수신자 모두를 '이롭게' → benefiting\n오답 ▶ ② easily(A는 가능)지만 harming(해치다)은 반대 ③ narrowly(좁게)는 평화로운 지역의 특징 ④ accidentally(우연히) 근거 없음 ⑤ specifically(특정하게)·endangering(위험에 빠뜨리다) 모두 반대\n포인트 ▶ comprehensible only to their close kin ↔ understood by all the goldenrod in the area", v=False),
 EXQ(40, '다음 글의 주제로 가장 적절한 것은?', p.full(), [
 "how goldenrods change their chemical signals in hostile environments", "why goldenrods grow better in peaceful areas", "how predators detect chemical signals from plants",
 "ways goldenrods attract more pollinators with color", "reasons plants stop communicating when attacked"], 0,
 "정답 ▶ ① 적대적인 환경에서 미역취가 화학 신호를 바꾸는 방식\n이유: 평화로운 곳 = 친족만 아는 암호 신호 ↔ 적대적인 곳 = 모두가 이해하는 신호(확성기). 보내는 쪽에도 이로움\n오답 ▶ ② 성장 비교 ✗ ③ 포식자의 감지 ✗ ④ 색깔 ✗ ⑤ 공격받을 때 신호를 보냄(반대)"),
 EXQ(40, '다음 빈칸에 들어갈 말로 가장 적절한 것은?', p.blank('alone'), ["alone", "together", "safely", "happily", "proudly"], 0,
 "정답 ▶ ① alone (혼자)\n이유: 정말 힘든 시기엔 들판에 '혼자' 남겨지고 싶지 않음 → 짝짓기할 상대도, 꽃가루 매개자를 불러올 상대도 없을 것 → 그래서 이웃 모두에게 신호를 보내는 게 보내는 쪽에도 이로움\n오답 ▶ ② together 함께 — 원치 않는 것이 아님 ③④⑤ 근거 없음")]
PICK1 = [PK(p, 'Researchers recently', 'peaceful', 'dangerous', "정답 ▶ peaceful (평화로운)\n오답 ▶ dangerous (위험한)\n이유: 포식자의 위협이 많지 않은(without much threat) 지역 → 평화로운"),
 PK(p, 'Researchers recently', 'specific', 'general', "정답 ▶ specific (특정한)\n오답 ▶ general (일반적인)\n이유: 가까운 친족만 이해할 수 있는(comprehensible only to their close kin) → 매우 '특정한' 신호"),
 PK(p, 'Researchers recently', 'rare', 'frequent', "정답 ▶ rare (드문)\n오답 ▶ frequent (잦은)\n이유: 위협이 많지 않은 평화로운 지역이니 공격받는 일은 '드묾'"),
 PK(p, 'But goldenrods', 'hostile', 'friendly', "정답 ▶ hostile (적대적인)\n오답 ▶ friendly (우호적인)\n이유: But — 평화로운 지역과 대조되는 '적대적인' 지역"),
 PK(p, 'Instead of using', 'coded', 'open', "정답 ▶ coded (암호화된)\n오답 ▶ open (공개된)\n이유: Instead of(~ 대신) — 확성기(모두에게)와 대조되는 '암호화된 속삭임'"),
 PK(p, 'It is the first', 'beneficial', 'harmful', "정답 ▶ beneficial (이로운)\n오답 ▶ harmful (해로운)\n이유: 받는 식물뿐 아니라 보내는 식물에게도 '이롭다' → 혼자 남지 않으니까")]
TF = [TF(p, "Goldenrods in peaceful areas send signals that only close relatives understand.", True, "comprehensible only to their close kin", "정답 ▶ T\n이유: 가까운 친족만 이해하는 신호예요.\n어휘 ▶ relatives = kin"),
 TF(p, "Goldenrods in peaceful areas are attacked very often.", False, "on the rare occasion they are attacked", "정답 ▶ F\n이유: 공격받는 일은 드물어요."),
 TF(p, "Goldenrods in hostile areas use signals understood by all goldenrods nearby.", True, "easily understood by all the goldenrod in the area", "정답 ▶ T\n이유: 그 지역 모든 미역취가 쉽게 이해하는 신호를 써요."),
 TF(p, "Goldenrods in hostile areas use coded whisper networks.", False, "Instead of using coded whisper networks", "정답 ▶ F\n이유: 암호화된 속삭임 대신 확성기처럼 널리 알려요."),
 TF(p, "The research confirmed that the signals also benefit the sender.", True, "but also to the sender", "정답 ▶ T\n이유: 보내는 식물에게도 이롭다는 것을 처음 확인했어요."),
 TF(p, "Being alone in a field helps goldenrods find mates.", False, "There will be no one to mate with", "정답 ▶ F\n이유: 혼자 남으면 짝짓기할 상대가 없어요.")]
MC = [MC(p, "글의 내용과 일치하지 <u>않는</u> 것은?", [
 "Chemical communication benefits only the receiving plant.", "Peaceful-area goldenrods face little threat from predators.", "Hostile-area goldenrods signal to their neighbors.",
 "The signals in hostile areas are understood beyond biological kin.", "Without neighbors, there would be no help bringing in pollinators."],
 "정답 ▶ Chemical communication benefits only the receiving plant.\n이유: beneficial not only to the plant receiving them but also to the sender\n포인트 ▶ not only A but also B · kin = 친족",
 [["화학적 교신은 받는 식물에게만 이롭다.", "not only to the plant receiving them but also to the sender", "✗ 보내는 쪽도"], ["평화로운 지역의 미역취는 포식자 위협이 적다.", "without much threat from predators", "일치"], ["적대적 지역의 미역취는 이웃에게 신호를 보낸다.", "signal to their neighbors", "일치"], ["적대적 지역의 신호는 생물학적 친족 너머까지 이해된다.", "not just their biological kin", "일치"], ["이웃이 없으면 꽃가루 매개자를 불러들이는 도움도 없다.", "no one to help bring in pollinators", "일치"]])]
PICK2 = [PK(p, 'Researchers recently', 'goldenrods that live', 'goldenrods what live', "정답 ▶ that\n이유: 선행사 goldenrods + 주어 빠진 절 → 주격 관계대명사 that"),
 PK(p, 'Researchers recently', 'are attacked', 'attack', "정답 ▶ are attacked\n이유: 미역취가 '공격받는' 수동"),
 PK(p, 'But goldenrods', 'signal to', 'signals to', "정답 ▶ signal\n이유: 주어 goldenrods(복수). in more hostile territory는 수식어"),
 PK(p, 'But goldenrods', 'understood', 'understanding', "정답 ▶ understood\n이유: 표현이 '이해되는' 수동 → 과거분사가 chemical phrases 수식"),
 PK(p, 'Instead of using', 'using', 'to use', "정답 ▶ using\n이유: 전치사 of 뒤 동명사"),
 PK(p, 'It is the first', 'receiving', 'received', "정답 ▶ receiving\n이유: 식물이 신호를 '받는' 능동 → 현재분사 (목적어 them이 뒤에 있음)"),
 PK(p, 'When times are', 'be left', 'leave', "정답 ▶ be left\n이유: 내가 혼자 '남겨지는' 수동 → want to be left")]
VERB = [VB(p, 'Researchers recently', 'issue', 'issue', "x"),
 VB(p, 'It is the first', 'confirmed', 'confirm', "정답 ▶ confirmed\n이유: has + p.p. 현재완료"),
 VB(p, 'When times are', 'standing', 'stand', "정답 ▶ standing\n이유: be left + -ing (~한 채로 남겨지다)"),
 VB(p, 'There will be', 'to mate', 'mate', "정답 ▶ to mate\n이유: no one을 꾸미는 형용사적 to부정사 (짝짓기할 상대)"),
 VB(p, 'There will be', 'bring', 'bring', "x")]
VERB = [v for v in VERB if v['v'] != v['a'][0]]
ERR = [ER(p, 'Researchers recently', ['that', ('specific', 'specifically'), 'are attacked'], 1, 'specific', "틀린 곳 ▶ ② specifically → specific\n이유: are의 보어 → 형용사 (calls that are incredibly specific)\n나머지 ▶ ① 명사절 접속사 that ✔ ③ 수동 ✔"),
 ER(p, 'But goldenrods', ['signal', ('using', 'used'), 'understood'], 1, 'using', "틀린 곳 ▶ ② used → using\n이유: 미역취가 표현을 '사용하면서'(능동) → 현재분사, 목적어 chemical phrases\n나머지 ▶ ① 복수 주어 ✔ ③ 수동 과거분사 ✔"),
 ER(p, 'When times are', ['truly', ('be left', 'leave'), 'standing'], 1, 'be left', "틀린 곳 ▶ ② leave → be left\n이유: 혼자 '남겨지는' 수동\n나머지 ▶ ① 부사 ✔ ③ be left + -ing ✔")]
SCR = [1, 2, 3, 4, 5]
ORDER = [[0, 1, 2, 3], [3, 4, 5]]
INSERT = [([0, 1, 2], 1, "정답 ▶ ① (But goldenrods ~ 문장)\n이유: 평화로운 지역(친족만 이해) → But 적대적 지역(모두가 이해) → Instead of 암호 속삭임, 확성기로"),
 ([3, 4, 5], 1, "정답 ▶ ① (When times are ~ 문장)\n이유: 보내는 쪽에도 이로움 → 그 이유: 힘든 시기엔 혼자 남고 싶지 않음 → 짝도, 매개자 불러올 상대도 없으니까")]
ODD = [([1, 2, "Goldenrods are famous for their bright yellow flowers in autumn.", 3], 2, "정답 ▶ ③\n이유: 적대적 환경에서 화학 신호를 널리 보내는 이유를 설명하는 흐름이에요. 가을의 노란 꽃 이야기는 관계없어요.")]
BLANK = [BL(p, 'Researchers recently', 'close kin', ["natural enemies", "human visitors", "all insects"], "정답 ▶ close kin (가까운 친족)\n이유: 매우 특정한 신호 → 가까운 '친족'만 이해\n오답 ▶ 천적 · 사람 방문객 · 모든 곤충"),
 BL(p, 'Instead of using', 'loudspeaker', ["telephone", "letter", "secret code"], "정답 ▶ loudspeaker (확성기)\n이유: 모두가 이해하도록 '널리' 알림 → 확성기 비유\n오답 ▶ telephone 전화 · letter 편지 · secret code 비밀 암호(반대)"),
 BL(p, 'There will be', 'pollinators', ["predators", "farmers", "diseases"], "정답 ▶ pollinators (꽃가루 매개자)\n이유: 번식을 돕는 존재 — 이웃이 함께 있어야 불러들일 수 있음\n오답 ▶ predators 포식자 · farmers 농부 · diseases 질병")]
GRAM = [{'q': "빈칸에 알맞은 것은?<br><b>They issue alarm calls on the rare occasion they ______.</b>", 'opts': ["are attacked", "attack", "attacking", "attacked"], 'ex': "정답 ▶ are attacked\n이유: 미역취가 공격'받는' 수동"},
 {'q': "빈칸에 알맞은 것은?<br><b>They use chemical phrases easily ______ by all the goldenrod.</b>", 'opts': ["understood", "understanding", "understand", "to understand"], 'ex': "정답 ▶ understood\n이유: 표현이 이해'되는' 수동 → 과거분사"},
 {'q': "빈칸에 알맞은 것은?<br><b>The communications are beneficial not only to the receiver ______ to the sender.</b>", 'opts': ["but also", "and also", "or also", "as well"], 'ex': "정답 ▶ but also\n이유: not only A but also B"},
 {'q': "빈칸에 알맞은 것은?<br><b>There will be no one ______ with.</b>", 'opts': ["to mate", "mate", "mating", "mated"], 'ex': "정답 ▶ to mate\n이유: no one을 꾸미는 to부정사 (mate with의 with는 그대로)"}]
SUMQ = []
