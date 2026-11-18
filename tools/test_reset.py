# 11/18 시험 리셋: python3 test_reset.py 데이터파일 시험id [시험id …]
# PKG.testReset = [[시험id, 지금 시각(ms)], …] 을 넣음 → 앱(app.js TST)이 그 전에 낸 답을 학생 기기에서 지우고 다시 첫 제출로 받음
# 같은 시험을 또 리셋하면 시각이 새로 바뀜(그 사이 낸 답도 지워짐). WRAPUP-TESTS 블록(시험 문항)은 건드리지 않음
import sys, json, re, subprocess, time
sys.path.insert(0, '/home/claude/srcrepo/generators')
from gencommon import write
import os
path, ids = os.path.abspath(sys.argv[1]), sys.argv[2:]
PK = json.loads(subprocess.check_output(['node', '-e', "global.window={};require(%r);process.stdout.write(JSON.stringify(window.PKG))" % path]))
have = [t['id'] for t in PK.get('tests', [])]
for i in ids: assert i in have, (i, have)
now = int(time.time() * 1000)
R = dict(PK.get('testReset') or [])
for i in ids: R[i] = now
R = [[k, v] for k, v in R.items()]  # gencommon.write가 키를 따옴표 없이 써서 '-' 든 id는 객체 키로 못 씀 → [[id, ms]] 목록
src = open(path, encoding='utf-8').read(); head = src[:src.index('window.PKG')]
tail = src[src.index('/* WRAPUP-TESTS'):] if '/* WRAPUP-TESTS' in src else ''
if tail: PK.pop('tests', None)
PK['testReset'] = R
write(PK, path, head)
if tail: open(path, 'a', encoding='utf-8').write(tail)
print('testReset', R)
