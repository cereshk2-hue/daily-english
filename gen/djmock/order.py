# 11/26 대진고2 10월 모고 20~24·29~42번 '문장 순서' DAY 18개 (지문 하나 = DAY 하나, om20~om41, 모고 어법·어휘 한 판 gm 뒤)
# 한 문장 = 한 조각, 지문 전체를 우리말 흐름 → 영어 순서로 완성. 3번 도전·0점 규칙은 order 단계(tries 3) 그대로
import sys, json, subprocess
sys.path.insert(0, '/home/claude/srcrepo/generators')
from gencommon import write
path = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/proj/data/h2-ne-oh-L3.js'
PK = json.loads(subprocess.check_output(['node', '-e', "global.window={};require('%s');process.stdout.write(JSON.stringify(window.PKG))" % path]))
D = {d['id']: d for d in PK['days']}
NUMS = ['20', '21', '22', '23', '24', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41~42']
TOPIC = eval(open('/home/claude/srcrepo/gen/djmock/gen.py', encoding='utf-8').read().split('TOPIC = ', 1)[1].split('\nGROUPS')[0])
days = []
for k in NUMS:
    q = D['q' + k.split('~')[0]]; body = [l for l in q['passage'] if l[0] != '#']
    lines = [l[1] for l in body]; assert len(lines) >= 5 and len(set(lines)) == len(lines), k
    days.append({'id': 'om' + k.split('~')[0], 'name': '', 'range': '모의고사 문장 순서 · 10월 %s번' % k,
                 'story': '모의고사 문장 순서 · 10월 모고 %s번 · %s · 문장 %d개 전부 · 지문 하나를 순서대로 완성' % (k, TOPIC[k], len(lines)),
                 'passage': q['passage'],
                 'steps': [{'type': 'order', 'title': '모의고사 문장 순서', 'tries': 3,
                            'guide': "지문 하나를 한 판으로 완성해요(한 조각 = 한 문장, %d문장). 먼저 우리말 조각을 내용 흐름대로, 다음에 영어 조각을 본문 순서대로 놓아요. 연결어(However·Thus·For example)·지시어(this·such·it)·대명사가 단서예요. 모두 맞혀야 100점, 하나라도 틀리면 0점! 3번 안에 통과 못 하면 오답 학습을 하고 다시 도전해요." % len(lines),
                            'items': [{'lines': lines}]}]})
NEW = [d['id'] for d in days]
PK['days'] = [d for d in PK['days'] if d['id'] not in NEW] + days
for i, d in enumerate(PK['days']): d['name'] = 'DAY %d' % (i + 1)
src = open(path, encoding='utf-8').read(); head = src[:src.index('window.PKG')]
tail = src[src.index('/* WRAPUP-TESTS'):]
if '모고 문장 순서' not in head: head = head.rstrip('\n') + '\n/* 11/26: 10월 모고 문장 순서 DAY om20~om41 맨 끝 (gen/djmock/order.py) */\n'
PK.pop('tests', None)
write(PK, path, head)
open(path, 'a', encoding='utf-8').write(tail)
print([(d['name'], d['range'], len(d['steps'][0]['items'][0]['lines'])) for d in days])
