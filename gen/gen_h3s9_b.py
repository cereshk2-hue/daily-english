# 9월 모평 DAY 34~41 : 25 도표 → 36 순서 → 28 안내문 → 29 어법 → 31 빈칸 → 35 무관 → 40 요약 → 30 어휘  (gen_h3s9.py 안에서 exec)

# ═══ 25번 도표 ═══
T25 = [
 ("The above graph shows the percentages of U.K. respondents by age who self-reported their dietary choices as Meat-eater, Flexitarian, or Vegetarian, based on data released in 2026.", "위 도표는 2026년에 발표된 자료를 바탕으로, 자신의 식단 선택을 육식주의자, 플렉시테리언, 채식주의자라고 스스로 밝힌 영국 응답자들의 연령별 비율을 보여 준다."),
 ("The most common dietary choice among the respondents was Meat-eater in all age groups shown.", "① 응답자들 사이에서 가장 흔한 식단 선택은 제시된 모든 연령 그룹에서 육식주의자였다."),
 ("With respect to the category of Vegetarian, Group A, the youngest age group, showed the highest percentage among the four age groups.", "② 채식주의자 항목과 관련해서는, 가장 어린 연령 그룹인 A그룹이 네 연령 그룹 중 가장 높은 비율을 보였다."),
 ("In Group B, the percentage of Meat-eater was lower than 70 percent.", "③ [틀린 문장] B그룹에서는 육식주의자의 비율이 70%보다 낮았다. → 실제는 73%로 70%보다 높아요."),
 ("When it comes to the percentage of Flexitarian in each age group, the highest was in Group C.", "④ 각 연령 그룹의 플렉시테리언 비율에 있어서 가장 높은 것은 C그룹이었다."),
 ("For Group D, the oldest age group, less than five percent of the respondents reported Vegetarian as their dietary choice.", "⑤ 가장 나이가 많은 연령 그룹인 D그룹에서는 5% 미만의 응답자가 식단 선택을 채식주의자라고 응답했다."),
]
ROWS25 = [('A (18-24)', 68, 12, 8), ('B (25-49)', 73, 12, 6), ('C (50-64)', 73, 16, 4), ('D (65+)', 77, 13, 3)]
CH25 = ('<b>Self-reported Dietary Choices by Age in the U.K. (2026)</b> (%)'
        '<table style="border-collapse:collapse;width:100%;font-size:12px;margin:6px 0;table-layout:fixed">'
        '<tr>' + ''.join('<th %s>%s</th>' % (TD, h) for h in ('Group<br>(Age)', 'Meat-<br>eater', 'Flexi-<br>tarian', 'Vege-<br>tarian')) + '</tr>'
        + ''.join('<tr>' + ''.join('<td %s>%s</td>' % (TD, v) for v in r) + '</tr>' for r in ROWS25) + '</table>'
        '<small>※ 일부 항목은 표시하지 않았고, 비율은 반올림한 값이에요.</small>')
day(25, 'q25', '도표', '도표 · lower than / less than 숫자 직접 대조', '다음 도표의 내용과 일치하지 <u>않는</u> 것은?', T25,
 ['①', '②', '③', '④', '⑤'], 2,
 'B그룹(25-49세)의 육식주의자(Meat-eater) 비율은 73%예요. 70%보다 “낮다(lower than 70 percent)”가 아니라 높아요. 그래서 ③이 불일치.',
 ['① 육식주의자: A 68, B 73, C 73, D 77 → 모든 그룹에서 1위 ✔',
  '② 채식주의자: A 8 > B 6 > C 4 > D 3 → 가장 어린 A가 최고 ✔',
  '④ 플렉시테리언: A 12, B 12, C 16, D 13 → C가 최고 ✔',
  '⑤ D그룹 채식주의자 3% → 5% 미만 ✔'],
 '도표 문제는 문장의 비교 표현(the highest, lower than, less than)에 동그라미 치고, 그 숫자를 표에서 바로 찾아 대조하세요. 그룹 이름(A~D)과 나이를 헷갈리지 않게 표에 표시하면 실수가 줄어요.',
 [(T25[0][0], "위 도표는 2026년에 발표된 자료를 바탕으로, 식단 선택을 육식주의자·플렉시테리언·채식주의자라고 스스로 밝힌 영국 응답자들의 연령별 비율을 보여 준다.", "respondents (by age) who self-reported ~ · report A as B A를 B라고 응답하다 · data released in 2026 (과거분사구가 data를 꾸밈)"),
  (T25[2][0], "채식주의자 항목과 관련해서는, 가장 어린 연령 그룹인 A그룹이 네 연령 그룹 중 가장 높은 비율을 보였다.", "with respect to ~에 관하여 · Group A, the youngest age group, (동격 콤마)"),
  (T25[4][0], "각 연령 그룹의 플렉시테리언 비율에 있어서 가장 높은 것은 C그룹이었다.", "when it comes to + 명사/동명사 ~에 있어서, ~에 관해서라면")],
 [('respondent', '응답자'), ('self-reported', '스스로 보고한'), ('dietary choice', '식단 선택'), ('meat-eater', '육식주의자'), ('flexitarian', '플렉시테리언(가끔 육식하는 채식주의자)'), ('vegetarian', '채식주의자'),
  ('release', '발표하다'), ('common', '흔한'), ('with respect to', '~에 관하여'), ('category', '항목, 범주'), ('when it comes to', '~에 있어서'), ('percentage', '비율')],
 ['respondent', 'vegetarian', 'release', 'common', 'category', 'percentage'],
 paras=[CH25, esc(T25[0][0]) + ' ①' + esc(T25[1][0]) + ' ②' + esc(T25[2][0]) + ' ③' + esc(T25[3][0]) + ' ④' + esc(T25[4][0]) + ' ⑤' + esc(T25[5][0])])

# ═══ 36번 순서 ═══
G36 = "Our choices and actions send messages to others about our values. Consider a manager who communicates to her employees in a call center that “customer care is the most important thing for our company.”"
A36 = ["In many cases, performance is multidimensional, but compensation is only given to one aspect of performance, typically the one that is easiest to measure.",
       "Simple “one-aspect” compensation sends a clear message to the workers: concentrate on what we’re paying you for and ignore everything else."]
B36 = ["That’s a signal to others regarding values.",
       "Now, imagine that the manager sets the incentives such that employees are paid by the number of calls they answer.",
       "This incentive sends a very different signal about what the manager is looking for: it’s about being fast, which comes at the expense of quality of care."]
C36 = ["Such mixed signals leave the employees confused about the manager’s values and expectations.",
       "This mixed signals problem is channeled into a simple question: what should be rewarded?"]
day(36, 'q36', '순서', '글의 순서 · That(앞 문장), Such mixed signals(두 신호)로 잇기', '주어진 글 다음에 이어질 글의 순서로 가장 적절한 것은?', [
 ("Our choices and actions send messages to others about our values.", "우리의 선택과 행동은 다른 사람들에게 우리의 가치관에 관한 메시지를 보낸다."),
 ("Consider a manager who communicates to her employees in a call center that “customer care is the most important thing for our company.”", "콜센터 직원들에게 “고객 응대가 우리 회사에 가장 중요한 일이다.”라고 전달하는 한 관리자를 생각해 보라."),
 (B36[0], "(B) 그것은 가치관에 관해 다른 사람들에게 보내는 하나의 신호이다."),
 (B36[1], "이제 관리자가 직원들이 응답하는 통화 수에 따라 급여를 받도록 유인책을 설정한다고 상상해 보라."),
 (B36[2], "이 유인책은 관리자가 무엇을 원하는지에 관해 매우 다른 신호를 보내는데, 즉 그것은 신속함에 관한 것이며, 이는 고객 응대의 질을 희생하면서 이루어진다."),
 (C36[0], "(C) 그러한 엇갈리는 신호는 직원들을 관리자의 가치관과 기대에 대해 혼란스럽게 만든다."),
 (C36[1], "이 엇갈리는 신호의 문제는 ‘무엇이 보상되어야 하는가?’라는 하나의 간단한 질문으로 귀결된다."),
 (A36[0], "(A) 많은 경우, 성과는 다차원적이지만 보상은 성과의 한 측면, 일반적으로 가장 측정하기 쉬운 측면에만 주어진다."),
 (A36[1], "단순한 ‘단일 측면’ 보상은 직원들에게 명확한 메시지를 보내는데, 즉 우리가 여러분에게 급여를 주는 것에 집중하고 그 밖의 다른 모든 것은 무시하라는 것이다."),
], ['(A) - (C) - (B)', '(B) - (A) - (C)', '(B) - (C) - (A)', '(C) - (A) - (B)', '(C) - (B) - (A)'], 2,
 '① 주어진 글 → (B): 관리자가 “고객 응대가 가장 중요하다”고 말함 → (B)의 That’s a signal(그것은 하나의 신호다)이 그 말을 받아요. 이어서 통화 수로 급여를 주면 “빠르기”라는 전혀 다른 신호를 보낸다. ② (B) → (C): (B)에서 나온 두 개의 다른 신호를 Such mixed signals(그러한 엇갈리는 신호)로 받아요 → 직원은 혼란 → “무엇이 보상되어야 하는가?”라는 질문. ③ (C) → (A): 그 질문에 대한 답으로 “보상은 측정하기 쉬운 한 측면에만 주어지고, 직원은 그것에만 집중한다”로 마무리.',
 ['①② (A)가 먼저 오면 compensation(보상) 이야기가 갑자기 나와요. 아직 급여(incentive) 이야기가 등장하지 않았어요.',
  '④⑤ (C)의 Such mixed signals는 ‘서로 다른 두 신호’가 앞에 나와야 쓸 수 있어요. 주어진 글에는 신호가 하나(말)뿐이에요.'],
 '순서 문제는 각 단락의 첫 단어를 보세요. That, Such + 명사, This + 명사는 바로 앞 단락의 내용을 가리켜요. “Such mixed signals(엇갈리는 신호들)”처럼 복수·대조를 가리키면, 앞에 두 가지가 나와 있어야 해요.',
 [(B36[1], "이제 관리자가 직원들이 응답하는 통화 수에 따라 급여를 받도록 유인책을 설정한다고 상상해 보라.", "set A such that ~ ~하도록 A를 설정하다 · be paid by ~에 따라 급여를 받다 · the number of calls (that) they answer"),
  (C36[0], "그러한 엇갈리는 신호는 직원들을 관리자의 가치관과 기대에 대해 혼란스럽게 만든다.", "leave + O + p.p.(confused) ~을 …한 상태로 만들다 · Such mixed signals = (B)의 두 신호"),
  (A36[0], "많은 경우, 성과는 다차원적이지만 보상은 성과의 한 측면, 일반적으로 가장 측정하기 쉬운 측면에만 주어진다.", "the one (that is) easiest to measure 가장 측정하기 쉬운 것 (one = aspect) · 형용사 + to부정사(easy to measure)")],
 [('value', '가치관'), ('communicate', '전달하다'), ('employee', '직원'), ('customer care', '고객 응대'), ('performance', '성과'), ('multidimensional', '다차원적인'),
  ('compensation', '보상'), ('aspect', '측면'), ('typically', '일반적으로'), ('measure', '측정하다'), ('concentrate on', '~에 집중하다'), ('ignore', '무시하다'),
  ('regarding', '~에 관하여'), ('incentive', '유인책, 장려책'), ('at the expense of', '~을 희생하여'), ('mixed', '엇갈리는'), ('confused', '혼란스러운'), ('expectation', '기대'),
  ('channel', '(어떤 방향으로) 돌리다, 귀결시키다'), ('reward', '보상하다')],
 ['communicate', 'employee', 'performance', 'multidimensional', 'compensation', 'aspect', 'typically', 'measure', 'ignore', 'incentive', 'confused', 'reward'],
 given=G36, paras=['<b>(A)</b> ' + esc(' '.join(A36)), '<b>(B)</b> ' + esc(' '.join(B36)), '<b>(C)</b> ' + esc(' '.join(C36))])

# ═══ 28번 안내문 일치 ═══
T28 = [
 ("Newstar Voice Acting Course", "Newstar 성우 연기 강좌"),
 ("Do you dream of hearing your own voice in an animation or movie?", "애니메이션이나 영화에서 여러분 자신의 목소리를 듣는 것을 꿈꾸시나요?"),
 ("If so, our voice acting course is perfect for you.", "만약 그렇다면, 저희의 성우 연기 강좌가 여러분에게 딱 맞습니다."),
 ("When & Where", "일시 & 장소"),
 ("6 p.m. to 8 p.m. every Thursday", "매주 목요일 오후 6시에서 8시"),
 ("Room #223, Newstar Building", "Newstar 빌딩 223호실"),
 ("Course Content", "강좌 내용"),
 ("Week 1: Ways to Breathe and Vocalize", "1주 차: 호흡하고 발성하는 방법"),
 ("Week 2: Script Analysis", "2주 차: 대본 분석"),
 ("Week 3: Animation Dubbing", "3주 차: 애니메이션 더빙"),
 ("Week 4: Movie Dubbing", "4주 차: 영화 더빙"),
 ("Registration", "등록"),
 ("The registration fee is $170.", "등록비는 170달러입니다."),
 ("You can register only in the first week of every month.", "매달 첫 번째 주에만 등록할 수 있습니다."),
 ("To register, call 789-331-0234 or email us at n#star@v#ac.com.", "등록하려면 789-331-0234로 전화하거나 n#star@v#ac.com으로 이메일을 보내 주세요."),
 ("Special Benefits", "특별 혜택"),
 ("Video-recorded class lectures will be provided for no additional fee.", "녹화된 수업 강의가 추가 비용 없이 제공될 것입니다."),
 ("You will have a chance to meet the famous voice actor Richard Choi, who will share his know-how with you.", "유명한 성우 Richard Choi를 만날 기회가 있을 것인데, 그는 여러분에게 자신의 노하우를 알려 줄 것입니다."),
]
H28 = {"Newstar Voice Acting Course", "When & Where", "Course Content", "Registration", "Special Benefits"}
TB28 = ('<table style="border-collapse:collapse;width:100%;font-size:12px;margin:6px 0">'
        '<tr>' + ''.join('<th %s>%s</th>' % (TD, h) for h in ('Class Schedule', 'Content')) + '</tr>'
        + ''.join('<tr><td %s>%s</td><td %s>%s</td></tr>' % (TD, w, TD, c) for w, c in
                  [('Week 1', 'Ways to Breathe and Vocalize'), ('Week 2', 'Script Analysis'), ('Week 3', 'Animation Dubbing'), ('Week 4', 'Movie Dubbing')]) + '</table>')
day(28, 'q28', '안내문 일치', '안내문 일치 · 요일·주차·무료/유료를 하나씩 지우기', 'Newstar Voice Acting Course에 관한 다음 안내문의 내용과 일치하는 것은?', T28,
 ['매주 주말마다 진행된다.', '1주 차 수업에 스크립트 분석을 한다.', '매월 마지막 주에만 등록할 수 있다.', '추가 비용을 내면 녹화된 수업 강의가 제공될 것이다.', '유명한 성우를 만날 기회가 있을 것이다.'], 4,
 'You will have a chance to meet the famous voice actor Richard Choi → 유명한 성우를 만날 기회가 있다. ⑤가 일치.',
 ['① every Thursday → 주말이 아니라 매주 목요일이에요.',
  '② Week 1은 호흡과 발성(Ways to Breathe and Vocalize), 대본 분석은 Week 2예요.',
  '③ only in the first week of every month → 마지막 주가 아니라 첫 번째 주예요.',
  '④ for no additional fee → 추가 비용 없이(무료로) 제공돼요.'],
 '“일치하는 것” 문제는 틀린 선택지 4개를 근거와 함께 지워 나가세요. 요일(Thursday), 주차(Week 1/2), first/last, no additional fee(무료)가 단골로 바뀌어 나와요.',
 [(T28[1][0], T28[1][1], "dream of -ing ~하는 것을 꿈꾸다 (전치사 of 뒤 동명사)"),
  (T28[16][0], T28[16][1], "will be provided 미래 수동 · for no additional fee 추가 비용 없이"),
  (T28[17][0], T28[17][1], "have a chance to ~할 기회가 있다 · 콤마 + who (계속적 용법: 그리고 그는 ~)")],
 [('voice acting', '성우 연기'), ('course', '강좌'), ('breathe', '호흡하다'), ('vocalize', '발성하다'), ('script', '대본'), ('analysis', '분석'),
  ('dubbing', '더빙'), ('registration fee', '등록비'), ('register', '등록하다'), ('benefit', '혜택'), ('lecture', '강의'), ('provide', '제공하다'),
  ('additional', '추가의'), ('voice actor', '성우'), ('know-how', '노하우')],
 ['course', 'breathe', 'script', 'analysis', 'register', 'benefit', 'lecture', 'provide', 'additional'],
 paras=[lines_html(T28[:7], H28), TB28, lines_html(T28[11:], H28)])

# ═══ 29번 어법 ═══
T29 = [
 ("Leaders come in all shapes and sizes, but successful leaders tend to have one thing in common: the ability to share someone else’s feelings, known as empathy.", "리더는 각양각색이지만, 성공적인 리더는 한 가지를 공통으로 가지는 경향이 있는데, 바로 공감이라고 알려진, 다른 사람의 감정을 공유하는 능력이다."),
 ("While empathy forms in everyone to some degree, effective leaders know how to develop this emotional guidance system to connect with others’ feelings and perspectives.", "공감 능력은 모든 사람에게 어느 정도 형성되어 있지만, 유능한 리더는 타인의 감정과 관점에 연결되기 위해 이 감정 길잡이 시스템을 발전시키는 방법을 알고 있다."),
 ("However, empathy in leaders is more than simply being kind to employees, clients, and customers.", "하지만 리더의 공감 능력은 단순히 직원, 고객, 손님에게 친절하게 대하는 것 이상이다."),
 ("Empathetic people seem more approachable, focusing on the words of others.", "공감 능력이 뛰어난 사람들은 타인의 말에 집중하므로, 더 다가가기 쉬워 보인다."),
 ("Listening to the needs of employees enables leaders to clearly identify what makes them feel heard.", "직원들의 요구를 듣는 것은 리더가 무엇이 직원들로 하여금 자기 말을 들어 준다고 느끼게 하는지를 분명히 파악할 수 있게 한다. (시험지의 enable → enables)"),
 ("Utilized in this way, empathy can be considered a crucial part of maintaining employee satisfaction.", "이런 방식으로 활용될 때, 공감은 직원 만족도를 유지하는 핵심적인 요소로 간주될 수 있다."),
 ("Leaders who are unable to surround themselves with competent employees will not be successful.", "유능한 직원들로 자신을 둘러쌀 수 없는 리더는 성공하지 못할 것이다."),
 ("Indeed, a leader’s failure to empathize with talented workers is one of the main situations that could lead them to leave an organization.", "사실 리더가 재능 있는 직원들에게 공감하지 못하는 것은 그들이 조직을 떠나게 할 수 있는 주요 상황 중 하나이다."),
 ("In this case, the organization must spend precious time and money to find suitable replacements for them.", "이 경우, 조직은 그들을 대체할 적합한 사람을 찾기 위해 귀중한 시간과 비용을 들여야만 한다."),
]
Q29 = para(T29, [(1, 'system to connect', 'system ①<u>to connect</u>'), (2, 'than simply being', 'than ②<u>simply</u> being'),
                 (4, 'employees enables', 'employees ③<u>enable</u>'), (5, 'of maintaining', 'of ④<u>maintaining</u>'), (7, 'situations that could', 'situations ⑤<u>that</u> could')])
day(29, 'q29', '어법', '어법 · 동명사 주어는 단수 동사', '다음 글의 밑줄 친 부분 중, 어법상 틀린 것은?', T29,
 ['① to connect', '② simply', '③ enable', '④ maintaining', '⑤ that'], 2,
 '주어는 동명사구 Listening to the needs of employees예요. 동명사 주어는 단수 취급하므로 동사는 enable이 아니라 enables가 맞아요. 바로 앞의 employees(복수)에 속으면 안 돼요!',
 ['① to connect: 감정 길잡이 시스템을 발전시키는 ‘목적’(~하기 위해)을 나타내는 to부정사 ✔',
  '② simply: 동명사구 being kind를 꾸미는 부사 ✔',
  '④ maintaining: 전치사 of의 목적어 자리 → 동명사 ✔',
  '⑤ that: 선행사 the main situations를 받아 could lead의 주어 역할을 하는 주격 관계대명사 ✔'],
 '동사에 밑줄이 있으면 “진짜 주어”를 찾으세요. 동명사(-ing)·to부정사·명사절 주어는 단수! 주어와 동사 사이에 끼어 있는 복수 명사(employees)는 함정이에요.',
 [(T29[0][0], T29[0][1], "have one thing in common 한 가지 공통점이 있다 · 콜론(:) 뒤 = one thing의 내용 · known as ~로 알려진(과거분사)"),
  (T29[4][0], T29[4][1], "동명사 주어 Listening ~ + 단수 동사 enables · enable + O + to부정사 · what makes them feel heard (make + O + 동사원형 + p.p.)"),
  (T29[5][0], T29[5][1], "Utilized in this way = When it is utilized ~ (수동 분사구문) · be considered + 명사 ~로 간주되다 · of + 동명사(maintaining)")],
 [('in common', '공통적으로'), ('empathy', '공감'), ('to some degree', '어느 정도는'), ('effective', '유능한, 효과적인'), ('guidance', '안내, 길잡이'), ('perspective', '관점'),
  ('client', '고객, 의뢰인'), ('empathetic', '공감하는'), ('approachable', '다가가기 쉬운'), ('identify', '파악하다'), ('utilize', '활용하다'), ('crucial', '핵심적인'),
  ('satisfaction', '만족(도)'), ('competent', '유능한'), ('empathize with', '~에 공감하다'), ('talented', '재능 있는'), ('precious', '귀중한'), ('suitable', '적합한'),
  ('replacement', '대체자, 후임자')],
 ['empathy', 'perspective', 'approachable', 'identify', 'utilize', 'crucial', 'satisfaction', 'competent', 'talented', 'precious', 'suitable', 'replacement'],
 paras=[Q29])

# ═══ 31번 빈칸 ═══
day(31, 'q31', '빈칸', '빈칸 추론 · excluded / alienated / exclusion의 반대말 찾기', '다음 빈칸에 들어갈 말로 가장 적절한 것은?', [
 ("What stresses you out more than anything?", "무엇이 여러분에게 그 어떤 것보다 더 많은 스트레스를 주는가?"),
 ("Perhaps it’s speaking in front of others.", "아마도 그것은 다른 사람들 앞에서 말하는 것일 것이다."),
 ("For many, this is so stressful it even has a name: glossophobia.", "많은 사람에게 이것은 너무 스트레스를 주어서 심지어 ‘말하기 공포증’이라는 이름까지 있다."),
 ("The explanation for why it’s uncomfortable to have everyone’s eyes on you is probably that, for almost all of our evolution, it’s been extremely important not to be excluded from the group.", "모든 사람의 시선이 여러분에게 놓이는 것이 불편한 이유에 대한 설명은 아마도, 우리가 진화해 온 거의 전 기간 동안 집단에서 배제되지 않는 것이 매우 중요했기 때문일 것이다."),
 ("To prepare for what might happen if you are evaluated and socially shamed ― and thus alienated from the group ― your brain fires up the stress system and your heart begins to beat harder.", "여러분이 평가받고 사회적으로 망신을 당해 그로 인해 집단에서 소외되는 경우에 일어날 수도 있는 일에 대비하기 위해, 뇌는 스트레스 체계를 작동시키고 심장은 더 세게 뛰기 시작한다."),
 ("Our natural sensitivity to being evaluated by other people is another example of our brain not being adapted to the modern world.", "다른 사람에게 평가받는 것에 대한 우리의 타고난 민감성은 우리의 뇌가 현대 세계에 적응되어 있지 않은 것의 또 다른 예이다."),
 ("If we give a bad presentation at work, we are unlikely to lose our job and thus risk starving to death.", "직장에서 발표를 망쳐도, 우리가 직장을 잃고 그래서 굶어 죽을 위험에 처할 것 같지는 않다."),
 ("But in the world we long ago evolved for, exclusion from the group could be a matter of life and death.", "하지만 오래전 우리가 (그에 맞게) 진화했던 세계에서 집단으로부터의 배제는 생사의 문제일 수 있었다."),
 ("Belonging was not merely a matter of safety but also of survival.", "소속감은 단순히 안전의 문제만이 아니라 생존의 문제이기도 했다."),
 ("You simply couldn’t make it on your own.", "여러분은 결코 혼자서는 살아남을 수 없었다."),
], ['Belonging', 'Confidence', 'Endurance', 'Learning', 'Competition'], 0,
 '글 전체에서 반복되는 말: not to be excluded from the group(집단에서 배제되지 않기), alienated from the group(집단에서 소외됨), exclusion from the group(집단에서의 배제)이 생사의 문제였다. 빈칸 뒤: 혼자서는 살아남을 수 없었다(couldn’t make it on your own). → 배제의 반대 = 집단에 속하는 것 = Belonging(소속감).',
 ['② Confidence(자신감): 발표 불안 이야기라 끌리지만, 글의 이유는 자신감이 아니라 집단에서 쫓겨나는 두려움이에요. (가장 매력적인 오답)',
  '③ Endurance(인내): 참고 견디는 이야기는 없어요.',
  '④ Learning(학습): 나오지 않아요.',
  '⑤ Competition(경쟁): 오히려 집단 속에 함께 있는 것이 중요해요.'],
 '빈칸이 글의 마지막에 있으면 앞에서 반복된 핵심어의 “같은 말 또는 반대말”이 답이에요. exclusion(배제)이 계속 나왔고 빈칸 뒤가 “혼자서는 못 산다”이니, 정답은 그 반대인 belonging이에요.',
 [("The explanation for why it’s uncomfortable to have everyone’s eyes on you is probably that, for almost all of our evolution, it’s been extremely important not to be excluded from the group.", "모든 사람의 시선이 여러분에게 놓이는 것이 불편한 이유에 대한 설명은 아마도, 진화의 거의 전 기간 동안 집단에서 배제되지 않는 것이 매우 중요했기 때문일 것이다.", "주어 The explanation (for why ~) / 동사 is / 보어 that절 · 가주어 it ~ 진주어 not to be excluded (to부정사 부정은 not to)"),
  ("Our natural sensitivity to being evaluated by other people is another example of our brain not being adapted to the modern world.", "다른 사람에게 평가받는 것에 대한 우리의 타고난 민감성은 우리의 뇌가 현대 세계에 적응되어 있지 않은 것의 또 다른 예이다.", "to being evaluated (전치사 to + 동명사 수동) · our brain not being adapted (동명사의 의미상 주어 our brain + 부정 not)"),
  ("Belonging was not merely a matter of safety but also of survival.", "소속감은 단순히 안전의 문제만이 아니라 생존의 문제이기도 했다.", "not merely A but also B A뿐만 아니라 B도 (= not only A but also B) · of survival = a matter of survival")],
 [('stress out', '스트레스를 주다'), ('glossophobia', '말하기 공포증'), ('explanation', '설명'), ('uncomfortable', '불편한'), ('evolution', '진화'), ('exclude', '배제하다'),
  ('evaluate', '평가하다'), ('shame', '망신시키다'), ('alienate', '소외시키다'), ('fire up', '작동시키다'), ('sensitivity', '민감성'), ('adapt', '적응시키다'),
  ('presentation', '발표'), ('starve', '굶주리다'), ('exclusion', '배제'), ('a matter of life and death', '생사의 문제'), ('belonging', '소속감'), ('survival', '생존'),
  ('make it', '살아남다, 해내다'), ('endurance', '인내')],
 ['explanation', 'uncomfortable', 'evolution', 'exclude', 'evaluate', 'alienate', 'sensitivity', 'adapt', 'starve', 'exclusion', 'belonging', 'survival'],
 blank='Belonging', notes='* starve: 굶주리다')

# ═══ 35번 무관한 문장 ═══
T35 = [
 ("Tourists make intense and short-term use of a very limited number of historical assets and cultural attractions, including material and non-material ones.", "관광객들은 물질적인 것과 비물질적인 것을 포함해 매우 제한된 수의 역사적 자산과 문화 명소를 집중적으로, 그리고 단기간에 이용한다."),
 ("The reason is to be found in the fact that tourist experience in cities is measured in days and hours, even in minutes in the case of cultural attractions or seconds in particular sites.", "① 그 이유는 도시에서의 관광 경험이 며칠과 몇 시간 단위로 측정되며, 문화 명소의 경우에는 심지어 몇 분 단위로, 특정 장소에서는 몇 초 단위로 측정된다는 사실에서 찾을 수 있다."),
 ("In addition, cultural tourists do not often repeat their visit to the same place, and therefore they are continuously looking for new attractions.", "② 게다가 문화 관광객들은 같은 장소를 자주 다시 방문하지 않으므로, 계속해서 새로운 명소를 찾는다."),
 ("As a result of this, a process of selection of cultural assets takes place since only a few buildings and only a small number of social representations are able to be adapted to the tourist visit.", "③ 그 결과, 소수의 건물과 적은 수의 사회적 표상만이 관광객의 방문에 맞게 조정될 수 있기 때문에 문화 자산을 선별하는 과정이 일어난다."),
 ("International festivals bring tourists closer to the community by offering a highly interactive and engaging experience.", "④ [무관한 문장] 국제 축제는 상호작용성이 높고 매력적인 경험을 제공하여 관광객을 지역 공동체에 더 가까워지게 한다."),
 ("The main difference between the selection of cultural assets made for locals and the one made for tourists is that in the second case, only a small choice is made among the largest, most impressive and unique resources.", "⑤ 지역 주민을 위해 이루어지는 문화 자산 선별과 관광객을 위해 이루어지는 선별의 주된 차이는, 후자의 경우 가장 규모가 크고 가장 인상적이며 독특한 자원들 가운데서 적은 수만이 선택된다는 것이다."),
]
day(35, 'q35', '무관한 문장', '무관한 문장 · ‘선별(selection)’ 흐름에서 벗어난 축제 이야기', '다음 글에서 전체 흐름과 관계 없는 문장은?', T35,
 ['①', '②', '③', '④', '⑤'], 3,
 '글의 흐름: 관광객은 아주 적은 수의 명소만 짧게 이용한다 → ① 이유: 관광 시간이 짧다 → ② 게다가 다시 방문하지 않고 새 명소를 찾는다 → ③ 그 결과 문화 자산의 ‘선별’이 일어난다 → ⑤ 관광객용 선별은 가장 크고 인상적인 것 중 소수만 고른다. ④는 “국제 축제가 관광객을 지역 공동체와 가깝게 한다”는 새로운 이야기라 흐름에서 벗어나요.',
 ['① The reason은 첫 문장(제한된 수를 짧게 이용)의 이유 ✔',
  '② In addition으로 두 번째 이유를 덧붙임 ✔',
  '③ As a result of this로 ①②의 결과(선별 과정) ✔',
  '⑤ ③의 selection을 이어받아 지역 주민용 선별과 비교 ✔'],
 '무관한 문장은 연결어(The reason → In addition → As a result → The main difference)로 이어지는 사슬에서 혼자 연결어 없이 새 소재(festivals, community)를 꺼내는 문장이에요. 소재(tourists)는 같아도 주제(선별)가 다르면 답이에요.',
 [(T35[0][0], T35[0][1], "make use of ~을 이용하다 → make intense and short-term use of ~을 집중적이고 단기적으로 이용하다 · ones = assets/attractions"),
  (T35[3][0], T35[3][1], "take place 일어나다 · since ~ 때문에 · be able to be adapted (조동사 표현 + 수동)"),
  (T35[5][0], T35[5][1], "주어 The main difference between A and B / 동사 is / 보어 that절 · the one made for tourists (one = selection)")],
 [('intense', '집중적인'), ('short-term', '단기간의'), ('limited', '제한된'), ('historical', '역사적인'), ('asset', '자산'), ('cultural attraction', '문화 명소'),
  ('material', '물질적인'), ('measure', '측정하다'), ('site', '장소, 현장'), ('repeat', '반복하다'), ('continuously', '계속해서'), ('selection', '선별'),
  ('take place', '일어나다'), ('social representation', '사회적 표상'), ('adapt', '조정하다, 맞추다'), ('interactive', '상호작용하는'), ('engaging', '매력적인'), ('local', '지역 주민'),
  ('impressive', '인상적인'), ('resource', '자원')],
 ['intense', 'limited', 'historical', 'asset', 'material', 'measure', 'continuously', 'selection', 'interactive', 'engaging', 'impressive', 'resource'],
 paras=[esc(T35[0][0]) + ' ① ' + esc(T35[1][0]) + ' ② ' + esc(T35[2][0]) + ' ③ ' + esc(T35[3][0]) + ' ④ ' + esc(T35[4][0]) + ' ⑤ ' + esc(T35[5][0])])

# ═══ 40번 요약문 ═══
T40 = [
 ("Many designers would argue that the most important element of lighting is visibility.", "많은 디자이너들은 조명의 가장 중요한 요소가 가시도라고 주장할 것이다."),
 ("Some even refer to it as the primary function of lighting.", "어떤 이들은 심지어 그것을 조명의 주요 기능이라고 부른다."),
 ("Visibility simply refers to the principle of using light to reveal or illuminate objects.", "가시도란 간단히 말해 물체를 드러내거나 비추기 위해 빛을 사용하는 원리를 가리킨다."),
 ("In the early days, the job of the designer was nothing more than to create enough light so that the audience or occupants of a space could see.", "초창기에 디자이너의 일은 관객이나 공간의 점유자가 볼 수 있도록 충분한 빛을 만들어 내는 것에 불과했다."),
 ("In many ways, this philosophy of lighting was based on the premise that more was better, and many believed that the more footcandles or lumens placed on a stage or in a room, the better visibility that you had.", "여러 면에서 이러한 조명 철학은 많을수록 좋다는 전제에 기반을 두었고, 많은 이들은 무대나 방에 놓인 피트 촉광이나 루멘이 많을수록 가시도가 더 좋아진다고 믿었다."),
 ("Since the 1950s or ’60s, theatrical designing moved toward a concept that we call selective visibility, which simply refers to revealing to an audience only what needs to be seen.", "1950년대나 60년대 이후로 무대 디자인은 우리가 선택적 가시도라고 부르는 개념 쪽으로 이동했는데, 이는 간단히 말해 관객에게 보일 필요가 있는 것만을 드러내는 것을 말한다."),
 ("Hence, a less-revealing image on stage might be more appropriate for the dramatic action than a fully illuminated stage.", "따라서 무대 위에서 덜 드러내는 이미지가 완전히 조명을 받은 무대보다 극적인 연출에 더 적절할 수도 있다."),
 ("In selective visibility, areas of low intensity, shadows, silhouettes, and high contrast can become effective elements in a lighting designer’s set of tools.", "선택적 가시도에서는 (빛의) 강도가 낮은 구역, 그림자, 실루엣, 강한 대비가 조명 디자이너의 도구 모음에서 효과적인 요소가 될 수 있다."),
]
day(40, 'q40', '요약문', '요약문 완성 · 앞(more was better) ↔ 뒤(selective)를 바꿔 말하기', '다음 글의 내용을 한 문장으로 요약하고자 한다. 빈칸 (A), (B)에 들어갈 말로 가장 적절한 것은?', T40,
 ['maximizing ······· strategic', 'increasing ······· uniform', 'controlling ······· minimal', 'reducing ······· targeted', 'limiting ······· purposeful'], 0,
 '(A) 초창기: 많을수록 좋다(more was better), 빛이 많을수록 가시도가 좋다 → 가시도를 “최대화하는(maximizing)” 데 집중. (B) 1950~60년대 이후: 선택적 가시도(selective visibility) = 보여야 할 것만 드러냄, 그림자·대비도 도구로 활용 → 극적 효과를 위한 “전략적인(strategic)” 조명. 그래서 ① maximizing - strategic.',
 ['② increasing(늘리는)은 (A)로 가능하지만, (B) uniform(균일한)은 선택적으로 비추는 것과 반대예요.',
  '③ controlling(통제하는)은 초창기 철학(많을수록 좋다)과 맞지 않아요. minimal(최소의)도 ‘필요한 것만’이지 무조건 최소가 아니에요.',
  '④ reducing(줄이는)은 초창기와 정반대예요. targeted는 (B)로 그럴듯하지만 (A)가 틀려요.',
  '⑤ limiting(제한하는)도 초창기와 정반대예요. purposeful은 (B)로 그럴듯해도 (A)에서 탈락!'],
 '요약문은 (A)·(B) 중 더 확실한 쪽부터 정해서 선택지를 지우세요. 이 문제는 (A)가 “많을수록 좋다”라서 maximizing/increasing만 남고, (B)에서 uniform이 탈락해요. (B)만 보면 targeted, purposeful도 그럴듯하니 꼭 (A)와 함께 확인하세요.',
 [(T40[3][0], T40[3][1], "nothing more than ~에 불과한 · so that + 주어 + could ~할 수 있도록"),
  (T40[4][0], T40[4][1], "the premise that ~ (동격의 that) ~라는 전제 · the 비교급 ~, the 비교급 … ~할수록 더 …하다"),
  (T40[5][0], T40[5][1], "a concept that we call selective visibility · 콤마 + which (계속적 용법) · what needs to be seen 보일 필요가 있는 것")],
 [('element', '요소'), ('lighting', '조명'), ('visibility', '가시도, 보이는 정도'), ('refer to A as B', 'A를 B라고 부르다'), ('primary', '주요한'), ('principle', '원리'),
  ('reveal', '드러내다'), ('illuminate', '비추다'), ('occupant', '점유자, 사용자'), ('philosophy', '철학'), ('premise', '전제'), ('theatrical', '무대의, 연극의'),
  ('selective', '선택적인'), ('appropriate', '적절한'), ('dramatic', '극적인'), ('intensity', '강도'), ('contrast', '대비'), ('maximize', '최대화하다'),
  ('strategic', '전략적인'), ('uniform', '균일한')],
 ['element', 'visibility', 'primary', 'principle', 'reveal', 'illuminate', 'premise', 'selective', 'appropriate', 'intensity', 'contrast', 'strategic'],
 summary='While stage lighting designs in the early days focused on <b>(A)</b> ________ visibility, they later shifted to <b>(B)</b> ________ illumination to enhance dramatic effect.',
 notes='* illuminate: 비추다 ** premise: 전제')

# ═══ 30번 어휘 ═══
T30 = [
 ("There is good news about pests and medicinal herbs: Most herbs either repel pests or attract beneficial insects that help keep pest populations in check.", "해충과 약초에 관한 좋은 소식이 있는데, 대부분의 허브가 해충을 쫓아 버리거나, 해충 개체 수를 억제하는 데 도움을 주는 익충을 유인한다는 것이다."),
 ("So the more herbs you grow, the more you will attract pollinators and “good” bugs that like to eat the more destructive pests, which will lead to a more successful garden!", "따라서 허브를 더 많이 키울수록 여러분은 꽃가루 매개자와 더 파괴적인 해충을 잡아먹기 좋아하는 ‘유익한’ 곤충을 더 많이 유인하게 되며, 이는 더 성공적인 정원으로 이어질 것이다!"),
 ("When it comes to managing pests in the garden, it’s important to remember that you are altering the ecosystem of an area that existed on its own before you planted anything into it.", "정원의 해충을 관리하는 것에 관해 말하자면, 여러분이 거기에 무언가를 심기 전부터 스스로 존재했던 구역의 생태계를 변화시키고 있다는 점을 기억하는 것이 중요하다."),
 ("So the first couple years in a new garden can feel like wave after wave of pests are overtaking your plants.", "그래서 새 정원에서의 처음 몇 년은 해충들이 파도처럼 연이어 밀려와 여러분의 식물을 뒤덮고 있는 듯한 느낌이 들 수 있다."),
 ("This is normal.", "이는 정상적이다."),
 ("The goal of a long-term healthy garden is to work with the environment you are trying to cultivate to allow the plants, pollinators, and even the annoying pests to balance out.", "장기적으로 건강한 정원의 목표는 여러분이 조성하려는 환경과 협력하여 식물, 꽃가루 매개자, 심지어 성가신 해충까지 균형을 이루도록 하는 것이다."),
 ("Immediately attempting to remove a new pest entirely from your garden will only further these initial imbalances and prolong the process of helping your garden grow better on its own.", "새로운 해충을 정원에서 즉시 완전히 제거하려고 시도하는 것은 초기의 불균형을 심화시키고, 정원이 스스로 더 잘 자라도록 돕는 과정을 연장시킬 뿐일 것이다. (시험지의 shorten → prolong)"),
]
Q30 = para(T30, [(1, 'more destructive', 'more ①<u>destructive</u>'), (2, 'are altering', 'are ②<u>altering</u>'), (3, 'are overtaking', 'are ③<u>overtaking</u>'),
                 (5, 'to allow the', 'to ④<u>allow</u> the'), (6, 'and prolong the', 'and ⑤<u>shorten</u> the')])
day(30, 'q30', '어휘', '어휘 · only further imbalances와 같은 방향인지 확인', '다음 글의 밑줄 친 부분 중, 문맥상 낱말의 쓰임이 적절하지 <u>않은</u> 것은?', T30,
 ['① destructive', '② altering', '③ overtaking', '④ allow', '⑤ shorten'], 4,
 '마지막 문장: 새 해충을 당장 완전히 없애려는 시도는 초기 불균형을 “심화시킬(further) 뿐”이다. 나쁜 결과가 이어지므로, 정원이 스스로 균형을 찾아가는 과정을 “단축시키는(shorten)” 게 아니라 “연장시키는(prolong, lengthen)” 거예요. 앞 문장(시간을 두고 균형을 이루는 것이 목표)과도 맞아요.',
 ['① destructive: 유익한 곤충이 잡아먹는 것은 “더 파괴적인” 해충 ✔',
  '② altering: 원래 스스로 존재하던 생태계를 여러분이 “변화시키고” 있다 ✔',
  '③ overtaking: 처음 몇 년은 해충이 식물을 “뒤덮는” 듯한 느낌 → 이는 정상이다 ✔',
  '④ allow: 식물·매개자·해충까지 균형을 이루도록 “허용하는” 것이 목표 ✔'],
 '어휘 문제는 문장 안의 방향을 맞춰 보세요. only further imbalances(불균형만 심화) and ⑤처럼 and로 묶인 말은 같은 방향(둘 다 나쁜 결과)이어야 해요. 좋은 쪽(shorten the process)으로 바뀌어 있으면 틀린 거예요.',
 [(T30[1][0], T30[1][1], "the 비교급 ~, the 비교급 … ~할수록 더 …하다 · 콤마 + which (앞 내용 전체) will lead to ~"),
  (T30[2][0], T30[2][1], "When it comes to -ing ~에 관해서라면 · 가주어 it ~ 진주어 to remember · an area that existed on its own (주격 관계대명사)"),
  (T30[6][0], T30[6][1], "동명사 주어 Attempting ~ + will · further(동사) 심화시키다 · help + O + 동사원형(grow)")],
 [('pest', '해충'), ('medicinal herb', '약초'), ('repel', '쫓아 버리다'), ('beneficial insect', '익충'), ('keep ~ in check', '~을 억제하다'), ('population', '개체 수'),
  ('pollinator', '꽃가루 매개자'), ('destructive', '파괴적인'), ('alter', '변화시키다'), ('ecosystem', '생태계'), ('on its own', '스스로'), ('overtake', '뒤덮다, 장악하다'),
  ('cultivate', '조성하다, 경작하다'), ('annoying', '성가신'), ('balance out', '균형을 이루다'), ('entirely', '완전히'), ('further', '심화시키다'), ('initial', '초기의'),
  ('imbalance', '불균형'), ('prolong', '연장시키다')],
 ['pest', 'repel', 'population', 'pollinator', 'destructive', 'alter', 'ecosystem', 'overtake', 'cultivate', 'annoying', 'imbalance', 'prolong'],
 paras=[Q30], notes='* repel: 쫓아 버리다 ** pollinator: 꽃가루 매개자', three=True)
