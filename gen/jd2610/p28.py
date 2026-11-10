from jfw import *
p = P(28, '28번 · 안내문 일치', [
 ("Illustrate a memorable moment in your school life and share it in the annual Calendar Design Contest!", "학교생활 중 기억에 남는 순간을 그림으로 그려서 매년 열리는 달력 디자인 대회에서 나누어 보세요!"),
 ("Have your work featured in our 2027 school calendar!", "여러분의 작품을 2027년 우리 학교 달력에 실어 보세요!"),
 ("Entries are limited to one per student.", "출품작은 학생 1인당 하나로 제한됩니다."),
 ("Artistic materials such as paint and pastels are accepted.", "물감과 파스텔 같은 미술 재료가 허용됩니다."),
 ("No digitally produced artworks will be allowed.", "디지털로 제작한 작품은 허용되지 않습니다."),
 ("The judging criteria are artistic skill, creativity, and concept.", "심사 기준은 예술적 기술, 창의성, 콘셉트입니다."),
 ("12 winners, one for each month, will be awarded a professional-grade art kit.", "매달 한 명씩, 12명의 수상자에게 전문가용 미술 도구 세트가 수여됩니다."),
 ("Winning artworks will be displayed on the school website.", "수상작은 학교 웹사이트에 게시됩니다."),
 ("Submit your entry to any art teacher by November 20.", "11월 20일까지 미술 선생님 누구에게나 출품작을 제출하세요.")])
NOTICE = ("<b>2027 Youngpine High School Calendar Design Contest</b><br>Illustrate a memorable moment in your school life and share it in the annual Calendar Design Contest! Have your work featured in our 2027 school calendar!"
 "<br><b>Requirements</b><br>• Entries are limited to one per student.<br>• Artistic materials such as paint and pastels are accepted.<br>(No digitally produced artworks will be allowed.)"
 "<br><b>Judging Criteria</b><br>• Artistic Skill, Creativity, Concept<br><b>Prize</b><br>• 12 winners, one for each month, will be awarded a professional-grade art kit.<br>• Winning artworks will be displayed on the school website."
 "<br><b>Submission</b><br>• Submit your entry to any art teacher by November 20.")
VOCAB = words(28, drop=('professional-grade 전문가용의,', 'award A B        '), add=[("professional-grade", "전문가용의, 전문가급의"), ("award A B", "A에게 B를 수여하다")])
VOCAB = [v for v in VOCAB if not v[0].startswith('award A B ')]
EXAM = [EXQ(28, '28. 2027 Youngpine High School Calendar Design Contest에 관한 다음 안내문의 내용과 일치하는 것은?', box(NOTICE), [
 "출품작은 학생 1인당 두 개로 제한된다.", "디지털로 만든 작품이 허용된다.", "심사 기준에 창의성이 포함된다.", "수상작은 교내 복도에 전시된다.", "10월 20일까지 출품작을 제출해야 한다."], 2,
 "정답 ▶ ③ 심사 기준에 창의성이 포함된다.\n이유: Judging Criteria • Artistic Skill, Creativity, Concept\n오답 ▶ ① one per student — 1인당 '하나' ② No digitally produced artworks will be allowed — 디지털 작품 불가 ④ displayed on the school website — 복도가 아니라 '학교 웹사이트' ⑤ by November 20 — 10월이 아니라 '11월' 20일\n포인트 ▶ 안내문 일치는 숫자·날짜·장소·허용 여부를 하나씩 대조", v=False),
 EXQ(28, '다음 안내문의 내용과 일치하지 <u>않는</u> 것은?', box(NOTICE), [
 "학교생활의 기억에 남는 순간을 그리는 대회이다.", "물감과 파스텔 같은 재료를 사용할 수 있다.", "수상자는 모두 12명이다.", "수상자에게는 현금이 상금으로 주어진다.", "출품작은 미술 선생님 누구에게나 제출하면 된다."], 3,
 "정답 ▶ ④ 수상자에게는 현금이 상금으로 주어진다.\n이유: will be awarded a professional-grade art kit — 상품은 '전문가용 미술 도구 세트'\n오답 ▶ ① Illustrate a memorable moment in your school life ② paint and pastels are accepted ③ 12 winners, one for each month ⑤ to any art teacher → 모두 일치"),
 EXQ(28, '다음 안내문을 읽고 답할 수 <u>없는</u> 질문은?', box(NOTICE), [
 "How many entries can each student submit?", "What materials can students use?", "Who will judge the entries?", "Where will the winning artworks be displayed?", "When is the submission deadline?"], 2,
 "정답 ▶ ③ 누가 출품작을 심사하는가?\n이유: 심사 '기준'(기술·창의성·콘셉트)과 제출처(미술 선생님)는 있지만, 누가 심사하는지는 나와 있지 않아요. 제출받는 사람 = 심사하는 사람이라고 단정할 수 없어요.\n오답 ▶ ① 1인당 하나 ② 물감·파스텔 ④ 학교 웹사이트 ⑤ 11월 20일 → 모두 답할 수 있음")]
PICK1 = [PK(p, 'Illustrate', 'memorable', 'forgettable', "정답 ▶ memorable (기억에 남는)\n오답 ▶ forgettable (잊기 쉬운)\n이유: 학교생활 중 '기억에 남는' 순간을 그려서 달력에 실어요."),
 PK(p, 'Entries are', 'limited', 'unlimited', "정답 ▶ limited (제한된)\n오답 ▶ unlimited (무제한의)\n이유: one per student — 1인당 하나로 '제한'"),
 PK(p, 'Artistic materials', 'accepted', 'banned', "정답 ▶ accepted (허용된)\n오답 ▶ banned (금지된)\n이유: 물감·파스텔은 '허용', 디지털 작품은 불가"),
 PK(p, 'Winning artworks', 'displayed', 'deleted', "정답 ▶ displayed (게시된)\n오답 ▶ deleted (삭제된)\n이유: 수상작은 학교 웹사이트에 '게시'돼요.")]
TF = [TF(p, "The contest is held every year.", True, "annual", "정답 ▶ T\n이유: annual(매년 열리는) 대회예요."),
 TF(p, "Each student may submit up to three entries.", False, "limited to one per student", "정답 ▶ F\n이유: 1인당 하나로 제한돼요."),
 TF(p, "Students can submit artworks made on a computer.", False, "No digitally produced artworks will be allowed", "정답 ▶ F\n이유: 디지털로 제작한 작품은 허용되지 않아요."),
 TF(p, "Pastels can be used for the contest.", True, "paint and pastels are accepted", "정답 ▶ T\n이유: 물감과 파스텔은 허용돼요."),
 TF(p, "Creativity is one of the judging criteria.", True, "creativity", "정답 ▶ T\n이유: 심사 기준은 예술적 기술, 창의성, 콘셉트예요."),
 TF(p, "Only one winner will be chosen.", False, "12 winners", "정답 ▶ F\n이유: 매달 한 명씩 12명이에요."),
 TF(p, "Winning artworks will be shown in the school hallway.", False, "displayed on the school website", "정답 ▶ F\n이유: 학교 웹사이트에 게시돼요."),
 TF(p, "Entries must be handed in to an art teacher by November 20.", True, "Submit your entry to any art teacher by November 20", "정답 ▶ T\n이유: 11월 20일까지 미술 선생님 누구에게나 제출해요.")]
MC = [MC(p, "안내문의 내용과 일치하지 <u>않는</u> 것은?", [
 "Winners will receive cash prizes.", "Each student can enter only one artwork.", "Digital artworks are not allowed.", "There will be twelve winners.", "The deadline is November 20."],
 "정답 ▶ Winners will receive cash prizes.\n이유: will be awarded a professional-grade art kit (전문가용 미술 도구 세트)\n포인트 ▶ enter = 출품하다 · deadline = 마감일",
 [["수상자는 현금 상금을 받는다.", "awarded a professional-grade art kit", "✗ 미술 도구 세트"], ["학생 1인당 한 작품만 출품할 수 있다.", "limited to one per student", "일치"], ["디지털 작품은 허용되지 않는다.", "No digitally produced artworks will be allowed", "일치"], ["수상자는 12명이다.", "12 winners", "일치"], ["마감일은 11월 20일이다.", "by November 20", "일치"]])]
PICK2 = [PK(p, 'Have your work', 'featured', 'feature', "정답 ▶ featured\n이유: have + 목적어 + p.p. — 작품이 달력에 '실리는' 수동 관계"),
 PK(p, 'Entries are', 'are limited', 'is limited', "정답 ▶ are\n이유: 주어 Entries(복수)"),
 PK(p, 'No digitally', 'digitally produced', 'digital produced', "정답 ▶ digitally\n이유: 과거분사 produced를 꾸미는 말 → 부사"),
 PK(p, '12 winners', 'be awarded', 'award', "정답 ▶ be awarded\n이유: 수상자가 상품을 '받는' 수동 → will be awarded + 목적어(art kit)")]
VERB = [VB(p, 'Winning artworks', 'displayed', 'display', "정답 ▶ displayed\n이유: 작품이 '게시되는' 수동 → will be displayed"),
 VB(p, 'Artistic materials', 'accepted', 'accept', "정답 ▶ accepted\n이유: 재료가 '허용되는' 수동 → are accepted")]
ERR = [ER(p, 'Have your work', [('featured', 'feature'), 'in', 'school'], 0, 'featured', "틀린 곳 ▶ ① feature → featured\n이유: have + 목적어(your work) + p.p. (작품이 실리는 수동)\n나머지 ▶ ② in our calendar ✔ ③ ✔")]
SCR = [0, 2, 4, 6, 8]
ORDER = []; INSERT = []; ODD = []
BLANK = [BL(p, 'Entries are', 'one per student', ["two per class", "three per student", "one per teacher"], "정답 ▶ one per student (학생 1인당 하나)\n오답 ▶ 숫자·단위를 바꾼 함정 — 안내문 일치에서 가장 많이 나오는 오답 유형"),
 BL(p, 'Submit your entry', 'November 20', ["October 20", "November 2", "December 20"], "정답 ▶ November 20 (11월 20일)\n오답 ▶ 날짜를 살짝 바꾼 함정 — 원문항 ⑤번도 10월로 바꾼 오답")]
GRAM = [{'q': "빈칸에 알맞은 것은?<br><b>Have your work ______ in our 2027 school calendar!</b>", 'opts': ["featured", "feature", "featuring", "to feature"], 'ex': "정답 ▶ featured\n이유: have + 목적어 + p.p. (목적어가 ~되게 하다)"},
 {'q': "빈칸에 알맞은 것은?<br><b>12 winners will ______ a professional-grade art kit.</b>", 'opts': ["be awarded", "award", "awarding", "be awarding"], 'ex': "정답 ▶ be awarded\n이유: award A B (A에게 B를 수여하다)의 수동 → A be awarded B"}]
