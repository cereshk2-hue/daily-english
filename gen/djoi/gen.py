# 11/26 대진고2 능률(오선영) 3·4과 본문 '문장 순서 · 문장 삽입' 면밀 학습 세트 (gen/m2doi/gen.py 방식, 고2용)
#  DAY: od3·oi3·od4·oi4 맨 끝 / 시험: dj-oi-3 · dj-oi-4 (20문항씩, 순서 + 삽입, 종이 시험지)
#  순서 DAY = 2문장 조각, 덩이 = 본문 DAY(3과 ❶❷❸/❹❺/❻❼, 4과 ❶❷/❸/❹❺/❻❼), 본문 한 줄도 안 빠짐(소제목은 ': '로 붙음)
#  삽입 = 단서(연결어·지시어·질문↔대답·수치)가 분명해 다른 자리가 안 되는 문장만. 창 6줄(①~⑤)은 되도록 같은 단락 안
import sys, json, re, subprocess, html
sys.path.insert(0, '/home/claude/srcrepo/generators')
from gencommon import write
args = [a for a in sys.argv[1:] if a != 'emit']
path = args[0] if args else '/home/claude/proj/data/h2-ne-oh-L3.js'
PK = json.loads(subprocess.check_output(['node', '-e', "global.window={};require('%s');process.stdout.write(JSON.stringify(window.PKG))" % path]))
D = {d['id']: d for d in PK['days']}
MARK = re.compile(r'^[❶-❿]$')
HEAD = lambda x: not re.search(r'[.!?:]["”’]?$', x.strip())
C = '①②③④⑤'
def unit(k):   # [(단락, en, ko)] 소제목 포함
    out, m = [], None
    for l in D[k]['passage']:
        if l[0] == '#': continue
        if MARK.match(l[1]): m = l[1]; continue
        out.append((m, l[1], l[2]))
    return out
U = {k: unit(k) for k in ('d1', 'd2', 'd3', 'p1', 'p2', 'p3', 'p4')}
B = {k: [x for x in v if not HEAD(x[1])] for k, v in U.items()}   # 소제목 뺀 본문
# ───────── 순서 DAY ─────────
def pairs(s): return [s[i:i + 2] for i in range(0, len(s), 2)]
def join(p, i):
    a = p[0][i]
    for x, y in zip(p, p[1:]): a += (': ' if HEAD(x[1]) else ' ') + y[i]
    return a
def order_day(gid, rng, keys, names):
    items, passage, n = [], [], 0
    for gi, k in enumerate(keys):
        ps = pairs(U[k]); lines = [join(p, 1) for p in ps]; assert len(lines) >= 3 and len(set(lines)) == len(lines)
        items.append({'lines': lines}); n += len(U[k])
        passage.append(['#', '덩이 %d · 본문 %s' % (gi + 1, names[gi]), ''])
        passage += [['', join(p, 1), join(p, 2)] for p in ps]
    return {'id': gid, 'name': '', 'range': rng, 'story': rng + ' · 2줄씩 조각, 본문 %d덩이 (본문 %d줄 전부)' % (len(keys), n), 'passage': passage,
            'steps': [{'type': 'order', 'title': '문장 순서', 'tries': 3,
                       'guide': "본문을 %d덩이로 나눴어요. 덩이마다 우리말 조각을 내용 흐름대로, 다음에 영어 조각을 본문 순서대로 놓아요(한 조각 = 2문장). 연결어(However·So·Therefore)·지시어(this·these·it)·수치를 단서로 쓰세요. 모두 맞혀야 100점, 하나라도 틀리면 0점! 3번 안에 통과 못 하면 오답 학습을 하고 다시 도전해요." % len(keys),
                       'items': items}]}
# ───────── 삽입: (본문 DAY, 문장 첫머리, 단서) ─────────
I3 = [('d1', 'However, there are many situations', "However(그러나) → 앞의 '개인적 선택(personal choices)'과 대비해 '집단으로 결정해야 하는 상황'을 꺼내요. 뒤 Group decision-making이 이 말을 받아요."),
      ('d1', 'Voting is often used', "Group decision-making이 복잡하다(수많은 목소리) → 그래서 투표가 쓰인다, various voting methods. 뒤 these different voting methods의 these가 이 말을 가리켜요."),
      ('d1', 'The following story illustrates', "these different voting methods = 앞 문장의 various voting methods. 다음에 이어질 이야기를 예고하는 ❶의 마지막 문장이에요."),
      ('d1', 'Their three options were', "Their three options = 앞 문장 '돈을 모을 방법'의 세 선택지. conflicting opinions → 뒤 So they decided to put it to a vote."),
      ('d1', 'So they decided to put it to a vote', "So(그래서) → 앞의 conflicting opinions(의견 충돌) 때문에 투표에 부쳐요. it = 결정할 문제."),
      ('d1', 'After doing some research', "Ms. Akers가 '익숙한 방식 말고 다른 것(something different)'을 권함 → 조사 후 세 가지 방식을 써 보기로 해요."),
      ('d1', 'The entire council was curious', "the different methods = 앞 문장의 세 투표 방식(FPTP·AV·Condorcet). 방식을 정한 뒤에야 '결과가 다를까' 궁금할 수 있어요."),
      ('d1', 'For example, if the charity concert', "For example → 앞의 '선호 순서대로 적으라(in order of preference)'는 지시의 예(CBA)."),
      ('d1', 'After every member had voted', "투표 방법 설명(지시·예) 다음 → 모두 투표한 뒤 개표 → 뒤 The results were as follows."),
      ('d2', 'Neither the second nor third preference', "앞 문장 '1순위 표(first-preference votes)를 가장 많이 얻으면 이긴다' → 그래서 2·3순위는 상관없어 무시된다."),
      ('d2', 'This was because it received 8', "This = 앞 문장의 '승자는 C'. 그 이유(8표 vs 5표·7표)가 바로 뒤에 와요."),
      ('d2', 'It is possible to win a vote without', "significant weakness(큰 약점)의 내용 → 뒤 That was the case here(여기서도 그랬다)가 이 문장을 받아요."),
      ('d2', 'However, only 8 out of 20', "However → 앞 문장 '결과는 자선 콘서트'에 반전: 20명 중 8명(40%)만 1순위로 골랐다 = 과반이 아님. ❹의 마지막."),
      ('d2', 'For an option to win in the first round', "앞 문장 '한 번 넘게 집계할 수 있다' → 1라운드 승리 조건(50% 초과) → 뒤 '40%뿐이라 2라운드 필요'."),
      ('d2', 'Therefore, option A was eliminated', "Therefore → 앞 문장 'A가 1순위 표를 가장 적게(5표) 받았다'의 결과로 A 탈락, 5표 재분배."),
      ('d2', 'This meant that option B had 11', "This = 앞 문장 'B에 4표, C에 1표가 더해졌다'. 7+4=11, 8+1=9가 맞아떨어져요."),
      ('d2', 'It sometimes allows second-preference votes', "앞 문장 'AV도 완벽하지 않다(not perfect either)'의 구체적 약점 → 뒤 In this case 제과 판매가 2순위 표 덕에 이김."),
      ('d3', 'In this case, there were three pairs', "앞 문장 '모든 가능한 쌍(each possible pair)을 비교' → 이 경우 세 쌍(A-B, B-C, A-C)."),
      ('d3', 'In other words, 11 people preferred A to B', "In other words → 앞 문장 'A를 B보다 11대 9로 선호'를 투표 조합(ABC·ACB·CAB)으로 풀어 말해요. 뒤 Meanwhile 9명은 B를 선호."),
      ('d3', 'Interestingly, the voters preferred option B to option C', "the same count of 11 to 9 → A-B 비교(11대 9) 설명이 끝난 뒤. 뒤 They also preferred A to C."),
      ('d3', 'As option A, the art show, was preferred', "both of the other options → A가 B(11:9)와 C(11:9) 모두를 이긴 결과가 다 나온 뒤에 승자 선언."),
      ('d3', 'This is especially true in elections', "This = 앞 문장 '승자를 고르지 못할 때가 있다'. 선택지가 많을수록 특히 그렇다."),
      ('d3', 'After a long, intense discussion', "앞 문장 '방식마다 승자가 달랐다' → 그래서 긴 토론 끝에 콩도르세 방식을 택함."),
      ('d3', 'Whichever we choose will have pros and cons', "앞 문장 '어떤 투표 제도도 흠이 없거나 더 우월하지 않다' → 무엇을 고르든 장단점이 있다."),
      ('d3', 'Others continue to develop', "Some people ~ / Others ~ 짝 → '단순하게 하자'는 사람들 다음에 '더 복잡한 방식을 개발하는' 다른 사람들."),
      ('d3', 'When we understand decision-making better', "앞 문장 '의사 결정 과정을 더 잘 이해하게 해 준다' → 더 잘 이해하면 더 나은 결정자가 된다. 글의 마지막.")]
I4 = [('p1', 'Although it still turns on', "앞 문장 '노트북을 떨어뜨려 심하게 손상됨' → 손상의 구체적 모습(화면 깨짐·키 고장). it = her laptop."),
      ('p1', 'Sometimes repairs are expensive', "앞 문장 '수리를 망설인다(hesitating to do so)'의 이유 → 뒤 Besides(게다가) 이유를 하나 더 보태요."),
      ('p1', 'In this case, getting rid of', "In this case = 수리비·시간·5년 된 노트북이라는 이유들 → 새로 사는 게 합리적으로 보인다."),
      ('p1', 'In reality, however, it may not be', "however → 앞의 '새로 사는 게 합리적으로 보일 수 있다'를 뒤집어요. 뒤 '버리면 전자 폐기물 문제에 기여'."),
      ('p1', 'The term refers to discarded', "What exactly is e-waste?(전자 폐기물이 정확히 뭘까?)에 대한 답. The term = e-waste."),
      ('p1', 'To make matters worse', "To make matters worse(설상가상으로) → 앞의 '건강·환경 위험'에 더 나쁜 사실(빠른 증가)을 보태요. 뒤에 증가 수치가 와요."),
      ('p1', 'Experts predict that by 2030', "앞 문장 2021년 수치(2014년 대비 37% 증가) 다음 → 2030년 예측. 16년 = 2014~2030."),
      ('p1', "Let's take a look at some practical", "앞 문장 '문제 해결 노력이 이뤄지고 있다' → 세계 곳곳의 실제 방법을 살펴보자. 단락의 마지막."),
      ('p2', 'For example, a device may be difficult', "For example → 앞 문장 '고치기 너무 어렵다(too difficult to repair)'의 예(분해 어려움·공식 센터)."),
      ('p2', 'The right-to-repair movement is trying', "these problems = 앞의 수리 어려움들(분해·공식 센터·의도적 설계·설명서·부품). 뒤 To protect ~ demands four things."),
      ('p2', 'Second, third parties', "First ~ 다음 Second. 뒤 Third ~로 이어져요."),
      ('p2', 'Advocates of the movement say', "all these goals = 앞의 네 가지 요구(First~Finally). 요구가 다 나온 뒤예요."),
      ('p2', 'This movement is gaining a growing influence in Europe', "as well(~에서도) → 앞 문장 '미국 40개 넘는 주'에 이어 유럽에서도."),
      ('p3', 'Using a score ranging from 0 to 10', "the index = 앞 문장의 'repairability index'. 법안 소개 뒤 지수가 어떻게 작동하는지 설명해요."),
      ('p3', 'Firstly, it allows consumers', "앞 문장 '두 가지 긍정적 효과(two positive effects)' → Firstly 첫째. 뒤 Secondly."),
      ('p3', 'As a result, with fewer electronic', "As a result → 앞 문장 '제조사가 수리하기 쉽게 만들도록 장려' → 매립지로 가는 물건이 줄어 지속 가능한 사회."),
      ('p3', 'We live in a global economy', "앞 문장 '영향이 프랑스를 훨씬 넘어 퍼질 것' → 그 이유: 세계 경제, 프랑스에 팔려면 지수를 붙여야 함."),
      ('p3', 'If the index is successful', "앞의 '프랑스 밖으로 퍼질 이유' 다음 → 성공하면 더 많은 나라가 따를 것. 단락의 마지막."),
      ('p4', 'That is why Repair Cafés were started', "That = 앞 문장 '도구·재료·조언만 있으면 스스로 고칠 수 있다'. 그래서 리페어 카페가 시작됐다."),
      ('p4', 'The cafés are staffed by volunteer experts', "앞 문장 '무료 모임 장소(free meeting places)'를 소개한 뒤 → 누가 일하는지(자원봉사 전문가)."),
      ('p4', 'It was such a success', "It = 앞 문장의 '최초의 리페어 카페(2009 암스테르담)'. 성공 → 이웃 나라로 퍼짐."),
      ('p4', 'Before long, there were Repair Cafés', "앞 문장 '이웃 나라로 곧 퍼졌다' → 머지않아 30개국 넘게."),
      ('p4', 'Furthermore, they foster', "Furthermore(더욱이) → 앞 문장 '기기를 유지하고 수명을 늘리게 해 준다'에 더 큰 효과(지속 가능한 관점)를 보태요."),
      ('p4', 'If that were the case', "that = 앞 문장 '수리가 일상인 세상에 산다면'. 그렇다면 선택지가 비싼 수리·새로 사기에 그치지 않을 것."),
      ('p4', 'Alternatively, she could bring', "Alternatively(아니면) → 앞 문장 '부품을 온라인으로 주문해 직접 교체'의 다른 선택지(리페어 카페)."),
      ('p4', 'Even more importantly', "Even more importantly → 앞 문장 '함께 노력하면 누릴 수 있는 미래'에 더 중요한 점(전자 폐기물 감소)을 보태요. 글의 마지막.")]
CYC = [2, 4, 1, 5, 3, 3, 1, 4, 2, 5]
def ins_items(L, tag, wants=None):
    out = []
    for k, (u, pre, clue) in enumerate(L):
        b = B[u]; idx = [i for i, x in enumerate(b) if x[1].startswith(pre)]; assert len(idx) == 1, pre; idx = idx[0]
        assert idx >= 1, pre
        m = b[idx][0]; lo = min(i for i, x in enumerate(b) if x[0] == m); hi = max(i for i, x in enumerate(b) if x[0] == m) + 1
        want = wants[k] if wants else CYC[k % len(CYC)]
        feas = [p for p in range(1, 6) if idx - p >= 0 and idx - p + 6 <= len(b)]
        inpar = [p for p in feas if idx - p >= lo and idx - p + 6 <= hi]
        p = min(inpar or feas, key=lambda q: (abs(q - want), q)); s = idx - p; win = b[s:s + 6]; assert win[p] == b[idx]
        pv, nx = win[p - 1], (win[p + 1] if p + 1 < 6 else None)
        ex = '정답 ▶ %s\n이유 ▶ %s\n앞 문장 ▶ %s (%s)' % (C[p - 1], clue, pv[1], pv[2])
        ex += ('\n뒤 문장 ▶ %s (%s)' % (nx[1], nx[2])) if nx else '\n뒤 문장 ▶ (창의 마지막)'
        out.append({'lines': [w[1] for w in win], 'given': p, 'ex': ex, 'm': m, 'u': u, 'ko': b[idx][2], 'tag': tag, 'pre': pre, 'cross': not inpar})
    return out
IT3 = ins_items(I3, '3과'); IT4 = ins_items(I4, '4과')
def ins_day(gid, rng, its, keys):
    return {'id': gid, 'name': '', 'range': rng, 'story': rng + ' · 단서가 분명한 문장 %d개 · 6줄 안에서 ①~⑤' % len(its),
            'passage': sum((D[k]['passage'] for k in keys), []),
            'steps': [{'type': 'insert', 'title': '문장 삽입', 'guide': "주어진 문장이 들어갈 곳을 고르세요. 연결어(However·Therefore·In other words·Furthermore)·지시어(this·these·it·that)·질문↔대답·수치(11 vs 9, 40%)가 단서예요. 틀리면 해설의 앞뒤 문장을 꼭 읽어요.",
                       'items': [{'lines': x['lines'], 'given': x['given'], 'ex': x['ex']} for x in its]}]}
# ───────── 시험 순서 문항: (본문 DAY, 단락, 주어진 글 [본문 번호], [정답 순서 조각들], 해설) — 번호는 그 단락의 소제목 뺀 문장 번호 ─────────
O3 = [('d1', '❶', [0], [[1], [2], [3, 4]], "개인적 선택 → However 집단 결정 상황 → 집단 결정은 개인 선택만큼 단순하지 않다 → 그래서 투표, these different voting methods 예고"),
      ('d1', '❷', [0], [[1, 2], [3], [4, 5]], "돈 모을 방법 → 세 선택지·의견 충돌, So 투표 → Ms. Akers '다른 방식(something different)' 권유 → 조사 후 세 방식, the different methods 궁금"),
      ('d1', '❸', [0], [[1], [2], [3, 4]], "선택지마다 글자 → 선호 순서대로 적으라 → For example CBA → 모두 투표 후 개표, 결과"),
      ('d2', '❹', [0, 1], [[2, 3], [4, 5], [6, 7, 8]], "1순위 최다 득표가 승리 → 2·3순위 무시 · 정치 선거에 흔함 → 학생회 결과 C, This was because 8표 → 쉽지만 약점, 과반 없이 이길 수 있다, That was the case here"),
      ('d2', '❺', [0, 1], [[2, 3], [4, 5], [6, 7, 8]], "여러 번 집계 가능 → 1라운드는 50% 초과 · 40%라 2라운드 → A 최소 득표 · Therefore A 탈락 → B에 4표 C에 1표, B 11 vs C 9, 제과 판매 승리"),
      ('d2', '❺', [4, 5], [[6, 7], [8, 9], [10, 11]], "A 탈락·재분배 → 4표·1표 더해짐, This meant B 11 → 제과 판매 승리 · Unfortunately AV도 완벽하지 않다 → 2순위 표가 더 큰 영향, In this case 2순위 덕분"),
      ('d3', '❻', [0, 1, 2], [[3, 4, 5], [6, 7], [8]], "세 쌍 → A>B 11:9 · In other words · Meanwhile 9명 → Interestingly B>C 같은 11:9 · also A>C → both of the other options를 이긴 A가 승자"),
      ('d3', '❼', [0], [[1, 2], [3, 4, 5], [6, 7]], "방식마다 승자가 다름 → 긴 토론 끝 콩도르세 선택·많이 배움 → 이상적 방식 고르기는 어렵다 · 흠 없는 제도 없음 · Whichever 장단점 → Some people 단순하게 / Others 더 복잡하게")]
O4 = [('p1', '❶', [0, 1], [[2, 3], [4, 5], [6, 7]], "노트북 손상 → 수리 망설임 · 비싸고 오래 걸림 → Besides 5년 됨 · In this case 새로 사는 게 합리적? → In reality, however 최선 아님 · 전자 폐기물"),
      ('p1', '❷', [0, 1], [[2, 3], [4, 5], [6, 7]], "e-waste 정의 → 유독 물질·위험 · To make matters worse 증가 → 2021년 수치 · 2030년 예측 → For this reason 노력 · 방법을 살펴보자"),
      ('p2', '❸', [0, 1, 2], [[3, 4], [5, 6], [7, 8, 9, 10]], "고치기 어려움 · For example · 제3자 수리점 불허 → What is more 의도적 설계 · 설명서·부품 못 구함 → these problems 해결하려는 운동 · 네 가지 요구 → First · Second · Third · Finally"),
      ('p2', '❸', [5, 6], [[7, 8], [9, 10], [11, 12]], "네 가지 요구 → First · Second → Third · Finally → all these goals가 이뤄지면 폐기물 감소 · Thanks to their efforts 미국 40개 주"),
      ('p3', '❺', [0], [[1, 2], [3, 4], [5, 6]], "두 가지 효과 → Firstly 소비자 · Secondly 제조사 → As a result 지속 가능한 사회 · however 영향은 프랑스 밖으로 → 세계 경제·프랑스 시장 · 성공하면 다른 나라도"),
      ('p4', '❻', [0, 1], [[2, 3], [4, 5], [6, 7]], "스스로 고칠 수 있다 · That is why 리페어 카페 → 무료 모임 장소 · 자원봉사 전문가 → 2009 암스테르담 최초 · such a success 이웃 나라로 → Before long 30개국 · 기술·지식 나눔"),
      ('p4', '❼', [0, 1], [[2, 3], [4, 5], [6, 7]], "Liz 기억? · 수리가 일상인 세상 상상 → If that were the case 선택지 확대 · 부품 주문 → Alternatively 리페어 카페 · 수리 어렵지 않을 것 → In fact 함께 누릴 미래 · Even more importantly 폐기물 감소")]
OPT = ['(A) - (C) - (B)', '(B) - (A) - (C)', '(B) - (C) - (A)', '(C) - (A) - (B)', '(C) - (B) - (A)']
def E(s): return html.escape(s, quote=False)
def ord_item(o, target, lesson):
    u, m, intro, chunks, clue = o; b = [x for x in B[u] if x[0] == m]
    seq = OPT[target].replace(' ', '').split('-'); lab = {seq[k]: chunks[k] for k in range(3)}
    txt = lambda ix: ' '.join(b[i][1] for i in ix); ko = lambda ix: ' '.join(b[i][2] for i in ix)
    used = sorted(sum(chunks, intro)); assert used == list(range(used[0], used[-1] + 1)), (m, used)
    bodyh = '<div class="wbox"><p>%s</p></div>' % E(txt(intro)) + ''.join('<p>%s %s</p>' % (L, E(txt(lab[L]))) for L in ('(A)', '(B)', '(C)'))
    ex = '정답 ▶ %s %s\n이유 ▶ %s\n주어진 글 ▶ %s\n' % (C[target], OPT[target], clue, ko(intro)) + '\n'.join('%s ▶ %s' % (L, ko(lab[L])) for L in seq)
    ex += '\n포인트 ▶ 연결어(However·Therefore·In other words)·지시어(this·these·it)·수치가 바로 앞 내용과 맞물리는지 확인해요.'
    return {'src': '%s 본문 %s · 글의 순서' % (lesson, m), 'stem': '주어진 글 다음에 이어질 글의 순서로 가장 적절한 것은?', 'body': bodyh, 'opts': OPT[:], 'ans': target, 'ex': ex}
def ins_test(x, lesson):
    g = x['lines'][x['given']]; rest = [l for j, l in enumerate(x['lines']) if j != x['given']]
    bodyh = '<div class="wbox"><p>%s</p></div><p>%s</p>' % (E(g), ' '.join('%s ( %s )' % (E(l), C[j]) for j, l in enumerate(rest)))
    ex = x['ex'] + '\n주어진 문장 해석 ▶ %s\n포인트 ▶ 주어진 문장의 연결어·지시어가 가리키는 말이 바로 앞에, 이어지는 말이 바로 뒤에 오는 곳' % x['ko']
    return {'src': '%s 본문 %s · 문장 삽입' % (lesson, x['m']), 'stem': '글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳은?', 'body': bodyh, 'opts': list(C), 'ans': x['given'] - 1, 'ex': ex}
def test(tid, title, short, items):
    out = [dict(it, n=n, en=True, ctx='', pts=5, words=[], kos=[]) for n, it in enumerate(items, 1)]
    assert len(out) == 20
    return {'id': tid, 'title': title, 'short': short, 'school': '대진고 2학년', 'minutes': 40, 'items': out}
# 시험 삽입 문항 고르기 (첫머리) — 다른 단락 걸친 창은 시험에서 뺌
T3 = ['The entire council was curious', 'So they decided to put it to a vote', 'After doing some research', 'This was because it received 8',
      'It is possible to win a vote without', 'However, only 8 out of 20', 'Therefore, option A was eliminated', 'This meant that option B had 11', 'In other words, 11 people preferred A to B',
      'As option A, the art show, was preferred', 'Whichever we choose will have pros and cons', 'Others continue to develop']
T4 = ['Sometimes repairs are expensive', 'In reality, however, it may not be', 'Experts predict that by 2030', "Let's take a look at some practical", 'The right-to-repair movement is trying',
      'Advocates of the movement say', 'This movement is gaining a growing influence in Europe', 'As a result, with fewer electronic', 'We live in a global economy',
      'It was such a success', 'Furthermore, they foster', 'If that were the case', 'Alternatively, she could bring']
W3 = [5, 2, 4, 1, 2, 5, 1, 1, 3, 3, 3, 4]; W4 = [1, 4, 3, 5, 1, 3, 5, 2, 4, 3, 5, 2, 4]   # 같은 단락 안 가능한 자리로 시험마다 ①~⑤ 4개씩
pick = lambda L, T, W, tag: ins_items([next(x for x in L if x[1] == p) for p in T], tag, W)
s3 = pick(I3, T3, W3, '3과'); s4 = pick(I4, T4, W4, '4과'); assert not any(x['cross'] for x in s3 + s4), [x['pre'] for x in s3 + s4 if x['cross']]
tg3 = [1, 3, 0, 4, 2, 3, 1, 4]; tg4 = [0, 3, 1, 4, 0, 2, 1]
it3 = [ord_item(o, t, '3과') for o, t in zip(O3, tg3)] + [ins_test(x, '3과') for x in s3]
it4 = [ord_item(o, t, '4과') for o, t in zip(O4, tg4)] + [ins_test(x, '4과') for x in s4]
TESTS = [test('dj-oi-3', '순서·삽입 실전 · 능률(오선영) 3과 (투표 방식)', '순서·삽입 3과', it3), test('dj-oi-4', '순서·삽입 실전 · 능률(오선영) 4과 (수리할 권리)', '순서·삽입 4과', it4)]
print('삽입 DAY', len(IT3), len(IT4), '· 창 걸침', [x['pre'][:20] for x in IT3 + IT4 if x['cross']], '· 시험 정답', [''.join(C[i['ans']] for i in t['items']) for t in TESTS])
if 'emit' in sys.argv:
    od3 = order_day('od3', '3과 본문 · 문장 순서', ['d1', 'd2', 'd3'], ['❶❷❸', '❹❺', '❻❼'])
    od4 = order_day('od4', '4과 본문 · 문장 순서', ['p1', 'p2', 'p3', 'p4'], ['❶❷', '❸', '❹❺', '❻❼'])
    oi3 = ins_day('oi3', '3과 본문 · 문장 삽입', IT3, ['d1', 'd2', 'd3']); oi4 = ins_day('oi4', '4과 본문 · 문장 삽입', IT4, ['p1', 'p2', 'p3', 'p4'])
    NEW = ('od3', 'oi3', 'od4', 'oi4')
    PK['days'] = [d for d in PK['days'] if d['id'] not in NEW] + [od3, oi3, od4, oi4]
    for i, d in enumerate(PK['days']): d['name'] = 'DAY %d' % (i + 1)
    src = open(path, encoding='utf-8').read(); head = src[:src.index('window.PKG')]
    tail = src[src.index('/* WRAPUP-TESTS'):]
    if '순서·삽입' not in head: head = head.rstrip('\n') + '\n/* 11/26: 3·4과 본문 순서·삽입 면밀 학습 DAY od3·oi3·od4·oi4 맨 끝 + 시험 dj-oi-3·4 (gen/djoi/gen.py) */\n'
    PK.pop('tests', None)
    write(PK, path, head)
    tail = re.sub(r'/\* DJOI-TESTS.*?/\* /DJOI-TESTS \*/\n?', '', tail, flags=re.S)
    ids = [t['id'] for t in TESTS]
    tail = tail.rstrip('\n') + '\n/* DJOI-TESTS: gen/djoi/gen.py 로 만듦 (손으로 고치지 말 것) */\nwindow.PKG.tests = (window.PKG.tests || []).filter(function (t) { return %s.indexOf(t.id) < 0; }).concat(%s);\n/* /DJOI-TESTS */\n' % (json.dumps(ids), json.dumps(TESTS, ensure_ascii=False))
    open(path, 'a', encoding='utf-8').write(tail)
    print([d['name'] + ' ' + d['range'] for d in PK['days']][-4:], [len(it['lines']) for it in od3['steps'][0]['items']], [len(it['lines']) for it in od4['steps'][0]['items']])
