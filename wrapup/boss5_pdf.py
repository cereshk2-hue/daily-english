# 11/20 중산고2 요약문 끝판왕 4~10 시험지·정답해설 PDF (boss5_build.py가 만든 HTML)
from playwright.sync_api import sync_playwright
from boss5_data import SETS
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page()
    for S in SETS:
        n = S['no']; nums = '%s·%s' % S['nums']
        for kind, ko in (('student', '시험지'), ('teacher', '정답해설')):
            pg.goto('file:///home/claude/work/wrapup/boss5/boss%d-%s.html' % (n, kind)); pg.wait_for_timeout(1500)
            pg.pdf(path='/home/claude/work/wrapup/boss5/중산고2_요약문끝판왕%d_%s번_%s.pdf' % (n, nums, ko), format='A4', print_background=True, prefer_css_page_size=True)
    b.close()
