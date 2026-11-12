# 11/12 중산고: 학교 시험에 문법은 안 나옴 → 문법 단계 빼고 내용(다각도)·순서·삽입 강화. common.day 가 씀
from sents import S
def P(cs): return ' '.join(S[c] for c in cs)
def box(cs, mark=None):
    t = P(cs) if mark is None else mark
    return '<span class="exam-box en">' + t + '</span>'
def Q(stem, cs, opts, ex, mark=None): return {'q': '<b>' + stem + '</b>' + box(cs, mark), 'opts': opts, 'ex': ex}
ORD = ['(A) - (C) - (B)', '(B) - (A) - (C)', '(B) - (C) - (A)', '(C) - (A) - (B)', '(C) - (B) - (A)']
def abc(intro, chunks, seq, why):
    """chunks = 맞는 순서의 세 덩어리, seq = 그 덩어리에 붙일 이름 (예 'CAB' → 첫 덩어리가 (C))"""
    lab = dict(zip(seq, chunks))
    body = P(intro) + '<br>' + '<br>'.join('(%s) %s' % (L, P(lab[L])) for L in 'ABC')
    ans = ' - '.join('(%s)' % L for L in seq); a = ORD.index(ans)
    return {'q': '<b>주어진 글 다음에 이어질 글의 순서로 가장 적절한 것은?</b><span class="exam-box en">' + body + '</span>', 'opts': ORD, 'keep': True, 'a': a,
            'ex': '정답 ▶ ' + '①②③④⑤'[a] + ' ' + ans + '\n이유 ▶ ' + why}
def mark(cs, target, word):   # 지문 속 한 낱말에 밑줄
    t = P(cs); assert t.count(target) == 1, target
    return t.replace(target, target.replace(word, '<u>' + word + '</u>', 1))

# ───────── DAY 16 (❶❷) ─────────
D1 = dict(
CONTENT=[
 Q('다음 글의 주제로 가장 적절한 것은?', ['A1','A2','A3','A4','B1','B2','B3','B4'],
   ['차별 속에서도 수학 재능을 키워 간 캐서린의 어린 시절과 학창 시절','흑인 대학의 수학 교육 과정이 바뀐 과정','어린이에게 수를 세는 습관이 중요한 이유','가족이 이사할 때 겪는 어려움','미국 공립 고등학교 제도의 발전'],
   '정답 ▶ 차별 속에서도 수학 재능을 키워 간 캐서린의 어린 시절과 학창 시절\n이유 ▶ 수학 영재(prodigy) → 차별적 교육 제도(segregated) → 이사해서 고등학교 입학 → 15세 대학 입학 → 3학년에 모든 과정 수강\n오답 ▶ ② 대학 교육 과정 변화 ③ 수 세기 습관 일반론 ④ 이사의 어려움 ⑤ 제도 발전 → 모두 언급 없거나 일부 소재\n포인트 ▶ 주제는 처음~끝을 다 묶는 말: 인물 + 재능 + 역경'),
 Q('다음 글의 제목으로 가장 적절한 것은?', ['B4','B5','B6','B7','B8','B9','B10','B11'],
   ['A Gifted Student Facing an Uncertain Future','How Segregation Ended in West Virginia','The Easiest Way to Find a Research Job','A Mentor Who Found Jobs for All His Students','Why Teaching Was the Most Popular Job'],
   '정답 ▶ A Gifted Student Facing an Uncertain Future (불확실한 미래를 마주한 재능 있는 학생)\n이유 ▶ 모든 과정을 마친 뛰어난 학생 → 일자리는 "네 문제" → 앞길이 불확실(unclear)하지만 헤쳐 나갈 힘 → 교사가 유일한 선택\n오답 ▶ ② 차별이 끝난 이야기 ✗ ③ 쉬운 방법 ✗ ④ 멘토는 일자리를 찾아 주지 않음 ⑤ 인기 직업이 아니라 유일한 선택지'),
 {'q': '<b>Why did Katherine\'s father move the family 200 kilometers away?</b>' + box(['B1','B2']),
  'opts': ['Because black students could not enter high school in their hometown.','Because he found a better job in another city.','Because Katherine wanted to live near her mentor.','Because their house was too small for four children.','Because the college asked Katherine to move.'],
  'ex': '정답 ▶ Because black students could not enter high school in their hometown.\n이유 ▶ segregated education system, black students could not enter high school → So her father moved ~ so that she could enter high school\n포인트 ▶ So(그래서) 앞 문장이 이유'},
 Q('밑줄 친 That이 가리키는 것으로 가장 적절한 것은?', [], ['연구 수학자로서 일자리를 어디에서 찾을지의 문제','멘토의 특별 수업을 듣는 일','고등학교에 입학하는 일','최우등으로 대학을 졸업하는 일','가족이 200킬로미터 떨어진 곳으로 이사하는 일'],
   '정답 ▶ 연구 수학자로서 일자리를 어디에서 찾을지의 문제\n이유 ▶ 바로 앞 질문 "Where will I find a job?"에 대한 대답 → That = 일자리를 찾는 일\n포인트 ▶ 지칭은 바로 앞 문장부터 확인', mark=mark(['B6','B7','B8'], '"That," he replied', 'That')),
 Q('밑줄 친 부분에서 알 수 있는 멘토의 심정으로 가장 적절한 것은?', [], ['regretful and worried','proud and satisfied','calm and indifferent','angry and annoyed','relieved and grateful'],
   '정답 ▶ regretful and worried (안타깝고 걱정스러운)\n이유 ▶ 뛰어난 학생에게 직업 기회를 말해야 할 때 기쁘지 않았다(not happy) → 흑인 여성에게 열린 길이 거의 없어서\n오답 ▶ ② 자랑스럽고 만족 ③ 무관심 ④ 화남 ⑤ 안도·감사', mark=mark(['B5'], 'he was not happy when he had to tell his outstanding student about her career opportunities', 'he was not happy when he had to tell his outstanding student about her career opportunities')),
 Q('윗글에서 추론할 수 있는 것으로 가장 적절한 것은?', ['B8','B9','B10','B11'],
   ['At that time, few career options were open to a black woman like Katherine.','Research jobs were easy to find for honor graduates.','Her mentor had already arranged a research position for her.','Katherine chose teaching because she disliked math research.','Private schools competed to hire Katherine.'],
   '정답 ▶ At that time, few career options were open to a black woman like Katherine.\n이유 ▶ "That will be your problem" + teaching was the only option available to her → 선택지가 거의 없었음\n오답 ▶ ② 쉽게 찾음 ✗ ③ 이미 마련 ✗ ④ 연구가 싫어서 ✗ ⑤ 사립학교 ✗ (black public school)'),
 Q('밑줄 친 부분에 드러난 Katherine의 태도로 가장 적절한 것은?', [], ['determined','hopeless','careless','jealous','indifferent'],
   '정답 ▶ determined (단호한, 굳게 마음먹은)\n이유 ▶ 앞길이 불확실하고 장애물로 가득했지만 스스로 길을 헤쳐 나갈 힘이 있다는 걸 알았다\n오답 ▶ hopeless 절망적인 · careless 부주의한 · jealous 질투하는 · indifferent 무관심한', mark=mark(['B9'], 'Katherine knew she had the strength to make her own way', 'Katherine knew she had the strength to make her own way')),
 Q('다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 적절한 것은?<br>➠ Despite a(n) (A)______ education system, Katherine (B)______ her studies and graduated from college with highest honors.', ['B1','B2','B3','B4','B10'],
   ['(A) segregated – (B) continued','(A) integrated – (B) continued','(A) segregated – (B) abandoned','(A) excellent – (B) delayed','(A) integrated – (B) abandoned'],
   '정답 ▶ (A) segregated – (B) continued\n이유 ▶ 흑인 학생이 고등학교에 못 가는 분리된 제도 → 그래도 이사해서 공부를 이어가 최우등 졸업\n포인트 ▶ Despite(~에도 불구하고) 뒤에는 어려움, 주절에는 극복'),
],
ABC=[
 abc(['A1','A2'], [['A3','A4'], ['B1','B2'], ['B3','B4']], 'BCA', '수학 영재 → (B) 어린 시절 모든 것을 셌고 고등학교 수학을 고대 → (C) But 고향은 흑인이 고등학교에 못 감, So 이사 → (A) 고등학교 졸업 후 15세에 대학, 3학년에 모든 과정'),
 abc(['B4'], [['B5','B6'], ['B7','B8'], ['B9','B10']], 'CAB', '모든 과정을 다 들음 → (C) 멘토의 특별 수업·"연구 수학자가 될 거야" → (A) "어디서 일자리를?" "그건 네 문제" → (B) 앞길은 불확실하지만 힘이 있었음, 1935년 졸업 후 교사'),
 abc(['A4'], [['B1','B2'], ['B3','B4','B5'], ['B6','B7','B8']], 'ACB', '고등학교에 빨리 가고 싶었음 → (A) But 차별 제도, So 이사 → (C) 대학 입학·모든 과정·멘토의 특별 수업 → (B) he told(멘토가 말함)·"어디서 일자리를?"·"네 문제"'),
],
ORDER=[
 (['A1','A2','A3','A4','B1','B2'], ['1918년 흑인 가정의 막내로 태어남','어릴 때부터 수학 영재','어린 시절 모든 것을 셌다고 회상','고등학교에서 수학을 빨리 배우고 싶었음','그러나(But) 고향은 흑인이 고등학교에 못 가는 제도','그래서(So) 아버지가 이사']),
 (['B3','B4','B5','B6','B7'], ['15세에 흑인 대학 입학','3학년 때 모든 수학 과정 수강','멘토의 특별 수업, 직업 이야기는 기쁘지 않음','멘토: 훌륭한 연구 수학자가 될 거야','캐서린: 어디서 일자리를?']),
],
INSERT=[
 (['A1','A2','A3','A4','B1','B2'], 5, ['막내로 태어남','수학 영재','모든 것을 셌음','고등학교 수학을 고대','흑인은 고등학교에 못 감','그래서 이사'], '정답 ▶ ⑤\n이유 ▶ So(그래서)는 "흑인 학생이 고등학교에 들어갈 수 없었다"의 결과 → 그 문장 바로 뒤'),
 (['B3','B4','B5','B6','B7','B8'], 3, ['15세 대학 입학','모든 과정 수강','멘토의 특별 수업','멘토: 연구 수학자가 될 거야','어디서 일자리를?','네 문제'], '정답 ▶ ③\n이유 ▶ he(멘토)가 "this career(연구 수학자)"를 준비시키겠다는 말 → 멘토가 직업 이야기를 해야 했다는 문장 뒤, 캐서린의 질문 앞'),
 (['B7','B8','B9','B10','B11'], 3, ['어디서 일자리를?','네 문제','앞길은 불확실, 힘은 있음','1935년 졸업, 교사로 시작','그 당시 유일한 선택'], '정답 ▶ ③\n이유 ▶ 앞길이 불확실했지만 힘이 있었다 → 그래서 1935년 졸업하고 교사로 시작 → At that time(그 당시) 유일한 선택'),
 (['A1','A2','A3','A4','B1'], 2, ['막내로 태어남','수학 영재','모든 것을 셌음(회상)','고등학교 수학을 고대','흑인은 고등학교에 못 감'], '정답 ▶ ②\n이유 ▶ "어린 시절을 회상하며 모든 것을 셌다"는 수학 영재라는 문장의 예 → 그 뒤, She excitedly added(덧붙였다) 앞'),
],
ODD=[(['B4','B5','The college offered free meals to all of its black students.','B6'], 2, '정답 ▶ ③\n이유 ▶ 멘토가 뛰어난 캐서린에게 특별 수업을 해 주고 진로를 이야기하는 흐름 → 학교 급식 이야기는 무관')],
)
# ───────── DAY 17 (❸) ─────────
D2 = dict(
CONTENT=[
 Q('다음 글의 주제로 가장 적절한 것은?', ['C1','C2','C3','C4','C5','C6','C7','C8','C9','C10','C11','C12','C13','C14'],
   ['NASA에서 차별에 맞서 질문으로 관행을 바꾸고 성과를 낸 캐서린','NASA가 흑인 직원을 많이 뽑은 이유','우주선을 궤도에 올리는 계산 방법','1950년대 미국 사무실의 근무 환경 개선','연구 보고서를 잘 쓰는 방법'],
   '정답 ▶ NASA에서 차별에 맞서 질문으로 관행을 바꾸고 성과를 낸 캐서린\n이유 ▶ 흑인 컴퓨터들이 겪은 차별 → 회의 참석 요청·"그런 법이 있나요?" → 관행을 끝냄 → 1960년 첫 여성 저자\n오답 ▶ ② 많이 뽑음 ✗ ③ 계산 방법은 세부 소재 ④ 환경 개선 ✗ ⑤ 보고서 작성법 ✗'),
 Q('다음 글의 제목으로 가장 적절한 것은?', ['C6','C7','C8','C9','C10','C11','C12'],
   ['One Question That Opened a Closed Door','Why NASA Hired Only White Engineers','The Invention of the Electronic Computer','How to Hold an Effective Meeting','A Law That Banned Women from Meetings'],
   '정답 ▶ One Question That Opened a Closed Door (닫힌 문을 연 질문 하나)\n이유 ▶ "Is there a law that says I can\'t go?" → 남자 직원들이 들여보낼 수밖에 없었음 → 차별적 관행이 끝남\n오답 ▶ ② 백인만 고용 ✗ ③ 컴퓨터 발명 ✗ ④ 회의 진행법 ✗ ⑤ 그런 법은 없었음'),
 Q('밑줄 친 "Black computers"가 뜻하는 것으로 가장 적절한 것은?', [], ['손으로 복잡한 계산을 해 기술자들을 도운 흑인 여성들','흑인 기술자들이 만든 전자 계산기','검은색으로 칠한 NASA의 컴퓨터','컴퓨터를 고치는 흑인 직원들','백인 남성 기술자들의 별명'],
   '정답 ▶ 손으로 복잡한 계산을 해 기술자들을 도운 흑인 여성들\n이유 ▶ who did complex calculations manually to support white male engineers\n포인트 ▶ manually = by hand (손으로)', mark=mark(['C2'], '"Black computers"', '"Black computers"')),
 Q('밑줄 친 "the girls"에 담긴 의미로 가장 적절한 것은?', [], ['전문직 여성들을 낮춰 부르는 차별적인 표현','어린 여학생들을 가리키는 친근한 말','회의를 준비하는 비서들','NASA에서 일하는 모든 직원','캐서린의 동료 백인 여성들'],
   '정답 ▶ 전문직 여성들을 낮춰 부르는 차별적인 표현\n이유 ▶ 앞에서 전문직 여성인데도 "girl" 같은 말로 불렸다(being referred to with terms like "girl" despite being professional women)는 차별을 설명함\n포인트 ▶ 따옴표 표현은 글쓴이의 비판적 거리두기', mark=mark(['C6','C7'], 'that "the girls" didn', '"the girls"')),
 {'q': '<b>Katherine이 밑줄 친 질문을 한 의도로 가장 적절한 것은?</b>' + box([], mark(['C7','C8','C9'], 'Is there a law that says I can\'t go?', 'Is there a law that says I can\'t go?')),
  'opts': ['회의에 못 갈 정당한 근거가 없다는 것을 지적하려고','새로운 법을 만들자고 제안하려고','법을 공부하고 싶다고 밝히려고','회의 일정을 바꿔 달라고 부탁하려고','동료들에게 사과를 요구하려고'],
  'ex': '정답 ▶ 회의에 못 갈 정당한 근거가 없다는 것을 지적하려고\n이유 ▶ "여자들은 보통 안 간다"는 관행뿐, 막는 법은 없음 → 당황한 남자 직원들이 들여보낼 수밖에 없었음\n포인트 ▶ 질문의 형태지만 실제로는 반박'},
 Q('밑줄 친 부분에 드러난 남자 직원들의 심경으로 가장 적절한 것은?', [], ['embarrassed','delighted','proud','bored','grateful'],
   '정답 ▶ embarrassed (당황한)\n이유 ▶ 막을 근거가 없어 들여보낼 수밖에 없었음(had no choice but to let her in)\n오답 ▶ delighted 기쁜 · proud 자랑스러운 · bored 지루한 · grateful 고마운', mark=mark(['C8','C9'], 'The embarrassed male workers had no choice but to let her in', 'The embarrassed male workers had no choice but to let her in')),
 Q('윗글에 나타난 Katherine의 심경 변화로 가장 적절한 것은?', ['C6','C7','C8','C9','C10','C11','C12'],
   ['frustrated → proud','proud → ashamed','excited → bored','calm → nervous','hopeful → disappointed'],
   '정답 ▶ frustrated → proud (답답한 → 자랑스러운)\n이유 ▶ 큰 공헌에도 회의에서 빠짐·"여자들은 안 간다" → 질문으로 관행을 끝내고 노력이 결실 → She felt proud\n오답 ▶ ② 부끄러움 ✗ ③ 지루함 ✗ ④ 초조 ✗ ⑤ 실망 ✗'),
 {'q': '<b>Why was Katherine\'s 1960 research paper significant?</b>' + box(['C13','C14']),
  'opts': ['It was the first time a woman in her division was credited as an author.','It was the first paper about sending people to Mars.','It was written by Katherine alone without any help.','It ended segregation in every NASA office.','It won a national prize for science.'],
  'ex': '정답 ▶ It was the first time a woman in her division was credited as an author.\n이유 ▶ That was the first time a woman in her division received credit as an author of a research report.\n오답 ▶ ② 화성 ✗(우주선 궤도) ③ 다른 기술자와 함께 씀 ④ ⑤ 언급 없음\n포인트 ▶ receive credit as an author = 저자로 인정받다'},
 Q('다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 적절한 것은?<br>➠ Although Katherine faced (A)______ at NASA, she (B)______ an unfair custom by asking a bold question.', ['C6','C7','C8','C9','C10'],
   ['(A) discrimination – (B) ended','(A) praise – (B) ended','(A) discrimination – (B) followed','(A) support – (B) created','(A) praise – (B) followed'],
   '정답 ▶ (A) discrimination – (B) ended\n이유 ▶ 백인끼리만 하는 회의(차별) → 아무도 하지 않던 질문으로 차별적 관행을 끝냄(ended a discriminatory custom)'),
],
ABC=[
 abc(['C1'], [['C2','C3'], ['C4','C5'], ['C6','C7']], 'BAC', '1953년 NASA 취직 → (B) There(그곳에서) 흑인 컴퓨터로 일함·차별 → (A) 2주 만에 엘리트 부서로, There 유일한 흑인 여성 → (C) 공헌에도 회의는 백인끼리, 참석을 요청하자 "여자들은 안 간다"'),
 abc(['C7'], [['C8','C9'], ['C10','C11'], ['C12','C13','C14']], 'CBA', '"여자들은 보통 안 간다" → (C) "그런 법이 있나요?"·당황해 들여보냄 → (B) 질문으로 차별적 관행을 끝냄·노력이 결실 → (A) 자랑스러워하며 계속 일함·1960년 첫 여성 저자'),
 abc(['C4'], [['C5','C6'], ['C7','C8','C9'], ['C10','C11','C12']], 'ACB', '엘리트 부서로 재배치 → (A) There 유일한 흑인 여성·회의는 백인끼리 → (C) 참석 요청·"그런 법이 있나요?"·들여보냄 → (B) 관행을 끝냄·노력이 결실·자랑스러움'),
],
ORDER=[
 (['C1','C2','C3','C4','C5'], ['1953년에야 NASA에 취직','흑인 컴퓨터로 손 계산','공헌했지만 차별을 견딤','2주 만에 엘리트 부서로','그곳의 유일한 흑인 여성']),
 (['C6','C7','C8','C9','C10'], ['회의는 백인끼리만','참석을 요청하자 "여자들은 안 간다"','"그런 법이 있나요?"','당황해서 들여보냄','질문으로 차별적 관행을 끝냄']),
 (['C10','C11','C12','C13','C14'], ['차별적 관행을 끝냄','장벽을 넘으려는 노력이 결실','자랑스러워하며 용기 있게 계속','1960년 궤도 진입에 관한 논문','부서에서 처음으로 여성이 저자로 인정']),
],
INSERT=[
 (['C1','C2','C3','C4','C5','C6'], 3, ['1953년 NASA 취직','흑인 컴퓨터','차별을 견딤','2주 만에 엘리트 부서로','There 유일한 흑인 여성','회의는 백인끼리'], '정답 ▶ ③\n이유 ▶ 다음 문장의 There는 엘리트 부서를 가리킴 → "엘리트 부서로 재배치"가 그 앞에 와야 함'),
 (['C6','C7','C8','C9','C10','C11'], 3, ['회의는 백인끼리','"여자들은 안 간다"','"그런 법이 있나요?"','당황해서 들여보냄','관행을 끝냄','노력이 결실'], '정답 ▶ ③\n이유 ▶ The embarrassed male workers(당황한 남자 직원들) → 캐서린의 질문 바로 뒤'),
 (['C10','C11','C12','C13','C14'], 3, ['관행을 끝냄','노력이 결실','자랑스러움','1960년 논문','첫 여성 저자'], '정답 ▶ ③\n이유 ▶ That was the first time ~의 That = 1960년 논문 → 논문 문장은 그 바로 앞, 자랑스러워하며 계속 일했다는 문장 뒤'),
 (['C1','C2','C3','C4','C5'], 2, ['1953년 NASA 취직','흑인 컴퓨터로 손 계산','공헌했지만 차별','2주 만에 재배치','유일한 흑인 여성'], '정답 ▶ ②\n이유 ▶ they(=Black computers)가 공헌했지만 차별을 견뎠다 → 흑인 컴퓨터를 소개한 문장 뒤'),
],
ODD=[(['C3','C4','Some engineers moved to other countries to build their own rockets.','C5'], 2, '정답 ▶ ③\n이유 ▶ 차별을 겪던 캐서린이 엘리트 부서로 옮겨 유일한 흑인 여성이 된 흐름 → 다른 기술자들의 해외 이주는 무관')],
)
# ───────── DAY 18 (❹❺) ─────────
D3 = dict(
CONTENT=[
 Q('다음 글의 주제로 가장 적절한 것은?', ['D1','D2','D3','D4','D5','D6','D7','D8'],
   ['전자 컴퓨터보다 더 신뢰받은 캐서린의 손 계산과 우주 탐사 공헌','전자 컴퓨터가 우주 탐사에 처음 쓰인 과정','존 글렌이 우주 비행사가 된 계기','계산자(slide rule) 사용법','화성 탐사 계획의 현재 진행 상황'],
   '정답 ▶ 전자 컴퓨터보다 더 신뢰받은 캐서린의 손 계산과 우주 탐사 공헌\n이유 ▶ 첫 문장(손 계산이 디지털 컴퓨터보다 신뢰받음) → 글렌의 확인 요청 → 첫 지구 궤도 비행 → 아폴로 11호·화성 계획\n오답 ▶ ② 컴퓨터는 오류가 많았다는 배경 ③ 글렌의 계기 ✗ ④ 사용법 ✗ ⑤ 세부 언급'),
 Q('다음 글의 제목으로 가장 적절한 것은?', ['D1','D2','D3','D4','D5','D6','D7','D8','E1','E2','E3','E4','E5'],
   ['The Hidden Hands Behind America\'s Space Age','The Rise of Electronic Computers at NASA','John Glenn\'s Childhood Dream','Why Astronauts Fear Space Travel','How to Use a Slide Rule Correctly'],
   '정답 ▶ The Hidden Hands Behind America\'s Space Age (미국 우주 시대를 뒷받침한 숨은 손)\n이유 ▶ 손 계산으로 첫 궤도 비행·아폴로 11호에 기여 → 은퇴 후 STEM 교육·훈장·건물 → 잊히지 않을 유산\n오답 ▶ ② 컴퓨터의 성장 ✗ ③ 글렌의 꿈 ✗ ④ 두려움 ✗ ⑤ 사용법 ✗'),
 {'q': '<b>Why did John Glenn ask Katherine to check the numbers?</b>' + box(['D3','D4','D5']),
  'opts': ['He was concerned about the accuracy of the electronic computer.','He wanted Katherine to replace him as an astronaut.','The computer had not been introduced yet.','Katherine had designed the spaceship herself.','He did not know how to use a slide rule.'],
  'ex': '정답 ▶ He was concerned about the accuracy of the electronic computer.\n이유 ▶ 전자 컴퓨터가 작은 오류를 많이 냄 → Glenn, who was concerned about its accuracy\n오답 ▶ ③ 1년 전에 이미 도입됨 ②④⑤ 언급 없음'},
 Q('밑줄 친 its가 가리키는 것으로 가장 적절한 것은?', [], ['the electronic computer','the spaceship','the space program','Katherine Johnson','the Earth'],
   '정답 ▶ the electronic computer\n이유 ▶ 앞 문장: 전자 컴퓨터가 궤도를 계산했지만 작은 오류를 많이 냄 → 그 정확성(its accuracy)을 걱정', mark=mark(['D3','D4'], 'concerned about its accuracy', 'its')),
 Q('밑줄 친 부분이 뜻하는 것으로 가장 적절한 것은?', [], ['캐서린이 계산을 확인해 주면 안심하고 비행하겠다','캐서린도 함께 우주에 가야 한다','숫자가 좋으면 비행을 미루겠다','컴퓨터의 계산만 믿겠다','캐서린이 비행 일정을 정해야 한다'],
   '정답 ▶ 캐서린이 계산을 확인해 주면 안심하고 비행하겠다\n이유 ▶ "If she says the numbers are good, I\'m good to go." = 그녀가 맞다고 하면 갈 준비가 됐다 → 캐서린에 대한 전적인 신뢰\n포인트 ▶ be good to go = 준비가 다 되다', mark=mark(['D4','D5'], 'I\'m good to go', 'I\'m good to go')),
 Q('윗글에서 추론할 수 있는 것으로 가장 적절한 것은?', ['D1','D2','D3','D4','D5','D6','D7'],
   ['Even after electronic computers were introduced, NASA still relied on human experts.','NASA stopped using computers after 1962.','Glenn checked all the calculations by himself.','Katherine thought computers would never make mistakes.','The flight was cancelled because of the computer\'s errors.'],
   '정답 ▶ Even after electronic computers were introduced, NASA still relied on human experts.\n이유 ▶ 전자 컴퓨터가 쓰였지만 오류 → 글렌이 캐서린에게 손으로 확인 요청 → 결국 비행 성공\n오답 ▶ ② 사용 중단 ✗ ③ 캐서린이 확인 ④ 오류를 냄 ⑤ 비행 성공'),
 Q('다음 글의 요지로 가장 적절한 것은?', ['E1','E2','E3','E4','E5'],
   ['캐서린은 은퇴 후에도 공헌을 이어 갔고, 그 업적은 널리 기려지고 있다.','캐서린은 은퇴 후 NASA로 돌아가 다시 일했다.','대통령 훈장은 과학자에게만 주어진다.','STEM 교육은 남학생에게 더 필요하다.','NASA 건물의 이름은 지역의 이름을 따서 짓는다.'],
   '정답 ▶ 캐서린은 은퇴 후에도 공헌을 이어 갔고, 그 업적은 널리 기려지고 있다.\n이유 ▶ 은퇴 후 흑인 소녀들의 STEM 교육 지원 → 대통령 자유 훈장 → 그녀 이름의 건물 → 잊히지 않을 유산\n오답 ▶ ② NASA 복귀 ✗ ③④⑤ 언급 없음'),
 Q('밑줄 친 부분에서 오바마 대통령이 말하려는 것으로 가장 적절한 것은?', [], ['캐서린은 성별과 인종에 대한 사회의 편견에 갇히지 않고 인류의 영역을 넓혔다.','캐서린은 사회가 기대한 대로 평범한 삶을 살았다.','캐서린은 정치에 참여해 사회를 바꿨다.','인류는 더 이상 우주에 갈 필요가 없다.','성별과 인종에 따라 맡을 일이 정해져 있다.'],
   '정답 ▶ 캐서린은 성별과 인종에 대한 사회의 편견에 갇히지 않고 인류의 영역을 넓혔다.\n이유 ▶ refused to be limited by society\'s expectations of her gender and race / expanding the boundaries of humanity\'s reach\n포인트 ▶ refuse to be limited = 갇히기를 거부하다', mark=mark(['E3'], 'refused to be limited by society\'s expectations of her gender and race while expanding the boundaries of humanity\'s reach', 'refused to be limited by society\'s expectations of her gender and race while expanding the boundaries of humanity\'s reach')),
 Q('Katherine Johnson에 관한 윗글의 내용으로 알 수 <u>없는</u> 것은?', ['D6','D7','D8','E1','E2','E3','E4','E5'],
   ['그녀가 대학에서 받은 학위의 이름','그녀가 계산을 확인하는 데 걸린 시간','그녀가 NASA에서 일한 기간','그녀의 이름을 딴 건물이 세워진 해','그녀가 세상을 떠난 나이'],
   '정답 ▶ 그녀가 대학에서 받은 학위의 이름\n이유 ▶ ② 하루 반(a day and a half) ③ 33년 ④ 2017년 ⑤ 101세 → 모두 본문에 있음. 학위 이름은 없음'),
 Q('다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 적절한 것은?<br>➠ Katherine\'s (A)______ calculations made historic space missions possible, and she was (B)______ for her contributions.', ['D1','D4','D5','D6','D7','E3','E4'],
   ['(A) accurate – (B) honored','(A) careless – (B) honored','(A) accurate – (B) blamed','(A) slow – (B) praised','(A) careless – (B) punished'],
   '정답 ▶ (A) accurate – (B) honored\n이유 ▶ 컴퓨터보다 믿을 수 있는 손 계산 → 첫 궤도 비행 성공 → 대통령 훈장·건물 이름으로 기림(in her honor)'),
],
ABC=[
 abc(['D1'], [['D2','D3'], ['D4','D5'], ['D6','D7']], 'BCA', '손 계산이 더 신뢰받음 → (B) 1962년 글렌의 첫 궤도 비행 준비, 컴퓨터의 오류 → (C) 정확성을 걱정한 글렌의 확인 요청 → (A) 연필과 계산자로 확인, 결국 첫 궤도 비행'),
 abc(['D7'], [['D8'], ['E1','E2'], ['E3','E4']], 'CAB', '글렌의 첫 궤도 비행 → (C) also 아폴로 11호·화성 계획 → (A) 1986년 은퇴, 그 후(After that) STEM 교육 → (B) For her contributions 대통령 훈장, 2017년 건물'),
 abc(['E1'], [['E2'], ['E3'], ['E4','E5']], 'ACB', '1986년 은퇴 → (A) After that STEM 교육에 헌신 → (C) For her contributions 2015년 대통령 훈장 → (B) 2017년 건물, 2020년 별세와 유산'),
],
ORDER=[
 (['D1','D2','D3','D4','D5'], ['손 계산이 디지털 컴퓨터보다 신뢰받음','1962년 글렌의 첫 지구 궤도 비행 준비','전자 컴퓨터가 작은 오류를 많이 냄','정확성을 걱정한 글렌이 확인을 부탁','"그녀가 맞다면 나는 갈 준비가 됐다"']),
 (['D5','D6','D7','D8','E1'], ['"그녀가 맞다면 갈 준비가 됐다"','연필과 계산자로 하루 반 동안 확인','결국 글렌이 첫 궤도 비행','아폴로 11호·화성 계획에도 참여','1986년 33년 만에 은퇴']),
 (['E1','E2','E3','E4','E5'], ['1986년 은퇴','그 후 흑인 소녀들의 STEM 교육에 헌신','2015년 대통령 자유 훈장','2017년 그녀의 이름을 딴 건물','2020년 101세로 별세, 유산은 잊히지 않음']),
],
INSERT=[
 (['D1','D2','D3','D4','D5','D6'], 3, ['손 계산이 신뢰받음','글렌의 비행 준비','컴퓨터의 오류','글렌이 확인을 부탁','"갈 준비가 됐다"','하루 반 동안 확인'], '정답 ▶ ③\n이유 ▶ its accuracy의 its = 전자 컴퓨터 → 컴퓨터가 오류를 냈다는 문장 바로 뒤'),
 (['D3','D4','D5','D6','D7','D8'], 4, ['컴퓨터의 오류','확인 부탁','"갈 준비가 됐다"','하루 반 동안 확인','결국 첫 궤도 비행','아폴로 11호'], '정답 ▶ ④\n이유 ▶ Eventually(결국) 첫 궤도 비행 → 캐서린이 계산을 다 확인한 뒤, also(또한) 다른 계획에 참여했다는 문장 앞'),
 (['E1','E2','E3','E4','E5'], 1, ['1986년 은퇴','그 후 STEM 교육','대통령 훈장','건물 헌정','별세와 유산'], '정답 ▶ ①\n이유 ▶ After that(그 후) = 은퇴 후 → 은퇴 문장 바로 뒤, For her contributions(그녀의 공헌으로) 앞'),
 (['D6','D7','D8','E1','E2'], 3, ['하루 반 동안 확인','첫 궤도 비행','아폴로 11호·화성','1986년 은퇴','STEM 교육'], '정답 ▶ ③\n이유 ▶ 우주 탐사 공헌(아폴로 11호·화성) 이야기가 끝나고 33년 만의 은퇴 → After that 앞'),
],
ODD=[(['E2','E3','Many astronauts later wrote books about their own adventures in space.','E4'], 2, '정답 ▶ ③\n이유 ▶ 은퇴 후 캐서린의 공헌과 그녀를 기린 일들의 흐름 → 우주 비행사들의 책 이야기는 무관')],
)
