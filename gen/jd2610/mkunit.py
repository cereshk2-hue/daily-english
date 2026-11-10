import sys
sys.path.insert(0, '/home/claude/work/gen'); sys.path.insert(0, '/home/claude/work/jd2610/gen')
from gencommon import write
from build import build
MODS = [('p20', '20번', '20 필자의 주장 · 세계 시민 정체성'), ('p21', '21번', '21 밑줄 함축 의미 · 타이타닉호의 갑판 의자'), ('p22', '22번', '22 글의 요지 · 시간은 사회적 산물'),
 ('p23', '23번', '23 글의 주제 · 내부 고발자 보호'), ('p24', '24번', '24 글의 제목 · 미래에 대한 환상'), ('p28', '28번', '28 안내문 일치 · 달력 디자인 대회'),
 ('p29', '29번', '29 어법 · 생물학적 불멸'), ('p30', '30번', '30 어휘 · 발전소 보조금'), ('p31', '31번', '31 빈칸 · Star Trek과 희소성'),
 ('p32', '32번', '32 빈칸 · 경청받는 느낌'), ('p33', '33번', '33 빈칸 · 장소와 경험'), ('p34', '34번', '34 빈칸 · 단순화 가정'),
 ('p35', '35번', '35 무관한 문장 · 번아웃은 구조적 문제'), ('p37', '37번', '37 글의 순서 · 원격 협업의 틈'), ('p38', '38번', '38 문장 삽입 · 진실 착각 효과'),
 ('p39', '39번', '39 문장 삽입 · 잠수와 압력'), ('p40', '40번', '40 요약문 · 미역취의 화학 신호')]
days = build(MODS)
PK = {'id': 'h1-mock-2610-jeodong', 'school': '고1 모의고사(2026년 10월 학평·저동고)', 'unit': '20~24 · 28~35 · 37~40번', 'pick': True,
      'title': 'October 2026 Mock Test', 'titleKo': '2026년 10월 고1 학력평가 · 저동고 내신 범위', 'exam': '내신·모의고사', 'prose': True, 'teacherPhone': '', 'days': days}
head = ('/* 고1 2026년 10월 전국연합학력평가(경기도교육청) · 저동고 내신 범위 20~24 · 28~35 · 37~40번 (한 지문 = 하루, DAY 1~17)\n'
        '   원자료: 해설서 hwp → work/jd2610/gen/extract*.py · prep.py, 지문별 문항 p20~p40.py (jfw.py = 안곡고2 fw.py + 요약문·어휘 파서), mkunit.py 로 생성.\n'
        '   지문은 정답이 반영된 원문(29번 makes, 30번 increased, 35번 ③ 문장 뺌, 37번은 바른 순서), 실전 문항에는 시험지 원문 그대로.\n*/\n')
write(PK, '/home/claude/proj/data/h1-mock-2610-jeodong.js', head)
print(len(days), sum(sum(len(s['items']) for s in d['steps']) for d in days))
