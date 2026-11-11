# 11/11 중산고1 · 비밀노트(edu-lab) 2025년 고1 9월 변형문제 18~24번 → h1-mock-2509 '비밀노트 변형문제' 탭 (종이 시험지 + 답안지)
# t1~t4.txt = hwp 글자(generators/hwpread.py). 문항 번호 = 파일 안 순서(묶음 '다음 글을 읽고 물음에 답하시오' 머리말은 번호 없음 — t3 '위 29번 참조'로 확인)
import re, json, html as H
D = '/home/claude/proj/data/h1-mock-2509.js'
CIRC = '①②③④⑤'; ALT = dict(zip('➀➁➂➃➄', CIRC))
def nc(s): return ''.join(ALT.get(c, c) for c in s)
SKIP = ('http://edu-lab', '비밀노트', 'edu-lab.kr')
# 파일별 문항 첫 줄(0부터 센 줄 번호)
STEMS = {
 '1': [11,18,22,24,32,47,55,62,69,94,108,120,132,158,166,176,183,187,189,193,202,206,209,212,233,241,249,257,279,283],
 '2': [0,7,10,13,22,26,30,39,47,55,62,70,78,86,96,98,100,103,107,110,119,129,137,145,153,161,169,177,185,195,203,207],
 '3': [0,11,19,27,35,44,53,62,71,75,79,83,87,90,93,96,99,103,107,111,115,119,123,127,133,141,148,155,172,184,192,199,206,213,225,228,231,235,241,244,251,255,261,271,278,288],
 '4': [0,8,16,24,28,39,56,65,73,81,101,119,123,128,133,139,144,148,152],
}
END = {'4': 162}
def arrow(a, b): return [a + s + b for s in (' → ', '→', ' -> ', '->', ' - ', ' ')] + [b]
def V(*xs):   # 정답 변형: 마침표·It's/It is
    out = []
    for x in xs:
        for y in (x, x.replace('’', "'"), x.replace('It’s', 'It is').replace("It's", 'It is')):
            if y not in out: out.append(y)
    return out
B = lambda lab, ans, review=False: {'label': lab, 'ans': ans if isinstance(ans, list) else V(ans), 'review': review}
# 서술형: (파일, 번호) → 칸들 · 모범답안
W = {
 ('1', 3): [B('', ['To study and do research after class.', 'To study and do research after class', 'to study and do research after class'], True)],
 ('1', 8): [B('', V('improving our academic environment and better supporting our needs', '[e] improving our academic environment and better supporting our needs'), True)],
 ('1', 14): [B('빈칸 1', ['restrictive']), B('빈칸 2', ['extended'])],
 ('1', 15): [B('', 'I hope you will take this recommendation into account as a step toward improving our academic environment and better supporting our needs.', True)],
 ('1', 18): [B('', ['Second senior munchkin', 'second senior munchkin', 'The second senior munchkin', 'She got the role of second senior munchkin.'], True)],
 ('1', 23): [B('', V('that whatever happened I could be involved in one of the productions', '[e] that whatever happened I could be involved in one of the productions'), True)],
 ('1', 29): [B('빈칸 1', ['audition']), B('빈칸 2', ['excited'])],
 ('1', 30): [B('', 'I had a wave of excitement wash over me', True)],
 ('2', 2): [B('', V('Often, if students are quiet enough and if there are many pressing demands on a teacher’s time at that moment, more than ten minutes can disappear before class starts.', '[a] Often, if students are quiet enough and if there are many pressing demands on a teacher’s time at that moment, more than ten minutes can disappear before class starts.'), True)],
 ('2', 15): [B('', ['The importance of using the opening minutes effectively'], True)],
 ('2', 16): [B('(A)', ['overlook']), B('(B)', ['the rest']), B('(C)', ['transitions'])],
 ('2', 17): [B('', V('you should establish an opening routine to develop your class with an effective start.', 'In summary, you should establish an opening routine to develop your class with an effective start.'), True)],
 ('2', 18): [B('', ['is→are, remained→remaining, because of→because, is existed→have existed'], True)],
 ('2', 31): [B('(1)', 'There are atoms in your body that have existed since the first moments of time, recycling throughout the universe among limitless forms, both nonliving and living.', True),
             B('(2)', ['태초부터 존재해 온 원자가 당신의 몸에 있으며 제한 없는 형태, 즉 비생물체와 생물체 가운데 우주 전체에 걸쳐 재순환한다.'], True)],
 ('2', 32): [B('', ['Through breathing and evaporation of sweat.', 'Through breathing and the evaporation of sweat.', 'By breathing and sweating.'], True)],
 ('3', 35): [B('', V('It’s a low-impact way to stay active and fit, making it accessible for people of all ages and physical abilities.', 'It is a low-impact way to stay active and fit, making it accessible for people of all ages and physical abilities.'), True)],
 ('3', 36): [B('', 'The sense of accomplishment from watching your plants grow and thrive can also boost self-esteem and overall well-being.', True)],
 ('3', 37): [B('', ['Robust Bodies and Mental Tranquility Resulting from Gardening'], True)],
 ('3', 38): [B('p', ['physically']), B('r', ['repetitively']), B('l', ['low', 'lower']), B('e', ['elevate']), B('c', ['confident'])],
 ('3', 39): [B('', 'humans have taken advantage of tools that translate and bring into our perception natural phenomena that we can’t perceive with our senses', True)],
 ('3', 40): [B('ⓐ', ['properties for which we have no sensory'], True), B('ⓑ', ['change them into that which we can observe'], True)],
 ('3', 41): [B('', 'Humans have qualitatively advanced the abilities of their sensory systems by using various tools.', True)],
 ('3', 42): [B('a', ['amplified']), B('e', ['expansions']), B('o', ['observe']), B('i', ['imperceptible'])],
 ('3', 43): [B('어법 ①', arrow('accessibly', 'accessible') + arrow('spend', 'spending')), B('어법 ②', arrow('spend', 'spending') + arrow('accessibly', 'accessible')),
             B('문맥 ①', arrow('accumulate', 'burn') + arrow('boast', 'boost')), B('문맥 ②', arrow('boast', 'boost') + arrow('accumulate', 'burn'))],
 ('3', 44): [B('1)', ['endurance']), B('2)', ['anxiety']), B('3)', ['weed', 'weeding'])],
 ('3', 45): [B('어법 ①', arrow('feeds', 'feed') + arrow('which', 'for which')), B('어법 ②', arrow('which', 'for which') + arrow('feeds', 'feed')),
             B('문맥 ①', arrow('abnormal', 'normal') + arrow('edible', 'audible')), B('문맥 ②', arrow('edible', 'audible') + arrow('abnormal', 'normal'))],
 ('3', 46): [B('1)', ['translate']), B('2)', ['signal', 'signals']), B('3)', ['property'])],
 ('4', 6): [B('(A)', 'not only is modern medicine not the only cause for the decline in mortality', True), B('(B)', 'has not been as responsible for biomedical discovery as defenders suggest', True)],
 ('4', 10): [B('①', ['inference']), B('②', ['prescribe', 'prescribes']), B('③', ['substantial'])],
 ('4', 11): [B('어법', arrow('that', 'than') + arrow('role that', 'role than')), B('문맥', arrow('support', 'reject'))],
 ('4', 14): [B('(A)', ['legal']), B('(B)', ['medical'])],
}
# 검수 메모 (해설 맨 앞에 붙임)
NOTE = {
 ('1', 17): '[검수] ❹ washing over: have + 목적어 + -ing(…이 ~하고 있게 하다)도 어법상 가능해서 틀린 것을 4개로 볼 여지가 있어요. 원문은 wash over.',
 ('2', 8): '[검수] 시험지 빈칸이 overlook 뒤에 있어서 "overlook fail to recognize ~"가 돼요. 빈칸은 overlook 자리부터(Inefficient teachers ______.)여야 해요. 정답 ①은 그대로.',
 ('2', 12): '[검수] 발문은 "고르시오"지만 정답이 ③④ 두 개 → "모두 고르시오"가 맞아요.',
 ('2', 18): '[검수] 정답표의 evaporates → is evaporated는 틀린 고침이에요. evaporate는 자동사라 "as our sweat evaporates"가 맞는 문장(원문). 실제 어색한 곳은 4개: is→are, remained→remaining, because of→because, is existed→have existed.',
 ('2', 27): '[검수] ② The Endless Recycling of Atoms도 글 전체(원자의 끝없는 순환)를 잘 담아 복수 정답 소지가 있어요.',
 ('3', 24): '[검수] ⓓ visual images(시각적 이미지)도 자연스러운 표현이라 2개로 볼 여지가 있어요.',
 ('3', 28): '[검수] 시험지 선지 번호 ③이 두 번 나와요(두 번째 ③ Spending time…). 정답은 첫 번째 ③ focus on anything but an object.',
}
def esc(s): return H.escape(s, quote=False)
def parse(fk):
    L = open('/home/claude/srcrepo/wrapup/bimi/t%s.txt' % fk, encoding='utf-8').read().split('\n')
    if fk in END: L = L[:END[fk]]
    S = STEMS[fk]; items = []
    for n, j in enumerate(S, 1):
        stop = S[n] if n < len(S) else len(L)
        seg = [l for l in L[j + 1:stop] if not l.strip().startswith(SKIP) and l.strip() not in ('/',)]
        stem = L[j].strip()
        key = (fk, n)
        if key in W:
            body = [l for l in seg]
            ans_line = ''
        else:
            ai = next(i for i, l in enumerate(seg) if re.match(r'\s*[①-⑤➀-➄]', nc(l)) and l.startswith(' '))
            ans_line = nc(seg[ai].strip()); body = seg[:ai] + seg[ai + 1:]
        it = {'n': str(n), 'src': ('%s번' % m.group(1)) if (m := re.search(r'\((\d\d)번?\)', stem)) else '', 'stem': esc(stem), 'pts': 2}
        txt = '\n'.join(l.rstrip() for l in body).strip()
        if key in W:
            bl = W[key]; per = round(2 / len(bl), 2)
            for b in bl: b['pts'] = per
            bl[-1]['pts'] = round(2 - per * (len(bl) - 1), 2)
            it.update({'kind': 'write', 'blanks': bl, 'body': esc(txt).replace('\n', '<br>'), 'model': ' / '.join(b['ans'][0] for b in bl),
                       'ex': (NOTE.get(key, '') + '\n' if key in NOTE else '') + ('여러 가지로 쓸 수 있는 답은 선생님이 확인해요.' if any(b['review'] for b in bl) else '')})
            items.append(it); continue
        m = re.match(r'([①-⑤]+)\s*:?\s*(.*)', ans_line)
        ans = [CIRC.index(c) for c in m.group(1)]
        # 선택지: ①로 시작하는 줄(한 줄에 여러 개 가능) / 표 모양(①\n A\n B)
        opts = [''] * 5; rest = []
        bl_ = body[:]; i = 0
        while i < len(bl_):
            l = nc(bl_[i].strip())
            if len(l) == 1 and l in CIRC and i + 2 < len(bl_):
                opts[CIRC.index(l)] = (bl_[i + 1].strip() + ' – ' + bl_[i + 2].strip()); i += 3; continue
            parts = re.split(r'(?=[①-⑤]\s)', l) if re.match(r'[①-⑤]', l) else None
            if parts and all(re.match(r'[①-⑤]', p) for p in parts if p.strip()):
                for p in parts:
                    if p.strip(): opts[CIRC.index(p[0])] = re.sub(r'\s+', ' ', re.sub(r'\s*(\t|\s{3,})\s*', ' – ', p[1:].strip())).strip()
            else: rest.append(bl_[i].rstrip())
            i += 1
        if not all(opts): opts = [o or CIRC[k] for k, o in enumerate(opts)]
        note = m.group(2).strip()
        orig = [l.strip() for l in rest if l.strip().startswith('[원문]')]
        rest = [l for l in rest if not l.strip().startswith('[원문]')]
        exs = []
        if key in NOTE: exs.append(NOTE[key])
        exs.append('정답 ▶ ' + ''.join(CIRC[a] for a in ans) + ((' ' + note) if note else ''))
        exs += orig
        it.update({'body': esc('\n'.join(rest).strip()).replace('\n', '<br>'), 'opts': [esc(o) for o in opts], 'en': sum(c.isascii() and c.isalpha() for c in opts[0]) > len(opts[0]) * .5,
                   'ans': ans[0] if len(ans) == 1 else ans, 'ex': '\n'.join(exs), 'ctx': ''})
        items.append(it)
    return items
META = [('1', 'bimi-1819', '18·19번'), ('2', 'bimi-2021', '20·21번'), ('3', 'bimi-2223', '22·23번'), ('4', 'bimi-24', '24번')]
tests = []
for fk, tid, sh in META:
    its = parse(fk)
    tests.append({'id': tid, 'kind': 'bimi', 'title': '비밀노트 변형문제 ' + sh, 'short': '비밀노트 ' + sh, 'school': '중산고 1학년', 'minutes': 50, 'items': its})
    mc = [i for i in its if i.get('kind') != 'write']
    print(tid, len(its), '문항 · 객관식', len(mc), '·', ' '.join('%s:%s' % (i['n'], ''.join(CIRC[a] for a in (i['ans'] if isinstance(i['ans'], list) else [i['ans']]))) for i in mc))
js = open(D, encoding='utf-8').read()
blk = ('/* BIMI-TESTS: 중산고1 비밀노트 변형문제 (wrapup/bimi/build_bimi.py 로 만듦 · 손으로 고치지 말 것) */\n'
       'window.PKG.tests = (window.PKG.tests || []).filter(function (t) { return t.kind !== "bimi"; }).concat(' + json.dumps(tests, ensure_ascii=False) + ');\n/* /BIMI-TESTS */\n')
if '/* BIMI-TESTS' in js: js = re.sub(r'/\* BIMI-TESTS.*?/\* /BIMI-TESTS \*/\n', lambda m: blk, js, flags=re.S)
else: js = js.rstrip('\n') + '\n' + blk
open(D, 'w', encoding='utf-8').write(js)
json.dump(tests, open('/home/claude/work/jsan/tests.json', 'w'), ensure_ascii=False, indent=1)
