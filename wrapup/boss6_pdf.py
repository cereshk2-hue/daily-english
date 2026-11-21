# 11/21 대진고2 요약문 끝판왕 1~10 시험지·정답해설 PDF
from playwright.sync_api import sync_playwright
from boss6_data import SETS
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page()
    for S in SETS:
        n = S['no']; nums = S['nums'][0] if S['nums'][0] == S['nums'][1] else '%s·%s' % S['nums']
        for kind, ko in (('student', '시험지'), ('teacher', '정답해설')):
            pg.goto('file:///home/claude/work/wrapup/boss6/boss%d-%s.html' % (n, kind)); pg.wait_for_timeout(1500)
            pg.pdf(path='/home/claude/work/wrapup/boss6/대진고2_요약문끝판왕%d_%s번_%s.pdf' % (n, nums, ko), format='A4', print_background=True, prefer_css_page_size=True)
    b.close()
