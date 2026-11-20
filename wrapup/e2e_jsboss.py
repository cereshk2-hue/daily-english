import subprocess,time,sys,json
from playwright.sync_api import sync_playwright
port='8796'; folder=[l for l in __import__('os').listdir('/home/claude/proj/dist/github') if l.startswith('h2-mock-2609-jungsan')][0]
srv=subprocess.Popen([sys.executable,'-m','http.server',port,'-d','/home/claude/proj/dist/github/'+folder],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL); time.sleep(1)
res=[]
try:
  with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':390,'height':844}); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('http://localhost:%s/?test'%port); pg.fill('#nm','검수'); pg.click('#nameform button'); pg.wait_for_timeout(700)
    print(pg.eval_on_selector_all('[data-tab]','e=>e.map(x=>x.dataset.tab+":"+x.textContent)'))
    pg.screenshot(path='/home/claude/work/jbb_nav.png')
    T=pg.evaluate('PKG.tests.map((t,ti)=>({ti:ti,id:t.id,kind:t.kind,items:t.items.map(i=>({n:i.n,ans:i.ans,bl:(i.blanks||[]).map(b=>b.ans[0])}))})).filter(t=>t.kind==="boss")')
    for t in T:
        for mode in ('right','wrong'):
            if mode=='wrong' and t['id']!='boss2609e': continue
            pg.goto('http://localhost:%s/?test'%port); pg.wait_for_timeout(400)
            pg.locator('[data-tab="boss"]').click(); pg.wait_for_timeout(300)
            if mode=='right': pg.locator('[data-tgo2="%d"]'%t['ti']).click()
            else: pg.locator('[data-tgo2="%d"]'%t['ti']).click()
            pg.wait_for_timeout(400)
            if t['id']=='boss2609e' and mode=='right': pg.screenshot(path='/home/claude/work/jbb_omr.png',full_page=True)
            for k,it in enumerate(t['items']):
                if it['bl']:
                    for inp,v in zip(pg.locator('#tq%d input'%k).all(),it['bl']): inp.fill(v)
                else:
                    A=it['ans'] if isinstance(it['ans'],list) else [it['ans']]
                    if mode=='wrong' and isinstance(it['ans'],list): A=A[:-1]   # 하나 빠뜨리기
                    if isinstance(it['ans'],list):   # 일부러 엉뚱한 것 눌렀다 풀기
                        extra=[i for i in range(5) if i not in A][0]; pg.locator('#tq%d .bub'%k).nth(extra).click(); pg.locator('#tq%d .bub'%k).nth(extra).click()
                    for a in A: pg.locator('#tq%d .bub'%k).nth(a).click()
            pg.click('#tsubmit'); pg.wait_for_timeout(300)
            if pg.locator('#tsubmit').count(): pg.click('#tsubmit')
            pg.wait_for_timeout(700)
            res.append((t['id'],mode,pg.locator('.tres').inner_text().replace('\n',' ')[:150]))
            if t['id']=='boss2609e' and mode=='right': pg.screenshot(path='/home/claude/work/boss_res.png',full_page=True)
    print(errs); b.close()
finally: srv.terminate()
for r in res: print(r)
