from playwright.sync_api import sync_playwright
U='http://localhost:8767/m1-chunjae-L6-2hmac/'
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
    # legacy record
    pg.goto(U); pg.evaluate("localStorage.clear(); localStorage.setItem('daily:m1-chunjae-so-L6', JSON.stringify({name:'옛학생',days:{d1:{scores:{0:[10,15]},wrong:{},started:1,finished:null,run:null}}}))")
    pg.reload(); pg.wait_for_timeout(500)
    print('legacy who:', pg.inner_text('.who .name') if pg.query_selector('.who .name') else None, pg.evaluate("Object.keys(localStorage)"))
    print('status1', pg.inner_text('.day .status'))
    pg.click('#rename'); pg.wait_for_timeout(200)
    print('chips', pg.eval_on_selector_all('[data-who]','e=>e.map(x=>x.textContent)'))
    pg.fill('#nm','김민준'); pg.click('#nameform button[type=submit]'); pg.wait_for_timeout(300)
    print('now', pg.inner_text('.who .name'), pg.inner_text('.day .status'))
    pg.click('[data-go="0"]'); pg.wait_for_timeout(1500)
    pg.goto(U); pg.wait_for_timeout(500)
    print('picker after reload (2 names):', pg.eval_on_selector_all('[data-who]','e=>e.map(x=>x.textContent)'))
    pg.click('[data-who="옛학생"]'); pg.wait_for_timeout(300); print('picked', pg.inner_text('.who .name'), pg.inner_text('.day .status'))
    pg.click('#rename'); pg.click('[data-unwho="옛학생"]'); pg.click('[data-unwho="옛학생"]'); pg.wait_for_timeout(200)
    print('after drop', pg.eval_on_selector_all('[data-who]','e=>e.map(x=>x.textContent)'))
    pg.goto(U); pg.wait_for_timeout(500); print('auto (1 name):', pg.inner_text('.who .name'))
    print('outbox', pg.evaluate("localStorage.getItem('daily:outbox')"), errs)
