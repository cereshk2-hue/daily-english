# 11/10 안곡고2: 9월 학평 40번 시험범위 제외 + 9월 학평 DAY 1~4(두 문항씩)를 번호 하나 = DAY 하나로 (q24 q29 q30 q34 q38 q41), 10월·고3 6월 e1~e10은 그대로
import sys, json, subprocess, re
sys.path.insert(0, '/home/claude/work/gen'); sys.path.insert(0, '/home/claude/srcrepo/generators/split')
from gencommon import write
from split import secs_of, assign, texts
path = '/home/claude/proj/data/h2-mock-2609-angok.js'
P = json.loads(subprocess.check_output(['node', '-e', "global.window={};require('%s');process.stdout.write(JSON.stringify(window.PKG))" % path]))
new, legacy, low = [], {}, []
for d in P['days']:
    if not re.match(r'd\d$', d['id']): continue
    secs = secs_of(d); buckets = {c['label']: [] for c in secs}
    for st in d['steps']:
        per = {c['label']: [] for c in secs}
        for q in st['items']:
            if len(secs) == 1: c, how = secs[0], 'one'
            else: c, how = assign(secs, st, q)
            if how not in ('n', 'g3', 'one'): low.append((d['id'], st['title'], c['label'], how, re.sub(r'<[^>]+>', ' ', str(texts(st, q)[0]))[:90]))
            per[c['label']].append(q)
        for lab, items in per.items():
            if items:
                s2 = dict(st, items=items)
                if st['type'] == 'vocab': s2['quizN'] = min(st.get('quizN', 15), len(items))
                buckets[lab].append(s2)
    rows = {}; cur = None
    for l in d['passage']:
        if l[0] == '#': cur = l[1]; rows[cur] = [l]
        else: rows[cur].append(l)
    ids = []
    for c in secs:
        num = c['num']
        if num == '40': continue          # 시험범위에서 빠짐
        nid = 'q' + num.split('~')[0]; kind = c['label'].split('·', 1)[1].strip()
        new.append({'id': nid, 'name': '', 'range': num + '번', 'story': num + ' ' + kind, 'passage': rows[c['label']], 'steps': buckets[c['label']]}); ids.append(nid)
    legacy[d['id']] = ids
P['days'] = new + [d for d in P['days'] if not re.match(r'd\d$', d['id'])]
for i, d in enumerate(P['days']): d['name'] = 'DAY %d' % (i + 1)
P['legacy'] = {'v': 3, 'map': legacy}
P['unit'] = '24·29·30·34·38·41~42번 + 10월 · 고3 6월 모평'
P['pick'] = True
src = open(path, encoding='utf-8').read(); head = src[:src.index('window.PKG')]
head = head.replace('24·29·30·34·38·40·41~42번', '24·29·30·34·38·41~42번', 1)
head = head.rstrip('\n') + '\n/* 11/10: 9월 40번 시험범위 제외, 9월 학평은 번호 하나 = DAY 하나(q24…q41, DAY 1~6), legacy v3 = 예전 d1~d4 완료 기록을 새 번호로. work/angok3/split1.py */\n'
write(P, path, head)
for x in low: print('LOW', x)
print(json.dumps(legacy)); print([(d['name'], d['range'], len(d['steps']), sum(len(s['items']) for s in d['steps'])) for d in P['days'][:7]])
