# 11/20 중산중3 외부지문 2: Cathy Song 「Picture Bride」(1983, 저작권 있음 → 시 원문은 싣지 않음, 학교 프린트 3쪽 표 11칸 번호로 가리킴)
# 분석지(내용·숨은 뜻·이야기 흐름 중심, 선생님: 중3 외부지문은 내용문제 비중 큼) + 백지노트(좌 원문 옮겨 쓰기 · 우 해석 쓰기)
import html, sys
esc = html.escape
PARTS = [('Part 1. Leaving Korea · 한국을 떠나다', [1, 2, 3, 4]), ('Part 2. A Man with Her Photograph · 사진을 든 남자', [5, 6, 7]), ('Part 3. Meeting Her Husband · 남편을 만나다', [8, 9, 10, 11])]
# 칸: (장면, 숨은 뜻, 내용 포인트, 문법·구조)
C = {
 1: ('할머니는 화자보다 한 살 어렸고, 한국을 떠날 때 스물세 살이었다.',
     '화자가 지금 할머니가 떠났던 나이와 거의 같다 → 할머니의 일을 \'내 일\'처럼 상상하며 시가 시작된다.',
     '떠난 나이 23세 · 화자는 할머니보다 한 살 많다 → 화자는 24세(추론)',
     '숫자 + 비교급 + than ~ (한 살 더 어린) · than 뒤 be동사 생략'),
 2: ('할머니는 그저 아버지 집의 문을 닫고 걸어 나왔을까?',
     '\'그저(simply)\'라는 말에 \'그렇게 쉬웠을 리 없다\'는 마음이 담김 → 가족·고향과의 이별이 얼마나 무거웠을지 묻는다.',
     '아버지의 집을 떠남 = 가족과의 이별',
     'Did + 주어 + 동사원형(close) and (동사원형) walk → 병렬'),
 3: ('부산의 양복점 거리를 지나 부두까지 가는 길은 멀었을까?',
     '실제 거리보다 \'마음의 거리\' — 망설임, 두려움, 떠나기 싫은 마음 때문에 길이 길게 느껴졌을 것.',
     '출발한 곳 = 부산 (서울·제주 X) · 부두(wharf)에서 배를 탐',
     'Was it + 거리 표현 + through A to B? (A를 지나 B까지 먼 길이었나?) · 비인칭 it'),
 4: ('부두에서는 이름을 최근에야 알게 된 섬으로 할머니를 데려갈 배가 기다리고 있었다.',
     '목적지 이름조차 얼마 전에 알았다 → 모든 것이 낯선 곳으로 가는 불안함.',
     '목적지 = 하와이의 섬 (이름도 잘 모르던 곳)',
     '관계부사 where(선행사 장소) · 소유격 관계대명사 whose(섬의 이름) · 과거완료 had learned(떠나기 전에 이미 알게 된 일)'),
 5: ('그 섬의 해안에서는 한 남자가 할머니의 사진을 빛에 비춰 보며 기다리고 있었다.',
     '남자도 그녀를 사진으로만 안다 → 두 사람 모두 서로에게 \'낯선 사람\'. 사진을 자꾸 들여다보는 모습 = 기대·설렘·궁금함.',
     '남자가 가진 것 = 할머니의 사진 (편지·꽃 X) · 사진신부라는 제목의 뜻',
     '전치사 + whose (그 섬의 해안에서) · 분사구문 turning ~ (~하면서, 동시동작)'),
 6: ('와이알루아 설탕 공장 밖 숙소에 등불이 켜질 무렵.',
     '하루 노동이 끝난 저녁 → 남자는 사탕수수 농장에서 일하는 노동자. 고된 삶의 터전이 드러난다.',
     '장소 = 와이알루아 설탕 공장(Sugar Mill) 옆 노동자 숙소 · 시간 = 저녁',
     '수동태 were lit (light – lit – lit) · when 시간 접속사'),
 7: ('사탕수수 줄기 사이에서 날아온 나방들의 날개 때문에 그의 방 안이 환하게 빛났을까?',
     '초라한 방이 잠시 환해지는 장면 → 신부를 기다리는 남자 마음속의 희망과 설렘. 빛을 향해 모여드는 나방 = 기다림·끌림.',
     '나방은 사탕수수 줄기에서 나옴 · 방이 \'빛나는(luminous)\' 이미지',
     'grow + 형용사 = ~해지다 (2형식) · 현재분사 migrating이 moths를 뒤에서 꾸밈'),
 8: ('할머니는 어떤 물건들을 가지고 떠났을까?',
     '화자는 답을 모른다 → 짐 속에는 물건뿐 아니라 고향의 기억·두려움·희망도 들어 있었을 것.',
     '화자가 할머니에게 직접 물어볼 수 없는 과거에 대한 궁금증',
     'What things did + 주어 + 동사원형? (의문사 의문문)'),
 9: ('할머니가 도착해 열세 살 많은 낯선 사람, 곧 남편의 얼굴을 들여다볼 때.',
     '\'남편인 낯선 사람\' — 남편이지만 처음 보는 사람이라는 아이러니(모순). 결혼 첫 만남의 어색함과 긴장.',
     '남편은 13살 연상 (3살·23살 X) · 처음 만나는 사이 (오래 알고 지낸 사이 X)',
     'to부정사(목적) · 주격 관계대명사 who · 나이 차 + 비교급 + than + 주어'),
 10: ('할머니는 예의 바르게 저고리의 비단 고름을 풀었을까?',
      '\'예의 바르게\' → 낯선 남편 앞에서의 조심스러움, 새 삶(결혼)을 받아들이는 순종과 긴장. 한복(저고리) = 할머니가 지닌 한국의 정체성.',
      '할머니는 한국 전통 옷차림 · 첫 만남의 태도 = 공손함',
      'did + 주어 + 동사원형(untie)? · untie = un(반대) + tie(묶다)'),
 11: ('남자들이 사탕수수를 태우던 주변 들판에서 불어온 건조한 바람이 할머니의 치마를 가득 부풀렸다.',
      '마르고 뜨거운 바람·불타는 사탕수수 = 앞으로 살아갈 낯선 땅의 거친 노동 현실. 바람에 부푼 치마 = 새 세계로 밀려 들어가는 할머니의 운명.',
      '들판에서 남자들이 사탕수수를 태움 · 바람은 건조(dry)함',
      '독립분사구문 명사 + -ing (치마가 바람으로 가득 차면서) · 주격 관계대명사 that · 관계부사 where'),
}
CSS = open('/home/claude/srcrepo/print/m3rf7_analysis.html', encoding='utf-8').read()
CSS = CSS[CSS.index('<style>'):CSS.index('</style>') + 8]
EXTRA = '''<style>
.bgk{background:var(--soft);border-radius:6px;padding:8px 12px;font-size:12px;line-height:1.6}
.bgk p{margin:2px 0}
.pt2{background:#eef3f9;border-radius:4px;padding:2px 8px;margin:3px 0;font-size:12px}
.pt2 b{color:#1f5bb8;margin-right:6px}
.hid{background:#fdf0e8;border-left:4px solid var(--red);padding:4px 10px;margin:4px 0;font-size:12.5px}
.hid b{color:var(--red);margin-right:6px}
.scene{font-size:13.5px;font-weight:700;margin:2px 0 4px}
.note{font-size:11px;color:var(--muted)}
.qq ol{margin:2px 0;padding-left:20px}.qq li{margin:1px 0}
.two{display:grid;grid-template-columns:1fr 1fr;gap:10px}
h2{break-after:avoid;page-break-after:avoid}
</style>'''

def analysis():
    cards = []
    for title, ns in PARTS:
        cards.append('<h2 style="margin-top:12px">%s</h2>' % esc(title))
        for n in ns:
            sc, hid, pt, gr = C[n]
            cards.append('<article class="card"><header class="ch"><span class="num">칸 %d</span><span class="pt">장면</span><ul><li>%s</li></ul></header><div class="body">'
                         '<p class="scene">%s</p><div class="hid"><b>숨은 뜻</b>%s</div><div class="pt2"><b>내용 포인트</b>%s</div>'
                         '<div class="gram"><b>문법·구조</b> %s</div></div></article>' % (n, esc(title.split(' · ')[1]), esc(sc), esc(hid), esc(pt), esc(gr)))
    tf = [('할머니는 스물세 살에 한국을 떠났다.', 'O'), ('할머니는 남편을 오래 전부터 알고 지냈다.', 'X · 처음 보는 낯선 사람'),
          ('남편은 할머니의 사진을 가지고 있었다.', 'O'), ('할머니는 서울에서 배를 탔다.', 'X · 부산의 부두'),
          ('남편은 할머니보다 세 살 많았다.', 'X · 열세 살'), ('남편은 설탕 공장 근처 숙소에서 지냈다.', 'O'),
          ('할머니는 목적지 섬의 이름을 오래 전부터 알고 있었다.', 'X · 최근에야 알게 됨'),
          ('시의 화자는 할머니의 과거를 궁금해한다.', 'O'), ('화자는 할머니보다 나이가 어리다.', 'X · 한 살 많다'),
          ('할머니가 도착했을 때 들판에서는 사탕수수를 태우고 있었다.', 'O')]
    mc = [('시의 화자는 누구인가?', ['할머니의 손녀', '할머니의 남편', '할머니의 아버지', '설탕 공장 주인', '부산의 양복점 주인'], 0, '할머니를 my grandmother라고 부르고 자신과 나이를 비교함'),
          ('이 시의 대부분 문장이 의문문으로 이루어진 이유로 가장 알맞은 것은?', ['화자가 할머니의 경험을 상상하며 궁금해하기 때문에', '할머니가 화자에게 질문을 했기 때문에', '남편이 할머니를 의심했기 때문에', '화자가 할머니를 비판하기 때문에', '독자에게 퀴즈를 내기 위해서'], 0, '화자는 직접 볼 수 없었던 할머니의 과거를 상상하며 묻는다 — 답은 시에 나오지 않음'),
          ('남자가 사진을 빛에 비춰 보는 모습에서 알 수 있는 남자의 마음은?', ['기대와 설렘', '분노와 실망', '지루함', '후회', '무관심'], 0, '아직 만나지 못한 신부를 사진으로 자꾸 들여다봄'),
          ('"남편인 낯선 사람"이라는 표현이 보여 주는 것은?', ['남편이지만 처음 보는 사이라는 아이러니', '남편이 외국인이라는 사실', '남편이 할머니를 싫어했다는 사실', '두 사람이 어릴 때부터 친구였다는 사실', '남편이 이름을 숨겼다는 사실'], 0, '사진만으로 결혼을 약속했기 때문에 처음 만나는 날 남편은 아직 낯선 사람'),
          ('마지막 장면의 건조한 바람과 불타는 사탕수수가 암시하는 것은?', ['할머니가 살아갈 거친 노동 현실', '할머니의 고향 부산의 풍경', '행복한 결혼식 축제', '남편의 부유한 생활', '화자의 현재 생활'], 0, '사탕수수 농장의 뜨겁고 힘든 노동 환경이 할머니를 맞이함'),
          ('이야기의 순서로 알맞은 것은? (a) 남자가 사진을 보며 기다린다 (b) 한국을 떠난다 (c) 낯선 남편을 만난다 (d) 배를 타고 섬으로 향한다', ['(b)-(d)-(a)-(c)', '(a)-(b)-(c)-(d)', '(b)-(a)-(d)-(c)', '(d)-(b)-(a)-(c)', '(b)-(c)-(d)-(a)'], 0, 'Part 1 떠남·배 → Part 2 기다리는 남자 → Part 3 만남 (학교 프린트 Activity 4: 1 떠남 · 2 배 · 3 기다림 · 4 만남)')]
    wr = [('할머니가 한국을 떠날 때의 마음을 두 가지 영어 형용사로 쓰고 이유를 한국어로 쓰시오.', '예) sad, nervous — 가족·고향을 떠나 처음 보는 사람과 결혼하러 낯선 나라로 가기 때문 (scared, lonely도 근거가 맞으면 정답)'),
          ('화자가 몇 살인지 쓰고, 그렇게 생각한 근거를 쓰시오.', '24세 — 할머니가 화자보다 한 살 어렸고 떠날 때 23세였다고 말함'),
          ('「Picture Bride(사진신부)」라는 제목의 뜻을 우리말로 설명하시오.', '사진만 보고 결혼을 약속한 뒤, 얼굴도 모르는 남편을 만나러 먼 나라로 간 신부')]
    tfh = ''.join('<tr><td>%d</td><td>%s</td><td>%s</td></tr>' % (i + 1, esc(q), esc(a)) for i, (q, a) in enumerate(tf))
    mch = ''.join('<div class="q qq"><p><b>%d.</b> %s</p><ol>%s</ol><p class="note">정답 ① · %s</p></div>' % (i + 1, esc(q), ''.join('<li>%s</li>' % esc(o) for o in os_), esc(why)) for i, (q, os_, a, why) in enumerate(mc))
    wrh = ''.join('<div class="q"><p><b>%d.</b> %s</p><p class="note">예시 답 · %s</p></div>' % (i + 1, esc(q), esc(a)) for i, (q, a) in enumerate(wr))
    sym = [('그저 문을 닫고 떠났을까?', '그렇게 쉬웠을 리 없다 → 이별의 무게'), ('부두까지의 먼 길', '실제 거리 + 마음의 거리(망설임)'), ('이름을 최근에야 안 섬', '모든 것이 낯선 목적지 → 불안'),
           ('사진을 빛에 비춰 보는 남자', '기대·설렘 / 남자도 그녀를 모름'), ('나방 날개로 빛나는 방', '기다리는 남자 마음속의 희망'), ('남편인 낯선 사람', '아이러니 — 남편이지만 처음 보는 사람'),
           ('예의 바르게 고름을 풂', '조심스러움·순종 / 한복 = 한국인의 정체성'), ('건조한 바람·불타는 사탕수수', '앞으로 살아갈 거친 노동 현실'), ('바람에 부푼 치마', '새 세계로 밀려 들어가는 운명')]
    symh = ''.join('<tr><td>%s</td><td>%s</td></tr>' % (esc(a), esc(b)) for a, b in sym)
    return ('<!DOCTYPE html><html lang="ko"><head><meta charset="utf-8"><title>중산중3 외부지문 Picture Bride 분석지</title>%s%s</head><body><div class="wrap">' % (CSS, EXTRA) +
        '<div class="top"><h1>중산중3 외부지문 「Picture Bride」 <small>내용 · 숨은 뜻 · 이야기 흐름 분석지</small></h1>'
        '<div class="meta">Cathy Song(캐시 송) · 1983년 시집 『Picture Bride』의 표제시 · 학교 프린트 15~19쪽 · 칸 번호 = 프린트 3쪽 「시 원문 | 우리말 해석」 표의 순서 (원문은 프린트로 확인)</div></div>'
        '<section class="block"><h2>배경 — 사진신부란?</h2><div class="bgk">'
        '<p>· 1903년부터 많은 한국인이 하와이 사탕수수 농장 노동자로 건너감 → 대부분 남자라 결혼 상대를 찾기 어려움</p>'
        '<p>· 남자들이 한국으로 사진을 보내고, 사진만 보고 결혼을 약속한 여성들이 배를 타고 하와이로 감 = <b>사진신부</b> (1910~1924년, 약 600~1,000명)</p>'
        '<p>· 도착해 보니 사진보다 나이가 많은 신랑, 생각과 다른 고된 농장 생활이 기다리기도 함</p>'
        '<p>· 시인 Cathy Song(1955~, 하와이 출생)의 한국인 할머니가 사진신부 → 손녀가 스물세 살의 할머니를 상상하며 쓴 시. 1982년 예일 젊은 시인상 수상작</p></div></section>'
        '<section class="block"><h2>한눈에 보기</h2><div class="tbl"><table>'
        '<tr><th style="width:18%">항목</th><th>내용</th></tr>'
        '<tr><td>화자</td><td>할머니의 손녀(나) — 할머니보다 한 살 많음 → 24세</td></tr>'
        '<tr><td>등장인물</td><td>할머니(23세에 부산에서 출발) · 남편(13살 연상, 와이알루아 설탕 공장 노동자, 할머니의 사진을 가지고 기다림)</td></tr>'
        '<tr><td>형식의 특징</td><td>시 전체가 <b>질문(의문문)</b>으로 이어짐 → 화자는 답을 모른다. 직접 볼 수 없었던 할머니의 과거를 상상하며 궁금해하고 공감함</td></tr>'
        '<tr><td>흐름</td><td>Part 1 떠남(집 → 부산 거리 → 부두 → 배) → Part 2 섬에서 사진을 들고 기다리는 남자 → Part 3 도착·낯선 남편과의 첫 만남</td></tr>'
        '<tr><td>주제</td><td>낯선 나라로 시집간 사진신부 할머니의 용기·두려움과, 그 삶을 이해하려는 손녀의 마음</td></tr>'
        '<tr><td>정서 변화</td><td>할머니: 슬픔·긴장(떠남) → 낯섦·불안(섬) → 어색함·조심스러움(첫 만남) / 남자: 기대·설렘</td></tr>'
        '</table></div></section>'
        '<section class="block"><h2>칸별 분석 (프린트 3쪽 표 순서)</h2>' + ''.join(cards) + '</section>'
        '<section class="block"><h2>숨은 뜻 · 이미지 정리</h2><div class="tbl"><table><tr><th style="width:38%">장면·표현</th><th>숨은 뜻</th></tr>' + symh + '</table></div></section>'
        '<section class="block"><h2>예상 내용 문제</h2><h2 style="font-size:13px;border-left-color:#26364a">A. T/F (일치하면 O)</h2><div class="tbl"><table><tr><th style="width:5%"></th><th>문장</th><th style="width:28%">정답</th></tr>' + tfh + '</table></div>'
        '<h2 style="font-size:13px;border-left-color:#26364a;margin-top:10px">B. 객관식</h2>' + mch +
        '<h2 style="font-size:13px;border-left-color:#26364a;margin-top:10px">C. 서술형</h2>' + wrh + '</section>'
        '<section class="block"><h2>핵심 어휘</h2><div class="tbl"><table><tr><th>어휘</th><th>뜻</th><th>어휘</th><th>뜻</th></tr>'
        '<tr><td>wharf</td><td>부두, 선창</td><td>shore</td><td>해안가</td></tr><tr><td>tailor shop</td><td>양복점</td><td>lantern</td><td>등불, 랜턴</td></tr>'
        '<tr><td>lit (light-lit-lit)</td><td>불이 켜진</td><td>sugar mill</td><td>설탕 공장</td></tr><tr><td>luminous</td><td>빛나는</td><td>moth</td><td>나방</td></tr>'
        '<tr><td>migrate</td><td>이동하다</td><td>cane stalk</td><td>사탕수수 줄기</td></tr><tr><td>stranger</td><td>낯선 사람</td><td>politely</td><td>예의 바르게</td></tr>'
        '<tr><td>untie</td><td>풀다</td><td>bow</td><td>매듭, 고름</td></tr><tr><td>tent-shaped</td><td>텐트 모양의</td><td>surrounding</td><td>주변의</td></tr>'
        '</table></div></section></div></body></html>')

def baekji():
    tpl = open('/home/claude/srcrepo/print/m3rf7_baekji.html', encoding='utf-8').read()
    head = tpl[:tpl.index('</style>')] + '''.cue{font-size:9pt;color:#9a3b2d;padding:2px 0 0}
.cue b{margin-right:4px}
td.en{border-right:1px solid #bbb}
td.en .ln,td.ko .ln{height:24px}
.part td{background:#eef1f5;font-weight:700;font-size:10pt;padding:3px 8px;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.st td,.st th{border:1px solid #888;font-size:9.5pt;padding:4px 6px;height:30px}
.st th{background:#eef1f5;color:#111}
.flow4{display:grid;grid-template-columns:repeat(4,1fr);gap:6px}.flow4 div{border:1px solid #888;height:84px;font-size:9pt;padding:3px 6px;color:#555}
</style></head><body>'''
    cues = {1: '화자는 몇 살일까?', 2: '\'그저\'라는 말에 담긴 마음은?', 3: '왜 길이 멀게 느껴졌을까?', 4: '목적지가 낯설다는 것을 보여 주는 말은?',
            5: '남자는 그녀를 어떻게 알고 있을까? 그의 마음은?', 6: '남자는 어떤 일을 하는 사람일까?', 7: '빛나는 방은 무엇을 뜻할까?',
            8: '화자는 왜 답을 모를까?', 9: '\'남편인 낯선 사람\'의 아이러니는?', 10: '\'예의 바르게\'에서 느껴지는 할머니의 마음은?', 11: '건조한 바람·불타는 사탕수수가 암시하는 것은?'}
    rows = []
    for title, ns in PARTS:
        rows.append('<tr class="part"><td colspan="3">%s</td></tr>' % esc(title))
        for n in ns:
            rows.append('<tr class="s"><td class="no">%d</td><td class="en"><div class="ln"></div><div class="ln"></div></td><td class="ko"><div class="ln"></div><div class="ln"></div></td></tr>'
                        '<tr class="memo"><td></td><td colspan="2"><div class="cue"><b>숨은 뜻 ✎</b>%s</div><div class="ln"></div></td></tr>' % (n, esc(cues[n])))
    sym = ['그저 문을 닫고 떠났을까?', '부두까지의 먼 길', '이름을 최근에야 안 섬', '사진을 빛에 비춰 보는 남자', '나방 날개로 빛나는 방', '남편인 낯선 사람', '예의 바르게 고름을 풂', '건조한 바람 · 불타는 사탕수수']
    return (head +
        '<div class="hd"><h1>중산중3 외부지문 「Picture Bride」 <small>백지노트</small></h1><div class="id">이름<span></span> 날짜<span></span></div></div>'
        '<p class="sub">Cathy Song · 칸 번호 = 학교 프린트 3쪽 표 순서. 왼쪽에 원문을 옮겨 쓰고, 오른쪽에 해석을 쓰세요. 아래 ✎ 칸에는 숨은 뜻을 정리하세요.</p>'
        '<table><tr><th></th><th>원문 옮겨 쓰기</th><th>해석</th></tr>' + ''.join(rows) + '</table>'
        '<div class="pg"></div><h2>이야기 흐름 (네 장면을 순서대로)</h2><div class="flow4"><div>① </div><div>② </div><div>③ </div><div>④ </div></div>'
        '<h2>인물 정리</h2><table class="st"><tr><th style="width:16%">인물</th><th>나이 · 장소</th><th>하는 일 · 가진 것</th><th>마음</th></tr><tr><td>할머니</td><td></td><td></td><td></td></tr><tr><td>남편</td><td></td><td></td><td></td></tr><tr><td>화자</td><td></td><td></td><td></td></tr></table>'
        '<h2>숨은 뜻 정리</h2><table class="st"><tr><th style="width:36%">장면 · 표현</th><th>숨은 뜻</th></tr>' + ''.join('<tr><td>%s</td><td></td></tr>' % esc(s) for s in sym) + '</table>'
        '<div class="grid"><div><h2>시 전체가 질문인 이유</h2><div class="box" style="height:120px"></div></div><div><h2>서술형 대비 (할머니의 마음 · 제목의 뜻)</h2><div class="box" style="height:120px"></div></div></div>'
        '</body></html>')

def pdf(h, out):
    from playwright.sync_api import sync_playwright
    open('/tmp/_pb.html', 'w', encoding='utf-8').write(h)
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(); pg.goto('file:///tmp/_pb.html'); pg.wait_for_timeout(1500)
        pg.pdf(path=out, format='A4', print_background=True, prefer_css_page_size=True); b.close()

if __name__ == '__main__' and 'answer' not in sys.argv:
    O = '/home/claude/work/m3pb/'
    a = analysis(); open(O + 'analysis.html', 'w', encoding='utf-8').write(a); pdf(a, O + '중산중3_외부지문_PictureBride_분석지.pdf')
    n = baekji(); open(O + 'baekji.html', 'w', encoding='utf-8').write(n); pdf(n, O + '중산중3_외부지문_PictureBride_백지노트.pdf')

# 11/20 10:47 선생님: 백지노트 답지 — 원문 칸은 '프린트 3쪽 n번 칸', 해석 칸은 장면 요약(내 말), ✎ 숨은 뜻 답, 3쪽 정리 칸 모범답
def answer():
    h = baekji()
    A = {n: C[n] for n in C}
    for title, ns in PARTS:
        for n in ns:
            sc, hid, pt, gr = A[n]
            old = '<tr class="s"><td class="no">%d</td><td class="en"><div class="ln"></div><div class="ln"></div></td><td class="ko"><div class="ln"></div><div class="ln"></div></td></tr>' % n
            new = '<tr class="s"><td class="no">%d</td><td class="en" style="font-family:inherit;font-size:9.5pt;color:#555">프린트 3쪽 표 %d번째 칸 원문<br><span style="color:#1f5bb8">포인트: %s</span></td><td class="ko"><span class="anw">%s</span></td></tr>' % (n, n, esc(pt), esc(sc))
            assert h.count(old) == 1; h = h.replace(old, new)
            i = h.index('<td colspan="2"><div class="cue">', h.index(new))
            j = h.index('<div class="ln"></div></td></tr>', i)
            h = h[:j] + '<div class="anw" style="padding:2px 0 4px">→ %s</div></td></tr>' % esc(hid) + h[j + len('<div class="ln"></div></td></tr>'):]
    fill = [('<div class="flow4"><div>① </div><div>② </div><div>③ </div><div>④ </div></div>',
             '<div class="flow4"><div class="anw">① 한국(부산)을 떠난다 — 아버지 집 → 양복점 거리 → 부두 (Part 1)</div><div class="anw">② 배를 타고 이름도 낯선 섬(하와이)으로 향한다 (Part 1)</div><div class="anw">③ 섬에서 한 남자가 그녀의 사진을 빛에 비춰 보며 기다린다 (Part 2)</div><div class="anw">④ 도착해 열세 살 많은 낯선 남편을 만난다 (Part 3)</div></div>'),
            ('<tr><td>할머니</td><td></td><td></td><td></td></tr>', '<tr><td>할머니</td><td class="anw">23세 · 부산에서 출발 → 하와이 섬</td><td class="anw">사진신부, 저고리(한복) 차림, 무엇을 가져갔는지는 모름</td><td class="anw">슬픔·긴장 → 낯섦·불안 → 조심스러움</td></tr>'),
            ('<tr><td>남편</td><td></td><td></td><td></td></tr>', '<tr><td>남편</td><td class="anw">할머니보다 13살 많음 · 와이알루아 설탕 공장 옆 숙소</td><td class="anw">사탕수수 농장 노동자, 할머니의 사진을 가지고 있음</td><td class="anw">기대·설렘 (사진을 빛에 비춰 봄)</td></tr>'),
            ('<tr><td>화자</td><td></td><td></td><td></td></tr>', '<tr><td>화자</td><td class="anw">할머니보다 한 살 많음 → 24세</td><td class="anw">할머니의 손녀, 할머니의 과거를 상상하며 질문함</td><td class="anw">궁금함·공감</td></tr>')]
    sym = {'그저 문을 닫고 떠났을까?': '그렇게 쉬웠을 리 없다 → 가족·고향과의 이별의 무게', '부두까지의 먼 길': '실제 거리 + 마음의 거리(망설임·두려움)', '이름을 최근에야 안 섬': '모든 것이 낯선 목적지 → 불안',
           '사진을 빛에 비춰 보는 남자': '기대·설렘 / 남자도 그녀를 사진으로만 앎', '나방 날개로 빛나는 방': '기다리는 남자 마음속의 희망', '남편인 낯선 사람': '아이러니 — 남편이지만 처음 보는 사람',
           '예의 바르게 고름을 풂': '조심스러움·순종 / 한복 = 한국인의 정체성', '건조한 바람 · 불타는 사탕수수': '앞으로 살아갈 거친 노동 현실 (바람에 부푼 치마 = 새 세계로 밀려 들어가는 운명)'}
    for a, b in fill: assert h.count(a) == 1, a; h = h.replace(a, b)
    for k, v in sym.items():
        a = '<tr><td>%s</td><td></td></tr>' % esc(k); assert h.count(a) == 1, k
        h = h.replace(a, '<tr><td>%s</td><td class="anw">%s</td></tr>' % (esc(k), esc(v)))
    boxes = h.split('<div class="box" style="height:120px"></div>'); assert len(boxes) == 3
    h = (boxes[0] + '<div class="box anw" style="height:auto;min-height:120px">화자는 할머니의 과거를 직접 볼 수 없었고 물어볼 수도 없다 → 답을 모르는 채 상상하며 묻는다. 질문이 이어질수록 할머니에 대한 궁금증과 공감이 커진다. (시에는 답이 나오지 않음)</div>' +
         boxes[1] + '<div class="box anw" style="height:auto;min-height:120px">· 마음: sad, nervous (scared, lonely) — 가족·고향을 떠나 처음 보는 사람과 결혼하러 낯선 나라로 가기 때문<br>· I think she felt sad and nervous.<br>· 제목: 사진만 보고 결혼을 약속한 뒤, 얼굴도 모르는 남편을 만나러 먼 나라로 간 신부<br>· 화자 나이 24세 — 할머니가 한 살 어렸고 떠날 때 23세</div>' + boxes[2])
    h = h.replace('<small>백지노트</small>', '<small>백지노트 · 답지</small>').replace('</style>', '.anw{color:#c8372d;font-size:9.5pt;line-height:1.5}\n</style>', 1)
    h = h.replace('왼쪽에 원문을 옮겨 쓰고, 오른쪽에 해석을 쓰세요. 아래 ✎ 칸에는 숨은 뜻을 정리하세요.', '원문은 학교 프린트 3쪽 표로 확인 · 오른쪽 해석 칸에는 장면 요약을 실음 · 빨간 글씨 = 모범 답')
    return h

if __name__ == '__main__' and 'answer' in sys.argv:
    O = '/home/claude/work/m3pb/'
    a = answer(); open(O + 'baekji_answer.html', 'w', encoding='utf-8').write(a); pdf(a, O + '중산중3_외부지문_PictureBride_백지노트_답지.pdf')
