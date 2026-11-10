from jfw import *
p = load(23, '23번 · 글의 주제')
VOCAB = words(23)
EXAM = [EXQ(23, '23. 다음 글의 주제로 가장 적절한 것은?', p.full(), [
 "difficulties in protecting whistleblowers’ rights", "importance of punishment for unlawful corporate activities", "causes of individuals’ hesitation to become a whistleblower",
 "effects of raising public awareness on reducing corporate corruption", "need of whistleblower protection to guard their actions and the public good"], 4,
 "정답 ▶ ⑤ 내부 고발자의 행위와 공익을 지키기 위한 내부 고발자 보호의 필요성\n이유: 기업 위법 행위는 용기 있는 제보자 덕분에 드러남 → 내부 고발자 보호가 주목받음 → 신고를 두려워하면 기업·제삼자·경제·법치까지 피해 → 보호는 '개인의 행위'와 '공익'을 모두 지키는 두 기능\n오답 ▶ ① 보호의 '어려움'이 아니라 '필요성' ② 처벌의 중요성 ✗ ③ 망설이는 이유(보복 두려움)는 일부 언급일 뿐 ④ 대중 인식 제고 이야기 없음\n포인트 ▶ guard = protect · the public good = 공익", v=False),
 EXQ(23, '다음 글의 제목으로 가장 적절한 것은?', p.full(), [
 "Protecting Whistleblowers Protects Us All", "Why Companies Should Hide Their Mistakes", "Brave Informants Always Win in Court",
 "The Rule of Law: An Outdated Idea", "How to Punish Corporate Criminals Faster"], 0,
 "정답 ▶ ① 내부 고발자를 보호하는 것은 우리 모두를 보호하는 것이다\n이유: 보호는 개인의 행위뿐 아니라 공익(the public good)도 지킨다 — 기업·제삼자·경제·대중·법치 모두와 연결\n오답 ▶ ② 반대 ③ 재판 이야기 없음 ④ 법치는 지켜야 할 것 ⑤ 처벌 속도 ✗"),
 EXQ(23, '다음 빈칸에 들어갈 말로 가장 적절한 것은?', p.blank('for fear of reprisals or consequences'), [
 "for fear of reprisals or consequences", "for the sake of higher salaries", "in order to protect the public good", "because they lack legal knowledge", "since the company rewards them"], 0,
 "정답 ▶ ① 보복이나 불이익을 두려워하여\n이유: 직원들이 위법 행위를 신고하기를 '두려워하는(fear to report)' 이유 → 보복·불이익 두려움. 그래서 보호 제도가 필요\n오답 ▶ ② 월급 ③ 공익 보호는 신고하는 이유지 '안 하는' 이유가 아님 ④ 법 지식 부족 언급 없음 ⑤ 보상하면 신고를 두려워할 이유가 없음\n포인트 ▶ for fear of ~ = ~을 두려워하여")]
PICK1 = [PK(p, 'In recent years', 'illegal', 'legal', "정답 ▶ illegal (불법의)\n오답 ▶ legal (합법적인)\n이유: 뒤에서 misconduct(위법 행위), violations of law로 이어져요."),
 PK(p, 'Such misconduct', 'exposed', 'hidden', "정답 ▶ exposed (드러난)\n오답 ▶ hidden (숨겨진)\n이유: 용기 있는 제보자들이 위험을 무릅써서 위법 행위가 '드러났다'"),
 PK(p, 'Such misconduct', 'brave', 'careless', "정답 ▶ brave (용기 있는)\n오답 ▶ careless (부주의한)\n이유: 많은 위험을 무릅쓴(risked a great deal) 사람들 → 용기 있는"),
 PK(p, 'If violations', 'undetected', 'reported', "정답 ▶ undetected (적발되지 않은)\n오답 ▶ reported (신고된)\n이유: 직원들이 신고를 두려워하니 위반이 여러 해 동안 '적발되지 않고' 처벌도 안 됨"),
 PK(p, 'If violations', 'negative', 'positive', "정답 ▶ negative (부정적인)\n오답 ▶ positive (긍정적인)\n이유: 다음 문장에서 기업·경제·대중에 해를 끼친다(harm)고 함"),
 PK(p, 'A well-balanced', 'positive', 'harmful', "정답 ▶ positive (긍정적인)\n오답 ▶ harmful (해로운)\n이유: 균형 잡힌 보호는 개인의 행위와 공익 모두에 '좋은' 영향")]
TF = [TF(p, "The number of revealed corporate illegal cases has increased in recent years.", True, "the number of cases that came to light, increased", "정답 ▶ T\n이유: 적어도 세상에 드러난 사건 수는 늘었어요.\n어휘 ▶ come to light = be revealed"),
 TF(p, "Misconduct is usually exposed by the companies themselves.", False, "only been exposed because brave informants have risked a great deal", "정답 ▶ F\n이유: 용기 있는 제보자들 덕분에 드러났어요."),
 TF(p, "Employees may not report illegal activities because they fear reprisals.", True, "fear to report illegal activities for fear of reprisals", "정답 ▶ T\n이유: 보복이나 불이익을 두려워해 신고를 꺼려요."),
 TF(p, "Unreported violations harm only the company itself.", False, "but also third-parties, the economy in general, the general public", "정답 ▶ F\n이유: 기업뿐 아니라 제삼자, 경제, 대중, 법치까지 영향을 받아요."),
 TF(p, "Protecting whistleblowers has two main functions.", True, "has two main functions", "정답 ▶ T\n이유: 개인의 행위 보호와 공익 보호, 두 가지 기능이 있어요."),
 TF(p, "The writer says whistleblower protection is good only for the individual.", False, "Protecting the individual’s actions as well as protecting the public good", "정답 ▶ F\n이유: 개인의 행위뿐 아니라 공익도 보호해요.")]
MC = [MC(p, "글의 내용과 일치하지 <u>않는</u> 것은?", [
 "Undetected violations have no effect on the general public.", "Informants took great risks to stop misconduct.", "Whistleblower protection has recently drawn attention.",
 "Fear of consequences can keep employees silent.", "Protecting whistleblowers can benefit the public good."],
 "정답 ▶ Undetected violations have no effect on the general public.\n이유: the general public, and even the rule of law could be affected\n포인트 ▶ take great risks = risk a great deal · draw attention = come into focus · keep silent ≒ fear to report",
 [["적발되지 않은 위반은 대중에게 영향이 없다.", "the general public, and even the rule of law could be affected", "✗ 영향 있음"], ["제보자들은 위법 행위를 멈추려고 큰 위험을 감수했다.", "brave informants have risked a great deal in order to put an end to it", "take risks = risk"], ["내부 고발자 보호가 최근 주목받았다.", "whistleblower protection has come into focus", "draw attention = come into focus"], ["불이익에 대한 두려움은 직원들을 침묵하게 할 수 있다.", "fear to report illegal activities for fear of reprisals or consequences", "일치"], ["내부 고발자 보호는 공익에 이로울 수 있다.", "protecting the public good", "일치"]]),
 MC(p, "글의 내용과 <u>일치하는</u> 것은?", ["위법 행위가 오래 적발되지 않으면 법치주의에도 영향을 줄 수 있다.", "기업 위법 행위의 수는 최근 줄어들었다.", "위법 행위는 주로 정부 조사로 드러났다.", "직원들은 대개 위법 행위를 기꺼이 신고한다.", "내부 고발자 보호는 공익과 관계없다."],
 "정답 ▶ 위법 행위가 오래 적발되지 않으면 법치주의에도 영향을 줄 수 있다.\n이유: even the rule of law could be affected\n오답 ▶ ② 증가 ③ 용기 있는 제보자 덕분 ④ 두려워서 꺼림 ⑤ 공익도 보호",
 [["", "even the rule of law could be affected", "일치 ✔"], ["", "has grown", "증가"], ["", "brave informants", "제보자"], ["", "fear to report", "두려워함"], ["", "protecting the public good", "공익"]])]
PICK2 = [PK(p, 'In recent years', 'has grown', 'have grown', "정답 ▶ has\n이유: the number of + 복수명사 → 주어는 the number(단수) → has"),
 PK(p, 'In recent years', 'cases that came', 'cases what came', "정답 ▶ that\n이유: 선행사 cases + 주어가 빠진 절 → 주격 관계대명사 that. what은 선행사를 포함하므로 선행사 뒤에 못 와요."),
 PK(p, 'Such misconduct', 'been exposed', 'exposed', "정답 ▶ been exposed\n이유: 위법 행위가 '드러나게 된' 수동 → has been exposed"),
 PK(p, 'Such misconduct', 'to put an end', 'to putting an end', "정답 ▶ to put\n이유: in order to + 동사원형 (~하기 위해)"),
 PK(p, 'If violations', 'go undetected', 'goes undetected', "정답 ▶ go\n이유: 주어 violations(복수). of law and order는 수식어"),
 PK(p, 'It can harm', 'be affected', 'affect', "정답 ▶ be affected\n이유: 법치가 '영향을 받는' 수동 → could be affected"),
 PK(p, 'Protecting those', 'has two', 'have two', "정답 ▶ has\n이유: 동명사구 주어(Protecting those ~ behaviour)는 단수")]
VERB = [VB(p, 'Such misconduct', 'risked', 'risk', "정답 ▶ risked\n이유: have + p.p. 현재완료"),
 VB(p, 'If violations', 'to report', 'report', "정답 ▶ to report (reporting도 정답)\n이유: fear + to부정사/동명사 (~하기를 두려워하다)", alt=('reporting',)),
 VB(p, 'Protecting those', 'reducing', 'reduce', "정답 ▶ reducing\n이유: 전치사 in 뒤 동명사 (assist in -ing)"),
 VB(p, 'Hence, it', 'come', 'come', "x")]
VERB = [v for v in VERB if v['v'] != v['a'][0]]
ERR = [ER(p, 'In recent years', [('has', 'have'), 'that', 'increased'], 0, 'has', "틀린 곳 ▶ ① have → has\n이유: the number of ~ = '~의 수'(단수)\n나머지 ▶ ② 주격 관계대명사 ✔ ③ the number ~ increased ✔"),
 ER(p, 'Protecting those', ['who', ('reducing', 'reduce'), 'has'], 1, 'reducing', "틀린 곳 ▶ ② reduce → reducing\n이유: 전치사 in 뒤 동명사\n나머지 ▶ ① 사람 선행사 those + who ✔ ③ 동명사 주어 단수 ✔"),
 ER(p, 'It can harm', [('itself', 'it'), 'also', 'be affected'], 0, 'itself', "틀린 곳 ▶ ① it → itself\n이유: '기업 그 자체' — 강조 용법 재귀대명사 the company itself\n나머지 ▶ ② not only ~ but also ✔ ③ 수동 ✔")]
SCR = [1, 2, 3, 5, 6]
ORDER = [[0, 1, 2, 3], [3, 4, 5, 6]]
INSERT = [([0, 1, 2, 3], 2, "정답 ▶ ② (Hence ~ 문장)\n이유: 위법 행위는 용기 있는 제보자 덕분에 드러남(원인) → Hence(따라서) 내부 고발자 보호가 주목받는 건 당연(결과)"),
 ([4, 5, 6], 2, "정답 ▶ ② (A well-balanced ~ 문장)\n이유: 두 기능(개인의 행위 보호·공익 보호) → both of these(이 둘 모두)가 바로 앞의 두 기능을 가리켜요.")]
ODD = [([2, 3, "Many companies now offer higher salaries to attract talented employees.", 4], 2, "정답 ▶ ③\n이유: 신고를 두려워해 위반이 적발되지 않으면 생기는 피해 이야기예요. 인재 유치를 위한 높은 월급은 관계없어요.")]
BLANK = [BL(p, 'Such misconduct', 'brave', ["lazy", "foolish", "wealthy"], "정답 ▶ brave (용기 있는)\n이유: 큰 위험을 무릅쓰고 위법 행위를 끝내려 한 사람들\n오답 ▶ lazy 게으른 · foolish 어리석은 · wealthy 부유한"),
 BL(p, 'Hence, it', 'no surprise', ["a mistake", "a secret", "a burden"], "정답 ▶ no surprise (놀랍지 않은 일)\n이유: Hence(따라서) — 앞의 원인에서 자연스럽게 나오는 결과\n오답 ▶ a mistake 실수 · a secret 비밀 · a burden 부담"),
 BL(p, 'Protecting those', 'public good', ["company profit", "private life", "market price"], "정답 ▶ public good (공익)\n이유: 앞에서 제삼자·경제·대중·법치 모두 피해를 본다고 했으니, 보호는 '모두의 이익'도 지켜요.\n오답 ▶ company profit 회사 이익 · private life 사생활 · market price 시장 가격")]
GRAM = [{'q': "빈칸에 알맞은 것은?<br><b>The number of illegal actions ______ grown in recent years.</b>", 'opts': ["has", "have", "having", "to have"], 'ex': "정답 ▶ has\n이유: the number of + 복수명사 = '~의 수' → 단수\n포인트 ▶ a number of + 복수명사 = 많은 ~ → 복수"},
 {'q': "빈칸에 알맞은 것은?<br><b>Employees fear ______ illegal activities.</b>", 'opts': ["to report", "report", "reported", "reports"], 'ex': "정답 ▶ to report\n이유: fear + to부정사/동명사 모두 가능, 보기 중 to report"},
 {'q': "빈칸에 알맞은 것은?<br><b>Even the rule of law could ______.</b>", 'opts': ["be affected", "affect", "affecting", "be affecting"], 'ex': "정답 ▶ be affected\n이유: 법치가 '영향을 받는' 수동 → 조동사 + be p.p."},
 {'q': "빈칸에 알맞은 것은?<br><b>______ those who report crimes has two main functions.</b>", 'opts': ["Protecting", "Protect", "Protected", "Protects"], 'ex': "정답 ▶ Protecting\n이유: 주어 자리 → 동명사, 단수 동사 has"}]
SUMQ = [SUM(p, "Because employees may stay silent out of (A) ______ of reprisals, protecting whistleblowers is needed to guard both individuals and the public (B) ______.", [
 "(A) fear – (B) good", "(A) fear – (B) image", "(A) hope – (B) good", "(A) lack – (B) opinion", "(A) memory – (B) debt"],
 "정답 ▶ (A) fear – (B) good\n(A) 보복을 '두려워하여'(for fear of reprisals) 침묵 → fear\n(B) 개인의 행위와 '공익'(the public good)을 보호 → good\n오답 ▶ hope 희망 · lack 부족 · memory 기억 / image 이미지 · opinion 여론 · debt 빚",
 ["for fear of reprisals", "protecting the public good"])]
