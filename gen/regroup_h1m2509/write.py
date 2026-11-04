import json,sys
sys.path.insert(0,'/home/claude/work/gen')
from gencommon import write
src=open('orig_h1-mock-2509.js').read()
tail=src[src.index('/* WRAPUP-TESTS'):]
P=json.load(open('pkg.json'))
head='''/* 고1 2025학년도 9월 전국연합학력평가(인천광역시교육청 주관) 영어 18~24 · 26 · 29~42번
   DAY 1~5 는 gen_h1m2509.py / gen_h1m2509b.py, 32~42번은 gen_h1m2509c.py 로 만든 뒤
   regroup_h1m2509 (assign.js → regroup.js → enrich40.js → write.py) 로 DAY 6~11 을 하루 2문항(지문)씩 다시 묶음.
   이 파일이 이제 원본(평평한 JSON). 고칠 때는 이 파일을 직접 고칠 것.
*/
'''
out='/home/claude/proj/data/h1-mock-2509.js'
write(P,out,head)
open(out,'a').write(tail)
