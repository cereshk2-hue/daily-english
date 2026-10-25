from playwright.sync_api import sync_playwright
import json
U='http://localhost:8768/m1-chunjae-L6-2hmac/?test'
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':390,'height':900}); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto(U); pg.evaluate("localStorage.clear()"); pg.reload(); pg.wait_for_timeout(300)
    pg.fill('#nm','이지혁'); pg.click('#nameform button[type=submit]'); pg.wait_for_timeout(200)
    st=pg.evaluate("JSON.parse(localStorage.getItem('daily:m1-chunjae-so-L6:이지혁'))")
    n=13; sc={str(i):[5,5] for i in range(n)}; sc['9']=[0,2]; sc['4']=[3,8]
    st['days']['d1']={'scores':sc,'wrong':{},'started':1,'finished':1761370000000,'run':None,'reviewDone':None,'titles':pg.evaluate('PKG.days[0].steps.map(x=>x.title)')}
    pg.evaluate("s=>localStorage.setItem('daily:m1-chunjae-so-L6:이지혁',JSON.stringify(s))", st); pg.reload(); pg.wait_for_timeout(400)
    print(pg.inner_text('.day .status'));el=pg.query_selector('.weakbox'); print('weakbox:', el.inner_text() if el else None)
    pg.query_selector('.day').screenshot(path='/tmp/claude-0/-home-claude/a9e3e882-1f02-5d62-8f70-aced81bc59d2/scratchpad/weak.png')
    pg.click('[data-weak="0:9"]'); pg.wait_for_timeout(300)
    print('crumb:', pg.inner_text('.crumb') if pg.query_selector('.crumb') else pg.inner_text('body')[:100])
    print(errs)
