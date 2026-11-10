from common import *
f, g = SEC['❻'], SEC['❼']
VOCAB = V('❻', [["along with", "~와 함께, ~에 더하여"], ["occur to", "~에 일어나다, 발생하다", "occurs to"], ["by oneself", "혼자서, 스스로", "by themselves"], ["gather", "모이다"],
  ["be staffed by", "~을 직원으로 두다", "are staffed by"], ["volunteer", "자원봉사자; 자원봉사하다"], ["technical", "기술적인"], ["such ~ that ...", "너무 ~해서 …하다", "such a success that"],
  ["neighboring", "이웃의, 인접한"], ["before long", "머지않아, 곧"], ["prevent A from -ing", "A가 ~하는 것을 막다", "preventing damaged items from becoming"], ["invaluable", "매우 귀중한 (= priceless)"],
  ["maintenance", "유지, 보수"], ["popularity", "인기"], ["sign up", "등록하다, 신청하다", "signing up"], ["enable A to-v", "A가 ~할 수 있게 하다", "enable individuals to maintain"], ["maintain", "~을 유지하다"],
  ["extend", "~을 연장하다"], ["life span", "수명", "life spans"], ["foster", "~을 조성하다, 촉진하다"], ["perspective", "관점, 시각"]]) + \
 V('❼', [["simply", "그저, 단순히"], ["be limited to", "~로 제한되다", "be limited to"], ["throw away", "~을 버리다", "throwing away"], ["order", "~을 주문하다"], ["replace", "~을 교체하다"],
  ["alternatively", "그렇지 않으면, 대안으로"], ["likely", "아마"], ["work toward", "~을 향해 노력하다"], ["even more importantly", "훨씬 더 중요한 것은"]])
PICK1 = [PK(f, 'When consumers are', 'helpful', 'misleading', "정답 ▶ helpful (유용한)\n오답 ▶ misleading (오해를 일으키는)\n이유: 알맞은 도구·재료와 '함께' 주어지면 스스로 고칠 수 있는 조언 → 유용한"),
 PK(f, 'They are free', 'gather', 'compete', "정답 ▶ gather (모이다)\n오답 ▶ compete (경쟁하다)\n이유: 만남의 장소(meeting places)에서 함께(together) '모여' 고침"),
 PK(f, 'The cafés are staffed', 'volunteer', 'paid', "정답 ▶ volunteer (자원봉사의)\n오답 ▶ paid (돈을 받는)\n이유: 무료(free) 장소 + 뒤에서 자원봉사하려고 등록하는 사람이 늘어남(signing up to volunteer)"),
 PK(f, 'It was such a success', 'success', 'failure', "정답 ▶ success (성공)\n오답 ▶ failure (실패)\n이유: 그래서(that) 아이디어가 곧 이웃 나라로 '퍼졌다'"),
 PK(f, 'Along with preventing', 'invaluable', 'worthless', "정답 ▶ invaluable (매우 귀중한)\n오답 ▶ worthless (가치 없는)\n이유: 사람들이 '나누도록' 장려하는 기술과 지식 → 귀중한. invaluable은 '가치 없는'이 아니라 '값을 매길 수 없을 만큼 귀중한'!"),
 PK(f, 'By providing spaces', 'extend', 'shorten', "정답 ▶ extend (연장하다)\n오답 ▶ shorten (줄이다)\n이유: 기기를 유지·관리하게 됨 → 수명을 '늘림'"),
 PK(f, 'Furthermore, they', 'positive', 'negative', "정답 ▶ positive (긍정적인)\n오답 ▶ negative (부정적인)\n이유: 지속 가능한 관점 → 미래에 '긍정적인' 영향"),
 PK(g, 'Imagine she lived', 'everyday', 'rare', "정답 ▶ everyday (일상의)\n오답 ▶ rare (드문)\n이유: 수리가 '그저(simply)' 일상의 한 부분인 세상 → 뒤에서 부품 주문·수리 카페·수리 쉬운 노트북"),
 PK(g, 'Repairing it probably', 'high', 'low', "정답 ▶ high (높은)\n오답 ▶ low (낮은)\n이유: 수리가 어렵지 않을 이유 → 수리 가능성 점수가 '높은' 노트북"),
 PK(g, 'Even more importantly', 'less', 'more', "정답 ▶ less (더 적은)\n오답 ▶ more (더 많은)\n이유: 지구를 더 깨끗하고 건강한 곳으로 → 전자 쓰레기를 '훨씬 적게' 만듦")]
TF = [TF(f, "With the right tools and advice, consumers can fix much of the damage themselves.", True, "they can repair much of the damage that occurs to electronic products by themselves", "정답 ▶ T\n이유: 알맞은 도구·재료와 조언이 있으면 대부분의 손상을 스스로 고칠 수 있어요."),
 TF(f, "People must pay a fee to use Repair Cafés.", False, "They are free meeting places", "정답 ▶ F\n이유: 무료 만남의 장소예요."),
 TF(f, "Repair Café experts teach people how to fix things.", True, "teach people how to fix things", "정답 ▶ T\n이유: 자원봉사 전문가들이 고치는 법을 가르쳐요."),
 TF(f, "The first Repair Café opened in Amsterdam in 2009.", True, "opened in the Netherlands in the city of Amsterdam in 2009", "정답 ▶ T\n이유: 2009년 네덜란드 암스테르담에서 처음 문을 열었어요."),
 TF(f, "Repair Cafés now exist in fewer than ten countries.", False, "Repair Cafés in over 30 countries", "정답 ▶ F\n이유: 30개국 이상에 있어요."),
 TF(f, "Fewer people are volunteering at Repair Cafés these days.", False, "with more and more people signing up to volunteer", "정답 ▶ F\n이유: 자원봉사 신청자가 점점 늘고 있어요."),
 TF(g, "In the imagined world, Liz's only choices would be costly repairs or a new laptop.", False, "her options wouldn't be limited to paying for expensive repairs or throwing away her laptop", "정답 ▶ F\n이유: 그 두 가지로 제한되지 않았을 거예요."),
 TF(g, "Liz could get repair advice at a Repair Café.", True, "to get advice on how to fix it", "정답 ▶ T\n이유: 가까운 수리 카페에 가서 고치는 방법에 대한 조언을 얻을 수 있었을 거예요."),
 TF(g, "The writer says a sustainable world can be achieved if we work together.", True, "a future we can all enjoy if we work toward it together", "정답 ▶ T\n이유: 함께 노력하면 모두가 누릴 수 있는 미래라고 해요.")]
MC = [MULTI("본문 ❻❼의 내용과 일치하지 <u>않는</u> 것은?", [
 "Repair Cafés expanded slowly and remain limited to the Netherlands.", "Volunteer specialists at the cafés offer technical guidance.", "The cafés help keep broken items from turning into e-waste.",
 "Liz could have ordered parts online and installed them herself.", "Liz's laptop would likely have had a high repairability score."],
 "정답 ▶ Repair Cafés expanded slowly and remain limited to the Netherlands.\n이유: the idea soon spread to neighboring countries ~ Before long, there were Repair Cafés in over 30 countries — 빠르게 30개국 이상으로 퍼짐\n포인트 ▶ expand = 확장되다 · specialist = expert · guidance = advice · keep A from -ing = prevent A from -ing · install = replace(교체해 끼우다)",
 [["수리 카페는 천천히 확장되었고 네덜란드에만 있다.", "Before long, there were Repair Cafés in over 30 countries", "✗ 30개국 이상"], ["카페의 자원봉사 전문가들은 기술적 안내를 제공한다.", "volunteer experts who can give technical advice", "specialist = expert ✔"],
  ["카페는 고장 난 물건이 전자 쓰레기가 되는 것을 막는다.", "preventing damaged items from becoming e-waste", "keep A from = prevent A from ✔"], ["Liz는 온라인으로 부품을 주문해 직접 끼울 수 있었을 것이다.", "order the necessary parts online and replace them herself", "일치 ✔"], ["Liz의 노트북은 아마 수리 가능성 점수가 높았을 것이다.", "a laptop with a high repairability score", "일치 ✔"]], ['❻', '❼']),
 MULTI("본문 ❻❼의 내용과 <u>일치하는</u> 것은?", ["Repair Cafés help people prolong the life of their devices.", "Repair Cafés sell new electronic devices at low prices.", "Only professionals can attend Repair Cafés.", "The writer thinks a sustainable future is impossible.", "Liz decided to throw her laptop away in the end."],
 "정답 ▶ Repair Cafés help people prolong the life of their devices.\n이유: Repair Cafés enable individuals to maintain their devices and extend their life spans\n오답 ▶ ② 새 기기 판매 ✗ ③ 누구나 모여 고침 ④ 함께 노력하면 누릴 수 있는 미래 ⑤ 결정은 나오지 않고 가정(Imagine)만\n포인트 ▶ prolong = extend · life = life span",
 [["", "extend their life spans", "일치 ✔"], ["", "fix their broken devices", "판매 ✗"], ["", "where people can gather together", "누구나"], ["", "a future we can all enjoy", "가능"], ["", "Imagine she lived in a world", "가정"]], ['❻', '❼'])]
PICK2 = [PK(f, 'When consumers are', 'are given', 'give', "정답 ▶ are given\n이유: 소비자가 도구를 '받는' 수동 (give A B의 수동: A are given B)"),
 PK(f, 'When consumers are', 'occurs', 'occur', "정답 ▶ occurs\n이유: 관계대명사 that의 선행사 the damage(셀 수 없음, 단수) → occurs"),
 PK(f, 'That is why', 'why', 'because', "정답 ▶ why\n이유: That is why + 결과 (그래서 ~하다). That is because + 원인 — 앞 문장이 '이유', 이 문장이 '결과'이므로 why"),
 PK(f, 'They are free', 'where', 'which', "정답 ▶ where\n이유: 선행사 places + 완전한 절(people can gather ~) → 관계부사 where"),
 PK(f, 'The cafés are staffed', 'who', 'which', "정답 ▶ who\n이유: 선행사 volunteer experts(사람) → 주격 관계대명사 who"),
 PK(f, 'It was such a success', 'such a success', 'so a success', "정답 ▶ such a success\n이유: such + a + (형용사) + 명사 + that ~. so는 형용사·부사 앞(so successful that)"),
 PK(f, 'Along with preventing', 'becoming', 'become', "정답 ▶ becoming\n이유: prevent A from -ing"),
 PK(g, 'Do you remember', 'who', 'which', "정답 ▶ who\n이유: 선행사 the girl(사람) → 주격 관계대명사 who"),
 PK(g, 'If that were', 'were', 'is', "정답 ▶ were\n이유: 가정법 과거 — If + 주어 + were, 주어 + would + 동사원형 (현재 사실의 반대)"),
 PK(g, 'Even more importantly', 'in which', 'which', "정답 ▶ in which\n이유: 뒤가 완전한 절(people will generate ~) → 전치사 + 관계대명사(= where). which만 쓰려면 뒤가 불완전해야 해요.")]
VERB = [VB(f, 'The first Repair', 'opened', 'open', "정답 ▶ opened\n이유: 카페가 '열린' 수동 → was opened"),
 VB(f, 'They continue to', 'signing', 'sign', "정답 ▶ signing\n이유: with + 목적어 + 분사 — 사람들이 '신청하는' 능동"),
 VB(f, 'By providing spaces', 'to maintain', 'maintain', "정답 ▶ to maintain\n이유: enable + 목적어 + to부정사"),
 VB(g, 'If that were', 'paying', 'pay', "정답 ▶ paying\n이유: be limited to의 to는 전치사 → 동명사 paying"),
 VB(g, 'Repairing it probably', 'purchased', 'purchase', "정답 ▶ purchased\n이유: would have + p.p. (~했을 것이다, 가정법 과거완료 형태)"),
 VB(g, 'Even more importantly', 'making', 'make', "정답 ▶ making\n이유: 콤마 뒤 결과의 분사구문 — 능동(목적어 our planet)")]
ERR = [ER(f, 'Along with preventing', ['preventing', 'encourage', ('to share', 'sharing')], 2, 'to share', "틀린 곳 ▶ ③ sharing → to share\n이유: encourage + 목적어 + to부정사\n나머지 ▶ ① 전치사 with 뒤 동명사 ✔ ② 주어 these cafés(복수) ✔"),
 ER(f, 'By providing spaces', ['providing', 'where', ('to maintain', 'maintaining')], 2, 'to maintain', "틀린 곳 ▶ ③ maintaining → to maintain\n이유: enable + 목적어 + to부정사\n나머지 ▶ ① by + 동명사 ✔ ② 선행사 spaces + 완전한 절 → where ✔"),
 ER(g, 'If that were', ['were', ('paying', 'pay'), 'buying'], 1, 'paying', "틀린 곳 ▶ ② pay → paying\n이유: be limited to + 명사/동명사 (to는 전치사). paying ~ or throwing ~ and buying 병렬\n나머지 ▶ ① 가정법 과거 were ✔ ③ 병렬 동명사 ✔"),
 ER(g, 'Even more importantly', ['in which', 'far', ('making', 'made')], 2, 'making', "틀린 곳 ▶ ③ made → making\n이유: 결과의 분사구문 — 지구를 '만드는' 능동(목적어 our planet + 보어)\n나머지 ▶ ① 전치사 + 관계대명사 ✔ ② 비교급 강조 far ✔")]
SCR = [('❻', 1), ('❻', 2), ('❻', 3), ('❻', 5), ('❻', 9), ('❻', 10), ('❼', 1), ('❼', 3), ('❼', 6)]
ORDER = [[('❻', 1), ('❻', 2), ('❻', 3), ('❻', 4)], [('❻', 4), ('❻', 5), ('❻', 6), ('❻', 7)], [('❼', 2), ('❼', 3), ('❼', 4), ('❼', 5)]]
INSERT = [([('❻', 0), ('❻', 1), ('❻', 2), ('❻', 3)], 1, "정답 ▶ ① (That is why ~ 문장)\n이유: 도구·조언이 있으면 스스로 고칠 수 있다(이유) → That is why(그래서) 수리 카페가 시작됨(결과) → They(카페)는 …"),
 ([('❼', 4), ('❼', 5), ('❼', 6), ('❼', 7)], 2, "정답 ▶ ② (In fact ~ 문장)\n이유: Liz의 가정 이야기 끝 → In fact(사실) 이런 지속 가능한 세상은 우리 모두의 미래 → Even more importantly(훨씬 더 중요한 것은)")]
ODD = [([('❻', 4), ('❻', 5), "Most visitors to Repair Cafés end up buying brand-new devices instead.", ('❻', 6)], 2, "정답 ▶ ③\n이유: 수리 카페가 성공해 세계로 퍼졌다는 흐름이에요. 방문객 대부분이 결국 새 기기를 산다는 말은 카페의 목적과 반대예요."),
 ([('❼', 2), ('❼', 3), "Online stores usually do not sell spare parts to individual buyers.", ('❼', 4)], 2, "정답 ▶ ③\n이유: 수리가 일상인 세상에서 Liz가 가질 수 있었던 선택지를 나열하는 흐름이에요. 온라인에서 부품을 팔지 않는다는 말은 바로 앞(부품을 온라인 주문)과 모순돼요.")]
BLANK = [BL(f, 'When consumers are', 'by themselves', ["at factories", "with machines", "for money"], "정답 ▶ by themselves (스스로)\n이유: 그래서 사람들이 직접 고치는 '수리 카페'가 생김\n오답 ▶ 공장에서 · 기계로 · 돈을 받고"),
 BL(f, 'Furthermore, they', 'perspective', ["product", "salary", "contest"], "정답 ▶ perspective (관점)\n이유: '지속 가능한' 생각의 틀을 키움(foster) → 관점\n오답 ▶ product 제품 · salary 월급 · contest 대회"),
 BL(g, 'Alternatively', 'the nearest Repair Café', ["a new laptop store", "the trash can", "the factory"], "정답 ▶ the nearest Repair Café (가장 가까운 수리 카페)\n이유: 고치는 방법에 대한 '조언을 얻으러' 가는 곳 → 앞 단락의 수리 카페\n오답 ▶ 새 노트북 가게 · 쓰레기통 · 공장")]
GRAM = [{'q': "빈칸에 알맞은 것은?<br><b>It was ______ success that the idea soon spread to neighboring countries.</b>", 'opts': ["such a", "so a", "so", "such"], 'ex': "정답 ▶ such a\n이유: such + a + 명사 + that (너무 ~해서 …하다)"},
 {'q': "빈칸에 알맞은 것은?<br><b>If that ______ the case, her options wouldn't be limited.</b>", 'opts': ["were", "is", "will be", "has been"], 'ex': "정답 ▶ were\n이유: 가정법 과거: If + 주어 + were ~, 주어 + would + 동사원형"},
 {'q': "빈칸에 알맞은 것은?<br><b>Repair Cafés enable individuals ______ their devices.</b>", 'opts': ["to maintain", "maintain", "maintaining", "maintained"], 'ex': "정답 ▶ to maintain\n이유: enable + 목적어 + to부정사"},
 {'q': "빈칸에 알맞은 것은?<br><b>It is a future ______ people will generate far less e-waste.</b>", 'opts': ["in which", "which", "what", "who"], 'ex': "정답 ▶ in which\n이유: 완전한 절 앞 → 전치사 + 관계대명사(= where)"}]
