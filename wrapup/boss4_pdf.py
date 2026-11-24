# 11/23 중산고1 요약문 끝판왕 7~10 시험지·정답해설 PDF (boss4_build.py가 만든 HTML)
from playwright.sync_api import sync_playwright
NUMS = {5: '31·32', 6: '33·34', 7: '35·36', 8: '37·38', 9: '39·40', 10: '41~42'}   # 11/24 5·6도
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page()
    for n, nums in NUMS.items():
        for kind, ko in (('student', '시험지'), ('teacher', '정답해설')):
            pg.goto('file:///home/claude/work/wrapup/boss4/boss%d-%s.html' % (n, kind)); pg.wait_for_timeout(1500)
            pg.pdf(path='/home/claude/work/wrapup/boss4/중산고1_요약문끝판왕%d_%s번_%s.pdf' % (n, nums, ko), format='A4', print_background=True, prefer_css_page_size=True)
    b.close()
