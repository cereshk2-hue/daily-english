# 11/9 고1 9월 30~42번 Wrap-up 6개 → 앱 P.tests (기존 js2509a~c 유지, 끝판왕 BOSS 블록은 그대로)
import json, subprocess, sys
src = open('totests.py', encoding='utf-8').read()
src = src.replace("W = '/tmp/claude-0/-home-claude/a9e3e882-1f02-5d62-8f70-aced81bc59d2/scratchpad/wrapup/'", "W = '/home/claude/work/wrapup/'")
src = src.replace(r"""(.*?)</p>', s)}""", r"""(.*?)</p>', s, re.S)}""")
assert 're.S)}' in src
exec(src[:src.index("F = D + 'h1-mock-2509.js'")])
import enrich
TS = [('3031', '30·31번'), ('3233', '32·33번'), ('3435', '34·35번'), ('3637', '36·37번'), ('3839', '38·39번'), ('4042', '40·41~42번')]
for tid, sh in TS:
    enrich.E['js2509-' + tid] = {int(k): v for k, v in json.load(open('en-%s.json' % tid)).items()}
F = D + 'h1-mock-2509.js'; O = origin(F)
old = json.loads(subprocess.check_output(['node', '-e', "global.window={};require('%s');console.log(JSON.stringify(window.PKG.tests))" % F]))
old = [t for t in old if t.get('kind') != 'boss' and not t['id'].startswith('js2509-')]
print('기존:', [t['id'] for t in old])
new = [parse('wrapup-2509-%s.html' % tid, {'id': 'js2509-' + tid, 'title': '9월 학평 %s Wrap-up' % sh, 'short': sh, 'school': '중산고 1학년', 'minutes': 30, 'pts': 5}, O) for tid, sh in TS]
emit(F, old + new)
