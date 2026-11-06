import time,re
from playwright.sync_api import sync_playwright
h=open('out_report.html').read().replace('https://cdn.jsdelivr.net/npm/html-to-image@1.11.13/dist/html-to-image.js','/opt/npm-tools/node_modules/html-to-image/dist/html-to-image.js')
open('t_report.html','w').write(h)
with sync_playwright() as p:
  b=p.chromium.launch()
  for w,name in [(390,'mobile'),(1100,'pc')]:
    pg=b.new_page(viewport={'width':w,'height':900},device_scale_factor=1)
    errs=[];pg.on('pageerror',lambda e:errs.append(str(e)));pg.on('console',lambda m:m.type=='error' and errs.append(m.text))
    pg.goto('file:///home/claude/work/report/t_report.html');time.sleep(1)
    pg.screenshot(path='r_%s.png'%name,full_page=True)
    if name=='mobile':
      pg.fill('#goal','DAY 10~13 완료, 오답 0개');pg.click('#save');time.sleep(.3);print('saved',pg.evaluate('window.__saved'),pg.inner_text('#msg'))
      pg.click('#img');pg.wait_for_selector('#ov img',timeout=15000);time.sleep(.5)
      src=pg.get_attribute('#ov img','src');import base64;open('r_img.png','wb').write(base64.b64decode(src.split(',')[1]))
      pg.click('#ovx');pg.click('#all');pg.wait_for_function("document.querySelectorAll('#ov img').length>=2",timeout=30000);print('all imgs',pg.eval_on_selector_all('#ov img','e=>e.length'))
    print(name,errs)
  bp=b.new_page(viewport={'width':390,'height':900});bp.goto('file:///home/claude/work/report/out_board.html');time.sleep(.8)
  print('board rpt href',bp.get_attribute('#rpt','href'),bp.eval_on_selector_all('a.tag','e=>e.map(x=>x.href).slice(0,2)'))
  bp.screenshot(path='r_board.png')
  b.close()
