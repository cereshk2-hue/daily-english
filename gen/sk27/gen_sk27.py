# 11/13 고3 수능특강 2027 영어 — 유형편 1~20강 (DAY = 강, 19강 2 DAY · 20강 3 DAY)
# DAY = ① 실전 문제(교재로 풀고 OMR에 마킹 — 지문은 교재, 화면은 발문·선택지·번호만) ② 단어 리스트(어려운 어휘만) ③ 단어 테스트(뜻 보고 철자)
# 해설: 정답 ▶ / 소재 / 이유 / 오답 ▶ / 포인트 ▶ / 핵심 문장(해석·구문) / 어휘 ▶ — 정답은 EBS 정답과 해설, 본문 탭 = 영어 지문 + EBS 해석
# 문항 내용(이유·오답·포인트·어휘·핵심 문장)은 sk27/c_LNN.py 의 A[코드] (손으로 씀)
import sys, re, json, glob, html, importlib.util
sys.path.insert(0, '/home/claude/srcrepo/generators')
from gencommon import write
sys.path.insert(0, '/home/claude/srcrepo/gen/sk27'); from structp import parse_struct, split_opts
W = '/home/claude/srcrepo/gen/sk27/'
B = json.load(open(W + 'book_items.json', encoding='utf-8'))
K = json.load(open(W + 'key_items.json', encoding='utf-8'))
CIR = '①②③④⑤'
TITLE = {1: '글의 목적', 2: '심경 변화', 3: '함축적 의미', 4: '요지', 5: '주장', 6: '주제', 7: '제목', 8: '도표', 9: '내용 일치(설명문)', 10: '내용 일치(실용문)',
         11: '어법', 12: '어휘', 13: '빈칸 (1)', 14: '빈칸 (2)', 15: '무관한 문장', 16: '글의 순서', 17: '문장 넣기', 18: '문단 요약', 19: '장문 (1)', 20: '장문 (2)'}
TIP = {1: '글의 목적 · 편지 끝부분의 요청·부탁 표현을 잡기', 2: '심경 변화 · 앞과 뒤의 감정 단서를 따로 찾기', 3: '함축 의미 · 밑줄 앞뒤의 설명으로 비유를 풀기',
       4: '요지 · 주제문과 반복되는 핵심어 찾기', 5: '주장 · should·명령문·필요 표현이 모이는 곳', 6: '주제 · 범위가 너무 넓거나 좁은 선택지 거르기', 7: '제목 · 비유적 제목을 본문 핵심으로 풀기',
       8: '도표 · 숫자·순위·배수 표현을 하나씩 확인', 9: '내용 일치 · 선택지 순서대로 본문 위치 찾기', 10: '내용 일치(안내문) · 항목별로 숫자·조건 확인', 11: '어법 · 동사 자리·수 일치·준동사·관계사',
       12: '어휘 · 반의어로 바꿔 넣어 흐름 확인', 13: '빈칸 · 빈칸 문장이 주제문인지 확인', 14: '빈칸 · 바꿔 쓴(재진술) 표현 찾기', 15: '무관한 문장 · 첫 문장의 주제에서 벗어난 것',
       16: '글의 순서 · 연결어·지시어·관사로 잇기', 17: '문장 넣기 · 흐름이 끊기는 곳 찾기', 18: '요약 · 요약문 핵심어의 재진술 찾기', 19: '장문 · 제목과 어휘(반의어) 확인', 20: '장문 · 순서·지칭·내용 일치'}
SPLIT = {19: [(0, 6), (6, 10)], 20: [(0, 6), (6, 12), (12, 15)]}   # 문항 인덱스 범위 → DAY
def mask(w): return ' '.join(p[0] + '□' * (len(p) - 1) for p in w.split(' '))
def esc(s): return html.escape(s, quote=False)
def clean(s): return re.sub(r'\s+', ' ', s).strip()
GLUE = set(json.load(open(W + 'glue.json', encoding='utf-8')))
def kclean(s):
    """해설(2단) 줄바꿈: 낱말 중간에서 끊긴 줄은 붙이고, 띄어쓰기에서 끊긴 줄은 한 칸 띄움"""
    ls = [l.strip() for l in s.split('\n') if l.strip() and not re.fullmatch(r'(Part|I|II|III|유형편|\d{1,3}|정답과 해설 \d+쪽)', l.strip())]
    out = ''
    for i, l in enumerate(ls):
        out += l
        if i + 1 < len(ls):
            nxt = ls[i + 1]
            out += '' if (''.join(re.findall(r'[가-힣]', l))[-7:] in GLUE and re.match(r'[가-힣]', nxt) and re.search(r'[가-힣]$', l)) else ' '
    return re.sub(r'\s+', ' ', out).strip()

A = {}
for f in sorted(glob.glob(W + 'c_L*.py')):
    sp = importlib.util.spec_from_file_location('c', f); m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); A.update(m.A)

def label(l, i):
    if l == 19: return 'Gateway %02d' % (i + 1) if i < 2 else 'Exercise %02d' % (i - 1)
    if l == 20: return 'Gateway %02d' % (i + 1) if i < 3 else 'Exercise %02d' % (i - 2)
    return 'Gateway' if i == 0 else 'Exercise %02d' % i

def keyrec(l, i):
    """장문은 해설 블록 하나가 문항 여러 개"""
    recs = K['K'][str(l)]
    if l == 19: return recs[0 if i < 2 else 1 + (i - 2) // 2]
    if l == 20: return recs[0 if i < 3 else 1 + (i - 3) // 3]
    return recs[i]

DAYS = []
def build(l):
    ans = K['ANS'][str(l)]; c0 = K['CODE0'][str(l)]
    ranges = SPLIT.get(l, [(0, len(ans))])
    for di, (a, b) in enumerate(ranges):
        items, voc, passage, seen_body = [], [], [], set()
        for i in range(a, b):
            code = c0 + i; bk = B[str(code)]; kr = keyrec(l, i); au = A.get(code)
            if au is None: return False
            ai = CIR.index(ans[i])
            opts = split_opts(bk['opts']) or list(CIR)
            if 'opts' in au: opts = au['opts']
            stem = au.get('stem') or bk['stem']
            q = '<b>%s · %s</b><span class="note" style="display:block;margin-top:4px">교재 %s강 %s — 지문은 교재에서 읽고 답을 고르세요.</span>' % (label(l, i), esc(stem), l, label(l, i))
            wrong = '\n'.join('%s %s' % (CIR[k - 1], t) for k, t in sorted(au['wrong'].items()))
            keys = au.get('keys', [])
            if not keys and au.get('kt'):
                pairs = [(e, re.sub(r'\s*\d\d$', '', kclean(n))) for e, n in parse_struct(kr['struct'])]
                assert len(pairs) == len(au['kt']), (code, len(pairs), len(au['kt']))
                keys = [(e, ko, nt) for (e, nt), ko in zip(pairs, au['kt'])]
            ex = '정답 ▶ %s %s\n소재: %s\n이유: %s\n오답 ▶ %s\n포인트 ▶ %s' % (ans[i], opts[ai] if opts[ai] not in CIR else '', kclean(kr['topic']), au['why'], wrong, au['point'])
            if keys: ex += '\n핵심 문장 ▶\n' + '\n'.join('%d) %s\n   → %s\n   ✎ %s' % (k + 1, e, ko, p) for k, (e, ko, p) in enumerate(keys))
            ex += '\n어휘 ▶ ' + ' · '.join('%s %s' % (w, mm) for w, mm in au['voc'])
            items.append({'n': code, 'q': q, 'opts': opts, 'a': ai, 'keep': True, 'ex': ex})
            for w, mm in au['voc']:
                if w not in [v[0] for v in voc]: voc.append((w, mm, code))
            body = clean(bk['body'])
            if body and body not in seen_body:
                seen_body.add(body)
                passage.append(['#', '%s · %s' % (label(l, i), kclean(kr['topic'])), ''])
                passage.append(['', body, kclean(kr['ko'])])
            for e, ko, p in keys: passage.append(['', e, '%s  ✎ %s' % (ko, p)])
        spell = [v for v in voc if ' ' not in v[0] and re.fullmatch(r'[a-z\-]+', v[0]) and len(v[0]) >= 6]
        step = max(1, len(spell) // 12); spell = spell[::step][:12]
        suf = '' if len(ranges) == 1 else ' (%d/%d)' % (di + 1, len(ranges))
        rng = '%s~%s' % (label(l, a), label(l, b - 1)) if len(ranges) > 1 else ''
        DAYS.append({'id': 'k%02d%s' % (l, 'abc'[di] if len(ranges) > 1 else ''), 'name': 'DAY', 'range': '%02d강 %s%s' % (l, TITLE[l], suf),
                     'story': TIP[l] + ((' · ' + rng) if rng else ''), 'passage': passage, 'steps': [
            {'type': 'mc', 'title': '실전 문제', 'guide': '교재 지문을 시간 재고 풀고, 답만 마킹하세요. 풀고 나면 해설(이유·오답·핵심 문장·어휘)을 꼭 읽어요.', 'items': items},
            {'type': 'vocab', 'title': '단어 리스트', 'guide': '이 강에서 어려운 어휘만 모았어요. 소리 내어 읽고, 퀴즈에서 뜻을 골라요.', 'quizN': min(20, len(voc)), 'items': [[w, m, c] for w, m, c in voc]},
            {'type': 'verb', 'title': '단어 테스트', 'guide': '우리말 뜻을 보고, 첫 글자와 네모칸 수에 맞게 영어로 쓰세요.', 'free': True, 'ph': '영어로 쓰기',
             'items': [{'s': '%s → ___' % m, 'v': mask(w), 'mask': mask(w), 'a': [w], 'ex': '정답 ▶ %s (%s)' % (w, m)} for w, m, c in spell]}]})
    return True

done = [l for l in range(1, 21) if build(l)]
for i, d in enumerate(DAYS): d['name'] = 'DAY %d' % (i + 1)
PK = {'id': 'h3-sk27-eng', 'school': '고3 수능특강', 'unit': '수능특강 2027 영어 · 유형편', 'title': 'EBS Suneung Special 2027', 'titleKo': '고3 수능특강 영어 · 유형편 강별 실전',
      'exam': '수능', 'prose': True, 'pick': True, 'passLock': True, 'noteNeed': 3, 'noteOnly': '단어|어휘|숙어', 'teacherPhone': '', 'days': DAYS}
write(PK, '/home/claude/proj/data/h3-sk27-eng.js', "/* 고3 수능특강 2027 영어 유형편 (11/13, srcrepo/gen/sk27/gen_sk27.py) · DAY = 강\n   실전 문제(교재로 풀고 OMR 마킹, keep/a) → 단어 리스트(어려운 어휘) → 단어 테스트. 본문 탭 = 지문 + EBS 해석 + 핵심 문장 */\n")
print('강', done, 'DAY', len(DAYS), '문항', sum(len(d['steps'][0]['items']) for d in DAYS))
