from jfw import *
S = PREP['35']['sents'][:]; assert S[3].startswith('A human’s average'); S = S[:3] + S[4:]
p = load(35, '35번 · 무관한 문장', sents=S)
VOCAB = words(35)
f = ' '.join(Q['35']['foot'])
ORIG = box(raw(35) + '<br><small>' + f + '</small>')
EXAM = [EXQ(35, '35. 다음 글에서 전체 흐름과 관계 없는 문장은?', ORIG, ["①", "②", "③", "④", "⑤"], 2,
 "정답 ▶ ③ (A human’s average life expectancy has increased, but relying too much on medicine damages our body system.)\n이유: 글 전체 = 과학적 발전이 전염병 치료·예방에 가져온 진보(페니실린, 천연두 백신, 실험실 백신, 위생 관리·치료법) → ③은 약에 과하게 의존하면 몸이 상한다는 '부작용' 이야기라 흐름에서 벗어남\n오답 ▶ ① 페니실린 ② 우두 → 천연두 예방 ④ 백신 → 질병 부담 감소 ⑤ 위생 관리·치료법 — 모두 '진보'의 사례\n포인트 ▶ 첫 문장(주제문)의 방향(긍정적 진보)과 반대 방향인 문장 찾기", v=False),
 EXQ(35, '다음 글의 주제로 가장 적절한 것은?', p.full(), [
 "medical progress in treating and preventing infectious diseases", "the side effects of relying too much on medicine", "why vaccines are hard to develop",
 "the life of Alexander Fleming", "the dangers of smallpox in the 18th century"], 0,
 "정답 ▶ ① 전염병 치료와 예방에서의 의학적 진보\n이유: 첫 문장(주제문) + 페니실린·천연두·백신·위생 관리 사례\n오답 ▶ ② 무관한 문장(③)의 내용 ③ 개발이 어렵다는 말 없음 ④ 사례 하나일 뿐 ⑤ 천연두도 사례 하나\n포인트 ▶ 사례가 여러 개 나열되면 그것을 묶는 첫 문장이 주제"),
 EXQ(35, '다음 빈칸에 들어갈 말로 가장 적절한 것은?', p.blank('harmless'), [
 "harmless", "deadly", "unknown", "contagious", "permanent"], 0,
 "정답 ▶ ① harmless (무해한)\n이유: 인간에게 '무해한' 우두에 노출되면 → '치명적인' 천연두로부터 보호됨 — 대비\n오답 ▶ ② 치명적인: 천연두 쪽 ③ 알려지지 않은 ④ 전염성의 ⑤ 영구적인 — 백신 원리와 맞지 않음\n포인트 ▶ deadly smallpox ↔ harmless cowpox")]
PICK1 = [PK(p, 'Scientific developments', 'enormous', 'little', "정답 ▶ enormous (엄청난)\n오답 ▶ little (거의 없는)\n이유: 뒤 사례들(페니실린, 백신 ~)이 모두 큰 성과 → '엄청난' 진보"),
 PK(p, 'Scientific developments', 'prevention', 'spread', "정답 ▶ prevention (예방)\n오답 ▶ spread (확산)\n이유: 치료와 '예방'에서의 진보 — 백신은 예방의 예"),
 PK(p, 'The discovery of penicillin', 'breakthroughs', 'failures', "정답 ▶ breakthroughs (획기적 발전)\n오답 ▶ failures (실패)\n이유: 노벨상을 받은 발견 → 가장 큰 '획기적 발전' 중 하나"),
 PK(p, 'Edward Jenner', 'protected', 'infected', "정답 ▶ protected (보호된)\n오답 ▶ infected (감염된)\n이유: 우두에 노출된 후 천연두로부터 '보호됨' — 백신의 원리"),
 PK(p, 'Vaccines developed', 'reduction', 'increase', "정답 ▶ reduction (감소)\n오답 ▶ increase (증가)\n이유: 백신은 질병 부담의 '감소'에 기여, 퇴치까지"),
 PK(p, 'For other infectious', 'manageable', 'incurable', "정답 ▶ manageable (관리 가능한)\n오답 ▶ incurable (치료할 수 없는)\n이유: 치명적이던 병을 만성적이지만 '관리 가능한' 병으로 바꿈")]
TF = [TF(p, "Alexander Fleming discovered penicillin in 1928.", True, "The discovery of penicillin in 1928 by Alexander Fleming", "정답 ▶ T\n이유: 1928년 Fleming이 페니실린을 발견했어요."),
 TF(p, "Fleming never received any award for his discovery.", False, "for which he later received the Nobel Prize", "정답 ▶ F\n이유: 후에 노벨상을 받았어요."),
 TF(p, "Jenner found that exposure to cowpox protected people against smallpox.", True, "humans were protected against the deadly smallpox virus after exposure to the cowpox virus", "정답 ▶ T\n이유: 우두에 노출된 후 천연두로부터 보호됐어요."),
 TF(p, "The cowpox virus is deadly to humans.", False, "which is harmless to humans", "정답 ▶ F\n이유: 우두는 인간에게 무해해요. 치명적인 건 천연두(smallpox)예요."),
 TF(p, "Vaccines have even helped eliminate poxvirus.", True, "have even led to the elimination of poxvirus", "정답 ▶ T\n이유: 수두 바이러스 퇴치로까지 이어졌어요."),
 TF(p, "Hygiene measures have increased the burden of cholera and malaria.", False, "control and hygiene management measures have reduced their burden", "정답 ▶ F\n이유: 위생 관리 조치가 부담을 '줄였어요'.")]
MC = [MC(p, "글의 내용과 일치하지 <u>않는</u> 것은?", [
 "All deadly viral diseases have been completely cured.", "Penicillin was a major breakthrough against infectious diseases.", "Jenner made his discovery around 1796.",
 "Vaccines are developed in laboratories.", "Some deadly viral diseases became chronic but manageable."],
 "정답 ▶ All deadly viral diseases have been completely cured.\n이유: treatment therapies turned viral diseases that were deadly into chronic manageable diseases (완치가 아니라 '만성적·관리 가능')\n포인트 ▶ chronic = 만성적인 · manageable = 관리 가능한",
 [["모든 치명적 바이러스 질병이 완전히 치료되었다.", "into chronic manageable diseases", "✗ 만성·관리"], ["페니실린은 전염병에 맞선 큰 획기적 발전이었다.", "one of the biggest breakthroughs", "일치"], ["Jenner는 1796년경에 발견을 했다.", "around 1796", "일치"], ["백신은 실험실에서 개발된다.", "Vaccines developed in laboratories", "일치"], ["일부 치명적 바이러스 질병은 만성적이지만 관리 가능해졌다.", "chronic manageable diseases", "일치"]]),
 MC(p, "글의 내용과 <u>일치하는</u> 것은?", ["콜레라와 말라리아의 부담은 위생 관리로 줄었다.", "페니실린은 1796년에 발견되었다.", "우두는 인간에게 치명적이다.", "백신은 세균성 질병에만 효과가 있다.", "과학 기술은 전염병 예방에 거의 기여하지 못했다."],
 "정답 ▶ 콜레라와 말라리아의 부담은 위생 관리로 줄었다.\n이유: For other infectious diseases (for example cholera and malaria), control and hygiene management measures have reduced their burden\n오답 ▶ ② 1928년 ③ 무해 ④ 세균성·바이러스성 모두 ⑤ 엄청난 진보",
 [["", "hygiene management measures have reduced their burden", "일치 ✔"], ["", "penicillin in 1928", "1928"], ["", "harmless to humans", "무해"], ["", "bacterial and viral diseases", "둘 다"], ["", "enormous progress", "엄청남"]])]
PICK2 = [PK(p, 'Scientific developments', 'have brought', 'has brought', "정답 ▶ have brought\n이유: 주어 Scientific developments and technologies(복수)"),
 PK(p, 'The discovery of penicillin', 'for which', 'which', "정답 ▶ for which\n이유: receive the Nobel Prize for the discovery → 전치사 for + which (뒤가 완전한 절)"),
 PK(p, 'The discovery of penicillin', 'was one', 'were one', "정답 ▶ was\n이유: 주어 The discovery(단수) — of penicillin ~ Fleming, 삽입절은 수식어"),
 PK(p, 'Edward Jenner', 'were protected', 'protected', "정답 ▶ were protected\n이유: 사람들이 '보호받은' 수동"),
 PK(p, 'Vaccines developed', 'developed', 'developing', "정답 ▶ developed\n이유: Vaccines를 꾸미는 과거분사 — 실험실에서 '개발된' 백신 (동사는 have contributed)"),
 PK(p, 'For other infectious', 'that were', 'what were', "정답 ▶ that\n이유: 선행사 viral diseases 있음 → 주격 관계대명사 that")]
VERB = [VB(p, 'The discovery of penicillin', 'received', 'receive', "정답 ▶ received\n이유: 과거(later) 사실 → 과거시제"),
 VB(p, 'Vaccines developed', 'contributed', 'contribute', "정답 ▶ contributed\n이유: have + p.p. 현재완료 (have contributed)"),
 VB(p, 'Vaccines developed', 'led', 'lead', "정답 ▶ led\n이유: have even led — 현재완료, lead-led-led"),
 VB(p, 'For other infectious', 'turned', 'turn', "정답 ▶ turned\n이유: 과거에 바꾼 일 → 과거시제 (turn A into B)")]
VERB = [v for v in VERB if v['v'] != v['a'][0]]
ERR = [ER(p, 'The discovery of penicillin', [('for which', 'which'), 'later', ('was', 'was')], 0, 'for which', "틀린 곳 ▶ ① which → for which\n이유: he later received the Nobel Prize for it — 뒤가 완전한 절이라 전치사 + 관계대명사\n나머지 ▶ ② 부사 later ✔ ③ 주어 The discovery(단수) → was ✔"),
 ER(p, 'Edward Jenner', [('were protected', 'protected'), 'exposure', 'which'], 0, 'were protected', "틀린 곳 ▶ ① protected → were protected\n이유: humans가 천연두로부터 '보호받는' 수동 (protected 뒤 목적어 없음)\n나머지 ▶ ② 명사 exposure ✔ ③ 계속적 용법 which(사물) ✔"),
 ER(p, 'Vaccines developed', [('developed', 'developing'), 'have contributed', 'have even led'], 0, 'developed', "틀린 곳 ▶ ① developing → developed\n이유: 백신이 실험실에서 '개발된' 수동 → 과거분사\n나머지 ▶ ② 주어 Vaccines(복수) → have ✔ ③ 현재완료 병렬 ✔")]
SCR = [0, 1, 2, 3, 4]
ORDER = [[0, 1, 2, 3], [1, 2, 3, 4]]
INSERT = [([0, 1, 2, 3], 1, "정답 ▶ ① (The discovery of penicillin ~ 문장)\n이유: 주제문(엄청난 진보) → 첫 사례 페니실린 → Jenner → 백신"),
 ([2, 3, 4], 2, "정답 ▶ ② (For other infectious diseases ~ 문장)\n이유: 백신이 세균성·바이러스성 질병 부담을 줄임 → '다른' 전염병(For other ~)은 위생 관리·치료법으로")]
ODD = [([1, 2, "Relying too much on medicine, however, can damage our body system.", 3], 2, "정답 ▶ ③\n이유: 의학 발전이 전염병 치료·예방에 가져온 '진보'의 사례가 이어지는 흐름이에요. 약 과다 의존의 부작용은 관계없어요(원문항 ③번과 같은 함정).")]
BLANK = [BL(p, 'Scientific developments', 'infectious', ["genetic", "mental", "rare"], "정답 ▶ infectious (전염성의)\n이유: 페니실린·백신·콜레라·말라리아 → 모두 '전염병'\n오답 ▶ genetic 유전적인 · mental 정신의 · rare 드문"),
 BL(p, 'Vaccines developed', 'elimination', ["discovery", "spread", "return"], "정답 ▶ elimination (퇴치)\n이유: 질병 부담을 줄이고 '심지어(even)' 바이러스를 '퇴치'\n오답 ▶ discovery 발견 · spread 확산(반대) · return 재발"),
 BL(p, 'For other infectious', 'chronic', ["deadly", "sudden", "unknown"], "정답 ▶ chronic (만성적인)\n이유: 치명적이던 병 → '만성적인' 관리 가능한 병으로 (죽지는 않고 오래 관리)\n오답 ▶ deadly 치명적인(바뀌기 전) · sudden 갑작스러운 · unknown")]
GRAM = [{'q': "빈칸에 알맞은 것은?<br><b>The discovery, ______ he received the Nobel Prize, changed medicine.</b>", 'opts': ["for which", "which", "that", "what"], 'ex': "정답 ▶ for which\n이유: receive A for B — 뒤가 완전한 절이므로 전치사 + 관계대명사"},
 {'q': "빈칸에 알맞은 것은?<br><b>Vaccines ______ in laboratories have reduced disease.</b>", 'opts': ["developed", "developing", "develop", "were developed"], 'ex': "정답 ▶ developed\n이유: 명사를 꾸미는 과거분사(수동), 동사는 have reduced"},
 {'q': "빈칸에 알맞은 것은?<br><b>Therapies turned deadly diseases ______ manageable ones.</b>", 'opts': ["into", "from", "with", "at"], 'ex': "정답 ▶ into\n이유: turn A into B (A를 B로 바꾸다)"},
 {'q': "빈칸에 알맞은 것은?<br><b>Humans were protected ______ smallpox after exposure to cowpox.</b>", 'opts': ["against", "into", "of", "toward"], 'ex': "정답 ▶ against\n이유: protect A against B / be protected against ~ (~으로부터 보호되다)"}]
SUMQ = [SUM(p, "Scientific advances such as antibiotics, vaccines, and hygiene measures have greatly (A) ______ the burden of infectious diseases, sometimes even (B) ______ them.", [
 "(A) reduced – (B) eliminating", "(A) reduced – (B) spreading", "(A) increased – (B) eliminating", "(A) ignored – (B) creating", "(A) hidden – (B) studying"],
 "정답 ▶ (A) reduced – (B) eliminating\n(A) the reduction of the burden / have reduced their burden (B) led to the elimination of poxvirus\n오답 ▶ increased 증가시켰다 · spreading 퍼뜨리는 — 반대",
 ["the reduction of the burden", "the elimination of poxvirus"])]
