from playwright.sync_api import sync_playwright
T=[('3031','30·31'),('3233','32·33'),('3435','34·35'),('3637','36·37'),('3839','38·39'),('4042','40·41~42')]
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1100,'height':1400})
    for t,nm in T:
        pg.goto('file:///home/claude/work/wrapup/pub-%s.html'%t); pg.wait_for_timeout(1500)
        # 칸 안에서 잘린 내용이 없는지 확인
        clip=pg.evaluate("[...document.querySelectorAll('.cols > .col')].filter(c=>c.scrollHeight>c.clientHeight+2).length")
        pg.emulate_media(media='print')
        pg.pdf(path='/home/claude/work/wu_e2e/9월학평_%s번_Wrap-up.pdf'%nm,format='A4',print_background=True,prefer_css_page_size=True)
        pg.emulate_media(media='screen')
        print(t,'clipped cols:',clip)
    b.close()
