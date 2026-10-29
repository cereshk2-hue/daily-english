import sys
sys.path.insert(0, '.')
from wcommon import *
# 중산고 1 · 2025년 9월 고1 학평 23·24번 Wrap-up 20문항 (10/29)
U = lambda x: '<u>' + x + '</u>'
TG = lambda t, x: '<span class="tag">(%s)</span><u>%s</u>' % (t, x)
CN = lambda n, x: '%s<u>%s</u>' % ('①②③④⑤'[n - 1], x)
GP = lambda n: ' <span class="gap">( %s )</span> ' % '①②③④⑤'[n - 1]

A1 = "For many centuries, humans have taken advantage of tools that translate and bring into our perception natural phenomena that we can't perceive with our senses."
A2 = "In some cases, this consists of simply amplifying signals that feed into our normal sensory inputs (e.g., telescopes can bring into clear view that which is too far away for our eyes to perceive on their own)."
A3 = "Other instruments turn signals that we cannot perceive into ones that we can observe."
A4 = "Some of these take the form of expanding the reach of our current senses, such as creating visible images based on the ultraviolet spectrum of light or changing sounds that are normally outside the range of what human ears can hear into audible signals."
A5 = "Alternatively, some instruments measure properties for which we have no sensory capacity at all and change them into that which we can observe."
P23 = ' '.join([A1, A2, A3, A4, A5])

B1 = "Many opponents of animal experimentation argue that not only is modern medicine not the only cause for the decline in mortality, many medical advances that did contribute to human health were not the result of animal experimentation."
B2 = "Defenders of research have claimed that since there is a strong correlation between the practice of animal experimentation and medical advancement, the former caused the latter."
B3 = "Opponents of research reject this inference."
B4 = "After all, we have independent reasons to expect these phenomena to be correlated."
B5 = "Since the law prescribes that all new drugs, prosthetic devices, and surgical techniques be tried on animals before they are used in humans, we will subsequently find that all medical advances are correlated with prior experimentation on animals."
B6 = "Consequently, the correlation between animal experimentation and medical discovery is the result of legal necessity, not evidence that animal experimentation led to medical advances."
B7 = "Moreover, several influential physicians have offered historical evidence that animal experimentation has not been as responsible for biomedical discovery as defenders suggest."
B8 = "They claim that clinical discoveries played a more substantial role than animal researchers have led us to believe."
P24 = ' '.join([B1, B2, B3, B4, B5, B6, B7, B8])

qs, ans, E = [], [], []
def add(stem, body, a, e): qs.append(Q(len(qs) + 1, stem, body)); ans.append(a); E.append(e)

# ── 23번 ──
add('다음 글의 주제로 가장 적절한 것은?' + src('23번'), BOX(P23) + '\n' + OL([
    'difficulties in replacing human senses with tools',
    'human senses that inspire the inventing of scientific tools',
    'differences between visual and auditory senses in humans',
    'the tools that increase the ability of human senses',
    'the power of human imagination in discovering the universe']), '④',
    '감각으로 지각할 수 없는 현상을 도구가 확장(amplify)하거나 변환(turn into)해 지각하게 해 준다 → 인간 감각의 능력을 높이는 도구. ① 대체의 어려움 언급 없음 ② 감각이 발명에 영감을 줬다는 내용 아님 ③ 시각·청각의 차이 비교 아님 ⑤ 상상력 아님')
add('23번 글의 내용과 일치하는 것은?' + src('23번'), OL([
    'Telescopes turn signals that our eyes can never receive into visible images.',
    'All instruments function by magnifying signals that already reach our senses.',
    'Some devices transform sounds beyond the range of human hearing into ones we can hear.',
    'Instruments measuring properties we cannot sense present the results in their original, imperceptible form.',
    'Such tools have been used by humans for only a few decades.']), '③',
    '③ 들을 수 있는 범위 밖(outside the range)의 소리를 들을 수 있는(audible) 신호로 바꾼다. ① 망원경은 눈으로 들어오는 신호를 단순히 확장(amplifying)하는 경우 → 받을 수 없는 신호를 바꾸는 게 아님 ② In some cases(일부 경우)일 뿐, 다른 도구는 신호를 변환함 ④ 감지 능력이 없는 속성도 측정해서 관찰할 수 있는 것으로 바꾼다(change them into that which we can observe) ⑤ for many centuries(수 세기)')
add('다음 글의 밑줄 친 부분 중, 문맥상 낱말의 쓰임이 적절하지 <u>않은</u> 것은?' + src('23번 변형'), BOX(
    A1 + " In some cases, this consists of simply " + CN(1, 'amplifying') + " signals that feed into our normal sensory inputs (e.g., telescopes can bring into clear view that which is " + CN(2, 'too far away') + " for our eyes to perceive on their own). Other instruments turn signals that we " + CN(3, 'cannot perceive') + " into ones that we can observe. Some of these take the form of " + CN(4, 'expanding') + " the reach of our current senses, such as creating visible images based on the ultraviolet spectrum of light or changing sounds that are normally " + CN(5, 'within') + " the range of what human ears can hear into audible signals. " + A5) + '\n' + OL(['amplifying', 'too far away', 'cannot perceive', 'expanding', 'within']), '⑤',
    '원래 들을 수 있는 범위 \'안(within)\'의 소리를 들을 수 있는 신호로 바꾼다는 건 말이 안 된다 → 범위 <i>밖(outside)</i>의 소리. ① 일반 감각 신호를 확장 ② 눈으로 보기엔 너무 먼 것 ③ 지각할 수 없는 신호를 관찰 가능한 신호로 ④ 현재 감각의 범위를 넓힘')
add('다음 글의 밑줄 친 (a)~(g) 중 어법상 <u>틀린</u> 것의 개수는?' + src('23번 변형'), BOX(
    "For many centuries, humans have " + TG('a', 'taken') + " advantage of tools that translate and bring into our perception natural phenomena " + TG('b', 'what') + " we can't perceive with our senses. In some cases, this consists of simply " + TG('c', 'amplifying') + " signals that feed into our normal sensory inputs (e.g., telescopes can bring into clear view that which " + TG('d', 'are') + " too far away for our eyes to perceive on their own). Other instruments turn signals that we cannot perceive into " + TG('e', 'ones') + " that we can observe. Some of these take the form of expanding the reach of our current senses, such as creating visible images based on the ultraviolet spectrum of light or " + TG('f', 'change') + " sounds that are normally outside the range of what human ears can hear into audible signals. Alternatively, some instruments measure properties " + TG('g', 'for which') + " we have no sensory capacity at all and change them into that which we can observe.") + '\n' + OL(['1개', '2개', '3개', '4개', '5개'], False), '③',
    '틀린 것 (b) (d) (f) 3개. (b) 선행사 natural phenomena가 있으므로 → <i>that</i>(what은 선행사 포함) (d) that which(= what, ~하는 것)는 단수 취급 → <i>is</i> (f) such as 뒤 creating과 or로 병렬 → <i>changing</i>. (a) have taken advantage of 현재완료 (c) consist of + 동명사 (e) ones = signals (g) have no capacity for properties → for which')
add('다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 적절한 것은?' + src('23번'), BOX(P23) + '\n' + SUM(
    'Instruments help us perceive nature either by <b>(A)</b> <span class="blank"></span> signals our senses can already receive or by <b>(B)</b> <span class="blank"></span> imperceptible signals into forms we can observe.') + '\n' + TB(['(A)', '(B)'], [
    ['strengthening', 'converting'], ['weakening', 'converting'], ['strengthening', 'erasing'], ['recording', 'ignoring'], ['filtering', 'hiding']]), '①',
    '(A) 일반 감각으로 들어오는 신호를 단순히 확장(amplifying) → <i>strengthening</i> 강화하다 (B) 지각할 수 없는 신호를 관찰할 수 있는 것으로 바꿈(turn into, change into) → <i>converting</i> 변환하다')
add('다음 문장의 밑줄 친 <i>ones</i>가 가리키는 것으로 가장 적절한 것은?' + src('23번'), BOX(
    "Other instruments turn signals that we cannot perceive into " + U('ones') + " that we can observe.") + '\n' + OL(['tools', 'instruments', 'senses', 'images', 'signals']), '⑤',
    'turn A into B: A를 B로 바꾸다. 지각할 수 없는 신호(signals)를 관찰할 수 있는 신호로 → ones = <i>signals</i>. 앞에 나온 복수 명사를 반복하지 않으려고 ones를 쓴다.')
add('글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳은?' + src('23번'), GIV(A2) + '\n' + BOX(
    GP(1).strip() + ' ' + A1 + GP(2) + A3 + GP(3) + A4 + GP(4) + A5 + GP(5).rstrip()), '②',
    '주어진 문장의 this = \'감각으로 지각할 수 없는 현상을 도구로 지각하는 것\'(첫 문장). In some cases(어떤 경우에는) 단순 확장 → Other instruments(다른 도구들은) 변환으로 이어진다. ③에 넣으면 Other instruments와 Some of these(= 그 도구들 중 일부) 사이가 끊긴다.')
add('주어진 글 다음에 이어질 글의 순서로 가장 적절한 것은?' + src('23번'), GIV(A1) + '\n' + BOX(
    '<b>(A)</b> ' + A5 + '</p><p><b>(B)</b> ' + A2 + '</p><p><b>(C)</b> ' + A3 + ' ' + A4) + '\n' + ORD(), '③',
    '(B) In some cases 단순 확장(망원경) → (C) Other instruments 변환, 그중 일부(Some of these)는 현재 감각의 범위를 넓힘 → (A) Alternatively(또는) 감지 능력이 전혀 없는 속성을 측정해 관찰 가능하게.')

# ── 24번 ──
add('다음 글의 제목으로 가장 적절한 것은?' + src('24번'), BOX(P24) + '\n' + OL([
    'Is Medicine Advanced by Experimenting on Animals?',
    'Biomedicine: Unlocking New Frontiers in Health Care',
    'Refer to Historical Evidence to Solve Medical Issues',
    "Why Aren't There Strict Laws for Animal Adoption?",
    'Medical Advances for Extending Human Life Span']), '①',
    '동물 실험이 의학 발전을 이끌었다는 옹호자들의 주장(상관관계 → 인과)을 반대자들이 반박하는 글 → 의학은 동물 실험으로 발전하는가? ③ 역사적 증거는 반대자 근거의 일부일 뿐 ④ 동물 입양 법 아님')
add('24번 글의 내용과 일치하지 <u>않는</u> 것은?' + src('24번'), OL([
    'Opponents maintain that factors other than modern medicine also lowered death rates.',
    'Opponents hold that some health-improving advances owed nothing to animal testing.',
    'Defenders treat a statistical association as evidence of a causal link.',
    'The law requires prosthetic devices to be tested on animals before human use.',
    'Influential physicians argue that clinical findings were less significant than animal researchers claim.']), '⑤',
    '의사들은 임상적 발견이 동물 연구자들이 믿게 한 것보다 \'더 상당한(more substantial)\' 역할을 했다고 주장 → less significant는 반대. ① not the only cause for the decline in mortality ② were not the result of animal experimentation ③ correlation → the former caused the latter ④ prosthetic devices도 동물에게 먼저 시험')
add('다음 글의 밑줄 친 부분 중, 문맥상 낱말의 쓰임이 적절하지 <u>않은</u> 것은?' + src('24번 변형'), BOX(
    "Many opponents of animal experimentation argue that not only is modern medicine not the only cause for the " + CN(1, 'decline') + " in mortality, many medical advances that did " + CN(2, 'contribute') + " to human health were not the result of animal experimentation. Defenders of research have claimed that since there is a " + CN(3, 'strong') + " correlation between the practice of animal experimentation and medical advancement, the former caused the latter. Opponents of research " + CN(4, 'accept') + " this inference. After all, we have independent reasons to expect these phenomena to be correlated. " + B5 + " " + B6 + " " + B7 + " They claim that clinical discoveries played a more " + CN(5, 'substantial') + " role than animal researchers have led us to believe.") + '\n' + OL(['decline', 'contribute', 'strong', 'accept', 'substantial']), '④',
    '바로 뒤에서 상관관계가 생기는 \'별개의 이유\'(법적 의무)를 들어 반박 → 추론을 받아들이는(accept) 게 아니라 <i>거부한다(reject)</i>. ① 사망률 감소 ② 건강에 기여 ③ 강한 상관관계 ⑤ 더 상당한 역할')
add('다음 글의 밑줄 친 (a)~(e) 중 어법상 <u>틀린</u> 것끼리 짝지은 것은?' + src('24번 변형'), BOX(
    "Many opponents of animal experimentation argue that not only " + TG('a', 'is modern medicine') + " not the only cause for the decline in mortality, many medical advances that " + TG('b', 'did contributed') + " to human health were not the result of animal experimentation. Defenders of research have claimed that since " + TG('c', 'there is') + " a strong correlation between the practice of animal experimentation and medical advancement, the former caused the latter. … Since the law prescribes that all new drugs, prosthetic devices, and surgical techniques " + TG('d', 'be tried') + " on animals before they are used in humans, we will subsequently find that all medical advances are correlated with prior experimentation on animals. … They claim that clinical discoveries played a more substantial role than animal researchers have led us " + TG('e', 'believing') + ".") + '\n' + OL(['(a), (c)', '(a), (d)', '(b), (d)', '(b), (e)', '(c), (e)'], False), '④',
    '(b) 강조의 조동사 did 뒤에는 동사원형 → <i>did contribute</i> (e) lead + 목적어 + to부정사(~하게 하다) → <i>to believe</i>. (a) not only가 문장(절) 앞에 오면 의문문 어순 도치 → is modern medicine ✔ (c) there is + 단수 명사 a strong correlation ✔ (d) prescribe(규정하다) that S (should) 동사원형 → be tried ✔')
add('다음 빈칸에 들어갈 말로 가장 적절한 것은?' + src('24번 변형'), BOX(
    B2 + " " + B3 + " " + B4 + " " + B5 + ' Consequently, the correlation between animal experimentation and medical discovery is the result of <span class="blank"></span>, not evidence that animal experimentation led to medical advances.') + '\n' + OL([
    'requirements imposed by law', 'careful clinical observation', 'growing public demand', 'competition among drug companies', 'mere chance and coincidence']), '①',
    '모든 신약·보철 장치·수술 기법은 사람에게 쓰기 전에 동물에게 시험하도록 법이 규정(prescribes) → 상관관계는 법이 요구한 결과 = legal necessity. ⑤ 우연이 아니라 \'예상할 별개의 이유(법)\'가 있다고 했다.')
add('다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 적절한 것은?' + src('24번'), BOX(
    B2 + " " + B3 + " " + B4 + " " + B5 + " " + B6) + '\n' + SUM(
    'Opponents claim that the link between animal testing and medical progress is <b>(A)</b> <span class="blank"></span> by law, so it is not <b>(B)</b> <span class="blank"></span> that the testing caused the progress.') + '\n' + TB(['(A)', '(B)'], [
    ['prohibited', 'proof'], ['required', 'doubt'], ['explained', 'denial'], ['required', 'proof'], ['ignored', 'evidence']]), '④',
    '(A) 법이 동물 실험을 의무화(prescribes) → 연결은 법이 <i>요구한(required)</i> 것 (B) 그러므로 동물 실험이 발전을 일으켰다는 <i>증거(proof)</i>가 아니다(not evidence that …). ② doubt는 \'의심이 아니다\' = 확실하다가 되어 반대')
add('밑줄 친 <i>the former</i>와 <i>the latter</i>가 가리키는 것을 바르게 짝지은 것은?' + src('24번'), BOX(
    "Defenders of research have claimed that since there is a strong correlation between the practice of animal experimentation and medical advancement, " + U('the former') + " caused " + U('the latter') + ".") + '\n' + TB(['the former', 'the latter'], [
    ['animal experimentation', 'medical advancement'], ['medical advancement', 'animal experimentation'], ['modern medicine', 'the decline in mortality'], ['defenders', 'opponents'], ['correlation', 'causation']]), '①',
    'between A and B에서 the former(전자) = A = the practice of animal experimentation, the latter(후자) = B = medical advancement → 동물 실험이 의학 발전을 일으켰다(옹호자의 주장).')
add('다음 글에서 전체 흐름과 관계 <u>없는</u> 문장은?' + src('24번 변형'), BOX(
    B2 + ' ① ' + B3 + ' ② ' + B4 + ' ③ Animal rights groups have also organized protests to raise public awareness of the conditions in laboratories. ④ ' + B5 + ' ⑤ ' + B6), '③',
    '상관관계가 법적 필요성 때문에 생긴다는 논리 전개 중에 동물 권리 단체의 시위 이야기는 관계없다. ② 별개의 이유가 있다 → ④ 그 이유 = 법 → ⑤ 따라서 상관관계는 법의 결과')
add('글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳은?' + src('24번'), GIV(B3) + '\n' + BOX(
    B1 + GP(1) + B2 + GP(2) + B4 + GP(3) + B5 + GP(4) + B6 + GP(5) + B7 + ' ' + B8), '②',
    'this inference(이 추론) = 옹호자들의 \'상관관계가 있으니 동물 실험이 발전을 일으켰다\'. 그 바로 뒤에서 거부하고, After all(결국 ~이니까)로 거부하는 이유(별개의 이유 = 법)가 이어진다. ①에는 아직 추론이 나오지 않았다.')
add('주어진 글 다음에 이어질 글의 순서로 가장 적절한 것은?' + src('24번'), GIV(B2) + '\n' + BOX(
    '<b>(A)</b> ' + B5 + '</p><p><b>(B)</b> ' + B3 + ' ' + B4 + '</p><p><b>(C)</b> ' + B6) + '\n' + ORD(), '②',
    '(B) 반대자들은 이 추론을 거부, 상관관계를 예상할 별개의 이유가 있다 → (A) 그 이유: 법이 동물 실험을 먼저 하도록 규정 → (C) 따라서(Consequently) 상관관계는 법적 필요성의 결과.')
add('24번 글에서 동물 실험 반대자들의 주장으로 가장 적절한 것은?' + src('24번'), OL([
    '동물 실험은 법으로 금지되어야 하므로 의학 발전과 관계가 없다.',
    '동물 실험과 의학 발전 사이에는 아무런 상관관계도 없다.',
    '임상적 발견은 동물 실험보다 의학 발전에 덜 기여했다.',
    '현대 의학은 사망률이 낮아진 유일한 원인이다.',
    '법이 신약 등을 먼저 동물에게 시험하게 하므로 둘의 상관관계는 당연하고, 인과의 증거가 되지 못한다.'], False), '⑤',
    '상관관계는 인정하되(①② ✗), 그것은 법적 필요성의 결과일 뿐 동물 실험이 발전을 이끈 증거는 아니라는 것. ① 금지 주장은 없음 ③ 임상적 발견이 더 상당한 역할 ④ not the only cause(유일한 원인이 아님)')

# ── 종합 ──
add('23·24번 지문에 나온 단어와 영영풀이가 바르게 짝지어지지 <u>않은</u> 것은?' + src('종합'), OL([
    '<b>perceive</b> : to notice or become aware of something through the senses',
    '<b>mortality</b> : the state of being able to live forever',
    '<b>amplify</b> : to make a sound or signal stronger',
    '<b>audible</b> : loud enough to be heard',
    '<b>prescribe</b> : to state officially what must be done']), '②',
    'mortality는 \'죽음을 피할 수 없음, 사망률\' (the decline in mortality 사망률 감소). 영원히 사는 것은 immortality. ① 지각하다 ③ 확장하다·증폭하다 ④ 들을 수 있는 ⑤ 규정하다')

from collections import Counter
assert len(qs) == 20 and len(ans) == 20 and len(E) == 20
print(Counter(ans), ''.join(ans))
key = '<div class="keygrid">\n    ' + ''.join('<div>%d<b>%s</b></div>' % (k + 1, a) for k, a in enumerate(ans[:10])) + '\n    ' + ''.join('<div>%d<b>%s</b></div>' % (k + 11, a) for k, a in enumerate(ans[10:])) + '\n  </div>\n  <div class="exp">\n' + ''.join('    <p><b>%d</b> <span class="k">%s</span> %s</p>\n' % (k + 1, ans[k], e) for k, e in enumerate(E)) + '  </div>'
html = ('<title>9월 학평 23·24 Wrap-up</title>\n<meta name="claude:viewport-fit-sides" content="cover">\n' + fonts + css + '''

<main>
<section class="page">
  <div class="top"><span>2025학년도 9월 고1 전국연합학력평가 · <b>23·24번 Wrap-up</b></span><span>중산고등학교 1학년 · 내신 대비</span></div>
  <div class="title">
    <div class="g">영어</div>
    <h1>9월 학평 23·24 Wrap-up<small>심화 · 내용 일치 변형 포함</small></h1>
    <div class="when">20문항 · 각 5점<br>제한 시간 30분</div>
  </div>
  <div class="idrow"><div>반</div><div>번호</div><div>이름</div><div>점수 &nbsp;&nbsp;&nbsp; / 100</div></div>
  <p class="notice">범위: 23번(감각을 넓혀 주는 도구) · 24번(동물 실험과 의학 발전). 지문은 원문을 일부 바꾼 것이 있어요. 내용 일치 문항의 선택지는 본문 표현을 다른 어휘로 바꿔 썼으니 뜻을 정확히 따져 보세요.</p>

  <div class="qs">''' + ''.join(qs) + '''  </div>
  <div class="foot"><span>2025년 9월 고1 학평 23·24번 · 원문 일부 변형</span><span>중산고 1학년 영어 · Wrap-up</span></div>
</section>

<section class="page">
  <div class="top"><span>9월 학평 23·24 Wrap-up · <b>정답과 해설</b></span><span>중산고등학교 1학년</span></div>
  <div class="title"><div class="g">영어</div><h1>정답과 해설</h1><div class="when">각 5점 · 100점</div></div>
  ''' + key + '''
  <div class="foot"><span>정답 분포 ①~⑤ 각 4개</span><span>중산고 1학년 영어 · Wrap-up</span></div>
</section>
</main>
''')
open('wrapup-2509-2324.html', 'w', encoding='utf-8').write(html)
