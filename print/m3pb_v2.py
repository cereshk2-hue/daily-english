# 11/20 10:53 Picture Bride 분석지·백지노트 v2 — 지난번(m3rf7) 카드 형식처럼 자세하게. 시 원문은 저작권 때문에 싣지 않고
# 칸마다 영어 핵심어 · 구조(문형 + 새로 만든 영어 예문) · 끊어 읽기 순서(구조 단위 → 뜻) · 장면 · 숨은 뜻 · 내용 포인트 · 미니 예상문제
import sys, html
sys.path.insert(0, '/home/claude/srcrepo/print')
from m3pb_make import C, PARTS, pdf
esc = html.escape
D = {
 1: dict(pt=['비교급 + than (뒤 be동사 생략)', '나이 + when절'], kw=[('younger', '더 어린'), ('twenty-three', '스물셋(의)'), ('leave – left – left', '떠나다')],
    st=[('비교급 + than + 주어 (+ be동사 생략)', 'She was two years older than I (was).', '그녀는 나보다 두 살 많았다.'), ('나이 + when + 주어 + 동사', 'He was ten when he moved to Seoul.', '그는 서울로 이사했을 때 열 살이었다.')],
    jd=[('주어 + be동사 + 비교급', '그녀는 한 살 더 어렸다'), ('than + 비교 대상', '나보다'), ('나이 + when절', '한국을 떠날 때 스물셋')],
    q=('할머니가 한국을 떠난 나이와 화자의 나이는?', '할머니 23세, 화자는 한 살 많은 24세')),
 2: dict(pt=['Did + 주어 + 동사원형 ~?', '병렬: 동사원형 and 동사원형', '부사 simply의 위치'], kw=[('walk away', '걸어 나가다, 떠나다'), ('simply', '그저, 단순히'), ('close', '닫다')],
    st=[('Did + 주어 + (부사) + 동사원형 ~ and 동사원형 ~?', 'Did you simply say goodbye and leave?', '너는 그저 작별 인사를 하고 떠났니?'), ('부사는 주어 뒤, 동사원형 앞', 'Did he really finish the work?', '그가 정말 그 일을 끝냈니?')],
    jd=[('Did + 주어 + simply + 동사원형', '그녀는 그저 ~을 닫았을까'), ('목적어 (집의 문)', '아버지 집의 문을'), ('and + 동사원형', '그리고 걸어 나갔을까')],
    q=('\'simply(그저)\'에 담긴 화자의 생각은?', '그렇게 간단히 떠날 수 있었을 리 없다 — 이별의 무게를 짐작함')),
 3: dict(pt=['Was it + 거리 표현 + through A to B? (의문문)', '비인칭 it(거리)'], kw=[('a long way', '먼 길'), ('tailor shop', '양복점'), ('wharf', '부두, 선창')],
    st=[('It is far from A to B. (비인칭 it = 거리)', 'Was it far from your house to the station?', '너희 집에서 역까지 멀었니?'), ('through + 장소 = ~을 지나서', 'We walked through the market to the river.', '우리는 시장을 지나 강까지 걸었다.')],
    jd=[('Was + it(비인칭) + 거리 표현', '먼 길이었을까'), ('through + 장소(부산의 양복점들)', '부산의 양복점 거리를 지나'), ('to + 장소(부두)', '부두까지')],
    q=('할머니가 배를 탄 곳은?', '부산의 부두 (서울·제주 X)')),
 4: dict(pt=['관계부사 where', '소유격 관계대명사 whose', '과거완료 had + p.p.', 'to부정사(목적)'], kw=[('boat', '배'), ('island', '섬'), ('recently', '최근에'), ('learn – learned', '알게 되다, 배우다')],
    st=[('장소 + where + 주어 + 동사 (관계부사)', 'This is the park where we first met.', '이곳은 우리가 처음 만난 공원이다.'), ('명사 + whose + 명사 + 주어 + 동사 (소유격)', 'I visited a city whose name I can\'t pronounce.', '나는 이름을 발음할 수 없는 도시를 방문했다.'),
        ('had + p.p. — 과거보다 더 이전', 'He had just heard the news when I called him.', '내가 전화했을 때 그는 막 그 소식을 들은 상태였다.')],
    jd=[('부두 + where + 주어(배) + 동사', '그 부두에서는 배가 기다렸다'), ('to부정사 (데려가려고)', '그녀를 한 섬으로 데려가려고'), ('섬 + whose + 이름 + 주어 + had learned', '그 섬의 이름을 그녀는 최근에야 알았다')],
    q=('목적지가 낯선 곳이라는 것을 알 수 있는 내용은?', '그 섬의 이름을 할머니가 얼마 전에야 알게 됨')),
 5: dict(pt=['전치사 + whose', '분사구문(동시동작) -ing'], kw=[('shore', '해안가'), ('photograph', '사진'), ('turn A to the light', 'A를 빛 쪽으로 돌리다')],
    st=[('전치사 + whose + 명사 (그 ~의 …에서)', 'They reached an island on whose beach turtles lay eggs.', '그들은 해변에 거북이 알을 낳는 섬에 도착했다.'), ('주절, + -ing ~ (~하면서)', 'He sat by the window, reading her letter again.', '그는 그녀의 편지를 다시 읽으면서 창가에 앉아 있었다.')],
    jd=[('on + whose + 장소 명사', '그 섬의 해안에서'), ('주어(한 남자) + 동사', '한 남자가 기다렸다'), ('-ing 분사구문', '그녀의 사진을 빛 쪽으로 돌려 보며')],
    q=('남자가 가지고 있던 것과 그 이유는?', '할머니의 사진 — 사진만 보고 결혼을 약속한 사진신부라서')),
 6: dict(pt=['when 시간절', '수동태 과거 were + p.p. (light-lit-lit)'], kw=[('lantern', '등불'), ('camp', '숙소, 막사'), ('sugar mill', '설탕 공장'), ('light – lit – lit', '불을 켜다')],
    st=[('when + 주어 + were + p.p. (수동)', 'The candles were lit when the guests arrived.', '손님들이 도착했을 때 촛불이 켜졌다.'), ('light의 과거·과거분사 = lit', 'She lit a fire to keep warm.', '그녀는 몸을 녹이려고 불을 피웠다.')],
    jd=[('when + 주어(등불)', '~할 때, 등불이'), ('장소 (설탕 공장 밖 숙소)', '와이알루아 설탕 공장 밖 숙소에'), ('were + p.p.', '켜졌다')],
    q=('남자가 사는 곳과 하는 일은?', '와이알루아 설탕 공장 옆 숙소 · 사탕수수 농장 노동자')),
 7: dict(pt=['grow + 형용사 (~해지다)', '현재분사 후치 수식', 'from = 원인'], kw=[('luminous', '빛나는'), ('wing', '날개'), ('moth', '나방'), ('migrate', '이동하다'), ('cane stalk', '사탕수수 줄기')],
    st=[('grow + 형용사 = ~해지다 (2형식)', 'The sky grew dark after sunset.', '해가 진 뒤 하늘이 어두워졌다.'), ('명사 + -ing ~ (~하는 명사)', 'We watched birds flying south.', '우리는 남쪽으로 날아가는 새들을 보았다.'), ('from + 명사 = ~ 때문에', 'Her eyes were red from crying.', '그녀의 눈은 울어서 빨갰다.')],
    jd=[('and + 주어(그의 방 안)', '그리고 그의 방 안이'), ('grew + 형용사', '빛나게 되었을까'), ('from + 명사(날개)', '나방들의 날개 때문에'), ('-ing 수식 (사탕수수에서 나오는)', '사탕수수 줄기에서 나오는')],
    q=('방이 빛나게 된 것은 무엇 때문인가?', '사탕수수 줄기에서 날아온 나방들의 날개')),
 8: dict(pt=['What + 명사 + did + 주어 + 동사원형?', 'take A with + 사람'], kw=[('take ~ with her', '~을 가지고 가다'), ('grandmother', '할머니')],
    st=[('What + 명사 + did + 주어 + 동사원형 ~?', 'What books did you take with you?', '너는 어떤 책들을 가지고 갔니?'), ('take + 물건 + with + 사람', 'Take an umbrella with you.', '우산을 가지고 가라.')],
    jd=[('What + 명사(물건들)', '어떤 물건들을'), ('did + 주어 + 동사원형 + with her', '할머니는 가지고 갔을까')],
    q=('화자가 이 질문에 답하지 못하는 이유는?', '할머니의 과거를 직접 보지 못했고 물어볼 수도 없어서 — 상상하며 묻는 시')),
 9: dict(pt=['to부정사(목적)', '주격 관계대명사 who', '나이 차 + 비교급 than'], kw=[('arrive', '도착하다'), ('look into one\'s face', '~의 얼굴을 들여다보다'), ('stranger', '낯선 사람'), ('thirteen years older', '열세 살 더 많은')],
    st=[('동사 + to부정사 (~하려고)', 'She came to see her teacher.', '그녀는 선생님을 보려고 왔다.'), ('사람 + who + 동사 (주격)', 'I met the man who was my new coach.', '나는 나의 새 코치인 남자를 만났다.'), ('숫자 + years + 비교급 + than + 주어', 'My uncle is five years older than my mom.', '삼촌은 엄마보다 다섯 살 많다.')],
    jd=[('And when + 주어 + 동사', '그리고 그녀가 도착했을 때'), ('to부정사 (들여다보려고)', '낯선 사람의 얼굴을 들여다보려고'), ('who + was + 보어', '그녀의 남편인'), ('나이 차 + 비교급 + than + 주어', '그녀보다 열세 살 많은')],
    q=('\'남편인 낯선 사람\'이 보여 주는 것은?', '남편이지만 처음 보는 사람이라는 아이러니 · 13살 연상')),
 10: dict(pt=['did + 주어 + 부사 + 동사원형?', '접두사 un-(반대)'], kw=[('politely', '예의 바르게'), ('untie', '풀다'), ('silk', '비단'), ('bow', '매듭, 고름'), ('jacket', '윗옷(저고리)')],
    st=[('did + 주어 + 부사 + 동사원형 ~?', 'Did she quietly open the door?', '그녀는 조용히 문을 열었니?'), ('un + 동사 = 반대 동작', 'untie(풀다) · unlock(열다) · unpack(짐을 풀다)', 'tie(묶다) ↔ untie(풀다)')],
    jd=[('did + 주어 + politely + 동사원형', '그녀는 예의 바르게 풀었을까'), ('목적어 (비단 고름)', '저고리의 비단 고름을')],
    q=('할머니의 옷차림과 태도는?', '한복(저고리) · 예의 바르고 조심스러운 태도')),
 11: dict(pt=['독립분사구문 (명사 + -ing)', '주격 관계대명사 that', '관계부사 where', '과거진행 were + -ing'], kw=[('tent-shaped', '텐트 모양의'), ('dress', '치마, 드레스'), ('fill with', '~로 가득 차다'), ('dry wind', '건조한 바람'), ('surrounding', '주변의'), ('burn the cane', '사탕수수를 태우다')],
    st=[('주절, + 명사 + -ing ~ (명사가 ~하면서)', 'She walked on, her hair blowing in the wind.', '그녀는 머리카락을 바람에 날리며 계속 걸었다.'), ('명사 + that + 동사 (주격)', 'We felt the wind that came from the sea.', '우리는 바다에서 불어오는 바람을 느꼈다.'), ('장소 + where + 주어 + 동사', 'These are the fields where farmers grow rice.', '이곳이 농부들이 쌀을 기르는 들판이다.')],
    jd=[('명사(치마) + -ing', '그녀의 텐트 모양 치마가 가득 차면서'), ('with + 명사(건조한 바람)', '건조한 바람으로'), ('that + 동사 + from + 장소', '주변 들판에서 불어온'), ('where + 주어 + were + -ing', '남자들이 사탕수수를 태우고 있던')],
    q=('마지막 장면의 바람과 불타는 사탕수수가 암시하는 것은?', '할머니가 앞으로 살아갈 거친 노동 현실')),
}
FLOW = {1: '① 떠남', 2: '① 떠남', 3: '① 떠남', 4: '① 떠남', 5: '② 기다림', 6: '② 기다림', 7: '② 기다림', 8: '③ 만남', 9: '③ 만남', 10: '③ 만남', 11: '③ 만남'}
CSS = open('/home/claude/srcrepo/print/m3rf7_analysis.html', encoding='utf-8').read()
CSS = CSS[CSS.index('<style>'):CSS.index('</style>') + 8]
EX = '''<style>
.src{background:#eef1f5;border:1px dashed #8a97a8;border-radius:4px;padding:4px 10px;font-size:12px;margin:4px 0}
.src b{color:#26364a;margin-right:6px}
.hid{background:#fdf0e8;border-left:4px solid var(--red);padding:4px 10px;margin:4px 0;font-size:12px}.hid b{color:var(--red);margin-right:6px}
.pt2{background:#eef3f9;border-radius:4px;padding:2px 8px;margin:3px 0;font-size:12px}.pt2 b{color:#1f5bb8;margin-right:6px}
.exs{margin:2px 0 4px;padding-left:0;list-style:none}.exs li{margin:2px 0;font-size:12px}.exs .p{color:#b05a00;font-weight:700}.exs .e{font-family:var(--serif);font-size:13px}.exs .k{color:#555}
.bgk{background:var(--soft);border-radius:6px;padding:8px 12px;font-size:12px;line-height:1.6}.bgk p{margin:2px 0}
h2{break-after:avoid;page-break-after:avoid}
.note{font-size:11px;color:var(--muted)}
</style>'''

def card(n, part):
    d = D[n]; sc, hid, pt, gr = C[n]
    kw = ' · '.join('<b>%s</b> %s' % (esc(a), esc(b)) for a, b in d['kw'])
    st = ''.join('<li><span class="p">%s</span><br><span class="e">%s</span> <span class="k">— %s</span></li>' % (esc(p), esc(e), esc(k)) for p, e, k in d['st'])
    jd = ''.join("<div class='cr'><span class='en'><i>/</i>%s</span><span class='ko'>%s</span></div>" % (esc(a), esc(b)) for a, b in d['jd'])
    return ('<article class="card"><header class="ch"><span class="num">칸 %02d</span><span class="pt">POINT</span><ul>%s</ul><span class="flow">%s</span></header><div class="body">'
            '<div class="keyw"><span class="tag">핵심어</span>%s</div>'
            '<div class="src"><b>원문</b>학교 프린트 3쪽 표 %d번째 칸 (영어 원문을 함께 펴 놓고 보세요)</div>'
            '<div class="jd"><h4>끊어 읽기 순서 (구조 → 뜻)</h4>%s</div>'
            '<p class="tr"><b>장면</b> %s</p><div class="hid"><b>숨은 뜻</b>%s</div><div class="pt2"><b>내용 포인트</b>%s</div>'
            '<div class="gram"><b>구조 · 문법</b> (예문은 같은 구조로 새로 만든 문장)<ul class="exs">%s</ul></div>'
            "<div class='chk'><b>예상 문제</b> %s <span>→ %s</span></div></div></article>") % (
        n, ''.join('<li>%s</li>' % esc(x) for x in d['pt']), FLOW[n], kw, n, jd, esc(sc), esc(hid), esc(pt), st, esc(d['q'][0]), esc(d['q'][1]))

def analysis():
    from m3pb_make import analysis as old
    o = old()
    s, e = o.index('<section class="block"><h2>칸별 분석'), o.index('<section class="block"><h2>숨은 뜻 · 이미지 정리</h2>')
    cards = ''.join('<h2 style="margin-top:12px">%s</h2>' % esc(t) + ''.join(card(n, t) for n in ns) for t, ns in PARTS)
    gram = [('비교급 + than', '칸 1, 9', 'She was two years older than I (was).', 'than 뒤 be동사 생략 · 나이 차는 비교급 앞에'),
            ('Did / did + 주어 + 동사원형 ?', '칸 2, 8, 10', 'Did you simply say goodbye and leave?', '병렬 동사도 동사원형 · 부사는 동사 앞'),
            ('비인칭 it (거리)', '칸 3', 'Was it far from your house to the station?', 'it = 거리·시간·날씨'),
            ('관계부사 where', '칸 4, 11', 'This is the park where we first met.', '장소 + where + 완전한 문장'),
            ('소유격 관계대명사 whose', '칸 4, 5', 'I visited a city whose name I can\'t pronounce.', 'whose + 명사 / 전치사 + whose도 가능'),
            ('과거완료 had + p.p.', '칸 4', 'He had just heard the news when I called him.', '과거의 어느 때보다 더 이전'),
            ('분사구문 -ing (동시동작)', '칸 5', 'He sat by the window, reading her letter.', '~하면서'),
            ('독립분사구문', '칸 11', 'She walked on, her hair blowing in the wind.', '주어가 달라서 명사를 남김'),
            ('수동태 과거', '칸 6', 'The candles were lit when the guests arrived.', 'light – lit – lit'),
            ('grow + 형용사', '칸 7', 'The sky grew dark after sunset.', '~해지다 (부사 X)'),
            ('주격 관계대명사 who / that', '칸 9, 11', 'I met the man who was my new coach.', '사람 who · 사물 that'),
            ('to부정사 (목적)', '칸 4, 9', 'She came to see her teacher.', '~하려고')]
    gt = ''.join('<tr><td><b>%s</b></td><td>%s</td><td style="font-family:var(--serif)">%s</td><td>%s</td></tr>' % tuple(esc(x) for x in g) for g in gram)
    gsec = '<section class="block"><h2>구조 · 문법 한눈에 (예문은 새로 만든 문장)</h2><div class="tbl"><table><tr><th style="width:22%">문법</th><th style="width:11%">칸</th><th>예문</th><th style="width:26%">주의</th></tr>' + gt + '</table></div></section>'
    gq = ('<section class="block"><h2>문법 확인 문제 (새 문장)</h2><div class="q"><p><b>Q1.</b> 어법상 알맞은 것을 고르시오.</p><ol>'
          '<li>I visited a town (whose / who) streets were very narrow.</li><li>This is the beach (where / which) we found the shells.</li>'
          '<li>He stood at the door, (holding / held) a photo of her.</li><li>The room grew (quiet / quietly) after the guests left.</li>'
          '<li>The lanterns were (lit / lighted up) when it got dark.</li><li>She walked away, her dress (filling / filled) with wind.</li></ol></div>'
          '<div class="q"><p><b>Q2.</b> 우리말과 같도록 빈칸을 채우시오.</p><p>아빠는 엄마보다 열 살 많다. → My dad is ten years ________ ________ my mom.</p></div>'
          '<div class="q"><p><b>Q3.</b> 우리말에 맞게 배열하시오.</p><p>그는 그저 가방을 싸서 집을 떠났니? (just / he / pack / did / his bag / and / leave the house)</p></div>'
          '<div class="ans"><b>정답</b><br>Q1 whose / where / holding / quiet / lit / filling<br>Q2 older than<br>Q3 Did he just pack his bag and leave the house?</div></section>')
    o = o[:s] + '<section class="block"><h2>칸별 분석 (프린트 3쪽 표 순서)</h2>' + cards + '</section>' + gsec + o[e:]
    i = o.index('<section class="block"><h2>핵심 어휘</h2>')
    o = o[:i] + gq + o[i:]
    o = o.replace('</style>', '</style>' + EX, 1).replace('<small>내용 · 숨은 뜻 · 이야기 흐름 분석지</small>', '<small>칸별 구조 · 내용 · 숨은 뜻 분석지</small>')
    return o

def baekji(ans=False):
    from m3pb_make import baekji as old
    h = old()
    A = (lambda s: '<span class="anw">%s</span>' % esc(s)) if ans else (lambda s: '')
    for t, ns in PARTS:
        for n in ns:
            d = D[n]; sc, hid, pt, gr = C[n]
            o1 = '<tr class="s"><td class="no">%d</td><td class="en"><div class="ln"></div><div class="ln"></div></td><td class="ko"><div class="ln"></div><div class="ln"></div></td></tr>' % n
            if ans:
                left = '<span class="anw" style="font-family:inherit">프린트 3쪽 표 %d번째 칸 원문<br>끊어 읽기: %s</span>' % (n, esc(' / '.join(a for a, b in d['jd'])))
                right = '<span class="anw">%s<br>(장면) %s</span>' % (esc(' / '.join(b for a, b in d['jd'])), esc(sc))
            else:
                left = '<div class="ln"></div><div class="ln"></div><div class="ln"></div>'; right = '<div class="ln"></div><div class="ln"></div><div class="ln"></div>'
            n1 = '<tr class="s"><td class="no">%d</td><td class="en">%s</td><td class="ko">%s</td></tr>' % (n, left, right)
            assert h.count(o1) == 1; h = h.replace(o1, n1)
            i = h.index('<td colspan="2"><div class="cue">', h.index(n1)); j = h.index('</td></tr>', i)
            kw = ' · '.join('%s(%s)' % (a, b) for a, b in d['kw'])
            st = '<br>'.join('<b>%s</b> — <i>%s</i> %s' % (esc(p), esc(e), esc(k)) for p, e, k in d['st'][:2])
            cues = h[i + len('<td colspan="2">'):j]
            cue_q = cues[cues.index('<b>숨은 뜻 ✎</b>') + len('<b>숨은 뜻 ✎</b>'):cues.index('</div>')]
            blk = ('<div class="tip"><b>핵심어</b> %s</div><div class="tip"><b>구조</b> %s</div>'
                   '<div class="cue"><b>구조 찾기 ✎</b>이 칸에서 [%s] 구조를 찾아 원문에 표시하고 뜻을 쓰세요.</div>%s'
                   '<div class="cue"><b>숨은 뜻 ✎</b>%s</div>%s'
                   '<div class="cue"><b>예상 문제 ✎</b>%s</div>%s') % (
                esc(kw), st, esc(' · '.join(d['pt'])), A('→ ' + ' / '.join(d['pt']) + ' — ' + gr) if ans else '<div class="ln"></div>',
                cue_q, A('→ ' + hid) if ans else '<div class="ln"></div>', esc(d['q'][0]), A('→ ' + d['q'][1]) if ans else '<div class="ln"></div>')
            h = h[:i] + '<td colspan="2">' + blk + h[j:]
    h = h.replace('</style>', '.tip{font-size:9pt;color:#333;padding:1px 0}.tip b{color:#26364a;margin-right:4px}.tip i{font-family:Georgia,serif}.anw{color:#c8372d;font-size:9.5pt;line-height:1.5}\n</style>', 1)
    h = h.replace('왼쪽에 원문을 옮겨 쓰고, 오른쪽에 해석을 쓰세요. 아래 ✎ 칸에는 숨은 뜻을 정리하세요.', '왼쪽: 프린트 3쪽의 원문을 옮겨 쓰고 끊어 읽기(/) 표시 · 오른쪽: 해석 · 아래: 핵심어와 구조(새 예문)를 보고 ✎ 칸을 채우세요.')
    if ans:
        from m3pb_make import answer
        a = answer()
        p = a[a.index('<div class="pg"></div>'):]
        h = h[:h.index('<div class="pg"></div>')] + p
        h = h.replace('<small>백지노트</small>', '<small>백지노트 · 답지</small>').replace('왼쪽: 프린트 3쪽의 원문을 옮겨 쓰고 끊어 읽기(/) 표시 · 오른쪽: 해석 · 아래: 핵심어와 구조(새 예문)를 보고 ✎ 칸을 채우세요.', '빨간 글씨 = 모범 답 · 원문은 학교 프린트 3쪽 표로 확인')
    return h

if __name__ == '__main__':
    O = '/home/claude/work/m3pb/'
    for name, h in (('분석지', analysis()), ('백지노트', baekji()), ('백지노트_답지', baekji(True))):
        open(O + 'v2_%s.html' % name, 'w', encoding='utf-8').write(h); pdf(h, O + '중산중3_외부지문_PictureBride_%s.pdf' % name)
