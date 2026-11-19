import subprocess,time,sys,re
from playwright.sync_api import sync_playwright
port='8797'
srv=subprocess.Popen([sys.executable,'-m','http.server',port,'-d','/home/claude/proj/dist/github/h1-mock-2610-jeodong-9bxzm'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL); time.sleep(1)
# 서술형 입력: 정답표 첫 답 대신 일부러 다른 허용 답을 넣어 보는 문항
ALT0={('m2d7-01','서술형 20'):['is important to drink a lot of water','It is hard to live without a smartphone.'],
     ('m2d7-07','서술형 19'):['It is important to eat breakfast.'],
     ('m2d7-07','서술형 20'):['strong','healthily → healthy'],
     ('m2d7-04','서술형 19'):["It isn’t possible to run faster than reindeer."],
     ('m2d7-08','서술형 20'):['My classmates and I name our team "The Winners"'],
     ('m2d7-06','서술형 18'):['Until then']}
res=[]
try:
  with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':390,'height':844}); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('http://localhost:%s/?test'%port); pg.fill('#nm','검수'); pg.click('#nameform button'); pg.wait_for_timeout(700)
    print(pg.eval_on_selector_all('[data-tab]','e=>e.map(x=>x.dataset.tab+":"+x.textContent)'))
    T=pg.evaluate('PKG.tests.map(t=>({id:t.id,kind:t.kind||"",items:t.items.map(i=>({n:i.n,ans:i.ans,bl:(i.blanks||[]).map(b=>b.ans[b.ans.length>1?1:0])}))}))')
    for ti,t in enumerate(T):
        if t['kind']!='boss': continue
        pg.goto('http://localhost:%s/?test'%port); pg.wait_for_timeout(500)
        pg.locator('[data-tab="%s"]'%('boss' if t['kind']=='boss' else 'test')).click(); pg.wait_for_timeout(300)
        pg.locator('[data-tgo2="%d"]'%ti).click(); pg.wait_for_timeout(400)
        for k,it in enumerate(t['items']):
            if pg.locator('#tq%d .bub'%k).count(): pg.locator('#tq%d .bub'%k).nth(it['ans']).click()
            else:
                vals=it['bl']
                ins=pg.locator('#tq%d input'%k).all(); assert len(ins)==len(it['bl']),(t['id'],it['n'],len(ins))
                for inp,v in zip(ins,vals): inp.fill(v)
        pg.click('#tsubmit'); pg.wait_for_timeout(300)
        if pg.locator('#tsubmit').count(): pg.click('#tsubmit')
        pg.wait_for_timeout(700)
        txt=pg.locator('.tres').inner_text().replace('\n',' ')
        res.append((t['id'],txt[:90]))
        
    print(errs)
    b.close()
finally: srv.terminate()
for r in res: print(r)
