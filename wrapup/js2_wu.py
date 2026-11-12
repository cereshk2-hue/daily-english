# 11/12 중산고2 Wrap-up 4세트 — 9월 학평 19~22 / 23·24·26·27 / 29·30 + 미래엔(김성연) L4 본문 — wu_js2.py 빌더
# 24·29·30번은 같은 시험이라 안곡고 세트(ag_wu.py)에서 검수 끝난 문항을 골라 다시 씀(재사용 문장 시작 줄 번호로 고름)
from wu_js2 import *
OPTS_ORD = ['(A) − (C) − (B)', '(B) − (A) − (C)', '(B) − (C) − (A)', '(C) − (A) − (B)', '(C) − (B) − (A)']
def ABC(given, chunks, seq):
    lab = dict(zip(seq, chunks))
    body = GIV(given) + '\n' + BOX('</p><p>'.join('<b>(%s)</b> %s' % (L, ' '.join(lab[L])) for L in 'ABC'))
    return body, OPTS_ORD.index(' − '.join('(%s)' % L for L in seq)) + 1
def INS(given_idx, sents):
    rest = [s for i, s in enumerate(sents) if i != given_idx]
    assert len(rest) in (5, 6), len(rest)
    body = rest[0] + ''.join(GP(k + 1) + (rest[k + 1] if k + 1 < len(rest) else '') for k in range(5))
    return sents[given_idx], body, given_idx

AGL = open('/home/claude/srcrepo/wrapup/ag_wu.py', encoding='utf-8').read().split('\n')
def AG(*starts):
    """ag_wu.py에서 그 줄에서 시작하는 문항(바로 앞 INS/ABC 줄 포함)을 그대로 실행"""
    for st in starts:
        i = st - 1; assert AGL[i].startswith('T.'), (st, AGL[i][:40])
        j = i + 1
        while j < len(AGL) and not re.match(r'(T\.|T = |g, body|body, a|#|$)', AGL[j]): j += 1
        pre = AGL[i - 1] if re.match(r'(g, body|body, a)', AGL[i - 1]) else ''
        exec(pre + '\n' + '\n'.join(AGL[i:j]), globals())
# 안곡고 세트의 지문 변수 (A=24, B=29, C=30)
exec('\n'.join(l for l in AGL[16:31]), globals())   # A, P24, B, P29
_s = '\n'.join(AGL); exec(_s[_s.index('C = ["Some people'):_s.index('D = ["When we focus')], globals())   # C, P30

# ═══════════════ 세트 1: 19·20·21·22 ═══════════════
S19 = ["I ran into the music room, breathing heavily.", "The rest of the band were sitting with long faces.", "Immy looked up at me and shook her head.", "I sank into a chair.",
 "I had truly believed we would make it; our audition had been flawless.", "My chest felt heavy as I asked, \"So, who won?\"", "I was holding back my tears.",
 "\"A band called A Happy Accident. They were quite good,\" she said calmly.", "A moment later, a big smile spread across Immy's face, and the others began to cheer.",
 "\"Wait, what? That's us!\" I said.", "Immy laughed and said, \"Since you were late, we decided to play a joke on you! We made it!\"", "I was filled with joy.",
 "We jumped up and hugged each other.", "My heart was racing with excitement."]
P19 = ' '.join(S19)
S20 = ["Only when you're happy that you've done the best you can for your story should you show it to someone else.",
 "You may well want to show it to your nearest and dearest, and that's fine, but in most cases you shouldn't look to their reading for any great benefit to your work.",
 "The most valuable feedback is likely to come from other sources: you should choose readers for their critical insight, not their closeness to you.",
 "Fellow writers are ideal, but don't imagine that any writer will do.",
 "If you are part of a writers' circle or class, you'll know whose writing you admire, and if you've had feedback in the past you'll know whose opinions have been helpful — and whose have not."]
P20 = ' '.join(S20)
S21 = ["A meeting in a flexible-time culture like those found in South America, parts of Europe, Africa, and the Middle East is more like an evergreen tree.",
 "An agenda with a meeting start time and a topic will probably be circulated before the meeting.", "This will serve as the trunk of the tree.",
 "But there's no expectation that the meeting will progress in a linear manner.",
 "What seemed like a priority last week when the agenda was crafted is not necessarily the priority right now — so discussion may branch off in a new direction.",
 "Other branches may sprout as some members have urgent phone calls that take them in and out of the meeting.",
 "Or sub-groups may form within the room to discuss timely subjects linked in some way to the main meeting trunk.",
 "In flexible-time cultures, it seems clear that the most productive meetings grow in unpredictable ways, and the effective manager is flexible and professional enough to capitalize on priorities and changing needs as they arise.",
 "Interruptions, agenda changes, and frequent shifts in direction are seen as natural and necessary."]
P21 = ' '.join(S21)
S22 = ["When we are \"always on\" we are constantly ingesting content — reading alerts and texts, liking, checking emails, downloading, uploading, upgrading, updating, deleting, submitting responses, and posting.",
 "If we do it while we are eating, our multi-tasking is overloading us.", "As our will attempts to digest the virtual content its forces are diverted from the physical content, our food.",
 "It's easy to eat a sandwich in a minute while talking on the phone.", "Some people are skilled at doing both at the same time.",
 "Others write a half-hearted, shorthand text while they hurriedly eat their sandwich at the same time.",
 "The result can be a misunderstood text with the need for further clarifying texts and the beginnings of nervous indigestion.", "Eat your sandwich. Taste it. Let it go down. Then text."]
P22 = ' '.join(S22)

T = Test('1922', '19~22번', '오디션 결과 · 피드백 독자 고르기 · 유연한 회의 · 먹을 때는 먹기만', '19~22번',
 '범위: 19번(오디션 결과를 기다리는 심경 변화) · 20번(작품을 보여 줄 독자 고르기) · 21번(유연한 시간 문화의 회의) · 22번(먹으면서 하는 디지털 멀티태스킹). 지문은 원문을 일부 바꾼 것이 있어요. 선택지는 본문 표현을 다른 말로 바꿔 썼으니 뜻을 정확히 따져 보세요.')
# 19
T.flex('다음 글에 드러난 \'I\'의 심경 변화로 가장 적절한 것은?', '19번', BOX(P19), [
 ('disappointed → delighted', '실망한 → 아주 기쁜'), ('relieved → annoyed', '안도한 → 짜증 난'), ('excited → bored', '신난 → 지루한'),
 ('nervous → indifferent', '초조한 → 무관심한'), ('confident → regretful', '자신 있는 → 후회하는')],
 "이유 ▶ 앞부분: 부원들의 시무룩한 얼굴, 가슴이 무겁고 눈물을 참음(실망) → 뒷부분: 우승은 바로 우리였다는 말에 기쁨으로 가득 차고 심장이 뜀(기쁨).\n오답 ▶ {1} 안도한 적도, 짜증 난 적도 없다 {2} 처음부터 신났던 것이 아니고 지루해지지도 않았다 {3} 마지막은 무관심이 아니라 흥분 {4} 오디션에 자신 있었던 것은 맞지만 마지막은 후회가 아니다\n포인트 ▶ 심경 변화는 앞(long faces, holding back my tears)과 뒤(filled with joy, racing with excitement)의 단서를 각각 찾는다.",
 [['long face', '시무룩한 얼굴'], ['sink into', '~에 털썩 주저앉다'], ['flawless', '흠 없는, 완벽한'], ['hold back', '(눈물 등을) 참다']])
T.flex('다음 글의 내용과 일치하는 것은?', '19번', BOX(P19), [
 ('The narrator arrived at the music room later than the other members.', '\'나\'는 다른 부원들보다 늦게 음악실에 도착했다.'),
 ('Immy told the narrator the truth about the result from the start.', 'Immy는 처음부터 \'나\'에게 결과에 대해 사실대로 말했다.'),
 ('The narrator thought the band\'s audition had gone poorly.', '\'나\'는 밴드의 오디션이 잘 안 됐다고 생각했다.'),
 ('A Happy Accident was the name of a rival band.', 'A Happy Accident는 경쟁 밴드의 이름이었다.'),
 ('The other members remained silent after Immy smiled.', '다른 부원들은 Immy가 웃은 뒤에도 조용히 있었다.')],
 "이유 ▶ Since you were late(네가 늦어서) → '나'가 가장 늦게 도착했다 ✔\n오답 ▶ {1} 처음에는 진 것처럼 장난을 쳤다 {2} our audition had been flawless(완벽했다) {3} That's us!(그건 우리야) → 우리 밴드 이름 {4} the others began to cheer(환호하기 시작했다)\n포인트 ▶ 장난(play a joke) 장면에서 '처음 말'과 '진짜 사실'을 구분!",
 [['narrator', '화자, 서술자'], ['from the start', '처음부터'], ['rival', '경쟁자, 경쟁하는'], ['remain silent', '조용히 있다']])
T.fixed('다음 글의 밑줄 친 부분 중, 어법상 <u>틀린</u> 것은?', '19번 변형', BOX(
 "I ran into the music room, " + CN(1, 'breathing') + " heavily. The rest of the band " + CN(2, 'were') + " sitting with long faces. I had truly believed we " + CN(3, 'would make') + " it; our audition had been flawless. My chest felt " + CN(4, 'heavily') + " as I asked, \"So, who won?\" Immy laughed and said, \"" + CN(5, 'Since') + " you were late, we decided to play a joke on you!\""),
 ['breathing', 'were', 'would make', 'heavily', 'Since'], 4,
 "이유 ▶ 감각동사 feel 뒤에는 형용사 보어 → <i>heavy</i>.\n오답 ▶ ① 동시 동작을 나타내는 분사구문(숨을 쉬면서) ✔ ② the rest of + 집합명사(the band) → 부원들 여럿을 가리켜 복수 동사 가능 ✔ ③ 과거의 믿음 속 미래 → would ✔ ⑤ 이유의 접속사 since(~이므로) ✔\n포인트 ▶ feel / look / sound / seem + 형용사 (부사 ❌)",
 [['breathe heavily', '숨을 가쁘게 쉬다'], ['make it', '해내다, 성공하다'], ['chest', '가슴'], ['play a joke on', '~에게 장난치다']])
T.fixed('다음 글의 밑줄 친 부분 중, 문맥상 낱말의 쓰임이 적절하지 <u>않은</u> 것은?', '19번 변형', BOX(
 "I sank into a chair. I had truly believed we would make it; our audition had been " + CN(1, 'flawless') + ". I was " + CN(2, 'holding back') + " my tears. \"A band called A Happy Accident. They were quite good,\" she said " + CN(3, 'calmly') + ". A moment later, a big smile spread across Immy's face, and the others began to " + CN(4, 'cheer') + ". \"Since you were late, we decided to play a joke on you! We made it!\" I was filled with " + CN(5, 'sorrow') + "."),
 ['flawless', 'holding back', 'calmly', 'cheer', 'sorrow'], 5,
 "이유 ▶ 장난이었고 사실은 우리가 우승(We made it!) → '기쁨'으로 가득 차야 한다 → <i>joy</i>. 바로 뒤의 껴안고 심장이 뛰는 장면과도 맞지 않는다.\n오답 ▶ ① 오디션이 '완벽했다' ✔ ② 눈물을 '참았다' ✔ ③ 장난이라 일부러 '차분하게' 말함 ✔ ④ 부원들이 '환호하기' 시작 ✔\n포인트 ▶ 반전(We made it!) 뒤의 감정 어휘는 긍정!",
 [['sorrow', '슬픔'], ['calmly', '차분하게'], ['cheer', '환호하다'], ['be filled with', '~으로 가득 차다']])
T.flex('밑줄 친 <u>we decided to play a joke on you</u>가 뜻하는 내용으로 가장 적절한 것은?', '19번', BOX(P19.replace('we decided to play a joke on you', U('we decided to play a joke on you'))), [
 '우승 소식을 일부러 숨기고 떨어진 척하며 \'나\'를 놀렸다.', '늦게 온 벌로 \'나\'를 공연에서 빼기로 했다.', '다른 밴드에게 우승을 양보하기로 했다.',
 '오디션 결과를 아직 몰라서 \'나\'에게 거짓말을 했다.', '\'나\' 대신 다른 사람에게 노래를 부르게 했다.'],
 "이유 ▶ 시무룩한 얼굴·고개 젓기·다른 밴드 이름 말하기 → 사실은 우리가 우승(That's us! / We made it!) → 결과를 숨기고 진 척한 장난.\n오답 ▶ {1} 공연에서 빼는 이야기는 없다 {2} 양보한 것이 아니라 우리가 이겼다 {3} 결과를 이미 알고 있었다 {4} 노래를 대신 부르는 이야기는 없다\n포인트 ▶ 밑줄 의미는 앞의 행동(long faces, shook her head)과 뒤의 사실(We made it!)을 함께 본다.",
 [['decide to', '~하기로 결정하다'], ['pretend', '~인 척하다'], ['give up', '양보하다, 포기하다'], ['instead of', '~ 대신에']], en=False)
# 20
T.flex('다음 글에서 필자가 주장하는 바로 가장 적절한 것은?', '20번', BOX(P20), [
 '자신의 글을 보여 줄 독자는 친밀함이 아니라 비판적 통찰력을 기준으로 골라야 한다.', '글은 가족과 친구에게 먼저 보여 주고 격려를 받아야 한다.',
 '작가 모임에 들어가야만 좋은 피드백을 받을 수 있다.', '모든 동료 작가의 의견을 똑같이 존중해야 한다.', '이야기를 완성하기 전에 되도록 많은 사람에게 보여 주어야 한다.'],
 "이유 ▶ you should choose readers for their critical insight, not their closeness to you(친밀함이 아니라 비판적 통찰력으로 독자를 골라라)가 주장.\n오답 ▶ {1} 가족·친구에게 보여 주는 것은 괜찮지만 큰 도움을 기대하지 말라고 했다 {2} 작가 모임은 하나의 예 {3} 아무 작가나 되는 것이 아니다(don't imagine that any writer will do) {4} 최선을 다한 뒤에만 보여 주라고 했다\n포인트 ▶ should / not A but B 문장이 주장의 핵심.",
 [['critical insight', '비판적 통찰력'], ['closeness', '친밀함'], ['encouragement', '격려'], ['fellow writer', '동료 작가']], en=False)
T.flex('다음 빈칸에 들어갈 말로 가장 적절한 것은?', '20번 변형', BOX(
 S20[0] + ' ' + S20[1] + " The most valuable feedback is likely to come from other sources: you should choose readers for their " + BL + ", not their closeness to you. " + ' '.join(S20[3:])), [
 ('critical insight', '비판적 통찰력'), ('warm support', '따뜻한 지지'), ('close friendship', '가까운 우정'), ('reading speed', '읽는 속도'), ('kind words', '친절한 말')],
 "이유 ▶ 가까운 사람의 읽기에는 큰 도움을 기대하지 말고, 'closeness(친밀함)가 아닌' 기준 → 글을 날카롭게 봐 줄 '비판적 통찰력'.\n오답 ▶ {1}·{2}·{4} 모두 친밀한 사람에게서 기대하는 것으로 closeness 쪽에 가깝다 {3} 읽는 속도는 근거 없음\n포인트 ▶ A, not B: A와 B는 대비되는 기준.",
 [['valuable', '가치 있는'], ['feedback', '피드백, 의견'], ['source', '원천, 출처'], ['nearest and dearest', '가장 가깝고 소중한 사람들']])
T.table('(A), (B), (C)의 각 네모 안에서 어법에 맞는 표현으로 가장 적절한 것은?', '20번', BOX(
 "Only when you're happy that you've done the best you can for your story <b>(A)</b> [ should you show / you should show ] it to someone else. … Fellow writers are ideal, but don't imagine that any writer <b>(B)</b> [ will do / to do ]. If you are part of a writers' circle or class, you'll know <b>(C)</b> [ whose / who's ] writing you admire."),
 ['(A)', '(B)', '(C)'], [['should you show', 'will do', 'whose'], ['you should show', 'will do', 'whose'], ['should you show', 'to do', 'whose'], ['should you show', 'will do', "who's"], ['you should show', 'to do', "who's"]],
 "이유 ▶ (A) Only + 부사절이 문장 앞 → 주절은 도치(조동사 + 주어 + 동사) → <i>should you show</i> (B) that절에 동사가 필요 → <i>will do</i>(충분하다, 괜찮다) (C) 뒤의 명사 writing을 꾸미는 소유격 → <i>whose</i>\n오답 ▶ you should show는 도치를 놓침 / to do는 동사 자리가 아님 / who's = who is라 명사 앞에 못 온다\n포인트 ▶ Only when ~ 이 앞에 오면 주절 도치!",
 [['do', '(자동사) 충분하다, 괜찮다'], ['ideal', '이상적인'], ['admire', '동경하다, 감탄하다'], ['circle', '모임, 동아리']],
 ko=['도치 / 동사 / 소유격', '도치 안 함 / 동사 / 소유격', '도치 / to부정사 / 소유격', '도치 / 동사 / who is', '도치 안 함 / to부정사 / who is'])
body, a = ABC(S20[0], [S20[1:2], S20[2:4], S20[4:5]], 'BAC')
T.fixed('주어진 글 다음에 이어질 글의 순서로 가장 적절한 것은?', '20번', body, OPTS_ORD, a,
 "이유 ▶ 주어진 글(최선을 다한 뒤에 보여 줘라) → (B) 가까운 사람에게 보여 주는 건 괜찮지만 큰 도움은 기대하지 마라 → (A) 가장 가치 있는 피드백은 '다른 곳(other sources)'에서: 비판적 통찰력으로 골라라 + 동료 작가가 이상적이지만 아무나는 아니다 → (C) 모임에 있다면 누구의 글·의견이 도움이 되는지 알 것이다.\n오답 ▶ (A)의 other sources는 (B)의 '가까운 사람들'과 대비되므로 (B) 뒤 / (C)의 whose opinions는 (A)의 '아무 작가나 되는 게 아니다' 뒤\n포인트 ▶ other(다른), any writer(아무 작가) 같은 연결 단서를 잡는다.",
 [['look to A for B', 'B를 A에게 기대하다'], ['benefit', '이익, 도움'], ['will do', '충분하다'], ['opinion', '의견']], en=False)
T.flex('다음 글의 내용과 일치하지 <u>않는</u> 것은?', '20번', BOX(P20), [
 ('Any fellow writer can give you useful feedback.', '어떤 동료 작가든 유용한 피드백을 줄 수 있다.'),
 ('It is natural to want to show your work to people close to you.', '가까운 사람들에게 작품을 보여 주고 싶은 것은 자연스럽다.'),
 ('Past feedback can tell you whose opinions are helpful.', '과거의 피드백으로 누구의 의견이 도움이 되는지 알 수 있다.'),
 ('Readers should be chosen for their critical insight.', '독자는 비판적 통찰력을 보고 골라야 한다.'),
 ('You should show your story only after doing your best on it.', '이야기에 최선을 다한 뒤에만 그것을 보여 주어야 한다.')],
 "이유 ▶ don't imagine that any writer will do(아무 작가나 괜찮을 거라고 생각하지 마라) → '어떤 동료 작가든'은 불일치.\n오답 ▶ {1} You may well want to show it ~ and that's fine ✔ {2} you'll know whose opinions have been helpful ✔ {3} choose readers for their critical insight ✔ {4} Only when ~ done the best ~ should you show it ✔\n포인트 ▶ may well = ~하는 것도 당연하다.",
 [['may well', '~하는 것도 당연하다'], ['natural', '자연스러운'], ['helpful', '도움이 되는'], ['useful', '유용한']])
# 21
T.flex('밑줄 친 <u>more like an evergreen tree</u>가 의미하는 바로 가장 적절한 것은?', '21번', BOX(P21.replace('more like an evergreen tree', U('more like an evergreen tree'))), [
 '의제라는 줄기를 중심으로, 논의가 예측할 수 없게 여러 방향으로 가지를 뻗어 간다.', '회의가 정해진 순서에 따라 한 줄로 차례차례 진행된다.',
 '회의가 일 년 내내 같은 주제로 반복된다.', '회의 시작 시간과 끝나는 시간이 정확히 지켜진다.', '회의는 자연 속 야외에서 편안하게 열린다.'],
 "이유 ▶ 의제 = 나무의 줄기(trunk), 논의가 새 방향으로 가지를 뻗고(branch off) 다른 가지가 싹틈(sprout) → 줄기는 있지만 예측할 수 없게 자라는 회의.\n오답 ▶ {1} no expectation ~ in a linear manner(일직선 진행을 기대하지 않음) {2} '상록수'를 늘 같다는 뜻으로 오해한 함정 {3} 시간 엄수는 반대 문화 {4} 야외는 근거 없음\n포인트 ▶ 비유(tree)는 뒤에 이어지는 trunk·branch·sprout로 풀린다.",
 [['evergreen', '상록의'], ['trunk', '(나무의) 줄기'], ['branch off', '갈라져 나가다'], ['sprout', '싹트다, 돋아나다']], en=False)
T.flex('다음 글의 내용과 일치하는 것은?', '21번', BOX(P21), [
 ('An agenda is likely to be shared before the meeting.', '의제는 회의 전에 공유될 가능성이 높다.'),
 ('Discussion is expected to follow the agenda in a straight line.', '논의는 의제를 따라 일직선으로 진행될 것으로 기대된다.'),
 ('Members are not allowed to leave the meeting for phone calls.', '구성원들은 전화 때문에 회의를 떠날 수 없다.'),
 ('Sub-groups never form inside the meeting room.', '회의실 안에서는 소그룹이 절대 생기지 않는다.'),
 ('Effective managers stick strictly to last week\'s priorities.', '유능한 관리자는 지난주의 우선순위를 엄격히 고수한다.')],
 "이유 ▶ An agenda ~ will probably be circulated before the meeting ✔\n오답 ▶ {1} no expectation ~ in a linear manner {2} phone calls that take them in and out of the meeting(들락날락함) {3} sub-groups may form within the room {4} capitalize on priorities and changing needs as they arise(그때그때 생기는 요구를 활용)\n포인트 ▶ circulate = (문서를) 돌리다, 배부하다.",
 [['circulate', '배부하다, 돌리다'], ['be allowed to', '~하는 것이 허용되다'], ['stick to', '~을 고수하다'], ['strictly', '엄격하게']])
T.fixed('다음 글의 밑줄 친 부분 중, 문맥상 낱말의 쓰임이 적절하지 <u>않은</u> 것은?', '21번 변형', BOX(
 "There's no expectation that the meeting will progress in a " + CN(1, 'linear') + " manner. What seemed like a priority last week is not " + CN(2, 'necessarily') + " the priority right now — so discussion may branch off in a new direction. Other branches may " + CN(3, 'sprout') + " as some members have urgent phone calls. The effective manager is flexible enough to " + CN(4, 'capitalize on') + " priorities and changing needs as they arise. Interruptions, agenda changes, and frequent shifts in direction are seen as " + CN(5, 'unnatural') + " and necessary."),
 ['linear', 'necessarily', 'sprout', 'capitalize on', 'unnatural'], 5,
 "이유 ▶ 유연한 시간 문화에서는 중단·의제 변경·방향 전환을 '자연스럽고' 필요한 것으로 본다 → <i>natural</i>. and necessary와도 짝이 맞아야 한다.\n오답 ▶ ① 일직선으로 진행될 거라는 기대가 '없다' ✔ ② '반드시' ~인 것은 아니다(부분 부정) ✔ ③ 다른 가지가 '싹튼다' ✔ ④ 변화를 '활용한다' ✔\n포인트 ▶ A and B로 묶인 두 형용사는 같은 방향(natural and necessary).",
 [['linear', '일직선의, 선형의'], ['not necessarily', '반드시 ~인 것은 아닌'], ['capitalize on', '~을 활용하다'], ['interruption', '중단, 방해']])
T.fixed('다음 글의 밑줄 친 부분 중, 어법상 <u>틀린</u> 것은?', '21번 변형', BOX(
 "An agenda with a meeting start time and a topic " + CN(1, 'will probably be circulated') + " before the meeting. What " + CN(2, 'seemed') + " like a priority last week when the agenda " + CN(3, 'was crafted') + " is not necessarily the priority right now. Other branches may sprout as some members have urgent phone calls that " + CN(4, 'take') + " them in and out of the meeting. Or sub-groups may form within the room to discuss timely subjects " + CN(5, 'linking') + " in some way to the main meeting trunk."),
 ['will probably be circulated', 'seemed', 'was crafted', 'take', 'linking'], 5,
 "이유 ▶ 주제들이 주요 회의 줄기에 '연결된' 것 → 과거분사 <i>linked</i>.\n오답 ▶ ① 의제가 '배부되는' 수동 ✔ ② What절의 동사(과거) ✔ ③ 의제가 '만들어지던' 수동 ✔ ④ 선행사 phone calls(복수) → take ✔\n포인트 ▶ link A to B → 수동으로 쓰면 (be) linked to.",
 [['agenda', '의제, 안건'], ['craft', '공들여 만들다'], ['urgent', '긴급한'], ['timely', '시의적절한']])
g, body, a = INS(3, S21[:7])
T.fixed('글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳은?', '21번', GIV(g) + '\n' + BOX(body), None, a,
 "이유 ▶ 의제가 나무의 '줄기' 역할을 한다(This will serve as the trunk) → But 일직선 진행은 기대하지 않는다 → 이어서 우선순위가 바뀌어 논의가 새 방향으로 가지를 뻗는다. 따라서 ③.\n오답 ▶ ①② 줄기(의제) 이야기가 끝나기 전 ④⑤ 이미 가지 뻗기(branch off) 예시가 시작된 뒤라 But의 대비가 어색하다\n포인트 ▶ But = 앞 내용(줄기·의제)과 반대되는 내용(일직선 아님)의 시작.",
 [['expectation', '기대'], ['progress', '진행되다'], ['manner', '방식'], ['serve as', '~의 역할을 하다']])
# 22
T.flex('다음 글의 요지로 가장 적절한 것은?', '22번', BOX(P22), [
 '음식을 먹을 때는 디지털 기기 사용을 멈추고 먹는 일에 집중해야 한다.', '멀티태스킹 능력을 길러 바쁜 시간을 아껴야 한다.', '문자 메시지는 짧고 간단하게 보내는 것이 좋다.',
 '전화 통화를 하면서 식사하면 대화가 더 즐거워진다.', '소화 불량은 주로 음식의 종류 때문에 생긴다.'],
 "이유 ▶ 먹으면서 콘텐츠를 소비하면 과부하·오해받는 문자·신경성 소화 불량 → Eat your sandwich. Taste it. ~ Then text.(먹고 나서 문자하라)\n오답 ▶ {1} 멀티태스킹은 오히려 과부하의 원인 {2} 성의 없이 줄여 쓴 문자는 오해를 부른다 {3} 즐거워진다는 말은 없다 {4} 원인은 음식 종류가 아니라 동시에 하는 것\n포인트 ▶ 명령문으로 끝나는 글 → 마지막 명령문이 요지.",
 [['concentrate on', '~에 집중하다'], ['indigestion', '소화 불량'], ['multi-tasking', '멀티태스킹, 동시에 여러 일 하기'], ['overload', '과부하를 주다']], en=False)
T.flex('다음 빈칸에 들어갈 말로 가장 적절한 것은?', '22번 변형', BOX(
 S22[0] + ' ' + S22[1] + " As our will attempts to digest the virtual content its forces are " + BL + " the physical content, our food. " + ' '.join(S22[3:])), [
 ('diverted from', '~로부터 다른 데로 돌려진다'), ('focused on', '~에 집중된다'), ('added to', '~에 더해진다'), ('protected by', '~에 의해 보호된다'), ('combined with', '~와 합쳐진다')],
 "이유 ▶ 가상 콘텐츠를 '소화'하느라 힘을 쓰면 진짜 음식에서는 그 힘이 '빠져나간다(다른 데로 돌려진다)' → 멀티태스킹 과부하.\n오답 ▶ {1} 음식에 집중되면 과부하·소화 불량이 생길 이유가 없다 {2}·{3}·{4} 힘이 나뉜다는 흐름과 반대이거나 관계없음\n포인트 ▶ digest(소화하다)를 콘텐츠와 음식에 함께 쓴 말장난 → 힘은 한쪽으로 쏠린다.",
 [['digest', '소화하다'], ['virtual', '가상의'], ['divert', '(방향을) 돌리다'], ['force', '힘']])
T.fixed('다음 글의 밑줄 친 부분 중, 문맥상 낱말의 쓰임이 적절하지 <u>않은</u> 것은?', '22번 변형', BOX(
 "When we are \"always on\" we are " + CN(1, 'constantly') + " ingesting content. If we do it while we are eating, our multi-tasking is " + CN(2, 'overloading') + " us. Some people are " + CN(3, 'skilled') + " at doing both at the same time. Others write a " + CN(4, 'careful') + ", shorthand text while they hurriedly eat their sandwich at the same time. The result can be a " + CN(5, 'misunderstood') + " text with the need for further clarifying texts."),
 ['constantly', 'overloading', 'skilled', 'careful', 'misunderstood'], 4,
 "이유 ▶ 샌드위치를 급하게 먹으며 줄여 쓴 문자 → '성의 없는' 문자라 오해를 부른다 → <i>half-hearted</i>. careful(신중한)이면 오해받는 결과와 맞지 않는다.\n오답 ▶ ① '끊임없이' 섭취 ✔ ② 멀티태스킹이 '과부하를 준다' ✔ ③ 둘 다 하는 데 '능숙한' 사람도 있다 ✔ ⑤ '오해받는' 문자 ✔\n포인트 ▶ 결과(misunderstood, clarifying texts)에서 거꾸로 원인 어휘를 확인!",
 [['ingest', '섭취하다'], ['half-hearted', '성의 없는, 마음이 내키지 않는'], ['shorthand', '줄여 쓴, 약칭의'], ['hurriedly', '서둘러']])
T.table('(A), (B), (C)의 각 네모 안에서 어법에 맞는 표현으로 가장 적절한 것은?', '22번', BOX(
 "When we are \"always on\" we are constantly <b>(A)</b> [ ingesting / ingested ] content. … Some people are skilled at <b>(B)</b> [ doing / to do ] both at the same time. … The result can be a misunderstood text with the need for further <b>(C)</b> [ clarifying / clarified ] texts."),
 ['(A)', '(B)', '(C)'], [['ingesting', 'doing', 'clarifying'], ['ingested', 'doing', 'clarifying'], ['ingesting', 'to do', 'clarifying'], ['ingesting', 'doing', 'clarified'], ['ingested', 'to do', 'clarified']],
 "이유 ▶ (A) 우리가 콘텐츠를 '섭취하고 있는' 능동 진행형 → <i>ingesting</i> (B) 전치사 at 뒤 → 동명사 <i>doing</i> (C) 앞의 오해를 '설명해 주는' 문자 → 현재분사 <i>clarifying</i>\n오답 ▶ ingested는 우리가 섭취'당하는' 뜻 / to do는 전치사 뒤 불가 / clarified는 문자가 설명'되는' 뜻\n포인트 ▶ 꾸밈을 받는 명사가 하는 일(능동) → -ing, 당하는 일(수동) → p.p.",
 [['be skilled at', '~에 능숙하다'], ['clarify', '분명히 설명하다'], ['further', '추가의'], ['content', '콘텐츠, 내용']],
 ko=['섭취하는 / 동명사 / 설명해 주는', '섭취되는 / 동명사 / 설명해 주는', '섭취하는 / to부정사 / 설명해 주는', '섭취하는 / 동명사 / 설명된', '섭취되는 / to부정사 / 설명된'])
T.flex('밑줄 친 <u>Eat your sandwich. Taste it. Let it go down. Then text.</u>가 뜻하는 내용으로 가장 적절한 것은?', '22번', BOX(P22.replace('Eat your sandwich. Taste it. Let it go down. Then text.', U('Eat your sandwich. Taste it. Let it go down. Then text.'))), [
 '먹는 일에만 온전히 집중해 다 먹은 다음에 문자를 보내라.', '샌드위치를 먹으면서 동시에 답장을 보내라.', '음식을 먹기 전에 먼저 문자를 확인하라.',
 '빨리 먹고 서둘러 일로 돌아가라.', '문자를 보낼 때 음식 사진을 함께 보내라.'],
 "이유 ▶ 먹고(Eat) → 맛보고(Taste) → 삼킨(Let it go down) '다음에(Then)' 문자 → 한 번에 한 가지만, 먹는 동안은 먹는 데 집중.\n오답 ▶ {1} 동시에 하는 것이 바로 문제 {2} 문자를 먼저 하라는 순서가 아니다 {3} 서두르는 것(hurriedly)은 비판 대상 {4} 근거 없음\n포인트 ▶ Then(그다음에) = 동시가 아니라 차례대로.",
 [['taste', '맛보다'], ['go down', '(음식이) 넘어가다'], ['text', '문자를 보내다'], ['fully', '온전히']], en=False)
T.render()

# ═══════════════ 세트 2: 23·24·26·27 ═══════════════
S23 = ["Music can bring us into a very comfortable rhythm, and it can be satisfying in and of itself.", "Most of the time, however, we want something more to happen.",
 "There needs to be a process that creates tension and drives the movement towards something in particular.", "The excitement that arises in this process creates satisfaction and pleasure.",
 "This is seen in the measureless prelude as well.", "But there the tension might be caused by the ambiguity of the rhythm.",
 "Therefore, the fluid movement in the prelude usually creates a tension that can be released in the subsequent movement with a set rhythm.",
 "This, in turn, creates new and other types of tensions, where the rhythm is unambiguous and predictable, but where unexpected chords and modulations create drama and an experience of development in the piece."]
P23 = ' '.join(S23)
S26 = ["Frederick Law Olmsted, known as the father of American landscape architecture, was born in 1822.",
 "When Olmsted was young, he often went on trips to the countryside with his father, who loved scenery.",
 "At age 14, he was preparing himself to study at Yale College, but he could not enter due to a severe sumac poisoning that damaged his eyesight.",
 "Instead of attending a college, he gained experience working as a clerk, a sailor, and a farmer.",
 "In 1858, he worked with Calvert Vaux and won the design competition for New York City's Central Park with the \"Greensward Plan.\"",
 "During the Civil War, Olmsted served as General Secretary of the United States Sanitary Commission.",
 "Although he passed away in 1903, his sons and successors continued his design philosophy.",
 "In 1979, the National Park Service designated his home and office in Brookline, Massachusetts, as a National Historic Site to honor his legacy."]
P26 = ' '.join(S26)
P27 = ('<b>Ashwood Dunes Reforestation Event</b></p><p>Join us for a meaningful morning at the annual Ashwood Dunes Reforestation. Volunteers will plant native tree seedlings to help restore the local environment. No special skills required, feel free to join us.</p><p>'
 '■ <b>When and Where</b>: September 5th, 2026, 8 a.m.–11 a.m., Ashwood Dunes Wilderness<br>■ <b>Participation Fee</b>: Free<br>'
 '■ <b>Rewards</b>: All participants will get a commemorative badge.<br>&nbsp;&nbsp;– Plant 5 trees: Receive a reusable water bottle<br>&nbsp;&nbsp;– Plant 10 or more trees: Receive a T-shirt<br>'
 '■ <b>Registration</b>: Online registration is encouraged, but on-site sign-ups will be available on the day of the event.<br>'
 '■ <b>Event Guidelines</b>: Bring a hat and gloves; shovels and water will be prepared. Follow instructions from the event staff.</p><p>For more information, please visit www.ashwooddunes.com.')

T = Test('2327', '23·24·26·27번', '음악의 긴장과 해소 · 주의력 문해력 · 조경가 Olmsted · 숲 가꾸기 행사', '23·24·26·27번',
 '범위: 23번(음악에서 긴장이 만들어지고 풀리는 과정) · 24번(주의를 빼앗도록 설계된 디지털 환경을 알아보는 교육) · 26번(Frederick Law Olmsted) · 27번(Ashwood Dunes 숲 가꾸기 행사). 지문은 원문을 일부 바꾼 것이 있어요. 선택지는 본문 표현을 다른 말로 바꿔 썼으니 뜻을 정확히 따져 보세요.')
# 23
T.flex('다음 글의 주제로 가장 적절한 것은?', '23번', BOX(P23), [
 ('how tension in music is created and released to give pleasure', '음악에서 긴장이 어떻게 만들어지고 풀려 즐거움을 주는가'),
 ('why measureless preludes contain no tension at all', '마디 없는 전주곡에 긴장이 전혀 없는 이유'),
 ('the importance of keeping one comfortable rhythm in music', '음악에서 하나의 편안한 리듬을 유지하는 것의 중요성'),
 ('ways to compose chords that avoid any surprise', '어떤 놀라움도 피하는 화음을 작곡하는 방법'),
 ('the history of the prelude in classical music', '클래식 음악에서 전주곡의 역사')],
 "이유 ▶ 편안한 리듬만으로는 부족 → 긴장을 만들고 몰고 가는 과정이 만족·즐거움을 줌 → 전주곡의 모호한 리듬이 만든 긴장이 다음 악장에서 풀리고, 다시 예상 못한 화음이 새 긴장을 만든다.\n오답 ▶ {1} 전주곡에도 긴장이 있다(리듬의 모호함) {2} 편안한 리듬 그 이상을 원한다고 했다 {3} 예상치 못한 화음이 극적 효과를 준다 {4} 역사 이야기는 없다\n포인트 ▶ tension(긴장) → released(해소) → new tensions의 반복이 글의 뼈대.",
 [['tension', '긴장(감)'], ['release', '풀어 주다, 해소하다'], ['prelude', '전주곡'], ['compose', '작곡하다']])
T.flex('다음 빈칸에 들어갈 말로 가장 적절한 것은?', '23번 변형', BOX(
 S23[0] + ' ' + S23[1] + " There needs to be a process that creates " + BL + " and drives the movement towards something in particular. " + ' '.join(S23[3:6])), [
 ('tension', '긴장'), ('comfort', '편안함'), ('silence', '침묵'), ('repetition', '반복'), ('balance', '균형')],
 "이유 ▶ 편안한 리듬 '이상의 무언가'가 일어나야 함(however) → 흥분을 일으키는 과정 → '긴장'. 뒤 문장의 the tension(그곳에서 긴장은)이 같은 말을 받는다.\n오답 ▶ {1} 편안함은 however 앞의 내용(이미 있는 것) {2}·{3}·{4} 흥분(excitement)을 만드는 과정과 거리가 멀다\n포인트 ▶ 빈칸 뒤에 같은 단어(the tension)가 다시 나오는지 확인!",
 [['in and of itself', '그 자체로'], ['drive', '몰고 가다'], ['in particular', '특정한'], ['arise', '생기다, 일어나다']])
T.fixed('다음 글의 밑줄 친 부분 중, 문맥상 낱말의 쓰임이 적절하지 <u>않은</u> 것은?', '23번 변형', BOX(
 "The excitement that arises in this process creates " + CN(1, 'satisfaction') + " and pleasure. This is seen in the " + CN(2, 'measureless') + " prelude as well. But there the tension might be caused by the " + CN(3, 'ambiguity') + " of the rhythm. Therefore, the fluid movement in the prelude usually creates a tension that can be " + CN(4, 'released') + " in the subsequent movement with a set rhythm. This, in turn, creates new types of tensions, where the rhythm is unambiguous and " + CN(5, 'unpredictable') + ", but where unexpected chords and modulations create drama."),
 ['satisfaction', 'measureless', 'ambiguity', 'released', 'unpredictable'], 5,
 "이유 ▶ 다음 악장은 정해진 리듬(set rhythm)이라 리듬이 분명하고 '예측 가능한' 대신(but), 예상 못한 화음이 긴장을 만든다 → <i>predictable</i>.\n오답 ▶ ① 흥분이 '만족'을 만든다 ✔ ② '마디 없는' 전주곡 ✔ ③ 리듬의 '모호함'이 긴장을 만든다 ✔ ④ 긴장이 다음 악장에서 '해소된다' ✔\n포인트 ▶ unambiguous and ___ , but unexpected ~ : but 앞은 '예측 가능', 뒤는 '예상 밖'.",
 [['ambiguity', '모호함'], ['subsequent', '그다음의'], ['modulation', '조바꿈, 전조'], ['unambiguous', '분명한']])
T.fixed('다음 글의 밑줄 친 부분 중, 어법상 <u>틀린</u> 것은?', '23번 변형', BOX(
 "There needs " + CN(1, 'to be') + " a process that " + CN(2, 'creates') + " tension. The excitement that " + CN(3, 'arises') + " in this process creates satisfaction and pleasure. Therefore, the fluid movement in the prelude usually creates a tension that can " + CN(4, 'release') + " in the subsequent movement with a set rhythm. This, in turn, creates new types of tensions, " + CN(5, 'where') + " the rhythm is unambiguous and predictable."),
 ['to be', 'creates', 'arises', 'release', 'where'], 4,
 "이유 ▶ 긴장이 '해소되는' 것 → 수동 <i>be released</i>. release는 '풀어 주다'라는 타동사라 목적어 없이 쓰면 틀린다.\n오답 ▶ ① There needs to be ~ (~이 있어야 한다) ✔ ② 선행사 a process(단수) ✔ ③ arise는 자동사(생기다) → 능동 ✔ ⑤ 뒤가 완전한 절 → 관계부사 where ✔\n포인트 ▶ arise(자동사, 수동 ❌) ↔ release(타동사, 목적어 없으면 수동).",
 [['fluid', '유동적인'], ['set rhythm', '정해진 리듬'], ['in turn', '이번에는, 다시'], ['process', '과정']])
T.flex('다음 글의 내용과 일치하는 것은?', '23번', BOX(P23), [
 ('In a measureless prelude, tension may come from an unclear rhythm.', '마디 없는 전주곡에서 긴장은 분명하지 않은 리듬에서 생길 수 있다.'),
 ('Music cannot be satisfying without any tension.', '음악은 긴장이 없으면 만족감을 줄 수 없다.'),
 ('The movement after the prelude usually has no set rhythm.', '전주곡 다음 악장에는 보통 정해진 리듬이 없다.'),
 ('Unexpected chords make a piece feel less dramatic.', '예상치 못한 화음은 곡을 덜 극적으로 느끼게 한다.'),
 ('Listeners usually want nothing more than a comfortable rhythm.', '듣는 사람은 보통 편안한 리듬 이상을 원하지 않는다.')],
 "이유 ▶ the tension might be caused by the ambiguity of the rhythm ✔\n오답 ▶ {1} it can be satisfying in and of itself(그 자체로도 만족을 줄 수 있다) {2} the subsequent movement with a set rhythm {3} unexpected chords ~ create drama {4} Most of the time, however, we want something more\n포인트 ▶ ambiguity = unclear, 모호함.",
 [['unclear', '분명하지 않은'], ['satisfying', '만족감을 주는'], ['dramatic', '극적인'], ['nothing more than', '~에 불과한, ~ 이상은 아닌']])
body, a = ABC(S23[0], [S23[1:4], S23[4:6], S23[6:8]], 'BCA')
T.fixed('주어진 글 다음에 이어질 글의 순서로 가장 적절한 것은?', '23번', body, OPTS_ORD, a,
 "이유 ▶ 주어진 글(편안한 리듬도 그 자체로 만족) → (B) however, 대개는 그 이상을 원함: 긴장을 만드는 과정이 즐거움을 줌 → (C) This(긴장의 즐거움)는 마디 없는 전주곡에서도 보임, 다만 그곳의 긴장은 리듬의 모호함에서 → (A) Therefore 전주곡의 긴장이 다음 악장에서 풀리고, 이것이 다시 새 긴장을 만든다.\n오답 ▶ (C)의 This is seen ~ as well은 앞에 긴장 이야기가 있어야 함 / (A)의 Therefore, the prelude는 전주곡이 먼저 소개된 뒤\n포인트 ▶ however(전환) → as well(추가) → Therefore(결과) 연결어 순서.",
 [['as well', '또한'], ['measureless', '마디가 없는'], ['therefore', '그러므로'], ['development', '전개, 발전']], en=False)
# 24 (안곡고 세트 검수 문항 재사용: 주제·일치·빈칸·어법·삽입·요약)
AG(39, 47, 55, 61, 77, 80)
# 26
T.flex('Frederick Law Olmsted에 관한 다음 글의 내용과 일치하지 <u>않는</u> 것은?', '26번', BOX(P26), [
 ('He entered Yale College at the age of 14.', '14세에 Yale College에 입학했다.'),
 ('He often traveled to the countryside with his father when young.', '어렸을 때 아버지와 함께 자주 시골로 여행을 갔다.'),
 ('He worked as a sailor and a farmer instead of going to college.', '대학에 가는 대신 선원과 농부로 일했다.'),
 ('He won the Central Park design competition with Calvert Vaux.', 'Calvert Vaux와 함께 Central Park 설계 공모전에서 당선되었다.'),
 ('His home and office became a National Historic Site in 1979.', '그의 집과 사무실은 1979년에 국가 사적지가 되었다.')],
 "이유 ▶ he was preparing ~ but he could not enter due to a severe sumac poisoning → 준비했지만 입학하지 '못했다'.\n오답 ▶ {1} went on trips to the countryside with his father ✔ {2} Instead of attending a college ~ a clerk, a sailor, and a farmer ✔ {3} worked with Calvert Vaux and won ✔ {4} In 1979 ~ designated ~ National Historic Site ✔\n포인트 ▶ 인물 글: 'prepare(준비)'와 'enter(입학)'처럼 비슷하지만 다른 사실을 구분.",
 [['landscape architecture', '조경 (건축)'], ['sumac poisoning', '옻나무 중독'], ['eyesight', '시력'], ['designate', '지정하다']])
T.flex('Frederick Law Olmsted에 관한 다음 글의 내용과 일치하는 것은?', '26번', BOX(P26), [
 '남북 전쟁 동안 미국 위생 위원회의 사무총장으로 일했다.', '1858년에 혼자서 Central Park 설계 공모전에 당선되었다.', '사고로 다쳐서 시력이 나빠졌다.',
 '그가 세상을 떠난 뒤 그의 디자인 철학은 잊혔다.', '1822년에 국립공원관리청에서 일하기 시작했다.'],
 "이유 ▶ During the Civil War, Olmsted served as General Secretary of the United States Sanitary Commission ✔\n오답 ▶ {1} worked with Calvert Vaux(함께) {2} 사고가 아니라 옻나무 중독(sumac poisoning) {3} his sons and successors continued his design philosophy(이어 감) {4} 1822년은 태어난 해\n포인트 ▶ 연도와 사건을 하나씩 짝지어 확인한다.",
 [['Civil War', '(미국) 남북 전쟁'], ['serve as', '~으로 일하다'], ['successor', '후계자'], ['philosophy', '철학']], en=False)
T.fixed('다음 글의 밑줄 친 부분 중, 어법상 <u>틀린</u> 것은?', '26번 변형', BOX(
 "Frederick Law Olmsted, " + CN(1, 'known') + " as the father of American landscape architecture, was born in 1822. When Olmsted was young, he often went on trips to the countryside with his father, " + CN(2, 'which') + " loved scenery. At age 14, he could not enter Yale College due to a severe sumac poisoning " + CN(3, 'that') + " damaged his eyesight. Instead of " + CN(4, 'attending') + " a college, he gained experience working as a clerk, a sailor, and a farmer. Although he passed away in 1903, his sons and successors " + CN(5, 'continued') + " his design philosophy."),
 ['known', 'which', 'that', 'attending', 'continued'], 2,
 "이유 ▶ 선행사 his father는 사람 → 계속적 용법 관계대명사 <i>who</i>.\n오답 ▶ ① Olmsted가 '알려진' 수동 분사구 ✔ ③ 선행사 poisoning(사물), 제한적 용법 that ✔ ④ 전치사 Instead of 뒤 동명사 ✔ ⑤ 주절의 과거 동사 ✔\n포인트 ▶ 사람 선행사 + 콤마 → , who (, which ❌ / , that ❌)",
 [['scenery', '경치'], ['severe', '심한'], ['clerk', '점원, 사무원'], ['pass away', '세상을 떠나다']])
T.flex('다음 빈칸에 들어갈 말로 가장 적절한 것은?', '26번 변형', BOX(
 ' '.join(S26[:6]) + " Although he passed away in 1903, his sons and successors " + BL + " his design philosophy. In 1979, the National Park Service designated his home and office in Brookline, Massachusetts, as a National Historic Site to honor his legacy."), [
 ('carried on', '이어 갔다'), ('gave up', '포기했다'), ('criticized', '비판했다'), ('forgot about', '잊어버렸다'), ('kept secret', '비밀로 했다')],
 "이유 ▶ Although(비록 ~지만) 그는 세상을 떠났'지만' → 그의 철학은 '계속 이어졌다'(continued). 뒤 문장의 유산을 기린다는 내용과도 연결.\n오답 ▶ {1}·{2}·{3}·{4} 모두 Although의 대비(죽었지만 → 남았다)를 깨뜨린다\n포인트 ▶ Although 절과 주절은 반대 방향.",
 [['carry on', '계속하다, 이어 가다'], ['legacy', '유산'], ['honor', '기리다'], ['criticize', '비판하다']])
# 27
T.flex('Ashwood Dunes Reforestation Event에 관한 다음 안내문의 내용과 일치하지 <u>않는</u> 것은?', '27번', BOX(P27), [
 '참가비는 심은 나무 수에 따라 다르다.', '자원봉사자들은 토종 나무 묘목을 심는다.', '특별한 기술이 없어도 참가할 수 있다.',
 '나무를 10그루 이상 심으면 티셔츠를 받는다.', '행사 당일 현장 등록이 가능하다.'],
 "이유 ▶ Participation Fee: Free(무료) → 나무 수에 따라 달라지는 것은 참가비가 아니라 보상(Rewards).\n오답 ▶ {1} plant native tree seedlings ✔ {2} No special skills required ✔ {3} Plant 10 or more trees: Receive a T-shirt ✔ {4} on-site sign-ups will be available ✔\n포인트 ▶ 안내문은 항목(Fee / Rewards)을 섞어 놓은 함정을 조심!",
 [['reforestation', '숲 가꾸기, 재조림'], ['native', '토종의'], ['seedling', '묘목'], ['participation fee', '참가비']], en=False)
T.flex('Ashwood Dunes Reforestation Event에 관한 다음 안내문의 내용과 일치하는 것은?', '27번', BOX(P27), [
 ('Shovels and water will be provided at the event.', '삽과 물은 행사에서 제공된다.'),
 ('Participants must bring their own shovels.', '참가자는 자신의 삽을 가져와야 한다.'),
 ('Only those who plant 5 trees will get a badge.', '나무 5그루를 심은 사람만 배지를 받는다.'),
 ('Online registration is required for everyone.', '모든 사람이 온라인으로 등록해야 한다.'),
 ('The event will be held in the afternoon.', '행사는 오후에 열린다.')],
 "이유 ▶ shovels and water will be prepared(준비되어 있다) ✔\n오답 ▶ {1} 가져올 것은 모자와 장갑 {2} All participants will get a commemorative badge(모든 참가자) {3} Online registration is encouraged(권장), 현장 등록도 가능 {4} 8 a.m.–11 a.m.(오전)\n포인트 ▶ encouraged(권장) ≠ required(필수).",
 [['provide', '제공하다'], ['commemorative', '기념하는'], ['require', '요구하다, 필수로 하다'], ['on-site', '현장의']])
T.flex('Ashwood Dunes Reforestation Event 안내문에서 언급되지 <u>않은</u> 것은?', '27번', BOX(P27), [
 ('the maximum number of participants', '최대 참가 인원'), ('the date and time of the event', '행사 날짜와 시간'), ('the participation fee', '참가비'),
 ('the rewards for planting trees', '나무를 심은 보상'), ('the items participants should bring', '참가자가 가져올 물건')],
 "이유 ▶ 인원 제한(최대 몇 명)은 어디에도 나오지 않는다.\n오답 ▶ {1} September 5th, 2026, 8 a.m.–11 a.m. {2} Free {3} badge, water bottle, T-shirt {4} a hat and gloves\n포인트 ▶ 언급되지 않은 것: 항목 제목(When and Where, Fee, Rewards, Registration, Guidelines)을 하나씩 지운다.",
 [['maximum', '최대의'], ['item', '물건, 항목'], ['reward', '보상'], ['guideline', '지침']])
T.fixed('다음 안내문의 밑줄 친 부분 중, 어법상 <u>틀린</u> 것은?', '27번 변형', BOX(
 "Volunteers will plant native tree seedlings to help " + CN(1, 'restore') + " the local environment. No special skills " + CN(2, 'required') + ", feel free to join us. All participants will get a " + CN(3, 'commemorative') + " badge. Online registration is encouraged, but on-site sign-ups will " + CN(4, 'be') + " available on the day of the event. Bring a hat and gloves; shovels and water will " + CN(5, 'prepare') + "."),
 ['restore', 'required', 'commemorative', 'be', 'prepare'], 5,
 "이유 ▶ 삽과 물이 '준비되는' 것 → 수동 <i>be prepared</i>.\n오답 ▶ ① help + (to) 동사원형 ✔ ② 기술이 '요구되는' 과거분사(No special skills (are) required) ✔ ③ 명사 badge를 꾸미는 형용사 ✔ ④ will + be available ✔\n포인트 ▶ 주어가 사물(shovels and water)이면 동사가 능동인지 수동인지 먼저 확인!",
 [['restore', '복원하다'], ['feel free to', '부담 없이 ~하다'], ['sign-up', '등록'], ['available', '이용할 수 있는']])
T.render()

# ═══════════════ 세트 3: 29·30 ═══════════════
T = Test('2930', '29·30번', '자본주의와 값싼 자연 · 도덕적 면허와 환경 죄책감', '29·30번',
 '범위: 29번(값싼 자연과 변경에 기대는 자본주의) · 30번(친환경 소비 뒤의 도덕적 면허와 환경 죄책감). 지문은 원문을 일부 바꾼 것이 있어요. 선택지는 본문 표현을 다른 말로 바꿔 썼으니 뜻을 정확히 따져 보세요.')
AG(87, 93, 101, 109, 114, 120, 123, 128, 135)   # 29번 9문항
AG(175, 180, 188, 196, 200, 205, 210, 216, 219)   # 30번 9문항
T.flex('29·30번 지문에 나온 단어와 영영풀이가 바르게 짝지어지지 <u>않은</u> 것은?', '종합', '', [
 ('compensate: to make a situation worse by causing more damage', 'compensate: 더 큰 피해를 일으켜 상황을 악화시키다'),
 ('inconsistency: a lack of agreement between two things', 'inconsistency: 두 가지 사이에 일치하지 않음'),
 ('petition: a written request signed by many people', 'petition: 많은 사람이 서명한 서면 요청'),
 ('dignity: the quality of being worthy of respect', 'dignity: 존중받을 가치가 있는 성질'),
 ('seize: to take something quickly and by force', 'seize: 무언가를 재빨리, 강제로 차지하다')],
 "이유 ▶ compensate는 '보상하다, 만회하다(to make up for something bad)'. 상황을 악화시킨다는 반대 뜻.\n오답 ▶ {1} inconsistency 불일치 ✔ {2} petition 청원(서) ✔ {3} dignity 존엄 ✔ {4} seize 빼앗다 ✔\n포인트 ▶ 영영풀이 문제는 뜻을 반대로 바꾼 풀이를 찾는다.",
 [['make up for', '만회하다'], ['agreement', '일치'], ['worthy of', '~할 가치가 있는'], ['by force', '강제로']])
T.fixed('다음 (a)~(g) 중 어법상 <u>틀린</u> 것의 개수는?', '종합', BOX(
 "Some people are more likely to cheat after " + TG('a', 'purchasing') + " eco-friendly products. Moral licensing has also " + TG('b', 'observed') + " in the context of cooperation for the good of the environment. People who experience eco-guilt " + TG('c', 'seeks') + " pro-environmental actions. They want to escape the guilt as quickly and " + TG('d', 'easily') + " as possible. Capitalism is a system in " + TG('e', 'which') + " islands of cash exchange exist. Workers' wages can be frozen, even " + TG('f', 'rolled') + " back. Frontiers offer places where the cheap work of humans can be " + TG('g', 'forcefully') + " taken."),
 ['1개', '2개', '3개', '4개', '5개'], 2,
 "이유 ▶ 틀린 것 (b) (c) 2개. (b) 도덕적 면허가 '관찰된' 것 → 수동 <i>has been observed</i> (c) 주어 People(복수) → <i>seek</i>\n오답 ▶ (a) 전치사 after 뒤 동명사 ✔ (d) as + 부사 + as possible, quickly와 병렬 ✔ (e) 전치사 + which ✔ (f) can be frozen, (be) rolled back 병렬 ✔ (g) 과거분사 taken을 꾸미는 부사 ✔\n포인트 ▶ 관계대명사 who 뒤 동사의 수는 선행사(People)에 맞춘다.",
 [['moral licensing', '도덕적 면허(착한 일 뒤 나쁜 일을 허락하는 심리)'], ['cooperation', '협력'], ['eco-guilt', '환경 죄책감'], ['cash exchange', '현금 거래']], en=False)
T.render()

# ═══════════════ 세트 4: 미래엔(김성연) L4 본문 ❶~❽ ═══════════════
HL4 = ('미래엔', '고2 영어Ⅱ 미래엔(김성연) Lesson 4 What-If Science', '미래엔(김성연) 영어Ⅱ', 'js2-mirae')
K1 = ["Have you ever wondered, \"What if I could run so fast that nobody could see me?\"", "If you have asked this kind of question, you may be ready to become the next Galileo.",
 "The Italian scientist Galileo Galilei is famous for a thought experiment, which is an imaginary experiment designed to explore a mathematical or scientific hypothesis.",
 "With only his thoughts, he demonstrated that objects with different masses should fall at the same speed when dropped from the same height in the absence of air resistance.",
 "With a hypothesis based on creativity and imagination, anyone can become a great scientist."]
K2 = ["The tallest man in recorded history was 272 cm tall, but have you ever wondered what would happen if humans could grow to enormous sizes like the giant in Jack and the Beanstalk?",
 "Unfortunately, the answer to this hypothetical question is that it is impossible due to the scale effect.",
 "When the length of an object doubles, its area increases by a factor of four (2x2), and its volume by a factor of eight (2x2x2).",
 "These changes can create many problems that would put the giant's life in danger."]
K3 = ["One issue is that the giant would not be able to stand properly on his own because of the weight pushing down on his feet.",
 "If a person's height increased ten times, his weight would increase by a factor of 1,000 (10x10x10) because weight changes in proportion to volume.",
 "However, the area of the feet supporting his body would only increase by a factor of 100 (10x10).",
 "This means that his feet would be under too much pressure to support the increased weight because the mass would have increased far more than the area of his feet."]
K4 = ["In addition, there is an issue of heat emission.",
 "Heat is generated in the human body, and it is constantly released from the surface of the skin to prevent heat from accumulating in the body.",
 "If a person's height were to increase ten times, the amount of heat generated would increase a thousand times in proportion to the body's volume.",
 "However, the surface area of the person's skin would only increase a hundred times, and as a result, not enough heat would be released from the body through the skin.",
 "This shows that while we may wish to grow as tall as a giant, we would not be able to survive in that form."]
K5 = ["\"O, swear not by the moon, the inconstant moon.\"", "This is a famous line from Romeo and Juliet.",
 "Juliet warns Romeo not to swear his love by the Moon as it may change just as the Moon changes its shape.",
 "Although its appearance changes, the Moon is always present in the night sky and plays a crucial role in regulating the length of the day on Earth as well as the Earth's seasons and weather patterns.",
 "Then, what would happen if there were no Moon?", "Without the Moon, our day would no longer be 24 hours.", "The Moon's gravity causes the Earth's ocean to rise and fall.",
 "Since the ocean is moving and the Earth is also spinning, friction occurs between them.", "This friction leads to a decrease in the rotation rate of the planet.",
 "Without the Moon, however, the Earth's rotation would not slow down, resulting in a change in the length of a day.",
 "According to some scientists, when the Earth first formed, there was no Moon and a day was only five hours long.", "This indicates that without the Moon, we would see the Sun rise every five hours."]
K6 = ["Additionally, the absence of the Moon would completely change weather patterns on Earth.", "We experience the beauty of different seasons because the Earth is tilted on its axis.",
 "The axis of rotation of the Earth is tilted at an angle of 23.5 degrees, and the Moon's gravity holds the Earth in place by stabilizing the tilt.",
 "However, if there were no Moon, the tilt could vary wildly between 0 and 85 degrees.", "Suppose the Earth were tilted at an angle of 60 degrees.",
 "The hemisphere of the Earth facing the Sun would receive much more energy from the sun than the other hemisphere.",
 "This could bring about extreme shifts in weather patterns, potentially making summers hotter and winters colder.", "If this trend continued, the Earth would become uninhabitable."]
K7 = ["Oxygen is a vital gas for life, making up 21 percent of the Earth's atmosphere.", "It is essential for breathing and is also necessary to burn common fuels like wood and oil to generate heat and light.",
 "Undoubtedly, it is an indispensable element for organisms on Earth.", "Then, would it be better to have a higher concentration of oxygen in the atmosphere?",
 "What would happen if the oxygen concentration were to double?", "While more oxygen may seem beneficial, it could have unexpected consequences, especially for insects.",
 "Insects, such as bees and dragonflies, do not have lungs and instead take in air through external openings called spiracles.",
 "Although insects can survive without lungs, their spiracles are not as efficient as lungs at taking in air."]
K8 = ["Therefore, with the current oxygen concentration, insects cannot evolve to be larger than their current size.",
 "If they were bigger in size, oxygen would not be able to reach the deepest parts of their bodies.",
 "However, if the concentration of oxygen were to double, insects could grow in size as oxygen would be more readily available.",
 "This increase in insect size could have a significant influence on the ecological environment, potentially disrupting the food chain.",
 "Dragonflies, for example, may become as large as eagles, altering the balance of predators and prey in the ecosystem.",
 "Fortunately, you wouldn't need to worry about giant insects chasing after you if this were to occur.",
 "If the oxygen concentration were to double, you would be able to run faster than you can right now.",
 "Considering that oxygen is used to break down energy so that muscles can use it, the increase in oxygen would help to use energy more efficiently and improve our capability for physical exercise.",
 "This leads us to expect that athletes would set new world records at the Olympics.",
 "While these three thought experiments offer interesting possibilities, it is important to consider that they are simply based on imagination and have not been tested through scientific research."]
J = ' '.join
T = Test('L4', 'L4 ❶~❽', 'What-If Science · 거인 · 달이 없다면 · 산소가 두 배라면', '본문 ❶~❽',
 '범위: 4과 본문 ❶~❽ (Galileo의 사고 실험 · 거인이 될 수 없는 이유 · 달이 없다면 · 산소 농도가 두 배라면). 지문은 본문을 일부 바꾼 것이 있어요. 선택지는 본문 표현을 다른 말로 바꿔 썼으니 뜻을 정확히 따져 보세요.', H=HL4)
# ❶
T.flex('다음 빈칸에 들어갈 말로 가장 적절한 것은?', '본문 ❶', BOX(
 J(K1[:3]) + " With only his thoughts, he demonstrated that objects with different masses should fall at " + BL + " when dropped from the same height in the absence of air resistance. " + K1[4]), [
 ('the same speed', '같은 속도로'), ('different speeds', '서로 다른 속도로'), ('a speed that depends on their mass', '질량에 따라 달라지는 속도로'),
 ('a slower speed than lighter objects', '더 가벼운 물체보다 느린 속도로'), ('the speed of sound', '소리의 속도로')],
 "이유 ▶ Galileo의 사고 실험: 공기 저항이 없으면 질량이 다른 물체도 같은 높이에서 '같은 속도로' 떨어진다.\n오답 ▶ {1}·{2}·{3} 모두 질량에 따라 속도가 달라진다는 뜻으로 사고 실험의 결론과 반대 {4} 근거 없음\n포인트 ▶ with different masses(다른 질량) ↔ the same speed(같은 속도)의 대비.",
 [['demonstrate', '입증하다'], ['mass', '질량'], ['in the absence of', '~이 없을 때'], ['air resistance', '공기 저항']])
T.fixed('다음 글의 밑줄 친 부분 중, 어법상 <u>틀린</u> 것은?', '본문 ❶ 변형', BOX(
 "If you " + CN(1, 'have asked') + " this kind of question, you may be ready to become the next Galileo. The Italian scientist Galileo Galilei is famous for a thought experiment, " + CN(2, 'that') + " is an imaginary experiment " + CN(3, 'designed') + " to explore a mathematical or scientific hypothesis. With only his thoughts, he demonstrated that objects with different masses should fall at the same speed when " + CN(4, 'dropped') + " from the same height. With a hypothesis " + CN(5, 'based') + " on creativity and imagination, anyone can become a great scientist."),
 ['have asked', 'that', 'designed', 'dropped', 'based'], 2,
 "이유 ▶ 콤마 뒤 계속적 용법에는 that을 쓸 수 없다 → <i>which</i>.\n오답 ▶ ① 경험의 현재완료 ✔ ③ 실험이 '설계된' 과거분사 ✔ ④ when (they are) dropped: 물체가 '떨어뜨려지는' 수동 ✔ ⑤ 가설이 창의성에 '근거한' 과거분사 ✔\n포인트 ▶ , which ⭕ / , that ❌",
 [['thought experiment', '사고 실험'], ['imaginary', '상상의'], ['hypothesis', '가설'], ['explore', '탐구하다']])
# ❷
T.flex('본문의 내용에 따를 때, 어떤 물체의 길이가 3배가 되면 그 용적(부피)은 몇 배가 되는가?', '본문 ❷', BOX(J(K2[1:])), [
 '27배', '9배', '6배', '3배', '81배'],
 "이유 ▶ 길이가 2배 → 면적 4배(2×2), 용적 8배(2×2×2). 같은 원리로 길이 3배 → 용적 3×3×3 = 27배.\n오답 ▶ {1} 9배는 면적(3×3) {2} 6배·{3} 3배는 길이를 곱하는 원리와 맞지 않음 {4} 81배는 3을 네 번 곱한 값\n포인트 ▶ 면적 ∝ 길이², 용적(부피·무게) ∝ 길이³ — 거인 문제의 핵심.",
 [['by a factor of', '~배로'], ['volume', '용적, 부피'], ['area', '면적'], ['double', '두 배가 되다']], en=False)
T.fixed('다음 글의 밑줄 친 부분 중, 문맥상 낱말의 쓰임이 적절하지 <u>않은</u> 것은?', '본문 ❷ 변형', BOX(
 "Have you ever wondered what would happen if humans could grow to " + CN(1, 'enormous') + " sizes like the giant in Jack and the Beanstalk? Unfortunately, the answer to this " + CN(2, 'hypothetical') + " question is that it is " + CN(3, 'possible') + " due to the scale effect. When the length of an object doubles, its area " + CN(4, 'increases') + " by a factor of four, and its volume by a factor of eight. These changes can create many problems that would put the giant's life in " + CN(5, 'danger') + "."),
 ['enormous', 'hypothetical', 'possible', 'increases', 'danger'], 3,
 "이유 ▶ Unfortunately(불행히도) + 거인의 생명을 위험에 빠뜨리는 문제 → 거인처럼 크게 자라는 것은 크기 효과 때문에 '불가능하다' → <i>impossible</i>.\n오답 ▶ ① '엄청난' 크기 ✔ ② '가상적인' 질문 ✔ ④ 면적이 4배로 '증가' ✔ ⑤ 생명을 '위험'에 빠뜨림 ✔\n포인트 ▶ Unfortunately 뒤에는 부정적인 결론.",
 [['enormous', '엄청난, 거대한'], ['hypothetical', '가상적인'], ['scale effect', '크기 효과'], ['put A in danger', 'A를 위험에 빠뜨리다']])
# ❸
T.flex('다음 글의 내용과 일치하는 것은?', '본문 ❸', BOX(J(K3)), [
 ('If a person\'s height increased ten times, the area of his feet would increase 100 times.', '사람의 키가 10배가 되면 발의 면적은 100배가 될 것이다.'),
 ('Weight changes in proportion to the area of the feet.', '무게는 발의 면적에 비례해 변한다.'),
 ('A giant\'s feet could easily support his increased weight.', '거인의 발은 늘어난 몸무게를 쉽게 지탱할 수 있을 것이다.'),
 ('The mass would increase less than the area of the feet.', '질량은 발의 면적보다 적게 늘어날 것이다.'),
 ('If his height increased ten times, his weight would increase ten times.', '키가 10배가 되면 몸무게도 10배가 될 것이다.')],
 "이유 ▶ the area of the feet ~ would only increase by a factor of 100 (10x10) ✔\n오답 ▶ {1} weight changes in proportion to volume(부피에 비례) {2} under too much pressure to support(지탱하기에 압력이 너무 큼) {3} increased far more than the area(훨씬 더 많이 늘어남) {4} by a factor of 1,000 (10x10x10)\n포인트 ▶ 키 10배 → 발 면적 100배 / 몸무게 1,000배.",
 [['in proportion to', '~에 비례하여'], ['support', '지탱하다'], ['pressure', '압력'], ['properly', '제대로, 똑바로']])
T.flex('다음 빈칸에 들어갈 말로 가장 적절한 것은?', '본문 ❸ 변형', BOX(
 J(K3[:3]) + " This means that his feet would be under too much pressure to support the increased weight because the mass would have increased " + BL + " the area of his feet."), [
 ('far more than', '~보다 훨씬 더 많이'), ('far less than', '~보다 훨씬 더 적게'), ('exactly as much as', '~와 정확히 같은 만큼'),
 ('at the same rate as', '~와 같은 비율로'), ('slightly less than', '~보다 약간 적게')],
 "이유 ▶ 몸무게(질량)는 1,000배, 발 면적은 100배 → 질량이 면적보다 '훨씬 더 많이' 늘어서 발이 지나친 압력을 받는다.\n오답 ▶ {1}·{4} 질량이 덜 늘면 압력이 커질 이유가 없다 {2}·{3} 같은 비율이면 압력은 그대로\n포인트 ▶ 1,000배 vs 100배 → 차이 10배 = too much pressure.",
 [['mass', '질량'], ['increased', '늘어난'], ['too ~ to …', '너무 ~해서 …할 수 없는'], ['rate', '비율, 속도']])
T.table('(A), (B), (C)의 각 네모 안에서 어법에 맞는 표현으로 가장 적절한 것은?', '본문 ❸', BOX(
 "One issue is <b>(A)</b> [ that / what ] the giant would not be able to stand properly on his own because of the weight <b>(B)</b> [ pushing / pushed ] down on his feet. … However, the area of the feet <b>(C)</b> [ supporting / supported ] his body would only increase by a factor of 100."),
 ['(A)', '(B)', '(C)'], [['that', 'pushing', 'supporting'], ['what', 'pushing', 'supporting'], ['that', 'pushed', 'supporting'], ['that', 'pushing', 'supported'], ['what', 'pushed', 'supported']],
 "이유 ▶ (A) 뒤가 완전한 절(주어 the giant + 동사) → 보어절을 이끄는 접속사 <i>that</i> (B) 무게가 발을 '누르는' 능동 → <i>pushing</i> (C) 발이 몸을 '지탱하는' 능동 + 뒤에 목적어 his body → <i>supporting</i>\n오답 ▶ what은 뒤가 불완전할 때 / pushed·supported는 수동이라 뜻이 맞지 않고, (C)는 뒤의 목적어와도 맞지 않는다\n포인트 ▶ 분사 뒤에 목적어가 있으면 -ing.",
 [['issue', '문제, 쟁점'], ['on one\'s own', '혼자 힘으로'], ['push down on', '~을 아래로 누르다'], ['by a factor of 100', '100배로']],
 ko=['접속사 / 누르는 / 지탱하는', '관계대명사 / 누르는 / 지탱하는', '접속사 / 눌린 / 지탱하는', '접속사 / 누르는 / 지탱되는', '관계대명사 / 눌린 / 지탱되는'])
# ❹
body, a = ABC(K4[0], [K4[1:2], K4[2:4], K4[4:5]], 'CAB')
T.fixed('주어진 글 다음에 이어질 글의 순서로 가장 적절한 것은?', '본문 ❹', body, OPTS_ORD, a,
 "이유 ▶ 주어진 글(열 배출 문제) → (C) 열은 몸에서 생겨 피부로 계속 내보내진다(원리) → (A) 키 10배면 열은 1,000배, 피부 면적은 100배라 열이 충분히 빠지지 못함(문제) → (B) This shows ~ 그 형태로는 살 수 없다(결론).\n오답 ▶ (A)의 the amount of heat generated는 열이 생긴다는 원리(C) 뒤 / (B)의 This shows는 앞의 계산 결과를 받는 결론이라 맨 끝\n포인트 ▶ 원리 → 계산(문제) → 결론 순서.",
 [['heat emission', '열 배출'], ['generate', '만들어 내다'], ['accumulate', '쌓이다, 축적되다'], ['survive', '살아남다']], en=False)
T.table('다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 적절한 것은?', '본문 ❹', BOX(J(K4)) + '\n' + SUM(
 'If a giant\'s height increased ten times, the heat produced would rise in proportion to his <b>(A)</b> ' + BL + ', while the skin area that <b>(B)</b> ' + BL + ' heat would grow much less.'),
 ['(A)', '(B)'], [['volume', 'releases'], ['height', 'releases'], ['volume', 'absorbs'], ['skin', 'stores'], ['height', 'generates']],
 "이유 ▶ (A) the amount of heat generated would increase ~ in proportion to the body's volume → <i>volume</i> (B) 열은 피부 표면으로 '배출된다(released)' → <i>releases</i>\n오답 ▶ height(키)는 10배만 늘어 열의 1,000배와 맞지 않음 / absorbs(흡수)·stores(저장)·generates(생성)는 피부가 하는 역할이 아니다\n포인트 ▶ 열 생성 ∝ 부피(1,000배), 열 배출 ∝ 피부 면적(100배).",
 [['produce', '만들어 내다'], ['absorb', '흡수하다'], ['store', '저장하다'], ['release', '내보내다, 배출하다']],
 ko=['부피 / 내보내는', '키 / 내보내는', '부피 / 흡수하는', '피부 / 저장하는', '키 / 만들어 내는'])
T.flex('본문 ❸·❹에서 말한, 사람이 거인처럼 커지면 살 수 없는 이유로 가장 적절한 것은?', '본문 ❸·❹', '', [
 '발이 늘어난 몸무게를 지탱하지 못하고, 몸의 열을 충분히 내보내지 못한다.', '키가 너무 커서 숨쉬기 어렵고, 먹을 것을 구하기 어렵다.',
 '뼈가 가벼워지고, 피부가 얇아져 쉽게 다친다.', '발 면적이 너무 넓어지고, 열이 너무 많이 빠져나가 춥다.', '몸무게가 오히려 줄고, 체온이 계속 떨어진다.'],
 "이유 ▶ ❸ 몸무게 1,000배 vs 발 면적 100배 → 똑바로 서지 못함 / ❹ 열 생성 1,000배 vs 피부 면적 100배 → 열이 충분히 배출되지 않음.\n오답 ▶ {1} 숨쉬기·음식 이야기는 없다 {2} 뼈·피부 두께 이야기는 없다 {3}·{4} 열이 너무 '적게' 빠져나가 몸에 쌓이는 것이 문제, 몸무게는 늘어난다\n포인트 ▶ 두 문제 모두 '부피(세제곱)는 면적(제곱)보다 훨씬 빨리 커진다'는 크기 효과.",
 [['body heat', '체열'], ['support', '지탱하다'], ['release', '내보내다'], ['scale effect', '크기 효과']], en=False)
# ❺
T.flex('밑줄 친 <u>the inconstant moon</u>이 뜻하는 내용으로 가장 적절한 것은?', '본문 ❺', BOX(J(K5[:4]).replace('the inconstant moon', U('the inconstant moon'), 1)), [
 '모양이 자꾸 바뀌는 달처럼, 사랑도 변할 수 있다.', '달은 늘 밤하늘에 있어 믿을 수 있다.', '달의 중력이 바다를 움직인다.',
 '달이 없으면 하루가 짧아진다.', '달빛 아래에서 한 약속은 반드시 지켜진다.'],
 "이유 ▶ Juliet warns Romeo not to swear his love by the Moon as it may change just as the Moon changes its shape → 모양이 변하는 달 = 변할 수 있는 사랑.\n오답 ▶ {1} 달이 늘 있다는 것은 뒤의 과학 설명이지 '변덕스러운 달'의 뜻이 아니다 {2}·{3} 뒤 문단의 과학 내용 {4} 반대 뜻\n포인트 ▶ inconstant = 변덕스러운(in + constant 변함없는).",
 [['swear by', '~에 걸고 맹세하다'], ['inconstant', '변덕스러운'], ['warn', '경고하다'], ['appearance', '모습, 외관']], en=False)
body, a = ABC(K5[5], [K5[6:8], K5[8:10], K5[10:12]], 'BCA')
T.fixed('주어진 글 다음에 이어질 글의 순서로 가장 적절한 것은?', '본문 ❺', body, OPTS_ORD, a,
 "이유 ▶ 주어진 글(달이 없으면 하루가 24시간이 아님) → (B) 달의 중력이 바다를 움직이고, 바다와 자전하는 지구 사이에 마찰 → (C) This friction이 자전 속도를 줄임, 달이 없으면 줄지 않음 → (A) 지구가 처음 생겼을 때 달이 없었고 하루는 5시간 → 달이 없으면 5시간마다 해가 뜬다.\n오답 ▶ (C)의 This friction은 마찰이 처음 나오는 (B) 뒤 / (A)의 예(5시간)는 원리 설명이 끝난 뒤\n포인트 ▶ 지시어(This friction)와 원인 → 결과 → 근거 흐름.",
 [['gravity', '중력'], ['friction', '마찰'], ['rotation', '자전, 회전'], ['spin', '회전하다']], en=False)
T.fixed('다음 글의 밑줄 친 부분 중, 문맥상 낱말의 쓰임이 적절하지 <u>않은</u> 것은?', '본문 ❺ 변형', BOX(
 "Although its appearance changes, the Moon is always " + CN(1, 'present') + " in the night sky and plays a " + CN(2, 'crucial') + " role in regulating the length of the day on Earth. The Moon's gravity causes the Earth's ocean to rise and fall. Since the ocean is moving and the Earth is also spinning, " + CN(3, 'friction') + " occurs between them. This friction leads to an " + CN(4, 'increase') + " in the rotation rate of the planet. Without the Moon, however, the Earth's rotation would not " + CN(5, 'slow down') + ", resulting in a change in the length of a day."),
 ['present', 'crucial', 'friction', 'increase', 'slow down'], 4,
 "이유 ▶ 마찰은 자전을 '느리게' 한다 → 자전율의 <i>decrease</i>(감소). 뒤 문장 '달이 없으면 자전이 느려지지 않는다'와 짝이 맞아야 한다.\n오답 ▶ ① 늘 밤하늘에 '존재한다' ✔ ② '중요한' 역할 ✔ ③ 바다와 지구 사이 '마찰' ✔ ⑤ 달이 없으면 '느려지지' 않음 ✔\n포인트 ▶ 마찰(friction) → 속도 감소.",
 [['present', '존재하는'], ['crucial', '중요한, 결정적인'], ['regulate', '조절하다'], ['rotation rate', '자전율']])
T.flex('다음 글의 내용과 일치하는 것은?', '본문 ❺', BOX(J(K5)), [
 ('Some scientists say a day was only five hours long when the Earth first formed.', '몇몇 과학자들은 지구가 처음 생겼을 때 하루가 5시간이었다고 말한다.'),
 ('Juliet asks Romeo to swear his love by the Moon.', 'Juliet은 Romeo에게 달에 걸고 사랑을 맹세하라고 한다.'),
 ('Friction between the ocean and the Earth speeds up the Earth\'s rotation.', '바다와 지구 사이의 마찰은 지구의 자전을 빠르게 한다.'),
 ('Without the Moon, a day would become longer than 24 hours.', '달이 없으면 하루가 24시간보다 길어질 것이다.'),
 ('The Moon only affects the Earth\'s weather, not the length of a day.', '달은 지구의 날씨에만 영향을 주고 하루 길이에는 영향을 주지 않는다.')],
 "이유 ▶ According to some scientists, when the Earth first formed, there was no Moon and a day was only five hours long ✔\n오답 ▶ {1} warns Romeo not to swear(맹세하지 말라고 경고) {2} leads to a decrease in the rotation rate(속도 감소) {3} 자전이 느려지지 않으니 하루는 더 '짧아진다'(5시간마다 일출) {4} regulating the length of the day as well as seasons and weather\n포인트 ▶ 달 없음 → 자전 그대로 빠름 → 하루가 짧음.",
 [['according to', '~에 따르면'], ['form', '형성되다'], ['indicate', '나타내다'], ['affect', '영향을 주다']])
# ❻
T.flex('다음 빈칸에 들어갈 말로 가장 적절한 것은?', '본문 ❻ 변형', BOX(
 K6[0] + ' ' + K6[1] + " The axis of rotation of the Earth is tilted at an angle of 23.5 degrees, and the Moon's gravity holds the Earth in place by " + BL + " the tilt. " + K6[3]), [
 ('stabilizing', '안정시킴'), ('increasing', '늘림'), ('removing', '없앰'), ('reversing', '뒤집음'), ('doubling', '두 배로 만듦')],
 "이유 ▶ 달의 중력이 지구를 '제자리에' 붙잡아 둔다 + 달이 없으면 기울기가 0~85도로 크게 흔들린다(However) → 달은 기울기를 '안정시킨다'.\n오답 ▶ {1}·{4} 기울기를 바꾸면 제자리에 붙잡아 둔다는 말과 맞지 않음 {2} 기울기가 없으면 계절이 없다 {3} 뒤집는다는 근거 없음\n포인트 ▶ hold ~ in place(제자리에 두다) = stabilize(안정시키다).",
 [['axis', '(회전)축'], ['tilt', '기울기; 기울이다'], ['hold ~ in place', '~을 제자리에 고정하다'], ['vary', '달라지다']])
T.fixed('다음 글의 밑줄 친 부분 중, 어법상 <u>틀린</u> 것은?', '본문 ❻ 변형', BOX(
 "We experience the beauty of different seasons because the Earth " + CN(1, 'is tilted') + " on its axis. However, if there " + CN(2, 'were') + " no Moon, the tilt could vary wildly between 0 and 85 degrees. Suppose the Earth were " + CN(3, 'tilted') + " at an angle of 60 degrees. The hemisphere of the Earth " + CN(4, 'facing') + " the Sun would receive much more energy than the other hemisphere. This could bring about extreme shifts in weather patterns, potentially " + CN(5, 'make') + " summers hotter and winters colder."),
 ['is tilted', 'were', 'tilted', 'facing', 'make'], 5,
 "이유 ▶ 앞 절의 결과를 덧붙이는 분사구문 → <i>making</i> (summers hotter: make + 목적어 + 형용사).\n오답 ▶ ① 지구가 '기울어져 있는' 수동 ✔ ② 가정법 과거 if there were ✔ ③ Suppose the Earth were tilted: 지구가 '기울어진' 상태(수동) ✔ ④ 반구가 태양을 '향하는' 능동 + 목적어 the Sun ✔\n포인트 ▶ 콤마 뒤 접속사 없이 동사가 또 오면 분사구문(-ing)!",
 [['hemisphere', '반구'], ['bring about', '가져오다, 일으키다'], ['extreme', '극단적인'], ['potentially', '잠재적으로']])
g, body, a = INS(2, K6[1:8])
T.fixed('글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳은?', '본문 ❻', GIV(g) + '\n' + BOX(body), None, a,
 "이유 ▶ 달의 중력이 기울기(23.5도)를 안정시킨다 → However 달이 없으면 기울기가 0~85도로 크게 변한다 → Suppose 60도로 기울었다면 ~. 따라서 ②.\n오답 ▶ ① 아직 달이 기울기를 안정시킨다는 말이 나오기 전 ③ Suppose(60도라고 가정)는 기울기가 크게 변할 수 있다는 말 뒤에 와야 한다 ④⑤ 60도의 결과 설명 사이라 흐름이 끊긴다\n포인트 ▶ However = 달이 있을 때(안정) ↔ 없을 때(크게 변함).",
 [['vary wildly', '크게 달라지다'], ['degree', '(각도의) 도'], ['suppose', '가정하다'], ['stabilize', '안정시키다']])
# ❼
T.flex('다음 글의 내용과 일치하지 <u>않는</u> 것은?', '본문 ❼', BOX(J(K7)), [
 ('Insects breathe through both lungs and spiracles.', '곤충은 폐와 숨구멍 둘 다로 숨을 쉰다.'),
 ('Oxygen makes up 21 percent of the Earth\'s atmosphere.', '산소는 지구 대기의 21%를 차지한다.'),
 ('Oxygen is needed to burn fuels like wood and oil.', '나무와 석유 같은 연료를 태우는 데 산소가 필요하다.'),
 ('Spiracles are less efficient than lungs at taking in air.', '숨구멍은 공기를 들이마시는 데 폐보다 덜 효율적이다.'),
 ('Bees and dragonflies take in air through external openings.', '꿀벌과 잠자리는 외부 구멍을 통해 공기를 들이마신다.')],
 "이유 ▶ Insects ~ do not have lungs and instead take in air through ~ spiracles → 곤충은 폐가 '없다'.\n오답 ▶ {1} making up 21 percent ✔ {2} necessary to burn common fuels like wood and oil ✔ {3} not as efficient as lungs ✔ {4} take in air through external openings called spiracles ✔\n포인트 ▶ not as ~ as = ~만큼 …하지 않다 = less ~ than.",
 [['spiracle', '숨구멍'], ['lung', '폐'], ['atmosphere', '대기'], ['efficient', '효율적인']])
# ❽
T.fixed('다음 글의 밑줄 친 부분 중, 문맥상 낱말의 쓰임이 적절하지 <u>않은</u> 것은?', '본문 ❽ 변형', BOX(
 "With the current oxygen concentration, insects cannot evolve to be " + CN(1, 'larger') + " than their current size. However, if the concentration of oxygen were to double, insects could grow in size as oxygen would be more " + CN(2, 'readily') + " available. This increase in insect size could have a significant influence on the ecological environment, potentially " + CN(3, 'disrupting') + " the food chain. Dragonflies, for example, may become as large as eagles, " + CN(4, 'maintaining') + " the balance of predators and prey in the ecosystem. The increase in oxygen would help to use energy more " + CN(5, 'efficiently') + "."),
 ['larger', 'readily', 'disrupting', 'maintaining', 'efficiently'], 4,
 "이유 ▶ 잠자리가 독수리만큼 커지면 먹이사슬이 무너져 포식자와 먹이의 균형이 '바뀐다' → <i>altering</i>. maintaining(유지)은 앞의 disrupting the food chain과 반대.\n오답 ▶ ① 현재 크기보다 '더 크게' 진화할 수 없다 ✔ ② 산소를 더 '쉽게' 이용 ✔ ③ 먹이사슬을 '붕괴시킴' ✔ ⑤ 에너지를 더 '효율적으로' 사용 ✔\n포인트 ▶ for example 뒤의 예는 앞 문장(disrupting)과 같은 방향.",
 [['concentration', '농도'], ['readily', '쉽게'], ['disrupt', '붕괴시키다, 방해하다'], ['alter', '바꾸다']])
T.flex('다음 빈칸에 들어갈 말로 가장 적절한 것은?', '본문 ❽ 변형', BOX(
 J(K8[6:9]) + " While these three thought experiments offer interesting possibilities, it is important to consider that they are simply based on imagination and " + BL + " through scientific research."), [
 ('have not been tested', '시험되지 않았다'), ('have been fully proven', '완전히 증명되었다'), ('were rejected', '거부되었다'),
 ('cannot be imagined', '상상할 수 없다'), ('are widely used', '널리 쓰인다')],
 "이유 ▶ While(~이지만) 흥미로운 가능성 ↔ 그저 상상에 근거한 것(simply based on imagination) → 과학적 연구로 '시험되지 않았다'는 한계.\n오답 ▶ {1} 증명되었다면 '상상에 근거할 뿐'이라는 말과 반대 {2} 거부된 것이 아니라 아직 시험되지 않음 {3} 이미 상상으로 한 실험 {4} 근거 없음\n포인트 ▶ 사고 실험 = 상상(가설) 단계, 아직 검증 전.",
 [['consider', '고려하다'], ['simply', '단지'], ['prove', '증명하다'], ['research', '연구']])
T.render()
