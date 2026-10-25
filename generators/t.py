from playwright.sync_api import sync_playwright
import os
dirs=[d for d in sorted(os.listdir('.')) if os.path.isdir(d) and not d.startswith('.') and not d.startswith('t-')]
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(); errs=[]
    pg.on('pageerror',lambda e:errs.append(str(e)))
    for d in dirs:
        pg.goto(f'http://localhost:8765/{d}/'); pg.wait_for_timeout(400)
        print(d, pg.title(), len(pg.inner_text('body')))
    print('errors',errs)
