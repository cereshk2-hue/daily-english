import sys, re, html
sys.path.insert(0, '/tmp/claude-0/-home-claude/a9e3e882-1f02-5d62-8f70-aced81bc59d2/scratchpad')
from gencommon import write
# 고3 수능실전반 (10/30) · 2026학년도 10월 고3 전국연합학력평가 · 하루 한 문제
# DAY = ① 실전 1문제(원문항 그대로, 선택지 순서 고정) ② 단어 리스트(공부 → 뜻 고르기) ③ 단어 테스트(뜻 보고 철자 쓰기)
# 본문 탭 = 문장별 해석 + 핵심 문장(노트 정리용). 해설: 정답 이유 · 오답별 이유 · 유형 전략 · 핵심 문장

def esc(s): return html.escape(s, quote=False)
def mask(word): return ' '.join(p[0] + '□' * (len(p) - 1) for p in word.split(' '))
CIR = '①②③④⑤'

DAYS = []
def day(no, did, typ, story, stem, T, opts, a, why, wrong, point, keys, vocab, spell, box=None, notes='', blank=None, given=None, paras=None, summary=None, u=None, three=False):
    """T: [(영어, 해석)] 지문 문장 / opts: 선택지(원래 순서) / a: 정답 번호(0~4)
       keys: [(영어, 해석, 구문 포인트)] 핵심 문장 2~3 / vocab: [(단어, 뜻)] / spell: 철자 테스트 단어(vocab 중)"""
    # 실전 문항 화면
    if paras is not None: body = ''.join('<p>%s</p>' % p for p in paras)
    else:
        txt = ' '.join(esc(e) for e, k in T)
        if blank: txt = txt.replace(esc(blank), '<span class="blank" style="min-width:7em">&nbsp;</span>')
        if u: txt = txt.replace(esc(u), '<u>%s</u>' % esc(u), 1)
        body = '<p>%s</p>' % txt
    if summary: body += '<p style="margin-top:10px;padding:8px 10px;border:1px dashed var(--line);border-radius:8px">%s</p>' % summary
    if notes: body += '<p style="font-size:13px;color:var(--muted);margin-top:6px">%s</p>' % notes
    q = '<b>%d. %s%s</b>%s<span class="exam-box en">%s</span>' % (no, stem, ' [3점]' if three else '', ('<span class="exam-given en">%s</span>' % esc(given)) if given else '', body)
    ex = '정답 ▶ %s %s\n이유: %s\n오답 ▶ %s\n포인트 ▶ %s\n핵심 문장 ▶\n%s' % (
        CIR[a], re.sub(r'<[^>]+>', '', opts[a]), why, '\n'.join(wrong), point,
        '\n'.join('%d) %s\n   → %s\n   ✎ %s' % (i + 1, e, k, p) for i, (e, k, p) in enumerate(keys)))
    passage = [['#', '%d번 · %s' % (no, typ), '']]
    if given: passage += [['', given, dict(T).get(given, '')]] if False else []
    passage += [['', e, k] for e, k in T]
    passage += [['#', '핵심 문장 (노트 정리)', '']] + [['', e, '%s  ✎ %s' % (k, p)] for e, k, p in keys]
    for w in spell: assert w in dict(vocab), (no, w)
    VM = dict(vocab)
    DAYS.append({'id': did, 'name': 'DAY', 'range': '%d번 %s' % (no, typ), 'story': story, 'passage': passage, 'steps': [
        {'type': 'mc', 'title': '실전 1문제', 'guide': '시험처럼 시간을 재고 풀어 보세요. 풀고 나면 해설과 핵심 문장을 노트에 정리해요.',
         'items': [{'n': no, 'q': q, 'opts': opts, 'a': a, 'keep': True, 'ex': ex}]},
        {'type': 'vocab', 'title': '단어 리스트', 'guide': '단어와 뜻을 소리 내어 읽고, 퀴즈에서 뜻을 골라요.', 'quizN': min(15, len(vocab)), 'items': [[w, m, no] for w, m in vocab]},
        {'type': 'verb', 'title': '단어 테스트', 'guide': '우리말 뜻을 보고, 첫 글자와 네모칸 수에 맞게 영어로 쓰세요.', 'free': True, 'ph': '영어로 쓰기',
         'items': [{'s': '%s → ___' % VM[w], 'v': mask(w), 'mask': mask(w), 'a': [w], 'ex': '정답 ▶ %s (%s)' % (w, VM[w])} for w in spell]},
    ]})

# ═══ DAY 1 · 20번 주장 ═══
day(20, 'q20', '주장', '필자의 주장 · 명령문이 모이는 곳을 찾기', '다음 글에서 필자가 주장하는 바로 가장 적절한 것은?', [
 ("Did you know that shadows are the color of the sky?", "그림자가 하늘색이라는 것을 알고 있었는가?"),
 ("That counterintuitive reality reminds us that preconceived notions, bias, and prejudice color our view of the world.", "그 반직관적인 사실은 선입견, 편향, 편견이 세상을 보는 우리의 시각을 물들인다는 것을 상기시켜 준다."),
 ("One profound habit of thinking individuals is to first acknowledge their biases and then intentionally overcome them.", "생각하는 사람들의 한 가지 심오한 습관은 먼저 자신의 편향을 인정하고 그런 다음 의도적으로 그것을 극복하는 것이다."),
 ("Asking challenging questions can help.", "도전적인 질문을 던지는 것이 도움이 될 수 있다."),
 ("Passionately argue an issue from the opposite point of view, and ask probing and difficult questions that challenge your original stance.", "반대 관점에서 쟁점을 열정적으로 논증해 보고, 원래 자신의 입장에 이의를 제기하는, 속을 캐는 어려운 질문을 던져라."),
 ("Be brutally honest and see what's actually there rather than what's expected.", "냉정할 만큼 솔직해져서, 예상되는 것이 아니라 실제로 거기에 있는 것을 보라."),
 ("Get in the habit of asking, “Do I really know?” and refuse to accept assertions blindly.", "“내가 정말 알고 있는가?”라고 묻는 습관을 들이고, 주장을 맹목적으로 받아들이기를 거부하라."),
 ("Challenge everything and everyone — including your teachers.", "모든 것과 모든 사람에게 이의를 제기하라. 여러분의 선생님까지 포함해서."),
 ("Don't be intimidated.", "겁먹지 마라."),
 ("You are the best authority on what you don't understand — trust yourself: don't be afraid to ask the questions you need to ask, and be brave enough to change your thinking when you uncover a blind spot.", "여러분이 이해하지 못하는 것에 관해서는 여러분 자신이 최고의 권위자이다. 자신을 믿어라. 해야 할 질문을 하는 것을 두려워하지 말고, 맹점을 발견했을 때는 생각을 바꿀 만큼 용감해져라."),
], ['논쟁을 할 때 상대방의 입장에서 생각하는 습관을 들여야 한다.', '자신의 기존 생각에 안주하지 말고 끊임없이 질문해야 한다.', '지식의 오류를 줄이기 위해 권위자의 의견을 존중해야 한다.', '타인의 비판에 위축되지 말고 자신의 직관을 믿어야 한다.', '편향을 극복하기 위해서는 객관적인 통계 자료를 확인해야 한다.'], 1,
 '처음 두 문장(그림자는 하늘색이다)은 “선입견이 우리 시각을 물들인다”는 것을 보여 주는 도입이에요. 필자의 주장은 셋째·넷째 문장부터 나와요: 편향을 인정하고 의도적으로 극복하라 → 도전적인 질문이 도움이 된다. 그 뒤의 명령문들(반대 관점에서 논증하라, “내가 정말 아는가?”라고 물어라, 모든 것에 이의를 제기하라, 맹점을 발견하면 생각을 바꿔라)이 모두 “기존 생각을 의심하고 계속 질문하라”로 모여요.',
 ['① 반대 관점에서 논증하라는 말은 질문하는 ‘방법 하나’일 뿐이에요. 상대방 입장에서 생각하는 습관 자체가 주장은 아니에요. (부분 정보 함정)',
  '③ 오히려 선생님까지 포함해서 모든 사람에게 이의를 제기하라고 했어요. 권위자 존중은 반대 내용이에요.',
  '④ Don\'t be intimidated, trust yourself가 나와서 헷갈리지만, 자신의 ‘직관’을 믿으라는 게 아니라 모르는 것을 질문하라는 뜻이에요. 타인의 비판도 나오지 않아요.',
  '⑤ 통계 자료는 전혀 언급되지 않아요.'],
 '주장 문제는 명령문·should가 몰려 있는 곳이 답이에요. 여러 명령문을 하나로 묶는 말(질문하라, 편향을 극복하라)을 고르세요. 도입의 신기한 사실(그림자 색)은 미끼예요.',
 [("One profound habit of thinking individuals is to first acknowledge their biases and then intentionally overcome them.", "생각하는 사람들의 한 가지 심오한 습관은 먼저 자신의 편향을 인정하고 그런 다음 의도적으로 그것을 극복하는 것이다.", "주어 One profound habit ~ / 동사 is / 보어 to first A and then B (to부정사 보어 · first A and then B 순서)"),
  ("Get in the habit of asking, “Do I really know?” and refuse to accept assertions blindly.", "“내가 정말 알고 있는가?”라고 묻는 습관을 들이고, 주장을 맹목적으로 받아들이기를 거부하라.", "get in the habit of -ing ~하는 습관을 들이다 · refuse to ~하기를 거부하다"),
  ("Be brave enough to change your thinking when you uncover a blind spot.", "맹점을 발견했을 때는 생각을 바꿀 만큼 용감해져라.", "형용사 + enough to ~할 만큼 충분히 …한 · uncover a blind spot 맹점을 발견하다")],
 [('counterintuitive', '반직관적인'), ('preconceived notion', '선입견'), ('bias', '편향'), ('prejudice', '편견'), ('color', '(판단 등을) 물들이다, 영향을 주다'), ('profound', '심오한, 깊은'),
  ('acknowledge', '인정하다'), ('intentionally', '의도적으로'), ('overcome', '극복하다'), ('passionately', '열정적으로'), ('probing', '속을 캐는, 면밀한'), ('stance', '입장'),
  ('brutally honest', '냉정할 만큼 솔직한'), ('assertion', '주장'), ('blindly', '맹목적으로'), ('intimidate', '겁을 주다'), ('authority', '권위자'), ('uncover', '발견하다, 밝혀내다'), ('blind spot', '맹점')],
 ['counterintuitive', 'prejudice', 'profound', 'acknowledge', 'intentionally', 'overcome', 'stance', 'assertion', 'blindly', 'intimidate', 'authority', 'uncover'],
 notes='* counterintuitive: 반(反)직관적인 ** probing: 속을 캐 보는 *** stance: 입장')

# ═══ DAY 2 · 22번 요지 ═══
day(22, 'q22', '요지', '글의 요지 · Yet 뒤의 반전을 잡기', '다음 글의 요지로 가장 적절한 것은?', [
 ("In some ways, we are more eager to track down and recover knowledge from the distant past than ever.", "어떤 면에서 우리는 그 어느 때보다도 먼 과거의 지식을 찾아내고 되살리기를 열망한다."),
 ("New storage technologies make it possible to preserve texts, images, and music at minimal cost, and social media have made it simpler to share this stored content more widely than ever before.", "새로운 저장 기술은 텍스트, 이미지, 음악을 최소한의 비용으로 보존하는 것을 가능하게 하고, 소셜 미디어는 이렇게 저장된 콘텐츠를 그 어느 때보다 더 널리 공유하는 것을 더 간단하게 만들었다."),
 ("Never have previously produced cultural artifacts and practices been as readily available to as many people as they are now.", "이전에 만들어진 문화 유물과 관습이 지금처럼 그렇게 많은 사람들에게 그렇게 쉽게 이용 가능했던 적은 결코 없었다."),
 ("Yet, amid this digital abundance of cultural content, older file formats, websites, and entire databases are becoming unreadable at a frightening speed, raising the question of whether we're really so much better at preserving the past than our ancestors were.", "하지만 이러한 문화 콘텐츠의 디지털 풍요 속에서, 오래된 파일 형식, 웹사이트, 그리고 데이터베이스 전체가 무서운 속도로 읽을 수 없게 되고 있어서, 우리가 정말로 조상들보다 과거를 보존하는 데 훨씬 더 뛰어난지에 대한 의문을 제기한다."),
 ("And while the technologies of cultural storage and distribution have changed, the laws governing how culture works — how it is preserved, transmitted, exchanged, and recovered — haven't.", "그리고 문화를 저장하고 유통하는 기술은 바뀌었지만, 문화가 작동하는 방식, 즉 문화가 어떻게 보존되고, 전달되고, 교환되고, 되살려지는지를 지배하는 법칙은 바뀌지 않았다."),
 ("The interplay of preservation and destruction, of loss and recovery, of error and adaptation continues unabated in a world that has put almost all human cultures in constant contact.", "보존과 파괴, 상실과 회복, 오류와 적응의 상호 작용은 거의 모든 인간 문화를 끊임없이 접촉하게 만든 세상에서도 약해지지 않고 계속된다."),
], ['디지털 콘텐츠의 공유는 문화 정체성을 약화시킨다.', '디지털 기술을 통해 콘텐츠 저장 비용을 절감할 수 있다.', '디지털 기술이 발전해도 문화 보존과 소실의 문제는 남아 있다.', '소셜 미디어는 콘텐츠를 재생산하여 문화 전파를 촉진한다.', '문화 콘텐츠 보존을 위해 원작자의 권리 강화가 필요하다.'], 2,
 '앞의 세 문장은 “지금은 과거의 문화를 그 어느 때보다 쉽게 저장·공유한다”는 일반적인 생각이에요. Yet(하지만)에서 반전: 오래된 파일·웹사이트·데이터베이스가 무서운 속도로 읽을 수 없게 되고 있다 → 우리가 정말 과거를 더 잘 보존하는가? 이어서 기술은 바뀌었지만 문화가 보존·소실되는 법칙은 바뀌지 않았고, 보존과 파괴, 상실과 회복의 상호 작용은 계속된다고 정리해요. → 기술이 발전해도 보존과 소실의 문제는 그대로 남아 있다.',
 ['① 문화 정체성이 약해진다는 내용은 없어요.',
  '② 저장 비용이 줄었다는 건 Yet 앞의 도입 내용이에요. 글이 말하려는 핵심이 아니에요. (부분 정보 함정)',
  '④ 소셜 미디어로 공유가 쉬워졌다는 말은 있지만, 콘텐츠를 재생산해 전파를 촉진한다는 게 요지는 아니에요.',
  '⑤ 원작자의 권리는 나오지 않아요.'],
 '요지 문제는 Yet / But / However 뒤가 핵심인 경우가 많아요. 앞부분(일반적인 생각)과 반대되는 필자의 생각을 찾고, 마지막 문장으로 확인하세요.',
 [("Never have previously produced cultural artifacts and practices been as readily available to as many people as they are now.", "이전에 만들어진 문화 유물과 관습이 지금처럼 그렇게 많은 사람들에게 그렇게 쉽게 이용 가능했던 적은 결코 없었다.", "부정어 Never가 문장 앞 → 도치 Never have + 주어 + p.p. · as ~ as … 비교"),
  ("Yet, amid this digital abundance of cultural content, older file formats, websites, and entire databases are becoming unreadable at a frightening speed, raising the question of whether we're really so much better at preserving the past than our ancestors were.", "하지만 이러한 문화 콘텐츠의 디지털 풍요 속에서, 오래된 파일 형식, 웹사이트, 데이터베이스 전체가 무서운 속도로 읽을 수 없게 되고 있어서, 우리가 정말 조상들보다 과거를 훨씬 더 잘 보존하는지 의문을 제기한다.", "amid ~의 한가운데에 · 분사구문 raising the question of whether ~인지에 대한 의문을 제기하며"),
  ("While the technologies of cultural storage and distribution have changed, the laws governing how culture works haven't.", "문화를 저장하고 유통하는 기술은 바뀌었지만, 문화가 작동하는 방식을 지배하는 법칙은 바뀌지 않았다.", "while ~이지만(대조) · the laws governing ~ (현재분사구가 laws 수식) · haven't (changed) 생략")],
 [('track down', '추적하다, 찾아내다'), ('recover', '되찾다, 복구하다'), ('storage', '저장'), ('preserve', '보존하다'), ('minimal', '최소한의'), ('artifact', '유물, 인공물'),
  ('practice', '관습, 관행'), ('readily', '쉽게'), ('amid', '~의 한가운데에'), ('abundance', '풍요, 풍부'), ('unreadable', '읽을 수 없는'), ('ancestor', '조상'),
  ('distribution', '유통, 분배'), ('govern', '지배하다, 좌우하다'), ('transmit', '전달하다'), ('interplay', '상호 작용'), ('destruction', '파괴'), ('adaptation', '적응'), ('unabated', '약해지지 않는'), ('constant', '끊임없는')],
 ['track down', 'preserve', 'minimal', 'artifact', 'readily', 'abundance', 'ancestor', 'govern', 'transmit', 'interplay', 'adaptation', 'unabated'],
 notes='* cultural artifact: 문화 유물 ** unabated: 약해지지 않는')

# ═══ DAY 3 · 23번 주제 ═══
day(23, 'q23', '주제', '글의 주제 · But 뒤의 핵심 + 마지막 예시로 확인', '다음 글의 주제로 가장 적절한 것은?', [
 ("We use space, eye contact, and touch to communicate positive and negative attitudes toward others.", "우리는 공간, 눈 맞춤, 접촉을 사용하여 다른 사람에 대한 긍정적, 부정적 태도를 전달한다."),
 ("These signals can reflect and regulate the intimacy in a relationship.", "이러한 신호는 관계의 친밀감을 반영하고 조절할 수 있다."),
 ("In one interesting application of this idea, researchers found that nonverbal intimacy regulation even occurs when people interact with others via avatars in online environments.", "이 생각을 흥미롭게 적용한 한 사례에서, 연구자들은 비언어적 친밀감 조절이 사람들이 온라인 환경에서 아바타를 통해 다른 사람과 상호 작용할 때조차 일어난다는 것을 발견했다."),
 ("As in face-to-face encounters, people typically respond to decreased distances by compensating with reduced gaze.", "대면 만남에서처럼, 사람들은 보통 줄어든 거리에 대해 시선을 줄이는 것으로 보완하여 반응한다."),
 ("But we should keep in mind what communication scholar Mark Knapp has pointed out: These stereotypical immediacy behaviors — close distances, eye contact, touch, body lean, and so forth — are more evident during the early stages of intimacy than they are during later stages.", "그러나 우리는 커뮤니케이션 학자 Mark Knapp이 지적한 것을 명심해야 한다. 즉, 가까운 거리, 눈 맞춤, 접촉, 몸 기울이기 등과 같은 이러한 전형적인 친밀 행동은 친밀감의 후기 단계보다 초기 단계에서 더 뚜렷하다."),
 ("When people become comfortable with each other, they may become more selective in their use of nonverbal immediacy signals, using them during a personal crisis, after a fight, on special occasions, at particular social gatherings, and the like.", "사람들이 서로 편안해지면, 비언어적 친밀 신호를 더 선별적으로 사용하게 되어, 개인적인 위기 때, 싸운 후에, 특별한 날에, 특정한 사교 모임에서 등에 그것을 사용할 수 있다."),
 ("They may also adopt other more idiosyncratic ways of showing their affection — a unique gesture or a special touch, for instance — and they may feel less obliged overall to display their affections in public.", "그들은 또한 애정을 표현하는 다른 더 특이한 방식, 예를 들어 독특한 몸짓이나 특별한 접촉을 택할 수도 있고, 전반적으로 사람들 앞에서 애정을 드러내야 한다는 의무감을 덜 느낄 수도 있다."),
], ['the role of positive attitudes in overcoming conflicts', 'the influence of maintaining eye contact in communication', 'the use of nonverbals to signal the current status of relationships', 'the effects of physical distance on interpersonal relationships', 'the benefits of online interaction over in-person conversation'], 2,
 '첫 두 문장이 주제문이에요: 공간·눈 맞춤·접촉 같은 비언어 신호가 관계의 친밀감을 ‘반영하고 조절한다’. 온라인 아바타 연구는 이것이 온라인에서도 일어난다는 예시예요. But 뒤에서 Knapp은 이런 행동이 관계의 초기에 더 뚜렷하고, 편안해지면 선별적으로 쓰거나 특이한 방식으로 바뀐다고 해요. → 관계가 지금 어떤 단계(상태)인지가 비언어 신호의 사용에 드러난다. 즉 “관계의 현재 상태를 알리기 위한 비언어 신호의 사용”이 주제예요.',
 ['① 갈등 극복에서 긍정적 태도의 역할 → after a fight는 신호를 쓰는 ‘때’의 예시일 뿐, 갈등 극복이 주제가 아니에요.',
  '② 의사소통에서 눈 맞춤 유지의 영향 → 눈 맞춤은 여러 신호 중 하나예요. (너무 좁음)',
  '④ 신체적 거리가 대인 관계에 미치는 영향 → 거리도 신호 중 하나이고, 방향도 반대예요. 글은 관계가 신호 사용에 드러난다는 내용이에요.',
  '⑤ 대면 대화보다 온라인 상호 작용이 가진 이점 → 온라인에서도 같은 현상이 일어난다는 것뿐, 이점 비교는 없어요.'],
 '주제 문제는 ① 첫 부분의 일반 진술 ② But 뒤의 수정 ③ 마지막 예시를 모두 아우르는 선택지를 골라요. 예시 하나(눈 맞춤, 거리, 온라인)만 다루는 선택지는 ‘너무 좁은’ 오답이에요.',
 [("These signals can reflect and regulate the intimacy in a relationship.", "이러한 신호는 관계의 친밀감을 반영하고 조절할 수 있다.", "주제문 · reflect(반영하다) and regulate(조절하다) 두 동사가 intimacy를 공통 목적어로"),
  ("These stereotypical immediacy behaviors are more evident during the early stages of intimacy than they are during later stages.", "이러한 전형적인 친밀 행동은 친밀감의 후기 단계보다 초기 단계에서 더 뚜렷하다.", "비교급 more evident ~ than they are … (they = behaviors, are 뒤 evident 생략)"),
  ("When people become comfortable with each other, they may become more selective in their use of nonverbal immediacy signals.", "사람들이 서로 편안해지면, 비언어적 친밀 신호를 더 선별적으로 사용하게 될 수 있다.", "become + 형용사(comfortable, selective) · be selective in ~에 있어 선별적이다")],
 [('regulate', '조절하다'), ('intimacy', '친밀감'), ('application', '적용'), ('nonverbal', '비언어적인'), ('via', '~을 통해'), ('encounter', '만남'),
  ('compensate', '보완하다, 보상하다'), ('gaze', '시선, 응시'), ('keep in mind', '명심하다'), ('point out', '지적하다'), ('stereotypical', '전형적인, 정형화된'), ('immediacy', '친밀감, 직접적인 가까움'),
  ('evident', '분명한, 뚜렷한'), ('selective', '선별적인'), ('occasion', '때, 행사'), ('idiosyncratic', '특이한, 개인 특유의'), ('affection', '애정'), ('obliged', '~해야 한다고 느끼는'), ('in public', '사람들 앞에서')],
 ['regulate', 'intimacy', 'nonverbal', 'encounter', 'compensate', 'gaze', 'stereotypical', 'evident', 'selective', 'idiosyncratic', 'affection', 'obliged'],
 notes='* idiosyncratic: 특이한')

# ═══ DAY 4 · 24번 제목 ═══
day(24, 'q24', '제목', '글의 제목 · 첫 문장과 마지막 문장을 비유로 바꾼 것 찾기', '다음 글의 제목으로 가장 적절한 것은?', [
 ("In many situations, corporate moral decisions do not entail a trade-off: doing the right thing is sometimes good for business.", "많은 상황에서 기업의 도덕적 결정은 상충 관계(하나를 얻으면 하나를 잃는 것)를 수반하지 않는다. 즉, 옳은 일을 하는 것이 때로는 사업에 이롭다."),
 ("Legal scholar Lucian Bebchuk calls this type of reasoning “instrumental stakeholderism.”", "법학자 Lucian Bebchuk는 이런 유형의 추론을 ‘도구적 이해관계자주의’라고 부른다."),
 ("Making stakeholders (customers, the community, employees, and so on) happy, even if it costs a little, may be in the interest of shareholders.", "이해관계자(고객, 지역 사회, 직원 등)를 만족시키는 것은 비용이 조금 들더라도 주주에게 이익이 될 수 있다."),
 ("For Bebchuk, such situations do not pose a challenge to economist Milton Friedman's view that managers should aim at maximizing profits.", "Bebchuk에게 이런 상황은 경영자가 이윤 극대화를 목표로 해야 한다는 경제학자 Milton Friedman의 견해에 문제를 제기하지 않는다."),
 ("Giving an extra week of paid vacation or long maternity leave may help attract the most talented young college graduates.", "1주일의 추가 유급 휴가나 긴 출산 휴가를 주는 것은 가장 재능 있는 젊은 대학 졸업생들을 끌어들이는 데 도움이 될 수 있다."),
 ("Sourcing inputs responsibly may appeal to millennial consumers who are concerned with the environment.", "원자재를 책임감 있게 조달하는 것은 환경에 관심이 있는 밀레니얼 세대 소비자들의 마음을 끌 수 있다."),
 ("Being more environmentally conscious than what current standards require might give a leading edge if one anticipates that regulations will become tighter in the near term.", "규제가 가까운 시일 내에 더 엄격해질 것으로 예상된다면, 현재 기준이 요구하는 것보다 더 환경을 의식하는 것이 앞서 나가는 우위를 줄 수도 있다."),
 ("Morality can be seen in such cases as an instrument for (current and long-term) profits, not necessarily as a goal for its own sake.", "그런 경우에 도덕성은 반드시 그 자체를 위한 목표로서가 아니라, (현재와 장기적인) 이윤을 위한 도구로 여겨질 수 있다."),
], ['Regulating Business for Sustainability and Its Limitations', 'When Goodness Pays Off: The Strategic Side of Ethics', 'Why Does Profit Maximization Still Come First?', 'Handling Conflicts: Personal Values vs. Work Ethics', 'How Trends Are Reshaping Young Consumers’ Behaviors'], 1,
 '첫 문장: 옳은 일을 하는 것이 사업에도 이롭다(상충 관계가 아니다). 가운데 예시들: 긴 휴가 → 인재 유치, 책임 있는 원자재 조달 → 환경을 생각하는 소비자, 기준보다 친환경 → 규제 강화에 앞서 우위. 마지막 문장: 도덕성은 이윤을 위한 ‘도구’로 볼 수 있다. → “선함이 이익이 될 때: 윤리의 전략적 측면”. pay off(성과를 내다) = good for business, strategic side(전략적 측면) = instrument for profits.',
 ['① 지속 가능성을 위한 기업 규제와 그 한계 → 규제 강화는 예시 하나이고, 규제의 한계는 없어요.',
  '③ 왜 이윤 극대화가 여전히 우선인가? → Friedman의 이윤 극대화 견해와 충돌하지 않는다는 말은 있지만, 글의 초점은 ‘도덕적 행동이 이익이 된다’는 것이에요. (매력적인 오답)',
  '④ 갈등 다루기: 개인적 가치 대 직업 윤리 → 개인과 직장의 가치 갈등은 나오지 않아요.',
  '⑤ 트렌드가 젊은 소비자의 행동을 어떻게 바꾸는가 → 밀레니얼 소비자는 예시 하나예요.'],
 '제목 문제는 주제를 비유·의문문·콜론(:)으로 바꿔 표현한 것을 찾아요. 첫 문장과 마지막 문장의 핵심어(good for business, instrument for profits)를 다른 말로 바꾼 선택지가 정답이에요.',
 [("In many situations, corporate moral decisions do not entail a trade-off: doing the right thing is sometimes good for business.", "많은 상황에서 기업의 도덕적 결정은 상충 관계를 수반하지 않는다. 즉, 옳은 일을 하는 것이 때로는 사업에 이롭다.", "콜론(:) 뒤 = 앞 내용을 풀어 쓴 말 · 동명사 주어 doing the right thing + is"),
  ("Making stakeholders happy, even if it costs a little, may be in the interest of shareholders.", "이해관계자를 만족시키는 것은 비용이 조금 들더라도 주주에게 이익이 될 수 있다.", "동명사 주어 Making + O + 형용사(make + 목적어 + happy) · be in the interest of ~에게 이익이 되다"),
  ("Morality can be seen in such cases as an instrument for profits, not necessarily as a goal for its own sake.", "그런 경우에 도덕성은 반드시 그 자체를 위한 목표로서가 아니라 이윤을 위한 도구로 여겨질 수 있다.", "see A as B의 수동태 A can be seen as B · not necessarily 반드시 ~인 것은 아닌 · for its own sake 그 자체를 위해")],
 [('corporate', '기업의'), ('entail', '수반하다'), ('trade-off', '상충 관계, 맞바꿈'), ('reasoning', '추론'), ('instrumental', '도구적인, 도움이 되는'), ('stakeholder', '이해관계자'),
  ('shareholder', '주주'), ('in the interest of', '~에게 이익이 되는'), ('pose a challenge to', '~에 문제를 제기하다'), ('maximize', '극대화하다'), ('maternity leave', '출산 휴가'), ('source', '(원자재를) 조달하다'),
  ('appeal to', '~의 마음을 끌다'), ('conscious', '의식하는'), ('leading edge', '앞서 나가는 우위, 선두'), ('anticipate', '예상하다'), ('regulation', '규제'), ('for its own sake', '그 자체를 위해'), ('pay off', '성과를 내다, 이익이 되다')],
 ['corporate', 'entail', 'trade-off', 'stakeholder', 'shareholder', 'maximize', 'appeal to', 'conscious', 'anticipate', 'regulation', 'pay off', 'reasoning'],
 notes='* stakeholder: 이해관계자 ** maternity leave: 출산 휴가')

# ═══ DAY 5 · 36번 순서 ═══
G36 = "In social cognition, the perceiver is interested in attributes such as intelligence, trustworthiness, love, aggressiveness, or humour."
A36 = ["We can observe whether the person is hitting someone, and we may use this observation to infer aggressiveness.",
       "Because these kinds of attributes cannot be directly observed, their assessment requires far more constructive processing than the assessment of size or colour.",
       "To make social judgments, individuals must go beyond the information given far more than when judging inanimate objects."]
B36 = ["One may argue that even basic perceptions such as colour and size require a considerable degree of inference.",
       "However, in most cases, it is the social judgments that require far more inferential processes, and it is precisely this large proportion of constructive processes that makes social cognition a specific and unique process."]
C36 = ["Individuals have no sensory receptors for these attributes, which refer to distal entities that have to be inferred from more proximal cues, and sometimes have no objective existence at all.",
       "For example, we cannot directly observe the “aggressiveness” of a particular person."]
day(36, 'q36', '순서', '글의 순서 · 지시어(these, the person)와 연결어(However)로 잇기', '주어진 글 다음에 이어질 글의 순서로 가장 적절한 것은?', [
 (G36, "사회적 인지에서 지각하는 사람은 지능, 신뢰성, 사랑, 공격성, 유머와 같은 속성에 관심이 있다."),
 (C36[0], "(C) 개인은 이러한 속성에 대한 감각 수용기가 없는데, 이 속성은 더 가까운 단서로부터 추론되어야 하는 먼 실재물을 가리키며, 때로는 객관적으로 전혀 존재하지 않기도 한다."),
 (C36[1], "예를 들어, 우리는 특정한 사람의 ‘공격성’을 직접 관찰할 수 없다."),
 (A36[0], "(A) 우리는 그 사람이 누군가를 때리고 있는지를 관찰할 수 있고, 이 관찰을 이용해 공격성을 추론할 수 있다."),
 (A36[1], "이런 종류의 속성은 직접 관찰될 수 없기 때문에, 그것을 평가하는 데는 크기나 색을 평가하는 것보다 훨씬 더 많은 구성적 처리가 필요하다."),
 (A36[2], "사회적 판단을 하기 위해서, 개인은 무생물을 판단할 때보다 주어진 정보를 훨씬 더 많이 넘어서야 한다."),
 (B36[0], "(B) 색과 크기 같은 기본적인 지각조차 상당한 정도의 추론을 필요로 한다고 주장하는 사람도 있을 것이다."),
 (B36[1], "그러나 대부분의 경우 훨씬 더 많은 추론 과정을 필요로 하는 것은 바로 사회적 판단이며, 사회적 인지를 특정하고 독특한 과정으로 만드는 것은 바로 이 많은 비율의 구성적 처리이다."),
], ['(A) - (C) - (B)', '(B) - (A) - (C)', '(B) - (C) - (A)', '(C) - (A) - (B)', '(C) - (B) - (A)'], 3,
 '① 주어진 글 → (C): 주어진 글의 속성들(지능, 공격성 …)을 (C)가 these attributes로 받아요. “이 속성에는 감각 수용기가 없다, 예를 들어 공격성은 직접 관찰할 수 없다.” ② (C) → (A): (C) 끝의 “특정한 사람의 공격성”을 (A)가 the person으로 받아요. “그 사람이 때리는지는 관찰할 수 있으니 이를 이용해 공격성을 추론한다 → 크기나 색을 평가할 때보다 훨씬 더 많은 구성적 처리가 필요하다.” ③ (A) → (B): (A) 끝의 “size or colour”를 (B)가 colour and size로 이어받아 “색과 크기 같은 기본 지각도 추론이 필요하다고 할 수 있지만(양보), However 사회적 판단이 훨씬 더 많은 추론을 필요로 한다”로 결론을 내요.',
 ['① (A)가 먼저 오면 the person(그 사람)이 누구인지 알 수 없어요.',
  '②③ (B)의 colour and size는 (A)에서 처음 비교 대상으로 나와야 자연스러워요. 주어진 글 바로 뒤에 “기본 지각도 추론이 필요하다”는 반론이 올 이유가 없어요.',
  '⑤ (C) 뒤에 (B)가 오면 (A)의 “공격성 추론” 설명이 결론 뒤로 밀려 흐름이 끊겨요.'],
 '순서 문제는 ① 지시어(these, the person, this) ② 관사(a → the) ③ 연결어(For example, However)를 표시하고, ‘앞 단락의 마지막 말’을 ‘다음 단락의 첫 말’이 받는지 확인하세요.',
 [(C36[0], "개인은 이러한 속성에 대한 감각 수용기가 없는데, 이 속성은 더 가까운 단서로부터 추론되어야 하는 먼 실재물을 가리키며, 때로는 객관적으로 전혀 존재하지 않기도 한다.", "계속적 용법 , which(= these attributes) refer to ~ and sometimes have … · have to be inferred 추론되어야 한다(수동)"),
  (A36[1], "이런 종류의 속성은 직접 관찰될 수 없기 때문에, 그것을 평가하는 데는 크기나 색을 평가하는 것보다 훨씬 더 많은 구성적 처리가 필요하다.", "far more ~ than … 훨씬 더 많은 (far = 비교급 강조) · their assessment = 그 속성들을 평가하는 것"),
  ("It is precisely this large proportion of constructive processes that makes social cognition a specific and unique process.", "사회적 인지를 특정하고 독특한 과정으로 만드는 것은 바로 이 많은 비율의 구성적 처리이다.", "It is ~ that 강조 구문 · make + O + 명사(a specific and unique process)")],
 [('social cognition', '사회적 인지'), ('perceiver', '지각하는 사람'), ('attribute', '속성'), ('trustworthiness', '신뢰성'), ('aggressiveness', '공격성'), ('sensory receptor', '감각 수용기'),
  ('refer to', '~을 가리키다'), ('distal', '먼 쪽의'), ('entity', '실재물'), ('infer', '추론하다'), ('proximal', '가까운 쪽의'), ('cue', '단서'), ('objective', '객관적인'),
  ('assessment', '평가'), ('constructive', '구성적인'), ('inanimate', '무생물의'), ('considerable', '상당한'), ('inference', '추론'), ('inferential', '추론의'), ('proportion', '비율')],
 ['attribute', 'trustworthiness', 'aggressiveness', 'infer', 'cue', 'objective', 'assessment', 'constructive', 'inanimate', 'considerable', 'inference', 'proportion'],
 given=G36, paras=['<b>(A)</b> ' + esc(' '.join(A36)), '<b>(B)</b> ' + esc(' '.join(B36)), '<b>(C)</b> ' + esc(' '.join(C36))],
 notes='* distal: 먼 쪽의 ** entity: 실재물(物) *** proximal: 가까운 쪽의', three=True)

# ═══ DAY 6 · 21번 함축 의미 ═══
day(21, 'q21', '함축 의미', '밑줄 함축 의미 · 비유(사진 현상)가 뜻하는 것 풀기', '밑줄 친 “develops the photograph” of the original text가 다음 글에서 의미하는 바로 가장 적절한 것은?', [
 ("All the philosophical dilemmas about whether translation “reflects” or instead “transforms” what's in the original need to be swept aside.", "번역이 원문에 있는 것을 ‘반영하는지’ 아니면 ‘변형하는지’에 관한 모든 철학적 딜레마는 치워 버릴 필요가 있다."),
 ("This is exactly the dichotomy that Merleau-Ponty's account of perception is trying to free us from: are we “seeing” objects or “constituting” them?", "이것이 바로 Merleau-Ponty의 지각 이론이 우리를 벗어나게 하려는 이분법이다. 즉, 우리는 대상을 ‘보는’ 것인가, 아니면 대상을 ‘구성하는’ 것인가?"),
 ("Neither, because we perceive things in a world we live in and have the power to transform: a chair is something we can go sit in; a mug is something we can pick up.", "둘 다 아니다. 왜냐하면 우리는 우리가 살고 있고 변화시킬 힘을 가진 세계 속에서 사물을 지각하기 때문이다. 의자는 우리가 가서 앉을 수 있는 것이고, 머그잔은 우리가 집어 들 수 있는 것이다."),
 ("One of Merleau-Ponty's many great metaphors is that perception neither finds the world nor creates it: it reveals it, which he expresses using the term révélateur, the developing fluid for photographs in a darkroom.", "Merleau-Ponty의 많은 훌륭한 은유 중 하나는 지각이 세계를 찾아내는 것도 창조하는 것도 아니고 드러낸다는 것인데, 그는 이것을 암실에서 사진을 현상하는 액체인 révélateur(현상액)라는 용어로 표현한다."),
 ("The act of seeing develops what's in the world, like developing a photograph.", "보는 행위는 사진을 현상하는 것처럼 세계에 있는 것을 현상한다(드러낸다)."),
 ("Likewise, a translation “develops the photograph” of the original text.", "마찬가지로, 번역은 원문의 ‘사진을 현상한다’."),
 ("Translators don't simply “recognize” what's there, but nor are we “changing” it into anything it isn't already, though we can be more or less aggressively interventionist in our darkroom.", "번역가는 거기에 있는 것을 단순히 ‘알아보는’ 것이 아니지만, 그렇다고 그것을 원래 그것이 아닌 어떤 것으로 ‘바꾸는’ 것도 아니다. 비록 우리가 우리의 암실에서 다소 적극적으로 개입할 수는 있지만 말이다."),
 ("As a translator I take up the affordances of the original, moving through its world and constantly invited to respond in certain ways.", "번역가로서 나는 원문의 행위유발성을 받아들여, 원문의 세계 속을 움직이며 끊임없이 특정한 방식으로 반응하도록 이끌린다."),
], ['brings into view what already exists without inventing anything new', 'invents ideologically driven values that are not grounded in the original', 'provides detailed background information of the original text to enhance reader comprehension', 'introduces a completely new interpretation that appeals to the target readers', 'exploits a work of art in order to convey the translator’s perspectives'], 0,
 '비유를 풀어요. 현상액(révélateur)은 필름에 이미 찍혀 있는 상을 ‘보이게’ 만들 뿐, 새로운 그림을 그려 넣지 않아요. 지각도 세계를 찾지도(find) 창조하지도(create) 않고 드러낸다(reveal). 마찬가지로 번역도 원문을 그냥 알아보는(recognize) 것이 아니지만, 원래 아닌 것으로 바꾸는(change) 것도 아니에요. → 원문에 이미 있는 것을 새로 지어내지 않고 드러내 보이게 한다 = ① brings into view what already exists without inventing anything new.',
 ['② 원문에 근거하지 않은, 이념에 이끌린 가치를 지어낸다 → “원래 아닌 것으로 바꾸지 않는다”와 정반대예요.',
  '③ 독자 이해를 위해 원문의 자세한 배경 정보를 제공한다 → 배경 정보 제공은 나오지 않아요.',
  '④ 목표 독자에게 호소하는 완전히 새로운 해석을 도입한다 → ‘완전히 새로운’ 것은 create/change에 해당해서 부정된 내용이에요.',
  '⑤ 번역가의 관점을 전달하려고 예술 작품을 이용한다 → 번역가의 관점 전달이 아니라 원문의 세계에 반응하는 것이에요.'],
 '함축 의미 문제는 밑줄이 비유일 때 ① 비유의 원래 뜻(현상 = 이미 있는 상을 보이게 함) ② 글에서 부정하는 두 극단(reflect/recognize vs transform/change)을 정리하고, ‘그 사이’를 말하는 선택지를 고르세요. 한쪽 극단만 말하는 선택지는 오답이에요.',
 [("One of Merleau-Ponty's many great metaphors is that perception neither finds the world nor creates it: it reveals it.", "Merleau-Ponty의 많은 훌륭한 은유 중 하나는 지각이 세계를 찾아내는 것도 창조하는 것도 아니고, 그것을 드러낸다는 것이다.", "One of + 복수명사 + is(단수 동사) · neither A nor B A도 B도 아닌"),
  ("Likewise, a translation “develops the photograph” of the original text.", "마찬가지로, 번역은 원문의 ‘사진을 현상한다’.", "Likewise 마찬가지로 → 앞의 지각 비유를 번역에 적용 (밑줄 문장)"),
  ("Translators don't simply “recognize” what's there, but nor are we “changing” it into anything it isn't already.", "번역가는 거기에 있는 것을 단순히 ‘알아보는’ 것이 아니지만, 그렇다고 그것을 원래 그것이 아닌 어떤 것으로 ‘바꾸는’ 것도 아니다.", "nor + be동사 + 주어 (부정 도치: ~도 아니다) · change A into B A를 B로 바꾸다")],
 [('philosophical', '철학적인'), ('dilemma', '딜레마, 진퇴양난'), ('reflect', '반영하다'), ('transform', '변형하다'), ('sweep aside', '치워 버리다, 일축하다'), ('dichotomy', '이분법'),
  ('account', '설명, 이론'), ('perception', '지각'), ('constitute', '구성하다'), ('metaphor', '은유'), ('reveal', '드러내다'), ('developing fluid', '현상액'),
  ('darkroom', '암실'), ('develop', '(사진을) 현상하다'), ('recognize', '알아보다'), ('interventionist', '개입주의적인'), ('affordance', '행위유발성'), ('take up', '받아들이다'),
  ('ideologically', '이념적으로'), ('exploit', '이용하다')],
 ['philosophical', 'reflect', 'transform', 'dichotomy', 'perception', 'constitute', 'metaphor', 'reveal', 'darkroom', 'recognize', 'exploit', 'account'],
 u='“develops the photograph”', notes='* dichotomy: 이분법 ** affordance: 행위유발성', three=True)

# ═══ DAY 7 · 31번 빈칸 ═══
day(31, 'q31', '빈칸', '빈칸 추론 · 빈칸 앞뒤에서 같은 말을 반복하는 표현 찾기', '다음 빈칸에 들어갈 말로 가장 적절한 것은?', [
 ("Almost all generalizations that political philosophers have made about the nature of human beings are wrong.", "정치 철학자들이 인간의 본성에 관해 내린 거의 모든 일반화는 틀렸다."),
 ("If there is anything we know about human nature in all of its history, art, literature, and the sciences, it is that traits vary.", "우리가 인간 본성에 대해 그 모든 역사, 예술, 문학, 과학을 통해 알고 있는 것이 있다면, 그것은 특성이 다양하다는 것이다."),
 ("Graph the distribution of human beings from the number who exhibit extreme self-interest to those who exhibit extreme self-sacrifice, and you will have variation.", "극단적인 이기심을 보이는 사람의 수부터 극단적인 자기희생을 보이는 사람의 수까지 인간의 분포를 그래프로 그려 보면, 다양성(변이)을 얻게 될 것이다."),
 ("Do the same with intelligence, rationality, brutishness, aggressiveness, or whatever feature you want, and you will find a range, with the exceptional numbering in the very few, and most of us somewhere in the middle.", "지능, 합리성, 야만성, 공격성, 또는 원하는 어떤 특성으로든 똑같이 해 보면, 하나의 범위를 발견하게 될 것인데, 예외적인 사람들은 극소수이고 우리 대부분은 중간 어딘가에 있다."),
 ("We are no more selfish than we are selfless, nor more brutish than we are refined.", "우리는 이타적인 정도보다 더 이기적이지 않으며, 세련된 정도보다 더 야만적이지도 않다. (즉, 어느 한쪽으로 치우쳐 있지 않다.)"),
 ("We are no more disposed to live in a large-scale society than we are inclined to live in familial tribes.", "우리는 가족 단위의 부족 속에서 살고 싶어 하는 정도보다 더 대규모 사회에서 살고 싶어 하는 것도 아니다."),
 ("We are mostly, in almost all respects that explain our behaviors and dispositions, in the middle of a spectrum.", "우리는 대부분, 우리의 행동과 성향을 설명하는 거의 모든 측면에서, 스펙트럼의 중간에 있다."),
 ("Very few behavioral or psychological traits are categorically universal to humankind, at least if the sciences are to be believed.", "적어도 과학을 믿는다면, 인류에게 단언컨대 보편적인 행동적·심리적 특성은 극히 드물다."),
], ['bias', 'progress', 'uniformity', 'variation', 'distortion'], 3,
 '빈칸 앞: “우리가 아는 것이 있다면 그것은 특성이 다양하다(traits vary)는 것이다.” 빈칸 문장: 극단적 이기심부터 극단적 자기희생까지 분포를 그리면 ______를 얻는다. 빈칸 뒤: 다른 특성으로 해 봐도 ‘범위(a range)’가 나오고, 대부분 중간에 있으며, 우리는 스펙트럼의 중간에 있다. → 앞뒤에서 반복되는 말 vary, a range, spectrum = variation(다양성, 변이).',
 ['① bias(편향) → 사람들이 한쪽으로 치우쳐 있다는 게 아니라 고르게 퍼져 있다는 내용이에요.',
  '② progress(진보) → 시간에 따른 발전 이야기가 아니에요.',
  '③ uniformity(획일성) → traits vary와 정반대예요. 가장 매력적인 오답이니 주의!',
  '⑤ distortion(왜곡) → 철학자들의 일반화가 틀렸다는 말은 있지만, 분포 그래프에서 얻는 것은 왜곡이 아니에요.'],
 '빈칸 문제는 빈칸 문장만 보지 말고, 앞뒤 문장에서 같은 뜻으로 반복되는 말(vary → range → spectrum)을 찾으세요. 정답은 그 말을 한 단어로 바꾼 것이에요. 반의어 선택지(uniformity)가 늘 함정으로 나와요.',
 [("If there is anything we know about human nature, it is that traits vary.", "우리가 인간 본성에 대해 알고 있는 것이 있다면, 그것은 특성이 다양하다는 것이다.", "If there is anything ~, it is that … ~한 것이 있다면 그것은 …이다 (빈칸의 근거)"),
  ("Do the same with whatever feature you want, and you will find a range, with the exceptional numbering in the very few, and most of us somewhere in the middle.", "원하는 어떤 특성으로든 똑같이 해 보면 하나의 범위를 발견하게 될 것인데, 예외적인 사람들은 극소수이고 우리 대부분은 중간 어딘가에 있다.", "명령문 + and ~하면 …할 것이다 · with + 명사 + 분사(numbering) 부대상황 · number(동사) 수가 ~에 이르다"),
  ("We are no more selfish than we are selfless, nor more brutish than we are refined.", "우리는 이타적인 정도보다 더 이기적이지 않으며, 세련된 정도보다 더 야만적이지도 않다.", "A no more ~ than B: B보다 더 ~하지 않다 (양쪽 비슷함) · nor (are we) more brutish 생략")],
 [('generalization', '일반화'), ('political philosopher', '정치 철학자'), ('trait', '특성'), ('vary', '다양하다, 서로 다르다'), ('distribution', '분포'), ('exhibit', '보이다, 드러내다'),
  ('self-interest', '이기심, 사리사욕'), ('self-sacrifice', '자기희생'), ('rationality', '합리성'), ('brutishness', '야만성'), ('exceptional', '예외적인'), ('refined', '세련된, 교양 있는'),
  ('be disposed to', '~하는 경향이 있다'), ('be inclined to', '~하는 경향이 있다'), ('familial', '가족의'), ('tribe', '부족'), ('disposition', '성향'), ('spectrum', '스펙트럼, 범위'),
  ('categorically', '단언컨대, 절대적으로'), ('universal', '보편적인'), ('uniformity', '획일성, 균일함'), ('variation', '다양성, 변이')],
 ['generalization', 'trait', 'vary', 'distribution', 'exhibit', 'rationality', 'exceptional', 'refined', 'disposition', 'universal', 'uniformity', 'variation'],
 blank='variation', notes='* categorically: 단언컨대')

# ═══ DAY 8 · 37번 순서 ═══
G37 = "The seamless conjoining of all our sensory information into a single, integrated experience is no easy task and to achieve it, the brain relies on a little trickery."
A37 = ["Moreover, everything we experience has already happened by the time we register it.", "To keep up with the real world and to compensate for this slight delay, the brain has to predict movements.", "If it didn't, we'd be hopelessly out of sync."]
B37 = ["The fact that a pistol is used isn't about tradition; it's simply because athletes, like the rest of us, are slightly slower to react to the light than the sound.", "Our sensory synchronisation is only possible because the brain imposes slight lags on different senses to make everything line up."]
C37 = ["For instance, it has to compensate for discrepancies in the time it takes to process the different senses: vision, being so data rich, takes a fraction longer than the other senses.", "That's why even in the twenty-first century we begin sprint finals with a starting pistol, rather than traffic lights."]
day(37, 'q37', '순서', '글의 순서 · For instance(첫 예시) → 같은 소재 이어가기 → Moreover(추가)', '주어진 글 다음에 이어질 글의 순서로 가장 적절한 것은?', [
 (G37, "우리의 모든 감각 정보를 하나의 통합된 경험으로 매끄럽게 결합하는 것은 결코 쉬운 일이 아니며, 그것을 이루기 위해 뇌는 약간의 속임수에 의존한다."),
 (C37[0], "(C) 예를 들어, 뇌는 서로 다른 감각을 처리하는 데 걸리는 시간의 차이를 보정해야 한다. 시각은 데이터가 아주 풍부해서 다른 감각보다 조금 더 오래 걸린다."),
 (C37[1], "그것이 21세기에도 우리가 단거리 경주 결승을 신호등이 아니라 출발 신호용 총으로 시작하는 이유이다."),
 (B37[0], "(B) 총이 사용된다는 사실은 전통 때문이 아니다. 그것은 단지 운동선수들도 나머지 우리처럼 소리보다 빛에 약간 더 늦게 반응하기 때문이다."),
 (B37[1], "우리의 감각 동기화는 뇌가 모든 것을 맞추기 위해 서로 다른 감각에 약간의 지연을 부과하기 때문에 가능할 뿐이다."),
 (A37[0], "(A) 게다가, 우리가 경험하는 모든 것은 우리가 그것을 인식할 무렵에는 이미 일어난 일이다."),
 (A37[1], "실제 세계를 따라잡고 이 약간의 지연을 보정하기 위해 뇌는 움직임을 예측해야 한다."),
 (A37[2], "만약 그렇게 하지 않는다면, 우리는 절망적일 만큼 동기화가 맞지 않을 것이다."),
], ['(A) - (C) - (B)', '(B) - (A) - (C)', '(B) - (C) - (A)', '(C) - (A) - (B)', '(C) - (B) - (A)'], 4,
 '① 주어진 글 → (C): “뇌는 약간의 속임수에 의존한다” → For instance(예를 들어) 첫 번째 속임수: 감각마다 처리 시간이 달라서 보정한다(시각이 더 오래 걸림) → 그래서 단거리 경주를 출발 총으로 시작한다. ② (C) → (B): (C) 끝의 starting pistol을 (B)가 The fact that a pistol is used로 받아서 이유를 설명하고, “뇌가 감각에 지연을 부과해 맞춘다”로 정리해요. ③ (B) → (A): Moreover(게다가) 두 번째 속임수: 모든 경험은 인식할 때 이미 지나간 일이라, 뇌가 움직임을 예측해야 한다.',
 ['① (A)의 Moreover는 앞에 이미 속임수 하나가 나와야 쓸 수 있어요. 주어진 글 바로 뒤에는 올 수 없어요.',
  '②③ (B)의 a pistol(총) 이야기는 (C)에서 starting pistol이 먼저 나와야 이해돼요.',
  '④ (C) 뒤에 (A)가 오면 출발 총의 이유를 설명하는 (B)가 맨 끝으로 밀려 흐름이 끊겨요.'],
 '순서 문제에서 For instance가 있는 단락은 일반 진술(주어진 글) 바로 뒤에 오기 쉽고, Moreover/Also가 있는 단락은 ‘두 번째’ 내용이라 뒤쪽에 와요. 같은 소재(pistol)를 이어받는 단락끼리 붙이세요.',
 [(G37, "우리의 모든 감각 정보를 하나의 통합된 경험으로 매끄럽게 결합하는 것은 결코 쉬운 일이 아니며, 그것을 이루기 위해 뇌는 약간의 속임수에 의존한다.", "주어 The seamless conjoining of ~ into … (긴 명사구) + is · no easy task 결코 쉽지 않은 일 · rely on ~에 의존하다"),
  ("Our sensory synchronisation is only possible because the brain imposes slight lags on different senses to make everything line up.", "우리의 감각 동기화는 뇌가 모든 것을 맞추기 위해 서로 다른 감각에 약간의 지연을 부과하기 때문에 가능할 뿐이다.", "impose A on B B에게 A를 부과하다 · make + O + 동사원형(line up) 사역동사"),
  ("To keep up with the real world and to compensate for this slight delay, the brain has to predict movements.", "실제 세계를 따라잡고 이 약간의 지연을 보정하기 위해 뇌는 움직임을 예측해야 한다.", "to부정사(목적) 두 개가 and로 병렬 · keep up with ~을 따라잡다 · compensate for ~을 보정하다")],
 [('seamless', '매끄러운'), ('conjoin', '결합하다'), ('integrated', '통합된'), ('trickery', '속임수'), ('compensate for', '~을 보정하다, 보완하다'), ('discrepancy', '차이, 불일치'),
  ('data rich', '데이터가 풍부한'), ('a fraction', '아주 조금'), ('sprint', '단거리 경주'), ('starting pistol', '출발 신호용 총'), ('synchronisation', '동기화'), ('impose', '부과하다'),
  ('lag', '지연'), ('line up', '맞추다, 정렬하다'), ('register', '인식하다, 알아차리다'), ('keep up with', '~을 따라잡다'), ('predict', '예측하다'), ('hopelessly', '절망적으로'), ('out of sync', '동기화가 맞지 않는')],
 ['seamless', 'integrated', 'trickery', 'compensate for', 'discrepancy', 'sprint', 'impose', 'lag', 'register', 'keep up with', 'predict', 'conjoin'],
 given=G37, paras=['<b>(A)</b> ' + esc(' '.join(A37)), '<b>(B)</b> ' + esc(' '.join(B37)), '<b>(C)</b> ' + esc(' '.join(C37))],
 notes='* seamless: 매끄러운 ** sync: 동기화 *** discrepancy: 차이')

# ═══ DAY 9 · 38번 삽입 ═══
G38 = "Some may be better adapted to a particular ecological niche, while most are either neutral or do worse."
S38 = ["Homo sapiens as a species is defined by its genome.",
       "Unlike a digital document that can be flawlessly copied, again and again, without a single character missing or out of place, genomes are subject to random mutations and copying errors as the information is passed from parents to offspring.",
       "This comes on top of the genetic lottery as we inherit about half of our dad's genes and half of our mom's, but which of our dad's genes and which of our mom's genes we inherit is random, like a deck of shuffled cards.",
       "We all carry variants of nature's instruction manual for who we can become — differing in roughly one out of every thousand nucleotides.",
       "These “copying errors” are not a bug but a feature, as offspring with diverse genomes are the raw material shaped by the forces of evolution by natural selection.",
       "The former will have a higher chance, and the latter a lower one, of surviving and therefore passing on their genome to the next generation."]
day(38, 'q38', '삽입', '문장 삽입 · 흐름이 끊긴 곳(the former / the latter) 찾기', '글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳은?', [
 (G38, "[주어진 문장] 어떤 것은 특정한 생태적 지위에 더 잘 적응할 수 있지만, 대부분은 중립적이거나 더 나빠진다."),
 (S38[0], "하나의 종으로서 호모 사피엔스는 유전체에 의해 정의된다."),
 (S38[1], "글자 하나 빠지거나 잘못된 위치에 있지 않고 계속해서 완벽하게 복사될 수 있는 디지털 문서와 달리, 유전체는 정보가 부모에게서 자손으로 전달될 때 무작위 돌연변이와 복사 오류를 겪기 쉽다."),
 (S38[2], "이것은 유전적 제비뽑기에 더해지는 것인데, 우리는 아빠 유전자의 약 절반과 엄마 유전자의 약 절반을 물려받지만, 아빠의 유전자 중 어느 것과 엄마의 유전자 중 어느 것을 물려받는지는 섞인 카드 한 벌처럼 무작위이다."),
 (S38[3], "우리는 모두 우리가 어떤 사람이 될 수 있는지에 대한 자연의 사용 설명서의 변이형을 지니고 있는데, 대략 뉴클레오티드 천 개 중 하나꼴로 다르다."),
 (S38[4], "이러한 ‘복사 오류’는 결함이 아니라 특징인데, 다양한 유전체를 가진 자손이 자연 선택에 의한 진화의 힘이 빚어내는 원재료이기 때문이다."),
 (S38[5], "전자는 생존하여 그 결과 자신의 유전체를 다음 세대에 물려줄 가능성이 더 높고, 후자는 더 낮을 것이다."),
], ['①', '②', '③', '④', '⑤'], 4,
 '마지막 문장의 The former(전자)와 the latter(후자)가 가리킬 ‘두 대상’이 바로 앞 문장(복사 오류는 특징이다, 다양한 유전체를 가진 자손은 원재료다)에는 없어요. → 흐름이 끊긴 곳이 ⑤예요. 주어진 문장의 Some(특정 생태적 지위에 더 잘 적응하는 것) = the former → 생존 가능성 더 높음, most(중립적이거나 더 나쁜 것) = the latter → 더 낮음. 주어진 문장의 Some / most는 “다양한 유전체를 가진 자손” 중 일부 / 대부분을 가리켜요.',
 ['① 첫 문장(유전체로 정의된다) 뒤에는 아직 다양한 자손이 나오지 않아서 Some이 가리킬 대상이 없어요.',
  '② 복사 오류 설명 뒤에 바로 “어떤 것은 더 잘 적응한다”가 오면, This comes on top of(이것은 ~에 더해진다)의 This가 가리키는 ‘복사 오류’와의 연결이 끊겨요.',
  '③④ 유전적 제비뽑기, 변이형 이야기 중간이라 ‘자연 선택에서 어떤 것은 유리, 대부분은 불리’라는 결과가 나오기엔 일러요.'],
 '삽입 문제는 주어진 문장의 단서(Some / most)와, 글에서 ‘갑자기 흐름이 끊기는 곳’(the former / the latter, this, they 등이 가리킬 대상이 없는 곳)을 찾으세요. 두 단서가 만나는 자리가 정답이에요.',
 [(S38[1], "글자 하나 빠지거나 잘못된 위치에 있지 않고 계속해서 완벽하게 복사될 수 있는 디지털 문서와 달리, 유전체는 정보가 부모에게서 자손으로 전달될 때 무작위 돌연변이와 복사 오류를 겪기 쉽다.", "Unlike ~와 달리 · without + 명사 + 형용사/분사(missing) · be subject to ~을 겪기 쉽다"),
  (S38[4], "이러한 ‘복사 오류’는 결함이 아니라 특징인데, 다양한 유전체를 가진 자손이 자연 선택에 의한 진화의 힘이 빚어내는 원재료이기 때문이다.", "not A but B A가 아니라 B · as ~이기 때문에 · the raw material shaped by … (과거분사구 수식)"),
  (G38 + " " + S38[5], "어떤 것은 특정한 생태적 지위에 더 잘 적응할 수 있지만 대부분은 중립적이거나 더 나빠진다. 전자는 생존하여 유전체를 다음 세대에 물려줄 가능성이 더 높고, 후자는 더 낮을 것이다.", "while ~인 반면 · the former(전자) = Some, the latter(후자) = most · the latter (will have) a lower one (생략, one = chance)")],
 [('species', '종'), ('genome', '유전체'), ('flawlessly', '완벽하게'), ('be subject to', '~을 겪기 쉽다'), ('mutation', '돌연변이'), ('offspring', '자손'),
  ('on top of', '~에 더하여'), ('genetic lottery', '유전적 제비뽑기'), ('inherit', '물려받다'), ('variant', '변이형'), ('instruction manual', '사용 설명서'), ('nucleotide', '뉴클레오티드'),
  ('bug', '결함, 오류'), ('feature', '특징'), ('raw material', '원재료'), ('natural selection', '자연 선택'), ('adapt', '적응하다'), ('ecological niche', '생태적 지위'), ('neutral', '중립적인'), ('the former', '전자')],
 ['species', 'genome', 'flawlessly', 'mutation', 'offspring', 'inherit', 'variant', 'feature', 'raw material', 'natural selection', 'adapt', 'neutral'],
 given=G38, paras=[esc(S38[0]) + ' ( ① ) ' + esc(S38[1]) + ' ( ② ) ' + esc(S38[2]) + ' ( ③ ) ' + esc(S38[3]) + ' ( ④ ) ' + esc(S38[4]) + ' ( ⑤ ) ' + esc(S38[5])],
 notes='* ecological niche: 생태적 지위 ** mutation: 돌연변이 *** nucleotide: 뉴클레오티드(핵산의 구성 성분)', three=True)

# ═══ DAY 10 · 40번 요약문 ═══
day(40, 'q40', '요약문', '요약문 완성 · (A)(B)를 본문의 다른 말로 바꿔 찾기', '다음 글의 내용을 한 문장으로 요약하고자 한다. 빈칸 (A), (B)에 들어갈 말로 가장 적절한 것은?', [
 ("Social norms are so pervasive and so deeply embedded in our performative muscle memory that we typically engage in them without even thinking.", "사회적 규범은 너무나 만연하고 우리의 수행적 근육 기억에 너무나 깊이 박혀 있어서, 우리는 보통 생각조차 하지 않고 그것을 따른다."),
 ("When someone greets us and asks, “How are you?,” we tend to respond automatically with something along the lines of “I'm OK” or “Not bad.”", "누군가 우리에게 인사하며 “잘 지내?”라고 물으면, 우리는 “괜찮아”나 “나쁘지 않아” 같은 말로 자동적으로 대답하는 경향이 있다."),
 ("The response is hardly ever “You know, I'm having a pretty awful day, and I'm really worried because there is talk of layoffs happening at my job,” even though that may be the case.", "비록 그것이 사실일지라도, 대답이 “있잖아, 나 오늘 정말 끔찍한 하루를 보내고 있고, 직장에서 정리 해고가 있을 거라는 말이 있어서 정말 걱정돼.”인 경우는 거의 없다."),
 ("This degree of transparency upon greeting someone is typically perceived as socially awkward.", "누군가와 인사할 때 이 정도로 솔직한 것은 보통 사회적으로 어색하게 여겨진다."),
 ("The list of social norms within a given community or society is ever growing and ever changing as community members negotiate what is acceptable behavior based on the standing beliefs and ideologies of the collective.", "특정 공동체나 사회 안의 사회적 규범 목록은, 공동체 구성원들이 그 집단의 기존 신념과 이념에 근거해 무엇이 용인되는 행동인지를 협의함에 따라 계속 늘어나고 계속 변한다."),
 ("During this process, new rules are constructed and enforced to establish expectations for community members.", "이 과정에서 공동체 구성원들에 대한 기대를 확립하기 위해 새로운 규칙이 만들어지고 시행된다."),
 ("Social norms could easily be reduced to practicing “good behavior,” but it's much more than that.", "사회적 규범은 ‘좋은 행동’을 실천하는 것으로 쉽게 축소될 수 있지만, 그것은 그보다 훨씬 더 큰 의미를 지닌다."),
 ("Social norms are the means by which social cohesion is achieved.", "사회적 규범은 사회적 결속이 이루어지는 수단이다."),
 ("And we navigate these rules, and thousands more like them, every single day.", "그리고 우리는 매일 이 규칙들과 그와 같은 수천 가지 규칙을 헤쳐 나간다."),
], ['unconsciously ······· strengthens', 'unconsciously ······· disrupts', 'habitually ······· challenges', 'reluctantly ······· assesses', 'reluctantly ······· reinforces'], 0,
 '(A) 첫 문장: 생각조차 하지 않고(without even thinking) 규범을 따른다, 인사에 자동적으로(automatically) 대답한다 → unconsciously(무의식적으로). (B) 협의된 규칙(these negotiated rules)이 결국 사회적 유대에 하는 일: 사회적 규범은 사회적 결속(cohesion)이 이루어지는 수단이다 → strengthens(강화한다). 요약문: 사회적 규범은 일상적 상호 작용에서 흔히 무의식적으로 실천되지만, 이 협의된 규칙들은 궁극적으로 사회적 유대를 강화하는 메커니즘으로 작용한다.',
 ['② unconsciously – disrupts(방해한다) → 결속을 이루는 수단이므로 반대예요.',
  '③ habitually(습관적으로)는 (A)에 어느 정도 어울리지만, challenges(도전한다)는 결속과 맞지 않아요.',
  '④ reluctantly(마지못해) → 싫은데 억지로 하는 게 아니라 생각 없이 자동으로 하는 것이에요. assesses(평가한다)도 근거가 없어요.',
  '⑤ reinforces(강화한다)는 (B)에 맞지만, reluctantly가 틀려요. (A)와 (B)를 둘 다 확인해야 해요!'],
 '요약문 문제는 요약문을 먼저 읽고 (A)(B)가 각각 본문의 어느 부분을 바꾼 말인지 찾아요. 본문 표현(without even thinking, cohesion)을 다른 단어(unconsciously, strengthens)로 바꾼 것이 정답이에요. 한쪽만 맞는 선택지(③⑤)를 조심하세요.',
 [("Social norms are so pervasive and so deeply embedded in our performative muscle memory that we typically engage in them without even thinking.", "사회적 규범은 너무나 만연하고 우리의 수행적 근육 기억에 너무나 깊이 박혀 있어서, 우리는 보통 생각조차 하지 않고 그것을 따른다.", "so ~ that … 너무 ~해서 …하다 · be embedded in ~에 박혀 있다 · engage in ~을 하다 → (A)의 근거"),
  ("The list of social norms is ever growing and ever changing as community members negotiate what is acceptable behavior.", "사회적 규범 목록은 공동체 구성원들이 무엇이 용인되는 행동인지를 협의함에 따라 계속 늘어나고 계속 변한다.", "ever + -ing 끊임없이 ~하는 · as ~함에 따라 · negotiate + what 명사절"),
  ("Social norms are the means by which social cohesion is achieved.", "사회적 규범은 사회적 결속이 이루어지는 수단이다.", "전치사 + 관계대명사 by which (= by the means) · cohesion 결속 → (B)의 근거")],
 [('social norm', '사회적 규범'), ('pervasive', '만연한'), ('embedded', '박혀 있는, 내재된'), ('performative', '수행적인'), ('muscle memory', '근육 기억'), ('engage in', '~에 참여하다, ~을 하다'),
  ('along the lines of', '~와 비슷한'), ('layoff', '정리 해고'), ('be the case', '사실이다'), ('transparency', '투명함, 솔직함'), ('awkward', '어색한'), ('negotiate', '협의하다, 협상하다'),
  ('acceptable', '용인되는'), ('standing', '기존의, 오래된'), ('collective', '집단'), ('enforce', '시행하다'), ('be reduced to', '~으로 축소되다'), ('cohesion', '결속, 결합'),
  ('navigate', '헤쳐 나가다'), ('unconsciously', '무의식적으로'), ('reluctantly', '마지못해'), ('disrupt', '방해하다, 붕괴시키다')],
 ['social norm', 'pervasive', 'embedded', 'layoff', 'transparency', 'awkward', 'negotiate', 'acceptable', 'enforce', 'cohesion', 'unconsciously', 'reluctantly'],
 summary='While social norms are often practiced <b>(A)</b> ________ in daily interactions, these negotiated rules act as a mechanism that ultimately <b>(B)</b> ________ social ties.',
 notes='* pervasive: 만연한 ** transparency: 투명함 *** cohesion: 결합', three=True)

for i, d in enumerate(DAYS): d['name'] = 'DAY %d' % (i + 1)
PK = {'id': 'h3-suneung-2510', 'school': '고3 수능실전반', 'unit': '하루 한 문제 · 2026학년도 10월 학평', 'title': 'Daily Suneung Practice',
      'titleKo': '고3 수능실전반 · 하루 한 문제', 'exam': '수능', 'prose': True, 'pick': True, 'passLock': True, 'teacherPhone': '', 'days': DAYS}
write(PK, '/home/claude/proj/data/h3-suneung-2510.js', "/* 고3 수능실전반 (10/30, scratchpad/gen_h3sn.py) · 2026학년도 10월 고3 전국연합학력평가\n   DAY = 실전 1문제(선택지 순서 고정 keep/a) → 단어 리스트 → 단어 테스트. 본문 탭 = 문장별 해석 + 핵심 문장 */\n")
print('ok', [(d['id'], d['range'], len(d['steps'][1]['items'])) for d in DAYS])
