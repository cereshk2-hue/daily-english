# 11/12 안곡고2 · 2026년 9월 고2 학평 Wrap-up 3세트 (24·29 / 30·34 / 38·41~42) — wu_ag.py 빌더
from wu_ag import *
OPTS_ORD = ['(A) − (C) − (B)', '(B) − (A) − (C)', '(B) − (C) − (A)', '(C) − (A) − (B)', '(C) − (B) − (A)']
def ABC(given, chunks, seq):
    """chunks = 맞는 순서의 세 덩어리(문장 목록), seq 예 'BAC' = 첫 덩어리가 (B) → 정답 번호 반환"""
    lab = dict(zip(seq, chunks))
    body = GIV(given) + '\n' + BOX('</p><p>'.join('<b>(%s)</b> %s' % (L, ' '.join(lab[L])) for L in 'ABC'))
    return body, OPTS_ORD.index(' − '.join('(%s)' % L for L in seq)) + 1
def INS(given_idx, sents):
    """sents 중 given_idx 문장을 빼고, 첫 문장 뒤부터 ( ① )~( ⑤ ) 자리 표시 → (주어진 문장, 지문, 정답 번호)"""
    rest = [s for i, s in enumerate(sents) if i != given_idx]
    assert len(rest) in (5, 6), len(rest)
    body = rest[0] + ''.join(GP(k + 1) + (rest[k + 1] if k + 1 < len(rest) else '') for k in range(5))
    return sents[given_idx], body, given_idx   # 정답: rest[0] 뒤가 ①이므로 given_idx(1~5)가 곧 번호

# ═══════════════ 세트 1: 24·29 ═══════════════
A = ["Progressive educators and librarians are developing curricula to teach what we might call attention literacy.",
 "This means helping students recognize, for example, how the architecture of a social media feed or a news site is deliberately designed to distract or provoke them.",
 "Classes in media literacy traditionally cover how to evaluate the credibility of sources — now they also include recognizing clickbait, understanding the role of algorithms in what content is served up, and observing one's own patterns of distraction.",
 "A student might be tasked with tracking how many times they switch tasks or check their phone in an hour of homework, to raise self-awareness about fragmentation.",
 "Another lesson might involve unpacking the design of popular apps: Why does an app use infinite scrolling instead of pages? Why do notifications appear with specific colors and sounds?",
 "By treating these as deliberate design choices (often rooted in psychology and profit motives), young people become more critical users rather than passive consumers."]
P24 = ' '.join(A)
B = ["Capitalism is not a system where cash is everywhere but rather one in which islands of cash exchange exist within oceans of cheap — or potentially cheap — natures.",
 "Reproducing life within the cash nexus is expensive, and it grows more expensive over time.",
 "Workers' wages can be frozen, even rolled back, but in the end inequality leads to crises of the kind we've recently seen bring about populist protests in the United States and the United Kingdom.",
 "Workers demand dignity, and their labor becomes expensive.",
 "Production processes burn through an island, and energy is no longer cheap.",
 "The climate changes, and crops can no longer grow as abundantly as they once did.",
 "Frontiers are so important in these processes because they offer places where the new cheap things can be seized — and the cheap work of humans and other natures can be forcefully taken."]
P29 = ' '.join(B)
T = Test('2429', '24·29번', '주의력 문해력 · 자본주의와 값싼 자연', '24·29번',
 '범위: 24번(주의를 빼앗도록 설계된 디지털 환경을 알아보는 교육) · 29번(값싼 자연과 변경에 기대는 자본주의). 지문은 원문을 일부 바꾼 것이 있어요. 선택지는 본문 표현을 다른 말로 바꿔 썼으니 뜻을 정확히 따져 보세요.')
T.fixed('다음 글의 밑줄 친 부분 중, 문맥상 낱말의 쓰임이 적절하지 <u>않은</u> 것은?', '24번 변형', BOX(
 "This means helping students recognize how the architecture of a social media feed is " + CN(1, 'deliberately') + " designed to distract or provoke them. Classes in media literacy traditionally cover how to evaluate the " + CN(2, 'credibility') + " of sources. A student might be tasked with tracking how many times they check their phone in an hour of homework, to " + CN(3, 'reduce') + " self-awareness about fragmentation. Another lesson might involve " + CN(4, 'unpacking') + " the design of popular apps. By treating these as deliberate design choices, young people become more " + CN(5, 'critical') + " users rather than passive consumers."),
 ['deliberately', 'credibility', 'reduce', 'unpacking', 'critical'], 3,
 "이유 ▶ 휴대폰을 몇 번 확인하는지 기록하는 것은 주의가 쪼개지는 것에 대한 자기 인식을 '높이기' 위해서 → <i>raise</i>가 맞다.\n오답 ▶ ① 피드가 '의도적으로' 설계됨 ✔ ② 출처의 '신뢰성'을 평가 ✔ ④ 앱 디자인을 '뜯어보는' 수업 ✔ ⑤ 더 '비판적인' 사용자 ✔\n포인트 ▶ 활동의 목적(to 부정사)이 글의 방향(알아차리게 하기)과 맞는지 확인!",
 [['deliberately', '의도적으로'], ['credibility', '신뢰성'], ['fragmentation', '파편화, 조각남'], ['unpack', '뜯어보다, 분석하다']])
T.flex('다음 글의 주제로 가장 적절한 것은?', '24번', BOX(P24), [
 ('teaching students to see how digital media is designed to capture attention', '디지털 미디어가 주의를 사로잡도록 어떻게 설계되는지 보도록 학생들을 가르치기'),
 ('the benefits of infinite scrolling for students\' learning', '무한 스크롤이 학생의 학습에 주는 이점'),
 ('why librarians should ban smartphones in schools', '사서들이 학교에서 스마트폰을 금지해야 하는 이유'),
 ('the history of media literacy classes in schools', '학교 미디어 문해력 수업의 역사'),
 ('how app designers learn psychology to earn profits', '앱 설계자들이 이익을 위해 심리학을 배우는 방법')],
 "이유 ▶ attention literacy = 피드·앱이 주의를 빼앗도록 의도적으로 설계된 방식을 알아보게 하는 교육 → 비판적 사용자로 키움.\n오답 ▶ {1} 무한 스크롤은 분석 대상일 뿐 이점이 아니다 {2} 금지는 언급 없음 {3} 역사는 일부 배경 {4} 설계자의 학습이 아니라 학생 교육이 중심\n포인트 ▶ 첫 문장(attention literacy)과 마지막 문장(critical users)이 주제를 감싼다.",
 [['capture', '사로잡다'], ['curriculum', '교육과정 (복수 curricula)'], ['literacy', '문해력, 이해 능력'], ['ban', '금지하다']])
T.flex('다음 글의 내용과 일치하는 것은?', '24번', BOX(P24), [
 ('Students may be asked to monitor how often they check their phones while studying.', '학생들은 공부하는 동안 휴대폰을 얼마나 자주 확인하는지 살펴보라는 과제를 받을 수 있다.'),
 ('Media literacy classes no longer teach how to judge the credibility of sources.', '미디어 문해력 수업은 더 이상 출처의 신뢰성을 판단하는 법을 가르치지 않는다.'),
 ('The design features of popular apps are presented as accidental.', '인기 앱의 디자인 요소는 우연한 것으로 소개된다.'),
 ('Attention literacy aims to make students passive consumers of media.', '주의력 문해력은 학생들을 미디어의 수동적 소비자로 만드는 것을 목표로 한다.'),
 ('Notifications are said to be designed without any colors or sounds.', '알림은 색깔이나 소리 없이 설계된다고 한다.')],
 "이유 ▶ tracking how many times they switch tasks or check their phone in an hour of homework = 공부 중 휴대폰 확인 횟수를 살펴봄 ✔\n오답 ▶ {1} traditionally cover ~ now they also include(전부터 가르쳤고 이제 더 가르침) {2} deliberate design choices(의도적인 선택) {3} critical users rather than passive consumers {4} specific colors and sounds\n포인트 ▶ no longer / also, accidental / deliberate 같은 반대 표현 함정!",
 [['monitor', '살펴보다, 감시하다'], ['judge', '판단하다'], ['accidental', '우연한'], ['passive', '수동적인']])
T.flex('다음 빈칸에 들어갈 말로 가장 적절한 것은?', '24번 변형', BOX(
 ' '.join(A[:5]) + " By treating these as deliberate design choices (often rooted in psychology and profit motives), young people become more critical users rather than " + BL + "."), [
 ('passive consumers', '수동적인 소비자'), ('creative designers', '창의적인 설계자'), ('expert programmers', '전문 프로그래머'),
 ('careful librarians', '신중한 사서'), ('active critics', '적극적인 비평가')],
 "이유 ▶ rather than(~가 아니라) 앞의 more critical users와 반대 → 비판 없이 받아들이기만 하는 '수동적인 소비자'.\n오답 ▶ {1}·{2}·{3} 학생이 되는 대상과 관계없음 {4} active critics는 critical users와 같은 쪽이라 rather than 대비가 깨진다\n포인트 ▶ A rather than B: A와 B는 반대 개념.",
 [['rooted in', '~에 뿌리를 둔'], ['profit motive', '이윤 동기'], ['critical', '비판적인'], ['consumer', '소비자']])
T.fixed('다음 글의 밑줄 친 부분 중, 어법상 <u>틀린</u> 것은?', '24번 변형', BOX(
 "This means " + CN(1, 'helping') + " students recognize how the architecture of a social media feed " + CN(2, 'is') + " deliberately designed to distract or provoke them. Classes in media literacy now also include " + CN(3, 'recognizing') + " clickbait. A student might be tasked with " + CN(4, 'tracking') + " how many times they switch tasks. By " + CN(5, 'treat') + " these as deliberate design choices, young people become more critical users."),
 ['helping', 'is', 'recognizing', 'tracking', 'treat'], 5,
 "이유 ▶ 전치사 By 뒤에는 동명사 → <i>treating</i>.\n오답 ▶ ① means의 목적어 동명사 ✔ ② 주어 the architecture(단수), 설계'되는' 수동 ✔ ③ include의 목적어 동명사 ✔ ④ be tasked with + 동명사 ✔\n포인트 ▶ 전치사(by, with, of) 뒤 동사는 -ing.",
 [['provoke', '자극하다, 도발하다'], ['clickbait', '낚시성 콘텐츠'], ['be tasked with', '~하는 일을 맡다'], ['switch', '바꾸다']])
T.table('(A), (B), (C)의 각 네모 안에서 어법에 맞는 표현으로 가장 적절한 것은?', '24번', BOX(
 "Progressive educators and librarians are developing curricula to teach <b>(A)</b> [ what / that ] we might call attention literacy. … A student might be tasked with tracking how many times they switch tasks or <b>(B)</b> [ check / checking ] their phone in an hour of homework. Another lesson might involve <b>(C)</b> [ unpacking / to unpack ] the design of popular apps."),
 ['(A)', '(B)', '(C)'], [['what', 'check', 'unpacking'], ['that', 'check', 'unpacking'], ['what', 'checking', 'unpacking'], ['what', 'check', 'to unpack'], ['that', 'checking', 'to unpack']],
 "이유 ▶ (A) teach의 목적어 + call의 목적어가 빠진 불완전한 절 → 선행사를 품은 <i>what</i> (B) they switch tasks or check: switch와 병렬인 동사 → <i>check</i> (C) involve는 동명사를 목적어로 → <i>unpacking</i>\n오답 ▶ that은 앞에 선행사가 필요 / checking은 tracking과 병렬로 착각 / involve + to부정사는 불가\n포인트 ▶ 병렬: 접속사 or 앞뒤의 형태를 맞춘다.",
 [['progressive', '진보적인'], ['curricula', '교육과정들'], ['attention literacy', '주의력 문해력'], ['involve', '포함하다']])
T.flex('밑줄 친 <u>fragmentation</u>이 의미하는 바로 가장 적절한 것은?', '24번', BOX(P24.replace('fragmentation', U('fragmentation'))), [
 '여러 일과 휴대폰 사이를 오가면서 주의가 조각조각 나뉘는 상태', '공부할 과목을 여러 개로 나누어 계획하는 습관',
 '스마트폰 화면이 깨져서 사용하기 어려운 상태', '친구들과의 관계가 멀어져 고립되는 현상', '숙제 시간을 일정하게 지키는 능력'],
 "이유 ▶ 숙제하는 한 시간 동안 일을 바꾸거나 휴대폰을 확인하는 횟수를 세는 활동 → 주의가 계속 끊기고 쪼개지는 상태(fragmentation)를 스스로 알아차리게 함.\n오답 ▶ {1} 계획 세우기 {2} 화면 파손 {3} 인간관계 {4} 시간 지키기 → 모두 근거 없음\n포인트 ▶ 함축 의미는 바로 앞 활동(switch tasks, check their phone)에서 찾는다.",
 [['fragmentation', '파편화, 조각남'], ['self-awareness', '자기 인식'], ['switch tasks', '일을 바꾸다'], ['distraction', '주의 산만']], en=False)
g, body, a = INS(3, A)
T.fixed('글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳은?', '24번', GIV(g) + '\n' + BOX(body), None, a,
 "이유 ▶ 앞 문장 끝의 observing one's own patterns of distraction(자신의 주의 산만 패턴 관찰)의 구체적인 예가 주어진 문장(휴대폰 확인 횟수 기록) → 그 뒤, Another lesson(또 다른 수업) 앞 ③.\n오답 ▶ ①② 아직 주의 산만 관찰 이야기가 나오기 전 ④⑤ Another lesson 뒤라 첫 번째 수업 예시가 빠진다\n포인트 ▶ A student might ~ / Another lesson might ~ : 예시 1 → 예시 2 순서.",
 [['be tasked with', '~하는 일을 맡다'], ['track', '기록하다, 추적하다'], ['raise', '높이다'], ['another', '또 다른']])
T.table('다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 적절한 것은?', '24번', BOX(P24) + '\n' + SUM(
 'Attention literacy teaches students to <b>(A)</b> ' + BL + ' how digital platforms are designed to grab their attention so that they can become <b>(B)</b> ' + BL + ' users.'),
 ['(A)', '(B)'], [['recognize', 'critical'], ['ignore', 'critical'], ['recognize', 'passive'], ['design', 'loyal'], ['ignore', 'frequent']],
 "이유 ▶ (A) helping students recognize ~ deliberately designed → <i>recognize</i> (B) become more critical users rather than passive consumers → <i>critical</i>\n오답 ▶ ignore(무시하다)는 recognize와 반대 / passive는 rather than 뒤의 반대 개념 / design·loyal·frequent는 근거 없음\n포인트 ▶ 요약문은 첫 문장(무엇을 가르치나)과 마지막 문장(어떤 사용자가 되나)을 합친다.",
 [['grab', '붙잡다'], ['recognize', '알아차리다'], ['loyal', '충성스러운'], ['frequent', '잦은']],
 ko=['알아차리다 / 비판적인', '무시하다 / 비판적인', '알아차리다 / 수동적인', '설계하다 / 충성스러운', '무시하다 / 잦은'])
# 29
T.flex('다음 글의 요지로 가장 적절한 것은?', '29번', BOX(P29), [
 '자본주의는 비용이 계속 오르기 때문에 값싼 자원과 노동을 차지할 수 있는 새로운 변경을 끊임없이 필요로 한다.',
 '현금이 모든 곳에서 쓰이게 되면 자본주의는 더 안정된다.', '노동자의 임금을 동결하면 불평등을 해소할 수 있다.',
 '기후 변화는 자본주의와 아무 관련이 없는 자연 현상이다.', '변경을 보호하면 값싼 노동이 자연스럽게 늘어난다.'],
 "이유 ▶ 현금 경제 안의 삶은 갈수록 비싸짐(노동·에너지·농작물) → 그래서 값싼 것을 빼앗을 수 있는 변경(frontiers)이 중요하다.\n오답 ▶ {1} 현금이 어디에나 있는 체제가 아니라고 했다 {2} 동결해도 결국 불평등이 위기를 부른다 {3} 기후 변화도 비용 상승 과정의 일부 {4} 변경은 보호가 아니라 빼앗는(seized) 곳\n포인트 ▶ 마지막 문장 Frontiers are so important ~ because ~ 가 요지.",
 [['frontier', '변경, 개척지'], ['capitalism', '자본주의'], ['inequality', '불평등'], ['seize', '빼앗다, 장악하다']], en=False)
T.flex('다음 빈칸에 들어갈 말로 가장 적절한 것은?', '29번 변형', BOX(' '.join(B[:6]) + " Frontiers are so important in these processes because they offer places where " + BL + "."), [
 ('new cheap things and labor can be seized', '새로운 값싼 것들과 노동을 빼앗을 수 있다'),
 ('workers are finally paid with dignity', '노동자들이 마침내 존엄하게 대우받는다'),
 ('cash exchange becomes completely unnecessary', '현금 거래가 완전히 필요 없어진다'),
 ('crops grow less abundantly than before', '농작물이 전보다 덜 풍부하게 자란다'),
 ('energy becomes more expensive than ever', '에너지가 그 어느 때보다 비싸진다')],
 "이유 ▶ 앞 내용: 노동·에너지·농작물이 모두 비싸짐 → 변경이 중요한 이유는 새로운 '값싼' 것과 노동을 차지할 수 있기 때문.\n오답 ▶ {1} 존엄한 대우는 노동을 비싸게 만드는 원인 {2} 현금 거래가 없어진다는 말은 없다 {3}·{4} 변경이 아니라 기존 '섬'에서 일어나는 비용 상승\n포인트 ▶ 빈칸 문장은 앞의 문제(비싸짐)에 대한 해결(값싼 것 확보).",
 [['process', '과정'], ['seize', '빼앗다'], ['dignity', '존엄'], ['abundantly', '풍부하게']])
T.flex('다음 글의 내용과 일치하지 <u>않는</u> 것은?', '29번', BOX(P29), [
 ('Workers\' wages can never be reduced under capitalism.', '자본주의에서 노동자의 임금은 결코 줄어들 수 없다.'),
 ('Cash exchange takes place only in limited areas.', '현금 거래는 제한된 영역에서만 이루어진다.'),
 ('Maintaining life within the cash economy grows costlier over time.', '현금 경제 안에서 삶을 유지하는 데는 시간이 갈수록 비용이 더 든다.'),
 ('Climate change can reduce the amount of crops produced.', '기후 변화는 농작물 생산량을 줄일 수 있다.'),
 ('Frontiers allow cheap labor to be taken by force.', '변경은 값싼 노동을 강제로 빼앗을 수 있게 해 준다.')],
 "이유 ▶ wages can be frozen, even rolled back(동결되고 심지어 깎일 수도 있다) → '결코 줄어들 수 없다'는 불일치.\n오답 ▶ {1} islands of cash exchange ✔ {2} it grows more expensive over time ✔ {3} crops can no longer grow as abundantly ✔ {4} forcefully taken ✔\n포인트 ▶ roll back = 되돌리다, (임금을) 삭감하다.",
 [['roll back', '되돌리다, 삭감하다'], ['take place', '일어나다'], ['costly', '비용이 드는'], ['by force', '강제로']])
T.fixed('다음 글의 밑줄 친 부분 중, 문맥상 낱말의 쓰임이 적절하지 <u>않은</u> 것은?', '29번 변형', BOX(
 "Capitalism is a system in which islands of cash exchange exist within oceans of " + CN(1, 'cheap') + " natures. Reproducing life within the cash nexus is " + CN(2, 'expensive') + ", and it grows more expensive over time. Workers' wages can be " + CN(3, 'frozen') + ", but in the end inequality leads to crises. The climate changes, and crops can no longer grow as " + CN(4, 'poorly') + " as they once did. Frontiers are important because the cheap work of humans and other natures can be " + CN(5, 'forcefully') + " taken there."),
 ['cheap', 'expensive', 'frozen', 'poorly', 'forcefully'], 4,
 "이유 ▶ 기후가 변해 농작물이 '예전만큼 풍부하게' 자라지 못한다 → <i>abundantly</i>. poorly면 '예전만큼 형편없이 자라지 못한다'로 뜻이 반대.\n오답 ▶ ① 값싼 자연 ✔ ② 비싸다 ✔ ③ 임금 동결 ✔ ⑤ 강제로 빼앗김 ✔\n포인트 ▶ no longer ~ as … as once: 예전만큼 …하지 않다 → 예전에는 좋았음.",
 [['nexus', '연결, 결합'], ['freeze', '동결하다'], ['abundantly', '풍부하게'], ['forcefully', '강제로']])
T.fixed('다음 글의 밑줄 친 부분 중, 어법상 <u>틀린</u> 것은?', '29번 변형', BOX(
 "Capitalism is not a system " + CN(1, 'where') + " cash is everywhere but rather one in " + CN(2, 'that') + " islands of cash exchange exist within oceans of cheap natures. Reproducing life within the cash nexus " + CN(3, 'is') + " expensive. In the end inequality leads to crises of the kind we've recently seen " + CN(4, 'bring') + " about populist protests. Frontiers offer places where the cheap work of humans can be forcefully " + CN(5, 'taken') + "."),
 ['where', 'that', 'is', 'bring', 'taken'], 2,
 "이유 ▶ 전치사 in 뒤에는 관계대명사 that을 쓸 수 없다 → <i>in which</i>.\n오답 ▶ ① 뒤가 완전한 절 + a system → 관계부사 where ✔ ③ 동명사 주어 Reproducing(단수) ✔ ④ 지각동사 see + 목적어 + 동사원형 ✔ ⑤ 노동이 '빼앗기는' 수동 ✔\n포인트 ▶ 전치사 + which ⭕ / 전치사 + that ❌",
 [['populist', '포퓰리즘의'], ['bring about', '일으키다'], ['reproduce', '재생산하다'], ['cash exchange', '현금 거래']])
body, a = ABC(B[0], [B[1:3], B[3:6], B[6:7]], 'BAC')
T.fixed('주어진 글 다음에 이어질 글의 순서로 가장 적절한 것은?', '29번', body, OPTS_ORD, a,
 "이유 ▶ 주어진 글(현금 거래의 섬 + 값싼 자연의 바다) → (B) 현금 경제 안의 삶은 점점 비싸짐·임금 동결도 결국 위기 → (A) 노동·에너지·농작물이 모두 비싸짐 → (C) 그래서 이런 과정(these processes)에서 변경이 중요\n오답 ▶ (C)가 먼저 오면 these processes가 가리킬 내용이 없다\n포인트 ▶ these processes = 앞에 나열된 비용 상승 과정.",
 [['frontier', '변경'], ['wage', '임금'], ['burn through', '다 써 버리다'], ['process', '과정']], en=False)
T.flex('밑줄 친 <u>islands of cash exchange exist within oceans of cheap natures</u>가 의미하는 바로 가장 적절한 것은?', '29번', BOX(P29.replace('islands of cash exchange exist within oceans of cheap — or potentially cheap — natures', U('islands of cash exchange exist within oceans of cheap — or potentially cheap — natures'))), [
 '현금이 오가는 영역은 일부일 뿐이고, 그 바깥의 값싼 자원과 노동이 훨씬 넓게 자본주의를 떠받친다.', '자본주의는 섬나라에서 시작되어 바다를 건너 퍼졌다.',
 '현금 거래는 바다를 통한 무역에서만 이루어진다.', '자연은 현금으로 사고팔 수 없는 영역이라 자본주의와 무관하다.', '값싼 자연은 곧 사라지고 현금 거래가 모든 곳을 덮을 것이다.'],
 "이유 ▶ 현금이 어디에나 있는 체제가 아니라(not ~ everywhere), 현금 거래는 '섬'처럼 일부이고 그 주변의 '바다' 같은 값싼 자연(자원·노동)에 기대고 있다는 비유.\n오답 ▶ {1}·{2} 실제 섬·바다로 착각한 함정 {3} 무관하다면 변경이 중요할 이유가 없다 {4} 오히려 값싼 것을 계속 새로 찾는다\n포인트 ▶ 비유(islands ↔ oceans)는 크기의 대비: 작은 현금 영역 ↔ 넓은 값싼 자연.",
 [['island', '섬'], ['ocean', '바다'], ['potentially', '잠재적으로'], ['nature', '자연(여기서는 자원·노동 등)']], en=False)
T.table('다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 적절한 것은?', '29번', BOX(P29) + '\n' + SUM(
 'As the costs of sustaining life within capitalism <b>(A)</b> ' + BL + ', frontiers become essential as sources of <b>(B)</b> ' + BL + ' resources and labor.'),
 ['(A)', '(B)'], [['rise', 'cheap'], ['fall', 'cheap'], ['rise', 'expensive'], ['stabilize', 'rare'], ['fall', 'protected']],
 "이유 ▶ (A) it grows more expensive over time → <i>rise</i> (B) places where the new cheap things can be seized → <i>cheap</i>\n오답 ▶ fall·stabilize는 비용 상승과 반대 / expensive·rare·protected는 변경이 주는 것(값싼 것)과 반대\n포인트 ▶ 원인(비용 상승) → 결과(값싼 것을 찾아 변경으로).",
 [['sustain', '유지하다'], ['essential', '필수적인'], ['stabilize', '안정되다'], ['source', '원천']],
 ko=['오르다 / 값싼', '떨어지다 / 값싼', '오르다 / 비싼', '안정되다 / 드문', '떨어지다 / 보호받는'])
g, body, a = INS(3, B)
T.fixed('글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳은?', '29번', GIV(g) + '\n' + BOX(body), None, a,
 "이유 ▶ 불평등이 위기·시위를 부른다는 문장 뒤에, 노동자들이 존엄을 요구해 노동이 비싸진다는 주어진 문장 → 이어서 에너지(Production processes ~)·농작물 순으로 비용 상승이 나열됨 → ③.\n오답 ▶ ①② 임금·위기 이야기가 나오기 전 ④⑤ 에너지·기후 이야기 사이에 끼면 노동 이야기가 흐름을 끊는다\n포인트 ▶ 나열 순서: 노동 → 에너지 → 농작물 → 그래서 변경.",
 [['dignity', '존엄'], ['labor', '노동'], ['demand', '요구하다'], ['crisis', '위기 (복수 crises)']])
T.flex('24·29번 지문에 나온 단어와 영영풀이가 바르게 짝지어지지 <u>않은</u> 것은?', '종합', '', [
 ('abundantly: in small and insufficient amounts', 'abundantly: 적고 부족한 양으로'),
 ('credibility: the quality of being trusted and believed', 'credibility: 신뢰받고 믿어지는 성질'),
 ('fragmentation: the process of breaking into small parts', 'fragmentation: 작은 조각으로 나뉘는 과정'),
 ('frontier: an area where new things can be found or developed', 'frontier: 새로운 것을 찾거나 개발할 수 있는 지역'),
 ('seize: to take something quickly and by force', 'seize: 무언가를 재빨리, 강제로 차지하다')],
 "이유 ▶ abundantly는 '풍부하게(in large amounts)'. 적고 부족한 양은 반대 뜻.\n오답 ▶ {1} credibility 신뢰성 ✔ {2} fragmentation 파편화 ✔ {3} frontier 변경, 개척지 ✔ {4} seize 빼앗다 ✔\n포인트 ▶ 영영풀이 문제는 반의어로 바꾼 풀이를 찾는다.",
 [['insufficient', '불충분한'], ['abundantly', '풍부하게'], ['by force', '강제로'], ['develop', '개발하다']])
T.fixed('다음 (a)~(g) 중 어법상 <u>틀린</u> 것의 개수는?', '종합', BOX(
 "Educators are developing curricula to teach " + TG('a', 'what') + " we might call attention literacy. A student might be tasked with " + TG('b', 'track') + " how many times they check their phone. Why " + TG('c', 'does') + " an app use infinite scrolling? Young people become more critical users rather than passive " + TG('d', 'consumers') + ". Reproducing life within the cash nexus " + TG('e', 'are') + " expensive. Workers' wages can " + TG('f', 'be frozen') + ". Frontiers offer places " + TG('g', 'which') + " the new cheap things can be seized."),
 ['1개', '2개', '3개', '4개', '5개'], 3,
 "이유 ▶ 틀린 것 (b) (e) (g) 3개. (b) be tasked with + 동명사 → <i>tracking</i> (e) 동명사 주어는 단수 → <i>is</i> (g) 뒤가 완전한 수동태 절 → 관계부사 <i>where</i>\n오답 ▶ (a) 불완전한 절을 이끄는 what ✔ (c) 의문문 does + 주어 + 동사원형 ✔ (d) rather than 뒤 명사 ✔ (f) 임금이 '동결되는' 수동 ✔\n포인트 ▶ 관계대명사 which(불완전) ↔ 관계부사 where(완전).",
 [['curricula', '교육과정들'], ['infinite scrolling', '무한 스크롤'], ['nexus', '연결'], ['seize', '빼앗다']], en=False)
T.render()

# ═══════════════ 세트 2: 30·34 ═══════════════
C = ["Some people are more likely to cheat and steal after purchasing \"eco-friendly\" products, probably because they feel licensed to do so since they morally account the \"eco-friendly\" choice as a \"good\" deed.",
 "Moral licensing has also been observed in the context of cooperation for the good of the environment.",
 "When people are reminded of deeds they have done that they know were harmful to the environment, they might be left with a feeling of \"eco-guilt.\"",
 "People who experience eco-guilt seek pro-environmental actions to compensate for this guilt and restore balance.",
 "In their search for such a balance, people are inclined to believe in \"quick-fixes,\" because they want to re-establish the moral balance and escape the guilt as quickly and easily as possible.",
 "In the same way that people may change their attitudes to reduce inconsistencies between attitudes and behavior, people may also change their evaluation of past environmentally burdening behaviors and future environmentally friendly behaviors.",
 "For instance, people are more likely to sign a petition addressing environmental damage after viewing evidence of human-caused environmental damage."]
P30 = ' '.join(C)
D = ["When we focus on the obvious aspects of media, we miss the changes that accumulate over time but are not apparent day to day.",
 "Most of us notice the obvious aspects of a new medium or technology while missing the more subtle aspects.",
 "Take, for example, the microwave oven.",
 "It was introduced in the early 1980s and revolutionized food preparation.",
 "Traditionally, one person spent the better part of an afternoon fixing an evening meal for a family.",
 "Now, it was possible to prepare foods very quickly, and this shortening of preparation time was liberating for the cooks in the family, most of whom tended to be women.",
 "But the short-term, obvious implications of greater convenience made it easy to overlook the long-term implications of no longer having one person fix food for the family to eat together at an evening meal.",
 "As time went on, fewer and fewer families sat down together to eat dinner.",
 "Meals that took a long time to prepare became a luxury of the past, except perhaps for special occasions.",
 "The effects of the microwave oven on family life were not anticipated and would have been difficult to foresee."]
P34 = ' '.join(D)
T = Test('3034', '30·34번', '도덕적 면허와 환경 죄책감 · 전자레인지와 보이지 않는 변화', '30·34번',
 '범위: 30번(친환경 행동과 도덕적 균형) · 34번(새 기술의 뚜렷한 면에 가려진 미묘한 변화). 지문은 원문을 일부 바꾼 것이 있어요. 선택지는 본문 표현을 다른 말로 바꿔 썼으니 뜻을 정확히 따져 보세요.')
T.fixed('다음 글의 밑줄 친 부분 중, 문맥상 낱말의 쓰임이 적절하지 <u>않은</u> 것은?', '30번 변형', BOX(
 "Some people are more likely to cheat after purchasing \"eco-friendly\" products, probably because they feel " + CN(1, 'licensed') + " to do so. When people are reminded of deeds that they know were " + CN(2, 'harmful') + " to the environment, they might be left with a feeling of \"eco-guilt.\" People who experience eco-guilt seek pro-environmental actions to " + CN(3, 'compensate') + " for this guilt. People are inclined to believe in \"quick-fixes,\" because they want to escape the guilt as " + CN(4, 'slowly') + " and easily as possible. For instance, people are " + CN(5, 'more') + " likely to sign a petition after viewing evidence of human-caused environmental damage."),
 ['licensed', 'harmful', 'compensate', 'slowly', 'more'], 4,
 "이유 ▶ quick-fixes(빠른 해결책)를 믿는 이유 → 죄책감에서 최대한 '빨리' 벗어나고 싶어서 → <i>quickly</i>.\n오답 ▶ ① 나쁜 짓을 해도 된다고 '허락받은' 느낌 ✔ ② 환경에 '해로운' 행동 ✔ ③ 죄책감을 '만회하려고' ✔ ⑤ 피해 증거를 보면 서명할 가능성이 '더' 높다 ✔\n포인트 ▶ 빈칸 근처의 핵심어(quick-fixes)와 어울리는지 확인.",
 [['licensed', '허락받은'], ['compensate for', '만회하다'], ['quick-fix', '빠른 해결책'], ['petition', '청원(서)']])
T.flex('다음 글의 주제로 가장 적절한 것은?', '30번', BOX(P30), [
 ('how people try to keep their moral balance through environmental behavior', '사람들이 환경 행동을 통해 도덕적 균형을 지키려는 방식'),
 ('why eco-friendly products are more expensive than others', '친환경 제품이 다른 제품보다 비싼 이유'),
 ('the long-term effects of petitions on environmental laws', '청원이 환경법에 미치는 장기적 영향'),
 ('ways to stop people from buying eco-friendly products', '사람들이 친환경 제품을 사지 못하게 하는 방법'),
 ('the history of the environmental movement', '환경 운동의 역사')],
 "이유 ▶ 착한 일(친환경 구매) 뒤엔 나쁜 행동을 허락하고(도덕적 면허), 해로운 일 뒤엔 죄책감을 만회하려 함 → 도덕적 균형(moral balance)을 맞추려는 심리.\n오답 ▶ {1} 가격 이야기 없음 {2} 청원은 예시일 뿐 {3} 구매를 막자는 말 없음 {4} 역사 언급 없음\n포인트 ▶ 반복어 balance가 주제의 열쇠.",
 [['moral', '도덕적인'], ['balance', '균형'], ['movement', '운동'], ['long-term', '장기적인']])
T.flex('다음 글의 내용과 일치하는 것은?', '30번', BOX(P30), [
 ('Feeling eco-guilt can push people to seek pro-environmental actions.', '환경 죄책감을 느끼면 사람들은 친환경 행동을 찾게 될 수 있다.'),
 ('Buying eco-friendly products makes people more honest.', '친환경 제품을 사면 사람들이 더 정직해진다.'),
 ('Moral licensing has never been seen in environmental cooperation.', '도덕적 면허는 환경 협력에서 관찰된 적이 없다.'),
 ('People with eco-guilt prefer slow and difficult solutions.', '환경 죄책감을 느끼는 사람들은 느리고 어려운 해결책을 좋아한다.'),
 ('Evidence of environmental damage makes people less likely to sign petitions.', '환경 피해의 증거를 보면 사람들은 청원에 덜 서명한다.')],
 "이유 ▶ People who experience eco-guilt seek pro-environmental actions ✔\n오답 ▶ {1} cheat and steal(속이고 훔친다) {2} has also been observed(관찰되었다) {3} quick-fixes, quickly and easily {4} more likely to sign\n포인트 ▶ 비교·부정 표현(more/less, never)을 꼼꼼히!",
 [['pro-environmental', '친환경적인'], ['honest', '정직한'], ['cooperation', '협력'], ['evidence', '증거']])
T.flex('다음 빈칸에 들어갈 말로 가장 적절한 것은?', '30번 변형', BOX(' '.join(C[:4]) + " In their search for such a balance, people are inclined to believe in " + BL + ", because they want to re-establish the moral balance and escape the guilt as quickly and easily as possible."), [
 ('quick-fixes', '빠른 해결책'), ('long-term plans', '장기 계획'), ('strict rules', '엄격한 규칙'), ('expert advice', '전문가의 조언'), ('public promises', '공개적인 약속')],
 "이유 ▶ 빈칸 뒤 because ~ as quickly and easily as possible(최대한 빠르고 쉽게) → 빠른 해결책(quick-fixes).\n오답 ▶ {1} 장기 계획은 빠르고 쉬운 것과 반대 {2}·{3}·{4} 빠르고 쉽다는 이유와 연결되지 않는다\n포인트 ▶ 빈칸 뒤 이유(because)가 단서.",
 [['be inclined to', '~하는 경향이 있다'], ['re-establish', '다시 세우다'], ['escape', '벗어나다'], ['strict', '엄격한']])
T.fixed('다음 글의 밑줄 친 부분 중, 어법상 <u>틀린</u> 것은?', '30번 변형', BOX(
 "Some people are more likely " + CN(1, 'to cheat') + " and steal after purchasing \"eco-friendly\" products, probably because they feel licensed " + CN(2, 'to do') + " so. When people are reminded of deeds they have done " + CN(3, 'that') + " they know were harmful to the environment, they might be left with a feeling of \"eco-guilt.\" People who experience eco-guilt " + CN(4, 'seeks') + " pro-environmental actions to compensate for this guilt. For instance, people are more likely to sign a petition " + CN(5, 'after') + " viewing evidence of human-caused environmental damage."),
 ['to cheat', 'to do', 'that', 'seeks', 'after'], 4,
 "이유 ▶ 주어는 People(복수), who experience eco-guilt는 꾸미는 말 → <i>seek</i>.\n오답 ▶ ① be likely to + 동사원형 ✔ ② feel licensed to do ✔ ③ deeds를 꾸미는 관계대명사(they know는 삽입) ✔ ⑤ 전치사 after + 동명사 ✔\n포인트 ▶ 주어 뒤 관계절은 괄호로 묶고 동사와 수 일치!",
 [['purchase', '구매하다'], ['deed', '행동, 행위'], ['experience', '경험하다'], ['view', '보다']])
T.table('(A), (B), (C)의 각 네모 안에서 어법에 맞는 표현으로 가장 적절한 것은?', '30번', BOX(
 "Some people are more likely to cheat and steal after <b>(A)</b> [ purchasing / purchased ] \"eco-friendly\" products. … People <b>(B)</b> [ who / which ] experience eco-guilt seek pro-environmental actions. … For instance, people are more likely to sign a petition <b>(C)</b> [ addressing / addressed ] environmental damage."),
 ['(A)', '(B)', '(C)'], [['purchasing', 'who', 'addressing'], ['purchased', 'who', 'addressing'], ['purchasing', 'which', 'addressing'], ['purchasing', 'who', 'addressed'], ['purchased', 'which', 'addressed']],
 "이유 ▶ (A) 전치사 after + 동명사 → <i>purchasing</i> (B) 선행사 People(사람) → <i>who</i> (C) 청원서가 환경 피해를 '다루는' 능동, 뒤에 목적어 environmental damage → <i>addressing</i>\n오답 ▶ purchased는 전치사 뒤에 못 옴 / which는 사물 / addressed는 수동이라 목적어를 못 받음\n포인트 ▶ 명사 뒤 분사: 뒤에 목적어가 있으면 -ing.",
 [['address', '다루다'], ['eco-friendly', '친환경적인'], ['experience', '경험하다'], ['damage', '피해']])
T.flex('밑줄 친 <u>they feel licensed to do so</u>가 의미하는 바로 가장 적절한 것은?', '30번', BOX(P30.replace('they feel licensed to do so', U('they feel licensed to do so'))), [
 '친환경 제품을 사며 착한 일을 했으니 나쁜 행동을 해도 된다고 스스로 허락한다.', '정부로부터 친환경 제품을 팔 수 있는 허가를 받았다고 느낀다.',
 '친환경 제품을 샀으니 앞으로도 계속 친환경 제품만 사야 한다고 느낀다.', '친환경 제품의 품질을 보증할 자격이 있다고 생각한다.', '환경을 해친 것에 대해 벌을 받아야 한다고 느낀다.'],
 "이유 ▶ 친환경 선택을 '착한 일(good deed)'로 계산하기 때문에 속이고 훔치는 것(cheat and steal)을 해도 된다고 스스로 허락한다는 뜻.\n오답 ▶ {1} license를 실제 면허로 착각 {2} 계속 친환경만 산다는 말은 없다 {3} 품질 보증과 무관 {4} 벌이 아니라 허락\n포인트 ▶ do so = cheat and steal.",
 [['license', '허락하다, 면허를 주다'], ['account A as B', 'A를 B로 여기다'], ['cheat', '속이다'], ['deed', '행위']], en=False)
g, body, a = INS(3, C)
T.fixed('글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳은?', '30번', GIV(g) + '\n' + BOX(body), None, a,
 "이유 ▶ 앞 문장에서 환경 죄책감(eco-guilt)이 생기고, 주어진 문장에서 그 죄책감을 만회하려고 균형(balance)을 찾음 → 다음 문장 In their search for such a balance(그런 균형을 찾는 과정에서)로 이어짐 → ③.\n오답 ▶ ①② eco-guilt가 아직 나오지 않음 ④⑤ such a balance가 가리킬 말이 앞에 없어짐\n포인트 ▶ such a balance ← restore balance.",
 [['restore', '되찾다'], ['compensate for', '만회하다'], ['pro-environmental', '친환경적인'], ['guilt', '죄책감']])
T.table('다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 적절한 것은?', '30번', BOX(P30) + '\n' + SUM(
 'Doing something eco-friendly can make people feel <b>(A)</b> ' + BL + ' to act badly, while eco-guilt drives them to seek <b>(B)</b> ' + BL + ' ways to restore their moral balance.'),
 ['(A)', '(B)'], [['entitled', 'easy'], ['afraid', 'easy'], ['entitled', 'difficult'], ['forced', 'costly'], ['unwilling', 'slow']],
 "이유 ▶ (A) feel licensed to do so = 나쁜 행동을 할 자격이 있다고 느낌 → <i>entitled</i> (B) quick-fixes, quickly and easily → <i>easy</i>\n오답 ▶ afraid·unwilling은 licensed와 반대 / difficult·slow·costly는 quick-fixes와 반대 / forced(강요된)는 스스로 허락한 것과 다름\n포인트 ▶ licensed ≒ entitled(자격이 있다고 여기는).",
 [['entitled', '자격이 있다고 여기는'], ['drive', '몰아가다'], ['restore', '되찾다'], ['unwilling', '꺼리는']],
 ko=['자격이 있다고 여기는 / 쉬운', '두려워하는 / 쉬운', '자격이 있다고 여기는 / 어려운', '강요된 / 비용이 드는', '꺼리는 / 느린'])
# 34
T.flex('다음 글의 요지로 가장 적절한 것은?', '34번', BOX(P34), [
 '새로운 기술의 뚜렷한 이점에 가려, 시간이 지나며 쌓이는 미묘한 영향을 놓치기 쉽다.', '전자레인지는 가족 식사를 더 풍성하게 만들었다.',
 '새로운 기술은 처음부터 모든 영향을 정확히 예측할 수 있다.', '요리 시간이 짧아지면 가족이 더 자주 함께 식사한다.', '특별한 날에는 전자레인지를 쓰지 않는 것이 좋다.'],
 "이유 ▶ 첫 두 문장(뚜렷한 면만 보고 미묘한 변화를 놓친다)이 주장, 전자레인지는 그 예시(편리함에 가려 가족 식사가 사라짐).\n오답 ▶ {1} 가족 식사는 줄었다 {2} not anticipated, difficult to foresee {3} fewer and fewer families {4} 특별한 날 이야기는 세부 내용\n포인트 ▶ Take, for example ~ 앞이 요지.",
 [['obvious', '뚜렷한'], ['subtle', '미묘한'], ['accumulate', '쌓이다'], ['foresee', '예견하다']], en=False)
T.flex('다음 빈칸에 들어갈 말로 가장 적절한 것은?', '34번 변형', BOX("When we focus on the obvious aspects of media, we miss the changes that " + BL + ". " + ' '.join(D[1:])), [
 ('accumulate over time but are not apparent day to day', '시간이 지나며 쌓이지만 날마다 드러나지는 않는'),
 ('are clearly visible from the very beginning', '처음부터 분명하게 보이는'),
 ('make cooking faster and more convenient', '요리를 더 빠르고 편리하게 만드는'),
 ('happen only on special occasions', '특별한 날에만 일어나는'),
 ('are carefully planned by inventors', '발명가들이 신중하게 계획한')],
 "이유 ▶ 뒤에서 전자레인지가 가족 식사를 '서서히(As time went on)' 줄였고 예상하지 못했다(not anticipated) → 시간이 지나며 쌓이지만 당장은 안 보이는 변화.\n오답 ▶ {1} 우리가 놓치는 것은 보이지 않는 변화 {2} 이건 뚜렷한(obvious) 면 {3} 특별한 날은 세부 내용 {4} 계획된 것이 아니라 예상 못 한 것\n포인트 ▶ miss(놓치다)의 대상 = 눈에 잘 안 띄는 것.",
 [['apparent', '분명한'], ['day to day', '날마다'], ['visible', '눈에 보이는'], ['inventor', '발명가']])
T.flex('다음 글의 내용과 일치하지 <u>않는</u> 것은?', '34번', BOX(P34), [
 ('The microwave oven led families to eat together more often.', '전자레인지 덕분에 가족이 더 자주 함께 식사하게 되었다.'),
 ('The microwave oven was introduced in the early 1980s.', '전자레인지는 1980년대 초에 소개되었다.'),
 ('Traditionally, preparing dinner took a large part of the afternoon.', '전통적으로 저녁 준비에는 오후의 상당 시간이 걸렸다.'),
 ('Most of the family cooks were women.', '가족의 요리 담당은 대부분 여성이었다.'),
 ('The microwave\'s effects on family life were hard to predict.', '전자레인지가 가족생활에 미친 영향은 예측하기 어려웠다.')],
 "이유 ▶ As time went on, fewer and fewer families sat down together to eat dinner → '더 자주 함께 식사'는 불일치.\n오답 ▶ {1} introduced in the early 1980s ✔ {2} spent the better part of an afternoon ✔ {3} most of whom tended to be women ✔ {4} difficult to foresee ✔\n포인트 ▶ the better part of = ~의 대부분.",
 [['the better part of', '~의 대부분'], ['predict', '예측하다'], ['introduce', '도입하다'], ['tend to', '~하는 경향이 있다']])
T.fixed('다음 글의 밑줄 친 부분 중, 문맥상 낱말의 쓰임이 적절하지 <u>않은</u> 것은?', '34번 변형', BOX(
 "Most of us notice the " + CN(1, 'obvious') + " aspects of a new technology while missing the more subtle aspects. The microwave oven was introduced in the early 1980s and " + CN(2, 'revolutionized') + " food preparation. This shortening of preparation time was " + CN(3, 'liberating') + " for the cooks in the family. But the obvious implications of greater convenience made it easy to " + CN(4, 'overlook') + " the long-term implications. As time went on, " + CN(5, 'more and more') + " families sat down together to eat dinner."),
 ['obvious', 'revolutionized', 'liberating', 'overlook', 'more and more'], 5,
 "이유 ▶ 장기적인 영향을 간과했고, 오랜 준비가 필요한 식사가 과거의 사치가 되었다 → 함께 식사하는 가족은 '점점 줄었다' → <i>fewer and fewer</i>.\n오답 ▶ ① 뚜렷한 면을 알아챔 ✔ ② 음식 준비를 '혁신했다' ✔ ③ 요리하는 사람에게 '해방감' ✔ ④ 장기 영향을 '간과' ✔\n포인트 ▶ But 뒤 흐름(부정적 장기 영향)과 맞추기.",
 [['revolutionize', '혁신하다'], ['liberating', '해방감을 주는'], ['overlook', '간과하다'], ['implication', '영향, 결과']])
T.fixed('다음 글의 밑줄 친 부분 중, 어법상 <u>틀린</u> 것은?', '34번 변형', BOX(
 "The microwave oven " + CN(1, 'was introduced') + " in the early 1980s. Traditionally, one person spent the better part of an afternoon " + CN(2, 'fixing') + " an evening meal for a family. This shortening of preparation time was liberating for the cooks in the family, most of " + CN(3, 'them') + " tended to be women. But the obvious implications of greater convenience made it easy " + CN(4, 'to overlook') + " the long-term implications. Meals that " + CN(5, 'took') + " a long time to prepare became a luxury of the past."),
 ['was introduced', 'fixing', 'them', 'to overlook', 'took'], 3,
 "이유 ▶ 콤마 뒤에서 두 절을 접속사 없이 이으려면 관계대명사가 필요 → most of <i>whom</i>.\n오답 ▶ ① 전자레인지가 '소개된' 수동 ✔ ② spend + 시간 + -ing ✔ ④ 가목적어 it ~ 진목적어 to부정사 ✔ ⑤ 과거의 일 ✔\n포인트 ▶ 접속사 없이 '대명사 them'으로 절을 이을 수 없다 → 관계대명사 whom.",
 [['spend + 시간 + -ing', '~하느라 시간을 보내다'], ['convenience', '편리함'], ['luxury', '사치'], ['make it easy to', '~하기 쉽게 만들다']])
body, a = ABC(D[2], [D[3:5], D[5:7], D[7:10]], 'ACB')
T.fixed('주어진 글 다음에 이어질 글의 순서로 가장 적절한 것은?', '34번', body, OPTS_ORD, a,
 "이유 ▶ 주어진 글(전자레인지를 예로 들자) → (A) 1980년대 초 도입·전통적으로는 오후 내내 저녁 준비 → (C) Now 빨라져서 해방감, But 장기 영향을 간과 → (B) 시간이 지나며 함께 식사하는 가족이 줄고 예상하지 못함\n오답 ▶ (C)의 Now는 (A)의 Traditionally와 대비되므로 (A) 뒤\n포인트 ▶ Traditionally → Now → As time went on: 시간 흐름.",
 [['traditionally', '전통적으로'], ['shortening', '단축'], ['as time went on', '시간이 지나면서'], ['anticipate', '예상하다']], en=False)
T.flex('밑줄 친 <u>a luxury of the past</u>가 의미하는 바로 가장 적절한 것은?', '34번', BOX(P34.replace('a luxury of the past', U('a luxury of the past'))), [
 '예전에는 흔했지만 이제는 특별한 날에나 누리는 드문 것이 되었다.', '과거에는 비싼 재료로만 만들 수 있었다.',
 '부유한 집안에서만 먹던 음식이었다.', '오래 걸려서 아무도 원하지 않게 되었다.', '전자레인지로 더 쉽게 만들 수 있게 되었다.'],
 "이유 ▶ 예전에는 매일 오후 내내 저녁을 준비했지만, 이제 오래 걸리는 식사는 특별한 날(special occasions)을 빼면 보기 어려운 드문 것이 됨.\n오답 ▶ {1}·{2} luxury를 '비싼 것'으로만 해석한 함정 {3} 원하지 않게 된 것이 아니라 드물어진 것 {4} 반대로 전자레인지로 대체됨\n포인트 ▶ except perhaps for special occasions가 의미를 정해 준다.",
 [['luxury', '사치(품), 드물게 누리는 것'], ['occasion', '때, 행사'], ['except for', '~을 제외하고'], ['the past', '과거']], en=False)
T.table('다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 적절한 것은?', '34번', BOX(P34) + '\n' + SUM(
 'The <b>(A)</b> ' + BL + ' convenience of the microwave oven hid its long-term <b>(B)</b> ' + BL + ' on family meals.'),
 ['(A)', '(B)'], [['immediate', 'impact'], ['delayed', 'impact'], ['immediate', 'benefit'], ['limited', 'demand'], ['delayed', 'cost']],
 "이유 ▶ (A) the short-term, obvious implications of greater convenience → <i>immediate</i>(즉각적인) (B) the long-term implications ~ fewer families ate together → <i>impact</i>(영향)\n오답 ▶ delayed(지연된)는 short-term과 반대 / benefit(이점)은 가족 식사가 줄어든 결과와 맞지 않음 / limited·demand는 근거 없음\n포인트 ▶ short-term ↔ long-term 대비를 요약문에 옮긴다.",
 [['immediate', '즉각적인'], ['impact', '영향'], ['delayed', '지연된'], ['hide', '숨기다']],
 ko=['즉각적인 / 영향', '지연된 / 영향', '즉각적인 / 이점', '제한된 / 요구', '지연된 / 비용'])
g, body, a = INS(3, D[4:])
T.fixed('글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳은?', '34번', GIV(g) + '\n' + BOX(body), None, a,
 "이유 ▶ 장기적인 영향을 간과했다(overlook the long-term implications)는 문장 뒤에, 그 영향의 구체적 내용(함께 식사하는 가족이 줄어듦)이 오고 → 오래 걸리는 식사가 과거의 사치가 됨 → ③.\n오답 ▶ ①② 아직 편리함(장점) 이야기 중 ④⑤ 결과가 원인보다 늦게 나와 흐름이 어색\n포인트 ▶ As time went on: 장기 영향이 시작되는 신호.",
 [['as time went on', '시간이 지나면서'], ['fewer and fewer', '점점 더 적은'], ['sit down to', '~하려고 자리에 앉다'], ['implication', '영향']])
T.flex('30·34번 지문에 나온 단어와 영영풀이가 바르게 짝지어지지 <u>않은</u> 것은?', '종합', '', [
 ('subtle: very obvious and easy to notice', 'subtle: 매우 뚜렷하고 알아차리기 쉬운'),
 ('compensate: to make up for something bad', 'compensate: 나쁜 것을 만회하다'),
 ('inclined: likely or wanting to do something', 'inclined: ~할 것 같은, ~하고 싶은'),
 ('petition: a written request signed by many people', 'petition: 많은 사람이 서명한 서면 요청'),
 ('anticipate: to expect something to happen', 'anticipate: 어떤 일이 일어날 것을 예상하다')],
 "이유 ▶ subtle은 '미묘한, 알아차리기 어려운'. 매우 뚜렷하다는 obvious의 뜻.\n오답 ▶ {1} compensate 만회하다 ✔ {2} inclined ~하는 경향이 있는 ✔ {3} petition 청원 ✔ {4} anticipate 예상하다 ✔\n포인트 ▶ 34번의 핵심 대비 obvious ↔ subtle.",
 [['make up for', '만회하다'], ['request', '요청'], ['notice', '알아차리다'], ['expect', '예상하다']])
T.fixed('다음 (a)~(g) 중 어법상 <u>틀린</u> 것의 개수는?', '종합', BOX(
 "Some people are more likely to cheat after " + TG('a', 'purchasing') + " eco-friendly products, probably because they " + TG('b', 'feels') + " licensed to do so. People are inclined " + TG('c', 'to believe') + " in quick-fixes. When we focus on the obvious aspects of media, we miss the changes that " + TG('d', 'accumulates') + " over time. Most of us " + TG('e', 'notice') + " the obvious aspects of a new medium. The microwave oven was introduced in the early 1980s and " + TG('f', 'revolutionizing') + " food preparation. As time went on, fewer and fewer families " + TG('g', 'sat') + " down together to eat dinner."),
 ['1개', '2개', '3개', '4개', '5개'], 3,
 "이유 ▶ 틀린 것 (b) (d) (f) 3개. (b) 주어 they → <i>feel</i> (d) 선행사 the changes(복수) → <i>accumulate</i> (f) was introduced와 and로 병렬인 과거 동사 → <i>revolutionized</i>\n오답 ▶ (a) 전치사 + 동명사 ✔ (c) be inclined to + 동사원형 ✔ (e) Most of us → 복수 동사 ✔ (g) 과거의 일 ✔\n포인트 ▶ 관계대명사 that의 동사는 선행사에 수 일치.",
 [['be inclined to', '~하는 경향이 있다'], ['accumulate', '쌓이다'], ['revolutionize', '혁신하다'], ['medium', '매체']], en=False)
T.render()

# ═══════════════ 세트 3: 38·41~42 ═══════════════
E = ["Environmental psychologists make a distinction between the physical measurement of density (how many people are in a particular space) and crowding (the psychological feeling of not having enough space).",
 "Usually, high density is needed for the phenomenon of crowding, which makes people experience sensory overload, a lack of control, and rising stress and anxiety.",
 "However, some psychologists see crowding as neutral rather than invariably negative, and believe that people's moods and behaviors intensify as density increases.",
 "So if an individual is looking forward to a concert, say, the feeling of crowding enhances their enjoyment of the performance.",
 "But if they are dreading an event, crowding will make the person's experience of it even worse.",
 "Put into a community setting, crowding may accentuate the dominant behavior — an aggressive group may turn violent as density rises.",
 "Conversely, creating positive social spaces such as parks and pedestrian areas in high-density urban environments may help to lift the general mood and defuse tension."]
P38 = ' '.join(E)
F = ["The concept of \"choice architecture,\" popularized in behavioral economics, highlights how the design of the environment in which choices are made can significantly influence the decisions people make.",
 "Algorithms are, in essence, sophisticated architects of our digital environments.",
 "By curating what we see, what we are recommended, and what options are presented to us, they subtly, and sometimes not so subtly, nudge us towards particular paths.",
 "While nudges can be used for beneficial purposes, such as encouraging healthier habits, they also carry the potential for manipulation, particularly when the underlying objectives of the architects are not aligned with the well-being or autonomy of the individual.",
 "The question then becomes: how can we cultivate and protect our human agency in an increasingly algorithmic world?",
 "It requires a conscious effort to maintain critical engagement with the technologies we use.",
 "It means actively seeking out diverse perspectives, challenging algorithmic recommendations, and making deliberate choices that go against the predicted grain.",
 "It involves cultivating a healthy skepticism towards the seemingly objective outputs of algorithms and remembering that these systems are designed by humans with specific goals, and that their data is a reflection of past realities, not necessarily a prescription for future flourishing."]
P41 = ' '.join(F)
T = Test('3842', '38·41~42번', '밀도와 혼잡 · 선택 설계와 알고리즘', '38·41~42번',
 '범위: 38번(밀도와 혼잡, 혼잡은 기분을 강화한다) · 41~42번(알고리즘이 설계하는 선택 환경과 인간의 주체성). 지문은 원문을 일부 바꾼 것이 있어요. 선택지는 본문 표현을 다른 말로 바꿔 썼으니 뜻을 정확히 따져 보세요.')
T.fixed('다음 글의 밑줄 친 부분 중, 문맥상 낱말의 쓰임이 적절하지 <u>않은</u> 것은?', '38번 변형', BOX(
 "Environmental psychologists distinguish density from crowding, the " + CN(1, 'psychological') + " feeling of not having enough space. Crowding makes people experience sensory " + CN(2, 'overload') + " and rising stress. However, some psychologists see crowding as " + CN(3, 'neutral') + " rather than invariably negative. So if an individual is looking forward to a concert, the feeling of crowding " + CN(4, 'diminishes') + " their enjoyment of the performance. Creating parks in high-density urban environments may help to " + CN(5, 'defuse') + " tension."),
 ['psychological', 'overload', 'neutral', 'diminishes', 'defuse'], 4,
 "이유 ▶ 혼잡은 기분을 '강화'하므로, 콘서트를 기대하는 사람에게는 즐거움을 '높인다' → <i>enhances</i>.\n오답 ▶ ① '심리적' 느낌 ✔ ② 감각 '과부하' ✔ ③ '중립적' ✔ ⑤ 긴장을 '누그러뜨림' ✔\n포인트 ▶ 기대함(looking forward) + 기분 강화 → 즐거움 증가.",
 [['distinguish', '구별하다'], ['overload', '과부하'], ['diminish', '줄이다'], ['defuse', '누그러뜨리다']])
T.flex('다음 글의 주제로 가장 적절한 것은?', '38번', BOX(P38), [
 ('how crowding can intensify people\'s existing moods and behaviors', '혼잡이 사람들의 기존 기분과 행동을 어떻게 강화할 수 있는가'),
 ('why concerts should limit the number of people', '콘서트가 인원을 제한해야 하는 이유'),
 ('the physical methods of measuring urban density', '도시 밀도를 측정하는 물리적 방법'),
 ('the dangers of living alone in rural areas', '시골에서 혼자 사는 것의 위험'),
 ('how to design concert halls for better sound', '더 좋은 소리를 위한 공연장 설계법')],
 "이유 ▶ 혼잡은 늘 부정적인 게 아니라 중립적이며, 밀도가 높아지면 기분과 행동이 강해진다(intensify) → 기대하면 더 즐겁고, 두려우면 더 나쁘고, 공격적인 집단은 폭력적으로.\n오답 ▶ {1} 콘서트는 예시 {2} 측정 방법은 다루지 않는다 {3} 시골·혼자 사는 삶 언급 없음 {4} 소리 설계 없음\n포인트 ▶ However 뒤 문장이 주제문.",
 [['intensify', '강화하다'], ['existing', '기존의'], ['measure', '측정하다'], ['rural', '시골의']])
T.flex('다음 글의 내용과 일치하는 것은?', '38번', BOX(P38), [
 ('Crowding may make a dreaded event feel even more unpleasant.', '혼잡은 두려운 행사를 훨씬 더 불쾌하게 느끼게 만들 수 있다.'),
 ('Density and crowding mean exactly the same thing.', '밀도와 혼잡은 정확히 같은 뜻이다.'),
 ('All psychologists see crowding as always negative.', '모든 심리학자가 혼잡을 언제나 부정적으로 본다.'),
 ('Parks in crowded cities tend to increase tension.', '붐비는 도시의 공원은 긴장을 높이는 경향이 있다.'),
 ('Aggressive groups usually calm down as density rises.', '공격적인 집단은 밀도가 높아지면 보통 차분해진다.')],
 "이유 ▶ if they are dreading an event, crowding will make ~ even worse ✔\n오답 ▶ {1} make a distinction(구별한다) {2} some psychologists see crowding as neutral {3} defuse tension(긴장을 누그러뜨림) {4} may turn violent\n포인트 ▶ all / some, increase / defuse 같은 범위·방향 함정!",
 [['dread', '몹시 두려워하다'], ['exactly', '정확히'], ['tension', '긴장'], ['calm down', '진정하다']])
T.flex('다음 빈칸에 들어갈 말로 가장 적절한 것은?', '38번 변형', BOX(' '.join(E[:2]) + " However, some psychologists see crowding as " + BL + " rather than invariably negative, and believe that people's moods and behaviors intensify as density increases. " + ' '.join(E[3:5])), [
 ('neutral', '중립적인'), ('harmful', '해로운'), ('pleasant', '즐거운'), ('avoidable', '피할 수 있는'), ('permanent', '영구적인')],
 "이유 ▶ 늘 부정적인 것이 아니라(rather than invariably negative), 기대하면 즐거움이 커지고 두려우면 더 나빠진다 → 좋지도 나쁘지도 않은 '중립적인'.\n오답 ▶ {1} harmful은 negative와 같은 쪽 {2} pleasant면 두려운 행사가 더 나빠진다는 내용과 맞지 않음 {3}·{4} 근거 없음\n포인트 ▶ A rather than B + 뒤의 양쪽 예시(좋아짐/나빠짐) → 중립.",
 [['invariably', '언제나'], ['neutral', '중립적인'], ['avoidable', '피할 수 있는'], ['permanent', '영구적인']])
T.fixed('다음 글의 밑줄 친 부분 중, 어법상 <u>틀린</u> 것은?', '38번 변형', BOX(
 "Environmental psychologists make a distinction " + CN(1, 'between') + " density and crowding. Usually, high density is needed for the phenomenon of crowding, which makes people " + CN(2, 'to experience') + " sensory overload. However, some psychologists see crowding as neutral rather than invariably " + CN(3, 'negative') + ". But if they are dreading an event, crowding will make the person's experience of it even " + CN(4, 'worse') + ". Creating positive social spaces may " + CN(5, 'help') + " to lift the general mood."),
 ['between', 'to experience', 'negative', 'worse', 'help'], 2,
 "이유 ▶ 사역동사 make + 목적어 + 동사원형 → <i>experience</i>.\n오답 ▶ ① distinction between A and B ✔ ③ see A as B, rather than 앞뒤 형용사 병렬 ✔ ④ make + 목적어 + 형용사(비교급) ✔ ⑤ 조동사 may + 동사원형 ✔\n포인트 ▶ make·have·let + O + 동사원형.",
 [['distinction', '구별'], ['phenomenon', '현상'], ['sensory', '감각의'], ['lift', '들어 올리다, 북돋우다']])
T.table('(A), (B), (C)의 각 네모 안에서 어법에 맞는 표현으로 가장 적절한 것은?', '38번', BOX(
 "Environmental psychologists make a distinction between the physical measurement of density (<b>(A)</b> [ how / what ] many people are in a particular space) and crowding. … Some psychologists believe that people's moods and behaviors <b>(B)</b> [ intensify / intensifies ] as density increases. … Put into a community setting, crowding may accentuate the dominant behavior — an aggressive group may turn <b>(C)</b> [ violent / violently ] as density rises."),
 ['(A)', '(B)', '(C)'], [['how', 'intensify', 'violent'], ['what', 'intensify', 'violent'], ['how', 'intensifies', 'violent'], ['how', 'intensify', 'violently'], ['what', 'intensifies', 'violently']],
 "이유 ▶ (A) how many + 명사(얼마나 많은) → <i>how</i> (B) 주어 moods and behaviors(복수) → <i>intensify</i> (C) turn + 형용사(보어, ~하게 되다) → <i>violent</i>\n오답 ▶ what many는 불가 / intensifies는 단수 주어용 / violently는 부사라 보어 자리에 못 옴\n포인트 ▶ turn·become·get + 형용사.",
 [['measurement', '측정'], ['accentuate', '두드러지게 하다'], ['dominant', '지배적인'], ['aggressive', '공격적인']])
T.flex('밑줄 친 <u>crowding may accentuate the dominant behavior</u>가 의미하는 바로 가장 적절한 것은?', '38번', BOX(P38.replace('crowding may accentuate the dominant behavior', U('crowding may accentuate the dominant behavior'))), [
 '집단에 이미 있던 성향이 밀도가 높아지면 더 강하게 드러날 수 있다.', '혼잡하면 사람들이 지도자를 따르게 된다.',
 '혼잡은 모든 집단을 공격적으로 만든다.', '밀도가 높아지면 집단의 행동이 사라진다.', '혼잡한 곳에서는 소수 의견이 더 중요해진다.'],
 "이유 ▶ 공격적인 집단은 밀도가 높아지면 폭력적으로 변할 수 있다 = 원래 지배적인 성향(dominant behavior)이 더 두드러진다.\n오답 ▶ {1} dominant를 '지배자'로 착각 {2} '모든' 집단이 아니라 원래 공격적인 집단 {3} 사라지는 게 아니라 강해짐 {4} 소수 의견 언급 없음\n포인트 ▶ accentuate = intensify(강화하다)의 바꿔 쓴 말.",
 [['accentuate', '두드러지게 하다'], ['dominant', '지배적인, 주된'], ['setting', '환경, 배경'], ['turn violent', '폭력적으로 변하다']], en=False)
g, body, a = INS(2, E)
T.fixed('글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳은?', '38번', GIV(g) + '\n' + BOX(body), None, a,
 "이유 ▶ 앞 문장: 혼잡은 과부하·스트레스를 준다(부정적) → However로 '중립적이며 기분을 강화한다'는 다른 시각 → 다음 문장 So if ~ concert(그래서 기대하면 즐거움이 커진다)가 그 예시 → ②.\n오답 ▶ ① 혼잡의 부정적 영향이 나오기 전이라 However가 어색 ③~⑤ So if ~ 예시의 근거(기분 강화)가 앞에 없어짐\n포인트 ▶ However + 대조, So + 결과·예시.",
 [['neutral', '중립적인'], ['invariably', '언제나'], ['intensify', '강해지다'], ['density', '밀도']])
T.table('다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 적절한 것은?', '38번', BOX(P38) + '\n' + SUM(
 'Crowding does not always have <b>(A)</b> ' + BL + ' effects; instead, it tends to <b>(B)</b> ' + BL + ' whatever mood or behavior people already have.'),
 ['(A)', '(B)'], [['negative', 'intensify'], ['positive', 'intensify'], ['negative', 'reverse'], ['lasting', 'hide'], ['positive', 'reduce']],
 "이유 ▶ (A) neutral rather than invariably negative → <i>negative</i> (B) moods and behaviors intensify → <i>intensify</i>\n오답 ▶ positive: '늘 긍정적인 것은 아니다'는 본문의 대비와 다름 / reverse(뒤집다)·hide·reduce는 intensify와 반대\n포인트 ▶ not always A; instead B = 늘 A인 건 아니고 B.",
 [['reverse', '뒤집다'], ['lasting', '지속적인'], ['whatever', '어떤 ~이든'], ['tend to', '~하는 경향이 있다']],
 ko=['부정적인 / 강화하다', '긍정적인 / 강화하다', '부정적인 / 뒤집다', '지속적인 / 숨기다', '긍정적인 / 줄이다'])
# 41~42
T.flex('다음 글의 요지로 가장 적절한 것은?', '41~42번', BOX(P41), [
 '알고리즘이 선택 환경을 설계하는 시대에 주체성을 지키려면 의식적이고 비판적으로 기술을 대해야 한다.', '알고리즘은 객관적이므로 그 추천을 그대로 따르는 것이 좋다.',
 '넛지는 언제나 개인에게 해롭기 때문에 금지해야 한다.', '행동 경제학은 알고리즘을 설계하는 방법을 가르친다.', '과거 데이터만 있으면 미래를 정확히 예측할 수 있다.'],
 "이유 ▶ 알고리즘 = 선택 환경의 설계자(넛지) → 조종 가능성 → 주체성을 지키려면 비판적 관여·다양한 관점·회의적 태도가 필요.\n오답 ▶ {1} seemingly objective(겉으로만 객관적) {2} 이로운 목적으로도 쓰일 수 있다 {3} 행동 경제학은 개념의 출처일 뿐 {4} not necessarily a prescription for future\n포인트 ▶ 질문(how can we ~ protect our human agency?) 뒤가 요지.",
 [['agency', '주체성'], ['nudge', '넛지, 슬쩍 유도'], ['objective', '객관적인'], ['prescription', '처방']], en=False)
T.flex('다음 빈칸에 들어갈 말로 가장 적절한 것은?', '41~42번 변형', BOX(' '.join(F[:7]) + " It involves cultivating a healthy skepticism towards the seemingly " + BL + " outputs of algorithms and remembering that these systems are designed by humans with specific goals."), [
 ('objective', '객관적인'), ('random', '무작위의'), ('biased', '편향된'), ('outdated', '구식의'), ('emotional', '감정적인')],
 "이유 ▶ seemingly(겉으로 보기에) + 회의적 태도 + 사람이 특정 목표로 설계 → 겉으로는 '객관적인' 것처럼 보이는 결과.\n오답 ▶ {1} 무작위라면 설계자의 목표와 맞지 않음 {2} 편향된 것처럼 '보이는' 것을 의심하라는 건 논리가 반대 {3}·{4} 근거 없음\n포인트 ▶ seemingly A = 겉으로 A처럼 보이지만 실제로는 아닐 수 있음.",
 [['skepticism', '회의적 태도'], ['seemingly', '겉으로 보기에'], ['output', '결과물'], ['biased', '편향된']])
T.flex('다음 글의 내용과 일치하지 <u>않는</u> 것은?', '41~42번', BOX(P41), [
 ('Algorithms influence our choices only in obvious and visible ways.', '알고리즘은 뚜렷하고 눈에 보이는 방식으로만 우리의 선택에 영향을 준다.'),
 ('The idea of choice architecture became popular through behavioral economics.', '선택 설계라는 개념은 행동 경제학을 통해 널리 알려졌다.'),
 ('Nudges can be used to encourage healthier habits.', '넛지는 더 건강한 습관을 북돋우는 데 쓰일 수 있다.'),
 ('Protecting human agency requires a conscious effort.', '인간의 주체성을 지키려면 의식적인 노력이 필요하다.'),
 ('Algorithmic data reflects past realities.', '알고리즘의 데이터는 과거의 현실을 반영한다.')],
 "이유 ▶ they subtly, and sometimes not so subtly, nudge us(미묘하게, 때로는 덜 미묘하게) → '뚜렷한 방식으로만'은 불일치.\n오답 ▶ {1} popularized in behavioral economics ✔ {2} encouraging healthier habits ✔ {3} It requires a conscious effort ✔ {4} a reflection of past realities ✔\n포인트 ▶ only가 붙은 선택지는 본문과 꼼꼼히 대조!",
 [['popularize', '대중화하다'], ['behavioral economics', '행동 경제학'], ['conscious', '의식적인'], ['reflect', '반영하다']])
T.fixed('다음 글의 밑줄 친 부분 중, 문맥상 낱말의 쓰임이 적절하지 <u>않은</u> 것은?', '41~42번 변형', BOX(
 "Algorithms are " + CN(1, 'sophisticated') + " architects of our digital environments. By " + CN(2, 'curating') + " what we see, they nudge us towards particular paths. Nudges can be used for " + CN(3, 'beneficial') + " purposes, but they also carry the potential for manipulation when the objectives of the architects are not " + CN(4, 'aligned') + " with the well-being of the individual. Protecting our human agency requires a conscious effort to maintain " + CN(5, 'passive') + " engagement with the technologies we use."),
 ['sophisticated', 'curating', 'beneficial', 'aligned', 'passive'], 5,
 "이유 ▶ 주체성을 지키려면 기술과 '비판적인' 관계를 유지해야 → <i>critical</i>. passive(수동적인)는 반대.\n오답 ▶ ① '정교한' 설계자 ✔ ② 보는 것을 '선별해서' ✔ ③ '이로운' 목적 ✔ ④ 목표가 개인의 행복과 '일치하지' 않을 때 ✔\n포인트 ▶ 주체성(agency) ↔ 수동성(passive).",
 [['sophisticated', '정교한'], ['curate', '선별하다'], ['aligned with', '~와 일치하는'], ['manipulation', '조종']])
T.fixed('다음 글의 밑줄 친 부분 중, 어법상 <u>틀린</u> 것은?', '41~42번 변형', BOX(
 "The concept of \"choice architecture,\" " + CN(1, 'popularized') + " in behavioral economics, highlights how the design of the environment in " + CN(2, 'which') + " choices are made can influence decisions. By " + CN(3, 'curating') + " what we see, algorithms nudge us towards particular paths. Protecting our agency means actively seeking out diverse perspectives, challenging algorithmic recommendations, and " + CN(4, 'make') + " deliberate choices. These systems " + CN(5, 'are designed') + " by humans with specific goals."),
 ['popularized', 'which', 'curating', 'make', 'are designed'], 4,
 "이유 ▶ seeking, challenging과 and로 병렬 → <i>making</i>.\n오답 ▶ ① 개념이 '대중화된' 수동 분사 ✔ ② 전치사 in + which ✔ ③ 전치사 By + 동명사 ✔ ⑤ 시스템이 '설계되는' 수동 ✔\n포인트 ▶ A, B, and C 병렬은 형태를 맞춘다.",
 [['concept', '개념'], ['highlight', '강조하다'], ['perspective', '관점'], ['deliberate', '의도적인']])
body, a = ABC(F[0], [F[1:3], F[3:5], F[5:7]], 'CBA')
T.fixed('주어진 글 다음에 이어질 글의 순서로 가장 적절한 것은?', '41~42번', body, OPTS_ORD, a,
 "이유 ▶ 주어진 글(선택 설계: 환경 설계가 결정에 영향) → (C) 알고리즘은 디지털 환경의 설계자, 선별해서 넛지 → (B) 넛지는 이롭지만 조종 가능성, 그래서 질문: 주체성을 어떻게 지킬까 → (A) It(그것)은 의식적 노력·다양한 관점 찾기\n오답 ▶ (A)의 It은 (B)의 질문에 대한 답이므로 (B) 뒤\n포인트 ▶ 개념 → 적용(알고리즘) → 문제 제기(질문) → 해결.",
 [['architect', '설계자'], ['nudge', '슬쩍 유도하다'], ['agency', '주체성'], ['engagement', '관여']], en=False)
T.flex('밑줄 친 <u>making deliberate choices that go against the predicted grain</u>이 의미하는 바로 가장 적절한 것은?', '41~42번', BOX(P41.replace('making deliberate choices that go against the predicted grain', U('making deliberate choices that go against the predicted grain'))), [
 '알고리즘이 예측하고 권하는 대로만 따르지 않고 일부러 다른 선택을 하는 것', '알고리즘이 추천하는 상품을 가장 먼저 사는 것',
 '곡물을 기를 때 예측된 날씨를 무시하는 것', '모든 기술 사용을 완전히 끊는 것', '다른 사람의 선택을 그대로 따라 하는 것'],
 "이유 ▶ the predicted grain = 알고리즘이 예측한 흐름. 그것을 거슬러(go against) 의도적으로 선택한다 = 추천을 무조건 따르지 않는 것.\n오답 ▶ {1} 추천을 따르는 것은 반대 {2} grain을 '곡물'로 착각한 함정 {3} 기술을 끊으라는 말은 없음(비판적 관여) {4} 따라 하기는 반대\n포인트 ▶ go against the grain = 흐름(관습)을 거스르다.",
 [['deliberate', '의도적인'], ['go against the grain', '흐름을 거스르다'], ['predicted', '예측된'], ['recommendation', '추천']], en=False)
T.table('다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 적절한 것은?', '41~42번', BOX(P41) + '\n' + SUM(
 'Because algorithms <b>(A)</b> ' + BL + ' the environments in which we make choices, protecting our agency requires <b>(B)</b> ' + BL + ' engagement with technology.'),
 ['(A)', '(B)'], [['design', 'critical'], ['ignore', 'critical'], ['design', 'passive'], ['copy', 'emotional'], ['ignore', 'constant']],
 "이유 ▶ (A) Algorithms are ~ sophisticated architects of our digital environments → <i>design</i> (B) maintain critical engagement → <i>critical</i>\n오답 ▶ ignore는 설계자 역할과 반대 / passive는 critical과 반대 / copy·emotional·constant는 근거 없음\n포인트 ▶ 원인(알고리즘이 환경 설계) → 해결(비판적 관여).",
 [['design', '설계하다'], ['engagement', '관여'], ['passive', '수동적인'], ['constant', '끊임없는']],
 ko=['설계하다 / 비판적인', '무시하다 / 비판적인', '설계하다 / 수동적인', '베끼다 / 감정적인', '무시하다 / 끊임없는'])
g, body, a = INS(1, F[:7])
T.fixed('글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳은?', '41~42번', GIV(g) + '\n' + BOX(body), None, a,
 "이유 ▶ 다음 문장의 they(그것들)가 가리킬 복수 명사가 필요 → 주어진 문장의 Algorithms. 선택 설계 개념 소개 바로 뒤 ①.\n오답 ▶ ②~⑤ they가 무엇인지 앞에서 알 수 없게 됨\n포인트 ▶ 대명사(they)의 짝을 먼저 찾는다.",
 [['in essence', '본질적으로'], ['sophisticated', '정교한'], ['architect', '설계자'], ['digital', '디지털의']])
T.flex('38·41~42번 지문에 나온 단어와 영영풀이가 바르게 짝지어지지 <u>않은</u> 것은?', '종합', '', [
 ('skepticism: complete trust in something', 'skepticism: 무언가에 대한 완전한 신뢰'),
 ('density: the number of people in a given area', 'density: 일정 지역 안의 사람 수'),
 ('accentuate: to make something more noticeable', 'accentuate: 무언가를 더 눈에 띄게 하다'),
 ('defuse: to make a situation less tense', 'defuse: 상황을 덜 긴장되게 하다'),
 ('autonomy: the ability to make your own decisions', 'autonomy: 스스로 결정하는 능력')],
 "이유 ▶ skepticism은 '의심, 회의적인 태도'. 완전한 신뢰(trust)는 반대.\n오답 ▶ {1} density 밀도 ✔ {2} accentuate 두드러지게 하다 ✔ {3} defuse 누그러뜨리다 ✔ {4} autonomy 자율성 ✔\n포인트 ▶ 반의어로 바꾼 영영풀이를 찾는다.",
 [['tense', '긴장된'], ['noticeable', '눈에 띄는'], ['given', '정해진'], ['trust', '신뢰']])
T.fixed('다음 (a)~(g) 중 어법상 <u>틀린</u> 것의 개수는?', '종합', BOX(
 "Density is how many people " + TG('a', 'are') + " in a particular space. Crowding, which " + TG('b', 'make') + " people experience sensory overload, usually needs high density. But if people are " + TG('c', 'dreading') + " an event, crowding makes it worse. By " + TG('d', 'curate') + " what we see, algorithms nudge us towards particular paths. Nudges can " + TG('e', 'be used') + " for beneficial purposes. The question is how we can cultivate and " + TG('f', 'protecting') + " our human agency. These systems are " + TG('g', 'designed') + " by humans with specific goals."),
 ['1개', '2개', '3개', '4개', '5개'], 3,
 "이유 ▶ 틀린 것 (b) (d) (f) 3개. (b) 선행사 Crowding(단수) → <i>makes</i> (d) 전치사 By + 동명사 → <i>curating</i> (f) can cultivate and protect: 조동사 뒤 동사원형 병렬 → <i>protect</i>\n오답 ▶ (a) many people(복수) ✔ (c) 진행형 are dreading ✔ (e) 넛지가 '쓰이는' 수동 ✔ (g) 시스템이 '설계되는' 수동 ✔\n포인트 ▶ 콤마 + which의 동사는 앞 명사에 수 일치.",
 [['density', '밀도'], ['crowding', '혼잡'], ['curate', '선별하다'], ['cultivate', '기르다']], en=False)
T.render()
