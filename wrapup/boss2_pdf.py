from playwright.sync_api import sync_playwright
import glob
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page()
    for n in (1,2,3):
        for kind,ko in (('student','시험지'),('teacher','정답해설')):
            pg.goto('file:///home/claude/work/wrapup/boss2/boss%d-%s.html'%(n,kind)); pg.wait_for_timeout(1500)
            nums={1:'19·20',2:'21·22',3:'23·24'}[n]
            pg.pdf(path='/home/claude/work/wrapup/boss2/고2_요약문끝판왕%d_%s번_%s.pdf'%(n,nums,ko),format='A4',print_background=True,prefer_css_page_size=True)
    b.close()
