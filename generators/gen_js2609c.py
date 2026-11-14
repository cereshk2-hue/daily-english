# 11/13 중산고2 · 2026년 9월 고2 학평 31~42번 — 번호 하나 = DAY 하나 (DAY 6~16)
# 학교 시험에 서술형 없음 → 동사변형·스크램블·오류찾기 빼고, 대의 파악(주제·제목·요지·주장·함축)과 '어휘 비틀기'(바꿔 쓴 말) 중심, 난도 높게
# 실전 문항: 34·38·41~42는 안곡고 데이터, 40은 gen_m2609.py 원문항. 시험지 순서(keep) + 정답 ▶ 형식으로 다시 씀
import sys, html, json, re
G = '/home/claude/srcrepo/generators/'
_src = open(G + 'gen_m2609.py', encoding='utf-8').read()
exec(_src[_src.index('def esc('):_src.index('def ilchi(')])
exec(_src[_src.index('# ───── 실전 문항 원문'):_src.index('# ═════════════ DAY 1')])          # T24…T41, Q34·Q38·Q41, S40, exam(), body() …
_lines = _src.split('\n')
_i = next(i for i, l in enumerate(_lines) if l.startswith("  {'n': 40, 'q': exam(40"))
R40 = eval('\n'.join(_lines[_i:_i + 8]).strip().rstrip(','))
RAG = json.load(open('/home/claude/work/js2d/real_ag.json', encoding='utf-8'))
CIR = '①②③④⑤'

def REAL(it, pos, n=None, why=''):
    """정답이 opts[0]인 문항 → 시험지 번호 pos(0~4) 자리에 정답, 나머지는 원래 차례로 (keep)"""
    o, p = list(it['opts']), list(it.get('per') or [])
    order = list(range(1, 5)); order.insert(pos, 0)
    q = dict(it); q['opts'] = [o[k] for k in order]
    if p: q['per'] = [p[k] for k in order]
    q['keep'] = True; q['a'] = pos
    body_ex = re.sub(r'^정답\s*[①-⑤]?\s*[·:]?\s*', '', it['ex'])
    q['ex'] = '정답 ▶ %s %s\n이유 ▶ %s%s' % (CIR[pos], re.sub(r'^[①-⑤]\s*', '', o[0]), body_ex, ('\n' + why) if why else '')
    if n is not None: q['n'] = n
    return q

def MC(q, opts, ex, per=None):
    d = {'q': q, 'opts': opts, 'ex': ex}
    if per: d['per'] = per
    return d
def BX(t): return '<span class="exam-box en">' + t + '</span>'
def P(T, idx=None): return ' '.join(esc(T[i][0]) for i in (idx if idx is not None else range(len(T))))
def U(T, i, w):   # 지문 전체, i번 문장의 w에 밑줄
    s = [esc(r[0]) for r in T]; assert s[i].count(esc(w)) == 1, w
    s[i] = s[i].replace(esc(w), '<u>' + esc(w) + '</u>'); return ' '.join(s)
def L(T, i): return T[i][0]
def PK(T, i, a, b):  # 어휘 비틀기 pick: 문장 i 속 a를 {a|b}로
    s = T[i][0]; assert s.count(a) == 1, a
    return s.replace(a, '{%s|%s}' % (a, b))
ORD = ['(A) - (C) - (B)', '(B) - (A) - (C)', '(B) - (C) - (A)', '(C) - (A) - (B)', '(C) - (B) - (A)']
def ABC(T, intro, chunks, seq, why):
    lab = dict(zip(seq, chunks))
    b = P(T, intro) + '<br>' + '<br>'.join('(%s) %s' % (L_, P(T, lab[L_])) for L_ in 'ABC')
    ans = ' - '.join('(%s)' % x for x in seq); a = ORD.index(ans)
    return {'q': '<b>주어진 글 다음에 이어질 글의 순서로 가장 적절한 것은?</b>' + BX(b), 'opts': ORD, 'keep': True, 'a': a,
            'ex': '정답 ▶ %s %s\n이유 ▶ %s' % (CIR[a], ans, why)}

GD = {'main': '주제·제목·요지·주장·함축을 묻는 문제예요. 선택지는 본문 표현을 어려운 말로 바꿔 썼어요(어휘 비틀기). 범위가 너무 넓거나 좁은 선택지를 조심하세요.',
      'para': '밑줄 친 말과 뜻이 가장 가까운(바꿔 쓸 수 있는) 것을 고르세요. 시험 선택지에 나오는 바꿔 쓴 표현이에요.',
      'pick': '문맥에 맞는 낱말을 고르세요. 반대말·비슷하게 생긴 말로 비틀어 놓았어요.',
      'tf': '본문 표현을 바꿔 쓴 문장이에요. 내용과 일치하면 T, 다르면 F를 고르세요.',
      'mc': '선택지는 본문을 어려운 어휘로 바꿔 쓴 문장이에요. 풀고 나서 해설의 어휘를 꼭 확인하세요.',
      'abc': '주어진 글 다음에 (A)·(B)·(C)를 순서대로 배열하세요. 연결어·지시어가 열쇠예요.'}

def mk(num, kind, T, real, vocab, main, para, pickv, tf, ilchi, blank, summ, abc, order, insert, odd, pickg):
    label = '%s번 · %s' % (num, kind)
    nn = int(str(num).split('~')[0])
    st = [{'type': 'vocab', 'title': '핵심어휘·숙어', 'quizN': min(15, len(vocab)), 'items': [[w, m, nn] for w, m in vocab]},
          {'type': 'mc', 'title': '실전 문항', 'guide': '시험지 원문항이에요. 지문을 읽고 답을 고르세요.', 'items': real},
          {'type': 'mc', 'title': '대의 파악', 'guide': GD['main'], 'items': main},
          {'type': 'mc', 'title': '어휘 비틀기', 'guide': GD['para'], 'items': para},
          {'type': 'pick', 'title': '어휘선택', 'guide': GD['pick'], 'items': [{'s': s, 'ex': x} for s, x in pickv]},
          {'type': 'tf', 'title': 'T/F 내용 확인', 'guide': GD['tf'], 'items': [[s, b, x, nn, ev] for s, b, x, ev in tf]},
          {'type': 'mc', 'title': '일치·불일치', 'guide': GD['mc'], 'items': [dict(q, box=[label]) for q in ilchi]},
          {'type': 'blank', 'title': '빈칸추론', 'guide': '빈칸에 들어갈 말로 가장 알맞은 것을 고르세요.', 'items': [{'s': s, 'opts': o, 'ex': x} for s, o, x in blank]},
          {'type': 'mc', 'title': '요약문 완성', 'guide': '지문을 읽고 요약문의 빈칸 (A), (B)에 들어갈 말을 고르세요.',
           'items': [{'box': [label], 'q': '다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 알맞은 것은?<br><b>' + s + '</b>', 'opts': o, 'ex': x, 'ev': ev} for s, o, x, ev in summ]},
          {'type': 'mc', 'title': '순서 실전', 'guide': GD['abc'], 'items': abc},
          {'type': 'order', 'title': '문장순서', 'guide': '문장을 본문 순서대로 눌러서 배열하세요.', 'items': [{'lines': [T[i][0] for i in idx], 'flow': f} for idx, f in order]},
          {'type': 'insert', 'title': '문장삽입', 'guide': '주어진 문장이 들어가기에 가장 알맞은 곳을 고르세요.', 'items': [{'lines': [T[i][0] for i in idx], 'given': g, 'ex': x} for idx, g, x in insert]},
          {'type': 'odd', 'title': '어색한 문장', 'guide': '글의 흐름과 관계없는 문장을 고르세요.', 'items': [{'lines': [T[a][0], T[b][0], o, T[c][0]], 'odd': 2, 'ex': x} for (a, b, c), o, x in odd]},
          {'type': 'pick', 'title': '어법선택', 'guide': '어법상 알맞은 것을 고르세요.', 'items': [{'s': s, 'ex': x} for s, x in pickg]}]
    for s in st:
        if s['type'] == 'mc':
            for q in s['items']: q.setdefault('n', nn)
    st = [s for s in st if s['items']]
    return {'num': num, 'label': label, 'kind': kind, 'passage': [['#', label, '']] + [['', a, b] for a, b in T], 'steps': st}

def IL(neg, T, opts, ex, per):
    q = "글의 내용과 일치하지 <u>않는</u> 것은?" if neg else "글의 내용과 <u>일치하는</u> 것은?"
    return {'q': '<b>' + q + '</b>' + BX(P(T)), 'opts': opts, 'ex': ex, 'per': per}
OUT = []

# ═════════════════ 34 빈칸 (전자레인지) ═════════════════
T = T34
OUT.append(mk(34, '빈칸 추론', T,
 real=[REAL(RAG['34번'][0], 2)],
 vocab=[['obvious', '분명한, 뻔한'], ['aspect', '측면'], ['accumulate', '축적되다, 쌓이다'], ['apparent', '뚜렷한, 명백한'], ['subtle', '미묘한'],
        ['medium (pl. media)', '매체'], ['revolutionize', '혁명을 일으키다, 완전히 바꾸다'], ['the better part of', '~의 대부분'], ['fix a meal', '식사를 준비하다'],
        ['shortening', '단축'], ['liberating', '해방감을 주는, 자유롭게 하는'], ['implication', '(예상되는) 영향, 결과'], ['convenience', '편리함'],
        ['overlook', '간과하다'], ['luxury', '사치(품)'], ['occasion', '경우, 특별한 때'], ['anticipate', '예상하다'], ['foresee', '예견하다']],
 main=[
  MC('<b>다음 글의 주제로 가장 적절한 것은?</b>' + BX(P(T)),
     ['unforeseen long-term social effects hidden behind a technology\'s convenience', 'how the microwave oven freed women from all household duties',
      'the gradual disappearance of meals for special occasions', 'reasons why families should reject new kitchen technologies', 'the engineering process behind the invention of the microwave oven'],
     "정답 ▶ unforeseen long-term social effects hidden behind a technology's convenience (기술의 편리함 뒤에 숨은, 예견하지 못한 장기적 사회적 영향)\n이유 ▶ 분명한 측면만 보면 서서히 쌓이는 변화를 놓친다 → 전자레인지의 편리함(단기) 뒤에 가족 저녁 식사가 사라지는 변화(장기) → 예상하지 못했고 예견하기도 어려웠다.\n오답 ▶ 모든 집안일에서 해방(all household duties) → 본문은 요리 시간 단축만, 범위 과장 / 특별한 날 식사 → 오히려 특별한 날에만 남았다는 세부 / 새 기술을 거부하라 → 그런 주장 없음 / 발명 과정 → 언급 없음\n어휘 ▶ unforeseen 예견하지 못한(= not anticipated) · convenience 편리함 · duty 의무, 일",
     [["편리함 뒤의 예견하지 못한 장기적 사회적 영향", "The effects of the microwave oven on family life were not anticipated", "정답"], ["전자레인지가 여성을 모든 집안일에서 해방", "liberating for the cooks in the family", "✘ 요리 시간 단축만 → 과장"],
      ["특별한 날 식사가 점점 사라짐", "except perhaps for special occasions", "✘ 세부이자 사실과 다름"], ["가족은 새 주방 기술을 거부해야", "", "✘ 주장 없음"], ["전자레인지 발명 공학 과정", "", "✘ 언급 없음"]]),
  MC('<b>다음 글의 제목으로 가장 적절한 것은?</b>' + BX(P(T)),
     ['The Quiet Price of Instant Convenience', 'Microwaves: The Secret Recipe for Closer Families', 'Why Cooking Takes Longer Than Ever Before',
      'Accurately Predicting the Future of Kitchen Technology', 'How the 1980s Created Modern Fast Food Chains'],
     "정답 ▶ The Quiet Price of Instant Convenience (즉석 편리함의 조용한 대가)\n이유 ▶ 빠른 조리(instant convenience)라는 눈에 띄는 이점 뒤에, 눈치채지 못한 사이(quiet) 가족 식사가 사라지는 대가(price)를 치렀다.\n오답 ▶ 가족을 더 가깝게 → 반대(함께 식사하는 가족이 줄어듦) / 요리가 더 오래 걸림 → 반대 / 미래를 정확히 예측 → 반대(예견하기 어려웠다) / 패스트푸드 체인 → 언급 없음\n포인트 ▶ 제목의 비유어(price 대가, quiet 조용한=눈에 띄지 않는)를 본문 내용(long-term implications, not apparent)으로 풀어 보세요."),
  MC('<b>다음 글의 요지로 가장 적절한 것은?</b>' + BX(P(T)),
     ['새로운 기술의 눈에 띄는 편리함에 가려, 서서히 나타나는 장기적 변화는 간과되기 쉽다.', '전자레인지는 가족의 식사 문화를 더 풍요롭게 만들었다.',
      '기술의 사회적 영향은 도입되는 즉시 분명하게 드러난다.', '음식 준비 시간이 짧아질수록 가족 간 대화가 늘어난다.', '특별한 날에는 시간이 오래 걸리는 정성 어린 식사를 준비해야 한다.'],
     "정답 ▶ 새로운 기술의 눈에 띄는 편리함에 가려, 서서히 나타나는 장기적 변화는 간과되기 쉽다.\n이유 ▶ 첫 문장(주제문) + the short-term, obvious implications ~ made it easy to overlook the long-term implications\n오답 ▶ 식사 문화가 풍요로워짐 → 반대 / 즉시 드러남 → 반대(not apparent day to day) / 대화가 늘어남 → 근거 없음 / 특별한 날 식사를 준비해야 → 당위 주장 없음\n포인트 ▶ 예시(전자레인지)가 아니라 예시가 증명하는 일반 원리가 요지!"),
  MC('<b>밑줄 친 <u>a luxury of the past</u>가 의미하는 바로 가장 적절한 것은?</b>' + BX(U(T, 8, 'a luxury of the past')),
     ['이제는 일상에서 거의 볼 수 없는 드문 일이 되었다.', '돈이 많이 드는 고급 음식이 되었다.', '과거보다 훨씬 더 자주 먹게 되었다.', '옛날 요리법으로만 만들 수 있게 되었다.', '가족 모두가 함께 준비하는 식사가 되었다.'],
     "정답 ▶ 이제는 일상에서 거의 볼 수 없는 드문 일이 되었다.\n이유 ▶ 함께 저녁을 먹는 가족이 줄어듦 → 오래 걸리는 식사는 특별한 날(special occasions)이 아니면 사라짐 → luxury는 '값비싼 물건'이 아니라 '누리기 힘든 드문 것'.\n오답 ▶ 비싼 고급 음식 → luxury를 글자 그대로 해석한 함정 / 더 자주 → 반대 / 옛날 요리법 → 근거 없음 / 함께 준비 → 근거 없음"),
  MC('<b>글쓴이가 이 글을 통해 궁극적으로 말하고자 하는 바로 가장 적절한 것은?</b>' + BX(P(T)),
     ['We should look beyond the immediate benefits of a technology to its subtle, long-term impacts.', 'We should return to traditional cooking methods to protect family life.',
      'Women should no longer be responsible for preparing family meals.', 'Engineers must predict all social effects before releasing a product.', 'The obvious aspects of media are more important than the hidden ones.'],
     "정답 ▶ We should look beyond the immediate benefits of a technology to its subtle, long-term impacts. (기술의 즉각적 이점 너머 미묘하고 장기적인 영향까지 봐야 한다)\n이유 ▶ 분명한 측면에만 집중하면 서서히 쌓이는 변화를 놓친다는 경고.\n오답 ▶ 전통 조리법으로 돌아가자 → 주장 없음 / 여성의 요리 책임 → 쟁점 아님 / 엔지니어가 모두 예측해야 → 오히려 예견하기 어려웠다고 함 / 분명한 측면이 더 중요 → 반대\n어휘 ▶ immediate 즉각적인 ↔ long-term · subtle 미묘한 = not apparent"),
 ],
 para=[
  MC('<b>밑줄 친 부분과 의미가 가장 가까운 것은?</b>' + BX(U(T, 0, 'not apparent day to day')), ['hard to notice on a daily basis', 'clearly visible every day', 'repeated each day', 'unimportant in daily life', 'impossible to change'],
     "정답 ▶ hard to notice on a daily basis (매일매일은 알아차리기 어려운)\n이유 ▶ apparent = obvious, noticeable(뚜렷한). not apparent day to day = 하루하루는 드러나지 않는\n오답 ▶ clearly visible 반대 / repeated 반복되는 / unimportant 중요하지 않은 → 중요하지 않은 게 아니라 '안 보이는' 것"),
  MC('<b>밑줄 친 부분과 의미가 가장 가까운 것은?</b>' + BX(U(T, 4, 'the better part of')), ['most of', 'the best moment of', 'a small part of', 'the end of', 'the beginning of'],
     "정답 ▶ most of (~의 대부분)\n이유 ▶ the better part of = 대부분. 오후의 '대부분'을 저녁 준비에 썼다\n오답 ▶ better를 '더 좋은'으로 해석한 함정(the best moment) / a small part 반대"),
  MC('<b>밑줄 친 부분과 의미가 가장 가까운 것은?</b>' + BX(U(T, 6, 'overlook')), ['fail to notice', 'look down on', 'watch over', 'examine closely', 'look forward to'],
     "정답 ▶ fail to notice (알아차리지 못하다)\n이유 ▶ overlook = 간과하다. 단기적 편리함 때문에 장기적 영향을 '못 보고 넘어감'\n오답 ▶ look down on 얕보다 / watch over 지켜보다 / examine closely 꼼꼼히 살피다(반대) / look forward to 고대하다\n포인트 ▶ over(넘어서) + look → '보지 않고 넘어가다'"),
  MC('<b>밑줄 친 부분과 의미가 가장 가까운 것은?</b>' + BX(U(T, 9, 'foresee')), ['predict', 'prevent', 'regret', 'remember', 'oversee'],
     "정답 ▶ predict (예측하다)\n이유 ▶ fore(미리) + see = 미리 보다 = 예견하다. 앞의 anticipated(예상된)와 같은 뜻으로 반복\n오답 ▶ prevent 막다 / regret 후회하다 / oversee 감독하다(생김새 함정)"),
 ],
 pickv=[
  (PK(T, 1, 'obvious', 'subtle'), "정답 ▶ obvious (분명한)\n이유 ▶ while missing the more subtle aspects(더 미묘한 측면은 놓치면서) → 우리가 '알아차리는' 것은 분명한 측면. subtle을 넣으면 앞뒤가 같은 말이 돼요."),
  (PK(T, 3, 'revolutionized', 'stagnated'), "정답 ▶ revolutionized (혁명을 일으켰다)\n이유 ▶ 오후 내내 걸리던 요리를 매우 빠르게 → 음식 준비를 '완전히 바꿨다'\n오답 ▶ stagnated 정체되었다(자동사라 목적어도 못 받아요)"),
  (PK(T, 5, 'liberating', 'confining'), "정답 ▶ liberating (해방감을 주는)\n이유 ▶ 준비 시간 단축 → 요리하던 사람들을 '자유롭게' 함\n오답 ▶ confining 가두는, 제한하는(반대)"),
  (PK(T, 6, 'overlook', 'recognize'), "정답 ▶ overlook (간과하다)\n이유 ▶ 단기적 편리함이 장기적 영향을 '못 보게' 만들었다 → 뒤에서 그 영향이 예상되지 않았다고 해요.\n오답 ▶ recognize 인식하다(반대)"),
  (PK(T, 8, 'luxury', 'routine'), "정답 ▶ luxury (사치, 누리기 힘든 것)\n이유 ▶ except perhaps for special occasions(특별한 날 말고는) → 오래 걸리는 식사는 '드문 것'이 됨\n오답 ▶ routine 일상적인 일(반대)"),
  (PK(T, 9, 'anticipated', 'neglected'), "정답 ▶ anticipated (예상된)\n이유 ▶ and would have been difficult to foresee(예견하기도 어려웠을 것) → '예상되지' 않았다와 짝\n오답 ▶ neglected 무시된: 영향이 무시된 게 아니라 아예 내다보지 못한 것"),
 ],
 tf=[
  ("The convenience of the microwave oven was immediately noticeable.", True, "정답 ▶ T\n이유: the short-term, obvious implications of greater convenience → 편리함은 곧바로 눈에 띄었어요.\n어휘 ▶ noticeable 눈에 띄는 = obvious", "the short-term, obvious implications of greater convenience"),
  ("People at the time expected the microwave oven to reduce family dinners.", False, "정답 ▶ F\n이유: 가족생활에 미친 영향은 예상되지 못했어요(not anticipated).", "The effects of the microwave oven on family life were not anticipated"),
  ("Time-consuming meals now tend to be reserved for special occasions.", True, "정답 ▶ T\n이유: 오래 걸리는 식사는 특별한 날을 빼면 과거의 사치가 되었어요.\n어휘 ▶ time-consuming 시간이 많이 걸리는 · be reserved for ~을 위해 남겨 두다", "except perhaps for special occasions"),
  ("Before the microwave, cooking duties were shared equally by all family members.", False, "정답 ▶ F\n이유: 전통적으로 '한 사람'이 오후 내내 준비했고, 그 사람은 대부분 여성이었어요.", "one person spent the better part of an afternoon fixing an evening meal"),
  ("The writer believes the long-term effects of the microwave were easy to predict.", False, "정답 ▶ F\n이유: would have been difficult to foresee(예견하기 어려웠을 것)\n어휘 ▶ predict = foresee", "would have been difficult to foresee"),
 ],
 ilchi=[IL(True, T, ['The microwave oven made family dinners more frequent over time.', 'The microwave oven became common in the early 1980s.', 'Preparing dinner used to take most of an afternoon.',
                      'Most family cooks were women.', 'People tend to miss the less obvious effects of new technologies.'],
  "정답 ▶ The microwave oven made family dinners more frequent over time.\n이유: fewer and fewer families sat down together to eat dinner → 함께하는 저녁은 오히려 '줄었어요'.\n어휘 ▶ frequent 잦은",
  [["전자레인지로 가족 저녁 식사가 점점 잦아졌다", "fewer and fewer families sat down together", "불일치 → 줄어듦"], ["1980년대 초에 도입됨", "introduced in the early 1980s", "일치"],
   ["저녁 준비에 오후 대부분이 걸렸다", "the better part of an afternoon", "일치"], ["가족 요리사 대부분은 여성", "most of whom tended to be women", "일치"], ["덜 분명한 영향을 놓치는 경향", "missing the more subtle aspects", "일치"]])],
 blank=[
  ("But the short-term, obvious implications of greater convenience made it easy to ____ the long-term implications of no longer having one person fix food for the family.", ['overlook', 'calculate', 'celebrate', 'reverse'],
   "정답 ▶ overlook (간과하다)\n이유: 뒤에서 그 영향이 '예상되지 못했다'고 해요 → 단기적 편리함 때문에 장기적 영향을 못 봄"),
  ("The effects of the microwave oven on family life were not ____ and would have been difficult to foresee.", ['anticipated', 'harmful', 'documented', 'permanent'],
   "정답 ▶ anticipated (예상된)\n이유: and 뒤 '예견하기 어려웠을 것'과 같은 방향 → '예상되지 못했다'\n오답 ▶ harmful: 해롭지 않았다는 게 아니라 '예측 못 했다'는 글"),
 ],
 summ=[("The (A) ______ benefits of a new technology can blind us to its (B) ______ effects that build up slowly over time.",
        ['(A) immediate – (B) long-term', '(A) hidden – (B) sudden', '(A) long-term – (B) obvious', '(A) minor – (B) positive', '(A) immediate – (B) temporary'],
        "정답 ▶ (A) immediate – (B) long-term\n(A) 짧은 시간에 분명히 드러나는 편리함 → immediate(즉각적인)\n(B) 시간이 흐르며 쌓이는 가족 식사의 변화 → long-term(장기적인)\n오답 ▶ hidden – sudden: 편리함은 숨겨지지 않았고 변화는 서서히 / temporary(일시적인): 쌓이는 변화와 반대",
        ["the short-term, obvious implications of greater convenience", "the long-term implications"])],
 abc=[ABC(T, [0, 1], [[2, 3, 4, 5], [6, 7, 8], [9]], 'CAB',
  "주어진 글(분명한 측면만 보고 미묘한 변화를 놓친다) → (C) 예: 전자레인지 도입, 오후 내내 걸리던 요리가 빨라져 해방감 → (A) But 단기적 편리함 때문에 장기적 영향을 간과, 함께 먹는 가족이 줄고 긴 식사는 사치가 됨 → (B) 그 영향은 예상되지 못했다(결론).\n포인트 ▶ Take, for example(예시 시작) → But(반전) → 결론")],
 order=[((2, 3, 4, 5), ["예: 전자레인지", "1980년대 초 도입, 음식 준비 혁명", "전통적으로 오후 대부분을 요리에", "이제 빨라져 요리하던 사람을 해방"]),
        ((6, 7, 8, 9), ["단기적 편리함이 장기적 영향을 가림", "함께 저녁 먹는 가족이 줄어듦", "오래 걸리는 식사는 과거의 사치", "그 영향은 예상하지 못했음"])],
 insert=[((4, 5, 6, 7), 2, "정답 ▶ ②\n이유: 요리 시간이 줄어 해방감을 줬다(긍정) → But 단기적 편리함이 장기적 영향을 가렸다(반전) → 함께 먹는 가족이 줄었다. But 앞에는 긍정적 이점이, 뒤에는 그 결과가 와야 해요."),
         ((0, 1, 2, 3), 1, "정답 ▶ ①\n이유: 일반 진술(분명한 측면에 집중하면 변화를 놓친다) → 같은 말을 풀어 쓴 문장(대부분 분명한 측면만 본다) → 예시(Take, for example)")],
 odd=[((5, 6, 7), "Many families today still gather every evening to enjoy long, home-cooked dinners together.",
       "정답 ▶ ③\n이유: 앞뒤는 함께 저녁 먹는 가족이 '줄었다'는 흐름. 오늘날도 매일 저녁 모인다는 문장은 정반대예요.")],
 pickg=[
  (L(T, 0).replace('accumulate', '{accumulate|accumulates}'), "정답 ▶ accumulate\n이유: 관계대명사 that의 선행사 the changes(복수) → 복수 동사"),
  (L(T, 5).replace('most of whom', '{most of whom|most of them}'), "정답 ▶ most of whom\n이유: 콤마 뒤 두 절을 잇는 접속사 역할 → 관계대명사 whom. them을 쓰면 접속사 없이 절이 두 개가 돼요."),
  (L(T, 6).replace('made it easy', '{made it easy|made easy}'), "정답 ▶ made it easy\n이유: make + 가목적어 it + 형용사 + to부정사(진목적어). it 없이 make easy to ~는 안 돼요."),
 ],
))

# ═════════════════ 38 문장 삽입 (혼잡성) ═════════════════
T = T38
OUT.append(mk(38, '문장 삽입', T,
 real=[REAL({**RAG['38번'][0], 'opts': ['③', '①', '②', '④', '⑤']}, 2)],
 vocab=[['make a distinction between', '~ 사이를 구분하다'], ['density', '밀도'], ['crowding', '혼잡(감)'], ['psychological', '심리적인'], ['phenomenon', '현상'],
        ['sensory overload', '감각 과부하'], ['anxiety', '불안'], ['neutral', '중립적인'], ['invariably', '변함없이, 언제나'], ['intensify', '강해지다'],
        ['look forward to', '~을 고대하다'], ['enhance', '높이다, 향상시키다'], ['dread', '두려워하다'], ['setting', '환경, 배경'], ['accentuate', '두드러지게 하다'],
        ['dominant', '지배적인, 우세한'], ['aggressive', '공격적인'], ['conversely', '반대로'], ['pedestrian area', '보행자 구역'], ['defuse', '완화하다']],
 main=[
  MC('<b>다음 글의 주제로 가장 적절한 것은?</b>' + BX(P(T)),
     ['crowding as a factor that magnifies existing moods and behaviors', 'why high density inevitably results in stress and anxiety', 'the difference between urban and rural population density',
      'the psychological benefits of attending crowded concerts', 'scientific methods of measuring physical density accurately'],
     "정답 ▶ crowding as a factor that magnifies existing moods and behaviors (이미 있는 기분과 행동을 증폭시키는 요인으로서의 혼잡)\n이유 ▶ However 이후 핵심: 혼잡은 언제나 나쁜 게 아니라 중립적이며, 밀도가 높아지면 기분·행동이 '강해진다(intensify)'. 기대 → 더 즐겁게 / 두려움 → 더 나쁘게 / 공격적 집단 → 폭력적으로.\n오답 ▶ 필연적으로 스트레스(inevitably) → However 앞의 통념, 필자 입장과 반대 / 도시·시골 비교 → 언급 없음 / 콘서트 이점 → 예시 하나(범위 좁음) / 밀도 측정법 → 언급 없음\n어휘 ▶ magnify 증폭시키다 = intensify, accentuate · inevitably 필연적으로 = invariably"),
  MC('<b>다음 글의 제목으로 가장 적절한 것은?</b>' + BX(P(T)),
     ['Crowds: An Amplifier Rather Than a Villain', 'Escape the Crowd, Escape the Stress', 'Density and Crowding: Two Words, One Meaning',
      'Why Parks Are Disappearing from Our Cities', 'Concerts: The Best Cure for Anxiety'],
     "정답 ▶ Crowds: An Amplifier Rather Than a Villain (혼잡: 악당이 아니라 증폭기)\n이유 ▶ 혼잡을 무조건 나쁜 것(villain)으로 보지 않고, 기분과 행동을 키우는 것(amplifier)으로 본다.\n오답 ▶ 혼잡을 피하면 스트레스도 피한다 → 혼잡 = 무조건 나쁨이라는 통념 / 두 단어 한 의미 → 반대(첫 문장에서 둘을 구분) / 공원이 사라짐 → 공원을 만들자는 내용 / 불안 치료제 → 과장\n포인트 ▶ A rather than B 제목: B(통념)를 부정하고 A(필자 주장)를 내세움."),
  MC('<b>다음 글의 요지로 가장 적절한 것은?</b>' + BX(P(T)),
     ['혼잡은 그 자체로 나쁜 것이 아니라, 사람들이 이미 지닌 기분과 행동을 증폭시킨다.', '밀도가 높아지면 누구나 공격적으로 변한다.', '혼잡은 물리적 밀도와 정확히 같은 개념이다.',
      '도시의 인구 밀도를 낮추는 것만이 긴장을 줄이는 유일한 방법이다.', '공연을 즐기려면 사람이 적은 곳을 골라야 한다.'],
     "정답 ▶ 혼잡은 그 자체로 나쁜 것이 아니라, 사람들이 이미 지닌 기분과 행동을 증폭시킨다.\n이유 ▶ see crowding as neutral rather than invariably negative + moods and behaviors intensify as density increases\n오답 ▶ 누구나 공격적 → '공격적인 집단'만 폭력적으로 / 같은 개념 → 구분함 / 유일한 방법 → 공원·보행 구역을 만드는 방법 제시 / 사람이 적은 곳 → 오히려 기대하면 혼잡이 즐거움을 높임"),
  MC('<b>밑줄 친 <u>crowding may accentuate the dominant behavior</u>가 의미하는 바로 가장 적절한 것은?</b>' + BX(U(T, 5, 'crowding may accentuate the dominant behavior')),
     ['집단에 이미 우세하던 성향이 밀도가 높아지면 더 뚜렷해진다.', '사람이 많아지면 지도자가 집단을 지배하게 된다.', '혼잡하면 사람들이 서로의 행동을 따라 하지 않는다.',
      '사람이 많을수록 공격적인 행동이 줄어든다.', '혼잡한 곳에서는 개인의 행동이 눈에 띄지 않는다.'],
     "정답 ▶ 집단에 이미 우세하던 성향이 밀도가 높아지면 더 뚜렷해진다.\n이유 ▶ 대시(—) 뒤 예: 공격적 집단은 밀도가 높아지면 폭력적으로 변함 → 원래 있던 성향(dominant behavior)이 두드러짐(accentuate)\n오답 ▶ dominant를 '지배하다'로 해석한 함정 / 공격성이 줄어듦 → 반대 / 눈에 띄지 않음 → accentuate(두드러지게 하다)와 반대"),
  MC('<b>글쓴이의 견해와 일치하는 진술로 가장 적절한 것은?</b>' + BX(P(T)),
     ['How crowding affects us depends largely on our state of mind beforehand.', 'Crowding is a purely physical condition unrelated to feelings.', 'Positive spaces in cities make little difference to tension.',
      'High density should be avoided in every situation.', 'Psychologists unanimously regard crowding as harmful.'],
     "정답 ▶ How crowding affects us depends largely on our state of mind beforehand. (혼잡이 우리에게 미치는 영향은 미리 가진 마음 상태에 크게 달려 있다)\n이유 ▶ 기대하면(looking forward to) 즐거움↑, 두려워하면(dreading) 더 나빠짐\n오답 ▶ 순전히 물리적 → 혼잡은 심리적 감정 / 공원은 차이 없음 → 기분을 올리고 긴장 완화 / 모든 상황에서 피해야 → 중립적으로 봄 / 만장일치로 해롭다 → some psychologists는 중립으로 봄\n어휘 ▶ beforehand 미리 · unanimously 만장일치로"),
 ],
 para=[
  MC('<b>밑줄 친 부분과 의미가 가장 가까운 것은?</b>' + BX(U(T, 2, 'invariably')), ['always', 'rarely', 'partly', 'unexpectedly', 'variously'],
     "정답 ▶ always (언제나)\n이유 ▶ in(not) + vary(변하다) + -ably → 변함없이, 언제나\n오답 ▶ variously(여러 가지로)는 생김새 함정 / rarely 드물게(반대)"),
  MC('<b>밑줄 친 부분과 의미가 가장 가까운 것은?</b>' + BX(U(T, 4, 'dreading')), ['fearing', 'expecting eagerly', 'organizing', 'forgetting', 'attending'],
     "정답 ▶ fearing (두려워하는)\n이유 ▶ 앞 문장 looking forward to(고대하다)와 대비 → dread = 두려워하다\n오답 ▶ expecting eagerly는 looking forward to의 뜻(반대)"),
  MC('<b>밑줄 친 부분과 의미가 가장 가까운 것은?</b>' + BX(U(T, 2, 'intensify')), ['grow stronger', 'become stable', 'disappear', 'turn negative', 'calm down'],
     "정답 ▶ grow stronger (더 강해지다)\n이유 ▶ intense(강렬한) + -ify(~하게 되다) → 강해지다. 기대하면 즐거움이 커지고 두려우면 더 나빠지는 '증폭'\n오답 ▶ turn negative: 부정적으로만 변한다는 건 중립적이라는 말과 반대"),
  MC('<b>밑줄 친 부분과 의미가 가장 가까운 것은?</b>' + BX(U(T, 6, 'defuse tension')), ['ease stress', 'spread anger', 'build pressure', 'avoid crowds', 'measure density'],
     "정답 ▶ ease stress (스트레스를 덜다)\n이유 ▶ defuse(폭탄의 뇌관을 빼다 → 완화하다) + tension(긴장). 앞의 lift the general mood와 같은 방향\n오답 ▶ spread(퍼뜨리다)·build(쌓다)는 반대 / diffuse(퍼뜨리다)와 헷갈리지 마세요"),
 ],
 pickv=[
  (PK(T, 0, 'psychological', 'physical'), "정답 ▶ psychological (심리적인)\n이유 ▶ 혼잡(crowding)은 '공간이 충분하지 않다는 느낌(feeling)' → 심리적. 물리적 측정은 밀도(density) 쪽이에요."),
  (PK(T, 2, 'neutral', 'harmful'), "정답 ▶ neutral (중립적인)\n이유 ▶ rather than invariably negative(언제나 부정적인 것이라기보다) → 그와 대비되는 '중립적인'. harmful은 negative와 같은 말이라 대비가 깨져요."),
  (PK(T, 2, 'intensify', 'diminish'), "정답 ▶ intensify (강해지다)\n이유 ▶ 뒤의 예: 기대하면 즐거움 '향상', 두려우면 '훨씬 더' 나빠짐 → 강해짐\n오답 ▶ diminish 줄어들다(반대)"),
  (PK(T, 3, 'enhances', 'spoils'), "정답 ▶ enhances (높인다)\n이유 ▶ 콘서트를 고대하고 있다면 혼잡의 느낌은 즐거움을 '높인다'(기분 증폭)\n오답 ▶ spoils 망친다: 두려워하는 경우(다음 문장)에 해당"),
  (PK(T, 5, 'violent', 'peaceful'), "정답 ▶ violent (폭력적인)\n이유 ▶ 지배적 행동이 두드러짐 → 공격적 집단은 더 '폭력적'으로\n오답 ▶ peaceful 평화로운(반대)"),
  (PK(T, 6, 'defuse', 'heighten'), "정답 ▶ defuse (완화하다)\n이유 ▶ Conversely(반대로) + 긍정적 공간 → 기분을 높이고 긴장을 '완화'\n오답 ▶ heighten 높이다(긴장을 높이면 반대)"),
 ],
 tf=[
  ("Density is an objective measure, whereas crowding is a subjective feeling.", True, "정답 ▶ T\n이유: 밀도 = 물리적 측정(physical measurement), 혼잡 = 심리적 감정(psychological feeling)\n어휘 ▶ objective 객관적인 ↔ subjective 주관적인", "the physical measurement of density ~ and crowding (the psychological feeling"),
  ("All psychologists agree that crowding is invariably harmful.", False, "정답 ▶ F\n이유: some psychologists see crowding as neutral", "some psychologists see crowding as neutral rather than invariably negative"),
  ("A person who is eager to see a performance may enjoy it more in a crowd.", True, "정답 ▶ T\n이유: looking forward to a concert → 혼잡의 느낌이 즐거움을 높임\n어휘 ▶ be eager to ~하기를 몹시 바라다 = look forward to", "the feeling of crowding enhances their enjoyment"),
  ("Parks in dense cities are likely to worsen tension among residents.", False, "정답 ▶ F\n이유: 공원·보행 구역은 기분을 높이고 긴장을 완화(defuse)해요.", "may help to lift the general mood and defuse tension"),
  ("Crowding usually requires a high level of density.", True, "정답 ▶ T\n이유: high density is needed for the phenomenon of crowding", "Usually, high density is needed for the phenomenon of crowding"),
 ],
 ilchi=[IL(False, T, ['Crowding can make an already negative experience even worse.', 'Density refers to the feeling of not having enough space.', 'Crowding always reduces people\'s sense of stress.',
                       'Aggressive groups tend to calm down as density rises.', 'Pedestrian areas are suggested for low-density rural areas.'],
  "정답 ▶ Crowding can make an already negative experience even worse.\n이유: 두려워하는 행사라면 혼잡은 경험을 훨씬 더 나쁘게 만들어요(even worse).",
  [["혼잡은 이미 부정적인 경험을 더 나쁘게", "crowding will make the person's experience of it even worse", "일치"], ["밀도 = 공간이 부족하다는 느낌", "crowding (the psychological feeling of not having enough space)", "불일치 → 그건 혼잡"],
   ["혼잡은 항상 스트레스를 줄임", "rising stress and anxiety", "불일치"], ["공격적 집단은 밀도가 높아지면 진정됨", "an aggressive group may turn violent", "불일치 → 폭력적으로"], ["보행 구역은 저밀도 시골에 제안", "in high-density urban environments", "불일치 → 고밀도 도시"]])],
 blank=[
  ("However, some psychologists see crowding as neutral rather than invariably negative, and believe that people's moods and behaviors ____ as density increases.", ['intensify', 'disappear', 'stabilize', 'reverse'],
   "정답 ▶ intensify (강해지다)\n이유: 뒤 예시 → 기대하면 더 즐겁고, 두려우면 더 나빠짐 = 원래 감정이 '강해짐'\n오답 ▶ reverse(뒤집히다): 기대가 두려움으로 바뀌는 게 아님"),
  ("Put into a community setting, crowding may accentuate the ____ behavior — an aggressive group may turn violent as density rises.", ['dominant', 'opposite', 'polite', 'hidden'],
   "정답 ▶ dominant (지배적인, 우세한)\n이유: 공격적 집단 → 폭력적: 원래 '우세하던' 행동이 두드러짐\n오답 ▶ opposite: 반대 행동이 나오는 게 아님 / hidden: 숨겨진 게 아니라 이미 우세한 것"),
 ],
 summ=[("Rather than being (A) ______ harmful, crowding tends to (B) ______ the feelings and behaviors people already have.",
        ['(A) inherently – (B) magnify', '(A) inherently – (B) suppress', '(A) rarely – (B) replace', '(A) temporarily – (B) ignore', '(A) physically – (B) measure'],
        "정답 ▶ (A) inherently – (B) magnify\n(A) invariably negative(언제나 부정적) → inherently harmful(본질적으로 해로운)\n(B) intensify, enhance, accentuate → magnify(증폭시키다)\n오답 ▶ suppress(억누르다)는 반대 / replace(대체하다): 원래 기분을 바꾸는 게 아니라 키움\n어휘 ▶ inherently 본질적으로",
        ["see crowding as neutral rather than invariably negative", "people's moods and behaviors intensify as density increases"])],
 abc=[ABC(T, [0, 1], [[2, 3, 4], [5], [6]], 'BCA',
  "주어진 글(밀도와 혼잡 구분, 혼잡은 스트레스·불안) → (B) However 혼잡은 중립, 기분·행동이 강해짐: 기대 → 즐거움↑ / 두려움 → 더 나쁨 → (C) 공동체에서는 지배적 행동이 두드러짐: 공격적 집단 → 폭력적 → (A) Conversely 긍정적 공간을 만들면 기분↑·긴장↓.\n포인트 ▶ (A)의 Conversely(반대로)는 부정적 예(폭력) 바로 뒤")],
 order=[((2, 3, 4), ["혼잡은 중립, 밀도가 높으면 기분·행동이 강해짐", "그래서 기대하면 즐거움이 커짐", "두려워하면 더 나빠짐"]),
        ((4, 5, 6), ["두려워하면 더 나빠짐", "공동체에서는 지배적 행동이 두드러짐", "반대로 긍정적 공간은 긴장 완화"])],
 insert=[((4, 5, 6), 2, "정답 ▶ ②\n이유: 공격적 집단이 폭력적으로 변함(부정) → Conversely(반대로) 긍정적 공간이 긴장을 완화. Conversely 앞에는 반대되는 부정적 예가 있어야 해요."),
         ((1, 2, 3), 1, "정답 ▶ ①\n이유: 혼잡은 스트레스·불안을 준다(통념) → However 중립적으로 보는 심리학자도 있다 → So 콘서트 예. However는 통념 바로 뒤에서 방향을 바꿔요.")],
 odd=[((2, 3, 4), "Most concerts today limit the number of tickets to prevent overcrowding.",
       "정답 ▶ ③\n이유: 앞뒤는 '기대하면 즐거움↑, 두려우면 더 나쁨'이라는 기분 증폭의 짝 예시. 콘서트 표 수 제한은 글의 흐름과 관계없어요.")],
 pickg=[
  (L(T, 1).replace('which makes', '{which makes|what makes}'), "정답 ▶ which makes\n이유: 콤마 뒤 계속적 용법 → which. what은 선행사를 품고 있어 앞에 명사(phenomenon)가 있으면 못 써요."),
  (L(T, 1).replace('experience sensory', '{experience|to experience} sensory'), "정답 ▶ experience\n이유: 사역동사 make + 목적어 + 동사원형"),
  (L(T, 6).replace('creating positive', '{creating|create} positive'), "정답 ▶ creating\n이유: 주어 자리(동사는 may help) → 동명사 creating. 동사원형 create는 주어가 될 수 없어요."),
 ],
))

# ═════════════════ 40 요약문 (선행) ═════════════════
T = T40
OUT.append(mk(40, '요약문 완성', T,
 real=[REAL(R40, 0)],
 vocab=[['retain', '유지하다, 간직하다'], ['preference', '선호'], ['perpetuate', '영속시키다, 계속되게 하다'], ['perceive A as B', 'A를 B로 인식하다'], ['deed', '행위'],
        ['accordingly', '그에 맞게'], ['motivate', '동기를 부여하다'], ['subject', '피실험자'], ['donate', '기부하다'], ['charity', '자선 단체'],
        ['earnings', '번 돈, 수입'], ['instruct', '지시하다'], ['recall', '회상하다'], ['take pains to', '공들여 ~하다'], ['respond', '반응하다'],
        ['significantly', '상당히'], ['appearance', '겉모습, 체면'], ['generous', '관대한, 후한'], ['for its own sake', '그 자체를 위해'], ['evident', '분명한'], ['conscious of', '~을 의식하는']],
 main=[
  MC('<b>다음 글의 주제로 가장 적절한 것은?</b>' + BX(P(T)),
     ['how valuing good deeds for their own sake fosters greater generosity', 'why recalling past mistakes makes people donate more', 'the influence of public praise on the success of charities',
      'how college students spend the money they earn from studies', 'the human tendency to exaggerate one\'s own good deeds'],
     "정답 ▶ how valuing good deeds for their own sake fosters greater generosity (선행을 그 자체로 소중히 여기는 것이 어떻게 더 큰 관대함을 키우는가)\n이유 ▶ 자신을 선한 사람으로 보고 행위 자체에 집중한 사람이 더 많이 기부, 겉모습(남의 반응)에 신경 쓴 사람은 덜 관대.\n오답 ▶ 과거 잘못을 떠올리면 더 기부 → 반대(나쁜 행위를 떠올린 쪽이 절반 정도) / 공개적 칭찬 → 오히려 반응을 신경 쓰면 덜 기부 / 학생의 돈 쓰기 → 실험 소재일 뿐 / 과장하는 경향 → 언급 없음\n어휘 ▶ foster 키우다, 촉진하다 · exaggerate 과장하다"),
  MC('<b>다음 글의 제목으로 가장 적절한 것은?</b>' + BX(P(T)),
     ['Do Good for Goodness\' Sake, and You Will Do More', 'Guilt: The Strongest Motive for Giving', 'Applause Makes Us Kinder', 'Why Students Rarely Give to Charity', 'Bad Memories Make Better People'],
     "정답 ▶ Do Good for Goodness' Sake, and You Will Do More (선 그 자체를 위해 선을 행하라, 그러면 더 많이 하게 된다)\n이유 ▶ 선행 그 자체를 위해(for its own sake) 하는 사람이 더 관대했다.\n오답 ▶ 죄책감이 가장 강한 동기 → 나쁜 행위를 떠올린 쪽이 덜 기부 / 박수가 더 친절하게 → 반응에 신경 쓰면 덜 기부(반대) / 학생은 기부를 거의 안 함 → 절반 이상 기부 / 나쁜 기억 → 반대"),
  MC('<b>다음 글의 요지로 가장 적절한 것은?</b>' + BX(P(T)),
     ['자신을 선한 사람으로 인식하고 선행 그 자체에 집중할수록 더 많은 선을 행하게 된다.', '남들의 반응을 의식해야 선행이 오래 지속된다.', '과거의 잘못을 반성하는 것이 기부를 늘리는 가장 좋은 방법이다.',
      '보수를 받는 실험의 결과는 믿기 어렵다.', '선행이 주변에 미친 영향을 기록하면 관대함이 커진다.'],
     "정답 ▶ 자신을 선한 사람으로 인식하고 선행 그 자체에 집중할수록 더 많은 선을 행하게 된다.\n이유 ▶ 첫 두 문장(주제문) + 마지막 문장(In other words 정리)\n오답 ▶ 남의 반응 의식 → 반대 / 잘못 반성 → 반대 / 실험 신뢰성 → 언급 없음 / 영향을 기록 → 선행의 '영향'까지 묘사한 쪽이 덜 기부(반대)"),
  MC('<b>밑줄 친 <u>for its own sake</u>가 의미하는 바로 가장 적절한 것은?</b>' + BX(U(T, 4, 'for its own sake')),
     ['보상이나 남의 평가 때문이 아니라 선행 그 자체가 좋아서', '자기 자신에게 이익이 돌아오기 때문에', '다른 사람에게 좋은 인상을 주기 위해', '연구에서 돈을 받았기 때문에', '과거의 잘못을 갚기 위해'],
     "정답 ▶ 보상이나 남의 평가 때문이 아니라 선행 그 자체가 좋아서\n이유 ▶ its = doing good. 겉모습(남의 반응, 영향)에 신경 쓰는 사람과 대비\n오답 ▶ own을 '자기 자신(이익)'으로 해석한 함정 / 좋은 인상 → appearances 쪽 / 돈·잘못 → 근거 없음"),
  MC('<b>윗글에서 추론할 수 있는 것으로 가장 적절한 것은?</b>' + BX(P(T)),
     ['Those who care how their kindness looks to others may end up giving less.', 'Recalling bad deeds doubles people\'s willingness to donate.', 'Focusing on others\' reactions is the key to generosity.',
      'Paying participants made the study results unreliable.', 'People forget their good deeds more easily than bad ones.'],
     "정답 ▶ Those who care how their kindness looks to others may end up giving less. (자신의 친절이 남에게 어떻게 보이는지 신경 쓰는 사람은 결국 덜 줄 수도 있다)\n이유 ▶ people who seemed concerned about appearances ~ were less generous\n오답 ▶ 나쁜 행위 → 두 배가 되는 건 좋은 행위 쪽 / 남의 반응이 열쇠 → 반대 / 실험 신뢰성·기억 → 언급 없음\n어휘 ▶ end up -ing 결국 ~하게 되다"),
 ],
 para=[
  MC('<b>밑줄 친 부분과 의미가 가장 가까운 것은?</b>' + BX(U(T, 0, 'perpetuating')), ['continuing', 'questioning', 'pretending', 'punishing', 'interrupting'],
     "정답 ▶ continuing (계속하는)\n이유 ▶ perpetuate = 영속시키다, 계속되게 하다. 성인의 뇌는 선한 행동을 '이어 가는' 것을 선호\n오답 ▶ pretending(~인 척하다)과 헷갈리지 마세요 / interrupting 중단시키다(반대)"),
  MC('<b>밑줄 친 부분과 의미가 가장 가까운 것은?</b>' + BX(U(T, 3, 'taken pains')), ['made a great effort', 'felt physical pain', 'refused politely', 'taken a short break', 'complained bitterly'],
     "정답 ▶ made a great effort (크게 애썼다)\n이유 ▶ take pains to ~ = 공들여 ~하다. 친절했던 일과 사람들의 반응까지 '공들여' 묘사\n오답 ▶ pain을 '아픔'으로 해석한 함정"),
  MC('<b>밑줄 친 부분과 의미가 가장 가까운 것은?</b>' + BX(U(T, 4, 'generous')), ['willing to give freely', 'eager to be praised', 'careful with money', 'quick to judge', 'worried about others'],
     "정답 ▶ willing to give freely (기꺼이 아낌없이 주는)\n이유 ▶ generous = 관대한, 후한 → 기부를 더 많이 하는\n오답 ▶ careful with money(돈을 아끼는)는 반대 / eager to be praised는 겉모습에 신경 쓰는 쪽"),
  MC('<b>밑줄 친 부분과 의미가 가장 가까운 것은?</b>' + BX(U(T, 1, 'accordingly')), ['in a way that matches', 'by accident', 'against one\'s will', 'in secret', 'at the same time'],
     "정답 ▶ in a way that matches (그에 맞는 방식으로)\n이유 ▶ 자신을 선한 사람으로 인식하고 '그에 맞게' 행동하는 것\n오답 ▶ according to(~에 따르면)와 연결되는 뜻: '그에 따라' → 맞춰서"),
 ],
 pickv=[
  (PK(T, 0, 'retain', 'abandon'), "정답 ▶ retain (유지하다)\n이유 ▶ 성인의 뇌는 선한 행동을 이어 가려는 선호를 '간직한다' → 그래서 선행이 더 큰 선행으로 이어짐\n오답 ▶ abandon 버리다(반대)"),
  (PK(T, 1, 'motivates', 'discourages'), "정답 ▶ motivates (동기를 부여한다)\n이유 ▶ 선한 사람으로 자신을 보는 것 → 미래에 더 큰 선을 행하도록 '동기 부여'\n오답 ▶ discourages 단념시킨다(반대)"),
  (L(T, 2).replace('previous bad deeds', 'previous {bad|good} deeds'), "정답 ▶ bad\n이유 ▶ 좋은 행위를 적은 사람이 '나쁜' 행위를 떠올린 사람보다 거의 두 배를 기부. 비교 대상이 같으면 비교가 성립하지 않아요."),
  (L(T, 3).replace('significantly less', 'significantly {less|more}'), "정답 ▶ less\n이유 ▶ 남의 반응까지 공들여 묘사(겉모습에 신경) → '덜' 기부. 다음 문장 were less generous로 다시 확인돼요."),
  (PK(T, 4, 'appearances', 'principles'), "정답 ▶ appearances (겉모습, 남에게 보이는 것)\n이유 ▶ 괄호 속 설명: 행위 자체만큼 그 영향(impact)에 신경 → 겉으로 보이는 것\n오답 ▶ principles 원칙: 원칙에 신경 쓰는 건 오히려 '그 자체를 위해' 쪽"),
 ],
 tf=[
  ("Reminding ourselves of our good deeds tends to encourage further kindness.", True, "정답 ▶ T\n이유: 과거 선행을 적은 사람이 더 많이 기부\n어휘 ▶ further 더 이상의, 추가의", "subjects who wrote down a list of past good deeds"),
  ("Students who listed bad deeds donated about twice as much as the others.", False, "정답 ▶ F\n이유: 두 배 가까이 기부한 쪽은 좋은 행위를 적은 학생들", "almost twice as much as those who had been instructed to recall previous bad deeds"),
  ("The participants received money for taking part in the study.", True, "정답 ▶ T\n이유: paid study + the earnings they'd made from the study", "In one paid study of one hundred college students"),
  ("Describing others' grateful reactions increased the amount people donated.", False, "정답 ▶ F\n이유: 사람들의 반응까지 묘사한 쪽은 상당히 '덜' 기부", "were likely to donate significantly less"),
  ("People who focused purely on the act of kindness itself were more generous.", True, "정답 ▶ T\n이유: those who focused purely on the actions themselves가 더 많이 기부", "those who focused purely on the actions themselves"),
 ],
 ilchi=[IL(True, T, ['The study involved several thousand adult volunteers.', 'Our brains tend to prefer continuing good behavior.', 'Subjects listing good deeds gave over half their earnings on average.',
                      'Some subjects described how people reacted to their kindness.', 'Concern for appearances was linked to less generosity.'],
  "정답 ▶ The study involved several thousand adult volunteers.\n이유: one hundred college students(대학생 100명)",
  [["수천 명의 성인 자원봉사자", "one hundred college students", "불일치 → 대학생 100명"], ["선한 행동을 이어 가길 선호", "retain a preference for perpetuating good, fair behavior", "일치"],
   ["평균적으로 번 돈의 절반 이상 기부", "over half the earnings they'd made", "일치"], ["반응을 묘사한 피실험자들", "how people responded", "일치"], ["겉모습을 신경 쓰면 덜 관대", "were less generous", "일치"]])],
 blank=[
  ("Simply perceiving ourselves as people who do good deeds and behaving accordingly ____ us to do greater good in the future.", ['motivates', 'forbids', 'tires', 'confuses'],
   "정답 ▶ motivates (동기를 부여하다)\n이유: 뒤 실험에서 좋은 행위를 떠올린 쪽이 더 많이 기부 → 더 큰 선을 하도록 '동기 부여'"),
  ("In other words, people who seemed concerned about ____ (e.g., the impact of their good deed, as much as the deed itself) were less generous than those who cared more about doing good for its own sake.", ['appearances', 'fairness', 'the poor', 'their health'],
   "정답 ▶ appearances (겉모습)\n이유: 앞 문장의 '사람들이 어떻게 반응했는지까지 묘사'를 다시 말함 → 남에게 보이는 겉모습\n오답 ▶ the poor: 가난한 사람을 걱정하면 더 기부할 것"),
 ],
 summ=[("Seeing ourselves as (A) ______ people and focusing on the deed (B) ______, rather than on how others react, makes us more generous.",
        ['(A) good – (B) itself', '(A) good – (B) publicly', '(A) guilty – (B) itself', '(A) popular – (B) quickly', '(A) wealthy – (B) alone'],
        "정답 ▶ (A) good – (B) itself\n(A) perceiving ourselves as people who do good deeds → good\n(B) focused purely on the actions themselves → the deed itself\n오답 ▶ publicly(공개적으로)는 겉모습 쪽 / guilty(죄책감 있는)는 나쁜 행위를 떠올린 쪽",
        ["perceiving ourselves as people who do good deeds", "focused purely on the actions themselves"])],
 abc=[ABC(T, [0], [[1], [2], [3, 4]], 'BAC',
  "주어진 글(성인의 뇌는 선한 행동을 이어 가길 선호) → (B) 자신을 선한 사람으로 보면 더 큰 선행 동기 → (A) 실험 1: 좋은 행위를 적은 학생이 거의 두 배 기부 → (C) In addition 실험 2: 반응까지 묘사한 사람은 덜 기부 + In other words 정리.\n포인트 ▶ In addition(추가)·In other words(정리)는 뒤쪽에 와요.")],
 order=[((1, 2, 3, 4), ["선한 사람으로 자신을 보면 더 큰 선행 동기", "실험: 좋은 행위를 적은 학생이 더 기부", "In addition 반응까지 묘사하면 덜 기부", "In other words 겉모습에 신경 쓰면 덜 관대"])],
 insert=[((1, 2, 3), 2, "정답 ▶ ②\n이유: 실험 1(좋은 행위 vs 나쁜 행위) → In addition 실험 2(반응까지 묘사한 사람은 덜 기부). In addition은 첫 실험 결과 뒤에 와요."),
         ((2, 3, 4), 2, "정답 ▶ ②\n이유: In other words(다시 말해)는 바로 앞 실험 2 결과(반응을 묘사하면 덜 기부)를 일반화해요.")],
 odd=[((1, 2, 3), "Most charities prefer donations from large companies rather than from students.",
       "정답 ▶ ③\n이유: 앞뒤는 피실험자의 기부 실험 결과. 자선 단체가 기업 기부를 선호한다는 문장은 흐름과 관계없어요.")],
 pickg=[
  (L(T, 1).replace('motivates', '{motivates|motivate}'), "정답 ▶ motivates\n이유: 주어는 동명사구(Simply perceiving ~ and behaving accordingly) → 하나의 일로 보아 단수 동사"),
  (L(T, 2).replace('who wrote down', '{who wrote down|who writing down}'), "정답 ▶ who wrote down\n이유: 관계대명사 who 뒤에는 동사가 와야 해요(and were then asked와 병렬)."),
  (L(T, 4).replace('were less generous', '{were|was} less generous'), "정답 ▶ were\n이유: 주어 people(복수). 중간의 who절과 괄호는 수식어예요."),
 ],
))

# ═════════════════ 41~42 장문 (알고리즘과 주체성) ═════════════════
T = T41
OUT.append(mk('41~42', '장문 (제목·어휘)', T,
 real=[REAL(RAG['41~42번'][0], 0, n=41), REAL(RAG['41~42번'][1], 3, n=42)],
 vocab=[['choice architecture', '선택 설계(구조)'], ['popularize', '대중화하다'], ['behavioral economics', '행동 경제학'], ['in essence', '본질적으로'], ['sophisticated', '정교한'],
        ['architect', '설계자'], ['curate', '선별하다, 큐레이션하다'], ['subtly', '미묘하게'], ['nudge', '(슬쩍) 유도하다'], ['beneficial', '유익한'],
        ['manipulation', '조작'], ['underlying', '근본적인, 밑에 깔린'], ['objective', '목표; 객관적인'], ['be aligned with', '~와 일치하다'], ['well-being', '행복, 복지'],
        ['autonomy', '자율성'], ['cultivate', '기르다'], ['agency', '주체성, 행위 능력'], ['conscious', '의식적인'], ['engagement', '관계 맺기, 관여'],
        ['seek out', '찾아내다'], ['perspective', '관점'], ['deliberate', '의도적인, 신중한'], ['go against the grain', '흐름(통념)을 거스르다'],
        ['skepticism', '회의론, 의심'], ['seemingly', '겉보기에'], ['output', '결과물'], ['reflection', '반영'], ['prescription', '처방'], ['flourishing', '번영']],
 main=[
  MC('<b>윗글의 주제로 가장 적절한 것은?</b>' + BX(P(T)),
     ['the need to consciously guard human agency against algorithmic nudges', 'how algorithms make human decisions more objective', 'the historical development of behavioral economics',
      'ways to design healthier digital habits through nudges', 'why people should stop using recommendation systems entirely'],
     "정답 ▶ the need to consciously guard human agency against algorithmic nudges (알고리즘의 유도에 맞서 인간의 주체성을 의식적으로 지켜야 할 필요성)\n이유 ▶ 알고리즘 = 선택을 유도하는 설계자, 조작 가능성 → 질문: 주체성을 어떻게 지킬까? → 답: 의식적 노력, 비판적 관계, 건전한 회의론\n오답 ▶ 더 객관적으로 → 겉보기에만 객관적(seemingly objective) / 행동 경제학의 역사 → 도입 소재 / 건강한 습관 → 넛지의 장점 예시일 뿐 / 완전히 그만 써라 → 과장(비판적으로 쓰라는 것)\n어휘 ▶ guard 지키다 = protect · agency 주체성"),
  MC('<b>윗글의 요지로 가장 적절한 것은?</b>' + BX(P(T)),
     ['알고리즘이 설계한 환경에서 주체성을 지키려면 비판적이고 의식적인 태도가 필요하다.', '알고리즘의 추천은 객관적이므로 따르는 것이 합리적이다.', '넛지는 언제나 개인의 복지를 해친다.',
      '과거 데이터를 충분히 모으면 미래의 번영을 정확히 처방할 수 있다.', '디지털 기기 사용 시간을 줄이는 것이 가장 중요하다.'],
     "정답 ▶ 알고리즘이 설계한 환경에서 주체성을 지키려면 비판적이고 의식적인 태도가 필요하다.\n이유 ▶ It requires a conscious effort to maintain critical engagement ~\n오답 ▶ 추천을 따르는 게 합리적 → 추천에 도전하라(반대) / 넛지는 언제나 해롭다 → 유익하게 쓰일 수도 있다(과장) / 과거 데이터 = 미래 처방 → not necessarily a prescription(반대) / 사용 시간 → 언급 없음"),
  MC('<b>밑줄 친 <u>go against the predicted grain</u>이 의미하는 바로 가장 적절한 것은?</b>' + BX(U(T, 6, 'go against the predicted grain')),
     ['알고리즘이 예측한 방향을 그대로 따르지 않고 스스로 선택한다.', '곡물 가격 예측에 반대한다.', '다른 사람의 선택을 무조건 반대한다.', '예측이 틀릴 때까지 기다린다.', '모든 디지털 기술 사용을 거부한다.'],
     "정답 ▶ 알고리즘이 예측한 방향을 그대로 따르지 않고 스스로 선택한다.\n이유 ▶ grain(나뭇결, 흐름) → against the grain = 흐름을 거스르다. 알고리즘이 '예측한' 흐름에 반하는 '의도적' 선택\n오답 ▶ grain을 '곡물'로 해석한 함정 / 무조건 반대·전부 거부 → 과장"),
  MC('<b>윗글의 제목으로 가장 적절한 것은?</b>' + BX(P(T)),
     ['Steering Your Own Course in an Algorithm-Built World', 'Algorithms: Perfectly Neutral Guides to Better Lives', 'Nudges Always Lead to Healthier Choices',
      'Why Data from the Past Predicts the Future', 'The Death of Choice Architecture'],
     "정답 ▶ Steering Your Own Course in an Algorithm-Built World (알고리즘이 지은 세상에서 스스로 길을 정하기)\n이유 ▶ steer one's own course = 스스로 방향을 잡다 = 주체성(agency) 유지\n오답 ▶ 완벽히 중립적 → 특정 목표를 가진 인간이 설계 / 넛지는 언제나 건강한 선택 → 조작 가능성 / 과거가 미래를 예측 → 반대 / 선택 설계의 죽음 → 근거 없음"),
  MC('<b>필자가 권하는 태도와 거리가 <u>먼</u> 것은?</b>' + BX(P(T, [5, 6, 7])),
     ['accepting algorithmic results as objective facts', 'looking for a wide range of viewpoints', 'questioning the recommendations we receive', 'making choices on purpose', 'remembering that systems reflect human goals'],
     "정답 ▶ accepting algorithmic results as objective facts (알고리즘 결과를 객관적 사실로 받아들이기)\n이유 ▶ 필자는 겉보기에 객관적인 결과물에 '건전한 회의론'을 가지라고 해요.\n오답(권하는 것) ▶ 다양한 관점 찾기(seeking out diverse perspectives) / 추천에 도전(challenging) / 의도적 선택(deliberate choices) / 인간의 목표로 설계됨을 기억\n어휘 ▶ on purpose 의도적으로 = deliberately"),
 ],
 para=[
  MC('<b>밑줄 친 부분과 의미가 가장 가까운 것은?</b>' + BX(U(T, 2, 'curating')), ['selecting and organizing', 'curing', 'deleting completely', 'paying for', 'translating'],
     "정답 ▶ selecting and organizing (골라서 정리하는)\n이유 ▶ curate = (전시품·콘텐츠를) 선별하다. 무엇을 보고, 추천받고, 어떤 옵션이 나오는지 '골라 준다'\n오답 ▶ curing(치료하는)은 생김새 함정"),
  MC('<b>밑줄 친 부분과 의미가 가장 가까운 것은?</b>' + BX(U(T, 3, 'aligned with')), ['in agreement with', 'opposed to', 'hidden from', 'compared with', 'separated from'],
     "정답 ▶ in agreement with (~와 일치하는)\n이유 ▶ 설계자의 목표가 개인의 복지·자율성과 '일치하지 않을 때' 조작 가능성\n오답 ▶ opposed to는 not aligned with의 뜻이라 반대"),
  MC('<b>밑줄 친 부분과 의미가 가장 가까운 것은?</b>' + BX(U(T, 4, 'agency')), ['the ability to act and choose independently', 'a travel company', 'a government office', 'a strong emotion', 'a public opinion'],
     "정답 ▶ the ability to act and choose independently (독립적으로 행동하고 선택하는 능력)\n이유 ▶ 알고리즘의 유도와 대비 → 스스로 결정하는 힘 = 주체성\n오답 ▶ agency를 '대행사, 기관'으로 해석한 함정"),
  MC('<b>밑줄 친 부분과 의미가 가장 가까운 것은?</b>' + BX(U(T, 7, 'skepticism')), ['a questioning attitude', 'complete trust', 'deep fear', 'strong anger', 'total indifference'],
     "정답 ▶ a questioning attitude (의문을 품는 태도)\n이유 ▶ 겉보기에 객관적인 결과물을 그대로 믿지 않는 '건전한 회의론'\n오답 ▶ complete trust 반대 / fear·anger·indifference는 감정이지 '의심하며 따져 보는' 태도가 아님"),
  MC('<b>밑줄 친 부분과 의미가 가장 가까운 것은?</b>' + BX(U(T, 7, 'prescription')), ['an instruction for what should be done', 'a description of the past', 'a medical disease', 'a financial reward', 'a personal opinion'],
     "정답 ▶ an instruction for what should be done (해야 할 일에 대한 지시)\n이유 ▶ 데이터는 과거의 '반영'일 뿐, 미래를 위해 무엇을 해야 하는지 알려 주는 '처방'은 아니다\n오답 ▶ a description of the past는 reflection의 뜻(대비되는 말)"),
 ],
 pickv=[
  (PK(T, 1, 'sophisticated', 'clumsy'), "정답 ▶ sophisticated (정교한)\n이유 ▶ 우리가 보는 것을 선별하고 미묘하게 유도하는 설계자 → '정교한'\n오답 ▶ clumsy 서투른(반대)"),
  (PK(T, 3, 'manipulation', 'cooperation'), "정답 ▶ manipulation (조작)\n이유 ▶ While(~이지만) 유익하게 쓰일 수 있지만 → 설계자의 목표가 개인과 어긋날 때 '조작'의 가능성\n오답 ▶ cooperation 협력: While의 대비가 깨져요."),
  (PK(T, 4, 'protect', 'surrender'), "정답 ▶ protect (보호하다)\n이유 ▶ cultivate(기르다)와 짝 → 주체성을 '지키다'\n오답 ▶ surrender 넘겨주다, 포기하다(반대)"),
  (PK(T, 6, 'challenging', 'following'), "정답 ▶ challenging (도전하는, 이의를 제기하는)\n이유 ▶ 다양한 관점 찾기, 예측된 흐름을 거스르는 선택과 나란히 → 추천을 그대로 따르지 않음. 실전 42번의 정답 자리예요!\n오답 ▶ following 따르는(반대)"),
  (PK(T, 7, 'skepticism', 'reliance'), "정답 ▶ skepticism (회의론)\n이유 ▶ seemingly objective(겉보기에만 객관적인) 결과물 → 건전한 '의심'\n오답 ▶ reliance 의존(반대)"),
  (PK(T, 7, 'past realities', 'future goals'), "정답 ▶ past realities (과거의 현실)\n이유 ▶ 데이터 = 과거의 반영, 미래 번영의 처방은 아님 → reflection(반영) 대상은 '과거'\n오답 ▶ future goals: 뒤의 future flourishing과 대비가 사라져요."),
 ],
 tf=[
  ("Choice architecture explains how the design of a setting can shape people's decisions.", True, "정답 ▶ T\n이유: the design of the environment ~ can significantly influence the decisions\n어휘 ▶ shape 형성하다 = influence", "how the design of the environment in which choices are made can significantly influence the decisions"),
  ("The writer claims that nudges can never serve good purposes.", False, "정답 ▶ F\n이유: nudges can be used for beneficial purposes, such as encouraging healthier habits", "nudges can be used for beneficial purposes"),
  ("Algorithms play a role in deciding which options are presented to us.", True, "정답 ▶ T\n이유: curating ~ what options are presented to us", "what options are presented to us"),
  ("According to the writer, algorithmic data reliably tells us how to flourish in the future.", False, "정답 ▶ F\n이유: not necessarily a prescription for future flourishing", "not necessarily a prescription for future flourishing"),
  ("Protecting human agency requires deliberate effort on our part.", True, "정답 ▶ T\n이유: It requires a conscious effort\n어휘 ▶ deliberate 의도적인 = conscious", "It requires a conscious effort"),
  ("The writer recommends sticking to a single trusted perspective.", False, "정답 ▶ F\n이유: actively seeking out diverse perspectives(다양한 관점)", "actively seeking out diverse perspectives"),
 ],
 ilchi=[IL(True, T, ['Algorithms are designed without any specific goals.', 'Choice architecture became popular through behavioral economics.', 'Nudges can sometimes be far from subtle.',
                      'Manipulation is more likely when designers\' goals conflict with users\' well-being.', 'Algorithmic outputs may look objective.'],
  "정답 ▶ Algorithms are designed without any specific goals.\n이유: designed by humans with specific goals(특정 목표를 가진 인간이 설계)",
  [["특정 목표 없이 설계", "designed by humans with specific goals", "불일치"], ["행동 경제학에서 대중화", "popularized in behavioral economics", "일치"], ["넛지가 전혀 미묘하지 않을 때도", "sometimes not so subtly", "일치"],
   ["설계자 목표가 복지와 충돌하면 조작 가능성", "not aligned with the well-being or autonomy", "일치"], ["결과물이 객관적으로 보일 수 있음", "the seemingly objective outputs", "일치"]]),
        IL(False, T, ['Recommendations should be questioned rather than blindly accepted.', 'Algorithms present every possible option equally.', 'The writer opposes using nudges to encourage healthy habits.',
                       'Past data guarantees future success.', 'Human agency grows automatically in an algorithmic world.'],
  "정답 ▶ Recommendations should be questioned rather than blindly accepted.\n이유: challenging algorithmic recommendations + healthy skepticism",
  [["추천은 맹목적으로 받아들이지 말고 의문을 가져야", "challenging algorithmic recommendations", "일치"], ["모든 옵션을 똑같이 제시", "nudge us towards particular paths", "불일치 → 특정 경로로 유도"],
   ["건강한 습관 넛지에 반대", "beneficial purposes, such as encouraging healthier habits", "불일치"], ["과거 데이터가 미래 성공 보장", "not necessarily a prescription", "불일치"], ["주체성이 저절로 커짐", "requires a conscious effort", "불일치 → 의식적 노력 필요"]])],
 blank=[
  ("By curating what we see, what we are recommended, and what options are presented to us, they subtly, and sometimes not so subtly, ____ us towards particular paths.", ['nudge', 'prevent', 'release', 'warn'],
   "정답 ▶ nudge (슬쩍 유도하다)\n이유: towards particular paths(특정 경로로) + subtly(미묘하게) → 살짝 밀어서 이끈다"),
  ("It involves cultivating a healthy skepticism towards the seemingly ____ outputs of algorithms.", ['objective', 'emotional', 'useless', 'random'],
   "정답 ▶ objective (객관적인)\n이유: seemingly(겉보기에) + 뒤에 '인간이 특정 목표로 설계' → 겉으로만 객관적\n오답 ▶ useless: 쓸모없어 보이면 회의론을 기를 필요가 없음"),
  ("Their data is a reflection of past realities, not necessarily a ____ for future flourishing.", ['prescription', 'record', 'memory', 'mirror'],
   "정답 ▶ prescription (처방)\n이유: reflection(과거를 비춤)과 대비 → 미래를 위해 해야 할 일 = 처방\n오답 ▶ record·memory·mirror는 모두 reflection과 같은 방향"),
 ],
 summ=[("Since algorithms (A) ______ our choices in subtle ways, we must make conscious efforts to (B) ______ our ability to decide for ourselves.",
        ['(A) steer – (B) preserve', '(A) steer – (B) abandon', '(A) ignore – (B) preserve', '(A) record – (B) share', '(A) limit – (B) sell'],
        "정답 ▶ (A) steer – (B) preserve\n(A) nudge us towards particular paths → steer(조종하다, 이끌다)\n(B) cultivate and protect our human agency → preserve(지키다)\n오답 ▶ abandon(버리다)은 반대 / ignore: 알고리즘은 선택을 무시하지 않고 유도함",
        ["nudge us towards particular paths", "how can we cultivate and protect our human agency"])],
 abc=[ABC(T, [0], [[1, 2], [3, 4], [5, 6, 7]], 'CAB',
  "주어진 글(선택 설계: 환경 설계가 결정에 영향) → (C) 알고리즘 = 디지털 환경의 설계자, 특정 경로로 유도 → (A) While 유익할 수도 있지만 조작 가능성 + 질문: 주체성을 어떻게 지킬까? → (B) It requires ~ 의식적 노력, 다양한 관점, 회의론(답).\n포인트 ▶ (B)의 It은 앞의 질문(how can we ~ protect our human agency)을 받아요.")],
 order=[((1, 2, 3, 4), ["알고리즘 = 디지털 환경의 설계자", "선별해서 특정 경로로 유도", "유익할 수도 있지만 조작 가능성", "질문: 주체성을 어떻게 지킬까"]),
        ((4, 5, 6, 7), ["질문: 주체성을 어떻게 지킬까", "의식적 노력이 필요", "다양한 관점, 추천에 도전, 의도적 선택", "건전한 회의론, 인간이 설계했음을 기억"])],
 insert=[((3, 4, 5, 6), 2, "정답 ▶ ②\n이유: 조작 가능성 → 질문(어떻게 주체성을 지킬까?) → It requires ~(답). It이 가리킬 질문이 바로 앞에 있어야 해요."),
         ((0, 1, 2, 3), 1, "정답 ▶ ①\n이유: 선택 설계 개념 → 알고리즘은 본질적으로 디지털 환경의 설계자(연결) → By curating ~ they(알고리즘) 유도. they가 가리킬 Algorithms가 먼저 나와야 해요.")],
 odd=[((4, 5, 6), "Many companies now hire more engineers to improve the speed of their algorithms.",
       "정답 ▶ ③\n이유: 앞뒤는 주체성을 지키는 방법(의식적 노력, 다양한 관점). 알고리즘 속도 개선을 위한 채용은 흐름과 관계없어요."),
      ((2, 3, 4), "Algorithms have proven to be completely free from human bias.",
       "정답 ▶ ③\n이유: 필자는 알고리즘이 특정 목표를 가진 인간이 설계했다고 해요. 인간의 편향에서 완전히 자유롭다는 문장은 흐름과 반대예요.")],
 pickg=[
  (L(T, 0).replace('in which choices', '{in which|which} choices'), "정답 ▶ in which\n이유: 뒤가 완전한 절(choices are made) → 전치사 + 관계대명사(= where). which만 쓰면 불완전한 절이 와야 해요."),
  (L(T, 5).replace('to maintain', '{to maintain|maintaining}'), "정답 ▶ to maintain\n이유: a conscious effort to ~ = ~하려는 의식적 노력(to부정사의 형용사적 용법)"),
  (L(T, 7).replace('remembering that', '{remembering|remember} that'), "정답 ▶ remembering\n이유: involves의 목적어 cultivating과 and로 병렬 → 동명사 remembering"),
 ],
))

exec(open(G + 'blk_js2609_3133.py', encoding='utf-8').read())
exec(open(G + 'blk_js2609_3539.py', encoding='utf-8').read())
OUT.sort(key=lambda x: int(str(x['num']).split('~')[0]))
json.dump(OUT, open('/home/claude/work/js2d/new_3142.json', 'w', encoding='utf-8'), ensure_ascii=False)
print([(d['num'], len(d['steps']), sum(len(s['items']) for s in d['steps'])) for d in OUT])
