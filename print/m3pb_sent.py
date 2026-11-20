# 11/20 11:09 Picture Bride 교사용 문장 단위 구조 분석 (원문 없이 행 번호로) — 프린트 2쪽 시 34행 기준
# 문장 5개: S1 1~3행 · S2 4~6행 앞 · S3 6행(And)~22행 · S4 23~24행 앞 · S5 24행(And when)~34행
import sys, html
sys.path.insert(0, '/home/claude/srcrepo/print')
from m3pb_make import pdf
esc = html.escape
# 노드: (행, 라벨, 설명, 뜻, 깊이, 종류) 종류 m=주절 s=종속절 p=구
S = [
 dict(no=1, ln='1~3행', title='할머니의 나이', kind='평서문 (2형식)', parts='Part 1 · 칸 1',
      tree=[('1행', '주절', '주어(She) + was + 숫자 + 비교급(younger)', '그녀는 한 살 더 어렸다', 0, 'm'),
            ('2행', 'than + 비교 대상', 'than + 주격 대명사 (뒤 be동사 생략)', '나보다', 1, 'p'),
            ('3행', '보충 설명(나이)', '숫자(twenty-three) — 앞 문장의 보어를 덧붙임', '스물셋이었다', 0, 'p'),
            ('3행', 'when 부사절', 'when + 주어(she) + 과거동사 + 목적어(Korea)', '한국을 떠났을 때', 1, 's')],
      gist='그녀는 나보다 한 살 어렸고, 한국을 떠날 때 스물셋이었다.',
      exam=['than 뒤: 주격 I (= than I was) — 구어체 me와 비교해 출제 가능', '화자 나이 추론: 23 + 1 = 24세', '나이 표현을 콤마로 덧붙인 구조 (= She was twenty-three when ~)'],
      hid='화자가 지금 할머니가 떠난 나이와 같다 → 공감하며 시작'),
 dict(no=2, ln='4~6행 앞', title='문을 닫고 떠났을까', kind='의문문 (마침표로 끝남)', parts='Part 1 · 칸 2',
      tree=[('4행', '주절(의문문)', 'Did + 주어(she) + 부사(simply) + 동사원형(close)', '그녀는 그저 닫았을까', 0, 'm'),
            ('5행', '목적어', '명사(the door) + of + 소유격 명사(아버지의 집)', '아버지 집의 문을', 1, 'p'),
            ('6행', '병렬 동사', 'and + 동사원형(walk away) — Did에 함께 걸림', '그리고 걸어 나갔을까', 0, 'm')],
      gist='그녀는 그저 아버지 집의 문을 닫고 걸어 나왔을까.',
      exam=['Did + 주어 + 동사원형 ~ and 동사원형: walked(X)', '부사 simply 위치: 주어 뒤, 동사원형 앞', '물음표 대신 마침표 — 대답을 바라지 않는 혼잣말 같은 물음(시적 표현)'],
      hid='\'그저\' — 그렇게 쉬웠을 리 없다는 마음, 이별의 무게'),
 dict(no=3, ln='6행 And ~ 22행', title='부두에서 섬, 기다리는 남자, 빛나는 방까지 (가장 긴 문장)', kind='의문문 1개에 관계사·분사·부사절이 겹겹이', parts='Part 1 칸 3~4 → Part 2 칸 5~7',
      tree=[('6~7행', '주절(의문문)', 'And + was + it(비인칭: 거리) + a long way', '먼 길이었을까', 0, 'm'),
            ('8행', '경로', 'through + 장소(부산의 양복점들)', '부산의 양복점 거리를 지나', 1, 'p'),
            ('9행', '도착점', 'to + 장소(부두 the wharf)', '부두까지', 1, 'p'),
            ('9~10행', 'where 관계부사절 ← 선행사 부두', '주어(배) + waited + to부정사(목적: 데려가려고) + to + 장소(an island)', '그곳에서 배가 그녀를 한 섬으로 데려가려고 기다렸다', 2, 's'),
            ('11~12행', 'whose 관계사절 ① ← 선행사 an island', 'whose + 명사(이름) + 주어(she) + had (only recently) learned', '그 섬의 이름을 그녀는 최근에야 알게 되었다', 3, 's'),
            ('13~14행', 'on whose 관계사절 ② ← 선행사 an island', '전치사 on + whose + 명사(해안) + 주어(a man) + waited', '그 섬의 해안에서는 한 남자가 기다렸다', 3, 's'),
            ('15~16행', '분사구문(동시동작) ← 주어 a man', 'turning + 목적어(그녀의 사진) + to the light', '그녀의 사진을 빛 쪽으로 돌려 보며', 4, 'p'),
            ('16~18행', 'when 부사절 ①', '주어(등불들) + 장소 수식(17~18행: 숙소 · 설탕 공장 밖) + were lit (수동)', '설탕 공장 밖 숙소의 등불이 켜질 때', 4, 's'),
            ('19~20행', 'and절 — when절 ② 또는 새 물음', 'and + 주어(그의 방 안) + grew + 형용사(luminous) — 2형식', '그리고 그의 방 안이 환해졌을까 (학교 프린트 해석)', 4, 's'),
            ('21행', '원인', 'from + 명사(나방들의 날개)', '나방들의 날개 때문에', 5, 'p'),
            ('22행', '현재분사 후치 수식 ← 나방들', 'migrating + out of + 장소(사탕수수 줄기)', '사탕수수 줄기에서 나와 날아다니는', 6, 'p')],
      gist='부산의 양복점 거리를 지나, 이름을 최근에야 안 섬으로 그녀를 데려갈 배가 기다리던 부두까지 가는 길은 멀었을까 — 그 섬의 해안에서는 숙소의 등불이 켜질 무렵 한 남자가 그녀의 사진을 빛에 비춰 보며 기다렸고, 나방 날개 때문에 그의 방 안은 환해졌을까.',
      exam=['두 whose절의 선행사는 모두 an island (11~12행 이름 · 13행 해안) — 선행사 찾기 문제', 'where의 선행사 = the wharf (관계부사 + 완전한 절) ↔ which(X)', 'had learned: 섬으로 떠나기 전에 이미 알게 된 일 (과거완료)', 'turning의 의미상 주어 = a man (그녀 X)', 'were lit: light – lit – lit, 등불이 \'켜지는\' 수동 ↔ lighted up(X)', 'grew + luminous(형용사) ↔ luminously(X)', 'migrating ← moths 수식 (능동 현재분사) ↔ migrated(X)', '19~20행 and절: 문법상 when절에 이어진다고 볼 수도, 따로 묻는 말로 볼 수도 있음 — 학교 프린트 해석은 \'방 안은 환해졌을까?\' (시험은 학교 해석 기준)', '해석 순서: 주절(먼 길이었을까) → 경로·도착점 → 부두를 꾸미는 where절 → 섬을 꾸미는 whose절 2개 → 남자를 꾸미는 분사구문·when절'],
      hid='Part 1(떠남)에서 Part 2(기다리는 남자)로 한 문장 안에서 장면이 바뀐다 — 바다 건너 두 사람의 장면이 한 문장으로 이어짐'),
 dict(no=4, ln='23~24행 앞', title='무엇을 가져갔을까', kind='의문사 의문문', parts='Part 3 · 칸 8',
      tree=[('23행', '의문사 + 명사', 'What + 명사(things)', '어떤 물건들을', 0, 'm'),
            ('23~24행', '조동사 + 주어 + 동사원형', 'did + 주어(my grandmother) + take + with + 대명사(her)', '할머니는 가지고 갔을까', 0, 'm')],
      gist='할머니는 어떤 물건들을 가지고 갔을까?',
      exam=['What + 명사 + did + 주어 + 동사원형: took(X)', 'take A with + 사람 = A를 가지고 가다', '이 문장에서 처음으로 my grandmother — 화자가 손녀임이 드러남'],
      hid='화자는 답을 모른다 — 시 전체가 질문인 이유'),
 dict(no=5, ln='24행 And when ~ 34행', title='낯선 남편과의 첫 만남, 바람에 부푼 치마', kind='부사절 + 의문문 주절 + 독립분사구문', parts='Part 3 · 칸 9~11',
      tree=[('24~25행', 'when 부사절', 'And when + 주어(she) + arrived', '그리고 그녀가 도착했을 때', 0, 's'),
            ('25~26행', 'to부정사(목적)', 'to look into + 명사(낯선 사람의 얼굴)', '낯선 사람의 얼굴을 들여다보려고', 1, 'p'),
            ('27행', 'who 관계사절 ← 선행사 the stranger', 'who + was + 보어(her husband)', '그녀의 남편인', 2, 's'),
            ('28행', '덧붙인 형용사구 ← the stranger', '숫자 + years + 비교급(older) + than + 주격(she)', '그녀보다 열세 살 많은', 2, 'p'),
            ('29~30행', '주절(의문문)', 'did + 주어(she) + 부사(politely) + 동사원형(untie) + 목적어(저고리의 비단 고름)', '그녀는 예의 바르게 고름을 풀었을까', 0, 'm'),
            ('31~32행', '독립분사구문 (주어가 달라 명사를 남김)', '명사(그녀의 텐트 모양 치마) + filling with + 명사(건조한 바람)', '치마가 건조한 바람으로 가득 부풀면서', 1, 'p'),
            ('33행', 'that 관계사절 ← 선행사 바람', 'that + blew + from + 장소(주변 들판)', '주변 들판에서 불어온', 2, 's'),
            ('34행', 'where 관계부사절 ← 선행사 들판', 'where + 주어(the men) + were burning (과거진행) + 목적어(사탕수수)', '남자들이 사탕수수를 태우고 있던', 3, 's')],
      gist='그리고 그녀가 도착해 열세 살 많은 낯선 사람, 곧 남편의 얼굴을 들여다볼 때, 그녀는 예의 바르게 저고리의 비단 고름을 풀었을까 — 남자들이 사탕수수를 태우던 주변 들판에서 불어온 건조한 바람에 텐트 모양의 치마가 부풀어 오르는 가운데.',
      exam=['주절은 29행 did she ~ (24~28행은 모두 when절) — 주절 찾기 문제', 'who의 선행사 = the stranger · 28행도 the stranger를 보충 (남편 = 낯선 사람 = 13살 연상)', 'than she: 주격 (= than she was)', '독립분사구문: 의미상 주어(치마) ≠ 주절 주어(she)라서 명사를 남김 · filled(X) — 치마가 바람으로 \'가득 차는\' 능동', 'that의 선행사 = 바람 / where의 선행사 = 들판 (관계부사 + 완전한 절)', 'were burning: 그때 진행 중이던 일 (과거진행)'],
      hid='\'남편인 낯선 사람\'의 아이러니, 건조한 바람·불타는 사탕수수 = 앞으로의 거친 노동 현실'),
]
CSS = open('/home/claude/srcrepo/print/m3rf7_analysis.html', encoding='utf-8').read()
CSS = CSS[CSS.index('<style>'):CSS.index('</style>') + 8]
EX = '''<style>
h2{break-after:avoid}
.tree{margin:6px 0 8px}
.nd{display:grid;grid-template-columns:62px 1fr 34%;gap:8px;align-items:start;border-bottom:1px solid #eee;padding:3px 0;font-size:12px}
.nd .l{font-weight:700;color:#26364a;font-variant-numeric:tabular-nums}
.nd .b{border-left:3px solid #aaa;padding-left:7px}
.nd.m .b{border-color:#1d2430}.nd.s .b{border-color:#c8372d}.nd.p .b{border-color:#13808a}
.nd .lab{font-weight:700}.nd.m .lab{color:#1d2430}.nd.s .lab{color:#c8372d}.nd.p .lab{color:#13808a}
.nd .d{color:#333;font-family:var(--serif)}
.nd .k{color:#555}
.lgd span{margin-right:14px;font-size:11.5px}
.hid{background:#fdf0e8;border-left:4px solid var(--red);padding:4px 10px;margin:4px 0;font-size:12px}.hid b{color:var(--red);margin-right:6px}
.srcbox{background:#eef1f5;border:1px dashed #8a97a8;border-radius:4px;padding:4px 10px;font-size:12px;margin:4px 0}
</style>'''
def card(s):
    rows = ''.join('<div class="nd %s"><span class="l">%s</span><div class="b" style="margin-left:%dpx"><span class="lab">%s</span><br><span class="d">%s</span></div><span class="k">%s</span></div>' % (k, esc(l), dp * 14, esc(lab), esc(d), esc(m)) for l, lab, d, m, dp, k in s['tree'])
    return ('<article class="card"><header class="ch"><span class="num">S%d</span><span class="pt">%s</span><ul><li>%s</li><li>%s</li></ul><span class="flow">%s</span></header><div class="body">'
            '<div class="srcbox"><b>원문</b> 프린트 2쪽 시 %s (선생님 프린트와 함께 보세요)</div>'
            '<div class="tree">%s</div><p class="tr"><b>문장 뜻</b> %s</p><div class="hid"><b>숨은 뜻</b>%s</div>'
            '<div class="gram"><b>시험 포인트</b><ul>%s</ul></div></div></article>') % (
        s['no'], esc(s['ln']), esc(s['title']), esc(s['kind']), esc(s['parts']), esc(s['ln']), rows, esc(s['gist']), esc(s['hid']), ''.join('<li>%s</li>' % esc(x) for x in s['exam']))
def build():
    ov = ''.join('<tr><td>S%d</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>' % (s['no'], esc(s['ln']), esc(s['title']), esc(s['kind']), esc(s['parts'])) for s in S)
    return ('<!DOCTYPE html><html lang="ko"><head><meta charset="utf-8"><title>Picture Bride 문장 단위 구조 분석 (교사용)</title>%s%s</head><body><div class="wrap">' % (CSS, EX) +
        '<div class="top"><h1>「Picture Bride」 <small>문장 단위 구조 분석 · 교사용</small></h1>'
        '<div class="meta">Cathy Song · 원문은 학교 프린트 2쪽(시 34행)의 행 번호로 표시 · 34행이지만 문장은 5개</div></div>'
        '<div class="legend lgd"><span><b style="color:#1d2430">■ 주절</b></span><span><b style="color:#c8372d">■ 종속절(관계사·부사절)</b></span><span><b style="color:#13808a">■ 구(분사·to부정사·전치사구)</b></span><span>들여쓰기 = 앞 줄을 꾸미거나 보충함</span></div>'
        '<section class="block"><h2>문장 5개 한눈에</h2><div class="tbl"><table><tr><th>문장</th><th>행</th><th>내용</th><th>형식</th><th>프린트 칸</th></tr>' + ov + '</table></div>'
        '<p class="meta">행 번호 세는 법: 프린트 2쪽 시의 첫 줄 = 1행, 마지막 줄(사탕수수를 태우던 들판) = 34행. S2·S3, S4·S5는 같은 행(6행·24행)의 And에서 나뉨</p></section>'
        '<section class="block"><h2>문장별 구조</h2>' + ''.join(card(s) for s in S) + '</section></div></body></html>')
if __name__ == '__main__':
    h = build(); open('/home/claude/work/m3pb/sent.html', 'w', encoding='utf-8').write(h)
    pdf(h, '/home/claude/work/m3pb/중산중3_외부지문_PictureBride_문장구조_교사용.pdf')
