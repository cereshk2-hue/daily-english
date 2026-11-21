# 11/21 안곡고1 · 2026년 9월 고1 학평(인천) 30 · 33~42번 → 새 단원 h1-mock-2609-angok (한 지문 = 하루 DAY 1~10, id q30…q41)
# 원자료: 지문분석 hwp(work_src/ag2609_src.hwp) → generators/hwpread_u.py → work/ag2609/e2609.txt → extract.py·extract2.py·prep.py
# 지문별 문항 p30 p33~p41.py (jfw = jd2610과 같음 + mk), 이 파일로 생성
import sys, re
sys.path.insert(0, '/home/claude/srcrepo/gen'); sys.path.insert(0, '/home/claude/srcrepo/gen/ag2609')
from gencommon import write
import jfw, importlib
MODS = [('p30', '30', '30 어휘 · 적절한 단락 길이'), ('p33', '33', '33 빈칸 · 모방으로서의 예술'), ('p34', '34', '34 빈칸 · 몸이 아는 달리기'),
 ('p35', '35', '35 무관한 문장 · 반려견 목욕'), ('p36', '36', '36 글의 순서 · 스도쿠와 수학'), ('p37', '37', '37 글의 순서 · 망원경 이전의 천문학'),
 ('p38', '38', '38 문장 삽입 · 측정의 일관성'), ('p39', '39', '39 문장 삽입 · 농부 개미'), ('p40', '40', '40 요약문 · 자아존중감이라는 감시 기제'),
 ('p41', '41~42', '41~42 장문 · 슬랭과 새로운 미디어')]
days = []
for k, (mod, n, story) in enumerate(MODS):
    m = importlib.import_module(mod)
    d = jfw.jday(m.p.n, 'DAY %d' % (k + 1), '%s번' % n, story, m.p, m)
    d = jfw.spread(d, re.match(r'\d+', n).group()); d['id'] = 'q' + re.match(r'\d+', n).group()
    days.append(d)
PK = {'id': 'h1-mock-2609-angok', 'school': '고1 모의고사(2026년 9월 학평·안곡고)', 'unit': '30 · 33~42번', 'pick': True,
      'title': 'September 2026 Mock Test', 'titleKo': '2026년 9월 고1 학력평가(인천) · 안곡고 내신 범위', 'exam': '내신·모의고사', 'prose': True, 'teacherPhone': '', 'days': days}
head = ('/* 고1 2026년 9월 전국연합학력평가(인천광역시교육청) · 안곡고 내신 범위 30 · 33~42번 (한 지문 = 하루, DAY 1~10)\n'
        '   원자료: 지문분석 hwp → gen/ag2609/extract*.py · prep.py, 지문별 문항 p30 p33~p41.py, mkunit.py 로 생성.\n'
        '   지문은 정답이 반영된 원문(30번 harder, 33·34번 빈칸 채움, 35번 ④ 문장 뺌, 36·37번 바른 순서, 38·39번 주어진 문장 제자리, 42번 (e) stronger), 실전 문항에는 시험지 원문 그대로.\n*/\n')
write(PK, '/home/claude/proj/data/h1-mock-2609-angok.js', head)
print(len(days), sum(sum(len(s['items']) for s in d['steps']) for d in days), [d['id'] for d in days])
