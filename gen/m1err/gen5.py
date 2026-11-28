# 11/28 중산중1 5과 본문 오류 고치기 (선생님 학습지 'Reading 연습 문제 2' 01~25, work_src/m1err/err5.pdf) → m1-donga-yoon-L6 맨 끝 DAY fx5
# 앱 step type 'fixs': 1차 25문장 → 틀린 문장만 3번 더 → 정답·해설. 점수는 1차. 맞는 문장(10·14·17·20·23)은 ○
# 정답 = 교과서 본문(앱 L5a·L5b) 그대로 — assert로 확인
import json, re, subprocess, sys
sys.path.insert(0, '/home/claude/srcrepo/generators')
from gencommon import write
path = '/home/claude/proj/data/m1-donga-yoon-L6.js'
Q = [  # (학습지 문장, 정답(None = 맞는 문장), 해설)
 ("Last Saturday, someone throws a cake at the Monalisa in the Botero Museum in Bogota, Colombia.", "Last Saturday, someone threw a cake at the Monalisa in the Botero Museum in Bogota, Colombia.", "Last Saturday(지난 일) → 과거 threw"),
 ("There was four eyewitnesses.", "There were four eyewitnesses.", "four eyewitnesses(복수) → There were"),
 ("What did they said?", "What did they say?", "did + 동사원형 say"),
 ("Read the following, and found the criminal.", "Read the following, and find the criminal.", "명령문 Read와 나란히 → 동사원형 find"),
 ("I was look at the Monalisa, and someone threw a cake at the painting.", "I was looking at the Monalisa, and someone threw a cake at the painting.", "과거진행형 was + -ing → was looking"),
 ("I turned around and see an old man.", "I turned around and saw an old man.", "turned와 나란히 과거 → saw"),
 ("He was standing on front of a wheelchair.", "He was standing in front of a wheelchair.", "in front of = ~ 앞에"),
 ("I'm about 170 cm tall, and he was a little tall than me.", "I'm about 170 cm tall, and he was a little taller than me.", "than 앞 → 비교급 taller"),
 ("An old man with gray hair was running away, and something falls off his head.", "An old man with gray hair was running away, and something fell off his head.", "지난 일 → 과거 fell"),
 ("It was his wig.", None, "맞는 문장 ○"),
 ("I ran after him, but I couldn't catched him.", "I ran after him, but I couldn't catch him.", "couldn't + 동사원형 catch"),
 ("He was fastest than me.", "He was faster than me.", "than 앞 → 비교급 faster"),
 ("At fact, the old man was not old.", "In fact, the old man was not old.", "in fact = 사실은"),
 ("He was a young man with long brown hair.", None, "맞는 문장 ○"),
 ("I went to the crime scene, and there were piece of cakes all over the painting.", "I went to the crime scene, and there were pieces of cake all over the painting.", "케이크 조각들 = pieces of cake (piece → pieces, cakes → cake)"),
 ("There be also a wheelchair near the painting, and I found a cake box next to the wheelchair.", "There was also a wheelchair near the painting, and I found a cake box next to the wheelchair.", "a wheelchair(단수) + 과거 → There was"),
 ("The box was from Camila's Bakery.", None, "맞는 문장 ○"),
 ("Last Friday, a young man comes in.", "Last Friday, a young man came in.", "Last Friday → 과거 came"),
 ("I spoke to him in Spain, but he didn't understand me.", "I spoke to him in Spanish, but he didn't understand me.", "언어 = Spanish (Spain은 나라 이름)"),
 ("He spoke only English.", None, "맞는 문장 ○"),
 ("We had a lot of different cakes, but he just wanted the small one.", "We had a lot of different cakes, but he just wanted the smallest one.", "많은 케이크 중 가장 작은 것 → 최상급 the smallest"),
 ("We selled only one cake that day, so I remember him clear.", "We sold only one cake that day, so I remember him clearly.", "sell - sold (불규칙), 동사 remember를 꾸밈 → 부사 clearly"),
 ("Oh, he had blue eyes.", None, "맞는 문장 ○"),
 ("Now, looks at the information about the suspects.", "Now, look at the information about the suspects.", "명령문 → 동사원형 look"),
 ("Who the cake threw at the Monalisa?", "Who threw the cake at the Monalisa?", "의문사 Who가 주어 → Who + 동사 + 목적어"),
]
assert len(Q) == 25
PK = json.loads(subprocess.check_output(['node', '-e', "global.window={};require('%s');process.stdout.write(JSON.stringify(window.PKG))" % path]))
D = {d['id']: d for d in PK['days']}
txt = ' '.join(l[1] for k in ('L5a', 'L5b') for l in D[k]['passage'] if l[0] != '#')
for s, a, ex in Q: assert (a or s) in txt, (a or s)
src = open(path, encoding='utf-8').read()
cut = re.search(r'\n/\* [A-Z0-9]+-TESTS', src).start() + 1
head, tail = src[:cut], src[cut:]
head = head[:head.index('window.PKG')]
PK2 = json.loads(subprocess.check_output(['node', '-e', "global.window={};eval(require('fs').readFileSync(0,'utf8'));process.stdout.write(JSON.stringify(window.PKG))"], input=src[:cut].encode()))
day = {'id': 'fx5', 'name': '', 'range': '5과 본문 오류 고치기 (Reading 연습 문제 2)', 'story': '25문장 · 틀린 부분을 모두 고쳐 쓰기, 맞는 문장은 ○ · 틀린 문장만 3번 더',
       'passage': [['#', '5과 본문 · 오류 고치기 — 바른 본문은 다 풀고 나면 해설에 나와요', '']],
       'steps': [{'type': 'fixs', 'title': '5과 본문 오류 고치기', 'guide': '각 문장에서 어법이나 어휘의 쓰임이 틀린 부분을 모두 찾아 바르게 고쳐 쓰세요. 맞는 문장이면 ○를 누르세요.',
                  'items': [{'no': '%02d' % (i + 1), 's': s, 'a': [a] if a else None, 'ex': ex} for i, (s, a, ex) in enumerate(Q)]}]}
PK2['days'] = [d for d in PK2['days'] if d['id'] != 'fx5'] + [day]
for i, d in enumerate(PK2['days']): d['name'] = 'DAY %d' % (i + 1)
if 'gen/m1err' not in head: head = head.rstrip('\n') + '\n/* 11/28: 5과 본문 오류 고치기 DAY fx5 (gen/m1err/gen5.py, step type fixs) */\n'
write(PK2, path, head)
open(path, 'a', encoding='utf-8').write(tail)
print(len(PK2['days']), PK2['days'][-1]['name'])
