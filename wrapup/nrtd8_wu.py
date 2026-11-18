# 11/18 너른터 실전 8과 1~9회 (중2 동아 윤정미 Lesson 8 · Time Travel / Eckels)
# 원본: 선생님 hwpx 200문항(work/nrt8b → nrtd8_src.json: 문항·선택지·정답지 해설). 전 문항 직접 풀어 검수.
#  - 객관식 173 중 84(74와 같은 문항) 뺌, 62(제목 선택지 둘이 정답 같음)·142(정답 선택지가 맞는 풀이여서 정답 없음) 고침
#  - 주관식 8개(17·23·70·144·150·166·168·190)를 객관식으로 바꿔 180문항 = 20 × 9
#  - 위치형(본문 속 ①~⑤ 밑줄·삽입 자리·밑줄 번호 풀이)은 순서 고정, 나머지는 정답 분포 ①~⑤ 각 4개로 자동 배치
import json, re
from wu_nrtd8 import *
H = ('너른터 실전 8과', '중2 영어 동아(윤정미) Lesson 8', '너른터 실전 8과', 'nrtd8')
NOTICE = '너른터 8과 문제를 검수해서 오류를 고치고, 주관식 일부는 객관식으로 바꿨어요. 답은 아래 OMR에 입력하세요.'
SRC = {'Voca': '어휘', '문법1': '문법', '대화문1': '대화문', '대화문2': '줄거리'}
I = {it['n']: it for it in json.load(open('/home/claude/srcrepo/wrapup/nrtd8_src.json', encoding='utf-8'))}
B = lambda *ls: BOX('<br>'.join(ls))

def tag(it):
    t = re.search(r'\[8-([^\]]+)\]', it['stem']).group(1)
    return SRC.get(t, '본문')
def clean_stem(s):
    s = re.sub(r'\s*\[8-[^\]]+\]\s*', '', s).strip()
    return re.sub(r'^\(주관식\)\s*', '', s)
def lines(body): return [l.rstrip() for l in body.split('\n') if l.strip()]
def ans_of(it): return '①②③④⑤'.index(it['ans'].strip()[0])
def split_ex(raw):
    """정답지 해설 → (본문, [(머리, 내용)]). 맨 앞 정답 번호는 뺌"""
    raw = re.sub(r'^\s*[①②③④⑤]\s*', '', raw).strip()
    parts = re.split(r'\s*\[(오답|수정|풀이|해석|우리말|원문|빈칸원문|지문 변형)\]\s*', raw)
    main, rest = parts[0].strip(), []
    for k in range(1, len(parts) - 1, 2): rest.append((parts[k], parts[k + 1].strip()))
    return main, rest
def build_ex(it, a, flex):
    main, rest = split_ex(it['ans'])
    out = ['이유 ▶ ' + main]
    for h, t in rest:
        if not t: continue
        if h in ('오답', '수정', '풀이'):
            if flex and CIR[a] in t: continue        # 정답지 오답 번호가 어긋난 경우(정답 번호가 섞여 있음) → 뺌
            out.append('오답 ▶ ' + t)
        elif h in ('원문', '빈칸원문'): out.append('원문 ▶ ' + t)
    ex = '\n'.join(out)
    if flex:
        others = [j for j in range(5) if j != a]
        def rep(m):
            j = CIR.index(m.group())
            return '{a}' if j == a else '{%d}' % (others.index(j) + 1)
        ex = re.sub('[①②③④⑤]', rep, ex)
    return ex

POS = {41, 42, 43, 58, 59, 69, 74, 75, 77, 83, 91, 95, 96, 108, 109, 112, 113, 117, 122, 123, 128, 137, 138, 139, 147, 148, 159, 163, 164, 170, 187, 193, 199, 200,
       120, 125, 127, 142, 167, 186}   # 위치형 → 고정
DROP = {84}
FIX = {   # 원본 오류 고침 (선택지 바꿈)
 62: {2: '② Why Travelers Should Leave the Path', 3: '③ A Fun Day of Hunting Dinosaurs'},
 142: {4: '④ stare: to look at someone or something quickly and then look away'},
}
FIXNOTE = {62: '수정 ▶ 원본 선택지 ② Stay on the Path in the Past, ③ Arrival in the Dinosaur Jungle도 글 내용과 맞아 정답이 여럿 → 두 선택지를 바꿈',
           142: '수정 ▶ 원본 ④는 stare의 올바른 풀이(to look at ~ for a long time without moving your eyes away)라 고를 답이 없었음 → glance 뜻 풀이로 바꿈'}

def make(it):
    n = it['n']; st = clean_stem(it['stem']); src_ = tag(it); L = lines(it['body'])
    opts = [re.sub(r'^\s*[①②③④⑤]\s*', '', o) for o in it['opts']]
    if n in FIX:
        for k, v in FIX[n].items(): opts[k - 1] = re.sub(r'^\s*[①②③④⑤]\s*', '', v)
    a = ans_of(it)
    # 본문 모양
    if '주어진 문장이 들어가기' in st:
        body = B(L[0]) + '\n' + B(*L[1:])
    elif '이어질' in st and '순서' in st:
        body = B(L[0]) + '\n' + BOX('<br>'.join(re.sub(r'^\((\w)\)', r'<b>(\1)</b>', l) for l in L[1:]))
    elif '사건을 글의 순서대로' in st:
        ev = [l for l in L if re.match(r'^\([A-D]\)', l)]; ps = [l for l in L if l not in ev]
        body = B(*ps) + '\n' + B(*ev)
    else:
        body = B(*L) if L else ''
    ex = build_ex(it, a, n not in POS)
    if n in FIXNOTE: ex += '\n' + FIXNOTE[n]
    if n in POS:
        return ('fixed', st, src_, body, opts or None, a + 1, ex)
    o = [opts[a]] + [opts[j] for j in range(5) if j != a]
    return ('flex', st, src_, body, o, ex)

# ── 주관식 → 객관식 (직접 씀: 정답이 opts[0]) ──
P2 = I[70]['body'].replace('<u>어떤 경우에도 그 길을 벗어나면 안 됩니다</u>', '<u>(A)</u>').split('[조건]')[0]
CONV = {
 17: ('flex', '다음 문장에서 <u>어색한</u> 부분을 바르게 고친 것은?', '문법', B('My family lived in Pohang since 2020.'),
      ['My family has lived in Pohang since 2020.', 'My family lives in Pohang since 2020.', 'My family was lived in Pohang since 2020.', 'My family has lived in Pohang for 2020.', 'My family lived in Pohang for 2020.'],
      "이유 ▶ since + 과거 시점(2020) = 그때부터 지금까지 계속 → 현재완료 has lived.\n오답 ▶ {1} 현재시제는 since와 쓰지 않음 {2} live는 수동태 ❌ {3}·{4} for 뒤에는 기간(예: for six years)\n포인트 ▶ since + 시점 / for + 기간"),
 23: ('flex', '다음 두 문장을 현재완료를 사용하여 한 문장으로 바르게 바꾼 것은?', '문법', B('He went to Canada. He is not here.'),
      ['He has gone to Canada.', 'He has been to Canada.', 'He has went to Canada.', 'He is gone to Canada since.', 'He has been in Canada before.'],
      "이유 ▶ 캐나다에 가서 지금 여기 없음 = 가 버렸다(결과) → has gone to.\n오답 ▶ {1} has been to = 가 본 적이 있다(경험) {2} 과거분사는 gone {3} 형태 오류 {4} 경험 표현이라 '지금 없다'는 뜻이 아님\n포인트 ▶ have gone to(가고 없다) ↔ have been to(가 본 적 있다)"),
 70: ('flex', '다음 글의 밑줄 친 (A)의 우리말 \'어떤 경우에도 그 길을 벗어나면 안 됩니다\'를 영어로 바르게 옮긴 것은?', '본문', B(*lines(P2)),
      ['You must not leave the path at any time.', 'You must leave not the path at any time.', 'You not must leave the path at any time.', 'You must not leave the path any at time.', 'You must not to leave the path at any time.'],
      "이유 ▶ 주어 You + 금지 must not + 동사원형 leave + 목적어 the path + at any time(어떤 경우에도).\n오답 ▶ {1}·{2} not은 조동사 must 바로 뒤 {3} at any time 어순 {4} 조동사 뒤 to ❌\n원문 ▶ You must not leave it at any time."),
 144: ('flex', '다음 글의 빈칸 (A), (B)에 공통으로 들어갈 말로 가장 알맞은 것은?', '본문', B(*lines(I[144]['body'].split('[보기]')[0])),
      ['anything', 'nothing', 'everything', 'something', 'thing'],
      "이유 ▶ (A) didn't kill anything(아무것도 죽이지 않았다) (B) without saying anything(아무 말 없이) — 부정의 뜻(not, without) 뒤에는 anything.\n오답 ▶ {1} nothing은 그 자체가 부정이라 didn't와 겹침 {2} everything = 모든 것 {3} something은 긍정문 {4} thing은 관사·수식어 필요"),
 150: ('flex', '다음 글의 밑줄 친 우리말 \'내 신발에는 진흙이 조금 있을 뿐이에요\'를 영어로 바르게 옮긴 것은?', '본문', B(*lines(I[150]['body'].split('[조건]')[0])),
      ['There is only a little mud on my shoes.', 'There are only a little mud on my shoes.', 'There is only a few mud on my shoes.', 'There is only little a mud on my shoes.', 'There are only a few muds on my shoes.'],
      "이유 ▶ mud는 셀 수 없는 명사 → There is + a little mud.\n오답 ▶ {1} 셀 수 없는 명사는 단수 동사 is {2} a few는 셀 수 있는 복수 명사 {3} 어순 a little {4} mud는 복수형 없음\n원문 ▶ There’s only a little mud on my shoes."),
 166: ('flex', '다음 글의 빈칸 (A)~(E)에 공통으로 들어갈 말로 가장 알맞은 것은?', '본문', B(*lines(I[166]['body'])),
      ['on', 'in', 'at', 'with', 'for'],
      "이유 ▶ (A) on the wall(벽에) (B) on the news(뉴스에 나오는) (C) What’s going on?(무슨 일이지?) (D)·(E) the mud on his shoes(신발에 묻은 진흙).\n오답 ▶ {1} in the news는 '보도된'의 뜻이 있지만 (A)·(C)·(D)에 맞지 않음 {2}·{3}·{4} 다섯 칸에 모두 들어갈 수 없음"),
 168: ('flex', '다음 글의 밑줄 친 (A), (B)의 우리말을 영어로 바르게 옮긴 것끼리 짝지은 것은?', '본문', B(*lines(I[168]['body'].split('[조건]')[0])),
      ['(A) was confused – (B) got more confused', '(A) was confusing – (B) got more confusing', '(A) confused – (B) got more confused', '(A) was confused – (B) got more confusing', '(A) was confusing – (B) got more confused'],
      "이유 ▶ 사람(Eckels)이 '혼란스러움을 느끼는' 상태 → 과거분사 confused. (A) was confused (B) get + 비교급 → got more confused(더 혼란스러워졌다).\n오답 ▶ confusing은 '혼란스럽게 만드는'(사물·상황) · confused만 쓰면 '혼란스럽게 했다(동사)'가 되어 목적어가 필요"),
 190: ('flex', '다음 글을 읽고 답할 때, 타임머신에 탄 사람은 모두 몇 명인가?', '줄거리', B(*lines(I[185]['body'])),
      ['4명', '2명', '3명', '5명', '6명'],
      "이유 ▶ Eckels + two other travelers(2명) + 여행 안내원 Travis = 모두 4명.\n오답 ▶ {2} 3명은 가이드를 뺀 여행자 수 · 나머지는 근거 없음"),
}
SEC = ['Voca', '문법1', '대화문1', '대화문2', '본문1', '본문2', '본문3', '본문4', '본문5', '본문6']
def sec(n): return re.search(r'\[8-([^\]]+)\]', I[n]['stem']).group(1)
def is_obj(n): return len(I[n]['opts']) == 5 or n in POS
POOL = []
for s in SEC:
    for n in sorted(I):
        if sec(n) != s or n in DROP: continue
        if n in CONV: POOL.append((n, CONV[n]))
        elif '주관식' not in I[n]['stem'] and is_obj(n): POOL.append((n, make(I[n])))
assert len(POOL) == 180, len(POOL)
TITLES = ['어휘 + 문법 (현재완료) ①', '문법 (현재완료) ② + 대화문 · 줄거리', '줄거리 + 본문 ① Time Travel 사무실', '본문 ① 사무실 + 본문 ② 정글 도착', '본문 ② 정글 도착 · 길을 벗어나지 마라',
          '본문 ③ 안개 낀 정글', '본문 ③ + 본문 ④ 티라노사우루스', '본문 ④ 티라노사우루스 + 본문 ⑤ 돌아온 타임머신', '본문 ⑤ + 본문 ⑥ 바뀐 현재']
def chunks():
    """20개씩 나누되, 고정(위치형) 정답이 한 번호에 4개를 넘지 않게 필요하면 이웃 세트와 맞바꿈"""
    sets = [POOL[k * 20:(k + 1) * 20] for k in range(9)]
    def ok(S):
        c = [0] * 5
        for _, it in S:
            if it[0] == 'fixed': c[it[5] - 1] += 1
        return max(c) <= 4
    for k in range(9):
        tries = 0
        while not ok(sets[k]) and tries < 50:
            tries += 1
            c = [0] * 5
            for _, it in sets[k]:
                if it[0] == 'fixed': c[it[5] - 1] += 1
            bad = c.index(max(c))
            j = max(i for i, (_, it) in enumerate(sets[k]) if it[0] == 'fixed' and it[5] - 1 == bad)
            nb = k + 1 if k < 8 else k - 1
            r = next(i for i, (_, it) in enumerate(sets[nb]) if it[0] == 'flex')
            sets[k][j], sets[nb][r] = sets[nb][r], sets[k][j]
        assert ok(sets[k]), k
    return sets
SETS = chunks()
if __name__ == '__main__':
    for k, S in enumerate(SETS, 1):
        T = Test(str(k), '%d회' % k, TITLES[k - 1], '8과', NOTICE, H=H)
        for n, it in S:
            if it[0] == 'flex': T.flex(it[1], it[2], it[3], it[4], it[5], [])
            else: T.fixed(it[1], it[2], it[3], it[4], it[5], it[6], [])
        T.render()
        print('   원문항', [n for n, _ in S])
