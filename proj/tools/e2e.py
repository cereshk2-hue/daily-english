# 끝까지 풀어보는 자동 테스트: DAY1 전부 정답, DAY2 일부러 몇 개 틀리고 복습까지
import subprocess, time, sys, json
from playwright.sync_api import sync_playwright
srv=subprocess.Popen([sys.executable,'-m','http.server','8765','-d','dist/github/'+(sys.argv[1] if len(sys.argv)>1 else 'm1-chunjae-L6-2hmac')],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL); time.sleep(1)
SH='/tmp/claude-0/shots/'+(sys.argv[1] if len(sys.argv)>1 else 'm1-chunjae-L6')+'_'
errs=[]
def solve(pg, wrong=False):
    rs=pg.evaluate('__dbg()'); q=rs['qs'][rs['qi']]; t=q['t']
    if t in('choice','pick'):
        ans=q['ans']; opts=q['opts']; i=opts.index(ans)
        if wrong: i=(i+1)%len(opts)
        pg.locator('.opt').nth(i).click()
    elif t=='tf': pg.locator('.opt[data-v="%d"]'%(int(q['ans'])^int(wrong))).click()
    elif t=='verb': pg.fill('#vin', 'zzz' if wrong else q['a'][0]); pg.click('#vf button')
    elif t in('insert','odd'): pg.locator('#qcard [data-m="%d"]'%((q['ans']+1)%2 if wrong else q['ans'])).click()
    elif t=='error': pg.locator('.mark[data-m="%d"]'%((q['w']+1)%3 if wrong else q['w'])).click()
    elif t in('order','scramble'):
        n=len(q['pool']); order=list(range(n))
        if wrong: order=order[::-1]
        for j in order: pg.locator('#pool .chip[data-j="%d"]'%j).click()
        pg.click('#chk')
    return t
try:
  with sync_playwright() as p:
      b=p.chromium.launch(); pg=b.new_page(viewport={'width':390,'height':844},device_scale_factor=2,user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X)')
      pg.on('pageerror',lambda e:errs.append(str(e))); pg.on('console',lambda m: m.type=='error' and errs.append(m.text))
      pg.goto('http://localhost:8765/?test'); pg.screenshot(path=SH+'1_home.png',full_page=True)
      pg.fill('#nm','김민준'); pg.click('#nameform button'); ND=pg.evaluate('PKG.days.length')
      for di,wrong_every in [(0,0),(1,4),(2,0),(3,0),(4,0),(5,0)][:ND]:
          if pg.locator('#quit').count(): pg.click('#quit')
          if not pg.locator('[data-go="%d"]'%di).count(): pg.locator('[data-sel="%d"]'%di).first.click()  # 모의고사: 번호 먼저 고르기
          pg.locator('[data-go="%d"]'%di).first.click(); k=0; shot=set()
          while True:
              rs=pg.evaluate('__dbg()')
              if rs is None: break
              if rs['phase']=='study':
                  if di==0 and 'study' not in shot: pg.screenshot(path=SH+'2_study.png'); shot.add('study')
                  pg.click('#gostart'); continue
              if rs['phase']=='summary':
                  if pg.locator('#tores').count(): pg.click('#tores'); break
                  if pg.locator('#toreview').count():
                      pg.click('#toreview'); n=0; rw=0
                      while pg.evaluate('__dbg()')['phase']!='summary':
                          n+=1; w = n in (2,5) and di==1; rw+=w; solve(pg,w); pg.click('#nx')
                          if di==1 and n==3:
                              pg.click('#quit'); print('home during review:', pg.locator('.status').first.inner_text()); (pg.locator('[data-rev="1"]').count() or pg.locator('[data-sel="1"]').first.click()); pg.locator('[data-rev="1"]').first.click()
                      print('review answered',n,'(wrong again',rw,')'); pg.click('#back'); break
                  pg.click('#tonext'); continue
              k+=1; wrong= wrong_every and k%wrong_every==0
              if di==0 and k==20:
                  before=(rs['si'],rs['qi']); pg.click('#quit'); pg.reload()
                  print('resume status:', pg.locator('.status').first.inner_text())
                  (pg.locator('[data-go="0"]').count() or pg.locator('[data-sel="0"]').first.click()); pg.locator('[data-go="0"]').first.click(); r2=pg.evaluate('__dbg()'); print('resume', before, '->', (r2['si'],r2['qi'])); assert before==(r2['si'],r2['qi'])
              t=solve(pg,wrong)
              if di==0 and t not in shot: pg.screenshot(path=SH+'3_%s.png'%t); shot.add(t)
              pg.click('#nx')
          assert pg.locator('#sms').count(), 'no result page'
          print('DAY',di+1,'score text:',pg.locator('.rc-score').first.inner_text().replace('\n',' '))
      href=pg.get_attribute('#sms','href'); print('sms href starts:',href[:30]); 
      import urllib.parse; print('--- message ---'); print(urllib.parse.unquote(href.split('body=')[1]))
      pg.screenshot(path=SH+'4_result.png',full_page=True)
      # 복습
      print('send buttons:', pg.locator('#kakao').count(), pg.locator('#sms').count()); pg.click('#quit')
      # 새로고침 후 진행 유지
      pg.reload(); print('home status:', [s.inner_text() for s in pg.locator('.status').all()])
      pg.click('[data-tab="text"]'); pg.click('[data-sel="1"]'); pg.screenshot(path=SH+'5_passage.png')
      pg.click('[data-tab="types"]'); pg.screenshot(path=SH+'7_types.png')
      pg.click('[data-free="8"]'); n=0
      while pg.evaluate('__dbg()')['phase']!='summary':
          solve(pg); pg.click('#nx'); n+=1
      print('free practice', n, 'back btn', pg.locator('#back').count()); pg.click('#back'); print('tab after back:', pg.locator('.tabs .on').inner_text())
      pg.emulate_media(color_scheme='dark'); pg.screenshot(path=SH+'6_dark.png')
      b.close()
finally:
  srv.terminate()
print('errors:',errs or 'none')
