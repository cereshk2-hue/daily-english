# 11/18 심학중1 천재(소영순)에도 중산중1과 같은 '실전 문법 (접속사 that) 1~3차' OMR (같은 시험지를 나눠 줌)
# 중산중1 m1-donga-yoon-L6 의 m1cs-1~3 를 그대로 복사해 m1-chunjae-so-L6 tests 뒤에 붙임 (학교 이름만 바꿈)
# build_m1c4.py 가 끝에서 이 파일을 부름. run_m1g5.py(중산중1)로 m1cs 를 다시 만들면 이것도 다시 돌릴 것
import json, re, subprocess, copy
D = '/home/claude/proj/data/'
SRC, DST = D + 'm1-donga-yoon-L6.js', D + 'm1-chunjae-so-L6.js'

def load(f):
    return json.loads(subprocess.check_output(['node', '-e', "global.window={};require(%r);process.stdout.write(JSON.stringify(window.PKG))" % f]))

src = [t for t in load(SRC)['tests'] if t['id'].startswith('m1cs-')]
assert [t['id'] for t in src] == ['m1cs-1', 'm1cs-2', 'm1cs-3'], [t['id'] for t in src]
js = open(DST, encoding='utf-8').read()
m = re.search(r'window\.PKG\.tests = (.*?);\n/\* /WRAPUP-TESTS \*/', js, re.S)
tests = [t for t in json.loads(m.group(1)) if not t['id'].startswith('m1cs-')]
for t in src:
    t = copy.deepcopy(t); t['school'] = '심학중 1학년'
    tests.append(t)
js = js[:m.start(1)] + json.dumps(tests, ensure_ascii=False) + js[m.end(1):]
js = js.replace("testLabel: '실전 문제',", "testLabel: '실전 문제 · 실전 문법',", 1)
open(DST, 'w', encoding='utf-8').write(js)
print('m1-chunjae-so-L6 tests:', [(t['id'], t['short']) for t in tests])
