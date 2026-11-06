from playwright.sync_api import sync_playwright
import time
h=open('out_report2.html').read().replace('https://cdn.jsdelivr.net/npm/html-to-image@1.11.13/dist/html-to-image.js','/opt/npm-tools/node_modules/html-to-image/dist/html-to-image.js')
open('t_report2.html','w').write(h)
with sync_playwright() as p:
  b=p.chromium.launch()
  pg=b.new_page(viewport={'width':390,'height':900});pg.on('pageerror',lambda e:print('ERR',e))
  pg.goto('file:///home/claude/work/report/t_report2.html');time.sleep(1)
  print('cur',pg.inner_text('.ppl button.on'),'| prev',pg.get_attribute('#prev','href')[-60:])
  pg.fill('#find','이준');time.sleep(.3);print('after search',pg.inner_text('.ppl'),'|',pg.inner_text('.who b'))
  print('next href',pg.get_attribute('#next','href')[-70:])
  pg.fill('#find','');pg.fill('#find','없는');time.sleep(.2);print(pg.inner_text('.ppl'))
  pg.fill('#find','박');pg.press('#find','Enter');time.sleep(.3)
  pg.screenshot(path='r2_mobile.png',full_page=True)
  pg.click('#img');pg.wait_for_selector('#ov img',timeout=15000);print('dl',pg.get_attribute('#ov a','download'))
  src=pg.get_attribute('#ov img','src');import base64;open('r2_img.png','wb').write(base64.b64decode(src.split(',')[1]))
  b.close()
