# 11/15 중산고1 9월 모고 '내용 꿰뚫기' DAY c1~c11 (YBM 본문 y3 다음, 변형 어휘 v1 앞)
# 판정 어휘 카드 → 한 단어 차이 T/F → 판정 어휘 해석 고르기 → 한글 오지선다(일치·불일치)
import sys, json, re, subprocess
sys.path.insert(0, '/tmp/claude-0/-home-claude/a9e3e882-1f02-5d62-8f70-aced81bc59d2/scratchpad')
sys.path.insert(0, '/home/claude/srcrepo/generators')
from gencommon import write
from js1cont_data import TF, KO, NU, SIG
path = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/proj/data/h1-mock-2509.js'
PK = json.loads(subprocess.check_output(['node', '-e', "global.window={};require('%s');process.stdout.write(JSON.stringify(window.PKG))" % path]))
SENT = {}
for d in PK['days']:
    if not re.match(r'(d\d|q\d)', d['id']): continue
    cur = None
    for r in d['passage']:
        if r[0] == '#':
            m = re.match(r'(\d+(?:·\d+)?(?:~\d+)?)번', r[1]); cur = m.group(1).replace('·', '~') if m else None
            if cur in ('41', '41~42'): cur = '41~42'
            SENT.setdefault(cur, [])
        elif cur and r[1] and not re.match(r'^[❶-❿]$', r[1]) and (r[1], r[2]) not in SENT[cur]: SENT[cur].append((r[1], r[2]))
GROUPS = [('18·19번', ['18', '19']), ('20번', ['20']), ('21·22번', ['21', '22']), ('23·24번', ['23', '24']), ('26·29번', ['26', '29']), ('30·31번', ['30', '31']),
          ('32·33번', ['32', '33']), ('34·35번', ['34', '35']), ('36~38번', ['36', '37', '38']), ('39·40번', ['39', '40']), ('41~42번', ['41~42'])]
ALL = ' '.join(en for v in SENT.values() for en, ko in v).replace('’', "'")
days = []
for i, (label, nums) in enumerate(GROUPS, 1):
    for n in nums: assert SENT.get(n), n
    cards, seen = [], set()
    for n in nums:
        for w, m in SIG[n]:
            if w not in seen: seen.add(w); cards.append([w, m])
    tf = []
    for n in nums:
        for s, v, why, sig, ev in TF[n]:
            assert ev.replace('’', "'") in ALL, ev
            tf.append([s, v, '정답 ▶ %s\n이유: %s\n판정 어휘 ▶ %s' % ('T' if v else 'F', why, sig), int(n.split('~')[0]), ev])
    nu = []
    for n in nums:
        for en, ok, wr, sig in NU[n]:
            nu.append({'q': '밑줄 친 판정 어휘에 주의해서 알맞은 해석을 고르세요. <small>(%s번 내용)</small><br><span class="en">%s</span>' % (n, en), 'opts': [ok] + wr,
                       'ex': '정답 ▶ %s\n이유: %s\n오답 ▶ %s\n포인트 ▶ 한글 선택지에서 \'~만, 모두, 결국, 처음부터, 전혀\' 같은 말이 본문의 판정 어휘와 맞는지 꼭 대조하세요.' % (ok, sig, ' / '.join(wr))})
    ko = []
    for n in nums:
        for kind, ok, wr, why, pt in KO[n]:
            q = '글의 내용과 <u>일치하지 않는</u> 것은?' if kind == '불일치' else '글의 내용과 <u>일치하는</u> 것은?'
            ko.append({'n': int(n.split('~')[0]), 'box': ['%s번 · 내용 %s (한글 선택지)' % (n, kind)], 'q': q, 'opts': [ok] + wr,
                       'ex': '정답 ▶ %s\n이유: %s\n오답 ▶ %s\n포인트 ▶ %s' % (ok, why, ' / '.join(wr) + (' → 모두 본문과 일치' if kind == '불일치' else ' → 모두 본문과 다름'), pt)})
    passage = []
    for n in nums:
        passage.append(['#', '%s번 · 실제 모의고사 원문' % n, ''])
        passage += [['', en, k] for en, k in SENT[n]]
    steps = [{'type': 'vocab', 'title': '판정 어휘 카드', 'guide': "solely(~만), eventually(결국)처럼 한 단어로 내용 일치의 정답이 뒤집히는 말이에요. 뜻을 정확히 익혀 두세요.", 'quizN': len(cards), 'items': cards},
             {'type': 'tf', 'title': '한 단어 차이 T/F', 'guide': '내용은 이미 알고 있죠? 이번엔 판정 어휘 하나 때문에 T/F가 갈려요. 범위(~만, 모두)·시간(전/후, 결국)·정도(거의, 전혀)를 본문과 대조하세요.', 'items': tf},
             {'type': 'mc', 'title': '판정 어휘 해석 고르기', 'guide': '영어 문장의 밑줄 친 말을 정확히 옮긴 한글을 고르세요. 시험의 한글 선택지가 바로 이렇게 갈려요.', 'items': nu},
             {'type': 'mc', 'title': '한글 오지선다 · 내용 일치', 'guide': '실제 시험처럼 한글 선택지예요. 선택지 속 \'~만, 모두, 처음부터, 결국, 전혀, 먼저\'에 동그라미 치는 기분으로 본문과 대조하세요.', 'items': ko}]
    days.append({'id': 'c%d' % i, 'name': '', 'range': '내용 꿰뚫기 %d · %s' % (i, label), 'story': '9월 모고 %s · 내용 꿰뚫기 (판정 어휘 → 한 단어 차이 T/F → 해석 고르기 → 한글 오지선다)' % label, 'passage': passage, 'steps': steps})
base = [d for d in PK['days'] if not re.match(r'c\d+$', d['id'])]
k = next(j for j, d in enumerate(base) if d['id'] == 'v1')
PK['days'] = base[:k] + days + base[k:]
for j, d in enumerate(PK['days']): d['name'] = 'DAY %d' % (j + 1)
src = open(path, encoding='utf-8').read(); head = src[:src.index('window.PKG')]
if '내용 꿰뚫기' not in head: head = head.rstrip('\n') + '\n/* 11/15: 내용 꿰뚫기 DAY c1~c11 (generators/gen_js1cont.py), 변형 어휘 앞 */\n'
write(PK, path, head)
for d in days: print(d['name'], d['range'], [(s['title'], len(s['items'])) for s in d['steps']])
