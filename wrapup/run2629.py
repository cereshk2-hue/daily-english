import json, subprocess
src = open('totests.py', encoding='utf-8').read()
src = src.replace("W = '/tmp/claude-0/-home-claude/a9e3e882-1f02-5d62-8f70-aced81bc59d2/scratchpad/wrapup/'", "W = '/home/claude/work/wrapup/'")
exec(src[:src.index("F = D + 'h1-mock-2509.js'")])
F = D + 'h1-mock-2509.js'; O = origin(F)
old = json.loads(subprocess.check_output(['node', '-e', "global.window={};require('%s');console.log(JSON.stringify(window.PKG.tests))" % F]))
old = [t for t in old if t['id'] != 'js2509c']
new = parse('wrapup-2509-2629.html', {'id': 'js2509c', 'title': '9월 학평 26·29번 Wrap-up', 'short': '26·29번', 'school': '중산고 1학년', 'minutes': 30, 'pts': 5}, O)
emit(F, old + [new])
