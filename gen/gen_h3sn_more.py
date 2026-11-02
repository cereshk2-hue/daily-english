# 고3 수능실전반 나머지 번호 (11/2) — gen_h3sn.py 안에서 exec 로 불러 씀 (day, esc, DAYS 공유)
# 지금 푸는 학생은 고1·2 → 남은 번호 전부, 쉬운 문항과 어려운 문항을 번갈아 배치
# 순서: 18 → 32 → 26 → 35 → 29 → 19 → 33 → 27 → 39 → 30 → 25 → 34 → 28 → 41·42 → 43~45
# 정답(직접 풀이): 18⑤ 19① 25④ 26② 27⑤ 28④ 29③ 30③ 32⑤ 33⑤ 34② 35④ 39③ 41⑤ 42④ 43② 44③ 45③

def multi(rng, n):
    """방금 day()로 만든 n개를 한 DAY로 합침 (장문 세트). 첫 DAY의 지문·단어를 쓰고, 나머지는 실전 문항만 붙임"""
    base = DAYS[-n]
    for extra in DAYS[-n + 1:]:
        it = extra['steps'][0]['items'][0]
        it['ex'] = it['ex'].split('\n핵심 문장 ▶')[0]
        base['steps'][0]['items'].append(it)
    del DAYS[-n + 1:]
    base['range'] = rng
    base['passage'][0][1] = rng.replace('번 ', '번 · ', 1)

def lines_html(rows, heads):
    out = []
    for e, k in rows:
        out.append(('<b>%s</b>' % esc(e)) if e in heads else ('- ' + esc(e) if not e.startswith('(') else esc(e)))
    return '<br>'.join(out)

# ═══ DAY 11 · 18번 목적 ═══
T18 = [
 ("Thank you for always ordering pies from our bakery for your special occasions.", "특별한 날마다 저희 빵집에서 늘 파이를 주문해 주셔서 감사합니다."),
 ("We truly appreciate your continued support and always try to provide pies of the highest quality.", "지속적인 성원에 진심으로 감사드리며, 저희는 늘 최고 품질의 파이를 제공하려고 노력합니다."),
 ("Unfortunately, we are writing to inform you that we are unable to prepare the apple pie you've ordered for the upcoming birthday celebration.", "안타깝게도, 다가오는 생일 축하 자리를 위해 주문하신 사과파이를 준비해 드릴 수 없다는 것을 알려 드리고자 글을 씁니다."),
 ("Due to a delayed apple harvest this season, we are currently experiencing difficulties sourcing fresh apples.", "이번 철 사과 수확이 늦어져서, 현재 신선한 사과를 구하는 데 어려움을 겪고 있습니다."),
 ("As a result, we are unable to fulfill the order that you've requested.", "그 결과, 요청하신 주문을 이행해 드릴 수 없습니다."),
 ("We sincerely apologize for this situation.", "이런 상황에 대해 진심으로 사과드립니다."),
 ("We appreciate your understanding and look forward to serving you again in the future.", "양해해 주셔서 감사드리며, 앞으로 다시 모실 수 있기를 기대합니다."),
]
day(18, 'q18', '목적', '글의 목적 · Unfortunately 뒤의 본론 찾기', '다음 글의 목적으로 가장 적절한 것은?', T18,
 ['사과파이 주문 방법을 공지하려고', '사과파이 특별 할인 행사를 홍보하려고', '주문 취소에 따른 환불 절차를 설명하려고', '주문 변경에 따른 추가 요금을 안내하려고', '주문한 사과파이를 제공할 수 없음을 알리려고'], 4,
 '처음 두 문장은 감사 인사예요. Unfortunately(안타깝게도)로 본론이 시작돼요: 주문한 사과파이를 준비해 드릴 수 없다(we are unable to prepare the apple pie you\'ve ordered). 이어서 이유(사과 수확이 늦어짐)와 사과가 나와요.',
 ['① 주문 방법은 나오지 않아요.', '② 할인 행사는 나오지 않아요.', '③ 주문을 이행할 수 없다고만 했지 환불 절차는 설명하지 않아요. (취소·환불이라는 말에 속지 않기)', '④ 추가 요금 이야기는 없어요.'],
 '목적 문제는 Unfortunately, However 같은 전환어 뒤와 we are writing to ~ 문장이 핵심이에요. 앞의 감사 인사는 인사말일 뿐이에요.',
 [(T18[2][0], T18[2][1], "be writing to inform you that ~ ~을 알려 드리려고 글을 쓰다 · the apple pie (that) you've ordered (목적격 관계대명사 생략)"),
  (T18[3][0], T18[3][1], "Due to + 명사 ~ 때문에 · experience difficulties (in) -ing ~하는 데 어려움을 겪다 · source 구하다, 조달하다"),
  (T18[6][0], T18[6][1], "look forward to -ing ~하기를 고대하다 (to는 전치사 → 동명사)")],
 [('occasion', '특별한 날, 행사'), ('appreciate', '감사하다'), ('continued', '지속적인'), ('support', '성원, 지원'), ('quality', '품질'), ('inform', '알리다'),
  ('be unable to', '~할 수 없다'), ('upcoming', '다가오는'), ('celebration', '축하 행사'), ('due to', '~ 때문에'), ('delayed', '늦어진'), ('harvest', '수확'),
  ('source', '(물건을) 구하다, 조달하다'), ('fulfill', '(주문·약속을) 이행하다'), ('request', '요청하다'), ('sincerely', '진심으로'), ('apologize', '사과하다'), ('look forward to', '~을 고대하다')],
 ['occasion', 'appreciate', 'support', 'quality', 'inform', 'upcoming', 'celebration', 'harvest', 'source', 'fulfill', 'sincerely', 'apologize'])

# ═══ DAY 12 · 32번 빈칸 ═══
T32 = [
 ("Reflective customer service chatbots employ self-assessment methodologies to continuously improve their ability to provide effective and satisfactory responses to users.", "성찰하는 고객 서비스 챗봇은 사용자에게 효과적이고 만족스러운 응답을 제공하는 능력을 지속적으로 향상시키기 위해 자기 평가 방법론을 사용한다."),
 ("By introspecting on past conversations, these chatbots can identify patterns, strengths, weaknesses, and areas for improvement, enabling them to refine their knowledge base, response strategies, and overall interaction capabilities.", "과거의 대화를 자기 분석함으로써 이 챗봇들은 패턴, 강점, 약점, 개선할 부분을 파악할 수 있고, 이는 그들이 지식 기반, 응답 전략, 전반적인 상호 작용 능력을 다듬을 수 있게 해 준다."),
 ("One key aspect of self-assessment is the ability to analyze the outcomes of past conversations.", "자기 평가의 한 가지 핵심 측면은 과거 대화의 결과를 분석하는 능력이다."),
 ("Chatbots can review user feedback, sentiment analysis, and conversation metrics to measure the success or failure of their responses.", "챗봇은 사용자 피드백, 감정 분석, 대화 메트릭스를 검토하여 자신의 응답이 성공했는지 실패했는지를 측정할 수 있다."),
 ("For instance, a chatbot might identify conversations where users expressed frustration or dissatisfaction through negative sentiment or low satisfaction ratings.", "예를 들어, 챗봇은 사용자가 부정적인 감정이나 낮은 만족도 평가를 통해 좌절감이나 불만을 표현한 대화를 찾아낼 수 있다."),
 ("By reflecting on these instances, the chatbot can pinpoint potential issues, such as misunderstandings, inadequate information, or inappropriate tone or language.", "이런 사례들을 되돌아봄으로써, 챗봇은 오해, 불충분한 정보, 부적절한 어조나 언어와 같은 잠재적 문제를 정확히 짚어 낼 수 있다."),
 ("Conversely, the chatbot can also analyze conversations that went well, where users expressed satisfaction or gratitude for the provided solutions.", "반대로, 챗봇은 사용자가 제공된 해결책에 만족이나 감사를 표현한, 잘 진행된 대화도 분석할 수 있다."),
 ("By studying the characteristics of these successful interactions, the chatbot can reinforce effective response strategies, identify best practices, and replicate them in future conversations.", "이런 성공적인 상호 작용의 특징을 연구함으로써, 챗봇은 효과적인 응답 전략을 강화하고, 모범 사례를 찾아내어, 앞으로의 대화에서 그것을 재현할 수 있다."),
]
day(32, 'q32', '빈칸', '빈칸 추론 · One key aspect 뒤의 예시를 한마디로 묶기', '다음 빈칸에 들어갈 말로 가장 적절한 것은?', T32,
 ['to provide scripted responses to users', 'to find more cost-effective communication channels', 'to keep users from noticing previous conversation errors', "to enhance the speed of the system's responses", 'to analyze the outcomes of past conversations'], 4,
 '빈칸 뒤에서 챗봇은 피드백·감정 분석·메트릭스로 응답의 성공 또는 실패를 측정해요. 불만족한 대화(실패)에서는 문제를 찾고, 잘된 대화(성공)에서는 모범 사례를 찾아요. 이 모두가 “과거 대화의 결과를 분석하는” 일이에요.',
 ['① 대본대로 정해진 응답 → 오히려 응답 전략을 계속 다듬어요.', '② 비용 효율적인 소통 경로는 나오지 않아요.', '③ 이전 대화의 오류를 사용자에게 숨기기 → 오히려 오류를 찾아 고쳐요.', '④ 응답 속도는 나오지 않아요.'],
 '빈칸 문장이 One key aspect of ~(핵심 측면 하나)이면, 바로 뒤 예시(For instance, Conversely)를 한마디로 묶는 말이 정답이에요.',
 [(T32[1][0], T32[1][1], "By -ing ~함으로써 · 분사구문 enabling them to ~ (= and this enables them to ~) · enable + O + to부정사"),
  (T32[4][0], T32[4][1], "관계부사 where (선행사 conversations, 상황·경우) · express frustration 좌절감을 표현하다"),
  (T32[7][0], T32[7][1], "reinforce, identify, replicate 세 동사가 can에 병렬로 연결 · replicate them(= best practices)")],
 [('reflective', '성찰하는'), ('employ', '사용하다'), ('self-assessment', '자기 평가'), ('methodology', '방법론'), ('satisfactory', '만족스러운'), ('introspect', '자기 분석하다'),
  ('identify', '찾아내다, 파악하다'), ('refine', '다듬다, 개선하다'), ('capability', '능력'), ('sentiment', '감정'), ('metrics', '메트릭스(계량 분석)'), ('frustration', '좌절감'),
  ('dissatisfaction', '불만'), ('pinpoint', '정확히 짚어 내다'), ('inadequate', '불충분한'), ('inappropriate', '부적절한'), ('conversely', '반대로'), ('gratitude', '감사'),
  ('reinforce', '강화하다'), ('replicate', '재현하다, 복제하다'), ('outcome', '결과')],
 ['employ', 'methodology', 'satisfactory', 'identify', 'refine', 'capability', 'sentiment', 'frustration', 'inadequate', 'conversely', 'reinforce', 'replicate'],
 blank='to analyze the outcomes of past conversations', notes='* introspect: 자기 분석하다 ** metrics: 메트릭스(업무 수행 결과를 보여 주는 계량적 분석)')

# ═══ DAY 13 · 26번 내용 불일치 ═══
T26 = [
 ("Otto Loewi was a pharmacologist whose discoveries greatly advanced the study of chemical communication between nerve cells.", "Otto Loewi는 신경 세포 간 화학적 소통에 관한 연구를 크게 발전시킨 발견을 한 약리학자였다."),
 ("Born in Frankfurt, Germany, in 1873, he originally hoped to study art history.", "1873년 독일 프랑크푸르트에서 태어난 그는 원래 미술사를 공부하기를 바랐다."),
 ("However, following his parents' advice, Loewi studied medicine at the University of Strasbourg, Germany (now part of France).", "그러나 부모님의 조언에 따라, Loewi는 독일(지금은 프랑스 영토)의 스트라스부르 대학교에서 의학을 공부했다."),
 ("Although he was qualified as a physician, he chose to switch from a doctor treating patients to a medical researcher seeking cures.", "그는 의사 자격을 갖추었지만, 환자를 치료하는 의사에서 치료법을 찾는 의학 연구자로 진로를 바꾸기로 했다."),
 ("In 1902, he first met Henry Dale in Ernest Starling's laboratory in London, where he spent several months.", "1902년, 그는 런던에 있는 Ernest Starling의 연구실에서 Henry Dale을 처음 만났는데, 그곳에서 몇 달을 보냈다."),
 ("In 1936, he and Henry Dale shared the Nobel Prize in Physiology or Medicine.", "1936년, 그와 Henry Dale은 노벨 생리의학상을 공동 수상했다."),
 ("After Germany invaded Austria in 1938, Loewi was forced to leave Austria, where he was living at the time.", "1938년 독일이 오스트리아를 침공한 후, Loewi는 당시 살고 있던 오스트리아를 떠날 수밖에 없었다."),
 ("Loewi became a research professor at New York University's College of Medicine in 1940.", "Loewi는 1940년에 뉴욕대학교 의과 대학의 연구 교수가 되었다."),
]
day(26, 'q26', '내용 불일치', '인물 내용 일치 · However 앞뒤로 바뀐 사실 잡기', 'Otto Loewi에 관한 다음 글의 내용과 일치하지 <u>않는</u> 것은?', T26,
 ['1873년에 독일에서 태어났다.', '부모님의 조언에 따라 미술사를 공부했다.', 'Ernest Starling의 연구실에서 Henry Dale을 처음 만났다.', 'Henry Dale과 노벨상을 공동 수상했다.', '뉴욕대학교 의과 대학의 연구 교수가 되었다.'], 1,
 '원래는 미술사를 공부하고 싶었지만(originally hoped to study art history), However 부모님의 조언에 따라 “의학(medicine)”을 공부했어요. 선택지는 미술사와 부모님의 조언을 섞어 놓은 함정이에요.',
 ['① Born in Frankfurt, Germany, in 1873 → 일치', "③ he first met Henry Dale in Ernest Starling's laboratory → 일치", '④ he and Henry Dale shared the Nobel Prize → 일치', "⑤ became a research professor at New York University's College of Medicine → 일치"],
 '인물 일치 문제는 선택지 순서 = 본문 순서예요. originally(원래), However처럼 “바뀐 것”을 나타내는 말이 나오면 거의 함정 자리예요.',
 [(T26[1][0], T26[1][1], "분사구문 Born ~ (= He was born ~, and he) · originally 원래"),
  (T26[3][0], T26[3][1], "Although ~이지만 · switch from A to B A에서 B로 바꾸다 · 현재분사 treating, seeking이 앞 명사를 꾸밈"),
  (T26[6][0], T26[6][1], "be forced to ~할 수밖에 없다 · 콤마 + where (= and there) 계속적 용법")],
 [('pharmacologist', '약리학자'), ('advance', '발전시키다'), ('chemical', '화학적인'), ('nerve cell', '신경 세포'), ('originally', '원래'), ('following', '~에 따라'),
  ('medicine', '의학'), ('be qualified as', '~의 자격을 갖추다'), ('physician', '의사'), ('switch', '바꾸다'), ('treat', '치료하다'), ('seek', '찾다, 구하다'),
  ('cure', '치료법'), ('laboratory', '연구실'), ('physiology', '생리학'), ('invade', '침공하다'), ('be forced to', '어쩔 수 없이 ~하다'), ('research professor', '연구 교수')],
 ['advance', 'chemical', 'originally', 'medicine', 'physician', 'switch', 'treat', 'seek', 'cure', 'laboratory', 'physiology', 'invade'],
 notes='* pharmacologist: 약리학자 ** physiology: 생리학')

# ═══ DAY 14 · 35번 무관한 문장 ═══
T35 = [
 ("Research with patients with damage to the hippocampus has indicated that conscious memory of events and motor learning are separate neurological systems.", "해마가 손상된 환자들을 대상으로 한 연구는 사건에 대한 의식적 기억과 운동 학습이 서로 다른 신경계라는 것을 보여 주었다."),
 ("A patient with hippocampal damage can learn a motor task and get better with practice, but each time he practices he will have no conscious memory of doing the task.", "① 해마 손상 환자는 운동 과제를 배우고 연습하면서 더 잘하게 될 수 있지만, 연습할 때마다 그 과제를 했다는 의식적 기억은 없을 것이다."),
 ("The motor circuits become trained, but damage to the hippocampus prevents the formation of new conscious memories.", "② 운동 회로는 훈련되지만, 해마의 손상이 새로운 의식적 기억의 형성을 막는다."),
 ("Therefore, the motor circuits learn a new task, such as solving a simple mechanical puzzle, but the person does not remember seeing or doing the puzzle.", "③ 따라서 운동 회로는 간단한 기계 퍼즐 풀기와 같은 새로운 과제를 배우지만, 그 사람은 퍼즐을 보거나 한 것을 기억하지 못한다."),
 ("This suggests that repetitive practice with the puzzle can help stimulate undamaged brain tissues to recover lost cognitive functions, thereby offering a therapeutic solution for hippocampal damage.", "④ [무관한 문장] 이것은 퍼즐을 반복 연습하는 것이 손상되지 않은 뇌 조직을 자극해 잃어버린 인지 기능을 회복하도록 도울 수 있고, 그리하여 해마 손상에 대한 치료적 해결책을 제공한다는 것을 시사한다."),
 ("With repeated practice, the person gets better and better at it, but each time the puzzle is presented, he says he has never seen it before.", "⑤ 반복 연습을 하면 그 사람은 그것을 점점 더 잘하게 되지만, 퍼즐이 제시될 때마다 그는 전에 그것을 본 적이 없다고 말한다."),
]
day(35, 'q35', '무관한 문장', '무관한 문장 · 같은 소재, 다른 방향(치료법)을 찾기', '다음 글에서 전체 흐름과 관계 없는 문장은?', T35,
 ['①', '②', '③', '④', '⑤'], 3,
 '글의 흐름: 해마 손상 환자는 운동 과제는 배우지만(운동 학습) 그것을 한 기억은 없다(의식적 기억) → 두 체계는 분리되어 있다. ④는 “퍼즐 연습이 뇌 조직을 자극해 잃어버린 인지 기능을 회복시키는 치료법이 된다”는 새로운 주제예요. ⑤에서 여전히 “본 적이 없다”고 말하니 기능이 회복된 것도 아니에요.',
 ['①②③⑤는 모두 “운동 기술은 늘지만 그것을 한 기억은 없다”를 반복하고 구체화해요.', '③ Therefore는 ②(운동 회로는 훈련되지만 기억 형성은 막힌다)의 결과예요.', '⑤는 ③의 퍼즐 예시를 그대로 이어 가요.'],
 '무관한 문장은 소재(퍼즐, 해마)는 같지만 “방향”이 다른 문장이에요. 치료·해결책처럼 글에 없던 새 주제가 나오면 의심하세요.',
 [(T35[0][0], T35[0][1], "주어 Research (with patients ~) / 동사 has indicated · that절 안 주어 A and B → 동사 are"),
  (T35[1][0], "해마 손상 환자는 운동 과제를 배우고 연습하면서 더 잘하게 될 수 있지만, 연습할 때마다 그 과제를 했다는 의식적 기억은 없을 것이다.", "each time + 주어 + 동사 ~할 때마다 (접속사처럼) · get better 더 잘하게 되다"),
  (T35[5][0], "반복 연습을 하면 그 사람은 그것을 점점 더 잘하게 되지만, 퍼즐이 제시될 때마다 그는 전에 그것을 본 적이 없다고 말한다.", "비교급 and 비교급 점점 더 ~한 · has never seen 현재완료(경험)")],
 [('hippocampus', '해마'), ('damage', '손상'), ('indicate', '보여 주다, 시사하다'), ('conscious', '의식적인'), ('motor learning', '운동 학습'), ('separate', '별개의'),
  ('neurological', '신경의'), ('motor task', '운동 과제'), ('circuit', '회로'), ('formation', '형성'), ('mechanical', '기계의'), ('repetitive', '반복적인'),
  ('stimulate', '자극하다'), ('tissue', '(세포) 조직'), ('cognitive', '인지의'), ('thereby', '그렇게 함으로써'), ('therapeutic', '치료의'), ('present', '제시하다')],
 ['damage', 'indicate', 'conscious', 'separate', 'neurological', 'circuit', 'formation', 'mechanical', 'repetitive', 'stimulate', 'cognitive', 'therapeutic'],
 paras=[esc(T35[0][0]) + ' ①' + esc(T35[1][0]) + ' ②' + esc(T35[2][0]) + ' ③' + esc(T35[3][0]) + ' ④' + esc(T35[4][0]) + ' ⑤' + esc(T35[5][0])],
 notes='* hippocampus: 해마')

# ═══ DAY 15 · 29번 어법 ═══
T29 = [
 ("Deduction makes us feel safe: If and when we know all the elements of the problem situation and how they hang together, then we can confidently deduce the outcome.", "연역은 우리를 안전하다고 느끼게 한다. 우리가 문제 상황의 모든 요소와 그것들이 어떻게 서로 맞물려 있는지를 알고 있다면, 그때 우리는 결과를 자신 있게 추론할 수 있다."),
 ("This is rationality at its most unassailable.", "이것은 논쟁의 여지가 가장 없는 상태의 합리성이다."),
 ("In professional practice, this type of thinking expresses itself in the belief that we can produce “logical” strategies and blueprints, or the claim to base ourselves on “best practices” and “evidence-based interventions.”", "직업 현장에서 이런 유형의 사고는, 우리가 ‘논리적인’ 전략과 청사진을 만들어 낼 수 있다는 믿음이나 ‘모범 사례’와 ‘증거 기반 개입’에 근거한다는 주장으로 나타난다."),
 ("But this gold standard of pure logic can only be achieved in a closed world, where we are absolutely sure we know all the elements of the problem situation and completely understand all the relationships at play beforehand.", "그러나 순수 논리라는 이 최고 기준은 닫힌 세계에서만 달성될 수 있는데, 그곳에서 우리는 문제 상황의 모든 요소를 알고 있고 작용하는 모든 관계를 미리 완전히 이해하고 있다고 절대적으로 확신한다."),
 ("In the real world, this never happens — and when it does, we are talking about quite uninteresting, mechanical, routine reasoning.", "현실 세계에서 이런 일은 결코 일어나지 않으며, 일어난다 해도 우리는 꽤 재미없고 기계적이며 일상적인 추론을 말하고 있는 것이다."),
 ("In practice, all problems are messy.", "실제로 모든 문제는 복잡하게 뒤엉켜 있다."),
 ("Yet it is tempting to claim that we have used deduction in dealing with a problem; this claim to pure rationality is so strong that we don't even have to defend the result.", "그런데도 문제를 다룰 때 연역을 사용했다고 주장하고 싶은 유혹이 드는데, 순수한 합리성에 대한 이 주장은 너무 강력해서 우리는 그 결과를 방어할 필요조차 없다."),
 ("It is “logical,” after all.", "어쨌든 그것은 ‘논리적’이니까."),
]
Q29 = ("Deduction makes us feel safe: If and when we know all the elements of the problem situation and how they hang together, then we can ①<u>confidently</u> deduce the outcome. "
       "This is rationality at its most unassailable. In professional practice, this type of thinking expresses itself in the belief ②<u>that</u> we can produce “logical” strategies and blueprints, or the claim to base ourselves on “best practices” and “evidence-based interventions.” "
       "But this gold standard of pure logic can only be achieved in a closed world, ③<u>which</u> we are absolutely sure we know all the elements of the problem situation and completely understand all the relationships at play beforehand. "
       "In the real world, this never happens — and when it ④<u>does</u>, we are talking about quite uninteresting, mechanical, routine reasoning. In practice, all problems are messy. "
       "Yet it is tempting ⑤<u>to claim</u> that we have used deduction in dealing with a problem; this claim to pure rationality is so strong that we don't even have to defend the result. It is “logical,” after all.")
day(29, 'q29', '어법', '어법 · 관계사 뒤 문장이 완전한지 확인', '다음 글의 밑줄 친 부분 중, 어법상 틀린 것은?', T29,
 ['① confidently', '② that', '③ which', '④ does', '⑤ to claim'], 2,
 '선행사 a closed world(장소) 뒤에 완전한 절(we are absolutely sure we know ~ and completely understand ~)이 와요. 빠진 성분이 없으니 관계대명사 which가 아니라 관계부사 where(= in which)가 맞아요.',
 ['① confidently: 동사 deduce를 꾸미는 부사 ✔', '② that: the belief와 동격인 접속사 that (뒤에 완전한 절) ✔', '④ does: 앞의 happens를 대신하는 대동사 (this never happens → when it does) ✔', '⑤ to claim: 가주어 it ~ 진주어 to부정사 ✔'],
 '관계사 문제는 “뒤 문장이 완전한가”부터 확인! 완전하면 관계부사(where/when) 또는 전치사 + which, 불완전하면 which/that이에요.',
 [(T29[0][0], T29[0][1], "make + O + 동사원형(feel) · how they hang together 간접의문문(know의 목적어)"),
  (T29[3][0], T29[3][1], "콤마 + where = and in that world (관계부사, 뒤에 완전한 절) · be sure (that) ~ · at play 작용하는"),
  (T29[6][0], T29[6][1], "가주어 it ~ 진주어 to claim · so ~ that … 너무 ~해서 …하다 · don't have to ~할 필요가 없다")],
 [('deduction', '연역'), ('element', '요소'), ('hang together', '서로 맞물리다, 일관되다'), ('confidently', '자신 있게'), ('deduce', '추론하다'), ('outcome', '결과'),
  ('rationality', '합리성'), ('unassailable', '논쟁의 여지가 없는'), ('blueprint', '청사진'), ('intervention', '개입'), ('gold standard', '최고 기준'), ('at play', '작용하는'),
  ('beforehand', '미리'), ('mechanical', '기계적인'), ('routine', '일상적인'), ('messy', '복잡하게 얽힌'), ('tempting', '유혹적인'), ('defend', '방어하다')],
 ['deduction', 'element', 'confidently', 'deduce', 'outcome', 'rationality', 'blueprint', 'intervention', 'beforehand', 'routine', 'tempting', 'defend'],
 paras=[Q29], notes='* deduction: 연역 ** unassailable: 논쟁의 여지가 없는')

# ═══ DAY 16 · 19번 심경 변화 ═══
T19 = [
 ("The night had finally arrived.", "마침내 그 밤이 왔다."),
 ("It was the night to take a photo of the Milky Way.", "은하수 사진을 찍는 밤이었다."),
 ("Dan had been checking the weather and searching for the perfect location.", "Dan은 (그동안) 날씨를 확인하고 완벽한 장소를 찾아 왔었다."),
 ("As he drove to the spot, he couldn't stop smiling and his heart raced with anticipation.", "그곳으로 차를 몰고 가는 동안, 그는 웃음을 멈출 수 없었고 그의 심장은 기대감으로 두근거렸다."),
 ("However, when he arrived, dark clouds began to cover the sky.", "하지만 그가 도착했을 때, 먹구름이 하늘을 덮기 시작했다."),
 ("Within minutes, every star disappeared behind the thick clouds.", "몇 분 만에 모든 별이 두꺼운 구름 뒤로 사라졌다."),
 ("Dan waited for over an hour, checking his weather app constantly.", "Dan은 날씨 앱을 계속 확인하며 한 시간 넘게 기다렸다."),
 ("Even worse, it started to rain.", "설상가상으로 비가 내리기 시작했다."),
 ("He lowered his head, letting out a loud sigh.", "그는 크게 한숨을 내쉬며 고개를 떨구었다."),
 ("He could do nothing but drive back home, downhearted.", "그는 낙담한 채 차를 몰고 집으로 돌아가는 수밖에 없었다."),
]
day(19, 'q19', '심경 변화', '심경 변화 · However 앞뒤의 행동 묘사를 감정으로 바꾸기', '다음 글에 드러난 Dan의 심경 변화로 가장 적절한 것은?', T19,
 ['excited → disappointed', 'anxious → relieved', 'terrified → indifferent', 'bored → delighted', 'relaxed → grateful'], 0,
 '앞: 웃음을 멈출 수 없었고(couldn\'t stop smiling) 심장이 기대감으로 두근거렸다(heart raced with anticipation) → 신남(excited). 뒤: 구름과 비, 고개를 떨구고(lowered his head) 크게 한숨(loud sigh), 낙담한 채(downhearted) → 실망(disappointed).',
 ['② anxious(불안한) → relieved(안도한): 처음에 불안하지 않았고, 끝에 안도하지도 않았어요.', '③ terrified(겁에 질린) → indifferent(무관심한): 둘 다 근거가 없어요.', '④ bored(지루한) → delighted(기쁜): 순서가 오히려 반대예요.', '⑤ relaxed(편안한) → grateful(감사하는): 근거가 없어요.'],
 '심경 변화는 However 앞뒤로 나누고, 행동 묘사(smiling, heart raced / lowered his head, sigh)를 감정 단어로 바꿔 보세요.',
 [(T19[2][0], T19[2][1], "had been -ing 과거완료진행: 그날 밤 전부터 계속 ~해 왔다"),
  (T19[3][0], T19[3][1], "As ~하는 동안 · couldn't stop -ing ~하는 것을 멈출 수 없었다 · race with anticipation 기대감으로 두근거리다"),
  (T19[9][0], T19[9][1], "can do nothing but + 동사원형 ~하는 수밖에 없다 · , downhearted (낙담한 상태로) 주어의 상태를 덧붙임")],
 [('Milky Way', '은하수'), ('location', '장소'), ('spot', '장소, 지점'), ('race', '(심장이) 두근거리다'), ('anticipation', '기대'), ('cover', '덮다'),
  ('disappear', '사라지다'), ('thick', '두꺼운'), ('constantly', '계속, 끊임없이'), ('even worse', '설상가상으로'), ('lower', '낮추다, 떨구다'), ('let out a sigh', '한숨을 내쉬다'),
  ('do nothing but', '~하는 수밖에 없다'), ('downhearted', '낙담한'), ('disappointed', '실망한'), ('relieved', '안도한'), ('indifferent', '무관심한'), ('grateful', '감사하는')],
 ['location', 'anticipation', 'cover', 'disappear', 'thick', 'constantly', 'lower', 'downhearted', 'disappointed', 'relieved', 'indifferent', 'grateful'])

# ═══ DAY 17 · 33번 빈칸 ═══
T33 = [
 ("The biggest obstacle for AI in real-world settings is that most human tasks aren't nearly as tidy in their rules and boundaries.", "현실 세계 환경에서 AI의 가장 큰 장애물은 대부분의 인간 과제가 규칙과 경계 면에서 전혀 그렇게 깔끔하지 않다는 것이다."),
 ("Those “gray areas” (like driving on busy city streets) are where AI tools often falter.", "그런 ‘회색 지대’(붐비는 도시 거리에서 운전하는 것 같은)가 AI 도구가 자주 불안정해지는 곳이다."),
 ("Despite years of expert forecasts of their imminent arrival, we don't yet have self-driving cars that can safely replace human drivers, other than in controlled settings.", "자율 주행차가 곧 나올 것이라는 수년간의 전문가 예측에도 불구하고, 통제된 환경을 제외하면 우리에게는 아직 인간 운전자를 안전하게 대체할 수 있는 자율 주행차가 없다."),
 ("That's why some driverless taxis created chaos on the streets of San Francisco.", "그래서 일부 무인 택시가 샌프란시스코 거리에서 혼란을 일으킨 것이다."),
 ("Despite years of optimistic predictions, many AI tools cannot yet be trusted in open-world environments, where the human stakes are high, and failure means real, permanent loss.", "수년간의 낙관적인 예측에도 불구하고, 많은 AI 도구는 인간에게 걸린 위험이 크고 실패가 실제적이고 영구적인 손실을 의미하는 열린 세계 환경에서는 아직 신뢰받을 수 없다."),
 ("AI performance in these areas can still improve, as the size of AI models grows, and they are trained on more human driving data.", "AI 모델의 규모가 커지고 더 많은 인간 운전 데이터로 훈련됨에 따라, 이런 분야에서의 AI 성능은 여전히 향상될 수 있다."),
 ("But they will improve only by mirroring more of the patterns found in our intelligent performances, as we cope with a world that no data set can ever contain.", "그러나 그것들은 어떤 데이터 세트도 결코 담아낼 수 없는 세상에 우리가 대처할 때 보이는 지적인 수행에서 발견되는 패턴을 더 많이 반영해야만 향상될 것이다."),
]
day(33, 'q33', '빈칸', '빈칸 추론 · But 뒤에서 첫 문장의 주제로 돌아오기', '다음 빈칸에 들어갈 말로 가장 적절한 것은?', T33,
 ['data sets can easily predict', 'clear rules and boundaries dominate', 'humans cannot influence in any way', 'we have under control owing to AI', 'no data set can ever contain'], 4,
 '글의 핵심: 인간의 과제는 규칙과 경계가 깔끔하지 않은 “회색 지대”이고, 열린 세계에서 AI는 아직 믿을 수 없다. 데이터가 늘면 나아지긴 하지만(can still improve), But 결국 “어떤 데이터 세트도 다 담을 수 없는” 세상에 대처하는 인간의 지적 수행을 닮아야만 나아진다.',
 ['① 데이터 세트가 쉽게 예측할 수 있는 세상 → 정반대예요.', '② 명확한 규칙과 경계가 지배하는 세상 → 첫 문장과 반대예요.', '③ 인간이 어떤 식으로도 영향을 줄 수 없는 세상 → 근거가 없어요.', '④ AI 덕분에 우리가 통제하는 세상 → AI는 아직 믿을 수 없다고 했어요.'],
 '빈칸 문장 앞에 But이 있으면 앞 내용(데이터가 늘면 나아진다)을 뒤집는 말이 와요. 첫 문장의 주제(규칙·경계가 깔끔하지 않다)와 같은 방향인지 확인하세요.',
 [(T33[0][0], T33[0][1], "not nearly as ~ 전혀 ~하지 않은 · that절이 문장의 보어"),
  (T33[4][0], T33[4][1], "Despite + 명사 ~에도 불구하고 · 콤마 + where (선행사 open-world environments) · stakes 걸려 있는 위험"),
  (T33[6][0], T33[6][1], "only by -ing ~해야만 · the patterns found in ~ (과거분사 수식) · a world that no data set can ever contain (목적격 관계대명사)")],
 [('obstacle', '장애물'), ('setting', '환경'), ('tidy', '깔끔한'), ('boundary', '경계'), ('gray area', '회색 지대'), ('falter', '불안정해지다, 흔들리다'),
  ('forecast', '예측'), ('imminent', '임박한'), ('replace', '대체하다'), ('controlled', '통제된'), ('chaos', '혼란'), ('optimistic', '낙관적인'),
  ('stakes', '(걸려 있는) 위험, 이해관계'), ('permanent', '영구적인'), ('mirror', '반영하다'), ('cope with', '~에 대처하다'), ('contain', '담다, 포함하다'), ('dominate', '지배하다')],
 ['obstacle', 'setting', 'tidy', 'boundary', 'falter', 'forecast', 'imminent', 'replace', 'chaos', 'optimistic', 'permanent', 'contain'],
 blank='no data set can ever contain', notes='* falter: 불안정해지다 ** imminent: 임박한', three=True)

# ═══ DAY 18 · 27번 안내문 불일치 ═══
T27 = [
 ("Ice Hockey Club Recruitment", "아이스하키 클럽 회원 모집"), ("Who We Are Looking For", "모집 대상"),
 ("We are open to all adults.", "모든 성인에게 열려 있습니다."), ("No prior skating experience is necessary.", "사전 스케이팅 경험은 필요하지 않습니다."),
 ("Schedule & Location", "일정 및 장소"), ("Practice is on every Friday, 7:00 p.m. – 10:00 p.m.", "연습은 매주 금요일 오후 7시~10시입니다."),
 ("Location is at Pinewood Ice Rink.", "장소는 Pinewood 아이스링크입니다."), ("Member Benefits", "회원 혜택"),
 ("A free introductory lesson is offered to new members.", "신규 회원에게는 무료 입문 강습이 제공됩니다."), ("Equipment is available for free rental.", "장비는 무료로 대여할 수 있습니다."),
 ("Professional hockey players offer one-on-one coaching.", "프로 하키 선수가 일대일 코칭을 제공합니다."), ("Inter-club matches are held once a month.", "클럽 간 경기는 한 달에 한 번 열립니다."),
]
H27 = {"Ice Hockey Club Recruitment", "Who We Are Looking For", "Schedule & Location", "Member Benefits"}
day(27, 'q27', '안내문 불일치', '안내문 · 횟수(once / twice)와 숫자 대조', 'Ice Hockey Club Recruitment에 관한 다음 안내문의 내용과 일치하지 <u>않는</u> 것은?', T27,
 ['사전 스케이팅 경험이 필요하지 않다.', '연습은 매주 금요일에 있다.', '신규 회원에게는 무료 입문 강습이 제공된다.', '장비를 무료로 대여할 수 있다.', '클럽 간 경기는 한 달에 두 번 열린다.'], 4,
 'Inter-club matches are held once a month → 한 달에 “한 번” 열려요. 두 번이 아니에요.',
 ['① No prior skating experience is necessary → 일치', '② Practice is on every Friday → 일치', '③ A free introductory lesson is offered to new members → 일치', '④ Equipment is available for free rental → 일치'],
 '안내문은 선택지의 숫자·요일·횟수·무료/유료를 본문과 하나씩 대조하세요. once(한 번) / twice(두 번)를 꼭 확인!',
 [("No prior skating experience is necessary.", "사전 스케이팅 경험은 필요하지 않습니다.", "prior 사전의, 이전의 · necessary 필요한"),
  ("Equipment is available for free rental.", "장비는 무료로 대여할 수 있습니다.", "be available for ~에 이용할 수 있다 · rental 대여"),
  ("Inter-club matches are held once a month.", "클럽 간 경기는 한 달에 한 번 열립니다.", "inter- ~ 사이의 · be held 열리다 · once a month 한 달에 한 번")],
 [('recruitment', '모집'), ('prior', '사전의, 이전의'), ('experience', '경험'), ('necessary', '필요한'), ('schedule', '일정'), ('rink', '(스케이트) 링크'),
  ('benefit', '혜택'), ('introductory', '입문의'), ('equipment', '장비'), ('available', '이용할 수 있는'), ('rental', '대여'), ('professional', '프로의, 전문적인'),
  ('one-on-one', '일대일의'), ('inter-club', '클럽 간의'), ('be held', '열리다')],
 ['recruitment', 'prior', 'necessary', 'schedule', 'benefit', 'introductory', 'equipment', 'available', 'rental', 'professional'],
 paras=[lines_html(T27, H27)])

# ═══ DAY 19 · 39번 문장 삽입 ═══
G39 = "But it would be a mistake to say that scientific truths are the only ones we can ever know for certain."
S39 = [
 ("Science is the study of things that can be observed or measured in our material reality.", "과학은 우리의 물질적 현실에서 관찰되거나 측정될 수 있는 것들에 관한 연구이다."),
 ("We have built the modern world on a set of processes that we call the scientific method that advance our understanding of the nature of that reality.", "우리는 과학적 방법이라고 부르는, 그 현실의 본질에 대한 이해를 증진하는 일련의 과정 위에 현대 세계를 세웠다."),
 ("Metaphysics, on the other hand, is the study of the things that lie outside of that material reality, such as the nature of the mind, consciousness, being, causality, and, well, pretty much everything we wonder about but don't have a scientific way to investigate.", "반면에 형이상학은 그 물질적 현실 밖에 있는 것들, 예를 들어 마음의 본질, 의식, 존재, 인과 관계, 그리고 음, 우리가 궁금해하지만 과학적으로 조사할 방법이 없는 거의 모든 것에 관한 연구이다."),
 ("The line between the two is fuzzy, and it shifts as science solves old mysteries and uncovers new ones.", "둘 사이의 경계는 불분명하며, 과학이 오래된 수수께끼를 풀고 새로운 수수께끼를 밝혀냄에 따라 그 경계는 이동한다."),
 ("Rather, they are the only ones we can prove — a very different thing.", "오히려 그것들은 우리가 증명할 수 있는 유일한 진리이다. 이것은 (아는 것과는) 매우 다른 것이다."),
 ("In point of fact, the vast majority of what you know cannot be scientifically proven.", "사실, 여러분이 아는 것의 대다수는 과학적으로 증명될 수 없다."),
 ("The old reporter's adage, “If your mother says she loves you, check it out,” is funny because you can't check it out, but you can obviously know it to be true.", "“어머니가 너를 사랑한다고 말하면, 확인해 봐라.”라는 기자들의 오래된 격언은 재미있는데, 여러분은 그것을 확인할 수 없지만 그것이 사실이라는 것은 분명히 알 수 있기 때문이다."),
]
day(39, 'q39', '삽입', '문장 삽입 · 주어진 문장 뒤의 Rather, they가 이어지는 곳', '글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳은?',
 [(G39, "[주어진 문장] 그러나 과학적 진리가 우리가 확실히 알 수 있는 유일한 진리라고 말하는 것은 잘못일 것이다.")] + S39[:4] + [(G39, "(③ 자리) 그러나 과학적 진리가 우리가 확실히 알 수 있는 유일한 진리라고 말하는 것은 잘못일 것이다.")] + S39[4:],
 ['①', '②', '③', '④', '⑤'], 2,
 '③ 뒤의 Rather(오히려)와 they(= scientific truths)가 단서예요. “과학적 진리가 확실히 알 수 있는 유일한 것이라는 말은 잘못이다. 오히려 그것은 우리가 ‘증명할 수 있는’ 유일한 것이다.” 아는 것과 증명하는 것은 매우 다르다는 흐름이에요. 주어진 문장이 없으면 ③ 뒤의 they와 Rather가 가리킬 대상이 없어요.',
 ['①② 아직 과학과 형이상학을 정의하는 중이라, “과학적 진리만 확실히 알 수 있다”는 말을 반박할 맥락이 아니에요.', '④⑤ 뒤 문장(증명할 수 없는 것이 대다수, 어머니의 사랑)은 이미 “알지만 증명할 수 없는 것”의 예라서, 주어진 문장이 그 뒤에 오면 늦어요.'],
 '삽입 문제는 주어진 문장 뒤에 이어질 말(Rather, they)이 바로 다음 문장에 있는지 확인하세요. “A가 아니다 → Rather B다” 구조는 강력한 단서예요.',
 [(G39, "그러나 과학적 진리가 우리가 확실히 알 수 있는 유일한 진리라고 말하는 것은 잘못일 것이다.", "가주어 it ~ 진주어 to say · the only ones (that) we can ever know (ones = truths) · for certain 확실히"),
  (S39[4][0], S39[4][1], "Rather 오히려 (앞 내용을 바로잡음) · they = scientific truths · a very different thing (앞 내용 전체를 덧붙여 설명)"),
  (S39[6][0], S39[6][1], "because절 안 can't ~, but can ~ 대조 · know + O + to be true ~가 사실이라는 것을 알다")],
 [('scientific truth', '과학적 진리'), ('for certain', '확실히'), ('observe', '관찰하다'), ('measure', '측정하다'), ('material reality', '물질적 현실'), ('scientific method', '과학적 방법'),
  ('advance', '증진하다, 발전시키다'), ('metaphysics', '형이상학'), ('consciousness', '의식'), ('causality', '인과 관계'), ('investigate', '조사하다'), ('fuzzy', '불분명한'),
  ('shift', '이동하다, 바뀌다'), ('uncover', '밝혀내다'), ('rather', '오히려'), ('prove', '증명하다'), ('vast majority', '대다수'), ('adage', '격언')],
 ['observe', 'measure', 'advance', 'metaphysics', 'consciousness', 'causality', 'investigate', 'fuzzy', 'shift', 'uncover', 'prove', 'adage'],
 given=G39, paras=[esc(S39[0][0]) + ' ' + esc(S39[1][0]) + ' ( ① ) ' + esc(S39[2][0]) + ' ( ② ) ' + esc(S39[3][0]) + ' ( ③ ) ' + esc(S39[4][0]) + ' ( ④ ) ' + esc(S39[5][0]) + ' ( ⑤ ) ' + esc(S39[6][0])],
 notes='* fuzzy: 불분명한 ** adage: 격언')
DAYS[-1]['passage'] = [l for l in DAYS[-1]['passage'] if not l[2].startswith('[주어진 문장]')]  # 지문 탭: 정답 자리에 넣어 바른 순서로

# ═══ DAY 20 · 30번 어휘 ═══
T30 = [
 ("At the base of the status hierarchy among performers are cover bands, which are often accorded little critical artistic weight.", "연주자들 사이의 지위 위계의 맨 아래에는 커버 밴드가 있는데, 이들은 흔히 비평적·예술적 무게를 거의 인정받지 못한다."),
 ("Reliance on someone else's material concedes that you have nothing of your own to say.", "다른 사람의 곡에 의존하는 것은 자신만의 할 말이 없다는 것을 인정하는 것이다."),
 ("However, playing covers fulfills aesthetic, educational and economic roles.", "그러나 커버곡을 연주하는 것은 미적, 교육적, 경제적 역할을 한다."),
 ("Some covers take the original recording as a starting point and modify or reinvent it creatively.", "어떤 커버곡은 원곡 녹음을 출발점으로 삼아 그것을 창의적으로 수정하거나 재창조한다."),
 ("Bands starting out rely on cover versions for a large part of their repertoire out of necessity, mastering them as part of a learning process.", "막 시작하는 밴드는 필요에 의해 레퍼토리의 많은 부분을 커버곡에 의존하며, 학습 과정의 일부로 그것들을 익힌다."),
 ("Even ‘original’ performers will usually play a few covers.", "‘자작곡’ 연주자들조차 보통 커버곡을 몇 곡 연주한다."),
 ("The distinction between ‘cover’ and ‘original’ is crucial, since upward career mobility is directly tied to notions of originality.", "‘커버’와 ‘자작곡’의 구분은 매우 중요한데, 경력상의 상승 이동이 독창성이라는 개념과 직접 연결되어 있기 때문이다. (시험지의 absent → crucial)"),
 ("Learning such songs is part of the apprenticeship process in acquiring musicianship through engaging with a musical tradition.", "그런 곡을 배우는 것은 음악적 전통에 참여함으로써 음악적 기량을 습득하는 수습 과정의 일부이다."),
 ("An example is the development of ‘rock’ in England in the 1960s through local bands covering imported copies of American rhythm and blues hits.", "한 예가 1960년대 영국에서 지역 밴드들이 수입된 미국 리듬 앤 블루스 히트곡 음반을 커버하면서 ‘록’이 발전한 것이다."),
 ("Cover songs are literally music to the ears of the managers of pubs and the like, as they are tapping into a proven product that the audience can identify with.", "커버곡은 말 그대로 술집 같은 곳의 관리자들에게는 반가운 소식인데, 청중이 공감할 수 있는 검증된 상품을 활용하는 것이기 때문이다."),
 ("For each new generation of listeners, a ‘good’ song is a good song.", "새로운 세대의 청취자들 각각에게도 ‘좋은’ 노래는 좋은 노래이다."),
]
Q30 = ("At the base of the status hierarchy among performers are cover bands, which are often accorded little critical artistic weight. Reliance on someone else's material concedes that you have nothing of your own to say. "
       "However, playing covers ①<u>fulfills</u> aesthetic, educational and economic roles. Some covers take the original recording as a starting point and modify or reinvent it creatively. "
       "Bands starting out rely on cover versions for a large part of their repertoire out of necessity, ②<u>mastering</u> them as part of a learning process. Even ‘original’ performers will usually play a few covers. "
       "The distinction between ‘cover’ and ‘original’ is ③<u>absent</u>, since upward career mobility is directly tied to notions of originality. "
       "Learning such songs is part of the apprenticeship process in acquiring musicianship through ④<u>engaging</u> with a musical tradition. "
       "An example is the development of ‘rock’ in England in the 1960s through local bands covering imported copies of American rhythm and blues hits. "
       "Cover songs are literally music to the ears of the managers of pubs and the like, as they are tapping into a ⑤<u>proven</u> product that the audience can identify with. For each new generation of listeners, a ‘good’ song is a good song.")
day(30, 'q30', '어휘', '어휘 · since 뒤의 이유와 밑줄 낱말이 맞는지', '다음 글의 밑줄 친 부분 중, 문맥상 낱말의 쓰임이 적절하지 <u>않은</u> 것은?', T30,
 ['① fulfills', '② mastering', '③ absent', '④ engaging', '⑤ proven'], 2,
 'since 이하에서 “경력의 상승이 독창성 개념과 직접 연결되어 있다”고 해요. 독창성이 경력을 좌우하니 커버와 자작곡의 구분은 “없는(absent)” 게 아니라 “매우 중요한(crucial, important)” 거예요.',
 ['① fulfills: However 뒤 → 무시당하는 커버곡도 미적·교육적·경제적 역할을 “한다” ✔', '② mastering: 시작하는 밴드는 학습 과정으로 커버곡을 “익힌다” ✔', '④ engaging: 음악적 전통에 “참여함”으로써 기량을 습득 ✔', '⑤ proven: 청중이 공감할 수 있는 “검증된” 상품 → 술집 관리자가 반기는 이유 ✔'],
 '어휘 문제는 이유를 나타내는 since, because, as 뒤의 내용과 밑줄 낱말이 논리적으로 맞는지 확인하세요.',
 [(T30[0][0], T30[0][1], "장소 부사구(At the base of ~) + 동사(are) + 주어(cover bands) 도치 · accord A B A에게 B를 부여하다 → 수동 be accorded little weight"),
  (T30[4][0], T30[4][1], "Bands (which are) starting out · out of necessity 필요에 의해 · 분사구문 mastering them"),
  (T30[9][0], T30[9][1], "music to one's ears 반가운 소식 · tap into ~을 활용하다 · identify with ~에 공감하다 · as ~ 때문에")],
 [('status', '지위'), ('hierarchy', '위계'), ('accord', '부여하다'), ('critical', '비평의'), ('reliance', '의존'), ('concede', '인정하다'),
  ('fulfill', '(역할을) 다하다'), ('aesthetic', '미적인'), ('modify', '수정하다'), ('reinvent', '재창조하다'), ('repertoire', '레퍼토리, 연주 목록'), ('out of necessity', '필요에 의해'),
  ('distinction', '구분'), ('upward mobility', '상승 이동'), ('originality', '독창성'), ('apprenticeship', '수습 기간'), ('musicianship', '음악적 기량'), ('tap into', '~을 활용하다'),
  ('proven', '검증된'), ('identify with', '~에 공감하다')],
 ['status', 'hierarchy', 'reliance', 'concede', 'aesthetic', 'modify', 'reinvent', 'repertoire', 'distinction', 'originality', 'apprenticeship', 'proven'],
 paras=[Q30], notes='* accord: 부여하다 ** concede: 인정하다 *** apprenticeship: 수습 기간', three=True)

# ═══ DAY 21 · 25번 도표 ═══
T25 = [
 ("The graph above shows the percentages of Canadians' preferred reading formats by age group, based on a survey conducted in 2025.", "위 도표는 2025년에 실시된 설문 조사를 바탕으로 연령대별 캐나다인이 선호하는 독서 형식의 비율을 보여 준다."),
 ("In all age groups, Print Books were the most preferred reading format, with the 55-64 age group showing the highest preference at 71%.", "① 모든 연령대에서 종이책이 가장 선호되는 독서 형식이었으며, 55~64세 연령대가 71%로 가장 높은 선호도를 보였다."),
 ("The percentage of people who preferred Ebooks was the highest in the 18-29 age group, followed by the 30-44 age group.", "② 전자책을 선호한 사람들의 비율은 18~29세 연령대에서 가장 높았고, 30~44세 연령대가 그 뒤를 이었다."),
 ("While the preference for Ebooks was higher than that for Audiobooks in the 18-29 age group, the opposite was true in both the 30-44 and 45-54 age groups.", "③ 18~29세 연령대에서는 전자책에 대한 선호도가 오디오북에 대한 선호도보다 높았지만, 30~44세와 45~54세 연령대에서는 둘 다 그 반대였다."),
 ("The percentage of people who answered No Preference was highest in the 30-44 age group at 11%, which was more than twice that of the 45-54 age group.", "④ [틀린 문장] 선호 없음이라고 답한 사람들의 비율은 30~44세 연령대에서 11%로 가장 높았는데, 이는 45~54세 연령대(7%)의 두 배가 넘었다. → 7%의 두 배는 14%예요."),
 ("In the 55-64 age group, the percentage of people who preferred Audiobooks and the percentage of people who showed No Preference were both lower than that for Ebooks.", "⑤ 55~64세 연령대에서는 오디오북을 선호한 사람들의 비율과 선호 없음을 보인 사람들의 비율이 둘 다 전자책의 비율보다 낮았다."),
]
TD = 'style="border:1px solid var(--line);padding:4px 2px;text-align:center;white-space:nowrap"'
ROWS25 = [('18-29', 52, 24, 21, 3), ('30-44', 49, 18, 22, 11), ('45-54', 60, 14, 18, 7), ('55-64', 71, 13, 8, 8)]
CH25 = ('<b>Canadians\' Preferred Reading Formats by Age Group in 2025</b> (%)'
        '<table style="border-collapse:collapse;width:100%;font-size:12px;margin:6px 0;table-layout:fixed">'
        '<tr>' + ''.join('<th %s>%s</th>' % (TD, h) for h in ('Age', 'Print<br>Books', 'Ebooks', 'Audio-<br>books', 'No<br>Pref.')) + '</tr>'
        + ''.join('<tr>' + ''.join('<td %s>%s</td>' % (TD, v) for v in r) + '</tr>' for r in ROWS25) + '</table>'
        '<small>No Pref. = No Preference · Note: Percentages may not sum to 100% due to rounding.</small>')
day(25, 'q25', '도표', '도표 · twice, followed by, the opposite를 직접 계산', '다음 도표의 내용과 일치하지 <u>않는</u> 것은?', T25,
 ['①', '②', '③', '④', '⑤'], 3,
 '선호 없음(No Preference): 30~44세 11%, 45~54세 7%. 7%의 두 배는 14%이므로 11%는 두 배가 넘지 않아요(약 1.6배).',
 ['① 종이책이 모든 연령대에서 1위, 55~64세 71%가 최고 ✔', '② 전자책: 18~29세 24% > 30~44세 18% > 45~54세 14% > 55~64세 13% ✔', '③ 18~29세 전자책 24 > 오디오북 21 / 30~44세 18 < 22 / 45~54세 14 < 18 ✔', '⑤ 55~64세 오디오북 8, 선호 없음 8, 전자책 13 → 둘 다 전자책보다 낮음 ✔'],
 '도표 문제는 twice(두 배), more than, the opposite, followed by 같은 비교 표현이 나오면 실제로 계산해 보세요. 숫자 하나하나를 표와 대조하는 게 정답률을 올리는 방법이에요.',
 [(T25[1][0], "모든 연령대에서 종이책이 가장 선호되는 독서 형식이었으며, 55~64세 연령대가 71%로 가장 높은 선호도를 보였다.", "with + O + -ing (~가 …하면서) 부대상황"),
  (T25[2][0], "전자책을 선호한 사람들의 비율은 18~29세 연령대에서 가장 높았고, 30~44세 연령대가 그 뒤를 이었다.", "followed by ~ ~이 그 뒤를 이은 (2위 표현)"),
  (T25[4][0], "선호 없음의 비율은 30~44세에서 11%로 가장 높았는데, 이는 45~54세의 두 배가 넘었다(→ 틀림).", "콤마 + which (앞의 11%) · more than twice that of ~ ~의 두 배가 넘는 (that = the percentage)")],
 [('percentage', '비율'), ('preferred', '선호되는'), ('format', '형식'), ('age group', '연령대'), ('survey', '설문 조사'), ('conduct', '실시하다'),
  ('print book', '종이책'), ('preference', '선호(도)'), ('followed by', '~이 뒤를 이은'), ('the opposite', '반대'), ('twice', '두 배'), ('rounding', '반올림'), ('sum to', '합계가 ~이 되다')],
 ['percentage', 'format', 'survey', 'conduct', 'preference', 'twice', 'rounding'],
 paras=[CH25, esc(T25[0][0]) + ' ①' + esc(T25[1][0]) + ' ②' + esc(T25[2][0]) + ' ③' + esc(T25[3][0]) + ' ④' + esc(T25[4][0]) + ' ⑤' + esc(T25[5][0])])

# ═══ DAY 22 · 34번 빈칸 ═══
T34 = [
 ("Commercial culture — generating the stories, images, and sounds that mattered most to the public — pushed folk culture practices underground.", "대중에게 가장 중요했던 이야기, 이미지, 소리를 만들어 낸 상업 문화는 민속 문화 관습을 지하로 밀어냈다."),
 ("People still composed and sang songs and amateur writers still scribbled verse.", "사람들은 여전히 노래를 짓고 불렀으며, 아마추어 작가들은 여전히 시를 끄적거렸다."),
 ("At the same time, grassroots fan communities emerged in response to mass media content.", "동시에, 대중 매체 콘텐츠에 반응하여 풀뿌리 팬 공동체가 생겨났다."),
 ("Some media scholars hold on to the useful distinction between mass culture (a category of production) and popular culture (a category of consumption).", "일부 미디어 학자들은 대량 문화(생산의 범주)와 대중문화(소비의 범주) 사이의 유용한 구분을 고수한다."),
 ("They argue that popular culture is what happens to the materials of mass culture when they get into the hands of consumers, when a song played on the radio becomes so associated with a particularly romantic evening that two young lovers decide to call it “our song,” or when a fan becomes so fascinated with a particular television series that it inspires her to write original stories about its characters.",
  "그들은 대중문화란 대량 문화의 재료가 소비자의 손에 들어갔을 때 그것에 일어나는 일이라고 주장하는데, 라디오에서 나온 노래가 특히 낭만적인 어느 저녁과 너무 밀접하게 연관되어 두 젊은 연인이 그것을 ‘우리 노래’라고 부르기로 할 때, 또는 한 팬이 특정 텔레비전 시리즈에 너무 매료되어 그것이 그녀에게 등장인물들에 관한 독창적인 이야기를 쓰도록 영감을 줄 때가 그렇다."),
 ("In other words, popular culture is what happens as mass culture gets pulled back into folk culture.", "다시 말해, 대중문화는 대량 문화가 민속 문화 속으로 다시 끌려 들어갈 때 일어나는 일이다."),
 ("The culture industries never really had to confront the existence of this alternative cultural economy because, for the most part, it existed behind closed doors and its products circulated only among a small circle of friends and neighbors.", "문화 산업은 이 대안적 문화 경제의 존재에 정면으로 맞설 필요가 전혀 없었는데, 대부분의 경우 그것은 닫힌 문 뒤에 존재했고 그 산물은 친구와 이웃의 작은 무리 안에서만 유통되었기 때문이다."),
]
day(34, 'q34', '빈칸', '빈칸 추론 · In other words 뒤 = 앞 예시의 요약 + 첫 문장 핵심어', '다음 빈칸에 들어갈 말로 가장 적절한 것은?', T34,
 ['fans react to media content as its producers intended', 'mass culture gets pulled back into folk culture', 'the market blocks otherwise accessible content', 'culture industries import unknown folk practices', 'the industry popularizes overlooked cultural practices'], 1,
 '대중문화의 예: 라디오 노래를 “우리 노래”라 부르기, 드라마 팬이 직접 이야기 쓰기 → 상업적으로 만들어진 대량 문화가 사람들의 손에서 다시 “직접 짓고 부르고 쓰는” 민속 문화처럼 바뀌어요. 첫 부분의 민속 문화(직접 노래를 짓고, 시를 끄적거림)와 연결돼요.',
 ['① 제작자가 의도한 대로 반응 → 오히려 소비자가 자기 방식으로 바꿔요.', '③ 시장이 콘텐츠를 막는다 → 근거가 없어요.', '④ 문화 산업이 민속 관습을 들여온다 → 방향이 반대예요(소비자가 대량 문화를 가져가요).', '⑤ 산업이 간과된 관습을 대중화 → 주체가 산업이 아니라 소비자예요.'],
 'In other words 뒤의 빈칸은 바로 앞 예시들을 한 문장으로 바꿔 말한 것이에요. 첫 문장의 핵심어(folk culture)가 다시 나오는 선택지에 주목하세요.',
 [(T34[0][0], T34[0][1], "대시(—) 사이 삽입: 분사구 generating ~이 주어 Commercial culture를 설명 · push A underground A를 지하로 밀어내다"),
  (T34[4][0], T34[4][1], "what happens to ~ (관계대명사 what) · so ~ that … 구문 두 번 · inspire + O + to부정사 ~가 …하도록 영감을 주다"),
  (T34[5][0], T34[5][1], "what happens 명사절 보어 · as ~할 때 · get pulled back into 수동(~ 속으로 다시 끌려 들어가다)")],
 [('commercial', '상업적인'), ('generate', '만들어 내다'), ('matter', '중요하다'), ('folk culture', '민속 문화'), ('underground', '지하로, 비밀리에'), ('compose', '(곡을) 짓다'),
  ('scribble', '끄적거리다'), ('verse', '시, 운문'), ('grassroots', '풀뿌리의'), ('emerge', '생겨나다'), ('in response to', '~에 반응하여'), ('scholar', '학자'),
  ('consumption', '소비'), ('associated with', '~와 연관된'), ('fascinated', '매료된'), ('inspire', '영감을 주다'), ('confront', '맞서다'), ('alternative', '대안적인'), ('circulate', '유통되다')],
 ['commercial', 'generate', 'compose', 'scribble', 'verse', 'grassroots', 'emerge', 'scholar', 'consumption', 'fascinated', 'confront', 'circulate'],
 blank='mass culture gets pulled back into folk culture', notes='* scribble: 끄적거리다', three=True)

# ═══ DAY 23 · 28번 안내문 일치 ═══
T28 = [
 ("E-Bike City Tour", "전기 자전거 시티 투어"), ("Explore the city's hidden spots on an E-Bike!", "전기 자전거를 타고 도시의 숨은 명소를 둘러보세요!"),
 ("Schedule & Meeting Site", "일정 및 집합 장소"), ("Schedule: Every Saturday at 10 a.m.", "일정: 매주 토요일 오전 10시"), ("Meeting Site: Riverside Park North Entrance", "집합 장소: Riverside 공원 북문"),
 ("Program Details", "프로그램 세부 사항"), ("Safety training on braking and signaling (30 mins)", "제동과 수신호에 관한 안전 교육 (30분)"), ("Guided group tour along the city path (1 hour)", "도시 길을 따라가는 가이드 단체 투어 (1시간)"),
 ("Participation Requirements", "참가 조건"), ("Age: Must be 16 years or older (valid ID required)", "나이: 16세 이상이어야 함 (유효한 신분증 필요)"), ("Maximum Speed: 30 km/h", "최고 속도: 시속 30km"),
 ("Fees", "요금"), ("$25 per person", "1인당 25달러"), ("10% off the total for groups of 4 or more", "4인 이상 단체는 총액에서 10% 할인"),
 ("(full refund if canceled 2 days before the tour but non-refundable after that)", "(투어 2일 전에 취소하면 전액 환불되지만 그 이후에는 환불 불가)"),
]
H28 = {"E-Bike City Tour", "Schedule & Meeting Site", "Program Details", "Participation Requirements", "Fees"}
day(28, 'q28', '안내문 일치', '안내문 일치 · 나머지 넷이 모두 틀렸는지 확인', 'E-Bike City Tour에 관한 다음 안내문의 내용과 일치하는 것은?', T28,
 ['일요일마다 오전 10시에 진행된다.', '안전 교육은 1시간 동안 진행된다.', '16세 미만은 신분증이 있어야 참여할 수 있다.', '4인 이상의 단체는 할인을 받을 수 있다.', '투어 전날 취소하면 전액 환불받을 수 있다.'], 3,
 '10% off the total for groups of 4 or more → 4인 이상 단체는 총액에서 10% 할인을 받아요.',
 ['① Every Saturday → 일요일이 아니라 토요일이에요.', '② 안전 교육은 30분이에요. 1시간은 단체 투어 시간이에요.', '③ 16세 이상만 참여할 수 있어요(신분증은 16세 이상도 필요해요).', '⑤ 2일 전까지 취소해야 전액 환불이고, 그 뒤(전날)는 환불이 안 돼요.'],
 '일치하는 것 고르기는 나머지 넷이 모두 틀렸는지까지 확인해야 해요. 30 mins / 1 hour처럼 숫자가 섞인 함정, or older(이상)와 under(미만)를 조심하세요.',
 [("Age: Must be 16 years or older (valid ID required)", "나이: 16세 이상이어야 함 (유효한 신분증 필요)", "or older ~ 이상 · valid 유효한 · (is) required 필요한"),
  ("10% off the total for groups of 4 or more", "4인 이상 단체는 총액에서 10% 할인", "off ~ 할인 · the total 총액 · or more ~ 이상"),
  ("(full refund if canceled 2 days before the tour but non-refundable after that)", "(투어 2일 전에 취소하면 전액 환불되지만 그 이후에는 환불 불가)", "full refund 전액 환불 · if (it is) canceled · non-refundable 환불 불가의")],
 [('explore', '둘러보다, 탐험하다'), ('hidden', '숨겨진'), ('meeting site', '집합 장소'), ('entrance', '입구'), ('braking', '제동'), ('signaling', '신호 보내기'),
  ('guided', '가이드가 안내하는'), ('participation', '참가'), ('requirement', '요건, 조건'), ('valid', '유효한'), ('maximum', '최대의'), ('fee', '요금'),
  ('refund', '환불'), ('cancel', '취소하다'), ('non-refundable', '환불 불가의')],
 ['explore', 'hidden', 'entrance', 'braking', 'participation', 'requirement', 'valid', 'maximum', 'refund', 'cancel'],
 paras=[lines_html(T28, H28)])

# ═══ DAY 24 · 41·42번 장문 ═══
T41 = [
 ("Music allows several individuals to produce sounds together.", "음악은 여러 개인이 함께 소리를 만들어 내게 해 준다."),
 ("Notably, only humans can synchronize their movements (including vocalizations) flexibly in a group to an external pulse.", "특히 오직 인간만이 집단 속에서 외부의 박자에 맞춰 자신의 움직임(발성 포함)을 유연하게 동기화할 수 있다."),
 ("This ability is possibly the simplest cognitive function that just separates us from animals, which would make music the decisive evolutionary step of the Homo sapiens.", "이 능력은 아마 우리를 동물과 구별해 주는 가장 단순한 인지 기능일 것이고, 이것은 음악을 호모 사피엔스의 결정적인 진화 단계로 만들 것이다."),
 ("Animals have “song” and “drumming”, but gorillas do not drum in synchrony, and whales do not sing in unison.", "동물에게도 ‘노래’와 ‘북치기’가 있지만, 고릴라는 박자를 맞춰 북을 치지 않고, 고래는 다 함께 같은 음으로 노래하지 않는다."),
 ("Making music together in a group, that is, joint synchronized action, is a powerful elicitor of social bonding.", "집단 속에서 함께 음악을 만드는 것, 즉 공동의 동기화된 행동은 사회적 유대를 강력하게 유발하는 요인이다."),
 ("Comparable to Robin Dunbar's vocal grooming hypothesis, music might have replaced manual grooming as the main mechanism for social bonding during human evolution.", "Robin Dunbar의 음성 털 고르기 가설과 비슷하게, 음악은 인간 진화 과정에서 사회적 유대를 위한 주요 기제로서 손으로 하는 털 고르기를 대체했을지도 모른다."),
 ("Dunbar's hypothesis is based on the observation that, similar to manual grooming, human language plays a key role in building and maintaining affiliative bonds and group cohesion.", "Dunbar의 가설은, 손으로 하는 털 고르기와 마찬가지로 인간의 언어가 친밀한 유대와 집단 결속을 형성하고 유지하는 데 핵심적인 역할을 한다는 관찰에 근거한다."),
 ("This process is supposedly driven by increased group size, which increases the number of social relationships an individual needs to maintain and monitor.", "이 과정은 아마 집단 규모의 증가에 의해 촉진되었을 것인데, 집단 규모의 증가는 한 개인이 유지하고 살펴야 하는 사회적 관계의 수를 늘린다."),
 ("Once the number of relationships becomes too large, an individual can no longer maintain its social networks with tactile interactions alone, and selection will favor alternative mechanisms such as talking to several individuals at the same time.", "일단 관계의 수가 너무 많아지면, 개인은 더 이상 촉각적 상호 작용만으로는 사회적 관계망을 유지할 수 없게 되고, 자연 선택은 여러 개인에게 동시에 말하기와 같은 대안적 기제를 선호할 것이다. (시험지의 reject → favor)"),
 ("However, many more individuals can make music in a group, and thus establish and foster social relationships.", "그러나 훨씬 더 많은 개인이 집단으로 음악을 만들 수 있고, 그래서 사회적 관계를 형성하고 키울 수 있다."),
 ("This makes music the more obvious candidate to maintain social networks, and increase social cohesion in large groups.", "이것은 음악을 큰 집단에서 사회적 관계망을 유지하고 사회적 결속을 높이는 더 확실한 후보로 만든다."),
 ("Thus a musical grooming hypothesis seems at least as likely to explain the emergence of music as a vocal grooming hypothesis for the emergence of language.", "따라서 음악적 털 고르기 가설은, 언어의 출현에 대한 음성 털 고르기 가설만큼이나 적어도 음악의 출현을 설명할 가능성이 있어 보인다."),
]
def q41():
    t = [esc(e) for e, k in T41]
    rep = [(2, 'just separates', 'just (a)<u>separates</u>'), (5, 'have replaced', 'have (b)<u>replaced</u>'), (7, 'which increases', 'which (c)<u>increases</u>'),
           (8, 'will favor', 'will (d)<u>reject</u>'), (10, 'the more obvious', 'the (e)<u>more obvious</u>')]
    for i, a, b in rep:
        assert t[i].count(a) == 1, a
        t[i] = t[i].replace(a, b)
    return ' '.join(t)
Q41 = q41()
V41 = [('individual', '개인'), ('notably', '특히'), ('synchronize', '동기화하다, 박자를 맞추다'), ('vocalization', '발성'), ('flexibly', '유연하게'), ('external', '외부의'),
       ('pulse', '박자'), ('cognitive', '인지의'), ('decisive', '결정적인'), ('evolutionary', '진화의'), ('in synchrony', '박자를 맞춰, 동시에'), ('in unison', '일제히, 제창으로'),
       ('elicitor', '유발 요인'), ('bonding', '유대'), ('grooming', '털 고르기'), ('hypothesis', '가설'), ('affiliative', '친화적인'), ('cohesion', '결속'),
       ('tactile', '촉각의'), ('favor', '선호하다'), ('foster', '키우다, 촉진하다'), ('candidate', '후보'), ('emergence', '출현')]
K41 = [(T41[2][0], T41[2][1], "콤마 + which (앞 내용 전체) = and this would make ~ · make + O + 명사(music the decisive step)"),
       ("Once the number of relationships becomes too large, an individual can no longer maintain its social networks with tactile interactions alone, and selection will favor alternative mechanisms such as talking to several individuals at the same time.", "일단 관계의 수가 너무 많아지면, 개인은 더 이상 촉각적 상호 작용만으로는 사회적 관계망을 유지할 수 없게 되고, 자연 선택은 여러 개인에게 동시에 말하기 같은 대안적 기제를 선호할 것이다.", "Once 일단 ~하면 · no longer 더 이상 ~않다 · favor 선호하다 (42번 (d) reject의 올바른 말)"),
       (T41[11][0], T41[11][1], "as likely to ~ as … …만큼 ~할 가능성이 있는 · at least 적어도")]
day(41, 'q41', '제목', '장문 제목 · 첫 부분과 결론을 함께 담기', '윗글의 제목으로 가장 적절한 것은?', T41,
 ['Integrating Music into Language Learning', 'Why Humans Evolved to Live in Large Groups', 'How Animals Build Social Bonds Without Language', 'Messages in Melody: Limits in Delivering Intentions', 'Making Music Collectively: What Binds Humans Together'], 4,
 '오직 인간만 집단으로 박자를 맞출 수 있고, 함께 동기화된 음악 만들기(joint synchronized action)가 사회적 유대를 강하게 만든다 → 큰 집단의 결속을 유지하는 기제로 음악이 진화했을 수 있다. → “함께 음악 만들기: 무엇이 인간을 하나로 묶는가”',
 ['① 언어 학습에 음악을 활용하는 이야기는 없어요.', '② 큰 집단은 음악이 필요해진 배경일 뿐, 왜 큰 집단으로 살게 됐는지가 주제가 아니에요.', '③ 동물은 박자를 못 맞춘다는 비교 대상으로만 나와요.', '④ 선율로 의도를 전달하는 한계는 나오지 않아요.'],
 '장문 제목은 첫 부분(인간만 동기화할 수 있다)과 마지막 결론(음악적 털 고르기 가설)을 함께 담은 것을 고르세요.',
 K41, V41, ['synchronize', 'flexibly', 'external', 'cognitive', 'decisive', 'evolutionary', 'bonding', 'hypothesis', 'cohesion', 'tactile', 'foster', 'emergence'],
 paras=[Q41], notes='* unison: 제창 ** elicitor: 유발 요인 *** tactile: 촉각의')
day(42, 'q42', '어휘', '장문 어휘', '밑줄 친 (a)~(e) 중에서 문맥상 낱말의 쓰임이 적절하지 <u>않은</u> 것은? [3점]', T41,
 ['(a) separates', '(b) replaced', '(c) increases', '(d) reject', '(e) more obvious'], 3,
 '관계의 수가 너무 많아 촉각(털 고르기)만으로 유지할 수 없게 되면, 자연 선택은 여러 명에게 동시에 말하기 같은 대안적 기제를 “거부하는(reject)” 게 아니라 “선호할(favor)” 거예요. 그래야 언어(음성 털 고르기)가 등장한 이유가 설명돼요.',
 ['(a) separates: 이 능력이 인간을 동물과 “구별한다” ✔', '(b) replaced: 음악이 손 털 고르기를 “대체했을” 수 있다 ✔', '(c) increases: 집단이 커지면 관계의 수가 “늘어난다” ✔', '(e) more obvious: 훨씬 더 많은 사람이 함께할 수 있으니 “더 확실한” 후보 ✔'],
 '장문 어휘는 Once ~, However 같은 논리 전환 앞뒤에서 방향이 맞는지 확인하세요. “할 수 없게 되면 → 대안을 선호한다”가 자연스러운 흐름이에요.',
 [], V41, [], paras=[Q41], notes='* unison: 제창 ** elicitor: 유발 요인 *** tactile: 촉각의', three=True)
multi('41·42번 장문 (제목·어휘)', 2)

# ═══ DAY 25 · 43~45번 장문 ═══
TA = [("Martin was an experienced woodworker in a small town.", "Martin은 작은 마을의 숙련된 목공이었다."),
      ("His assistant Tom loved creating delicate designs.", "그의 조수 Tom은 섬세한 디자인을 만드는 것을 좋아했다."),
      ("Tom always carried a sketchbook filled with design ideas.", "Tom은 항상 디자인 아이디어로 가득 찬 스케치북을 들고 다녔다."),
      ("One day, a librarian ordered a bookcase for children.", "어느 날, 한 사서가 아이들을 위한 책장을 주문했다."),
      ("Martin confidently started to build a bookcase with thick oak boards.", "Martin은 자신 있게 두꺼운 참나무 판자로 책장을 만들기 시작했다."),
      ("Tom suggested adding a few decorative touches and showed him his sketches.", "Tom은 몇 가지 장식을 더하자고 제안하며 그에게 자신의 스케치를 보여 주었다."),
      ("But Martin just said, “If it can hold books safely, it has done its job.”", "그러나 Martin은 “책을 안전하게 담을 수 있으면 그것으로 제 할 일은 다 한 거야.”라고만 말했다.")]
TB = [("Seeing his frustration, Tom quietly showed his sketches once more.", "그가 좌절한 것을 보고, Tom은 조용히 자신의 스케치를 한 번 더 보여 주었다."),
      ("“Maybe the color isn't the problem,” Tom said.", "“아마 색깔이 문제가 아닐 거예요.” Tom이 말했다."),
      ("“Perhaps a few small details could make a difference.”", "“어쩌면 몇 가지 작은 세부 장식이 차이를 만들 수 있을 거예요.”"),
      ("Martin looked at the sketches.", "Martin은 스케치를 보았다."),
      ("Not having a better idea, he allowed Tom to add some details.", "더 나은 생각이 없었기 때문에, 그는 Tom이 세부 장식을 더하도록 허락했다."),
      ("Tom picked up his brushes and painted flowers on both sides of the bookcase.", "Tom은 붓을 들고 책장 양쪽 측면에 꽃을 그렸다."),
      ("At first, Martin had his doubts, but over time the bookcase came to look better.", "처음에 Martin은 의심했지만, 시간이 지나면서 책장은 더 좋아 보이게 되었다."),
      ("When the workshop grew dark, Martin quietly placed a lamp beside Tom so that he could continue working.", "작업장이 어두워지자, Martin은 그가 작업을 계속할 수 있도록 Tom 옆에 조용히 램프를 놓아 주었다."),
      ("His work was finished late that night.", "그의 작업은 그날 밤늦게 끝났다.")]
TC = [("Several days later, the librarian stopped by to see how the bookcase was coming along.", "며칠 후, 사서가 책장이 어떻게 되어 가는지 보러 들렀다."),
      ("Martin expected praise.", "Martin은 칭찬을 기대했다."),
      ("Instead, the librarian said, “This bookcase is certainly strong and well-made, but it doesn't look like it belongs in a children's library. I wish it looked more playful.”", "그 대신 사서는 “이 책장은 확실히 튼튼하고 잘 만들어졌지만, 어린이 도서관에 어울리는 것 같지는 않아요. 좀 더 재미있어 보이면 좋겠어요.”라고 말했다."),
      ("To solve the issue, Martin painted the bookcase yellow.", "문제를 해결하기 위해 Martin은 책장을 노란색으로 칠했다."),
      ("However, it still looked too plain, and he had to admit that he had no idea what else to do.", "하지만 그것은 여전히 너무 밋밋해 보였고, 그는 달리 무엇을 해야 할지 모르겠다는 것을 인정해야 했다.")]
TDd = [("The next morning, the librarian smiled when she saw the bookcase.", "다음 날 아침, 사서는 책장을 보고 미소 지었다."),
       ("“This is exactly what we hoped for,” she said.", "“이게 바로 저희가 바라던 거예요.” 그녀가 말했다."),
       ("“The kids are going to love it when they see it.”", "“아이들이 보면 정말 좋아할 거예요.”"),
       ("After the librarian left, Martin apologized to Tom.", "사서가 떠난 후, Martin은 Tom에게 사과했다."),
       ("“I was so proud of my work that I forgot the importance of details,” he admitted.", "“내 작품이 너무 자랑스러워서 세부 장식의 중요성을 잊었어.” 그가 인정했다."),
       ("Martin picked up Tom's sketchbook and turned the pages.", "Martin은 Tom의 스케치북을 집어 들고 페이지를 넘겼다."),
       ("Together, they decided to use one of the sketches for their next project.", "함께, 그들은 다음 작업에 스케치 중 하나를 사용하기로 했다."),
       ("Tom was happy that Martin finally came to see the value of the details he had once ignored.", "Tom은 Martin이 마침내 자신이 한때 무시했던 세부 장식의 가치를 알게 된 것이 기뻤다.")]
def ul(T, i, a, b):
    s = esc(T[i][0]); assert s.count(a) == 1, a; return s.replace(a, b)
def para(T, marks):
    out = []
    for i, (e, k) in enumerate(T):
        s = esc(e)
        for j, a, b in marks:
            if j == i: assert s.count(a) == 1, a; s = s.replace(a, b)
        out.append(s)
    return ' '.join(out)
P43 = ['<b>(A)</b> ' + para(TA, [(5, 'showed him', 'showed (a)<u>him</u>')]),
       '<b>(B)</b> ' + para(TB, [(4, 'idea, he allowed', 'idea, (b)<u>he</u> allowed'), (7, 'so that he could', 'so that (c)<u>he</u> could')]),
       '<b>(C)</b> ' + para(TC, [(4, 'and he had', 'and (d)<u>he</u> had')]),
       '<b>(D)</b> ' + para(TDd, [(7, 'details he had', 'details (e)<u>he</u> had')])]
T43 = [('(A) ' + TA[0][0], '(A) ' + TA[0][1])] + TA[1:] + [('(C) ' + TC[0][0], '(C) ' + TC[0][1])] + TC[1:] + [('(B) ' + TB[0][0], '(B) ' + TB[0][1])] + TB[1:] + [('(D) ' + TDd[0][0], '(D) ' + TDd[0][1])] + TDd[1:]
V43 = [('experienced', '숙련된'), ('woodworker', '목공'), ('assistant', '조수'), ('delicate', '섬세한'), ('librarian', '사서'), ('bookcase', '책장'),
       ('oak', '참나무'), ('decorative', '장식의'), ('touch', '(마무리) 손질'), ('stop by', '들르다'), ('come along', '(일이) 되어 가다'), ('praise', '칭찬'),
       ('belong', '어울리다, 속하다'), ('playful', '재미있는, 장난기 있는'), ('plain', '밋밋한'), ('admit', '인정하다'), ('frustration', '좌절'), ('detail', '세부 (장식)'),
       ('doubt', '의심'), ('workshop', '작업장'), ('apologize', '사과하다'), ('ignore', '무시하다')]
K43 = [(TB[4][0], TB[4][1], "분사구문(이유) Not having ~ = Because he didn't have ~ · allow + O + to부정사"),
       (TB[7][0], TB[7][1], "grow + 형용사 ~해지다 · so that + 주어 + could ~할 수 있도록"),
       (TDd[7][0], TDd[7][1], "come to + 동사원형 ~하게 되다 · had ignored 과거완료(그보다 더 이전) · the details (that) he had once ignored")]
day(43, 'q43', '순서', '장문 순서 · 시간 표현과 감정 단서로 잇기', '주어진 글 (A)에 이어질 내용을 순서에 맞게 배열한 것으로 가장 적절한 것은?', T43,
 ['(B) - (D) - (C)', '(C) - (B) - (D)', '(C) - (D) - (B)', '(D) - (B) - (C)', '(D) - (C) - (B)'], 1,
 '(A) Martin은 책장을 튼튼하게만 만듦 → (C) 며칠 후(Several days later) 사서: 어린이 도서관에 안 어울린다 / 노란색으로 칠해도 밋밋, 방법을 모름 → (B) 그의 좌절(his frustration)을 보고 Tom이 스케치를 다시 보여 주고 꽃을 그림, 그날 밤늦게 완성 → (D) 다음 날 아침(The next morning) 사서가 미소, Martin이 사과.',
 ['① (B)가 먼저 오면 his frustration(좌절)의 이유인 사서의 지적이 아직 없어요.', '③ (D)의 “다음 날 아침 만족”이 꽃 그리기(B)보다 먼저 올 수 없어요.', '④⑤ (D)가 (A) 바로 뒤에 오면, 아직 아무것도 고치지 않았는데 사서가 만족하는 셈이에요.'],
 '장문 순서는 시간 표현(Several days later, late that night, The next morning)과 감정 단서(his frustration)를 이어 보세요.',
 K43, V43, ['experienced', 'assistant', 'delicate', 'librarian', 'decorative', 'praise', 'playful', 'plain', 'admit', 'frustration', 'doubt', 'ignore'],
 paras=P43)
day(44, 'q44', '지칭', '장문 지칭', '밑줄 친 (a)~(e) 중에서 가리키는 대상이 나머지 넷과 다른 것은?', T43,
 ['(a)', '(b)', '(c)', '(d)', '(e)'], 2,
 '(c) he = Tom이에요. Martin이 Tom 옆에 램프를 놓아 준 것은 Tom이 작업을 계속할 수 있도록 하기 위해서예요. 나머지는 모두 Martin이에요.',
 ['(a) him: Tom이 스케치를 보여 준 상대 = Martin', '(b) he: Tom이 장식을 더하도록 허락한 사람 = Martin', '(d) he: 달리 무엇을 할지 모르겠다고 인정한 사람 = Martin', '(e) he: 한때 세부 장식을 무시했던 사람 = Martin'],
 '지칭 문제는 밑줄 친 대명사 바로 앞에서 누가 “행동하는 사람”인지 확인하세요. so that 뒤의 he는 “도움을 받는 사람”일 수 있어요.',
 [], V43, [], paras=P43)
day(45, 'q45', '내용 불일치', '장문 내용 일치', '윗글에 관한 내용으로 적절하지 <u>않은</u> 것은?', T43,
 ['사서는 아이들을 위한 책장을 주문했다.', 'Tom은 책장 양쪽 측면에 꽃을 그렸다.', 'Tom은 다음 날 아침에 작업을 끝냈다.', 'Martin은 책장을 노란색으로 칠했다.', '사서가 떠난 후 Martin은 Tom에게 사과했다.'], 2,
 'His work was finished late that night → Tom의 작업은 “그날 밤늦게” 끝났어요. 다음 날 아침은 사서가 완성된 책장을 본 때예요.',
 ['① a librarian ordered a bookcase for children → 일치', '② painted flowers on both sides of the bookcase → 일치', '④ Martin painted the bookcase yellow → 일치', '⑤ After the librarian left, Martin apologized to Tom → 일치'],
 '장문 일치는 시간 표현(that night / the next morning)이 섞인 선택지를 특히 조심하세요.',
 [], V43, [], paras=P43)
multi('43~45번 장문 (순서·지칭·일치)', 3)
