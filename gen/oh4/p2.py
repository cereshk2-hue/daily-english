from common import *
c = SEC['❸']
VOCAB = V('❸', [["right-to-repair movement", "수리할 권리 운동"], ["empower", "~에게 권한을 주다", "Empowering"], ["dispose of", "~을 버리다, 처분하다"], ["disassemble", "~을 분해하다 (↔ assemble)"],
  ["manufacturer", "제조사, 제조업자"], ["official", "공식적인"], ["service center", "수리소, 서비스 센터"], ["third-party", "제삼자의"], ["what is more", "게다가, 더욱이"],
  ["intentionally", "의도적으로, 고의로 (= deliberately)"], ["acquire", "~을 얻다, 획득하다 (= obtain)"], ["instructions", "설명(서), 사용법"], ["promote", "~을 촉진하다, 장려하다", "promoting"],
  ["legislation", "법률, 법률 제정"], ["state", "~을 명시하다, 진술하다", "states"], ["technician", "기술자"], ["of one's choice", "자신이 선택한", "of your choice"], ["demand", "~을 요구하다", "demands"],
  ["available", "이용할 수 있는"], ["obtain", "~을 얻다"], ["practice", "관행, 관례"], ["prevent A from -ing", "A가 ~하는 것을 막다", "preventing consumers from installing"],
  ["install", "~을 설치하다", "installing"], ["custom", "맞춤형의, 주문 제작한"], ["prohibit", "~을 금지하다 (= ban, forbid)", "prohibited"], ["advocate", "지지자, 옹호자", "Advocates"],
  ["accomplish", "~을 이루다, 성취하다", "accomplished"], ["far less", "훨씬 더 적은"], ["influence", "영향(력)"], ["join the cause", "대의에 동참하다", "joining the cause"]])
PICK1 = [PK(c, 'One reason many', 'dispose of', 'hold on to', "정답 ▶ dispose of (~을 버리다)\n오답 ▶ hold on to (~을 계속 가지고 있다)\n이유: 수리하기 너무 어려워서 고장 난 기기를 '버린다'"),
 PK(c, 'For example, a device', 'disassemble', 'assemble', "정답 ▶ disassemble (분해하다)\n오답 ▶ assemble (조립하다)\n이유: 수리가 어려운 예 → '분해하기' 어렵다"),
 PK(c, 'For example, a device', 'official', 'independent', "정답 ▶ official (공식적인)\n오답 ▶ independent (독립적인)\n이유: 제조사가 '공식' 수리소로 가져오라고 요구 → 다음 문장 '제삼자 수리점은 허용 안 함'과 연결"),
 PK(c, 'What is more', 'intentionally', 'accidentally', "정답 ▶ intentionally (의도적으로)\n오답 ▶ accidentally (우연히)\n이유: 수리하기 어렵게 '설계된(designed)' → 의도적으로"),
 PK(c, 'It is common for', 'unable', 'able', "정답 ▶ unable (~할 수 없는)\n오답 ▶ able (~할 수 있는)\n이유: 수리가 어려운 이유들을 나열하는 중 → 설명서나 부품을 '얻지 못하는' 것이 흔함"),
 PK(c, 'Second, third parties', 'obtain', 'reject', "정답 ▶ obtain (얻다)\n오답 ▶ reject (거절하다)\n이유: 운동의 요구 — 제삼자도 수리에 필요한 부품과 도구를 '얻을' 수 있어야 함"),
 PK(c, 'Third, the practice', 'prohibited', 'encouraged', "정답 ▶ prohibited (금지된)\n오답 ▶ encouraged (장려된)\n이유: 소비자가 소프트웨어를 설치하지 '못하게 막는' 관행 → 법으로 '금지되어야'"),
 PK(c, 'Finally, it demands', 'easy', 'complex', "정답 ▶ easy (쉬운)\n오답 ▶ complex (복잡한)\n이유: 소비자 권리를 위한 요구 → 수리를 최대한 '쉽게' 만드는 설계"),
 PK(c, 'Advocates of the', 'less', 'more', "정답 ▶ less (더 적은)\n오답 ▶ more (더 많은)\n이유: 수리가 쉬워지면 버려지는 기기가 줄어 전자 쓰레기가 '훨씬 적게' 발생"),
 PK(c, 'This movement is', 'growing', 'declining', "정답 ▶ growing (커지는)\n오답 ▶ declining (줄어드는)\n이유: with more and more countries joining(점점 더 많은 나라가 동참) → 영향력이 '커지고' 있음")]
TF = [TF(c, "Repair difficulty is one reason people throw away broken devices.", True, "One reason many people dispose of their damaged devices is that they are too difficult to repair", "정답 ▶ T\n이유: 수리하기 너무 어려운 것이 버리는 한 가지 이유예요.\n어휘 ▶ throw away = dispose of"),
 TF(c, "Most companies encourage customers to use third-party repair shops.", False, "Many companies do not allow their customers to take their damaged items to third-party repair shops", "정답 ▶ F\n이유: 많은 회사가 제삼자 수리점 이용을 허용하지 않아요."),
 TF(c, "Some products are deliberately made hard to repair.", True, "intentionally designed to be difficult to repair", "정답 ▶ T\n이유: 일부 제품은 의도적으로 수리하기 어렵게 설계돼요.\n어휘 ▶ deliberately = intentionally"),
 TF(c, "The movement believes owners should be able to choose who repairs their products.", True, "bring it to a technician of your choice", "정답 ▶ T\n이유: 직접 고치거나 자신이 선택한 기술자에게 가져갈 권리가 있다고 해요."),
 TF(c, "The movement makes three demands.", False, "demands four things", "정답 ▶ F\n이유: 네 가지를 요구해요."),
 TF(c, "The movement wants product information to be shared only with official service centers.", False, "make information about their products available to everyone", "정답 ▶ F\n이유: 모든 사람이 정보를 이용할 수 있게 하라고 요구해요."),
 TF(c, "Over 40 U.S. states have started working on right-to-repair laws.", True, "more than 40 states in the U.S. have begun working on right-to-repair legislation", "정답 ▶ T\n이유: 미국 40개 이상의 주가 관련 법률 제정에 착수했어요."),
 TF(c, "The movement has had no impact outside the United States.", False, "gaining a growing influence in Europe as well", "정답 ▶ F\n이유: 유럽에서도 영향력이 커지고 있어요.")]
MC = [MC(c, "본문 ❸의 내용과 일치하지 <u>않는</u> 것은?", [
 "The movement calls for manufacturers to keep repair manuals confidential.", "Manufacturers may insist that devices be repaired at authorized centers.", "Consumers often cannot get the components necessary for repairs.",
 "Supporters claim e-waste would drop sharply if the goals were met.", "A growing number of European nations are backing the movement."],
 "정답 ▶ The movement calls for manufacturers to keep repair manuals confidential.\n이유: companies must make information about their products available to everyone — 정보를 '비밀로' 하는 게 아니라 '모두에게 공개'\n포인트 ▶ call for = demand · confidential = 기밀의 · insist = require · authorized = official · components = parts · supporters = advocates · drop sharply ≒ far less · back = 지지하다",
 [["운동은 제조사가 수리 설명서를 기밀로 유지하라고 요구한다.", "make information about their products available to everyone", "✗ 공개 요구"], ["제조사는 공인 센터에서 수리받으라고 요구할 수 있다.", "its manufacturer may require that it be brought to an official service center", "insist ≒ require ✔"],
  ["소비자는 흔히 수리에 필요한 부품을 구하지 못한다.", "unable to acquire the instructions for how to fix their items or the parts", "components = parts ✔"], ["지지자들은 목표가 이뤄지면 전자 쓰레기가 크게 줄 거라 주장한다.", "far less e-waste will be generated", "supporters = advocates ✔"], ["점점 더 많은 유럽 국가가 운동을 지지한다.", "more and more countries joining the cause", "back ≒ join the cause ✔"]]),
 MC(c, "본문 ❸의 내용과 <u>일치하는</u> 것은?", ["The movement seeks to outlaw blocking users from installing custom software.", "The movement asks consumers to stop buying electronic devices.", "Only companies should be allowed to buy spare parts.", "The movement has already succeeded in every U.S. state.", "The movement wants repairs to remain difficult for safety reasons."],
 "정답 ▶ The movement seeks to outlaw blocking users from installing custom software.\n이유: the practice of preventing consumers from installing custom software ~ should be prohibited by law\n오답 ▶ ② 구매 중단 요구 없음 ③ 개인을 포함한 제삼자도 얻을 수 있어야 ④ 40개 이상 주에서 '착수'했을 뿐 ⑤ 최대한 쉽게\n포인트 ▶ outlaw = 법으로 금지하다 (= prohibit by law) · block A from -ing = prevent A from -ing",
 [["", "should be prohibited by law", "일치 ✔"], ["", "demands four things", "구매 중단 ✗"], ["", "third parties, including individuals", "개인도"], ["", "have begun working on", "착수"], ["", "as easy as possible", "쉽게"]])]
PICK2 = [PK(c, 'One reason many', 'is that', 'are that', "정답 ▶ is\n이유: 주어의 핵 One reason(단수). many people ~ devices는 reason을 꾸미는 관계절(that/why 생략)"),
 PK(c, 'For example, a device', 'be brought', 'is brought', "정답 ▶ be brought\n이유: 요구 동사 require + that + 주어 + (should) 동사원형 → (should) be brought"),
 PK(c, 'Many companies do', 'to take', 'take', "정답 ▶ to take\n이유: allow + 목적어 + to부정사"),
 PK(c, 'What is more', 'to be difficult', 'being difficult', "정답 ▶ to be\n이유: be designed + to부정사 (~하도록 설계되다)"),
 PK(c, 'It is common for', 'for consumers', 'of consumers', "정답 ▶ for\n이유: to부정사의 의미상 주어 → for + 목적격 (common은 사람의 성격 형용사가 아니므로 of 불가)"),
 PK(c, 'It is common for', 'needed', 'needing', "정답 ▶ needed\n이유: 부품이 수리에 '필요한' — the parts를 꾸미는 과거분사(수동)"),
 PK(c, 'The right-to-repair', 'promoting', 'promote', "정답 ▶ promoting\n이유: 전치사 by 뒤 동명사 (~함으로써)"),
 PK(c, 'Third, the practice', 'installing', 'install', "정답 ▶ installing\n이유: prevent A from -ing"),
 PK(c, 'Finally, it demands', 'makes repairs', 'make repairs', "정답 ▶ makes\n이유: 관계대명사 that의 선행사 a way(단수) → makes. (앞의 that절 design은 요구 동사 뒤 (should) 동사원형)"),
 PK(c, 'This movement is', 'joining', 'joined', "정답 ▶ joining\n이유: with + 목적어 + 분사 — 나라들이 '동참하는' 능동")]
VERB = [VB(c, 'Second, third parties', 'required', 'require', "정답 ▶ required\n이유: 부품과 도구가 수리에 '필요한' — 과거분사가 the parts and tools 수식"),
 VB(c, 'Third, the practice', 'prohibited', 'prohibit', "정답 ▶ prohibited\n이유: 관행이 '금지되어야' 하는 수동 → should be prohibited"),
 VB(c, 'Finally, it demands', 'design', 'design', "x"),
 VB(c, 'Advocates of the', 'accomplished', 'accomplish', "정답 ▶ accomplished\n이유: 목표가 '이루어지는' 수동 → are accomplished"),
 VB(c, 'Advocates of the', 'generated', 'generate', "정답 ▶ generated\n이유: 전자 쓰레기가 '발생되는' 수동 → will be generated"),
 VB(c, 'Thanks to their', 'working', 'work', "정답 ▶ working (to work도 정답)\n이유: begin + 동명사/to부정사", alt=('to work',))]
VERB = [v for v in VERB if v['v'] != v['a'][0]]
ERR = [ER(c, 'For example, a device', ['to disassemble', ('be', 'is'), 'to be fixed'], 1, 'be', "틀린 곳 ▶ ② is → be\n이유: require that + 주어 + (should) 동사원형\n나머지 ▶ ① 형용사 difficult 뒤 to부정사 ✔ ③ 기기가 '고쳐지기' 위해 → 수동 to부정사 ✔"),
 ER(c, 'It is common for', ['for', ('to be unable', 'being unable'), 'needed'], 1, 'to be unable', "틀린 곳 ▶ ② being unable → to be unable\n이유: 가주어 It ~ 진주어 to부정사 (for consumers는 의미상 주어)\n나머지 ▶ ① 의미상 주어 ✔ ③ 수동 과거분사 ✔"),
 ER(c, 'Finally, it demands', ['that', ('design', 'designs'), 'makes'], 1, 'design', "틀린 곳 ▶ ② designs → design\n이유: demand that + 주어 + (should) 동사원형\n나머지 ▶ ① 명사절 that ✔ ③ 선행사 a way(단수) → makes ✔"),
 ER(c, 'Advocates of the', ['say', 'are accomplished', ('far', 'very')], 2, 'far', "틀린 곳 ▶ ③ very → far\n이유: 비교급(less)을 강조할 때는 far / much / even / still / a lot. very는 비교급 강조 불가\n나머지 ▶ ① 주어 Advocates(복수) ✔ ② 조건절 현재시제 수동 ✔")]
SCR = [('❸', 0), ('❸', 2), ('❸', 3), ('❸', 6), ('❸', 7), ('❸', 9), ('❸', 11), ('❸', 13)]
ORDER = [[('❸', 0), ('❸', 1), ('❸', 2), ('❸', 3)], [('❸', 6), ('❸', 7), ('❸', 8), ('❸', 9), ('❸', 10)], [('❸', 11), ('❸', 12), ('❸', 13)]]
INSERT = [([('❸', 4), ('❸', 5), ('❸', 6), ('❸', 7)], 1, "정답 ▶ ① (The right-to-repair movement ~ 문장)\n이유: 수리를 어렵게 만드는 문제들 나열 → 수리할 권리 운동이 '이 문제들(these problems)'을 해결하려 함 → 그 운동의 네 가지 요구"),
 ([('❸', 9), ('❸', 10), ('❸', 11), ('❸', 12)], 2, "정답 ▶ ② (Advocates of the movement ~ 문장)\n이유: Third → Finally(네 가지 요구 끝) → 지지자들: 이 모든 목표(all these goals)가 이루어지면 → Thanks to their efforts(그들의 노력 덕분에)")]
ODD = [([('❸', 1), ('❸', 2), "Most manufacturers now provide free repair guides for every product they sell.", ('❸', 3)], 2, "정답 ▶ ③\n이유: 수리가 어려운 이유를 나열하는 흐름이에요. 제조사가 모든 제품에 무료 수리 안내서를 준다는 말은 흐름과 반대이고, 뒤의 '설명서를 얻지 못하는 게 흔하다'와도 모순돼요."),
 ([('❸', 7), ('❸', 8), "Fourth, consumers should replace their devices every two years.", ('❸', 10)], 2, "정답 ▶ ③\n이유: 수리할 권리 운동의 요구는 수리를 쉽게 만드는 것이에요. 2년마다 교체하라는 말은 운동의 목적과 반대이고, 순서도 Third(❸)가 와야 해요.")]
BLANK = [BL(c, 'Many companies do', 'third-party', ["official", "company-owned", "authorized"], "정답 ▶ third-party (제삼자의)\n이유: 앞 문장에서 제조사는 '공식' 수리소를 요구 → 많은 회사는 '제삼자' 수리점을 허용하지 않음\n오답 ▶ official 공식 · company-owned 회사 소유 · authorized 공인된 → 회사가 허용하는 쪽"),
 BL(c, 'The right-to-repair', 'a technician of your choice', ["the original manufacturer only", "a government office", "the nearest store"], "정답 ▶ a technician of your choice (자신이 선택한 기술자)\n이유: 소유자의 '권리' → 직접 고치거나 원하는 사람에게 맡길 자유\n오답 ▶ 제조사만 · 관공서 · 가장 가까운 가게 → 선택권이 없음"),
 BL(c, 'This movement is', 'joining the cause', ["leaving the market", "opposing the idea", "banning repairs"], "정답 ▶ joining the cause (대의에 동참하는)\n이유: 영향력이 '커지는(growing)' 이유 → 점점 더 많은 나라가 동참\n오답 ▶ 시장을 떠남 · 생각에 반대 · 수리 금지")]
GRAM = [{'q': "빈칸에 알맞은 것은?<br><b>Its manufacturer may require that it ______ to an official service center.</b>", 'opts': ["be brought", "is brought", "brings", "was brought"], 'ex': "정답 ▶ be brought\n이유: require/demand/insist/suggest + that + 주어 + (should) 동사원형"},
 {'q': "빈칸에 알맞은 것은?<br><b>It is common ______ consumers to be unable to acquire the instructions.</b>", 'opts': ["for", "of", "to", "with"], 'ex': "정답 ▶ for\n이유: 의미상 주어 for + 목적격. of는 kind, wise처럼 사람의 성격을 나타내는 형용사 뒤"},
 {'q': "빈칸에 알맞은 것은?<br><b>The practice of preventing consumers ______ custom software should be prohibited.</b>", 'opts': ["from installing", "to install", "installing", "install"], 'ex': "정답 ▶ from installing\n이유: prevent A from -ing"},
 {'q': "빈칸에 알맞은 것은?<br><b>If all these goals are accomplished, ______ less e-waste will be generated.</b>", 'opts': ["far", "very", "too", "so"], 'ex': "정답 ▶ far\n이유: 비교급 강조 far/much/even/still/a lot"}]
