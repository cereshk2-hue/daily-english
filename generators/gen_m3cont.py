# 11/15 중3 지학사(민찬규) 7·8과 '내용 꿰뚫기' DAY c1~c6 (맨 뒤에 추가)
import sys, json, re, subprocess
sys.path.insert(0, '/tmp/claude-0/-home-claude/a9e3e882-1f02-5d62-8f70-aced81bc59d2/scratchpad')
sys.path.insert(0, '/home/claude/srcrepo/generators')
from gencommon import write
from m3cont_data import GROUPS, TF, KO, NU, SIG
path = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/proj/data/m3-jihak-min-L7.js'
PK = json.loads(subprocess.check_output(['node', '-e', "global.window={};require('%s');process.stdout.write(JSON.stringify(window.PKG))" % path]))
DAY = {d['id']: d for d in PK['days']}
norm = lambda s: s.replace('’', "'").replace('“', '"').replace('”', '"')
days = []
for cid, label, src in GROUPS:
    passage = [r for s in src for r in DAY[s]['passage']]
    text = norm(' '.join(r[1] for r in passage))
    cards = [[w, m] for w, m in SIG[cid]]
    tf = []
    for s, v, why, sig, ev in TF[cid]:
        assert norm(ev) in text, (cid, ev)
        tf.append([s, v, '정답 ▶ %s\n이유: %s' % ('T' if v else 'F', why) + ('\n판정 어휘 ▶ %s' % sig if sig != '-' else ''), None, ev])
    nu = [{'q': '밑줄 친 판정 어휘에 주의해서 알맞은 해석을 고르세요.<br><span class="en">%s</span>' % en, 'opts': [ok] + wr,
           'ex': '정답 ▶ %s\n이유: %s\n오답 ▶ %s\n포인트 ▶ 한글 선택지의 \'~만, 모두, 항상, 거의, 이상/까지\'가 영어의 판정 어휘와 맞는지 꼭 대조하세요.' % (ok, sig, ' / '.join(wr))} for en, ok, wr, sig in NU[cid]]
    ko = []
    for kind, ok, wr, why, pt in KO[cid]:
        ko.append({'box': ['%s · 내용 %s (한글 선택지)' % (label, kind)], 'q': '글의 내용과 <u>일치하지 않는</u> 것은?' if kind == '불일치' else '글의 내용과 <u>일치하는</u> 것은?', 'opts': [ok] + wr,
                   'ex': '정답 ▶ %s\n이유: %s\n오답 ▶ %s\n포인트 ▶ %s' % (ok, why, ' / '.join(wr) + (' → 모두 본문과 일치' if kind == '불일치' else ' → 모두 본문과 다름'), pt)})
    steps = [{'type': 'vocab', 'title': '판정 어휘 카드', 'guide': "always(항상)·sometimes(때때로)·only(~만)·up to(~까지)처럼 한 단어로 내용 일치의 정답이 뒤집히는 말이에요.", 'quizN': len(cards), 'items': cards},
             {'type': 'tf', 'title': '한 단어 차이 T/F', 'guide': '내용은 이미 알고 있죠? 이번엔 판정 어휘 하나 때문에 T/F가 갈려요. 횟수·범위·숫자·시간을 본문과 대조하세요.', 'items': tf},
             {'type': 'mc', 'title': '판정 어휘 해석 고르기', 'guide': '영어 문장의 밑줄 친 말을 정확히 옮긴 한글을 고르세요. 시험의 한글 선택지가 바로 이렇게 갈려요.', 'items': nu},
             {'type': 'mc', 'title': '한글 오지선다 · 내용 일치', 'guide': '실제 시험처럼 한글 선택지예요. 선택지 속 \'~만, 모두, 항상, 이미, 완전히, 이상\'에 동그라미 치는 기분으로 본문과 대조하세요.', 'items': ko}]
    days.append({'id': cid, 'name': '', 'range': '내용 꿰뚫기 · %s' % label, 'story': '%s · 내용 꿰뚫기 (판정 어휘 → 한 단어 차이 T/F → 해석 고르기 → 한글 오지선다)' % label, 'passage': passage, 'steps': steps})
base = [d for d in PK['days'] if not re.match(r'c\d+$', d['id'])]
PK['days'] = base + days
for j, d in enumerate(PK['days']): d['name'] = 'DAY %d' % (j + 1)
src = open(path, encoding='utf-8').read(); head = src[:src.index('window.PKG')]
if '내용 꿰뚫기' not in head: head = head.rstrip('\n') + '\n/* 11/15: 내용 꿰뚫기 DAY c1~c6 (generators/gen_m3cont.py) */\n'
write(PK, path, head)
for d in days: print(d['name'], d['range'], [(s['title'], len(s['items'])) for s in d['steps']])
