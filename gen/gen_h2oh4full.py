import sys, json, subprocess, re
sys.path.insert(0, '/home/claude/work/gen')
from gencommon import write
# 고2 능률(오선영) 영어Ⅱ L4 · 본문 완전정복 k1~k3 (11/11) — 3과 완전정복(gen_h2ohfull.py)과 같은 방식·난이도
CH = {
 '❶': [
  "On her way / to a study group meeting, / Liz accidentally dropped / her laptop / on the street, / seriously damaging it.",
  "Although / it still turns on, / the screen is cracked, / and some keys / are not working.",
  "She can have / it repaired, / but she / is hesitating / to do so.",
  "Sometimes / repairs are expensive, / and they often / take a long time.",
  "Besides, / the laptop is / about / five years old.",
  "In this case, / getting rid of / the old one / and purchasing / a new one / might seem like / a more reasonable option.",
  "In reality, / however, / it may not be / the best thing / to do.",
  "If Liz throws / her laptop / in the trash, / she will be contributing / to a serious problem: / e-waste.",
 ],
 '❷': [
  "What exactly / is / e-waste?",
  "The term / refers to / discarded electronic devices / and electrical appliances.",
  "Due to / toxic materials / contained in these products, / such as lead, / e-waste is / a serious health / and environmental hazard.",
  "To make matters worse, / the amount of e-waste / produced each year / is increasing / at an alarming rate.",
  "In 2021, / a total of / 57.4 million metric tons / of e-waste / was generated worldwide, / which was / a 37% increase / from 2014, / the year when / data about e-waste / was first collected.",
  "Experts predict / that by 2030, / the amount of e-waste / generated annually / will have doubled / in just 16 years.",
  "For this reason, / efforts are being made / to address this problem, / most of which / are focused on / making products / easier to repair.",
  "Let's take a look / at some / practical approaches / from around the world.",
 ],
 '❸': [
  "One reason / many people / dispose of / their damaged devices / is that / they are too difficult / to repair.",
  "For example, / a device / may be difficult / to disassemble, / or its manufacturer / may require / that it be brought / to an official service center / to be fixed.",
  "Many companies / do not allow / their customers / to take / their damaged items / to third-party repair shops.",
  "What is more, / some products / are intentionally designed / to be difficult / to repair.",
  "It is common / for consumers / to be unable / to acquire the instructions / for how to fix their items / or the parts / needed to complete repairs.",
  "The right-to-repair movement / is trying / to solve these problems / by promoting legislation / that states the following: / If you own a product, / you have the right / to fix it yourself / or bring it / to a technician / of your choice.",
  "To protect / the rights of consumers, / the right-to-repair movement / demands / four things.",
  "First, / companies must make / information about their products / available / to everyone.",
  "Second, / third parties, / including individuals, / should be able to obtain / the parts and tools / required / to make repairs.",
  "Third, / the practice of / preventing consumers / from installing custom software / on their own devices / should be prohibited / by law.",
  "Finally, / it demands / that manufacturers / design devices / in a way / that makes repairs / as easy as possible.",
  "Advocates of the movement / say that / if all these goals / are accomplished, / far less e-waste / will be generated.",
  "Thanks to / their efforts, / more than 40 states / in the U.S. / have begun working / on right-to-repair legislation.",
  "This movement / is gaining / a growing influence / in Europe as well, / with more and more countries / joining the cause.",
 ],
 '❹': [
  "In January 2021, / the French government / passed a bill / that requires / that every manufacturer / include / a “repairability index” / on five categories / of electronic devices and electrical appliances: / smartphones, laptops, washing machines, televisions, and lawn mowers.",
  "Using a score / ranging from 0 to 10, / as well as / a color-coded system, / the index / lets consumers see / how easily / the product can be repaired / before they purchase it.",
  "The index / takes into account / several elements, / including / the availability of repair information, / the ease of disassembly, / and the price / of spare parts.",
  "A low number / on a bright red label / means that / repairing the product / will be difficult, / whereas / a high number / on a green label / indicates that / the product is easy / to repair.",
 ],
 '❺': [
  "The index / was designed / to have / two positive effects.",
  "Firstly, / it allows consumers / to make informed decisions / when purchasing / new devices and appliances.",
  "Secondly, / it encourages manufacturers / to make / their products / easier to repair.",
  "As a result, / with fewer / electronic and electrical items / ending up / in its landfills, / France can expect / to make a transition / to a more sustainable society / in the near future.",
  "The impact of the index, / however, / is likely / to spread / far beyond France.",
  "We live / in a global economy, / and any company / that wants to sell / its appliances / on the French market / will need to label / its products / according to / the repairability index.",
  "If the index / is successful, / we can anticipate / seeing more countries / around the world / following / France's innovative lead.",
 ],
 '❻': [
  "When consumers / are given / the right tools and materials, / along with / some helpful advice, / they can repair / much of the damage / that occurs / to electronic products / by themselves.",
  "That is why / Repair Cafés / were / started.",
  "They are / free meeting places / where people / can gather together / and fix / their broken devices.",
  "The cafés / are staffed by / volunteer experts / who can give / technical advice / and teach people / how to fix things.",
  "The first Repair Café / was opened / in the Netherlands / in the city of Amsterdam / in 2009.",
  "It was / such a success / that the idea / soon spread / to neighboring countries.",
  "Before long, / there were / Repair Cafés / in over 30 countries / around the world.",
  "Along with / preventing damaged items / from becoming e-waste, / these cafés also / encourage people / to share / their invaluable skills and knowledge / about the repair and maintenance / of electronics.",
  "They continue / to grow / in popularity, / with more and more people / signing up / to volunteer.",
  "By providing spaces / where people can learn, / Repair Cafés / enable individuals / to maintain their devices / and extend / their life spans.",
  "Furthermore, / they foster / a sustainable perspective / that can have / a huge positive impact / on our future.",
 ],
 '❼': [
  "Do you remember / Liz, / the girl / who dropped / her laptop?",
  "Imagine / she lived / in a world / where repairing / damaged devices and appliances / was simply / part of everyday life.",
  "If that were the case, / her options / wouldn't be limited to / paying for expensive repairs / or throwing away her laptop / and buying / a new one.",
  "She would be able / to order / the necessary parts / online / and replace them / herself.",
  "Alternatively, / she could bring / her damaged device / to the nearest Repair Café / to get advice / on how to fix it.",
  "Repairing it / probably wouldn't be / very hard, / as she likely / would have purchased / a laptop / with a high repairability score.",
  "In fact, / this sustainable world / is a future / we can all enjoy / if we work toward it / together.",
  "Even more importantly, / it is a future / in which / people will generate / far less e-waste, / making our planet / a cleaner, healthier place / for everyone.",
 ],
}
HUNT = {
 '❶': ("On her way to a study group meeting, Liz accidentally dropped her laptop on the street, seriously [[damaged|damaging]] it. "
       "[[Despite|Although]] it still turns on, the screen is cracked, and some keys are not working. "
       "She can have it [[repairing|repaired]], but she is hesitating to do so. "
       "Sometimes repairs are [[affordable|expensive]], and they often take a long time. "
       "Besides, the laptop is about five years old. "
       "In this case, getting rid of the old one and purchasing a new one might seem like a more [[unreasonable|reasonable]] option. "
       "In reality, however, it may not be the best thing [[doing|to do]]. "
       "If Liz [[will throw|throws]] her laptop in the trash, she will be [[preventing|contributing]] to a serious problem: e-waste.",
       ["콤마 뒤 결과의 분사구문 — 떨어뜨린 일이 노트북을 '손상시키는' 능동(목적어 it) → damaging",
        "뒤에 절(it still turns on)이 옴 → 접속사 Although. Despite는 전치사",
        "have + 목적어 + p.p. — 노트북이 '수리되는' 수동 → repaired",
        "[어휘] 수리를 망설이는 이유 + and 오래 걸린다 → '비싸다(expensive)'. affordable(적당한 가격의)이면 망설일 이유가 없어요",
        "[어휘] 비싸고 오래된 노트북 → 새로 사는 게 더 '합리적인(reasonable)' 선택처럼 보일 수 있음. 다음 문장 However로 반박",
        "the best thing을 꾸미는 형용사적 to부정사 → to do",
        "조건 부사절(If ~)은 미래라도 현재시제 → throws",
        "[어휘] 버리면 전자 쓰레기 문제에 '기여하게(contributing to)' 됨. preventing은 뜻도 반대이고 to와 함께 쓰지도 않아요"]),
 '❷': ("What exactly is e-waste? "
       "The term refers to [[recycled|discarded]] electronic devices and electrical appliances. "
       "Due to toxic materials [[containing|contained]] in these products, such as lead, e-waste is a serious health and environmental hazard. "
       "To make matters [[better|worse]], the amount of e-waste produced each year [[are|is]] increasing at an alarming rate. "
       "In 2021, a total of 57.4 million metric tons of e-waste was generated worldwide, [[that|which]] was a 37% increase from 2014, the year [[which|when]] data about e-waste was first collected. "
       "Experts predict that by 2030, the amount of e-waste generated annually [[has|will have]] doubled in just 16 years. "
       "For this reason, efforts are being made to address this problem, most of [[them|which]] are focused on making products easier to repair. "
       "Let's take a look at some practical approaches from around the world.",
       ["[어휘] 전자 '쓰레기'의 정의 → '버려진(discarded)' 장치. recycled(재활용된)는 쓰레기가 아님",
        "물질이 제품에 '포함된' 수동 → 과거분사 contained",
        "[어휘] 유독성 위험에 더해 양까지 급증 → To make matters worse(설상가상으로). better는 반대",
        "주어의 핵 the amount(단수) → is",
        "콤마 뒤 계속적 용법 → which (that 불가)",
        "선행사 the year(시간) + 완전한 절 → 관계부사 when",
        "by 2030(미래 시점까지) → 미래완료 will have doubled",
        "콤마 뒤 두 절을 잇는 관계대명사 필요 → most of which. them이면 접속사가 없음"]),
 '❸': ("One reason many people dispose of their damaged devices [[are|is]] that they are too difficult to repair. "
       "For example, a device may be difficult to [[assemble|disassemble]], or its manufacturer may require that it [[is|be]] brought to an official service center to be fixed. "
       "Many companies do not allow their customers [[taking|to take]] their damaged items to third-party repair shops. "
       "What is more, some products are [[accidentally|intentionally]] designed to be difficult to repair. "
       "It is common for consumers to be unable to acquire the instructions for how to fix their items or the parts [[needing|needed]] to complete repairs. "
       "The right-to-repair movement is trying to solve these problems by promoting legislation that states the following: If you own a product, you have the right to fix it yourself or bring it to a technician of your choice. "
       "To protect the rights of consumers, the right-to-repair movement demands four things. "
       "First, companies must make information about their products [[unavailable|available]] to everyone. "
       "Second, third parties, including individuals, should be able to obtain the parts and tools required to make repairs. "
       "Third, the practice of preventing consumers from [[install|installing]] custom software on their own devices should be [[encouraged|prohibited]] by law. "
       "Finally, it demands that manufacturers design devices in a way that makes repairs as easy as possible. "
       "Advocates of the movement say that if all these goals are accomplished, [[very|far]] less e-waste will be generated. "
       "Thanks to their efforts, more than 40 states in the U.S. have begun working on right-to-repair legislation. "
       "This movement is gaining a growing influence in Europe as well, with more and more countries [[joined|joining]] the cause.",
       ["주어의 핵 One reason(단수) → is (many people ~ devices는 reason을 꾸미는 절)",
        "[어휘] 수리하려면 열어서 '분해해야(disassemble)' 함 → 분해가 어려운 기기. assemble은 '조립하다'",
        "require that + 주어 + (should) 동사원형 → be brought",
        "allow + 목적어 + to부정사 → to take",
        "[어휘] 수리하기 어렵게 '설계된(designed)' → 의도적으로(intentionally). 설계는 우연히 할 수 없어요",
        "부품이 수리에 '필요한' 수동 → 과거분사 needed",
        "[어휘] 소비자 권리를 위한 요구 → 정보를 모두가 '이용할 수 있게(available)'",
        "prevent A from -ing → installing",
        "[어휘] 소비자를 '막는' 관행 → 법으로 '금지되어야(prohibited)'. encouraged(장려)면 운동의 목적과 반대",
        "비교급 less 강조 → far (very는 비교급 강조 불가)",
        "with + 목적어 + 분사: 나라들이 '동참하는' 능동 → joining"]),
 '❹': ("In January 2021, the French government passed a bill that requires that every manufacturer [[includes|include]] a “repairability index” on five categories of electronic devices and electrical appliances: smartphones, laptops, washing machines, televisions, and lawn mowers. "
       "[[Used|Using]] a score ranging from 0 to 10, as well as a color-coded system, the index lets consumers [[to see|see]] how [[easy|easily]] the product can be repaired before they purchase it. "
       "The index takes into account several elements, including the [[absence|availability]] of repair information, the ease of disassembly, and the price of spare parts. "
       "A low number on a bright red label means that repairing the product will be [[simple|difficult]], [[despite|whereas]] a high number on a green label indicates that the product is easy to repair.",
       ["require that + 주어 + (should) 동사원형 → include",
        "분사구문의 의미상 주어 the index가 점수를 '사용하는' 능동 → Using",
        "사역동사 let + 목적어 + 동사원형 → see",
        "동사 can be repaired를 꾸미는 부사 → easily",
        "[어휘] 수리 가능성을 따질 때 고려하는 것 → 수리 정보의 '이용 가능성(availability)'",
        "[어휘] 빨간 라벨의 낮은 숫자 ↔ 초록 라벨의 높은 숫자(쉬움) → 수리가 '어려움(difficult)'",
        "뒤에 절(a high number ~ indicates ~) → 대조의 접속사 whereas. despite는 전치사"]),
 '❺': ("The index was designed to have two positive effects. "
       "Firstly, it allows consumers [[making|to make]] informed decisions when purchasing new devices and appliances. "
       "Secondly, it [[discourages|encourages]] manufacturers to make their products easier to repair. "
       "As a result, with [[more|fewer]] electronic and electrical items [[ended|ending]] up in its landfills, France can expect to make a transition to a more sustainable society in the near future. "
       "The impact of the index, however, is likely to spread far [[within|beyond]] France. "
       "We live in a global economy, and any company that [[want|wants]] to sell its appliances on the French market will need to label its products according to the repairability index. "
       "If the index [[will be|is]] successful, we can anticipate [[to see|seeing]] more countries around the world following France's innovative lead.",
       ["allow + 목적어 + to부정사 → to make",
        "[어휘] 두 번째 '긍정적' 효과 → 제조사가 수리하기 쉽게 만들도록 '장려(encourages)'",
        "[어휘] 지속 가능한 사회로의 전환 → 매립지로 가는 물건이 '더 적어짐(fewer)'",
        "with + 목적어 + 분사: 물건들이 매립지에 '이르는' 능동(자동사 end up) → ending",
        "[어휘] however + 세계 경제 이야기 → 영향이 프랑스를 '훨씬 넘어(far beyond)' 퍼짐. far within은 말이 안 돼요",
        "주격 관계대명사 that의 선행사 any company(단수) → wants",
        "조건 부사절(If ~)은 미래라도 현재시제 → is",
        "anticipate + 동명사 → seeing"]),
 '❻': ("When consumers [[give|are given]] the right tools and materials, along with some helpful advice, they can repair much of the damage that [[occur|occurs]] to electronic products by themselves. "
       "That is [[because|why]] Repair Cafés were started. "
       "They are free meeting places [[which|where]] people can gather together and fix their broken devices. "
       "The cafés are staffed by [[paid|volunteer]] experts who can give technical advice and teach people how to fix things. "
       "The first Repair Café was opened in the Netherlands in the city of Amsterdam in 2009. "
       "It was [[so|such]] a success that the idea soon spread to neighboring countries. "
       "Before long, there were Repair Cafés in over 30 countries around the world. "
       "Along with preventing damaged items from [[become|becoming]] e-waste, these cafés also encourage people to share their [[worthless|invaluable]] skills and knowledge about the repair and maintenance of electronics. "
       "They continue to grow in popularity, with more and more people signing up to volunteer. "
       "By providing spaces where people can learn, Repair Cafés enable individuals [[maintaining|to maintain]] their devices and [[shorten|extend]] their life spans. "
       "Furthermore, they foster a sustainable perspective that can have a huge positive impact on our future.",
       ["소비자가 도구를 '받는' 수동 → are given (give A B의 수동)",
        "관계대명사 that의 선행사 the damage(셀 수 없음, 단수) → occurs",
        "앞 문장(스스로 고칠 수 있다)이 원인, 이 문장이 결과 → That is why. That is because는 뒤에 원인이 와요",
        "선행사 places + 완전한 절(people can gather ~) → 관계부사 where",
        "[어휘] 무료 장소 + 뒤 '자원봉사 신청자 증가' → 자원봉사(volunteer) 전문가",
        "such + a + 명사 + that (너무 ~해서 …하다). so는 형용사·부사 앞",
        "prevent A from -ing → becoming",
        "[어휘] 사람들이 '나누도록' 장려하는 기술과 지식 → 매우 귀중한(invaluable). invaluable ≠ 가치 없는!",
        "enable + 목적어 + to부정사 → to maintain",
        "[어휘] 기기를 관리하게 됨 → 수명을 '늘림(extend)'. to maintain과 병렬(to 생략)"]),
 '❼': ("Do you remember Liz, the girl [[which|who]] dropped her laptop? "
       "Imagine she lived in a world where repairing damaged devices and appliances was simply part of [[rare|everyday]] life. "
       "If that [[is|were]] the case, her options wouldn't be limited to [[pay|paying]] for expensive repairs or throwing away her laptop and buying a new one. "
       "She would be able to order the necessary parts online and replace them [[her|herself]]. "
       "Alternatively, she could bring her damaged device to the nearest Repair Café to get advice on how to fix it. "
       "Repairing it probably wouldn't be very hard, as she likely would have purchased a laptop with a [[low|high]] repairability score. "
       "In fact, this sustainable world is a future we can all enjoy if we work toward it together. "
       "Even more importantly, it is a future [[which|in which]] people will generate far [[more|less]] e-waste, [[made|making]] our planet a cleaner, healthier place for everyone.",
       ["선행사 the girl(사람) → 주격 관계대명사 who",
        "[어휘] 수리가 '그저(simply)' 일상의 한 부분 → everyday life. rare(드문)와 simply는 어울리지 않아요",
        "주절 wouldn't be ~ → 가정법 과거: If + 주어 + were",
        "be limited to의 to는 전치사 → 동명사 paying (throwing, buying과 병렬)",
        "주어 She가 '직접' — 강조의 재귀대명사 herself",
        "[어휘] 수리가 어렵지 않았을 이유 → 수리 가능성 점수가 '높은(high)' 노트북",
        "뒤가 완전한 절(people will generate ~) → 전치사 + 관계대명사 in which (= where)",
        "[어휘] 더 깨끗하고 건강한 지구 → 전자 쓰레기를 '훨씬 적게(far less)'",
        "콤마 뒤 결과의 분사구문, 능동(목적어 our planet) → making"]),
}
path = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/proj/data/h2-ne-oh-L3.js'
PK = json.loads(subprocess.check_output(['node', '-e', "global.window={};require('%s');process.stdout.write(JSON.stringify(window.PKG))" % path]))
base = [d for d in PK['days'] if not re.match(r'k\d$', d['id'])]
BODY = [d for d in base if re.match(r'p\d$', d['id'])]
KO = {}
for d in BODY:
    for l in d['passage']:
        if l[0] != '#' and l[2]: KO[l[1]] = l[2]

def sec_passage(secs):
    out = []
    for d in BODY:
        on = False
        for l in d['passage']:
            if not l[0] and len(l[1]) == 1 and not l[2]: on = l[1] in secs
            if on: out.append(l)
    return out

def mkday(did, secs, rng):
    scr = []
    for s in secs:
        for c in CH[s]:
            en = c.replace(' / ', ' ')
            assert en in KO, (s, en)
            if len(c.split(' / ')) >= 4: scr.append({'ko': KO[en], 'en': en, 'chunks': c.split(' / ')})
    hunt = []
    for s in secs:
        txt, why = HUNT[s]
        fixed = re.sub(r'\[\[([^|\]]*)\|([^\]]*)\]\]', r'\2', txt)
        want = ' '.join(c.replace(' / ', ' ') for c in CH[s])
        assert fixed == want, (s, [(a, b) for a, b in zip(fixed.split(), want.split()) if a != b][:3])
        n = len(re.findall(r'\[\[', txt)); assert n == len(why), (s, n, len(why))
        hunt.append({'label': '본문 ' + s, 's': txt, 'why': why})
    return {'id': did, 'name': 'DAY', 'range': '4과 본문 완전정복 ' + rng, 'story': '주요문장 덩어리 배열 → 틀린 곳 ' + '·'.join(str(len(HUNT[s][1])) + '개' for s in secs) + ' 찾아 고치기 (어법 + 문맥 어휘)',
            'passage': sec_passage(secs), 'steps': [
        {'type': 'scramble', 'title': '주요문장 덩어리 스크램블', 'guide': '우리말을 보고 잘게 나뉜 의미 덩어리를 순서대로 눌러 문장 전체를 완성하세요.', 'items': scr},
        {'type': 'hunt', 'title': '오류 사냥 · 틀린 곳 찾아 고치기', 'guide': '단락에서 틀린 곳을 정해진 개수만큼 찾고(1점), 바르게 고쳐 쓰세요(1점). 어법뿐 아니라 문맥에 맞지 않는 낱말도 있어요.', 'items': hunt}]}

# 본문 전 문장이 CH에 다 들어갔는지 (소제목 줄 제외)
allen = [l[1] for d in BODY for l in d['passage'] if l[0] != '#' and l[2]]
used = {c.replace(' / ', ' ') for v in CH.values() for c in v}
missing = [e for e in allen if e not in used and len(e.split()) > 4 and e[-1] in '.?!:']  # 소제목 줄(마침표 없음) 제외
assert not missing, missing

NEW = [mkday('k1', ['❶', '❷', '❸'], '❶❷❸'), mkday('k2', ['❹', '❺'], '❹❺'), mkday('k3', ['❻', '❼'], '❻❼')]
k = max(i for i, d in enumerate(base) if re.match(r'p\d$', d['id']))
PK['days'] = base[:k + 1] + NEW + base[k + 1:]
for i, d in enumerate(PK['days']): d['name'] = 'DAY %d' % (i + 1)
src = open(path, encoding='utf-8').read(); head = src[:src.index('window.PKG')]
tail = src[src.index('/* WRAPUP-TESTS'):] if '/* WRAPUP-TESTS' in src else ''
if '4과 본문 완전정복' not in head: head = head.rstrip('\n') + '\n/* 11/11: 4과 본문 완전정복 k1~k3 gen/gen_h2oh4full.py (4과 본문 DAY p1~p4 다음) */\n'
PK.pop('tests', None)
write(PK, path, head)
if tail: open(path, 'a', encoding='utf-8').write(tail)
print('ok', [(d['name'], d['range'], [len(s['items']) for s in d['steps']]) for d in PK['days']])
