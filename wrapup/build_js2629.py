import sys
sys.path.insert(0, '.')
from wcommon import *
# 중산고 1 · 2025년 9월 고1 학평 26·29번 Wrap-up 20문항 (10/31) · 선택지는 본문을 다른(조금 더 어려운) 어휘로 바꿔 씀
U = lambda x: '<u>' + x + '</u>'
TG = lambda t, x: '<span class="tag">(%s)</span><u>%s</u>' % (t, x)
CN = lambda n, x: '%s<u>%s</u>' % ('①②③④⑤'[n - 1], x)
GP = lambda n: ' <span class="gap">( %s )</span> ' % '①②③④⑤'[n - 1]

R1 = "Roger Payne was born in Manhattan in 1935."
R2 = "He studied biology at Harvard University and eventually earned his Ph.D. from Cornell University in 1961."
R3 = "In 1967, he discovered that humpback whales make long and complex sounds."
R4 = "They're known as “whale songs,” and he showed that whales use them to communicate."
R5 = "Then in 1970, he released an album <i>Songs of the Humpback Whale</i>, which became a surprise hit and helped start the global “Save the Whales” movement."
R6 = "The following year, he founded Ocean Alliance to protect whales and the earth's oceans, and he used new, safe methods to study whales without harming them."
R7 = "Over his career, he led more than 100 research trips worldwide, including the Voyage of the Odyssey from 2000 to 2005, which studied ocean pollution."
R8 = "His work helped make laws that protect marine mammals, which finally led to the global ban on commercial whaling in 1986."
P26 = ' '.join([R1, R2, R3, R4, R5, R6, R7, R8])

G1 = "Big mammalian herbivore species react to danger from predators or humans in different ways."
G2 = "Some species are nervous, fast, and programmed for instant flight when they perceive a threat."
G3 = "Other species are slower, less nervous, seek protection in herds, stand their ground when threatened, and don't run until necessary."
G4 = "Naturally, the nervous species are difficult to keep in captivity."
G5 = "If put into an enclosure, they are likely to panic, and either die of shock or hit themselves repeatedly to death against the fence in their attempts to escape."
G6 = "That's true, for example, of gazelles, which for thousands of years were the most frequently hunted game species in some parts of the Fertile Crescent."
G7 = "There is no mammal species that the first settled peoples of that area had more opportunity to domesticate than gazelles."
G8 = "But no gazelle species has ever been domesticated."
G9 = "Just imagine trying to herd an animal that runs away, blindly hits itself against walls, can leap up to nearly 30 feet, and can run at a speed of 50 miles per hour!"
P29 = ' '.join([G1, G2, G3, G4, G5, G6, G7, G8, G9])

qs, ans, E = [], [], []
def add(stem, body, a, e): qs.append(Q(len(qs) + 1, stem, body)); ans.append(a); E.append(e)

# ── 26번 ──
add('다음 글의 내용과 일치하지 <u>않는</u> 것은?' + src('26번'), BOX(P26) + '\n' + OL([
    'Payne obtained his doctorate in his mid-twenties.',
    'Payne found that humpback whales produce lengthy, intricate sounds.',
    "Payne's record achieved unexpected commercial success.",
    'Payne established Ocean Alliance in the same year his album came out.',
    'Payne relied on non-invasive techniques to study whales.']), '④',
    '앨범은 1970년, Ocean Alliance는 그다음 해(The following year = 1971)에 설립 → 같은 해(the same year)가 아니다. ① 1935년생, 1961년 박사 → 26세 = mid-twenties(20대 중반) ✔ doctorate = Ph.D. ② lengthy = long, intricate = complex ✔ ③ unexpected commercial success = a surprise hit ✔ ④ establish = found(설립하다) ⑤ non-invasive(몸에 해를 주지 않는) = safe methods ~ without harming them ✔')
add('26번 글의 내용과 일치하는 것은?' + src('26번'), OL([
    'Payne completed his undergraduate studies in biology at Cornell.',
    'The Voyage of the Odyssey lasted roughly half a decade and examined marine contamination.',
    'Payne headed fewer than a hundred research expeditions in total.',
    'His research brought about an immediate worldwide ban on whaling in 1970.',
    'The “Save the Whales” movement had already been under way before his album was released.']), '②',
    '② 2000~2005년 = 약 5년(roughly half a decade), ocean pollution = marine contamination(해양 오염) ✔. ① 생물학은 하버드(Harvard)에서 공부, 코넬은 박사 학위 ③ more than 100(100회 넘게) ↔ fewer than a hundred ④ 포경 금지는 1986년, 그것도 finally(마침내) → immediate(즉각적인) ✗ ⑤ 앨범이 운동을 시작하는 데 도움(helped start) → 이미 진행 중(already under way)이 아니었다')
add('다음 글의 밑줄 친 부분 중, 문맥상 낱말의 쓰임이 적절하지 <u>않은</u> 것은?' + src('26번 변형'), BOX(
    R1 + ' ' + R2 + " In 1967, he discovered that humpback whales make long and " + CN(1, 'complex') + " sounds. They're known as “whale songs,” and he showed that whales use them to " + CN(2, 'communicate') + ". Then in 1970, he released an album <i>Songs of the Humpback Whale</i>, which became a " + CN(3, 'surprise') + " hit and helped start the global “Save the Whales” movement. The following year, he founded Ocean Alliance to protect whales and the earth's oceans, and he used new, safe methods to study whales without " + CN(4, 'harming') + " them. " + R7 + " His work helped make laws that protect marine mammals, which finally led to the global " + CN(5, 'approval') + " of commercial whaling in 1986.") + '\n' + OL(['complex', 'communicate', 'surprise', 'harming', 'approval']), '⑤',
    '해양 포유류를 보호하는 법(laws that protect marine mammals)이 이어진 결과는 상업적 포경의 \'승인(approval)\'이 아니라 <i>금지(ban)</i>. ① 길고 복잡한 소리 ② 의사소통하기 위해 ③ 뜻밖의(surprise) 히트작 ④ 해를 끼치지 않고(without harming) → 안전한 방법')
add('다음 글의 밑줄 친 (a)~(g) 중 어법상 <u>틀린</u> 것의 개수는?' + src('26번 변형'), BOX(
    "Roger Payne " + TG('a', 'was born') + " in Manhattan in 1935. " + R2 + " In 1967, he discovered " + TG('b', 'what') + " humpback whales make long and complex sounds. They're known as “whale songs,” and he showed that whales use them " + TG('c', 'to communicate') + ". Then in 1970, he released an album <i>Songs of the Humpback Whale</i>, " + TG('d', 'which') + " became a surprise hit and helped " + TG('e', 'starting') + " the global “Save the Whales” movement. The following year, he founded Ocean Alliance to protect whales and the earth's oceans, and he used new, safe methods to study whales without " + TG('f', 'harming') + " them. " + R7 + " His work helped make laws that " + TG('g', 'protects') + " marine mammals, which finally led to the global ban on commercial whaling in 1986.") + '\n' + OL(['1개', '2개', '3개', '4개', '5개'], False), '③',
    '틀린 것 (b) (e) (g) 3개. (b) 뒤에 완전한 절(humpback whales make ~ sounds)이 오므로 명사절 접속사 <i>that</i> (what 뒤에는 불완전한 절) (e) help + (to)동사원형 → <i>start</i> (g) 선행사 laws(복수) → <i>protect</i>. (a) 태어나다 be born ✔ (c) 목적(~하기 위해) to부정사 ✔ (d) 콤마 뒤 계속적 용법 which ✔ (f) 전치사 without + 동명사 ✔')
add('다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 적절한 것은?' + src('26번'), BOX(P26) + '\n' + SUM(
    'Roger Payne, who <b>(A)</b> <span class="blank"></span> that humpback whales communicate through songs, devoted his career to <b>(B)</b> <span class="blank"></span> whales and the oceans.') + '\n' + TB(['(A)', '(B)'], [
    ['demonstrated', 'safeguarding'], ['disproved', 'safeguarding'], ['demonstrated', 'exploiting'], ['doubted', 'hunting'], ['assumed', 'commercializing']]), '①',
    '(A) 고래가 노래로 의사소통한다는 것을 보여 주었다(showed) → <i>demonstrated</i> 입증했다 (B) 고래와 바다를 보호(protect)하는 데 일생을 바침 → <i>safeguarding</i> 보호하는. 오답: disproved 틀렸음을 증명하다 · doubted 의심했다 · assumed 추정했다(직접 보여 준 것과 다름) · exploiting 착취하는 · commercializing 상업화하는')
add('다음 빈칸에 들어갈 말로 가장 적절한 것은?' + src('26번 변형'), BOX(
    R3 + ' ' + R4 + ' Then in 1970, he released an album <i>Songs of the Humpback Whale</i>, which became a surprise hit and <span class="blank"></span>. ' + R6) + '\n' + OL([
    'financed his doctoral research at Cornell',
    'prompted a ban on recording whale sounds',
    'served as a catalyst for a worldwide conservation movement',
    'convinced scientists that whales cannot communicate',
    'replaced field research on whales altogether']), '③',
    '원문: helped start the global "Save the Whales" movement(전 세계 고래 보호 운동을 시작하는 데 도움을 줌) → <i>served as a catalyst</i>(촉매 역할을 했다) for a worldwide <i>conservation</i>(보호) movement. ① 박사 학위는 1961년, 앨범보다 먼저 ② 녹음 금지 아님 ④ 고래가 의사소통한다는 것을 보여 줌 → 반대 ⑤ 다음 문장에서 계속 연구함')
add('주어진 글 다음에 이어질 글의 순서로 가장 적절한 것은?' + src('26번'), GIV(R1 + ' ' + R2) + '\n' + BOX(
    '<b>(A)</b> ' + R5 + ' ' + R6 + '</p><p><b>(B)</b> ' + R3 + ' ' + R4 + '</p><p><b>(C)</b> ' + R7 + ' ' + R8) + '\n' + ORD(), '②',
    '시간 순서: 1961 박사 → (B) 1967 고래의 노래 발견, They(= long and complex sounds) → (A) Then in 1970 앨범, The following year(1971) Ocean Alliance → (C) Over his career(경력 전반) 100회 넘는 연구 여행, 1986 포경 금지. (A)의 Then이 (B)의 1967 다음임을 보여 준다.')
add('글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳은?' + src('26번'), GIV(R6) + '\n' + BOX(
    R1 + ' ' + R2 + ' ' + R3 + GP(1) + R4 + GP(2) + R5 + GP(3) + R7 + GP(4) + R8 + GP(5).rstrip()), '③',
    'The following year(그다음 해)는 앞 문장의 연도(1970년 앨범) 바로 다음이어야 한다 → 1970 문장 뒤 ③. ①에 넣으면 1968년이 되어 1970년보다 앞이 되고, ④⑤는 2000~2005년·1986년 뒤라 시간이 맞지 않는다.')

# ── 29번 ──
add('다음 글의 밑줄 친 부분 중, 어법상 <u>틀린</u> 것은?' + src('29번 변형'), BOX(
    G1 + " Some species " + CN(1, 'are') + " nervous, fast, and programmed for instant flight when they perceive a threat. Other species are slower, less nervous, seek protection in herds, stand their ground when " + CN(2, 'threatening') + ", and don't run until necessary. Naturally, the nervous species are difficult to keep in captivity. If " + CN(3, 'put') + " into an enclosure, they are likely to panic, and either die of shock or hit " + CN(4, 'themselves') + " repeatedly to death against the fence in their attempts to escape. That's true, for example, of gazelles, " + CN(5, 'which') + " for thousands of years were the most frequently hunted game species in some parts of the Fertile Crescent.") + '\n' + OL(['are', 'threatening', 'put', 'themselves', 'which']), '②',
    'when (they are) threatened: 동물이 \'위협을 받을\' 때 → 수동 의미의 과거분사 <i>threatened</i>. ① 주어 Some species(복수) → are ✔ ③ If (they are) put into ~: 울타리 안에 \'넣어지면\' → 과거분사 put ✔ ④ 주어 they가 자기 자신을 부딪침 → 재귀대명사 themselves ✔ ⑤ 콤마 뒤 계속적 용법, 선행사 gazelles(사물) → which ✔')
add('(A), (B), (C)의 각 네모 안에서 어법에 맞는 표현으로 가장 적절한 것은?' + src('29번'), BOX(
    "Some species are nervous, fast, and <b>(A)</b> [ programmed / programming ] for instant flight when they perceive a threat. Other species are slower, less nervous, <b>(B)</b> [ seek / seeking ] protection in herds, stand their ground when threatened, and don't run until necessary. … There is no mammal species that the first settled peoples of that area had more opportunity to domesticate than gazelles. But no gazelle species <b>(C)</b> [ has / have ] ever been domesticated.") + '\n' + TB(['(A)', '(B)', '(C)'], [
    ['programming', 'seek', 'has'], ['programmed', 'seeking', 'have'], ['programming', 'seeking', 'has'], ['programmed', 'seek', 'have'], ['programmed', 'seek', 'has']]), '⑤',
    '(A) 종이 (본능적으로) 달아나도록 \'프로그램된\' 수동 → <i>programmed</i> (nervous, fast와 함께 are의 보어) (B) are slower, less nervous, seek, stand, don\'t run이 모두 주어 Other species의 동사로 병렬 → <i>seek</i> (C) no + 단수명사 gazelle species(여기서는 \'어떤 가젤 종도\' 단수 취급) → <i>has</i>')
add('29번 글의 주제로 가장 적절한 것은?' + src('29번'), BOX(P29) + '\n' + OL([
    'the innate temperament that rendered gazelles unsuitable for domestication',
    'the reasons ancient peoples hunted gazelles to extinction',
    'the remarkable agility that helped gazelles escape early hunters',
    'the benefits of raising herd animals in fenced enclosures',
    'how herding techniques developed in the Fertile Crescent']), '①',
    '예민한 종은 가두어 기르기 어렵다 → 가젤은 길들일 기회가 가장 많았지만 한 번도 가축화되지 않았다 → 가젤의 타고난(innate) 기질(temperament)이 가축화에 맞지 않게(unsuitable) 만들었다. render + O + 형용사 = ~을 …하게 만들다. ② 멸종 언급 없음 ③ 빠르기는 근거일 뿐, 사냥꾼을 피한 이야기가 아님(실제로 가장 많이 사냥됨) ④ 울타리 사육의 장점 ✗(오히려 죽음) ⑤ 몰이 기술의 발달 아님')
add('29번 글의 내용과 일치하지 <u>않는</u> 것은?' + src('29번'), OL([
    'Some large herbivores take flight the moment they sense danger.',
    'Less skittish species tend to hold their position rather than bolt.',
    'Confined gazelles may fatally injure themselves while trying to break free.',
    'Early settlers in the region had scant opportunity to tame gazelles.',
    'Gazelles are capable of reaching speeds of around 50 miles per hour.']), '④',
    '그 지역 최초 정착민에게 가젤보다 길들일 기회가 더 많았던 포유류는 없다 → 기회가 \'가장 많았다\'. scant(거의 없는) ✗. ① take flight 달아나다 = instant flight, sense = perceive ✔ ② skittish(겁 많은, 예민한) → less skittish = less nervous, hold their position = stand their ground, bolt(달아나다) ✔ ③ confined(갇힌) = put into an enclosure, fatally(치명적으로), break free = escape ✔ ⑤ 시속 50마일 ✔')
add('다음 글의 밑줄 친 부분 중, 문맥상 낱말의 쓰임이 적절하지 <u>않은</u> 것은?' + src('29번 변형'), BOX(
    G1 + " Some species are nervous, fast, and programmed for " + CN(1, 'instant') + " flight when they perceive a threat. Other species are slower, less nervous, seek protection in " + CN(2, 'herds') + ", stand their ground when threatened, and don't run until necessary. Naturally, the nervous species are " + CN(3, 'difficult') + " to keep in captivity. " + G5 + " That's true, for example, of gazelles, which for thousands of years were the most " + CN(4, 'frequently') + " hunted game species in some parts of the Fertile Crescent. There is no mammal species that the first settled peoples of that area had " + CN(5, 'less') + " opportunity to domesticate than gazelles. " + G8 + " " + G9) + '\n' + OL(['instant', 'herds', 'difficult', 'frequently', 'less']), '⑤',
    '수천 년 동안 가장 자주 사냥된 동물 → 정착민이 가장 많이 접한 동물이었는데도(But) 가축화되지 않았다는 대조 → 가젤보다 길들일 기회가 \'더 많았던(more)\' 종은 없다. less로 쓰면 가젤의 기회가 가장 적었다는 뜻이 되어 But과 연결되지 않는다. ① 즉시 달아남 ② 무리 속에서 보호 ③ 예민한 종은 가두어 기르기 어려움 ④ 가장 자주 사냥된')
add('다음 빈칸에 들어갈 말로 가장 적절한 것은?' + src('29번 변형'), BOX(
    G2 + ' ' + G3 + ' Naturally, the nervous species are <span class="blank"></span>. ' + G5) + '\n' + OL([
    'easily tamed by early settlers',
    'ill-suited to life in confinement',
    'rarely hunted for their meat',
    'highly valued as companions',
    'capable of defending their herds']), '②',
    '원문: difficult to keep in captivity(가두어 기르기 어렵다). 뒤 문장에서 울타리에 넣으면 겁에 질려 죽는다 → <i>ill-suited to</i>(~에 맞지 않는) life in <i>confinement</i>(감금, 갇힌 상태). ① 쉽게 길들여짐 → 반대 ③ 가젤은 가장 자주 사냥됨 ④ 반려동물로 귀하게 여김 언급 없음 ⑤ 무리를 지키는 것은 덜 예민한 종의 특징')
add('다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 적절한 것은?' + src('29번'), BOX(P29) + '\n' + SUM(
    'Herbivores that are <b>(A)</b> <span class="blank"></span> and quick to flee, such as gazelles, resist <b>(B)</b> <span class="blank"></span>, even though early settlers had plenty of chances to tame them.') + '\n' + TB(['(A)', '(B)'], [
    ['placid', 'domestication'], ['high-strung', 'predation'], ['high-strung', 'domestication'], ['sluggish', 'extinction'], ['placid', 'hunting']]), '③',
    '(A) nervous(예민한) → <i>high-strung</i> 신경이 과민한 (B) 한 번도 길들여지지 않았다 → <i>domestication</i>(가축화)에 저항한다. 오답: placid 차분한(반대) · sluggish 느린(반대) · predation 포식 · extinction 멸종 · hunting 사냥(가젤은 오히려 가장 많이 사냥됨)')
add('주어진 글 다음에 이어질 글의 순서로 가장 적절한 것은?' + src('29번'), GIV(G1 + ' ' + G2 + ' ' + G3) + '\n' + BOX(
    '<b>(A)</b> ' + G4 + ' ' + G5 + '</p><p><b>(B)</b> ' + G8 + ' ' + G9 + '</p><p><b>(C)</b> ' + G6 + ' ' + G7) + '\n' + ORD(), '①',
    '(A) Naturally, the nervous species(앞에서 말한 예민한 종)는 가두어 기르기 어렵다 → (C) That\'s true of gazelles(예민한 종이 갇히면 죽는다는 것이 가젤에게 해당), 길들일 기회는 가장 많았다 → (B) But 한 번도 가축화되지 않았다, 그런 동물을 몰아 보라고 상상해 보라.')
add('글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳은?' + src('29번'), GIV(G8) + '\n' + BOX(
    G1 + ' ' + G2 + ' ' + G3 + ' ' + G4 + GP(1) + G5 + GP(2) + G6 + GP(3) + G7 + GP(4) + G9 + GP(5).rstrip()), '④',
    'But(그러나)은 \'가젤보다 길들일 기회가 많았던 종은 없다\'(기회가 가장 많았다)와 대조된다 → 그 바로 뒤 ④. 이어서 Just imagine ~이 왜 길들여지지 않았는지를 보여 준다. ③에 넣으면 \'기회가 가장 많았다\'는 문장이 But 다음에 와서 흐름이 거꾸로 된다.')
add('다음 글의 밑줄 친 <i>That</i>이 가리키는 내용으로 가장 적절한 것은?' + src('29번'), BOX(
    G4 + ' ' + G5 + ' ' + U("That") + "'s true, for example, of gazelles, which for thousands of years were the most frequently hunted game species in some parts of the Fertile Crescent.") + '\n' + OL([
    '예민한 종은 울타리에 가두면 겁에 질려 죽을 가능성이 크다는 것',
    '가젤이 비옥한 초승달 지대에서 가장 자주 사냥되었다는 것',
    '덜 예민한 종은 무리 속에서 보호를 구한다는 것',
    '큰 초식동물은 모두 위험에 같은 방식으로 반응한다는 것',
    '가젤은 시속 50마일로 달릴 수 있다는 것'], False), '①',
    'That은 바로 앞 두 문장: 예민한 종은 가두어 기르기 어렵고, 울타리에 넣으면 겁에 질려 충격으로 죽거나 스스로 부딪쳐 죽는다는 것 → 그것이 가젤에게도 사실(true of gazelles). ② That 뒤 which절의 내용 ③ 덜 예민한 종의 특징 ④ 서로 다른 방식(in different ways) ⑤ 마지막 문장의 내용')
add('다음 글의 밑줄 친 (a)~(e) 중 어법상 <u>틀린</u> 것끼리 짝지은 것은?' + src('29번 변형'), BOX(
    "Some species are nervous, fast, and programmed for instant flight when they " + TG('a', 'perceive') + " a threat. Other species are slower, less nervous, seek protection in herds, " + TG('b', 'standing') + " their ground when threatened, and don't run until necessary. Naturally, the nervous species are difficult to keep in captivity. If put into an enclosure, they are likely " + TG('c', 'to panic') + ", and either die of shock or hit themselves repeatedly to death against the fence in their attempts to escape. That's true, for example, of gazelles, which for thousands of years were the most frequently " + TG('d', 'hunting') + " game species in some parts of the Fertile Crescent. There is no mammal species " + TG('e', 'that') + " the first settled peoples of that area had more opportunity to domesticate than gazelles.") + '\n' + OL(['(a), (c)', '(a), (e)', '(b), (c)', '(c), (e)', '(b), (d)'], False), '⑤',
    '(b) are slower, less nervous, seek, stand, don\'t run이 주어 Other species의 동사로 병렬 → <i>stand</i> (d) 가젤이 \'사냥된\' 수동 → 과거분사 <i>hunted</i> (game species를 꾸밈). (a) 주어 they(복수) + perceive ✔ (c) be likely to + 동사원형 ✔ (e) 선행사 mammal species, 뒤에 domesticate의 목적어가 빠진 불완전한 절 → 목적격 관계대명사 that ✔')

# ── 종합 ──
add('26·29번 지문에 나온 단어와 영영풀이가 바르게 짝지어지지 <u>않은</u> 것은?' + src('종합'), OL([
    '<b>domesticate</b> : to tame an animal so that it can live with or be used by people',
    '<b>captivity</b> : the state of being kept in an enclosed space and not allowed to leave',
    '<b>perceive</b> : to notice or become aware of something',
    '<b>herbivore</b> : an animal that feeds mainly on the flesh of other animals',
    '<b>commercial</b> : related to buying and selling things for profit']), '④',
    'herbivore는 \'초식동물\'(an animal that eats only plants). 다른 동물의 고기(flesh)를 먹는 동물은 carnivore(육식동물). ① 길들이다, 가축화하다 ② 감금, 사육 상태 ③ 감지하다, 인식하다 ⑤ 상업적인(commercial whaling 상업적 포경)')

from collections import Counter
assert len(qs) == 20 and len(ans) == 20 and len(E) == 20
c = Counter(ans); print(c, ''.join(ans)); assert all(v == 4 for v in c.values())
key = '<div class="keygrid">\n    ' + ''.join('<div>%d<b>%s</b></div>' % (k + 1, a) for k, a in enumerate(ans[:10])) + '\n    ' + ''.join('<div>%d<b>%s</b></div>' % (k + 11, a) for k, a in enumerate(ans[10:])) + '\n  </div>\n  <div class="exp">\n' + ''.join('    <p><b>%d</b> <span class="k">%s</span> %s</p>\n' % (k + 1, ans[k], e) for k, e in enumerate(E)) + '  </div>'
html = ('<title>9월 학평 26·29 Wrap-up</title>\n<meta name="claude:viewport-fit-sides" content="cover">\n' + fonts + css + '''

<main>
<section class="page">
  <div class="top"><span>2025학년도 9월 고1 전국연합학력평가 · <b>26·29번 Wrap-up</b></span><span>중산고등학교 1학년 · 내신 대비</span></div>
  <div class="title">
    <div class="g">영어</div>
    <h1>9월 학평 26·29 Wrap-up<small>심화 · 어휘 바꿔 쓰기 선택지</small></h1>
    <div class="when">20문항 · 각 5점<br>제한 시간 30분</div>
  </div>
  <div class="idrow"><div>반</div><div>번호</div><div>이름</div><div>점수 &nbsp;&nbsp;&nbsp; / 100</div></div>
  <p class="notice">범위: 26번(Roger Payne과 고래의 노래) · 29번(가젤은 왜 가축이 되지 못했나). 지문은 원문을 일부 바꾼 것이 있어요. 선택지는 본문 표현을 더 어려운 어휘로 바꿔 썼으니, 단어 뜻을 정확히 따져 보세요.</p>

  <div class="qs">''' + ''.join(qs) + '''  </div>
  <div class="foot"><span>2025년 9월 고1 학평 26·29번 · 원문 일부 변형</span><span>중산고 1학년 영어 · Wrap-up</span></div>
</section>

<section class="page">
  <div class="top"><span>9월 학평 26·29 Wrap-up · <b>정답과 해설</b></span><span>중산고등학교 1학년</span></div>
  <div class="title"><div class="g">영어</div><h1>정답과 해설</h1><div class="when">각 5점 · 100점</div></div>
  ''' + key + '''
  <div class="foot"><span>정답 분포 ①~⑤ 각 4개</span><span>중산고 1학년 영어 · Wrap-up</span></div>
</section>
</main>
''')
open('wrapup-2509-2629.html', 'w', encoding='utf-8').write(html)
