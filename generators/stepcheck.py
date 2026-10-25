import sys,subprocess,time
from playwright.sync_api import sync_playwright
folder=sys.argv[1]; days=[int(x) for x in sys.argv[2].split(',')]
srv=subprocess.Popen(['python3','-m','http.server','8790','-d','/home/claude/proj/dist/github'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL); time.sleep(1)
def solve(pg):
    rs=pg.evaluate('__dbg()'); q=rs['qs'][rs['qi']]; t=q['t']
    if t in('choice','pick'): pg.locator('#qcard .opt').nth(q['opts'].index(q['ans'])).click()
    elif t=='tf': pg.locator('.opt[data-v="%d"]'%int(q['ans'])).click()
    elif t=='verb': pg.fill('#vin', q['a'][0]); pg.click('#vf button')
    elif t in('insert','odd'): pg.locator('#qcard [data-m="%d"]'%q['ans']).click()
    elif t=='error': pg.locator('.mark[data-m="%d"]'%q['w']).click()
    elif t in('order','scramble'):
        for j in range(len(q['pool'])): pg.locator('#pool .chip[data-j="%d"]'%j).click()
        pg.click('#chk')
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(); e=[]; pg.on('pageerror',lambda x:e.append(str(x)))
    pg.goto(f'http://localhost:8790/{folder}/?test'); pg.evaluate('localStorage.clear()'); pg.reload(); pg.wait_for_timeout(300)
    pg.fill('#nm','김민준'); pg.click('#nameform button[type=submit]'); pg.wait_for_timeout(200)
    for di in days:
        ns=pg.evaluate(f'PKG.days[{di}].steps.length'); tot=0; ok=0
        for si in range(ns):
            pg.click('[data-tab="types"]'); pg.click(f'[data-sel="{di}"]'); pg.click(f'[data-free="{si}"]'); pg.wait_for_timeout(100)
            while True:
                rs=pg.evaluate('__dbg()')
                if rs['phase']=='study': pg.click('#gostart'); continue
                if rs['phase']=='summary': break
                solve(pg); tot+=1; ok+= pg.locator('.feedback.ok').count(); pg.click('#nx'); pg.wait_for_timeout(30)
            pg.click('#back'); pg.wait_for_timeout(50)
        print('DAY',di+1,'correct',ok,'/',tot)
    print('errors',e)
srv.kill()
