# 11/22 중산중3 7·8과 서술형 최종 점검 (10문항, 한 세트) — 본문에서 문법이 가장 많이 걸린 문장 + 외부지문(일본 가옥·Picture Bride)
# 출력: /home/claude/out/m3fin/ 서술형_시험지.pdf(A4, 문제+답 칸) · 서술형_정답.pdf(A4) · 서술형_화면용.pdf(16:9, 문제 → 정답 순)
# Picture Bride는 시 원문 없이(4단어 이상 겹침 검사 — gen_m3pb.POEM)
import re, html, sys
OUT = '/home/claude/out/m3fin/'
E = html.escape
Q = [
 dict(tag='7과 본문 ❶', gram='가정법 과거 · to부정사(목적)', title='다음 우리말을 &lt;조건&gt;에 맞게 영작하시오.',
      box=['만약 내가 푸에블로에 산다면, 나는 집에 들어가기 위해 사다리를 오를 것이다.'],
      cond=['가정법 과거로 쓸 것', 'live, pueblo, climb up, ladder, enter를 쓰되 필요하면 형태를 바꿀 것', '16단어로 쓸 것'],
      parts=[('', 2)],
      ans=['If I lived in a pueblo, I would climb up a ladder to enter my house.'],
      pts=['If + 과거형 lived', '주절 would + 동사원형 climb', '목적(~하기 위해) to enter']),
 dict(tag='7과 본문 ❷❸', gram='가정법 과거 전환', title='다음 문장을 가정법 과거 문장으로 바꿔 쓰시오.',
      box=[], cond=[],
      parts=[('(1) As I don\'t live in Venice, I can\'t take a gondola to school every morning.', 2), ('(2) As I am not in a tulou, I don\'t hear my neighbor calling me.', 2)],
      ans=['(1) If I lived in Venice, I could take a gondola to school every morning.', '(2) If I were in a tulou, I would hear my neighbor calling me.'],
      pts=['현재 사실의 반대 → 동사는 과거형(be동사는 were)', '긍정 ↔ 부정을 반대로(don\'t live → lived, can\'t → could)', '(2) 지각동사 hear + 목적어 + -ing는 그대로']),
 dict(tag='7과 본문 ❷', gram='수 일치 · 간접의문문 · keep + 목적어 + 형용사', title='다음 글에서 어법상 <u>틀린</u> 부분 3개를 찾아 바르게 고쳐 쓰시오.',
      box=['At high tide, the water from the Adriatic Sea often rise and leaves the streets full of water. However, I would be able to walk around the town through the raised walkways. '
           'Venice is known as the "floating city." In Venice, there are many colorful houses on the water. You may wonder how and why did they build the houses on the water. '
           'The old Venetians decided to live there to keep themselves safely from invaders. But it was not easy for them to build their homes on this swampy surface.'],
      cond=[], parts=[('(1) ________ → ________', 1), ('(2) ________ → ________', 1), ('(3) ________ → ________', 1)],
      ans=['(1) rise → rises (주어 the water는 단수)', '(2) did they build → they built (간접의문문: 의문사 + 주어 + 동사)', '(3) safely → safe (keep + 목적어 + 형용사)'],
      pts=['leaves와 짝: 주어 the water → rises', 'how and why + 주어 + 동사(과거) → they built', 'keep themselves safe(형용사 보어)']),
 dict(tag='7과 본문 ❷', gram='It ~ that 강조 · 가주어 it ~ for … to', title='다음 물음에 답하시오.',
      box=[], cond=[],
      parts=[('(1) 밑줄 친 부분을 강조하는 문장으로 바꿔 쓰시오.<br><span class="en"><u>These wooden poles</u> support Venice to this day.</span>', 2),
             ('(2) 다음 우리말을 영작하시오. (it, easy, for, build, swampy를 쓸 것)<br>그러나 그들이 이 늪 같은 표면 위에 집을 짓는 것은 쉽지 않았다.', 2)],
      ans=['(1) It is these wooden poles that support Venice to this day.', '(2) But it was not easy for them to build their homes on this swampy surface.'],
      pts=['(1) It is + 강조어 + that ~ / 강조되는 주어가 복수 → support', '(2) 가주어 It + was not easy + for 의미상 주어 + to부정사(진주어)', '(2) easy는 of가 아니라 for']),
 dict(tag='7과 본문 ❸', gram='지각동사 + 목적어 + -ing · 동명사 주어 · keep + 목적어 + 형용사', title='다음 물음에 답하시오.',
      box=[], cond=[],
      parts=[('(1) 우리말과 같도록 괄호 안의 말을 바르게 배열하시오.<br>나는 가끔 이웃이 차나 저녁을 먹으러 오라고 나를 부르는 소리를 들을 것이다.<br><span class="en">( calling / my neighbor / would / me / hear / sometimes / I ) to come over for tea or dinner.</span>', 2),
             ('(2) 다음 우리말을 &lt;조건&gt;에 맞게 영작하시오.<br>한 건물에서 함께 사는 것이 그들을 안전하게 지켜 준다.<br><span class="cond">조건: live, together, building, keep, safe를 쓰되 형태를 바꿀 것 · 동명사 주어 · 8단어</span>', 2)],
      ans=['(1) I would sometimes hear my neighbor calling me to come over for tea or dinner.', '(2) Living together in one building keeps them safe.'],
      pts=['(1) 빈도부사 sometimes는 조동사 would 뒤 / hear + 목적어 + -ing', '(2) 동명사구 주어 Living ~ building은 단수 → keeps', '(2) keep + them + safe(형용사)']),
 dict(tag='8과 본문 ❷❸', gram='too ~ to … ↔ so ~ that … can\'t', title='다음 문장을 [ ] 안의 지시대로 바꿔 쓰시오.',
      box=[], cond=[],
      parts=[('(1) He is so greedy that he can\'t share with the people. [too ~ to 구문으로]', 2), ('(2) It\'s too dangerous for you to stand there. [so ~ that 구문으로]', 2)],
      ans=['(1) He is too greedy to share with the people.', '(2) It\'s so dangerous that you can\'t stand there.'],
      pts=['too + 형용사 + to부정사 = so + 형용사 + that + 주어 + can\'t', '(2) 의미상 주어 for you → that절의 주어 you', '시제를 그대로(is → can\'t)']),
 dict(tag='8과 본문 ❶❷', gram='No one + 단수 동사 · decide + to부정사 · 지각동사', title='다음 글에서 어법상 <u>틀린</u> 부분 3개를 찾아 바르게 고쳐 쓰시오.',
      box=['Pascal was doing his math homework in his room. He was struggling with graphs. "It\'s too hard to read and draw graphs. Why do I need these anyway? No one need graphs in real life." '
           'He put down his pen and picked up his favorite book, <i>Robin Hood</i>. He decided reading himself to sleep. When he was about to open the book, he heard a voice. He looked up from the book to see who was talking. '
           '(…) Pascal closed his eyes and repeated the words. Suddenly, he heard men to shout.'],
      cond=[], parts=[('(1) ________ → ________', 1), ('(2) ________ → ________', 1), ('(3) ________ → ________', 1)],
      ans=['(1) need → needs (No one은 단수 취급)', '(2) reading → to read (decide + to부정사)', '(3) to shout → shouting 또는 shout (지각동사 hear + 목적어 + -ing/동사원형)'],
      pts=['No one / Nobody + 단수 동사', 'decide는 to부정사를 목적어로', 'hear·see + 목적어 + 동사원형/-ing (to부정사 ❌)']),
 dict(tag='8과 본문 ❹', gram='make + 목적어 + 형용사(비교급) · No one can ~ (전체 부정)', title='다음 우리말을 &lt;조건&gt;에 맞게 영작하시오.',
      box=[], cond=[],
      parts=[('(1) 그래프가 이것을 이해하기 더 쉽게 만들어 줄지도 몰라.<br><span class="cond">조건: might, make, easy, understand를 쓰되 필요하면 형태를 바꿀 것 · 8단어</span>', 2),
             ('(2) 이제 아무도 우리가 그것들(그래프)이 더 이상 필요 없다고 말할 수 없어.<br><span class="cond">조건: No one, say, need, anymore를 쓸 것 · Now로 시작</span>', 2)],
      ans=['(1) A graph might make this easier to understand.', '(2) Now no one can say that we don\'t need them anymore.'],
      pts=['(1) make + this + easier(형용사 비교급) + to understand', '(2) No one + can(긍정) — No one can\'t ❌(이중 부정)', '(2) graphs(복수) → them']),
 dict(tag='외부지문 · 일본 가옥', gram='수동태 · to부정사(목적) · keep + 목적어 + 형용사', title='다음 글을 읽고 물음에 답하시오.',
      box=['(…) Rooms are divided by <i>shoji</i>, portable sliding doors that are made from wood and thin paper. For large gatherings, these doors can be removed to create one large room. (…) '
           'In summer, heavy rain can cause flooding. (A) <u>바닥은 거주 공간을 홍수로부터 건조하고 안전하게 지키기 위해 땅에서 약간 높여져 있다.</u> The house also has sloped roofs because they keep rainwater flowing off easily.'],
      cond=[],
      parts=[('(1) 밑줄 친 (A)를 &lt;조건&gt;에 맞게 영작하시오.<br><span class="cond">조건: The floor of the house로 시작 · 수동태와 to부정사를 쓸 것 · raise, keep, dry, safe, flooding을 쓸 것</span>', 2),
             ('(2) 다음 질문에 윗글의 내용을 바탕으로 완전한 영어 문장으로 답하시오.<br><span class="en">Q: What can people do with the shoji for large gatherings?</span>', 2)],
      ans=['(1) The floor of the house is raised a little off the ground to keep the living area dry and safe from flooding.',
           '(2) They can remove the shoji (these doors) to create one large room.<br>(= The shoji can be removed to create one large room.)'],
      pts=['(1) 바닥이 \'높여지는\' → is raised(수동태)', '(1) 목적 to keep + 목적어 + 형용사 dry and safe', '(2) remove(떼어 내다) + 목적(to create one large room)']),
 dict(tag='외부지문 · Picture Bride', gram='관계대명사 who · 전치사 + 동명사 / 내용 서술', title='다음 물음에 답하시오. (학교 프린트의 시를 떠올리며)',
      box=[], cond=[],
      parts=[('(1) 다음 우리말을 &lt;조건&gt;에 맞게 영작하시오.<br>사진신부는 사진만 보고 한 남자와 결혼한 여자였다.<br><span class="cond">조건: A picture bride로 시작 · 관계대명사 who와 after + 동명사를 쓸 것 · only, photograph를 쓸 것</span>', 2),
             ('(2) 화자가 시 전체에서 할머니에 대해 계속 질문을 던지는 이유를 우리말로 쓰시오.', 3)],
      ans=['(1) A picture bride was a woman who married a man after seeing only his photograph.',
           '(2) 할머니가 겪은 일과 그때의 마음을 화자는 직접 알 수 없기 때문에, 질문을 던지며 (자신과 비슷한 나이였던) 할머니의 처지와 마음을 상상하고 이해하려고.'],
      pts=['(1) 선행사 a woman(사람) + who + 동사 married', '(1) 전치사 after + 동명사 seeing', '(2) 핵심어: 알 수 없음 → 상상 · 공감(이해)']),
]
assert len(Q) == 10

# 시 원문과 4단어 이상 겹침 검사
src = open('/home/claude/srcrepo/generators/gen_m3pb.py', encoding='utf-8').read()
POEM = re.search(r'POEM = """(.*?)"""', src, re.S).group(1)
_w = lambda t: re.findall(r"[a-z'\-]+", re.sub('<[^>]+>', ' ', t).lower())
pw = _w(POEM); G = set(tuple(pw[i:i + 4]) for i in range(len(pw) - 3))
alltxt = ' '.join(str(v) for q in Q[9:] for v in q.values())
w = _w(alltxt); bad = [' '.join(w[i:i + 4]) for i in range(len(w) - 3) if tuple(w[i:i + 4]) in G]
assert not bad, bad

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
    h += '<div class="head"><div><h1>중산중3 7·8과 서술형 최종 점검%s</h1><div class="sub">지학사(민찬규) Lesson 7·8 본문 + 외부지문(일본 가옥 · Picture Bride) · 10문항</div></div>' % (' — 정답과 채점 포인트' if answer else '')
    h += '<div class="who"><span>번호</span><span>이름</span></div></div>' if not answer else '</div>'
    if not answer: h += '<div class="note">본문에서 문법이 가장 많이 걸린 문장만 골랐어요. 조건(단어 수·형태 변화)을 끝까지 지키고, 대소문자·마침표까지 정확히 쓰세요.</div>'
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
    h += '<div class="s cover"><h1>7·8과 서술형 최종 점검</h1><p>중산중 3학년 · 본문 + 외부지문 · 10문항</p><p style="margin-top:30px;font-size:20px">문제 → 다음 장 정답</p></div>'
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
            hp = '/home/claude/work/m3sw_%s.html' % name; open(hp, 'w', encoding='utf-8').write(doc)
            pg.goto('file://' + hp); pg.wait_for_timeout(1200)
            if name == '서술형_화면용': pg.pdf(path=OUT + '중산중3_7·8과_' + name + '.pdf', width='1280px', height='720px', print_background=True)
            else: pg.pdf(path=OUT + '중산중3_7·8과_' + name + '.pdf', format='A4', print_background=True, prefer_css_page_size=True)
        b.close()
    print('ok')
