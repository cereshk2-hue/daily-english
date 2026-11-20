# 백지노트 PDF 만들기 (11/20 선생님 "너무 좋아 이렇게 기억해줘")
# 사용: python3 baekji_note.py 제목 출력.pdf  ← 문장 목록 S = [(영어, 해석), ...] 을 아래 load()에서 바꿔 끼움
# 형식: A4 · 1~2쪽 문장마다 [번호 | 왼쪽 본문(세리프) | 오른쪽 해석] + 아래 점선 2줄(문법·구문 메모)
#       마지막 쪽: 내용 정리(흐름) 칸 · 핵심 문법 정리표(문법 이름만, 예문·함정 칸 비움) · 어휘·숙어 칸 · 서술형 대비 칸
# 템플릿 원본: print/m3rf7_baekji.html (중산중3 L7 외부지문)
import sys, html
def build(title, sub, S, flow, grams):
    esc = html.escape
    rows = ''.join('<tr class="s"><td class="no">%d</td><td class="en">%s</td><td class="ko">%s</td></tr><tr class="memo"><td></td><td colspan="2"><div class="ln"></div><div class="ln"></div></td></tr>' % (i + 1, esc(e), esc(k)) for i, (e, k) in enumerate(S))
    tpl = open('/home/claude/srcrepo/print/m3rf7_baekji.html', encoding='utf-8').read()
    head = tpl[:tpl.index('<body>') + 6]
    gt = ''.join('<tr><td>%s</td><td></td><td></td></tr>' % esc(g) for g in grams + [''])
    body = tpl[tpl.index('<body>') + 6:]
    body = body[:body.index('<table><tr><th></th>')]
    import re
    body = re.sub(r'<h1>.*?</h1>', '<h1>%s <small>백지노트</small></h1>' % esc(title), body)
    body = re.sub(r'<p class="sub">.*?</p>', '<p class="sub">%s</p>' % esc(sub), body)
    tail = tpl[tpl.index('<div class="pg"></div>'):]
    tail = re.sub(r'(<h2>내용 정리 — 흐름 \().*?(\)</h2>)', lambda m: m.group(1) + esc(flow) + m.group(2), tail)
    tail = re.sub(r'(<tr><th style="width:24%">문법</th>.*?</tr>).*?(</table>)', lambda m: m.group(1) + gt + m.group(2), tail, flags=re.S)
    return head.replace('<title>중산중3 L7 외부지문 백지노트</title>', '<title>%s 백지노트</title>' % esc(title)) + body + '<table><tr><th></th><th>본문</th><th>해석</th></tr>' + rows + '</table>' + tail
def pdf(htmlstr, out):
    from playwright.sync_api import sync_playwright
    open('/tmp/_baekji.html', 'w', encoding='utf-8').write(htmlstr)
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(); pg.goto('file:///tmp/_baekji.html'); pg.wait_for_timeout(800)
        pg.pdf(path=out, format='A4', print_background=True, prefer_css_page_size=True); b.close()
