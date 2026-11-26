import subprocess,time,sys,json
from playwright.sync_api import sync_playwright
# 사용: e2e_tests_ids.py <포트> <폴더 앞부분> <탭> <id,id,…>  (11/24 시험 id 지정 E2E)
port=sys.argv[1]; folder=[l for l in __import__('os').listdir('/home/claude/proj/dist/github') if l.startswith(sys.argv[2]+'-')][0]; TAB=sys.argv[3]; IDS=sys.argv[4].split(',')
srv=subprocess.Popen([sys.executable,'-m','http.server',port,'-d','/home/claude/proj/dist/github/'+folder],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL); time.sleep(1)
res=[]
try:
  with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':390,'height':844}); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('http://localhost:%s/?test'%port); pg.fill('#nm','검수'); pg.click('#nameform button'); pg.wait_for_timeout(700)
    print(pg.eval_on_selector_all('[data-tab]','e=>e.map(x=>x.dataset.tab+":"+x.textContent)'))
    pg.screenshot(path='/home/claude/work/m1cx_nav.png')
    T=pg.evaluate('PKG.tests.map((t,ti)=>({ti:ti,id:t.id,kind:t.kind,items:t.items.map(i=>({n:i.n,ans:i.ans,bl:(i.blanks||[]).map(b=>b.ans[0])}))}))')
    T=[t for t in T if t["id"] in IDS]; assert len(T)==len(IDS), T
    for t in T:
        for mode in ('right','wrong'):
            if mode=='wrong' and t['id']!=IDS[0]: continue
            pg.goto('http://localhost:%s/?test'%port); pg.wait_for_timeout(400)
            pg.locator('[data-tab="%s"]'%TAB).click(); pg.wait_for_timeout(300)
            if mode=='right': pg.locator('[data-tgo2="%d"]'%t['ti']).click()
            else: pg.locator('[data-tgo2="%d"]'%t['ti']).click()
            pg.wait_for_timeout(400)
            if t['id']=='m1cx-1' and mode=='right': pg.screenshot(path='/home/claude/work/m1cx_omr.png',full_page=True)
            for k,it in enumerate(t['items']):
                if it['bl']:
                    for inp,v in zip(pg.locator('#tq%d input'%k).all(),it['bl']): inp.fill(v)
                else:
                    A=it['ans'] if isinstance(it['ans'],list) else [it['ans']]
                    if mode=='wrong' and k in (0,7): A=[(A[0]+1)%5]   # 하나 빠뜨리기
                    if isinstance(it['ans'],list):   # 일부러 엉뚱한 것 눌렀다 풀기
                        extra=[i for i in range(5) if i not in A][0]; pg.locator('#tq%d .bub'%k).nth(extra).click(); pg.locator('#tq%d .bub'%k).nth(extra).click()
                    for a in A: pg.locator('#tq%d .bub'%k).nth(a).click()
            pg.click('#tsubmit'); pg.wait_for_timeout(300)
            if pg.locator('#tsubmit').count(): pg.click('#tsubmit')
            pg.wait_for_timeout(700)
            res.append((t['id'],mode,pg.locator('.tres').inner_text().replace('\n',' ')[:150]))
            if t['id']=='m1cx-1' and mode=='wrong': pg.screenshot(path='/home/claude/work/m1cx_res.png',full_page=True)
    print(errs); b.close()
finally: srv.terminate()
for r in res: print(r)
