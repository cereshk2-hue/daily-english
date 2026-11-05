# 11/5: YBM(김은형) 3과 본문을 '중산고1 모의고사 2025년 9월' 단원 뒤에 DAY 16~18 로 붙인다 (따로 만든 단원 카드는 없앰)
import json,subprocess,sys,common,y1,y2,y3
sys.path.insert(0,'/home/claude/work/gen'); from gencommon import write
F='/home/claude/proj/data/h1-mock-2509.js'
P=json.loads(subprocess.check_output(['node','-e',"global.window={};require('%s');console.log(JSON.stringify(window.PKG))"%F]))
src=open(F).read(); head=src[:src.index('window.PKG')]; tail=src[src.index('/* WRAPUP-TESTS'):]
P.pop('tests',None)
P['days']=[d for d in P['days'] if not d['id'].startswith('y')]
P['days']+=[common.day('y1','DAY 16','YBM 3과 본문 ❶❷','교과서 · 수학 영재 캐서린 · 차별 속에서 이어 간 공부',['❶','❷'],y1),
            common.day('y2','DAY 17','YBM 3과 본문 ❸','교과서 · NASA의 흑인 컴퓨터 · 차별에 맞선 질문',['❸'],y2),
            common.day('y3','DAY 18','YBM 3과 본문 ❹❺','교과서 · 손 계산으로 연 우주 시대 · 은퇴 후의 공헌과 유산',['❹','❺'],y3)]
P['unit']='18~24 · 26 · 29~42번 + YBM 3과 본문'
if 'YBM' not in head: head=head.replace('*/','   DAY 16~18 = YBM(김은형) 공통영어2 Lesson 3 본문 (work/ybm3/gen/attach.py). exam.py(실전 변형·문법 축소)는 merge.py 뒤에 돌릴 것.\n*/',1)
write(P,F,head); open(F,'a').write(tail)
print([(d['id'],d['name'],d['range']) for d in P['days']][-5:])
