from common import *
a, b = SEC['❶'], SEC['❷']
VOCAB = V('❶', [["accidentally", "실수로, 우연히"], ["damage", "~에 손상을 입히다; 손상", "damaging"], ["turn on", "켜지다", "turns on"], ["cracked", "금이 간, 갈라진"],
  ["have A repaired", "A를 수리받다(수리되게 하다)", "have it repaired"], ["hesitate to-v", "~하기를 망설이다, 주저하다", "hesitating to do"], ["besides", "게다가 (= moreover, in addition)"],
  ["get rid of", "~을 버리다, 없애다", "getting rid of"], ["purchase", "~을 구입하다 (= buy)", "purchasing"], ["reasonable", "합리적인, 타당한 (↔ unreasonable)"], ["option", "선택(지) (= choice)"],
  ["in reality", "실제로는 (= in fact, actually)"], ["trash", "쓰레기, 쓰레기통"], ["contribute to", "~에 기여하다, ~의 한 원인이 되다", "contributing to"], ["e-waste", "전자 쓰레기"]]) + \
 V('❷', [["refer to", "~을 나타내다, 가리키다", "refers to"], ["discarded", "버려진"], ["electronic device", "전자 장치", "electronic devices"], ["electrical appliance", "전기 기기, 가전제품", "electrical appliances"],
  ["toxic", "유독성의 (= poisonous)"], ["contain", "~을 포함하다", "contained"], ["lead", "납"], ["hazard", "위험 (요소) (= danger)"], ["to make matters worse", "설상가상으로, 엎친 데 덮친 격으로"],
  ["alarming", "걱정스러운, 놀라운"], ["metric ton", "미터톤(1,000kg)", "metric tons"], ["generate", "~을 발생시키다, 만들어 내다", "generated"], ["annually", "매년, 해마다 (= each year)"],
  ["double", "두 배가 되다", "doubled"], ["address", "(문제 등을) 다루다, 처리하다"], ["focus on", "~에 중점을 두다", "focused on"], ["practical", "현실성 있는, 실용적인"], ["approach", "접근법"]])
PICK1 = [PK(a, 'On her way', 'accidentally', 'intentionally', "정답 ▶ accidentally (실수로)\n오답 ▶ intentionally (의도적으로)\n이유: 모임에 가던 길에 노트북을 '실수로' 떨어뜨려 손상시킴"),
 PK(a, 'Although it still', 'cracked', 'polished', "정답 ▶ cracked (금이 간)\n오답 ▶ polished (윤이 나는)\n이유: Although(비록 켜지긴 하지만) 뒤 → 손상된 상태: 화면은 '금이 갔고' 키도 작동 안 함"),
 PK(a, 'She can have', 'hesitating', 'eager', "정답 ▶ hesitating (망설이는)\n오답 ▶ eager (열망하는)\n이유: 수리할 수 '있지만(but)' + 다음 문장(수리는 비싸고 오래 걸림) → 수리를 '망설이고' 있음. eager(몹시 하고 싶은)면 but의 반전과 맞지 않아요."),
 PK(a, 'Sometimes repairs', 'expensive', 'affordable', "정답 ▶ expensive (비싼)\n오답 ▶ affordable (적당한 가격의)\n이유: 수리를 망설이는 이유 → 비싸고 오래 걸림"),
 PK(a, 'In this case', 'reasonable', 'irrational', "정답 ▶ reasonable (합리적인)\n오답 ▶ irrational (비이성적인)\n이유: 수리는 비싸고 노트북도 5년 됨 → 새로 사는 게 더 '합리적인' 선택처럼 '보일 수 있다(might seem)'"),
 PK(a, 'If Liz throws', 'contributing to', 'preventing', "정답 ▶ contributing to (~에 기여하는)\n오답 ▶ preventing (막는)\n이유: 노트북을 버리면 전자 쓰레기라는 심각한 문제에 '보태게' 됨"),
 PK(b, 'The term refers', 'discarded', 'brand-new', "정답 ▶ discarded (버려진)\n오답 ▶ brand-new (새것인)\n이유: 전자 쓰레기 = '버려진' 전자 장치와 전기 기기"),
 PK(b, 'Due to toxic', 'toxic', 'harmless', "정답 ▶ toxic (유독성의)\n오답 ▶ harmless (무해한)\n이유: 납 같은 물질 때문에 건강·환경 '위험 요소(hazard)'가 됨 → 유독성"),
 PK(b, 'To make matters', 'alarming', 'reassuring', "정답 ▶ alarming (걱정스러운)\n오답 ▶ reassuring (안심시키는)\n이유: To make matters worse(설상가상으로) → 양이 '걱정스러운' 속도로 증가"),
 PK(b, 'For this reason', 'easier', 'harder', "정답 ▶ easier (더 쉬운)\n오답 ▶ harder (더 어려운)\n이유: 전자 쓰레기 문제를 다루려는 노력 → 제품을 수리하기 '더 쉽게' 만드는 것")]
TF = [TF(a, "Liz damaged her laptop on purpose.", False, "accidentally dropped her laptop", "정답 ▶ F\n이유: 실수로(accidentally) 떨어뜨렸어요.\n어휘 ▶ on purpose(일부러) ↔ accidentally"),
 TF(a, "Liz's laptop no longer turns on at all.", False, "it still turns on", "정답 ▶ F\n이유: 여전히 켜지기는 해요."),
 TF(a, "Liz is reluctant to have her laptop fixed.", True, "she is hesitating to do so", "정답 ▶ T\n이유: 수리받기를 망설이고 있어요.\n어휘 ▶ reluctant to(~하기를 꺼리는) ≒ hesitate to · fixed = repaired"),
 TF(a, "Repairs are sometimes costly and time-consuming.", True, "repairs are expensive, and they often take a long time", "정답 ▶ T\n이유: 수리는 때때로 비싸고 오래 걸려요.\n어휘 ▶ costly = expensive · time-consuming = take a long time"),
 TF(a, "The writer says buying a new laptop is definitely the best choice.", False, "it may not be the best thing to do", "정답 ▶ F\n이유: 실제로는 최선이 아닐 수 있다고 해요."),
 TF(b, "E-waste includes electrical appliances that people have thrown away.", True, "discarded electronic devices and electrical appliances", "정답 ▶ T\n이유: 버려진 전자 장치와 전기 기기를 말해요.\n어휘 ▶ thrown away = discarded"),
 TF(b, "The amount of e-waste generated in 2021 was lower than in 2014.", False, "a 37% increase from 2014", "정답 ▶ F\n이유: 2014년보다 37% 증가했어요."),
 TF(b, "Data about e-waste was first collected in 2014.", True, "the year when data about e-waste was first collected", "정답 ▶ T\n이유: 2014년이 자료를 처음 수집한 해예요."),
 TF(b, "Experts expect the annual amount of e-waste to double by 2030.", True, "will have doubled in just 16 years", "정답 ▶ T\n이유: 2030년이면 16년 만에 두 배가 될 거라고 예측해요.")]
MC = [MULTI("본문 ❶❷의 내용과 일치하지 <u>않는</u> 것은?", [
 "Most efforts to address e-waste concentrate on recycling raw materials.", "Liz's laptop sustained damage when it fell onto the street.", "The laptop is roughly half a decade old.",
 "Lead is cited as an example of a hazardous substance in e-waste.", "Global e-waste reached 57.4 million metric tons in 2021."],
 "정답 ▶ Most efforts to address e-waste concentrate on recycling raw materials.\n이유: most of which are focused on making products easier to repair — 재활용이 아니라 '수리하기 쉽게' 만드는 데 중점\n포인트 ▶ concentrate on = focus on · sustain damage = 손상을 입다 · roughly = about · half a decade = 5년 · cite = 언급하다 · hazardous = toxic",
 [["전자 쓰레기 대응 노력 대부분은 원자재 재활용에 집중한다.", "most of which are focused on making products easier to repair", "✗ 수리 용이성"], ["Liz의 노트북은 길에 떨어져 손상을 입었다.", "dropped her laptop on the street, seriously damaging it", "sustain damage ✔"],
  ["노트북은 대략 5년 되었다.", "the laptop is about five years old", "roughly = about ✔"], ["납은 전자 쓰레기 속 유해 물질의 예로 언급된다.", "toxic materials contained in these products, such as lead", "hazardous = toxic ✔"], ["2021년 전 세계 전자 쓰레기는 5,740만 톤에 달했다.", "a total of 57.4 million metric tons of e-waste was generated worldwide", "일치 ✔"]], ['❶', '❷']),
 MULTI("본문 ❶❷의 내용과 <u>일치하는</u> 것은?", [
 "The yearly volume of e-waste is rising at a worrying pace.", "Liz has already decided to buy a new laptop.", "All of the laptop's keys still work properly.",
 "E-waste refers only to broken smartphones.", "E-waste poses little risk to human health."],
 "정답 ▶ The yearly volume of e-waste is rising at a worrying pace.\n이유: the amount of e-waste produced each year is increasing at an alarming rate\n오답 ▶ ② 망설이는 중이며 결정한 것 아님 ③ some keys are not working ④ 전자 장치와 전기 기기 전반 ⑤ serious health ~ hazard\n포인트 ▶ volume = amount · worrying = alarming · pace = rate · pose a risk = 위험을 제기하다",
 [["", "increasing at an alarming rate", "일치 ✔"], ["", "she is hesitating to do so", "결정 안 함"], ["", "some keys are not working", "일부 고장"], ["", "discarded electronic devices and electrical appliances", "전반"], ["", "a serious health and environmental hazard", "심각한 위험"]], ['❶', '❷'])]
PICK2 = [PK(a, 'On her way', 'damaging', 'damaged', "정답 ▶ damaging\n이유: 콤마 뒤 결과의 분사구문 — 떨어뜨린 일이 노트북을 '손상시키는' 능동, 목적어 it이 있음 → damaging"),
 PK(a, 'Although it still', 'Although', 'Despite', "정답 ▶ Although\n이유: 뒤에 절(it still turns on) → 접속사 Although. Despite는 전치사라 명사(구)만"),
 PK(a, 'She can have', 'repaired', 'repair', "정답 ▶ repaired\n이유: have + 목적어 + p.p. — 노트북이 '수리되는' 수동 관계"),
 PK(a, 'In this case', 'might seem', 'might seems', "정답 ▶ seem\n이유: 조동사 might + 동사원형. 주어는 동명사구 두 개(getting ~ and purchasing ~)"),
 PK(a, 'In reality', 'to do', 'doing', "정답 ▶ to do\n이유: the best thing을 뒤에서 꾸미는 형용사적 to부정사 (할 수 있는 최선의 일)"),
 PK(a, 'If Liz throws', 'throws', 'will throw', "정답 ▶ throws\n이유: 조건 부사절(If ~)은 미래라도 현재시제"),
 PK(b, 'Due to toxic', 'contained', 'containing', "정답 ▶ contained\n이유: 물질이 제품에 '포함된' 수동 → 과거분사가 toxic materials 수식"),
 PK(b, 'To make matters', 'is increasing', 'are increasing', "정답 ▶ is\n이유: 주어의 핵 the amount(단수). of e-waste produced each year는 수식어"),
 PK(b, 'In 2021', 'when data', 'which data', "정답 ▶ when\n이유: 선행사 the year(시간) + 완전한 절(data ~ was first collected) → 관계부사 when"),
 PK(b, 'For this reason', 'most of which', 'most of them', "정답 ▶ most of which\n이유: 콤마 뒤 두 절을 잇는 관계대명사 필요(접속사 없음) → most of which. them을 쓰면 접속사가 없어 문장이 둘로 쪼개짐")]
VERB = [VB(a, 'Although it still', 'working', 'work', "정답 ▶ working\n이유: are not + -ing 현재진행 (작동하지 않고 있다)"),
 VB(a, 'She can have', 'hesitating', 'hesitate', "정답 ▶ hesitating\n이유: is + -ing 현재진행"),
 VB(a, 'If Liz throws', 'contributing', 'contribute', "정답 ▶ contributing\n이유: will be + -ing 미래진행"),
 VB(b, 'Experts predict', 'doubled', 'double', "정답 ▶ doubled\n이유: by 2030(미래의 기준 시점까지) → 미래완료 will have + p.p."),
 VB(b, 'For this reason', 'being', 'be', "정답 ▶ being\n이유: are being + p.p. 현재진행 수동 (노력이 이루어지고 있다)"),
 VB(b, 'For this reason', 'making', 'make', "정답 ▶ making\n이유: 전치사 on 뒤 동명사 (focused on making)")]
ERR = [ER(a, 'She can have', ['have', ('repaired', 'repairing'), 'to do'], 1, 'repaired', "틀린 곳 ▶ ② repairing → repaired\n이유: have + 목적어(it) + p.p. — 노트북이 수리'되는' 수동\n나머지 ▶ ① 조동사 can + 동사원형 ✔ ③ hesitate + to부정사 ✔"),
 ER(a, 'In this case', ['getting', ('purchasing', 'purchase'), 'like'], 1, 'purchasing', "틀린 곳 ▶ ② purchase → purchasing\n이유: getting rid of ~ and purchasing ~ — 동명사 주어 병렬\n나머지 ▶ ① 동명사 주어 ✔ ③ seem like + 명사(구) ✔"),
 ER(b, 'Due to toxic', [('Due to', 'Because'), 'contained', 'such as'], 0, 'Due to', "틀린 곳 ▶ ① Because → Due to\n이유: 뒤에 명사구(toxic materials ~) → 전치사 Due to\n나머지 ▶ ② 수동 과거분사 ✔ ③ such as + 예시 ✔"),
 ER(b, 'Experts predict', ['that', 'generated', ('will have doubled', 'will double')], 2, 'will have doubled', "틀린 곳 ▶ ③ will double → will have doubled\n이유: by 2030 + in just 16 years(2014~2030 기간 동안 완료) → 미래완료\n나머지 ▶ ① 명사절 that ✔ ② 발생'된' 수동 과거분사 ✔")]
SCR = [('❶', 2), ('❶', 5), ('❶', 6), ('❶', 7), ('❷', 1), ('❷', 3), ('❷', 6)]
ORDER = [[('❶', 2), ('❶', 3), ('❶', 4), ('❶', 5)], [('❷', 3), ('❷', 4), ('❷', 5), ('❷', 6)]]
INSERT = [([('❶', 4), ('❶', 5), ('❶', 6), ('❶', 7)], 2, "정답 ▶ ② (In reality, however ~ 문장)\n이유: 새것을 사는 게 더 합리적으로 보일 수 있다 → In reality, however(하지만 실제로는) 최선이 아닐 수 있다 → 그 이유: 전자 쓰레기 문제에 기여"),
 ([('❷', 0), ('❷', 1), ('❷', 2), ('❷', 3)], 3, "정답 ▶ ③ (To make matters worse ~ 문장)\n이유: 전자 쓰레기는 유독 물질 때문에 심각한 위험(문제 1) → To make matters worse(설상가상으로) 양까지 급증(문제 2)")]
ODD = [([('❶', 2), ('❶', 3), "Many laptops today come with a free three-year warranty that covers accidental drops.", ('❶', 4)], 2, "정답 ▶ ③\n이유: 수리를 망설이는 이유(비싸고 오래 걸림, 5년 된 노트북)를 이어 가는 흐름이에요. 무상 보증이 실수로 떨어뜨린 것까지 보장한다면 망설일 이유가 없어져 흐름과 맞지 않아요."),
 ([('❷', 4), ('❷', 5), "Most consumers now prefer to repair their devices rather than replace them.", ('❷', 6)], 2, "정답 ▶ ③\n이유: 전자 쓰레기가 급증한다는 흐름이에요. 대부분 소비자가 이미 수리를 선호한다면 쓰레기가 늘어날 이유가 약해지고, 뒤의 '그래서 수리를 쉽게 만들려는 노력'과도 어긋나요.")]
BLANK = [BL(a, 'Sometimes repairs', 'take a long time', ["are always free", "are very simple", "make laptops faster"], "정답 ▶ take a long time (오랜 시간이 걸리다)\n이유: 수리를 망설이는 이유 — 비싸고 '오래 걸림'\n오답 ▶ 늘 무료 · 아주 간단함 · 노트북을 빠르게 함 → 망설일 이유가 아님"),
 BL(b, 'The term refers', 'discarded', ["borrowed", "upgraded", "imported"], "정답 ▶ discarded (버려진)\n이유: 전자 '쓰레기'의 정의 → 버려진 기기\n오답 ▶ borrowed 빌린 · upgraded 업그레이드된 · imported 수입된"),
 BL(b, 'For this reason', 'easier to repair', ["cheaper to produce", "harder to open", "faster to sell"], "정답 ▶ easier to repair (수리하기 더 쉬운)\n이유: 뒤에 소개되는 접근법(수리할 권리·수리 가능성 지수·수리 카페)이 모두 수리 이야기\n오답 ▶ 생산비 절감 · 열기 어렵게 · 빨리 팔기")]
GRAM = [{'q': "빈칸에 알맞은 것은?<br><b>Liz dropped her laptop on the street, seriously ______ it.</b>", 'opts': ["damaging", "damaged", "damage", "to damage"], 'ex': "정답 ▶ damaging\n이유: 결과의 분사구문, 능동(목적어 it) → 현재분사\n포인트 ▶ = which seriously damaged it"},
 {'q': "빈칸에 알맞은 것은?<br><b>She can have it ______, but she is hesitating to do so.</b>", 'opts': ["repaired", "repair", "repairing", "to repair"], 'ex': "정답 ▶ repaired\n이유: have + 목적어 + p.p.(수동). 수리공에게 시키는 능동이면 have the mechanic repair it"},
 {'q': "빈칸에 알맞은 것은?<br><b>By 2030, the amount of e-waste ______ in just 16 years.</b>", 'opts': ["will have doubled", "has doubled", "doubled", "had doubled"], 'ex': "정답 ▶ will have doubled\n이유: by + 미래 시점 → 미래완료"},
 {'q': "빈칸에 알맞은 것은?<br><b>Efforts are being made, most of ______ are focused on making products easier to repair.</b>", 'opts': ["which", "them", "that", "what"], 'ex': "정답 ▶ which\n이유: 부분 표현 + 관계대명사(most of which). that은 전치사 뒤·계속적 용법 불가"}]
