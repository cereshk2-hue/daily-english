# 11/22 저동고1 능률(민병천) 3·4과 본문 서술형 10문항 — print/m3sw_make.py(중산중3) 형식 그대로, 고1 수준·학교 기출 서술형 유형(재구성 빈칸·연결어·n단어 조건 영작) 반영
import re, html, sys, os
os.makedirs('/home/claude/out/jdsw', exist_ok=True)
OUT = '/home/claude/out/jdsw/'
E = html.escape
Q = [
 dict(tag='3과 본문 ❶', gram='목적격 관계대명사 that · used to', title='다음 우리말을 &lt;조건&gt;에 맞게 영작하시오.',
      box=['Keller가 상을 받은 자신의 책을 쓰게 된 영감은 그녀의 할머니가 그녀에게 들려주곤 했던 옛 민담이었다.'],
      cond=["Keller's로 시작할 것", 'inspiration, award-winning, folktale, that, use, tell을 쓰되 필요하면 형태를 바꿀 것', "17단어로 쓸 것(Keller's, award-winning은 각 1단어)"],
      parts=[('', 2)],
      ans=["Keller's inspiration for her award-winning book was an old folktale that her halmoni(grandmother) used to tell her."],
      pts=['inspiration for her award-winning book(~에 대한 영감)', '선행사 an old folktale + 목적격 관계대명사 that', 'used to + 동사원형(~하곤 했다) — use를 used to로 바꾸기']),
 dict(tag='3과 본문 ❷❸', gram='It is estimated / It seems that ~ → 주어 + be p.p. / seem + to have p.p.', title='다음 두 문장의 의미가 같도록 빈칸에 알맞은 말을 쓰시오.',
      box=[], cond=[],
      parts=[('(1) It is estimated that tigers lived in Korea for at least 100,000 years.<br>= <span class="en">Tigers ______________________ in Korea for at least 100,000 years.</span>', 1),
             ('(2) It seems that people at the time had conflicting feelings about tigers.<br>= <span class="en">People at the time ______________________ conflicting feelings about tigers.</span>', 1)],
      ans=['(1) are estimated to have lived', '(2) seem to have had'],
      pts=['that절 주어를 문장 주어로 → 동사는 to부정사로', 'that절 시제(lived, had)가 주절(is, seems)보다 앞섬 → 완료부정사 to have p.p.', '(1) 주절이 수동(is estimated) → are estimated(주어 Tigers 복수)']),
 dict(tag='3과 본문 ❷❸', gram='현재분사 수식 · 부분 표현 수 일치 · 동명사 주어', title='다음 글에서 어법상 <u>틀린</u> 부분 3개를 찾아 바르게 고쳐 쓰시오.',
      box=['Since then, tigers have appeared in many aspects of Korean culture, from legends to art and musical instruments. Some of you may have heard Korean folktales featured tigers. '
           'In fact, approximately forty percent of Korean folktales about animals includes a tiger. Tigers in Korean folktales are sometimes shown in a positive light and sometimes as foolish creatures. (…) '
           'They had respect for tigers\' power and courage. However, they were also scared of tigers because being injured or even killed by tigers were common in the past.'],
      cond=[], parts=[('(1) ________ → ________', 1), ('(2) ________ → ________', 1), ('(3) ________ → ________', 1)],
      ans=['(1) featured → featuring (호랑이가 \'등장하는\' 민담 — 능동의 현재분사)', '(2) includes → include (percent of + 복수 명사 folktales → 복수 동사)', '(3) were → was (동명사구 주어 being injured ~ by tigers는 단수)'],
      pts=['folktales featuring tigers: 민담이 호랑이를 \'등장시키는\' 능동', '분수·퍼센트 of + 명사 → 명사에 수 일치', '동명사 주어 → 단수 동사']),
 dict(tag='3과 본문 ❸', gram='재구성 빈칸 · 품사 바꾸기(명사 → 동사)', title='다음 글은 본문 ❸을 재구성한 것이다. 빈칸 (A)~(C)에 들어갈 말을 &lt;조건&gt;에 맞게 쓰시오.',
      box=['Long ago, Korean people (A) ________ tigers for their power and courage, but at the same time they were afraid of them. Later, the number of tigers (B) ________ sharply because of hunting, and tigers nearly disappeared from Korea. '
           'In modern times, however, tigers were (C) ________ as the mascots of the Olympics held in Korea, and this brought their symbolism back to life.'],
      cond=['본문 ❸에 \'명사\'로 쓰인 단어를 찾아 문맥에 맞게 형태를 바꿀 것', '각각 한 단어'],
      parts=[('(A) ____________ &nbsp;&nbsp; (B) ____________ &nbsp;&nbsp; (C) ____________', 1)],
      ans=['(A) respected (← respect)', '(B) declined (← decline)', '(C) selected (← selection)'],
      pts=['(A) had respect for → respected(과거)', '(B) faced a decline in population → declined(자동사, 과거)', '(C) through their selection as the mascot → were selected(수동태)']),
 dict(tag='3과 본문 ❺', gram='현재완료 수동 + to be -ing · 수사의문문', title='다음 물음에 답하시오.',
      box=[], cond=[],
      parts=[('(1) 다음 우리말을 &lt;조건&gt;에 맞게 영작하시오.<br>요즘에는 단지 몇 마리의 야생 호랑이만이 북한에 살고 있다고 보고되어 왔다.<br><span class="cond">조건: These days, 뒤에 이어지는 14단어 · only a few, wild, report, live를 쓰되 형태를 바꿀 것 · 현재완료 수동태와 진행형 to부정사를 쓸 것</span>', 2),
             ('(2) 다음 문장과 의미가 같도록 No one으로 시작하는 평서문으로 바꿔 쓰시오.<br><span class="en">Who can deny that the tiger is a symbol of Korea?</span>', 2)],
      ans=['(1) (These days,) only a few wild tigers have been reported to be living in North Korea.', '(2) No one can deny that the tiger is a symbol of Korea.'],
      pts=['(1) 현재완료 수동 have been reported', '(1) to be living(살고 있다는 것 — 진행형 부정사)', '(2) 수사의문문 Who can ~? = No one can ~ (No one can\'t ❌)']),
 dict(tag='4과 본문 ❶', gram='with + 목적어 + 분사 · 진행형 수동태 · stop A from -ing', title='다음 우리말을 &lt;조건&gt;에 맞게 영작하시오.',
      box=[], cond=[],
      parts=[('(1) 지구가 더 따뜻해지면서, 해수면이 상승하고 있다.<br><span class="cond">조건: With로 시작 · the planet, become, warm, sea levels, rise를 쓰되 형태를 바꿀 것 · 9단어</span>', 2),
             ('(2) 우리가 기후 변화가 위험한 수준에 이르는 것을 막을 수 있을까?<br><span class="cond">조건: Can으로 시작 · stop, climate change, reach, dangerous levels를 쓰되 형태를 바꿀 것 · 9단어</span>', 2)],
      ans=['(1) With the planet becoming warmer, sea levels are rising.', '(2) Can we stop climate change from reaching dangerous levels?'],
      pts=['(1) with + 목적어(the planet) + 현재분사 becoming(~하면서)', '(1) become + 비교급 warmer / 현재진행 are rising', '(2) stop A from -ing(A가 ~하는 것을 막다) → from reaching']),
 dict(tag='4과 본문 ❷', gram='부분 표현 수 일치 · 간접의문문 · 현재완료 수동', title='다음 글에서 어법상 <u>틀린</u> 부분 3개를 찾아 바르게 고쳐 쓰시오.',
      box=['About fifty percent of plastic are produced for single-use products. That means the items are used just once and then discarded. Do you ever stop to think about where do these plastic items go after you throw them away? '
           'Recycling can help reduce the amount of plastic in our landfills. However, less than ten percent of the world\'s plastic waste has recycled so far.'],
      cond=[], parts=[('(1) ________ → ________', 1), ('(2) ________ → ________', 1), ('(3) ________ → ________', 1)],
      ans=['(1) are → is (percent of + 셀 수 없는 명사 plastic → 단수 동사)', '(2) do these plastic items go → these plastic items go (간접의문문: 의문사 + 주어 + 동사)', '(3) has recycled → has been recycled (쓰레기가 \'재활용되는\' 수동)'],
      pts=['percent of + 명사 → 명사에 수 일치(plastic 단수)', '전치사 about의 목적어인 간접의문문 어순', '주어 plastic waste가 동작을 받음 → 현재완료 수동 has been p.p.']),
 dict(tag='4과 본문 ❷', gram='전치사 + 관계대명사 · help + 목적어 + 동사원형 · keep + 목적어 + 형용사', title='다음 물음에 답하시오.',
      box=[], cond=[],
      parts=[('(1) 두 문장을 &lt;조건&gt;에 맞게 한 문장으로 쓰시오.<br><span class="en">They also want to speed up the process. The bacteria break down plastic by the process.</span><br><span class="cond">조건: 전치사 + 관계대명사를 쓸 것</span>', 2),
             ('(2) 다음 우리말을 &lt;조건&gt;에 맞게 영작하시오.<br>이것은 우리가 매립지를 플라스틱이 없는 상태로 유지하도록 도울지도 모른다.<br><span class="cond">조건: may, help, keep, landfills, plastic-free를 쓸 것 · 8단어(plastic-free는 1단어)</span>', 2)],
      ans=['(1) They also want to speed up the process by which the bacteria break down plastic.', '(2) This may help us keep our landfills plastic-free.'],
      pts=['(1) by the process → by which(전치사를 관계대명사 앞으로, that ❌)', '(2) help + 목적어(us) + 동사원형(keep)', '(2) keep + 목적어(our landfills) + 형용사(plastic-free)']),
 dict(tag='4과 본문 ❸', gram='연결어 · 조동사 수동태 · 간접의문문', title='다음 글을 읽고 물음에 답하시오.',
      box=['Although polluted soil can be dug up and transported to a landfill, this process is expensive. (A) ________, it only moves the problem to another area and does not really solve it. (…) '
           'Research on the effectiveness of using willow trees for this purpose is in development. Scientists have found that some species of willow trees are able to absorb harmful materials better than others. '
           '(B) ________, (C) <u>이 유망한 분야는 어떤 나무가 가장 효과적인지 알아내기 위해 더 탐구되어야 한다.</u>'],
      cond=[],
      parts=[('(1) 빈칸 (A), (B)에 들어갈 알맞은 연결어를 각각 쓰시오. (A) __________ &nbsp; (B) __________', 1),
             ('(2) 밑줄 친 (C)를 &lt;조건&gt;에 맞게 영작하시오.<br><span class="cond">조건: this promising area로 시작 · should, further, explore, find out, which, effective를 쓰되 형태를 바꿀 것 · 16단어</span>', 2)],
      ans=['(1) (A) Moreover (= Furthermore, In addition, Besides) (B) Therefore (= Thus, So)', '(2) This promising area should be further explored to find out which trees are the most effective.'],
      pts=['(A) 비싸다 + 문제를 옮길 뿐 → 첨가(Moreover)', '(B) 종마다 효과가 다르다 → 그러므로(Therefore) 더 연구', '(2) 조동사 수동 should be explored / 목적 to find out / 간접의문문 which trees are']),
 dict(tag='4과 본문 ❹', gram='계속적 용법 which · 수동태 · by + 동명사', title='다음 물음에 답하시오.',
      box=[], cond=[],
      parts=[('(1) 다음 우리말을 &lt;조건&gt;에 맞게 영작하시오.<br>커피를 만드는 과정은 사용된 커피 찌꺼기를 만들어 내는데, 그것들은 보통 매립지로 보내진다.<br><span class="cond">조건: 관계대명사의 계속적 용법과 수동태를 쓸 것 · coffee-making, generate, used coffee grounds, normally, send를 쓸 것 · 13단어</span>', 2),
             ('(2) 다음 질문에 본문의 내용을 바탕으로 by를 써서 완전한 영어 문장으로 답하시오.<br><span class="en">Q: How can we reduce greenhouse gas emissions from used coffee grounds?</span>', 2)],
      ans=['(1) The coffee-making process generates used coffee grounds, which are normally sent to landfills.', '(2) We can reduce them(greenhouse gas emissions) by turning used coffee grounds into biofuel.'],
      pts=['(1) 콤마 + which(계속적 용법, that ❌)', '(1) 찌꺼기가 \'보내지는\' → are sent(수동태)', '(2) by + 동명사 turning / turn A into B(A를 B로 바꾸다)']),
]
assert len(Q) == 10

CSS = '''
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700;900&family=Noto+Serif:wght@400;700&display=swap');
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'Noto Sans KR',sans-serif;color:#1d2433;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.en,.box{font-family:'Noto Serif',serif}
.navy{background:#1f3a5f;color:#fff}
'''
A4 = CSS + '''
@page{size:A4;margin:11mm 12mm}
body{font-size:12.5px;line-height:1.6}
.head{display:flex;justify-content:space-between;align-items:flex-end;border-bottom:3px solid #1f3a5f;padding-bottom:6px;margin-bottom:10px}
.head h1{font-size:20px;font-weight:900;color:#1f3a5f}.head .sub{font-size:11.5px;color:#556}
.who{display:flex;gap:6px;font-size:12px}.who span{border:1px solid #99a;padding:3px 10px;min-width:70px}
.note{background:#eef3f9;border-left:4px solid #1f3a5f;padding:6px 10px;margin-bottom:10px;font-size:11.5px}
.q{break-inside:avoid;margin-bottom:12px;border:1px solid #c9d3e0;border-radius:6px;overflow:hidden}
.qh{display:flex;gap:8px;align-items:center;padding:5px 10px;font-weight:700;font-size:13px}
.qh .no{background:#fff;color:#1f3a5f;border-radius:50%;width:22px;height:22px;display:flex;align-items:center;justify-content:center;font-weight:900}
.qh .tag{font-size:10.5px;font-weight:500;opacity:.85;margin-left:auto}
.qb{padding:8px 11px}
.title{font-weight:700;margin-bottom:5px}
.box{border:1px solid #9aa7b8;background:#fafbfd;padding:7px 10px;margin:5px 0;font-size:13px;line-height:1.65}
.condbox{border:1px dashed #1f3a5f;padding:4px 10px;margin:5px 0;font-size:11.5px}
.cond{display:inline-block;font-size:11.5px;color:#1f3a5f;margin-top:2px}
.part{margin-top:6px}.part .en{font-size:13px}
.line{border-bottom:1px solid #8a94a6;height:25px}
.gram{font-size:10.5px;color:#667;margin-top:4px}
.ans{color:#c0262d;font-weight:700;font-family:'Noto Serif',serif;font-size:13px;margin:3px 0}
.pt{font-size:11.5px;color:#334;margin-top:3px}.pt b{color:#1f3a5f}
.pb{break-before:page}
'''
SC = CSS + '''
@page{size:1280px 720px;margin:0}
.s{width:1280px;height:720px;padding:38px 56px;break-after:page;position:relative;overflow:hidden;background:#fff}
.s .top{display:flex;align-items:center;gap:16px;margin-bottom:18px}
.s .no{background:#1f3a5f;color:#fff;font-weight:900;font-size:30px;border-radius:12px;padding:4px 18px}
.s .tag{font-size:20px;color:#1f3a5f;font-weight:700}.s .gram{margin-left:auto;font-size:17px;color:#667}
.s .title{font-size:26px;font-weight:700;margin-bottom:12px}
.s .box{border:2px solid #9aa7b8;background:#fafbfd;padding:14px 20px;font-size:22px;line-height:1.6;margin-bottom:12px}
.s .condbox{border:2px dashed #1f3a5f;padding:8px 18px;font-size:19px;margin-bottom:10px}
.s .part{font-size:22px;line-height:1.55;margin-bottom:12px}.s .part .en{font-size:23px}
.s .cond{font-size:18px;color:#1f3a5f}
.s.a{background:#fff8f8}.s .ans{color:#c0262d;font-weight:700;font-family:'Noto Serif',serif;font-size:27px;line-height:1.5;margin-bottom:10px}
.s .pt{font-size:20px;margin-top:8px;color:#334}.s .pt b{color:#1f3a5f}
.s .foot{position:absolute;bottom:16px;right:56px;font-size:15px;color:#99a}
.cover{display:flex;flex-direction:column;justify-content:center;align-items:center;background:#1f3a5f;color:#fff}
.cover h1{font-size:54px;font-weight:900;margin-bottom:18px}.cover p{font-size:24px;opacity:.9}
'''
def qbody(q, scr=False):
    o = '<div class="title">%s</div>' % q['title']
    for b in q['box']: o += '<div class="box">%s</div>' % b
    if q['cond']: o += '<div class="condbox">&lt;조건&gt; ' + ' · '.join(q['cond']) + '</div>'
    for t, n in q['parts']:
        o += '<div class="part">%s%s</div>' % (t, '' if scr else ''.join('<div class="line"></div>' for _ in range(n)))
    return o

def a4(answer):
    h = '<!doctype html><html><head><meta charset="utf-8"><style>%s</style></head><body>' % A4
    h += '<div class="head"><div><h1>저동고1 3·4과 본문 서술형%s</h1><div class="sub">공통영어2 능률(민병천) Lesson 3 A Timeless Symbol of Korea · Lesson 4 Looking to Nature for Help · 10문항</div></div>' % (' — 정답과 채점 포인트' if answer else '')
    h += '<div class="who"><span>번호</span><span>이름</span></div></div>' if not answer else '</div>'
    if not answer: h += '<div class="note">본문에서 문법이 가장 많이 걸린 문장만 골랐어요. 단어 수·형태 변화 조건을 끝까지 지키고, 철자·대소문자·마침표까지 정확히 쓰세요. (하이픈으로 이어진 말은 한 단어)</div>'
    for i, q in enumerate(Q, 1):
        h += '<div class="q"><div class="qh navy"><span class="no">%d</span>%s<span class="tag">%s</span></div><div class="qb">' % (i, q['gram'], q['tag'])
        if answer:
            h += '<div class="title" style="font-weight:500;color:#556">%s</div>' % re.sub('<br>.*', '', q['title'])
            for a in q['ans']: h += '<div class="ans">%s</div>' % a
            h += '<div class="pt"><b>채점 포인트</b> ' + ' / '.join(q['pts']) + '</div>'
        else:
            h += qbody(q)
        h += '</div></div>'
    return h + '</body></html>'

def screen():
    h = '<!doctype html><html><head><meta charset="utf-8"><style>%s</style></head><body>' % SC
    h += '<div class="s cover"><h1>3·4과 본문 서술형</h1><p>저동고 1학년 · 능률(민병천) Lesson 3·4 · 10문항</p><p style="margin-top:30px;font-size:20px">문제 → 다음 장 정답</p></div>'
    for i, q in enumerate(Q, 1):
        top = '<div class="top"><span class="no">%d</span><span class="tag">%s</span><span class="gram">%s</span></div>' % (i, q['tag'], q['gram'])
        h += '<div class="s">%s%s<div class="foot">서술형 %d / 10</div></div>' % (top, qbody(q, True), i)
        a = ''.join('<div class="ans">%s</div>' % x for x in q['ans'])
        a += '<div class="pt"><b>채점 포인트</b><br>' + '<br>'.join('· ' + p for p in q['pts']) + '</div>'
        h += '<div class="s a">%s<div class="title">정답</div>%s<div class="foot">서술형 %d 정답</div></div>' % (top, a, i)
    return h + '</body></html>'

if __name__ == '__main__':
    from playwright.sync_api import sync_playwright
    files = {'서술형_시험지': a4(False), '서술형_정답': a4(True), '서술형_화면용': screen()}
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page()
        for name, doc in files.items():
            hp = '/home/claude/work/jdsw_%s.html' % name; open(hp, 'w', encoding='utf-8').write(doc)
            pg.goto('file://' + hp); pg.wait_for_timeout(1200)
            if name == '서술형_화면용': pg.pdf(path=OUT + '저동고1_3·4과_본문_' + name + '.pdf', width='1280px', height='720px', print_background=True)
            else: pg.pdf(path=OUT + '저동고1_3·4과_본문_' + name + '.pdf', format='A4', print_background=True, prefer_css_page_size=True)
        b.close()
    print('ok')
