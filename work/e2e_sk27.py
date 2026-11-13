import subprocess, time, sys
from playwright.sync_api import sync_playwright
srv=subprocess.Popen([sys.executable,'-m','http.server','8812','-d','/home/claude/proj/dist/github/h3-sk27-eng-53nx4'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL); time.sleep(1)
SH='/home/claude/work/shots_sk27_'; errs=[]
def solve(pg):
    rs=pg.evaluate('__dbg()'); q=rs['qs'][rs['qi']]; t=q['t']
    if t in('choice','pick'): pg.locator('.opt').nth(q['opts'].index(q['ans'])).click()
    elif t=='tf': pg.locator('.opt[data-v="%d"]'%int(q['ans'])).click()
    elif t=='verb': pg.fill('#vin', q['a'][0]); pg.click('#vf button')
    elif t in('insert','odd'): pg.locator('#qcard [data-m="%d"]'%q['ans']).click()
    elif t=='error': pg.locator('.mark[data-m="%d"]'%q['w']).click()
    elif t in('order','scramble'):
        for j in range(q.get('need') or len(q['pool'])): pg.locator('#pool .chip[data-j="%d"]'%j).click()
        pg.click('#chk')
    elif t=='hunt':
        for i,w in enumerate(q['toks']):
            if w.get('e') is not None: pg.locator('.hw[data-h="%d"]'%i).click()
        pg.click('#hchk')
        for j,e in enumerate(q['errs']): pg.fill('[data-f="%d"]'%j, e['ok'])
        pg.screenshot(path=SH+'hunt_fix.png',full_page=True)
        pg.click('#hchk')
    return q
try:
  with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':390,'height':844},device_scale_factor=2)
    pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('http://localhost:8812/?test'); pg.fill('#nm','테스트'); pg.click('#nameform button')
    for di in range(0,6):
        if pg.locator('#quit').count(): pg.click('#quit')
        if not pg.locator('[data-go="%d"]'%di).count(): pg.locator('[data-sel="%d"]'%di).first.click()
        pg.locator('[data-go="%d"]'%di).first.click(); n=0; shot=set()
        while True:
            rs=pg.evaluate('__dbg()')
            if rs is None: break
            if rs['phase']=='study': pg.click('#gostart'); continue
            if rs['phase']=='summary':
                if pg.locator('#tores').count(): pg.click('#tores'); break
                pg.click('#tonext'); continue
            q=rs['qs'][rs['qi']]; key=(q['t'], bool(q.get('ko')), bool(q.get('num')))
            if key not in shot and (q.get('num') or q.get('ko') or q['t'] in ('scramble','insert','hunt')):
                pg.screenshot(path=SH+'d%d_%s%s%s.png'%(di+1,q['t'],'_ko' if q.get('ko') else '','_num' if q.get('num') else ''),full_page=True); shot.add(key)
            time.sleep(0.4); solve(pg); n+=1; time.sleep(0.55); pg.click('#nx')
        print('DAY',di+1,pg.locator('.rc-score').first.inner_text().replace('\n',' '), 'answered',n)
    b.close()
finally: srv.terminate()
print('errors:',errs or 'none')
