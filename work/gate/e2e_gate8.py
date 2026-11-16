import subprocess, time, sys
from playwright.sync_api import sync_playwright
srv=subprocess.Popen([sys.executable,'-m','http.server','8835','-d','/home/claude/proj/dist/github/m2-visang-hwang-L7-x1iso'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL); time.sleep(1)
SH='/tmp/pv/gate_'; errs=[]
def choose(pg, q, wrong_first=False):
    k=0
    for pi,p in enumerate(q['parts']):
        for si,sg in enumerate(p['segs']):
            if 'opts' not in sg: continue
            o=sg['opts'].index(sg['ans'])
            if wrong_first and k==0: o=1-o
            pg.locator('.gb[data-g="%d:%d"] .gopt[data-o="%d"]'%(pi,si,o)).click(); k+=1
try:
  with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':390,'height':844},device_scale_factor=2)
    pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('http://localhost:8835/?test'); pg.fill('#nm','테스트'); pg.click('#nameform button')
    di=19
    if not pg.locator('[data-go="%d"]'%di).count(): pg.locator('[data-sel="%d"]'%di).first.click()
    pg.locator('[data-go="%d"]'%di).first.click()
    rs=pg.evaluate('__dbg()')
    if rs['phase']=='study': pg.click('#gostart')
    time.sleep(0.5); pg.screenshot(path=SH+'1play.png',full_page=True)
    # 덩이 1: 3번 틀리기
    for t in range(3):
        q=pg.evaluate('__dbg()')['qs'][0]; time.sleep(0.4); choose(pg,q,True); pg.click('#gchk'); time.sleep(0.4)
        if t==0: pg.screenshot(path=SH+'2fail.png',full_page=True); print('msg:',pg.inner_text('#gmsg')[:80]); print('any right/wrong shown:',pg.locator('.gopt.right,.gopt.wrong').count())
    print('review sentences:',pg.locator('.gs').count(),'gre disabled:',pg.locator('#gre').is_disabled())
    pg.screenshot(path=SH+'3review.png',full_page=True)
    q=pg.evaluate('__dbg()')['qs'][0]
    for g in pg.locator('.gb').all():
        pi,si=map(int,g.get_attribute('data-g').split(':')); sg=q['parts'][pi]['segs'][si]; o=sg['opts'].index(sg['ans'])
        g.locator('.gopt[data-o="%d"]'%(1-o)).click(); g.locator('.gopt[data-o="%d"]'%o).click()
    pg.screenshot(path=SH+'4review_done.png',full_page=True); print('gre enabled:',pg.locator('#gre').is_enabled())
    pg.click('#gre'); time.sleep(0.5)
    q=pg.evaluate('__dbg()')['qs'][0]; print('round',q['round'],'tries',q['tries'],'phase',q['phase'])
    time.sleep(0.4); choose(pg,q); pg.click('#gchk'); time.sleep(0.5); pg.screenshot(path=SH+'5pass.png',full_page=True)
    print('fb:',pg.inner_text('#fb')[:120].replace('\n',' '))
    time.sleep(0.6); pg.click('#nx'); time.sleep(0.5)
    q=pg.evaluate('__dbg()')['qs'][1]; time.sleep(0.4); choose(pg,q); pg.click('#gchk'); time.sleep(0.6); pg.click('#nx'); time.sleep(0.6)
    rs=pg.evaluate('__dbg()'); print('phase',rs and rs['phase'])
    pg.screenshot(path=SH+'6summary.png',full_page=True)
    print('score:',pg.locator('.rc-score').first.inner_text().replace('\n',' ') if pg.locator('.rc-score').count() else '-')
    b.close()
finally: srv.terminate()
print('errors:',errs or 'none')
